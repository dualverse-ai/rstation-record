# Conditional Sibling Decoupling and Micro-Horizon Weight Maximization in Forward-Only Transformer Credit Assignment

## 1. Introduction and Architectural Ledger

### 1.1 The Width-Scaling Variance Bottleneck in Forward-Only Credit
Eliminating the global reverse-depth sweep of backpropagation is a central pursuit in neuromorphic computing and biologically plausible credit assignment [1, 2, 8]. While standard reverse-mode automatic differentiation computes exact gradients in $\mathcal{O}(1)$ depth sweeps, it enforces global backward locking: no upstream layer can update its weights until the entire network forward graph has executed and downstream layers have finished their reverse-depth passes.

Forward perturbation methods avoid backward depth locking by perturbing hidden states during forward execution and correlating the resulting loss shifts with the injected noise [5, 6, 8, 12]. However, conventional forward perturbation rules face a severe **neuronal width-scaling bottleneck**:
- **Global Scalar-Reward Perturbation (`fwd_global_dust_K2`)**: Simultaneous zero-mean perturbation across all parameters or activations correlated with a single global scalar loss shift $\Delta \mathcal{L}$ yields estimator variance that scales with the total parameter count $\mathcal{O}(|\Theta| / K)$. In a 6-layer Transformer at $D=512$ ($M=2048$), relative variance at Layer 3 (`midMLP`) explodes to $3.26 \times 10^7$ (Table 3), stalling 200-step pretraining at $2.3898$ holdout BPB (Table 4) and 1000-step pretraining on `d6` ($D=384$) at $2.44794 \pm 0.11598$ holdout BPB (Table 5).
- **Token-Level Probing (`fwd_token_uwm_K2`)**: Evaluating per-token scalar rewards $\Delta \mathcal{L}_t \in \mathbb{R}$ isolates individual tokens, but shares a single scalar return across all $M = 4D$ sibling units in that sublayer. As Ren et al. [8] established, estimator variance scales as $\mathcal{O}(M / K)$, causing Layer 3 relative variance to grow from $26,968.01$ ($D=128$) to $103,931.10$ ($D=512$) (Table 3) and limiting 200-step holdout BPB to $2.1868$ at $D=512$ (Table 4) and 1000-step `d6` holdout BPB to $2.09816 \pm 0.00521$ (Table 5).

### 1.2 Stephen Chung's Foundations and Sylvester-Hadamard Coordination
To overcome this width bottleneck without a global backward pass, we adapt Stephen Chung's credit principles:
1. **Weight Maximization (`arXiv:2010.09770v3`) [2]**: Hidden units do not require an activation-space transpose circuit $(V^\top \delta_t)_i$. Instead, each unit $i$ observes only the plasticity displacement $\Delta \mathbf{v}^{(i)}$ of its own outgoing synaptic column $\mathbf{v}^{(i)} = V_{:, i}$, reinforcing activity when its outgoing column norm expands ($G^{(i)} = \mathbf{v}^{(i)} \cdot \Delta \mathbf{v}^{(i)}$).
2. **Unbiased Weight Maximization (`arXiv:2307.13270`) [3]**: Centered and antithetic exploration cancels zero-order norm biases, and difference-quotient path averaging evaluates non-linear activation credit without analytical backward derivatives.
3. **Structured Coordination [4] and Sylvester-Hadamard Exploration [11]**: Multi-agent exploration noise coordinated via orthogonal Sylvester-Hadamard matrices eliminates cross-agent exploration interference. Following Choromanski et al. [11] (`arXiv:1804.02395`), who proved variance reduction for orthogonal and Hadamard perturbation directions, we adapt Sylvester-Hadamard exploration codebooks to the $S$-token micro-horizon of parameter-space column contractions. This is conceptually distinct from Chung's Structured Coordination [4] (`arXiv:2307.13256`), which investigated recurrent networks of stochastic Boltzmann units coordinated via multi-agent reinforcement learning.
4. **MAP Propagation (`arXiv:2010.07893v2`) [1]**: Layers iteratively settle post-activation states $H^1(n) = \mu^1 + e_1(n)$ to minimize output discrepancy, damping credit through maximum a posteriori (MAP) prior precision.

### 1.3 Forward-Only Execution Taxonomy and Verified Cost Ledger
All candidate learning algorithms **eliminate the global reverse-depth backward phase**:
- `@torch.no_grad()` is enforced across all candidate model operations;
- `loss.backward()` and `torch.autograd.grad` are strictly forbidden (`num_backward_calls = 0`);
- No global backward computation graph is instantiated, and the forward pass count is fixed independent of width $M$ and depth $L$.
Backpropagation (`backprop`, `backprop_ckpt`) and block-detached autograd controls (`block_fixed_top_discrepancy_bp`, `block_local_greedy_bp_tophead`, `block_local_greedy_bp`, `block_local_greedy_bp_vsub256`) are included strictly as comparison baselines to isolate each step in the sequential ablation ladder.

We formulate two pure forward-only architectural paradigms:
- **Paradigm A: Two-Level Coordinated Weight Maximization (`fwd_two_level_cowm`)**: Combines parameter-space `Co-WM-S` column contraction on `lm_head` over micro-horizons of $S=8$ tokens, $2 K_{\text{net}}$ end-to-end antithetic full-network passes ($x_0 \to x_L$) with either depth-Hadamard carrier modulation (`net_carrier_mode="depth_hadamard"`) or independent per-probe carrier resampling (`net_carrier_mode="iid_resample"`), and intra-block parameter-space `Co-WM-S` on MLP projections ($W_1, V$) with head-decoupled forward FlashAttention probing on attention matrices ($W_Q, W_K, W_V, W_O$).
- **Paradigm B: Streaming Stagewise Forward Co-WM-S (`fwd_streaming_cowm`)**: Executes a single forward sweep through the network ($l = 0 \dots L-1$). At each block $l$:
  1. Forward output $x_l$ is evaluated and correlated with the language modeling target via an active sub-vocabulary projection ($V_{\text{sub}} = 256$ active tokens);
  2. Block $l$'s parameters ($W_Q, W_K, W_V, W_O, W_1, V$) compute gradients blockwise into `.grad`;
  3. **Block Deallocation**: All intermediate activations of block $l$ ($x_{\text{prev}}, x_{\text{attn\_in}}, u_{\text{attn}}, x_{\text{mlp\_in}}, u_{\text{mlp}}$) are **freed from GPU memory immediately** before block $l+1$ begins execution;
  4. The optimizer updates all parameters only after `execute_pure_forward_step` returns.

To construct a strictly unconfounded, 6-rung ablation ladder between end-to-end backpropagation and streaming `Co-WM-S`, we evaluate five intermediate reference packages:
1. **`block_fixed_top_discrepancy_bp` (Fixed Final-State Discrepancy + Detached Inter-Block Sublayers)**: Detaches residual stream inputs at each block boundary (`bwd_calls = 6`), evaluates the language modeling loss and `lm_head` update **exclusively at the final state $x_{L-1}$** (`w_stage = 1.0` on $L-1$, $0.0$ on $l < L-1$), and broadcasts the fixed final-state pre-norm discrepancy $\delta_{\text{final}} = \frac{\partial \mathcal{L}(x_{L-1})}{\partial x_{L-1}}$ directly into each detached block $l$ via the residual identity skip connection (`x_l.backward(delta_final)`). Comparing `backprop` to `block_fixed_top_discrepancy_bp` holds the downstream supervision discrepancy fixed at $\delta_{\text{final}}$ while replacing all intervening non-identity sublayer Jacobians ($l' > l$) with the identity residual path.
2. **`block_local_greedy_bp_tophead` (Intermediate Local Supervision + Final-Only Readout Update)**: Retains the detached block boundaries (`bwd_calls = 6`), exact intra-block autograd, full vocabulary ($V$), and final-only `lm_head` update (`w_stage = 1.0` on $L-1$, $0.0$ on $l < L-1$) of `block_fixed_top_discrepancy_bp`, but replaces the broadcast final-state discrepancy $\delta_{\text{final}}$ with each block's own intermediate local-loss discrepancy $\frac{\partial \mathcal{L}(x_l)}{\partial x_l}$.
3. **`block_local_greedy_bp` (Mixed-Readout Block-Detached Local Autograd [8])**: Identical to `block_local_greedy_bp_tophead`, except the shared `lm_head` accumulates $50\%$ of its gradient from the final block $L-1$ and $50\%$ uniformly across earlier blocks $l < L-1$ (`w_stage = 0.5 / (L-1)`), matching the readout update rule of `fwd_streaming_*`. (In Table 3, `block_local_greedy_bp_vsub256` additionally restricts the readout pullback to $V_{\text{sub}}=256$.)
4. **`fwd_streaming_oracle_fullvocab` (Full-Vocabulary Analytic-Linear Intra-Block Surrogate, $V_{\text{sub}}=0$)**: Retains the full vocabulary ($V$) and 50/50 `lm_head` mixture of `block_local_greedy_bp`, but replaces intra-block autograd with the streaming forward-only intra-block package: exact matrix transposes ($W_O^\top, V^\top$) for linear projections, linearized value-branch credit, directional RMSNorm pull, and $K_{\text{qk}}=2$ forward attention probes (`bwd_calls = 0`).
5. **`fwd_streaming_oracle` (Sub-Vocabulary Analytic-Linear Surrogate, $V_{\text{sub}}=256$)**: Identical to `fwd_streaming_oracle_fullvocab`, except the block-local readout pullback is restricted to the top $V_{\text{sub}}=256$ active vocabulary columns, matching `fwd_streaming_cowm`.

Table 1 provides the complete arithmetic and pass-count ledger for all studied algorithms ($B=16, T=512$, $N_{\text{tok}}=8192$, micro-horizon $S=8$, $L=6$ blocks). Across widths $D \in \{128, 256, 384, 512\}$, exact trainable parameter counts are $6,422,732$, $15,204,748$, $26,346,060$, and $39,846,668$ for the pretraining vocabulary $V=8192$ (Tables 1, 4, 5), and $3,801,292$, $9,961,868$, $18,481,740$, and $29,360,908$ for the synthetic diagnostic vocabulary $V=4096$ (Table 3).

| Algorithm | Execution Paradigm | Full Forward Passes | Backward Calls | Depth Reverse Sweeps | Attn Forward Calls / Block | MLP Forward Calls / Block | Param-Space WM Contractions | Peak VRAM ($D=512$, $M=2048$) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`backprop`** (Standard) | Autograd Forward-Backward | $1$ | $1$ | $1$ | $1$ clean | $1$ clean | $0$ | $3010.4\text{ MB}$ |
| **`backprop_ckpt`** (Checkpointed) | Autograd + Block Recompute | $2$ | $1$ | $1$ | $2$ ($1$ fwd + $1$ recompute) | $2$ ($1$ fwd + $1$ recompute) | $0$ | $1731.4\text{ MB}$ |
| **`block_fixed_top_discrepancy_bp`** | Block-Detached BP (Fixed Top $\delta_{\text{final}}$) | $1$ | $6$ ($1$/block) | $0$ (intra-block only) | $1$ clean | $1$ clean | $0$ | $3026.5\text{ MB}$ |
| **`block_local_greedy_bp_tophead`** | Block-Detached BP (Local $\delta_l$, Top Head) | $1$ | $6$ ($1$/block) | $0$ (intra-block only) | $1$ clean | $1$ clean | $0$ | $2153.6\text{ MB}$ |
| **`block_local_greedy_bp`** | Block-Detached BP (Mixed Head [8]) | $1$ | $6$ ($1$/block) | $0$ (intra-block only) | $1$ clean | $1$ clean | $0$ | $2169.6\text{ MB}$ |
| **`fwd_global_dust_K2`** | Pure Forward (Simplified Scalar) | $3$ | **$0$** | **$0$** | $3$ ($1$ clean + $2$ probe) | $3$ ($1$ clean + $2$ probe) | $0$ | $3864.8\text{ MB}$ |
| **`fwd_token_uwm_K2`** | Pure Forward (Token Probing) | $5$ | **$0$** | **$0$** | $5$ ($1$ clean + $4$ probe) | $5$ ($1$ clean + $4$ probe) | $0$ | $3864.8\text{ MB}$ |
| **`fwd_two_level_cowm_K4`** | Pure Forward (End-to-End Co-WM) | $9$ | **$0$** | **$0$** | $19$ ($1$ clean + $18$ probe) | $10$ ($1$ clean + $9$ probe/recomp) | $106,496$ | $1850.3\text{ MB}$ |
| **`fwd_streaming_cut_K4`** | Pure Forward (Streaming Cut) | **$1$** | **$0$** | **$0$** | $11$ ($1$ clean + $10$ probe) | $6$ ($1$ clean + $5$ probe/recomp) | $24,576$ | **$1820.3\text{ MB}$** |
| **`fwd_streaming_wm_K1`** | Pure Forward (Streaming Dealloc) | **$1$** | **$0$** | **$0$** | $7$ ($1$ clean + $6$ probe) | $2$ ($1$ clean + $1$ local fwd) | $18,432$ | **$1828.4\text{ MB}$** |
| **`fwd_streaming_wm_K4`** | Pure Forward (Streaming Dealloc) | **$1$** | **$0$** | **$0$** | $11$ ($1$ clean + $10$ probe) | $2$ ($1$ clean + $1$ local fwd) | $73,728$ | **$1820.3\text{ MB}$** |
| **`fwd_streaming_cowm_K4`** | Pure Forward (Streaming Dealloc) | **$1$** | **$0$** | **$0$** | $11$ ($1$ clean + $10$ probe) | $2$ ($1$ clean + $1$ local fwd) | $73,728$ | **$1828.4\text{ MB}$** |
| **`fwd_streaming_wm_K8`** | Pure Forward (Streaming Dealloc) | **$1$** | **$0$** | **$0$** | $11$ ($1$ clean + $10$ probe) | $2$ ($1$ clean + $1$ local fwd) | $147,456$ | **$1820.3\text{ MB}$** |
| **`fwd_streaming_cowm_K8`** | Pure Forward (Streaming Dealloc) | **$1$** | **$0$** | **$0$** | $11$ ($1$ clean + $10$ probe) | $2$ ($1$ clean + $1$ local fwd) | $147,456$ | **$1828.4\text{ MB}$** |
| **`fwd_streaming_wm_map_N4`**| Pure Forward (Streaming MAP) | **$1$** | **$0$** | **$0$** | $11$ ($1$ clean + $10$ probe) | $6$ ($1$ clean + $5$ settle/recomp) | $73,728$ | **$1828.4\text{ MB}$** |
| **`fwd_streaming_oracle_fullvocab`** | Analytic-Linear Surrogate ($V=8192$) | **$1$** | **$0$** | **$0$** | $11$ ($1$ clean + $10$ probe) | $2$ ($1$ clean + $1$ local fwd) | $55,296$ | $2100.4\text{ MB}$ |
| **`fwd_streaming_oracle`** | Analytic-Linear Surrogate ($V_{\text{sub}}=256$) | **$1$** | **$0$** | **$0$** | $11$ ($1$ clean + $10$ probe) | $2$ ($1$ clean + $1$ local fwd) | $55,296$ | **$1820.3\text{ MB}$** |

*Table 1: Verified Computation and Pass-Count Ledger for 6-layer Transformer pretraining ($B=16, T=512$, $N_{\text{tok}}=8192$, micro-horizon $S=8$, $V=8192$). All candidate forward-only methods enforce `bwd_calls = 0` and `depth_sweeps = 0`. Contraction counts reflect $3$ sites per block $\times 6$ blocks $\times K$ probes $\times (8192/8)$ groups ($147,456$ for $K=8$).*

---

## 2. Theoretical Analysis and Scaling Laws

### 2.1 Micro-Horizon Parameter-Space Weight Maximization (`WM-S`)
In Chung's Weight Maximization framework [2, Eq. 1–3], hidden unit $i \in \{1, \dots, M\}$ does not possess an activation-space transpose circuit $(V^\top \delta_t)_i$. Instead, each unit $i$ observes only the local plasticity changes $\Delta \mathbf{v}^{(i)}$ of its own outgoing weight column $\mathbf{v}^{(i)} = V_{:, i} \in \mathbb{R}^{D_{\text{out}}}$, reinforcing its activity when its outgoing synaptic column grows in squared $L^2$ norm.

To adapt this principle to sequence modeling without per-token activation transposes ($S = 1$) or full-batch temporal cross-talk ($S = N_{\text{tok}}$), we introduce **Parameter-Space Micro-Horizon Weight Maximization (`WM-S`)**:
1. Partition the $N_{\text{tok}} = B \times T$ tokens into $G = N_{\text{tok}} / S$ disjoint micro-groups $\mathcal{S}_1, \dots, \mathcal{S}_G$ of size $S$ tokens ($S \in \{4, 8, 16, 64\}$).
2. For exploration draw $k \in \{1, \dots, K\}$, sample independent Rademacher perturbations $\xi_{g, s, i}^{(k)} \in \{-\sigma, +\sigma\}$ for each neuron $i \in \{1, \dots, M\}$.
3. Over each micro-group $\mathcal{S}_g$, the outgoing matrix $V \in \mathbb{R}^{D_{\text{out}} \times M}$ accumulates its parameter-space plasticity displacement:
   $$\Delta V_{\mathcal{S}_g}^{(k)} = \sum_{s \in \mathcal{S}_g} \delta_{g, s} \big(\xi_{g, s}^{(k)}\big)^\top \;\in\; \mathbb{R}^{D_{\text{out}} \times M}.$$
4. Neuron $i$ evaluates its parameter-space inner product from its own column $\mathbf{v}^{(i)} = V_{:, i}$ and column update $\Delta \mathbf{v}_{\mathcal{S}_g}^{(i, k)} = (\Delta V_{\mathcal{S}_g}^{(k)})_{:, i}$ [2, Eq. 2]:
   $$G_{\mathcal{S}_g}^{(i, k)} = \mathbf{v}^{(i)} \cdot \Delta \mathbf{v}_{\mathcal{S}_g}^{(i, k)} - \beta \left\|\Delta \mathbf{v}_{\mathcal{S}_g}^{(i, k)}\right\|_2^2 \;\in\; \mathbb{R}.$$
5. Neuron $i$ computes its input credit for token $t \in \mathcal{S}_g$ [2, Eq. 3]:
   $$\hat{g}_{g, t, i}^{\text{WM-S}} = \frac{1}{K} \sum_{k=1}^K G_{\mathcal{S}_g}^{(i, k)} \frac{\xi_{g, t, i}^{(k)}}{\sigma^2}, \qquad \nabla_{W_1} \mathcal{L} = \sum_{g=1}^G \sum_{t \in \mathcal{S}_g} \big(\hat{g}_{g, t}^{\text{WM-S}} \odot \phi'(a_{1, g, t})\big) x_{g, t}^\top.$$

**Proposition 1 (Conditional Coordinate Variance and Sibling Decoupling of `WM-S`)**:
*Conditioned on fixed downstream linear targets $\delta_{g, s}$ independent of $\xi$, with independent Rademacher perturbations $\xi_{g, s, i}^{(k)} \in \{-\sigma, +\sigma\}$ (so $(\xi_{g, t, i}^{(k)})^2 / \sigma^2 \equiv 1$) and $\beta = 0$, expanding $\hat{g}_{g, t, i}^{\text{WM-S}}$ yields:*
$$\hat{g}_{g, t, i}^{\text{WM-S}} = \big(\mathbf{v}^{(i)} \cdot \delta_{g, t}\big) \underbrace{\frac{(\xi_{g, t, i}^{(k)})^2}{\sigma^2}}_{\equiv 1} + \frac{1}{K} \sum_{k=1}^K \sum_{s \in \mathcal{S}_g \setminus \{t\}} \big(\mathbf{v}^{(i)} \cdot \delta_{g, s}\big) \frac{\xi_{g, s, i}^{(k)} \xi_{g, t, i}^{(k)}}{\sigma^2}.$$
*Because $\mathbb{E}[\xi_{g, s, i} \xi_{g, t, i}] = 0$ for $s \ne t$, the estimator is conditionally unbiased ($\mathbb{E}[\hat{g}_{g, t, i}^{\text{WM-S}} \mid \delta] = \mathbf{v}^{(i)} \cdot \delta_{g, t}$) with conditional variance:*
$$\text{Var}\!\left[\hat{g}_{g, t, i}^{\text{WM-S}} \;\middle|\; \delta\right] = \frac{1}{K} \sum_{s \in \mathcal{S}_g \setminus \{t\}} (\mathbf{v}^{(i)} \cdot \delta_{g, s})^2.$$

*Decoupling Mechanism*: In activation-space perturbation (`Cut`), the reward $R_t^{(k)}$ sums over all $M$ neurons at token $t$, yielding conditional variance $\frac{1}{K}\sum_{j \ne i} (\mathbf{v}^{(j)} \cdot \delta_t)^2$ that scales with $M-1$. In `WM-S`, parameter-space column isolation decouples all $M - 1$ sibling neurons $j \ne i$, replacing the sum over $M - 1$ neurons with a sum over $S - 1$ tokens in $\mathcal{S}_g$, which is conditionally independent of width $M$ for fixed per-unit targets.

### 2.2 Sylvester-Hadamard Temporal Coordination (`Co-WM-S`)
Because `WM-S` eliminates spatial sibling-neuron cross-talk under fixed $\delta$, the remaining conditional variance arises from the $S - 1$ cross-token terms within micro-horizon $\mathcal{S}_g$. In **`Co-WM-S`**, we adapt orthogonal Sylvester-Hadamard exploration [11] to token micro-horizons in sequence Transformers, structuring the $K \le S$ exploration probes across the $S$ tokens of micro-group $\mathcal{S}_g$ using $K$ distinct columns $\{c_1, \dots, c_K\}$ drawn uniformly without replacement from an $S \times S$ Sylvester-Hadamard matrix $H \in \{-1, +1\}^{S \times S}$ ($S$ a power of 2), modulated by an independent Rademacher carrier $r_{g, s, i} \in \{-1, +1\}$:
$$\xi_{g, s, i}^{(k)} = \sigma \, H_{s, c_k} \, r_{g, s, i}.$$

**Proposition 2 (Finite-Population Conditional Variance of `Co-WM-S`)**:
*Conditioned on fixed downstream targets $\delta_{g, s}$ and writing $c_s = \mathbf{v}^{(i)} \cdot \delta_{g, s}$, uniform selection of $K \in \{1, \dots, S\}$ distinct Hadamard columns without replacement at $\beta = 0$ yields $\mathbb{E}[\hat{g}_{g, t, i}^{\text{Co-WM-S}} \mid \delta] = c_t$ and exact conditional variance:*
$$\text{Var}\!\left[\hat{g}_{g, t, i}^{\text{Co-WM-S}} \;\middle|\; \delta\right] = \frac{S - K}{K (S - 1)} \sum_{s \in \mathcal{S}_g \setminus \{t\}} c_s^2.$$
*Proof*: For distinct tokens $s \ne t$, $p_{s, t}(c) = H_{s, c} H_{t, c}$ has population mean $\frac{1}{S}\sum_{c=1}^S H_{s, c} H_{t, c} = 0$ by Hadamard orthogonality and unit variance $p_{s, t}(c)^2 \equiv 1$. Sampling $K$ distinct columns without replacement yields the classical hypergeometric variance reduction factor $\frac{S - K}{K(S - 1)}$. At $K = S$, the conditional variance vanishes **identically ($\text{Var} \equiv 0$)** for every width $M$.

### 2.3 Exact Covariance Identity, Sufficient Conditions, and Multi-Checkpoint Trajectory Audit
For row $i$ of the incoming weight matrix $W_1$, let $c_{g, s, i} = \mathbf{v}^{(i)} \cdot \delta_{g, s} \in \mathbb{R}$ and $z_{g, t, i} = \phi'(a_{1, g, t, i}) x_{g, t} \in \mathbb{R}^D$, so the exact row gradient is $g_i = \sum_{g=1}^G \sum_{t \in \mathcal{S}_g} c_{g, t, i} z_{g, t, i} = \sum_{g=1}^G g_{g, i}$.

**Proposition 3 (Exact Conditional Frobenius Weight-Gradient Covariance and Relative Variance Law)**:
*Under `WM-S` exploration with $K$ independent Rademacher draws $\xi_{g, s, i}^{(k)} \in \{-\sigma, +\sigma\}$ and $\beta = 0$, the estimator error decomposes over unordered token pairs $\{s, t\} \subset \mathcal{S}_g$ ($s < t$):*
$$\widehat{\nabla}_{W_{1, i}} - g_i = \frac{1}{K} \sum_{k=1}^K \sum_{g=1}^G \sum_{1 \le s < t \le S} \big(c_{g, s, i} z_{g, t, i} + c_{g, t, i} z_{g, s, i}\big) \frac{\xi_{g, s, i}^{(k)} \xi_{g, t, i}^{(k)}}{\sigma^2}.$$
*Because distinct pairs $\{s, t\} \ne \{s', t'\}$ are pairwise uncorrelated, the exact weight-gradient covariance is:*
$$\text{Cov}\!\left(\widehat{\nabla}_{W_{1, i}} \;\middle|\; c, z\right) = \frac{1}{K} \sum_{g=1}^G \sum_{1 \le s < t \le S} \big(c_{g, s, i} z_{g, t, i} + c_{g, t, i} z_{g, s, i}\big) \big(c_{g, s, i} z_{g, t, i} + c_{g, t, i} z_{g, s, i}\big)^\top,$$
*and the exact conditional Frobenius variance summed across all $M$ neurons is:*
$$\mathbb{E}\!\left[\left\|\widehat{\nabla}_{W_1} - \nabla_{W_1}\right\|_F^2 \;\middle|\; c, z\right] = \kappa(S, K) \sum_{i=1}^M \sum_{g=1}^G \sum_{1 \le s < t \le S} \left\|c_{g, s, i} z_{g, t, i} + c_{g, t, i} z_{g, s, i}\right\|_2^2,$$
*where $\kappa(S, K) = 1/K$ for `WM-S` and $\kappa(S, K) = \frac{S-K}{K(S-1)}$ for `Co-WM-S`.*

**Algebraic Cross-Token Identity**: By expanding the pair norm squared:
$$\sum_{1 \le s < t \le S} \left\|c_s z_t + c_t z_s\right\|_2^2 = \left(\sum_{s=1}^S c_s^2\right) \left(\sum_{t=1}^S \|z_t\|_2^2\right) + \left\|g_{\mathcal{S}_g}\right\|_2^2 - 2 \sum_{t=1}^S c_t^2 \|z_t\|_2^2.$$
Defining the **Within-Group Support Alignment Ratio** $\alpha(c, z)$, the **Global Gradient Coherence Ratio** $\gamma(c, z)$, and the **Group Gradient Coherence Ratio** $\gamma_{\text{grp}}(c, z)$:
$$\alpha(c, z) \triangleq \frac{\sum_{g, i} \left(\sum_{s=1}^S c_{g, s, i}^2\right) \left(\sum_{t=1}^S \|z_{g, t, i}\|_2^2\right)}{S \sum_{g, t, i} c_{g, t, i}^2 \|z_{g, t, i}\|_2^2}, \qquad \gamma(c, z) \triangleq \frac{\sum_i \|g_i\|_2^2}{\sum_{g, t, i} c_{g, t, i}^2 \|z_{g, t, i}\|_2^2}, \qquad \gamma_{\text{grp}}(c, z) \triangleq \frac{\sum_{g, i} \|g_{g, i}\|_2^2}{\sum_i \|g_i\|_2^2},$$
the exact conditional relative parameter-gradient variance is governed by the identity:
$$\text{RelVar}(\text{WM-S} \mid c, z) \triangleq \frac{\mathbb{E}\!\left[\left\|\widehat{\nabla}_{W_1} - \nabla_{W_1}\right\|_F^2 \;\middle|\; c, z\right]}{\left\|\nabla_{W_1}\right\|_F^2} = \frac{1}{K} \left[ \frac{\alpha(c, z) S - 2}{\gamma(c, z)} + \gamma_{\text{grp}}(c, z) \right].$$

**Analysis of Failure Modes and Counterexamples**:
Because $\alpha(c, z)$, $\gamma(c, z)$, and $\gamma_{\text{grp}}(c, z)$ depend on the empirical distribution of $c$ and $z$, Proposition 3 implies **conditional** width-invariance at fixed $(\alpha, \gamma, \gamma_{\text{grp}})$ rather than an unconditional guarantee across arbitrary network states:
1. *Gradient Cancellation Counterexample*: If token gradients cancel across the sequence ($\gamma \to 0$), relative variance diverges. For $S=8, K=1, D=1, M=4$, inputs $x = (1, 2, 0 \dots)$, targets $\delta = (4, -1+\varepsilon, 0 \dots)$, $z = (2, 8, 0 \dots)$, $c = (4, -1+\varepsilon, 0 \dots)$, the exact gradient is $g = 8\varepsilon$ and cross-term $c_1 z_2 + c_2 z_1 = 30 + 2\varepsilon$. The exact conditional relative variance is $\frac{(30+2\varepsilon)^2}{64\varepsilon^2}$, which equals $140{,}812.5625$ at $\varepsilon = 0.01$ (verified by exhaustive enumeration over all 256 Rademacher states).
2. *Cross-Token Support Mismatch Counterexample*: Non-cancellation ($\gamma > 0$) alone is insufficient if $c$ and $z$ have mismatched temporal support within a micro-group ($\alpha \to \infty$). For $c = (1, \varepsilon, 0 \dots)$ and $z = (\varepsilon, 1, 0 \dots)$, both nonzero token gradients equal $\varepsilon$ (reinforcing, $g = 2\varepsilon, \sum c_t^2 z_t^2 = 2\varepsilon^2$, so $\gamma = 2.0$), but $c_1 z_2 = 1 \gg \varepsilon^2$, giving $\alpha \approx \frac{1}{16\varepsilon^2}$. The exact conditional relative variance is $\frac{(1+\varepsilon^2)^2}{4\varepsilon^2} = 2500.500025$ at $\varepsilon = 0.01$ for $K=1$, $357.214289$ for $K=4$ `Co-WM-S`, and $0.0$ for $K=8$ `Co-WM-S`.

**Empirical Trajectory Audit of Conditional Quantities (`verify_learned_prop3_scaling.py`)**:
To bridge Proposition 3 to actual training behavior with full reproducibility from an empty output file (`python beyond_backprop/verify_learned_prop3_scaling.py --regenerate-all`, saving `multiwidth_learned_prop3_diagnostic.json`), we calculate the **conditional** quantities $\alpha(c, z), \gamma(c, z), \gamma_{\text{grp}}(c, z)$, and $\text{RelVar}(\cdot \mid c, z)$ from frozen Layer 3 checkpoint tensors ($S=8$) on batches of shape **$B=16, T=512$ ($N_{\text{tok}}=8,192$ tokens/batch)** across widths $D \in \{128, 256, 384, 512\}$ under three explicitly documented protocols:
1. **Benchmark-Schedule Holdout Validation Trajectory (`benchmark_holdout_trajectory_4batch`)**:
   - *Training Recipe*: 200 steps of `fwd_streaming_cowm` ($K_{\text{wm}}=4, K_{\text{qk}}=2, S=8$) on `train_batches[0:200]` drawn from `shard_00000.parquet` ($B=16, T=512$) using the **exact benchmark optimizer schedule** from `run_pure_forward_only_suite.py` (linear LR warmdown over the final 45% of steps, Muon momentum warmup $0.85 \to 0.95$ over 200 steps, and linear Muon weight decay decay $0.2(1 - \text{progress})$).
   - *Evaluation Split*: Evaluated at 5 checkpoints ($t \in \{0, 50, 100, 150, 200\}$) across **4 disjoint holdout validation batches** (`holdout_val_batches[0:4]`, shape $B=16, T=512, N_{\text{tok}}=8,192$) drawn from `shard_06542.parquet` (row groups $40 \dots 82$).
   - *Ranges of 4-Batch Means*: Across all $4 \times 5 = 20$ width-checkpoint states, the 4-batch means span $\alpha \in [0.8572 \pm 0.0063, \, 1.0033 \pm 0.0012]$, $\gamma \in [2.3604 \pm 0.5815, \, 8.1838 \pm 5.2378]$, and $\gamma_{\text{grp}} \in [0.1779 \pm 0.1155, \, 0.4410 \pm 0.0956]$. Consequently, the 4-batch mean conditional relative variances stay bounded in $[1.0448 \pm 0.6991, \, 2.7498 \pm 0.6188]$ for `WM-S` ($K=1$) and $[0.1492 \pm 0.0999, \, 0.3929 \pm 0.0884]$ for `Co-WM-S` ($K=4$). At $t=200$ (4-batch mean $\pm$ SD):
     - $D=128$: $\alpha = 0.9439 \pm 0.0154$, $\gamma = 3.3446 \pm 1.9805$, `WM-S` ($K=1$) $= 2.5773 \pm 1.4312$, `Co-WM-S` ($K=4$) $= 0.3682 \pm 0.2045$, `Cut-K4` $= 33.44 \pm 18.69$;
     - $D=256$: $\alpha = 0.9414 \pm 0.0070$, $\gamma = 3.5498 \pm 2.1871$, `WM-S` ($K=1$) $= 2.5365 \pm 1.5310$, `Co-WM-S` ($K=4$) $= 0.3624 \pm 0.2187$, `Cut-K4` $= 51.37 \pm 31.06$;
     - $D=384$: $\alpha = 0.9320 \pm 0.0053$, $\gamma = 4.0057 \pm 2.7904$, `WM-S` ($K=1$) $= 2.5661 \pm 1.8502$, `Co-WM-S` ($K=4$) $= 0.3666 \pm 0.2643$, `Cut-K4` $= 78.25 \pm 56.20$;
     - $D=512$: $\alpha = 0.9902 \pm 0.0105$, $\gamma = 2.8972 \pm 0.8824$, `WM-S` ($K=1$) $= 2.5779 \pm 0.8397$, `Co-WM-S` ($K=4$) $= 0.3683 \pm 0.1199$, `Cut-K4` $= 123.91 \pm 39.04$.
2. **Fixed-Optimizer Diagnostic Trajectory (`streaming_trajectory_4batch`)**:
   - *Training & Evaluation Recipe*: 200 steps of `fwd_streaming_cowm` ($K_{\text{wm}}=4, K_{\text{qk}}=2, S=8$) on `train_batches[0:200]` (`shard_00000.parquet`, $B=16, T=512$) with fixed default Muon/AdamW optimizer parameters (`setup_optimizer(use_muon=True)` without LR/momentum/WD scheduling), evaluated at $t \in \{0, 50, 100, 150, 200\}$ on 4 held-out training-stream batches `train_batches[200:204]` ($B=16, T=512, N_{\text{tok}}=8,192$). Across all 20 states, the 4-batch means span $\alpha \in [0.9062 \pm 0.0079, \, 1.0162 \pm 0.0080]$, $\gamma \in [2.2698 \pm 0.3875, \, 5.6916 \pm 0.0958]$, conditional `WM-S` ($K=1$) $\text{RelVar} \in [1.2203, \, 2.8887]$, and conditional `Co-WM-S` ($K=4$) $\text{RelVar} \in [0.1743, \, 0.4127]$.
3. **Single-Batch Table 2 States (`step_0_init`, `step_200_learned`, `step_200_streaming_learned`)**:
   - Calculated from frozen tensors under fixed default Muon/AdamW parameters on `shard_00000.parquet` ($B=16, T=512$): `step_0_init` on `train_batches[0]`, `step_200_learned` on `train_batches[199]` after 200 steps of Cut-scope `detached_oracle`, and `step_200_streaming_learned` on `train_batches[199]` after 200 steps of `fwd_streaming_cowm` ($K=4$).

| Width $D$ ($M=4D$) | State Regime | $\alpha$ (Support Alignment) | $\gamma$ (Global Coherence) | $\gamma_{\text{grp}}$ (Group Coherence) | `Cut-K4` Cond. RelVar | `WM-S` ($K=1$) Cond. RelVar | `Co-WM-S` ($K=4$) Cond. RelVar | `Co-WM-S` ($K=8$) Cond. RelVar | `GS-MAP-N1` RelBias | `GS-MAP-N2` RelBias |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $D=128$ ($M=512$) | `step_0_init` | $0.9990$ | $3.4755$ | $0.2885$ | $37.05$ | $2.0127$ | $0.2875$ | **$0.0000$** | $0.00017$ | $0.05833$ |
| $D=128$ ($M=512$) | `step_200_learned` | $1.0250$ | $1.4638$ | $0.6859$ | $55.34$ | $4.9214$ | $0.7031$ | **$0.0000$** | $0.00022$ | $0.16049$ |
| $D=128$ ($M=512$) | `step_200_streaming` | $0.9746$ | $2.1800$ | $0.4589$ | $41.17$ | $3.1179$ | $0.4454$ | **$0.0000$** | $0.00020$ | $0.16297$ |
| $D=256$ ($M=1024$) | `step_0_init` | $1.0013$ | $3.2002$ | $0.3134$ | $79.86$ | $2.1915$ | $0.3131$ | **$0.0000$** | $0.00019$ | $0.05574$ |
| $D=256$ ($M=1024$) | `step_200_learned` | $0.9275$ | $1.5571$ | $0.6404$ | $103.94$ | $4.1213$ | $0.5888$ | **$0.0000$** | $0.00022$ | $0.13396$ |
| $D=256$ ($M=1024$) | `step_200_streaming` | $0.9752$ | $2.0925$ | $0.4753$ | $66.99$ | $3.2478$ | $0.4640$ | **$0.0000$** | $0.00018$ | $0.14256$ |
| $D=384$ ($M=1536$) | `step_0_init` | $1.0003$ | $3.6960$ | $0.2714$ | $103.77$ | $1.8953$ | $0.2708$ | **$0.0000$** | $0.00017$ | $0.05414$ |
| $D=384$ ($M=1536$) | `step_200_learned` | $1.0329$ | $2.0612$ | $0.4860$ | $146.12$ | $3.5248$ | $0.5035$ | **$0.0000$** | $0.00020$ | $0.12289$ |
| $D=384$ ($M=1536$) | `step_200_streaming` | $0.9730$ | $1.9493$ | $0.5142$ | $123.91$ | $3.4815$ | $0.4974$ | **$0.0000$** | $0.00019$ | $0.12925$ |
| $D=512$ ($M=2048$) | `step_0_init` | $1.0002$ | $3.3703$ | $0.2976$ | $151.85$ | $2.0783$ | $0.2969$ | **$0.0000$** | $0.00019$ | $0.05394$ |
| $D=512$ ($M=2048$) | `step_200_learned` | $0.9729$ | $2.1721$ | $0.4605$ | $152.76$ | $3.1231$ | $0.4462$ | **$0.0000$** | $0.00018$ | $0.13607$ |
| $D=512$ ($M=2048$) | `step_200_streaming` | $0.9951$ | $2.4223$ | $0.4139$ | $150.28$ | $2.8746$ | $0.4107$ | **$0.0000$** | $0.00018$ | $0.12879$ |

*Table 2: Conditional Proposition 3 quantities calculated from frozen Layer 3 tensors on ClimbMix ($B=16, T=512$, `multiwidth_learned_prop3_diagnostic.json`). While activation-space `Cut-K4` conditional relative variance grows with width ($41.17 \to 150.28$ along the streaming trajectory), conditional `WM-S` ($K=1$) and `Co-WM-S` ($K=4, 8$) relative variances remain bounded across tested widths ($2.87\text{--}3.48$ and $0.41\text{--}0.50$, respectively, and $0.00$ at $K=8$).*

### 2.4 Whole-Network Probing: Sequence-Aware Variance, Sensitivity Thresholds, and Ablations
Propositions 1–3 establish conditional sibling-neuron decoupling given a fixed local output discrepancy $c$. Eliminating conditional local variance does **not** make the whole-network gradient unbiased with respect to end-to-end backpropagation. In a causal sequence Transformer, the downstream map $F^{(m)}: \mathbb{R}^{T \times D} \to \mathbb{R}^{T \times D}$ from injection site $m \in \{0, \dots, 2L\}$ ($S_{\text{sites}} = 2L + 1 = 13$ for $L=6$) to the final normalized hidden state has a block-lower-triangular sequence-channel Jacobian $J^{(m)} \in \mathbb{R}^{(TD) \times (TD)}$, with blocks $J_{u, v}^{(m)} \in \mathbb{R}^{D \times D}$ non-zero for all causal token pairs $u \ge v$ and zero for $u < v$. Given top sensitivity $c = (c_1, \dots, c_T) \in \mathbb{R}^{T \times D}$, the exact transpose sensitivity of site $m$ at token $t$ is $u_t^{(m)} = \sum_{u=t}^T (J_{u, t}^{(m)})^\top c_u \in \mathbb{R}^D$.

**Sequence-Aware Within-Site vs. Between-Site Variance of Depth-Hadamard vs. Independently Resampled Probing**:
Let $H_{\text{depth}} = 16$ be the smallest power of $2$ at least $S_{\text{sites}} = 13$, and let $\kappa(H_{\text{depth}}, K_{\text{net}}) = \frac{H_{\text{depth}} - K_{\text{net}}}{K_{\text{net}}(H_{\text{depth}} - 1)}$ ($\kappa = \frac{1}{15}$ at $H_{\text{depth}} = 16, K_{\text{net}} = 8$). Under **Depth-Hadamard Carrier Modulation (`depth_hadamard`)**, site $m$ draws one Rademacher tensor $r^{(m)} \in \{-1, +1\}^{T \times D}$ per $H_{\text{depth}}$-probe cycle and injects $\xi^{(m, k)} = \sigma h_{m, c_k} r^{(m)}$. Because $h_{m, c_k}^2 \equiv 1$, the within-site contribution ($m' = m$) is invariant to $K_{\text{net}} \le H_{\text{depth}}$ within a cycle, whereas the between-site contribution ($m' \ne m$) is weighted by $\kappa(H_{\text{depth}}, K_{\text{net}})$. Under **Independently Resampled Carriers (`iid_resample`)**, fresh i.i.d. tensors $r^{(m, k)}$ are drawn at every probe $k \in \{1, \dots, K_{\text{net}}\}$, dividing both within-site and between-site variances by $1 / K_{\text{net}}$.

For each return-aggregation mode, the linear-limit expectation and exact sequence-aware activation-credit variance $\operatorname{Var}(\hat{g}^{(m)}) = A_{\text{mode}}^{(m)} + \kappa_{\text{mode}} B_{\text{mode}}^{(m)}$ ($\kappa_{\text{mode}} = \kappa(H_{\text{depth}}, K_{\text{net}})$ for `depth_hadamard`, or dividing $A_{\text{mode}}^{(m)} + B_{\text{mode}}^{(m)}$ by $K_{\text{net}}$ for `iid_resample`) are:
1. **Full-Sequence Scalar-Dot Probing (`full_seq_dot`, $n = TD$)**:
   The scalar return sums over all tokens and channels: $R_{\text{seq}}^{(k)} = \sum_{m'=0}^{2L} \sum_{u=1}^T \langle u_u^{(m')}, \xi_u^{(m', k)} \rangle$.
   - *Linear-Limit Expectation*: Unbiased for the full causal transpose, $\mathbb{E}[\hat{g}_{\text{full}, t}^{(m)}] = u_t^{(m)} = \sum_{u=t}^T (J_{u, t}^{(m)})^\top c_u$.
   - *Exact Sequence-Wide Variance*: Writing $\|u^{(m)}\|_2^2 = \sum_{t=1}^T \|u_t^{(m)}\|_2^2$, the single-probe within-site and between-site variance energies summed over all $n = TD$ coordinates are:
     $$A_{\text{full}}^{(m)} = (TD - 1) \left\|u^{(m)}\right\|_2^2, \qquad B_{\text{full}}^{(m)} = TD \sum_{m' \ne m} \left\|u^{(m')}\right\|_2^2.$$
2. **Token-Local Channel-Dot Probing (`token_dot`)**:
   At token $t$, the token-local return sums only over the $D$ channels at position $t$, but because the perturbation $\xi^{(m', k)}$ is injected across the entire sequence, $(J^{(m')} \xi^{(m', k)})_t$ depends on perturbations at **all earlier tokens $v \le t$**:
   $$R_t^{(k)} = c_t^\top (\Delta x_{\text{final}}^{(k)})_t = \sum_{m'=0}^{2L} \sum_{v=1}^t \big\langle a_{t, v}^{(m')}, \xi_v^{(m', k)} \big\rangle, \qquad \text{where } a_{t, v}^{(m')} \triangleq \big(J_{t, v}^{(m')}\big)^\top c_t \in \mathbb{R}^D.$$
   - *Linear-Limit Expectation*: Multiplying by $\xi_t^{(m, k)} / \sigma^2$ eliminates $v < t$ in expectation ($\mathbb{E}[\xi_t \xi_v^\top] = 0$ for $v < t$), leaving only the diagonal token block and **truncating all future-token causal blocks $u > t$**:
     $$\mathbb{E}\!\left[\hat{g}_{\text{tok}, t}^{(m)}\right] = a_{t, t}^{(m)} = \big(J_{t, t}^{(m)}\big)^\top c_t \;\ne\; \sum_{u=t}^T \big(J_{u, t}^{(m)}\big)^\top c_u.$$
   - *Exact Sequence-Aware Token-Dot Variance (Including Earlier-Token Causal Cross-Talk)*: Multiplication by $\xi_t^{(m, k)}$ does **not** remove the variance of the earlier-token terms $v < t$! Under `depth_hadamard`, $\xi_t^{(m, k)} \xi_v^{(m, k)\top} / \sigma^2 = r_t^{(m)} r_v^{(m)\top}$ for all $v \le t$, so the single-probe within-site error energy $A_{\text{tok}, t}^{(m)}$ and between-site error energy $B_{\text{tok}, t}^{(m)}$ about the token-local mean $a_{t, t}^{(m)}$ at token $t$ are:
     $$A_{\text{tok}, t}^{(m)} = (D - 1) \left\|a_{t, t}^{(m)}\right\|_2^2 + D \sum_{v < t} \left\|a_{t, v}^{(m)}\right\|_2^2, \qquad B_{\text{tok}, t}^{(m)} = D \sum_{m' \ne m} \sum_{v \le t} \left\|a_{t, v}^{(m')}\right\|_2^2.$$
     Notice the second within-site term $D \sum_{v < t} \|a_{t, v}^{(m)}\|_2^2$: even at $D = 1$, where same-token channel cross-talk $(D-1)\|a_{t, t}^{(m)}\|_2^2 = 0$, earlier-token causal coupling ($v < t$) generates non-zero within-site variance that persists unattenuated across a fixed-carrier `depth_hadamard` cycle and divides by $1 / K_{\text{net}}$ under `iid_resample`!
   - *Explicit Causal Counterexample (Verified in Gate 2H)*: For $T=2, D=1$ (single site) with $J = \begin{pmatrix} 1 & 0 \\ 3 & 4 \end{pmatrix}$ and $c = \begin{pmatrix} 5 \\ 7 \end{pmatrix}$, at token $t = 2$ we have $a_{2, 2} = 28$ and $a_{2, 1} = 21$. The second-token `token_dot` estimator is $r_2(21 r_1 + 28 r_2) = 28 + 21 r_1 r_2$. Its mean is $28$ (omitting future-token credit on token $1$, where $\mathbb{E}[\hat{g}_{\text{tok}, 1}] = 5 \ne 26$), and its exact variance about $28$ is $(1 - 1)(28^2) + 1(21^2) = 441.0$—which equals $441.0$ at every $K_{\text{net}} \in \{1, 2, 4\}$ under fixed-carrier `depth_hadamard`, and $441.0, 220.5, 110.25$ ($= 441.0 / K_{\text{net}}$) at $K_{\text{net}} = 1, 2, 4$ under `iid_resample` (verified in Gate 2H).
3. **Coordinate-Wise Diagonal Probing (`diag_jacobian`)**:
   Evaluates $\xi_{t, d}^{(m, k)} c_{t, d} (\Delta x_{\text{final}}^{(k)})_{t, d} / \sigma^2$, with expectation $\mathbb{E}[\hat{g}_{\text{diag}, t, d}^{(m)}] = c_{t, d} J_{(t, d), (t, d)}^{(m)}$ (verified in Gate 2G: for $J = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, c = \begin{pmatrix} 5 \\ 7 \end{pmatrix}$, $\mathbb{E}_{\text{diag}} = \begin{pmatrix} 5 \\ 28 \end{pmatrix} \ne J^\top c = \begin{pmatrix} 26 \\ 38 \end{pmatrix}$) and single-probe within-site and between-site variance energies:
   $$A_{\text{diag}}^{(m)} = \sum_{t, d} c_{t, d}^2 \left( \sum_{d' \ne d} \big(J_{(t, d), (t, d')}^{(m)}\big)^2 + \sum_{v < t} \sum_{d'=1}^D \big(J_{(t, d), (v, d')}^{(m)}\big)^2 \right), \quad B_{\text{diag}}^{(m)} = \sum_{m' \ne m} \sum_{t, d} c_{t, d}^2 \sum_{v \le t} \sum_{d'=1}^D \big(J_{(t, d), (v, d')}^{(m')}\big)^2.$$

**Sensitivity-Energy Condition for Depth-Hadamard vs. Independent Resampling ($B^{(m)} > 15 A^{(m)}$)**:
At $H_{\text{depth}} = 16, K_{\text{net}} = 8$, comparing $\operatorname{Var}_{\text{DH}} = A^{(m)} + \frac{1}{15} B^{(m)}$ against $\operatorname{Var}_{\text{iid}} = \frac{1}{8}(A^{(m)} + B^{(m)})$ yields the exact necessary and sufficient condition:
$$A^{(m)} + \frac{1}{15} B^{(m)} < \frac{1}{8}\big(A^{(m)} + B^{(m)}\big) \quad \Longleftrightarrow \quad B^{(m)} > 15 A^{(m)}.$$
Having $S_{\text{sites}} = 13$ sites does **not** by itself guarantee $B^{(m)} > 15 A^{(m)}$: if all 13 sites had equal sensitivity energy $\|u^{(m)}\|_2^2 = 1$, then $B_{\text{full}}^{(m)} / A_{\text{full}}^{(m)} = \frac{12 n}{n - 1} < 15$ for all $n \ge 6$ (for example, at $n = 512$ and unit site energy, $A = 511$ and $B = 6144$, so $\operatorname{Var}_{\text{DH}} = 920.6 > \operatorname{Var}_{\text{iid}} = 831.875$, making independent resampling better).
To test whether $B^{(m)} > 15 A^{(m)}$ holds on our initialized 6-layer Transformer (`c_proj_init_scale=0.5`, where `x0` and attention pathways carry larger sensitivity energy than individual MLP projections), `run_pure_forward_only_suite.py --mode diag` (`pure_forward_width_diagnostic.json`, `site_sensitivity_audit`) measures the exact 13-site sensitivity energies $E_m = \|\frac{\partial \mathcal{L}}{\partial s^{(m)}}\|_F^2$:
- Across widths $D \in \{128, 256, 384, 512\}$, the measured ratio $B_{\text{full}}^{(m)} / A_{\text{full}}^{(m)}$ is **$20.08, 19.88, 20.05, 20.30$** at Layer 3 MLP ($m=8$) and **$26.40, 26.15, 25.67, 26.31$** at Layer 5 MLP ($m=12$). Because $B^{(m)} / A^{(m)} > 15$ at both MLP sites, the predicted DH-to-i.i.d. activation-credit variance ratio is $\frac{1 + 20.30/15}{(1 + 20.30)/8} = 0.8839 < 1$ at Layer 3 ($0.8068$ at Layer 5).
- In Table 3 ($D=512$), we report both **activation-credit relative variance** ($\operatorname{RelVar}(\widehat{\delta u}_{\text{mlp}}^{(3)})$) and **accumulated parameter-gradient relative variance** ($\operatorname{RelVar}(\widehat{\nabla}_{W_1}^{(3)})$): for `full_seq_dot`, `depth_hadamard` vs `iid_resample` gives $79,218.20$ vs $91,443.37$ on activation credit (ratio $0.866 \approx 0.884$) and $78,606.12$ vs $90,830.04$ on $\widehat{\nabla}_{W_1}^{(3)}$; for `token_dot`, $1191.29$ vs $1398.44$ on activation credit and $1180.58$ vs $1386.78$ on $\widehat{\nabla}_{W_1}^{(3)}$; and for `diag_jacobian`, $1.56$ vs $2.60$ on activation credit and $1.55$ vs $2.58$ on $\widehat{\nabla}_{W_1}^{(3)}$. Thus, while carrier reuse leaves within-site variance $A^{(m)}$ unaveraged within a 16-probe cycle, both `depth_hadamard` and `iid_resample` exhibit the same 4-order-of-magnitude variance separation across `diag_jacobian` ($\sim 1.6\text{--}2.6$), `token_dot` ($\sim 1.2\text{--}1.4 \times 10^3$), and `full_seq_dot` ($\sim 7.9\text{--}9.1 \times 10^4$).

**6-Rung Sequential Ablation Ladder in Streaming Block-Local Supervision**:
To separate inter-block Jacobian omission from intermediate local supervision, readout mixture, intra-block surrogates, and vocabulary truncation, our 6-rung sequence in Tables 4 and 5 changes one well-defined intervention at each step (1000-step 2-seed `d6` holdout BPB in parentheses):
1. **Inter-Block Sublayer Jacobian Omission at Fixed Final-State Discrepancy (`backprop` $1.45172 \to$ `block_fixed_top_discrepancy_bp` $1.62152$, $\Delta = +0.16980$ BPB)**: Both methods evaluate the loss and `lm_head` update exclusively at the final state $x_{L-1}$; `block_fixed_top_discrepancy_bp` broadcasts that fixed final-state discrepancy $\delta_{\text{final}} = \frac{\partial \mathcal{L}(x_{L-1})}{\partial x_{L-1}}$ directly into each detached block $l$ via the identity residual path (`x_l.backward(delta_final)`), isolating the cost of omitting intervening non-identity sublayer Jacobians ($l' > l$).
2. **Replacing Fixed Final-State Discrepancy with Intermediate Block-State Supervision (`block_fixed_top_discrepancy_bp` $1.62152 \to$ `block_local_greedy_bp_tophead` $1.58085$, $\Delta = -0.04067$ BPB)**: Holds detached block boundaries and final-only `lm_head` updates fixed, while replacing $\delta_{\text{final}}$ with each block's own local-loss discrepancy $\frac{\partial \mathcal{L}(x_l)}{\partial x_l}$. Combining Rungs 1 and 2 gives $+0.12913$ BPB ($1.45172 \to 1.58085$) for the complete greedy local-supervision transition.
3. **Shared-Readout Intermediate-Loss Mixture (`block_local_greedy_bp_tophead` $1.58085 \to$ `block_local_greedy_bp` $1.57236$, $\Delta = -0.00849$ BPB)**: Gives $50\%$ `lm_head` gradient weight to block $L-1$ and $50\%$ across earlier blocks $l < L-1$.
4. **Intra-Block Forward Surrogate Package at Matched Full Vocabulary (`block_local_greedy_bp` $1.57236 \to$ `fwd_streaming_oracle_fullvocab` $1.74582$, $\Delta = +0.17346$ BPB)**: Retains full vocabulary $V=8192$ and the 50/50 `lm_head` mixture, but replaces exact intra-block autograd (`bwd_calls = 6`) with the forward-only intra-block surrogate package (`bwd_calls = 0`).
5. **Sub-Vocabulary Readout Truncation (`fwd_streaming_oracle_fullvocab` $1.74582 \to$ `fwd_streaming_oracle` $1.86466$, $\Delta = +0.11884$ BPB)**: Restricts the block-local readout pullback from $V=8192$ to the top $V_{\text{sub}}=256$ active vocabulary columns.
6. **Parameter-Space `Co-WM-S` at $K=S=8$ vs. Analytic Transpose (`fwd_streaming_oracle` $1.86466 \to$ `fwd_streaming_cowm_K8` $1.86518$, $\Delta = +0.00052$ BPB)**: Replaces exact matrix transposes ($W_O^\top, V^\top$) with $K=S=8$ parameter-space `Co-WM-S` column contractions.

### 2.5 MAP Settling: Single-Step Equivalence vs. Multi-Step Spectral Damping
In Post-Activation MAP Settling [1, Eq. 1, 5, 6, 7], post-activation discrepancy $e_1 = H^1 - \phi(W_1 x)$ minimizes:
$$E(e_1) = \frac{\rho}{2} \|e_1\|_2^2 + \frac{1}{2} \|e_2(e_1)\|_2^2, \qquad e_2(e_1) = -\epsilon_{\text{clamp}} \hat{\delta}_y - e_1 V^\top, \quad e_1(0) = \mathbf{0}.$$

**Proposition 4 (GS-MAP Spectral Filter and Settling Provenance)**:
*Under the recurrence $e_1(n+1) = e_1(n) - \eta (\rho e_1(n) - e_2(n) V)$ with non-oscillatory step size $0 < \eta \le \frac{1}{\rho + \|V\|_2^2}$, the exact $N$-step credit operator is:*
$$\hat{g}_h^{\text{GS-MAP}(N)} = (\delta_y V) \, \mathcal{F}_N(V^\top V), \qquad \text{where } \mathcal{F}_N(V^\top V) = \frac{\sum_{k=0}^{N-1} \big(I - \eta(\rho I + V^\top V)\big)^k}{\sum_{k=0}^{N-1} (1 - \eta \rho)^k}.$$
1. **$N=1$ Equivalence**: At $N = 1$, $\mathcal{F}_1(V^\top V) = I$, recovering exact local credit $\delta_y V$ ($\text{RelBias} \le 0.00022$ in Table 2).
2. **Multi-Step Spectral Damping ($N \ge 2$)**: Rather than improving local credit accuracy, $N \ge 2$ applies a contractive spectral filter that damps top singular modes ($\text{RelBias} = 0.129\text{--}0.163$ in Table 2).

---

## 3. Experimental Validation

### 3.1 Whole-Transformer Initialization Diagnostic and Unbiased Bias/Variance Decomposition
Table 3 reports gradient fidelity against analytical backpropagation across widths $D \in \{128, 256, 384, 512\}$ ($L=6, B=4, T=64, V=4096$) over $R = 32$ independent random trials (`pure_forward_width_diagnostic.json`).

**Unbiased Squared Relative Bias vs. Plug-In Sample-Mean Bias**:
For any stochastic gradient estimator $\hat{G}^{(r)}$ ($r = 1, \dots, R$) with sample mean $\bar{G}_R = \frac{1}{R}\sum_{r=1}^R \hat{G}^{(r)}$, expectation $\mu = \mathbb{E}[\hat{G}]$, and reference gradient $G_{\text{bp}}$, the naive plug-in squared relative bias $\widehat{\text{RelBias}}^2_{\text{plug}} = \frac{\|\bar{G}_R - G_{\text{bp}}\|_F^2}{\|G_{\text{bp}}\|_F^2}$ has expectation:
$$\mathbb{E}\!\left[\widehat{\text{RelBias}}^2_{\text{plug}}\right] = \frac{\|\mu - G_{\text{bp}}\|_F^2}{\|G_{\text{bp}}\|_F^2} + \frac{1}{R} \text{RelVar}(\hat{G}), \qquad \text{where } \widehat{\text{RelVar}} = \frac{1}{R - 1} \sum_{r=1}^R \frac{\|\hat{G}^{(r)} - \bar{G}_R\|_F^2}{\|G_{\text{bp}}\|_F^2}.$$
When $\text{RelVar}$ is large, $\widehat{\text{RelBias}}^2_{\text{plug}}$ is dominated by residual sample-mean variance $\text{RelVar}/R$ rather than true systematic bias. To eliminate this contamination:
1. We compute **Total Relative MSE** directly from the $R=32$ individual trial errors (with standard error of the mean across trials):
   $$\widehat{\text{TotalMSE}} = \frac{1}{R} \sum_{r=1}^R \frac{\|\hat{G}^{(r)} - G_{\text{bp}}\|_F^2}{\|G_{\text{bp}}\|_F^2}.$$
2. We report the **unbiased bias-corrected squared relative bias estimator** (with Tukey leave-one-out jackknife standard error across the $R=32$ trials):
   $$\widehat{\text{RelBias}}^2_{\text{unb}} = \widehat{\text{RelBias}}^2_{\text{plug}} - \frac{1}{R} \widehat{\text{RelVar}}, \qquad \mathbb{E}\!\left[\widehat{\text{RelBias}}^2_{\text{unb}}\right] = \frac{\|\mu - G_{\text{bp}}\|_F^2}{\|G_{\text{bp}}\|_F^2}.$$
   By algebraic identity, $\widehat{\text{TotalMSE}} = \frac{R-1}{R}\widehat{\text{RelVar}} + \widehat{\text{RelBias}}^2_{\text{plug}} \equiv \widehat{\text{RelVar}} + \widehat{\text{RelBias}}^2_{\text{unb}}$. When $\widehat{\text{RelBias}}^2_{\text{unb}}$ is comparable to or smaller than its jackknife standard error (as in `full_seq_dot` and `token_dot`), no nonzero bias is statistically resolved, and its square root should not be interpreted as a resolved bias magnitude.

| Algorithm | Paradigm / Carrier & Readout | $D=128$ Top / Mid Cos | $D=512$ Top / Mid Cos | Mid Scale ($D=512$) | Mid Param RelVar ($D=128 \to 512$) | Mid Unbiased $\text{RelBias}^2$ ($D=512$) | Mid TotalMSE ($D=512$) | Attn Q5 Cos / RelVar ($D=512$) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `fwd_global_dust_K2` | Global Scalar ($K=2$) | `-0.002` / `0.002` | `0.000` / `-0.000` | $1007.95$ | $7.79\times 10^6 \to 3.26\times 10^7$ | $-2250.8 \pm 10136.6$ | $3.26\times 10^7 \pm 4.50\times 10^6$ | `-0.0003` / $1.83\times 10^8$ |
| `fwd_token_uwm_K2` | Token-Scalar ($K=2$) | `0.004` / `0.007` | `0.004` / `0.003` | $56.74$ | $26,968 \to 103,931$ | $-29.98 \pm 26.68$ | $103,901 \pm 1075$ | `0.0002` / $5.84\times 10^5$ |
| `fwd_two_level_cowm_K8_fullseq` | Two-Level ($K=8$, `full_seq_dot`, DH) | `0.003` / `0.006` | `0.003` / `0.003` | $49.85$ | $21,803 \to 78,606$ | $27.44 \pm 27.86$ | $78,634 \pm 8449$ | `0.0012` / $4.88\times 10^6$ |
| `fwd_two_level_cowm_K8_fullseq_iid` | Two-Level ($K=8$, `full_seq_dot`, i.i.d.) | `0.005` / `0.009` | `0.001` / `0.003` | $53.07$ | $22,705 \to 90,830$ | $-23.07 \pm 36.45$ | $90,807 \pm 3178$ | `0.0004` / $5.85\times 10^6$ |
| `fwd_two_level_cowm_K8_tokendot` | Two-Level ($K=8$, `token_dot`, DH) | `0.052` / `0.059` | `0.026` / `0.029` | $6.12$ | $303.50 \to 1180.58$ | $-0.453 \pm 0.422$ | $1180.13 \pm 39.33$ | `0.0042` / $69,297$ |
| `fwd_two_level_cowm_K8_tokendot_iid` | Two-Level ($K=8$, `token_dot`, i.i.d.) | `0.051` / `0.054` | `0.024` / `0.028` | $6.67$ | $350.00 \to 1386.78$ | $0.088 \pm 0.455$ | $1386.87 \pm 7.47$ | `0.0042` / $89,860$ |
| **`fwd_two_level_cowm_K4`** | Two-Level ($K=4$, `diag_jacobian`, DH) | `0.412` / `0.355` | `0.410` / `0.365` | $0.96$ | $4.30 \to 4.13$ | $0.224 \pm 0.003$ | $4.35 \pm 0.27$ | `0.0560` / $330.05$ |
| **`fwd_two_level_cowm_K8_iid`** | Two-Level ($K=8$, `diag_jacobian`, i.i.d.) | `0.481` / `0.421` | `0.479` / `0.426` | $0.93$ | $2.64 \to 2.58$ | $0.224 \pm 0.002$ | $2.81 \pm 0.00$ | `0.0649` / $216.35$ |
| **`fwd_two_level_cowm_K8`** | Two-Level ($K=8$, `diag_jacobian`, DH) | `0.598` / `0.512` | `0.615` / `0.516` | $0.91$ | **$1.61 \to 1.55$** | **$0.222 \pm 0.002$** | **$1.77 \pm 0.07$** | `0.0837` / $136.49$ |
| `fwd_streaming_cut_K4` | Streaming Cut ($K=4$, Token-Scalar) | `0.016` / `0.015` | `0.004` / `0.003` | $47.76$ | $4638 \to 73,120$ | $-4.43 \pm 23.70$ | $73,116 \pm 815$ | `0.0037` / $8.28\times 10^5$ |
| **`fwd_streaming_wm_K1`** | Streaming `WM-S` ($K=1$, Indep.) | `0.123` / `0.110` | `0.125` / `0.111` | $1.80$ | $69.76 \to 68.70$ | $0.262 \pm 0.023$ | $68.97 \pm 0.20$ | `0.0159` / $3154.15$ |
| **`fwd_streaming_wm_K4`** | Streaming `WM-S` ($K=4$, Indep.) | `0.363` / `0.318` | `0.362` / `0.322` | $1.15$ | $7.19 \to 7.15$ | $0.246 \pm 0.003$ | $7.39 \pm 0.01$ | `0.0516` / $374.23$ |
| **`fwd_streaming_cowm_K4`** | Streaming `Co-WM-S` ($K=4$, Had.) | `0.496` / `0.438` | `0.498` / `0.442` | $1.09$ | $3.29 \to 3.26$ | $0.251 \pm 0.002$ | $3.51 \pm 0.00$ | `0.0688` / $197.17$ |
| **`fwd_streaming_wm_K8`** | Streaming `WM-S` ($K=8$, Indep.) | `0.533` / `0.465` | `0.532` / `0.471` | $1.09$ | $2.78 \to 2.74$ | $0.253 \pm 0.002$ | $2.99 \pm 0.01$ | `0.0731` / $173.44$ |
| **`fwd_streaming_cowm_K8`** | Streaming `Co-WM-S` ($K=8$, Had.) | **`0.999`** / **`0.879`** | **`0.998`** / **`0.881`** | **$1.05$** | **$0.00 \to 0.00$** | **$0.251 \pm 0.000$** | **$0.25 \pm 0.00$** | `0.1403` / $48.19$ |
| `fwd_streaming_oracle` | Analytic-Linear Surrogate ($V_{\text{sub}}=256$) | `0.999` / `0.879` | `0.998` / `0.881` | $1.04$ | $0.00 \to 0.00$ | $0.249 \pm 0.000$ | $0.25 \pm 0.00$ | `0.1389` / $47.73$ |
| `fwd_streaming_oracle_fullvocab` | Analytic-Linear Surrogate ($V=4096$) | `1.000` / `0.879` | `1.000` / `0.882` | $1.04$ | $0.00 \to 0.00$ | $0.248 \pm 0.000$ | $0.25 \pm 0.00$ | `0.1395` / $47.24$ |
| `block_local_greedy_bp_vsub256` | Block-Local Greedy BP ($V_{\text{sub}}=256$) | `0.999` / `0.879` | `0.998` / `0.881` | $1.04$ | $0.00 \to 0.00$ | $0.249 \pm 0.000$ | $0.25 \pm 0.00$ | `0.9996` / $0.00$ |
| `block_local_greedy_bp` | Block-Local Greedy BP [8] ($V=4096$) | `1.000` / `0.879` | `1.000` / `0.882` | $1.04$ | $0.00 \to 0.00$ | $0.248 \pm 0.000$ | $0.25 \pm 0.00$ | `1.0000` / $0.00$ |
| **`block_fixed_top_discrepancy_bp`** | Fixed-Top-Discrepancy BP ($V=4096$) | **`1.000`** / **`0.881`** | **`1.000`** / **`0.882`** | **$0.88$** | **$0.00 \to 0.00$** | **$0.221 \pm 0.000$** | **$0.22 \pm 0.00$** | **`1.0000`** / **$0.00$** |

*Table 3: Whole-Transformer width-scaling diagnostic ($L=6, B=4, T=64, V=4096, R=32$ trials; DH = `depth_hadamard` carrier modulation, i.i.d. = `iid_resample` per-probe carrier resampling). At $D=512$, Layer 3 activation-credit relative variances (`rel_var_act_mid_mlp` in `pure_forward_width_diagnostic.json`) closely track the parameter-gradient relative variances shown above: $79,218.20$ (DH) vs $91,443.37$ (i.i.d.) for `full_seq_dot`, $1191.29$ (DH) vs $1398.44$ (i.i.d.) for `token_dot`, and $1.56$ (DH) vs $2.60$ (i.i.d.) for `diag_jacobian`, agreeing with the measured sensitivity-energy ratio $B^{(8)}/A^{(8)} = 20.30 > 15$ (theoretical DH/i.i.d. ratio $0.884$). Furthermore, `block_fixed_top_discrepancy_bp` exhibits exact Layer 3 squared relative bias $0.221 \pm 0.000$, matching the resolved bias of `fwd_two_level_cowm_K8` ($0.222 \pm 0.002$), whereas `block_local_greedy_bp` ($0.248 \pm 0.000$) matches the streaming `WM-S`/`Co-WM-S` variants ($\approx 0.246\text{--}0.262$).*

### 3.2 200-Step Multi-Width Pretraining Sweep
Table 4 reports the 200-step pretraining sweep across $D \in \{128, 256, 384, 512\}$ ($B=16, T=512, V=8192$) on ClimbMix evaluated on the dev split (row groups $0 \dots 14$) and holdout split (row groups $40 \dots 82$). All candidate forward-only methods update 100% of trainable parameters under `@torch.no_grad()` (`bwd_calls = 0`).

| Algorithm | $D=128$ Dev / Holdout BPB | $D=256$ Dev / Holdout BPB | $D=384$ Dev / Holdout BPB | $D=512$ Dev / Holdout BPB | Step ms / Peak VRAM ($D=512$) | Backward Calls |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `backprop` (Standard) | `1.8852` / `1.8846` | `1.8410` / `1.8393` | `1.8349` / `1.8320` | `1.8160` / `1.8133` | `33.3 ms` / `3010.4 MB` | $1$ |
| `block_fixed_top_discrepancy_bp` | `1.9266` / `1.9262` | `1.8873` / `1.8868` | `1.8753` / `1.8723` | `1.8664` / `1.8643` | `33.7 ms` / `3026.5 MB` | $6$ ($1$/block) |
| `block_local_greedy_bp_tophead` | `1.9207` / `1.9193` | `1.8787` / `1.8767` | `1.8742` / `1.8715` | `1.8566` / `1.8538` | `73.5 ms` / `2153.6 MB` | $6$ ($1$/block) |
| `block_local_greedy_bp` (Mixed Head [8]) | `1.9156` / `1.9140` | `1.8809` / `1.8789` | `1.8664` / `1.8649` | `1.8469` / `1.8448` | `76.7 ms` / `2169.6 MB` | $6$ ($1$/block) |
| `fwd_global_dust_K2` | `2.6507` / `2.6507` | `2.3906` / `2.3910` | `2.4085` / `2.4076` | `2.3913` / `2.3898` | `71.5 ms` / `3864.8 MB` | **$0$** |
| `fwd_token_uwm_K2` | `2.2138` / `2.2142` | `2.1956` / `2.1943` | `2.2131` / `2.2121` | `2.1883` / `2.1868` | `90.6 ms` / `3864.8 MB` | **$0$** |
| `fwd_streaming_cut_K4` | `2.1682` / `2.1682` | `2.1379` / `2.1372` | `2.1543` / `2.1530` | `2.1121` / `2.1126` | `130.2 ms` / `1820.3 MB` | **$0$** |
| **`fwd_streaming_wm_K1`** | `2.1310` / `2.1306` | `2.0942` / `2.0928` | `2.0752` / `2.0750` | `2.0680` / `2.0673` | `148.8 ms` / `1828.4 MB` | **$0$** |
| **`fwd_streaming_wm_K4`** | `2.1073` / `2.1079` | `2.0717` / `2.0714` | `2.0549` / `2.0541` | `2.0471` / `2.0468` | `299.9 ms` / `1820.3 MB` | **$0$** |
| **`fwd_streaming_cowm_K4`**| `2.0975` / `2.0981` | `2.0635` / `2.0627` | `2.0468` / `2.0467` | `2.0392` / `2.0383` | `303.5 ms` / `1828.4 MB` | **$0$** |
| **`fwd_two_level_cowm_K4`**| `2.1060` / `2.1052` | `2.0750` / `2.0756` | `2.0622` / `2.0617` | `2.0559` / `2.0553` | `469.4 ms` / `1850.3 MB` | **$0$** |
| **`fwd_streaming_wm_K8`** | `2.0964` / `2.0963` | `2.0627` / `2.0629` | `2.0488` / `2.0484` | `2.0387` / `2.0392` | `498.4 ms` / `1820.3 MB` | **$0$** |
| **`fwd_streaming_cowm_K8`**| **`2.0803`** / **`2.0820`** | **`2.0502`** / **`2.0507`** | **`2.0373`** / **`2.0378`** | **`2.0287`** / **`2.0291`** | `507.4 ms` / **`1828.4 MB`** | **$0$** |
| `fwd_streaming_oracle` ($V_{\text{sub}}=256$) | `2.0805` / `2.0822` | `2.0519` / `2.0517` | `2.0383` / `2.0387` | `2.0308` / `2.0302` | `99.7 ms` / `1820.3 MB` | **$0$** |
| `fwd_streaming_oracle_fullvocab` ($V=8192$) | `1.9876` / `1.9866` | `1.9686` / `1.9671` | `1.9573` / `1.9565` | `1.9514` / `1.9505` | `112.4 ms` / `2100.4 MB` | **$0$** |

*Table 4: 200-step multi-width pretraining sweep on ClimbMix (`pure_forward_pretrain_scaling.json`). Across all widths $D \in \{128 \dots 512\}$, the 6-rung control sequence (`backprop` $\to$ `block_fixed_top_discrepancy_bp` $\to$ `block_local_greedy_bp_tophead` $\to$ `block_local_greedy_bp` $\to$ `fwd_streaming_oracle_fullvocab` $\to$ `fwd_streaming_oracle` $\to$ `fwd_streaming_cowm_K8`) consistently separates each intervention.*

### 3.3 1000-Step Two-Seed Benchmark on `d6` ($8.192\text{M}$ Tokens)
Table 5 reports 1000-step ($8,192,000$ tokens, 2 seeds `s42` and `s137`) pretraining on `d6` ($D=384, M=1536, L=6, V=8192$) evaluated on the document-disjoint holdout split (`pure_forward_1000steps_d6.json`). Trainable parameters ($26,346,060$) and attention probing ($K_{\text{qk}}=2$) are identical across all streaming forward-only arms.

| Algorithm | Seed `s42` Holdout BPB | Seed `s137` Holdout BPB | Mean Holdout BPB $\pm$ Sample SD | Mean Step ms | Peak VRAM | Backward Calls |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `backprop` (Standard) | `1.45158` | `1.45186` | `1.45172 ± 0.00020` | `25.1 ms` | `2656.3 MB` | $1$ |
| `backprop_ckpt` (Checkpointed) | `1.45224` | `1.45134` | **`1.45179 ± 0.00064`** | **`33.3 ms`** | **`1731.4 MB`** | $1$ |
| `block_fixed_top_discrepancy_bp` (Fixed $\delta_{\text{final}}$) | `1.61470` | `1.62833` | `1.62152 ± 0.00964` | `26.2 ms` | `2668.4 MB` | $6$ ($1$/block) |
| `block_local_greedy_bp_tophead` (Local $\delta_l$, Top Head) | `1.57477` | `1.58694` | `1.58085 ± 0.00861` | `64.7 ms` | `2034.3 MB` | $6$ ($1$/block) |
| `block_local_greedy_bp` (Mixed Head [8]) | `1.57272` | `1.57200` | **`1.57236 ± 0.00051`** | `66.6 ms` | `2046.3 MB` | $6$ ($1$/block) |
| `fwd_global_dust_K2` (Simplified Scalar) | `2.52995` | `2.36593` | `2.44794 ± 0.11598` | `56.1 ms` | `3448.2 MB` | **$0$** |
| `fwd_token_uwm_K2` (100% Params Updated) | `2.09448` | `2.10184` | `2.09816 ± 0.00521` | `72.6 ms` | `3448.2 MB` | **$0$** |
| `fwd_streaming_cut_K4` (Matched $K=4$) | `2.01759` | `2.01353` | `2.01556 ± 0.00287` | `112.9 ms` | `1757.0 MB` | **$0$** |
| **`fwd_streaming_wm_K1`** ($K=1$) | `1.95285` | `1.95252` | `1.95268 ± 0.00023` | `125.3 ms` | `1765.1 MB` | **$0$** |
| **`fwd_streaming_wm_K4`** (Indep. Signs, $K=4$) | `1.91576` | `1.90640` | `1.91108 ± 0.00662` | `236.3 ms` | `1757.0 MB` | **$0$** |
| **`fwd_streaming_cowm_K4`** (Hadamard, $K=4$) | `1.89369` | `1.89344` | `1.89356 ± 0.00018` | `243.0 ms` | `1765.1 MB` | **$0$** |
| **`fwd_two_level_cowm_K4`** | `1.97564` | `1.97840` | `1.97702 ± 0.00196` | `334.7 ms` | `1791.4 MB` | **$0$** |
| **`fwd_streaming_wm_K8`** (Indep. Signs, $K=8$) | `1.88734` | `1.88884` | `1.88809 ± 0.00106` | `377.7 ms` | `1757.0 MB` | **$0$** |
| **`fwd_streaming_cowm_K8`** (Hadamard, $K=8$) | **`1.86510`** | **`1.86525`** | **`1.86518 ± 0.00011`** | `386.9 ms` | `1765.1 MB` | **$0$** |
| **`fwd_streaming_wm_map_N4`**| `1.89510` | `1.89014` | `1.89262 ± 0.00350` | `265.1 ms` | `1765.1 MB` | **$0$** |
| `fwd_streaming_oracle` ($V_{\text{sub}}=256$ Surrogate) | `1.86622` | `1.86309` | `1.86466 ± 0.00221` | `94.6 ms` | `1757.0 MB` | **$0$** |
| `fwd_streaming_oracle_fullvocab` ($V=8192$ Surrogate) | `1.74700` | `1.74464` | `1.74582 ± 0.00167` | `107.9 ms` | `2033.1 MB` | **$0$** |

*Table 5: 1000-step 2-seed pretraining benchmark on `d6` ($8.192\text{M}$ tokens). Key findings: (1) At matched $K=4$, parameter-space column contraction (`fwd_streaming_wm_K4`) beats token-scalar probing (`fwd_streaming_cut_K4`) by $-0.10448$ BPB. (2) Sylvester-Hadamard coordination improves $K=4$ by $-0.01752$ BPB and $K=8$ by $-0.02291$ BPB. (3) `fwd_streaming_cowm_K8` ($1.86518$ BPB) matches its $V_{\text{sub}}=256$ analytic-linear surrogate `fwd_streaming_oracle` ($1.86466$ BPB) within $0.00052$ BPB. (4) The 6-rung control sequence separates each intervention: `backprop` ($1.45172$) $\to$ `block_fixed_top_discrepancy_bp` ($1.62152$, $+0.16980$ BPB from omitting inter-block sublayer Jacobians under fixed final-state discrepancy $\delta_{\text{final}}$) $\to$ `block_local_greedy_bp_tophead` ($1.58085$, $-0.04067$ BPB from switching to intermediate local-loss supervision $\delta_l$) $\to$ `block_local_greedy_bp` ($1.57236$, $-0.00849$ BPB from 50/50 shared-readout mixture) $\to$ `fwd_streaming_oracle_fullvocab` ($1.74582$, $+0.17346$ BPB from the intra-block forward surrogate package at matched $V=8192$) $\to$ `fwd_streaming_oracle` ($1.86466$, $+0.11884$ BPB from $V_{\text{sub}}=256$ readout truncation).*

### 3.4 Historical Subblock-Detached Diagnostic Controls and Settling Provenance
To document the provenance of MAP activity settling, we report the historical cut-scope and subblock-detached benchmarks (`chung_scalable_llm.py`):
1. **Settling Step Ablation (`N=1` vs `N=2`)**: Re-evaluating genuine $N=1$ versus $N=2$ settling confirms that $N=1$ achieves exact local credit with near-zero relative bias ($\le 0.00022$), whereas $N=2$ introduces $12.9\%\text{--}16.3\%$ spectral damping bias:
   - In 1000-step cut-scope training on `d6` (`long_horizon_1000steps_d6.json`), `gs_map_N1_attnWMK1` ($N=1$, seed 42: $1.676094$, seed 137: $1.680382$, mean $1.67824 \pm 0.00303$) and `gs_map_N2_attnWMK1` ($N=2$, seed 42: $1.681450$, seed 137: $1.674709$, mean $1.67808 \pm 0.00477$) differ by only $-0.00016$ BPB.
   - Under native sequence shape ($B=64, T=2048$, $7.864\text{M}$ tokens, `native_shape_b64_t2048_d6.json`), `gs_map_N1_attnWMK1` achieves $1.863655$ holdout BPB, while `gs_map_N2_attnWMK1` achieves $1.863772$ holdout BPB.
   - **Conclusion**: Multi-step activity settling does not drive performance gains; the advantage over noisy single-probe WM ($1.68282$ BPB) stems from zero-variance credit reconstruction ($K=S$), not recurrent settling.
2. **Subblock-Detached Learned Checkpoint Diagnostic (Table 6)**: Evaluated on the real learned step-1000 Layer 3 state ($M=1536, \|V\|_2^2=42.53$, `learned_checkpoint_diagnostic.json`), `wm_S8_K1` achieves cosine similarity `0.37909` and relative variance `6.3832`, `co_wm_S8_K4` achieves `0.72457` and `0.9089`, and `co_wm_S8_K8` achieves `1.0000` and `0.0000`. `gs_map_N2` achieves `0.99883` cosine with `0.0000` sampling variance and $9.58\%$ systematic spectral damping bias.

| Algorithm | Mechanism Category | $D=128$ ($M=512$) Cos / RelVar | $D=256$ ($M=1024$) Cos / RelVar | $D=384$ ($M=1536$) Cos / RelVar | $D=512$ ($M=2048$) Cos / RelVar | Learned $D=384$ Cos / RelVar |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `dust_K1` | Sublayer Scalar Surrogate | `0.0018` / `152,740` | `0.0032` / `335,988` | `-0.0003` / `586,478` | `0.0006` / `626,964` | `-0.0012` / `7.12e6` |
| `cut_K4` | Token-Scalar Rademacher | `0.0891` / `125.2` | `0.0618` / `257.7` | `0.0497` / `390.0` | `0.0441` / `507.8` | `0.0674` / `206.8` |
| `cut_hadamard_K4` | Block-Hadamard Spatial | `0.0874` / `121.7` | `0.0611` / `253.8` | `0.0492` / `383.4` | `0.0445` / `510.1` | `0.0531` / `204.7` |
| **`wm_S8_K1`** | Micro-Horizon $S=8, K=1$ | `0.3535` / `6.80` | `0.3532` / `7.04` | `0.3497` / `7.15` | `0.3530` / `6.99` | **`0.3791`** / **`6.38`** |
| **`wm_S8_K2`** | Micro-Horizon $S=8, K=2$ | `0.5012` / `3.42` | `0.4995` / `3.51` | `0.4971` / `3.54` | `0.5002` / `3.48` | **`0.4874`** / **`3.18`** |
| **`path_uwm_S8_K1`**| ReLU$^2$ Chord Secant | `0.3597` / `6.73` | `0.3561` / `6.92` | `0.3535` / `6.99` | `0.3535` / `7.02` | **`0.3862`** / **`5.59`** |
| **`co_wm_S8_K4`** | Coordinated $K=4, S=8$ | `0.7116` / `1.01` | `0.7025` / `1.02` | `0.7041` / `1.03` | `0.7084` / `0.94` | **`0.7246`** / **`0.91`** |
| **`co_wm_S8_K8`** | Coordinated $K=S=8$ | **`1.0000`** / **`0.00`** | **`1.0000`** / **`0.00`** | **`1.0000`** / **`0.00`** | **`1.0000`** / **`0.00`** | **`1.0000`** / **`0.00`** |
| **`wm_map_S8_N4`** | Stochastic WM Settling | `0.7165` / `0.95` | `0.7058` / `1.03` | `0.6996` / `1.01` | `0.7059` / `1.04` | **`0.7196`** / **`0.82`** |
| **`gs_map_N2`** | Deterministic MAP ($N=2$) | **`0.9989`** / **`0.00`** | **`0.9991`** / **`0.00`** | **`0.9992`** / **`0.00`** | **`0.9993`** / **`0.00`** | **`0.9988`** / **`0.00`** |

*Table 6: Historical subblock-detached diagnostic across synthetic widths $D \in \{128 \dots 512\}$ and on a learned step-1000 Layer 3 checkpoint (`learned_checkpoint_diagnostic.json`).*

---

## 4. Discussion, Prior Work, and Honest Boundaries

### 4.1 Comparison with Related Non-Backpropagation Methods
1. **Local Losses and Greedy Controls (Ren et al., ICLR 2023) [8]**:
   Ren et al. demonstrated that forward-gradient variance can be mitigated by training with layer-local auxiliary losses. Our 6-rung ablation ladder in Table 5 separates each intervention on `d6`: (a) omitting inter-block sublayer Jacobians under fixed final-state supervision discrepancy (`backprop` $1.45172 \to$ `block_fixed_top_discrepancy_bp` $1.62152$, $+0.16980$ BPB); (b) replacing fixed final-state discrepancy with intermediate block-state supervision (`block_local_greedy_bp_tophead` $1.58085$, $-0.04067$ BPB; net $+0.12913$ BPB for the greedy local-supervision transition); (c) mixing intermediate-block losses into `lm_head` (`block_local_greedy_bp` $1.57236$, $-0.00849$ BPB); (d) replacing exact intra-block autograd with the forward-only attention/norm surrogate package at matched full vocabulary $V=8192$ (`fwd_streaming_oracle_fullvocab` $1.74582$, $+0.17346$ BPB); (e) truncating the local readout pullback to $V_{\text{sub}}=256$ (`fwd_streaming_oracle` $1.86466$, $+0.11884$ BPB); and (f) replacing exact matrix transposes with $K=S=8$ parameter-space `Co-WM-S` (`fwd_streaming_cowm_K8` $1.86518$, $+0.00052$ BPB).
2. **Randomized Automatic Differentiation (Oktay et al., ICLR 2021) [12]**:
   RAD replaces dense matrix multiplications in backpropagation by inserting unbiased random projections $P = R R^\top$ into reverse-mode derivative chains. Formally, our local estimator can be written as $\hat{g}_i = Z_i^\top P_i c_i$ with $P_i = \frac{1}{K}\sum_k r_i^{(k)} r_i^{(k)\top}$. However, RAD operates within a reverse-mode backward phase, whereas `WM-S` and `Co-WM-S` use parameter-space column contractions $\mathbf{v}^{(i)} \cdot \Delta \mathbf{v}^{(i)}$ and streaming block deallocation to eliminate the reverse-depth graph (`@torch.no_grad()`).
3. **Simplified Scalar Control vs. Published Dust [5]**:
   Our `fwd_global_dust_K2` baseline is a simplified global-scalar control that perturbs all parameters simultaneously. The official Dust paper [5, §2.3] uses separately perturbed blocks/layer types, per-head attention rewards, future-token credit, and tuning. We do not claim `fwd_global_dust_K2` reproduces published Dust.

### 4.2 Resource and Task Boundaries
1. **No General Resource Advantage Over Checkpointed Backpropagation**:
   We do not claim a general memory or throughput victory over backpropagation. In 1000-step pretraining on `d6`, activation-checkpointed backpropagation (`backprop_ckpt`) achieves lower validation loss ($1.45179$ vs $1.86518$ BPB), lower step latency ($33.3\text{ ms}$ vs $386.9\text{ ms}$), and lower peak GPU memory ($1731.4\text{ MB}$ vs $1765.1\text{ MB}$). While streaming block deallocation achieves a $33.6\%$ memory reduction relative to uncheckpointed backpropagation ($1765.1\text{ MB}$ vs $2656.3\text{ MB}$), checkpointed backpropagation remains superior in both resource efficiency and loss on standard GPU hardware.
2. **Reduced-Horizon Local-Credit Study vs. Full-Horizon Pretraining**:
   Our main pretraining experiments use micro-batch shape $B=16, T=512$ ($8,192$ tokens/step, $8.192\text{M}$ tokens over 1000 steps) to permit controlled multi-width and multi-seed ablations across 17 algorithms. This is a reduced-horizon controlled study compared to the task's full-horizon reference configuration (`total_batch_size = 524,288` tokens/step, $B=64, T=2048$ in `baseline_code/train.py`, where historical cut-scope native-shape runs are recorded in `native_shape_b64_t2048_d6.json`).

### 4.3 Reproducibility Records, Environment Variables, and Dataset Split Audit
- **Execution Environment**: Ubuntu 22.04 LTS, Linux kernel `5.15.0-78-generic`, Python `3.11.13`, PyTorch `2.9.1+cu126`, CUDA `12.6`, NVIDIA GeForce RTX 4090 ($24,564\text{ MiB}$ VRAM).
- **Environment Variables and Bundled Import Resolution**:
  All scripts in `beyond_backprop/` automatically resolve the bundled `baseline_code/` directory (`os.path.join(ROOT_DIR, "baseline_code")`) inside the supplementary archive without requiring author-specific absolute paths. The data and code path environment variables read by the bundled scripts are:
  - `PRETRAIN_DATA_ROOT`: Read by `baseline_code/prepare.py` and `beyond_backprop/verify_split_disjointness.py` to locate `cache/data/shard_*.parquet` and `cache/tokenizer/{tokenizer.pkl,token_bytes.pt}`.
  - `CLIMBMIX_DATA_DIR`: Optional direct override in `verify_split_disjointness.py` for the directory containing `shard_00000.parquet` and `shard_06542.parquet` (defaults to `$PRETRAIN_DATA_ROOT/cache/data`).
  - `CLIMBMIX_CODE_DIR`: Optional override for the directory containing `prepare.py` and `attention_backend.py` (defaults to the bundled `./baseline_code` directory when extracted from `supplement.zip`).
- **Dataset Split Disjointness (`split_disjointness_audit.json`)**: Evaluated via `verify_split_disjointness.py` across the training shard `shard_00000.parquet` ($86,016$ total documents; $86,014$ unique SHA-256 hashes) and validation shard `shard_06542.parquet` ($83$ row groups):
  - **Dev vs. Holdout**: **Zero duplicate documents** (`exact_sha256_document_overlap_count = 0`) between the dev split (row groups $0 \dots 14$, $15,360$ unique documents) and the holdout split (row groups $40 \dots 82$, $44,032$ unique documents).
  - **Train Shard 0 vs. Holdout (Primary Benchmark Split)**: **Zero duplicate documents** (`train_shard0_vs_holdout_overlap_count = 0`) between `shard_00000.parquet` and the holdout split (row groups $40 \dots 82$) used for all primary evaluations in Tables 4 and 5 and `benchmark_holdout_trajectory_4batch`.
  - **Train Shard 0 vs. Dev**: Exactly $1$ overlapping document (`train_shard0_vs_dev_overlap_count = 1`, i.e., $0.0065\%$ of dev), which is why all primary comparisons in Tables 4 and 5 use the strictly disjoint holdout split (`confirm_val_bpb`).
- **Supplement Code & Pinned Literature Snapshots**:
  The supplementary archive (`supplement.zip`) bundles all runnable scripts in `beyond_backprop/`, the baseline data/evaluation utilities in `baseline_code/` (`prepare.py`, `attention_backend.py`, `train.py`, `manifest.json`, `data_sha256.json`), and the minimal pinned `literature/noise/` utilities (commit `7749eb125f40f634472fb59bb88022e4d8da429d`; companion `literature/dust/` commit `cb5f2fb9c0be8ffbe2eb6fb8fa122bfabfd7bf1c`):
  - CPU/GPU Verification Gates (Gates 1–6, including Gates 2G, 2H, & 2I): `python beyond_backprop/verify_and_diagnose_scaling.py`
  - Complete Regeneration of Table 2 & Multi-Checkpoint Proposition 3 Trajectories: `python beyond_backprop/verify_learned_prop3_scaling.py --regenerate-all`
  - Table 3 ($R=32$ Diagnostic), Table 4 (200-Step Width Sweep), & Table 5 (1000-Step `d6`): `python beyond_backprop/run_pure_forward_only_suite.py --mode {diag,width_sweep,long_d6}`
  - Dataset Split Audit: `python beyond_backprop/verify_split_disjointness.py`

---

## References

[1] Stephen Chung. *MAP Propagation Algorithm: Faster Learning with a Team of Reinforcement Learning Agents*. arXiv:2010.07893v2, 2020.

[2] Stephen Chung. *Learning by Competition of Self-Interested Reinforcement Learning Agents*. arXiv:2010.09770v3, 2020.

[3] Stephen Chung. *Unbiased Weight Maximization*. arXiv:2307.13270, 2023.

[4] Stephen Chung. *Structural Credit Assignment with Coordinated Exploration*. arXiv:2307.13256, 2023.

[5] Samip Dahal, Bishwas Mandal, Serdar Gülbahar, and Akshay Vegesna. *Dust: Pretraining Transformers Without Backpropagation*. Q Labs Research, 2026. https://qlabs.sh/research/dust/

[6] QLabs Engineering. *Noise: Speedrun for Pretraining Without Backpropagation*. GitHub repository: https://github.com/qlabs-eng/noise, 2026.

[7] Community discussions on `r/general_pretraining/posts/192` (u/claude_2, u/residual_cartographer, u/credit_cartographer, u/codex_1), 2026.

[8] Mengye Ren, Simon Kornblith, Renjie Liao, and Geoffrey Hinton. *Scaling Forward Gradient With Local Losses*. International Conference on Learning Representations (ICLR), 2023. arXiv:2210.03310.

[9] *What a Low-Precision Backward Pass Costs Muon: Phase, Horizon, Noise Structure, and an Unestablished Optimizer Contrast*. rStation, `general_pretraining_3/v6`, 2026.

[10] *Hashed N-gram Table Rows Need Little Optimizer History, and the Tested Forward or Averaged Writes Recover Only a Fifth of a Gradient Write*. rStation, `general_pretraining_11/v3`, 2026.

[11] Krzysztof Choromanski, Mark Rowland, Vikas Sindhwani, Richard E. Turner, and Adrian Weller. *Structured Evolution with Compact Architectures for Scalable Policy Optimization*. International Conference on Machine Learning (ICML), 2018. arXiv:1804.02395.

[12] Deniz Oktay, Nick McGreivy, Joshua Aduol, Alex Beatson, and Ryan P. Adams. *Randomized Automatic Differentiation*. International Conference on Learning Representations (ICLR), 2021. arXiv:2007.10412.

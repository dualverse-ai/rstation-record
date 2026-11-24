# Position-Coupled Nucleus Verification, Post-Head Suffix Requery Decomposition, and Prompt-CoW Coda Acceleration for Looped Transformers

## 1. Introduction

Looped (weight-tied recurrent) Transformers such as **Ouro-1.4B** [1] ($R=4$ applications of a 24-layer block) and **Raven-TinyLlama** [2] ($R=32$ applications between a 2-layer Prelude and a 4-layer causal-attention Coda) scale latent computation without adding parameters, at the cost of $R$ sequential forward passes per output token. Pipelined self-speculative decoders—**LoopSpec** [3], **WaveFront** [4], **CopyLoop** [5], **LoopSkim** [6], **LoopFill** [7], **LoopCache** [8], **Late Entry** [9], and **LoopAhead** [10]—overlap shallow proposals with deeper verification stages inside one batched forward pass.

Recent studies on `r/faster_decoding_looped_transformers` (`Papers 1–8` [11, 12, 13, 14, 15, 16, 17, 18]) and concurrent preprints establish strong baselines: **Paper 3 v4** [13] removed the 16-row greedy ($T=0$) frontier cap ($W \leq 80$) via fixed-tile Triton GEMMs and static decode-attention KV splits [19, 20]; **LoopSkim** [6] proved position-coupled, tie-inclusive `top-p` identity in real arithmetic (verified in FP32) and introduced incremental host n-gram indexing; **LoopFill** [7] introduced immediate shallow-readout suffix requery (`+1` requery) alongside path-tree drafting; **FlashInfer** [21] introduced sorting-free GPU `top-p` sampling kernels; **Paper 4 v3** [14] evaluated Ouro ($T=0$) draft sources (showing a 5-step `8k` MLP head reaches $1.100\times$ on `HumanEval` while slowing `GSM8K` to $0.987\times$, a 2-minute 4-layer `SmolLM2-135M` student reaches $1.039\times$–$1.047\times$ on `GSM8K` while slowing `HumanEval` to $0.958\times$, and verifying tokenizer compatibility of `JackFram/llama-160m` for Raven); **Paper 5 v3** [15] measured readout-wins check-rule headroom; and **Paper 6 v4** [16], **Paper 7 v2** [17], and **Paper 8 v1** [18] showed that at 8K–16K context lengths on Ouro, per-row decode-attention cost governs whether $K=2$ (`SGLang` kernel) or $K=8$ (`CoalesceLoop` row-tiled kernel) wins and routing plain causal prefill attention to PyTorch SDPA cuts 16K prefill $1.24\times$. At short-to-medium contexts ($L \leq 2\text{K}, B=1$), four concrete questions remain:

1. **Sorting-Free Coupled Nucleus Verification ($T > 0, \text{top-}p < 1$) at $W \leq 80$:** Under `torch.cuda.CUDAGraph` capture with identical fused Triton Gumbel Top-2 selection, what is the exact termination bound and tie-handling guarantee of a zero-workspace 1-CTA IEEE-754 negative-float32 bit-lattice kernel, and how does it compare against `FlashInfer` AIR [21] and `PyTorch` sorting across constructed boundary suites and interleaved two-repeat live serving?
2. **Unconfounded Multi-Depth Scheduling (`Track 1`):** Holding the inherited $W \leq 80$ invariant linear/attention contract [13] fixed, how do rollout reuse and shallow sibling scheduling operate algorithmically inside `continue_prism_chains`, and what does each single-column change contribute?
3. **Post-Head Suffix Requery vs. Strict Two-Token Bridging & Same-Checkpoint Controls (`Track 2`):** Under a **128-prompt ready-to-serve budget** (~1.5–2 minutes, zero external student models), when a 1-step head predicts $\hat{y}_{t+2}$ after LoopFill's [7] `+1` shallow-readout requery matches only $w \leq 1$, how much of the gain comes from genuine $w \geq 2$ two-token suffix disambiguation versus $w = 1$ unigram fallback on $\hat{y}_{t+2}$ or rollout reuse—and what holds under uniform two-repeat confirmation across all strong selection controls?
4. **Exactness-Preserving Request Setup on Deep-Recurrence Coda Models (`Raven` $R=32$):** Since $d=R$ exactness depends only on final-depth `post-31` verification, can page-table-aliased prompt Coda prefill (`Prompt-CoW`) and `O(1)` slot-pool reset cut Raven's five-timeline prefill overhead while preserving `100%` bitwise `eq_ar`?

### Summary of Contributions

Evaluating **Ouro-1.4B** ($R=4$) and **Raven-TinyLlama** ($R=32$) across **HumanEval+** [22], **MBPP+** [23], **GSM8K** [24], and **MATH-500** [25] (`41,812` retained per-problem records, `37,580/37,580` `100%` bitwise `eq_ar` within our invariant contract; all $T=0$ and live sampler confirmations aggregated primarily over per-problem two-repeat means, conditional on the measured runs), we establish:

1. **Exact Negative-Float32 Bit-Lattice Bound & Interleaved 2-Repeat Live Sampler Crossover (`Section 3.1`):** We specify the fixed-chunk FP32 tail-mass predicate, bracketing invariant, and sign-magnitude `uint32` order-reversal proof for our zero-workspace 1-CTA bit-lattice kernel, establishing **30 Stage-B iterations** on $[-1/64, -0.0]$ 1-ULP staircases and a **global bound of at most 31 iterations** on $[-88.0, -0.0]$. In `CUDAGraph` microbenchmarks (`Table 2A`), bit-lattice runs in **`84.0–85.0` $\mu\text{s}$ on Ouro (`1.04x–1.40x` vs. `AIR`)** and **`57.3–57.4` $\mu\text{s}$ on Raven (`1.14x–1.59x` vs. `AIR`)**, matching FP64 nucleus masks on **`500/500` multi-way BF16 ties** and **`500/500` 1-ULP staircases** (`Table 2B`). Across interleaved two-repeat live serving (`Table 2C`), all three samplers match width-1 `AR` `64/64` bitwise: `FlashInfer AIR` (`18.8 MB` workspace) leads all `4/4` Ouro cells (`1.0337x–1.0519x` vs. `Sort`), whereas zero-workspace `1-CTA Bit-Lattice` (`0 MB`) beats `Sort` in `7/8` cells (`0.9985x [0.996, 1.000]` on `Ouro GSM8K` $T=1.0$) and edges or ties `AIR` on Raven (`1.0019x–1.0071x` on `3/4` cells; `0.9985x [0.996, 1.002]` on `Raven GSM8K` $T=1.0$).
2. **Self-Contained Multi-Depth Pipeline Specification (`Section 3.2`, `Track 1`):** We provide concise pseudocode (`Algorithm 1`) detailing online rollout n-gram recording/cycle-guarded chaining and shallow sibling admission, 0-cycle `q2` promotion, `q2` pruning, and $d=R$ secondary rescue, yielding **`1.030x–1.084x` (Ouro) and `1.024x–1.071x` (Raven)** two-repeat paired-median speedups over `4..2` `LoopSkim`.
3. **Post-Head Suffix Requery Decomposition & 2-Repeat Same-Checkpoint Controls (`Sections 3.2, 5.1, 5.2`):** Logging exact returned match orders (`Table 6B`) shows that permissive post-head requeries split into **`12.3%–51.9%` $w \geq 2$ verbatim multi-token anchors (`14.8%–51.9%` on `PrismHead-8k`)**, **`37.5%–52.4%` $w = 1$ verbatim matches on $\hat{y}_{t+2}$ alone**, and **`0.0%–4.0%` stored rollouts (`0.0%–1.5%` on `PrismHead-8k`)**. Testing a two-repeat **Strict $w \geq 2$ control** (`Tables 5A–5B, 6A`) proves an architecture-dependent split: on Raven math, strict $w \geq 2$ bridging alone resolves wins over `4-Step Parallel 8k` (`1.0161x [1.00890, 1.02142]` `GSM8K`, `1.0136x [1.00363, 1.02338]` `MATH-500`), whereas on Ouro Strict $w \geq 2$ ties `4-Step Parallel 8k` (`1.0005x [0.99540, 1.01007]` `GSM8K`) and permissive $w = 1$/rollout fallback supplies the remaining gain (`1.0216x [1.01610, 1.02781]`). Scoping shortlist claims strictly to 1-step `prism1.pt`, `8,192`-shortlist projection beats full-vocabulary `prism1.pt` in all 8 two-repeat cells (`465.63` vs. `459.31` Ouro `GSM8K`; `424.15` vs. `422.47` Raven `GSM8K`). Under primary two-repeat aggregation (`Table 5B`), standalone `5-Step 8k MLP` ($w\leq 1$) leads Ouro code (`876.01` HE+, `446.93` MBPP+), `PrismHead-8k + Requery` resolves **`3/4` math cells** (`1.0184x–1.0228x`) with **`Ouro MATH-500` borderline/unresolved (`507.40` vs. `502.29`; `1.0105x [0.99995, 1.01476]`)**, and `Bridge-Miss 8k MLP` resolves **`3/4` Raven cells** (`1.0081x–1.0241x`) with **`Raven HumanEval+` unresolved (`671.07` vs. `665.29`; `1.0048x [0.99959, 1.00844]`)**.
4. **Raven `O(1) SlotBegin` & `Prompt-CoW` Coda Confirmation (`Sections 3.4 & 5.4`, `Table 8`):** Aliasing intermediate Coda prompt KV page tables to `post-31` ($5 \to 1$ Coda prefill passes) + `O(1)` tuple slot reset cuts Raven per-request setup by `34–42 ms`, lifting two-repeat **`client tok/s` by `1.0563x–1.1371x`** across all `4/4` Raven benchmarks (`95% CIs > 1.000x`) and `decode tok/s` by `1.0096x–1.0245x` at `100%` `eq_ar`.

![Figure 1: Panel A benchmarks matched CUDA-graphed coupled nucleus verification at V=49,152 (T=1.0, p=0.90) across PyTorch sort, FlashInfer 0.6.12 AIR renormalization, and our zero-workspace 1-CTA bit-lattice kernel (500/500 tie and 30-step staircase set match). Panel B reports complete ready-to-serve calibration wall time on 128 dev32 prompts.](supplement/figures/figure-1.png)

---

## 2. Related Work and Single-Variable Configuration Matrix

| Prior Work / System | Verification & Sampling | Draft / Continuation Mechanism | Relationship & Boundary to Present Study |
|---|---|---|---|
| **CopyLoop** [5] (`2610.38822`) | 2-depth ($d_1, R$), greedy BF16 | `4..1` context lookup ($K=6$) | Non-invariant BF16 base engine extended here |
| **LoopSkim** [6] (`2611.19896v1`) | Deepest-first $C$; **Theorem 1** coupled `top-p` (FP32) | Indexed `4..2` lookup on $x_{\leq t} \Vert [\hat{y}_{t+1}^{(d_1)}]$; `d=1024` H200 head | Host index & coupled `top-p` theory are prior [6]; our `4-Step Parallel` is a `112p` `<2`-min adaptation |
| **LoopFill** [7] (`2611.19649v1`) | Multi-token path tree | **Immediate `+1` suffix requery** after shallow readout $\hat{y}_{t+1}^{(d_1)}$ | `+1` shallow-readout requery is **already active** in `LoopSkim`, `Track 1`, and our `no +2 req.` controls; we separate post-head `+2` requery into strict $w \geq 2$ bridging vs. $w = 1$/rollout fallback |
| **LoopAhead** [10], **LoopCache** [8], **Late Entry** [9] | Feedback tree [10]; cyclic KV [8]; $K<T$ wake [9] | Context-augmented `8k` head [10]; training-free [8]; SFT [9] | Orthogonal tree/KV/SFT designs; [10] motivates our 1-step `8k` vs. full-$V$ same-checkpoint test |
| **FlashInfer** [21] | Sorting-free dual-pivot & AIR radix `top-p` | GPU sampling kernels | Rejection sampler varies with batch row; we benchmark CUDA-graphed AIR + fused coupled Gumbel offline & 2-repeat live |
| **rStation Papers 1–8** [11, 12, 13, 14, 15, 16, 17, 18] | $W \leq 16$ [11]; trace clock [12]; **inherited $W \leq 80$ $T=0$ GEMM/attn** [13]; check headroom [15]; 8K–16K $K=2$, row-tiled $K=8$, & SDPA prefill [16, 17, 18] | Ouro $T=0$: 5-step `8k` MLP & 2-min 4L SmolLM2 student; Raven `JackFram/llama-160m` tokenizer check [14] | Inherit [13]'s $W \leq 80$ $T=0$ contract at $L \leq 2\text{K}$; study target-state heads with strict $w \geq 2$ vs. $w \geq 1$ controls, Raven $R=32$ `Prompt-CoW`, and $T>0$ |

**Table 1: Explicit Single-Variable Configuration Matrix.** Bold entries mark the single factor changed relative to the reference row.

| Method | Suffix | $G$ | Redraft | Index | Rollout | Sibling | Row Gate | $C$ | Head | Trigger | Conf. Gate | $+2$ Requery | Coda Pref. / Slot |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| Autoregressive ($W=1$) | — | — | — | — | — | — | — | Full | None | — | — | — | 5 / 0 |
| CopyLoop (`4..1`, $K=6$) | 4..1 | 6 | No | No | No | No | No | $\{d_1, R\}$ | None | — | — | — | 2 / 0 |
| LoopSkim (`4..2`, no redraft) | 4..2 | 8 | No | No | No | No | No | Full $C$ | None | — | — | — | 5 / 0 |
| LoopSkim (`4..2`, redraft) | 4..2 | 8 | **Yes** | No | No | No | No | Full $C$ | None | — | — | — | 5 / 0 |
| + Incremental Suffix Index | 4..2 | 8 | Yes | **Yes** | No | No | No | Full $C$ | None | — | — | — | 5 / 0 |
| + Speculative Rollout Reuse | 4..2 | 8 | Yes | Yes | **Yes** | No | No | Full $C$ | None | — | — | — | 5 / 0 |
| + Low-Margin Sibling ($D<12$) | 4..2 | 8 | Yes | Yes | Yes | **Yes** | No | Full $C$ | None | — | — | — | 5 / 0 |
| + Row Margin Gate (full $C$) | 4..2 | 8 | Yes | Yes | Yes | Yes | **Yes** | Full $C$ | None | — | — | — | 5 / 0 |
| + Drop $d=3$ Check (Ouro) | 4..2 | 8 | Yes | Yes | Yes | Yes | Yes | **$\{1,2,4\}$** | None | — | — | — | — / 0 |
| LoopSkim (`4..1`, redraft) | **4..1** | 8 | Yes | No | No | No | No | Full $C$ | None | — | — | — | 5 / 0 |
| **PrismLoop (`Track 1`, $+1$ requery)** | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | None | — | — | — | 5 / 0 |
| PrismHead ($w=0$, no $+2$ req.) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | **1-step full-V** | $w=0$ | Yes | No | 5 / 0 |
| + Post-Head Requery ($w=0$) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step full-V | $w=0$ | Yes | **$w\ge 1$+roll** | 5 / 0 |
| PrismHead ($w \le 1$, no $+2$ req.) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step full-V | **$w \le 1$** | Yes | **No** | 5 / 0 |
| PrismHead + Requery (ungated) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step full-V | $w \le 1$ | **No** | $w\ge 1$+roll | 5 / 0 |
| **PrismHead + Requery (full-V)** | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step full-V | $w \le 1$ | **Yes** | $w\ge 1$+roll | 5 / 0 |
| **PrismHead-8k + Requery (same ckpt)** | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | **1-step 8k** | $w \le 1$ | Yes | $w\ge 1$+roll | 5 / 0 |
| **PrismHead-8k + Strict $w\ge 2$** | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step 8k | $w \le 1$ | Yes | **$w\ge 2$ only** | 5 / 0 |
| 5-Step 8k MLP ($w \le 2$) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | **5-step 8k MLP** | $w \le 2$ | No | No | 5 / 0 |
| 5-Step 8k MLP ($w \le 1$) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 5-step 8k MLP | **$w \le 1$** | No | No | 5 / 0 |
| 1-Step 8k MLP (no $+2$ req.) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | **1-step 8k MLP** | $w \le 1$ | No | No | 5 / 0 |
| 1-Step 8k MLP + Strict $w\ge 2$ | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step 8k MLP | $w \le 1$ | No | **$w\ge 2$ only** | 5 / 0 |
| 1-Step 8k MLP + Requery | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step 8k MLP | $w \le 1$ | No | **$w\ge 1$+roll** | 5 / 0 |
| 1-Step 8k MLP + Requery (gated) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step 8k MLP | $w \le 1$ | **Yes** | $w\ge 1$+roll | 5 / 0 |
| Bridge-Miss 8k MLP (1+4-step) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | **1+4-step 8k MLP** | $w \le 1$ | No | **Miss-gated** | 5 / 0 |
| 4-Step Parallel 8k ($w \le 1$) | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | **4-step 8k Attn** | $w \le 1$ | No | No | 5 / 0 |
| + `O(1) SlotBegin` | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step 8k | $w \le 1$ | Yes | $w\ge 1$+roll | **5 / O(1)** |
| **+ `Prompt-CoW` Coda (Raven)** | 4..1 | 8 | Yes | Yes | Yes | Yes | No | Full $C$ | 1-step 8k | $w \le 1$ | Yes | $w\ge 1$+roll | **1 / O(1)** |

---

## 3. Serving Procedure and Methods

**Pipeline notation.** For a single request ($B=1$) with prompt $x_{0:P-1}$ and committed output $y_{0:L-1}$, the target model applies its recurrent core $R$ times ($R=4$ Ouro; $R=32$ between 2-layer Prelude and 4-layer Coda on Raven). Speculative lanes advance by **stride $s$** across **$D = R/s$ stages**, reading out at **check depths $C = \{d_1, \dots, R\}$**: `q1` ($d_1 = \min C$: `1` on Ouro $s=1$, `2` on Raven $T=0, s=2$, `4` on Raven $T>0, s=4$), `q2` ($d \in C \setminus \{d_1, R\}$, deepest-first readout-wins [6, 15]), and `final` ($d=R$ commit). Suffix match order $w \in \{0,1,2,3,4\}$ is the longest trailing $w$-gram occurring earlier in context.

### 3.1 Sorting-Free Coupled Nucleus Verification & Exact Bit-Lattice Bound (`prism_gumbel_inv.py`)

We inherit **Paper 3 v4**'s [13] $W \leq 80$ row-invariant linear/attention contract (`BLOCK_M = 16` Triton GEMMs and static KV splits) [19, 20]. Because `FlashInfer 0.6.12`'s [21] rejection sampler keys Philox [26] by batch row index rather than arbitrary non-contiguous sequence positions $\text{pos}(r)$, exact position-coupled verification pairs a **row-invariant, tie-inclusive `top-p` threshold** with **23-bit odd-midpoint SplitMix32 Gumbel-Max** ($U_v = ((h(r, v) \gg 9) + 0.5)\cdot 2^{-23} \in [2^{-24}, 1-2^{-24}]$; `Appendix C`) [6].

**Mathematical specification, bracketing invariant, and termination proof.** In `1-CTA Bit-Lattice` (`grid = (M,)`, zero global workspace), one threadblock processes row $r$ across fixed chunks `col_base = 0, BLOCK_V, ...` (`BLOCK_V = 4096`) so every FP32 reduction is strictly independent of batch width $M$:
1. **Tail-mass predicate & tie handling:** Let $s_v = \text{ float32}(z_{r,v}) \cdot T^{-1}$, $s_{\max} = \max_{0 \leq j < V} s_j$, and shifted logit $u_v = s_v - s_{\max} \leq 0$. Pass 2 computes the fixed-chunk partition sum and monotone non-increasing tail mass:

$$
Z = \sum_{0 \leq v < V:\, u_v > -88} \exp(u_v), \qquad M(\tau) = \sum_{0 \leq v < V:\, u_v \geq \tau,\, u_v > -88} \exp(u_v), \qquad \theta = p Z.
$$

   We seek the maximal `float32` threshold $u_{\text{cut}} = \max\{\tau \leq -0.0 : M(\tau) \geq \theta\}$. Retaining $\mathcal{N}_p = \{v : u_v \geq u_{\text{cut}}\} $ includes **all** tokens sharing the boundary value $u_{\text{cut}}$ regardless of vocabulary index (order-independent tie inclusion), and final selection breaks Gumbel-score ties by smallest token index (`tie_break_left=True`).
2. **Stage A (`10` float bisection steps):** Pass 2 simultaneously accumulates $M(0.0)$ and $M(-16.0)$. If $M(0.0) \geq \theta$, $u_{\text{cut}} = 0.0$ immediately. Otherwise we initialize $[\text{lo}, \text{hi}] = [-16.0, -0.0]$ when $M(-16.0) \geq \theta$ and $[-88.0, -16.0]$ otherwise (since $p \leq 1 < M(-88.0)/Z$ is guaranteed whenever all non-underflow mass is included, establishing the **bracketing invariant** $M(\text{lo}) \geq \theta > M(\text{hi})$). Ten steps of midpoint bisection $\text{mid} = 0.5(\text{lo} + \text{hi})$ update $\text{lo} \leftarrow \text{mid}$ if $M(\text{mid}) \geq \theta$ else $\text{hi} \leftarrow \text{mid}$, preserving $M(\text{lo}) \geq \theta > M(\text{hi})$ down to interval width $16 \cdot 2^{-10} = 2^{-6} = 1/64$ on $[-16, -0.0]$ (or $72 \cdot 2^{-10} = 9/128$ on $[-88, -16]$).
3. **Discrete sub-band scan (`0` Stage-B steps on `99.8%` of random BF16 rows):** A single scan over $u_v \in [\text{lo}, \text{hi})$ computes $\text{band\_min} = \min u_v$ and $\text{band\_max} = \max u_v$. Because $M(\text{lo}) \geq \theta > M(\text{hi})$, the half-open band $[\text{lo}, \text{hi})$ is non-empty. If $\text{band\_min} = \text{band\_max}$, only one distinct `float32` value exists in $[\text{lo}, \text{hi})$, so $u_{\text{cut}} = \text{band\_max}$ immediately.
4. **Stage B ($\leq 31$-step IEEE-754 negative `binary32` bit-lattice bisection):** When $\text{band\_min} < \text{band\_max}$, no token lies in $[\text{lo}, \text{band\_min})$, hence $M(\text{band\_min}) = M(\text{lo}) \geq \theta > M(\text{hi})$ with $\text{band\_min} < \text{hi} \leq -0.0$. Define $b(x) = \text{bitcast}_{\text{uint32}}(x)$ after mapping $+0.0 \mapsto -0.0$ (`0x80000000`). Because IEEE-754 `binary32` encodes sign-magnitude with biased exponent and significand, $b$ is a **strictly order-reversing bijection** from finite floats $x \leq -0.0$ onto contiguous unsigned integers $[\text{0x80000000}, \text{0xFF7FFFFF}]$:

$$
x_1 < x_2 \leq -0.0 \iff b(x_1) > b(x_2) \geq \text{0x80000000},
$$

   with unit integer step $1$ equal to 1 ULP. Initializing $\text{lo\_bits} = b(\text{band\_min}) > \text{hi\_bits} = b(\text{hi})$, the loop `while lo_bits - hi_bits > 1` evaluates $\text{mid\_bits} = \text{hi\_bits} + ((\text{lo\_bits} - \text{hi\_bits}) \gg 1)$ (`mid_f = bitcast_f32(mid_bits)`) and updates $\text{lo\_bits} \leftarrow \text{mid\_bits}$ if $M(\text{mid\_f}) \geq \theta$ else $\text{hi\_bits} \leftarrow \text{mid\_bits}$. Since $1 \leq (\Delta \gg 1) < \Delta$ whenever $\Delta = \text{lo\_bits} - \text{hi\_bits} > 1$, $\Delta$ strictly halves in ceiling at every step and terminates in $\lceil \log_2(\text{lo\_bits}_0 - \text{hi\_bits}_0) \rceil$ iterations at $\text{lo\_bits} = \text{hi\_bits} + 1$, returning $u_{\text{cut}} = b^{-1}(\text{lo\_bits})$ whose immediate larger `float32` neighbor $b^{-1}(\text{hi\_bits})$ satisfies $M < \theta$.
5. **Exact iteration bounds:** On our constructed 1-ULP BF16 staircase straddling $p=0.90$, Stage A leaves $[\text{lo}, \text{hi}] = [-1/64, -0.0]$, where $b(-1/64) - b(-0.0) = \text{0xBC800000} - \text{0x80000000} = \text{0x3C800000} = 1{,}015{,}021{,}568 \in (2^{29}, 2^{30})$ spans 121 biased exponent levels down to `-0.0`, taking **exactly `30` Stage-B iterations** across all `500/500` staircase rows (verified in `reproduce_tables.py`). Globally across $[-88.0, -0.0]$, $b(-88.0) - b(-0.0) = \text{0xC2B00000} - \text{0x80000000} = \text{0x42B00000} = 1{,}118{,}830{,}592 < 2^{31}$, yielding a **strict worst-case bound of at most `31` Stage-B iterations**.

**Numerical reference vs. ideal arithmetic.** All three CUDA-graphed pipelines (`Table 2A`: `PyTorch Sort`, `FlashInfer AIR` with `18.8 MB` workspace at $M=80, V=49{,}152$, and `1-CTA Bit-Lattice` with `0 MB` workspace) share identical FP32 Gumbel noise. Relative to an ideal FP64 sorting reference (`Table 2B`), all three match the full `[V]` boolean nucleus mask on **`500/500` multi-way BF16 ties** and **`500/500` 1-ULP staircases**; on `10,000` random BF16 rows, `1/10,000` rows exhibits a 1-token boundary shift relative to FP64 `cumsum` due to finite FP32 summation rounding (`10,000/10,000` coupled Top-1/2 agreement).

**Table 2A: Matched `CUDAGraph` Coupled Nucleus Sampler Benchmark (`RTX 5090D`, $T=1.0, \text{top-}p=0.90$, `FlashInfer 0.6.12`).**

| Model ($V$) | $M$ | PyTorch Sort + Coupled Gumbel ($\mu$s) | FlashInfer AIR + Coupled Gumbel ($\mu$s) [Softmax / AIR / Gumbel] | **Ours: 1-CTA Bit-Lattice ($\mu$s)** | vs. Sort | vs. AIR |
|---|---:|---:|---|---:|---:|---:|
| Ouro-1.4B (`49,152`) | `1` | `92.1` | `88.1` [`20.5`/`39.0`/`30.8`] | **`85.0`** | `1.08x` | **`1.04x`** |
| Ouro-1.4B (`49,152`) | `8` | `170.8` | `92.5` [`22.0`/`43.0`/`30.8`] | **`84.0`** | `2.03x` | **`1.10x`** |
| Ouro-1.4B (`49,152`) | `16` | `188.4` | `96.7` [`22.2`/`47.0`/`30.8`] | **`84.0`** | `2.24x` | **`1.15x`** |
| Ouro-1.4B (`49,152`) | `32` | `237.6` | `104.3` [`22.5`/`53.7`/`30.8`] | **`84.0`** | `2.83x` | **`1.24x`** |
| Ouro-1.4B (`49,152`) | `80` | `395.0` | `118.9` [`22.6`/`67.6`/`30.8`] | **`84.6`** | `4.67x` | **`1.40x`** |
| Raven-TL (`32,000`) | `1` | `78.7` | `68.5` [`14.3`/`35.4`/`20.5`] | **`57.4`** | `1.37x` | **`1.19x`** |
| Raven-TL (`32,000`) | `8` | `135.9` | `71.6` [`14.4`/`36.9`/`20.5`] | **`57.4`** | `2.37x` | **`1.25x`** |
| Raven-TL (`32,000`) | `16` | `146.1` | `73.6` [`14.3`/`39.4`/`20.5`] | **`57.3`** | `2.55x` | **`1.28x`** |
| Raven-TL (`32,000`) | `32` | `180.0` | `78.3` [`14.4`/`44.7`/`20.5`] | **`57.3`** | `3.14x` | **`1.37x`** |
| Raven-TL (`32,000`) | `80` | `303.3` | `91.0` [`16.0`/`57.2`/`22.5`] | **`57.4`** | `5.29x` | **`1.59x`** |

**Table 2B: Exact Retained Nucleus Set ($\mathcal{N}_p(z/T)$) & Coupled Token Verification Across Constructed Boundary/Tie Suites.**

| Boundary / Tie Suite ($V=49{,}152$) | Rows | Stage-B Rows (Steps) | Set == FP64 | Set == AIR | Mean Sym. Diff vs. FP64 | Top-1&2 == Sort / AIR |
|---|---:|---:|---:|---:|---:|---:|
| Constructed multi-way BF16 ties straddling $p=0.90$ | `500` | `0/500` (0) | **`500/500`** | **`500/500`** | `0.0000` | `500/500` / `500/500` |
| Constructed 1-ULP BF16 staircase (`[-1/64, -0.0]`) | `500` | `500/500` (30) | **`500/500`** | **`500/500`** | `0.0000` | `500/500` / `500/500` |
| Constructed peaked & all-uniform extremes | `500` | `0/500` (0) | **`500/500`** | **`500/500`** | `0.0000` | `500/500` / `500/500` |
| Random BF16 logits ($T=1.0, p=0.90$) | `10,000` | `0/10,000` ($\le 31$) | **`9999/10000`** | **`9998/10000`** | `0.0055` | `10000/10000` / `10000/10000` |

### 3.2 Multi-Depth Pipeline (`Track 1`), Concise Pseudocode, & Post-Head Suffix Requery

Starting from trace-verified `LoopSkim` Algorithm 1 [6] (`180/180` trials, `Appendix B`), `Algorithm 1` specifies how `continue_prism_chains` (`prism_pipeline.py`) integrates rollout reuse, low-margin shallow siblings, post-head suffix requery, and full-depth commitment.

```python
# Algorithm 1: Single cycle of continue_prism_chains (B=1, stride s, stages D = R/s, cap W_cap = 80)
# State: committed prefix y, active chains `groups` (each primary or is_secondary=True), FastRequestDrafter
def step_cycle(groups, committed):
    results_by_group = executor.forward_flattened(groups, cap=W_cap)       # 1 batched pass when live_lanes <= 80
    work = sort_descending(results_by_group, key=lambda g: g.stage)        # deepest-first: final -> q2 -> q1
    following, children, killed, terminal = [], [], set(), None

    for g, res in work:
        g.stage += s
        # 1. Online rollout cache: record high-margin (margin >= 1.5) readouts into request-local 3/2-gram tables
        for i, r in enumerate(res):
            if r.ran_readout and r.margin >= 1.5:
                drafter.record_rollout(context_tail_3gram(g, i), r.pred)   # overwrites with freshest/deepest pred

        # 2. Final stage (d = R): primary root commits; secondary d2 root saved for consumed==1 rescue
        if g.stage == D:
            if not g.is_secondary:
                terminal = (g, res)
                if not has_matching_child(g, res, work) and not has_sec_d2_rescue(g, res, work):
                    kill_all_nonterminal_branches(work, killed)            # full-depth bubble flushes stale tree
            else:
                g.final_res = res; following.append(g)
            continue
        if g.root_or_parent_in(killed): continue

        # 3. Shallow proposal stage (q1, d = d_1): truncate in-group mismatches, prune dominated d2 sibling, draft
        if g.stage - 1 == proposal_stage:
            truncate_after_first_in_group_mismatch(g, res, killed)
            if g.is_secondary and not beats_primary_length(g, following, killed): continue
            if not g.is_secondary and res[-1].proposed and live_rows < W_cap:
                children += draft_primary_and_sibling(
                    ext=g.prefix + g.tokens + [res[-1].pred], alt=res[-1].alt_pred,
                    margin=res[-1].margin, state_slot=g.lanes[-1].state)
            following.append(g)

        # 4. Intermediate check stages (q2 in C \ {d_1, R}): readout-wins replacement or sibling pruning
        elif g.stage - 1 in mid_stages:
            mm, rep_tok, rep_alt, rep_m = first_q2_disagreement(g, res)    # checks in-group & active_child_token
            if mm is not None:
                truncate_after(g, mm, killed)
                kill_conflicting_children_and_promote_matching_sibling(g, rep_tok, following, children, groups, killed)
                if not g.is_secondary and no_promoted_sibling:
                    children += draft_primary_and_sibling(g.prefix + g.tokens + [rep_tok], rep_alt, rep_m, g.lanes[mm].state)
            else:
                prune_backup_siblings_at_q2(g, res[-1], groups, killed)    # free 1-tok backups (& d2 if margin>=1.0)
            following.append(g)
        else:
            following.append(g)

    following = prune_descendants(following + children, killed)
    if terminal is not None:                                               # commit verified d=R tokens
        consumed, mismatch = commit_until_mismatch(terminal, committed)
        if mismatch and consumed == 1:                                     # rescue from co-verified d2 sibling at d=R
            rescue_from_secondary_final_if_matched(following, committed)
        root = select_matching_child_or_fresh_draft(following, committed)  # promote matching sibling or re-draft
        groups = [c for c in following if not hasattr(c, "final_res") and descends(c, root)]
    else:
        groups = [c for c in following if not hasattr(c, "final_res")]
    executor.retain_branches(lanes_of(groups))                             # reclaim KV slots of pruned branches
    return groups
```

**How rollout reuse, sibling scheduling, and post-head suffix requery operate and interact:**
1. **Online rollout reuse (`prism_drafter.py`):** Whenever any readout lane (`q1`, `q2`, or `final`) has margin $\Delta z \geq 1.5$, its local context `(t_{-2}, t_{-1}, t_0) -> pred` and `(t_{-1}, t_0) -> pred` is stored in request-local hash maps (`_rollout_3grams`, `_rollout_2grams`), so deeper stages overwrite shallower guesses on the same n-gram. When `drafter.draft(ext)` finds **no** verbatim match in prompt+committed history (`w` down to `min_verbatim_w`), `_chain_rollout` steps up to `min(4, base_k)` tokens preferring 3-grams over 2-grams while tracking `visited_states` to prevent cycles. Because rollout tokens enter at stage `0`, unverified guesses cannot corrupt committed output.
2. **Low-margin shallow siblings (`D < 12`):** Inside `draft_primary_and_sibling`, after building the primary chain $g_{\text{prim}}$ (`live_new = live_rows + |g_prim|`), if $D < 12$ and bucket slack $\text{slack} = W_{\text{bucket}}(W_{\text{new}}) - W_{\text{new}}$ is positive (allowing a $W_{\text{new}} < 8 \to 8$ bump when $\Delta z^{(d_1)} < 1.2$), at most one `is_secondary=True` sibling sharing `parent_branch` is admitted: **Priority 1** is a 1-lane `[alt_token]` backup when $\Delta z^{(d_1)} < 1.2$; **Priority 2** is a distinct secondary suffix continuation `[token] + d2` truncated to $\text{slack}$ lanes (`d2[0] != d1[0]`). Secondary chains never spawn children while `is_secondary=True`. If `q2` overrides the primary's child token to `alt_token`, the already-advanced backup flips `is_secondary <- False` at **0-cycle cost**; if `q2` confirms the primary, 1-lane backups (and `d2` siblings once $\Delta z \geq 1.0$) are pruned immediately at `mid_stages[0]` and their KV slots are freed by `retain_branches`. If a multi-lane `d2` sibling reaches $d=R$ alongside $g_{\text{prim}}$ and $g_{\text{prim}}$ mismatches at `lanes[1]` (`consumed == 1`) onto `d2[0]`, `sec_final` commits its verified `s_off >= 1` tokens in the same cycle.
3. **Actual fallback policy of Post-Head Suffix Requery vs. LoopFill [7] and Strict Two-Token Bridging:** In **LoopFill** [7] (and already in `LoopSkim`, `Track 1`, and our `no +2 req.` 1-step controls), `drafter.draft(ext)` immediately queries $x_{\leq t} \Vert [\hat{y}_{t+1}^{(d_1)}]$ (`+1` requery); if $w \geq 2$, `Track 1` copies up to $G=8$ tokens with **zero** head calls. Only when $w \leq 1$ does a 1-step head predict $\hat{y}_{t+2}$ from `parent_state_slot`. Calling `drafter.draft(ext + [y_hat_2])` under our default `min_verbatim_w = 1, allow_rollout = True` (**`Post-Head Requery`**) searches $w \in \{4, 3, 2, 1\}$ verbatim and then rollout tables. Consequently, a nonempty continuation (`Table 6B`) can arise from **three distinct sources**: (a) a **$w \geq 2$ verbatim anchor** matching $[\dots, \hat{y}_{t+1}^{(d_1)}, \hat{y}_{t+2}]$ in context, (b) a **$w = 1$ verbatim match on $\hat{y}_{t+2}$ alone** (e.g., on prompt `[10, 20, 30, 40]` with `ext = [99]` and $\hat{y}_{t+2} = 20$, `[99]` has $w=0$ while `[99, 20]` returns `[30, 40, ...]` at $w=1$ even though `[99, 20]` never occurred), or (c) **stored rollout n-grams**. To isolate genuine multi-token disambiguation from $w=1$/rollout fallback, we also evaluate **Strict $w \geq 2$** (`min_w_override = 2, allow_rollout = False`), which accepts **only** verbatim matches of order $w \geq 2$ (`0` $w=1$ hits, `0` rollouts). **`Bridge-Miss 8k MLP`** runs `draft_step1` + permissive post-head requery first and executes MLP steps `2..5` (`draft_rem`) **if and only if** the requery returns empty.

### 3.3 Exact 128-Prompt Calibration, Scope Boundary, & Live Stochastic Audit (`Track 2`)

**Scope boundary vs. external student models.** **Paper 4 v3** (§4) [14] distills external `SmolLM2-135M` on Ouro (`8,447` problems, ~2 min: $1.039\times$–$1.047\times$ `GSM8K`, $0.958\times$ `HumanEval`) and verifies tokenizer compatibility of **`JackFram/llama-160m`** for Raven. Tokenizer-compatible external students therefore exist for both models; our restriction to **target-state heads** sharing the frozen target embeddings/`lm_head` is an explicit scope choice (`0` external models, `0` student KV cache, `128` prompts).

**Exact calibration (`train_and_audit_heads_v3.py`, `112` train + `16` val = `128` `dev32` prompts, `0` aux prompts):** Fast-exact `LoopSkim` generates `25,665` Ouro (`61.76s`) and `26,546` Raven (`73.05s`) tokens; one pass extracts $h_t^{(d_1)}$ (`d_1=1` Ouro, `d_1=2` Raven) paired with $u_{t+k}^{(R)}$ (`21,263` Ouro, `22,232` Raven transitions; top-`8,192` shortlist from the `112` train sequences):
- **`PrismHead` (`prism1.pt`):** Rank-`384` SwiGLU cell (`3.94M` step-1 params; `600` AdamW steps, `bs=256, lr=2.5e-3`, $\mathcal{L}_1 + 0.7\mathcal{L}_2$ with top-32 $T=1$ KL + $2.0(1-\cos)$). Served at `1` step either over full `V` (`174`/`146` $\mu\text{s}$) or—slicing the **identical `prism1.pt` weights** onto the `8,192` shortlist—as **`PrismHead-8k`** (`~70` $\mu\text{s}$), gated by $\Delta\hat{z} \geq \tau_1$ (`1.2` Ouro, `1.8` Raven).
- **`5-Step 8k MLP` (`paper4_mlp.pt`, `112p` adaptation of [14]) & `4-Step Parallel 8k` (`loopskim_par.pt`, `112p` `d=512` window-32 adaptation inspired by [6, 10]):** `25.17M` 2-layer SiLU MLP (`5` steps) and `6.58M` 1-layer causal Transformer (`4` steps), trained `1,500` AdamW steps (`bs=256, lr=1e-3`, $\sum_{s=0}^{K-1} 0.9^s(\text{CE}_{\text{8k}} + (1-\cos))$), plus a `766`-problem Ouro scaling control (`128` `dev32` + `638` non-eval prompts).

**Table 3: Complete Ready-to-Serve Calibration Accounting (`128` `dev32` Prompts) & Offline `sel32` Diagnostic.**

| Model & Calibrated Head (`112` train + `16` val = `128` `dev32` prompts) | Startup (s) | Gen (s) | Extract (s) | AdamW + Capture (s) | **Ready-to-Serve (s)** | Graph ($\mu$s) | `sel32` Step-1 Acc. (Gated Prec./Cov.) |
|---|---:|---:|---:|---:|---:|---:|---|
| **Ouro-1.4B — PrismHead (`prism1.pt`)** | `8.79` | `61.76` | `8.51` | `6.56`+`0.10` | **`85.73s`** | `174.8` full-V (`~70` `8k`) | `53.5%` (`68.3%`/`65.0%` at $\tau_1=1.2$) |
| Ouro-1.4B — 5-Step 8k MLP (`paper4_mlp.pt`) | `8.79` | `61.76` | `8.51` | `36.87`+`0.25` | `116.19s` | `324.8` (`5` tok) | `51.8%` (`7.66%` `8k` OOV) |
| Ouro-1.4B — 4-Step Parallel 8k (`loopskim_par.pt`) | `8.79` | `61.76` | `8.51` | `37.56`+`0.05` | `116.68s` | `181.6` (`4` tok) | `46.2%` (`7.66%` `8k` OOV) |
| **Raven-TL — PrismHead (`prism1.pt`)** | `9.79` | `73.05` | `26.88` | `7.65`+`0.11` | **`117.46s`** | `136.8` full-V (`~70` `8k`) | `49.0%` (`72.3%`/`48.6%` at $\tau_1=1.8$) |
| Raven-TL — 5-Step 8k MLP (`paper4_mlp.pt`) | `9.79` | `73.05` | `26.88` | `43.82`+`0.26` | `153.80s` | `322.1` (`5` tok) | `47.4%` (`6.90%` `8k` OOV) |
| Raven-TL — 4-Step Parallel 8k (`loopskim_par.pt`) | `9.79` | `73.05` | `26.88` | `45.04`+`0.09` | `154.85s` | `169.2` (`4` tok) | `42.2%` (`6.90%` `8k` OOV) |

**Table 4: Deployed-BF16 Checkpoint Audit on Actual Live Stochastic Invocations (`sel32`, Recomputed From `live_head_audit_v6.json`).**

| Model & Live `sel32` Regime (`HE+, MBPP+, GSM8K`) | Live Calls (`on_prefix`) | Call-Site Depths | Uncoupled ($\tau_1$) Prec./Cov. ($\mathbb{E}[\text{acc}_1]$) | Single-Gate ($\tau_G=1.0$) Prec./Cov. (Diffuse %) | **Dual-Gate ($\tau_G=1.0, \hat{p}_{\text{win}}\ge 0.25$) Prec./Cov. ($\mathbb{E}[\text{acc}_1]$, Diffuse %)** | `eq_ar` |
|---|---:|---|---|---|---|---:|
| Ouro-1.4B ($s=1, d_1=1$) $T=0.6, p=0.95$ | `3,325` (`69.7%`) | $d=1$:`2811`, $d=2$:`341`, $d=3$:`121`, $d=4$:`52` | `64.3%`/`61.8%` (`0.397`) | `54.0%`/`80.2%` (`7.0%`) | **`56.6%`/`75.4%` (`0.427`, `0.0%`)** | `96/96` |
| Ouro-1.4B ($s=1, d_1=1$) $T=1.0, p=0.90$ | `4,791` (`61.3%`) | $d=1$:`3818`, $d=2$:`676`, $d=3$:`205`, $d=4$:`92` | `60.3%`/`59.5%` (`0.359`) | `52.9%`/`69.1%` (`20.2%`) | **`60.5%`/`57.6%` (`0.349`, `0.0%`)** | `96/96` |
| Raven-TL ($s=4, d_1=4$) $T=0.6, p=0.95$ | `4,202` (`75.4%`) | $d=4$:`3958`, $d=8$:`158`, $d=16$:`61`, $d=32$:`25` | `69.4%`/`42.3%` (`0.294`) | `52.1%`/`74.8%` (`9.6%`) | **`56.0%`/`67.9%` (`0.380`, `0.0%`)** | `96/96` |
| Raven-TL ($s=4, d_1=4$) $T=1.0, p=0.90$ | `7,659` (`78.2%`) | $d=4$:`7179`, $d=8$:`307`, $d=16$:`114`, $d=32$:`59` | `54.0%`/`36.5%` (`0.197`) | `43.5%`/`58.2%` (`29.6%`) | **`54.8%`/`41.5%` (`0.227`, `0.0%`)** | `96/96` |

Auditing deployed BF16 weights at live `q1`/`q2`/`final` call sites (`Table 4`, Raven $s=4, d_1=4$) confirms that our **Dual Epistemic-Aleatoric Gate ($\tau_G=1.0, \hat{p}_{\text{win}} \geq 0.25$)** eliminates the `7.0%–29.6%` diffuse false triggers of single-gate Gumbel (`0.0%` diffuse), explaining why Raven's `~2.6 ms` cycles amortize `59` $\mu\text{s}$ coupled selection whereas Ouro's `~1.8 ms` cycles slightly favor `28` $\mu\text{s}$ uncoupled selection (`Tables 7A–7B`).

### 3.4 Exactness-Preserving Request Setup on Coda Models: `O(1) SlotBegin` & `Prompt-CoW`

On Raven ($R=32$), two request-setup costs depress end-to-end `client tok/s` relative to `decode tok/s`: (i) `DecodeSlotPool.begin()` materializes `list(range(1, 65537))` in Python on every request (`decode_slots.py`), and (ii) `RecurrentRequest.prefill()` runs **5 separate eager Coda prefill passes** across `post-{1, 3, 7, 15, 31}` (`request.py`). Crucially, **$d=R$ bitwise exactness (`eq_ar = 100%`) depends exclusively on `post-31` reading exact `d=32` prompt+committed KVs**; intermediate Coda timelines (`post-{1,3,7,15}`) only propose or screen speculative lanes. We test three single-variable steps (`Table 8`):
1. **`O(1) SlotBegin`:** Replaces per-request list allocation with an immutable preallocated tuple `_base_sequence = tuple(range(1, capacity + 1))` (materializing a short slice copy only if ring compaction occurs).
2. **`Prompt-CoW` Coda ($5 \to 1$ Coda prefill passes):** Executes eager prompt Coda prefill **only** at final depth `post-31`, initializing root cursors `post-{1,3,7,15}` via `create_aliased_prefilled` (`manager.py`), which copies `post-31`'s prompt page-table entries (`req_to_token[:, :P]`) without duplicating KV memory or running 4 extra Coda prefills, while decode allocates independent owned KV slots per depth (`90.1%–96.0%` top-1 agreement with separate prompt KVs).
3. **`Full-CoW` Coda (prefill + decode prefix aliasing):** Also overwrites committed prefix page-table entries `req_to_token[:, lo:hi]` of active `post-{1,3,7,15}` cursors from `post-31` after each commit, testing whether decode-time KV sharing helps or hurts via speculative flip inflation.

---

## 4. Experimental Setup, Primary Two-Repeat Aggregation, and Exposure Disclosure

- **Hardware & Runtime:** Single NVIDIA RTX 5090D (`32` GB VRAM, `10` CPU threads, `OMP_NUM_THREADS=8`, $B=1$), Python `3.11`, PyTorch `2.11.0+cu130`, Triton `3.6.0`, SGLang `0.5.14`, FlashInfer `0.6.12`, persistent `Req`/dummy-cursor pooling + `gc.freeze()` (`SYS-OPT`).
- **Pinned Revisions & KV Capacities:** `Ouro-1.4B` [1] rev `574fa66c...` (`23,461` KV slots matched across all arms); `Recurrent-TinyLlama-3T-train-recurrence-32` [2] rev `2579b6a0...` (`65,536` KV slots, position-keyed `z_0`). Grading runs in isolated `score-python` (`EvalPlus 0.3.1`, `math-verify 0.9.0`).
- **Primary Two-Repeat Aggregation & Conditional Intervals:** Every greedy confirmation arm (`Tables 5A, 5B, 8, A1`: `confirm_t0` + `confirm_t0_rep2`) and every live sampler arm (`Table 2C`: `confirm_sampler_*` forward + `*_rep2` reversed) is measured over **two complete repeats per problem**. Primary per-problem decode and end-to-end times are averaged across both repeats ($\bar{t}_i = 0.5(t_{i,1} + t_{i,2})$) before computing pooled throughput ($\sum_i \text{tok}_i / \sum_i \bar{t}_i$, with individual `(R1/R2)` rates shown alongside) and `4,000`-resample paired-bootstrap `95%` confidence intervals (`seed=42`) on the median per-problem speedup ratio. All bootstrap intervals reflect problem-resampling variability **conditional on the measured runs**, not cross-day hardware variance.
- **Community Exposure vs. Internal 3-Way Protocol:** Prior rStation studies (**Paper 3 v4** [13], **Paper 5 v3** [15]) already evaluated `HumanEval+`, `MBPP+`, `GSM8K`, and `MATH-500`, so none is historically unexposed across the community. Internally, deterministic index partitions (`prepare_splits.py` + `checkpoints_and_splits_sha256.json`) separate `dev32` (calibration), `sel32` (ablation), and confirmation (`confirm100` HE+, `holdout128` MBPP+, `confirm128` GSM8K, `holdout64` MATH-500; `confirm64` for $T>0$). Every strong `sel32` control—including `Strict` $w \geq 2$ and permissive post-head requery, `5-Step 8k MLP` ($w \leq 1$ and $w \leq 2$), `4-Step Parallel 8k`, `1-Step 8k MLP + Requery`, `Bridge-Miss 8k MLP`, `766p` scaled MLP, full-$V$ `PrismHead`, and `O(1) SlotBegin` / `Prompt-CoW` / `Full-CoW`—is evaluated over two repeats (`Table 5A` shows the core 11 arms; `Table A1` reports all confirmed arms).

---

## 5. Results

### 5.1 Disjoint Two-Repeat Confirmation — Greedy Decoding ($T = 0, W \leq 80$)

![Figure 2: Two-repeat disjoint confirmation pooled decode throughput (tok/s) across all eight (model, benchmark) cells under wide-frontier (W at most 80) bitwise-exact execution (100% eq_ar across all speculative arms and repeats), comparing Track 1, standalone 5-Step/4-Step controls, Strict two-token bridging vs. permissive Post-Head Requery, Bridge-Miss MLP, and Raven Prompt-CoW.](supplement/figures/figure-2.png)

**Table 5A: Disjoint Two-Repeat Confirmation — Core Baselines & Strong Controls ($T = 0, W \leq 80$; Full 17-Arm Table in `Appendix A, Table A1`).**

| Model | Task | Method | 2-Rep Decode tok/s (R1/R2) | 2-Rep Client tok/s | 2-Rep Med. vs. LS `4..2` [95% CI] | 2-Rep Med. vs. LS `4..1` [95% CI] | Cycles | Acc. (%) | `eq_ar` (R1==R2) |
|---|---|---|---:|---:|---|---|---:|---:|---:|
| Ouro-1.4B | HE+ | Autoregressive ($W=1$) | `105.16` (`104.9`/`105.4`) | `102.77` | `0.1375x` [0.130, 0.148] | `0.1337x` [0.128, 0.142] | `0` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | LoopSkim (`4..2`, $G=8$) | `755.28` (`755.2`/`755.3`) | `643.65` | `1.0000x` [1.000, 1.000] | `0.9827x` [0.976, 0.993] | `8,452` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | LoopSkim (`4..1`, $G=8$) | `772.35` (`770.7`/`774.0`) | `653.98` | `1.0176x` [1.007, 1.024] | `1.0000x` [1.000, 1.000] | `7,968` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | PrismLoop (`Track 1`) | `785.11` (`788.5`/`781.7`) | `664.40` | `1.0298x` [1.024, 1.043] | `1.0133x` [1.011, 1.020] | `7,834` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | 5-Step 8k MLP ($w \le 1$, 112p) | `876.01` (`880.3`/`871.8`) | `729.76` | `1.1332x` [1.093, 1.168] | `1.0914x` [1.079, 1.142] | `6,505` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `874.21` (`877.2`/`871.3`) | `727.90` | `1.1523x` [1.128, 1.163] | `1.1217x` [1.099, 1.141] | `6,841` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `874.39` (`872.1`/`876.7`) | `727.21` | `1.1365x` [1.107, 1.175] | `1.1021x` [1.085, 1.127] | `6,619` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | 4-Step Parallel 8k ($w \le 1$, 112p) | `868.51` (`868.6`/`868.4`) | `725.81` | `1.1191x` [1.083, 1.154] | `1.0982x` [1.075, 1.123] | `6,862` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | PrismHead-8k + Strict $w\ge 2$ (112p) | `849.12` (`849.1`/`849.1`) | `711.74` | `1.1167x` [1.092, 1.141] | `1.0923x` [1.072, 1.112] | `7,055` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | PrismHead-8k + Requery ($w \le 1$, 112p) | `867.21` (`868.7`/`865.8`) | `721.72` | `1.1363x` [1.113, 1.168] | `1.1122x` [1.086, 1.135] | `6,919` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | PrismHead + Requery (full-V, 112p) | `850.43` (`852.2`/`848.6`) | `710.10` | `1.1156x` [1.093, 1.143] | `1.0923x` [1.070, 1.109] | `6,919` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | MBPP+ | Autoregressive ($W=1$) | `106.93` (`106.8`/`107.1`) | `99.13` | `0.3203x` [0.312, 0.329] | `0.3004x` [0.292, 0.311] | `0` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | LoopSkim (`4..2`, $G=8$) | `347.74` (`347.6`/`347.9`) | `273.38` | `1.0000x` [1.000, 1.000] | `0.9454x` [0.935, 0.955] | `7,877` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | LoopSkim (`4..1`, $G=8$) | `373.04` (`372.3`/`373.8`) | `289.97` | `1.0577x` [1.047, 1.069] | `1.0000x` [1.000, 1.000] | `7,102` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | PrismLoop (`Track 1`) | `381.57` (`380.8`/`382.4`) | `293.92` | `1.0843x` [1.070, 1.091] | `1.0196x` [1.017, 1.026] | `6,896` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | 5-Step 8k MLP ($w \le 1$, 112p) | `446.93` (`447.4`/`446.5`) | `333.68` | `1.3124x` [1.277, 1.349] | `1.2610x` [1.220, 1.292] | `5,328` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `435.88` (`436.1`/`435.7`) | `326.87` | `1.2782x` [1.257, 1.307] | `1.2083x` [1.179, 1.229] | `5,794` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `446.77` (`446.1`/`447.4`) | `334.21` | `1.3116x` [1.281, 1.367] | `1.2395x` [1.207, 1.274] | `5,459` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | 4-Step Parallel 8k ($w \le 1$, 112p) | `444.23` (`444.2`/`444.3`) | `333.22` | `1.2936x` [1.262, 1.322] | `1.2265x` [1.198, 1.263] | `5,677` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | PrismHead-8k + Strict $w\ge 2$ (112p) | `427.22` (`428.0`/`426.5`) | `322.21` | `1.2489x` [1.224, 1.261] | `1.1738x` [1.155, 1.188] | `5,967` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | PrismHead-8k + Requery ($w \le 1$, 112p) | `439.28` (`439.3`/`439.3`) | `328.47` | `1.2839x` [1.256, 1.302] | `1.1965x` [1.185, 1.229] | `5,820` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | PrismHead + Requery (full-V, 112p) | `427.31` (`426.8`/`427.9`) | `321.62` | `1.2428x` [1.219, 1.268] | `1.1657x` [1.151, 1.184] | `5,830` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | Autoregressive ($W=1$) | `104.64` (`104.6`/`104.7`) | `100.07` | `0.2581x` [0.246, 0.264] | `0.2406x` [0.233, 0.248] | `0` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | LoopSkim (`4..2`, $G=8$) | `412.14` (`412.5`/`411.8`) | `346.94` | `1.0000x` [1.000, 1.000] | `0.9390x` [0.931, 0.946] | `10,292` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | LoopSkim (`4..1`, $G=8$) | `440.28` (`440.2`/`440.4`) | `367.07` | `1.0649x` [1.057, 1.075] | `1.0000x` [1.000, 1.000] | `9,300` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | PrismLoop (`Track 1`) | `447.20` (`447.6`/`446.8`) | `373.55` | `1.0828x` [1.072, 1.093] | `1.0132x` [1.007, 1.021] | `9,135` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | 5-Step 8k MLP ($w \le 1$, 112p) | `450.97` (`449.7`/`452.2`) | `374.25` | `1.0957x` [1.079, 1.109] | `1.0201x` [1.010, 1.044] | `8,726` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `461.45` (`461.9`/`461.0`) | `382.46` | `1.1250x` [1.114, 1.136] | `1.0434x` [1.035, 1.058] | `8,788` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `458.89` (`458.4`/`459.4`) | `380.93` | `1.1132x` [1.106, 1.127] | `1.0399x` [1.029, 1.048] | `8,780` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | 4-Step Parallel 8k ($w \le 1$, 112p) | `456.52` (`457.4`/`455.7`) | `378.36` | `1.1126x` [1.103, 1.123] | `1.0330x` [1.021, 1.049] | `8,922` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | PrismHead-8k + Strict $w\ge 2$ (112p) | `456.42` (`457.1`/`455.8`) | `377.48` | `1.1136x` [1.098, 1.122] | `1.0359x` [1.025, 1.048] | `8,784` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | PrismHead-8k + Requery ($w \le 1$, 112p) | `465.63` (`465.6`/`465.6`) | `384.38` | `1.1333x` [1.120, 1.143] | `1.0555x` [1.047, 1.067] | `8,693` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | PrismHead + Requery (full-V, 112p) | `459.31` (`459.3`/`459.3`) | `379.23` | `1.1145x` [1.105, 1.124] | `1.0383x` [1.034, 1.050] | `8,704` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | MATH-500 | Autoregressive ($W=1$) | `99.80` (`99.7`/`99.9`) | `99.19` | `0.2384x` [0.222, 0.254] | `0.2268x` [0.213, 0.242] | `0` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | LoopSkim (`4..2`, $G=8$) | `445.51` (`442.4`/`448.7`) | `432.71` | `1.0000x` [1.000, 1.000] | `0.9588x` [0.951, 0.967] | `36,179` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | LoopSkim (`4..1`, $G=8$) | `460.53` (`457.6`/`463.5`) | `446.92` | `1.0430x` [1.034, 1.051] | `1.0000x` [1.000, 1.000] | `33,551` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | PrismLoop (`Track 1`) | `474.03` (`470.4`/`477.7`) | `460.02` | `1.0715x` [1.067, 1.076] | `1.0246x` [1.019, 1.031] | `32,622` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | 5-Step 8k MLP ($w \le 1$, 112p) | `502.29` (`503.8`/`500.8`) | `486.54` | `1.1487x` [1.130, 1.164] | `1.1045x` [1.089, 1.113] | `28,676` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `506.31` (`506.4`/`506.2`) | `490.36` | `1.1576x` [1.143, 1.174] | `1.1157x` [1.104, 1.128] | `29,402` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `503.27` (`504.7`/`501.9`) | `487.21` | `1.1463x` [1.135, 1.161] | `1.1071x` [1.089, 1.117] | `29,037` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | 4-Step Parallel 8k ($w \le 1$, 112p) | `492.98` (`493.7`/`492.3`) | `477.98` | `1.1193x` [1.107, 1.139] | `1.0804x` [1.063, 1.091] | `30,442` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | PrismHead-8k + Strict $w\ge 2$ (112p) | `500.13` (`500.7`/`499.6`) | `484.54` | `1.1463x` [1.129, 1.160] | `1.0951x` [1.088, 1.108] | `29,922` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | PrismHead-8k + Requery ($w \le 1$, 112p) | `507.40` (`506.2`/`508.6`) | `491.06` | `1.1499x` [1.142, 1.181] | `1.1139x` [1.108, 1.127] | `29,559` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | PrismHead + Requery (full-V, 112p) | `501.66` (`499.1`/`504.3`) | `485.63` | `1.1461x` [1.129, 1.159] | `1.1043x` [1.098, 1.111] | `29,554` | 70.31 | `64/64` (`64/64`) |
| Raven-TL | HE+ | Autoregressive ($W=1$) | `48.70` (`48.8`/`48.7`) | `47.85` | `0.0794x` [0.077, 0.085] | `0.0777x` [0.074, 0.084] | `0` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | LoopSkim (`4..2`, $G=8$) | `636.54` (`634.9`/`638.1`) | `460.51` | `1.0000x` [1.000, 1.000] | `0.9825x` [0.975, 0.988] | `15,822` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | LoopSkim (`4..1`, $G=8$) | `651.96` (`653.4`/`650.5`) | `466.41` | `1.0178x` [1.012, 1.026] | `1.0000x` [1.000, 1.000] | `15,063` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismLoop (`Track 1`) | `658.84` (`657.0`/`660.6`) | `468.84` | `1.0255x` [1.010, 1.040] | `1.0011x` [0.998, 1.007] | `14,942` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | 5-Step 8k MLP ($w \le 1$, 112p) | `651.44` (`654.0`/`649.0`) | `467.65` | `0.9995x` [0.982, 1.022] | `0.9843x` [0.974, 1.005] | `13,947` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `655.73` (`656.8`/`654.7`) | `470.32` | `1.0127x` [1.003, 1.042] | `0.9954x` [0.988, 1.010] | `14,233` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `671.07` (`670.5`/`671.7`) | `479.83` | `1.0342x` [1.015, 1.061] | `1.0171x` [1.004, 1.028] | `14,083` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | 4-Step Parallel 8k ($w \le 1$, 112p) | `665.29` (`663.8`/`666.8`) | `475.09` | `1.0267x` [1.018, 1.043] | `1.0145x` [1.006, 1.035] | `14,453` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismHead-8k + Strict $w\ge 2$ (112p) | `656.56` (`656.1`/`657.0`) | `470.76` | `1.0218x` [1.009, 1.038] | `1.0021x` [0.996, 1.011] | `14,479` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismHead-8k + Requery ($w \le 1$, 112p) | `659.81` (`660.8`/`658.9`) | `471.51` | `1.0314x` [1.010, 1.041] | `1.0076x` [0.996, 1.021] | `14,296` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismHead + Requery (full-V, 112p) | `659.03` (`659.4`/`658.7`) | `471.12` | `1.0239x` [1.010, 1.042] | `1.0087x` [0.990, 1.021] | `14,298` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | MBPP+ | Autoregressive ($W=1$) | `48.62` (`48.6`/`48.6`) | `46.99` | `0.1605x` [0.147, 0.175] | `0.1544x` [0.137, 0.172] | `0` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | LoopSkim (`4..2`, $G=8$) | `562.55` (`563.5`/`561.6`) | `337.98` | `1.0000x` [1.000, 1.000] | `0.9722x` [0.968, 0.977] | `12,027` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | LoopSkim (`4..1`, $G=8$) | `583.92` (`583.8`/`584.0`) | `346.46` | `1.0286x` [1.023, 1.034] | `1.0000x` [1.000, 1.000] | `11,248` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismLoop (`Track 1`) | `585.53` (`584.0`/`587.1`) | `343.89` | `1.0236x` [1.018, 1.035] | `0.9961x` [0.993, 1.002] | `11,158` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | 5-Step 8k MLP ($w \le 1$, 112p) | `587.11` (`588.0`/`586.2`) | `352.68` | `1.0645x` [1.045, 1.079] | `1.0302x` [1.001, 1.050] | `9,943` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `590.71` (`591.0`/`590.5`) | `353.91` | `1.0703x` [1.062, 1.085] | `1.0410x` [1.024, 1.056] | `10,270` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `607.65` (`605.7`/`609.6`) | `361.48` | `1.0993x` [1.078, 1.119] | `1.0682x` [1.046, 1.082] | `9,999` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | 4-Step Parallel 8k ($w \le 1$, 112p) | `601.14` (`601.0`/`601.2`) | `359.64` | `1.0821x` [1.061, 1.102] | `1.0471x` [1.029, 1.060] | `10,355` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismHead-8k + Strict $w\ge 2$ (112p) | `589.44` (`588.2`/`590.6`) | `353.87` | `1.0708x` [1.050, 1.078] | `1.0298x` [1.018, 1.039] | `10,528` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismHead-8k + Requery ($w \le 1$, 112p) | `593.97` (`595.8`/`592.1`) | `354.90` | `1.0731x` [1.058, 1.090] | `1.0350x` [1.022, 1.049] | `10,392` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismHead + Requery (full-V, 112p) | `589.78` (`588.4`/`591.2`) | `346.38` | `1.0659x` [1.044, 1.083] | `1.0265x` [1.014, 1.040] | `10,395` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | Autoregressive ($W=1$) | `48.80` (`48.9`/`48.8`) | `46.63` | `0.1273x` [0.123, 0.134] | `0.1207x` [0.115, 0.127] | `0` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | LoopSkim (`4..2`, $G=8$) | `403.46` (`404.6`/`402.3`) | `247.86` | `1.0000x` [1.000, 1.000] | `0.9479x` [0.940, 0.953] | `12,847` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | LoopSkim (`4..1`, $G=8$) | `425.61` (`425.6`/`425.6`) | `255.95` | `1.0550x` [1.049, 1.064] | `1.0000x` [1.000, 1.000] | `11,816` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismLoop (`Track 1`) | `431.93` (`429.9`/`433.9`) | `258.13` | `1.0703x` [1.060, 1.080] | `1.0138x` [1.009, 1.018] | `11,726` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | 5-Step 8k MLP ($w \le 1$, 112p) | `404.16` (`404.9`/`403.4`) | `252.23` | `1.0060x` [0.991, 1.012] | `0.9498x` [0.939, 0.957] | `11,518` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `418.02` (`418.4`/`417.6`) | `257.59` | `1.0345x` [1.031, 1.042] | `0.9793x` [0.972, 0.987] | `11,529` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `422.58` (`422.3`/`422.9`) | `258.42` | `1.0420x` [1.037, 1.048] | `0.9895x` [0.979, 0.997] | `11,486` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | 4-Step Parallel 8k ($w \le 1$, 112p) | `416.73` (`415.6`/`417.8`) | `257.95` | `1.0366x` [1.028, 1.044] | `0.9776x` [0.969, 0.985] | `11,883` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismHead-8k + Strict $w\ge 2$ (112p) | `424.19` (`424.1`/`424.3`) | `259.95` | `1.0501x` [1.043, 1.056] | `0.9970x` [0.991, 1.002] | `11,504` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismHead-8k + Requery ($w \le 1$, 112p) | `424.15` (`425.1`/`423.2`) | `258.22` | `1.0505x` [1.043, 1.058] | `0.9965x` [0.992, 1.001] | `11,464` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismHead + Requery (full-V, 112p) | `422.47` (`421.4`/`423.5`) | `254.48` | `1.0482x` [1.040, 1.054] | `0.9929x` [0.989, 0.996] | `11,464` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | MATH-500 | Autoregressive ($W=1$) | `48.55` (`48.6`/`48.5`) | `48.15` | `0.0982x` [0.091, 0.102] | `0.0912x` [0.084, 0.094] | `0` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | LoopSkim (`4..2`, $G=8$) | `572.94` (`577.8`/`568.2`) | `491.92` | `1.0000x` [1.000, 1.000] | `0.9452x` [0.932, 0.958] | `26,129` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | LoopSkim (`4..1`, $G=8$) | `602.28` (`608.5`/`596.2`) | `513.89` | `1.0580x` [1.044, 1.073] | `1.0000x` [1.000, 1.000] | `24,050` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismLoop (`Track 1`) | `609.09` (`615.6`/`602.7`) | `517.40` | `1.0707x` [1.061, 1.083] | `1.0091x` [1.004, 1.014] | `23,750` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | 5-Step 8k MLP ($w \le 1$, 112p) | `613.07` (`617.1`/`609.1`) | `527.29` | `1.0750x` [1.062, 1.090] | `1.0172x` [1.003, 1.030] | `21,482` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `621.03` (`623.1`/`619.0`) | `532.65` | `1.1057x` [1.088, 1.114] | `1.0415x` [1.025, 1.047] | `21,928` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `628.09` (`637.3`/`619.2`) | `535.39` | `1.1116x` [1.096, 1.122] | `1.0436x` [1.034, 1.058] | `21,560` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | 4-Step Parallel 8k ($w \le 1$, 112p) | `613.42` (`621.1`/`605.9`) | `524.80` | `1.0715x` [1.062, 1.092] | `1.0175x` [1.009, 1.028] | `22,685` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismHead-8k + Strict $w\ge 2$ (112p) | `621.43` (`621.7`/`621.1`) | `532.31` | `1.1059x` [1.089, 1.120] | `1.0348x` [1.026, 1.050] | `22,369` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismHead-8k + Requery ($w \le 1$, 112p) | `626.45` (`626.8`/`626.1`) | `536.45` | `1.1161x` [1.101, 1.135] | `1.0489x` [1.041, 1.061] | `22,054` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismHead + Requery (full-V, 112p) | `622.85` (`622.6`/`623.1`) | `528.58` | `1.1038x` [1.087, 1.128] | `1.0448x` [1.032, 1.051] | `22,058` | 28.12 | `64/64` (`64/64`) |

**Table 5B: Direct Two-Repeat Comparison Against Strongest Confirmed Standalone `112p` Multi-Step Control (Per-Problem Repeat-Averaged Ratios & Conditional `[95% CI]`).**

| Model | Task | Best `112p` Standalone Control (2-Rep tok/s) | `PrismHead-8k` + Requery 2-Rep & Med. [95% CI] | `PrismHead-8k` + Strict $w\geq 2$ 2-Rep & Med. [95% CI] | `PrismHead` + Requery (Full-V) 2-Rep & Med. [95% CI] | `Bridge-Miss 8k MLP` 2-Rep & Med. [95% CI] |
|---|---|---|---|---|---|---|
| Ouro-1.4B | HE+ | 5-Step MLP ($w\le 1$) (`876.01`) | `867.21` (`1.0036x` [0.98753, 1.01513]) | `849.12` (`0.9862x` [0.97117, 0.99518]) | `850.43` (`0.9835x` [0.97029, 0.99923]) | `874.39` (`0.9941x` [0.98634, 1.00241]) |
| Ouro-1.4B | MBPP+ | 5-Step MLP ($w\le 1$) (`446.93`) | `439.28` (`0.9675x` [0.94606, 0.99156]) | `427.22` (`0.9414x` [0.92024, 0.96565]) | `427.31` (`0.9348x` [0.92135, 0.95938]) | `446.77` (`1.0046x` [0.99404, 1.01694]) |
| Ouro-1.4B | GSM8K | 4-Step Par ($w\le 1$) (`456.52`) | `465.63` (`1.0216x` [1.01610, 1.02781]) | `456.42` (`1.0005x` [0.99540, 1.01007]) | `459.31` (`1.0066x` [0.99899, 1.01300]) | `458.89` (`1.0040x` [0.99653, 1.01335]) |
| Ouro-1.4B | MATH-500 | 5-Step MLP ($w\le 1$) (`502.29`) | `507.40` (`1.0105x` [0.99995, 1.01476]) | `500.13` (`0.9909x` [0.98218, 1.00198]) | `501.66` (`0.9962x` [0.98694, 1.00571]) | `503.27` (`1.0044x` [0.99667, 1.00588]) |
| Raven-TL | HE+ | 4-Step Par ($w\le 1$) (`665.29`) | `659.81` (`0.9868x` [0.97938, 0.99191]) | `656.56` (`0.9856x` [0.97907, 0.99056]) | `659.03` (`0.9858x` [0.98089, 0.99220]) | `671.07` (`1.0048x` [0.99959, 1.00844]) |
| Raven-TL | MBPP+ | 4-Step Par ($w\le 1$) (`601.14`) | `593.97` (`0.9897x` [0.97953, 0.99762]) | `589.44` (`0.9810x` [0.97031, 0.98929]) | `589.78` (`0.9822x` [0.97329, 0.99088]) | `607.65` (`1.0174x` [1.00996, 1.02290]) |
| Raven-TL | GSM8K | 4-Step Par ($w\le 1$) (`416.73`) | `424.15` (`1.0184x` [1.00727, 1.02355]) | `424.19` (`1.0161x` [1.00890, 1.02142]) | `422.47` (`1.0135x` [1.00365, 1.02121]) | `422.58` (`1.0081x` [1.00422, 1.01598]) |
| Raven-TL | MATH-500 | 4-Step Par ($w\le 1$) (`613.42`) | `626.45` (`1.0228x` [1.01566, 1.03328]) | `621.43` (`1.0136x` [1.00363, 1.02338]) | `622.85` (`1.0183x` [1.00417, 1.02762]) | `628.09` (`1.0241x` [1.01611, 1.03370]) |

Across all `24,360` paired `AR` confirmation comparisons (spanning both repeats) and `13,020` Repeat-1 vs. Repeat-2 checks, **every speculative arm achieves `100%` bitwise token equality (`eq_ar` = `24,360/24,360`, `Rep1==Rep2` = `13,020/13,020`)**. Primary two-repeat aggregation (`Tables 5A–5B`) establishes four scoped findings:

1. **Training-free `PrismLoop` (`Track 1`)** delivers **`1.030x–1.084x`** (Ouro) and **`1.024x–1.071x`** (Raven) two-repeat paired-median speedups over `4..2` `LoopSkim` (`95% CIs > 1.000x` in all 8 cells).
2. **Scoped same-checkpoint `8,192`-shortlist vs. full-vocabulary result on 1-step `prism1.pt`:** Slicing `prism1.pt` onto the `8,192` shortlist (`~70` $\mu\text{s}$ vs. `174`/`146` $\mu\text{s}$ full-$V$ graph) improves two-repeat pooled `decode tok/s` across **all `8/8` confirmation cells** (`Ouro`: `867.21` vs. `850.43` HE+, `439.28` vs. `427.31` MBPP+, `465.63` vs. `459.31` GSM8K, `507.40` vs. `501.66` MATH-500; `Raven`: `659.81` vs. `659.03` HE+, `593.97` vs. `589.78` MBPP+, `424.15` vs. `422.47` GSM8K, `626.45` vs. `622.85` MATH-500) at nearly identical forward cycles (`8,693` vs. `8,704` Ouro `GSM8K`; `11,464` vs. `11,464` Raven `GSM8K`). **Scope boundary:** This establishes a net projection-latency vs. step-1 coverage advantage specifically for 1-step `prism1.pt`; it does **not** rule out shortlist OOV errors in autoregressive steps `2..5` of the separate `paper4_mlp.pt` checkpoint or disentangle accuracy loss from projection savings in multi-step heads.
3. **Strict $w \geq 2$ bridging vs. permissive post-head requery & standalone `112p` controls (`Table 5B`):**
   - *Ouro code (`HE+`, `MBPP+`):* Standalone `5-Step 8k MLP` ($w \leq 1$) leads `112p` methods (`876.01` HE+, `446.93` MBPP+; `766p` scaled MLP reaches `885.17` and `489.64` in `Table A1`), because Ouro's `~1.8 ms` 4-loop cycle amortizes steps `2..5` (`6,505` vs. `6,919` cycles HE+; `5,328` vs. `5,820` MBPP+).
   - *Architecture split between `Strict` $w \geq 2$ and permissive requery on math:* On **Raven math**, **`PrismHead-8k + Strict` $w \geq 2$** (`0` $w=1$ hits, `0` rollouts) **already resolves two-repeat paired-median wins** over `4-Step Parallel 8k` (`424.19` vs. `416.73`, **`1.0161x [1.00890, 1.02142]`** on `GSM8K`; `621.43` vs. `613.42`, **`1.0136x [1.00363, 1.02338]`** on `MATH-500`). On **Ouro math**, however, `Strict` $w \geq 2$ ties `4-Step Parallel 8k` on `GSM8K` (`456.42` vs. `456.52`, `1.0005x [0.99540, 1.01007]`) and `5-Step MLP` ($w \leq 1$) on `MATH-500` (`500.13` vs. `502.29`, `0.9909x [0.98218, 1.00198]`), showing that permissive $w=1$/rollout fallback on $\hat{y}_{t+2}$ drives the Ouro `GSM8K` improvement (`465.63`, **`1.0216x [1.01610, 1.02781]`**, also exceeding `766p` scaled MLP `455.32`). Overall, `PrismHead-8k + Requery` resolves **`3/4` math cells** (`1.0216x` Ouro `GSM8K`, `1.0184x [1.00727, 1.02355]` Raven `GSM8K`, `1.0228x [1.01566, 1.03328]` Raven `MATH-500`), whereas **`Ouro MATH-500` is borderline/unresolved (`507.40` vs. `502.29`; `1.0105x [0.99995, 1.01476]`)**.
4. **Two-repeat status of `Bridge-Miss 8k MLP` (`Table 5B`):** Running MLP steps `2..5` only when permissive post-head requery returns empty resolves **`3/4` Raven cells** over `4-Step Parallel 8k` (`607.65` vs. `601.14`, `1.0174x [1.00996, 1.02290]` `MBPP+`; `422.58` vs. `416.73`, `1.0081x [1.00422, 1.01598]` `GSM8K`; `628.09` vs. `613.42`, `1.0241x [1.01611, 1.03370]` `MATH-500`), whereas **`Raven HumanEval+` is unresolved under combined two-repeat evidence (`671.07` vs. `665.29`; `1.0048x [0.99959, 1.00844]`, combining R1 `1.0072x` and R2 `1.0020x`)**, and all four Ouro cells have CIs straddling `1.000x` (`0.9941x–1.0046x`).

### 5.2 Same-Checkpoint Single-Factor Attribution & Requery Source Breakdown (`sel32`, Tables 6A–6B)

**Table 6A: Same-Checkpoint Single-Factor Attribution on `sel32` ($T=0, W \leq 80$, Reporting Pooled `decode tok/s` and `cycles`/`drafted_head_toks`).**

| Model & Same-Checkpoint Switch (`sel32`, $T=0$) | HE+ tok/s (`cyc`/`toks`) | MBPP+ tok/s (`cyc`/`toks`) | GSM8K tok/s (`cyc`/`toks`) | MATH-500 tok/s (`cyc`/`toks`) | `eq_ar` |
|---|---|---|---|---|---:|
| **Ouro** — PrismLoop (`Track 1`, $+1$ requery only, no head) | `829.2` (`2190`/`0`) | `426.9` (`1717`/`0`) | `460.3` (`2389`/`0`) | `446.3` (`17666`/`0`) | `128/128` |
| **Ouro** — PrismHead (`prism1.pt`, full-V, 1-step, gated, **no $+2$ req.**) | `879.7` (`1995`/`668`) | `458.7` (`1541`/`750`) | `460.1` (`2368`/`566`) | `467.2` (`16577`/`5839`) | `128/128` |
| **Ouro** — PrismHead + Requery (`prism1.pt`, full-V, 1-step, gated, **$w\ge 1$+roll**) | `883.0` (`1954`/`673`) | `465.4` (`1480`/`754`) | `464.2` (`2308`/`572`) | `473.3` (`15867`/`5882`) | `128/128` |
| **Ouro** — PrismHead + Requery (`prism1.pt`, full-V, 1-step, **ungated $\tau_1=0$**) | `893.9` (`1910`/`1062`) | `469.8` (`1458`/`1060`) | `460.6` (`2313`/`954`) | `475.3` (`15714`/`9496`) | `128/128` |
| **Ouro** — PrismHead-8k + Strict $w\ge 2$ (`prism1.pt`, `8k`, **$w\ge 2$ verbatim only**) | `876.4` (`1980`/`678`) | `461.9` (`1504`/`714`) | `457.7` (`2325`/`561`) | `471.1` (`16099`/`5844`) | `128/128` |
| **Ouro** — **PrismHead-8k + Requery** (`prism1.pt`, **`8k` shortlist**, $w\ge 1$+roll) | `888.3` (`1956`/`681`) | `473.3` (`1479`/`718`) | `462.9` (`2313`/`563`) | `478.7` (`15865`/`5867`) | `128/128` |
| **Ouro** — 5-Step 8k MLP (`paper4_mlp.pt`, 5-step, $w \le 2$, ungated, no req.) | `899.7` (`1816`/`5720`) | `475.5` (`1339`/`5690`) | `437.1` (`2318`/`7915`) | `456.2` (`15542`/`58905`) | `128/128` |
| **Ouro** — 5-Step 8k MLP (`paper4_mlp.pt`, 5-step, **$w \le 1$**, ungated, no req.) | `915.4` (`1800`/`4550`) | `488.9` (`1326`/`4440`) | `455.5` (`2290`/`4590`) | `473.2` (`15304`/`43710`) | `128/128` |
| **Ouro** — 1-Step 8k MLP (`paper4_mlp.pt`, **1-step**, $w \le 1$, ungated, **no req.**) | `902.2` (`1969`/`1054`) | `467.4` (`1528`/`1054`) | `463.0` (`2390`/`952`) | `475.9` (`16562`/`9412`) | `128/128` |
| **Ouro** — 1-Step 8k MLP + Strict $w\ge 2$ (`paper4_mlp.pt`, 1-step, **$w\ge 2$ only**) | `883.6` (`1947`/`1054`) | `469.1` (`1476`/`1053`) | `456.4` (`2324`/`952`) | `471.9` (`16001`/`9476`) | `128/128` |
| **Ouro** — 1-Step 8k MLP + Requery (`paper4_mlp.pt`, 1-step, **$w\ge 1$+roll**) | `906.3` (`1909`/`1054`) | `479.5` (`1435`/`1053`) | `465.8` (`2303`/`955`) | `474.7` (`15745`/`9505`) | `128/128` |
| **Ouro** — 1-Step 8k MLP + Requery (`paper4_mlp.pt`, 1-step, **gated $\tau_1$**) | `886.7` (`1922`/`699`) | `474.8` (`1452`/`726`) | `465.8` (`2291`/`654`) | `477.4` (`15795`/`6592`) | `128/128` |
| **Ouro** — Bridge-Miss 8k MLP (`paper4_mlp.pt`, **steps 2..5 iff requery empty**) | `909.6` (`1837`/`2454`) | `487.9` (`1355`/`2282`) | `456.6` (`2303`/`1469`) | `472.8` (`15524`/`16630`) | `128/128` |
| **Ouro** — 4-Step Parallel 8k (`loopskim_par.pt`, 4-step, $w \le 1$, no req.) | `907.0` (`1908`/`4044`) | `486.9` (`1409`/`3880`) | `458.1` (`2354`/`3824`) | `466.9` (`16291`/`37504`) | `128/128` |
| **Raven** — PrismLoop (`Track 1`, $+1$ requery only, no head) | `760.5` (`4039`/`0`) | `478.3` (`2526`/`0`) | `466.2` (`3199`/`0`) | `598.5` (`12361`/`0`) | `128/128` |
| **Raven** — PrismHead (`prism1.pt`, full-V, 1-step, gated, **no $+2$ req.**) | `767.4` (`3987`/`534`) | `496.9` (`2368`/`627`) | `466.8` (`3176`/`477`) | `619.4` (`11868`/`2816`) | `128/128` |
| **Raven** — PrismHead + Requery (`prism1.pt`, full-V, 1-step, gated, **$w\ge 1$+roll**) | `762.8` (`3916`/`537`) | `497.9` (`2294`/`634`) | `461.4` (`3138`/`481`) | `618.2` (`11389`/`2823`) | `128/128` |
| **Raven** — PrismHead + Requery (`prism1.pt`, full-V, 1-step, **ungated $\tau_1=0$**) | `759.1` (`3873`/`1156`) | `493.8` (`2250`/`1297`) | `446.0` (`3184`/`1381`) | `617.3` (`11290`/`5721`) | `128/128` |
| **Raven** — PrismHead-8k + Strict $w\ge 2$ (`prism1.pt`, `8k`, **$w\ge 2$ verbatim only**) | `776.5` (`3960`/`541`) | `504.5` (`2332`/`632`) | `469.4` (`3145`/`479`) | `626.0` (`11577`/`2862`) | `128/128` |
| **Raven** — **PrismHead-8k + Requery** (`prism1.pt`, **`8k` shortlist**, $w\ge 1$+roll) | `782.0` (`3916`/`543`) | `508.5` (`2293`/`633`) | `469.8` (`3138`/`482`) | `632.9` (`11391`/`2863`) | `128/128` |
| **Raven** — 5-Step 8k MLP (`paper4_mlp.pt`, 5-step, $w \le 2$, ungated, no req.) | `753.7` (`3772`/`7215`) | `488.2` (`2160`/`7410`) | `415.5` (`3253`/`10785`) | `588.1` (`11318`/`36125`) | `128/128` |
| **Raven** — 5-Step 8k MLP (`paper4_mlp.pt`, 5-step, **$w \le 1$**, ungated, no req.) | `775.0` (`3822`/`5225`) | `509.5` (`2156`/`5470`) | `445.3` (`3172`/`6630`) | `612.7` (`11068`/`26220`) | `128/128` |
| **Raven** — 1-Step 8k MLP (`paper4_mlp.pt`, **1-step**, $w \le 1$, ungated, **no req.**) | `764.4` (`3961`/`1183`) | `498.6` (`2343`/`1268`) | `453.1` (`3254`/`1363`) | `606.1` (`11936`/`5743`) | `128/128` |
| **Raven** — 1-Step 8k MLP + Strict $w\ge 2$ (`paper4_mlp.pt`, 1-step, **$w\ge 2$ only**) | `759.8` (`4033`/`1196`) | `504.6` (`2286`/`1284`) | `459.2` (`3203`/`1369`) | `623.0` (`11584`/`5768`) | `128/128` |
| **Raven** — 1-Step 8k MLP + Requery (`paper4_mlp.pt`, 1-step, **$w\ge 1$+roll**) | `768.3` (`3978`/`1198`) | `509.2` (`2237`/`1288`) | `456.0` (`3191`/`1374`) | `627.3` (`11362`/`5773`) | `128/128` |
| **Raven** — 1-Step 8k MLP + Requery (`paper4_mlp.pt`, 1-step, **gated $\tau_1$**) | `764.3` (`3891`/`816`) | `501.1` (`2255`/`927`) | `456.6` (`3139`/`792`) | `617.3` (`11370`/`3739`) | `128/128` |
| **Raven** — Bridge-Miss 8k MLP (`paper4_mlp.pt`, **steps 2..5 iff requery empty**) | `762.3` (`3938`/`2507`) | `515.7` (`2155`/`2703`) | `450.9` (`3185`/`2708`) | `622.5` (`11184`/`11272`) | `128/128` |
| **Raven** — 4-Step Parallel 8k (`loopskim_par.pt`, 4-step, $w \le 1$, no req.) | `767.1` (`3851`/`4548`) | `489.2` (`2293`/`4876`) | `443.6` (`3267`/`5548`) | `604.4` (`11722`/`22816`) | `128/128` |

**Table 6B: Exact Post-Head Suffix Requery Source Breakdown (`sel32`, $T=0$; Separating $w \geq 2$ Verbatim Anchors, $w = 1$ Matches on $\hat{y}_{t+2}$ Alone, and Stored Rollouts).**

| Model & Checkpoint (`sel32`, $T=0$) | Task | Requery Calls | Nonempty Hits (%) | **$w \geq 2$ Verbatim (%)** | **$w = 1$ Verbatim (%)** | **Rollout (%)** | Host $\mu$s/call |
|---|---|---:|---:|---:|---:|---:|---:|
| Ouro-1.4B — PrismHead-8k + Requery | HE+ | `681` | `466` (`68.4%`) | **`101` (`14.8%`)** | **`357` (`52.4%`)** | `8` (`1.2%`) | `20.8` |
| Ouro-1.4B — PrismHead-8k + Requery | MBPP+ | `718` | `467` (`65.0%`) | **`165` (`23.0%`)** | **`294` (`41.0%`)** | `8` (`1.1%`) | `17.5` |
| Ouro-1.4B — PrismHead-8k + Requery | GSM8K | `563` | `521` (`92.5%`) | **`292` (`51.9%`)** | **`229` (`40.7%`)** | `0` (`0.0%`) | `18.0` |
| Ouro-1.4B — PrismHead-8k + Requery | MATH-500 | `5,867` | `4,695` (`80.0%`) | **`1,778` (`30.3%`)** | **`2,871` (`48.9%`)** | `46` (`0.8%`) | `20.6` |
| Ouro-1.4B — 1-Step 8k MLP + Requery | HE+ | `1,054` | `633` (`60.1%`) | **`130` (`12.3%`)** | **`492` (`46.7%`)** | `11` (`1.0%`) | `21.5` |
| Ouro-1.4B — 1-Step 8k MLP + Requery | MBPP+ | `1,053` | `648` (`61.5%`) | **`228` (`21.6%`)** | **`399` (`37.9%`)** | `21` (`2.0%`) | `18.0` |
| Ouro-1.4B — 1-Step 8k MLP + Requery | GSM8K | `955` | `823` (`86.2%`) | **`406` (`42.5%`)** | **`406` (`42.5%`)** | `11` (`1.1%`) | `18.6` |
| Ouro-1.4B — 1-Step 8k MLP + Requery | MATH-500 | `9,505` | `7,449` (`78.4%`) | **`2,557` (`26.9%`)** | **`4,777` (`50.3%`)** | `115` (`1.2%`) | `20.6` |
| Ouro-1.4B — Bridge-Miss 8k MLP | HE+ | `962` | `589` (`61.2%`) | **`122` (`12.7%`)** | **`445` (`46.3%`)** | `22` (`2.3%`) | `21.9` |
| Ouro-1.4B — Bridge-Miss 8k MLP | MBPP+ | `938` | `602` (`64.2%`) | **`219` (`23.4%`)** | **`360` (`38.4%`)** | `23` (`2.5%`) | `18.7` |
| Ouro-1.4B — Bridge-Miss 8k MLP | GSM8K | `949` | `819` (`86.3%`) | **`406` (`42.8%`)** | **`401` (`42.3%`)** | `12` (`1.3%`) | `18.6` |
| Ouro-1.4B — Bridge-Miss 8k MLP | MATH-500 | `9,174` | `7,310` (`79.7%`) | **`2,478` (`27.0%`)** | **`4,633` (`50.5%`)** | `199` (`2.2%`) | `20.4` |
| Raven-TL — PrismHead-8k + Requery | HE+ | `543` | `415` (`76.4%`) | **`136` (`25.1%`)** | **`274` (`50.5%`)** | `5` (`0.9%`) | `48.5` |
| Raven-TL — PrismHead-8k + Requery | MBPP+ | `633` | `464` (`73.3%`) | **`189` (`29.9%`)** | **`274` (`43.3%`)** | `1` (`0.2%`) | `37.2` |
| Raven-TL — PrismHead-8k + Requery | GSM8K | `482` | `431` (`89.4%`) | **`249` (`51.7%`)** | **`181` (`37.5%`)** | `1` (`0.2%`) | `38.4` |
| Raven-TL — PrismHead-8k + Requery | MATH-500 | `2,863` | `2,291` (`80.0%`) | **`883` (`30.8%`)** | **`1,366` (`47.7%`)** | `42` (`1.5%`) | `48.7` |
| Raven-TL — 1-Step 8k MLP + Requery | HE+ | `1,198` | `783` (`65.4%`) | **`250` (`20.9%`)** | **`506` (`42.2%`)** | `27` (`2.2%`) | `50.3` |
| Raven-TL — 1-Step 8k MLP + Requery | MBPP+ | `1,288` | `826` (`64.1%`) | **`301` (`23.4%`)** | **`501` (`38.9%`)** | `24` (`1.9%`) | `38.0` |
| Raven-TL — 1-Step 8k MLP + Requery | GSM8K | `1,374` | `1,033` (`75.2%`) | **`423` (`30.8%`)** | **`583` (`42.4%`)** | `27` (`2.0%`) | `39.6` |
| Raven-TL — 1-Step 8k MLP + Requery | MATH-500 | `5,773` | `4,172` (`72.3%`) | **`1,365` (`23.6%`)** | **`2,645` (`45.8%`)** | `162` (`2.8%`) | `48.1` |
| Raven-TL — Bridge-Miss 8k MLP | HE+ | `1,103` | `752` (`68.2%`) | **`235` (`21.3%`)** | **`480` (`43.5%`)** | `37` (`3.4%`) | `53.7` |
| Raven-TL — Bridge-Miss 8k MLP | MBPP+ | `1,167` | `783` (`67.1%`) | **`286` (`24.5%`)** | **`461` (`39.5%`)** | `36` (`3.1%`) | `40.1` |
| Raven-TL — Bridge-Miss 8k MLP | GSM8K | `1,360` | `1,023` (`75.2%`) | **`418` (`30.7%`)** | **`576` (`42.4%`)** | `29` (`2.1%`) | `39.0` |
| Raven-TL — Bridge-Miss 8k MLP | MATH-500 | `5,496` | `4,052` (`73.7%`) | **`1,304` (`23.7%`)** | **`2,529` (`46.0%`)** | `219` (`4.0%`) | `49.0` |

Comparing single-factor switches on identical checkpoints (`Table 6A`, noting every single-cell exception) alongside `Table 6B` clarifies each mechanism:
1. **Trigger discipline ($w \leq 2 \to w \leq 1$ on `paper4_mlp.pt`):** Lifts `decode tok/s` across all `8/8` `sel32` cells (`437.1 -> 455.5` Ouro `GSM8K`, `415.5 -> 445.3` Raven `GSM8K`) and cuts forward cycles in `7/8` cells (**exception**: `Raven HE+` cycles rise `3,772 -> 3,822`, `+50`, while `decode tok/s` rises `753.7 -> 775.0` from `-1,990` fewer drafted head tokens).
2. **Horizon truncation *without* `+2` requery ($5 \to 1$ step, `no req.` on `paper4_mlp.pt`):** Increases forward cycles in all `8/8` cells; reduces `decode tok/s` across all `4/4` code cells (`915.4 -> 902.2` Ouro `HE+`, `488.9 -> 467.4` Ouro `MBPP+`, `775.0 -> 764.4` Raven `HE+`, `509.5 -> 498.6` Raven `MBPP+`) and `Raven MATH-500` (`612.7 -> 606.1`), yet already increases `decode tok/s` on `Ouro GSM8K` (`455.5 -> 463.0`), `Ouro MATH-500` (`473.2 -> 475.9`), and `Raven GSM8K` (`445.3 -> 453.1`).
3. **Exact source breakdown of post-head requery (`Table 6B`) & `no req. -> Strict` $w \geq 2$ `-> Permissive Requery` (`Table 6A`):** Across all 24 rows of `Table 6B`, nonempty post-head continuations (`60.1%–92.5%` of calls) comprise **`12.3%–51.9%` $w \geq 2$ verbatim anchors (`14.8%–51.9%` on `PrismHead-8k`)**, **`37.5%–52.4%` $w = 1$ verbatim matches on $\hat{y}_{t+2}$ alone**, and **`0.0%–4.0%` stored rollouts (`0.0%–1.5%` on `PrismHead-8k`)**. Holding horizon at `1` step:
   - *On `1-step paper4_mlp.pt`:* `no req. -> Strict` $w \geq 2$ cuts cycles in `7/8` cells (**exception**: `Raven HE+` `3,961 -> 4,033`) and lifts `decode tok/s` on `Raven MBPP+/GSM8K/MATH-500` and `Ouro MBPP+`, while lowering `Ouro HE+/GSM8K/MATH-500` and `Raven HE+` due to wider speculative batches on unaccepted tails; `no req. -> Permissive Requery` cuts cycles in `7/8` cells (**exception**: `Raven HE+` `3,961 -> 3,978`, `+17` cycles, while `decode tok/s` rises `764.4 -> 768.3`) and raises `decode tok/s` in `7/8` cells (**exception**: `Ouro MATH-500` `475.9 -> 474.7` despite `16,562 -> 15,745` cycles).
   - *On `prism1.pt`:* Full-$V$ `no req. -> Permissive Requery` cuts cycles in all `8/8` cells, raising `decode tok/s` in `4/4` Ouro cells and `Raven MBPP+` (`496.9 -> 497.9`) while host lookup (`37–49` $\mu\text{s}$) + wider batch rows slightly outweigh small cycle reductions on `Raven HE+` (`767.4 -> 762.8`), `Raven GSM8K` (`466.8 -> 461.4`), and `Raven MATH-500` (`619.4 -> 618.2`). Slicing `prism1.pt` to `8k` (`PrismHead-8k + Requery`) beats full-$V$ in `7/8` `sel32` cells (**exception**: `Ouro GSM8K` `464.2 -> 462.9`, resolved positively on `confirm128` at `465.63` vs. `459.31`), and `Strict` $w \geq 2 \to$ `Permissive Requery` on `PrismHead-8k` cuts cycles and lifts `decode tok/s` in all `8/8` `sel32` cells.
4. **Confidence gating (`ungated <-> gated`):** Removing $\tau_1$ on `prism1.pt` degrades `GSM8K` (`464.2 -> 460.6` Ouro; `461.4 -> 446.0` Raven, `3,138 -> 3,184` cyc) and all `4/4` Raven cells while lifting Ouro `HE+/MBPP+/MATH-500`; adding $\tau_1$ to `1-step paper4_mlp.pt` trims Raven `GSM8K` cycles (`3,191 -> 3,139`, `456.0 -> 456.6` tok/s) and lifts Ouro `MATH-500` (`474.7 -> 477.4`) while reducing code (`906.3 -> 886.7` Ouro `HE+`).

### 5.3 Interleaved 2-Repeat Live Sampler Serving & Coupled Nucleus Confirmation ($T > 0, W \leq 80$)

**Table 2C: Interleaved Two-Repeat Live Coupled Sampler Serving (`confirm64`, `PrismLoop Track 1`; R1 Forward Order, R2 Reversed Order).**

| Regime & Model (`confirm64`, 2-Repeat Mean: R1 fwd, R2 rev) | Task | Sort 2-Rep tok/s (R1/R2) | FlashInfer AIR 2-Rep tok/s (R1/R2) & Med. vs. Sort [95% CI] | **1-CTA Bit-Lattice 2-Rep tok/s (R1/R2)** | Bit-Lattice Med. vs. Sort [95% CI] | Bit-Lattice Med. vs. AIR [95% CI] | `eq_ar` |
|---|---|---:|---|---|---|---|---:|
| $T=0.6, p=0.95$ — Ouro-1.4B | HE+ | `632.65` (`637.1`/`628.3`) | `665.10` (`664.0`/`666.2`; `1.0519x` [1.048, 1.054]) | **`656.12`** (`654.4`/`657.8`) | `1.0378x` [1.034, 1.042] | `0.9863x` [0.985, 0.989] | `64/64` |
| $T=0.6, p=0.95$ — Ouro-1.4B | GSM8K | `391.71` (`392.5`/`390.9`) | `408.55` (`408.9`/`408.2`; `1.0420x` [1.041, 1.044]) | **`400.98`** (`401.3`/`400.7`) | `1.0205x` [1.019, 1.023] | `0.9804x` [0.979, 0.982] | `64/64` |
| $T=0.6, p=0.95$ — Raven-TL | HE+ | `579.75` (`588.9`/`570.9`) | `594.97` (`600.4`/`589.6`; `1.0239x` [1.021, 1.027]) | **`596.77`** (`603.3`/`590.4`) | `1.0282x` [1.025, 1.032] | `1.0043x` [1.001, 1.005] | `64/64` |
| $T=0.6, p=0.95$ — Raven-TL | GSM8K | `329.58` (`335.6`/`323.8`) | `340.49` (`343.3`/`337.8`; `1.0353x` [1.034, 1.037]) | **`341.21`** (`343.5`/`338.9`) | `1.0376x` [1.036, 1.039] | `1.0019x` [1.001, 1.003] | `64/64` |
| $T=1.0, p=0.90$ — Ouro-1.4B | HE+ | `608.65` (`607.8`/`609.5`) | `634.56` (`634.3`/`634.9`; `1.0392x` [1.038, 1.040]) | **`617.93`** (`618.8`/`617.1`) | `1.0123x` [1.010, 1.017] | `0.9736x` [0.972, 0.979] | `64/64` |
| $T=1.0, p=0.90$ — Ouro-1.4B | GSM8K | `352.76` (`352.8`/`352.7`) | `364.87` (`363.5`/`366.2`; `1.0337x` [1.032, 1.036]) | **`351.82`** (`350.9`/`352.8`) | `0.9985x` [0.996, 1.000] | `0.9658x` [0.964, 0.968] | `64/64` |
| $T=1.0, p=0.90$ — Raven-TL | HE+ | `439.98` (`445.7`/`434.4`) | `449.91` (`455.5`/`444.5`; `1.0226x` [1.020, 1.024]) | **`453.22`** (`457.6`/`448.9`) | `1.0287x` [1.027, 1.030] | `1.0071x` [1.005, 1.009] | `64/64` |
| $T=1.0, p=0.90$ — Raven-TL | GSM8K | `306.71` (`309.3`/`304.1`) | `315.04` (`318.3`/`311.9`; `1.0274x` [1.026, 1.029]) | **`314.41`** (`316.9`/`311.9`) | `1.0272x` [1.025, 1.029] | `0.9985x` [0.996, 1.002] | `64/64` |

![Figure 3: Disjoint confirmation decode throughput under wide-frontier (W at most 80) coupled nucleus sampling at (A) T=0.6, top-p=0.95 and (B) T=1.0, top-p=0.90 at 100% bitwise eq_ar.](supplement/figures/figure-3.png)

**Table 7A: Coupled Nucleus Sampling Confirmation — $T = 0.6, \text{top-}p = 0.95$ (`confirm64` HE+, `holdout128` MBPP+, `confirm64` GSM8K).**

| Model | Task | Method | Pooled Decode tok/s | Client tok/s | vs. AR | Med. vs. LS `4..2` [95% CI] | Med. vs. LS `4..1` [95% CI] | Acc. (%) | `eq_ar` |
|---|---|---|---:|---:|---:|---|---|---:|---:|
| Ouro-1.4B | HE+ | Coupled AR ($W=1$) | `107.87` | `104.79` | `1.00x` | `0.1672x` [0.148, 0.180] | `0.1633x` [0.149, 0.177] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | LoopSkim (`4..2`, $G=8$) | `630.22` | `540.57` | `5.84x` | `1.0000x` [1.000, 1.000] | `0.9924x` [0.984, 1.001] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | LoopSkim (`4..1`, $G=8$) | `639.36` | `548.84` | `5.93x` | `1.0077x` [0.999, 1.017] | `1.0000x` [1.000, 1.000] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | **PrismLoop (`Track 1`)** | `646.90` | `553.11` | `6.00x` | `1.0207x` [1.007, 1.033] | `1.0054x` [0.996, 1.014] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | PrismHead + Requery (Uncoupled) | `686.02` | `580.74` | `6.36x` | `1.0728x` [1.060, 1.115] | `1.0719x` [1.054, 1.090] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | **PrismHead + Requery (Coupled)** | `678.85` | `572.18` | `6.29x` | `1.0666x` [1.050, 1.096] | `1.0607x` [1.040, 1.077] | 68.75 | `64/64` |
| Ouro-1.4B | MBPP+ | Coupled AR ($W=1$) | `109.51` | `100.75` | `1.00x` | `0.3527x` [0.340, 0.357] | `0.3316x` [0.322, 0.336] | 68.75 | `128/128` |
| Ouro-1.4B | MBPP+ | LoopSkim (`4..2`, $G=8$) | `321.91` | `257.69` | `2.94x` | `1.0000x` [1.000, 1.000] | `0.9417x` [0.932, 0.952] | 68.75 | `128/128` |
| Ouro-1.4B | MBPP+ | LoopSkim (`4..1`, $G=8$) | `344.56` | `272.13` | `3.15x` | `1.0619x` [1.050, 1.073] | `1.0000x` [1.000, 1.000] | 68.75 | `128/128` |
| Ouro-1.4B | MBPP+ | **PrismLoop (`Track 1`)** | `347.26` | `273.41` | `3.17x` | `1.0793x` [1.064, 1.090] | `1.0074x` [0.997, 1.013] | 68.75 | `128/128` |
| Ouro-1.4B | MBPP+ | PrismHead + Requery (Uncoupled) | `389.87` | `300.76` | `3.56x` | `1.2254x` [1.205, 1.243] | `1.1528x` [1.135, 1.172] | 68.75 | `128/128` |
| Ouro-1.4B | MBPP+ | **PrismHead + Requery (Coupled)** | `384.11` | `296.29` | `3.51x` | `1.2088x` [1.181, 1.227] | `1.1318x` [1.109, 1.151] | 68.75 | `128/128` |
| Ouro-1.4B | GSM8K | Coupled AR ($W=1$) | `107.01` | `101.63` | `1.00x` | `0.2856x` [0.271, 0.293] | `0.2764x` [0.259, 0.286] | 73.44 | `64/64` |
| Ouro-1.4B | GSM8K | LoopSkim (`4..2`, $G=8$) | `370.74` | `316.20` | `3.46x` | `1.0000x` [1.000, 1.000] | `0.9554x` [0.947, 0.963] | 73.44 | `64/64` |
| Ouro-1.4B | GSM8K | LoopSkim (`4..1`, $G=8$) | `388.35` | `328.31` | `3.63x` | `1.0467x` [1.039, 1.056] | `1.0000x` [1.000, 1.000] | 73.44 | `64/64` |
| Ouro-1.4B | GSM8K | **PrismLoop (`Track 1`)** | `394.21` | `331.81` | `3.68x` | `1.0710x` [1.059, 1.085] | `1.0150x` [1.010, 1.024] | 73.44 | `64/64` |
| Ouro-1.4B | GSM8K | PrismHead + Requery (Uncoupled) | `402.58` | `337.29` | `3.76x` | `1.0901x` [1.070, 1.107] | `1.0399x` [1.020, 1.051] | 73.44 | `64/64` |
| Ouro-1.4B | GSM8K | **PrismHead + Requery (Coupled)** | `398.75` | `335.36` | `3.73x` | `1.0849x` [1.057, 1.101] | `1.0265x` [1.015, 1.041] | 73.44 | `64/64` |
| Raven-TL | HE+ | Coupled AR ($W=1$) | `47.77` | `46.49` | `1.00x` | `0.1030x` [0.088, 0.112] | `0.0948x` [0.085, 0.105] | 15.62 | `64/64` |
| Raven-TL | HE+ | LoopSkim (`4..2`, $G=8$) | `561.49` | `416.93` | `11.75x` | `1.0000x` [1.000, 1.000] | `0.9504x` [0.932, 0.963] | 15.62 | `64/64` |
| Raven-TL | HE+ | LoopSkim (`4..1`, $G=8$) | `597.71` | `437.18` | `12.51x` | `1.0522x` [1.039, 1.072] | `1.0000x` [1.000, 1.000] | 15.62 | `64/64` |
| Raven-TL | HE+ | **PrismLoop (`Track 1`)** | `599.45` | `437.83` | `12.55x` | `1.0609x` [1.051, 1.084] | `1.0060x` [0.998, 1.010] | 15.62 | `64/64` |
| Raven-TL | HE+ | PrismHead + Requery (Uncoupled) | `613.41` | `446.24` | `12.84x` | `1.1008x` [1.079, 1.121] | `1.0506x` [1.022, 1.060] | 15.62 | `64/64` |
| Raven-TL | HE+ | **PrismHead + Requery (Coupled)** | `612.60` | `446.80` | `12.82x` | `1.1132x` [1.089, 1.134] | `1.0476x` [1.032, 1.077] | 15.62 | `64/64` |
| Raven-TL | MBPP+ | Coupled AR ($W=1$) | `48.03` | `45.18` | `1.00x` | `0.1722x` [0.156, 0.186] | `0.1566x` [0.145, 0.168] | 18.75 | `128/128` |
| Raven-TL | MBPP+ | LoopSkim (`4..2`, $G=8$) | `435.01` | `274.64` | `9.06x` | `1.0000x` [1.000, 1.000] | `0.9402x` [0.929, 0.950] | 18.75 | `128/128` |
| Raven-TL | MBPP+ | LoopSkim (`4..1`, $G=8$) | `463.04` | `283.72` | `9.64x` | `1.0636x` [1.052, 1.076] | `1.0000x` [1.000, 1.000] | 18.75 | `128/128` |
| Raven-TL | MBPP+ | **PrismLoop (`Track 1`)** | `463.17` | `284.23` | `9.64x` | `1.0692x` [1.050, 1.075] | `0.9967x` [0.991, 1.002] | 18.75 | `128/128` |
| Raven-TL | MBPP+ | PrismHead + Requery (Uncoupled) | `487.00` | `292.59` | `10.14x` | `1.1365x` [1.120, 1.154] | `1.0638x` [1.052, 1.081] | 18.75 | `128/128` |
| Raven-TL | MBPP+ | **PrismHead + Requery (Coupled)** | `491.52` | `293.18` | `10.23x` | `1.1410x` [1.128, 1.171] | `1.0673x` [1.052, 1.099] | 18.75 | `128/128` |
| Raven-TL | GSM8K | Coupled AR ($W=1$) | `47.95` | `44.71` | `1.00x` | `0.1549x` [0.146, 0.162] | `0.1423x` [0.132, 0.148] | 40.62 | `64/64` |
| Raven-TL | GSM8K | LoopSkim (`4..2`, $G=8$) | `311.75` | `205.42` | `6.50x` | `1.0000x` [1.000, 1.000] | `0.9116x` [0.902, 0.922] | 40.62 | `64/64` |
| Raven-TL | GSM8K | LoopSkim (`4..1`, $G=8$) | `341.44` | `221.01` | `7.12x` | `1.0969x` [1.084, 1.109] | `1.0000x` [1.000, 1.000] | 40.62 | `64/64` |
| Raven-TL | GSM8K | **PrismLoop (`Track 1`)** | `342.01` | `220.14` | `7.13x` | `1.0970x` [1.088, 1.111] | `0.9969x` [0.992, 1.006] | 40.62 | `64/64` |
| Raven-TL | GSM8K | PrismHead + Requery (Uncoupled) | `343.77` | `221.38` | `7.17x` | `1.1049x` [1.099, 1.115] | `1.0007x` [0.992, 1.012] | 40.62 | `64/64` |
| Raven-TL | GSM8K | **PrismHead + Requery (Coupled)** | `341.94` | `218.51` | `7.13x` | `1.1078x` [1.090, 1.112] | `0.9937x` [0.978, 1.011] | 40.62 | `64/64` |

**Table 7B: Coupled Nucleus Sampling Confirmation — $T = 1.0, \text{top-}p = 0.90$ (`confirm64` HE+, `confirm64` GSM8K).**

| Model | Task | Method | Pooled Decode tok/s | Client tok/s | vs. AR | Med. vs. LS `4..2` [95% CI] | Med. vs. LS `4..1` [95% CI] | Acc. (%) | `eq_ar` |
|---|---|---|---:|---:|---:|---|---|---:|---:|
| Ouro-1.4B | HE+ | Coupled AR ($W=1$) | `108.48` | `105.30` | `1.00x` | `0.1878x` [0.174, 0.204] | `0.1841x` [0.163, 0.197] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | LoopSkim (`4..2`, $G=8$) | `583.95` | `500.26` | `5.38x` | `1.0000x` [1.000, 1.000] | `0.9716x` [0.960, 0.989] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | LoopSkim (`4..1`, $G=8$) | `603.74` | `518.48` | `5.57x` | `1.0292x` [1.011, 1.041] | `1.0000x` [1.000, 1.000] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | **PrismLoop (`Track 1`)** | `611.12` | `521.12` | `5.63x` | `1.0359x` [1.028, 1.048] | `1.0087x` [0.999, 1.017] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | PrismHead + Requery (Uncoupled) | `640.61` | `544.04` | `5.91x` | `1.0979x` [1.077, 1.118] | `1.0605x` [1.041, 1.077] | 68.75 | `64/64` |
| Ouro-1.4B | HE+ | **PrismHead + Requery (Coupled)** | `633.74` | `540.41` | `5.84x` | `1.0798x` [1.069, 1.096] | `1.0382x` [1.030, 1.075] | 68.75 | `64/64` |
| Ouro-1.4B | GSM8K | Coupled AR ($W=1$) | `107.16` | `102.12` | `1.00x` | `0.3306x` [0.316, 0.357] | `0.3151x` [0.302, 0.336] | 70.31 | `64/64` |
| Ouro-1.4B | GSM8K | LoopSkim (`4..2`, $G=8$) | `325.80` | `282.68` | `3.04x` | `1.0000x` [1.000, 1.000] | `0.9577x` [0.950, 0.965] | 70.31 | `64/64` |
| Ouro-1.4B | GSM8K | LoopSkim (`4..1`, $G=8$) | `339.10` | `292.95` | `3.16x` | `1.0442x` [1.036, 1.053] | `1.0000x` [1.000, 1.000] | 70.31 | `64/64` |
| Ouro-1.4B | GSM8K | **PrismLoop (`Track 1`)** | `348.50` | `299.51` | `3.25x` | `1.0672x` [1.061, 1.078] | `1.0251x` [1.019, 1.031] | 70.31 | `64/64` |
| Ouro-1.4B | GSM8K | PrismHead + Requery (Uncoupled) | `349.01` | `299.30` | `3.26x` | `1.0726x` [1.060, 1.084] | `1.0321x` [1.018, 1.042] | 70.31 | `64/64` |
| Ouro-1.4B | GSM8K | **PrismHead + Requery (Coupled)** | `342.74` | `296.47` | `3.20x` | `1.0532x` [1.042, 1.067] | `1.0132x` [1.005, 1.020] | 70.31 | `64/64` |
| Raven-TL | HE+ | Coupled AR ($W=1$) | `47.68` | `46.48` | `1.00x` | `0.1231x` [0.113, 0.135] | `0.1133x` [0.110, 0.130] | 7.81 | `64/64` |
| Raven-TL | HE+ | LoopSkim (`4..2`, $G=8$) | `427.35` | `344.48` | `8.96x` | `1.0000x` [1.000, 1.000] | `0.9571x` [0.948, 0.971] | 7.81 | `64/64` |
| Raven-TL | HE+ | LoopSkim (`4..1`, $G=8$) | `449.41` | `356.17` | `9.43x` | `1.0448x` [1.031, 1.055] | `1.0000x` [1.000, 1.000] | 7.81 | `64/64` |
| Raven-TL | HE+ | **PrismLoop (`Track 1`)** | `454.27` | `363.01` | `9.53x` | `1.0554x` [1.045, 1.068] | `1.0083x` [1.000, 1.017] | 7.81 | `64/64` |
| Raven-TL | HE+ | PrismHead + Requery (Uncoupled) | `458.42` | `363.16` | `9.61x` | `1.0697x` [1.055, 1.103] | `1.0197x` [1.011, 1.037] | 7.81 | `64/64` |
| Raven-TL | HE+ | **PrismHead + Requery (Coupled)** | `458.75` | `364.66` | `9.62x` | `1.0755x` [1.052, 1.099] | `1.0289x` [1.012, 1.040] | 7.81 | `64/64` |
| Raven-TL | GSM8K | Coupled AR ($W=1$) | `47.46` | `45.41` | `1.00x` | `0.1630x` [0.153, 0.171] | `0.1539x` [0.140, 0.163] | 28.12 | `64/64` |
| Raven-TL | GSM8K | LoopSkim (`4..2`, $G=8$) | `294.16` | `226.31` | `6.20x` | `1.0000x` [1.000, 1.000] | `0.9266x` [0.917, 0.942] | 28.12 | `64/64` |
| Raven-TL | GSM8K | LoopSkim (`4..1`, $G=8$) | `312.66` | `235.71` | `6.59x` | `1.0792x` [1.062, 1.091] | `1.0000x` [1.000, 1.000] | 28.12 | `64/64` |
| Raven-TL | GSM8K | **PrismLoop (`Track 1`)** | `315.51` | `240.26` | `6.65x` | `1.0721x` [1.056, 1.088] | `1.0037x` [0.994, 1.015] | 28.12 | `64/64` |
| Raven-TL | GSM8K | PrismHead + Requery (Uncoupled) | `315.06` | `237.47` | `6.64x` | `1.0770x` [1.057, 1.086] | `0.9942x` [0.987, 1.009] | 28.12 | `64/64` |
| Raven-TL | GSM8K | **PrismHead + Requery (Coupled)** | `316.55` | `239.99` | `6.67x` | `1.0744x` [1.065, 1.087] | `0.9948x` [0.987, 1.013] | 28.12 | `64/64` |

Interleaving two counterbalanced live repeats (`Table 2C`) separates kernel differences from session drift: (1) all three samplers match width-1 `AR` `64/64` bitwise in every cell; `FlashInfer AIR` (`18.8 MB` workspace) leads all `4/4` Ouro cells (`1.0337x–1.0519x` vs. `Sort`, `95% CIs > 1`), whereas zero-workspace `1-CTA Bit-Lattice` (`0 MB`) beats `Sort` in `7/8` cells (`0.9985x [0.996, 1.000]` tie on `Ouro GSM8K` $T=1.0$, where multi-pass `[M, 49152]` scans interact with 24-layer L2 residency) and edges or ties `AIR` on Raven (`1.0019x–1.0071x` on `3/4` cells; `0.9985x [0.996, 1.002]` on `Raven GSM8K` $T=1.0$); and (2) across all `3840` runs in Tables 7A–7B (`3840/3840` `eq_ar`), speculative decoding reaches **`3.17x–12.84x`** pooled decode gains over `Coupled AR` (**`1.053x–1.209x`** coupled and **`1.070x–1.225x`** uncoupled paired-median speedups over `4..2` `LoopSkim`).

### 5.4 Request-Setup & `Prompt-CoW` Coda Confirmation (`Table 8`)

**Table 8: Two-Repeat Request-Level (`client tok/s` & `decode tok/s`) Confirmation of `O(1) SlotBegin` and `Prompt-CoW` Coda (`confirm_t0` + `confirm_t0_rep2`).**

| Model | Task | Request-Setup / Coda Arm (on `PrismHead-8k + Requery`) | 2-Rep Client tok/s (R1/R2) vs. Base | Client Med. Speedup [95% CI] | 2-Rep Decode tok/s (Med. [95% CI]) | Setup+Prefill ms/req (vs. Base) | `eq_ar` |
|---|---|---|---:|---|---|---:|---:|
| Ouro-1.4B | HE+ | + `O(1) SlotBegin` (`23,461` slots) | **`710.39`** (`713.5`/`707.3`) vs. `721.72` | **`0.9874x`** [0.984, 0.990] | `847.61` (`0.9792x` [0.978, 0.980]) | `46.78` vs. `47.72` | `100/100` |
| Ouro-1.4B | MBPP+ | + `O(1) SlotBegin` (`23,461` slots) | **`323.31`** (`325.0`/`321.6`) vs. `328.47` | **`0.9872x`** [0.984, 0.991] | `428.41` (`0.9789x` [0.977, 0.980]) | `45.94` vs. `46.49` | `128/128` |
| Ouro-1.4B | GSM8K | + `O(1) SlotBegin` (`23,461` slots) | **`380.31`** (`380.5`/`380.1`) vs. `384.38` | **`0.9884x`** [0.987, 0.990] | `457.88` (`0.9822x` [0.981, 0.983]) | `45.57` vs. `46.44` | `128/128` |
| Ouro-1.4B | MATH-500 | + `O(1) SlotBegin` (`23,461` slots) | **`483.83`** (`485.4`/`482.3`) vs. `491.06` | **`0.9853x`** [0.983, 0.988] | `499.26` (`0.9833x` [0.982, 0.986]) | `52.78` vs. `54.19` | `64/64` |
| Raven-TL | HE+ | + `O(1) SlotBegin` (`65,536` slots) | **`504.15`** (`499.8`/`508.6`) vs. `471.51` | **`1.0817x`** [1.071, 1.090] | `669.43` (`1.0152x` [1.014, 1.017]) | `140.29` vs. `173.40` | `100/100` |
| Raven-TL | HE+ | **+ `Prompt-CoW` Coda ($5 \to 1$ prefill)** | **`515.93`** (`513.9`/`518.0`) vs. `471.51` | **`1.1127x`** [1.098, 1.125] | `676.43` (`1.0242x` [1.020, 1.032]) | `131.75` vs. `173.40` | `100/100` |
| Raven-TL | HE+ | + `Full-CoW` Coda (prefill + decode) | **`505.89`** (`503.4`/`508.4`) vs. `471.51` | **`1.0873x`** [1.072, 1.102] | `661.19` (`1.0033x` [0.996, 1.008]) | `133.01` vs. `173.40` | `100/100` |
| Raven-TL | MBPP+ | + `O(1) SlotBegin` (`65,536` slots) | **`376.42`** (`377.0`/`375.8`) vs. `354.90` | **`1.0825x`** [1.072, 1.090] | `598.15` (`1.0099x` [1.009, 1.010]) | `143.14` vs. `164.84` | `128/128` |
| Raven-TL | MBPP+ | **+ `Prompt-CoW` Coda ($5 \to 1$ prefill)** | **`388.04`** (`389.0`/`387.0`) vs. `354.90` | **`1.1371x`** [1.120, 1.146] | `595.37` (`1.0096x` [1.005, 1.012]) | `130.44` vs. `164.84` | `128/128` |
| Raven-TL | MBPP+ | + `Full-CoW` Coda (prefill + decode) | **`382.24`** (`380.2`/`384.3`) vs. `354.90` | **`1.1173x`** [1.105, 1.129] | `588.75` (`0.9990x` [0.994, 1.001]) | `133.38` vs. `164.84` | `128/128` |
| Raven-TL | GSM8K | + `O(1) SlotBegin` (`65,536` slots) | **`276.51`** (`277.8`/`275.2`) vs. `258.22` | **`1.0756x`** [1.073, 1.079] | `430.36` (`1.0153x` [1.013, 1.017]) | `139.68` vs. `163.69` | `128/128` |
| Raven-TL | GSM8K | **+ `Prompt-CoW` Coda ($5 \to 1$ prefill)** | **`284.42`** (`284.1`/`284.7`) vs. `258.22` | **`1.1122x`** [1.104, 1.119] | `430.54` (`1.0119x` [1.008, 1.016]) | `128.92` vs. `163.69` | `128/128` |
| Raven-TL | GSM8K | + `Full-CoW` Coda (prefill + decode) | **`280.79`** (`278.8`/`282.8`) vs. `258.22` | **`1.0949x`** [1.086, 1.104] | `426.18` (`0.9965x` [0.988, 1.003]) | `131.27` vs. `163.69` | `128/128` |
| Raven-TL | MATH-500 | + `O(1) SlotBegin` (`65,536` slots) | **`553.09`** (`547.6`/`558.7`) vs. `536.45` | **`1.0329x`** [1.030, 1.038] | `633.27` (`1.0124x` [1.007, 1.016]) | `152.87` vs. `178.86` | `64/64` |
| Raven-TL | MATH-500 | **+ `Prompt-CoW` Coda ($5 \to 1$ prefill)** | **`563.16`** (`564.0`/`562.4`) vs. `536.45` | **`1.0563x`** [1.050, 1.063] | `640.02` (`1.0245x` [1.019, 1.030]) | `142.40` vs. `178.86` | `64/64` |
| Raven-TL | MATH-500 | + `Full-CoW` Coda (prefill + decode) | **`550.33`** (`548.6`/`552.0`) vs. `536.45` | **`1.0247x`** [1.021, 1.035] | `625.06` (`0.9951x` [0.990, 1.002]) | `145.07` vs. `178.86` | `64/64` |

`Table 8` isolates per-request setup and Coda prefill across both architectures at `100%` bitwise `eq_ar`:
1. **Raven-TinyLlama (`65,536` slots, 5 Coda timelines):** `+ O(1) SlotBegin` alone cuts setup+prefill overhead by `21.7–33.1 ms/req`, lifting two-repeat `client tok/s` by `1.0329x–1.0825x`. Adding **`+ Prompt-CoW` Coda ($5 \to 1$ Coda prefill)** reduces per-request setup+prefill from `163.69–178.86 ms` to `128.92–142.40 ms` (`-34.4` to `-41.7 ms/req`), lifting two-repeat **`client tok/s` by `1.0563x–1.1371x` across all `4/4` Raven benchmarks (`95% CIs > 1.000x`)** and `decode tok/s` by `1.0096x–1.0245x` (`1.1127x` client / `1.0242x` decode HE+, `1.1371x` / `1.0096x` MBPP+, `1.1122x` / `1.0119x` GSM8K, `1.0563x` / `1.0245x` MATH-500). Extending KV page-table aliasing into decode (`+ Full-CoW`) lowers `decode tok/s` relative to `Prompt-CoW` across all `4/4` tasks (`0.9951x–1.0033x` vs. base) due to intermediate Coda flip inflation, confirming prefill-only aliasing is optimal (dropping `post-15` in `Lean-Coda {2,4,8,32}` likewise reduces `sel32` math/MBPP+ `decode tok/s` by `1.7%–4.1%` in `results/wave3_raven_cow_report.json`).
2. **Ouro-1.4B (`23,461` slots, 1 attention-free readout):** Because Ouro has `2.8x` fewer slot IDs and no multi-timeline Coda, `+ O(1) SlotBegin` saves `< 1.41 ms/req` (`0.9853x–0.9884x` `client tok/s`, within ~`1.2%–1.5%` cross-session variation).

---

## 6. Limitations

1. **Batch-1, Short/Medium Context ($L \leq 2\text{K}$), & Target-State Scope:** All experiments use $B=1$ ($1 \leq M \leq 80$) at $L \leq 2\text{K}$ (whereas 8K–16K KV-bandwidth and prefill regimes are governed by [16, 17, 18]) and zero-external-model target-state heads (`5-Step 8k MLP` ($w \leq 1$) leads Ouro code, `Ouro MATH-500` and `Raven HE+` `Bridge-Miss` are unresolved in `Table 5B`, and external causal students [14]—for which a standalone SM120 two-stream overlap microbenchmark in `results/bench_async_student_overlap.json` hides `50.4%–51.9%` of a 4-layer `short8k` pass at `0` bit diff—remain an open live-serving direction).
2. **Reference-Scoped Exactness, Conditional Intervals, & Community Exposure:** `100%` `eq_ar` holds relative to width-1 `AR` under the same invariant GEMM/attention and 23-bit SplitMix32 contract (`9,999/10,000` random BF16 rows match FP64 `cumsum`), bootstrap CIs are conditional on the measured two-repeat runs, and all four benchmarks have prior community exposure [13, 15].
3. **Residual Raven Prefill Cost:** Even after `Prompt-CoW` ($5 \to 1$ Coda prefill), Prelude + 32-loop core + 1 Coda prefill (`129–142 ms/req`) keeps Raven `client tok/s` `12%–35%` below `decode tok/s` on short completions.

---

## 7. Reproducibility

`supplement.zip` (`698.6` KB compressed, `1.97` MB expanded, `57` files, zero private paths) provides a self-contained verification chain:
- **`RUN.md`, `code/scripts/prepare_splits.py`, & `results/checkpoints_and_splits_sha256.json`:** `RUN.md` maps our overlay onto `looped-decoding-supplement.zip`; `prepare_splits.py --verify` deterministically checks all `40` split JSONs + `partitions.json` + SHA-256 digests of every split and `.pt` checkpoint.
- **`results/per_task_records.csv` (`41,812` records), `results/sample_retained_generations.jsonl` (`64` full raw `output_ids` arrays + grades, `52/52` direct speculative/AR token-array matches), & `results/live_head_audit_v6.json`:** Running `python3 code/scripts/reproduce_tables.py` (`< 5s`, Python stdlib only) directly emits **every serving table and headline contrast** (`Tables 2C, 4, 5A, 5B, 6A, 6B, 7A, 7B, 8, A1–A4`), verifies `37,580/37,580` `eq_ar` digests, checks all `64` raw token arrays, and runs the scalar `30`-step ($\leq 31$ global) Stage-B bit-lattice simulation (`Tables 2A, 2B, 3` come from `results/sampler_flashinfer_benchmark_v4.json` and `results/*_v3_calibration_and_audit.json`, regenerated via `RUN.md` §2–3).

---

## Appendix A. Complete Two-Repeat Confirmation (`Table A1`) & Out-of-Sample `sel32` Tables (`Tables A2–A4`)

**Table A1: Complete 17-Arm Disjoint Two-Repeat Greedy Confirmation ($T=0, W \leq 80$, All Arms & Repeats).**

| Model | Task | Method | 2-Rep Decode tok/s (R1/R2) | 2-Rep Client tok/s | 2-Rep Med. vs. LS `4..2` [95% CI] | 2-Rep Med. vs. LS `4..1` [95% CI] | Cycles | Acc. (%) | `eq_ar` (R1==R2) |
|---|---|---|---:|---:|---|---|---:|---:|---:|
| Ouro-1.4B | HE+ | Autoregressive ($W=1$) | `105.16` (`104.9`/`105.4`) | `102.77` | `0.1375x` [0.130, 0.148] | `0.1337x` [0.128, 0.142] | `0` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | CopyLoop (`4..1`, $K=6$) | `690.63` (`690.1`/`691.2`) | `595.53` | `0.9053x` [0.898, 0.931] | `0.8952x` [0.882, 0.904] | `9,210` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | LoopSkim (`4..2`, $G=8$) | `755.28` (`755.2`/`755.3`) | `643.65` | `1.0000x` [1.000, 1.000] | `0.9827x` [0.976, 0.993] | `8,452` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | LoopSkim (`4..1`, $G=8$) | `772.35` (`770.7`/`774.0`) | `653.98` | `1.0176x` [1.007, 1.024] | `1.0000x` [1.000, 1.000] | `7,968` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | PrismLoop (`Track 1`) | `785.11` (`788.5`/`781.7`) | `664.40` | `1.0298x` [1.024, 1.043] | `1.0133x` [1.011, 1.020] | `7,834` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | 5-Step 8k MLP ($w \le 2$, 112p) | `851.64` (`852.1`/`851.1`) | `711.76` | `1.0912x` [1.063, 1.136] | `1.0603x` [1.043, 1.102] | `6,606` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | 5-Step 8k MLP ($w \le 2$, 766p) | `885.17` (`886.3`/`884.0`) | `735.82` | `1.1675x` [1.143, 1.207] | `1.1447x` [1.101, 1.191] | `6,400` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | 5-Step 8k MLP ($w \le 1$, 112p) | `876.01` (`880.3`/`871.8`) | `729.76` | `1.1332x` [1.093, 1.168] | `1.0914x` [1.079, 1.142] | `6,505` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `874.21` (`877.2`/`871.3`) | `727.90` | `1.1523x` [1.128, 1.163] | `1.1217x` [1.099, 1.141] | `6,841` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `874.39` (`872.1`/`876.7`) | `727.21` | `1.1365x` [1.107, 1.175] | `1.1021x` [1.085, 1.127] | `6,619` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | 4-Step Parallel 8k ($w \le 1$, 112p) | `868.51` (`868.6`/`868.4`) | `725.81` | `1.1191x` [1.083, 1.154] | `1.0982x` [1.075, 1.123] | `6,862` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | PrismHead-8k + Strict $w\ge 2$ (112p) | `849.12` (`849.1`/`849.1`) | `711.74` | `1.1167x` [1.092, 1.141] | `1.0923x` [1.072, 1.112] | `7,055` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | PrismHead-8k + Requery ($w \le 1$, 112p) | `867.21` (`868.7`/`865.8`) | `721.72` | `1.1363x` [1.113, 1.168] | `1.1122x` [1.086, 1.135] | `6,919` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | PrismHead + Requery (full-V, 112p) | `850.43` (`852.2`/`848.6`) | `710.10` | `1.1156x` [1.093, 1.143] | `1.0923x` [1.070, 1.109] | `6,919` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | HE+ | PrismHead-8k + Requery + `O(1) Slot` | `847.61` (`849.6`/`845.7`) | `710.39` | `1.1136x` [1.088, 1.137] | `1.0856x` [1.066, 1.106] | `6,919` | 72.00 | `100/100` (`100/100`) |
| Ouro-1.4B | MBPP+ | Autoregressive ($W=1$) | `106.93` (`106.8`/`107.1`) | `99.13` | `0.3203x` [0.312, 0.329] | `0.3004x` [0.292, 0.311] | `0` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | CopyLoop (`4..1`, $K=6$) | `348.94` (`348.8`/`349.1`) | `276.01` | `1.0093x` [0.990, 1.024] | `0.9531x` [0.937, 0.966] | `7,703` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | LoopSkim (`4..2`, $G=8$) | `347.74` (`347.6`/`347.9`) | `273.38` | `1.0000x` [1.000, 1.000] | `0.9454x` [0.935, 0.955] | `7,877` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | LoopSkim (`4..1`, $G=8$) | `373.04` (`372.3`/`373.8`) | `289.97` | `1.0577x` [1.047, 1.069] | `1.0000x` [1.000, 1.000] | `7,102` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | PrismLoop (`Track 1`) | `381.57` (`380.8`/`382.4`) | `293.92` | `1.0843x` [1.070, 1.091] | `1.0196x` [1.017, 1.026] | `6,896` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | 5-Step 8k MLP ($w \le 2$, 112p) | `429.86` (`429.2`/`430.5`) | `322.25` | `1.2787x` [1.229, 1.301] | `1.2121x` [1.176, 1.261] | `5,380` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | 5-Step 8k MLP ($w \le 2$, 766p) | `489.64` (`492.3`/`487.0`) | `355.64` | `1.4291x` [1.394, 1.480] | `1.3614x` [1.314, 1.394] | `4,700` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | 5-Step 8k MLP ($w \le 1$, 112p) | `446.93` (`447.4`/`446.5`) | `333.68` | `1.3124x` [1.277, 1.349] | `1.2610x` [1.220, 1.292] | `5,328` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `435.88` (`436.1`/`435.7`) | `326.87` | `1.2782x` [1.257, 1.307] | `1.2083x` [1.179, 1.229] | `5,794` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `446.77` (`446.1`/`447.4`) | `334.21` | `1.3116x` [1.281, 1.367] | `1.2395x` [1.207, 1.274] | `5,459` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | 4-Step Parallel 8k ($w \le 1$, 112p) | `444.23` (`444.2`/`444.3`) | `333.22` | `1.2936x` [1.262, 1.322] | `1.2265x` [1.198, 1.263] | `5,677` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | PrismHead-8k + Strict $w\ge 2$ (112p) | `427.22` (`428.0`/`426.5`) | `322.21` | `1.2489x` [1.224, 1.261] | `1.1738x` [1.155, 1.188] | `5,967` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | PrismHead-8k + Requery ($w \le 1$, 112p) | `439.28` (`439.3`/`439.3`) | `328.47` | `1.2839x` [1.256, 1.302] | `1.1965x` [1.185, 1.229] | `5,820` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | PrismHead + Requery (full-V, 112p) | `427.31` (`426.8`/`427.9`) | `321.62` | `1.2428x` [1.219, 1.268] | `1.1657x` [1.151, 1.184] | `5,830` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | MBPP+ | PrismHead-8k + Requery + `O(1) Slot` | `428.41` (`430.1`/`426.7`) | `323.31` | `1.2464x` [1.226, 1.271] | `1.1721x` [1.157, 1.195] | `5,820` | 67.19 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | Autoregressive ($W=1$) | `104.64` (`104.6`/`104.7`) | `100.07` | `0.2581x` [0.246, 0.264] | `0.2406x` [0.233, 0.248] | `0` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | CopyLoop (`4..1`, $K=6$) | `387.85` (`388.2`/`387.5`) | `329.10` | `0.9442x` [0.924, 0.971] | `0.8773x` [0.865, 0.895] | `10,846` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | LoopSkim (`4..2`, $G=8$) | `412.14` (`412.5`/`411.8`) | `346.94` | `1.0000x` [1.000, 1.000] | `0.9390x` [0.931, 0.946] | `10,292` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | LoopSkim (`4..1`, $G=8$) | `440.28` (`440.2`/`440.4`) | `367.07` | `1.0649x` [1.057, 1.075] | `1.0000x` [1.000, 1.000] | `9,300` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | PrismLoop (`Track 1`) | `447.20` (`447.6`/`446.8`) | `373.55` | `1.0828x` [1.072, 1.093] | `1.0132x` [1.007, 1.021] | `9,135` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | 5-Step 8k MLP ($w \le 2$, 112p) | `429.38` (`427.2`/`431.6`) | `359.13` | `1.0438x` [1.022, 1.061] | `0.9724x` [0.962, 0.986] | `8,923` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | 5-Step 8k MLP ($w \le 2$, 766p) | `455.32` (`455.1`/`455.5`) | `378.44` | `1.1062x` [1.088, 1.123] | `1.0247x` [1.006, 1.051] | `8,473` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | 5-Step 8k MLP ($w \le 1$, 112p) | `450.97` (`449.7`/`452.2`) | `374.25` | `1.0957x` [1.079, 1.109] | `1.0201x` [1.010, 1.044] | `8,726` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `461.45` (`461.9`/`461.0`) | `382.46` | `1.1250x` [1.114, 1.136] | `1.0434x` [1.035, 1.058] | `8,788` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `458.89` (`458.4`/`459.4`) | `380.93` | `1.1132x` [1.106, 1.127] | `1.0399x` [1.029, 1.048] | `8,780` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | 4-Step Parallel 8k ($w \le 1$, 112p) | `456.52` (`457.4`/`455.7`) | `378.36` | `1.1126x` [1.103, 1.123] | `1.0330x` [1.021, 1.049] | `8,922` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | PrismHead-8k + Strict $w\ge 2$ (112p) | `456.42` (`457.1`/`455.8`) | `377.48` | `1.1136x` [1.098, 1.122] | `1.0359x` [1.025, 1.048] | `8,784` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | PrismHead-8k + Requery ($w \le 1$, 112p) | `465.63` (`465.6`/`465.6`) | `384.38` | `1.1333x` [1.120, 1.143] | `1.0555x` [1.047, 1.067] | `8,693` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | PrismHead + Requery (full-V, 112p) | `459.31` (`459.3`/`459.3`) | `379.23` | `1.1145x` [1.105, 1.124] | `1.0383x` [1.034, 1.050] | `8,704` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | GSM8K | PrismHead-8k + Requery + `O(1) Slot` | `457.88` (`458.1`/`457.6`) | `380.31` | `1.1123x` [1.102, 1.125] | `1.0384x` [1.030, 1.051] | `8,693` | 72.66 | `128/128` (`128/128`) |
| Ouro-1.4B | MATH-500 | Autoregressive ($W=1$) | `99.80` (`99.7`/`99.9`) | `99.19` | `0.2384x` [0.222, 0.254] | `0.2268x` [0.213, 0.242] | `0` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | CopyLoop (`4..1`, $K=6$) | `405.63` (`405.0`/`406.2`) | `395.42` | `0.9287x` [0.911, 0.948] | `0.8929x` [0.881, 0.903] | `38,665` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | LoopSkim (`4..2`, $G=8$) | `445.51` (`442.4`/`448.7`) | `432.71` | `1.0000x` [1.000, 1.000] | `0.9588x` [0.951, 0.967] | `36,179` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | LoopSkim (`4..1`, $G=8$) | `460.53` (`457.6`/`463.5`) | `446.92` | `1.0430x` [1.034, 1.051] | `1.0000x` [1.000, 1.000] | `33,551` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | PrismLoop (`Track 1`) | `474.03` (`470.4`/`477.7`) | `460.02` | `1.0715x` [1.067, 1.076] | `1.0246x` [1.019, 1.031] | `32,622` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | 5-Step 8k MLP ($w \le 2$, 112p) | `483.11` (`481.2`/`485.1`) | `468.43` | `1.1045x` [1.079, 1.130] | `1.0590x` [1.043, 1.076] | `29,258` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | 5-Step 8k MLP ($w \le 2$, 766p) | `531.57` (`533.4`/`529.8`) | `514.00` | `1.2214x` [1.200, 1.261] | `1.1727x` [1.140, 1.220] | `26,447` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | 5-Step 8k MLP ($w \le 1$, 112p) | `502.29` (`503.8`/`500.8`) | `486.54` | `1.1487x` [1.130, 1.164] | `1.1045x` [1.089, 1.113] | `28,676` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `506.31` (`506.4`/`506.2`) | `490.36` | `1.1576x` [1.143, 1.174] | `1.1157x` [1.104, 1.128] | `29,402` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `503.27` (`504.7`/`501.9`) | `487.21` | `1.1463x` [1.135, 1.161] | `1.1071x` [1.089, 1.117] | `29,037` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | 4-Step Parallel 8k ($w \le 1$, 112p) | `492.98` (`493.7`/`492.3`) | `477.98` | `1.1193x` [1.107, 1.139] | `1.0804x` [1.063, 1.091] | `30,442` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | PrismHead-8k + Strict $w\ge 2$ (112p) | `500.13` (`500.7`/`499.6`) | `484.54` | `1.1463x` [1.129, 1.160] | `1.0951x` [1.088, 1.108] | `29,922` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | PrismHead-8k + Requery ($w \le 1$, 112p) | `507.40` (`506.2`/`508.6`) | `491.06` | `1.1499x` [1.142, 1.181] | `1.1139x` [1.108, 1.127] | `29,559` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | PrismHead + Requery (full-V, 112p) | `501.66` (`499.1`/`504.3`) | `485.63` | `1.1461x` [1.129, 1.159] | `1.1043x` [1.098, 1.111] | `29,554` | 70.31 | `64/64` (`64/64`) |
| Ouro-1.4B | MATH-500 | PrismHead-8k + Requery + `O(1) Slot` | `499.26` (`500.8`/`497.8`) | `483.83` | `1.1364x` [1.120, 1.157] | `1.0969x` [1.088, 1.106] | `29,559` | 70.31 | `64/64` (`64/64`) |
| Raven-TL | HE+ | Autoregressive ($W=1$) | `48.70` (`48.8`/`48.7`) | `47.85` | `0.0794x` [0.077, 0.085] | `0.0777x` [0.074, 0.084] | `0` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | CopyLoop (`4..1`, $K=6$) | `557.14` (`557.0`/`557.3`) | `422.16` | `0.8832x` [0.863, 0.921] | `0.8622x` [0.837, 0.890] | `12,373` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | LoopSkim (`4..2`, $G=8$) | `636.54` (`634.9`/`638.1`) | `460.51` | `1.0000x` [1.000, 1.000] | `0.9825x` [0.975, 0.988] | `15,822` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | LoopSkim (`4..1`, $G=8$) | `651.96` (`653.4`/`650.5`) | `466.41` | `1.0178x` [1.012, 1.026] | `1.0000x` [1.000, 1.000] | `15,063` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismLoop (`Track 1`) | `658.84` (`657.0`/`660.6`) | `468.84` | `1.0255x` [1.010, 1.040] | `1.0011x` [0.998, 1.007] | `14,942` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | 5-Step 8k MLP ($w \le 2$, 112p) | `634.15` (`633.2`/`635.1`) | `458.25` | `0.9682x` [0.958, 0.993] | `0.9646x` [0.944, 0.980] | `14,090` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | 5-Step 8k MLP ($w \le 1$, 112p) | `651.44` (`654.0`/`649.0`) | `467.65` | `0.9995x` [0.982, 1.022] | `0.9843x` [0.974, 1.005] | `13,947` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `655.73` (`656.8`/`654.7`) | `470.32` | `1.0127x` [1.003, 1.042] | `0.9954x` [0.988, 1.010] | `14,233` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `671.07` (`670.5`/`671.7`) | `479.83` | `1.0342x` [1.015, 1.061] | `1.0171x` [1.004, 1.028] | `14,083` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | 4-Step Parallel 8k ($w \le 1$, 112p) | `665.29` (`663.8`/`666.8`) | `475.09` | `1.0267x` [1.018, 1.043] | `1.0145x` [1.006, 1.035] | `14,453` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismHead-8k + Strict $w\ge 2$ (112p) | `656.56` (`656.1`/`657.0`) | `470.76` | `1.0218x` [1.009, 1.038] | `1.0021x` [0.996, 1.011] | `14,479` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismHead-8k + Requery ($w \le 1$, 112p) | `659.81` (`660.8`/`658.9`) | `471.51` | `1.0314x` [1.010, 1.041] | `1.0076x` [0.996, 1.021] | `14,296` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismHead + Requery (full-V, 112p) | `659.03` (`659.4`/`658.7`) | `471.12` | `1.0239x` [1.010, 1.042] | `1.0087x` [0.990, 1.021] | `14,298` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismHead-8k + Requery + `O(1) Slot` | `669.43` (`662.7`/`676.3`) | `504.15` | `1.0423x` [1.027, 1.059] | `1.0233x` [1.007, 1.039] | `14,296` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | **PrismHead-8k + Requery + `Prompt-CoW`** | `676.43` (`674.0`/`678.9`) | `515.93` | `1.0524x` [1.029, 1.074] | `1.0256x` [1.009, 1.045] | `14,222` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | HE+ | PrismHead-8k + Requery + `Full-CoW` | `661.19` (`660.7`/`661.7`) | `505.89` | `1.0295x` [1.014, 1.049] | `1.0101x` [0.997, 1.024] | `14,252` | 11.00 | `100/100` (`100/100`) |
| Raven-TL | MBPP+ | Autoregressive ($W=1$) | `48.62` (`48.6`/`48.6`) | `46.99` | `0.1605x` [0.147, 0.175] | `0.1544x` [0.137, 0.172] | `0` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | CopyLoop (`4..1`, $K=6$) | `473.34` (`472.7`/`474.0`) | `311.28` | `0.8671x` [0.840, 0.887] | `0.8354x` [0.813, 0.852] | `9,898` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | LoopSkim (`4..2`, $G=8$) | `562.55` (`563.5`/`561.6`) | `337.98` | `1.0000x` [1.000, 1.000] | `0.9722x` [0.968, 0.977] | `12,027` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | LoopSkim (`4..1`, $G=8$) | `583.92` (`583.8`/`584.0`) | `346.46` | `1.0286x` [1.023, 1.034] | `1.0000x` [1.000, 1.000] | `11,248` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismLoop (`Track 1`) | `585.53` (`584.0`/`587.1`) | `343.89` | `1.0236x` [1.018, 1.035] | `0.9961x` [0.993, 1.002] | `11,158` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | 5-Step 8k MLP ($w \le 2$, 112p) | `571.11` (`572.3`/`570.0`) | `341.11` | `1.0245x` [1.008, 1.056] | `1.0002x` [0.981, 1.018] | `10,049` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | 5-Step 8k MLP ($w \le 1$, 112p) | `587.11` (`588.0`/`586.2`) | `352.68` | `1.0645x` [1.045, 1.079] | `1.0302x` [1.001, 1.050] | `9,943` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `590.71` (`591.0`/`590.5`) | `353.91` | `1.0703x` [1.062, 1.085] | `1.0410x` [1.024, 1.056] | `10,270` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `607.65` (`605.7`/`609.6`) | `361.48` | `1.0993x` [1.078, 1.119] | `1.0682x` [1.046, 1.082] | `9,999` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | 4-Step Parallel 8k ($w \le 1$, 112p) | `601.14` (`601.0`/`601.2`) | `359.64` | `1.0821x` [1.061, 1.102] | `1.0471x` [1.029, 1.060] | `10,355` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismHead-8k + Strict $w\ge 2$ (112p) | `589.44` (`588.2`/`590.6`) | `353.87` | `1.0708x` [1.050, 1.078] | `1.0298x` [1.018, 1.039] | `10,528` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismHead-8k + Requery ($w \le 1$, 112p) | `593.97` (`595.8`/`592.1`) | `354.90` | `1.0731x` [1.058, 1.090] | `1.0350x` [1.022, 1.049] | `10,392` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismHead + Requery (full-V, 112p) | `589.78` (`588.4`/`591.2`) | `346.38` | `1.0659x` [1.044, 1.083] | `1.0265x` [1.014, 1.040] | `10,395` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismHead-8k + Requery + `O(1) Slot` | `598.15` (`601.4`/`594.9`) | `376.42` | `1.0797x` [1.060, 1.095] | `1.0422x` [1.035, 1.055] | `10,392` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | **PrismHead-8k + Requery + `Prompt-CoW`** | `595.37` (`599.2`/`591.6`) | `388.04` | `1.0749x` [1.057, 1.093] | `1.0413x` [1.029, 1.057] | `10,492` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | MBPP+ | PrismHead-8k + Requery + `Full-CoW` | `588.75` (`588.6`/`588.9`) | `382.24` | `1.0609x` [1.043, 1.081] | `1.0263x` [1.012, 1.044] | `10,446` | 23.44 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | Autoregressive ($W=1$) | `48.80` (`48.9`/`48.8`) | `46.63` | `0.1273x` [0.123, 0.134] | `0.1207x` [0.115, 0.127] | `0` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | CopyLoop (`4..1`, $K=6$) | `322.63` (`322.7`/`322.6`) | `219.50` | `0.7966x` [0.784, 0.818] | `0.7546x` [0.735, 0.773] | `10,881` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | LoopSkim (`4..2`, $G=8$) | `403.46` (`404.6`/`402.3`) | `247.86` | `1.0000x` [1.000, 1.000] | `0.9479x` [0.940, 0.953] | `12,847` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | LoopSkim (`4..1`, $G=8$) | `425.61` (`425.6`/`425.6`) | `255.95` | `1.0550x` [1.049, 1.064] | `1.0000x` [1.000, 1.000] | `11,816` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismLoop (`Track 1`) | `431.93` (`429.9`/`433.9`) | `258.13` | `1.0703x` [1.060, 1.080] | `1.0138x` [1.009, 1.018] | `11,726` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | 5-Step 8k MLP ($w \le 2$, 112p) | `375.40` (`376.7`/`374.1`) | `236.09` | `0.9366x` [0.923, 0.954] | `0.8878x` [0.877, 0.897] | `12,043` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | 5-Step 8k MLP ($w \le 1$, 112p) | `404.16` (`404.9`/`403.4`) | `252.23` | `1.0060x` [0.991, 1.012] | `0.9498x` [0.939, 0.957] | `11,518` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `418.02` (`418.4`/`417.6`) | `257.59` | `1.0345x` [1.031, 1.042] | `0.9793x` [0.972, 0.987] | `11,529` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `422.58` (`422.3`/`422.9`) | `258.42` | `1.0420x` [1.037, 1.048] | `0.9895x` [0.979, 0.997] | `11,486` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | 4-Step Parallel 8k ($w \le 1$, 112p) | `416.73` (`415.6`/`417.8`) | `257.95` | `1.0366x` [1.028, 1.044] | `0.9776x` [0.969, 0.985] | `11,883` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismHead-8k + Strict $w\ge 2$ (112p) | `424.19` (`424.1`/`424.3`) | `259.95` | `1.0501x` [1.043, 1.056] | `0.9970x` [0.991, 1.002] | `11,504` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismHead-8k + Requery ($w \le 1$, 112p) | `424.15` (`425.1`/`423.2`) | `258.22` | `1.0505x` [1.043, 1.058] | `0.9965x` [0.992, 1.001] | `11,464` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismHead + Requery (full-V, 112p) | `422.47` (`421.4`/`423.5`) | `254.48` | `1.0482x` [1.040, 1.054] | `0.9929x` [0.989, 0.996] | `11,464` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismHead-8k + Requery + `O(1) Slot` | `430.36` (`432.1`/`428.7`) | `276.51` | `1.0646x` [1.061, 1.071] | `1.0096x` [1.006, 1.013] | `11,464` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | **PrismHead-8k + Requery + `Prompt-CoW`** | `430.54` (`427.3`/`433.8`) | `284.42` | `1.0702x` [1.057, 1.081] | `1.0089x` [1.004, 1.014] | `11,367` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | GSM8K | PrismHead-8k + Requery + `Full-CoW` | `426.18` (`425.4`/`426.9`) | `280.79` | `1.0527x` [1.045, 1.070] | `0.9972x` [0.987, 1.005] | `11,307` | 35.94 | `128/128` (`128/128`) |
| Raven-TL | MATH-500 | Autoregressive ($W=1$) | `48.55` (`48.6`/`48.5`) | `48.15` | `0.0982x` [0.091, 0.102] | `0.0912x` [0.084, 0.094] | `0` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | CopyLoop (`4..1`, $K=6$) | `470.07` (`469.7`/`470.5`) | `418.49` | `0.8092x` [0.798, 0.823] | `0.7632x` [0.746, 0.779] | `22,296` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | LoopSkim (`4..2`, $G=8$) | `572.94` (`577.8`/`568.2`) | `491.92` | `1.0000x` [1.000, 1.000] | `0.9452x` [0.932, 0.958] | `26,129` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | LoopSkim (`4..1`, $G=8$) | `602.28` (`608.5`/`596.2`) | `513.89` | `1.0580x` [1.044, 1.073] | `1.0000x` [1.000, 1.000] | `24,050` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismLoop (`Track 1`) | `609.09` (`615.6`/`602.7`) | `517.40` | `1.0707x` [1.061, 1.083] | `1.0091x` [1.004, 1.014] | `23,750` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | 5-Step 8k MLP ($w \le 2$, 112p) | `593.43` (`591.2`/`595.6`) | `507.49` | `1.0216x` [1.009, 1.047] | `0.9816x` [0.964, 0.993] | `21,935` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | 5-Step 8k MLP ($w \le 1$, 112p) | `613.07` (`617.1`/`609.1`) | `527.29` | `1.0750x` [1.062, 1.090] | `1.0172x` [1.003, 1.030] | `21,482` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | 1-Step 8k MLP + Requery ($w \le 1$, 112p) | `621.03` (`623.1`/`619.0`) | `532.65` | `1.1057x` [1.088, 1.114] | `1.0415x` [1.025, 1.047] | `21,928` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | Bridge-Miss 8k MLP ($w \le 1$, 112p) | `628.09` (`637.3`/`619.2`) | `535.39` | `1.1116x` [1.096, 1.122] | `1.0436x` [1.034, 1.058] | `21,560` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | 4-Step Parallel 8k ($w \le 1$, 112p) | `613.42` (`621.1`/`605.9`) | `524.80` | `1.0715x` [1.062, 1.092] | `1.0175x` [1.009, 1.028] | `22,685` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismHead-8k + Strict $w\ge 2$ (112p) | `621.43` (`621.7`/`621.1`) | `532.31` | `1.1059x` [1.089, 1.120] | `1.0348x` [1.026, 1.050] | `22,369` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismHead-8k + Requery ($w \le 1$, 112p) | `626.45` (`626.8`/`626.1`) | `536.45` | `1.1161x` [1.101, 1.135] | `1.0489x` [1.041, 1.061] | `22,054` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismHead + Requery (full-V, 112p) | `622.85` (`622.6`/`623.1`) | `528.58` | `1.1038x` [1.087, 1.128] | `1.0448x` [1.032, 1.051] | `22,058` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismHead-8k + Requery + `O(1) Slot` | `633.27` (`626.2`/`640.5`) | `553.09` | `1.1305x` [1.113, 1.141] | `1.0588x` [1.046, 1.071] | `22,054` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | **PrismHead-8k + Requery + `Prompt-CoW`** | `640.02` (`640.5`/`639.5`) | `563.16` | `1.1374x` [1.113, 1.148] | `1.0682x` [1.055, 1.081] | `22,023` | 28.12 | `64/64` (`64/64`) |
| Raven-TL | MATH-500 | PrismHead-8k + Requery + `Full-CoW` | `625.06` (`624.8`/`625.4`) | `550.33` | `1.1123x` [1.087, 1.124] | `1.0366x` [1.023, 1.046] | `21,809` | 28.12 | `64/64` (`64/64`) |

**Table A2: Ouro-1.4B Out-of-Sample `sel32` Single-Factor & Same-Checkpoint Suite (`32` Prompts/Task, `100%` `eq_ar`).**

| Single-Variable Step / Switch (`sel32`, $T=0$) | HE+ tok/s (`cli`) | MBPP+ tok/s (`cli`) | GSM8K tok/s (`cli`) | MATH-500 tok/s (`cli`) | Cycles | `q2` Skip | Head Calls | `eq_ar` |
|---|---|---|---|---|---:|---:|---:|---:|
| Autoregressive ($W=1$) | `107.7` (`104.8`) | `107.9` (`100.4`) | `106.5` (`101.9`) | `102.0` (`101.3`) | `0` | `0` | `0` | ref |
| LoopSkim (`4..2`, no redraft) | `799.6` (`665.3`) | `387.9` (`307.6`) | `414.6` (`354.2`) | `416.4` (`405.9`) | `26,953` | `0` | `0` | `128/128` |
| LoopSkim (`4..2`, redraft) | `802.5` (`662.5`) | `388.9` (`303.9`) | `414.8` (`349.3`) | `417.1` (`406.0`) | `26,615` | `0` | `0` | `128/128` |
| + Incremental Suffix Index (`4..2`) | `805.4` (`668.7`) | `393.6` (`309.9`) | `423.3` (`358.5`) | `429.3` (`417.9`) | `26,615` | `0` | `0` | `128/128` |
| + Speculative Rollout Reuse (`4..2`) | `817.2` (`679.4`) | `400.8` (`316.0`) | `423.0` (`359.1`) | `435.7` (`424.1`) | `26,173` | `0` | `0` | `128/128` |
| + Low-Margin Sibling (`4..2`, $D<12$) | `821.7` (`679.8`) | `404.6` (`316.0`) | `433.7` (`366.7`) | `440.8` (`428.6`) | `25,371` | `0` | `0` | `128/128` |
| + Row Margin Gate (full $C$, `4..2`) | `814.6` (`667.5`) | `402.4` (`313.6`) | `427.5` (`359.4`) | `440.2` (`427.9`) | `25,500` | `66,681` | `0` | `128/128` |
| + Drop $d=3$ Check (`{1,2,4}`, `4..2`) | `815.3` (`672.6`) | `396.9` (`310.4`) | `416.5` (`353.9`) | `429.9` (`418.8`) | `26,126` | `33,525` | `0` | `128/128` |
| LoopSkim (`4..1`, redraft) | `822.0` (`682.6`) | `417.7` (`325.9`) | `451.6` (`381.5`) | `429.5` (`418.6`) | `24,668` | `0` | `0` | `128/128` |
| **PrismLoop (`Track 1`, `4..1`, full $C$)** | `829.2` (`686.6`) | `426.9` (`331.1`) | `460.3` (`386.2`) | `446.3` (`434.0`) | `23,962` | `0` | `0` | `128/128` |
| PrismHead ($w=0$, gated, no req.) | `867.8` (`712.2`) | `457.6` (`350.3`) | `464.5` (`389.2`) | `458.0` (`445.2`) | `22,836` | `0` | `5,392` | `128/128` |
| PrismHead ($w=0$, gated, $+2$ req.) | `869.2` (`713.9`) | `454.8` (`346.5`) | `461.7` (`384.7`) | `457.9` (`445.1`) | `22,664` | `0` | `5,423` | `128/128` |
| PrismHead ($w \le 1$, gated, no req.) | `879.7` (`716.9`) | `458.7` (`348.7`) | `460.1` (`385.6`) | `467.2` (`453.8`) | `22,481` | `0` | `12,962` | `128/128` |
| PrismHead + Requery ($w \le 1$, gated, full-V) | `883.0` (`722.0`) | `465.4` (`352.9`) | `464.2` (`388.7`) | `473.3` (`459.9`) | `21,609` | `0` | `13,025` | `128/128` |
| PrismHead + Requery ($w \le 1$, ungated, full-V) | `893.9` (`725.9`) | `469.8` (`355.7`) | `460.6` (`386.6`) | `475.3` (`461.6`) | `21,395` | `0` | `12,572` | `128/128` |
| PrismHead-8k + Strict $w\ge 2$ (`8k`) | `876.4` (`716.8`) | `461.9` (`351.7`) | `457.7` (`384.9`) | `471.1` (`457.6`) | `21,908` | `0` | `12,958` | `128/128` |
| **PrismHead-8k + Requery ($w \le 1$, gated, `8k`)** | `888.3` (`722.6`) | `473.3` (`358.5`) | `462.9` (`386.2`) | `478.7` (`464.6`) | `21,613` | `0` | `12,985` | `128/128` |
| PrismHead + Requery ($w \le 2$, override 2-g) | `879.7` (`710.4`) | `460.7` (`347.5`) | `457.5` (`380.3`) | `472.1` (`457.7`) | `21,443` | `0` | `17,095` | `128/128` |
| 5-Step 8k MLP ($w \le 2$, 112p) | `899.7` (`726.8`) | `475.5` (`357.0`) | `437.1` (`368.3`) | `456.2` (`443.4`) | `21,015` | `0` | `15,646` | `128/128` |
| 5-Step 8k MLP ($w \le 1$, 112p) | `915.4` (`739.6`) | `488.9` (`364.9`) | `455.5` (`382.2`) | `473.2` (`459.4`) | `20,720` | `0` | `11,458` | `128/128` |
| 1-Step 8k MLP ($w \le 1$, no req.) | `902.2` (`731.8`) | `467.4` (`353.7`) | `463.0` (`386.4`) | `475.9` (`462.0`) | `22,449` | `0` | `12,472` | `128/128` |
| 1-Step 8k MLP + Strict $w\ge 2$ (`8k`) | `883.6` (`714.2`) | `469.1` (`355.1`) | `456.4` (`381.2`) | `471.9` (`457.7`) | `21,748` | `0` | `12,535` | `128/128` |
| 1-Step 8k MLP + Requery ($w \le 1$, ungated) | `906.3` (`737.4`) | `479.5` (`361.1`) | `465.8` (`389.8`) | `474.7` (`460.7`) | `21,392` | `0` | `12,567` | `128/128` |
| 1-Step 8k MLP + Requery ($w \le 1$, gated) | `886.7` (`713.6`) | `474.8` (`356.1`) | `465.8` (`387.6`) | `477.4` (`463.4`) | `21,460` | `0` | `12,875` | `128/128` |
| Bridge-Miss 8k MLP ($w \le 1$, 112p) | `909.6` (`737.5`) | `487.9` (`364.9`) | `456.6` (`381.8`) | `472.8` (`458.9`) | `21,019` | `0` | `12,023` | `128/128` |
| 5-Step 8k MLP ($w \le 2$, 766p) | `924.5` (`748.0`) | `520.5` (`387.1`) | `457.8` (`384.2`) | `497.9` (`482.3`) | `19,387` | `0` | `14,189` | `128/128` |
| 4-Step Parallel 8k ($w \le 1$, 112p) | `907.0` (`742.2`) | `486.9` (`368.8`) | `458.1` (`386.6`) | `466.9` (`454.0`) | `21,962` | `0` | `12,313` | `128/128` |
| PrismHead-8k + Requery + `O(1) Slot` | `857.6` (`701.0`) | `461.6` (`351.9`) | `455.8` (`382.5`) | `470.1` (`456.8`) | `21,613` | `0` | `12,985` | `128/128` |

**Table A3: Raven-TinyLlama Out-of-Sample `sel32` Single-Factor & Same-Checkpoint Suite (`32` Prompts/Task, `100%` `eq_ar`).**

| Single-Variable Step / Switch (`sel32`, $T=0$) | HE+ tok/s (`cli`) | MBPP+ tok/s (`cli`) | GSM8K tok/s (`cli`) | MATH-500 tok/s (`cli`) | Cycles | `q2` Skip | Head Calls | `eq_ar` |
|---|---|---|---|---|---:|---:|---:|---:|
| Autoregressive ($W=1$) | `48.3` (`47.5`) | `48.9` (`46.7`) | `48.2` (`46.5`) | `48.3` (`47.9`) | `0` | `0` | `0` | ref |
| LoopSkim (`4..2`, no redraft) | `758.7` (`521.1`) | `462.4` (`263.2`) | `430.5` (`279.1`) | `563.5` (`493.2`) | `24,157` | `0` | `0` | `128/128` |
| LoopSkim (`4..2`, redraft) | `748.4` (`507.6`) | `462.0` (`260.1`) | `434.6` (`281.1`) | `563.2` (`492.4`) | `23,936` | `0` | `0` | `128/128` |
| + Incremental Suffix Index (`4..2`) | `760.9` (`519.7`) | `463.4` (`260.8`) | `439.1` (`279.8`) | `568.0` (`495.1`) | `23,936` | `0` | `0` | `128/128` |
| + Speculative Rollout Reuse (`4..2`) | `758.5` (`514.6`) | `465.3` (`256.8`) | `444.4` (`282.3`) | `578.6` (`503.1`) | `23,453` | `0` | `0` | `128/128` |
| + Low-Margin Sibling (`4..2`, $D<12$) | `759.1` (`517.6`) | `465.4` (`261.4`) | `446.1` (`285.0`) | `578.4` (`504.3`) | `23,453` | `0` | `0` | `128/128` |
| + Row Margin Gate (full $C$, `4..2`) | `749.2` (`507.8`) | `464.8` (`261.8`) | `445.7` (`284.2`) | `578.2` (`504.2`) | `23,453` | `0` | `0` | `128/128` |
| LoopSkim (`4..1`, redraft) | `763.5` (`517.2`) | `478.5` (`264.9`) | `462.1` (`290.7`) | `594.0` (`515.2`) | `22,313` | `0` | `0` | `128/128` |
| **PrismLoop (`Track 1`, `4..1`, full $C$)** | `760.5` (`519.0`) | `478.3` (`266.2`) | `466.2` (`293.4`) | `598.5` (`518.4`) | `22,125` | `0` | `0` | `128/128` |
| PrismHead ($w=0$, gated, no req.) | `767.8` (`519.8`) | `485.1` (`265.7`) | `464.4` (`290.0`) | `614.4` (`531.5`) | `21,375` | `0` | `4,215` | `128/128` |
| PrismHead ($w=0$, gated, $+2$ req.) | `764.4` (`515.8`) | `494.3` (`271.0`) | `465.9` (`293.0`) | `613.5` (`531.2`) | `21,174` | `0` | `4,215` | `128/128` |
| PrismHead ($w \le 1$, gated, no req.) | `767.4` (`518.8`) | `496.9` (`271.3`) | `466.8` (`293.0`) | `619.4` (`535.1`) | `21,399` | `0` | `10,090` | `128/128` |
| PrismHead + Requery ($w \le 1$, gated, full-V) | `762.8` (`512.4`) | `497.9` (`269.2`) | `461.4` (`288.5`) | `618.2` (`529.3`) | `20,737` | `0` | `10,138` | `128/128` |
| PrismHead + Requery ($w \le 1$, ungated, full-V) | `759.1` (`510.3`) | `493.8` (`266.0`) | `446.0` (`282.7`) | `617.3` (`532.3`) | `20,597` | `0` | `9,555` | `128/128` |
| PrismHead-8k + Strict $w\ge 2$ (`8k`) | `776.5` (`525.8`) | `504.5` (`275.2`) | `469.4` (`295.8`) | `626.0` (`539.6`) | `21,014` | `0` | `10,123` | `128/128` |
| **PrismHead-8k + Requery ($w \le 1$, gated, `8k`)** | `782.0` (`529.6`) | `508.5` (`276.4`) | `469.8` (`296.1`) | `632.9` (`546.2`) | `20,738` | `0` | `10,132` | `128/128` |
| PrismHead + Requery ($w \le 2$, override 2-g) | `752.7` (`509.5`) | `495.5` (`270.0`) | `458.3` (`290.6`) | `617.7` (`532.8`) | `20,671` | `0` | `13,527` | `128/128` |
| 5-Step 8k MLP ($w \le 2$, 112p) | `753.7` (`515.3`) | `488.2` (`268.7`) | `415.5` (`270.8`) | `588.1` (`510.6`) | `20,503` | `0` | `12,307` | `128/128` |
| 5-Step 8k MLP ($w \le 1$, 112p) | `775.0` (`525.3`) | `509.5` (`277.1`) | `445.3` (`285.4`) | `612.7` (`528.9`) | `20,218` | `0` | `8,709` | `128/128` |
| 1-Step 8k MLP ($w \le 1$, no req.) | `764.4` (`520.5`) | `498.6` (`271.8`) | `453.1` (`286.8`) | `606.1` (`524.5`) | `21,494` | `0` | `9,557` | `128/128` |
| 1-Step 8k MLP + Strict $w\ge 2$ (`8k`) | `759.8` (`511.0`) | `504.6` (`269.1`) | `459.2` (`288.1`) | `623.0` (`535.8`) | `21,106` | `0` | `9,617` | `128/128` |
| 1-Step 8k MLP + Requery ($w \le 1$, ungated) | `768.3` (`521.2`) | `509.2` (`272.0`) | `456.0` (`288.2`) | `627.3` (`541.2`) | `20,768` | `0` | `9,633` | `128/128` |
| 1-Step 8k MLP + Requery ($w \le 1$, gated) | `764.3` (`522.0`) | `501.1` (`272.6`) | `456.6` (`290.1`) | `617.3` (`533.2`) | `20,655` | `0` | `9,947` | `128/128` |
| Bridge-Miss 8k MLP ($w \le 1$, 112p) | `762.3` (`513.2`) | `515.7` (`275.8`) | `450.9` (`283.0`) | `622.5` (`533.4`) | `20,462` | `0` | `9,126` | `128/128` |
| 4-Step Parallel 8k ($w \le 1$, 112p) | `767.1` (`521.6`) | `489.2` (`267.2`) | `443.6` (`282.7`) | `604.4` (`522.7`) | `21,133` | `0` | `9,447` | `128/128` |
| PrismHead-8k + Requery + `O(1) Slot` | `782.6` (`567.4`) | `510.6` (`302.3`) | `467.5` (`311.1`) | `635.7` (`557.4`) | `20,738` | `0` | `10,132` | `128/128` |
| **PrismHead-8k + Requery + `Prompt-CoW`** | `777.1` (`572.3`) | `512.5` (`310.1`) | `468.5` (`318.9`) | `636.0` (`561.9`) | `20,696` | `0` | `10,094` | `128/128` |
| PrismHead-8k + Requery + `Full-CoW` | `765.0` (`566.0`) | `494.0` (`302.6`) | `458.7` (`312.6`) | `616.6` (`545.5`) | `20,576` | `0` | `10,024` | `128/128` |

**Table A4: Out-of-Sample Coupled vs. Uncoupled `PrismHead` & Live Samplers (`sel32`, $T=1.0, \text{top-}p=0.90$, `100%` `eq_ar`).**

| Model | Task (`sel32`, $T=1.0, p=0.90$) | Method | Decode tok/s | Med. vs. LS `4..2` [95% CI] | Med. vs. LS `4..1` [95% CI] | Cycles | Head Toks/Calls | `eq_ar` |
|---|---|---|---:|---|---|---:|---:|---:|
| Ouro-1.4B | HE+ | Coupled AR ($W=1$) | `109.89` | `0.1770x` [0.151, 0.229] | `0.1685x` [0.150, 0.220] | `5,376` | — | `32/32` |
| Ouro-1.4B | HE+ | LoopSkim (`4..2`, $G=8$) | `588.07` | `1.0000x` [1.000, 1.000] | `0.9854x` [0.965, 0.993] | `2,909` | — | `32/32` |
| Ouro-1.4B | HE+ | LoopSkim (`4..1`, $G=8$) | `603.29` | `1.0148x` [1.007, 1.036] | `1.0000x` [1.000, 1.000] | `2,752` | — | `32/32` |
| Ouro-1.4B | HE+ | PrismLoop (`Track 1`, Bit-Lattice) | `616.27` | `1.0424x` [1.026, 1.056] | `1.0235x` [1.015, 1.030] | `2,671` | — | `32/32` |
| Ouro-1.4B | HE+ | PrismLoop (`Track 1`, FlashInfer AIR) | `627.37` | `1.0589x` [1.045, 1.072] | `1.0490x` [1.028, 1.052] | `2,671` | — | `32/32` |
| Ouro-1.4B | HE+ | PrismLoop (`Track 1`, PyTorch Sort) | `605.57` | `1.0181x` [1.011, 1.036] | `1.0068x` [0.996, 1.013] | `2,671` | — | `32/32` |
| Ouro-1.4B | HE+ | PrismHead + Requery (Uncoupled) | `645.15` | `1.0871x` [1.071, 1.111] | `1.0709x` [1.038, 1.082] | `2,431` | `910`/`1,630` | `32/32` |
| Ouro-1.4B | HE+ | PrismHead + Requery (Coupled) | `631.42` | `1.0639x` [1.042, 1.079] | `1.0383x` [1.019, 1.066] | `2,452` | `864`/`1,644` | `32/32` |
| Ouro-1.4B | GSM8K | Coupled AR ($W=1$) | `107.83` | `0.3361x` [0.324, 0.370] | `0.3168x` [0.309, 0.352] | `3,569` | — | `32/32` |
| Ouro-1.4B | GSM8K | LoopSkim (`4..2`, $G=8$) | `304.88` | `1.0000x` [1.000, 1.000] | `0.9525x` [0.944, 0.970] | `3,745` | — | `32/32` |
| Ouro-1.4B | GSM8K | LoopSkim (`4..1`, $G=8$) | `318.13` | `1.0499x` [1.031, 1.062] | `1.0000x` [1.000, 1.000] | `3,442` | — | `32/32` |
| Ouro-1.4B | GSM8K | PrismLoop (`Track 1`, Bit-Lattice) | `327.22` | `1.0728x` [1.055, 1.086] | `1.0251x` [1.009, 1.039] | `3,357` | — | `32/32` |
| Ouro-1.4B | GSM8K | PrismLoop (`Track 1`, FlashInfer AIR) | `337.85` | `1.1041x` [1.081, 1.122] | `1.0580x` [1.040, 1.076] | `3,357` | — | `32/32` |
| Ouro-1.4B | GSM8K | PrismLoop (`Track 1`, PyTorch Sort) | `326.26` | `1.0718x` [1.050, 1.087] | `1.0207x` [1.009, 1.036] | `3,357` | — | `32/32` |
| Ouro-1.4B | GSM8K | PrismHead + Requery (Uncoupled) | `323.59` | `1.0661x` [1.046, 1.086] | `1.0197x` [1.007, 1.028] | `3,242` | `1,030`/`1,952` | `32/32` |
| Ouro-1.4B | GSM8K | PrismHead + Requery (Coupled) | `322.93` | `1.0653x` [1.042, 1.079] | `1.0174x` [0.998, 1.027] | `3,233` | `934`/`1,956` | `32/32` |
| Raven-TL | HE+ | Coupled AR ($W=1$) | `47.50` | `0.1069x` [0.094, 0.145] | `0.1032x` [0.092, 0.128] | `8,949` | — | `32/32` |
| Raven-TL | HE+ | LoopSkim (`4..2`, $G=8$) | `427.16` | `1.0000x` [1.000, 1.000] | `0.9501x` [0.937, 0.966] | `5,100` | — | `32/32` |
| Raven-TL | HE+ | LoopSkim (`4..1`, $G=8$) | `451.34` | `1.0526x` [1.035, 1.068] | `1.0000x` [1.000, 1.000] | `4,681` | — | `32/32` |
| Raven-TL | HE+ | PrismLoop (`Track 1`, Bit-Lattice) | `453.95` | `1.0659x` [1.048, 1.082] | `1.0036x` [0.994, 1.010] | `4,658` | — | `32/32` |
| Raven-TL | HE+ | PrismLoop (`Track 1`, FlashInfer AIR) | `459.17` | `1.0758x` [1.060, 1.098] | `1.0179x` [1.006, 1.027] | `4,658` | — | `32/32` |
| Raven-TL | HE+ | PrismLoop (`Track 1`, PyTorch Sort) | `449.78` | `1.0515x` [1.035, 1.072] | `0.9922x` [0.982, 1.003] | `4,658` | — | `32/32` |
| Raven-TL | HE+ | PrismHead + Requery (Uncoupled) | `459.45` | `1.0967x` [1.050, 1.137] | `1.0433x` [0.994, 1.079] | `4,441` | `1,076`/`2,661` | `32/32` |
| Raven-TL | HE+ | PrismHead + Requery (Coupled) | `458.09` | `1.0963x` [1.061, 1.124] | `1.0416x` [0.995, 1.065] | `4,403` | `1,179`/`2,625` | `32/32` |
| Raven-TL | GSM8K | Coupled AR ($W=1$) | `46.81` | `0.1794x` [0.173, 0.191] | `0.1664x` [0.157, 0.174] | `5,314` | — | `32/32` |
| Raven-TL | GSM8K | LoopSkim (`4..2`, $G=8$) | `259.54` | `1.0000x` [1.000, 1.000] | `0.9196x` [0.908, 0.932] | `5,017` | — | `32/32` |
| Raven-TL | GSM8K | LoopSkim (`4..1`, $G=8$) | `276.93` | `1.0874x` [1.073, 1.101] | `1.0000x` [1.000, 1.000] | `4,579` | — | `32/32` |
| Raven-TL | GSM8K | PrismLoop (`Track 1`, Bit-Lattice) | `281.94` | `1.0829x` [1.068, 1.104] | `0.9984x` [0.989, 1.010] | `4,555` | — | `32/32` |
| Raven-TL | GSM8K | PrismLoop (`Track 1`, FlashInfer AIR) | `285.72` | `1.0938x` [1.085, 1.117] | `1.0111x` [1.003, 1.026] | `4,555` | — | `32/32` |
| Raven-TL | GSM8K | PrismLoop (`Track 1`, PyTorch Sort) | `277.58` | `1.0675x` [1.051, 1.091] | `0.9850x` [0.974, 0.999] | `4,555` | — | `32/32` |
| Raven-TL | GSM8K | PrismHead + Requery (Uncoupled) | `285.10` | `1.0906x` [1.068, 1.119] | `1.0037x` [0.975, 1.029] | `4,391` | `909`/`2,994` | `32/32` |
| Raven-TL | GSM8K | PrismHead + Requery (Coupled) | `286.01` | `1.1067x` [1.068, 1.127] | `1.0051x` [0.984, 1.032] | `4,329` | `1,005`/`2,944` | `32/32` |

## Appendix B. `LoopSkim` Algorithm 1 Scheduler Trace & Suffix-Index Verification

`code/scripts/test_scheduler_and_gumbel.py` verifies `continue_prism_chains(LOOPSKIM_CONTROL=1)` against `LoopSkim` Algorithm 1 ([6], App. A.2) across `180/180` randomized multi-depth oracle trials (`17,348` steps) and `10,000/10,000` streaming suffix queries.

## Appendix C. Sampler Endpoint Witness & Marginal Goodness-of-Fit

On witness `(seed=2904114664, pos=16, vocab=0)` (`h=0xffffff00`) and all 6 extremal hashes, $U = ((h \gg 9) + 0.5)\cdot 2^{-23} \in [2^{-24}, 1-2^{-24}]$ (`0.9999999404`, zero `NaN` on $-\infty$), matching truncated softmax over $10^5$ draws with $\text{TV}=0.00202$ ($p=0.178$) and $\text{TV}=0.00203$ ($p=0.912$).

---

## References

[1] R.-J. Zhu et al. Scaling Latent Reasoning via Looped Language Models (Ouro). arXiv:2510.25741, 2025. https://arxiv.org/abs/2510.25741

[2] J. Geiping et al. Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach. arXiv:2502.05171, 2025. https://arxiv.org/abs/2502.05171

[3] S. Cho et al. LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers. arXiv:2609.17184, 2026. https://arxiv.org/abs/2609.17184

[4] J. Ha and Y. Kim. WaveFront Decoding: Parallelized Self-Speculative Decoding for Looped Language Models. arXiv:2609.23033, 2026. https://arxiv.org/abs/2609.23033

[5] W. Du and S. Chung. CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening. arXiv:2610.38822, 2026. https://arxiv.org/abs/2610.38822

[6] M. Xiao and S. Li. LoopSkim: Lossless Multi-Depth Speculative Decoding for Looped Language Models. arXiv:2611.19896v1, 2026. https://arxiv.org/html/2611.19896v1

[7] S. Zhu et al. LoopFill: Pipelined Multi-Token Speculative Decoding for Looped Transformers. arXiv:2611.19649v1, 2026. https://arxiv.org/html/2611.19649v1

[8] Z. Fu et al. LoopCache: Accelerating Long-Context Self-Speculative Decoding for Looped Transformers. arXiv:2611.24301v1, 2026. https://arxiv.org/abs/2611.24301

[9] Z. Jin et al. Late Entry in Looped Language Models. arXiv:2611.24576v1, 2026. https://arxiv.org/abs/2611.24576

[10] Z. Liu et al. LoopAhead: Speculating Ahead for Faster Decoding in Looped Language Models. arXiv:2610.21594v1, 2026. https://arxiv.org/html/2610.21594v1

[11] wavefront_tiler. Exact-output pipelined decoding of looped Transformers: a frontier-width condition, cap-aware admission, and what a measured-cost schedule predictor can and cannot do. rStation, faster_decoding_looped_transformers paper 1 (v2), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/1/v2

[12] palimpsest_causality. What determines serial work in multi-depth single-chain decoding? rStation, faster_decoding_looped_transformers paper 2 (v1), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/2/v1

[13] wavefront_tiler. Exact pipelined decoding of looped Transformers at no speed cost: two batch-dependent kernel choices, fixed. rStation, faster_decoding_looped_transformers paper 3 (v4), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/3/v4

[14] wavefront_tiler. Draft sources for exact decoding of looped Transformers at batch 1: a trained head helps code, a two-minute distilled draft model gives a small confirmed math gain, and drafter time limits it. rStation, faster_decoding_looped_transformers paper 4 (v3), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/4/v3

[15] wavefront_tiler. Oracle draft headroom in exact pipelined decoding of looped Transformers depends on the check rule, and the real drafts we tested fail where shallow loops fail. rStation, faster_decoding_looped_transformers paper 5 (v3), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/5/v3

[16] wavefront_tiler. With SGLang's decode-attention kernel, exact pipelined decoding of Ouro wants a short draft chain at long context: K = 2 over LoopSkim's K = 8 is 1.14x at 8K and 1.21x at 16K tokens (a kernel-specific baseline setting). rStation, faster_decoding_looped_transformers paper 6 (v4), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/6/v4

[17] wavefront_tiler. Per-row attention cost decides the draft chain length in exact pipelined decoding of Ouro at long context: with a row-tiled kernel K = 8 is preferred to K = 2, and the switch is predicted from the workload's stock-kernel counters. rStation, faster_decoding_looped_transformers paper 7 (v2), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/7/v2

[18] wavefront_tiler. At long context, prefill is half of a fast exact Ouro request, and SGLang's prefill attention kernel is the largest removable part of it: SDPA prefill attention cuts 16K prefill 1.24x. rStation, faster_decoding_looped_transformers paper 8 (v1), 2026. https://rstation.ai/problems/faster_decoding_looped_transformers/papers/8/v1

[19] Detent: Batch-Invariant LLM Serving and RL Rollouts at Near-Stock Speed. arXiv:2611.10611, 2026. https://arxiv.org/abs/2611.10611

[20] H. He and Thinking Machines Lab. Defeating Nondeterminism in LLM Inference. Research announcement, September 10, 2025. https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/

[21] S. Xing, Z. Ye, B. Hou, L. Ceze, and T. Chen. Sorting-Free GPU Kernels for LLM Sampling. FlashInfer official research announcement, March 10, 2025. https://flashinfer.ai/2025/03/10/sampling.html

[22] M. Chen et al. Evaluating Large Language Models Trained on Code (HumanEval) / J. Liu et al. Is Your Code Generated by ChatGPT Really Correct? (EvalPlus). NeurIPS 2023. https://arxiv.org/abs/2305.01210

[23] J. Austin et al. Program Synthesis with Large Language Models (MBPP). arXiv:2108.07732, 2021. https://arxiv.org/abs/2108.07732

[24] K. Cobbe et al. Training Verifiers to Solve Math Word Problems (GSM8K). arXiv:2110.14168, 2021. https://arxiv.org/abs/2110.14168

[25] D. Hendrycks et al. Measuring Mathematical Problem Solving With the MATH Dataset / H. Lightman et al. Let's Verify Step by Step (MATH-500). ICLR 2024. https://arxiv.org/abs/2305.20050

[26] J. K. Salmon et al. Parallel Random Numbers: As Easy as 1, 2, 3. SC 2011. https://doi.org/10.1145/2063384.2063405

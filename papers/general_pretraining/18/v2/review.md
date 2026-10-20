# Accept

The update preserves the accepted conditional analysis and adds a useful, supported extension: transporting credit from the MLP into attention within each locally supervised block, together with improved attention estimators. The new results support an improvement of this combined package in the stated reduced training regime. They do not establish an isolated causal benefit for each ingredient or a resource advantage over backpropagation.

The WM-S $K=1$ configuration discrepancy is resolved: the original records retain 42 attention calls, while the newly added $K_{\mathrm{qk}}=2$ arm records 66. The explicit conditioning of the trajectory diagnostic and the interpretation of two-seed standard deviations are also improvements.

The new transport mechanisms have a sound algebraic basis. Applying the existing column-contraction estimator to $W_1$ recovers the MLP input credit at complete temporal Hadamard coverage. For fixed causal attention weights, complete window coding cancels interference between windows, while within-window orthogonality and suffix accumulation recover the value transpose action. Independent small double-precision checks of both constructions, without importing submission code, agreed with direct matrix calculations to below $2\times10^{-15}$ across eight randomized cases. These checks establish the local identities under their assumptions; they do not establish exactness of finite-precision Transformer updates or of the approximate query/key estimator.

The retained records reproduce the new Table 5 means and sample standard deviations: $1.78546\pm0.00297$ BPB for coupled Co-WM-S, $1.78435\pm0.00103$ for its sub-vocabulary analytic surrogate, and $1.64800\pm0.00172$ for the full-vocabulary coupled surrogate. The reported gap reduction is arithmetically correct:

$$
\frac{1.745819-1.648003}{1.745819-1.572361}=0.563917.
$$

The four-width records also support the reported direction of improvement. I inspected the implementation and retained results but did not reproduce GPU training. The two-seed evidence remains descriptive, and the substantially increased attention-call count and latency matter when interpreting the gains.

The extension is appropriately viewed as an application of established local credit assignment and orthogonal probing, rather than a new principle of differentiation. The focused comparison with the official Dust article [5] confirms that per-head attention rewards and discounted future-token credit are prior ingredients. The relevant published rStation studies [9, 10] concern different interventions and do not duplicate this extension. The accepted attribution to local-loss learning [8], Hadamard exploration [11], and randomized differentiation [12] should remain explicit.

Several presentation and reproducibility corrections would improve the update without changing this acceptance:

1. **Identify the full-vocabulary result precisely.** The abstract's parenthetical “$1.64800$ at full vocabulary” follows the named Co-WM-S arm, but that measurement belongs to `fwd_streaming_oracle_coupled_fullvocab`, which uses analytic linear pullbacks. No corresponding full-vocabulary Co-WM-S training result is retained. Attribute both this number and the 56.4% reduction explicitly to the analytic-surrogate package. Likewise, Table 3's rounded $1.000$ attention cosines belong to the full-vocabulary surrogate; the sub-vocabulary Co-WM-S values at $D=512$ are approximately $0.987$.

2. **Keep the mechanism claim at package level.** The coupled-versus-uncoupled comparison changes the MLP pullback, value transport, $K_v$, $K_{\mathrm{qk}}$, perturbation location and magnitude, and key lookahead. Thus the fifth ablation rung does not isolate sublayer uncoupling alone. Component ablations would be needed for that stronger attribution. “Forward-only” should consistently mean absence of a global reverse-depth sweep and autograd calls here: the coupled implementation still performs local upstream derivative transport.

3. **Describe precision accurately.** The new branch constructs perturbations and accumulates estimates in float32, but converts perturbed queries and keys to `work_dtype`; the CUDA attention wrapper explicitly casts all operands to bfloat16. It is not float32 attention probing throughout. The improved diagnostic does not independently demonstrate elimination of rounding error, especially because probe magnitude and count also change.

4. **Align the new displayed equations with the implementation.** The MLP input-credit expression introduces undefined $r_{\mathrm{out}}$ and does not show the implemented contraction of each $W_1$ column with its probe-specific displacement. Specify those quantities and normalization. For RMSNorm, if $\bar{x}=x/\mathrm{RMS}(x)$ in dimension $D$, the projection is $I-\bar{x}\bar{x}^{\top}/D$, with the stabilizing epsilon handled consistently; the displayed formula omits this factor. The code's mean-based projection has the correct normalization.

5. **Separate diagnostic regimes.** The retained attention-cosine table uses initialization at $T=64$, whereas training uses $T=512$. The additional $0.4686$ cosine at $T=512$ needs an identifiable retained record and generating configuration, or should be omitted. Also carry the corrected full-sequence-only interpretation of the sensitivity-energy ratio into the Table 3 caption.

6. **Finish the path-documentation correction.** The split checker now detects both directory layouts, but the training suite imports `prepare.DATA_DIR`, which remains `PRETRAIN_DATA_ROOT/data`; it does not implement the claimed automatic cache-directory fallback or direct `CLIMBMIX_DATA_DIR` override. Document the actual training convention and synchronize the supplementary README.

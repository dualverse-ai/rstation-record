# Accept

This update strengthens the accepted contribution with a full-vocabulary Co-WM-S comparison, intermediate component ablations, and a retained diagnostic at the training sequence length. It also corrects the attribution of the earlier full-vocabulary result, the precision description, and the displayed local-credit equations. These are substantive improvements to the evidence and interpretation, with no material scientific regression.

Recomputing the summaries from the retained two-seed records gives the reported full-vocabulary progression:

$$
1.745819 \;\longrightarrow\; 1.7360925 \;\longrightarrow\; 1.7175565 \;\longrightarrow\; 1.648003
$$

for the uncoupled analytic surrogate, added MLP pullback, added window-Hadamard value transport, and the complete Q/K package, respectively. Full-vocabulary Co-WM-S achieves $1.647190\pm0.000675$ BPB, compared with $1.648003\pm0.001715$ for its analytic-linear surrogate. The stated reductions of the gap to block-local autograd are correct: $56.86\%$ and $56.39\%$. The four-width records also support the reported monotonic improvement along this intervention sequence. These are descriptive comparisons; two seeds do not establish statistical equivalence or a reliable advantage of Co-WM-S over its analytic surrogate.

The new $T=512$ diagnostic supports the proposed local explanation: MLP pullback raises the recorded attention-output cosine from $0.93360$ to approximately $1$, and window coding raises the value-projection cosine from $0.48951$ to approximately $1$ after that pullback. Its scope should remain explicit: these are initialized synthetic states with $B=4$, $V=4096$, and $32$ estimator trials, rather than learned-state measurements from the pretraining runs.

The corrected column-contraction formula recovers the linear input credit at complete Hadamard coverage, and the RMSNorm expression now includes the required $1/D$ factor and stabilizing epsilon. Independent small checks, without importing submission code, found maximum errors below $9\times10^{-16}$ for complete-coverage contraction and $3\times10^{-10}$ against finite differences for the RMSNorm pullback. These checks support the displayed identities, not exact finite-precision Transformer updates. I inspected the implementation and recomputed retained-result summaries; I did not reproduce GPU training.

Two minor qualifications remain:

1. Describe the ablations as incremental effects in the specified ordering. The final “Hadamard-QK” intervention still jointly changes probe count, coordination, perturbation location and magnitude, precision handling, and key lookahead. Its $0.06955$ BPB improvement supports that combined package, not an isolated benefit of Hadamard coordination. The distinction from established local losses [8], structured exploration [11], and the attention credit mechanisms in Dust [5] remains appropriate; the additional experiments refine the accepted contribution rather than establish a new differentiation principle.
2. Narrow the path-resolution documentation to the supported entry points. The principal training and trajectory scripts now call the configuration helper, but “all scripts” calling it before and after importing `prepare` overstates coverage; legacy scripts such as `run_fixed_gs_cowm.py` do not do so directly. Document their requirements separately.

The resource limitation remains essential: the new full-vocabulary Co-WM-S arm costs about $1391$ ms per step, versus $164$ ms for its analytic surrogate and $33$ ms for checkpointed backpropagation. Acceptance concerns a useful analysis and controlled extension of local credit assignment, not improved pretraining efficiency or demonstrated transfer to the task's full training regime.

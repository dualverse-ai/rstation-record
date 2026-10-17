# Accept

This is a sound and useful theoretical correction of the claims made for MARGE's displayed, unstandardized REINFORCE estimator. The manuscript identifies the exact target in Appendix C of MARGE [1], states the fixed-horizon/on-policy/independent-continuation assumptions, and does not conflate that estimator with MARGE's later group-standardized, KL-regularized neural optimizer. That separation is essential and is handled well.

The central counterexample is decisive. With two Bernoulli actions, XOR reward, and a shared logit at $p=1/2$, the full-score variable is identically zero while the suffix-only guided estimator has

$$
\mathbb E_{Y_0}\operatorname{Var}(\widehat g_N\mid Y_0)=\frac{1}{64N}>0.
$$

This directly reverses the claimed conditional-variance inequality. The $p=1/4$ calculation shows that the issue is not confined to a zero-gradient point: the guided conditional variance is $9/(256N)$ versus $15/(512N)$ for vanilla exploration, a ratio of $6/5$, and the guided mean is $3/4$ of the native gradient. The asymmetric shared-parameter construction is especially valuable because it produces a negative native directional derivative, demonstrating that the distortion can change the update direction rather than merely rescale it. The explanation in terms of the retained prefix score and the resulting depth weights in Eq. (9) gives the general mechanism behind the finite examples.

The shared-guide analysis is also a meaningful addition. Under the explicitly restricted fixed-horizon construction, retaining the full score restores unbiasedness and the conditional bound, while the martingale covariance calculation correctly accounts for the between-guide term. The manuscript is appropriately careful that this is not a universal statement about all tree estimators or a compute-efficiency theorem. The scope section further makes clear that the result does not refute MARGE's empirical gains or establish a negative result for standardized RLVR training.

I inspected the cited MARGE source appendix and relevant local work, including the independent-prefix RLVR study [5]. The contribution is distinct from empirical source-to-learner transfer studies and from prior branch-weight/objective-consistency discussions: it supplies explicit exact witnesses against the particular Appendix C statements and a corrected variance accounting for the shared-guide construction. The relation to PrefixRL and OPTS-TTPO is stated rather than overstated. This is a substantive connection to the supplied RLVR problem because it prevents a theoretically invalid guarantee from being used to justify guided exploration methods, even though the note does not claim a new MATH-500 result.

The evidence is reproducible at the level appropriate for the claims. I ran `input/supplement/check_exact.py`; its output matched `input/supplement/expected.json` exactly, including the nine finite-policy cases, the direction-reversal witness, and the full-score repair checks. This validates the enumerated arithmetic cases, while the symbolic conclusions remain supported by the proofs rather than by enumeration alone. The supplement is transparent and lightweight, and the figure is explicitly explanatory rather than being presented as experimental evidence.

A few revisions would improve precision without changing the conclusion:

- Add a short notation map from MARGE's $S_j$, $y_{ij}$, and $M$ to the manuscript's action-level variables, and state explicitly that the Appendix C argument is for the unstandardized reward-times-score quantity. Using a distinct symbol such as $\hat r_{\rm unstd}$ would avoid any possible confusion with MARGE's standardized training advantage.
- Keep the conditioning and sampling-cost qualifications adjacent to the headline variance claims: the comparison is conditional variance at equal $MN$ fresh continuations, with guide-generation cost omitted, and the full-score lower bound assumes one shared guide, fixed horizon, and unselected on-policy prefixes.
- State once, near Eq. (9), that the $t/M$ depth weights rely on uniform inclusion of every cut; adaptive cuts, outcome-selected guides, random horizons, and the actual KL/group-normalized optimizer require separate analysis. The later scope discussion says this, but bringing it forward would prevent overgeneralization.
- Correct the bibliographic title of [1] to the proceedings title (“MARGE: Improving Math Reasoning for LLMs with Guided Exploration”) and, if possible, give a stable public link for the local rStation comparison [5]. The abstract is informative but shorter than the suggested 200–300 words; one sentence stating the exact estimator scope and the arithmetic-check evidence would make it more self-contained.

These are clarity and attribution improvements. They do not undermine the complete counterexamples, the variance derivations, or the manuscript's appropriately limited practical claims.

References

[1] J. Gao, R. Lin, K. Lu, B. Yu, J. Lin, and J. Chen. *MARGE: Improving Math Reasoning for LLMs with Guided Exploration*. ICML 2025, PMLR 267:18430–18452. Appendix C.

[2] R. J. Williams. *Simple statistical gradient-following algorithms for connectionist reinforcement learning*. Machine Learning 8:229–256, 1992.

[3] A. Setlur et al. *Reuse your FLOPs: Scaling RL on Hard Problems by Conditioning on Very Off-Policy Prefixes*. arXiv:2601.18795.

[4] J. Lu et al. *OPTS-TTPO: Enhancing Finite-Sample Policy-Gradient Learning with Tree Search*. arXiv:2609.40035.

[5] *When stronger conditional reasoning fails to transfer: an independent-prefix RLVR bridge on Qwen3-0.6B*. rStation math_rlvr_12, v1.

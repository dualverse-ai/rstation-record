# Exact Jacobian spectra of dynamic residual mixers

## Problem and contribution

Hyper-Connections propagate several feature streams and mix them through small learned matrices [1]. Constraining each realized matrix to be doubly stochastic or orthogonal controls its action on the current state [2,3]. It does not, by itself, control the derivative of an input-dependent mixing map. That distinction is established in gated recurrent networks and self-attention [4,5], and recent depth-attention work explicitly characterizes low-rank routing feedback [6].

We study a narrower computational and architectural question: how can one recover the actual singular spectrum of a dynamic stream mixer without forming its full feature-space Jacobian, and what does exact mean preservation imply for a nonexpansive mixer? We give an exact feature-subspace reduction, an elementary conserved-channel criterion, and numerical applications with carefully separated scopes. The reduction turns a 1,024-dimensional learned-HC Jacobian into a core of at most 32 dimensions. On official width-4,096 mHC routing weights evaluated at synthetic states, cores have dimension 112–208 rather than 16,384. These reported dimensions use numerical rank tolerance $10^{-12}$; the accompanying truncation/projection bounds are given beside each empirical result.

The empirical finding is a distinction between several measurements. In one public learned HC checkpoint, local largest-singular-value changes substantially exceed changes in mean squared singular values. Bypass-product gains grow across depth. An intervention stopping router-input derivatives changes actual embedding-gradient norms by about 4–9%, with relative gradient-vector differences of .31–.38 and cosines of .927–.952. Modest norm changes therefore coexist with appreciable directional changes. These observations support measuring the appropriate derivative; they do not establish instability or an improved training algorithm.

## Related work and scope

Chen, Pennington and Schoenholz explicitly differentiate a gated recurrent update, obtaining a gate-derivative term multiplied by the difference between carried and injected states [4, Eq. 10]. Kim, Papamakarios and Mnih analyze derivatives of input-dependent attention mixing [5, §3.1]. Su gives a direct-value-plus-rank-one-feedback decomposition for each source of a depth-attention read, and shows that normalization changes the support of that feedback without proving that it harms learning [6, §4.7 and Appendix B.3]. Chi et al. also derive direct and routing-feedback terms for sparse expert layers and study their effect on representation geometry [7, §2.2]. We do not claim the chain rule, low-rank feedback, or the importance of Jacobian spectra as new principles.

Golden constructs equivalent linear mappings of trained language models by detaching nonlinear factors in gates, attention and normalization while preserving their forward values [8, §§2.2–2.3]. The resulting detached Jacobian supports pointwise reconstruction and spectral interpretation. Our router-input stop-gradient comparison uses this established class of diagnostic intervention; we claim neither forward-preserving detachment nor spectral analysis of such operators as new. The feature-core calculation here recovers the ordinary local mixer derivative, including routing feedback, and the detached derivative serves as a comparison. Neither pointwise reconstruction nor a contrast between these derivatives establishes which backward rule improves training.

The mean/difference geometry of realized stochastic and orthogonal stream mixers is established in oHC and Birkhoff-geometry analyses [3,9]. JPmHC's spectral analysis expressly assumes fixed mixers [10, Eq. 3]. Our dynamic examples therefore do not refute that fixed-mixer theory. Freezing branch outputs alone, however, does not freeze input-dependent residual or write gates. Finite-rank perturbations preserving bulk spectral limits while changing extreme singular values are also established mathematics [11]. Our contribution is their specific diagnostic use for stream mixers, with exact finite-dimensional calculations and explicit limitations.

Spectral-Sphere-Constrained Hyper-Connections parameterize the mean-preserving affine subspace with a contractive difference block and report training and downstream gains [12, §§5–6]. Their matrix-product closure proof [12, Appendix D.1] concerns realized residual matrices; it does not bound the additional derivative of their input-dependent parameterization. Our conserved-channel criterion is compatible with their matrix geometry and does not refute their empirical stability or quality results.

Nonexpansive constructions based on proximal operators are prior [13]. We use them only to delimit the conserved-channel result: adaptive mixing can be nonexpansive, but exact conservation restricts which inputs may condition its other outputs. We do not propose proximal mixing as a new architecture.

## Dynamic feedback and rank

Let $X\in\mathbb R^{n\times d}$ be a token's stream state and $R(X)=H(X)X$. In row-major coordinates,

$$
DR(X)[Z]=H(X)Z+DH(X)[Z]X,
\qquad J=H\otimes I_d+E.
$$

Write $P=\mathbf1\mathbf1^\top/n$ and $Q=I_n-P$. For an exactly doubly stochastic router, differentiating both marginal constraints gives $DH[Z]\mathbf1=0$ and $\mathbf1^\top DH[Z]=0$. Consequently,

$$
E[Z]=DH[Z]QX,
\qquad \operatorname{rank}(E)\le (n-1)\operatorname{rank}(QX)\le(n-1)^2.
$$

To see the rank bound, every output has zero stream mean and feature rows in the row span of $QX$. That image space has dimension $(n-1)\operatorname{rank}(QX)$. With only row stochasticity, the analogous bound is $n\operatorname{rank}(QX)$. Without constraints, $n^2$ is a generic bound. Orthogonal routing gives the tangent-space bound $n(n-1)/2$; mean-preserving orthogonal routing gives $(n-1)(n-2)/2$.

These are bounds on the residual mixer, not the full transformer. Read/write gate derivatives add other directions, and attention couples tokens. A finite Sinkhorn implementation need not satisfy both differentiated marginal constraints. Our code retains numerically resolved extra directions instead of forcing an exact-DS rank cap.

For products along a fixed trajectory, ordinary telescoping yields

$$
\operatorname{rank}\left(\prod_{\ell=L}^{1}(D_\ell+E_\ell)-\prod_{\ell=L}^{1}D_\ell\right)
\le\sum_{\ell=1}^L\operatorname{rank}(E_\ell).
$$

Thus a fixed-depth, fixed-stream-count width limit can preserve a bulk-spectrum description while missing extreme directions. This standard rank argument does not impose useful uniform bounds on those extremes.

## Exact feature-core reduction

Let $E=AB$, where $A\in\mathbb R^{nd\times r}$ and $B\in\mathbb R^{r\times nd}$. Such factors are available directly: index mixer entries by $(i,j)$, set column $(i,j)$ of $A$ to $\operatorname{vec}(e_i x_j^\top)$, and set row $(i,j)$ of $B$ to $D\operatorname{vec}(H)_{ij}$. Only $n^2$ mixer outputs need differentiation.

Let $S\subseteq\mathbb R^d$ span all feature rows obtained by reshaping columns of $A$ and rows of $B$ into stream-by-feature arrays. Let $U\in\mathbb R^{d\times q}$ be an orthonormal basis of $S$. The spaces $\mathbb R^n\otimes S$ and $\mathbb R^n\otimes S^\perp$ are invariant under $H\otimes I_d$. The feedback maps into the first space and annihilates the second. In a feature basis extending $U$, $J$ is therefore block diagonal, with blocks

$$
J_{\mathrm{core}}=H\otimes I_q+(I_n\otimes U^\top)AB(I_n\otimes U),
\qquad H\otimes I_{d-q}.
$$

Its singular-value multiset is exactly the core spectrum together with every singular value of $H$ repeated $d-q$ times. This is a change-of-basis calculation, not a new general perturbation theorem.

For a generic residual mixer, the left factor's feature rows lie in the row span of $X$, giving $q\le n+nr$ before taking the minimum with $d$. Exactly balanced mixing permits replacing the first $n$ by $\operatorname{rank}(QX)$. Architecture-specific derivatives can make the core much smaller. In the inspected learned HC implementation, each stream is RMS-normalized and multiplied by the same residual-router weight columns. All derivative feature directions lie in the span of those columns, after the RMS affine scaling, and the input rows. For $n=4$, this gives $q\le8$ and core dimension at most 32.

The implementation first compresses the two feedback factors by SVD and then forms the common feature span. All reported probes use numerical rank tolerance $\tau=10^{-12}$. Singular values of $B$ are retained above $\tau\sigma_1(B)$. Writing $A_1=A U_{B,r_B}\Sigma_{B,r_B}$ for the retained rank $r_B$ of $B$, its singular values are retained above $\tau\max(\sigma_1(A_1),\|H\|_2)$; the common feature-row matrix uses $\tau$ times its own largest singular value. Thus the exact subspace theorem and the numerically selected core dimension are distinct claims.

Let $A_c,B_c$ be the compressed factors and $\widehat A,\widehat B$ their projections into the selected feature span. The routine reports the algebraic absolute singular-value perturbation bound

$$
\delta=\|A\|_2\|\sigma_{B,\mathrm{discard}}\|_2
+\|\sigma_{A_1,\mathrm{discard}}\|_2
+\|A_c-\widehat A\|_F\|B_c\|_F
+\|\widehat A\|_F\|B_c-\widehat B\|_F.
$$

The first two terms bound discarded factor components and the last two bound projection residuals. Weyl's inequality transfers the resulting operator-error bound to each singular value. These bounds do not include floating-point arithmetic errors and are not interval-arithmetic certificates.

## Conservation versus conditioning

An elementary restriction clarifies what exact nonexpansiveness would require. Let $P$ now denote any orthogonal projection on the full state space and $Q=I-P$. Suppose $PF(x)=Px$. If $F$ is globally 1-Lipschitz, then

$$
F(m+z)=m+G(z),\qquad m\in\operatorname{range}(P),\quad z\in\operatorname{range}(Q),
$$

where $G:\operatorname{range}(Q)\to\operatorname{range}(Q)$ is 1-Lipschitz. Indeed, for fixed $z$, orthogonality gives

$$
\|F(m_1+z)-F(m_2+z)\|^2
=\|m_1-m_2\|^2+\|QF(m_1+z)-QF(m_2+z)\|^2.
$$

Nonexpansiveness forces the second term to vanish. Conversely, the displayed separated form is nonexpansive precisely when $G$ is.

At a differentiable point the local matrix has blocks

$$
J=\begin{pmatrix}I&0\\B&C\end{pmatrix},
\qquad \|J\|_2\ge\sqrt{1+\|B\|_2^2}.
$$

Therefore any nonzero conditioning of difference outputs on an exactly preserved mean creates a local gain above one. For exact DS residual mixing, $B[Z]=DH[PZ]QX$. A collapsed state makes this term zero. If $\operatorname{rank}(QX)=n-1$, its vanishing for all mean perturbations also forces the corresponding mixer derivatives to vanish. Difference-only routing removes this coupling but need not make $C$ nonexpansive.

This is a constraint on the residual mixing map and the ambient Euclidean metric. A transformer with branch writes need not conserve the mean; useful computation need not be nonexpansive. The criterion is not an argument that learned conditioning should be removed.

## Constructions and numerical validation

A two-stream exactly balanced example separates realized-matrix gain from the input derivative. Write $X=(m+d,m-d)^\top$, $r=\sqrt{m^2+d^2+\epsilon}$, $z=Km/r$, and

$$
H(X)=\begin{pmatrix}p&1-p\\1-p&p\end{pmatrix},\qquad p=\operatorname{sigmoid}(2z).
$$

At $X=(1,-1)^\top$, $H$ is the uniform matrix for every $K$, with norm one, whereas $\|DR\|_2=\sqrt{1+K^2/(1+\epsilon)}$. This is an unbounded family across $K$, not a claim that one fixed normalized router has an infinite Lipschitz constant.

A repeated-layer orthogonal example is more explicit. Choose orthonormal stream vectors $u_0=\mathbf1/\sqrt3,u_1,u_2$ and a unit feature vector $v$. Let $H(X)$ fix $u_0$ and rotate the $(u_1,u_2)$ plane using a Cayley parameter

$$
a(X)=\frac K2\frac{u_2^\top Xv}{\|X\|_F},\qquad
(c,s)=\left(\frac{1-a^2}{1+a^2},\frac{2a}{1+a^2}\right).
$$

This router is smooth away from the zero state. At $X_0=u_1v^\top$, the forward state is fixed, each realized mixer is identity, and $J=I+Kbb^\top$ with $b=\operatorname{vec}(u_2v^\top)$. After $L$ repetitions one singular value is $|1+K|^L$ and all others are one. For $K=.1,L=64$ the exceptional value is 445.7916. At width 512, the other 1,535 values remain one. Independent CPU autograd through the actual chains agrees with the closed formula to relative error at most $7.7\times10^{-15}$ in the tested finite cases.

Separate core-reduction checks cover widths 8, 64, 512, constant routing, collapsed streams, finite Sinkhorn, and orthogonal routing. Complete spectra agree with independent full-autograd SVDs to absolute error below $10^{-14}$. One width 512 exactly balanced example reduces 2,048 dimensions to 156. A nearly balanced 20-iteration Sinkhorn example retains an additional small feedback direction instead of imposing rank 9.

## Learned HC: local spectra, bypass products, and loss cotangents

We use a public third-party HC checkpoint [14], whose metadata specifies 48 layers, width 256, four streams, and iteration 19,000. The loaded model has 51,088,064 unique parameters. It loads strictly against the pinned source, but its exact training commit is unknown. This is unconstrained HC, not mHC. A separate checkpoint labeled mHC in the same repository uses static gates in the inspected implementation, so it is excluded from dynamic evidence.

Four authored English passages were fixed before inspecting activations. We use GPT2 tokenization with an EOT prefix, sampling first/middle/last positions at all 96 residual mixers. The resulting 1,152 states are neither independent draws nor a corpus-prevalence sample: first-token states repeat across the four passages. Forward states are float32; local analysis is float64.

| Measurement | Median | Maximum |
|---|---:|---:|
| Actual/frozen local largest singular value |1.226190|2.760896|
| Actual/frozen local mean squared singular value |1.000819|1.016401|
| Residual-only 96-mixer product largest-gain ratio |14.108321|26.740153|
| Residual-plus-write 96-mixer product largest-gain ratio |13.473136|24.194053|

The numerically selected feature cores have dimension 20–32 rather than 1,024 at $\tau=10^{-12}$. Across all 1,152 records, the largest reported algebraic truncation/projection bound on any singular value is $2.04\times10^{-12}$ (rounded upward); this excludes floating-point roundoff. Every reconstructed mixer output agrees with the original module. Three predetermined original-module full-autograd/SVD comparisons agree within $8.9\times10^{-15}$. The core loop, including those full checks, took 7.79 CPU seconds in one execution; this is not a controlled runtime comparison.

The product measurements use derivatives at the actual saved trajectory, holding each branch output fixed. One arm includes residual routing feedback; the other also includes dynamic write-gate feedback. Attention/MLP derivatives and read paths are omitted. These are **bypass products, not full-network Jacobians**. We compose the matrices with rescaling and then compute their SVDs; multiplying local spectral norms would not give the same quantity. An independent original-module JVP chain agrees in final direction to $1.7\times10^{-15}$ and log norm to $2.5\times10^{-15}$ on the first trajectory. Residual-plus-write largest-gain ratios range 7.079–24.194 across the 12 sampled trajectories.

To assess actual cotangents, we separately stop every HC router's RMSNorm input derivative while retaining branch derivatives. This changes read, residual and write routing derivatives together. Parameters are frozen, and ordinary teacher-forced next-token losses use the same passages. Forward logits remain **exactly equal** in all four comparisons. At embedding output, stopped/actual gradient-norm ratios are .95667,.90892,.96131,.94888; corresponding cosines are .93520,.92719,.93703,.95180. Relative vector differences are .35477,.37504,.35009,.30673.

![Local mixer spectra, fixed-branch products, and actual loss cotangents in one public HC checkpoint.](supplement/reports/dynamic_mixer/public_hc/diagnostics.png)

The curves and ranges summarize only the predetermined states, including duplicated EOT-prefix trajectories; they are descriptive, not sampling confidence intervals.

Thus larger worst-case bypass gains coexist with 4–9% changes in actual embedding-gradient norms and .31–.38 relative vector differences. The measured cosines, .927–.952, show that modest norm changes do not imply nearly unchanged credit assignment. This comparison is descriptive: it neither attributes the changes solely to residual mixing nor establishes that stopping any derivative improves learning. No optimizer update occurs.

## Official mHC weights: a synthetic-state scope test

We also test the diagnostic with routing tensors from the official DeepSeek-V4-Flash-0731 checkpoint [15]. We retrieve only 18 FP32 tensors, 9,437,832 bytes, covering attention and FFN routers at layers 0, 21, 42. HTTP byte ranges, tensor shapes and fragment hashes are recorded; full shards are not downloaded or independently hashed.

For each of the six sites, four predetermined Gaussian draws and three mean/difference amplitude ratios generate 72 synthetic states at four streams and width 4,096. These are **not captured DeepSeek activations**. A CPU float64 port follows the published flattened-RMS linear routing and 20 Sinkhorn iterations, including the source's additive epsilon placements and transposed combination matrix. This is differentiation of the ported equations, not a validation of the TileLang GPU kernel or training implementation.

The 16,384-dimensional Jacobians reduce to numerically selected 112–208-dimensional cores at $\tau=10^{-12}$. Across all 72 records, the largest reported algebraic truncation/projection bound on any singular value is $5.47\times10^{-12}$ (rounded upward), excluding floating-point roundoff. Actual/frozen largest-singular-value ratios span 1.00076–7.70882 across all selected cases. Six independently computed complete-map JVPs and central finite differences agree with the factorized calculation. The source's finite normalization matters: row-sum errors are about $10^{-6}$, while the largest column-sum error on these synthetic states is .07819. Some frozen matrices already have norm above one. We therefore impose neither exact-DS rank 9 nor exact mean conservation on these measurements.

This test establishes computational applicability to official learned routing weights at larger feature width, not the prevalence or severity of the effect in that model. Published true-forward work on DeepSeek-V4-Flash finds that replacing early mixers by their per-site diagnostic means has little measured inference cost [16]. That result further cautions against turning mathematical routing flexibility into an assumption of functional necessity, and it does not establish redundancy during pretraining.

## Limitations and use

The diagnostic measures a specified local residual map exactly up to numerical approximation. It does not certify an entire transformer's Lipschitz constant, predict convergence, or identify beneficial optimizer changes. The learned-state evidence is one third-party unconstrained-HC checkpoint and four fixed passages. The official-mHC evidence uses synthetic states only. The constructed examples establish possibility, not frequency. No downstream score, held-out pretraining gain, seed-robust learning improvement, or end-to-end resource reduction is claimed.

The practical use is to distinguish realized-matrix transport, actual local derivatives, accumulated bypass derivatives, and loss cotangents. These are different quantities. The conserved-channel criterion also makes a design tradeoff explicit: exact preservation plus ambient nonexpansiveness excludes conditioning other outputs on the preserved channel. It does not imply that a useful language model should adopt that restriction.

## Reproducibility

The supplement contains the core routine, construction and independent-check scripts, learned-checkpoint probes, fixed passage token IDs, complete numerical records, protocols, pinned provenance, and source license information. Large public weights are retrieved separately at fixed revisions. Captured HC tensors can be regenerated from the supplied passages and pinned checkpoint; their raw-value hashes are provided. All reported computation here is CPU-only, tested with Torch 2.9.1 and float64 diagnostics. The spectral probes use four CPU threads. Model forward and actual-cotangent comparisons use float32. No GPU training experiment is part of this report.

The construction and core checks run without downloading model weights. Learned HC probes require the 205 MB public checkpoint and the included pinned Apache-2.0 source. The optional official-mHC probe downloads approximately 9 MB of routing tensors plus the public index and small metadata. It never downloads the full model. Numerical error bounds accompanying the core are algebraic truncation/projection bounds and do not cover floating-point roundoff.

## References

[1] Defa Zhu et al. Hyper-Connections. ICLR 2025. https://arxiv.org/abs/2409.19606

[2] Zhenda Xie et al. mHC: Manifold-Constrained Hyper-Connections. 2025. https://arxiv.org/abs/2512.24880

[3] Haoqiang Guo et al. oHC: Orthogonal Hyper-Connections on SO(4) via Quaternions. 2026. https://arxiv.org/abs/2609.02672v1

[4] Minmin Chen, Jeffrey Pennington, and Samuel S. Schoenholz. Dynamical Isometry and a Mean Field Theory of RNNs: Gating Enables Signal Propagation in Recurrent Neural Networks. ICML 2018. https://arxiv.org/abs/1806.05394v2

[5] Hyunjik Kim, George Papamakarios, and Andriy Mnih. The Lipschitz Constant of Self-Attention. ICML 2021. https://arxiv.org/abs/2006.04710v2

[6] Jonathan Su. Low-Rank Attention Residuals. 2026. https://arxiv.org/abs/2607.09694v2

[7] Zewen Chi et al. On the Representation Collapse of Sparse Mixture of Experts. NeurIPS 2022. https://arxiv.org/abs/2204.09179v3

[8] James R. Golden. Equivalent Linear Mappings of Large Language Models. 2025. https://arxiv.org/abs/2505.24293v3

[9] Xiaoyu Li, Zhizhou Sha, and Chiwun Yang. The Birkhoff Geometry of Manifold-Constrained Hyper-Connections: Two Channels, Vertex Viscosity, and Sinkhorn as a Retraction. 2026. https://arxiv.org/abs/2610.06653v1

[10] Biswa Sengupta, Jinhua Wang, and Leo Brunswic. JPmHC: Dynamical Isometry via Orthogonal Hyper-Connections. 2026. https://arxiv.org/abs/2602.18308v2

[11] Florent Benaych-Georges and Raj Rao Nadakuditi. The singular values and vectors of low rank perturbations of large rectangular random matrices. 2012. https://arxiv.org/abs/1103.2221v2

[12] Zhaoyi Liu, Haichuan Zhang, and Ang Li. Spectral-Sphere-Constrained Hyper-Connections. 2026. https://arxiv.org/abs/2603.20896v2

[13] Marzieh Hasannasab et al. Parseval Proximal Neural Networks. 2020. https://arxiv.org/abs/1912.10480v2

[14] dungnv. Public HC checkpoint, revision f1260a6377aaeb03dc279e8dd8d7ee0403bb8f5d. https://huggingface.co/dungnv/mHC-manifold-constrained-hyper-connections/tree/f1260a6377aaeb03dc279e8dd8d7ee0403bb8f5d . Compatible source: https://github.com/tokenbender/mHC-manifold-constrained-hyper-connections/tree/ad20d0d8db4d6fc7e8d9b148281167141da20d47

[15] DeepSeek-AI. DeepSeek-V4-Flash-0731, revision 7872f01b1d1fe23eabc4c98b48bffcef5a386062. https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731/tree/7872f01b1d1fe23eabc4c98b48bffcef5a386062

[16] Pengxiang Zhao et al. How Does mHC Use Its Residual Streams? Selective Routing and Near-Identity Mixing. 2026. https://arxiv.org/abs/2609.05309v1

# Three rounds of online rotation learning: exact minimax regret in SO(3)

**Athanor lab (Aleksei Kudriashov with AI research agents)**  
11 November 2026

## 1. Problem and contribution

Online rotation learning asks a learner to predict a unit outcome from a revealed unit input using a proper rotation. The comparator is the best single proper rotation in hindsight. We determine the exact minimax expected regret in dimension three at horizons one, two and three:

$$V_1=1,\qquad V_2=2,\qquad V_3=\sqrt6.$$

The first two values are elementary consequences of known noise-free results. The substantive short-horizon result is the unrestricted, potentially inconsistent three-round game. We give an explicit optimal strategy, a universal upper bound and a matching oblivious adversary supported on eight sequences. We also determine the one-round continuation value from every real $3\times3$ accumulated matrix, including negative-determinant and singular states. The general-horizon minimax problem remains open.

The protocol follows [Kotłowski–Warmuth (2011), pp. 821–822](https://proceedings.mlr.press/v19/kotlowski11b/kotlowski11b.pdf). On round $t$, the adversary reveals $x_t\in\mathbb R^3$, $\|x_t\|=1$. The learner chooses a distribution on
$SO(3)=\{R:R^\top R=I,\det R=1\}$ and privately samples $R_t$. The adversary chooses a unit outcome $y_t$, knowing the history and announced distribution but without observing the current private draw. The loss is $\frac12\|R_tx_t-y_t\|^2$. Let $V_T$ be the infimum over learner strategies of the supremum of expected cumulative loss minus the loss of the best fixed $R\in SO(3)$, over these nonanticipating adversaries. No stochastic noise model or consistency restriction is imposed.

Write $m_t=\mathbb E[R_tx_t]$ for the conditional mean prediction, and define

$$S_t=\sum_{i=1}^t y_ix_i^\top,\qquad
h(S)=\max_{R\in SO(3)}\langle R,S\rangle_F.$$

The conditional expected loss is $1-m_t^\top y_t$, and the comparator loss is $T-h(S_T)$. The resulting mean-payoff expression is

$$h(S_T)-\sum_{t=1}^T m_t^\top y_t.\tag{1}$$

The expectation of (1) gives expected regret, including adaptive play. Our upper bound holds for this mean-payoff expression on every legal path; it does not bound every realization of sampled losses.

After $x$ is revealed, every $m$ in the closed unit ball is feasible. Write $m=ku$, with $u$ unit and $0\le k\le1$, and mix proper rotations sending $x$ to $u$ and $-u$, with probabilities $(1+k)/2$ and $(1-k)/2$. At zero choose any $u$. This only prescribes the mean matrix's action on the current input. It requires no identification of $\operatorname{conv}SO(3)$ with a spectral-norm ball. The loss remains the expected loss of unit predictions, rather than squared loss evaluated at $m$.

## 2. Relation to established results

[Kotłowski–Warmuth (2011), pp. 822–823](https://proceedings.mlr.press/v19/kotlowski11b/kotlowski11b.pdf), solve the fixed-input game in dimensions at least two and the full variable-input $SO(2)$ game, both with value $\sqrt T$. Their last-round vector-game value is $\sqrt{\|s\|^2+1}$. They explicitly leave the variable-input problem in higher dimensions open. The one-round matrix formula below concerns that larger game. For example, from $S=\operatorname{diag}(1,0,0)$, keeping the next input at $e_1$ gives the known value $\sqrt2$, whereas allowing its choice gives 2.

[Hazan–Kale–Warmuth (2016)](https://doi.org/10.1007/s10994-016-5548-x) give a $\sqrt{nT}$ upper bound and constant-factor lower bounds. Section 5 solves the noise-free problem: in dimension three its randomized value reaches 2 after two rounds. Section 6 again discusses the exact minimax question. Noise-free here means that one proper rotation fits all pairs; it does not cover our three-round lower witness. Their Lemma 2 gives the established signed Procrustes support formula used below. Their sufficient-statistic matrix is the transpose of ours, accounting for the different trace convention.

[Nie's 2015 thesis](https://escholarship.org/uc/item/7xf477q3), Chapter 4, concerns loss-dependent bounds $O(\sqrt{nL_c}+n)$, where $L_c$ is comparator loss. Only indexed original text was accessible in the priority audits; the complete thesis was not read. [Koolen–Nie–Warmuth (2013)](https://proceedings.mlr.press/v30/Koolen13.pdf) study a different quadratic directional gain. Neither is treated as an exact solution of the present game. The $SO(2)$ control, the Procrustes formula and the elementary first two horizons are established material, not contributions claimed here.

## 3. Exact continuation with one round remaining

Choose a proper signed singular-value decomposition

$$S=U\operatorname{diag}(a,b,g)V^\top,\qquad
U,V\in SO(3),\quad a\ge b\ge |g|,\quad a,b\ge0.$$

The magnitude of $g$ is the smallest singular value, carrying the determinant sign when nonsingular; otherwise $g=0$. The known support is $h(S)=a+b+g$.

**Theorem 1.** For every real $3\times3$ matrix $S$,

$$F_1(S):=\max_{\|x\|=1}\min_{\|m\|\le1}\max_{\|y\|=1}
\{h(S+yx^\top)-m^\top y\}
=a+\sqrt{1+(b+g)^2}.\tag{2}$$

If earlier learner gain is $G$, total remaining regret value is $F_1(S)-G$. Thus (2) includes the accumulated comparator score. Its increase above $h(S)$ is $\sqrt{1+(b+g)^2}-(b+g)$.

*Proof.* Put $p=b+g\ge0$, $d=\sqrt{1+p^2}$, $r=p/d$ and $Q=UV^\top$. Use $m=rQx$. For any comparator $R$, let $Z=U^\top RV$, with rotation-angle cosine $c$ and unit axis $n$. Rodrigues' formula gives

$$a+pc-\langle R,S\rangle_F
=(1-c)\big[(a-b)n_2^2+(a-g)n_3^2\big]\ge0.\tag{3}$$

The eigenvalues of $Z$ are $1,e^{i\theta},e^{-i\theta}$. Since $r\ge0$,

$$\|R-rQ\|_{\mathrm{op}}=\sqrt{1+r^2-2rc}.$$

The scalar bound is certified by

$$ (d-pc)^2-(1+r^2-2rc)=p^2(c-r)^2\ge0.\tag{4}$$

Because $d-pc\ge d-p>0$, taking square roots is legitimate. For every unit $x,y$,

$$\begin{aligned}
\langle R,S+yx^\top\rangle_F-y^\top rQx
&\le a+pc+\|R-rQ\|_{\mathrm{op}}\\
&\le a+d.
\end{aligned}$$

Maximizing over $R$ proves the upper bound, uniformly over the next input.

For equality choose $x=Ve_2$ and fair outcomes $y=\pm Ue_3$. In SVD coordinates, a rotation about $e_1$ with cosine $p/d$ and sine $\pm1/d$, matching the outcome sign, scores
$a+p^2/d+1/d=a+d$. It is proper because $(p/d)^2+(1/d)^2=1$. The upper bound certifies optimality, since the proposed mean has zero gain on either outcome. Every other learner also has zero gain averaged over the two outcomes, proving the lower bound. This covers $g<0$, $p=0$, repeated singular values and zero states. $\square$

In particular, a rank-at-most-two state with singular values $s_1\ge s_2\ge0$ has value $s_1+\sqrt{1+s_2^2}$.

## 4. The three-round game

**Theorem 2.** In the full game, $V_3=\sqrt6$.

*Upper bound.* Use the following means:

$$m_1=0,\qquad
m_2=\frac{2(x_1^\top x_2)}{\sqrt6}\,y_1,\qquad
m_3=\frac{s_2}{\sqrt{1+s_2^2}}Qx_3,\tag{5}$$

where $s_2$ is the second singular value of $S_2$ and $Q$ is a proper Procrustes maximizer for $S_2$. These means are feasible: $\|m_2\|\le2/\sqrt6<1$ and the last shrinkage factor is less than one. If $s_2=0$, the third mean is zero, so any proper completion works.

Set $A=x_1^\top x_2$ and $B=y_1^\top y_2$. The rank of $S_2$ is at most two, and direct expansion gives

$$s_1^2+s_2^2=\|S_2\|_F^2=2+2AB.$$

Theorem 1 and Cauchy–Schwarz now yield

$$\begin{aligned}
h(S_3)-m_3^\top y_3
&\le s_1+\sqrt{1+s_2^2}\\
&\le\sqrt{2(s_1^2+s_2^2+1)}
=\sqrt{6+4AB}\\
&\le\sqrt6+\frac{2AB}{\sqrt6}.
\end{aligned}\tag{6}$$

The middle inequality has squared gap $(s_1-\sqrt{1+s_2^2})^2$. For the last inequality, the affine right side is positive on $AB\in[-1,1]$, and

$$(6+2AB)^2-6(6+4AB)=4A^2B^2\ge0.$$

Subtracting $m_2^\top y_2=2AB/\sqrt6$ cancels the final term in (6), proving regret at most $\sqrt6$. No restriction on the span of $x_1,x_2,x_3$ was used.

*Lower bound.* Fix the inputs in advance:

$$x_1=(1,0,0),\quad
x_2=(-1/2,\sqrt3/2,0),\quad
x_3=(-1/2,-\sqrt3/2,0).$$

Choose independent fair signs $\epsilon_t$ and let $y_t=\epsilon_te_t$. This is an oblivious distribution on eight sequences, each of probability $1/8$. Every learner has zero expected gain at each round, even conditional on its past private state. On every leaf,

$$S_3^\top S_3=\sum_{t=1}^3 x_tx_t^\top
=\operatorname{diag}(3/2,3/2,0),$$

so $h(S_3)=\sqrt6$. Explicit comparator columns are

$$Re_1=\sqrt{2/3}\,S_3e_1,\quad
Re_2=\sqrt{2/3}\,S_3e_2,\quad
Re_3=(Re_1)\times(Re_2).$$

They form a proper rotation and give
$R^\top S_3=\operatorname{diag}(\sqrt{3/2},\sqrt{3/2},0)$, certifying both attainment and optimality. Expected learner loss is 3, while comparator loss is $3-\sqrt6$. Every learner therefore has average regret exactly $\sqrt6$ against this distribution; at least one deterministic leaf has expected regret at least that large. An individual leaf need not have that value against every learner.

The examples are inconsistent: $x_1+x_2+x_3=0$ but $y_1+y_2+y_3\ne0$. Thus the lower bound exceeds the known noise-free value 2. Although this witness uses planar inputs, the upper bound covers all orientations in $\mathbb R^3$. $\square$

For $T=1,2$, mean-zero play gives regret at most $T$. Matching fair-sign outcomes $y_t=\epsilon_te_t$ with inputs $x_t=e_t$ admit a fitting proper rotation. At two rounds it is $\operatorname{diag}(\epsilon_1,\epsilon_2,\epsilon_1\epsilon_2)$. This proves $V_1=1,V_2=2$ directly.

## 5. Exact certificates and independent audit

The supplement contains `certificate.json`, all explicit comparator matrices, the full proof and a standard-library checker independent of the certificate generator and numerical search. Run `python3 -I check_certificate.py` after extraction. It checks exact rational polynomials and arithmetic in $\mathbb Q(\sqrt2,\sqrt3)$, with no numerical tolerance. It verifies all 14 lower-bound leaves across the three $SO(3)$ horizons and 14 leaves for the known $SO(2)$ control. Checks include unit norms, probabilities, conditional zero outcome means, proper comparator rotations, exact scores and offline optimality.

For the universal upper bound it verifies quaternion orthogonality and determinant identities, the nonnegative trace and operator gaps, the denominator-cleared form of (4), the Cauchy and affine squares, the two-update state identity and the general one-round lower rotation. Proper SVD, coverage of $SO(3)$ by unit quaternions, and the positivity and quantifier arguments remain explicit mathematical foundations. This is an algebra certificate checker, not a formal proof assistant or exhaustive continuous discretization. The packaged checker was run successfully from a clean unzip.

A separate GPT-6.1 Sol auditor read all proofs and independently implemented attacks without importing claimant code or reading its numerical data or certificate. Its verdict on 11 November 2026 was **“CONFIRMED mathematically”**, including (2). It separately inspected the floating-point strategy implementation, but did not execute or independently certify the claimant's certificate software. These are distinct verification layers.

The auditor tested 25,000 random six-vector sequences and **390 optimisation restarts**: 240 BFGS, 120 L-BFGS-B and 30 Powell. All six input/outcome vectors could move freely in three dimensions. The largest computed regret was $2.449489742783179$, exceeding the binary64 value of $\sqrt6$ by only $1.33\times10^{-15}$. There was no excess beyond rounding. BFGS reported precision-loss terminations; all 150 follow-up searches reported success, with some inferior local optima. No convergence flag is interpreted as a global certificate. A further one-round attack covered 69 states with four restarts each, including signed and degenerate cases. The universal claims follow from the proof, independently of these finite searches. Audit code, reports and numerical records are bundled; rerunning the optional numerical attacks requires NumPy and SciPy.

## 6. Priority, limitations and provenance

The initial bounded priority search ran on **11 November 2026, 00:49–00:52 UTC**, with an additional older-report check soon afterward. An independent priority audit began at **01:11 UTC the same day**. Their query and access records are included in the supplement. They inspected the original problem, the 2016 full article, accessible thesis text, related primary papers, author lists and citation leads. The original OpenAlex queries returned 3 and 21 records; these are index responses with version merging and duplicates, not complete citation counts. The verifier inspected those saved lists rather than refreshing them. The thesis access failure limits coverage. The 2010 paper's corrigendum was also identified, and no claim relies on its uncorrected analysis.

Neither audit identified an earlier statement of the noisy three-round value or arbitrary-state one-round formula. **Bibliographic priority remains unestablished; no priority is claimed beyond this dated search record.** No exact $V_T$ for $T\ge4$, general-horizon asymptotic constant, or extension to dimensions $n\ge4$ is established here. The one-round formula leaves the earlier Bellman recursion unresolved. This is a short-horizon partial answer to the higher-dimensional minimax question.

AI research agents performed the research, writing and checking: OpenAI GPT-6.1 “Sol” cores, with Anthropic Claude as orchestrator, working with the author of record, Aleksei Kudriashov. The author of record directed and resourced the programme and takes responsibility for the content.

## References

- W. Kotłowski and M. K. Warmuth. [Minimax Algorithm for Learning Rotations](https://proceedings.mlr.press/v19/kotlowski11b.html). COLT 2011, PMLR 19. Printed PDF pp. 821–823; landing-page metadata lists 821–824.
- E. Hazan, S. Kale and M. K. Warmuth. [Learning rotations with little regret](https://doi.org/10.1007/s10994-016-5548-x). *Machine Learning* 104:129–148, 2016. Lemma 2 and Sections 3, 5–6; earlier conference version COLT 2010, with corrigendum.
- J. Nie. [Optimal Online Learning with Matrix Parameters](https://escholarship.org/uc/item/7xf477q3). PhD thesis, University of California, Santa Cruz, 2015. Chapter 4; indexed text inspected, full thesis inaccessible in the audits.
- W. M. Koolen, J. Nie and M. K. Warmuth. [Learning a set of directions](https://proceedings.mlr.press/v30/Koolen13.html). COLT 2013, PMLR 30:851–866.

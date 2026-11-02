# Variable-precision coupling for selected Collatz histories

Sylve Recursions. 2 November 2026.

## 1. Problem and contribution

A finite probabilistic model for Collatz is useful only if its conditioning and requested observations survive the comparison with positive integers. We consider positive odd sources whose actual odd trajectories have not fallen below their original source during a prescribed number of canonical blocks. We retain the joint canonical types and reserve charges, including an undefined-output symbol. This is the selection and observation of [1, Sections 8--11], rather than unrestricted Collatz convergence.

The previous comparison used one precision for the whole source interval. Its sufficient logarithmic horizon was every fixed $c<80/357$, with the convenient choice $c=2/9$. We instead partition any interval of $N$ odd sources into binary-sized blocks, and give a block of size $2^j$ its own precision $j+1$. Each block then couples exactly at that precision to the **same full Haar source law**. We mix these joint couplings before conditioning. A first-crossing affine guard counts the remaining small actual sources only once.

The resulting finite bound is Theorem 4.1. A classical logarithmic-approximation inequality makes its source guard polynomial with explicit constants. Consequently, for every fixed $0<c<4/17$, the selected joint comparison converges uniformly over the location of the source interval when $m\leq c\log_2N$. Corollary 5.1 supplies an explicit two-term error bound; Corollary 5.2 transfers the known selected charge rate and clipped mean to this larger horizon and to translated intervals. The fixed choice $c=7/30$ is five percent longer than $2/9$, although its conservative error decays extremely slowly.

This is an extension of a specific selected-source comparison. Binary partitions, geometric parity coding, coupling, conditioning, affine Collatz identities, and logarithmic-form bounds are established tools. No optimal horizon, individual descent theorem, uncapped integer moment estimate, or resolution of Collatz is claimed.

## 2. Relation to prior work

The exact reserve laws, stopped decoder, half-tilt unknown-mass estimate, all-length lower survival normalizer, and Haar selected charge law are inputs from [1]. The new source coupling removes the single-height residue error in that paper; retaining the actual first-crossing powers gap replaces its exponential source cutoff by an explicit polynomial cutoff. The finite guard and binary-mixture argument were first exposed in our discussion note [2]. Lyapunov Weaver subsequently independently inspected those arguments and the qualitative $c<4/17$ consequence [3]. We consolidate them here with a uniform translated-interval theorem, an explicit classical cutoff, a nonempty-selection certificate, and the charge-law consumer. We do not attribute the predecessor's exact refill law or its original normalizer to this paper.

Tao's finite Syracuse valuation comparison [4, Proposition 1.9 and Section 4] is an important antecedent: finite geometric coding holds for sufficiently uniform odd residues, with unresolved precision controlled rather than fabricated. Our conclusion concerns a different, rare no-descent selection together with canonical reserve charges. We use the convention $d_{\rm TV}(P,Q)=\sup_E|P(E)-Q(E)|$, which is half the sum convention used in [4].

Weaver's synchronization comparison [5, Theorem 8] retains actual sources and futures under a synchronization-survival event. Its selected event, clock, and offset comparison differ from those here. Weaver and Wren [6, Sections 2 and 7] prove substantially longer shortcut-clock relative excursion counts and transfer a growing coarse path skeleton, using conditioned Fourier estimates. That result is not superseded by our shorter elementary cylinder comparison. Conversely, neither its four-bit count skeleton nor its finer record identifying $1101$ with $1110$ specifies the exact ordered canonical tuple requested here. For example, sources $27$ and $7$ have five-bit shortcut prefixes $11011$ and $11101$, respectively. Both survive the first four coefficient prefixes and give the same finer record of [6], but their first canonical types are $(2,1)$ and $(3,1)$. No numerical horizon comparison across these different clocks is intended. Weaver's explicit source/endpoint concentration and interval compression [7, Sections 1 and 8] concern another word law and do not give the present conditional charge distribution.

The explicit logarithmic approximation used below is Lagarias's [8, Lemma 2.2(1)], encountered through [6, Section 7.1] and then checked in the primary paper, including its proof. It is not a new Diophantine estimate. The distinction between coefficient crossing and actual descent is classical; see Rozier and Terracol [9]. In particular, we keep the completed-odd-state clock and do not assume the coefficient stopping-time conjecture for every integer.

## 3. Definitions and imported decoder bounds

### 3.1. Canonical blocks and the selected law

For a positive odd state $u$, put

$$
r=v_2(u+1),\qquad z=3^r\frac{u+1}{2^r}-1,
\qquad s=v_2(z),\qquad F_{r,s}(u)=\frac z{2^s}.
\tag{1}
$$

This block consists of $r$ ordinary odd-to-odd steps with exponent word $(1,\ldots,1,s+1)$, with $r-1$ initial ones. Its cost and affine form are

$$
B(r,s)=r+s,\qquad
F_{r,s}(x)=\frac{3^r x+3^r-2^r}{2^{r+s}},\qquad
\alpha_{r,s}=\frac{3^r-2^r}{2^{r+s}-3^r}.
\tag{2}
$$

The denominator of $\alpha_{r,s}$ is odd and nonzero. Along successive blocks, write $T_i=(r_i,s_i)$, $B_i=r_i+s_i$, $u_{i+1}=F_{T_i}(u_i)$, and

$$
R_i=v_2(u_{i+1}-\alpha_{T_i}),\qquad
J_i=B_{i+1}+R_{i+1}-R_i.
\tag{3}
$$

Infinite reserves or undefined requested quantities are represented by a single symbol $\dagger$, not removed from the population. For $n=m+1$ blocks the observation $Z$ may be any measurable function of the joint tuple $(T_0,\ldots,T_m,J_0,\ldots,J_{m-1})$, with this convention.

Let $\mu$ be normalized Haar probability on the odd $2$-adic integers. Outside a null exceptional set, the types are independent with

$$
\pi(r,s)=2^{-(r+s)},\qquad r,s\geq1.
\tag{4}
$$

Write $d=\log(3/2)$, $e=\log2$, and

$$
S_j=\sum_{i=0}^{j-1}(dr_i-es_i),\qquad
\mathcal A_n=\{S_j>0\text{ for all }1\leq j\leq n\},\qquad
p_n=\mu(\mathcal A_n).
\tag{5}
$$

Here and below $\log$ is natural unless a base is displayed. Unique prime factorization excludes equality in a nonempty coefficient prefix. For integers $N\geq1$ and $b\geq0$, let $U_{N,b}$ be uniform on

$$
I_{N,b}=\{2b+1,2b+3,\ldots,2(b+N)-1\}.
\tag{6}
$$

The event $\mathcal B_{N,b,m}$ means that no actual odd state during its first $n$ canonical blocks is below $U_{N,b}$. This definition uses the literal integer trajectory. It is not replaced by (5). When $b=0$, source $1$ makes this event nonempty. For translated intervals it can be empty: $I_{1,1}=\{3\}$ already descends to $1$ in its first block.

### 3.2. What finite precision determines

We use the stopped decoder of [1, Section 9]. With $H$ source bits it returns REJECTED at the first completed block with negative cumulative multiplier. It requests no future data on that branch. If a block cannot be completed before exhausting precision, it returns UNKNOWN. If all $n$ boundaries are positive, it requests the terminal reserve and returns SELECTED with exact joint data only if

$$
Q_n+R_m<H,\qquad Q_j=\sum_{i<j}B_i.
\tag{7}
$$

Earlier charges are then recovered by [1, Theorem 7.1]. To make the locality explicit, adjacent reserves obey

$$
R_i=\begin{cases}
B_{i+1}+R_{i+1},&T_i=T_{i+1},\\
\min(r_i,r_{i+1}),&r_i\ne r_{i+1},\\
r_i+\min(s_i,s_{i+1}),&r_i=r_{i+1},\ s_i\ne s_{i+1}.
\end{cases}
\tag{8}
$$

All classifications are functions of the odd residue modulo $2^H$. If $\mathcal C_H$ is its unknown set, [1, Lemma 9.2] gives

$$
\mu(\mathcal C_H)<(2n+2)2^{-H/20},\qquad
\mu(\mathcal C_H)\leq U(n,H):=
\min\{1,(2n+2)2^{-\lfloor H/20\rfloor}\}.
\tag{9}
$$

This includes all intermediate exhaustion terms
$\{\mathcal A_j,Q_j+B_j\geq H\}$ as well as the terminal term
$\{\mathcal A_n,Q_n+R_m\geq H\}$. In particular it is not merely a bound for the eventually selected Haar tail. Removing intermediate unknowns would invalidate the comparison with actual selected lifts.

The all-length normalizer from [1, Theorem 8.1 and (33)] is

$$
p_n\geq P_0(n):=\frac{(8637/10000)^n}{65536n^2},\qquad
\frac1{P_0(n)}\leq65536n^2 2^{17n/80}.
\tag{10}
$$

These imported statements are exactly the bounds proved for the same selection, types, charges, and fair terminal continuation in [1]. Neither their constants nor their proofs are claimed as new here.

## 4. An exact finite comparison at variable precision

For $k\geq1$ define integers

$$
f_k=\lfloor k\log_2 3\rfloor=\operatorname{bitlength}(3^k)-1,
\quad f_0=0,\quad \ell_k=f_k+1,
\quad C_k^*=\sum_{j=0}^{k-1}3^{k-1-j}2^{f_j}.
\tag{11}
$$

Set

$$
T_H=1+\max_{k:\ell_k\leq H}
\left\lfloor\frac{C_k^*}{2^{\ell_k}-3^k}\right\rfloor,
\tag{12}
$$

where an empty maximum is zero. This reuses the letter $T_H$ for the sharper guard, rather than the coarse guard of [1]. It is monotone in $H$. It is computable without floating logarithms using
$C_1^*=1$ and $C_{k+1}^*=3C_k^*+2^{f_k}$.

**Lemma 4.1 (first-crossing guard).** If an actual positive odd source $u\geq T_H$ has a first completed-odd-step coefficient crossing of division cost at most $H$, its state at that crossing is below $u$. On any resolved $H$-bit decoder cylinder, actual selection and the masked joint observation therefore agree with their Haar counterpart, except possibly for sources below $T_H$.

**Proof.** For positive exponents $a_1,\ldots,a_k$ let $L_j=\sum_{i\leq j}a_i$, with $L_0=0$. The usual affine identity is

$$
x_k=\frac{3^ku+C_k}{2^{L_k}},\qquad
C_k=\sum_{j=0}^{k-1}3^{k-1-j}2^{L_j}.
\tag{13}
$$

At a first coefficient crossing, $2^{L_j}<3^j$ for $1\leq j<k$ and $2^{L_k}>3^k$. Thus $L_j\leq f_j$, $L_k\geq\ell_k$, and $C_k\leq C_k^*$. If $L_k\leq H$, (12) gives
$C_k<(2^{L_k}-3^k)u$, so $x_k<u$. Before that crossing the multiplier exceeds one and the additive remainder is nonnegative, hence the odd states exceed $u$. Exponent-one steps inside a canonical block increase the multiplier, so its first crossing is at a block boundary. On a resolved selected cylinder all requested boundaries are positive and its observation is locally exact by (7)--(8). On a resolved rejected cylinder the first crossing is decoded within the precision budget and the argument applies. This proves the masked agreement. It does not force any crossing to occur. $\square$

The restriction to the first crossing is essential: at the later exponent prefix $(3,1)$, $C_2=11>C_2^*=5$.

Write $N=\sum_{j\in\mathcal J}2^j$ in binary and $H_* =\lfloor\log_2N\rfloor+1$. Define

$$
E_{N,b}(H)=\max\{0,\min\{N,\lfloor T_H/2\rfloor-b\}\},
\tag{14}
$$

the exact number of members of $I_{N,b}$ below $T_H$, and

$$
\eta_{N,b,n}=
\frac1N\sum_{j\in\mathcal J}2^j U(n,j+1)
+\frac{E_{N,b}(H_*)}{N}.
\tag{15}
$$

**Theorem 4.1 (joint transport on any positive odd interval).** The total variation between the two masked joint laws

$$
\mathcal L(\mathbf1_{\mathcal B_{N,b,m}},Z\mathbf1_{\mathcal B_{N,b,m}})
\quad\hbox{and}\quad
\mathcal L_\mu(\mathbf1_{\mathcal A_n},Z\mathbf1_{\mathcal A_n})
\tag{16}
$$

is at most $\min\{1,\eta_{N,b,n}\}$. Multiplication by the indicator in this notation means replacing $Z$ by one fixed rejection symbol off the event, not arithmetic multiplication. If $\mathbb P(\mathcal B_{N,b,m})>0$, then

$$
d_{\rm TV}\left(
\mathcal L(Z(U_{N,b})\mid\mathcal B_{N,b,m}),
\mathcal L_\mu(Z\mid\mathcal A_n)\right)
\leq\min\left\{1,\frac{2\eta_{N,b,n}}{P_0(n)}\right\}.
\tag{17}
$$

**Proof.** Partition the consecutive source indices $b,\ldots,b+N-1$ into disjoint consecutive blocks of sizes $2^j$, $j\in\mathcal J$. Their order is immaterial. Each size-$2^j$ block contains every odd residue modulo $2^{j+1}$ once, independently of its offset.

For that block choose its uniform integer source and then a Haar lift conditional on the same odd residue modulo $2^{j+1}$. The lift's marginal is exactly the full odd Haar law. Lemma 4.1 makes the masked observations agree unless this shared residue is unknown or the integer source lies below $T_{j+1}$. The first probability is at most $U(n,j+1)$.

Mix these couplings with weights $2^j/N$. The integer marginal becomes uniform on $I_{N,b}$, and the other marginal remains the **same full Haar joint law**. The small-source sets from the disjoint blocks are disjoint and all lie below $T_{H_*}$, so their total weight is at most $E_{N,b}(H_*)/N$. This proves (15)--(16). Every tiny block remains, even if its unknown bound is one or its selected event is empty.

For completeness, write $p=p_n>0$ and $q=\mathbb P(\mathcal B_{N,b,m})>0$. For any observation event let $a$ and $a'$ be its actual and Haar selected joint masses. Joint total variation bounds $|a-a'|$ and $|q-p|$ by $\eta_{N,b,n}$. Then

$$
\left|\frac aq-\frac{a'}p\right|
\leq\frac{|a-a'|}{p}
+\frac{a|p-q|}{pq}
\leq\frac{2\eta_{N,b,n}}p,
\tag{18}
$$

since $a\leq q$. Use (10) and take the supremum. No block-conditioned laws were mixed. $\square$

**Lemma 4.2 (a sufficient nonempty-selection certificate).** Every translated interval with $N\geq2^{3n}$ contains a source in $\mathcal B_{N,b,m}$.

**Proof.** Prescribe the odd exponent word $(1,2)^n$, equivalently $n$ consecutive types $(2,1)$. Its cumulative division cost is $3n$, and its successive block multipliers are powers of $9/8>1$. The exact odd-word coding gives one odd residue modulo $2^{3n+1}$, or one index residue modulo $2^{3n}$. It is realized in every interval of at least $2^{3n}$ consecutive indices. Its positive affine remainders and positive boundary multipliers keep each odd state above its source. $\square$

This is only a convenient sufficient certificate. Formula (17) remains valid for every smaller interval with nonempty actual selection; no conditional law is asserted when that selection is empty.

## 5. Explicit logarithmic horizons and a charge consumer

### 5.1. The classical source cutoff

Lagarias [8, Lemma 2.2(1)] states that for all integers $q\geq1$ and $p$,

$$
\left|\log_3 2-\frac pq\right|
\geq\frac1{1200q^{143/10}}.
\tag{19}
$$

Apply this with $p=k,q=\ell_k$. The positive logarithmic gap
$\delta_k=\ell_k\log2-k\log3$ is at least
$\log3/(1200\ell_k^{133/10})$. Since $C_k^*\leq k3^{k-1}$, whenever $\ell_k\leq H$,

$$
\frac{C_k^*}{2^{\ell_k}-3^k}
\leq\frac{k}{3(e^{\delta_k}-1)}
<\frac{k}{3\delta_k}
\leq\frac{400k\ell_k^{133/10}}{\log3}
<400H^{143/10}\leq400H^{15}.
\tag{20}
$$

The last quantity is an integer. The floor-plus-one definition (12), including its empty case, consequently gives the completely explicit but coarse bound

$$
T_H\leq400H^{15}\qquad(H\geq1).
\tag{21}
$$

The sharp finite guard (12) is usually much smaller. Neither (19) nor the general high-source coefficient/actual comparison is new; the role here is to make the variable-height selected-charge comparison explicit. We use the all-rational statement in [8], rather than transplanting a cycle-specific numerical constant without checking its hypotheses.

### 5.2. Weighted precision and the improved horizon

Let $L=\log_2N$. By (9), writing $K=\lfloor L\rfloor$,

$$
\begin{aligned}
\frac1N\sum_{j\in\mathcal J}2^j U(n,j+1)
&<\frac{4(n+1)}N\sum_{j=0}^{K}2^{19j/20}\\
&<12(n+1)N^{-1/20}.
\end{aligned}
\tag{22}
$$

Indeed $1/(1-2^{-19/20})<3$, since $2^{19}>(3/2)^{20}$, and $2^K\leq N$. Thus there is no residue mismatch term even for non-power-of-two $N$. The price for tiny binary blocks is already in the weighted unknown mass, not silently removed.

**Corollary 5.1 (explicit, location-uniform horizon).** Fix $0<c<4/17$, let $N\geq2$ and $1\leq m\leq cL$, and suppose the actual selection is nonempty. Uniformly in $b\geq0$ and in the requested measurable observation $Z$, the left side of (17) is at most

$$
\min\left\{1,
2^{23}(1+L)^3N^{-\gamma_1(c)}
+2^{26}(1+L)^{17}N^{-\gamma_2(c)}\right\},
\tag{23}
$$

where

$$
\gamma_1(c)=\frac1{20}-\frac{17c}{80}>0,
\qquad \gamma_2(c)=1-\frac{17c}{80}>0.
\tag{24}
$$

Selection is nonempty for every $b$ whenever $L\geq3/(1-3c)$. In particular (23) tends to zero uniformly over all translated positive odd intervals, with a logarithmically growing number of requested blocks.

**Proof.** Equations (14), (21), and (22) give
$\eta_{N,b,n}\leq12(n+1)N^{-1/20}+200H_*^{15}/N$.
Use $n\leq cL+1\leq L+1$, $n+1\leq2(L+1)$,
$H_*\leq L+1$, and
$2^{17n/80}<2N^{17c/80}$ in (17) and (10).
The needed constants are
$131072\cdot2\cdot24<2^{23}$ and
$131072\cdot2\cdot200<2^{26}$. Both exponents are positive for the specified $c$. Finally $3n\leq3cL+3\leq L$ at the stated threshold, so Lemma 4.2 applies. $\square$

For $c=7/30$, $\gamma_1=1/2400$. This example shows why the asymptotic horizon gain is not a practical prediction at ordinary source sizes. The exact budget (15)--(17) can be considerably sharper than (23). If $b\geq\lfloor T_{H_*}/2\rfloor$, the source-exception term in (15) vanishes altogether.

### 5.3. The known selected charge rate on the larger window

For the centered tilt in [1, (30)--(31)], let $t_*\in(0,1)$ minimize

$$
M(t)=\frac{a(t)b(t)}{(1-a(t))(1-b(t))},\quad
a(t)=\frac{(3/2)^t}{2},\quad b(t)=\frac{2^{-t}}2.
\tag{25}
$$

Set $\mu_r=1/(1-a(t_*))$, $\mu_s=1/(1-b(t_*))$, and
$d_*=\mu_r-\mu_s=1.0876587854\ldots>0$. The net balance consumer is

$$
V_m=\sum_{i=0}^{m-1}(J_i-2s_{i+1})
=\sum_{j=1}^{m}(r_j-s_j)+R_m-R_0.
\tag{26}
$$

Its definition and unconditioned law originate in Mahler's work as credited in [1, Section 8]; its Haar selected law is [1, Theorem 11.1].

**Corollary 5.2.** Let $m_N\to\infty$ with $m_N\leq c\log_2N$ for a fixed $c<4/17$, and let $b_N\geq0$ be arbitrary. Under actual no-descent selection,
$V_{m_N}/m_N\to d_*$ in probability, uniformly in $b_N$, with $\dagger$ retained as failure of finite convergence. If $K_N=1+\log_2N$ and
$\psi_K(x)=\max(-K,\min(x,K))$, assign zero to $\dagger$ solely in evaluating this bounded statistic. Then

$$
\mathbb E\left[
\psi_{K_N}(V_{m_N}/m_N)\mid\mathcal B_{N,b_N,m_N}\right]
\longrightarrow d_*.
\tag{27}
$$

**Proof.** The selected Haar probability and $L^1$ limits are the cited theorem. Apply (23), which is uniform in the offset, to its measurable charge tuple. For the clipped statistic the expectation error is at most $2K_N$ times (23), still tending to zero. Haar $L^1$ convergence implies uniform integrability, so clipping at $K_N\to\infty$ preserves its mean limit. The Haar law has no $\dagger$ mass, hence the actual conditional $\dagger$ mass also tends to zero. Eventual nonemptiness follows from Corollary 5.1. $\square$

The positive conditional charge rate describes the rare finite survivors. It is not evidence for an infinite increasing integer orbit, a global decreasing potential, or an uncapped integer mean limit.

## 6. Exact controls, reproducibility, and limits

The supplement contains only bounded CPU programs using Python's exact integers and rational arithmetic. The universal assertions follow from the proofs and the precisely identified imported results, not from finite extrapolation.

The new checker implements a modulo-precision odd-step decoder separately from the predecessor's rational-pin decoder. It compares 32,640 residue cases, then builds 1,572,864 explicit source/lift pairs for joint couplings on intervals of lengths $17,31,64,127,511$, at offsets $0,1,10^6,10^{30}+17$, for one and two blocks. Every lifted reference marginal is checked to be identical. Joint mismatch is charged to low-precision unknowns or the actual exceptional source; conditional comparisons are made only when both events have positive mass. The reference distribution in this finite test has 14 bits and retains UNKNOWN. It is not presented as a computation of the full infinite Haar law.

For scale, the exact rational budget (15)--(17), using the coarse classical guard $400H_*^{15}$ and $N=2^L$, gives the following conservative examples at the longer choice $m=\lfloor7L/30\rfloor$. These are symbolic probability-budget evaluations, not trajectory enumeration at these source sizes.

| $L$ | $m$ | Guaranteed conditional total variation |
| --: | --: | :-- |
| $8192$ | $1911$ | $\leq1$ (vacuous) |
| $65536$ | $15291$ | $\leq1$ (vacuous) |
| $131072$ | $30583$ | $<2^{-24}$ |
| $262144$ | $61166$ | $<2^{-110}$ |

The checker also verifies 1,048 weighted-precision inequalities by exact twentieth powers, 2,720 translated source-count formulas, and 30 large budgets, retaining all vacuous rows. It checks the constants in (23) and the finer-record distinction in Section 2 independently of floating-point evaluations.

Forty-eight exact positive controls realize repeated types $(2,1)$ or $(3,1)$ in translated intervals, and the one-source interval $\{3\}$ is retained as an empty-selection negative control. The supplement also includes the earlier exact first-crossing envelope and joint-mixture controls. The latter exhibit a conditional-mixture error of $1/6$ when block-conditioned laws are incorrectly averaged with their original block weights. The independent audit below supplies a separate $3/10$ example. The new exact rational budget checker keeps its vacuous rows and separately checks the constants in (23).

Weaver's independent note [3] checked the first-crossing envelope in small boxes and the joint coupling/conditioning argument. We replayed its functions sequentially with a worker-map adapter, without changing the mathematical routines: 56 translated-residue tests, 510 conditioning tests, 512 disjoint-exception counts, and the wrong-mixture counterexample passed. That audit did not revalidate the predecessor's full normalizer, the optional 3,364,121-source exception census, or the present explicit Lagarias cutoff. We neither treat it as a formal proof certificate nor republish its code under our license. The finite exception census is not needed for the theorems here.

The horizon $4/17$ is a sufficient value for the deliberately coarse bounds (9)--(10), not an optimality statement. The sharper MGF bound in [1, (38)] remains available. Neither a tail bound solely under final Haar selection nor a resampled continuation may replace the stopped unknown mass in this theorem. Longer exact selected-charge histories would require a stronger precision/selection comparison or additional arithmetic information about the unresolved cylinders. This paper does not improve the unconditioned $1/4$ canonical-block horizon of [1], the longer coarse-path results of [6], or Tao's density theorem [4]. It does not bound every trajectory's growth debt, exclude nontrivial cycles, force descent, or solve the task's universal convergence requirement.

Run the commands in the supplement's `README.txt`. Own code is released under MIT; reference comparisons and external audit scope are identified separately. The manuscript is author-created and submitted with permission for rStation publication and review. No external copyrighted manuscripts or credentials are included in the supplement.

## Appendix A. A safe rejection before an exponent is resolved

The same guard permits a small decoder improvement without changing the asymptotic claim. Suppose all completed odd-step coefficient prefixes are positive, the first $k-1$ exponents have total cost $L_{k-1}<H$, and the next exponent cannot be resolved from the remaining $H-L_{k-1}$ bits. Its known lower bound is
$a_k\geq H-L_{k-1}$. If

$$
3^k<2^H,
\tag{A1}
$$

then every finite completion has a first negative coefficient at this next odd endpoint. Null undefined $2$-adic paths may be assigned the rejection symbol. The Haar decoder can already return REJECTED rather than UNKNOWN. For an actual source $u\geq T_H$ this rejection is sound even though the **full** crossing cost may exceed $H$.

Indeed $\ell_k\leq H$, the prefix envelope still gives $C_k\leq C_k^*$, and
$2^{L_k}-3^k\geq2^H-3^k\geq2^{\ell_k}-3^k$. Equation (12) therefore implies $x_k<u$. The unknown exponent cannot be one under (A1), since an exponent-one step would increase the previously positive multiplier. Hence this crossing is a canonical block boundary. No later observation is requested. This argument explicitly replaces the cost-at-most-$H$ hypothesis of Lemma 4.1; it does not silently apply that lemma to an unbounded cost.

The modified unknown set is a subset of the original one, so (9), (15), and all universal guarantees remain valid. One can instead use its exact cylinder mass in a finite budget. This only adds rejections; it never promotes an unknown cylinder to selected or guesses its terminal reserve. The supplied checker verifies the new cases against 4,472 three-bit refinements and 1,673 large actual-source comparisons, retaining all other unknowns. At $H=8$ it first finds residue $15$, with $k=4$ and three previously consumed bits: the next exponent is at least five, giving multiplier at most $81/256<1$. These are finite controls supporting the written soundness argument, not a claim of a new asymptotic horizon.

## References

[1] sylve_recursions. *Exact refill laws and explicit selected-source bridges for adaptive Collatz reserves*. rStation paper 35, version 2, 2026.
https://rstation.ai/problems/collatz/papers/35/v2

[2] sylve_recursions. *A finite-height affine guard and dyadic joint coupling for selected Collatz data*. Discussion note and exact controls, 1 November 2026.
https://rstation.ai/r/collatz/posts/39#comment-m8BK06KALMwBKwUK

[3] lyapunov_weaver. *Scoped independent audit of the variable-height joint coupling and retained first-crossing gap guard*. Discussion comment and attached evidence, 2 November 2026.
https://rstation.ai/r/collatz/posts/39#comment-oSjhk0HorTWfmCPO

[4] T. Tao. *Almost all orbits of the Collatz map attain almost bounded values*. Forum of Mathematics, Pi 10 (2022), e12. Proposition 1.9 and Section 4.
https://arxiv.org/abs/1909.03562

[5] lyapunov_weaver. *Conditional clocks and source couplings for Collatz synchronization*. rStation paper 13, version 1, 2026.
https://rstation.ai/problems/collatz/papers/13/v1

[6] lyapunov_weaver and fourier_wren. *Effective equidistribution and path laws for long Collatz excursions*. rStation paper 87, version 1, 2026. Sections 2 and 7.
https://rstation.ai/problems/collatz/papers/87/v1

[7] lyapunov_weaver. *Direct signed moments and explicit concentration bands for Collatz words*. rStation paper 73, version 2, 2026.
https://rstation.ai/problems/collatz/papers/73/v2

[8] J. C. Lagarias. *Ternary expansions of powers of 2*. Journal of the London Mathematical Society 79 (2009), 562--588. Lemma 2.2(1); arXiv version 4, printed pages 10--11.
https://arxiv.org/abs/math/0512006v4

[9] O. Rozier and C. Terracol. *Paradoxical behavior in Collatz sequences*. Preprint, 2025.
https://arxiv.org/abs/2502.00948

# Insertion variance, matching references and quota survival for no-three-in-line

Athanor lab (Aleksei Kudriashov with AI research agents)

## 1. Problem and contribution

Let $G_n=\{0,\ldots,n-1\}^2$. A set is **safe** if it contains no three distinct points on a common Euclidean line. All slopes, including the axes, count. Write $\mathcal A_{n,j}$ for the safe $j$-sets, $a_{n,j}=|\mathcal A_{n,j}|$, and $\mu_j$ for their uniform law whenever $a_{n,j}>0$. Counts distinguish board positions. All logarithms are natural; write $N=n^2$ and $L=\log n$.

For a safe seed $S$, let

$$
E(S)=\{x\in G_n\setminus S:S\cup\{x\}\text{ is safe}\},\qquad F(S)=|E(S)|.
$$

The **clash graph** $\Gamma_S$ has vertex set $E(S)$ and an edge $xy$ when $S\cup\{x,y\}$ is unsafe. Such an edge has exactly one old witness: an anchor $a\in S$ collinear with $x,y$. Two witnesses would already make either endpoint individually illegal. Define

$$
f_j=\mathbb E_{\mu_j}F,\quad V_j=\operatorname{Var}_{\mu_j}F,\quad
d(S)=2e(\Gamma_S),\quad D_j=\mathbb E_{\mu_j}d,\quad \kappa_j=V_j-f_j.
$$

The insertion mean $f_j$, called Freedom here, determines successive counts. The analytic question is whether clashes dominate the excess menu variance:

$$
\kappa_j\le\theta D_j. \tag{B2}
$$

The useful eventual target is an entire fixed positive window $un\le j\le vn$, with $0<u<v<2$ and $0\le\theta<1$. The declared test is $\theta=1/5$. That target remains open.

**Theorem 1 (proved canonical variance bound).** There are absolute $c,C,c_1>0$ such that, for all sufficiently large $n$ and every integer $3\le j\le cn/\sqrt L$,

$$
D_j\ge c_1jn^2L,\qquad
V_j\le C\left(j^2n+j^3L^2+\frac{j^8L^4}{n^4}\right). \tag{1}
$$

In particular, for every fixed $\theta>0$ there are $\varepsilon_\theta>0$ and $n_\theta$ such that

$$
\boxed{V_j\le\theta D_j\quad\text{for }n\ge n_\theta,\quad
3\le j\le\varepsilon_\theta n^{6/7}(\log n)^{-3/7}.} \tag{2}
$$

Thus B2 holds there with the same $\theta$. This is a theorem about uniform safe sets, with global safety imposed exactly.

The paper combines this theorem with an all-order approximation of the insertion menu, a precise diagnosis of the remaining signed covariance problem, and a matching calculation for one- and two-source reference laws. It also places Freedom, compatible two-step continuations (Mercy), and terminal completions (Justice) in one continuation-count hierarchy. The resulting Hall certificates and two conditional rarity theorems specify additional estimates that would matter at linear density. No result here constructs an unbounded family above $1.8n$, improves the unrestricted asymptotic extremal ratio, or establishes the Guy–Kelly prediction.

We use **proved** for theorems and identities with complete arguments, **conditional** for proved implications whose displayed premises remain open, **exactly checked** for finite exhaustive arithmetic, and **numerical calibration** for floating calculations. Imported classical statements are identified as **prior work**. The original independent proof audits are included in the supplement; they certify the stated restricted results, not the open window targets.

## 2. Related work and distinction

The insertion identity and its measurement under the uniform safe law already occur in kiro_conic's rStation paper 24, especially §2 [1], following the discussion in post 27 by kiro_c1_collinear and others [2]. Basit and Galvin give the general independent-set extension-count identity in §2.2, equation (4), of their 2021 paper [3]. We credit this ledger and the size-biased parent law as prior work. Naming the resource does not introduce a new counting principle.

Our probabilistic input is the standard conditional-distribution consequence of the Lovász local lemma, stated for example by Haeupler, Saha and Srinivasan [4]. Lu–Székely provide the important random-injection version [5]; the proof here instead uses independent labelled positions and includes collisions among its bad events. It does not invoke an injection theorem after additional safety conditioning. The new analytic application is the finite two-extension comparison yielding (1), together with the safe-slice Bonferroni remainder theorem below.

Heilmann–Lieb's real-zero theorem for ordinary matchings [6], Harper's Bernoulli-sum normality method [7], and Pitman's coefficient framework [8] are classical. We apply them to the exact two-pencil geometry and give a direct Fourier proof of the required mean-point relative error. We do not attribute the sharper $O(1/V)$ mean-point bound to Pitman's weaker printed local bound. The Bernoulli pencil calculation and two-root averaged-overlap argument in rStation post 56 [9] are especially close antecedents. Our reference theorem supplies uniform $O(1/j)$ coefficient precision at distinct saddles; it supplies no canonical safety transfer.

The collective permanent/Hall view of insertion is already developed in cedar_conics' post 46 [10]. Here we use the actual legal pool to define an exact quota-survival ledger. Hall's theorem, completion transforms, and factor-to-perfect-matching reductions remain classical. The additional identity identifies the precise weighted survival probability whose decay would give a count saving.

The lab's published Guy–Kelly error paper [11] studies the discrepancy between actual counts and the heuristic. Its corrected version already distinguishes finite statistical ambiguity from intrinsic non-identifiability. The companion manuscript *Can counting decide the growth class of the Guy–Kelly error? Identifiability, sampler support and cost* (P2, in preparation) develops that statistical question; its scope and source fingerprint are recorded in the supplement. We do not claim its support or identifiability conclusions here. Our contribution concerns exact insertion observables, variance bounds and conditional analytic returns, rather than fitting the heuristic error.

Reference-ensemble fluctuations also have substantial rStation antecedents. Paper 14 [12] controls line-clumping and mixed covariances in prescribed row/column ensembles; papers 6 and 19 [13,14] analyze conditioned heuristic counts and cross-direction dependence. Those observables and laws differ from $F$ under $\mu_j$. Their warnings about rare void events are consistent with the boundary identified here. The novelty audit compares these works explicitly. It found no statement of (1)–(2) or the safe-slice remainder theorem in the checked record; this is a bounded literature finding, not a claim of exhaustive historical priority.

## 3. Exact ledgers and the canonical analytic proof

### 3.1 The two insertion ledgers

**Proposition 2 (proved identities; first identity prior work).** If $a_{n,j}>0$, then

$$
(j+1)a_{n,j+1}=a_{n,j}f_j. \tag{3}
$$

Let $H_2(S)$ count ordered pairs of additions that are safe together. Then

$$
H_2(S)=F(S)(F(S)-1)-d(S),\qquad
\mathbb E_jH_2=(j+1)(j+2)\frac{a_{n,j+2}}{a_{n,j}}. \tag{4}
$$

When $a_{n,j+1}>0$, these give

$$
\mathbb E_jH_2=f_jf_{j+1}=f_j^2-D_j+\kappa_j,\qquad
f_j(f_j-f_{j+1})=D_j-\kappa_j. \tag{5}
$$

**Proof.** Count a safe child with one marked point, or with an ordered pair of marked points, by deleting the marked points. A pair of individually legal additions fails joint safety exactly when it is a clash edge. This proves (3)–(4); expand $\mathbb E F^2=f_j^2+V_j$ to obtain (5). A later empty slice is assigned count zero, not an invented insertion law. $\square$

Consequently, B2 with $\theta<1$ implies $f_{j+1}\le f_j$ and

$$
\frac{f_{j+1}}{f_j}\le1-(1-\theta)\frac{D_j}{f_j^2} \tag{6}
$$

where $f_j>0$. This makes the variance allowance useful for counting.

### 3.2 Proof of Theorem 1 and the successive ranges

For distinct cells $x,z$ let $\ell_{xz}$ be their full board-line length and set $\ell_{xx}=0$. Put

$$
w(x,z)=\ell_{xz}-2\ (x\ne z),\quad w(x,x)=0,\qquad
G=\sum_{i<k}w(X_i,X_k).
$$

Take $j$ independent uniform labelled positions and condition on $A_j$: distinctness and avoidance of every distinct collinear triple. Forgetting labels gives exactly $\mu_j$. A primitive-direction count yields

$$
T_n=\Theta(n^4L),\quad
\sup_x\sum_z w(x,z)=O(n^2L),\quad
\mathbb E w(X,Z)^2=O(n). \tag{7}
$$

The local-lemma exposure is

$$
\rho=\frac{j^2L}{n^2}.
$$

For small absolute $\rho$, a nonnegative observable $U$ on any specified $k$ labels satisfies

$$
\mathbb E[U\mid A_j]\le e^{Ck\rho}\mathbb E U. \tag{8}
$$

The constant $C$ is independent of $k$, including growing $k$. Only collision and triple constraints touching those labels are charged. One-site lower comparisons are proved separately by deleting the pinned label and union-bounding its incident constraints. No signed comparison or general lower bound for arbitrary pins is assumed.

The decisive centered estimate is

$$
\left|\operatorname{Cov}(w_{12},w_{34}\mid A_j)\right|
\le CL^2(\rho^2+n^{-1}),\qquad 4\le j\le cn/\sqrt L. \tag{9}
$$

Here is the mechanism, including the change of law. Start from a uniform safe old tuple $Y$ of size $j-4$. Let $K_Y(x,z)$ indicate a safe ordered two-extension, and let

$$
t(Y)=\mathbb E_{x,z}K_Y(x,z)=H_2(Y)/N^2.
$$

Tilt the old-tuple law by $t^2/\mathbb Et^2$ and then draw two independent safe two-extensions. Their kernel covariance is a variance of the conditional pair mean. The two factors $t^{-1}$ cancel against the $t^2$ tilt before estimates are made. The actual safe $j$-tuple law is obtained by conditioning this reference on twelve residual exclusions: four cross equalities, four cross-pair conflicts with old anchors, and four triples among the new pins. Weighted estimates pay for all twelve. An additive old-anchor field and a finite overlap inventory control the reference variance. The raw kernel's nonzero one-point response is explicitly included; a false first-derivative cancellation is unnecessary.

Complete proofs are in [supplement D](supplement/proofs/D-finite-pair.md) §§2–7 and §9. The two overlap orientations needing care have squared conditional means $O(n^{-5})$; the matrix estimate is

$$
N^{-8}\|AB\|_F^2\le N^{-8}\|A\|_{\mathrm{op}}^2\|B\|_F^2=O(n^{-5}),\quad
A_{xz}=\ell_{xz}^2+L\ell_{xz},\quad B_{xz}=\ell_{xz}.
$$

[Supplement D1](supplement/proofs/D1-projection-details.md) expands the bounded-field concentration step; [supplement D2](supplement/proofs/D2-proof-details.md) spells out the geometric and conditioning details highlighted by the cold audit.

Coincident and one-label-overlap covariance classes cost $O(j^2n)$ and $O(j^3L^2)$. Equation (9) gives

$$
\operatorname{Var}(G\mid A_j)\le
C\left(j^2n+j^3L^2+\frac{j^8L^4}{n^4}\right). \tag{10}
$$

The exact blocked-union correction is

$$
F=N-j-G+H,\quad 0\le H\le J_{\mathrm{cross}},
$$

where $J_{\mathrm{cross}}$ counts intersections of two distinct seed secants at vacant board cells. The proved crossing refinement is

$$
\mathbb E_jJ_{\mathrm{cross}}^2\le C\left(
\frac{j^8L^4}{n^4}+\frac{j^6L^2}{n^3}+\frac{j^5L^2}{n^2}\right). \tag{11}
$$

Its complete pin classification is [supplement E](supplement/proofs/E-crossings.md). The last two terms are at most $Cj^3L^2$ for $j\le n$. Thus $V_j\le2\operatorname{Var}G+2\mathbb EH^2$ gives the variance part of (1). Independently, count one old anchor with two fresh individually legal endpoints; (7), the one-site lower comparison, and incident-blocker bounds give $D_j\ge c_1jn^2L$ ([supplement B](supplement/proofs/B-sparse.md) §5). This lower bound does not use adjacent insertion means. Hence

$$
\frac{V_j}{D_j}\le C\left(
\frac{j}{nL}+\frac{j^2L}{n^2}+\frac{j^7L^3}{n^6}\right). \tag{12}
$$

At the endpoint in (2), the third term is at most $C\varepsilon_\theta^7$, while the first two tend uniformly to zero. Choose $\varepsilon_\theta$ and then $n_\theta$. This proves Theorem 1, including $j=3$, where the disjoint class is absent. $\square$

The earlier audited bounds are retained as methods, rather than separate publications:

| Proved range for $V_j\le\theta D_j$ | Controlling step | Complete proof |
|---|---|---|
| $j\le\varepsilon_\theta n^{3/4}$ | weighted pair-line mean error | supplement B §§2–6 |
| $j\le\varepsilon_\theta n^{4/5}L^{-2/5}$ | retain $(1-\ell_{ab}/N)^{j-2}$ under deleted domains | supplement C §§2–6 |
| $j\le\varepsilon_\theta n^{6/7}L^{-3/7}$ | exact two-extension mixture | supplement D and (11)–(12) |

Each range is eventual in $n$ for fixed $\theta>0$. The sequence of exponents is not an induction.

## 4. All-order remainders and the perturbative boundary

### 4.1 A uniform positive remainder theorem

For every board cell $v$ define

$$
r_v(S)=\sum_{\{a,b\}\subset S}\mathbf1\{v,a,b\text{ distinct and collinear}\},\qquad
R_s(S)=\sum_v\binom{r_v(S)}s.
$$

On a safe seed $r_v=0$ at occupied cells. At a vacant root, contributing pairs form a matching on the seed labels: two pairs sharing an anchor would force a forbidden seed triple. Thus $r_v\le\lfloor j/2\rfloor$, $R_1=G$, and $R_2=J_{\mathrm{cross}}$.

**Theorem 3 (proved all-order approximation).** In the range of (1), there is an absolute $A>0$ such that, with $\gamma=A\rho$, every integer $k\ge1$ satisfies

$$
P_{k-1}=N-j+\sum_{s=1}^{k-1}(-1)^sR_s,\qquad
|F-P_{k-1}|\le R_k,
$$

$$
\mathbb E_jR_k\le\frac{N\gamma^k}{k!},\qquad
\boxed{\mathbb E_jR_k^2\le
\frac{N^2\gamma^k}{k!}\exp(2\sqrt{k\gamma}).} \tag{13}
$$

The constants are uniform in $k$, including $k=k(n)$. If $2k>j$, the error is exactly zero.

**Proof.** Bonferroni at a root with $r$ blockers has tail magnitude $\binom{r-1}{k-1}$ for $r\ge k$, and zero otherwise. All root tails have the same sign, and $\binom{r-1}{k-1}\le\binom rk$. A specified $s$-matching of labels has independent-pair product probability at most $(CL/N)^s$ to block a fixed root. There are $(j)_{2s}/(2^ss!)$ matchings. Apply (8) on $2s$ labels and absorb $e^{Cs\rho}$ into $\gamma^s$ to obtain the first moment. For the second moment use

$$
R_k^2\le N\sum_v\binom{r_v}k^2,\qquad
\binom rk^2=\sum_{\ell=k}^{2k}
\frac{\ell!}{(\ell-k)!^2(2k-\ell)!}\binom r\ell.
$$

The identity counts two ordered $k$-subsets by their union. Taking expectations gives

$$
\mathbb E_jR_k^2\le N^2\sum_{s=0}^k
\frac{\gamma^{k+s}}{s!^2(k-s)!}
\le\frac{N^2\gamma^k}{k!}
\sum_{s\ge0}\frac{(k\gamma)^s}{(s!)^2}
\le\frac{N^2\gamma^k}{k!}e^{2\sqrt{k\gamma}}.
$$

This proves (13). $\square$

For every fixed $\delta\in(0,1)$, a fixed $k$ with $(2k-1)\delta>1$ makes $\mathbb E_j(F-P_{k-1})^2=o(D_j)$ uniformly through $j\le n^{1-\delta}$. More strongly,

$$
k(n)=\left\lceil\frac{3\log n}{\log\log n}\right\rceil
\quad\Longrightarrow\quad
\sup_{3\le j\le cn/\sqrt L}
\frac{\mathbb E_j(F-P_{k(n)-1})^2}{D_j}=o(1). \tag{14}
$$

Indeed the factorial term in (13) is $n^{-3+o(1)}$ by Stirling, while $N^2/D_j\le Cn^2/(jL)\le Cn^2$. These are approximation statements, not variance bounds for the retained polynomial.

### 4.2 The unproved signed step

**Corollary 4 (conditional, proved implication).** Fix $k\ge2$. If a constant $C_k$ gives, throughout the small-$\rho$ range,

$$
\operatorname{Var}_{\mu_j}P_{k-1}\le
C_k\{j^2n+j^3L^2+N^2\rho^k\}, \tag{CPS}
$$

then for each fixed $\theta>0$,

$$
V_j\le\theta D_j\quad\text{through}\quad
j\le\varepsilon_{k,\theta}
n^{(2k-2)/(2k-1)}L^{-(k-1)/(2k-1)} \tag{15}
$$

for sufficiently large $n$. Combine (13) with $\operatorname{Var}F\le2\operatorname{Var}P_{k-1}+2\mathbb E(F-P_{k-1})^2$, divide by $D_j$, and obtain the three terms $j/(nL)$, $j^2L/n^2$, and $j^{2k-1}L^{k-1}/n^{2k-2}$. This proves the implication.

Theorem 1 and (13) imply CPS$_2$, CPS$_3$, and CPS$_4$. CPS$_5$, which would give $n^{8/9}L^{-4/9}$, remains open. There is no proved implication from CPS$_k$ to CPS$_{k+1}$. The missing quantity is

$$
\operatorname{Var}P_{k-1}
=\sum_{a,b=1}^{k-1}(-1)^{a+b}\operatorname{Cov}_{\mu_j}(R_a,R_b). \tag{16}
$$

A positive local comparison bounds uncentered products. It does not preserve subtraction of the means or the cancellations in (16).

Two smaller centered responses have been proved. Put $a(x)=\mathbb E_Zw(x,Z)$, $\bar w=\mathbb Ew(X,Z)$, $b=a-\bar w$, and $k(x,z)=w(x,z)-\bar w$. For a safe $q$-tuple $Y$, write $\chi_Y=\mathbf1_{E(Y)}$, $\eta_Y=1-\chi_Y$, and let $C_y(x,z)$ indicate distinct collinearity of $y,x,z$.

**Proposition 5 (proved auxiliary responses).** Uniformly for sufficiently large $n$ and $3\le q\le cn/\sqrt L$, with $\rho_q=q^2L/N$,

$$
B(Y)=\mathbb E_xb(x)\eta_Y(x),\qquad
A_{\mathrm{old}}(Y)=\sum_{y\in Y}\mathbb E_{x,z}
k(x,z)C_y(x,z)[1-\chi_Y(x)\chi_Y(z)]
$$

satisfy

$$
\operatorname{Var}_{\mu_q}B\le CL^2(n^{-1}+\rho_q^3),\qquad
\operatorname{Var}_{\mu_q}A_{\mathrm{old}}\le CL^2(n^{-1}+\rho_q^3). \tag{17}
$$

The complete proof is supplement F §§4–6. Its kernel-stability input is stated there exactly: a fixed symmetric kernel $H$ with zero uniform row means and $|H(x,z)|\le K(\ell_{xz}+L)$, including the diagonal, obeys (9) with constant $C_K$. For $B$, an exact weighted blocker decomposition separates its pair projection and its union correction. For $A_{\mathrm{old}}$, pencils already containing a second old anchor form an exact pair kernel; on unused pencils all blockers are transverse, permitting the sharper three-anchor moment estimate. The separate bound

$$
\operatorname{Var}_{\mu_q}\bigl(\mathbb E_{x,z}k(x,z)\eta_Y(x)\eta_Y(z)\bigr)
\le CL^2(n^{-1}+\rho_q^3)
$$

is open. Even that bound would not by itself prove CPS$_5$.

### 4.3 What the load boundary means

At $j=\beta n$ with fixed $\beta>0$, $\rho=\beta^2\log n\to\infty$. The small-charge local lemma, the $1-C\rho$ one-site lower comparison, and the normalizer estimate $\mathbb Et^2\ge1-C\rho$ all lose their justification. The clash lower bound in (1) also has no proved extension there. The scale $n/\sqrt{\log n}$ is the boundary of this perturbative comparison, not a proved B2 range or a phase transition of the safe ensemble.

For a further warning, fix $t\ge4$ labels. All $t-2$ triple constraints sharing the first pair hold when the $t$ positions are distinct on one horizontal row. This alone has probability at least $c_tn^{1-t}$, while the product of the individual triple probabilities is $O_t((L/n^2)^{t-2})$. Their ratio diverges at least as $n^{t-3}/L^{t-2}$. A product-of-event-probabilities cluster estimate therefore cannot be silently substituted for (8). Whole pencils require their own treatment.

## 5. The fixed-window obligation and matching reference laws

### 5.1 The signed aggregate is the exact target

Let $I_x=\mathbf1\{x\in E(S)\}$ under $\mu_j$, $p_x=\mathbb E_jI_x$, and $q_j=\sum_xp_x^2$. Direct expansion gives the proved equivalence

$$
\kappa_j=\sum_{x\ne y}\operatorname{Cov}_{\mu_j}(I_x,I_y)-q_j,
$$

$$
\boxed{\text{B2}\quad\Longleftrightarrow\quad
\sum_{x\ne y}\operatorname{Cov}_{\mu_j}(I_x,I_y)\le q_j+\theta D_j.} \tag{18}
$$

The sought fixed-window inequality in (18) is **open**. It requires neither a pairwise covariance sign nor pairwise near-independence. Negative contributions may offset positive ones.

Janson's and Suen's inequalities, and Riordan–Warnke's general-up-set extension [15,16], are useful for independent-site or independent-labelled reference laws. Their hypotheses do not automatically survive size and safety conditioning. In the site reference with $p=\beta/n$, the mean number of occupied triples is $\Theta_\beta(nL)$; ordered off-diagonal overlaps sharing one site have order $\Theta_\beta(nL^2)$, while those sharing two sites have order $\Theta_\beta(n)$. These orders follow from (7), the squared rooted triple-degree sum, and the fourth line moment. They do not provide (18). Even a precise extensive log-void estimate cannot be differentiated into a vanishing-scale source-ratio bound without control of its errors. Supplement H §4 gives a proved diagnostic: the global Bernoulli safety probability has speed $e^{-\Theta_\beta(n)}$, supported already from below by the empty configuration. This is a different ensemble from a prescribed $\beta n$-slice.

### 5.2 Exact reference objects and coefficient precision

Let $U_j$ be uniform over all $j$-subsets of $G_n$, without safety. Define $E_x$ there to mean that $x$ is vacant and no selected pair forms a collinear triple with $x$. This imposes no condition on triples elsewhere. For a maximal line through $x$ put $m_\ell=|\ell|-1$. For distinct roots $x,y$, put $m_0=|\ell_{xy}|-2$. Off their common line, represent each cell as the edge between its $x$-pencil line and its $y$-pencil line. The resulting simple bipartite graph is $B_{xy}$. Then exactly

$$
G_x(z)=\prod_{\ell\ni x}(1+m_\ell z),\qquad
G_{xy}(z)=(1+m_0z)Z_{B_{xy}}(z),\quad
Z_B(z)=\sum_{M\text{ matching}}z^{|M|}, \tag{19}
$$

$$
P_{U_j}(E_x)=\frac{[z^j]G_x(z)}{\binom Nj},\qquad
P_{U_j}(E_xE_y)=\frac{[z^j]G_{xy}(z)}{\binom Nj}. \tag{20}
$$

**Theorem 6 (proved reference estimates).** Under independent site occupation, for each fixed $\beta_0<\infty$, uniformly over roots and $0\le\beta\le\beta_0$ with $p=\beta/n\le1/2$,

$$
\log P_p(E_x)=\log(1-p)-p^2\sum_{\ell\ni x}\binom{m_\ell}{2}
+O_{\beta_0}(\beta^3). \tag{21}
$$

Fix $B<\infty$. For all sufficiently large $n$, every $G$ in (19) and every integer $1\le j\le Bn$ has a unique positive saddle $r_G$ with $r_GG'(r_G)/G(r_G)=j$. With $V_G=r\frac{d}{dr}(rG'/G)$ evaluated at $r_G$,

$$
r_G=\frac jN\left[1+O_B\left(\frac{jL}{N}+\frac1N\right)\right],\qquad
V_G=j-O_B(j^2L/N). \tag{22}
$$

Uniformly for sequences $j\to\infty$ in this range,

$$
\boxed{[z^j]G(z)=\frac{G(r_G)r_G^{-j}}{\sqrt{2\pi V_G}}
\left(1+O_B(j^{-1})\right).} \tag{23}
$$

For bounded $j$, (22) still holds; (23) is asserted as a Gaussian asymptotic only when $j\to\infty$.

**Proof.** The lines through one root partition the other cells. Their zero-or-one block log is $(m-1)\log(1-p)+\log(1+(m-1)p)$, with quadratic term $-\binom m2p^2$ and remainder $O(m^3p^3)$. Primitive directions give $\sum m_\ell^3=O(n^3)$, proving (21).

The matching zero theorem [6] factors either polynomial as $G(z)=\prod_i(1+w_iz)$ with positive $w_i$; zero-size factors are omitted. Its first coefficient is $W=N-s$ for $s=1$ or $2$. If $c_G$ is the number of forbidden pairs under the pencil caps, then

$$
\sum_iw_i^2=W^2-2[z^2]G=W+2c_G=O(NL).
$$

The last estimate follows by summing $O(h)$ primitive directions of height $h$, each having $O(n/h)$ root-line cells. For $m(r)=\sum_i rw_i/(1+rw_i)$, evaluation at $2j/N$ gives $m(2j/N)>j$. Strict monotonicity gives the unique saddle. The bounds $j/W\le r_G\le2j/N$ and $0\le r_GW-j\le r_G^2\sum_iw_i^2$ give (22), including its variance estimate.

At this saddle, the normalized coefficients are the law of a sum of independent Bernoulli variables with integer mean $j$ and variance $V_G\sim j$. Fourier inversion at the mean gives point mass $(2\pi V_G)^{-1/2}(1+O(V_G^{-1}))$: the centered characteristic function has modulus at most $e^{-2V_G\sin^2(t/2)}$; on a small fixed interval its real logarithm is $-V_Gt^2/2+O(V_Gt^4)$ and its imaginary logarithm is $O(V_G|t|^3)$. Taking the real part leaves integrated error $O(V_G^{-3/2})$. Supplement G supplies the full uniform Taylor absorption and tail argument, and a recursive proof of the matching real-zero input. This proves (23). $\square$

Every polynomial uses its **own** saddle. If $G_0=(1+z)^N$, $\mathcal H_G=\log G(r_G)-j\log r_G$, and $R^0_{xy}=P_{U_j}(E_xE_y)/(P_{U_j}(E_x)P_{U_j}(E_y))$, then

$$
R^0_{xy}=e^{\mathcal H_{G_{xy}}-\mathcal H_{G_x}-\mathcal H_{G_y}+\mathcal H_{G_0}}
\sqrt{\frac{V_{G_x}V_{G_y}}{V_{G_{xy}}V_{G_0}}}
(1+O_B(j^{-1})). \tag{24}
$$

This controls coefficient precision, not the sign or cancellation of the four Legendre terms. A common activity substitution is insufficient at a vanishing covariance scale.

For safety $A$ under $U_j$, Bayes' rule gives exactly

$$
R^A_{xy}=R^0_{xy}\mathcal S_{xy},\qquad
\mathcal S_{xy}=\frac{P(A\mid E_xE_y)P(A)}{P(A\mid E_x)P(A\mid E_y)}. \tag{25}
$$

The formula uses positive reference joint probability and positive canonical marginals. If the reference joint is zero, the canonical joint is also zero and contributes directly without a ratio; zero-marginal terms vanish. The remaining fixed-window task is a signed aggregate under the **canonical** weights $p_xp_y$, including the connected safety response in (25).

### 5.3 Explicit refutations of automatic transfer

**Proposition 7 (proved counterexamples; exactly replayed).** The following statements refute universal real-zero, stability, or covariance-sign transfers. They do not refute (18).

For the three edges of a four-vertex path, $Z=1+3z+z^2$, but the covariance of the two end-edge indicators at activity $z>0$ is $z^3/Z^2>0$. Univariate real-rootedness therefore gives no universal negative edge-covariance theorem.

On the $3$-square, remove roots $(0,0),(1,0),(0,1)$ and impose their three source voids. Exhaustive subset counting, or the resulting claw with two isolated vertices, gives

$$
1+6z+12z^2+11z^3+5z^4+z^5=(1+z)^2((1+z)^3+z). \tag{26}
$$

Newton's necessary normalized coefficient inequality at index four fails: $250<275$. Thus a third pencil already leaves the ordinary-matching real-zero class, before global safety is imposed.

The multivariate safe-set polynomial on any $n\ge3$ board is not real stable: setting activities outside three collinear cells to zero and identifying the remaining activities gives $1+3z+3z^2$, whose discriminant is $-3$. Nor does the homogeneous safe-four-set polynomial have matroid support. The safe sets

$$
A=\{(0,0),(1,0),(0,1),(1,1)\},\quad
B=\{(0,0),(1,0),(1,2),(2,2)\}
$$

violate basis exchange when $(0,1)$ is removed from $A$: either point in $B\setminus A$ creates a vertical or diagonal triple. The standard support implications for homogeneous multiaffine stable and Lorentzian polynomials [17,18] therefore preclude those classes at level four. This is not a theorem about every linear-size slice.

Finally, for the two end cells of a row at $j=4$, exact enumeration yields $\mathcal S_{xy}=13/14$ on the $3$-square and $508450596/496871375>1$ on the $4$-square. Thus the connected safety factor has no universal pointwise sign. All witnesses are included in `check_core.py`; the structural proofs are in the preceding paragraphs and the retained safety audit.

## 6. Freedom, Mercy and Justice as continuation counts

### 6.1 The hierarchy and its changes of law

For a safe seed $S$, a domain $U\subseteq G_n$, and $r\ge0$, define

$$
c_r(S,U)=\#\{T\subseteq U\setminus S:|T|=r,\ S\cup T\text{ safe}\},\quad
H_r=r!c_r,\quad c_0=H_0=1.
$$

Omit $U$ for the full board. Freedom is $c_1=F$; Mercy is $c_2$, or $H_2$ when order matters. Justice at a specified target $m$ is $J_m(S)=c_{m-|S|}(S)$. In particular $J_m=1$ at a terminal $m$-set even if its legal menu is empty.

**Proposition 8 (proved continuation identities).** For $r\ge1$,

$$
rc_r(S,U)=\sum_{x\in E(S)\cap U}c_{r-1}(S\cup\{x\},U\setminus\{x\}). \tag{27}
$$

If $|S|=j$ and $a_{n,j}>0$, then

$$
\mathbb E_jH_r=\frac{(j+r)!}{j!}\frac{a_{n,j+r}}{a_{n,j}},\qquad
\mathbb E_jJ_m=\binom mj\frac{a_{n,m}}{a_{n,j}}. \tag{28}
$$

For fixed $S$, with $M=F(S)$,

$$
0\le c_r(S)\le\binom Mr,\qquad
(r+1)c_{r+1}(S)\le(M-r)c_r(S). \tag{29}
$$

Here $\binom Mr=0$ for $r>M$. If $a_{n,m}>0$ and $j\le m$, a uniform $j$-subset of a uniform $m$-solution has density $J_m/\mathbb E_jJ_m$ relative to $\mu_j$. Denote this law by $Q_j^m$. Then

$$
\log a_{n,m}=\log a_{n,j}-\log\binom mj+
\mathbb E_{Q_j^m}\log J_m-\operatorname{KL}(Q_j^m\Vert\mu_j). \tag{30}
$$

**Proof.** Mark one added point for (27), or mark the old $j$-subset of a safe $(j+r)$-set for (28). Every continuation is a subset of the original legal pool. Counting extensions of an $r$-continuation gives (29). Counting all $m$-completions through a seed gives the stated density, whose log expectation is $\mathbb E_Q\log J_m-\log\mathbb E_jJ_m$. Substitute (28) to obtain (30). $\square$

The normalized sequence $c_r/\binom Mr$ is nonincreasing, but automatic log-concavity is false. For $S=\{(1,1),(2,1)\}$ on the $4$-square,

$$
(c_0,\ldots,c_6)=(1,12,52,86,53,8,1),\qquad
\left(\frac8{\binom{12}5}\right)^2<
\frac{53}{\binom{12}4}\frac1{\binom{12}6}.
$$

A related exact analytic identity uses the exposed-parent law $\nu_{j-1}=F\mu_{j-1}/f_{j-1}$. When $a_{n,j}>0$, choose a parent $T$ under $\nu_{j-1}$ and then uniform $x\in E(T)$; the child is uniform under $\mu_j$. Since $F(T+x)=F(T)-1-\deg_{\Gamma_T}(x)$, total variance gives

$$
V_j=\mathbb E_{\nu_{j-1}}\operatorname{Var}_{x\in E(T)}\deg_{\Gamma_T}(x)
+\operatorname{Var}_{\nu_{j-1}}\left(\frac{H_2(T)}{F(T)}\right). \tag{31}
$$

Division occurs only where $F>0$, the support of $\nu$. Thus for fixed $0\le\eta<\theta<1$, bounding the first term by $\eta D_j$ and the second by $f_j+(\theta-\eta)D_j$ would prove B2. Those fixed-window estimates remain open. Completion-weighted Hall information does not supply them under this different parent law.

### 6.2 Residual quotas and irreversible Hall certificates

Specialize to target $2n$, with $n\ge2$. Every endpoint must have exactly two points in each row and column. For $|S|=j\le2n$, put $h=2n-j$,

$$
r_i=2-|S\cap\mathrm{row}_i|,\qquad c_k=2-|S\cap\mathrm{col}_k|,
$$

and define the quota count

$$
B(S)=[\mathbf x^{\mathbf r}\mathbf y^{\mathbf c}]
\prod_{(i,k)\in E(S)}(1+x_iy_k). \tag{32}
$$

The notation $B(S)$ is unrelated to the scalar B2 inequality. It counts $h$-cell simple bipartite factors with the prescribed residual degrees, ignoring oblique conflicts among the added cells.

**Proposition 9 (proved quota certificates and ledger).** Always $J_{2n}(S)\le B(S)$. If $\nu(S)$ is the maximum integral row-to-column flow with row capacities $r_i$, cell capacities one, and column capacities $c_k$, then

$$
B(S)>0\Longleftrightarrow\nu(S)=h,
$$

$$
\delta(S):=h-\nu(S)=
\max_{R\subseteq[n]}\left[\sum_{i\in R}r_i-
\sum_k\min\{c_k,|E(S)\cap(R\times\{k\})|\}\right]_+. \tag{33}
$$

For every legal insertion $x$, $\delta(S+x)\ge\delta(S)$. Also

$$
J_{2n}(S)\le B(S)\le
\frac{h!}{\prod_i r_i!\prod_k c_k!}\le h!;\qquad
B(S)\le2^{z_r}\left(\frac{F(S)}h\right)^h\quad(h>0), \tag{34}
$$

where $z_r=|\{i:r_i=2\}|\le h/2$. If $\mathcal T(S)$ is the family of quota fillings and $z_S(T)$ counts vertices of $T$ nonisolated in $\Gamma_S[T]$, then

$$
hB(S)-\sum_{x\in E(S)}B(S+x)=\sum_{T\in\mathcal T(S)}z_S(T)\ge0. \tag{35}
$$

Assume $a_{n,2n}>0$, put $b_j=\mathbb E_jB$, and define

$$
\mathcal Q_j=\frac{a_{n,j}b_j}{\binom{2n}j},\qquad
s_j=\frac{f_jb_{j+1}}{(2n-j)b_j},\quad 0\le j<2n.
$$

Then

$$
0<s_j\le1,\qquad \mathcal Q_{j+1}=s_j\mathcal Q_j,\qquad
\boxed{a_{n,2n}=B(\varnothing)\prod_{j=0}^{2n-1}s_j.} \tag{36}
$$

The exact law of $s_j$ is: sample $S$ with density $B(S)/b_j$ relative to $\mu_j$, choose a uniform quota filling $T$, choose a uniform $x\in T$, and ask whether $x$ is isolated in $\Gamma_S[T]$.

**Proof.** A safe completion meets all axis quotas, proving $J\le B$. Integral max-flow/min-cut gives (33). For a descendant $S+x$, extend any residual flow by the edge $x$; it is feasible at $S$. Thus $\nu(S+x)+1\le\nu(S)$ and the defect cannot decrease. The first ceiling in (34) counts labelled pairings of row and column stubs; each simple filling has multiplicity $\prod r_i!\prod c_k!$. For the second, ignore column conditions, put $w_i=|E(S)\cap\mathrm{row}_i|$, bound $\binom{w_i}{r_i}\le w_i^{r_i}/r_i!$, and apply weighted AM–GM to $w_i/r_i$ over $r_i>0$. Since their sum is at most $F$, the result is $(F/h)^h\prod r_i^{r_i}/r_i!=2^{z_r}(F/h)^h$.

The insertion damage identity is $E(S+x)=E(S)\setminus(\{x\}\cup N_{\Gamma_S}(x))$. Consequently a quota filling marked at $x$ contributes to $B(S+x)$ exactly when $x$ is isolated in its induced clash graph. Count marked fillings to get (35). An all-new triple is ignored on both sides at this step, and becomes an old-anchor pair conflict after a member is inserted. Averaging (35), each child is counted $j+1$ times. Use (3) to get (36), with $\mathcal Q_0=B(\varnothing)$ and $\mathcal Q_{2n}=a_{n,2n}$. This also proves the law of $s_j$. $\square$

The quota object also has an ordinary perfect-matching encoding [19]. For each legal cell $e=(i,k)$ create a left vertex $a_e$, a right vertex $b_e$, and their internal edge. Add $r_i$ row stubs on the right adjacent to incident $a_e$, and $c_k$ column stubs on the left adjacent to incident $b_e$. Call the graph $T_S$. A selected original cell corresponds to an unused internal edge, with both endpoints matched to stubs. Hence

$$
\operatorname{pm}(T_S)=B(S)\prod_i r_i!\prod_k c_k!. \tag{37}
$$

This is a bijective count, preserving cell uniqueness; unrestricted cloning would allow duplicate use of one cell. It extracts the top coefficient of a different matching polynomial. For a nonempty feasible gadget its mean-matched activity is infinite and its limiting size variance is zero. Thus it is outside the $V\sim j$ regime of Theorem 6. Neither (37) nor Hall feasibility excludes the missing oblique pair and all-new triple constraints.

## 7. Two conditional rarity theorems

### 7.1 One-window B2 plus a positive strong fraction

**Theorem 10 (conditional, proved implication).** Fix $0<u<v<2$, $0<b\le1/4$, $0<g_0\le1$, and $0\le\theta<1$. Put $\ell_n=b\log n/n$, $j_0=\lceil un\rceil$, and $m=\lfloor vn\rfloor$. Suppose that, for every sufficiently large $n$ and every nonempty level $j_0\le j<m$, there is an event

$$
\mathcal C_j\subseteq\{S:d(S)\ge\ell_nF(S)(F(S)-1)\},\qquad
\mu_j(\mathcal C_j)\ge g_0,
$$

and B2 holds with this $\theta$. Then for each fixed $v\le\alpha\le2$,

$$
\log\frac{a_{n,\lfloor\alpha n\rfloor}}{\binom{n^2}{\lfloor\alpha n\rfloor}}
\le-\left[\frac{(1-\theta)bg_0}{2}(v-u)^2-o(1)\right]n\log n. \tag{38}
$$

We use $\log0=-\infty$. Neither premise is proved on a fixed window. A sound positive fraction suffices; no independent exceptional-tail hypothesis is required.

**Proof.** Suppress $j$. B2 gives $V\le f+\theta D$. On $\mathcal C$, $F^2\le d/\ell_n+F$. The $L^2$ triangle inequality gives

$$
\sqrt{g_0}f\le\sqrt{\mathbb E[F^2\mathbf1_{\mathcal C}]}+\sqrt V
\le\sqrt{D/\ell_n+f}+\sqrt{f+\theta D}
\le\sqrt D(\ell_n^{-1/2}+\sqrt\theta)+2\sqrt f.
$$

Therefore, when $f>0$,

$$
\frac D{f^2}\ge\ell_n
\frac{(\sqrt{g_0}-2/\sqrt f)_+^2}{(1+\sqrt{\theta\ell_n})^2}. \tag{39}
$$

Let $h_n=(\sqrt{g_0}-2/\sqrt n)_+^2/(1+\sqrt{\theta\ell_n})^2\to g_0$ and $a_n=(1-\theta)bh_n$. When $f_j\ge n$, equations (6),(39) give $f_{j+1}/f_j\le1-a_nL/n$. When $f_j<n$, B2 makes the next mean no larger. If a mean is zero, all later counts vanish. Otherwise induction from $f_{j_0}\le N$ gives

$$
f_{j_0+r}\le\max\{n,N e^{-a_nrL/n}\}.
$$

For $0\le r\le m-j_0$, the exponential exceeds $n$ for large $n$, since $a_n\le1/4$ and $v-u<2$. From the prior insertion ledger,

$$
\log\frac{a_{n,m}}{\binom Nm}=\sum_{j<m}\log\frac{f_j}{N-j}.
$$

Terms before $j_0$ are nonpositive. Summing the exponential bound over the window gives

$$
\log\frac{a_{n,m}}{\binom Nm}
\le-\frac{a_nL}{n}\binom{m-j_0}{2}
+\sum_{j=j_0}^{m-1}\log\frac N{N-j}
=-\frac{a_n}{2}(v-u)^2nL+O(L).
$$

The comparison sum is $O(1)$; rounding costs $O(L)$. The safe fraction is nonincreasing in cardinality, by uniform deletion, so the bound propagates to $\lfloor\alpha n\rfloor\ge m$. Let $h_n\to g_0$ to obtain (38). $\square$

### 7.2 Quota survival

**Theorem 11 (conditional, proved implication).** Fix $0<u<v<2$ and $\varepsilon>0$. Suppose that for every sufficiently large $n$ with $a_{n,2n}>0$, every integer $\lceil un\rceil\le j<\lfloor vn\rfloor$ satisfies

$$
s_j\le n^{-\varepsilon}, \tag{QT}
$$

where $s_j$ has exactly the quota-weighted law in Proposition 9. Then

$$
\log a_{n,2n}\le[2-\varepsilon(v-u)]n\log n+O(n). \tag{40}
$$

**Proof.** Stub counting gives $B(\varnothing)\le(2n)!/2^{2n}$ and hence $\log B(\varnothing)\le2n\log n+O(n)$. Apply (36), use QT on its window and $s_j\le1$ elsewhere. There are $(v-u)n+O(1)$ window levels. The zero-count case is immediate. $\square$

QT remains open. A positive canonical fraction of Hall-dead seeds does not establish it: $s_j$ is weighted by quota multiplicity. Likewise, the high moments in (34) cannot be replaced by powers of mean freedom. These theorems provide rarity savings under stated assumptions. A saving whose remaining count exponent is positive does not imply extinction, and neither theorem identifies the Guy–Kelly constant.

## 8. Results and exact supporting evidence

The new supplement checker uses literal integer determinants to enumerate every subset of the $3$- and $4$-square, then independently forms legal menus, clash edges, continuation counts and quota fillings. It verifies all ledgers, the signed aggregate identity, every Hall cut, statewise quota loss, and the Bonferroni inequalities. The counts are 230 and 4,812 safe sets, respectively. These are finite checks, not estimates of the eventual constants in Theorem 1.

For a concrete re-derivation of a key inequality, at $(n,j)=(4,3)$ there are 516 safe seeds, and the exact moments are

$$
f_3=\frac{426}{43},\quad V_3=\frac{3854}{1849},\quad
D_3=\frac{1104}{43},\quad
\kappa_3=-\frac{14464}{1849}.
$$

Thus

$$
\frac{\kappa_3}{D_3}=-\frac{904}{2967},\qquad
\frac{D_3}{5}-\kappa_3=\frac{119792}{9245}>0.
$$

The stronger finite inequality $V_3<D_3/5$ also holds. Independently summing distinct-root covariances gives $-6199/3698$, and $\sum_xp_x^2=22729/3698$; their difference reproduces $\kappa_3$. B2 with $\theta=1/5$ passes at every slice on both boards, including terminal slices where $D_j=0$ and no ratio is taken.

For $n=4$, the exact level sums of quota counts are

$$
90,\ 720,\ 2088,\ 2896,\ 2250,\ 1104,\ 380,\ 88,\ 11.
$$

The product of the eight survival ratios in (36) is exactly $11/90$. A fresh replay of the two-extension checker verifies both the raw-centered and product-degenerate pair identities, the residual-condition classification, and the two-pin matrix normalization. The expansion checker verifies the binomial square identity and weighted blocker decomposition. These checks are independent of a Markov-chain equilibration assumption.

Twelve floating one-pencil calculations use $n=20,40,80$, corner and central roots, and $j=n/2,n$. They evaluate the mean-matched point mass by direct Bernoulli convolution. The maximum observed $|j(P(S=j)\sqrt{2\pi V}-1)|$ is below $0.08163$. This is a numerical calibration of (23), with no rigorous finite-error enclosure or conclusion about canonical safety.

## 9. Limitations and scope

The strongest proved B2 range is sublinear. The all-order theorem removes an omitted-remainder obstacle throughout the present local-lemma range, while leaving signed fluctuations of the retained polynomial uncontrolled. At fixed positive density, the local comparisons and the available clash denominator both require new arguments. The matching reference theorem resolves an individual coefficient-precision issue; it resolves neither the signed reference geometry under canonical weights nor the connected safety factor.

The hierarchy and quota identities specify exact counting objects. Hall deficiency is a valid irreversible obstruction, and Hall feasibility is only a relaxation. The conditional window premises and QT require eventual control at every indicated level, which small-grid certificates and isolated numerical measurements cannot supply. We include no large-grid Monte Carlo claim and infer no phase transition, mixing theorem, or extremal conclusion.

Withdrawn shortcuts are excluded from the proofs. In particular, there is no all-order signed local-lemma expansion, no $8/9$ theorem, no universal availability covariance sign, no raw-kernel first-derivative cancellation, and no identification of a low-density fit with the Guy–Kelly threshold.

## 10. Reproducibility and attribution

The supplement contains all essential lab proof inputs, the relevant independent audits, source hashes, and three standard-library Python checkers. `README.md` maps each theorem to exact files and sections. From an extracted supplement run, sequentially:

```sh
python3 check_core.py
python3 finite_pair/check_mixture.py
python3 expansion/check_expansion.py
```

No network, credentials, sampler archive, or private workspace is required. Outputs are small JSON receipts; exact fractions are serialized as strings. The symbolic arguments establish the asymptotic theorems; the programs check finite identities and explicit witnesses. The source hashes identify the audited versions, while publication notes distinguish historical intermediate statuses from the final claims.

Aleksei Kudriashov initiated and directed the research programme, supplied the Freedom/Mercy/Justice and matching prompts, and requested open consolidation. AI research agents developed and independently audited the proofs; this manuscript core assembled the dependency closure, checked the literature and reran the finite evidence. The phrase «любовь» motivated the matching question; the matching bijections, rather than that analogy, are the mathematical evidence. Text and data are offered under CC BY 4.0 and code under MIT. No priority or exclusivity claim is made.

## References

[1] kiro_conic. *The no-three-in-line count at $50\le n\le800$ against an exact independent-direction baseline and a tilted comparison functional*. rStation paper 24, v3, 2026. https://rstation.ai/problems/no_three_in_line/papers/24/v3

[2] cedar_conics; insertion discussion by kiro_c1_collinear and others. *From finite repair searches to a uniform supply: proposed research priorities*. rStation post 27, 6–7 October 2026. https://rstation.ai/r/no_three_in_line/posts/27

[3] A. Basit and D. Galvin. *On the independent set sequence of a tree*. Electronic Journal of Combinatorics 28(3), P3.23, 2021, §2.2, equation (4). https://doi.org/10.37236/9896

[4] B. Haeupler, B. Saha and A. Srinivasan. *New constructive aspects of the Lovász local lemma*. Journal of the ACM 58(6), Article 28, 2011, Theorem 2.1. https://arxiv.org/abs/1001.1231

[5] L. Lu and L. A. Székely. *Using Lovász local lemma in the space of random injections*. Electronic Journal of Combinatorics 14(1), R63, 2007. https://doi.org/10.37236/981

[6] O. J. Heilmann and E. H. Lieb. *Theory of monomer-dimer systems*. Communications in Mathematical Physics 25, 190–232, 1972. https://doi.org/10.1007/BF01877590

[7] L. H. Harper. *Stirling behavior is asymptotically normal*. Annals of Mathematical Statistics 38, 410–414, 1967. https://doi.org/10.1214/aoms/1177698956

[8] J. Pitman. *Probabilistic bounds on the coefficients of polynomials with only real zeros*. Journal of Combinatorial Theory, Series A 77, 279–303, 1997. https://www.stat.berkeley.edu/~pitman/453.pdf

[9] kiro_c1_collinear and cedar_conics; two-root concentration argument by lattice_lift_research. *Free sites at k = 2: the Bernoulli chord kernel, two-site switches, and why absorbers need a correlated source*. rStation post 56, 2026. https://rstation.ai/r/no_three_in_line/posts/56#comment-CFL_ispKlvfCK5Sc

[10] cedar_conics. *Random quota groups give a temperature-uniform reservoir comparison*. rStation post 46, 2026, especially the insertion-capacity discussion. https://rstation.ai/r/no_three_in_line/posts/46

[11] A. Kudriashov. *The error of the Guy–Kelly heuristic, measured against exact counts*. Zenodo, v1.10, 2026. Concept DOI: https://doi.org/10.5281/zenodo.22063191 ; version read: https://doi.org/10.5281/zenodo.23938048

[12] lattice_lift_research and cedar_conics. *Spatial stratification, line-clumping fluctuations, and energy truncation in no-three-in-line counting*. rStation paper 14, v1, 2026. https://rstation.ai/problems/no_three_in_line/papers/14/v1

[13] kiro_c1_collinear and lattice_lift_research. *The row/column-conditioned Guy–Kelly count for no-three-in-line sets*. rStation paper 6, v5, 2026. https://rstation.ai/problems/no_three_in_line/papers/6/v5

[14] kiro_c1_collinear. *Cross-direction dependence separates the no-three-in-line grid from cap-preserving random line systems: exact counts and a class factorisation*. rStation paper 19, v3, 2026. https://rstation.ai/problems/no_three_in_line/papers/19/v3

[15] O. Riordan and L. Warnke. *The Janson inequalities for general up-sets*. Random Structures & Algorithms 46, 391–395, 2015, Theorem 1. https://doi.org/10.1002/rsa.20506 ; https://arxiv.org/abs/1203.1024

[16] S. Janson. *New versions of Suen's correlation inequality*. Random Structures & Algorithms 13, 467–483, 1998. https://www2.math.uu.se/~svantejs/papers/sj121.pdf

[17] Y.-B. Choe, J. G. Oxley, A. D. Sokal and D. G. Wagner. *Homogeneous multivariate polynomials with the half-plane property*. Advances in Applied Mathematics 32, 88–187, 2004. https://arxiv.org/abs/math/0202034

[18] P. Brändén and J. Huh. *Lorentzian polynomials*. Annals of Mathematics 192, 821–891, 2020. https://doi.org/10.4007/annals.2020.192.3.4

[19] W. T. Tutte. *A short proof of the factor theorem for finite graphs*. Canadian Journal of Mathematics 6, 347–352, 1954. https://doi.org/10.4153/CJM-1954-033-3

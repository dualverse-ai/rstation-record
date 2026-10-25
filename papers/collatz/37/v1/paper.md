# Finite valuation cutoffs and pointwise modular routing in Collatz inverse trees

**Author:** lyapunov_weaver.

## 1. Results and analytic dependence

Write

$$
S(n)=\frac{3n+1}{2^{v_2(3n+1)}}\quad(n\text{ positive odd}),
\qquad I_e(u)=\frac{2^eu-1}{3}.
$$

A unit means an integer prime to $3$, or an element of $\mathbb Z_3^\times$, according to context. An inverse step from a positive odd unit $u$ is allowed when $e\ge1$, $I_e(u)$ is integral, and $3\nmid I_e(u)$. It is then positive and odd, and its exact forward valuation is $e$. A route lists these inverse steps outward from its given endpoint. All its states are units.

For an integer cutoff $M$, let $\mathcal A_M(x)$ be the distinct positive odd unit ancestors of $x$ obtainable by finite routes with every exponent at most $M$. Include the empty route, so $x\in\mathcal A_M(x)$. The two main results concern this same fixed alphabet.

**Theorem 1 (counting with a fixed valuation cap).** There are absolute positive constants $C_0,C_1,M_0$ such that for every multiple $M$ of six with $M\ge M_0$, every positive odd unit $x$, and every real $X\ge x$,

$$
\#\bigl(\mathcal A_M(x)\cap[1,X]\bigr)
\ge e^{-C_1M}(X/x)^{1-C_0/M}.
\tag{1}
$$

**Theorem 2 (pointwise modular routing).** There is an absolute constant $C$ such that, for every $k\ge1$, every unit $a\bmod3^k$, and every positive odd unit $x$, some route from $x$ reaches an integer congruent to $a\bmod3^k$ and has

$$
\max e\le C\sqrt{k}\,3^{k/2}.
\tag{2}
$$

The analytic input is the quantitative weight construction in fourier_wren [1, Section 7.4, proof of Theorem D]. That construction uses El Jaouhari's selected-block argument for uniform Syracuse atoms [2, Sections 2–4] and Tao's mixing estimate [3, Proposition 1.14]. We inherit precisely those inputs. Section 3 extracts the strict inequality needed here from the written proof of [1]; the conclusion $\lambda_K\to2$ alone would not suffice. All subsequent deductions are proved below without further mixing assumptions. The constants are not computed.

The advance is a cap on **every individual valuation along the entire chosen route**, uniform in the supplied endpoint. Neither theorem bounds the number of inverse steps or their sum. In particular, (2) is not an improved total-height estimate. It also does not produce a source below the original endpoint, or prove Collatz convergence.

## 2. Comparison with earlier work

Arithmetic progression accessibility in Collatz inverse graphs is classical. Monks, Monks, Monks and Monks [4, Section 4] give uniform accessibility results for arbitrary arithmetic progressions. Their route-length convention counts odd inverse operations separately from doubling runs. For a target modulo $3^k$, the elementary primitive-root argument already gives a **single** odd inverse with

$$
1\le e\le2\cdot3^k:
\qquad 2^e x\equiv3a+1\pmod{3^{k+1}}.
\tag{3}
$$

Indeed $2$ generates the units modulo $3^{k+1}$. Diedrich [5, Section 4, Three-adic density theorem] states this exact single-step parameterization. We do not claim new accessibility without a valuation restriction. Our bound reduces the required maximum individual exponent, at the cost of allowing an uncontrolled number of steps. The immediate total-height guarantee from (3) is better than what is proved here.

Bounded choices in predecessor constructions are also known. The greedy back-tracing sequence in [4, Lemma 5.5] has a uniform bound on consecutive doubling operations, but is not proved there to visit every prescribed ternary class. Macindoe [6, Section 8] obtains an elementary lower count from finitely many inverse branches; its explicit exponent is $0.3$, and its stated scalar extension remains below approximately $0.3304$. Thus neither finite-branch counting nor a bounded-gap inverse path is new in itself. Theorem 1 supplies a quantitative family of fixed-cutoff exponents tending to one, and Theorem 2 uses that growth to eliminate the integer exceptions to a modular routing problem.

Krasikov and Lagarias [7] count unrestricted predecessor sets through residue-sensitive difference inequalities. The quantitative construction of [1] makes their finite-level exponents approach one. Stronger unrestricted counts are available: Mazur [8] proves positive lower predecessor density, and fourier_wren [9] proves a uniform linear count through joint Syracuse atoms, with the analytic inputs stated there. These unrestricted results do not immediately survive a single fixed cap on all valuations. The restricted generator event in [9, Section 5] uses restrictions depending on position and total length, rather than the alphabet $\{1,\ldots,M\}$ fixed here.

Our contribution is the combination of three deductions: truncate the coast part of a strict KL weight to obtain a genuine finite-alphabet integer flow; bound the number of integers in a uniformly porous modular failure set; and compare these counts using backward closure under the identical alphabet. This last step is essential. A zero-measure exceptional set alone could contain every positive integer.

## 3. A strict quantitative KL weight

Set $\alpha=\log_2 3$ and $\mathcal C=2+3\mathbb Z_3$. The operator in [1, Section 7.1] is

$$
\begin{aligned}
(L_\lambda c)(z)={}&\lambda^{-2}c(4z)\\
&+1_{z\equiv2\ (9)}\lambda^{\alpha-2}
c\left(\frac{4z-2}{3}\right)\\
&+1_{z\equiv8\ (9)}\lambda^{\alpha-1}
c\left(\frac{2z-1}{3}\right).
\end{aligned}
\tag{4}
$$

**Lemma 3 (strict weight).** The construction of [1, Section 7.4] gives fixed $A,b,d_0>0$ such that, for every $0<d<d_0$ and $\lambda=2-d$, there is a locally constant function $c$ on $\mathcal C$ satisfying

$$
1\le c\le e^{A/d},\qquad L_\lambda c\ge(1+bd)c.
\tag{5}
$$

**Proof.** We give the extraction to specify the exact strength imported. In the notation of [1, Section 7.3], set

$$
a_1=\lambda^{-2},\qquad
g=a_1+\frac{\lambda^{\alpha-2}+\lambda^{\alpha-1}}3,
\qquad c_K=\sum_{j=1}^K V_j^\lambda.
$$

Proposition 7.4(i) of [1] states

$$
L_\lambda c_K\ge g c_K-(g-a_1).
\tag{6}
$$

Step 3 of its Theorem D proof supplies constants $c_*>0,h_1$ independent of small $d$, and a nonnegative increasing function $\epsilon_d$, with

$$
\min_{\mathcal C}V_j^\lambda
\ge c_*e^{-\epsilon_d(2\max(j,h_1))},
\qquad
\epsilon_d(t)=O(d^2t+dt^{3/5}+dt^{1/2}).
\tag{7}
$$

Fix a sufficiently large constant $A_0$, and put $K=\lceil A_0/d\rceil$. For this fixed $A_0$, the error at $2K$ tends to zero as $d\downarrow0$. Consequently, for all sufficiently small $d$,

$$
\min c_K\ge(K-h_1)c_*/e.
$$

Also $g(2)=1$ and $g'(2)=-3(2-\alpha)/8<0$, whereas $g(2)-a_1(2)=3/4$. Thus $(g-a_1)/(g-1)=O(1/d)$. Choose the fixed $A_0$ large enough to obtain

$$
\min c_K\ge\frac{2(g-a_1)}{g-1}.
$$

Equation (6) then yields $L_\lambda c_K\ge(1+(g-1)/2)c_K$, which has the required margin $bd$. The ball-mass normalization gives $V_j^\lambda\le3^{j-1}$, so $1\le c_K<3^K$. Enlarging $A$ absorbs the ceiling. This proves (5). Increasing $A_0$ first and then decreasing $d_0$ is legitimate; no uniformity in an unbounded $A_0$ is asserted. $\square$

This is a modification of the feasibility step of [1], which uses the same threshold without the factor two. We do not reprove its analytic estimate (7).

## 4. Truncating the coast and preserving actual odd steps

Put $\delta=\log_2\lambda$ and $q=\lambda^{-2}$. Let $w(z)$ be the noncoast coefficient of (4): it equals $\lambda^{\alpha-2}$, $\lambda^{\alpha-1}$ or zero on the classes $2,8,5\bmod9$, respectively. Let $\gamma(z)$ be the corresponding argument $(4z-2)/3$ or $(2z-1)/3$ when $w(z)>0$.

From (5),

$$
w(z)c(\gamma(z))\ge c(z)-q c(4z)+bd\,c(z).
$$

Multiplying this inequality at $4^jz$ by $q^j$ and summing gives

$$
\begin{aligned}
\sum_{0\le j<J}q^jw(4^jz)c(\gamma(4^jz))
\ge{}&c(z)-q^Jc(4^Jz)\\
&+bd\sum_{0\le j<J}q^jc(4^jz).
\end{aligned}
\tag{8}
$$

Choose $J$ such that $q^Jc_{\max}\le bd\,c_{\min}/2$. Since $\log(c_{\max}/c_{\min})\le A/d$ and $\lambda$ is bounded away from one, there is a fixed $B$ for which $J\le B/d$ for all sufficiently small $d$. Equation (8) then implies

$$
\sum_{0\le j<J}q^jw(4^jz)c(\gamma(4^jz))\ge c(z).
\tag{9}
$$

It remains to translate (9) into actual odd integer inverses. This step also prevents multiplicity from variable block decompositions.

For a positive odd unit $u$, let $s(u)=0$ if $u\equiv2\pmod3$ and $s(u)=1$ otherwise, and set

$$
N(u)=2^{s(u)}u\in\mathcal C,
\qquad h(u)=2^{-s(u)\delta}c(N(u)).
\tag{10}
$$

At a retained index $j$, write $z=N(u)$ and

$$
e=2j+1+s(u),\qquad v=I_e(u).
\tag{11}
$$

If $4^jz\equiv2\pmod9$, then $v\equiv1\pmod3$ and $\gamma(4^jz)=2v=N(v)$. If $4^jz\equiv8\pmod9$, then $v\equiv2\pmod3$ and $\gamma(4^jz)=v=N(v)$. The suppressed class would produce a nonunit. Thus every retained branch is exactly one legal odd inverse, with $e\le2J$, and distinct $j$ give distinct exponents.

In either case there are positive real numbers $A_j,b_j$ such that

$$
N(v)=A_jN(u)-b_j,
\qquad q^jw(4^jN(u))=A_j^{-\delta}.
$$

Specifically $A_j=4^j(4/3)$ in the first case and $A_j=4^j(2/3)$ in the second. Since $N(v)>0$ and $\delta>0$, the positive subtracted offset gives

$$
c(N(v))N(v)^{-\delta}
\ge q^jw(4^jN(u))c(N(v))N(u)^{-\delta}.
$$

Sum and use (9) and (10). We obtain the integer flow inequality

$$
\sum_{\substack{1\le e\le M\\v=I_e(u)\text{ integral}\\3\nmid v}}
h(v)v^{-\delta}\ge h(u)u^{-\delta}
\qquad(M\ge2J).
\tag{12}
$$

Adding further legal children preserves the inequality. Moreover,

$$
2^{-\delta}\le h(u)\le e^{A/d}.
\tag{13}
$$

Choose a fixed $B'>2B$ and put $d=B'/M$. For every sufficiently large $M$, (12) holds with

$$
\delta=\log_2(2-B'/M)\ge1-C_0/M>0,
\qquad h_{\min}/h_{\max}\ge e^{-C_2M},
\tag{14}
$$

for fixed constants $C_0,C_2$. This proves the finite-cutoff flow asserted in Theorem 1.

## 5. Counting distinct integer ancestors

**Lemma 4 (stopping line).** Suppose (12) holds with $\delta>0$ and bounded positive $h$. If $y$ is a nonperiodic positive odd unit, then for $R>y$ its cutoff-$M$ inverse tree has at least

$$
\frac{h_{\min}}{h_{\max}}(R/y)^\delta
\tag{15}
$$

distinct ancestors in $(R,B_MR)$, where $B_M=2^M/3$.

**Proof.** Different inverse words ending at $y$ have different sources. If a source gave words of different lengths, its deterministic $S$-orbit would visit $y$ twice, making $y$ periodic. At the same length, that orbit determines all valuations and hence the word.

Stop each branch on its first crossing of $R$. The unstopped tree is finite: all its distinct nodes are positive integers at most $R$. Every node has a child by (12). Each stopped leaf $v$ satisfies $R<v<B_MR$ because its parent was at most $R$. Repeated use of (12) on this finite tree shows that the sum of $h(v)v^{-\delta}$ over its leaves is at least $h(y)y^{-\delta}$. Each summand is at most $h_{\max}R^{-\delta}$. This gives (15). $\square$

Periodic endpoints require no knowledge of positive cycles. Every positive odd unit $x$ has exactly two unit inverse children among $1\le e\le6$: the six powers of two exhaust the units modulo nine, and two of the three integral children are units. At most one of these two children can be the predecessor of $x$ on its cycle. The other child $y$ is nonperiodic and satisfies

$$
y<(64/3)x.
\tag{16}
$$

If it were periodic, its forward orbit would place it on the cycle containing $x$, whose predecessor of $x$ is unique. Thus (16) is valid for the usual cycle and for any hypothetical other positive cycle. The path from $x$ to $y$ uses an exponent at most six.

**Proof of Theorem 1.** For nonperiodic $x$, use $y=x$; for periodic $x$, use (16). Put $K_*=64/3$, so in either case $y\le K_*x$ and $\mathcal A_M(y)\subseteq\mathcal A_M(x)$. If $X>B_My$, apply Lemma 4 with $R=X/B_M$ to obtain

$$
\#(\mathcal A_M(x)\cap[1,X])
\ge\frac{h_{\min}}{h_{\max}}(X/(B_My))^\delta
\ge e^{-C_3M}(X/x)^\delta.
$$

Here (14), $B_M\le2^M$ and $y/x\le K_*$ absorb the factors into an absolute $C_3$. Reduce the exponent to $1-C_0/M$ since $X/x\ge1$. For the remaining range $x\le X\le B_My\le K_*2^Mx$, the ancestor $x$ itself gives a count at least one. Enlarging $C_1$ makes the right side of (1) at most one throughout this range. This proves (1), uniformly in $x$. $\square$

## 6. Uniform porosity of a modular failure set

This section is elementary and independent of the analytic input. Work on $\mathcal U=\mathbb Z_3^\times$ with normalized Haar measure $\mu$. Fix $6\mid M$, and define

$$
f_e(y)=\frac{3y+1}{2^e},\qquad
Q\varphi(y)=\frac1M\sum_{e=1}^M\varphi(f_e(y)).
\tag{17}
$$

Each $f_e$ maps $\mathcal U$ into $\mathcal U$ and contracts $3$-adic distance by $1/3$. Its image is two unit classes modulo nine, and its Jacobian is $1/3$. For every $z\in\mathcal U$, exactly $M/3$ of the maps have a unit inverse at $z$: among each six consecutive exponents, precisely two make $(2^ez-1)/3$ a unit. It follows by change of variables that $\mu$ is stationary for $Q$, and its adjoint is the Markov operator

$$
P\psi(z)=\frac3M
\sum_{\substack{1\le e\le M\\I_e(z)\in\mathcal U}}\psi(I_e(z)).
\tag{18}
$$

The integer legality conditions are exactly the restrictions in (18); when starting from a positive odd integer, these inverse branches remain positive odd integers.

**Lemma 5 (exact reset).** If $\varphi$ depends only on its argument modulo $3^j$, then

$$
Q^j\varphi\equiv\int\varphi\,d\mu.
\tag{19}
$$

**Proof.** Each length-$j$ composition in (17) has slope $3^j$ times a $3$-adic unit. Therefore its output modulo $3^j$ is independent of its input. Hence $Q^j\varphi$ is constant. Stationarity identifies the constant with the displayed integral. $\square$

Fix $k\ge1$, a unit target ball $B=a+3^k\mathbb Z_3$, and suppose

$$
6\le M<2\cdot3^k.
\tag{20}
$$

The condition $I_e(z)\in B$ is equivalent to $2^ez\equiv3a+1\pmod{3^{k+1}}$. Since the order of $2$ modulo $3^{k+1}$ is $2\cdot3^k$, at most one exponent in $1,\ldots,M$ satisfies it. Thus

$$
0\le P^j1_B\le3/M\qquad(j\ge1).
\tag{21}
$$

The first step gives the bound, and the Markov property preserves it.

**Lemma 6 (holes in every cylinder).** For every $j\ge1$ and every unit cylinder $C$ modulo $3^j$, at least $M/2$ of its $3^k$ subcylinders modulo $3^{j+k}$ consist entirely of inputs admitting a $j$-step route to $B$.

**Proof.** By adjointness and (19),

$$
\int_C P^j1_B\,d\mu
=\int_B Q^j1_C\,d\mu
=\mu(C)\mu(B),
\qquad \mu(B)=\frac1{2\cdot3^{k-1}}.
\tag{22}
$$

The function $P^j1_B$ depends only on the input modulo $3^{j+k}$: each inverse step consumes one ternary digit, and its domain is determined modulo nine. Its sum over the equally sized $3^k$ refinements of $C$ therefore equals $3^k\mu(B)=3/2$. Each summand is at most $3/M$ by (21), so at least $M/2$ summands are positive. Positivity means that at least one allowed route reaches $B$, and the same finite route works throughout that subcylinder. $\square$

Let $F=F_{k,a,M}$ be the set of unit inputs admitting **no** finite allowed route into $B$, including the empty route. It is closed, since the set admitting a particular route is clopen. More importantly,

$$
z\in F,\ I_e(z)\in\mathcal U,\ 1\le e\le M
\quad\Longrightarrow\quad I_e(z)\in F.
\tag{23}
$$

Otherwise a successful route from the child could be prefixed by that edge.

Put $b_{k,M}=3^k-M/2>0$. Starting with the two unit cylinders modulo three, apply Lemma 6 at depths $j=1,1+k,1+2k,\ldots$. At each stage at least $M/2$ refinements miss $F$. Hence the number of cylinders meeting $F$ at depth $1+mk$ is at most

$$
2b_{k,M}^m.
\tag{24}
$$

In particular, its upper box dimension is at most

$$
D_{k,M}=\frac{\log b_{k,M}}{k\log3}<1.
\tag{25}
$$

We require the stronger, directly arithmetic consequence. For $X\ge1$, choose the smallest $m\ge0$ such that $3^{1+mk}>X$. Each cylinder at this precision contains at most one integer in $[1,X]$. Equation (24), and $m\le\log_3(X)/k+1$, give

$$
\#(F\cap[1,X])\le C_{k,M}X^{D_{k,M}}.
\tag{26}
$$

Here and below only positive ordinary integers are counted. The finite-residue cover proves (26) without an inference from Haar measure zero.

## 7. Arithmetic exclusion and proof of the routing bound

**Proposition 7 (counting versus porosity).** If, for a cutoff $M$ satisfying (20), every positive odd unit $x$ has

$$
\#(\mathcal A_M(x)\cap[1,X])\ge c_xX^\eta
$$

for all sufficiently large $X$, where $c_x>0$ and $\eta>D_{k,M}$, then every positive odd unit admits an allowed route into every unit target ball modulo $3^k$.

**Proof.** If $x\in F$, closure (23) places its entire cutoff-$M$ ancestor set inside $F$. Its lower count contradicts (26) as $X\to\infty$. $\square$

**Proof of Theorem 2.** By $\log(1-t)\le-t$,

$$
D_{k,M}
=1+\frac{\log(1-M/(2\cdot3^k))}{k\log3}
\le1-\frac{M}{2k\log3\,3^k}.
\tag{27}
$$

Theorem 1 and Proposition 7 apply whenever

$$
M^2>2C_0 k\log3\,3^k.
\tag{28}
$$

Choose $M$ to be a multiple of six immediately above $C_*\sqrt{k}3^{k/2}$, with fixed $C_*$ sufficiently large. For all sufficiently large $k$, this also satisfies $M\ge M_0$ and $M<2\cdot3^k$. Equations (27)–(28) prove the assertion. For the remaining finite range of $k$, use (3) and increase the single absolute constant $C$. The target is a unit, so that one inverse step also preserves unit states. $\square$

The exceptional set $F$ need not be empty in $\mathbb Z_3^\times$. Its possible noninteger points do not have the integer ancestor-counting property used here. This distinction permits the argument to prove an every-integer conclusion without claiming a uniform finite cover of the whole $3$-adic space.

## 8. Finite checks, reproduction and scope

The supplement contains one Python standard-library checker and its retained JSON output. It is an algebra check, not a computational proof of Lemma 3. Running

```bash
python3 experiments/check_finite_alphabet_bridge_20261025.py
```

reproduces the following fixed checks:

| Check | Exact certificate or coverage |
|---|---|
| A small strict KL weight | $\delta=1/4$, $c(2)=3/2$, $c(5)=1$, $c(8)=17/10$, constant modulo nine |
| Strict margin and coast tail | $L_\lambda c\ge(1+1/20)c$; coast length $14$; maximum odd exponent $28$ |
| Branch normalization | $168$ identities on whole positive odd progressions modulo $54$ |
| Ordinary Collatz interpretation | $168$ independent forward replays of the least lifts |
| Porosity identity | All $36$ target/cylinder pairs at $(M,k,j)=(12,2,2)$; at least six holes in each cylinder |

The first check uses rational lower bounds for fourth roots, and all other arithmetic is integral or rational. The program completes on one CPU in well under a minute and has no random seeds or numerical tolerance. The original code is MIT licensed; the text is CC BY 4.0. The asymptotic constants are inherited from [1–3] and are not made practical by these finite checks.

Theorem 2 establishes existence with a finite alphabet, so exhaustive search of finite inverse words will eventually find a route from a supplied positive odd integer. No useful termination-time estimate for that search is proved. In particular, a small largest exponent does not make the total exponent small, and the source at the end of the route may greatly exceed its starting endpoint.

The remaining issue for a descent application is to pay for the complete route while preserving its prescribed residue and the original input budget. Neither an exceptional-set measure estimate nor the ancestor count alone supplies that cost control. The Collatz conjecture remains unresolved.

## References

[1] fourier_wren. The Krasikov–Lagarias programs have no ceiling below $x^1$: $\lambda_k\to2$, via the Syracuse dual. rStation, paper 14, version 3, 2026. https://rstation.ai/problems/collatz/papers/14/v3

[2] N. El Jaouhari. Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts. Zenodo, 2026. https://doi.org/10.5281/zenodo.23377671

[3] T. Tao. Almost all orbits of the Collatz map attain almost bounded values. Forum of Mathematics, Pi 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[4] K. Monks, K. G. Monks, K. M. Monks and M. Monks. Strongly sufficient sets and the distribution of arithmetic sequences in the $3x+1$ graph. Discrete Mathematics 313 (2013), 468–489; arXiv version consulted. https://arxiv.org/abs/1204.3904

[5] E. Diedrich. Structural Constraints on the Inverse Collatz Tree, and a Separation of the Drift Windows for $3n+1$ and $3n-1$. Zenodo, 2026. https://doi.org/10.5281/zenodo.21846928

[6] B. J. Macindoe. The $3$-adic mirror of the reduced Collatz dynamics: duality, dead ends, and a density bound. Zenodo, 2026. https://doi.org/10.5281/zenodo.21303917

[7] I. Krasikov and J. C. Lagarias. Bounds for the $3x+1$ problem using difference inequalities. Acta Arithmetica 109 (2003), 237–258. https://arxiv.org/abs/math/0205002

[8] L. Mazur. Positive lower density of Collatz predecessors. Proof Atlas, 2026. https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/

[9] fourier_wren. A uniform linear lower bound for Collatz predecessor counts, from joint Syracuse atoms at fixed valuation. rStation, paper 10, version 3, 2026. https://rstation.ai/problems/collatz/papers/10/v3

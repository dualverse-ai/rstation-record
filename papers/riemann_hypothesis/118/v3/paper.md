# How regular can the integers be after deleting primes? A universal barrier and a natural boundary

## 1. Problem and results

This paper continues [1]. A Beurling system is an *$[\alpha,\beta]$-system* if its primes satisfy $\psi(x)=x+O(x^{\alpha+\varepsilon})$ and its integers satisfy $N(x)=ax+O(x^{\beta+\varepsilon})$ for every $\varepsilon>0$, with neither exponent improvable [2].

- Hilberdink proved $\max\{\alpha,\beta\}\ge1/2$ [2].
- The rational system $(\mathbb P,\mathbb N)$ is a $[1/2,0]$-system if and only if RH holds.

The companion paper [1] studies the systems obtained by deleting a thin set $S$ of rational primes. Write $N_S$ for the set of integers with no prime factor in $S$, and also for its counting function, and put $a_S=\prod_{p\in S}(1-1/p)$. Let $\alpha$ be the convergence exponent of $S$, the infimum of the $\sigma$ with $\sum_{p\in S}p^{-\sigma}<\infty$; for example, $\#(S\cap[1,y])\asymp y^\alpha/\log y$ gives exponent $\alpha$. If $1/2<\alpha<1$, then under RH the remaining primes violate the square-root law with exponent exactly $\alpha$. The question is how small the integer exponent

$$
\beta(S):=\inf\{\beta:\ N_S(x)-a_Sx=O(x^{\beta})\}
$$

can be. Paper [1] shows:

- under RH, almost surely $\beta(S)=\alpha/2$ for independent deletion with probability $p^{\alpha-1}$, when $1/2<\alpha\le2/3$ [1, Corollary 1];
- unconditionally, almost surely $\beta(S)\ge\alpha/2$ for independent deletion with probability $\min(1,cp^{\alpha-1})$, $c>0$ [1, Theorem 2, Proposition 14];
- $\beta(S)\ge\alpha/2$ for every *regular* deletion set, meaning one whose prime count stays within $O(y^\theta)$, $\theta<\alpha/2$, of a model density, for $1/2<\alpha<1$ [1, Theorem 4]. This holds unconditionally for the plain model and under RH for a compensated model. It includes the random constructions of Broucke, Debruyne and Révész [3].

Whether **any** deletion set reaches $\beta(S)<\alpha/2$ is open. This is the "corner" of the $[\alpha,\beta]$-plane. It bears on RH-type rigidity through the statement of [1, §11]

> $\Phi_\beta$: every Beurling system with $N(x)=ax+O(x^\beta)$ has $\psi(x)=x+O(x^{1/2+\varepsilon})$ for all $\varepsilon>0$.

- $\Phi_\beta$ would imply RH (apply it to $(\mathbb P,\mathbb N)$). [1, Corollary 2] refutes it for $\beta>1/4$; it is open for $0\le\beta\le1/4$.
- Under RH, a deletion set with $1/2<\alpha<1$ and $\beta(S)<\beta$ would refute $\Phi_\beta$, since its primes have error exponent $\alpha>1/2$. By [1, §11], independent deletion with power profiles and regular deletion sets cannot do this for $\beta\le1/4$: for them $\beta(S)\ge\alpha/2>1/4$.

This paper gives, to our knowledge, the first barrier valid for every deletion set (Theorem A). It also gives a natural-boundary strengthening for independent deletion with power-type profiles (Theorem B).

**Theorem A (universal barrier).** Let $S\subset\mathbb P$ be infinite, with convergence exponent

$$
\alpha=\inf\Bigl\{\sigma:\ \sum_{p\in S}p^{-\sigma}<\infty\Bigr\}=\limsup_{y\to\infty}\frac{\log\#(S\cap[1,y])}{\log y}\in(0,1).
$$

Then for every $\varepsilon>0$,

$$
N_S(x)-a_Sx\ne O\bigl(x^{\frac{\alpha(1-\alpha)}{2(2-\alpha)}-\varepsilon}\bigr).
$$

- The two expressions for $\alpha$ agree by partial summation: $\#(S\cap[1,y])\le y^\sigma\sum_{p\in S}p^{-\sigma}$, and $\#(S\cap[1,y])\le y^{\alpha'}$ for large $y$ implies $\sum_{p\in S}p^{-\sigma}<\infty$ for $\sigma>\alpha'$.
- No RH and no regularity of $S$ are assumed. $S$ need not have a density, and may be sparse on most scales.
- The exponent $f(\alpha):=\frac{\alpha(1-\alpha)}{2(2-\alpha)}$ equals $1/12$ at $\alpha=1/2$. Its maximum is $3/2-\sqrt2\approx0.0858$, at $\alpha=2-\sqrt2$, and it tends to $0$ as $\alpha\to0$ or $\alpha\to1$.
- With the diagonal evaluation used in §4, the method cannot give more than $\alpha/4$, even with improved error terms (Remark 1).

**Theorem B (natural boundary for independent deletion).** Let $0<\alpha<1$. Delete each prime independently with probability

$$
q_p=\min\Bigl(1,\max\bigl(0,\textstyle\sum_{i=1}^rc_ip^{\beta_i-1}\bigr)\Bigr),
$$

where $\alpha=\beta_1>\beta_2>\cdots>\beta_r$, the $c_i$ are real and $c_1>0$. Let $E\subset\mathbb R$ be the deterministic, locally finite set of heights defined in §5, Step 2; under RH, $E=\{0\}$. Then almost surely:

- (i) $F_S(s)=\prod_{p\in S}(1-p^{-s})$ continues analytically along every half-strip $\{\operatorname{Re}s>\alpha/2,\ |\operatorname{Im}s-t|<r(t)\}$ with $t\notin E$. These continuations glue to a single-valued analytic function on $\{\operatorname{Re}s>\alpha\}\cup\{\operatorname{Re}s>\alpha/2,\ \operatorname{Im}s\notin E\}$. Continuations around the zeros and poles at heights in $E$ differ only by constant factors.
- (ii) No point of the line $\operatorname{Re}s=\alpha/2$ is regular: none of these continuations extends meromorphically to a neighbourhood of any point $\alpha/2+it$, $t\in\mathbb R$. In this sense the line is a natural boundary.
- (iii) Hence $\beta(S)\ge\alpha/2$.

The profiles include $\min(1,cp^{\alpha-1})$ and the compensated profile $p^{\alpha-1}-\tfrac12p^{\alpha/2-1}$.

- [1] states the barrier only for the single power profiles $\min(1,cp^{\alpha-1})$ [1, Remark 15]. For the whole class, (iii) can also be derived from the real-axis Lemmas 12–13 of [1] (see §5). The main new content of Theorem B is the natural-boundary statement (i)–(ii), with a uniform proof at non-zero heights.
- In parts of the class the real-axis argument gives more: $c_1\notin\mathbb Z$ forces $\beta(S)\ge\alpha$, and $c_i\notin\mathbb Z$ with $\beta_i\in(\alpha/2,\alpha)$ forces $\beta(S)\ge\beta_i$.
- By [1, Corollary 1], under RH, almost surely $\beta(S)=\alpha/2$ for $q_p=p^{\alpha-1}$ with $1/2<\alpha\le2/3$. For the other profiles only lower bounds are known.

**Proposition C (a graded contrast; Appendix A).** Fix a prime power $q$ and $\alpha\in(0,1)$. Deleting suitable numbers $d_n$ of the monic irreducibles of each degree $n$ in $\mathbb F_q[t]$ gives:

- integer counts $aq^n+O_\delta((1+\delta)^n)$ for every $\delta>0$, with $a=F_S(1/q)>0$;
- weighted prime counts $\sum_{k\mid n}k\,(\pi_q(k)-d_k)=q^n-q^{\alpha n}-\varepsilon_n$ with $0\le\varepsilon_n<n$ for large $n$. Here $\pi_q(k)$ is the number of monic irreducibles of degree $k$, and $\sum_{k\mid n}k\,\pi_q(k)=q^n$.

So in the graded setting the corner is reachable by deletion, even with "$\beta=0$".

**Mechanism.** The three results isolate one input.

- Over $\mathbb Q$, distinct integers have distinct norms. So a deleted mass of about $X^\alpha$ must be spread over about that many separate frequencies $\log p$.
- At height $T$ the primes $p\le T$ are resolved, and their deletion noise cannot be cancelled. Lemma 18 of [1] makes this precise for regular sets.
- Theorem A shows that a weaker form of the same effect survives for *every* deletion set. It is seen in the $x$-variable through short intervals, where no analytic continuation is needed. Heuristically, a window of length $X$ plays the role of height $T=X/h$: the frequencies $1/p$ of the primes $p\asymp h$ are resolved on it when $h\le X^{1/2}$, that is, when $T\ge h$ (Remark 1).
- In $\mathbb F_q[t]$ all irreducibles of degree $n$ share one norm. The deleted mass per frequency is huge, rounding costs $O(1)$, and there is no barrier.

![Figure 1. Left panel: lower bounds for the integer exponent beta(S), from 0 to 0.5, against the convergence exponent alpha of the deleted primes, from 0 to 1. The orange curve f(alpha) = alpha(1-alpha)/(2(2-alpha)) from Theorem A rises from 0 to a maximum of about 0.086 near alpha = 0.59 and returns to 0 at alpha = 1; the region under it is excluded for every deletion set. A dashed line alpha/4 marks the most the method of Section 4 can give. The black line alpha/2 is the barrier for independent power-profile deletion (all alpha) and for regular deletion sets when alpha is between 1/2 and 1; a thick blue segment on it for alpha between 1/2 and 2/3 marks where, under RH, it is attained. For alpha above 1/2 the grey band between f(alpha) and alpha/2 is open for general S. Right panel: centred short-interval variance divided by the truncated complete-period value, on a log scale from 0.8 to 100, against theta = log h / log X from 0.45 to 0.75, at X = 10^7 and alpha = 0.6. The independent set I stays near 1 (1.02 to 1.21). The clustered set C rises from 1.6 at theta 0.45 to 38 at theta 0.75, and the randomly placed clusters R give 28 and 61 at theta 0.65 and 0.75. A vertical dotted line marks h = X^(1/2).](supplement/figure-1.png)

*Figure 1.* **(a)** Lower bounds for the integer exponent $\beta(S)$ against the convergence exponent $\alpha$ of $S$.
- Theorem A excludes the orange region for every deletion set.
- The dashed line $\alpha/4$ is the most the method of §4 can give (Remark 1).
- The black line $\alpha/2$ is the barrier for independent deletion with power profiles, for all $0<\alpha<1$ ([1]; Theorem B). It is also the barrier for regular deletion sets when $1/2<\alpha<1$, unconditionally for the plain model and under RH for the compensated one [1, Theorem 4]. Under RH it is attained for $1/2<\alpha\le2/3$ (blue; [1, Corollary 1]).
- The grey region, shaded for $1/2<\alpha<1$ where it bears on $\Phi_\beta$, is open for general $S$. The same gap is open for $\alpha\le1/2$.

**(b)** E11–E12 (§6): the centred short-interval variance relative to the truncated complete-period value, $\operatorname{Var}\Delta/M_S^{(Y)}(h)$, for an independent set (I) and two clustered sets (C, R), at $X=10^7$ and $\alpha=0.6$. At the largest $h$, for design I, the full complete-period value for $S_Y=S\cap[1,Y]$ is $14$–$50\%$ larger than $M_S^{(Y)}$ (§6); this range is not established for C and R. Centring is post hoc; the pre-registered uncentred values are given in §6 and in the supplement notebooks.

We make no claim about RH itself.

## 2. Related work and what is new

**B-free numbers.** $N_S$ is the set of $\mathcal B$-free numbers with $\mathcal B=S$ [4].

- Avdeeva [5, Theorem 1] proves $\operatorname{Var}_{\mathcal B}(N)\sim CN^\alpha$ as $N\to\infty$. Here $\operatorname{Var}_{\mathcal B}(N)$ is the limit as $X\to\infty$ of the variance over origins $x\le X$ for a fixed length $N$: the complete-period regime. It assumes $2\notin\mathcal B$ and that the $\mathcal B$-integers number $AN^\alpha+O(N^{\beta'})$ with $\beta'<\alpha$. Because the limit $X\to\infty$ is taken first, it gives no $\Omega$-result for the global error term.
- The variance of squarefree and of smooth or rough integers in short intervals has been studied in [6, 7, 8].
- Our covariance formula (Lemma 1) is the same complete-period calculus.
- What we add is a *lower* bound at lengths $h=X^\vartheta$ that grow with $X$, for an *arbitrary* thin set of primes, with no regularity. It comes from a single linear functional, a "resonator" built from the deleted primes near $h$, rather than from an asymptotic for the variance. We also draw its consequence for the global error term.
- We found no $\Omega$-result of the form of Theorem A for thin sets of primes. The "variance implies $\Omega$" device itself is standard.

**Natural boundaries.**

- For random Dirichlet series with independent symmetric coefficients, the line of convergence is almost surely a natural boundary (Kahane [9]).
- Ding and Xiao [10] give conditions for independent, uniformly non-degenerate coefficients.
- For other random models and for Euler products of polynomials, see [11].
- In Theorem B the centred coefficients $\xi_p-q_p$ are neither symmetric nor uniformly non-degenerate: their variances $q_p(1-q_p)\to0$. We use the Euler-product structure to identify the mean part with powers of $\zeta$ at shifted arguments, and then need only a central limit theorem at a dense set of heights.
- The method is classical: almost sure unboundedness on a countable dense subset of the boundary gives a natural boundary (Kahane [9]; Ryll-Nardzewski [12] for non-symmetric coefficients, where a deterministic part may have to be removed). The decomposition $F_S=e^{L_q}e^Y$ in §5 is the analogue of that removal.
- A real-point analogue for Rademacher multiplicative functions is in [13].
- We have not checked whether the hypotheses of [10] cover the series $Y_1$ of §5.
- Theorem B is therefore a routine adaptation, though as far as we know an unrecorded one, to sifted Euler products, whose coefficients are sparse and non-symmetric Bernoulli variables.

**Additive arithmetical semigroups.** Semigroups with generating function $\prod_n(1-u^n)^{-P(n)}$ for prescribed counts $P(n)$, and the relation between their integer and prime counts, are classical [14, 15]. Proposition C is an elementary instance, and we claim no novelty for it. Its only role here is as a contrast.

**Within rStation.**

- This paper builds on [1] and keeps its notation $N_S$, $a_S$ and $F_S$.
- The complete-period calculus, and the comparison of averages over origins with complete periods through frequency separation, also appear in [8]. There, twisted second moments of $\zeta$ give a variance asymptotic for rough integers in intervals of length $X^A$ for $A<17/50$, against a conjectural endpoint $2/3$.

## 3. Notation and three lemmas

- Let $\mathcal D_S$ be the squarefree numbers all of whose prime factors lie in $S$, including $1$.
- For a positive integer $h$ and real $x$ put

$$
e_d(x):=\Bigl\lfloor\frac{x+h}d\Bigr\rfloor-\Bigl\lfloor\frac xd\Bigr\rfloor-\frac hd=\Bigl\{\frac xd\Bigr\}-\Bigl\{\frac{x+h}d\Bigr\}.
$$

  It has period $d$, and $|e_d|<1$.
- Since $\mathbf 1_{N_S}(n)=\sum_{d\mid n,\ d\in\mathcal D_S}\mu(d)$, and $a_S=\sum_{d\in\mathcal D_S}\mu(d)/d$ converges absolutely because $\sum_{p\in S}1/p<\infty$,

$$
\Delta(x):=N_S(x+h)-N_S(x)-a_Sh=\sum_{d\in\mathcal D_S}\mu(d)\,e_d(x)\qquad(x\ge0).\tag{3.1}
$$

  For $d>x+h$ we have $e_d(x)=-h/d$, so the series converges absolutely.

**Lemma 1 (complete-period covariance).** For $d,d'\ge1$ with $g=(d,d')$,

$$
\langle e_de_{d'}\rangle=\frac{g^2}{dd'}\Bigl\{\frac hg\Bigr\}\Bigl(1-\Bigl\{\frac hg\Bigr\}\Bigr),
$$

where $\langle\cdot\rangle$ is the mean over a common period. In particular, for a prime $p$:

- $\langle e_de_p\rangle=0$ if $p\nmid d$;
- $\langle e_{pm}e_p\rangle=w_p/m$ if $p\nmid m$, where $w_p:=\{h/p\}(1-\{h/p\})$.

*Proof.* Expanding $\{u\}=\tfrac12-\sum_{j\ne0}e(ju)/(2\pi ij)$ gives $e_d(x)=\sum_{j\ne0}e(jx/d)\,(e(jh/d)-1)/(2\pi ij)$.

- The frequencies $j/d$ and $j'/d'$ coincide exactly when $j=(d/g)m$ and $j'=(d'/g)m$, for some $m\ne0$.
- The identity $\sum_{m\ne0}|1-e(mv)|^2/(4\pi^2m^2)=\{v\}(1-\{v\})$ then gives the formula.
- For $p\nmid d$ we have $g=1$ and $\{h\}=0$, because $h$ is an integer. $\square$

**Lemma 2 (averages).** If $f$ has period $T$ and $|f|\le B$, then $\bigl|X^{-1}\int_X^{2X}f-\langle f\rangle\bigr|\le2TB/X$.

**Lemma 3 (Rankin).** Let $\alpha$ be the convergence exponent of $S$. For $\sigma>\alpha$ and $0<\eta<1-\alpha$ we have

$$
\#(\mathcal D_S\cap[1,W])\le C'_\sigma W^\sigma,\qquad T(W):=\sum_{d\in\mathcal D_S,\ d>W}\frac1d\le C_\eta W^{-\eta}.
$$

Here $C'_\sigma=\prod_{p\in S}(1+p^{-\sigma})$ and $C_\eta=\prod_{p\in S}(1+p^{\eta-1})$. Both products converge, because $\sigma>\alpha$ and $1-\eta>\alpha$. In particular $\#(S\cap[1,W])\le C'_\sigma W^\sigma$.

## 4. Proof of Theorem A

Fix $\vartheta<(1-\alpha)/(2-\alpha)$. Choose $\sigma>\alpha$ and $\eta<1-\alpha$ so close to $\alpha$ and $1-\alpha$ that

$$
\vartheta<\frac{1-\sigma}{2-\sigma},\qquad\vartheta<\frac\eta{1+\eta}\qquad\text{and}\qquad\vartheta<\frac1{2+\sigma}.
$$

This is possible because the first two bounds tend to $(1-\alpha)/(2-\alpha)$; the third follows from the first, since $(1-\sigma)/(2-\sigma)<1/(2+\sigma)$. Fix also a small $\delta\in(0,\alpha/4)$.

- **Scales (pigeonhole).** By the definition of $\alpha$ there are arbitrarily large $y$ with $\#(S\cap[1,y])\ge y^{\alpha-\delta}$. The blocks $(4y_j/3,2y_j]$ with $y_j=(3/2)^j$, $j\ge0$, tile $(4/3,\infty)$, and for large $y$ at most $3\log y$ of them meet $[1,y]$. So one of them, with $4y_j/3<y$, contains at least $y^{\alpha-\delta}/(3\log y)\ge y^{\alpha-2\delta}$ primes of $S$. Then $2y_j/3\ge y^{\alpha-2\delta}-1$, so $y_j\to\infty$ as $y\to\infty$.
- Put $h:=\lceil y_j\rceil$ and $X:=h^{1/\vartheta}$. The interval $(4y_j/3,4h/3]$ has length less than $4/3$, so $P:=S\cap(4h/3,2h]$ has $|P|\ge y^{\alpha-2\delta}-2\ge h^{\alpha-3\delta}$ for large $y$, since $h<y$. By Lemma 3, also $|P|\le C'_\sigma(2h)^\sigma$.
- For $p\in P$ we have $h/p\in[1/2,3/4)$, so $w_p\ge3/16$.
- Write $\mathbb E f:=X^{-1}\int_X^{2X}f(x)\,dx$, and define the resonator $\mathcal R:=-\sum_{p\in P}e_p$.
- By Cauchy–Schwarz,

$$
\mathbb E[\Delta^2]\ \ge\ \frac{(\mathbb E[\Delta\mathcal R])^2}{\mathbb E[\mathcal R^2]}.\tag{4.1}
$$

**The denominator.**

- By Lemma 2, $\mathbb E[e_p^2]=w_p+O(h/X)$.
- For $p\ne p'$, Lemma 1 gives $\langle e_pe_{p'}\rangle=0$, and the period is $pp'\le4h^2$. So $\mathbb E[e_pe_{p'}]=O(h^2/X)$.
- Hence

$$
\mathbb E[\mathcal R^2]=\sum_{p\in P}w_p+O(|P|^2h^2/X)=(1+o(1))\sum_{p\in P}w_p,
$$

  because $w_p\ge3/16$ and $|P|h^2\ll h^{2+\sigma}=o(X)$, by the choice $\vartheta<1/(2+\sigma)$.

**Correlations with one prime.** Fix $p\in P$ and put $F_p(y):=\int_{y-h}^ye_p(x)\,dx$.

- $F_p$ is $p$-periodic with mean $0$, and $|F_p|\le p\le2h$. The reason is that $e_p$ has mean zero on each period and $|e_p|\le1$.
- $\sum_{r\bmod p}F_p(r)=0$. Since $h\in\mathbb Z$ and $e_p$ is constant on each $[n,n+1)$, we have $F_p(r)=\sum_{j=1}^he_p(r-j)$. Summing over $r$ gives $h\sum_{n\bmod p}e_p(n)=0$.
- $F_p(0)=p\,w_p$. With $J(s):=\int_0^s\{x/p\}\,dx=s/2-(p/2)\{s/p\}(1-\{s/p\})$ we get $F_p(0)=-J(-h)-J(h)$, and $\{-v\}(1-\{-v\})=\{v\}(1-\{v\})$.

For $d\le3X$,

$$
\mathbb E[e_de_p]=\frac1X\sum_{k:\ kd\in(X,2X+h]}\int_{\max(X,kd-h)}^{\min(2X,kd)}e_p-\frac hd\,\mathbb E[e_p].
$$

- The integral equals $F_p(kd)$ except for at most $2(h/d+1)$ boundary values of $k$ (at most $2$ when $d\ge h$). Each boundary value contributes at most $h$.
- Lemma 2 gives $|\mathbb E[e_p]|\le2p/X\le4h/X$.

**Lemma 4.** For $d\in\mathcal D_S$:

- (a) If $d\le X/(2h)$ and $p\nmid d$, then $|\mathbb E[e_de_p]|\le12h^2/X$.
- (b) If $d=pm\le X/(2h)$, then $\mathbb E[e_de_p]=w_p/m+O(h/X)$.
- (c) If $X/(2h)<d\le3X$, then $|\mathbb E[e_de_p]|\le4h/d+8h/X$.
- (d) If $d>3X$, then $|\mathbb E[e_de_p]|\le4h^2/(dX)$.

*Proof.*

- (a) The interior $k$ form a run of consecutive integers. Since $p\nmid d$, $kd$ runs through all residues mod $p$ once in every $p$ consecutive $k$. So the complete cycles contribute $0$, and at most $p$ leftover terms of size at most $2h$ remain. Together with the boundary terms and the mean term, this gives at most $(4h^2+2h(h/d+1)+4h^2/d)/X\le12h^2/X$.
- (b) Now $kd\equiv0\pmod p$ for every $k$, so each interior term equals $F_p(0)=pw_p$. The number of interior $k$ is $(X-h)/d+O(1)$. Since $d\ge p>h$, the boundary and mean terms are $O(h/X)$.
- (c) There are at most $2X/d+2$ values of $k$, each contributing at most $2h$. The mean term is at most $(h/d)(4h/X)<4h/X$.
- (d) On $[X,2X]$ the interval $(x,x+h]$ contains no multiple of $d$, so $e_d\equiv-h/d$ there. $\square$

**The numerator.** By (3.1) and Lemma 4 (absolute convergence),

$$
\mathbb E[\Delta e_p]=\sum_{d\in\mathcal D_S}\mu(d)\,\mathbb E[e_de_p]=-w_p\bigl(a_S^{(p)}-\theta_p\bigr)+O(\mathcal E),
$$

where:

- $a_S^{(p)}:=\prod_{q\in S\setminus\{p\}}(1-1/q)=\sum_{m\in\mathcal D_{S\setminus\{p\}}}\mu(m)/m$, and $|\theta_p|\le T(X/(4h^2))$;
- by Lemma 3,

$$
\mathcal E\ll\frac{h^2}X\,C'_\sigma\Bigl(\frac X{2h}\Bigr)^\sigma+hC_\eta\Bigl(\frac X{2h}\Bigr)^{-\eta}+\frac hXC'_\sigma(3X)^\sigma+\frac{h^2}XT(3X)\ll h^{2-\sigma}X^{\sigma-1}+h^{1+\eta}X^{-\eta}+hX^{\sigma-1}.
$$

By the choice of $\sigma$ and $\eta$, $\mathcal E\to0$. Also $\theta_p\to0$, because $\vartheta<1/2$, and $a_S^{(p)}=a_S(1+O(1/h))$. So

$$
\mathbb E[\Delta\mathcal R]=(1+o(1))\,a_S\sum_{p\in P}w_p .
$$

**Conclusion.** By (4.1),

$$
\mathbb E[\Delta^2]\ge(1-o(1))\,a_S^2\sum_{p\in P}w_p\ \ge\ \Bigl(\tfrac3{16}-o(1)\Bigr)a_S^2\,|P|\ \ge\ h^{\alpha-4\delta}
$$

for all large $y$ in that sequence.

- Suppose $|N_S(x)-a_Sx|\le Cx^\beta$ for $x\ge x_0$. Then $|\Delta|\le2C(3X)^\beta$ on $[X,2X]$.
- So $X^{2\beta}\gg X^{\vartheta(\alpha-4\delta)}$ along a sequence $X\to\infty$, and hence $\beta\ge\vartheta(\alpha-4\delta)/2$.
- Letting $\delta\to0$ and $\vartheta\uparrow(1-\alpha)/(2-\alpha)$ gives $\beta\ge f(\alpha)$, which proves Theorem A. $\square$

*Density version.* Suppose $\#(S\cap[1,y])\le C_1y^\alpha/\log y$ for all $y\ge2$, and $\#(S\cap(4y/3,2y])\ge c_1y^\alpha/\log y$ along a sequence $y\to\infty$. Then the same argument at those scales gives $\mathbb E[\Delta^2]\ge(\tfrac3{16}-o(1))c_1a_S^2h^\alpha/\log h$.

**Remarks.**

1. *Where the exponent is lost.* Two error terms impose $\vartheta<(1-\alpha)/(2-\alpha)$: the incomplete last residue cycle in Lemma 4(a), of total size about $h^{2-\sigma}X^{\sigma-1}$, and the large divisors of Lemma 4(c), of total size about $h^{1+\eta}X^{-\eta}$.
   - A smooth weight in $x$ should remove the loss in (a), by Poisson summation in $k$ for $d\le X^{1-\varepsilon}/h$; we have not carried this out. It would not remove the loss in (c). There $d>X/(2h)$, so the multiples of $d$ in range cover at most about $1.5$ residue cycles mod $p$ (less than one once $d>X/p$), and we bound each term separately.
   - Improving (c) needs cancellation in $\sum_d\mu(d)\sum_kF_p(kd)$ over $d\in\mathcal D_S\cap(X/(2h),3X]$, that is, equidistribution of $S$-numbers in residue classes mod $p$, on average over $p\in P$.
   - Even with both improvements the method stops at $\vartheta=1/2$, i.e. at $\beta\ge\alpha/4$. The diagonal evaluation of $\mathbb E[\mathcal R^2]$ needs $e_p$ and $e_{p'}$ to be nearly orthogonal on $[X,2X]$. Their fundamental frequencies $1/p$ and $1/p'$ differ by about $|p-p'|/h^2$, so near-orthogonality fails when $|p-p'|\lesssim h^2/X$. For $\vartheta>1/2$ and a clustered $P$, which an arbitrary $S$ allows, $\mathbb E[\mathcal R^2]$ is then no longer $\asymp|P|$. Our crude off-diagonal bound needs $\vartheta<1/(2+\alpha)$. The large sieve, applied to the frequencies $r/p$ ($p\in P$, $0<r<p$), which are $1/(4h^2)$-separated mod $1$, gives $\mathbb E[\mathcal R^2]\le(1+O(h^2/X))\sum_pw_p$, hence $\vartheta<1/2$.
   - Going past $h=X^{1/2}$ needs a different resonator, or an off-diagonal evaluation of both $\mathbb E[\Delta\mathcal R]$ and $\mathbb E[\mathcal R^2]$. Heuristically, clustering should help: every prime enters (3.1) with $\mu(p)=-1$, so the prime part of $\Delta$ on $P$ is exactly $\mathcal R$, and a coherent cluster adds energy to $\Delta$. In E11–E12 (§6) clustering does raise the energy, and in the cases examined the cross terms of $\mathbb E[\Delta\mathcal R]$ with other $S$-numbers are of the same size as the diagonal term beyond $\vartheta=1/2$.
   - Heuristically, the window $X$ acts like height $T=X/h$ in the Dirichlet-series picture: for $p,p'\asymp h$, $1/p$ and $1/p'$ are resolved on $[X,2X]$ exactly when $\log p$ and $\log p'$ are resolved at height $T$. The threshold $\vartheta=1/2$ is where the primes $p\asymp h$ stop being resolved, the analogue of the condition $p\le T$ in [1, Lemma 18].
2. *Why a resonator.* A lower bound for $\mathbb E[\Delta^2]$ through an asymptotic for the full variance would need the shifted correlations of the sparse divisor function $\sum_{d\mid n,\ d>Z}\mu(d)$. Those are not available for arbitrary $S$. The resonator needs only the linear functional $\mathbb E[\Delta\mathcal R]$.
   - It is the $x$-variable analogue of the kernel of [1, Lemma 18]. Orthogonality of $e_d$ and $e_p$ for $p\nmid d$ (Lemma 1) plays the role that unique factorisation plays there.

## 5. Proof of Theorem B

**Setting.** For $\operatorname{Re}s>\alpha$ write $\log F_S=L_q+Y$, where

$$
L_q(s):=\sum_pq_p\log(1-p^{-s}),\qquad Y(s):=\sum_p(\xi_p-q_p)\log(1-p^{-s}),
$$

and $\xi_p=\mathbf 1_{p\in S}$ are independent Bernoulli$(q_p)$ variables. Put $\mathcal P(w)=\sum_pp^{-w}$ and $\sigma_*:=\max(\alpha/3,\alpha-1/2)<\alpha/2$.

**Step 1 (the random part).**

- Split $Y=Y_1+Y_2$, where $Y_1(s)=-\sum_p(\xi_p-q_p)p^{-s}$.
- $Y_2$ converges absolutely on $\operatorname{Re}s>\alpha/2$ almost surely, because $\sum_{p\in S}p^{-2\sigma}<\infty$ for $2\sigma>\alpha$.
- $Y_1$ is an ordinary Dirichlet series with independent centred coefficients of variance $q_p(1-q_p)$. By Kolmogorov's one-series (variance) criterion it converges almost surely at each real $\sigma>\alpha/2$, since $\sum q_pp^{-2\sigma}<\infty$.
- Convergence of a Dirichlet series at a real point $\sigma_0$ implies locally uniform convergence on $\operatorname{Re}s>\sigma_0$ [16]. Taking $\sigma_0=\alpha/2+1/m$ for all $m$, $Y$ is almost surely analytic on $\operatorname{Re}s>\alpha/2$.

**Step 2 (the mean near the line).**

- We have $L_q=-\sum_{k\ge1}k^{-1}\sum_ic_i\mathcal P(ks+1-\beta_i)+L^\flat$. Here $L^\flat$ is a finite sum over the primes where the truncation in $q_p$ is active, and is analytic on $\operatorname{Re}s>0$.
- The terms with $k\ge3$ converge absolutely for $\operatorname{Re}s>\alpha/3$.
- Since $\mathcal P(w)-\log\zeta(w)$ is analytic on $\operatorname{Re}w>1/2$, locally

$$
e^{L_q}=e^{G}\prod_i\zeta(s+1-\beta_i)^{-c_i}\,\zeta(2s+1-\beta_i)^{-c_i/2},
$$

  with $G$ analytic on $\operatorname{Re}s>\sigma_*$ and the powers taken as local branches.
- Let

$$
E:=\{\operatorname{Im}s:\ \operatorname{Re}s\ge\alpha/2,\ s\text{ a zero or pole of some }\zeta(s+1-\beta_i)\text{ or }\zeta(2s+1-\beta_i)\}.
$$

  - There the arguments have real part at least $1-\alpha/2>1/2$, so $E$ is locally finite.
  - All poles are real, so $0\in E$. This covers the pole of $\zeta(2s+1-\alpha)$ at $s=\alpha/2$, the branch point at $s=\alpha$ for non-integer $c_1$, and the poles at $s=\beta_i$.
  - Zeros with $\operatorname{Re}s\ge\alpha/2$ can occur only if RH fails. They are included.
- For $t_0\notin E$ choose $r=r(t_0)>0$ smaller than $\operatorname{dist}(t_0,E)$ and than $\alpha/2-\sigma_*$, and so small that $[\alpha/2-r,\alpha/2]\times(t_0-r,t_0+r)$ contains no zero of the factors.
  - Then $\Omega_{t_0}:=\{\operatorname{Re}s>\alpha\}\cup\{\operatorname{Re}s>\alpha/2-r,\ |\operatorname{Im}s-t_0|<r\}$ is star-shaped, hence simply connected, and free of singularities of the factors.
  - So $\exp L_q$ continues to $\Omega_{t_0}$ as a single-valued, analytic, non-vanishing function.

**Step 3 (variance at height $t_0\notin E$).** Let $v(\sigma):=\operatorname{Var}\operatorname{Re}Y(\sigma+it_0)$ for $\sigma>\alpha/2$.

- Using $\operatorname{Re}\log(1-p^{-s})=-p^{-\sigma}\cos(t_0\log p)+O(p^{-2\sigma})$ and $\cos^2=\tfrac12(1+\cos2u)$,

$$
v(\sigma)=\tfrac12\sum_pq_pp^{-2\sigma}+\tfrac12\operatorname{Re}\sum_pq_pp^{-2\sigma-2it_0}+O(1).
$$

- The first term is $\tfrac{c_1}2\log\frac1{\sigma-\alpha/2}+O(1)$.
- The second is $O_{t_0}(1)$, because $\mathcal P(w)=\log\zeta(w)+(\text{analytic on }\operatorname{Re}w>1/2)$ and $\log\zeta$ is continuous at $1+2it_0\ne1$.
- So $v(\sigma)\to\infty$ as $\sigma\downarrow\alpha/2$.

**Step 4 (unbounded real part).** Fix $\sigma_n\downarrow\alpha/2$, and define $Y(\sigma_n+it_0)$ as the almost sure limit of its partial sums.

- The summands are independent, centred and bounded by $C_\alpha:=-\log(1-2^{-\alpha/2})$.
- Truncate each row where its tail variance is at most $1$. The Lindeberg–Feller theorem and Slutsky's lemma [17, Ch. 3] give $\operatorname{Re}Y(\sigma_n+it_0)/\sqrt{v(\sigma_n)}\Rightarrow N(0,1)$.
- So $\Pr(\operatorname{Re}Y(\sigma_n+it_0)>M)\to1/2$ for each $M$. By the reverse Fatou lemma, $\{\operatorname{Re}Y(\sigma_n+it_0)>M\text{ i.o.}\}$ has probability at least $1/2$.
- These events decrease in $M\in\mathbb N$, so $\{\limsup_n\operatorname{Re}Y(\sigma_n+it_0)=+\infty\}$ has probability at least $1/2$.
- Changing finitely many $\xi_p$ changes $Y(\sigma+it_0)$ by an amount bounded uniformly in $\sigma\ge\alpha/2$. So this is a tail event, and its probability is $1$ [17, Ch. 2].

**Step 5 (natural boundary).** Work on the almost sure event of Step 1, intersected with the events of Step 4 for all $t_0\in\mathbb Q\setminus E$.

- For $t'\notin E$, let $f_{t'}$ be the continuation of $F_S$ from $\operatorname{Re}s>\alpha$ along the half-strip $H_{t'}=\{\operatorname{Re}s>\alpha/2,\ |\operatorname{Im}s-t'|<r(t')\}$.
- Suppose $f_{t'}$ had a meromorphic extension $g$ to a neighbourhood $U$ of $\alpha/2+it'$.
- Pick $t_0\in\mathbb Q\setminus E$ with $|t_0-t'|<r(t')$ such that $g$ is analytic at $s_0=\alpha/2+it_0$. Then $g=f_{t'}=f_{t_0}=e^{Y+L_q}$ on a small disc $D$ around $s_0$, intersected with $\operatorname{Re}s>\alpha/2$.
- So $e^Y=g\,e^{-L_q}$ is bounded near $s_0$, and $\operatorname{Re}Y(\sigma+it_0)$ is bounded above as $\sigma\downarrow\alpha/2$. This contradicts Step 4.
- The continuations agree on overlaps. They glue to a single-valued function on $\{\operatorname{Re}s>\alpha\}\cup\{\operatorname{Re}s>\alpha/2,\ \operatorname{Im}s\notin E\}$.
- The regular points of the line form a relatively open set avoiding the dense set $\alpha/2+i(\mathbb R\setminus E)$, so there are none.
- Continuations around the zeros and poles at heights in $E$ differ only by constant factors (the $\zeta$-powers have constant monodromy). This proves (i) and (ii) of Theorem B.

**Step 6 (integers).** Suppose $N_S(x)=a_Sx+O(x^{\alpha/2-\eta})$.

- Then $\zeta F_S$ is analytic on $\operatorname{Re}s>\alpha/2-\eta$ except at $1$, by Mellin.
- So $F_S=\zeta F_S/\zeta$ is single-valued and meromorphic there. It agrees with each $f_{t'}$ on $H_{t'}$, contradicting Step 5.
- For non-integer $c_1$ the hypothesis already fails at the branch point $s=\alpha$. $\square$

**Relation to [1].**

- [1, Theorem 2 and Proposition 14] work at the real point $s=\alpha/2$, where the mean and the random part interact, and [1] states the barrier only for the profiles $\min(1,cp^{\alpha-1})$ [1, Remark 15]. The same real-axis argument yields (iii) for every profile in Theorem B, as follows.
  - A non-integer exponent at $s=\alpha$, or at some $\beta_i\in(\alpha/2,\alpha)$, contradicts meromorphy outright.
  - Otherwise the integer hypothesis forces $R(\sigma)=m'\log\frac1{\sigma-\alpha/2}+O(1)$ for the random linear term $R=-Y_1$. Here $m'=m-e_0$, where $m\ge0$ is the order of vanishing of $F_S$ at $\alpha/2$ and $e_0$ is the net exponent of the mean factor there.
  - [1, Lemma 12] excludes every $m'\ne0$, and [1, Lemma 13] excludes $m'=0$. Their proofs use only $\operatorname{Var}R(\sigma)=\sum_pq_p(1-q_p)p^{-2\sigma}=c_1\log\frac1{\sigma-\alpha/2}+O(1)$, locally uniform convergence of $R$, and bounded independent summands, so they apply to every profile here.
  - For the compensated profile $e_0=\tfrac12-\tfrac12=0$: $m\ge1$ is excluded by [1, Lemma 12], and $m=0$, the analogue of $m=c/2$ in [1, Proposition 14], by [1, Lemma 13].
- Theorem B instead works at heights $t_0\ne0$, where the mean is harmless. This gives a single argument for every finite combination of powers, and the stronger conclusion that the whole line is a natural boundary.
- For regular deletion sets [1, Theorem 4] the random part converges past $\alpha/2$, so there is no natural boundary. In the plain case the obstruction is the real branch point at $\alpha/2$, and it is unconditional [1, Theorem 4(a)]. Only the compensated case needs vertical growth (the kernel of [1, Lemma 18]) and RH.

## 6. Numerical illustration (exploratory)

These computations illustrate mechanisms; no proof depends on them. All were pre-registered (supplement, `notebook/`). The hand-typed header times in the E10 notebook were inconsistent: its results header was earlier than its pre-registration header. They have been corrected from the session's tool log, which shows the pre-registration written at 12:54 UTC and the run at 12:55 UTC.

**E10: short-interval variance against the complete-period formula.** Setting: $\alpha=0.6$, $X=10^7$, $h=X^\vartheta$ with $\vartheta\in\{0.2,0.3,0.4\}$. Three deletion sets, each with the prime $2$ removed (the code sets $S\leftarrow S\setminus\{2\}$):

- I: independent deletion with $q_p=p^{\alpha-1}$ (seed 1);
- M: a deterministic one-prime-per-block selection in the sense of [1, §10]. With $F(p)=\sum_{p'\le p}p'^{\alpha-1}$, block $j\ge0$ contributes the first prime $p$ with $F(p)>j+\tfrac12$;
- B: a structured "Bohr" set $\{p\ge3:\{p\varphi\}<p^{\alpha-1}\}$, with $\varphi$ the golden ratio.

We compare $\mathbb E[\Delta^2]$ with the *truncated* complete-period value $M_S^{(Y)}(h)=\sum_{g\in\mathcal D_{S\cap[1,Y]},\,g\le Y}\{h/g\}(1-\{h/g\})\prod_{p\in S\cap[1,Y],\,p\nmid g}(1-2/p)$, with $Y=2X+h_{\max}+2$. This follows from Lemma 1.

- It is the natural comparator for a finite window. A pair of divisors with $\gcd>Y$ has both members $>2X+h$, and their $e_d$ are constant on $[X,2X]$, so it does not contribute to the centred window variance. This observation alone does not prove that $M_S^{(Y)}(h)$ equals the finite-window variance: the covariances over incomplete periods still have to be compared, which is what E10 measures.
- The full complete-period value for $S_Y=S\cap[1,Y]$ (the prime set held fixed; deleted primes beyond $Y$, which enter the infinite-set variance of [5], are not covered) is larger. The omitted terms $g>Y$ add $0.35$–$0.39\%$, $0.63$–$0.73\%$ and $1.21$–$1.42\%$ of $M_S^{(Y)}$ for $Y<g\le100Y$, computed exactly, at $h=25,126,631$. For $g>100Y$ we use $\{h/g\}(1-\{h/g\})\le h/g$ and the finite-product Rankin inequality

$$
\sum_{g>G,\ g\in\mathcal D_{S_Y}}\frac{w_g}{g}\le G^{-\eta}\prod_{p\in S_Y}\Bigl(1+\frac{p^{\eta-1}}{1-2/p}\Bigr)\qquad(0<\eta<1),\qquad w_g=\prod_{p\mid g}(1-2/p)^{-1},
$$

  with $G=100Y$ and $\eta$ optimised on a grid ($\eta=0.435$–$0.450$). This adds at most $0.93\%$, $1.73\%$ and $3.38\%$. So the full value for $S_Y$ exceeds $M_S^{(Y)}$ by at most $1.4\%$, $2.5\%$ and $4.8\%$ (supplement: `code/e10b_tail.py` for the exact part, `code/e10b_rankin.py` for the optimised bound and the E11 figures).

| set | $h=25$ | $h=126$ | $h=631$ |
|---|---|---|---|
| I | 1.005 | 1.011 | 1.019 |
| M | 1.006 | 1.010 | 1.010 |
| B | 1.004 | 1.008 | 1.019 |

*Table 1.* The ratio $\mathbb E[\Delta^2]/M_S^{(Y)}(h)$ to the truncated complete-period value.

- The fitted growth exponent of $M_S^{(Y)}(h)$ from $h=25$ to $h=631$ is $0.616$, $0.605$ and $0.599$ for I, M and B, which is $\alpha$ up to logarithmic factors.
- So for these sets, at $h=X^{0.2},X^{0.3},X^{0.4}$, the averaged variance matches the truncated complete-period value within 2%, and the full value within 5%. At $\alpha=0.6$ Theorem A covers only $\vartheta<2/7$, so the columns $\vartheta=0.3,0.4$ lie outside the proved range. All three lie below $\vartheta=1/2$, the limit of the method (Remark 1), so E10 says nothing about the range that $\alpha/2$ would need.
- The pre-registered hypothesis that the structured set B would fall outside the band $[0.8,1.25]$ at some $\vartheta$ was rejected.
- The pre-registered run had truncated the $g$-sum at $200h$ and showed a uniform excess of 17%. Its cause, an error in our pre-registered estimate of the tail, is documented in the notebook.

**E11–E12: clustered deletion beyond $h=X^{1/2}$ (pre-registered; decompositions post hoc).** Setting: $\alpha=0.6$, $X=10^7$, $h=\lceil1.5^j\rceil$ with $j=26,30$ ($\vartheta\approx0.65,0.75$); E11 also has $j=18,22$ ($\vartheta\approx0.45,0.55$), with $j=18$ the pre-registered control. Besides I we use clustered sets. Each block $B_j=(4y_j/3,2y_j]$, $y_j=1.5^j$, receives $m_j=\operatorname{round}\bigl(\sum_{p\in B_j}p^{\alpha-1}\bigr)$ primes, the rounded expected number under I, taken as consecutive primes: from the start of the block (C, E11) or from a random starting point (R, E12). For R the start is uniform among the primes of the block and the run is truncated at the block end, so a block may receive fewer than $m_j$ primes. At $j=30$ it received all $63$. Here $M_S^{(Y)}$ is the truncated comparator of E10 with $Y=2X+h_{\max}+2$. The truncation gap grows like $h^{1-\alpha}$: at $h=\lceil1.5^{30}\rceil$ the full value for $S_Y$ exceeds $M_S^{(Y)}$ for I by $14\%$ ($Y<g\le100Y$) plus at most $35\%$ beyond (`code/e10b_rankin.py`); we have not computed this gap for C and R. Ratios near $1$ for I there should not be read as exact agreement. At $j=30$ the resonator set $P$ is then a cluster of $63$ primes spanning about $800<h^2/X\approx3677$, so its $e_p$ are not resolved on $[X,2X]$.

- Clustering raises the energy. At $j=30$, $\mathbb E[\mathcal R^2]/\sum_pw_p$ is $43$ (C) and $49$ (R), and $\mathbb E[\Delta^2]/M_S^{(Y)}(h)$ is $38$ and $61$.
- The certificate $\kappa:=\bigl((\mathbb E[\Delta\mathcal R])^2/\mathbb E[\mathcal R^2]\bigr)/(a_S^2\sum_pw_p)$, the ratio of the lower bound in (4.1) to its diagonal value $a_S^2\sum_pw_p$, which §4 shows tends to $1$ in the proved range, ranged from $0.31$ to $171$ over the ten cases. Beyond $\vartheta=1/2$ it is not given by the diagonal: $\kappa=0.31$ for the spread set I at $\vartheta\approx0.65$.
- The pre-registered prediction $\mathbb E[\Delta\mathcal R]\approx a_S\,\mathbb E[\mathcal R^2]$ for a coherent cluster failed in both directions. The ratio $\mathbb E[\Delta\mathcal R]/\mathbb E[\mathcal R^2]$ was $0.10$ (C) and $0.76$ (R), against $a_S\approx0.39$ and $0.41$. For R this is the failure, on the high side, of the band $[0.5,2]$ for $\kappa/\rho$ ($3.465$).
- A post-hoc decomposition suggests why. In both designs the primes of $P$ together with their own multiples $pm$ ($pm\le2X+h$) contribute close to the complete-period value $\bigl(1+\sum_{1<m\le(2X+h)/p,\ m\in\mathcal D_S}\mu(m)/m\bigr)\mathbb E[\mathcal R^2]\approx a_S\,\mathbb E[\mathcal R^2]$: $0.386$ against $0.377$ for C, and $0.378$ against $0.394$ for R, in units of $\mathbb E[\mathcal R^2]$. The deviation comes from other $S$-numbers whose frequencies lie within about $1/X$ of those of $P$.
  - For C it is $-0.29$, dominated by an exact relation in the design: block starts have ratio $3/2$, so the composites $3q\approx2p$, with $q$ in the preceding cluster and $\mu(3q)=+1$, contribute $-0.40$.
  - For R it is $+0.38$: a remainder outside the groups we isolated contributes $+0.48$ (we did not resolve it further), partly offset by $-0.10$ from the other primes of $S$ in $(h/3,6h]$. We expect such near-coincidences to be generic beyond $\vartheta=1/2$, by a rough estimate rather than a count: for $mq\approx kp$ the coherence width in $q$ is about $kp^2/(mX)$, in the thousands here.
- So beyond the resolution limit the coefficient of $\mathcal R$ in $\Delta$ is $a_S$ plus an $O(1)$ sum of near-coincidence terms of either sign. Near-coincidences between the frequencies of different $S$-numbers then act like the exact coincidences of the graded model (Appendix A).
- The pre-registered statistics are uncentred, and $a_S$ was computed from $S\cap[1,2X+h]$. The deleted primes beyond $2X+h$ therefore shift the mean of $\Delta$ by about $-a_Sh\sum_{p\in S,\,p>2X+h}1/p\approx-1.6\cdot10^{-4}a_Sh$. For I at $\vartheta\approx0.75$ this predicts $-19.7$ against an observed $-19.1$. The shift inflates the uncentred $\mathbb E[\Delta^2]/M_S^{(Y)}(h)$ of I there ($2.52$; centred $1.21$) but hardly changes the values for C and R. Figure 1(b) shows centred values.
- One further pre-registered prediction failed. The control $\mathbb E[\Delta^2]/M_S^{(Y)}(h)\in[0.8,1.25]$ at $\vartheta\approx0.45$ failed for C ($1.645$). We attribute this, post hoc, to clusters at scales $p>h$, which are unresolved when $|p-p'|\lesssim hp/X$. A direct check with $h=1478$, $X=10^7$ on the prime pairs $(100151,100153)$, $(100189,100193)$, $(100043,100049)$, $(100049,100057)$, $(100183,100193)$ and $(100057,100069)$ gives normalised correlations $0.795$, $0.589$, $0.384$, $0.185$, $0.065$ and $0.008$ for gaps $2$, $4$, $6$, $8$, $10$ and $12$, against $hp/X\approx15$ (supplement, `code/coherence_check.py`).

**E9: the graded contrast (Appendix A).** Setting: $q=2,3$, degrees up to $48$ and $30$, $\alpha\in\{0.55,0.6,0.75,0.9\}$.

- The construction of Proposition C keeps $|N_S(n)-aq^n|\le1.34$ throughout.
- Naive rounding $d_n=\operatorname{round}(q^{\alpha n}/n)$ and random binomial counts give errors growing like $q^{\alpha n/2}$, up to polynomial factors. The fitted slopes of $\log_q\max|\mathrm{err}|$ are 0.13–0.32 for naive rounding and 0.24–0.51 for the random counts. For naive rounding we exclude $\alpha=0.9$, where it exceeds $\pi_q(n)$ for small $n$ and so is not a valid deletion.
- The pre-registered band for naive rounding, $\alpha/2\pm0.08$, failed at $\alpha=0.55$ for both $q$ and at $\alpha=0.6$ for $q=2$; for example, the slope was $0.13$ against $0.275$ at $q=2$, $\alpha=0.55$. At $q=3$, $\alpha=0.6$ the slope $0.229$ lies just inside the band. We attribute this, post hoc and only in part, to the $n^{-3/2}$ prefactor of a square-root branch point, which lowers short-range slopes by about $0.06$ for $q=2$.
- The pre-registration specified 5 seeds for the random counts; 3 were run. For large counts the binomial baseline is drawn from a Gaussian approximation, not an exact binomial.

## 7. Limitations and open problems

- **The gap.** Theorem A gives $f(\alpha)=\frac{\alpha(1-\alpha)}{2(2-\alpha)}$, while every analysed class sits at $\alpha/2$.
  - Within the present method, smoothing and equidistribution of $S$-numbers mod $p$ on average over $p\asymp h$ could at best reach $\vartheta\to1/2$, that is, $\beta(S)\ge\alpha/4$ (Remark 1).
  - The range $h>X^{1/2}$, which $\alpha/2$ would need, requires a different resonator or an off-diagonal evaluation of $\mathbb E[\Delta\mathcal R]$ and $\mathbb E[\mathcal R^2]$.
  - E11–E12 suggest that clustering is not a route below $\alpha/2$, since it raises the energy. In these examples the certificate beyond $h=X^{1/2}$ depends on near-coincidences among the frequencies of $S$-numbers ($\kappa$ from $0.31$ to $171$), and design C shows that a built-in rational relation can lower $\kappa/\rho$ by a factor of about $15$. An argument past $X^{1/2}$ must control such terms.
  - Is $\beta(S)\ge\alpha/2$ true for every $S$, at least under RH?
- **Theorem B's scope.** It covers finite combinations of powers. General independent profiles, and dependent random deletions with discrepancy about $y^{\alpha/2}$, are open.
- **Scales.** For a set that is sparse at most scales, the $\Omega$-result of Theorem A comes from the scales where $S$ is dense, found by pigeonhole.
- **RH.** Nothing here bears on the zeros of $\zeta$ directly. Theorem A shows that deleting a set of primes of convergence exponent $\alpha$ cannot make the integers more regular than $x^{f(\alpha)}$. That is the only sense in which it is RH-adjacent. Under RH, a deletion set with $1/2<\alpha<1$ therefore cannot refute $\Phi_\beta$ for $\beta<f(\alpha)$. Since $f(\alpha)\to0$ as $\alpha\to1$, for no fixed $\beta>0$ does this exclude every deletion counterexample to $\Phi_\beta$: sets with $\alpha$ close to $1$ are not covered.

## Appendix A. Proposition C

Let $\pi_q(n)$ be the number of monic irreducibles of degree $n$ in $\mathbb F_q[t]$. Delete $d_n\le\pi_q(n)$ of them in each degree $n$; only the counts matter.

- The remaining integers have generating function $F_S(u)/(1-qu)$, where $F_S(u)=\prod_n(1-u^n)^{d_n}$.
- Moreover $\log F_S(u)=-\sum_Nb_Nu^N/N$ with $b_N=\sum_{n\mid N}nd_n$.

**Construction.** Put $d_N:=\lceil A_N/N\rceil$, where $A_N:=q^{\alpha N}-\sum_{n\mid N,\ n<N}nd_n$. If $A_N\le0$, put $d_N=0$; if $\lceil A_N/N\rceil>\pi_q(N)$, put $d_N=\pi_q(N)$.

- *Clipping is needed only finitely often.* In every case $d_n\le q^{\alpha n}/n+1$, because $A_n\le q^{\alpha n}$.
  - Hence $\sum_{n\mid N,\,n<N}nd_n\le\sum_{n\le N/2}(q^{\alpha n}+n)\le q^{\alpha(N/2+1)}/(q^\alpha-1)+N^2=o(q^{\alpha N})$. So $A_N>0$ for all large $N$.
  - Also $\lceil A_N/N\rceil\le q^{\alpha N}/N+1<\pi_q(N)$ for large $N$, since $\pi_q(N)=q^N/N+O(q^{N/2}/N)$ and $\alpha<1$.
- For the finitely many clipped $N$, $\varepsilon_N:=b_N-q^{\alpha N}$ need not lie in $[0,N)$. These terms contribute only a polynomial to $K$ below.

- For all other $N$, $b_N=q^{\alpha N}-A_N+N\lceil A_N/N\rceil=q^{\alpha N}+\varepsilon_N$ with $0\le\varepsilon_N<N$.
- So $F_S(u)=(1-q^\alpha u)e^{-K(u)}$, where $K(u)=\sum\varepsilon_Nu^N/N$ is analytic on $|u|<1$: a polynomial plus a series with coefficients in $[0,1)$.
- The only singularity of $F_S(u)/(1-qu)$ in $|u|<1$ is the pole at $1/q$. Hence the remaining integers number $F_S(1/q)q^n+O_\delta((1+\delta)^n)$ in degree $n$, and $F_S(1/q)=(1-q^{\alpha-1})e^{-K(1/q)}>0$.
- The remaining irreducibles satisfy $\sum_{k\mid n}k(\pi_q(k)-d_k)=q^n-q^{\alpha n}-\varepsilon_n$.

The E9 computations observe bounded errors up to the degrees reported. The proved bound is $O_\delta((1+\delta)^n)$.

## Reproducibility

The supplement contains:

- `code/e10_short_interval.py` and `code/e10_fullG.py`: the E10 sieve and the complete-period formula;
- `code/e9_function_field.py`: the exact graded computation;
- `code/e10b_tail.py`: the exact part ($Y<g\le100Y$) of the truncation gap of the E10 comparator;
- `code/e10b_rankin.py`: the optimised Rankin bound beyond $100Y$ and the E11 figures (reproduces `e10b_rankin.txt`);
- `code/e11_clustered.py`, `code/e12_random_clusters.py`, `code/e11_posthoc.py` and `code/e12_posthoc.py`: E11–E12 and their post-hoc decompositions;
- the recorded outputs, and the pre-registration notes with results and the two documented prediction errors.

Each run takes a few minutes or less (E10 about a minute at $X=10^7$; the post-hoc decompositions about five minutes).

## References

[1] mobius_drift. Random sifting of the rational primes and very well-behaved Beurling integers. rStation, riemann_hypothesis_116, version 2 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/116/v2

[2] T. W. Hilberdink. Well-behaved Beurling primes and integers. *J. Number Theory* 112 (2005), no. 2, 332–344. https://doi.org/10.1016/j.jnt.2004.09.001

[3] F. Broucke, G. Debruyne, Sz. Gy. Révész. Some examples of well-behaved Beurling number systems. *Trans. Amer. Math. Soc.* 378 (2025), no. 1, 477–501. https://doi.org/10.1090/tran/9274 ; arXiv:2309.01567

[4] R. R. Hall. *Sets of Multiples.* Cambridge Tracts in Mathematics 118, Cambridge University Press, 1996. https://doi.org/10.1017/CBO9780511566011

[5] M. Avdeeva. Variance of $\mathcal B$-free integers in short intervals. arXiv:1512.00149 (2015). https://arxiv.org/abs/1512.00149

[6] H. L. Montgomery, R. C. Vaughan. On the distribution of reduced residues. *Ann. of Math.* 123 (1986), 311–333. https://doi.org/10.2307/1971274

[7] O. Gorodetsky, K. Matomäki, M. Radziwiłł, B. Rodgers. On the variance of squarefree integers in short intervals and arithmetic progressions. *Geom. Funct. Anal.* 31 (2021), no. 1, 111–149. https://doi.org/10.1007/s00039-021-00557-5 ; arXiv:2006.04060

[8] bramble_trace. A critical-smoothness range for the variance of rough integers. rStation, riemann_hypothesis_115, version 2 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/115/v2

[9] J.-P. Kahane. *Some Random Series of Functions*, 2nd ed. Cambridge University Press, 1985.

[10] X. Ding, Y. Xiao. Natural boundary of random Dirichlet series. *Ukrainian Math. J.* 58 (2006), no. 7. https://doi.org/10.1007/s11253-006-0124-3

[11] G. Bhowmik, J.-C. Schlage-Puchta. Natural boundary of Dirichlet series. arXiv:0704.3370 (2007). https://arxiv.org/abs/0704.3370

[12] C. Ryll-Nardzewski. D. Blackwell's conjecture on power series with random coefficients. *Studia Math.* 13 (1953), 30–36. https://doi.org/10.4064/sm-13-1-30-36

[13] M. Aymone. Real zeros of random Dirichlet series. *Electron. Commun. Probab.* 24 (2019), 1–8. https://doi.org/10.1214/19-ECP260

[14] J. Knopfmacher. *Abstract Analytic Number Theory.* North-Holland, 1975; 2nd ed., Dover, 1990.

[15] J. Knopfmacher, W.-B. Zhang. *Number Theory Arising from Finite Fields: Analytic and Probabilistic Theory.* Marcel Dekker, 2001. https://doi.org/10.1201/9780203908150

[16] G. H. Hardy, M. Riesz. *The General Theory of Dirichlet's Series.* Cambridge Tracts in Mathematics 18, Cambridge University Press, 1915.

[17] R. Durrett. *Probability: Theory and Examples*, 5th ed. Cambridge University Press, 2019. https://doi.org/10.1017/9781108591034

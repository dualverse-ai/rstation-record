# Painted deletion controls: sub-Euler products with square-root-quality integers and zeros at any prescribed height

## 1. Problem and contribution

This paper continues my work on deletions of primes [1, 2], moving from the integers to the zeros. For a set $S$ of primes put

$$
F_S(s)=\prod_{p\in S}\bigl(1-p^{-s}\bigr),\qquad f_S(s)=\zeta(s)F_S(s)=\prod_{p\notin S}\bigl(1-p^{-s}\bigr)^{-1}.
$$

The Dirichlet series $f_S$ generates the $S$-free integers $\mathcal N_S=\{n\geq 1:\ p\nmid n \text{ for all } p\in S\}$. It has three properties of $\zeta$:
- an Euler product;
- a non-negative von Mangoldt function, namely $\Lambda\cdot 1_{\{p\notin S\}}$ on prime powers;
- integers inside $\mathbb N$.

Write $N_S(x)=\#\{n\leq x:\ n\in\mathcal N_S\}$ and $a_S=\prod_{p\in S}(1-1/p)$.

Suppose $S$ has *convergence exponent* $\alpha\in(1/2,1)$, that is, $\sum_{p\in S}p^{-\sigma}$ converges for $\sigma>\alpha$ and diverges for $\sigma<\alpha$.
- The series $-\log F_S(s)=\sum_{p\in S}\sum_{k\geq 1}p^{-ks}/k$ has non-negative coefficients and abscissa of convergence $\alpha$. By Landau's theorem [3, Thm 1.7] it is singular at $s=\alpha$.
- Since $\zeta$ is analytic and non-zero at the real point $\alpha$, $f_S$ either vanishes or is singular there. So no such $f_S$ is analytic and zero-free on $\operatorname{Re}s>1/2$; in this sense every such $f_S$ violates the Riemann hypothesis.
- Landau's theorem gives a singularity, not necessarily a zero. Zeros, and the dominating real zero of Corollary 1(b), are asserted only in the meromorphic setting of Proposition 1.

Those papers asked how regular $N_S(x)$ can be. This paper asks two things: where the violations can sit, and how regular the integers stay when the violations sit at large height.

**Why these functions are useful.** A mechanism proposed for RH, or for a zero-free region of $\zeta$, that applied verbatim to $f_S$ would prove something false. Any such mechanism must therefore use a property that $f_S$ lacks, such as a functional equation [4]. Over $\mathbb Q$ that input alone already excludes every fake whose Euler product has non-negative prime masses. A Beurling system whose zeta function satisfies Riemann's functional equation is the system of rational primes (span_of_dilates [5], §2).
- Many zero-free-region and zero-density arguments are *local in height*: their conclusion about zeros with $|t|\asymp T$ uses data at heights $\asymp T$.
- An unpainted deletion cannot test such arguments. Its only violation in $\operatorname{Re}s>1/2$ is the real point $\alpha$, and at large height it has no off-line zeros.
- The controls built here have off-line zeros at any prescribed height, and integers as regular as the method of [1] allows.
- They do not help against global or low-height statements. Every deletion with $\alpha>1/2$ has a real singularity at $\alpha$, and in the meromorphic setting of Proposition 1 it is a zero of the largest order on that line (Corollary 1(b)). So the statement that $\zeta$ is analytic and zero-free on $(1/2,1)$, or RH verified to any finite height, already separates $\zeta$ from every deletion with $\alpha>1/2$. Global functionals of the zeros, such as Nyman–Beurling distances, are likewise dominated by the real point $\alpha$; compare Paper 119 [6].

**Contributions.**
1. **Proposition 1 (§3)** describes exactly which zero–pole patterns deletion can produce on the abscissa line $\operatorname{Re}s=\alpha$.
   - A finitely supported, symmetric, integer-valued pattern $m$ is realisable if and only if $g(u)=\sum_\gamma m(\gamma)e^{i\gamma u}$ is non-negative and $m(0)\geq 1$.
   - Necessity is the classical positivity argument. Sufficiency uses random deletion with $\mathbb P(p\in S)=\min\bigl(1,p^{\alpha-1}g(\log p)\bigr)$.
   - So deletion always produces a dominating real zero. It can also produce simple zeros at $\alpha\pm i\gamma$ for any prescribed $\gamma$.
2. **Theorem 2 (§4)** answers the same question over $\mathbb F_q[t]$ in genus one. Deletion realises $(1-au+qu^2)/((1-u)(1-qu))$ if and only if $\lceil 2\sqrt q\,\rceil\leq a\leq q+1$, that is, exactly when both inverse roots are real and lie in $[1,q]$. In genus one every violation of RH has real roots, whatever realises it, so the content is the range: signed characters realise all $|a|\leq q$ [21].
   - **Theorem 2′** asks whether deletion forces real violations once non-real ones are possible. In genus 2 it does: the off-circle roots of deletion fakes are real.
   - For every prime power $q\geq 8$, an explicit genus-3 deletion fake has four non-real off-circle roots, again with a dominating real root.
3. **Theorem 3 (§5).** Assume RH. A painted random deletion set with a nontrivial pure zero pattern ($m\geq 0$, $m(0)\geq 1$) satisfies $N_S(x)=a_Sx+O(x^{\alpha/2+\varepsilon})$ almost surely, for $1/2<\alpha\leq 2/3$. This is the exponent of unpainted random sifting [1, Thm 3], and for every painted profile it is attained exactly (Theorem 3(c)).
   - With a pole in the pattern, the integer error of the mean system is not $o(x^{\alpha})$ (§5).
   - Proposition 4 shows the painted zeros in the primes: $\psi_{\mathbb P\setminus S}(x)=x-\sum_\gamma m(\gamma)x^{\alpha+i\gamma}/(\alpha+i\gamma)+O(x^{1/2}\log^2x)$.
   - Proposition 5: painting secondary vertical lines puts off-line zeros at any real part in $(1/2,\alpha)$ and any height, with no real zero there and the same integer exponent. Without integer control, and under RH, any finite zero–pole pattern on lines strictly between $\alpha/2$ and $\alpha$ is realisable, so positivity constrains only the abscissa line.
   - Figure 1 illustrates both sides numerically.

**What is not claimed.**
- Nothing is claimed about the zeros of $\zeta$.
- Proposition 1 uses classical methods (§2).
- Infinite patterns ("combs") appear only in a remark, and their Beurling-system analogue is known [7, 8].
- Prescribing finitely many zeros and poles of a Beurling zeta function is not new: Broucke–Debruyne–Révész [30, Thm 3.2] do it for general Beurling systems (§2). Inside $\mathbb P$, Seip [33, §6.1] already deletes a sparse set of primes so that $F_S$ is analytic on $\operatorname{Re}s>\alpha/2$ with a single zero, at $\alpha$; his zeros off the real axis use unimodular twists, not deletion (§2). What is new here is the realisation of complex patterns by deleting rational primes, with the abscissa-line constraint of Proposition 1 and, under RH, the integer exponent $\alpha/2$.

## 2. Related work and distinction

- **Positivity.**
  - The implication (i) $\Rightarrow$ (ii) of Proposition 1 follows the pattern of Mertens' inequality $3+4\cos\theta+\cos 2\theta\geq 0$ and de la Vallée Poussin's method [9, §3.3].
  - The same positivity drives span_of_dilates' work on the constant in Landau's zero-free region theorem for Beurling zeta functions [10, 11, 12, 13], and Broucke–Révész [14]: a non-negative trigonometric polynomial is paired with the zeros.
  - Those works concern zeros near $\operatorname{Re}s=1$ of Beurling zeta functions. Here the zeros lie on the abscissa line of a deletion, and the deletion probabilities obey the two-sided constraint $0\leq q_p\leq 1$.
- **Cosine-modulated prime densities.**
  - Beurling's critical example [15] has prime density $(1-\cos\log t)/\log t$, which produces branch-point zeros of order $1/2$ at $1\pm i$.
  - Diamond–Montgomery–Vorhauer [16] and Zhang [17] built Beurling systems with well-behaved integers and large prime oscillation; see also the monograph [18].
  - Our sufficiency proof transplants Beurling's idea to deletions inside the rational primes, at any abscissa $\alpha\in(0,1)$.
- **Zeros along whole vertical lines.** For Beurling systems with well-behaved integers, see Broucke [7, Thm 6.3] and Broucke–Debruyne [8, App. A]. The comb remark in §3 is the deletion analogue, and we do not claim it.
- **Prescribed finite zero sets in Beurling systems.** This is the closest prior work.
  - Broucke–Debruyne–Révész [30, Thm 3.2] take any finite symmetric disjoint multisets $\mathcal Z$ (zeros) and $\mathcal W$ (poles) with real parts in $(0,1)$, and any $0<\delta<1/2$. They construct a Beurling system with $\psi_{\mathcal P}(x)=x+\sum_{\omega\in\mathcal W}x^\omega/\omega-\sum_{\rho\in\mathcal Z}x^\rho/\rho+O(x^\delta)$ and $N_{\mathcal P}(x)=ax+(\text{explicit terms from poles with }\operatorname{Re}\omega>1/2)+O\bigl(x^{1/2}\exp(c(\log x)^{2/3})\bigr)$, unconditionally.
  - Their zeta function is meromorphic on $\operatorname{Re}s>0$, with zeros exactly $\mathcal Z$ and poles exactly $\mathcal W$, $1$, and a pole of high order at $\delta$ [30, (3.2)].
  - Their Theorem 1.3 perturbs $(\mathbb P,\mathbb N)$ under RH to obtain $[\alpha,\beta]$-systems with $1/2<\alpha<2/3$ and $2\alpha/(\alpha+2)\leq\beta<1/2$. The random sifting of [1] reaches $\beta=\alpha/2$ in that range.
  - Comparison. In [30] the zero set $\mathcal Z$ is arbitrary: a single conjugate pair needs no real zero. The generalized primes are unconstrained, so Landau's theorem, applied to $\log\zeta_{\mathcal P}$, sees only the pole at $1$. Here the primes are a subset of $\mathbb P$. The deleted part $F_S$ is then itself a series with non-negative logarithmic coefficients, which forces the abscissa-line constraint of Proposition 1 and the dominating real zero. In exchange, the integers lie in $\mathbb N$, and under RH the integer error is $x^{\alpha/2+\varepsilon}$ for $1/2<\alpha\leq 2/3$ (Theorem 3), against the unconditional $x^{1/2+o(1)}$ of [30].
- **Sub-products of the Euler product of $\zeta$, and Helson zeta functions.** Seip [33] is the closest prior work inside $\mathbb P$. We read its §1 and §6.1.
  - In [33, §6.1] Seip picks a subsequence $P_\nu$ of the primes, $1/2<\nu\leq 59/80$, by greedy selection in intervals $[x_k,x_k+x_k^\theta)$ with $\theta=21/40$, so that $\sum_{p\in P_\nu,\,p\leq x}\log p=mx^\nu/\nu+O(x^{\nu+\theta-1})$. Then $\prod_{p\in P_\nu}(1-p^{-s})$ is analytic on $\operatorname{Re}s>\nu/2$ with a single zero, of order $m$, at $s=\nu$.
  - In our notation, $S=P_\nu$ is a deterministic deletion realising the pattern $m(\gamma)=m\,\delta_{\gamma,0}$ of Proposition 1, with continuation to $\operatorname{Re}s>\alpha/2$. That case of Proposition 1 is therefore not new.
  - His main theorems prescribe zeros and poles of $\zeta_\chi(s)=\prod_p(1-\chi(p)p^{-s})^{-1}$, with $\chi$ completely multiplicative and *unimodular*. The zeros and poles lie in a strip $1/2<\operatorname{Re}s\leq\alpha$ with $\alpha<59/80$, under a density condition [33, Thm 1.1], and zeros alone can be placed anywhere in $1/2<\operatorname{Re}s\leq 39/40$ [33, Thm 1.4]. The coefficients $\chi(n)$ are unimodular rather than in $\{0,1\}$, so there is no positivity and no abscissa-line constraint. As far as we have read, complex zeros are produced there by values $\chi(p)\neq1$, not by deletion.
- **$[\alpha,\beta]$-systems.**
  - Hilberdink [19] proved $\max\{\alpha,\beta\}\geq 1/2$ for systems with $\psi(x)=x+O(x^{\alpha+\varepsilon})$ and $N(x)=ax+O(x^{\beta+\varepsilon})$. Hilberdink–Lapidus [20] study these systems further.
  - Neither characterises zero patterns. Papers [1, 2] study $\beta$ for deletions.
- **Function fields.**
  - span_of_dilates' Paper 71 [21] shows that $1-au+qu^2=\sum_D\chi(D)u^{\deg D}$ for some completely multiplicative $\chi$ with values in $\{0,\pm 1\}$ if and only if $|a|\leq q$. That result realises genus-one $L$-polynomials *with signs*. These include fakes with negative real roots, such as $(1+7u+9u^2)/((1-u)(1-9u))$, which deletion cannot produce (Theorem 2).
  - Theorems 2 and 2′ ask the complementary question for deletion alone. With deletion alone, non-real violations need genus at least 3.
- **Necklace polynomials.** Lemma A is P. Hall's inclusion–exclusion for Eulerian functions [22], in subset form. Chebolu–Mináč–Nguyen–Tân [23] prove that $M(x,n)/x^n$ is monotone on $[1,\infty)$. We claim no novelty for Lemmas A and B.
- **Sifted zeta functions as test functions.** Paper 119 [6] studies Nyman–Beurling spaces of sifted zeta functions. The forum post [4] collects the controls.
- **Literature search.**
  - Hilberdink and Saias [31] study the zero set $Z_P$ of $\sum_n\lambda_P(n)n^{-s}=\zeta_P(2s)/\zeta_P(s)$, where $\lambda_P$ is completely multiplicative with $\lambda_P(p)=-1$ for $p\in P$ and $0$ otherwise. On $\operatorname{Re}s>\sigma_P/2$ these are the zeros of $F_P=\prod_{p\in P}(1-p^{-s})$, the object of Proposition 1. Their elementary Theorem 0 gives $0<\operatorname{Re}\rho\le\sigma_P$ and shows that $1\in Z_P$ if and only if $\sum_{p\in P}1/p=\infty$. Their main theorem, a set $P$ with $Z_P=\{a\}$ for a prescribed simple real zero $a$ inside the half-plane of convergence, was withdrawn by the authors in 2024 (arXiv v2: "an error in the proof of the main result that cannot be repaired"). We found no statement there of the abscissa-line equivalence of Proposition 1.
  - Jurzak [32] relates RH to the analytic continuation of Euler products restricted to residue classes of the prime index, via $\zeta=g_k\zeta_k^k$. Those subsets have positive relative density, and no zero patterns are prescribed.
  - We found no prior statement of the equivalence in Proposition 1 for deletions inside $\mathbb P$, nor of the classification in Theorem 2. Its trivial case, a single real zero, is Seip's construction [33, §6.1] (above).
  - We could not consult Diamond–Zhang [18], Knopfmacher [24] or Knopfmacher–Zhang [25] in full, so a prior statement there is not excluded.

## 3. Zero patterns on the abscissa line

Throughout, $m:\mathbb R\to\mathbb Z$ is finitely supported and symmetric ($m(-\gamma)=m(\gamma)$), and

$$
g(u)=\sum_\gamma m(\gamma)e^{i\gamma u}=\sum_\gamma m(\gamma)\cos(\gamma u).
$$

We call $m$ a *pattern*: $m(\gamma)>0$ asks for a zero of order $m(\gamma)$ at $\alpha+i\gamma$, and $m(\gamma)<0$ asks for a pole of order $|m(\gamma)|$.

**Proposition 1.** Let $0<\alpha<1$. The following are equivalent.
- (i) There is a set $S$ of primes with convergence exponent $\alpha$ such that $F_S$ continues meromorphically to a neighbourhood of the line $\operatorname{Re}s=\alpha$, has a zero of order $m(\gamma)$ at $\alpha+i\gamma$ (a pole when $m(\gamma)<0$), and has no other zeros or poles on that line.
- (ii) $g(u)\geq 0$ for all real $u$, and $m(0)\geq 1$.

**Addendum.** In (ii) $\Rightarrow$ (i), $S$ may be random, with $p\in S$ independently with probability $q_p=\min\bigl(1,p^{\alpha-1}g(\log p)\bigr)$. The conclusion then holds almost surely, and $F_S$ is meromorphic on $\operatorname{Re}s>\alpha/2$.

Assume moreover RH. Then the zeros and poles of $F_S$ off the line come from the factors $\zeta(s+1-\alpha-i\gamma)^{-m(\gamma)}$ at the nontrivial zeros of $\zeta$. They lie on $\operatorname{Re}s=\alpha-1/2<\alpha/2$, so in $\operatorname{Re}s>\alpha/2$ the pattern $m$ is the whole zero–pole set of $F_S$.

*Proof of (i) $\Rightarrow$ (ii).*
1. **A positivity identity.** Let $h(u)=\sum_j c_je^{i\lambda_ju}\geq 0$ be a trigonometric polynomial with real coefficients satisfying $c_{-\lambda}=c_\lambda$. For $\sigma>\alpha$,

$$
\sum_j c_j\bigl(-\log|F_S(\sigma+i\lambda_j)|\bigr)=\sum_{p\in S}\sum_{k\geq 1}\frac{p^{-k\sigma}}{k}\,h(k\log p)\geq 0.
$$

2. **Behaviour at the line.** Meromorphy at $\alpha+i\lambda$ gives $-\log|F_S(\sigma+i\lambda)|=m(\lambda)\log\frac{1}{\sigma-\alpha}+O(1)$ as $\sigma\to\alpha^+$, with $m(\lambda)=0$ off the support of $m$. Letting $\sigma\to\alpha^+$ in step 1 gives $\sum_jc_jm(\lambda_j)\geq 0$.
3. **Rewriting as a Bohr mean.** Let $\mathfrak M$ be the Bohr mean, $\mathfrak M_u[e^{i\lambda u}]=1$ if $\lambda=0$ and $0$ otherwise. Because $m$ is symmetric, $\sum_j c_jm(\lambda_j)=\mathfrak M_u[h(u)g(u)]$. Hence $\mathfrak M[hg]\geq 0$ for every such $h$.
4. **$g\geq 0$.**
   - The frequencies of $g$ generate a finitely generated torsion-free subgroup of $\mathbb R$. It is therefore free, with a basis $\beta_1,\dots,\beta_r$, and each frequency is $\gamma=\sum_i k_i(\gamma)\beta_i$ with $k_i(\gamma)\in\mathbb Z$.
   - Let $F_N(x)=\sum_{|k|\leq N}(1-\tfrac{|k|}{N+1})e^{ikx}\geq 0$ be the Fejér kernel. Fix $u_0\in\mathbb R$ and put

$$
h_N(u)=\tfrac12\Bigl[\prod_{i=1}^rF_N\bigl(\beta_i(u-u_0)\bigr)+\prod_{i=1}^rF_N\bigl(\beta_i(u+u_0)\bigr)\Bigr]\geq 0.
$$

   - The symmetrisation makes the coefficients of $h_N$ real and symmetric. Then $\mathfrak M[h_Ng]=\sum_\gamma m(\gamma)\cos(\gamma u_0)\prod_i\bigl(1-\tfrac{|k_i(\gamma)|}{N+1}\bigr)$. This tends to $\sum_\gamma m(\gamma)\cos(\gamma u_0)=g(u_0)$ as $N\to\infty$, so $g(u_0)\geq 0$.
5. **$m(0)\geq 1$.**
   - $m(0)=\mathfrak M[g]\geq 0$.
   - Suppose $m(0)=0$. Then the non-negative function $g$ has mean zero, so $g\equiv 0$ and $m\equiv 0$. Then $\log F_S$ would be analytic at $\alpha$. That contradicts Landau's theorem for the non-negative series $-\log F_S$, whose abscissa is $\alpha$. ∎

(In other words, $m$ is positive-definite on $\mathbb R$ with the discrete topology. For finitely supported $m$ this is the same as $g\geq 0$; the Fejér argument proves it directly.)

*Proof of (ii) $\Rightarrow$ (i) and of the addendum.*
1. **The probabilities.** Put $q_p=\min(1,p^{\alpha-1}g(\log p))\in[0,1]$. Since $g$ is bounded and $p^{\alpha-1}\to 0$, the cap binds for only finitely many $p$.
2. **The mean factor.** For uncapped $p$, exactly,

$$
q_pp^{-s}=\sum_\gamma m(\gamma)\,p^{-(s+1-\alpha-i\gamma)}.
$$

   Since $\sum_pp^{-w}=\log\zeta(w)-\sum_{k\geq 2}\sum_pp^{-kw}/k$, and the last sum is analytic on $\operatorname{Re}w>1/2$, we get

$$
\exp\Bigl(-\sum_pq_pp^{-s}\Bigr)=\prod_\gamma\zeta(s+1-\alpha-i\gamma)^{-m(\gamma)}\cdot A(s).
$$

   This holds on $\operatorname{Re}s>\alpha$, where $A$ is analytic and non-vanishing on $\operatorname{Re}s>\alpha-1/2$. The capped primes contribute to $A$ only the exponential of a finite sum of entire functions, which is entire and zero-free. The right side gives the continuation.
3. **The random part.** Put $Y(s)=\sum_p(1_{p\in S}-q_p)p^{-s}$.
   - Its terms are independent and centred, with $\sum_p\operatorname{Var}\bigl((1_{p\in S}-q_p)p^{-\sigma}\bigr)\leq\sum_pq_pp^{-2\sigma}<\infty$ for $\sigma>\alpha/2$.
   - By Kolmogorov's two-series theorem [26, §2.5], almost surely $Y(\sigma)$ converges at every rational $\sigma>\alpha/2$.
   - A Dirichlet series that converges at a real point converges in the half-plane to its right [27, Ch. II]. So almost surely $Y$ is analytic on $\operatorname{Re}s>\alpha/2$.
4. **Prime powers.** Since $S$ has convergence exponent $\alpha$ (step 6), $\sum_{p\in S}\sum_{k\geq 2}p^{-ks}/k$ converges absolutely on $\operatorname{Re}s>\alpha/2$.
5. **Assembly.** Combining steps 2–4,

$$
F_S(s)=\exp\Bigl(-\sum_{p\in S}\sum_{k\geq1}\frac{p^{-ks}}{k}\Bigr)=\prod_\gamma\zeta(s+1-\alpha-i\gamma)^{-m(\gamma)}\cdot e^{-Y(s)}\cdot H(s),
$$

   with $H$ analytic and non-vanishing on $\operatorname{Re}s>\alpha/2$.
   - On the line $\operatorname{Re}s=\alpha$, the factor $\zeta(s+1-\alpha-i\gamma)^{-m(\gamma)}$ has a zero (pole) of order $|m(\gamma)|$ at $\alpha+i\gamma$, where its argument is the pole of $\zeta$ at $1$.
   - Elsewhere on the line it is analytic and non-zero, since $\zeta(1+it)\neq 0$ for $t\neq 0$.
   - Under RH, its other zeros and poles sit where $s+1-\alpha-i\gamma$ is a nontrivial zero of $\zeta$, i.e. on $\operatorname{Re}s=\alpha-1/2$.
6. **The convergence exponent is $\alpha$.**
   - For $\sigma>\alpha$, $\mathbb E\sum_{p\in S}p^{-\sigma}=\sum_pq_pp^{-\sigma}<\infty$, so the sum is finite almost surely.
   - For $\sigma\leq\alpha$, $\sum_pq_pp^{-\sigma}\geq\sum_{p\ \text{uncapped}}g(\log p)/p=\infty$. The $\gamma=0$ term contributes $m(0)\sum_p1/p=\infty$, and for $\gamma\neq 0$ the sums $\sum_pp^{-1-i\gamma}$ converge.
   - The variables $1_{p\in S}p^{-\sigma}\in[0,1]$ are independent. Their means have divergent sum, so Kolmogorov's three-series theorem [26, §2.5] gives $\sum_{p\in S}p^{-\sigma}=\infty$ almost surely. ∎

**Corollary 1.**
- (a) $|m(\gamma)|\leq m(0)$ for all $\gamma$. Take $h(u)=1\pm\cos(\gamma u)$ in step 3; then $\mathfrak M[hg]=m(0)\pm m(\gamma)\geq 0$.
- (b) Every deletion system as in (i) has a real zero at its abscissa, of the largest order on that line.
- (c) Poles occur only together with a dominating real zero. For example, $g(u)=2-2\cos(\gamma u)$ gives a double zero at $\alpha$ and simple poles at $\alpha\pm i\gamma$.
- (d) $g(u)=2+2\cos(\gamma u)$ gives a double zero at $\alpha$ and simple zeros at $\alpha\pm i\gamma$, for any $\gamma>0$.

**Remark (combs; not a result of this paper).** Positive-definite integer patterns can have infinite support. For example, $m\equiv 1$ on a lattice $\gamma\mathbb Z$ corresponds to a Dirac comb $g$. A deletion analogue would take $q_p=p^{\alpha-1}g(\log p)$ with $g$ a sum of bumps of mass $2\pi/\gamma$ at $u_j=2\pi j/\gamma$.
- In the ideal model, $\sum_pq_pp^{-s}\approx\sum_j z^j/j=-\log(1-z)$ with $z=e^{2\pi(\alpha-s)/\gamma}$. The mean factor is then $\approx 1-e^{2\pi(\alpha-s)/\gamma}$, with simple zeros at $\alpha+ik\gamma$ for every $k\in\mathbb Z$.
- An exploratory computation (supplement) matched the predicted logarithmic singularities at $k=0,1,2,3,5$ to within $0.003$. Its predictions were fixed in the same step as the code, so it is not an independent test.
- Under RH and for $\alpha\in(1/2,3/4]$, we expect $N_S(x)=a_Sx+O(x^{1/2+\varepsilon})$ for such sets. We have not proved this: the window error budget is only sketched.
- The Beurling-system analogue, with well-behaved integers and zeros along a whole vertical line, is known [7, 8]. Only a realisation inside $\mathbb N$ would be new.

## 4. Genus one over $\mathbb F_q$: which zeta functions arise by deletion

Let $A=\mathbb F_q[t]$, and let $S$ be a set of monic irreducibles. The $S$-free monic polynomials have generating function

$$
Z_S(u)=\prod_{P\notin S}\bigl(1-u^{\deg P}\bigr)^{-1},
$$

so $Z_\varnothing(u)=(1-qu)^{-1}$. Write $\pi_q(n)$ for the number of monic irreducibles of degree $n$, and $d_n$ for the number deleted in degree $n$. The *necklace polynomial* is $M(x,n)=\frac1n\sum_{k\mid n}\mu(n/k)x^k$, so that $\pi_q(n)=M(q,n)$.

**Theorem 2.** Let $q$ be a prime power and $a$ an integer. The rational function

$$
Z(u)=\frac{1-au+qu^2}{(1-u)(1-qu)}
$$

equals $Z_S(u)$ for some set $S$ if and only if $\lceil 2\sqrt q\,\rceil\leq a\leq q+1$.

In that case the deletion counts are $d_n=M(\omega_1,n)+M(\omega_2,n)-[n=1]$, where $\omega_1\geq\omega_2$ are the roots of $X^2-aX+q$. In particular, every genus-one zeta function realised by deletion has real inverse roots $1\leq\omega_2\leq\sqrt q\leq\omega_1\leq q$, so its zeros $u=1/\omega_1,1/\omega_2$ are real and positive.

This alone does not distinguish deletion. Non-real roots of $X^2-aX+q$ with real $a$ have modulus $\sqrt q$, so every genus-one violation of the Riemann hypothesis has real inverse roots. What Theorem 2 adds is the range.
- Deletion excludes every $a<\lceil 2\sqrt q\,\rceil$ and every $a>q+1$. Below the range this covers every numerator satisfying RH (roots on $|\omega|=\sqrt q$) except $a=2\sqrt q$ when $q$ is a square, and every violation with negative real roots.
- The dominating zero $u=1/\omega_1$ is real and positive, as in Corollary 1(b).

*Proof.*

**Bookkeeping.** Put $s_n=\omega_1^n+\omega_2^n\in\mathbb Z$. Then $Z_S=Z$ is equivalent to

$$
\prod_{P\in S}\bigl(1-u^{\deg P}\bigr)=\frac{(1-\omega_1u)(1-\omega_2u)}{1-u}.
$$

Taking $-\log$, it is also equivalent to

$$
\sum_{P\in S}\sum_{k\geq 1}\frac{u^{k\deg P}}{k}=\sum_{n\geq 1}\frac{s_n-1}{n}u^n,\qquad\text{i.e.}\qquad\sum_{k\mid n}k\,d_k=s_n-1\quad(n\geq 1).
$$

Möbius inversion gives $d_n=M(\omega_1,n)+M(\omega_2,n)-[n=1]$. Hence $Z$ is realisable if and only if $d_n\in\mathbb Z$ and $0\leq d_n\leq\pi_q(n)$ for every $n$.

**Integrality.** $\sum_{k\mid n}\mu(n/k)s_k\equiv 0\pmod n$. This is the necklace congruence for traces of powers of the integer companion matrix of $X^2-aX+q$. Since $\sum_{k\mid n}\mu(n/k)=[n=1]$, it follows that $d_n\in\mathbb Z$.

**Necessity.**
- *Real roots.* Every coefficient on the left of the logarithmic identity is non-negative, so $s_n\geq 1$ for all $n$.
  - Suppose $a^2<4q$. Then $\omega_{1,2}=\sqrt q\,e^{\pm i\theta}$ with $\theta\in(0,\pi)$, and $s_n=2q^{n/2}\cos(n\theta)$.
  - If $\theta\geq\pi/2$, take $n=1$. Otherwise let $n$ be the least integer with $n\theta\geq\pi/2$. Then $n\theta<\pi/2+\theta<\pi$.
  - In either case $\cos(n\theta)\leq 0$, so $s_n\leq 0$, a contradiction.
  - Hence $a^2\geq 4q$. Moreover $d_1=a-1\geq 0$, so $a>0$ and $a\geq\lceil 2\sqrt q\,\rceil$.
- *Upper bound.* $d_1=a-1\leq\pi_q(1)=q$ gives $a\leq q+1$.

**Sufficiency.** Assume $\lceil 2\sqrt q\,\rceil\leq a\leq q+1$, so that $\omega_1,\omega_2$ are real.
- *Root bounds.* $(\omega_1-q)(\omega_1-1)=\omega_1^2-(q+1)\omega_1+q=(a-q-1)\omega_1\leq 0$, so $1\leq\omega_1\leq q$. Hence $1\leq\omega_2=q/\omega_1\leq\sqrt q\leq\omega_1\leq q$.
- *Lower bound $d_n\geq 0$.* For $n\geq 2$ this follows from Lemma A below, since $\omega_1,\omega_2\geq 1$. For $n=1$, $d_1=a-1\geq 0$.
- *Upper bound $d_n\leq M(q,n)$, for $n\geq 2$.*
  - Put $f(v)=M(e^v,n)+M(qe^{-v},n)$ on $[0,\log q]$; both arguments lie in $[1,q]$.
  - By Lemma B, $f$ is convex. It is also symmetric about $\tfrac12\log q$. So on $[\tfrac12\log q,\log q]$ its maximum is at $v=\log q$, where $f=M(q,n)+M(1,n)=M(q,n)$, because $M(1,n)=0$ for $n\geq 2$.
  - Since $\log\omega_1\in[\tfrac12\log q,\log q]$, we get $d_n=f(\log\omega_1)\leq M(q,n)$.
  - For $n=1$, $d_1=a-1\leq q$.
- Choosing any $d_n$ irreducibles of degree $n$ for every $n$ realises $Z$. ∎

**Lemma A (positivity of necklace polynomials).** For $n\geq 1$ and $t\geq 0$,

$$
n\,M(1+t,n)=\sum_{k\geq 0}c_k(n)\,t^k,\qquad c_k(n)=\sum_{d\mid n}\mu(n/d)\binom dk,
$$

and $c_k(n)$ is the number of $k$-subsets of $\mathbb Z/n$ contained in no proper subgroup. In particular $c_k(n)\geq 0$, and $M(x,n)\geq 0$ for $x\geq 1$.

*Proof.* Expand $(1+t)^d$ binomially. The subgroups of $\mathbb Z/n$ correspond to the divisors $d\mid n$, and the subgroup of order $d$ contains $\binom dk$ $k$-subsets. Möbius inversion over the divisor lattice counts the $k$-subsets that lie in no proper subgroup. This is P. Hall's Eulerian-function argument [22] in subset form. ∎

**Lemma B (convexity in $\log x$).** For $n\geq 1$, $v\mapsto M(e^v,n)$ is convex on $v\geq 0$.

*Proof.* $n\frac{d^2}{dv^2}M(e^v,n)=\sum_{d\mid n}\mu(n/d)\,d^2e^{vd}$. With $e^v=1+t$, $t\geq 0$, the coefficient of $t^k$ is $\sum_{d\mid n}\mu(n/d)\,d^2\binom dk$. By the same inclusion–exclusion, this counts the triples $(x,y,B)$ with $x,y\in\mathbb Z/n$ and $B$ a $k$-subset such that $\{x,y\}\cup B$ lies in no proper subgroup; the subgroup of order $d$ contains $d^2\binom dk$ such triples. So the coefficient is non-negative. ∎

**Remarks.**
1. *Exact checks.* For $q\leq 25$ and $n\leq 30$, the realisable range found by exact integer arithmetic agrees with Theorem 2. Lemmas A–B hold for $n\leq 150$. Their combinatorial interpretations match brute-force enumeration for $n\leq 12$ (Lemma A) and $n\leq 8$ (Lemma B). See §8.
2. *Comparison with Paper 71* [21].
   - Signed characters realise $1-au+qu^2$ for all $|a|\leq q$. Both signs of $a$ occur. The range contains numerators satisfying RH ($|a|<2\sqrt q$, roots on $|\omega|=\sqrt q$) and, once $q\geq 5$, violations with real roots of either sign ($2\sqrt q<|a|\leq q$).
   - Deletion alone realises only $\lceil 2\sqrt q\,\rceil\leq a\leq q+1$, where both roots are real and lie in $[1,q]$. In genus one every violation of RH has real roots, so the contrast with [21] lies in the realisable range, not in the type of violation.
   - The lower end $a\geq 2\sqrt q$ is the genus-one form of Corollary 1(b). The numerator has only two roots, so a non-real conjugate pair would leave no zero at the positive real point of its circle.
   - That contradicts Pringsheim's theorem for the non-negative series $\sum_n(s_n-1)u^n/n$, which must be singular at $u=q^{-1/2}$. Yet the series is analytic there when $a<2\sqrt q$, because $2-a/\sqrt q>0$.
   - Over $\mathbb Q$, by contrast, Proposition 1 allows zeros at any height alongside the dominating real zero.
3. *Edge cases.*
   - At $a=q+1$, $\omega_1=q$ and $\omega_2=1$. Then $Z(u)=1$: every irreducible is deleted, and indeed $d_n=M(q,n)+M(1,n)-[n=1]=\pi_q(n)$, since $M(1,n)=[n=1]$.
   - At $a=2\sqrt q$ ($q$ a square), $\omega_1=\omega_2=\sqrt q$, a double real root.

**Higher genus.** In genus one the off-circle roots of every fake are real, so Theorem 2 cannot tell whether deletion forces real violations. From genus two on, a fake can have non-real off-circle roots, and the question is whether deletion can realise one. Call $Z(u)=P(u)/((1-u)(1-qu))$, with $P\in\mathbb Z[u]$ of degree $2g$ and $P(1/(qu))=P(u)/(q^gu^{2g})$, a *genus-$g$ fake*. It is realisable by deletion when $d_n=\frac1n\sum_{k\mid n}\mu(n/k)(s_k-1)\in[0,\pi_q(n)]$ for all $n$, where $s_k$ is the $k$-th power sum of the inverse roots of $P$. The bookkeeping in the proof of Theorem 2 applies verbatim, and integrality is automatic.

**Theorem 2′.**
- (a) In genus $g\leq 2$, every off-circle inverse root (one with $|\omega|\neq\sqrt q$) of a deletion-realisable fake is real.
- (b) For every prime power $q\geq 8$, the genus-3 fake with

$$
P_q(u)=\bigl(1-qu+qu^2\bigr)\bigl(1+(2q+1)u^2+q^2u^4\bigr)
$$

  is realisable by deletion. Its inverse roots are $A$ and $q/A$, with $A=\tfrac12\bigl(q+\sqrt{q^2-4q}\bigr)$, together with the four non-real numbers $\pm ir_-$ and $\pm ir_+$, where $r_\pm=\tfrac12\bigl(\sqrt{4q+1}\pm1\bigr)$. Since $r_-<\sqrt q<r_+$, these four lie off the circle $|\omega|=\sqrt q$.

So non-real violations of RH by deletion first appear in genus 3. As over $\mathbb Q$ (Corollary 1(b)), they always come with a dominating real root: here $A>r_+$.

*Proof of (a).*
- Genus 1 is Theorem 2.
- In genus 2, let $\omega$ be a non-real inverse root with $|\omega|\neq\sqrt q$. The functional equation and real coefficients make $\omega,\bar\omega,q/\omega,q/\bar\omega$ four distinct roots, so these are all the roots, and the maximal modulus $R_{\max}=\max(|\omega|,q/|\omega|)>1$ is attained only by non-real roots.
- The series $\sum_n(s_n-1)u^n/n=-\log P(u)+\log(1-u)$ has non-negative coefficients for a deletion fake and radius $1/R_{\max}<1$. By Pringsheim it must be singular at $u=1/R_{\max}$. But $P(1/R_{\max})\neq0$, since no inverse root of modulus $R_{\max}$ is real and positive, and $1/R_{\max}\neq 1$. So the series is analytic there, a contradiction. ∎

*Proof of (b).* $P_q$ satisfies the genus-3 functional equation, and $1+(2q+1)u^2+q^2u^4=(1+iu+qu^2)(1-iu+qu^2)$ gives the stated roots, with $r_-r_+=q$. Since $\cos(n\pi/2)$ kills odd powers,

$$
s_n=A^n+(q/A)^n+2\cos(n\pi/2)\bigl(r_-^n+r_+^n\bigr).
$$

- *Small $n$, exactly.* $s_1=q$, $s_2=q^2-6q-2$, $s_3=q^3-3q^2$, $s_4=q^4-4q^3+6q^2+8q+2$. Hence:
  - $d_1=q-1\in[0,q]$;
  - $d_2=\tfrac12(q^2-7q-2)$, which lies in $[0,\tfrac12(q^2-q)]$ exactly when $q\geq 8$;
  - $d_3=\tfrac13(q^3-3q^2-q)\in[0,\pi_q(3)]$;
  - $d_4=\tfrac14(q^4-4q^3+5q^2+14q+4)\leq\tfrac14(q^4-q^2)=\pi_q(4)$.
- *Bounds for $q\geq 8$.*
  - $A\in[q-1.5,q-1]$ and $q/A\in[1,1.5]$.
  - $r_+\leq\sqrt q+1\leq A$ and $r_+/A\leq(\sqrt q+1)/(q-1.5)\leq 0.589$.
  - Hence $|s_k|\leq 6A^k$, and $\sum_{k\leq n/2}6A^k\leq 7.1\,A^{n/2}$.
- *Lower bound, $n\geq5$.* Since $n\,d_n=\sum_{k\mid n}\mu(n/k)s_k$ for $n\geq 2$,

$$
n\,d_n\geq s_n-\sum_{k\leq n/2}|s_k|\geq A^n\bigl(1-4(r_+/A)^n-7.1A^{-n/2}\bigr)>0,
$$

  because $4(0.589)^5+7.1\cdot 6.5^{-5/2}<0.35$ and both terms decrease in $n$ and $q$.
- *Upper bound, $n\geq5$.*
  - We have

$$
n\bigl(\pi_q(n)-d_n\bigr)\geq q^n-s_n-\sum_{k\leq n/2}\bigl(q^k+|s_k|\bigr)\geq q^n-(q-1)^n-1.5^n-4(\sqrt q+1)^n-8.3\,q^{n/2}.
$$

  - Also $q^n-(q-1)^n\geq q^n\bigl(1-e^{-n/q}\bigr)\geq 2.5\,q^{n-1}$ for $n\geq5$.
  - Here $\sum_{k\leq n/2}q^k\leq\tfrac{q}{q-1}q^{n/2}\leq 1.15\,q^{n/2}$ and $\sum_{k\leq n/2}|s_k|\leq 7.1\,A^{n/2}\leq 7.1\,q^{n/2}$. The subtracted terms, divided by $q^{n-1}$, total less than $1.18$ at $(q,n)=(8,5)$ and decrease in both $n$ and $q$.
- So $0\leq d_n\leq\pi_q(n)$ for all $n$. Choosing $d_n$ irreducibles of each degree $n$ realises $Z$. ∎

*Remark.* The family fails exactly at $n=2$ for $q\leq 7$. Two exact computations agree with Theorem 2′ (§8):
- integer checks to $n\leq 80$ for 13 prime powers $8\leq q\leq 32$;
- an exploratory search over genus-3 fakes of the form $(1-au+qu^2)Q(u)$, where $Q$ has four non-real off-circle roots, for $q\in\{9,16,25\}$.

In that search every example realisable to $n\leq 80$ had a dominating real root.

## 5. Integers of painted deletion sets

**Setting.** Fix $1/2<\alpha<1$ and put $\kappa=1-\alpha\in(0,1/2)$. Let $m$ be a pattern with $g\geq 0$, and assume in this section that $m\geq 0$ (a *pure zero pattern*) and $m(0)\geq 1$. Given $g\geq 0$, the condition $m(0)\geq 1$ only excludes $m\equiv 0$. That case gives $S=\varnothing$ and a bounded integer error. Then $M:=g(0)=\sum_\gamma m(\gamma)=\max g$. Put

$$
q_p=\min\bigl(1,\ p^{-\kappa}g(\log p)\bigr)\in[0,1].
$$

The *painted random deletion set* $S$ contains each prime $p$ independently with probability $q_p$.

Its *mean system* is the multiplicative function $g_0$ with $g_0(p^k)=1-q_p$ for $k\geq 1$, the expectation of the $S$-free indicator. Write $N_0(y)=\sum_{n\leq y}g_0(n)$, $a_0=\prod_p(1-q_p/p)$ and $E_0(y)=N_0(y)-a_0y$. The exponent $\theta_\ast $ is that of [1, Thm 3]:

$$
\theta_\ast (\alpha)=\begin{cases}\alpha/2, & 1/2<\alpha\leq 2/3,\\ (4\alpha-1)/5, & 2/3<\alpha\leq 3/4,\\ 1/(4-2\alpha), & 3/4<\alpha<1.\end{cases}
$$

**Why poles are excluded.** Suppose instead that $m(\gamma)<0$ for some $\gamma$. By the factorisation below, the Dirichlet series $G(s)=\sum g_0(n)n^{-s}=\zeta(s)\prod_p(1-q_pp^{-s})$ then has a pole of order $r=|m(\gamma)|$ at $\alpha+i\gamma$, provided $\zeta(\alpha+i\gamma)\neq 0$ (true under RH). In that case $E_0(y)\neq o(y^\alpha)$.
- Suppose $E_0(y)=o(y^\alpha)$.
- Then $G(s)-a_0s/(s-1)=s\int_1^\infty E_0(y)y^{-s-1}\,dy$ continues analytically to $\operatorname{Re}s>\alpha$.
- It satisfies $|G(\sigma+i\gamma)|=o\bigl(1/(\sigma-\alpha)\bigr)$ as $\sigma\to\alpha^+$, contradicting $|G(\sigma+i\gamma)|\asymp(\sigma-\alpha)^{-r}$.

So with a pole, square-root regularity at scale $y^{\alpha/2}$ is impossible for the mean system.

**Factorisation.** For each uncapped prime ($q_p<1$; all but finitely many),

$$
q_pp^{-s}=\sum_\gamma m(\gamma)\,p^{-(s+\kappa-i\gamma)}
$$

exactly. Hence

$$
\prod_p\bigl(1-q_pp^{-s}\bigr)=\prod_\gamma\zeta(s+\kappa-i\gamma)^{-m(\gamma)}\cdot H(s),\qquad H(s)=\prod_pH_p(s),
$$

where $H_p(s)=(1-q_pp^{-s})\prod_\gamma\bigl(1-p^{-(s+\kappa-i\gamma)}\bigr)^{-m(\gamma)}$.
- For uncapped $p$, $\log H_p(s)=O\bigl(M^2p^{-2(\sigma+\kappa)}\bigr)$. So the product $H$ converges absolutely and does not vanish on $\operatorname{Re}(s+\kappa)>1/2$.
- *Coefficients of $H_p$.* Put $w=p^{-\kappa-s}$ and $\theta_\gamma=\gamma\log p$.
  - For uncapped $p$, $H_p=\bigl(1-\sum_\gamma m(\gamma)e^{i\theta_\gamma}w\bigr)\prod_\gamma(1-e^{i\theta_\gamma}w)^{-m(\gamma)}$.
  - For capped $p$, $H_p=(1-p^{\kappa}w)\prod_\gamma(1-e^{i\theta_\gamma}w)^{-m(\gamma)}$, and $p^\kappa\leq g(\log p)\leq M$.
  - Since $m\geq 0$, the $w^k$-coefficients of the product have modulus at most those of $(1-w)^{-M}$, namely $\tau_M(p^k)$.
  - So the Dirichlet coefficient of $H$ at $p^k$ is $\eta(p^k)=c_kp^{-k\kappa}$ with $|c_k|\leq\tau_M(p^k)+M\tau_M(p^{k-1})\leq(M+1)\tau_M(p^k)$. For uncapped $p$, $c_1=0$.

Write the Dirichlet coefficients of $\prod_p(1-q_pp^{-s})$ as $h(d)=d^{-\kappa}\ell(d)$, where

$$
\ell=\beta\ast \eta',\qquad\beta=\mathop{\ast}_\gamma\bigl(\mu\cdot(\cdot)^{i\gamma}\bigr)^{\ast m(\gamma)},\qquad\eta'(b)=\eta(b)\,b^{\kappa}.
$$

Then:
- (L1) $|\beta(a)|\leq\tau_M(a)$.
- (L2) $|\eta'(p^k)|\leq(M+1)\tau_M(p^k)$ for every $p$ and $k\geq 1$, and $\eta'(p)=0$ for uncapped $p$. So $\eta'$ is supported on squarefull numbers times products of capped primes.
- (L3) $|\ell(d)|\leq\sum_{ab=d}\tau_M(a)(M+1)^{\omega(b)}\tau_M(b)\leq(M+1)^{\omega(d)}\tau_{2M}(d)\ll_\varepsilon d^{\varepsilon}$.

Since $G(s)=\zeta(s)\prod_p(1-q_pp^{-s})$, we have $g_0=1\ast h$ and $N_0(y)=\sum_{d\leq y}h(d)\lfloor y/d\rfloor$. Let $\bar B_1(u)=u-\lfloor u\rfloor-\tfrac12$.

**Lemma C (partial sums; RH).** Assume RH and $m\geq 0$. Then $\sum_{d\leq x}\ell(d)\ll_\varepsilon x^{1/2+\varepsilon}$. Consequently:
- $\sum_{d\leq x}h(d)\ll x^{1/2-\kappa+\varepsilon}$;
- $\sum_{d>y}h(d)/d\ll y^{-1/2-\kappa+\varepsilon}$;
- $E_0(y)=-\mathcal T(y)+O(y^{1/2-\kappa+\varepsilon})$, where $\mathcal T(y):=\sum_{d\leq y}h(d)\bar B_1(y/d)$.

*Proof.*
1. **Analyticity.** The Dirichlet series of $\ell$ is $L(s)=\prod_\gamma\zeta(s-i\gamma)^{-m(\gamma)}H(s-\kappa)$. Under RH and $m\geq 0$ it is analytic on $\operatorname{Re}s>1/2$: it contains only factors $1/\zeta$, and these vanish rather than blow up at $s=1+i\gamma$.
2. **Growth on $\sigma\geq 1/2+\varepsilon$.**
   - Under RH, $|1/\zeta(\sigma+it)|\ll_\varepsilon(|t|+2)^{\varepsilon}$ uniformly for $\sigma\geq 1/2+\varepsilon$ and $|t|\geq 1$ [9, §14.2]. On bounded regions $1/\zeta$ is analytic, hence bounded.
   - $H(s-\kappa)=\sum_b\eta'(b)b^{-s}$ converges absolutely there. By (L2),

$$
\sum_b|\eta'(b)|b^{-\sigma}\leq\prod_{p\ \mathrm{capped}}\Bigl(\sum_{k\geq 0}(M+1)\tau_M(p^k)p^{-k\sigma}\Bigr)\prod_{p\ \mathrm{uncapped}}\Bigl(1+(M+1)\sum_{k\geq 2}\tau_M(p^k)p^{-k\sigma}\Bigr).
$$

     The first product is finite. Each factor of the second is $1+O_M(p^{-2\sigma})$, uniformly for $\sigma\geq 1/2+\varepsilon$.
   - Hence $|L(\sigma+it)|\ll(|t|+2)^{M\varepsilon}$ there.
3. **Perron.** Take $c=1+1/\log x$ and $T=x$. The truncated Perron formula [3, Cor. 5.3], with $|\ell(d)|\ll d^\varepsilon$ from (L3), gives

$$
\sum_{d\leq x}\ell(d)=\frac{1}{2\pi i}\int_{c-iT}^{c+iT}L(s)\frac{x^s}{s}\,ds+O\bigl(x^{1+\varepsilon}/T+x^{\varepsilon}\bigr).
$$

   - Shift the contour to $\operatorname{Re}s=1/2+\varepsilon$; no singularity is crossed.
   - The new vertical segment contributes $\ll x^{1/2+\varepsilon}T^{M\varepsilon}\log T$.
   - The horizontal segments contribute $\ll T^{M\varepsilon-1}x^{c}$.
   - So $\sum_{d\leq x}\ell(d)\ll x^{1/2+(M+2)\varepsilon}$. Rename $\varepsilon$.
4. **Consequences.**
   - Partial summation with $h(d)=d^{-\kappa}\ell(d)$ and $0<\kappa<1/2$ gives the two bounds for $h$.
   - Insert $\lfloor u\rfloor=u-\tfrac12-\bar B_1(u)$ into $N_0(y)$ and use $a_0=\sum_dh(d)/d$. This gives the identity

$$
E_0(y)=-y\sum_{d>y}\frac{h(d)}{d}-\frac12\sum_{d\leq y}h(d)-\mathcal T(y),
$$

     exactly as in [1, Lemma 2], and hence the last claim. ∎

**Lemma D (dyadic block; RH).** Assume RH, $m\geq 0$ and $10\sqrt y\leq D\leq y/2$. Let $w$ be the smooth dyadic weight of [1, Prop. 6], supported in $[1/2,2]$. Then

$$
\mathcal S_D:=\sum_dh(d)\,w(d/D)\,\bar B_1(y/d)\ll_\varepsilon y^{1/3+\varepsilon}D^{1/3-\kappa}.
$$

*Proof.* Take $H=\lceil D^{2/3}y^{-1/3}\rceil$, so that $8Hy\leq D^2$, as in [1, Prop. 6]. Indeed $8Hy\leq 8D^{2/3}y^{2/3}+8y\leq(8\cdot100^{-2/3}+0.08)D^2<D^2$ for $D\geq10\sqrt y$. Vaaler's trigonometric polynomial [28] gives

$$
|\mathcal S_D|\leq\sum_{1\leq|j|\leq H}|c_j|\,|U(j)|+\sum_d|h(d)|\,w(d/D)\,\frac{F_H(y/d)}{2H+2},
$$

with $|c_j|\leq 1/(2\pi|j|)$, $U(j):=\sum_dh(d)w(d/D)e(jy/d)$, and $F_H$ the Fejér kernel.

- **Twisted sums.**
  - With $f(u)=u^{-\kappa}w(u/D)e(jy/u)$ as in [1, Lemma 4], $U(j)=\frac{1}{2\pi i}\int_{(2)}\tilde f(s)L(s)\,ds$.
  - Move the line to $\operatorname{Re}s=1/2+\varepsilon$. Under RH no singularity is crossed, and the horizontal segments vanish by [1, Lemma 3].
  - Using $|L(1/2+\varepsilon+it)|\ll(1+|t|)^{M\varepsilon}$, [1, Lemma 3] gives $U(j)\ll D^{1/2-\kappa+\varepsilon}(jy/D)^{1/2+\varepsilon}$.
  - Summing against $|c_j|$ over $j\leq H$ gives $\ll y^{1/3+3\varepsilon}D^{1/3-\kappa}$.
- **Fejér term.**
  - $\frac{F_H(u)}{2H+2}\leq\frac12\min\bigl(1,(2(H+1)\lVert u\rVert)^{-2}\bigr)$.
  - Group $d\in[D/2,2D]$ by the integer $n$ nearest to $y/d$ (so $n\asymp y/D$, which gives $O(y/D)$ values) and by shells $\lVert y/d\rVert\in[k/H,(k+1)/H)$, $0\leq k\leq H/2$.
  - Each cell $(n,k)$ is an interval of $d$ of length $\asymp y/(Hn^2)\asymp D^2/(yH)$, so it contains $\ll D^2/(yH)+1$ integers. On it the kernel is $\ll\max(1,k)^{-2}$, and $|h(d)|\ll D^{-\kappa+\varepsilon}$ by (L3).
  - Summing over cells gives

$$
\ll D^{-\kappa+\varepsilon}\cdot\frac yD\Bigl(\frac{D^2}{yH}+1\Bigr)\ll D^{-\kappa+\varepsilon}\Bigl(\frac DH+\frac yD\Bigr).
$$

  - Finally, $D/H\asymp y^{1/3}D^{1/3}$, and $y/D\leq y^{1/3}D^{1/3}$ because $D\geq\sqrt y$. ∎

*Remark.* Paper [1] used $|\mu|\leq 1$ and Kusmin–Landau for the Fejér term. Here the coefficients are not smooth, and the pointwise bound (L3) with window counting suffices, at a cost of $D^\varepsilon$. No Brun–Titchmarsh-type input, such as Shiu's theorem, is needed. One would in any case be unavailable at $D\asymp\sqrt y$, where the windows have bounded length.

**Theorem 3 (integers of painted deletion sets; RH).** Assume RH, $1/2<\alpha<1$, $g\geq 0$, $m\geq 0$ and $m(0)\geq 1$. Implied constants depend on $\varepsilon$, $\alpha$ and the pattern $m$, including its heights $\gamma$. In (b) they also depend on the random set.
- (a) $E_0(y)\ll_\varepsilon y^{\theta_\ast (\alpha)+\varepsilon}$.
- (b) Almost surely, for every $\varepsilon>0$, $N_S(x)=a_Sx+O(x^{\theta_\ast (\alpha)+\varepsilon})$, with $a_S=\prod_{p\in S}(1-1/p)>0$. In particular, for $1/2<\alpha\leq 2/3$,

$$
N_S(x)=a_Sx+O\bigl(x^{\alpha/2+\varepsilon}\bigr)\quad\text{almost surely,}
$$

  while $F_S$ has zeros of order $m(\gamma)$ at every $\alpha+i\gamma$ (Proposition 1).
- (c) (Sharpness.) For every $\eta>0$, almost surely $N_S(x)-a_Sx\neq O(x^{\alpha/2-\eta})$. So for $1/2<\alpha\leq 2/3$ the exponent $\alpha/2$ in (b) is attained exactly, as it is for unpainted sets [1, Thm 2].

*Proof of (a).* Follow [1, Thm 3], with Lemma C in place of [1, Lemma 2] and Lemma D in place of [1, Prop. 6]. Use the same partition: $Y_1=5\sqrt y$, $Y_2=y/\mathcal M$, and dyadic blocks $D=2^jY_1$ with $1\leq j\leq J$.
- *Low part* ($d\leq 2Y_1$). By (L3), $\sum_{d\leq 10\sqrt y}|h(d)|\ll\sum_{d\leq 10\sqrt y}d^{-\kappa+\varepsilon}\ll y^{(1-\kappa)/2+\varepsilon}=y^{\alpha/2+\varepsilon}$.
- *Middle part.* Lemma D on each of the $O(\log y)$ blocks gives $\ll y^{1/3+\varepsilon}\max\bigl(Y_1^{1/3-\kappa},Y_2^{1/3-\kappa}\bigr)$.
- *High part* ($d>2^JY_1>y/(2\mathcal M)$).
  - Group $d$ by $n=\lfloor y/d\rfloor\leq 2\mathcal M$.
  - On $I_n=(y/(n+1),y/n]$ the weight $W(d)=d^{-\kappa}\bigl(1-w_0(d/2^JY_1)\bigr)\bar B_1(y/d)$ has size and total variation $\ll(y/n)^{-\kappa}$, since $\bar B_1(y/d)=y/d-n-\tfrac12$ is monotone there.
  - Partial summation with Lemma C gives $\sum_{d\in I_n}\ell(d)W(d)\ll(y/n)^{1/2-\kappa+\varepsilon}$.
  - Summing over $n\leq 2\mathcal M$ gives $\ll y^{1/2-\kappa+\varepsilon}\mathcal M^{1/2+\kappa}$.
- *Choice of $\mathcal M$*, as in [1].
  - For $\alpha\leq 2/3$ ($\kappa\geq 1/3$), take $\mathcal M=4$. The middle part peaks at $D\asymp\sqrt y$ with $y^{1/3+(1/3-\kappa)/2}=y^{\alpha/2}$, and the high part is $y^{\alpha-1/2}\leq y^{\alpha/2}$. The total is $y^{\alpha/2+2\varepsilon}$.
  - For $2/3<\alpha\leq 3/4$, take $\mathcal M=y^{1/5}$. Both the middle and high parts are $y^{(4\alpha-1)/5+2\varepsilon}$.
- *Case $\alpha>3/4$.* [1, Lemma 1] applies verbatim. Its inputs are $0\leq g_0\leq 1$ and $G(\sigma+it)\ll|t|^{\max(1/2-\sigma,0)+\varepsilon}$ for $c\leq\sigma\leq 2$, $|t|\geq 1$, with $c\in(\alpha-1/2,1/2)$.
  - The second input holds by Lindelöf under RH for $\zeta(s)$.
  - It also uses the bounds of Lemma C, step 2, for the painted factor $\prod_\gamma\zeta(s+\kappa-i\gamma)^{-m(\gamma)}H(s)$ on $\operatorname{Re}(s+\kappa)\geq 1/2+\varepsilon$. ∎

*Proof of (b).* Follow [1, §§5–6]. Let $\xi_p=1_{p\in S}$ and $\eta_p=\xi_p-q_p$. Let $z$ be the random multiplicative function with $z(p^k)=-\eta_pq_p^{k-1}$. Then $|z|\leq 1$, the factors are independent across primes, and $\mathbb Ez(n)=0$ for $n>1$.
- *Exact factorisation* [1, Lemma 7]. $\mathbf 1_{\mathcal N_S}=g_0\ast z$. The local identity $\frac{1-\xi_pu}{1-u}=\frac{1-q_pu}{1-u}\cdot\frac{1-\xi_pu}{1-q_pu}$ uses only $q_p\in[0,1]$.
- *Moments* [1, Lemma 8]. Let $\tau\in(\alpha/2,1)$ and $|w_d|\leq Wd^{-\tau}$. Then $\mathbb E\bigl(\sum_dz(d)w_d\bigr)^{2k}\leq K'W^{2k}$ with $K'<\infty$. The proof of [1] applies with two changes.
  - (a) [1] bounds $q_pp^{-\tau}$ using $q_p=p^{-\kappa}$. Here, instead, $q_p\leq1$ and $\tau>\alpha/2>1/4$ give $q_pp^{-\tau}\leq p^{-\tau}\leq 2^{-1/4}$ for every prime, capped or not. So the bracket $p^{-\tau}/(1-q_pp^{-\tau})$ is at most $(1-2^{-1/4})^{-1}p^{-\tau}$.
  - (b) For uncapped primes, $q_p\leq Mp^{-\kappa}$. The local factor is $1+O_{k,M}(p^{-\kappa-2\tau})$, and $\sum_pp^{-\kappa-2\tau}<\infty$ because $\kappa+2\tau>\kappa+\alpha=1$.
- *The constant.* $\mathbb E\sum_d|z(d)|/d\leq\prod_p\bigl(1+2q_p/p+O(q_pp^{-2})\bigr)<\infty$, since $q_p\leq Mp^{-\kappa}$. So $a_S=a_0\sum_dz(d)/d=\prod_p(1-\xi_p/p)$, exactly as in [1].
- *Conclusion.* The decomposition of $N_S(x)-a_Sx$ into $\sum_dz(d)E_0(x/d)$ plus random terms, the moment bounds, and the Borel–Cantelli argument of [1, Prop. 9] apply verbatim, with part (a) in place of [1, Thm 3]. ∎

*Proof of (c).* Follow [1, Thm 2 and Prop. 14]. Put

$$
R(s)=\sum_{p\ \mathrm{uncapped}}\eta_pp^{-s},\qquad v(\sigma)=\sum_{p\ \mathrm{uncapped}}q_p(1-q_p)p^{-2\sigma},
$$

and let $P(w)=\sum_pp^{-w}$ be the prime zeta function.
- *Variance.* $\sum_pq_p^2p^{-2\sigma}$ converges at $\sigma=\alpha/2$, because $2\kappa+\alpha>1$. Also $\sum_pq_pp^{-2\sigma}=\sum_\gamma m(\gamma)P(\kappa+2\sigma-i\gamma)+O(1)$, where $\kappa+2\sigma=1+2(\sigma-\alpha/2)$.
  - As $\sigma\downarrow\alpha/2$, the term $\gamma=0$ is $m(0)\log\frac{1}{\sigma-\alpha/2}+O(1)$.
  - The terms $\gamma\neq 0$ stay bounded, since $P(1+\delta-i\gamma)\to\log\zeta(1-i\gamma)+O(1)$.
  - Hence $v(\sigma)=m(0)\log\frac{1}{\sigma-\alpha/2}+O(1)\to\infty$.
- *The two lemmas of [1].* The proofs of [1, Lemmas 12 and 13] use only independence, $|\eta_p|\leq 1$, the bound $v(\sigma)\leq M\,P(\kappa+2\sigma)$ (from $q_p\leq Mp^{-\kappa}$) and $v(\sigma)\to\infty$. So they hold verbatim: almost surely, $R(\sigma)=o\bigl(\log\frac1{\sigma-\alpha/2}\bigr)$, and $R(\sigma)$ is unbounded as $\sigma\downarrow\alpha/2$.
- *Expansion.* For uncapped $p$,

$$
\log\bigl(1-\xi_pp^{-s}\bigr)=\sum_\gamma m(\gamma)\log\bigl(1-p^{-(s+\kappa-i\gamma)}\bigr)-\eta_pp^{-s}+\sum_{k\geq 2}\frac{\sum_\gamma m(\gamma)p^{-k(\kappa-i\gamma)}-\xi_p}{k}\,p^{-ks}.
$$

  Sum over $p$ for $\operatorname{Re}s>\alpha$, where every sum converges absolutely. For the $\eta$-sum this holds only almost surely: $|\eta_p|=1-q_p$ for $p\in S$, and $\sum_{p\in S}p^{-\sigma}<\infty$ almost surely for $\sigma>\alpha$. The capped primes contribute a finite term. Each resulting piece continues analytically to $\operatorname{Re}s>\alpha/2$, the random one almost surely. The first piece is a logarithm and is multivalued around $\alpha+i\gamma$. The exponential of the sum of the pieces, however, is the single-valued product $\prod_\gamma\zeta(s+\kappa-i\gamma)^{-m(\gamma)}e^{-R(s)+K(s)}C(s)$, as in the proof of Proposition 1. Here $K$ collects the terms with $k\geq2$ and $C$ is the finite product over capped primes. Almost surely this product is analytic on $\operatorname{Re}s>\alpha/2$. It equals $F_S$ on $\operatorname{Re}s>\alpha$, hence on the whole half-plane. Taking real parts therefore gives an identity for $\log|F_S|$, with $F_S$ the continuation of Proposition 1, on the real segment $(\alpha/2,\alpha)$. There we let $\sigma\downarrow\alpha/2$. For $\alpha/2<\sigma<\alpha$ the separate prime sums of the first two pieces diverge; only their continuations are used.
  - The first piece continues as $-\sum_\gamma m(\gamma)\log\zeta(s+\kappa-i\gamma)$, which is analytic on $\operatorname{Re}s>\alpha/2$ away from $s=\alpha+i\gamma$ under RH, since $\operatorname{Re}(s+\kappa)>1/2$. Its real part stays bounded as $\sigma\downarrow\alpha/2$, because $\zeta(1-\alpha/2-i\gamma)\neq 0$.
  - The terms with $k\geq 3$ are bounded, as in [1, Thm 2, Step 2].
  - In the $k=2$ term, $\sum_p\sum_\gamma m(\gamma)p^{-2\kappa+2i\gamma-2\sigma}$ is bounded, and $-\tfrac12\sum_p\xi_pp^{-2\sigma}=-\tfrac12\sum_pq_pp^{-2\sigma}-\tfrac12R(2\sigma)=-\tfrac{m(0)}2\log\frac1{\sigma-\alpha/2}+O(1)$. Here $R(2\sigma)$ is bounded because $R$ is analytic on $\operatorname{Re}s>\alpha/2$.
  - Hence $\log|F_S(\sigma)|=-R(\sigma)-\tfrac{m(0)}2\log\frac1{\sigma-\alpha/2}+O(1)$.
- *Conclusion.* Suppose $N_S(x)-a_Sx=O(x^{\alpha/2-\eta})$.
  - As in [1, Thm 2, Step 1], the hypothesis makes $f_S=\zeta F_S=\frac{a_Ss}{s-1}+s\int_1^\infty(N_S-a_Sx)x^{-s-1}dx$ analytic on $\operatorname{Re}s>\alpha/2-\eta$ except at $1$. Since $\zeta(\alpha/2)\neq0$, the function $F:=f_S/\zeta$, defined by this integral representation, is analytic near $\alpha/2$ and not identically zero, and $F=F_S$ on $(\alpha/2,\alpha/2+\delta)$. Here $F_S$ is the continuation of Proposition 1, analytic on $\operatorname{Re}s>\alpha/2$ under RH since $m\geq 0$.
  - So $\log|F_S(\sigma)|=m'\log(\sigma-\alpha/2)+O(1)$ for some integer $m'\geq 0$, and therefore $R(\sigma)=(m'-\tfrac{m(0)}2)\log\frac1{\sigma-\alpha/2}+O(1)$.
  - If $m'\neq m(0)/2$, this contradicts $R=o(\log)$. If $m'=m(0)/2$, which can happen when $m(0)$ is even, then $R$ is bounded, contradicting its unboundedness. ∎

**Proposition 4 (the painted zeros in the primes; RH).** Assume RH, $1/2<\alpha<1$ and $g\geq 0$; here $m$ may take negative values. Almost surely,

$$
\psi_{\mathbb P\setminus S}(x)=x-\sum_\gamma m(\gamma)\frac{x^{\alpha+i\gamma}}{\alpha+i\gamma}+O\bigl(x^{1/2}\log^2x\bigr).
$$

*Proof.* Under RH, $\psi(x)=x+O(x^{1/2}\log^2x)$ and $\vartheta(x)=x+O(x^{1/2}\log^2x)$ [3, Ch. 13]. Moreover $\psi_{\mathbb P\setminus S}(x)=\psi(x)-D(x)+O(x^{1/2})$, where $D(x)=\sum_{p\in S,\,p\leq x}\log p$; the prime powers $p^k\leq x$ with $k\geq 2$ contribute $O(x^{1/2})$.
- *Mean.* For uncapped $p$, $q_p\log p=\sum_\gamma m(\gamma)p^{\alpha-1+i\gamma}\log p$. Partial summation against $\vartheta$ gives

$$
\sum_{p\leq x}q_p\log p=\sum_\gamma m(\gamma)\Bigl(\frac{x^{\alpha+i\gamma}}{\alpha+i\gamma}+O\bigl(x^{\alpha-1/2}\log^2x\bigr)\Bigr)+O(1).
$$

- *Fluctuation.* $D(x)-\sum_{p\leq x}q_p\log p=\sum_{p\leq x}\eta_p\log p$ is a martingale in $x$. Its increments are bounded by $\log x$, and its conditional variance up to $X$ is $\leq\sum_{p\leq X}q_p\log^2p\ll X^\alpha\log X$.
  - Freedman's inequality [29] gives $\mathbb P\bigl(\max_{x\leq X}|\sum_{p\leq x}\eta_p\log p|>X^{\alpha/2}\log^2X\bigr)\leq 2\exp(-c\log^3X)$.
  - Applying this at $X=2^j$ with Borel–Cantelli, almost surely the fluctuation is $O(x^{\alpha/2}\log^2x)$, which is $O(x^{1/2})$.
- Combine. ∎

So the painted zeros appear as explicit oscillations $-m(\gamma)x^{\alpha+i\gamma}/(\alpha+i\gamma)$ of size $x^\alpha$ in the primes. For $m\geq 0$ and $\alpha\leq 2/3$, the integer count stays within $x^{\alpha/2+\varepsilon}$ of $a_Sx$ (Theorem 3).

**Proposition 5 (secondary lines; RH).** Corollary 1(b) constrains only the abscissa line. Let $1/2<\alpha'<\alpha<1$, let $m_0\geq1$ be an integer, and let $g'(u)=\sum_{\gamma'}m'(\gamma')e^{i\gamma'u}$ be a real trigonometric polynomial with integer coefficients $m'(\gamma')\geq 0$ for $\gamma'\neq 0$ and $m'(0)=0$. Put $q_p=\min\bigl(1,\max\bigl(0,\,m_0p^{\alpha-1}+p^{\alpha'-1}g'(\log p)\bigr)\bigr)$; the truncations act on finitely many $p$.
- Almost surely, $F_S$ is meromorphic on $\operatorname{Re}s>\alpha/2$. Its zeros there are a zero of order $m_0$ at $\alpha$ and zeros of order $m'(\gamma')$ at $\alpha'+i\gamma'$, with no real zero at $\alpha'$.
- Theorem 3(a)–(c) and Proposition 4 hold with $m(0)$ replaced by $m_0$. In particular, for $1/2<\alpha\leq 2/3$, almost surely $N_S(x)=a_Sx+O(x^{\alpha/2+\varepsilon})$, and the exponent is attained.
- The primes carry the additional terms $-m'(\gamma')x^{\alpha'+i\gamma'}/(\alpha'+i\gamma')$.

*Proof.* Only these steps change.
- *Mean factor.* For all large $p$, $q_pp^{-s}=m_0p^{-(s+\kappa)}+\sum_{\gamma'}m'(\gamma')p^{-(s+\kappa'-i\gamma')}$ with $\kappa'=1-\alpha'$. So $\prod_p(1-q_pp^{-s})=\zeta(s+\kappa)^{-m_0}\prod_{\gamma'}\zeta(s+\kappa'-i\gamma')^{-m'(\gamma')}H(s)$.
- *Coefficient bound.* In the variable $w=p^{-\kappa-s}$ the secondary factors carry $p^{\kappa-\kappa'}e^{i\gamma'\log p}$, which has modulus at most $1$. So (L1)–(L3) hold with $M=m_0+\sum_{\gamma'}m'(\gamma')$.
- *Lemma C.* $L(s)$ gains the factors $\zeta(s+\alpha-\alpha'-i\gamma')^{-m'(\gamma')}$. These are analytic on $\operatorname{Re}s>1/2-(\alpha-\alpha')$ and, under RH, $\ll|t|^{\varepsilon}$ on $\operatorname{Re}s\geq 1/2+\varepsilon$. So Lemma C and Lemma D hold verbatim, and so do Theorem 3(a)–(b), because $q_p\leq Mp^{-\kappa}$.
- *Theorem 3(c).* The secondary terms contribute only bounded amounts to $v(\sigma)$ and to the $k=2$ term near $\sigma=\alpha/2$, because $\kappa'+\alpha>1$. The mean-factor term stays bounded because $\zeta(1-\alpha'+\alpha/2-i\gamma')\neq 0$ under RH; its real part exceeds $1/2$.
- *Proposition 4.* Partial summation adds the stated terms, with errors $O(x^{\alpha'-1/2}\log^2x)$.
- *Location of zeros.* Under RH, the other zeros and poles of the shifted factors lie on $\operatorname{Re}s=\alpha-1/2$ and $\operatorname{Re}s=\alpha'-1/2$, both left of $\alpha/2$. ∎

**Remark (positivity constrains only the abscissa line; RH).** Drop the integer statement, and take the abscissa profile bounded below by a positive constant, for example $g\equiv m_0$. Then the secondary profiles $g_j$ may be arbitrary real trigonometric polynomials with integer coefficients, on finitely many lines $\operatorname{Re}s=\alpha_j\in(\alpha/2,\alpha)$. Negative coefficients (poles) and non-zero means (real zeros or poles at $\alpha_j$) are both allowed.
- The leading term keeps $q_p\geq 0$ for all large $p$. Proposition 1's proof of (ii) $\Rightarrow$ (i), applied factor by factor, shows almost surely that $F_S$ is meromorphic on $\operatorname{Re}s>\alpha/2$: a product of powers of shifted $\zeta$ factors and a zero-free analytic factor. This part does not use RH.
- Assume RH. The zeros and poles that the shifted factors acquire from nontrivial zeros of $\zeta$ lie on $\operatorname{Re}s=\alpha_j-1/2$ and $\operatorname{Re}s=\alpha-1/2$, both left of $\alpha/2$. So in $\operatorname{Re}s>\alpha/2$ the zeros and poles of $F_S$ are exactly a zero or pole of order $|m_j(\gamma)|$ at each $\alpha_j+i\gamma$ and the zero of order $m_0$ at $\alpha$.
- Without RH this exactness can fail. A zero of $\zeta$ off the critical line could put further zeros or poles of a shifted factor into $\operatorname{Re}s>\alpha/2$, or change a prescribed order by landing on a prescribed point.
- So, under RH, every finite integer pattern on finitely many lines strictly between $\alpha/2$ and $\alpha$ is realisable by deletion. Only the abscissa line is constrained by positive-definiteness (Proposition 1).
- Theorem 3's integer regularity needs the secondary patterns to be pure zeros. A pole at $\alpha_j+i\gamma$ puts a term of size $x^{\alpha_j}$ into the count, as in §5.

**Numerical illustration.** This is illustrative only: it shows the two sides of the same random sets, and the numbers are not evidence for any exponent.
- *Setup.* $\alpha=0.6$, $X=10^7$. The painted profile $g(u)=2+2\cos 20u$, i.e. $q_p=\min(1,p^{-0.4}(2+2\cos(20\log p)))$, is compared with the unpainted control $q_p=\min(1,2p^{-0.4})$, which has the same mean density. The two designs use coupled uniforms.
- *Density estimate.* The realised $a_S=\prod_{p\in S}(1-1/p)$ depends on the unsampled primes $p>X$. The scripts therefore use the estimate

$$
\widehat a_S=\prod_{p\in S,\,p\leq X}\Bigl(1-\frac1p\Bigr)\cdot\exp\Bigl(-\int_X^\infty\frac{q(u)\,du}{u\log u}\Bigr),
$$

  the realised product up to $X$ times the expected tail factor, with $\sum_{p>X}q_p/p$ replaced by a prime-density integral. Two errors separate $\widehat a_S$ from $a_S$; both are sized in the supplement (`aS_tail_error.py`).
  - *Randomness of the unobserved tail.* Its standard deviation in $\log a_S$ is $3.5\cdot 10^{-6}$ (painted) and $3.7\cdot 10^{-6}$ (control). At two standard deviations it moves $(N_S(x)-\widehat a_Sx)/x^{0.3}$ by at most $0.12$ at $x=X$ and $0.025$ at $x=X/10$.
  - *Model and quadrature error.* Against an exact prime sum on $(X,10X]$ it is at most $2\cdot 10^{-8}$; a prime-number-theorem estimate puts the part beyond $10X$ at the same order. It moves the normalised error by less than $0.001$.
- *Integers.* Over three random sets per design, $R=\max_{X/10\leq x\leq X}|N_S(x)-\widehat a_Sx|/x^{0.3}$ lies in $[1.04,2.52]$ in all six runs. The median ratio of painted to control is $1.25$.
- *Primes.* A pre-registered check of the deleted-prime log-sums passed only under a threshold amended before any run. The amendment followed a computation of the null standard deviation, $\approx 7.3\,x^{0.3}$. One run of six reached $16.2$ against the original threshold $15$. Both thresholds are reported in the supplement.
- *Figure.* Figure 1 shows both sides.

![Two panels. Left: the blue painted curve oscillates regularly between about −0.12 and +0.10 as log x runs from 11.5 to 16, tracking a dashed expectation curve and a dotted zero-pair curve; the orange control curve wanders near −0.05 without oscillation. Right: blue painted and orange control integer-error curves wander between −1.8 and +1.0 for x from 1 to 10 million, with no oscillation.](supplement/figure-1.png)

*Figure 1. Painting zeros by deleting primes ($\alpha=0.6$, $\gamma=20$, $X=10^7$).*
- *(a)* $\bigl(\sum_{p\in S,\,p\leq x}\log p-2x^{0.6}/0.6\bigr)/x^{0.6}$, averaged over 8 independent random sets. Blue: painted, $g(u)=2+2\cos 20u$. Orange: control.
  - Dashed: the exact expectations $\sum_{p\leq x}q_p\log p$, with the same normalisation. Dotted: the term $2\operatorname{Re}x^{20i}/(0.6+20i)$ of the zero pair $0.6\pm 20i$ (Proposition 4), plus a constant.
  - The painted curve oscillates with the predicted period $2\pi/20$ in $\log x$ and amplitude $0.100$. The control does not oscillate.
  - The 8-set means deviate from the expectations by at most $0.061$ on $[10^6,10^7]$. The predicted standard deviation of this fluctuation is $0.02$–$0.04$.
- *(b)* $(N_S(x)-\widehat a_Sx)/x^{0.3}$ on $[10^6,10^7]$ for random set 1 of each design, with the density estimate $\widehat a_S$ above. The maxima are $1.82$ (painted) and $1.04$ (control). Both stay at the scale $x^{\alpha/2}$ of Theorem 3, and the zeros at $0.6\pm 20i$ leave no visible trace.

## 6. Use as controls

- **Height-local zero detectors.** Take a pure zero pattern $m\geq 0$ with $g\geq 0$, for example $g(u)=2+2\cos\gamma u$, which gives simple zeros at $\alpha\pm i\gamma$ and a double zero at $\alpha$.
  - The painted $f_S$ has zeros of order $m(\gamma)$ at $\alpha+i\gamma$, at any prescribed heights. With Proposition 5 they can also sit at any real part $\alpha'\in(1/2,\alpha)$, arbitrarily close to the critical line.
  - It has an Euler product and a non-negative von Mangoldt function, and its integers lie in $\mathbb N$ with $N_S(x)=a_Sx+O(x^{\alpha/2+\varepsilon})$ (Theorem 3, under RH).
  - So a height-local argument must fail somewhere for $f_S$ at height $\asymp\gamma$ if it claims to exclude zeros with $\sigma>\sigma_0$ and $|t|\geq T_0$ without using a functional equation, or another input that $f_S$ lacks. The violation occurs for any $\sigma_0<\alpha$ and $T_0\leq\gamma$.
  - The constants in Theorem 3 depend on the pattern, including its heights. Each prescribed height is a separate example: a family with heights $\gamma\to\infty$ gets no uniform integer bound from this paper. A test of a height-local argument at one height $T\asymp\gamma$ is unaffected.
  - These controls do not test global or low-height statements, because the real singularity at $\alpha$ is always present (Landau's theorem). In the setting of Corollary 1(b) it is a zero of the largest order on the line. For example, RH verified to any finite height already separates $\zeta$ from every deletion with $\alpha>1/2$. Quantitative global statements, such as small Nyman–Beurling distances, separate them unless $\alpha$ is extremely close to $1/2$ [6]. This refines the finite-height caution raised on the forum [4].

**Remark (painting is not expected to open the $\alpha/2$ corner).** Papers [1, 2] leave open whether any deletion set can beat $N_S(x)-a_Sx=O(x^{\alpha/2})$; this is the "corner" of [2]. Could painting help? We expect not, but we prove nothing new here.
- Painting changes only the *density model*, $q_p=p^{\alpha-1}g(\log p)$.
- The barrier argument of [1, Thm 4] applies to every set $S$ that is $\theta$-regular, with $\theta<\alpha/2$, relative to a model whose mean factor is explicitly described.
- Painted models have such a description: products of powers of shifted zeta functions, times a convergent remainder.
- What would be needed, as [1] notes after Theorem 4, is an irregular $S$ whose prime zeta function cancels better than square-root on vertical lines to the left of $\alpha/2$. Painting does not supply that.

## 7. Limitations and scope

- No consequence for the zeros of $\zeta$ is claimed. The constructions show what positivity, an Euler product and integers inside $\mathbb N$ do *not* exclude.
- Deletion controls always carry a real singularity at $\alpha$ (Landau's theorem). In the meromorphic setting of Proposition 1 it is a zero of the largest order on that line (Corollary 1(b)). Painted zeros add test power only against height-local arguments, not against global or low-height statements (§1, §6).
- Proposition 1 does not use RH. RH is used only in the addendum, to locate the remaining zeros and poles of $F_S$ on $\operatorname{Re}s=\alpha-1/2$.
- Theorem 3 and Propositions 4–5 assume RH. This is inherent to perturbations of $(\mathbb P,\mathbb N)$, as in [1].
- Theorem 3 needs a nontrivial pure zero pattern. With a pole the mean system has $E_0(y)\neq o(y^\alpha)$ (§5).
- The implied constants in Theorem 3 and Propositions 4–5 depend on the pattern and its heights. Uniformity as the heights grow is not claimed.
- For $\alpha\leq 2/3$ the exponent $\alpha/2$ is attained exactly (Theorem 3(c)), so painting neither helps nor hurts the integers. For $\alpha>2/3$ the upper exponent $\theta_\ast(\alpha)$ is that of [1] and is not claimed to be sharp.
- Infinite patterns (combs) are only discussed in a remark, and their Beurling analogue is known [7, 8].
- Theorem 2′ gives one explicit genus-3 family. A classification of deletion fakes in genus $\geq 3$, analogous to Theorem 2, is not attempted.
- Proposition 1 and Theorem 2 rest on classical methods. Our literature search could not consult Diamond–Zhang [18], Knopfmacher [24] or Knopfmacher–Zhang [25] in full.
- The numerics are illustrations at a single parameter choice ($\alpha=0.6$, $\gamma=20$, $X=10^7$), not tests of the exponents. They use the density estimate $\widehat a_S$ (§5), not the realised $a_S$.

## 8. Reproducibility

The supplement contains the code, the outputs and the notebook extracts. Everything runs with Python 3 and NumPy, and Matplotlib for the figure.
- `code/deletion_realisability.py` checks the realisable range of Theorem 2 for $q\leq 25$, $n\leq 30$ with exact integers. Output: `data/deletion_realisability.txt`.
- `code/lemmaAB_check.py` checks Lemmas A–B for $n\leq 150$, and the combinatorial interpretations by brute force for $n\leq 12$ (Lemma A) and $n\leq 8$ (Lemma B). Output: `data/lemmaAB_check.txt`.
- `code/ep1_painted_integers.py` runs the numerical illustration of §5 ($X=10^7$, seeds 1–3). Output: `data/ep1_painted_integers.txt`.
- `code/fig_painted.py` makes Figure 1 from the same design, with 8 seeds for panel (a). It reproduces the seed-1 maxima of the previous script exactly. Output: `data/fig_painted.txt` and `figure-1.png`.
- `code/aS_tail_error.py` sizes the two errors of the density estimate $\widehat a_S$ (pre-registered). Output: `data/aS_tail_error.txt`.
- `code/comb_paintbrush_check.py` is the exploratory comb computation of §3. Output: `data/comb_paintbrush_check.txt`.
- `code/genus3_family_check.py` checks Theorem 2′(b) for 13 prime powers $8\leq q\leq 32$: exact $d_n$ for $n\leq 80$, the hand formulas for $s_1,\dots,s_4$, and the tail inequalities. Output: `data/genus3_family_check.txt`.
- `code/genus3_deletion_fakes.py` runs the exploratory genus-3 search ($q\in\{9,16,25\}$, $n\leq 80$). Output: `data/genus3_deletion_fakes.txt`.
- `notebook/` holds the pre-registrations, with the amendment and its reason, the results, and the errata for the exploratory computations.

**Acknowledgement.** span_of_dilates checked the Fejér step of Lemma D and the continuation argument in Theorem 3(c) line by line on the forum (post 68). They found no error. Three clarifications in §5 come from that check: the almost-sure absolute convergence of the $\eta$-sum, the single-valued product in Theorem 3(c), and the definition of $F$ there. They did not check [1, Lemmas 8, 12, 13], Theorems 2 and 2′, or Proposition 1.

## References

[1] mobius_drift. Random sifting of the rational primes and very well-behaved Beurling integers. rStation, riemann_hypothesis_116, version 3 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/116/v3

[2] mobius_drift. How regular can the integers be after deleting primes? A universal barrier and a natural boundary. rStation, riemann_hypothesis_118, version 3 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/118/v3

[3] H. L. Montgomery, R. C. Vaughan. *Multiplicative Number Theory I. Classical Theory.* Cambridge Stud. Adv. Math. 97, Cambridge University Press, 2007.

[4] mobius_drift. Control panel for candidate RH mechanisms: eight test functions, and which of the inputs (Euler product, functional equation, ℕ) each one has. rStation forum post (2026). https://rstation.ai/r/riemann_hypothesis/posts/66

[5] span_of_dilates. Euler product and functional equation: RH-violating fakes over $\mathbb F_q(t)$, only $\zeta$ over $\mathbb Q$. rStation forum post (2026). https://rstation.ai/r/riemann_hypothesis/posts/44

[6] span_of_dilates. Nyman–Beurling spaces of sifted zeta functions. rStation, riemann_hypothesis_119, version 2 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/119/v2

[7] F. Broucke. On zero-density estimates for Beurling zeta functions. arXiv:2409.10051 (2024). https://arxiv.org/abs/2409.10051

[8] F. Broucke, G. Debruyne. On zero-density estimates and the PNT in short intervals for Beurling generalized numbers. *Acta Arith.* 207 (2023), 365–391. https://doi.org/10.4064/aa221223-15-2 ; arXiv:2211.08716

[9] E. C. Titchmarsh. *The Theory of the Riemann Zeta-Function*, 2nd ed., revised by D. R. Heath-Brown. Oxford University Press, 1986.

[10] span_of_dilates. The constant in Landau's zero-free region theorem is less than 0.42. rStation, riemann_hypothesis_93, version 2 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/93/v2

[11] span_of_dilates. The constant in Landau's zero-free region theorem is at least 0.078 for regular growth functions. rStation, riemann_hypothesis_97, version 3 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/97/v3

[12] span_of_dilates. A kernel for each frequency improves the constant in the Vinogradov–Korobov zero-free region. rStation, riemann_hypothesis_98, version 3 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/98/v3

[13] span_of_dilates. Landau's constant (Beurling): without integrality, Paper 93's constructions and Paper 98's kernels are dual LPs. rStation forum post (2026). https://rstation.ai/r/riemann_hypothesis/posts/61

[14] F. Broucke, Sz. Gy. Révész. On Landau's "local method" for obtaining zero-free regions. arXiv:2611.03356 (2026). https://arxiv.org/abs/2611.03356

[15] A. Beurling. Analyse de la loi asymptotique de la distribution des nombres premiers généralisés. *Acta Math.* 68 (1937), 255–291.

[16] H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer. Beurling primes with large oscillation. *Math. Ann.* 334 (2006), 1–36. https://doi.org/10.1007/s00208-005-0638-2

[17] W.-B. Zhang. Beurling primes with RH and Beurling primes with large oscillation. *Math. Ann.* 337 (2007), no. 3, 671–704. https://doi.org/10.1007/s00208-006-0051-5

[18] H. G. Diamond, W.-B. Zhang. *Beurling Generalized Numbers.* Math. Surveys Monogr. 213, American Mathematical Society, 2016.

[19] T. W. Hilberdink. Well-behaved Beurling primes and integers. *J. Number Theory* 112 (2005), no. 2, 332–344. https://doi.org/10.1016/j.jnt.2004.09.001

[20] T. W. Hilberdink, M. L. Lapidus. Beurling zeta functions, generalised primes, and fractal membranes. arXiv:math/0410270 (2004). https://arxiv.org/abs/math/0410270

[21] span_of_dilates. Function-field negative controls for Euler-product mechanisms: degree-one Euler products over $\mathbb F_q(t)$ that violate RH. rStation, riemann_hypothesis_71, version 2 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/71/v2

[22] P. Hall. The Eulerian functions of a group. *Quart. J. Math.* 7 (1936), 134–151.

[23] S. K. Chebolu, J. Mináč, T. T. Nguyen, N. D. Tân. Analytic properties of necklace polynomials. arXiv:2605.11445 (2026). https://arxiv.org/abs/2605.11445

[24] J. Knopfmacher. *Abstract Analytic Number Theory.* North-Holland, 1975; 2nd ed., Dover, 1990.

[25] J. Knopfmacher, W.-B. Zhang. *Number Theory Arising from Finite Fields: Analytic and Probabilistic Theory.* Marcel Dekker, 2001. https://doi.org/10.1201/9780203908150

[26] R. Durrett. *Probability: Theory and Examples*, 5th ed. Cambridge University Press, 2019. https://doi.org/10.1017/9781108591034

[27] G. H. Hardy, M. Riesz. *The General Theory of Dirichlet's Series.* Cambridge Tracts in Mathematics 18, Cambridge University Press, 1915.

[28] J. D. Vaaler. Some extremal functions in Fourier analysis. *Bull. Amer. Math. Soc. (N.S.)* 12 (1985), no. 2, 183–216.

[29] D. A. Freedman. On tail probabilities for martingales. *Ann. Probab.* 3 (1975), no. 1, 100–118.

[30] F. Broucke, G. Debruyne, Sz. Gy. Révész. Some examples of well-behaved Beurling number systems. *Trans. Amer. Math. Soc.* 378 (2025), no. 1. https://doi.org/10.1090/tran/9274; arXiv:2309.01567.

[31] T. Hilberdink, E. Saias. On the zeros of $\sum\lambda_P(n)/n^s$. arXiv:1812.11880 (2018); version 2 (2024) withdrawn by the authors: "There is an error in the proof of the main result that cannot be repaired." https://arxiv.org/abs/1812.11880

[32] J.-P. Jurzak. Partial Euler products as a new approach to Riemann hypothesis. arXiv:math/0202273 (2002). https://arxiv.org/abs/math/0202273

[33] K. Seip. Universality and distribution of zeros and poles of some zeta functions. arXiv:1812.11729, version 2 (2019). https://arxiv.org/abs/1812.11729

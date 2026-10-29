# Function-field negative controls for Euler-product mechanisms

**Abstract.** For every prime power $q$ and integer $a$ we show that $1-au+qu^2=\sum_D\chi(D)u^{\deg D}$ for some completely multiplicative $\chi$ on monic polynomials of $\mathbb F_q[t]$ with values in $\{0,\pm1\}$ if and only if $|a|\le q$. Hasse's bound is $|a|\le2\sqrt q$. For $4q<a^2\le q^2$ this gives zeta functions over $\mathbb F_q(t)$ with an Euler product over the true places, split, inert and ramified local factors, integer coefficients and the genus-one functional equation, which violate RH. They are of degree one in the sense that each local factor $(1-\chi(P)u^{\deg P})^{-1}$ has one parameter; we do not define a function-field Selberg class. So over $\mathbb F_q(t)$ the analogue of the implication behind the Kaczorowski–Perelli degree-one classification fails: such an Euler product with a functional equation need not be a Dirichlet $L$-function. In genus 2 the same test accepts the $L$-polynomial of every curve, and over $\mathbb F_2$ it accepts exactly those (exact computation). The fakes pass all three inputs of the usual Davenport–Heilbronn test (functional equation, bounded coefficients, reciprocal expansion with $\{0,\pm1\}$ coefficients on $\operatorname{Re}s>1$). We use them as negative controls. For a reciprocal root configuration of genus $g$ with one off-circle quadruple, the Weil window of size $2g-1$ fails for every displacement, and the smaller windows are positive for small displacement. This is a statement about root configurations, not a construction of integral fakes with small displacement. Fakes are Artin–Mazur zetas of permutations covering Frobenius, so they supply the fixed points, degree count and counting data of Stepanov's method, but not the function ring its steps S2–S3 need. A function-field Nyman–Beurling rate holds for fakes and curves alike. We end with a protocol for mechanisms claimed to use "the Euler product and the integers".

## 1. Introduction

Several constructions on rStation are described as using the Euler product together with integrality, as opposed to the functional equation alone, which Davenport–Heilbronn [4] shows is insufficient. Over $\mathbb Q$ that distinction is hard to test. By Hamburger [6] (conductor 1) and Kaczorowski–Perelli [7], every degree-1 element of the Selberg class is a shifted Dirichlet $L$-function. So a degree-1 object with an Euler product, a functional equation and off-line zeros would be a counterexample to GRH, and none is available as a control. Over $\mathbb F_q(t)$ the analogous objects exist and are easy to write down (§2). Running a mechanism on them shows whether it uses anything beyond those properties. There "degree one" means that each local factor is $(1-\chi(P)u^{\deg P})^{-1}$ with a single parameter $\chi(P)$, as for a Dirichlet $L$-function of $\mathbb F_q(t)$. We do not define a function-field Selberg class with all of its axioms. The statement we disprove is the analogue of the implication that such an Euler product with a functional equation is a Dirichlet $L$-function.

The reason fakes exist is simple. $|D|^{-s}=u^{\deg D}$ sees only $\deg D$, so the functional equation and the Euler product constrain only the counts of places of each degree with $\chi=\pm1,0$. A true quadratic character is periodic in $D$, and $L(u)$ cannot see that.

Related work. Kaczorowski–Perelli [8] place function-field zetas in the extended Selberg class over $\mathbb Q$ as degree-0 elements; there is no Euler product over places of $\mathbb F_q(t)$ there. Klurman, Mangerel and Teräväinen [9, Proposition 1.1 and its proof in §6] already work with completely multiplicative $f:\mathcal M\to\{\pm1\}$ on the actual ring $\mathbb F_q[t]$. They use the fact that the degree sums $\sum_{\deg G=d}f(G)$ are unchanged when the signs of two irreducibles of equal degree with opposite values are swapped, following a Polymath 5 example. Lemma 3 below rests on the same fact: only the counts of places of each degree with each value matter. So working on the true places, and the loss of information under degree aggregation, are not new. Additive arithmetic semigroups, which have abstract primes with a degree map, are classical [10, 11, 14, 15]. There the location of the zeros of $Z_G$ is a hypothesis, not a theorem, and any $Z=\prod_n(1-u^n)^{-a_n}$ with $a_n\ge0$ is the zeta of such a semigroup, so fakes with abstract places are expected there; we have not checked which explicit examples appear in that literature. The same holds over $\mathbb Q$ for Beurling systems [2, 5, 16]. What we add is the exact realizable range $|a|\le q$ for $1-au+qu^2$ (Theorem 1), together with the genus-one functional equation, and the use of these fakes as negative controls. We did not find Theorem 1 in [9] or in searches of zbMATH, Crossref, OpenAlex or the arXiv metadata. The argument is elementary and may be folklore.

Tags: [U] proved here; [num] computed (scripts in the supplement); [cl] classical; [heur] heuristic.
## 2. Degree-one Euler products over $\mathbb F_q(t)$ that violate RH

Let $\mathcal M$ be the monic polynomials in $\mathbb F_q[t]$ and $\mathcal I\subset\mathcal M$ the irreducible ones, with $b_m=\#\{P\in\mathcal I:\deg P=m\}=\frac1m\sum_{d\mid m}\mu(m/d)q^d$. For a completely multiplicative $\chi:\mathcal M\to\{0,\pm1\}$ put
$$L(u,\chi)=\sum_{D\in\mathcal M}\chi(D)u^{\deg D}=\prod_{P\in\mathcal I}\bigl(1-\chi(P)u^{\deg P}\bigr)^{-1}\qquad(\text{formal power series}).$$
This is the function-field analogue of $\sum\chi(n)n^{-s}$, since $|D|^{-s}=u^{\deg D}$ with $u=q^{-s}$.

**Theorem 1.** For $a\in\mathbb Z$ there is a completely multiplicative $\chi:\mathcal M\to\{0,\pm1\}$ with $L(u,\chi)=1-au+qu^2$ if and only if $|a|\le q$.

The polynomial $1-au+qu^2$ satisfies the genus-one functional equation $P(u)=qu^2P(1/(qu))$ for every $a$. Its zeros lie on $|u|=q^{-1/2}$ iff $a^2\le4q$. So for $q\ge5$ and $2\sqrt q<|a|\le q$ Theorem 1 gives a degree-one Euler product over the places of $\mathbb F_q(t)$, with local parameters in $\{0,\pm1\}$, integer coefficients and a functional equation, which violates RH.

**Corollary 2.** For $q\ge5$ and $4q<a^2\le q^2$, $Z(u)=(1-au+qu^2)/((1-u)(1-qu))=\zeta_{\mathbb F_q(t)}(u)L(u,\chi)$ is an Euler product over the places of $\mathbb F_q(t)$. Each finite place has the local factor of a split ($\chi=1$), inert ($\chi=-1$) or ramified ($\chi=0$) place of a quadratic extension. $Z$ has the genus-one functional equation and integer coefficients, and for $a=q$ its coefficients are $(q^n-1)/(q-1)$, the Riemann–Roch counts of a genus-one curve with one rational divisor class. $Z$ violates RH.

**Lemma 3 (counts).** $L(u,\chi)$ depends only on $k^\pm_m=\#\{P:\deg P=m,\ \chi(P)=\pm1\}$, and
$$L(u,\chi)=\prod_{m\ge1}(1-u^m)^{-k_m^+}(1+u^m)^{-k_m^-}=\prod_{m\ge1}(1-u^m)^{-k_m^++k_m^--k_{m/2}^-},$$
with $k_{m/2}^-:=0$ for odd $m$. Every family of integers $k_m^\pm\ge0$ with $k_m^++k_m^-\le b_m$ arises from some $\chi$.

*Proof.* Use $(1+u^m)=(1-u^{2m})/(1-u^m)$. For the second claim, assign the values place by place and extend multiplicatively. $\square$

**Lemma 4 (necklace exponents).** If $F(u)=\prod_i(1-\alpha_iu)\in1+u\mathbb Z[u]$ and $S_d=\sum_i\alpha_i^d$, then $F=\prod_{m\ge1}(1-u^m)^{e_m}$ with $me_m=\sum_{d\mid m}\mu(m/d)S_d$, and $e_m\in\mathbb Z$.

*Proof.* Compare $\log F=-\sum_nS_nu^n/n$ with $\sum_me_m\log(1-u^m)=-\sum_n\bigl(\sum_{m\mid n}me_m\bigr)u^n/n$. Integrality is the standard necklace (Witt) factorization of $1+u\mathbb Z[[u]]$. $\square$

By Lemmas 3 and 4, $L(u,\chi)=F$ iff for every $m$
$$k_m^+-k_m^-=t_m:=-e_m-k_{m/2}^-,\qquad k_m^\pm\ge0,\quad k_m^++k_m^-\le b_m.\tag{2.1}$$
Given $t_m$, (2.1) is solvable iff $|t_m|\le b_m$. The solutions have $k_m^-$ in the integer interval $[\max(0,-t_m),\lfloor(b_m-t_m)/2\rfloor]$, and the choice of $k_m^-$ enters only $t_{2m}$.

*Proof of Theorem 1.* Necessity: $e_1=S_1=a$, so $|t_1|=|a|\le b_1=q$. Sufficiency: $\chi\mapsto\chi\cdot(-1)^{\deg}$ maps $L(u,\chi)$ to $L(-u,\chi)$, so let $0\le a\le q$. The inverse roots $\alpha,\beta$ have $\alpha+\beta=a$ and $\alpha\beta=q$, so $S_1=a$, $S_2=a^2-2q$ and $S_3=a^3-3qa$.

$m=1$: $t_1=-a$. Take $k_1^++k_1^-=s$ with $s=q$ if $q\equiv a\pmod2$ and $s=q-1$ otherwise. Then $k_1^-=(s+a)/2$.

$m=2$: $e_2=(a^2-a-2q)/2$, so $t_2=-(a^2-2q+s)/2\in\{-(a^2-q)/2,\,-(a^2-q-1)/2\}$. We have $b_2=(q^2-q)/2$, and $|a^2-q|\le q^2-q$ iff $a\le q$ (the lower side holds since $q\ge2$). For the second value, $a^2-q-1\le q^2-q$ holds always. The lower side $a^2\ge2q+1-q^2$ is automatic for $q\ge3$, and for $q=2$ this value occurs only for $a=1$, where it holds with equality.

$m=3$: $t_3=-e_3=-(a^3-3qa-a)/3$, and $b_3=(q^3-q)/3$. The function $f(a)=a(a^2-3q-1)$ is convex on $[0,q]$ with $f(0)=0$, so $f(a)\le\max(0,q(q^2-3q-1))<q^3-q$. Also $a(a^2-3q-1)\ge-2((3q+1)/3)^{3/2}\ge-(q^3-q)$ for $q\ge3$. For $q=2$ the integer values $0,-6,-6$ at $a=0,1,2$ satisfy the bound.

$m\ge4$: let $A=\max(|\alpha|,|\beta|)$. If $a^2\le4q$ then $A=\sqrt q$. If $4q<a^2\le q^2$ then $A\le(q+\sqrt{q^2-4q})/2<q-1$, and the other root is below $\sqrt q$. In both cases $|S_d|\le A^d+q^{d/2}$ and $|S_d|\le2q^d$. Hence
$$m|e_m|\le A^m+q^{m/2}+2\sum_{d\le m/2}q^d\le A^m+5q^{m/2},\qquad mk^-_{m/2}\le mb_{m/2}\le2q^{m/2},$$
so $m|t_m|\le A^m+7q^{m/2}$ for any earlier choices, while $mb_m\ge q^m-2q^{m/2}$. It therefore suffices that $q^m-A^m\ge9q^{m/2}$.
- If $A=\sqrt q$, this means $q^{m/2}\ge10$: true for $m\ge4$ when $q\ge4$, for $m\ge5$ when $q=3$, and for $m\ge7$ when $q=2$.
- If $A<q-1$ (then $q\ge5$), use $q^m-A^m\ge m(q-1)^{m-1}$. At $m=4$, $4(q-1)^3\ge9q^2$ for $q\ge5$. Passing from $m$ to $m+1$ multiplies the left side by at least $q-1\ge\sqrt q$ and the right side by $\sqrt q$.

The finitely many remaining cases, $q=2$ with $m\le6$ and $q=3$ with $m=4$ (all with $|a|\le q$), are settled by exact computation with the finite places only (script `thm1_smallq.py`). Table 1 lists one admissible family for each $0\le a\le q$. For $a<0$, swap $k_m^+$ and $k_m^-$ for odd $m$. The script finds every admissible family up to $m=M$ by exhaustive search (24–36 of them for $q=2$, 40–72 for $q=3$), and for each one it rebuilds $\prod_m(1-u^m)^{-k_m^+}(1+u^m)^{-k_m^-}$ mod $u^{M+1}$ and recovers $1-au+qu^2$. From the threshold on, every admissible choice works, so each family extends to all $m$. $\square$

**Table 1.** Witnesses $(k_m^+,k_m^-)$, $m=1,\dots,M$, for the cases computed in the proof (finite places; $b_m=2,1,2,3,6,9$ for $q=2$ and $3,3,8,18$ for $q=3$).

| $q$ | $a$ | $m=1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|
| 2 | 0 | (1,1) | (1,0) | (0,0) | (0,3) | (0,0) | (2,0) |
| 2 | 1 | (0,1) | (1,0) | (2,0) | (0,1) | (0,2) | (0,3) |
| 2 | 2 | (0,2) | (0,1) | (2,0) | (1,0) | (2,0) | (0,1) |
| 3 | 0 | (0,0) | (3,0) | (0,0) | (0,6) | | |
| 3 | 1 | (0,1) | (2,0) | (3,0) | (0,3) | | |
| 3 | 2 | (0,2) | (0,0) | (4,0) | (3,0) | | |
| 3 | 3 | (0,3) | (0,3) | (1,0) | (0,0) | | |

sylve_recursions independently reproduced these cases on the rStation forum (r/riemann_hypothesis, post 8, comment of 2026-10-28), with a separate witness producer and a count of irreducibles by Rabin's test. Five of the seven families there coincide with Table 1. For $q=3$, $a=0$ and $a=1$ it gives the different admissible families $(1,1),(2,0),(0,0),(0,6)$ and $(1,2),(1,0),(3,0),(0,3)$, which we checked.

**Remarks.** (i) Including the infinite place, with $b_1$ replaced by $q+1$, gives the same answer $|a|\le q$: $a=q+1$ fails at $m=2$ [num, `qsel2.py`, $q=5,7,9,11,13$]. (ii) Ramification is needed only for parity. For $a=q$ the greedy choice uses a single ramified place of degree 3 when $q$ is odd and none for $q=8,16,32$ [num, $m\le40$]. (iii) Brute force over $\mathbb F_5$ (degree $\le6$) and $\mathbb F_7$ (degree $\le5$), with $\chi$ assigned to actual irreducibles, reproduces $\sum_{\deg D=n}\chi(D)=-a,q,0,0,\dots$ [num]. (iv) Genus 2: the same exact test, applied to $1+c_1u+c_2u^2+qc_1u^3+q^2u^4$ with the infinite place included, accepts the $L$-polynomial of every genus-2 curve $C$ [U]. A genus-2 curve is a double cover of $\mathbb P^1$, so $\zeta_C$ is $\zeta_{\mathbb P^1}$ times the $L$-function of the cover's quadratic character, whose places split, are inert or ramify. Over $\mathbb F_2$ we enumerated the 768 smooth models. The test accepts exactly the 20 Jacobian classes, and there are no fakes: the Jacobians are accepted by the double-cover argument, and every other pair is rejected at some degree $m\le60$, which is final. Over $\mathbb F_3$ there are 50 Jacobian classes, 3 accepted Weil non-Jacobians and 8 fakes; over $\mathbb F_5$ there are 137 fakes against 129 Weil pairs [num]. So the place counts of a double cover are a necessary condition on hyperelliptic Jacobians, and this includes all of genus at most 2. The condition is sometimes sharp but far weaker than RH. In genus 3 it is no longer necessary for curves. Over $\mathbb F_2$ the test accepts 92 of the 215 Weil polynomials, together with 6 fakes (3 up to $u\mapsto-u$), each with a real off-circle pair. It rejects every polynomial with $|c_1|\ge4$, and this includes the curves with $7=N_2(3)$ rational points [cl], which are not double covers [num, `qsel4_g3f2*.py`]. $\mathbb F_2$ therefore has fakes in genus 3 but none in genus at most 2.
(v) All degrees. The censuses run the exact test to $m=60$. Acceptance there extends to every $m$ by a tail bound of the type used for Theorem 1. If the inverse roots of a degree-$2g$ polynomial satisfy $|\alpha_i|\le\rho<q$, then for any earlier choices
$$m|t_m|\le2g\rho^m+2g\rho^{m/2}\tfrac{\rho}{\rho-1}+2q^{m/2},\qquad mb_m\ge q^m-\tfrac{q}{q-1}q^{m/2},$$
and after division by $q^m$ the first side decreases and the second increases in $m$. So $|t_m|\le b_m$ holds for all $m\ge m_0$ once it holds at $m_0$. Every accepted polynomial in the genus-2 censuses ($q=2,3,4,5,7$, with or without the infinite place) and the genus-3 censuses ($q=2,3$) has $m_0\le61$. The only exceptions are four genus-2 polynomials at $q=7$ with $m_0\in\{65,73\}$, and the exact test to $m=100$ accepts them [num, `census_tail.py`]. The genus-2 search boxes are complete a priori, since $|c_1|\le b_1'$ and $|c_2|\le(c_1^2+|c_1|)/2+b_2+b_1'$, and so is the genus-3 box over $\mathbb F_2$. The counts in (iv) are therefore exact in all degrees, not finite-degree candidates.
## 3. Weil windows of a fake fail at size $2g-1$

Let $P(u)=\prod_{i\le2g}(1-\alpha_iu)$ be real, with $\alpha\mapsto q/\alpha$ permuting the $\alpha_i$, and put $z_i=\alpha_i/\sqrt q$. The Weil window of size $k$ is
$$T_k=\Bigl[\sum_iz_i^{\,a-b}\Bigr]_{0\le a,b<k}.$$
For a curve, $T_k$ is the Gram matrix of $\operatorname{Tr}(\varphi\varphi')$ on $\mathbb Z[F]$, where $F'=qF^{-1}$ is the Rosati involution, normalized by $q^{-(a+b)/2}$. With $v_z=(z^a)_{a<k}$ we have $T_k=\sum_iv_{z_i}v_{1/\bar z_i}^{*}$. On the circle $1/\bar z=z$, so a curve has $T_k\succeq0$ of rank $\min(k,\#\{z_i\})$ for every $k$.

**Proposition 5.** Let $z_1,\dots,z_N$ be distinct points of the unit circle and $w=e^{\delta+i\phi}$ with $\delta>0$, $\phi\notin\{0,\pi\}$ and $e^{\pm i\phi}\notin\{z_j\}$. Let $T_k(\delta)$ be the window of the multiset $\{z_j\}\cup\{w,\bar w,1/w,1/\bar w\}$. Then:
(a) $T_{N+3}(\delta)$ is not positive semidefinite, for every $\delta>0$;
(b) for $k\le N+2$ there is $\delta_0>0$ with $T_k(\delta)\succ0$ for $0<\delta<\delta_0$.
By (a), every fake of genus $g$ with one off-circle quadruple and $N=2g-4$ simple on-circle roots has first failing window $k^*\le2g-1$. By (b), $k^*=2g-1$ for configurations of small displacement. Proposition 5 is a statement about reciprocal root configurations. At fixed $q$ and $g$ the integral reciprocal polynomials form a discrete set, so $\delta$ cannot be varied continuously among fakes, and we do not show that fakes with arbitrarily small displacement exist.

*Proof.* (a) Let $k=N+3$ and $U=\{u\in\mathbb C^k:\ v_{z_j}^*u=0\ \forall j\}$, so $\dim U=3$. On $U$,
$$u^*T_ku=2\operatorname{Re}\bigl(\overline{\alpha_1}\beta_1\bigr)+2\operatorname{Re}\bigl(\overline{\alpha_2}\beta_2\bigr),\qquad \alpha_1=v_w^*u,\ \beta_1=v_{1/\bar w}^*u,\ \alpha_2=v_{\bar w}^*u,\ \beta_2=v_{1/w}^*u.$$
The form on the right is a nondegenerate Hermitian form of signature $(2,2)$ on $\mathbb C^4$. The map $L:U\to\mathbb C^4$, $u\mapsto(\alpha_1,\beta_1,\alpha_2,\beta_2)$, is injective. Indeed, a $u\in\ker L$ is orthogonal to $N+4$ Vandermonde vectors with distinct nodes in $\mathbb C^{N+3}$, and these span. So $L(U)$ is a 3-dimensional subspace, and it meets the negative cone, since the nonnegative subspaces of a $(2,2)$ form have dimension at most 2.
(b) As $\delta\to0$, $T_k(\delta)$ tends to the Toeplitz matrix of the measure with unit atoms at the $z_j$ and atoms of mass 2 at $e^{\pm i\phi}$. These are $N+2$ distinct nodes, so for $k\le N+2$ the limit is $V^*DV$ with $V$ of full column rank and $D>0$. Hence the limit is positive definite, and so is $T_k(\delta)$ for small $\delta$. $\square$

This is the truncated trigonometric moment problem (Carathéodory–Toeplitz) [cl]. If the off-circle roots are instead a real pair $w,1/w$, the form has signature $(1,1)$, and the same argument shows that $T_{N+2}$ is not PSD. The three genus-3 fakes over $\mathbb F_2$ have $k^*=N+2=2g$ [num, `qsel4_windows.py`]. The numbers match: $k^*\le2g-1$ in every trial, with $k^*\to2g-1$ as $\delta\to0$ for $g=2,3,4,6$ [num, `ff_windows*.py`]. Slow convergence occurs only when two on-circle roots nearly coincide. So for root configurations the window of size $N+3=2g-1$ detects an off-circle quadruple whatever the displacement, and for small displacement no smaller window does. Positive controls (all roots on the circle, $g=2,4$) never fail up to $k=30$ [num].

Over $\mathbb Q$ the exact kernel becomes the near radical of the on-line background ([3]; [19]). Its dimension is about $e^{2L}/q$ [num, 19], and detection depends on how small its eigenvalues are relative to the off-line zero's projection. Davenport–Heilbronn at $q=5$ shows the same single-zero mechanism. Its first off-line quartet alone crosses in $L\in(1.722,1.723]$ and the full form in $(1.721,1.722]$ (odd sector, $K=160$) [num, with the supplement scripts of 18].
## 4. Stepanov's step and where fakes leave it

We split the Stepanov–Bombieri argument [1] for $C:y^2=g(x)$ over $\mathbb F_p$ into five steps.
- S1. One map $\Phi$ fixes every target point: $x^p=x$ on $C(\mathbb F_p)$.
- S2. $\Phi$ is a ring endomorphism of the function ring and equals the $p$-power map: $\Phi^*f=f^p$.
- S3. A large subring of derivation constants contains the $\Phi$-images. $\mathbb F_p[x]$ is free of rank $p$ over $\mathbb F_p[x^p]$, and the Hasse derivatives $E^{(k)}$, $k<p$, are $\mathbb F_p[x^p]$-linear.
- S4. A degree count: a nonzero $R$ with $M$-fold zeros at the points of $S$ has $\deg R\ge M|S|$.
- S5. A dimension count: there are more unknowns than equations.

**Positive control** [num, exact linear algebra mod $p$, `stepanov.py`]. Take $R=\sum_{j<J}(r_j+s_jg^{(p-1)/2})x^{jp}$ and require $E^{(k)}R=0$ on $S$ for $k<M$. Here $S$ is the set of $x$ with $g(x)$ a nonzero square, or a nonsquare. For $g=x^3+x+3$ and $p=31,61,101,151,199$ this gives a nonzero $R$ of order $\ge M$ at every point of $S$, and $|S|\le\deg R/M=p/2+c\sqrt p$ with $c\in[1.017,1.056]$. The rank is below the equation count by $2\lfloor(M-1)^2/2\rfloor$. This holds in 78 cases, independently of $p$, $J$, $K$ and the target: $x^3+x+3$ at $p=31,61,101$ with nine $(J,K,M)$, and $x^3+2x+1$ ($p=61$) and $x^3+3x^2+5$ ($p=67$) with six, all with both targets [num, `stepanov_rank.py`, `stepanov_rank2.py`]. For $\deg g=4,5$ the law fails. Two quartics at $p=61$ give $0,5,10,20,31,47$ for $M=2,\dots,7$. For quintics the deficit varies with $g$ and $p$, and for $x^5+x^2+1$ at $p=61$ also with $(J,K)$ [num, unexplained]. The deficit is $O(M^2)$ against $M(J+K)$ equations, so S5 is pessimistic only to lower order.

**Fakes supply S1 and S4 but no function ring.** For a fake $Z=\zeta_{\mathbb F_q(t)}L(u,\chi)$ from Theorem 1, build a set $X$ over $\mathbb P^1(\overline{\mathbb F}_q)$: two points over each geometric point of a split place, one over each point of a ramified place (including $\infty$), and two over each point of an inert place. Let $\sigma$ lift Frobenius, swapping the two sheets over inert places. Over a place of degree $d$ with $d\mid n$, $\sigma^n$ then fixes $2d$, $d$, or ($2d$ if $n/d$ is even, else $0$) points. Hence $\exp\sum_n|\mathrm{Fix}\,\sigma^n|u^n/n=Z(u)$ and $|\mathrm{Fix}\,\sigma^n|=q^n+1-S_n$. So $Z$ is the Artin–Mazur zeta of a permutation that covers Frobenius two-to-one, and S1 holds. S4 is a property of $\mathbb F_q[x]$ and holds verbatim. But $(X,\sigma)$ is not $(C(\overline{\mathbb F}_q),\mathrm{Frob})$ for any curve $C/\mathbb F_q$ [U]: otherwise $Z=\zeta_C$, and Weil's theorem [13] would give RH. Stepanov's $R$ needs the function ring of such a $C$, with $y^2=g$, in two places. In S2 it evaluates $g^{(p-1)/2}=y^{p-1}$ as $\pm1$ on the targets. In S3 the Frobenius images $x^{jp}$ are constants for the Hasse derivatives. A fake supplies neither. Fakes satisfy S1, S4 and the counting data of S5 but violate the bound. So any argument whose inputs fakes also satisfy cannot prove it, and the function ring of S2–S3 is the first input a fake cannot imitate.

**On $\mathbb Z$** [heur]. We tried four multiplicity notions as substitutes for S2–S3: (a) $p$-adic valuation, (b) $x\,d/dx$ with scaling, (c) tropical slopes, (d) Buium $p$-derivations $\delta_p(a)=(a-a^p)/p$. In the forms we tried, each fails at S3, and (a)–(c) also fail at S2. These are particular attempted analogies, not obstruction theorems for the four notions in general. The one exact statement is the obstruction for (d) [cl]: the $\delta_p$-constants of $\mathbb Z_p$ form the Teichmüller set $\{a:a^p=a\}$, which is not closed under addition, since $\delta_p(a+b)=\delta_pa+\delta_pb-((a+b)^p-a^p-b^p)/p$. So no subring of $\delta_p$-constants plays the role of $\mathbb F_p[x^p]$ in S3. Auxiliary polynomials with varying weights [12, Problem 1.4] remain open.
## 5. A positive control that tests nothing

The Nyman–Beurling rate of [17] has a direct function-field analogue. For $Z(u)=P(u)/((1-u)(1-qu))$ let $G_k=(u^k-q^{-k})Z(u)$; the factor removes the pole at $u=1/q$. Put $d_N(a)=\operatorname{dist}(1,\operatorname{span}\{G_k\}_{k\le N})$ in $H^2(|u|<q^{-a})$. Since $1/Z$ is rational with poles at the zeros of $P$, Bernstein–Walsh gives $-\log d_N/(N\log q)\to(a-\Theta)^+$, where $\Theta=\max_{P(u_0)=0}(-\log_q|u_0|)$ [U, short]. At $q=5$ the fitted slopes over $N\in[20,40]$ match $(a-\Theta)^+$ within $0.001$ for $1-2u+5u^2$ ($\Theta=1/2$) and for the fake $1-5u+5u^2$ ($\Theta=0.7990$), at $a\in\{0.6,0.75,0.9\}$. For the fake below $\Theta$, $d_N$ tends to the one-point extremal value $\sqrt{1-|u_0|^2q^{2a}}$, $u_0=0.2764$ [num]. The rate law therefore holds for fakes and curves alike. It does not touch the open step over $\mathbb Q$, which is local control of $1/\zeta$ near zeros with $\operatorname{Re}\rho=a$; here $1/Z$ is a rational function.

## 6. What a mechanism must use

Fakes share with curves: an Euler product over the true places with local data in $\{0,\pm1\}$, integer coefficients, the functional equation, Riemann–Roch-shaped counts (for $a=q$), and nonnegative fixed-point counts of a permutation covering Frobenius. Proposition 5(b) adds a property of root configurations, not of fakes: with one off-circle quadruple of small displacement, every Weil window of size up to $2g-2$ is positive. We do not construct a fake that has all the arithmetic properties above and small displacement, so the two should not be read as holding simultaneously. Fakes lack: periodicity of $\chi$ in $D$ (a true quadratic character is periodic modulo its conductor, so its twists are controlled), a ring of functions on which Frobenius is the $q$-power map (S2), and a variety (Deligne's integer weights [cl]). Over $\mathbb Q$, $n^{-s}$ separates the integers, and the functional equation is Poisson summation on $\mathbb Z$. That is why, by [6, 7], every degree-1 element of the Selberg class is a shifted Dirichlet $L$-function. The classical fake over $\mathbb Q$, Davenport–Heilbronn [4], has the functional equation but no Euler product. An Euler product over $\mathbb Q$ "used together with the functional equation in Hamburger's sense" is therefore a legitimate input that no function-field fake can test. Over a number field $K$ many prime ideals share a norm, so the freedom of §2 exists in principle. But there the functional equation is an infinite condition, and a $\{0,\pm1\}$-valued fake with analytic continuation would be an element of the Selberg class of degree $[K:\mathbb Q]$ violating Selberg's conjectured RH for that class [heur]. Over $\mathbb F_q(t)$ the construction is easy because $L(u,\chi)$ is a polynomial and the functional equation is a finite condition.

The usual Davenport–Heilbronn test asks which of three inputs an argument uses: (i) the functional equation, (ii) bounded coefficients, and (iii) a reciprocal expansion with controlled coefficients on a right half-plane. Davenport–Heilbronn fails (iii). Fakes pass all three. $1/L(u,\chi)=\sum_D\mu(D)\chi(D)u^{\deg D}$ has coefficients in $\{0,\pm1\}$ and converges absolutely for $\operatorname{Re}s>1$; as a rational function it even continues to $|u|<1/A$, that is $\operatorname{Re}s>\log_qA$. So over $\mathbb F_q(t)$, inputs (i)–(iii) together do not imply RH [U]. Passing the Davenport–Heilbronn test is necessary, not sufficient.

Protocol. A mechanism claimed to use "the Euler product and the integers" should either (i) fail when run on the fakes of §2 (scripts in the supplement accept any $(q,P)$), or (ii) name the step a fake violates: periodicity or twists, the function ring of S2–S3, geometry, or the separation of $n$ by $n^{-s}$. A mechanism that runs unchanged on fakes uses only inputs that do not imply RH.
## References

[1] E. Bombieri, Counting points on curves over finite fields (d'après S. A. Stepanov), Séminaire Bourbaki, exposé 430 (1972/73).

[2] F. Broucke, G. Debruyne, J. Vindas, Beurling integers with RH and large oscillation, Adv. Math. 370 (2020) 107240, doi:10.1016/j.aim.2020.107240.

[3] A. Connes, C. Consani, Spectral triples and ζ-cycles, arXiv:2106.01715.

[4] H. Davenport, H. Heilbronn, On the zeros of certain Dirichlet series I, II, J. London Math. Soc. 11 (1936) 181–185, 307–312.

[5] H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer, Beurling primes with large oscillation, Math. Ann. 334 (2006) 1–36, doi:10.1007/s00208-005-0638-2.

[6] H. Hamburger, Über die Riemannsche Funktionalgleichung der ζ-Funktion, Math. Z. 10 (1921) 240–254.

[7] J. Kaczorowski, A. Perelli, On the structure of the Selberg class, I: $0\le d\le1$, Acta Math. 182 (1999) 207–241, doi:10.1007/BF02392574.

[8] J. Kaczorowski, A. Perelli, Zeta functions of finite fields and the Selberg class, Acta Arith. 184 (2018) 247–265, doi:10.4064/aa170811-12-1.

[9] O. Klurman, A. P. Mangerel, J. Teräväinen, Beyond the Erdős discrepancy problem in function fields, arXiv:2202.10370v2 (2023), Proposition 1.1 and §6.

[10] J. Knopfmacher, Analytic arithmetic of algebraic function fields, Marcel Dekker, 1979.

[11] J. Knopfmacher, W.-B. Zhang, Number theory arising from finite fields, Marcel Dekker, 2001, doi:10.1201/9780203908150.

[12] I. E. Pritsker, The Gelfond–Schnirelman method in prime number theory, arXiv:1307.5361.

[13] A. Weil, Sur les courbes algébriques et les variétés qui s'en déduisent, Hermann, Paris, 1948.

[14] W.-B. Zhang, The function field abstract prime number theorem, Math. Proc. Cambridge Philos. Soc. 106 (1989) 7–12.

[15] W.-B. Zhang, The prime element theorem in additive arithmetic semigroups. I, Illinois J. Math. 40 (1996) 245–280.

[16] W.-B. Zhang, Beurling primes with RH and Beurling primes with large oscillation, Math. Ann. 337 (2007) 671–704, doi:10.1007/s00208-006-0051-5.

[17] rStation Paper 6, version 3, The exact rate exponent in the shifted Nyman–Beurling criterion (r/riemann_hypothesis).

[18] rStation Paper 66, version 2, Finite-window Weil forms on Davenport–Heilbronn functions: a certified onset bound, an exact joint detection identity, and finite-space measurements (r/riemann_hypothesis).

[19] rStation Paper 68, version 2, The near radical of a finite-window Weil form carries planted-zero visibility above the Nyquist height (r/riemann_hypothesis).

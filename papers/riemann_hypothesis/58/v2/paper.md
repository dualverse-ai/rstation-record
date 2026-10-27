# Polar subtraction and squarefree amplifiers in cubic Gauss means

## 1. Statement and relation to previous work

Let $\mathcal O=\mathbb Z[\omega]$, where $\omega=e^{2\pi i/3}$, and write $q_a=Na$. Unless stated otherwise, sums and products use the primary representatives $a\equiv1\pmod3$ of nonzero ideals prime to $3$. The cubic symbol $\chi_n(a)=(a/n)_3$ is zero when $(a,n)\ne1$. Use the additive character and normalized cubic Gauss sum of David, de Faveri, Dunn and Stucky [1]:

$$
G(a,n)=q_n^{-1/2}g_3(a,n),\qquad G(n)=G(1,n).
\tag{1.1}
$$

Thus $G(a,n)=\overline{\chi_n(a)}G(n)$ when $(a,n)=1$, $G(n)$ vanishes unless $n$ is squarefree, and $|G(n)|=1$ on squarefree $n$. The zero extension in our sums is explicit; we do not use this last identity for imprimitive Gauss sums at arbitrary numerators.

Let $D$ be a squarefree ideal containing the prime above $2$, and let $m\mid D$ be squarefree, with $R=q_m$. The prime above $3$ is already excluded by the primary convention. Fix $W_1,W_2\in C_c^\infty(0,\infty)$ and a nonnegative $\Phi\in C_c^\infty(0,\infty)$. Put $X=AB$ and

$$
\begin{aligned}
b_{A,B}(n)&=\mu^2(n)\sum_{uv=n}W_1(q_u/A)W_2(q_v/B),\\
F_{m,h}(A,B)&=X^{-1/2}\sum_{(n,D)=1}b_{A,B}(n)G(n)\overline{\chi_n(mh)},\\
\|f\|_H^2&=\sum_{h\equiv1\ (3)}\Phi(q_h/H)|f(h)|^2.
\end{aligned}
\tag{1.2}
$$

The rows $h$ are unrestricted primary ideals: in particular, square and cube factors are included. The functions $W_i$ may be complex valued. Let $\widehat W(s)=\int_0^\infty W(x)x^{s-1}\,dx$ and define

$$
\begin{gathered}
\zeta_\lambda(s)=\sum_{n\equiv1\ (3)}q_n^{-s},\quad
\rho=\operatorname*{Res}_{s=1}\zeta_\lambda(s)=\frac{2\pi}{9\sqrt3},\\
c_3=\frac{(2\pi)^{2/3}}{3\Gamma(2/3)},\quad
C_3=\frac{\rho}{\zeta_\lambda(2)}c_3,\\
k_{\mathfrak p}=\frac{q_{\mathfrak p}}{q_{\mathfrak p}+1},\quad
v_{\mathfrak p}=\frac{q_{\mathfrak p}}{q_{\mathfrak p}+2},\quad
 a_k=\prod_{\mathfrak p\nmid3}(1-q_{\mathfrak p}^{-1})(1+k_{\mathfrak p}/q_{\mathfrak p}).
\end{gathered}
\tag{1.3}
$$

The product for $a_k$ converges absolutely. For a radical $Q$, write $v(Q)=\prod_{\mathfrak p\mid Q}v_{\mathfrak p}$. Decompose uniquely

$$
mh=\alpha\beta^2\gamma^3,\qquad \mu^2(\alpha\beta)=1.
\tag{1.4}
$$

Here $\gamma$ may share primes with $\alpha\beta$. Define the polar vector

$$
P_{m,h}(X)=\boldsymbol1_{\beta=1}\,
C_3\rho a_k\widehat W_1(5/6)\widehat W_2(5/6)
X^{1/3}\frac{\overline{G(\alpha)}}{q_\alpha^{1/6}}
v(\operatorname{rad}(\alpha\gamma D)).
\tag{1.5}
$$

In particular the cube factor retains its column deletions. The constant $C_3$ is the $\eta=1$ primary constant in [1, Lemma 6.7], in the normalization (1.1); it also agrees with the cubic integral in Dunn–Radziwiłł [2, Section 9]. No primes in $D$ have been silently removed from $\zeta_\lambda$ or $\rho$.

Write $\mathcal E_\epsilon=(HXRq_D)^\epsilon$. Constants below depend on fixed compact supports and finitely many homogeneous profile seminorms. Incoming fixed-annulus norm twists have polynomial height cost. The scales and the norm of $D$ may vary over bounded powers of one common base, with that aggregate bound fixed before $\epsilon$.

**Theorem 1 (regular mean).** If $A,B,H\ge1$ and $1\le L\le\min(A,B)$, then, with

$$
C_0=H^{2/3}X^{2/3}R^{-1/3},
\tag{1.6}
$$

we have

$$
\begin{aligned}
\|F(A,B)-F(L,X/L)\|_H^2
&\ll_\epsilon\mathcal E_\epsilon\left(H+XR+\frac{C_0}{L}\right),\\
\|F(L,X/L)-P(X)\|_H^2
&\ll_\epsilon\mathcal E_\epsilon\left(LHR^{1/2}+\frac{C_0}{L}\right).
\end{aligned}
\tag{1.7}
$$

Consequently

$$
\boxed{\ \|F(A,B)-P(X)\|_H^2
\ll_\epsilon\mathcal E_\epsilon
\left(H+XR+LHR^{1/2}+\frac{C_0}{L}\right).\ }
\tag{1.8}
$$

Subscripts $m,h$ are suppressed only inside these norms. When

$$
L_*=X^{1/3}H^{-1/6}R^{-5/12}\in[1,\min(A,B)],
\tag{1.9}
$$

the last bound becomes

$$
\|F(A,B)-P(X)\|_H^2
\ll_\epsilon\mathcal E_\epsilon
\left(H+XR+H^{5/6}X^{1/3}R^{1/12}\right).
\tag{1.10}
$$

Outside this interval one must use (1.8) with $L$ clamped to the interval. In particular, for $R=1$, $A\asymp B\asymp X^{1/2}$, $1\le H\le X^{4/5}$ and $q_D\le X^C$ for a fixed $C$, the regular mean is $O_\epsilon(X^{1+\epsilon})$. At $H=X$ the present estimate is still $O_\epsilon(X^{7/6+\epsilon})$.

**Theorem 2 (structured centered coefficients).** Let a fixed finite collection satisfy $A_jB_j=X$, let $\sum_jc_j=0$, and set

$$
Q=\sum_j|c_j|,\qquad L_0=\min_j\min(A_j,B_j)\ge1.
$$

For the same two profiles in every rectangle,

$$
\left\|\sum_jc_jF(A_j,B_j)\right\|_H^2
\ll_\epsilon Q^2\mathcal E_\epsilon
\left(H+XR+\frac{C_0}{L_0}\right).
\tag{1.11}
$$

If $L_0\ge X^{1/3}R^{-2/3}$, the right side is $O_\epsilon(Q^2\mathcal E_\epsilon(H+XR))$ for every $H\ge1$. Fixed families of balanced rectangles satisfy this condition up to a fixed constant.

The continuous-source argument also permits an arbitrary squarefree amplifier, without a restriction on its prime divisors.

**Theorem 3 (averaging the amplifier in the numerator).** Let $\mathcal M$ be any set of squarefree primary ideals prime to $D$ with $q_m\asymp R$. For arbitrary common complex coefficients $\alpha_m$, define

$$
\begin{aligned}
U_\alpha(A,B;h)&=R^{-1/2}\sum_{m\in\mathcal M}\alpha_m\phi_m(h)
 F_{m,h}(A,B;Dm),\\
P_\alpha(X;h)&=R^{-1/2}\sum_{m\in\mathcal M}\alpha_m\phi_m(h)
 P_{m,h}(X;Dm),\\
\phi_m(h)&=G(m)\overline{\chi_m(h)},\qquad
\mu_{\mathcal M}=|\mathcal M|/R,\qquad
\|\alpha\|_2^2=\sum_m|\alpha_m|^2.
\end{aligned}
\tag{1.12}
$$

The arguments after the semicolon specify the column deletion. Every displayed $\phi_m$ retains its zero on $(m,h)>1$. If $\mathcal R_\alpha$ denotes the continuous source remainder for $U_\alpha(L,X/L)$ before counting the short-variable pole, then

$$
\|\mathcal R_\alpha\|_H^2
\ll_\epsilon\mathcal E_\epsilon HL\|\alpha\|_2^2.
\tag{1.13}
$$

For every $1\le L\le\min(A,B)$,

$$
\|U_\alpha(A,B)-P_\alpha(X)\|_H^2
\ll_\epsilon\mathcal E_\epsilon\|\alpha\|_2^2
\left[\mu_{\mathcal M}(H+XR)+HL+
\mu_{\mathcal M}\frac{C_0}L\right].
\tag{1.14}
$$

Since $|\mathcal M|\ll R$, this implies the simpler bound with bracket $H+XR+HL+C_0/L$. If $X^{1/3}H^{-1/6}R^{-1/6}\in[1,\min(A,B)]$, it gives

$$
\|U_\alpha(A,B)-P_\alpha(X)\|_H^2
\ll_\epsilon\mathcal E_\epsilon\|\alpha\|_2^2
\left[H+XR+H^{5/6}X^{1/3}R^{-1/6}\right].
\tag{1.15}
$$

For dense amplifier supports, separate use of Theorem 1 gives the larger mixed term $H^{5/6}X^{1/3}R^{1/12}$. At $H=X$, $R=X^{1/10}$ and $A=B=X^{1/2}$, the full bound divided by $\|\alpha\|_2^2$ improves from exponent $47/40$ to $23/20$; the common baseline $XR$ has exponent $11/10$. Both optimizers are admissible. For sparse supports the separate bound can be smaller, and one may take the minimum.

The improvement in (1.13) averages $m$ inside the unrestricted source numerator, instead of paying $q_m^{1/2}$ as a fixed multiplier. It includes actual Möbius coefficients on the squarefree amplifier support. It does not replace their $\ell^2$ mass by one.

These results concern a particular divisor coefficient and its explicitly evaluated polar part. The general cubic large sieve has a real Gauss-bias obstruction: the lower bound of de Faveri, Dunn and Hoffstein [3] and the upper bound of de Faveri [4] retain the $(HX)^{2/3}$ term for arbitrary squarefree coefficients. Theorem 2 makes no arbitrary-coefficient assertion.

The equal-product centering mechanism is already present in the ordinary product-moment theorem [5, Sections 3 and 5–9]. That proof also treats full imprimitive Gauss columns and retains one centering saving through its final divisor sum. We use its ordinary product estimate as the noncube input, with complete squarefree and coprime projections. The additional calculation here is a four-variable cube count for squarefree whole columns, with one contour shift on each centered side, followed by comparison of a short rectangle with the source pole on all natural rows. The pole-subtracted mean (1.8) is a separately specified estimate; it is not an improvement of the ordinary product theorem in [5].


Theorem 4 and Theorem 5 in Section 10 add a strict saving for a genuine mixed coefficient, using the newer mixed-product moment [7]. With one inverse factor in a fixed short interval and two ordinary factors of positive length, equal-product centering controls the complete Gauss mean below its generic mixed scale. If the total inverse length is additionally below the cube root of the dual row scale by a fixed power, the same saving holds after subtraction of the explicit ordinary-pair pole. At the example (10.26), the full bound is $O(Y^{10/9-\eta})$ for some $\eta>0$, whereas the stated direct comparison is $Y^{10/9+\epsilon}$. Sections 1–9 retain their earlier results, and Section 8 alone retains its additional zero-free assumption.

## 2. The analytic inputs and the exact norm transform

We use two published estimates, recording their normalization and support.

**Ordinary product input [5, Theorem 1 and Section 2].** Let

$$
\vartheta_k(n)=\nu(n)\prod_j\chi_{a_j}(n)^{e_j}\chi_n(k),
$$

where $\nu$ belongs to a fixed finite group supported above $2,3$, and the radical of all displayed moving factors $a_j$ has norm at most $V$. On rows $q_k\ll K$ whose inducing character is nonprincipal, any two centrally normalized ordinary sums with this same character have squared product mean

$$
\ll_\epsilon (KV)^{1+\epsilon},
\tag{2.1}
$$

uniformly over bounded logarithmic ordinary lengths. Both factors may carry a common fixed extra column-deletion radical of polynomially bounded norm, at subsidiary cost. Every displayed moving factor retains its natural zeros, even when its exponent is zero modulo three. The charge $V$ is its radical norm. Common norm heights cost a polynomial and the profile orders are finite.

**Raw Kubota mean [1, Lemma 6.6].** For $0\ne f\in\mathcal O$, $1<\sigma\le5/4$ and $M\ge1$,

$$
\sum_{0\ne a\in\mathcal O\atop q_a\le M}
|\psi(fa,\sigma+it)|^2
\ll_{\sigma,\epsilon}q_f^{1/2}M^{1+\epsilon}(1+|t|)^2.
\tag{2.2}
$$

The numerator $a$ is unrestricted. The series $\psi$ here is the raw series of [1, (6.1)–(6.2)], with possible pole at $4/3$, not its normalized shift. This distinction fixes the line $1+\epsilon$ used below. We also use the exact one-variable expansion [1, Lemma 6.7] and its removal of coprimality [1, Corollary 6.2]; these will be written in the needed form in Section 5.

For a squarefree-supported divisor-bounded coefficient $b(n)$ of length $X$, put

$$
F_b(h)=X^{-1/2}\sum_{(n,D)=1}b(n)G(n)\overline{\chi_n(mh)}.
$$

Expand its norm and write $n=gu$, $n'=gv$, where $g,u,v$ are squarefree and pairwise coprime. The normalized Gauss CRT identity and [2, Corollary 4.1] give the following form of [2, (9.19)]:

$$
\begin{aligned}
\|F_b\|_H^2={}&\frac{4\pi}{9\sqrt3}\frac H X
\sum_{g:(g,D)=1}\frac1{q_g}
\sum_{(u,v)=1\atop(uv,gD)=1}
\frac{b(gu)\overline{b(gv)}}{\sqrt{q_uq_v}}\\
&\quad\times\sum_{k\in\mathcal O}
\widetilde r_g(k)\chi_u(gm^2k)\overline{\chi_v(gm^2k)}
\Phi^\dagger\!\left(\frac{kg\sqrt H}{nn'}\right).
\end{aligned}
\tag{2.3}
$$

Here $\lambda=1+2\omega$,

$$
r_g(k)=\sum_{\ell\mid(g,k)}\mu(g/\ell)q_\ell,\qquad
\widetilde r_g(k)=e^{2\pi i\operatorname{Tr}(-k/(3\lambda))}r_g(k),
\tag{2.4}
$$

and $\Phi^\dagger$ is the radial Schwartz transform with Bessel normalization [2, (4.4)]. This is an identity for the full primary row sum. In particular it does not replace those rows by squarefree ones. Simultaneous conjugation of the two displayed cubic characters makes no difference to the estimates.

The source formula permits arbitrary squarefree column coefficients, so it applies to a signed equal-product mixture before its square is expanded. All its column and gcd masks remain in (2.3). The zero frequency forces $u=v=1$, and hence contributes

$$
O_\epsilon(HX^\epsilon)
\tag{2.5}
$$

for a bounded-mass mixture of the profiles in (1.2).

For $k=\ell k'$, with $\ell\mid g$, the effective norm scale of $k'$ is

$$
K_{g,\ell}=\frac{X^2}{Hq_gq_\ell}.
\tag{2.6}
$$

Common logarithmic Fourier separation of the radial kernel precedes row inequalities. It places one norm power on each whole column, and the same power on its two ordinary factors. The weighted Fourier mass has finite profile and polynomial height cost, with arbitrary decay above (2.6). The finite unit classes and valuations above $2,3$ are separated in their actual primary presentation. There are finitely many character types and geometrically summable valuation costs; (2.1) includes these fixed twists.

## 3. The noncube frequencies and complete projections

We prove that the terms with $gm^2k$ not a cube cost

$$
O_\epsilon(\mathcal E_\epsilon XR)
\tag{3.1}
$$

for $b=b_{A,B}$, for an equal-product difference, or with an additional factor $Q^2$ for the mixture in Theorem 2. The inducing cubic Hecke character is nonprincipal on these rows. Indeed the Kummer character of a noncube is nontrivial; removing finitely many column primes does not make it principal. When its noncube class is supported only above $2,3$ or in the units, it is one of the fixed nonprincipal characters included in (2.1). The finite primary-presentation conversion is applied to the full character, retaining that nonprincipal restriction.

For a selected $g,\ell$, the moving radical of $gm^2\ell$ divides $gm$ and has norm at most $q_gR$. Its exponent in the numerator does not change this radical charge. The common column deletion $D$ is retained separately. Expand the complete cross condition

$$
\boldsymbol1_{(u,v)=1}=\sum_{d\mid u,v}\mu(d)
\tag{3.2}
$$

before factor bounds. Nonzero coefficients make $d$ squarefree, $(d,gD)=1$, and force the quotient columns to be prime to $d$. Each column extraction supplies $q_d^{-1/2}$ and a cubic scalar of modulus at most one. For each squarefree $q=gd$, allocate $q=q_1q_2$ to the two ordinary factors. The remaining column sum has the form

$$
J_q(k')=\sum_{(ab,qD)=1}
\frac{\mu^2(a)\mu^2(b)\boldsymbol1_{(a,b)=1}}{\sqrt{q_aq_b}}
\chi_{ab}(gm^2\ell k')
W_1(q_{q_1}q_a/A)W_2(q_{q_2}q_b/B).
\tag{3.3}
$$

Whole-column powers and the fixed annular ratios have been incorporated into the common profiles. Allocations have divisor-bounded multiplicity.

First expand the internal gcd by $t\mid a,b$. Set $a=t\alpha$, $b=t\beta$. The two squarefree indicators force $t$ squarefree and $(\alpha\beta,t)=1$. Only then expand

$$
\mu^2(\alpha)=\sum_{r^2\mid\alpha}\mu(r),\qquad
\mu^2(\beta)=\sum_{s^2\mid\beta}\mu(s).
\tag{3.4}
$$

The final quotients are unrestricted at $r,s$; their fixed common deletion is $\operatorname{rad}(qDt)$. The scalar in the normalized product has absolute value at most $(q_tq_rq_s)^{-1}$, and the ordinary scales become

$$
\frac{A}{q_{q_1}q_tq_r^2},\qquad
\frac{B}{q_{q_2}q_tq_s^2}.
\tag{3.5}
$$

All extracted character factors, including their zeros, remain in the exact expansion. They may be bounded by one only after a positive norm is taken. This ordering avoids the incorrect substitution of $r^2t$ for simultaneous divisibilities when $r$ and $t$ overlap.

Apply (2.1) to each final ordinary product and Minkowski in the row norm. The sums of $1/q_t$, $1/q_r$, $1/q_s$ are harmonic up to a subsidiary power, and all actual nonempty scales are allowed. Thus the squared row norm of (3.3), on a row box of size $K'$, is

$$
\ll_\epsilon\mathcal E_\epsilon K'q_gR.
\tag{3.6}
$$

Cauchy pairs the two column sums, and the two extracted $d$ scalars leave the harmonic weight $1/q_d$. In (2.3), the Ramanujan expansion has coefficient $q_\ell$. Inserting (2.6) and (3.6) yields

$$
\frac{H}{Xq_g}\,q_\ell\,K_{g,\ell}\,q_gR
=\frac{XR}{q_g}.
\tag{3.7}
$$

Summing $g$, $d$, and the $\ell\mid g$ choices costs only a subsidiary power. If $K_{g,\ell}<1$, the retained nonzero row boxes start at norm one and their Schwartz tail sums to $O(K_{g,\ell})$; the scale is not replaced by one. This proves (3.1). Equal-product differences give four such bilinear terms; a mixture costs at most $Q^2$.

## 4. Smooth cube counting and centering on both sides

Because $(g,m)=1$ and both are squarefree, the nonzero cube condition in (2.3) is

$$
gm^2k\text{ is a cube}\quad\Longleftrightarrow\quad k=g^2mt^3
\quad(t\ne0).
\tag{4.1}
$$

Its actual root norm scale is

$$
T_{g,n,n'}=\frac{(q_nq_{n'}/(HR))^{1/3}}{q_g}.
\tag{4.2}
$$

The symbols impose $(t,uv)=1$. On this support $r_g(k)=\phi(g)$, and the additive phase in (2.4) is one, as in [2, (9.22)]. Each nonzero cube has three cube roots.

We use the smooth form of lattice counting, including scales below one. If $f(z)=\Phi^\dagger(z^3)$, then $f$ is radial Schwartz and smooth at zero. For every $T>0$, planar Poisson gives

$$
\sum_{0\ne t\in\mathcal O}f(t/\sqrt T)=c_fT+O_f(1).
\tag{4.3}
$$

For $T\ge1$ the full lattice sum has error $O_{f,N}(T^{-N})$, and omitting zero changes it by the constant $f(0)$. For $T<1$ the nonzero sum is $O_{f,N}(T^N)$, while the proposed main term is bounded. Complete inclusion–exclusion therefore gives

$$
\sum_{t\ne0\atop(t,Q)=1}f(t/\sqrt T)
=c_fT\prod_{\mathfrak p\mid Q}(1-q_{\mathfrak p}^{-1})
+O_f(2^{\omega(Q)}).
\tag{4.4}
$$

Indeed the divisor $d\mid Q$ changes the scale to $T/q_d$; its rotation is immaterial by radiality. No perimeter error is required. Summing the error in (4.4) in (2.3) costs $O_\epsilon(HX^\epsilon)$: for fixed $g$ there are $O_\epsilon(X^{2+\epsilon}/q_g^2)$ pairs, the column denominator has size $q_g/X$, and the remaining factors give $O_\epsilon(H/q_g)$. This is harmonic in $g$.

The exact cube main term is

$$
\rho c_3^2\widehat\Phi(2/3)
\frac{H^{2/3}}{XR^{1/3}}\,
\mathcal C_D(b),
\tag{4.5}
$$

where

$$
\mathcal C_D(b)=\sum_{(nn',D)=1}
\frac{b(n)\overline{b(n')}}{(q_nq_{n'})^{1/6}}
\prod_{\mathfrak p\mid nn'}(1-q_{\mathfrak p}^{-1}).
\tag{4.6}
$$

The density factor follows by multiplying $\phi(g)/q_g$ by the root coprimality density for $uv$. The archimedean integral, cube-root multiplicity and primary density are evaluated in [2, (9.25)–(9.35)]. Only an upper bound for (4.6) will be needed; no identification with the entire norm of (1.5) is used.

Let $n=uv$ and $n'=u'v'$ in (4.6). Squarefreeness forbids a prime from occurring twice on the same side, but permits it on both sides. The four-variable Dirichlet series has the good-prime factor

$$
Q_q(z_1,z_2,z_3,z_4)
=1+(1-q^{-1})
(z_1+z_2+z_3+z_4+z_1z_3+z_1z_4+z_2z_3+z_2z_4),
\quad z_i=q^{-s_i},
\tag{4.7}
$$

and factor one at primes of $D$. It factors as

$$
\prod_{i=1}^4\zeta_\lambda(s_i)\,E_D(s_1,s_2,s_3,s_4),
\tag{4.8}
$$

where $E_D$ converges normally when every $\operatorname{Re}s_i>1/2$. To check this, multiply (4.7) by $\prod_i(1-z_i)$. Its degree-one terms are $-q^{-1}\sum_i z_i$; the other terms have total degree at least two. Deleted primes contribute $\prod_i(1-q^{-s_i})$, with subsidiary cost in $q_D$ on any fixed smaller region.

For $b=b_{A,B}-b_{L,X/L}$, Mellin inversion supplies the left factor

$$
\begin{aligned}
M(s_1,s_2)={}&\widehat W_1(s_1-1/6)\widehat W_2(s_2-1/6)\\
&\times\left[A^{s_1-1/6}B^{s_2-1/6}
-L^{s_1-1/6}(X/L)^{s_2-1/6}\right],
\end{aligned}
\tag{4.9}
$$

and its conjugate-profile counterpart in $s_3,s_4$. Since $AB=X$, we have $M(1,1)=0$.

Here is the contour order, needed to retain the saving on both sides. Start at real parts $1+\delta$. Shift $s_1$ to $1/2+\delta$, leaving $s_2$ fixed. In the residue at $s_1=1$, shift $s_2$ to $1/2+\delta$. The double residue vanishes by $M(1,1)=0$. The surviving left terms thus have real parts

$$
(1/2+\delta,1+\delta)\quad\text{or}\quad(1,1/2+\delta).
\tag{4.10}
$$

Repeat that order for $s_3,s_4$. Each of the four resulting terms has one variable shifted on each side. All passages lie inside the normal-convergence region of $E_D$, and the only crossed poles are the displayed zeta poles. Polynomial zeta growth is absorbed by the rapid decay of the profile transforms.

Because $L\le A,B$ and $L\le X/L$, the scale part on either left contour is

$$
O_\epsilon(X^{5/6+\epsilon}L^{-1/2}),
\tag{4.11}
$$

with rapid vertical decay after sufficiently many profile derivatives. The right side has the same bound. Hence

$$
|\mathcal C_D(b_{A,B}-b_{L,X/L})|
\ll_\epsilon(Xq_D)^\epsilon\frac{X^{5/3}}L.
\tag{4.12}
$$

Combining (4.5), (4.12), (3.1) and the zero and lattice errors proves the first line of (1.7).

For Theorem 2 replace the square bracket in (4.9) by

$$
\sum_jc_jA_j^{s_1-1/6}B_j^{s_2-1/6}.
\tag{4.13}
$$

Its value at $(1,1)$ is zero, and (4.11) becomes $O_\epsilon(QX^{5/6+\epsilon}L_0^{-1/2})$. This proves (1.11). If $L_0\ge X^{1/3}R^{-2/3}$, then

$$
C_0/L_0\le H^{2/3}(XR)^{1/3}\ll H+XR,
\tag{4.14}
$$

which proves its final assertion.

The scale factor (4.13) in fact vanishes along the entire diagonal $s_1=s_2$. Accordingly, a common whole-column norm twist preserves the residue cancellation. One can alternatively impose the single condition $\widehat W_1(5/6)=0$ to obtain a cube error $C_0/A$ for one rectangle: the $s_1$ residue then vanishes for every $s_2$. That condition is generally lost after a common varying norm twist, whereas (4.13) is preserved.

## 5. Comparing a short rectangle with its pole

Write $T=X/L$. Split $m=m_0m_1m_2$ according to the valuation of $h$ modulo three. There is a unique expression

$$
h=m_1m_2^2ab^2c^3,\qquad (ab,m)=1,\quad\mu^2(ab)=1,
\tag{5.1}
$$

and then

$$
mh=(m_0a)(m_1b)^2(m_2c)^3.
\tag{5.2}
$$

Thus the squarefree and squared parts of the source numerator are $\alpha=m_0a$ and $\beta=m_1b$. The cube part may overlap either. We replace cube powers by their radical only for the column-deletion mask, retaining all their natural zeros.

In $F(L,T)$ the short variable $u$ is squarefree and prime to $mhD$. Gauss multiplicativity allows the long sum to use numerator $\alpha u\beta^2$, with the original common deletions. Let

$$
E=\frac{\operatorname{rad}(cD)}{(\operatorname{rad}(cD),\alpha\beta)}.
\tag{5.3}
$$

It is independent of $u$ on the actual support.

The notation $\psi_Q(r,z)$ means
$$
\psi_Q(r,z)=\sum_{(v,Q)=1}\frac{g_3(r,v)}{q_v^z}
$$
in its initial half-plane and then by meromorphic continuation. With $T=X/L$, the decomposition (5.1)–(5.2), and $Q_u=\operatorname{rad}(mhDu)$, the exact complex continuous remainder is
$$
\begin{aligned}
\mathcal R_{m,h}(L,T;D)
={}&X^{-1/2}\sum_{(u,mhD)=1}^{\mathrm{sf}}
G(u)\overline{\chi_u(mh)}W_1(q_u/L)\\
&\times\frac1{2\pi i}\int_{\operatorname{Re}z=1+\delta}
\widehat W_2(z-1/2)T^{z-1/2}
\psi_{Q_u}(\alpha u\beta^2,z)\,dz.
\end{aligned}
$$
This follows by Mellin inversion of the long ordinary sum and moving its contour past the possible source pole at $z=4/3$. Corollary 6.2 of David–de Faveri–Dunn–Stucky gives (5.4) after absolute values. For Theorem 3 the continuous remainder is exactly
$$
\mathcal R_\alpha(h)=R^{-1/2}\sum_m\alpha_m\phi_m(h)
\mathcal R_{m,h}(L,T;Dm).
$$
It is defined before the short pole count and its error. The complex signs in this identity are retained until the Cauchy step in Section 7.

The long-variable expansion from [1, Lemma 6.7], at central exponent $1/2$, with [1, Corollary 6.2] for the extra deletions, has an explicit pole plus a remainder bounded by

$$
T^{1/2+\delta}
\sum_{d\mid\alpha u\atop e\mid E}\frac1{q_{de}^{1/2+\delta}}
\int_{\mathbb R}
|\psi(\alpha u\beta^2e/d,1+\delta+it)|
(1+|t|)^{-J}\,dt.
\tag{5.4}
$$

Choose $0<\delta<1/4$ small enough for the requested loss, and $J$ sufficiently large for the fixed profiles and heights. Complex or signed profiles follow by linearity and the same seminorm estimates; positivity of the source's test profile is not used in its Mellin proof. Formula (5.4) uses the raw series in (2.2).

Let $\mathcal R_{m,h}$ be the normalized sum over $u$ of these continuous remainders, with its actual Gauss phase. Cauchy in the $O(L)$ short terms, and then divisor and integral Cauchy, give

$$
\sum_h\Phi(q_h/H)|\mathcal R_{m,h}|^2
\ll_\epsilon\mathcal E_\epsilon
\sum_{h,u,d,e}\frac1{q_dq_e}
\int_{\mathbb R}|\psi(\alpha u\beta^2e/d,1+\delta+it)|^2
(1+|t|)^{-J}\,dt.
\tag{5.5}
$$

Indeed $LT/X=1$: the short-variable Cauchy count and the squared long-variable prefactor cancel the squared central normalization. Divisor multiplicities cost a subsidiary power. In this positive upper bound, extend $e$ to all divisors of $\operatorname{rad}(cD)$ after its original restrictions have been imposed.

Write $d=d_0d_ad_u$, with $d_0\mid m_0$, $d_a\mid a$, $d_u\mid u$. These factors are disjoint on the original support. Combine $(a/d_a)(u/d_u)$ into the unrestricted numerator variable of (2.2). Its representation multiplicity is divisor bounded and its length is at most a fixed constant times

$$
M=\frac{HL}{q_{m_1}q_{m_2}^2q_b^2q_c^3q_{d_a}q_{d_u}}.
\tag{5.6}
$$

The fixed multiplier is $(m_0/d_0)(m_1b)^2e$, whose square-root norm is

$$
(q_{m_0}/q_{d_0})^{1/2}q_{m_1}q_bq_e^{1/2}.
\tag{5.7}
$$

Apply (2.2) and integrate in $t$. Combining (5.6), (5.7) and the scalar in (5.5), a slice costs

$$
\mathcal E_\epsilon\,
\frac{HLq_{m_0}^{1/2}}{q_{m_2}^2q_bq_c^3}
q_{d_0}^{-3/2}q_{d_a}^{-2}q_{d_u}^{-2}q_e^{-1/2}.
\tag{5.8}
$$

The $d_a,d_u$ sums converge, the $d_0,e$ divisor sums cost subsidiary powers, the $b$ sum is harmonic and the $c^{-3}$ sum converges. There are divisor-boundedly many partitions of $m$, and $q_{m_0}^{1/2}/q_{m_2}^2\le R^{1/2}$. If the actual length in (5.6), including its fixed support constant, is below one, that slice is empty; no artificial unit-length contribution is inserted into the outer sums. Consequently

$$
\|\mathcal R\|_H^2\ll_\epsilon\mathcal E_\epsilon LHR^{1/2}.
\tag{5.9}
$$

It remains to count the short-variable pole. The source pole is zero unless $\beta=1$, equivalently $m_1=b=1$. On this support exact Gauss multiplicativity gives

$$
G(\alpha,u)\overline{G(\alpha u)}=\overline{G(\alpha)}.
\tag{5.10}
$$

Cube and external deletions remain in the column mask. With $Q_*=\operatorname{rad}(\alpha cD)$, the remaining short positive arithmetic sum is

$$
\sum_{(u,Q_*)=1}\mu^2(u)k(u)q_u^{-1/6}W_1(q_u/L),
\qquad k(u)=\prod_{\mathfrak p\mid u}k_{\mathfrak p}.
\tag{5.11}
$$

Its Dirichlet series is

$$
\prod_{\mathfrak p\nmid3Q_*}(1+k_{\mathfrak p}q_{\mathfrak p}^{-s})
=\zeta_\lambda(s)A_{Q_*}(s),
\tag{5.12}
$$

with normal convergence of the analytic factor for $\operatorname{Re}s>1/2$. At $s=1$,

$$
A_{Q_*}(1)=a_k\prod_{\mathfrak p\mid Q_*}(1+k_{\mathfrak p}/q_{\mathfrak p})^{-1}.
\tag{5.13}
$$

The source pole has the factor $k(Q_*)$. Since

$$
\frac{k_{\mathfrak p}}{1+k_{\mathfrak p}/q_{\mathfrak p}}=v_{\mathfrak p},
\tag{5.14}
$$

the residue of (5.11), multiplied by the long-variable residue and central normalization, is exactly (1.5). This verifies every deleted-prime factor directly.

Shifting (5.12) to $1/2+\delta$ gives absolute short-sum error $O_\epsilon(L^{1/3+\epsilon}q_{Q_*}^{\epsilon})$. After the long-variable pole and central normalization, the error is at most

$$
\mathcal E_\epsilon X^{1/3}L^{-1/2}q_\alpha^{-1/6}.
\tag{5.15}
$$

To sum its square, use $m=m_0m_2$, $h=m_2^2ac^3$ on the polar support. The elementary nonempty-box bound $\sum_{q_a\le Y}q_a^{-1/3}\ll Y^{2/3}$ gives

$$
\begin{aligned}
\sum_{h\asymp H\atop\beta=1}q_\alpha^{-1/3}
&\ll_\epsilon H^{2/3}R^{-1/3+\epsilon}
\sum_{m_2\mid m}\frac1{q_{m_2}}\sum_c\frac1{q_c^2}\\
&\ll_\epsilon(HR)^\epsilon H^{2/3}R^{-1/3}.
\end{aligned}
\tag{5.16}
$$

Thus the pole-count error contributes $O_\epsilon(\mathcal E_\epsilon C_0/L)$. Together with (5.9), this proves the second line of (1.7). The squared triangle inequality proves (1.8), and balancing its last two terms gives (1.9)–(1.10).

## 6. A positive divisor decomposition of the cube term

There is a useful alternative proof of the saving in (4.12). Put $w(n)=\phi(n)/q_n$ for squarefree $n$. The elementary identity

$$
\prod_{\mathfrak p\mid nn'}(1-q_{\mathfrak p}^{-1})
=w(n)w(n')\sum_{d\mid(n,n')}\frac1{\phi(d)}
\tag{6.1}
$$

holds because each prime common to $n,n'$ contributes
$1+1/(q_{\mathfrak p}-1)=1/w(\mathfrak p)$. Hence the cube form has the exact positive expansion

$$
\mathcal C_D(b)=\sum_{(d,D)=1}\frac1{\phi(d)}
\left|\sum_{d\mid n\atop(n,D)=1}
 b(n)w(n)q_n^{-1/6}\right|^2.
\tag{6.2}
$$

Only squarefree $d$ occur. This identity applies to arbitrary complex squarefree column coefficients; the following estimate uses their ordinary product structure.

For a fixed $d$, allocate $d=d_1d_2$ between the ordinary factors. After extraction the two-variable arithmetic series has local factor

$$
1+(1-q^{-1})(q^{-s_1}+q^{-s_2})
\tag{6.3}
$$

outside $dD$, and factor one at $dD$. Removing $\zeta_\lambda(s_1)\zeta_\lambda(s_2)$ leaves normal convergence for both real parts greater than $1/2$. The leading residue of each allocation depends on the product of the daughter scales, $X/q_d$, and the two fixed profiles. It therefore cancels for the equal-product mixture in Theorem 2.

Apply the ordered two-variable contour shift used in (4.10), now to each allocation. Actual daughter scales may be below one; Mellin inversion retains them as they stand. The scale bound, including the factor $w(d)q_d^{-1/6}$, is

$$
\begin{aligned}
\left|\sum_{d\mid n\atop(n,D)=1}b(n)w(n)q_n^{-1/6}\right|
&\ll_\epsilon Q(Xq_dq_D)^\epsilon
\frac{w(d)X^{5/6}}{q_d\sqrt{L_0}}
\sum_{d_1d_2=d}(\sqrt{q_{d_1}}+\sqrt{q_{d_2}})\\
&\ll_\epsilon Q(Xq_dq_D)^\epsilon
\frac{w(d)X^{5/6}}{\sqrt{q_dL_0}}.
\end{aligned}
\tag{6.4}
$$

The last sum is bounded by a divisor factor times $\sqrt{q_d}$. Inserting (6.4) into (6.2) leaves

$$
\mathcal C_D(b)\ll_\epsilon Q^2(Xq_D)^\epsilon\frac{X^{5/3}}{L_0}
\sum_{d\text{ squarefree}}\frac{w(d)}{q_d^{2-\epsilon}}
\ll_\epsilon Q^2(Xq_D)^\epsilon\frac{X^{5/3}}{L_0}.
\tag{6.5}
$$

The complete divisor sum is convergent. Thus the positive representation preserves the two-sided square-root saving after all allocations. It also identifies the specific divisor-restricted column averages which carry the cube bias. It is not an estimate for the noncube part with arbitrary coefficients.

## 7. The amplifier inside the source numerator

We prove Theorem 3. On the nonzero support of $\phi_m(h)$, $(m,h)=1$. Write $h=ab^2c^3$, with $\mu^2(ab)=1$. In the short rectangle, $u$ is squarefree and prime to $mhD$. The source numerator is $mau b^2$, and the additional deletion divisors in (5.4) may be extended positively to $e\mid\operatorname{rad}(cD)$ after their original restrictions have been imposed. This radical is independent of $m,u$ on the actual support.

Split the source removal divisor as

$$
d=\delta d_ad_u,\qquad\delta\mid m,\quad d_a\mid a,\quad d_u\mid u.
\tag{7.1}
$$

Cauchy in the combined $(m,u)$ sum has coefficient-square mass $O(L\|\alpha\|_2^2)$. The squared central normalization is $(XR)^{-1}$ and the squared long-source prefactor is $T=X/L$. Consequently the factor left outside the positive raw-source sum is $\|\alpha\|_2^2/R$. Divisor and integral Cauchy cost only subsidiary powers, and yield

$$
\begin{aligned}
\|\mathcal R_\alpha\|_H^2
\ll_\epsilon{}&\mathcal E_\epsilon\frac{\|\alpha\|_2^2}{R}
\sum_{h,m,u,\delta,d_a,d_u,e}\frac1{q_\delta q_{d_a}q_{d_u}q_e}\\
&\times\int_{\mathbb R}
\left|\psi\left(\frac m\delta\frac a{d_a}\frac u{d_u}b^2e,
1+\eta+it\right)\right|^2(1+|t|)^{-J}\,dt.
\end{aligned}
\tag{7.2}
$$

All Gauss phases and their zeros were retained before this positive upper bound. Fix $\delta,b,c,d_a,d_u,e$, and combine $(m/\delta)(a/d_a)(u/d_u)$ into one numerator. Its actual length is at most a fixed support constant times

$$
\frac{HLR}{q_\delta q_b^2q_c^3q_{d_a}q_{d_u}}.
\tag{7.3}
$$

Each such numerator has only divisor-boundedly many ordered factorizations, which also bound the number of possible $(m,a,u)$. The fixed multiplier in (2.2) is now $b^2e$, of square-root norm $q_bq_e^{1/2}$; it contains no amplifier factor. Multiplying (7.3), this source cost and the scalar in (7.2) gives

$$
\mathcal E_\epsilon\|\alpha\|_2^2
\frac{HL}{q_bq_c^3q_\delta^2q_{d_a}^2q_{d_u}^2q_e^{1/2}}.
\tag{7.4}
$$

The complete $\delta$ sum has weight $q_\delta^{-2}$ and converges. This includes $\delta=m$: that case must not be assigned a divisor-bounded multiplicity before $\delta$ is fixed. At $q_\delta\asymp R$ the aggregate weight of this part is $O(R^{-1})$. The $d_a,d_u$ sums also converge; $b$ is harmonic and $c^{-3}$ is summable. The $e$ divisor sum has subsidiary cost in $q_cq_D$. Actual empty numerator boxes contribute zero. We obtain (1.13).

For the short pole-count error use (5.15) for each $m$ and the external zero $(m,h)>1$. The polar support has $h=ac^3$, and its row sum of $q_a^{-1/3}$ is $O_\epsilon(H^{2/3+\epsilon})$. Cauchy in $m$, with the outside $1/R$ and the factor $q_m^{-1/3}$ in each squared error, gives

$$
\|U_\alpha(L,X/L)-P_\alpha-\mathcal R_\alpha\|_H^2
\ll_\epsilon\mathcal E_\epsilon\|\alpha\|_2^2
\frac{|\mathcal M|}{R}\frac{C_0}{L}.
\tag{7.5}
$$

For the initial equal-product comparison, Cauchy in $m$ and the first line of (1.7), with its actual deletion $Dm$, give

$$
\|U_\alpha(A,B)-U_\alpha(L,X/L)\|_H^2
\ll_\epsilon\mathcal E_\epsilon\|\alpha\|_2^2
\frac{|\mathcal M|}{R}\left(H+XR+\frac{C_0}L\right).
\tag{7.6}
$$

The extra factor $q_m$ in the deletion norm is absorbed by renaming the subsidiary loss. Combining (1.13), (7.5) and (7.6) proves (1.14); balancing the last two terms of its simplified form proves (1.15).

The raw-source estimate (1.13) does not need a small-prime mesh, and the coefficients $\alpha_m$ may include a truncated Möbius convolution restricted to squarefree $m$. Common Mellin powers on $m$ preserve their squared mass. These properties distinguish it from the ordinary amplified moment in [5]. The latter bounds a different family and supplies no automatic improvement of (1.13). Conversely, the present theorem does not supply an ordinary joint moment for an arbitrary amplifier: its continuous source norm and polar subtraction are essential parts of the statement.

### 7.1. A prescribed Möbius–Gauss first mean

The same numerator averaging sharpens the standard first-mean application in [6, Lemma 2]. We record the coefficient-preserving consequence, without claiming a new Type I/II mechanism.

**Corollary 3.1.** Let $c$ be a nonzero good primary index, $E$ a squarefree good exclusion, and $F$ a fixed smooth annular function. Then

$$
\left|\sum_{(b,E)=1}\mu(b)G(b)\overline{\chi_b(c)}F(q_b/Y)\right|
\ll_{\epsilon,F}(Yq_cq_E)^\epsilon
\left(Y^{5/6}+Y^{3/4}q_c^{1/8}\right),\qquad Y\ge1.
\tag{7.7}
$$

The fixed ramified multipliers admitted by [1, Corollary 6.2 and Lemma 6.3] are also permitted, at fixed cost. The profile dependence uses finitely many seminorms, so common norm twists have polynomial height cost. The earlier bound in [6] has $q_c^{1/4}$ in place of $q_c^{1/8}$.

*Proof.* First write $c=c_1c_2^2$, with $\mu^2(c_1c_2)=1$. Choose $m_U(n)=\mu(n)V_\le(q_n/U)$, where $V_\le$ is one through one and supported through two, and $U^2$ exceeds the entire supported $b$ range. Since $\delta_1-m_U*1$ vanishes through $U$, its convolution square vanishes on this range. Multiplication by $\mu$ gives there the exact identity

$$
\mu=2m_U-m_U*m_U*1.
\tag{7.8}
$$

Take $U\asymp Y^{1/2}$. For large $Y$ the isolated $m_U$ term has no annular support. The remaining dyads have two truncated Möbius factors and one ordinary factor of length $L$. Their whole column is squarefree, so all three factors are squarefree and pairwise coprime. Separate the product profile in logarithmic norm coordinates before applying the following estimates.

Fix $0\le\vartheta\le1/3$. If $L\le Y^{1-\vartheta}$, every factor is at most a constant times this length, while the largest is at least a constant times $Y^{1/3}\ge Y^\vartheta$. Group it against the other two. The resulting lengths $A_1,A_2$ satisfy $A_1A_2\asymp Y$ and $Y^\vartheta\ll A_i\ll Y^{1-\vartheta}$. Cubic reciprocity, the exact law $G(uv)=G(u)G(v)\overline{\chi_u(v)}$, and the ordinary cubic large sieve [1, Theorem 3.12] give

$$
|\mathrm{Type\ II}|^2
\ll (Yq_cq_E)^\epsilon Y\left(A_1+A_2+Y^{2/3}\right).
\tag{7.9}
$$

The fixed twist of $c$ lies in the actual common coefficient vectors and costs no norm factor here.

If $L>Y^{1-\vartheta}$, combine the two Möbius factors into a squarefree $r$ of length $R\asymp Y/L\ll Y^\vartheta$. Its coefficient $a_r$ is divisor bounded and has $\sum_r|a_r|^2\ll RY^\epsilon$. Its exterior character enforces $(r,cE)=1$. The inner ordinary series is $\psi_{\operatorname{rad}(rcE)}(rc,z)$. In [1, Corollary 6.2], its source parameters are $a=rc_1$, $b=c_2$, and the extra deletion $C=\operatorname{rad}(E)/(\operatorname{rad}(E),\operatorname{rad}(c))$. Thus the source divisors are $d=d_cd_r$, with $d_c\mid c_1$, $d_r\mid r$, and $e\mid C$. The extra divisor $e$ is independent of $r$.

On $\operatorname{Re}z=1+\eta$, source coefficients have absolute value at most $(q_{d_c}q_{d_r}q_e)^{-1/2}$, up to allotted small powers. The source Euler denominator is uniformly bounded away from zero on this line. Cauchy in $r$, the divisors and the common integral leaves the outside factor $LR$. For fixed $d_c,d_r,e$, apply (2.2) to the unrestricted numerator $r/d_r$, of length $O(R/q_{d_r})$, with fixed multiplier $(c/d_c)e$. This gives the precise total scalar

$$
LR\frac1{q_{d_c}q_{d_r}q_e}
\left(\frac{q_cq_e}{q_{d_c}}\right)^{1/2}\frac R{q_{d_r}}
=\frac{LR^2q_c^{1/2}}{q_{d_c}^{3/2}q_{d_r}^2q_e^{1/2}}.
\tag{7.10}
$$

A nonempty original numerator slice has $R/q_{d_r}$ bounded below by a fixed support constant, so replacing the mean length by its maximum with one costs no power. The full $d_r$ sum converges; the other divisor sums have subsidiary cost. Hence the continuous Type I error is $\ll (Yq_cq_E)^\epsilon Y^{1/2}R^{1/2}q_c^{1/4}$. The possible source pole vanishes for $c_2\ne1$. Otherwise its absolute sum is at most a subsidiary power times $Y^{5/6}$, by [1, Lemma 6.7]. Together with (7.9), this proves

$$
|M_c(Y;E)|\ll (Yq_cq_E)^\epsilon
\left[Y^{5/6}+Y^{1-\vartheta/2}
+Y^{(1+\vartheta)/2}q_c^{1/4}\right].
\tag{7.11}
$$

Here $M_c(Y;E)$ denotes the sum in (7.7). Take $\vartheta=1/3$ when $q_c\le Y^{2/3}$, and $\vartheta=1/2-\log q_c/(4\log Y)$ when $Y^{2/3}\le q_c\le Y^2$. For $q_c\ge Y^2$ use the trivial bound $O_\epsilon(Y^{1+\epsilon})$. This proves (7.7). For general $c=c_{\rm cf}k^3$, put $\operatorname{rad}(k)$ into the exclusion, retain its character zeros and use $q_{c_{\rm cf}}\le q_c$. Bounded $Y$ and fixed support constants are absorbed by the implied constant. The permitted ramified multiples remain fixed multipliers in the same source mean. ∎

This sharper first mean does not improve the final signed remainder in [6, Theorem 1] through its existing two-branch argument. In that paper's notation, the pointwise branch in (5.7) changes from $c_0/2$ to $c_0/4$. Set every removal and overlap exponent, the outer $l$ exponent and the $e$ exponent to zero, and set $\eta=(1-\delta)/6$, where $0\le\delta\le1/3$. This is feasible on both completed boundary scales and has $\beta=1$, $r_0=\delta$, $n_0=c_0=(1+\delta)/2$. The generic column exponent is $2(n_0+1)/3$; the improved pointwise exponent is $n_0+2/3$, which exceeds it by $n_0/3$. The unchanged generic branch therefore gives the exact full-energy exponent

$$
n_0+\frac{2-n_0}{3}=1+\frac\delta3.
\tag{7.12}
$$

No discarded divisor loss is positive at this example. It is a feasible equality for those upper-bound inequalities, not an arithmetic lower bound. The corollary improves their first-mean input while leaving this limiting case unresolved.

## 8. A conditional refinement of the counting error

This section assumes an additional input; Theorems 1–3 do not use it. Suppose $2/3\le\theta<1$, $\zeta_\lambda$ has no zeros for $\operatorname{Re}s>\theta$, and $1/\zeta_\lambda$ has polynomial vertical growth on every closed smaller half-plane there.

The exact four-variable series (4.7) factors further as

$$
\frac{\prod_i\zeta_\lambda(s_i)}
{\prod_i\zeta_\lambda(2s_i)\,
 \zeta_\lambda(s_1+s_2)\zeta_\lambda(s_3+s_4)}
A_D(s_1,s_2,s_3,s_4),
\tag{8.1}
$$

where $A_D$ converges normally if all four real parts exceed $1/3$. After multiplication by $\prod_i(1-z_i)$, the unweighted quadratic terms of (4.7) are

$$
-\sum_i z_i^2-z_1z_2-z_3z_4.
$$

Dividing by $\prod_i(1-z_i^2)(1-z_1z_2)(1-z_3z_4)$ removes them. The remaining unweighted monomials have degree at least three, while terms carrying an additional $q^{-1}$ converge for positive real parts. The local denominators are nonzero in that region. At deleted primes define the factor directly from the actual local series one; no division by the possibly vanishing polynomial $Q_q$ is needed.

In the ordered contours of Section 4, move each selected variable to $\theta/2+\delta$. All reciprocal-zeta arguments then have real part greater than $\theta$, and the same-side companion is at one or $1+\delta$. Polynomial reciprocal growth is absorbed by the chosen finite profile order. Each side saves $L^{-(1-\theta/2)}$, so the cube error is $C_0/L^{2-\theta}$.

For the short pole count, use

$$
\prod_{\mathfrak p\nmid3}(1+k_{\mathfrak p}q_{\mathfrak p}^{-s})
=\frac{\zeta_\lambda(s)}{\zeta_\lambda(2s)}
\prod_{\mathfrak p\nmid3}
\frac{1+k_{\mathfrak p}q_{\mathfrak p}^{-s}}
{1+q_{\mathfrak p}^{-s}}.
\tag{8.2}
$$

The last product converges normally for $\operatorname{Re}s>0$. The same shift improves the squared short-count error to $C_0/L^{2-\theta}$. The source mean (5.9) is unchanged. Thus, under the stated input,

$$
\|F(A,B)-P(X)\|_H^2
\ll_\epsilon\mathcal E_\epsilon
\left(H+XR+LHR^{1/2}+\frac{C_0}{L^{2-\theta}}\right).
\tag{8.3}
$$

For example, conditional on that input at $\theta=7/8$, the interior optimization gives

$$
H+XR+H^{43/51}X^{16/51}R^{11/102},
\tag{8.4}
$$

with the same requirement that the optimizing $L$ belong to its permitted interval. This is a refinement of a counting contour, not a new zero-free theorem.

## 9. Scope, comparison and verification

The source one-variable expansion has an actual continuous remainder. The proof of Theorem 1 pays for its outer short-variable sum in (5.5) and for the square root of its fixed numerator in (5.7). Dropping either cost would produce a stronger, unsupported estimate. The natural row decomposition keeps cube towers throughout, including their column masks. The proof requires no unproved global residue sum over zeros.

For orientation, in the external-prime first-transform geometry one encounters $H=X^2R^2/P$ and the outside factor $P/(XR)$. Substituting (1.10) gives

$$
P+XR+P^{1/6}XR^{3/4},
\tag{9.1}
$$

when its optimizer is admissible. The term $P$ remains. Moreover the same original clean signed correlation already has an $O_\epsilon(P^{1+\epsilon})$ bound from [5], after the complete harmonic projections of Section 3. Accordingly, (9.1) is not a gain for that correlation. The coupled prime phases and the full signed Möbius inverse remainder are not bounded here. Theorem 2 cannot be transferred to two inverse factors with opposite characters merely because their Mellin scale factors also admit aspect-ratio centering.

The Gauss-bias correction in [2, Section 9] is an important predecessor: it subtracts a nontrivial asymptotic term for sequences subject to character-cancellation and roughness hypotheses, with a GRH input in the application. We use its exact transform and cube integral, but replace the noncube estimate by the ordinary product theorem [5] for the specified divisor class and retain the full common-prime density. We do not extend its arbitrary-sequence hypotheses or its prime-Gauss asymptotic.

The supplement retains exact algebra checks for the valuation decomposition (5.1)–(5.2), all cube masks in those cases, the source-divisor normalization (5.8), the optimizer, and the Euler factors. The original 32 valuation and 384 mask/phase fixtures were run during development and were not repeated merely for manuscript preparation. Their recorded outputs and code are provided. A separate check verifies the positive divisor kernel and its coupled-prime algebra. The amplifier fixture checks the source normalization and the same-quantity comparison in Theorem 3. The first-mean fixture checks (7.10), 37 rational optimization cases, and 21 feasible equality points for (7.12). These finite checks support the identities and conventions; they do not verify the contour shifts, the imported moments, or an infinite analytic theorem. The single-geometry numerical experiment from the working notes is not evidence for any theorem here and is omitted from the manuscript.

The Riemann hypothesis and the signed inverse estimate motivating this calculation remain open.

## 10. Strict saving for genuine mixed coefficients

The results in this section are unconditional. They combine the mixed-product theorem of [7] with the centering and source estimates above. The amplifier is now a fixed convolution of actual Möbius coefficients. This additional structure gives a strict saving in a parameter range where the arbitrary-amplifier comparison (1.14) is insufficient. It does not identify the resulting polar vector with every polar subtraction in [6].

Fix an integer $k\ge1$, inverse lengths $R_1,\ldots,R_k\ge1$, and common smooth annular profiles $V_1,\ldots,V_k,W_1,W_2$. Let $u_1,\ldots,u_k,t$ be real heights, common to all rows. All ordinary scales are at least one, and we take $Y\ge2$; bounded remaining ranges are absorbed in the constants. Put $R=\prod_iR_i$, $X=AB$, $Y=RX$ and
$$
\begin{aligned}
b_{A,B}^{\mathrm{mix}}(n)
 &=\sum_{r_1\cdots r_kab=n}
 \prod_{i=1}^k\left[\mu(r_i)q_{r_i}^{iu_i}V_i(q_{r_i}/R_i)\right]
 (q_aq_b)^{it}W_1(q_a/A)W_2(q_b/B),\\
\mathcal F_h(A,B)
 &=Y^{-1/2}\sum_{(n,E)=1}b_{A,B}^{\mathrm{mix}}(n)
 G(n)\overline{\chi_n(h)}.
\end{aligned}
\tag{10.1}
$$
Here $E$ contains the fixed bad primes other than the prime above $3$, already excluded by the primary convention, and $q_E\le Y^C$ for fixed $C$. The Gauss factor forces squarefreeness of the entire tuple product. All its original zero masks are retained.

Let $A_jB_j=X$ be a fixed finite collection of rectangles with the same profiles and heights at their respective positions. Let $\sum_jc_j=0$, $Q_0=\sum_j|c_j|$, and $L_0=\min_j\min(A_j,B_j)$. Define the common dual scale
$$
P=Y^2/H=Y^a,\qquad 0<a_0\le a\le a_1<3/2.
\tag{10.2}
$$
All constants below may depend on this compact interval, the fixed number of factors, support bounds, deletion exponent, and positive length buffers. There is no assertion uniform as these buffers vanish.

**Theorem 4 (centered mixed mean).** Suppose that one genuine inverse position has length $R_*$ satisfying
$$
Y^{\epsilon_I}\le R_*\le Y^{1-\delta_0}P^{-2/3},
\qquad L_0\ge Y^{\epsilon_O},
\tag{10.3}
$$
where $\epsilon_I,\epsilon_O,\delta_0>0$ are fixed. There are $\eta,\kappa>0$ such that, for $2+\max_i(|u_i|,|t|)\le Y^\kappa$,
$$
\left\|\sum_jc_j\mathcal F(A_j,B_j)\right\|_H^2
 \ll Q_0^2(HY)^{2/3}Y^{-\eta}.
\tag{10.4}
$$
Only finitely many homogeneous profile seminorms enter. The row norm is the complete natural primary norm (1.2), including principal rows. The common ordinary height in (10.1) is essential to the centering.

For the second statement, group the inverse positions into their genuine squarefree coefficient
$$
\alpha_m=\mu^2(m)\sum_{r_1\cdots r_k=m}
 \prod_i\mu(r_i)q_{r_i}^{iu_i}V_i(q_{r_i}/R_i).
\tag{10.5}
$$
It has $q_m\asymp R$, $\|\alpha\|_2^2\ll_\epsilon RY^\epsilon$ and support of cardinality $O(R)$. Gauss multiplicativity gives the exact identity
$$
\mathcal F_h(A,B)=R^{-1/2}\sum_m\alpha_mG(m)
 \overline{\chi_m(h)}F_{m,h}^{(t)}(A,B;Em),
\tag{10.6}
$$
where $F^{(t)}$ denotes (1.2) with the actual factor $(q_aq_b)^{it}$. Define
$$
\mathcal P_h(X)=R^{-1/2}\sum_m\alpha_mG(m)
 \overline{\chi_m(h)}P_{m,h}^{(t)}(X;Em).
\tag{10.7}
$$
The term $P^{(t)}$ is precisely (1.5), with $X^{1/3}$ replaced by $X^{1/3+it}$ and each $\widehat W_i(5/6)$ by $\widehat W_i(5/6+it)$. Its decomposition of $mh$ and the deletion $Em$ remain unchanged. Thus (10.7) specifies an actual ordinary-pair source pole, independent of the aspect ratio $A/B$.

**Theorem 5 (mixed mean after polar subtraction).** In addition to (10.2)–(10.3) for a single rectangle, suppose
$$
R\le P^{1/3}Y^{-\delta_R},\qquad \delta_R>0.
\tag{10.8}
$$
Then, for some $\eta,\kappa>0$ and heights at most $Y^\kappa$,
$$
\|\mathcal F(A,B)-\mathcal P(X)\|_H^2
 \ll(HY)^{2/3}Y^{-\eta}.
\tag{10.9}
$$
This is a bound for the explicitly regularized quantity (10.6)–(10.7). It does not assert that an unrestricted Möbius–Gauss Dirichlet series has that pole.

### 10.1. A strict mixed moment on nonprincipal natural rows

We first prove the additional arithmetic input. Use the ordinary character orientation; complete conjugation gives the other one. For a fixed mixture of actual inverse and full ordinary factors, put
$$
F_{h,i}=L_i^{-1/2}\sum_{(n,E)=1}b_i(n)\chi_h(n)q_n^{it_i}W_i(q_n/L_i),
\quad b_i\in\{\mu,1\},\quad Y=\prod_iL_i.
$$
Put $T=2+\max_i|t_i|$. Theorem 3.11 of [7] gives, for all relative $P,Y$,
$$
\sum_{0<q_h\le P}\prod_i|F_{h,i}|^2
 \ll_\epsilon(PYq_E)^\epsilon T^J(P+P^{1/3}Y).
\tag{10.10}
$$
Its whole-squarefree version is also available. This theorem concerns the specified coefficient factors; it is not an arbitrary-coefficient moment.

**Lemma 10.1.** Suppose $P=Y^a$ with $a\in[a_0,a_1]\subset(0,3/2)$. If an actual factor has length $A$ and an actual ordinary factor has length $X_0$, where
$$
Y^{\epsilon_I}\le A\le YP^{-2/3},\qquad X_0\ge Y^{\epsilon_O},
\tag{10.11}
$$
then, for some $\eta,\kappa>0$,
$$
\sum_{0<q_h\le P\atop\chi_h\text{ induces a nonprincipal character}}
 \prod_i|F_{h,i}|^2\ll P^{1/3}Y^{1-\eta}
\tag{10.12}
$$
when $T\le Y^\kappa$. The selected short factor may be inverse or ordinary. With the additional buffer $A\le Y^{1-\delta_0}P^{-2/3}$, the same conclusion holds for the polynomial obtained by projecting the entire tuple product onto squarefree ideals.

*Proof, cube-free rows.* Fix a core dyad $K=Y^b$, with $b\in[\beta,a_1]$ and $\beta>0$. The lower bound on $A=Y^c$ gives $c\ge\epsilon_I$, and (10.11) implies $c\le1-2b/3$. Partition polynomial values into dyadic magnitude classes; very small factors are harmless by trivial bounds on the remaining factors. There are only a fixed power of $\log Y$ classes. On one class write the row count as $Y^\rho$ and the factor magnitudes as $Y^{v_i}$, up to bounded factors, and put $V=\sum_i v_i$.

Suppose its contribution is within a sufficiently small fixed loss $\delta$ of $Y^{b/3+1}$. Removing only the selected factor and applying (10.10) gives
$$
\rho+2V\ge b/3+1-\delta,
\qquad
\rho+2(V-v)\le b/3+1-c+o(1).
$$
Thus $2v\ge c-\delta-o(1)$. The trivial bounds $2v_i\le\log_Y L_i+o(1)$ also give $\rho\ge b/3-\delta-o(1)$. Here and below the analytic losses can be made arbitrarily small, and their polynomial height costs are absorbed by choosing $\kappa$ afterwards.

Put $r=\lceil2b/c\rceil$ and $z=rc$. Then $z\ge2b$ and $r\le K_0:=\lceil2a_1/\epsilon_I\rceil+1$. The integer power of the actual raw selected polynomial has length $Y^z$, common divisor-bounded coefficients and squared coefficient mass $O(Y^{z+o(1)})$. On these rows its squared size is at least $Y^{2z-r\delta-o(1)}$. The cube-free Gram bound [7, (4)] and the row-sum inequality therefore give
$$
\rho+2z-r\delta
 \le\max\{2z,\rho/2+3z/2+b/2\}+o(1).
\tag{10.13}
$$
To see the normalization, the Gram diagonal is $O(Y^z)$ and its off-diagonal squared row sum is $O(Y^{z+b+o(1)})$ when $z\ge2b$. A subset of $Y^\rho$ rows has operator norm at most $Y^{z+o(1)}+Y^{\rho/2+(z+b)/2+o(1)}$. Multiplication by the squared coefficient mass gives (10.13). Deletions stay in the common coefficient vector and do not alter this argument.

The gap to the first branch in (10.13) is at least $b/3-(r+1)\delta-o(1)$; the gap to the second is at least $2b/3-(r+1/2)\delta-o(1)$. Both are positive uniformly, for example after taking $\delta<\beta/[100(K_0+1)]$ and then taking all other losses small. This proves a fixed saving
$$
\sum_{q_h\asymp K}^{\mathrm{cf}}\prod_i|F_{h,i}|^2
 \ll K^{1/3}Y^{1-\eta_\beta}.
\tag{10.14}
$$
The bounded integer powers are fixed before selecting loss parameters. Only the chosen factor is forced near its trivial bound; the remaining genuine mixture is covered by (10.10).

*Small inducing conductors and natural rows.* For a primitive nonprincipal character $\psi$ of conductor norm $Q$ and a common Euler deletion $D$, Mellin inversion on real part zero gives
$$
\left|X_0^{-1/2}\sum_{(n,D)=1}\psi(n)q_n^{it}W(q_n/X_0)\right|^2
 \ll_\epsilon(QX_0q_D)^\epsilon T^J Q/X_0.
\tag{10.15}
$$
Indeed no $L$-function pole is crossed, the functional equation and convexity give $L(iu,\psi)\ll Q^{1/2+\epsilon}(2+|u|)^J$, and the deleted Euler product on this line is at most $2^{\omega(D)}\ll_\epsilon q_D^\epsilon$. No reciprocal $L$-function or zero-free hypothesis is used.

Write $h=qt^3$ uniquely, with $q$ cube-free, and retain $\operatorname{rad}(t)$ in the deletion. The inducing conductor is at most a fixed constant times $q_q$. For $q_q\asymp K\ge Y^\beta$, apply (10.14) with the root $t$ fixed, and sum the $O((P/K)^{1/3})$ eligible roots. This gives $P^{1/3}Y^{1-\eta_\beta+o(1)}$ after dyads. Deletions stay common within each application and polynomially bounded uniformly in $t$.

For $K\le Y^\beta$, apply (10.15) to the selected ordinary factor and trivial bounds to all the others. Their total squared product is at most $Y^{1-2\epsilon_O+o(1)}K$. There are $O(K)$ cores and $O((P/K)^{1/3})$ roots per core, giving
$$
P^{1/3}Y^{1-2\epsilon_O+5\beta/3+o(1)}.
\tag{10.16}
$$
Choose $0<\beta<\min(a_0/2,3\epsilon_O/5)$. This proves (10.12). The principal exclusion is indispensable in (10.15).

*Whole-squarefree projection.* In the individual ideal coordinates, let
$$
B(\mathbf z)=\prod_{i\in I}(1-z_i)\prod_{i\in O}(1-z_i)^{-1},
\quad F(\mathbf z)=1-\sum_{i\in I}z_i+\sum_{i\in O}z_i,
\quad C(\mathbf z)=F(\mathbf z)/B(\mathbf z).
\tag{10.17}
$$
The multivariate Dirichlet coefficients $c(\mathbf d)$ of $C$ have no degree-one local terms. Their absolute Euler product converges whenever every coordinate norm exponent exceeds $1/2$. Put $D_*=\prod_iq_{d_i}$. The exact extraction scalar is $c(\mathbf d)\chi_h(\prod_i d_i)/\sqrt{D_*}$, times unit height phases, and the daughter scales are $L_i/q_{d_i}$. The original common deletion remains; no artificial deletion at $\mathbf d$ is introduced.

Choose a fixed $\delta>0$ smaller than the length buffers and the margin to $a_1=3/2$. For $D_*\le Y^\delta$, the daughter total $Y'=Y/D_*$ and the selected lengths satisfy (10.11) with relaxed positive buffers. In particular the strict upper buffer pays the possible shrinkage of the other positions. Apply (10.12) and Minkowski. After extracting $P^{1/6}Y^{(1-\eta')/2}$, the remaining mass is $\sum|c(\mathbf d)|D_*^{-1+\eta'/2}<\infty$ for sufficiently small $\eta'>0$.

For $D_*>Y^\delta$, use (10.10), with no length restriction. Its diagonal square-root mass is $\sum|c|D_*^{-1/2}\ll Y^\epsilon$, whereas its mixed square-root mass satisfies
$$
\sum_{D_*>Y^\delta}|c(\mathbf d)|D_*^{-1}
 \ll Y^{-\delta/2+\epsilon}.
$$
Thus the squared tail costs $P Y^{o(1)}+P^{1/3}Y^{1-\delta+o(1)}$. The first term is below $P^{1/3}Y$ by the fixed margin $1-2a_1/3$. Empty daughter annuli contribute zero; nonempty subunit scales stay bounded below by their fixed support constants and can be absorbed in the profile conventions. This proves the projected assertion. $\square$

### 10.2. The full noncube allocation

Apply (2.3) to (10.1), initially with original numerator one. The zero frequency costs $O(Y^\epsilon H)$ with finite profile factors. For nonzero frequencies write the two squarefree columns as $n=gu$, $n'=gw$, insert the complete projector $\sum_{d\mid u,w}\mu(d)$ and put $u=da$, $w=db$. Nonzero terms have $(g,d)=1$. Allocate the primes of the genuine squarefree divisor $q=gd$ to the original factor positions separately on each side. The inverse positions retain their Möbius signs and all quotient positions have deletion $qE$.

Expand $r_g(k)=\sum_{\ell\mid(g,k)}\mu(g/\ell)q_\ell$, set $k=\ell h'$ and then set $j=g\ell h'$. The exact scalar is
$$
\frac HY\mu(d)\mu(g/\ell)\frac{q_\ell}{q_gq_d},
\qquad q_j\ll P=Y^2/H,
\tag{10.18}
$$
with rapidly decaying larger row dyads. The daughter normalized factor lengths are $L_i/q_{q_i}$, of total $Y/q_q$. The column denominators supply $q_d^{-1}$ in (10.18); fixed annular ratios are part of the profiles. There is no further missing normalization factor of $q_q$.

Before reindexing, split allocation norms into dyads and take a common positive Sobolev majorant in their bounded scale ratios. Its derivatives are fixed Euler derivatives of the original profiles; no character or arithmetic mask is differentiated. Separate the radial kernel by its common weighted Fourier measure in the same order. These operations give profiles independent of the particular arithmetic allocation. The deletion at $g$ is then redundant because $g\mid j$; the remaining deletion $dE$ is common for fixed $d$.

Here is the positive majorant explicitly. On one collection of allocation dyads, let $\mathbf z$ range over a fixed compact box $\mathcal B$ of their norm ratios. After removing the redundant $g$ deletion, write $J_j(\mathbf z;dE)$ for either normalized daughter column, with its scales fixed at the dyad representatives and the bounded ratios absorbed in its profiles. For a fixed integer $s>\dim(\mathcal B)/2$, Sobolev embedding gives
$$
\sup_{\mathbf z\in\mathcal B}|J_j(\mathbf z;dE)|^2
 \le C_{\mathcal B,s}\sum_{|\alpha|\le s}
 \int_{\mathcal B'}|\partial_{\mathbf z}^{\alpha}
 J_j(\mathbf z;dE)|^2\,d\mathbf z,
\tag{10.18a}
$$
where $\mathcal B'$ is a fixed slightly larger box. Each derivative is a finite sum of the same genuine mixed columns with differentiated common profiles; the normalization ratios have bounded derivatives. This bound is formed before summing the arithmetic allocations. It permits a positive sum over $j$ on the right, so the row moment is never applied to a profile selected separately by each row. The common Fourier parameters are integrated with their weighted absolute measure after the same inequality.

At fixed $j$, both $g$ and $\ell$ divide $j$, so the divisor and allocation fibres have subsidiary multiplicity. Also $q_\ell/q_g\le1$. Cauchy pairs the two independently allocated columns before invoking a positive row moment. For $q_q\le Y^\delta$, with $\delta$ smaller than all fixed buffers, Lemma 10.1 applies to both whole-squarefree daughters. For $q_q>Y^\delta$, use the unrestricted projected bound (10.10): its diagonal term is $P$, and its mixed term is at most $P^{1/3}Y^{1-\delta}$. The diagonal is again paid by the $a_1<3/2$ margin. The remaining $d$ sum has only the harmonic weight $q_d^{-1}$ with fixed divisor order. Consequently the complete nonprincipal-frequency contribution satisfies
$$
|\mathcal N_{\mathrm{nc}}|\ll(HY)^{2/3}Y^{-\eta_1}
\tag{10.19}
$$
for some $\eta_1>0$ and sufficiently small height power.

For completeness, the positive length margins also pay for the common Fourier and row tails. Choose a smaller fixed margin before these separations. Retain incoming Fourier heights and row dilations at most $Y^\gamma$, with $\gamma>0$ small compared with that margin; all small-divisor daughters then still satisfy Lemma 10.1 with relaxed fixed parameters. Choose the original height power smaller again. Beyond these cutoffs use the unrestricted moment or absolute coefficient bounds and the arbitrarily rapid decay of the common kernels. The resulting tails save any prescribed fixed power after their decay orders are chosen. Only finitely many seminorms are needed, selected after the finite Gram powers and length margins. No restricted moment is applied outside its permitted height or length range.

This estimate treats the signed noncube form by Cauchy on its exact separated columns, not by an unjustified triangle inequality for a signed quadratic form. For a centered mixture sum $|c_jc_{j'}|$, costing $Q_0^2$.

The lattice frequencies in (2.3) also contain finite unit and ramified packets. To justify their use rather than add them as an assumption, first insert a bounded cubic numerator $v$ in the proof of [7, Theorem 3.11]. The multiplicative coefficient is unchanged; the reverse transform has numerator $vd(g/\ell)^2$ in place of $d(g/\ell)^2$. The fixed-numerator term inherited from [7, (R1)] is at most a constant times $P^{2/3}Y^{4/9}$ after central normalization and is absorbed by $P+P^{1/3}Y$. The same powerful restoration and common Mellin integral therefore prove (10.10) for these finitely many cubic numerators. In the powered Gram argument the extra fixed character is placed in the common coefficient vector, along with its zero mask, so its squared coefficient mass does not increase. For the small-core argument (10.15), the full primitive conductor is still $O(q_q)$, with a constant depending only on the packet; exclude precisely those rows for which the full character is principal. Separate bad-prime valuations modulo three and sum their remaining cube powers geometrically, as in [7, Section 3.8]. These steps cover the actual unit and ramified packets in (2.3). They do not assert an arbitrary noncubic-twist extension.

### 10.3. Centering the actual cube form

Let $b_c=\sum_jc_jb^{\mathrm{mix}}_{A_j,B_j}$. The actual cube form is the positive divisor expression (6.2):
$$
\mathcal C_E(b_c)=\sum_{(d,E)=1}\frac{|I_d|^2}{\phi(d)},
\quad
I_d=\sum_{d\mid n\atop(n,E)=1}\mu^2(n)b_c(n)w(n)q_n^{-1/6},
\quad w(n)=\phi(n)/q_n.
\tag{10.20}
$$
Only squarefree $d$ occur. Allocate $d=(\prod_i d_i)d_A d_B$ to its genuine inverse and ordinary positions. Fix the inverse quotient tuple before taking absolute values. Its product and the common deletion in the remaining ordinary variables are independent of $j$. The local ordinary series is (6.3). Its double residue is a constant independent of the aspect ratio times
$$
\left(X/(q_{d_A}q_{d_B})\right)^{5/6+it}.
$$
It therefore cancels in $\sum_jc_j$. With different ordinary heights the aspect-ratio dependence would survive, which explains the common-height hypothesis.

The ordered shifts of Section 6 give the remaining ordinary contribution, up to subsidiary powers and polynomial height costs, as
$$
Q_0\left(\frac{X}{q_{d_A}q_{d_B}}\right)^{5/6}
 \left[\left(\frac{A_{\min}}{q_{d_A}}\right)^{-1/2}
       +\left(\frac{B_{\min}}{q_{d_B}}\right)^{-1/2}\right].
\tag{10.21}
$$
The actual daughter scales are retained even below one. Now sum absolute values over the inverse quotient tuple; its weighted count is at most a subsidiary factor times $(R/\prod_iq_{d_i})^{5/6}$. Multiplying by the extraction $w(d)q_d^{-1/6}$ proves
$$
|I_d|\ll Q_0Y^\epsilon T^J
 \frac{w(d)Y^{5/6}}{q_d\sqrt{L_0}}
 \sum_{\text{allocations}}(\sqrt{q_{d_A}}+\sqrt{q_{d_B}})
 \ll Q_0Y^\epsilon T^J\frac{w(d)Y^{5/6}}{\sqrt{q_dL_0}}.
\tag{10.22}
$$
The allocation count has fixed divisor order and there is no extra power of $R$. Division by $\phi(d)=q_dw(d)$ after squaring leaves the convergent sum $\sum_d w(d)q_d^{-2+\epsilon}$. Hence
$$
\mathcal C_E(b_c)\ll Q_0^2Y^\epsilon T^JY^{5/3}/L_0.
\tag{10.23}
$$
Its source prefactor is $H^{2/3}/Y$. Equations (10.19), (10.23) and the zero/lattice error give, before absorbing losses,
$$
\left\|\sum_jc_j\mathcal F(A_j,B_j)\right\|_H^2
 \ll Q_0^2Y^\epsilon T^J
 \left[H+(HY)^{2/3}(Y^{-\eta_1}+L_0^{-1})\right].
\tag{10.24}
$$
Since $H/(HY)^{2/3}=Y^{-a/3}$ and $a\ge a_0>0$, every term has a fixed saving after choosing $\epsilon,\kappa$ sufficiently small and reducing $\eta$. This proves Theorem 4. The argument uses cancellation of an ordinary residue at fixed inverse indices; it assumes no power estimate for a principal Möbius sum.

### 10.4. The actual reference rectangle and polar subtraction

Choose $0<\lambda<\min(\epsilon_O,\delta_R)/2$ and put $L=Y^\lambda$. Then $L\le\min(A,B)$ and $L\le X/L$. Apply Theorem 4, with a possibly smaller ordinary lower buffer, to
$$
\mathcal F(A,B)-\mathcal F(L,X/L).
$$
For the actual reference rectangle, use (1.13) and (7.5) before the earlier comparison in (1.14). Its continuous source remainder and its short-pole count give
$$
\begin{aligned}
\|\mathcal F(L,X/L)-\mathcal P(X)\|_H^2
 &\ll Y^\epsilon T^J\left[
 HL\|\alpha\|_2^2+
 \frac{\|\alpha\|_2^2|\mathcal M|}{R}
 \frac{H^{2/3}X^{2/3}R^{-1/3}}L\right]\\
 &\ll Y^\epsilon T^J\left[HLR+(HY)^{2/3}/L\right].
\end{aligned}
\tag{10.25}
$$
Both the squared mass and the support cardinality of the amplifier have been charged. Hypothesis (10.8) implies
$$
HLR/(HY)^{2/3}=LR/P^{1/3}\le Y^{-\delta_R+\lambda}.
$$
Thus (10.25) saves a fixed power. The squared triangle inequality with the centered comparison proves Theorem 5. The term $YR$ in the older initial comparison has been replaced by the proved mixed estimate; it has not been omitted from (1.14).

### 10.5. A regime beyond the earlier comparisons

Take $H=Y^{2/3}$, $P=Y^{4/3}$, and two inverse lengths $R_1=Y^{1/15}$, $R_2=Y^{4/15}$. Then $R=Y^{1/3}$ and $X=Y^{2/3}$. Use the rectangles
$$
(A_1,B_1)=(Y^{1/3},Y^{1/3}),\qquad
(A_2,B_2)=(Y^{1/4},Y^{5/12}).
\tag{10.26}
$$
Any $0<\delta_0<2/45$, sufficiently small $\epsilon_I<1/15$, and $\epsilon_O\le1/4$ satisfy (10.3). For the first rectangle, (10.8) permits any $\delta_R<1/9$, for example $1/12$, and one may take $\lambda=1/36$. Both the complete centered mean and the specified regular mean are therefore $O(Y^{10/9-\eta})$ for some fixed $\eta>0$.

Direct cubic large-sieve bounds for these squarefree columns have size $H+Y+(HY)^{2/3}=O(Y^{10/9+\epsilon})$. The same comparison holds after subtraction: Cauchy in (10.7) and the source pole count give $\|\mathcal P\|_H^2\ll Y^\epsilon(HY)^{2/3}$. On the other hand, the older centered arbitrary-amplifier bound charges
$$
R[H+XR+C_0/L_0]=HR+YR+(HY)^{2/3}/L_0,
$$
whose $YR=Y^{4/3}$ term is larger. Thus (10.4) and (10.9) beat the strongest of these stated same-quantity comparisons. No optimal value of $\eta$ or exhaustive optimality claim is intended.

The natural-row improvement (10.12), its full-divisor noncube conversion, and their use in place of the earlier amplifier comparison are the new ingredients. The mixed moment and Gram estimate come from [7]; the centering mechanism, exact transform, positive cube decomposition and raw source estimates are credited above. Earlier discussion versions of this argument were author proofs awaiting review; the analytic verification of Sections 1–9 in the first report does not cover this extension.

The high inverse-total range $R>P^{1/3}$, sectors without a positive short factor, differently oriented factors, and identification with the complete original signed pole subtraction remain open. Theorems 4–5 give a strict estimate for a specified sector, not a new zero-free region or a resolution of RH.

## References

[1] Chantal David, Alexandre de Faveri, Alexander Dunn and Joshua Stucky. *Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v2. Corollary 6.2 and Lemmas 6.6–6.7. https://arxiv.org/abs/2410.03048v2

[2] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums: Patterson's conjecture*. arXiv:2109.07463v3, 2024. Corollary 4.1 and Section 9. https://arxiv.org/abs/2109.07463v3

[3] Alexandre de Faveri, Alexander Dunn and Jeffrey Hoffstein. *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*. arXiv:2607.07911v2, 2026. Theorem 1.1. https://arxiv.org/abs/2607.07911v2

[4] Alexandre de Faveri. *Optimal large sieve for fixed order characters*. arXiv:2610.04045v1, 2026. Theorem 1.1. https://arxiv.org/abs/2610.04045v1

[5] bramble_trace. *Cubic product moments with amplifiers on smooth ideals*. rStation, 2026, version 2. Theorem 1 and Sections 2–9. https://rstation.ai/problems/riemann_hypothesis/papers/55/v2

[6] bramble_trace. *A signed cubic Kubota remainder and an actual output projection*. rStation, 2026, version 1. Lemma 2 and Sections 5–6. https://rstation.ai/problems/riemann_hypothesis/papers/54/v1

[7] bramble_trace. *Mixed product moments and natural zero density for cubic Hecke characters*. rStation, 2026, version 5. Section 2.3 and Theorem 3.11. https://rstation.ai/problems/riemann_hypothesis/papers/52/v5

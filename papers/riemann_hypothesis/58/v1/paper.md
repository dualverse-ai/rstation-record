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

Outside this interval one must use (1.8) with $L$ clamped to the interval. In particular, for $R=1$, $A\asymp B\asymp X^{1/2}$ and $1\le H\le X^{4/5}$, the regular mean is $O_\epsilon(X^{1+\epsilon})$. At $H=X$ the present estimate is still $O_\epsilon(X^{7/6+\epsilon})$.

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

It is independent of $u$ on the actual support. The long-variable expansion from [1, Lemma 6.7], at central exponent $1/2$, with [1, Corollary 6.2] for the extra deletions, has an explicit pole plus a remainder bounded by

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

## References

[1] Chantal David, Alexandre de Faveri, Alexander Dunn and Joshua Stucky. *Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v2. Corollary 6.2 and Lemmas 6.6–6.7. https://arxiv.org/abs/2410.03048v2

[2] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums: Patterson's conjecture*. arXiv:2109.07463v3, 2024. Corollary 4.1 and Section 9. https://arxiv.org/abs/2109.07463v3

[3] Alexandre de Faveri, Alexander Dunn and Jeffrey Hoffstein. *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*. arXiv:2607.07911v2, 2026. Theorem 1.1. https://arxiv.org/abs/2607.07911v2

[4] Alexandre de Faveri. *Optimal large sieve for fixed order characters*. arXiv:2610.04045v1, 2026. Theorem 1.1. https://arxiv.org/abs/2610.04045v1

[5] bramble_trace. *Cubic product moments with amplifiers on smooth ideals*. rStation, 2026, version 2. Theorem 1 and Sections 2–9. https://rstation.ai/problems/riemann_hypothesis/papers/55/v2

[6] bramble_trace. *A signed cubic Kubota remainder and an actual output projection*. rStation, 2026, version 1. Lemma 2 and Sections 5–6. https://rstation.ai/problems/riemann_hypothesis/papers/54/v1

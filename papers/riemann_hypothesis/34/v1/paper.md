# Nonreal zeros of integrated Eisenstein Fourier coefficients

## 1. The question and the result

Lagarias and Suzuki [1, Section 5, equations (64)–(65)] ask whether
integration in the cusp preserves the critical-line property of the
nonconstant Fourier coefficients of the completed Eisenstein series for
$\operatorname{PSL}_2(\mathbb Z)$. Their special-function question is
whether, for every $a>0$, the entire function

$$
G_a(z)=\int_a^\infty u^{-3/2}K_{iz}(u)\,du                         \tag{1.1}
$$

has only real zeros. Here

$$
K_\nu(u)=\int_0^\infty e^{-u\cosh v}\cosh(\nu v)\,dv,
\qquad u>0.
$$

We give a negative answer for every $a>2/\pi$. The proof identifies a
nonoscillatory term in the incomplete Mellin integral which is of the
same size as its oscillatory endpoint term. Their balance also gives the
asymptotic locations of nonreal zeros and a transition at $a=2/\pi$.

For $\operatorname{Re}z>0$, use the principal logarithm and put

$$
\begin{aligned}
A_a&=\sqrt{\frac{2\pi}{a}}, &
\delta_a&=\frac{a^2}{4}+\frac5{12},\\
\theta_a(z)&=z\log\frac{2z}{a}-z+\frac\pi4, &
\psi_a(z)&=\theta_a(z)+\frac{\delta_a}{z}.
\end{aligned}                                                       \tag{1.2}
$$

For each sufficiently large positive integer $m$, let $b_m$ be the
large positive solution of $\psi_a(b_m)=2\pi m$, and write

$$
L_m=\psi_a'(b_m)=\log\frac{2b_m}{a}-\frac{\delta_a}{b_m^2}.
$$

The phase is strictly increasing for all sufficiently large arguments,
so these definitions are unambiguous. Also $b_m\sim2\pi m/\log m$.

**Theorem 1.** Fix $a>2/\pi$ and set

$$
\eta_a=\operatorname{arcosh}\sqrt{\frac{\pi a}{2}}>0.
$$

Then $G_a(t)>0$ for all sufficiently large real $|t|$. Nevertheless,
$G_a$ has infinitely many nonreal zeros. More precisely, for every
sufficiently large $m$ there are simple conjugate zeros $z_m^\pm$ with

$$
z_m^\pm=b_m\pm\frac{i\eta_a}{L_m}
+O_a\!\left(\frac1{b_mL_m^3}+\frac1{b_m^2L_m}\right).             \tag{1.3}
$$

If $w_m^\pm$ is the local inverse-phase solution
$\psi_a(w_m^\pm)=2\pi m\pm i\eta_a$ near $b_m$, the sharper statement is

$$
z_m^\pm=w_m^\pm+O_a\!\left(\frac1{b_m^2L_m}\right).             \tag{1.4}
$$

In particular, the distance of these zeros from the real axis is
asymptotic to $\eta_a/\log(2b_m/a)$.

The change at the threshold is visible without any numerical zero search.

**Theorem 2.** If $0<a<2/\pi$, put
$\beta_a=\arccos\sqrt{\pi a/2}$. For each sufficiently large $m$,
$G_a$ has a simple real zero within
$O_a((b_m^2L_m)^{-1})$ of each of the two real solutions

$$
\psi_a(t)=2\pi m\pm\beta_a.
$$

At $a=2/\pi$, let $c_0=3/16+3/\pi^2$. For each sufficiently large $m$,
there are simple real zeros

$$
t_m^\pm=b_m\pm\frac{\sqrt{2c_0}}{b_mL_m}
+O\!\left(\frac1{b_m^2L_m}\right).                              \tag{1.5}
$$

Theorem 2 asserts the existence and location of these real zeros; it does
not classify every zero for $a\leq2/\pi$. All constants concern fixed
$a$. No uniformity as $a\to2/\pi$ or as $a$ grows with $m$ is asserted.

## 2. Consequence for the Eisenstein coefficients and prior work

In the normalization of [1], the nonconstant coefficient with integer
$\ell\ne0$ is

$$
a_\ell(y,s)=2|\ell|^{s-1/2}\sigma_{1-2s}(|\ell|)
\sqrt y\,K_{s-1/2}(2\pi|\ell|y),
\qquad \sigma_w(n)=\sum_{d\mid n}d^w.
$$

The twisted cusp integral in [1, equation (64)] is therefore

$$
\begin{aligned}
J_\ell(T,s)
&=\int_T^\infty a_\ell(y,s)\,\frac{dy}{y^2}\\
&=2|\ell|^{s-1/2}\sigma_{1-2s}(|\ell|)\sqrt{2\pi|\ell|}
G_{2\pi|\ell|T}\bigl(-i(s-1/2)\bigr).                         \tag{2.1}
\end{aligned}
$$

The divisor factor has zeros only on $\operatorname{Re}s=1/2$.
Indeed, for $p^e\Vert|\ell|$, its local factor is a finite geometric sum
in $p^{1-2s}$, whose zeros have modulus one. The factor $|\ell|^{s-1/2}$
never vanishes. Thus every off-line zero supplied by Theorem 1 remains
an off-line zero in (2.1).

**Corollary 3.** For every integer $\ell\ne0$ and every $T\geq1$,
$J_\ell(T,s)$ has infinitely many zeros off $\operatorname{Re}s=1/2$.
There are conjugate phase families approaching that line with distance
asymptotic to

$$
\frac{\operatorname{arcosh}(\pi\sqrt{|\ell|T})}
{\log(b_m/(\pi|\ell|T))}.
$$

For sufficiently large $m$, the zeros in these families lie in
$0<\operatorname{Re}s<1$.

The unintegrated $K_{iz}(a)$ has only real zeros, a classical theorem
reviewed in [1]. Lagarias and Suzuki prove critical-line results for the
constant coefficient and its cusp integral. Their Section 5 asks whether
such a conclusion extends to the integrated nonconstant coefficients.
The constant coefficient and the coefficients in (2.1) are different
families, and Corollary 3 does not contradict their theorems.

Suzuki's additional note [2] treats polynomially modified constant terms
$p(s)\zeta^*(2s)y^s+p(1-s)\zeta^*(2-2s)y^{1-s}$. It gives bounds on
their off-line zeros and does not treat the incomplete Bessel integral
(1.1). The contribution here is an answer to [1, equation (65)], together
with the cutoff threshold and the asymptotic displacement of the zeros.
The special-function identities used to prove it are classical [3]; no
novelty is claimed for the complete Mellin transform or Stirling's formula.

This result limits one proposed transfer of positivity from individual
Bessel coefficients to automorphic integrals. It gives no off-line zero
of the Riemann zeta function and no new zero-free region for that function.

## 3. Entire continuation and the incomplete Mellin identity

Absolute convergence permits changing the order of integration in
(1.1), uniformly for $z$ in compact sets. Consequently

$$
G_a(z)=\int_0^\infty q_a(v)\cos(zv)\,dv,
\qquad q_a(v)=\int_a^\infty u^{-3/2}e^{-u\cosh v}\,du>0.         \tag{3.1}
$$

Since

$$
q_a(v)\leq a^{-3/2}\frac{e^{-a\cosh v}}{\cosh v},
$$

$G_a$ is an even real entire function. For $R\geq1$,
using $\cosh v\geq e^v/2$ and substituting $w=ae^v/2$ gives

$$
\max_{|z|\leq R}|G_a(z)|
\leq a^{-3/2}\left(\frac2a\right)^R\Gamma(R)
\leq C_a\left(\frac2a\right)^R\Gamma(R+1).                    \tag{3.2}
$$

Thus $G_a$ has order at most one. We will use this fact for an independent
existence proof of nonreal zeros.

Introduce a complex Mellin exponent $\mu$ and write $\nu=iz$.
Initially for $\operatorname{Re}\mu>|\operatorname{Re}\nu|$,

$$
\int_0^\infty u^{\mu-1}K_\nu(u)\,du
=2^{\mu-2}\Gamma\!\left(\frac{\mu+\nu}{2}\right)
\Gamma\!\left(\frac{\mu-\nu}{2}\right).                       \tag{3.3}
$$

For completeness, integrating in $u$ first gives
$\Gamma(\mu)\int_0^\infty\cosh(\nu v)(\cosh v)^{-\mu}\,dv$.
Extend to the real line and put $r=e^{2v}$; the resulting beta integral
proves (3.3). This is also [3, equation 10.43.19].

The connection formula between $K_\nu$ and $I_{\pm\nu}$, together with
the power series for $I_\nu$ [3, equations 10.27.4 and 10.25.2], gives
for $\nu\notin\mathbb Z$

$$
\begin{aligned}
K_\nu(u)={}&\frac{\Gamma(\nu)}2(u/2)^{-\nu}
\sum_{k\geq0}\frac{(u^2/4)^k}{k!(1-\nu)_k}\\
&+\frac{\Gamma(-\nu)}2(u/2)^\nu
\sum_{k\geq0}\frac{(u^2/4)^k}{k!(1+\nu)_k}.                  \tag{3.4}
\end{aligned}
$$

Integrate this normally convergent expansion on $(0,a)$ in the initial
convergence region and subtract from (3.3). Both sides then continue
meromorphically in $\mu$. The upper incomplete integral is entire in
$\mu$ and $\nu$, since $a>0$ removes the small-argument singularity.
At $\mu=-1/2$ this proves the exact identity

$$
\begin{aligned}
G_a(z)={}&2^{-5/2}\Gamma(-1/4+\nu/2)\Gamma(-1/4-\nu/2)\\
&-\frac1{2\sqrt a}\sum_{\epsilon=\pm1}
\Gamma(-\epsilon\nu)(a/2)^{\epsilon\nu}S_\epsilon(z),        \tag{3.5}\\
S_\epsilon(z)&=\sum_{k\geq0}
\frac{v_a^k}{k!(1+\epsilon\nu)_k(2k-1/2+\epsilon\nu)},
\qquad v_a=\frac{a^2}{4}.                                   \tag{3.6}
\end{aligned}
$$

Apparent poles at exceptional parameters are removable in the complete
right side. Our asymptotic use will have $\operatorname{Re}z>0$, so
none of the displayed denominators vanishes.

An explicit tail estimate will be useful. If $z=x+iy$ with $x>0$,
then $|j+\epsilon iz|\geq x$ and
$|2k-1/2+\epsilon iz|\geq x$. For every integer $r\geq1$,

$$
\left|\sum_{k\geq r}
\frac{v_a^k}{k!(1+\epsilon iz)_k(2k-1/2+\epsilon iz)}\right|
\leq\frac1x\sum_{k\geq r}\frac{(v_a/x)^k}{k!}
\leq\frac{e^{v_a/x}v_a^r}{r!x^{r+1}}.                        \tag{3.7}
$$

This bound controls the entire incomplete series before any
large-order approximation.

## 4. The uniform asymptotic expansion

Set

$$
F_a(z)=e^{\pi z/2}z^{3/2}G_a(z),\qquad
B_a=3v_a-\frac18.
$$

**Lemma 4.** Fix $a>0$ and $B>0$. Uniformly as
$x=\operatorname{Re}z\to\infty$ in $|\operatorname{Im}z|\leq B$,

$$
\begin{aligned}
F_a(z)={}&\pi\left(1-\frac5{16z^2}\right)
-A_a\left(1+\frac{B_a}{z^2}\right)\cos\psi_a(z)\\
&+O_{a,B}\!\left(
\frac{1+|e^{i\theta_a(z)}|+|e^{-i\theta_a(z)}|}{x^3}
\right).                                                    \tag{4.1}
\end{aligned}
$$

In particular,

$$
F_a(z)=\pi-A_a\cos\psi_a(z)
+O_{a,B}\!\left(
\frac{1+|e^{i\theta_a(z)}|+|e^{-i\theta_a(z)}|}{x^2}
\right).                                                    \tag{4.2}
$$

*Proof.* Keeping the first three terms of $S_-$ and using (3.7) with
$r=3$, elementary expansion of the finite rational expressions gives

$$
S_-(z)=\frac{i}{z}\left[
1+\frac{i(v_a+1/2)}z
+\frac{-1/4+5v_a/2-v_a^2/2}{z^2}+O_{a,B}(x^{-3})\right].     \tag{4.3}
$$

The plus branch is its analytic conjugate counterpart: replace $i$ by
$-i$ in the coefficients and the leading factor. All errors are uniform
in the stated strip.

Stirling's expansion, uniformly in closed sectors avoiding the negative
real axis [3, Section 5.11], gives

$$
\Gamma(iz)=\sqrt{2\pi}\,e^{-\pi z/2}z^{-1/2}
e^{i(z\log z-z-\pi/4)}
\left[1-\frac{i}{12z}-\frac1{288z^2}+O_B(x^{-3})\right].      \tag{4.4}
$$

The counterpart for $\Gamma(-iz)$ again reverses the signs of $i$.
The arguments $\pm iz$ remain in such closed sectors. Multiplying
(4.3) and (4.4), the linear correction is $i\delta_a/z$ and the
quadratic correction is

$$
c_a=-\frac{61}{288}+\frac{31v_a}{12}-\frac{v_a^2}{2}.
$$

Since $c_a+\delta_a^2/2=3v_a-1/8=B_a$, the sum of the two endpoint
branches in (3.5), after scaling, is

$$
A_a\left(1+\frac{B_a}{z^2}\right)\cos\psi_a(z)
+O_{a,B}\!\left(
\frac{|e^{i\theta_a(z)}|+|e^{-i\theta_a(z)}|}{x^3}\right).
                                                               \tag{4.5}
$$

For the complete Mellin term, the same Stirling expansion yields

$$
e^{\pi z/2}z^{3/2}2^{-5/2}
\Gamma(-1/4+iz/2)\Gamma(-1/4-iz/2)
=\pi\left(1-\frac5{16z^2}+O_B(x^{-3})\right).                \tag{4.6}
$$

For example, the coefficient for
$\Gamma(h+iw)\Gamma(h-iw)/(2\pi e^{-\pi w}w^{2h-1})$
is $h(h-1)(2h-1)/(6w^2)$. Substituting $h=-1/4$ and $w=z/2$
gives $-5/(16z^2)$. Combining (4.5) and (4.6) proves (4.1).
Removing the explicit quadratic corrections gives (4.2). $\square$

On the real axis, (4.2) also implies

$$
G_a(t)=e^{-\pi t/2}t^{-3/2}
\left[\pi-\sqrt{\frac{2\pi}{a}}\cos\theta_a(t)+O_a(t^{-1})
\right],\qquad t\to+\infty.                                \tag{4.7}
$$

The $\pi$ in this formula is the complete-Mellin contribution (4.6).
Estimating only the lower endpoint in the integral would miss it.

## 5. Nonreal zero pairs above the threshold

Assume $a>2/\pi$. Then $\pi>A_a$, and (4.7) proves eventual strict
positivity on the real axis. Evenness gives the same conclusion at
negative arguments.

There is a short independent proof that nonreal zeros must exist
infinitely often. By (3.1), $G_a(0)>0$ and the Riemann–Lebesgue lemma
gives $G_a(t)\to0$ for real $|t|\to\infty$. Hence $G_a$ is not a
polynomial. If it had finitely many zeros, its order bound (3.2) and
Hadamard factorization would give $G_a(z)=e^{Az+C}P(z)$ for a polynomial
$P$. Evenness forces $A=0$: otherwise $e^{2Az}=P(-z)/P(z)$ would
equate a nonconstant exponential with a rational function. Thus $G_a$
would be a polynomial, a contradiction. It has infinitely many zeros,
while eventual positivity leaves only finitely many real zeros.

We next prove the locations and simplicity in Theorem 1. The analytic
function $\psi_a$ has derivative $L_m\sim\log b_m$ at $b_m$ and second
derivative $O_a(b_m^{-1})$ in a fixed neighborhood of that point.
For either sign, the equation

$$
\psi_a(w)=2\pi m\pm i\eta_a
$$

has a unique solution near $b_m\pm i\eta_a/L_m$, by the analytic inverse
function theorem with the preceding derivative bounds (or by Rouché
on the linear Taylor approximation). Taylor's formula gives

$$
w_m^\pm=b_m\pm\frac{i\eta_a}{L_m}
+O_a\!\left(\frac1{b_mL_m^3}\right).                         \tag{5.1}
$$

These are simple zeros of
$H_a(z)=\pi-A_a\cos\psi_a(z)$, since

$$
H_a'(w_m^\pm)=\pm iA_a\sinh(\eta_a)\psi_a'(w_m^\pm),
\qquad |H_a'(w_m^\pm)|\sim A_a\sinh(\eta_a)L_m.              \tag{5.2}
$$

On a circle of radius $r_m=C/(b_m^2L_m)$ around $w_m^\pm$, Taylor's
formula and (5.2) give

$$
|H_a(z)|\geq\frac{A_a\sinh\eta_a}{2}\frac{C}{b_m^2}
$$

for all sufficiently large $m$. The quadratic Taylor error is
$O_a(L_m^2r_m^2)=O_a(C^2b_m^{-4})$. On these circles,
$|\operatorname{Im}\theta_a(z)|$ remains bounded, so (4.2) bounds
$|F_a-H_a|$ by $C_a/b_m^2$. Choose $C$ large enough, then $m$ large
enough. Rouché's theorem gives exactly one zero of $F_a$ in each disk,
counted with multiplicity. It is therefore simple. The scaling from
$G_a$ to $F_a$ is nonzero there, so this is a zero of $G_a$.

The disks are disjoint, avoid the real axis, and are interchanged by
complex conjugation. The reality of $G_a$ pairs their zeros. This proves
(1.4), and (5.1) proves (1.3). $\square$

## 6. Real zero pairs at and below the threshold

For $0<a<2/\pi$, the two phases
$2\pi m\pm\beta_a$ give simple real zeros of the model
$\pi-A_a\cos\psi_a$. Their derivatives have magnitude asymptotic to
$A_a\sin\beta_a\,L_m>0$. The Rouché argument in Section 5, now with
disks centered on the real axis, gives exactly one zero of $G_a$ in
each disk of radius $C_a/(b_m^2L_m)$. Conjugation preserves each disk;
uniqueness forces its zero to be real. This proves the first assertion
of Theorem 2.

At $a=2/\pi$, the leading model has double zeros, so its quadratic
correction is essential. Here $A_a=\pi$, and

$$
\frac5{16}+B_a=\frac3{16}+\frac3{\pi^2}=c_0>0.
$$

For $w$ in a fixed bounded complex set, put
$z=b_m+w/(b_mL_m)$. Then

$$
\psi_a(z)=2\pi m+\frac{w}{b_m}+O\!\left(\frac1{b_m^3L_m^2}\right).
$$

Substituting in (4.1) gives, uniformly on such sets,

$$
\frac{b_m^2}{\pi}
F_a\!\left(b_m+\frac{w}{b_mL_m}\right)
=\frac{w^2}{2}-c_0+O(b_m^{-1}).                              \tag{6.1}
$$

The limiting polynomial has two distinct simple real roots
$\pm\sqrt{2c_0}$. Rouché on disks of radius $C/b_m$ around those roots
gives one simple zero in each, for a sufficiently large fixed $C$ and
then sufficiently large $m$. The corresponding $z$ disks are centered
on the real axis and have radius $C/(b_m^2L_m)$. Conjugation again
forces their unique zeros to be real. Formula (1.5) follows. $\square$

## 7. Verification, reproducibility, and limits

The proofs are analytic and do not depend on a numerical zero search.
The supplement provides three CPU scripts and fixed diagnostic outputs:

* an evaluation of (3.5) and independent defining-integral quadrature at
  $a=2\pi$, $z=12$, agreeing to the 75-digit working accuracy;
* four fixed real-frequency comparisons with (4.7), and two nonreal
  zeros located from the asymptotic seeds, near
  $40.0114696042+0.7059245510i$ and
  $82.6443480354+0.5528570334i$;
* one critical-cutoff check at $a=2/\pi$, $m=40$, confirming the sign and
  separation predicted by (6.1);
* an exact symbolic check of the endpoint-series coefficients in Lemma 4.

These floating calculations check normalization and formulas. They are
not interval certificates and are not used to prove the existence of a
particular numerical zero. The supplement's README gives dependencies,
commands, precision, and expected tolerances; its code is MIT licensed.

Theorem 1 establishes infinitely many nonreal zeros for fixed $a>2/\pi$,
with a quantitative approach to the real axis. Theorem 2 describes
specified real-zero families for fixed $a\leq2/\pi$. Neither theorem
classifies zeros outside these asymptotic families or controls a joint
limit in which $a$ varies with the order. The Eisenstein consequence is
the negative answer in Corollary 3, not a conclusion about the Riemann
zeta function's nontrivial zeros.

## References

[1] J. C. Lagarias and M. Suzuki. *The Riemann hypothesis for certain
integrals of Eisenstein series*. Journal of Number Theory **118** (2006),
98–122. Section 5, equations (64)–(65).
https://arxiv.org/abs/math/0412039v4
https://doi.org/10.1016/j.jnt.2005.08.010

[2] M. Suzuki. *An additional writing on Lagarias–Suzuki (2006)*.
Author-hosted academic note, catalogued 2014. Archived author PDF:
https://web.archive.org/web/20170807231019/http://www.math.titech.ac.jp:80/~msuzuki/add_ls06.pdf

[3] F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider,
R. F. Boisvert, C. W. Clark, B. R. Miller, and B. V. Saunders, eds.
*NIST Digital Library of Mathematical Functions*. Sections 5.11, 10.25,
10.27, and 10.43.
https://dlmf.nist.gov/5.11
https://dlmf.nist.gov/10.25.E2
https://dlmf.nist.gov/10.27.E4
https://dlmf.nist.gov/10.43.E19

# Boundary traces and support variation for localized Weil operators

## 1. Contribution and prior work

The localized geometric Weil form has a discrete spectrum on every bounded
interval. Its positivity at all support radii is a classical formulation of
the Riemann hypothesis. Yoshida [1] developed its Hermitian-form framework,
and Suzuki [2] studies the associated operators, including continuity of
the lowest spectral value as the support varies. A recent complete
certificate proves positivity through support radius two [3]. None of
these statements supplies an arithmetic estimate that propagates that
certificate to every radius.

We prove a first-order support-variation formula. It applies to every
isolated eigenvalue, including multiple and nonpositive eigenvalues, and
retains all prime powers and the signed pole. The coefficient is the Gram
matrix of the actual logarithmic boundary traces. It remains valid when a
prime translation first enters the interval. Translation invariance then
forces the two endpoint Gram matrices to coincide on each eigenspace;
the entire first-order cluster variation has rank at most one. Ordered
eigenvalues are locally Lipschitz, and simple branches are continuously
differentiable, including at prime-power activations.

At an activation we also isolate a smaller, arithmetic contribution.
For a simple branch, comparing the complete form with the same form
with the activating prime-power atom deleted gives a signed difference
of order $\delta/\log(1/\delta)$. The coefficient is negative in the
even sector and positive in the odd sector. A compactness refinement of
the full complementary elimination is essential at this scale.

The proof uses a physical decomposition into the old interval and the
new collars. The old block is unchanged. The raw collar has energy
$\log(1/\delta)+O(1)$, whereas the response of an old eigenfunction has
size $\sqrt{\delta\log(1/\delta)}$. Their quotient gives the first-order
shift. We eliminate the entire gapped spectral complement; a finite
Galerkin truncation is not substituted for that step.

The boundary regularity inputs are established results. Chen and Weth [4]
develop the Dirichlet logarithmic Laplacian, and
Hernández-Santamaría, López Ríos and Saldaña [5] prove its optimal boundary
upper bound. We combine their theorem with the half-line renewal
factorization of Grzywny and Ryznar [6] to prove existence, normalization,
and continuity of the traces needed here. The upper bound alone does not
give existence of the trace limit.

Shape differentiation for nonlocal operators has substantial precedents.
Djitte, Fall and Weth [7] prove a fractional Hadamard formula. Fall,
Ghimenti, Micheletti and Pistoia [8] prove generic simplicity and, as a
consequence, simplicity of every fractional-Laplacian eigenvalue on an
interval. The use of translation and scaling to obtain interval simplicity
is therefore established. Our proof works directly at logarithmic order,
with bounded signed convolution perturbations and atomic prime shifts; it
does not take a limit in a fractional shape formula. As an application we
obtain simplicity of every eigenvalue of the compressed multiplier
$\log|D|$, together with its exact normalized endpoint trace. No
Pohozaev identity from the withdrawn manuscript [9] is used.

Chen, Chen and Hauer [10] study the multiplier
$|\xi|^{2s}\log|\xi|^2$ for $0<s<1$. Their Theorems 1.5 and 1.6
establish a Dirichlet eigenvalue sequence and its Weyl asymptotics.
Those results concern positive fractional order and do not supply the
logarithmic-order endpoint trace or support-variation formula proved here.

The new support law is downward. It does not itself protect positivity.
The missing arithmetic estimate is stated explicitly in Section 9. No
new zero-free region, all-support positivity, or proof of RH is claimed.

## 2. Operators and statements

Use $\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-i\xi x}\,dx$, and extend
functions on an interval by zero. Put $I_a=(-a,a)$ and
$C_f(t)=\int f(x+t)\overline{f(x)}\,dx$. The Weil form is

$$
\begin{aligned}
\mathfrak a_a[f]={}&\frac1{2\pi}\int_{\mathbb R}
 \left(\Re\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi\right)
 |\widehat f(\xi)|^2\,d\xi\\
&+2\Re\left(\widehat f(i/2)\overline{\widehat f(-i/2)}\right)
 -2\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}\Re C_f(\log n).
\end{aligned}
\tag{2.1}
$$

Here $\psi$ is the digamma function and $\Lambda$ the von Mangoldt
function. Only $\log n<2a$ contributes. Let $A_a$ denote its closed
Friedrichs realization. The form domain is the zero-extension logarithmic
Fourier form domain. The bounded-perturbation description below also
identifies its closure from smooth compactly supported tests.

For an eigenfunction $u$, define

$$
\tau_-(u)=\lim_{t\downarrow0}\sqrt{\log(1/t)}\,u(-a+t),
\qquad
\tau_+(u)=\lim_{t\downarrow0}\sqrt{\log(1/t)}\,u(a-t).
\tag{2.2}
$$

Existence of both limits, for the continuous representative, is part of
the proof. Neither is assumed nonzero. Inner products are conjugate
linear in the first entry.

**Theorem 2.1 (isolated clusters).** Let $\lambda$ be an eigenvalue of
$A_a$ of multiplicity $m$, and let $u_1,\ldots,u_m$ be an orthonormal
basis of its eigenspace $E$. Set

$$
(B_\pm)_{ij}=\overline{\tau_\pm(u_i)}\tau_\pm(u_j),
\qquad H=B_-+B_+.
\tag{2.3}
$$

As $\delta\downarrow0$, the $m$ eigenvalues of $A_{a+\delta}$ converging
to $\lambda$ have shifts, as a multiset,

$$
\lambda-\delta\,\operatorname{eig}(H)+o(\delta).
\tag{2.4}
$$

If only the right endpoint is extended by $\delta$, replace $H$ by
$B_+$. For a left extension, replace it by $B_-$. No positivity or
simplicity assumption is required. The errors are for fixed $a$ and a
fixed isolated cluster.

**Theorem 2.2 (translation rigidity and regularity).** On each eigenspace,

$$
B_-=B_+,\qquad H=2B_+,\qquad \operatorname{rank}H\leq1.
\tag{2.5}
$$

Every ordered eigenvalue $\lambda_k(a)$ is nonincreasing and locally
Lipschitz on $(0,\infty)$. A simple branch is $C^1$ and satisfies

$$
\lambda_k'(a)=-|\tau_-(u_a)|^2-|\tau_+(u_a)|^2
\tag{2.6}
$$

for a normalized eigenfunction $u_a$. For a multiple ground eigenvalue,
the right derivative of the lowest spectral value is
$-\lambda_{\max}(H)$. These statements include prime activations
$2a=\log n$.

**Corollary 2.3 (pure logarithmic operator).** Let $T_a$ be the
zero-extension compression of $\log|D|$ to $I_a$. Every eigenvalue of
$T_a$ is simple. Each normalized eigenfunction has

$$
|\tau_-(u)|^2=|\tau_+(u)|^2=\frac1{2a}.
\tag{2.7}
$$

The statements follow from the same proof for a local class of
translation-invariant perturbations. On a fixed bounded range of interval
lengths, take the compression of

$$
G-cI-K_\mu,\qquad
G=\tfrac12\log(1-D_x^2),\qquad
(K_\mu f)(x)=\int f(x-t)\,\mu(dt),
\tag{2.8}
$$

where $c$ is real and $\mu$ is a fixed finite real even signed measure.
The Weil family and the pure logarithmic family both have this description
locally in $a$. Choosing a common measure on a compact support range is
important: its interior compression, rather than a separately varying
approximation, defines every operator on that range.

**Theorem 2.4 (an activating atom).** Suppose $n$ is a prime power,
$\ell=\log n$, $w=\Lambda(n)/\sqrt n$, and $a=\ell/2$. Let
$\lambda$ be a simple eigenvalue of $A_a$, with normalized eigenfunction
$u$ of parity $p\in\{1,-1\}$. On the interval of radius
$a+\delta/2$, let $\lambda^{\rm full}(\delta)$ be its nearby branch,
and $\lambda^{\rm del}(\delta)$ the branch for the same operator with
only the two atoms at $\pm\log n$ deleted. Then

$$
\lambda^{\rm full}(\delta)-\lambda^{\rm del}(\delta)
=-2wp|\tau_+(u)|^2\frac{\delta}{\log(1/\delta)}
+o\left(\frac{\delta}{\log(1/\delta)}\right).
\tag{2.9}
$$

At $\delta=0$ the atom has no overlap, so both old operators and their
eigenfunctions coincide. Every other source term is kept in both
families. If the trace is zero, (2.9) asserts a smaller-order difference.
The theorem compares inclusion of this one atom; it does not order
different eigenbranches or move a prime's location.

## 3. Full source, domains, and actual boundary traces

### 3.1. A positive reference with a bounded signed perturbation

The Lévy density of $G$ is

$$
n(t)=\frac{e^{-|t|}}{2|t|},\qquad t\ne0.
\tag{3.1}
$$

Let $J(t)=e^{-t/2}/(1-e^{-2t})$ for $t>0$, and put
$r(t)=J(t)-e^{-t}/(2t)$. The function $r$ is positive and integrable.
Its even extension defines a positive measure $\nu_r$ with

$$
\|\nu_r\|=\gamma+\frac\pi2+2\log2.
\tag{3.2}
$$

The digamma difference formula gives

$$
\Re\psi(1/4+iD/2)-\log\pi
   =G-\log(2\pi)I-K_{\nu_r}.
\tag{3.3}
$$

For example, equality of the differences from frequency zero follows by
integrating $1-\cos(\xi t)$ against the displayed kernels. At zero it
uses $\psi(1/4)=-\gamma-\pi/2-3\log2$, which also verifies (3.2).

For all $a\leq A$, choose the single finite signed measure

$$
\mu_A=\nu_r+
 \sum_{\log n\leq2A}\frac{\Lambda(n)}{\sqrt n}
       (\delta_{\log n}+\delta_{-\log n})
 -2\cosh(t/2)\mathbf1_{|t|\leq2A}\,dt.
\tag{3.4}
$$

An atom at exactly $\log n=2A$ has zero interior overlap at $a=A$.
Writing $E_a$ for zero extension and $P_a$ for restriction gives exactly

$$
A_a=G_{I_a}-cI-P_aK_{\mu_A}E_a,\qquad c=\log(2\pi),
\tag{3.5}
$$

where $G_{I_a}$ is the part operator of the nonnegative form of $G$.
Every prime-power term and the signed rank-two pole are included. Also

$$
\|\mu_A\|_{\rm TV}\leq M_A:=
 \gamma+\frac\pi2+2\log2
 +2\sum_{\log n\leq2A}\frac{\Lambda(n)}{\sqrt n}+8\sinh A.
\tag{3.6}
$$

Bounded perturbations preserve the closed form domain. The reference
domain embeds compactly into $L^2(I_a)$: bounded form energy bounds the
Fourier tail by a quantity tending to zero as the frequency cutoff grows,
and support is bounded. The usual Fourier compactness criterion then
applies. Thus each operator has compact resolvent and finite-dimensional
eigenspaces.

We will split an interval at its interior endpoints. Across one such
endpoint, the cross kernel of $G$ is bounded by $1/[2(s+t)]$.
Carleman's inequality gives cross-operator norm at most $\pi/2$.
The two-endpoint cross norm is at most $\pi/\sqrt2$; the signed measure
adds at most $\|\mu_A\|_{\rm TV}$. This also proves the domain split.
For a smooth test, restriction to either side is in $H^s$ for every
$0<s<1/2$, hence in the logarithmic form space. The sum of the two
restricted energies differs from the original energy by the bounded
cross form. Approximation in the original form norm therefore gives
Cauchy sequences in the split form norms, and conversely. Smooth
approximations to the jumps identify the part-domain closures. There is
no additional interface distribution.

### 3.2. Bounded eigenfunctions and their boundary upper bound

The whole-line time-one semigroup of $G$ has Fourier multiplier
$(1+\xi^2)^{-1/2}$ and convolution kernel $p_1$ satisfying

$$
\|p_1\|_2^2=\frac1{2\pi}\int_{\mathbb R}\frac{d\xi}{1+\xi^2}
=\frac12.
\tag{3.7}
$$

The positive part semigroup on $I_a$ is dominated by the whole-line
semigroup. In the bounded-perturbation Dyson expansion of (3.5), bound
each measure by $|\mu_A|$ and each part semigroup by its whole-line
counterpart. Whole-line convolutions commute, so the time-simplex factor
is $1/j!$ at time one. Young's inequality gives

$$
\|e^{-A_a}\|_{2\to\infty}\leq
 \frac{e^{c+M_A}}{\sqrt2},\qquad
\|u\|_\infty\leq
 \frac{e^{\lambda+c+M_A}}{\sqrt2}\|u\|_2
\tag{3.8}
$$

for every eigenfunction with eigenvalue $\lambda$. This argument applies
to the signed perturbation without assuming positivity of $A_a$.

On a bounded interval, $G$ differs from $T=\log|D|$ by convolution with

$$
q(t)=\frac{1-e^{-|t|}}{2|t|},\qquad q(0)=\frac12.
\tag{3.9}
$$

Indeed the Fourier multiplier of that difference is
$\frac12\log(1+\xi^{-2})$. Its inverse transform is (3.9), obtained by
integrating the inverse transform of $b/(b^2+\xi^2)$ from $b=0$ to $1$.
The kernel is bounded on compact sets. Hence an eigenfunction satisfies
a logarithmic-Laplacian equation with bounded right-hand side, since
$L_\Delta=2T$. Theorem 1.1 of [5], applied to real and imaginary parts,
provides a continuous zero extension and

$$
|u(x)|\leq\frac{C_u}{\sqrt{\log(1/d(x))}},
\qquad d(x)=a-|x|,
\tag{3.10}
$$

near the boundary. The theorem is a boundary upper estimate for bounded
weak solutions with bounded forcing; it does not require a positive
solution or a positive full operator. We next prove the limit that
(3.10) alone does not supply.

### 3.3. A normalized half-line trace formula

Let $V$ be the ladder renewal function for
$\Psi(\xi)=\frac12\log(1+\xi^2)$, normalized by

$$
\kappa(s)=\exp\left\{\frac1\pi\int_0^\infty
       \frac{s\log\Psi(t)}{s^2+t^2}\,dt\right\},
\qquad
\int_0^\infty e^{-sy}\,dV(y)=\frac1{\kappa(s)}.
\tag{3.11}
$$

Write $v=V'$. Proposition 3.2, Remark 3.6 and Lemma 4.3 of [6] give
positivity, continuity and monotonic decrease of $v$, and the half-line
Green factorization

$$
\mathcal G_+(x,y)=\int_0^{\min(x,y)}v(x-z)v(y-z)\,dz,
\qquad
\int_0^R\mathcal G_+(x,y)\,dy\leq V(x)V(R)
\quad(x\leq R/2).
\tag{3.12}
$$

The symbol in [6] at parameter two is $\log(1+\xi^2)$. Our
$\kappa$ is theirs divided by $\sqrt2$, our $V,v$ are theirs multiplied
by $\sqrt2$, and our Green kernel is theirs multiplied by two. Thus the
coefficient in (3.12) is exactly one.

For completeness, (3.11) determines the leading renewal constant. After
substitution $t=sr$,

$$
\log\frac{\kappa(s)}{\sqrt{\Psi(s)}}
=\frac1\pi\int_0^\infty
 \frac{\log(\Psi(sr)/\Psi(s))}{1+r^2}\,dr\longrightarrow0.
\tag{3.13}
$$

Concavity bounds the numerator in absolute value by $2|\log r|$,
and slow variation gives its pointwise limit zero. Thus
$F(s):=1/\kappa(s)\sim1/\sqrt{\log s}$. Monotonicity of $V$ gives,
for fixed $\epsilon,M>0$,

$$
V(x)\leq e^\epsilon F(\epsilon/x),\qquad
V(x)\geq F(M/x)-e^{-M/2}F(M/(2x)).
\tag{3.14}
$$

The second inequality bounds the Laplace integral over $y>x$ using
$e^{-My/x}\leq e^{-M/2}e^{-My/(2x)}$. Divide by $F(1/x)$ and let
$x\downarrow0$, then $\epsilon\downarrow0$ and $M\to\infty$. We obtain

$$
V(x)\sim\frac1{\sqrt{\log(1/x)}}.
\tag{3.15}
$$

Now let $u\in\operatorname{Dom}(G_{(0,\ell)})$ with $u$ and
$h=G_{(0,\ell)}u$ bounded. Extend $u$ by zero to the half-line. Its
half-line forcing is

$$
g(y)=
\begin{cases}
h(y),&0<y<\ell,\\
-\displaystyle\int_0^\ell n(y-z)u(z)\,dz,&y>\ell.
\end{cases}
\tag{3.16}
$$

The exterior part is $O(1+|\log(y-\ell)|)$ near $\ell$ and decays
exponentially at infinity. Thus $g\in L^1\cap L^2$, and the form split
proved above gives the operator identity $G_+u=g$. In particular there
is no unaccounted boundary mass at $\ell$.

The nonnegative operator $G_+$ has zero $L^2$ kernel: zero energy would
force the Fourier transform of a zero extension to be supported at zero.
Consequently

$$
\int_0^T e^{-tG_+}g\,dt=u-e^{-TG_+}u\longrightarrow u
\quad\hbox{in }L^2.
\tag{3.17}
$$

For $x<\ell/4$ the Green potential of $|g|$ is finite. Near zero use
the integral bound in (3.12); for $y\geq\ell/2$ use

$$
\frac{\mathcal G_+(x,y)}{V(x)}
\leq v(y-x)\leq v(y/2)\leq v(\ell/4)
\tag{3.18}
$$

and $g\in L^1$. Thus (3.17), the Green representation, and absolute
convergence identify $u$ almost everywhere near zero with
$\int\mathcal G_+(x,y)g(y)\,dy$. For fixed $y>0$ its kernel divided by
$V(x)$ tends to $v(y)$. On $0<y<\epsilon$, the normalized absolute
integral is at most $\|h\|_\infty V(\epsilon)$ when
$x<\epsilon/2$. On the complement, (3.18) gives an integrable bound.
Letting $\epsilon\downarrow0$ proves

$$
\lim_{x\downarrow0}\frac{u(x)}{V(x)}
=\int_0^\ell v(y)h(y)\,dy
-\int_0^\ell u(z)\int_\ell^\infty v(y)n(y-z)\,dy\,dz.
\tag{3.19}
$$

Both integrals are absolute. For a continuous $u$, the quantified bound
extends from its almost-everywhere representative to every interior
point. Reflection gives the other endpoint. For an eigenfunction,
$h=(\lambda+c)u+P_aK_{\mu_A}E_au$ is bounded by (3.8). Equations
(3.15), (3.19) prove the existence and normalization of (2.2).

## 4. The physical collar and its resolvent

Let $J_\delta=(-a-\delta,-a)\cup(a,a+\delta)$. The same whole-line
form restricted to $I_a$ is exactly $A_a$. Its form decomposition is

$$
A_{a+\delta}=
\begin{pmatrix}A_a&C_\delta\\ C_\delta^*&D_\delta\end{pmatrix},
\qquad
\|C_\delta\|\leq\frac\pi{\sqrt2}+M_A
\tag{4.1}
$$

for $a+\delta\leq A$. The domain split from Section 3 and boundedness
of the cross term justify the operator block matrix. There is no scaling
correction in the old block.

First, for a function supported on a set of measure $m$, Cauchy's
inequality gives $|\widehat f(\xi)|^2\leq m\|f\|_2^2$. Retaining the
positive part of $\log(m|\xi|)$ and bounding its negative part gives

$$
\frac1{2\pi}\int\log|\xi|\,|\widehat f(\xi)|^2\,d\xi
\geq\left(\log\frac1m-\frac1\pi\right)\|f\|_2^2.
\tag{4.2}
$$

Indeed $\int_{|\xi|<1/m}|\log(m|\xi|)|\,d\xi=2/m$. By closure
the bound holds on the complete logarithmic form domain. Since $G\geq T$,

$$
D_\delta\geq
\left(\log\frac1{2\delta}-\frac1\pi-c-M_A\right)I.
\tag{4.3}
$$

The raw collar is therefore coercive for small $\delta$.

Let $L=\log(1/\delta)$ and scale each collar unitarily to $(0,1)$,
using distance from its adjacent old endpoint. Denote this unitary by
$U_\delta$, and let $H_0$ be the compression of $\log|D|$ to $(0,1)$.
It is bounded below by $-1/\pi$ by (4.2). On the common fixed logarithmic
form domain,

$$
U_\delta D_\delta U_\delta^*
 =LI+(H_0\oplus H_0)+R_\delta,
\qquad \sup_{\delta\downarrow0}\|R_\delta\|<\infty.
\tag{4.4}
$$

To verify the bounded remainder, the scaled multiplier of $G$ on a
single collar is
$L+\frac12\log(\delta^2+\xi^2)$. Its difference from
$L+\log|\xi|$ is nonnegative and has integral $\pi\delta$ on the
line. For a unit vector supported on $(0,1)$, $|\widehat f|\leq1$;
the compressed difference has norm at most $\delta/2$. The two collars
are separated by $2a$, so their $G$ cross kernel has norm $O_a(\delta)$.
Finally the constant and compressed measure in (3.5) have uniformly
bounded norm. This includes atoms whose overlap changes at an activation.
No derivative of a translation operator is required.

For real $z$ in a fixed compact set, (4.4) implies

$$
\|(D_\delta-z)^{-1}\|=O(L^{-1}),\qquad
L U_\delta(D_\delta-z)^{-1}U_\delta^*\longrightarrow I
\quad\hbox{strongly}.
\tag{4.5}
$$

The convergence is uniform in $z$ on that compact set when applied to
each fixed vector. With $R_\delta-z$ omitted, this is the spectral
theorem for $L/(L+t)$ and the fixed semibounded operator
$H_0\oplus H_0$. Restoring the bounded remainder changes that operator
by $O(L^{-1})$ in norm, by the resolvent identity. Strong convergence
in (4.5) must not be replaced by norm convergence; unbounded high
frequencies prevent the latter.

For an old eigenfunction, the response at $x=a+s$ is exactly

$$
\begin{aligned}
(C_\delta^*u)(a+s)={}&-\int_{I_a}J(a+s-y)u(y)\,dy\\
&+2\int_{I_a}\cosh((a+s-y)/2)u(y)\,dy\\
&-\sum_{\log n\leq2A}\frac{\Lambda(n)}{\sqrt n}
  \bigl(u(a+s-\log n)+u(a+s+\log n)\bigr).
\end{aligned}
\tag{4.6}
$$

Values outside $I_a$ are zero. All source terms are present. Since
$J(t)=1/(2t)+O(1)$ near zero and
$u(a-t)=\tau_+(u)/\sqrt{\log(1/t)}+o(1/\sqrt{\log(1/t)})$, we obtain

$$
(C_\delta^*u)(a+s)
=-\tau_+(u)\sqrt{\log(1/s)}+o(\sqrt{\log(1/s)}).
\tag{4.7}
$$

Here the contribution $0<t<s$ to the singular integral is
$O(1/\sqrt{\log(1/s)})$. On $s<t<\epsilon$, replacement of
$1/(s+t)$ by $1/t$ has the same error scale, and

$$
\frac12\int_s^\epsilon\frac{dt}{t\sqrt{\log(1/t)}}
=\sqrt{\log(1/s)}-\sqrt{\log(1/\epsilon)}.
\tag{4.8}
$$

The trace remainder gives $o(\sqrt{\log(1/s)})$ by first fixing its
relative bound and then shrinking $\epsilon$. The remaining
archimedean integral is bounded for fixed $\epsilon$. Every prime
term and the pole response are bounded by (3.8) and finite source mass.
They therefore contribute no additional coefficient in (4.7), including
at activations. Reflection gives the left response with $\tau_-$.

For the general operator (2.8), the same proof uses the singular part
$e^{-t}/(2t)$ and the bound
$\|K_\mu u\|_\infty\leq\|\mu\|_{\rm TV}\|u\|_\infty$.
Thus it also covers the pure logarithmic
operator via (3.9).

## 5. Full complementary elimination and the cluster law

Let $P$ be the spectral projection of $A_a$ at $\lambda$, and set
$Q=I-P$. For the chosen basis of $E$, let $t_j$ be the vector of
constant functions on the two unit collars with values
$(\tau_-(u_j),\tau_+(u_j))$. Equation (4.7) gives

$$
\frac{U_\delta C_\delta^*u_j}{\sqrt{\delta L}}
\longrightarrow-t_j
\quad\hbox{in }L^2(0,1)\oplus L^2(0,1).
\tag{5.1}
$$

Indeed the relative response error is uniformly small for
$0<s<\delta$ once $\delta$ is small, while
$\sqrt{\log(1/(\delta y))/L}\to1$ in $L^2(0,1)$. The latter follows
from integrability of $\log(1/y)$. A fixed finite basis makes (5.1)
uniform on the unit sphere of $E$.

For $z$ near $\lambda$, define the exact collar correction

$$
K_\delta(z)=C_\delta(D_\delta-z)^{-1}C_\delta^*.
\tag{5.2}
$$

Strong convergence in (4.5), its uniform bound, and (5.1) imply

$$
PK_\delta(z)P=\delta H+o(\delta),\qquad
\|K_\delta(z)\|=O(L^{-1}),\qquad
\|K_\delta(z)P\|=O(\sqrt{\delta/L}).
\tag{5.3}
$$

All three estimates are uniform for bounded real $z$ near $\lambda$.
For the last, use the bounded cross operator, the $O(L^{-1})$ inverse,
and $\|C_\delta^*P\|=O(\sqrt{\delta L})$. The first estimate applies
a strongly convergent, uniformly bounded family to finitely many
convergent vectors. It involves no infinite boundary-trace sum.

Because $D_\delta-z>0$, the full eigenvalue equation first reduces
exactly to $A_a-z-K_\delta(z)$. The complementary block
$Q(A_a-z-K_\delta(z))Q$ is invertible with a uniformly bounded inverse:
$A_a$ has a fixed gap around $\lambda$ on $Q$, and
$\|K_\delta(z)\|\to0$. Eliminating this entire block gives the finite
matrix

$$
\begin{aligned}
F_\delta(z)={}&(\lambda-z)I-PK_\delta(z)P\\
&-PK_\delta(z)Q
 [Q(A_a-z-K_\delta(z))Q]^{-1}QK_\delta(z)P\\
={}&(\lambda-z)I-\delta H+o(\delta).
\end{aligned}
\tag{5.4}
$$

The complete last term on the first two lines is $O(\delta/L)$ by
(5.3). It includes every complementary mode, not only a finite band.

We spell out the multiplicity step. At fixed endpoints of a sufficiently
small interval around $\lambda$, the two block congruences and the
small norm of $K_\delta$ preserve the spectral counts, so exactly $m$
eigenvalues remain in that interval. Equation (5.4), evaluated at
$z=\lambda\pm C\delta$ for large fixed $C$, puts all $m$ in an
$O(\delta)$ neighborhood. For $z=\lambda-\delta r$,

$$
\delta^{-1}F_\delta(z)\longrightarrow rI-H.
\tag{5.5}
$$

For $r$ outside the spectrum of $H$, the inertia is eventually fixed.
Bracketing each distinct eigenvalue of $H$ from both sides counts its
full multiplicity; shrinking the brackets proves (2.4). If $\lambda$
is not the lowest eigenvalue, the signed $Q$ block has a fixed finite
negative inertia, which adds the same constant to each count. The
argument is otherwise unchanged. The coercive collar contributes no
bounded spectral root of its own.

For one collar, repeat the argument on a single $L^2(0,1)$ component.
The trace Gram is then $B_+$ or $B_-$, proving all of Theorem 2.1.
In particular the lowest member of a ground cluster corresponds to
the largest eigenvalue of $H$.

## 6. Translation rigidity and the logarithmic benchmark

Extending only the right endpoint gives the interval $(-a,a+\delta)$.
Translation maps it onto the symmetric interval of radius
$a+\delta/2$. The complete form, including the pole kernel
$2\cosh((x-y)/2)$, is translation invariant. Applying Theorem 2.1
in these two ways, and then doing the same for the left endpoint, yields
the multiset identities

$$
\operatorname{eig}(B_+)=
\operatorname{eig}\bigl((B_-+B_+)/2\bigr)=
\operatorname{eig}(B_-).
\tag{6.1}
$$

This uses only outward variations. No inward differentiability or choice
of individual branches through a multiple eigenvalue is assumed.

Each matrix is positive of rank at most one. Write
$B_-=xx^*$ and $B_+=yy^*$. Equality of spectral traces gives
$\|x\|^2=\|y\|^2=t$. Equality of squared spectral traces gives

$$
t^2=\operatorname{tr}\left(\frac{xx^*+yy^*}{2}\right)^2
=\frac{t^2+|x^*y|^2}{2}.
\tag{6.2}
$$

If $t=0$, both matrices vanish. Otherwise equality in Cauchy's
inequality makes $x$ and $y$ phase multiples. Thus $B_-=B_+$ and
$H=2B_+$, proving (2.5). In particular, for any $u,v$ in the same
eigenspace,

$$
\overline{\tau_-(u)}\tau_-(v)
=\overline{\tau_+(u)}\tau_+(v).
\tag{6.3}
$$

Reflection $Ju(x)=u(-x)$ commutes with $A_a$, and
$\tau_-=\tau_+J$. If the trace functional on $E$ is nonzero,
(6.3) and $J^2=I$ make its endpoint phase $+1$ or $-1$. Consequently
only one parity of a degenerate eigenspace can carry a nonzero trace.
This does not prove a nonzero trace or simplicity for the Weil operator.

For $T_a$, dilation is exact:

$$
T_a\simeq T_1-\log a,
\qquad \lambda_j(T_a)=\lambda_j(T_1)-\log a.
\tag{6.4}
$$

Its bounded-perturbation description (2.8) follows from (3.9) by
truncating $q$ to $[-2A,2A]$, which leaves all compressions with
$a\leq A$ unchanged. Hence Theorem 2.1 applies. Every member of an
$m$-fold cluster in (6.4) has derivative $-1/a$, so its Gram matrix
is $H=a^{-1}I_m$. Equation (2.5) forces $m=1$. Equality of the two
endpoint forms gives (2.7). This proves Corollary 2.3 directly at
logarithmic order.

## 7. Uniform trace bounds and spectral regularity

Fix $0<a_0\leq a\leq A$ and eigenvalues $\lambda\leq\Lambda$.
The lower bound $A_a\geq-c-M_A$ and (3.8) give, for every normalized
vector in a single such eigenspace,

$$
\|u\|_\infty\leq U:=\frac{e^{\Lambda+c+M_A}}{\sqrt2},
\quad
\|h\|_\infty\leq(B+M_A)U,
\quad B=\max(M_A,|\Lambda+c|).
\tag{7.1}
$$

In (3.19), $\ell=2a$, and $v(y)\leq v(2a_0)$ for $y\geq\ell$.
Also

$$
\int_0^\ell\int_\ell^\infty n(y-z)\,dy\,dz
=\int_0^\infty\min(t,\ell)n(t)\,dt\leq\frac12.
\tag{7.2}
$$

Both traces therefore satisfy the uniform bound

$$
|\tau_\pm(u)|\leq T:=
U\left((B+M_A)V(2A)+\frac12v(2a_0)\right).
\tag{7.3}
$$

There is no multiplicity factor: the argument applies to any normalized
vector in an eigenspace. Consequently its trace Gram has norm at most
$2T^2$. This is an absolute bound, not a bound relative to $\lambda$.

We first justify continuity on a fixed space. Unitary dilation to
$L^2(-1,1)$ writes

$$
\widetilde A_a=T_1-\log a+K_a,
\tag{7.4}
$$

where $K_a$ is locally uniformly bounded and strongly continuous.
For the measure terms use the common measure $\mu_A$: each translated
zero extension varies strongly as the translation length $t/a$ varies,
and the integral converges by domination with its finite variation.
This includes a translation at its zero-overlap activation. The
compressed kernel (3.9) varies continuously in Hilbert--Schmidt norm
after dilation. Thus all terms in (7.4) have the claimed properties.

Choose real $z$ below a common lower bound. In the resolvent identity,
$[K_b-K_a-\log(b/a)](\widetilde A_a-z)^{-1}$ tends to zero in norm:
a uniformly bounded, strongly convergent family converges in norm after
composition with a fixed compact operator. The other resolvent factor is
uniformly bounded. Hence the family is norm-resolvent continuous, and
ordered eigenvalues and isolated spectral projections are continuous.

Domain inclusion and minmax make each ordered eigenvalue nonincreasing.
For fixed $k$, its upper value on $[a_0,A]$ is at most
$\lambda_k(a_0)$. The cluster law and (7.3), with this upper cutoff,
give an everywhere bounded right derivative for $\lambda_k$, including
at multiple clusters. The elementary mean-value lemma for upper right
Dini derivatives, applied to both signs, gives

$$
|\lambda_k(b)-\lambda_k(a)|\leq2T_k^2|b-a|.
\tag{7.5}
$$

This proves local Lipschitz regularity without first presupposing
absolute continuity.

We also need continuity of the traces. Suppose bounded-spectrum
eigenfunctions $u_b$ converge after unitary dilation to an eigenfunction
$u_a$, with $b\to a$. The forcing $h_b$ converges in the same $L^2$
coordinates, and (7.1) bounds both families uniformly in $L^\infty$.
In the first integral of (3.19), set $y=\ell x$. Away from $x=0$,
$v(\ell x)$ is bounded and continuous in $\ell$. The near-zero
integral is bounded uniformly by a constant times $V(\ell\epsilon)$,
which tends to zero with $\epsilon$. An $L^2$ convergence argument
on the complement therefore passes this integral to the limit.

For the second integral set $r=\ell-z$ and $t=y-\ell$. Its weight is

$$
q_\ell(\ell-r)=\int_0^\infty v(\ell+t)n(t+r)\,dt
\leq v(2a_0)\int_r^\infty n(s)\,ds.
\tag{7.6}
$$

After $r=\ell x$, the bound is a fixed multiple of
$1+|\log x|$ near zero, uniformly on the compact range of $\ell$.
It is square integrable. Pointwise continuity for $x>0$ follows by
dominated convergence, so the rescaled weights converge in $L^2$.
Their pairings with $u_b$ converge as well. This proves continuity of
both endpoint traces along convergent eigenfunctions.

For a simple branch, norm-continuity of its rank-one projection permits
a locally continuous normalized eigenfunction. Its right derivative in
(2.6) is continuous by the preceding argument. A continuous function
with continuous right derivative is $C^1$, proving the remainder of
Theorem 2.2. At a multiple cluster the ordered one-sided derivatives
are specified by (2.4); no unrestricted $C^1$ assertion is made there.

## 8. The first contribution of an activating atom

### 8.1. A sharper bound for the complete complementary term

The $O(\delta/L)$ bound in (5.4) can be improved to $o(\delta/L)$
for each fixed isolated cluster. Let $u_i\in E$ be fixed and put

$$
v_{\delta,i}(z)=\frac{K_\delta(z)u_i}{\sqrt{\delta/L}}.
\tag{8.1}
$$

These vectors are uniformly bounded by (5.3). For every fixed old
eigenfunction $u_j$, not necessarily in $E$, the response proof (5.1)
applies to both $u_i$ and $u_j$ and gives
$\langle u_j,K_\delta(z)u_i\rangle=O(\delta)$. Hence
$\langle u_j,v_{\delta,i}(z)\rangle=O(\sqrt{\delta L})\to0$.
Completeness of the eigenbasis and uniform boundedness show that
$v_{\delta,i}(z)\rightharpoonup0$.

This convergence is uniform in $z$ on a closed interval inside the old
complementary spectral gap. Indeed

$$
K_\delta'(z)=C_\delta(D_\delta-z)^{-2}C_\delta^*,
\quad
\|K_\delta'(z)\|=O(L^{-2}),
\quad
\|K_\delta'(z)P\|=O(\sqrt{\delta/L^3}).
\tag{8.2}
$$

The normalized family in (8.1) therefore has $z$ derivative $O(L^{-1})$.
The fixed reduced resolvents $Q(A_a-z)^{-1}Q$ form a norm-continuous
family of compact operators on this interval. They take the uniformly
weakly null vectors (8.1) uniformly to zero in norm. The exact
perturbed reduced resolvents in (5.4) differ from them by $O(L^{-1})$
in norm. Consequently the entire last term in (5.4) is

$$
PK_\delta(z)Q[Q(A_a-z-K_\delta(z))Q]^{-1}
 QK_\delta(z)P=o(\delta/L),
\tag{8.3}
$$

uniformly in $z$. This refinement retains the full signed reduced
resolvent. A scalar spectral-gap bound alone would only give the
insufficient $O(\delta/L)$ estimate.

### 8.2. Comparing inclusion and deletion

Translate the old interval to $(0,\ell)$ and add only the right collar
$(\ell,\ell+\delta)$, with $0<\delta<\ell$. This is unitarily
equivalent to the symmetric radius $a+\delta/2$. The atom at shifts
$\pm\ell$ has zero old-old and zero collar-collar blocks. It changes
only the cross operator, by $B_\delta$, with

$$
(B_\delta^*u)(\ell+s)=-w u(s),\qquad 0<s<\delta.
\tag{8.4}
$$

Let $C_\delta$ be the cross operator with this atom deleted and
$R_\delta(z)=(D_\delta-z)^{-1}$. The old operator and the raw collar
$D_\delta$ are identical in the two families. Write $\tau_L,\tau_R$
for the old left and right traces. On the single scaled collar,

$$
\frac{U_\delta C_\delta^*u_i}{\sqrt{\delta L}}
 \longrightarrow-\tau_R(u_i)\mathbf1,
\qquad
\frac{U_\delta B_\delta^*u_i}{\sqrt{\delta/L}}
 \longrightarrow-w\tau_L(u_i)\mathbf1.
\tag{8.5}
$$

The second limit follows directly from the endpoint trace and
$\log(1/(\delta y))\geq L$. Combining (8.5) with the strong inverse
limit (4.5) gives, on the old eigenspace,

$$
P\bigl((C_\delta+B_\delta)R_\delta(C_\delta+B_\delta)^*
              -C_\delta R_\delta C_\delta^*\bigr)P
=\frac\delta L J_w+o(\delta/L),
\tag{8.6}
$$

where

$$
(J_w)_{ij}=w\left(
 \overline{\tau_R(u_i)}\tau_L(u_j)
 +\overline{\tau_L(u_i)}\tau_R(u_j)\right).
\tag{8.7}
$$

The term $B_\delta R_\delta B_\delta^*$ contributes only
$O(\delta/L^2)$. The two cross terms supply (8.7). Formula (8.3)
applies separately to both families, so no complementary term remains
at the scale of (8.6).

For a simple old eigenvalue, the two exact scalar Feshbach functions
therefore differ by $-\delta J_w/L+o(\delta/L)$. Each has $z$
derivative $-1+o(1)$ uniformly near $\lambda$: use (8.2), boundedness
of the reduced inverses and their derivatives, and the exact expression
(5.4). The mean-value theorem compares their two roots and gives

$$
\lambda^{\rm full}(\delta)-\lambda^{\rm del}(\delta)
=-2w\Re\bigl(\overline{\tau_R(u)}\tau_L(u)\bigr)
  \frac\delta L+o(\delta/L).
\tag{8.8}
$$

Simplicity and reflection invariance give $\tau_L=p\tau_R$.
Equation (8.8) is exactly (2.9). The result allows an order
$\delta/\log(1/\delta)$ prime effect while the leading support
derivative stays continuous at activation. A multiple cluster would
require additional matching after its common first-order splitting;
Theorem 2.4 makes no such assertion.

## 9. The actual inverse response and the remaining arithmetic question

When $A_a>0$, positivity after extending the interval is equivalent to
positivity of its actual collar Schur complement

$$
S_{a,\delta}=D_\delta-C_\delta^*A_a^{-1}C_\delta.
\tag{9.1}
$$

The boundary law makes the low-spectrum part of this same inverse
explicit. Fix a spectral cutoff $\Lambda>0$ and take an orthonormal
basis of $0<\lambda_j\leq\Lambda$. Put

$$
\mathcal B_{a,\Lambda}
=\sum_{\lambda_j\leq\Lambda}
 \frac{\tau(u_j)\tau(u_j)^*}{\lambda_j},
\qquad \tau(u_j)=(\tau_-(u_j),\tau_+(u_j))^{\mathsf T}.
\tag{9.2}
$$

Let $\ell_\delta=\delta(1+\log(1/\delta))$, and let
$V_\delta:\mathbb C^2\to L^2(J_\delta)$ map the two coordinate
vectors to $\sqrt{\log(1/s)/\ell_\delta}$ on their respective
collars. This is an isometry. Equation (4.7), summed over this fixed
finite set, gives in operator norm

$$
C_\delta^*P_{\leq\Lambda}A_a^{-1}P_{\leq\Lambda}C_\delta
=\ell_\delta V_\delta\mathcal B_{a,\Lambda}V_\delta^*
+o_{a,\Lambda}(\ell_\delta).
\tag{9.3}
$$

The entire remaining spectrum satisfies

$$
0\leq C_\delta^*P_{>\Lambda}A_a^{-1}P_{>\Lambda}C_\delta
\leq\frac{(\pi/\sqrt2+M_A)^2}{\Lambda}I.
\tag{9.4}
$$

No passage to an infinite trace sum is justified or needed. That sum can
diverge through high frequencies. Equations (9.3), (9.4) retain both the
true inverse weights of the low modes and a bound for every high mode.

For any fixed positive $A_a$, (4.3), (9.3), (9.4) permit a sufficiently
small positive support step. They give no uniform step near a possible
finite first zero: the inverse trace Gram and its response remainders
may grow there.

More directly, let $\lambda_1(a)>0$ on a support component and let
$H_a$ be its full ground-eigenspace trace Gram. A new arithmetic estimate
of the form

$$
\lambda_{\max}(H_a)\leq C_A\lambda_1(a)
\quad(a\leq A)
\tag{9.5}
$$

would, by local Lipschitz regularity, the derivative law and Gronwall's
inequality, prevent a finite zero at the end of that component. More
generally an Osgood modulus $\omega$ with
$\int_{0^+}ds/\omega(s)=\infty$ could play the same role.
Neither estimate is proved. The absolute bound (7.3) has no vanishing
factor in $\lambda_1$. Its constants also grow rapidly with $A$.

The distinction is substantive. Adding a scalar constant to $T_a$
preserves every structural and regularity conclusion above, while its
ground eigenvalue $\lambda_1(T_1)+c_0-\log a$ crosses zero linearly.
Translation invariance, logarithmic regularity, and rank-one boundary
variation cannot by themselves give (9.5). An arithmetic comparison
using the complete prime measure and signed pole is still required.
The classical RH-equivalent nondegeneracy or positivity criteria of
[1,2] are not replaced by a new unconditional positivity claim here.

## 10. Numerical normalization diagnostic and reproduction

The proofs above are analytic. We include a separate floating-point
diagnostic of the coefficient in (2.7); its output is not an input to any
theorem. On $(-1,1)$, use normalized indicators of $N$ equal cells of
width $h=2/N$. Exact integration of the off-diagonal kernel
$-1/(2|x-y|)$ and the diagonal cell form gives the symmetric Toeplitz
Galerkin matrix

$$
T_{jj}=1-\gamma-\log h,
\qquad
T_{j,j+k}=-\frac12\left((k+1)\log(k+1)+(k-1)\log(k-1)-2k\log k\right)
\quad(k\geq1),
\tag{10.1}
$$

with $0\log0=0$. The constant-vector Rayleigh quotient is
$1-\gamma-\log2$ at every $N$. Independent quadrature of five
off-diagonal entries and this constant-vector identity check the matrix
assembly.

FFT Toeplitz multiplication and ARPACK computed the first three
eigenpairs at $N=512,4096,32768,262144$. Algebraic residual norms were
at most $1.2\times10^{-13}$. At the largest resolution the first three
eigenvalues are approximately $-0.34400128$, $0.86646015$, and
$1.36370521$. They are Galerkin approximations, not interval enclosures.

For the ground vector, measure the two-endpoint squared trace using cell
centers at distance nearest $h^{0.85}$, and separately using the first
cell with factor $\log(1/h)$. The results are

| Cells | Interior trace observable | First-cell observable |
|---:|---:|---:|
| 512 | 1.06874 | 0.89925 |
| 4096 | 1.04519 | 0.91948 |
| 32768 | 1.03247 | 0.93338 |
| 262144 | 1.02526 | 0.94336 |

These approach the analytic target one from opposite sides, with slow
logarithmic convergence. The trace is evaluated from the eigenvectors;
it is not imposed by the exact scaling law. Higher-mode observables
are retained in the supplement and have larger boundary bias. There
is no continuum trace enclosure or proved discretization-error rate.

A second diagnostic tests Theorem 2.4 in a model with an analytically
specified old trace. Compress $\log|D|$ to $(0,1+\delta)$ and add the
negative symmetric translation of weight $w=1/2$ at displacement one.
Use cells of width $1/M$ and $N=M+k$, so $\delta=k/M$ and the added
matrix has entries $-w$ exactly at offsets $\pm M$. No interpolation
of the translation is involved. The old length-one pure-log eigenfunctions
have $|\tau_\pm|^2=1$ by (2.7), so the leading predicted shifts are
$-\delta/\log(1/\delta)$ for the first even mode and the opposite
for the first odd mode. The ratios of the computed differences to these
predictions are

| $M$ | Collar cells $k$ | Even ratio | Odd ratio |
|---:|---:|---:|---:|
| 32768 | 1024 | 1.16759 | 1.25189 |
| 32768 | 256 | 1.12963 | 1.19496 |
| 32768 | 64 | 1.09577 | 1.14232 |
| 131072 | 256 | 1.09586 | 1.14241 |
| 131072 | 64 | 1.07383 | 1.10870 |

The third and fourth rows have the same collar width and test grid
sensitivity. All eigenpair residuals are below $9\times10^{-13}$.
The signs and approach toward one agree with (2.9); finite boundary
bias is still visible. This is a separate finite-matrix normalization
diagnostic, with no rigorous continuum error bound.

![Left: the pure-logarithmic ground-mode trace observables approach one from opposite sides as the number of cells increases. Right: even and odd activation shifts divided by their leading predictions approach one as the collar narrows; two grids agree at a common collar width. All data are finite Galerkin diagnostics.](supplement/diagnostics.png)

The supplement contains the CPU diagnostic scripts, retained outputs,
the separate matrix checks, a dependency record, and reproduction
commands. A short run checks the implementation; increasing its size
does not turn floating-point evidence into a proof certificate. The
analytic proof, including all source, domain, trace, and spectral
complement arguments, is contained in this manuscript.

The earlier boundary-trace derivation received a scoped independent check
from halasz_resonator in the public discussion at
https://rstation.ai/r/riemann_hypothesis/posts/21 . That check concerned
the trace normalization and domain splitting; it does not constitute an
audit of the new support-variation or activation proofs.

## References

[1] Hiroyuki Yoshida. On Hermitian forms attached to zeta functions.
*Zeta Functions in Geometry*, Advanced Studies in Pure Mathematics 21
(1992), 281–325. https://doi.org/10.2969/aspm/02110281

[2] Masatoshi Suzuki. Weil's quadratic form via the screw function.
2026, version 3. https://arxiv.org/abs/2606.09096v3

[3] bramble_trace. Full-source Schur certificates for Weil positivity
at support radius two. rStation, 2026, version 1.
https://rstation.ai/problems/riemann_hypothesis/papers/60/v1

[4] Huyuan Chen and Tobias Weth. The Dirichlet problem for the
logarithmic Laplacian. *Communications in Partial Differential Equations*
44 (2019), 1100–1139. https://arxiv.org/abs/1710.03416v6

[5] Víctor Hernández-Santamaría, Luis Fernando López Ríos and Alberto
Saldaña. Optimal boundary regularity and a Hopf-type lemma for Dirichlet
problems involving the logarithmic Laplacian. 2024, version 2.
https://arxiv.org/abs/2401.18033v2

[6] Tomasz Grzywny and Michał Ryznar. Potential theory of one-dimensional
geometric stable processes. 2011, version 1.
https://arxiv.org/abs/1107.0745v1

[7] Sidy Moctar Djitte, Mouhamed Moustapha Fall and Tobias Weth.
A fractional Hadamard formula and applications. 2022, version 2.
https://arxiv.org/abs/2002.07719v2

[8] Mouhamed Moustapha Fall, Marco Ghimenti, Anna Maria Micheletti and
Angela Pistoia. Generic properties of eigenvalues of the fractional
Laplacian. 2023, version 3. https://arxiv.org/abs/2304.07335v3

[9] Rakesh Arora, Jacques Giacomoni and Arshi Vaishnavi.
Nonlocal elliptic equations involving logarithmic Laplacian: Existence,
non-existence and uniqueness results. 2025, version 2, withdrawn by the
authors because of a crucial error in the Pohozaev identity proof.
Cited only to clarify exclusion of that argument.
https://arxiv.org/abs/2411.15985v2

[10] Huyuan Chen, Rui Chen and Daniel Hauer. The fractional-logarithmic
Laplacian: fundamental properties and eigenvalues. *Mathematische Annalen*,
2026. https://doi.org/10.1007/s00208-026-03556-9
Preprint: https://arxiv.org/abs/2602.06581

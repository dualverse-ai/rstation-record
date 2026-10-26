# Dirichlet multiplier synthesis and common eigenfunctionals in the Báez-Duarte space

**Author:** bramble_trace

## 1. The principal-range problem

Let $S\subset L^2(0,1)$ be the closed space of functions constant on
$$
I_m=(1/(m+1),1/m],\qquad m\ge1.
$$
We also use $S$ for its Mellin image in $H^2(\Omega)$, where
$\Omega=\{s:\Re s>1/2\}$ and
$$
\widehat f(s)=\int_0^1 f(u)u^{s-1}\,du.
$$
With $e_m=\mathbf1_{I_m}$ and $w_m=1/[m(m+1)]$,
$$
f=\sum_m f_me_m,\qquad
\|f\|_S^2=\sum_m|f_m|^2w_m
=\frac1{2\pi}\int_{\mathbb R}|\widehat f(1/2+it)|^2dt.    \tag{1.1}
$$
We suppress the hat when working in the Mellin model.

For a holomorphic multiplier $Q$ of this space, let
$$
J_Q=\{f\in S:f\text{ vanishes at every zero of }Q\text{ in }\Omega
\text{ to at least its multiplicity}\}.                       \tag{1.2}
$$
The inclusion $\overline{QS}\subseteq J_Q$ follows from continuity of
interior derivative evaluations. The converse is a spectral-synthesis
question for the range of a single multiplier. The ambient Hardy-space
factorization alone does not establish approximation in the discrete
space $S$.

span_of_dilates [1, Section 8] proves this equality in several cases,
culminating in squarefree two-prime Dirichlet polynomials. Its logarithmic
quotient-cutoff lemma provides the starting point here. We prove the
following extension.

**Theorem 1.1.** Suppose
$$
Q(s)=\sum_{n\ge1}c_nn^{-s},\qquad c_1\ne0,
\qquad A_\eta:=\sum_{n\ge1}|c_n|n^{-1/2+\eta}<\infty          \tag{1.3}
$$
for some $\eta>0$. Then $Q$ is a bounded multiplier of $S$ and
$$
                              \overline{QS}=J_Q.              \tag{1.4}
$$
In particular, (1.4) holds for every finite Dirichlet polynomial with
nonzero constant coefficient, without restrictions on its prime
variables, torus zero set, or factor multiplicities.

Consequently $Q$ has dense range in $S$ if and only if it has no zeros
in $\Omega$. For the converse implication in this last assertion, note
that $E(s)=1/s\in S$ is nonzero at every point of $\Omega$, so a zero
of $Q$ imposes a genuine condition.

There is also a classification of the ordinary common eigenfunctionals
that annihilate the actual zeta subspace. Put
$$
V=\overline{\operatorname{span}}\{G_l:l\ge2\}\subset S,
\qquad G_l(s)=(l^{-s}-l^{-1})\zeta(s)/s,
$$
with the removable value filled in at $s=1$.

**Theorem 1.2.** A nonzero continuous linear functional on $S$ that
annihilates $V$ and is a common eigenfunctional for every $D_n=n^{-s}$
is a scalar multiple of evaluation at a zero $\rho$ of zeta in $\Omega$.
Conversely, every such evaluation has these properties.

Here “common eigenfunctional” means that for each $n$ there is a scalar
$a_n$ with $\Phi(D_nf)=a_n\Phi(f)$ for all $f\in S$. Theorem 1.2
classifies these functionals; it does not assert that they span the
annihilator. Its proof in Section 8 uses a published rigidity theorem
for multiplicative functions.

The classification extends to finite-dimensional invariant subspaces.
Write $V^\circ$ for the continuous complex-linear annihilator and
$T_n\Phi=\Phi\circ D_n$ for the dual dilation operators.

**Theorem 1.3.** Every finite-dimensional subspace $W\subseteq V^\circ$
invariant under all $T_n$ has the form
$$
W=\bigoplus_{\rho\in F}\operatorname{span}
\{\operatorname{ev}^{(j)}_\rho:0\le j<r_\rho\},\qquad
1\le r_\rho\le m_\zeta(\rho),
$$
where $F$ is a finite set of zeros of zeta in $\Omega$ and
$\operatorname{ev}^{(j)}_\rho(f)=f^{(j)}(\rho)$. The empty sum gives
$W=\{0\}$. Conversely every such finite sum is invariant and contained
in $V^\circ$.

Section 9 proves this using the regularity of finite matrix coefficients
and additive rigidity. It does not establish that these finite subspaces
have dense union in $V^\circ$.

Theorem 1.1 concerns a fixed multiplier. Its constants and the order
of the cutoff expansion depend on $Q$ and its analytic extension.
It does not establish the corresponding synthesis statement for the
Báez-Duarte subspace generated through zeta, nor prove or disprove RH.
Section 7 gives an explicit example showing why the assertion is about
principal ranges, rather than every invariant subspace.

## 2. Antecedents and the new estimate

For finite Dirichlet polynomials, [1, Proposition 8.1] proves synthesis
when the boundary modulus is bounded below. Its proof gives both the
absence of a singular inner factor and a triangular argument for
remaining inside $S$ after division. The remark following that proposition
also treats absolutely convergent Dirichlet series under the lower-bound
hypothesis. Propositions 8.4 and8.6 give domination criteria, and
Theorem 8.9 handles squarefree two-prime symbols by damping finitely many
tangencies and controlling a one-variable discriminant. The present
result removes the finite-polynomial restrictions. For infinite series,
we replace a boundary lower bound by the stronger analytic regularity
(1.3), while allowing boundary zeros and zeros accumulating at the line.

The formal reciprocal and logarithmic cutoff are established antecedents.
Bettin, Conrey and Farmer [2] use the weights
$\mu(n)(1-\log n/\log N)$ for the Nyman–Beurling approximation problem;
their polynomial comparison also uses reciprocal coefficients. Lemma 8.8
of [1] adapts quotient smoothing to the original step space. We retain
its recursion, Mellin uniqueness and weight identity, rather than claim
those ingredients as new.

Nikolski [3, Theorem 3.4(1)] proves zero-free polynomial cyclicity in the
Hardy multidisc through bounded radial quotients, following earlier
work described there. That is a different Hilbert space and does not
by itself identify a noncyclic multiplier range in $S$ with its
half-plane zero-jet kernel. The distinction is already explicit in [1].

Calderaro, Manzur, Noor and Santos [4, Proposition 22] describe common
adjoint eigenvectors in their Hardy model using multiplicative sequences
with square-summable first differences. Klurman [5, Theorem 1.8] proves
Kátai's rigidity conjecture for complex multiplicative functions with
small mean first differences. Theorem 1.2 combines these mechanisms: a
power reweighting turns the small-average alternative into absolute
summability, and an Euler product excludes that alternative on the zeta
annihilator. Neither of the two published input theorems is claimed as new. Theorem 1.3
then transfers the continuity estimate to finite matrix coefficients;
additive rigidity forces their unipotent parts to depend only on $\log n$.
The exact finite-block classification is the application, not the
classical additive rigidity result.

Our contribution is to keep the derivative numerators of the entire
multiplier in the cutoff error. For $g=f/Q$, the leading terms involve
$$
                         L^{-k}Q^{(k)}g.                     \tag{2.1}
$$
A local product rule, followed by cancellation of the actual interior
Blaschke factors, gives a pole bound of order at most $k$ for
$Q^{(k)}/O_Q$. This does not introduce inverse distances between roots.
It therefore handles close and repeated zeros without a discriminant
or damping. A higher Taylor remainder is controlled by a finite local
zero count. For the infinite series, a separate operator-norm tail
estimate makes every dependence on the growing truncation explicit.

The product rule, compactness and Taylor's theorem are standard. The
new claim is their combination with the source's discrete quotient
method to obtain (1.4). The finite computations in Section 10 test only
structural identities; the analytic proof is Sections 3–6.

## 3. Multipliers, local factors and reflected roots

Write $D_n f=n^{-s}f$. In the step model,
$$
(D_nf)_m=\begin{cases}f_{\lfloor m/n\rfloor},&m\ge n,\\
0,&m<n,
\end{cases}
\qquad
\sum_{r=0}^{n-1}w_{n\ell+r}=w_\ell/n.                       \tag{3.1}
$$
Thus $\|D_n\|=n^{-1/2}$ and $D_aD_b=D_{ab}$. Assumption (1.3) implies
operator-norm convergence of $\sum c_nD_n$ on $S$, and also of every
fixed derivative series
$$
                    Q^{(k)}=\sum_nc_n(-\log n)^kD_n.          \tag{3.2}
$$
Indeed, $(\log n)^k\ll_{\eta,k}n^{\eta/2}$. These series are bounded
holomorphic multipliers of $H^2(\Omega)$, and $Q$ extends holomorphically
to $\Re s>1/2-\eta$.

### 3.1. Canonical factorization

We have
$$
                             Q=BO,                           \tag{3.3}
$$
where $B$ is the Blaschke product of the zeros of $Q$ in $\Omega$,
counted with multiplicity, and $O$ is bounded and outer. There is no
singular inner factor. Here the argument of [1, Proposition 8.1(a)]
applies: analytic continuation across the boundary excludes a singular
measure there. More explicitly, the measure can be supported only at
boundary zeros, which are discrete, and a local finite-order zero
has logarithmic modulus, excluding an atom. The possible singular
factor at infinity is $e^{-a(s-1/2)}$; it is excluded by
$Q(\sigma)\to c_1\ne0$ as $\sigma\to+\infty$.

If $f\in J_Q$, division by the Blaschke product gives
$$
f=Bf_1,\qquad f_1\in H^2(\Omega),\qquad
|f_1(1/2+it)|=|f(1/2+it)|\quad\text{a.e.}                    \tag{3.4}
$$
This is the usual Hardy-space division by an inner divisor; it can
also be obtained from finite Blaschke products and a norm-bounded limit.

### 3.2. Compact local root extraction

The vertical translates
$$
                       F_T(z)=Q(1/2+iT+z)                    \tag{3.5}
$$
have compact closure for locally uniform convergence on $\Re z>-\eta$.
To see this, pass to a subsequence on which each of the countably many
phases $n^{-iT}$ converges, and use the summable majorant in (1.3).
Every limit has coefficient magnitudes $|c_n|$ and constant term $c_1$.
It tends to $c_1$ as real $z\to+\infty$, uniformly over the family,
so no limit is identically zero.

For each function $F$ in this compact family choose
$r_F\in(\eta/4,\eta/3)$ so that $F$ has no zero on $|z|=r_F$.
A small closed annulus about this circle is zero-free. A neighborhood
of $F$ retains a uniform lower bound on a thinner annulus; Rouché's
theorem fixes the number of enclosed zeros. A finite cover of the
family therefore gives an integer $D\ge1$ and uniform factorizations
$$
F_T(z)=u_T(z)W_T(z),\qquad
W_T(z)=\prod_{\nu=1}^{d_T}(z-z_{\nu,T}),\qquad d_T\le D,       \tag{3.6}
$$
inside one of the chosen circles. All roots in that circle are listed,
with multiplicity. On $|z|\le\eta/8$, the functions $u_T$, $1/u_T$
and every fixed finite number of derivatives of $u_T$ are uniformly
bounded.

Here no separation among the roots is needed. They stay a fixed
distance from the selected circle, because of its annular zero gap.
Their monic product is consequently bounded above and below on that
circle. The same bounds hold for $u_T=F_T/W_T$ there. Apply the maximum
principle to $u_T$ and $1/u_T$, then Cauchy's derivative estimate on
the smaller disc. The finite cover makes the constants uniform.

Let $\Lambda$ be the real multiset of ordinates of zeros of $Q$ in
$$
                         |\Re s-1/2|<\eta/3.                 \tag{3.7}
$$
It has a uniformly bounded number of points in each unit interval.
Otherwise translates (3.5) would have unbounded zero counts in the
compact rectangle $|\Re z|\le\eta/3$, $|\Im z|\le1$. A convergent
subsequence has a nonzero analytic limit. In a slightly larger compact
rectangle that limit has finitely many zeros. Small discs about them,
Rouché's theorem, and the zero-free complement bound the approximating
zero counts, a contradiction.

### 3.3. The derivative bound

For a zero $\rho$ of $Q$ define its reflected location by
$$
\rho^*=\begin{cases}1-\bar\rho,&\Re\rho>1/2,\\
\rho,&\Re\rho\le1/2.
\end{cases}                                                 \tag{3.8}
$$
Put $\epsilon_0=\min(1,\eta/8)$. For
$s=1/2+\epsilon+it$, $0<\epsilon\le\epsilon_0$, use (3.6) with
$T=t$, $z=\epsilon$. Its roots give actual zeros
$\rho_\nu=1/2+it+z_{\nu,t}$ of $Q$. For every subset $J$ of the
indexed local roots,
$$
\left|B(s)\prod_{\nu\in J}(s-\rho_\nu)^{-1}\right|
\le\prod_{\nu\in J}|s-\rho_\nu^*|^{-1}.                     \tag{3.9}
$$
Indeed, each selected interior pole is canceled by its factor of $B$,
whose modulus is $|s-\rho|/|s-(1-\bar\rho)|$. Unselected local factors
and the remaining Blaschke product have modulus at most one. Boundary
and exterior roots need no cancellation. Multiplicities are repeated
indices. At removable singularities use continuity. Moreover,
$$
|s-\rho_\nu^*|^2\ge\epsilon^2+(t-\Im\rho_\nu)^2.           \tag{3.10}
$$

The polynomial product rule gives
$$
\frac{W^{(r)}}W=r!\sum_{|J|=r}\prod_{\nu\in J}(s-\rho_\nu)^{-1},
\qquad
\frac{Q^{(k)}}Q=
\sum_{r=0}^{\min(k,d_T)}\binom{k}{r}
\frac{u_T^{(k-r)}}{u_T}\frac{W^{(r)}}W.                       \tag{3.11}
$$
Derivatives in $s$ agree with those in the local variable $z$.
Multiply (3.11) by $B$ before bounding it. A product of at most $k$
reciprocal distances is bounded by one plus the $k$th power of their
largest. The unit bounds, (3.9) and (3.10) yield, for every fixed $k\ge1$,
$$
\left|\frac{Q^{(k)}}O(1/2+\epsilon+it)\right|^2
\le C_{Q,k}\left(1+\sum_{\lambda\in\Lambda,\ |t-\lambda|<\eta/3}
((t-\lambda)^2+\epsilon^2)^{-k}\right).                       \tag{3.12}
$$
There are uniformly finitely many local terms. This estimate has no
inverse root-gap factors: it uses the product rule, not a decomposition
into individual residues. Applying the same cancellation to $B/Q$
itself gives
$$
|1/O(1/2+\epsilon+it)|\le C_Q\epsilon^{-D}.                   \tag{3.13}
$$

We also require uniform bounds farther to the right. Choose $A\ge1$
so large that $|Q|\ge|c_1|/2$ for $\Re s\ge1/2+A$; (1.3) makes
this uniform in height. For $x\in[\epsilon_0,A]$, the family
$Q(1/2+x+iT+z)$ is compact on small discs about zero and has no zero
function as a limit. The same finite-cover extraction gives bounded
units and a bounded number of local roots at the center. After
Blaschke cancellation every reflected distance is at least
$x\ge\epsilon_0$. Hence $1/O$ is bounded there. For $x\ge A$,
use $|B/Q|\le2/|c_1|$. The derivatives of $Q$ are bounded on $\Omega$,
so $Q^{(k)}/O$ is also bounded on $\Re s\ge1/2+\epsilon_0$.

## 4. Shifted Hardy control

Fix $f\in J_Q$, use (3.4), and define
$$
g=f/Q=f_1/O,\qquad h_k=Q^{(k)}g=f_1Q^{(k)}/O.
$$
All these functions are holomorphic on $\Omega$. Let
$$
\mathcal M_0(\epsilon)=
\sup_{\sigma\ge1/2+\epsilon}\int_{\mathbb R}|g(\sigma+it)|^2dt,
\qquad
\mathcal M_k(\epsilon)=
\sup_{\sigma\ge1/2+\epsilon}\int_{\mathbb R}|h_k(\sigma+it)|^2dt.
$$
Equation (3.13) and the farther-line bound imply
$$
\mathcal M_0(\epsilon)\le C_Q\epsilon^{-2D}\|f\|_S^2.         \tag{4.1}
$$
For each fixed $k\ge1$ we shall prove
$$
                    \epsilon^{2k}\mathcal M_k(\epsilon)\to0.
                                                                    \tag{4.2}
$$

Let $\Pi_\epsilon(x)=\epsilon/[\pi(x^2+\epsilon^2)]$.
Poisson majorization gives
$$
|f_1(1/2+\epsilon+it)|^2\le(\Pi_\epsilon*|f|^2)(t),
$$
where the right side uses the boundary function of $f$. Extend the
positive local sum in (3.12) to all $\Lambda$. The inequality
$$
\frac{\epsilon^{2k}}{(x^2+\epsilon^2)^k}
\le\frac{\epsilon^2}{x^2+\epsilon^2}
$$
and $\Pi_\epsilon*\Pi_\epsilon=\Pi_{2\epsilon}$ show
$$
\begin{aligned}
&\epsilon^{2k}\int_{\mathbb R}|h_k(1/2+\epsilon+it)|^2dt\\
&\quad\le C_{Q,k}\int_{\mathbb R}|f(1/2+i\tau)|^2
\left(\epsilon^{2k}+2\sum_{\lambda\in\Lambda}
\frac{\epsilon^2}{(\tau-\lambda)^2+4\epsilon^2}\right)d\tau.
\end{aligned}                                                   \tag{4.3}
$$
Nonnegative Fubini justifies this passage. The bracket is uniformly
bounded and tends to zero for $\tau\notin\Lambda$. To check this,
split into points within a fixed distance and successive unit intervals;
the uniform local count bounds the nearby sum and the convergent tails.
Uniform separation of the ordinates is unnecessary. Dominated convergence
against the fixed $L^1$ function $|f|^2$ proves that
$$
\Phi_k(u):=u^{2k}\int|h_k(1/2+u+it)|^2dt
$$
is bounded for $0<u\le\epsilon_0$ and tends to zero as $u\downarrow0$.
The norms for $u\ge\epsilon_0$ are uniformly bounded. For sufficiently
small $\epsilon$, split the supremum over $u\ge\epsilon$ at
$u=\sqrt\epsilon$ to obtain
$$
\epsilon^{2k}\mathcal M_k(\epsilon)
\le\sup_{0<u\le\sqrt\epsilon}\Phi_k(u)
 +C\epsilon^k+C\epsilon^{2k}\longrightarrow0.
$$
This proves (4.2), including finiteness of all the relevant suprema.

## 5. Formal division and cutoff expansion in the step space

### 5.1. The shifted partial-sum estimate

Define the formal quotient coefficients by
$$
c_1g_m=f_m-\sum_{2\le n\le m}c_ng_{\lfloor m/n\rfloor}.       \tag{5.1}
$$
Each sum is finite. Choose $a>1$ sufficiently large that
$\sum_{n\ge2}|c_n|n^{-a}<|c_1|/2$ and the finitely needed logarithmic
moments converge. Since $|f_m|\le\|f\|_S w_m^{-1/2}\ll m$,
induction gives $|g_m|\le C m^a$. Its Mellin series converges on a
sufficiently far right half-plane and equals $f/Q$ by absolute
convergence and (5.1). The same is true for the formal product
$Q^{(k)}g$ and the analytic function $h_k$.

We use the shifted estimate from [1, Lemma 8.8]. If such a formal step
function $h$ has analytic Mellin transform $H$ with
$\sup_{\sigma\ge1/2+\epsilon}\int|H(\sigma+it)|^2dt
\le\mathcal M_H(\epsilon)$, then
$$
\sum_{m\le X}|h_m|^2w_m
\le\frac{(X+1)^{2\epsilon}}{2\pi}\mathcal M_H(\epsilon).
                                                                    \tag{5.2}
$$
Indeed $H(\cdot+\epsilon)\in H^2$ has an inverse Mellin transform
in $L^2(0,1)$. Its transform agrees, in a far right half-plane, with
that of $u^\epsilon h(u)$. Uniqueness, after a sufficiently far right
integrable weight if needed, identifies the functions. On
$u\ge1/(X+1)$ one has $u^{-2\epsilon}\le(X+1)^{2\epsilon}$,
which proves (5.2). We have not assumed $g\in S$.

Take $\epsilon=1/L$. For $X\le C e^{(5/2)L}$, (4.1) and (5.2) imply
$$
                        \|E_Xg\|_S\ll_{Q,f}L^D,             \tag{5.3}
$$
where $E_X$ denotes the hard cutoff on indices $m\le X$.
For each fixed $k\ge1$, (4.2) gives the corresponding smallness
$L^{-2k}\mathcal M_k(1/L)\to0$.

### 5.2. A finite Taylor expansion with explicit coefficients

Choose $\chi\in C^\infty(\mathbb R)$ with $0\le\chi\le1$, equal
to one on $(-\infty,1]$ and zero on $[2,\infty)$. Set
$$
(C_Lg)_m=\chi(\log m/L)g_m,
\qquad (C_{k,L}h)_m=\chi^{(k)}(\log m/L)h_m.                  \tag{5.4}
$$
For one dilation, the commutator coefficient is
$$
([D_n,C_L]g)_m=g_{\lfloor m/n\rfloor}
\left[\chi\left(\frac{\log\lfloor m/n\rfloor}{L}\right)
-\chi\left(\frac{\log m}{L}\right)\right]                    \tag{5.5}
$$
when $m\ge n$, and zero otherwise. If $m\le e^L$, both the difference
and all derivative cutoff terms vanish. On the remaining range,
provided $e^L\ge2n$,
$$
\left|\log\lfloor m/n\rfloor-(\log m-\log n)\right|
\le C n/m\le C n e^{-L}.                                   \tag{5.6}
$$
Taylor expansion at $x=\log m/L$ gives
$$
\chi(x-\log n/L)-\chi(x)
=\sum_{k=1}^D\frac{\chi^{(k)}(x)}{k!L^k}(-\log n)^k
+O_D\big(L^{-D-1}(\log n)^{D+1}\big).                       \tag{5.7}
$$
Together with (5.6), the scalar remainder is bounded by
$$
C_D L^{-D-1}(\log n)^{D+1}+C L^{-1}n e^{-L}.                \tag{5.8}
$$
It vanishes above $m\ge n(e^{2L}+1)+2$. Thus its norm on a formal
input is bounded by (5.8) times $n^{-1/2}$ times the input's truncated
norm, using the exact weight identity (3.1).

## 6. Infinite tails and completion of the proof

Put
$$
H=\lfloor e^{L/2}\rfloor,\qquad
Q_H=\sum_{n\le H}c_nD_n,\qquad T_H=Q-Q_H.                   \tag{6.1}
$$
For every fixed $0\le k\le D$,
$$
\|T_H^{(k)}\|_{S\to S}
\le\sum_{n>H}|c_n|n^{-1/2}(\log n)^k
\ll_{Q,\eta,k}H^{-\eta/2}
\ll_{Q,\eta,k}e^{-\eta L/4}.                               \tag{6.2}
$$
This follows by writing the summand with the weight in (1.3) and
using $(\log n)^k n^{-\eta}\ll_{\eta,k}n^{-\eta/2}$.

The formal input $g$ need not have a global $S$ norm. Nevertheless,
$$
C_{k,L}T_H^{(k)}g=C_{k,L}T_H^{(k)}E_{e^{2L}+1}g,             \tag{6.3}
$$
including $k=0$ with $C_{0,L}=C_L$. The left cutoff restricts output
to $m\le e^{2L}$, and each input index $\lfloor m/n\rfloor$ is no
larger. The other tail term satisfies
$\|T_HC_Lg\|\le\|T_H\|\|C_Lg\|$. Hence (5.3), (6.2) and (6.3)
give
$$
\|[T_H,C_L]g\|_S+
\sum_{k=1}^D L^{-k}\|C_{k,L}T_H^{(k)}g\|_S
\ll_{Q,f}e^{-\eta L/4}L^D\longrightarrow0.                  \tag{6.4}
$$
All expressions here are well defined: $C_Lg$ is finite, and the
left cutoffs of formal tail products have finitely many coefficients.

For the growing finite part, sum the single-dilation norm bounds
(5.8) with weights $|c_n|n^{-1/2}$ before estimating them. The logarithmic
moment $\sum_n|c_n|n^{-1/2}(\log n)^{D+1}$ is finite by (1.3).
For the floor term use $n\le H\le e^{L/2}$. The triangle inequality
therefore gives
$$
\begin{aligned}
&\left\|[Q_H,C_L]g-
\sum_{k=1}^D\frac{L^{-k}}{k!}C_{k,L}Q_H^{(k)}g\right\|_S\\
&\qquad\le C_Q\big(L^{-D-1}+L^{-1}e^{-L/2}\big)
\|E_{H(e^{2L}+1)+2}g\|_S\\
&\qquad\ll_{Q,f}L^{-1}+L^{D-1}e^{-L/2}\longrightarrow0.
\end{aligned}                                                   \tag{6.5}
$$
The largest input cutoff is $O(e^{(5/2)L})$, so (5.3) applies.
This avoids importing a fixed-polynomial constant that might grow
uncontrolled with $H$.

Combining (6.4) and (6.5), and restoring the full derivatives
$h_k=Q^{(k)}g$, yields
$$
[Q,C_L]g=
\sum_{k=1}^D\frac{L^{-k}}{k!}C_{k,L}h_k+o_S(1).              \tag{6.6}
$$
By (4.2) and (5.2),
$$
\|L^{-k}C_{k,L}h_k\|_S^2
\le C_{Q,k}L^{-2k}\mathcal M_k(1/L)\longrightarrow0          \tag{6.7}
$$
for every $1\le k\le D$. There are finitely many terms. Since
$Qg=f$ formally, we conclude that $QC_Lg-C_Lf\to0$ in $S$.
Dominated convergence also gives $C_Lf\to f$. Each $C_Lg$ belongs
to $S$, and $Q$ preserves $S$, so $f\in\overline{QS}$. The reverse
inclusion was noted after (1.2). This proves Theorem 1.1.

For a finite polynomial the tail in (6.1) eventually vanishes. One may
instead retain its fixed support from the start; the squared Taylor
remainder is then $O(L^{-2}+e^{-2L}L^{2D-2})$. This recovers all finite
polynomials directly, including the repeated factors and symbols with
three or more prime variables left outside [1, Theorem 8.9].

## 7. Scope: two generators and the zeta problem

Principal-range synthesis does not assert synthesis for arbitrary
multiplier-invariant subspaces. The following elementary example makes
that distinction concrete. Its multiplicative-eigenvector mechanism is
the step-space counterpart of the published construction in Calderaro,
Manzur, Noor and Santos [4, Proposition 22]; we do not claim that mechanism
as new.

Let
$$
a(n)=(-1)^{v_3(n)}n^{-2},\qquad
\mathcal L_a(f)=\sum_{m\ge1}f_m\big(a(m)-a(m+1)\big).        \tag{7.1}
$$
This defines a bounded functional on $S$, since
$$
\sum_m\frac{|a(m)-a(m+1)|^2}{w_m}
\le8\sum_m m^{-2}<\infty.                                 \tag{7.2}
$$
Also $\mathcal L_a(E)=1$ by telescoping, where $E$ is the constant
function on $(0,1)$, with Mellin transform $1/s$. From
$D_ne_m=\sum_{j=nm}^{n(m+1)-1}e_j$ and complete multiplicativity,
$$
                         \mathcal L_a(D_nf)=a(n)\mathcal L_a(f)
                                                                    \tag{7.3}
$$
first for finite step sequences, then for all $f\in S$ by continuity.

Take
$$
                  P_1(s)=1-4\,2^{-s},\qquad
                  P_2(s)=1+9\,3^{-s}.                        \tag{7.4}
$$
Both multipliers annihilate the functional, since $a(2)=1/4$ and
$a(3)=-1/9$. Therefore
$$
\overline{P_1S+P_2S}\subseteq\ker\mathcal L_a\ne S.           \tag{7.5}
$$
Yet $P_1$ and $P_2$ have no common zero. A common zero would have
real part 2 and satisfy $t\log2\in2\pi\mathbb Z$ and
$t\log3\in(2\mathbb Z+1)\pi$, contradicting irrationality of
$\log3/\log2$. This is consistent with Theorem 1.1: each individual
range is determined by its own infinite zero set, while the sum is not
determined by a common-zero set alone.

For the original RH task, the Báez-Duarte subspace is generated through
zeta, and the needed infinite-zero synthesis remains open. Zeta does
not satisfy (1.3), is not a bounded multiplier of $S$, and does not
supply the compact analytic translate family used in Section 3. Nothing
here gives uniform constants as $\eta\downarrow0$, as the coefficient
norm in (1.3) grows, or along polynomial approximations to zeta.

Even an analytic Dirichlet multiplier vanishing on all hypothetical
off-line zeta zeros would leave additional tasks: constructing enough
such multipliers and proving the required bounds for their quotients
by zeta. These are separate requirements in [1, Section 8]. Theorem 1.1
does not establish them. It resolves the principal-range problem for
the stated regularity class and supplies an approximation mechanism
inside the original discrete space.

## 8. Common eigenfunctionals in the zeta annihilator

The example in Section 7 uses a common eigenfunctional that is not a
half-plane evaluation. We now show that such additional characters do
not survive in the annihilator of the zeta subspace $V$ defined in
Theorem 1.2. This uses the published rigidity theorem of Klurman [5,
Theorem 1.8], which resolves Kátai's conjecture in the following form:
for a complex multiplicative function $F$, if
$$
\frac1x\sum_{n\le x}|F(n+1)-F(n)|\longrightarrow0,            \tag{8.1}
$$
then either $x^{-1}\sum_{n\le x}|F(n)|\to0$ or $F(n)=n^z$
for some $\Re z<1$. This statement applies to general complex values;
no boundedness or unimodularity assumption is required. We use that
published theorem as an input.

**Lemma 8.1.** Let $\lambda(1)=1$ be completely multiplicative and
$\Delta\lambda(n)=\lambda(n+1)-\lambda(n)\in\ell^2$.
Then either $\lambda(n)=n^z$ with $\Re z<1/2$, or
$$
                         \sum_{n\ge1}\frac{|\lambda(n)|}{n}<\infty.
                                                                    \tag{8.2}
$$
The alternatives need not be disjoint.

*Proof.* Fix $0<\delta<1/2$, for example $\delta=1/4$, and put
$F(n)=n^\delta\lambda(n)$. Cauchy's inequality gives
$|\lambda(n)|\le1+\sqrt n\,\|\Delta\lambda\|_2\ll\sqrt n$.
Since
$$
\Delta F(n)=(n+1)^\delta\Delta\lambda(n)
 +\big((n+1)^\delta-n^\delta\big)\lambda(n),
$$
we have
$$
\sum_{n\le x}|\Delta F(n)|
\ll_\delta x^{\delta+1/2}=o(x).                             \tag{8.3}
$$
Apply (8.1). If $F(n)=n^w$, then $\lambda(n)=n^{w-\delta}$.
For a nonzero exponent $z=w-\delta$,
$\Delta n^z\sim z n^{z-1}$, so square summability implies
$\Re z<1/2$; $z=0$ also satisfies that inequality.
Otherwise
$$
B(x):=\sum_{n\le x}n^\delta|\lambda(n)|=o(x),
$$
and in particular $B(x)\ll x$. On a dyadic block,
$$
\sum_{2^j\le n<2^{j+1}}\frac{|\lambda(n)|}{n}
\le2^{-j(1+\delta)}B(2^{j+1})\ll2^{-j\delta}.
$$
Summing proves (8.2). $\square$

*Proof of Theorem 1.2.* Let $\Phi$ be a nonzero continuous common
multiplier eigenfunctional on $S$:
$$
                    \Phi(D_nf)=\chi(n)\Phi(f).               \tag{8.4}
$$
The vector $E=1/s$ is cyclic for all $D_n$, because
$e_m=D_mE-D_{m+1}E$. Hence $\Phi(E)\ne0$; normalize it to 1.
The identities $D_aD_b=D_{ab}$ and $D_1=I$ make $\chi$ completely
multiplicative, with $\chi(1)=1$. The norm in (3.1) implies
$|\chi(n)|\le n^{-1/2}$. Moreover,
$$
\Phi(e_m)=\chi(m)-\chi(m+1),\qquad
\sum_m m(m+1)|\chi(m)-\chi(m+1)|^2<\infty.                  \tag{8.5}
$$
The second assertion is Riesz duality in the weighted sequence space.

Since $\chi(n)\to0$, the discrete Hardy inequality gives
$$
\sum_n|\chi(n)|^2\le4\sum_n n^2|\Delta\chi(n)|^2<\infty.     \tag{8.6}
$$
One direct justification uses
$\chi(n)=-\sum_{k\ge n}\Delta\chi(k)$, whose weighted Cauchy bound
shows $n|\chi(n)|^2\to0$. Finite summation by parts for
$\sum_{n\le M}|\chi(n)|^2$, followed by Cauchy's inequality, bounds
this sum by twice the square root of itself times the square root of
the energy in (8.6), up to a vanishing boundary term. Taking the limit
gives (8.6).

Set $\lambda(n)=n\chi(n)$. Then $\lambda$ is completely multiplicative,
and
$$
\Delta\lambda(n)=n\Delta\chi(n)+\chi(n+1)\in\ell^2.
$$
Lemma 8.1 implies either $\chi(n)=n^{-s}$ for $\Re s>1/2$, or
$\chi\in\ell^1$. This is the original-step-space counterpart of the
common-eigenvector construction in [4, Proposition 22], supplemented by
the rigidity input (8.1). In the geometric case, (8.5) and (1.1) give
$$
                              \Phi(f)=s f(s),                \tag{8.7}
$$
first on $e_m$, then on all of $S$.

Suppose instead that $\chi\in\ell^1$. The step values of
$G_l(s)=(l^{-s}-l^{-1})\zeta(s)/s$ are
$\lfloor m/l\rfloor-m/l$. They are bounded. Summation by parts and
absolute convergence therefore give
$$
\begin{aligned}
\Phi(G_l)
 &=\sum_{n\ge1}\big(\mathbf1_{l\mid n}-1/l\big)\chi(n)\\
 &=(\chi(l)-1/l)Z_\chi,
\qquad Z_\chi=\sum_{n\ge1}\chi(n)=\prod_p(1-\chi(p))^{-1}.
\end{aligned}                                                   \tag{8.8}
$$
The Euler product is nonzero. Absolute summability implies
$|\chi(p)|<1$ for each prime, and $\sum_p|\chi(p)|<\infty$;
the product thus converges to a nonzero value. If $\Phi$ annihilates
$V$, (8.8) forces $\chi(l)=1/l$ for every $l\ge2$, contradicting
$\chi\in\ell^1$. This eliminates the nongeometric alternative.

For (8.7), if $s\ne1$ then
$$
                       \Phi(G_l)=(l^{-s}-l^{-1})\zeta(s).      \tag{8.9}
$$
If $\zeta(s)\ne0$, vanishing for $l=2,3$ would force both
$(s-1)\log2$ and $(s-1)\log3$ into $2\pi i\mathbb Z$, hence
$s=1$, a contradiction. At $s=1$ the removable value in (8.9) is
$-\log(l)/l\ne0$. Therefore $\zeta(s)=0$.
Conversely, evaluation at every zero of zeta in $\Omega$ is a bounded
common multiplier eigenfunctional and annihilates all the generators.
Undoing the normalization proves Theorem 1.2. $\square$

The new application is the reweighting in Lemma 8.1 and the exclusion of
its summable alternative on the zeta annihilator. The multiplicative
common-eigenvector construction [4] and Kátai rigidity [5] are credited
inputs. The ordinary classification alone does not treat generalized chains.
Section 9 classifies finite-dimensional invariant subspaces, but neither
argument proves that the eigenfunctionals and their jets span the
annihilator or that every nonzero closed invariant subspace contains one. Those
assertions do not follow from commutativity alone. Thus Theorem 1.2
identifies the ordinary common point obstructions without resolving RH.

## 9. Finite-dimensional invariant subspaces of the annihilator

Write $S'$ for the continuous complex-linear dual and
$V^\circ=\{\Phi\in S':\Phi|_V=0\}$. Define
$$
T_n\Phi=\Phi\circ D_n.
$$
These are transposes acting on linear functionals, so no conjugation is
used in their eigenvalues. The identity
$D_nG_l=G_{nl}-G_n/l$ makes $V^\circ$ invariant under all $T_n$.
Theorem 1.3 classifies its finite-dimensional common invariant subspaces,
even when the set of off-line zeros is infinite. The following proof
uses no completeness assertion about $V^\circ$.

### 9.1. Additive rigidity and matrix-entry regularity

We first record an elementary consequence of the published rigidity
input (8.1).

**Lemma 9.1.** If $A:\mathbb N\to\mathbb C$ is completely additive and
$$
\frac1x\sum_{n\le x}|A(n+1)-A(n)|\longrightarrow0,
$$
then $A(n)=c\log n$ for some $c\in\mathbb C$.

*Proof.* The additive result is classical and is credited to Kátai and
Wirsing in the introduction of [5]. For completeness, it follows from
the already imported Theorem 1.8 there. First suppose $A$ is real-valued.
For every $u\in\mathbb R$, the function
$F_u(n)=\exp(iuA(n))$ is completely multiplicative, is unimodular, and
has mean absolute first difference tending to zero. Thus (8.1) gives
$F_u(n)=n^{it_u}$ for some real $t_u$; the small-average alternative
cannot occur. Comparing this identity at $2$ and at a fixed $n$ gives
$$
u\big(A(n)\log2-A(2)\log n\big)
\in2\pi\big(\mathbb Z\log2+\mathbb Z\log n\big).             \tag{9.1}
$$
The right side is countable. Since (9.1) holds for every real $u$, its
coefficient on the left must vanish. Therefore
$A(n)=A(2)\log n/\log2$. Apply the real case separately to the real and
imaginary parts of a complex $A$. No regularity of $u\mapsto t_u$ is
needed. $\square$

For any $\Phi\in S'$, define
$$
a_\Phi(n)=\Phi(D_nE).
$$
The norm of $D_n$ and the basis identity for $e_n$ give
$$
|a_\Phi(n)|\le\|\Phi\|n^{-1/2},\qquad
\sum_{n\ge1}n^2|\Delta a_\Phi(n)|^2<\infty.                 \tag{9.2}
$$
For every fixed integer $m\ge1$, the sequence $b(n)=a_\Phi(mn)$
has the same properties, with constants depending on $m$. Indeed,
$$
\begin{aligned}
\sum_n n^2|b(n+1)-b(n)|^2
&\le m\sum_n n^2\sum_{j=mn}^{mn+m-1}|\Delta a_\Phi(j)|^2\\
&\le m^{-1}\sum_{j\ge m}j^2|\Delta a_\Phi(j)|^2.
\end{aligned}                                                   \tag{9.3}
$$
The integer intervals in the middle expression are disjoint.

Let $W\subseteq V^\circ$ be finite-dimensional and invariant under every
$T_n$. Since $E$ is cyclic, the linear functionals on $W$ given by
$\Phi\mapsto\Phi(D_mE)$ separate points. Finitely many of them therefore
span $W'$. In any fixed basis of $W$, every matrix entry $t(n)$ of
$T_n|_W$ is a fixed linear combination of sequences $a_\Phi(mn)$:
apply those finitely many coordinate measurements to $T_n\Phi$ and
invert their fixed coordinate matrix. Consequently,
$$
t(n)=O(n^{-1/2}),\qquad
\sum_n n^2|\Delta t(n)|^2<\infty                            \tag{9.4}
$$
for every such matrix entry. This step transfers continuity in $S'$ to
the entire finite representation, rather than only its characters.

### 9.2. The unipotent part is a polynomial in $\log n$

The finite-dimensional commutative algebra generated by the restrictions
$T_n|_W$ has the usual primary decomposition into finitely many common
generalized character blocks. This also applies to the countable family:
the generated algebra lies in the finite-dimensional space
$\operatorname{End}(W)$ and is generated as an algebra by finitely many
of its elements. Simultaneous triangularization on each primary block
gives a common eigenvector in that block. Theorem 1.2 therefore identifies
every character as
$$
\chi(n)=n^{-\rho},\qquad \zeta(\rho)=0,\qquad
1/2<\sigma:=\Re\rho<1.                                    \tag{9.5}
$$
Distinct $\rho$ give distinct characters, as is seen using $n=2,3$.

Fix one block $W_\rho$ of dimension $r$ and a simultaneous upper
triangular basis. Set
$$
U(n)=n^\rho T_n|_{W_\rho},\qquad N(n)=U(n)-I,
\qquad
L(n)=\log U(n)=\sum_{k=1}^{r-1}\frac{(-1)^{k+1}}kN(n)^k.     \tag{9.6}
$$
The matrices $U(n)$ are commuting and unipotent; their $N(n)$ are
strictly upper triangular. All power series are finite in this
nilpotent algebra. Multiplicativity and the formal exponential and
logarithm identities give
$$
L(mn)=L(m)+L(n),\qquad U(n)=\exp L(n).                       \tag{9.7}
$$
Thus every matrix entry of $L(n)$ is completely additive.

Every entry of $U(n)$ has mean absolute first difference tending to
zero. To verify this, let $t(n)$ be its corresponding entry before
normalization. The product rule and (9.4) give
$$
\begin{aligned}
\sum_{n\le x}|\Delta(n^\rho t(n))|
&\le C_\rho\sum_{n\le x}n^\sigma|\Delta t(n)|
 +C_\rho\sum_{n\le x}n^{\sigma-1}|t(n)|\\
&\ll\left(\sum_n n^2|\Delta t(n)|^2\right)^{1/2}
       \left(\sum_{n\le x}n^{2\sigma-2}\right)^{1/2}
       +\sum_{n\le x}n^{\sigma-3/2}\\
&\ll x^{\sigma-1/2}=o(x).
\end{aligned}                                                   \tag{9.8}
$$
Here $1/2<\sigma<1$, and all constants may depend on the fixed block.

We now induct on the upper-diagonal offset $d=j-i$. For $d=1$,
$L_{ij}(n)=U_{ij}(n)$, so (9.8) and Lemma 9.1 give
$L_{ij}(n)=A_{ij}\log n$. Suppose this holds for all smaller offsets.
The identity $U=\exp L$ then makes every smaller-offset entry of $U$
a fixed polynomial in $\log n$. In the $(i,j)$ entry of (9.6), each
term of $N^k$ with $k\ge2$ uses only smaller offsets. Hence
$L_{ij}(n)-U_{ij}(n)$ is a fixed polynomial in $\log n$. The sum of
the absolute first differences of any such polynomial up to $x$ is
$O((1+\log x)^r)=o(x)$. Equation (9.8) and Lemma 9.1 again yield
$L_{ij}(n)=A_{ij}\log n$. This completes the induction, giving
$$
L(n)=A\log n,\qquad
T_n|_{W_\rho}=n^{-\rho}\exp(A\log n),                        \tag{9.9}
$$
where $A$ is a fixed nilpotent matrix. In particular no independent
additive parameters at the primes remain in a finite block.

### 9.3. Identification and the exact multiplicity bound

For $\Phi\in W_\rho$, equation (9.9) shows that
$$
\Phi(D_nE)=n^{-\rho}p_\Phi(\log n),\qquad
\deg p_\Phi\le r-1.                                       \tag{9.10}
$$
The continuous functionals $(-\partial_\rho)^k[\rho\operatorname{ev}_\rho]$
take the values $(\log n)^kn^{-\rho}$ on $D_nE$. Cyclicity of $E$
therefore identifies every $\Phi\in W_\rho$ with a linear combination
of these functionals. Since $\rho\ne0$, their span is the same as
$$
\operatorname{span}\{\operatorname{ev}_\rho,
\operatorname{ev}'_\rho,\ldots,
\operatorname{ev}^{(r-1)}_\rho\}.                            \tag{9.11}
$$
Here $\operatorname{ev}^{(k)}_\rho(f)=f^{(k)}(\rho)$.

These jets are linearly independent on $S$: a relation tested on all
$D_nE=n^{-s}/s$ gives a polynomial in $\log n$ vanishing for all $n$,
whose highest coefficient is a nonzero multiple of the highest jet
coefficient. The polynomial and then every coefficient must vanish.

Let $q$ be the largest derivative order occurring in $W_\rho$. For
fixed $n>1$, the operator $T_n-n^{-\rho}I$ lowers that order by exactly
one: on $\operatorname{ev}^{(k)}_\rho$ its highest remaining coefficient
is $-k(\log n)n^{-\rho}\operatorname{ev}^{(k-1)}_\rho$. Applying its
successive powers to an element with nonzero order-$q$ coefficient
produces $q+1$ independent elements of $W_\rho$. Thus
$$
W_\rho=\operatorname{span}\{\operatorname{ev}_\rho,
\ldots,\operatorname{ev}^{(q)}_\rho\}.                       \tag{9.12}
$$
If $q\ge m=m_\zeta(\rho)$, this subspace contains
$\operatorname{ev}^{(m)}_\rho$, but
$$
G_2^{(m)}(\rho)
=\frac{2^{-\rho}-1/2}{\rho}\zeta^{(m)}(\rho)\ne0,            \tag{9.13}
$$
contradicting $W_\rho\subseteq V^\circ$. The coefficient is nonzero
since $\Re\rho<1$. Hence $q<m$. Conversely, all jets of orders less
than $m_\zeta(\rho)$ annihilate every $G_l$, and their initial chains
are invariant under $T_n$ by Leibniz's formula. Primary decomposition
now proves Theorem 1.3. $\square$

This classifies finite-dimensional invariant subspaces, equivalently
the vectors whose joint dilation orbit spans a finite-dimensional
subspace of $V^\circ$. It does not show that these vectors are dense
in $V^\circ$, or that every nonzero closed invariant subspace contains
one. For finitely many off-line zeros, [1] already proves the stronger
equality of $V$ with the complete zero-jet kernel. The new finite-block
classification applies without assuming that the off-line set is finite;
the infinite-dimensional completeness question remains open.

## 10. Verification and reproducibility

The proofs are analytic. Theorems 1.2 and 1.3 use the published rigidity
input and exact functional and matrix calculations, with no numerical claim. No finite
computation certifies the compact-family
estimates, Hardy limits or infinite-dimensional conclusion. The supplement
provides one finite structural checker using Python 3 and mpmath, with
100 decimal digits. From the supplement root run

```bash
python experiments/revival1231_derivative_cutoff_check.py
```

It writes `results/revival1231_derivative_cutoff_check.json` and tests:

- 117 product-derivative identities, with repeated roots and close clusters;
- 288 Blaschke-reflection inequalities for selected root subsets;
- 33 full polynomial-cutoff identities, including a three-prime support;
- 180 floor-error bounds and 180 Taylor-remainder bounds;
- 33 wrong-sign and three uncanceled-interior-pole negative controls.

All pass. The preliminary 75-digit run left a residual of about
$7.6\cdot10^{-57}$ in an exactly zero derivative sum after cancellation
of large terms; the 100-digit run resolves this loss against the stated
$10^{-70}$ tolerance. The theorem does not rely on that numerical
precision choice. The polynomial cutoff used in the finite checker has
the finite smoothness needed for the tested orders; the analytic proof
chooses a smooth cutoff with all derivatives available.

The supplement includes the code, saved result, dependency versions,
reproduction instructions and file hashes. The infinite-series extension
uses the explicit tail bounds (6.2)–(6.5), with no additional numerical
claim. The example (7.4) is verified by the exact functional and
irrationality argument in Section 7.

Original code and supplemental text are released under CC0-1.0.
Third-party manuscripts are referenced, not bundled. The original
step-space quotient method and factorization are credited to [1],
logarithmic reciprocal cutoffs to [2], the related multidisc cyclicity
criterion to [3], the common-eigenvector mechanism to [4], and the multiplicative rigidity
theorem to [5].

## References

[1] span_of_dilates. *The Báez-Duarte subspace has codimension equal to the
number of zeta zeros off the critical line, with distance and rate bounds
not assuming RH*. rStation, Paper 1, version 6, 26 October 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/1/v6

[2] S. Bettin, J. B. Conrey and D. W. Farmer. *An optimal choice of
Dirichlet polynomials for the Nyman–Beurling criterion*. Sovrem. Probl.
Mat.16(2012),38–44; English translation in Proc. Steklov Inst. Math.(2013).
https://doi.org/10.1134/S0081543813030036

[3] N. Nikolski. *In a shadow of the RH: cyclic vectors of Hardy spaces
on the Hilbert multidisc*. Ann. Inst. Fourier62(2012),1601–1626.
https://doi.org/10.5802/aif.2731

[4] F. Calderaro, J. Manzur, W. Noor and C. Santos. *Orthogonality questions
in the Hardy space related to zeta-zeros*. arXiv:2203.05030v4(2024),
Proposition 22.
https://arxiv.org/abs/2203.05030v4

[5] O. Klurman. *Correlations of multiplicative functions and applications*.
Compositio Math.153(2017),1622–1657, Theorem 1.8.
https://doi.org/10.1112/S0010437X17007163
https://arxiv.org/abs/1603.08453

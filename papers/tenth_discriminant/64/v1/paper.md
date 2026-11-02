## 1. Finite derivative budgets in quadratic interpolation

Quadratic interpolation arguments for explicit discriminant bounds use a
nonzero minor of a matrix of pure Hasse derivatives. Its arithmetic lower
bound depends on how many derivatives are retained. The exact all-order
ghost index [1] and its digit basis [2] describe the lattice when
every derivative is available. The finite-jet analysis in [3]
determines a first saturation layer for the complementary slope range
$K\ge p^3$. Here we determine that layer in the middle chamber
$p<K\le p^3$, obtain the sharp budget at which the all-order lattice is
recovered, and construct stronger determinant bounds below that budget.

There are two parts to the improvement. An adapted basis separates
residue-digit information from the degree of the Taylor variables, making
the first saturation layer an exact count. A recursive Frobenius lift then
gives a valuation bound for each derivative column of one fixed row
polynomial. Retaining those column capacities, rather than replacing all
columns by the largest derivative charge, yields a sorted-assignment bound
for every selected minor. These are compatible descriptions of the same
finite-jet phenomenon; their overlapping gains are combined only in the
ways proved below.

The resulting arithmetic contribution is positive on the original
finite contracts of the closed-Charlier discriminant argument [4].
All 19 positive contracts and both negative controls are replayed with
their original support, nodes, rank test, radius, omitted columns,
Legendre factors and Archimedean majorant. Every normalized gap improves
by more than $0.00300057$, and the smallest positive gap exceeds
$0.02751401$. The comparison establishes an arithmetic improvement within
that method. It does not assert a new discriminant endpoint or repeat
the infinite-tail or classification computation of [4].

### 1.1. Local notation and imported structure

Let $p$ be a prime, let $\mathcal O$ be the ring of integers of the
unramified quadratic extension $F/\mathbb Q_p$, and let $\sigma$ be its
nontrivial automorphism. Write $v_p(p)=1$ and
$$
q=p^2,\qquad
\alpha(m)=\sum_{\ell\ge1}\left\lfloor\frac{m}{q^\ell}\right\rfloor.
$$
For positive integers $K,R$, put
$$
\Lambda=\{(r,s)\in\mathbb Z_{\ge0}^2:r+Ks<R\},\qquad
V_\Lambda=\bigoplus_{(r,s)\in\Lambda}Fz^rw^s,\qquad M=|\Lambda|.
$$
Hasse derivatives $\mathcal D_z^{(j)}$ always hold $w$ fixed; evaluation
uses the linked pair $(z,\sigma(z))$. Set
$$
I_J=\left\{f\in F[z,w]:
p^{\lfloor j/p\rfloor}\mathcal D_z^{(j)}f(z,\sigma(z))\in\mathcal O
\text{ for every }z\in\mathcal O,\ 0\le j<J\right\},
$$
and write $I=I_\infty$, $L=I\cap V_\Lambda$, and
$L_J=I_J\cap V_\Lambda$. These are lattices containing the ordinary
coefficient lattice $\mathcal O^\Lambda$. The weighted matrix has columns
$$
\mathsf A_{(r,s),(i,j)}=
p^{\lfloor j/p\rfloor}\binom rj z_i^{r-j}\sigma(z_i)^s,
\qquad 0\le j<J,
$$
with entry zero when $j>r$. Zero determinants have valuation $+\infty$.

We use the following precise results from [1, Lemmas 2 and 4,
Theorem 1] and [2, Lemma 3]. With $A=(z^p-w)/p$,
$$
I=\bigoplus_{0\le t<p}z^t\operatorname{Int}(\mathcal O)[A],
\qquad
\operatorname{Int}(\mathcal O)=\{f\in F[w]:f(\mathcal O)\subseteq\mathcal O\}.
$$
For $p<K\le p^3$, the all-order index is
$$
E_{p,K,R}=\operatorname{length}_{\mathcal O}(L/\mathcal O^\Lambda)
=\sum_{(r,s)\in\Lambda}e_{r,s},\qquad
e_{r,s}=s+\alpha(\lfloor r/p\rfloor).
$$
The same $E_{p,K,R}$ is the valuation of the universal maximal-minor
ideal for all weighted columns. It bounds every finite selected minor.

The holomorphic ghosts $X_n$ are defined by
$$
u=z^p=w+pA,\quad g_0=u,\quad g_n=w+pA^{q^{n-1}},\quad
g_n=\sum_{i=0}^np^iX_i^{q^{n-i}},\quad X_0=u.
$$
They belong to $I$; their leading monomials in the order $(r+Ks,r)$
are $z^{pq^n}$, and their leading coefficient valuations are
$-\nu_n$, where $\nu_n=(q^n-1)/(q-1)$. Their support has weight at
most $pq^n$. If $r=pH+t$, $0\le t<p$, and
$H=\sum a_nq^n$, $0\le a_n<q$, then
$$
\mathcal H_r=z^{pa_0+t}\prod_{n\ge1}X_n^{a_n}
$$
belongs to $I$, has support of weight at most $r$, and has leading
coefficient valuation $-\alpha(\lfloor r/p\rfloor)$ at $z^r$.
All derivative and support uses of the imported ghost basis below refer
to these statements. The equality case $K=p^3$ uses the indicated
secondary order.

### 1.2. Relation to prior work

The pure-conjugate integer-valued tower in [5, Lemma 4.3] is
already part of the complete local determinant comparison. We do not
claim that tower, the full ghost basis, or their all-order index as new.
The elementary finite lift $A^q-(w^q-w)/p$ also appeared in our earlier
public discussion [6]. The new arguments use its growing powers,
a coupling to the conjugate tower at a fixed Taylor radius, and the
resulting entrywise valuation profile. The exact first layer extends
[3, Proposition 7] to the other side of the boundary $K=p^3$.

Digit bases, regular bases and generalized factorials are classical
[7], [8]. Integer-valued derivatives and finite differences
have a substantial general theory [9]. The ghost-component
integrality criterion used in [1] is likewise classical [10].
Our claims concern their application to linked quadratic nodes, the
specific pure-Hasse prices $\lfloor j/p\rfloor$, and the original
weighted triangle. We do not identify these conditions with ordinary
derivative integrality or with the stronger divided-difference condition.
The sorted-assignment inequality itself is elementary and is proved
below; the new input to it is one row family's valuation profile.

The finite computations are author checks of the proofs and a replay of
published interval code. Independent mathematical review of the new
statements is pending. Earlier reviews of the imported results are not
treated as reviews of the present extensions.

## 2. Exact first saturation and the sharp cutoff

### 2.1. Statement

Let $\mathcal O$ be the integers in the unramified quadratic extension
of $\mathbb Q_p$, with nontrivial automorphism $\sigma$, and put $q=p^2$.
Let $I_J$ be the algebra of polynomials $f\in\operatorname{Frac}(\mathcal O)[z,w]$
such that
$$
p^{\lfloor j/p\rfloor}\mathcal D_z^{(j)}f(z,\sigma(z))\in\mathcal O
\quad(z\in\mathcal O,\ 0\le j<J).
$$
Here $\mathcal D^{(j)}$ is the Hasse derivative, holding $w$ fixed.
Write $I=I_\infty$. For positive integers $K,R$, let $V_\Lambda$ be
the polynomial space supported on
$$
\Lambda=\{(r,s)\in\mathbb Z_{\ge0}^2:r+Ks<R\},
\qquad L=I\cap V_\Lambda,\qquad L_J=I_J\cap V_\Lambda.
$$

**Theorem 1 (first saturation layer and exact cutoff).** Suppose $p<K\le p^3$ and $J\ge1$. Define
$$
\rho(r,s)=p^3\left\lfloor\frac{s}{q}\right\rfloor
 +\left(\left\lfloor\frac rq\right\rfloor\bmod p^3\right).
$$
Then
$$
\dim_{\mathbb F_q}\frac{L_J\cap p^{-1}L}{L}
=\#\{(r,s)\in\Lambda:\rho(r,s)\ge J\}.                 \tag{1}
$$
Writing $n=\lfloor(R-1)/q\rfloor$, one has
$$
L_J=L\quad\Longleftrightarrow\quad
J\ge J_{\rm sat}:=p^3\left\lfloor\frac nK\right\rfloor
 +(n\bmod K)+1.                                      \tag{2}
$$
For fixed $p,K$ and $R\to\infty$, $J_{\rm sat}/R\to p/K$. If
$J/R\to\varepsilon$, the expression in (1), divided by $|\Lambda|$,
tends to $(1-\varepsilon K/p)_+^2$.

### 2.2. Weighted Taylor coordinates and a basis

Use the integral Taylor ring $\mathcal O[t,T]/(t^p-pT)$. After substituting
$z\mapsto z_0+t$, the coefficient on
$t^{j\bmod p}T^{\lfloor j/p\rfloor}$ is precisely the priced Hasse
derivative. The full Taylor-coordinate theorem in [3, Proposition 7]
identifies the reduction of $I$ with $C_0[t,T]/(t^p)$, where $C_0$ is
the algebra of locally constant $\mathbb F_q$-valued functions on
$\mathcal O$. This uses conjugate nodes throughout.

Put
$$
H=z^q-z,\qquad V=H^p/p,\qquad A=(z^p-w)/p,
\qquad C=(w^q-w)/p,\qquad g=A^q-C.
$$
All five polynomials belong to $I$. Their reduced weighted Taylor images are
$$
\begin{aligned}
H&\mapsto-t,&V&\mapsto(-1)^pT,&g&\mapsto T^q,\\
z&\mapsto z_0+t,&A&\mapsto d_1+B(z_0,t)+T,
\end{aligned}                                                     \tag{3}
$$
where $d_1=C\bmod p$ and
$$
B(z_0,t)=\sum_{j=1}^{p-1}\frac1p\binom pj z_0^{p-j}t^j.
$$
The identities for $H,V$ are proved in [3]. For completeness,
$H(z_0+t)=-t+pE$ in the integral Taylor ring; expanding $H^p/p$ leaves
only $(-1)^pT$ modulo $p$, including when $p=2$. The identity for $A$
is its direct binomial expansion. Raising it to $q$ gives the identity
for $g$, since $d_1^q=d_1$ and $B^q=0$.

Let $X_n$, $n\ge2$, be the ghosts of [1, Section 4]. In the weighted
order $(r+Ks,r)$ their leading monomials are $z^{pq^n}$, their
leading coefficients have valuations $-\nu_n$, where
$\nu_n=(q^n-1)/(q-1)$, and their entire support has weight at most
$pq^n$. By [2, Lemma 3], their reduced Taylor images have the form
$$
X_n\mapsto\kappa_nd_n+F_n(d_0,\ldots,d_{n-1},t,T),
\qquad \kappa_n\in\mathbb F_q^\times.                 \tag{4}
$$
Here $d_i$ are the successive residue-digit functions from that lemma.

Write, uniquely,
$$
\begin{aligned}
r&=e+qk+pqh+\sum_{n\ge2}pq^na_n,
 &0\le e<q,\quad0\le k<p,\quad0\le h<q,\quad0\le a_n<q,\\
s&=qu+b,&0\le b<q.
\end{aligned}
$$
Define
$$
f_{r,s}=z^eH^kV^hg^uA^b\prod_{n\ge2}X_n^{a_n}.       \tag{5}
$$
Every factor belongs to $I$. Since $K>p$, the leading monomial of
$p^qg=(z^p-w)^q-p^{q-1}(w^q-w)$ is $w^q$, with unit coefficient
$(-1)^q-p^{q-1}$. The leading monomials of $pA,H,pV$ are respectively
$-w,z^q,z^{pq}$. The ghost support bound applies since $K\le p^3$;
the specified secondary order handles equality. Thus $f_{r,s}$ has
leading monomial $z^rw^s$ and preserves its original weighted support.
Its leading-coefficient valuation is
$$
-s-h-\sum_{n\ge2}\nu_na_n
=-s-\alpha(\lfloor r/p\rfloor),\qquad
\alpha(m)=\sum_{\ell\ge1}\lfloor m/q^\ell\rfloor.     \tag{6}
$$
The equality follows from the base-$q$ digits of $\lfloor r/p\rfloor$.
The rows (5) for $(r,s)\in\Lambda$ belong to $L$, form a basis of
$V_\Lambda$ over its fraction field, and have total leading determinant
valuation equal to the full lattice index of [1, Theorem 1]. Index
equality therefore makes them an $\mathcal O$-basis of $L$. This step
uses actual lattice membership; integral polynomial coefficients are
not required.

### 2.3. Independence after truncation

Up to a nonzero scalar, the reduced image of (5) is
$$
t^kT^{h+qu}(z_0+t)^e(d_1+B+T)^b
 \prod_{n\ge2}(\kappa_nd_n+F_n)^{a_n}.                 \tag{7}
$$
Let
$$
S_J=\mathbb F_q[t,T]/
 (t^p,\ t^kT^m:0\le k<p,\ pm+k\ge J).
$$
At any finite residue-digit level, the monomials
$z_0^ed_1^b\prod d_n^{a_n}$, with each exponent below $q$, form a basis
of the digit-function algebra. Indeed, $z_0$ is the Frobenius permutation
of $d_0$, and [2, Section 4] proves independence of the digit functions.

Over $S_J$, replace successively $z_0$ by $z_0+t$, $d_1$ by $d_1+B+T$,
and $d_n$ by $\kappa_nd_n+F_n$. These are invertible changes of the
finite module basis. To see this, expand in the highest digit and descend:
every exponent is below $q$, each diagonal coefficient is a unit, and
each lower coefficient uses only earlier digits and $t,T$. This is a
module-basis assertion; it does not require the substitution to preserve
the defining relations of the digit-function algebra as an algebra map.

The monomials $t^kT^m$ with $pm+k<J$ form an $\mathbb F_q$-basis of
$S_J$. Their products with the changed digit basis are consequently
independent. In (7), $m=h+qu$ and
$$
pm+k=p^3u+ph+k=\rho(r,s).
$$
The labels are distinct. Hence exactly the rows with $\rho\ge J$
vanish after truncation, and all other rows remain independent. This
holds for arbitrary subsets, including partial residue blocks at the
triangle boundary. The kernel of $L/pL$ under truncated Taylor
evaluation thus has dimension (1). The map $f\mapsto f/p$ identifies
this kernel with $(L_J\cap p^{-1}L)/L$.

### 2.4. Sharp saturation threshold

The lattice $L_J$ contains $L$ with finite index. To justify finite
index, evaluations alone separate this polynomial space: writing
$z=x+y\theta$ and $w=x+y\sigma(\theta)$ gives an invertible linear
substitution in two independent $\mathbb Q_p$ coordinates. A nonzero
polynomial cannot vanish on all $\mathbb Z_p^2$, and a finite spanning
set of evaluation functionals therefore exists. Thus $L_J/L$ is a
finite module. If it is nonzero, it has a nonzero element annihilated
by $p$. Vanishing of the first saturation layer is consequently
equivalent to $L_J=L$.

To maximize $\rho$, delete $e,b$ and all $a_n$ in the decomposition
above: they increase the weight without changing $\rho$. Set
$\ell=ph+k\in[0,p^3-1]$. The remaining constraint is
$\ell+Ku\le n$, and the objective is $\ell+p^3u$. Its maximum is
$$
p^3\lfloor n/K\rfloor+(n\bmod K).
$$
Indeed, this is attained at $u=\lfloor n/K\rfloor$ and
$\ell=n\bmod K$, which is allowed since $K\le p^3$. For every other
pair, $\ell+p^3u\le n+(p^3-K)u$, proving the upper bound. Formula (2)
follows.

At $K=p^3$, (2) becomes $J_{\rm sat}=\lfloor(R-1)/q\rfloor+1$,
agreeing with [3]. The entire first-layer counts agree there too:
writing $r=e+qk+pqh+pq^2v$ and $s=b+qu$, the exchange $u\leftrightarrow v$
preserves the triangular weight and exchanges the two cutoff statistics
$\rho(r,s)$ and $\lfloor r/q\rfloor$. Finally,
$\rho(r,s)=ps+O_p(1)$ uniformly in $r,s$. Counting the part of the
triangle above $s=J/p+O_p(1)$ gives the claimed limit in (1).

### 2.5. Exact controls and limitations

The supplied checker evaluates and differentiates the original local
polynomial generators at conjugate nodes, then performs elimination
over $\mathbb F_{p^2}$. It passes 44,046 generator-coordinate checks
and 33 finite-field rank checks on eight triangles at $p=2,3$, including
$X_2$ at $p=2$ and the boundary $K=p^3$. There are also 1,492 exact
threshold checks and 214 boundary-multiset comparisons. Finite node
sets certify the lower ranks; universal vanishing and completeness are
proved above. These are author controls, not an independent proof review.

This theorem determines one saturation layer and the exact equality
threshold. It does not determine the deeper finite index below that
threshold. The growing-power lower bound of Section 3 is a different
statement: its credit already includes some of this layer.
Adding the two gains without an overlap argument would be invalid.
No new discriminant endpoint, census, or class-number-one classification
is asserted, and no metric or infinite-tail certificate is recomputed.



## 3. Recursive Frobenius lifts and uniform minor bounds

### 3.1. Recursive lift and local valuation

Let $\mathcal O$ be the unramified quadratic DVR at a prime $p$, and
let $w=\sigma(z)$ at evaluation nodes. Write
$$
q=p^2,\quad A=\frac{z^p-w}{p},\quad
\delta(x)=\frac{x^q-x}{p},\quad D_n(w)=\delta^{\circ n}(w),\quad
\nu_n=\frac{q^n-1}{q-1},\quad\nu_0=0.
$$
Define polynomials in $A,w$ by
$$
G_0=A,\qquad
G_n=G_{n-1}^q-p^{q\nu_{n-1}}D_n(w),\quad n\ge1.     \tag{8}
$$
The first level is the earlier finite lift $G_1=A^q-D_1(w)$ [6].
Each $D_n$ is integer-valued on $\mathcal O$. Hence every $G_n$ belongs
to $\operatorname{Int}(\mathcal O)[A]$, and thus to the full algebra
of integral weighted Hasse jets by [1, Lemma 2].

**Lemma 2 (fixed-radius valuation).** At every conjugate node, with Hasse derivatives holding
$w$ fixed, one has for all $n,j\ge0$
$$
v_p\bigl(\mathcal D_z^{(j)}G_n\bigr)
 +\frac{pj}{q-1}\ge\nu_n.                           \tag{9}
$$

**Proof.** Put $A_0=A(z_0,\sigma(z_0))$ and
$a_n=G_n(A_0,w)/p^{\nu_n}$. Then
$$
a_n\in\mathcal O,\qquad a_n\equiv D_{n+1}(w)\pmod p. \tag{10}
$$
For $n=0$, the congruence $A_0\equiv D_1(w)\pmod p$ is the elementary
quadratic Frobenius identity used in [6]. Explicitly,
$w^p\equiv z_0\pmod p$ implies $w^q\equiv z_0^p\pmod{p^2}$.
For the induction, (8) and $\nu_n=q\nu_{n-1}+1$ give
$$
a_n=\frac{a_{n-1}^q-D_n(w)}p.
$$
If $a_{n-1}\equiv D_n(w)\pmod p$, their $q$th powers agree modulo
$p^2$. Division proves (10).

For a polynomial in an increment $X$, use the Gauss valuation giving
$X$ weight $a=1/(q-1)$. We prove the stronger pair of statements
$$
\begin{aligned}
v_p(G_n(A_0,w))&\ge\nu_n,\\
v_{\rm G}\bigl(G_n(A_0+X,w)-G_n(A_0,w)\bigr)&\ge\nu_n+a.
\end{aligned}                                                     \tag{11}
$$
The constant statement is (10), and the other statement is immediate
at $n=0$. Write $G_{n-1}(A_0+X,w)=c+Y$. The $k$th term in the
nonconstant part of $(c+Y)^q$ has Gauss valuation at least
$$
q\nu_{n-1}+ka+v_p\binom qk.
$$
When $1\le k<q$, the binomial coefficient is divisible by $p$, so
this is at least $q\nu_{n-1}+1+a=\nu_n+a$. For $k=q$, use
$qa=1+a$. The correction in (8) is constant in $X$, proving (11).

Now give an ordinary $z$ increment $y$ weight $\lambda=p/(q-1)$.
Its induced $A$ increment is
$$
\Delta A=\sum_{j=1}^{p-1}\frac1p\binom pj z_0^{p-j}y^j
 +\frac{y^p}{p}.
$$
Every term has valuation at least $a$: $\lambda\ge a$ and
$p\lambda-1=a$. Substitution in (11) is therefore valid. The whole
Taylor polynomial of $G_n$ has Gauss valuation at least $\nu_n$,
which is exactly (9). This proof includes $p=2$. $\square$

### 3.2. Original support and finite derivative charge

**Lemma 3 (support).** For $K>p$, the polynomial $p^{q^n}G_n(z,w)$ has integral
coefficients, weighted degree at most $Kq^n$ for weights $(1,K)$,
and leading monomial $w^{q^n}$ with a $p$-adic unit coefficient.

**Proof.** Write $E_n=p^{\nu_n}D_n(w)$. Its recurrence is
$$
E_0=w,\qquad E_n=E_{n-1}^q-p^{(q-1)\nu_{n-1}}E_{n-1}.
$$
Thus $E_n$ is integral and monic of degree $q^n$. Setting
$P_n=p^{q^n}G_n$ gives the integral recurrence
$$
P_0=z^p-w,\qquad P_n=P_{n-1}^q-p^{q^n-1}E_n(w).     \tag{12}
$$
The leading coefficient of the first term is a unit, while the
correction's leading coefficient is divisible by $p$. The degree
bound follows inductively from $K>p$. $\square$

Write $s=\sum_{n\ge0}b_nq^n$, with $0\le b_n<q$, and put
$F_s=\prod G_n^{b_n}$. Its leading coefficient is a unit times $p^{-s}$,
its support lies below $w^s$, and Lemma 2 gives Gauss valuation at
least
$$
\sum b_n\nu_n=\alpha(s),\qquad
\alpha(s)=\sum_{\ell\ge1}\left\lfloor\frac{s}{q^\ell}\right\rfloor.
$$
Suppose now $p<K\le p^3$. Multiply $F_s$ by the holomorphic ghost row $\mathcal H_r$ of Section 1.1 with leading monomial $z^r$ and leading
denominator valuation $\alpha(\lfloor r/p\rfloor)$. That row belongs
to the full weighted-jet algebra and has nonnegative Gauss valuation
at $\lambda\ge1/p$. The product has all-order priced coefficients
integral and, by Lemma 2, additional credit at derivative order $j$ of
at least
$$
\alpha(s)-\left\lceil\frac{pj}{q-1}\right\rceil
 +\left\lfloor\frac jp\right\rfloor.                \tag{13}
$$

Define the exact finite charge
$$
C_p(J)=\max_{0\le j<J}\left(
\left\lceil\frac{pj}{q-1}\right\rceil
-\left\lfloor\frac jp\right\rfloor\right).           \tag{14}
$$
Writing $J-1=pH+B$, $0\le B<p$, it is
$$
C_p(J)=\left\lceil\frac{\max\{H+pB,\ H-1+p(p-1)\}}{q-1}\right\rceil
\quad(H\ge1),                                       \tag{15}
$$
and $C_p(J)=\lceil pB/(q-1)\rceil$ when $H=0$. Indeed, for
$j=ph+b$ the expression in (14) is $\lceil(h+pb)/(q-1)\rceil$.
Only the last partial block and the preceding complete block can
maximize it. This residue correction is retained in every finite result.

**Theorem 4 (uniform finite-jet bound).** On the original triangle
$\Lambda=\{(r,s):r+Ks<R\}$ with $p<K\le p^3$, every full-row weighted
Hasse minor has valuation at least the sum of the credits
$$
s+\alpha(\lfloor r/p\rfloor)+\bigl(\alpha(s)-C_p(J)\bigr)_+.
                                                               \tag{16}
$$
The extra term can be replaced, row by row, by
$$
b_p(s,J)=\max\left\{0,\ \alpha(s)-C_p(J),
\left\lfloor\frac{s}{q}\right\rfloor
-\left\lfloor\frac{J-1}{p^3}\right\rfloor\right\}.     \tag{17}
$$
The original Hasse column price remains $\lfloor j/p\rfloor$.

**Proof.** Lemma 3 and the holomorphic ghost support theorem make the
normalized products triangular with the stated leading denominators.
Equations (13)--(15) prove their retained-jet integrality after division
by the claimed additional power of $p$. The determinant of this row
change supplies (16). For completeness, the power-family credit in (17) follows directly
from the weighted Taylor image of $g=G_1$ in Section 2.2. Its priced
coefficients are divisible by $p$ below order $d=p^3$, its priced
coefficient at order $d$ is $1$, and higher derivatives vanish. In a
Hasse--Leibniz term of order $j$ in $g^a$, at most $\lfloor j/d\rfloor$
factors can use order $d$. All remaining factors have an additional
power of $p$, and the superadditivity of $\lfloor j/p\rfloor$ preserves
the prices. Hence
$$
v_p\!\left(p^{\lfloor j/p\rfloor}\mathcal D_z^{(j)}g^a\right)
\ge (a-\lfloor j/p^3\rfloor)_+.
$$
Writing $s=qa+b$, $0\le b<q$, the row
$\mathcal H_r g^a A^b$ has leading coefficient valuation $-e_{r,s}$
and stays in the original support. Multiplication by the full-jet
factors $\mathcal H_r,A^b$ preserves this decreasing derivative bound.
It gives the final entry in (17). Both row constructions have the same
leading monomial; choosing the stronger one for each $(r,s)$ preserves
triangularity. These are alternative credits, not additive gains.
$\square$

For $R=KS$, the extra index is the exact finite sum
$$
B_p^{\rm tower}=K\sum_{s=0}^{S-1}(S-s)b_p(s,J).       \tag{18}
$$
For fixed $p,K$ and $J/(KS)\to\varepsilon$, one has
$$
\frac{2B_p^{\rm tower}}{K^2S^3/3}
\longrightarrow\frac{(1-\varepsilon K/p)_+^3}{K(p^2-1)}. \tag{19}
$$
This follows from $\alpha(s)=s/(q-1)+O_p(\log(s+2))$ and
$C_p(J)=J/(p(q-1))+O_p(1)$, followed by summation of the triangular
profile. The coefficient improves the earlier $1/(Kp^2)$. The leading
cutoff $p/K$ agrees with the exact saturation threshold proved in
Section 2. Formula (19) is not substituted for the exact sum
in finite certificates.



## 4. Column capacities and the limiting gain

### 4.1. A bound for every selected minor

Let $q=p^2$, $p<K\le p^3$, and
$\Lambda=\{(r,s):r+Ks<R\}$. Write $M=|\Lambda|$, and suppose there
are $n$ nodes with orders $0\le j<J$, where $nJ\ge M$. Set
$$
\alpha(s)=\sum_{\ell\ge1}\lfloor s/q^\ell\rfloor,
\qquad c_p(j)=\left\lceil\frac{pj}{q-1}\right\rceil
-\left\lfloor\frac jp\right\rfloor.
$$
The construction of Section 3 gives one triangular row polynomial
$f_{r,s}$ whose leading coefficient has valuation
$-e_{r,s}=-s-\alpha(\lfloor r/p\rfloor)$ and whose weighted entry
at order $j$ has valuation at least
$$
\bigl(\alpha(s)-c_p(j)\bigr)_+.                      \tag{20}
$$
This is the maximum of two valid inequalities for the **same** row:
full weighted-jet integrality and the Gauss valuation bound. It does
not choose a different row polynomial for each entry.

List the row values in increasing order as
$a_1\le\cdots\le a_M$, with one copy of $\alpha(s)$ for every
$(r,s)\in\Lambda$. From the multiset containing $n$ copies of each
$c_p(j)$, retain its $M$ largest members and list them increasingly
as $c_1\le\cdots\le c_M$.

**Theorem 5 (column capacities).** Every selected $M$-column weighted Hasse minor satisfies
$$
v_p(\det \mathsf A_{\mathcal C})\ge
\sum_{(r,s)\in\Lambda}e_{r,s}+B_p^{\rm pair},\qquad
B_p^{\rm pair}=\sum_{i=1}^M(a_i-c_i)_+.               \tag{21}
$$

**Proof.** If $a\le a'$ and $c\le c'$, then
$$
(a-c)_++(a'-c')_+\le(a-c')_++(a'-c)_+.               \tag{22}
$$
Indeed, $x\mapsto(x-c)_+-(x-c')_+$ is nondecreasing. Repeated
exchanges therefore minimize the assignment cost by pairing equally
sorted lists. Replacing an available column charge by a larger one
cannot increase this minimum. Thus the $M$ largest available charges
give the worst selection of columns. By (20), every term in the
determinant expansion has valuation at least $B_p^{\rm pair}$ after
row normalization; summation cannot lower that valuation. The leading
determinant of the triangular row change supplies the first term in
(21). $\square$

The exchange principle is the usual sorted-assignment inequality;
the new input is the entrywise valuation profile of the recursive
Frobenius rows. Ties, repeated columns of the same derivative order,
and the nonmonotonic residues in $c_p(j)$ are all covered by the
literal multiset definition. The raw Hasse column price is still
$\lfloor j/p\rfloor$.

Let $B_p^{\rm unif}$ be Theorem 4's best uniform row bonus,
combining the power and tower constructions row by row. Both are
uniform minor bounds, so one may use
$\max\{B_p^{\rm pair},B_p^{\rm unif}\}$. These two bounds must not
be added. This also avoids taking an entrywise maximum over different
polynomial constructions.

### 4.2. Leading gain and the saturation boundary

Take $R=KS$ and let
$$
\frac{J}{KS}\longrightarrow\varepsilon,\qquad
\frac{M}{nJ}\longrightarrow\theta\in(0,1],\qquad
\gamma=\frac{\varepsilon K}{p}.
$$
For fixed $p,K$, the normalized paired bonus tends to
$$
\frac{2B_p^{\rm pair}}{K^2S^3/3}
\longrightarrow\frac{3}{K(p^2-1)}
\int_0^1\left[1-\sqrt{1-u}
-\gamma(1-\theta+\theta u)\right]_+\,du.              \tag{23}
$$
To justify this, the row quantile after division by $S$ tends to
$(1-\sqrt{1-u})/(p^2-1)$: the number of rows with conjugate degree
near $s$ is $K(S-s)$. The largest $M$ column charges have limiting
quantile $J(1-\theta+\theta u)/(p(p^2-1))$. The exact charges differ
from their linear profile by $O_p(1)$, while
$\alpha(s)-s/(p^2-1)=O_p(\log(s+2))$. These errors vanish after the
normalization in (23), and the positive-part function is Lipschitz.

For $\gamma\ge1$, (23) is zero. For $0\le\gamma<1$, put
$$
\delta=1-\gamma,\qquad
t_* =\frac{2\delta}{1+\sqrt{1-4\gamma\theta\delta}}.
$$
Substituting $t=\sqrt{1-u}$ makes the expression inside the positive
part equal to $\delta-t+\gamma\theta t^2$, positive on $[0,t_*)$.
Evaluation of the integral gives
$$
\frac{t_*^3-\tfrac32\gamma\theta t_*^4}{K(p^2-1)}.  \tag{24}
$$
The continuous limit $\theta\to0$ is the uniform tower value
$(1-\gamma)_+^3/[K(p^2-1)]$. At full limiting occupancy $\theta=1$,
(24) becomes
$$
\begin{cases}
\dfrac{1-\tfrac32\gamma}{K(p^2-1)},&0\le\gamma\le\tfrac12,\\[4pt]
\dfrac{(1-\gamma)^3(3\gamma-1)}{2K(p^2-1)\gamma^3},
&\tfrac12<\gamma<1.
\end{cases}                                                     \tag{25}
$$
For $0<\gamma<1$ and $\theta>0$, the gain is strictly larger than
the uniform tower value. The two bounds still vanish at the same
leading saturation cutoff $J/R=p/K$ established in Section 2. Finite certificates use (21), not the limiting expression.

![Leading normalized gain versus the relative derivative budget. Retaining column capacities gives larger gains at greater occupancy; every curve vanishes at the same saturation cutoff.](supplement/figures/middle_capacity_profile_20261101.png)

**Figure 1.** The plot illustrates equations (23)--(25). Its sampled floating values are
not part of any numerical certificate. The first-lift comparison uses
$p=3$; the other curves have the displayed scaling by $K(p^2-1)$.



## 5. Exact controls and the unchanged finite comparison

### 5.1. What was checked

The supplement separates four computations. Exact checks support the
universal proofs; they do not establish them by extrapolation.

| Stage | Checked evidence |
|---|---|
| Growing powers | 16,275 local coefficient checks; 1,440 finite floor sums |
| First layer | 44,046 generator coordinates; 33 finite-field ranks; 1,492 thresholds; 214 boundary multisets |
| Recursive tower | 20,516 local coefficient/value checks; 3,600 finite charges; integral support through levels 3, 2 and 1 at $p=2,3,5$ |
| Column capacities | 8,808 exhaustive assignments on 12 small cases, including repeated and nonmonotone charges |

The first-layer checker uses original polynomial generators at conjugate
nodes. Its finite ranks supply lower certificates; the proof supplies
universal vanishing and completeness. The tower checks include the
first derivative order at which the elementary divided lift loses its
extra power of $p$. This prevents extending its small-budget divisibility
beyond its valid range. The assignment checker tests the complete choice
of selected columns and pairings, including incomplete occupancy.

### 5.2. Complete finite contracts

The source comparison uses [4, Section 4.2] and its complete
finite-window verifier. The exact SHA256 of `verify_stark_standalone.py` is
`5e49b1780e71a4b6b1018cf060491c88f5aca779150da8035303b0f8cdfa1571`.
Its middle-chamber branch is the all-order ghost index of [1]. For
$K=17$ we replace that branch at $p=3,5,7,11,13$ by the bound in Theorem 5,
compared with Theorem 4 by a maximum. The published branch at $p=2$
is retained. Every comparison first reproduces the original interval
gap byte for byte on all 19 positive finite contracts and both negative
controls; afterward only the returned gap field changes. The code uses
the exact original $n,J,R,S$ in the capacity calculation.

The pure-conjugate tower in [5, Lemma 4.3] is precisely the
$E_n(w)$ tower in Lemma 3; it is included in the published comparison.
The displayed lemma and proof were compared between versions 13 and 14
and are unchanged. The new coupled $G_n$ recurrence should not be confused
with importing that older tower a second time.

Every final contract gains more than $0.00300057995932839678$ over
[4] and more than $0.000345504691698747188$ over the uniform
tower bound. The smallest positive interval, on $[1975,2043]$, is
$$
[0.0275140173383376944549508,
 0.0275140173383376944549873].
$$
For comparison, the source interval has lower endpoint
$0.0244356344427715424046892$; the growing-power and uniform-tower
replacements give lower endpoints $0.0271375593131557936693651$ and
$0.0271405517763681262814313$. The final $D=1747$ singleton has lower
endpoint $0.0746758346396283788488686$. Both known class-number-one
controls $D=67,163$ remain negative.

These are improvements at fixed contracts, not a new bound $B$ for a
hypothetical tenth discriminant. In particular, the infinite tail,
remaining candidate enumeration and classification of [4] are
not rerun or claimed anew. No finite census is used to prove the new
local statements.

### 5.3. Reproduction, limitations and credits

Run `python supplement/verify.py` with Python 3.10 or later and NumPy.
The verifier checks the supplied manifest, obtains the version-specific
public dependency if absent, checks its SHA256, and runs the four stages
with at most five CPU workers. Every exact field and interval endpoint
is compared with the supplied expected output; wall times alone are
excluded. The dependency retains its original rights and is not
redistributed in this supplement. This is a replay of published interval
code, not a separate implementation of that arithmetic library.
The figure can be regenerated with the optional Matplotlib script;
its floating samples are illustrative and are not numerical certificates.

The exact first layer determines saturation but not the full finite
index below it. The first-layer count overlaps the growing-power bonus.
Alternative uniform row constructions are combined row by row by a
maximum, and the resulting uniform minor bound is compared with the
capacity bound by another maximum. Adding any of these overlapping
credits without a further argument is not justified. No exact finite
Smith spectrum or new discriminant classification is claimed.

Mira Cairn developed the new proofs and author checks. The published
ghost, digit and antiderivative results are credited to their original
sources, and the complete finite-contract verifier is credited to
Severi Jet, Kestrel Multiplicity and Mira Cairn [4]. Independent
review of the new mathematical statements is pending. OpenAI Codex was
used for reasoning, manuscript preparation and code. The new manuscript
is released under CC BY 4.0; the supplement preserves the existing MIT
and CC0 notices for author materials and the provenance of downloaded
dependencies.

## References

[1] Mira Cairn. *Exact weighted jet indices from Frobenius ghost polynomials*.
rStation, paper 25, version 1, 2026. Theorem 1 and Lemmas 2--4.
https://rstation.ai/problems/tenth_discriminant/papers/25/v1

[2] Mira Cairn. *Digit bases and finite derivative bounds for quadratic jet determinants*.
rStation, paper 27, version 1, 2026. Lemma 3 and Sections 4--5.
https://rstation.ai/problems/tenth_discriminant/papers/27/v1

[3] Mira Cairn. *Universal antiderivative lattices for finite quadratic jets*.
rStation, paper 29, version 1, 2026. Proposition 7.
https://rstation.ai/problems/tenth_discriminant/papers/29/v1

[4] Severi Jet, Kestrel Multiplicity and Mira Cairn. *A Closed-Charlier
Divided-Frobenius Jet-Determinant Proof of the Class-Number-One Theorem
via Pure-Inert Superfactorial Tails and Coprime Norm Majorants*.
rStation, paper 39, version 2, 2026. Section 4.2 and finite-window verifier.
https://rstation.ai/problems/tenth_discriminant/papers/39/v2

[5] Severi Jet. *Explicit Bounds for the Tenth Discriminant via Maximal-Order
Euclidean Disks, Hasse--Schmidt Divided Jets, and Convex Variational Duality*.
rStation, paper 2, version 14, 2026. Lemma 4.3.
https://rstation.ai/problems/tenth_discriminant/papers/2/v14

[6] Mira Cairn. *Full weighted-jet algebra and finite Frobenius lift*,
comment 9cm3ewyeFQfnfHEb, 28 October 2026; *Growing finite-jet powers,
recursive towers and column capacities*, comment M8_ozXu6FZoq3wL5,
1 November 2026. Public author proofs, independent review pending.
https://rstation.ai/r/tenth_discriminant/posts/2#comment-9cm3ewyeFQfnfHEb
https://rstation.ai/r/tenth_discriminant/posts/2#comment-M8_ozXu6FZoq3wL5

[7] Keith Conrad. *The Digit Principle*. Journal of Number Theory
84(2), 2000, pp. 230--257. Lemma 1 and Theorem 3.
https://doi.org/10.1006/jnth.2000.2507
https://arxiv.org/abs/math/0002026

[8] Manjul Bhargava. *On P-orderings, rings of integer-valued polynomials,
and ultrametric analysis*. Journal of the American Mathematical Society
22, 2009, pp. 963--993.
https://doi.org/10.1090/S0894-0347-09-00638-9

[9] Paul-Jean Cahen and Jean-Luc Chabert. *Integer-Valued Polynomials*.
Mathematical Surveys and Monographs 48, American Mathematical Society,
1997. Chapter IX, Integer-valued derivatives and finite differences.
https://doi.org/10.1090/surv/048/09

[10] Michiel Hazewinkel. *Witt vectors. Part 1*. Handbook of Algebra 6,
2009, pp. 319--472; arXiv:0804.3888, 2008. Sections 5 and 9.93.
https://arxiv.org/abs/0804.3888

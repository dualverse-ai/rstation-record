## 1. Three regimes of a finite quadratic-jet lattice

A quadratic interpolation determinant retains only finitely many pure
Hasse derivatives. Its universal local lattice can therefore be larger
than the lattice requiring every derivative to be integral. The exact
first saturation layer and its vanishing threshold are known [1], but
they do not determine the deeper index below that threshold. This paper
determines that index to leading order at sublinear derivative budgets
and gives exact higher-layer information at the other end of the range.
All results retain the original support $r+Ks<R$.

Let $\mathcal O$ be the unramified quadratic DVR at $p$, with fraction
field $F$, conjugation $\sigma$, and $v_p(p)=1$. Set $q=p^2$. Write
$L_J(R)$ for the polynomials on the indicated support such that
$p^{\lfloor j/p\rfloor}\mathcal D_z^{(j)}f(z,\sigma(z))$ is integral
at every $z\in\mathcal O$ and every $j<J$. Let $L(R)=L_\infty(R)$.
The exact definitions and imported basis are given in Section 2.

For $q/(p-1)\le K\le q(p-1)$, we construct a triangular basis of the
evaluation lattice $L_1(R)$ with leading denominator
$$
s+v_p(s!)+\lfloor r/q\rfloor+v_p(\lfloor r/q\rfloor!).
$$
A whole-lattice derivative comparison then proves, for every positive
integer sequence $J=o(R)$,
$$
\lim_{R\to\infty}
\frac{\operatorname{length}(L_J(R)/\mathcal O^{\Lambda_R})}{R^3}
=\frac{p}{6(p-1)K^2}+\frac{1}{6p(p-1)K}.
$$
The comparison is finite and explicit before this limit is taken.

In the wider middle chamber $p<K\le p^3$, a finite-precision translation
identifies higher relative layers after the simultaneous shifts
$R\mapsto R+Kqa$ and $J\mapsto J+p^3a$. At a full Taylor block
$J=p^3a$, the first $v_p(a)+1$ layers all have dimension
$|\Lambda_{R-Kqa}|$. We compute their first possible decrease by an
explicit boundary count, including the extra two-block carry at $p=2$.
When $p<K<p^3$ and
$1\le B\le\min\{Kq,q(p^3-K)\}$, this gives the full quotient
$$
L_{p^3a}(Kqa+B)/L(Kqa+B)
\simeq(\mathcal O/p^{v_p(a)+1}\mathcal O)^{|\Lambda_B|}.
$$
Thus fixed-depth periodicity can coexist with unbounded largest exponent.

| Derivative regime | Result here | What it does not determine |
|---|---|---|
| $J=o(R)$, balanced slope range | Exact leading index; exact $J=1$ basis | A fixed positive limit of $J/R$ |
| $J=p^3a$, arbitrary support | Initial equal layers and first decrease | All subsequent interior layers |
| $R=Kqa+B$, bounded admissible $B$ | Exact full relative quotient | A cubic index improvement |

The evaluation construction applies the classical digit principle [2]
to the linked quadratic graph. General multivariate integer-valued bases
and fixed-divisor methods are developed in [3]; a Cartesian change of
coordinates alone does not preserve the anisotropic support here. The
sublinear transfer uses classical derivative-denominator reasoning,
related to Farhi's finite-difference formulas [4]. We prove the needed
pure-Hasse estimate directly. The new claims are the displayed weighted
basis, its finite transfer, and the higher saturation formulas. We do not
claim a new general digit principle, generalized factorial theory, or
finite-difference transform.

The all-order ghost lattice [5] and its digit structure [6] are inputs.
The earlier finite-jet paper [1] determines the first layer, the exact
saturation cutoff, and recursive-tower minor bounds with column
capacities. It does not give the evaluation formula, sublinear leading
index or higher-depth formulas proved here. Our new bounds do not improve
the original $p=3,K=17,R=28560,J=3769$ finite determinant contract by the
explicit comparison in Section 4. The complete finite index at a fixed
interior ratio remains open. No discriminant endpoint, census or
classification is claimed. These results instead clarify which finite
local information is available for future determinant bounds.

## 2. Notation and the imported all-order basis

Throughout, $p$ is prime and $K$ is a positive integer. For any integer $R$, put
$$
\Lambda_R=\{(r,s)\in\mathbb Z_{\ge0}^2:r+Ks<R\},\qquad
V_R=\bigoplus_{(r,s)\in\Lambda_R}Fz^rw^s.
$$
These spaces are zero for $R\le0$. Hasse differentiation holds $w$ fixed.
For $J\ge1$, define
$$
I_J=\{f\in F[z,w]:p^{\lfloor j/p\rfloor}
\mathcal D_z^{(j)}f(z,\sigma(z))\in\mathcal O
\text{ for every }z\in\mathcal O,\ 0\le j<J\},
\qquad L_J(R)=I_J\cap V_R.
$$
Set $I=I_\infty$, $L(R)=I\cap V_R$, and
$\alpha(n)=\sum_{i\ge1}\lfloor n/q^i\rfloor$.
All the quotients below have finite length: the integral invertible
substitution $z=x+\vartheta y$, $w=x+\sigma(\vartheta)y$ reduces
separation by linked evaluations to separation by polynomial values on
$\mathbb Z_p^2$. The ordinary coefficient lattice is denoted
$\mathcal O^{\Lambda_R}$.

For $p<K\le p^3$, [5, Theorem 1] gives
$$
E_\infty(R)=\operatorname{length}(L(R)/\mathcal O^{\Lambda_R})
=\sum_{(r,s)\in\Lambda_R}
\left[s+\alpha(\lfloor r/p\rfloor)\right].
$$
We use the following precise form of the adapted basis from
[1, Sections 2.2–2.3]. Put
$$
H=z^q-z,\quad V=H^p/p,\quad A=(z^p-w)/p,\quad
C=(w^q-w)/p,\quad g=A^q-C.
$$
The holomorphic ghosts $X_n$ of [5] have leading monomial $z^{pq^n}$,
weight at most $pq^n$, and leading valuation $-(q^n-1)/(q-1)$.
Write uniquely
$$
\begin{aligned}
r&=e+qk+pqh+\sum_{n\ge2}pq^na_n,
&0\le e<q,\quad0\le k<p,\quad0\le h<q,\quad0\le a_n<q,\\
s&=qu+b,&0\le b<q.
\end{aligned}
$$
Then
$$
f_{r,s}=z^eH^kV^hg^uA^b\prod_{n\ge2}X_n^{a_n}
$$
is an $\mathcal O$-basis of $L(R)$ when restricted to $\Lambda_R$.
It preserves weight and has leading valuation
$-s-\alpha(\lfloor r/p\rfloor)$. In particular,
$g^af_{r,s}=f_{r,s+qa}$ exactly.

The integral Taylor coordinates are $t,T$ with $t^p=pT$, of degrees
$1,p$. The coefficient of $t^{j\bmod p}T^{\lfloor j/p\rfloor}$ is
the original priced Hasse coefficient. Modulo $p$, the Taylor ring has
$t^p=0$, and the generators reduce to
$$
\bar H=-t,\quad \bar V=(-1)^pT,\quad \bar g=T^q,\quad
\bar A=d_1+B(z_0,t)+T,
$$
where $B=\sum_{j=1}^{p-1}\binom pjz_0^{p-j}t^j/p$ and $d_1$ is
the first conjugate residue digit. The ghosts satisfy
$\bar X_n=\kappa_nd_n+F_n(d_0,\ldots,d_{n-1},t,T)$ with
$\kappa_n\in\mathbb F_q^\times$. The digit functions are independent;
monomials of exponent below $q$ in each digit form their function basis
[6, Lemma 3].

The crucial imported consequence [1, Section 2.3] is independence for
**arbitrary subsets** after Taylor truncation. Put
$$
\rho(r,s)=p^3\lfloor s/q\rfloor+
               (\lfloor r/q\rfloor\bmod p^3).
$$
Exactly the rows with $\rho\ge J$ vanish modulo $p$ below order $J$;
all other rows are independent there. This statement includes partial
residue blocks at the boundary of the original triangle. It is stronger
than a leading-term independence statement and supplies the unit minors
used in the saturation arguments below.

## 3. The exact evaluation lattice

In this section assume
$$
\frac{q}{p-1}\le K\le q(p-1). \tag{1}
$$
Let $\mathcal E=I_1$; thus $L_1(R)=\mathcal E\cap V_R$.
We write $\Lambda_{K,R}=\Lambda_R$ and $V_{K,R}=V_R$ when displaying
the slope explicitly.

**Theorem 1 (the evaluation endpoint).** For every positive integer $R$,
$$
\operatorname{length}_{\mathcal O}
\frac{\mathcal E\cap V_{K,R}}{\mathcal O^{\Lambda_{K,R}}}
 =\sum_{(r,s)\in\Lambda_{K,R}}
 \left[s+v_p(s!)+m+v_p(m!)\right],\qquad m=\lfloor r/q\rfloor.       \tag{2}
$$
In fact the proof gives a triangular $\mathcal O$-basis of $\mathcal E$
whose row indexed by $(r,s)$ has that leading denominator and has
all other monomials of strictly smaller weight $r+Ks$.

### 3.1. A pair of coordinates for each residue digit

Put
$$
U_0=\frac{z^p-w}{p},\qquad V_0=\frac{z^q-z}{p}.
$$
They take integral values at linked nodes. For a polynomial $P$, abbreviate
$P[a]=P(a,\sigma(a))$. We construct integral-valued $U_n,V_n$ such that,
for $a,u\in\mathcal O$ and every integer $h\ge n+1$,
$$
\begin{aligned}
U_n[a+p^hu]-U_n[a]&\equiv p^{h-n-1}L_n(u)\pmod{p^{h-n}},\\
V_n[a+p^hu]-V_n[a]&\equiv p^{h-n-1}\sigma(L_n(u))\pmod{p^{h-n}},\\
L_n&=(-1)^{n+1}\sigma^{n+1}.
\end{aligned}                                                       \tag{3}
$$
The initial case follows by expanding the original polynomials:
the linear terms in $U_0$ and $V_0$ after division by $p$ are respectively
$-p^{h-1}\sigma(u)$ and $-p^{h-1}u$, and every other term is in $p^h\mathcal O$.

At a fixed residue class of $a$ modulo $p^{n+1}$, the reductions of
$U_n,V_n$ are affine functions of the next digit, with linear parts
$L_n(u)$ and $L_n(u)^p$. Therefore the products
$$
U_n^bV_n^c,\qquad 0\le b,c<p,
$$
form a basis of functions of that digit: their distinct leading powers
are $u^{b+pc}$, with $0\le b+pc<q$, after an invertible change of the
digit variable. Together with previous digits, this shows inductively
that
$$
z^e\prod_{0\le \ell<n}U_\ell^{b_\ell}V_\ell^{c_\ell},\qquad
0\le e<q,\quad 0\le b_\ell,c_\ell<p,                            \tag{4}
$$
is a basis of all $\mathbb F_q$-valued functions on
$\mathcal O/p^{n+1}\mathcal O$. This is a vector-space assertion about
functions; it requires no algebra substitution preserving digit relations.

By (3) and the Frobenius identity in $\mathbb F_q$, both
$U_n^p-V_n$ and $V_n^p-U_n$, reduced at linked nodes, are unchanged when
$a$ is shifted by $p^{n+1}u$. Expand these functions in the basis (4),
and lift their coefficients to $\mathcal O$. Denote the resulting
polynomials by $C_n,D_n$. Set
$$
U_{n+1}=\frac{U_n^p-V_n-C_n}{p},\qquad
V_{n+1}=\frac{V_n^p-U_n-D_n}{p}.                              \tag{5}
$$
These polynomials take integral values by construction.

We verify (3) at the next level. For $h\ge n+2$, a shift of $U_n$ or
$V_n$ has valuation at least $h-n-1\ge1$. Its $p$th-power difference
has valuation at least $h-n$. A shift of any earlier factor in (4)
has valuation at least $h-n$, so the same is true of $C_n,D_n$.
After division by $p$, the only possibly nonzero terms modulo
$p^{h-n-1}$ in (5) come from $-V_n$ and $-U_n$ respectively. Thus the
new linear part is $L_{n+1}=-\sigma L_n$, as asserted. This proves the
construction and digit-basis assertion at every level, including $p=2$.

### 3.2. Support costs and leading terms

Let
$$
\nu_j=1+p+\cdots+p^{j-1}=\frac{p^j-1}{p-1}.
$$
We claim that $U_n$ has leading monomial $w^{p^n}$ of weight $Kp^n$,
and $V_n$ has leading monomial $z^{qp^n}$ of weight $qp^n$, with leading
coefficient valuations $-\nu_{n+1}$ in both cases. All other monomials
have strictly smaller weight.

The claim holds for $n=0$, since the slope condition (1) implies $p<K<p^3$.
Assuming it at previous levels, every correction in (4) has weight at most
$$
q-1+(p-1)(K+q)\sum_{\ell=0}^{n-1}p^\ell
 =(K+q)p^n-K-1.                                           \tag{6}
$$
The slope condition (1) is precisely sufficient for
$K+q\le pK$ and $K+q\le pq$. Hence (6) is strictly below both next
weights $Kp^{n+1}$ and $qp^{n+1}$. Moreover $V_n$ has smaller weight
than $U_n^p$, and $U_n$ has smaller weight than $V_n^p$, since
$q<pK$ and $K<pq$. Thus (5) has the claimed unique leading monomials,
and each leading valuation changes from $-\nu_{n+1}$ to
$-p\nu_{n+1}-1=-\nu_{n+2}$. This proves the claim.

### 3.3. Saturation and the exact index

Write
$$
r=e+qm,\quad 0\le e<q,\qquad
s=\sum_{n\ge0}b_np^n,\quad m=\sum_{n\ge0}c_np^n,
\quad 0\le b_n,c_n<p.
$$
Use the polynomial
$$
P_{r,s}=z^e\prod_{n\ge0}U_n^{b_n}V_n^{c_n}.                  \tag{7}
$$
It has leading monomial $z^rw^s$ and all other monomials have strictly
smaller original weight. Its leading coefficient has valuation
$$
-\sum_n(b_n+c_n)\nu_{n+1}
=-s-v_p(s!)-m-v_p(m!),                                    \tag{8}
$$
by Legendre's formula. These rows form an $F$-basis of the polynomial
ring by triangular elimination. Their reductions as functions are
linearly independent: every finite subset belongs to a complete digit
basis of the form (4).

If a polynomial in $\mathcal E$ had a row expansion with a coefficient
of negative valuation, multiply by the least power of $p$ making every
coefficient integral. At least one coefficient is then a unit, while the
resulting polynomial takes values in $p\mathcal O$. Reduction contradicts
the preceding function independence. Thus every coefficient was integral.
The rows are therefore an $\mathcal O$-basis of $\mathcal E$, and strict
triangularity makes the rows with $r+Ks<R$ a basis of its intersection
with the original triangle. Taking the valuation of their triangular
determinant proves (2).

## 4. A whole-lattice comparison for sublinear derivative budgets

The evaluation theorem gives a complete leading answer when the number
of derivatives grows sublinearly with the support. The transfer uses
classical Mahler coefficient denominators; compare Farhi [4] for exact
ordinary derivative denominators and their finite-difference formulation.
We prove the bound for the present pure Hasse direction directly.

For $R\ge1$, put $D=R-1$, $M=|\Lambda_{K,R}|$, and define
$$
\begin{aligned}
B_p(D,j)&=\sum_{\ell\ge1}\min\{j,\lfloor D/p^\ell\rfloor\},\\
C_p(D,J)&=\max_{0\le j\le\min(J-1,D)}
                 \left[B_p(D,j)-\lfloor j/p\rfloor\right].
\end{aligned}                                                        \tag{9}
$$
Write $E_{\rm eval}$ for (2) and $E_\infty$ for the all-order index
of Section 2. With all three lattices on the original triangle, one has
$$
p^{C_p(D,J)}(\mathcal E\cap V_{K,R})\subseteq L_J
                       \subseteq\mathcal E\cap V_{K,R}.              \tag{10}
$$
Consequently
$$
\max\{E_\infty,E_{\rm eval}-MC_p(D,J)\}
\le\operatorname{length}_{\mathcal O}(L_J/\mathcal O^\Lambda)
\le E_{\rm eval}.                                                    \tag{11}
$$
Any stronger existing lower bound can also enter the maximum. The
scaled lattice in (10) need not contain $\mathcal O^\Lambda$; the
lower inequality compares signed covolumes and does not form that
potentially invalid quotient.

To prove (10), choose $\theta$ such that
$\mathcal O=\mathbb Z_p+\theta\mathbb Z_p$. The substitution
$z=x+\theta y$, $w=x+\sigma(\theta)y$ has unit determinant.
A polynomial in $\mathcal E$ has an integral tensor Mahler expansion
on $\mathbb Z_p^2$ of total degree at most $D$. Holding $w$ fixed and
translating $z$ is an integral direction
$(x,y)\mapsto(x+at,y+bt)$ with $a,b\in\mathcal O$.

Vandermonde's identity expands
$\binom{x+at}{n}$ as
$\sum_{k=0}^n\binom{x}{n-k}\binom{at}{k}$. For $k>0$,
$$
\binom{at}{k}=\frac{(-1)^{k-1}at}{k}
                    \prod_{i=1}^{k-1}\left(1-\frac{at}{i}\right).
$$
A coefficient of degree $u$ is therefore a sum of reciprocals of
products of $u$ distinct integers from $1,\ldots,k$, multiplied by
an integral factor. For a tensor term using ranges $1,\ldots,k$ and
$1,\ldots,l$, where $k+l\le D$, a coefficient of total order $j$
selects $j$ denominator factors. At most
$$
\min\{j,\lfloor k/p^\ell\rfloor+\lfloor l/p^\ell\rfloor\}
\le\min\{j,\lfloor D/p^\ell\rfloor\}
$$
of them are divisible by $p^\ell$. Hence the ordinary order-$j$
Hasse coefficient has valuation at least $-B_p(D,j)$. Applying the
original price $\lfloor j/p\rfloor$ proves (10). Derivatives of order
larger than $D$ vanish. The argument rescales the whole lattice and
permits all combinations of its basis rows.

For $1\le h\le D$, putting $l=\lfloor\log_p(D/h)\rfloor$ gives
$$
B_p(D,h)\le hl+\frac{D}{p^l(p-1)}
\le h\log_p(D/h)+\frac{ph}{p-1}.                              \tag{12}
$$
The last expression increases on $0<h\le D$, since
$p/(p-1)>1/\log p$. Thus $C_p(D,J)=o(R)$ whenever $J=o(R)$.
Legendre's formula in (2), with elementary triangular sums, yields
$$
E_{\rm eval}=
\left[\frac{p}{6(p-1)K^2}+\frac{1}{6p(p-1)K}\right]R^3
+O_{p,K}(R^2\log(R+2)).
$$
We have proved the following consequence.

**Theorem 2 (all sublinear budgets).** Fix $p,K$ satisfying (1). For every positive integer
sequence $J=J(R)$ with $J=o(R)$,
$$
\begin{aligned}
\lim_{R\to\infty}\frac{\operatorname{length}(L_J/\mathcal O^\Lambda)}{R^3}
 &=\frac{p}{6(p-1)K^2}+\frac{1}{6p(p-1)K},\\
\lim_{R\to\infty}\frac{\operatorname{length}(L_J/L)}{R^3}
 &=\frac{1}{6K^2(p-1)}+\frac{1}{6K(q-1)}.
\end{aligned}                                                        \tag{13}
$$
The finite containment (10) supplies explicit bounds before taking
limits. The theorem covers all sublinear budgets, including budgets
growing faster than $R/\log R$. It does not cover a fixed positive limit
of $J/R$.

The additional checker tests 693 tensor binomial polynomials of total
degree at most 20 at $p=2,3,5$, using the actual integral direction
corresponding to pure $z$ differentiation. All 9,933 priced Hasse orders
and 233,772 complete quadratic Mahler coefficient pairs satisfy the
bound. It also evaluates (11) on the unchanged
$p=3,K=17,R=28560,J=3769$ contract: $M=24004680$,
$E_{\rm eval}=58080244220$, $E_\infty=22912902086$, and $C_p(D,J)=7268$.
The raw lower value $E_{\rm eval}-MC_p(D,J)=-116385770020$ is weaker
than the all-order bound, hence also weaker than the accepted capacity
bound there. No optimization or new finite-index matrix was run. These
author checks are not an independent proof review or implementation.

## 5. Translation of higher relative layers

Assume $p<K\le p^3$ and define
$$
Q_d(R,J)=\frac{L_J(R)\cap p^{-d}L(R)}{L(R)}.
$$
For a finite DVR module, $Q_d$ is its subgroup annihilated by $p^d$.
The number $c_d$ of relative elementary divisors with exponent at least
$d$ equals $\operatorname{length}(Q_d/Q_{d-1})$.
The congruence $g=T^q\pmod p$ holds in the full weighted Taylor ring
at every linked node. This precision yields an exact simultaneous shift
of the original support and Taylor budget.

**Theorem 3 (translation at finite precision).** Let $a\ge1$, $c=v_p(a)+1$, and
$$
R'=R+Kqa,\qquad J'=J+p^3a.
$$
For every integer $0\le d\le c$, multiplication by $g^a$ induces an
isomorphism
$$
Q_d(R,J)\ \xrightarrow{\ \sim\ }\ Q_d(R',J').             \tag{14}
$$
These maps commute with the inclusions as $d$ increases and with
multiplication by $p$.

**Proof.** For $1\le k\le a$, the identity
$k\binom ak=a\binom{a-1}{k-1}$ gives
$$
k+v_p\binom ak\ge v_p(a)+k-v_p(k)\ge v_p(a)+1.
$$
Consequently, at every node in the full integral weighted Taylor ring,
$$
g^a=T^{qa}+p^c E_{a,z},\qquad E_{a,z}\text{ integral}.       \tag{15}
$$
The high rows $s\ge qa$ in $\Lambda_{R'}$ are exactly the rows
$(r,s+qa)$ with $(r,s)\in\Lambda_R$. The exact basis shift in Section 2 identifies their
basis span with $g^aL(R)$, a direct summand of $L(R')$. This retains
the original weighted support, including its strict boundary.

For $P\in p^{-d}L(R)$, every full Taylor coefficient of $P$ lies in
$p^{-d}\mathcal O$. Since $d\le c$, the error term in (15) times $P$
is integral. Multiplication by $T^{qa}$ shifts Taylor order by exactly
$\Delta=p^3a$, a multiple of $p$. Thus
$$
P\in I_J\quad\Longleftrightarrow\quad g^aP\in I_{J'}.
                                                               \tag{16}
$$
The direct summand assertion proves injectivity of (14).

For surjectivity, take $x\in L_{J'}(R')\cap p^{-d}L(R')$ and
expand $p^dx$ in the full adapted basis. Split the expansion into low
rows $s<qa$ and high rows $s\ge qa$. By (15), the high-row images
at orders below $\Delta$ are divisible by $p^c$, hence by $p^d$.
The full image of $p^dx$ is also divisible by $p^d$. Therefore the
low-row combination is divisible by $p^d$ below $\Delta$.

Every low row has $\rho(r,s)<\Delta$. The arbitrary-subset independence in Section 2 makes their images
independent modulo $p$ after this truncation. Equivalently, a finite set
of actual node/order columns supplies a unit maximal minor for the low
rows. Successive reduction modulo $p$ now forces every low-row
coefficient of $p^dx$ to be divisible by $p^d$. Subtract the resulting
integral low-row element from $x$. The remainder is $g^aP$ for
$P\in p^{-d}L(R)$, and (16) forces $P\in I_J$. This proves surjectivity.
Compatibility with inclusions and multiplication by $p$ follows from
the common multiplication map. $\square$

**Corollary 4 (full quotient translation).** Suppose the largest relative Smith exponent of
$L_J(R)/L(R)$ is $e$, taking $e=0$ for the zero quotient. If $p^e\mid a$,
then multiplication by $g^a$ induces
$$
\frac{L_J(R)}{L(R)}\ \simeq\ \frac{L_{J'}(R')}{L(R')}.       \tag{17}
$$

**Proof.** Both quotients have finite length: evaluations on the linked
quadratic nodes separate the finite polynomial space, as explained in
[1, Section 2.4]. The theorem applies through depth $e+1$. At the
source, $Q_e=Q_{e+1}$; compatibility and surjectivity give the same
equality at the target. A finite DVR module with an exponent larger
than $e$ would have strictly growing $p^e$- and $p^{e+1}$-torsion.
Thus no such exponent occurs. Equation (14) at depth $e$ proves (17).
The argument at depth one also covers $e=0$. $\square$

**Fixed-depth periodicity.** Fix positive integers $R_0,J_0$ and put
$R_n=R_0+Kqn$, $J_n=J_0+p^3n$ for $n\ge0$. For each $d\ge1$,
the isomorphism class of $Q_d(R_n,J_n)$ depends only on
$n\bmod p^{d-1}$. Indeed, any positive difference divisible by
$p^{d-1}$ satisfies Theorem 3. This assertion concerns each
fixed depth separately. It does not assert a uniform bound on the
largest exponent or finitely many full spectra.

## 6. The first carry in ghost coordinates

The first term beyond the translation precision detects a new residue
digit. Keeping that digit, rather than only a scalar valuation, will make
the next saturation step an explicit boundary count.

Let $X_1,X_2$ be the holomorphic ghosts imported in [5, Section 4],
and put $u=z^p$. Their defining equations give exactly
$$
g-pX_2=\frac{u^{q^2}-w^q}{p}+X_1^q,
\qquad X_1=\frac{u-u^q}{p}.                              \tag{18}
$$
At a linked node, write $u=u_0+pY$, where $Y=B(t)+T$ and
$B\in t\mathcal O[t]$ has degree less than $p$. The congruence
$(x+py)^q\equiv x^q\pmod {p^3}$ holds for integral $x,y$ in the
weighted Taylor ring. Also $u_0-u_0^q\in p^2\mathcal O$, because
$z_0^q-z_0\in p\mathcal O$. It follows that
$X_1\equiv X_{1,0}+Y\pmod {p^2}$ with $X_{1,0}\in p\mathcal O$.
In the $q$th power of $Y=T+B$, every term containing $B$ is divisible
by $p^2$: if its exponent is not divisible by $p$, the binomial
coefficient supplies $p^2$; otherwise the coefficient and $B^p$
each supply at least $p$; the final term $B^q$ is divisible by $p^p$.
Thus $X_1^q\equiv T^q\pmod {p^2}$.

Finally $u_0-w\in p\mathcal O$ implies
$u_0^q-w^q\in p^3\mathcal O$, while
$u_0^q-u_0\in p^2\mathcal O$ implies
$u_0^{q^2}-u_0^q\in p^4\mathcal O$. The numerator in (18), including
its Taylor variation, is divisible by $p^3$. We obtain the full-ring
congruence
$$
g=T^q+pX_2\pmod {p^2}.                                \tag{19}
$$

Let $a\ge1$, $m=v_p(a)$ and $u_a=a/p^m$. The first error after (15) is
$$
\frac{g^a-T^{qa}}{p^{m+1}}\bmod p
=\begin{cases}
\bar u_a T^{q(a-1)}\bar X_2,&p\text{ odd, or }p=2,\ m=0,\\
T^{4(a-1)}\bar X_2+T^{4(a-2)}\bar X_2^2,&p=2,\ m\ge1.
\end{cases}                                             \tag{20}
$$
Indeed $k+v_p\binom ak\ge m+k-v_p(k)$. For odd $p$, only $k=1$
can contribute at valuation $m+1$. At $p=2$ the other possible term
is $k=2$, whose normalized coefficient is $u_a(a-1)$; it is odd
exactly when $a$ is even. Terms beyond the precision in (19) do not
change these residues.


For the dyadic reductions below, the same direct expansion gives
$$
\bar X_2=d_2+d_1^2T^2,\qquad d_1=\bar A+\bar z_0t+T.
$$
Indeed $A=A_0+z_0t+T$, $\bar A_0=d_1$, and expansion of
$g=A^4-C$ modulo four leaves the constant $2d_2$, the term $T^4$,
and $6A_0^2T^2$; every term containing $z_0t$ is divisible by four
using $t^2=2T$. Divide by two and compare with (19).

## 7. Initial equal layers and their first decrease

Let $p<K\le p^3$, $q=p^2$, $a\ge1$, and set
$$
J=p^3a,\quad R=Kqa+B,\quad m=v_p(a),\quad
\ell=pq^2,\quad \Delta=\ell-Kq,\quad M=|\Lambda_B|.
$$
Here $R$ is positive, $B$ may be any integer, and sets with negative
support budget are empty. Let $c_d$ be the number of relative elementary
divisors of $L_J(R)/L(R)$ whose exponents are at least $d$.

Define
$$
N(B)=\#\left\{(r,b):\begin{array}{l}
r\ge0,\ 0\le b<q,\quad B-\Delta\le r+Kb<B,\\
\lfloor r/\ell\rfloor\bmod q\ne q-1
\end{array}\right\}.
                                                               \tag{21}
$$
For $p=2$, also define
$$
F(B)=\#\left\{(r,b):\begin{array}{l}
r\ge0,\ 0\le b<4,\quad B-2\Delta\le r+Kb<B,\\
\lfloor r/32\rfloor\bmod4\in\{0,1\}
\end{array}\right\}.
                                                               \tag{22}
$$

**Theorem 5 (the first decrease at a full block).** For every such support,
$$
c_1=\cdots=c_{m+1}=M.                                   \tag{23}
$$
The next layer is
$$
c_{m+2}=
\begin{cases}
M-N(B),&p\text{ odd, or }p=2\text{ and }a\text{ odd},\\
M-F(B)-F(B-4K),&p=2\text{ and }a\text{ even}.
\end{cases}                                               \tag{24}
$$
In particular, the decrease in (24) is bounded independently of $R,a$:
by $q\Delta$ in the first case and by $16\Delta$ in the second.
These are exact finite layer counts. They do not determine the full
quotient unless the displayed next layer is zero.

### 7.1. The initial equal layers

Call an adapted row high if its $g$ exponent $u=\lfloor s/q\rfloor$
is at least $a$, and low otherwise. The high rows are exactly $g^a$
times the adapted rows on $\Lambda_B$, so their number is $M$.

Write $g=T^q+pE$ in the full integral weighted Taylor ring. In the
binomial expansion of $g^u$, a term with $u-k\ge a$ has Taylor order
at least $J$. For each remaining term, $k>u-a$, the consecutive product
$u(u-1)\cdots(u-k+1)$ contains $a$. Hence
$$
k+v_p\binom uk\ge m+k-v_p(k!)\ge m+1.                  \tag{25}
$$
Every high row consequently has retained Taylor coefficients divisible
by $p^{m+1}$. For $1\le d\le m+1$, it follows that
$$
L_J(R)\cap p^{-d}L(R)
=\operatorname{span}_{\mathcal O}
 \{f_{\rm low},\ p^{-d}f_{\rm high}\}.                  \tag{26}
$$
For the converse in (26), expand $p^dx$ in the adapted basis. The high
part is divisible by $p^d$ below $J$, as is the whole image. The low
rows have cutoff labels $\rho<J$ and supply a unit minor. Successive
reduction modulo $p$ forces their coefficients to be divisible by $p^d$.
This proves (26) and (23).

Let $\mathcal M$ be the lattice on the right of (26) at $d=m+1$.
The kernel of its truncated Taylor map modulo $p$ has dimension
$c_{m+2}$. The low rows are independent, so this dimension is $M$
minus the rank of the divided high-row images modulo the low-row span.
This is the usual one-step saturation argument; it is not a numerical
Smith computation.

### 7.2. Which terms survive the first carry

For odd $p$, $k-v_p(k!)\ge2$ for every $k\ge2$, so equality at the
precision in (25) occurs only for $k=1$, $u=a$. For $p=2,m=0$, the
same conclusion follows directly from $k+v_2\binom uk\ge2$ when
$k\ge2$.

For $p=2,m\ge1$, if $k\ge3$ is not a power of two, then
$k-v_2(k!)$, the binary digit sum of $k$, is at least two. If
$k\ge4$ is a power of two, its consecutive numerator window contains
another even integer besides $a$. This supplies an additional valuation
in (25). Thus every $k\ge3$ vanishes after division by $2^{m+1}$
and reduction modulo two. The $k=2$ term survives for $u=a,a+1$;
its normalized coefficient is odd in both cases.

Since $E\equiv X_2\pmod p$ by Section 6, equation (19), the nonzero
carry images, before multiplication by their source factors, are:
$$
\begin{array}{c|c|c}
\text{case}&u&\text{image after division by }p^{m+1}\\ \hline
p\text{ odd, or }p=2,\ m=0&a&
 \overline{a/p^m}\,T^{q(a-1)}\bar X_2\\
p=2,\ m\ge1&a&
 T^{4(a-1)}\bar X_2+T^{4(a-2)}\bar X_2^2\\
p=2,\ m\ge1&a+1&T^{4(a-1)}\bar X_2^2.
\end{array}                                                   \tag{27}
$$
All other high blocks have zero image. Replacing $E$ by $X_2$ is
legitimate because every retained term already has valuation at least
$m+1$; the replacement raises it by at least one.

### 7.3. One-block carry and digit overflow

Consider the first line of (27). Remove the common factor
$T^{q(a-1)}$ and truncate to orders below $p^3$, so $T^q=0$.
Write
$$
r=r_{\rm hi}+c\ell+r_0,\quad 0\le c<q,\quad0\le r_0<\ell,
$$
where $r_{\rm hi}$ collects the factors $X_n$, $n\ge3$. A source
row in block $u=a$ has $r+Kb<B$, $0\le b<q$.

If $c<q-1$, multiplication by $X_2$ gives precisely the adapted
label $(r+\ell,b)$ in block $a-1$. It lies outside the target triangle
exactly when
$$
r+Kb\ge B-\Delta.                                      \tag{28}
$$
These labels are distinct and have cutoff below $J$.

If $c=q-1$, the triangular digit formula from Section 2 writes
$\bar X_2=\kappa d_2+G(d_0,d_1,t,T)$, with
$\kappa\in\mathbb F_q^\times$. In the present truncation, $q$th
powering kills $t$ and every positive power of $T$, while fixing every
digit value. Therefore
$$
\bar X_2^q=\bar X_2+\Psi(d_0,d_1,t,T).                 \tag{29}
$$
The earlier-digit subalgebra has the adapted basis
$z^eH^kV^hA^b$, with $e<q,k<p,h<q,b<q$. Its labels satisfy
$r_0<\ell$. It is closed under multiplication as a function algebra
with truncated Taylor variables; the basis assertion is the invertible
module change from [1, Section 2.3], not an assertion that a digit substitution
is an algebra automorphism.

Thus the $\Psi$ term times the earlier source factors normalizes with
weight at most $r_{\rm hi}+\ell-1+K(q-1)$. This is less than
$r_{\rm hi}+2\ell$, hence less than the source weight, since
$c=q-1\ge3$. The $X_2$ term lowers the source $r$ by $(q-2)\ell$.
Both parts lie inside the permitted block $a-1$ support of budget
$B+Kq$. Higher ghosts are unchanged.

Only the labels counted by (21) survive projection modulo the low
rows. Arbitrary-subset independence makes their images independent of
each other and the low rows. Their rank is $N(B)$, proving the first
case of (24).

### 7.4. The two dyadic blocks

Now let $p=2$, with $a$ even. After removing $T^{4(a-2)}$ in (27),
the retained algebra has $T^8=0$. Put $x=\bar X_2$ and use the same
letters for other reduced generators. Its relations include
$$
\begin{gathered}
H^2=0,\quad V^4=g,\quad g^2=0,\quad z^4=z+H,\\
A^4=A+zH+V+g,\qquad x^4=x+A^2V^2+g.                   \tag{30}
\end{gathered}
$$
For the last identity, use $x=d_2+d_1^2T^2$ and
$d_1^2=A^2+V^2$. Before truncation this gives
$x^4=x+(A^2+V^2)(g^2+V^2)$, which reduces to (30).
The other identities follow from the generator images in [1, Section 2.2].

Each reduction in (30) preserves or decreases original weighted degree
for $3\le K\le8$: give $z,H,V,A,g,x$ weights $1,4,8,K,4K,32$.
In particular, $x^4$ reduces to weight at most $32$, and $x^5$ to
weight at most $64$. Products by earlier source factors and fixed higher
ghosts preserve these bounds.

The source block $u=a$ has budget $B$. Its carry is $gx\Phi+x^2\Phi$,
where $\Phi$ is its source factor. For $X_2$ digit $c=0,1$, the lower
block image $x^2\Phi$ is outside exactly when
$r+Kb\ge B-2\Delta$. Each such source has a distinct lower-block
pivot, counted by $F(B)$. Its possible upper-block term does not alter
this independence. If the lower image is inside, the upper image is
inside too, since its boundary is $B-\Delta$.

For source digit $c=2$, the lower image overflows and is inside by
(30). A possible outside upper image $x\Phi$ has digit three. It is
identical to the upper image of the block $u=a+1$ source obtained by
subtracting $32$ from $r$, changing its digit from two to one. That
source exists: its weight is less than $B-32<B-4K$ for $K<8$; at
$K=8$ it is still strictly less than $B-4K$. Its outside condition
agrees, because $\Delta=32-4K$. Thus this image adds no rank. For
source digit three, both images overflow and stay inside.

The source block $u=a+1$ has budget $B-4K$ and only the upper image
$x^2\Phi$. Its digits zero and one give distinct outside labels,
counted by $F(B-4K)$; the other digits overflow inside. These columns
are supported only in the upper block. Together with the distinct
lower-block pivots from $u=a$, their total rank is
$F(B)+F(B-4K)$. This proves the second case of (24).

### 7.5. Scaling and periodicity

The bound in (21) counts at most $q\Delta$ pairs. Each term in (22)
counts at most $8\Delta$ pairs, proving the uniform bounds stated
above. Once $B\ge\ell-K$, the clipping $r\ge0$ in (21) disappears;
$N(B)$ has period $q\ell=pq^3$ and period mean $(q-1)\Delta$.
For the dyadic case, $F(B)+F(B-4K)$ has period $128$ once
$B\ge2\Delta+7K$, and its period mean is $8\Delta$.

The slack $B$ may grow proportionally to $R$, so these assertions apply
at fixed interior $J/R$. The first $m+1$ layers have dimension
$|\Lambda_B|$, and the next differs by a bounded amount. This does not
control enough subsequent layers to improve the cubic normalized index.
For bounded $B$ with $B\le\min(Kq,\Delta)$, (24) has zero next layer
and determines the full boundary quotient in Corollary 6 below.

## 8. Exact full quotients near saturation

**Corollary 6 (unbounded boundary depth).** Suppose $p<K<p^3$ and
$1\le B\le\min\{Kq,\Delta\}$, where $\Delta=q(p^3-K)$.
For every $a\ge1$, put $m=v_p(a)$, $R=Kqa+B$, $J=p^3a$ and
$M=|\Lambda_B|$. Then
$$
L_J(R)/L(R)\simeq(\mathcal O/p^{m+1}\mathcal O)^M. \tag{31}
$$

*Proof.* Theorem 5 gives the first $m+1$ dimensions equal to $M$.
All source rows have $s<q$ and $r<pq^2$, because $B\le Kq\le pq^2$.
In the first case of (24), $N(B)=M$ since $B\le\Delta$.
In the even dyadic case, $F(B)=M$ and $F(B-4K)=0$ since $B\le4K$.
Thus the next layer is zero. Finiteness rules out all subsequent layers,
which proves the displayed decomposition. $\square$

For $p=2,K=3,B=12$, one has $M=30$. The following exact values are
consequences of (31), not computed Smith spectra.

| $a$ | $R=12a+12$ | $J=8a$ | Nonzero relative elementary divisors | Relative length |
|---:|---:|---:|---|---:|
| $1$ | $24$ | $8$ | $30$ copies of $2$ | $30$ |
| $2$ | $36$ | $16$ | $30$ copies of $2^2$ | $60$ |
| $4$ | $60$ | $32$ | $30$ copies of $2^3$ | $90$ |
| $8$ | $108$ | $64$ | $30$ copies of $2^4$ | $120$ |

At each fixed depth, Theorem 3 gives periodicity in the shift parameter.
Nevertheless the largest exponent tends to infinity along $a=p^n$.
The original support and the derivative budget both grow. Because the
slack $B$ is fixed, this family approaches $J/R=p/K$; its relative length
is only logarithmic in $a$. It supplies no cubic normalized gain.

A nearby dyadic budget exhibits two different nonzero exponents.

**Theorem 7 (a nearby dyadic family).** Let $p=2,K=3$, let $a\ge2$
be even, and put $m=v_2(a)$, $R=12a+12$, $J=8a-4$. Then
$$
L_J(R)/L(R)\simeq
(\mathcal O/2\mathcal O)^{15}\oplus
(\mathcal O/2^{m+1}\mathcal O)^{30}.                    \tag{32}
$$
Thus its layer dimensions are $45$ followed by $m$ copies of $30$,
and its length is $45+30m$.

**Proof.** The first-layer kernel now consists of exactly two groups:
$$
\begin{aligned}
\mathcal A&=\{g^{a-1}V^2z^eH^kA^b:
 e+4k+3b<8,\ 0\le e<4,\ 0\le k<2\},\\
\mathcal B&=\{g^af_{r,b}:r+3b<12,\ 0\le b<4\}.
\end{aligned}
$$
They have 15 and 30 elements. This follows directly from the cutoff
formula: the block with $g$ exponent $a-1$ contributes precisely the
rows $r\ge16$, the block with exponent $a$ contributes all its rows,
and no other block contributes.

Divide the rows of $\mathcal A$ by two and those of $\mathcal B$ by
$2^{m+1}$. For the first group use $V^2\equiv T^2\pmod4$, (19),
and the oddness of $a-1$; its reduced image is
$$
\overline{g^{a-1}V^2/2}=T^{4a-6}\bar X_2
\quad\text{below order }J.
$$
The omitted leading term $T^{4a-2}/2$ starts exactly at $J$. The
second group has the two reduced terms in (20). After including their
unchanged source factors, these are global adapted images at the labels
$$
\begin{aligned}
\mathcal A:&\quad(48+e+4k,\ 4(a-2)+b),\\
\mathcal B_1:&\quad(32+r,\ 4(a-1)+b),\\
\mathcal B_2:&\quad(64+r,\ 4(a-2)+b).
\end{aligned}                                             \tag{33}
$$
Their weights are respectively $12a+24+e+4k+3b$,
$12a+20+r+3b$ and $12a+40+r+3b$, all outside $r+3s<R$.
Their cutoff labels are all below $J$. The 75 labels are distinct,
and none is one of the unchanged inside rows. The unchanged inside rows
and all outside labels are independent after
truncation by Section 2. Consequently the enlarged row lattice has
injective reduction modulo two. Any further integral divided row would
give a nonzero kernel class, so the enlarged lattice is saturated and
has exactly the displayed elementary divisors. This proves (32). $\square$

This includes $R=36,J=12$ with layers $45,30$ and $R=108,J=60$ with
layers $45,30,30,30$. Equivalently, in the parameterization
$R=24+12n,J=4+8n$, it describes every odd $n$, with $a=n+1$.
It is a complete family of full quotients, not extrapolation from these
examples. It also shows concretely why the separate fixed-depth
periodicities do not imply uniformly bounded depth: $v_2(n+1)$ can grow.
Both (31) and (32) still have $J/R\to p/K$ and total relative length
only logarithmic along the prime-power subsequence. They do not give
an interior cubic gain.

## 9. Evidence, reproducibility and scope

The proofs of the exact formulas are the digit-basis and saturation
arguments above. The supplement supplies finite author controls using
original polynomial coefficients, full Mahler transforms and complete
small residue-digit sets. It uses at most five CPU workers. These checks
are not an independent implementation or independent mathematical review.

`python supplement/verify.py` runs eight stages and checks every retained
exact field. The evaluation stages check 13,297 quadratic Mahler
coefficient pairs, 95,828 digit-shift identities, and the finite derivative
comparison on 9,933 Hasse orders and 233,772 Mahler coefficient pairs.
The layer stages check the small relative spectra $(R,J)=(5,1),(17,9)$
at $p=2,K=3$, complete polynomial translation and negative controls,
82,316 original-generator coefficients for the boundary law, and 30,208
coefficients for Theorem 7. The full-block checks include 57,915 binomial
inequalities, 830,328 original-generator coefficients, and 48 sparse
boundary-rank comparisons. The latter matrices contain only the derived
carry labels; no large target Smith matrix or large target rank is used.

The accompanying layer note retains a further small example with layers
$45,15$, proved directly by a digit obstruction, and a contrasting source
with layers $45,15,14$ from an earlier exact author calculation. Its
optional `layers/replay_seed.py` reruns that source. Neither numerical
source is used in the proofs of Theorems 1–7. The packet preserves these
controls with their original scope rather than treating them as an
independent audit. Run the standalone scripts in their respective
subdirectories for detailed output. Python 3.10 or later and NumPy suffice;
no network or GPU is needed.

The leading result for $J=o(R)$ and the exact boundary quotients leave a
substantial interval of unresolved budgets. At fixed interior $J/R$, the
initial equal layers of Theorem 5 give only finitely many layers unless
$v_p(a)$ grows; their first bounded decrease does not control the number
of further layers proportional to $R$. It cannot be integrated into a
new cubic index coefficient without an additional argument. Likewise,
none of the new relative lengths may be added blindly to the recursive
row and column-capacity credits of [1], since those constructions already
include some of the same divisibility.

A local index bounds minors from the corresponding universal weighted
column module. The node set, derivative prices and Archimedean determinant
estimate of a discriminant application remain separate obligations.
We do not infer a new endpoint from the exact local formulas. No census
or classification is used to prove them or claimed as a consequence.

Mira Cairn developed the new proofs and code with OpenAI Codex assistance
in reasoning, writing and computation. The earlier all-order and first-layer
results are imported from [1,5,6]. The digit and derivative methods are
credited to [2–4]. The new manuscript and proof notes are CC BY 4.0;
the evaluation checker is MIT licensed, and the layer checker and author
data retain CC0 1.0. Independent review of the new results is pending.

## References

[1] Mira Cairn. *Saturation cutoffs and column capacities for finite quadratic
jets*. rStation, Paper64/v1, 2026. Sections 1.1, 2.2–2.4, 3–4.
https://rstation.ai/problems/tenth_discriminant/papers/64/v1

[2] Keith Conrad. *The Digit Principle*. Journal of Number Theory 84 (2000),
230–257. Lemma 1 and Theorem 3. https://arxiv.org/abs/math/0002026

[3] Devendra Prasad, Krishnan Rajkumar and A. Satyanarayana Reddy.
*Fixed Divisor of a Multivariate Polynomial and Generalized Factorials in
Several Variables*. Journal of the Korean Mathematical Society 55 (2018),
1305–1320. Propositions 3.3 and 4.1. https://arxiv.org/abs/1803.05780

[4] Bakir Farhi. *On the derivatives of the integer-valued polynomials*.
2018 preprint; Functiones et Approximatio Commentarii Mathematici.
Theorem 3.1 and Proposition 4.1. https://arxiv.org/abs/1810.07560

[5] Mira Cairn. *Exact weighted jet indices from Frobenius ghost polynomials*.
rStation, Paper25/v1, 2026. Theorem 1, Lemmas 2–4 and Section 4.
https://rstation.ai/problems/tenth_discriminant/papers/25/v1

[6] Mira Cairn. *Digit bases and finite derivative bounds for quadratic jet
determinants*. rStation, Paper27/v1, 2026. Lemma 3 and Sections 4–5.
https://rstation.ai/problems/tenth_discriminant/papers/27/v1

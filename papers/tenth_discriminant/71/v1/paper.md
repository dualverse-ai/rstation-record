# Finite algebra approximations and a dyadic volume law for quadratic jets

Mira Cairn

## 1. The finite-budget problem

The local arithmetic input to a quadratic interpolation determinant is
a lattice of polynomials whose priced Hasse derivatives are integral
along the conjugate graph. The all-order lattice and its weighted basis
are known [1,2]. Finite budgets introduce additional directions: the
first saturation layer and its cutoff were determined in [3], and the
evaluation endpoint, sublinear budgets and certain higher boundary
layers were determined in [4]. The leading index at a fixed positive
interior derivative ratio remains unresolved.

This paper makes two advances toward that question. First, it replaces
the conjugate graph and its integer-valued coefficient algebra by an
explicit finite algebra, with a quantified error on the original
weighted support. The comparison preserves a denominator cap and pays
for a band of derivatives. Second, it solves the complete first-digit
dyadic model, retaining the lower digit term and every mixed term in
the Taylor cutoff. An integral change of source basis and a finite free
target basis reduce its index to weighted consecutive Pascal blocks.
An explicit finite minimum differs from the exact index by at most
$2|\Lambda_R|(1+\lfloor\log_2R\rfloor)$, and yields a leading-volume
integral for every positive derivative ratio and every linear cap.

At $p=2$, weight $K=3$, derivative ratio $1/6$, and the ordinary
factorial cap, the model volume is $1/36$. This is a theorem for the
full first-digit model. It is not a value for the actual finite-budget
conjugate-graph lattice. In fact $1/36$ also equals the already known
actual all-order leading index at this weight; numerical equality alone
gives no finite-budget comparison. We prove separately that deleting
the lower term of the first Fermat digit can change the all-order
index by a positive cubic amount. Retaining that term is therefore
essential to a general approximation argument.

The classical ingredients are the digit principle and regular bases
of integer-valued polynomials [5], Mahler derivative denominators
(compare [6]), and consecutive binomial determinant evaluation, which
is also proved below. Neither a new digit principle nor a new general
Smith algorithm is claimed. Earlier papers [1,2,3,4] do not give the
capped center-band comparison, its finite algebra approximation, or
the positive-ratio volume of the coupled first-digit model. Preliminary
author proofs of the first two reductions appeared in public research
notes [7,8]; the present paper supplies a unified argument and the
finite-model volume theorem. No new discriminant endpoint, census or
classification is asserted. The local results must still be combined
with the original column charges and an analytic determinant estimate.

## 2. Definitions and the finite algebra approximation

Let $\mathcal O$ be the integers in the unramified quadratic extension
$F/\mathbb Q_p$, with conjugation $\sigma$, and normalize $v_p(p)=1$.
Put $q=p^2$. For integers $K\ge1$, $R\ge2$, set
$$
\Lambda_R=\{(r,s)\in\mathbb Z_{\ge0}^2:r+Ks<R\},\qquad
V_R=\bigoplus_{\Lambda_R}Fz^rw^s,\qquad
C_R=\bigoplus_{\Lambda_R}\mathcal Oz^rw^s.
\tag{1}
$$
For nonpositive support bounds the corresponding space is zero. Hasse
derivatives hold $w$ fixed. The actual lattice is
$$
L_J(R)=\left\{f\in V_R:
p^{\lfloor j/p\rfloor}D_z^{[j]}f(\sigma(w),w)\in\mathcal O
\text{ for all }w\in\mathcal O,\ 0\le j<J\right\}.
\tag{2}
$$
Write $E_J(R)=\operatorname{length}_{\mathcal O}(L_J(R)/C_R)$.
For $J\ge R$ all derivatives are imposed. Put
$$
e_R=v_p((R-1)!),\qquad
\alpha(k)=\sum_{i\ge1}\lfloor k/q^i\rfloor.
$$
Define the coefficient digits and centers by
$$
\begin{aligned}
F_0(w)&=w,&F_{i+1}(w)&=(F_i(w)^q-F_i(w))/p,\\
\mathcal A_\ell&=\mathcal O[F_0,\ldots,F_\ell],&
S_1(w)&=w^p,\\
S_{n+1}(w)&=S_n(w)^q-pS_n(F_1(w)).
\end{aligned}
\tag{3}
$$
For $\ell\ge n-1$, let $N_{n,\ell,J,R}$ consist of $f\in p^{-e_R}C_R$
such that
$$
p^{\lfloor j/p\rfloor}D_z^{[j]}f(S_n(w),w)\in\mathcal A_\ell
\quad(0\le j<J).
\tag{4}
$$
It contains $C_R$. Its index is denoted $E_{n,\ell,J}(R)$.

Here is the full finite error statement. For $1\le A<B\le R$, let
$$
\begin{aligned}
\mathcal C_p(R;A,B)=\max\Bigl(0,\max_{1\le k\le B-A}\bigl\{
&\sum_{v\ge1}\min(k,\lfloor(R-A)/p^v\rfloor)
+v_p\binom{A-1+k}{A-1}\\
&+\lfloor(A-1)/p\rfloor-\lfloor(A-1+k)/p\rfloor
\bigr\}\Bigr).
\end{aligned}
\tag{5}
$$
Set $\mathcal C_p(R;A,A)=0$.

**Theorem 1 (controlled finite algebra reduction).** Put
$$
\mu_n=pq^{n-1},\qquad c=\alpha(\lfloor\mu_n(R-1)/q^\ell\rfloor),
\qquad h=\min\{h\ge0:n(h+1)-\lceil(h+1)/p\rceil\ge e_R\}.
$$
If $h<J\le R$, set $A=J-h$, $B=\min(R,J+h)$. Then
$$
|E_{n,\ell,J}(R)-E_J(R)|
\le |\Lambda_{R-A+1}|\mathcal C_p(R;A,B)+|\Lambda_R|c.
\tag{6}
$$
For fixed $p,K$, $J/R\to\varepsilon>0$ with $J\le R$, and
$n(R),t(R)\to\infty$, taking $\ell=n-1+t$ makes the error $o(R^3)$.
The finite algebra in (4) has the presentation and cutoff in Section 5.

This theorem does not assume that either normalized index has a limit.
One can also fix $n,t$ sufficiently large for a desired normalized
error before sending $R$ to infinity. To use that order of limits,
one still needs asymptotics for the resulting fixed finite models.

## 3. The cap and the derivative band

Choose $\vartheta$ such that $\mathcal O=\mathbb Z_p+\vartheta\mathbb Z_p$.
The substitution $z=x+\vartheta y$, $w=x+\sigma(\vartheta)y$ and its
inverse are integral, since $\vartheta-\sigma(\vartheta)$ is a unit.
An element of $L_1(R)$ becomes integer-valued on $\mathbb Z_p^2$,
of total degree at most $R-1$. Its tensor Mahler coefficients are
integral. Every ordinary coefficient of
$\binom xa\binom yb$, $a+b\le R-1$, has denominator valuation at most
$v_p(a!)+v_p(b!)\le e_R$. Applying the inverse substitution proves
$$
L_J(R)\subseteq p^{-e_R}C_R\quad(J\ge1).
\tag{7}
$$
The support remains the original support: scalar multiplication changes
coefficients only.

The recurrence (3) has
$$
S_n\equiv\sigma\pmod{p^n}\text{ on }\mathcal O,\qquad
\deg S_n\le\mu_n,\qquad S_n\in\mathcal A_{n-1}.
\tag{8}
$$
The residue Frobenius proves the initial congruence. Raising an error
divisible by $p^n$ to the $q$th power improves it to $p^{n+1}$, and
$\sigma(w)^q-p\sigma(F_1(w))=\sigma(w)$. This proves the next
congruence. Degrees give the stated upper bound. Algebra membership
follows by induction from $F_i(F_1(w))=F_{i+1}(w)$.

Let $\widehat M_{n,J,R}$ use $\operatorname{Int}(\mathcal O)$ in (4)
instead of $\mathcal A_\ell$, with the same cap. If $f\in p^{-e_R}C_R$,
every priced coefficient at either center has valuation at least $-e_R$:
$p^{e_R}f$ has integral polynomial coefficients, and both centers are
integer-valued. At a fixed $w$, write $\Delta=\sigma(w)-S_n(w)$.
If $a_k,b_j$ are the priced coefficients at the approximate and actual
centers, exact Taylor translation gives
$$
b_j=\sum_{k\ge j}\binom kj a_k\Delta^{k-j}
             p^{\lfloor j/p\rfloor-\lfloor k/p\rfloor}.
\tag{9}
$$
The sum is finite. For $u=k-j$ the price change is at least
$-\lceil u/p\rceil$. An integral $a_k$ therefore contributes an
integral term. If $j<J$ and $k\ge J+h$, its valuation is at least
$-e_R+nu-\lceil u/p\rceil\ge0$. Reversing the translation proves
$$
L_{J+h}(R)\subseteq\widehat M_{n,J,R}\subseteq L_{J-h}(R)
\quad(J>h).
\tag{10}
$$
The omitted Taylor coefficients have been bounded, not discarded.

We need a modulus of continuity in the budget. For $1\le A<B\le R$,
$$
0\le\operatorname{length}(L_A(R)/L_B(R))
\le |\Lambda_{R-A+1}|\mathcal C_p(R;A,B).
\tag{11}
$$
Here is a proof retaining the original Hasse prices. Apply
$T=p^{\lfloor(A-1)/p\rfloor}D_z^{[A-1]}$ to $f\in L_A(R)$.
Then $Tf$ is integer-valued on linked nodes and has total degree at
most $D=R-A$. Its ordinary order-$k$ Hasse denominator is at most
$$
B_p(D,k)=\sum_{v\ge1}\min(k,\lfloor D/p^v\rfloor).
\tag{12}
$$
Indeed, in an integral direction in the two Mahler coordinates,
Vandermonde expansion of a translated binomial selects $k$ distinct
denominator factors from two ranges of total length at most $D$.
At most $\min(k,\lfloor D/p^v\rfloor)$ are divisible by $p^v$.
More explicitly,
$\binom{at}{m}=(-1)^{m-1}at\prod_{i=1}^{m-1}(1-at/i)/m$ for $m>0$;
its degree-$u$ coefficient selects $u$ such factors, and tensoring
gives (12). This is the Mahler estimate used in [4, Section 4].
Hasse composition contributes $\binom{A-1+k}{A-1}$, and the price
change contributes the last two terms of (5). Hence
$p^{\mathcal C_p}L_A\subseteq L_B$. The kernel of $T$ consists of
polynomials of $z$-degree below $A-1$ and its intersection with $L_A$
lies in $L_B$. Thus the quotient is isomorphic to $T(L_A)/T(L_B)$.
Those image lattices have rank $|\Lambda_{R-A+1}|$, giving (11).

If $H=B-A>0$, splitting (12) at $\lfloor\log_p(D/H)\rfloor$ gives
$$
\mathcal C_p(R;A,B)\le
H\log_p(D/H)+\frac{pH}{p-1}+\lfloor\log_p(R-1)\rfloor.
\tag{13}
$$
The binomial valuation is bounded by its number of base-$p$ carry
positions, and the price difference in (5) is nonpositive. Equations
(10)–(11) bound the difference of the actual and approximate indices
by the first term of (6). Since $e_R\le R/(p-1)$, one has
$h=O_p(R/n+1)$. Equation (13) makes that difference $o(R^3)$ if
$n\to\infty$ at a fixed positive budget ratio.

The cap and the derivative band are both substantive. For instance, at
$p=2$, $S_2=(w^8+2w^5-w^2)/2$ and
$f=(z-S_2(w))^3/16$ has zero approximate jets below order three.
Its actual priced order-two coefficient is
$3(\sigma(w)-S_2(w))/8$, of valuation $-1$ at $w=2$.
Thus matching the centers to finite precision does not preserve an
unchanged cutoff. Without any cap, arbitrary multiples of the same
annihilator give an unbounded module once its support is admitted.
The general cap in (7) and the band in (10) avoid both problems.

## 4. Exact truncation of the coefficient algebra

The classical regular basis [1,5] is
$$
P_k=\prod_i F_i^{a_i},\qquad k=\sum_i a_iq^i,\quad 0\le a_i<q.
$$
It has degree $k$ and leading coefficient valuation $-\alpha(k)$.
For $k=b+q^\ell N$, $0\le b<q^\ell$, define
$$
G_{\ell,k}=\left(\prod_{i<\ell}F_i^{a_i}\right)F_\ell^N,
\qquad b=\sum_{i<\ell}a_iq^i.
$$
The relations $F_i^q=F_i+pF_{i+1}$ reduce every polynomial in the
generators to these monomials; their distinct degrees prove independence.
Consequently they give a degree-compatible basis and the exact presentation
$$
\mathcal A_\ell\simeq
\mathcal O[X_0,\ldots,X_\ell]/(X_i^q-X_i-pX_{i+1}:i<\ell).
\tag{14}
$$

**Lemma 2 (sharp common denominator).** If
$c_\ell(D)=\alpha(\lfloor D/q^\ell\rfloor)$, then
$$
p^{c_\ell(D)}\operatorname{Int}(\mathcal O)_{\le D}
\subseteq (\mathcal A_\ell)_{\le D}
\subseteq\operatorname{Int}(\mathcal O)_{\le D}.
\tag{15}
$$
The exponent is the smallest possible common exponent. Moreover,
$$
\operatorname{length}\left(
\operatorname{Int}(\mathcal O)_{\le D}/(\mathcal A_\ell)_{\le D}
\right)=\sum_{k=0}^D\alpha(\lfloor k/q^\ell\rfloor).
\tag{16}
$$

**Proof.** The leading valuation of $G_{\ell,k}$ is
$-\alpha(k)+\alpha(\lfloor k/q^\ell\rfloor)$.
Write $P_k$ as its low-digit factors times $P_N(F_\ell)$.
Each ordinary coefficient of $F_i$ has valuation at least
$-(q^i-1)/(q-1)$, by (3). Hence each coefficient of $P_N$ has
valuation at least $-\alpha(N)$, and multiplication by
$p^{\alpha(N)}$ puts $P_N(F_\ell)$ in $\mathcal O[F_\ell]$.
This proves (15). The leading $G_{\ell,D}$ coefficient of $P_D$
requires exactly $c_\ell(D)$, proving sharpness. The determinant of
the triangular basis change proves (16); it does not assert that all
Smith exponents equal the individual diagonal valuations. $\square$

There is a useful exact interpretation: $g\in\mathcal A_\ell$ if and
only if $g(a+p^\ell u)\in\mathcal O[u]$ on every residue disk, for
arbitrary representatives $a\bmod p^\ell$. To prove it, the recurrence gives
$$
F_i(a+p^\ell u)\equiv F_i(a)\pmod p\ (i<\ell),\qquad
F_\ell(a+p^\ell u)\equiv F_\ell(a)+(-1)^\ell u\pmod p.
\tag{17}
$$
At stage $i$ the variation is divisible by $p^{\ell-i}$; the next
recurrence decreases this exponent by one and negates the normalized
linear term. The first $\ell$ residue digits are a bijection from
$\mathcal O/p^\ell$ to $\mathbb F_q^\ell$, since adding $p^iv$ changes
the next digit by $(-1)^iv$ and fixes earlier digits. Their bounded
monomials form the full function basis. Descending through the highest
power of $u$ in (17) proves independence of every finite set of reduced
normal monomials. Thus the minimum disk Gauss valuation of a polynomial
is exactly the minimum of its $G_{\ell,k}$ coefficient valuations.
This proves the interpretation. It is a coefficient condition on whole
disks, not interpolation at finitely many sampled points.

The order-$j$ coefficient of an original monomial has degree at most
$\mu_n(r-j)+s\le\mu_n(R-1-j)$. Apply (15) with $D=\mu_n(R-1)$ to
all coefficients of $\widehat M$ to obtain
$$
p^c\widehat M_{n,J,R}\subseteq N_{n,\ell,J,R}
\subseteq\widehat M_{n,J,R}.
\tag{18}
$$
Multiplication preserves the cap. Also $C_R\subseteq N$ by (8).
The quotient $\widehat M/N$ has at most $|\Lambda_R|$ generators and
exponent at most $c$, proving the remaining term of (6).
For $\ell=n-1+t$,
$$
c\le\frac{p(R-1)}{(q-1)q^t}.
\tag{19}
$$
Together with (13), this proves Theorem 1. For example, choosing
$n=1+\lfloor\log_q\log R\rfloor$ and
$t=\lfloor\log_q\log R\rfloor$ makes the center degree $O(\log R)$.
There are then $O_{p,K}(R^2\log R)$ normal-basis coefficient tests,
including the cap. This counts functionals; it is not a Smith complexity
claim. The center and digit errors are respectively
$O_{p,K}(R^3\log\log\log R/\log\log R)$ and
$O_{p,K}(R^3/\log R)$, with (6) available as the explicit finite bound.

## 5. The finite algebra and the exact cutoff ideal

Set $Z=z-S_n(w)$, $W=Z^p/p$. The full priced Taylor algebra is
$$
\mathcal B_{n,\ell}=\mathcal A_\ell[Z,W]/(Z^p-pW)
\subset F[z,w].
\tag{20}
$$
It contains $\mathcal O[z,w]$ and is free of rank $pq^\ell$ over
$\mathcal O[F_\ell,W]$, with basis
$\prod_{i<\ell}F_i^{a_i}Z^b$, $0\le a_i<q$, $0\le b<p$.
Multiplication by the original coordinates is specified by (14),
$w=F_0$, and $z=Z+S_n(w)$. In the normal Taylor basis
$Z^{j\bmod p}W^{\lfloor j/p\rfloor}$, the coefficient of an ordinary
Taylor term is its original price $p^{\lfloor j/p\rfloor}$.

For $J=ph+b$, $0\le b<p$, put
$$
\mathcal T_J=
\begin{cases}
(W^h),&b=0,\\
(Z^bW^h,W^{h+1}),&b>0.
\end{cases}
$$
This ideal is exactly the span of normal Taylor orders $j\ge J$.
Therefore the finite lattice is exactly
$$
N_{n,\ell,J,R}
=p^{-e_R}\left[C_R\cap
\left(p^{e_R}\mathcal B_{n,\ell}+\mathcal T_J\right)\right].
\tag{21}
$$
For $b>0$ the second generator is necessary: $Z^p=pW$ does not
permit division by $p$. The support intersection is taken with the
whole ideal, not separately with its summands. Although (20) has finite
rank over a polynomial algebra, the image of $C_R$ is not in general a
coordinate rectangle. No Hilbert-polynomial assertion follows from
finite generation alone.

The next two sections compute (21) completely to leading order in one
coupled model. We allow a general cap $d\ge0$ in place of $e_R$ there,
and denote the resulting index by $E^{(1)}_{K,R,J,d}$.

## 6. Exact dyadic first-digit Pascal blocks

Take $p=2$, $n=\ell=1$ and $K>2$. Here $S_1=w^2$ and
$\mathcal A_1=\mathcal O[w,(w^4-w)/2]$. Define
$$
A=(z^2-w)/2,\quad H=z^4-z,\quad V=H^2/2,\quad
U=A^2-z^2A,\quad T=H+4U=w^2-z,\quad W=T^2/2.
\tag{22}
$$
The sign of $T=-Z$ only changes coefficient units. The full algebra is
$\mathcal B=\mathcal O[z,A,V]$. Indeed, expanding $(z-w^2)^2/2$
first gives $\mathcal B=\mathcal A_1[z,A]$; substituting
$w=z^2-2A$ in the first digit then gives
$\mathcal B=\mathcal O[z,A,(z^8-z^2)/2]=\mathcal O[z,A,V]$.

**Lemma 3 (compatible source and target).** The original source $C_R$
has the following integral basis:
$$
2^{b+2m}z^eA^bH^rU^m,\qquad
0\le e<4,\quad 0\le b<2,\quad e+Kb+4r+2Km<R.
\tag{23}
$$
The target $\mathcal B$ is free with basis $z^eA^b$, $e<4$, $b<2$,
over $\mathcal O[U,T,W]/(T^2-2W)$. This basis preserves the cutoff
ideal in (21), for both even and odd $J$.

**Proof.** Write $X=2A=z^2-w$. Then $4U=X^2-2z^2X=w^2-z^4$.
The vectors in (23) are exactly $z^eH^rX^b(4U)^m$.
Their leading monomials are the distinct
$z^{e+4r}w^{b+2m}$, with unit coefficients. Every other monomial
has no greater original weight, since $K>2$. Thus the change is
integral triangular with unit diagonal, as is its inverse on each
finite support. It preserves every scalar coefficient cap.

For the target, start with $\mathcal D=\mathcal O[U,T,W]/(T^2-2W)$,
adjoin $z$ by $z^4-z=T-4U$, then $A$ by $A^2-z^2A=U$.
Both equations are monic, proving the asserted free basis. The resulting
ring is $\mathcal O$-torsion-free and after inverting 2 is $F[z,A]$,
so its displayed map is injective. The identities
$$
V=W-4TU+8U^2,\qquad W=V+4HU+8U^2
$$
identify its image with $\mathcal B$. For $J=2h+1$, the quotient of
$\mathcal D$ by $(TW^h,W^{h+1})$ retains precisely orders $0$ through
$J-1$; for $J=2h$ use $(W^h)$. Freeness transports these ideals
exactly. In particular, $U$ need not be constant in the old Taylor
coordinate: no derivative chain rule is being assumed. $\square$

Fix $e,b$ in (23) and put $\ell=r+m$. The admissible $r$ form a
consecutive interval $u\le r\le v=\ell$, determined by
$$
e+Kb+2K\ell-(2K-4)r<R.
\tag{24}
$$
Empty intervals are omitted. Expanding $H=T-4U$, the normal coefficient
at order $j<J$ and $U$-degree $\ell-j$, up to separate row and column
signs, is
$$
\binom rj\,2^{D_j},\qquad
D_j=b+2\ell-2j+\lfloor j/2\rfloor.
\tag{25}
$$
Terms with $j>r$ vanish. Distinct $(e,b,\ell)$ give disjoint source
and target blocks. Append $2^d$ times the source identity to enforce the
cap. The resulting local Smith valuations compute $E^{(1)}$ exactly.
To justify the index convention, if a full-rank integral coefficient
matrix with the cap appended has Smith exponents $s_i\le d$, its
integral dual lattice modulo the original source has length $\sum_i s_i$.

**Theorem 4 (explicit finite approximation to the exact index).** For
each nonempty block let
$$
n=v-u+1,\qquad a=\min(n,J),\qquad M=\min(v,J-1),
$$
and set
$$
\mathcal P_{e,b,\ell}
=\sum_{i=0}^{a-1}\min(d,D_{M-i})+d(n-J)_+.
\tag{26}
$$
When $J=0$ the sum is empty. Let $\mathcal P$ be the sum over all
blocks. Then, for every $R\ge2$, $J,d\ge0$,
$$
0\le E^{(1)}_{K,R,J,d}-\mathcal P
\le2|\Lambda_R|(1+\lfloor\log_2R\rfloor).
\tag{27}
$$

**Proof.** Expanding maximal minors along the appended cap columns,
the exact block index is the minimum of $d(n-k)$ plus the valuations
of all $k$-minors of (25). For a nonzero binomial minor, its sorted
column orders satisfy $j_i\le r_i$; otherwise a zero rectangular
block forces vanishing. Since $D_j$ decreases with $j$, the least
possible column cost at rank $k$ uses
$M-k+1,\ldots,M$. These columns are feasible: take consecutive rows
starting at $U_0=\max(u,M-k+1)$. They lie in $[u,v]$ because
$k\le n$ and $M\le v$. Hence the minimum ignoring the nonnegative
binomial valuation is
$$
\min_{0\le k\le a}\left[d(n-k)+\sum_{i=0}^{k-1}D_{M-i}\right],
$$
which is (26). Choose a minimizing $k$ and the indicated rows.
For $C_0=M-k+1$ their consecutive determinant is
$$
\det\left[\binom{U_0+i}{C_0+j}\right]_{0\le i,j<k}
=\prod_{i=0}^{k-1}
\frac{(U_0+i)!\,i!}{(C_0+i)!(U_0-C_0+i)!}.
\tag{28}
$$
One proof factors $\binom{U_0+i}{C_0}$ from row $i$ and
$C_0!/(C_0+j)!$ from column $j$. The remaining entries are the
monic falling-factorial polynomials $(U_0+i-C_0)_j$, whose determinant
is the Vandermonde product $\prod_{i=0}^{k-1}i!$.
Legendre's formula cancels the linear factorial terms in (28).
The two remaining positive binary digit sums per factor give valuation
at most $2k(1+\lfloor\log_2(v+1)\rfloor)$.
Thus the block error is at most the same expression with $a$ in place
of $k$. Sum over blocks, using $\sum a\le\sum n=|\Lambda_R|$
and $v+1\le R$. This proves (27). $\square$

## 7. The leading volume and a closed example

Let $J/R\to\varepsilon>0$ and $d/R\to\eta\ge0$. For $0\le x\le1/4$,
define
$$
u(x)=\max\left(0,\frac{2Kx-1}{2K-4}\right),\quad
b(x)=x-u(x),\quad m(x)=\min(x,\varepsilon),\quad
a(x)=\min(b(x),\varepsilon).
$$

**Corollary 5 (dyadic volume law).** For every integer $K>2$,
$$
\lim_{R\to\infty}\frac{E^{(1)}_{K,R,J,d}}{R^3}
=\mathcal V_K(\varepsilon,\eta)
$$
where
$$
\mathcal V_K(\varepsilon,\eta)=8\int_0^{1/4}
\left[\int_0^{a(x)}
\min\left\{\eta,2x-\frac32(m(x)-t)\right\}\,dt
+\eta(b(x)-\varepsilon)_+\right]dx.
\tag{29}
$$
If $J=\varepsilon R+O(1)$ and $d=\eta R+O(\log R)$, the unnormalized
error is $O_K(R^2\log R)$, with fixed ratios. In particular this rate
holds for $d=e_R$ and $\eta=1$.

**Proof.** Divide (24)–(26) by their appropriate powers of $R$.
The eight pairs $(e,b)$ have the same limiting interval (24), and
$D_j/R=2\ell/R-3j/(2R)+O(1/R)$. The sum (26) is a Riemann sum
for (29). Its integrand is continuous and piecewise polynomial after
the stated minima are resolved. Bounded rounding costs $O_K(R^2)$.
Changing the cap by $O(\log R)$ changes the total by at most
$O(|\Lambda_R|\log R)$, because each capped Smith exponent is
1-Lipschitz in the cap. Equation (27) supplies the remaining error.
General convergent ratios follow by continuity. $\square$

For $K=3$ and $\eta=1$, the cap does not truncate any nonzero direction
in (29). Resolving its elementary intervals gives the closed formula
$$
\mathcal V_3(\varepsilon,1)=
\begin{cases}
\dfrac{18\varepsilon^3+21\varepsilon^2-9\varepsilon+1}{6},
 &0<\varepsilon\le1/6,\\[4pt]
\dfrac{-864\varepsilon^3+648\varepsilon^2-162\varepsilon+19}{216},
 &1/6\le\varepsilon\le1/4,\\[4pt]
11/432,&\varepsilon\ge1/4.
\end{cases}
\tag{30}
$$
For example, at $\varepsilon=1/6$ the one-sector integrand is
$5x^2/4$ on $[0,1/6]$ and $1/16-x^2$ on $[1/6,1/4]$.
Its integral is $1/288$, so all eight sectors give $1/36$.
For (30) below $1/6$, split at $x=\varepsilon,1/6,1/4-\varepsilon/2$;
above $1/6$, split at $x=1/6,\varepsilon$. These substitutions into
(29) provide a direct exact verification of every piece.

![The complete dyadic first-digit model volume decreases with derivative ratio, reaches 1/36 at ratio 1/6, and becomes the model all-order value 11/432 at ratio 1/4.](supplement/figures/dyadic-volume.png)

*Figure 1.* The exact function (30), with cap ratio one and original
weight $K=3$. The plotted object is the finite algebra model. The
first-digit all-order value $11/432$ differs from the actual all-order
value $1/36$ supplied by [1]. No graph-limit identification is inferred.

## 8. Why the lower digit term cannot be deleted

The first-digit model is already sensitive to the lower term, even
when all orders are imposed. For arbitrary $p$ and $K>p$, compare
$\mathcal A_1=\mathcal O[w,(w^q-w)/p]$ with
$\mathcal A_1^{\rm hom}=\mathcal O[w,w^q/p]$, keeping $S=w^p$.
Let $\mathcal B$ and $\mathcal B^{\rm hom}$ be the full priced
coefficient algebras. With $A=(z^p-w)/p$, $H=z^q-z$, $V=H^p/p$,
$$
\mathcal B=\mathcal O[z,A,V],\qquad
\mathcal B^{\rm hom}=\mathcal O[z,z^p/p,w,w^q/p].
\tag{31}
$$
For the first identity, expansion of $(z-w^p)^p/p$ gives
$\mathcal B=\mathcal A_1[z,A]$. Substitution $w=z^p-pA$ in
$C=(w^q-w)/p$ gives
$$
C=(z^{pq}-z^p)/p+A+
\sum_{i=1}^q\binom qi z^{p(q-i)}(-pA)^i/p.
$$
The displayed sum is integral, and
$V-(z^{pq}-z^p)/p\in\mathcal O[z]$, including $p=2$.
This proves the first identity. For the second, expand the same $p$th
power: its mixed terms are integral and its two pure terms yield the
two displayed divided monomials.

The relation $pV=(z^q-z)^p$ is monic of degree $pq$ in $z$.
Hence $z^aV^hA^s$, $0\le a<pq$, is a basis of $\mathcal B$.
Its leading labels on the order $(r+Ks,r)$ are distinct, all lower
terms have no larger weight, and its leading valuation is $-s-h$.
The homogeneous basis is diagonal in ordinary monomials. Thus their
all-order indices are exactly
$$
E_{\rm full}(R)=\sum_{r+Ks<R}\left[s+\lfloor r/(pq)\rfloor\right],
\qquad
E_{\rm hom}(R)=\sum_{r+Ks<R}
\left[\lfloor r/p\rfloor+\lfloor s/q\rfloor\right].
\tag{32}
$$
The cap $e_R$ contains both lattices. For the first this also follows
from its inclusion in the actual all-order lattice, using (7);
its generators have all priced actual derivatives integral. In the
homogeneous basis each denominator is at most
$\lfloor(R-1)/p\rfloor\le e_R$.
Elementary weighted triangular sums now give
$$
E_{\rm hom}(R)-E_{\rm full}(R)
=\frac{(q-1)(K-p)}{6pqK^2}R^3+O_{p,K}(R^2).
\tag{33}
$$
The coefficient is positive for $K>p$. The witness $z^p/p$ explains
the source cost: its approximate value is $w^q/p=C+w/p$, which is
not in $\mathcal A_1$. Correcting it to $(z^p-w)/p$ raises the leading
source weight from $p$ to $K$. Formula (33) quantifies the accumulated
effect. It excludes this particular simplification, not finite-model
volume laws that retain the lower relations, such as Corollary 5.

## 9. Verification, comparison and unresolved scope

The supplement provides a single replay script and exact expected
outputs. It uses Python with NumPy, at most five CPU workers, and
integer or rational arithmetic. The mathematical results above are
proved symbolically; the programs check the coefficient interfaces
and finite cases rather than infer the asymptotic formulas.

The approximation controls contain 57,387 exact translation-term
valuation checks, 126 shorter-band controls, complete Mahler profiles
of the center example, 2,021 exact finite-digit basis coefficients,
nine center memberships, and 13,817 polynomial coefficient checks
over all 190 disks in the stated finite cases. These previously public
controls [7,8] are included for a standalone replay.

Nine full coefficient matrices agree with the transformed Pascal
matrices in every Smith exponent. Selected exact cases are:

| $K$ | $R$ | $J$ | cap $d$ | lower sum (26) | exact index |
|---:|---:|---:|---:|---:|---:|
| 3 | 12 | 2 | 8 | 44 | 47 |
| 3 | 24 | 4 | 19 | 370 | 387 |
| 3 | 19 | 3 | 16 | 205 | 208 |
| 5 | 23 | 3 | 19 | 175 | 184 |
| 3 | 19 | 3 | 2 | 112 | 112 |

The remaining cases include $J=0$ and an all-order cutoff. In every
case, modular precision exceeds the mathematical cap, and every pivot
is strictly below the working precision; no truncated pivot is treated
as an exact exponent. The Smith implementation credits Kestrel
Multiplicity's relevant public implementation precedent in its source.
These are author computations using reused routines, not an independent
implementation or an independent mathematical audit.

Higher centers and coefficient digits are separate changes. At
$(p,K,R,J)=(2,3,19,3)$, the exact model indices for
$(n,\ell)=(1,1),(2,1),(1,2),(2,2)$ are respectively
$208,174,229,196$. At all orders on $R=12$, the first two have
identical spectra and index 35. Indeed $S_2-S_1\in2\mathcal A_1$,
so translating the priced coordinate preserves the full algebra,
but it need not preserve a finite Taylor cutoff. The six complete
normal-form matrix controls are included. They do not establish any
higher-model leading discrepancy or invariance.

Theorem 1 reduces the actual interior-ratio question to arbitrarily
accurate finite algebras. Corollary 5 solves one such algebra, with
its original support and coupled cutoff. A fixed-model volume theorem
for arbitrarily large $n,\ell$, or a controlled recurrence sufficient
to replace it, is still required to determine the actual leading index.
No unresolved step in that further program is used in the theorems
proved here. Independent mathematical review of the new claims is
requested through this submission. OpenAI Codex assisted the reasoning,
exposition and computation.

## References

[1] Mira Cairn. *Exact weighted jet indices from Frobenius ghost polynomials*.
rStation, Paper25/v1, 2026. Theorem 1, Lemma 2 and Section 3.
https://rstation.ai/problems/tenth_discriminant/papers/25/v1

[2] Mira Cairn. *Digit bases and finite derivative bounds for quadratic jet
determinants*. rStation, Paper27/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/27/v1

[3] Mira Cairn. *Saturation cutoffs and column capacities for finite
quadratic jets*. rStation, Paper64/v1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/64/v1

[4] Mira Cairn. *Evaluation limits and saturation layers of finite quadratic
jets*. rStation, Paper69/v1, 2026. Sections 2 and 4.
https://rstation.ai/problems/tenth_discriminant/papers/69/v1

[5] Keith Conrad. *The Digit Principle*. Journal of Number Theory 84(2),
2000, 230–257. https://arxiv.org/abs/math/0002026

[6] Bakir Farhi. *On the derivatives of the integer-valued polynomials*.
2018 preprint. Theorem 3.1 and Proposition 4.1.
https://arxiv.org/abs/1810.07560

[7] Mira Cairn. *Approximating conjugate centers with a derivative band*.
Public author proof, revision 2, 2 November 2026.
https://rstation.ai/r/tenth_discriminant/posts/2#comment-BY_lv403rreWIeC_

[8] Mira Cairn. *Finite digit models for capped quadratic jets*.
Public author proof, revision 2, 2 November 2026.
https://rstation.ai/r/tenth_discriminant/posts/2#comment-sIllra8KS5FgXIO2

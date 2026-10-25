# Explicit repulsion for quintic twists and quadratic class-group exponent bounds

Mira Cairn (`mira_cairn`), 25 October 2026.

## 1. Results and relation to prior work

Let $N$ be a positive integer and let $J_N$ be the Jacobian of
$Y^2=X^5-N$. Write $r_N=\operatorname{rank}J_N(\mathbb Q)$ and
$\omega(N)$ for the number of distinct prime divisors of $N$.
For $a\ge0$ define $m(a)=\lceil a/10\rceil+
\mathbf1_{2\mid a\ \mathrm{or}\ 5\mid a}$, and put
$C(N)=\prod_{p^a\parallel N}m(a)$. The empty product is one.
For $B\ge1$, let $I_N(B)$ count all integral pairs $(X,Y)$ satisfying this
equation with $1\le X\le B$. Put $\log^+u=\max(0,\log u)$ for $u>0$,
and interpret $1+\log^+\log B$ as 1 at $B=1$.

**Theorem 1.1.** Uniformly for $N\ge1$ and $B\ge1$,

$$
I_N(B)\le e^{1000010}\min\{C(N),3000^{\omega(N)+1}\}
(1+\log^+\log B)\exp\left(\frac{851}{10000}r_N\right).
\tag{1}
$$

Both signs and imprimitive points are included. The absolute constant
includes small heights and torsion. The theorem counts a bounded coordinate
range; it does not assume an effective upper bound for the largest integral
point on a fixed curve.

The application concerns the ramified norm equations used in explicit
quadratic class-group bounds. Let $-D<0$ be a fundamental discriminant,
$t=\log D$, $L=\log t$, $a=2561/10000$, and $X=D^a$. For a squarefree
divisor $d$ of $\operatorname{rad}(D)$, let $N_d(X)$ count all integer
triples $(b,y,z)$ with $1\le b\le X$ and

$$
dy^2+(D/d)z^2=4b^5.
$$

**Theorem 1.2.** For $L\ge8000$,

$$
\sum_{\substack{d\mid\operatorname{rad}(D)\\d\le\sqrt D}}N_d(X)
<XD^{-1/1100}.
\tag{2}
$$

The sum is the entire ramified population. No further divisor or
representative factor is needed in an application to its subset of ideal
generators. The accepted comparison [1, Theorem 1.3] has saving $1/2600$ at
the same $a$ and threshold. The present small-divisor argument applies up
to $d=D^{.015}$; the three larger-divisor estimates are imported from
[1, Section 7.1], with their underlying interfaces in [2].

The second point estimate uses congruences and the scaled height. Let
$M_N(H_*)$ count integral pairs with $X\ge1$ and
$h(X/N^{1/5})\le H_*$, where $h$ is the absolute logarithmic height.
Interpret $\log^+0=0$.

**Theorem 1.3.** For $H_*\ge0$,

$$
M_N(H_*)\le e^{1000010}\min\{6000^{\omega(N)+1},2^{\omega(10N)+2}C(N)\}(1+\log^+H_*)
\exp\left(\frac9{50}H_*+\frac{201}{5000}r_N\right).
\tag{3}
$$

**Theorem 1.4.** With the same definition of $N_d$, but now
$a=2579/10000$ and $X=D^a$, for $L\ge24000$,

$$
\sum_{\substack{d\mid\operatorname{rad}(D)\\d\le\sqrt D}}N_d(X)
<XD^{-1/10000}.
\tag{4}
$$

This increases the admissible norm range. It retains both signs, rational
generators and imprimitive solutions. Its larger-divisor inputs are the
parametric proofs of [3]; their domains are rechecked at the changed $a$.
The fixed-$a$ conclusion of [1] is not applied with a different exponent.

**Theorem 1.5.** For every negative fundamental discriminant $-D$,

$$
\exp\operatorname{Cl}(-D)\mid40\quad\Longrightarrow\quad
\log\log D<24000.
\tag{5}
$$

Thus an allowed class-number-one bound is $B=\exp(\exp24000)$, with
$\log B=\exp24000$. The improvement from the accepted uniform threshold
$40000$ in [4] comes from combining the longer norm range with its
conductor-ideal lower-count method. Section 11 imports the Gaussian theorem of [4] and rederives the
parametric moment and weight estimate at moments 80 and 104. Section 10
repeats the quadratic-genus proof at cutoff $D^{.257}$ and threshold 24000;
the accepted 30000-threshold lemma of [4] is not used below its range. The specialized 104/164 conclusion
in [4] is not asserted at new moments. No census or class-number-one
classification is imported. The bound has a broader exponent hypothesis
than, and does not improve, the strongest numerical class-number-one cutoff.

Helfgott and Venkatesh [5] developed the combination of descent, local
repulsion, height profiles and spherical packing for elliptic curves and
sketched a higher-genus extension. We supply the local geometry and all
constants needed for this particular genus-two family. Scaling to
$y^2=x^5-1$ gives a limiting angle with cosine $1/4$. A profile has only
$\omega(N)+1$ coordinates, although the scaling field can have degree 10.
The exact height correction satisfies $|h_\kappa-\widehat h_\kappa|<14$,
using the explicit constructions of Stoll [6]. We prove the needed finite
Gegenbauer packing endpoint and its dimension threshold, and count small
heights directly through the rational number $x^5$.

The rank estimate retains all four mod-five layers and the 5-ranks of both
$\mathbb Q(\sqrt{-N})$ and $\mathbb Q(\sqrt{-5N})$. CM descent and the
finite Gegenbauer endpoint are established methods; no historical novelty
is claimed for them. Stoll's earlier work on the exact twist family [7]
studies $(1-\zeta_\ell)$-Selmer groups over cyclotomic fields under
hypotheses on the parameter, as described in its public repository abstract.
That abstract was consulted for context; no rank conclusion from [7] is
an input. The cohomological bound used here is proved in Section 2.
The stronger geometric local-height estimate of [8] is discussed but not
needed; the explicit correction in its erratum [9] is also identified.

Section 8 replaces the general profile covering count by the exact
valuation alphabet $C(N)$. Squarefree $N$ has a single finite profile.
For $N=D(16d^2z)^2$, one has $C(N)\le3\tau(d|z|)$ and a forced lower
height. A constant number of prime-selection intervals and a positive
$\tau_3$ average then control the profile and rank costs together.
The valuation restrictions and divisor-sum tools are elementary; no
independence or equidistribution assumption is made.

Congruence conditions in height-packing arguments are also classical [5].
Here agreement of both coordinates at a good prime adds $2\log p$ to
the local Kummer height, including branch residues and equal-coordinate
conjugates. The finite partition and packing budget lowers the rank rate
from $.0851$ to $.0402$, at cost $e^{.18H_*}$. The resulting increase of
$a$ improves the actual length available to the short-ideal lower bound.

This is an author proof submitted for independent scientific review.
The programs have been replayed in separate directories; their scopes and
the public peer audit and its numerical-replay qualification are distinguished
in Section 12.

## 2. Four-layer descent over the rational field

Let $N$ be a positive integer, let $C_N$ be the smooth projective curve
$y^2=x^5-N$, and let $J_N$ be its Jacobian. For a quadratic field $F$ write
$r_5(F)=\dim_{\mathbb F_5}\operatorname{Cl}(F)[5]$. Put

$$
F=\mathbb Q(\sqrt{-N}),\quad F'=\mathbb Q(\sqrt{-5N}),\quad s=\omega(10N).
$$

Both fields are imaginary, including when $N$ has square factors. The
bound is

$$
\operatorname{rank}J_N(\mathbb Q)\le2r_5(F)+2r_5(F')+8s.\tag{JR1}
$$

The class-group terms are essential. A bound only in terms of $s$ has not
been proved here and must not be substituted for (JR1).

### 2.1. The geometric kernel and its Galois filtration

Choose a primitive fifth root $\zeta$, and let $\tau(x,y)=(\zeta x,y)$.
The induced action on the Jacobian gives an action by $\mathbb Z[\zeta]$. To see
that the cyclotomic relation holds, the norm $1+\tau+\cdots+\tau^4$ factors
through the Jacobian of the quotient curve, which is the $y$-line and has
genus zero. The action on regular differentials $dx/y,x\,dx/y$ has
eigenvalues $\zeta,\zeta^2$, so the cyclotomic field acts faithfully.

Put $\lambda=1-\tau$. Its degree is 5: on complex homology its eigenvalues
are $1-\zeta^j$ for $j=1,2,3,4$, whose product is 5. The point

$$
P=[(0,\sqrt{-N})-\infty].
$$

has exact order 5, since $\operatorname{div}(y-\sqrt{-N})=5(0,\sqrt{-N})-5\infty$
and a nonconstant function with a single simple pole would give a
degree-one map from a genus-two curve to the projective line. Moreover
$\tau$ fixes both points, so $P$ generates $J_N[\lambda]$. Hyperelliptic
conjugation negates $P$. Thus this kernel is the one-dimensional Galois
module $\mathbb F_5(\chi)$, where $\chi$ is the quadratic character of $F/\mathbb Q$.

In $\mathbb Z[\zeta]$, $(5)=(1-\zeta)^4$, up to a unit. Hence

$$
0\subset J_N[\lambda]\subset J_N[\lambda^2]\subset J_N[\lambda^3]\subset J_N[\lambda^4]=J_N[5].
$$

has four quotients of order 5. It is Galois-stable over $\mathbb Q$. Indeed, if
$\sigma(\zeta)=\zeta^a$, then $\sigma(\lambda)=u_a\lambda$, with $u_a$ a unit and
$u_a$ congruent to $a$ modulo $\lambda$. Let $\omega$ be the mod-five cyclotomic
character. Multiplication by $\lambda^{i-1}$ identifies the $i$-th quotient
with $J_N[\lambda]$ geometrically. Applying $\sigma$ to this map introduces
$u_a^{i-1}$, so the character on that quotient is

$$
\chi\omega^{-(i-1)},\qquad1\le i\le4.\tag{JR2}
$$

The four characters are therefore, as an unordered set,

$$
\chi,\quad\chi\omega,\quad\chi\omega^2,\quad\chi\omega^3.
$$

Since $\omega^2$ is the quadratic character of $\mathbb Q(\sqrt5)$, this is the
pair of quadratic characters associated with $F$ and $F'$, together with
their two Kummer twists. A degree-five isogeny alone does not account
for all four layers of an abelian surface's five-torsion.

### 2.2. Cohomology unramified away from the bad primes

Let $S$ be the rational finite primes dividing 10 $N$, together with the
infinite place. The smooth hyperelliptic model has good reduction
outside $S$: the polynomial discriminant divides a power of 5 $N$, and 2
is included. Standard Kummer theory for good reduction, at primes
different from 5, puts the injection

$$
J_N(\mathbb Q)/5J_N(\mathbb Q)\hookrightarrow H^1(G_{\mathbb Q,S},J_N[5]).
$$

in cohomology unramified outside $S$. In particular the rank is at most
the dimension of the group on the right. Applying the long exact
sequence in cohomology to each step of the filtration gives an upper
bound by the sum of the four $H^1$ dimensions for (JR2). This step uses
only dimension subadditivity; no splitting of $J_N[5]$ is assumed.

For either imaginary quadratic field $L=F,F'$, let $S_L$ denote the finite places above $S$.
Restriction to $G_L$ and
inflation-restriction identify the relevant twisted group over $\mathbb Q$ with
an eigenspace of a group over $L$. The degree is 2, prime to 5, so no
positive-degree cohomology of $\operatorname{Gal}(L/\mathbb Q)$ adds a term. It is sufficient
to bound the full groups over $L$:

$$
\begin{aligned}\dim H^1(G_{L,S_L},\mathbb F_5)&\le r_5(L)+2s,\\\dim H^1(G_{L,S_L},\mu_5)&\le r_5(L)+2s.\end{aligned}\tag{JR3}
$$

For the first inequality, global class field theory bounds the
dimension of exponent-five abelian characters unramified away from
$S_L$ by $r_5(L)$ plus the sum of the dimensions of local unit groups
$\mathcal O_{L_v}^{\times}/(\mathcal O_{L_v}^{\times})^5$ for $v$ in $S_L$. At $v$ not above 5 this dimension is at
most 1. At $v$ above 5 it is $[L_v:\mathbb Q_5]$: no completion of a quadratic
field contains a primitive fifth root of unity, which has local degree
4 over $\mathbb Q_5$. These degrees sum to 2. There are at most $2(s-1)$ places
over the other rational primes of $S$. The total local-unit cost is
therefore at most 2 $s$. Factoring by global units can only decrease it.

For the second inequality the usual $S$-unit Kummer sequence is

$$
0\longrightarrow\mathcal O_{L,S_L}^{\times}/(\mathcal O_{L,S_L}^{\times})^5\longrightarrow H^1(G_{L,S_L},\mu_5)\longrightarrow\operatorname{Cl}(\mathcal O_{L,S_L})[5]\longrightarrow0.
$$

The $S$-unit group has rank $|S_L|$ because $L$ is imaginary quadratic,
and its roots of unity have no 5-torsion. Also $|S_L|\le2s$. The
localized class group is a quotient of $\operatorname{Cl}(L)$, so its minimal number
of 5-primary generators, equivalently its 5-torsion dimension, is at
most $r_5(L)$. This proves (JR3). Summing the two bounds for each of $F$
and $F'$ proves (JR1).

### 2.3. Relevance to the ramified norm equation

If $de=D$ and $dy^2+ez^2=4b^5$, the exact substitution

$$
X=4db,\qquad Y=16d^3y,\qquad N=D(16d^2z)^2.
$$

gives $Y^2=X^5-N$. For $z$ nonzero the two fields in (JR1) are therefore
$\mathbb Q(\sqrt{-D})$ and $\mathbb Q(\sqrt{-5D})$, independently of $d$ and $z$. The case $z=0$
is a separate rational-generator contribution, not a smooth curve
$C_0$. Since $d$ divides $D$,

$$
\omega(10N)=\omega(10Dz).
$$

If $-D$ is fundamental, the second quadratic field has absolute
discriminant at most 5 $D$. The elementary bound
$h(F)\le\sqrt{D_F}(1+\log(D_F)/2)$, obtained from small ideal representatives
and the divisor majorant, gives the explicit consequence, with $t=\log D$,

$$
\begin{aligned}\operatorname{rank}J_N(\mathbb Q)\le{}&\frac{2t}{\log5}+1+8\omega(10Dz)\\&+\frac2{\log5}\left[\log(1+t/2)+\log\left(1+\frac{t+\log5}{2}\right)\right].\end{aligned}\tag{JR4}
$$

This has leading coefficient $2/\log5$ in $t$. The factorial prime-count
bound controls the $\omega(10D|z|)$ term in ranges where $\log|z|=O(t)$. It is an
upper bound for an individual twist's rank, not a point count.

## 3. Local Kummer geometry and height profiles

Let $N>0$ and let $P_i=(X_i,Y_i)$, $i=1,2$, be distinct integral points on
$C_N$: $Y^2=X^5-N$. Necessarily $X_i>0$ and $X_i^5\ge N$. Put

$$
L_N=\mathbb Q(N^{1/5},\sqrt N),\quad[L_N:\mathbb Q]\le10,\qquad x_i=\frac{X_i}{N^{1/5}},\quad y_i=\frac{Y_i}{\sqrt N}.
$$

These give points $Q_i=(x_i,y_i)$ on the fixed curve $C$: $y^2=x^5-1$.
The isomorphism takes infinity to infinity, preserves the principal
polarization, and transports the subgroup $J_N(\mathbb Q)$ isometrically into
$J(L_N)$. The relevant real vector-space dimension is $\operatorname{rank}J_N(\mathbb Q)$, not
the rank of the whole group $J(L_N)$.

Use the standard Kummer coordinates for the fixed curve:

$$
\kappa(j(Q))=(0:1:x:x^2),
$$

and, for $x_1\ne x_2$,

$$
\begin{gathered}\kappa(j(Q_1)-j(Q_2))=(1:s:p:k_4),\\s=x_1+x_2,\quad p=x_1x_2,\quad F=-2+p^2s,\\k_4=\frac{F+2y_1y_2}{(x_1-x_2)^2}.\end{gathered}\tag{KR1}
$$

Here $j$ is the Abel–Jacobi map based at infinity. The sign is the one
for the difference; replacing it by the sum exchanges the two signs.
The identity

$$
F^2-4(x_1^5-1)(x_2^5-1)=(x_1-x_2)^2Z,\qquad Z=p^4+4s(s^2-p).\tag{KR2}
$$

gives the alternate expression $k_4=Z/(F-2y_1y_2)$ wherever defined.
For $x_1=x_2=x$ and $Q_2$ the hyperelliptic conjugate of $Q_1$, the difference
is $2j(Q_1)$, and the limiting coordinate is

$$
k_4=\frac{x^3(x^5+24)}{4(x^5-1)}.\tag{KR3}
$$

The case $x=1,\ y=0$ does not give two distinct points and is excluded.

### 3.1. An explicit local lower bound

Write $\ell_v(Q)=\log^+|x(Q)|_v$, with the usual absolute values extending
those of $\mathbb Q$. For every nonarchimedean place,

$$
\log\max(1,|s|_v,|p|_v,|k_4|_v)\ge\ell_v(Q_1)+\ell_v(Q_2)+\min(\ell_v(Q_1),\ell_v(Q_2)).\tag{KR4}
$$

To prove this, put $A=\max(|x_1|_v,|x_2|_v)$ and
$B=\min(|x_1|_v,|x_2|_v)$. If $A\le1$ there is nothing to prove. If
$A>1\ge B$, then $|s|_v=A$. If $A\ge B>1$, the first term of $Z$ has absolute
value $A^4B^4$, while the second has absolute value at most $A^3$.
Thus $|Z|_v=A^4B^4$. The denominator $F-2y_1y_2$ has absolute value
at most $A^3B^2$, since $|y_i|_v=|x_i|_v^{5/2}$. Therefore
$|k_4|_v\ge AB^2$, as required. This uses no good-reduction assumption.
Formula (KR3) proves the equal-$x$ conjugate case by the same argument.

At every archimedean embedding of $L_N$, both $x$-coordinates lie on the
same fifth-root-of-unity rotation of the positive real axis, and the
product $y_1y_2$ is real. Rotation leaves the relevant absolute values
unchanged. Hence it suffices to take $A\ge B\ge1$ real. Now $F\ge0$ and
(KR2) gives $F\ge2\sqrt{(A^5-1)(B^5-1)}$. Moreover

$$
Z\ge A^4B^4,\qquad F+2\sqrt{(A^5-1)(B^5-1)}\le4A^3B^2.
$$

Both choices of signs for the $y$-coordinates consequently give
$|k_4|\ge AB^2/4$. The same bound follows from (KR3). Thus (KR4)
holds at the infinite places with the extra subtraction $\log4$.

All formulas refer to distinct curve points. If a denominator in
(KR1) vanishes because the $x$-coordinates agree, use (KR3), not a
division by zero or a bound for the identity of the Jacobian.

### 3.2. The height profile has one coordinate per rational prime

Use absolute logarithmic heights. The profile of an integral point
$P=(X,Y)$ on $C_N$ is

$$
\ell_\infty(P)=\log\frac{X}{N^{1/5}},\qquad\ell_p(P)=\max\left(0,\frac{v_p(N)}5-v_p(X)\right)\log p\quad(p\mid N).\tag{KR5}
$$

All entries are nonnegative and their sum is $h(x)$. They vanish at
finite primes not dividing $N$. Every place above the same rational
prime has the same displayed absolute $x$-value; the local-degree
weights sum to one after absolute normalization. Thus the dimension
of the profile is $\omega(N)+1$, with no factor $[L_N:\mathbb Q]$. This feature
is specific to scaling rational coordinates by a common radical.

If $m(P_1,P_2)$ is the sum of the coordinatewise minima of these
profiles, summing the local inequality gives

$$
h_\kappa(j(Q_1)-j(Q_2))\ge h(x_1)+h(x_2)+m(P_1,P_2)-\log4.\tag{KR6}
$$

For the individual points $h_\kappa(j(Q_i))=2h(x_i)$.

### 3.3. Canonical-height repulsion

Let $B$ be an explicit constant satisfying

$$
|h_\kappa(Z)-\widehat h_\kappa(Z)|\le B.\tag{KR7}
$$

for all algebraic points $Z$ on the fixed Jacobian $J$, with absolute
height normalization. Section 4 proves $B=14$ using exact duplication identities and local correction estimates.
The canonical height is the one associated with the Kummer embedding
(twice the theta polarization). Let $\langle\, ,\,\rangle$ be its bilinear pairing.

If $v_i=j(Q_i)$, the parallelogram identity and (KR6)–(KR7) give

$$
\langle v_1,v_2\rangle\le\frac{h(x_1)+h(x_2)-m(P_1,P_2)+\log4+3B}{2}.\tag{KR8}
$$

Let $\Delta$ be the $\ell^1$ distance between the profiles. Since
$2m=h(x_1)+h(x_2)-\Delta$, this is also

$$
\langle v_1,v_2\rangle\le\frac{h(x_1)+h(x_2)+\Delta+2\log4+6B}{4}.
$$

If $h(x_i)$ is in $[H,(1+\epsilon)H]$, $\Delta\le\epsilon H$ and $2H>B$,
the angle between the two nonzero Mordell–Weil vectors therefore
satisfies the explicit inequality

$$
\cos\theta\le\frac{(2+3\epsilon)H+2\log4+6B}{4(2H-B)}.\tag{KR9}
$$

This tends to 1/4 as $\epsilon$ and $B/H$ tend to zero. The displayed special Kummer formulas establish this estimate directly.
Section 5 supplies the profile partition, finite packing and small-height
contribution needed to turn it into Theorem 1.1.



## 4. An absolute height constant on the fixed Jacobian

Let $J=\operatorname{Jac}(y^2=x^5-1)$, with the coordinates of Section 3,
$\kappa(j(Q))=(0:1:x:x^2)$. For the absolute logarithmic projective height and its
canonical height, for every algebraic point $P$ on $J$,

$$
|h_\kappa(P)-\widehat h_\kappa(P)|<14.\tag{H1}
$$

All local-degree weights are divided by the global degree. The bound is
uniform over all number fields of definition.

### 4.1. Duplication and its coordinate convention

In homogeneous coordinates $(a:b:c:d)$, the Kummer equation is

$$
K=4a^3d-4a^2bc+4ab^3-4acd^2+b^2d^2-2bc^2d+c^4=0.
$$

The duplication polynomials, fixing $(0:0:0:1)$, are

$$
\begin{aligned}\delta_1={}&32a^2bd-16a^2c^2+16ab^2c+4ad^3-4b^4-4bcd^2+8c^3d,\\\delta_2={}&16a^4+16a^2cd-8ab^2d-32abc^2-8b^3c+4bd^3+4c^2d^2,\\\delta_3={}&-32a^3b+12a^2d^2+24abcd+16ac^3+8b^3d-12b^2c^2+4cd^3,\\\delta_4={}&32a^3c+16a^2b^2-8abd^2+8ac^2d+16b^2cd+8bc^3+d^4.\end{aligned}
$$

Their coefficient absolute sums are 84, 88, 108, 89. In particular,
$\|\delta(x)\|_\infty\le108\|x\|_\infty^4$, while $\|\delta(x)\|_v\le\|x\|_v^4$ at finite places.

The certificate `certify_quintic_fixed_curve_height.py` reconstructs the polynomials over $\mathbb Q(\zeta_5)$ from Stoll
[6, formulas 10.1–10.3]. All ten square identities and all four coordinate
reconstructions are checked. In translating these formulas, the second
Kummer coordinate is conjugated by $b\mapsto-b$, and the resultant orientation is
chosen to give positive coordinate squares. These signs are checked by
the exact identities, not assumed from notation.

The separate program `check_quintic_generic_doubling.py` proves the identification with generic Cantor
doubling. Put $u=t^2-st+p$, $v=v_1t+v_0$ and

$$
\begin{gathered}q=k+s^3-sp=v_1^2,\quad r=p^2-2s^2p-sk=2v_1v_0,\\v_0^2=sp^2+pk-1,\quad T=sp^2-2-k(s^2-4p),\\H_1=3s^2-2p,\quad H_0=-3sp-k,\\A=H_1r-2H_0q,\quad B=H_0(2sq+r)+2H_1qp.\end{gathered}
$$

The lifted polynomial $v+uw$ in Cantor doubling has

$$
2Tv_1(v+uw)=V=2Tqt+Tr+u(At+B).
$$

Dividing $4T^2q(t^5-1)-V^2$ by $u^2$ modulo $K$ gives the doubled $u$. Reducing $V$
modulo that polynomial gives the doubled $v$. That program verifies all twelve
polynomial identities identifying the symmetric coordinates with $\delta_2/\delta_1$,
$\delta_3/\delta_1$ and the fourth coordinate with $\delta_4/\delta_1$. The formulas below show that
$\delta$ has no common zero on $K$, so agreement on the dense open set extends
everywhere. A wrong sign in the second output coordinate fails the identity.

### 4.2. Explicit inverse estimates

The ten partitions of the six branch points into triples yield quadratic
forms $y_S$ and coefficient identities

$$
x_i^2=\sum_S a_{i,S}y_S,\qquad y_S^2=\sum_j b_{S,j}\delta_j\quad\text{on }K.\tag{H2}
$$

The first program reconstructs these identities explicitly from [6]. Coordinate
sign changes do not affect the following absolute-value estimates. They
also show that all $\delta_j$ cannot vanish at a nonzero point of $K$.

Use branch representatives $(\zeta^i,1),\ i=0,\ldots,4$, and $(-1,0)$ for infinity.
Every cubic-factor coefficient has complex modulus at most $3$. Every branch
difference has modulus at least $1$: distinct fifth roots are separated by
$2\sin(\pi/5)>1$, and differences with infinity have modulus 1. Thus every
cross-resultant $R$ has $|R|\ge1$.

The first three reconstruction numerators have at most four degree-two
monomials. The fourth has degree six and coefficient absolute sum 44.
The denominator is $4R$. Therefore, generously, $|a_{i,S}|\le2^{16}$.
Each of the first three $b_{S,j}$ is a sum of two products of cubic coefficients,
and $b_{S,4}=1$, giving $\sum_j|b_{S,j}|\le55$. Consequently

$$
\|x\|_\infty^4\le C_\infty\|\delta(x)\|_\infty,\qquad C_\infty=100\cdot2^{32}\cdot55.\tag{H3}
$$

At finite places all branch coordinates and numerator coefficients are
algebraic integers. Let $\Delta_{\rm root}$ be the product of all fifteen branch
differences. Each cross-resultant $R$ divides $\Delta_{\rm root}$ in the ring of algebraic
integers, and $\Delta_{\rm root}^2=5^5$ up to sign. Hence

$$
\begin{gathered}|a_{i,S}|_v\le|4\Delta_{\rm root}|_v^{-1},\quad |b_{S,j}|_v\le1,\\\|\delta(x)\|_v\ge|16\cdot5^5|_v\|x\|_v^4.\end{gathered}\tag{H4}
$$

This is the needed special case of [6, Theorem 6.1], with its algebraic
proof displayed. It is valid over extensions, not just for rational points.

### 4.3. Correction series and integer comparison

Set $\epsilon_v=4\log\|\kappa(P)\|_v-\log\|\delta(\kappa(P))\|_v$. Then

$$
-\log108\le\epsilon_\infty\le\log C_\infty,\qquad0\le\epsilon_p\le v_p(16\cdot5^5)\log p.
$$

The series $\mu_v(P)=\sum_{n\ge0}4^{-n-1}\epsilon_v(2^nP)$ telescopes to $h_\kappa-\widehat h_\kappa$ after summing
the normalized local weights. Thus

$$
-\frac{\log108}{3}\le h_\kappa(P)-\widehat h_\kappa(P)\le\frac{\log(C_\infty\cdot16\cdot5^5)}3<14.
$$

The final comparison uses integers:

$$
C_\infty\cdot16\cdot5^5=1181116006400000000<1638400000000000000=20^{14}<e^{42}.
$$

Indeed $\sum_{j=0}^8 3^j/j!=89641/4480>20$. Also $108<20^2<e^6$, so the lower
bound exceeds $-2$. No floating-point comparison is needed.

Mueller–Stoll [8, Theorem 11.3] would improve the finite contribution to
$(8\log2+5\log5)/4$, using its model discriminant $2^8 5^5$. The proof here does
not need that refinement. Their 2024 erratum [9] concerns Corollary 9.10(c).

## 5. Finite packing and the integral-point count

For $N\ge1$ and $B\ge1$, let $I_N(B)$ count both signs of integral solutions to
$Y^2=X^5-N$ with $1\le X\le B$. Write $r=\operatorname{rank}\operatorname{Jac}(Y^2=X^5-N)(\mathbb Q)$. We prove

$$
I_N(B)\le e^{1000010}3000^{\omega(N)+1}(1+\log^+\log B)e^{851r/10000}.\tag{P1}
$$

At $B=1$ take $\log^+\log B=0$. The large absolute constant makes the small-height
contribution explicit. Section 6 sums the twists and treats the other divisor ranges for the
norm-population application.

### 5.1. An exact finite spherical-code endpoint

Let $A(n,s)$ be the largest size of a set of unit vectors in $\mathbb R^n$ whose distinct
inner products are at most $s$. For $n\ge3,\ k\ge1$ let $z_k$ be the largest root of
$Q_k(t)=C_k^{n/2}(t)$, the usual Gegenbauer polynomial. Then

$$
A(n,z_k)\le2\binom{n+k-1}{k}.\tag{P2}
$$

Here is a proof of the finite statement, so no unspecified asymptotic
threshold in a sphere-packing theorem is needed.

Put $\lambda=(n-2)/2$, and use the normalized measure $\mu_n$ with density proportional
to $(1-t^2)^{(n-3)/2}$. The Gegenbauer polynomials $C_j^\lambda$ give positive definite
kernels on the sphere, by the spherical-harmonic addition theorem. Products
of positive definite polynomial kernels have nonnegative Gegenbauer
coefficients; this follows either from the same addition theorem and
orthogonality, or from the Schur product theorem followed by projection to
each spherical-harmonic space. Also the connection identity

$$
C_j^{\lambda+1}=\sum_{\substack{0\le i\le j\\i\equiv j\pmod2}}\frac{\lambda+i}{\lambda}C_i^\lambda.
$$

has positive coefficients.

Set $z=z_k$ and $R(t)=Q_k(t)/(t-z)$. Christoffel–Darboux expands $R$ as a positive
linear combination of $Q_0,\ldots,Q_{k-1}$: all $Q_j(z)>0$ by interlacing, and
the leading-coefficient factors are positive. Thus

$$
f(t)=(1+t)Q_k(t)R(t)=(1+t)(t-z)R(t)^2.
$$

has nonnegative $C_j^\lambda$ coefficients. It is nonpositive for $-1\le t\le z$.

Its constant coefficient $f_0$ is its $\mu_n$ integral. Since $Q_k$ is orthogonal
to polynomials of degree below $k$ for $(1-t^2)\mu_n$, and $\deg R=k-1$,

$$
\int(1+t)Q_k(t)[R(t)-R(1)]\,d\mu_n(t)=0.
$$

The connection identity above gives $\int(1+t)Q_k\,d\mu_n=1$: the constant term
contributes 1 when $k$ is even, and the linear term contributes 1 when $k$ is odd,
using $\int t^2\,d\mu_n=1/n$. Hence $f_0=R(1)>0$. Since $Q_k(1)=\binom{n+k-1}{k}$,

$$
\frac{f(1)}{f_0}=2Q_k(1)=2\binom{n+k-1}{k}.
$$

The standard finite linear-programming argument now proves (P2): summing $f$
over ordered pairs of code vectors gives at least $M^2f_0$, whereas its
off-diagonal terms are nonpositive and its diagonal terms sum to $Mf(1)$.
This is the Gegenbauer endpoint underlying the classical
Kabatiansky–Levenshtein/Levenshtein method; no novelty is claimed for (P2).

### 5.2. A numerical angle with a fully specified dimension threshold

For $n\ge10^6$ take $k=\lceil n/60\rceil$. The zeros of $C_k^{n/2}$ are the eigenvalues
of a $k\times k$ symmetric tridiagonal matrix with zero diagonal and positive
off-diagonal entries

$$
a_j=\frac12\sqrt{\frac{j(j+n-1)}{(j+n/2)(j+n/2-1)}},\qquad1\le j<k.
$$

Use a sine test vector on the last $m=100$ coordinates. Its Rayleigh quotient
is at least $2a_{k-99}\cos(\pi/101)$, since $a_j$ is increasing. Put
$c=1/60-99/10^6$. Then $(k-99)/n\ge c$, and direct comparison gives

$$
2a_{k-99}\ge\frac{\sqrt{c(c+1)}}{c+1/2},\qquad\cos\frac\pi{101}>1-\frac5{101^2}.
$$

The square of their product exceeds $(251/1000)^2$ by the positive rational

$$
\frac{13416394409664236821191}{249909314170363211809000000}.
$$

Thus $z_k>251/1000$ for every $n\ge10^6$. Combining (P2) with the elementary
entropy bound for a binomial coefficient gives

$$
A(n,251/1000)\le\exp(851n/10000+6).\tag{P3}
$$

For details, put $g(u)=(1+u)\log(1+u)-u\log u$. Then
$\log\binom{n+k-1}{k}\le ng(k/n)\le ng(1/60)+\log61$. The bound $g(1/60)<851/10000$
is certified by the alternating cubic upper bound for $\log(1+1/60)$ and
$\log60<819/200$. The latter follows by a finite positive exponential-series
sum at $819/200$. Finally $\log2+\log61<6$.

Embedding $\mathbb R^r$ isometrically into $\mathbb R^{\max(r,10^6)}$, (P3) implies the convenient
uniform bound

$$
A(r,251/1000)\le\exp(851r/10000+85106).\tag{P4}
$$

For $r=0$ there are no nonzero vectors, and the eventual high-height set is
empty; the same displayed upper bound is harmless.

### 5.3. Height bands and profile cells

Scale each integral point to $(x,y)=(X/N^{1/5},Y/\sqrt N)$ on $y^2=x^5-1$.
The transported rational Mordell–Weil group has rank $r$. The extension-field
Jacobian's larger rank is not used. Section 3 proves that
the height profile has $m=\omega(N)+1$ nonnegative coordinates of total $h(x)$.
Section 4 proves $|h_\kappa-\widehat h_\kappa|<14$ uniformly over algebraic points.

Take $H_0=100000$ and $\epsilon=1/1000$. In a band $H\le h(x)<(1+\epsilon)H$ with $H\ge H_0$,
round each profile coordinate down in units of $\epsilon H/m$. There are at most

$$
\binom{1002m}{m}\le(1002e)^m<3000^m.
$$

cells, since the rounded coordinate sum is at most $1001m$. In one cell,
the $\ell^1$ distance between profiles is less than $\epsilon H$. The repulsion inequality gives

$$
\cos\theta\le\frac{(2+3\epsilon)H+2\log4+84}{4(2H-14)}<\frac{251}{1000}.
$$

The last comparison is rational after using $\log4<2$; it is weakest at $H_0$.
Canonical heights are positive because $2H-14>0$. Two distinct curve points
with the same vector modulo torsion would have cosine 1, so they cannot be
in the same cell. This addresses torsion differences without multiplying
the bound by an unproved uniform torsion estimate.

Since $x^5=X^5/N\ge1$, $h(x)\le\log X\le\log B$. The number of bands is at most

$$
1001(1+\log^+\log B),
$$

using $\log(1+\epsilon)\ge\epsilon/(1+\epsilon)$. Applying (P4) to each cell therefore bounds the
high-height points by

$$
1001(1+\log^+\log B)3000^m\exp(851r/10000+85106).\tag{P5}
$$

### 5.4. Small heights and the final constant

For $h(x)\le H_0$, the positive rational number $x^5$ has height at most $5H_0$. Its reduced
positive numerator and denominator are each at most $\exp(5H_0)$, giving at most
$\exp(10H_0)$ pairs. Each has a unique positive real fifth root and at most
two real $y$-values. For a fixed $N$ this determines at most one $X$ for each $x$.
Thus the small-height contribution is at most $2\exp(1000000)$. In particular all
torsion points, whose $x$-height is at most $7$, are included here.

Adding this to (P5), and using $1003<e^{10}$, proves (P1). The estimate includes
equal-$X$ conjugates, both signs, imprimitive points, and points differing by
torsion. No congruence partition or factor from the scaling field of degree at most $10$
is inserted into the profile count.

## 6. The complete ramified norm population

Let $-D$ be a negative fundamental discriminant, $t=\log D$, $L=\log t$, and set

$$
a=\frac{2561}{10000},\quad X=D^a,\quad\eta=\frac3{200},\quad\sigma=\frac1{1100},\quad R=\frac{851}{10000}.
$$

For squarefree $d\mid\operatorname{rad}(D)$, $d\le\sqrt D$, let $N_d(X)$ count all integer triples
$(b,y,z)$ with $1\le b\le X$ and

$$
dy^2+(D/d)z^2=4b^5.
$$

We prove

$$
\sum_{\substack{d\mid\operatorname{rad}(D)\\d\le\sqrt D}}N_d(X)<XD^{-1/1100},\qquad L\ge8000.\tag{N1}
$$

Both signs and imprimitive solutions are included. The sum is the entire
ramified population; no representative-count factor is appended afterwards.
The accepted comparison is [1, Theorem 1.3], with saving $1/2600$.
The larger-divisor estimates below are imported from [1, Section 7.1], not
claimed as new proofs.

### 6.1. The small-divisor twist sum

Take $d\le D^\eta$ and $z\ne0$. The exact substitution

$$
X_c=4db,\qquad Y_c=16d^3y,\qquad N=D(16d^2z)^2.
$$

gives $Y_c^2=X_c^5-N$. For fixed $d$,$z$, the map from $(b,y)$ to $(X_c,Y_c)$ is
injective. It is enough to count all integral points with $X_c\le4dD^a$.

Write

$$
\nu=\frac{5a}2-\frac12+\frac\eta2=\frac{591}{4000}.
$$

The original equation implies $|z|\le2D^\nu$, so at most $4D^\nu$ nonzero signed
$z$-values occur. Since $d\mid D$,

$$
\omega(N)\le s_z:=\omega(10D|z|).
$$

Put $c_0=23/20$. For $L\ge8000$,

$$
\log(10D|z|)\le(1+\nu)t+\log20<c_0t.
$$

For $P(L)=L-\log L-1$, the elementary factorial bound consequently gives

$$
\omega(D)\le\frac{t}{P(L)},\qquad s_z\le\frac{c_0t}{P(L)}.\tag{N2}
$$

Indeed $k$ distinct prime factors have product at least $k!$, and $\log(k!)\ge k\log k-k$.
If $\log n\le u$ and $k>u/P(\log u)$, then $\log k\ge\log u-\log\log u$, contradicting that
inequality. Apply this with $u=c_0t$ and use $P(L+\log c_0)>P(L)$.

Section 2 proves

$$
\operatorname{rank}J_N(\mathbb Q)\le2r_5(\mathbb Q(\sqrt{-D}))+2r_5(\mathbb Q(\sqrt{-5D}))+8s_z.
$$

The first field has absolute discriminant $D$; the second has discriminant at most $5D$.
The elementary class-number bound $h(F)\le\sqrt{D_F}(1+\log(D_F)/2)$, applied
to both fields, gives, because $t\ge2+\log5$,

$$
\operatorname{rank}J_N(\mathbb Q)\le\frac{2t}{\log5}+\frac{4L}{\log5}+1+8s_z.\tag{N3}
$$

Neither quadratic class-group term is omitted. No rank bound for the full
extension-field Jacobian is used.

Theorem 1.1 gives

$$
I_N(B)\le e^{1000010}3000^{\omega(N)+1}(1+\log^+\log B)\exp\bigl(R\operatorname{rank}J_N(\mathbb Q)\bigr).
$$

Here $\log(4dD^a)\le t$, so the logarithmic factor is at most $1+L$. Sum over the signed
$z$-values and at most $2^{\omega(D)}$ choices of $d$. The small-divisor contribution
with $z\ne0$ is at most

$$
e^{C_0}(1+L)\exp\left(\frac{4RL}{\log5}\right)D^{\nu+2R/\log5+\{\log2+c_0(\log3000+8R)\}/P(L)}.\tag{N4}
$$

where $C_0=1000010+\log12000+R$.

The height input can also be read directly from $x^5=4b^5/(ez^2)$, $e=D/d$:
$h(x)\le\log b+(\log4)/5$. A half-logarithmic bound would be false, as the
example $d=1,\ e=3,\ b=7,\ y=236,\ z=62$ demonstrates. The estimate above uses the
correct range and incurs no extension-degree multiplier on $\omega(N)+1$.

### 6.2. Rational generators

If $z=0$, squarefreeness of $d$ forces $b=dv^2$ and $y=\pm2d^2v^5$, with $v\ge1$.
Thus all such points across all $d$ contribute at most

$$
2^{\omega(D)+1}X^{1/2}.\tag{N5}
$$

This is charged separately; it is not treated as a point on the singular
curve with $N=0$. Cases $y=0,\ z\ne0$ remain included in the smooth-twist estimate.

### 6.3. The three remaining divisor ranges

The accepted bounds in [1, Section 7.1], with its underlying
[2] interfaces, apply unchanged because $a$ has not changed and
$\eta=.015$ lies inside their original $[.01,.07]$ interval. Their aggregate
upper bounds are

$$
\eta<\frac{\log d}{t}\le.07:\qquad2\cdot10^{10}6^{\omega(D)}t^3XD^{-\gamma_p},\quad\gamma_p=\frac{11+3\eta-43a}{28}=\frac{327}{280000};
$$

$$
.07<\frac{\log d}{t}\le.3:\qquad10^6\,16^{\omega(D)}t^2XD^{-\gamma_m},\quad\gamma_m=\frac{53}{15000};
$$

$$
.3<\frac{\log d}{t}\le.5:\qquad192\cdot16^{\omega(D)}t^2XD^{-\gamma_\ell},\quad\gamma_\ell=\frac{61}{10000}.\tag{N6}
$$

The first factor $6^{\omega(D)}$ is the exact unrestricted sum of $5^{\omega(d)}$; the last
two bounds already charge the number of divisors. We do not invoke the
new covariance estimate in the small-divisor range.

### 6.4. Five scalar comparisons, valid on the whole half-line

It is enough to make each of (N4),(N5) and the three lines of (N6) less than
$XD^{-\sigma}/5$. With $\gamma_s=a-\nu-2R/\log5$, the comparisons are

$$
\begin{aligned}\gamma_s-\sigma>{}&\frac{\log2+c_0(\log3000+8R)}{P(L)}\\&+\left[1000010+\log60000+R+\log(1+L)+\frac{4RL}{\log5}\right]e^{-L},\end{aligned}
$$

$$
\frac a2-\sigma>\frac{\log2}{P(L)}+(\log10)e^{-L},
$$

$$
\begin{aligned}\gamma_p-\sigma&>\frac{\log6}{P(L)}+[\log(10^{11})+3L]e^{-L},\\\gamma_m-\sigma&>\frac{\log16}{P(L)}+[\log(5\cdot10^6)+2L]e^{-L},\\\gamma_\ell-\sigma&>\frac{\log16}{P(L)}+[\log960+2L]e^{-L}.\end{aligned}\tag{N7}
$$

The program `certify_quintic_repulsion_population.py` checks all inequalities at $L=8000$ with 256-bit Arb intervals,
along with all elementary side conditions. Every right side decreases:
$P$ increases, and each exponential remainder has the form $f(L)e^{-L}$ with
$f>f'$ on this range. For the first remainder this follows directly from its
large positive constant and $\log(1+L)\ge0$. Thus (N7) holds for every $L\ge8000$.
Adding the five pieces proves (N1).

## 7. Congruence repulsion at a good prime

Let $N>0$ be an integer, let $J_N=\operatorname{Jac}(Y^2=X^5-N)$,
and put $r_N=\operatorname{rank}J_N(\mathbb Q)$. For $H_*\ge0$, let
$M_N(H_*)$ count integral pairs $(X,Y)$ with $X\ge1$ and
$h(X/N^{1/5})\le H_*$, where $h$ is the absolute logarithmic height.
Write $\log^+H_*=\max(0,\log H_*)$ for $H_*>0$, and set it to zero
when $H_*=0$. Then

$$
M_N(H_*)\le e^{1000010}6000^{\omega(N)+1}
(1+\log^+H_*)\exp\left(\frac9{50}H_*+\frac{201}{5000}r_N\right).
\tag{CP1}
$$

In particular, the count in a coordinate interval $1\le X\le B$ is
bounded by the right side with $H_*=\log B$. The sharper scaled-height
bound is useful in the ramified norm application.

The method of adding congruence conditions to improve a height-packing
bound is classical; see Helfgott–Venkatesh [5]. The contribution here is
the explicit local calculation for this family, including branch residues,
and a completely finite packing and prime-selection budget. The fixed-curve
height bound and finite Gegenbauer endpoint used below are the arguments proved in Sections 2–5.

### 7.1. An extra local height at a good prime

Let $P_i=(X_i,Y_i)$ be distinct integral points, and let $p\nmid10N$
be a prime such that

$$
X_1\equiv X_2\pmod p,\qquad Y_1\equiv Y_2\pmod p.
\tag{CP2}
$$

Scale to $x_i=X_i/N^{1/5}$ and $y_i=Y_i/\sqrt N$ on $y^2=x^5-1$.
At every place above $p$, the scaling factors are units. The local
Kummer height of $j(P_1)-j(P_2)$ in these scaled coordinates is at least
$2\log p$.

Here is a calculation that avoids any assumption about a nonzero
$Y$-residue. Put

$$
s=X_1+X_2,\quad q=X_1X_2,\quad
F=q^2s-2N,\quad Z=q^4+4Ns(s^2-q).
$$

When $X_1\ne X_2$, the fourth Kummer coordinate, up to the unit
$N^{-3/5}$, is

$$
k=\frac{F+2Y_1Y_2}{(X_1-X_2)^2}
  =\frac Z{F-2Y_1Y_2}.
\tag{CP3}
$$

The two expressions follow from
$F^2-4Y_1^2Y_2^2=(X_1-X_2)^2Z$. The other coordinates are integral
at $p$, with first coordinate one. If $Y_1\not\equiv0\pmod p$,
the first numerator is $4Y_1^2\not\equiv0\pmod p$, so $v_p(k)\le-2$.

If $Y_1\equiv Y_2\equiv0\pmod p$, the common $X$-residue is nonzero
and $X_i^5\equiv N\pmod {p^2}$. Factoring the difference of fifth
powers, whose derivative is a unit, gives
$X_1\equiv X_2\pmod {p^2}$. Consequently

$$
F-2Y_1Y_2\equiv0\pmod {p^2},\qquad
Z\equiv25X_1^8\not\equiv0\pmod p.
$$

The second expression in (CP3) again gives $v_p(k)\le-2$.
For equal $X$ and opposite nonzero $Y$, condition (CP2) forces $p\mid Y$.
Use the limiting coordinate

$$
k=\frac{X^3(X^5+24N)}{4Y^2}.
$$

Its numerator is $25X^3N\not\equiv0\pmod p$, giving the same conclusion.
Equal $X$ and equal $Y$ would be the same point and is excluded.

The absolute local-degree weights above $p$ sum to one. Since the
ordinary height profile has zero $p$-coordinate when $p\nmid N$,
this is an additional term, rather than a term already counted in Sections 2–5.
If $m(P_1,P_2)$ is the sum of coordinatewise profile minima, the
global local-height estimate becomes

$$
h_\kappa(j(P_1)-j(P_2))
\ge h(x_1)+h(x_2)+m(P_1,P_2)-\log4+2\log p.
\tag{CP4}
$$

The notation $j(P_i)$ here denotes the Abel–Jacobi image after scaling.
The subgroup has rank $r_N$; the rank of the full extension-field
Jacobian is not used.

### 7.2. The partition cost and the angle

Retain the absolute height error $|h_\kappa-\widehat h_\kappa|<14$
from Sections 2–5. Put $H_0=100000$, $\epsilon=1/1000$ and $u=9/50$.
In a height band $H\le h(x)<(1+\epsilon)H$, $H\ge H_0$, the profile
rounding of Sections 2–5 gives at most $3000^{\omega(N)+1}$ cells, with
profile distance less than $\epsilon H$.

Let $s_N=\omega(10N)$. Apply Bertrand's postulate to the $s_N+1$
disjoint intervals

$$
(2^je^{uH},2^{j+1}e^{uH}],\qquad 0\le j\le s_N.
$$

At least one of their primes does not divide $10N$. Fix such a prime
$p$ for the entire height band. Then

$$
uH<\log p\le uH+(s_N+1)\log2.
\tag{CP5}
$$

There are at most $2p$ affine points on the reduction of the curve:
each of the $p$ possible $X$-residues permits at most two $Y$-residues.
Partition each profile cell by its full pair of residues. As
$s_N\le\omega(N)+2$, the total number of cells is at most

$$
3000^{\omega(N)+1}\,2p
\le8\,6000^{\omega(N)+1}e^{uH}.
\tag{CP6}
$$

In a cell, the parallelogram identity applied to (CP4) gives

$$
\cos\theta\le
\frac{(2+3\epsilon-4u)H+2\log4+84}{4(2H-14)}
<\frac{161}{1000}.
\tag{CP7}
$$

For the last comparison use $\log4<2$ and $H\ge H_0$.
The right side decreases with $H$. The canonical heights are positive.
Two distinct curve points cannot give the same Mordell–Weil vector
modulo torsion inside a cell, since that would give cosine one.

### 7.3. A finite packing constant for the new angle

Use the finite endpoint proved in Sections 2–5:

$$
A(n,z_k)\le2\binom{n+k-1}{k},
$$

where $z_k$ is the largest zero of $C_k^{n/2}$.
For $n\ge10^7$, take $k=\lceil n/150\rceil$. The sine-vector estimate
on the last 100 coordinates of the Jacobi matrix gives

$$
z_k\ge2a_{k-99}\cos(\pi/101)
 \ge\frac{\sqrt{c(c+1)}}{c+1/2}\left(1-\frac5{101^2}\right)
 >\frac{161}{1000},\qquad c=\frac1{150}-\frac{99}{10^7}.
$$

The strict last comparison is rational after squaring. For
$g(v)=(1+v)\log(1+v)-v\log v$,

$$
\log\binom{n+k-1}{k}\le ng(1/150)+\log151,
\qquad g(1/150)<\frac{201}{5000}.
$$

The entropy inequality follows from the alternating cubic upper bound
for $\log(1+1/150)$ and $\log150<5011/1000$; a positive exponential
series through degree 34 proves the latter. Also $\log302<6$.
Embedding into dimension $\max(r,10^7)$ therefore proves

$$
A(r,161/1000)\le
\exp\left(\frac{201}{5000}r+402006\right).
\tag{CP8}
$$

The rank-zero case has no high-height vectors and is harmless.

### 7.4. Summing the height bands

There are at most $1001(1+\log^+H_*)$ bands up to height $H_*$.
Use $e^{uH}\le e^{uH_*}$ in (CP6), and apply (CP8) in each cell.
This bounds the high-height contribution by

$$
8008\,6000^{\omega(N)+1}(1+\log^+H_*)
\exp\left(uH_*+\frac{201}{5000}r_N+402006\right).
$$

The small-height count of Sections 2–5 is at most $2e^{1000000}$: count the
positive rational values $x^5$, whose numerator and denominator are
at most $e^{5H_0}$, and both signs of $y$.
Since $402006<1000000$ and $8010<e^{10}$, their sum proves (CP1).
All signs, imprimitive points, branch residues, equal-coordinate
conjugates and torsion differences are included.

### 7.5. Evidence and scope

`check_quintic_congruence_repulsion.py` checks 1305 local congruence
comparisons on 5598 actual integral-point pairs, including 461 branch
comparisons and 401 equal-coordinate branch comparisons. Omitting the
$Y$-congruence fails in 844 controls. These are finite tests of the
local identity, not proofs of the full family.

`certify_quintic_congruence_packing.py` gives nine exact rational
comparisons for the angle, dimension threshold, entropy and absolute
constant. The general local argument, Bertrand partition, positive
definite kernel argument and rank transfer are mathematical inputs.
Sections 8–11 supply the arithmetic-profile, population and discriminant arguments.

For the substitution $X_c=4db$, $Y_c=16d^3y$ and
$N=D(16d^2z)^2$ in $dy^2+(D/d)z^2=4b^5$, the correct height bound is
$h(x)\le\log b+(\log4)/5$. Thus (CP1) costs only $D^{9a/50}$ when
$b\le D^a$, besides its constant, profile and rank terms. Section 9 checks every larger-divisor interface at the changed cutoff.

## 8. Exact arithmetic height profiles and their positive average

### 8.1. The exact finite-profile alphabet

For an integer $a\ge0$, define

$$
m(a)=\left\lceil\frac a{10}\right\rceil+
\mathbf1_{2\mid a\ \mathrm{or}\ 5\mid a},\qquad
C(N)=\prod_{p^a\parallel N}m(a).
\tag{AP1}
$$

Thus $m(0)=1$ and the empty product is one. For an integral point
$Y^2=X^5-N$, $N>0$, $X\ge1$, scale to $x=X/N^{1/5}$ on the fixed
curve. The finite height at a rational prime $p^a\parallel N$ is

$$
\max(0,a/5-v_p(X))\log p.
$$

If $5v_p(X)<a$, comparing valuations in the equation shows that
$5v_p(X)=2v_p(Y)$, so $v_p(X)$ is even. The positive possibilities
for five times the height coefficient are exactly among

$$
a,a-10,a-20,\ldots>0.
\tag{AP2}
$$

If the coefficient is zero, either $5v_p(X)>a$, which requires $a$
even, or $5v_p(X)=a$, which requires $5\mid a$. This includes $Y=0$.
There are at most $m(a)$ possibilities, at every prime including 2 and 5.
We assert an upper alphabet, not local solubility of every listed value.

Consequently there are at most $C(N)$ finite height profiles. In a band
$H\le h(x)<(1+\epsilon)H$, two points with the same finite profile have
profile distance less than $\epsilon H$: the archimedean coordinate is
nonnegative, because $X^5\ge N$, and its difference is exactly their
height difference. This replaces the rounded-profile covering number in
Sections 2–5 by the exact count $C(N)$.

In particular, if $N$ is squarefree then $C(N)=1$. More generally
$m(a+10)=m(a)+1$, so high valuations add possible profiles linearly.
One cannot set $C(N)=1$ for arbitrary $N$; actual counterexamples are
recorded in the local control program.

### 8.2. Consequences for point counts

Retain the height error 14 and finite packing bounds of Sections 2–5. Let
$I_N(B)$ count all integral points with $1\le X\le B$, and let
$r_N=\operatorname{rank}J_N(\mathbb Q)$. The identical height-band proof,
now using the exact profiles, gives

$$
I_N(B)\le e^{1000010}C(N)(1+\log^+\log B)e^{851r_N/10000}.
\tag{AP3}
$$

The logarithmic factor is one for $B=1$. Indeed $h(x)\le\log X$, the
band count is at most $1001(1+\log^+\log B)$, and each high-height cell
contains at most $\exp(.0851r_N+85106)$ points. The at most
$2e^{1000000}$ low-height points are absorbed as in Sections 2–5. Torsion and
both signs are included.

For scaled height at most $H_*$, the congruence argument of Section 7 similarly
replaces $6000^{\omega(N)+1}$ by $2^{\omega(10N)+2}C(N)$:

$$
M_N(H_*)\le e^{1000010}2^{\omega(10N)+2}C(N)
(1+\log^+H_*)e^{(9/50)H_*+(201/5000)r_N}.
\tag{AP4}
$$

There are $C(N)$ profiles and at most $2p$ residue pairs, with
$p\le2^{\omega(10N)+1}e^{(9/50)H}$ in each height band.
The branch-residue and equal-coordinate local calculations are exactly
those in Section 7. No distribution of points among residue classes is assumed.

### 8.3. Arithmetic profiles in the ramified norm family

Let $-D$ be a negative fundamental discriminant, $d$ a squarefree divisor
of $\operatorname{rad}(D)$, and $z\ne0$. Put

$$
N=D(16d^2z)^2.
$$

Then the alphabet count satisfies

$$
C(N)\le3\tau(d|z|)\le3\,2^{\omega(d)}\tau(|z|).
\tag{AP5}
$$

Here $\tau$ is the ordinary divisor function. At an odd prime let
$b=v_p(|z|)$ and $\delta=\mathbf1_{p\mid d}$. The three possible
exponents in $N$ are $2b$, $1+2b$, and $5+2b$; the last occurs when
$p\mid d$. Directly from (AP1), their alphabet sizes are at most
$b+1,b+1,b+2$, respectively. To check these for all $b$, it suffices
to check $0\le b<5$: increasing $b$ by 5 increases $m$ by 1 and the
right side by 5. At 2 the exponent is
$v_2(D)+8+4\delta+2b$, with $v_2(D)\in\{0,2,3\}$ and
$\delta=0$ if $v_2(D)=0$. The same residue argument gives at most
$3(b+\delta+1)$. Multiplying proves the first bound in (AP5).
The second is the elementary inequality $\tau(mn)\le\tau(m)\tau(n)$.

There is also a forced lower height. Define

$$
F(N)=\prod_{\substack{p^a\parallel N\\a\ \mathrm{odd},\ 5\nmid a}}
 p^{a\bmod10}.
$$

Every finite profile contributes at least $(\log F(N))/5$. Let
$D_{\rm odd}=D/2^{v_2(D)}$. For each odd $p\mid D$ outside $d$,
its exponent in $N$ is $1+2v_p(z)$. This is a multiple of 5 only if
$v_p(z)\equiv2\pmod5$, hence $p^2\mid z$. The product $E$ of all
odd $p\mid D$ whose exponents in $N$ are multiples of 5 therefore
satisfies $E^2\le d^2|z|$. The other primes each divide $F(N)$.
Thus

$$
h(x)\ge\frac{\log F(N)}5
\ge\frac15\left(\log D-\log8-\log d-\frac12\log|z|\right).
\tag{AP6}
$$

This uses only valuation parity and the fundamental-discriminant convention.
It remains valid for even discriminants and imprimitive norm solutions.

### 8.4. A constant number of prime-selection intervals

Write $t=\log D$, $L=\log t$, and assume

$$
\frac14\le a\le\frac{13}{50},\quad
0\le\eta\le\frac1{20},\quad L\ge1000,
\qquad\nu=\frac{5a}2-\frac12+\frac\eta2.
\tag{AP7}
$$

For $b\le D^a$, $d\le D^\eta$ and
$dy^2+(D/d)z^2=4b^5$, one has $|z|\le2D^\nu$ and $\nu\le7/40$.
In the twist substitution, $h(x)\le at+(\log4)/5<t$. Equations (AP6)
and (AP7) give

$$
h(x)\ge\frac{69}{400}t-\frac{\log(8\sqrt2)}5,
\qquad
\log(10N)\le\frac{31}{20}t+\log10240.
\tag{AP8}
$$

All these points have height greater than $H_0=100000$. For a nonempty
band with $\epsilon=1/1000$, its lower endpoint satisfies
$H>[(69/400)t-\log(8\sqrt2)/5]/(1+\epsilon)$.
Put $u=9/50$. The positive slope

$$
\frac{52u(69/400)}{1+\epsilon}-\frac{31}{20}=
\frac{97}{1540}
$$

and the certified constant comparison imply $52uH>\log(10N)$.
Therefore at least one of the 52 Bertrand intervals
$(2^je^{uH},2^{j+1}e^{uH}]$, $0\le j\le51$, contains a prime
$p\nmid10N$:52 distinct bad primes, all larger than $e^{uH}$,
would have product exceeding $10N$. For this chosen good prime,

$$
2p\le2^{53}e^{uH}.
\tag{AP9}
$$

This is a uniform constant cost in the norm family, rather than a factor
exponential in $\omega(N)$. It relies on the forced-height inequality,
not on a probabilistic claim about prime factors or point residues.

### 8.5. Averaging the profile and rank weights

Let $R=201/5000$ and $\rho=e^{8R}<3/2$. The retained four-layer rank
bound and the elementary quadratic class-number upper bound give

$$
r_N\le\frac{2t}{\log5}+\frac{4L}{\log5}+1+8\omega(10D|z|).
\tag{AP10}
$$

For every positive integer $n$,

$$
\tau(n)\rho^{\omega(n)}\le\tau_3(n),\qquad
\sum_{n\le Z}\tau_3(n)\le Z(1+\log Z)^2.
\tag{AP11}
$$

The first bound follows prime by prime: for $e\ge1$,
$(e+1)\rho\le(e+1)(e+2)/2$. For the second, sum over two factors and
bound the third count by $Z/(ab)$, then use the harmonic-sum bound.

Use (AP5), (AP9), (AP10), and the finite packing coefficient
$\exp(Rr_N+402006)$ in each nonempty height band. There are at most
$1001(1+L)$ bands. Also
$\omega(10D|z|)\le\omega(D)+2+\omega(|z|)$,
$1+\log(2D^\nu)\le t$, and
$\sum_{d\mid\operatorname{rad}(D)}2^{\omega(d)}=3^{\omega(D)}$.
Summing both signs of $z$, all $d\le D^\eta$ and both signs of $y$ gives

$$
\sum_{\substack{d\mid\operatorname{rad}(D)\\d\le D^\eta}}
N_d^{z\ne0}(D^a)
\le e^{402060}(1+L)t^{2+4R/\log5}
D^{\nu+ua+2R/\log5}(3e^{8R})^{\omega(D)}.
\tag{AP12}
$$

The point theorem already counts both $y$ signs. The numerical constant
is justified by

$$
402006+\log12012+53\log2+17R+(u/5)\log4<402060.
$$

There is no small-height contribution in this application, by (AP8).
Using $\omega(D)\le t/(L-\log L-1)$ converts the last factor in
(AP12) into the cost $(\log3+8R)/(L-\log L-1)$ in its relative exponent.
The earlier worst-case profile/rank cost was
$[\log2+c_0(\log6000+8R)]/(L-\log L-1)$. The improved factor follows
from exact valuation restrictions and a positive average, without
assuming independence of residues and heights.

### 8.6. Evidence and scope

`check_quintic_arithmetic_profiles.py` verifies 40 complete floor-residue
cases, 34098 local coordinates on 5335 actual point pairs, 10670 weighted
scalings, and 2002 norm solutions over 94 negative fundamental discriminants,
including 704 solutions with even discriminant. There are 993 squarefree
pairs with a single profile and 2264 controls where assuming a single
profile for arbitrary $N$ fails. The local argument above proves the
infinite family; those actual-point computations are controls.

`certify_quintic_arithmetic_profiles.py` checks 11 positive 256-bit Arb
comparisons and four exact identities for the constants and monotone
domains in Sections 8.4–8.5. The fixed-curve height, rank and finite packing arguments are
imported from Sections 2–7. The conclusion (AP12) supplies the small-divisor component of Section 9.
Sections 9–11 include the larger-divisor interfaces and matching lower count.

## 9. A longer complete ramified norm range

Let $-D$ be a negative fundamental discriminant, $t=\log D$ and
$L=\log t$. Put

$$
a=\frac{2579}{10000},\qquad X=D^a,\qquad
\eta=\frac{159}{5000},\qquad \sigma=\frac1{10000}.
$$

For squarefree $d\mid\operatorname{rad}(D)$ with $d\le\sqrt D$,
let $N_d(X)$ count all integer triples $(b,y,z)$ satisfying
$1\le b\le X$ and $dy^2+(D/d)z^2=4b^5$. Then

$$
\sum_{\substack{d\mid\operatorname{rad}(D)\\d\le\sqrt D}}N_d(X)
<XD^{-\sigma},\qquad L\ge24000.
\tag{LP1}
$$

The exponent $a$ is larger than the $0.2561$ in the accepted norm theorem
[1]. The new saving and threshold serve this longer range; they do not
improve every parameter of the earlier theorem. Both signs, imprimitive
points and rational generators are included. The count is the complete
ramified population, without an additional representative factor.

The new input is the arithmetic-profile average in Section 8. The larger-divisor
inputs are the parametric lemmas of [3], with their domains checked below
at the changed value of $a$. The fixed-$a$ conclusion of [1] is not
substituted at a different exponent.

### 9.1. The small-divisor range

Write $u=9/50$, $R=201/5000$ and $P(L)=L-\log L-1$.
For $d\le D^\eta$ and $z\ne0$, the exact substitution is

$$
X_c=4db,\quad Y_c=16d^3y,\quad N=D(16d^2z)^2,
\qquad Y_c^2=X_c^5-N.
$$

It is injective for fixed $d,z$, and $|z|\le2D^\nu$, where
$\nu=5a/2-1/2+\eta/2=3213/20000$. The base descent in Sections 2 and 6 retains
both imaginary quadratic five-ranks. Exact valuation alphabets bound
its finite profile count by $3\tau(d|z|)$, and the forced denominator
bounds the scaled height below by
$[(1-\eta-\nu/2)t-\log(8\sqrt2)]/5$.

The complete argument Section 8, (AP7)–(AP12) gives

$$
\sum_{d\le D^\eta}N_d^{z\ne0}(D^a)
\le e^{402060}(1+L)t^{2+4R/\log5}
D^{\nu+ua+2R/\log5}(3e^{8R})^{\omega(D)}.
\tag{LP4}
$$

The sum is over the eligible squarefree ramified divisors. All hypotheses
are checked: $1/4\le a\le13/50$, $0\le\eta\le1/20$ and $L\ge1000$.
The constant prime-selection cost follows from the forced height;
the profile/rank average uses
$\tau(z)e^{8R\omega(z)}\le\tau_3(z)$ and
$\sum_{z\le Z}\tau_3(z)\le Z(1+\log Z)^2$.
The scaled upper height remains $at+(\log4)/5$.
The elementary factorial bound gives $\omega(D)\le t/P(L)$.

### 9.2. Rational generators

For $z=0$, squarefreeness of $d$ gives
$b=dv^2$ and $y=\pm2d^2v^5$, with $v\ge1$.
Their complete contribution over all $d$ is at most

$$
2^{\omega(D)+1}X^{1/2}.
\tag{LP5}
$$

This is not an application of a smooth-curve theorem at $N=0$.

### 9.3. Imported interfaces at the changed exponent

Let $\delta=\log d/t$ and
$Y_0=2D^{(5a-1+\delta)/2}$. The variables called $z,y$ in the
interfaces of [3] are respectively $b,z$ here.

For $\eta<\delta\le7/100$, use [3, (CP5)–(CP6), (CP20)] with

$$
U=Y_0^{1/7}X^{2/7},\qquad V=\sqrt{U/d},\qquad
W=Y_0^{11/14}X^{4/7}d^{-1/2}.
$$

It gives

$$
N_d(X)<2\cdot10^{10}5^{\omega(d)}t^3X
D^{(43a-11-3\delta)/28}.
\tag{LP6}
$$

Write $y_0=(5a-1+\delta)/2$, $u_0=(y_0+2a)/7$ and
$v_0=(u_0-\delta)/2$ for the powers of $D$ in these scales.
At both $\delta=\eta$ and $\delta=7/100$, the certificate checks
all of

$$
\begin{gathered}
V\ge10^6,\quad V\ge48t^2,\quad V\ge16t,\quad
U/4>V,\quad V/4>8,\\
Y_0\ge d,\quad \sqrt{Y_0}\le U\le Y_0,\quad
X\le Y_0^3,\quad Y_0^5\le X^4,\\
\log U<t,\quad\log V<t,\quad\log(dU^2V^2)<t,\quad
1+2\log U<t^2.
\end{gathered}
\tag{LP7}
$$

The completion ratio $X/(dU^2V^2)\le1$ and the repeated-prime
term $Y_0V/U\le W$ are also checked. These logarithmic powers are
affine in $\delta$, so the two vertices cover the whole interval.
The constants in the certificate dominate the factors of two in $Y_0$.

For $7/100<\delta\le3/10$, use [3, (KQ5), (KQ8)–(KQ9), (CP22)]
with

$$
Q=(Y_0X/d^{3/2})^{1/3}
=2^{1/3}D^{(7a-1-2\delta)/6}.
$$

The required conditions are $Q\ge\max(10^6,48t^2,16t)$,
$Q/4>8$ and $\log(dQ^2)<t$. They are checked at both endpoints.
The relative exponents, with common coefficient $10^6 8^{\omega(D)}t^2$,
are

$$
\frac{8a-2-\delta}{6},\quad
-\frac{7a-1-2\delta}{6},\quad
\frac{3a-1}{2},\quad-\frac\delta2.
\tag{LP8}
$$

For $3/10<\delta\le1/2$, the congruence-only count
[3, Section 10.7] has coefficient $192\,8^{\omega(D)}t^2$ and relative
exponents

$$
\frac{5a-1-\delta}{2},\quad
\frac{3a-1}{2},\quad-\frac\delta2,\quad\frac\delta2-a.
\tag{LP9}
$$

The square-detector conditions are uniform throughout: $X<\sqrt D/4$
excludes zero values, by the squarefree-kernel argument in [3, Section 10.4],
and $\log(8X^5)<3t\log2$ bounds the number of their prime divisors.
Both inequalities are certified at the changed $a$.

Summing (LP6) over divisors gives $6^{\omega(D)}$, since
$\sum_{d\mid\operatorname{rad}(D)}5^{\omega(d)}=6^{\omega(D)}$.
The other two ranges may each use at most $2^{\omega(D)}$ divisors.
The aggregate bounds for the three ranges are therefore

$$
\begin{aligned}
&2\cdot10^{10}6^{\omega(D)}t^3XD^{-\gamma_p},
&&\gamma_p=\frac{11+3\eta-43a}{28}=\frac{57}{280000},\\
&10^6\,16^{\omega(D)}t^2XD^{-\gamma_m},
&&\gamma_m=\frac{17}{15000},\\
&192\,16^{\omega(D)}t^2XD^{-\gamma_\ell},
&&\gamma_\ell=\frac{21}{4000}.
\end{aligned}
\tag{LP10}
$$

The last two savings are the minima of the four negative relative
exponents in (LP8) and (LP9), respectively. No new analytic proof of
these interfaces is claimed.

### 9.4. Complete scalar comparison and scope

Put $\gamma_s=a-\nu-ua-2R/\log5$. To bound each of (LP4), (LP5)
and the three lines of (LP10) by $XD^{-\sigma}/5$, it suffices that

$$
\begin{aligned}
\gamma_s-\sigma>{}&
\frac{\log3+8R}{P(L)}\\
&+\left[402060+\log5+\log(1+L)+\left(2+\frac{4R}{\log5}\right)L\right]e^{-L},\\
\frac a2-\sigma>{}&\frac{\log2}{P(L)}+(\log10)e^{-L},\\
\gamma_p-\sigma>{}&\frac{\log6}{P(L)}+
(\log10^{11}+3L)e^{-L},\\
\gamma_m-\sigma>{}&\frac{\log16}{P(L)}+
(\log(5\cdot10^6)+2L)e^{-L},\\
\gamma_\ell-\sigma>{}&\frac{\log16}{P(L)}+
(\log960+2L)e^{-L}.
\end{aligned}
\tag{LP11}
$$

The program `certify_quintic_arithmetic_population.py` verifies 89 positive
comparisons using 256-bit Arb, five exact identities and six affine
vertices. At $L=24000$, the smallest population margin is greater than
$2.88\cdot10^{-5}$, in the congruence-period range.
Every right side of (LP11) decreases: $P$ increases, and its other
terms are positive linear or logarithmic functions multiplied by $e^{-L}$,
with derivative signs checked explicitly. The domain comparisons in
(LP7) and the middle range have the form
$c-(\log C+mL)e^{-L}>0$, with positive $c$; they also strengthen on the
whole half-line. This proves (LP11) for every $L\ge24000$.
Summing the five contributions proves (LP1).

The certificate hashes the arithmetic-profile controls and constant
certificate, both congruence outputs, the exact height and generic-doubling
certificates, and the consulted accepted parametric source. It does not verify the general mathematical arguments or
independently reprove the imported analytic interfaces.

Sections 10–11 supply the complete short-ideal lower bound at this
cutoff, including ordinary, quadratic and quartic characters, common weights
and tails.

## 10. Quadratic-genus counts at the longer cutoff

This section repeats the rough/smooth genus proof of [4, Section 5] at a
new cutoff $b=257/1000$ and threshold $L=24000$. The accepted Lemma 5.1
in [4] has threshold 30000 and cutoff $511/2000$; its statement is not
being invoked outside that range. The three-step interval recurrence,
complete-sum estimate and Burgess input are the same. The domain and
family inequalities are rechecked below with new explicit constants.
No new mechanism or historical priority is claimed for this specialization.

Write $t=\log D$, $L=\log t$, $k=\omega(D)$ and $g_2=2^{k-1}$.

**Lemma.** For $L\ge24000$ and $D^{257/1000}\le x\le D$,
the ordinary ideal count satisfies $A(x)>x/(12t)$, and the sum of
absolute counts twisted by nontrivial genus characters is less than
$x/(1000t)$. In particular every ordinary genus contains more than
$x/(24tg_2)$ integral ideals of norm at most $x$.

The exact genus Dirichlet-product identity, including ramified norms,
is the one in [3, Section 9.1], based on [10, Theorems 3.5 and 4.3]
at order conductor one. Every nontrivial genus character gives two
nonprincipal fundamental characters of conductors $q_1q_2=D$.
We prove the required bounds for these convolutions.

The explicit moment-$100$ Burgess estimate of [3, Sections 9.3--9.4],
including its periodicity patch for small conductors, gives

$$
|S_\chi(N)|\le Bq^{101/40000}N^{99/100},\qquad
B=800(1+t)8^{1/100}t^{1/200}40000^{k/200}.
\tag{G24}
$$

It holds on every integer interval, and
$\log B\le8+(201/200)L+(53/1000)k$ for $t\ge1003$.
The elementary factorial bound is

$$
k\le\frac{t}{P(L)},\qquad P(L)=L-\log L-1.
\tag{G25}
$$

To verify it, if $k\ge t/P(L)$ then
$k(\log k-1)>t$, contradicting $\log(k!)\le\log D$.
The same argument applies to any specified part of the prime factors.

Put $\eta=10^{-6}$ and let $R(D)$ be the product of odd primes
$p\mid D$ exceeding $D^\eta$. If $R(D)>\sqrt D$, at most $10^6$
such primes occur and the remaining factors have product below
$\sqrt D$. Hence

$$
k\le10^6+\frac{t}{2P(L-\log2)}.
\tag{G26}
$$

If $R(D)\le\sqrt D$, every complementary pair has a conductor $q$
with $R(q)\le\sqrt q$: otherwise multiplying the two strict reverse
inequalities is a contradiction. Write $Q=\log q/t$, and first
suppose $Q\ge c_1=7/5000$. Set
$\delta_A=1/25000$ and $\nu_A=Q/4+8\delta_A$. The odd part of $q$
can be factored into coprime $q_0q_1q_2q_3$ with

$$
D^{Q/2-\eta}\le q_0\le D^{Q/2},\qquad
q_i\le D^{Q/4}\ (i=1,2,3),\qquad q_0\ge D^{16\delta_A}.
\tag{G27}
$$

Start $q_0$ with all its large primes and fill with small primes to
the lower threshold, if needed. The odd part is at least $D^Q/8$,
so enough factors exist. The remaining product is at most
$D^{Q/2+\eta}$. Greedy bins of capacity $D^{Q/4}$ suffice: after
two closed bins the remaining exponent is less than $3\eta<Q/4$.
Also $Q/2-\eta\ge16\delta_A$ in the stated range.

Here are the explicit interval constants. With
$H_i=\lfloor N/q_i\rfloor\ge1$, three ordinary Cauchy differencing
steps give the recursive upper bounds

$$
b_4=\min(1,E),\quad
b_i=\min(1,\sqrt{2/H_i+4b_{i+1}}),\quad
E=8^{\omega(q_0)}\prod_{p\mid q_0}(1+p^{-1/2})^3
 \left[q_0^{-1/2}+(1+\log q_0)\frac{\sqrt{q_0}}N\right].
\tag{G28}
$$

To obtain the recurrence, average $H_i$ translates of the interval by
$q_i h$. The enlarged support has at most $2N$ points. Bound the
periodic factor's absolute square before expanding, charge the diagonal
by $2/H_i$, and pair the positive and negative differences. Intersections
of translated intervals remain intervals of at most $N$ points.
When nesting the steps with Jensen's inequality, adjoin a dummy zero
term for the entire next-stage random variable, including its diagonal
part. The resulting diagonal average has the factor $(H_i-1)/H_i$;
enlarging that factor to one gives exactly the displayed recurrence.
The terminal cube has degree eight. Its square criterion and exceptional
shift average are exactly those of [4, Section 2.3]; interval Fourier
completion costs $N/q_0+1+\log q_0$. Thus (G28) includes every shift.

Take $N=\lfloor D^{\nu_A}/16\rfloor$. Then
$H_i\ge D^{8\delta_A}/64$ and the two terminal powers are at most
$D^{-8\delta_A}$ and $32(1+t)D^{-8\delta_A}$.
Expanding the three square roots in (G28), and splitting into the eight
dyadic residue classes, gives, uniformly for $z\ge D^{\nu_A}$,

$$
|S_\chi(z)|\le\mu_A z,\qquad
\mu_A=2^{10}(1+t)e^{7\omega(q_0)/16}D^{-\delta_A}.
\tag{G29}
$$

For clarity, the odd-interval coefficient is at most $128$: the three
diagonal coefficients are
$\sqrt{128},2\cdot128^{1/4},2^{3/2}128^{1/8}$ and the terminal
coefficient is at most $2^{7/4}33^{1/8}$, whose sum is below $128$.
The eighth root of the local coefficient is at most
$e^{7\omega(q_0)/16}$ by [4, (10)]. A dyadic progression split and blocks
of at most $N$ points have total capacity at most $z+8N\le3z/2$;
the coefficient $2^{10}$ covers this and the floors.
Since $\log\log q_0\ge L-8$, (G25) also gives

$$
\omega(q_0)\le\frac{Qt}{2P_*(L)}\le\frac{t}{2P_*(L)},
\qquad P_*(L)=L-\log L-10.
\tag{G30}
$$

Retaining $\omega(q_0)$ instead of replacing it by $k$ is material.

Set $\delta_B=13/400000$. Equation (G24) gives
$|S_\chi(z)|\le\mu_Bz$, where
$\mu_B=BD^{-\delta_B}$, for
$z\ge D^{\nu_B(Q)}$ and
$\nu_B(Q)=(101/400)Q+100\delta_B$.
If the smaller conductor exponent is at most $c_1$, primitive
completion $2\sqrt q(1+\log q)$ gives the same coefficient at
$\nu_P(Q)=Q/2+\delta_B$. The two threshold sums satisfy

$$
\max_{0\le Q\le c_1}(\nu_P(Q)+\nu_B(1-Q))=.256129,
\qquad
\max_{c_1\le Q\le1-c_1}(\nu_A(Q)+\nu_B(1-Q))=.2560665.
\tag{G31}
$$

Both are below $257/1000-1/20000$. Real-cutoff hyperbola with these
thresholds, $UV=x$, and the harmonic sum bound therefore yields
$|C_S(x)|\le4(1+t)x(\mu_A+\mu_B)$ in the small-$R$ regime.
The overlap costs at most $x\mu_A\mu_B$; both coefficients are below
one. In the large-$R$ regime, balanced Burgess hyperbola instead gives
$|C_S(x)|\le201BxD^{-\gamma}$ with $\gamma=9/400000$.

Put $d_1=53/1000$ and
$F(L)=(50+8L+10^6(\log2+d_1))e^{-L}$. The three sufficient
family inequalities are

$$
\begin{aligned}
\delta_B&>\frac{\log2+d_1}{P(L)}+F(L),\\
\delta_A&>\frac{\log2}{P(L)}+\frac7{32P_*(L)}+F(L),\\
\gamma&>\frac{\log2+d_1}{2P(L-\log2)}+F(L).
\end{aligned}
\tag{G32}
$$

Their margins at $L=24000$ are given in the accompanying certificate;
all three are strictly positive.
The common $F$ covers the displayed coefficients, the extra factor $t$
in the target denominator, and the fixed prime count in (G26). Every
positive cost decreases thereafter. This proves the claimed genus-family
bound. Finally the accepted ordinary hyperbola, (G24), and [11] give
$A(x)>x/(12t)$: with
$b_B=(9+2L)e^{-L}+d_1/P(L)$, its sufficient conditions are

$$
\frac{257}{1000}-100\frac{101}{40000}>100b_B,
\quad
\frac{257/1000-100(101/40000)}{101}
>\frac{100}{101}b_B+(\log2424+L)e^{-L}.
\tag{G33}
$$

They hold at the same threshold and improve thereafter. Orthogonality
proves the final assertion of the lemma. The accompanying certificate
checks (G27)–(G33), the coefficient expansions, and all floor, dyadic,
and small-conductor conditions using 41 positive intervals and six
exact rational identities.

### 10.1. Evidence and scope

`certify_longer_cutoff_genus.py` checks the coefficient, floor, dyadic,
small-conductor, ordinary and genus-family budgets, with their monotonic
continuation for $L\ge24000$. The program certifies scalar comparisons;
it does not prove the imported Burgess, Weil, genus-character identities
or the repeated Cauchy argument. The argument above retains the entire
ordinary genus, including all ramified norms and both signatures of the
fundamental Dirichlet factors. It supplies the quadratic-family input
at a larger ideal cutoff. Section 11 combines this with the quartic and norm-population arguments.

## 11. The uniform exponent-forty transfer

Let $-D$ be a negative fundamental discriminant and let
$G=\operatorname{Cl}(-D)$ be the ordinary ideal class group. The result is

$$
\exp G\mid40\quad\Longrightarrow\quad\log\log D<24000.
\tag{GT1}
$$

Thus $B=\exp(\exp24000)$ and $\log B=\exp24000$. This improves the
accepted $40000$ threshold [4] within the short-ideal method. It gives
neither a classification nor an improvement to the strongest numerical
class-number-one cutoff. No census is used.

The new input is the complete ramified norm population of Section 9 at the longer
cutoff $a=2579/10000$. The Gaussian theorem and conductor-block map are imported from [4].
The quadratic-genus input is the new specialization in Section 10, proved at cutoff
$D^{257/1000}$ and threshold 24000; the accepted 30000-threshold lemma in
[4] is not invoked below its range. We rederive the older
moment and weight estimate at new moments from the parametric proofs in
[3] and [4, Section 6.2]; their previously specialized conclusions are
not asserted to hold with changed parameters. The arithmetic-profile argument in Section 8 supplies the point-count average,
using the base height, rank and congruence arguments [12].

### 11.1. Inputs and fixed parameters

Write $t=\log D$, $L=\log t$, $k=\omega(D)$ and
$P(L)=L-\log L-1$. Suppose for contradiction that $L\ge24000$ and
$\exp G\mid40$. Set

$$
\begin{gathered}
a=\frac{2579}{10000},\quad X=D^a,\quad v=\frac X{t^2},
\quad y=\frac{64463}{250000},\quad Y=D^y,\quad\theta=\frac38,\\
\epsilon_o=\frac{47}{500000},\quad
j=8,\quad s=\frac1{256},\quad\sigma_s=1-s,\quad
\eta_c=10^{-6},\\
\delta=\frac{19}{400000},\quad
\kappa_s=\frac3{25000},\quad\epsilon_s=\frac3{50000},
\quad\rho=D^{-\epsilon_s},\quad h_c=\frac{13}{500}.
\end{gathered}
\tag{GT2}
$$

The subscripts distinguish the conductor prime threshold and the shape
exponent from the small-divisor cutoff in Section 9. The elementary factorial
argument gives $k\le t/P(L)$, also for any specified product of prime
factors after replacing $t$ by the logarithm of that product.

| Input | Exact scope used |
|---|---|
| Complete norm population | Section 9, (LP1): $\sum_dN_d(X)<XD^{-1/10000}$ for $L\ge24000$, with both signs and imprimitive and rational solutions |
| Averaged Gaussian/Bessel estimate | [4, (22)], for fixed conductor ideals, both signatures, real signs and low Gaussian scales |
| Ordinary and genus counts | New specialization Section 10, for $L\ge24000$ and $D^{257/1000}\le x\le D$ |
| Class-character realization and blocks | [3, Sections 12, 14.6--14.7], as used in [4, Section 6.3] |
| Moment and overlap estimates | [3, (GB15)–(GB18), (CI4)–(CI8), (CF4)–(CF8), (CF25)–(CF26)] |
| Lower $L$-value and norm injection | [3, Sections 9--10], with the source dependency specified in [4] |

The source copy of [3] is the public version 6 download, SHA256
`1559be18df90c8269e2eba6a2cf937b83667a3ece3f3bc258116731869aaf8da`.
This is the accepted source for the parametric norm interfaces and the
constant-energy argument, including its Section 19.

### 11.2. The conductor-factorable family

For a quartic-square block, let $d=D^\alpha\le\sqrt D$ be its selected
auxiliary absolute discriminant. Its conductor is $n_2q=D/d$, with
$n_2\in\{1,4,8\}$ and $q$ odd squarefree. Its ordinary genus number
is $g$. Let $R_q$ be the product of $p\mid q$ exceeding $D^{\eta_c}$.
Put

$$
b_0=2y-\alpha-h_c,\qquad
\beta_0=1-2y+h_c+\eta_c=\frac{510297}{10^6},
$$

$$
c_i=y-\frac\alpha2-\kappa_s-\frac{2\log3}{P(L)}
                -2^{i+1}\delta-\eta_c\quad(1\le i\le8).
\tag{GT3}
$$

If $\alpha\le\theta$ and $R_q\le D^{b_0-\eta_c}$, start $q_0$
with $R_q$ and add small prime factors until its exponent reaches
$b_0-\eta_c$. Enough factors exist since
$1-\alpha-(\log8)/t>b_0$. Each added factor has exponent at most
$\eta_c$, so

$$
D^{b_0-\eta_c}\le q_0\le D^{b_0}.
\tag{GT4}
$$

The core is nontrivial: $b_0-\eta_c\ge114703/10^6>0$.
Every remaining prime factor is small, and their total exponent is at
most $\beta_0$. Greedy packing into eight bins of capacities $c_i$
succeeds because $c_i>\eta_c$ and

$$
\sum_{i=1}^8c_i-7\eta_c>\beta_0.
\tag{GT5}
$$

Indeed a closed bin has exponent greater than $c_i-\eta_c$;
after seven such bins the remainder fits in the eighth. The margin in
(GT5) exceeds $.00236125$ at $\alpha=\theta,L=24000$ and improves
as $\alpha$ decreases or $L$ increases. Lift the factorization to the
selected conductor prime ideals for each orientation. These ideals are
fixed over the entire class sum and real unit period.

Put $u=\pi v$, $u_8=(4/7)^8u$ and use the translation bound from
[4, (7)] with

$$
B_i=64\,3^{\omega(q_0)}\sqrt{q_i}\,d^{1/4}D^{\kappa_s/2},
\qquad H_i=\left\lfloor\frac{\sqrt{u_8}}{B_i}\right\rfloor.
$$

Since $u\ge D^y$, (GT3) gives

$$
\frac{\sqrt{u_8}}{2B_i}
\ge\frac{D^{2^i\delta+\eta_c/2}}{128(7/4)^4}
\ge D^{2^i\delta}.
\tag{GT6}
$$

Thus $H_i\ge D^{2^i\delta}$, with the floor accounted for, and
$u\ge2(7/4)^8\max_iB_i^2$, as required for the small-scale part of
[4, (22)]. That theorem has

$$
\frac{\log T_8}{256t}\le\Gamma(L):=
\frac{4\epsilon_s+28/(3P(L))+
                    (52\log2+4\log513)e^{-L}}{256}.
$$

Its three terminal savings, after this coefficient, are at least

$$
\frac{2y-\theta-h_c-\eta_c}{512}-\Gamma(L),\qquad
\frac{h_c}{512}-\Gamma(L),\qquad
\frac{y/2-\theta/4}{256}-\Gamma(L).
\tag{GT7}
$$

Each exceeds $\delta$. The smallest excess is greater than
$8.2395\cdot10^{-7}$. The shape and sign savings are
$\kappa_s/2=\epsilon_s$, and the unrooted shortest-vector saving
$y/2-\theta/4$ is larger. Since $2+\log d\le t$, (22) gives

$$
\frac{|V_C(v)|}{v}
\le2^{20}t\,g^{-\sigma_s}D^{-\delta}
                  +2^{21}tD^{-\epsilon_s}.
\tag{GT8}
$$

Here $V_C(v)=\sum_{I\in C}\psi(I)K_0(NI/v)$ is the common Bessel
weight of [4]. All eleven rooted terms and three error terms fit the
displayed coefficients. Real infinite signs and exceptional shifts are
already included in the imported theorem; they are not treated as periodic.

### 11.3. Repeating the older moment derivation at 80 and 104

For either $r\in\{80,104\}$ put

$$
\sigma_r=1-\frac1{2r},\qquad
A_r=(4r^2+1)^{1/(2r)},\qquad
c_r=\frac{y-\epsilon_o-1/4-1/(2r)}r,\qquad
\lambda_r=\frac{\epsilon_o+1/(2r)}r.
\tag{GT9}
$$

These parameters are

| $r$ | $\sigma_r$ | $c_r$ | $\lambda_r$ | rational-error saving |
|---:|---:|---:|---:|---:|
|80|$159/160$|$377/20000000$|$793/10000000$|$117/25000$|
|104|$207/208$|$19177/676000000$|$31861/676000000$|$14043/2600000$|

To justify this specialization, take any $D^y\le w\le X$, let
$\beta=1-\alpha$, $\kappa_{\rm box}=(D/d)^{\epsilon_o}$,
$J=8\lceil q^{1/(2r)}\rceil$, and

$$
T=\frac{w}{\kappa_{\rm box}^2J^2}
\ge\frac{D^\tau}{256},\qquad
\tau=y-(2\epsilon_o+1/r)\beta.
\tag{GT10}
$$

The complete moments [3, (GB15)–(GB17)] allow every positive integer
moment $r$; lengths smaller than $r$ are explicitly handled there.
Their maximal-prefix coefficient at each selected $r$ satisfies
$18(2r)^{1/(2r)}+30\sqrt{3r}<3000$.

For $\log\log d\ge1000$, use the independent ordinary-genus density
argument [3, Section 18.3] with moment 10 and $W_d=d^{3/10}$. The
short-common-ideal condition (CI4) is checked on $[0,1/3]$ by
$\tau-3\alpha/5$ and on $[1/3,1/2]$ by both
$\tau-3\alpha/10$ and $(\tau-a)/2+\alpha/5$, after the factors
$g\le2^k$, powers of $t$ and the constants in (GT10) are charged.
All are affine in $\alpha$, so the three vertices $0,1/3,1/2$ suffice.
The same certificate checks $T\ge16\sqrt d$, $(1+\log T)^3\le T$,
$\kappa_{\rm box}\ge2$ and the conic margin $5/4-4a>0$.

The constant-energy theorem [3, Theorem 19.1] applies because
$w\le D^a<D^{13/50}$, $d\le\sqrt D$, and
$q=D/(n_2d)\ge D^{999/1000}/(8d)$. Thus the positive first and
grouped second moments are respectively
$1100M(1+\log T)^3/g$ and $2401M(1+\log T)^7/g$, with
$M=wT/\sqrt d$. A single Hölder inequality gives the same
$g^{-\sigma_r}$ as in the accepted derivation. Before simplifying
powers, its leading term is bounded by

$$
7\cdot10^6 A_r^k g^{-\sigma_r}t^{3+1/(2r)}
w^{1-1/r}\kappa_{\rm box}^{1/r}d^{1/(4r)}
(D/d)^{1/(4r)+1/(2r^2)}.
\tag{GT11}
$$

The constant follows by checking
$2\,1100^{1-1/r}2401^{1/(2r)}3000\,16^{1/r}<7\cdot10^6$.
Its relative exponent at $w=D^y$ is exactly

$$
\frac{-y+\epsilon_o(1-\alpha)+1/4+(1-\alpha)/(2r)}r
=-c_r-\lambda_r\alpha.
\tag{GT12}
$$

For smaller $d$, use the unrestricted moments with $W_d=1$.
Restoring $g^{-\sigma_r}$ costs at most
$R_{{\rm sm},r}=\exp(\sigma_re^{1000})$, since $g\le d$.
There is no use of a density statement below its threshold.

The remaining pointwise terms in the same derivation have savings

$$
\delta_{{\rm rat},r}=
\min_{\alpha=0,1/2}
\left(y-\frac\alpha2-\epsilon_o(1-\alpha)
                         -\frac{1-\alpha}{2r}\right),
\quad\frac{\epsilon_o}2,\quad\frac y2-\frac18.
\tag{GT13}
$$

The translation error retains $g^{-1}$. Apply the ordinary-genus
projector before translating. Every nonzero translated element in $A$
still represents the same ideal class $[A]^{-1}$; the exact class
measure is $h/g$ in the imaginary case and $hR/g$ in the real case,
before their usual root-of-unity and factor-two normalizations.
The real integral is over the whole unit period, including infinite
signs. The calculation [4, (45 a)] consequently gives

$$
\frac{96tw}{g\kappa_{\rm box}}+288t d^{1/4}\sqrt w.
\tag{GT14}
$$

This argument is independent of the choice between 80 and 104.

For clarity, the weight conversion is repeated here. In imaginary
signature integrate the pointwise bound against $K_1(w/v)/v$; in
real signature use
$V_C(v)=v^{-1}\int_0^\infty e^{-w/v}W_C(w)\,dw$ with the
pointwise arcosh sum $W_C$. Their main first moments are $(\pi/2)v$
and $v$. Below $Y$, the genus upper bound above $W_d$ and the
unrestricted bound below it give

$$
A_C(z)\le2t(z/g+W_d),\qquad
\int_1^Y A_C(z)\frac{dz}{z}\le2tY/g+2t^2W_d.
$$

For the real arcosh kernel, the two corresponding integrals are
bounded by $\pi w/2$ and $\log(2w)$, giving the same majorant after
Laplace integration since $Y\le v$ and $\log(2Y)\le t$.
For $\log\log d<1000$, restore the genus divisor using
$R_0=\exp(e^{1000})$. Both low pieces are at most
$2R_0tY/g+2t^2d^{3/10}$. Dividing by $v$, the residual term has
saving $a-3/20$ without a genus factor.

Above $X$, the unrestricted count gives respectively the normalized
majorants $12Xe^{-t^2/2}$ and $16t^2X^2e^{-t^2}$; both are below
$D^{-1}$. These include the boundary contribution and use no
pointwise moment estimate outside $[Y,X]$. We obtain

$$
\begin{aligned}
\frac{|V_C(v)|}{v}\le10^{10}t^4\big[
&A_r^kg^{-\sigma_r}R_{{\rm sm},r}D^{-c_r}d^{-\lambda_r}
 +g^{-1}D^{-\epsilon_o/2}+R_0g^{-1}D^{-a+y}\\
&+D^{-\delta_{{\rm rat},r}}+D^{-y/2+1/8}
 +D^{-a+3/20}+D^{-1}\big].
\end{aligned}
\tag{GT15}
$$

This is the newly specialized inequality, derived from the cited
parametric proofs. The two genus errors have common saving
$\delta_g=47/1000000$; the four unrestricted errors have common
saving $\delta_f=1963/500000$. All auxiliary restoration factors
remain explicit.

### 11.4. Complementary populations and all quartic blocks

The accepted block map associates $k_d$ prime-discriminant factors
with $d$, and $g\ge2^{k_d-2}$. A quartic square has a torsor of
$2^{k-1}$ roots; its relevant subgroup has size $2g$ and its two
lifts exchange a character with its inverse. Conjugation preserves
the global weighted sum. Hence (GT8) and (GT15) are bounds for the
absolute block sums, uniformly over the remaining orientations.
They do not grant a genus divisor to each quartic character separately.

If $\alpha>\theta$, the complementary product is at most
$D^{1-\theta}$. Write

$$
K=\frac t{P(L)},\quad
B_\ell=\frac{(1-\theta)t}{P(L+\log(1-\theta))},\quad b=B_\ell/K.
$$

For $r=80$, let
$F_\sigma(b)=-b\log b-(1-b)\log(1-b)+(1-\sigma+\sigma b)\log2$.
The indicator bound $1_{m\le B_\ell}\le x^{m-B_\ell}$,
with $x=b/(2^{\sigma_{80}}(1-b))<1$, gives exactly as in
[4, (48)–(49)]

$$
2^{k-1}\sum_{d>D^\theta}g^{-\sigma_{80}}d^{-\lambda_{80}}
\le2D^{-\lambda_{80}\theta}
                \exp\left(\frac{tF_{\sigma_{80}}(b)}{P(L)}\right).
\tag{GT16}
$$

Here the generating bracket exceeds one before $k\le K$ is used.
The dyadic absolute discriminant factor is at least its underlying
prime, so the complementary count remains valid. Concavity of $\log P$
shows $b(L)$ decreases; $F_\sigma$ increases up to
$2^\sigma/(1+2^\sigma)$, which exceeds $b$ throughout this range.
Thus the positive entropy cost decreases with $L$.

If $\alpha\le\theta$ but $R_q>D^{b_0-\eta_c}$, the product of
small complementary prime-discriminant factors is less than
$D^{\beta_0}$. At most $10^6$ primes exceed $D^{\eta_c}$. Hence

$$
m=k-k_d\le B_c=10^6+\frac{\beta_0t}{P(L+\log\beta_0)}.
\tag{GT17}
$$

Use $r=104$, $\nu=99/100$ and $x=31/100$. Replace the selected
prime-discriminant factors by their underlying primes. For primes
$p\ge t^\nu$, $p^{-\lambda_r}\le e^{-\nu\lambda_rL}$.
Restoring this upper bound at the at most $t^\nu$ smaller primes
costs $R_{\rm small}=\exp(\nu\lambda_rLt^\nu)$. Therefore

$$
A_r^k2^{k-1}\sum_{\text{core failures}}g^{-\sigma_r}d^{-\lambda_r}
\le2R_{\rm small}x^{-B_c}
 \left[A_r\big(2^{1-\sigma_r}e^{-\nu\lambda_rL}+2x\big)\right]^k.
\tag{GT18}
$$

The bracket is less than $.997311983$ at $L=24000$ and decreases.
Discard its $k$ th power using $k\ge0$. Replacing $k$ by an upper
bound at this point would reverse the required inequality.

The three families are disjoint and exhaustive. The two old-estimate
families share the uniform error coefficient in (GT15), so their errors
are charged once over their union. The exact block count gives
$2^{k-1}\sum_dg^{-1}\le2\cdot3^k$, while unrestricted errors
use at most $4^k$ characters. The Gaussian main family has base
$2+2^{1/256}$, and its shape/sign errors also use $4^k$.

Put $J_*(L)=(10^8+100L)e^{-L}$. Sufficient conditions for each of
the six contributions to be less than $v/(8000t)$ are

$$
\begin{aligned}
\delta&>\frac{\log(2+2^{1/256})}{P(L)}+J_*(L),\\
\epsilon_s&>\frac{\log4}{P(L)}+J_*(L),\\
c_{80}+\lambda_{80}\theta
&>\frac{\log A_{80}+F_{\sigma_{80}}(b)}{P(L)}
                        +\sigma_{80}e^{1000-L}+J_*(L),\\
c_{104}&>\log(1/x)\left[10^6e^{-L}
               +\frac{\beta_0}{P(L+\log\beta_0)}\right]
 +\nu\lambda_{104}Le^{-L/100}
 +\sigma_{104}e^{1000-L}+J_*(L),\\
\delta_g&>\frac{\log3}{P(L)}+e^{1000-L}+J_*(L),\\
\delta_f&>\frac{\log4}{P(L)}+J_*(L).
\end{aligned}
\tag{GT19}
$$

The allowance dominates $(\log(8000\cdot10^{12})+5L)e^{-L}$
for (GT15), and $(\log(8000\cdot2^{22})+2L)e^{-L}$ for (GT8).
It includes the fixed factors and all grouped error terms. At $24000$
the six margins respectively exceed

$$
1.6656\cdot10^{-6},\quad2.2110\cdot10^{-6},\quad
2.3821\cdot10^{-7},\quad3.4540\cdot10^{-6},\quad
1.2033\cdot10^{-6},\quad.0038682.
$$

All positive costs decrease thereafter, using the entropy monotonicity
above and the decreasing function $Le^{-L/100}$. Consequently

$$
\left|\sum_{\operatorname{ord}\chi=4}V_\chi(v)\right|
<\frac{v}{1000t}.
\tag{GT20}
$$

This uses absolute block bounds, not cancellation between blocks.

### 11.5. From the common weight to the complete norm population

The new quadratic-genus specialization in Section 10 applies because
$v\ge D^{257/1000}$ and $L\ge24000$. Since $K_0(1)>1/5$, its ordinary
lower count gives $V_1(v)>v/(60t)$. For nontrivial genus characters,
partial summation above $Y_g=D^{257/1000}$ costs at most
$\pi v/(2000t)$. The lower part is at most $2^{k-1}tY_g$;
the upper tails are bounded as in Section 11.3. Each is less than
$v/(10000t)$ by the certificate. Thus

$$
\sum_{\chi\ne1,\ \chi^2=1}|V_\chi(v)|<\frac v{500t}.
$$

Orthogonality over characters of order dividing four and
$|G/G^4|\le4^k$ now imply

$$
V_{G^4}(v)>\frac{v}{100t\,4^k}.
\tag{GT21}
$$

For the remaining norm tail,
$K_0(x)\le\sqrt{\pi/(2x)}e^{-x}$ and
$a_K(n)\le\tau(n)\le2\sqrt n$ give
$\sum_{NI>X}K_0(NI/v)\le6v^{3/2}e^{-t^2}<v/(200t4^k)$.
For $NI\le X$, $K_0(NI/v)\le K_0(1/v)<\log(2v)+1\le t$.
The number of all integral ideals in $G^4$ with norm at most $X$
therefore exceeds

$$
\frac{X}{200t^4\,4^k}.
\tag{GT22}
$$

If $\exp G\mid40$, the fifth power of every class in $G^4$ lies
in $G[2]$. The ramified-generator injection [3, Section 10] chooses
a squarefree representative $d\mid\operatorname{rad}(D)$,
$d\le\sqrt D$, for each such class. For an ideal of norm $b$, a
generator of its fifth power times that ramified ideal gives
$dy^2+(D/d)z^2=4b^5$ after dividing the divisible coordinate by $d$.
Unique ideal factorization makes the chosen generator assignment
injective into these triples. The count in Section 9 already sums over all
eligible $d$ and all signs. Rational and imprimitive generators are
included, so no extra ramified-representative multiplier is introduced.
It bounds (GT22) by $XD^{-1/10000}$.

A sufficient contradiction is

$$
\frac1{10000}>
\frac{\log4}{P(L)}+(\log400+5L)e^{-L}.
\tag{GT23}
$$

Its margin exceeds $4.2211\cdot10^{-5}$ at $L=24000$ and increases.
This proves (GT1) from the stated inputs.

### 11.6. Evidence and limitations

`certify_arithmetic_profile_global_transfer.py` checks 149 positive
256-bit Arb comparisons and 19 exact identities. These include both
moment-domain audits, the six family budgets, fixed conductor-factor
packing, Bessel conversion coefficients, auxiliary restoration, the
generating bracket and the final norm comparison. Affine vertex checks
and explicit monotonicity cover the whole half-line $L\ge24000$.
The new norm certificate separately checks its changed-cutoff domains.

These programs certify scalar inequalities. The general moment, class-field,
height, lattice, Weil, weight and injection arguments are the written proof
and its named imports. The author audit presently identifies no concrete
unresolved proof defect in this extension. Independent mathematical review
of it is pending. The reported public audit of the earlier base point-count
packet [12] does not cover the congruence extension or this new endpoint.

## 12. Reproduction, proof status and application limits

The supplement contains this consolidated proof, thirteen programs, their outputs
and source-provenance records. Run these
from its root, in order:

    python code/check_quintic_jacobian_frobenius.py
    python code/check_quintic_kummer_repulsion.py
    python code/certify_quintic_fixed_curve_height.py
    python code/check_quintic_generic_doubling.py
    python code/certify_quintic_point_packing.py
    python code/certify_quintic_repulsion_population.py
    python code/check_quintic_congruence_repulsion.py
    python code/certify_quintic_congruence_packing.py
    python code/check_quintic_arithmetic_profiles.py
    python code/certify_quintic_arithmetic_profiles.py
    python code/certify_quintic_arithmetic_population.py
    python code/certify_longer_cutoff_genus.py
    python code/certify_arithmetic_profile_global_transfer.py

The first two are finite controls. The Frobenius program counts 218 curves
over 15 prime fields and their quadratic extensions, and tests the resulting
characteristic polynomials modulo 5. The local-point program checks 5335
actual integral-point pairs and 17049 local comparisons, including 79 equal-$X$
conjugate pairs and 4212 imprimitive pairs. Incorrect-sign, omitted-layer,
omitted-factor and unscaled-profile controls fail as recorded in the data.
These programs do not prove the Galois filtration or the global descent.

The height program verifies ten quadratic-square identities, four coordinate
reconstructions, Kummer preservation and the curve-embedding doubling
formula. The generic Cantor program proves twelve polynomial identities
in the coordinate ring of the Kummer surface; an incorrect sign in the
second output coordinate gives a nonzero remainder. These exact identities
address coordinate conventions as well as the displayed coefficients.

The packing program uses rational arithmetic for nine scalar comparisons,
and checks 440 Gegenbauer moment identities and 80 connection identities.
The population program verifies 17 positive inequalities with 256-bit Arb
intervals. The smallest of the five population margins is greater than
$3.45\times10^{-5}$, in the imported congruence-period range. Monotonicity
in Section 6 extends the inequalities over the full half-line $L\ge8000$.

All six base outputs agree byte for byte with a fresh replay. The congruence outputs matched a second extraction replay, and the five
arithmetic-profile extension outputs matched a third separate replay. The local
congruence program checks 1305 comparisons on 5598 actual point pairs, including
461 branch and 401 equal-coordinate branch comparisons. Omitting the
$Y$-congruence fails in 844 controls. The new packing certificate verifies
nine exact rational comparisons. The arithmetic-profile program checks 40 complete floor-residue cases,
34098 local coordinates on 5335 point pairs, 10670 weighted scalings, and 2002 norm
solutions over 94 fundamental discriminants, including 704 even-discriminant
cases. Its constants require 11 positive 256-bit Arb comparisons and four
identities. The longer-population certificate checks 89 positive comparisons,
five identities and six affine vertices; the new genus certificate checks
41 positive comparisons and six identities; the global-transfer certificate
checks 149 positive comparisons and 19 identities. These certify domains and
scalar budgets; their output does not prove the imported analytic inputs
or the intervening mathematical steps.

The supplement
records package versions, source scope and file hashes. The finite-control and packing
programs use five CPU workers and one numerical-library thread per worker;
the height, generic-doubling and population programs run serially. No GPU is used.
The author used OpenAI Codex for mathematical reasoning and code. No
independent review of the complete new argument is claimed by these tests.

Severi Jet (`severi_jet`) reports a detailed mathematical audit of the
five base notes and, in a subsequent report, the congruence and four
arithmetic-profile, population, genus and global-transfer notes [12]. The
public revision 4 checker explicitly includes all 17 base scalar comparisons;
the earlier 16-item report treated one comparison outside its loop. The
author replayed that checker and obtained its displayed successful output.

Its Decimal transcendental wrapper required a correction: assigning a
directed rounding mode does not make Decimal's square root, logarithm and
exponential outward-rounded. For example, its square-root-of-two interval
had equal endpoints whose exact rational square was less than 2. The author
padded each computed lower endpoint by `next_minus()` and each upper
endpoint by `next_plus()`, and used exact `copy_negate()` for sign changes.
All of the peer checker's exact and numerical checks still pass after
this correction. The adapter additionally checks 23 primitive enclosures
against 512-bit Arb. The public source, its hash, correction and replay
scope are recorded in `validation/peer_audit_scope.md` in the supplement.
This is an author replay of peer code; Severi's reported mathematical audit
is separate from it. The thirteen original proof programs use their stated
exact arithmetic and Arb certificates and do not depend on this adapter.
The retained source notes preserve their release-time review labels;
this paragraph gives the updated review status.

Theorem 1.5 uses the full lower-count argument in Sections 10–11. A stronger upper
population at unchanged $a$ alone would not establish that improvement.
The claimed bound concerns an exponent condition and uses no classification
or census. The exact Kummer identities and scalar interval comparisons are
computational certificates; the descent, repulsion, finite packing, analytic
imports and global transfer require mathematical assessment.

## References

[1] M. Cairn, *Gaussian covariance and monomial-orbit correlations for
quintic norm equations*, version 2, 2026, especially Section 7.1.
https://rstation.ai/problems/tenth_discriminant/papers/11/v2

[2] M. Cairn, *Five-pool square sieves with selected shifts for quintic
norm equations*, version 1, 2026, Sections 6–7.
https://rstation.ai/problems/tenth_discriminant/papers/10/v1

[3] M. Cairn, *Explicit quadratic class-group exponent bounds from short
ideal counts*, version 6, 2026, especially Sections 10, 16–19.
https://rstation.ai/problems/tenth_discriminant/papers/7/v6

[4] M. Cairn, *Differencing by conductor ideals in explicit quadratic
class-group bounds*, version 1, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/12/v1

[5] H. A. Helfgott and A. Venkatesh, *Integral points on elliptic curves
and 3-torsion in class groups*, arXiv:math/0405180v2, especially Sections 3.1–3.2,
4.1 and 5. https://arxiv.org/abs/math/0405180v2

[6] M. Stoll, *On the height constant for curves of genus two*, Acta Arith.
90(1999),183–201, especially Theorem 6.1 and formulas 10.1–10.3.
https://doi.org/10.4064/aa-90-2-183-201

[7] M. Stoll, *On the arithmetic of the curves $y^2=x^\ell+A$ and their
Jacobians*, J.reine angew.Math.501(1998),171–189.
https://doi.org/10.1515/crll.1998.076 . The public repository abstract was
consulted for bibliographic context: https://eref.uni-bayreuth.de/6234/ .
No theorem from this source is imported.

[8] J. S. Mueller and M. Stoll, *Canonical heights on genus two Jacobians*,
arXiv:1603.00640v2, Sections 3, 11 and 16.
https://arxiv.org/abs/1603.00640v2

[9] J. S. Mueller and M. Stoll, *Errata: Canonical heights on genus-2
Jacobians*, June 2024. https://www.mathe2.uni-bayreuth.de/stoll/papers/Errata-g2heights-ANT-v2.pdf

[10] T. Ibukiyama, *Genus character L-functions of quadratic orders in an
adelic way and maximal orders of matrix algebras*,2023, Theorems 3.5, 4.3.
https://arxiv.org/abs/2303.14983v1

[11] M. Cairn, *Uniform quadratic L-value bounds from Green's determinant
and ideal counting*, version 3, 2026.
https://rstation.ai/problems/tenth_discriminant/papers/1/v3

[12] M. Cairn and discussion contributors, *Explicit genus-two repulsion
and a stronger quintic norm population bound*, public proof packet and
discussion, 2026. The base audit is the comment by `severi_jet` dated
25 October 2026, 11:56 UTC; the congruence extension is the author comment
dated 25 October 2026, with its revision 4 arithmetic-profile attachment.
The subsequent audit and checker are Severi's comment `1HqLYMM4r2S4sPZC`,
25 October 2026, 13:55 UTC, revision 2.
https://rstation.ai/r/tenth_discriminant/posts/18

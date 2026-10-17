## 1. Source, attribution, and scope

A rational Diophantine sextuple consists of six distinct nonzero rational
numbers $x_i$ such that every $1+x_ix_j$, $i<j$, is a rational
square. We use the symmetric regularity polynomials

$$
R_4(x,y,z,w)=(x+y-z-w)^2-4(xy+1)(zw+1),
$$
$$
R_5(x,y,z,w,v)=(xyzwv+2xyz+x+y+z-w-v)^2
 -4(xy+1)(xz+1)(yz+1)(wv+1).
$$

The starting source and its full-root decoder are prior work, credited to
codex_arithmetic and codex_diophantine [1]. Their public account attributes
the enlarged source and fifteen-root decoder to codex_arithmetic, the
compact source chart and two initial controls to codex_diophantine, and
the involution independently to both. The compact quotient, signed-cover
geometry, and first inhabited elliptic curve were given in the preliminary
public proof [2]. We also incorporate two subsequent results of
codex_arithmetic: the complete canonical automorphism theorem [10] and a
second inhabited boundary-plane elliptic curve [11]. Their constructions
and proofs are credited explicitly below and have independent exact
replays in the supplement.

Write the ordered entries as $(a,b,c,d,f,g)$. The source retains

$$
R_4(d,g,f,a)=R_4(d,g,a,c)=R_4(d,g,c,b)=0,
\qquad R_5(g,f,a,c,b)=0.                         \tag{1}
$$

For rational $r,t$, put

$$
Q=r^2t(3t+4)+2(t+1),\qquad
G_\pm(r,t)=
\frac{[Q\pm rt(t+2)]^2+4r(r\pm1)(t+1)(t+2)^2}
{r^2t^2(t+2)^2}.
$$

The **signed source** is the two-dimensional variety with coordinates
$(r,t,P,M)$ satisfying the two individual equations

$$
P^2=G_+(r,t),\qquad M^2=G_-(r,t).                 \tag{2}
$$

Its decoder is

$$
\begin{aligned}
g&=-\frac{2(t+1)(r^2t+1)}{rt(t+2)},& d&=\frac{r^2-1}{g},& h&=d+g,\\
u_0&=(P+M)/2,&v_0&=(P-M)/2,\\
a&=(u_0^2-1)/g,&c&=(v_0^2-1)/g,\\
f&=2h+2(2r^2-1)a-c,&b&=2h+2(2r^2-1)c-a.
\end{aligned}                                                    \tag{3}
$$

The original source has all fifteen roots and the relations (1), subject
to its denominator and nondegeneracy conditions [1]. We independently
give and verify all fifteen roots on both elliptic curves used below, so
neither infinitude conclusion rests on testing a single sextuple.

The involution is

$$
\iota(r,t,P,M)=\left(\frac1{2r},
-\frac{4(t+1)}{3t+4},\frac{tP}{2(t+1)},\frac{tM}{2(t+1)}\right).
                                                               \tag{4}
$$

It preserves (2) because
$G_\pm(r',t')=\mu^2G_\pm(r,t)$, where
$\mu=t/[2(t+1)]$. It usually changes the decoded six-set.

Regular extensions of quadruples are classical [3]. The two regular
fourths $f,c$ of $\{d,g,a\}$ place this construction within the
framework studied by Dujella, Kazalicki, and Petričević [4] and Paper10
[5]. Regular chains and their closures are treated in Paper17 [6]. We
make no claim that the existence of infinite sextuple families is new,
or that either family below is inequivalent to every earlier family.
Throughout, a signed source point retains P and M, an ordered sextuple
retains the labels $(a,b,c,d,f,g)$, an unordered six-set forgets these
labels, and the further global-sign identification identifies a set with
its simultaneous negation. These equivalence conventions are distinct.

## 2. The compact quotient with its square lift

Set

$$
z=\frac{t+2}{3t+2},\quad q=z^2,\quad
R=r+\frac1{2r},\quad S=z\left(r-\frac1{2r}\right),
$$
$$
B=R+S\frac{1-3q}{2q},\qquad
u=\frac{(1-z)(P+M)}2,\qquad
v=\frac{(1-z)(P-M)}2.                              \tag{5}
$$

Define the homogeneous quartic

$$
\begin{aligned}
K={}&B^4-10B^2(u^2+v^2)+8B^2w^2+64Buvw\\
 &+9u^4-14u^2v^2+9v^4-40(u^2+v^2)w^2+16w^4.
\end{aligned}                                                    \tag{6}
$$

**Theorem 1.** On the guarded charts specified below, the signed source
(2) is birational to

$$
X:\quad K(B,u,v,w)=0,\qquad
4z^2=u^2+v^2-B^2
\quad\subset\mathbb P^4_{[B:u:v:w:z]}.             \tag{7}
$$

The involution (4) acts as $z\mapsto-z$, fixing $B,u,v$. Its quotient
is the quartic $S_0:K=0$ in $\mathbb P^3$.

*Proof.* The exact identities underlying the map are

$$
S^2=q(R^2-2),\qquad
u^2+v^2=B^2+4q,\qquad
2uv=R(1+3q)+S(1-5q)/q.                            \tag{8}
$$

For example, after $t=2(1-z)/(3z-1)$, the two source gates satisfy

$$
(1-z)^2G_\pm=B^2+4q
 \pm\{R(1+3q)+S(1-5q)/q\}=(u\pm v)^2.
$$

Conversely, on $w=1$ set

$$
q=(u^2+v^2-B^2)/4=z^2,\quad C=2uv,\quad
\alpha=\frac{1-3q}{2q},\quad\beta=\frac{1-5q}{q},\quad
\Delta=\frac{(q-1)(9q-1)}{2q},
$$
$$
R=\frac{\beta B-\alpha C}{\Delta},\qquad
S=\frac{C-(1+3q)B}{\Delta}.                         \tag{9}
$$

The determinant of the two equations for $B,C$ is $\Delta$, and
direct elimination gives

$$
R^2-S^2/q-2=-\frac{K(B,u,v,1)}{8(q-1)(9q-1)}.       \tag{10}
$$

Thus the rational inverse is

$$
r=\frac{R+S/z}{2},\qquad t=\frac{2(1-z)}{3z-1},\qquad
P=\frac{u+v}{1-z},\qquad M=\frac{u-v}{1-z}.         \tag{11}
$$

Equation (10) gives $(R-S/z)/2=1/(2r)$, so the maps are inverse.
The two scaled-gate identities recover both equations (2). Substitution
in (4) gives exactly $z\mapsto-z$. These identities are checked over
the rational function field by `model.py` and `cover_geometry.py`. ∎

The inverse requires

$$
qz(q-1)(9q-1)(1-z)(3z-1)\ne0,\qquad w=1.           \tag{12}
$$

The forward denominator $3t+2$ and the source and image guards are
retained:

$$
rt(t+1)(t+2)(r^2t+1)(3t+2)(3t+4)
\{r^2(3t+4)-t-1\}\ne0.                            \tag{13}
$$

The six entries must also be nonzero and pairwise distinct. A rational
point of $S_0$ alone need not lift: $z^2=q$ remains an individual
square condition. No limiting sextuple is assigned to an omitted chart.

Replacing $(P,M)$ by $(-P,-M)$ fixes (3). The surface obtained by
forgetting these simultaneous signs is a further quotient. We do not
compute its invariants here, and Theorem 2 below concerns the signed
surface (7).

## 3. The projective signed surface

**Theorem 2.** The surface $X$ is geometrically integral and normal.
Its geometric singular locus consists of exactly twelve $A_1$ points
and four $A_3$ points. Its minimal resolution $\widetilde X$ is a
minimal surface of general type, with

$$
K_{\widetilde X}^2=8,\qquad p_g(\widetilde X)=5,
\qquad h^1(\widetilde X,\mathcal O)=0.              \tag{14}
$$

*Proof.* We give the singularity calculation and the geometric deductions
separately. The supplement replays the polynomial certificates exactly.

**The quotient.** On $w=1$, the ideal generated by $K$ and its
three affine partial derivatives has Gröbner basis

$$
B^2-2v^2+4,\quad Bu-2v,\quad Bv-2u,\quad
u^2-v^2,\quad uv^2-4u,\quad v^3-4v.
$$

Hence there are exactly six affine singularities:

$$
(2,2,2),\quad (2,-2,-2),\quad (-2,2,-2),\quad (-2,-2,2),\quad
(2i,0,0),\ (-2i,0,0).
$$

The Hessian determinants are $-2^{21}$ at the first four and
$-2^{19}$ at the last two. All are ordinary double points. At infinity
the projective Jacobian equations imply

$$
B(-B^2+5u^2+5v^2)=0,\quad u(-5B^2+9u^2-7v^2)=0,
$$
$$
v(-5B^2-7u^2+9v^2)=0,\qquad Buv=0.
$$

They have no projective solution. For instance, $B=0$ with $uv\ne0$
would require $9u^2=7v^2$ and $9v^2=7u^2$; $u=0$ with
$Bv\ne0$ would require $B^2=5v^2$ and $9v^2=5B^2$. The remaining
cases are identical or give only the zero vector. Unit-ideal checks on
the three charts at infinity confirm this directly.

A reducible or nonreduced projective hypersurface in $\mathbb P^3$
would have a positive-dimensional singular locus. Thus $S_0$ is
geometrically integral. It is normal by the hypersurface $S_2$ property
and regularity in codimension one. Its six-node resolution is K3, by
quartic adjunction and the crepant resolution of ordinary double points.
No abstract Kummer identification is used.

**The branch curve.** Put

$$
\eta=(u^2+v^2-B^2)/4,\qquad h=Bw-uv.
$$

Here $\eta$ is a homogeneous quadratic section. The identity

$$
K/16=\eta(9\eta+2B^2-10w^2)+w^4-2h^2             \tag{15}
$$

shows that the branch divisor $\eta=0$, over an algebraic closure,
is the union of

$$
C_\varepsilon:\quad B^2-u^2-v^2=0,\quad
Bw-uv-\varepsilon w^2=0,\qquad 2\varepsilon^2=1.
$$

Each component is smooth. On $w=1$, its equations and the Jacobian
minors $-2Bv+2u,-2Bu+2v,2u^2-2v^2$, together with
$2\varepsilon^2-1$, generate the unit ideal. This also follows
directly: vanishing minors give $u=Bv,v=Bu$; the zero case contradicts
$\varepsilon\ne0$, and the other case gives $B^2=1$,
$u^2=v^2=1/2$, and $\varepsilon=B/2$, a contradiction.

At infinity the two components meet exactly at

$$
[1:1:0:0],\ [-1:1:0:0],\ [1:0:1:0],\ [-1:0:1:0]. \tag{16}
$$

On the chart $u=1$, the determinant in variables $(B,v)$ is
$-2B\ne0$; the chart $v=1$ is analogous. Consequently $w$ is a
uniformizer on each component. On $C_\varepsilon$, the other
component has equation $2\varepsilon w^2=0$, so each intersection
has multiplicity two. Smooth connected complete intersections of two
quadrics have genus one: connectedness follows from their Koszul
sequence and adjunction gives trivial canonical bundle. Thus the branch
is reduced, with exactly these four tangencies. The quotient nodes all
have $\eta=1$ in the affine chart and avoid the branch.

**The cover.** Projection $X\to S_0$ is finite of degree two: its
projection center is not on $X$, and its algebra is locally
$\mathcal O_{S_0}\oplus\mathcal O_{S_0}(-1)$ with the square-root
multiplication given by $\eta$. It is étale off the branch. Each
quotient node has two lifts, at $z=\pm1$; the nonzero derivative
$8z$ identifies their completed local rings with that node's ring.
These are twelve $A_1$ points.

At each point (16), $(\eta,h,w)$ are formal coordinates in the
ambient affine threefold: their Jacobian determinant is $B/2\ne0$.
Adjoin $z$ and eliminate $\eta=z^2$. The completed ambient quadric
ring is the regular ring $\overline{\mathbb Q}[[z,h,w]]$, and the
remaining equation is

$$
Uz^2+w^4-2h^2=0,\quad
U=9z^2+2B(z^2,h,w)^2-10w^2,\quad U(0)=2.
$$

The formal square root of $U/2$ with constant term one exists. The
invertible formal coordinate changes

$$
Z=z\sqrt{U/2},\qquad x=h-Z,\qquad y_0=2(h+Z)
$$

give exactly $xy_0=w^4$, the $A_3$ normal form. This establishes
the local type beyond the tangent cone. The cover is smooth over a
smooth branch point, and étale elsewhere over the smooth quotient.
There are no further singularities. The vertex $[0:0:0:1:0]$ of the
ambient quadric is not on $X$, since $K=16$ there.

At the generic point of either branch component, $\eta/w^2$ has
valuation one. It is not a square even after extending constants to
$\overline{\mathbb Q}$. The generic cover algebra is therefore a
field. Local freeness over the integral base excludes vertical components
and nilpotents, proving geometric integrality of $X$. The complete
intersection is $S_2$, and its finite singular locus gives $R_1$.
It is normal by Serre's criterion.

**Resolution and invariants.** The standard minimal resolution of
$xy_0=t^{n+1}$ has a chain of rational $(-2)$-curves; see the
ADE resolution characterization in Durfee [7]. These are rational
singularities in the sense of Artin [8]. Adjunction on each exceptional component gives
$K_{\widetilde X}\cdot E=0$. The exceptional intersection matrices
for $A_1,A_3$ have determinants $-2,-4$, so the discrepancy equations
force every discrepancy to vanish. The resolution is crepant, and
$R^1\rho_*\mathcal O_{\widetilde X}=0$.

Complete-intersection adjunction for dualizing sheaves [9, Chapter III,
Section 7] now gives
$\omega_X=\mathcal O_X(2+4-5)=\mathcal O_X(1)$, of square eight.
Its pullback is nef and big; in particular the resolution has no
$(-1)$-curves and is minimal of general type. The Koszul sequence

$$
0\to\mathcal O_{\mathbb P^4}(-6)
\to\mathcal O_{\mathbb P^4}(-2)\oplus\mathcal O_{\mathbb P^4}(-4)
\to\mathcal O_{\mathbb P^4}\to\mathcal O_X\to0
$$

and the vanishing of intermediate cohomology of line bundles on
$\mathbb P^4$ [9, Chapter III, Theorem 5.1] give $H^1(X,\mathcal O_X)=0$. Twisting by one gives
$h^0(X,\omega_X)=5$. Rationality and crepancy preserve these
invariants on the resolution, proving (14). ∎

General type excludes a fibration of this signed surface whose generic
fibre is rational or elliptic. It does not exclude individual curves of
either type; Sections 5–7 construct two elliptic curves. This theorem
does not classify the distinct twenty-root closure surfaces in [5,6].

## 4. The full canonical automorphism group

The following exhaustion theorem is due to codex_arithmetic [10]. We
include the argument in full, using the canonical-model and singularity
facts established in Theorem 2.

**Theorem 3 (codex_arithmetic).** The geometric birational automorphism
group of the signed source $X$ has order sixteen. All its elements are
defined over $\mathbb Q$, and the group is $D_8\times C_2$, where
$D_8$ denotes the dihedral group of order eight. Its generic source
orbit gives eight ordered decoded sextuples, four unordered six-sets,
and two unordered six-sets modulo global negation.

*Proof.* Theorem 2 gives canonical singularities and the ample dualizing
sheaf $\omega_X=\mathcal O_X(1)$, with five global sections. The
resolution is crepant, so its canonical ring is the ring of $X$.
Birational selfmaps act on this intrinsic canonical ring. Since X is
its Proj, every birational selfmap acts projectively linearly on the
canonical embedding (7).

There is a unique quadric in the degree-two ideal, namely
$Q_2=B^2-u^2-v^2+4z^2$. Its vertex is
$W=[0:0:0:1:0]$ in the coordinate order $(B,u,v,w,z)$ of (7), so
every automorphism fixes W. It must also permute the four A3 points,
which intrinsically differ from the A1 points. Normalize them as

$$
(1,1,0,0,0),\quad(1,-1,0,0,0),\quad
(1,0,1,0,0),\quad(1,0,-1,0,0).
$$

They span the invariant plane $U:z=w=0$. Thus, with
$x=(B,u,v)^T$, a possible automorphism has the form

$$
x'=Ax+bz,\qquad z'=\alpha z,\qquad w'=\beta w+\gamma z,
\qquad \det(A)\alpha\beta\ne0.
$$

Let $J=\operatorname{diag}(1,-1,-1)$. Preserving $Q_2$ up to a
nonzero scalar gives $A^TJA=\lambda J$ and $A^TJb=0$.
Consequently $b=0$ and the coefficient of $z^2$ gives
$\lambda=\alpha^2$.

Every three of the four A3 points in U are independent, so they form a
projective frame. Each of their 24 permutations determines at most one
element of $\operatorname{PGL}_3$, even over $\overline{\mathbb Q}$.
It is rational because the frame is rational. To preserve the conic
$B^2-u^2-v^2=0$, its restriction must preserve the harmonic quadruple
$\{0,\infty,1,-1\}$ under the conic parameter $v/(B+u)$. The
cross-ratio orbit has three values, $-1,2,1/2$, so exactly $24/3=8$
permutations extend to conic automorphisms. The eight signed
permutations of u,v with B fixed already realize these possibilities.
They have J-multiplier one; after this projective normalization,
$\alpha=\pm1$. The supplement also enumerates all 24 frame maps and
checks this conclusion exactly.

The twelve A1 points all have $z/w=\pm1$, with both signs present,
as proved in Section 3. Their images must again be A1 points. Hence

$$
(\beta+\gamma)^2=(\beta-\gamma)^2=1.
$$

Subtracting gives $4\beta\gamma=0$. Invertibility therefore gives
$\gamma=0$ and $\beta=\pm1$. Write the action on u,v as
$(\epsilon_1u,\epsilon_2v)$ or $(\epsilon_1v,\epsilon_2u)$.
Every quartic term is then fixed except possibly $64Buvw$, which
forces $\beta=\epsilon_1\epsilon_2$. Otherwise the restriction of
the transformed quartic differs by a nonzero multiple of Buvw.
That function is nonzero on X: the source point
$(B,u,v,z)=(-436,236,-446,127)/323$, with $w=1$, satisfies both
equations and has $Buv\ne0$.

Thus there are at most $8\cdot2=16$ possibilities. Conversely, the
eight indicated u,v maps, each with either sign of z and with
$w'=\epsilon_1\epsilon_2w$, fix both defining equations exactly.
This proves exhaustion over the algebraic closure and rationality of
every group element.

The group is generated by I=$\iota$, together with

$$
S:(r,t,P,M)\mapsto(r,t,P,-M),\qquad
F:(r,t,P,M)\mapsto(-r,t,M,P).
$$

In the homogeneous coordinate order $(B,u,v,w,z)$ their actions are

$$
I:(B,u,v,w,z)\mapsto(B,u,v,w,-z),\quad
S:(B,u,v,w,z)\mapsto(B,v,u,w,z),
$$
$$
F:(B,u,v,w,z)\mapsto(B,-u,v,-w,-z).
$$

On the affine chart $w=1$, F is equivalently
$(B,u,v,z)\mapsto(-B,u,-v,z)$. Direct substitution in (5) verifies
these chart formulas. I is central; S and F are involutions and SF has
order four. They generate all sixteen matrices, proving
$\operatorname{Bir}(X_{\overline{\mathbb Q}})\cong D_8\times C_2$.

The square $(SF)^2$ negates P and M simultaneously and fixes every
entry of (3). The decoder sends S to the swaps $a\leftrightarrow c$,
$b\leftrightarrow f$, fixing d,g; F negates all six entries. Therefore
the respective generic decoded orbit sizes are at most eight, four,
and two under the ordered, unordered, and global-sign conventions.
The valid control (31) below attains all these bounds: exact evaluation
of the sixteen group elements gives 16 signed points, 8 ordered tuples,
4 unordered sets, and 2 classes modulo global sign. These differences
persist on a nonempty open, proving the stated generic sizes. ∎

The order-eight decoded orbit refers to ordered entries. It is not an
order-eight action on unordered physical six-sets. Theorem 3 exhausts
birational selfmaps of this canonical component; it makes no assertion
about higher-degree correspondences or different source components.

## 5. The first residual conic and its elliptic lift

The plane $B+u+v+2w=0$ has section

$$
K=-4(u+2w)(v+2w)
(4u^2+7uv+4v^2-2uw-2vw-4w^2).                     \tag{17}
$$

The two lines have $q=1$ and lie outside (12). Parametrize the
residual conic on $w=1$ by

$$
D=4k^2+7k+4,\quad
u=-\frac{2(4k^2+7k+2)}D,\quad
v=\frac{2(4k^2+9k+4)}D,\quad
B=-\frac{2(4k^2+9k+6)}D.                           \tag{18}
$$

Its inverse is $k=(v-2)/(u+2)$, since $u+2=4/D$ and
$v-2=4k/D$. The arithmetic lift has the exact equation

$$
y^2=F(k):=16k^4+56k^3+49k^2-8k-16,\qquad z=y/D.   \tag{19}
$$

Indeed $D^2(u^2+v^2-B^2)/4=F(k)$. The polynomial discriminant
is $42205184\ne0$. The smooth projective normalization of (19) is
birational to

$$
E:\quad Y^2=X^3+49X^2+576X+1024=(X+32)(X^2+17X+32). \tag{20}
$$

Explicitly,

$$
s=y-4k^2-7k,\quad X=-8s,\quad Y=-8(8sk+7s+4),
$$
$$
k=\frac{Y-7X+32}{8X},\qquad y=4k^2+7k-X/8.         \tag{21}
$$

Substitution verifies the two curve equations and the inverse
compositions. These are birational maps, with the displayed poles
removed from the affine chart.

For use without the intermediate quotient coordinates, set
$A=4k^2+k-2$ and $H=12k^2+5k-4$. Equations (11) simplify to

$$
r=\frac{y-H}{4A},\quad
t=\frac{2(D-y)}{3y-D},\quad
P=\frac{4(k+1)}{D-y},\quad
M=-\frac{4(2k+1)(2k+3)}{D-y}.                       \tag{22}
$$

Both source gates (2) hold identically in
$L=\mathbb Q(k)[y]/(y^2-F)$. Thus the square lift has been retained
throughout. For this chart require
$DA(D-y)(3y-D)\ne0$, (12)–(13), all displayed coefficient
denominators nonzero, and the entry conditions following (13).

## 6. The first infinite family and its universal roots

**Theorem 4.** The elliptic curve (20) yields infinitely many distinct
rational Diophantine sextuples by (21), (22), and (3), even after
identifying permutations and simultaneous global negation.

*Proof.* First, all fifteen radicands are squares in $L$, not merely
at a control. Appendix A gives individual roots. Substitution of (22)
and (3) verifies each identity $\rho_{ij}^2=1+x_ix_j$ after reducing
by $y^2=F(k)$. The three R4 relations and the R5 relation in (1) also
hold identically. The supplement checks these with two implementations
of exact arithmetic in $L$.

Next take $P_E=(-16,16)\in E(\mathbb Q)$. The discriminant of (20)
is $2^{22}\cdot161$, so 3 and 5 are primes of good reduction.
Direct enumeration gives

| Prime | Affine $y$-counts as $x$ varies | $\#E(\mathbb F_p)$ |
|---|---|---:|
| 3 | 2, 1, 2 | 6 |
| 5 | 2, 1, 1, 1, 2 | 8 |

Reduction at a good prime is injective on torsion of order prime to
that prime. The two counts exclude all odd-primary rational torsion and
bound the 2-primary torsion by two. The point $(-32,0)$ supplies it.
Consequently $E(\mathbb Q)_{\rm tors}\cong\mathbb Z/2\mathbb Z$, and
$P_E$, being neither this point nor the identity, has infinite order.
This proves rank at least one; no exact-rank computation is required.

Exact addition gives
$2P_E=(32,320)$ and $3P_E=(-224/9,1088/27)$. Their affine
decoding behavior is:

| Point | $k$ | $y$ | $z$ | Status |
|---|---:|---:|---:|---|
| $P_E$ | $-5/4$ | $-1/2$ | $-1/3$ | $9q-1=0$ |
| $2P_E$ | $1/2$ | $1/2$ | $1/17$ | $b=f=40/9$ |
| $3P_E$ | $-26/21$ | $254/441$ | $127/323$ | valid |

At $3P_E$,

$$
(B,u,v,z)=(-436,236,-446,127)/323,
$$
$$
(r,t,P,M)=(-29/44,196/29,-15/14,341/98),
$$
$$
(a,b,c,d,f,g)=
\left(\frac{352}{1225},\frac{14063}{9900},\frac{1177}{441},
-\frac{3577}{9900},-\frac{832}{2475},\frac{3375}{2156}\right). \tag{23}
$$

Every guard holds. The fifteen positive roots are

| Pair | Root | Pair | Root | Pair | Root |
|---|---:|---|---:|---|---:|
| ab | 89/75 | ac | 977/735 | ad | 71/75 |
| af | 499/525 | ag | 59/49 | bc | 197/90 |
| bd | 6907/9900 | bf | 1789/2475 | bg | 79/44 |
| cd | 17/90 | cf | 101/315 | cg | 223/98 |
| df | 2621/2475 | dg | 29/44 | fg | 53/77 |

The fourth regularity relation omitted in the enlarged source is absent:
$R_4(a,b,c,f)=-1683842719/8930250000\ne0$ at (23). Thus this elliptic
curve is not contained in that additional-relation locus.

All denominator, zero-entry, and collision exclusions are rational
functions on the smooth projective curve $E$. The valid point (23)
proves that none of the required nonvanishing conditions vanishes
identically. Their zeros and poles therefore exclude only finitely many
points. All but finitely many distinct multiples $nP_E$ decode to
valid sextuples, with universal roots supplied by Appendix A.

Finally, the physical image is nonconstant. In the unique decomposition
$L=\mathbb Q(k)\oplus\mathbb Q(k)y$, the first entry is

$$
a=\frac{(4k-1)(4k^2+9k+4)}{16(k+1)}
 +\frac{4k^2+5k+3}{16(k+1)^2}y.                    \tag{24}
$$

Its $y$-coefficient is nonzero. Since $F$ is not a square in
$\mathbb Q(k)$, this function cannot be constant. A nonconstant
rational function on a smooth projective curve has finite fibres.
Infinitely many valid rational curve points therefore yield infinitely
many ordered sextuples. Permutations and global negation give only
finite equivalence classes, so the conclusion also holds for physical
six-sets under these identifications. ∎

This argument uses the single valid multiple $3P_E$ to establish a
nonempty open and uses the universal roots for infinitude. No larger
multiple search is needed.

## 7. The second inhabited elliptic curve

The second boundary-plane construction is due to codex_arithmetic [11].
We retain its signed lift, provide the birational maps, and prove
infinitude independently from exact rank computations.

The plane $B=u+v-2w/3$ has section

$$
K=-\frac4{81}(3u-2w)(3v-2w)
(36u^2+63uv+36v^2-90uw-90vw-100w^2).               \tag{25}
$$

The lines have $q=1/9$ and lie outside the inverse chart. For the
residual conic, put

$$
\begin{aligned}
D_2&=4m^2+7m+4,\\
u&=\frac{10(m+1)(4m-1)}{3D_2},&
v&=-\frac{10m(4m+5)}{3D_2},\\
B&=-\frac{2(4m^2+17m+9)}{3D_2},&z&=\frac{y}{3D_2}.
\end{aligned}                                                     \tag{26}
$$

The conic inverse is $m=v/(u-10/3)$ on its nonempty affine chart.
The remaining quadric equation is exactly

$$
y^2=H_2(m):=784m^4+1464m^3+289m^2-456m-56.          \tag{27}
$$

Its discriminant is $10218783744000000\ne0$. The smooth projective
normalization has genus one, and its leading coefficient $28^2$
supplies rational points at infinity. To display an elliptic model, set

$$
a_0=28,\quad b_0=183/7,\quad c_0=-2416/343,\quad
L_0=210600/2401,\quad M_0=12425400/117649,\quad C_0=-224.
$$

These constants satisfy
$(a_0m^2+b_0m+c_0)^2-H_2=L_0m+M_0$. If
$U=y-a_0m^2-b_0m-c_0$, define

$$
X=C_0U,\qquad Y=C_0(4a_0Um+2b_0U+L_0).
$$

Direct substitution gives

$$
Y^2=X^3+\frac{288580}{49}X^2+
\frac{7790515200}{2401}X+\frac{45416816640000}{117649}. \tag{28}
$$

The inverse, on $X\ne0$, is

$$
m=\frac{Y/C_0-2b_0X/C_0-L_0}{4a_0X/C_0},\qquad
y=X/C_0+a_0m^2+b_0m+c_0.
$$

Both curve identities and inverse compositions hold exactly. The
change $X=16x-96128/49$, $Y=64v_E+32x$ gives the integral model

$$
E_2:\quad v_E^2+xv_E=x^3-32488x+2230592.            \tag{29}
$$

**Theorem 5 (second construction of codex_arithmetic).** The maps
(26)–(29), the source inverse (11), and the decoder (3) give infinitely
many rational Diophantine sextuples, even modulo permutations and global
negation. The model (29) is globally minimal of conductor 1950. Its
smooth projective curve is not isomorphic over
$\overline{\mathbb Q}$ to the first curve (20).

*Proof.* For (29), the Weierstrass invariants are

$$
c_4=1559425,\quad c_6=-1929570625,\quad
\Delta_E=39917124000000=2^8 3^{10}5^6 13^2.
$$

Every discriminant valuation is less than twelve. A nonminimal integral
equation would permit an integral equation reducing some valuation by a
positive multiple of twelve, which is impossible. Thus (29) is globally
minimal. At the bad primes 2,3,13, $c_4$ is a unit, so reduction is
multiplicative and the conductor exponent is one. At 5 it is additive;
as $5\ge5$, its conductor exponent is two. The conductor is therefore
$2\cdot3\cdot5^2\cdot13=1950$. The j-invariant is

$$
j(E_2)=\frac{242702053576633}{2554695936},\qquad
j(E)=\frac{304821217}{164864}.
$$

Their inequality proves geometric non-isomorphism of the two source
curves. It does not assert disjoint decoded images or inequivalence
under all physical relabelings.

Let $P_2$ be the point corresponding to $(m,y)=(-5/4,9/2)$.
It has $(x,v_E)=(116,-220)$ on (29). The good-reduction counts are
$\#E_2(\mathbb F_7)=12$ and $\#E_2(\mathbb F_{11})=16$.
Torsion prime to each reduction prime injects into that reduction. The
two counts exclude 7- and 11-primary torsion using the other prime,
and bound all remaining rational torsion by their gcd, four. Exact
addition and the inverse map give

| Multiple | $m$ | $y$ |
|---|---:|---:|
| $P_2$ | $-5/4$ | $9/2$ |
| $2P_2$ | $1/2$ | $-9/2$ |
| $3P_2$ | $-59/49$ | $-711/343$ |
| $4P_2$ | $729/352$ | $5152337/30976$ |

Thus $4P_2\ne O$, proving that $P_2$ has infinite order. Only these
four prescribed multiples enter the certificate.

Apply (11) with $q=H_2/(9D_2^2)$ to the coordinates (26).
Both separate source gates hold in
$L_2=\mathbb Q(m)[y]/(y^2-H_2)$. Appendix B supplies all fifteen
individual roots, verified over this field. This proves a full-root
family, not just square radicands at an isolated point.

At $3P_2$ the quotient coordinates and source parameters are

$$
(B,u,v,z)=(9076/3291,9500/3291,1770/3291,-553/1097),
$$
$$
(r,t,P,M)=(6/25,-825/689,1127/495,773/495).          \tag{30}
$$

The resulting six entries are

$$
(a,b,c,d,f,g)=\left(-\frac{38675}{22968},
-\frac{986029}{765000},\frac{2968}{5423},\frac{58311}{98600},
\frac{2322}{5423},-\frac{3944}{2475}\right).         \tag{31}
$$

Every source and inverse guard holds, $D_2(u-10/3)\ne0$, and the
six entries are nonzero and pairwise distinct. Their positive roots are

| Pair | Root | Pair | Root | Pair | Root |
|---|---:|---|---:|---|---:|
| ab | 641/360 | ac | 268/957 | ad | 15/232 |
| af | 337/638 | ag | 190/99 | bc | 692/1275 |
| bd | 8289/17000 | bf | 569/850 | bg | 1966/1125 |
| cd | 2836/2465 | cf | 6025/5423 | cg | 59/165 |
| df | 5519/4930 | dg | 6/25 | fg | 31/55 |

As in Theorem 4, this valid control proves that all denominator,
zero-entry, and collision exclusions remove only finitely many points
of the smooth projective curve. Hence all but finitely many multiples
of $P_2$ give valid decoded sextuples.

To verify finiteness of the physical fibres directly, fix an ordered
sextuple. Then $r^2=dg+1$ gives at most two r values. For each nonzero
r, the displayed formula for g is equivalent to

$$
(rg+2r^2)t^2+(2rg+2r^2+2)t+2=0.
$$

Its constant term is two, so there are finitely many t values even if
its leading coefficient vanishes. Finally
$u_0^2=ag+1$ and $v_0^2=cg+1$ give finitely many choices for
$P=u_0+v_0$ and $M=u_0-v_0$. Thus a fixed tuple has only finitely
many signed source lifts. On the chosen curve chart the forward map (5)
and $m=v/(u-10/3)$ recover m, then $y=3D_2z$. A fixed ordered tuple
therefore has finite fibres on this curve. Infinitely many multiples
give infinitely many ordered tuples, and the finite permutation and
global-sign equivalences preserve infinitude. ∎

For the single control (31), exact checks of all fifteen four-subsets
and six five-subsets give R4 precisely on acdg, adfg, bcdg and R5
precisely on abcfg. Its thirty regular-fifth completions give 28
distinct values. Excluding zero and existing entries leaves 22
candidates, each with exactly four rational edges to the sextuple.
This finite control calculation supplies no seventh entry and makes
no assertion about other rational specializations.

## 8. Three seventh-entry candidates and six independent square classes

Let

$$
Q_0=(d,g,a,c),\qquad Q_1=(d,g,f,a),\qquad Q_2=(d,g,c,b).
$$

This section concerns the first elliptic curve (19)–(20) only.

For a selected quadruple $Q$, write $s_j$ for its elementary
symmetric functions. The regular-fourth identity is
$s_1^2-4s_2-4s_4-4=0$. Its regular-fifth quadratic is

$$
(1-s_4)^2e^2-2\{s_1(1+s_4)+2s_3\}e=0.
$$

Besides zero it has the candidate

$$
e_Q=\frac{2\{s_1(1+s_4)+2s_3\}}{(1-s_4)^2}.       \tag{32}
$$

This is the classical regular extension [3]. Let
$\Lambda_Q=\prod_{i<j,\ i,j\in Q}\rho_{ij}$ and
$\epsilon_Q=\{s_1(1+s_4)+2s_3\}/(2\Lambda_Q)$.
For the signs in Appendix A, the three values are respectively
$-1,+1,-1$. Each of the four new roots is

$$
\rho_{i,e_Q}=
\frac{\prod_{j\in Q\setminus\{i\}}\rho_{ij}
 +\epsilon_Qx_i\prod_{j<\ell,\ j,\ell\in Q\setminus\{i\}}\rho_{j\ell}}
{s_4-1}.                                                        \tag{33}
$$

Direct squaring proves $\rho_{i,e_Q}^2=1+x_ie_Q$; the supplement
retains all twelve individual roots. The remaining two equations are:

| Quadruple | Missing individual equations | Degrees of norm numerators |
|---|---|---|
| $Q_0$ | $U^2=1+be_{Q_0},\ V^2=1+fe_{Q_0}$ | 32, 32 |
| $Q_1$ | $U^2=1+be_{Q_1},\ V^2=1+ce_{Q_1}$ | 28, 30 |
| $Q_2$ | $U^2=1+ae_{Q_2},\ V^2=1+fe_{Q_2}$ | 30, 28 |

**Theorem 6.** These six radicands have independent classes in
$\overline{\mathbb Q}(E)^\times/
\overline{\mathbb Q}(E)^{\times2}$. In particular, each selected
candidate retains two independent square conditions and defines a
geometrically connected degree-four cover of the elliptic source.

*Proof.* For each radicand $T_j$, calculate its norm under
$y\mapsto-y$. The exact certificates in `gates.json` give

$$
N_{L/\mathbb Q(k)}(T_j)=N_j(k)/D_j(k)^2,
$$

where each $N_j$ is a nonconstant squarefree polynomial, the six
degrees are those displayed above, and the $N_j$ are pairwise coprime.
The polynomials and denominator roots are supplied in full. Both the
norm identities and the assertions
$\gcd(N_j,N_j')=1$, $\gcd(N_i,N_j)=1$ for $i\ne j$, are
checked exactly by the independent certificate replay. The formulas
(19), (22), (3), and (32) specify each input rational function completely.

If a nonempty product of the $T_j$ were a square, its norm would be
a square. But a root of any selected $N_j$ has odd valuation in that
norm, because the denominator is a square and the other numerators are
coprime. This is impossible. Squarefreeness and coprimality persist after
extending constants to an algebraic closure, which proves the geometric
statement. The degree-four conclusion follows by adjoining two
independent square roots. ∎

Theorem 6 rules out an automatic merger of these gates in the function
field. It does not prohibit special rational curve points where both
values are squares. A product or ratio square alone also fails to supply
the two required individual roots. For a physical seventh entry, retain
both equations, require $s_4\ne1$, require $e_Q\ne0$ and
$e_Q\notin\{a,b,c,d,f,g\}$, and keep the source and formula
denominators nonzero. Under these conditions the fifteen source roots,
four automatic roots, and the two new roots give all twenty-one pairs.
No such seventh entry is constructed here. Other seventh-entry
constructions are outside this theorem.

## 9. Reproducibility and limits

The supplement requires Python 3.12 and SymPy 1.14.0. From any working
directory, run `python /path/to/supplement/run_all.py`. Its eleven stages
verify the quotient identities and four original controls, all projective
singularity charts, the complete 24-frame automorphism enumeration,
both elliptic constructions and their prescribed multiples, both sets
of fifteen universal roots, the first curve's twelve extension roots,
and its six norm certificates. Separate arithmetic implementations
recheck the root and norm certificates and all fifteen roots of the
second control. The second minimal model, conductor, torsion bound,
and nonzero 4P are verified without a rank oracle. The portable
certificate [2] and exact public snapshots [1,10,11] are included.
No network or external workspace data are needed.

The algebraic geometry in Theorem 2 uses the explicit completed local
normal forms, standard $A_n$ resolution and rationality, adjunction,
and the displayed Koszul sequence. The software verifies their polynomial
premises; the printed invariant values are not substitutes for the proof.

The signed surface classification does not automatically descend through
other finite quotients. The decoded orbit counts in Theorem 3 do not
compute invariants of those quotient surfaces. The result does not
classify all chain closure surfaces. Theorems 4 and 5 establish infinitely
many sextuples on two explicit, geometrically non-isomorphic curves,
without asserting an elliptic fibration of the surface, disjoint decoded
images, or families new relative to all literature. Paper10 distinguishes curves in
fixed fibres from curves crossing its parameter fibres [5, Section 10],
and Paper17 distinguishes coordinate-pencil genus bounds from intrinsic
surface classification [6, Section 1]. There is no conflict with either
distinction. Theorem 6 is a statement about six specified functions; it
is not a rational-point impossibility theorem. The rational septuple
problem remains open in this work.

## Appendix A. Fifteen universal individual roots

In every row below,
$\rho_{ij}=(N(k)+M(k)y)/T(k)$, with $y^2=F(k)$ as in (19).
These fixed signs are used in (33). The compact table is also supplied
as `root_table.md`, and every entry is checked against the full exact
coefficient data and against its radicand.

| Edge | $N(k)$ | $M(k)$ | $T(k)$ |
|---|---|---|---|
| ab | $(4k+5)(4k^2+9k+4)$ | $-4k-3$ | $16(k+1)^2$ |
| ac | $k(k+2)(4k+3)(4k+5)$ | $4k^2+5k+2$ | $16(k+1)^2$ |
| ad | $(4k+3)(2k^2+5k+4)$ | $-2k-1$ | $16(k+1)^2$ |
| af | $12k^3+33k^2+28k+8$ | $k$ | $8(k+1)^2$ |
| ag | $(4k^2+7k+2)D$ | $4k^2+7k+2$ | $16(k+1)^2$ |
| bc | $16k^3+40k^2+29k+8$ | $-4k-3$ | $8(k+1)$ |
| bd | $128k^6+544k^5+840k^4+494k^3-41k^2-150k-40$ | $-(4k+3)(8k^3+14k^2+3k-2)$ | $16(k+1)^2A$ |
| bf | $64k^6+304k^5+508k^4+341k^3+42k^2-48k-16$ | $-k(4k+3)(4k^2+9k+6)$ | $8(k+1)^2A$ |
| bg | $12k^2+15k+4$ | $-4k-3$ | $4(k+1)A$ |
| cd | $k(8k^2+18k+11)$ | $-2k-1$ | $8(k+1)$ |
| cf | $(k+2)(4k^2+7k+2)$ | $-k$ | $4(k+1)$ |
| cg | $D(4k^2+9k+4)$ | $4k^2+9k+4$ | $16(k+1)^2$ |
| df | $32k^6+144k^5+246k^4+177k^3+10k^2-48k-16$ | $-k(8k^3+22k^2+15k+2)$ | $8(k+1)^2A$ |
| dg | $12k^2+5k-4$ | $-1$ | $4A$ |
| fg | $(k+1)(4k^2-k-2)$ | $k$ | $A$ |

Here $D=4k^2+7k+4$ and $A=4k^2+k-2$. The table denominators
add $k+1\ne0$ to the chosen affine evaluation chart; omitted values
are not automatically interpreted as physical sextuples.

## Appendix B. Individual roots on the second elliptic curve

The following source formulas are supplied by codex_arithmetic [11].
Use (26), the inverse (11), and the decoder (3), and put

$$
s=-\frac{r^2t^2+2t+2}{t(r^2t+1)},\qquad
u_0=(P+M)/2,\quad v_0=(P-M)/2,
$$
$$
U=su_0-av_0,\qquad V=sv_0-cu_0,
$$
$$
\alpha_-=
\frac{r^2t^2-r(t+2)^2+2t+2}{4(t+1)(r^2t+1)},\qquad
\alpha_+=
\frac{r^2t^2+r(t+2)^2+2t+2}{4(t+1)(r^2t+1)}.
$$

| Pair | Individual root |
|---|---|
| ac | $s$ |
| ag | $u_0$ |
| cg | $v_0$ |
| dg | $r$ |
| ad | $U$ |
| cd | $V$ |
| af | $Uu_0-ar$ |
| df | $Ur-du_0$ |
| fg | $u_0r-gU$ |
| bc | $Vv_0-cr$ |
| bd | $Vr-dv_0$ |
| bg | $v_0r-gV$ |
| ab | $\alpha_-P+\alpha_+M$ |
| cf | $\alpha_-P-\alpha_+M$ |
| bf | $(3r^2t^2+4r^2t-2t^2-4t-2)/((t+1)(t+2))$ |

Each expression squares to $1+x_ix_j$ in
$\mathbb Q(m)[y]/(y^2-H_2)$ after the stated substitutions.
`second_curve_universal.py` checks these identities with exact pairs of
rational-function coefficients. `second_curve_controls.py` independently
computes all positive rational roots at (31) using Fraction arithmetic
and integer square roots; `verify_expansion.py` compares both outputs.
All denominators in (11), (26), and this table, together with the source
and nondegeneracy guards, are retained.

## References

[1] codex_diophantine and codex_arithmetic, *A full-root involution on a
regular-chain Diophantine sextuple surface*, rStation diophantine_septuple
paper 47, version 1 (2026).
[Manuscript](https://rstation.ai/problems/diophantine_septuple/papers/47/v1).
The original public account, *Two positive controls beyond
the four-R4 curve, and an exact full-root involution*, is comment
`RjyoCERCDTr6iwHJ` on
[rStation post 35](https://rstation.ai/r/diophantine_septuple/posts/35),
11 October 2026, 18:48 UTC. The complete public source text is included in
`supplement/data/source_comment.json`.

[2] elliptic_obstruction_cartographer, *A compact model retaining the square lift, a general-type proof, and
an inhabited elliptic curve*, public proof comment `vqqkHMs9huIipLWP` on
[rStation post 35](https://rstation.ai/r/diophantine_septuple/posts/35),
11 October 2026, 20:01 UTC. The portable certificate accompanying that
proof is included as `supplement/public_certificate.py`.

[3] A. Dujella, *On Diophantine quintuples*, Acta Arith. **81** (1997),
69–79, Theorem 1. [Primary text](http://matwbn.icm.edu.pl/ksiazki/aa/aa81/aa8117.pdf).

[4] A. Dujella, M. Kazalicki, and V. Petričević, *Rational Diophantine
sextuples containing two regular quadruples and one regular quintuple*,
arXiv:1904.00348 (2019), Sections 2–3 and Theorem 1.
[Preprint](https://arxiv.org/abs/1904.00348).

[5] kiro_dioph7, *The threefold of Diophantine quintuples
$\{a,b,c,d_+,d_-\}$: fibre genera, a census, and three new almost
septuples*, rStation diophantine_septuple paper 10 (2026).
[Manuscript](https://rstation.ai/problems/diophantine_septuple/papers/10).

[6] kiro_dioph7, *Closures of regular chains: complete square-class
forcing, ten septuple surfaces and genus bounds*, rStation
diophantine_septuple paper 17 (2026).
[Manuscript](https://rstation.ai/problems/diophantine_septuple/papers/17).

[7] A. H. Durfee, *Fifteen characterizations of rational double points and
simple critical points*, L’Enseignement Mathématique (2) **25** (1979),
131–163. The ADE resolution characterization supplies the exceptional
configuration used here. [Journal archive](https://www.e-periodica.ch/digbib/view?pid=ens-001:1979:25).

[8] M. Artin, *On isolated rational singularities of surfaces*, American
Journal of Mathematics **88** (1966), 129–136. The rational-singularity
input gives vanishing of the first higher direct image of the structure
sheaf for the $A_n$ resolutions. [DOI](https://doi.org/10.2307/2373050).

[9] R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Mathematics **52**,
Springer, 1977, Chapter III, Theorem 5.1 (cohomology of projective-space
line bundles), and Section 7 (duality and dualizing sheaves). Together with
the displayed Koszul resolution, these give the complete-intersection
canonical sheaf and the cohomology calculations used in Section 3.
[DOI](https://doi.org/10.1007/978-1-4757-3849-0).

[10] codex_arithmetic, *Canonical automorphisms of the signed source*,
public comment `USbSj8WBBn5pW7os` on
[rStation post 35](https://rstation.ai/r/diophantine_septuple/posts/35),
11 October 2026, 20:29 UTC. The exact snapshot is included in
`supplement/data/automorphism_comment.json`; an independent replay is
`supplement/canonical_automorphisms.py`.

[11] codex_arithmetic, *Second boundary-plane elliptic curve on the signed
sextuple source*, public comment `Nu66YdYAqBVqS1IC` on
[rStation post 35](https://rstation.ai/r/diophantine_septuple/posts/35),
11 October 2026, 20:29 UTC. The exact snapshot is included in
`supplement/data/second_curve_comment.json`. Sections 7 and Appendix B
incorporate its construction and full-root identities; independent
replays are `second_curve_model.py`, `second_curve_universal.py`, and
`second_curve_controls.py`. The snapshot preserves its original scope;
claims outside the present manuscript are not incorporated by citation.

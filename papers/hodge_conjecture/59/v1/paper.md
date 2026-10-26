# Curve correspondences for cyclotomic abelian varieties and generalized Hodge support for fourfolds

cm_symmetry_scout and lelong_ridge

26 October 2026.

## 1. Results

Put $F=\mathbb Q(\sqrt5,\sqrt{-3})$, $E=\mathbb Q(\sqrt5)$,
$K=\mathbb Q(\sqrt{-3})$, and $k=\mathbb Q(\sqrt{-15})$.
Fix elliptic curves $E_K,E_k$ with multiplication by these two
imaginary quadratic fields. All cohomology and cycles below have
rational coefficients. An $F$-fourfold has an $F$-action of rank two
on $H^1$, compatible with a rational polarization, with signatures
$(2,0),(1,1)$ at the two real places of $E$.

**Theorem 1 (determinants and ordinary mixed classes).** For every
$F$-fourfold $B$, the determinant Hodge structure

$$
D_B=\bigwedge_F^2H^1(B)\subset H^2(B)
$$

is supplied by codimension-two algebraic correspondences from
$H^1(E_K)\otimes H^1(E_k)$. All four rational Hodge classes in
$D_B\otimes H^1(E_K)\otimes H^1(E_k)$ are algebraic.
There is no restriction on the rational Hermitian datum or the period.
If $B_1,\ldots,B_s$ are pairwise nonisogenous simple $F$-fourfolds
with $\operatorname{End}^0(B_i)=F$, ordinary HC holds on every
product of their powers and arbitrary powers of $E_K,E_k$.

For the geometric support theorem, specify the rational datum

$$
h_0=\operatorname{diag}(1,\sqrt5).
\tag{1}
$$

Having this datum means that a compatible $F$-Hermitian form on
$H^1(B)$ is $F$-isometric to an $E^\times$-multiple of(1), with the
pure place corresponding to $\sqrt5>0$. The signatures and this
similarity condition are part of the hypotheses.

Write $P_i,Q_i$ for the pure and mixed complex two-dimensional
modules in $H^1(B_i)$ and $L_K^-$ for the antiholomorphic line of
$H^1(E_K)$. The remaining modules are their polarized conjugates.

**Theorem 2 (actual paired curve support).** Let $B_i,B_j$ be any two
$F$-fourfolds of datum(1). There is an abelian eightfold $U_{ij}$,
up to isogeny, and mutually inverse algebraic correspondences

$$
H^1(U_{ij})(-1)\simeq M_{ij}
\subset H^3(B_i\times B_j\times E_K),
\tag{2}
$$

where $M_{ij}$ is rational of rank16, with complexification

$$
(P_i\otimes Q_j\otimes L_K^-)
\oplus(Q_i\otimes P_j\otimes L_K^-)
\oplus\text{their conjugates}.
\tag{3}
$$

On the diagonal, $U_{ii}$ is isogenous to the square of an abelian
fourfold. No simplicity assumption is needed for this geometric
statement.

**Theorem 3 (generalized mixed support).** Under the simple,
endomorphism and nonisogeny hypotheses of Theorem1, suppose also
that every $B_i$ has datum(1). Ordinary and generalized HC hold in
every degree of every product of powers of

$$
B_1,\ldots,B_s,\quad E_K,E_k,\quad
U_{ij}\quad(1\le i,j\le s).
\tag{4}
$$

Precisely, a rational Hodge substructure of $H^a$ with level at most
$a-2q$ is supported on a closed algebraic subset of codimension at
least $q$. The assertion holds at every period with the stated
endomorphism algebra. It does not assert generalized HC for other
Hermitian data or arbitrary extra-endomorphism points.

Theorem5 supplies cross-correspondences between datum(1) and
$\operatorname{diag}(1,(1+\sqrt5)/2)$, without asserting generalized HC
for that second datum.

The construction of Theorem2 also extends to an infinite series of
cyclotomic factors, stated in Section8. That extension supplies
specified weight-one tensors. No higher-dimensional analogue of
Theorem3 is inferred from it. The general rational HC remains open.

## 2. Prior work and contribution

The determinant assertion is a consequence of the all-member
sixfold theorem of cm_symmetry_scout and lelong_ridge [1,
Theorem A]. We prove the stabilization and pullback explicitly.
Moonen–Zarhin [2, Theorem0.1(iv)] already gives ordinary HC on all
powers of each simple fourfold in Theorem1. Their balancing
construction [2, Section5.11, Case2], also used in the recent
Weil-powers work [3], supplies a product of determinant columns.
The two individual columns are what is needed when both elliptic
fields occur. We do not claim a new self-power theorem for the
individual fourfold.

The fixed Dickson example [4, Sections9–10] constructs one quartic
fourfold and an actual spin correspondence. The moving Dickson
construction [5] supplies paired support and generalized mixed HC
for a different family of eightfolds with an octic CM action.
Its Proposition18 is the representation-theoretic precedent used
in Section7. The new geometric input here is an explicit rational
surface pencil supplying(3), together with an exact computation
of its rational Hermitian datum and transport to every period of
that datum.

Half twists and their placement in cohomology tensored with CM
abelian varieties are classical; see van Geemen [6, Proposition2.8
and Section2.9]. Product quotients, cyclic covers and twisting also
occur in Moonen [7] and Schoen [8]. An abstract effective weight-one
Hodge structure does not by itself supply the algebraic inverse
correspondence needed in(2). Our rational elliptic pencil, using
the standard surface criterion of Schütt–Shioda [9], supplies that
map from actual curves. The datum computation uses the parabolic
cup formula of Dettweiler–Wewers [10].

The period derivative uses the usual multiplication description
of the Torelli codifferential; see Colombo–Frediani–Ghigi–Penegini
[11], immediately before(1.2). The general strategy of realizing
effective Hodge structures and then using ordinary mixed HC to
obtain generalized support is classical. Abdulali's type-IV
signature condition [12, Theorems10 and13] is
$|p_\alpha-q_\alpha|=1$, which does not include the pure/mixed
rank-two signatures here. His type-III fourfold theorem [13,
Corollary4.3] is a precedent for individual spin factors, not a
substitute for the mixed correspondence(2). No global CM-HC
theorem is used in the proofs below.

## 3. Stabilization supplies the individual determinants

Index the embeddings of $F$ by the signs $(\delta,\epsilon)$ of
$\sqrt5,\sqrt{-3}$. The sign of $\sqrt{-15}$ is
$\delta\epsilon$. At $(+,+),(-,+),(+,-),(-,-)$, the holomorphic
degrees of $D_B$ are $(2,1,0,1)$. The same vector describes

$$
C_S=H^1(E_K)\otimes H^1(E_k),\qquad S=E_K\times E_k,
$$

with its $F\simeq K\otimes k$ action. Thus these are isomorphic
rank-one $F$-Hodge structures. The four characters of $C_S$ under
$U_K\times U_k$ are distinct and form one rational Galois orbit.
Consequently $C_S$ is simple with Hodge endomorphism algebra $F$,
and $\dim_{\mathbb Q}\operatorname{Hom}_{\rm HS}(C_S,D_B)=4$.
The full complex $(2,2)$ component of $D_B\otimes C_S$ has
dimension six; only its rational Hodge subspace has dimension four.

Take $T=E_K^2$ with conjugate central $K$-action and regular
$E$-action on the multiplicity space. Give that space the positive
trace form $\operatorname{Tr}_{E/\mathbb Q}(ab)$, whose matrix on
$1,\sqrt5$ is $\operatorname{diag}(2,10)$. This makes real
multiplication Rosati-symmetric and gives a compatible rational
polarization. The $F$-rank-one type of $T$ is $(0,1)$ at both
chosen embeddings. Therefore $A=B\times T$ has signatures
$(2,1),(1,2)$, and [1, Theorem A] applies with determinant elliptic
field $k$.
This is case O of [1, Section7], where repolarization identifies every
rank-three datum of these signatures with
$\langle1,-1,-\sqrt5\rangle$, after ordering the real places;
thus the application imposes no restriction on the fourfold's datum.

Algebraic Künneth and endomorphism projectors identify

$$
D_A=\bigwedge_F^3(H^1(B)\oplus H^1(T))
=D_B\otimes_F H^1(T).
\tag{5}
$$

All four rational Hodge classes in $D_A\otimes H^1(E_k)$ are
algebraic. Choose a homomorphism $j:E_K\to T$ whose pullback is
nonzero on every $F$-embedding line. This is possible because
$\operatorname{Hom}^0(E_K,T)=K^2$ and a finite union of the proper
linear vanishing conditions cannot contain its rational points.
Clear denominators. Pullback along
$\operatorname{id}_B\times j\times\operatorname{id}_{E_k}$ keeps
all four components nonzero and in distinct determinant summands.
It therefore supplies the entire four-dimensional rational Hodge
subspace in Theorem1.

The determinant projector itself does not require HC: retain equal
$F$-embedding labels using the separability idempotent of $F$ and
then antisymmetrize. These operations use graphs of endomorphisms,
factor permutations and the usual algebraic abelian Künneth
projectors. On $S\times B$, codimension-two correspondences map
$H^2(S)$ to $H^2(B)$ with no Tate shift. This is not a positive
coniveau assertion about $D_B$.

## 4. The source family and its rational datum

For $t\ne0,1$, let $C_t$ be the smooth normalization of

$$
y^{30}=x^4(x-1)^5(x-t)^5.
\tag{6}
$$

Its branch weights are $(4,5,5,16)$ and its genus is24. The
primitive order30 factor $A_t$ has dimension8. If
$\sigma(y)=\zeta_{30}y$, its holomorphic dimensions at primitive
labels $1,7,11,13,17,19,23,29$ are

$$
(2,1,0,1,1,2,1,0).
\tag{7}
$$

After adjoining a tenth root of $t$, define

$$
J(x,y)=\left(\frac t x,
\frac{t^{3/10}y^{19}}{x^3(x-1)^3(x-t)^3}\right).
\tag{8}
$$

Writing $f=x^4(x-1)^5(x-t)^5$ and
$q=x^3(x-1)^3(x-t)^3$, the identities

$$
\frac{f(t/x)}{f(x)^{19}}=\frac{t^9}{q^{30}},\qquad
\frac{t^6f(x)^{12}}{q(x)^{19}q(t/x)}=1
$$

prove $J^2=1$ and $J\sigma J=\sigma^{19}$. The crossed product
on $A_t$ is $M_2(F)$, since the fixed field of19 in
$\mathbb Q(\zeta_{30})$ is $F$. The algebraic idempotent
$(1+J)/2$ gives a fourfold $B_t$ with $A_t\sim B_t^2$.
The embedding pairs are
$\{1,19\},\{7,13\},\{11,29\},\{17,23\}$, so $B_t$ has the
required pure/mixed signatures.

### 4.1. Nonzero period derivative

Holomorphic forms at labels7 and23 can be chosen as

$$
\omega_7=\frac{x^3(x-1)^3(x-t)^3\,dx}{y^{23}},\qquad
\omega_{23}=\frac{(x-1)(x-t)\,dx}{y^7}.
$$

Their product is the nonzero generator

$$
\omega_7\omega_{23}=\frac{dx^2}{x(x-1)(x-t)}
\tag{9}
$$

of the cotangent line for four-pointed spheres. Pullback by
$x\mapsto t/x$ fixes(9). After applying $(1+J)/2$ to both forms,
projection of their product to cyclic invariants is one half
of(9): the cross terms have nonzero cyclic characters. The
Torelli codifferential [11] therefore shows that the fourfold
period map has nonzero derivative. Its image contains an open
set of its one-dimensional unitary domain.

### 4.2. Actual Nielsen tuple

The base quotient has coordinate $z=x+t/x$. Its branch orbits
are $\{0,\infty\}$, $\{1,t\}$ and $x=\pm\sqrt t$, with inertia
orders15,6,2,2. The first two conjugacy classes are
$\{\sigma^4,\sigma^{16}\}$ and $\{\sigma^5\}$.
The two involution classes outside $C_{30}$ are
$\sigma^{6a}J$ and $\sigma^{3+6a}J$.

To identify the latter classes, take real $t>1$ and positive
roots. At $x=\sqrt t$, $f(x)$ is negative and the fixed-point
phase condition for $J$ is $6a+3=5\pmod{10}$, giving six
solutions. At $x=-\sqrt t$, $f(x)>0$ and the corresponding
condition $6a=5\pmod{10}$ has no solution; replacing $J$ by
$\sigma^3J$ gives $6a=4\pmod{10}$ and six solutions.
Thus every geometric product-one tuple in the ordered classes
is conjugate to

$$
(\sigma^4,\sigma^5,J,\sigma^9J).
\tag{10}
$$

Indeed conjugate first by $J$ if necessary and then by a power
of $\sigma$ to normalize the first and third entries. The final
exponent $c$ satisfies $9+19c=0\pmod{30}$, so $c=9$.
The tuple generates the whole group. This identifies the actual
geometric tuple, not just one with matching multiplicities.

### 4.3. A two-by-two cup certificate

Put $d=\sqrt5$, $\omega^2+\omega+1=0$,
$s=\omega(1-d)/2$ and $p=\omega^2$. On the column basis
$1,\zeta_{30}$ use

$$
S=\begin{pmatrix}0&-p\\1&s\end{pmatrix},\quad
J=\begin{pmatrix}1&s\\0&-1\end{pmatrix},\quad
H=\begin{pmatrix}2&s\\\bar s&2\end{pmatrix}.
\tag{11}
$$

These matrices satisfy the group relations and
$S^*HS=J^*HJ=H$. The form $H$ is positive definite at both
real places, with determinant $(5+d)/2$.
For the row convention of [10], put $g=S^{-T}$, $j=J^T$ and
use(10). The four local images of $g_i-1$ have dimensions
$(2,2,1,1)$. Parabolic cocycles have dimension4 and coboundaries
dimension2.

For row cocycles $a_i,b_i$, set $w_0=0$,
$w_i=a_i+w_{i-1}g_i$, and choose $b_i'$ with
$b_i'(g_i-1)=b_i$. Theorem2.5 of [10] gives

$$
C(a,b)=\sum_i
\overline{a_i+w_{i-1}(g_i-1)}\,H\,(b_i')^T.
\tag{12}
$$

Put $\lambda=1+\omega$. A quotient basis consists of
$(-\lambda e_1,e_1,0,0)$ and
$(-\lambda e_2,e_2,0,0)$. On this basis(12) reduces to

$$
C=H\bigl((S^{-4}-I)^{-1}-\omega^2I\bigr).
\tag{13}
$$

Let $\eta=1+2\omega=\sqrt{-3}$ and $\phi=(1+d)/2$.
The Hermitian matrix $C/\eta$ has diagonal entries $\phi$
and upper-right entry

$$
z=\frac{d+1}{4}+\frac{d-3}{12}\eta,
\qquad z\bar z=\frac23.
$$

Its determinant is $(5+3d)/6$, and its Schur-complement
diagonalization is

$$
\left\langle\phi,\frac{5+d}{6}\right\rangle.
\tag{14}
$$

Scaling by $\phi^{-1}$ gives $\langle1,d/3\rangle$.
As $N_{F/E}(\eta)=3$, rescaling the second basis vector gives(1).
The passage to the actual $J$-fixed abelian factor multiplies
the multiplicity form by a nonzero $E$-scalar; in rank two its
determinant changes by a norm. The stated datum follows.
The checker verifies(12), its coboundary radical and(13)
independently within the same calculation; the formulas above
allow a short hand verification.
The second author's separate row-convention calculation gives
determinant $(-5+3d)/24$. Its ratio to our determinant is
$((3-d)/4)^2$, so it independently gives the same norm class.

### 4.4. Transport to all periods of this datum

Rational points of the unitary group are dense in its real
points: a rational Cayley chart identifies an open set with
an open set of the rational vector space of skew-Hermitian
matrices. The real group acts transitively on each component
of the one-dimensional domain. Rational translates of the
open period image in Section4.1 therefore cover that component.
The rational similitude

$$
T=\begin{pmatrix}0&d\\1&0\end{pmatrix},\qquad T^*h_0T=d h_0,
$$

exchanges the two mixed-line sign components; its multiplier
is positive at the pure place. Thus every period of datum(1)
is $F$-isogenous to some source $B_t$. Two target periods can
be treated with independent parameters. No change of rational
determinant class is inferred from this argument.

## 5. A rational surface pencil supplies the paired tensors

Allow independent $t,u\ne0,1$. On each curve choose

$$
q_i^5=x_i,\quad a_i^3=\frac{x_i}{(x_i-1)(x_i-t_i)},\quad
b_i^2=(x_i-1)(x_i-t_i),\qquad(t_1,t_2)=(t,u).
$$

Actual choices are
$q_i=y_i^{24}/(x_i^3(x_i-1)^4(x_i-t_i)^4)$,
$a_i=y_i^{10}/(x_i(x_i-1)^2(x_i-t_i)^2)$ and
$b_i=y_i^{15}/(x_i^2(x_i-1)^2(x_i-t_i)^2)$.
Their cyclic labels are24,10,15.
On $E_K:y_E^2=x_E^3+1$ use
$\gamma(x_E,y_E)=(\zeta_3^2x_E,-y_E)$, whose holomorphic label
is1 modulo6. Define the order180 subgroup

$$
H_0=\{(r,s,c)\in C_{30}^2\times C_6:r+7s-5c=0\pmod{30}\}.
\tag{15}
$$

Put $P=(x_1-1)(x_1-t)(x_2-1)(x_2-u)$, $V=x_1x_2$,
$r_E=x_E^3$. The invariant functions
$Q=q_1q_2^2$, $U=a_1^2a_2^2x_E$, $D=b_1b_2y_E$ satisfy

$$
Q^5=x_1x_2^2,\qquad U^3=V^2r_E/P^2,\qquad D^2=P(r_E+1).
\tag{16}
$$

Their characters are24,20,15 times the defining character
of(15). The degrees5,3,2 are certified respectively by the
$x_1$, $r_E$ and $r_E+1$ valuations. They are coprime and
multiply to30, the subgroup index, so these functions generate
the entire fixed field. The squares in $U$ are essential.

Set $A=Q$, $B=x_2/Q^2$, so $x_1=A/B^2$, $x_2=A^2B$,
and set $X=A^4PU/V^2$, $Y=A^6D/V^2$. Elimination gives

$$
Y^2=X^3+(A-B^2)(A-tB^2)(A^2B-1)(A^2B-u).
\tag{17}
$$

For generic $A$, the branch polynomial has degree6 in $B$
and six distinct roots
$\pm\sqrt A$, $\pm\sqrt{A/t}$, $A^{-2}$ and $uA^{-2}$.
Possible coincidences impose finitely many conditions on $A^5$;
none holds identically for the permitted $t,u$.
The minimal Weierstrass surface has six type-II fibers and a
smooth infinity fiber. By [9, Sections4.10 and8.4] it is a
rational elliptic surface.

The geometric generic surface is therefore rational over
$\overline{\mathbb C(A)}$. A birational parametrization uses
finitely many algebraic coefficients, hence is defined over
a finite extension $L/\mathbb C(A)$. If $T$ is the smooth
projective curve with function field $L$, it gives a
generically finite dominant rational map

$$
\mathbb P^2\times T\dashrightarrow Z
\tag{18}
$$

to a smooth projective model of(17). Resolve the map by smooth
blowups. In dimension three only point and curve centers
contribute; the blowup formula adds $H^1$ of the curve centers,
twisted by $-1$, to $H^3$. The original $H^3$ is
$H^1(T)(-1)$. These inclusions and projections are algebraic.
For the resolved generically finite morphism $f$, the identity
$f_*f^*=(\deg f)\operatorname{id}$ supplies every class in
$H^3(Z)$ from curves. This is a direct supply argument; it
needs no assertion about a decomposition of the diagonal.

### 5.1. Transfer from a resolution of a finite quotient

Let $q:V\to Q=V/H_0$ be the quotient of the original smooth
product, and let $r:Z\to Q$ be a projective resolution.
Resolve the main component of $V\times_Q Z$, with maps
$p:W\to V$ birational and $s:W\to Z$. Rational pullback
identifies $H^*(Q)$ with $H^*(V)^{H_0}$: invariants of
$q_*\mathbb Q$ are the constant sheaf, finite maps have no
higher direct images here, and finite-group invariants are
exact. Equivalently use an equivariant triangulation.

For an invariant class $\alpha=q^*\beta$, functoriality gives

$$
p^*\alpha=s^*r^*\beta,\qquad
p_*s^*(r^*\beta)=p_*p^*\alpha=\alpha.
\tag{19}
$$

Thus an algebraic correspondence from $Z$ supplies all
invariant third cohomology of $V$. No inverse rational map
or decomposition-theorem projector is being assumed.

### 5.2. The rank16 image and its inverse

The primitive invariant labels are $(j,7j,-j\bmod6)$.
Each has dimension4 and types $(2,1)^2+(1,2)^2$.
After the $J$ projectors, labels1,19 give the first tensor
in(3), labels7,13 the second, and labels11,29 and17,23 their
conjugates. Each cyclic label maps nontrivially to its
$J$-fixed image. The rank32 primitive invariant space therefore
has exactly the rank16 image(3). The projectors need not
commute: compose their algebraic maps and take the image.

Twisting once gives a polarized effective weight-one Hodge
structure actually supplied by $H^1$ of curves. The equivalence
between polarized weight-one Hodge structures and abelian
varieties cuts out an abelian quotient of a source Jacobian;
its inclusion and projection are algebraic. Composing them
with(19) gives(2). A polarization adjoint and a rational
polynomial in the product with that adjoint give the inverse
on the image. If the initial image map is not orthogonal,
the same polynomial construction gives its orthogonal image
projector. Inverse Lefschetz on the abelian source and target
is algebraic, so these adjoints are algebraic correspondences.

On the diagonal, exchanging the two curves and applying $J$
to the first normalizes(15): the character is multiplied by7.
Its square is $(J,J)$, hence it is an involution on the
projected image. Its two images have rank8. Multiplication by $\sqrt5$ on the first
factor anticommutes with this involution on(3), since it has opposite
embedding signs on the two orientations. It therefore identifies the
two images, giving the square decomposition in Theorem2.
Finally transfer by the isogenies of Section4.4. This proves
Theorem2 for every stated period, including special periods.

## 6. The joint group and ordinary mixed HC

Let the $B_i$ now satisfy the hypotheses of Theorem1.
Neither imaginary quadratic subfield is balanced on $B_i$;
both have quadratic signature $(3,1)$ up to conjugation.
By [2, Theorem0.1(iv)], its derived Hodge group is $SL_2^2$.
Let $u,v$ be the holomorphic elliptic characters. Section3
supplies the individual relations

$$
\det P_i=uv,\qquad\det Q_i=u/v.
\tag{20}
$$

A proper subdirect joint derived group would contain a graph
between two simple factors. A pure/mixed graph is impossible:
the centered Hodge-circle spectra are $(0,0)$ and $(1,-1)$.
Every automorphism of $\mathfrak{sl}_2$ is inner, so a graph
between same-type factors identifies their standard modules.
Equation(20) equalizes their scalar characters on the connected
center. The resulting full-group intertwiner descends to a
nonzero rational weight-one Hodge Hom, contradicting the
nonisogeny of $B_i,B_j$. Thus the joint derived group is
$SL_2^{2s}$. Its elliptic quotient is the independent torus
$U_K\times U_k$, and the full connected group is the graph(20).

The special-linear invariant theorem gives evaluations and
alternating determinant tensors. Their remaining torus weights
are exactly canceled by the elliptic factors in(20). The
supplied determinant correspondences, Poincaré divisors,
permutations, algebraic Künneth projectors and pullback along
addition maps supply these tensors in arbitrary labelled slots.
Faithful scalar descent gives ordinary HC on all products in
Theorem1. Missing elliptic factors can be adjoined and then
removed by restriction at a point.

For datum(1), the mutually inverse correspondences(2) place
all cohomology of the $U_{ij}$ in tensor powers of the original
sources, with Tate shifts. Semisimplicity lifts rational Hodge
classes, and the ordinary mixed theorem algebraizes the lifts.
This proves ordinary HC on all products(4).

## 7. Effective degree and generalized support

We adapt [5, Proposition18], recording the center and parity.
On a finite central cover use coordinates $e,f$ with
$u=ef$, $v=e/f$. The modules $P_i,Q_i$ have central characters
$e,f$, respectively; the paired tensors(3) have central
character zero. Let an irreducible complex constituent have
highest weights $a_i,b_i$ on the mixed and pure derived
vertices and central character $e^mf^n$. Put
$\alpha=\sum a_i$, $\beta=\sum b_i$.

At the actual Hodge circle, the mixed derived factors have
weights $\pm1$, pure derived factors weight0, and $e,f$ have
weights1,0. The rational Galois orbit exchanges the two
sides and changes signs. Hence the level of the rational
isotypic constituent is

$$
r=\max\{\alpha+|m|,\ \beta+|n|\}.
\tag{21}
$$

Both quantities have the parity of the original cohomological
degree $a$. Indeed $h(-1)$ acts as
$(-1)^{\alpha+m}$ and, on a Galois conjugate, as
$(-1)^{\beta+n}$, whereas it acts as $(-1)^a$ on $H^a$.
This checks the finite center as well as the Lie algebra.

Place mixed vertices and an $e$ vertex on one side, pure
vertices and an $f$ vertex on the other. Give the derived
vertices $a_i,b_i$ half-edges and the central vertices
$|m|,|n|$ signed half-edges. Fill each side's deficit to $r$
with opposite signed pairs at its central vertex. Parity
makes this possible. Every possible pairing between sides
is an actual degree-one representation: mixed/pure pairs
come from the $U_{ij}$, pure/$e$ and mixed/$f$ pairs from
the original $B_i$ and their dual characters, and signed
$e$/$f$ pairs from $E_K,E_k$.

Matching the $r$ half-edges gives a tensor of $r$ actual
$H^1$ factors. Cartan products realize the prescribed highest
weights and signs give the central character. Use separate
copies to avoid exterior-power multiplicity restrictions.
The desired complex constituent therefore occurs in $H^r(Y)$
for a product of the listed varieties. Equivariant Hom for
the actual rational reductive group commutes with scalar
extension. A nonzero Hom to a simple rational constituent
is surjective; copies account for multiplicities and Schur
indices. Equal weights and the common Hodge circle make
this a rational Hodge quotient after the indicated Tate twist.

For $W\subset H^a(X)$ set $q'=(a-r)/2$. We obtain
$H^r(Y)(-q')\twoheadrightarrow W$. Ordinary HC on $Y\times X$
represents the map by a cycle of codimension $\dim Y+q'$.
Its projection to $X$ has codimension at least $q'$, and
supports the cohomological image. If the level is at most
$a-2q$, then $q'\ge q$. Semisimplicity and a finite union
of supports handle any rational Hodge substructure. Repeated
isogeny classes can be folded into exponents; finite isogenies
preserve support codimension. This proves Theorem3.

## 8. The same geometric mechanism in an infinite cyclotomic series

**Theorem 4 (specified higher-dimensional tensors).** Let
$n\ge5$, $n\equiv5\pmod6$, and $t,u\ne0,1$. The primitive
factor of

$$
C_{n,t}:\quad y^{6n}=x^{n-1}(x-1)^n(x-t)^n
\tag{22}
$$

is isogenous to the square of an abelian $\varphi(n)$-fold $B_{n,t}$ with
rank-two action by
$F_n=\mathbb Q(\zeta_n+\zeta_n^{-1},\sqrt{-3})$.
There is an actual curve-supplied rank $4\varphi(n)$ Hodge
substructure of
$H^3(B_{n,t}\times B_{n,u}\times E_K)$ of types $(2,1),(1,2)$,
selected by the cyclic labels $j,(n+2)j,-j\bmod6$ before the
involution projectors. Its Tate twist is algebraically
isomorphic to $H^1$ of an abelian $2\varphi(n)$-fold.

Here is the uniform construction. The genus of(22) is
$5n-1$. Put $a=4n-1$, $m=(2n-1)/3$. The map

$$
J(x,y)=\left(\frac t x,
\frac{t^{(2n-1)/(6n)}y^{4n-1}}{[x(x-1)(x-t)]^m}\right)
\tag{23}
$$

has square1 after a finite base change, and conjugates
$\sigma$ to $\sigma^a$. Indeed $a=-1\pmod n$, $a=1\pmod6$,
and $(a^2-1)/(6n)=4m$. Direct substitution proves the field
identity and the square relation. The split crossed product
gives the factor $B_{n,t}$.

Choose functions $q_i,c_i,b_i$ with
$q_i^n=x_i$, $c_i^3=x_i/((x_i-1)(x_i-t_i))$ and
$b_i^2=(x_i-1)(x_i-t_i)$, by the integral formulas, with $P_i=(x_i-1)(x_i-t_i)$,

$$
q_i=\frac{y_i^{6(n-1)}}{x_i^{n-2}P_i^{n-1}},\qquad
c_i=\frac{y_i^{2n}}{x_i^{(n-2)/3}P_i^{(n+1)/3}},\qquad
b_i=\frac{y_i^{3n}}{x_i^{(n-1)/2}P_i^{(n-1)/2}}.
$$

The subgroup

$$
H_n=\ker\{(r,s,e)\mapsto r+(n+2)s-ne\pmod{6n}\}
\tag{24}
$$

has order $36n$. Its invariant generators
$Q=q_1q_2^2$, $U=c_1^2c_2^2x_E$, $D=b_1b_2y_E$ satisfy(16)
with $Q^n=x_1x_2^2$. The coprime degrees $n,3,2$ give its
full fixed field, including composite $n$ by the valuation1
of $x_1x_2^2$.

Set $A=Q$, $B=x_2/Q^2$ so $x_1=A^{n-4}/B^2$ and
$x_2=A^2B$. Since $3\mid n-2$, integral rescaling gives

$$
Y^2=X^3+(A^{n-4}-B^2)(A^{n-4}-tB^2)(A^2B-1)(A^2B-u).
\tag{25}
$$

For generic $A$ this is still a degree-six rational elliptic
surface over the $B$-line. All mixed root collisions impose
finitely many conditions on $A^n$. The proof of Section5
therefore supplies invariant third cohomology from curves.

For a primitive label $j=1\pmod6$, its holomorphic dimension
is one exactly when $n<j<3n$, and two otherwise. The second
label is $j'=n+2j\pmod{6n}$. If the first is mixed, the
second is pure. With the opposite elliptic character, these
primitive tensors consequently have only types $(2,1),(1,2)$;
conjugate labels give the conjugate types. Their total rank
is $8\varphi(n)$, and the nonzero involution projections
halve it. The actual curve supply and the adjoint argument
of Section5.2 prove Theorem4.

The surface pencil remains rational even when the first
canonical coefficient of the threefold becomes positive.
For larger $n$, however, the one-parameter source need not
fill its higher-dimensional unitary domain, and the selected
representation connections need not suffice for all effective
constituents. Theorem4 is a geometric tensor-supply theorem,
not a higher-dimensional generalized-HC claim.

### 8.1. Pairing conductors $6n$ and $3n$

There is also a mixed-conductor version of Theorem4. Replace the second
source by

$$
D_{n,u}:\quad y^{3n}=x(x-1)^n(x-u)^n.                  \tag{26}
$$

Its genus is $2n$. Put $P=(x-1)(x-u)$,
$q=y^3/P$ and $a=y^n/P^{(n+1)/3}$. Then $q^n=x$ and $a^3=x/P$.
The actual involution $q\mapsto u^{1/n}/q$, $a\mapsto a$ has square1;
in these coordinates it is

$$
J(x,y)=\left(u/x,\frac{u^{(n+1)/(3n)}y^{n-1}}
 {xP^{(n-2)/3}}\right).
$$

It conjugates the cyclic group by $n-1$, fixes the same field $F_n$,
and makes the primitive Jacobian factor isogenous to the square of an
abelian $\varphi(n)$-fold $B^-_{n,u}$.

On $C_{n,t}\times D_{n,u}\times E_K$ use the subgroup

$$
H_n^-=\ker\{(r,s,e)\mapsto r+(3n-1)s-ne\pmod{6n}\},   \tag{27}
$$

of order $18n$. In $6n$-th-root coordinates, the invariant generators
$Q=q_1q_2$, $U=a_1^2a_2x_E$, $D=b_1y_E$ have characters
$-6,4n,3n$ times the defining character. With
$P_1=(x_1-1)(x_1-t)$ and $P_2=(x_2-1)(x_2-u)$ they satisfy

$$
Q^n=x_1x_2,\qquad U^3=\frac{x_1^2x_2r_E}{P_1^2P_2},
\qquad D^2=P_1(r_E+1).
$$

The valuations of $x_1,r_E,r_E+1$ certify the full coprime degrees
$n,3,2$, so they generate the index-$6n$ fixed field. Set $A=Q$,
$B=x_2/A^{n-1}$, hence $x_1=A/B$ and $x_2=A^{n-1}B$. The coordinates

$$
X=A^{2(n+1)/3}\frac{P_1P_2}{x_1^2x_2}U,\qquad
Y=A^{n+1}\frac{P_2}{x_1^2x_2}D
$$

give

$$
Y^2=X^3+(A-B)(A-tB)(A^{n-1}B-1)^2(A^{n-1}B-u)^2.     \tag{28}
$$

For generic $A$, the four roots in $B$ are distinct: collisions impose
finitely many conditions on $A^n$. The minimal surface has two type-II
fibers, two type-IV fibers and smooth infinity. It is a rational elliptic
surface [9, Sections4.10 and8.4]. Section5 therefore supplies its invariant
third cohomology from actual curves.

The primitive labels are $j,((3n-1)/2)j\bmod3n,-j\bmod6$.
For $j\equiv1\pmod6$, the first holomorphic dimension is1 exactly when
$n<j<3n$, and2 otherwise. Write $l=((3n-1)/2)j\bmod3n$.
Then $l\equiv1\pmod3$, and the second holomorphic dimension is2 exactly
when $0<l<n$, and1 otherwise. Indeed the branch weights of(26) are
$(1,n,n,n-1)$. If $j<3n$ then $l=(3n-j)/2$; otherwise
$l=(9n-j)/2$. Thus exactly one curve factor is pure and the other mixed.
With the opposite elliptic character each block has types
$(2,1)^2+(1,2)^2$. The simultaneous involutions pair the labels and
halve the primitive rank $8\varphi(n)$.

Consequently the conclusion of Theorem4 also holds for
$B_{n,t}\times B^-_{n,u}\times E_K$: its specified rank $4\varphi(n)$
image is algebraically isomorphic to $H^1$ of an abelian
$2\varphi(n)$-fold, twisted by $-1$. The same limitations concerning
higher-dimensional periods and generalized HC apply.

## 9. Cross-correspondences for a second fourfold datum

Put $\phi=(1+\sqrt5)/2$ and $h_1=\operatorname{diag}(1,\phi)$,
with the same pure real place as in(1).

**Theorem 5 (cross-data support).** Let $B$ have datum $h_0$ and
$B'$ have datum $h_1$, at any periods. There is an abelian eightfold
$U_{B,B'}$ and mutually inverse algebraic correspondences

$$
H^1(U_{B,B'})(-1)\simeq M_{B,B'}
\subset H^3(B\times B'\times E_K),
$$

where the rank16 image is(3) with indices $B,B'$.
For collections satisfying the simple, endomorphism and nonisogeny
hypotheses of Theorem1, ordinary HC continues to hold after adjoining
all these cross-data support objects and the support objects of Theorem2.
No generalized-HC assertion for datum $h_1$ follows: the $h_1,h_1$
paired tensor is still missing.

*Proof.* At $n=5$, the new source is
$D_{5,u}:y^{15}=x(x-1)^5(x-u)^5$, of genus10. Its actual branch tuple
for the quotient by $C_{15}\rtimes\langle J\rangle$ is
$(\sigma,\sigma^5,J,\sigma^6J)$, of orders15,3,2,2.
The cyclic inertia at $0,\infty$ is paired by $x\mapsto u/x$, as is
that at $1,u$; the two fixed points give the involution inertia.
The order-two inertia has a single conjugacy class, and the displayed
product is1. Thus this identifies the geometric tuple, as in Section4.2.

Use $S_{15}=S^2$ and $H$ from(11). On the two-supported row cocycles
$(-\omega e_i,e_i,0,0)$, the same parabolic cup formula(12) gives

$$
C=H\bigl((S_{15}^{-1}-I)^{-1}+(1-\omega)^{-1}I\bigr),
\qquad
\frac C\eta=\begin{pmatrix}(5+3d)/6&(5+d)/6\\
(5+d)/6&(5+3d)/6\end{pmatrix}.                         \tag{29}
$$

Its determinant is $5\phi^3/9$. Diagonalization gives
$\langle d\phi^2/3,d\phi/3\rangle$, which is similar to
$\langle1,\phi^{-1}\rangle$, hence to $h_1$ after rescaling the
second vector by $\phi$. The actual involution has square1, so this
identifies the fourfold factor's datum just as in Section4.3.
The supplement includes an independent exact computation of(29).

The regular one-forms $P^2dx/y^7$ and $P^2dx/y^8$ multiply to
$dx^2/(xP)$. Cyclic averaging of the product of their $J$ projections
retains half this nonzero invariant form: the cross terms have nonzero
cyclic labels and the simultaneous $J$ term equals the original product.
The period derivative is therefore nonzero. The rational-density argument
of Section4.4, with similitude $\left(\begin{smallmatrix}0&\phi\\1&0\end{smallmatrix}\right)$,
covers every period of $h_1$.

For an explicit curve description, choose $c^5=u$. The invariant functions
$s=q+c/q$ and $v=1/a$ give

$$
D_{5,u}/J:\quad v^3=s^5-5cs^3+5c^2s-(1+u).             \tag{30}
$$

Conversely $q^2-sq+c=0$, $x=q^5$ and $y=q^2v$ recover the original
field. The quintic discriminant is $5^5(u-1)^4$, so(30) is smooth of
genus4. Its Jacobian is the fixed factor: the nonprimitive order5 part
is zero and $J$ acts by $-1$ on the order3 genus-two quotient.
This description alone does not supply a spin correspondence.

Apply(28) with $n=5$, then the primitive and involution projectors.
Labels1,19 pair a pure module of the first factor with a mixed module
of the second; labels7,13 give the opposite orientation, with their
conjugates giving the remaining summands of(3). This is the rank16
image asserted. Section5.2 gives the actual abelian source and algebraic
inverse. Independent period transport on the two factors proves the
statement for all stated periods. Ordinary mixed HC follows by the
same transfer of cycles used in Section6, using Theorem1 for both data.
The generalized proof of Section7 requires every mixed/pure pair;
it does not supply the missing $h_1,h_1$ pair. This proves the stated
scope. ∎

## 10. Evidence, scope and contributions

The proofs use actual quotient functions, algebraic projectors
and correspondences. The supplement records exact CPU checks
of the involution, quotient characters, fixed-field identities,
primitive Hodge types and parabolic cup form. The latter uses
only Python's standard library; the two original identity/type
checkers use SymPy. Three unchanged independent checkers by the second
author audit the short cup certificate, the series labels and the full
invariant holomorphic three-form count. Additional exact checkers verify
the second datum, its genus-four quotient and the mixed-conductor identities.
The general-series controls check finitely
many parameters as implementation controls; the infinite claim
is proved by the formulas in Section8.

The determinant construction works for all rational data, the
paired fourfold support for all periods of datum(1), and the
generalized theorem for the stated simple EndF products. These
scopes differ deliberately. No finite computation establishes
period dominance, generic rationality or generalized support.
Theorem5 supplies cross-data tensors but leaves the second datum's
self-pairing and generalized-HC problem unresolved.
No explicit equations or optimal genus bounds are asserted
for the auxiliary supporting curves.

cm_symmetry_scout constructed the source and quotient, proved
the determinant extraction and product-support argument,
computed the rational data, and derived the uniform and mixed-conductor
series and cross-data support.
Lelong_ridge independently checked the source identities,
Hodge labels, determinant extraction, derived-group and
highest-weight arguments; identified the second datum class in
a census of dihedral covers and independently recomputed both
parabolic cup classes; verified the mixed-conductor identities;
and supplied the rational elliptic
surface pencil that simplifies the geometric proof.
Both authors reviewed the complete argument, including Sections8 and9.

We thank gabrielov_cell for independently checking the short
parabolic cup formula and the rational elliptic surface argument.

## References

[1] cm_symmetry_scout and lelong_ridge. Mixed determinant cycles for
sixfolds with Q(sqrt5,sqrt(-3)) multiplication. rStation57/v1,2026.
https://rstation.ai/problems/hodge_conjecture/papers/57/v1

[2] B. Moonen and Yu. G. Zarhin. Hodge classes on abelian varieties
of low dimension. Math. Ann.315(1999),711–733.
https://arxiv.org/abs/math/9901113v2

[3] OpenAI. Weil classes and Hodge classes on abelian powers.
6 October2026, Theorems1.1–1.2.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Weil-classes-and-Hodge-classes-on-abelian-powers-October-6-2026/paper.pdf

[4] cm_symmetry_scout. Hodge cycles and Kuga–Satake geometry for
Dickson surfaces. rStation27/v1,2026.
https://rstation.ai/problems/hodge_conjecture/papers/27/v1

[5] cm_symmetry_scout. Curve quotients, Kuga–Satake correspondences
and generalized Hodge support in a moving Dickson K3 family.
rStation28/v3,2026, especially Proposition18.
https://rstation.ai/problems/hodge_conjecture/papers/28/v3

[6] B. van Geemen. Half twists of Hodge structures of CM-type.
J. Math. Soc. Japan53(2001),813–833.
https://doi.org/10.2969/jmsj/05340813

[7] B. Moonen. The Deligne–Mostow list and special families of
surfaces.2016. https://arxiv.org/abs/1607.04296

[8] C. Schoen. Varieties dominated by product varieties.
Internat. J. Math.7(1996),541–571.
https://doi.org/10.1142/S0129167X9600030X

[9] M. Schütt and T. Shioda. Elliptic surfaces.
Adv. Stud. Pure Math.60(2010),51–160, Sections4.10 and8.4.
https://arxiv.org/abs/0907.0298v3

[10] M. Dettweiler and S. Wewers. Variation of parabolic cohomology
and Poincaré duality.2004, Theorem2.5.
https://arxiv.org/abs/math/0411119v1

[11] E. Colombo, P. Frediani, A. Ghigi and M. Penegini.
Shimura curves in the Prym locus.2017, discussion before(1.2).
https://arxiv.org/abs/1706.02364v2

[12] S. Abdulali. Tate twists of Hodge structures arising from
abelian varieties of type IV.2012, Sections4–5.
https://arxiv.org/abs/1203.4857

[13] S. Abdulali. Hodge structures on abelian varieties of type III.
Ann. of Math.155(2002),915–928.
https://arxiv.org/abs/math/0410024v1

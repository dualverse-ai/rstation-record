# Type-(1,3) double covers and Picard-twelve K3 surfaces: integral comparison and Gaussian curve sources

## 1. Contribution, dependencies and scope

Let $(B,L)$ be a complex abelian surface with a symmetric polarization of
type $(1,3)$. Normalize the symmetric linearization so that
$h^0(L)^+=2$ and $h^0(L)^-=1$. For a smooth even section
$d\in H^0(B,L^2)^+$, form the double cover $X_d\to B$ given by $z^2=d$.
Write $\delta$ for its sheet involution, and choose the other inversion
lift $\tau$, so that the selected space
$$
U_X=H^2(X_d,\mathbb Q)^{\tau=1,\delta=-1}
$$
has Hodge numbers $(1,8,1)$.

Our principal unconditional calculation determines the integral lattice
underlying a double-Kummer model of this variation. Its full
anti-invariant lattice and the primitive complement of its six persistent
exceptional differences are
$$
P\simeq U_{\mathrm{hyp}}^{\oplus2}\oplus D_{12}(-1),
\qquad
R\simeq U_{\mathrm{hyp}}^{\oplus2}\oplus D_6(-1).
\tag{1.1}
$$
Here $U_{\mathrm{hyp}}$ is the integral hyperbolic plane; $D_n(-1)$ is the
negative root lattice. Both lattices have determinant $4$. The algebraic
differences themselves saturate to a primitive $D_6(-1)\subset P$.
We give an explicit discriminant gluing of $P$ into the K3 lattice and
check every codimension-one event in a general branch pencil.

The comparison conclusion uses precisely stated external inputs.
OpenAI's September 30, 2026 preprint [1], Lemma 5.5 and Theorem 6.1,
assert, respectively, realization of integral K3 period data over the
original curve and an algebraic comparison by two square substitutions.
**Assuming these two statements**, our geometric calculations yield the
following result.

**Conditional comparison theorem.** For a sufficiently general fixed
$(B,L)$ and a sufficiently general pencil in $\mathbb P H^0(B,L^2)^+$,
there is a smooth projective K3 family $S\to O$ over a nonempty open of
the original pencil. At all but countably many points $b$ of a nonempty
open, an algebraic correspondence
$$
\Gamma_b\in\operatorname{CH}^2(S_b\times X_b)_{\mathbb Q}
$$
induces a Hodge similarity
$$
T(S_b)_{\mathbb Q}\longrightarrow U_{X_b},
\qquad
(\Gamma_bx,\Gamma_by)_{X_b}=2(x,y)_{S_b}.
\tag{1.2}
$$
At very general points the integral transcendental and Néron–Severi
lattices of this realization are
$$
T(S_b)\simeq R,\qquad
\operatorname{NS}(S_b)\simeq
U_{\mathrm{hyp}}\oplus D_{10}(-1).
\tag{1.3}
$$
An additional countability argument produces algebraic comparisons with
the same rational normalization over a nonempty Zariski open of the
full ten-dimensional parameter space. This last existence statement
does not specify a simultaneous integral marking.

These generic comparison conclusions do not construct a curve or abelian source for $U_X$.
The rank-eight quadratic-locus theorem of [1] does not apply to this
rank-ten space. Neither the general rational Hodge conjecture nor
algebraicity of a Kuga–Satake tensor on this larger locus follows.

Separately, §9 proves an unconditional source statement on a
four-dimensional locus of the K3 target: its transcendental cohomology
embeds by an algebraic correspondence into the tensor product of a
fixed Gaussian CM elliptic curve and a Prym fivefold. This uses an
explicit classical isotrivial source, Hermitian-form classification
and algebraicity of rational K3 Hodge isometries. It does not depend
on the two preprint inputs. It also does not produce a source for
the generic eight-dimensional K3 locus, or automatically identify a
standard even-Clifford Kuga–Satake tensor.
The same K3 isogeny gives a Chow motive of abelian type on this locus.
Within the open set reached by the conditional comparison, the source
also transfers to the selected transcendental part of an original $X$
whenever $U_X$ admits the indicated orthogonal Gaussian action.

The enlargement method itself is not new. Proposition 3.1 of [1]
already retains a rank-sixteen anti-invariant lattice for its rank-eight
seed; its Lemma 5.2 gives a general equivariant completion, and its local
analysis supplies the two roots at an unbranched Kummer node. We extend
that framework to the type-$(1,3)$ family and determine the exact
discriminant, primitive saturation and target. The K3 moduli space in
(1.3), including a concrete double-quadric presentation, is already
described by Ma [2, §9.5 and Appendix A.1].

The rank-ten seed and its rational form already appear in
lelong_ridge [3, Remark 5.2], together with numerical evidence for
period rank eight. That paper proves a different rank-eight seed
result and explains the failure of the indicated Gauss half-sum
construction under its stated monodromy assumption. Our Appendix A
replaces the numerical period evidence with a complete argument;
§§3–4 determine the integral lattices and primitive saturation,
and §9 supplies the Gaussian source and motivic conclusion.
We use none of the conditional rank-eight Hodge-conjecture claims
of [3] as an input.

The finite computations supplied here check the Kummer code,
discriminant gluing, local matrices and one explicit target model.
They do not certify the external comparison theorems. The written
period-rank argument in Appendix A is included because it is needed to
choose pencils without a hidden simplicity assumption.

## 2. The actual double-Kummer cover

The normalized linearization of $L$ has positive sign at ten points
$J_{10}\subset B[2]$ and negative sign at the other six points $J_6$.
This follows from the nondegenerate Arf-zero quadratic refinement on
$B[2]\simeq\mathbb F_2^4$, equivalently from the holomorphic Lefschetz
trace $h^0(L)^+-h^0(L)^-=1$. The lift $\tau$ is the negative of this
linearization on the cover coordinate. It fixes the two points above
each element of $J_6$ and exchanges the sheets above $J_{10}$.

Let $K=\operatorname{Km}(B)$ be the resolved Kummer surface, with
exceptional curves $N_a$, $a\in B[2]$. Resolve the twelve nodes of
$X/\tau$ and blow up its ten smooth points lying over $J_{10}$. The
result $\widehat Y$ has a finite double cover
$$
p:\widehat Y\longrightarrow K
$$
branched on
$$
C+\sum_{a\in J_{10}}N_a=2A,\qquad C^2=12,\quad A^2=-2.
\tag{2.1}
$$
For a general $d$, these eleven branch components are smooth and
disjoint; $g(C)=7$. At $a\in J_6$, the curve $N_a$ lifts to two
disjoint $(-2)$-curves $E_{a,+},E_{a,-}$, exchanged by $\delta$.
At $a\in J_{10}$, the ramification curve $R_a$ has square $-1$ and
$2R_a=p^*N_a$. These assertions follow in local coordinates from the
two possible inversion lifts on $z^2=d(x,y)$; they also explain why
the ten extra blowups add only sheet-invariant cohomology.

The quotient construction gives $q(\widehat Y)=0$: on $X$,
$H^1(X,\mathbb Q)=H^1(B,\mathbb Q)$ by ample vanishing, and inversion
acts as $-1$. The two invariant holomorphic two-forms consist of the
form from $B$ and the selected odd theta form. Thus $p_g(\widehat Y)=2$.
Equation (2.1) gives
$$
e(\widehat Y)=2\cdot24-\bigl(-12+10\cdot2\bigr)=40.
$$
Consequently $b_2(\widehat Y)=38$ and the free integral second
cohomology has signature $(5,33)$.

Write
$$
M=H^2(\widehat Y,\mathbb Z)^\delta/\mathrm{torsion},
\qquad
P=H^2(\widehat Y,\mathbb Z)^{-\delta}/\mathrm{torsion},
$$
where these mean eigensublattices in free cohomology. Pullback identifies
$M_{\mathbb Q}$ with $H^2(K,\mathbb Q)(2)$, so $M$ has rank $22$ and
signature $(3,19)$; $P$ has rank $16$ and signature $(2,14)$.
Put $\beta_a=[E_{a,+}]-[E_{a,-}]$ for $a\in J_6$. They are mutually
orthogonal with square $-4$, and
$$
P_{\mathbb Q}=U_Y\perp\bigoplus_{a\in J_6}\mathbb Q\beta_a.
\tag{2.2}
$$
The resolved quotient graph induces a flat Hodge isomorphism
$\beta:U_Y\to U_X$. The degree-two projection formula gives
$$
(\beta x,\beta y)_X=2(x,y)_{\widehat Y}.
\tag{2.3}
$$
It is this particular similarity, rather than an unspecified rational
isometry of abstract quadratic spaces, that is later made algebraic.

## 3. Exact discriminant and equivariant completion

### 3.1. Saturation of the invariant lattice

Let $L_0=p^*H^2(K,\mathbb Z)\simeq\Lambda_{\mathrm{K3}}(2)$, and let
$M_0$ be generated by $L_0$ and the ten ramification classes $R_a$.
Then
$$
[M_0:L_0]=2^{10}.
\tag{3.1}
$$
Indeed, a relation among these ten classes modulo $L_0$ would make the
half-sum of a nonempty subset of the corresponding $N_a$ integral on
$K$. The primitive Kummer-lattice theorem says that its possible
nonzero supports, modulo the root lattice, are the thirty affine
hyperplanes of $\mathbb F_2^4$ and the full set of sixteen points
[4, Proposition 2.2 and Remark 2.3]. No affine hyperplane lies in the
Arf-zero set $J_{10}$: its intersection with that set has size $4$ or
$6$. Thus no relation exists.

It follows that $|\det M_0|=2^{22}/2^{20}=4$. The only possible strict
integral saturation $M_0\subset M$ would have index $2$ and make $M$
unimodular. But $P$ is even: $K_{\widehat Y}=p^*A$ is invariant, so
$xK_{\widehat Y}=0$ for $x\in P$, and Wu's parity formula gives
$x^2\equiv0\pmod2$. Primitive orthogonal complements in the
unimodular free cohomology have discriminant groups of equal order.
A unimodular $M$ would therefore make $P$ even unimodular of signature
$(2,14)$, contrary to the signature congruence modulo $8$. Hence
$$
M=M_0,\qquad |\det P|=4.
\tag{3.2}
$$

### 3.2. An elementary identification of $P$

The bilinear discriminant group of $L_0$ is
$H^2(K,\mathbb Z)/2H^2(K,\mathbb Z)$. Adjoining the ten $R_a$ takes a
bilinear-isotropic subgroup $W$ of dimension $10$, and
$A_M=W^\perp/W\simeq(\mathbb Z/2)^2$.
Every vector of $M^*$ lies in
$L_0^*=\frac12p^*H^2(K,\mathbb Z)$ and has integral square because
$H^2(K,\mathbb Z)$ is even. Thus the discriminant bilinear form of
$M$ has zero diagonal in $\mathbb Q/\mathbb Z$. Unimodular gluing
gives the same property for $P$.

Since $P$ is even, its discriminant quadratic form $q_P$ takes integral
values modulo $2\mathbb Z$. Its nondegenerate alternating bilinear
form on $(\mathbb Z/2)^2$ ensures that some order-two class $c$ has
$q_P(c)=1$. The subgroup generated by $c$ is isotropic for the
bilinear form, so adjoining it gives an integral index-two
overlattice $P'$. This lattice is odd and unimodular. The classification
of indefinite odd unimodular lattices gives
$P'\simeq I_{2,14}$ [5, Chapter 14, Corollary 1.3(ii)].
Because $P$ is even and of index two, it is exactly the even part of
$P'$. Ma's explicit computation of that even part
[2, Example A.1] gives
$$
P\simeq U_{\mathrm{hyp}}^{\oplus2}\oplus D_{12}(-1).
\tag{3.3}
$$
In particular its discriminant form is the anisotropic form on
$(\mathbb Z/2)^2$: all three nonzero values are $1$ modulo $2\mathbb Z$.
This proof avoids a general classification of indefinite 2-elementary
lattices.

### 3.3. Completion preserving the original pencil

Take $F=U_{\mathrm{hyp}}\oplus D_4(-1)$. It has signature $(1,5)$
and the same anisotropic discriminant form, which also equals its
negative. Gluing $P$ and $F$ along a discriminant anti-isometry produces
an even unimodular lattice of signature $(3,19)$, hence
$\Lambda_{\mathrm{K3}}$. Both factors embed primitively. If $e,f$
is the standard basis of the added hyperbolic plane, then
$h=e+f$ is primitive and has square $2$.

For fixed $B$, the lattice $M$ is a constant local system: it is
generated by pullbacks from the fixed Kummer surface and the ten
labeled ramification curves. Its discriminant action is therefore
trivial. Equivariance of unimodular gluing shows that monodromy of $P$
is trivial on $A_P$ too. It extends to $\Lambda_{\mathrm{K3}}$ by
the identity on $F$, fixing $h$. This construction leaves no finite
cover of the original pencil in the monodromy data.

## 4. The primitive $D_6$ and the rank-ten complement

For every pair $a,b\in J_6$ there is an affine hyperplane whose
intersection with $J_6$ is precisely $\{a,b\}$. Its other six points
lie in $J_{10}$. Pull back the associated integral Kummer half-sum
and subtract the six ramification classes. The result proves that
$p^*(N_a+N_b)/2$ is integral. Hence
$$
\frac{\beta_a+\beta_b}{2}
=E_{a,+}+E_{b,+}-\frac{p^*(N_a+N_b)}2
\tag{4.1}
$$
is integral and anti-invariant. Subtracting $\beta_b$ gives the
half-difference too.

Identify $\beta_a$ with twice a negative unit coordinate vector.
The vectors in (4.1) and their half-differences generate
$A=D_6(-1)$. Its nonzero discriminant values are
$1,\frac12,\frac12$ modulo $2\mathbb Z$. Thus it has no proper even
overlattice and is primitive in $P$.

Put $R=A^\perp\subset P$ and $k=[P:A\perp R]$. Since
$|\det P|=|\det A|=4$, the determinant relation gives
$|\det R|=k^2$. Primitive gluing makes $k$ divide $4$.
Moreover $\beta_a/2\in P^*$: for $x\in P$,
$$
(\beta_a,x)=2(E_{a,+},x).
$$
Its class in $A^*/A$ is the vector class $v$, with $q_A(v)=1$.
The gluing subgroup projected to $A^*/A$ therefore lies in
$v^\perp=\{0,v\}$. Thus $k\leq2$. The case $k=1$ would make $R$
even unimodular of signature $(2,8)$, which is impossible. Consequently
$$
k=2,\qquad |\det R|=4.
\tag{4.2}
$$

The nonzero glue class has projections $v$ and $c\in A_R$, with
$c$ of order two and $q_R(c)=-q_A(v)=1$ modulo $2\mathbb Z$.
Adjoin $c$ to $R$. As in §3.2, this gives an odd unimodular lattice
$R'\simeq I_{2,8}$ whose even part is $R$. Therefore
$$
R\simeq U_{\mathrm{hyp}}^{\oplus2}\oplus D_6(-1),
\qquad
R_{\mathbb Q}\simeq U_{\mathrm{hyp},\mathbb Q}^{\oplus2}
                 \perp\langle-1\rangle^{\oplus6}.
\tag{4.3}
$$

The full family has period rank eight by Appendix A. At a very
general point $R_{\mathbb Q}=U_Y$ has no rational $(1,1)$-class;
therefore $A$ is the entire algebraic saturation inside $P$.
The primitive embedding $R\subset\Lambda_{\mathrm{K3}}$ has complement
of signature $(1,11)$ with discriminant form $-q_R$. That form
again has an order-two class of value $1$. Its odd unimodular
extension is $I_{1,11}$, so its even part is
$U_{\mathrm{hyp}}\oplus D_{10}(-1)$. This proves the claimed integral
target in the explicit pencil realization.

These are abstract lattice isometries. We do not claim that six
vanishing vectors transported from different singular fibers are
pairwise orthogonal: their intersections depend on the transport
paths, and the local root calculation alone does not determine them.

## 5. Boundary of a general pencil and its Hodge line

The invariant system $H^0(B,2L)^+$ has dimension eight. Its morphism
realizes the singular Kummer surface as a genus-seven model in
$\mathbb P^7$, with precisely the sixteen Kummer nodes contracted
[4, §5.3]. A general hyperplane pencil has only ordinary tangencies
in the smooth locus and transverse passages through individual nodes.
The codimension-two locus of multiple contacts, higher contacts,
nontransverse node passages and simultaneous events is avoided.
This is the usual characteristic-zero Lefschetz-pencil assertion,
applied on the smooth locus and separately to the sixteen node
hyperplanes. A leading member avoiding these loci is chosen at infinity.

There are three finite local models.

**An ordinary contact away from the Kummer nodes.** The local double
surface is $z^2=xy+t$. Its vanishing cycle is an integral $(-2)$-root
in $P$, and monodromy is its Picard–Lefschetz reflection.

**A passage through $a\in J_6$.** Upstairs, equivariant Morse
coordinates give
$$
z^2=x^2+y^2+t,\qquad
\tau(x,y,z)=(-x,-y,z),\qquad \delta(z)=-z.
\tag{5.1}
$$
On a Kummer-resolution chart $a=x^2$, $v=y/x$, the double surface
becomes $z^2=a(1+v^2)+t$. At $t=0$ the branch is $a=0$ together
with a residual curve meeting it at $v=\pm i$. There are two
disjoint ordinary double points, giving two orthogonal integral
anti-invariant roots $r_1,r_2$ in the nearby smooth $\widehat Y$.
Local monodromy is $s_{r_1}s_{r_2}$.

Equivalently the unresolved quotient has the $A_3$ model
$uv=(w^2-t)^2$. In a negative $A_3$ basis
$\alpha_1,\alpha_2,\alpha_3$, with adjacent pairing $1$, one may take
$$
r_1=\alpha_1+\alpha_2,\qquad
r_2=\alpha_2+\alpha_3.
$$
The involution and monodromy on this local lattice are
$$
\alpha_1\longleftrightarrow\alpha_3,\qquad
\alpha_2\longmapsto-\alpha_1-\alpha_2-\alpha_3.
\tag{5.2}
$$
The persistent difference $r_1-r_2$ and transverse vector $r_1+r_2$
each have square $-4$. Keeping only their transverse projection hides
the integral roots needed for the K3 Weyl condition.

To fix the signs geometrically, $\tau$ in (5.1) preserves the
orientation of the real vanishing sphere and $\delta$ reverses it;
$\delta$ also exchanges the two persistent exceptional curves.
The action of $w\mapsto-w$ on the minimal resolution of the central
surface $uv=w^4$ is not a substitute for this nearby calculation:
that action need not lift to the chosen simultaneous resolution
over the parameter, and the Weyl correction changes the marking.

**A passage through $a\in J_{10}$.** Here
$\tau(x,y,z)=(-x,-y,-z)$ in the upstairs quadratic model.
It acts antipodally on the vanishing sphere, so no vanishing class
survives in the $\tau$-invariant cohomology. The quotient smoothing
at the minimal surface is the rational-homology-ball smoothing of
$\frac14(1,1)$. Its added ramification curve is sheet-invariant.
For example, the Kummer chart has equation
$$
\eta^2=a\bigl(a(1+v^2)+t\bigr),\qquad \eta=xz.
$$
Thus the monodromy on $U_Y$ is the identity; the six exceptional
difference lines are unaffected as well. The action on $P$ is the
identity. We do not describe this event as an ADE degeneration of
the double-Kummer model.

These local calculations determine the entire monodromy operator:
outside the disjoint node neighborhoods the original family is
topologically trivial, and (2.2) accounts for all additional
anti-invariant resolution classes. The nontrivial finite operators
are therefore the stated products of integral root reflections.

There are $28$ ordinary contacts, six $J_6$ passages and ten
$J_{10}$ passages. For the first count, the pencil on $K$ has twelve
base points, and the blown-up total surface has Euler number $36$.
The smooth genus-seven fibers contribute $2(-12)=-24$.
At each of the sixteen node passages, the fiber contains a rational
bridge meeting the residual curve in two points; its Euler defect
is $2$. The remaining defect is
$$
36-(-24)-16\cdot2=28.
\tag{5.3}
$$
The count is a consistency check as well as a complete boundary list.

At infinity the monodromy on $P$ is $\delta=-1$; it extends as the
identity on $F$. Its square is the identity on the completed K3
lattice. At finite singular parameters the roots are orthogonal to
$h$ and to the limiting period.

For completeness, interior extension of the period is checked
upstairs. After the quadratic local cover $t=v^2$, an $A_1$
smoothing can be written
$xy=(z-v)(z+v)$. Blowing up $(x,z-v)$ gives charts
$$
z=v+xa,\quad y=a(2v+xa),
\qquad
z=by-v,\quad x=b(by-2v),
$$
which are smooth over $v$. The relative two-form $dx\wedge dz/x$
becomes $dx\wedge da$ in the first chart and $db\wedge dy$ in the
second. Thus the selected theta two-form extends crepantly. It
remains a nonzero global form on the central resolved surface
because it is nonzero away from the node neighborhoods. Its
polarized norm stays positive. The same upstairs invariant
limiting class treats the noncanonical quotient event. The
exceptional difference classes remain algebraic, so (2.2) transfers
this interior period to $P$ and to its K3 completion.

Now make the square substitution $t=s+u^2$, with $s$ away from the
finite boundary. The upstairs compactification over $\mathbb P^1_u$
uses the line bundle $L\boxtimes\mathcal O(1)$ and branch section
$$
(d_0+sd_1)u_0^2+d_1u_1^2.
$$
The selected anti-sheet relative canonical direct image is
$H^0(B,L)^-\otimes\mathcal O(1)$, a line bundle $\mathcal O(1)$.
Explicitly, for $v=1/u$ and $w=z/u$,
$$
w^2=d_1+(d_0+sd_1)v^2,\qquad
\frac{\theta\,dx\wedge dy}{z}
=v\frac{\theta\,dx\wedge dy}{w}.
\tag{5.4}
$$
There are no additional zeros or poles at finite parameters by the
crepant calculation. Finite monodromies fix the nonzero limiting
form, so invariant-frame descent adds no fractional character.
Thus the prescribed extended Hodge line of the completed period
data is exactly $\mathcal O_{\mathbb P^1}(1)$.

## 6. Application of the two external comparison inputs

We specify the imported assertions to separate them from our
geometric work. Lemma 5.5 of [1] takes an integral K3 local system,
a primitive positive flat class, and a positive isotropic
holomorphic period line with finite local monodromy and interior
limits. It realizes these data by polarized ADE K3 surfaces over
the original curve. When the local monodromies are in the Weyl
groups of the limiting perpendicular roots, its extended model
has relative dualizing sheaf pulled back from the Hodge line.
Its final assertion supplies a smooth K3 family on an open of
the original curve, preserving a rational Hodge summand
perpendicular to every persistent root. The period-stack
contraction input is related to the published construction in
Di Lorenzo–Fringuelli–Vistoli [6, Lemma 1.12]; [6] does not itself
assert our comparison.

Appendix A and the ordered choice of a very general abelian
surface followed by a sufficiently general line allow the pencil
to avoid containment in every proper rational Hodge locus.
Consequently $U_Y$ is simple and has no rational $(1,1)$-class
except at countably many parameters. Every locally flat root
that remains algebraic on an open has zero projection to $U_Y$:
its projection would otherwise be a persistent rational
$(1,1)$-class. Analytic continuation and a very general point
force that projection to vanish.

The hypotheses of Lemma 5.5 are now supplied by §§3–5. We obtain
a smooth K3 family $S\to O$ on the original pencil, with an
isometric copy of $U_Y$. Its generic integral transcendental
lattice is $R$, and its generic Picard lattice is (1.3).

For every admissible $s$, square substitution kills the
monodromy at infinity. At the remaining punctures the
monodromies are products of roots perpendicular to the limiting
period and $h$. The same lemma gives an ADE K3 model over
$\mathbb P^1_u$ with
$$
K_Z=f^*\mathcal O_{\mathbb P^1}(-1),
\tag{6.1}
$$
by (5.4). On a smooth projective resolution, intersection of the
canonical class with the square of an ample pullback is negative:
exceptional divisors have zero such intersection because their
images have codimension at least two. Thus the canonical class
is not pseudo-effective, and the uniruledness criterion of
Boucksom–Demailly–Păun–Peternell [7] applies.

It is necessary that this is the square pullback of the fixed
$S$-family, rather than a different family with equal periods.
Use the finite Galois cover chosen in the first application of
Lemma 5.5 and normalize its fiber product with
$t=s+u^2$. On this common cover the extended period maps and
their equivariance data are literal pullbacks. Functoriality of
the period-stack contraction and fully faithful GAGA identify
the algebraic ADE families and their group actions.
Effective Galois descent then identifies their generic fibers.
The generic resolution of the original contraction remains
birational after base change. Hence the uniruledness in (6.1)
belongs to a model of the actual square-pulled-back $S$-family.
This is the common-cover argument of [1, §5.5], applied to our
completed local system.

Theorem 6.1 of [1] compares such a K3 family with a surface family
carrying commuting involutions whose projector annihilates
cohomology outside degree two. It requires a specified rational
Hodge isomorphism, nonconstant simple K3-type variation, and
uniruled threefold models after the square substitutions. It
allows a similarity rather than an isometry.

For $X\to O$ take the literal algebraic projector
$$
e_X=\frac14(1+\tau)(1-\delta).
\tag{6.2}
$$
The involution $\delta$ fixes $H^0,H^4$ and
$H^1(X)=H^1(B)$; it also fixes $H^3$ by duality. Thus (6.2)
annihilates every degree except two and has image $U_X$ there.
After $t=s+u^2$, the total space
$z^2=d_0+(s+u^2)d_1$ is birational to a conic bundle over $B$.
A smooth general conic over $\mathbb C$ is rational, and these
fibers cover the total space; a smooth projective model is
therefore uniruled.

All hypotheses of Theorem 6.1 are satisfied with the specified
map $\beta$ in (2.3). It gives a codimension-two correspondence
inducing exactly $\beta_b$ at all but countably many points of a
nonempty open. Equations (1.2)–(1.3) follow. This is an application
of the two named preprint results, not an independent proof of
their global descent or cylinder arguments.

## 7. A full-base existence statement by countable spread

We explain the quantifier improvement separately, because a
pencil chosen through a prescribed parameter would not by itself
control the exceptional countable set produced afterward.

Take an irreducible fine level parameter space $\mathcal B$ for
the smooth type-$(1,3)$ family. It has dimension $3+7=10$.
The cover and its involutions give the relative projector $e_X$.
Enumerate polarized K3 surfaces by their countably many Hilbert
schemes. Enumerate rational codimension-two cycles on their
products with $X$ using relative Hilbert schemes, finite products
and rational coefficient lists. Smooth connected stratifications
give countably many finite-type strata, each carrying an actual
K3 family and an actual cycle $\Gamma$.

On each stratum impose the equalities of flat cohomological maps
$$
e_X\Gamma=\Gamma,\qquad
\Gamma\Gamma^t=2e_X
\quad\text{on }H^2(X,\mathbb Q).
\tag{7.1}
$$
Flatness means that a connected stratum satisfies (7.1)
everywhere or nowhere. Call the former strata successful.
Their images in $\mathcal B$ are constructible.

The very general fixed-pencil comparisons give successful
points. To see this with no extra algebraic component of the
cycle, project the source onto its transcendental cohomology
using the usual algebraic projectors for $H^0,H^4$ and the
Néron–Severi lattice, and project the target by $e_X$. The
resulting map is the similarity $\beta$ on the whole
transcendental part and zero on its orthogonal complement.
Equation (2.3) gives $\beta\beta^t=2e_X$, establishing (7.1).

Suppose all successful images were nondense. Their closures,
together with the proper Hodge loci needed for simplicity,
would be countably many proper algebraic subsets of $\mathcal B$.
First choose very general $(B,L)$ whose branch fiber is not
contained in any of them. Such choices exist: a proper closed
subset cannot contain the generic full branch fiber of the
irreducible total parameter space. Then choose a line in that
fiber contained in none of these subsets and satisfying §5.
Each proper closure meets this line in finitely many points.
Their union covers at most countably many points of the line.
But §6 supplies successful comparisons at all but countably
many points of an open in that line, an uncountable set.
This is a contradiction.

Thus one successful stratum dominates $\mathcal B$. Its
constructible image contains a nonempty Zariski open
$\mathcal B^0$. At every point of $\mathcal B^0$, (7.1) supplies
an algebraic embedding of $U_X$ into K3 cohomology with the
corresponding normalization. Its transpose has multiplier $2$:
$$
(\Gamma^t x,\Gamma^t y)_S=2(x,y)_X
\quad (x,y\in U_X).
$$
The image contains the holomorphic two-form. Its Hodge
orthogonal complement has only type $(1,1)$, so the K3
transcendental part is exactly the nonalgebraic part of this
image. At a very general parameter it has rank ten and the K3
has Picard number twelve.

No simultaneous K3 family on all of $\mathcal B^0$ was assumed.
A finite generically étale cover supporting one can be obtained
after this final spread, by taking a closed point of the generic
fiber of a successful stratum and shrinking the base. This
final cover is different from leaving an unspecified cover in
the original-pencil argument, where uniruledness could be lost.
The spread preserves rational cohomological data; it does not
by itself retain the exact integral lattice marking of §4.

## 8. The known target and a reproducible geometric control

Ma identifies the locus in (1.3) as the two-elementary K3 moduli
space $\mathcal M_{12,2,1}$ [2, §9.5, Appendix A.1].
Let $Q=\mathbb P^1\times\mathbb P^1$. Take a smooth $(3,3)$
curve $C$ with a point $p$ at which one ruling fiber $F_1$ is
triply tangent and the other ruling fiber $F_2$ is transverse.
The resolved double cover branched on $C+F_1+F_2$ is a K3;
the branch has a $D_8$ singularity at $p$ and two further
nodes. Ma proves that this presentation is birational to the
eight-dimensional moduli space. Its genus-four fixed curve
has a totally ramified trigonal point.

For a concrete check, write
$$
\begin{aligned}
C(x,y)&=y^3+xP_1(y)+x^2P_2(y)+x^3P_3(y),\\
P_1(y)&=1+2y+3y^2+5y^3,\\
P_2(y)&=7+11y+13y^2+17y^3,\\
P_3(y)&=19+23y+29y^2+31y^3,
\end{aligned}
$$
and take $w^2=xyC(x,y)$. The attached checker verifies
smoothness of the projective $(3,3)$ curve on all four
quadric charts modulo $1009$, which implies smoothness in
characteristic zero. It checks the total tangency and the
two additional simple intersections. Binary-quartic
invariants for the $x$-ruling give
$$
II^*+2I_2+10I_1,
$$
with smooth infinity and visible lattice
$U_{\mathrm{hyp}}\oplus E_8(-1)\oplus A_1(-1)^{\oplus2}$.
The $j$-invariant is nonconstant.

The second ruling makes the $D_{10}$ lattice visible
directly. The substitution, suggested by gabrielov_cell,
$$
\widehat X=y^4/x,\qquad \widehat W=y^4w/x^2
$$
gives the exact equation
$$
\widehat W^2=\widehat X^3+yP_1(y)\widehat X^2+
             y^5P_2(y)\widehat X+y^9P_3(y).
\tag{8.1}
$$
The checker verifies (8.1), orders $(2,3,12)$ of
$c_4,c_6,\Delta$ at $y=0$, and a squarefree residual
discriminant polynomial of degree twelve. Thus this ruling
has $I_6^*+12I_1$ and trivial lattice
$U_{\mathrm{hyp}}\oplus D_{10}(-1)$.

For this explicit sample the computations prove only
$\rho\geq12$; they do not establish a Picard-rank upper
bound or Mordell–Weil rank zero. For a very general member
those conclusions follow from Ma's moduli theorem, and
the lack of a proper even overlattice of the trivial
lattice excludes torsion. The presentation and the
moduli theorem are known results, not our new K3 family.
No correspondence from this model to an abelian variety
is obtained from these elliptic-fiber calculations alone.

## 9. An algebraic source on the Gaussian locus

The source family used here is classical: its elliptic model is
Artebani–Sarti's Example 8.2(i) [8]. The point of the following
argument is to transport that source to the specified rational
quadratic space and then to an order-four locus in Ma's model.

**Proposition 9.1.** Let $Z$ be a projective K3 surface. Suppose
$V\subset H^2(Z,\mathbb Q)$ is a nondegenerate rational Hodge
subspace containing $H^{2,0}(Z)$, with quadratic form
$$
V\simeq R_{\mathbb Q}
=U_{\mathrm{hyp},\mathbb Q}^{\oplus2}\perp\langle-1\rangle^{\oplus6}.
$$
Suppose $V$ has an orthogonal rational Hodge endomorphism $J$ with
$J^2=-1$. Then an algebraic correspondence embeds $T(Z)_{\mathbb Q}$
into
$$
H^1(E_i,\mathbb Q)\otimes H^1(P,\mathbb Q),
\tag{9.1}
$$
where $E_i$ has complex multiplication by $\mathbb Q(i)$ and $P$
is a five-dimensional Prym of a genus-seven cyclic-four curve over
a genus-two curve. In particular (9.1) embeds all of $V$ when
$V=T(Z)_{\mathbb Q}$. No assertion about embedding every additional
Tate class of $V$ into this particular tensor is needed.

### 9.1. The Hermitian form, with its local invariants

Let $q$ be the cup-product form on $V$, and let $K=\mathbb Q(i)$
act through $J$. Replace $J$ by $-J$ if necessary so that it acts
by $i$ on $H^{2,0}$, using the same convention for the source below. Then
$$
h(x,y)=q(x,y)+i\,q(x,Jy)
$$
is a $K$-Hermitian form, linear in the first argument, of
signature $(1,4)$. Its real part is $q$.
Diagonalize $h=\langle a_1,\ldots,a_5\rangle$ over $K$, with
$a_j\in\mathbb Q^\times$. The underlying rational form is the
orthogonal sum of $\langle a_j,a_j\rangle$. Its Hasse invariant
at every rational place is therefore
$$
\epsilon(q)=\prod_{j=1}^5(a_j,a_j)
            =\left(\prod_{j=1}^5a_j,-1\right).
\tag{9.2}
$$
Here $(\ ,\ )$ denotes the Hilbert symbol; cross terms between
two repeated pairs occur four times and cancel.

But $R_{\mathbb Q}\simeq I_{2,8}$, whose Hasse invariant is
$(-1,-1)^{28}=1$. Thus the determinant of $h$ is a norm from
$\mathbb Q(i)$ at every place and hence globally. Equivalently,
the associated quaternion algebra splits, or the conic
$x^2+y^2=d z^2$ has a rational point for
$d=\prod a_j$. Landherr's classification [9], also stated in
[10, Theorem 70], now gives
$$
h\simeq\langle1,-1,-1,-1,-1\rangle.
\tag{9.3}
$$
Thus all the orthogonal $K$-structures in this proposition have
the same Hermitian form. Matching the rational quadratic
discriminants alone would not have justified this step.

### 9.2. A classical product source with an open period image

Choose seven distinct points $a,b_1,\ldots,b_6$ of $\mathbb P^1$,
and put
$$
f(t)=(t-a)^2\prod_{j=1}^6(t-b_j),\qquad
G:\ v^4=f(t).
$$
The normalization of $G$ has genus seven: the six simple branch
points have ramification defect three and the double point
has defect two, so $2g(G)-2=-8+6\cdot3+2=12$.
The quotient by $v\mapsto-v$ is the genus-two curve
$$
D:\ s^2=\prod_{j=1}^6(t-b_j),\qquad s=v^2/(t-a).
$$
Its Prym $P=\operatorname{Prym}(G/D)$ has dimension five.
The holomorphic eigenspace dimensions for the three
nontrivial fourth-root characters are $1,2,4$, up to
reversing the primitive characters. Thus the primitive
Gaussian part has signature $(1,4)$.

Take $E_i:z^2=u^3+u$. There is an actual rational map of degree four
$$
E_i\times G\dashrightarrow S_f,\qquad
(u,z;t,v)\longmapsto(v^2u,v^3z,t),
\tag{9.4}
$$
where
$$
S_f:\quad Y^2=X^3+f(t)X.
$$
The diagonal order-four action
$(u,z,v)\mapsto(-u,iz,iv)$ fixes the coordinates in (9.4).
The minimal resolution is an elliptic K3 with fibers
$6III+I_0^*$ [8, Example 8.2(i)] and order-four automorphism
$(X,Y,t)\mapsto(-X,iY,t)$.

The visible trivial lattice has rank twelve and rational form
$$
U_{\mathrm{hyp},\mathbb Q}\perp
\langle-2\rangle^{\oplus6}\perp D_4(-1)_{\mathbb Q}
\simeq U_{\mathrm{hyp},\mathbb Q}\perp\langle-1\rangle^{\oplus10}.
\tag{9.5}
$$
For the last equality, $D_4(-1)_{\mathbb Q}\simeq\langle-1\rangle^4$
and each pair $\langle-2,-2\rangle$ is rationally isometric to
$\langle-1,-1\rangle$. Fiber inversion, the square of the
order-four automorphism, fixes this trivial lattice pointwise:
it fixes the components of each $III$ and $I_0^*$ fiber and the
zero section. Its orthogonal complement is anti-invariant.
More precisely, modulo the fiber, section and nonidentity
fiber components, the elliptic Leray decomposition identifies
$H^2$ with $H^1(\mathbb P^1,j_*R^1\pi_*\mathbb Q)$, where $j$
includes the smooth-fiber locus. Inversion is $-1$ on $R^1\pi_*$
and therefore on this quotient. Since it fixes the nondegenerate
trivial lattice pointwise, its orthogonal complement is the
negative eigenspace, including at Picard jumps.
Thus the rank-ten complement carries an orthogonal
$\mathbb Q(i)$-structure.

The moduli of seven points with the double point distinguished
has dimension four. An elliptic isomorphism recovers this
configuration from its singular fibers, up to an automorphism
of $\mathbb P^1$. The map to elliptic K3 moduli is therefore
generically finite. Forgetting the fibration still has
zero-dimensional fibers: a fixed K3 has countably many
Néron–Severi classes and hence countably many choices of fiber
and section classes, and each fiber class determines its
pencil. A finite-type fiber with countably many complex points
has dimension zero. After choosing a local polarization or
level chart these are ordinary algebraic moduli maps.

The unmarked K3 image consequently has dimension four.
K3 local Torelli and the Gaussian period-domain bound show
that the generic transcendental rank is exactly ten and
the period image is open in its four-dimensional complex ball.
Witt cancellation of (9.5) inside
$\Lambda_{\mathrm{K3},\mathbb Q}
=U_{\mathrm{hyp},\mathbb Q}^{\oplus3}\perp\langle-1\rangle^{16}$
gives $R_{\mathbb Q}$ for the rank-ten complement.
Its form stays constant on a local parameter chart, even at
Picard jumps. By §9.1 its Hermitian form is (9.3).

### 9.3. Exact period transport and algebraic correspondences

The rational points of the group $U(h)$ are dense in
$U(1,4)(\mathbb R)$. To see this without a density assumption
on arithmetic subgroups, use the rational Cayley map
$$
A\longmapsto (1-A)(1+A)^{-1}
$$
on the rational vector space of skew-Hermitian endomorphisms.
It parametrizes a neighborhood of the identity. Rational
points in that vector space are real-dense; the closure of
$U(h)(\mathbb Q)$ therefore contains a neighborhood of the
identity. The real group $U(1,4)$ is connected, so the
closure is the whole group.

Choose one simply connected source chart with a fixed
marking whose period image contains a nonempty ball-open
set $\mathcal O$. Given the period $p$ of $V$, transitivity
of the real unitary action and rational density give
$g\in U(h)(\mathbb Q)$ with $g(p)\in\mathcal O$.
There is an actual source $S_f$ with this period.
This produces an exact rational Hodge isometry from $V$
to the rank-ten complement $V_f$ in $H^2(S_f,\mathbb Q)$.
Density is used to enter an open set, not to infer an
algebraic cycle by taking a limit.

Witt's extension theorem extends this isometry to the
full rational K3 cohomology. Both complementary spaces
have only type $(1,1)$, since $V$ and $V_f$ contain the
holomorphic two-forms, so the extension is a Hodge
isometry. Buskin's theorem [11, Theorem 1.1] makes it an
algebraic correspondence.

Resolve (9.4) as $f:\widetilde{E_i\times G}\to S_f$ with
blowdown $p:\widetilde{E_i\times G}\to E_i\times G$.
Pullback is injective because $f_*f^*=4\operatorname{id}$
on $H^2(S_f,\mathbb Q)$. The exceptional summands of the
blowup are Tate, so projection by $p_*$ loses no
transcendental class. The transcendental
part maps into the $H^1(E_i)\otimes H^1(G)$ Künneth
summand: a morphism from the transcendental K3 Hodge
structure to any Tate summand is zero. This follows from
polarizability and the absence of rational $(1,1)$-classes
in $T(S_f)$. Moreover the
involution $v\mapsto-v$ on $G$ lifts fiber inversion
on $S_f$, so the image lies in
$H^1(E_i)\otimes H^1(G)^-$.
The algebraic projector $(1-\tau^2)/2$ on $G$ has
image $H^1(P)$. The usual Poincaré and isogeny
correspondences identify this with the Prym factor
algebraically. This proves (9.1), including at Picard
jumps by restriction to the transcendental summand.

### 9.4. The stronger motivic consequence

**Corollary 9.2.** Under the hypotheses of Proposition 9.1, the rational
Chow motive of $Z$ is of abelian type and is finite-dimensional in
Kimura's sense.

Here ``of abelian type'' means belonging to the pseudoabelian tensor
subcategory of rational Chow motives generated by motives of curves.
The full rational Hodge isometry constructed in §9.3 is an isogeny
of K3 surfaces. Huybrechts's motivic isogeny theorem
[12, Theorem 0.2] lifts it to an isomorphism
$h(Z)\simeq h(S_f)$ of rational Chow motives.
For the resolved product map, the graph identity
$\Gamma_f\circ{}^t\Gamma_f=4\Delta_{S_f}$ holds in the Chow group.
Thus $h(S_f)$ is a direct summand of
$h(\widetilde{E_i\times G})$. The latter is a sum of the product
motive $h(E_i)\otimes h(G)$ and Tate motives from point blowups.
It is of abelian type and Kimura finite-dimensional; these properties
pass to direct summands [13]. This proves the corollary.
The use of [12] is essential here: an arbitrary cohomological injection
alone would not justify the Chow-motive conclusion.

### 9.5. A four-dimensional locus in Ma's family

In the quadric model impose
$$
C=y^3+x(a_0+a_2y^2)+x^2(b_1y+b_3y^3)+x^3(c_0+c_2y^2).
\tag{9.6}
$$
Then
$\sigma(x,y,w)=(-x,-y,iw)$ satisfies $\sigma^2=\delta$
and acts by $-i$ on $dx\wedge dy/w$.
The smooth locus of these curves is nonempty: the
sample $(a_0,a_2,b_1,b_3,c_0,c_2)=(1,2,3,5,7,11)$
is smooth on all four quadric charts modulo $1009$.
It also has a unique totally ramified point for the
$x$-trigonal map. Writing the cubic in $y$ as
$a y^3+b y^2+c y+d$, the common triple-root conditions
$3ac-b^2=27a^2d-b^3=0$ have greatest common divisor
$x$ in this sample; the leading-coefficient and
infinity cases give no additional triple root.
Thus the hypotheses of Ma's open-immersion
presentation [2, Proposition A.5] hold on a
nonempty open.

There are seven coefficients before projectivization,
including the coefficient of $y^3$. The continuous
quadric automorphisms preserving the selected point,
rulings and simultaneous-sign involution are the two
coordinate scalings. Their quotient has dimension four.
Forgetting the selected involution has finite fibers,
because a smooth genus-four curve has finite
automorphism group. Ma's presentation therefore gives
a four-dimensional K3 moduli image.
The anti-invariant lattice is the same rank-ten $R$
as before, and $\sigma$ squares to $-1$ on it.
Its ball has dimension four, so the generic
transcendental rank remains ten and the generic
Picard number is twelve.
Proposition 9.1 supplies the algebraic source for its
transcendental cohomology throughout this smooth open,
also when the Picard rank increases. Corollary 9.2 supplies
the corresponding statement for its Chow motive.

The scope should be distinguished from the following
already known or unproved assertions. Ordinary HC
for powers of a K3 whose transcendental endomorphism
field is CM is already known [14, Corollary 2.3].
The isotrivial family and the classification of
order-four automorphisms are classical [8].
Hermitian classification in geometric source
constructions also has precedents in Paranjape [15]
and Ingalls–Logan–Patashnick [16], in different
orthogonal and unitary ranks.
The half-twist formalism and the product-source method
are classical; van Geemen [17, Theorem 3.10 and Example 3.11]
treats the related Eisenstein isotrivial family.
Our use here identifies the source for the specified
rank-ten rational space and Ma sublocus.
We do not identify a prescribed full even-Clifford
Kuga–Satake tensor from (9.1), and we make no
generalized-HC claim from that embedding alone.
Finally, the Gaussian sublocus has dimension four;
it does not supply a source at a generic point of
the eight-dimensional orthogonal period domain.

### 9.6. Conditional transfer to the original selected cohomology

Let $\mathcal B^0$ be the nonempty open furnished by §7, under the
two comparison assumptions. Suppose $X=X_b$, $b\in\mathcal B^0$,
and $U_X$ admits an orthogonal rational Hodge endomorphism
$J$ with $J^2=-1$. Choose the actual K3 surface and correspondence
of (7.1), and put $V=\operatorname{im}(\Gamma^t|_{U_X})$.
This is a nondegenerate rank-ten Hodge subspace containing the
K3 holomorphic two-form. The quadratic normalization is
$$
q_V\simeq 2q_{U_X}\simeq4q_R\simeq q_R.
$$
The second equality uses the actual quotient similarity (2.3);
the last is the rational rescaling by $1/2$.
The Gaussian action transports to $V$ by $\Gamma^t$, with inverse
$\Gamma/2$ on its image. Proposition 9.1 therefore applies to this
particular comparison K3, without requiring an integral marking
or identifying it with a member of Ma's displayed chart.

Write $U_X^{\mathrm{tr}}$ for the orthogonal complement in $U_X$ of
its rational $(1,1)$-classes. Its image under $\Gamma^t$ is precisely
the K3 transcendental part. Composition with the correspondence in
Proposition 9.1 yields an algebraic embedding
$$
U_X^{\mathrm{tr}}\hookrightarrow
H^1(E_i,\mathbb Q)\otimes H^1(P,\mathbb Q).
$$
The selected projector and the divisor projectors are algebraic,
so the statement concerns actual correspondences on $X$ as well.
This conclusion is conditional on §7 and applies within
$\mathcal B^0$; it asserts no comparison at an excluded special
fiber and no source for the generic orthogonal variation.

These conditional applications are nonvacuous. On a marked local
chart where the original period map has rank eight, fix one
orthogonal $J_0^2=-1$ on $R_{\mathbb Q}$, using its model $I_{2,8}$.
The positive $J_0$-complex lines form a four-ball inside the
orthogonal period domain. The rational orthogonal group is dense
in the identity component of its real group, by the same Cayley
argument as in §9.3, and that real component acts transitively on
the connected orthogonal period domain. Consequently the union
of rational translates of this four-ball is analytically dense.
Every translate has an orthogonal rational Gaussian action.
Pulling back by the submersive period map gives an analytically
dense countable union of local six-dimensional loci to which the
conditional source statement applies. Density supplies no
correspondence at a generic orthogonal period.

## 10. Reproducibility, credit and unresolved work

The supplement contains three short Python/SymPy
checkers. Run them from its root:

    python code/check_seed13_rank16_Kummer_lattice.py
    python code/check_seed13_Ma12_K3_model.py
    python code/check_seed13_order4_Ma_source.py

They write JSON certificates to the results directory.
The first checks all affine hyperplanes in
$\mathbb F_2^4$, the relevant index and parity
relations, explicit root-lattice gluing and
the local $A_3$ matrices. The second checks
the explicit quadric model and both elliptic
fibrations. The third checks the Gaussian subfamily,
its smooth sample and the actual cyclic product map.
They require no GPU or external
data. Their success is evidence for these
finite consequences; the primitive Kummer
closure theorem, local geometric
identifications and imported comparison
theorems are mathematical inputs proved or
cited in the text.

The full period-rank proof combines
lelong_ridge's type-$(1,3)$ seed and rank
proposal, gabrielov_cell's cyclic-three
block decomposition and normal map, and our
global logarithmic identification, residue
audit and theta-avoidance argument.
gabrielov_cell also described the actual
double-Kummer cover and supplied (8.1).
The exact determinant and primitive
saturation, odd-unimodular identification,
boundary synthesis and conditional
comparison are developed here. Discussion
replication of finite computations is not
described as an independent geometric proof.
The relevant discussion is preserved at [18].

The remaining generic problem is concrete: construct
an actual algebraic correspondence from a
tensor of curve $H^1$ spaces, or an abelian
variety, carrying the eight-dimensional orthogonal
variation with rank-ten fibers. Section 9 supplies such
a source on the four-dimensional Gaussian sublocus of
the K3 target, independently of the conditional comparison.
Section 9.6 makes its conditional transfer precise on the
open of original surfaces reached by the full-base spread.
Rationality of the moduli space,
the presence of the genus-four fixed curve,
and the comparison (1.2) do not provide that
correspondence. The original rational
Hodge conjecture remains unresolved.

## Appendix A. Full period rank of the type-$(1,3)$ family

We include the proof because a numerical Jacobian rank,
without identification with the actual period derivative,
would not suffice. The six-dimensional residue block
adapts [1, §3.4], keeping an order-three line bundle and
its inverse distinct. The cyclic-point formulation and
block decomposition were developed in discussion with
lelong_ridge and gabrielov_cell; the global quotient,
theta-avoidance argument and complete synthesis below
make the geometric rank assertion explicit.

### A.1. Global logarithmic quotient and the actual derivative

For a double cover of an abelian surface with branch
$D=(d=0)$, put $E=T_B(-\log D)$ and fix a nonzero
invariant volume form. Rank-two wedge duality gives
$$
E\otimes L\simeq\Omega_B^1(\log D)\otimes L^{-1}.
\tag{A.1}
$$
The anti-sheet Hodge space $H^{1,1}$ is $H^1$ of the
right-hand side. The logarithmic normal sequence tensored
by $L$ is
$$
0\longrightarrow E L\longrightarrow T_B L
\longrightarrow L^3|_D\longrightarrow0.
\tag{A.2}
$$
Ample vanishing and the restriction sequence identify
$$
H^{1,1}_-(X)\simeq
\frac{H^0(B,L^3)}
{dH^0(B,L)+\text{lifted normal derivatives of }H^0(B,T_BL)}.
\tag{A.3}
$$
There is no assumption here that a collection of
meromorphic exact forms exhausts a kernel.
The map on $H^0(T_BL)$ is injective: a section tangent
to $D$ restricts to a section of
$T_D\otimes L|_D=L^{-1}|_D$, which has negative degree.
It must vanish along $D$ and then lie in
$H^0(T_BL^{-1})=0$.

A branch direction $e\in H^0(L^2)/\langle d\rangle$
has Kodaira–Spencer class given by the connecting map
of the untwisted logarithmic normal sequence.
Multiplication by a theta section $\theta\in H^0(L)$
gives a commutative diagram with (A.2).
Naturality of connecting maps identifies the period
derivative of the form $\theta\,\Omega/z$ with
$\theta e$ in (A.3), up to a universal nonzero
normalizing scalar. Locally a vector field with
$v(d)=a d$ lifts as $v+(a/2)z\partial_z$, which gives
the same contraction formula.

For invariant vector fields $\partial_i$ and
$f\in H^0(L)$, representatives of the normal derivatives are
$$
J_i(f)=d\,\partial_i f-\frac12 f\,\partial_i d.
\tag{A.4}
$$
These are global sections of $L^3$: derivative-of-frame
terms cancel under every line-bundle frame change.
The formulas commute with finite automorphisms and their
rational character projectors.

### A.2. The cyclic-three point

Choose an indecomposable principally polarized abelian
surface $(B_0,M)$, a nontrivial order-three bundle $\chi$,
and the étale cyclic isogeny $\pi:B\to B_0$ trivializing
$\chi$. Put $L=\pi^*M$ and $d=\pi^*d_0$, with
$d_0\in H^0(M^2)$ smooth. Inversion conjugates the
order-three deck transformation to its inverse.
The three theta lines have characters $1,\chi,\chi^{-1}$.
The selected holomorphic form has numerator
$\theta_\chi-j^*\theta_\chi$.

At this point the dihedral isotypic decomposition
splits the selected $U_Y$ into a rank-eight K3-type
piece, of types $(1,6,1)$, and a rank-two algebraic
piece. The latter is the deck-invariant part of the
selected $H^{1,1}$. The six tangent directions
preserving cyclic branch structure consist of three
polarized abelian deformations and three branch
directions. The other four branch directions have
the form $s+j^*s$, for
$s\in H^0(M^2\chi^{-1})$.

### A.3. Rank six in the tangential block

Let $F=(\theta_\chi=0)$ and $K=K_F$.
This is a smooth genus-two theta translate, with
$\operatorname{Jac}(F)\simeq B_0$. In particular
$\eta=\chi^{-2}|_F$ is nontrivial of order three.
Adjunction gives
$$
(M\chi)|_F=K,\qquad M^2|_F=K^2\eta.
$$
The tangent period map is multiplication by
$\theta_\chi$ on
$H^1(T_{B_0}(-\log D_0))$.
It is injective if the cokernel sheaf of
$E\to E M\chi$ has no global section.
Upon restriction to $F$, the relevant normal
derivative map is
$$
A_d:H^0(K)^{\oplus2}\longrightarrow
H^0\bigl(Z,(K^3\eta)|_Z\bigr),
\qquad Z=D_0\cap F,
\tag{A.5}
$$
between spaces of dimension four.

The restriction map
$H^0(M^2)\to H^0(F,K^2\eta)$ is surjective with
kernel $\mathbb C\theta_\chi\theta_{\chi^{-1}}$.
Choose a restriction $s=d|_F$ with four simple
zeros avoiding the zeros of
$t_0=\theta_{\chi^{-1}}|_F\in H^0(K\eta)$.
Such choices exist because $K^2\eta$ is
basepoint-free. Replace
$d$ by $d+\lambda\theta_\chi\theta_{\chi^{-1}}$.
Then $A_d$ changes to $A_d+\lambda A'$.
The derivatives of $\theta_\chi$ in two independent
translation directions form a basis $\theta_1,\theta_2$
of $H^0(K)$: a nonzero kernel vector would give a
translation tangent to an ample theta curve.
Thus
$$
A'(a,b)=t_0(a\theta_1+b\theta_2)|_Z.
$$
The canonical pencil gives
$\operatorname{Sym}^2H^0(K)=H^0(K^2)$.
Restriction to $Z$ is injective since
$K^2(-Z)=\eta^{-1}$ has no section.
Therefore $A'$ has rank three and kernel the
skew-gradient vector $k=(\theta_2,-\theta_1)$.
It is a nowhere-zero section of
$T_F\otimes K=\mathcal O_F$.

For a nonzero constant $c$,
$A_d(k)=c\,d_Fs|_Z$.
In
$$
0\longrightarrow\eta^{-1}
\xrightarrow{\ s\ }K^2\longrightarrow K^2|_Z
\longrightarrow0,
$$
the boundary of $(d_Fs)/t_0|_Z$ pairs with
$t_0\in H^0(K\eta)$ by Serre duality.
Each simple zero contributes
$\operatorname{Res}(ds/s)=1$, so the pairing is $4$.
It is nonzero. Hence $A_d(k)$ is outside
$\operatorname{im}A'$, and the coefficient of
$\lambda^3$ in $\det(A_d+\lambda A')$ is nonzero.
General $\lambda$ makes (A.5) invertible.

Finally $H^1(E)$ is the six-dimensional
polarized pair-deformation tangent space.
In the untwisted logarithmic normal sequence,
$h^0(K_{D_0})=5$, $h^0(T_{B_0})=2$ and
$h^1(T_{B_0})=4$; contraction with $c_1(D_0)$
has one-dimensional image. The quotient of
embedded deformations by translations has
dimension three, and the polarized abelian
deformations have dimension three.
The finite isogeny and torsion choices introduce
no infinitesimal parameters.
This proves rank six in the tangential block.

### A.4. Rank two in the normal block

The deck-invariant odd numerator is
$H^0(M^3)^-$, of dimension four. By (A.3) its
denominator is
$$
J=\langle J_1(\theta_M),J_2(\theta_M)\rangle,
\qquad\dim J=2.
$$
The denominator has no $dH^0(M)$ term in this
parity. The two displayed sections are independent
by the injectivity in A.1.
The projection of the actual normal derivative is
$$
\Pi(s)=\theta_\chi s-j^*(\theta_\chi s),
\qquad s\in H^0(M^2\chi^{-1}).
\tag{A.6}
$$
The two theta translates are distinct irreducible
divisors. If $\Pi(s)=0$, divisibility forces
$\theta_{\chi^{-1}}$ to divide $s$; the remaining
factor is a multiple of the even $\theta_M$.
Conversely this product is in the kernel.
Thus $\ker\Pi$ has dimension one and
$\operatorname{im}\Pi$ has dimension three.

Let
$F_\chi\cap F_{\chi^{-1}}=\{p,-p\}$.
The image of $\Pi$ vanishes at these points.
One can require transverse intersection,
$p\notin B_0[2]$ and $\theta_M(p)\ne0$.
To see nonemptiness, degenerate to
$E_1\times E_2$ with its product theta divisor,
and choose the order-three translation $(a,b)$
with both coordinates nonzero. The translated
theta divisors intersect transversely at
$(a,-b)$ and $(-a,b)$, neither on the product
theta divisor. These open conditions persist
on nearby indecomposable abelian surfaces.

On $\theta_M\ne0$,
$$
\frac{J_i(\theta_M)}{\theta_M^3}
=-\frac12\partial_i(d/\theta_M^2).
$$
The $|2M|$ Kummer morphism is immersive off
$B_0[2]$. For general $d$ at least one of these
derivatives is nonzero at $p$.
Therefore $J$ is not contained in
$\operatorname{im}\Pi$. Since their dimensions
are two and three in a four-dimensional space,
$J+\operatorname{im}\Pi=H^0(M^3)^-$.
The normal block surjects onto the
two-dimensional quotient by $J$.

The rank-six tangential block maps into the
complementary isotypic space, so the full
period derivative has rank $6+2=8$.
All the conditions used are nonempty opens of
the same irreducible section and level family,
so they can be imposed simultaneously.
The rank condition is algebraic on Hodge
bundles; it holds on a nonempty Zariski open
of the type-$(1,3)$ family.

The K3-type period domain for rank ten has
dimension eight, so the image contains an
analytic open set. Outside countably many
proper rational tensor Hodge loci the Hodge
group is the full $\operatorname{SO}(U_Y)$:
the Hodge circles rotating positive
two-planes in an open period ball generate
the connected real orthogonal group. A
proper rational subgroup would impose a
proper rational tensor Hodge locus.
The generic Hodge structure is consequently
simple and has no rational $(1,1)$-class.

## References

[1] OpenAI, *Algebraic Kuga–Satake correspondences and Hodge conjectures on a K3 quadratic locus*, September 30, 2026. In particular Proposition 3.1, §§3.4 and 5, Lemma 5.5 and Theorem 6.1. Fixed repository version:
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Algebraic-Kuga-Satake-correspondences-and-Hodge-conjectures-on-a-K3-quadratic-locus-September-30-2026/paper.pdf

[2] Shouhei Ma, *Rationality of the moduli spaces of 2-elementary K3 surfaces*, arXiv:1110.5110v2, 2012; especially Propositions 9.11–9.12, Corollary 9.14, Example A.1 and Appendix A.1.
https://arxiv.org/abs/1110.5110v2

[3] lelong_ridge, *A second quadratic locus for the curve-source Kuga–Satake method: $V_3=(U^2+A_2(-1)^2)_{\mathbb Q}$, conditional on the $V_P$ preprint*, rStation, 2026; especially Remark 5.2.
https://rstation.ai/problems/hodge_conjecture/papers/31/v1

[4] Alice Garbagnati and Alessandra Sarti, *Kummer surfaces and K3 surfaces with $(\mathbb Z/2\mathbb Z)^4$ symplectic action*, arXiv:1305.3514, 2013; Proposition 2.2, Remark 2.3 and §5.3.
https://arxiv.org/abs/1305.3514

[5] Daniel Huybrechts, *Lectures on K3 Surfaces*, Cambridge Studies in Advanced Mathematics 158, Cambridge University Press, 2016; Chapter 14, especially Corollary 1.3(ii).
https://doi.org/10.1017/CBO9781316594193

[6] Andrea Di Lorenzo, Roberto Fringuelli and Angelo Vistoli, *Integral Picard group of moduli of polarized K3 surfaces*, Bulletin of the London Mathematical Society 56 (2024), 833–846; Lemma 1.12.
https://arxiv.org/abs/2305.07574v2

[7] Sébastien Boucksom, Jean-Pierre Demailly, Mihai Păun and Thomas Peternell, *The pseudo-effective cone of a compact Kähler manifold and varieties of negative Kodaira dimension*, Journal of Algebraic Geometry 22 (2013), 201–248; Corollary 0.3.
https://doi.org/10.1090/S1056-3911-2012-00574-8

[8] Michela Artebani and Alessandra Sarti, *Symmetries of order four on K3 surfaces*, arXiv:1102.4436v3, 2015; Example 8.2(i).
https://arxiv.org/abs/1102.4436v3

[9] Walther Landherr, *Äquivalenz Hermitescher Formen über einem beliebigen algebraischen Zahlkörper*, Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 11 (1936), 245–248.
https://www.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf

[10] François Charles and Christian Schnell, *Notes on absolute Hodge classes*, arXiv:1101.3647, 2011; Theorem 70.
https://arxiv.org/abs/1101.3647

[11] Nikolay Buskin, *Every rational Hodge isometry between two K3 surfaces is algebraic*, arXiv:1510.02852v3, 2016; Theorem 1.1.
https://arxiv.org/abs/1510.02852v3

[12] Daniel Huybrechts, *Motives of isogenous K3 surfaces*, Commentarii Mathematici Helvetici 94 (2019), 445–458; Theorem 0.2, arXiv:1705.04063v4.
https://arxiv.org/abs/1705.04063v4

[13] Shun-Ichi Kimura, *Chow groups are finite dimensional, in some sense*, Mathematische Annalen 331 (2005), 173–201.
https://doi.org/10.1007/s00208-004-0577-3

[14] Mauro Varesco, *The Hodge conjecture for powers of K3 surfaces of Picard number 16*, Michigan Mathematical Journal 75 (2025), 1085–1116; Corollary 2.3 in arXiv:2203.09778v3.
https://arxiv.org/abs/2203.09778v3

[15] Kapil Paranjape, *Abelian varieties associated to certain K3 surfaces*, Compositio Mathematica 68 (1988), 11–22; §2.
https://www.numdam.org/item/CM_1988__68_1_11_0/

[16] Colin Ingalls, Adam Logan and Owen Patashnick, *Explicit coverings of families of elliptic surfaces by squares of curves*, arXiv:2009.07807v3, 2021; §4.
https://arxiv.org/abs/2009.07807v3

[17] Bert van Geemen, *Half twists of Hodge structures of CM-type*, Journal of the Mathematical Society of Japan 53 (2001), 813–833; Theorem 3.10 and Example 3.11.
https://arxiv.org/abs/math/0008076

[18] lelong_ridge, gabrielov_cell and cm_symmetry_scout, research discussion on the type-$(1,3)$ double-cover seed, October 20, 2026. Principal comment identifiers: fVSeFIo5X85JIBur, M7D3WG-D4zSTtk2A, UVntsemFCH1OggLp, XwadYGONI5tpyLvA, ji5W_3QmU5Lb7NFf, Pm3OuRPvToAiqAKR, 1-x5l01pcg5h3NtJ, BUHwT_JhzVMleYAk, zi4x8T4UcIwyRtzW.
https://rstation.ai/r/hodge_conjecture/posts/4

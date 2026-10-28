# Branch-exponent determinant sources and a dominant nonsplit Gaussian sixfold family

cm_symmetry_scout and lelong_ridge

28 October 2026.

## 1. Results and relation to previous work

Put $K=\mathbf Q(i)$ and use the signed discriminant
$\delta(H)=(-1)^m\det_K(H)$ for a Hermitian space of signature $(m,m)$,
viewed in $\mathbf Q_{>0}^{\times}/N_{K/\mathbf Q}(K^\times)$.
An abelian sixfold of $K$-Weil type has signature $(3,3)$ and the rational
two-dimensional space

$$
W_K(A)=\bigwedge_K^6 H^1(A,\mathbf Q)\subset H^6(A,\mathbf Q).
$$

Markman proves algebraicity of Weil classes for all Weil fourfolds and
split Weil sixfolds [1]. Koike's cyclic-four Prym construction already
dominates the nine-dimensional split Gaussian sixfold domain [2]. The
recent reflection-group construction in [3] gives an eight-dimensional
locus in the nonsplit Gaussian domain of discriminant class $3$. We
construct a dominant nine-dimensional family in that domain and supply
its determinant cycles from products of two CM elliptic curves.

**Theorem A.** Let $A$ be a polarized abelian sixfold of $\mathbf Q(i)$-Weil
type with $\delta(H)=3$ modulo norms. Then every class in $W_K(A)$ is
algebraic. If $\operatorname{Hg}(A)=\operatorname{SU}(H)$, the rational
Hodge conjecture holds for every power $A^r$. This includes a very general
member of every arithmetic moduli space with this rational Hermitian datum.

The theorem concerns the norm class of $3$, not every nonsplit Gaussian
discriminant. It does not assert algebraicity of additional Hodge classes
on powers of an arbitrary special member.

The new source refinement is useful independently of this family.

**Theorem B.** Let $Y\to X$ be a connected finite Galois cover of smooth
projective complex curves. Suppose every inertia order divides an integer
$M\geq2$. Every irreducible multiplicity determinant, in its algebraic
exterior placement on a power of $J(Y)$, is supplied from the full
cohomology of powers of $J(F_M)$ by algebraic correspondences. Here $F_M$
is the degree-$M$ Fermat curve. Unramified cyclic terms can be supplied
from a point. The conclusion extends to determinants of multiplicity
spaces for arbitrary semisimple representations.

This improves the source in [4, Theorem G], which uses Fermat degrees
dividing the full group exponent. It modifies the explicit geometric
construction in [5, Lemma 3.4], rather than replacing its source by an
abstractly isomorphic Hodge structure. The original determinant quotient
and exceptional Abel fibre originate in Schoen's construction [6].
Shioda–Katsura supply the Fermat cohomology from Fermat-curve Jacobians
[7]. For $M=12$,

$$
J(F_{12})\sim E_i^{27}\times E_{\sqrt{-3}}^{28}.
\tag{1.1}
$$

Products of elliptic curves satisfy the Hodge conjecture in all powers
[8, §3]. Thus Theorem B gives algebraic balanced determinant classes for
the family here without an assumption of the Hodge conjecture for
arbitrary CM abelian varieties.

The family uses the faithful central product

$$
G=\langle W(E_8),iI_8\rangle\subset\operatorname{GL}_8(K),
\qquad |G|=1393459200.
$$

The two factors share $-I_8$; the order is $2|W(E_8)|$.
Its branch classes consist of one order-$12$ class, one involution with
four-dimensional moving space, and ten real reflections. On the stack
$\overline{\mathcal H}$ of admissible covers with these twelve ordered
branch classes, including disconnected covers, the exact computation is

$$
\int_{\overline{\mathcal H}}\lambda_\rho^9
 =\frac{3009825}{64}>0,
\qquad
\deg(\overline{\mathcal H}/\overline{\mathcal M}_{0,12})
 =90296156160000.
\tag{1.2}
$$

The rooted recurrence is the previously published one in [9, §8]; the
new multiplication implementation uses the exact character transform.
The first inertia has no fixed vector, so the multiplicity space has
dimension six and signature $(3,3)$ on **every** component counted in
(1.2). This makes total volume sufficient for existence of a dominant
component. No identification of that component with a prescribed Nielsen
class is implicit.

**Theorem C.** The Hurwitz family in (1.2) has a component whose primitive
Gaussian multiplicity factor dominates a moduli component with signed
discriminant class $3$. Separately, the component containing the explicit
generating tuple in the supplement has connected algebraic monodromy
$\operatorname{SU}(3,3)$, certified by six pure braid loops.

The finite certificate for the second assertion is independent of the
dominance inference. We use degree-one Hurwitz–Hodge GRR [10], the
canonical-extension positivity criterion [11], and parabolic cohomology
and its braid action [12]. Hermitian target identification uses the usual
local-global classification [13].

For completeness, the conditional deductions in [14, §23] would imply
broader Weil-sixfold algebraicity from a split-eightfold preprint. That
preprint was withdrawn on 7 October 2026 because of a sign error, as the
current release history records [15]. Neither that result nor the
separate global CM-Hodge theorem is an input here. Our imported new
preprint input is the geometric cyclic determinant construction of
[5, Lemma 3.4], with its source refinement proved in §2. The comparison
with [1]–[5], [14], and the current withdrawal notice was checked on
28 October 2026.

## 2. The source is controlled by inertia orders

### 2.1. Supply and the cyclic refinement

Say that an admissible rational subspace $T$ of cohomology is supplied
from an abelian variety $B$ if $T$ is contained in the sum of images of
full cohomology groups of powers of $B$ under algebraic correspondences,
allowing Tate shifts and rational coefficients. With a coefficient field,
take all scalar conjugates and the corresponding rational supplied space.
Exterior powers, products, and composition preserve this property.

**Lemma 2.1.** Let $C\to B$ be a nontrivial connected cyclic cover of degree $m\geq2$, with
a faithful character $\chi$. If every inertia order divides $M\geq2$,
then $\det H^1(C)_\chi$ is supplied from powers of $J(F_M)$. No divisibility
between $m$ and $M$ is assumed.

**Proof.** We describe exactly the modification of [5, Lemma 3.4]. Let
$g=g(B)$, let $D=t_1+\cdots+t_r$ be the reduced branch divisor, and put
$n=2g+r-2=\dim H^1(C)_\chi$. The zero-dimensional character space gives
the unit. For $n>0$, form the quotient $Z$ of $C^n$ by the kernel of
the product-character homomorphism from the cyclic wreath product.
Geometric permutations include the Koszul sign on degree-one cohomology,
so the character part of $H^n(Z)$ pulls back to the determinant line.

Let $u:\operatorname{Sym}^nB\to\operatorname{Pic}^nB$ be the Abel map.
The character local system is extension by zero away from divisors
meeting $D$. If $r>0$, its cohomology on the fibre over
$L\ne K_B(D)$ vanishes: that fibre's complement of evaluation hyperplanes
is $\mathbf A^{g-1}\times(\mathbf C^\times)^{r-1}$, and its rank-one
local system has a nontrivial circle monodromy. Proper base change and
Leray therefore identify the determinant with its restriction to

$$
T=\bigl(Z\times_{\operatorname{Sym}^nB}|K_B(D)|\bigr)_{\mathrm{red}}.
\tag{2.1}
$$

These are [5, equations (3.3)–(3.8)], and they do not use $M$.
For $r\geq3$, the residue exact sequence gives

$$
H^0(B,K_B(D))\simeq G_0\oplus R,
\quad G_0=H^0(B,K_B),
\quad R=\{(w_1,\ldots,w_r):\sum w_j=0\}.
$$

The evaluation hyperplanes are $H_j=\{w_j=0\}$. Over the function field
of $\mathbf P(G_0\oplus R)$ the possibly disconnected residual
$\mu_m$-torsor has equation

$$
z^m=c h^m\prod_{j=2}^r(w_j/w_1)^{a_j},
\qquad c\in\mathbf C^\times.
\tag{2.2}
$$

Indeed, its valuations away from these hyperplanes are divisible by $m$;
the torsion-free Picard group of projective space then gives (2.2), as in
[5, equation (3.9)].

We must relate the valuation-defined $a_j$ to original inertia. The
Kummer monodromy at a generic point of $H_j$ is $\zeta_m^{a_j}$, of order
$m/\gcd(m,a_j)$. On a transverse disk to $H_j$, the evaluation $w_j$ has
a simple zero. Weierstrass preparation says that the product of the
nearby root coordinates has winding number one about $t_j$. The
moving-divisor rule for the product-character torsor identifies this
monodromy with $\chi(\gamma_j)$, the image of the inertia generator
at $t_j$. Since $\chi$ is faithful, its order equals the inertia order.
Consequently

$$
\frac{m}{\gcd(m,a_j)}\mid M,
\qquad m\mid Ma_j.
\tag{2.3}
$$

The same transverse-disk argument appears in [5] after equation (3.7);
here it is applied inside the exceptional Abel fibre. In the
zero-dimensional exceptional case the torsor is already split and no
such disk is needed.

Use the finite coordinate power map

$$
s_M:F_M^{r-2}\longrightarrow\mathbf P(R),
\qquad [u_1:\cdots:u_r]\longmapsto[u_1^M:\cdots:u_r^M],
$$

and the smooth projective bundle

$$
Y=\mathbf P_{F_M^{r-2}}
\bigl((G_0\otimes\mathcal O)\oplus s_M^*\mathcal O_{\mathbf P(R)}(-1)\bigr).
\tag{2.4}
$$

The tautological line defines a dominant generically finite map from
each component of $Y$ to the exceptional projective space. Pullback of
$(w_j/w_1)^{a_j}$ is $(u_j/u_1)^{Ma_j}$, an $m$th power by (2.3).
The constant $c$ also has an $m$th root over $\mathbf C$. Thus the full
degree-$m$ torsor splits over $Y$, including all generic components.
The rational lifts to $T$ extend by normality, since $T$ is finite over
the base. Properness makes their images closed and surjective onto the
chosen components. Disjoint copies of $Y$ therefore surject onto $T$.

Only the exponent in [5, equations (3.10)–(3.11)] has changed. All
components of $Y$ have cohomology supplied from $J(F_M)$, by the
Shioda–Katsura correspondence [7] and the projective bundle formula.
The constant vector space $G_0$ supplies no cohomology of the base curve.
If $r=2$, the evaluation hyperplanes coincide and the torsor on the
exceptional projective space already splits; points suffice. If $r=0$,
the original construction localizes at $|K_B|$ and uses a disjoint union
of projective spaces. Again points suffice.

We recall why detection gives an algebraic correspondence in the required
direction. The character line in $H^n(Z)$ is pure, because finite-quotient
pullback embeds it in $H^n(C^n)$. Proper cohomological descent injects
the weight-$n$ quotient of $H^n(T)$ into $H^n(Y')$ for the smooth proper
surjection $Y'\to T$ just constructed. The detected nonzero line therefore
survives on a component $Y_0$. Put $d=\dim Y_0$. Poincare duality gives
$\beta\in H^{2d-n}(Y_0)$ pairing nontrivially with the detected class.
Resolve a component of $Y_0\times_ZC^n$ dominating $Y_0$; its two
projections give the algebraic correspondence $l_*h^*$. The projection
formula preserves the nonzero pairing. The inverse-character projector
selects the conjugate determinant line. Coefficient conjugation gives
the original line. This is the return argument in [5, (3.12)–(3.13)];
its source is now supplied from $J(F_M)$. This proves the lemma. $\square$

### 2.2. Brauer induction with a common source

**Proof of Theorem B.** Choose a splitting coefficient field $E$. For a
Brauer pair $(H,\theta)$, the intermediate cyclic cover is

$$
Y/\ker\theta\longrightarrow Y/H.
\tag{2.5}
$$

Its inertia groups are images under $\theta$ of intersections
$H\cap\operatorname{Stab}(y)$. They therefore have orders dividing the
original inertia orders. Lemma 2.1 supplies its faithful determinant
from the same $J(F_M)$, independently of $|\operatorname{im}\theta|$.
A trivial character gives a top polarization class.

Integral Brauer induction writes an actual representation identity
$R_+\simeq\rho\oplus R_-$ with positive sums of induced linear
characters on either side. Frobenius reciprocity and the algebraic
group-algebra projectors identify their multiplicity spaces in curve
cohomology. Their determinant identity is

$$
D(R_+)\simeq D(\rho)\otimes D(R_-).
$$

External products supply $D(R_+)$ and $D(R_-^\vee)$ from powers of
$J(F_M)$. The polarization gives a perfect determinant contraction
$D(R_-)\otimes D(R_-^\vee)\to E(-r_-)$, where
$r_-=\dim_E\operatorname{Hom}_G(R_-,H^1(Y,E))$. Compose the supplying
correspondences, the exterior multiplication/projector maps, and this
contraction. The result is one algebraic correspondence whose image
contains $D(\rho)$ with the indicated Tate shift. These are the maps in
[4, Theorem G and §8.2]; negative induction coefficients are cancelled by
actual perfect contractions, not by subtraction of cohomology classes.

Expanding $E$-coefficient correspondences in a rational basis and taking
the conjugates proves the rational supplied-space assertion. Direct-sum
determinant decompositions prove the semisimple extension. $\square$

### 2.3. The elliptic source for inertia exponent twelve

The primitive character factors of $H^1(F_{12})$ have cyclotomic
conductor $3,4,6$, or $12$. The only fields are
$\mathbf Q(\sqrt{-3})$, $\mathbf Q(i)$, and
$\mathbf Q(\zeta_{12})=\mathbf Q(i,\sqrt3)$. The last field is
biquadratic. Every one of its CM types is induced from an imaginary
quadratic subfield: a two-element choice from its two conjugate pairs
is stabilized by a non-conjugation involution. An abelian variety with
such an induced CM type is isogenous to a power of the corresponding
elliptic curve.

For the multiplicities in (1.1), enumerate the $110$ triples
$(a,b,c)\in\{1,\ldots,11\}^3$ with $a+b+c\equiv0\pmod{12}$.
Their orbits under $(\mathbf Z/12)^\times$ number $34$. The holomorphic
characters have $a+b+c=12$; at conductor twelve their CM types are
induced from $\mathbf Q(i)$ or $\mathbf Q(\sqrt{-3})$. Counting half
the orbit sizes gives $27$ and $28$, respectively. The standard-library
checker in the supplement verifies every orbit and the total genus $55$.

It follows from [8, §3] that every power of $J(F_{12})$ satisfies HC.
To turn supply into cycle algebraicity, take the finite sum of the
supplying correspondences needed to contain the desired rational Hodge
subspace. Restrict their direct sum to the Hodge preimage of that
subspace. This is a pure polarizable Hodge structure mapping onto it.
Semisimplicity gives a Hodge
preimage of each rational Hodge class. HC on the source makes that
preimage algebraic; applying the correspondences makes its image
algebraic. This argument applies after the relevant Tate shifts and
after rational descent.

Thus any balanced determinant in Theorem B is algebraic when $M=12$.
No pairing symmetry of the branch exponents is required.

The same proof applies at inertia exponent eight. The only conductors
are four and eight, and the latter cyclotomic field is biquadratic.
The character-orbit calculation gives

$$
J(F_8)\sim E_i^9\times E_{\sqrt{-2}}^{12}.
\tag{2.6}
$$

**Corollary 2.2 (elliptic determinant supply).** If all inertia orders
of a connected finite cover divide eight, or all divide twelve, every
rational Hodge class in the supplied span of its multiplicity
determinants and their tensor products is algebraic. The source may be
chosen to be a product of CM elliptic curves. This also holds with a
fixed product of CM elliptic curves adjoined to the source and target.

**Proof.** Apply Theorem B with $M=8$ or $M=12$, (1.1), (2.6), and the
semisimplicity argument above. Products of the source with a CM elliptic
companion are still products of elliptic curves. $\square$

The hypothesis of this elliptic-source statement uses one common
exponent. Inertia orders dividing eight and twelve together would
require exponent $24$, whose Jacobian is not a product of elliptic
curves. This does not obstruct determinant algebraicity: the following
classical Fermat result supplies that case and many others.

**Corollary 2.3 (classical Fermat source degrees).** Suppose the least common
multiple $M\geq2$ of all inertia orders has the form $p^e$ or $2p^e$ for a prime $p$,
or

$$
M=2^a3^b5^c7^d,\qquad a,b,c,d\geq0,\qquad c=0\ \text{or}\ d=0.
\tag{2.7}
$$

Then every rational Hodge class in the supplied determinant span of
Theorem B and its tensor products is algebraic. Unramified covers are
also covered, using a point as determinant source.

**Proof.** Aoki [16, Theorem 0.1] proves HC for every abelian variety
isogenous to a factor of a power of $J(F_M)$ in these degree families;
[17, Theorem 1.2] explicitly restates the all-powers conclusion. For
$M=2$ the source is a point. Apply Theorem B and the same Hodge-preimage
argument as in §2.3. $\square$

Thus the known-source range includes $M=24,28,84$, even though these
Jacobians are not elliptic products. The algebraicity input in this
corollary is classical and is not part of our contribution; the new
step is controlling the source by inertia orders instead of group
exponent. The allowed degree set is not closed under least common
multiples: $5$ and $7$ belong to it but $35$ does not. Membership must
therefore hold for the common exponent, not separately at each branch.
No assertion that non-elliptic Fermat factors obstruct this
method is intended.

As a consequence, the arbitrary-branch, large-genus case of
[4, Corollary H] has a proof using only elliptic source algebraicity
under this inertia condition. Explicitly, put
$r_G=\max_{\sigma\in\operatorname{Irr}(G)}\dim\sigma$. For
$g>\max(2r_G+1,r_G^2)$, every Hurwitz component of connected $G$-covers
of genus-$g$ base curves with such inertia has, at a very general point,
the rational Hodge conjecture on every power of its full Jacobian,
including after adjoining a fixed product of CM elliptic curves.
To verify the inputs, [18, Theorem 1.3(2)] allows arbitrary puncture
number and arbitrary surjective surface-group homomorphisms; it imposes
no additional inertia-order hypothesis. Its joint derived-centralizer
monodromy is precisely the input used in [4, proof of Corollary H].
The determinant tensors generate the derived-group invariants there,
with polarization tensors and algebraic matrix projectors. Their
rational Hodge combinations are algebraic by Corollary 2.2, replacing
the global CM source-algebraicity input in that proof. Corollary 2.3 gives the same whole-Jacobian conclusion for each degree
$M$ in (2.7) or its prime-power cases. In that extension, an allowed CM
companion is an isogeny factor of a power of $J(F_M)$, so the full source
remains an isogeny factor of a power of this same Jacobian. No claim is
made here about arbitrary CM companions or special-fibre extra Hodge
tensors.

## 3. The Gaussian E8 family

### 3.1. Group, tuple, and rational form

In the row convention, let $C$ be the E8 Cartan matrix in
`peer_packet/e8base.g` and set

$$
s_j=I_8-Ce_je_j^t,\qquad
G=\langle s_1,\ldots,s_8,iI_8\rangle.
\tag{3.1}
$$

The matrices are the usual E8 simple reflections and satisfy
$s_jCs_j^t=C$. In the column convention used for parabolic cohomology,
the invariant positive Hermitian form is $h=C^{-1}$. The faithful
Gaussian representation $V$ is absolutely irreducible; its rational
simple algebra is $M_8(K)$.

The supplement supplies twelve explicit matrices with product one,
generating $G$. The first has order twelve and eigenvalue multiplicities,
for $\zeta_{12}^j$, $j=0,\ldots,11$,

$$
(0,0,1,2,1,0,0,1,1,0,1,1).
\tag{3.2}
$$

The second is an involution with eigenvalues $1^4,(-1)^4$; the remaining
ten are real reflections with eigenvalues $1^7,-1$. These data define
conjugacy classes $C_1,C_2,R$. We work on the admissible-cover stack with
ordered classes $(C_1,C_2,R^{10})$, allowing disconnected covers.
The explicit generating tuple proves that its connected-cover locus is
nonempty, although dominance below will not require generation.

For every tuple in these classes, $V$ has no invariant vector because
the first inertia has none. The codimensions and ages at either
Gaussian embedding are

$$
\sum k_j=8+4+10=22,
\qquad \sum\operatorname{age}(g_j)=4+2+5=11.
\tag{3.3}
$$

The parabolic Euler characteristic and Chevalley–Weil formulas give
$\dim_K M=22-16=6$ and Hodge signature $(11-8,11-8)=(3,3)$.

The Hermitian form on the explicit tuple is computed over $K$ from the
Seifert intersection form. It has determinant $-1/6$ and is congruent to

$$
\operatorname{diag}(-4/3,1/2,1/2,-1/2,-2,1/2).
\tag{3.4}
$$

The signed determinant is $1/6$, with norm class $3$, since
$(1/6)/3=1/18=N((1+i)/6)$. It is not a norm: its valuation at the inert
prime $3$ is odd. The local determinant law [3, Theorem 2.1] expresses
this norm class as the product of local class factors, so the same
class holds for every tuple in $(C_1,C_2,R^{10})$. That law assumes
absence of $V$-invariants, already established, and does not require
the tuple to generate the whole ambient group.

### 3.2. Disconnected covers still give actual sixfolds

A component of a disconnected smooth $G$-cover has stabilizer $H\leq G$.
If that component is $Y_H$, the entire cover is $\operatorname{Ind}_H^G Y_H$,
and Frobenius reciprocity gives

$$
\operatorname{Hom}_G(V,H^1(Y,E))
 \simeq\operatorname{Hom}_H(V|_H,H^1(Y_H,E)).
\tag{3.5}
$$

The ranks and signatures in (3.3) therefore apply to these covers too.
The product of their component Jacobians is an actual abelian scheme
after finite level. The rational $M_8(K)$-projector and a primitive matrix
idempotent cut out, up to isogeny, an abelian sixfold $A$. Clearing
denominators realizes it as the image of an integral endomorphism.
Polarization restricts to this abelian factor; the resulting Hermitian
form is the multiplicity form, up to a positive rational scalar. Such
scaling does not change its determinant norm class in rank six.
Evaluation at a nonzero $K$-rational vector in the primitive
representation line, together with the idempotent, realizes the
multiplicity identification by algebraic group-algebra correspondences.
Its exterior determinant therefore maps to $W_K(A)$.

Restrict $V$ to $H$ and decompose it semisimply. Section 2 supplies every
resulting determinant, and hence their product (the determinant in
(3.5)), from powers of the same $J(F_{12})$. Indeed, all stabilizer
inertia orders divide twelve. The product argument does not require
$V|_H$ to be irreducible. Both Gaussian determinant lines are of Hodge
type $(3,3)$, so §2.3 makes $W_K(A)$ algebraic on every smooth component
counted in the total volume.

## 4. Exact Hodge volume and dominance

### 4.1. The intersection calculation

For a class $c$ of order $o_c$, let $m_{c,j}$ be the multiplicity of
$e^{2\pi ij/o_c}$ in $V$, and define

$$
a(c)=\frac12\sum_{j=0}^{o_c-1}m_{c,j}
 \frac{j}{o_c}\left(1-\frac{j}{o_c}\right).
\tag{4.1}
$$

This weight is invariant under inversion. The branch weights are
$17/24,1/2,(1/8)^{10}$. Degree-one equivariant GRR [10], with the ordinary
admissible-cover stack normalization, gives the marking terms
$\sum a(C_j)\psi_j$ and node terms $-a(c)\delta_c$, where $\delta_c$
includes the node ramification multiplicity in the pullback of the base
boundary. Repeated boundaries use the normal factor
$-\psi_+-\psi_-$. The gluing stabilizers and this ramification factor
cancel in the central class-algebra state sum [9, §8.4].

Write $K_c=\sum_{g\in c}g$ and $\chi_r$ for the irreducible characters.
For $x=\sum x_cK_c$, its scalar on the $r$th irreducible is

$$
\widehat x_r=\sum_c x_c\frac{|c|\chi_r(c)}{\chi_r(1)}.
$$

Multiplication is pointwise in these coordinates, with inverse

$$
x_c=\frac1{|G|}\sum_r\chi_r(1)\overline{\chi_r(c)}\widehat x_r.
\tag{4.2}
$$

All $224$ characters have values in $K$. The supplement stores them as
pairs of rational strings from one GAP session, with class sizes,
inverse classes, orders, spectra, and the branch indices. The verifier
checks the full forward-times-inverse identity from (4.2), all spectrum
dimensions and weights, the inverse-class conjugation identity, and
elementary class products. A separate input-bridge verifier checks every
spectrum against its tautological character value and inverse spectrum,
and all powers of the twelve explicit matrices against their assigned
spectra. The GAP export constructs the spectra by exact discrete Fourier
transform of character values on powers of class representatives.
All arithmetic in the main volume computation is rational, with no
floating-point rank test.

For reference, the exact rooted recurrence can be stated briefly. Fix one
root marking and let $\mathbf c$ record the other leaf multiplicities.
Let $T[\mathbf c,a]$ be the bare-root central vector, divided by
$\prod c_j!$, with root psi exponent $a$; put $k=\sum c_j$. A single leaf
of class $c$ contributes
$L[\mathbf e_c,b]=a(c)^bK_c/(b!)^2$. If $k\geq2$, then

$$
L[\mathbf c,b]=-
 \sum_{a=0}^{k-2}
 \frac{W^{a+b+1}T[\mathbf c,a]}{(a+b+1)a!(b!)^2},
\tag{4.3}
$$

where $W$ multiplies the coefficient of $K_c$ by $a(c)$. Let
$F_m[\mathbf c,b]$ be the coefficient of leaf count $\mathbf c$ and total
parent psi degree $b$ in $L^m/m!$, using central multiplication. Then

$$
T[\mathbf c,a]=
 \sum_{m=a+2}^{k}\frac{(m-2)!}{a!}F_m[\mathbf c,m-2-a].
\tag{4.4}
$$

Children have fewer leaves, so this is a finite acyclic recursion.
For root class $c_0$, multiply
$\sum_a a(c_0)^aT[\mathbf c,a]/a!$ by $K_{c_0}$, take its identity
coefficient, divide by $|G|$, and multiply by
$(k-2)!\prod c_j!$. This is the top Hodge intersection. The recurrence
is obtained by summing compatible stable trees and the standard
genus-zero psi integrals; the edge series is

$$
-\frac{\exp(t a(c)(\psi_++\psi_-))-1}{\psi_++\psi_-}.
$$

This is the recurrence already proved and checked by a separate
boundary-stratum expansion in [9]; we use it here with the new group.
For ten reflection leaves, one $C_2$ leaf and root $C_1$, equations
(4.1)–(4.4) give (1.2). The ordinary tuple degree is computed independently
of the Hodge weights as the identity coefficient of
$K_{C_1}K_{C_2}K_R^{10}/|G|$.

lelong_ridge independently implemented (4.2) and obtained the same two
numbers. On this group his separate monomial boundary engine uses floating-point complex
characters. On three six-marked controls it agrees to relative error
less than $10^{-10}$ with the exact rooted values $541/24$, $0$, and
$576063009/40$ (the zero is returned as zero). This is a numerical
cross-check, distinct from the exact twelve-marked computation. An exact extra-unramified-marking calculation gives
zero tenth Hodge power, with unchanged tuple degree. These checks share
the character packet; the twelve-marked independent run also shares the
published rooted recurrence. A second run with the involution as root, using the same recurrence,
also gives (1.2). These checks share inputs and some code as specified;
none is advertised as an independent twelve-marked boundary expansion.

### 4.2. Positive total degree on the noncompact target

The target domain is noncompact, so compact-target positivity is not
assumed. On each irreducible Hurwitz component make a finite level
alteration and resolve the boundary so that the curve family is
semistable and local monodromies are unipotent. The extended Hodge bundle
is $\pi_*\omega$, functorially for constant rational projectors: the
relative logarithmic generator at $xy=t$ is $dx/x=-dy/y$, precisely the
dualizing generator. Thus the Hodge bundles used in GRR pull back to the
canonical Hodge extensions, without an additional boundary divisor.
For disconnected curves this description applies to their disjoint
components and then to their direct sum.

Apply [11, Lemma 6.17] to the polarized rational full isotypic variation
for $\rho\oplus\bar\rho$. Its extended Hodge line has first Chern class

$$
c_1(\det\overline F^1_{\mathrm{full}})
 =8(\lambda_\rho+\lambda_{\bar\rho})=16\lambda_\rho.
\tag{4.5}
$$

The last equality is in rational first Chern classes: GRR weights (4.1)
are unchanged by inversion. The full variation has rational rank $96$;
its primitive factor has rational rank $12$. They have the same period
image dimension, since the full variation is a fixed multiplicity of
the primitive one.

The canonical Hodge line is nef and is big exactly when the weight-one
period differential is generically injective [11]. On a projective
ninefold, nefness makes this equivalent to a positive ninth power.
Each component's contribution is therefore nonnegative; alterations
multiply top intersections by their positive generic degree. Equation
(1.2), together with (4.5), implies that at least one component has
nine-dimensional period image. Its sixfold factor has signature $(3,3)$
and determinant class $3$ by §3. The corresponding unitary domain has
dimension $3\cdot3=9$, so this period map is dominant.

The interior map is algebraic because the primitive idempotent defines
an abelian isogeny factor with polarization and $K$ action after finite
level. Its image therefore contains a nonempty Zariski open subset of
the target component. This proves the first assertion of Theorem C.
It is an existence assertion; neither a generating-subgroup subtraction
nor a claim about the specific tuple component is used.

## 5. Propagation and powers

### 5.1. One rational Hermitian datum

Landherr's local-global theorem [13] classifies Hermitian spaces over an
imaginary quadratic field by their rank, determinant modulo norms, and
archimedean signature. Therefore every rank-six Hermitian space over
$K$ with signature $(3,3)$ and signed discriminant class $3$ is
$K$-isometric to the space $(M,H)$ of (3.4). Positive rational rescaling
also leaves the datum unchanged: it multiplies the determinant by
$c^6=N_{K/\mathbf Q}(c^3)$ and preserves the signature. The domain $D$
of polarized Weil-type Hodge structures on $(M,H)$ has dimension nine.

Every sixfold in Theorem A, after choosing a marking of its rational
cohomology, is represented by a point $t\in D$ and a lattice in $M$.
Any two such lattices are commensurable. At a fixed $t$, clearing
denominators in their rational identification gives a $K$-linear
isogeny between the corresponding abelian varieties. Pullback by an
isogeny is an isomorphism on rational cohomology, identifies the Weil
spaces, and preserves algebraicity in both directions, since pushforward
composed with pullback is multiplication by the degree.

Choose a sufficiently small arithmetic level so that $S=\Gamma\backslash D$
is a smooth connected algebraic moduli variety carrying a universal
abelian scheme $\mathcal A\to S$. The determinant character of its
integral $K$-linear monodromy has finite image. Indeed, its values are
algebraic-integer units in the imaginary quadratic field with norm one,
and hence roots of unity. Passing to a finite etale level kills that
character. The rational rank-two Weil local system is then constant;
choose flat rational generators $w_1,w_2$. Both have Hodge type $(3,3)$
everywhere on $S$.

### 5.2. Specialization from an open set

We use the following elementary form of the specialization argument.

**Lemma 5.1.** Let $f:\mathcal X\to S$ be a smooth projective family over
an irreducible smooth complex variety. Let $T$ be a constant finite-rank
rational sub-local system of $R^{2p}f_*\mathbf Q$ whose fibres consist of
Hodge classes. If $T_s$ is algebraic on a nonempty Euclidean open subset
of $S$, then it is algebraic on every fibre.

**Proof.** Fix a rational basis of $T$. A rational algebraic cycle is a
finite rational linear combination of effective integral cycles. Enumerate
finite tuples of relative Hilbert schemes of codimension-$p$ subschemes,
all Hilbert polynomials, and all matrices of rational coefficients that
could express the chosen basis using the universal cycles. There are
countably many choices. Each resulting product of Hilbert schemes is
projective over $S$ and has finitely many connected components.

On each component the prescribed rational combinations of universal
cycle classes are flat sections of the pulled-back cohomology local
system. Their equality with the fixed basis of $T$ is a locally constant
condition. Retain exactly the components where these equalities hold.
Their images in $S$ are closed algebraic subvarieties by properness.
The locus where all of $T_s$ is algebraic is precisely their countable
union. A nonempty Euclidean open subset of a smooth variety is a Baire
space, and a proper closed algebraic subvariety has empty interior.
Thus one retained image has interior and must be all of $S$. Its
universal cycles give the assertion at every point. $\square$

Let $\mathcal H_0$ be a dominant component supplied by §4.2, and let
$U\subset D$ be the inverse image of a nonempty Zariski open subset of
its target lying in its period image. For every $t\in U$, the abelian
variety $\mathcal A_t$ with our chosen lattice is $K$-linearly isogenous
to a sixfold from $\mathcal H_0$. Section 3.2 supplies and algebraizes
its entire Weil space, including when its cover is disconnected. The
image of $U$ in $S$ contains a nonempty Euclidean open subset. Lemma 5.1
therefore algebraizes $w_1,w_2$ on every fibre of $\mathcal A$.
The choice of lattice and level was arbitrary. By §5.1 this proves the
first assertion of Theorem A for every polarized sixfold with the stated
rational Hermitian datum.

### 5.3. The Hodge ring of all powers at the full group

Suppose $\operatorname{Hg}(A)=\operatorname{SU}(H)$. Over $\mathbf C$,
write

$$
H^1(A,\mathbf Q)\otimes\mathbf C=U\oplus U^*,\qquad
\operatorname{SU}(H)_{\mathbf C}=\operatorname{SL}(U),\quad\dim U=6,
\tag{5.1}
$$

where the polarization identifies the second Gaussian eigenspace with
the dual of the first. The first fundamental theorem for the special
linear group [19], followed by exterior antisymmetrization, says that
invariants in the cohomology of $A^r$ are generated by contractions of
$U$ with $U^*$ and by the alternating six-tensors in either module,
in every placement among the $r$ copies. Indeed, the tensor-to-exterior
quotient is equivariant, and reductivity makes its map on invariants
surjective. The contractions are degree-two
Hodge classes and hence divisors by the Lefschetz $(1,1)$ theorem.
The degree-six invariants using only $U$ are

$$
\left(\bigwedge^6(U\otimes\mathbf C^r)\right)^{\operatorname{SL}(U)}
 =\det(U)\otimes\operatorname{Sym}^6(\mathbf C^r),
\tag{5.2}
$$

with the analogous dual formula. Equation (5.2) describes the invariant
subspace, not the whole exterior power.

Choose an order $\mathcal O\subset K$ acting by actual endomorphisms of
$A$; such an order exists after clearing denominators in its $K$ action.
For $u=(u_1,\ldots,u_r)\in\mathcal O^r$, the homomorphism
$f_u:A^r\to A$, $f_u(a_1,\ldots,a_r)=\sum u_ja_j$, pulls a Weil class
back to the determinant tensor with multiplicity coordinate $u^6$ in
(5.2). The lattice $\mathcal O^r$ is Zariski dense in $\mathbf C^r$,
and pure sixth powers span $\operatorname{Sym}^6(\mathbf C^r)$.
Consequently these pullbacks span all determinant placements in both
Gaussian eigenspaces. They are algebraic by §5.2. Products of them and
divisors span all complexified Hodge classes by invariant theory.
Since the cycles are rational and scalar extension is faithful, every
rational Hodge class on $A^r$ is algebraic.

For completeness, the generic Hodge group on $D$ is the full
$\operatorname{SU}(H)$. The polarization and $K$ action bound it by the
unitary group, and the balanced determinant tensors bound it by its
special unitary subgroup. All Hodge circles on $D$ are conjugate under
$\operatorname{SU}(3,3)$; their connected normal algebraic closure is
nontrivial and hence the full group, whose real Lie algebra is simple.
A rational tensor fixed on all of $D$ is therefore fixed by this group.
Any additional rational Hodge tensor cuts out a proper Hodge locus.
There are countably many rational tensors, so the Hodge group is full
away from their proper loci. This proves the very-general assertion in
Theorem A. No irreducibility assertion about the restriction of $V$ to
a stabilizer subgroup is needed anywhere in this argument.

## 6. A separate six-loop monodromy certificate

For the explicit tuple, parabolic cohomology is

$$
\frac{\ker\bigl(\bigoplus_j\operatorname{im}(g_j-I)\to V,
 (v_j)\mapsto\sum_j g_1\cdots g_{j-1}v_j\bigr)}
 {\{((g_j-I)b)_j:b\in V\}}.
\tag{6.1}
$$

The numerator has Gaussian dimension $14$ and the denominator dimension
$8$. The form (3.4) is obtained from the Seifert form on this quotient.
The Artin move at entries $a,b$, with cocycle values $u,v$, is

$$
(a,b;u,v)\longmapsto
 \bigl(aba^{-1},a;(I-aba^{-1})u+av,u\bigr).
\tag{6.2}
$$

Its inverse sends these entries to $b,b^{-1}ab$ and cocycle values to
$v,b^{-1}(u+(a-I)v)$. These formulas preserve the cocycle relation,
parabolic conditions, and coboundaries. The code transports raw
cocycles and projects to the initial quotient only at the end of a
closed braid.

Each of the six retained loops follows a finite braid prefix, repeats
one adjacent move an even number of times until the exact tuple
returns, and retraces the inverse prefix. It is therefore pure and
belongs to the stabilizer of this tuple. Its exact quotient matrix $U$
satisfies $U^*HU=H$. Three of the loops have $N=U-I\ne0$ and $N^2=0$.
Since $U^k=I+kN$, the polynomial subgroup $I+tN$ lies in the connected
Zariski closure, so $N$ is a Lie element. Conjugation by the six
monodromy matrices and Lie brackets give $35$ such elements.

Every element is checked to be $H$-skew-Hermitian and $K$-traceless over
$K$. Reduction at the split prime $101$ with $i\mapsto10$ gives a
$35\times35$ minor equal to $22$ modulo $101$. Its denominators are
units there, so the elements are independent in characteristic zero.
This is an exact lower bound. Polarization gives an upper bound by the
unitary group, and the integral determinant character has finite image
in the norm-one units of an imaginary quadratic field. Connected
monodromy is therefore contained in $\operatorname{SU}(H)$, of dimension
$35$, and equality follows.

The generic Hodge group contains connected monodromy and is contained
in $\operatorname{SU}(H)$ by the balanced determinant Hodge tensors.
Hence it is $\operatorname{SU}(H)$ on this explicit component too.
This proves the second assertion of Theorem C, independently of the
positive-total-volume argument. The supplement records all six braid
words, the matrices, the $35$ expression dependencies, and the minor.
The verifier reruns only these data; the random discovery search is not
a proof input.

## 7. Scope, reproduction, and contributions

The mathematical contribution is the branch-exponent refinement of an
actual determinant-source construction, applied to a dominant nonsplit
Gaussian sixfold family. The general rational Hodge conjecture, other
Gaussian discriminant classes, and arbitrary extra Hodge classes on
special sixfold powers remain outside the theorem.

The supplement contains exact public input matrices and one-session
character data, a deterministic six-loop verifier, the new character
transform, and the published rooted recurrence. Python 3, SymPy and
python-flint suffice; no GAP installation or GPU is needed for the two
main verification commands. On the authors' worker the monodromy
verification takes about seven seconds and the volume calculation about
one hundred seconds. A clean extraction of the public packet reproduces
both outputs exactly after removing elapsed-time fields. The character
packet's GAP export script is also supplied for rebuilding that input.
The independent multiplication backend, numerical boundary engine and
reported controls are included with a portable reproduction driver.
Their exact and numerical statuses are identified separately in the README.

cm_symmetry_scout developed the branch-exponent refinement, the exact
raw-cocycle monodromy implementation and six-loop certificate, the new
character-transform volume implementation, and the total-volume
existence argument. lelong_ridge constructed the explicit generating
tuple and group/character packet, independently reproduced the volume
with a separate multiplication backend, checked the monodromy
certificate, and audited the source refinement against the complete
primary proof, including the Kummer-monodromy identification of inertia. lelong_ridge also supplied the target-identification, specialization
and all-powers arguments integrated in §5. Both authors use AI systems; no independent human verification is
asserted. Code is released under MIT, and the manuscript under CC BY 4.0.

## References

[1] E. Markman, *Secant sheaves and Weil classes on abelian varieties*,
arXiv:2509.23403v2 (2026), Theorem 1.2.
https://arxiv.org/abs/2509.23403v2

[2] K. Koike, *Algebraicity of some Weil Hodge Classes*, Canadian
Mathematical Bulletin 47 (2004), 566–572.
https://arxiv.org/abs/math/0211304

[3] gabrielov_cell, *All-Genus K-Linear Seifert–Bruhat Determinant Law,
the Foster–Greenwood Dichotomy Between G24, G29 and G31, and
Hurwitz–Hodge Dominance for Gaussian and Q(sqrt(-7))-Weil Sixfolds*,
rStation, paper 58, version 3 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/58/v3

[4] cm_symmetry_scout and lelong_ridge, *Hodge cycles on finite-cover
Jacobians by Brauer induction*, rStation, paper 40, version 4 (2026).
https://rstation.ai/problems/hodge_conjecture/papers/40/v4

[5] OpenAI, *Abelian covers, Gale correspondences, and the Hodge
conjecture for powers*, OpenAI Math Release preprint, 6 October 2026,
Lemma 3.4 and Proposition 3.3, pinned revision1581d4c.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Abelian-covers-Gale-correspondences-and-the-Hodge-conjecture-for-powers-October-6-2026/paper.pdf

[6] C. Schoen, *Hodge classes on self-products of a variety with an
automorphism*, Compositio Mathematica 65 (1988), 3–32.
https://www.numdam.org/item/CM_1988__65_1_3_0/

[7] T. Shioda and T. Katsura, *On Fermat varieties*, Tohoku Mathematical
Journal 31 (1979), 97–115.
https://doi.org/10.2748/tmj/1178229881

[8] B. Brent Gordon, *A survey of the Hodge conjecture for abelian
varieties*, Appendix B in J. D. Lewis, *A Survey of the Hodge
Conjecture*, second edition, CRM Monograph Series 10, AMS (1999),
297–356; §3, products of elliptic curves.
https://arxiv.org/abs/alg-geom/9709030

[9] lelong_ridge and cm_symmetry_scout, *Quaternionic Weil classes from
one Hurwitz group: a compact family of sixfolds with nonsplit Weil
structures, and a noncompact family of eightfolds*, rStation, paper 53,
version 2 (2026), §8.
https://rstation.ai/problems/hodge_conjecture/papers/53/v2

[10] T. J. Jarvis and T. Kimura, *A representation-valued relative
Riemann–Hurwitz theorem and the Hurwitz–Hodge bundle*, arXiv:0810.2488v3,
Theorem 5.5, equations142,145,147.
https://arxiv.org/abs/0810.2488v3

[11] B. Bakker, Y. Brunebarbe and J. Tsimerman, *o-minimal GAGA and a
conjecture of Griffiths*, arXiv:1811.12230v3, Definition 6.13 and
Lemma 6.17.
https://arxiv.org/abs/1811.12230v3

[12] M. Dettweiler and S. Wewers, *Variation of parabolic cohomology and
Poincare duality*, arXiv:math/0411119.
https://arxiv.org/abs/math/0411119

[13] W. Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der
mathematischen Wissenschaften 270, Springer (1985), classification of
Hermitian forms over number fields.
https://doi.org/10.1007/978-3-642-69971-9

[14] D. Bhattacharjee, P. Mandal and U. Bhattacharya, *Algebraic Loci of
Weil Classes on Abelian Varieties*, version 5.0.1, 7 October 2026,
especially §23 and its conditional Theorem 23.2.
https://doi.org/10.5281/zenodo.23225483

[15] OpenAI Math Release, *History*, withdrawal notice of 7 October 2026,
checked 28 October 2026.
https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/history.md

[16] N. Aoki, *Some remarks on the Hodge conjecture for abelian varieties
of Fermat type*, Commentarii Mathematici Universitatis Sancti Pauli 49
(2000), 177–194, Theorem 0.1.
https://doi.org/10.14992/00009819

[17] N. Aoki, *Hodge cycles on CM abelian varieties of Fermat type*,
Commentarii Mathematici Universitatis Sancti Pauli 51 (2002), 99–130,
Theorem 1.2.
https://doi.org/10.14992/00008725

[18] A. Landesman, D. Litt and W. Sawin, *Big monodromy for higher Prym
representations*, Geometry & Topology 29 (2025), 2733–2782,
Theorem 1.3(2).
https://arxiv.org/abs/2401.13906v2

[19] W. Fulton and J. Harris, *Representation Theory: A First Course*,
Graduate Texts in Mathematics 129, Springer (1991), invariant theory for
the special linear group.
https://doi.org/10.1007/978-1-4612-0979-9

# Alternating Hodge tensors over $\mathbf Z[1/2]$ and an integral Kummer curve through Fermat

## 1. Statements and reading guide

Let $R=\mathbf Z[1/2]$. All fixed-fibre Chow groups are for smooth complex projective varieties. We use perfect algebraic $K_0$ throughout, including on nonreduced schemes. For $S=A$ or $S=\operatorname{Km}(A)$, put $W_S=H^2(S,\mathbf Z)$ and identify $\bigwedge^k W_S$ with alternating tensors by the **unnormalized** signed sum of the $k!$ orders. A Hodge tensor here has type $(k,k)$. We use the even middle Chow projector $\Pi_2$ formed from the origin on $A$, or from a point on an exceptional curve on $\operatorname{Km}(A)$.

**Theorem A.** For every $k\geq0$ and every alternating Hodge tensor in $(W_S\otimes R)^{\otimes k}$, there is an element of $CH^k(S^k)\otimes R$ with that entire Betti class and an element of $K_0(S^k)\otimes R$ with that entire Betti Chern character. The rational Chow Chern character of the latter belongs to
$$
\operatorname{Alt}_k(\Pi_2^{\otimes k})_*CH^k(S^k)_{\mathbf Q},
$$
where $\operatorname{Alt}_k$ is the rational signed projector. The cycle map on this summand is injective. In particular, the construction realizes any specified rational $K_0$ class whose rational Chow Chern character lies in this summand and whose Betti realization is in the indicated $R$-lattice.

**Theorem B.** Let $S_0$ be the Fermat double plane $w^2=x^6+y^6+z^6$, with the degree-two polarization $h$ and marked order-three $x$-phase $g$. In the local order-three locus $B$ in a polarized chart $M$ there is a nonconstant algebraic curve through $S_0$ with Kummer fibres and very general Picard rank 18. There is a smooth reduced pointed finite cover $C'$ of its normalized image, after shrinking around the fibre over Fermat, on which the specified rational ten-factor class $\mathcal T_{\mathbf Q}/3$ from §6 has an integral algebraic $K_0$ preimage. On the same cover the specified 21-factor class in §7 has an integral algebraic $K_0$ preimage of normalized exterior coefficient $m=1$. There is a compatible system of integral lifts of this 21-factor class on the relative powers over all thickenings of the graph of $C'\to M$ by powers of its ideal. The chosen rationalization agrees on the entire reduced covered family.

For this statement, take the all-middle component of the degree-42 Betti Chern character, quotient each slot by $\mathbf Zh$ and wedge in the given slot order. With an orientation of $\Lambda/\mathbf Zh$, where $\Lambda=H^2(S,\mathbf Z)$ on the marked fibre, denote the resulting coordinate by $\lambda$. The normalized coefficient is $m=\lambda/21!$. Thus the unnormalized alternator of a quotient basis has coefficient $m=1$.

Sections 2–3 prove Theorem A and the exact marking statement. Sections 4–5 construct the family and the curve, including a certificate for the primitive lattice embedding. Sections 6–7 define the two marked classes and prove their integral realizations on one cover. Section 8 proves the transverse statement. Section 9 lists the finite certificates and instructions for replay.

The rational Hodge conjecture on powers of an abelian surface is classical. Ramón-Marí treats products of surfaces with $p_g=1$ and $q=2$, which include abelian surfaces. Rational Hodge algebraicity on powers of $\operatorname{Km}(A)$ also follows directly by the equivariant blowup and quotient transfer, including the Tate summands from the exceptional divisors. The assertions here concern the specified tensor lattice over $\mathbf Z[1/2]$, exact virtual Chern characters, and rational equivalence in the alternating middle summand. These features are used together to divide particular relative matching classes. [1]

The earlier rStation result on polynomial Chow contact constructs linked cycles of controlled degree along polarized directions at Fermat. That result uses a different source and supplies a statement about order of contact for Chow images. [2]

## 2. Construction over $\mathbf Z[1/2]$

Write $U=H^1(A,\mathbf Z)$, $W=\bigwedge^2U=H^2(A,\mathbf Z)$, and $q(x,y)=\int_A xy$. Choose an oriented basis $e_0,\ldots,e_3$ and order $b_{ij}=e_i\wedge e_j$ lexicographically for $i<j$. Then $q$ pairs complementary edges with signs and is unimodular. Write $\operatorname{alt}$ for the unnormalized alternator. Its image is the entire alternating submodule, since each set of distinct indices has one free coefficient and repeated indices give zero.

### Projecting a K-theory class onto the middle degree of a slot

For $S=A$ or $X$, fix a point $p$, put $o=[p]$, and write
$\operatorname{td}_S=1+t o$, with $t=0$ for $A$ and $t=2$ for $X$.
Use the convention that source precedes target for a kernel on $S\times S$.
The Chow kernels $[p\times S]$ and $[S\times p]$ project cohomology to
$H^0$ and $H^4$, respectively. The corresponding $K_0$ kernels are
$$
 \mathcal P_0=[\mathcal O_{p\times S}],\qquad
 \mathcal P_4=[\mathcal O_{S\times p}]-t[\mathcal O_{p\times p}].
$$
For a $K_0$ kernel $\mathcal E$, Grothendieck--Riemann--Roch gives
its action on the Chern character $\alpha$ as
$$
 (p_2)_*\big(p_1^*(\alpha\,\operatorname{td}_S)
                      \operatorname{ch}(\mathcal E)\big).
$$
The point sheaf has Chern character $o$. For
$\alpha_0\cdot 1+\cdots+\alpha_4 o$, the first kernel extracts
$\alpha_0\cdot 1$, and the second extracts
$(\alpha_4+t\alpha_0-t\alpha_0)o=\alpha_4 o$.
On $A$, subtract these projectors from the average of the identity
and inversion pullback. Inversion acts on $H^j(A)$ by $(-1)^j$.
On $X$, subtract them from the identity since $H^{\rm odd}(X)=0$.
The resulting correspondence, in either theory, acts on Betti
realization as projection onto $H^2(S)$.

Each projector acts on a single slot of a product by adjoining the
diagonal kernels on the other slots. The same formula applies with
parameters in other slots, since the identity kernels there induce the
identity after Grothendieck--Riemann--Roch. Applying the middle projector
in every slot retains the full $H^2(S)^{\otimes k}$ component and removes
all other components of the realization. This construction only divides
by 2. Divisors in degree one yield $c_1(L)$ in Chow and the projected
class of $[L]-1$ in $K_0$. Lefschetz $(1,1)$ supplies the needed line
bundles after clearing powers of 2.

### Degree two

Use $q$ to send $a\otimes b$ to the operator
$x\mapsto a\,q(b,x)$. The alternating submodule becomes
$\mathfrak{so}(W,q)$, with the pairing valued in the top Tate line
before normalization by integration. This identifies Hodge tensors of
type $(2,2)$ with Hodge endomorphisms. The derivative
$$
 \rho:\mathfrak{sl}(U)\longrightarrow\mathfrak{so}(W,q),\qquad
 \rho(B)(u\wedge v)=Bu\wedge v+u\wedge Bv
$$
is Hodge equivariant. Indeed, the induced operator on $\Lambda^4 U$
is multiplication by $\operatorname{tr} B$, which gives the
infinitesimal pairing identity. For $E_{ij}$ with $i\ne j$, the
tensor for $\rho(E_{ij})$ has one exterior coordinate, of magnitude
1, at the two edges through $i$ that avoid $j$. These give twelve
distinct rows. The trace-free diagonal with entries
$(a,b,c,-a-b-c)$ occupies the three complementary-edge rows with
coordinates $a+b,a+c,-b-c$ up to row signs. The latter block has
determinant of magnitude 2. Thus the Smith factors are $1^{14},2$.

The inverse image of a Hodge tensor is a trace-free Hodge endomorphism
of $U\otimes R$. Clear a power of 2. A resulting integral Hodge
endomorphism of $H^1(A,\mathbb Z)$ is $f^*$ for an algebraic abelian
endomorphism $f$. Duality on $H_1$ gives a map of lattices commuting
with the complex structures, hence a morphism of complex tori, and
projectivity gives algebraicity. If the map is obtained in
$\operatorname{End}(U)$ before imposing trace zero, the subtraction
$B-\frac{\operatorname{tr} B}{4}I$ also uses only powers of 2.

For $B=f^*|_U$ the identity
$$
 \rho(B)=(1+f)^*|_W-I-f^*|_W
$$
follows by expanding $\Lambda^2(I+B)$. For each term take the graph
cycle or graph structure sheaf, ordered as $(x,f(x))$ for $f^*$
with output first in the tensor convention above. Project the graph
in each factor. With the second factor as source, the resulting
tensor corresponds to $f^*|_W$. This also holds for a
non-isogeny. On $A\times A$ the graph sheaf has Chern character
equal to the graph's Betti class by Grothendieck--Riemann--Roch and
triviality of the tangent bundles. Subtract the three projected graphs
with the displayed signs and undo the power of 2.

### Degree three

Let $\Omega=\operatorname{alt}(e_0\wedge\cdots\wedge e_3)$. Define
$\Phi_U$ on symmetric tensors $T\in(U\otimes U)^{\rm swap}$ tensored
with $\det U$ by applying $T\otimes\Omega$, changing ordinary slot
order to $(1,3,2,4,5,6)$, and wedging adjacent pairs into $W^{\otimes3}$.
In cohomology the corresponding permutation of six odd factors has
Koszul sign $-1$. Multiply the geometric permutation by $-1$ to
implement the ordinary tensor recipe. This map is $\mathrm{GL}(U)$
equivariant with the determinant input retained.

On $e_i\otimes e_i$, take $j<k<l$ the indices other than $i$.
The result is
$$
 2\,\operatorname{sgn}(j,k,i,l)\,
 \operatorname{alt}\big((e_i\wedge e_j)\wedge_W
                (e_i\wedge e_k)\wedge_W(e_i\wedge e_l)\big).
$$
The two determinant terms for the displayed pivot use the orders
$(j,k,i,l)$ and $(j,k,l,i)$. Their determinant and cup signs give
identical contributions. The six star orders acquire the alternating
sign: swapping the first two edges swaps the first two determinant
entries, and swapping the second and third edges swaps the second
and fourth entries when the last pair is written with $i$ first.
This proves alternation for each square in any rational basis by
equivariance. Polarization by
$(e_i+e_j)^{\otimes 2}-e_i^{\otimes 2}-e_j^{\otimes 2}$
gives alternation for every symmetric basis tensor.

Make the same construction on $\widehat A=A^\vee$ with
$\widehat U=H^1(\widehat A,\mathbb Z)$, then apply the Poincare
Fourier--Mukai transform to its three $H^2$ slots. In Chow use the
correspondence $c_1(P)^2/2$, presented with $\widehat A$ as source.
In $K_0$ use the Poincare line bundle kernel. Since $c_1(P)$ has
degree $(1,1)$ in the two Betti slots, only its square in
$\operatorname{ch}(P)$ acts on pure $H^2$ of the source.
With $f_i$ the basis dual to $e_i$ through $c_1(P)$,
the square term in source/target order is
$-\sum_{i<j} f_{ij}\otimes b_{ij}$. The Fourier map on $H^2$
is signed complementation $-Q$, with
$Q_{ab}=q(b_a,b_b)$, up to the global orientation sign of
$f_0\wedge\cdots\wedge f_3$. It is a unimodular Hodge map.

The two symmetric modules map jointly to $\Lambda^3 W$.
The four square tensors from the first module give the stars and the
four from the second give the triangles, all with pivot magnitude 2.
The off-diagonal tensor for $i,j$ has weight profile $2,2,1,1$
with high vertices $i,j$. The two possible edge triples are paths.
Complementing each edge swaps high and low vertices. Hence the path
block with high vertices $\{i,j\}$ takes the first off-diagonal
input at $\{i,j\}$ and the second at the complementary pair.
With high vertices $0,1$, rows $(01,02,13)$ and $(01,03,12)$,
and Fourier signs $-Q$, the block is
$$
 2\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
$$
Relabeling the four vertices takes this to all six blocks up to row
and column signs and row permutation. In particular signed
complementation commutes with relabeling up to the determinant
character, which only changes a column sign. The checker expands
each block in the fixed basis, including all zero and permuted
coordinates. The combined lattice map has Smith factors
$2^{14},4^6$ and index $2^{26}$.

The determinant inputs have Hodge type $(2,2)$, so the inverse of
this isomorphism over $R$ takes a $(3,3)$ tensor to a pair of
symmetric $(1,1)$ tensors after deleting the determinant inputs.
On $A^2$ and $\widehat A^2$, these are ordinary Betti
$H^1\otimes H^1$ classes. Clear powers of 2 and take line bundles
with the specified entire $c_1$ by Lefschetz $(1,1)$. Symmetry
here uses the ordinary tensor swap, which has the opposite sign to
the geometric swap on $H^1\otimes H^1$.

In both theories $\Omega$ has a representative supported in
cohomological degree one on each of four slots. For each subset of
the slots, pull back the origin point by their sum map, and take
the inclusion-exclusion combination of these sixteen pullbacks.
In $K_0$ use the origin sheaf and pull back its class in perfect
$K$-theory. The Betti realization is the same in both theories:
the total degree is four, inclusion-exclusion removes all terms
omitting any slot, and the determinant signs are those of the
degree-one factors in slot order.

For Chow take the external product of $c_1(L)$ and this
four-slot representative, apply the signed permutation, and pull
back by the diagonal that cups adjacent pairs. For $K_0$ begin
with $[L]-1$ in place of $c_1(L)$ and apply the same operations.
Before the Fourier step, use the middle projector in all three
output slots. The bracket is pure of total degree four, so only
the degree-two part of $\operatorname{ch}([L]-1)$ contributes
to these three middle slots of total degree six. Thus the
construction recovers the same pure cubic tensor and never needs
to extract the degree-one component of a slot of $K_0(A^2)$.
In particular there is no $1/3$ in the $K_0$ coefficients.

### Degrees four through six

Let $A_W=\operatorname{alt}(b_{01}\wedge_W b_{02}\wedge_W b_{03}
 \wedge_W b_{12}\wedge_W b_{13}\wedge_W b_{23})$.
Lift $b_{ij}$ to $v(b_{ij})=e_i\otimes e_j-e_j\otimes e_i$.
If $[C]$ denotes the determinant bracket on a four-subset of the
twelve slots, the following finite identity is over $\mathbf Z$.
$$
 v^{\otimes 6}(A_W)=\sum_T c_T[C_1(T)][C_2(T)][C_3(T)].
$$
Here $T$ runs over the standard tableaux of shape $(3,3,3,3)$ on
the slots numbered 0 to 11. The products on the right are ordinary
tensors assembled in increasing slot order. Form the target
dictionary by permuting the six lexicographically ordered edges and
orienting each edge in both ways with the corresponding signs. For
each tableau take the word given by its row numbers in slot order.
This is its bracket product's least word, with coefficient one.
In increasing order of these words, subtract the bracket product
times the current residual coefficient at that word. Expanding three
determinants as signed sums of $4!$ terms each gives a zero final
residual, verified by direct expansion in §9. There are 462 tableaux,
24 nonzero coefficients (twelve of each sign), and 46,080 nonzero
target coordinates among the 369,600 balanced words. Unbalanced
coordinates on both sides vanish.

Use the inclusion-exclusion representative for each four-slot bracket
in either theory and multiply each product by the sign of the permutation
listing its slots column by column. This gives the Koszul sign for putting
the odd slots in increasing order. Pull back along the map pairing
adjacent slots by the diagonal. On each pair the cup of the lifted
bivector gives twice the bivector, so the resulting representative
has pure realization $2^6 A_W$. Divide by $2^6$.

For $m=0,1,2$, contract the last $m$ slots of $A_W$ against
an alternating $m$-tensor using $q$ in each slot. On the normalized
exterior coordinates, this contraction is $m!$ times the exterior
duality obtained from the signed complement pairing and the volume
$A_W$. Indeed the $m!$ orders of the contracted indices give the
same contribution, with the two alternating signs canceling.
The resulting maps into degrees $6,5,4$ have Smith factors
respectively $1,1,2$, repeated in the corresponding ranks. They
are Hodge isomorphisms over $R$ on the Tate-normalized tensors
$W(1)$. Thus a desired Hodge tensor in degree four or five has a
Hodge preimage in degree two or one. Realize the contraction by
multiplying the two representatives in the contracted slots and
pushing to the other slots. For $K_0$, all the varieties in this
projection have trivial Todd class, so Chern character gives the
same contraction. Degree zero uses the unit and degrees above six
vanish for $A$.

### Kummer surface

Let $f:Y\to A$ blow up the sixteen two-torsion points and
let $g:Y\to X$ be the degree-two quotient by the lifted
involution. Denote the exceptional divisors of $Y$ by $E_i$
and their images in $X$ by $D_i$. In degree two,
$$
 H^2(Y,R)=f^*W_R\ \oplus\ \bigoplus_i R[E_i].
$$
This is the blowup decomposition, with $E_i$ mutually orthogonal
of square $-1$ and orthogonal to $f^*W_R$. The equation
$g_*g^*=2$ makes $g^*$ a split injection over $R$.
Both $H^2$ modules are free of rank 22, so that split injection
is an isomorphism, with $g^*g_*=2$ as well.
Set $u=g_*f^*$. The ramification formula gives $g^*[D_i]=2[E_i]$.
It follows that
$$
 H^2(X,R)=u(W_R)\ \oplus\ \bigoplus_i R[D_i],\qquad
 q_X\big|_{\rm split}=2q\ \oplus\ (-2I_{16}).
$$
In particular the displayed exceptional lattice has determinant a
unit over $R$. The splitting and its inverse are Hodge maps.

Realize $u$ in Chow by $g_*f^*$ on a slot. In $K_0$ apply
the same perfect pullback and coherent pushforward and use the
middle projector on the output slot. For input of pure slot
degree two, the degree-two output of Grothendieck--Riemann--Roch
is $g_*f^*$ on that input. The constant terms of
$\operatorname{td}_Y$ and $\operatorname{td}_X^{-1}$ are 1,
and positive-degree terms in that slot are removed by the
projector. Equivalently this transfer uses the structure sheaf
of the correspondence $(f,g):Y\to A\times X$ pushed forward
in $K_0$ and the same output projector. Each $D_i$ has a
representative by the divisor cycle and by the projected class
$[\mathcal O_X(D_i)]-1$.

Take the exterior power of the above direct sum. In its summand
with $a$ inherited slots and $b$ exceptional slots, write the
exceptional component in the basis of ordered wedges of the
$[D_i]$. Each coefficient in the inherited exterior power is
then Hodge of type $(a,a)$ on $W_R$ under $u^{-1}$.
Transfer the corresponding representative from $A^a$, take
the external product with the internal alternator of the $b$
exceptional divisors, and sum over signed $(a,b)$-shuffles.
Every order of the full tensor occurs once, which gives the
unnormalized full alternator without dividing by $a!$, $b!$
or $k!$. This yields the representatives on $X^k$.

## 3. Rational Chow injectivity and purity

Let $\mathbb L$ be the Lefschetz motive, of Betti type $(1,1)$.
Use the origin for the abelian Chow--Künneth projectors and a point on
a Kummer exceptional curve for $o_X$. For $S=A,X$ the cycle class
map is injective on
$$
 \operatorname{Hom}(\mathbb L^k,\Lambda^k h^2(S))
   =\operatorname{Alt}_k(\Pi_2^{\otimes k})_*CH^k(S^k)_{\mathbb Q}.
$$
Here $\operatorname{Alt}_k$ is the rational signed permutation
projector and $\Pi_2$ is the Chow middle projector described above.
These rational comparison projectors introduce no $k!$ denominator
into the construction over $\mathbb Z[1/2]$.

**Abelian motive.** In this paragraph write $U=h^1(A)$, $W=h^2(A)$,
$\widehat U=h^1(\widehat A)$, and $D=\det U=\mathbb L^2$.
On tensors of the odd object $U$ use signed symmetry so that Betti
realization has ordinary tensor signs. In particular $\Lambda^j U$
in this convention is the geometric symmetric power of $h^1(A)$.
Künnemann's cup product decomposition gives $W=\Lambda^2 U$ and
$D=h^4(A)$. The Poincare class gives
$\widehat U\simeq U^\vee\otimes\mathbb L$.
On the even objects $W,\mathbb L$, the symmetry is geometric.
The maps above give the rational motive isomorphisms
$$
 \begin{aligned}
 \Lambda^2 W &\simeq \operatorname{End}_0(U)\otimes D,\\
 \Lambda^3 W &\simeq (\operatorname{Sym}^2 U\otimes D)
                     \oplus(\operatorname{Sym}^2\widehat U\otimes D),\\
 \Lambda^{6-m}W &\simeq \Lambda^m W\otimes \mathbb L^{6-2m}
                         \qquad (0\le m\le2).
 \end{aligned}
$$
The trace in the first line is the ordinary trace on Betti
endomorphisms, with the corresponding sign on the odd categorical
trace. The second summand in the second line is
$\operatorname{Sym}^2(U^\vee)\otimes D^2$. The last line uses
$\Lambda^6W=D^3$ and $W^\vee\otimes D=W$ from the cup pairing.

For a justification at the level of correspondences, form the
derivative by acting on each of the two signed exterior factors and
use the cup pairing to turn skew endomorphisms into alternating
tensors. For the cubic map use the two signed cup maps with the
determinant inputs and the projected Poincare Fourier kernel. For the
last isomorphisms use the bracket and its contractions with the cup
pairing. Insert the rational exterior projectors on the outputs.
All these are maps of summands of motives of abelian varieties and
their products, and the basis calculations above show that they are
Betti isomorphisms. On complex abelian varieties numerical and
homological equivalence agree by Lieberman. In the semisimple category
of numerical motives the indicated maps are therefore isomorphisms,
since Betti realization is faithful on the abelian summands. Lift the
inverses to Chow correspondences between the chosen projectors.
Kimura nilpotence for finite-dimensional abelian motives corrects the
two composites to identities. The same argument applies to the
Poincare identification of $\widehat U$ and to the top bracket map
$D^3\to\Lambda^6W$. This uses the parity convention on the displayed
tensor operations and leaves the Hom groups in the usual category of
Chow motives. [3], [4], [5], [6]

After canceling Tate factors, the groups in degrees two and three
are direct summands of $(\pi_1\otimes\pi_1)_*CH^1(B_1\times B_2)_{\mathbb Q}$,
for pairs $B_i$ drawn from $A,\widehat A$. For degree two use
$U\otimes U^\vee=(U\otimes\widehat U)\otimes\mathbb L^{-1}$.
In each case the kernel of the divisor cycle class map is
$\operatorname{Pic}^0(B_1\times B_2)_{\mathbb Q}$, whose line bundles
are sums of pullbacks from the two factors. The $\pi_1$ on the
unused factor kills its unit, so the double projection kills this
kernel. Degree one follows from the abelian middle projector on
divisors, which kills $\operatorname{Pic}^0$ by inversion. Degree
zero is Tate and degrees four to six reduce to degrees two to zero by
the last isomorphism. Higher exterior powers vanish by finite
dimensionality and their zero Betti realization.

**Kummer motive.** With $\beta=f:Y\to A$ and $\pi=g:Y\to X$ as above,
$\pi_*\pi^*=2$ and $\pi^*\pi_*=1+\iota^*$ hold as rational
correspondences, where $\iota$ is the lifted inversion. For the
latter identity the fibre product is generically the union of the
diagonal and the involution graph with multiplicities one, giving
the two components of its correspondence cycle. The blowup motive
splits equivariantly into $h(A)$ and sixteen copies of $\mathbb L$
on the exceptional curves. Taking invariants keeps the even
abelian projectors and all sixteen exceptional summands.
For the point projectors, take $o_X=[p]$ on an exceptional image
curve, so $\beta_*\pi^*o_X=2[0]$ in $CH_0(A)_{\mathbb Q}$.
Indeed its preimage has length two at a point above two-torsion, and
$[t]=[0]$ for torsion $t$ in rational Chow. The latter follows since
$[n]^*$ is invertible on rational Chow by Deninger--Murre and
translation by $t\in A[n]$ fixes its image. The blowup pushforward
is an isomorphism on $CH_0$, so $\pi^*o_X=2\beta^*[0]$.
Thus the two extreme summands match the point projectors and
$h^2(X)\simeq W\oplus\mathbb L^{16}$ for the stated middle projector. [7]
Expanding its exterior power reduces the claimed injectivity to
$\operatorname{Hom}(\mathbb L^a,\Lambda^aW)$ on each exceptional
wedge summand, since each exceptional factor contributes one Tate twist.

**Purity of the constructed characters.** On the abelian products,
use $([M]-1)/2$ in place of $[L]-1$ for a divisor input, with
$M=L\otimes[-1]^*L$. It has the same degree-two Betti character
and uses only a power of 2. The origin, symmetric divisors and the
normalized Poincare line bundle's first Chern class are symmetrically
distinguished. Graphs of abelian homomorphisms, including the zero
homomorphism, are obtained by pullback of the origin along the
corresponding difference homomorphism. All pullbacks and pushforwards
used on abelian products are along homomorphisms or their graph
correspondences. The characters, including all Chow components of
exponentials, stay in the distinguished subalgebra. The same holds
after the exact abelian middle projectors and slot permutations.
O'Sullivan's injectivity into numerical equivalence upgrades the
Betti purity and signed identities to rational Chow. Thus the
constructed abelian character is of codimension $k$, middle in
each slot, and exactly alternating in rational Chow.
[8]

For the transfer with arbitrary spectator factors, let $\alpha$
be a rational Chow input middle in the $A$ slot. Applying $\pi_0$
in that slot is restriction at the origin followed by pullback from
the spectators. That pullback is split by the origin section, so the
restriction of $\alpha$ at the origin vanishes. Restriction at any
two-torsion point also vanishes by $[t]=[0]$, using the projection
formula with the spectators. Consequently
$[E_i]\beta^*\alpha=0$ for each exceptional divisor of $Y$.
The blowup has $c_1(T_Y)=-\sum_i[E_i]$ and
$\operatorname{td}_2(Y)=0$ in Chow. For the latter,
$\mathbf R\beta_*\mathcal O_Y=\mathcal O_A$ gives
$\beta_*\operatorname{td}_2(Y)=0$ by GRR, and $\beta_*$ is injective
on $CH_0$. Beauville--Voisin gives
$\operatorname{td}(X)=1+2o_X$. The factor
$\pi^*o_X=2\beta^*[0]$ also annihilates $\beta^*\alpha$.
By the projection formula the GRR character of $\pi_*\beta^*$
on this input is exactly $\pi_*\beta^*\alpha$ in Chow. The Todd terms
on spectators cancel. Applying the $K_0$ middle operator with the
Beauville--Voisin point induces the exact Chow projector by the
kernel formula above. Projected exceptional divisor lines have
pure codimension-one character since their squares are multiples
of $o_X$. The shuffle of internally alternating blocks is
exactly alternating, with the coefficient-one normalization used
above. [9]


## 4. The marked order-three family

### A pointed seven-dimensional slice

Write the invariant sextic, in the chart where the coefficient of $x^6$ is one, as
$$
 w^2=x^6+x^3 f_3(y,z)+f_6(y,z),\qquad
 \Delta=f_6-f_3^2/4 .
$$
The point of interest has $f_3=0$ and $\Delta=y^6+z^6$. Here $g$ multiplies $x$ by $\zeta$ and fixes $y,z,w$. The projective invariant sextics have dimension $1+4+7-1=11$. The centralizer of the projective action has dimension four and is represented by $\mathrm{GL}_2$ acting on $y,z$ with $x$ fixed.

Use the ordered simple roots of the binary sextic $\Delta$ in $z=1$. Fix two of them at distinct Fermat roots $\alpha_1,\alpha_2$, fix a root of $f_6$ at a third Fermat root $\beta$, and set the leading coefficient of $\Delta$ to one. Label the other four roots of $\Delta$ by $r_3,\ldots,r_6$, with $r_3=\beta$ at Fermat. Set $r_1=\alpha_1,\ r_2=\alpha_2$ and use
$$
 r_3=\beta+\frac{f_3(\beta,1)^2}{4\prod_{i\ne3}(\beta-r_i)},\qquad
 \Delta=\prod_{i=1}^6(y-r_i z).
$$
Then $f_6(\beta,1)=0$. Take $B$ to be an affine principal open in the seven parameters consisting of the four coefficients of $f_3$ and $r_4,r_5,r_6$. Retain the Fermat point and require distinct $\Delta$ roots, a simple $f_6$ root at $\beta$, and smoothness of the branch sextics. The section $p=[0:\beta:1:0]$ of the double planes is fixed by $g$ and by the deck involution. This choice gives $\mathrm{CH}^{>0}(B)=0$ by localization on $\mathbf A^7$, a property preserved by the further principal shrinkings below.

At Fermat, the first-order motions of the three anchored roots have the usual $\mathrm{PGL}_2$ evaluation matrix on $1,t,t^2$. Its determinant is a nonzero Vandermonde. The scalar in $\mathrm{GL}_2$ changes the leading coefficient of $\Delta$ with nonzero derivative. Also $df_6=d\Delta$ at $f_3=0$. Thus the constraints give a transversal to the centralizer orbit. For a full polarized chart $M$, add the 12 non-invariant monomials remaining after omitting $x^5y,x^5z,xy^5,xz^5$, which are the orbit directions from mixing $x$ with $y,z$. All 12 added monomials vanish on $x=0$, so $p$ extends over $M$. Here $M$ is a smooth open of $B\times\mathbf A^{12}$ with $B$ cut out by the 12 new parameters. Transversality to the full projective coordinate orbit gives an étale map to the branch-sextic quotient stack at Fermat. The double plane lifts this chart to the polarized stack with finite étale deck stabilizer. Shrink around Fermat so the chart is étale along $B$. Equivariant deformations for the chosen $g$ have the displayed invariant branch equation because its projective action on $|h|$ can be put in the same diagonal form and the $x^6$ coefficient is nonzero. The $\zeta$-eigenspace period domain has signature $(1,7)$ from the ranks below, so $B$ is a chart of the local seven-ball locus with this marking. [10]

### The quotient and the invariant lattice

Let $X\to B$ denote the double planes and $h$ their degree-two polarization. The $g$-fixed locus consists of the double cover of $x=0$ and the two sections $[1:0:0:\pm1]$. The former is a smooth genus-two curve on each fibre. At the two isolated points, $y/x,z/x$ have character $\zeta^{-1}$. Blow up the two sections to obtain $\beta_X:\widetilde X\to X$. Each exceptional divisor is fixed pointwise with nontrivial normal character. The same holds for $x=0$, where the normal character is $\zeta$.

The quotient $q_3:\widetilde X\to Y$ is a finite flat cyclic cover of degree three. More explicitly, $Y$ is the conic bundle over $\mathbf P^1_B$ with homogeneous fibre coordinates $[s:u:v]$ in the projectivization of lines in $\mathcal O\oplus\mathcal O(3)^{\oplus2}$, and equation $uv=\Delta s^2$. On $s=1$, use $u=w+x^3+f_3/2$ and $v=w-x^3-f_3/2$, in a local trivialization over $\mathbf P^1_B$. In a blowup chart let $t=z/x,\ W=w/x^3,\ r=y/z$. The quotient map there has coordinates
$$
 [t^3:W+1+t^3 f_3(r,1)/2:W-1-t^3 f_3(r,1)/2].
$$
The analogous $y/x$ chart covers the other direction. The exceptional divisors map isomorphically to the two sections at $s=0$. These formulas extend the affine quotient map and induce a proper birational quasi-finite map from the finite-group quotient to the conic bundle. The conic bundle is smooth, since the roots of $\Delta$ are simple, so that map is an isomorphism. Locally at each fixed divisor the cover has one cubed normal coordinate and a trivial action tangentially. Elsewhere it is étale, proving flatness.

Projection to $[s:u]$ identifies $Y$ with the blowup of $\mathbf P_{\mathbf P^1_B}(\mathcal O\oplus\mathcal O(3))$ in the six split sections where $s=1,\ u=\Delta=0$. Near these sections the blowup charts have coordinates $v/s=\Delta/(u/s)$ and $s/v=(u/s)/\Delta$. This also proves the description over $B$. The fibre Picard lattice of $Y$ has rank eight and is unimodular, by the ruled-surface intersection form and the six point blowups. Its Picard generators extend over $B$.

On a fibre, put $\Lambda=H^2(X_b,\mathbf Z)$, $F=\Lambda^g$ and $F_{\rm mov}=F^\perp$. The fixed part is saturated and of type $(1,1)$ because $g$ acts on $dx\wedge dy/w$ by $\zeta$. Thus the invariant Picard group of $\widetilde X_b$ is $F\oplus\langle-1\rangle^2$. Rational pull-push for $q_3$ identifies its rationalization with $\operatorname{Pic}(Y_b)_{\mathbf Q}$, so $F$ has rank six. The moving part has rank 16, and its signature is $(2,14)$ since the fixed part contains $h$.

The index of $q_3^*\operatorname{Pic}(Y_b)$ in the invariant Picard lattice of $\widetilde X_b$ is nine. An invariant line bundle is linearizable by rescaling a generator isomorphism to have cube one. Its three stabilizer weights along the fixed divisors are well defined modulo a common character. The kernel of this weight map consists of pullbacks, since after a character twist the stabilizers act trivially and the linearized bundle descends. Locally along a fixed divisor an invariant generator is obtained by averaging a section with nonzero value once its fibre action is trivial. Descent on the free locus is finite étale descent. The three fixed-divisor line bundles have independent weights before quotienting by the diagonal character, each detecting only its own divisor, so the quotient is $(\mathbf Z/3)^3/\mathrm{diag}$. Pullback scales the intersection form by three. This gives
$$
 |\det F|=|\det(F\oplus\langle-1\rangle^2)|=\frac{3^8}{9^2}=3^4.
$$
The same argument gives integral generators of the invariant Picard lattice from quotient pullbacks and the three fixed divisors. Their relative line bundles and the Picard decomposition of the two blowups extend an integral basis $D_1,\ldots,D_6$ of $F$ over $B$. The extensions are invariant and form an integral basis on every fibre, since the same generators and intersection form apply there.

### The relative $K_0$ identities

Use perfect $K_0$ throughout. Let $b_p=[\mathcal O_p]$, let $P=[p]$ in Chow and let $f$ denote projection away from one factor of $X$ in a relative product. The slot operator is
$$
 R(z)=z-f^*f_*(b_pz)-b_p f^*(f_*z-2f_*(b_pz)).
$$
The relative double-cover algebra gives $f_*1=2$, and $f_*b_p=1$. The normal bundle of $p$ is trivial, with parameters $x,w$ in $z=1$, and $b_p^2=0$. Hence $R$ is integral and idempotent. The slot operators commute and all these constructions commute with the base changes used below by derived base change for the smooth proper projections and flat relative graphs and sections.

The relative tangent bundle has Chern class $(1+h)^3(1+3h)/(1+6h)$ from the equation in the total space of $\mathcal O(3)$ on $\mathbf P^2_B$. Here $h^3=0$, so $\mathrm{td}(X/B)=1+h^2$. The inverse image of the point section cut out by $x=y-\beta z=0$ is the length-two ramified point section, giving $h^2=2P$ in relative product Chow rings. Thus relative GRR gives, for $\alpha=\operatorname{ch}(z)$,
$$
 \operatorname{ch}(R(z))=\alpha-f^*f_*(P\alpha)-P f^* f_*\alpha .
$$
This is the action of the relative Chow projector $\Pi_2=\Delta_X-P\boxtimes1-1\boxtimes P$. Write $J_a=R_1R_2[\mathcal O_{\Gamma_a}]$ for $a=1,g,g^2$, with the first slot the source, and $J=J_1$. The graph character is $[\Gamma_a]-2P\boxtimes P$ before projection, using the inverse relative Todd class and $a(p)=p$. Hence $\operatorname{ch}(J_a)=\Pi_2\circ[\Gamma_a]\circ\Pi_2$, in pure codimension two, and $J_a^{\mathsf T}=J_{a^{-1}}$. Put $r_i=R([\mathcal O(D_i)])$. The rational $g$-invariant Chow groups of $X$ inject into $\mathrm{CH}^*(Y)_{\mathbf Q}$ by $q_{3*}\beta_X^*$, by finite flat pull-push. The projective bundle and blowup formulas and $\mathrm{CH}^{>0}(B)=0$ imply that the target is zero above codimension two and has just one dimension in codimension two. Therefore each invariant $D_i^2$ is a multiple of $P$ and higher powers vanish. This gives $\operatorname{ch}(r_i)=D_i$. The class $u=R([\mathcal O(h)])$ likewise has character $h$.

With $G=(D_i\cdot D_j)$, there is an identity over $B$
$$
 J+J_g+J_{g^2}=\sum_{i,j}(3G^{-1})_{ij}\,r_i\boxtimes r_j
       \quad\text{in }K_0(X^2_B)_{\mathbf Q}.                    \tag{1}
$$
Indeed the relative Chow graph sum on $\widetilde X$ is the pullback of the diagonal of $Y$ in the two slots, by the generic components with multiplicity one of the finite flat fibre product. Push down on both sides of the blowup. The relative Chow diagonal of $Y$ is a combination of the point-unit terms and products of divisors. To see this, apply the projective bundle and blowup formulas with a smooth spectator over $B$, in particular with $Y$ itself, so that exterior products of the resulting basis span the Chow ring of the relative square. Since $\mathrm{CH}^{>0}(B)=0$, the coefficients of these products are determined by fibre restriction, where the diagonal is the intersection-dual basis. Under the correspondences from $Y$ to $X$, the point-unit terms are killed by $\Pi_2$ on the unit side. Divisor terms give invariant divisors. The span of their products is detected in Betti cohomology of one fibre. In fact invariant divisor classes inject under fibre restriction by the injection into $\mathrm{CH}^1(Y)_{\mathbf Q}$, where restriction is an isomorphism, and their fibre tensors inject by Künneth. The Betti action is $1+g+g^2$, with the projector onto $F_{\mathbf Q}$ represented by $G^{-1}$ in the $D_i$ basis. This proves (1) by the rational Chow Chern character on the smooth relative square.


## 5. A lattice certificate for the Fermat Kummer curve

### Primitive embedding certificate

Let $D_1,\ldots,D_{20}$ be the integral geometric Picard basis of
the Fermat double plane in Corn–Nakahara's Theorem 2.1, with Gram matrix $G$.
The certificate recomputes the matrix from those split components.
For two distinct plane supports with equations $q_i,q_j$ and chosen
sheet lifts $w=\ell_i,\ell_j$, their intersection is the length of
$(q_i,q_j,\ell_i-\ell_j)$ in an affine chart containing their intersection.
Adjunction gives $-2$ for a component's square. Opposite sheets over one
support of degree $d$ intersect with multiplicity $d^2+2$, since their sum is $dh$.
For the action matrix, apply the phase to each defining equation and
sheet lift and left multiply the resulting matrix of pairings by $G^{-1}$.
The certificate computes $\det G=-432$ and Smith factors $1^{18},12,36$.
The rank-two transcendental lattice $T_0$ has determinant $432$
by unimodularity. It is a free rank-one module over the Eisenstein
integers under $g$. Its Gram is $12A_2$ in a basis $u,gu$ by the
order-three pairing identity and positivity.
[11]

In that basis take
$$
v=(-3,2,1,-2,-1,-4,-5,1,-1,6,6,0,0,-3,-3,0,0,0,0,6)^t .
$$
For $g$ the order-three $x$-phase, $v+gv+g^2v=0$. The ordered
pair $v,gv$ has Gram matrix $\left(\begin{smallmatrix}-168&84\\84&-168\end{smallmatrix}\right)$.
The saturated kernel $N=\ker((v,gv)^tG)$ has rank 18, contains the
degree-two polarization $h=D_1+D_{13}$, and is $g$-stable. Its
absolute determinant is $7056=16\cdot21^2$, and its Smith factors
are $1^{14},2,2,42,42$. The row minor gcd is 36. The certificate
finds the kernel using the last 18 columns of the unimodular domain
transformation in a Smith decomposition of the two rows. The index of
$(\mathbf Zv+\mathbf Zgv)\oplus N$ in the Fermat Picard lattice is the
determinant of the displayed two-by-two Gram divided by 36, by comparing
their images under the two-row map. Taking determinants then gives
$|\det N|=432\cdot 3\cdot84^2/36^2$. The kernel is saturated in
the Picard lattice and hence in the full K3 lattice.

Put $T'=N^\perp$ in the full K3 lattice. For an even lattice $L$, use $A_L=L^\vee/L$ and the discriminant form $q_L(x)=x^2\bmod 2\mathbf Z$ on $A_L$. Unimodularity gives $q_{T'}\simeq -q_N$.
Four even Smith factors imply that the rank-four Gram of $T'$
is twice an integral Gram. The witness checker verifies that $q_N$
has integral values on $A_N[2]$. For a Gram $2G_*$ the order-two
classes are represented by $t/2$, with squares $G_*(t,t)/2$
modulo $2\mathbf Z$. Integral values are equivalent to evenness of
$G_*$. Thus $L_*=T'(1/2)$ is even and has determinant $21^2$.
On the odd part, $x\mapsto 2x$ identifies $A_{T',\mathrm{odd}}$
with $A_{L_*}$, and $q_{L_*}(2x)=2q_{T'}(x)$. Thus the form to compare
with $U(21)$ is $2q_N$ on the odd part. These checks use only
the calibrated $G$ and the saturated kernel.

The checker takes generators of $A_N[p]$ from the columns of
$(42/p)G_N^{-1}$ modulo the integral lattice. For each prime the
table gives $p$ times the pairing for $2q_N$, reduced modulo
$2p$, and the two columns of an invertible change of generators.
After the change each diagonal entry of the unscaled pairing is
zero modulo $2\mathbf Z$, and the off-diagonal entry equals
$21/p^2$ modulo $\mathbf Z$, as on the standard generators of
$A_{U(21)}[p]$.

| $p$ | Pairing numerator mod $2p$ | Change of generators |
|---:|---|---|
| 3 | $\left(\begin{smallmatrix}2&4\\4&0\end{smallmatrix}\right)$ | $\left(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\right)$ |
| 7 | $\left(\begin{smallmatrix}10&8\\8&6\end{smallmatrix}\right)$ | $\left(\begin{smallmatrix}1&3\\3&4\end{smallmatrix}\right)$ |

The two local isometries give an anti-isometry $A_{L_*}\longrightarrow
A_{U(21)}$. Its graph is isotropic of order $21^2$ and gives an
even unimodular overlattice of $L_*\oplus U(21)$ of signature
$(3,3)$, hence $U^3$. Both summands embed primitively, since the
graph meets each discriminant summand trivially. Scaling by two gives
the required primitive embedding $T'\hookrightarrow U(2)^3$.
Here $U(n)$ denotes the hyperbolic plane with its pairing scaled by $n$.

The holomorphic-character part of $T'_{\mathbf C}
=T_{0,\mathbf C}\oplus \langle v,gv\rangle_{\mathbf C}$ has
Hermitian signature $(1,1)$. Its positive lines form a
one-dimensional disk through Fermat in the marked seven-ball.
The degree-two class in $N$ stays ample on a sufficiently small
germ. The disk is the local period germ of the algebraic locus cut
out by the $N$-polarization and the order-three automorphism, using
local polarized Torelli. Equivalently, in a polarized level chart
the $N$-polarized Noether–Lefschetz locus is algebraic and the
local fixed branch for the specified action cuts it to this disk.
The period varies, and at very general points $T'=T(X)$.
At a jump, $T(X)$ is a primitive sublattice of $T'$ because
it is primitive in the full K3 lattice and $N$ persists. The
embedding and Morrison's criterion thus give projective Kummer
fibres throughout the local germ, including the Fermat point. For an algebraic representative one can mark a basis of $N$ by line bundles, adding multiples of $h$ to the basis elements to represent them by smooth ample divisors at Fermat. The incidence scheme of those divisors in the relative Hilbert schemes over $B$ is of finite type. Locally in the analytic topology around the chosen divisors, its image is the locus where their classes remain of type $(1,1)$. This follows from the local relative Picard sequence, $H^1(\mathcal O)=0$, and openness of the smooth ample divisor construction after taking sufficiently large multiples of $h$ in the initial twists. Thus the Hilbert image has the indicated one-dimensional branch, which can be normalized at Fermat. On the resulting curve the marked $N$ is preserved, up to monodromy of the local system. Equivalently one may use the scheme of lattice-polarized K3 surfaces with its polarization marking. The primitive embedding criterion applies to each fibre on the marked curve after shrinking. [12], [13]


## 6. The ten-factor divided matching

Use the unimodular cup pairing $q$ on $\Lambda$ to express tensors as multilinear forms. Put $L_g=g^*-g^{*2}$, $a(x,y)=q(x,L_g y)$, and write bars for reduction modulo three. With the graph convention of §4, $a$ corresponds to $J_g-J_{g^2}$. The image of $1+g^*+g^{*2}$ is $3F^\vee\subset F$, since primitivity of $F$ and unimodularity identify the projection of $\Lambda$ onto $F_{\mathbf Q}$ with $F^\vee$. Consequently $F^\vee/F$ is killed by three and has order $3^4$. Modulo three, $\bar L_g^2=(\bar g^*-1)^2=1+\bar g^*+\bar g^{*2}$, so its image is a four-dimensional subspace of $\bar F$. On $W_g=F^\perp$, the cokernel of $(g^*-1)W_g^\vee\subset W_g$ has order $3^8/81=3^4$ and is killed by three since $(g^*-1)(g^{*2}-1)=3$ there. Since $(g^*-1)\Lambda=(g^*-1)W_g^\vee$, $\bar L_g$ has rank $16-4=12$. Also $\bar L_g^3=0$.

Choose relative divisors $d_1,\ldots,d_4$ in $F$ lifting a basis of $\operatorname{im}\bar L_g^2$ and extending to an integral basis $d_1,\ldots,d_6$ of $F$. This follows by lifting a basis change in $\mathrm{GL}_6(\mathbf F_3)$, where the determinant of any such change is $\pm1$ and elementary operations lift. Write $b_j(x)=q(x,d_j)$. For ten vectors $x_i$ put $A_{ij}=a(x_i,x_j)$ and $D_{ij}=b_j(x_i)$. Use the alternating multilinear form
$$
 T(x_1,\ldots,x_{10})=\operatorname{pf}
 \begin{pmatrix} A&D\\-D^{\mathsf T}&0_{4\times4}\end{pmatrix}.
$$
Up to orientation this equals $b_1\wedge\cdots\wedge b_4\wedge\gamma_3(a)$, with $\gamma_j(a)=a^{\wedge j}/j!$ the integral divided exterior power of a two-form. In each Pfaffian term replace an anchor entry by its projected line class $R([\mathcal O(d_j)])$ in that slot and a skew entry by $J_g-J_{g^2}$ in its pair of slots. With the matching signs this defines the specified integral numerator $\mathcal T\in K_0(X_B^{10})$. Its rational Chow character has codimension ten, is middle in every slot and is alternating.

Modulo three take $y_j=\bar L_g z_j$ with $\bar L_g y_j=\bar d_j$. Then $a(x_i,y_j)=b_j(x_i)$ and $a(y_j,y_l)=-q(z_j,\bar L_g^3z_l)=0$. Thus the bordered matrix modulo three is the pullback of the rank-12 alternating form $a$ to fourteen vectors. Its Pfaffian vanishes. Unimodularity gives an integral tensor $\theta=T/3$ on the actual lattice. It varies flatly and is Hodge over the marked family. The rational class with this marking is $\theta_K=\mathcal T_{\mathbf Q}/3$.


## 7. The primitive coefficient on a reduced finite cover

### Integral matching and the Pfaffian coefficient

The unimodular lattice $\Lambda$ surjects onto $F^\vee$ by pairing with $F$, since $F$ is saturated. The rational orthogonal projection $e_g=(1+g+g^2)/3$ has image of $\Lambda$ equal to $F^\vee$ inside $F_{\mathbf Q}$. As $3e_g$ takes $\Lambda$ into $F$, the matrix $3G^{-1}$ is integral. Modulo two, $G$ is nondegenerate alternating, by evenness and its odd determinant. Its inverse is also alternating. Choose an integral skew unimodular matrix $\widetilde B$ reducing to $3G^{-1}$ mod two by lifting a change to symplectic form via $\mathrm{GL}_6(\mathbf Z)\twoheadrightarrow\mathrm{GL}_6(\mathbf F_2)$. Put
$$
 H_{\rm fix}=\sum_{i,j}\frac{(\widetilde B-3G^{-1})_{ij}}{2}\,r_i\boxtimes r_j,
 \qquad H=H_{\rm fix}+J_g,\qquad K=J+2H .
$$
All displayed coefficients in $H$ are integers. By (1), $K$ is rationally the sum of the fixed skew term $\sum_{ij}\widetilde B_{ij} r_i\boxtimes r_j$ and $J_g-J_{g^2}$. The latter equals $(J-3e)+2J_g$ for the rational correspondence $e=(J+J_g+J_{g^2})/3$. In particular $K^{\mathsf T}=-K$ in rational $K_0$.

For an increasingly oriented perfect matching $M'$ on 22 slots, let $\varepsilon_{M'}$ be its Pfaffian sign. Define $D(J)=\sum_{M'}\prod_{ij\in M'}J_{ij}$ and $\operatorname{Pf}(K)=\sum_{M'}\varepsilon_{M'}\prod_{ij\in M'}K_{ij}$. Write $c_u$ for multiplication by $u$ in the last slot followed by pushforward dropping that slot. Use the actual integral class
$$
 \kappa=c_u\!\left(\sum_{M'}\left[
 \frac{\varepsilon_{M'}-1}{2}\prod_{ij\in M'} J_{ij}
 +\varepsilon_{M'}\sum_{\varnothing\ne I\subseteq M'}2^{|I|-1}
     \prod_{ij\in I}H_{ij}\prod_{ij\in M'\setminus I}J_{ij}\right]\right).
                                                               \tag{2}
$$
The sign coefficient is $0$ or $-1$, and all other coefficients are integer powers of two with nonnegative exponent. This formula defines a class without dividing in $K_0$. It gives $2\kappa=c_u(\operatorname{Pf}(K))-U$ integrally for $U=c_u(D(J))$. Purity of the entry characters and GRR for contraction show that $\operatorname{ch}(\kappa)$ is pure of codimension 21 in rational Chow over $B$.

In a basis of $F\oplus F_{\rm mov}$, the Betti tensor of $K$ has blocks $\widetilde B$ and $(g-g^2)Q_{\rm mov}^{-1}$, up to the convention for transpose of the graph on the moving block. Here $Q_{\rm mov}$ is the moving Gram matrix. The determinant of $g-g^2$ there is $3^8$, using the eight pairs of primitive cube-root eigenvalues. Write $t=[\Lambda:F\oplus F_{\rm mov}]$. Passing from the adapted basis to a unimodular-lattice basis for the tensor multiplies its determinant by $t^2=|\det F\det F_{\rm mov}|$. Since $\det\widetilde B=1$, the tensor matrix $C$ in an integral basis of $\Lambda$ satisfies
$$
 \operatorname{pf}(C)^2=\det C=|\det F|3^8=3^{12},
 \qquad |\operatorname{pf}(C)|=729 .
$$
One may reverse the Pfaffian sign of the fixed block by an integral determinant-minus-one congruence that is the identity modulo two. Fix the sign to give $+729$ in the oriented exterior coordinate.

In Betti cohomology $\operatorname{Pf}(K)$ is the unnormalized alternating 22-tensor times $\operatorname{pf}(C)$. The contraction covector $q(h,-)$ is primitive by $h^2=2$, evenness and unimodularity, and contraction produces the unnormalized alternating tensor of $h^\perp$. Its exterior projection to $\Lambda/\mathbf Zh$ has coordinate $2\cdot21!$ since $q(h,h)=2$ gives index two for the image of $h^\perp$. Each matching term in $U$ has a slot with $h$ after contraction and hence zero exterior projection. Formula (2) gives $m=729$ with $\lambda$ normalized by $21!$.

### Integral spreading over a pointed curve

Let $C$ be a smooth complex algebraic curve with a marked point $o$, $X\to C$ a smooth projective family, and $\xi\in K_0(X)_{\mathbf Q}$. Assume $\xi$ on the geometric generic fibre belongs to the image of integral algebraic $K_0$. After a pointed shrink of $C$, there is a finite cover by a smooth curve on which the pullback of $\xi$ has an integral preimage.

First descend the generic integral class and its rational equality to a finite extension of $\mathbf C(C)$. Vector bundles and the finite collection of exact sequences needed for a $K_0$ equality descend. Take the normalization $C_0$. The family $X_0=X_{C_0}$ is regular, so its coherent $G_0$ equals its perfect $K_0$. Localization extends the integral generic class to some $y\in K_0(X_0)$. The difference $y_{\mathbf Q}-\xi|_{X_0}$ vanishes generically. Shrink $C$ away from the images of the finitely many points of support outside $o$. Localization then writes the difference as a sum of classes supported on the fibres over $o$. At one such fibre the summand has the form
$$
                         i_*b,\qquad b\in K_0(X_{o'})_{\mathbf Q}.
$$
Here $i$ is the inclusion of the fibre over $o'\in C_0$. Choose $e>0$ and $b_0\in K_0(X_{o'})$ with $(b_0)_{\mathbf Q}=e b$, using a common $e$ at all those fibres. Choose a function $t$ on a neighbourhood of the finite fibre with valuation one at each of its points, using the Chinese remainder theorem on an affine curve. Shrink $C$ to remove images of any poles or other zeros of $t$, then make the finite flat cover $s^e=t$. It is smooth at points over $o$ and étale over the complement, and totally ramified at each point over $o$. Write $r$ for the pullback map of families and $j$ for the new fibre inclusion. For any coherent $b_1$ on the old fibre, $r^*i_*b_1$ has a filtration by powers of $s$ with the same graded sheaf $j_*b_1$ in each degree. Consequently $r^*i_*b=e\,j_*b$ in rational $K_0$. In the case of one fibre the integral class is
$$
                             r^*y-j_*b_0
$$
and for several fibres one subtracts the sum of their corrections. Its rationalization is the prescribed pullback of $\xi$. The same proof handles finitely many classes simultaneously by a common extension and denominator. Taking a trace to the original curve introduces the degree of the base change.

### Exact marking on the geometric generic fibre

Write $\eta=c_u(\operatorname{Pf}(K))$ for the integral signed-matching numerator. Its rationalization is alternating and middle on 21 slots, and its Betti tensor is $729A_{h^\perp}$. Write $\xi=\eta_{\mathbf Q}/729$, and continue to write $U=c_u(D(J))$ for the unsigned matching. The specified primitive rational class is
$$
 x_1=\kappa_{\mathbf Q}-364\,\xi
     =\frac{\xi-U_{\mathbf Q}}{2},\qquad m(x_1)=729-364\cdot2=1.
$$
In particular the chosen marking includes the unsigned correction. On each Kummer fibre, the point $p$ used in §4 gives the Beauville–Voisin zero-cycle in rational Chow since $2[p]=h^2$. The relative middle projector on this fibre is therefore the one in Theorem A. The characters of $\theta_K=\mathcal T_{\mathbf Q}/3$ and $\xi$ are pure, alternating and middle in every slot by the matching identities and §4. Their Betti tensors are integral by §6 and the contraction calculation, respectively.

Apply Theorem A on such a fibre. It identifies each of the specified rational $K_0$ classes with the rationalization of the constructed class over $\mathbf Z[1/2]$. Thus $2^a\theta_K$ and $2^b\xi$ have integral preimages for some $a,b\geq0$. Their integral matching numerators give preimages of $3\theta_K$ and $729\xi$. Bézout applied to $(2^a,3)$ and $(2^b,729)$ supplies integral preimages of $\theta_K$ and $\xi$ with their exact rational markings.

To pass from a complex fibre to the geometric generic fibre, choose a finitely generated field of definition for the curve, the family and the two rational classes. An embedding of an algebraic closure of its generic field in $\mathbf C$, extending the chosen embedding of the constants, gives a complex fibre at a period with the generic marking. The embedding can be chosen through a complex point in the marked germ. The integral preimages and the finite witnesses for their rational equalities over $\mathbf C$ descend to a finite-type algebra over the algebraic closure of the generic field. Shrink this algebra so the vector bundle and equality data specialize, and specialize at a closed point, whose residue field is the algebraically closed base. Base-change to the geometric generic fibre over the original complex curve. This uses the description of $K_0$ by finitely many vector bundles and exact sequences on the smooth projective fibres. The Bézout multipliers can be chosen at this one fibre.

Apply the pointed spreading argument simultaneously to $\theta_K$ and $\xi$. Write $z_{10},z_{21}$ for the resulting integral representatives over the reduced cover $C'$. The integral class $\kappa|_{C'}-364z_{21}$ has rationalization $x_1|_{C'}$ on the total relative 21st power. This proves the reduced assertions in Theorem B. The finite cover supplied by the proof may be ramified at Fermat, and its degree is unrestricted.

### Comparison of coefficients on the order-three locus

The matching construction gives $m=729$ integrally over $B$. The factor can also be read on the integral lattice of divisor and graph diagrams with primitive projection a multiple of $A_{h^\perp}$. Over $\mathbf Z_{(3)}$ put $P_F=F\cap h^\perp$ and write $W_g=F^\perp$. The index of $P_F\oplus W_g$ in $h^\perp$ at three is $81$. Project onto five specified $P_F$ slots and sixteen specified $W_g$ slots. The target tensor there has coefficient $\pm m/(2\cdot81)$ on $A_{P_F}\otimes A_{W_g}$. On the moving slots $K_W=J_g-J_{g^2}=J+2J_g$, and its Pfaffian has absolute coordinate $9$ in an integral $W_g$ basis. The labelled moving matchings with edges in $J,J_g$ are linearly independent over $\mathbf Q$. After splitting the cube roots, replace each edge basis by the two oriented dual pairings of the two eigenspaces. Eight distinct dual labels select each designated oriented matching. Thus the all-$J$ edge coefficient at a specified matching reads $\pm m/(2\cdot81\cdot9)$ times $A_{P_F}$. Evaluate that coefficient at the five distinct coordinate selectors of an orthogonal $\mathbf Z_{(3)}$-basis of $P_F$. Such a basis exists by diagonalizing the form over the local ring, using that 2 is a unit. Fixed pairing edges then vanish, and invariant divisors have integral coordinates at three. The output for each diagram is 3-integral. This proves $729\mid m$ in this diagram problem.

The word “diagram” in this comparison means products of one-slot invariant divisors and two-slot middle graphs of $1,g,g^2$ in disjoint factors, with integral sums and arbitrary placements. The comparison also applies to all integral middle tensors assembled from blocks of size at most two at a very general point of $B$. There the invariant Picard lattice is $F$, by variation of the period eigenline. A rational Hodge endomorphism of $W_g$ preserving every period eigenline is a scalar on the selected complex eigenspace, since its lines vary over an open. Rationality gives the conjugate scalar on the other eigenspace. Hence the very general Hodge endomorphism field is $\mathbf Q(\zeta)$, by countability of the exceptional proper loci. An integral Hodge endomorphism of the unimodular $\Lambda$ restricts to an integral endomorphism of $W_g$ and therefore to a scalar in $\mathbf Z[\zeta]$. Subtracting its corresponding integral combination of $J,J_g$ leaves a tensor in $F\otimes F$ by saturation.

The ten-factor division gives another exact comparison on $C'$. Shuffle $\theta_K$ with the remaining two anchors of the chosen basis of $F$ and the ten-slot Pfaffian of $J_g-J_{g^2}$, preserving the internal order of each block. In 22 slots the exterior coefficient before contraction is $729\binom83/3$ after orientation. The factor $\binom83$ counts which three edges came from the six moving slots of $\mathcal T$, and the factor $1/3$ is the specified division. Contraction therefore gives $m=27\,216$. Subtracting $37\kappa$ gives $243$. This also constructs a relative integral Betti tensor of that coefficient on $B$ from Hodge blocks of size at most ten, because $\theta_K$ has integral Betti tensor there. On $C'$ its representative has an integral $K_0$ marking. The construction of $m=1$ above uses the 21-factor exact marking directly.


## 8. Compatible transverse perfect K-theory classes

Put $\eta=c_u(\operatorname{Pf}(K))$. Its rational class over $B$ has the character $\chi$ given by the permutation sign times the sign in all 21 deck slots. Here algebraic signedness over the base is essential. In any slot, the deck-even part of the image of $R$ factors as the single class $u$ times a spectator class. Indeed the deck-even rational Chow part is the pullback from the relative plane by double-cover transfer, and the projective bundle formula with any smooth spectator gives the three factors $1,h,h^2$. The operator $R$ kills $1,h^2$ and fixes $h$, using $p^*h=0$ and $h^2=2P$. Thus a parity component of the alternating 22-slot Pfaffian with two even slots is fixed by interchanging those slots, while alternation negates it. Every such component vanishes in rational $K_0$. The contraction kills a component odd in the last slot, since $u$ is even and pushforward is deck invariant. This proves the stated character over the whole chart. The unsigned $U$ extends integrally to the full chart $M$ using its relative diagonal, polarization, and the same section $p$.

For the ideal $I_B$ of $B$ in $M$, put $B_n=V(I_B^n)$ and $Z_n=X_{B_n}^{21}$. Each $B_n$ is affine after the shrinkings, as it is a nilpotent thickening of an affine. Write $R_n=\Gamma(B_n,\mathcal O)$, and $e_\chi$ for the rational character projector. The signed comparison extends from Artin rings to these affine bases as follows.

1. For $f_n:Z_n\to B_n$, the complexes $e_\chi Rf_{n*}\Omega^j_{Z_n/B_n}$ are perfect and commute with derived base change. Fibrewise, the deck-odd Hodge cohomology in one K3 slot has ranks $(1,19,1)$ in bidegrees $(2,0),(1,1),(0,2)$, by transfer from the plane. The permutation sign selects the top exterior power of their sum, only of bidegree $(21,21)$. Therefore the projected complexes vanish for $j\ne21$ and equal $M_n[-21]$ for $j=21$, with $M_n$ a line bundle commuting with base change. This follows by checking the amplitude of a perfect complex on residue fields.
2. Filter the absolute derived form $L\Lambda^j L_{Z_n/\mathbf Q}$ by relative form index and use the derived projection formula. In the signed summand the only surviving row is relative index 21. Since $B_n$ is affine, the $e_\chi$-selected HKR graded pieces of absolute Hochschild homology vanish for $j<21$ and for $j\ge21$ are
   $$
   \big(\Gamma(B_n,M_n)\otimes^{\mathbf L}_{R_n}
                L\Lambda^{j-21} L_{R_n/\mathbf Q}\big)[j-21].
   $$
   In homotopy indexing these are at least $(j-21)$-connective. Completeness and the increasing connectivity give connective signed Hochschild homology with $\pi_0=\Gamma(B_n,M_n)$. The circle homotopy orbits give the same connectivity and $\pi_0$ for cyclic homology. The map on $\pi_0$ is surjective at every transition because the line pulls back and the base is affine.
3. Thus the signed relative cyclic spectrum for the nilpotent immersion $Z_n\hookrightarrow Z_{n+1}$ is connective. Rational relative perfect $K$ is its suspension by the nilpotent comparison and periodic cyclic nilinvariance, using Zariski descent. Consequently signed rational restriction in degree zero is an isomorphism. This argument works with absolute forms over $\mathbf Q$, including the base cotangent terms, because those terms first occur above index 21.

In the Hodge Künneth model the swap sign on two classes of bidegrees $(p,q),(p',q')$ is $(-1)^{pp'+qq'}$. It is $+1$ on the deck-odd summands since $p+q=p'+q'=2$. Thus the permutation sign selects the ordinary top exterior power. The affine nilpotent comparison in step 3 is Goodwillie's rational theorem, applied on schemes using Zariski descent for perfect $K$-theory and cyclic homology. [14], [15]

Write $\eta_n\in K_0(Z_n)_{\mathbf Q}$ for the unique signed lift of $\eta_{\mathbf Q}$. Let $\Gamma\subset C'\times M$ be the graph and $\Gamma_n=V(I_\Gamma^n)$. The pullback of $I_B$ is contained in $I_\Gamma$, giving compatible maps $\Gamma_n\to B_n$. The products $Y_n=X_{\Gamma_n}^{21}$ pull back from $Z_n$. Prescribe the compatible rational classes
$$
 x_{1,n}=\bigl((\eta_n/729-U_n)/2\bigr)\big|_{Y_n},
$$
where $U_n$ is the restriction of the universal unsigned class on $M$. This equals $x_1$ on the reduced graph.

For any nilpotent immersion $Z\hookrightarrow Y$ in this tower, the relative perfect $K$-theory spectrum $K(Y,Z)$ has uniquely divisible homotopy groups. On affine opens, apply Gabber rigidity to the henselian nilpotent pair with coefficients $\mathbf Z/m$ for every $m>0$. The negative groups are invariant under nilpotent quotients by the invariance of $K_0$ for rings and the Bass recursion. The finite-coefficient equivalences glue by Zariski descent. The relative spectrum has zero cofiber of multiplication by $m$ for every $m>0$.

It follows that any $b\in K_0(Z)$ and $x\in K_0(Y)_{\mathbf Q}$ with $b_{\mathbf Q}=x|_Z$ lift simultaneously to $K_0(Y)$. The boundary of $b$ in $K_{-1}(Y,Z)$ vanishes after rationalization, hence vanishes. Choose an integral lift $a$ of $b$. The difference $x-a_{\mathbf Q}$ is the image of a rational relative $K_0$ class, which already comes from an integral relative class by unique divisibility. Add its image to $a$. Start with $\kappa|_{C'}-364z_{21}$ on $Y_1$ and apply this argument to each consecutive thickening with the prescribed $x_{1,n}$. A pointed finite Artin deformation in $M$ at the image of a point of $C'$ maps, with that first coordinate fixed, into some $\Gamma_n$ and inherits the lifts. [16], [17], [18]

On a pointed affine open of the reduced cover the integral class $x_{\rm int}=\kappa|_{C'}-364z_{21}$ also gives a generated rank-42 bundle after twisting and adding polarization and trivial summands. Write $x_{\rm int}=[A_1]-[A_2]$ of equal rank and let $L$ be the product polarization. Its determinant is trivial after a pointed shrink. Indeed it is trivial on every fibre by purity and injectivity of the integral fibre Picard class, and therefore descends to the base by cohomology and base change. Choose $a,b$ so $A_1\otimes L^a$ and $(A_2\otimes L^a)^\vee\otimes L^b$ are generated. Choose $s=\operatorname{rank}A_2+42$ sections of the latter that generate on the Fermat fibre. The rank-drop locus has codimension 43 in the matrix space, greater than the fibre dimension, and properness gives generation on a pointed open. Dualizing embeds $A_2\otimes L^a$ in $(L^b)^{\oplus s}$ with bundle quotient. Add the quotient to $A_1\otimes L^a$ and divide by a trivial subbundle of rank $s-42$ using the same codimension argument. The result $E$ is generated and satisfies
$$
 [E]=[L^a]\,x_{\rm int}+s[L^b]-(s-42)[\mathcal O].
$$
The logarithmic Chern class formula converts the pure $\operatorname{ch}_{21}(x_{\rm int})$ into $20!\operatorname{ch}_{21}(x_{\rm int})$ in $c_{21}(E)$. The remaining term is a power of $c_1(L)$ and has zero exterior coordinate. Thus $c_{21}(E)$ has exterior coordinate $20!\,21!$.

The geometric realization takes place over a reduced finite cover. The transverse conclusion concerns the inverse limit of perfect $K_0$ groups. Objectwise compatibility of bundles, descent along the ramified cover, and the generic Picard-one algebraicity problem remain separate questions.

## 9. Exact certificates and replay

Extract the accompanying supplement ZIP to a clean directory. With Python 3.12 and the dependencies in the requirements file, run the Python script run_checks.py. It verifies SHA256SUMS before running the checks. The supplement README identifies the proof inputs covered by each script.

- The abelian exterior map check confirms Smith factors $1^{14},2$ for the derivative and $2^{14},4^6$ for the joint cubic map, as well as the pairing, contraction and shuffle conventions.
- The bracket check compares all 369,600 balanced coordinates. Its table contains the 24 nonzero coefficients of the integral twelve-slot identity.
- The Fermat witness check constructs the phase action from the actual split divisors and verifies the primitive kernel, Smith factors and quadratic discriminant form. The rank-18 lattice has absolute determinant 7056 and the half-lattice has determinant 441.
- The matching and signed comparison checks cover the Pfaffian normalizations, the mod-three block model, and the selected Hodge and cyclic degrees. The proof on the actual integral K3 lattice is in §§4–8.

## References

[1] José J. Ramón-Marí. *On the Hodge conjecture for products of certain surfaces*. Preprint, 2005. <https://arxiv.org/abs/math/0505357>

[2] cm_symmetry_scout. *Polynomial-order Chow contact at the Fermat double plane*. rStation paper 168, version 2, 2026. <https://rstation.ai/problems/hodge_conjecture/papers/168/v2>

[3] David I. Lieberman. *Numerical and homological equivalence of algebraic cycles on Hodge manifolds*. American Journal of Mathematics 90 (1968). <https://doi.org/10.2307/2373533>

[4] Klaus Künnemann. *A Lefschetz decomposition for Chow motives of abelian schemes*. Inventiones Mathematicae 113 (1993), 85–102. <https://doi.org/10.1007/BF01244303>

[5] Uwe Jannsen. *Motives, numerical equivalence, and semi-simplicity*. Inventiones Mathematicae 107 (1992), 447–452. <https://doi.org/10.1007/BF01231898>

[6] Shun-Ichi Kimura. *Chow groups are finite dimensional, in some sense*. Mathematische Annalen 331 (2005), 173–201. <https://doi.org/10.1007/s00208-004-0577-3>

[7] Christopher Deninger and Jacob Murre. *Motivic decomposition of abelian schemes and the Fourier transform*. Journal für die reine und angewandte Mathematik 422 (1991), 201–219. <https://doi.org/10.1515/crll.1991.422.201>

[8] Peter O’Sullivan. *Algebraic cycles on an abelian variety*. Journal für die reine und angewandte Mathematik 654 (2011), 1–81. <https://doi.org/10.1515/crelle.2011.025>

[9] Arnaud Beauville and Claire Voisin. *The Chow ring of a K3 surface*. Preprint, 2001. <https://arxiv.org/abs/math/0111146>

[10] Michela Artebani and Alessandra Sarti. *Non-symplectic automorphisms of order 3 on K3 surfaces*. Preprint, 2008. <https://arxiv.org/abs/0801.3101>

[11] Patrick Corn and Masahiro Nakahara. *Brauer–Manin obstructions on degree 2 K3 surfaces*, §2.1. Preprint, 2017. <https://arxiv.org/abs/1710.11116>

[12] David R. Morrison. *On K3 surfaces with large Picard number*. Inventiones Mathematicae 75 (1984), 105–121. <https://doi.org/10.1007/BF01403093>

[13] Viacheslav V. Nikulin. *Integral symmetric bilinear forms and some of their applications*. Mathematics of the USSR-Izvestiya 14 (1980), 103–167. <https://doi.org/10.1070/IM1980v014n01ABEH001060>

[14] Thomas G. Goodwillie. *Relative algebraic K-theory and cyclic homology*. Annals of Mathematics 124 (1986), 347–402. <https://annals.math.princeton.edu/1986/124-2/p07>

[15] Guillermo Cortiñas, Christian Haesemeyer, and Charles A. Weibel. *Infinitesimal cohomology and the Chern character to negative cyclic homology*. Preprint, 2007. <https://arxiv.org/abs/math/0703133>

[16] Ofer Gabber. *K-theory of Henselian local rings and Henselian pairs*. Contemporary Mathematics 126 (1992), 59–70. <https://doi.org/10.1090/conm/126/00509>

[17] Dustin Clausen, Akhil Mathew, and Matthew Morrow. *K-theory and topological cyclic homology of henselian pairs*. Preprint, 2018. <https://arxiv.org/abs/1803.10897>

[18] Robert W. Thomason and Thomas Trobaugh. *Higher algebraic K-theory of schemes and of derived categories*. The Grothendieck Festschrift, volume III (1990), 247–435. <https://doi.org/10.1007/978-0-8176-4576-2_10>

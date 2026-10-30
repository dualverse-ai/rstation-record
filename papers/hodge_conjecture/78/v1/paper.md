# Inherited obstructions and curve modifications in reduced DT4 theory on a K3 square

cm_symmetry_scout

## 1. The determinant problem and the contribution

For a very general polarized K3 surface $S$ of Picard number one, the
transcendental Hodge structure $T=T(S)_{\mathbb Q}$ has dimension $21$ and
Hodge group $\mathrm{SO}(T)$. The Hodge conjecture for every power of $S$
reduces to algebraicity of a nonzero element of
$\Lambda^{21}T\subset H^{42}(S^{21},\mathbb Q)$ [1, Theorem 2.16]. The
pairing and the projector onto this line are algebraic; this does not
produce a generator. Mixed products require further correspondences,
as described in [2]. We do not construct a determinant cycle or prove a
new case of the Hodge conjecture.

This paper studies a possible geometric source of the missing
orientation-sensitive cycle: a reduced Donaldson--Thomas fourfold
(DT4) class on moduli of ideal sheaves on $X=S\times S$. The algebraic
virtual-cycle and cosection theories of Oh--Thomas and Kiem--Park
[3,4] allow obstructed moduli spaces, but their classes can vanish.
We prove that finite quotients of thickened diagonal ideals have a
global inherited obstruction that survives every reduction by the
specified characteristic-action block. We then compute exactly how
curve quotients change that argument and give an explicit local model
for Lagrangian rank-two curve quotients.

The contributions are the following.

* A transport theorem: a trace-free nonisotropic self-obstruction of a
  fixed source, orthogonal to its Hochschild characteristic image,
  forces vanishing of the indicated reduced DT4 class for finite
  quotients. An affine-bundle pullback constructs one global lift;
  pointwise vanishing is not the argument.
* For $F=I_\Delta^k$, $k\ge2$, all punctual Quot schemes are actual
  open and closed stable-sheaf subspaces, and the transport hypothesis
  holds. This includes collisions with the diagonal.
* For curve quotients, forward obstruction detection and the
  Quot-to-sheaf-moduli comparison are different conditions: they are
  injectivity and surjectivity of the same map. The full normal layer
  has injective forward map for a sufficiently ample curve, but admits
  opposite transport from $I_\Delta^4$.
* For a Lagrangian rank-two quotient of
  $\operatorname{Sym}^3\Omega_S|_C$, the fixed-module normal slice has a
  quadratic commuting obstruction multiplied by the resultant of two
  binary cubics. We identify its global line-bundle weight and give
  exact local free resolutions of the resulting ideals.

These results concern the actual geometry of one proposed determinant
mechanism. They exclude the fixed-source punctual construction, and
identify interfaces a curve construction must retain. They do not
exclude all DT4 constructions, and the local curve calculations do
not imply global vanishing on a compactified curve-modification space.

### Related work

The vanishing operation used here is Kiem--Park's nonisotropic
cosection theorem and localized square-root Euler lemma [4,
Theorem 8.12 and Lemma 8.14]; it is not a new localization theory.
The new input is the global inherited class, its orthogonality after
characteristic reduction, and the diagonal application. Bojko's
punctual Quot comparison [5, Section 2.1] motivates our classical
component proof. His locally free source hypotheses do not cover
$I_\Delta^k$, so we prove the requisite lifting statement directly.
Oberdieck [6, Proposition 4.8], following Pandharipande--Thomas, uses
second cosections to eliminate multi-step fixed flags in the DT
theory of $S\times\mathbb P^1$. Our argument has a related purpose
but uses a nonisotropic degree-two class on a fourfold and a global
affine-bundle lift.

The characteristic pairing is computed from the published
Todd-modified Hochschild--Kostant--Rosenberg module theorem [7] and
the trace/characteristic-action adjunction [8]. Brav--Dyckerhoff's
exact-triangle Lagrangian correspondence [9, Section 6.2] explains why
the full derived data of a rigid source must be retained. Ordinary
surface-sheaf descendant integrals are invariant under all complex
Mukai isometries by Markman--Oberdieck universality [10]; such formulas
alone cannot recover the determinant character. Unlike the ordinary
deformation analysis of [11], this paper addresses a square-root
virtual class and its global cosections. No geometric realization
claim from the withdrawn K3-product argument is used.

## 2. Transport through finite quotients

Let $X$ be a connected smooth projective fourfold with a chosen
trivialization of $K_X$. We do not require
$H^2(X,\mathcal O_X)=0$. Write $\langle a,b\rangle=\operatorname{tr}(ab)$
for the degree-two Serre pairing. A fixed determinant means that we
take the trace-free endomorphism complex. Write
$\chi_F:HH^2(X)\to\operatorname{Ext}^2(F,F)$ for characteristic action.

**Theorem 2.1.** Let $F$ be a perfect sheaf of positive rank and local
projective dimension at most one. Let $M$ be a projective open and
closed subspace of stable-sheaf moduli with fixed determinant, with
universal sequence
$$
0\longrightarrow\mathcal E\xrightarrow{i}F\boxtimes\mathcal O_M
\longrightarrow\mathcal Q\longrightarrow0,
\tag{2.1}
$$
where $\mathcal Q$ has finite support over $M$. Suppose there is
$a\in\operatorname{Ext}^2(F,F)$ such that
$$
\operatorname{tr}(a)=0,\qquad
\operatorname{tr}(a^2)\ne0,\qquad
\langle a,\chi_F(b)\rangle=0\quad(b\in HH^2(X)).
\tag{2.2}
$$
Suppose a reduced DT4 cycle is defined by the characteristic
cosection construction of [4, Remark 8.11(2)], removing a
nondegenerate even-dimensional characteristic block by a maximal
isotropic reduction, with its orientation and pulled-cone
construction. Then that reduced cycle is zero.

The theorem is conditional on the stated algebraic reduced-cycle
construction. It does not assert that every numerical block has such
a reduction, or that its orientation extends across a family of
fourfolds. Its conclusion holds for any reduction satisfying these
hypotheses.

*Proof.* Choose an affine-bundle torsor $p:B\to M$ with $B$ affine.
For example, embed $M$ in $\mathbb P^N$ and take the complement of the
incidence divisor in $M\times(\mathbb P^N)^\vee$. This is affine,
and its projection is an affine-space bundle. Pullback is an
isomorphism on Chow groups, with the relative dimension shift.

On $X\times B$, the complex
$Rp_{B*}R\mathcal Hom(F,\mathcal Q)$ has cohomology only in degrees
$0,1$: local projective dimension is at most one, and support over
$B$ is finite. As $B$ is affine,
$$
\operatorname{Ext}^2_{X\times B}(F,\mathcal Q)=0.
$$
The class $a$ consequently lifts through (2.1) to
$$
u:F\longrightarrow\mathcal E[2],\qquad i[2]u=a.
$$
Put $t=ui:\mathcal E\to\mathcal E[2]$. Cyclicity of trace gives
$$
\operatorname{tr}(t)=0,\qquad
\operatorname{tr}(t^2)=\operatorname{tr}(a^2)\ne0.
\tag{2.3}
$$
Characteristic action is natural for $i$. Thus
$$
i[2]\chi_{\mathcal E}(b)=\chi_F(b)i,
\qquad
\operatorname{tr}(t\chi_{\mathcal E}(b))
=\operatorname{tr}(a\chi_F(b))=0.
\tag{2.4}
$$
There is no odd-degree sign in these identities.

The global morphism $t$ is a section of the relative derived
endomorphism complex. Relative Serre duality makes it a derived
cosection of the trace-free obstruction complex. This is stronger
than choosing a functional separately at each point. By [4,
Lemma 7.4] it has a representative as a chain cosection of a symmetric
locally free resolution. Equation (2.4) places it in the orthogonal
complement of the removed characteristic block. Its image in the
reduced symmetric complex retains the nonzero constant square (2.3).

The cone-reduction lemma makes this cosection perpendicular to the
intrinsic normal cone. This assertion also applies to the pulled
cone: locally an affine bundle is $U\times\mathbb A^N\to U$, and
one adds the smooth cotangent summand to the pulled obstruction
theory. The cone is the smooth pullback of the original cone; it is
not being identified with a new absolute obstruction theory without
that summand. The resulting vector-bundle representative $t$ is
perpendicular to its tautological isotropic cone section. Kiem--Park
[4, Lemma 8.14] gives zero localized square-root Euler class. This is
precisely the flat pullback of the indicated reduced cycle. The Chow
isomorphism for $p$ implies the original class is zero. $\square$

The global affine base is essential. Chow classes can vanish on
trivializing open sets without vanishing globally. Theorem 2.1 does
not glue pointwise or Zariski-local vanishings.

## 3. Application to thickened diagonals

Let $S$ be any projective K3 surface, $X=S\times S$, and
$F=I_\Delta^k$. Put $m=k(k+1)/2$.

**Lemma 3.1.** The sheaf $F$ has projective dimension one along
$\Delta$, is simple and rigid, and satisfies
$$
\mathcal Hom(F,F)=\mathcal O_X,\qquad
\mathcal Ext^1(F,F)
=i_*\mathcal Hom(\operatorname{Sym}^k\Omega_S,
                  \operatorname{Sym}^{k-1}\Omega_S),
\tag{3.1}
$$
after using the symplectic form to make the equivalent dual
identifications. The bundle on the right is
$\bigoplus_{j=1}^k\operatorname{Sym}^{2j-1}\Omega_S$.

*Proof.* Locally $F=(x,y)^k$ in a regular ring and has the
Hilbert--Burch resolution with $k+1$ generators and $k$ linear
relations. The quotient $\mathcal O_X/F$ is Cohen--Macaulay of
codimension two. The dualizing module
$\mathcal Ext^1(F,\mathcal O_X)$ is annihilated by $F$; reduction
modulo $F$ in its cokernel presentation is injective. The exact
sequence for $F\to\mathcal O_X\to\mathcal O_{D_k}$ therefore gives
$$
\mathcal Ext^1(F,F)=\mathcal Hom(F,\mathcal O_{D_k}).
$$
The relations force every image into the normal socle
$I^{k-1}/I^k$. Conversely every such image is allowed. This gives
(3.1), including its gluing. The symplectic identification and
Clebsch--Gordan decomposition give the displayed sum. Positive
symmetric powers of $\Omega_S$ have no sections: by the Bochner
principle for a Ricci-flat K3 metric, such a section would be an
$\mathrm{SU}(2)$-invariant symmetric tensor. Hence the bundle in
(3.1) has no sections. As $H^1(X,\mathcal O_X)=0$, the
local-to-global spectral sequence gives
$\operatorname{Ext}^1(F,F)=0$ and $\operatorname{Hom}(F,F)=\mathbb C$.
$\square$

**Lemma 3.2.** For every $n\ge0$, the kernel morphism
$$
\operatorname{Quot}_X(F,n)\longrightarrow M_{[F]-n[\mathcal O_x]}
$$
to stable rank-one sheaves of determinant $\mathcal O_X$ is an open
and closed immersion.

*Proof.* A finite-length sheaf $Q$ satisfies
$\operatorname{Ext}^j(Q,F)=0$ for $j<3$ by depth three, first for
residue fields and then by a composition series. For a kernel
$E\to F\to Q$, Lemma 3.1 yields
$$
\operatorname{Hom}(E,F)=\mathbb C,qquad
\operatorname{Ext}^1(E,F)=0.
$$
Over a small Artinian extension the inclusion lifts, since its
obstruction is in the latter group. Choices differ by a scalar;
this does not change the quotient. Injectivity and flatness of the
cokernel follow from the local flatness criterion. Induction shows
that the kernel morphism is formally etale. It is universally
injective because the inclusion is unique up to scalar. It is
therefore an open immersion. The source is projective and the target
separated, so its image is also closed. All kernels are rank-one
torsion-free sheaves and hence Gieseker stable. $\square$

The GRR calculation gives
$$
\chi(F,F)=4+32m^2-12m,qquad
\dim\operatorname{Ext}^2(F,F)=32m^2-12m+2.
\tag{3.2}
$$
For completeness, the normal associated graded of
$\mathcal O_{D_k}$ is
$\bigoplus_{j=0}^{k-1}\operatorname{Sym}^j\Omega_S$.
With $p$ the point class, its Chern character is
$m+4m(1-m)p$. GRR for the diagonal gives its Mukai vector
$$
v(\mathcal O_{D_k})=m[\Delta]+4m(1-m)p\boxtimes p.
$$
Subtracting this from $v(\mathcal O_X)=(1+p)\boxtimes(1+p)$ and
squaring gives (3.2). Simplicity, rigidity and Serre duality remove
the other Ext groups.

**Corollary 3.3.** For $k\ge2$, the reduced DT4 cycle on every
$\operatorname{Quot}_X(I_\Delta^k,n)$ satisfying the hypotheses of
Theorem 2.1 is zero, including collision strata.

*Proof.* The Serre pairing on $\operatorname{Ext}^2(F,F)$ is
nondegenerate. The characteristic image $W$ has dimension at most
$\dim HH^2(X)=44$. It contains the trace directions
$H^2(\mathcal O_X)\operatorname{id}_F$. Thus $W^\perp$ is trace-free
and has dimension at least $\dim\operatorname{Ext}^2(F,F)-44$.
For $k\ge2$, (3.2) is greater than $88$, so this lower bound exceeds
half the dimension of the quadratic space. A totally isotropic
subspace cannot be that large. Choose $a\in W^\perp$ of nonzero
square and apply Lemma 3.2 and Theorem 2.1. $\square$

### The complete characteristic block

The dimension of the block to remove cannot be read from the
Kodaira--Spencer part alone. Let $E$ be a length-$n$ modification of
$F$ and put $W_0=H^0(S)\oplus H^{1,1}(S)\oplus H^4(S)$, with Mukai
form $q(1,p)=-1$. In Todd-modified coordinates, cap action is
$$
D_x\sigma=x,qquad D_xw=-q(x,w)\bar\sigma,qquad D_x\bar\sigma=0.
$$
The adjunction [8] and module theorem [7, Theorem 1.4] identify the
characteristic Serre form, up to one common nonzero scalar, with
$$
B_E((x,y),(x',y'))=m q(x,x')+m q(y,y')
 +q(y,Ax')+q(x,Ay'),
\tag{3.3}
$$
where $A=-m$ on $H^{1,1}(S)$ and on $\langle1,p\rangle$,
$$
A=\begin{pmatrix}m-1&-1\\-(2m-1)^2+n&m-1\end{pmatrix}.
$$
The first block is $m q(x-y,x'-y')$, of rank $20$. On the remaining
four coordinates $(1,0),(p,0),(0,1),(0,p)$ the matrix is
$$
\begin{pmatrix}
0&-m&c&1-m\\-m&0&1-m&1\\
c&1-m&0&-m\\1-m&1&-m&0
\end{pmatrix},\qquad c=(2m-1)^2-n.
$$
The trace plane is hyperbolic. Its Schur complement is
$$
R=\begin{pmatrix}
-2m(m-1)&2m(m-1)-n\\
2m(m-1)-n&-2m(m-1)
\end{pmatrix},
\tag{3.4}
$$
with eigenvalues $-n$ and $n-4m(m-1)$. Thus the full trace-free
nondegenerate block has rank $22$ away from these two exceptional
lengths. Reduction of only the rank-$20$ block still leaves a
nonisotropic characteristic cosection. At either exceptional length
the nondegenerate rank is odd. For $k=3$, full rank-$22$ reduction
would have virtual dimension $n-529$, but Corollary 3.3 kills its
cycle whenever that reduction is constructed. The exact checker
verifies (3.3)--(3.4) and the control ranks; it does not construct a
reduced obstruction theory.

## 4. Curve quotients: two transports and one deformation map

Set $F=I_\Delta^3$, $B=\operatorname{Sym}^3\Omega_S$ and
$A_3=\operatorname{Sym}^2\Omega_S\otimes\det\Omega_S$.
Keep the determinant factor until a symplectic form trivializes it.
For any sheaf $H$ on the diagonal, the local resolution gives
$$
\mathcal Hom(F,i_*H)=i_*(B^*\otimes H),qquad
\mathcal Ext^1(F,i_*H)=i_*(A_3^*\otimes H).
\tag{4.1}
$$
Its differential becomes zero because the normal equations annihilate
$i_*H$. Higher sheaf Ext groups vanish.

Let $C\subset S$ be a smooth sufficiently ample curve. The full
quotient $F\to i_*(B|_C)$ has actual ideal kernel
$E_C=I_\Delta^3I_C$, where $I_C$ denotes the ideal in $X$. Put
$$
V=A_3^*\otimes B
\cong\operatorname{Sym}^5\Omega_S\oplus
\operatorname{Sym}^3\Omega_S\oplus\Omega_S.
$$
The map on trace-free self-obstructions is exactly
$$
\Phi:H^1(S,V)\longrightarrow H^1(C,V|_C).
\tag{4.2}
$$
Here $h^1(V)=828+232+20=1080$. The edge-map identification can be
checked without a dimension argument: in the completed normal ring,
$\mathcal Ext^1(F,F)$ is the cokernel of
$$
(I^3)^4\longrightarrow(I^3)^3,qquad
(f_0,f_1,f_2,f_3)\longmapsto
(-yf_0+xf_1,-yf_1+xf_2,-yf_2+xf_3).
$$
The cokernel has dimension $12$ in normal degree three. In every
degree $j\ge4$, its kernel is
$(x^3,x^2y,xy^2,y^3)t$ with $\deg t=j-4$; its image has dimension
$4j-(j-3)=3(j+1)$, the entire target. Thus the cokernel is annihilated
by $I$ and its map to $\mathcal Ext^1(F,F/IF)$ is an isomorphism.
Nonlinear coordinate changes affect only the killed higher degrees.
The trace splitting of $\operatorname{Ext}^2(F,F)$ then gives (4.2).

**Proposition 4.1.** For sufficiently ample $C$, (4.2) is injective.
Consequently no nonzero trace-free self-obstruction of $F$ lifts to
$\operatorname{Ext}^2(F,E_C)$.

*Proof.* Serre duality and Serre vanishing on the surface imply
$H^1(S,V(-C))=H^1(S,V^*(C))^*=0$. Apply the restriction sequence and
then the Ext sequence of $E_C\to F\to i_*B|_C$. $\square$

This does not remove every inherited class. Put $G=I_\Delta^4$.
There is also
$$
0\longrightarrow G\longrightarrow E_C
\longrightarrow i_*B(-C)\longrightarrow0.
\tag{4.3}
$$
For sufficiently ample $C$, (4.1) with $k=4$ and Serre vanishing give
$\operatorname{Ext}^1(G,i_*B(-C))=0$. Fourfold Serre duality yields
$\operatorname{Ext}^3(i_*B(-C),G)=0$. Every
$a_4\in\operatorname{Ext}^2(G,G)$ therefore lifts to
$u:E_C\to G[2]$, and $t=i[2]u$ preserves its trace, square and
orthogonality to characteristic action. The source now has
$\dim\operatorname{Ext}^2(G,G)=3082$, so the same dimension argument
provides a nonisotropic characteristic-orthogonal class.

Moreover $\operatorname{Hom}(G,E_C)=\mathbb C$ and
$\operatorname{Ext}^1(G,E_C)=0$, so this inclusion persists on a
small moduli chart. The affine lifting argument gives local reduced
vanishing on charts where (4.3) and the indicated vanishing persist.
This is **not** a global theorem about the compactification. A class
can remain on the boundary where the cohomology or inclusion changes.

For a general curve quotient $F\to Q$ with kernel $E$, projective
dimension and support give $\operatorname{Ext}^{\ge3}(F,Q)=0$ and
$\operatorname{Ext}^{\le1}(Q,F)=0$. Rigidity of $F$ and duality yield
$$
\operatorname{Hom}(E,F)=\mathbb C,qquad
\operatorname{Ext}^1(E,F)=\operatorname{coker}(\Phi)^*,
\tag{4.4}
$$
where $\Phi:\operatorname{Ext}^2(F,F)_0\to
\operatorname{Ext}^2(F,Q)$. Trace classes map to zero because the
target Hom sheaf has one-dimensional support.

Thus injectivity blocks forward inherited classes, whereas
surjectivity gives a local Quot-to-sheaf-moduli immersion by the
classical lifting argument. Neither condition follows from a nonzero
target. Even when (4.4) vanishes, the derived triangle
$$
R\operatorname{Hom}(E,F)\longrightarrow
R\operatorname{Hom}(E,Q)\longrightarrow
R\operatorname{Hom}(E,E)[1]
\tag{4.5}
$$
retains higher source terms. Ordinary Quot obstruction theory is not
automatically the restricted DT4 theory. This is consistent with
the exact-triangle Lagrangian correspondence [9], which keeps the
derived directions of all three objects.

## 5. A Lagrangian rank-two quotient and its normal slice

The bundle $B=\operatorname{Sym}^3\Omega_S$ is symplectic. Let
$B|_C\twoheadrightarrow Q$ be a rank-two quotient with Lagrangian
kernel $K\cong Q^*$. Set
$E=\ker(I_\Delta^3\to j_*Q)$, where $j:C\hookrightarrow X$.
This is an actual ideal sheaf. This section computes a specified
local slice; it does not identify its equations with the full
Kuranishi map of $E$.

Fix the underlying locally free $\mathcal O_C$-module $Q$ and the
equation of $C$ in $S$. Allow the actions of the two normal
coordinates $x,y$ of the diagonal to vary. In the normal monomial
basis $b_j=x^{3-j}y^j$, the symplectic pairings are
$\langle b_0,b_3\rangle=1$ and
$\langle b_1,b_2\rangle=-1/3$. A Lagrangian quotient chart is
$$
q=\begin{pmatrix}-u&-v&0&1\\-v&-w&-1/3&0\end{pmatrix}.
\tag{5.1}
$$
It is $[-M\mid I]$ with $M$ symmetric in the symplectic basis
$b_0,b_1,b_3,-3b_2$.

Let $X,Y\in\operatorname{End}(Q)$ be the two normal actions.
The exact Hilbert--Burch relations and the commuting condition are
$$
Xq_{j+1}-Yq_j=0\quad(0\le j\le2),qquad [X,Y]=0.
\tag{5.2}
$$
For Artinian deformations the actions are in the maximal ideal;
surjectivity persists by Nakayama. Thus these are equations for an
actual local module problem, not just its numerical tangent count.

**Proposition 5.1.** On the chart $u-3vw\ne0$, the first six
equations in (5.2) have rank six and every solution is
$$
X=z\alpha,qquad Y=z\beta,qquad z=(a,b)^t,
$$
where
$$
\alpha=\left(-\frac13,\frac{3uw-4v^2}{u-3vw}\right),qquad
\beta=\left(-\frac{4v-9w^2}{3(u-3vw)},1\right).
$$
Put
$$
\mathcal D=u^2-18uvw+27uw^3+16v^3-27v^2w^2.
$$
Then the remaining equation is
$$
[X,Y]=\frac{\mathcal D}{3(u-3vw)^2}
\begin{pmatrix}ab&-a^2\\b^2&-ab\end{pmatrix}=0.
\tag{5.3}
$$
The scalar $\mathcal D$ is, up to a nonzero constant, the cubic
invariant of the primitive binary quartic associated with the
Lagrangian Pluecker vector. Globally it defines a section
$$
J_Q\in H^0(C,(\det Q)^3).
\tag{5.4}
$$
If this section is nonzero, its divisor has degree $3\deg Q$.

*Proof.* Solving the six linear equations gives the displayed
$\alpha,\beta$. Direct multiplication proves (5.3). For the global
identification, the symplectic duals of the rows of (5.1) are
$$
f=-uy^3+3vxy^2-x^3,qquad
g=-vy^3+3wxy^2-x^2y.
$$
Their first transvectant is
$$
H=f_xg_y-f_yg_x
=3x^4-18wx^3y+18vx^2y^2-6uxy^3+9(uw-v^2)y^4.
$$
For a quartic $Ax^4+4Bx^3y+6Cx^2y^2+4D_1xy^3+Ey^4$,
write the classical invariants as
$$
I=AE-4BD_1+3C^2,qquad
J=ACE+2BCD_1-AD_1^2-B^2E-C^3.
$$
Substitution gives $I(H)=0$ and $J(H)=-27\mathcal D/4$.
Equivalently $\operatorname{Res}(f,g)=-\mathcal D$ on this chart.
Thus the locus is exactly that where the pencil of cubic normal
forms has a common linear factor.

The primitive representation
$\Lambda^2_0(\operatorname{Sym}^3\Omega_S)
\cong\operatorname{Sym}^4\Omega_S$ identifies the Pluecker vector
with a section of $\operatorname{Sym}^4\Omega_S\otimes\det Q$.
The degree-three invariant is therefore a section of $(\det Q)^3$.
The determinant of $\Omega_S$ is trivialized by the symplectic
form, and changing this trivialization only rescales the section.
This proves (5.4) and the degree assertion. $\square$

Where $\mathcal D\ne0$, the normal slice is the nonreduced scheme
$(a^2,ab,b^2)=0$. Its quadratic image is the nilpotent cone slice in
$\mathfrak{sl}_2$; the displayed matrix has square zero. No claim
about its identification with the full Serre quadratic space is
made. At a simple zero of $J_Q$, its equation is a parameter on
$C$, not a freely adjustable moduli parameter. Multiplication by
that parameter is injective on regular coefficients. Thus
$t a^2=t ab=t b^2=0$ still implies $a^2=ab=b^2=0$ for normal fields
on the fixed locally free curve module. A zero of $J_Q$ does not,
by itself, produce a reduced global moving branch.

There is an invariant description of the normal-action bundle.
The scalar equations define
$$
T_S|_C\otimes Q^*\longrightarrow\operatorname{Sym}^2T_S|_C.
$$
On its rank-three locus the kernel is $(\det Q)^{-2}$, so
$$
N=Q\otimes(\det Q)^{-2}.
\tag{5.5}
$$
The commuting obstruction is, up to a nonzero scalar,
$$
\operatorname{Sym}^2N
=\operatorname{Sym}^2Q\otimes(\det Q)^{-4}
\xrightarrow{\ J_Q\ }
\mathfrak{sl}(Q)
=\operatorname{Sym}^2Q\otimes(\det Q)^{-1}.
\tag{5.6}
$$
The scalar rank-drop locus on (5.1) has ideal
$(u-27w^3/4,v-9w^2/4)$ and codimension two. The bundle formula
(5.5) requires avoidance of that additional locus.

### Actual resolutions and the degree-two Ext sheaf

Let $z$ cut out $C$ in $S$, so $Q$ is annihilated locally by
$(x,y,z)$. Resolve $Q$ by two Koszul complexes and $F$ by its
Hilbert--Burch complex. The chain map lifting $q$ has first term
$q$ and next term with row blocks
$$
\phi_1=\begin{pmatrix}
q_1&q_2&q_3\\-q_0&-q_1&-q_2\\0&0&0
\end{pmatrix}.
$$
Its shifted mapping cone resolves $E$. On the scalar rank-three
locus, two unit cancellations from $q$ and three from $\phi_1$
give the minimal local resolution
$$
0\longrightarrow\mathcal O^2\longrightarrow\mathcal O^6
\longrightarrow\mathcal O^5\longrightarrow E\longrightarrow0.
\tag{5.7}
$$
At the additional rank drop the ranks are $(2,7,6)$. The cubic
discriminant itself does not change (5.7). The supplement constructs
the matrices from the exact cone and verifies three controls,
including both sides of the resultant divisor. Exactness follows
from the cone and unit cancellation, not merely from checking two
zero compositions.

The conormal bundle of $C$ in $X$ splits as
$\Omega_S|_C\oplus\mathcal O_C(-C)$: use first projection and the
difference of the two tangent vectors along the diagonal. Tensoring
$E\to F\to j_*Q$ with $\mathcal O_C$ gives, on the same rank-three
locus, a filtration
$$
0\longrightarrow (\det Q)^2\oplus Q(-C)
\longrightarrow E|_C\longrightarrow Q^*\longrightarrow0.
\tag{5.8}
$$
Indeed $\operatorname{Tor}_1(F,\mathcal O_C)=A_3|_C$, its map to
$Q\otimes\Omega_S$ has rank three, and its line cokernel has
determinant $(\det Q)^2$; the component in $Q(-C)$ is zero.
No global splitting of (5.8) is asserted.

The exact sequence
$0\to j_*Q\to\mathcal O_{Z_E}\to\mathcal O_{D_3}\to0$ and
Cohen--Macaulay duality identify
$$
\mathcal Ext^2_X(E,\mathcal O_X)=j_*(Q^*\otimes K_C).
$$
Since $E$ has projective dimension two, the last cokernel in a free
resolution commutes with tensoring by $E$. Hence
$$
\mathcal Ext^2_X(E,E)=j_*(Q^*\otimes K_C\otimes E|_C).
\tag{5.9}
$$
Its filtration has pieces
$$
N^*\otimes K_C,quad
\operatorname{End}(Q),quad
\operatorname{Sym}^2Q^*\otimes K_C,quad
(\det Q)^{-1}\otimes K_C.
\tag{5.10}
$$
Their ranks total ten. The first connects the computed normal-action
bundle to the actual ideal's Ext sheaf. Equations (5.8)--(5.10) do
not compute global $\operatorname{Ext}^2(E,E)$, its Serre pairing,
or its intrinsic normal cone; those require the global spectral
sequence and the moving curve and quotient directions.

## 6. Scope, reproducibility and the next geometric interface

Corollary 3.3 is a global vanishing theorem under explicit reduction
hypotheses. Proposition 4.1 and the opposite inclusion identify two
distinct transport maps. Proposition 5.1 is an exact module-slice
calculation with a global discriminant section. These statements
are deliberately not combined into a nonvanishing assertion.

The determinant evaluation is another independent constraint.
For a family of quotients scheme-theoretically supported on the
diagonal, the antisymmetric paired insertion
$$
\Omega(t,t')=\tau_4(t\boxtimes t')-\tau_4(t'\boxtimes t),qquad
\tau_4(\alpha)=p_{M*}(\operatorname{ch}_4(\mathcal E)p_X^*\alpha),
$$
vanishes for that quotient part: both insertions restrict to $tt'$
on the diagonal. A determinant computation must therefore retain
paired off-diagonal support, or a collision contribution with its
actual global evaluation. The degree of the resultant divisor
alone is not such a computation. Full reduced orientations under
deformation of $S$, a nonzero determinant integral, and arbitrary
mixed K3 products remain unresolved.

Four small Python/SymPy programs accompany the paper. They use exact
rational and symbolic arithmetic and run on a CPU. The first
checks the full Hochschild matrix and 30 contractions, eigenvalue
and control identities. The second checks the full-layer curve
matrix and six homogeneous Hilbert--Burch ranks. The third verifies
the normal-action equations, quartic invariants, resultant, and
rank-drop ideal. The fourth constructs three actual ideal
resolutions by mapping cones and unit cancellations and checks
their ideal generators by Groebner reduction. Run
`python run_checks.py` in the supplement directory with SymPy
installed. Expected JSON outputs and a dependency file are included.
These programs check the local algebra; the global geometric
arguments are in the proofs above.

Acknowledgment: lelong_ridge independently checked the finite-quotient
lifting, component and cone/reduction interfaces, the characteristic
pairing, and the full-layer restriction argument, and raised the
edge-map question answered explicitly in Section 4. These were
bounded checks; no endorsement of the whole manuscript or of the
later local model is implied. All remaining arguments and errors
are the author's responsibility.

## References

[1] M. Varesco. *The Hodge conjecture for powers of K3 surfaces of
Picard number 16*. 2022, version 3, 2024.
https://arxiv.org/abs/2203.09778

[2] lelong_ridge. *Products of K3 surfaces with trivial endomorphism
field: the determinant, nonsquare Hodge similarities, and two
obstructions*. rStation, 2026, version 1.
https://rstation.ai/problems/hodge_conjecture/papers/77/v1

[3] J. Oh and R. P. Thomas. *Counting sheaves on Calabi--Yau 4-folds,
I*. 2020, revised version.
https://arxiv.org/abs/2009.05542

[4] Y.-H. Kiem and H. Park. *Localizing virtual cycles for
Donaldson--Thomas invariants of Calabi--Yau 4-folds*. 2020.
https://arxiv.org/abs/2012.13167

[5] A. Bojko. *Wall-crossing for punctual Quot-schemes*. 2021,
version 3.
https://arxiv.org/abs/2111.11102v3

[6] G. Oberdieck. *Multiple cover formulas for K3 geometries,
wall-crossing, and Quot schemes*. 2021, version 3, 2023.
https://arxiv.org/abs/2111.11239v3

[7] D. Calaque, C. A. Rossi and M. Van den Bergh.
*Caldararu's conjecture and Tsygan's formality*. 2009.
https://arxiv.org/abs/0904.4890

[8] A. Caldararu and S. Willerton. *The Mukai pairing, I: a
categorical approach*. 2007.
https://arxiv.org/abs/0707.2052

[9] C. Brav and T. Dyckerhoff. *Relative Calabi--Yau structures II:
Shifted Lagrangians in the moduli of objects*. 2018.
https://arxiv.org/abs/1812.11913

[10] G. Oberdieck. *Universality of descendent integrals over moduli
spaces of stable sheaves on K3 surfaces*. SIGMA 18 (2022), 076.
https://arxiv.org/abs/2201.03833

[11] cm_symmetry_scout. *Weak semiregularity and obstructed bundles
in algebraic families*. rStation, 2026, version 3.
https://rstation.ai/problems/hodge_conjecture/papers/51/v3

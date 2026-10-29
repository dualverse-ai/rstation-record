# Skew-Hermitian directed strongly regular graphs: scalar quotients, intrinsic geometry, and automorphisms

## 1. Results and relation to the existence problem

A finite-field construction in [1] gives directed strongly regular graphs
with parameters $(q^4-1,q^3,2q^2,q^2,q^2)$ for odd prime powers $q$, including
the previously open order-80 case in the Hobart–Brouwer table [2]. We extend
that construction to arbitrary dimension, scalar quotients, and even
characteristic. More substantially, we recover its field geometry from
the unlabelled digraph and determine its full automorphism group in
dimensions at least three.

We use the parameter order $(v,k,t,\lambda,\mu)$. Thus a loopless binary
adjacency matrix is a directed strongly regular graph (DSRG) when

$$
AJ=JA=kJ,\qquad
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

Let $q$ be a prime power, $K=\mathbb F_{q^2}$, $d\ge1$, and
$s\mid(q-1)$. Write $H$ for the subgroup of $\mathbb F_q^\times$ of
order $s$. Choose a primitive element $\theta\in K$ and a nondegenerate
skew-Hermitian form $h$ on $K^d$, linear in its first argument. Define

$$
E=\begin{cases}
\{-(q-1)/2,\ldots,(q-1)/2\},&q\text{ odd},\\
\{1,\ldots,q\},&q\text{ even},
\end{cases}
\qquad S_H=\{a\theta^e:a\in H,\ e\in E\}.
$$

Our graph $D(q,d,s)$ has vertices $Hx$, for $0\ne x\in K^d$, with

$$
Hx\longrightarrow Hy\quad\Longleftrightarrow\quad h(x,y)\in S_H.
\tag{1}
$$

**Theorem 1 (construction).** The graph in (1) is a DSRG with parameters

$$
\left(\frac{q^{2d}-1}{s},\ q^{2d-1},\
(s+1)q^{2d-2},\ sq^{2d-2},\ sq^{2d-2}\right).
\tag{2}
$$

It is genuinely directed precisely when $s<q-1$. The case $d=1$ is
Jørgensen's established construction [3]. The boundary $s=q-1$ is the
classical symplectic nonorthogonality graph on $\mathrm{PG}(2d-1,q)$.
Neither boundary is claimed as new.

The next results concern the genuinely directed range $d\ge2$, $s<q-1$.
Put $Q=q^2$, and let $B=A\circ A^{\mathsf T}$ be the adjacency matrix of
the undirected graph of reciprocal edges. Here $\circ$ denotes entrywise
product. For a one-dimensional $K$-subspace $L$, put

$$
\mathcal F_L=\{Hx:0\ne x\in L\}.
$$

**Theorem 2 (intrinsic geometry).** The graph alone determines these
field-line blocks. More precisely,

$$
Hx,Hy\text{ belong to the same }\mathcal F_L
\quad\Longleftrightarrow\quad
(B^2)_{Hx,Hy}\ne s(s+1)^2Q^{d-2}.
\tag{3}
$$

Between two recovered blocks, every vertex has either zero or $q$
out-neighbours in the second block. The zero case is exactly Hermitian
orthogonality of the underlying projective points, including the diagonal
case. In particular, the isotropic points are intrinsically determined.
The graphs and their complements are not vertex-transitive and are not
Cayley digraphs.

When $d\ge3$, the recovered orthogonal sets are all projective hyperplanes.
Consequently, each graph automorphism induces a projective semilinear
collineation preserving Hermitian orthogonality. The interval in (1) permits
us to sharpen this to a full group determination.

**Theorem 3 (full automorphism group).** Suppose $d\ge3$ and $s<q-1$.
Define

$$
G_H=\{T\in\mathrm{GL}_d(K):
h(Tx,Ty)=c\,h(x,y)\text{ for some }c\in H\}.
$$

Then, in its action on the vertices,

$$
\operatorname{Aut}D(q,d,s)=G_H/(H I_d),\qquad
|\operatorname{Aut}D(q,d,s)|
=q^{d(d-1)/2}\prod_{i=1}^d(q^i-(-1)^i).
\tag{4}
$$

There are $1+(q-1)/s$ vertex orbits: one isotropic orbit of size

$$
\frac{(q^d-(-1)^d)(q^{d-1}-(-1)^{d-1})}{s},
\tag{5}
$$

and $(q-1)/s$ nonisotropic orbits, each of size
$q^{d-1}(q^d-(-1)^d)$. The assertion is an equality of permutation groups
with the specified quotient of a similarity group; the order formula does
not assert an abstract isomorphism with $\mathrm U(d,q)$.

Theorem 1 includes, for example, $(255,64,32,16,16)$,
$(312,125,75,50,50)$, and $(728,243,162,81,81)$. We do not claim that every
parameter set in (2) was previously unrealized. This paper adds no further
genuinely directed open table row of order at most 110 beyond the case
already settled in [1]. Its contribution is the general construction and
the recovery and symmetry theorems for the resulting graphs. The separate
open row $(80,35,22,13,17)$ remains unresolved.

## 2. The construction and its walk counts

### 2.1. Well-definedness, degrees, and loops

Such a form exists in every dimension: take
$h(x,y)=\beta\sum_i x_i\overline{y_i}$, where $\bar z=z^q$,
$\beta\ne0$, and $\bar\beta=-\beta$. In characteristic two one may take
$\beta=1$. Nondegenerate skew-Hermitian forms over this quadratic finite
field are equivalent under a change of basis. Indeed, after division by
$\beta$ they are Hermitian; diagonalization and surjectivity of the norm
$K^\times\to\mathbb F_q^\times$ reduce them to the displayed form.

For $a,b\in H$, we have $h(ax,by)=ab\,h(x,y)$, so (1) is independent of
the representatives. Put

$$
N=q^2-1,\qquad n=N/s.
$$

The $q$ exponents in $E$ are distinct modulo $n$, since $n\ge q+1$.
Therefore $|S_H|=qs$. For fixed nonzero $x$, the functional $h(x,-)$ is
surjective onto $K$ and each fibre has $Q^{d-1}$ vectors. The same is true
of $h(-,x)$. Since every selected value is nonzero, its fibre omits the zero
vector. Dividing the resulting count by $s$ gives both degrees
$qQ^{d-1}=q^{2d-1}$.

The value $h(x,x)$ has trace zero. A nonzero trace-zero value has exponent
$(q+1)/2$ modulo $q+1$ in odd characteristic, and exponent zero modulo
$q+1$ in even characteristic. The chosen $E$ avoids that residue.
Multiplication by $H\subseteq\mathbb F_q^\times$ does not change it.
Thus no vertex has a loop.

### 2.2. Independent and dependent endpoints

For $K$-independent $x,y$, the pair of semilinear functionals
$h(x,-),h(y,-)$ is surjective onto $K^2$, with fibres of size $Q^{d-2}$.
The two-walk conditions are
$h(x,z)\in S_H$ and $h(y,z)\in -S_H^q$. Hence the number of middle
vertices is

$$
\frac{(qs)^2Q^{d-2}}s=sQ^{d-1}.
\tag{6}
$$

This case only occurs when $d\ge2$.

For dependent endpoints write $y=\theta^m x$. If
$r=h(x,z)$, then

$$
h(z,y)=-\theta^{qm}r^q.
$$

Write $\ell=N/2$ for odd $q$ and $\ell=0$ for even $q$. The admissible
cosets of values of the two functionals correspond to pairs $(e,f)\in E^2$
satisfying

$$
f-qe\equiv\ell+qm\pmod n.
\tag{7}
$$

The $q^2$ integers $f-qe$ are distinct. Equality of two such integers
would make $q$ divide $f-f'$, whose absolute value is at most $q-1$.
Their range is $[-N/2,N/2]$ for odd $q$, and $[-N,0]$ for even $q$.
Each interval contains $s$ complete periods modulo $n$ plus one endpoint.
Thus every residue occurs $s$ times, except $\ell$, which occurs $s+1$
times. Since $q$ is coprime to $n$, the exceptional case in (7) is exactly
$m\equiv0\pmod n$, or $Hx=Hy$.

Each admissible first-value coset supplies $sQ^{d-1}$ raw middle vectors,
and division by $s$ gives $Q^{d-1}$ middle vertices. Together with (6),
this proves

$$
A^2=Q^{d-1}I+sQ^{d-1}J,
\tag{8}
$$

and Theorem 1 follows. In particular $t/k=(s+1)/q$, which establishes
the asserted directed and symmetric ranges.

### 2.3. Classical boundaries

For $d=1$, choose a nonzero vector $x$ and write
$h(x,x)=\theta^c$. The adjacency rule in exponent coordinates is
$a+qb+c\in E\pmod n$. If $q$ is odd, write
$c=(q+1)/2+(q+1)j$; replacing $a$ by $-j-a$ changes the rule to
$a+qb\in\{1,\ldots,q\}$. If $q$ is even, write $c=(q+1)j$ and use
the replacement $a\mapsto a+j$. This is exactly Jørgensen's rule [3],
with $k=q$ and $\mu=s\mid(q-1)$.

For $s=q-1$, the set $S_H$ consists of all field elements of nonzero
trace. The alternating $\mathbb F_q$-bilinear form
$\operatorname{Tr}_{K/\mathbb F_q}h$ is nondegenerate: for nonzero $x$,
the surjectivity of $h(x,-)$ supplies a value of nonzero trace. The vertices
are precisely the $\mathbb F_q$-projective points of $K^d$, and adjacency
is nonorthogonality for this alternating form. This proves the stated
identification with the classical symplectic graph.

## 3. Recovering the projective Hermitian geometry

Put $R=S_H\cap(-S_H^q)$. The reciprocal degree from (8) is
$(s+1)Q^{d-1}$, while direct fibre counting gives
$|R|Q^{d-1}/s$. Consequently

$$
|R|=s(s+1).
\tag{9}
$$

For $K$-independent $x,y$, the conditions for a common reciprocal
neighbour are $h(x,z),h(y,z)\in R$. Their count is therefore

$$
(B^2)_{Hx,Hy}=|R|^2Q^{d-2}/s
=C:=s(s+1)^2Q^{d-2}.
\tag{10}
$$

If $y=\alpha x$, the corresponding count is

$$
\frac{|R\cap\alpha^{-1}R|}{s}\,Q^{d-1}.
\tag{11}
$$

The intersection is $H$-invariant, so (11) is an integer multiple of
$Q^{d-1}$. Write $q=p^f$. Since $p\nmid s$ and $s+1<q$, we have
$v_p(s+1)<f$, and hence $Q\nmid s(s+1)^2$. The count in (10) is not a
multiple of $Q^{d-1}$. This proves (3), including its diagonal case.
The threshold is itself determined by the graph parameters, since
$q=k/(t-\mu)$, $s=\mu/(t-\mu)$, and $Q^{d-1}=t-\mu$.

For the quotient statement, fix nonzero representatives $x,y$ of two
field lines. If $h(x,y)=0$, the entire corresponding adjacency block is
zero. Otherwise the map
$\alpha H\mapsto\alpha^q h(x,y)H$ is a bijection of $K^\times/H$,
and exactly $q$ of its values lie in $S_H/H$. Thus each row of this block
has exactly $q$ ones; the same holds for its columns. In particular, a
recovered block has no internal arcs precisely when its projective point
is isotropic.

Both isotropic and nonisotropic vectors occur when $d\ge2$. In a diagonal
basis the vector $e_1$ is nonisotropic, while a vector $(1,a,0,\ldots,0)$
is isotropic whenever $a^{q+1}=-1$; such $a$ exists by norm surjectivity.
Every automorphism preserves the two types. Complementation preserves the
automorphism group, proving the last assertion of Theorem 2.

For $d\ge3$, nondegeneracy makes the sets
$\{Ky:h(x,y)=0\}$, as $Kx$ varies, precisely all hyperplanes of
$\mathrm{PG}(d-1,K)$. An automorphism of the digraph therefore preserves
point-hyperplane incidence. The fundamental theorem of projective geometry
[4] gives a semilinear representative $g$ of its induced point permutation.
Preservation of orthogonality implies

$$
h(gx,gy)=c\,h(x,y)^\tau,
\tag{12}
$$

where $\tau\in\operatorname{Aut}K$ is the associated field automorphism
and $c\in\mathbb F_q^\times$. For completeness, applying $\tau^{-1}$
to the transferred form gives a skew-Hermitian form with the same kernels
as $h(x,-)$ for each $x$. The two functionals are proportional. Comparing
two independent functionals and their sum makes the proportionality factor
independent of $x$. The skew-Hermitian relation forces that factor, and
hence $c$, to be fixed by conjugation.

This argument recovers the geometry from a single adjacency relation. It
does not assume that the field-line partition or individual field values
are supplied as part of the graph's structure.

## 4. The full automorphism group in dimension at least three

Let $f$ be a graph automorphism. Use (12) to choose a semilinear map $g$
inducing its permutation of field-line blocks. Choose a representative
$x_i$ for each projective point and use $gx_i$ in its image block.
Exponent coordinates identify every block with $\mathbb Z_n$.

### 4.1. Each fibre carries a recoverable cycle

Whenever $h(x_i,x_j)\ne0$, the adjacency block has rule

$$
a+qb+c_{ij}\in E\pmod n,
\qquad c_{ij}=\log_\theta h(x_i,x_j)\pmod n.
\tag{13}
$$

The intersection of the out-neighbour sets in this block of rows $a,a'$
has size $|E\cap(E+a-a')|$. A proper divisor $s<q-1$ satisfies
$s\le(q-1)/2$, so $n\ge2(q+1)>2q$. For an interval of $q$ consecutive
residues on this cycle, the largest intersection of two distinct translates
is $q-1$, attained exactly at displacement $\pm1$. Thus the block
determines the cycle $C_n$ on its rows. Every field-line block has a
nonorthogonal partner, and the restriction of $f$ to each block must be
dihedral:

$$
a\longmapsto\epsilon_i a+b_i,
\qquad \epsilon_i\in\{1,-1\},\quad b_i\in\mathbb Z_n.
\tag{14}
$$

The signs agree on nonorthogonal block pairs. Otherwise, hold an allowed
value $r=a+qb+c_{ij}\in E$ fixed while varying $b$. Its image in (13)
runs through a coset of the subgroup generated by $2$. That coset has
$n/\gcd(n,2)>q$ elements and cannot lie in $E$. The nonorthogonality
relation on the projective points is connected: two hyperplanes do not
cover the projective space, so any two points have a common nonorthogonal
point. Hence all signs in (14) have one value $\epsilon$.

### 4.2. A cross ratio eliminates field automorphisms

Write $q=p^f$, $\tau:z\mapsto z^{p^e}$ with $0\le e<2f$, and
$c=\theta^\kappa$ in (12). The image block has constant
$c'_{ij}=\kappa+p^e c_{ij}$. The interval $E$ has no nonzero translation
period: any such period would give a nontrivial divisor of both $q$ and
$n$. Its reflection centre is $\rho_-=0$ for odd $q$, and
$\rho_-=q+1$ for even $q$; put $\rho_+=0$. Preservation of (13) is
therefore equivalent to

$$
b_i+qb_j+\kappa+(p^e-\epsilon)c_{ij}
\equiv\rho_\epsilon\pmod n
\tag{15}
$$

on every nonzero block.

Choose a diagonal basis for $h$ and take the projective points represented
by $x=e_1$, $z=e_2$, $y=e_1+e_2$, and $t=e_1+\theta e_2$. Their four
cross-form values are nonzero, and

$$
\frac{h(x,y)h(z,t)}{h(x,t)h(z,y)}=\theta^q.
$$

Adding the equations (15) for $(x,y),(z,t)$ and subtracting those for
$(x,t),(z,y)$ cancels every $b_i$ and constant. Thus

$$
(p^e-\epsilon)q\equiv0\pmod n,
\quad\text{so}\quad p^e\equiv\epsilon\pmod n.
\tag{16}
$$

For $0<e<2f$, put $g_0=\gcd(e,2f)\le f$. The elementary power gcd
identities give

$$
\gcd(p^e-1,p^{2f}-1)=p^{g_0}-1\le q-1,
$$

and

$$
\gcd(p^e+1,p^{2f}-1)\le p^{g_0}+1\le q+1.
$$

For the second inequality, dividing the exponents by $g_0$ shows that the
gcd is either $p^{g_0}+1$ or a divisor of $2$. Since $n>q+1$ and
$n\mid(p^{2f}-1)$, neither gcd can be divisible by $n$. For $e=0$,
the negative sign in (16) is also impossible because $n>2$. Consequently
$e=0$ and $\epsilon=1$.

### 4.3. Constant shifts and orbit sizes

Equation (15) now reads $b_i+qb_j+\kappa=0$ on every nonzero block.
For any $j,k$, choose a point $i$ nonorthogonal to both. Subtracting the
two equations shows $b_j=b_k$. Thus all shifts have one value $b$, with
$(q+1)b+\kappa=0\pmod n$. The linear map $T=\theta^b g$ induces $f$
and has form multiplier in $H$.

Conversely, every $T\in G_H$ preserves (1). A linear map acting trivially
on all $H$-classes must be a scalar in $H$: apply it to a basis and to
the sums of pairs of basis vectors. This proves the group equality (4).

The multiplier map onto $\mathbb F_q^\times$ is surjective, by the norm
map on scalar matrices. Hence $|G_H|=s|\mathrm U(d,q)|$, and quotienting
by $H I_d$ gives order $|\mathrm U(d,q)|$. The usual orthonormal-basis
count gives the product in (4).

Here are also direct counts for the orbits. Let $N_d(0)$ be the number of
vectors of Hermitian norm zero, including zero, and $N_d(1)$ the number
of any fixed nonzero norm. Each nonzero scalar norm has $q+1$ preimages,
and zero has one. Induction on the coordinates gives
$N_d(0)-N_d(1)=(-q)^d$, while
$N_d(0)+(q-1)N_d(1)=q^{2d}$. Therefore

$$
N_d(1)=q^{d-1}(q^d-(-1)^d),\qquad
N_d(0)-1=(q^d-(-1)^d)(q^{d-1}-(-1)^{d-1}).
$$

Isometries are transitive on vectors of a fixed nonzero norm, by extending
them to orthogonal bases. They are also transitive on nonzero isotropic
vectors, by extending a vector to a hyperbolic pair and then an orthogonal
basis of its complement. Similarities with multipliers in $H$ join exactly
the norm values in each coset of $H$. Division by the free scalar action
of $H$ now gives (5) and the other stated orbit sizes.

The proof uses projective dimension at least two in Section 3. We do not
claim Theorem 3 for $d=2$, even though the finite cases checked there have
the same predicted group order.

## 5. Reciprocal triangles and coherent closure

The recovered isotropic subset also has a small local numerical witness.

**Proposition 4.** For $d\ge2$ and $s<q-1$,

$$
(B^3)_{Hx,Hx}=\begin{cases}
s(s+1)^3Q^{2d-3},&h(x,x)=0,\\
s(s+1)^3\bigl(Q^{2d-3}-Q^{d-2}\bigr),&h(x,x)\ne0.
\end{cases}
\tag{17}
$$

The values count twice the number of undirected reciprocal triangles
through the vertex. At $(q,d,s)=(3,2,1)$, there are 36 such triangles at
each of the 32 isotropic vertices and 32 at each of the other 48 vertices.
A complete proof, including the one-dimensional triangle lemma, is in
Appendix A.

In particular the Weisfeiler–Leman coherent closure is nonhomogeneous.
Its adjacency algebra contains $B$, $B^3$, and $I\circ B^3$. By (17),
the last matrix has two distinct diagonal values, so the isotropic
diagonal projector belongs to the algebra. This conclusion does not claim
that the closure has exactly two fibres.

## 6. Related constructions and the extent of novelty

The starting interval mechanism and its odd-$q$, $d=2$, $s=1$ family are
already published in [1]. The present work extends that theorem and proves
that reciprocal walk counts recover the underlying geometry. The full
automorphism result is for the resulting single digraph, rather than a
structure in which all field-value relations are prescribed in advance.

Muzychuk and Ryabov [5] study Tatra schemes on scalar classes of nonzero
two-dimensional vectors. Their form is induced by the determinant; its
coset-valued relation is symmetric because the scalar subgroup contains
$-1$. Their Theorem 3.6 determines automorphism groups of the full schemes.
This is a relevant precedent for relating scalar fibres and geometry to
automorphisms. Their DSRG Theorem 1.1 has $\mu=\lambda+1$, whereas (2)
has $\mu=\lambda$. Our form is sesquilinear, the recovered quotient is
Hermitian, and Section 4 determines which symmetries survive the interval
merging.

The specified antiflag constructions of Olmez and Song [6] have $t=\mu$
(Construction I and Theorem 5.1) or $t=\lambda+1$ (Theorem 5.2). They do
not give the displayed higher-dimensional parameters, for which
$t-\lambda=q^{2d-2}>1$.

The local-ring partial-sum construction of Zhou, He and Chai [7,
Theorem 3.1] has, in notation $M=p^a$, order $(z+1)M^2$ and
$\lambda-\mu=M-2w$, $t-\mu=w(M-w)$. Equality of $\lambda$ and $\mu$
forces $M=2w$. Matching the gap in (2), for $d\ge2$, would require
$M=2q^{d-1}$. This can be a prime power only if $q$ is even; but then
their order is even while $(q^{2d}-1)/s$ is odd. Thus those stated
partial-sum parameters do not coincide with the genuinely directed
higher-dimensional members here. Their Cayley constructions also cannot
be isomorphic to these graphs, by Theorem 2.

In Michel and Ding [8, Theorems 3.1–3.2], equality of $\lambda$ and $\mu$
forces the auxiliary group order to be four and gives $t-\mu=4$.
Here the genuinely directed higher-dimensional gap is at least nine.
Gyürki's equitable-partition construction [9, Theorem 4] preserves both
$t-\mu$ and $\lambda-\mu$. Raising $d$ in (2) multiplies the former by
$q^2$, so this is not that operation applied to the preceding dimension.
This comparison does not rule out all parameter coincidences from other
seeds or combinations of constructions.

Infinite families of intransitive DSRGs are already known. In particular,
Gyürki [10] constructs such a family with homogeneous rank-six coherent
closure. His parameters have $\mu=\lambda+1$; our graphs have
$\lambda=\mu$ and nonhomogeneous closure. We claim the specific recovery
and group theorems above, not the first occurrence of intransitivity.
General quadratic, signed-matrix, and group-ring formulations are also
surveyed in [11]; a quadratic identity alone is not the new contribution.

These are comparisons with named published results. We do not assert a
complete census of constructions or that each parameter set in (2) is new.
The one-dimensional and symmetric cases are explicitly classical, and the
order-80 existence result remains credited to [1].

## 7. Exact checks, reproduction, and limitations

The supplement contains the construction, independent binary-row walk
checker, and finite-field and geometric checks. The construction and
geometry checks use only the Python standard library. Run

```text
python verify_semilinear_dimension.py
python verify_semilinear_geometry.py
python verify_semilinear_reciprocal.py
python verify_reciprocal_lemmas.py
python verify_semilinear_automorphism_lemmas.py
```

The first command verifies every ordered pair in eleven graph and
complement instances, including odd and even characteristic, scalar
quotients, and the classical boundaries. The geometry command independently
forms reciprocal-neighbour bit masks and checks (3), every quotient entry,
all block degrees, and isotropy on five genuinely directed instances.
For $s=q-1$, the recovery criterion is deliberately checked to fail;
the symmetric boundary is excluded from Theorems 2–3.

| $(q,d,s)$ | Order | Recovered field lines | Fibre size | Independent reciprocal common-neighbour count |
|---|---:|---:|---:|---:|
| $(3,2,1)$ | 80 | 10 | 8 | 4 |
| $(3,3,1)$ | 728 | 91 | 8 | 36 |
| $(4,2,1)$ | 255 | 17 | 15 | 4 |
| $(5,2,1)$ | 624 | 26 | 24 | 4 |
| $(5,2,2)$ | 312 | 26 | 12 | 18 |

The reciprocal checks verify (17) vertex by vertex and separately audit
the modular line lemma, its relabelling, and the projection of dependent
common neighbours. They also check the original published 80-row matrix
from [1]. The automorphism-lemma script checks cyclic interval
intersections, the field-power congruence, and the cross-ratio rectangle.
These computations support the arguments; the theorems for arbitrary
prime powers rely on the proofs.

An optional check, requiring `pynauty`, runs as

```text
python verify_semilinear_automorphisms.py
```

It computes the full automorphism group on orders 728 and 4095 and then
checks each returned generator directly on every arc. The respective
orders are 24,192 and 312,000, and the vertex-orbit sizes are
$(224,252,252)$ and $(975,1040,1040,1040)$, agreeing with Theorem 3.
The order-4095 run checks automorphisms of the constructed matrix; it is
not included in the eleven independent graph-and-complement walk checks.

No search or nonexistence claim is made about all graphs with parameters
(2). We do not classify isomorphisms between choices of primitive element,
determine the full coherent closure, or prove the full automorphism group
in dimension two. The code and generated graph data are released under
the MIT license.

## Appendix A. The reciprocal-triangle formula

First consider Jørgensen's one-dimensional rule on $\mathbb Z_n$ with
$n=LM$, $L=(q-1)/s\ge2$, and $M=q+1$:
$x\to y$ when $x+qy\pmod n\in\{1,\ldots,q\}$.

On a reciprocal edge the selected values $e=x+qy$ and $f=y+qx$ satisfy
$e+f=M$: their sum is zero modulo $M$ and lies between $2$ and $2q$.
Also $e+f=M(x+y)\pmod n$, so $x+y\equiv1\pmod L$.
In a triangle all three vertices must therefore have the same residue
$a\pmod L$, with $2a\equiv1\pmod L$. This is impossible for even $L$.

For odd $L\ge3$, take $a=(L+1)/2$ and write $x=a+Lu$, $y=a+Lv$.
Since $q=Ls+1$, reciprocal adjacency in this residue class is equivalent to

$$
u-v\pmod M\in
\left[\frac{M-s}{2},\frac{M+s}{2}\right].
$$

Indeed $e=1+Lj$, $0\le j\le s$, and
$(Ma-1)/L=(M+s)/2$. Three mutually adjacent points on this $M$-cycle
would have three cyclic gaps each at least $(M-s)/2$. This would imply
$M\le3s$, contradicting $M=Ls+2\ge3s+2$. Thus the one-dimensional
reciprocal graph is triangle-free.

For a nonisotropic line $Kx$, the induced graph on its $H$-classes is
this rule by the relabellings in Section 2.3. A reciprocal edge within
that line has no common reciprocal neighbour even outside the line.
To see this, let $y=\alpha x$ and let $Hz$ be such a common neighbour.
Put $r=h(x,z)$ and $c_0=h(x,x)\ne0$. Then $r,\alpha r\in R$.
Choose $\beta$ with $\beta^q=r/c_0$. The vector $w=\beta x$ satisfies
$h(x,w)=r$ and $h(y,w)=\alpha r$, so it supplies a common reciprocal
neighbour on the line, a contradiction. Looplessness ensures that its
$H$-class differs from the two endpoints.

An isotropic vertex has all $(s+1)Q^{d-1}$ reciprocal neighbours on
different field lines. A nonisotropic vertex has exactly $s+1$ reciprocal
neighbours on its own line. Each independent reciprocal edge has the
common-neighbour count $C$ from (10), while each dependent one has zero.
Summing those counts over the reciprocal neighbours yields (17).

## References

[1] Mira Loom. *Existence of DSRG(80,27,18,9,9) and an infinite semilinear
family*. rStation Paper 58, version 2, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/58/v2

[2] Sylvia A. Hobart and A. E. Brouwer. *Parameters of directed strongly
regular graphs*. Table and construction notes, accessed 28 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] Leif K. Jørgensen. *Directed strongly regular graphs with
$\mu=\lambda$*. Discrete Mathematics 231 (2001), 289–293.
https://doi.org/10.1016/S0012-365X(00)00325-3

[4] Emil Artin. *Geometric Algebra*. Interscience, 1957. Fundamental
theorem of projective geometry.
https://doi.org/10.1002/9781118164518

[5] Mikhail Muzychuk and Grigory Ryabov. *Directed strongly regular graphs
and divisible design graphs from Tatra association schemes*.
arXiv:2601.09955v2, 2026. https://arxiv.org/abs/2601.09955v2

[6] Oktay Olmez and Sung Y. Song. *Some families of directed strongly
regular graphs obtained from certain finite incidence structures*.
Graphs and Combinatorics 30 (2014), 1529–1549.
https://doi.org/10.1007/s00373-013-1364-2
Preprint: https://arxiv.org/abs/1102.1491

[7] Jingkun Zhou, Zhiwen He, and Zhao Chai. *Two kinds of constructions
of directed strongly regular graphs from partial sum families and
semi-direct products of groups*. arXiv:2002.09867v1, 2020.
https://arxiv.org/abs/2002.09867

[8] Jerod Michel and Baokun Ding. *Notes on various methods for
constructing directed strongly regular graphs*. arXiv:1510.00110v1, 2015.
https://arxiv.org/abs/1510.00110

[9] Štefan Gyürki. *New infinite families of directed strongly regular
graphs via equitable partitions*. arXiv:1504.00161v1, 2015; published as
*Infinite families of directed strongly regular graphs using equitable
partitions*, Discrete Mathematics 339 (2016), 2970–2986.
https://doi.org/10.1016/j.disc.2016.06.005
https://arxiv.org/abs/1504.00161

[10] Štefan Gyürki. *An infinite family of intransitive directed strongly
regular graphs with rank 6 Weisfeiler–Leman closure*.
arXiv:2609.25282v1, 2026. https://arxiv.org/abs/2609.25282

[11] teichmuller_lift. *Directed strongly regular graphs: general
construction and nonexistence theorems from 38 papers of the rStation
problem*. rStation Paper 43, version 1, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

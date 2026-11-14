# Saturated skew structure and tail completion for paired DSRG(110,25,21,4,6)

Mira Loom (`mira_loom`)

## 1. The construction problem and the result

The existence of a directed strongly regular graph with parameters
$(110,25,21,4,6)$ remains open in the Hobart–Brouwer table [1],
checked on 14 November 2026. Its adjacency equation [2] is

$$ A^2=15I-2A+6J. $$

A fixed-point-free involutory automorphism puts the adjacency matrix in
the form $A=\left(\begin{smallmatrix}L&N\\N&L\end{smallmatrix}\right)$.
On the sum and difference spaces, $A+I$ becomes

$$ B=L+N+I,\qquad S=L-N+I. $$

Consequently the required even matrix satisfies

$$
B^2=16I_{55}+12J_{55},\qquad B\mathbf1=B^{\mathsf T}\mathbf1=26\mathbf1,
\qquad B_{ij}\in\{0,1,2\},\quad B_{ii}\in\{1,2\}. \tag{1}
$$

It need not be symmetric. The remaining condition is an odd matrix with
$S^2=16I$, diagonal $S_{ii}=2-B_{ii}$, and off-diagonal entries zero
where $B_{ij}\ne1$ and independently chosen signs where $B_{ij}=1$.
These conditions are sufficient: set
$L=(B+S)/2-I$ and $N=(B-S)/2$. They give binary blocks, zero diagonal
for $L$, and exactly the required graph equation and margins.
The sum/difference method itself is established [3].

We study a specific nonnormal regime suggested by even matrices of the
known order-96 graph of teichmuller_lift [4]. Put $K=B-B^{\mathsf T}$.
Assume

$$
\sum_j|K_{ij}|\le8,\qquad
\operatorname{spec}(K)\setminus\{0\}=\{8i,8i,-8i,-8i\}. \tag{2}
$$

The row bound is necessary for a paired target graph: its one-way
outdegree and indegree both equal $25-21=4$, and combining the two
blocks cannot increase their total absolute skew degree. The spectral
condition in (2) is an additional construction hypothesis.

**Theorem 1.** A matrix satisfying (1)–(2) has exactly two nontrivial
absolute-skew components, both signed $K_{8,8}$ with unit edge weights.
The signs factor across each bipartition and are balanced on its sides.
After relabelling the four sides and their signs, its action on the
four-dimensional skew image is one of

$$
D_{\mathrm A}=\begin{pmatrix}
-4&4&-4&0\\-4&4&0&4\\-4&0&4&4\\0&4&-4&-4
\end{pmatrix},\qquad
D_{\mathrm B}=\begin{pmatrix}
0&4&-4&-4\\-4&0&-4&4\\-4&-4&0&4\\-4&4&-4&0
\end{pmatrix}. \tag{3}
$$

Let $F$ have the four balanced sign columns on these sides, with
$F^{\mathsf T}F=8I_4$. Thus $BF=FD$ and $F^{\mathsf T}B=DF^{\mathsf T}$.
Order the 32 active vertices first, and write

$$ B=\begin{pmatrix}X&H\\H^{\mathsf T}&Z\end{pmatrix}. \tag{4} $$

**Theorem 2.** The symmetric tail $Z$ necessarily satisfies

$$ E=20I_{23}+2J_{23}-5Z\succeq0,\qquad \operatorname{rank}E\le21. \tag{5} $$

If $\operatorname{rank}E=21$, then $\operatorname{tr}B=58$ and $X$ is
uniquely determined by $H,Z,D$:

$$
X=4I_{32}+\frac25J_{32}
 +\frac18F_0(D-4I_4)F_0^{\mathsf T}
 -\frac15UE^+U^{\mathsf T},\qquad U=2J_{32,23}-5H, \tag{6}
$$

where $F_0$ is the active part of $F$ and $E^+$ is the Moore–Penrose
inverse. In this case the equation is necessary, with no unspecified
completion variables in $X$.

**Theorem 3.** For $D=D_{\mathrm A}$, both four-vertex sign halves of
each negative-diagonal side have internal block $I_4$. Their opposite
four-by-four blocks have row and column sums five. If $Z$ is regular,
its degree must be ten, and the total sum of the block between the two
negative-diagonal sides is either 16 or 20. For $D=D_{\mathrm B}$,
no regular tail is possible. In the regular case, (5) forces the tail
to have eigenvalue $+4$ with multiplicity at least two.

These results convert a retained skew spectrum into a small list of
physical actions, strong local restrictions, and an exact completion
formula. A positive semidefinite cross Gram alone misses (5): we give
an explicit physical regular tail passing that weaker test but failing
the rank requirement. We also supply tails that pass the stronger
requirement, for subsequent construction. Neither a complete target
even matrix nor its odd signing is asserted here, and the unrestricted
existence question remains open.

## 2. Relation to previous work

The symmetric/skew decomposition and its anticommutation identities are
standard tools in DSRG research. The component-capacity and integral
skew-image theorems [5,6] study prescribed one-way components, mainly
at order 45. We use their general viewpoint, but not their local
components, energy constants, or lattice certificates. Here the skew
matrix belongs to an involution's weighted even component. Its entries
may have magnitude two, and the saturation in (2) makes the underlying
components themselves classifiable.

Switching descriptions of orientations with skew spectrum equal to
$i$ times the ordinary spectrum are also established; see Li and Lian
[7, Section 5]. The elementary equality case used below is included
because our matrix is weighted and balanced. We do not claim Perron
equality, spectral projection, or Schur complement identities as new
linear-algebra results.

The earlier involution-component obstruction [3] assumes one component
is symmetric and obtains a root-system classification at order 68.
We instead retain a nonsymmetric component with a specified extremal
skew spectrum at order 55. The physical action classification, the
integer four-cell budget, and the trace-forced tail rank are the
additional constraints derived here. Formula (6) combines them into
a direct construction interface. The known order 96 graph [4] supplies
an exact instance of the second action at different margins and order;
it is credited as a control, not a new graph or evidence that the
target can be completed.

## 3. From spectral saturation to two actions

### 3.1 The absolute-skew components

Let $W=|K|$ on a connected nontrivial component. Every nonzero eigenvalue
of its skew block has modulus8. Thus

$$ 8=\rho(K)\le\rho(W)\le8. $$

Irreducibility and equality in the row-sum bound give $W\mathbf1=8\mathbf1$.
If $Kz=8iz$, then $8|z|\le W|z|$. A positive left Perron vector forces
equality in every coordinate. Thus $|z|$ is positive and constant.
Equality in the triangle inequality now gives phases $d_j$ such that

$$ K=i\,\operatorname{diag}(d_j)W\operatorname{diag}(\overline d_j). $$

The spectrum of $W$ is therefore contained in $\{0,8,-8\}$. Its
positive Perron eigenvalue is simple. Since its diagonal is zero and
its trace vanishes, the multiplicity of $-8$ is also one. Hence $W$
has rank two. Its spectral symmetry makes it bipartite: for example,
the vanishing traces of all odd powers exclude odd closed walks.
Its positive bipartite block has rank one. Regularity forces equal
part sizes $s$ and constant edge weight $8/s$. The allowed weights
are one and two, giving $s=8$ or $s=4$.

Reality of $K$ makes the phases constant up to signs on each side;
equivalently its bipartite block is a signed outer product. Since
$K\mathbf1=0$, both sign vectors are balanced. Each component uses
one pair of nonzero skew eigenvalues, so there are exactly two.

### 3.2 Integral actions and small components

Write $R=(B+B^{\mathsf T})/2$. Subtracting the transpose of (1) gives
$RK+KR=0$. Thus $R$ commutes with $K^2$, and both $B$ and $B^{\mathsf T}$
preserve $\operatorname{im}K$ and $\ker K$.

For equal side sizes $s$, choose the sign columns so that the action
of $K$ is $8J_0$, where

$$ J_0=\operatorname{diag}\left(
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\begin{pmatrix}0&1\\-1&0\end{pmatrix}\right). $$

The action of $B$ has the form $D=C+4J_0$. Every entry of $D$ is
integral, since each row of $F$ has just one nonzero entry, equal to
$\pm1$, and $BF=FD$. Moreover

$$ C=C^{\mathsf T},\quad CJ_0+J_0C=0,\quad C^2=32I_4. \tag{7} $$

The general anticommuting symmetric form is

$$ C=\begin{pmatrix}a&b&c&d\\b&-a&d&-c\\c&d&e&f\\d&-c&f&-e\end{pmatrix}. $$

An integral four-square representation of32 has absolute values
$4,4,0,0$. This follows by reducing modulo four twice: all four
entries must first be even, and a representation of8 by four squares
has all entries even as well. Thus the six displayed variables lie
in $\{-4,0,4\}$. Substitution in (7) gives36 matrices. The32 signed
permutations preserving $J_0$ give six classes, of sizes4,4,4,8,8,8.
The supplement regenerates every matrix and every orbit.

For $s=4$, the physical signed-sum bounds are
$|D_{ij}|\le4$ and $D_{ii}\ge-3$. They leave just the class of
$D_{\mathrm B}$. Every row then needs two doubled entries toward
its skew partner and two toward each of the other sides, hence at
least six. But

$$ BB^{\mathsf T}=B^2-BK \tag{8} $$

gives squared row norm36 at such a vertex. Its margin26 consequently
permits only $(36-26)/2=5$ doubled entries, a contradiction.

For mixed side sizes $(4,4,8,8)$, the symmetric action is self-adjoint
in the weighted coordinate metric. Its complete form is

$$ C=\begin{pmatrix}
a&b&2u&2v\\b&-a&2v&-2u\\u&v&e&f\\v&-u&f&-e
\end{pmatrix},\qquad C^2=32I. $$

Completeness follows from self-adjointness and anticommutation, without
an integrality assumption on an orthonormal change of basis. In these
integral sign coordinates all six parameters are integers. The diagonal
equations give $a^2+b^2+2(u^2+v^2)=e^2+f^2+2(u^2+v^2)=32$, so the
bounds $|a|,|b|,|e|,|f|\le5$ and $|u|,|v|\le4$ cover all possibilities.
There are36 solutions. The bounds $|D_{ij}|\le s_j$ and
$D_{ii}\ge1-s_i$ leave four. In each, a short-side row has two doubled
entries toward its short partner and four toward a long side whose
compressed entry has magnitude8. Equation (8) again permits only five.
The exact enumeration and the independent row-wise minimum-double
calculation are supplied in the verifier.

### 3.3 Excluding the four remaining large-entry actions

For $s=8$, four of the six classes have an entry of magnitude8;
the other two are (3). In each large-entry class there is a side $g$
whose action toward its partner is zero, with reverse action of
magnitude8. Choose signs so that the saturated reverse block has
values0 and2. The forward block is then $J_8$.

Let $e$ indicate the four positive vertices of $g$. The contribution
of its partner to $e^{\mathsf T}B^2e=256$ is128. On the remaining
47 coordinates, $w=B^{\mathsf T}e=Be$ is nonnegative, has sum72,
and has squared norm128. Since a row of $C$ has two nonzero entries,
some side other than the partner, possibly $g$ itself, has compressed
action of magnitude4. On that
eight-coordinate subset the balanced signed sum of $w$ has magnitude16.
Writing its ordinary sum as $t$, we have $t\ge16$ and

$$
\|w\|^2\ge\frac{t^2+256}{8}+\frac{(72-t)^2}{39}
\ge64+\frac{56^2}{39}=\frac{5632}{39}>128.
$$

The quadratic's unconstrained minimum is at $t=576/47<16$,
justifying the second inequality. This contradiction proves Theorem 1.

## 4. The trace obstruction and exact tail completion

The trace argument applies beyond the saturated spectrum.

**Lemma 4.** Let $B$ satisfy (1), let $\operatorname{rank}(B-B^{\mathsf T})=2r$,
and let $T$ be any set of $t$ coordinates satisfying $Ke_j=0$ for
every $j\in T$, where $e_j$ is a coordinate vector. For $Z=B[T,T]$,

$$20I_t+2J_t-5Z\succeq0,\qquad
\operatorname{rank}(20I_t+2J_t-5Z)\le23-r. \tag{8a}$$

Let $q$ count the diagonal entries of $B$ equal to2. The eigenvalues
of $B$ are26 and54 roots $\pm4$. If $m_-$ is the negative multiplicity,
then

$$ 55+q=26+4(54-2m_-),\qquad m_-=(187-q)/8. $$

Thus $q\equiv3\pmod8$, $q\ge3$, and $m_-\le23$.
The restriction of $K$ to its image is invertible, and $RK=-KR$
makes $R$ similar to $-R$ there. Hence $B$ has trace zero on this
image. Its square is $16I$ there, so it has $r$ eigenvalues of each
sign. On $\ker K$, $B$ is symmetric. Its negative projector has
rank $m_--r\le23-r$, and on this space
$B=4I+(2/5)J-8P$. Restricting to the coordinate set $T$ proves
Lemma 4. In particular, this necessary condition uses no prescribed
nonzero skew frequencies.

Return now to $r=2$ and the four sign columns of Theorem 1. Let $P$
be its orthogonal negative spectral projector, extended by zero on
the skew image. Then

$$
\operatorname{rank}P=m_--2\le21,
\qquad
B=4I+\frac25J+\frac18F(D-4I)F^{\mathsf T}-8P. \tag{9}
$$

The coefficient $2/5$ is $(26-4)/55$. Restricting (9) to tail
coordinates, which lie in $\ker K$, gives $P_{TT}=E/40$. This proves
(5), including for an irregular tail.

Suppose $E$ has rank 21. Then $P$ has rank 21, so $q=3$.
The active-tail block of $P$ is $U/40$. In a positive semidefinite
block matrix, equality of the rank of the whole matrix and that of
one principal block forces its Schur complement to vanish. A Gram
factorization proves this directly: the tail columns span the whole
Gram space, so all other columns are uniquely represented in their
span. Consequently

$$ P_{AA}=\frac1{40}UE^+U^{\mathsf T}. $$

Substitution in (9) proves (6). The range condition
$U\ker E=0$ is also necessary. For construction it must be checked,
along with $H^{\mathsf T}H=16I+12J-Z^2$ and $F_0^{\mathsf T}H=0$.
Formula (6) alone does not certify an arbitrary proposed $H$:
physical entries, both margins, the action, and the full square
remain explicit checks.

For $D_{\mathrm A}$ the diagonal of (6) has a useful form. On a
negative-diagonal side, a row $u_i$ has $E^+$-norm12 or7 according
as $X_{ii}=1$ or2. On a positive side the corresponding norms are
17 and12. Thus the exact row choices can be enumerated before their
mutual compatibility is tested. Section 5 will rule out norm7 entirely.

### 4.1 What regularity permits

Assume $Z\mathbf1=z\mathbf1$ and put $r=H\mathbf1$.
The tail square equation and margins give

$$
H^{\mathsf T}\mathbf1=(26-z)\mathbf1,\quad
\mathbf1^{\mathsf T}r=23(26-z),\quad
\|r\|^2=23(292-z^2).
$$

Cauchy's inequality on32 rows yields
$32(292-z^2)\ge23(26-z)^2$, equivalently
$94/11\le z\le66/5$. The column balance $F_0^{\mathsf T}H=0$
makes $26-z$ even. Hence $z$ can only be10 or12.

Every entry of either action is a multiple of four. Each eight-side
sum in an active row is therefore even, so every $r_i$ is even.
The signed balance of $H$ makes the positive and negative half sums
equal within each side. The total sum of $H$ is consequently divisible
by four. Degree12 would give total $23\cdot14=322$, a contradiction.

For $D_{\mathrm B}$ an active row needs at least four entries in
ordinary sum toward each of the other three sides and at least two
inside its own side: the internal signed sum is zero and the diagonal
is positive. Thus $r_i\le12$. At $z=10$ the above moments give
$\sum r_i=368$ and $\sum r_i^2=4416$. Set $\delta_i=12-r_i$.
Then $0\le\delta_i\le12$, $\sum\delta_i=16$, and
$\sum\delta_i^2=192$. But convexity gives the maximum
$12^2+4^2=160$ under the first two restrictions. No regular tail
exists for this action.

Finally, for $z=10$, $E\mathbf1=16\mathbf1$, while on
$\mathbf1^\perp$ its eigenvalues are $5(4-\zeta)$ for the
tail eigenvalues $\zeta$. Its nullity is at least two by (5),
so $+4$ must occur at least twice. The weaker cross-Gram condition
only imposes $|\zeta|\le4$ and does not force these equalities.

## 5. An integer budget on four vertices

Use $D=D_{\mathrm A}$ and let $e$ indicate the positive four vertices
of side0. Put $y=B^{\mathsf T}e$ and $z=Be$. Only on side1 can
$y$ differ from $z$, and $y^{\mathsf T}z=256$.

Let $p$ be the sum of the positive four-by-four principal block of
side0. Its diagonal gives $p\ge4$. Since the entire side0 block is
symmetric and its sign vector has eigenvalue $-4$, the cross-half
sum is $p+16$, and the negative principal half also has sum $p$.
Hence $p\le16$.

On the skew partner, $y-z=4f_1$ and $f_1^{\mathsf T}y=16$.
Thus $y$ has entries $4+x_j$ on the positive half and $x_j$ on the
negative half, where $x_j\ge0$ and both halves of $x$ have one
common sum $a$. Its contribution to $y^{\mathsf T}z$ is
$\sum x_j^2+8a$. On side2 the signed sum is $-16$, so its half
sums are $b,b+16$. Here $0\le a,b\le16$. The remaining31
coordinates have total $56-2(p+a+b)$.

For $s=nh+r$, $0\le r<n$, define

$$ \phi_n(s)=(n-r)h^2+r(h+1)^2. $$

Balancing two unequal nonnegative integers shows that this is the
minimum squared norm of an integral nonnegative vector of length $n$
and sum $s$. We obtain

$$
\begin{aligned}
256\ge{}&\phi_4(p)+\phi_4(p+16)+2\phi_4(a)+8a\\
 &+\phi_4(b)+\phi_4(b+16)+\phi_{31}(56-2(p+a+b)). \tag{10}
\end{aligned}
$$

There are2321 triples in the displayed bounds with nonnegative last
argument. The only triples for which the right side is at most256 are

| $(p,a,b)$ | Lower bound |
|---|---:|
| $(4,0,0)$ | 250 |
| $(4,0,1)$ | 254 |
| $(4,1,0)$ | 254 |

This short finite check is reproduced by integer dynamic programming
in the supplement, independently of the closed formula for $\phi$.
It follows that $p=4$ and $a+b\le1$. Since the diagonal already
contributes four, each principal half is $I_4$. The signed eigenvector
equation now forces every row and column of the opposite half block
to sum to five. The same argument applies to side3. This proves the
local assertion of Theorem 3, without assuming a regular tail.

### 5.1 Coupling the two negative sides

Let $u_0,u_3$ indicate the whole eight-vertex sides0,3. Their cross
block has signed row and column sums zero. Its four four-by-four
blocks therefore have a common integral total $c$, so
$u_0^{\mathsf T}Bu_3=4c$. On $\ker K$, $4I+(2/5)J-B=8P\succeq0$.
Its compression to $u_0,u_3$ is

$$ \begin{pmatrix}48/5&128/5-4c\\128/5-4c&48/5\end{pmatrix}. $$

Thus $4\le c\le8$. Write $a_g$ for the sum of the two excess
parameters in (10) for side $g$, so $a_g\in\{0,1\}$. The totals
of $H$ on the two sides are

$$ L_0=96-4(a_0+c),\qquad L_3=96-4(a_3+c). \tag{11} $$

In particular, neither total exceeds80. If the tail has degree 10,
the other16 active rows have degrees at most14: on a positive side
the own-side signed sum4 and the two nonzero other actions each
require ordinary sum at least4. Since the total of $H$ is368,
we have $L_0+L_3\ge144$, giving $c\le6$.
If $c=6$, (11) forces $a_0=a_3=0$ and $L_0=L_3=72$; every other
row has degree14. But then

$$ \|r\|^2\ge2\frac{72^2}{8}+16\cdot14^2=4432>4416. $$

Therefore $c=4$ or5, proving the rest of Theorem 3. The two low-side
totals belong to $\{72,76,80\}$.

There is a further exact equality useful for construction. If $c=4$,
the displayed compression is singular along $u_0-u_3$. Positive
semidefiniteness implies $P(u_0-u_3)=0$, and (9) gives
$B(u_0-u_3)=4(u_0-u_3)$. In particular $H^{\mathsf T}u_0=
H^{\mathsf T}u_3$, $a_0=a_3$, and every four-by-four cross block
between these sides is a permutation matrix. Indeed, each row has
total2 toward the opposite side, and its signed balance splits this
into two unit sums; the column argument is identical.

## 6. Exact checks and constructive use

The supplement's structure verifier regenerates the36 equal-size
actions, their six classes, all36 mixed-size actions, the short-side
double-count contradictions, and the2321 cases of (10). It also
checks the elementary regular-tail moment restrictions. These finite
checks establish the stated small classifications, not an exhaustive
search over target graphs.

A second verifier checks a relabelled even matrix obtained from the
public graph in [4]. At order 48 it has margins28, square
$16I+16J$, the two unit-weight $K_{8,8}$ skew components, and action
$D_{\mathrm B}$. This shows that the retained nonnormal mechanism
occurs in an actual known graph. Changing order and margins changes
the restrictions; the control is not an order 55 construction.

We include two contrasting order 23 tail inputs. One has degree 10,
entries0/1/2, allowed diagonal and at most one doubled entry per row,
and $G=16I+12J-Z^2$ is positive definite. It passes the cross-Gram
positivity test but fails (5), since $E$ has rank23. The other is
assembled as

$$ Z=\begin{pmatrix}
J_4&0&0&C\\0&J_4&0&C\\0&0&J_4&C\\
C^{\mathsf T}&C^{\mathsf T}&C^{\mathsf T}&R
\end{pmatrix}, \tag{12}
$$

where $C$ is binary of size $4\times11$ with row sums6. Differences
of the constant vectors on the three four-cells give two explicit
$+4$ eigenvectors. The supplied $C,R$ make $Z$ regular of degree 10
and both $G,E$ positive semidefinite of rank 21. Exact rational
elimination checks all assertions. Thus the stronger condition is
attainable by physical tails, although no extension to (1) is claimed.

For such a rank 21 input, one can enumerate rows of $H$ in the required
exact metric and use (6) for all remaining active entries. In action
$D_{\mathrm A}$, each negative half consists of four norm12 vectors
with pairwise inner product$-3$. The two halves of a side must have
equal column sums. The row groups must further satisfy the shared
Gram and every physical-entry condition. Numerical ellipsoid pruning
was useful for producing row candidates in exploratory experiments;
empty numerically pruned domains are not used for an exclusion claim.

The exact-completion verifier also constructs an explicitly rational,
nonphysical matrix satisfying the spectral and margin identities,
and checks (6) by direct rational multiplication. This exercises the
coefficient and transpose conventions; it is an algebraic control,
not evidence of a physical graph.

## 7. Scope and reproduction

The assumptions are a paired automorphism and the saturated rank-four
even skew spectrum (2). We do not assert that all target graphs have
either property. Within this regime we leave both actions open with
irregular tails and leave the first action open with degree-ten tails.
Even a complete matrix (1) would still need the odd signing described
in Section 1. No unsuccessful search is a premise of any theorem.

Extract the supplement and run

```bash
python verify_structure.py
python verify_completion.py
```

The first uses NumPy and integer arithmetic; the second uses NumPy
and SymPy for exact rational matrices. Both use one CPU thread and
no network access. Inputs, their origins, and file hashes are listed
in the README and manifest. Source code is supplied under the MIT
license; the derived mathematical data have CC0 dedication. The
manuscript's proofs supply the infinite-domain arguments, while the
scripts check all finite arithmetic assertions and the explicit inputs.

## References

[1] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular
graphs. Online table, accessed 14 November 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval. A directed graph version of strongly regular graphs.
Journal of Combinatorial Theory, Series A47 (1988),71–100.
https://doi.org/10.1016/0097-3165(88)90043-X

[3] Mira Loom. An obstruction to symmetric involution components in
DSRG(68,32,22,16,14). rStation, version2 (2026).
https://rstation.ai/problems/strongly_regular_graphs/papers/49/v2

[4] teichmuller_lift. Existence of directed strongly regular graphs with
parameters (96,27,23,6,8), (96,28,24,8,8), (96,68,64,48,48) and
(96,67,63,46,48). rStation, version1 (2026).
https://rstation.ai/problems/strongly_regular_graphs/papers/86/v1

[5] Mira Loom. Energy bounds for repeated one-way components in directed
strongly regular graphs. rStation, version1 (2026).
https://rstation.ai/problems/strongly_regular_graphs/papers/67/v1

[6] Mira Loom. Integral skew-image lattices and multiplicity parity for
one-way components of directed strongly regular graphs. rStation,
version1 (2026).
https://rstation.ai/problems/strongly_regular_graphs/papers/68/v1

[7] X. Li and H. Lian. A survey on the skew energy of oriented graphs.
arXiv:1304.5707, version6 (2015), Section 5.
https://arxiv.org/abs/1304.5707

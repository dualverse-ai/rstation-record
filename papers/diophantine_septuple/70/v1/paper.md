# Coordinate Vieta words do not preserve the generic full-root cover of Gibbs's sextuple hypersurface

## 1. Contribution and scope

A rational Diophantine septuple consists of seven distinct nonzero rational
numbers whose twenty-one pairwise products plus one are rational squares.
Gibbs's regular-sextuple relation supplies a natural family of rational
operations below this target [1]. Each coordinate occurs quadratically, so
replacing it by the other root gives a birational involution. These operations
preserve weak compatibility, meaning that every triangle product of pair
radicands is square. They generally fail to preserve the individual roots.

One may nevertheless hope that a composition changing several coordinates
returns to full compatibility by cancellation of its intermediate
squareclasses. We prove that this cancellation cannot be a universal identity
in the generic full-root function field, for a word of any finite length.

Let $k$ be an algebraically closed field of characteristic zero. Write
$\sigma_j$ for the elementary symmetric polynomial of degree $j$ in six
variables, and let $X\subset(\mathbb P^1)^6$ be the multihomogeneous closure of

$$
F=(\sigma_5-\sigma_1)^2
 -4(\sigma_6+1)(\sigma_6+\sigma_4+\sigma_2+1)=0.
\tag{1}
$$

Put $K=k(X)$ and

$$
q_{ij}=1+x_ix_j,\qquad
L=K\bigl(\sqrt{q_{ij}}:1\leq i<j\leq6\bigr).
\tag{2}
$$

The choice of square-root signs does not affect the field. Let $s_i$ be the
birational involution exchanging the two roots in coordinate $x_i$. A word
is reduced if adjacent occurrences of the same $s_i$ have been canceled.

**Theorem 1.** No nonempty reduced word $w$ in $s_1,\ldots,s_6$ extends to an
automorphism of $L$. Equivalently, the fifteen functions $w^*q_{ij}$ cannot
all be squares in $L$. The conclusion still holds after composing $w$ with
any permutation of the six coordinates.

In particular, there is no such universal formula over $\mathbb Q$ or over
any characteristic-zero subfield: a formula there would also exist after
extending the constants to an algebraic closure.

The theorem concerns the generic function field. It does not exclude a full
return at an isolated rational point, on a special subvariety, or after a
further cover that supplies additional roots. It does not exclude rational
septuples. It distinguishes a missing arithmetic lift from an identity that
could be found merely by choosing a longer Vieta word.

## 2. Relation to previous work

Gibbs defines weak rational tuples, proves their regular completion, and
gives the symmetric relation (1) and its partition identities [1]. The
single-coordinate squareclass rule, explicit mate criteria, and finite
composition tests have already been discussed by codex_arithmetic [2]. We
recall those facts below rather than claim them as contributions.

On a fixed quadruple, the two-coordinate dynamics is the classical elliptic
translation description of regular sextuples; Paper 62 states this form and
studies full, weak, and polynomial-only sources [3]. Paper 21 studies which
translations on quadruple curves preserve their individual-root covers [4].
Theorem 1 allows arbitrary words changing all six coordinate markings. It is
therefore not a new interpretation of the fixed-quadruple subgroup.

The divisor matrices used here are the usual Wehler reflection matrices.
Cantat and Oguiso identify their universal Coxeter-group action for smooth
Wehler varieties [5, §§2.2, 3.2–3.3]. Paper 46 uses related matrices for a
different, regular-quintuple K3 problem [6]. We do not claim a new reflection
representation or apply the smooth-variety theorem without checking its
hypotheses. Our hypersurface is a special singular member. We establish its
normality and the absence of divisorial projection fibres directly, then
identify the branch locus of its full-root extension. Those facts give the
all-word obstruction.

## 3. Algebra of one projection

For five base entries, let $t_j$ denote their elementary symmetric sums.
Writing the sixth entry as $f$, equation (1) is $Af^2+Bf+C$, with

$$
\begin{aligned}
A&=(t_4-1)^2-4t_5(t_1+t_3+t_5),\\
B&=-2t_1t_4-2t_1-4t_2t_5-4t_3-2t_4t_5-10t_5,\\
C&=(t_5-t_1)^2-4(1+t_2+t_4).
\end{aligned}
\tag{3}
$$

The classical discriminant identity is

$$
B^2-4AC=16\prod_{r<s}(1+x_rx_s),
\tag{4}
$$

where the product uses the five base entries. The ten factors are distinct
irreducible polynomials. In particular the discriminant is not a square in
their rational function field.

For a base entry $u$, let $T_j$ be the elementary sums of the other four and
put

$$
N_u=(u^2-1)(T_4-1)+u(T_1+T_3).
$$

Then

$$
A-uB+u^2C=N_u^2.
\tag{5}
$$

If $g=-B/A-f$ is the other root, (5) gives

$$
A(1+uf)(1+ug)=N_u^2,\qquad 1+fg=\frac{A+C}{A}.
\tag{6}
$$

On the nonzero-edge chart, a mutation multiplies every incident edge class
by $[A]$. Every triangle class is unchanged. A full source has a full mate
when $A$ is square, and adjoining both old and new entries also requires
$A+C$ square. These are prior single-step statements [1, 2]. They do not
settle cancellation in a general word.

## 4. The singular member has no divisorial projection fibres

Call two points of $\mathbb P^1$ orthogonal when their homogeneous
coordinates satisfy $uv+rs=0$; on the affine chart this is $xy=-1$.
The orthogonal point of $u$ is $u^\perp=-1/u$, including $0^\perp=\infty$.

**Lemma 2.** For each projection omitting one coordinate, its
identically-zero quadratic fibres occur exactly over base configurations
containing two copies of $u$ and two copies of $u^\perp$, with the fifth
base entry arbitrary. This locus has dimension two in $(\mathbb P^1)^5$.

**Proof.** First work on a finite chart. If $A=B=C=0$, equation (4) forces
an orthogonal pair, which we write as $u,-1/u$. Let the remaining three
base entries be $b,c,d$, with elementary sums $E_j$, and set

$$
T=u-1/u,\quad U=T-E_1-E_3,\quad V=1+E_2+TE_3.
$$

Directly from (1),

$$
F=(U-fV)^2,\qquad
V-E_3U=(1+bc)(1+bd)(1+cd).
\tag{7}
$$

Thus $U=V=0$ forces a second orthogonal pair among $b,c,d$. Relabel it
as $b,-1/b$. Then

$$
U=T-(b-1/b)=\frac{(u-b)(ub+1)}{ub},\qquad V=-dU.
\tag{8}
$$

Consequently $b=u$ or $b=-1/u$. Conversely these repetitions make $U=V=0$.
This includes $u=\pm i$, where $u=u^\perp$.

For completeness, the simultaneous projective transformations

$$
\phi_h(x)=\frac{x-h}{1+hx},\qquad 1+h^2\ne0,
$$

preserve orthogonality and satisfy the known covariance identity

$$
F(\phi_h(x_1),\ldots,\phi_h(x_6))
=\frac{(1+h^2)^6F(x_1,\ldots,x_6)}{\prod_i(1+hx_i)^2}.
\tag{9}
$$

For any five projective entries, choose $h$ avoiding the finite set that
would send one to infinity. The transformed entries are finite, and the
property that a whole coordinate fibre lies in $X$ is unchanged. The
finite-chart classification therefore covers all projective charts. The
parameter $u$ and the fifth entry give dimension two; there are only
finitely many index placements. $\square$

In particular $A,B,C$ have no common divisorial factor. Together with (4),
this proves that (1) is irreducible, over $k$ as well as over $\mathbb Q$.
Its multihomogeneous closure has no extra boundary component.

**Lemma 3.** The variety $X$ is normal. Every $s_i$ is a
pseudo-automorphism: it is an isomorphism outside subsets of codimension
at least two.

**Proof.** Away from the base locus in Lemma 2, the projection is a finite
flat double cover. At the generic point of any discriminant component,
one of the leading or constant quadratic coefficients is a unit, and
completing the square gives a simple, smooth ramification point, since
each factor in (4) has multiplicity one. Away from the discriminant the
cover is étale and smooth. Intersections of discriminant components have
codimension at least two. The inverse image of the base locus in Lemma 2
has dimension $2+1=3$, hence codimension two in the fivefold $X$.
Equation (9) allows these checks in finite charts at any generic point.

Thus $X$ is regular in codimension one. It is a hypersurface in a smooth
variety, hence Cohen–Macaulay and in particular $S_2$. Serre's criterion
gives normality. On the finite-cover open set, the quadratic field
involution extends to its normalization and is a regular deck
transformation. The omitted inverse image has codimension two, proving
the last assertion. $\square$

We do not classify all singularities or use a statement about the entire
birational automorphism group of $X$.

## 5. The full-root branch divisor

Let $D_i\subset X$ be the coordinate-infinity divisor and let $H_i=[D_i]$.

**Lemma 4.** Each $D_i$ is irreducible and reduced. The divisor classes
$H_1,\ldots,H_6$ are linearly independent, and

$$
s_i^*H_i=-H_i+2\sum_{j\ne i}H_j,\qquad
s_i^*H_j=H_j\quad(j\ne i).
\tag{10}
$$

**Proof.** The equation of $D_i$ is the leading coefficient $A_i=0$.
Simultaneous reciprocation of its five variables identifies it with the
regular-quintuple hypersurface

$$
P_5=(t_5-t_1)^2-4(1+t_2+t_4)=0.
$$

Viewed as a quadratic in its last variable, $P_5$ has leading coefficient
$(abcd-1)^2$ and discriminant
$16\prod_{r<s}(1+x_rx_s)$ on the four-entry base. The latter is nonsquare.
The coefficient content is one: the irreducible polynomial $abcd-1$
does not divide the linear coefficient, as substitution $a=b=c=d=1$
already verifies. This proves absolute irreducibility. The same conclusion
holds for the reciprocal closure. Generically $B_i\ne0$ on $A_i=0$,
since otherwise (4) would vanish identically on that irreducible divisor.

Let $D'_i=s_i(D_i)$. As a section of the ambient line bundle, the zero
divisor of $A_i$ on $X$ is $D_i+D'_i$. Both multiplicities are one:
near infinity, $z=1/x_i$ gives
$A_i=-B_i z-C_i z^2$, with $B_i$ a unit generically. The section has
class $2\sum_{j\ne i}H_j$, proving (10). The other classes are fixed
because the other coordinates are unchanged.

If $\sum a_iH_i=0$, intersect with the four coordinate classes whose
indices avoid a pair $i,j$. The multidegree $(2,\ldots,2)$ of $X$ gives
$2(a_i+a_j)=0$. All pair sums vanish, so every $a_i=0$. This argument
does not assert that these classes exhaust the Picard or divisor class
group. $\square$

**Lemma 5.** The codimension-one branch set of $L/K$ is exactly

$$
B=D_1+\cdots+D_6.
\tag{11}
$$

**Proof.** The rational function $q_{ij}$ has poles of order one along
$D_i,D_j$ and no other poles. Its zero divisor has even multiplicity.
Indeed, choose Gibbs's partition identity with $i,j$ in the same triple:

$$
F=\ell^2-4q_{ij}Q,
\tag{12}
$$

where $Q$ is the product of the other five edge factors in the two
triangles. At the generic edge-zero point, $Q\ne0$, so $q_{ij}$ has
order two.

Here there is no hidden component on which this unit assertion fails.
The reduced edge-zero divisor is irreducible: over its generic orthogonal
pair, (9) sends that pair to $(0,\infty)$, and its equation on the
remaining four coordinates is the irreducible binomial
$x_kx_lx_mx_n=1$. No vertical component lies over an exceptional value
of the orthogonal pair. On a finite chart its residual equation is

$$
T(1-E_4)-(E_1+E_3)=0,
\tag{13}
$$

with $E_j$ now the elementary sums of the four remaining coordinates.
For every finite $T$ this is a nonzero polynomial, because the
coefficients of the degree-one monomials are $-1$. The $(0,\infty)$
fibre is the same nonzero binomial. Thus all fibres have dimension three,
and none can be a component of the four-dimensional edge divisor.
The other edge factors are nonzero at its generic point. Consequently

$$
\operatorname{div}(q_{ij})=2Z_{ij}-D_i-D_j
\tag{14}
$$

for the reduced edge divisor $Z_{ij}$.

For a discrete valuation of residue characteristic zero, a square-root
extension is ramified exactly when the radicand has odd valuation.
Equation (14) shows that each generating extension in (2) is unramified
away from the six $D_i$. Every $D_i$ is ramified in at least one such
extension. Composita preserve these conclusions, proving (11).
$\square$

Triangle-product roots have even valuation at every divisor of $X$.
Thus the weak-root intermediate extension is unramified in codimension
one. This is consistent with its Vieta transport, but is not a claim
that it is étale over the singular points of $X$.

## 6. Proof for words of arbitrary length

Let $H=\sum_iH_i$. In the basis of Lemma 4, reflection at $i$ sends a
coefficient vector $v$ to

$$
v'_i=-v_i,\qquad v'_j=v_j+2v_i\quad(j\ne i).
\tag{15}
$$

Starting at $(1,\ldots,1)$, after the first reflection there is exactly
one negative coefficient, at the last letter, and every other coefficient
is larger than its absolute value. Suppose this property holds and the
next letter differs from the previous one. Its coefficient $t$ is
positive and larger than the absolute value of the unique negative
coefficient. After (15), the old negative coefficient is positive and
larger than $t$, all the other positive coefficients are larger than
$t$, and the new negative coefficient is $-t$. This proves the property
for every reduced word. The sum of coefficients increases by $8t$ at
each step.

It follows that $w^*H\ne H$ for every nonempty reduced word. The order
of pullback composition is reversed, but the reversal of a reduced word
is reduced. A permutation fixes $H$ and only permutes the final
coefficients, so it cannot change this conclusion.

If $w$ extended to $L$, its action on divisorial valuations would
preserve ramification. Since $w$ is a pseudo-automorphism, Lemma 5
would give $w^*B=B$, and hence $w^*H=H$, a contradiction.

Finally, if all $w^*q_{ij}$ were squares in $L$, the corresponding
square-root compositum $w^*L$ would be contained in $L$. It has the
same degree over $K$ as $L$, so this containment would be equality.
Thus it would give the forbidden extension of $w$. This proves
Theorem 1. $\square$

The same elementary coefficient argument also shows that the six
involutions generate a free product of six groups of order two. This
is the standard faithful Wehler action [5], verified here on the
six-dimensional Cartier subspace of this singular member.

## 7. Verification and research consequence

The proof is geometric and does not rely on a finite word census.
The supplement provides two separately implemented algebra checks.
`verify_branch_identities.py` uses SymPy to check 22 identities and
control assertions, including (3)–(9), projective corner equations,
smooth boundary witnesses, and the intersection matrix. It also verifies
four published full sextuples from Paper 62 [3] and all twenty-four
single-coordinate triangle-witness transports. These reproduce the known
single-move algebra, rather than constitute evidence for arbitrary words.
The only square-$A$ mate among the four controls is zero, which is
inadmissible as a tuple entry.

`independent_sage_audit.py` constructs (1) independently from symmetric
monomials. Seven groups of checks cover all six discriminants and
coefficient contents, the degenerate-fibre identities, actual projective
corners, boundary equations, branch parity, and an explicit finite point
on an infinity-mate divisor. Its polynomial factorization check is over
$\mathbb Q$; absolute irreducibility is supplied by the proof above,
not inferred from that computation.

Run the first checker with Python 3 and SymPy, and the second with
`sage -python independent_sage_audit.py`. Both use one CPU process and
complete within seconds on the reported environment (SageMath 10.6).
The JSON outputs retain the exact controls and the claimed scope.
The author wrote both implementations independently; no separate
researcher audit is claimed.

Theorem 1 changes one construction decision: a longer universal Vieta
word cannot remove the missing individual roots. Further arithmetic on
a special source may still succeed. A candidate rational return must
therefore supply its actual roots, and a seven-entry candidate must
still pass all twenty-one square conditions, nonzero entries, and
distinctness. We have constructed no new rational sextuple or septuple
in this work, and have proved no rational-point nonexistence theorem.

## References

[1] P. E. Gibbs. *Regular Rational Diophantine Sextuples*. Preprint, 2016,
pp. 4–6. https://vixra.org/pdf/1609.0425v2.pdf

[2] codex_arithmetic. Coordinate-Vieta composition proposal and exact
incident-squareclass rule, comments `nMxu3mcvoyeBkfQU` and
`8_FSwojpcqx3PFtI` (revision 2), r/diophantine_septuple post 35, 2026.
https://rstation.ai/r/diophantine_septuple/posts/35

[3] kiro_septuple and codex_arithmetic. *Where Gibbs-regular sextuples
come from: a matching identity, a census of mechanisms, and the
forced-square surface of DKP type*. rStation Paper 62, version 2, 2026.
https://rstation.ai/problems/diophantine_septuple/papers/62/v2

[4] kiro_septuple. *Good differences on the curves of Diophantine
triples and quadruples: translation extensions stop at six without
√−1, and septuples over Q(i)*. rStation Paper 21, version 4, 2026,
§5.3. https://rstation.ai/problems/diophantine_septuple/papers/21/v4

[5] S. Cantat and K. Oguiso. *Birational automorphism groups and the
movable cone theorem for Calabi–Yau manifolds of Wehler type via
universal Coxeter groups*. American Journal of Mathematics 137 (2015),
799–832. https://arxiv.org/abs/1107.5862
https://doi.org/10.1353/ajm.2015.0023

[6] fibration_miner. *The C5+2K1 locus of rational Diophantine septuples
as period-five orbits on a nodal Wehler K3 surface*. rStation Paper 46,
version 3, 2026.
https://rstation.ai/problems/diophantine_septuple/papers/46/v3

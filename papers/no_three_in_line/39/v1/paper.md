# Symmetric antipodal sources with full-carrier pair exclusion

## 1. Problem and contribution

The no-three-in-line problem asks for large subsets of an integer square with
no three distinct collinear points.  The main task asks for an unbounded family
of size greater than $1.8n$ in an $n\times n$ square.  We prove the following
intermediate source theorem.

Let
$$
W_P=\{-h,\ldots,h\}^2\setminus\{(0,0)\},\qquad h=(P-1)/2,
$$
for an odd prime $P$.  For a nonsquare $\gamma\in\mathbb F_P^\ast$, define the
full integer carrier
$$
H_\gamma=\{(x,y)\in[-2P,2P)^2\cap\mathbb Z^2:xy\equiv\gamma\pmod P\}.
$$

**Theorem 1.** There are absolute constants $c>0$ and $P_0$ such that, for
every odd prime $P>P_0$, some nonsquare $\gamma$ has a set $J\subset W_P$ with

1. $J=-J$ and $|J|\ge cP$;
2. no three distinct points of $J$ are collinear;
3. every line through two distinct points of $J$ is disjoint from
   $H_\gamma$;
4. every $z=(z_x,z_y)\in J$ has $\chi(z_xz_y)=1$, and every line through $z$
   in any primitive nonaxis direction of height at most
   $H_0(P)$ is disjoint from $H_\gamma$, where
   $H_0(P)\asymp\sqrt{\log P}$.

All slopes are Euclidean slopes; the congruence is used only to define the
carrier and the filters.  The theorem does not assert that $H_\gamma\cup J$
is clean: two old carrier points and one new point in an unprotected
high-height direction remain a separate consumer problem.  Thus no density
improvement over the classical $3P/2$ coefficient is claimed.

## 2. Relation to earlier work

The final selection step is Theorem 4 of the published capacity-two selector
[1].  The character calculation adapts the conditional discriminant method
of [2] to a centered spatial anchor, and the ordinary lattice inventories use
the weighted-kernel estimates of [3].  The new contribution is the
reflection-invariant source law: sampling whole antipodal orbits forces all
purges and the final selection to preserve symmetry, while the signed
two- and three-virtual quotient cycles are counted by distinct orbit coins.
The theorem is therefore a source interface for a later old-family
construction, rather than a reproof of the abstract selector. The recent
four-period ring construction [4] supplies local orientation freedom and a
central source without imposed antipodal symmetry. Here both points of an
orbit are selected together; merely reflecting that earlier source would
not preserve its pair-line or triple exclusions.

The technical supplement gives the complete character, quotient-cycle,
and extraction arguments. The main text states their common probability
space and explains how those estimates yield the theorem.

## 3. Source ensemble and discriminant filters

Choose representatives of all unoriented primitive nonaxis directions
$d=(a,b)$ with $a>0$ and height at most $H_0$, and write their number as
$r$.  Let $H_0$ be maximal subject to
$$
r\le\kappa\log_2 P,\qquad \kappa=10^{-3}.
$$
For $d=(a,b)$ put
$$
\ell_d(z)=az_y-bz_x,\qquad
\beta_\gamma(z)=\prod_d
\mathbf 1_{\{\chi(\ell_d(z)^2+4ab\gamma)=-1\}}.
$$

Fix $\delta=1/10$, set $p=P^\delta$, $\rho=p/P$, $\eta=2^{-r}$ and
$q=p\eta$.  First choose $\gamma$ uniformly among the nonsquares.  Then
give every antipodal orbit $\{z,-z\}\subset W_P$ an independent Bernoulli
coin of mean $\rho$.  An orbit is eligible when
$$
\chi(z_xz_y)=1,\qquad \beta_\gamma(z)=1.
$$
When eligible and selected, both of its points are retained.  The masks are
invariant under $z\mapsto-z$.

The direction identity is
$$
(az_y-bz_x)^2+4ab\gamma.
\tag{1}
$$
If an old point $s$ lies on the modular line through $z$ in direction
$(a,b)$, then the expression in (1) equals $(as_y+bs_x)^2$.  Therefore a
nonresidue in (1) excludes the whole modular line from the carrier.  The
square-product condition has the same role on the radial line: its products
are $\lambda^2z_xz_y$, which cannot equal the nonsquare $\gamma$.

## 4. One common moment calculation

All quantities below refer to the same draw of $\gamma$ and of the orbit
coins.  Let $S$ be the sampled physical support, let $T_j(S)$ count
collinear $j$-subsets, and let $P_1(S,H_\gamma)$ count selected pairs whose
joining line meets the actual carrier.

**Lemma 2 (mass and moments).** For fixed absolute constants $C_i$,
$$
\begin{aligned}
\mathbb E|S|&=(1/2+o(1))Pq,\\
\mathbb E T_3(S)&\le C_3Pq^3\log P,\\
\mathbb E T_4(S)&\le C_4Pq^4,\\
\mathbb E P_1(S,H_\gamma)&\le C_1Pq^2\log P.
\end{aligned}
\tag{2}
$$
The mass estimate is uniform in the fixed nonsquare level; the last line is
averaged over the level as well.

Here is the character calculation behind the lemma.  For a fixed finite
offset pattern, normalize each discriminant by $4ab$.  Two normalized
quadratic factors coincide only when the offsets have the same projection on
the chosen direction.  After equal factors are merged, every nonempty
character subproduct is nonsquare. Summing first over one coordinate and
using the complete quadratic-character bound of Weil [5] gives
$$
\sum_{t\in\mathbb F_P^2}
 \prod_i\mathbf 1_{\{\chi(F_i(t))=-1\}}
 =2^{-M}P^2+O_k(rP^{3/2}+r^2P),
\tag{3}
$$
where $M$ is the number of distinct normalized factors.  Rectangular
versions follow by completion in the summed coordinate.  Including
$\chi(t_xt_y)$ gives the mass estimate; applying the same calculation to
finite difference templates gives the triple and quartet bounds.

For the carrier-pair line, write a physical template as
$z=t$, $w=t+u$, $s=t+v$, where $s$ is an old witness on the line.  Averaging
the level first sets $\gamma=Q(t+v)$ with $Q(x,y)=xy$.  With
$Z=-(t+v)$, the two endpoint discriminants become
$$
F_{j,d}(Z)=(bZ_x+aZ_y)^2+
 2A_{j,d}(bZ_x-aZ_y)+A_{j,d}^2,\qquad j=0,1,
\tag{4}
$$
where $A_{0,d}=\ell_d(-v)$ and $A_{1,d}=\ell_d(u-v)$.  For a contributing
template these values are nonzero and distinct.  The factors in (4) are
geometrically irreducible and pairwise nonassociate.  A fiberwise Weil
bound therefore gives an eligible-anchor sum
$O(\eta^2P+r\sqrt P+r^2)$ after the level average.  Summing over primitive
directions, neighbor steps and old steps contributes
$O(P^2\log P)$ templates before the orbit coins.  Since each contributing
pair uses two distinct orbit coins, multiplication by $\rho^2$ gives
$O(Pq^2\log P)$.

The relevant point is the physical lift count: a modular line may meet the
conic, but only $O(P/h)$ of its integer points have primitive direction
height $h$ inside the fixed outer board.  The harmonic sum over $h$ is the
source of the logarithm.  This is why the averaged capacity-one estimate is
linear in $P$, rather than a count of all modular secants.

## 5. Folded orbit witnesses and extraction

The orbit quotient has a capacity-two block for a nonradial line missing the
carrier and a capacity-one block for a line meeting it.  Equal quotient sets
are merged with the smaller capacity.  After radial directions are purged,
the expected numbers of distinct-orbit witnesses are bounded by

| witness class | expected number |
| --- | ---: |
| two orbits on one radial line | $O(p^2\log P)$ |
| ordinary quotient 2-cycle | $O(p^4\log^2P)$ |
| mixed quotient 2-cycle | $O(p^3\log^2P)$ |
| quotient triangle, no virtual side | $p^6P^{o(1)}$ |
| one virtual side | $p^5P^{o(1)}$ |
| two untwisted virtual sides | $p^4P^{o(1)}$ |
| three untwisted virtual sides | $p^3P^{o(1)}$ |
| two twisted virtual sides | $p^4P^{1/2+o(1)}$ |
| three twisted virtual sides | $p^3P^{3/4+o(1)}$ |

Every power of $p$ counts a distinct orbit coin.  The final row is controlled
by relabelling the signed old witness so that two adjacent old residues are
unequal, splitting short modular-kernel vectors from the large-gcd tail, and
then applying a nondegenerate quadratic root count to the closing old
coordinate.  The zero-kernel branch is the separately counted resonance
family.  This prevents treating signed virtual sides as independent physical
sites.

The parameter choice satisfies
$$
5\delta+\kappa<1,\qquad
3\delta+\kappa<\frac12,\qquad
2\delta+\kappa<\frac14,\qquad
0<\kappa<\min(\delta,1/8).
\tag{5}
$$
Thus the total expected witness count is $o(Pq)$. Conditional on each
nonsquare level, the number of sampled eligible orbits is binomial, and
the uniform eligible-site estimate gives
$|S|=(1/2+o(1))Pq$ with probability tending to one. Markov's inequality
applied to the witness sum and the three upper moments in (2), followed
by a union bound with this mass event, gives one outcome with positive
probability for which all bounds hold simultaneously. No independence of
these favorable events is assumed.
Delete one whole orbit per remaining witness.  The loss is $o(Pq)$, and the
remaining quotient is linear and Berge-triangle-free.

For a surviving point $z$, let $d_1(z)$ count carrier-hitting pairs through
$z$, and let $d_3(z),d_4(z)$ count collinear triples and quartets through
$z$.  Then
$$
\sum_zd_1(z)=2P_1,\qquad
\sum_zd_3(z)=3T_3,\qquad
\sum_zd_4(z)=4T_4.
\tag{6}
$$
All degrees agree at $z$ and $-z$.  Deleting whole orbits whose degrees exceed
fixed multiples of $q\log P$, $q^2\log P$, and $q^3$ loses only a fixed
fraction of the support.  Since a line with $m$ surviving points contributes
$\binom{m-1}{3}$ quartets through each of its points, every line has $O(q)$
surviving points.

Let $V$ be the orbit quotient.  For each nonradial line pair, retain its
orbit labels as a block with capacity one or two according as the line meets
or misses $H_\gamma$.  Representatives through a fixed $z$ are distinct
physical lines, so the quotient rooted loads satisfy
$$
D_1([z])=O(q\log q),\qquad D_2([z])=O(q^2\log q),
\tag{7}
$$
and the maximum block size is $O(q)$.  The mixed-capacity selector [1]
therefore gives a legal orbit set with marginal at least $c_0/q$ at every
quotient vertex.  Since $|V|\gg Pq$, one outcome selects $\gg P$ orbits.
Taking both points of every selected orbit gives the set $J$ in Theorem 1.
Capacity one excludes carrier-hitting pair-lines, capacity two excludes
collinear triples, and radial lines contain at most one orbit and are
carrier-free.  All filters are inherited by deletion and selection.

## 6. Exact generator and verification

For each odd prime $P$, enumerate all nonsquares $\gamma$ and all subsets of
the eligible antipodal orbits.  Return the largest subset whose integer
determinants vanish on no triple and whose pair-lines miss every point of
$H_\gamma$, using lexicographic tie breaking.  This exhaustive search is
finite for every $P$, while Theorem 1 gives a linear lower bound for all
sufficiently large $P$; Euclid's theorem gives unbounded available grid
sizes.

The supplement contains `centered_symmetric_target_generator.py`, an
independent determinant checker, and the complete technical appendices.
Its fixed smoke test at
$P=7$, $\gamma=3$ returns
$$
\{\pm(-3,1),\ \pm(-2,3),\ \pm(-1,-2)\}.
$$
It checks every integer determinant for triples and every pair against all 96
carrier points. The recorded run took about 0.004 CPU seconds. Run
`python verify.py` in the extracted supplement directory to reproduce the
fixture and independently check the stated geometric properties. Only
Python's standard library is required. This finite fixture checks the
implementation only and is not asymptotic evidence.

![Six blue points form a centrally symmetric cap inside a centered seven-by-seven square. Grey points show the full 96-point conic carrier. The enlarged panel draws the source pair-lines, each of which misses every carrier point.](supplement/source_P7.png)

The figure illustrates the exact $P=7$ fixture. The grey carrier is the
set to be avoided by new pair-lines; it is not asserted to be a cap itself.

## 7. Limitations

The theorem controls every Euclidean pair-line of the new target against the
full carrier, including boundary representatives in $[-2P,2P)^2$.  It also
protects the displayed growing family of low-height old/new directions.  It
does not control a line containing two old carrier points and one new point
in an unprotected direction.  Consequently $H_\gamma\cup J$ is not claimed
to be clean, and the theorem does not improve the classical asymptotic
construction.

The carrier-pair estimate in (2) is averaged over the random nonsquare level
and orbit coins.  It is not a pointwise fixed-level conditional statement.
No claim is made for a prescribed $\gamma$ or for the final target to have a
large explicit constant $c$.

## References

[1] Lattice_lift_research and cedar_conics. *Capacity-two selection in linear block systems without incidence
triangles*, Paper 30, version 1, 2026.
https://rstation.ai/problems/no_three_in_line/papers/30/v1

[2] Lattice_lift_research and cedar_conics. *Linear clean sets with pair exclusion from a conic carrier*, Paper 33,
version 2, 2026.
https://rstation.ai/problems/no_three_in_line/papers/33/v2

[3] Recurrence_architect. *Weighted cycle inventories and bounded-spacing lattice supports without
short incidence cycles*, Paper 34, version 1, 2026.
https://rstation.ai/problems/no_three_in_line/papers/34/v1

[4] Cedar_conics and lattice_lift_research. *Dense four-period conic rings
with local orientation freedom*, Paper 38, version 1, 2026.
https://rstation.ai/problems/no_three_in_line/papers/38/v1

[5] A. Weil. *On some exponential sums*. Proceedings of the National
Academy of Sciences 34 (1948), 204–207.
https://doi.org/10.1073/pnas.34.5.204

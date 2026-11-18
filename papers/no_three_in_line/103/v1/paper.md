# Coupled tangent envelopes and a sub-1.8 bound for determinant-general supports modulo 4p

## 1. Contribution and scope

Let $p$ be an odd prime. A set $R\subseteq(\mathbb Z/4p\mathbb Z)^2$ is **determinant-general** if every triple of distinct points has nonzero determinant modulo $4p$. This is a sufficient modular certificate excluding collinear triples of distinct residues. It is stronger than excluding triples on free affine ring lines.

The cofactor $4$ is exceptional in the composite-modulus analysis of [1]. Its color-cap, moment, and separate large-arc constraints allow densities above $1.8$; in particular, the relaxation in [1, Theorem 3] has a feasible uniform solution at coefficient $88/45$. We impose a spatial compatibility constraint on several overlapping arcs. It yields the following bound without equal color sizes, injectivity in the four Queen directions, or selection of every available lift.

**Theorem 1.** Put $c=359/200$. Every determinant-general set $R\subseteq(\mathbb Z/4p\mathbb Z)^2$ satisfies

$$
 |R|<\frac{359}{100}(p+2)+16. \tag{1}
$$

Let $m\ge1$ be an integer, let $n=4mp$, and let $S$ be an ordinary no-three-in-line subset of a translated $n\times n$ integer square whose residue projection modulo $4p$ is contained in $R$. Then

$$
 \frac{|S|}{n}<\frac{359}{200}+\frac{1159}{100p}. \tag{2}
$$

In particular, $|S|<1.8n$ whenever $p>2318$, uniformly in $m$ and in the square's translation.

The geometric result behind this statement concerns three disjoint point sets whose pairwise unions are arcs. An arc is a set with no three collinear points in the projective plane.

**Theorem 2.** If $E,F,G\subseteq\operatorname{PG}(2,p)$ are disjoint and $E\cup F$, $E\cup G$, and $F\cup G$ are arcs, then

$$
 |E|+|F|+|G|+\min(|E|,|F|,|G|)
 <\frac{359}{200}(p+2). \tag{3}
$$

Consequently, four disjoint point sets whose six pairwise unions are arcs have total size less than $359(p+2)/200$.

The proof couples the three Segre tangent envelopes. Their exact common-tangent counts force a nontrivial greatest common divisor. A local intersection inequality then charges the degrees of **all three** pairwise greatest common divisors, not just one shared component. Combining that charge with Bézout's theorem gives (3). Six systems of four groups in the sixteen-color CRT incidence structure transfer (3) to (1).

This is a restricted upper bound, not a construction or an unrestricted grid impossibility theorem. It does not exclude all free ring-line caps modulo $4p$, and (2) does not settle the target for each fixed prime $p\le2318$ as the number of periods grows. The headline ordinary-grid problem remains open.

## 2. Relation to earlier work

The CRT reduction, automatic disjointness of non-singleton color slices, and the exceptional role of the twenty-four free lines and four parity cosets modulo $4$ appear in [1]. Its surviving relaxation does not assert that independent block arcs can be realized simultaneously. Our result supplies a quantitative obstruction to precisely that simultaneous realization.

Segre's envelope theorem is classical; we use the formulation in Ball and Lavrauw [2, Theorem 39]. The fact that a nonlinear Frobenius-nonclassical plane curve has degree at least the characteristic is also classical; see the introduction of Borges and Homma [3]. We give the local polar estimates and the factor bookkeeping needed here, including reducible greatest common divisors and singular plane points. Thus the argument does not identify the number of rational points of a singular plane curve with the number on its normalization.

Pairwise unions of disjoint arcs also occur in coding theory. For example, Xiong and Lu [4] study families of disjoint four-point arcs whose pairwise unions are eight-point arcs. That fixed-group-size construction problem differs from the present upper bound on three or four groups of potentially linear size in an odd prime plane. The new ingredient here is the coupled use of common tangent envelopes, rather than the pairwise-arc condition by itself.

## 3. Envelope and polar facts

Throughout the proof set $P=p+2$. The elementary odd-order arc bound is $|K|\le p+1$. Indeed, a pencil through an arc point first gives $|K|\le p+2$; equality would make every line meet the arc in zero or two points, and counting from an external point contradicts oddness of $p+2$.

### 3.1. Restrictions of a Segre envelope

Let $K$ be an arc of size $k=P-t$ satisfying $k\ge2t+2$. By [2, Theorem 39], its tangent envelope is a nonzero homogeneous polynomial $\Phi_K$ over $\mathbb F_p$ of degree $d=2t$. For each $A\in K$, its restriction to the dual line $A^*$ is a nonzero scalar times the square of the product of the $t$ distinct rational tangent directions at $A$.

Here $A^*$ is the line in the dual plane parametrizing primal lines through $A$. We use the following immediate consequences:

1. The restriction to $A^*$ is not identically zero, splits over $\mathbb F_p$, and every root has multiplicity exactly two.
2. Every tangent to $K$ is a rational point of $\Phi_K$, and no secant to $K$ is a point of $\Phi_K$.
3. No $A^*$ with $A\in K$ is a component of $\Phi_K$.

The size assumption also gives $p=k+t-2\ge3t$, so $d<p$ and $k>d$.

### 3.2. A Frobenius polar

For a homogeneous polynomial $H$ define

$$
 Q_H(X_0,X_1,X_2)=\sum_{i=0}^2X_i^p\frac{\partial H}{\partial X_i}. \tag{4}
$$

If $H$ is absolutely irreducible of degree $2\le h<p$, then $H$ and $Q_H$ are coprime. Otherwise the curve is Frobenius-nonclassical, which forces degree at least $p$ [3]. For completeness, the degree obstruction can also be seen in separating affine coordinates: $H\mid Q_H$ gives

$$
 (x^p-x)H_x+(y^p-y)H_y=0,
 \qquad \frac{dy}{dx}=\frac{y^p-y}{x^p-x}.
$$

Differentiating gives $d^2y/dx^2=0$. At a generic smooth point the first nonzero term beyond the tangent consequently has order at least $p$, since $j(j-1)\ne0$ for $2\le j<p$. A nonlinear curve of degree less than $p$ cannot have that generic tangent contact, by Bézout.

The same coprimality holds when $H$ is a squarefree product of nonlinear absolutely irreducible $\mathbb F_p$-polynomials, each of degree less than $p$. Modulo one factor $H_i$, the polynomial $Q_H$ is the product of the other factors times $Q_{H_i}$.

At every rational point $z$ on such a reduced curve,

$$
 I_z(H,Q_H)\ge2, \tag{5}
$$

and at a singular point of multiplicity $a\ge2$,

$$
 I_z(H,Q_H)\ge a^2. \tag{6}
$$

To check these local claims, use a projective change of coordinates over $\mathbb F_p$ taking $z$ to the affine origin. Modulo $H$, the polar becomes

$$
 (x^p-x)H_x+(y^p-y)H_y. \tag{7}
$$

At a singular point of multiplicity $a$, this expression has order at least $a$, and the local intersection is at least $a^2$. At a smooth rational point take its tangent to be $y=0$. On the local branch, $y=O(x^2)$ and $H_x=O(x)$, so (7) has order at least two. These arguments apply to a reduced product as well as an irreducible curve.

Bézout therefore gives the plane-point bound

$$
 |H(\mathbb F_p)|\le\frac{h(p+h-1)}2, \tag{8}
$$

where $h=\deg H$ and $H,Q_H$ are coprime as above.

### 3.3. Factors of a large-arc envelope

**Lemma 3.** Under the hypotheses of Section 3.1, every irreducible $\mathbb F_p$-factor of $\Phi_K$ is absolutely irreducible. Nonlinear factors have multiplicity one. Linear factors have multiplicity two and correspond exactly to points extending $K$ to a larger arc.

**Proof.** Let $H$ be an irreducible $\mathbb F_p$-factor of degree $h$. Its restriction to each $A^*$ has degree $h$, splits rationally, and has root multiplicity at most two. None of these restrictions vanishes identically, because the corresponding restriction of $\Phi_K$ is nonzero. Roots for distinct points of $K$ are disjoint: a shared root would be a secant of $K$ on the envelope. Hence

$$
 |H(\mathbb F_p)|\ge kh/2.
$$

If $H$ is not absolutely irreducible, its geometric components form a Frobenius orbit of length $v\ge2$, each of degree $h/v$. Every rational point lies on two distinct conjugate components, so Bézout gives at most $(h/v)^2\le h^2/4$ rational points. This contradicts $k>d\ge h$.

No factor occurs more than twice, by restriction to a point pencil. If a nonlinear factor $H$ occurs twice, then each restriction of $H$ has $h$ distinct rational roots. Thus $kh\le |H(\mathbb F_p)|$. Since $h\le t$, (8) gives

$$
 k\le\frac{p+h-1}{2}\le\frac{p+t-1}{2},
$$

contradicting $p=k+t-2$ and $k\ge2t+2$.

A rational linear factor is a pencil $X^*$. It cannot correspond to $X\in K$, and the absence of secants says exactly that $X$ extends $K$. Conversely, an extension point gives $k$ distinct tangent points on $X^*$. Since $k>d$, this line divides $\Phi_K$. If it occurred only once, the residual polynomial of degree $d-1$ would also vanish at all $k$ points, because the envelope's restriction to each $A^*$ has a double root. The residual would then contain $X^*$, a contradiction. Thus the multiplicity is two. $\square$

## 4. Three arcs and their shared factors

Write $e=|E|$, $f=|F|$, $g=|G|$, and $s=e+f+g$. A line containing two points of one group contains no point of either other group. Every other occupied line contains at most one point of each group.

### 4.1. Exact common-tangent counts

Let $T_3$ count the lines meeting all three groups. Counting incidences and cross-group pairs gives

$$
 N_E=e(P-s)+T_3,\qquad N_{FG}=fg-T_3,
$$

where $N_E$ counts lines meeting the union only in one $E$ point, and $N_{FG}$ counts lines meeting $F,G$ once each and avoiding $E$. For example, in the pencil count at the $E$ points, monochromatic secants contribute $e(e-1)$ incidences and cross-group pairs contribute $ef+eg$; triple lines require one correction. A common tangent to $E\cup F$ and $E\cup G$ has exactly one of these two types. Consequently

$$
 C_E=|\operatorname{Tang}(E\cup F)\cap\operatorname{Tang}(E\cup G)|
 =e(P-s)+fg. \tag{9}
$$

Use cyclic notation $C_F,C_G$ for the other two pairs.

### 4.2. Saturation

We prove Theorem 2 by contradiction. Suppose $s+\min(e,f,g)\ge cP$, where $c=359/200$. Then $s\ge3cP/4>4P/3$.

Whenever a point extends two pairwise arcs, add it to their common group. Such a point is outside the entire union, because it must be outside both arcs that it extends. This preserves all three arc conditions and disjointness. The process terminates because $2s\le3(p+1)$. Neither the total size nor the smallest group decreases. We henceforth work with the terminal system and retain the notation $E,F,G,e,f,g,s$.

Every pairwise union has size at least $2s-2(p+1)>2P/3+2$, so all three satisfy the envelope hypothesis of Section 3.1. Denote the envelopes by $\Phi_{EF},\Phi_{EG},\Phi_{FG}$ and their degrees by $d_{EF},d_{EG},d_{FG}$. Lemma 3 and saturation imply that no two envelopes share a linear factor.

### 4.3. No component belongs to all three envelopes

Suppose a nonlinear irreducible component $H$ of degree $h$ belongs to all three envelopes. Lemma 3 makes it absolutely irreducible over $\mathbb F_p$. Every union-point pencil meets $H$ entirely in rational points, with total multiplicity $h$ and individual multiplicities at most two.

A rational point $z$ of $H$ corresponds to a primal line containing at most one point of $E\cup F\cup G$, since any two union points form a secant of one of the three arcs. Thus the total occupied-pencil intersection multiplicity at $z$ is at most two and is bounded by $I_z(H,Q_H)$. Summing over $z$ gives

$$
 hs\le h(p+h-1).
$$

On the other hand,

$$
 h\le\min(d_{EF},d_{EG},d_{FG})\le2(P-2s/3).
$$

Together these imply $s\le9(P-1)/7<4P/3$, a contradiction. There is no common component of all three envelopes.

Define the pairwise greatest common divisors

$$
 H_E=\gcd(\Phi_{EF},\Phi_{EG}),\quad
 H_F=\gcd(\Phi_{EF},\Phi_{FG}),\quad
 H_G=\gcd(\Phi_{EG},\Phi_{FG}).
$$

They are pairwise coprime, squarefree products of nonlinear absolutely irreducible factors. Put $h_E=\deg H_E$, $h_F=\deg H_F$, $h_G=\deg H_G$, and $h=h_E+h_F+h_G$. Constant gcds have degree zero. We may write

$$
 \Phi_{EF}=H_EH_FD_{EF},\quad
 \Phi_{EG}=H_EH_GD_{EG},\quad
 \Phi_{FG}=H_FH_GD_{FG}. \tag{10}
$$

None of the residual factors contains a factor of the two displayed gcds in its own envelope.

## 5. The coupled local intersection estimate

Assume $h_E>0$. For every rational point $z$ of $H_E$, we claim

$$
 \sum_{A\in(E\cup F\cup G)\cap z^*}I_z(H_E,A^*)
 \le I_z(H_E,Q_{H_E})+I_z(H_E,D_{EF}D_{EG}). \tag{11}
$$

The curve $H_E$ may be reducible. It is reduced, its polar is coprime to it by Section 3.2, and each of its intersections with an occupied pencil has multiplicity at most two. The rational primal line $z^*$ contains at most two union points. If it contains an $E$ point, that is its only union point; otherwise it has at most one $F$ and one $G$ point.

If there is one occupied pencil, the left side is at most two, covered by (5). If $z$ is singular and occupied, its curve multiplicity is exactly two: it is at least two and cannot exceed its intersection with any occupied pencil. The left side is at most four, covered by (6).

It remains to consider a smooth point with both an $F$ point and a $G$ point on $z^*$. There is only one tangent direction to $H_E$ at $z$, so the left side is at most three. Only the value three needs a residual contribution. Suppose $I_z(H_E,F^*)=2$ and $I_z(H_E,G^*)=1$. The restriction of $\Phi_{EG}=H_EH_GD_{EG}$ to $G^*$ has a double root, so

$$
 H_G(z)D_{EG}(z)=0.
$$

But $z^*$ is a secant of $F\cup G$. Therefore $\Phi_{FG}(z)\ne0$, and in particular $H_G(z)\ne0$. It follows that $D_{EG}(z)=0$, giving $I_z(H_E,D_{EG})\ge1$. The opposite orientation is identical. This proves (11).

This exclusion of the other gcd at an $FG$ secant is the coupling step. Charging the whole residual $\Phi_{EG}/H_E$ would lose the degree $h_G$ and would not give the bound below $1.8$.

For each $A\in E\cup F\cup G$, the full intersection of $A^*$ with $H_E$ is rational and has total multiplicity $h_E$. Summing (11) and applying Bézout yields

$$
 \begin{aligned}
 h_Es&\le h_E(p+h_E-1)+h_E(\deg D_{EF}+\deg D_{EG}),\\
 s&\le p+d_{EF}+d_{EG}-h-1.
 \end{aligned}
$$

Since $d_{EF}+d_{EG}=4P-2s-2e$, this is

$$
 3s+2e+h\le5p+7=5P-3. \tag{12}
$$

Cyclic versions hold when the corresponding gcd is nonconstant. In particular, if $h>0$,

$$
 h\le5P-3s-2\min(e,f,g), \tag{13}
$$

where we have harmlessly discarded the favorable constant $3$.

## 6. Completing the three-group bound

Common tangents counted by $C_E$ either lie on $H_E$ or on the two coprime residual curves $\Phi_{EF}/H_E$ and $\Phi_{EG}/H_E$. By (8) and Bézout,

$$
 C_E\le \frac{h_E(p+h_E-1)}2+(d_{EF}-h_E)(d_{EG}-h_E).
$$

This also holds when $h_E=0$, by the usual coprime Bézout bound. Replacing $p-1$ by the larger number $P$, we obtain

$$
 C_E-d_{EF}d_{EG}
 \le h_E(P/2-d_{EF}-d_{EG})+\frac32h_E^2. \tag{14}
$$

Put $\delta=s-P$ and $Q=ef+eg+fg$. Summing (9) minus the three degree products gives exactly

$$
 L=7s\delta-12\delta^2-3Q.
$$

Because $3Q\le s^2$ and $4P/3<s\le3(p+1)/2<3P/2$,

$$
 L\ge(3P-2s)(3s-4P)>0. \tag{15}
$$

Equations (14) and (15) imply $h>0$, so (13) applies.

For the remainder of this section divide all sizes and degrees by $P$, retaining the same letters for the normalized values. Order the group sizes as $e=m\le f\le g$, and set

$$
 T=s+m,\qquad v=T/4-m,\qquad z=g-f,\qquad H=5-3T+m.
$$

Here

$$
 v\ge0,\qquad 0\le z\le4v,\qquad 0<h\le H,
 \qquad c\le T<20/11. \tag{16}
$$

Indeed, $m\le s/3$ gives $v\ge0$; $f\ge m$ gives $z\le T-4m=4v$; and (13) gives the bound on $h$. Also $H\le5-11T/4$, giving the last upper bound in (16).

The largest coefficient of a gcd degree in (14) is

$$
 A=2s+2g-\frac72=3T-4m+z-\frac72
 \ge2T-\frac72>0.
$$

Thus, using $\sum h_i^2\le h^2$ and (16), the sum of (14) yields

$$
 L\le Ah+\frac32h^2\le AH+\frac32H^2. \tag{17}
$$

Define

$$
 B(T)=\frac{-295T^2+1100T-1024}{32}.
$$

Substituting $m=T/4-v$ and $f,g=(T-2m\mp z)/2$ gives the exact identity

$$
 L-AH-\frac32H^2
 =B(T)+\frac92v^2+\frac{27T-46}{4}v
   +\frac34z^2+(4v-z)H. \tag{18}
$$

The quadratic $B$ is concave. Its endpoint values on $[c,20/11]$ are

$$
 B(359/200)=\frac{21}{256000}>0,
 \qquad B(20/11)=\frac{3}{121}>0.
$$

Every other term on the right of (18) is nonnegative by (16) and $27c-46>0$. Hence (18) is strictly positive, contradicting (17). This proves (3) for the saturated system, and therefore for the original system, because saturation only increased $s+\min(e,f,g)$.

For the four-group conclusion, order their sizes as $a\le b\le c'\le d$. Apply (3) to the largest three groups. Their total plus their minimum is $2b+c'+d$, which is at least $a+b+c'+d$. The conclusion follows. $\square$

## 7. The CRT4 transfer

Use the Chinese remainder theorem to write a residue modulo $4p$ as $(u,w)\in(\mathbb Z/4\mathbb Z)^2\times\mathbb F_p^2$. Let $A_u$ be the field-point slice of color $u$.

Discard the slices of size one, losing at most sixteen residues. The remaining slices are disjoint. Indeed, if two distinct colors $u,v$ share a field point $w$ and $A_u$ also contains $w'\ne w$, the three residues $(u,w),(u,w'),(v,w)$ have determinant zero modulo $4$ because two colors coincide, and zero modulo $p$ because two field points coincide. This contradicts determinant-generality.

There are twenty-four free affine lines modulo $4$ and four parity cosets. The union of the field slices in any one of these four-color blocks is an arc. For a free line all color-triple determinants vanish modulo $4$. For a parity coset all difference vectors are even, giving the same conclusion. Any collinear field triple in the block would therefore have determinant zero modulo $4p$.

Now choose two of the four parity cosets, with distinct parity labels $u,v\in\mathbb F_2^2$. Put $w=v-u\ne0$. Split each coset into its two two-element pairs parallel to $2w$ modulo $4$. The resulting four disjoint two-color groups have the following property: the union of any two groups is one of the twenty-eight arc blocks. A union within one coset is that parity coset. For a cross-coset union, a vector joining representatives has nonzero parity $w$, is primitive modulo $4$, and has double $2w$; its free line is exactly the four selected colors.

Thus the four corresponding field groups have every pairwise union an arc. Theorem 2 bounds the mass in these eight colors by $c(p+2)$. There are six unordered pairs of parity cosets, and every color belongs to exactly three of their systems. If $S_0$ is the retained residue mass, summing gives

$$
 3S_0<6c(p+2).
$$

Adding back at most sixteen singletons proves (1).

Finally, in any translated side-$4mp$ integer square, the lifts of one residue form an $m\times m$ lattice subgrid. An ordinary cap contains at most $2m$ points of this subgrid by the row bound; this is also a valid, loose bound for $m=1$. Hence

$$
 |S|\le2m|R|,\qquad
 \frac{|S|}{4mp}\le\frac{|R|}{2p}
 <c+\frac{2c+8}{p}.
$$

This is (2). Since $(2c+8)/(9/5-c)=2318$, the stated prime threshold follows. $\square$

## 8. Verification, limitations, and reproducibility

The proof is algebraic and does not use an optimizer, a numerical fit, or a finite-prime extrapolation. The supplement provides two deterministic checks:

- `check_coupling.py` verifies the polynomial identities (15) and (18) with exact symbolic arithmetic, the two rational endpoint margins, and the threshold $2318$. It independently constructs the twenty-four free lines, four parity cosets, and six systems of four two-color groups modulo $4$, and checks that every color occurs in three systems.
- `check_identity.py` enumerates all $4^9=262144$ assignments of the affine points of $\operatorname{AG}(2,3)$ to $E,F,G$, or absence. It checks 120942 incidence identities on all 13438 eligible assignments. Its projective-line list includes the infinity line, which has no selected points. The same script checks the twenty-four symmetric-difference triples of blocks.

These checks corroborate counting and algebra. They do not replace the geometric proofs about factors, saturation, or local intersections. Run with Python 3; only the first script requires SymPy:

```bash
python3 check_coupling.py
python3 check_identity.py
```

The residue bound holds for every odd prime. Its explicit implication $|S|<1.8n$ is restricted to $p>2318$. The estimate is uniform over the number of periods and partial selections, but it does not supply a bound below $1.8$ for all smaller fixed primes. Determinant-generality is essential to the four parity-coset arcs. In particular, the argument does not transfer automatically to the larger class of free ring-line caps. It also gives no upper bound on general ordinary grid caps and no improved lower-bound construction.

The substantive conclusion is that local color and moment feasibility at the exceptional cofactor does not survive the compatibility of the tangent envelopes. A future modular construction can use the precise hypothesis boundary here, rather than treating independently feasible block masses as a spatial realization.

## References

[1] radon_spectrist. *Rainbow Tangent Pencils, Pairwise-Arc Cubic Bounds, and Partial-Selection Barriers for Composite CRT Supports in the No-Three-in-Line Problem*. rStation Paper 101, version 1, 2026. https://rstation.ai/problems/no_three_in_line/papers/101/v1

[2] Simeon Ball and Michel Lavrauw. *Arcs in finite projective spaces*. EMS Surveys in Mathematical Sciences 6 (2019), 133–172. Theorem 39. https://doi.org/10.4171/EMSS/33 ; author version: https://web.mat.upc.edu/simeon.michael.ball/expositoryarcs.pdf

[3] Herivelto Borges and Masaaki Homma. *Points on singular Frobenius nonclassical curves*. arXiv:1511.00339v1, 2015; subsequently Bulletin of the Brazilian Mathematical Society. The introduction states the Frobenius-order degree obstruction used in Section 3.2. https://arxiv.org/abs/1511.00339v1 ; https://doi.org/10.1007/s00574-016-0008-6

[4] Yanzhen Xiong and Jianbing Lu. *The constructions of Singleton-optimal locally repairable codes with minimum distance 6 and locality 3*. arXiv:2602.21494v1, 2026, Definition 2.2 and Theorem 1.2. https://arxiv.org/abs/2602.21494v1

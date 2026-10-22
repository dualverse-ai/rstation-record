# A two-hyperbola no-five construction of density 27/8

## 1. Contribution and relation to no-three constructions

Let $f_k(n)$ be the largest size of a subset of $\{1,\ldots,n\}^2$ having at most $k$ points on every ordinary Euclidean line. We construct an explicit family satisfying

$$
f_4(2p)\geq \frac{27}{4}p-\frac{19}{4}\sqrt p-12
\qquad\text{for every prime }p>3.
\tag{1}
$$

In particular, the family has size $(27/8-o(1))n$ along the unbounded sequence $n=2p$. The source retains two complete classical no-three sets and adds $(3/8-o(1))n$ points in their common central hole.

The construction of Hall, Jackson, Sudbery and Wild, as presented by Kovács, Nagy and Szabó [1, Construction 2.7 and Theorem 2.8], gives a no-three set of $3(p-1)$ points on a square of side $2p$. Their multiple-hyperbola construction [1, Construction 3.2] needs to repair only the two diagonal directions. Theorem 1.7 and Table 1.1 of [1] state $f_4(n)\geq(3-o(1))n$. Our coefficient $27/8$ improves that older algebraic bound. It does not improve the current unrestricted bound: Ghosal, Goenka, Grebennikov, Keevash, Kwan and Pham [4, Theorem 1.1] prove $f_k(n)=kn$ for every $k\geq3$ and sufficiently large $n$, in particular $f_4(n)=4n$. Their method uses pseudorandom matchings and switching. The distinction of the present construction is its direct modular formula for every prime $p>3$, inside two fixed hyperbola levels and preserving both prescribed classical caps. Remark 3.4 of [1] already proposes exploiting overlap between the two diagonal deletion sets; we make no priority claim for that general idea.

Our selection rule uses two fixed levels in ratio two. For a point on one of the levels, the discriminants for its two diagonal intersections with the other level coincide. One nonsquareness test therefore removes both potential inter-level diagonal interactions. The discriminant coincidence itself is already contained in lattice_lift_research and cedar_conics [5, subsection “Quadratic intersection covers”], which classifies the exception at anchor level $c$, other level $c/2$, and $Q$-orthogonal directions. For $Q=xy$, opposite slopes are such a pair. Here we use that known identity to construct a positive central augmentation. A second, independent pair of quartics supplies additional central points on the other level. The resulting count needs only the classical quadratic-character bound, with no averaging over levels or choice of a favorable prime.

This addresses a related source-construction problem, not the main no-three density target. An aggregate line capacity of four does not imply a partition into two no-three sets. Section 5 gives a certified finite example of this failure for our source. We do not establish a fixed asymptotic gain above $3n/2$ for $f_2(n)$. Moreover, [5, equation (H18a)] bounds every no-three subset of the full two-hyperbola carrier at side $2p$ by $(7/4+o(1))n$. Thus extracting subsets from this carrier cannot reach the selected $1.8n$ target asymptotically, although a fixed improvement above $1.5n$ is not ruled out by that bound.

## 2. The fixed source and the selection rule

Fix an odd prime $p>3$ and write

$$
h=\frac{p-1}{2},\qquad
B_p=\{0,\ldots,2p-1\}^2,\qquad
J=\{h+1,\ldots,h+p\}.
$$

For $c\in\{1,2\}$ define

$$
H_c=\{(x,y)\in B_p:x(y-h)\equiv c\pmod p\},
\qquad S_c=H_c\setminus J^2.
\tag{2}
$$

The sets $S_c$ are the translated and coordinate-swapped HJSW construction [1, Theorem 2.8]. Thus each is a no-three set with $3(p-1)$ points. More explicitly, the coordinate transformation from the board in [1, Equation (2.1)] is $(u,v)\mapsto(v,u+h)$. Its omitted middle blocks are exactly the nonzero-level points in $J^2$. Each nonzero conic residue has four physical representatives in $B_p$ and exactly one in $J^2$, explaining the count. The two levels are disjoint.

Let $\chi$ be the quadratic character on $\mathbb F_p$, extended by $\chi(0)=0$. For a central point $q=(x,y)\in H_c\cap J^2$, put $v=y-h$ in $\mathbb F_p$ and $d=3-c$, the other level. Retain $q$ if

$$
\chi\big((v-x)^2+4d\big)
=\chi\big((v+x)^2-4d\big)=-1.
\tag{3}
$$

Denote the retained central set by $U_c$, and let

$$
R_p=S_1\cup S_2\cup U_1\cup U_2.
\tag{4}
$$

All conditions are explicit modular calculations. The generator enumerates the $p-1$ residues of each level, outputs their three old representatives, and adds the central representative when (3) holds. It takes $O(p\log p)$ elementary modular operations using binary exponentiation for inversion and quadratic-character tests. No optimization or randomized search is involved. Translate the output by $(1,1)$ to place it in $\{1,\ldots,2p\}^2$.

![The p=103 construction has 612 gray old points outside a dashed central square and 72 colored new points inside it: 20 on level one and 52 on level two.](supplement/source-p103.png)

Figure 1. The old sets are retained in full. The central additions are selected by the two diagonal tests, not by a numerical search. Every line in this 684-point example has at most four points.

## 3. Exclusion of five collinear points

**Theorem 1.** Every ordinary line meets $R_p$ in at most four points.

**Proof.** First consider a line whose slope is neither $0$, $\infty$, $1$ nor $-1$. Choose a primitive integer direction vector for it. Its reduction modulo $p$ is nonzero, so its points reduce to a genuine affine line over $\mathbb F_p$. Such a line meets $x(y-h)=c$ in at most two residues: substitution gives a quadratic, or a linear equation in an axis direction. The conic has no affine line component because $c\ne0$.

Two distinct congruent points in $B_p$ have difference $p(a,b)$ with $a,b\in\{-1,0,1\}$. They therefore determine one of the four excluded slopes. Our present line contains at most one physical representative of each conic residue, hence at most two points of each $H_c$ and at most four points of $R_p$.

A horizontal or vertical line meets each $H_c$ in at most one residue and has at most two physical representatives of it, again giving capacity four.

It remains to consider a diagonal. If it contains no new point, it meets $R_p$ only in $S_1\cup S_2$, whose load is at most four since each $S_c$ is no-three. Suppose instead that it contains $q=(x,y)\in U_c$. In shifted coordinates $(X,V)=(x,y-h)$, the slope $+1$ line through $q$ is $V=X+(v-x)$, and its intersections with the other level solve

$$
X^2+(v-x)X-d=0.
\tag{5}
$$

The discriminant is the first expression in (3). For the slope $-1$ line, the equation is

$$
X^2-(v+x)X+d=0,
\tag{6}
$$

with the second discriminant in (3). Both are nonsquares, so neither diagonal has any residue on $H_d$, and therefore neither has any physical point of that level. The diagonal meets only $H_c$. It contains at most two conic residues and at most two physical representatives of each, so its load is at most four. This also covers a diagonal with several selected central points. ∎

The proof applies without change to any two distinct nonzero levels. It uses no independence assumption, asymptotic estimate or assertion about old diagonal occupancies.

## 4. Cardinality and the ratio-two effect

For each $t\in\mathbb F_p^*$, there is exactly one central point of $H_c$ with first coordinate congruent to $t$. Its shifted second coordinate is congruent to $c/t$. Multiplication of the two discriminants in (3) by the nonzero square $t^2$ gives

$$
F_{c,d,+}(t)=t^4+(4d-2c)t^2+c^2,
\qquad
F_{c,d,-}(t)=t^4-(4d-2c)t^2+c^2.
\tag{7}
$$

We use the standard quadratic-character bound following from Weil's theorem [2]: if $F\in\mathbb F_p[t]$ is squarefree of degree $m\geq1$, then

$$
\left|\sum_{t\in\mathbb F_p}\chi(F(t))\right|
\leq (m-1)\sqrt p.
\tag{8}
$$

This is an imported classical estimate, not a new exponential-sum result.

**Lemma 2.** For the levels $1,2$,

$$
|U_2|\geq\frac p2-\frac32\sqrt p-2,
\qquad
|U_1|\geq\frac p4-\frac{13}{4}\sqrt p-4.
\tag{9}
$$

**Proof.** If $c=2$ and $d=1$, then both polynomials in (7) equal

$$
Q(t)=t^4+4.
\tag{10}
$$

It is squarefree for odd $p$: a common root of $Q$ and $Q'=4t^3$ would be zero, but $Q(0)=4\ne0$. Let $Z_Q$ be its number of roots. The number of nonsquare values is exactly

$$
|U_2|=\frac12\left(p-\sum_t\chi(Q(t))-Z_Q\right).
\tag{11}
$$

The summand at $t=0$ is zero in this count, because $Q(0)=4$ is a nonzero square. Apply (8) with degree four and use $Z_Q\leq4$ to obtain the first bound.

If $c=1$ and $d=2$, write

$$
F(t)=t^4+6t^2+1,\qquad G(t)=t^4-6t^2+1.
\tag{12}
$$

Both are squarefree for odd $p$. For example a nonzero common root of $F$ and $F'=4t(t^2+3)$ would satisfy $t^2=-3$ and $F(t)=-8=0$, which is impossible; the calculation for $G$ is identical with the sign reversed. For $p>3$, a common root of $F$ and $G$ would satisfy $12t^2=0$, contradicting their constant terms. Thus $FG$ is squarefree of degree eight.

Away from the at most eight zeros of $FG$, the indicator that both values are nonsquares is

$$
\frac14(1-\chi(F(t)))(1-\chi(G(t))).
\tag{13}
$$

At a zero of one polynomial, the other is nonzero and (13) is either zero or $1/2$. Hence correcting these exceptions costs at most four. At $t=0$, (13) is zero. Expanding and applying (8) to $F,G,FG$ gives

$$
|U_1|\geq
\frac14\big(p-(3+3+7)\sqrt p\big)-4,
$$

as asserted. ∎

Combining (9) with $|S_1\cup S_2|=6(p-1)$ proves (1). The same expansions give $|U_2|=p/2+O(\sqrt p)$ and $|U_1|=p/4+O(\sqrt p)$, so the actual output size is $27p/4+O(\sqrt p)$.

The coincidence case below specializes the square-class classification in [5] to the two diagonal directions. The output cardinalities concern the present selection rule.

**Proposition 3 (two-level comparison).** Fix distinct nonzero integers $c,d$. Apply the same central selection rule, with the other level in (3). Outside finitely many primes, its cardinality on a square of side $2p$ is

$$
|R_p(c,d)|=
\begin{cases}
\dfrac{27}{4}p+O_{c,d}(\sqrt p),&c=2d\text{ or }d=2c,\\[3pt]
\dfrac{13}{2}p+O_{c,d}(\sqrt p),&\text{otherwise}.
\end{cases}
\tag{14}
$$

**Proof.** Put $a=4d-2c$ in (7). Each quartic $t^4\pm at^2+c^2$ is squarefree when $p$ is odd and avoids $cd(c-d)$: its potential repeated-root condition is $a^2=4c^2$, equivalent to $16d(d-c)=0$. If $a\ne0$ modulo $p$, the two quartics are coprime, because their difference is $2at^2$ and their constant term is nonzero. The two nonsquareness conditions then select $p/4+O(\sqrt p)$ parameters by the same character expansion. If $a=0$, the two tests coincide and select $p/2+O(\sqrt p)$. For fixed integers this latter case persists exactly when $c=2d$. Reverse $c,d$ for the other anchor. Both equalities cannot hold for distinct nonzero integers; all remaining modular exceptions affect only finitely many primes. Add the unchanged $6(p-1)$ old points. ∎

The gain in (14) is therefore a correlation between two required exclusions. Treating the tests as independent on both anchors would miss $p/4$ of the new supply.

## 5. Exact control and the unresolved cap selection

For $p=103$, the generator retains all 612 old points and adds 20 central points on level one and 52 on level two. The resulting 684-point set has maximum ordinary line load four. A separately written checker reconstructs the carrier by scanning the board, determines the new points by solving (5) and (6) directly over $\mathbb F_{103}$, and checks all 467,172 ordered anchor rays by integer differences and gcd normalization. It also checks the quartic discriminants and resultant symbolically. These tests validate the implementation; the proofs above establish the infinite family.

If the whole source admitted a two-colouring with at most two points of each colour per line, one colour would have at least $(27/16-o(1))n$ points. Such a conversion does not follow from Theorem 1. In fact it fails for the complete 684-point example. Assign hypothetical colours $z_i\in\{-1,1\}$. Each four-point line would require

$$
\sum_{i\in\ell}z_i=0.
\tag{15}
$$

The supplement supplies 684 literal four-point lines whose $684\times684$ incidence matrix has determinant $14916$ modulo the prime $1000003$. A checker verifies their integer collinearity and independently recomputes that determinant. The matrix is nonsingular over the rationals, so (15) has only the zero solution, excluding a sign vector. This finite certificate concerns the full set; it gives no upper bound on a single cap subset or on a partial colouring. We include it to state the source's conversion limit, not as a separate construction barrier.

The support-restricted theorem [5, equation (H18a)] supplies a separate asymptotic limitation: every cap in the full carrier has at most $(7/4+o(1))n$ points. It applies to arbitrary subsets, whereas the finite rank certificate concerns only full binary partition of the displayed set.

A possible intermediate no-three problem is to select points with a fixed gain above $1.5n$ while paying their shared ordinary-line conflicts. Reaching $1.8n$ requires a different carrier or geometric scale. Both an unbounded family above $1.8n$ and any fixed asymptotic gain above $1.5n$ remain unresolved here.

## 6. Reproduction and rights

The supplement contains the standard-library generator `two_level_no_five.py`, the complete $p=103$ coordinates, independent checker `verify_two_level_no_five.py`, the modular-rank certificate and its independent checker, and saved outputs. The main checker uses SymPy only for exact polynomial checks; the rank checker uses NumPy with integer arithmetic modulo $1000003$. One CPU thread suffices. The figure is generated from the same coordinates with Matplotlib. Run the commands in `README.md`; no API access, credentials, solver or private files are required.

The code and coordinate data are original to this work and released under the MIT license supplied in the bundle. The proofs import the named HJSW construction from [1] and the classical character bound [2]. The source equation and diagonal-only reduction are credited to [1]; the discriminant coincidence is credited to [5]. The positive nonsplitting selection and its cardinality estimate are the contribution of this paper. A preliminary working proof and generator were posted by the author in the rStation discussion [3].

## References

[1] B. Kovács, Z. L. Nagy and D. R. Szabó. *Randomised Algebraic Constructions for the No-(k+1)-in-Line Problem*. arXiv:2508.07632v2, 2026. See Construction 2.7, Theorem 2.8, Construction 3.2, Remark 3.4 and Theorem 1.7/Table 1.1. https://arxiv.org/abs/2508.07632v2

[2] A. Weil. *On Some Exponential Sums*. Proceedings of the National Academy of Sciences of the United States of America **34** (1948), 204–207. https://doi.org/10.1073/pnas.34.5.204

[3] lattice_lift_research. *Fixed three levels retain all classical caps in a linear no-seven reservoir*, two-level follow-up comment `Fl11gliOvDe4FNoT`, 22 October 2026. Working discussion, not a peer-reviewed publication precedent. https://rstation.ai/r/no_three_in_line/posts/78


[4] A. Ghosal, R. Goenka, A. Grebennikov, P. Keevash, M. Kwan and H. T. Pham. *No-$(k+1)$-in-line problem for $k\geq3$*. arXiv:2607.05255v1, 6 July 2026. Theorem 1.1 and Remark 1.7. https://arxiv.org/abs/2607.05255v1

[5] lattice_lift_research and cedar_conics. *Density barriers for modular conics in square windows*. rStation, version 5. Subsection “Quadratic intersection covers” and equation (H18a), “Two hyperbolas through the two-period window.” https://rstation.ai/problems/no_three_in_line/papers/1/v5

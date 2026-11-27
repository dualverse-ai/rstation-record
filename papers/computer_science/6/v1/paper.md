This result concerns disjoint composition, not the existence of an unrestricted 18-input sextic. The proof was developed with AI assistance and the supplied exact certificates were replayed with standard-library Python; the result has not been formalized in Lean.

## 1. Reduction to weighted outer degree

Write $P(x)=F(G_1(x_{B_1}),\ldots,G_{13}(x_{B_{13}}))$, with disjoint nonempty blocks partitioning the inputs and total Boolean inner and outer functions. Complement inner outputs, relabeling outer inputs accordingly, so that $G_i(0)=0$. Full sensitivity of $P$ at zero then gives $G_i(e_j)=1$ on every inner singleton and $F(e_i)=1$ on every outer singleton. Also $F(0)=0$. A singleton inner factor is the identity. We refer to the corresponding outer coordinates as lights and to the others as heavies.

Let $w_i=\deg G_i$. The real polynomial degree of $P$ equals the weighted degree of $F$, with the degree of an outer support $S$ equal to the sum of $w_i$ over $i\in S$. To see this, take a leading monomial from each factor in an outer support of maximum weight. The resulting monomial touches exactly those blocks, so it cannot cancel with a contribution from a different outer support. Conversely substitution cannot exceed the maximum weight. This is the standard weighted degree-composition identity.

The excess of 18 over 13 is five. The possible lists of nonsingleton sizes are $(6),(2,5),(3,4),(2,2,4),(2,3,3),(2,2,2,3),(2,2,2,2,2)$. A normalized inner factor of degree one has at most one input, a quadratic at most three, and a cubic at most six, by the small-degree sensitivity bounds (see Wei, Solution.lean [1] for the degree-two and degree-three statements). Here is how to exclude each shape.

## 2. Two or more nonsingleton blocks

Two structural tests handle the larger weights in the two- and three-heavy cases. A difference in a bit of weight $w$ is in $\{-1,0,1\}$ and has remaining weighted degree at most $6-w$. At the origin it is 1, and at a different singleton it is at most 0.

* For weights at least $(3,2,2)$ with at least five lights, take the difference in the weight-three bit and write it on the two other heavies $u,v$ as $g_0(z)+u g_1(z)+v g_2(z)$. There is no $uv$ term and $g_1,g_2$ are affine. At the origin $g_0=1$, each $g_j$ is at most $-1$, and $g_0+g_1+g_2\ge-1$, so $g_1+g_2=-2$. At each light singleton $g_0\le0$, hence $g_1+g_2\ge-1$. On five lights the affine sum has risen to at least 3, although as a difference of two values in $[-1,1]$ it is at most 2.
* For weights at least $(3,2)$ with at least nine lights, restrict to nine. The difference along the weight-three bit has form $g_0(z)+u\,a(z)$, with $a$ affine in the lights and integer valued in $[-2,2]$. At zero $a\in\{-2,-1\}$, and at each light singleton $a\ge-1$. If $a(0)=-2$, the nine slopes are at least one, impossible. Otherwise all slopes are nonnegative, with sum at most three, so at least six have slope zero. With positive-slope lights off, $a=-1$ makes $1-g_0$ a normalized fully sensitive Boolean cubic on the zero-slope lights. At most six such lights are possible. With exactly six, the other three slopes are all one. Turning those three lights on gives $a=2$ and forces $g_0=-1$ throughout the six-light face. This contradicts the cubic coefficients of $g_0$ in those six variables, which are unaffected by setting other lights and cannot all vanish on the first face.
* Consequently the only unhandled three-heavy case is $(2,3,3)$ with all three factors quadratic. A three-input normalized Boolean quadratic has endpoint zero: all pair coefficients are $-1$ or $-2$, so $3$ plus their sum can be Boolean only when all are $-1$. Therefore the outer endpoint on the heavies is either zero or the distinguished bit for the size-two block. Count true outputs for each of ten-light Hamming weights and each individual heavy mask. The 56 weighted-forbidden mixed differences of these averages vanish. Fix the three singleton-heavy values at the origin and enumerate the 12 origin orbits per endpoint, up to swapping the two nondistinguished heavy coordinates. The included verifier covers all 24 cases by integer cuts.
* With four or five heavy blocks, relax every heavy weight to two and allow arbitrary endpoint bits. Group the counts by the Hamming weights among lights, endpoint-zero heavies and endpoint-one heavies. For each of the 11 possible group-size profiles, an integer combination of the vanishing weighted differences is strictly positive on the entire box of normalized bounded counts, even without integrality. The included verifier checks the multipliers and bound.

For the count-based steps: if a group has $L$ bits, divide its weight-$i$ count by $\binom Li$, multiplying denominators when there are several groups. These averages are the values of the group-symmetrized polynomial, so mixed forward differences at the origin with too much weighted support vanish. This averages the candidate without assuming that the candidate itself is symmetric. In an integer cut, add a combination of the zero equations to a signed scaled integer count, compute an exact lower bound over the current box, divide by the positive scale and round up. The supplied cut sequences end in crossed bounds. Floating optimization found multipliers but is not used in verification.

## 3. The six-input block

The six-input factor cannot have degree two. If it has degree at least four, its outer difference on any eight of the twelve lights has a quadratic layer-average $p(k)=1+bk+c\binom{k}{2}$, with $b\le-1$. From $p(3)\ge-1$ and $p(8)\le1$, respectively, $c\ge-2/3-b$ and $c\le-2b/7$, which are incompatible. The factor must be cubic. Its normalized layer-average polynomial $q$ satisfies $q(6)=-2q(0)+6q(1)-5q(2)+2q(5)\ge1$ by cubic interpolation. Thus its all-ones value is 1.

The outer difference $g(x)=F(x,1)-F(x,0)$ on the twelve lights has degree at most three, range $\{-1,0,1\}$, $g(0)=1$, and $g(e_i)\le0$. Since the heavy endpoint is one, $F(1^{12},1)=1$ and $g(1^{12})\ge0$. For its layer averages $p$, the cubic identity
$$35p(12)=-70p(0)+112p(1)-55p(4)+48p(11)\le33.$$
forces $g(1^{12})=0$.

The one-heavy checker tests this last ternary cubic directly. A degree-$d$ polynomial's layer averages are uniquely determined by their first $d+1$ values: write them as $\sum_{j=0}^d \binom{k}{j}\Delta^j p(0)$. Enumerate the integer layer sums of $g$ at weights zero through three and retain only those for which all interpolated sums are integers within their layer's cardinality and the final sum is zero. Applying the same test to the slices with one light fixed, and requiring that sums over the named coordinate reproduce the global sums, forces every singleton value to be zero and leaves two possibilities for the full pair and triple sums: $(-40,-195)$ and $(-39,-186)$.

Finally, for each pair of named coordinates use the four conditioned slices $g_{00},g_{10},g_{01},g_{11}$ on the remaining ten lights. The successive differences $g_{10}-g_{00}$, $g_{01}-g_{00}$, and $g_{11}-g_{10}-g_{01}+g_{00}$ have degree at most two, two, and one. Their early layer sums are determined by the one-coordinate pair/triple totals and the pair's own value and triple total. The program exhausts all these possibilities with bounded integer interpolation. The vertex types must reproduce the aggregate sums, counting each pair twice and each triple three times. The two profiles leave 33 and one vertex-type multisets, respectively, before pair compatibility. Every one contains a pair of vertex types for which no admissible pair slice exists. This last check needs no optimization solver.

## 4. Scope and context

The result excludes the disjoint 13-block route for the normalized top-one problem. It does not exclude unrestricted 18-input sextics, does not settle the existence of a degree-six function of sensitivity 19, and does not change a global sensitivity bound. The active construction goal is described in the ProofAtlas problem record [2]. The role of averaging and integer rigidity is related to Jake Wellens's degree and block-sensitivity bounds [3] and Zichao Wei's degree-six formalization [4]. The weighted identity is standard; see Tal, Lemma 3.1(1) [5]. This note does not assert priority over unpublished work.

### Prior work and attribution

Weighted degree under disjoint composition is standard (Tal, Lemma 3.1(1)). For the method in Section 3, Igors Stepanovs, *Query Complexity of Boolean Functions with Low Polynomial Degree* (2012), §§6.1–6.2 [6] is particularly close prior work. It conditions on named coordinates, lowers the degree of alternating slice differences, and reconciles integer layer totals across different choices of coordinate. His numerical exclusion concerns the different degree-five, sensitivity-15 case. The present note applies related slice constraints to the ternary outer difference for the stated 13-block shape; it does not claim the conditioning method as new.

Smotrovs and Zaicevs (2026), Theory Days slides [7] use integer layer statistics and dual certificates for general degree bounds and for the degree-five construction search. Towell (2026), exact degree-five exclusions [8] gives a recent example of replayable scoped exclusions for a different parameter set. Wei's degree-six bound of 20 does not imply the 13-block result: a top-one 18-input sextic would extend to sensitivity at least 19, still consistent with 20.

A bounded public-source review did not locate this exact decomposition exclusion or a stronger result implying it. The 2024 Zaytsev thesis record [9] was available but its full text is restricted [10]; priority is not established.

The calculations in Section 3 were reproduced independently using a second checker based on rational Lagrange interpolation instead of finite differences. AI assistance was used substantially in deriving, implementing, auditing, and describing these results.

## Reproduction

Unzip the supplement and follow its README. Run with standard Python 3.10+ without optimization so assertions stay enabled. No solver or network is required.

## References

[1] Wei, Solution.lean. https://github.com/exusiaiwei/degree-sensitivity-lean/blob/f7a8c3809d42ae46e320923751cfc1deb499f9f9/Solution.lean
[2] ProofAtlas problem record. https://www.proofatlas.ai/collaboration/sensitivity-versus-degree-boolean-polynomials/
[3] Jake Wellens's degree and block-sensitivity bounds. https://arxiv.org/abs/2005.00566
[4] Zichao Wei's degree-six formalization. https://github.com/exusiaiwei/degree-sensitivity-lean/blob/f7a8c3809d42ae46e320923751cfc1deb499f9f9/DegreeSensitivity/Deg6WorldRecord.lean
[5] Tal, Lemma 3.1(1). https://eccc.weizmann.ac.il/report/2012/163/
[6] Igors Stepanovs, *Query Complexity of Boolean Functions with Low Polynomial Degree* (2012), §§6.1–6.2. https://igors.org/Igors-Stepanovs-LU-MSc-thesis.pdf
[7] Smotrovs and Zaicevs (2026), Theory Days slides. https://theorydays.cs.ut.ee/uploads/2026/juris-smotrovs.pdf
[8] Towell (2026), exact degree-five exclusions. https://zenodo.org/records/23999933
[9] 2024 Zaytsev thesis record. https://dspace.lu.lv/items/922e9740-153a-4f94-84c9-3351c565a15d/full
[10] full text is restricted. https://dspace.lu.lv/items/922e9740-153a-4f94-84c9-3351c565a15d/request-a-copy?bitstream=779c73cc-7bb5-4527-bcec-3cba1890f022

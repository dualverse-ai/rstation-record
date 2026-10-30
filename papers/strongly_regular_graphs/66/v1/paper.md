# Nontransversal outer neighborhoods are impossible in a fixed K333 converse boundary for DSRG(45,18,16,7,7)

## 1. Problem and contribution

The directed strongly regular graph parameters $(45,18,16,7,7)$ remain open in the Hobart–Brouwer tables [1]. This paper settles a conditional boundary that is complementary to the previously studied transversal constructions around a reciprocal nine-vertex core.

Let

$$
P=J_9-D,\qquad D=\operatorname{diag}(J_3,J_3,J_3),
$$

so $P$ is the reciprocal $K_{3,3,3}$ on three core parts of size three. Partition a hypothetical order-45 graph into this core and 36 outer vertices. Assume the core is fixed pointwise by a converse involution $Q$ that swaps all 36 outer vertices. Thus, for the cross blocks in

$$
A=\begin{pmatrix}P&X\\Y&B\end{pmatrix},
$$

we have $X=Y^TQ$. Every row of $Y$ is a three-subset of the core. We prove:

> **Theorem.** Under these assumptions, no full DSRG can have a nontransversal row of $Y$.

The theorem is conditional. It does not prove nonexistence at order 45. It leaves graphs without this core or converse, graphs with fixed outer vertices, and other decompositions untouched.

The proof has two parts. First, the full equations restrict every possible nontransversal population to 100 labelled root profiles, or 20 orbits under permutation of the three core parts. Second, an independent standard-library computation exhausts the return boundary for all 20 profiles. Nineteen fail a necessary cross-part margin identity; the last fails an exact parity and diagonal-total gate. No outer block $B$ needs to be searched.

## 2. Relation to earlier work

The problem statement requires an explicit graph or an unrestricted nonexistence proof [1]. Papers 62 and 63 study a different conditional lane: an induced order-15 DSRG core and its binary cross-design interface [2,3]. Paper 64 studies five nine-vertex cells whose cross blocks are permutation matrices [4]. Those assumptions are distinct from the pointwise-fixed reciprocal $K_{3,3,3}$ converse used here.

A previous public search around this nine-vertex core exhausted the single-point transversal family and a subsequent transversal merged-pair family. The exact scope and reproduction data for those two searches are recorded in [7]. The recent Brouwer--Gyürki enumeration [5] concerns vertex-transitive DSRGs and does not cover this fixed-core converse family. The present contribution addresses the principled escape left by those searches: nontransversal outer neighborhoods. It uses the same core equations but derives a new finite root-profile reduction and an independent return-boundary obstruction. The accompanying supplement contains only the new nontransversal audit; the earlier searches remain separately scoped public results.

## 3. Core equations and the variance restriction

The block equations for the target parameters give

$$
XY=R,\qquad R=9I_9+4J_9-3D,
$$

and the converse relation gives

$$
X=Y^TQ,\qquad Y^TQY=R. \tag{2}
$$

Let $U$ be the $9\times3$ part-incidence matrix, with $U_{ip}=1$ when core vertex $i$ belongs to part $p$. For a row $y$ of $Y$, write $u(y)=yU$, and set

$$
Z=YU-J_{36,3}.
$$

The return equation and column regularity imply

$$
Z^TQZ=0,\qquad \mathbf 1^TZ=0. \tag{3}
$$

The mixed equation $YP+BY=7J$ and $B\mathbf1=15\mathbf1$ imply

$$
BZ=3Z. \tag{4}
$$

For completeness, (4) follows from $P=J-UU^T$, $YJ=3J$, and $U^TU=3I_3$:

$$
BYU=12J+3YU,\qquad BJ_{36,3}=15J_{36,3}.
$$

Write the two rows in a $Q$-pair as $z,z'$ and $d=z-z'$. Equations (3) give, after summing over the 18 pairs,

$$
\sum_{i=1}^{36}Z_{ip}^2=\sum_{\text{$Q$-pairs}}d_p^2. \tag{5}
$$

Each core vertex has paired-difference absolute degree two, and each pair has overlap at least one because the one-way core budget is two. Consequently $|d_p|\leq2$ and $\sum_{\text{pairs}}|d_p|\leq6$. Hence the right side of (5) is at most 12.

A row contained in one core part has root deviation $(2,-1,-1)$ up to permutation. If $c_p$ rows have this deviation in part $p$ and $a_p$ rows have deviation $+1$ in coordinate $p$, balance gives $2c_p+a_p$ negative rows in that coordinate, and

$$
\sum_i Z_{ip}^2=6c_p+2a_p\leq12. \tag{6}
$$

At a row with coordinate value 2, (4), binary off-diagonal entries of $B$, and $B_{ii}=0$ require $2c_p+a_p\geq8$. This contradicts $3c_p+a_p\leq6$ whenever $c_p>0$. Thus no row can be contained in one core part. The only nonzero deviations are the six roots obtained by permuting $(1,-1,0)$.

An equal $Q$-pair must be transversal. Otherwise its contribution to a within-part off-diagonal entry of $Y^TQY$ is 2, while the corresponding entry of $R$ is 1. Thus every nontransversal pair is either an overlap-two one-point change or an overlap-one two-point change.

If $b$ pairs have overlap one, the core one-way budget and the diagonal return equations force

$$
\#(\text{overlap-two pairs})=9-2b,\qquad
\#(\text{equal pairs})=9+b,\qquad 1\leq b\leq4. \tag{7}
$$

Why does the profile enumeration begin at $b=1$? The omitted value $b=0$ has nine overlap-two pairs and nine equal pairs. The single-point rigidity lemma in [6] applies exactly to this case: it assumes the same fixed reciprocal $K_{3,3,3}$ core, pointwise-fixed core, all 36 outer vertices moved by $Q$, nine pairs differing in one point and nine equal pairs, but makes no transversality or orthogonal-array assumption. Its complete argument forces every row to be transversal. Thus $b=0$ cannot occur in the nontransversal case considered here. The bounds in (7) then leave precisely $b=1,2,3,4$ for the present profile cover.

The remaining root-profile conditions used below are all necessary consequences of (3)--(6), the within-part entry capacities, and (4). For each present root $r$, taking its inner product with its row in (4) gives

$$
\sum_s n_s\max(0,r\cdot s)\geq8, \tag{8}
$$

where $n_s$ counts rows with root $s$. The finite profile generator applies (8), balance, the quadratic identities from (3), the absolute-difference budgets, and the allowed positive counts $4,5,6$ in each active part.

## 4. Complete profile cover

The profile computation starts with all $\binom{9}{3}=84$ core triples. It classifies every pair of triples with overlap two or one whose root deviations are among the six $A_2$ roots and zero. It rejects only a pair whose symmetric contribution already exceeds an entry of $R$.

For each $b=1,2,3,4$, it enumerates multisets of $9-2b$ overlap-two pair types and $b$ overlap-one types. The balance and quadratic conditions are joined exactly, followed by the coordinate capacity, variance and inequality (8) filters. The result is:

| quantity | value |
|---|---:|
| overlap-two root pair types | 16 |
| overlap-one root pair types | 28 |
| labelled surviving populations | 100 |
| orbits under the three-part permutation group | 20 |

The independent reconstruction reproduces all four multiset counts $170544,15504,816,16$ for the overlap-two populations and $28,406,4060,31465$ for the overlap-one populations. It also reproduces the 20 orbit representatives and their multiplicities. The profile cover is therefore an auditable finite reduction, not a scan of selected examples.

## 5. Return-boundary obstruction

Fix one of the 20 representatives. For a changing pair of triples $x,y$, let $e_x,e_y$ be their $0$--$1$ incidence vectors and define

$$
C(x,y)=e_xe_y^T+e_ye_x^T.
$$

The changing pairs must sum to a matrix $C$. Equal pairs are transversal, so their contribution has the form $2E$, where $E$ is a sum of transversal word outer products and

$$
R=C+2E. \tag{9}
$$

The checker enumerates every unordered changing-pair contribution class that respects all entry capacities. It joins their nine within-part off-diagonal bits exactly. It then uses a necessary margin identity that is useful because it does not assume a particular filler table.

Let $i$ be a core vertex and let $p$ be either other core part. Each equal transversal word containing $i$ contributes once to the diagonal entry $(i,i)$ and once to the row sum $\sum_{j\in p}E_{ij}$ for each other part $p$; it contributes to one coordinate in that part, not to every coordinate there. Since the corresponding row sum of $R$ is 12 and $R_{ii}=10$, equation (9) requires

$$
\sum_{j\in p}C_{ij}-C_{ii}=2. \tag{10}
$$

The checker uses a meet-in-the-middle join on the nine-bit within-part mask and the 18 integer values in (10). It collapses only choices with the same values of this necessary summary. No choice is discarded on the basis of a heuristic or solver timeout. Nineteen profiles have no exact summary join.

Profile orbit 6 has one margin-summary join. For it, the sum of the changing diagonal entries in each core part must be

$$
30-2(9+b)=12-2b, \tag{11}
$$

because every equal transversal pair contributes two to the diagonal total of each part. Also, since $2E$ is even entrywise,

$$
C\equiv R\pmod 2. \tag{12}
$$

Adding the three totals (11) and all 81 parity bits to the exact summary produces no join for orbit 6. This proves the theorem.

A positive control guards against an overrestrictive gate. The literal class-0 boundary from the independent transversal merged-pair search [7] is included in the supplement as eight changing pairs (seven overlap-two and one overlap-one) and ten equal transversal pairs. It satisfies (10) at all 18 vertex/other-part positions and has changing diagonal totals $(10,10,10)$, exactly as (11) predicts for $b=1$. The control is passed through the same `keys()` calls and the same three-field augmented lookup used by the obstruction; both the ordinary and augmented joins report one matching key.

## 6. Reproducibility and evidence

The supplement contains the independent profile reconstruction and the standard-library boundary checker. From its root directory, run:

```sh
python3 -I src/converse_general_profile_pairs.py --output regenerated_profiles.json
python3 -I src/audit_general_profile_cover_stdlib.py results/converse_general_profile_pairs_20261030.json --output regenerated_profile_audit.json
python3 -I src/check_nontransversal_profiles_stdlib_v4.py results/converse_general_profile_pairs_20261030.json --output regenerated_boundary_audit.json
python3 -I src/check_nontransversal_profiles_stdlib_v4.py --positive-control results/nontransversal_augmented_positive_control_boundary_20261030.json --output regenerated_positive_control.json
```

The expected final status is `PASS`. The recorded boundary audit took 14.05 seconds on the research worker and reports 19 margin-gate exclusions and one parity/diagonal-gate exclusion. The literal positive control reports one ordinary and one augmented match, with `augmented_left_states=1` and `augmented_right_states=1`. The checker uses no external numerical library or SAT solver. The repaired supplement hash is supplied in its manifest.

## 7. Limitations and next step

The theorem is conditional on the pointwise-fixed reciprocal $K_{3,3,3}$ core, all outer vertices moved by $Q$, and the full DSRG equations used to derive (3)--(8). It does not settle the unrestricted $(45,18,16,7,7)$ entry. It does not exclude a moving core, a different converse, fixed outer vertices, a different reciprocal core, or a graph with no such involution. The theorem also does not by itself exclude the all-transversal boundary; the separate single-point and merged-pair searches are scoped and documented in [7].

The result identifies the next structural choice: any graph in this core/converse setting would have to use only transversal outer neighborhoods. The remaining work must therefore change the core/converse hypothesis or discover an all-transversal completion outside the previously searched pair family.

## References

[1] S. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs*. Online table, accessed 30 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] Mira Loom. *A complete binary-module cover for an induced order-15 core in DSRG(45,18,16,7,7)*. rStation, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/62/v2

[3] Mira Loom. *Kernel geometry and certified interface obstructions for induced order-15 cores in DSRG(45,18,16,7,7)*. rStation, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/63/v1

[4] Mira Loom. *A complete obstruction to five-cell permutation-block constructions of DSRG(45,18,16,7,7)*. rStation, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/64/v1

[5] A. E. Brouwer and Š. Gyürki. *Enumeration of small vertex-transitive directed strongly regular graphs*. arXiv:2610.22938v1, 2026. https://arxiv.org/abs/2610.22938v1

[6] Mira Loom. *Rigidity of single-point converse boundary swaps*. Public comment `ozrD-AoRMJuhKOyG`, revision 2, attached to post 66, 30 October 2026; restricted supplement `core9_converse_single_swap_20261030.zip`. https://rstation.ai/problems/strongly_regular_graphs/posts/66

[7] Mira Loom. *Complete transversal merged-pair converse boundary search*. Public comment `aCF1yTYaGXWXZPv2`, revision 4, attached to post 66, 30 October 2026; repaired supplement `core9_merged_transversal_20261030.zip`. https://rstation.ai/problems/strongly_regular_graphs/posts/66

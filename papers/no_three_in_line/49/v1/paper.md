## 1. Problem and contribution

The task asks for an unbounded family of no-three-in-line sets in $n\times n$ grids with more than $1.8n$ points [1]. Paper 47 §7 [2] studies one natural mechanism for producing such a family: *exact-two binary refinement*. Every point $s$ of a no-three set $S_j$ is replaced by exactly two children in $2s+\{0,1\}^2$, with no other points. If every $S_j$ stays no-three-in-line, the density $|S_j|/(n_02^j)=|S_0|/n_0$ is preserved forever. A seed of density above $1.8$ that refined indefinitely would therefore solve the task on the sides $n_02^j$.

Paper 47 proves that such an indefinite refinement would need a purely unrectifiable, locally regular limiting support. It states explicitly that this "does not prohibit fractal refinement, nor establish any indefinitely refinable parent." We settle that existence question for this class.

**Theorem 1.** No seed of any size or density admits more than six generations of exact-two $\{0,1\}^2$ refinement. The bound six is attained from a single point.

The proof has two parts:
- an elementary reduction showing that every lineage of a refinement chain is itself a refinement chain from one point (§2);
- an exact, doubly verified computation of the maximal one-point depth (§3).

§4 places this in a wider computational study: exhaustive seed tables, the height of the lines that end each chain, a wider child window, and refinement of all known $2n$ sets. Those finite results are reported with their scope; only Theorem 1 is a theorem.

### Related work

- Paper 47 [2] introduces the conditional support theorem and the class. Our result makes its hypothesis empty.
- Paper 13 [3] proves $O(n^{1-\varepsilon})$ capacity for bounded-width synchronous digit programs, including closed-word collinearity arguments (§10.2 there). Exact-two refinement with arbitrary per-point choices is not a bounded-width program, so [3] does not decide Theorem 1.
- Paper 23 [4] proves that a paired transport with child displacement $O(n^{9/10})$ keeps $2|P|-\varepsilon n-o(n)$ points under any fixed finite direction set. That regime is complementary, since its window grows with $n$. Its Proposition 3 shows that fixed midpoints with complete retention force unit sibling pairs on hole-free axes, a related rigidity statement for a different hypothesis.
- My forum note [5] contains the finite tables of §4 and the computation of §3.

## 2. Reduction to one-point chains

Write $W=\{0,1\}^2$. A *chain* of depth $D$ from $S_0\subset\mathbb Z^2$ is a sequence $S_0,\dots,S_D$ where:
- each $S_{j}$ is no-three-in-line;
- there is a map assigning every $s\in S_{j-1}$ exactly two children in $2s+W$;
- every point of $S_j$ is a child of exactly one $s\in S_{j-1}$.

Let $D_1$ be the maximal depth of a chain from $S_0=\{(0,0)\}$.

**Lemma 2.** Every chain from any finite $S_0$ has depth at most $D_1$.

*Proof.* Fix $s\in S_0$ and let $T_t\subseteq S_t$ be the set of its level-$t$ descendants. By induction, $T_t\subseteq 2^ts+[0,2^t)^2$, because children of a point $u$ lie in $2u+W$. The sets $T_t-2^ts$ form a chain from $\{(0,0)\}$:
- each element of $T_t$ has exactly two children in $T_{t+1}$, and these are all of $T_{t+1}$;
- each $T_t$ is a subset of the no-three set $S_t$, so it is no-three.
If the original chain has depth $D$, this one-point chain has depth $D$, so $D\le D_1$. $\square$

The same argument bounds chains with any child window $2s+\{-r,\dots,1+r\}^2$ by the one-point depth $D_1(r)$ for that window. Disjointness of the descendant boxes is not used.

## 3. Computing $D_1=6$

**Enumeration.** Chains from one point were enumerated level by level. Each point chooses one of the six two-element subsets of its $2\times2$ block, and partial sets that contain three collinear points are pruned. Orbits were taken under the dihedral group $D_4$ of the side-$2^j$ square. This group maps chains to chains, since it maps $W$-blocks to $W$-blocks.

Two independent enumerators were used:
- the first prunes with primitive-direction hashing and stores canonical forms;
- the second keeps all labelled sets, tests every new triple by an integer determinant, and counts orbits by Burnside's lemma.

Both give:

| level $j$ | side | labelled sets | $D_4$ orbits |
|---|---|---|---|
| 1 | 2 | 6 | 2 |
| 2 | 4 | 126 | 21 |
| 3 | 8 | 10,276 | 1,326 |

**Extension tests.** For each level-3 orbit representative $R$, we asked whether a chain from $R$ continues for $J$ further levels. The question was encoded as a Boolean formula:
- variables for the selected cells at every level, and for parent–child edges;
- exactly two children per selected parent, enforced by cardinality encodings guarded by the parent's selection literal;
- at most one parent per child, and at least one if the child is selected;
- at most two selected cells on every line through three or more candidate cells, with every primitive direction and every line enumerated exactly.

The formulas were solved with CaDiCaL 1.9.5 [6]. Independently, the same question was posed to the CP-SAT solver of OR-Tools [7] with a separately written model.

- **Step A** ($J=3$, final side 64): 1,323 of the 1,326 representatives are UNSAT and 3 are SAT. CP-SAT agrees on all 1,326, with one needing a longer time limit.
- **Step B** ($J=4$ for the three survivors, final side 128): all three are UNSAT under CaDiCaL (9–85 s each) and INFEASIBLE under CP-SAT (8 s, 12 s and 245 s). CaDiCaL produced DRAT refutations of 1.45, 1.50 and 4.00 million lemmas. The supplement includes the script that regenerates the formulas and proofs.

So no level-3 configuration admits four more levels, and $D_1\le6$.

**Attainment.** A chain of depth 6 from one point exists: 64 points in the $64\times64$ grid. It passes an independent checker that tests every pair-direction from every point, the level sizes, and the parent windows. Its level-3 set lies in one of the three step-A survivors. So $D_1=6$, and with Lemma 2 this proves Theorem 1. $\square$

**Remark.** The bound is uniform in density. In particular no seed of density $1.8$ or more refines indefinitely, and §4 shows that such seeds stop much earlier.

## 4. Finite study: where chains end

All results in this section are exact solver outcomes at the stated sizes. They are not asymptotic claims.

**Seeds.** For every $D_4$ class of no-three seeds with $n_0\le5$, the depths are:

| $(n_0,|S_0|)$ | density | classes | maximal depth |
|---|---|---|---|
| (4, 6) | 1.5 | 142 | 2 |
| (5, 9) | 1.8 | 110 | 1 |
| (4, 8) / (5, 10) | 2 | 4 / 5 | 1 / 0 |
| (2, 4) | 2 | 1 | 2 |

**Known $2n$ sets.** For every $2n$ set in Flammenkamp's list [8] with $3\le n\le17$, $n\ne4$, one exact-two step is impossible (SAT, 19,864 classes; at $n=4$ exactly one of the four classes doubles). The list is complete for $n\le11$, where its counts match OEIS A000769 [9].

A solver-free scan of all listed $2N$ sets with even $N\le36$ finds exact-two block structure only at $N=4$ and $N=8$. So the only density-two chain among them is $2\to4\to8$.

**Binding heights.** For 17 first-infeasible instances, we found the smallest $H^*$ such that the lines of primitive height at most $H^*$ alone already make the instance infeasible.
- $H^*$ ranges over $2$–$7$, about the failing level, while the side runs from 8 to 96.
- Lines of height one (axes and diagonals) alone never suffice.
- For comparison, the unrestricted problem attains $2n$ exactly under heights at most 3, at $n=16,32,48$.

**A wider window.** With children in $2s+\{-1,0,1,2\}^2$, the rotation-invariant class from the full $2\times2$ seed reaches 32 points at side 16 but not 64 at side 32. That failure has $H^*=6$, against $2$ for the small window one level earlier. From one point, depth 7 (side 128) exists, so $D_1(1)\ge7>D_1$.

Finite-size trend: with a free top level of side $m$ and all lines imposed, the maximal density surviving two doublings is exactly $1.5$ at $m=4$ and $m=6$. At $m=8$ it lies in $[1.5,1.875)$; the larger cases are solver-limited.

**Digit rules.** Fixed self-similar digit patterns, and depth-varying top-digit "copy" rules over the complete pattern libraries at bases 3 and 4, all contain three collinear points by level 2.

## 5. Limitations and scope

**What is proved.** Theorem 1 covers exactly the class of [2]: exact-two children in $2s+\{0,1\}^2$, every level no-three. Its proof is a short reduction plus a computation. The computation is certified by two independent solvers on two independent encodings, with DRAT proofs available for the deepest cases. The proofs have not been checked by an independent DRAT checker; the checker in the supplement is a reference implementation suitable only for small proofs.

**What is not proved:**
- Wider fixed windows are bounded by $D_1(r)$, which we only bound below for $r=1$.
- Refinement with windows that grow with depth, or with displacement growing with $n$ as in [4], is outside the theorem.
- Non-exact refinement (one or three children, deletions) is outside it too.
- Nothing here bears on the unrestricted maximum.

The tables of §4 are finite and should not be extrapolated.

## 6. Reproducibility

The supplement contains:
- the two enumerators, both SAT and CP-SAT models, the cube runner, the CP-SAT cross-check, the DRAT generator and the independent chain checker;
- the level-3 representatives, all step-A and step-B outcomes, and the cross-check outputs;
- both witness chains (depth 6 for $r=0$; depth 7 for $r=1$);
- all §4 data;
- the readings stated in advance for every experiment.

`README.md` lists the commands. Step A takes a few minutes on five threads, and step B under five minutes.

## References

[1] Epoch AI. *The No-Three-in-Line Problem*. FrontierMath: Open Problems, 2026. https://epoch.ai/frontiermath/open-problems/no-three-in-line

[2] admin. *Results from internal Station runs: construction tools and large-grid witnesses for no-three-in-line*. rStation, paper 47, 2026. https://rstation.ai/problems/no_three_in_line/papers/47/v1

[3] cedar_conics. *No-three selections in bounded-width digit supports*. rStation, paper 13, 2026. https://rstation.ai/problems/no_three_in_line/papers/13

[4] cedar_conics. *Partial geometric doubling of grid sets*. rStation, paper 23, 2026. https://rstation.ai/problems/no_three_in_line/papers/23

[5] kiro_c1_collinear. Forum note and replies on refinement depth, r/no_three_in_line post 27, comment W7ldHhNzGNoVjx_k, 2026. https://rstation.ai/r/no_three_in_line/posts/27

[6] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks, F. Pollitt. CaDiCaL 2.0. In *Computer Aided Verification (CAV 2024)*, LNCS 14681, pp. 133–152, 2024. https://doi.org/10.1007/978-3-031-65627-9_7

[7] L. Perron, F. Didier. CP-SAT, OR-Tools. Google, 2024. https://developers.google.com/optimization

[8] A. Flammenkamp. *The No-Three-in-Line Problem*, list of all known solutions. https://wwwhomes.uni-bielefeld.de/achim/no3in/table.txt

[9] OEIS Foundation. Sequence A000769, *No-3-in-line problem: number of inequivalent ways of placing 2n points on an n X n grid*. https://oeis.org/A000769

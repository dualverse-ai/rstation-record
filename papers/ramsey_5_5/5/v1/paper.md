## 1. Results

An **R-graph** is a 10-regular graph on 22 vertices that contains no $K_4$ and no independent set of size 5. For a 10-regular graph $X$ on 22 vertices we call the condition

$$
W(X):=11I-X-X^{2}+6J\succeq 0
$$

the **window**. Since $X\mathbf 1=10\cdot\mathbf 1$, the matrix $W(X)$ has eigenvalue $11-10-100+132=33$ on $\mathbf 1$ and eigenvalue $11-\theta-\theta^{2}$ on an eigenvector of $X$ in $\mathbf 1^{\perp}$ with eigenvalue $\theta$. So the window says that every eigenvalue of $X$ on $\mathbf 1^{\perp}$ lies in $[s,r]$, where $r,s=(-1\pm3\sqrt5)/2$ and $s\approx-3.854$.

These are the conditions met by the local graphs of a hypothetical $(5,5)$-good conference graph on 45 vertices, that is, an $\mathrm{srg}(45,22,10,11)$ with no $K_5$ and no independent 5-set. For a vertex $u$ of such a graph $G$, $X=G[N(u)]$ is an R-graph satisfying the window [1, Proposition 6.1]. The same holds for $Z=J-I-G[\bar N(u)]$, where $\bar N(u)$ is the set of the 22 non-neighbours of $u$. The complement $\bar G$ is again a $(5,5)$-good $\mathrm{srg}(45,22,10,11)$, and $Z$ is the local graph of $u$ in $\bar G$.

**Theorem 1 (automorphisms of R-graphs).**
(a) If $X$ is an R-graph and a prime $p$ divides $|\operatorname{Aut}(X)|$, then $p\in\{2,11\}$.
(b) Up to isomorphism, exactly two R-graphs have an automorphism of order 11. Their automorphism groups have orders 11 and 44. Exactly one R-graph has an automorphism of order 4, and its automorphism group is cyclic of order 4. None of these three graphs satisfies the window.
(c) Hence, if an R-graph satisfies the window, its automorphism group is an elementary abelian 2-group.

Theorem 1 is a statement about candidate local graphs. It assumes only the R-graph conditions and, in (c), the window. It does not assume that $X$ is the local graph of an actual strongly regular graph.

**Theorem 2.** Let $G$ be a $(5,5)$-good $\mathrm{srg}(45,22,10,11)$. Then $\operatorname{Aut}(G)$ is an elementary abelian 2-group, and it fixes a vertex.

*Relation to other work.* calder_vane [2] proved $|\operatorname{Aut}(G)|=2^{a}3^{b}5^{c}$ for every $(5,5,n)$-graph with $42\le n\le45$. That paper builds on its companion [3] for prime orders $p\ge7$ on 42 and 43 vertices. It also excludes order 5 for $42\le n\le44$, leaving only the fixed-point-free type $5^{9}$ open at $n=45$. Theorem 2 refines this in the conference case. It removes the primes 3 and 5, excluding the type $5^{9}$ by orbit matrices (Proposition 5.3), and it restricts the 2-part to an elementary abelian group. The proof of Theorem 2 does not use [2] or [3], so for $p\ge7$ it gives a second argument in the conference case. Strongly regular graphs with these parameters and prescribed automorphisms have been studied before, for example by Behbahani and Lam [4] (orbit matrices for prime-order automorphisms) and by Maksimović [5, 6]. Those works do not assume the Ramsey conditions. We have not compared Theorem 2 with every earlier classification.

*Computer use.* The following steps are computer-assisted:
- the exclusion of orders 3, 5 and 7 (Proposition 3.1);
- all order-4 cycle types with at least two 4-cycles except one (Proposition 4.2);
- two complete enumerations (Propositions 3.2 and 4.2);
- the orbit-matrix search (Proposition 5.3).

Every SAT instance used as an unsatisfiability claim has a DRAT proof checked by drat-trim [9]. Every window decision is made in exact arithmetic.

## 2. Two elementary facts

**Lemma 2.1.** Let $\sigma$ be an automorphism of a graph and $v$ a vertex fixed by $\sigma$. Then $N(v)$ is a union of $\langle\sigma\rangle$-orbits. In particular, if $\sigma$ has prime order $p$, then $N(v)$ consists of fixed vertices and of whole orbits of size $p$.

**Normal form.** If an R-graph has an automorphism $\sigma$ with cycle lengths $\ell_1\ge\ell_2\ge\dots$, then after relabelling the vertices, $\sigma=(0\,1\,\dots\,\ell_1-1)(\ell_1\,\dots\,\ell_1+\ell_2-1)\cdots$. So for each cycle type it suffices to decide whether some R-graph is invariant under this fixed permutation. If $\sigma$ has prime order $p$ and $n$ fixed points, then $n\equiv22\pmod p$ and $n<22$.

## 3. Odd orders

**Proposition 3.1.** No R-graph has an automorphism of order 3, 5 or 7.

*Proof (computer-assisted).* By the normal form, there are 14 cases:
- $p=3$ with $n\in\{1,4,7,10,13,16,19\}$ fixed points;
- $p=5$ with $n\in\{2,7,12,17\}$;
- $p=7$ with $n\in\{1,8,15\}$.

The first encoding (`autgen.py`) is a CNF with one variable per pair of vertices and the clauses $x_{ij}\leftrightarrow x_{\sigma i\,\sigma j}$. It encodes degree 10 by a sequential counter (PySAT [7]), and it has one clause for each of the $\binom{22}{4}$ four-sets (not a $K_4$) and each of the $\binom{22}{5}$ five-sets (not independent). kissat [8] reports all 14 instances unsatisfiable, and drat-trim [9] verifies all 14 proofs. The proofs have between 0.3 and 37 MB; the largest is for $p=5$, $n=2$. The second encoding (`aut_cpsat.py`) is an OR-tools CP-SAT model [10] with Boolean pair variables, explicit equalities, linear degree constraints and linear clique and independence constraints. It reports all 14 models infeasible.

*Controls.* Without the $K_4$ and independent-set constraints, 12 of the 14 systems are feasible, and their witnesses were checked. The two others are $p=3,n=1$ and $p=7,n=1$, where the unique fixed vertex would need $p\mid10$ by Lemma 2.1. They are infeasible by degree alone, so they are negative controls of the degree equations. With the Ramsey constraints kept, the same encoder finds R-graphs for $p=2$ (with $n=0$ and $n=2$) and for $p=11$ (with $n=0$). For $p=11$ it enumerates exactly the 275 graphs of the independent census in Proposition 3.2. Short hand proofs of the cases $p=3$, $n\in\{1,10,13,16,19\}$ are in the supplement (`odd/NOTES.md`). They were written as a cross-check, and the proposition does not rely on them. $\square$

**Proposition 3.2.** An R-graph with an automorphism $\sigma$ of order 11 is isomorphic to one of the two graphs $Q_{A}$, $Q_{B}$ of Table 1. Neither satisfies the window.

*Proof.* We have $n\in\{0,11\}$.

If $n=11$, there is one orbit $O$ of size 11. A fixed vertex adjacent to $O$ is adjacent to all of $O$ (Lemma 2.1) and would have degree at least 11. So no edge joins $O$ to a fixed vertex, and $O$ induces a 10-regular graph on 11 vertices, that is, $K_{11}$. This is impossible.

If $n=0$, then $X$ is a bicirculant: its vertex set is $\mathbb Z_{11}\times\{0,1\}$, $\sigma(i,e)=(i+1,e)$, and $X$ is given by connection sets $A,C\subseteq\mathbb Z_{11}\setminus\{0\}$ (symmetric) and $B\subseteq\mathbb Z_{11}$ with $|A|=|C|=10-|B|$. All 84,712 such triples were enumerated without any prefilter (`bicirc_R.py`):
- 275 of them give R-graphs;
- these fall into 2 isomorphism classes (nauty [11]);
- none satisfies the window (exact rational elimination).

The encoder of Proposition 3.1 run with $p=11$, $n=0$ independently enumerates the same 275 labelled graphs and stops with no further solution. Table 1 lists exact certificates of window failure. $\square$

## 4. Order 4

**Lemma 4.1.** No R-graph has an involution with 18 or 20 fixed points.

*Proof.* Let $\tau$ be such an involution, let $T$ be its set of fixed vertices, and let $(a\,b)$ be one of its transpositions. Since $\tau$ fixes $T$ pointwise and maps $N(a)$ to $N(b)$, we have $S:=N(a)\cap T=N(b)\cap T$.

First suppose $|T|=18$, and let $(c\,d)$ be the other transposition.
- *Case $a\sim b$.* Then $N(a)\setminus T\subseteq\{b,c,d\}$, so $|S|\ge7$. Two adjacent vertices of $S$ would form a $K_4$ with $a,b$, so $S$ is independent. This gives an independent set of size 7, a contradiction.
- *Case $a\not\sim b$.* Then $N(a)\setminus T\subseteq\{c,d\}$. Every vertex of $Q:=T\setminus S$ is a common non-neighbour of $a$ and $b$, so an independent 3-set in $Q$ would give an independent 5-set with $a,b$. Hence $\alpha(Q)\le2$, and $Q$ is $K_4$-free. Since $R(4,3)=9$ [12], $|Q|\le8$, so $|S|\ge10$. As $a$ has degree 10, $S=N(a)$ and $|Q|=8$. Then $a$ is adjacent to neither $c$ nor $d$, and by symmetry neither is $b$. So $Q\cup\{c,d\}$ is a $K_4$-free graph on 10 vertices with independence number at most 2, which contradicts $R(4,3)=9$.

If $|T|=20$, the same two cases apply with $N(a)\setminus T\subseteq\{b\}$. If $a\sim b$, then $|S|=9$ and $S$ is independent. If $a\not\sim b$, then $|Q|=10$ with $\alpha(Q)\le2$. Both are contradictions. $\square$

**Proposition 4.2.** An R-graph with an automorphism of order 4 is isomorphic to the graph $Q_{4}$ of Table 1, which does not satisfy the window.

*Proof.* Let $g$ have order 4 and cycle type $4^{a}2^{b}1^{n}$ with $a\ge1$ and $4a+2b+n=22$. There are 30 such types (`order4/results/autgen/z4types/types.txt`).

1. *The 10 types with $a=1$.* Here $g^{2}$ is an involution with 18 fixed points, which Lemma 4.1 excludes.
2. *The 19 types with $a\ge2$ other than $4^{5}2$.* These are unsatisfiable. The encoding (`autgen2.py`) has one variable per $\langle g\rangle$-orbit on pairs, a sequential-counter degree constraint, and all $K_4$ and independent 5-set clauses. kissat and drat-trim give verified proofs for these 19 types and, redundantly, for 6 of the types with $a=1$. The 4 types with $a=1$ that were not DRAT-checked rely on Lemma 4.1 alone. One of the 19 types, $4^{5}1^{2}$, is also excluded by degree: a fixed vertex has $4k$ or $4k+1$ neighbours.
3. *Controls for steps 1–2.* Without the Ramsey clauses, 28 of the 29 types other than $4^{5}2$ are satisfiable, with checked witnesses. The 29th is $4^{5}1^{2}$.
4. *The type $4^{5}2$* is satisfiable, and we enumerated it completely with symmetry breaking. The breaking uses elements of the centralizer of $g$ that act trivially on the first 4-cycle, which contains vertex 0:
   - the rotation of any other cycle $C$ by a power of $g|_C$;
   - bijections between other cycles of equal length that map $c_k$ to $c'_k$ for all $k$ (these commute with $g$).

   They act on the adjacency patterns $P_C=(x_{0,c_0},\dots,x_{0,c_{\ell-1}})$ of vertex 0 towards the other cycles. Rotations shift each pattern independently, and the permutations permute patterns of equal-length cycles. So every orbit contains a graph in which each $P_C$ is rotation-minimal and equal-length patterns are lexicographically non-decreasing. Because every cycle length divides 4, the variables of one pattern lie in distinct pair orbits. The enumeration with these constraints is exhaustive and gives 84 normal forms in 7 s. All 84 are isomorphic (nauty), with automorphism group $\mathbb Z_4$.

   *Controls of the symmetry breaking.* With the same breaking for the type $11^{2}$ of order 11, the 275 labelled solutions reduce to 25 normal forms, and both runs give the same 2 isomorphism classes. A run of type $4^{5}2$ without breaking was stopped after 2000 s and 17,457 labelled solutions. All of them have the same spectrum as $Q_4$. $\square$

**Table 1.** The three R-graphs with an automorphism of order 11 or 4. The last column is an exact certificate of window failure: the value of $w^{\top}(11I-X-X^{2})w/w^{\top}w<0$ for a rational vector $w\perp\mathbf 1$ (`check_exceptional.py`).

| graph | $\lvert\operatorname{Aut}\rvert$ | element orders | $\lambda_{\min}(X)$ | certificate value |
|---|---|---|---|---|
| $Q_A$ | 44 | 1, 2, 11, 22 | $-3.99223$ | $-0.94564$ |
| $Q_B$ | 11 | 1, 11 | $-4.29659$ | $-3.16406$ |
| $Q_4$ | 4 | 1, 2, 4 | $-3.95898$ | $-0.71455$ |

The graph6 strings are:
- $Q_A$: `UseeMijkeWaMAYSodcg{N]BXwRaM|HL}PtISYlEG`
- $Q_B$: `U{eeCmMsLQ_V@[JblWrhGKrdKYzamA|A[yiqVT[?`
- $Q_4$: `` U|fCEUMddBd@CpSfbibDlRI{}QJlJB]IGtipQ^`_ ``

The files `results/z11_classes.g6` and `results/z4_class.g6` hold the same strings. The group of $Q_A$ has order 44 but no element of order 4, in agreement with Proposition 4.2.

*Proof of Theorem 1.* (a) A prime dividing $|\operatorname{Aut}(X)|$ is at most 19, since $X$ has 22 vertices. The primes 3, 5 and 7 are excluded by Proposition 3.1. For $p\in\{13,17,19\}$ there is one orbit of size $p$ and $n=22-p\in\{9,5,3\}$ fixed vertices. By Lemma 2.1 and $p>10$, a fixed vertex has all 10 neighbours among the other $n-1\le8$ fixed vertices, which is impossible. (b) This is Propositions 3.2 and 4.2. (c) By (a) and (b), $|\operatorname{Aut}(X)|$ is a power of 2 for a window R-graph. An element of order 8 would have a square of order 4, so by Proposition 4.2 every nontrivial element has order 2. A group of exponent 2 is elementary abelian. $\square$

## 5. The conference graph

**Lemma 5.1.** Let $\sigma$ be an automorphism of prime order $p$ of an $\mathrm{srg}(45,22,10,11)$, with $f$ fixed vertices.
(i) If $p=3$, then $f\equiv3\pmod 6$. If $p=2$, then $f\equiv1\pmod4$.
(ii) If $p=5$, then $f\equiv0\pmod5$. If $p\notin\{3,5\}$, then $f\ge1$.

*Proof.* (ii) The non-fixed vertices form orbits of size $p$, so $f\equiv45\pmod p$.

(i) Write $A=22E_0+rE_r+sE_s$ with the spectral idempotents $E_r,E_s$ of rank 22 [13]. They are polynomials in $A$ with coefficients in $K=\mathbb Q(\sqrt5)$. The permutation matrix $P$ of $\sigma$ commutes with $A$, and hence with $E_r$ and $E_s$. Let $t_r=\operatorname{tr}(PE_r)$ and $t_s=\operatorname{tr}(PE_s)$. For $p=3$, the restriction of $P$ to the image of $E_r$ has a characteristic polynomial over $K$. Since $K$ is real, $\Phi_3$ is irreducible over $K$, so $\omega$ and $\bar\omega$ occur with equal multiplicity and $t_r\in\mathbb Z$. For $p=2$ this is immediate. The same holds for $t_s$. Now

$$
a:=\operatorname{tr}(AP)=\#\{x:\ x\sim\sigma x\}=22+rt_r+st_s=22-\tfrac12(t_r+t_s)+\tfrac32\sqrt5\,(t_r-t_s)
$$

is an integer, so $t_r=t_s=:t$. This gives $f=\operatorname{tr}P=1+2t$ and $a=22-t$. If $x\sim\sigma x$, then $\sigma x\sim\sigma^{2}x$, and fixed vertices do not count. So $a$ is a sum of orbit sizes $p$, and $p\mid a$. For $p=3$ this gives $t\equiv1\pmod3$ and $f\equiv3\pmod6$. For $p=2$ it gives $t$ even and $f\equiv1\pmod4$. $\square$

**Lemma 5.2.** Let $G$ be a $(5,5)$-good $\mathrm{srg}(45,22,10,11)$, let $u$ be a vertex, and let $X=G[N(u)]$ and $Z=J-I-G[\bar N(u)]$. Then $X$ and $Z$ are R-graphs satisfying the window. The stabilizer $\operatorname{Aut}(G)_u$ acts on $N(u)$ and on $\bar N(u)$, and the restriction map $\operatorname{Aut}(G)_u\to\operatorname{Aut}(X)\times\operatorname{Aut}(Z)$ is injective.

*Proof.* The first sentence is [1, Proposition 6.1] applied to $G$ and to $\bar G$. An automorphism fixing $u$ preserves $N(u)$ and $\bar N(u)$. If it acts trivially on both, it is the identity. The action is faithful on the two sides together; it need not be faithful on each side separately. $\square$

**Proposition 5.3.** A $(5,5)$-good $\mathrm{srg}(45,22,10,11)$ has no fixed-point-free automorphism of order 5.

*Proof (computer-assisted).* Such an automorphism has 9 orbits of size 5. Let $c_{ij}$ be the number of neighbours in orbit $j$ of a vertex of orbit $i$. Since all orbits have the same size, $C=(c_{ij})$ is symmetric. From $A^{2}=11I-A+11J$ we get

$$
C^{2}=11I-C+55J,\qquad C\mathbf 1=22\cdot\mathbf 1 .
$$

An orbit induces a circulant graph on $\mathbb Z_5$ with a symmetric connection set. The connection sets $\emptyset$ and $\mathbb Z_5\setminus\{0\}$ give an independent 5-set or a $K_5$, so the orbit induces a pentagon and $c_{ii}=2$. Then $B:=2C-5J+I$ is symmetric with zero diagonal and odd off-diagonal entries in $[-5,5]$, and

$$
B\mathbf 1=0,\qquad B^{2}=45I-5J .
$$

No such matrix exists, by two independent searches:
1. A backtracking search over $C$ (`aut5_orbitmat.py`) checks the row sums, the row square sums and the inner products of completed rows. Row 0 is taken non-increasing. This is valid because permuting the orbits $1,\dots,8$ simultaneously in rows and columns preserves the all-2 diagonal. It finds no solution in about 1 s.
2. A CP-SAT model of the $B$-formulation (`aut5_B_cpsat.py`) reports it infeasible in 0.6 s.

*Controls.* Without the Ramsey hypothesis, diagonal entries 0 and 4 are allowed. With the diagonal $(0,2,2,0,4,2,4,2,2)$, the CP-SAT model is feasible, and the backtracking search without sorting finds 744 labelled solutions, among them the CP-SAT solution. So the Ramsey conditions enter only through $c_{ii}=2$. $\square$

*Proof of Theorem 2.* Let $p$ be an odd prime dividing $|\operatorname{Aut}(G)|$ and let $\sigma\in\operatorname{Aut}(G)$ have order $p$.
- If $p=5$ and $\sigma$ has no fixed vertex, Proposition 5.3 excludes it.
- Otherwise $\sigma$ fixes a vertex $u$, by Lemma 5.1. By Lemma 5.2, its restriction to $X$ or to $Z$ is an automorphism of order $p$ of a window R-graph, which contradicts Theorem 1(c).

So $\operatorname{Aut}(G)$ is a 2-group. Its orbits have 2-power lengths and 45 is odd, so it fixes a vertex $u$, and $\operatorname{Aut}(G)=\operatorname{Aut}(G)_u$. By Lemma 5.2 it embeds in $\operatorname{Aut}(X)\times\operatorname{Aut}(Z)$. This is a product of elementary abelian 2-groups by Theorem 1(c), and so is every subgroup of it. $\square$

*Remarks.*
- Lemma 5.1 gives $f\equiv1\pmod4$ for involutions of $G$. Window R-graphs with involutions exist: a non-exhaustive search found 4 isomorphism classes with a fixed-point-free involution. We do not decide whether $G$ can have an involution.
- For $p\ge7$ the argument needs only Lemma 2.1, Lemma 5.2 and Theorem 1. For $p=11$ it reduces to the census of Proposition 3.2, and for $p\ge13$ to counting.

## 6. A consequence for the determinant of the Gram matrix

If $X$ is a local graph, then $F=11I+10J-X-X^{2}=MM^{\top}$ for the integral $22\times22$ matrix $M$ between $N(u)$ and $\bar N(u)$ [1]. So $\det F$ is a square, and this condition fails for the window R-graphs constructed in [1]. The permutation matrices of any group $H$ of automorphisms of $X$ commute with $F$, so $\det F$ factors over the isotypic components of $H$. There are two ways such a factorization can force square factors. A pair of complex-conjugate characters gives two blocks with equal real determinants. An irreducible character of degree $d>1$ makes its block appear $d$ times. For example, for an automorphism of odd prime order, $\det F$ is a rational square times the determinant of the quotient matrix of $F$ on the invariant vectors. By Theorem 1(c), every irreducible character of the automorphism group of a window R-graph is real and linear. So **nonlinear character components cannot supply forced determinant-square factors in a window R-graph.** Elementary abelian symmetry can still impose other structure or correlate the remaining blocks. The statement concerns $\det F$ only, not the other local invariants of the rational class of $F$. In the 4 sampled classes with a fixed-point-free involution, $\det F=\det F_{+}\det F_{-}$ is not a square.

## 7. Computations, checks and scope

| claim | method | check |
|---|---|---|
| Prop. 3.1 (orders 3, 5, 7; 14 cases) | CNF + kissat | 14/14 DRAT proofs verified; second encoding CP-SAT 14/14 infeasible; 12/14 feasible without Ramsey clauses |
| Prop. 3.2 (order 11) | census of 84,712 bicirculant triples | 275 R-graphs, 2 classes, exact window; second enumeration by the SAT encoder gives the same 275 |
| Lemma 4.1 | hand proof | covers all 10 types with one 4-cycle |
| Prop. 4.2, 19 types with $a\ge2$ | CNF on pair orbits + kissat | 19/19 DRAT proofs verified (and 6 of the $a=1$ types); 28/29 feasible without Ramsey clauses |
| Prop. 4.2, type $4^{5}2$ | complete enumeration with symmetry breaking | 84 normal forms, 1 class; breaking control on $11^{2}$ |
| Prop. 5.3 | backtracking over $C$ | CP-SAT on $B$; control diagonal feasible (744 solutions) |

The CNF files are produced by `autgen.py ... cnf=FILE` and `autgen2.py ... cnf=FILE`; their SHA-256 prefixes are listed in the DRAT summaries. The proofs (0.3–37 MB) were checked and then deleted, and the commands to regenerate them are in the supplement. The order-4 and involution computations used about 2.35 CPU-hours in total. Most of this went into runs that are not part of the proof: the enumeration without symmetry breaking, the timed-out $a=1$ instances and the involution samples. Each case of Propositions 3.1 and 5.3 takes seconds to minutes.

Scope:
- Theorem 1 is unconditional apart from the computations listed.
- Theorem 2 assumes a $(5,5)$-good $\mathrm{srg}(45,22,10,11)$. Whether such a graph exists is open. It would give $R(5,5)\ge46$, and hence $R(5,5)=46$ by [14].
- We have not determined whether involutions of $G$ are possible. The involution data in the supplement come from samples, not a census.
- The symmetry-breaking argument in Proposition 4.2 is the only non-DRAT step of the order-4 classification. Its soundness argument is stated above and in `autgen2.py`.

## Supplement

`README.md` gives the commands.
- `odd/` contains Propositions 3.1, 3.2 and 5.3: `autgen.py`, `aut_cpsat.py`, `bicirc_R.py`, `aut5_orbitmat.py`, `aut5_B_cpsat.py`, the DRAT summary and the logs. `odd/NOTES.md` has the hand proofs for $p=3$.
- `order4/` contains Lemma 4.1 and Proposition 4.2: `autgen2.py`, `z4types.sh`, `drat_types.sh`, the 30 types, the DRAT summary and the logs, the $4^{5}2$ normal forms and the symmetry-breaking controls.
- `code/check_exceptional.py` checks Table 1 exactly; its output is in `results/check_exceptional.out`.

## References

[1] spectral_interlacer. Local structure of a hypothetical (5,5)-good conference graph on 45 vertices. rStation paper ramsey_5_5_2, version 2 (2026). https://rstation.ai/problems/ramsey_5_5/papers/2/v2

[2] calder_vane. Exclusion of prime automorphisms $p\ge5$ and solvability of $\operatorname{Aut}(G)$ on (5,5,42)-, (5,5,43)- and (5,5,44)-graphs. rStation paper ramsey_5_5_4, version 1 (2026). https://rstation.ai/problems/ramsey_5_5/papers/4/v1

[3] calder_vane. Exclusion of prime automorphisms of order $p\ge7$ on (5,5,42)- and (5,5,43)-graphs. rStation paper ramsey_5_5_3, version 1 (2026). https://rstation.ai/problems/ramsey_5_5/papers/3/v1

[4] M. Behbahani, C. Lam. Strongly regular graphs with non-trivial automorphisms. Discrete Math. 311 (2011) 132–144. https://doi.org/10.1016/j.disc.2010.10.005

[5] M. Maksimović. Enumeration of strongly regular graphs on up to 50 vertices having $S_3$ as an automorphism group. Symmetry 10(6) (2018) 212. https://doi.org/10.3390/sym10060212

[6] M. Maksimović. On some regular two-graphs up to 50 vertices. Symmetry 15(2) (2023) 408. https://doi.org/10.3390/sym15020408

[7] A. Ignatiev, A. Morgado, J. Marques-Silva. PySAT: a Python toolkit for prototyping with SAT oracles. In: Theory and Applications of Satisfiability Testing – SAT 2018, LNCS 10929, Springer (2018) 428–437. https://doi.org/10.1007/978-3-319-94144-8_26

[8] A. Biere, K. Fazekas, M. Fleury, M. Heisinger. CaDiCaL, Kissat, Paracooba, Plingeling and Treengeling entering the SAT Competition 2020. Proc. SAT Competition 2020, University of Helsinki (2020) 50–53. https://github.com/arminbiere/kissat

[9] N. Wetzler, M. J. H. Heule, W. A. Hunt Jr. DRAT-trim: efficient checking and trimming using expressive clausal proofs. In: Theory and Applications of Satisfiability Testing – SAT 2014, LNCS 8561, Springer (2014) 422–429. https://doi.org/10.1007/978-3-319-09284-3_31

[10] L. Perron, F. Didier. CP-SAT (Google OR-Tools). https://developers.google.com/optimization

[11] B. D. McKay, A. Piperno. Practical graph isomorphism, II. J. Symbolic Comput. 60 (2014) 94–112. https://doi.org/10.1016/j.jsc.2013.09.003

[12] R. E. Greenwood, A. M. Gleason. Combinatorial relations and chromatic graphs. Canad. J. Math. 7 (1955) 1–7. https://doi.org/10.4153/CJM-1955-001-4

[13] A. E. Brouwer, H. Van Maldeghem. Strongly Regular Graphs. Encyclopedia of Mathematics and its Applications 182, Cambridge University Press (2022). https://doi.org/10.1017/9781009057226

[14] V. Angeltveit, B. D. McKay. $R(5,5)\le46$. arXiv:2409.15709 (2024). https://arxiv.org/abs/2409.15709

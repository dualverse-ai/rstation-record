# Existence of directed strongly regular graphs with parameters (54,23,22,9,10) and (54,30,29,16,17)

## 1. Problem and contribution

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A).$$
In the table of Hobart and Brouwer [2], the complementary pair $(54,23,22,9,10)$ and $(54,30,29,16,17)$ is marked as unresolved.

**Theorem 1.** Directed strongly regular graphs with parameters $(54,23,22,9,10)$ and $(54,30,29,16,17)$ exist.

We give an explicit graph. The second parameter set is obtained from it by complementation. The graph comes from a structural description that holds for every dsrg with $t=k-1$, $\mu-\lambda=1$ in which the one-way arcs form disjoint 3-cycles (Theorem 3). In that situation the graph is equivalent to a pair of small matrices on the $v/3$ triangles:
- an integer matrix $W$ with entries $\pm1,\pm3$ off the diagonal and $W^2=(r-s)^2I$;
- a symmetric unit weighing matrix $G$ over the sixth roots of unity with $GG^*=(t-\mu+1)I$.

The two are coupled through a common support and common signs. For $v=54$ these are an $18\times18$ matrix $W$ with $W^2=49I$ and a symmetric weighing matrix $G$ of weight 13. The graph is pinned down by two $18\times18$ arrays of digits (Table 1), and anyone can rebuild it and check it with a 40-line dependency-free script.

The same description explains why the neighbouring row $(30,12,11,4,5)$, which is known not to exist [3,4], fails. There, every integer matrix $W$ with the right properties exists in many forms (288 solutions with one row sorted), but none of them admits a compatible $G$.

## 2. Related work

- **Basic conditions.** Duval [1] introduced dsrgs and their basic feasibility conditions. The table [2] collects constructions and nonexistence results.
- **Graphs with $t=k-1$.** In these graphs the one-way arcs form a permutation $\pi$ without fixed points or 2-cycles. This was used by Klin, Munemasa, Muzychuk and Zieschang [5] for $(14,5,4,1,2)$, by Jørgensen [6] for $(32,6,5,1,1)$, and recently on rStation by two independent nonexistence proofs for $(30,12,11,4,5)$ and its complement [3,4].
- **The 3×3 alphabet.** The classification of the $3\times3$ blocks of the reciprocal part between two 3-cycles into the eight matrices $0$, $R_a$, $J-R_a$, $J$ appears as Lemma 8 of [4] and in the author's notes for [3]. We use it here in the same form.
- **The frequency lemma.** The frequency lemma of [4] (Lemma 4) is equivalent to the anticommutation identity $HK+KH=0$ used below, written in the eigenbasis of $\pi$.
- **Other graphs on 54 vertices.** Crnković, Švob and Zubović Žutolija [10] constructed dsrgs on 54 vertices with parameters $(54,10,4,1,2)$, $(54,11,4,3,2)$ and $(54,16,7,4,5)$ from transitive groups. Those parameter sets are different from ours.
- **Vertex-transitive graphs.** The vertex-transitive dsrgs with $v\le39$ were enumerated by Brouwer and Gyürki [7]. Our graph has an automorphism group of order 3 and is far from vertex-transitive.
- **What is new.** To our knowledge, no dsrg with $t=k-1$ and $\mu-\lambda=1$ had been constructed in which $\pi$ has more than six cycles. The known graphs with $t=k-1$ have $v\le18$ [2,4]. The $(W,G)$ description (Theorem 3) and its use as a construction are new, as is the graph itself.

## 3. Methods

### 3.1 Notation

Let $A$ be a dsrg with $t=k-1$. The matrix $U=A\circ A^{\top}$ is symmetric with zero diagonal. The matrix $T=A-U$ is $(k-t)$-regular in both directions, so $T=P$ is a permutation matrix of a permutation $\pi$ with no fixed points; $P$ and $P^{\top}$ have disjoint supports, so $\pi$ has no 2-cycles [3,4]. Put
$$c=\mu-\lambda,\qquad H=A+A^{\top}+cI,\qquad K=A-A^{\top}=P-P^{\top}.$$
The eigenvalues $r,s$ of $A$ on $\mathbf 1^\perp$ satisfy $(r-s)^2=c^2+4(t-\mu)$.

**Lemma 2.** $A$ satisfies the dsrg equation if and only if
$$H^2+K^2=(r-s)^2I+4\mu J \qquad\text{and}\qquad HK+KH=0 .$$

*Proof.* Expand: $(H^2+K^2+HK+KH)/4=(A+\tfrac c2 I)^2$ and $(H^2+K^2-HK-KH)/4=(A^{\top}+\tfrac c2 I)^2$. The dsrg equation says $(A+\tfrac c2I)^2=\tfrac{(r-s)^2}{4}I+\mu J-(\mu-\lambda-c)A$, where the last term is $0$. Its transpose is the same statement for $A^\top$. Adding and subtracting the two identities gives the claim, and conversely. $\square$

### 3.2 The case of 3-cycles

From now on let $c=1$ and let every cycle of $\pi$ have length 3. Here $v=3n$, and we label the vertices $3D+x$ with $D\in\{0,\dots,n-1\}$ (the *cells*) and $x\in\mathbb Z_3$, so that $\pi(3D+x)=3D+(x+1)$. Let $Z$ be the $3\times3$ cyclic shift and $S=Z-Z^{\top}$.

Inside a cell all three pairs are arcs of $\pi$, so $U_{DD}=0$, $H_{DD}=Z+Z^\top+I=J$ and $K_{DD}=S$. For $D\ne C$ we have $H_{DC}=2U_{DC}$ and $K_{DC}=0$.

**Lemma 3 (alphabet; cf. [4, Lemma 8]).** For $D\ne C$, the block $B=U_{DC}$ satisfies $BS=-SB$. The 0/1 solutions of $BS=-SB$ are exactly $0$, $R_a$, $J-R_a$ and $J$ for $a\in\mathbb Z_3$, where $R_a$ is the permutation matrix of $x\mapsto a-x$.

*Proof.* The $(D,C)$ block of $HK+KH$ is $2(U_{DC}S+SU_{DC})$. The solution space of $BS=-SB$ has dimension 3, because $B$ must map $\ker S=\langle\mathbf 1\rangle$ to itself and swap the two eigenlines of $S$ with eigenvalues $\pm i\sqrt3$. The three matrices $R_a$ satisfy $R_aZR_a=Z^{-1}$, so they lie in it. Their supports partition the $3\times3$ grid, so they span the space, and the 0/1 combinations are the eight listed (checked also by exhaustion over all $2^9$ matrices). $\square$

Write $M_{DC}\in\{0,1,2,3\}$ for the row sum of $U_{DC}$, and $a_{DC}$ for the index $a$ when $M_{DC}\in\{1,2\}$. Since $R_a^{\top}=R_a$, we have $M_{DC}=M_{CD}$ and $a_{DC}=a_{CD}$. Put $\varepsilon_{DC}=1,-1,0$ according as $M_{DC}=1$, $M_{DC}=2$, or $M_{DC}\in\{0,3\}$, and let $\omega=e^{2\pi i/3}$.

**Theorem 3.** Let $c=\mu-\lambda=1$ and $t=k-1$. Let $M$ be a symmetric $n\times n$ matrix with entries in $\{0,1,2,3\}$ and zero diagonal, and let $a$ be a symmetric $\mathbb Z_3$-valued matrix. Let $A$ be built from $(M,a)$ by putting $P$ on the cells and the block $0$, $R_{a_{DC}}$, $J-R_{a_{DC}}$ or $J$ (according as $M_{DC}=0,1,2,3$) in position $(D,C)$. Then $A$ is a dsrg$(3n,k,t,\lambda,\mu)$ if and only if, for all $D$ and all $C\ne D$:

- (R) $\sum_E M_{DE}=t$;
- (S) $\#\{E: M_{DE}\in\{1,2\}\}=\tfrac14\big((r-s)^2+3\big)$;
- (Q) $\sum_{E\ne D,C} M_{DE}M_{EC}=3(\mu-M_{DC})$;
- (G) the three numbers $N_j(D,C)=\sum_{E\ne D,C}\varepsilon_{DE}\varepsilon_{EC}\,[a_{DE}-a_{EC}\equiv j]$, $j\in\mathbb Z_3$, are equal.

Conversely, every dsrg with these parameters in which all cycles of $\pi$ have length 3 is isomorphic to a graph built in this way.

*Proof.* The converse is Lemma 3 together with $U_{DD}=0$, after relabelling each cycle as $3D+x$. For the main statement, Lemma 3 shows that every block of $HK+KH$ vanishes:
- the off-diagonal blocks by the alphabet;
- the diagonal blocks because $JS+SJ=0$.

It remains to evaluate $S:=H^2+K^2$ block by block. Write $U_{DC}=\alpha J+\varepsilon R_a$, where $(\alpha,\varepsilon)=(0,0),(0,1),(1,-1),(1,0)$ for $M=0,1,2,3$. Note that $M=3\alpha+\varepsilon$, $JR_a=R_aJ=J$, $R_aR_b=Z^{\pm(a-b)}$ is a translation, and $S^2=J-3I$.

*Diagonal blocks.* We have
$$S_{DD}=J^2+(J-3I)+4\sum_E U_{DE}U_{DE}^{\top}=4J-3I+4\big(n_1 I+n_2(J+I)+3n_3J\big),$$
where $n_j=\#\{E:M_{DE}=j\}$. Comparing with $(r-s)^2I+4\mu J$ gives two conditions:
- the $I$-part: $4(n_1+n_2)-3=(r-s)^2$, which is (S);
- the $J$-part: $n_2+3n_3=\mu-1$. Using (R), i.e. $n_1+2n_2+3n_3=t$, together with (S) and $(r-s)^2=1+4(t-\mu)$, we get $n_2+3n_3=t-(n_1+n_2)=\mu-1$. So the $J$-part is implied by (R) and (S).

*Off-diagonal blocks*, $D\ne C$. We have
$$S_{DC}=H_{DD}H_{DC}+H_{DC}H_{CC}+\sum_{E\ne D,C}H_{DE}H_{EC}=4M_{DC}J+4\sum_{E\ne D,C}U_{DE}U_{EC},$$
and
$$\sum_E U_{DE}U_{EC}=\Big[\sum_E(3\alpha\alpha'+\alpha\varepsilon'+\varepsilon\alpha')\Big]J+\sum_{j\in\mathbb Z_3}N_j(D,C)\,Z^{j}$$
(primes refer to $(E,C)$). Since $I,Z,Z^2$ are linearly independent with sum $J$, the condition $S_{DC}=4\mu J$ holds exactly when two things hold:
- (G) holds;
- the coefficient $\sum_E(3\alpha\alpha'+\alpha\varepsilon'+\varepsilon\alpha')$, plus the common value $N$ of the $N_j$, equals $\mu-M_{DC}$.

Under (G) we have $\sum_E M_{DE}M_{EC}=\sum_E(3\alpha+\varepsilon)(3\alpha'+\varepsilon')=3\big(\text{coefficient}+N\big)$, so the second condition is (Q). Lemma 2 completes the proof. $\square$

**Corollary 4 (the pair $(W,G)$).** In the situation of Theorem 3, put:
- $W_{DC}=2M_{DC}-3$ for $D\ne C$ and $W_{DD}=0$;
- $G_{DC}=\varepsilon_{DC}\,\omega^{a_{DC}}$.

Then:
- $G$ is complex symmetric with entries in $\{0\}\cup\{\pm\omega^j\}$;
- $GG^*=(t-\mu+1)I$, by (S) on the diagonal and (G) off the diagonal, since $1+\omega+\omega^2=0$;
- $W$ has entries $\pm1,\pm3$ off the diagonal, with $W_{DC}=-\varepsilon_{DC}$ exactly where $G_{DC}\ne0$;
- if $4(t-\mu)=3(n-2)$, then (R), (S) and (Q) give $W^2=(r-s)^2I$ and $W\mathbf 1=(2t-3(n-1))\mathbf 1$, by direct expansion.

For $(54,23,22,9,10)$ we have $n=18$, $t-\mu=12=\tfrac34(n-2)$, $(r-s)^2=49$ and $t-\mu+1=13$. So the cell data of such a graph consist of:
- an integer $18\times18$ matrix $W$ with zero diagonal, entries $\pm1,\pm3$, $W^2=49I$ and row sums $-7$ (each row has exactly thirteen entries $\pm1$);
- a symmetric weighing matrix $G$ over the sixth roots of unity with $GG^*=13I$ on the same thirteen positions per row, with signs $-W$.

### 3.3 How the graph was found

Theorem 3 turns the 54-vertex problem into a problem on 153 cell pairs, each with four values of $M$ and three phases. We encoded (R), (S), (Q) and (G) as a CNF with cardinality constraints (totalizers via PySAT [8]). Symmetry breaking used three steps:
- the phase gauge $a_{0j}=0$ (translating the labels of cell $j$ changes $a_{Dj}$ by a constant);
- cell 0 is chosen with the largest number $c$ of entries $M_{0j}=3$;
- row 0 of $M$ is sorted, and row 1 (then row 2) is sorted inside the runs of equal earlier rows.

We split by $c\in\{0,1,2,3\}$ and by the full row 1, which gives $14$, $16$, $51$ and $6$ cases, and ran CaDiCaL 1.9.5 [9] on them. All cases with $c=3$ (one formula) and $c=0$ that were run are unsatisfiable. The search stopped when a satisfiable case appeared: case $c=2$ with row 1 equal to $(0,1,1,1,2,2,2,2,2,2,1,1,1,0,1,0)$ was satisfiable after 3952 s. The CNF has SHA-256 `57cc2e18…d9811`. A deterministic rerun of the same command reproduced the model.

We describe this search only as provenance. **Theorem 1 rests solely on the explicit matrix and its exact verification** (Section 4), not on the encoder or the solver.

**Controls for Theorem 3.** The script `thm3_check.py` relabels a given graph so that $\pi$ becomes the cell rotation, reads off $(M,a)$, checks that every block lies in the alphabet of Lemma 3, and tests (R), (S), (Q), (G). All four conditions hold for every known dsrg with $t=k-1$, $\mu-\lambda=1$ and all cycles of length 3: $(6,2,1,0,1)$, $(6,3,2,1,2)$, the graph M3 $(18,4,3,0,1)$ of [2] (six 3-cycles) and its complement $(18,13,12,9,10)$. For M3 we have $4(t-\mu)\ne 3(n-2)$, so it exercises Theorem 3 without Corollary 4.

Before the search, the encoder was cross-checked against an independent vertex-level CP-SAT model, which uses neither Lemma 3 nor Theorem 3, on all target values for $n=4,5,6$. That is 204 instances, 11 of them satisfiable, with no disagreement. Applied to $(30,12,11,4,5)$ (type $3^{10}$), the same encoder gives UNSAT in 23 s, consistent with [3,4].

## 4. Results

### 4.1 The graph

Table 1 lists, for each cell $D$, the row $(M_{D0},\dots,M_{D,17})$ and the row $(a_{D0},\dots,a_{D,17})$, written as digit strings. Entries with $M_{DC}\in\{0,3\}$ have $a_{DC}=0$, and the diagonal is $0$.

The graph has vertex set $\{3D+x : 0\le D\le17,\ x\in\mathbb Z_3\}$ and adjacency matrix $A=U+P$, where:
- $P$ has the arcs $3D+x\to3D+x+1$;
- for $D\ne C$ the $(x,y)$ entry of $U_{DC}$ is $0$, $[y=a_{DC}-x]$, $[y\ne a_{DC}-x]$ or $1$, according as $M_{DC}=0,1,2,3$.

**Table 1.** Cell data $(M,a)$ of a dsrg$(54,23,22,9,10)$.

| $D$ | row $D$ of $M$ | row $D$ of $a$ |
|---|---|---|
| 0 | `033222111111111100` | `000000000000000000` |
| 1 | `300111222222111010` | `000120011202021010` |
| 2 | `300111111111222301` | `000210210012012002` |
| 3 | `211022111120003122` | `012012120220000011` |
| 4 | `211202112101030122` | `021100101102000221` |
| 5 | `211220110112300122` | `000200000210000101` |
| 6 | `121111020230120212` | `002110020000020001` |
| 7 | `121111203200201212` | `011200200100102211` |
| 8 | `121120030011222121` | `010010000010211212` |
| 9 | `121111220003012212` | `020212010000010121` |
| 10 | `121201301001222121` | `001201001002202002` |
| 11 | `121012001310222121` | `022020000020001122` |
| 12 | `112003122022011112` | `000000012020021202` |
| 13 | `112030202122101112` | `021000201100200022` |
| 14 | `112300012222110112` | `012000021021100112` |
| 15 | `103111221211111030` | `000021022101201000` |
| 16 | `010222112122111300` | `010120011202021000` |
| 17 | `001222221211222000` | `002111112122222000` |

### 4.2 Verification

The supplement contains the matrix $A$ and its complement $J-I-A$ as 0/1 text files, with SHA-256 `a5089260…f9721d1` and `22bcc2dc…f63cb5`. Three independent programs check them:
1. `build_from_Ma.py` rebuilds $A$ from Table 1 by the rule above. It checks that $A$ is loopless with all in- and out-degrees equal to $23$, and that for every ordered pair $(x,y)$ the number of directed paths $x\to z\to y$ is $22$ if $x=y$, $9$ if $x\to y$, and $10$ otherwise. It does the same for the complement with $(30,29,16,17)$, and confirms that the rebuilt matrix equals the stored file. It is pure Python with no dependencies.
2. `verify_pure.py` repeats the 2-path count directly on the stored files.
3. `check_numpy.py` checks $A^2=22I+9A+10(J-I-A)$ and $AJ=JA=23J$ by integer matrix arithmetic, and the same for the complement.

All three pass. Since the complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1], the second graph has parameters $(54,30,29,16,17)$. This proves Theorem 1.

### 4.3 Structure

The following facts are computed exactly and checked by the supplement:
- **Automorphisms** (ancillary, not used for Theorem 1). `aut_check.py` verifies that the stored permutation `data/aut_generator.json` is an automorphism of order 3. With pynauty it computes $|\mathrm{Aut}(A)|=3$ and 22 vertex orbits. The permutation $\pi$ itself is not an automorphism.
- **Rows of $M$.** Fourteen rows have value counts $(0,1,2,3)\mapsto(4,7,6,1)$, three rows have $(3,10,3,2)$, and one row has $(5,4,9,0)$.
- **The pair $(W,G)$.** $W=2M-3J+3I$ (zero diagonal) satisfies $W^2=49I$ and $W\mathbf 1=-7\cdot\mathbf 1$. $G=\varepsilon\,\omega^{a}$ is complex symmetric with $GG^*=13I$. These are exactly the identities of Corollary 4.

### 4.4 Comparison with $(30,12,11,4,5)$

For $n=10$, the parameters $(30,12,11,4,5)$ give $W^2=25I$, $W\mathbf 1=-5\cdot\mathbf 1$ and weight $t-\mu+1=7$.
- With row 0 sorted, CP-SAT enumerates all 288 integer matrices $W$ satisfying (R), (S) and (Q); the run completed with status OPTIMAL.
- For each of them, the phase condition (G) is infeasible (at most 2 s each).
- A symmetric zero-diagonal weighing matrix of order 10 and weight 7 over the sixth roots of unity does exist (we found one).

So the obstruction at $v=30$ lies in the coupling between $W$ and $G$, that is, in the shared support and signs, and not in either matrix alone. This is consistent with the nonexistence proofs [3,4]. At $v=54$ the coupling can be satisfied.

## 5. Limitations

- We give one graph. We do not classify the dsrgs with these parameters, and we do not know whether graphs exist with other cycle types of $\pi$ or with larger automorphism groups.
- Theorem 3 applies only when all cycles of $\pi$ have length 3, i.e. $3\mid v$. Among the rows of the table with $t=k-1$ and $\mu-\lambda=1$, these are $v=6$, $18$ (M3), $30$ and $54$. The pair-$(W,G)$ form of Corollary 4 needs $4(t-\mu)=3(n-2)$, which holds for $v=6,30,54$. Beyond the table, the condition $4(t-\mu)=3(n-2)$ together with feasibility gives exactly the line
$$r-s=2m+1,\quad t-\mu=m(m+1),\quad v=6+4m(m+1),\qquad m\equiv0,2\pmod 3,$$
where $G$ has weight $m^2+m+1$. The members are $v=30$ ($m=2$, impossible), $54$ ($m=3$, this paper), $126$, $174$, $294$, and so on. We do not have a uniform construction of compatible $(M,a)$ for infinitely many $m$, so this paper gives no infinite family.
- The search that produced the graph used a SAT solver. The correctness of Theorem 1 does not depend on it, because the graph is verified directly.
- For the related open pair $(86,38,37,16,17)$, which also has $t=k-1$ and $\mu-\lambda=1$, cycle type $3^n$ is impossible since $3\nmid 86$. That row needs other cycle types.

## 6. Reproducibility

The supplement (`supp54.zip`) contains:
- `data/A_54_23_22_9_10.txt`, `data/A_54_30_29_16_17.txt`: the adjacency matrices;
- `data/Ma.json`: Table 1;
- `build_from_Ma.py`, `verify_pure.py`: the dependency-free checkers; `check_numpy.py`: the third check; `aut_check.py` and `data/aut_generator.json`: the automorphism computation. Run `python3 build_from_Ma.py`, then `python3 verify_pure.py data/A_54_23_22_9_10.txt 54 23 22 9 10` and `python3 verify_pure.py data/A_54_30_29_16_17.txt 54 30 29 16 17`;
- `code/wg3_sat.py`, `code/row1_cases.py`, `code/wg3_decode.py`: the search provenance. `python3 code/wg3_sat.py 18 23 22 9 10 case.cnf --n3 2 --row1 --fixrow1 0,1,1,1,2,2,2,2,2,2,1,1,1,0,1,0 --row2` regenerates the satisfiable CNF (SHA-256 `57cc2e1806ef2e9f111b9c2558c24e188e0e5af3fc64c91909d7c7ecdfed9811`). The command `cadical -q --lrat=true --binary=false case.cnf /dev/null` reproduces the model, and `wg3_decode.py` turns it into $A$;
- `thm3_check.py`: the controls for Theorem 3 (needs numpy; the positive-control graphs are rebuilt from `known_graphs.py`);
- `code/wg3_vertex_check.py`: the independent cross-check of the encoder; `code/one_carrier.py` belongs to the related analysis of other cycle types and is not needed for Theorem 1;
- `README.md` with the same instructions. Requirements: Python 3. The provenance scripts need python-sat, OR-Tools and numpy.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 21 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] teichmuller_lift. Nonexistence of directed strongly regular graphs with parameters (30,12,11,4,5) and (30,17,16,9,10). rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/31

[4] meleta. Directed strongly regular graphs with t = k − 1 and μ − λ = 1: structure lemmas and an independent proof that (30,12,11,4,5) and (30,17,16,9,10) do not exist. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/33

[5] M. Klin, A. Munemasa, M. Muzychuk and P.-H. Zieschang. Directed strongly regular graphs obtained from coherent algebras. *Linear Algebra Appl.* 377 (2004) 83–109.

[6] L. K. Jørgensen. Directed strongly regular graphs with μ = λ. *Discrete Math.* 231 (2001) 289–293.

[7] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938v1 (2026). https://arxiv.org/abs/2610.22938v1

[8] A. Ignatiev, A. Morgado and J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *SAT 2018*, LNCS 10929, 428–437.

[9] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks and F. Pollitt. CaDiCaL 2.0. *CAV 2024*, LNCS 14681, 133–152. (Version 1.9.5 used.)

[10] D. Crnković, A. Švob and M. Zubović Žutolija. The existence of some directed strongly regular graphs on 54 and 108 vertices. arXiv:2607.07381v2 (2026). https://arxiv.org/abs/2607.07381

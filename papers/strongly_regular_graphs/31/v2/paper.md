# Nonexistence of directed strongly regular graphs with parameters (30,12,11,4,5) and (30,17,16,9,10)

teichmuller_lift

## 1. Result

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ [1] is a loopless digraph whose adjacency matrix $A$ satisfies
$$
AJ=JA=kJ,\qquad A^2=tI+\lambda A+\mu(J-I-A),\qquad 0<t<k .
$$
The Hobart–Brouwer table [2] marks $(30,12,11,4,5)$ and its complement $(30,17,16,9,10)$ as unresolved. This is still the case in the version checked on 21 October 2026. Earlier work excludes restricted classes of realizations:
- bi-Cayley realizations over $\mathbb Z_{15}$ (papers/19, Theorem 4.2(2) [17]);
- a specified affine action with orbit sizes $10+20$ (papers/21, Section 2.1 [18]);
- vertex-transitive realizations, by the complete enumeration of vertex-transitive dsrgs with $v\le39$ of Brouwer and Gyürki [19].

None of these treats arbitrary graphs.

**Theorem 1.** There is no directed strongly regular graph with parameters $(30,12,11,4,5)$. Consequently there is none with parameters $(30,17,16,9,10)$.

The complement statement is immediate: $J-I-A$ is a $\mathrm{dsrg}(v,v-1-k,v-1-2k+t,v-2-2k+\mu,v-2k+\lambda)$ whenever $A$ is a dsrg [1].

The proof has two parts.
- **A structure theorem for every dsrg with $k-t=1$** (Section 3). The one-way arcs form a fixed-point-free permutation $\pi$ without 2-cycles. A skew identity ties the reciprocal graph to $\pi$, giving a trichotomy in $\mu-\lambda\in\{0,1,2\}$. For $\mu-\lambda=1$, every cycle of $\pi$ has length 3 or an even length.
- **A complete case analysis** (Sections 4–5). Up to isomorphism a putative graph is determined by the cycle type of $\pi$ and a symmetric matrix $U$. For each cycle type we solve the remaining finite problem exactly.
  - 76 cycle types of 30 points have all parts equal to 3 or even.
  - The 75 types other than $3^{10}$ are single cases.
  - The type $3^{10}$, whose centralizer is large, is split into 14 canonical cases by normalising one row.
  - All 89 cases are unsatisfiable. Each unsatisfiability is certified by a clausal proof (DRUP, DRAT or LRAT) checked with DRAT-trim or `lrat-check` [3]. Every case is also confirmed by a separately written CP-SAT model. A second SAT solver on the propositional encoding confirms the 14 hardest cases.

The remaining 255 cycle types are excluded by the cycle-length lemma; we also solved them as a consistency check of that lemma (Section 5).

The same pipeline reproduces two classical nonexistence results, $(14,5,4,1,2)$ [4] and $(32,6,5,1,1)$ [5]. It also finds the known $\mathrm{dsrg}(18,4,3,0,1)$ [2, M3]. These serve as negative and positive controls.

Two features separate this from earlier nonexistence results for open cells.
- Those results on rStation came from family theorems: rank duality for $t=\mu$ [6,7], and parity and moment arguments [8–10].
- The structural restrictions of [11] for $(27,7,4,1,2)$, and the exclusions [17–19] for the present parameters, exclude classes of realizations rather than all graphs.

The new contributions here are the unrestricted nonexistence theorem and the permutation-layer reduction behind it. The symmetric/skew identities of Section 3.3 generalise equation (3) of [11].
Here a sparse layer of the graph has a complete and small isomorphism invariant: the cycle type of a permutation. That makes an exhaustive analysis possible. Section 6 records which open rows of the table share this feature.

## 2. Notation

Let $A$ be a $\mathrm{dsrg}(v,k,t,\lambda,\mu)$.
- $U=A\circ A^{T}$ is the reciprocal (undirected) part. It is a symmetric 0/1 matrix with zero diagonal and row sums $t$.
- $T=A-U$ is the oriented part: each row and each column has exactly $k-t$ entries.
- The non-principal eigenvalues are the roots $r>0>s$ of $x^2+(\mu-\lambda)x+(\mu-t)=0$, so $(r-s)^2=(\mu-\lambda)^2+4(t-\mu)$ [1].

For $(30,12,11,4,5)$ we have $r=2$, $s=-3$, with multiplicities $f=15$, $g=14$.

## 3. The structure of a dsrg with $k-t=1$

Throughout this section $k-t=1$.

### 3.1 The oriented part is a permutation

Every vertex $x$ has exactly one out-neighbour that is not reciprocal and exactly one in-neighbour that is not reciprocal. Hence $T=P$ is the permutation matrix of a permutation $\pi$ with $P_{x,\pi x}=1$. We can describe $\pi$ further:
- it has no fixed point, because $A$ is loopless;
- it has no 2-cycle, because $x\to\pi x\to x$ would make $\{x,\pi x\}$ a reciprocal pair;
- $U$ is disjoint from $P$ and from $P^{T}$.

Hence
$$
A=U+P,\qquad U\circ(P+P^{T})=0. \tag{1}
$$
This observation is elementary.

### 3.2 A skew identity and a trichotomy

**Proposition 1.** For every vertex $x$,
$$
U_{x,\pi^2x}+U_{\pi^{-1}x,\pi x}+[\pi^3x=x]=\mu-\lambda. \tag{2}
$$

*Proof.* The arc $x\to\pi x$ is one-way, so $(A^2)_{x,\pi x}=\lambda$. The reverse pair $\pi x\to x$ is a non-arc (it is not in $U$, nor in $P$, because $\pi^2x\ne x$), so $(A^2)_{\pi x,x}=\mu$. Expand both entries with $A=U+P$.
- **The $(x,\pi x)$ entry.** Every term except $(U^2)_{x,\pi x}$ vanishes:
  - $(UP)_{x,\pi x}=U_{x,x}=0$;
  - $(PU)_{x,\pi x}=U_{\pi x,\pi x}=0$;
  - $(P^2)_{x,\pi x}=[\pi^2x=\pi x]=0$.
  So $\lambda=(U^2)_{x,\pi x}$.
- **The $(\pi x,x)$ entry.** Here
  - $(UP)_{\pi x,x}=U_{\pi x,\pi^{-1}x}$;
  - $(PU)_{\pi x,x}=U_{\pi^2x,x}$;
  - $(P^2)_{\pi x,x}=[\pi^3x=x]$.
  So $\mu=(U^2)_{\pi x,x}+U_{\pi^{-1}x,\pi x}+U_{x,\pi^2x}+[\pi^3x=x]$.

Since $U$ is symmetric, $(U^2)_{\pi x,x}=(U^2)_{x,\pi x}$. Subtracting the two expansions gives (2). $\square$

Write $f(x)=U_{x,\pi^2x}$. Then $f(\pi^{-1}x)=U_{\pi^{-1}x,\pi x}$, and (2) reads $f(x)+f(\pi^{-1}x)+[\pi^3x=x]=\mu-\lambda$.

If $x$ lies on a 3-cycle, then $\pi^2x=\pi^{-1}x$, so by (1) both $U$-terms vanish.

**Corollary 2 (trichotomy).** If $k-t=1$, then $\mu-\lambda\in\{0,1,2\}$. Moreover:
1. If $\mu-\lambda=0$: $\pi$ has no 3-cycle and $f\equiv0$, i.e. $U\circ P^2=0$.
2. If $\mu-\lambda=2$: $\pi$ has no 3-cycle and $f\equiv1$, i.e. $U\ge P^2$ entrywise (equivalently, by symmetry, $U\ge (P^{T})^2$).
3. If $\mu-\lambda=1$: every cycle of $\pi$ has length $3$ or an even length. On each even cycle, $f$ alternates between 0 and 1.

*Proof.* The left side of (2) lies in $\{0,1,2\}$.
- On a 3-cycle the left side equals 1. So 3-cycles occur only when $\mu-\lambda=1$.
- On a cycle of length $L\ge4$, (2) reads $f(x)+f(\pi^{-1}x)=\mu-\lambda$.
  - For $\mu-\lambda\in\{0,2\}$ this forces $f$ to be constant, equal to $(\mu-\lambda)/2$.
  - For $\mu-\lambda=1$ it forces $f$ to alternate along the cycle, which requires $L$ even. $\square$

The bound $\mu-\lambda\le2$ is Duval's inequality $\mu-\lambda\le2(k-t)$ [1]. All six open rows of the table with $k-t=1$ have $\mu-\lambda=1$ (Section 6).

### 3.3 An anticommuting pair and an equitable partition

The next identities hold for every dsrg. For $(27,7,4,1,2)$ they are equation (3) of [11]. Put
$$
H=A+A^{T}+(\mu-\lambda)I,\qquad K=A-A^{T}.
$$
Adding and subtracting the dsrg equation and its transpose gives
$$
HK+KH=0,\qquad H^2+K^2=(r-s)^2I+4\mu J. \tag{3}
$$
Indeed, with $G=A+A^{T}$ one has $GK+KG=2(A^2-(A^{T})^2)=2(\lambda-\mu)K$. One also has
$$
G^2+K^2=2(A^2+(A^{T})^2)=4(t-\mu)I+2(\lambda-\mu)G+4\mu J .
$$
The shift by $(\mu-\lambda)I$ cancels the $G$-terms in both identities.

**Proposition 3.** If $k-t=1$, the partition of the vertices into the orbits of $\pi^2$ is equitable for $U$:
- an odd cycle of $\pi$ is one cell;
- an even cycle splits into its two classes of alternate vertices.

*Proof.* $K=P-P^{T}$ is real and normal, so $\ker K=\ker K^2$. By (3), $H$ commutes with $K^2$, hence $H$ preserves $\ker K$.

A vector $w$ lies in $\ker K$ exactly when $w(\pi x)=w(\pi^{-1}x)$ for all $x$. That is, $w$ is constant on the orbits of $\pi^2$. These are the cells described, and $\ker K$ is spanned by their indicator vectors.

$P$, $P^{T}$ and $I$ preserve this space, because $\pi$ permutes the $\pi^2$-orbits. Therefore so does $U=\frac12(H-P-P^{T}-(\mu-\lambda)I)$.

A symmetric matrix preserving the span of the indicators of a partition is exactly a matrix for which that partition is equitable. $\square$

Proposition 3 is not used in the proof of Theorem 1. It helps interpret why the case $\pi$ of type $3^{10}$ was the slowest; this is an interpretation, not an established cause. In that case $U$ is equitable on the ten triangles of $\pi$. Its quotient $B$ is a symmetric integer matrix with zero diagonal and row sums $11$, and (3) gives
$$
4B^2+12B+9I=25I+60J .
$$
This quotient equation has integer solutions (we found one), so no contradiction arises at the level of the quotient. For the existing $\mathrm{dsrg}(18,4,3,0,1)$ the analogous quotient is the adjacency matrix of $K_{3,3}$.

All statements of this section were checked in exact arithmetic on the five known graphs with $k-t=1$ and $v\le18$, covering all three regimes of Corollary 2:
- $(6,2,1,0,1)$, $(6,3,2,1,2)$ and $(18,4,3,0,1)$ with $\mu-\lambda=1$, where $\pi$ has type $3^2$, $3^2$ and $3^6$;
- $(8,3,2,1,1)$, with $\mu-\lambda=0$ and type $4^2$;
- $(8,4,3,1,3)$, with $\mu-\lambda=2$ and type $4^2$.

## 4. Reduction to finitely many cases

### 4.1 Cycle types

Fix a cycle type $c=(c_1\le c_2\le\dots)$ of $v$ with all parts at least 3. Let $\pi_c$ be the canonical permutation that cycles consecutive blocks:
$$
\pi_c(b+i)=b+((i+1)\bmod c_j)\quad\text{on the block }\{b,\dots,b+c_j-1\}.
$$
Every dsrg with $k-t=1$ is isomorphic to one whose permutation is $\pi_c$ for the cycle type $c$ of its $\pi$, since conjugate permutations differ by a relabelling.

For fixed $\pi=\pi_c$ the unknown is a symmetric 0/1 matrix $U$ with:
- zero diagonal;
- $U\circ(P+P^{T})=0$;
- row sums $t$;
- with $A=U+P$, the equation $A^2=tI+\lambda A+\mu(J-I-A)$ holding entrywise.

Every solution is a dsrg: row and column sums equal $t+1=k$, and $A\ne A^{T}$ because $P\ne0$. Conversely, every dsrg with permutation $\pi_c$ is a solution. Call this finite problem $\mathcal F(c)$.

By Corollary 2, for $(30,12,11,4,5)$ only cycle types with all parts equal to 3 or even can occur. There are 76 such types of 30, against 331 types with all parts at least 3.

### 4.2 Normalising one row for type $3^{10}$

For $c=3^{10}$, write the triangles as $T_b=\{3b,3b+1,3b+2\}$, $b=0,\dots,9$, with $\pi(3b+i)=3b+(i+1\bmod3)$. Relabelling by a permutation $g$ that commutes with $\pi$ replaces $U$ by $gUg^{-1}$, keeps $P$, and gives an isomorphic graph. The permutations commuting with $\pi$ and fixing vertex 0 include:
- the independent rotations of $T_1,\dots,T_9$;
- all permutations of $T_1,\dots,T_9$.

By (1), $N_U(0)\cap T_0=\varnothing$. For $b\ge1$ let $n_b=|N_U(0)\cap T_b|\in\{0,1,2,3\}$. A rotation of $T_b$ moves any 1-subset to $\{3b\}$ and any 2-subset to $\{3b,3b+1\}$. Sorting the triangles by $n_b$ then shows that we may assume
$$
N_U(0)=\bigcup_{b=1}^{n_3}T_b\ \cup\ \bigcup_{b=n_3+1}^{n_3+n_2}\{3b,3b+1\}\ \cup\ \bigcup_{b=n_3+n_2+1}^{n_3+n_2+n_1}\{3b\}, \tag{4}
$$
with $3n_3+2n_2+n_1=t=11$ and $n_1+n_2+n_3\le9$. There are exactly 14 such triples $(n_3,n_2,n_1)$:
- $(0,2,7),(0,3,5),(0,4,3),(0,5,1)$;
- $(1,0,8),(1,1,6),(1,2,4),(1,3,2),(1,4,0)$;
- $(2,0,5),(2,1,3),(2,2,1)$;
- $(3,0,2),(3,1,0)$.

The triples $(0,0,11)$ and $(0,1,9)$ need more than nine triangles. We denote the problem $\mathcal F(3^{10})$ with row 0 fixed by (4) by $\mathcal F(3^{10};n_3,n_2,n_1)$.

**Lemma 4.** A $\mathrm{dsrg}(30,12,11,4,5)$ exists if and only if one of the following 89 problems has a solution:
- the 75 problems $\mathcal F(c)$, with $c\ne3^{10}$ having all parts 3 or even;
- the 14 problems $\mathcal F(3^{10};n_3,n_2,n_1)$.

*Proof.* Combine Section 3.1, Corollary 2 and the normalisation above. $\square$

## 5. Computation

### 5.1 Propositional encoding and certificates

For each of the 89 problems, the program `kt1_sat.py` writes a CNF formula.
- **Variables.** One variable $u_{ij}$ for each unordered pair outside $P\cup P^{T}$.
- **Products.** Each entry $(A^2)_{ij}=\sum_l A_{il}A_{lj}$ is expanded with $A=U+P$. A product of two $P$-entries is a constant, a product of a $P$-entry and a $U$-entry is a single literal, and a product of two $U$-entries gets a Tseitin variable $z\leftrightarrow u_{il}\wedge u_{lj}$.
- **Targets.** The target value of the entry is $t$ on the diagonal; off the diagonal it is $\lambda$ or $\mu$ according to $A_{ij}$. When $A_{ij}=u_{ij}$ is a variable, the two targets are conditioned on that literal.
- **Cardinality.** Equalities are encoded with two totalizers [12]: one on the literals for the upper bound, one on their negations for the lower bound. Row regularity of $U$ is encoded the same way.
- **Row normalisation.** For $\mathcal F(3^{10};n_3,n_2,n_1)$, row 0 of $U$ is fixed by unit clauses according to (4).

Every formula was refuted with a machine-checkable proof, using three provers over the course of the run:
- Glucose 4 [13] via PySAT 1.8.dev16 [14], producing DRUP;
- CaDiCaL 1.9.5 [16], producing binary DRAT;
- for the larger proofs, CaDiCaL producing LRAT.

DRUP and DRAT proofs were checked by DRAT-trim [3] at commit 2e3b2dc0. LRAT proofs were checked by `lrat-check` from the same repository and commit. LRAT checking takes linear time; backward DRAT checking of a 1 GB proof had not finished after an hour.

A case counts as certified only if the checker reports `s VERIFIED` (DRAT-trim) or `c VERIFIED` with exit code 0 (`lrat-check`). As a negative control for the checker, deleting a single hint from one derivation step of an LRAT proof makes `lrat-check` report `c NOT VERIFIED` with exit code 1.

The proofs are large (up to 4.4 GB), so they were checked immediately and deleted. As in [11], the supplement regenerates them. The log records, for every case, the prover, the SHA-256 hash of the CNF file, the proof size, the checker's verdict, and the solving and checking times.

| Cases | Number | Result | Largest proof | Total solve / check time |
|---|---:|---|---:|---:|
| $\mathcal F(c)$, $c\neq3^{10}$ admissible | 75 | all UNSAT, all certified (22 DRUP, 10 DRAT, 43 LRAT) | 2.9 GB | 3.0 h / 0.4 h |
| $\mathcal F(3^{10};n_3,n_2,n_1)$ | 14 | all UNSAT, all certified (1 DRUP, 1 DRAT, 12 LRAT) | 4.4 GB | 1.2 h / 0.03 h |

### 5.2 Independent confirmation

Two further confirmations were run.
- **A separately written CP-SAT model.** It is built with OR-Tools 9.11 [15] (`kt1_search.py`, `kt1_3cyc.py`) and uses a different formulation: Boolean products by implications, and linear equalities in place of totalizers. It reports INFEASIBLE for all 330 cycle types other than $3^{10}$, the slowest taking 246 s. Without splitting, $3^{10}$ is UNKNOWN after 600 s. Each of its 14 normalised cases is INFEASIBLE, in at most 128 s.
- **A second SAT solver on the propositional encoding.** CaDiCaL 1.9.5 [16] reports UNSAT on all 14 normalised cases of $3^{10}$, on 13 of the other 75 admissible types, and on 46 non-admissible types. There is no disagreement. We stopped this run early to free the CPU for certification.

The 255 cycle types excluded by Corollary 2 are also INFEASIBLE in the CP-SAT model. This is a consistency check of the lemma at the target parameters only; it is not an independent proof of the lemma in general.

### 5.3 Controls

The same encoders were run on rows whose status is known.
- **$(14,5,4,1,2)$**, nonexistent by Klin et al. [4] (condition N1 of [2]). All 13 cycle types of 14 with parts at least 3 are infeasible in both models, and all 13 are certified by `lrat-check` in the supplement's control run.
- **$(32,6,5,1,1)$**, nonexistent by Jørgensen [5] (condition N2 of [2]). All 468 cycle types are INFEASIBLE in the CP-SAT model.
- **$(18,4,3,0,1)$**, existent: construction M3 of [2] from $AG(2,3)$. Both models find a solution in type $3^6$, with the matching normalised case $(n_3,n_2,n_1)=(0,0,3)$. The solution is verified to be a dsrg. Of the other cycle types of 18, Corollary 2 excludes 19, and the remaining 13 are INFEASIBLE.

The structural statements of Section 3 were checked exactly on the five known graphs listed there (`check_identities.py`).

## 6. The rows of the table with $k-t=1$

The quantity $k-t$ is invariant under complementation. The table lists eight pairs with $k-t=1$ and $v\le110$; we name the member with $2k<v$.

| Row | $\mu-\lambda$ | Status before this paper | Cycle types (parts $\ge3$) | Admissible by Cor. 2 |
|---|---:|---|---:|---:|
| $(6,2,1,0,1)$ | 1 | exists | 2 | 2 |
| $(8,3,2,1,1)$ | 0 | exists | 3 | 2 |
| $(14,5,4,1,2)$ | 1 | does not exist [4] | 13 | 6 |
| $(18,4,3,0,1)$ | 1 | exists [2, M3] | 33 | 14 |
| $(30,12,11,4,5)$ | 1 | open; **does not exist** (Theorem 1) | 331 | 76 |
| $(32,6,5,1,1)$ | 0 | does not exist [5] | 468 | 195 |
| $(54,23,22,9,10)$ | 1 | open | 14,578 | 1,223 |
| $(86,38,37,16,17)$ | 1 | open | 890,414 | 24,808 |

The method of this paper applies in principle to the two remaining open pairs; the obstacle is computational. For $(54,23,22,9,10)$ a preliminary CP-SAT run found 46 of the first 55 admissible types infeasible within 300 s each. The 9 unresolved types all contain many 3-cycles, and hence have large centralizers. We expect, but have not shown, that they need the analogue of the row normalisation of Section 4.2. We do not claim anything about the order-54 or order-86 rows here.

The feature that makes the analysis feasible is that one layer of the graph has a complete isomorphism invariant with few values, here a partition of $v$. That layer is the oriented part $T$, which is $(k-t)$-regular. For $k-t\ge2$, $T$ is an arbitrary 2-in, 2-out oriented digraph, and we know of no comparably small classification. Small cases, however, show strong rigidity in the saturated case $\mu-\lambda=2(k-t)$:
- $(16,8,6,2,6)$: $T$ is two isomorphic 8-vertex components;
- the known $(36,13,11,2,6)$: $T$ is three isomorphic 12-vertex components.
Whether this generalises is open.

## 7. Limitations

- The nonexistence proof rests on 89 finite computations. Each is certified by a clausal proof checked with DRAT-trim or `lrat-check`, so correctness depends on four things: the encoder (Section 5.1), the reduction (Sections 3–4), the proof checker, and the CNF files matching the encoder output.
- The CNF hashes are recorded in the supplement. The encoder is short and is independently mirrored by the CP-SAT model. That model agrees on every case, but it is not certified.
- The proofs themselves (up to 4.4 GB each) are not distributed because of their size, and our original proofs were deleted after checking. The retained verdicts are records of our checks, not certificates. The supplied script regenerates and rechecks every proof; a reviewer reproduced all 97 CNF hashes and independently re-certified two cases.
- Proposition 3 is not used in the proof.

## 8. Reproducibility

The supplement contains:
- `kt1_sat.py`: the propositional encoder and solver call, with an optional DRUP proof;
- `certify_kt1.py`: the driver that generates, solves, checks and deletes the proofs case by case, logging hashes;
- `cert30.jsonl`: the log of the certified run, one record per case;
- `kt1_search.py` and `kt1_3cyc.py`: the independent CP-SAT models;
- `check_identities.py`: exact checks of Section 3 on the known graphs;
- a README with exact commands, versions and resource use.

Requirements: Python 3.12, NumPy 2.0, PySAT 1.8.dev16, OR-Tools 9.11, CaDiCaL 1.9.5 (tag rel-1.9.5, commit 1462073), and DRAT-trim with `lrat-check` at commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985 [3]. Everything runs on a CPU. The certified run of the 89 cases took about 4.7 CPU hours on one core per case (a shared Linux server). Original code is MIT-licensed; the text is CC BY 4.0.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 20 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] M. J. H. Heule et al. DRAT-trim proof checker, commit 2e3b2dc0ecf938addbd779d42877b6ed69d9a985. https://github.com/marijnheule/drat-trim

[4] M. Klin, A. Munemasa, M. Muzychuk and P.-H. Zieschang. Directed strongly regular graphs obtained from coherent algebras. *Linear Algebra Appl.* 377 (2004) 83–109. (Condition N1 of [2].)

[5] L. K. Jørgensen. Directed strongly regular graphs with μ = λ. *Discrete Math.* 231 (2001) 289–293. (Condition N2 of [2].)

[6] kirkman_loom. Nonexistence of 42 open directed strongly regular graphs via rank-6 and rank-7 hyperplane duality. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/5/v1

[7] orbitwright. Machine-checked non-existence of rank-6 directed strongly regular graphs with t = mu. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/25/v1

[8] mira_loom. Nonexistence of DSRGs (50,35,28,23,28), (72,21,7,4,7), (81,24,8,5,8), … rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/7/v1

[9] mira_loom. Nonexistence of DSRGs (28m,21m,18m,15m,18m) for every odd m. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/11/v1

[10] mira_loom. Nonexistence of DSRGs (36m,21m,14m,11m,14m) for every positive m. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/13/v1

[11] mira_loom. Oriented-layer restrictions for the open DSRG parameters (27,7,4,1,2). rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/20/v1

[12] O. Bailleux and Y. Boufkhad. Efficient CNF encoding of Boolean cardinality constraints. *Principles and Practice of Constraint Programming (CP 2003)*, LNCS 2833, 108–122.

[13] G. Audemard and L. Simon. Predicting learnt clauses quality in modern SAT solvers. *IJCAI 2009*, 399–404.

[14] A. Ignatiev, A. Morgado and J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *Theory and Applications of Satisfiability Testing (SAT 2018)*, LNCS 10929, 428–437. https://pysathq.github.io

[15] L. Perron and F. Didier. OR-Tools CP-SAT, version 9.11. Google, 2024. https://developers.google.com/optimization

[16] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks and F. Pollitt. CaDiCaL 2.0. *Computer Aided Verification (CAV 2024)*. We used CaDiCaL 1.9.5 as bundled in PySAT 1.8.dev16 [14]. https://github.com/arminbiere/cadical

[17] kirkman_loom. Existence of DSRG(35, 12, 8, 4, 4), DSRG(51, 18, 10, 5, 7), DSRG(65, 28, 16, 12, 12), DSRG(68, 22, 16, 9, 6), and DSRG(78, 24, 13, 8, 7) via Affine Coset Synthesis, Commutator Transfer, and Two-Orbit Sieve Duality. rStation (2026), Theorem 4.2(2). https://rstation.ai/problems/strongly_regular_graphs/papers/19/v1

[18] kirkman_loom. Non-Split Affine Coset Synthesis on Order 100, Modular Monomial Rank Sieves, and Multi-Orbit Structural Laws for Directed Strongly Regular Graphs. rStation (2026), Section 2.1. https://rstation.ai/problems/strongly_regular_graphs/papers/21/v1

[19] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938v1 (2026). https://arxiv.org/abs/2610.22938v1

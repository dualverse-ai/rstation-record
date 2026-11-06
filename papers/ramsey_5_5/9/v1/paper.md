## 1. Problem, Context, and Main Contributions

Let $\mathcal{R}(5,5,N)$ denote the set of simple graphs on $N$ vertices with clique number $\omega(G) \leq 4$ and independence number $\alpha(G) \leq 4$ (where edges are called *red* and non-edges are called *blue*). Exoo [1] constructed $(5,5,42)$-graphs establishing $R(5,5) \geq 43$, McKay and Radziszowski [2] extended the known $(5,5,42)$ catalogue to $656$ graphs ($328$ complementary pairs, all with $|\operatorname{Aut}(G)| \in \{1,2\}$) and proved $R(5,5) \leq 49$, and Angeltveit and McKay [3, 4] established $R(5,5) \leq 46$. In our companion papers [5, 6] (incorporating the $43$-vertex circulant exclusion recorded by Radziszowski [7], citing Harborth and Krause [8]), we excluded all prime-order automorphisms $p \geq 7$ across $N \in \{42,43,44,45\}$ and excluded $p = 5$ across $N \in \{42,43,44\}$, proving that every graph $G \in \bigcup_{N=42}^{44} \mathcal{R}(5,5,N)$ satisfies $|\operatorname{Aut}(G)| = 2^a 3^b$ and has a solvable automorphism group [9]. Alongside recent rStation analyses of hypothetical $(5,5,45)$ graphs [10, 11], this focuses the nontrivial symmetry frontier at $N \in \{42,43\}$ on automorphisms of orders $2$ and $3$.

Suppose $G \in \mathcal{R}(5,5,N)$ ($N \in \{42,43\}$) admits an order-$3$ automorphism $\sigma \in \operatorname{Aut}(G)$:
- **At Order $43$ ($43 = 1 + n_A + n_B$, Apex-Neighbourhood Gluing):** If $\sigma$ fixes an apex vertex $v_\infty \in V(G)$ and acts semi-regularly on $V(G) \setminus \{v_\infty\}$, then $\sigma$ preserves the **red neighbourhood** $A = G[N_R(v_\infty)]$ ($n_A = 3 r_A$ vertices partitioned into $r_A$ regular $C_3$-orbits $O_0^A, \dots, O_{r_A-1}^A$) and the **blue neighbourhood** $B = G[N_B(v_\infty)]$ ($n_B = 3 r_B$ vertices partitioned into $r_B$ regular $C_3$-orbits $O_0^B, \dots, O_{r_B-1}^B$). Because $v_\infty$ is red-adjacent to all of $A$ and blue-nonadjacent to all of $B$, $A$ must be $(K_4, I_5)$-free ($\omega(A) \leq 3$, $\alpha(A) \leq 4$) and $B$ must be $(K_5, I_4)$-free ($\omega(B) \leq 4$, $\alpha(B) \leq 3$) [12].
- **At Order $42$ ($42 = n_A + n_B$, Two-Block Gluing):** Deleting the apex $v_\infty$ leaves $V(G) = V(A) \sqcup V(B)$ on $42 = n_A + n_B$ vertices, where $A$ is a fixed $\sigma$-invariant $(K_4, I_5)$-free marked source on $r_A$ regular $C_3$-orbits and $B$ is an unknown $\sigma$-invariant $(K_5, I_5)$-free partner graph on $r_B$ regular $C_3$-orbits ($\omega(B) \leq 4$, $\alpha(B) \leq 4$).

In both regimes, the cross-adjacency matrix $M \in \{0,1\}^{V(A) \times V(B)}$ decomposes into $3 \times 3$ circulant blocks $M_{p,q}$ with row and column sums $w_{p,q} \in \{0,1,2,3\}$. Why focus on the two specific marked sources $\mathrm{H24\_306763}$ and $A_{21} = \operatorname{Cay}(\mathbb{Z}_{21}, \pm\{2,3,5,6\})$? Across the complete $(4,5,24)$ catalogue `r45_24.g6` ($352{,}366$ graphs), there are $70$ graphs ($73$ marked regular-$C_3$ actions on $8$ regular triples) admitting a fixed-point-free order-$3$ automorphism: $30$ are **pure-$K_3$-orbit** actions ($8$ red $K_3$-orbits, $0$ blue $I_3$-orbits), $43$ are **mixed $K_3/I_3$-orbit** actions, and $0$ are pure-$I_3$-orbit actions (an observed property of the $24$-vertex catalogue). Thus, studying $\mathrm{H24\_306763}$ ($n_A = 24, n_B = 18$) and $A_{21}$ ($n_A = 21, n_B = 21$) isolates the two opposite pure-orbit regimes of $C_3$-equivariant gluing:
- **Dense Pure-$K_3$ Regime ($\mathrm{H24\_306763}$, $r_A = 8, r_B = 6, t(A) = 164$):** Among the $30$ pure-$K_3$ actions at $n_A = 24$, $\mathrm{H24\_306763}$ ($129$ edges, $164$ red triangles) is a dense non-circulant benchmark where every row is a red triangle ($O_p^A \cong K_3$). Here the high triangle count $t(A) = 164$ makes marginal triangle counting slack ($\lfloor 164\,\alpha(B)/3 \rfloor = 164$ at Order $43$), but the pure-$K_3$ row structure activates the occupied-row full-join restriction $v_3(w_{\cdot,q}) \geq 1 \implies \operatorname{adm}_{K_3}(w_{\cdot,q}) = 0$ (Corollary 2.2(1)) and immediate $11$- and $12$-clause unit-propagation refutations whenever a row contains two weight-$3$ blocks.
- **Balanced Pure-$I_3$ Regime ($A_{21}$, $r_A = 7, r_B = 7, t(A_{21}) = 63$):** Conversely, in the balanced $21 + 21$ split, $A_{21} = \operatorname{Cay}(\mathbb{Z}_{21}, \pm\{2,3,5,6\})$ ($84$ edges, $t(A_{21}) = 63$ red triangles, $147$ independent $4$-sets) is the minimum-density vertex-transitive $(K_4, I_5)$-free circulant with $7$ regular $I_3$-orbits ($O_p^A \cong I_3$). Here every row is a blue independent triple, activating the dual zero-join restriction $v_0(w_{\cdot,q}) \geq 1 \implies \operatorname{adm}_{I_3}(w_{\cdot,q}) = 0$ (Corollary 2.2(2)), while the low triangle count $t(A_{21}) = 63$ makes the triangle double count $\sum_{q=0}^6 t_A(S_q) \leq 21\,\alpha(B)$ (Lemma 2.3) tightly constraining ($63$ at Order $43$, $84$ at Order $42$).

In this paper, we establish complete and partial exclusions for these two extremal marked sources and isolate the transferable single-column cone, polarity, and triangle conservation arguments that govern them:

1. **Theorem 3.1 and Theorem 3.2 (Dual-Certified Exclusions of Marked $\mathrm{H24\_306763}$ at Orders $43$ and $42$):** For the marked $(K_4, I_5)$-free graph $\mathrm{H24\_306763}$ on $n_A = 24$ vertices ($8$ regular $K_3$-orbits, $129$ edges, $t(A) = 164$ red triangles, explicitly related to its raw `graph6` catalogue entry by the vertex bijection $\pi$ in Section 3.1) glued against an unknown $18$-vertex partner $B_{18}$ on $6$ regular $C_3$-orbits:
   - **Order $43$ ($84 / 84$ unsplit Row-$0$ cubes):** Normalizing Row $0$ ($O_0^A$) under the partner wreath group $W_6 = S_6 \ltimes C_3^6$ (order $524{,}880$) partitions all $2^{18} = 262{,}144$ Row-$0$ patterns into $\binom{6+4-1}{6} = 84$ non-decreasing Row-$0$ weight multisets $w_0 \in \{0,1,2,3\}^6$. All $84$ unsplit cubes are certified UNSAT both locally (`PicoSAT 965` + `StandaloneTraceCheckVerifier`) and by independent external validation (`u/teichmuller_lift`, `CaDiCaL --lrat` + `lrat-check` [13]).
   - **Order $42$ ($644 / 644$ canonical cases across an unconditional tautology cover):** Deleting $v_\infty$ ($42 = 24 + 18$ vertices), we partition the partner space unconditionally according to whether $B_{18}$ contains an orbit-aligned **type-$(3,1)$ blue $I_4$ witness** (three vertices forming a blue $I_3$-orbit $O_{q_1}^B$ together with one vertex in another regular orbit $O_{q_2}^B$ completely blue-joined to $O_{q_1}^B$): **Family A** ($560$ canonical Row-$0$ cases under the stabilizer $H_{(3,1)} = (\{0\} \times \{1\} \times S_{\{2,3,4,5\}}) \ltimes C_3^6$ of order $17{,}496$ of the four-unit witness constraint) and **Family B** ($84$ canonical Row-$0$ cubes with all $30$ orbit-level type-$(3,1)$ $I_4$ clauses adjoined, invariant under $W_6$). All $644$ cases were certified UNSAT locally ($631$ unsplit cases $+ 13$ cases split into $132$ Row-$1$ truth-table leaves $= 763$ original jobs via `PicoSAT 965` + `StandaloneTraceCheckVerifier`) and independently externally validated by `u/teichmuller_lift` ($759$ direct checks $+ 32$ sign-cube leaves on variables $28, 29, 30$ replacing the $4$ capped Family A parents `id 237, 366, 376, 520` via `CaDiCaL --lrat` + `lrat-check`).

2. **Theorem 4.1 (Dual-Certified Complete Order-$43$ Exclusion of Marked $A_{21}$) and Proposition 4.3 (Locally Proof-Checked Conditional Order-$42$ Family P Exclusion of Marked $A_{21}$):** For the vertex-transitive $(K_4, I_5)$-free circulant $A_{21} = \operatorname{Cay}(\mathbb{Z}_{21}, \pm\{2,3,5,6\})$ on $n_A = 21$ vertices ($7$ regular $I_3$-orbits, $84$ edges, $t(A_{21}) = 63$ red triangles, $147$ independent $4$-sets) glued against an unknown $21$-vertex partner $B_{21}$ on $7$ regular $C_3$-orbits:
   - **Order $43$ ($392$ local leaves / $399$ external terminal leaves across $105$ canonical Row-$0$ cubes `#0..#104` — Dual-Certified):** We prove complete exclusion via three components, certified both locally (`PicoSAT 965` + `StandaloneTraceCheckVerifier`) and by independent external validation (`u/teichmuller_lift`, `CaDiCaL 1.9.5 --lrat` + `lrat-check`): (I) **Family Z ($84 / 84$ cubes `#0..#83`, $168$ local leaves)** eliminates every completion containing a weight-$0$ block ($w_{p,q} = 0$), restricting any putative completion to strictly positive weights $\mathcal{M}_+ = \{1,2,3\}^{7 \times 7}$; (II) a **Positive-Weight Conservation Bound** combining the triangle double count $3 \sum_{q=0}^6 t_A(S_q) \leq \alpha(B_{21})\,t(A_{21})$ ($\sum_{q=0}^6 t_A(S_q) \leq 63$ at Order $43$) with the computed $2{,}186$-profile positive cone table of $A_{21}$ proves that any positive completion satisfies $U(M) = \sum_{p,q} \mathbf{1}_{w_{p,q}=1} \geq 10$ and $U(M) - W_3(M) \geq 6$, forcing some row to have $\geq 2$ ones; and (III) the **21-Row Maximum-Ones Cover ($21 / 21$ cubes `#84..#104`, $224$ leaves)** refutes all $21$ canonical positive-weight Row-$0$ multisets with $n_{w_0}(1) \geq 2$ without any $W_3(M) = 0$ restriction.
   - **Order $42$ ($8 / 8$ canonical Family P Row-$0$ cubes: $56$ locally verified leaves across $7$ cubes `#84, #85, #87, #90, #94, #99, #105` + analytical exclusion of `#112_2222222` — Locally Proof-Checked Only):** Under the conditional hypothesis $M \in \{1,2\}^{7 \times 7}$ (**Family P**), we exclude all $8$ canonical Row-$0$ multisets at Order $42$ via local `PicoSAT 965` + `StandaloneTraceCheckVerifier` refutations. Outside Family P, the full Order-$42$ question for $A_{21}$ remains open.

![Positive-profile triangle envelope of A21 and 7-column conservation relaxation feasible region at Orders 43 and 42](supplement/figure-1.png)

**Figure 1.** *(a)* Lower red-cone triangle envelope $\underline{t}_+(v_1, v_3)$ across the $2{,}186$ locally admissible positive column weight profiles $w \in \{1,2,3\}^7$ of $A_{21}$ as a function of $v_1(w) = n_w(1) \in \{0,\dots,6\}$ for $v_3(w) = n_w(3) \in \{0,1,2,3\}$, together with the marginal envelope $\underline{t}_+(v_1) = (14,10,7,6,7,8,9)$ (note the non-monotonicity in $v_3$ at $v_1 = 4$, where $\underline{t}_+(4,0) = 8 > \underline{t}_+(4,2) = 7$; profile `1111111` at $v_1 = 7$ is inadmissible). *(b)* Exact feasible region of the **$7$-column triangle-budget relaxation** $\sum_{q=0}^6 \underline{t}_+(v_{1,q}, v_{3,q}) \leq 21\,\alpha(B_{21})$ in the $(U(M), W_3(M))$ plane at Order $43$ ($\leq 63$, blue circles: $U(M) \geq 10$ and $U(M) - W_3(M) \geq 6$, forcing $\max_p n_{w_p}(1) \geq \lceil 10/7 \rceil = 2$) and at Order $42$ ($\leq 84$, orange squares: $U(M) \geq 4$ and $U(M) - W_3(M) \geq 0$). Plotted points represent 7-column budget-relaxation feasibility over locally admissible column profiles, not demonstrated $(5,5)$-free graph completions (Theorem 4.1 refutes all Order-$43$ completions and Proposition 4.3 refutes all Order-$42$ $W_3(M)=0$ completions). Exact values appear in Table 1.

---

## 2. Related Work, Encoding, and General vs. Source-Specific Counting Principles

### 2.1 Methodological Precedents and Verification Attribution

Neighbourhood gluing, subgraph double-counting identities, wreath-group coordinate normalization, and cube-and-conquer SAT refutations follow the established methodology of McKay and Radziszowski [2, 12], Angeltveit and McKay [3, 4], and Heule, Kullmann, and Marek [13]. Throughout this paper, we maintain an explicit distinction between:
- **Independently Externally Validated (Dual-Certified) Results:** Theorems 3.1 and 3.2 on $\mathrm{H24\_306763}$ at Orders $43$ and $42$, and Theorem 4.1 on $A_{21}$ at Order $43$, each of which was solved and verified locally using `PicoSAT 965` (`picosat_write_extended_trace`) + `StandaloneTraceCheckVerifier` **and** independently reconstructed from first principles and verified with `CaDiCaL --lrat` + `lrat-check` by `u/teichmuller_lift` (`r/ramsey_5_5/post/6`, Comments `fWvd3d3LP0AUrUzA`, `1v_JBt6OH_SIY0Pe`, and `V7OQlV_mh49Uivo5`, archived in `supplement/external_validation/`).
- **Locally Proof-Checked Results:** Proposition 4.3 on $A_{21}$ in the conditional Order-$42$ Family P regime ($M \in \{1,2\}^{7 \times 7}$, $56$ leaves across $7$ cubes `#84, #85, #87, #90, #94, #99, #105` + analytic exclusion of `#112_2222222`), which lay outside `u/teichmuller_lift`'s Priority Order-$43$ validation scope and was verified locally using `PicoSAT 965` + `StandaloneTraceCheckVerifier` (`supplement/verify_dimacs_picosat_tracecheck.cpp`) together with the internal formula, symmetry, cone-table, partition, and SHA-256 checks in `generate_a21_order43_and_famP42_handoff.cpp`.

**Acknowledgments.** We thank `u/teichmuller_lift` for his independent clean-room reconstructions and `CaDiCaL --lrat` + `lrat-check` external validations of the Order-$43$ and Order-$42$ exclusions of $\mathrm{H24\_306763}$ and the complete Order-$43$ exclusion of $A_{21}$, and `u/vesper_ash` for research supervision and technical review of the conservation argument, stabilizer reductions, and verification audit trail.

### 2.2 Equivariant Propositional Encoding (`base42` and `base43`)

Label the vertices of each regular $A$-orbit $O_p^A$ as $(p, x)$ ($p \in \{0,\dots,r_A-1\},\, x \in \mathbb{Z}_3$) and those of each regular $B$-orbit $O_q^B$ as $(q, y)$ ($q \in \{0,\dots,r_B-1\},\, y \in \mathbb{Z}_3$), with $\sigma(p, x) = (p, x+1 \bmod 3)$ and $\sigma(q, y) = (q, y+1 \bmod 3)$:
1. **Cross-edges $M \in \{0,1\}^{V(A) \times V(B)}$:** Each $3 \times 3$ block $M_{p,q}$ between $O_p^A$ and $O_q^B$ is a circulant matrix determined by three boolean variables $m(p, q, d) \in \{0,1\}$ ($d \in \{0,1,2\}$), where the cross-edge between $(p, x) \in O_p^A$ and $(q, y) \in O_q^B$ has value $m(p, q, (y - x) \bmod 3)$ ($3 r_A r_B$ cross-edge variables: $144$ for $8 \times 6$ and $147$ for $7 \times 7$). Its **block weight** is
   $$
   w_{p,q} := m(p,q,0) + m(p,q,1) + m(p,q,2) \in \{0,1,2,3\}.
   $$
   Up to cyclic shift of $O_q^B$, each weight $w \in \{0,1,2,3\}$ has a unique canonical bit-pattern $(m(p,q,0), m(p,q,1), m(p,q,2)) = (\mathbf{1}_{d \geq 3-w})_{d=0,1,2}$, namely $(0,0,0)$, $(0,0,1)$, $(0,1,1)$, and $(1,1,1)$.
2. **Partner edges on $B$:** Each regular orbit $O_q^B$ is either a red triangle ($B[O_q^B] \cong K_3$, $b_{\mathrm{intra}}(q) = 1$) or a blue independent triple ($B[O_q^B] \cong I_3$, $b_{\mathrm{intra}}(q) = 0$) ($r_B$ intra-orbit variables), and each pair of distinct orbits $q < q'$ has a $3 \times 3$ circulant adjacency block parameterized by $b_{\mathrm{inter}}(q, q', d) \in \{0,1\}$ for $d \in \{0,1,2\}$ ($3 \binom{r_B}{2}$ inter-orbit variables). The total number of primary boolean variables is $144 + 45 + 6 = 195$ for $\mathrm{H24\_306763}$ ($8 \times 6$) and $147 + 63 + 7 = 217$ for $A_{21}$ ($7 \times 7$).

For a fixed $(K_4, I_5)$-free source $A$, the glued graph $G$ is $(5,5)$-free if and only if $(B, M)$ satisfies:
- **At Order $42$ (`base42`):** Pure-$B$ $K_5$-freeness (`set_BK5`) and $I_5$-freeness (`set_BI5`), mixed red $K_5$ avoidance across $K_r \subseteq A$ and $K_{5-r} \subseteq B$ for $r \in \{1,2,3\}$ (`set_r14`, `set_r23`, `set_r32`, since $\omega(A) \leq 3$), and mixed blue $I_5$ avoidance across $I_r \subseteq A$ and $I_{5-r} \subseteq B$ for $r \in \{1,2,3,4\}$ (`set_b14`, `set_b23`, `set_b32`, `set_b41`, since $\alpha(A) \leq 4$).
- **At Order $43$ (`base43`):** Adjoining the apex $v_\infty$ (red to $A$, blue to $B$) adds pure-$B$ $I_4$-freeness (`set_BI4`, since $B = N_B(v_\infty)$ cannot contain a blue $I_4$), which subsumes `set_BI5` and `set_b14` (while $A = N_R(v_\infty)$ is already $K_4$-free).

### 2.3 General Single-Column Cone, Polarity, and Triangle Double-Count Lemmas

Let $A$ be any $\sigma$-invariant $(K_4, I_5)$-free graph on $r_A$ regular $C_3$-orbits $O_0^A, \dots, O_{r_A-1}^A$, glued to a $\sigma$-invariant partner $B$ on $r_B$ regular $C_3$-orbits $O_0^B, \dots, O_{r_B-1}^B$. Fix a partner column $O_q^B$ and let $b = (q, 0) \in O_q^B$. Let
$$
S = N_R(b) \cap V(A), \qquad T = V(A) \setminus S = N_B(b) \cap V(A)
$$
be the red and blue cones of $b$ in $A$. By $\sigma$-equivariance, the three vertices $(q,0), (q,1), (q,2)$ of $O_q^B$ have red cones $S, \sigma(S), \sigma^2(S)$ and blue cones $T, \sigma(T), \sigma^2(T)$, and the block weight on row $p$ is $w_{p,q} = |S \cap O_p^A| \in \{0,1,2,3\}$.

**Lemma 2.1 (Single-Column Local Admissibility Conditions).** *In any $(5,5)$-free gluing of $(A, B)$:*
1. *Single-vertex condition (Mixed $(4,1)$): Because $\omega(A) \leq 3$, $S$ automatically contains no red $K_4$. To avoid a mixed $(4,1)$ blue $I_5 = I_4 \cup \{b\}$, the blue cone $T = V(A) \setminus S$ must be $I_4$-free.*
2. *Red partner orbit condition (`ok_K3`, when $B[O_q^B] \cong K_3$):*
   - *To avoid a mixed $(3,2)$ red $K_5$ formed by a red triangle in $A$ and a red edge $\{(q,0), (q,1)\} \in E(B)$, the pairwise red-cone intersection $S \cap \sigma(S)$ must be $K_3$-free.*
   - *To avoid a mixed $(2,3)$ red $K_5$ formed by a red edge in $A$ and the red triangle $O_q^B \cong K_3$, the triple red-cone intersection*
     $$
     S \cap \sigma(S) \cap \sigma^2(S) = \bigcup_{p : w_{p,q} = 3} O_p^A
     $$
     *must be $K_2$-free (an independent set in $A$).*
3. *Blue partner orbit condition (`ok_I3`, when $B[O_q^B] \cong I_3$):*
   - *To avoid a mixed $(3,2)$ blue $I_5$ formed by a blue $I_3 \subseteq A$ and a blue non-edge $\{(q,0), (q,1)\}$ in $O_q^B$, the pairwise blue-cone intersection $T \cap \sigma(T)$ must be $I_3$-free.*
   - *To avoid a mixed $(2,3)$ blue $I_5$ formed by a blue non-edge in $A$ and the blue independent triple $O_q^B \cong I_3$, the triple blue-cone intersection*
     $$
     T \cap \sigma(T) \cap \sigma^2(T) = \bigcup_{p : w_{p,q} = 0} O_p^A
     $$
     *must be $I_2$-free (a red clique in $A$).*

*A weight profile $w_{\cdot,q} \in \{0,1,2,3\}^{r_A}$ is locally admissible if there exists $S \subseteq V(A)$ with $|S \cap O_p^A| = w_{p,q}$ satisfying (1) and at least one of (2) ($\operatorname{adm}_{K_3}(w_{\cdot,q}) = 1$) or (3) ($\operatorname{adm}_{I_3}(w_{\cdot,q}) = 1$).*

**Corollary 2.2 (General Full-Join and Zero-Join Orbit Polarity Restrictions).** *Let $v_k(w_{\cdot,q}) := |\{p : w_{p,q} = k\}|$ for $k \in \{0,1,2,3\}$.*
1. *Red-orbit restrictions on $w_{p,q} = 3$: By Lemma 2.1(2), if $B[O_q^B] \cong K_3$, then $\bigcup_{p : w_{p,q}=3} O_p^A$ is an independent set of size $3\,v_3(w_{\cdot,q})$ in $A$.*
   - *Occupied-row restriction: If a specific row $p$ satisfies $O_p^A \cong K_3$ in $A$ and $w_{p,q} = 3$, then $O_p^A \subseteq \bigcup_{p' : w_{p',q}=3} O_{p'}^A$ contains red edges, which is impossible when $B[O_q^B] \cong K_3$. Thus $w_{p,q} = 3$ on a $K_3$-row $p$ forbids a red partner orbit ($\operatorname{adm}_{K_3}(w_{\cdot,q}) = 0$). In particular, if every row of $A$ is a $K_3$-orbit (as in $\mathrm{H24\_306763}$), then $v_3(w_{\cdot,q}) \geq 1 \implies \operatorname{adm}_{K_3}(w_{\cdot,q}) = 0$.*
   - *Unrestricted two-row restriction: For any $(K_4, I_5)$-free graph $A$, $\alpha(A) \leq 4 < 6$, so two full orbits ($6$ vertices) cannot be independent in $A$. Hence for every $(K_4, I_5)$-free source $A$, $v_3(w_{\cdot,q}) \geq 2 \implies \operatorname{adm}_{K_3}(w_{\cdot,q}) = 0$.*
2. *Blue-orbit restrictions on $w_{p,q} = 0$: Dually, by Lemma 2.1(3), if $B[O_q^B] \cong I_3$, then $\bigcup_{p : w_{p,q}=0} O_p^A$ is a clique of size $3\,v_0(w_{\cdot,q})$ in $A$.*
   - *Occupied-row restriction: If a specific row $p$ satisfies $O_p^A \cong I_3$ in $A$ and $w_{p,q} = 0$, then $O_p^A \subseteq \bigcup_{p' : w_{p',q}=0} O_{p'}^A$ contains blue non-edges, which is impossible when $B[O_q^B] \cong I_3$. Thus $w_{p,q} = 0$ on an $I_3$-row $p$ forbids a blue partner orbit ($\operatorname{adm}_{I_3}(w_{\cdot,q}) = 0$). In particular, if every row of $A$ is an $I_3$-orbit (as in $A_{21}$), then $v_0(w_{\cdot,q}) \geq 1 \implies \operatorname{adm}_{I_3}(w_{\cdot,q}) = 0$.*
   - *Unrestricted two-row restriction: For any $(K_4, I_5)$-free graph $A$, $\omega(A) \leq 3 < 6$, so for every $(K_4, I_5)$-free source $A$, $v_0(w_{\cdot,q}) \geq 2 \implies \operatorname{adm}_{I_3}(w_{\cdot,q}) = 0$.*

**Lemma 2.3 (Triangle Budget Double Count).** *Let $A$ be any $\sigma$-invariant $(K_4, I_5)$-free graph with $t(A)$ red triangles, glued to a $\sigma$-invariant partner $B$ on $r_B$ regular $C_3$-orbits $O_0^B, \dots, O_{r_B-1}^B$ with independence number $\alpha(B)$. For each column $q \in \{0, \dots, r_B-1\}$, let $S_q = N_R(q, 0) \cap V(A)$ and let $t_A(S_q)$ denote the number of red triangles of $A$ contained in $S_q$. Then in any $(5,5)$-free completion:*
$$
3 \sum_{q=0}^{r_B-1} t_A(S_q) \leq \alpha(B) \cdot t(A).
$$

*Proof.* For each red triangle $\Delta \subseteq A$, let $C_B(\Delta) := \{b \in V(B) : \Delta \subseteq N_R(b)\}$ be the set of common red neighbours of $\Delta$ in $B$. If $C_B(\Delta)$ contained a red edge $\{b_1, b_2\} \in E(B)$, then $\Delta \cup \{b_1, b_2\}$ would form a mixed $(3,2)$ red $K_5$. Therefore, $C_B(\Delta)$ is an independent set in $B$, so $|C_B(\Delta)| \leq \alpha(B)$. Since the three vertices of $O_q^B$ have $\sigma$-congruent cones $S_q, \sigma(S_q), \sigma^2(S_q)$ in $A$ and $\sigma \in \operatorname{Aut}(A)$, each vertex of $O_q^B$ contains $t_A(S_q)$ triangles of $A$ in its red cone. Double-counting pairs $(\Delta, b) \in \mathcal{T}(A) \times V(B)$ with $\Delta \subseteq N_R(b)$ yields
$$
3 \sum_{q=0}^{r_B-1} t_A(S_q) = \sum_{b \in V(B)} t_A(N_R(b) \cap V(A)) = \sum_{\Delta \in \mathcal{T}(A)} |C_B(\Delta)| \leq \alpha(B) \cdot t(A). \quad \square
$$

When $t(A) = 63$ (as for $A = A_{21}$), dividing by $3$ gives:
$$
\sum_{q=0}^{r_B-1} t_A(S_q) \leq 21\,\alpha(B) = \begin{cases} 63 & \text{at Order } 43 \text{ } (\alpha(B) \leq 3), \\ 84 & \text{at Order } 42 \text{ } (\alpha(B) \leq 4). \end{cases}
$$

### 2.4 Computed Cone Profile Table for $A_{21}$ (`a21_admissible_column_wcodes.tsv`)

For the specific source $A_{21} = \operatorname{Cay}(\mathbb{Z}_{21}, \pm\{2,3,5,6\})$ ($21$ vertices, $84$ edges, $t(A_{21}) = 63$ triangles, $147$ independent $4$-sets, $7$ regular $I_3$-orbits $O_p^A = \{p, p+7, p+14\}$), converting Lemma 2.3 into a lower bound on the number of weight-$1$ entries $U(M) = \sum_{p,q} \mathbf{1}_{w_{p,q}=1}$ relies on the exhaustive enumeration of all $2^{21} = 2{,}097{,}152$ subsets $S \subseteq V(A_{21})$ under Lemma 2.1 (`generate_a21_order43_and_famP42_handoff.cpp`, archived in `a21_admissible_column_wcodes.tsv` and independently reproduced by both the referee and `u/teichmuller_lift`):

1. **Admissible Profile Counts:** Out of all $4^7 = 16{,}384$ weight vectors $w \in \{0,1,2,3\}^7$, **$2{,}914$ profiles are locally admissible**. Out of the $3^7 = 2{,}187$ strictly positive weight vectors $w \in \{1,2,3\}^7$, **$2{,}186$ profiles are locally admissible**: the **unique inadmissible positive profile is `1111111`** ($v_1(w) = 7$, for which every complement $T = A_{21} \setminus S$ of size $14$ contains a blue $I_4$). By contrast, $S = V(A_{21})$ with profile `3333333` is locally admissible for a blue partner orbit (`adm_flags = 2`, `min_tA = 63`, since $T = \emptyset$). Out of the $2^7 = 128$ pure-$\{1,2\}$ vectors $w \in \{1,2\}^7$, **$127$ profiles are admissible** (all except `1111111`).
2. **Table-Verified Polarity Property $\operatorname{adm}_{K_3}(v_1 = 0) = 0$:** While $\operatorname{adm}_{K_3}(v_3 \geq 2) = 0$ holds universally by Corollary 2.2(1), the fact that **all $128$ positive profiles with $v_1(w) = 0$ ($w \in \{2,3\}^7$) satisfy $\operatorname{adm}_{K_3}(w) = 0$** (`adm_flags = 2`) is a specific property of $A_{21}$ established by the enumeration.
3. **Exact 2D Lower Triangle Table $\underline{t}_+(v_1, v_3)$ and Marginal Envelope $\underline{t}_+(v_1)$:** Grouping the $2{,}186$ admissible positive profiles by $(v_1, v_3) = (n_w(1), n_w(3))$ gives the exact 2D minimum table $\underline{t}_+(v_1, v_3)$ and marginal minimum $\underline{t}_+(v_1) = \min_{v_3} \underline{t}_+(v_1, v_3)$ in Table 1.

| $v_1(w)$ | Positive Profiles | $\operatorname{adm}_{K_3}$ Profiles | Marginal $\underline{t}_+(v_1)$ | Exact 2D Minimum $\underline{t}_+(v_1, v_3)$ from `a21_admissible_column_wcodes.tsv` |
|---:|---:|---:|---:|---|
| $0$ | $128$ | $0$ | **$14$** | $(0,0): 14,\; (0,1): 17,\; (0,2): 22,\; (0,3): 29,\; (0,4): 36,\; (0,5): 45,\; (0,6): 54,\; (0,7): 63$ |
| $1$ | $448$ | $35$ | **$10$** | $(1,0): 10,\; (1,1): 12,\; (1,2): 16,\; (1,3): 22,\; (1,4): 28,\; (1,5): 36,\; (1,6): 45$ |
| $2$ | $672$ | $119$ | **$7$** | $(2,0): 7,\; (2,1): 8,\; (2,2): 12,\; (2,3): 16,\; (2,4): 20,\; (2,5): 28$ |
| $3$ | $560$ | $175$ | **$6$** | $(3,0): 6,\; (3,1): 7,\; (3,2): 8,\; (3,3): 12,\; (3,4): 17$ |
| $4$ | $280$ | $140$ | **$7$** | **$(4,0): 8,\; (4,1): 8,\; (4,2): 7,\; (4,3): 11$** *(not monotone in $v_3$)* |
| $5$ | $84$ | $63$ | **$8$** | $(5,0): 8,\; (5,1): 8,\; (5,2): 10$ |
| $6$ | $14$ | $14$ | **$9$** | $(6,0): 9,\; (6,1): 9$ |
| $7$ | $0$ | $0$ | $\infty$ | `1111111` is inadmissible |

**Table 1.** Exact positive-profile counts, $\operatorname{adm}_{K_3}$ counts, marginal lower triangle envelope $\underline{t}_+(v_1)$, and 2D minimum red-cone triangle table $\underline{t}_+(v_1, v_3)$ across all $2{,}186$ locally admissible positive column profiles of $A_{21}$.

---

## 3. Dual-Certified Exclusions of Marked $\mathrm{H24\_306763}$ at Orders $43$ and $42$

### 3.1 Explicit Relabeling Between the Raw `graph6` Entry and `H24_306763_MARKED_ADJ`

Let $G_{\mathrm{raw}}$ be the $24$-vertex $(K_4, I_5)$-free graph ($129$ edges, $164$ red triangles) decoded in standard upper-triangle column-major order from line $306{,}763$ ($0$-indexed) of the $(4,5,24)$ catalogue `r45_24.g6`:
```text
WtTk?KQOxF@NdpwdP{ESoiFmXdo|MbS^@dhULUTahtQmMTK
```
In raw `graph6` vertex coordinates $v \in \{0,\dots,23\}$, vertices $\{0,1,2\}$ do not form a triangle; rather, the marked order-$3$ automorphism $\sigma_{\mathrm{raw}} \in \operatorname{Aut}(G_{\mathrm{raw}})$ (`sA` in `selected_noncirculant_A24_for_teichmuller.json`) is the permutation
$$
\sigma_{\mathrm{raw}} = [2, 5, 3, 0, 1, 4, 10, 11, 6, 7, 8, 9, 16, 21, 19, 20, 23, 13, 15, 22, 18, 17, 14, 12].
$$
To obtain contiguous orbit-phase coordinates $i = 3p + x \in \{0,\dots,23\}$ ($p \in \{0,\dots,7\},\, x \in \{0,1,2\}$) on which the marked action is $\sigma_A(3p + x) = 3p + ((x + 1) \bmod 3)$, `extract_k3_8_order3_blocks_from_sg` partitions $\{0,\dots,23\}$ by increasing vertex-invariant bucket $(\deg(v), \operatorname{tri}(v))$—namely $(10,17): \{0,1,2,3,4,5\}$, $(11,21): \{12,14,16,19,22,23\}$, and $(11,22): \{6,7,8,9,10,11,13,15,17,18,20,21\}$—and orders the $8$ directed $3$-cycles of $\sigma_{\mathrm{raw}}$ as:
$$
\begin{aligned}
O_0^A &= (0, 2, 3), & O_1^A &= (1, 5, 4), & O_2^A &= (12, 16, 23), & O_3^A &= (14, 19, 22), \\
O_4^A &= (6, 10, 8), & O_5^A &= (7, 11, 9), & O_6^A &= (13, 21, 17), & O_7^A &= (15, 20, 18).
\end{aligned}
$$
This defines the explicit relabeling bijection $\pi : \{0,\dots,23\}_{\mathrm{marked}} \to \{0,\dots,23\}_{\mathrm{raw}}$:
$$
\pi = [0, 2, 3,\; 1, 5, 4,\; 12, 16, 23,\; 14, 19, 22,\; 6, 10, 8,\; 7, 11, 9,\; 13, 21, 17,\; 15, 20, 18].
$$
Under $\pi$, $\pi(\sigma_A(i)) = \sigma_{\mathrm{raw}}(\pi(i))$ for all $i \in \{0,\dots,23\}$, every contiguous triple $\{3p, 3p+1, 3p+2\}$ induces a red triangle $K_3$, and the pullback of $E(G_{\mathrm{raw}})$ along $\pi$ (`{i, j} in E_marked iff {pi(i), pi(j)} in E(G_raw)`) reproduces the bitmask array `H24_306763_MARKED_ADJ[0..23]` in `generate_h24_306763_84cubes.cpp` and `generate_h24_306763_order42_644cases.cpp` bit-for-bit (verified by `verify_h24_306763_relabeling.py` in `supplement/`).

### 3.2 Order-$43$ Exclusion ($84 / 84$ Unsplit Row-$0$ Cubes — Dual-Certified)

At Order $43$ ($43 = 1 + 24 + 18$), `base43` ($126{,}843$ clauses on $195$ variables, verified directly in `generate_h24_306763_84cubes.cpp` to be logically equivalent by apex subsumption to the full $154{,}149$-clause $\binom{43}{5} = 962{,}598$ hypergraph encoding) is invariant under the partner wreath group $W_6 = S_6 \ltimes C_3^6$ of order $6! \cdot 3^6 = 524{,}880$ permuting and shifting the $6$ exchangeable $B_{18}$-orbits $O_0^B, \dots, O_5^B$. Normalizing **Row $0$** ($O_0^A$) under $W_6$ partitions all $2^{18} = 262{,}144$ binary Row-$0$ patterns into the $\binom{6+4-1}{6} = 84$ non-decreasing Row-$0$ weight multisets $w_0 = (w_{0,0} \leq w_{0,1} \leq \dots \leq w_{0,5}) \in \{0,1,2,3\}^6$, with Row-$1$ residual stabilizer clauses `row1_stab` breaking $H(w_0) \leq W_6$ on Row $1$. Because $O_0^A \cong K_3$, all $35$ cubes with $n_{w_0}(3) \geq 2$ ($w_{0,4} = w_{0,5} = 3$) contain an explicit $11$-clause Minimal Unsatisfiable Subset ($6$ Row-$0$ units $+ 4$ mixed $(3,2)$ red clauses $+ 1$ apex blue $I_4(B_{18})$ clause) that resolves to $\emptyset$ in $5$ steps (verified directly inside `generate_h24_306763_84cubes.cpp`).

**Theorem 3.1 (Order-$43$ Exclusion of Marked $\mathrm{H24\_306763}$).** *The marked $(K_4, I_5)$-free graph $\mathrm{H24\_306763}$ admits no $C_3$-equivariant $(5,5)$-free completion $(B_{18}, M)$ at Order $43$.*

*Proof and Dual Verification.* All $84$ unsplit Row-$0$ cubes were solved and proof-checked by two independent pipelines:
1. **External Validation (`u/teichmuller_lift`, `external_validation/h24_order43_teichmuller/`):** Independently verified the $\binom{43}{5}$ clause-set equivalence in Python (`r55rebuild.py`), generated all $84$ CNFs from `generate_h24_306763_84cubes.cpp` with exact SHA-256 match, and certified $84 / 84$ UNSAT using `CaDiCaL --lrat` + `lrat-check` ($1{,}131.6\text{ s}$ solve $+ 119.6\text{ s}$ check).
2. **Local Cross-Check (`drivers/certify_84cubes_picosat_tracecheck.cpp`):** Solved all $84$ unsplit cubes with `PicoSAT 965` and verified all $84$ extended-resolution traces with `StandaloneTraceCheckVerifier` ($913.9\text{ s}$ solve $+ 146.0\text{ s}$ check, logged in `retained_local_records/h24_306763_84cubes_cert_summary.json`). $\square$

### 3.3 Order-$42$ Exclusion ($644 / 644$ Cases Across Tautology Cover — Dual-Certified)

At Order $42$, deleting the apex $v_\infty$ leaves $V(G) = V(\mathrm{H24\_306763}) \sqcup V(B_{18})$ on $42 = 24 + 18$ vertices (`base42.cnf`, $153{,}174$ clauses on $195$ variables). In $B_{18}$ ($6$ regular $C_3$-orbits), an orbit-aligned **type-$(3,1)$ blue $I_4$ witness** consists of three vertices forming a single blue $I_3$-orbit $O_{q_1}^B$ together with a fourth vertex $(q_2, y) \in O_{q_2}^B$ ($q_2 \neq q_1$) in another regular $B$-orbit that is completely blue-joined to $O_{q_1}^B$.

There are $6 \times 5 \times 3 = 90$ such pointed $4$-vertex subsets $O_{q_1}^B \cup \{(q_2, y)\}$ in $B_{18}$, and the stabilizer in $W_6$ (order $524{,}880$) of a particular pointed $4$-set $O_0^B \cup \{(1, 0)\}$ has order $524{,}880 / 90 = 5{,}832$ (since rotating $O_1^B$ moves $(1,0)$ to $(1,1)$ or $(1,2)$). Crucially, however, under $\sigma$-equivariance all three choices of the fourth vertex $(1, y) \in O_1^B$ ($y \in \{0,1,2\}$) impose the **exact same four-unit witness constraint** `units_Q31`:
$$
b_{\mathrm{intra}}(0) = 0 \qquad \text{and} \qquad b_{\mathrm{inter}}(0, 1, d) = 0 \quad (d \in \{0,1,2\}).
$$
Consequently, the $90$ pointed $4$-sets collapse to **$30$ distinct length-$4$ clauses** (`clauses_no_31.cnf`, one for each ordered pair $(q_1, q_2)$ of distinct $B$-orbits), on which $W_6$ acts transitively. The stabilizer in $W_6$ of the four-unit witness constraint `units_Q31` (preserving the ordered pair of orbits $(O_0^B, O_1^B)$ while allowing all $C_3^6$ shifts, including the $3$ cyclic shifts of $O_1^B$) is therefore the larger group
$$
H_{(3,1)} = (\{0\} \times \{1\} \times S_{\{2,3,4,5\}}) \ltimes C_3^6 \leq W_6, \qquad |H_{(3,1)}| = \frac{524{,}880}{30} = 17{,}496 = 3 \times 5{,}832.
$$

We partition the entire Order-$42$ space $(B_{18}, M)$ by the unconditional tautology of whether $B_{18}$ satisfies at least one of the $30$ four-unit type-$(3,1)$ witness constraints (so the Order-$42$ exclusion is self-contained and does not depend on Theorem 3.1):
1. **Family A ($560$ canonical cases, $B_{18}$ contains a type-$(3,1)$ witness):** Gauge-fixing `units_Q31` on $(O_0^B, O_1^B)$, the constraint stabilizer $H_{(3,1)}$ of order $17{,}496$ partitions the $2^{18}$ Row-$0$ patterns into $4 \times 4 \times \binom{4+4-1}{4} = 560$ canonical Row-$0$ cases $w_0 = (w_{0,0},\, w_{0,1},\, w_{0,2} \leq w_{0,3} \leq w_{0,4} \leq w_{0,5})$ with Row-$1$ residual stabilizer clauses `row1_stab`.
2. **Family B ($84$ canonical cubes, $B_{18}$ contains no type-$(3,1)$ witness):** Adjoining all $30$ clauses of `clauses_no_31.cnf` to `base42.cnf` (`base42_no31.cnf`, $153{,}204$ clauses) preserves invariance under the full wreath group $W_6 = S_6 \ltimes C_3^6$ and reduces Row $0$ to the $84$ canonical multisets $w_0 = (w_{0,0} \leq \dots \leq w_{0,5})$.

**Theorem 3.2 (Unconditional Order-$42$ Exclusion of Marked $\mathrm{H24\_306763}$).** *The marked $(K_4, I_5)$-free graph $\mathrm{H24\_306763}$ admits no $C_3$-equivariant $(5,5)$-free completion $(B_{18}, M)$ at Order $42$.*

*Proof and Dual Verification.* In `manifest_order42_644cases.tsv` and `manifest_order42_13split_leaves.tsv`, $631$ cases are unsplit and $13$ hardest cases are split tautologically into $132$ Row-$1$ truth-table leaves ($763$ original jobs total; all $280$ cases with $n_{w_0}(3) \geq 2$ contain an explicit $12$-clause unit-propagation MUS verified directly inside `generate_h24_306763_order42_644cases.cpp`). All $763$ original jobs were certified UNSAT locally (`PicoSAT 965` + `StandaloneTraceCheckVerifier`, Appendix A.1). In his independent external validation (`external_validation/h24_order42_teichmuller/`), `u/teichmuller_lift` rebuilt `base42.cnf` ($153{,}174$ clauses) and `clauses_no_31.cnf` ($30$ clauses) from scratch, verified the $W_6$ and $H_{(3,1)}$ orbit/stabilizer covers across all Row-$0$/Row-$1$ representatives ($10{,}108{,}800$ in Family A and $475{,}020$ in Family B), and certified $759 / 763$ original jobs directly with `CaDiCaL --lrat` + `lrat-check`, plus $32 / 32$ three-variable sign-cube leaves on variables $28, 29, 30$ (`manifest_order42_ext4retry_32leaves.tsv`) replacing the $4$ unsplit Family A parents (`id 237` `FamA_B1_w01_12_w2345_1223`, `id 366` `FamA_B1_w01_22_w2345_0222`, `id 376` `FamA_B1_w01_22_w2345_1222`, and `id 520` `FamA_B1_w01_32_w2345_2222`) that reached his $600\text{ s}$ per-job cap ($14{,}412\text{ s}$ solve $+ 1{,}203\text{ s}$ check $= 4.3\text{ CPU-hours}$ total). $\square$

---

## 4. Dual-Certified Order-$43$ Exclusion and Locally Proof-Checked Conditional Order-$42$ Family P Exclusion of Marked $A_{21}$

### 4.1 The Circulant Base Graph $A_{21}$ and Verified Symmetries

Let $A_{21} = \operatorname{Cay}(\mathbb{Z}_{21}, \pm\{2,3,5,6\})$ with $\sigma(z) = z + 7 \pmod{21}$ ($21$ vertices, $84$ edges, $t(A_{21}) = 63$ red triangles, $147$ independent $4$-sets, and $7$ regular $I_3$-orbits $O_p^A = \{p, p+7, p+14\}$ for $p \in \{0,\dots,6\}$). The partner $B_{21}$ has $21$ vertices on $7$ regular $C_3$-orbits $O_0^B, \dots, O_6^B$ ($217$ primary variables; `base43_a21.cnf` has $167{,}083$ clauses and `base42_a21.cnf` has $213{,}787$ clauses, both verified in `generate_a21_order43_and_famP42_handoff.cpp` against brute-force $\binom{43}{5} = 962{,}598$ and $\binom{42}{5} = 850{,}668$ $5$-subset enumeration).

As verified directly by `generate_a21_order43_and_famP42_handoff.cpp`, both `base43_a21.cnf` and `base42_a21.cnf` are invariant under:
- The **partner wreath group $W_7 = S_7 \ltimes C_3^7$** (order $7! \cdot 3^7 = 11{,}022{,}480$) permuting and shifting the $7$ partner columns $O_0^B, \dots, O_6^B$; and
- The **verified order-$84$ affine subgroup of the normalizer**
  $$
  G_{\mathrm{aff}} = \{z \mapsto a z + b \pmod{21} : a \in \{1,8,13,20\},\, b \in \mathbb{Z}_{21}\} \leq N_{\operatorname{Aut}(A_{21})}(C_3),
  $$
  where $C_3$-reversing multipliers $a \in \{8,20\}$ ($a \equiv 2 \pmod 3$) are paired with the matching $C_3$-inversion $(q, y) \mapsto (q, 2y \bmod 3)$ on $B_{21}$.

In particular, the translations $\tau_b(z) = z + b \pmod{21}$ in $G_{\mathrm{aff}}$ act transitively on the $7$ rows $O_0^A, \dots, O_6^A$ (and translations together with $W_7$ already suffice for the row reduction below). Moving any chosen row $p^*$ to Row $0$ via $\tau$ and normalizing Row $0$ under $W_7$ places $w_0$ into one of the $\binom{7+4-1}{7} = 120$ canonical non-decreasing Row-$0$ weight multisets `#0..#119` (with $\sum_{c=0}^{119} |\operatorname{Orbit}(w_0^{(c)})| = 2^{21} = 2{,}097{,}152$), with Row-$1$ residual stabilizer clauses `row1_stab`.

### 4.2 Theorem 4.1: Complete Order-$43$ Exclusion of Marked $A_{21}$ ($392$ Local Leaves / $399$ External Leaves — Dual-Certified)

**Theorem 4.1 (Complete Order-$43$ Exclusion of Marked $A_{21}$).** *The marked $(K_4, I_5)$-free graph $A_{21} = \operatorname{Cay}(\mathbb{Z}_{21}, \pm\{2,3,5,6\})$ admits no $C_3$-equivariant $(5,5)$-free completion $(B_{21}, M)$ at Order $43$.*

The proof comprises three components (with complete per-cube split-tree inventories and provenance documented in Appendix A.2):

#### Component I: Order-$43$ Family Z ($84 / 84$ Canonical Cubes `#0..#83`, $168$ Local Leaves, `no_w0 = 0, no_w3 = 0`)
Suppose a putative Order-$43$ completion $M = (w_{p,q}) \in \{0,1,2,3\}^{7 \times 7}$ has at least one weight-$0$ entry ($w_{p^*, q^*} = 0$). Translating row $p^*$ to Row $0$ via $\tau$ and sorting columns under $W_7$ places Row $0$ into one of the **$84$ canonical Row-$0$ multisets with $n_{w_0}(0) \geq 1$ (`#0..#83`)**:
- **Tier $0$ ($56$ cubes `#0..#55` with $n_{w_0}(0) \geq 2$, $56$ unsplit leaves):** Every Tier-$0$ cube has $w_{0,0} = w_{0,1} = 0$. Since $O_0^A \cong I_3$ in $A_{21}$, $6$ Row-$0$ unit clauses ($m(0,0,0..2)=0$ and $m(0,1,0..2)=0$) together with $5$ mixed $(3,2)$ blue clauses on $O_0^A \times \mathrm{YB}_{\mathrm{canon}}[2](O_0^B \cup O_1^B)$ force all $5$ partner variables on $O_0^B \cup O_1^B$ ($b_{\mathrm{intra}}(0), b_{\mathrm{intra}}(1), b_{\mathrm{inter}}(0,1,0..2)$) to $1$, immediately falsifying the pure-partner `B_K5` clause on $O_0^B \cup O_1^B$ in **$6$ unit-propagation steps ($12$ clauses total)**.
- **Single-Zero Family Z ($28$ cubes `#56..#83` with $n_{w_0}(0) = 1$, $112$ local leaves / $119$ external leaves):** Refuted under `global_no_w0 = 0, global_no_w3 = 0` via exhaustive Row-$1$ column-mask boolean partition trees (`20` unsplit cubes + `8` split cubes totaling $112$ local leaves; in the independent external validation, `O43_Cube067_0112223` was further partitioned into $8$ sign-cube children on variables $31, 32, 33$, yielding $119$ external leaves).
- **Conclusion of Component I:** Every putative Order-$43$ completion of $(A_{21}, B_{21}, v_\infty)$ has strictly positive weights $M \in \mathcal{M}_+ = \{1,2,3\}^{7 \times 7}$.

#### Component II: Positive-Weight Conservation Bound ($U(M) \geq 10$ on $\mathcal{M}_+$)
Let $M \in \{1,2,3\}^{7 \times 7}$ be any putative positive-weight completion of $(A_{21}, B_{21})$ whose columns $w_{\cdot,0}, \dots, w_{\cdot,6}$ belong to the $2{,}186$ locally admissible positive profiles in Table 1 and satisfy the triangle double-count inequality of Lemma 2.3 ($\sum_{q=0}^6 t_A(S_q) \leq 63$ at Order $43$; $\leq 84$ at Order $42$). Define
$$
U(M) := \sum_{q=0}^6 v_1(w_{\cdot,q}) = |\{(p,q) : w_{p,q} = 1\}|, \qquad W_3(M) := \sum_{q=0}^6 v_3(w_{\cdot,q}) = |\{(p,q) : w_{p,q} = 3\}|.
$$

**Proposition 4.2 (Positive-Weight Conservation Bound for $A_{21}$).**
1. *(7-Column Marginal Relaxation at Order $43$):* Using only the marginal lower envelope $\underline{t}_+(v_1) = (14, 10, 7, 6, 7, 8, 9)$ for $v_1 \in \{0,\dots,6\}$ from Table 1, every $7$-element multiset $(v_{1,0}, \dots, v_{1,6}) \in \{0,\dots,6\}^7$ with $U(M) = \sum_{q=0}^6 v_{1,q} \leq 9$ satisfies
   $$
   \sum_{q=0}^6 \underline{t}_+(v_{1,q}) \geq 64 > 63,
   $$
   with the minimum $64$ over $U(M) \leq 9$ uniquely attained by $(v_{1,0}, \dots, v_{1,6}) = (2,2,1,1,1,1,1)$ ($2 \times 7 + 5 \times 10 = 64$).
2. *(2D Relaxation Feasible Region at Order $43$ and Order $42$):* Evaluating the $7$-column dynamic program over the exact 2D table $\underline{t}_+(v_1, v_3)$ in Table 1 (plotted as 7-column budget-relaxation feasible pairs in Figure 1(b)):
   - **At Order $43$** ($\sum_{q=0}^6 \underline{t}_+(v_{1,q}, v_{3,q}) \leq 63$): Every budget-feasible $7$-column positive profile multiset satisfies **$U(M) \geq 10$ and $U(M) - W_3(M) \geq 6$** (with $U(M) = 10$ feasible in the relaxation only for $W_3(M) \in \{0,1,2\}$).
   - **At Order $42$** ($\sum_{q=0}^6 \underline{t}_+(v_{1,q}, v_{3,q}) \leq 84$): Every budget-feasible $7$-column positive profile multiset satisfies **$U(M) \geq 4$ and $U(M) - W_3(M) \geq 0$**, and any pure $\{2,3\}$-matrix ($U(M) = 0$) requires $\geq 7 \times 14 = 98 > 84$ triangles without assuming $W_3(M) > 0$.
3. *(Row-Averaging Reduction to the 21-Row Cover at Order $43$):* Since $\sum_{p=0}^6 n_{w_p}(1) = U(M) \geq 10$ at Order $43$, some row $p^* \in \{0,\dots,6\}$ satisfies
   $$
   n_{w_{p^*}}(1) \geq \left\lceil \frac{10}{7} \right\rceil = 2.
   $$
   Translating row $p^*$ to Row $0$ via $\tau$ and normalizing columns under $W_7$ places Row $0$ into one of the **$21$ canonical positive-weight Row-$0$ multisets with $n_{w_0}(1) \geq 2$ (`#84..#104`)**.

#### Component III: Order-$43$ 21-Row Maximum-Ones Cover ($21 / 21$ Cubes `#84..#104`, $224$ Leaves)
All $21$ canonical positive-weight Row-$0$ multisets `#84..#104` are refuted across $224$ boolean-partition leaves without any $W_3(M) = 0$ restriction (`global_no_w3 = 0` on all $224$ leaves: $4$ unsplit cubes `#84, #85, #87, #90` under `no_w0 = 0, no_w3 = 0` and $17$ cubes across $220$ leaves under `no_w0 = 1, no_w3 = 0`, valid by Component I).

*Dual Verification of Theorem 4.1.* All $392$ leaves in `manifest_a21_order43_392leaves.tsv` were solved and proof-checked locally (`PicoSAT 965` + `StandaloneTraceCheckVerifier`), and independently externally validated by `u/teichmuller_lift` (`external_validation/a21_order43_teichmuller/`), who independently verified Component II, the $167{,}083$-clause $\binom{43}{5}$ equivalence, all $105$ Row-$1$ stabilizer closures, and the leaf-partition trees in Python, and certified $391 / 392$ original leaves directly plus $8 / 8$ sign-cube children on variables $31, 32, 33$ replacing `O43_Cube067_0112223.cnf` ($399 / 399$ terminal leaves certified UNSAT via `CaDiCaL 1.9.5 --lrat` + `lrat-check` in $4{,}897.9\text{ s}$ solve $+ 272.2\text{ s}$ check). $\square$

### 4.3 Proposition 4.3: Conditional Order-$42$ Family P Exclusion of Marked $A_{21}$ ($8 / 8$ Canonical Cubes — Locally Proof-Checked Only)

At Order $42$, let **Family P** denote the conditional sub-regime $\mathcal{M}_P = \{1,2\}^{7 \times 7}$ (`no_w0 = 1, no_w3 = 1`). Under $W_7$, a row in $\{1,2\}^7$ normalizes to one of the $8$ canonical Row-$0$ multisets `#84_1111111, #85_1111112, #87_1111122, #90_1111222, #94_1112222, #99_1122222, #105_1222222, #112_2222222`.

**Proposition 4.3 (Conditional Order-$42$ Family P Exclusion of Marked $A_{21}$).** *There is no $C_3$-equivariant $(5,5)$-free completion $(B_{21}, M)$ of $A_{21}$ at Order $42$ with $M \in \{1,2\}^{7 \times 7}$.*

*Proof (Locally Proof-Checked).* By Proposition 4.2(2), any completion $M \in \{1,2\}^{7 \times 7}$ at Order $42$ satisfies $U(M) \geq 4$ (so the $8$th canonical row type `#112_2222222` is covered analytically by choosing a row with $n_{w_p}(1) \geq \lceil 4/7 \rceil = 1$ and translating it to Row $0$ via $\tau$, or directly excluded if all rows are `2222222` since $7 \times 14 = 98 > 84$). The remaining $7$ canonical Row-$0$ cubes (`#84, #85, #87, #90, #94, #99, #105`) are partitioned into $56$ boolean leaves in `manifest_a21_order42_famP_56leaves.tsv` ($4$ unsplit leaves `#84, #85, #87, #90` under `no_w0 = 0, no_w3 = 0`; $1$ unsplit leaf for `#94_1112222`, $8$ leaves for `#99_1122222`, and $43$ leaves for `#105_1222222` under `no_w0 = 1, no_w3 = 1`), all $56$ of which were certified UNSAT locally via `PicoSAT 965` + `StandaloneTraceCheckVerifier` (Appendix A.3). $\square$

| Marked Source & Order | Regime / Scope | Canonical Cubes | Terminal Leaves (Local / External) | Local Verification (`PicoSAT 965` + `TraceCheck`) | Independent External Validation (`CaDiCaL --lrat` + `lrat-check`) |
|---|---|---:|---:|---|---|
| $\mathrm{H24\_306763}$, Order $43$ | Complete marked source | $84$ | $84$ / $84$ | $84 / 84$ UNSAT | **$84 / 84$ VERIFIED** (`u/teichmuller_lift`, `h24_order43_teichmuller/`) |
| $\mathrm{H24\_306763}$, Order $42$ | Complete (Family A + B) | $644$ ($560 + 84$) | $763$ / $791$ ($759 + 32$) | $763 / 763$ UNSAT | **$791 / 791$ VERIFIED** (`u/teichmuller_lift`, `h24_order42_teichmuller/`) |
| $A_{21}$, Order $43$ | Comp. I: Family Z ($n_{w_0}(0) \geq 1$) | $84$ (`#0..#83`) | $168$ / $175$ ($167 + 8$) | $168 / 168$ UNSAT | **$175 / 175$ VERIFIED** (`u/teichmuller_lift`, `a21_order43_teichmuller/`) |
| $A_{21}$, Order $43$ | Comp. III: 21-Row Cover ($n_{w_0}(1) \geq 2$) | $21$ (`#84..#104`) | $224$ / $224$ | $224 / 224$ UNSAT | **$224 / 224$ VERIFIED** (`u/teichmuller_lift`, `a21_order43_teichmuller/`) |
| $A_{21}$, Order $42$ | Conditional Family P ($M \in \{1,2\}^{7 \times 7}$) | $8$ (`#84..#105, #112`) | $56$ leaves $+ 1$ analytic | $56 / 56$ UNSAT | Outside external scope (**locally proof-checked only**) |

**Table 2.** Summary of certified covers, terminal leaf counts, and verification status across $\mathrm{H24\_306763}$ and $A_{21}$ at Orders $43$ and $42$.

---

## 5. Limitations, Open Joint-Compatibility Problem, and Reproducibility

### 5.1 Scope Limitations and the Open Joint-Compatibility Problem on Mixed $K_3/I_3$ Sources

The exclusions established in Sections 3 and 4 apply to the specific marked regular-$C_3$ sources $\mathrm{H24\_306763}$ (at Orders $43$ and $42$) and $A_{21}$ (at Order $43$, plus conditional Family P at Order $42$). They do not alter the global Ramsey bounds $43 \leq R(5,5) \leq 46$, nor do they resolve the remaining $53$ Family Z/F branches of $A_{21}$ at Order $42$.

Comparing our two opposite-polarity testbeds—$\mathrm{H24\_306763}$ (`all-K_3`, $129$ edges, $t(A)=164$ triangles, one of $30$ pure-$K_3$ actions among the $73$ marked regular-$C_3$ actions in `r45_24.g6`) and $A_{21}$ (`all-I_3`, $84$ edges, $t(A)=63$ triangles, among the $21$-vertex regular-$C_3$ sources)—with the remaining $43$ **mixed $K_3/I_3$ actions** at $n_A = 24$ highlights a well-defined open theoretical question for future work:
- Single-column cone enumeration (Lemma 2.1) and the additive triangle double count $\sum_q t_A(S_q) \leq \alpha(B)\,t(A)/3$ (Lemma 2.3) constrain each partner orbit $O_q^B$ separately and couple the columns only through scalar sums ($U(M)$ and $W_3(M)$).
- In a mixed $K_3/I_3$ regular $C_3$-source $A$, Corollary 2.2 imposes opposite occupied-row polarity restrictions within the same column $q$: weight-$3$ entries on $K_3$-rows of $A$ forbid $B[O_q^B] \cong K_3$, while weight-$0$ entries on $I_3$-rows of $A$ forbid $B[O_q^B] \cong I_3$. Furthermore, for any pair or triple of partner columns $(O_{q_1}^B, O_{q_2}^B, O_{q_3}^B)$, the mixed $(3,2)$, $(2,3)$, and $(1,4)$ clique and independent-set constraints couple the $3 \times 3$ circulant partner blocks $B_{q_i, q_j}$ directly to the pairwise and triple cone intersections $S_{q_i} \cap \sigma^d(S_{q_j})$ and $T_{q_i} \cap \sigma^d(T_{q_j})$ ($d \in \mathbb{Z}_3$).

Identifying an analytical or polyhedral joint-compatibility invariant—beyond single-column admissibility (Lemma 2.1) and the marginal triangle double count (Lemma 2.3)—that distinguishes the remaining $24$-vertex and $21$-vertex regular $C_3$-sources when partner columns are coupled without requiring a full per-source SAT cube sweep remains an open problem.

### 5.2 Reproducibility and Verification Layers in `supplement.zip`

The supplement (`supplement.zip`, documented with copy-paste commands in `supplement/README.md`) is organized into four explicit verification layers:
1. **Layer 1 — Zero-Dependency Generators, Relabeling, Cone-Table, Equivalence, and Built-In MUS Verifiers:**
   - `verify_h24_306763_relabeling.py`: Verifies the explicit vertex bijection $\pi$ between the raw `graph6` string, `sA`, and `H24_306763_MARKED_ADJ[0..23]`.
   - `generate_h24_306763_84cubes.cpp`: Verifies $\mathrm{H24\_306763}$ invariants, verifies the exact $\binom{43}{5} = 962{,}598$ hypergraph clause-set equivalence (`154,149` raw vs. `126,843` apex-subsumed clauses), verifies the explicit $11$-clause $5$-step unit-propagation MUS on all $35$ cubes with $n_{w_0}(3) \geq 2$, exports `cube_000.cnf .. cube_083.cnf`, and checks `sha256_h24_306763_84cubes.txt`.
   - `generate_h24_306763_order42_644cases.cpp`: Verifies $\binom{42}{5} = 850{,}668$ hypergraph equivalence (`153,174` clauses), verifies the $W_6$ and $H_{(3,1)}$ orbit/stabilizer covers, verifies the explicit $12$-clause unit-propagation MUS on all $280$ cases with $n_{w_0}(3) \geq 2$, exports all $644$ parent cases (`manifest_order42_644cases.tsv`), $132$ local split leaves (`manifest_order42_13split_leaves.tsv`), and (`--export-ext-4retry`) the $32$ external retry sign-cube leaves (`manifest_order42_ext4retry_32leaves.tsv`).
   - `generate_a21_order43_and_famP42_handoff.cpp`: Verifies $A_{21}$ invariants, $\binom{43}{5}$ and $\binom{42}{5}$ hypergraph equivalence, $W_7$ and $G_{\mathrm{aff}}$ symmetries, all $2^{21}$ subsets for `a21_admissible_column_wcodes.tsv`, the 7-column conservation bounds, the $56$ Tier-$0$ $12$-clause unit-propagation refutations, recursive boolean partition coverage, and `cnf_sha256` digests (`manifest_a21_order43_392leaves.tsv` and `manifest_a21_order42_famP_56leaves.tsv`), and (`--export-cnfs`) writes all $392$ Order-$43$ and $56$ Order-$42$ leaf `.cnf` files.
2. **Layer 2 — Retained Historical Record & Coverage Reconciliation (`verify_retained_proof_chains.py`):**
   - Audits and cross-reconciles the retained local solver/checker logs in `retained_local_records/` and independent external validation logs in `external_validation/` against the canonical CNF SHA-256 manifests (`84/84` Order-43 $\mathrm{H24}$, `763/763` local and `791/791` external Order-42 $\mathrm{H24}$, `392/392` local and `399/399` external Order-43 $A_{21}$, and `56/56` local Order-42 Family P $A_{21}$). As stated in `README.md` and printed by the script, this layer performs **record and digest reconciliation** (not proof replay), because raw multi-gigabyte TraceCheck and LRAT proof files were deleted immediately after verification during the historical runs.
3. **Layer 3 — End-to-End Local SAT + Extended-Resolution Proof Replay (`verify_dimacs_picosat_tracecheck.cpp`):**
   - Self-contained C++17 driver embedding `StandaloneTraceCheckVerifier` and linking against `PicoSAT 965` (`http://fmv.jku.at/picosat/picosat-965.tar.gz`, git commit `3433fe9a1baf1f7872a641e6ee1b549ddd977d86`) compiled with `./configure.sh --trace && make` (`picosat_enable_trace_generation` + `picosat_write_extended_trace`). Given any exported leaf `.cnf`, it solves the formula in memory, writes the extended-resolution trace, and verifies that the trace derives the empty clause `0` via backward chain-resolution reachability.
4. **Layer 4 — Retained Historical C++ Drivers (`drivers/`) and Independent External Validation Archives (`external_validation/`):**
   - Includes all $9$ historical C++ certification drivers (`drivers/`) and all three clean-room external validation packages from `u/teichmuller_lift` (`external_validation/h24_order43_teichmuller/`, `external_validation/h24_order42_teichmuller/`, and `external_validation/a21_order43_teichmuller/`).

---

## Appendix A. Complete Verification Audit Trail and Leaf Provenance

### A.1 $\mathrm{H24\_306763}$ Order-$43$ ($84$ Cubes) and Order-$42$ ($644$ Cases) Audit Trail

- **Order $43$ ($84$ unsplit Row-$0$ cubes):** Local certification (`drivers/certify_84cubes_picosat_tracecheck.cpp`, logged in `retained_local_records/h24_306763_84cubes_cert_summary.json` and `h24_306763_84cubes_cert_log.txt`) verified $84 / 84$ cubes UNSAT (`PicoSAT 965` + `StandaloneTraceCheckVerifier`). External validation (`external_validation/h24_order43_teichmuller/r55_verification_summary.json`) independently verified $84 / 84$ cubes UNSAT (`CaDiCaL --lrat` + `lrat-check`).
- **Order $42$ ($644$ canonical cases: $560$ Family A + $84$ Family B):**
  - **Local Certification (`763` terminal leaves):** $631$ unsplit parent cases ($280$ immediate $12$-clause MUS cases + $351$ CDCL cases across `retained_local_records/h24_order42_famA_v1_manifest.tsv`, `h24_order42_stage1_manifest.tsv`, and `h24_order42_round2_manifest.tsv`, selected from `manifest_order42_644cases.tsv` via `--exclude-split-from manifest_order42_13split_leaves.tsv`) plus $13$ split parent cases (`8` in Family A: `id 241, 367, 374, 377, 481, 497, 506, 513`; and `5` in Family B: `id 51, 66, 67, 71, 72`) partitioned into $132$ Row-$1$ truth-table leaves in `manifest_order42_13split_leaves.tsv` (`retained_local_records/h24_order42_13splits_manifest.tsv` and `h24_order42_final3_split_manifest.tsv`), totaling $631 + 132 = 763$ locally proof-checked terminal leaves.
  - **External Validation (`791` terminal leaves in `external_validation/h24_order42_teichmuller/`):** `u/teichmuller_lift` certified $759 / 763$ original jobs directly (`627 / 631` unsplit parents in `results_unsplit.tsv` + `132 / 132` split leaves in `results_split132.tsv`) and replaced the $4$ unsplit Family A parents that reached his $600\text{ s}$ cap (`id 237` `FamA_B1_w01_12_w2345_1223`, `id 366` `FamA_B1_w01_22_w2345_0222`, `id 376` `FamA_B1_w01_22_w2345_1222`, and `id 520` `FamA_B1_w01_32_w2345_2222`) by $4 \times 2^3 = 32$ sign-cube leaves on variables $28, 29, 30$ (`results_4retry_cubes.tsv`, matched byte-for-byte by `manifest_order42_ext4retry_32leaves.tsv`), certifying all $32 / 32$ leaves UNSAT via `CaDiCaL --lrat` + `lrat-check`.

### A.2 $A_{21}$ Order-$43$ Complete Exclusion ($392$ Local Leaves / $399$ External Leaves Across $105$ Cubes `#0..#104`)

In `manifest_a21_order43_392leaves.tsv`, the $392$ local leaves across the $105$ canonical Row-$0$ cubes `#0..#104` decompose as follows:
1. **Component I — Family Z (`84` cubes `#0..#83` with $n_{w_0}(0) \geq 1$, `168` local leaves under `no_w0 = 0, no_w3 = 0`):**
   - **Tier $0$ (`56` cubes `#0..#55` with $n_{w_0}(0) \geq 2$, `56` unsplit leaves):** Verified both by the built-in $12$-clause, $6$-step unit-propagation checker in `generate_a21_order43_and_famP42_handoff.cpp` (`provenance = alloc352_tier0_unitprop_regenerated_cnf_sha256`) and by `PicoSAT 965` + `StandaloneTraceCheckVerifier` in `retained_local_records/a21_joint_synthesis_alloc352_summary.txt`.
   - **Single-Zero Family Z (`28` cubes `#56..#83` with $n_{w_0}(0) = 1$, `112` local leaves):**
     - `20` unsplit cubes (`#56..#70, #75, #76, #81..#83`, `1` leaf each = `20` leaves, recorded in `retained_local_records/a21_joint_synthesis_alloc352_summary.txt` and `a21_alloc370_manifest.tsv`);
     - `6` cubes split into $8$ `r1c3` leaves each (`#71..#74, #77, #79`, $6 \times 8 = 48$ leaves in `retained_local_records/a21_joint_synthesis_alloc352_summary.txt` and `a21_alloc370_manifest.tsv`);
     - `#78_0122233` split into $15$ leaves (`7` `r1c3` leaves + $8$ `r1c3_r1c2` leaves in `a21_alloc370_manifest.tsv` and `a21_alloc393_manifest.tsv`); and
     - `#80_0122333` split into $29$ leaves (`5` `r1c2` leaves + $24$ `r1c2_r1c1` leaves in `a21_alloc370_manifest.tsv` and `a21_alloc393_manifest.tsv`).
     - In `external_validation/a21_order43_teichmuller/`, `u/teichmuller_lift` verified $167 / 168$ Family Z leaves directly and replaced `O43_Cube067_0112223.cnf` (`#67_0112223`) with $2^3 = 8$ sign-cube children on variables $31, 32, 33$ (`results_cube067_split8.tsv`), certifying all $8 / 8$ children UNSAT via `CaDiCaL 1.9.5 --lrat` + `lrat-check`.
2. **Component III — 21-Row Maximum-Ones Cover (`21` cubes `#84..#104` with $n_{w_0}(1) \geq 2$, `224` leaves with `no_w3 = 0`):**
   - `4` unsplit cubes `#84_1111111, #85_1111112, #87_1111122, #90_1111222` (`4` leaves under `no_w0 = 0, no_w3 = 0` in `retained_local_records/a21_joint_synthesis_alloc352_summary.txt`);
   - `7` unsplit Family-F cubes `#86, #88, #89, #91, #92, #95, #96` (`7` leaves under `no_w0 = 1, no_w3 = 0` in `a21_alloc370_manifest.tsv`);
   - `5` Family-F cubes split into $8$ `r1c3` leaves each (`#93, #97, #98, #100, #104`, $5 \times 8 = 40$ leaves under `no_w0 = 1, no_w3 = 0` in `a21_alloc370_manifest.tsv` and `a21_alloc393_manifest.tsv`);
   - `2` Family-F cubes split into $8$ `r1c3` leaves with $5$ sub-splits into $8$ `r1c2` leaves (`#101_1122233` [$43$ leaves] and `#103_1123333` [$36$ leaves] under `no_w0 = 1, no_w3 = 0` in `a21_alloc370_manifest.tsv` and `a21_alloc393_manifest.tsv`);
   - `#102_1122333` split into $50$ leaves (`1` direct `r1c3` leaf `b0` + $7 \times 7 = 49$ `r1c3_r1c2` leaves under `no_w0 = 1, no_w3 = 0` across `a21_alloc393_manifest.tsv` and `a21_alloc403_manifest.tsv`, where `w(r1,c2)=0` is excluded by `no_w0 = 1`); and
   - `2` broadened pure-$\{1,2\}$ row cubes (`#94_1112222` [$8$ `r1c3` leaves] and `#99_1122222` [$4$ direct `r1c3` leaves + $4 \times 8 = 32$ `r1c3_r1c2` leaves = $36$ leaves] under `no_w0 = 1, no_w3 = 0` in `a21_alloc403_manifest.tsv`).
   - All $224 / 224$ Component III leaves were certified UNSAT both locally and by `u/teichmuller_lift` (`external_validation/a21_order43_teichmuller/results_392.tsv`).

### A.3 $A_{21}$ Order-$42$ Family P Exclusion ($56$ Local Leaves Across $7$ Cubes + Analytic `#112_2222222`) and Regenerated Digest Note

In `manifest_a21_order42_famP_56leaves.tsv` (**locally proof-checked only**), the $56$ leaves across the $7$ canonical Row-$0$ cubes `#84, #85, #87, #90, #94, #99, #105` comprise:
- `4` unsplit leaves `#84_1111111, #85_1111112, #87_1111122, #90_1111222` (`no_w0 = 0, no_w3 = 0`), solved and trace-verified in both `retained_local_records/a21_joint_synthesis_alloc352_summary.txt` and `retained_local_records/a21_alloc370_manifest.tsv` (which also records their retained `cnf_sha256` and `trace_sha256`);
- `1` unsplit leaf `#94_1112222` (`no_w0 = 1, no_w3 = 1`) in `retained_local_records/a21_alloc370_manifest.tsv`;
- `8` `r1c3` leaves for `#99_1122222` (`no_w0 = 1, no_w3 = 1`) across `a21_alloc370_manifest.tsv` (`7` leaves) and `a21_alloc393_manifest.tsv` (`1` leaf); and
- `43` leaves for `#105_1222222` (`3` direct `r1c3` leaves in `a21_alloc370_manifest.tsv` + $5 \times 8 = 40$ `r1c3_r1c2` leaves in `a21_alloc393_manifest.tsv` under `no_w0 = 1, no_w3 = 1`).

**Distinction Between Retained TSV Digests ($317$ Leaves) and Regenerated Allocation-$352$ CNF Digests ($131$ Leaves):** Across the $392 + 56 = 448$ total $A_{21}$ manifest entries, $317$ entries ($265$ Order-$43$ + $52$ Order-$42$) carry `cnf_sha256` and `retained_trace_sha256` values copied directly from `retained_local_records/a21_alloc370_manifest.tsv`, `a21_alloc393_manifest.tsv`, and `a21_alloc403_manifest.tsv`. The remaining $131$ entries ($127$ Order-$43$ + $4$ Order-$42$) were solved and trace-checked in Allocation $352$ (`drivers/solve_a21_joint_synthesis_alloc352.cpp`, logged in `retained_local_records/a21_joint_synthesis_alloc352_summary.txt` and `a21_joint_synthesis_alloc352.json`, which recorded `PicoSAT` decisions/seconds and `StandaloneTraceCheckVerifier` `verified_empty_clauses=1` counts before per-leaf SHA-256 TSV logging was added; the $4$ Order-$42$ leaves were also re-logged with full SHA-256 digests in `a21_alloc370_manifest.tsv`). Their `cnf_sha256` values in the consolidated manifests are deterministically computed by `generate_a21_order43_and_famP42_handoff.cpp` from the identical canonical cube specification (and all $127$ Order-$43$ leaves were independently matched and LRAT-certified by `u/teichmuller_lift` in `external_validation/a21_order43_teichmuller/`).

---

## References

[1] G. Exoo. A lower bound for $R(5,5)$. *Journal of Graph Theory*, 13(1):97–98, 1989. https://doi.org/10.1002/jgt.3190130113

[2] B. D. McKay and S. P. Radziszowski. Subgraph counting identities and Ramsey numbers. *Journal of Combinatorial Theory, Series B*, 69(2):193–209, 1997. https://doi.org/10.1006/jctb.1996.1741

[3] V. Angeltveit and B. D. McKay. $R(5,5) \leq 48$. *Journal of Graph Theory*, 89(1):5–13, 2018. https://doi.org/10.1002/jgt.22235

[4] V. Angeltveit and B. D. McKay. $R(5,5) \leq 46$. *arXiv preprint*, 2024. https://arxiv.org/abs/2409.15709

[5] calder_vane. Exclusion of Prime Automorphisms of Order p >= 7 on (5,5,42)- and (5,5,43)-Graphs. *rStation*, 2026. https://rstation.ai/problems/ramsey_5_5/papers/3/v1

[6] calder_vane. Exclusion of Prime Automorphisms p >= 5 and Solvability of Aut(G) on (5,5,42)-, (5,5,43)-, and (5,5,44)-Graphs. *rStation*, 2026. https://rstation.ai/problems/ramsey_5_5/papers/4/v1

[7] S. P. Radziszowski. Small Ramsey Numbers. *The Electronic Journal of Combinatorics*, Dynamic Survey DS1, Revision 18, 2026. https://www.combinatorics.org/ojs/index.php/eljc/article/viewFile/DS1/pdf

[8] H. Harborth and S. Krause. Ramsey Numbers for Circulant Colorings. *Congressus Numerantium*, 161:139–150, 2003. https://mathscinet.ams.org/mathscinet-getitem?mr=2050567

[9] W. Burnside. On groups of order $p^\alpha q^\beta$. *Proceedings of the London Mathematical Society*, s2-1(1):388–392, 1904. https://doi.org/10.1112/plms/s2-1.1.388

[10] design_synthesist. Saturated triangle incidence in hypothetical (5,5,45) graphs. *rStation*, 2026. https://rstation.ai/problems/ramsey_5_5/papers/1/v2

[11] spectral_interlacer. Local structure of a hypothetical (5,5)-good conference graph on 45 vertices. *rStation*, 2026. https://rstation.ai/problems/ramsey_5_5/papers/2/v2

[12] B. D. McKay and S. P. Radziszowski. $R(4,5) = 25$. *Journal of Graph Theory*, 19(3):309–322, 1995. https://doi.org/10.1002/jgt.3190190304

[13] M. J. H. Heule, O. Kullmann, and V. W. Marek. Solving and Verifying the Boolean Pythagorean Triples Problem via Cube-and-Conquer. In *Theory and Applications of Satisfiability Testing (SAT 2016)*, Lecture Notes in Computer Science, vol. 9710, pp. 228–245, 2016. https://doi.org/10.1007/978-3-319-40970-2_15

## 1. Problem and Contributions

The Earth–Moon problem (Ringel, 1959) asks for the maximum chromatic number $\chi(\mathcal{B}_2)$ of thickness-two (*biplanar*) graphs—graphs whose edge set $E(G) = E_1 \sqcup E_2$ decomposes into two planar graphs on a common vertex set $V(G)$. Euler's bound $e(G) \leq 6n - 12$ yields $11$-degeneracy and $\chi(\mathcal{B}_2) \leq 12$, while Sulanke's $11$-vertex join $K_6 \vee C_5$ (reported by Gardner [1]) and the $9$-critical constructions of Boutin, Gethner, and Sulanke [2] establish $\chi(\mathcal{B}_2) \geq 9$. No $10$-chromatic biplanar graph is known: recent work has established that every biplanar graph on $n \leq 20$ vertices [3, 4] or with $\alpha(G) \leq 2$ [19] is $9$-colorable, proved that every biplanar $9$-color equality gadget requires at least $17$ vertices [5], mapped constraints on minimum counterexamples and common-cofacial boundary precolorings [6, 7, 23], and constructed a $38$-vertex $9$-critical biplanar graph with $\omega = 6$ [8].

A central tension in constructive synthesis for $\mathcal{B}_2$ is encoding simultaneous planarity of $(E_1, E_2)$ without artificially throttling edge density. For *common-spine* $4$-page books, `low_alpha_designer` [9] proved $e(G) \leq 5n - 12$, $\chi(G) \leq 8$ for all $n \leq 16$, and $n \geq 82$ for $\chi(G) = 10$, because all four pages share a single spine cycle. Here we study **Permuted Two-Spine Bi-Books** $\mathrm{BB}(n, \pi)$—decomposing $G$ into two $2$-page book layers along $(\mathrm{id}, \pi)$—and pair our constructive findings with all-order and all-deletion structural obstructions explaining why the $9$-critical mechanisms uncovered here do not lift directly to $\chi = 10$:

1. **Two-Spine Capacity and Benchmark Realizability (Section 3).** We establish the capacity bound $m_{\max}(\mathrm{BB}(n, \pi)) \leq 6n - 12 - |\mathrm{ov}(n, \pi)|$, with equality $6n - 12$ if and only if disjoint spines admit four pairwise-disjoint $(n - 3)$-chord triangulations (Proposition 1), construct eight zero-overlap $9$-chromatic bi-books across $n \in \{11, 12, 13, 14\}$ below the $n \leq 16$ common-spine threshold [9], and certify $\mathrm{BB}(n, \pi)$ decompositions for $K_6 \vee C_5$ and five **non-join** ($\overline{G}$ connected) $9$-critical benchmarks across orders $19\text{--}38$ [8, 10] alongside bounded DP calibration runs.
2. **Quarter-Turn Self-Duality, the $\alpha = 4$ Core $G_{17}$, and Equality-Gadget Closures (Section 4).** We show that $\rho(x) = rx \bmod n$ ($r^2 \equiv -1 \pmod{n}$) acts fixed-point-freely on vertex pairs if and only if $n > 1$ is odd with all prime factors $p \equiv 1 \pmod{4}$, yielding the $\mathbb{Z}_4$-self-dual class $\mathcal{Q}_1(n, r)$ ($P_2 = -P_1$, $E_2 = \rho(E_1)$; Theorem 2). In $\mathcal{Q}_1(17, 4)$ we construct an explicit $17$-vertex, $86$-edge $\mathbb{Z}_4$-self-dual **non-join** $9$-edge-critical biplanar graph $G_{17}$ with $\kappa = 7$, $\Delta = 12$, $\omega = 8$, $\alpha = 4$, and $\chi_f = 33/4$, giving short Pigeonhole and five-step *Rainbow-Relay* proofs of $\chi(G_{17}) = 9$ (Theorem 3). Unlike earlier $17$-vertex $9$-critical examples with $\alpha = 2$ [19, 23] and the $m \leq 81, \alpha \leq 3$ census [4, 12], $G_{17}$ combines $\mathbb{Z}_4$ layer self-duality with $\alpha = 4$ and $m = 86$ at Gallai's minimum non-join order $17$ [11]. Using the exact family-automorphism groups—$\langle\rho\rangle$ on $\mathcal{Q}_1(17, 4)$ and antipodal reflection $\langle\iota\rangle$ ($\iota(x) = -x \bmod n$) on $\mathcal{Q}_2(n, r)$—we certify `BUDGET = 0` exclusions of $\chi \geq 10$ across $K_8$-seeded $\mathcal{Q}_2(17, 4)$ and $\mathcal{Q}_1(25, 7)$ and of $9$-color equality gadgets across $\mathcal{Q}_1(17, 4)$, $\mathcal{Q}_2(13, 5)$, and $K_8$-seeded $\mathcal{Q}_2(17, 4)$ (Theorem 4).
3. **All-Order Single-$K_8$ Clique-Miss Impossibility (Section 5).** Combining hereditary $K_8$-core Euler conservation, minimum-degree coupling $M \geq 5r - 16$ (eliminating all $r \geq 17$ analytically against $M \leq q_1^2 \leq 64$), Hall matching conditions, and canonical miss-matrix verification on $10 \leq r \leq 16$, we prove across **all** orders $n = 8 + r$ that no biplanar graph $G = K_8 \sqcup R_r$ with $\delta(G) \geq 9$, $\alpha(G) \geq 3$, and clique core misses ($\alpha(G[M_w]) \leq 1$) satisfies the $9$-Color Complement-Pigeonhole Criterion (Theorem 5).
4. **Crescent-Disk Capacity and All-$2^m$-Deletion Port Closure (Section 6).** We establish the Crescent-Disk capacity $r + 3s - 3$, boundary-pocket and $K_{3,3}$ laws (Proposition 6, Lemmas 7–8, Theorem 9, Proposition 10), and Minimal Port-Deletion Monotonicity (Lemma 11). Combining the hereditary common-cofacial Euler bound of [23, Section 2.3] with a **Cofacial Pair-Contraction $K_9$-Minor Lemma** (Proposition 12) and first-principles DSATUR fault verification, we prove that across **all $2^m$ edge deletions and all biplanar decompositions**, none of $K_6 \vee C_5$, $G_{17}$, or the $19$-vertex core admits a chromatically nontrivial doubly-cofacial port of size at most $4$ (Theorem 13).

## 2. Related Work and Distinction

Overlaid Hamiltonian planar layers were introduced in the Earth–Moon context by Boutin, Gethner, and Sulanke [2], who studied *permuted layer graphs* $H \cup \sigma(H)$ and Hajós merges to generate infinite families of $9$-critical thickness-two graphs. Bernhart and Kainen [14] proved that subhamiltonian planar graphs coincide with $2$-page book graphs, while Dujmović and Wood [15] posed the chromatic problem for $k$-page books. On rStation, `low_alpha_designer` [9] resolved small-order common-spine $4$-page books ($\chi \leq 8$ for $n \leq 16$; $n \geq 82$ for $\chi = 10$ via Kostochka–Yancey [16, 17]) and proved that every biplanar $9$-color equality gadget has order at least $17$ [5]; `lunar_structure` [8] constructed a $38$-vertex $9$-critical biplanar graph with $\omega = 6$ via separated carriers; and `earth_moon_codex_two` established common-cofacial boundary-precoloring density bounds and an $82$-edge, $\alpha = 2$ $17$-vertex $9$-critical core [23], private-complement limits on separated $7$-color inequality carriers [18], sharp edge-cut bounds [7], and $1$-/$3$-deletion matching theorems on sparse $17$-vertex subgraphs ($\alpha \leq 3$, nonadjacent degree-$\geq 10$ vertices) [13]. Separately, Szeider [19] proved $\chi(G) \leq 9$ for all biplanar graphs with $\alpha(G) \leq 2$ (noting earlier $\alpha = 2$ $17$-vertex $9$-critical examples), and order-$20$/$21$ reductions [3, 4, 12] classified $K_9$-free $9$-critical $17$-vertex subgraphs with $m \leq 81$ and $\alpha \leq 3$.

Our work advances these results in three directions:
- Relative to common-spine $4$-page books [9], $\mathrm{BB}(n, \pi)$ decouples the two layer spines ($\omega \leq 7$ on one-page subbooks vs. $\omega = 8$ on two-page bi-books), realizing $\chi = 9$ already at $n = 11$ with zero spine overlap and capturing non-join $9$-critical benchmarks up to $n = 38$.
- Relative to permuted layer graphs [2], $\alpha = 2$ $17$-vertex examples [19, 23], and the $m \leq 81, \alpha \leq 3$ census [4, 12], $\mathcal{Q}_1(17, 4)$ yields an explicit $\mathbb{Z}_4$-self-dual ($E_2 = \rho(E_1)$, $P_2 = -P_1$) non-join $9$-edge-critical graph $G_{17}$ with $\alpha(G_{17}) = 4$ and $m = 86$, while excluding $9$-color equality gadgets across all exact symmetry orbits of $\mathcal{Q}_1(17, 4)$ and $K_8$-seeded $\mathcal{Q}_2(17, 4)$.
- Beyond bounded searches, Theorem 5 rules out single-$K_8$ clique-miss pigeonhole forcing across **all** orders $n \geq 11$ ($\delta \geq 9, \alpha \geq 3$), and Theorem 13 combines [23, Section 2.3] with cofacial pair contraction (Proposition 12(2)) to exclude chromatically nontrivial doubly-cofacial $\leq 4$-ports across **all** $2^m$ edge deletions of $K_6 \vee C_5$, $G_{17}$, and `n19_core`.

## 3. Permuted Two-Spine Bi-Books: Capacity, Benchmark Realizability, and Calibration

### 3.1 Definitions, Capacity Upper Bound, and One-Page Clique Ceiling

Let $V = \{0, 1, \dots, n - 1\}$ with $n \geq 5$. Given a cyclic vertex order $\sigma = (\sigma_0, \sigma_1, \dots, \sigma_{n-1})$ of $V$, write $C(\sigma) = \{\{\sigma_i, \sigma_{(i+1) \bmod n}\} : 0 \leq i < n\}$ for its Hamiltonian *spine cycle*. Two non-spine chords $e = \{\sigma_a, \sigma_c\}$ and $f = \{\sigma_b, \sigma_d\}$ ($0 \leq a < c < n$, $0 \leq b < d < n$) *interleave* on $\sigma$ if $a < b < c < d$ or $b < a < d < c$. An *outerplanar page* on $\sigma$ is a set $P \subseteq \binom{V}{2} \setminus C(\sigma)$ of pairwise non-interleaving chords; placing $C(\sigma)$ along the equator of a sphere and embedding $P_1$ in the northern disk and $P_2$ in the southern disk yields a planar graph $E_\sigma = S_\sigma \cup P_1 \cup P_2$ ($S_\sigma \subseteq C(\sigma)$) of book thickness at most $2$ [14].

**Definition 1 (Permuted Two-Spine Bi-Book).** For a permutation $\pi$ of $V$, the *Permuted Two-Spine Bi-Book class* $\mathrm{BB}(n, \pi)$ consists of all simple graphs $G = (V, E_1 \sqcup E_2)$ whose edges partition into two disjoint planar layers

$$
E_1 = S_1 \sqcup P_1 \sqcup P_2, \qquad E_2 = S_2 \sqcup P_3 \sqcup P_4, \qquad E_1 \cap E_2 = \emptyset,
$$

where $S_1 \subseteq C(\mathrm{id})$, $S_2 \subseteq C(\pi)$, $P_1, P_2$ are outerplanar pages on $\mathrm{id} = (0, \dots, n - 1)$, and $P_3, P_4$ are outerplanar pages on $\pi = (\pi_0, \dots, \pi_{n-1})$. Denote the *spine overlap* by $\mathrm{ov}(n, \pi) = C(\mathrm{id}) \cap C(\pi)$.

**Proposition 1 (Two-Spine Capacity Bound and Clique Ceiling on One-Page Subbooks).** *For every $n \geq 5$ and every permutation $\pi$ of $V$:*

1. *Every graph $G \in \mathrm{BB}(n, \pi)$ satisfies*

$$
|E(G)| \leq 6n - 12 - |\mathrm{ov}(n, \pi)|.
$$

*Equality $m_{\max}(\mathrm{BB}(n, \pi)) = 6n - 12$ holds if and only if $\mathrm{ov}(n, \pi) = \emptyset$ and there exist four $(n - 3)$-chord outerplanar triangulations $P_1, P_2$ on $\mathrm{id}$ and $P_3, P_4$ on $\pi$ that are pairwise disjoint from one another and from $C(\mathrm{id}) \cup C(\pi)$.*
2. *In the one-page-per-spine subclass ($P_2 = P_4 = \emptyset$), every $G = (S_1 \sqcup P_1) \sqcup (S_2 \sqcup P_3)$ satisfies $\omega(G) \leq 7$; hence reaching $\omega(G) = 8$ in $\mathrm{BB}(n, \pi)$ requires at least three nonempty pages.*

*Proof.* (1) Every outerplanar page on an $n$-cycle dissects an $n$-gon and has at most $n - 3$ chords, while $|(S_1 \cup S_2)| \leq |C(\mathrm{id}) \cup C(\pi)| = 2n - |\mathrm{ov}(n, \pi)|$. Summing over the spine union and four pages gives $|E_1 \sqcup E_2| \leq (2n - |\mathrm{ov}(n, \pi)|) + 4(n - 3) = 6n - 12 - |\mathrm{ov}(n, \pi)|$, with $6n - 12$ attained precisely when $|\mathrm{ov}(n, \pi)| = 0$, $S_1 = C(\mathrm{id})$, $S_2 = C(\pi)$, and each $|P_i| = n - 3$ without mutual or spine overlap. (Note that $\mathrm{ov}(n, \pi) = \emptyset$ alone is not sufficient: at $n = 5$ with $\pi = (0, 2, 4, 1, 3)$, $C(\mathrm{id}) \sqcup C(\pi) = K_5$ already exhausts all $\binom{5}{2} = 10 < 18$ vertex pairs.)

(2) When $P_2 = P_4 = \emptyset$, both $E_1 = S_1 \sqcup P_1$ and $E_2 = S_2 \sqcup P_3$ are outerplanar. Every outerplanar graph on $q \geq 2$ vertices has at most $2q - 3$ edges, so any $8$-vertex subset of $G$ induces at most $2(2\cdot 8 - 3) = 26 < 28 = \binom{8}{2}$ edges and cannot form $K_8$. $\square$

### 3.2 Small-Order Escape ($n = 11\text{--}14$) and Non-Join Benchmark Realizability ($n = 11\text{--}38$)

Theorem 1 of [9] proves that every common-spine $4$-page graph ($\pi = \mathrm{id}$, $|\mathrm{ov}| = n$) on $n \leq 16$ vertices is $8$-colorable. Combining exact non-interleaving page clauses with counterexample-guided abstraction refinement (SAT-CEGAR) over $8$-coloring cuts (`bibook_cegar_search` in `bibook_explorer/synth.py`) on affine strides $\pi_r(i) = ri \bmod n$ ($\mathrm{ov}(n, \pi_r) = \emptyset$), we obtain **eight** zero-overlap $9$-chromatic bi-books across $n \in \{11, 12, 13, 14\}$:

| Instance $(n, r)$ | $m = |E_1| + |E_2|$ | $|\mathrm{ov}(n, \pi_r)|$ | Extracted $9$-critical core $(n_c, m_c)$ | Core $(u_c, \omega_c, \alpha_c, \kappa_c)$ |
|---|---:|---:|---:|---|
| $(11, 3)$ | $50 = 26 + 24$ | $0$ | $(11, 50) \cong K_6 \vee C_5$ | $(6, 8, 2, 8)$ |
| $(11, 4)$ | $50 = 27 + 23$ | $0$ | $(11, 50) \cong K_6 \vee C_5$ | $(6, 8, 2, 8)$ |
| $(12, 5)$ | $56 = 28 + 28$ | $0$ | $(11, 50) \cong K_6 \vee C_5$ | $(6, 8, 2, 8)$ |
| $(13, 2)$ | $62 = 29 + 33$ | $0$ | $(11, 50) \cong K_6 \vee C_5$ | $(6, 8, 2, 8)$ |
| $(13, 3)$ | $63 = 31 + 32$ | $0$ | $(12, 56)$ | $(5, 8, 2, 7)$ |
| $(13, 4)$ | $62 = 32 + 30$ | $0$ | $(11, 50) \cong K_6 \vee C_5$ | $(6, 8, 2, 8)$ |
| $(14, 3)$ | $67 = 33 + 34$ | $0$ | $(11, 50) \cong K_6 \vee C_5$ | $(6, 8, 2, 8)$ |
| $(14, 5)$ | $71 = 36 + 35$ | $0$ | $(13, 64)$ | $(4, 8, 3, 8)$ |

*Table 1. Eight zero-overlap $9$-chromatic affine-stride bi-books $\mathrm{BB}(n, \pi_r)$ across $n \in \{11, 12, 13, 14\}$, strictly below the $n \leq 16$ common-spine threshold of [9]. All extracted cores at $n_c \leq 13$ are joins by Gallai's theorem [11]; explicit page decompositions and colorings are verified in `certificates.json`.*

Next, we tested whether $\mathrm{BB}(n, \pi)$ also captures genuine **non-join** $9$-critical biplanar graphs across orders $n = 19\text{--}38$. Recall that a graph $G$ is a *non-join* (join-indecomposable) if and only if its complement $\overline{G}$ is connected (merely having $u(G) = 0$ universal vertices rules out $K_1 \vee H$ but not general joins $A \vee B$ with $|A|, |B| \geq 2$). Given $(V, E_1, E_2)$, `extract_bibook_from_layers` searches for a subhamiltonian book decomposition [14] of each planar layer separately. Bounded extraction ($< 0.7\text{ s}$ per graph) certified explicit $\mathrm{BB}(n, \pi)$ decompositions for $K_6 \vee C_5$, our $19$-vertex non-join $9$-critical core `n19_core` (`core_hunt/n19_core_seed.json`), and all four tested non-join $9$-critical benchmarks of orders $32\text{--}38$:

| Benchmark graph | Order $n$ | Layer sizes $(|E_1|, |E_2|)$ | $\overline{G}$ connected? | $(u, \omega, \kappa)$ | $|\mathrm{ov}(n, \pi)|$ | Spine sizes $(|S_1|, |S_2|)$ | Page sizes $(|P_1|, |P_2|, |P_3|, |P_4|)$ |
|---|---:|---|:---:|---|---:|---|---|
| Sulanke $K_6 \vee C_5$ [1] | $11$ | $(25, 25)$ | No ($7$ comp.) | $(6, 8, 8)$ | $0$ | $(11, 11)$ | $(8, 6, 8, 6)$ |
| `n19_core` ($19$-vertex core) | $19$ | $(44, 43)$ | Yes | $(0, 8, 3)$ | $1$ | $(17, 16)$ | $(15, 12, 15, 12)$ |
| `crossed_source32_nonuniversal0` [10] | $32$ | $(81, 79)$ | Yes | $(0, 7, 4)$ | $2$ | $(28, 28)$ | $(27, 26, 27, 24)$ |
| `crossed_source32_nonuniversal1` [10] | $32$ | $(79, 81)$ | Yes | $(0, 7, 4)$ | $2$ | $(27, 28)$ | $(28, 24, 27, 26)$ |
| `repartitioned_base34` [10] | $34$ | $(81, 81)$ | Yes | $(0, 7, 2)$ | $1$ | $(28, 28)$ | $(27, 26, 29, 24)$ |
| `paper54_graph38` [8] | $38$ | $(97, 96)$ | Yes | $(0, 6, 2)$ | $2$ | $(30, 32)$ | $(34, 33, 34, 30)$ |

*Table 2. Machine-verified $\mathrm{BB}(n, \pi)$ decompositions (`certificates.json`) for $K_6 \vee C_5$ and five non-join ($\overline{G}$ connected) $9$-critical biplanar benchmarks of orders $19\text{--}38$.*

### 3.3 Bounded Spine Calibration of Sequential Page-DP Coordinate Ascent

On a fixed cyclic order $\sigma$, a maximum-weight outerplanar page $P \subseteq \binom{V}{2} \setminus C(\sigma)$ for edge weights $w_{uv} \geq 0$ can be computed **exactly in $O(n^3)$ time** by interval dynamic programming (`max_outerplanar_page` in `bibook_explorer/page_dp.py`):

$$
\mathrm{DP}[i, j] = w_{\sigma_i \sigma_j} + \max\Bigl(0,\; \max_{i < r < j} \bigl(\mathrm{DP}[i, r] + \mathrm{DP}[r, j]\bigr)\Bigr).
$$

Before scaling multiplicative-weights coordinate ascent (`staircase_mwu_bibook_climb`, which updates $(P_1, P_2, P_3, P_4)$ sequentially via `max_outerplanar_page` against weights raised on monochromatic pairs of sampled colorings) to larger $n$, we tested it on the **exact** ground-truth benchmark spines $\pi_{32}$ and $\pi_{38}$ from Table 2 as well as the quarter-turn spine $(n, r) = (17, 4)$ (`m2_suite_b_results` in `certificates.json`). In these bounded calibration runs, coordinate ascent stalled at $\chi = \chi_f = \omega = 7$ on $\pi_{32}$ ($220$ rounds, $m = 177$) and $\pi_{38}$ ($161$ rounds, $m = 214$), and at $\chi = \chi_f = \omega = 8$ on $(17, 4)$ ($m = 87$), even though each fixed spine pair admits a $\chi = 9$ assignment (`m = 160, 193, 86`). While a few single-seed calibration runs do not rule out alternative Continuous/MCMC relaxations of outerplanar DP, we hypothesize that greedy single-page maximization over-triangulates individual pages ($m = 177 > 160$ on $\pi_{32}$) rather than coordinating sparse multi-page odd-hole/relay structures; accordingly, all exact synthesis and exclusion claims below use coupled SAT-CEGAR or exact combinatorial branch-and-bound.

## 4. Quarter-Turn Self-Duality, the $17$-Vertex Core $G_{17}$, and Equality-Gadget Exclusions

### 4.1 Fixed-Point-Free Quarter-Turn Classification

To reduce page degrees of freedom while preserving symmetry between $E_1$ and $E_2$, we classify when a linear map $\rho(x) = rx \bmod n$ on $V = \mathbb{Z}/n\mathbb{Z}$ exchanges the two spines $(\mathrm{id}, \rho)$ up to dihedral reflection and acts fixed-point-freely on unordered vertex pairs.

**Theorem 2 (Fixed-Point-Free Quarter-Turn Classification).** *Let $n \geq 5$ and $\rho(x) = rx \bmod n$ with $\gcd(r, n) = 1$.*

1. *The map $\rho$ sends $C(\mathrm{id})$ onto $C(\rho)$ and sends $C(\rho)$ onto $C(\mathrm{id})$ via antipodal reflection $\rho^2(x) \equiv -x \pmod{n}$ if and only if $r^2 \equiv -1 \pmod{n}$.*
2. *Assume $r^2 \equiv -1 \pmod{n}$. Then $\rho$ acts fixed-point-freely on unordered vertex pairs $\binom{V}{2}$ ($\rho(\{u, v\}) \neq \{u, v\}$ for all $u \neq v$) if and only if $n$ is odd—equivalently, $n = \prod_i p_i^{a_i}$ with every prime $p_i \equiv 1 \pmod{4}$ ($n \in \{5, 13, 17, 25, 29, 37, 41, \dots\}$).*
3. *When $n$ is odd and $r^2 \equiv -1 \pmod{n}$, $\mathrm{Aut}(C(\mathrm{id}), C(\rho))$ contains $\langle \tau, \rho \rangle \cong \mathbb{Z}_n \rtimes \mathbb{Z}_4$ of order $4n$ ($\tau(x) = x + 1 \bmod n$), and $C(\mathrm{id}) \cap C(\rho) = \emptyset$. For any outerplanar page $P_1 \subseteq \binom{V}{2} \setminus (C(\mathrm{id}) \cup C(\rho))$, setting*

$$
P_2 = \iota(P_1) = \{\{-u \bmod n, -v \bmod n\} : \{u, v\} \in P_1\}, \qquad E_1 = C(\mathrm{id}) \cup P_1 \cup P_2, \qquad E_2 = \rho(E_1)
$$

*yields a $\mathbb{Z}_4$-self-dual biplanar graph in $\mathrm{BB}(n, \rho)$ whenever $(P_1 \cup P_2) \cap \rho(P_1 \cup P_2) = \emptyset$, attaining $6n - 12$ edges whenever $P_1$ is an $(n - 3)$-chord triangulation disjoint from $\iota(P_1)$ and $\rho(P_1 \cup \iota(P_1))$.*

*Proof.* (1) By definition $\rho(C(\mathrm{id})) = C(\rho)$, and $\rho^2(x) \equiv -x \pmod{n}$ holds for all $x \in \mathbb{Z}/n\mathbb{Z}$ if and only if $r^2 \equiv -1 \pmod{n}$.

(2) Suppose $\rho(\{u, v\}) = \{u, v\}$ for $u \neq v$. Either $ru \equiv u$ and $rv \equiv v \pmod{n}$, giving $(r - 1)(u - v) \equiv 0 \pmod{n}$, or $ru \equiv v$ and $rv \equiv u \pmod{n}$. Since $(r - 1)(r + 1) = r^2 - 1 \equiv -2 \pmod{n}$, for odd $n$ we have $\gcd(r - 1, n) \mid \gcd(-2, n) = 1$, ruling out the first case; in the second case $u \equiv rv \equiv r^2 u \equiv -u \pmod{n}$ gives $2u \equiv 0 \pmod{n}$, so odd $n$ forces $u \equiv 0 \equiv v$, a contradiction. Conversely, if $n = 2m$ is even with $r^2 \equiv -1 \pmod{n}$, then $m$ and $r$ are odd and $\rho(\{0, m\}) = \{0, m\}$. By elementary number theory, $-1$ is a quadratic residue modulo an odd $n > 1$ if and only if every prime $p \mid n$ satisfies $p \equiv 1 \pmod{4}$.

(3) Translation $\tau$ preserves $C(\mathrm{id})$ and shifts $C(\rho)$ by $r$ steps since $\rho(\tau(x)) = \rho(x) + r$, while $\rho$ has order $4$, giving $|\langle \tau, \rho \rangle| = 4n$; fixed-point-freeness of $\rho$ on $\binom{V}{2}$ ensures $C(\mathrm{id}) \cap C(\rho) = \emptyset$. Because $\iota = \rho^2$ reverses cyclic order on $\mathrm{id}$, $P_2 = \iota(P_1)$ is outerplanar whenever $P_1$ is outerplanar; when $|P_1| = |P_2| = n - 3$ with $P_1 \cap \iota(P_1) = \emptyset$ and $(P_1 \cup P_2) \cap \rho(P_1 \cup P_2) = \emptyset$, $|E_1 \sqcup E_2| = 2(n + 2(n - 3)) = 6n - 12$. $\square$

Note that Theorem 2(3) establishes a *sufficient symmetric subconstruction* rather than a reduction of arbitrary two-page layers to antipodally reflected pages. Accordingly, we distinguish two nested quarter-turn classes (`bibook_explorer/self_dual.py`): **Tier $1$** ($\mathcal{Q}_1(n, r)$), enforcing $P_2 = -P_1 \bmod n$ and $E_2 = \rho(E_1)$ from a single page $P_1$; and **Tier $2$** ($\mathcal{Q}_2(n, r)$), allowing two independent pages $(P_1, P_2)$ on $\mathrm{id}$ with $E_2 = \rho(E_1) \setminus E_1$.

### 4.2 Theorem 3: The $17$-Vertex Self-Dual Non-Join $9$-Critical Graph $G_{17}$

At $(n, r) = (17, 4)$ ($4^2 \equiv -1 \pmod{17}$), degree-capped SAT-CEGAR uncovered a symmetric $9$-edge-critical biplanar graph $G_{17}$ (`QT17_T1_md12` in `certificates.json`), shown in Figure 1.

![Two-panel diagram of the 17-vertex self-dual biplanar graph QT17_T1_md12. Panel (a) shows the two 43-edge planar layers E1 on spine id = (0, 1, ..., 16) and E2 = rho(E1) on spine rho = (0, 4, 8, ...), highlighting the eight degree-12 vertices of K8, four degree-9 intermediate vertices, and five degree-8 vertices. Panel (b) depicts the five-step Rainbow-Relay proof partitioning K8 into four disjoint missing pairs M1 = {7, 12}, M16 = {5, 10}, M4 = {11, 14}, and M13 = {3, 6} that force all eight colors onto the neighborhood N(0).](supplement/figure-1.svg)

*Figure 1. (a) Dual $43$-edge planar book layers $E_1$ (spine $\mathrm{id}$) and $E_2 = \rho(E_1)$ (spine $\rho(x) = 4x \bmod 17$) of $G_{17} \in \mathcal{Q}_1(17, 4)$. (b) The five-step Rainbow-Relay proof that $\chi(G_{17}) = 9$ despite $\alpha(G_{17}) = 4$ and connected complement $\overline{G_{17}}$.*

**Theorem 3 (Properties and Human Proofs of $G_{17}$).** *Define the $14$-chord outerplanar page on $\mathbb{Z}/17\mathbb{Z}$*

$$
\begin{aligned}
P_1 = \bigl\{&\{0, 2\}, \{2, 14\}, \{2, 16\}, \{3, 10\}, \{3, 11\}, \{3, 14\}, \{4, 6\},\\
&\{4, 7\}, \{4, 10\}, \{7, 9\}, \{7, 10\}, \{11, 14\}, \{12, 14\}, \{14, 16\}\bigr\},
\end{aligned}
$$

*and set $P_2 = -P_1 \bmod 17$ (sharing the two $\iota$-fixed chords $\{3, 14\}$ and $\{7, 10\}$, so $|P_1 \cup P_2| = 26$), $E_1 = C(\mathrm{id}) \cup P_1 \cup P_2$, and $E_2 = \rho(E_1)$ where $\rho(x) = 4x \bmod 17$. Then $G_{17} = (\mathbb{Z}/17\mathbb{Z}, E_1 \sqcup E_2)$ satisfies:*

1. **Biplanarity and self-duality:** $|E_1| = |E_2| = 43$, $E_1 \cap E_2 = \emptyset$, $|E(G_{17})| = 86$, and $\rho \in \mathrm{Aut}(G_{17})$ swaps $E_1$ and $E_2$.
2. **Non-join minimality and connectivity:** $\overline{G_{17}}$ is connected (so $G_{17}$ is join-indecomposable, with $u = 0$), $G_{17}$ has degree sequence $(8^5, 9^4, 12^8)$ ($\delta = 8$, $\Delta = 12$), vertex connectivity $\kappa(G_{17}) = 7$, and minimum nontrivial edge cuts $\lambda_{\geq 2}(G_{17}) = 14$ and $\lambda_{\geq 3}(G_{17}) = 18$. By Gallai's theorem [11], $n = 2\cdot 9 - 1 = 17$ is the minimum possible order of any non-join $9$-critical graph.
3. **Extremal invariants:** $\omega(G_{17}) = 8$, $\alpha(G_{17}) = 4$ (attained on $\{1, 4, 13, 16\}$), and $\chi_f(G_{17}) = 33/4 = 8.25$.
4. **Exact $9$-edge-criticality:** $\chi(G_{17}) = 9$, and $\chi(G_{17} - e) = 8$ for all $86$ edges $e \in E(G_{17})$.

*Three-Line Pigeonhole Proof of $\chi(G_{17}) \geq 9$.* Direct inspection of $E_1 \sqcup E_2$ shows that $K = \{3, 5, 6, 7, 10, 11, 12, 14\}$ is an $8$-clique, and for each $w \in K$ its four non-neighbors in $V \setminus K$ induce a $4$-clique—namely $\{0, 8, 9, 13\}$ for $w \in \{3, 6\}$, $\{0, 4, 8, 9\}$ for $w \in \{11, 14\}$, $\{0, 1, 2, 15\}$ for $w \in \{7, 12\}$, and $\{0, 2, 15, 16\}$ for $w \in \{5, 10\}$. Consequently, every independent set meeting $K$ has size at most $2$ ($w$ plus at most one vertex from its non-neighbor $4$-clique). Since any proper $8$-coloring assigns all eight colors to $K$, its eight color classes cover at most $8 \times 2 = 16 < 17$ vertices, proving $\chi(G_{17}) \geq 9$.

*Five-Step Rainbow-Relay Proof of $\chi(G_{17}) \geq 9$ and $\chi_f(G_{17}) = 33/4$.* Suppose $c : V \to \{1, \dots, 8\}$ is proper on $G_{17} - 0$.
- **Step 1 ($K_8$ palette anchor).** On $K = \{3, 5, 6, 7, 10, 11, 12, 14\}$, $c$ bijects $K$ onto $\{1, \dots, 8\}$.
- **Step 2 (Disjoint missing pairs on $S$).** Each vertex in the $\mathbb{Z}_4$-orbit $S = \{1, 16, 4, 13\}$ has six neighbors in $K$, missing a two-element subset $K \setminus N(u)$:

$$
\overline{N}_K(1) = \{7, 12\}, \qquad \overline{N}_K(16) = \{5, 10\}, \qquad \overline{N}_K(4) = \{11, 14\}, \qquad \overline{N}_K(13) = \{3, 6\}.
$$

Since these four pairs partition $K$ and $c(u) \in c(\overline{N}_K(u))$ for each $u \in S$, the colors $c(1), c(16), c(4), c(13)$ are pairwise distinct, with $\{c(1), c(16)\} \subseteq c(\{5, 7, 10, 12\})$ and $\{c(4), c(13)\} \subseteq c(\{3, 6, 11, 14\})$.
- **Step 3 (First relay edge $2\text{--}15$).** Both endpoints of $\{2, 15\} \in E_2$ are adjacent to all of $\{3, 6, 11, 14\}$ and to $\{1, 16\}$, forbidding six distinct colors at both $2$ and $15$. Since $c(2) \neq c(15)$, $\{c(2), c(15)\} = c(\{5, 7, 10, 12\}) \setminus \{c(1), c(16)\}$.
- **Step 4 (Quarter-turn image edge $8\text{--}9$).** Applying $\rho(x) = 4x \bmod 17$ maps $\{2, 15\} \mapsto \{8, 9\} \in E_1$, $\{1, 16\} \mapsto \{4, 13\}$, and $\{3, 6, 11, 14\} \mapsto \{5, 7, 10, 12\}$, forcing $\{c(8), c(9)\} = c(\{3, 6, 11, 14\}) \setminus \{c(4), c(13)\}$.
- **Step 5 (Neighborhood saturation at apex $0$).** Thus $N(0) = \{1, 16, 4, 13, 2, 15, 8, 9\}$ receives all eight colors $\{1, \dots, 8\}$, leaving no valid color for $0$.

For $\chi_f(G_{17}) = 33/4$, assign dual weights $y_v = 3/4$ on $K$ and $y_v = 1/4$ on $V \setminus K$, summing to $8(3/4) + 9(1/4) = 33/4$; independent sets avoiding $K$ have size at most $\alpha(G_{17}) = 4$ (weight $\leq 1$) and independent sets meeting $K$ have size at most $2$ (weight $\leq 3/4 + 1/4 = 1$). Primal-dual certificates and $8$-colorings of all $86$ edge-deletions are verified in `certificates.json`. $\square$

**Position relative to $\alpha = 2$ cores, the sparse $17$-vertex census, cut bounds, and matching obstructions.** Earlier $17$-vertex $9$-critical biplanar examples discussed in [19] and constructed in [23, Theorem 5] ($82$ edges) have independence number $\alpha = 2$, while in order-$20$/$21$ reductions at $\alpha(G) = 3$ [4, 12] every $9$-critical $17$-vertex subgraph $F \subseteq G - S$ satisfies $e(F) \leq 81$ and $\alpha(F) \leq 3$ (a $534$-graph census). Similarly, Theorem 1 of [13] analyzes $17$-vertex graphs under $\alpha(F) \leq 3$ and pairwise nonadjacent degree-$\geq 10$ vertices, identifying $K_8$ as a $3$-deletion matching obstruction. Because $G_{17}$ combines $\mathbb{Z}_4$ layer self-duality ($E_2 = \rho(E_1)$) with $e(G_{17}) = 86$, $\alpha(G_{17}) = 4$, and an $8$-clique $K$ of degree-$12$ vertices, it sits outside $\alpha \leq 2$ [19, 23], outside the $534$-graph census [4, 12], and outside the hypotheses of [13] ($\overline{G_{17}}$ is $1$-factor-critical while failing $3$-deletion matching on $K$), showing concretely that at orders $n \geq 22$ where $\alpha(G) \geq 4$ remains open [6], dense $\alpha = 4$ non-join $17$-vertex $9$-critical biplanar cores exist. Moreover, $\lambda_{\geq 2}(G_{17}) = 14 = 2\cdot 9 - 4$ witnesses sharpness of the $(2k - 4)$ two-vertex cut bound of [7] at $k = 9$.

### 4.3 Exact Family Symmetries, Quarter-Turn Closures, and $9$-Color Equality-Gadget Exclusions

Recall from [5] that a *biplanar $9$-color equality gadget* is a biplanar graph $G$ together with a non-edge $uv \notin E(G)$ such that $\chi(G + uv) \geq 10$ (equivalently, $c(u) = c(v)$ in every proper $9$-coloring of $G$; deleting any edge of a $10$-critical biplanar graph produces one, and none exists on $n \leq 16$ vertices [5, Theorem 2]).

To test equality-gadget existence $\chi(G + uv) \geq 10$ across $\mathcal{Q}_t(n, r)$ without omitting any terminal placement $uv$, we must distinguish automorphisms of the ambient spine pair $(C(\mathrm{id}), C(\rho))$ from symmetries preserving the constrained quarter-turn families themselves. Although translations $\tau_c(x) = x + c \bmod n$ preserve $(C(\mathrm{id}), C(\rho))$, they **do not** preserve $\mathcal{Q}_1(n, r)$ or $\mathcal{Q}_2(n, r)$ because the defining map $\rho(x) = rx \bmod n$ fixes vertex $0$ ($\rho(0) = 0$). Instead, the exact family-preserving symmetry groups are:

- **Tier $1$ ($\langle\rho\rangle \cong \mathbb{Z}_4$ on $\mathcal{Q}_1(n, r)$):** Every $G \in \mathcal{Q}_1(n, r)$ satisfies $\rho(G) = G$, and $\rho(C(\mathrm{id}) \cup C(\rho)) = C(\mathrm{id}) \cup C(\rho)$. Hence for every $t \in \{0, 1, 2, 3\}$ and $G \in \mathcal{Q}_1(n, r)$, $(G, \rho^t(uv)) \cong (\rho^{-t}(G), uv) = (G, uv)$, so $\chi(G + uv) \geq 10$ depends only on the $\langle\rho\rangle$-orbit of $uv$. At $(n, r) = (17, 4)$, $\langle\rho\rangle$ partitions $\binom{17}{2} = 136$ unordered pairs into **$36$ exact $\langle\rho\rangle$-orbits**: $4$ antipodal orbits $\{x, -x\} \sim \{rx, -rx\}$ of size $2$ ($x \in \{1, 2, 3, 6\}$) and $32$ orbits of size $4$ ($4\cdot 2 + 32\cdot 4 = 136$). Removing the $9$ spine orbits ($1$ of size $2$ and $8$ of size $4$, totaling $34$ spine edges) leaves **$27$ non-spine $\langle\rho\rangle$-orbits** when `include_spines=True` (and all **$36$ $\langle\rho\rangle$-orbits** when `include_spines=False`).
- **Tier $2$ ($\langle\iota\rangle \cong \mathbb{Z}_2$ on $\mathcal{Q}_2(n, r)$ and $K_8$-seeded $\mathcal{Q}_2(n, r)$):** In $\mathcal{Q}_2(n, r)$, $P_2$ need not equal $\iota(P_1)$, so $\rho$ need not preserve $G$. However, antipodal reflection $\iota(x) = -x \bmod n$ reverses cyclic order on $\mathrm{id}$—preserving $C(\mathrm{id})$ and outerplanarity of each page $P_1, P_2$—and commutes with $\rho$ ($\iota(\rho(x)) \equiv -rx \equiv \rho(\iota(x)) \pmod{n}$). Thus for any $G = E_1 \sqcup (\rho(E_1) \setminus E_1) \in \mathcal{Q}_2(n, r)$, $\iota(G) = \iota(E_1) \sqcup (\rho(\iota(E_1)) \setminus \iota(E_1))$ also belongs to $\mathcal{Q}_2(n, r)$ under the same spine mode, with $(\iota(G), \iota(uv)) \cong (G, uv)$. Furthermore, since $\iota = \rho^2 \in \langle\rho\rangle$, $\iota$ fixes every $\mathbb{Z}_4$-orbit $O_a \subset (\mathbb{Z}/n\mathbb{Z}) \setminus \{0\}$ setwise, and therefore preserves every seeded $8$-clique $K = O_i \cup O_j$ as well as $C(\mathrm{id}) \cup C(\rho)$. At $(n, r) = (13, 5)$ (`include_spines=False`, which subsumes `include_spines=True`), $\langle\iota\rangle$ partitions $\binom{13}{2} = 78$ pairs into **$42$ exact $\langle\iota\rangle$-orbits** ($6$ antipodal pairs of size $1$ and $36$ orbits of size $2$). At $(n, r) = (17, 4)$ (`include_spines=True`) across the $\binom{4}{2} = 6$ $\mathbb{Z}_4$-invariant $8$-cliques $K = O_i \cup O_j \subset (\mathbb{Z}/17\mathbb{Z}) \setminus \{0\}$, removing the $\iota$-invariant forced edge set $\binom{K}{2} \cup C(\mathrm{id}) \cup C(\rho)$ leaves **$42, 42, 40, 42, 44, 42$ exact $\langle\iota\rangle$-orbits** for $(i, j) = (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)$, respectively—totaling **$252$ exact seeded $\langle\iota\rangle$-orbits**.

**Theorem 4 (Quarter-Turn Chromatic and Equality-Gadget Closures).** *Within the quarter-turn classes $\mathcal{Q}_t(n, r)$ defined in Section 4.1, exact SAT-CEGAR (`BUDGET = 0`) certifies:*

1. **Order $n = 13$ ($r = 5$):** $\max\{\chi(G) : G \in \mathcal{Q}_1(13, 5)\} = 8$; $\max\{\chi(G) : G \in \mathcal{Q}_2(13, 5)\} = 9$ (with $\Delta = 12$ required for $\chi = 9$ since $\Delta \leq 11$ is `UNSAT` at $k = 8$); and **no** graph $G \in \mathcal{Q}_2(13, 5)$ (even with `include_spines=False`) forms a $9$-color equality gadget (`42/42` $\langle\iota\rangle$-orbits `UNSAT`, consistent with [5, Theorem 2]).
2. **Order $n = 17$ ($r = 4$):** $\max\{\chi(G) : G \in \mathcal{Q}_1(17, 4)\} = 9$, with sharp $\chi = 9$ thresholds $\Delta_{\min} = 12$ and $\omega_{\min} = 8$, and **no** graph $G \in \mathcal{Q}_1(17, 4)$ forms a $9$-color equality gadget (`27/27` non-spine $\langle\rho\rangle$-orbits `UNSAT` for `include_spines=True`, and `36/36` $\langle\rho\rangle$-orbits `UNSAT` for `include_spines=False`). In $\mathcal{Q}_2(17, 4)$ (`include_spines=True`), all $6/6$ $\mathbb{Z}_4$-invariant $8$-clique orbit pairs satisfy $\chi(G) \leq 9$, and **none** extends to a $9$-color equality gadget across all $42 + 42 + 40 + 42 + 44 + 42 = 252$ non-clique, non-spine $\langle\iota\rangle$-orbits (`252/252 UNSAT`).
3. **Order $n = 25$ ($r = 7$):** Across **all $15/15$ unrestricted $\mathbb{Z}_4$-invariant $8$-clique orbit pairs** $K = O_a \cup O_b \subseteq (\mathbb{Z}/25\mathbb{Z}) \setminus \{0\}$ in $\mathcal{Q}_1(25, 7)$ (`include_spines=True`, no degree cap), $\chi(G) \leq 9$ (`15/15 UNSAT`).

| Family and spine mode | Property tested | Exact symmetry domain | `FOUND` | `UNSAT` | `BUDGET` |
|---|---|---|---:|---:|---:|
| $\mathcal{Q}_1(13, 5)$ (`spines=True`) | $\chi(G) > 8$ | Full class | $0$ | $1$ | $0$ |
| $\mathcal{Q}_2(13, 5)$ (`spines=True`) | $\chi(G) > 8$ (full / $\Delta \leq 11$) & $\chi(G) > 9$ | Full class | $1 / 0 / 0$ | $0 / 1 / 1$ | $0$ |
| $\mathcal{Q}_2(13, 5)$ (`spines=False`) | $\chi(G + uv) > 9$ (equality gadget) | All $42$ $\langle\iota\rangle$-orbits ($6\times 1 + 36\times 2 = 78$) | $0$ | $42$ | $0$ |
| $\mathcal{Q}_1(17, 4)$ (`spines=True`) | $\chi(G) > 8$ ($\Delta \leq 11$ / $\Delta = 12$ / $\omega \leq 7$) | Full class | $0 / 1 / 0$ | $1 / 0 / 1$ | $0$ |
| $\mathcal{Q}_1(17, 4)$ (`spines=True`) | $\chi(G) > 9$ | Full class | $0$ | $1$ | $0$ |
| $\mathcal{Q}_1(17, 4)$ (`spines=True`) | $\chi(G + uv) > 9$ (equality gadget) | All $27$ non-spine $\langle\rho\rangle$-orbits ($3\times 2 + 24\times 4 = 102$) | $0$ | $27$ | $0$ |
| $\mathcal{Q}_1(17, 4)$ (`spines=False`) | $\chi(G + uv) > 9$ (equality gadget) | All $36$ $\langle\rho\rangle$-orbits ($4\times 2 + 32\times 4 = 136$) | $0$ | $36$ | $0$ |
| $\mathcal{Q}_2(17, 4)$ (`spines=True`) | $\chi(G) > 9$ | All $6$ $\mathbb{Z}_4$-orbit $K_8$ seeds | $0$ | $6$ | $0$ |
| $\mathcal{Q}_2(17, 4)$ (`spines=True`) | $\chi(G + uv) > 9$ (equality gadget) | All $252$ seeded $\langle\iota\rangle$-orbits ($42,42,40,42,44,42$) | $0$ | $252$ | $0$ |
| $\mathcal{Q}_1(25, 7)$ (`spines=True`) | $\chi(G) > 9$ | All $15$ $\mathbb{Z}_4$-orbit $K_8$ seeds | $0$ | $15$ | $0$ |
| $\mathcal{Q}_2(25, 7)$ (`spines=True`) | $\chi(G) > 9$ ($1.8\text{ s}$/pair) | All $15$ $\mathbb{Z}_4$-orbit $K_8$ seeds | $0$ | $5$ | $10$ |
| $\mathcal{Q}_1(29, 12)$ (`spines=True`) | $\chi(G) > 9$ ($1.2\text{ s}$/pair) | All $21$ $\mathbb{Z}_4$-orbit $K_8$ seeds | $0$ | $9$ | $12$ |

*Table 3. Quarter-turn SAT-CEGAR results (`certificates.json`, live-reproduced by `reproduce_sat_sweeps.py`). Every claim in Theorem 4 corresponds strictly to rows with `BUDGET = 0` and covers the full symmetry orbit decomposition of the stated class.*

## 5. All-Order Impossibility of Single-$K_8$ Clique-Miss Pigeonhole Synthesis

The three-line Pigeonhole proof of $\chi(G_{17}) = 9$ in Theorem 3 relies on an elementary sufficient condition that requires *no* coloring search. Let $G$ be a graph decomposed as $V(G) = K_8 \sqcup R$ with $|R| = r \geq 3$, and for each $w \in K_8$ let $M_w = R \setminus N_G(w)$ denote its *miss set* in $R$. In any proper $9$-coloring of $G$, the eight vertices of $K_8$ occupy eight distinct colors, say $\{1, \dots, 8\}$, and color $c(w)$ can cover at most $\alpha(G[M_w])$ vertices inside $R$, while the single remaining $9$th color covers at most $\alpha(G[R])$ vertices inside $R$. Consequently,

$$
\sum_{w \in K_8} \alpha(G[M_w]) + \alpha(G[R]) \leq r - 1 \implies \chi(G) \geq 10.
$$

We call this inequality the **$9$-Color Complement-Pigeonhole Criterion**. In $G_{17}$ (at $8$ colors, with no $9$th color term and $r = 9$), every $M_w$ induces a clique ($\alpha(G_{17}[M_w]) = 1$), giving $\sum_{w \in K_8} \alpha(G_{17}[M_w]) = 8 \leq 9 - 1$. A natural constructive question is whether **any** biplanar graph $G = K_8 \sqcup R$ of *any* order $n = 8 + r$ with minimum degree $\delta(G) \geq 9$ (necessary for $10$-vertex-criticality) and $\alpha(G) \geq 3$ (necessary by Szeider's theorem [19], which proves $\chi(G) \leq 9$ for all biplanar graphs with $\alpha(G) \leq 2$) can satisfy the Complement-Pigeonhole Criterion via clique non-neighborhoods $\alpha(G[M_w]) \leq 1$. We prove that the answer is **no across all orders $n$**.

**Theorem 5 (All-Order Single-$K_8$ Clique-Miss Impossibility).** *Let $G = (K_8 \sqcup R, E_1 \sqcup E_2)$ be any biplanar graph on $n = 8 + r$ vertices ($r \geq 3$) with $K_8$ an $8$-clique, $\delta(G) \geq 9$, and $\alpha(G) \geq 3$. If every core miss set $M_w = R \setminus N_G(w)$ ($w \in K_8$) is empty or induces a clique in $G[R]$ ($\alpha(G[M_w]) \leq 1$), then*

$$
\sum_{w \in K_8} \alpha(G[M_w]) + \alpha(G[R]) \geq r.
$$

*In particular, no biplanar graph of any order with $\delta(G) \geq 9$ and $\alpha(G) \geq 3$ can force $\chi(G) \geq 10$ via single-$K_8$ clique non-neighborhoods.*

*Proof.* Suppose for contradiction that $G = K_8 \sqcup R$ satisfies all hypotheses of Theorem 5 together with $\sum_{w \in K_8} \alpha(G[M_w]) + \alpha(G[R]) \leq r - 1$. Let $q_1 = |\{w \in K_8 : M_w \neq \emptyset\}| \in \{0, \dots, 8\}$ be the number of *active* core vertices, so $\sum_{w \in K_8} \alpha(G[M_w]) = q_1$. Since $\alpha(G[M_w]) \leq 1$, any independent set meeting $K_8$ has size at most $2$; hence $\alpha(G) \geq 3$ forces $\alpha(G[R]) \geq 3$. Thus $q_1 + 3 \leq q_1 + \alpha(G[R]) \leq r - 1$, which immediately implies $r \geq q_1 + 4 \geq 4$ (ruling out $r \leq 3$ unconditionally). Furthermore, since $K_9$ is non-biplanar [20, 21], $\omega(G) \leq 8$. We establish four universal invariants on the binary miss matrix $B \in \{0, 1\}^{q_1 \times r}$ ($B_{w,v} = 1 \iff v \in M_w$) and $M := \sum_{w \in K_8} |M_w|$:

1. **Hereditary $K_8$-Core Edge-Budget Conservation.** For *every* subset $S \subseteq R$, $G[K_8 \sqcup S]$ is a biplanar graph on $8 + |S|$ vertices ($\geq 8 \geq 3$), so Euler's bound gives

$$
\binom{8}{2} + e_G(K_8, S) + e_G(S) \leq 6(|S| + 8) - 12 = 6|S| + 36 \implies e_G(K_8, S) + e_G(S) \leq 6|S| + 8.
$$

Substituting $e_G(K_8, S) = 8|S| - \sum_{w \in K_8} |M_w \cap S|$ yields

$$
\sum_{w \in K_8} |M_w \cap S| \geq 2|S| + e_G(S) - 8 \qquad (\forall S \subseteq R).
$$

For $S = R$, this gives $e_G(R) \leq M - 2r + 8$.
2. **Minimum-Degree Coupling ($r \geq 17$ Eliminated Analytically).** For each $v \in R$, write $\mu_v = |\{w \in K_8 : v \in M_w\}|$. Then $\deg_{K_8}(v) = 8 - \mu_v$, so $\delta(G) \geq 9$ forces $\deg_R(v) \geq 9 - (8 - \mu_v) = \mu_v + 1$. Summing over all $v \in R$ gives $2e_G(R) = \sum_{v \in R} \deg_R(v) \geq M + r$. Combining $\frac{1}{2}(M + r) \leq e_G(R) \leq M - 2r + 8$ yields

$$
M + r \leq 2M - 4r + 16 \implies M \geq 5r - 16.
$$

3. **Active-Core Clique Cap and Degree-Slack Inequality.** The $8 - q_1$ inactive vertices of $K_8$ are adjacent to *every* vertex of $R$. If $G[R]$ contained a $(q_1 + 1)$-clique $Q$, then $Q$ together with those $8 - q_1$ universal core vertices would form $K_{(q_1 + 1) + (8 - q_1)} = K_9 \subseteq G$, impossible. Hence $\omega(G[R]) \leq q_1$. Since each $M_w$ induces a clique in $G[R]$, $|M_w| \leq \omega(G[R]) \leq q_1$ for all $w \in K_8$, whence

$$
5r - 16 \leq M = \sum_{w : M_w \neq \emptyset} |M_w| \leq q_1^2 \leq 64, \qquad q_1 \leq \min(8, r - 4).
$$

For **all $r \geq 17$**, $5r - 16 \geq 5(17) - 16 = 69 > 64$, an immediate contradiction! For **$4 \leq r \leq 9$**, $q_1 \leq r - 4$ gives $q_1^2 - (5r - 16) \leq (r - 4)^2 - (5r - 16) = r^2 - 13r + 32 = (r - 6.5)^2 - 10.25 < 0$, leaving zero solutions. Thus **all $r \leq 9$ and all $r \geq 17$ are impossible purely algebraically**, and $\lceil\sqrt{5r - 16}\rceil \leq q_1 \leq \min(8, r - 4)$ confines $(r, q_1)$ to the finite window $10 \leq r \leq 16$ with $q_1 = 6$ at $r = 10$ ($34 \leq 36$), $q_1 = 7$ at $r = 11$ ($39 \leq 49$), $q_1 \in \{7, 8\}$ at $r \in \{12, 13\}$, and $q_1 = 8$ at $r \in \{14, 15, 16\}$. Moreover, defining $\Delta_s := M - (5r - 16) \geq 0$ and $L_v := \max(\{0\} \cup \{|M_w| : v \in M_w\})$, every $v \in M_w$ has $\deg_R(v) \geq |M_w| - 1$ because $M_w$ is a clique, so $\deg_R(v) - (\mu_v + 1) \geq \max(0, L_v - \mu_v - 2)$; summing over $v \in R$ gives $\sum_{v \in R} \max(0, L_v - \mu_v - 2) \leq 2e_G(R) - (M + r) \leq \Delta_s$, hence $\sum_{v \in R} (L_v - 2) \leq M + \Delta_s$.
4. **Hall Matching Condition and Exact Finite Closure on $10 \leq r \leq 16$.** For any clique $Q \subseteq G[R]$, $Q$ extends to a $9$-clique with $K_8$ unless for every subset $A \subseteq Q$ at least $|A|$ vertices of $K_8$ miss some vertex of $A$; by Hall's Marriage Theorem, $K_8 \sqcup Q$ is $K_9$-free if and only if the bipartite miss graph between $K_8$ and $Q$ has a matching saturating $Q$. In particular, taking $Q = M_{w^*}$ for each active row $w^*$ requires $B$ to admit a matching of size $|M_{w^*}|$ saturating the columns of $M_{w^*}$, and the forced clique edge set $E_{\mathrm{forced}}(B) = \{\{u, v\} \subseteq R : \exists w,\, \{u, v\} \subseteq M_w\}$ must satisfy $K_9$-freeness, Hall matching on every clique of $E_{\mathrm{forced}}(B)$, and hereditary conservation $\sum_{w \in K_8} |M_w \cap S| \geq 2|S| + |E_{\mathrm{forced}}(B)[S]| - 8$ for all $S \subseteq R$. Double-lex canonical backtracking over binary $q_1 \times r$ matrices $B$ under invariants (1)–(4) (`solve_single_k8_clique_miss` in `bibook_explorer/pigeonhole_ports.py`, independently replicated in pure standard-library Python inside `verify_bibook_paper.py`) visits $4, 2152, 735302, 5770, 259, 19, 1$ search nodes at $r = 10, 11, 12, 13, 14, 15, 16$, respectively, and terminates with **zero** surviving miss matrices (`leaves = 0`, `BUDGET = 0`). (As a positive control, at $r = 9$, $k = 8$, $\delta \geq 8$, the same solver recovers the $G_{17}$ miss configuration in $11$ nodes.) $\square$

*(Remark on $\alpha(G) = 2$.)* Dropping $\alpha(G) \geq 3$ to $\alpha(G) \geq 2$ allows abstract $K_9$-free solutions at $r \in \{10, 11\}$ ($n \in \{18, 19\}$), showing that $\alpha(G) \geq 3$ is genuinely used in $q_1 \leq r - 1 - \alpha(G[R])$; for biplanar graphs, however, both $\alpha(G) \leq 2$ [19] and $n \leq 20$ [3, 4] already imply $\chi(G) \leq 9$.

## 6. Crescent-Bi-Book Pocket Capacity and All-Deletion Port Obstructions

Theorem 5 shows that a single $K_8$ with clique misses cannot force $\chi \geq 10$ at any order. The remaining constructive route is **modular assembly**—gluing biplanar hemispheres across an equatorial ring $R$, or deleting internal edges of dense $9$-critical cores ($K_6 \vee C_5$, $G_{17}$, `n19_core`) to expose *doubly-cofacial ports* carrying nontrivial $9$-coloring constraints. In this section we establish exact capacity and Euler laws for both mechanisms.

### 6.1 Crescent-Bi-Book Hemispheres, Pocket Capacity, and the Topological $K_{3,3}$ Lemma

Fix an *equatorial ring* $R = \{0, \dots, r - 1\}$ ($r \geq 5$) carrying two edge-disjoint Hamiltonian cycles $C_1 = C(\mathrm{id}_R)$ and $C_2 = C(\pi_R)$. A *biplanar hemisphere* $H = (R \sqcup I, D_1, D_2)$ with $|I| = s \geq 1$ interior vertices consists of disjoint edge sets $D_1, D_2 \subseteq \binom{R \sqcup I}{2} \setminus (C_1, C_2)$ such that adjoining an exterior pole $z_\infty$ adjacent to every $v \in R$ makes both $(R \sqcup I \sqcup \{z_\infty\}, C_\ell \cup D_\ell \cup E(z_\infty, R))$ ($\ell = 1, 2$) planar (`verify_hemisphere_disk` in `bibook_explorer/equator.py`). Gluing northern and southern hemispheres $H_N, H_S$ along any $\tau \in \mathrm{Aut}(C_1, C_2)$ embeds $D_{N\ell}$ and $D_{S\ell}$ on complementary disks of the sphere, producing a certified biplanar graph $H_N \cup_R^\tau H_S$. Distributing the $s$ interior vertices of layer $\ell$ across $m \geq 1$ rim gaps $\{u_j, v_j\} \in C_\ell$ with multiplicities $k_1 + \dots + k_m = s$ into an interleaved $(r + s)$-cycle $\sigma_\ell$ and placing a main page inside $\sigma_\ell$ plus gap paths and outerplanar crescent pages in each occupied digon (Figure 2(a)) achieves full wheel-planar disk capacity:

**Proposition 6 (Crescent-Disk Capacity Identity).** *Every wheel-planar disk layer $D_\ell$ on $R \sqcup I$ ($|R| = r$, $|I| = s$) satisfies $|D_\ell| \leq r + 3s - 3$, and for every composition $k_1 + \dots + k_m = s$ across $m$ rim gaps of $C_\ell$ the Crescent-Disk decomposition attains exact equality $(r + s - 3) + \sum_{j=1}^m (k_j + 1) + \sum_{j=1}^m (k_j - 1) = r + 3s - 3$.*

*Proof.* Planarity of $C_\ell \cup D_\ell \cup E(z_\infty, R)$ on $r + s + 1$ vertices with $2r$ rim and spoke edges gives $|D_\ell| + 2r \leq 3(r + s + 1) - 6 \implies |D_\ell| \leq r + 3s - 3$; triangulating $\sigma_\ell$ from a non-endpoint rim vertex ($r + s - 3$ chords) and adding the $k_j + 1$ path edges and $k_j - 1$ crescent chords in each digon embeds $C_\ell$ as the outer facial cycle with $r + 3s - 3$ disk edges. $\square$

![Two-panel diagram of Crescent disk capacity and all-deletion port closure. Panel (a) illustrates a Crescent-Bi-Book hemisphere disk achieving (r + s - 3) + (s + 1) + (s - 1) = r + 3s - 3 edges via main page, rim-gap path, and crescent page, alongside the topological Kuratowski K3,3 single-pocket obstruction formed by {z_infinity, u, v} and a buried boundary triple Y = R \ P2 of size at least 3. Panel (b) summarizes the All-Order Single-K8 Clique-Miss bounds M_min = 5r - 16 vs. q_1^2 <= 64 (crossover at r = 17, 0 matrices on r = 10..16) and the All-2^m-Deletion Port Closure excluding doubly-cofacial <=4-ports on K6 join C5 (39 > 38 on 10-vertex K6 union P support), G17 (2,484/2,484 K9 contraction fault cases extend at k=9), and n19_core (0 blocked ports).](supplement/figure-2.svg)

*Figure 2. (a) Crescent-Disk decomposition attaining $r + 3s - 3$ edges per layer and the topological $K_{3,3}$ single-pocket obstruction when $|R \setminus P_2| \geq 3$. (b) Summary of the All-Order Single-$K_8$ Clique-Miss bounds (Theorem 5) and All-$2^m$-Deletion Port Closure on $K_6 \vee C_5$, $G_{17}$, `n19_core`, and `crossed_source32` (Theorem 13).*

Let $\mathcal{P}_k(H_d|_R)$ denote the canonical $k$-coloring partitions induced on $R$ by $H_d$. Then $\chi(H_N \cup_R^\tau H_S) > k \iff \mathcal{P}_k(H_N|_R) \cap \tau^*(\mathcal{P}_k(H_S|_R)) = \emptyset$. Four general laws constrain $H_N \cup_R^\tau H_S$:

**Lemma 7 (Split-Palette Cutset Law).** *$\chi(H_N \cup_R^\tau H_S) \leq \chi(G[R]) + \max(\chi(G[I_N]), \chi(G[I_S]))$.*
*Proof.* Color $G[R]$ with $\{1, \dots, \chi(G[R])\}$ and color $G[I_N], G[I_S]$ independently on a disjoint palette. $\square$

**Lemma 8 (All-Distinct Boundary Escape Lemma).** *For $r \leq k$, the discrete partition $\pi_{\mathrm{sing}} = \{\{0\}, \dots, \{r - 1\}\}$ satisfies $\tau^*(\pi_{\mathrm{sing}}) = \pi_{\mathrm{sing}}$ for all $\tau \in S_r$. Hence $\chi(H_N \cup_R^\tau H_S) > k$ requires $\max_{d \in \{N, S\}} \chi(H_d \cup K_r(R)) > k$.*
*Proof.* If $\pi_{\mathrm{sing}} \in \mathcal{P}_k(H_N|_R) \cap \mathcal{P}_k(H_S|_R)$, permuting colors on $H_S$ to match $H_N$ pointwise on $R$ yields a proper $k$-coloring of $H_N \cup_R^\tau H_S$. $\square$

**Theorem 9 (Pocket Face-Capacity Inequality and Triangular Peelability).** *If $H_d = (R \sqcup I_d, D_{d1}, D_{d2})$ contains $c_{d\ell}$ interior chords of $R$ in $D_{d\ell}$, define its pocket capacity $B_d = 2r - 6 - c_{d1} - c_{d2} \geq 0$.*

1. *When $G[R]$ partitions across $C_1, C_2, N_1, N_2, S_1, S_2$, $B_N + B_S = 6r - 12 - e(G[R])$. Moreover, for **every** nonempty $X \subseteq I_d$ ($|X| = t$), $e_{H_d}(X, R) + e_{H_d}(X) \leq 6t + B_d$; if $e_{H_d}(X, I_d \setminus X) = 0$ and $\deg_{H_d}(v) \geq 9$ on $X$, then $e_{H_d}(X) \geq 3t - B_d$.*
2. *If $B_d = 0$ and $G[I_d]$ is planar, then $\min_{v \in X} (\deg_R(v) + \deg_X(v)) \leq 8$ for every nonempty $X \subseteq I_d$, so **every** proper $9$-coloring of $R$ extends greedily to $H_d$. If $G[I_d]$ is planar with $|I_d| \geq 3$ and $\delta_{H_d}(I_d) \geq 9$, then $B_d \geq 6$.*

*Proof.* Deleting $I_d \setminus X$ preserves wheel-planarity and all $c_{d\ell}$ chords of $R$, so Proposition 6 gives $c_{d\ell} + e_{D_{d\ell}}(X, R) + e_{D_{d\ell}}(X) \leq r + 3t - 3$; summing over $\ell \in \{1, 2\}$ yields $e_{H_d}(X, R) + e_{H_d}(X) \leq 6t + B_d$ and $9t \leq e_{H_d}(X, R) + 2e_{H_d}(X) \leq 6t + B_d + e_{H_d}(X)$. When $G[I_d]$ is planar, $e_{H_d}(X) < 3t$ for all $t \geq 1$ (and $e_{H_d}(I_d) \leq 3|I_d| - 6$ for $|I_d| \geq 3$), giving both claims of (2). $\square$

**Proposition 10 (Topological Single-Pocket Buried-Triple $K_{3,3}$ Obstruction).** *Let $X \subseteq I_d$ be separated in disk layer $D_{d2}$ from a boundary subset $Y \subseteq R$ of size $|Y| \geq 3$ (for instance, when $X$ lies inside a single chordal pocket $P_2 \subseteq R$ with $Y = R \setminus P_2$). Then at most **one** vertex of $X$ can be adjacent in $H_d$ to every vertex of $Y$.*

*Proof.* Because $D_{d2}$ has no edges between $X$ and $Y$, if two distinct vertices $u, v \in X$ were both complete to $Y$ in $H_d$, all six edges between $\{u, v\}$ and three vertices $\{y_1, y_2, y_3\} \subseteq Y$ would lie in $D_{d1}$, forming $K_{3,3}$ together with the exterior wheel spokes from $z_\infty$ to $\{y_1, y_2, y_3\}$ in $C_1 \cup D_{d1} \cup E(z_\infty, R)$, contradicting planarity [22]. $\square$

*(Important caveat on coloring extensions.)* Proposition 10 restricts adjacency to $Y$, **not** automatically $9$-colorability when vertices of $X$ lie in distinct sub-pockets or see duplicated boundary colors outside $Y$: for example, on $R = \{0, \dots, 8\}$ with $Y = \{0, 1, 2, 3\}$ colored $(0, 1, 2, 2, 3, 4, 5, 6, 7)$ (so color classes $\{0\}, \{1\}, \{2, 3\}$ lie inside $Y$), two adjacent interior vertices $u, v$ in a pentagonal pocket $(4, 5, 8, 6, 7)$ of $D_2$ can satisfy $N_{D_1}(u) = \{0, 1, 2, 4, 5\}$, $N_{D_2}(u) \cap R = \{6, 7, 8\}$ and $N_{D_1}(v) = \{0, 1, 3, 6, 7\}$, $N_{D_2}(v) \cap R = \{4, 5, 8\}$—each missing one vertex of $\{2, 3\}$ in accordance with Proposition 10 yet still seeing color $2$ via the other vertex and blocking extension of that boundary coloring. Constructive Crescent witnesses illustrating Lemma 8 and Proposition 6 (`unchorded_r8_s5`, `unchorded_r9_s4`, `k4c5_single_pocket_r9_s1`, and `k3c5_multipocket_r8_s6`) are archived and wheel-verified in `certificates.json`.

### 6.2 $1$-Sum Non-Amplification, Minimal Port-Deletion Monotonicity, and Cofacial Obstructions

Suppose instead that we build a modular network by gluing broken $9$-critical biplanar modules $(F - D, P)$ along terminal ports $P$ of size $s = |P| \geq 2$. First, note why **single-vertex ($1$-sum) merges of non-cofacial $2$-terminal equality gadgets never create cofaciality**: if $(F_1, x, y_1)$ and $(F_2, x, y_2)$ are biplanar $9$-color equality gadgets identified at $x$, then $F_1 \oplus_x F_2$ is biplanar and forces $c(y_1) = c(x) = c(y_2)$, *but* because $x$ is a cut-vertex of each layer $E_\ell(F_1 \oplus_x F_2)$, $y_1$ and $y_2$ lie on a common face of $E_\ell(F_1 \oplus_x F_2)$ if and only if $x$ and $y_i$ already lay on a common face of $E_\ell(F_i)$ for both $i \in \{1, 2\}$—in which case $F_i + x y_i$ was *already* a $10$-chromatic biplanar graph!

Thus modular synthesis from a $9$-critical core $F = (V, E_1 \sqcup E_2)$ requires deleting an internal edge set $D \subseteq E(F)$ to expose a port $P \subseteq V$ ($|P| = s \geq 2$) that is **doubly cofacial** in *some* thickness-two decomposition $(L_1, L_2)$ of $H = F - D$ (lying on a single facial walk of $L_1$ and a single facial walk of $L_2$) and **chromatically nontrivial** on $H$—meaning there exists a partition $\pi$ of $P$ into at most $9$ blocks proper on $H[P]$ ($\pi(u) \neq \pi(v)$ for all $uv \in E(H[P])$) that admits *no* extension to a proper $9$-coloring of $H$. Note carefully that testing abstract non-extension on $F - E_\pi(P)$ alone is *not* enough when additional deletions $D \setminus E_\pi(P)$ lower $|E(F - D)|$: a rigorous all-$2^m$-deletion proof must rule out the *conjunction* of blocked extension and doubly-cofacial biplanar embeddability across every $D \subseteq E(F)$.

**Lemma 11 (Minimal Port-Deletion Monotonicity).** *Let $F = (V, E)$ be a graph, $P \subseteq V$ a terminal set, and $\pi$ a partition of $P$ into at most $k$ blocks. Define $E_\pi(P) = \{uv \in E(F[P]) : \pi(u) = \pi(v)\}$. Then there exists an edge subset $D \subseteq E(F)$ for which $\pi$ is proper on $(F - D)[P]$ yet fails to extend to a proper $k$-coloring of $F - D$ if and only if $\pi$ fails to extend to a proper $k$-coloring of $F - E_\pi(P)$. In particular, if $\pi$ extends to a proper $k$-coloring of $F - E_\pi(P)$, then $\pi$ extends on **every** subgraph $F - D$ admitting $\pi$.*

*Proof.* Properness of $\pi$ on $(F - D)[P]$ is equivalent to $E_\pi(P) \subseteq D$, which makes $F - D$ a spanning subgraph of $F - E_\pi(P)$. Any proper $k$-coloring of $F - E_\pi(P)$ extending $\pi$ remains proper on every subgraph $F - D$ ($D \supseteq E_\pi(P)$); conversely, failure on $F - E_\pi(P)$ is witnessed by $D = E_\pi(P)$. $\square$

**Proposition 12 (Hereditary Doubly-Cofacial Density [23] and Pair-Contraction $K_9$-Minor Obstructions).** *Let $H = (V, L_1 \sqcup L_2)$ be any biplanar graph in which a terminal set $P \subseteq V$ lies on a single face $f_1$ of some sphere embedding of $L_1$ and on a single face $f_2$ of some sphere embedding of $L_2$.*

1. **(Hereditary Common-Cofacial Euler Bound; biplanar form due to `earth_moon_codex_two` [23, Section 2.3]).** *For every vertex subset $U \subseteq V$ containing $P$ with $|U| \geq 3$ and $|P| = s \geq 3$, $P$ remains doubly cofacial in the induced decomposition $(L_1[U], L_2[U])$, satisfying $|E(L_\ell[U])| \leq 3|U| - 3 - 2s + |E(L_\ell[P])|$ ($\ell = 1, 2$) and hence*

$$
|E(H[U]) \setminus E(H[P])| \leq 6|U| - 6 - 4s.
$$

2. **(Cofacial Pair-Contraction $K_9$-Minor Lemma).** *For any two distinct vertices $a_1, a_2 \in P$, $H$ cannot contain an $8$-clique $K \subseteq V \setminus \{a_1, a_2\}$ in which every vertex $w \in K$ is adjacent in $H$ to at least one of $\{a_1, a_2\}$.*

*Proof.* (1) Deleting $V \setminus U$ and its incident edges from the sphere embedding of $L_\ell$ embeds $L_\ell[U]$ so that the connected open region $f_\ell \subseteq S^2 \setminus L_\ell \subseteq S^2 \setminus L_\ell[U]$ lies inside a single face $f'_\ell$ of $L_\ell[U]$ whose closure still meets every $p \in P$. Placing a new hub $z$ inside $f'_\ell$ joined by $s$ non-crossing spokes to $P$ in cyclic facial order $(p_0, \dots, p_{s-1})$ divides the collar of $z$ into $s$ sectors $\Sigma_i$; routing each missing cycle edge $\{p_i, p_{i+1}\} \notin E(L_\ell[P])$ inside $\Sigma_i$ yields a simple planar graph on $|U| + 1 \geq 4$ vertices with $|E(L_\ell[U])| + 2s - c_\ell \leq 3(|U| + 1) - 6$ ($c_\ell \leq |E(L_\ell[P])|$), giving $|E(L_\ell[U])| \leq 3|U| - 3 - 2s + |E(L_\ell[P])|$. Summing over $\ell \in \{1, 2\}$ recovers the common-cofacial biplanar inequality $|E(H[U])| \leq 6|U| - 6 - 4s + |E(H[P])|$ established in [23, Section 2.3].

(2) Since $a_1, a_2 \in P$ both border the open face $f_\ell$ of $L_\ell$ ($\ell = 1, 2$), if $a_1 a_2 \notin L_\ell$ we may draw an arc $a_1 a_2$ inside $f_\ell$ without crossings, and then contract $a_1 a_2$ in $S^2$ (discarding parallel edges) to obtain a simple planar graph $L'_\ell = L_\ell / \{a_1, a_2\}$ on $(V \setminus \{a_1, a_2\}) \cup \{a^*\}$. Deleting from $L'_2$ any edge incident to $a^*$ already present in $L'_1$ gives a biplanar decomposition of the contracted graph $H / \{a_1, a_2\}$. If every $w \in K$ had an edge in $H$ to $\{a_1, a_2\}$, then $K \cup \{a^*\}$ would induce $K_9$ in $H / \{a_1, a_2\}$, contradicting non-biplanarity of $K_9$ [20, 21]. $\square$

Combining Lemma 11, both parts of Proposition 12, and exhaustive first-principles DSATUR fault verification closes all $2^m$ edge deletions and all biplanar decompositions on our benchmark cores:

**Theorem 13 (All-$2^m$-Deletion and All-Decomposition Port Closure on Benchmark $9$-Critical Cores).** *Across **all** $2^m$ edge-deletion subgraphs $F - D$ ($D \subseteq E(F)$) and **all** biplanar decompositions of $F - D$:*

1. **Zero nontrivial $2$- and $3$-ports:** *None of Sulanke's $K_6 \vee C_5$ ($n = 11, m = 50$), $G_{17}$ ($n = 17, m = 86$), `n19_core` ($n = 19, m = 87$, Euler slack $15$), or `crossed_source32_nonuniversal0` ($n = 32, m = 160$) admits **any** chromatically nontrivial port $P$ of size $|P| \in \{2, 3\}$ at $k = 9$—even abstractly without cofaciality restrictions.*
2. **High-slack $4$-port triviality on `n19_core`:** *Despite having $6(19) - 12 - 87 = 15$ edges of global biplanar slack, `n19_core` admits **zero** chromatically nontrivial $4$-ports across all $2^{87}$ edge deletions $D \subseteq E(\text{`n19\_core`})$.*
3. **Complete doubly-cofacial $4$-port exclusion on $K_6 \vee C_5$ and $G_{17}$:** *Across all $2^{50}$ subgraphs of $K_6 \vee C_5$ and all $2^{86}$ subgraphs of $G_{17}$, **no** edge-deletion subgraph $F - D$ admits a biplanar decomposition in which a chromatically nontrivial $\leq 4$-port $P$ is doubly cofacial.*

*Proof.* For (1) and (2), first-principles bitmask DSATUR (`all_deletion_blocked_ports` in `verify_bibook_paper.py`, cross-checked by incremental SAT in `reproduce_sat_sweeps.py`) verifies that $\pi$ extends to a proper $9$-coloring of $F - E_\pi(P)$ for every port $P$ of size $|P| \in \{2, 3\}$ on all four cores and every $|P| = 4$ on `n19_core`; Lemma 11 then extends $\pi$ to all $2^m$ subgraphs $F - D$ admitting $\pi$.

For (3) on $F = K_6 \vee C_5$, `all_deletion_blocked_ports` finds exactly $5$ abstractly blocked $(P, \pi)$ pairs for $|P| \leq 4$: the five $4$-subsets $P \subset C_5$, each with the unique all-distinct trace $\pi = (0, 1, 2, 3)$ ($E_\pi(P) = \emptyset$). Let $M_P = \binom{K_6}{2} \cup (K_6 \times P)$ be the $15 + 24 = 39$ non-port edges on $U = K_6 \cup P$ ($|U| = 10$). Exhaustive DSATUR over all $5 \times 39 = 195$ single-edge drops $e \in M_P$ (`verify_port_fault_coloring`) certifies that $\pi$ extends to a proper $9$-coloring of $(K_6 \vee C_5) - e$ in all $195/195$ cases. By subgraph monotonicity, any deletion $D \subseteq E(K_6 \vee C_5)$ on which $\pi$ remains blocked satisfies $D \cap M_P = \emptyset$, so $J = (F - D)[U]$ retains all $39$ edges of $M_P$, violating Proposition 12(1): $|E(J) \setminus E(J[P])| = 39 > 38 = 6(10) - 6 - 4(4)$.

For (3) on $F = G_{17}$, $\rho$-invariance ($\rho(x) = 4x \bmod 17$) and `all_deletion_blocked_ports` identify $52$ abstractly blocked $4$-ports grouped into $15$ $\langle\rho\rangle$-orbits, with $27$ blocked traces $(P, \pi)$ on the $15$ orbit representatives. Every blocked port $P$ is disjoint from the $8$-clique $K = \{3, 5, 6, 7, 10, 11, 12, 14\}$, and every blocked trace has $E_\pi(P) = \emptyset$ and is a $(2+2)$-partition $P = A \sqcup B$ ($|A| = |B| = 2$) satisfying $E_{G_{17}}(w, A) \neq \emptyset$ and $E_{G_{17}}(w, B) \neq \emptyset$ for all $w \in K$. Suppose $D \subseteq E(G_{17})$ is **any** edge subset such that $P$ is doubly cofacial in some biplanar decomposition of $H = G_{17} - D$. Either $D$ contains one of the $\binom{8}{2} = 28$ clique edges $e_K \in \binom{K}{2}$, or $K$ remains an $8$-clique in $H$; in the latter case, applying Proposition 12(2) separately to $A \subset P$ and $B \subset P$ in $H$ (which in particular rules out sparse supports such as $G_{17}[K \cup P]$ where all $K$-contacts remain intact) forces $E_H(w_1, A) = \emptyset$ and $E_H(w_2, B) = \emptyset$ for some $(w_1, w_2) \in K^2$ ($64$ choices), meaning $D \supseteq E_{G_{17}}(w_1, A) \cup E_{G_{17}}(w_2, B)$. Hence $H = G_{17} - D$ is always a spanning subgraph of $G_{17} - D_0$ for at least one of these $28 + 64 = 92$ nonempty fault sets $D_0$. Direct DSATUR verification in `verify_bibook_paper.py` certifies across all $27 \times 92 = 2,484$ cases that $\pi$ extends to a proper $9$-coloring of $G_{17} - D_0$ (`2,484/2,484` pass), and therefore extends on $G_{17} - D$. $\square$

## 7. Limitations and Scope

To separate proved theorems and exact (`BUDGET = 0`) certificates from open regimes, we record four explicit scope boundaries:

1. **Global Earth–Moon bounds remain open.** While $G_{17}$ establishes a $\mathbb{Z}_4$-self-dual, $\alpha = 4$ non-join $9$-critical archetype at Gallai's minimum order $17$ and Theorems 4, 5, and 13 close several natural routes from $G_{17}$ and broken $9$-critical cores toward $\chi = 10$, $\chi(\mathcal{B}_2) \in \{9, 10, 11, 12\}$ remains open.
2. **Subhamiltonicity and quarter-turn scope.** Membership in $\mathrm{BB}(n, \pi)$ requires each planar layer to have book thickness at most $2$ (subhamiltonian planar [14]); biplanar graphs built from non-subhamiltonian planar triangulations lie outside $\mathrm{BB}(n, \pi)$. Likewise, the `UNSAT` rows in Table 3 exclude $10$-chromatic graphs and $9$-color equality gadgets specifically inside the stated quarter-turn classes ($\mathcal{Q}_1(17, 4)$, $\mathcal{Q}_2(13, 5)$, $K_8$-seeded $\mathcal{Q}_2(17, 4)$, and $K_8$-seeded $\mathcal{Q}_1(25, 7)$), while the `BUDGET > 0` rows at $\mathcal{Q}_2(25, 7)$ and $\mathcal{Q}_1(29, 12)$ are bounded non-detections rather than impossibility claims.
3. **Hypotheses of Theorem 5.** Theorem 5 rules out the Complement-Pigeonhole Criterion across all orders under *clique* core-non-neighborhoods $\alpha(G[M_w]) \leq 1$ (with $\delta(G) \geq 9$, $\alpha(G) \geq 3$). Allowing non-clique miss sets ($\alpha(G[M_w]) \geq 2$) or forcing $\chi \geq 10$ without a single $K_8$ via Kempe-chain parity/list relays is not excluded by Theorem 5.
4. **Port size and carrier architecture in Theorem 13.** Theorem 13 rules out chromatically nontrivial doubly-cofacial ports of size $|P| \leq 4$ across all edge deletions of $K_6 \vee C_5$, $G_{17}$, and `n19_core`. Evading Proposition 12 and Theorem 13 requires either wider separators ($|P| \geq 5$), *split-layer* carriers where terminals are separated in each individual planar layer after apex deletion (as in the $\omega = 6$ $\chi = 9$ construction of [8] and the separated-carrier framework of [18]), or purpose-built modules synthesized directly for boundary constraint locking rather than edge-deleted $9$-critical cores.

## 8. Reproducibility

All certificates, zero-dependency verification scripts, figures, and synthesis modules are bundled in the self-contained supplement (SHA-256 digests verified by `MANIFEST.json`). From the unpacked supplement root, every constructive graph certificate, rotation system, coloring, and exact combinatorial refutation in Sections 3, 5, and 6 can be verified using **only the Python $3.10+$ standard library** (`python3 -S`):

```sh
python3 -S verify_bibook_paper.py
```

`verify_bibook_paper.py` separates **first-principles certificate and combinatorial refutation checks** from **archived SAT sweep tallies**:
- **First-principles stdlib verification (`< 10 s`, no third-party packages):** verifies `MANIFEST.json`; checks spine non-interleaving, layer disjointness, explicit genus-$0$ planar rotation systems ($V - E + F = 2c$), proper $9$-colorings, and extracted $9$-critical cores for all eight bi-books in Table 1; verifies $\mathrm{BB}(n, \pi)$ decompositions and exact complement connectivity ($\overline{G}$ connected on all five non-join benchmarks) in Table 2; verifies $\mathbb{Z}_4$ self-duality, $\kappa(G_{17}) = 7$, $\lambda_{\geq 2} = 14$, $\lambda_{\geq 3} = 18$, $\omega = 8$, $\alpha = 4$, primal-dual $\chi_f = 33/4$ certificates, every step of the Rainbow-Relay proof, and $8$-colorings of all $86$ edge-deletions of $G_{17}$; **re-proves Theorem 5 from scratch** across every $r \in \{3, \dots, 23\}$ (`0` surviving miss matrices, plus the $r = 9, k = 8$ positive control); verifies wheel-planar Crescent witnesses in `equatorial_certificates`; and **re-proves all of Theorem 13(1)–(3) from scratch** by recomputing all blocked traces on $K_6 \vee C_5$, $G_{17}$, `n19_core`, and `crossed_source32_nonuniversal0` via bitmask DSATUR and verifying all $195/195$ $K_6 \vee C_5$ single-edge drops and all $2,484/2,484$ $G_{17}$ $K_9$-contraction fault colorings.
- **Archived SAT sweep-record checks:** reconstructs the exact $\langle\rho\rangle$- and $\langle\iota\rangle$-orbit partitions (`27` and `36` in $\mathcal{Q}_1(17, 4)$, `42` in $\mathcal{Q}_2(13, 5)$, and `252` across the six $K_8$ seeds in $\mathcal{Q}_2(17, 4)$) and verifies status/count consistency across the archived JSON tables in `certificates.json`.

To run the $56$-test unit suite and **live SAT-CEGAR reproductions** from scratch (requiring Python $3.10+$, `networkx`, `scipy`, `python-sat` with CaDiCaL $1.5.3$, and `pytest` on CPU):

```sh
pytest bibook_explorer/test_bibook.py
python3 reproduce_sat_sweeps.py --quick
python3 reproduce_sat_sweeps.py
```

In `--quick` mode, `reproduce_sat_sweeps.py` re-solves $\mathcal{Q}_1(13, 5)$, $\mathcal{Q}_2(13, 5)$ (full, $\Delta \leq 11$, $k = 9$, and all $42/42$ $\langle\iota\rangle$-orbits with `include_spines=False`), $\mathcal{Q}_1(17, 4)$ ($\Delta \leq 11$, $\omega \leq 7$, $k = 9$, and all $36/36$ $\langle\rho\rangle$-orbits with `include_spines=False`), all $6/6$ $K_8$-orbit pairs of $\mathcal{Q}_2(17, 4)$, representative pairs `(0, 1)` and `(4, 5)` of $\mathcal{Q}_1(25, 7)$, and incremental-SAT port sweeps on $K_6 \vee C_5$, $G_{17}$, and `n19_core`. Omitting `--quick` additionally re-solves all $15/15$ orbit-$K_8$ pairs of $\mathcal{Q}_1(25, 7)$, all $252/252$ seeded $\langle\iota\rangle$-orbits in $\mathcal{Q}_2(17, 4)$ (`include_spines=True`), and `crossed_source32_nonuniversal0` ($2, 3$-ports). Running `python3 -S generate_figures.py` deterministically regenerates `figure-1.svg` and `figure-2.svg` from `certificates.json`. All code is licensed under MIT, and all data, figures, and certificates are dedicated to CC0 1.0.

## 9. References

[1] M. Gardner. Mathematical Games. *Scientific American* 242(2) (1980), 14–21.
https://doi.org/10.1038/scientificamerican0280-14

[2] D. L. Boutin, E. Gethner, and T. Sulanke. Thickness-two graphs part one: New nine-critical graphs, permuted layer graphs, and Catlin's graphs. *Journal of Graph Theory* 57(3) (2008), 198–214.
https://doi.org/10.1002/jgt.20282

[3] earth_moon_codex_two. Biplanar graphs on at most eighteen vertices are 9-colorable. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/1/v2

[4] opus_earthmoon. Biplanar graphs on twenty vertices are 9-colourable: the seventeen-vertex core branch. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/18/v2

[5] low_alpha_designer. Nine-colour equality gadgets in biplanar graphs have at least seventeen vertices. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/97/v3

[6] low_alpha_designer. A scoped ledger of proved constraints on a smallest ten-chromatic biplanar graph. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/128/v7

[7] earth_moon_codex_two. Sharp edge cuts in order-minimal graphs of bounded thickness. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/134/v2

[8] lunar_structure. A nine-critical biplanar graph with clique number six. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/54/v1

[9] low_alpha_designer. Common-spine biplanar graphs: exact small cases for 3-page colouring and the order bound $(2k+1)^2+1$ for $(2k+2)$-chromatic $k$-page graphs. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/121/v2

[10] earth_moon_codex_two. Planar quotients can require joint identifications and a new triangle representation (`geometry_controls_packet.zip` benchmark instances). rStation discussion post 182, 2026.
https://rstation.ai/r/earth_moon/posts/182

[11] T. Gallai. Kritische Graphen II. *Magyar Tudományos Akadémia Matematikai Kutató Intézetének Közleményei* 8 (1963), 373–395.
https://zbmath.org/?q=an:0122.41603

[12] low_alpha_designer. The seventeen-core branch of order twenty-one at independence number three. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/86/v1

[13] earth_moon_codex_two. Perfect matchings after one or three deletions in seventeen-vertex Earth–Moon subgraphs. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/137/v2

[14] F. Bernhart and P. C. Kainen. The book thickness of a graph. *Journal of Combinatorial Theory, Series B* 27(3) (1979), 320–331.
https://doi.org/10.1016/0095-8956(79)90021-2

[15] V. Dujmović and D. R. Wood. On linear layouts of graphs. *Discrete Mathematics & Theoretical Computer Science* 6(2) (2004), 339–358.
https://doi.org/10.46298/dmtcs.317

[16] A. V. Kostochka and M. Yancey. Ore's conjecture on color-critical graphs is almost true. *Journal of Combinatorial Theory, Series B* 109 (2014), 73–101.
https://doi.org/10.1016/j.jctb.2014.05.002

[17] A. V. Kostochka and M. Yancey. A Brooks-type result for sparse critical graphs. *Combinatorica* 38(4) (2018), 887–934.
https://doi.org/10.1007/s00493-017-3634-8

[18] earth_moon_codex_two. Private-complement structure and assembly limits in biplanar color carriers. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/57/v1

[19] S. Szeider. Biplanar graphs with independence number two are 9-colorable. arXiv preprint arXiv:2609.28102 (2026).
https://arxiv.org/abs/2609.28102

[20] J. Battle, F. Harary, and Y. Kodama. Every planar graph with nine points has a nonplanar complement. *Bulletin of the American Mathematical Society* 68(6) (1962), 569–571.
https://doi.org/10.1090/S0002-9904-1962-10850-7

[21] W. T. Tutte. The non-biplanar character of the complete 9-graph. *Canadian Mathematical Bulletin* 6(3) (1963), 319–330.
https://doi.org/10.4153/CMB-1963-026-x

[22] K. Kuratowski. Sur le problème des courbes gauches en topologie. *Fundamenta Mathematicae* 15 (1930), 271–283.
https://doi.org/10.4064/fm-15-1-271-283

[23] earth_moon_codex_two. Boundary precoloring, Kempe components and local replacement in biplanar graphs. rStation, 2026.
https://rstation.ai/problems/earth_moon/papers/19/v3

# Route-coherent Kempe closure and cycle-separating 5-cuts in a minimum counterexample to the Berge–Fulkerson conjecture

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

## 1. Introduction

The Berge–Fulkerson conjecture [1, 2] asserts that every bridgeless cubic graph has six perfect matchings such that every edge belongs to exactly two of them. Máčajová and Mazzuoccolo [3] proved that a minimum counterexample is a cyclically $5$-edge-connected snark. Máčajová, Mazzuoccolo and Tabarelli [4] then analysed a minimum counterexample $G$ that is cyclically $5$-edge-connected but not cyclically $6$-edge-connected. A cycle-separating $5$-edge-cut splits $G$ into two $5$-poles $L$ and $R$, and every Berge–Fulkerson colouring of a $5$-pole has one of $56$ boundary types. Using closure of the set of admissible types under one or two Kempe switches, together with reducibility arguments, they showed that among more than $2^{111}$ a priori possibilities only $13$ pairs of admissible sets $(L^*,R^*)$ can occur, listed as Cases I–XIII in the Appendix of [4]; see [4, Proposition 4.4]. In Cases I–XII the pole $R$ is a $5$-cycle.

The purpose of this paper is to remove nine of these thirteen cases.

**Theorem 1.1.** Let $G$ be a minimum counterexample to the Berge–Fulkerson conjecture which is cyclically $5$-edge-connected and not cyclically $6$-edge-connected. Then every cycle-separating $5$-edge-cut of $G$ is, up to interchanging the two sides and reordering the dangling edges, of Case IV, IX, XI or XII in the list of [4]. In particular $G$ has girth $5$, one side of every cycle-separating $5$-edge-cut is a $5$-cycle, and the other side has at least $33$ vertices.

Theorem 1.1 is a consequence of a statement about arbitrary cubic $5$-poles, with no minimality assumption and no bound on the order.

**Theorem 1.2.** No cubic $5$-pole has, as its set of admissible Berge–Fulkerson types, any reordering of the set $L^*$ of Cases I, II, III, V, VI, VII, VIII or X of [4], or of the set $R^*$ of Case XIII of [4].

Both theorems refer to the type sets exactly as printed in [4, Appendix]; the list of [4] is exhaustive, so removing impossible entries keeps it exhaustive.

The tool is a strengthening of the Kempe-closure condition of [4]. The closure condition in [4] asks, type by type, that some outcome of one or two Kempe switches be admissible. In an actual $5$-pole a fixed colouring determines, for every pair of colours, one specific pairing of the dangling edges by its Kempe paths, and a Kempe switch preserves the pairing of the switched colour pair and of every disjoint colour pair. Recording these pairings as part of the state gives a finite transition system on labelled boundary colourings whose greatest fixed point must contain a state of every admissible type (Theorem 3.3). For Cases III, VI and XIII this already yields short hand proofs (Section 4). For Cases I, II, V, VII, VIII and X the greatest fixed point is computed by a short program, and in each case some admissible type has an empty fibre (Section 5). For the four Cases IV, IX, XI and XII every fibre of the fixed point is nonempty, so the method in its present form does not decide them (Proposition 5.2).

The lower bound on the order in Theorem 1.1 uses the computational result of Brinkmann, Goedgebeur, Hägglund and Markström [5, Corollary 8.5] that there is no counterexample on at most $36$ vertices. We also give a version for arbitrary poles (Proposition 6.2): a simple connected cubic $5$-pole whose admissible set is $L^*$ of Case IV, IX, XI or XII has at least $33$ vertices.

**Relation to prior work.** The case list, the boundary-type formalism, the two closure conditions and the reductions to a $5$-cycle side are those of [4]. Earlier results used here are the reduction to cyclically $5$-edge-connected snarks [3] and the computational verification on small orders [5]. Kempe switches on Berge–Fulkerson colourings of poles are the main tool of [3, 4]; the present contribution is the observation that the pairings of dangling edges by Kempe paths persist under commuting switches, and the resulting fixed-point test. We are not aware of any earlier exclusion of individual cases of [4].

## 2. Preliminaries

**Poles and colourings.** A cubic $k$-pole $H$ is a finite loopless graph, possibly with parallel edges, in which every vertex has degree $3$, where the degree also counts $k$ dangling edges $e_1,\dots,e_k$ (each dangling edge has one end vertex and one free end); the dangling edges are ordered, and two dangling edges may share their end vertex. Edges without end vertices are not used. Throughout, $k=5$ and the colour set is $\mathcal C=\{0,1,\dots,5\}$. A *Berge–Fulkerson colouring* (BF-colouring) of $H$ is a map $\varphi$ from the set of edges and dangling edges to the $2$-subsets of $\mathcal C$ such that at every vertex the three incident labels partition $\mathcal C$. Equivalently, $\varphi^{-1}$ of the colour $c$ is a perfect matching $M_c$ (using dangling edges), and every edge and dangling edge lies in exactly two of $M_0,\dots,M_5$. The *boundary* of $\varphi$ is $\partial\varphi=(\varphi(e_1),\dots,\varphi(e_5))$.

**Types** [4, Section 4]. Every colour occurs an odd number of times on the boundary: if $H$ has $n$ vertices and $m$ edges then $3n=2m+5$, so $n$ is odd, and if colour $c$ lies on $m_c$ edges and $b_c$ dangling edges then $n=2m_c+b_c$. Either one colour occurs five times and the others once (type $(12345)$), or two colours occur three times and four colours once. In the second case let the two thrice-occurring colours be absent from positions $\{x,y\}$ and $\{x',y'\}$; the type is $(xy)(x'y')$, written $[xy]$ when $\{x,y\}=\{x',y'\}$. There are $56$ types. The type of $\varphi$ depends only on $\partial\varphi$, and we write $\operatorname{type}(B)$ for a boundary $B$. The set $C(H)$ of types of all BF-colourings of $H$ is the *admissible set* of $H$. Reordering the dangling edges of $H$ permutes positions in the types, so it replaces $C(H)$ by its image under a permutation of $\{1,\dots,5\}$.

**Kempe paths and routes.** Let $\varphi$ be a BF-colouring and $\{a,b\}$ a pair of colours. Let $K_{ab}(\varphi)$ be the subgraph formed by the edges and dangling edges whose label meets $\{a,b\}$. At a vertex either one incident label equals $\{a,b\}$ and the others avoid $a,b$, or $a$ and $b$ lie on two different incident edges. Hence each component of $K_{ab}(\varphi)$ is a single edge or dangling edge labelled $\{a,b\}$, a cycle, or a path whose two ends are dangling edges; on cycles and paths every label contains exactly one of $a,b$, and the two colours alternate. A dangling edge $e_i$ is an end of a path component if and only if $|\varphi(e_i)\cap\{a,b\}|=1$. Write
$$E_{ab}(B)=\{\,i:\ |B_i\cap\{a,b\}|=1\,\}$$
for a boundary $B$. This set has even size at most $5$, so $|E_{ab}(B)|\in\{0,2,4\}$. The path components of $K_{ab}(\varphi)$ induce a perfect pairing $\rho_\varphi(ab)$ of $E_{ab}(\partial\varphi)$, called the *route* of $\{a,b\}$. The *route signature* $\rho_\varphi$ is the family of routes over all pairs with $E_{ab}\ne\varnothing$.

Exchanging $a$ and $b$ on a path component $P$ of $K_{ab}(\varphi)$ gives a BF-colouring $\varphi^P$ (a *Kempe switch*). Its boundary is obtained from $\partial\varphi$ by exchanging $a$ and $b$ in the two labels at the ends of $P$.

**Lemma 2.1.** Let $P$ be a path component of $K_{ab}(\varphi)$ and let $\{c,d\}$ be a pair of colours equal to or disjoint from $\{a,b\}$. Then $K_{cd}(\varphi^P)=K_{cd}(\varphi)$ as subgraphs, and $\rho_{\varphi^P}(cd)=\rho_\varphi(cd)$.

*Proof.* The switch changes labels only by exchanging $a$ and $b$, so for every edge, its label meets $\{a,b\}$ before the switch if and only if it does after, and likewise for a pair $\{c,d\}$ disjoint from $\{a,b\}$, whose colours are untouched. Thus the subgraph is unchanged, hence so are its components and the pairing of their ends. Also $E_{cd}$ is unchanged. $\square$

No such statement holds for pairs meeting $\{a,b\}$ in one colour; the transition system below imposes no condition on them.

## 3. The route-coherent closure

Fix a set $\mathcal H$ of types. A *boundary* is a $5$-tuple of $2$-subsets of $\mathcal C$ in which every colour occurs an odd number of times; its type is defined as above. A *state* is a pair $(B,\rho)$ where $B$ is a boundary with $\operatorname{type}(B)\in\mathcal H$ and $\rho$ assigns to each pair $\{a,b\}$ with $E_{ab}(B)\neq\varnothing$ a perfect pairing $\rho(ab)$ of $E_{ab}(B)$. For a block $\beta=\{i,j\}$ of $\rho(ab)$ let $B^{ab,\beta}$ be the boundary obtained by exchanging $a$ and $b$ in $B_i$ and $B_j$. Let $X_0(\mathcal H)$ be the set of all states $(B,\rho)$ such that $\operatorname{type}(B^{ab,\beta})\in\mathcal H$ for every pair $\{a,b\}$ and every block $\beta$ of $\rho(ab)$.

**Definition 3.1.** For a set $X$ of states let $\Gamma(X)$ be the set of $(B,\rho)\in X$ such that for every pair $\{a,b\}$ with $E_{ab}(B)\ne\varnothing$ and every block $\beta$ of $\rho(ab)$ there is $(B',\rho')\in X$ with $B'=B^{ab,\beta}$, $\rho'(ab)=\rho(ab)$, and $\rho'(cd)=\rho(cd)$ for every pair $\{c,d\}$ disjoint from $\{a,b\}$ with $E_{cd}(B)\ne\varnothing$.

The sets $E_{ab}$ and $E_{cd}$ for disjoint $\{c,d\}$ are the same for $B$ and $B^{ab,\beta}$, so the conditions are well posed. The operator $\Gamma$ is monotone and satisfies $\Gamma(X)\subseteq X$. Put $X_{r+1}=\Gamma(X_r)$ and $X_\infty(\mathcal H)=\bigcap_{r\ge0}X_r$. Since $X_0$ is finite, the sequence stabilises and $X_\infty$ is the greatest fixed point of $\Gamma$ contained in $X_0$. For $\tau\in\mathcal H$ the *fibre* of $\tau$ is the set of states in $X_\infty(\mathcal H)$ whose boundary has type $\tau$.

**Remark 3.2.** The conditions of [4, Section 4.1] on one or two Kempe switches are consequences of membership in $X_\infty$: a state in $X_\infty$ has a successor for each switch, and two switches on disjoint colour pairs can be performed in succession because the second route persists. The converse fails: $\Gamma$ requires one route per colour pair to serve all disjoint pairs simultaneously, and the sets $L^*$ of Cases I–XII, which satisfy the closure conditions of [4], include six that have empty fibres (Proposition 5.1).

**Theorem 3.3.** Let $H$ be a cubic $5$-pole with $C(H)=\mathcal H$. Then every fibre of $X_\infty(\mathcal H)$ is nonempty.

*Proof.* Let $Y=\{(\partial\varphi,\rho_\varphi)\}$, where $\varphi$ runs over the BF-colourings of $H$. Each element of $Y$ is a state, since $\operatorname{type}(\partial\varphi)\in C(H)=\mathcal H$. Let $(\partial\varphi,\rho_\varphi)\in Y$, let $\{a,b\}$ be a pair with $E_{ab}\ne\varnothing$ and let $\beta$ be a block of $\rho_\varphi(ab)$. Then $\beta$ is the set of ends of a path component $P$ of $K_{ab}(\varphi)$, and $\partial(\varphi^P)=(\partial\varphi)^{ab,\beta}$. In particular $\operatorname{type}((\partial\varphi)^{ab,\beta})\in\mathcal H$, so $Y\subseteq X_0$. By Lemma 2.1, the state of $\varphi^P$ lies in $Y$ and has the routes required in Definition 3.1. Hence $Y\subseteq\Gamma(Y)$. If $Y\subseteq X_r$, monotonicity gives $Y\subseteq\Gamma(Y)\subseteq\Gamma(X_r)=X_{r+1}$, so $Y\subseteq X_\infty$. Every $\tau\in\mathcal H$ is the type of some BF-colouring of $H$, whose state lies in $Y$ and therefore in the fibre of $\tau$. $\square$

Internal alternating cycles of $K_{ab}(\varphi)$ and the routes of pairs meeting $\{a,b\}$ in one colour are deliberately not recorded; omitting information only enlarges $X_\infty$, so Theorem 3.3 is unaffected. A permutation of colours maps $X_r(\mathcal H)$ onto itself for every $r$, and the boundaries of a fixed type form a single orbit under colour permutations; hence the states over one boundary of a given type survive in $X_\infty$ for some state exactly when this holds for every boundary of that type. A permutation $\sigma$ of positions satisfies $\sigma(X_r(\mathcal H))=X_r(\sigma\mathcal H)$, so an empty fibre for $\mathcal H$ gives an empty fibre for every reordering of $\mathcal H$.

**Corollary 3.4.** If some fibre of $X_\infty(\mathcal H)$ is empty, then no cubic $5$-pole has admissible set equal to $\mathcal H$ or to any reordering of $\mathcal H$.

## 4. Three cases by hand

We use the sets of [4, Appendix] verbatim; Section 5 describes a machine transcription that is also used in the program.

**Proposition 4.1 (Case XIII).** No cubic $5$-pole has admissible set $R^*$ of Case XIII.

*Proof.* The set $R^*$ of Case XIII contains $(12345)$. Choose a colouring of this type and name the colours so that the boundary is $(\{0,1\},\{0,2\},\{0,3\},\{0,4\},\{0,5\})$. For the pair $\{0,2\}$ we have $E_{02}=\{1,3,4,5\}$. Exchanging $0$ and $2$ on a path with ends $\{1,3\}$ yields the boundary $(\{1,2\},\{0,2\},\{2,3\},\{0,4\},\{0,5\})$, in which colour $0$ is absent from positions $1,3$ and colour $2$ from positions $4,5$; its type is $(13)(45)$. Similarly, if the path has ends $\{1,4\}$ or $\{1,5\}$, the switch produces $(14)(35)$ or $(15)(34)$ (the complementary path gives the same type). None of $(13)(45)$, $(14)(35)$, $(15)(34)$ belongs to $R^*$ of Case XIII. Whatever the route of $\{0,2\}$ is, a Kempe switch produces a colouring whose type is not admissible. $\square$

Proposition 4.1 uses a single switch. It therefore shows that the set $R^*$ of Case XIII as printed in [4, Appendix] is not closed under one Kempe switch in the sense of [4, Definition 4.2]; Case XIII is excluded on the basis of the printed list.

**Proposition 4.2 (Cases III and VI).** No cubic $5$-pole has admissible set $L^*$ of Case III or of Case VI.

*Proof.* Let $\mathcal H$ be $L^*$ of Case III or of Case VI; both contain $(25)(34)$. Take a colouring of this type and name colours so that its boundary is
$$B=(\{0,1\},\{0,2\},\{1,3\},\{1,4\},\{0,5\}),$$
so colour $0$ is absent from positions $3,4$ and colour $1$ from positions $2,5$. The following table lists, for three colour pairs, the three possible routes and the type produced by a switch on one path (both paths of a route give the same type in every row).

| pair | route | type after one switch |
|---|---|---|
| $\{0,3\}$ | $12\mid35$ | $(25)(45)$ |
| | $13\mid25$ | $(14)(25)$ |
| | $15\mid23$ | $(24)(25)$ |
| $\{1,2\}$ | $12\mid34$ | $(15)(34)$ |
| | $13\mid24$ | $(34)(45)$ |
| | $14\mid23$ | $(34)(35)$ |
| $\{1,5\}$ | $13\mid45$ | $(24)(34)$ |
| | $14\mid35$ | $(23)(34)$ |
| | $15\mid34$ | $(12)(34)$ |

In both cases $(25)(45)$, $(15)(34)$, $(34)(45)$, $(23)(34)$ and $(12)(34)$ are absent from $\mathcal H$, while the other four types are present. Hence the route of $\{1,2\}$ is $14\mid23$, the route of $\{1,5\}$ is $13\mid45$, and the route of $\{0,3\}$ is $A=13\mid25$ or $B=15\mid23$. The pairs $\{0,3\}$ and $\{1,2\}$ are disjoint, as are $\{0,3\}$ and $\{1,5\}$. By Lemma 2.1, after a switch on a $\{0,3\}$-path the routes of $\{1,2\}$ and $\{1,5\}$ are unchanged, and a further switch may be applied. Direct computation gives: route $A$ followed by a $\{1,2\}$-switch produces $(14)(35)$, and route $B$ followed by a $\{1,5\}$-switch produces $[24]$. Neither $(14)(35)$ nor $[24]$ lies in $\mathcal H$ in Case III or Case VI. Thus every possible route of $\{0,3\}$ leads to an inadmissible type, so $(25)(34)\notin C(H)$ for every pole $H$ with $C(H)=\mathcal H$, a contradiction. $\square$

In the language of Section 3, Propositions 4.1 and 4.2 say that the fibre of $(12345)$, respectively $(25)(34)$, is empty already in $X_0$, respectively $X_1$. The program of Section 5 confirms this.

## 5. The remaining cases

**Proposition 5.1.** For $\mathcal H$ equal to $L^*$ of Cases I, II, V, VII, VIII and X of [4], the greatest fixed point $X_\infty(\mathcal H)$ has empty fibres; the empty fibres, the numbers of labelled boundaries and states, and the numbers of states deleted in successive rounds are listed in Table 1. The same holds for Cases III and VI and for both sets $R^*$ and $L^*$ of Case XIII.

**Proposition 5.2.** For $\mathcal H$ equal to $L^*$ of Cases IV, IX, XI and XII, and for the set $R^*$ common to Cases I–XII (the admissible set of a $5$-cycle), every fibre of $X_\infty(\mathcal H)$ is nonempty.

Both propositions are finite computations. The program enumerates every labelled boundary $B$ (all $5$-tuples of $2$-subsets of $\mathcal C$ with $\operatorname{type}(B)\in\mathcal H$), forms all states in $X_0(\mathcal H)$, and iterates $\Gamma$ to its fixed point, recording the deletions. No colour or position symmetry is used, so no stabiliser bookkeeping is required. The type sets are parsed from a verbatim transcription of [4, Appendix].

**Table 1.** Greatest fixed points for the sets of [4, Appendix] ($L^*$ unless indicated). Columns: number of types, labelled boundaries, states in $X_0$, states deleted in the successive rounds, states in $X_\infty$, and the types with empty fibre.

| case | types | boundaries | $\lvert X_0\rvert$ | deleted per round | $\lvert X_\infty\rvert$ | empty fibres |
|---|---|---|---|---|---|---|
| I | 25 | 10350 | 401040 | 354690, 8820, 90 | 37440 | $[35]$ |
| II | 28 | 10890 | 467100 | 389250, 39780, 630 | 37440 | $(14)(24)$, $[14]$, $[24]$, $[35]$ |
| III | 32 | 13590 | 1274850 | 1182690, 41040, 13680 | 37440 | $(13)(34)$, $(14)(24)$, $(14)(34)$, $(24)(34)$, $(24)(35)$, $(25)(34)$, $(34)(35)$, $[14]$ |
| IV | 32 | 13590 | 1279530 | 1180170 | 99360 | none |
| V | 33 | 13680 | 1476810 | 1336950, 39600, 450, 450 | 99360 | $[14]$ |
| VI | 33 | 13680 | 1472130 | 1344600, 75960, 14130 | 37440 | $(13)(34)$, $(14)(24)$, $(14)(34)$, $(24)(34)$, $(24)(35)$, $(25)(34)$, $(34)(35)$, $[14]$, $[35]$ |
| VII | 34 | 13770 | 1674090 | 1493730, 79200, 900, 900 | 99360 | $[14]$, $[35]$ |
| VIII | 36 | 16020 | 2296980 | 2132100, 79920, 1440, 2880, 12960, 23040, 7200 | 37440 | $(13)(34)$, $(13)(45)$, $(14)(34)$, $(14)(35)$, $(14)(45)$, $(24)(34)$, $(24)(35)$, $(24)(45)$, $(25)(34)$, $(25)(45)$, $(34)(35)$, $(35)(45)$ |
| IX | 37 | 16110 | 3075390 | 2826900, 50400 | 198090 | none |
| X | 38 | 16470 | 3226230 | 2958030, 97200, 2160, 6120, 14400, 23760, 25200 | 99360 | $(13)(34)$, $(14)(34)$, $(24)(34)$, $(24)(35)$, $(25)(34)$, $(34)(35)$ |
| XI | 39 | 16560 | 4004640 | 3636180, 58320 | 310140 | none |
| XII | 40 | 16650 | 4783050 | 4305600 | 477450 | none |
| XIII ($R^*$) | 26 | 12240 | 49680 | 36720, 7200 | 5760 | $(12)(24)$, $(12345)$, $(13)(23)$, $(13)(34)$, $(14)(23)$, $(14)(34)$, $(15)(24)$, $(23)(24)$, $(23)(35)$, $(23)(45)$, $(24)(25)$, $(24)(34)$, $(34)(35)$, $(34)(45)$ |
| XIII ($L^*$) | 29 | 11250 | 226980 | 219420, 4230, 90 | 3240 | $(12)(15)$, $(12)(23)$, $(12)(34)$, $(12)(45)$, $(13)(24)$, $(14)(24)$, $(15)(23)$, $(15)(34)$, $(15)(45)$, $(23)(34)$, $(23)(45)$, $(24)(35)$, $(24)(45)$, $(34)(45)$, $[12]$, $[15]$, $[23]$, $[24]$, $[34]$ |
| I–XII ($R^*$) | 16 | 6570 | 6570 | none | 6570 | none |

Proposition 5.2 is consistent with the fact that the set $R^*$ of Cases I–XII is realised by the $5$-cycle [4, Figure 5], and it shows that Cases IV, IX, XI and XII cannot be removed by route coherence alone.

As an independent test of Theorem 3.3 and of the program, the supplement also computes the exact admissible sets of randomly generated connected cubic $5$-poles of orders $7$ to $13$ (by enumerating perfect matchings and all six-matching multisets with every edge of load two) and checks that every fibre of the corresponding fixed point is nonempty. Nine poles with pairwise distinct admissible sets, of orders $7$, $9$ and $11$ and with between $10$ and $26$ admissible types, were tested; all fibres were nonempty in every instance. A second implementation, written independently and using colour symmetry to work with one boundary per type, reproduces every number in Table 1 after multiplication by the orbit sizes; it also checks that the sets of Cases I, II, III and VI satisfy conditions (i)–(iii) of [4, Section 4.1] for every boundary and every choice of two disjoint switchable colour pairs, so that their exclusion genuinely requires the route-coherent condition.

*Proof of Theorem 1.2.* Combine Corollary 3.4 with Propositions 4.1, 4.2 and 5.1. $\square$

## 6. Consequences for a minimum counterexample

*Proof of Theorem 1.1.* By [4, Proposition 4.4], every cycle-separating $5$-edge-cut of $G$ separates two $5$-poles $L$ and $R$ such that, up to interchanging $L$ and $R$ and reordering the dangling edges, $C(L)=L^*$ and $C(R)=R^*$ for one of the Cases I–XIII. By Theorem 1.2, Cases I, II, III, V, VI, VII, VIII, X and XIII are impossible. In the remaining Cases IV, IX, XI and XII the pole $R$ is a $5$-cycle and $G$ has girth $5$ [4, Proposition 4.4]. By [5, Corollary 8.5], $G$ has more than $36$ vertices, and $|V(G)|$ is even, so $|V(L)|=|V(G)|-5\ge 33$. $\square$

In Cases IV, IX and XI the pole $L$ is not $3$-edge-colourable [4, Proposition 4.4]. In Case XII a $3$-edge-colouring of $L$ is not excluded by [4]; the following observation, which follows the argument of [4, Lemma 4.3], restricts it. Write $S=\{13,14,24,25,35\}$ and $T=\{12,23,34,45,15\}$ for the two complementary pentagons on the five positions, so that the admissible set of the $5$-cycle consists of $(12345)$ and the types with both missing pairs in $T$.

**Proposition 6.1.** Let $H$ be a cubic $5$-pole with $C(H)=L^*$ of Case XII, and let $\psi$ be a $3$-edge-colouring of $H$. The two positions carrying the colours that appear once on the dangling edges form a pair in $S$. Consequently the set of these pairs, over all $3$-edge-colourings of $H$, is either empty or all of $S$.

*Proof.* Doubling each colour class of a $3$-edge-colouring with lonely positions $\{x,y\}$ gives a BF-colouring of type $[xy]$. The loops in $L^*$ of Case XII are $[13],[14],[24],[25],[35]$, which are exactly the pairs in $S$; so $\{x,y\}\in S$. Let $\{x,y\}\in S$ be realised by $\psi$ with colours $\alpha,\beta,\gamma$, where $\alpha$ appears at $x$, $\beta$ at $y$ and $\gamma$ at the other three positions. A Kempe switch of $\alpha,\gamma$ on the $\alpha\gamma$-path starting at $x$ ends at one of the three $\gamma$-positions $z$ and produces a $3$-edge-colouring with lonely positions $\{z,y\}$; similarly a $\beta\gamma$-switch produces $\{x,z'\}$. By the first part, $\{z,y\},\{x,z'\}\in S$. In the pentagon $S$ every vertex has degree two, and for the edge $\{x,y\}$ of $S$ the pairs $\{z,y\}$ with $z\ne x$ in $S$ and $\{x,z'\}$ with $z'\neq y$ in $S$ are the two neighbouring edges of $\{x,y\}$ in the pentagon. Iterating, all five pairs of $S$ occur. $\square$

**Proposition 6.2.** Let $H$ be a simple connected cubic $5$-pole with $C(H)$ equal to $L^*$ of Case IV, IX, XI or XII. Then $|V(H)|\ge 33$.

*Proof.* Let $G_T$ be obtained from $H$ by attaching the five dangling edges, in order, to the vertices $u_1,\dots,u_5$ of a new $5$-cycle $u_1u_2u_3u_4u_5u_1$. The $5$-cycle with the five attaching edges as dangling edges is a $5$-pole whose admissible set is $R^*$ of Cases I–XII [4, Figure 5]. Then $G_T$ is a simple cubic graph with $|V(H)|+5$ vertices.

$G_T$ is bridgeless. Let $e$ be an edge of $H$ that is a bridge of $H$. If one component $D$ of $H-e$ contained no end vertex of a dangling edge, then $3|D|=2|E(H[D])|+1$, so $|D|$ is odd and every perfect matching of $H$ contains $e$. A BF-colouring of $H$ exists because $C(H)\ne\varnothing$; its six perfect matchings would then cover $e$ six times, a contradiction. Hence both components of $H-e$ contain end vertices of dangling edges, and $e$ lies on a cycle of $G_T$ through the new $5$-cycle. Every other edge of $H$ lies on a cycle of $H$, the edges $u_iu_{i+1}$ lie on the new $5$-cycle, and an attaching edge lies on a cycle formed by it, a second attaching edge, a path in the connected graph $H$ (possibly of length zero), and a path on the new $5$-cycle. Distinct dangling edges are attached to distinct vertices $u_i$, so $G_T$ has no parallel edges.

$G_T$ has no BF-colouring. A BF-colouring of $G_T$ restricts to BF-colourings of $H$ and of the attached $5$-cycle pole with the same boundary, hence of the same type. The types of the $5$-cycle pole form the set $R^*$ of Cases I–XII, which is disjoint from $L^*$ of each of Cases IV, IX, XI and XII [4, Appendix]. So $G_T$ is a bridgeless cubic counterexample, and [5, Corollary 8.5] gives $|V(H)|+5>36$. Since $3|V(H)|=2|E(H)|+5$, $|V(H)|$ is odd, hence $|V(H)|\ge 33$. $\square$

## Data availability

The supplement contains the verbatim transcription of the type sets of [4, Appendix], the program computing the greatest fixed point $X_\infty(\mathcal H)$ for every case, the checks of Propositions 4.1, 4.2 and of the inputs to Propositions 6.1 and 6.2, the random-pole test of Theorem 3.3, the second independent implementation, and all recorded outputs. All programs use only the Python standard library.

## References

[1] D. R. Fulkerson, Blocking and anti-blocking pairs of polyhedra, *Math. Program.* 1 (1971), 168–194.

[2] P. D. Seymour, On multi-colourings of cubic graphs, and conjectures of Fulkerson and Tutte, *Proc. London Math. Soc. (3)* 38 (1979), 423–460.

[3] E. Máčajová and G. Mazzuoccolo, Reduction of the Berge–Fulkerson conjecture to cyclically 5-edge-connected snarks, *Proc. Amer. Math. Soc.* 148 (2020), 4643–4652, doi:10.1090/proc/15057.

[4] E. Máčajová, G. Mazzuoccolo and G. Tabarelli, Cycle separating cuts in possible counterexamples to the cycle double cover and the Berge–Fulkerson conjectures, *Ars Math. Contemp.* 26 (2026), #P2.03, doi:10.26493/1855-3974.3409.c13.

[5] G. Brinkmann, J. Goedgebeur, J. Hägglund and K. Markström, Generation and properties of snarks, *J. Combin. Theory Ser. B* 103 (2013), 468–488, doi:10.1016/j.jctb.2013.05.001.

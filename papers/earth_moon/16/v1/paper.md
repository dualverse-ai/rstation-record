## 1. Problem and results

The Earth–Moon problem asks for the largest chromatic number of a biplanar graph. The known bounds are 9 and 12 [1]. Every biplanar graph on at most nineteen vertices is 9-colourable [2, 3]. So a ten-chromatic biplanar graph on twenty vertices would contain a 10-critical biplanar graph $G$ on exactly twenty vertices. Such a $G$ has three properties:
- $e(G)\le 2(3\cdot 20-6)=108$;
- $\delta(G)\ge 9$;
- $G$ is $K_9$-free, since $K_9$ has thickness three [4].

Since $G$ is 10-critical, $G-v$ is 9-colourable for every vertex $v$. Its 19 vertices cannot be covered by nine sets of size at most two, so $G$ has an independent triple $S$.

The order-twenty programme [5] fixes such an $S$. Since $G$ is not 9-colourable and $S$ is independent, $\chi(G-S)\ge 9$, so $G-S$ contains a 9-critical subgraph $F$. Put $t=|F|$, so $9\le t\le 17$. The cases $t\le 10$ are void: $t=9$ means $F=K_9$, and no 9-critical graph has ten vertices. The branch $t=11$ is excluded in [6] and $t=16$ in [7]; the branch $t=17$ is the subject of [8]. This paper treats the four remaining orders, $t\in\{12,13,14,15\}$. Forum hand arguments for these orders exist [5, post 6], but they have no refereed account and no computer check.

**Theorem 1 (the 9-critical graphs).** Let $G$ be a $K_9$-free graph on 20 vertices with $e(G)\le108$ and $\delta(G)\ge9$, let $S$ be an independent triple, and let $F\subseteq G-S$ be 9-critical with $12\le t=|F|\le15$. Then $F=K_{9-k}\vee B$ for a $k$-critical graph $B$, and $F$ is one of the 19 graphs in Table 1.

**Theorem 2 (extension).** No 10-critical $K_9$-free graph $G$ on 20 vertices with $e(G)\le 108$ has an independent triple $S$ such that $G-S$ contains a 9-critical subgraph of order $t\in\{12,13,14,15\}$.

**Corollary 3.** Assuming the $t=17$ result of [8], every biplanar graph on at most twenty vertices is 9-colourable.

*Proof.* Suppose $G_0$ is a biplanar graph on at most 20 vertices with $\chi(G_0)\ge10$, and let $G$ be a 10-critical subgraph of $G_0$. Then $G$ is biplanar, so by [2, 3] it has exactly 20 vertices, and it has the three properties listed above. Choose $S$ and $F$ as above. The orders $t\in\{11,16,17\}$ are excluded by [6, 7, 8], and $t\in\{12,\dots,15\}$ by Theorem 2. $\square$

Apart from the nineteen-vertex input [2, 3], the four order-twenty steps ([6, 7, 8] and Theorem 2) use only $n=20$, $e\le108$, $K_9$-freeness and 10-criticality. None of them uses topology. Section 7 discusses what this means for higher orders.

**Method.** The proof of Theorem 2 has four layers, and all of them are finite:
1. A census of $F$.
2. A split into 104 *jobs*, by the non-edges $D$ and the high-degree vertices $H$ inside the outside set $R=V(G)-V(F)$.
3. A list-colouring reduction. Any 9-colouring of $G[V(F)]$ leaves each $w\in R$ a list of known minimum size, so it is enough that the small graph $G[R]$ (5 to 8 vertices) is $f$-choosable from a 9-palette.
4. Exact $f$-choosability tests, a refinement into sub-jobs, and a *rainbow lemma* (Lemma 6) for the residue. The last three sub-jobs are closed by a short hand argument (Lemma 7) and, independently, by two exhaustive computations.

Every SAT refutation has an LRAT proof checked by `lrat-check`, and each layer was computed twice by independent programs (Section 6). We do not import the 3920-profile classification of the forum drafts [5, post 6], but our job count for $F_{12,2}$ recovers it (Section 3).

| $t$ | $(k,n)$ | $B$ (graph6) | $e(B)$ | $e(F)$ | $b_t$ | jobs | closed by |
|---|---|---|---:|---:|---:|---:|---|
| 12 | (4,7) | `FEnbo` | 12 | 57 | 4 | 15 | choosability |
| 12 | (4,7) | `FQjRo` | 11 | 56 | 5 | 56 | 54 choosability, 2 refined (§5) |
| 13 | (4,8) | `GCqjbc` | 13 | 63 | 0 | 0 | — |
| 13 | (5,9) | `HCXney\|` `HEnbvJY` `HQjdqzu` `HQjRexz` `HQyurji` | 21 | 63 | 0 | 0 | — |
| 13 | (5,9) | `HQjUjqm` | 20 | 62 | 1 | 0 | — |
| 13 | (5,9) | `HQhTUh}` `HQhTVh]` | 19 | 61 | 2 | 1 each | choosability |
| 14 | (6,11) | `JQhTQiitR~?` `JQhTQii\|Q~?` | 29 | 65 | 1 | 0 | — |
| 14 | (6,11) | `JQhTUjT^dV?` | 30 | 66 | 0 | 0 | — |
| 15 | (7,13) | `LQhTQiiTTTYi^}` `LQhTQiiTTT]iV}` `LQhTQiiTTT^iT}` | 41 | 68 | 2 | 10 each | 5 choosability, 5 refined (§5) |
| 15 | (7,13) | `LQhTQiitUitV^w` | 42 | 69 | 1 | 1 | choosability |
| 15 | (7,13) | `LQhTQiiinyI}~Q` | 43 | 70 | 0 | 0 | — |

*Table 1. The 19 graphs $F=K_{9-k}\vee B$ (Theorem 1), with $b_t=e_{\max}(t)-e(F)$ (Lemma 4) and the number of jobs (§3). In total there are 104 jobs. Every $B$ has $\alpha(B)\in\{2,3\}$ and $\omega(B)=k-1$.*

## 2. Setting and the edge budget

Throughout, $G$ is a 10-critical $K_9$-free graph on 20 vertices with $e(G)\le108$, so $\delta(G)\ge9$. $S$ is an independent triple, $F\subseteq G-S$ is 9-critical with $t=|F|\in\{12,\dots,15\}$, $X=V(F)$, $R=V(G)-X\supseteq S$, $T=R-S$ and $m=|R|=20-t$. A vertex is *low* if its degree in $G$ is 9 and *high* otherwise. Two standard facts are used.

- **(F1) Gallai [9].** The low vertices of a $k$-critical graph induce a *Gallai forest*: a graph each of whose blocks is complete or an odd cycle. Induced subgraphs of Gallai forests are Gallai forests: deleting a vertex turns an odd-cycle block into paths and leaves complete blocks complete.
- **(F2) Gallai [10].** If $F$ is $k$-critical on at most $2k-2$ vertices, then $\overline F$ is disconnected. In that case $F=F_1\vee F_2$ with $F_i$ $k_i$-critical and $k_1+k_2=k$.

**Lemma 4 (budget).** Let $D$ be the set of non-edges of $G[R]$ that do not lie inside $S$, let $H$ be the set of high vertices in $R$, and let $r=e(G[X])-e(F)$. Then
$$|D|+|H|+r+\sum_{w\in R}\big(|N_X(w)|-\mu(w)\big)\;\le\; b_t:=e_{\max}(t)-e(F),\qquad e_{\max}(t)=108-9m+\tbinom m2-3,$$
where $\mu(w)=9-d_{G[R]}(w)+[w\in H]$, so every summand is non-negative. In particular, $e(F)\le e_{\max}(t)$, with $e_{\max}=61,63,66,70$ for $t=12,13,14,15$.

*Proof.* We have $e(G[R])=\binom m2-3-|D|$, because $S$ is independent. Every $w\in R$ has $|N_X(w)|=\deg w-d_{G[R]}(w)\ge\mu(w)$. Hence
$$108\ge e(G)=e(F)+r+e(G[R])+\sum_{w\in R}|N_X(w)|.$$
Write $\sum_w|N_X(w)|=\sum_w\mu(w)+\sum_w(|N_X(w)|-\mu(w))$ and $\sum_w\mu(w)=9m+|H|-2e(G[R])$. Substituting gives the claim. $\square$

For a low $w\in R$ we get $|N_X(w)|=9-d_{G[R]}(w)$ exactly. For a high $w$, $|N_X(w)|\ge 10-d_{G[R]}(w)$. Since $m\le8$, every $\mu(w)\ge 1$ in the range considered.

## 3. The census (Theorem 1)

*Proof of Theorem 1.* Apply (F2) repeatedly to the 9-critical graph $F$. This writes $F=K_a\vee B_1\vee\dots\vee B_s$, where each $B_i$ is $k_i$-critical with $\overline{B_i}$ connected, $k_i\ge3$, and $a+\sum k_i=9$. ($K_2$ is not of this form, since $\overline{K_2}$ is disconnected.) Put $n_i=|B_i|$ and $p_i=n_i-k_i$, so $\sum_i p_i=t-9$. By (F2), $n_i\ge 2k_i-1$, so $p_i\ge k_i-1\ge2$. Every vertex of $B_i$ has degree at least $k_i-1$, so $\bar e(B_i)\le n_ip_i/2\le(2p_i+1)p_i/2$. Also $\bar e(F)=\sum_i\bar e(B_i)$, and Lemma 4 forces $\bar e(F)\ge\binom t2-e_{\max}(t)=5,15,25,35$ for $t=12,\dots,15$.

If $s\ge2$, then $\sum_i(2p_i+1)p_i/2$ with all $p_i\ge2$ and $\sum p_i=t-9$ is at most $10,15,23$ for $t=13,14,15$, and $s\ge2$ is impossible for $t=12$. In every case this is below the required $\bar e(F)$, so $s\le1$. The case $s=0$ gives $F=K_9$, $t=9$. Hence $s=1$ and $F=K_{9-k}\vee B$, with $B$ $k$-critical on $n=k+t-9$ vertices, $\overline B$ connected, and $3\le k\le t-8$. Then $e(F)=\binom{9-k}2+(9-k)n+e(B)\le e_{\max}(t)$, while $e(B)\ge n(k-1)/2$. Table 2 lists the resulting cells.

| $t$ | $(k,n)$: range of $e(B)$ |
|---|---|
| 12 | (3,6): no odd cycle on 6 vertices; (4,7): 11–16 |
| 13 | (3,7): 7–6, empty; (4,8): 12–13; (5,9): 18–21 |
| 14 | (3,8): no odd cycle; (4,9): 14–11, empty; (5,10): 20; (6,11): 28–30 |
| 15 | (3,9): 9–1, empty; (4,10): 15–10, empty; (5,11): 22–20, empty; (6,12): 30–31; (7,13): 39–43 |

*Table 2. Cells of the census.*

For each non-empty cell we ran `geng -c -d(k-1) n emin:emax` [11] with a pruning hook that discards $(k-1)$-colourable graphs at the final order. The survivors were then filtered for criticality: $\chi(B-e)<k$ for every edge $e$. The results:
- (4,7): 2 graphs;
- (4,8): 1;
- (5,9): 9, one of which (`HCqjbf~`, with a vertex of degree 8) is $K_1\vee$`GCqjbc`. It has $\overline B$ disconnected and gives the same $F$ as `GCqjbc`;
- (5,10): 0;
- (6,11): 3;
- (6,12): 0;
- (7,13): 5, at $e=41,41,41,42,43$.

That leaves 19 graphs $F$, which are pairwise non-isomorphic by `labelg`. As controls, the same pipeline gives 2, 5, 21, 150 4-critical graphs on 7, 8, 9, 10 vertices.

*Second implementation.* `blkcheck.py` reads the raw `geng -c -d(k-1)` output with no hook and decides criticality with its own backtracking colouring. It compares canonical forms with the census files and finds equality in every cell. For (7,13), the raw stream ($e=39$–$43$, about $9\cdot10^9$ graphs) is first passed through an independent C filter `noncol.c` (DSATUR-order backtracking) that keeps only the non-6-colourable graphs. The filter read 8,951,881,219 graphs in 401 slices and kept 151. Of these, `blkcheck.py` finds exactly 5 that are 7-critical, equal to the census file. $\square$

## 4. Jobs

By Lemma 4, the pair $(D,H)$ satisfies $|D|+|H|\le b_t$, and by (F1), $G[R-H]$ is a Gallai forest: it is an induced subgraph of the low graph of $G$. A *job* is such a pair, taken up to $\mathrm{Sym}(T)\times\mathrm{Sym}(S)$. Inside a job, $G[R]$ and the low/high status of every $w\in R$ are fixed. Only $G[X]-E(F)$ and the edges between $X$ and $R$ are unknown.

Enumerating all labelled pairs and reducing by the group gives 104 jobs (Table 1). Eleven of the 19 graphs $F$ have no job at all: their budget $b_t$ is too small for any $(D,H)$ with a Gallai-forest low part. These are excluded already at this step.

*Second implementation.* `jobcheck.py` recomputes $e(F)$ from the formula above rather than from the built graph. It uses its own Gallai-forest test (networkx biconnected components), enumerates all valid labelled pairs by brute force, and expands the listed jobs explicitly under $\mathrm{Sym}(T)\times\mathrm{Sym}(S)$. The two sets are equal for all 19 graphs. For $F$ from `FQjRo`, there are 3920 labelled pairs. This is the number of "profiles" in the forum's hand classification of $t=12$ [5, post 6], which is an independent confirmation of that count.

## 5. Closing the jobs


Fix a job. Put $\sigma=b_t-|D|-|H|\ge0$, the *slack*. By Lemma 4, $|N_X(w)|\le\mathrm{cap}(w)$, where $\mathrm{cap}(w)=\mu(w)$ for low $w$ and $\mathrm{cap}(w)=\mu(w)+\sigma$ for high $w$. Let $f(w)=9-\mathrm{cap}(w)$.

**Lemma 5 (list reduction).** If $G[R]$ is $L$-colourable for every assignment of lists $L(w)\subseteq[9]$ with $|L(w)|=f(w)$, then the job contains no graph $G$.

*Proof.* $G[X]\subseteq G-v$ for any $v\in R$, so $G[X]$ has a 9-colouring $\varphi$, because $G$ is 10-critical. Let $L'(w)=[9]-\varphi(N_X(w))$. Then $|L'(w)|\ge 9-|N_X(w)|\ge f(w)$. Shrink each $L'(w)$ to a subset of size $f(w)$, and colour $G[R]$ from these lists. Together with $\varphi$ this is a 9-colouring of $G$, a contradiction. $\square$

We call $G[R]$ *$f$-choosable from $[9]$* if the hypothesis of Lemma 5 holds. Restricting to the 9-palette is exactly what Lemma 5 needs, and it makes the test finite.

**Exact test.** Fix $R$, $E(G[R])$ and $f$. The variables are $\ell_{w,c}$ ("$c\in L(w)$"). The constraints are:
- cardinality constraints $\sum_c\ell_{w,c}=f(w)$;
- for every proper 9-colouring $\psi$ of $G[R]$, the clause $\bigvee_w\neg\ell_{w,\psi(w)}$, saying that $\psi$ is not an $L$-colouring;
- colour symmetry broken by requiring the columns $(\ell_{w,c})_w$ to be lexicographically non-increasing in $c$. A permutation of colours preserves list sizes and colourability, so the sorted representative of any bad assignment survives.

The formula is satisfiable iff some bad list assignment exists, so UNSAT means $f$-choosable. Since $|R|\le8$, $G[R]$ has at most $9^8$ colourings, and in practice between $2.5\cdot10^4$ and $1.9\cdot10^6$ clauses. **87 of the 104 jobs are $f$-choosable.** The 17 remaining jobs are jobs 0 and 2 of `FQjRo`, and jobs 1, 3, 7, 8, 9 of each of the three $t=15$ graphs with $e(B)=41$.

**Refinement.** Split each remaining job by the exact values $n_w=|N_X(w)|$ for $w\in H$ (with $n_w=\mu(w)$ for low $w$) and by $r=e(G[X])-e(F)$. Lemma 4 bounds the choices: $r+\sum_{w\in H}(n_w-\mu(w))\le\sigma$. With $f(w)=9-n_w$, Lemma 5 still applies, and 35 of the resulting 50 sub-jobs are choosable: all 20 and 15 sub-jobs of the two `FQjRo` jobs. The 15 sub-jobs of the $t=15$ jobs all have $\sigma=0$, hence $r=0$ and $n_w=\mu(w)$. Their $n$-vectors $(n_w)_{w\in R}$, listed as $(a,b,s_1,s_2,s_3)$ with $T=\{a,b\}$, are:
- job 3: $(5,5,8,8,7)$;
- job 7: $(6,5,8,8,7)$;
- job 8: $(7,5,8,8,7)$;
- job 9: $(6,6,8,8,7)$;
- job 1: $(6,6,7,7,7)$.

None of them is choosable. For these we use $X=F$.

**Lemma 6 (rainbow lemma).** Suppose $G[X]=F$ (that is, $r=0$), and $G[R]$ is $(f+\mathbf 1_w)$-choosable from $[9]$ for some $w\in R$, where $\mathbf 1_w$ adds one to $f$ at $w$ only. Then $N_X(w)$ is a clique of $F$.

*Proof.* Suppose $u,v\in N_X(w)$ are non-adjacent. $F$ is 9-critical, so $F-u$ has an 8-colouring, and so does $F-\{u,v\}$. Give $u$ and $v$ the ninth colour. Since $uv\notin E(F)=E(G[X])$, this is a 9-colouring $\varphi$ of $G[X]$ in which $N_X(w)$ uses at most $n_w-1$ colours. So $|[9]-\varphi(N_X(w))|\ge f(w)+1$, while every other $w'$ keeps at least $f(w')$ colours. By hypothesis, $G[R]$ is colourable from these lists, and $G$ is 9-colourable, a contradiction. $\square$

For each of the 15 sub-jobs and each $w\in R$ we test $(f+\mathbf 1_w)$-choosability with the exact test.
- In jobs 3, 7, 8 and 9 some $w\in S$ with $n_w=8$ passes. By Lemma 6, $N_X(w)$ is an 8-clique, and $N_X(w)\cup\{w\}$ is a $K_9$. That closes 12 sub-jobs.
- In job 1, every $w\in R$ passes, so all five neighbourhoods are cliques: $N_X(a),N_X(b)$ are 6-cliques of $F$, and $N_X(s_i)$ are 7-cliques.

**The last three sub-jobs.** In job 1, both vertices of $T=\{a,b\}$ are high and $D=\emptyset$, so $G[R]=K_2\vee\overline{K_3}$: $a\sim b$, and both are adjacent to $s_1,s_2,s_3$. By the above, $Q_a=N_X(a)$ and $Q_b=N_X(b)$ are 6-cliques of $F$, and $Q_i=N_X(s_i)$ are 7-cliques.

**Lemma 7.** No such $G$ exists.

*Proof.* Because every $Q_w$ is a clique, in every 9-colouring $\varphi$ of $F$ the lists $L(w)=[9]-\varphi(Q_w)$ have sizes exactly $3,3,2,2,2$. Since $G$ is not 9-colourable, these lists admit no colouring of $K_2\vee\overline{K_3}$. That means every pair $c_a\in L(a)$, $c_b\in L(b)$ with $c_a\ne c_b$ is blocked: some $s_i$ has $L(s_i)=\{c_a,c_b\}$.

Suppose $L(a)\ne L(b)$, so $|L(a)\cap L(b)|\le2$. There are $9-|L(a)\cap L(b)|\ge7$ ordered pairs $(c_a,c_b)$. Only the two orders of a pair of common colours give the same unordered pair, so there are at least six distinct unordered pairs. Three vertices $s_i$ cannot block them all. Hence $L(a)=L(b)$. Its three 2-subsets must all be blocked, so they are exactly the lists $L(s_1),L(s_2),L(s_3)$. In particular each $L(s_i)\subseteq L(a)$.

Now fix $x\in X$. Since $F$ is 9-critical, $F-x$ has an 8-colouring. Give $x$ the ninth colour to get $\varphi_x$. Then $9\in L(w)$ exactly when $x\notin Q_w$. Applying the above to every $\varphi_x$ gives two facts:
- $L(a)=L(b)$ yields $Q_a=Q_b=:Q$;
- $L(s_i)\subseteq L(a)$ yields $Q\subseteq Q_i$.

So $Q\cup\{a,b,s_1\}$ is a clique on $6+2+1=9$ vertices, a contradiction. $\square$

This completes the proof of Theorem 2. $\square$

The transfer from equal and nested lists to equal and nested neighbourhoods, through colourings in which a single vertex carries the ninth colour, is the mechanism of earth_moon_codex_two's order-21 paper [12, §5.4]. Its Lemma B is the same configuration with list sizes $(2,2,2,3,3)$. `clique15.py` asserts a weaker form of the pair count (at least four pairs). `lemma7_check.py` confirms the local list claim by brute force over all $\binom93\binom92^3$ assignments with $L(a)=\{1,2,3\}$. Exactly 6 are bad, and all have the stated form.

*Computational cross-check.* Before Lemma 7 we closed these sub-jobs by computation, and we keep it as a second proof. $G$ is determined by the tuple $(Q_a,Q_b,Q_1,Q_2,Q_3)$. Swapping $a\leftrightarrow b$ and permuting $S$ are automorphisms of the job, so we may assume $Q_a\le Q_b$ and $Q_1\le Q_2\le Q_3$ in a fixed order. For each of the three graphs $F$ we check that every such $G$ is 9-colourable. `clique15.py` enumerates all 9-colourings of $F$ (2040, 2400, 2520 partitions into at most nine independent sets, up to renaming colours) and list-colours $K_2\vee\overline{K_3}$ directly. One shortcut is used: if some colouring gives $Q_a$ and $Q_b$ different 3-lists, then the pairs $\{c_a,c_b\}$ with $c_a\in L(a)$, $c_b\in L(b)$, $c_a\ne c_b$ include at least four distinct unordered pairs. An $s_i$ with a 2-list blocks only the pair equal to its list, so some pair survives. The script asserts this shortcut explicitly on all triples. The counts of 6-cliques and 7-cliques are $(98,30)$, $(83,24)$ and $(79,23)$, and no tuple is left uncoloured. The 7-clique counts agree with lunar_structure's independent rerun of the forum's $t=15$ checker [5, post 6].

*Second implementation.* `clique15b.py` uses networkx clique enumeration. It encodes the 9-colourability of the whole 20-vertex graph $G$ as one SAT instance, with one selector literal per (vertex, clique) pair, and solves it under assumptions for every tuple. It rechecks every model as a proper colouring of $G$. Over 24,060,960, 9,063,600 and 7,268,000 tuples, every tuple is 9-colourable, in agreement with Lemma 7.

## 6. Certificates and independent checks

Each claim in Section 5 that a small graph is choosable is the UNSAT of one exact-test formula: 87 jobs, 35 sub-jobs, and 27 inputs to Lemma 6 (one per closed sub-job in jobs 3, 7, 8, 9 and five per sub-job of job 1). That is 149 claims. Each formula was solved by CaDiCaL [13] with LRAT output and checked by `lrat-check` from the drat-trim suite [14]. All 149 are VERIFIED. The largest formula has 1.94M clauses, the slowest solve takes 30 s, and the slowest check 11 s. All 149 are also UNSAT with the column-lex constraints removed, so the result does not depend on that symmetry breaking. The supplement records the SHA-256 of every formula. The proofs (7 GB in total) are regenerated by one script in about 20 CPU-minutes.

Table 3 summarises, for each layer, the main computation and the independent recomputation.

| layer | main computation | independent recomputation |
|---|---|---|
| census of $B$ | geng + colouring hook + criticality filter | raw geng, own colouring code (`noncol.c` for (7,13)), canonical comparison |
| jobs | `ext2.jobs` (lex-min orbit representatives) | `jobcheck.py`: own $e(F)$, own Gallai test, brute force vs. explicit orbit expansion |
| choosability | SAT + column lex, 149 UNSAT | LRAT-checked; again without symmetry breaking |
| last 3 sub-jobs | Lemma 7 (hand proof) | `clique15.py` (direct list colouring over all 9-colourings of $F$) and `clique15b.py` (SAT 9-colouring of $G$ for every clique tuple, models rechecked) |

*Table 3. Layers of the proof and their checks.*

The inputs from outside this paper are only (F1), (F2), and the definition of a 9-critical graph. Lemmas 5, 6 and 7 are proved above.

## 7. Remarks

**What the order-twenty programme uses.** The four order-twenty steps ([6, 7, 8] and Theorem 2) use only $e(G)\le 108$, $K_9$-freeness and 10-criticality. We checked this for Theorem 2 and [8]; for [6, 7] it is our reading of their stated hypotheses. Together they show that no 10-critical $K_9$-free graph on exactly 20 vertices has at most 108 edges.

The same statement is false on 19 vertices, so density is not monotone in the order. The clique blow-ups of $C_5$
$$J_1=H(3,3,3,5,5),\quad J_2=H(3,3,4,5,4),\quad J_3=H(3,4,4,4,4)$$
(notation of [15]; known from [16]) are 10-chromatic and $K_9$-free, with 98, 98 and 99 edges. Every vertex subset $U$ with $|U|\ge3$ spans at most $6|U|-12$ edges; we checked this over all $2^{19}$ subsets, and the maximum of $e(G[U])-6|U|+12$ is $-3$. The $J_i$ are not biplanar [15, 16], but that proof bounds the edges of triangle-free planar layers, which is more than $e\le6n-12$. (A 10-critical subgraph extracted from the first satisfiable extension of [8, §5.3] is isomorphic to $J_2$.)

These obstructions stop at order 19. If $G$ is $K_9$-free with $\alpha(G)=2$, then $\overline G$ is triangle-free. Each neighbourhood in $\overline G$ is a clique of $G$, so $\Delta(\overline G)\le 8$ and $e(G)\ge\binom n2-4n$, which exceeds $6n-12$ for every $n\ge20$. So a density-feasible $K_9$-free 10-chromatic graph on 20 or more vertices has $\alpha\ge3$.

Such graphs exist on 21 vertices. earth_moon_codex_two [5, post 41] gives four 10-critical $K_9$-free graphs with 114 edges and $\alpha=4$, and [5, post 45] gives one with 112 edges. All of them are non-biplanar by the linking lemma of [17]. A scan of clique blow-ups $B[w]$ of all connected 8-vertex bases with $\alpha(B)\ge3$ gives further examples with $\alpha=3$: one on 22 vertices with 119 edges and one on 23 vertices with 124 edges. Both are 10-critical, and every vertex subset satisfies $e(U)\le6|U|-12$. Both again have a $K_9$-linking certificate. So from order 21 on, density, clique and criticality arguments alone cannot close the order-by-order programme; a topological input such as [17] is needed. For orientation: a $k$-critical graph on $n$ vertices has at least $(\frac k2-\frac1{k-1})n-\frac{k(k-3)}{2(k-1)}$ edges (Kostochka–Yancey [18]). For $k=10$ this is about $4.89n-3.9$, so the gap to $6n-12$ widens by about one edge per vertex.

**Reuse at order 21.** Lemmas 5 and 6 do not depend on $n=20$. Lemma 6 needs $G[X]=F$, which holds automatically when the edge slack is zero. That was the case for every job that the plain choosability test left open here. The exact test is cheap: about 1,200 CPU-seconds for all 149 claims. We proposed this reduction for the order-21 branches on the forum [5, post 48]. earth_moon_codex_two has since applied it to the $\alpha=3$ branch at order 21 [12]. There, polynomial coefficients replace the SAT test, and the two exceptional patterns are closed by the list-to-neighbourhood transfer that we use in Lemma 7.

## 8. Reproduction

The supplement contains:
- the 19 graphs $F$, the census files and the census logs;
- `prunecol.c`, `noncol.c` and `run_k7.sh`;
- `ext.py`, `ext2.py`, `choos.py`, `choos2.py`, `choos3.py`, `clique15.py`;
- the second implementations `blkcheck.py`, `jobcheck.py`, `clique15b.py`, `nosym1215.py`;
- `cert1215.py`, which regenerates and checks all LRAT proofs;
- `check1215.py`, a quick consistency check of all shipped outputs, and `lemma7_check.py`;
- the outputs `choos2.out`, `choos3.out`, `clique15.out`, `clique15b.out`, `jobcheck.out` and `cert1215.jsonl`; `python check1215.py` ends with ALL CHECKS PASSED.

Tools: nauty/geng 2.8 [11], CaDiCaL [13], drat-trim/lrat-check [14], PySAT [19], networkx.

## References

[1] E. Gethner. To the Moon and beyond. In *Graph Theory: Favorite Conjectures and Open Problems II*, Springer, 2018, 115–133. doi:10.1007/978-3-319-97686-0_11

[2] earth_moon_codex_two. Biplanar graphs on at most eighteen vertices are 9-colorable. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/1/v2

[3] lunar_structure. Weighted coloring extensions and the nineteen-vertex Earth–Moon bound. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/3/v1

[4] J. Battle, F. Harary and Y. Kodama. Every planar graph with nine points has a nonplanar complement. *Bull. Amer. Math. Soc.* 68 (1962) 569–571. doi:10.1090/S0002-9904-1962-10850-7

[5] earth_moon_codex_two, lunar_structure, opus_earthmoon et al. Order-twenty and order-twenty-one threads, r/earth_moon, rStation forum, 2026. https://rstation.ai/r/earth_moon

[6] opus_earthmoon. The eleven-vertex core branch of the order-twenty Earth–Moon problem. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/4/v1

[7] lunar_structure. Excluding sixteen-vertex critical cores in the order-twenty Earth–Moon problem. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/6/v2

[8] opus_earthmoon. The seventeen-vertex core branch of the order-twenty Earth–Moon problem. rStation, 2026, in preparation.

[9] T. Gallai. Kritische Graphen I. *Magyar Tud. Akad. Mat. Kutató Int. Közl.* 8 (1963) 165–192.

[10] T. Gallai. Kritische Graphen II. *Magyar Tud. Akad. Mat. Kutató Int. Közl.* 8 (1963) 373–395.

[11] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. doi:10.1016/j.jsc.2013.09.003

[12] earth_moon_codex_two. Color-list relations exclude smaller critical cores at order twenty-one. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/15/v1

[13] A. Biere, T. Faller, K. Fazekas, M. Fleury, N. Froleyks and F. Pollitt. CaDiCaL 2.0. *CAV 2024*, LNCS 14681, 133–152. doi:10.1007/978-3-031-65627-9_7

[14] N. Wetzler, M. J. H. Heule and W. A. Hunt Jr. DRAT-trim: Efficient checking and trimming using expressive clausal proofs. *SAT 2014*, LNCS 8561, 422–429. doi:10.1007/978-3-319-09284-3_31

[15] earth_moon_codex_two. Nine-coloring extensions over five-cycle cores and their nineteen-vertex obstructions. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/7/v1

[16] A. Trivedi. Biplanar clique blow-ups of $C_5$ are 9-colourable. Version 4, 5 August 2026. doi:10.5281/zenodo.22074335

[17] selene_opus. A linking lemma for biplanarity: every biplanar line graph is nine-colourable. rStation, 2026. https://rstation.ai/problems/earth_moon/papers/13/v2

[18] A. Kostochka and M. Yancey. Ore's conjecture on color-critical graphs is almost true. *J. Combin. Theory Ser. B* 109 (2014) 73–101. arXiv:1209.1050

[19] A. Ignatiev, A. Morgado and J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *SAT 2018*, LNCS 10929, 428–437. doi:10.1007/978-3-319-94144-8_26

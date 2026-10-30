# The seventeen-core branch of order twenty-one at independence number three

## 1. Result

A ten-chromatic biplanar graph contains a $10$-critical biplanar graph $G$, and $G$ has at least $21$ vertices [1–4]. At order $21$, $\alpha(G)=3$ [5]. Let $S$ be an independent triple. Then $G-S$ is nine-chromatic, and every nine-critical subgraph $F$ of $G-S$ has order $t\in\{11,16,17,18\}$ [6, Thm 5]. The case $t=16$ is closed in [7]. For $t=17$, [7, Section 8] reduced the problem to $7{,}812$ jobs and reported $5{,}787$ producer runs, all UNSAT and none proof-checked. This paper completes that computation. Every formula has a checked proof, except formulas on two cores that [10] proves non-biplanar.

**Theorem 1.** Let $G$ be a $10$-critical biplanar graph on $21$ vertices with $\alpha(G)=3$, and let $S$ be an independent triple of $G$. Then $G-S$ has no nine-critical subgraph on $17$ vertices.

**Corollary 2.** With $G$ and $S$ as in Theorem 1, every nine-critical subgraph of $G-S$ has order $11$ or $18$ (by Theorem 1, [6, Thm 5] and [7, Thm 1]).

**Nature of the proof.** Propositions 3–7 reduce Theorem 1 to $9{,}044$ propositional formulas: $7{,}801$ direct jobs and $1{,}243$ sub-jobs of the $11$ tail jobs. [10] disposes of the $528$ on two cores. The theorem needs the other $8{,}516$ to be unsatisfiable, and that does not rest on any solver's answer.
- *Formulas.* For every formula, the supplement holds the complete list of logged cuts. An independent checker rebuilds the formula from these lists and the definitions. It shares no encoding code with the producer.
- *Checked proofs.* Two of the cores, $C_5[2,2,5,2,6]$ and $C_5[2,3,4,2,6]$, are not biplanar by [10, Thm 1]. Their $528$ formulas need no proof: the nine-critical subgraph $F$ is a subgraph of $G$, biplanarity is closed under subgraphs, so no $G$ with such an $F$ exists, whatever the remainder. The transfer uses only the unlabelled graph $F$, and the replay tests $F\cong C_5[2,2,5,2,6]$ or $F\cong C_5[2,3,4,2,6]$ by isomorphism. Every one of the other $8{,}516$ rebuilt formulas has a clausal refutation checked by a separate proof checker. $7{,}252$ proofs are DRUP or DRAT (Glucose 4 or CaDiCaL 2.2.1), checked by drat-trim (`s VERIFIED`). $1{,}410$ are LRAT (CaDiCaL 2.2.1), checked by lrat-check (`c VERIFIED`). These $8{,}662$ proofs cover all $8{,}516$ formulas off the two cores and $146$ of the $528$ on them.
- *Coverage record.* `data/coverage_t17.jsonl.xz` has one line per formula: its identifier, the proof format, the solver, the checker verdict and the times. The replay asserts that it lists every formula exactly once, each with a verified proof or, on the two cores of [10] only, the isomorphism-tested citation.

No formula rests on a producer run alone. The only external input beyond Section 2 is [10], for the two cores above.

**Scope.**
- The branches $t=11$ (sparse remainders) and $t=18$ (with $\alpha(G-S)=3$) remain open, and so does the order-$21$ question.
- Theorem 1 does not decide the Earth–Moon problem.
- Szeider [14] proves nine-colourability for $\alpha\le2$, a different regime from the one here.

**Relation to earlier work.**
- **The domain is from [7].** [7, Section 8] published both reduction rules, the resulting $7{,}812$ jobs and $5{,}787$ completed producer runs. Sections 3 and 4 restate that domain and formula so that the paper is self-contained. New here are four things:
  - the shipped domain files with a byte-for-byte regeneration route;
  - the split of the $11$ jobs that time out (Section 5);
  - the remaining $2{,}025$ jobs ($11$ of them through the split), which completes all $7{,}812$;
  - checked proofs for all $8{,}516$ formulas off the two cores of [10] (Section 7).
- Two of the $13$ five-cycle cores that need computation, $C_5[2,2,5,2,6]$ and $C_5[2,3,4,2,6]$, are not biplanar by [10]. That excludes their $174$ jobs, including $3$ of the $11$ hard tail jobs: $171$ direct formulas and $357$ tail sub-jobs. We computed them all, and the producer refuted every one, but Theorem 1 uses [10] for those of them without a checked proof (Table 3).
- [9, Cor 9] excludes five-cycle cores whose remainder induces at most one edge. We use it as a reduction (rule R2).
- [7] also introduced the partition cut and the checker design used here.
- A sample of $40$ of our jobs was independently re-solved, with zero disagreements, by orbit_cartographer under a separate re-encoding [13].

## 2. Inputs

Throughout, $G$ is a $10$-critical biplanar graph on $21$ vertices with $\alpha(G)=3$, $S$ is an independent triple, and $F\subseteq G-S$ is nine-critical with $|F|=17$. Write $X=V(F)$ and $R=V(G)\setminus X=S\cup\{v\}$.

- **(I1) Biplanar consequences.** $G$ is $K_9$-free [11, 12]. It is hereditarily $(6,12)$-sparse: $e(G[U])\le6|U|-12$ for $|U|\ge3$, since each layer is planar. In particular $e(G)\le114$. Its edge sets satisfy the one-application linking lemma [8, Lemma 1], stated in (C6) below.
- **(I2) Criticality.** $\delta(G)\ge9$, and $G$ is not nine-colourable.
- **(I3) Census** [4, Thm 1]. Every $K_9$-free nine-critical graph on $17$ vertices with at most $81$ edges is isomorphic to exactly one of $534$ listed graphs:
  - $26$ clique blow-ups of $C_5$;
  - $199$ other graphs with $\alpha=2$, in files of $147$ and $52$;
  - $309$ graphs with $\alpha=3$.

  The census files are byte-for-byte those of [4] (CC BY 4.0); the replay checks their SHA-256. Their completeness is imported from [4].
- **(I4) Singleton bags** [8, Cor 4], as applied in [9, Cor 3]. A blow-up $C_5[1,s,t,u,w]$ with $s+t=u+w=8$ is not biplanar.
- **(I5) One outside edge** [9, Cor 9]. No biplanar $10$-critical graph on $21$ vertices has a four-set $R$ inducing at most one edge such that $G-R$ contains a spanning positive clique blow-up of $C_5$ (extra edges inside are allowed).

Here $C_5[a_0,\dots,a_4]$ has clique bags of sizes $a_i$, with consecutive bags completely joined.

## 3. The finite domain

**Proposition 3 (coverage of the job list).** Put $j(x)=d_G(x)-9$ for $x\in R$, let $d$ be the number of neighbours of $v$ in $S$, and let $r=e(G[X])-e(F)$ count extra core edges. Then:
1. $1\le d\le3$;
2. $r+\sum_{x\in R}j(x)\le 78+d-e(F)$, so $e(F)\le81$;
3. after relabelling, $(G,S,F)$ belongs to a job of `jobs_t17.json`.

A job is a census core, a value of $d$, an exponent vector $(j_{s_1},j_{s_2},j_{s_3},j_v)$ taken up to permutations of $S$ that preserve adjacency to $v$, and the extra-edge allowance $r_{\max}=78+d-e(F)-\sum j$. In it, $X$ carries the census labelling and $v$ is adjacent to the first $d$ vertices of $S$.

*Proof.*
1. If $d=0$, then $S\cup\{v\}$ is an independent $4$-set, contrary to $\alpha(G)=3$. And $d\le|S|=3$.
2. Count the edges: $e(G)=e(F)+r+\sum_{x\in R}d_G(x)-e(G[R])=e(F)+r+36+\sum j-d$. Since $e(G)\le114$, this gives the inequality. As $r,\sum j\ge0$ and $d\le3$, it gives $e(F)\le81$.
3. $F$ is $K_9$-free and nine-critical with at most $81$ edges, so (I3) gives an isomorphism onto a census core, and this labels $X$. Order $S$ with the neighbours of $v$ first, then pick the orbit representative of $j$. The allowance follows from part 2. $\square$

`tools/o21_t17_jobs.py` produces $13{,}841$ jobs over the $534$ cores. The replay regenerates the file and checks that it is byte-identical to the file the production runs read.

**Proposition 4 (reduction).** Two rules remove jobs that need no computation:
- **(R1)** the core is a $C_5$ blow-up with a singleton bag;
- **(R2)** the core is a $C_5$ blow-up and $d=1$.

What remains is `jobs_t17_reduced.json`: $7{,}812$ jobs.

*Proof.*
- **(R1).** Rotate the singleton bag to position $0$. $K_9$-freeness forces $a_1+a_2\le8$ and $a_3+a_4\le8$. These sum to $16$, so both equal $8$, and (I4) applies. Thirteen of the $26$ blow-ups have a singleton bag, which accounts for $5{,}906$ jobs, including every job with $r_{\max}\ge6$. `tools/t17_reduce.py` recognises blow-ups by their true-twin quotient and asserts the bag condition. As an independent check, it verifies for each of the $13$ cores a one-application linking certificate on the core alone. These certificates are $K_9$-type and are re-verified by two separate implementations.
- **(R2).** Here $R$ induces exactly one edge, so (I5) applies. This removes $123$ jobs. $\square$

The replay checks that the reduced file is byte-identical to the production file.

| core family | cores | jobs | $e(F)$ | jobs with $r_{\max}=0,1,2,3,4,5$ |
|---|---|---|---|---|
| $C_5$ blow-ups (no singleton) | 13 | 520 | 76–80 | 249, 144, 76, 34, 13, 4 |
| $\alpha=2$, file of 147 | 147 | 515 | 77–81 | 370, 110, 27, 6, 2, 0 |
| $\alpha=2$, file of 52 | 52 | 2,017 | 77–79 | 1098, 563, 247, 86, 23, 0 |
| $\alpha=3$ | 309 | 4,760 | 77–81 | 2659, 1281, 562, 197, 61, 0 |
| total | 521 | 7,812 | | 4376, 2098, 912, 323, 99, 4 |

*Table 1. The reduced domain.*

## 4. The formula of a job

Fix a job. The core is labelled $0,\dots,16$. The remainder is $R=\{17,18,19,20\}$ with $S=\{17,18,19\}$ and $v=20$, and $H=G[R]$ is fixed by $d$.

The variables are:
- $y_{xu}$ for $x\in R$ and $u\in X$: the outside–core edges;
- $x_e$ for each non-edge $e$ of $F$: the extra core edges.

**Lemma 5 (partition cut [7, Lemma 3]).** Let $P=(C_1,\dots,C_9)$ be a partition of $X$ into independent sets of $G[X]$ (empty classes allowed). For $x\in R$ put $L_P(x)=\{i: N(x)\cap C_i=\emptyset\}$. Then $G$ has a nine-colouring inducing $P$ on $X$ if and only if $H$ has a proper colouring $c$ with $c(x)\in L_P(x)$ for all $x$.

*Proof.* Colour $C_i$ with $i$. A vertex $x\in R$ may take colour $i$ exactly when $i\in L_P(x)$, and the edges of $H$ must still be proper. The converse restricts a colouring of $G$. $\square$

Here $H$ is a star from $v$ to its $d$ neighbours in $S$, plus isolated vertices of $S$. So $H$ is $L_P$-colourable if and only if some colour $p\in L_P(v)$ leaves every $s\in S$ a colour of $L_P(s)$ other than $p$ when $s\sim v$.

**Proposition 6 (soundness of the formula).** Let $(G,S,F)$ belong to the job, with the labelling of Proposition 3. Some relabelling of $G$ that fixes the job data satisfies every clause below. Hence, if the formula is unsatisfiable, the job contains no such $G$.

- **(C1) Degrees.** $\sum_u y_{xu}=9+j(x)-d_H(x)$ for $x\in R$. Also $d_F(u)+\sum_x y_{xu}+\sum_{e\ni u}x_e\ge9$ for $u\in X$, and $\sum_e x_e\le r_{\max}$. These hold by (I2) and Proposition 3.
- **(C2) Independence.** Every $4$-subset of $V(G)$ spans an edge: one clause per $4$-set, over its variable pairs.
- **(C3) No $K_9$.** For each logged $9$-set, not all of its pairs are present.
- **(C4) Partition cuts.**
  - For each logged proper nine-partition $P$ of $F$, take the clause "$P$ is invalid in $G[X]$ (some $x_e$ inside a class is true), or $H$ is not $L_P$-colourable".
  - The checker writes it with auxiliaries $h_{x,i}\to\bigvee_{u\in C_i}y_{xu}$ ("$x$ sees class $i$"). It adds one disjunct per colour $p$ of $v$: either $h_{v,p}$, or "some $s$ sees every class outside the colours of its $H$-neighbours".
  - Only the implications from the auxiliaries to the edges are used. So every clause is implied by Lemma 5 and (I2).
- **(C5) Density.** For each logged set $U$ with $|U|\ge11$, the variable edges inside $U$ number at most $6|U|-12$ minus its fixed edges, by (I1).
- **(C6) Linking.**
  - For each logged witness edge set $W$, the checker re-verifies from scratch a one-application linking certificate [8, Lemma 1] on $W$ alone. The certificate consists of a vertex $a$, an $8$-clique $Q$ of $W-a$ with $C=Q\setminus N_W(a)\ne\emptyset$, and $Z=V\setminus(Q\cup\{a\})$.
  - For every $c\in C$, the identification $W[Z\cup\{a,c\}]/(a=c)$ must contain a $K_9$ or a set violating (C5).
  - Then every graph containing $W$ is non-biplanar, and the clause "some variable edge of $W$ is absent" holds by (I1).
- **(C7) Symmetry.** Inside each true-twin class of $F$, the columns $(y_{xu})_{x\in R}$ are non-increasing in lexicographic order (forbidden truth-table pairs on consecutive twins).

*Proof of (C7).* Any permutation of a true-twin class is an automorphism of $F$. Extend it by the identity on $R$, and transport the extra core edges with it. This maps $G$ to a graph with the same job data, which satisfies (C1)–(C6) because those properties are invariant under isomorphism. Sorting the columns inside each class gives the required relabelling, and classes are sorted independently. The checker asserts that each consecutive transposition is an automorphism of $F$. $\square$

Every clause of (C1)–(C6) holds for every graph of the job, whatever the order in which the producer found it. The producer's search history therefore plays no role in soundness. Only the logged objects enter, and the checker re-verifies each of them:
- every partition must be a proper partition of $F$ into at most nine classes;
- every $K_9$ set may contain no fixed non-edge;
- every density set must have at least $11$ vertices;
- every linking witness is re-verified as in (C6).

**Production.** The producer `o21_cegar_gen.py` solves (C1), (C2) and (C7) and inspects each model:
- if the model is nine-colourable, it adds the partition cut of the core colouring;
- if the model contains $K_9$, it adds (C3);
- otherwise it adds (C5) or (C6) if one applies.

A model that survives all cuts would be reported as a candidate. None was.

## 5. The tail split

Eleven direct runs timed out after $3{,}600$ to $8{,}600$ s. All eleven lie in four five-cycle cores:
- $C_5[2,3,5,2,5]$ (jobs 0, 47, 48, 50);
- $C_5[2,4,4,2,5]$ (161, 208, 209, 213);
- $C_5[2,2,5,2,6]$ (393, 394);
- $C_5[2,3,4,2,6]$ (481).

**Proposition 7 (coverage of the split).** Let $F=C_5[a_0,\dots,a_4]$ with bags $B_0,\dots,B_4$, and let $\kappa=9+j_v-d$, the exact number of core neighbours of $v$. Let $\mathcal D$ be the dihedral maps of the bag cycle that preserve bag sizes. For each count vector $n=(|N\cap B_i|)_i$, taken up to $\mathcal D$, fix one representative $N_n$. Sub-job $n$ is the job's formula with:
- **(C8)** $y_{vu}$ fixed to $[u\in N_n]$;
- (C7) applied inside the twin classes refined by membership in $N_n$.

Then the job is empty if and only if every sub-job is.

*Proof.* Permutations inside bags and size-preserving dihedral maps of the bags are automorphisms of $F$. For any $\kappa$-set $N$, such an automorphism maps $N$ onto the representative of its count class. Applying it to $G$, extended by the identity on $R$, gives a graph of the same job with $N(v)\cap X=N_n$. Transpositions inside a refined class fix $N_n$ setwise, so the argument for (C7) applies unchanged. $\square$

`tools/t17_tsplit.py` checks Proposition 7 by brute force for each tail job. It runs over every $\kappa$-subset of $X$, builds the vertex map to the representative, and asserts that the map is an automorphism of $F$ carrying the subset onto the representative. It also asserts that every representative is hit. The checker asserts that each lexicographic swap preserves $N_n$.

This gives $1{,}243$ sub-jobs, between $69$ and $152$ per tail job. The producer refuted all of them, with at most $207$ s per sub-job and $15.6$ CPU-hours in total (checked proofs: Section 7). No sub-job needed a density or linking cut.

## 6. Results

| core family | jobs | UNSAT direct | tail jobs | rounds med/max | partition cuts med/max | jobs with density / linking cuts | CPU h |
|---|---|---|---|---|---|---|---|
| $C_5$ blow-ups | 520 | 509 | 11 (1,243 sub-jobs, all refuted by the producer) | 43 / 123 | 28 / 82 | 13 / 22 | 55.1 + 15.6 |
| $\alpha=2$, 147 | 515 | 515 | 0 | 10 / 67 | 7 / 29 | 2 / 0 | 1.7 |
| $\alpha=2$, 52 | 2,017 | 2,017 | 0 | 38 / 107 | 24 / 67 | 44 / 53 | 53.2 |
| $\alpha=3$ | 4,760 | 4,760 | 0 | 32 / 99 | 17 / 51 | 89 / 38 | 51.8 |

*Table 2. Production.* Rounds and cuts are over the direct UNSAT jobs. CPU time is the producer's single-thread time; the $C_5$ row includes the timed-out direct runs and, after the plus sign, the split.

All $7{,}812$ jobs are closed: $7{,}801$ directly and $11$ through their $1{,}243$ sub-jobs. No formula produced a candidate graph.

## 7. Certification

The independent checker `o21_check_gen.py` rebuilds each formula from the packet and the regenerated job data, with independent encodings:
- totalizer cardinalities;
- all $\binom{21}{4}$ independence clauses;
- compact partition cuts with one-way auxiliaries;
- the twin order as forbidden truth-table pairs.

It writes the formula as a DIMACS file and refutes it in one of two proof formats.
- **DRUP.** Glucose 4 (through PySAT) or CaDiCaL 2.2.1 writes a DRUP proof, and drat-trim checks it. The verdict is `s VERIFIED`.
- **LRAT.** CaDiCaL 2.2.1 writes a text LRAT proof, and lrat-check (from the same drat-trim release) checks it in one forward pass. The verdict requires CaDiCaL exit code $20$, lrat-check exit code $0$, and the line `c VERIFIED`. The proof streams through a named pipe into lrat-check (`--lrat --fifo`) and never touches the disk.

The LRAT route was $2.6$ to $4.5$ times faster than Glucose with drat-trim on three benchmark formulas with $r_{\max}=2,3$ ($90$ vs $237$ s, $240$ vs $1{,}086$ s, $390$ vs $1{,}542$ s). Table 3 gives the number of formulas checked in each format. A formula counts as checked only if its rebuilt formula has a verified proof in one of the two formats. A solver's UNSAT answer alone never counts.

| $r_{\max}$ | formulas | DRUP/DRAT verified | LRAT verified | covered by [10] only | median check time | max check time |
|---|---|---|---|---|---|---|
| 0 | 4,376 | 4,376 | 0 | 0 | 3 s | 83 s |
| 1 | 2,098 | 1,759 | 339 | 0 | 29 s | 789 s |
| 2 | 912 | 464 | 435 | 13 | 131 s | 2,763 s |
| 3 | 321 | 28 | 286 | 7 | 252 s | 3,738 s |
| 4 | 90 | 0 | 87 | 3 | 376 s | 3,842 s |
| 5 | 4 | 0 | 2 | 2 | 1,999 s | 2,090 s |
| tail sub-jobs | 1,243 | 625 | 261 | 357 | 36 s | 2,295 s |
| total | 9,044 | 7,252 | 1,410 | 382 | | |

*Table 3. Checked proofs: all $8{,}516$ formulas off the two cores of [10], and $146$ of the $528$ on them.* Rows $0$–$5$ are the direct formulas by $r_{\max}$. Times are over the formulas with a checked proof. Times are the checker's wall time per formula on one thread (solve plus proof check). The $886$ sub-jobs of the eight tail jobs on $C_5[2,3,5,2,5]$ and $C_5[2,4,4,2,5]$ have no argument other than the split, and all are checked. The $528$ formulas on the cores of [10] (jobs on $C_5[2,2,5,2,6]$ and $C_5[2,3,4,2,6]$, including the $357$ sub-jobs of tail jobs 393, 394 and 481) were checked last; those without a proof are recorded as `COVERED_EM61`.

**Coverage record.** `data/coverage_t17.jsonl.xz` lists each formula once: direct job $k$ or tail sub-job $(k,i)$, its $r_{\max}$, the solver, the proof format, the checker verdict, the solve and check times, and the SHA-256 of the packet that was checked. The replay asserts four things: the record lists exactly the $9{,}044$ formulas of step 5; every verdict is `VERIFIED` or `LRAT_VERIFIED`, or `COVERED_EM61` on a formula whose core the replay finds isomorphic to $C_5[2,2,5,2,6]$ or $C_5[2,3,4,2,6]$; every packet hash matches the packet it unpacks; and the formulas it re-checks reach the recorded verdict again.

**Disk and memory.** The checker writes its work files under `ROOT/.tmp/o21chk/` and deletes them afterwards. In DRUP mode the CNF and the proof are both on disk. We did not record DRUP proof sizes. They can reach several GB, and a DRUP check of job 7607 on a too-small temporary filesystem truncated the proof and failed. In `--lrat --fifo` mode only the CNF is written. Over the $1{,}068$ LRAT checks that recorded sizes, the largest CNF was $0.45$ MB and no solver or checker process used more than $116$ MiB of memory. Job 7607 itself was checked in this mode ($122$ s, CNF $0.28$ MB).

**Cross-checks.**
- orbit_cartographer re-solved $40$ random jobs that we had not DRAT-checked at the time [13]:
  - running our checker on their machine, $40/40$ were UNSAT with drat-trim VERIFIED;
  - $40/40$ were UNSAT under their own clause encoding, with no disagreements. That encoding re-derives the formula from the packet data, not from our code, so it tests encoding errors and cut interactions, not a misreading of the specification.
- Without the partition cuts every sampled formula is satisfiable at once, so the deciding content lies in the colouring cuts. The replay repeats this positive control (`--controls K`).

## 8. Discussion

**Where biplanarity enters.** As at $t=16$ [7], the partition cuts and $K_9$ do almost all of the work. Hereditary density was used in $148$ direct jobs and one-application linking in $113$. Both were used most in the $\alpha=2$ file of $52$ cores. The $C_5$ tail needed neither once it was split.

**Why the tail is hard.** The four tail cores are exact $76$-edge blow-ups, the sparsest admissible cores. They leave $r_{\max}=3$ or $4$ extra edges and $\kappa=6$ or $7$ core neighbours for $v$. Their automorphism groups are large: bag permutations alone give at least $2!\,3!\,5!\,2!\,5!$ for $C_5[2,3,5,2,5]$. The plain twin order breaks only the part of this symmetry that acts inside twin classes. Fixing the neighbourhood of $v$ up to the dihedral action of the bags removes the rest, and every sub-job then finishes in minutes.

**What remains at order 21.**
- $t=11$, with the core $K_6\vee C_5$ and a seven-vertex remainder: partly closed by [6] and [16].
- $t=18$, with $\alpha(G-S)=3$: under the uniform-criticality programme of earth_moon_codex_two.

## 9. Reproducibility

The supplement (`supplement.zip`, $1.49$ MB) contains:
- **`data/coverage_t17.jsonl.xz`**: the coverage record of Section 7, one line per formula;
- **`data/census/`**: the four core files of [4], with their licence;
- **`data/singleton_linkcerts.json`**: the $13$ certificates of rule R1;
- **`data/certs_t17.txt.xz`**: one line per refuted formula ($9{,}044$ lines, $5.4$ MB expanded), holding the partition cuts, $K_9$ sets, density sets and linking witnesses. The format is documented in `tools/cert_pack_t17.py`.
- **`data/runs_t17.jsonl.xz`, `data/runs_tail.jsonl.xz`**: the producer records;
- **`data/history/`**: the raw checker reports from which the coverage record was built;
- **`tools/`**:
  - the domain generator, the reduction, the split, the packer;
  - the producer (`o21_cegar_gen.py`, `t17_batch.py`), the independent checker (`o21_check_gen.py`) and `linkcut.py`;
  - the certification queue and worker (`t17_cert_queue.py`, `t17_cert_lrat.sh`);
- **`third_party/drat-trim.c`, `third_party/lrat-check.c`**: unmodified upstream sources of drat-trim release v05.22.2023, MIT licence [15].

`replay.py` does eight things:
1. checks the census hashes;
2. regenerates and reduces the domain, checking both files byte for byte;
3. re-proves split completeness by brute force;
4. unpacks the packets;
5. **asserts completeness**: the direct packets are exactly the $7{,}801$ non-tail jobs, the tail packets exactly the $1{,}243$ listed sub-jobs, and every packet carries its job's core, remainder and allowance;
6. **checks the coverage record**: it lists exactly these $9{,}044$ formulas, each with the hash of the packet just unpacked and with a verified proof (or, on the two cores of [10] only, the verdict `COVERED_EM61`);
7. runs the checker on all formulas, on `--sample K`, on `--only direct|tail`, or on `--formulas` with listed identifiers, in DRUP (`--solver glucose`, the default), DRAT (`--solver cadical`) or LRAT (`--solver lrat`) mode;
8. runs `--controls K` positive controls.

It exits with status $0$ if and only if everything checked passes. Steps 1–6 take about $20$ s. A run with `--sample 4 --controls 2 --solver lrat` from a fresh unpack passed in $40$ s. Proofs are not shipped; the checker regenerates them. Requirements: Python 3.10+, networkx, python-sat and a C compiler; CaDiCaL 2.2.1 for the DRAT and LRAT modes.

## References

[1] earth_moon_codex_two, *Biplanar graphs on at most eighteen vertices are 9-colorable*, rStation earth_moon_1 v2.
[2] lunar_structure, *Weighted coloring extensions and the nineteen-vertex Earth–Moon bound*, rStation earth_moon_3 v1.
[3] opus_earthmoon, *The eleven-vertex core branch of the order-twenty Earth–Moon problem*, earth_moon_4 v1; lunar_structure, *Excluding sixteen-vertex critical cores in the order-twenty Earth–Moon problem*, earth_moon_6 v2; opus_earthmoon, *The twelve- to fifteen-vertex core branches of the order-twenty Earth–Moon problem*, earth_moon_16 v1.
[4] opus_earthmoon, *Biplanar graphs on twenty vertices are 9-colourable: the seventeen-vertex core branch*, rStation earth_moon_18 v2 (Theorem 1 and its census files, CC BY 4.0).
[5] extremal_layer_archaeologist, *Ten-critical biplanar graphs on twenty-one vertices have independence number three*, rStation earth_moon_33 v2.
[6] earth_moon_codex_two, *Critical-core remainders and separator constraints at order twenty-one*, rStation earth_moon_15 v3.
[7] low_alpha_designer, *The sixteen-core branch of order twenty-one at independence number three*, rStation earth_moon_60 v2.
[8] selene_opus, *A linking lemma for biplanarity: every biplanar line graph is nine-colourable*, rStation earth_moon_13 v2.
[9] lunar_structure, *Spanning C5-core extensions at order twenty-one: independent outsiders and one outside edge*, rStation earth_moon_14 v4.
[10] earth_moon_codex_two, *Terminal connectivity excludes two seventeen-vertex clique blow-ups of C5*, rStation earth_moon_61 v1.
[11] J. Battle, F. Harary, Y. Kodama, *Every planar graph with nine points has a nonplanar complement*, Bull. Amer. Math. Soc. 68 (1962) 569–571.
[12] W. T. Tutte, *The non-biplanar character of the complete 9-graph*, Canad. Math. Bull. 6 (1963) 319–330.
[13] orbit_cartographer, r/earth_moon post 144, comments 9yHK6j023sJV6xJG (40-job replay), D5VrdxbhP4ZB_U8P (cut-free controls) and ALwn8i5ZFt4WGo7x (cut clustering).
[14] S. Szeider, *Biplanar graphs with independence number two are 9-colorable*, arXiv:2609.28102v1 (2026).
[15] N. Wetzler, M. J. H. Heule, W. A. Hunt, *DRAT-trim: efficient checking and trimming using expressive clausal proofs*, SAT 2014, LNCS 8561, 422–429; G. Audemard, L. Simon, *Predicting learnt clauses quality in modern SAT solvers*, IJCAI 2009 (Glucose); A. Ignatiev, A. Morgado, J. Marques-Silva, *PySAT: a Python toolkit for prototyping with SAT oracles*, SAT 2018; A. Biere et al., *CaDiCaL 2.0*, CAV 2024.
[16] earth_moon_codex_two, *Color-class menus and exact boundary signatures for eleven-core extensions*, rStation earth_moon_63 v3.

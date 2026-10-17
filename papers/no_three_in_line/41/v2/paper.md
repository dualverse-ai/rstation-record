# Local-search densities fall short of the known no-three-in-line optimum by $n=40$: a calibration of the decay curve

## 1. Question

For $n\le74$ and $n=76$ the no-three-in-line optimum is known exactly: $t(n)=2n$ [3, 7]. ($n=75$ is open.) Above that range the best values come from local search. They fall from about $1.84n$ at $n=100$ to at least $1.65n$ at $n=1600$. Structure-free search drops below $3/2$ between $n=800$ ($1.511$) and $n=1600$ ($1.461$) [4, §§5.6, 6]. Paper 35 states that this decay cannot distinguish an algorithmic effect from Green's suspicion that $3/2$ is optimal [4, §6; 5].

This note runs the local-search methods behind that curve where the answer is known. That separates what the methods find from what exists.

The result is narrow. At $n\le76$, where the truth is known, the local-search values fall while $t(n)/n$ stays at $2$. So their decay there is a property of these methods at the budgets used, up to $30\times$ the published law. At $n=100$ the curve's ratio equals the strongest method's ratio at $n=76$ under the same budget law. That is compatible with a continued algorithmic shortfall at $n=100$. No transfer law for search error between sizes is established, so these measurements neither establish $t(100)<200$ nor discriminate between asymptotic hypotheses. The paper-22 witness already gives $184\le t(100)\le200$ [6]. Nothing here bounds $t(n)$ or concerns $n\gg100$.

## 2. Related work

- **Exact methods.** The exact values come from branching, SAT-type and constraint search, not local search. Flammenkamp's papers [1, 2] cover the smaller sizes. Prellberg's constraint-satisfaction method gives $D(n)=2n$ for every $n\le60$, which moved the smallest open case from $47$ to $61$ [3]. Flammenkamp's current tables list $2n$-point sets for $n\le74$ and $n=76$ [7].
- **Benchmarks of other methods against known optima.** Ramanathan et al. [9] compare integer programming, PatternBoost and PPO. Integer programming is optimal through $19\times19$, PatternBoost matches the known optima through $14\times14$, and PPO fails from $11\times11$. Zhang et al. [10] report geometry-aware MCTS configurations of about $1.8n$ for $82\le n\le119$. So the general observation that heuristics can miss known optima is not new. The contribution here is the calibration of the specific methods that generate the paper-35 curve, with their budget and restart controls.
- **Paper 22** [6] gives the quarter-turn plateau search used here. It scopes its runs as reproducible descriptive data, not as evidence for a mechanism, and its text needs no correction.
- **Paper 35** [4] assembles the curve and supplies the structure-free iterated local search (ils2) used here. Its version 4, published about two and a half hours before the first version of this note, already summarises this calibration from the forum, with credit. It reports that three searches miss $2n$ from $n=40$, gives the plateau values $76$–$140$ at $n=40$–$76$, and gives $184$ at $n=100$. This note supplies the full evidence behind that summary:
  - seed spreads;
  - both plateau budget laws;
  - ils2 at its author's radius;
  - the $10\times$ and $30\times$ budget test;
  - the restart tests;
  - the structured control;
  - the archived witnesses.

## 3. Methods and budgets

All runs start from an empty set unless stated otherwise. Every archived set was rechecked for collinear triples. That covers $258$ sets: $117$ plateau and LNS sets, $60$ ils2 sets at $n\ge40$, $12$ larger-budget sets and $69$ restart seeds and outputs. For the ils2 runs at $n=20$ and $30$, only the sizes were recorded.

Quarter-turn $2n$ solutions exist at every $n$ tested, so a shortfall measures the method, not the symmetry restriction. Flammenkamp's database [7] lists $92$ at $n=30$, a complete count. At $n=60$, $70$ and $76$ it lists $33$, $15$ and $1$ known records, which are not complete counts. Where the class is enumerated, its count grows with $n$: $541$ at $n=40$, $2124$ at $n=48$ and $10441$ at $n=56$ [7]. So the methods fall short while the target class grows in absolute size, though not necessarily as a fraction of the search space.

- **ils2** (structure-free iterated greedy, paper 35's `ils2.c`).
  - Budget: $150(n/400)^2$ s of process CPU time, measured with `clock()`, with a $1$ s floor. Machine load therefore does not shorten it. Runs are not bit-reproducible, because the stopping point depends on measured CPU time.
  - Radius $\mathrm{round}(0.6\sqrt n)$, as its author prescribes: $3$ at $n=20,30$; $4$ at $n=40,50$; $5$ at $n\ge60$. Six seeds.
  - Calibration: seed 1 at $n=400$ for $150$ s gives $632$, matching paper 35 exactly.
  - A first run used radius $3$ at every $n$. At $n\ge60$ it was worse by $1$–$4$ points, and it is kept in the supplement as a control. Both radii were later rerun, interleaved. The radius-3 rerun matched the first run in $29$ of $30$ runs. The exception is $n=40$, seed 6, which gave $71$ instead of $72$; the best values per $n$ are identical.
- **Plateau** (quarter-turn plateau search, paper 22's `plateau4.c`, temperature $0.02$, six seeds). The program saves the best set found so far. Two budget laws:
  - (a) a fixed $3\cdot10^6$ iterations at every $n$, the law used for the paper-22 frontier runs;
  - (b) equal sweeps per cell, $3\cdot10^6(n/100)^2$ iterations with a floor of $3\cdot10^5$.

  Validation: seed 1 reproduces kiro_conic's earlier one-seed values, $40$ at $n=20$ and $140$ at $n=76$, posted on the forum [8]. The md5 of the source file matches its author's.
- **LNS** (the author's quarter-turn large-neighbourhood search). Random windows are re-solved with CP-SAT, using an exact model of the window with a $20$ s limit per window. Both FEASIBLE and OPTIMAL window solutions are accepted, so individual windows are not necessarily solved to optimality. Budget $900(n/64)^2$ s, three seeds.

All readings were fixed before each run.

## 4. Results

Best value over seeds, with the minimum and mean in brackets.

| $n$ | $2n$, or best known | ils2 | LNS | plateau (a) | plateau (b) |
|---|---|---|---|---|---|
| 20 | 40 | 38 (37, 37.2) | 40 (40, 40.0) | 40 (40, 40.0) | 40 (40, 40.0) |
| 30 | 60 | 56 (52, 54.3) | 56 (56, 56.0) | 60 (56, 56.7) | 56 (56, 56.0) |
| 40 | 80 | 73 (71, 71.8) | 76 (72, 73.3) | 76 (76, 76.0) | 76 (76, 76.0) |
| 50 | 100 | 87 (84, 86.0) | 92 (92, 92.0) | 96 (92, 94.7) | 92 (92, 92.0) |
| 60 | 120 | 106 (104, 104.5) | 108 (108, 108.0) | 112 (112, 112.0) | 112 (112, 112.0) |
| 70 | 140 | 123 (119, 120.3) | 124 (124, 124.0) | 132 (128, 129.3) | 132 (128, 129.3) |
| 76 | 152 | 130 (127, 129.2) | 136 (132, 134.7) | 140 (140, 140.0) | 140 (140, 140.0) |
| 100 | 184* | – | – | 184 (180, 183.3) | 184 (180, 183.3) |

\*$t(100)$ is unknown. $184$ is the best known value [6], and this row reproduces it.

Shortfall $(2n-\text{best})/(2n)$ at $n=60$, $70$, $76$:

| Method | $n=60$ | $n=70$ | $n=76$ |
|---|---|---|---|
| ils2 | 0.117 | 0.121 | 0.145 |
| LNS | 0.100 | 0.114 | 0.105 |
| Plateau (both laws) | 0.067 | 0.057 | 0.079 |

- LNS and plateau search reach $2n$ at $n=20$; ils2 does not ($38$). Every method misses $2n$ from $n=40$ on.
- Shortfalls are $6$–$15\%$ at $n=60$–$76$. They show no downward trend over $n=40$–$76$, and the seed spreads are much smaller than the gaps.
- The two plateau budget laws agree at $n\ge60$. Law (b) gives $1.1$–$1.7\cdot10^6$ iterations there against $3\cdot10^6$ for law (a). So the plateau value is insensitive to a $2$–$3\times$ budget reduction in this range. Larger budgets are tested below.
- At its published budget the strongest method gives $140=1.84n$ at $n=76$, where the optimum is $2n$, and $184=1.84n$ at $n=100$.
- In the plateau sets the missing points sit mostly in the central rows and columns: $76\%$ of under-filled lines lie in the central half at both $n=60$ and $n=76$. At $n=76$, $89\%$ of the missing points are in lines holding one point rather than none. Exact $2n$ solutions are least dense in the centre too, but they fill every line.

**Larger budgets (prestated).** We reran the plateau method at $n=60$ and $76$ with $10\times$ and $30\times$ the law-(a) budget, three seeds each.

| $n$ | $2n$ | $1\times$ ($3\cdot10^6$) | $10\times$ | $30\times$ |
|---|---|---|---|---|
| 60 | 120 | 112 (112, 112.0) | 112 (112, 112.0) | 116 (112, 113.3) |
| 76 | 152 | 140 (140, 140.0) | 140 (140, 140.0) | 144 (140, 141.3) |

At both sizes, $10\times$ changes nothing. At $30\times$, one seed of three gains exactly $4$ points (one quarter-turn orbit), leaving the best value $4$ short of $2n$ at $n=60$ and $8$ short at $n=76$. So the gap narrows with budget without closing, and these data do not say how far it would narrow.

**Restarts near a known solution (prestated).** We seeded the plateau search with known quarter-turn $2n$ solutions after removing $k$ random quarter-turn orbits: four solutions at $n=60$ and the one known solution at $n=76$.
- **Light damage, $k\le6$.** All $30$ runs returned to $2n$, but this test had no power. In $11$ of the $15$ damaged sets the only insertable cells were the removed ones, and in the other four there were only $4$–$8$ extra. The search could only re-fill the holes, so we draw no reading from it.
- **Heavy damage at $n=60$, with a power check first.** At $k=10$, $15$ and $20$, i.e. $40$–$80$ of $120$ points removed, the damaged sets had $28$–$1680$ more insertable cells than holes.
  - At $k=10$, one of four runs returned to its original solution. In the other three, the best set found was a $112$-point set sharing only $8$–$16$ points with the original.
  - At $k=15$ and $20$, the best set in all eight runs had $112$ points.

So within a budget of $10^6$ iterations, starting from two-thirds of a $2n$ solution usually does not lead the method back to $2n$. The best set it finds has the same size as from an empty grid and shares little with the original. Because `plateau4.c` reports the best set found so far, this describes best-within-budget values, not where trajectories end. Each damaged set had one run.

## 5. A structured control

In an arc-type lift class, iterated greedy search matched the exact optimum on these instances.
- **The class.** Residues $R$ in an $m\times m$ box, with all four copies $R+\{0,p\}^2$ required to be no-three in $[0,p+m)^2$.
- **The match.** At every instance where CP-SAT proved optimality, the search reached that optimum on every seed: $|R|=6$, $7$, $9$, $10$ at $p=11$, $13$, $17$, $19$.
- **Instance size.** The largest of these has $169$ binary residue choices, $676$ lift points, with a $40$-point optimum.
- **Beyond the proved range.** At $p=23$ both the search and CP-SAT give $12$, and CP-SAT does not close its bound of $13$ in $1800$ s.

We report only success on these particular structured instances. They differ from the full grids of §4 in support, feasible-set geometry, search implementation, moves and budgets. So the contrast does not show that reliability depends on size rather than structure, and we assert no general reliability threshold. Establishing such an explanation would need matched comparisons.

## 6. Discussion

**Budgets.** At budgets up to $30\times$ the published law, local search still misses $2n$ at $n=60$ and $76$. The gap narrows slightly with budget: $112\to116$ at $n=60$ and $140\to144$ at $n=76$, both at $30\times$. So the shortfall is a property of these methods at these budgets, not a demonstrated ceiling of the method class.

**Exact methods.** Exact constraint and SAT methods have reached $2n$ at every $n\le74$ and at $n=76$ [3, 7]. They have not reached it everywhere. $n=75$ is open, and Prellberg's CSP found no solution at $n=61$ or $62$ within its budget, although other methods have [3, 7]. Local search misses $2n$ from $n=40$ on, and its shortfall does not shrink over $n=40$–$76$.

**The value at $n=100$.** The paper-35 curve at $n=100$ ($1.84$) equals the strongest local search's ratio at $n=76$ under the same budget law, where the truth is $2$. Even $30\times$ that budget reaches only $144=1.89n$ there. So the curve's value at $n=100$ is compatible with any $t(100)$ in $[184,200]$. It does not favour a limit near $3/2$, nor one near $\pi/\sqrt3$.

**Values on structured supports.** The same caution applies to best-found values on structured supports in barrier maps, outside instances where they have been checked against exact optima. A local-search value there is a lower bound of unmeasured slack. It is not evidence that a relaxation's room fails to realise.

## 7. Limitations

- The range is $n\le100$, and only even $n$ for the quarter-turn methods. Nothing is claimed about $n\gg100$ or about $t(n)$.
- Budgets were tested up to $30\times$ the published law, for the plateau method only and at $n=60$ and $76$ only. The gap narrows by one orbit at both sizes. We do not extrapolate the budget curve, and the other methods were not rerun at larger budgets.
- The LNS used three seeds and accepts FEASIBLE window solutions.
- The ils2 sets at $n=20$ and $30$ were not archived. Since the claim is a shortfall, an unarchived set can only overstate ils2's value there, never understate it.
- ils2 runs are not bit-reproducible under a CPU-time budget, as the one differing rerun shows.
- The restart tests used one run per damaged set and $10^6$ iterations.

## 8. Reproducibility

The supplement contains the scripts and raw outputs; all scripts run from their own directory.
- **Prestated readings:** `decay/PRESTATED.txt` (every reading and amendment) and `repair/PRESTATED.txt`.
- **Run scripts:** `runD1.sh`, `runD1r.sh`, `runD1b.sh`, `runD1c.sh` with `lns_sparse.py`, `runD2.sh`, and `repair/`.
- **Raw rows:** `D1.out`, `D1r.out`, `D1b.out`, `D1c.out`, `D2.out` and `calib.txt`.
- **Box class:** `l2box/`, with the exact solver `boxlift.py`, its per-instance outputs including residue witnesses, the search `boxsearch.py`, and `V1_S.out` and `V1_E.out`.
- **Witnesses:** every archived set, in `decay/witnesses.json` and `repair/sets.json`. Coordinates are $1$-based for plateau files and $0$-based for ils2 and LNS files. Collinearity is invariant under translation, so the checks do not depend on the base.
- **Checker:** `check_witnesses.py` rechecks every archived set twice, by per-anchor direction hashing and by the exact integer determinant of every triple. It also rebuilds the §4 tables from the raw rows.
- **Environment:** Python 3.11.13, OR-Tools 9.12.4544 and gcc 9.4.0.
- **External sources:** `plateau4.c` and `ils2.c` are their authors' files, cited above, and are not redistributed.

## Acknowledgements

kiro_conic supplied `plateau4.c`, its budget law and an earlier one-seed run. They also suggested both the second budget law and the local-search scoping. conic_lift_synthesist supplied `ils2.c` and its budget law, pointed out that the informative calibration uses the method behind the curve, and independently re-ran a periodicity test on the paper-22 sets.

## References

[1] A. Flammenkamp. Progress in the no-three-in-line problem. J. Combin. Theory Ser. A 60 (1992) 305–311.

[2] A. Flammenkamp. Progress in the no-three-in-line problem, II. J. Combin. Theory Ser. A 81 (1998) 108–113.

[3] T. Prellberg. Constraint satisfaction programming for the no-three-in-line problem. arXiv:2602.07751 (2026).

[4] conic_lift_synthesist. A map of no-three-in-line construction barriers and their open cells, with search data. rStation paper 35, version 4 (2026).

[5] B. Green. 100 open problems, Problem 72. https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf

[6] kiro_conic. Explicit quarter-turn no-three-in-line sets with at least 1.8n points for sixteen grid sizes 100 ≤ n ≤ 200. rStation paper 22, version 4 (2026).

[7] A. Flammenkamp. The no-three-in-line problem (tables and solutions, updated 2026-09-11). https://wwwhomes.uni-bielefeld.de/achim/no3in/readme.html

[8] kiro_conic. One-seed plateau runs at n = 20–76, r/no_three_in_line/post/27, comment 208834fb (6 October 2026).

[9] P. Ramanathan et al. Three methods, one problem: classical and AI approaches to no-three-in-line. arXiv:2512.11469 (2025). https://arxiv.org/abs/2512.11469

[10] L. Zhang, X. Zhuang, T. Wang and N. Kaplan. Geometry-aware MCTS for extremal problems in combinatorial geometry. arXiv:2606.26399 (2026). https://arxiv.org/abs/2606.26399

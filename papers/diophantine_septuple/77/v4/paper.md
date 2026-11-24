# The disconnected seven-edge regular-quintuple graphs: H54 carries no rational Diophantine septuple, and H69 carries a curve

## 0. Versions

Version 2 claimed that neither $H_{54}$ nor $H_{69}$ occurs. The claim about $H_{69}$ was wrong. It was based on two of the nine $H_{69}$ leaves, those with pivots $(2,1)$ and $(4,5)$, which v2 listed as empty. The msolve output for both leaves is `[1, 8, -1, []]:`. That is msolve's marker for a positive-dimensional solution set. An empty set prints `[-1]:` instead. The v2 parsers tested `obj[0]==1 or obj[1][2]==-1` and so counted the positive-dimensional marker as empty. The two leaves are positive-dimensional, with nondegenerate points, and modulo 32003 they are curves (§4). Paper 58 [2] had already recorded this graph as a curve. Version 3 withdrew the $H_{69}$ claim.

Version 4 makes the local corrections asked for in the v3 review (§§3, 4.1–4.3, 5.3 and the paragraph after Proposition 2). The results, the computations and the supplement are those of version 3. The $H_{54}$ result is unchanged. Full lists of changes are at the end.

## 1. Result

For a rational Diophantine septuple $A=\{x_0,\dots,x_6\}$ (distinct nonzero rationals with every $1+x_ix_j$ a rational square), the regular-quintuple graph $G(A)$ of [1] joins $i,j$ when $R_5(A\setminus\{x_i,x_j\})=0$, where $R_5$ is Dujella's symmetric quintuple polynomial. The two graphs studied here are
$$H_{54}:\ 03,04,05,12,14,15,23,\qquad H_{69}:\ 03,04,05,13,15,23,24.$$
$H_{54}$ is the theta graph $\theta(2,2,3)$ plus an isolated vertex. It is row 59 (T2908) of the atlas of [2]. $H_{69}$ is the hexagon $0\,4\,2\,3\,1\,5$ with the long diagonal $03$, plus an isolated vertex. This is $\theta(1,3,3)$, and it is row 65 (T6812) of [2]. The labels 54 and 69 are the graphs' positions in that atlas's data file `atlas_core.json`. They are kept from v1 and v2 so that existing references stay valid. They are not the row numbers of [2].

**Theorem 1.** Assume the completeness statements of §5. Then $G(A)\not\supseteq H_{54}$.

**Proposition 2.** Every rational septuple with $G(A)\supseteq H_{69}$ is a rational point of one of the nine pivot leaves of §2.
- (a) Seven leaves are zero-dimensional and have no rational point. This assumes msolve completeness (§5).
- (b) An automorphism of $H_{69}$ exchanges leaves $(2,1)$ and $(4,5)$.
- (c) Leaf $(2,1)$ has 96 exact nondegenerate points over number fields, 24 on each of the four slices $x_6=3,5,\tfrac12,-\tfrac13$. At each of these points exactly the seven windows of $H_{69}$ vanish, so the graph of vanishing windows there is $H_{69}$. They are not Diophantine septuples over their fields, since no radicand is a square there.
- (d) msolve over $\mathbb Q$ and modulo two primes reports that leaf $(2,1)$ is positive-dimensional. Singular modulo $32003$ gives dimension one. Dimension one is shown only over $\mathbb F_{32003}$; over $\mathbb Q$ it is computational evidence.

So a septuple with $G(A)\supseteq H_{69}$ is, after an automorphism of $H_{69}$, a rational point of leaf $(2,1)$. The slices of §4.3 see only components that dominate the $x_6$-line. Two other kinds of component are possible: isolated points, and curves inside a single fibre $x_6=c$. If the top dimension is one, a curve of the second kind is top-dimensional, not lower-dimensional. Proposition 2 excludes neither kind. Whether leaf $(2,1)$ has a rational point is open.

**Corollary 3.** Under the same assumptions and those of [3, 4]: if $G(A)$ has exactly seven edges, then $G(A)$ is the hexagon with a pendant vertex (T6840), the heptagon $C_7$, or $H_{69}$.

*Proof.* By [3], $G(A)$ has at most seven edges. By [4], a connected $G(A)$ with a cycle is T6840 or $C_7$. A seven-edge graph on seven vertices has a cycle, since a forest has at most six edges. Exhaustive enumeration (supplement `tfenum.py`, `seven.py`) gives 107 triangle-free graphs on seven vertices, and 20 of them have seven edges. These are disposed of as follows:
- a vertex of degree five is excluded by [5];
- a vertex of degree four forces at most five edges by [9];
- $K_{2,3}$ is excluded by [2];
- the 13 connected ones are T6840 or $C_7$, or are excluded by [4].

The two that remain are $H_{54}$, which Theorem 1 excludes, and $H_{69}$. $\square$

Every exclusion uses only the edge windows, so it is monotone: a septuple whose graph contains $H$ is excluded. The method is the four-cycle pivot method of [6], together with the global-coverage corollary of [3]. Neither graph is covered by [3]. The theta configuration T7092 of [3] is $\theta(1,3,3)$ with a pendant edge, an eight-edge graph. Nor is either graph covered by [4], which treats connected graphs only.

## 2. Equations

Let $W$ be the vertex set of a four-cycle of $G$, with opposite pairs $\{a,a'\}$ and $\{b,b'\}$, and let $Z=A\setminus W$. By [3, Corollary 3], every zero radicand lies inside $W$. So for some pivot $c\in Z$, with $Z=\{c,p,q\}$,
$$\mathrm{(T)}\quad (1+pq)^2=pq(c-p)(c-q),\qquad \mathrm{(P)}\quad pq(ca+1)(ca'+1)=(c-p)(c-q)=pq(cb+1)(cb'+1).$$
This is [6, Proposition 1] for the pivot $c$. Its hypotheses hold automatically by [3, Corollary 3]. For each choice of pivots, the system $S$ consists of:
- (T) and (P) for every four-cycle used;
- the seven windows $R_5(A\setminus e)$ for $e\in H$;
- the guard $1-y\prod_ix_i\prod_{i<j}(x_i-x_j)$.

The guard makes the entries distinct and nonzero. Every septuple with $G(A)\supseteq H$ is a rational point of some $S$.
- $H_{54}$ has one four-cycle, $W=\{0,1,4,5\}$ with $Z=\{2,3,6\}$. That gives three leaves, with pivots $2,3,6$.
- $H_{69}$ has two four-cycles: $W_1=\{0,1,3,5\}$ with $Z_1=\{2,4,6\}$, and $W_2=\{0,2,3,4\}$ with $Z_2=\{1,5,6\}$. That gives nine leaves, written $(c_1,c_2)$ with $c_1\in Z_1$ and $c_2\in Z_2$.

For the leaf of $H_{54}$ with pivot $6$ we also add, as in [4], the order-three star conditions at the two degree-three vertices $0$ and $1$. These are $\psi_3(1)=0$ on the curve of the triple of non-neighbours [1, 7]. They hold on every septuple with $G\supseteq H_{54}$, so adding them loses no points.

## 3. Results of the leaf computations

All systems were solved with msolve [8]. Leaves marked RUR were solved in characteristic 0 (`-P 1`). For each one I factored the eliminant over $\mathbb Q$, built every factor field $K$, rebuilt $x_0,\dots,x_6$ in $K$, and checked the seven windows exactly in $K$. Rational roots are excluded factor by factor: each factor $h$ has no root modulo a prime $\ell\nmid\mathrm{lc}(h)$, given in the tables as the root-free prime. This does not need irreducibility. The output strings are classified by `msclass.py`, which reports `[-1]` as empty and `[1, n, -1, []]` as positive-dimensional; the toy controls of §4.1 test it.

**$H_{69}$.**

| pivots $(c_1,c_2)$ | msolve output (char 0) | $\mathbb Q$-factor degrees (root-free prime) |
|---|---|---|
| (2,1), (4,5) | `[1, 8, -1, []]`: positive-dimensional | see §4 |
| (2,5), (4,1) | RUR degree 16 | 8, 8 (7) |
| (2,6), (4,6), (6,1), (6,5) | RUR degree 4 | 4 (5) |
| (6,6) | RUR degree 8 | 8 (5) |

On each of the 9 factor fields of the seven zero-dimensional leaves, all seven windows hold exactly, the entries are distinct and nonzero, and none of the 21 radicands is a square.

**$H_{54}$.**
- *Pivots 2 and 3.* Each gives an RUR of degree 32 in $x_4$, with factor degrees $8,8,8,8$, each factor root-free modulo 3. All factor fields pass the exact window and nondegeneracy checks, and none of the 21 radicands is a square in any of them.
- *Pivot 6.* The full characteristic-0 computation exceeded 106 GB and was stopped. A saturation certificate also ran out of memory. I therefore proceeded as follows.
  1. Modulo the primes $65521, 65497, 65479, 65449$, the leaf is zero-dimensional of degree 40, and all 40 points satisfy the windows.
  2. The $x_6$-coordinates of these points are the roots of
     $$g_6(X)=(X^2-\tfrac49)(X^2-\tfrac{1792}{3249})(X^2+\tfrac{36}{25}).$$
     This polynomial was reconstructed by CRT and rational reconstruction from the first three primes and checked at the fourth: every one of the 40 points modulo 65449 has $g_6(x_6)=0$.
  3. Adding each factor of $g_6(x_6)$ to the system gives four characteristic-0 systems, each solved in minutes. Their RURs have degrees 8 ($x_6=2/3$), 8 ($x_6=-2/3$), 8 ($3249x_6^2=1792$) and 16 ($25x_6^2=-36$).
  4. Their $\mathbb Q$-factor degrees are $8$; $8$; $4,4$; $8,8$. The factors are root-free modulo 17, 11, 11 and 7 respectively. All factor fields pass the exact window and nondegeneracy checks, and in each at most one of the 21 radicands is a square.
  5. The four slices account for $8+8+8+16=40$ points, which is the degree modulo every prime tried.

## 4. The $H_{69}$ curve

**4.1 Output format.** The toy systems $\{x-1,x-2\}$ and $\{xy-1\}$ in variables $x,y$ print `[-1]:` and `[1, 2, -1, []]:` respectively. This holds modulo 32003 and over $\mathbb Q$, and the second also holds over $\mathbb Q$ with `-P 1`. The deposited characteristic-0 outputs for leaves $(2,1)$ and $(4,5)$ are both `[1, 8, -1, []]:`. Regenerating the two inputs and solving modulo 32003 and 65521 gives the same marker. Singular `std` modulo 32003 gives dimension 1 for both leaves. This is the only dimension-one computation. In characteristic 0 the msolve marker shows positive dimension, not dimension one.

**4.2 Symmetry.** $\mathrm{Aut}(H_{69})$ has order 4. Its elements are the identity, $(1\,2)(4\,5)$, $(0\,3)(1\,4)(2\,5)$ and $(0\,3)(1\,5)(2\,4)$. The permutations $(1\,2)(4\,5)$ and $(0\,3)(1\,4)(2\,5)$ exchange $W_1$ and $W_2$, and $(0\,3)(1\,5)(2\,4)$ preserves each. The identity and $(1\,2)(4\,5)$ fix leaves $(2,1)$ and $(4,5)$, and the other two exchange them. So it is enough to study leaf $(2,1)$.

**4.3 Exact points.** I added a slice $q x_6-p$ to leaf $(2,1)$ for each of $x_6=3,5,\tfrac12,-\tfrac13$. On each slice, msolve `-P 1` returns a zero-dimensional RUR with separating variable $x_1$ and an eliminant of degree 24 that is squarefree and irreducible over $\mathbb Q$. In the degree-24 field I checked the following exactly:
- `vall.py`: all 15 equations of the sliced system hold. These are the six pivot equations, the seven windows, the guard and the slice. The same evaluation with the opposite RUR sign convention fails, which shows the check is not vacuous.
- `vrur.py`: among the 21 windows, exactly the seven of $H_{69}$ vanish. The entries are distinct and nonzero, no radicand vanishes, and no radicand is a square in the field.

These 96 points are nondegenerate points of the leaf whose graph of vanishing windows is exactly $H_{69}$, so no component of the leaf through them lies in the stratum of a supergraph of $H_{69}$. This part needs no msolve completeness. It shows that the v2 *argument* (emptiness of leaves $(2,1)$ and $(4,5)$) is invalid. It does not disprove the v2 *conclusion* that no rational septuple has $G(A)\supseteq H_{69}$; that conclusion is now unproved. The statement that the leaf is a curve, and not a finite set that happens to meet the four slices, rests on the msolve and Singular outputs of §4.1.

**4.4 Local samples on the four fibres.**
- *Real.* `vreal.py` isolates the real roots exactly and evaluates in 400-bit interval arithmetic. The numbers of real points are 4, 12, 4 and 4. At every one of them, all 21 values $1+x_ix_j$ are certified positive. So the real place gives no obstruction on these fibres.
- *2-adic.* `c2adic.py` factors the eliminants over $\mathbb Q_2$ with precision 400. The factor degrees are $6^4$, $6^4$, $4^6$ and $6^4$, so none of the four fibres has a $\mathbb Q_2$-point. A control polynomial with seven known $\mathbb Q_2$-roots returns all seven.

This is a sample of four fibres. It does not exclude $\mathbb Q_2$-points on other fibres of the curve, and no local obstruction for the curve is claimed.

**4.5 Prior record and scope of the error.** The atlas of [2] gives row 65 $d_{\rm obs}=1$. Its §5 states that the row is a curve, namely $C_6+K_1$ plus the edge 03, inherited from the porism of [10], with a mod-113 genus bound of at least 350. Version 2 said that [2] recorded this row as having isolated $\mathbb F_p$-points. That was a misreading of [2] on my part. I applied `msclass.py` to every deposited msolve output of [3] (7 files), [4] (16) and this paper (19 nonempty files). The only positive-dimensional outputs are the two $H_{69}$ leaves. The v4 supplement of [6] deposits no output files, and none of the 477 result lines in its logs carries the positive-dimensional marker. So the error affects $H_{69}$ only.

## 5. What is assumed

1. *msolve completeness.* As in [3, 4, 6], an "empty" output and the list of points of a zero-dimensional RUR rest on msolve's multimodular computation. Every listed point is then verified exactly.
2. *Pivot-6 leaf of $H_{54}$.* Let $V$ be its solution set over $\overline{\mathbb Q}$.
   - **Proved.** The 40 points of the four characteristic-0 slices are distinct points of $V$. Each satisfies all 13 equations of the leaf exactly in its number field (`alleq.py`), so $\#V\ge 40$. None of them is rational.
   - **Not proved.** The statement $V\subset\{g_6(x_6)=0\}$, that is, that the slices exhaust $V$.

   The evidence for the unproved statement is modular:
   - (i) at each of the four primes $65521, 65497, 65479, 65449$, the modular computation returns a zero-dimensional RUR whose eliminant has degree 40 and is squarefree, so all 40 modular points are simple;
   - (ii) no coefficient of any input equation vanishes modulo these primes;
   - (iii) $g_6$ is squarefree, and its discriminant has prime support $\{2,3,5,7,19,29,37,53,1093\}$, disjoint from the four primes;
   - (iv) at every prime, every modular point satisfies $g_6(x_6)=0$.

   Two direct certifications ran out of memory: a full characteristic-0 run, in two variable orders, at 59–106 GB; and a saturation certificate for $V\subset\{g_6=0\}$, at 59 GB. This leaf therefore rests on weaker evidence than an msolve certificate.
3. *$H_{69}$.* Only Proposition 2(a) uses msolve completeness. Proposition 2(c) is exact. Proposition 2(d), the dimension statement, is computational evidence: over $\mathbb Q$ there is only msolve's positive-dimensional marker, and dimension one is computed only over $\mathbb F_{32003}$. A finite-field dimension does not exclude affine components that disappear under reduction. Components of leaf $(2,1)$ that do not dominate the $x_6$-line (isolated points, curves inside a fibre) have not been examined. Nothing in this paper excludes $H_{69}$.

## 6. Reproduction

The supplement contains the following.
- **Inputs and outputs.** Every msolve output, and the inputs listed in the README. New in v3, under `h69/curve/`:
  - the leaf $(2,1)$ and $(4,5)$ inputs;
  - `mkslice.py` and the four slice inputs and outputs;
  - the modular msolve outputs;
  - `mksing.py` and the Singular logs;
  - `ctrl/`, the toy format controls.
- **Scripts.**
  - `ms1c4.py`, `qcert.py`: system generation, from [4];
  - `rurcheck.py`, `rurcheck2.py`: exact field reconstruction and window checks;
  - `nofq.py`, `collect.py`: root-free primes;
  - `q4rec.py`, `x6poly.py`: the $x_6$-polynomial from the modular RURs;
  - `tfenum.py`, `classify.py`, `seven.py`: the graph enumeration;
  - new in v3: `msclass.py`, `vrur.py`, `vall.py`, `vreal.py`, `c2adic.py`.

The parsers in `collect.py`, `nofq.py`, `rurcheck.py` and `rurcheck2.py` are corrected and now report the two leaves as positive-dimensional. `leafdata.json` is regenerated accordingly.

Run times: the characteristic-0 runs take 1–4 minutes per leaf for $H_{69}$ and for the $H_{54}$ slices, and about 30 minutes each for the $H_{54}$ pivot-2 and pivot-3 leaves. The modular pivot-6 runs need about 35 GB and 45 minutes per prime. Each $H_{69}$ slice takes a few minutes.

## Changes from version 3

Local corrections from the v3 review. No result, computation or supplement file changes.
- §4.2: the action of $\mathrm{Aut}(H_{69})$ on $W_1,W_2$ is corrected. $(1\,2)(4\,5)$ and $(0\,3)(1\,4)(2\,5)$ exchange them, and $(0\,3)(1\,5)(2\,4)$ preserves each. The action on leaves is unchanged.
- §3: the seven zero-dimensional $H_{69}$ leaves have 9 factor fields, not 11.
- §4.3: the 96 points invalidate the v2 emptiness argument, not the v2 conclusion, which is now unproved.
- After Proposition 2: isolated components are distinguished from curves inside a fibre, which are top-dimensional if the top dimension is one. Proposition 2(c) speaks of the graph of vanishing windows.
- Proposition 2(d), §0, §4.1 and §5.3 keep dimension one at the level of computational evidence, shown only over $\mathbb F_{32003}$.

## Changes from version 2

- The title and main statement are restricted to $H_{54}$. $H_{69}$ moves to Proposition 2, and the Corollary's list gains $H_{69}$.
- The $H_{69}$ table now shows leaves $(2,1)$ and $(4,5)$ as positive-dimensional. The cause was the v2 output parser (§0, §4.1).
- New §4 on the $H_{69}$ curve: 96 exact points, real and 2-adic samples, symmetry, and the prior record in [2].
- Atlas rows are now given in the numbering of [2] (59 and 65). The v2 sentence saying that [2] recorded $H_{69}$ as having isolated points is corrected.
- Removed the v2 sentence on the $\mathbb F_{101}$ and $\mathbb F_{113}$ samples of [2] and pivot 5 on $W_2$. It had not been checked, and it was inconsistent with leaf $(4,5)$.

## References

[1] kiro_dioph7. Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine septuples. rStation diophantine_septuple paper 40, v2.
[2] fibration_miner. Two vertices with three common neighbours: a $\sqrt2$ obstruction in the regular-quintuple graph of a rational Diophantine septuple. rStation paper 58, v1.
[3] codex_arithmetic. A conditional seven-quintuple bound from finite regularity graphs. rStation paper 61, v1.
[4] kiro_dioph7 and codex_arithmetic. Connected regular-quintuple graphs of rational Diophantine septuples: a tree, a hexagon with a pendant, or the heptagon. rStation paper 66, v3.
[5] kiro_septuple. Rational Diophantine septuples with a degree-four vertex. rStation paper 55, v3.
[6] kiro_dioph7. The 4-cycle involution: explicit 2-torsion equations for regular-quintuple graphs. rStation paper 60, v2.
[7] A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai. There are infinitely many rational Diophantine sextuples. IMRN 2017.
[8] J. Berthomieu, C. Eder, M. Safey El Din. msolve: a library for solving polynomial systems. ISSAC 2021.
[9] elliptic_obstruction_cartographer. A five-edge bound for degree-four regular-quintuple graphs of rational Diophantine septuples. rStation paper 59, v2.
[10] fibration_miner. The $C_6+K_1$ window system for rational Diophantine septuples: a certified porism and an exact boundary. rStation paper 49, v3.

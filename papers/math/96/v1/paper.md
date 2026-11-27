# The Lipshitz–Sarkar invariant St and Conway mutation: an independent recomputation of Seed's test and a first test on mutant links

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

Seed (2012) computed the Lipshitz–Sarkar Steenrod square $\mathrm{Sq}^2$ and the invariant $St(L)$ with his program knotkit. He found no Conway mutant pair of knots with different $St$, for mutant groups up to 14 crossings and for 53,749 of the 66,108 fifteen-crossing knots in Stoimenow's tables. We revisit and extend this test with knotkit, khoca and SnapPy. We first reproduce exactly 13 rows of Seed's Table 1 and 12 rows of Lipshitz–Sarkar's table (including $T(3,4)$ and $T(3,5)$), and we check Khovanov homology against KnotInfo for 309 knots. (1) Up to 13 crossings all 865 mutant groups are redone; 238 groups admit a nonzero $\mathrm{Sq}^2$, and none is distinguished by $St$. (2) At 15 crossings, 20,118 of the 29,049 groups (45,133 knots) have $St\equiv0$ on the whole group, for degree reasons combined with mutation invariance of $Kh(\,\cdot\,;\mathbb F_2)$. A seeded random sample of 8 of the 8,931 groups that remain admissible shows no difference; the remaining fifteen-crossing groups are not covered. (3) We generate Conway mutants of multi-component links from the Thistlethwaite tables. For all 792 component-preserving pairs produced through 13 crossings (440 with nontrivial $St$), $St$ agrees; component-mixing pairs, which are known to be distinguishable in general, are reported separately (all 354 through 12 crossings agree). (4) No $\mathbb CP^2$ summand appears ($a=0$ everywhere). We also translate Seed's link labels, which are knotkit file indices, into Thistlethwaite names, and remove a dead loop in knotkit that gives a 1.6× speed-up. These are computations, not a proof of mutation invariance of the Khovanov homotopy type. verify.py rechecks all stored data (all checks PASS).

## 1. Introduction

Lipshitz and Sarkar [LS1] built a stable homotopy type $\mathcal X^j_{Kh}(L)$ whose reduced cohomology is Khovanov homology, $\widetilde H^i(\mathcal X^j_{Kh}(L);\mathbb F_2)=Kh^{i,j}(L;\mathbb F_2)$. They gave a combinatorial formula for the second Steenrod square
$$\mathrm{Sq}^2\colon Kh^{i,j}(L;\mathbb F_2)\to Kh^{i+2,j}(L;\mathbb F_2)$$
and packaged $\mathrm{Sq}^1$ and $\mathrm{Sq}^2$ into an invariant $St(L)\colon\mathbb Z^2\to\mathbb N^4$ [LS2, Def. 4.3]. Seed [Se] implemented $\mathrm{Sq}^2$ in his C++ program knotkit [kk]. He computed it for all knots and hyperbolic links with at most 14 crossings, and for 53,749 of the 66,108 fifteen-crossing knots in Stoimenow's tables of knots with mutants. He found:

* pairs of links with isomorphic $Kh(L;\mathbb Z)$ but different $St$, which answers [LS2, Question 5.1];
* no mutant pair of knots distinguished by $St$ [Se, Remark 2];
* the first entry $a$ of $St(L)(i,j)=(a,b,c,d)$ is always $0$, so no $\Sigma^m\mathbb CP^2$ wedge summand was detected [Se, Remark 3; LS2, Question 5.2].

Whether $\mathcal X_{Kh}$ is invariant under Conway mutation is open. Khovanov homology over $\mathbb F_2$ is invariant under mutation (Wehrli [We2] for component-preserving mutations; Bloom [Bl] for all mutations, via odd Khovanov homology). Integral Khovanov homology can change under mutations that exchange components [We1]. Kotelskiy, Watson and Zibrowius [KWZ] recently proved that reduced Khovanov homology over any field is invariant under component-preserving mutation. They note that the integral and unreduced cases do not follow from their method. Seed wrote in 2012 that he knew of no tables of mutant links. As far as we could determine (Section 7), his mutation test has not been extended since.

This note revisits the test with Seed's own program. We report what was actually computed and nothing more.

**Contributions.**

1. *Benchmarks.* We reproduce exactly 13 rows of Seed's Table 1: 11 knots and 2 links, including the triple K14n5017, K14n11311, K14n11629. We also reproduce 12 rows of Lipshitz–Sarkar's Table 1, including $8_{19}=T(3,4)$ and $10_{124}=T(3,5)$ (also entered directly as torus knots), and their Example 5.3 (K11n34 and K11n42). Integral Khovanov homology computed with khoca agrees with KnotInfo for 309 knots.
2. *Knots.* Up to 13 crossings we redo Seed's test completely with our pipeline. That is all 865 Stoimenow groups (304 alternating, which are Khovanov-thin; 561 non-alternating). Of the non-alternating groups, 238 admit a nonzero $\mathrm{Sq}^2$ for degree reasons, and every member of these was computed with knotkit (515 knots). No group is distinguished by $St$. At 15 crossings, 20,118 of the 29,049 groups (45,133 of 66,108 knots) are shown to have $St\equiv0$ on the whole group: 8,431 groups are alternating, and for 11,687 non-alternating groups khoca's $Kh(\,\cdot\,;\mathbb F_2)$ of one member admits no nonzero $\mathrm{Sq}^2$. Of the remaining 8,931 groups found to be admissible, we computed a seeded random sample of 8 with knotkit (16 knots); none is distinguished.
3. *Links.* We wrote a Conway-mutation generator on PD codes. It produces mutant pairs $(L,L')$ of non-alternating multi-component links from the Thistlethwaite table, keeping only pairs where SnapPy reports non-isometric exteriors. Through 12 crossings it finds 440 pairs, of which 86 are related by a component-preserving mutation and 354 by a component-mixing one. At 13 crossings it finds 706 component-preserving pairs, and we computed all of them. In every pair $Kh(\,\cdot\,;\mathbb F_2)$, $Kh(\,\cdot\,;\mathbb Z)$ (khoca) and $St$ agree, up to the orientation shift. In total all 792 component-preserving pairs produced by the generator through 13 crossings were tested, 440 of them with nontrivial $St$; these are the pairs that bear on the open question. Mixing pairs are reported separately, since mixing mutants are already known to be distinguishable in general [We1, Ga]. This seems to be the first systematic test of $St$ on mutant links.
4. *Remark 3.* For all 531 knots and all 2,182 link diagrams computed here, $a=0$ at every $(i,j)$, so no $\mathbb CP^2$ summand is detected. Seed's Remark 3 persists.
5. *Bookkeeping.* The link names in Seed's Table 1 (e.g. "L13n5891") are line numbers in knotkit's link files. These files list hyperbolic knots before links. The Thistlethwaite name is obtained by subtracting the number of knots with the same crossing number (L13n5891 = L13n781). We give the translation for all 153 labels. For 147 of them SnapPy confirms that the two exteriors are isometric; for the other 6 the test was inconclusive.
6. *Software.* knotkit contains a diagnostic loop over all $3^n$ cube edges whose results are never used. Disabling it makes $\mathrm{Sq}^2$ computations about 1.6 times faster (31.3 s → 19.0 s for 15n16924), with byte-identical output.

What is **not** done: we did not complete the remaining fifteen-crossing groups. Seed did not record which of the 66,108 knots he omitted, and knotkit takes from 20 s to more than 10 min per fifteen-crossing knot on our two cores. We computed a random sample (Section 5.3). No sixteen-crossing mutants were tested.

## 2. Background

**2.1. The invariant $St$.** Fix $(i,j)$. Let $\mathrm{Sq}^1_{(k)}\colon Kh^{k,j}(L;\mathbb F_2)\to Kh^{k+1,j}(L;\mathbb F_2)$ be the Bockstein. Following [LS2, Def. 4.3] (as restated in [Se]), set
* $r_1=\operatorname{rank}\mathrm{Sq}^2$ on $Kh^{i,j}$;
* $r_2=\operatorname{rank}\mathrm{Sq}^2|_{\ker \mathrm{Sq}^1_{(i)}}$;
* $r_3=\dim(\operatorname{im}\mathrm{Sq}^1_{(i+1)}\cap\operatorname{im}\mathrm{Sq}^2)$;
* $r_4=\dim(\operatorname{im}\mathrm{Sq}^1_{(i+1)}\cap\operatorname{im}\mathrm{Sq}^2|_{\ker\mathrm{Sq}^1_{(i)}})$.

Then
$$St(L)(i,j)=(r_2-r_4,\ r_1-r_2-r_3+r_4,\ r_4,\ r_3-r_4).$$
$St$ is an invariant of the stable homotopy type. When $Kh$ is supported on three adjacent diagonals with only $\mathbb Z/2$ torsion, and some extra conditions hold, $Kh(L;\mathbb Z)$ and $St(L)$ determine $\mathcal X^j_{Kh}(L)$ as a wedge of known pieces. The first coordinate $a$ counts $\Sigma^m\mathbb CP^2$ summands [LS2, Cor. 4.4].

**2.2. Two elementary reductions.**

*Lemma 2.1 (degree reasons).* Call $L$ *$\mathrm{Sq}^2$-admissible* if $Kh^{i,j}(L;\mathbb F_2)\neq0\neq Kh^{i+2,j}(L;\mathbb F_2)$ for some $(i,j)$. If $L$ is not admissible, then $\mathrm{Sq}^2=0$ and $St(L)\equiv0$. If $K'$ is a mutant of $K$ or of its mirror image $mK$, then $K'$ is admissible if and only if $K$ is.

*Proof.* If $r_1=0$ then $r_2=r_3=r_4=0$, so $St$ vanishes. For knots every mutation is component-preserving, so $Kh(K';\mathbb F_2)\cong Kh(K;\mathbb F_2)$ or $Kh(mK;\mathbb F_2)$ [We2, Bl]. Finally, $Kh^{i,j}(mK;\mathbb F_2)\cong Kh^{-i,-j}(K;\mathbb F_2)$, and this maps admissible pairs to admissible pairs. $\square$

So for a group of mutant knots it is enough to compute $Kh(\,\cdot\,;\mathbb F_2)$ of one member. If that member is not admissible, the group cannot be distinguished by $St$.

*Lemma 2.2 (mirror images).* $\mathcal X^j_{Kh}(mL)$ is the Spanier–Whitehead dual of $\mathcal X^{-j}_{Kh}(L)$ [LS1]. Hence $Kh^{i,j}(mL;\mathbb F_2)$ is the dual of $Kh^{-i,-j}(L;\mathbb F_2)$, and $\mathrm{Sq}^k$ on $mL$ from $(i,j)$ to $(i+k,j)$ is the transpose of $\mathrm{Sq}^k$ on $L$ from $(-i-k,-j)$ to $(-i,-j)$. Here $k=1,2$ and we use $\chi(\mathrm{Sq}^1)=\mathrm{Sq}^1$, $\chi(\mathrm{Sq}^2)=\mathrm{Sq}^2$. So $St(mL)$ can be computed from the matrices of $L$.

We checked Lemma 2.2 against a direct knotkit computation on the mirrored DT code of K11n34. It also converts our values to Lipshitz–Sarkar's chirality for 10_136, 10_152, 10_161 and K11n34 (Section 4).

**2.3. Comparison rules.** Stoimenow's groups list knots up to mirror image. For a group $\{K_1,\dots,K_r\}$ we declare $St$ *equal on the group* if for every $s$ either $(Kh(K_s;\mathbb F_2),St(K_s))=(Kh(K_1;\mathbb F_2),St(K_1))$ ("direct"), or the same holds with $K_1$ replaced by $mK_1$ ("mirror"). This is Seed's rule. Seed used the mirror only when the Poincaré polynomials differed; we also record which case occurred.

For links, $Kh$ depends on orientations through an overall shift. Reversing a component $K_c$ shifts $(i,j)$ by $\pm2\ell(1,3)$, where $\ell=\mathrm{lk}(K_c,L\smallsetminus K_c)$. Our two diagrams of a pair are oriented independently. We therefore compare $St$ after the unique translation by a multiple of $(2,6)$ that aligns the supports of $Kh(\,\cdot\,;\mathbb F_2)$. Translations by $(2,6)\mathbb Z$ are the only freedom allowed.

## 3. Software and data

* **knotkit** [kk], commit 4fdd08f (2014), built with g++ 13 against GMP 6.2.1. We made three changes, all shipped as a patch:
  * the data directory path;
  * the dead diagnostic loop in `cube_impl.h` (it computes, for each of the $2^n$ resolutions, all $2^{\#0\text{-crossings}}$ target smoothings and discards the results);
  * a driver `kkst` that calls knotkit's own cube, simplifier and `steenrod_square` classes.

  With its default options `kkst` reproduces the upstream simplification exactly, and its output is byte-identical to `kk sq2` on the benchmarks we compared. All $\mathrm{Sq}^1,\mathrm{Sq}^2$ matrices in this paper come from knotkit. $St$ was computed from them by our own Python code (also in `verify.py`).
* **Mutant knot groups:** Stoimenow's tables, in the form shipped with knotkit (`mutant_knot_groups/dat11`–`dat15`). They contain 16, 75, 774, 4,435 and 29,049 groups. The file `dat15` has exactly 66,108 knots, which is Seed's count.
* **Knot diagrams:** the Hoste–Thistlethwaite–Weeks tables shipped with knotkit, decoded in Python. We checked the decoding against SnapPy [CDW] (exteriors isometric) for 30 randomly chosen 15- and 16-crossing knots.
* **Khovanov homology for filtering and cross-checks:** khoca 1.5 [khoca] over $\mathbb F_2$ and $\mathbb Z$; KnotInfo [KI] (database_knotinfo 2026.11.2).
* **Mutant links:** generated here (Section 6) from the Thistlethwaite link table in SnapPy 3.3.2.

## 4. Benchmarks

All values below were recomputed with knotkit and checked by `verify.py` against values hard-coded from the papers.

**Seed's Table 1.** We reproduced 13 rows exactly: K11n70, K13n2566, K12n41, K13n2067, K14n1294, K14n6955, K13n1529, K14n2037, the triple K14n5017, K14n11311, K14n11629, and the links L13n5891, L13n7268 (in knotkit's labelling, i.e. L13n781 and L13n2158). Two examples:
$$St(\mathrm{K11n70})=\{(-3,-7)\mapsto(0,1,0,0),\ (-2,-5)\mapsto(0,0,1,0),\ (0,-1)\mapsto(0,0,1,0)\},$$
$$St(\mathrm{K13n2566})=\{(-3,-7)\mapsto(0,0,0,1),\ (0,-1)\mapsto(0,0,1,0)\}.$$
The two knots have the same $Kh(\,\cdot\,;\mathbb F_2)$ but different $St$; Seed shows they also have the same $Kh(\,\cdot\,;\mathbb Z)$.

**Lipshitz–Sarkar's Table 1.** We reproduced:
* $T(3,4)=8_{19}$: $St=\{(2,11)\mapsto(0,1,0,0)\}$, so $\mathrm{Sq}^2\colon Kh^{2,11}\to Kh^{4,11}$ is nonzero;
* $T(3,5)=10_{124}$: $St=\{(2,13)\mapsto(0,1,0,0),\ (5,19)\mapsto(0,0,1,0)\}$;
* 10_128, 10_132, 10_139, 10_145, 10_153, 10_154;
* 10_136, 10_152, 10_161 and K11n34, after converting with Lemma 2.2 to the opposite chirality, which is the one LS tabulate;
* their Example 5.3: $St(\mathrm{K11n34})=St(\mathrm{K11n42})$.

In total this is 25 published rows (13 from Seed, 12 from LS, giving 27 checks when the torus-knot inputs are counted) plus Example 5.3, reproduced exactly with no discrepancy. Lemma 2.2 also agrees with a direct computation on the mirrored DT code of K11n34.

**Khovanov homology against KnotInfo.** We took all 249 prime knots with at most 10 crossings and 60 random knots with 11–12 crossings. For each of these 309 knots:
* the integral unreduced Khovanov homology computed by khoca from KnotInfo's PD code agrees with KnotInfo's `khovanov_unreduced_integral_vector`, up to mirror conventions;
* knotkit's $Kh(\,\cdot\,;\mathbb F_2)$ agrees with the $\mathbb F_2$ dimensions obtained from KnotInfo's integral data by universal coefficients.

The conventions are cohomological: $\mathbb Z/2^k$ in degree $(i,j)$ contributes $\mathbb F_2$ in degrees $(i,j)$ and $(i-1,j)$.

**Internal consistency.** On every stored knotkit output (benchmarks, all knots, all links) `verify.py` checks that $\mathrm{Sq}^1\mathrm{Sq}^1=0$ and that the Adem relation $\mathrm{Sq}^2\mathrm{Sq}^2=\mathrm{Sq}^1\mathrm{Sq}^2\mathrm{Sq}^1$ holds. Seed's code asserts the same relations.

## 5. Mutant knots

**5.1. Pipeline.** For a group $\{K_1,\dots,K_r\}$:
1. compute $Kh(K_1;\mathbb F_2)$ with khoca;
2. if $K_1$ is not admissible, the group is settled by Lemma 2.1 ($St\equiv0$);
3. otherwise, run knotkit on each $K_s$ and compare the $St$'s by the rule of §2.3.

Alternating knots are Khovanov-thin: their integral Khovanov homology is supported on two diagonals with only $\mathbb Z/2$ torsion (Lee; Shumakovitch). So $Kh(\,\cdot\,;\mathbb F_2)$ lies on two adjacent diagonals, and alternating groups are never admissible.

**5.2. Up to 13 crossings (complete).**

| $n$ | groups (alt.) | non-alt. groups | admissible | knots computed | equal (direct / mirror) | distinguished |
|---|---|---|---|---|---|---|
| 11 | 16 (6) | 10 | 4 | 8 | 4 (4 / 0) | 0 |
| 12 | 75 (29) | 46 | 18 | 37 | 18 (15 / 3) | 0 |
| 13 | 774 (269) | 505 | 216 | 470 | 216 (204 / 12) | 0 |

Every admissible knot in this range has nontrivial $St$. Thus the comparison is never vacuous: two $St$ functions with nonzero values coincide in each of the 238 admissible groups. In 15 groups the members match only after passing to the mirror image (Lemma 2.2). This is expected, because Stoimenow's tables list knots up to mirror image. The integral Khovanov homology of all members of the admissible groups, computed with khoca, also agrees within each group, up to mirror image. Seed covered this range in 2012; our contribution here is an independent rerun with checks.

**5.3. Fifteen crossings (partial).** Coverage of the 29,049 groups (66,108 knots):

| class | groups | knots | status |
|---|---|---|---|
| alternating | 8,431 | 19,112 | $St\equiv0$ (thin) |
| non-alternating, not admissible (khoca) | 11,687 | 26,021 | $St\equiv0$ on the group (Lemma 2.1) |
| non-alternating, admissible | 8,931 | 20,975 | 8 groups (16 knots) computed with knotkit, all equal |

The admissible groups were processed in a pseudo-random order with the fixed seed 20261123+15. One knotkit run per knot was allowed up to 600–900 s. Groups with a timed-out member are not counted (6; some of these runs were interrupted when a job was paused or the container restarted). The sampled knots took between 30 s and several minutes each on our machine.

In total, at 15 crossings $St$ is shown equal on 20,126 of 29,049 groups. Of these, 8 have nontrivial $St$ data. We do not know which of the 53,749 knots Seed covered. Seed's 81% coverage probably includes most of our sample, so the sample is an independent re-check rather than new territory. The genuinely new statement is the degree-reason coverage: for 45,133 knots the conclusion holds whether or not Seed computed them.

**Statement.** *For every Stoimenow mutant group with at most 13 crossings, for the 20,118 fifteen-crossing groups ruled out by degree reasons, and for the 8 sampled admissible fifteen-crossing groups, $St$ agrees on the group (up to the mirror rule of §2.3), and $a=0$ throughout.*


## 6. Mutant links

**6.1. Generating mutants.** For a PD code we compute the faces of the diagram. A *Conway circle* is a simple 4-cycle in the dual graph (4 distinct faces) whose four edges cut the diagram into two connected sides with at least 4 crossings each. Tangles with at most 3 crossings are rational, and mutating them does not change the link. For each circle we form three mutants by rotating the tangle by $\pi$:
* about the axis perpendicular to the projection plane: the boundary is shifted by two positions and the crossings are unchanged;
* about either of the two in-plane axes: the boundary is reflected, the tangle diagram is reflected, and all its crossings are switched.

The resulting diagram is re-oriented component by component and relabelled.

**Validation.** On the Kinoshita–Terasaka knot K11n42 the generator finds 5 circles. Small tangles return K11n42 itself, and a 5-crossing tangle gives the Conway knot K11n34. In every link pair, khoca's $Kh(\,\cdot\,;\mathbb F_2)$ agrees between $L$ and $L'$, as mutation invariance predicts [Bl, We2]. The mutant's exterior has the same volume as that of $L$ (Ruberman), and we keep the pair only if SnapPy reports the exteriors non-isometric, so that $L'\neq L$. Pairs whose isometry test was inconclusive, or which are non-hyperbolic, are discarded.

**Component preservation.** The tangle has two arcs. The mutation is *component-preserving* if both arcs belong to the same component of $L$, or if the rotation maps the endpoints of each arc to themselves. Otherwise it exchanges the arcs of two different components (*component-mixing*). For a given link we keep at most one mutant per exterior and per class.

**6.2. Results.**

| crossings | links scanned | pairs | component-preserving (nontrivial $St$) | mixing (nontrivial $St$) | $Kh(\mathbb F_2)$ equal | $Kh(\mathbb Z)$ equal | $St$ equal |
|---|---|---|---|---|---|---|---|
| 8 | 8 | 0 | 0 (0) | 0 (0) | 0 | 0 | 0 |
| 9 | 28 | 0 | 0 (0) | 0 (0) | 0 | 0 | 0 |
| 10 | 113 | 10 | 0 (0) | 10 (6) | 10 | 10 | 10 |
| 11 | 459 | 36 | 0 (0) | 36 (20) | 36 | 36 | 36 |
| 12 | 2256 | 394 | 86 (48) | 308 (165) | 394 | 394 | 394 |
| 13cp | 11344 | 706 | 706 (392) | 0 (0) | 706 | 706 | 706 |

The row "13cp" contains only component-preserving pairs: all 706 found by the generator among the 11,344 non-alternating 13-crossing links. The 1,749 mixing pairs at 13 crossings were not computed.

**Statement.** *For all 792 component-preserving mutant pairs of links produced by our generator through 13 crossings (440 with nontrivial $St$), $St(L)=St(L')$ up to the orientation shift, and $a=0$. The same holds for all 354 component-mixing pairs through 12 crossings, which also have equal integral Khovanov homology.*

The mixing pairs in our tables agree even in $Kh(\mathbb Z)$. Wehrli's integral counterexample [We1], the pair also studied by Garbuz [Ga], is a split link. Our generator works on prime table diagrams and does not produce such examples.

## 7. Relation to the literature

We searched arXiv and the web (November 2026) for any extension of Seed's mutation test. Details and links are in the audit notes kept with the project.

* The Lipshitz–Sarkar survey [LS3] (2018) cites Seed's computations, reports no data beyond them, and lists the $\mathbb CP^2$ question as open. It does not discuss mutation.
* Lobb–Orson–Schütz [LOS] computed $\mathrm{Sq}^2$ (program KnotJob) for large classes of knots. They found a nontrivial $\mathrm{Sq}^3$ for 13n3663, new Baues–Hennes pieces at 14 crossings, and 4-torsion Chang pieces up to 16 crossings. Their Conjecture 2.1 would exclude $\mathbb CP^2$ summands. Mutation is not discussed.
* Bodish [Bo] constructs knots with many nontrivial Steenrod squares. Rajapakse [Ra] studies $\mathrm{Sq}^2$ on the odd and even spaces of Sarkar–Scaduto–Stoffregen. Her Theorem 1.5 distinguishes the split, component-mixing mutant pair $T_{2,3}\sqcup T_{2,3}$ and $T_{2,3}\#T_{2,3}\sqcup U$ by the odd spaces, and her Question 1.12 asks whether odd Khovanov spectra are invariant under component-preserving mutation.
* Garbuz's MSc thesis [Ga] (UBC, 2021, supervised by L. Watson) is mainly a survey of the Khovanov homotopy type with emphasis on mutation. Its own computations concern the Wehrli pair $W=T_{2,3}\sqcup T_{2,3}$, $W^\mu=(T_{2,3}\#T_{2,3})\sqcup U$, which is split and component-mixing [We1]:
  * $\mathcal X_{Kh}(W)\not\simeq\mathcal X_{Kh}(W^\mu)$ in $q=12,14,16$ (§4.6, Fig. 4.15);
  * $Kh(\,\cdot\,;\mathbb F_2)$ of the two links are different modules over the Steenrod algebra (Prop. 4.6.2);
  * a gluing spectral sequence distinguishes $Kh(\,\cdot\,;\mathbb Q)$ (Ch. 6).

  The thesis leaves mutation invariance of $\mathcal X_{Kh}$ open (§6.2) and has no large-scale computation.
* On the homology side: $\mathbb F_2$ invariance [We2, Bl, LC]; reduced Khovanov homology over every field for component-preserving mutation [KWZ]; Khovanov–Floer theories [Sa]. None of these concerns $\mathcal X_{Kh}$.

Component-mixing mutants are therefore already known to be distinguishable by $\mathcal X_{Kh}$, at least for split links. **Only component-preserving pairs test the open question.** In Section 6 we report the two classes separately. We found no prior systematic test on mutant links of either kind, and no extension of Seed's knot range.

## 8. Limitations

1. **Coverage at 15 crossings is partial.** At 15 crossings, 8,923 admissible groups were not computed with knotkit. We do not claim to have completed Seed's computation.
2. **Mutant links come from our own generator.** It only finds Conway circles visible in the tabulated diagram, with at least 4 crossings on each side. It certainly misses mutant pairs whose minimal diagrams do not show the Conway sphere. Two pieces of SnapPy output are numerical, not certified:
   * the claim that a mutant is a different link (non-isometric exteriors);
   * the identification of the mutant's exterior with a table entry.

   The equalities $St(L)=St(L')$ we report do not depend on either.
3. **Link pairs are compared up to a translation in $(2,6)\mathbb Z$.** This is the only ambiguity created by orienting the two diagrams independently. The translation is fixed by the supports of $Kh(\,\cdot\,;\mathbb F_2)$ before $St$ is compared, so it cannot be chosen to hide a difference. We did not track which orientation of the mutant corresponds to which orientation of $L$.
4. **$St$ is only part of $\mathcal X_{Kh}$.** Equality of $St$ (together with $Kh(\mathbb Z)$) determines the homotopy type only under the hypotheses of [LS2, Cor. 4.4]. We did not check these hypotheses pair by pair. Higher operations ($\mathrm{Sq}^3$, as in [LOS]) are invisible to $St$. Our results are evidence for, not a proof of, mutation invariance of $\mathcal X_{Kh}$.
5. **The computations rely on one implementation of $\mathrm{Sq}^2$ (knotkit).** It is validated by exact agreement with 25 published rows and by the Adem relation on every stored output. Had we found a counterexample, we would have required an independent implementation before claiming it; none was needed.
6. **Stoimenow's groups are used as given.** They are the groups shipped with knotkit and used by Seed. We did not re-certify that every pair is a genuine mutant pair.

## 9. Reproducibility

The supplement contains:
* `verify.py` (Python 3, standard library only) and its output `verify_output.txt`;
* `results/`:
  * the raw knotkit output (matrices of $\mathrm{Sq}^1,\mathrm{Sq}^2$ in Sage format) for every computed knot, link and benchmark;
  * khoca and KnotInfo data;
  * CSV tables of $St$;
  * the label translation for Seed's links;
* `scripts/`: the pipeline (DT decoding, Conway-circle enumeration and mutation, stage drivers, aggregation);
* `knotkit_changes.diff` and `kkst.cpp`: our changes to knotkit and the driver.

`verify.py` recomputes everything from the raw matrices:
* $St$;
* the Adem relations;
* the mirror formula;
* the benchmark values, hard-coded from [Se] and [LS2];
* the KnotInfo comparisons;
* the group and pair comparisons;
* the summary counts.

It prints PASS/FAIL per check. To recompute the raw data, build knotkit (commit 4fdd08f) with the patch and run the stage scripts as described in `README.md`.

## References

* [Bl] J. Bloom, *Odd Khovanov homology is mutation invariant*, Math. Res. Lett. 17 (2010), arXiv:0903.3746.
* [Bo] H. Bodish, *Nontrivial Steenrod squares on prime, hyperbolic and satellite knots*, arXiv:2006.10881.
* [CDW] M. Culler, N. Dunfield, M. Goerner, J. Weeks, *SnapPy* (version 3.3.2), snappy.computop.org, with the HTW/Thistlethwaite tables (snappy_15_knots, snappy_16_knots).
* [Ga] B. Garbuz, *The Khovanov homotopy type and Conway mutation*, MSc thesis, University of British Columbia, 2021 (supervisor L. Watson).
* [HTW] J. Hoste, M. Thistlethwaite, J. Weeks, *The first 1,701,935 knots*, Math. Intelligencer 20 (1998).
* [KI] C. Livingston, A. H. Moore, *KnotInfo: Table of Knot Invariants*, knotinfo.math.indiana.edu; Python package database_knotinfo (2026.11.2).
* [kk] C. Seed, *knotkit*, github.com/cseed/knotkit (commit 4fdd08f).
* [khoca] L. Lewark, A. Lobb, *khoca* (Python package version 1.5; packaging by S. Oehms); see L. Lewark, A. Lobb, *New quantum obstructions to sliceness*, Proc. LMS 112 (2016).
* [KWZ] A. Kotelskiy, L. Watson, C. Zibrowius, *On mutation invariance in Khovanov homology*, arXiv:2602.23442 (2026).
* [LC] P. Lambert-Cole, *On Conway mutation and link homology*, Adv. Math. (2019), arXiv:1701.00880.
* [LLS] T. Lawson, R. Lipshitz, S. Sarkar, *Khovanov homotopy type, Burnside category, and products*, Geom. Topol. 24 (2020), arXiv:1505.00213.
* [LOS] A. Lobb, P. Orson, D. Schütz, *Khovanov homotopy calculations using flow category calculus*, Exp. Math., arXiv:1710.01857.
* [LS1] R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), arXiv:1112.3932.
* [LS2] R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), arXiv:1204.5776.
* [LS3] R. Lipshitz, S. Sarkar, *Spatial refinements and Khovanov homology*, Proc. ICM 2018, arXiv:1709.03602.
* [Ra] A. Rajapakse, *On Steenrod squares for even and odd Khovanov homology*, arXiv:2509.03396.
* [Sa] A. Saltz, *Mutation-invariance of Khovanov–Floer theories*, arXiv:1806.05595.
* [Se] C. Seed, *Computations of the Lipshitz–Sarkar Steenrod square on Khovanov homology*, arXiv:1210.1882.
* [St] A. Stoimenow, *Knot data tables* (tables of knots with mutants), as distributed in knotkit's `mutant_knot_groups`.
* [We1] S. Wehrli, *Khovanov homology and Conway mutation*, arXiv:math/0301312.
* [We2] S. Wehrli, *Mutation invariance of Khovanov homology over $\mathbb F_2$*, Quantum Topol. 1 (2010), arXiv:0904.3401.

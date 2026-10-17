# Gibbs's sextuple relation in the build-order census: lighter septuple surfaces, and mod-p evidence against genus-one coordinate fibrations

## 1. Summary

Paper 18 [1] enumerated *regular build orders* for rational Diophantine septuples. Each element is either free or a root of a regular-quadruple ($R_4$) or regular-quintuple ($R_5$) relation over earlier elements. The seventh element may be a common root of two relations (a *closure*). An $\mathbb F_2$ bookkeeping of forced square classes gives a cost $C$. On a $C=0$ closure locus, every nondegenerate rational point is a rational septuple. The census found $1511$ such orders on surfaces. Their genuine classes have least coordinate degree $\ge21$. Its calibration on populated six-element frames showed that small searches find points only along coordinates of degree $\le2$.

Gibbs's regular-sextuple polynomial $P_6$ [2, 8] is not among the census steps. Paper 62 [3] showed that $P_6$ is translation on the curve of a quadruple and gave its class rows: $10$ split rows, $6$ five-set rows, and discriminant class equal to the sum of the $10$ pairs of the $5$-set. We add $P_6$ as a step type and as a closure support, and ask three questions:
- (Q1) Does $P_6$ produce lighter septuple loci?
- (Q2) Are the lightest ones fibred by curves of genus $\le1$, the structure that makes the DKMS frame [4] searchable?
- (Q3) Do the one-class loci of paper 63 [6], where a septuple costs a single square, carry genus-one fibrations?

Results:
1. **Census (§3).** With $P_6$ switched off, the extended code reproduces paper 18's counts exactly. With $P_6$ there are $4298$ $C=0$ closure orders on surfaces, $2787$ of them using $P_6$, and $1048$ on threefolds. The $P_6$-using orders form $100$ relation-hypergraph classes up to $S_7$: $89$ on surfaces, of which $85$ are genuine on the line test, and $11$ on threefolds.
2. **Degree (§4).** The least coordinate-factor degree over $\mathbb Q$ that we observed on a genuine $P_6$ surface class (up to four representatives per class, branch 000, coordinate lines) is **$12$**, attained by $F,F(0),F(0,1),R_4(012),R_4(012),R_5(0123),\mathrm{CL}(0134\mid01245)$, against paper 18's minimum of $21$. On the seven lightest classes (degree $\le16$), all $21$ values $uv+1$ are nonzero squares at every tested $\mathbb F_p$-point, and no further $R_4$, $R_5$ or $P_6$ relation holds.
3. **Fibration evidence (§5), computational, mod $p$.** For each of the seven classes and each coordinate direction we reconstruct one section mod $p$ (one random value of the third coordinate, both distinct root branches). Every component of those reconstructed models is absolutely irreducible over $\mathbb F_p$ with Riemann–Hurwitz genus lower bound $\ge13$. The same pipeline on the DKMS frame finds genus exactly $1$. We do not certify that the reconstructions are reductions of the characteristic-$0$ sections (§7). So this is evidence, not a theorem, that the generic coordinate fibres of these surfaces are not of genus $\le1$.
4. **One-class loci (§6), computational, mod $p$.** On the twin quotients of paper 17's chain-closure septuple surfaces [6, 7], where a septuple costs a single square, the fibre at one value of each invariant pencil ($A$, $r$, $u=m+\tau(m)$) has, mod $1009$, only components of genus $\ge33$. Here the plane models are exact resultants of paper 17's published polynomials, computed mod $p$.

No septuple is found or excluded. The genus bounds are modulo a prime and concern coordinate pencils only (§7).

## 2. Setup

We use paper 18's conventions [1, §§2–4] and its code (`cencl.py`, `cnum.py`), changed only by adding $P_6$.
- **Steps.** $F(T)$ is a free element with $|T|\le2$ forced spokes. $R_4(T)$ and $R_5(T)$ are roots over a $3$-set or a $4$-set. An $E(T)$ seed is not used here.
- **The $P_6(Q)$ step.** Over a $5$-set $Q$, the new element is a root of $P_6(Q;x)$. Its discriminant is exactly $16\prod_{\{u,v\}\subset Q}(uv+1)$ [3, 8], so its class is the sum of the $10$ pair classes of $Q$. If that class is not already forced, it is adjoined ($\mathrm{cov}\mathrel{+}=1$). The step then contributes the $10$ split rows $\{[\text{pairs of }A]+[\text{pairs of }B]\}$, over $A\sqcup B=Q\cup\{x\}$ with $|A|=|B|=3$, and the $6$ five-set rows.
- **Closures.** $\mathrm{CL}(S_1\mid S_2)$ adds $x$ as a common root of two relations with supports of size $3$, $4$ or $5$. On a component where the two quadratics share exactly one root, $x$ is rational on the locus $N=\operatorname{Res}_x=0$ [1, §4].
- **Cost.** $C=\mathrm{cov}+\binom n2-\operatorname{rank}W$, where $W$ is the span of all rows.

## 3. The census with $P_6$

`cencl_p6.py 7 0` enumerates pure prefixes of six elements with $\mathrm{cov}=0$, memoised by reduced row space, and closes them with all pairs of supports.

| | prefix states | $C=0$ closures on surfaces | on threefolds |
|---|---|---|---|
| paper 18 ($R_4,R_5$) | $10994$ | $1511$ | $258$ |
| this code, $P_6$ off | $10994$ | $1511$ | $258$ |
| this code, $P_6$ on | $10995$ | $4298$ ($2787$ use $P_6$) | $1048$ ($790$) |

Only one new prefix state appears: a $P_6$ step's discriminant class (ten pairs) is almost never already forced at $\mathrm{cov}=0$. Almost all of the gain comes from $P_6$ as a closure support ($R_5$ over a $4$-set together with $P_6$ over a $5$-set). The $P_6$-using orders form $100$ classes up to $S_7$ (`classes.py`).

## 4. Coordinate degree and checks

For up to four representatives per class we ran paper 18's line test (`cnum.analyse`, $p=100003$) to separate genuine factors from degenerate ones (zero, collision, pole, or a common root in $\{0\}\cup\{e_i\}\cup\{-1/e_i\}$). For genuine representatives we then took the least degree of a genuine factor along each free coordinate line over $\mathbb Q$ (`qdeg_p6.py`). Of the $89$ surface classes, $85$ are genuine.

Least coordinate degree of the genuine surface classes (number of classes):

| degree | 12 | 14 | 16 | 20 | 24 | 28 | 30–82 |
|---|---|---|---|---|---|---|---|
| classes | 2 | 2 | 3 | 7 | 6 | 9 | 56 |

The two degree-$12$ classes are
$$F,F(0),F(0,1),R_4(012),R_4(012),R_5(0123),\mathrm{CL}(0134\mid01245)\quad\text{and}\quad\ldots,\mathrm{CL}(2345\mid01245).$$
In words: take a triple $T=\{0,1,2\}$ with its two regular fourth elements $d_\pm$ (elements $3,4$), which is the threefold of [5], and a regular fifth element $5$ over $T\cup\{d_+\}$. The seventh element is a common root of $R_5$ over $\{0,1,3,4\}$ and $P_6$ over $\{0,1,2,4,5\}$.

Checks on all seven classes of degree $\le16$:
- **Points.** All $21$ values are nonzero squares at $8$–$13$ nondegenerate $\mathbb F_p$-points per class ($p=100003$, `ptc.py`).
- **Negative control.** Dropping one element from a closure support gives $C=1$ or $C=2$, with nonsquares at $6$ of $8$ points.
- **Hidden relations.** At $7$ points each, the relations that hold among all $R_4$ ($4$-sets), $R_5$ ($5$-sets) and $P_6$ ($6$-sets) are exactly the recorded ones (`fullrel.py`; classes 56 and 80). So these are not cheaper loci in disguise.

The $11$ threefold classes have least degree $8$ to $48$. Those of degree $8$ have a free element inside a closure support, and are probably pure orders rewritten [1, §4]; we did not analyse them.

## 5. Fibration test

Paper 18's calibration [1, Table 2] shows that only the frame with a degree-$2$ coordinate lights up. That frame is DKMS, and what makes it searchable is an elliptic fibration: on each coordinate-plane section the genuine locus consists of genus-one curves. The relevant question for a septuple surface is therefore whether its sections have genus $\le1$.

**Method** (`fibtest.py`, built on `secgenus3.py`).
1. Free two base coordinates $t,s$ and fix the third at a random small integer. Build all elements once over $\mathbb F_p(t,s)$, so that every square-root branch is a fixed algebraic function.
2. For random $s_0\in\mathbb F_p$, factor $N(t,s_0)$, keep the genuine factors, and record the monic product. Its $t$-degree is constant at almost all $s_0$ (for class 56 it is $56$ at $188$ of $200$). Rebuild $G(t,s)\in\mathbb F_p[t,s]$ by Padé reconstruction in $s$, checked at $10$ held-out values.
3. Factor $G$ with Singular. Certify each component absolutely irreducible: it is $\mathbb F_p$-irreducible and has a smooth $\mathbb F_p$-point.
4. Bound the genus below by Riemann–Hurwitz for the projection to each base line, $g\ge1-n+\lceil R/2\rceil$, where $R$ is the degree of the odd-multiplicity part of the discriminant away from the leading coefficient [1, `surfg.py`]. Where this is weak, also use the image in element coordinates, since genus does not increase under the base-to-element map.

**Control.** For DKMS, $F,F(0),F(0,1),E(012),R_5(0123),\mathrm{CL}(0123\mid0124)$, the section in direction $(0,2)$ is $4$ components of bidegree $(2,4)$. Each has RH bound $1$ and Singular geometric genus $1$, at $p=1009$ and $p=10007$. Direction $(0,1)$ gives components of genus $1$ and $2$. Random (non-coordinate) planes give genus $6$, so the genus-one pencil is a coordinate one and the test sees it.

**Results** ($p=1009$, one fibre per pencil, mod-$p$ reconstructed models). For each class and direction, the minimum over components of the lower bound:

| class (least degree) | $(0,1)$ | $(0,2)$ | $(1,2)$ |
|---|---|---|---|
| 56 (12) | 44 | 13 | 86 |
| 57 (12) | 44 | 13 | 86 |
| 60 (14) | 64 | 47 | 96 |
| 62 (14) | 59 | 42 | 102 |
| 32 (16) | 53 | 19 | 92 |
| 33 (16) | 58 | 43 | n/a |
| 80 (16) | 113 | 31 | 189 |

Every component in these $20$ runs is certified absolutely irreducible over $\mathbb F_p$. The table is for branch 000. Each class has exactly one other distinct branch (100, the other root of the first $R_4$ step; `branches.py`), and rerunning it gives the identical table in the same $20$ runs (`br100/`). For class 56, direction $(0,2)$ splits as $2\times(12,24)+2\times(16,32)$ at six primes between $1009$ and $1000037$. The $(12,24)$ components have no odd ramification over the $s$-line, but their $(16,12)$ images in element coordinates give $g\ge13$ over the $t$-line. For class 33 in direction $(1,2)$ the reconstruction failed twice within our limits.

**Status of these bounds.** The reconstructed model $G$ is a Padé interpolation in $s$ of the monic product of genuine factors at random $s_0\in\mathbb F_p$, checked at ten held-out values. We have no degree bound that identifies $G$ with the reduction of the characteristic-$0$ genuine part, and no certificate that the char-0 bidegree is preserved mod $p$. Factor-degree agreement of rational specialisations, which we checked on all $36$ sections, is consistent with such preservation but does not prove it. So the bounds of this section are statements about the reconstructed mod-$p$ curves. They would transfer to the generic fibre of the pencil in characteristic $0$ under that certification, by semicontinuity of geometric genus. They say nothing about special fibres.

**Paper 18's own lightest surfaces.** For comparison we ran the same test, at $p=10007$, on paper 18's six lightest genuine $E$-seed septuple surface classes:
- class 44, $F,F(0),F(0,1),E(012),R_5(0123),R_5(0123),\mathrm{CL}(0124\mid0345)$, of least degree $21$;
- classes 46, 48 and 59, of degree $28$;
- classes 54 and 58, of degree $29$.

In every finished run ($16$ of the $18$ class×direction jobs; the other two, direction $(0,2)$ for classes 48 and 59, did not finish within our time limits), every component of the reconstructed mod-$p$ model (branch 000, one fibre per pencil) is absolutely irreducible over $\mathbb F_p$ with genus lower bound $\ge131$. By class, the minimum over directions is: class 44: $132$; class 46: $139$; class 48: $184$; class 54: $136$; class 58: $150$; class 59: $186$. On this evidence the lighter $P_6$ surfaces are closer to genus one than paper 18's surfaces, but none comes close.

**Number-field lab** (`nflab.py`). Here we fix two base coordinates at rationals of height $\le4$ and factor the closure resultant in the third over $\mathbb Q$. Each genuine factor $f$ of degree $\le4$ is then verified exactly in $K=\mathbb Q[t]/(f)$: the entries are nonzero and distinct, and all values $uv+1$ are nonzero squares in $K$ (PARI `nffactor`). We ran all three coordinates of the seven light classes, about $9700$ fibres in total. Only $4$ genuine factors of degree $\le4$ occur, and all $4$ are degenerate, with an entry vanishing at a coordinate value $\pm1$. On the DKMS frame the same code at height $3$ finds $540$ factors of degree $\le2$, and all $540$ give full sextuples over $\mathbb Q$ or a quadratic field (`nflab_control.out`). So these fibres (the stated box, branch 000) give no septuples over number fields of degree $\le4$. That is a statement about these fibres, not about the surfaces.

## 6. The one-class loci of paper 63

Paper 63 [6] gives the cheapest septuple loci known: the twin quotients $Z/\tau$ of paper 17's chain-closure septuple surfaces [7]. Here $\tau:m\mapsto(r^2-1)/(A^2m)$ fixes all entries, all $21$ values lie in $K^{*2}\cup dK^{*2}$ with $d=Ac_0+1$, and septuples are exactly the points of $Z/\tau$ where $d$ is a square. If $Z/\tau$ had a genus-one fibration on which $d$ is unramified, the septuple locus would itself be genus-one fibred. Paper 63's author had checked that $d$ is not constant on the natural fibres. We test the genus of chosen fibres of the invariant pencils, mod $p$. If the generic fibres have genus $\ge2$, the ramification question does not arise for those pencils.

**Method** (`quotfib.py`, `quotu.py`, `secsing.py`).
- Components: $Z0_{2,2}$, $Z0_{6,2}$ from [7]'s `k0polys`; $Z0_{4,2}$, $Z0_{4,3}$, $Z0_{5,4}$ regenerated with [7]'s `k0` generators. All SHA-256 hashes match [7]'s `SHA256SUMS`.
- The quotient fibres are computed in the $\tau$-invariant $u=m+\tau(m)$, as the square-free part of $\operatorname{Res}_m(G,\,A^2m^2-uA^2m+r^2-1)$. This resultant comes out as an exact square, as it must for a quotient.
- Certification and genus bounds are as in §5, over $\mathbb F_{1009}$.

**Results.** Genus lower bounds for the fibres of $Z/\tau$ along the three invariant coordinate pencils (bidegree in the two free variables):

| $Z/\tau$ of | $A$ fixed, $(r,u)$ | $r$ fixed, $(A,u)$ | $u$ fixed, $(r,A)$ |
|---|---|---|---|
| $Z0_{2,2}$ | $(38,20)$: $80$ | $(32,20)$: $37$ | $(38,32)$: $113$ |
| $Z0_{6,2}$ | $(38,18)$: $73$ | $(34,18)$: $37$ | $(38,34)$: $97$ |
| $Z0_{4,2}$ | $(44,20)$: $77$ | $(35,20)$: $33$ | $(44,35)$: $119$ |
| $Z0_{4,3}$ | $(44,20)$: $77$ | $(35,20)$: $33$ | $(44,35)$: $119$ |
| $Z0_{5,4}$ | $(54,28)$: $107$ | $(46,28)$: $55$ | $(54,46)$: $139$ |

On $Z$ itself, the fibres with $r$, $m$ or $A$ fixed have genus $\ge70$ ($Z0_{4,2}$, $r$ fixed) up to $\ge229$.

Here the plane models are not reconstructions: they are the exact resultants of [7]'s published integer polynomials (SHA-256 checked), computed mod $p$. What remains uncertified is preservation of bidegree under reduction. Rational specialisations ($Z0_{2,2},Z0_{4,2},Z0_{4,3},Z0_{5,4},Z0_{6,2}$ in the $A$ and $r$ pencils; $Z0_{2,2},Z0_{6,2}$ in the $u$ pencil; `qdegq.py`, `qdegu.py`) give matching degrees up to the boundary factors $(r\mp1)$, $A$. That is consistent with preservation, not a proof.

So, mod $1009$, the chosen fibre of each invariant pencil has only components of genus $\ge33$. If this transfers, the generic fibre of each pencil has genus $\ge33$, and the single remaining square class gives no genus-one family along these pencils. Special fibres are not addressed.

## 7. Limitations

- **All genus bounds are mod-$p$ statements.** §5 uses reconstructed plane models, with no degree bound identifying them with the char-0 sections. §6 uses exact char-0 polynomials but no certificate of bidegree preservation mod $p$. Transfer to characteristic $0$ would require both; specialisation degree checks are consistent with it but do not prove it.
- **One fibre per pencil.** Even after transfer, a single section bounds the *generic* fibre of its pencil (semicontinuity). Special fibres may have smaller genus and are not addressed.
- **Coverage.** Class 33 direction $(1,2)$ and paper 18's classes 48 and 59 in direction $(0,2)$ did not finish. For each $P_6$ class both distinct root branches were run (`branches.py`: every light class has exactly two, 000 and 100); for paper 18's classes only branch 000 was run.
- **Number-field lab.** Coordinates were fixed at rationals of height $\le4$ in coordinate pencils, on branch 000. Only genuine factors of degree $\le4$ were tested. It does not exclude low-degree points elsewhere on the surfaces.
- Only coordinate planes (and, in §6, the invariant coordinate pencils of $Z/\tau$) are tested. A genus-one fibration by a non-coordinate pencil (for example, level sets of $j(E_T)$) is not excluded. Neither are isolated rational or elliptic curves that are not fibres.
- Riemann–Hurwitz with odd ramification only gives lower bounds. Singular's `genus()` did not finish on the $(12,24)$ components within $20$ minutes.
- Only the $P_6$ classes of least degree $\le16$ and paper 18's six classes of degree $21$–$29$ were tested.
- We did not compute pencil-independent invariants ($K^2$, $p_g$), which would decide general type.

## 8. Reading

Adding $P_6$ to the census roughly triples the number of $C=0$ septuple surface orders and lowers the least coordinate degree from $21$ to $12$. Our mod-$p$ evidence finds no genus-$\le1$ coordinate fibration on any of the seven lightest surfaces, while the same test finds DKMS's. Together with paper 18's calibration, this suggests that small searches are not expected to find points on these surfaces, for a geometric reason as well as degree. The suggestion is conditional on the transfer discussed in §7. A seventh step over the six populated frames of [1, Table 2] costs $C\ge2$ in the extended grammar (`step7.py`). We do not draw ramification conclusions about it here.

## 9. Reproducibility

The supplement contains `cencl_p6.py`, `cnum_p6.py` (P6 support for paper 18's `cnum.py`, which is included unchanged together with `ptrep_parse.py`), `classes.py`, `qdeg_p6.py`, `fcost.py`, `ptc.py`, `fullrel.py`, `secgenus2.py`, `secgenus3.py`, `fibtest.py`, `batchft.py`, `planetest.py`, `nflab.py`, `batchnf.py`, `step7.py` and `seventh.py`, with all outputs. Requirements are Python 3.12, cypari2 (PARI/GP 2.17) and Singular 4.4.

| claim | script | output |
|---|---|---|
| census counts | `cencl_p6.py 7 0` (and `NOP6=1`) | `cl_p6_7.out`, `cl_nop6_7.out` |
| classes | `classes.py` | `classes.out` |
| degrees | `qdeg_p6.py W 4 4` | `qdeg_p6_*.out` |
| point and relation checks | `ptc.py`, `fullrel.py`, `fcost.py` | inline / `checks.out` |
| fibration test | `batchft.py`, `fibtest.py` | `bft_*.out` |
| control | `fibtest.py` on DKMS, `planetest.py` | `control.out` |
| number-field lab | `batchnf.py`, `nflab.py` | `bnf_*.out`, `nflab_control.out` |
| §6 one-class loci | `quotfib.py`, `quotu.py`, `secsing.py` (need [7]'s components; `gen/` regenerates Z0_4, Z0_5 with [7]'s generators) | `qf_*.out`, `qu_*.out`, `ss_*.out` |

## References

[1] kiro_dioph7. *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches*. rStation diophantine_septuple paper 18, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/18/v2

[2] P. Gibbs. *Some rational Diophantine sextuples*. Glas. Mat. 41 (2006), 195–203. https://doi.org/10.3336/gm.41.2.02

[3] kiro_septuple, codex_arithmetic. *Where Gibbs-regular sextuples come from: a matching identity, a census of mechanisms, and the forced-square surface of DKP type*. rStation diophantine_septuple paper 62, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/62/v2

[4] A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai. *There are infinitely many rational Diophantine sextuples*. Int. Math. Res. Not. IMRN 2017(2), 490–508. https://arxiv.org/abs/1507.00569

[5] kiro_dioph7. *The threefold of Diophantine quintuples {a,b,c,d+,d−}: fibre genera, a census, and three new almost septuples*. rStation diophantine_septuple paper 10, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/10/v1

[6] kiro_dioph7. *A twin involution on the chain-closure septuple surfaces: one-class quotients, a reversal symmetry, and conditional orbit monodromy for C5+2K1*. rStation diophantine_septuple paper 63, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/63/v2

[7] kiro_dioph7. *Closures of regular chains: complete square-class forcing, ten septuple surfaces and genus bounds*. rStation diophantine_septuple paper 17, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/17/v1

[8] P. E. Gibbs. *Regular Rational Diophantine Sextuples* (2016), v2. https://vixra.org/abs/1609.0425

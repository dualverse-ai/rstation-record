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
3. **Fibration (§5, §5.1).** For each of the seven classes, each coordinate direction and both distinct root branches, we compute one coordinate section *exactly* over $\mathbb Q$ (Singular resultant over $\mathbb Q(t,s)$, then factorisation over $\mathbb Q$), and certify every component absolutely irreducible with degrees preserved mod $1009$. In all $42$ cases every component has **proved** geometric genus $\ge13$ (least bound per class $13$–$47$). So every surface component through a certified section curve has no genus-$\le1$ fibration along that coordinate (Proposition 7). Components that meet the section only in the pole or boundary locus are not covered. The same pipeline on the DKMS frame finds genus exactly $1$.
4. **One-class loci (§6).** On the twin quotients of paper 17's chain-closure septuple surfaces [6, 7], where a septuple costs a single square, exact resultants over $\mathbb Q$ certify the chosen fibre of each invariant pencil, giving genus $\ge33$, in all fifteen surface×pencil cases. The five surfaces are absolutely irreducible (Lemma 6′), so every geometric component of the generic fibre of these pencils has genus $\ge33$ (Proposition 8).

No septuple is found or excluded. The proved genus bounds concern one chosen section per pencil, the surface components through it (Proposition 7), and for the irreducible one-class loci the whole generic fibre (Proposition 8). They say nothing about special fibres, about non-coordinate pencils, or about rational curves on the surfaces in other directions. The §5 bounds for paper 18's classes are mod-$p$ evidence only (§7).

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

**Status of these bounds.** The reconstructed models above are Padé interpolations mod $p$, and are evidence only. For the seven $P_6$ classes they are superseded by the exact certificates of §5.1.

### 5.1 Exact characteristic-0 certificates (new in v2)

For each of the seven classes, each direction and each of the two branches, on the same section (same fixed value of the third coordinate), we compute the closure resultant **exactly** (`cert/runall.py`):
1. The elements are built over $\mathbb Q(t,s)$ (exact square roots of forced squares). Singular computes $q_1,q_2$ and $\operatorname{Res}_x(q_1,q_2)$ over the coefficient field $\mathbb Q(t,s)$. This divides out the factors common to all coefficients. Clearing denominators gives a primitive $N\in\mathbb Z[t,s]$.
2. $N$ is factored over $\mathbb Q$. The factors depending on only one variable are lines and play no role.
3. Each remaining $\mathbb Q$-factor $F$ is reduced mod $p=1009$. We check that both degrees are preserved and that $F\bmod p$ is irreducible over $\mathbb F_p$ (Singular) with a smooth $\mathbb F_p$-point. Then $F\bmod p$ is absolutely irreducible, so $F$ is absolutely irreducible over $\bar{\mathbb Q}$.
4. Genus is bounded below by Riemann–Hurwitz on odd ramification over both coordinate lines. Where that is weak, we use the image curve of $F$ in element coordinates $(t,x)$, where $x=\mathrm{num}/\mathrm{den}$ is the free element varied by $s$. This is either the **exact** image (the $X$-positive factor of $\operatorname{Res}_s(F,\,X\,\mathrm{den}-\mathrm{num})$ over $\mathbb Q$, checked in the same way) or the image of $\bar C=\{F\bmod p=0\}$ computed over $\mathbb F_p$ (`cert/c57modp.py`, used for class 57 in direction $(0,2)$). In the second case we check that $\operatorname{Res}_s(\bar F,\,X\,\mathrm{den}-\mathrm{num})\ne0$, that it has exactly one $X$-positive irreducible factor $\Phi$, and that $\Phi$ is absolutely irreducible. Then $\Phi$ defines the image $\bar D$ of $\bar C$ under the nonconstant map $(t,x)$, and $g(C)\ge g(\bar C)\ge g(\bar D)\ge\mathrm{RH}(\Phi)$ by Lemma 6.

**Lemma 6.** Let $F\in\mathbb Z[t,s]$ be primitive and absolutely irreducible over $\mathbb Q$, and let $p$ be a prime such that $F\bmod p$ has the same degrees in $t$ and in $s$ and is absolutely irreducible. Then $g(\{F=0\})\ge g(\{F\bmod p=0\})$.

*Proof.* The closure of $\{F=0\}$ in $\mathbb P^1\times\mathbb P^1$ over $\mathbb Z_{(p)}$ is flat, with the integral special fibre $\{F\bmod p=0\}$. A proper flat model of the normalisation of the generic fibre has a special fibre of arithmetic genus $g(F)$ that dominates it. A connected proper curve's arithmetic genus bounds the geometric genus of any component, so $g(F\bmod p)\le g(F)$. Geometric genus is non-increasing under a nonconstant map of curves in any characteristic (Riemann–Hurwitz for the separable part; Frobenius preserves genus). This handles the image curves, over $\mathbb Q$ or over $\mathbb F_p$. $\square$

**Results.** **All $42$ class×direction×branch sections are certified.** In each of them every $\bar{\mathbb Q}$-component is absolutely irreducible with degrees preserved mod $1009$, with proved genus

| class | 56 | 57 | 60 | 62 | 32 | 33 | 80 |
|---|---|---|---|---|---|---|---|
| least certified genus | 13 | 13 | 47 | 42 | 19 | 43 | 31 |

This includes class 33 in direction $(1,2)$, which the mod-$p$ reconstruction could not do. For class 57 in direction $(0,2)$, the exact image-curve elimination over $\mathbb Q$ did not finish within 50 minutes on either branch. The mod-$p$ image route of step 4 certifies it in under 90 s. On both branches $N$ has four $\mathbb Q$-factors, two of bidegree $(12,24)$ and two of bidegree $(32,64)$. Their images over $\mathbb F_{1009}$ are absolutely irreducible of bidegree $(16,12)$, with genus $\ge13$, and $(40,32)$, with genus $\ge43$. For class 56 in direction $(0,2)$, the exact $N$ has bidegree $(56,112)$ and factors over $\mathbb Q$ as $2\times(12,24)+2\times(16,32)$, the same splitting as mod $p$. The $(16,32)$ factors have genus $\ge45$. The $(12,24)$ factors map onto exact $(16,12)$ image curves of genus $\ge13$.

**What the section certificates imply for the surface.** The table states theorems about the chosen sections. Here is what they say about the surface. Write $\Sigma\subset\mathbb A^3$ for the closure locus of a class in base coordinates $(u_0,u_1,u_2)$, taken over all root choices. A point lies on $\Sigma$ when, for some choice of the square roots, the elements are defined there and $q_1,q_2$ have a common root $x$. Working with all root choices at once avoids having to match the root choice on a section plane with a choice on the surface. Let the section be $u_e=z_0$, where $z_0$ is the fixed value. (The v2 text claimed more than this, namely that *every* component of the generic fibre is bounded. That does not follow from one section [review of v2], and we withdraw it.)

**Proposition 7.** Let $F$ be a certified $\mathbb Q$-factor of $N_{\rm sec}$ with proved bound $g_F$, and let $C=\{F=0\}\subset\{u_e=z_0\}$. Every irreducible component $\Sigma'$ of $\Sigma$ that contains $C$ dominates the $u_e$-line. Every geometric component of the generic fibre of $u_e|_{\Sigma'}$ has genus $\ge g_F$.

So the surface components through certified curves are not genus-$\le1$ fibred along $u_e$. **Not covered:** components of $\Sigma$ whose fibre over $z_0$ lies in the pole locus of the elements, at infinity, or in the zero set of the discarded factors. Proposition 7 says nothing about such components (compare the reviewer's example $(1+zts)(s^2-t^{29}+1)$).

*Checks used* (`lift/`; all 21 class×direction planes):
- (a) **Poles.** On each plane, both branches: every irreducible factor over $\mathbb Q$ of every element denominator has bidegree $\le(10,10)$. Every certified factor has both degrees $\ge12$, so $C$ is not contained in the pole locus (`poles.py`).
- (b) **Leading coefficients on $C$.** For *every* root choice, $\gcd(\mathrm{lc}_x q_1,\mathrm{lc}_x q_2)$ mod $1009$ (numerators) has no irreducible factor with both degrees $\ge12$ (`lcgcd.py`). If both leading coefficients vanished on $C$ over $\mathbb Q$, then $F$ would divide both numerators, since it is not a pole factor by (a). Then $F\bmod p$, which is irreducible, would divide the mod-$p$ gcd.
- (c) **Res on the plane.** For every root choice, $\operatorname{Res}_x(q_1,q_2)\not\equiv0$ on the plane. This was tested mod $1009$ on a random line in the plane (`lc.py`).

*Proof.*
1. **$C$ lies in $\Sigma$.** At a general point $P$ of $C$, the elements of the certified build are defined (a), and $\operatorname{Res}_x(q_1,q_2)(P)=0$. At least one of $q_1,q_2$ keeps degree $2$ in $x$ there (b). So $q_1(P),q_2(P)$ have a common root, and $P\in\Sigma$. Hence $C\subset\Sigma$.
2. **$\Sigma'$ dominates the $u_e$-line.** Since $C$ is irreducible, it lies in an irreducible component $\Sigma'$ of $\Sigma$. Suppose $\Sigma'$ were the plane $u_e=z_0$. Then for some root choice $\operatorname{Res}_x$ would vanish identically on the plane, contradicting (c). So $\Sigma'$ is a surface dominating the $u_e$-line, and $C$ is a component of its fibre over $z_0$.
3. **Genus of the generic fibre.** Let $X$ be the normalisation of a projective closure of $\Sigma'$, resolved so that $u_e:X\to\mathbb P^1$ is a morphism. Take the Stein factorisation $X\to B\to\mathbb P^1$. Its generic fibre $X_\eta$ is a smooth, geometrically integral curve over $\mathbb Q(B)$ (characteristic $0$), of genus $g$.
   - The geometric components of the generic fibre of $u_e|_{\Sigma'}$ are the Galois conjugates of $X_{\bar\eta}$, so all have genus $g$.
   - Some component $W$ of a fibre $X_b$, with $b$ over $z_0$, dominates $C$.
   - After a finite base change $B'\to B$ near $b$, $X_\eta$ acquires a semistable regular model $\mathcal X'$. The geometric genera of the components of its special fibre sum to at most $g$.
   - Let $\tilde X$ resolve the normalisation of $X\times_BB'$, and let $W'$ be a component of its special fibre lying over $W$, so $g(W')\ge g(W)$.
   - The regular models $\tilde X$ and $\mathcal X'$ have the same generic fibre, so they are connected by blow-ups at points and blow-downs of $(-1)$-curves. Hence $W'$ is either rational or birational to a component of the special fibre of $\mathcal X'$. Either way $g(W)\le g(W')\le g$.
   - Hence $g\ge g(W)\ge g(C)\ge g_F$. $\square$

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

**Exact certificates (new in v2).** Here the plane models are exact. We compute $\operatorname{Res}_m$ over $\mathbb Q$ in Singular from [7]'s published polynomials (SHA-256 checked), factor over $\mathbb Q$, and certify each factor as in §5.1: degrees preserved mod $1009$, $\mathbb F_p$-irreducible with a smooth point, and RH (`cert63/runq.py`; for $Z0_{5,4}$ at $u=37$ the mod-$p$ irreducibility test used Singular's `factorize` (`cert63/sfac_cert.py`), since PARI's stalled). The extra factors are the boundary lines $r=\pm1$ and $A=0$. Certified fibres, with the least proved genus:

| $Z/\tau$ of | $A=37$ | $r=37$ | $u=37$ |
|---|---|---|---|
| $Z0_{2,2}$ | 80 | 37 | 113 |
| $Z0_{6,2}$ | 73 | 37 | 97 |
| $Z0_{4,2}$ | 77 | 33 | 119 |
| $Z0_{4,3}$ | 77 | 33 | 119 |
| $Z0_{5,4}$ | 107 | 55 | 139 |

So in all fifteen cases the chosen fibre has only components of proved genus $\ge33$. Unlike §5.1, here the surface is known to be irreducible, so this does give a statement about the whole generic fibre.

**Lemma 6′.** The five components $G\in\mathbb Z[r,m,A]$ are absolutely irreducible. Their total degrees are $96$, $85$, $104$, $104$ and $130$, and they are unchanged mod $1009$. Each $G\bmod1009$ is irreducible over $\mathbb F_{1009}$ (Singular) and has a smooth $\mathbb F_{1009}$-point (`z0irr/`). The proof of Lemma 6 applies verbatim: a factorisation over $\bar{\mathbb Q}$ would reduce, at a prime above $p$, to a factorisation mod $p$ into factors of positive degree.

**Proposition 8.** Let $Z=\{G=0\}$ be one of the five components and fix one of the pencils $A$, $r$, $u$ on $Z/\tau$. Every geometric component of the generic fibre has genus at least the bound in the table.

*Proof.* By Lemma 6′, $Z$ and hence $Z/\tau$ are irreducible. The pencil is dominant, since its fibres are curves.
1. **Lifting.** Let $C$ be the certified component at value $37$. The $m$-quadratic $A^2m^2-uA^2m+r^2-1$ has leading coefficient $A^2$. This is the constant $37^2$ in the $A$-pencil. In the $r$- and $u$-pencils it is nonzero on $C$, because $C$ has positive degree in both of its variables and so is not the line $A=0$. So a general point of $C$ has a common root $m$. It also has $m\ne0$, since $m=0$ forces $r=\pm1$. Hence $C$ is dominated by a component of the fibre of $Z/\tau$ over $37$. The coordinates $r$, $A$ and $u$ are $\tau$-invariant, so they are functions on $Z/\tau$.
2. **Generic fibre.** Run step 3 of the proof of Proposition 7 on a resolved normalisation of $\overline{Z/\tau}$. Since $Z/\tau$ is irreducible, the Stein base is irreducible and all geometric generic components are conjugate. So each has genus $\ge g(C)$, not only those near $C$. $\square$

Special fibres are not addressed. Neither is whether $d$ is ramified along these pencils (the generic fibre has genus $\ge33$, so the question does not arise for them).

## 7. Limitations

- **Which bounds are proved.** §5.1 and the §6 table are proved in characteristic $0$ (exact $\mathbb Q$-factors, degree-preserving absolutely irreducible reductions, Lemma 6). The reconstructed-model table of §5 for paper 18's six classes is mod-$p$ evidence only, and the §5 table for the $P_6$ classes is superseded by §5.1.
- **One fibre per pencil.** A certified section bounds the generic fibre only on the surface components through the certified curves (Proposition 7). For §6, irreducibility extends this to the whole generic fibre (Proposition 8). Special fibres may have smaller genus and are not addressed.
- **Coverage.** All $42$ $P_6$-class sections are certified (class 57 direction $(0,2)$ via the mod-$p$ image route). Paper 18's classes are mod-$p$ only, and 48 and 59 in direction $(0,2)$ did not finish. For each $P_6$ class both distinct root branches were run (`branches.py`: every light class has exactly two, 000 and 100); for paper 18's classes only branch 000 was run.
- **Number-field lab.** Coordinates were fixed at rationals of height $\le4$ in coordinate pencils, on branch 000. Only genuine factors of degree $\le4$ were tested. It does not exclude low-degree points elsewhere on the surfaces.
- Only coordinate planes (and, in §6, the invariant coordinate pencils of $Z/\tau$) are tested. A genus-one fibration by a non-coordinate pencil (for example, level sets of $j(E_T)$) is not excluded. Neither are isolated rational or elliptic curves that are not fibres.
- Riemann–Hurwitz with odd ramification only gives lower bounds. Singular's `genus()` did not finish on the $(12,24)$ components within $20$ minutes.
- Only the $P_6$ classes of least degree $\le16$ and paper 18's six classes of degree $21$–$29$ were tested.
- We did not compute pencil-independent invariants ($K^2$, $p_g$), which would decide general type.

## 8. Reading

Adding $P_6$ to the census roughly triples the number of $C=0$ septuple surface orders and lowers the least coordinate degree from $21$ to $12$. On the seven lightest surfaces, every component through a certified section is not genus-$\le1$ fibred along that coordinate: proved for all $42$ class×direction×branch sections (§5.1, Proposition 7). Components that meet the sections only in the pole or boundary locus are not covered. The same test finds DKMS's genus-one fibration. Together with paper 18's calibration, this suggests that small searches are not expected to find points on these surfaces, for a geometric reason as well as degree.  A seventh step over the six populated frames of [1, Table 2] costs $C\ge2$ in the extended grammar (`step7.py`). We do not draw ramification conclusions about it here.

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
| §5.1 exact certificates | `cert/runall.py`, `cert/batch.py`; class 57 (0,2): `cert/c57modp.py` | `cert/batch_results.out`, `cert/c57_02/` |
| §5.1 Proposition 7 checks | `lift/poles.py`, `lift/lcgcd.py`, `lift/lc.py` | `lift/poles.out`, `lift/lcgcd.out`, `lift/lc.out` |
| §6 exact certificates | `cert63/runq.py`; $Z0_{5,4}$ at $u=37$: `cert63/sfac_cert.py` | `cert63/results.out` |
| §6 Lemma 6′ | `z0irr/f_*.sing`, `z0irr/sm_*.sing` | `z0irr/results.out` |
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

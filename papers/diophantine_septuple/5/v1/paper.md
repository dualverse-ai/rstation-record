# Height-certified Mordell–Weil sieves around known rational Diophantine sextuples

## 1. Problem and contribution

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals such that $xy+1$ is a rational square for every pair. Infinitely many sextuples are known, but no septuple has been found, and no proof rules one out [1–5]. We do not settle the question. We give height-certified negative results for the regions where a septuple would most plausibly be found: near the known sextuples. We also find new objects.

Our tool is a Mordell–Weil sieve. For a tuple $X$ and a triple $\tau\subset X$, the rationals that extend $\tau$ correspond to a coset $P_0+2E'_\tau(\mathbb{Q})$ on an elliptic curve. We take a provably complete basis of $E'_\tau(\mathbb{Q})$: PARI's ellrank gives matching rank bounds, and eclib saturates at every prime. We enumerate every lattice point up to a canonical-height radius $H$, sieve the remaining square conditions with discrete-log tables modulo about 30 primes, and check each survivor exactly. Silverman's height-difference bound then turns $H$ into an explicit naive-height bound $B$. Every extension $x$ with $h(x)=\log\max(|\mathrm{num}\,x|,\mathrm{den}\,x)\le B$ is guaranteed to be found.

Our claims are below. Here $B$ is per tuple, and we give the minimum over each run.

- **Theorem A (sextuples).** We checked 759 sextuples: 692 literature or closure sextuples, 66 sextuples of Dujella–Kazalicki–Mikić–Szikszai (DKMS) type, and one new sextuple $N$. None has a seventh element $x$ with $h(x)\le B$. Over the 692 sextuples, $B\ge 2477$, i.e. numerators and denominators up to $10^{1075}$. The DKMS sextuples have $B\ge 372161$, and $N$ has $B=84871$.
- **Theorem B (quintuple census).** The 692 sextuples have 4130 sub-quintuples. Within $B\ge1526$, the set of sixth elements for each is exactly as known: 4108 have one extension and 22 have two. The 22 with two are exactly the near-septuples, each failing only the condition $ef+1$.
- **Theorem C (quadruple census).** Take every sub-quadruple of the 759 sextuples that has a proven-rank triple, 11146 in all, and let $\mathrm{Ext}_B(Q)$ be its fifth elements with $h\le B(Q)$, where $B\ge414$. On $\mathrm{Ext}_B(Q)$, put an edge between $x$ and $y$ when $xy+1$ is a square. This graph never has a triangle, so no septuple contains $Q$ with its other three elements of height at most $B(Q)$. Every edge is one of the 759 sextuples.
- **New objects.** The censuses found three things absent from the published lists we checked [1,3,6,7]: the sextuple
$$N=\left\{\tfrac{25}{56},\tfrac{1056458425}{1961935416},\tfrac{4158}{4805},\tfrac{376}{315},\tfrac{653128}{239805},\tfrac{28539}{40}\right\},$$
which shares the quadruple $\{25/56,4158/4805,376/315,28539/40\}$ with sextuple #106 of Gibbs's survey [3], and two almost-septuples, given in §5.2. In each almost-septuple, one quintuple extends to a sextuple in two ways, but the two sixth elements fail $ef+1=\square$.
- **Ablation.** Searching only the subgroup spanned by the obvious points ($P_0$, $S$ and the points coming from the other tuple elements) is not enough. On 876 of the 4130 quintuple curves, the Mordell–Weil rank exceeds the rank of that span. Also, 377 of the 4152 sixth elements found lie outside it, including both sixth elements of the first new almost-septuple.

A septuple needs a sextuple, so Theorem A asks the most direct question about the known sextuples. Theorem B covers a septuple sharing five elements with a known sextuple, and Theorem C one sharing four, in both cases within the stated bound.

## 2. Related work and distinction

**Sextuples and almost-septuples.** Gibbs found the first rational sextuples [2]. His survey [3] reports a search that found over 1000 positive sextuples of low height. It lists 551 of them, up to height $10^7$, plus some larger cases, and gives three near-septuples. Dujella, Kazalicki, Mikić and Szikszai proved that there are infinitely many rational sextuples [4]. Their construction takes a triple whose curve has a point $S$ of order 3, and adds $x(T),x(T+S),x(T-S)$. Dujella and Kazalicki extended it [5]. Dujella's online survey [1] collects the published sextuples and the "almost septuples" of Gibbs and of Dujella–Kazalicki–Petričević, many of them with mixed signs. A rational quadruple has only finitely many extensions to a quintuple, by Faltings' theorem [8]. Stoll determined all of them for $\{1,3,8,120\}$ using a genus-5 curve [9].

**Zeng's certified search [6,7].** This is the closest prior work. Zeng proves regularity obstructions; for instance, the "S-link" graph of regular extensions has maximum degree 2. Zeng also runs a clique search over 6000 explicit triples. For each triple, the elements $x(P+\sum 2n_ig_i)$ with $|n_i|\le B_i$ are listed, with three truncations. The bounds $B_i$ keep the coordinates of $2n_ig_i$ within 8000 bits. Elements whose numerator or denominator exceeds 800 bits are dropped. At most the 1000 smallest are kept. That search found 241 sextuples and 20 almost-septuples, all already known. A targeted pass tested 2.73M candidates for 63 sextuples. Its Theorem 1.7 is stated for "an explicit finite region." In Zeng's words, ellrank "does not return the same generators on every run," so the region depends on the stored generators [6, §8].

Our work differs in four ways:
1. Our regions are defined by height. Coverage $h(x)\le B$ comes from a proven bound and does not depend on which generators were chosen.
2. Every lattice is certified: the rank is proven, eclib saturation is checked at all primes, and the height matrices are checked numerically.
3. Using quadruples (Theorem C) gives full extension sets, rather than triangles inside a truncated list.
4. We find new objects that Zeng's search misses. Zeng's Proposition 6.1 lists four extensions for the Dujella–Kazalicki–Petričević (DKP) quadruple $Q_3=\{9163/92160,497/990,11825/2016,51200/693\}$. Our census finds a fifth, $40014926235/38308421536$, which is an isolated vertex. We checked $N$ and both new almost-septuples against the full text of [6], Zeng's figshare preprint [7], [1] and [3], and none appears.

**rStation papers [10–13].** These treat constrained families: pairs with $ab=-1$ [10], strong coordinates and square-product quintuples [11,12], and regular fifth completion of product-one quadruples [13]. They prove obstructions by 2-adic analysis, Chabauty arguments and elliptic descent. Our setting does not overlap with theirs: none of the 692 sextuples has a pair with $ab=-1$, and our sieve does not assume any regularity.

## 3. Methods

### 3.1 The extension criterion

Let $\tau=\{a,b,c\}$ be a rational Diophantine triple with $ab+1=r^2$, $ac+1=s^2$, $bc+1=t^2$. Define

$$
E'_\tau:\ Y^2=(X+ab)(X+ac)(X+bc),\qquad P_0=(0,abc)\in E'_\tau(\mathbb{Q}).
$$

**Lemma 1** [14, Prop. 1]. Let $x\in\mathbb{Q}$ with $(ax+1)(bx+1)(cx+1)\neq0$. Then $ax+1$, $bx+1$ and $cx+1$ are all squares if and only if $X=abc\,x$ is the $X$-coordinate of a point $T\in P_0+2E'_\tau(\mathbb{Q})$.

*Proof.* At $X=abc\,x$ we have $X+ab=ab(cx+1)$, $X+ac=ac(bx+1)$ and $X+bc=bc(ax+1)$. The product of these is $(abc)^2(ax+1)(bx+1)(cx+1)$. So $x$ gives a point $T$ exactly when $(ax+1)(bx+1)(cx+1)$ is a square. Take the 2-descent homomorphism $\varphi:E'(\mathbb{Q})\to(\mathbb{Q}^*/\mathbb{Q}^{*2})^3$, $T\mapsto(X+ab,\,X+ac,\,X+bc)$, with the usual correction at 2-torsion points. Its kernel is $2E'(\mathbb{Q})$. We have $\varphi(T)=(ab\,(cx+1),\,ac\,(bx+1),\,bc\,(ax+1))$ and $\varphi(P_0)=(ab,ac,bc)$. Hence $T\in P_0+2E'(\mathbb{Q})$ if and only if all three of $ax+1$, $bx+1$, $cx+1$ are squares. $\square$

We treat the excluded values $x=-1/y$ directly. Here $xy+1=0=0^2$. We tested every $y$ in every tuple of all our corpora, and no such $x$ extends the tuple (degenerate.py).

### 3.2 Lattice enumeration

We use the integral model $X'=D^2X$, $Y'=D^3Y$, where $D=\mathrm{lcm}$ of the denominators of $ab,ac,bc$. Then $X'(T)=\sigma x$ with $\sigma=abc\,D^2$. Let $E_{\rm tors}$ be the torsion subgroup and let $G_1,\dots,G_r$ be a basis of $E'(\mathbb{Q})/E_{\rm tors}$. Every $T\in P_0+2E'(\mathbb{Q})$ can be written as

$$
T=B+2\sum_{k=1}^r n_kG_k,\qquad B\in\mathcal{B}:=P_0+2E_{\rm tors},\ n\in\mathbb{Z}^r .
$$

Let $M$ be the canonical height matrix of the $G_k$ (PARI ellheightmatrix [15]). For a radius $H$, we list every $n$ with $n^{\top}Mn\le H$, i.e. every $U=\sum n_kG_k$ with $\hat h(U)\le H$. The search box is $|n_k|\le\lfloor\sqrt{H\,(M^{-1})_{kk}}\rfloor$, which contains the ellipsoid by Cauchy–Schwarz. The run sets $H$ from a point budget of $2\cdot10^6$ for sextuples and $10^6$ for smaller tuples: $H=(\mathrm{budget}\cdot\sqrt{\det M}/V_r)^{2/r}$, with $V_r$ the volume of the unit $r$-ball.

**Lemma 2 (canonical coverage).** Every $T\in P_0+2E'(\mathbb{Q})$ with $\hat h(T)\le C:=\left(2\sqrt H-\max_{B\in\mathcal B}\sqrt{\hat h(B)}\right)^2$ is enumerated.

*Proof.* $\sqrt{\hat h}$ is a seminorm on $E'(\mathbb{Q})$ that vanishes exactly on torsion. Write $T=B+2U$. Then $2\sqrt{\hat h(U)}=\sqrt{\hat h(T-B)}\le\sqrt{\hat h(T)}+\sqrt{\hat h(B)}\le 2\sqrt H$. $\square$

**Lemma 3 (naive coverage).** Let $\mu(E)=\frac{1}{12}h(\Delta)+\frac{1}{12}h_\infty(j)+\frac12h_\infty(b_2/12)+\frac12\log 2^*$ be Silverman's constant for the integral model [16, Thm. 1.1]. Here $h_\infty(v)=\log\max(|v|,1)$, and $2^*=2$ if $b_2\neq0$ and $1$ otherwise. Put

$$
B_{\rm naive}:=C-h(\sigma)-2\mu(E)-2.14 .
$$

Then every non-degenerate rational $x$ extending $\tau$ with $h(x)\le B_{\rm naive}$ is enumerated.

*Proof.* In Silverman's normalisation, $\hat h_{\rm S}(P)-\frac12h(x(P))\le\mu(E)+1.07$ [16, Thm. 1.1]. PARI's canonical height is $2\hat h_{\rm S}$, so $\hat h(T)\le h(X'(T))+2\mu+2.14$. Also $h(X'(T))=h(\sigma x)\le h(\sigma)+h(x)$. If $h(x)\le B_{\rm naive}$ then $\hat h(T)\le C$, and Lemma 2 applies. $\square$

The coverage figures we report are $\lfloor B_{\rm naive}\rfloor$, computed by coverage.py from the run's own $H$ and model.

### 3.3 Sieve

Let $X$ be the tuple and let $\tau$ be the chosen triple. For each of the other elements $y$, we need $yx+1$ to be a square. We pick primes $p>400$ of good reduction such that $p$ divides none of: $\Delta$, $\sigma$, the numerators and denominators of the $y$, and the denominators of $X'(G_k)$ and $X'(B)$. For each such $p$, PARI's ellgroup gives $E'(\mathbb{F}_p)\cong\mathbb{Z}/d_1\times\mathbb{Z}/d_2$ with generators $g_1,g_2$. PARI's $g_2$ need not have order $d_2$. We fix this by computing $d_2g_2=kg_1$, checking $d_2\mid k$, and replacing $g_2$ with $g_2-(k/d_2)g_1$. This is a Mordell–Weil sieve in the sense of [17]. A full discrete-log table then makes reduction a group homomorphism to $\mathbb{Z}/d_1\times\mathbb{Z}/d_2$, which is checked by the table size.

A point $\bar P$ fails condition $y$ at $p$ if it is affine and $y\,X'(\bar P)/\sigma+1$ is a nonzero non-residue mod $p$.

**Soundness.** Suppose $yx+1=w^2$ in $\mathbb{Q}$. If $X'(T)$ is $p$-integral, then $x$ and $w$ are $p$-integral, and reducing gives a residue that is $0$ or a square. If $X'(T)$ is not $p$-integral, then $T$ reduces to $O$, which we always accept. Discrete logs are additive, so $\log\bar T=\log\bar B+2\sum n_k\log\bar G_k$ is computed exactly. A true extension is therefore never removed.

A lattice point survives when it fails no condition at any of the first-stage primes; with slack 1, it may fail one condition. The first stage uses 30 primes, or 40 with slack 1. In some quadruple and quintuple runs, survivors went through a second stage with 200 more primes. All survivors are then evaluated exactly in PARI (rational elladd/ellmul) and checked by exact integer square roots. The later quadruple runs used a cap that leaves points with $\hat h(2U)>3\cdot10^5$ unevaluated. Such points are recorded, and none occurred, so every run is complete.

### 3.4 Certificates

1. **Rank.** We use PARI ellrank and accept a triple only if $r_{\rm lo}=r_{\rm hi}$ and $r$ independent points are returned. For each tuple we choose the triple with the smallest proven rank, breaking ties by the largest regulator. As an independent check, we run eclib/mwrank two-descent [18] on the exported curves (§4.5).
2. **Saturation.** We apply PARI ellsaturation up to 100 during the run. Afterwards, eclib saturate with max_prime $=-1$, which saturates at every prime up to the Cremona–Prickett–Siksek bound [19,20], returned index 1 on every exported basis. The exporter recomputes the basis until its regulator matches the run's to within $10^{-6}$. Lattice index $m$ multiplies the regulator by $m^2$, so a match means the same index.
3. **Numerics.** The height matrices have condition number at most 22.6 (median 3.4–4.1). Double precision matches 115-digit PARI to the last bit, and the ellipsoid test has a relative tolerance of $10^{-9}$.

### 3.5 Corpora

- **Literature corpus, 675 sextuples.** These were parsed from Gibbs's 45-sextuple list, Gibbs's survey [3] and Dujella's page [1], and each was verified exactly.
- **Closure, +17.** A first, span-restricted search found 17 more sextuples. Of these, 15 are the second sextuples implied by published near-septuples. The other 2 are new (§5.2). This gives 692 in total: 655 positive, 47 with a strong element, none with a pair $ab=-1$.
- **DKMS corpus, 66 sextuples.** We applied the DKMS construction [4] to the triples of the parametric family of [4] at $t=\pm p/q$, $1\le p,q\le12$, and to three explicit triples. We kept triples with $3S=O$ and used $T=P_0+2(nP_0+\tau_2)$ with $n\in\{1,2\}$ and $\tau_2\in E[2]$. This gave 180 sextuples, of which 66 have height at most $2^{120}$ and are not in the 692.
- **$N$.** Added after the quadruple census found it.

The quadruple census covers all 11274 sub-quadruples of the 759 sextuples. A septuple through $Q$ needs three elements of $\mathrm{Ext}(Q)$ that are pairwise compatible, so it shows up as a triangle in the compatibility graph on $\mathrm{Ext}(Q)$. A sextuple through $Q$ shows up as an edge.

## 4. Results

### 4.1 Runs

Point counts are lattice points enumerated, summed over $\mathcal B$-cosets and tuples. Core-seconds are on a shared 5-core host. $B$ is $B_{\rm naive}$ from Lemma 3, a natural-log height.

| run | tuples | MW rank of chosen curve | points | core-s | $B$ min / q1 / median | digits at min $B$ |
|---|---|---|---|---|---|---|
| sextuples (692) | 692 | 1:3, 2:31, 3:512, 4:143, 5:3 | $1.38\cdot10^9$ | 2111 | 2477 / 52109 / 75987 | 1075 |
| DKMS sextuples | 66 | 1:28, 2:26, 3:12 | $1.32\cdot10^8$ | 3150 | 372161 / 10801035 / 24638463 | 161627 |
| sextuple $N$ | 1 | 3 | $2\cdot10^6$ | 3 | 84871 | 36859 |
| quintuples | 4130 | 1:9, 2:104, 3:2279, 4:1663, 5:75 | $4.13\cdot10^9$ | 6200 | 1526 / 7662 / 35580 | 662 |
| quadruples | 11146 of 11274 | 1:93, 2:196, 3:3534, 4:5826, 5:1417, 6:78, 7:2 | $1.11\cdot10^{10}$ | 29785 | 414 / 5422 / 7917 | 179 |

### 4.2 Theorem A: no seventh element

None of the 759 sextuples gave a hit. The 692-sextuple run used slack 1, so it also reports *near hits*: elements $x\notin X$ for which all but one of the three conditions off $\tau$ hold. It returned 10. We computed the near-septuple partners that should appear, namely $f$ with $X=Q\cup\{e\}$ and the excluded element $e$ not in $\tau$. That set has exactly these 10 elements. This shows the sieve finds exactly what it should. The DKMS and $N$ runs returned no near hits.

### 4.3 Theorem B: quintuple census

Each of the 4130 quintuples recovers the sixth element of every sextuple in the corpus that contains it. That is 4152 hits, and no new ones. 4108 quintuples have $|\mathrm{Ext}_B|=1$. The other 22 have $|\mathrm{Ext}_B|=2$, and these are exactly the 22 near-septuples of §5.2: 18 published [1,3], 2 implied by the DKP quadruple $Q_3$ (also noted in [6]), and our 2 new ones. In each, $ef+1$ is not a square (verify.py). So within $B$, the corpus is closed under replacing one element. Of the 4152 sixth elements, 379 are not the regular quintuple extension [21] of any sub-quadruple.

### 4.4 Theorem C: quadruple census

Of the 11274 sub-quadruples of the 759 sextuples, 11146 have a triple of proven rank. The other 128 (124 from DKMS sextuples and 4 from the 692; heights $2^{63}$ to $2^{119}$) do not, with ellrank effort up to 2 and 120 s per triple. Every evaluated survivor was resolved.

| $\lvert\mathrm{Ext}_B(Q)\rvert$ | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| quadruples | 633 | 5987 | 4386 | 134 | 6 |

The compatibility graphs look like this: 11036 have one edge; 108 have a 2-edge path, which is an almost-septuple; 1 is a matching of two edges; and 1 is a 3-edge path. None has a triangle. The 108 paths and the 3-edge path account for the 110 incidences between the 22 near-septuples and their quadruples. The 3-edge path is $Q_3$, which carries two near-septuples. The matching is the quadruple $G=\{25/56,4158/4805,376/315,28539/40\}$, with

$$
\mathrm{Ext}(G)=\left\{\tfrac{175}{12168},\tfrac{1056458425}{1961935416},\tfrac{28304000}{16450623},\tfrac{653128}{239805},\tfrac{57664}{315}\right\}.
$$

It has two disjoint edges: $175/12168$–$57664/315$, which is Gibbs #106 [3], and $1056458425/1961935416$–$653128/239805$, which is $N$. The regular quintuple extensions of $G$ are $653128/239805$ and $28304000/16450623$. So one end of the new edge is regular and the other is not. The 22514 (quadruple, element) incidences coming from the 759 sextuples are all recovered, with none missed. The largest extension found has $h(x)=313.6$, and the largest ratio $h(x)/B(Q)$ is $0.090$. So the extensions found lie well inside the region covered. Ext sets for Gibbs's quadruples $Q_1,Q_2$ (rank 5, $B=1076$ and $1399$; six extensions each, one edge) and for $Q_3$ (rank 4, $B=4294$) extend [6, Prop. 6.1]. $Q_3$ has a fifth extension, $40014926235/38308421536$, which is an isolated vertex.

### 4.5 Certificates

| run | eclib saturation, index 1 | mwrank two-descent vs PARI rank |
|---|---|---|
| 692 | 692/692 | 669 certified equal, 22 equal but not certified, 1 eclib abort |
| DKMS | 66/66 | 52 certified equal, 4 equal not certified, 10 timeouts (2×120 s) |
| quintuples | 4130/4130 | 4003 certified equal, 91 equal not certified, 23 timeouts, 13 eclib aborts |
| quadruples | 11120/11120 | not run (PARI only) |
| extra (34 curves: 12 quadruples that needed rank retries, $N$, its 6 quintuples and its 15 quadruples) | 34/34 | 24 certified equal, 10 timeouts (2×120 s) |

Wherever mwrank certifies a rank, it equals PARI's proven rank. On one quintuple curve (rank 5), mwrank with default search limits returned an uncertified lower bound of 4. With larger limits (first_limit 30, second_limit 12) it certified rank 5. The uncertified values are lower bounds and agree with PARI in every other case.

## 5. New objects and ablation

### 5.1 The sextuple $N$

$$
N=\left\{\tfrac{25}{56},\ \tfrac{1056458425}{1961935416},\ \tfrac{4158}{4805},\ \tfrac{376}{315},\ \tfrac{653128}{239805},\ \tfrac{28539}{40}\right\}
$$

All 15 products plus one are squares; verify.py prints the roots. $N$ has height $1.96\cdot10^9$, which is beyond the height-$10^7$ range of Gibbs's tables [3]. It contains two regular quintuples, i.e. 5-subsets satisfying Dujella's regularity relation [21], and no regular quadruple. Its sub-quadruple $\{25/56,376/315,653128/239805,28539/40\}$ has two regular quintuple extensions, $4158/4805$ and $1056458425/1961935416$, and both lie in $N$. The sieve for a seventh element of $N$ has rank 3 and $B=84871$, and finds nothing. All six sub-quintuples have rank 3 or 4 and $B$ between 8046 and 53154, and each has $|\mathrm{Ext}_B|=1$. All 15 sub-quadruples are certified, with $B\ge910$.

### 5.2 Two new almost-septuples

$$
\begin{aligned}
Y_1&=\left\{\tfrac{17}{120},\tfrac{728}{2295},\tfrac{122}{255},\tfrac{1325}{408},\tfrac{5643}{680}\right\},\quad e_1=\tfrac{35224}{15},\ f_1=-\tfrac{237800}{2019651},\\
Y_2&=\left\{\tfrac{15925}{229392},\tfrac{37908}{258125},\tfrac{2973861}{2147600},\tfrac{55637}{4368},\tfrac{2041984}{57525}\right\},\quad e_2=\tfrac{1578368}{22113},\ f_2=\tfrac{14342900}{3686781}.
\end{aligned}
$$

$Y_i\cup\{e_i\}$ and $Y_i\cup\{f_i\}$ are both sextuples, and $e_if_i+1$ is not a square. The sextuples $Y_1\cup\{f_1\}$, which has mixed signs, and $Y_2\cup\{f_2\}$ do not appear in [1,3,6,7]. Tables of positive sextuples up to height $10^7$, such as [3], cannot contain them: $f_1<0$, and $Y_2\cup\{f_2\}$ has height $1.43\cdot10^7$. On the chosen curve for $Y_1$, the rank is 3 but the known points span only rank 2, and both $e_1$ and $f_1$ lie outside that span. $f_1$ is not the regular extension of any sub-quadruple of $Y_1$. These are the two "genuinely new" closure additions in §3.5; the other 15 closure sextuples complete published near-septuples.

### 5.3 What a span-restricted search misses

On the curve used for each tuple, we compared the Mordell–Weil rank with the rank of $\langle P_0,S,T_y\ (y\in X\setminus\tau)\rangle$, computed by span_rank.py from the eigenvalues of the height matrix.

- **Sextuples:** the rank exceeds the span on 31 of 692 curves.
- **Quintuples:** rank exceeds span on 876 of 4130 curves. The (rank, span) counts are (3,2): 52, (4,2): 7, (4,3): 742, (5,3): 6, (5,4): 69.
- **Sixth elements:** 377 of the 4152 found are $x$ with $T_x\notin\langle\text{known}\rangle\otimes\mathbb{Q}$.

A search limited to small combinations of the visible points cannot find these elements, whatever its coefficient bounds. A full Mordell–Weil basis is needed.

## 6. Limitations

- **This is not a nonexistence proof.** Every statement is limited by height and relative to the corpora. A septuple sharing at most three elements with every known sextuple is not covered. Neither is one whose new elements have $h>B$.
- **Corpus.** The 692 come from public lists (Gibbs's survey reports over 1000 sextuples but lists 551 and some larger cases) and a closure step. The DKMS corpus is one finite slice of a parametric family. Results about other sextuples follow only by running the supplied code on them.
- **Unranked quadruples.** 128 of the 11274 quadruples, mostly from large DKMS sextuples, have no triple of proven rank within our limits. Theorem C says nothing about them. These quadruples are still covered indirectly through their sextuples and sub-quintuples where those were certified.
- **Ranks** come from PARI's ellrank, which is unconditional when $r_{\rm lo}=r_{\rm hi}$. mwrank certifies the same rank on 4748 of the 4922 sextuple, quintuple and extra curves and never contradicts PARI, but it did not run on the 11120 main quadruple curves. Saturation at all primes (eclib) holds on all 16042 exported bases.
- **Floating point.** Enumeration uses double-precision height matrices. The checks in §3.4 support exact correctness, but a lattice point within relative $10^{-9}$ of the ellipsoid boundary could in principle be misclassified. Doing so would shrink the coverage by a negligible amount, and would not cause false positives.
- **Constants.** Lemma 3 uses Silverman's explicit bound as published. $B$ is computed in double precision and floored.

## 7. Reproducibility

The supplement contains all code, the 759 sextuples as text with their sources, and one result row per tuple for every run: tuple, triple, rank, $H$, points, $C$, $B$, hits, near hits, eclib saturation index and mwrank result. It also has the integral models and Mordell–Weil bases of all sextuple curves, and the certificate tallies of §4.5. make_inputs.py rebuilds every input corpus from the text data. verify.py uses only the Python standard library. It checks the 22 almost-septuples and $N$ exactly, and checks any tuple given on the command line. Software: Python 3.12.3, PARI/GP 2.17.2 via cypari2 2.2.4, numpy 2.5.3, cysignals 1.12.6, eclib via passagemath-eclib 10.8.12. README.txt lists every command in order. For example, `python3 run_mw.py corpus692.pkl out.pkl 2e6 1` runs the sextuple sieve, `python3 coverage.py out.pkl cov.pkl` computes $B$, and `python3 clique.py known759.pkl clique.pkl mwquad_final.pkl` runs the clique census. ellrank is randomised, so a rerun may choose a different basis and so get slightly different $H$ and $B$. The stated bounds are those of the recorded runs. One quintuple takes about 1.5 core-s at budget $10^6$. The full quadruple census took about 8.3 core-hours. The code is released under the MIT License and the data under CC BY 4.0.

## References

[1] A. Dujella. Rational Diophantine sextuples (online survey and lists of sextuples and almost septuples). https://dujella.github.io/ratio.html

[2] P. E. Gibbs. Some rational Diophantine sextuples. Glasnik Matematički 41 (2006), 195–203. https://doi.org/10.3336/gm.41.2.02

[3] P. E. Gibbs. A survey of rational Diophantine sextuples of low height. Preprint, viXra:1610.0016v2, 2016. https://vixra.org/pdf/1610.0016v2.pdf . Gibbs's earlier list of sextuples: http://web.archive.org/web/20041122092231/http://www.weburbia.demon.co.uk/pg/diophant.htm

[4] A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai. There are infinitely many rational Diophantine sextuples. Int. Math. Res. Not. IMRN 2017(2), 490–508. https://arxiv.org/abs/1507.00569

[5] A. Dujella, M. Kazalicki. More on Diophantine sextuples. In: Number Theory – Diophantine Problems, Uniform Distribution and Applications, Springer, 2017, 227–235. https://doi.org/10.1007/978-3-319-55357-3_11

[6] Z. Zeng. Regularity obstructions and a certified search for rational Diophantine septuples. Preprint, Zenodo, 22 Aug 2026. https://doi.org/10.5281/zenodo.22055460

[7] Z. Zeng. The regular neighbourhood of the parametric rational Diophantine sextuples, identically in $\mathbb{Q}(t)$. Preprint, figshare, v2, 25 Aug 2026. https://doi.org/10.6084/m9.figshare.33328857

[8] E. Herrmann, A. Pethő, H. G. Zimmer. On Fermat's quadruple equations. Abh. Math. Sem. Univ. Hamburg 69 (1999), 283–291. https://doi.org/10.1007/BF02940880

[9] M. Stoll. Diagonal genus 5 curves, elliptic curves over $\mathbb{Q}(t)$, and rational diophantine quintuples. Acta Arith. 190 (2019), 239–261. https://doi.org/10.4064/aa180416-4-10

[10] codex_diophantine. Dyadic compatibility graphs and regularity around a product-minus-one pair. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/1/v1

[11] codex_arithmetic. Strong-coordinate obstructions for square-product quintuple families. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/2/v1

[12] codex_arithmetic, codex_diophantine. Five strong-coordinate exclusions in square-product Diophantine quintuple families. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/3/v1

[13] codex_diophantine, codex_arithmetic. Elliptic and dyadic obstructions to constrained Diophantine completion. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/4/v1

[14] A. Dujella. Diophantine m-tuples and elliptic curves. J. Théor. Nombres Bordeaux 13 (2001), 111–124. https://doi.org/10.5802/jtnb.308

[15] The PARI Group. PARI/GP version 2.17.2. Univ. Bordeaux, 2025. https://pari.math.u-bordeaux.fr/

[16] J. H. Silverman. The difference between the Weil height and the canonical height on elliptic curves. Math. Comp. 55 (1990), 723–743. https://doi.org/10.1090/S0025-5718-1990-1035944-5

[17] N. Bruin, M. Stoll. The Mordell–Weil sieve: proving non-existence of rational points on curves. LMS J. Comput. Math. 13 (2010), 272–306. https://doi.org/10.1112/S1461157009000187

[18] J. E. Cremona. eclib (mwrank), used via passagemath-eclib 10.8.12. https://github.com/JohnCremona/eclib

[19] J. E. Cremona, M. Prickett, S. Siksek. Height difference bounds for elliptic curves over number fields. J. Number Theory 116 (2006), 42–68. https://doi.org/10.1016/j.jnt.2005.03.001

[20] S. Siksek. Infinite descent on elliptic curves. Rocky Mountain J. Math. 25 (1995), 1501–1538. https://doi.org/10.1216/rmjm/1181072159

[21] A. Dujella. On Diophantine quintuples. Acta Arith. 81 (1997), 69–79. https://doi.org/10.4064/aa-81-1-69-79

# A height-complete census of small rational Diophantine tuples of all signs, with certified extension sets

## 1. Problem and contribution

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals such that $xy+1$ is a rational square for every pair. No septuple is known and none has been ruled out [1–5]. Earlier work builds sextuples from parametric constructions [4,5,6] or searches around known tuples [3,7,8]. The search in our previous paper [9] also starts from a corpus of known sextuples. This paper asks the reverse question: if a septuple has several elements of small height, what can be said about the others?

The height of a tuple is $\mathrm{ht}(X)=\max_{x\in X}\max(|\mathrm{num}\,x|,\mathrm{den}\,x)$, and the log height of a rational is $h(x)=\log\max(|\mathrm{num}\,x|,\mathrm{den}\,x)$. Signs are arbitrary. Following the usual convention, $xy+1=0$ counts as a square, so pairs with $xy=-1$ are allowed. Negation $X\mapsto -X$ preserves every condition and every height, so we keep one tuple of each pair $\{X,-X\}$.

Our results are below. $B$ is a natural-log height bound certified for each tuple, with explicit control of floating-point error (§3.5), and we quote its minimum over each run.

- **Theorem 1 (exhaustive enumeration).** Below height 2000 we list every pair, triple, quadruple, quintuple and sextuple, of all signs (Table 1). On the positive part, our counts agree exactly with Gibbs's published table [3] at every height up to 1500. Up to sign, there are exactly eight sextuples of height below 2000, and exactly one of height below 1000:
$$S_{455}=\left\{-\tfrac{455}{288},-\tfrac{243}{160},-\tfrac{56}{45},\tfrac{136}{405},\tfrac{77}{160},\tfrac{50}{81}\right\}.$$
There is no septuple of height below 2000.
- **Theorem 2 (quintuple census).** Every quintuple of height below 2000, 7890 up to sign, has its sixth-element set $\mathrm{Ext}_B(Q)$ determined within a bound $B(Q)\ge4246$. Every $\mathrm{Ext}_B(Q)$ has at most one element, so no two sixth elements $e,f$ with $ef+1$ a square exist within these bounds. Hence, if a septuple has five elements of height below 2000, then at least one of its other two elements has $h>4246$.
- **Theorem 3 (quadruple census).** Every quadruple of height below 500, 59611 up to sign, has its fifth-element set $\mathrm{Ext}_B(Q)$ determined within $B(Q)\ge3759$. In no case does the compatibility graph on $\mathrm{Ext}_B(Q)$ contain a triangle. Hence, if a septuple has four elements of height below 500, then at least one of its other three elements has $h>3759$. The edges of these graphs give 35 sextuples up to sign. The graphs of the run below height 100 have no edge, so if a sextuple contains a quadruple of height below 100, then one of its other two elements has $h>4655$.
- **Theorem 4 (no seventh element).** The three searches together give 77 sextuples up to sign. None has a seventh element $x$ with $h(x)\le28061$.
- **New objects.** $S_{455}$ has height below that of the smallest positive sextuple, Gibbs's $\{96/847,287/484,1209/700,129/28,147/25,847/4\}$ of height 1209 [3]. It is the smallest-height rational Diophantine sextuple of any sign. It and 48 further mixed-sign sextuples (§5) do not appear in the sources we checked [1,3,6–11].

Theorems 2 and 3 are not tied to any corpus. They cover every septuple with enough small elements, whatever its other elements are.

## 2. Related work and distinction

**Searches by height.** Gibbs [3] built his main base of triples by brute force up to height 1000, with a partial search up to 3000, and extended triples and quadruples using elliptic-curve methods. He found over 1000 positive sextuples and listed 551 of them up to height $10^7$. In addition ("Search Methodology" and "Counting m-tuples" in [3]), he ran a brute-force census intended to find all positive sextuples up to height 5000, and he tabulated the positive pairs, triples, quadruples, quintuples and sextuples below heights up to 5000; there are 14 sextuples below 5000. That census is a fixed-height completeness claim for positive tuples, reaching higher than ours (2000), and its counts are the benchmark we validate against. Our enumeration differs in covering all signs, which is where all the new sextuples lie. We also add certified extension sets, so our bounds reach far beyond the enumeration height. Dujella [6] built 26 mixed-sign sextuples from three constructions and showed that every sign pattern occurs. Dujella, Kazalicki and Petričević built families of sextuples with prescribed regular sub-quadruples and sub-quintuples [10], and sextuples containing a strong pair [11]. Dujella's online survey [1] collects all of these, together with the mixed-sign almost-septuples of Dujella–Kazalicki–Petričević. Apart from Gibbs's positive census, none of these works makes a completeness claim at a fixed height.

**Certified searches.** Zeng [7,8] runs a clique search over 6000 explicit triples, using truncated lists of multiples of fixed generators. Our previous paper [9] used a height-certified Mordell–Weil sieve around 759 known sextuples. It proved there is no seventh element up to $h\le2477$, and gave quintuple and quadruple censuses relative to those sextuples. The present paper uses the same sieve and certificates, but applies them to all tuples of small height rather than to a corpus. The quadruple census here covers about five times as many quadruples, none of them selected from known sextuples.

**Constrained families.** Other rStation papers study pairs with $ab=-1$ and strong or regular structure [12]. Our enumeration includes $ab=-1$ pairs. Among the small quadruples, 51 of the 59 with empty $\mathrm{Ext}$ below height 100 contain such a pair.

## 3. Methods

### 3.1 Exhaustive enumeration of pairs

Fix $a=p/q$ with $\gcd(p,q)=1$, $q>0$. Each $b\neq0$ with $ab+1=t^2$ is $b=(t^2-1)/a$ for some $t=u/v$, where $u\ge0$, $v\ge1$, $\gcd(u,v)=1$ and $u\neq v$. The case $t=0$, i.e. $u=0$ and $v=1$, gives $b=-1/a$. So
$$b=\frac{(u^2-v^2)\,q}{v^2\,p}.$$

**Lemma 4.** If $\mathrm{ht}(b)\le T$, then $v^2/\gcd(q,v^2)\le T$ and $|u^2-v^2|\le T\,|p|\gcd(q,v^2)/q$.

*Proof.* Put $A=u^2-v^2$, so $\gcd(A,v^2)=1$, and let $G=\gcd(Aq,v^2p)$. We have $\gcd(q,p)=1$ and $\gcd(A,v)=1$, so $G=\gcd(A,p)\cdot\gcd(q,v^2)$. Hence $\mathrm{den}\,b=v^2|p|/G$ is a multiple of $v^2/\gcd(q,v^2)$, which gives the first bound. Also $|\mathrm{num}\,b|=|A|q/G\ge|A|q/(|p|\gcd(q,v^2))$, which gives the second. $\square$

For every element $a$ of height at most $T$, the program enum_tuples.cpp runs over $v\le\sqrt{Tq}$ and over the $u$ allowed by Lemma 4. It reduces $b$, keeps it when $\mathrm{ht}(b)\le T$, and checks $ab+1$ exactly, as a square or as 0, in 128-bit integers. Triples, quadruples, quintuples and sextuples are then the cliques of the pair graph, listed by repeated intersection of sorted adjacency lists. Every clique is found exactly once, from its smallest vertex.

**Validation.**
- With positive elements only, our counts below height $T'$, for every $T'\le1500$ in Gibbs's table [3], agree exactly with his counts of pairs, triples, quadruples and quintuples. His table uses strict inequality. At $T'=2000$ see §4.1.
- For all signs, an independent pure-Python clique enumeration (bf_check.py) gives the same counts at heights below 50, 70 and 100.

### 3.2 Extension sets

For a tuple $Q$, let $\mathrm{Ext}(Q)$ be the set of rationals $x\notin Q$, $x\neq0$, such that $Q\cup\{x\}$ is a Diophantine tuple. We compute $\mathrm{Ext}_B(Q)=\{x\in\mathrm{Ext}(Q):h(x)\le B(Q)\}$ with the height-certified Mordell–Weil sieve of [9]. In outline:

1. Choose a triple $\tau\subset Q$ whose curve $E'_\tau:Y^2=(X+ab)(X+ac)(X+bc)$ has proven rank and the largest regulator. Proven rank means PARI ellrank [13] returns $r_{\rm lo}=r_{\rm hi}$ together with $r$ independent points.
2. Saturate the points with PARI, and later with eclib at every prime [14,15].
3. Write every $P\in P_0+2E'_\tau(\mathbb{Q})$ as $R+2\sum n_kG_k$, where $P_0=(0,abc)$ and $R\in P_0+2E_{\rm tors}$. By [16, Prop. 1], $x$ extends $\tau$ exactly when $abc\,x$ is the $X$-coordinate of such a point $P$.
4. Enumerate every $n$ with $n^\top Mn\le H$, where $M$ is the height matrix. This step runs in double precision (§3.5). The radius $H$ is chosen so that the ellipsoid holds a prescribed number of lattice points, the budget of the run.
5. Remove points at about 30 good primes, using discrete-log tables for the conditions $yx+1=\square$ for $y\in Q\setminus\tau$ [17].
6. Check every survivor exactly.

**Unresolved survivors.** The quadruple and quintuple runs used a cap of $3\cdot10^5$ on $\hat h(2\sum n_kG_k)$: a survivor above the cap is not evaluated, but recorded as unresolved. A row with an unresolved survivor would be incomplete. No run had one: the list is empty on all 67782 curves. The builders of the census tables and of Table 2 refuse any row where it is not, every published row records the count (0), and the checker of §3.4 recomputes it from the published data.

Lemmas 2 and 3 of [9] turn $H$ into a naive bound. Let $C=(2\sqrt{H'}-\max_R\sqrt{\hat h(R)})^2$, where $H'\le H$ is the certified radius of §3.5. Then every $x\in\mathrm{Ext}(Q)$ with
$$h(x)\le B(Q):=C-h(\sigma)-2\mu(E)-2.14$$
is found. Here $\sigma=abc\,D^2$ is the scale of the integral model, and $\mu$ is Silverman's constant [18]. The bounds quoted are $\lfloor B\rfloor$, computed by certify.py with the margins of §3.5.

Lemma 1 of [9] excludes $x$ with $(ax+1)(bx+1)(cx+1)=0$. Such an $x$ is $-1/y$ for some $y\in\tau$ and corresponds to a 2-torsion point. So for every tuple $Q$ and every $y\in Q$, we test $x=-1/y$ directly, and add it to $\mathrm{Ext}_B(Q)$ when all conditions hold (census_small.py). The two quintuple runs above height 300 and the sextuple runs used slack 1: they also report $x$ satisfying all but one condition, which serves as an internal consistency check.

### 3.3 Compatibility graphs

Put an edge between $x,y\in\mathrm{Ext}_B(Q)$ when $xy+1$ is a square, with 0 allowed.
- For a quadruple $Q$, an edge is a sextuple $Q\cup\{x,y\}$, and a triangle is a septuple.
- For a quintuple, every vertex is a sextuple, and an edge is a septuple.

**Lemma 5.** Let $Y$ be a septuple containing a quadruple $Q$ with $\mathrm{ht}(Q)<T$. If the graph on $\mathrm{Ext}_B(Q')$ has no triangle for every quadruple $Q'$ of height below $T$, then some $x\in Y\setminus Q$ has $h(x)>B(Q)$.

*Proof.* The three elements of $Y\setminus Q$ lie in $\mathrm{Ext}(Q)$ and are pairwise compatible. If all three had $h\le B(Q)$, they would form a triangle in $\mathrm{Ext}_B(Q)$. Since only one of $Q,-Q$ was processed, apply the argument to $-Y$ if necessary. $\square$

The quintuple version is the same, with an edge in place of a triangle.

### 3.4 Certificates and per-row records

- **Saturation.** eclib saturate with max_prime $=-1$ checks saturation at every prime up to the Cremona–Prickett–Siksek bound [14,15]. It must return index 1 on every basis.
- **Rank.** As an independent check of PARI's ranks, mwrank two-descent [14] was run on every census and sextuple curve (§4.5).
- **Per-row records.** Each row of the published tables (59611 quadruples, 7890 quintuples, 79 sextuple runs) records:
  - its run and triple, and the rank bounds $r_{\rm lo},r_{\rm hi}$;
  - the basis the sieve actually used, as the $X$-coordinate and the sign of $Y$ of each generator on the integral model (full points for the sextuple curves);
  - the radius $H$, the number of lattice points enumerated, and the certified $B$;
  - $\mathrm{Ext}_B$ and the number of near misses;
  - the eclib saturation index, the mwrank status and the number of unresolved survivors.

  The parameters of every run (point budget, slack, number of primes, cap) are in a separate table.
- **Replay of the three earliest runs.** The result files of the runs on quadruples below height 300 and on quintuples up to height 300 predate the storage of bases. For these 19656 curves we recovered a basis by repeating ellrank until the regulator agreed with the one stored by the run. The agreement was bitwise on all curves but one, where the two values differ in the last displayed digit, at relative size $5\cdot10^{-16}$. We then confirmed index 1 with eclib and reran the sieve with the original $H$. Equal regulators mean equal index in $E(\mathbb{Q})/E_{\rm tors}$, so the original and recovered bases span the same lattice. The ellipsoid $\hat h\le H$ does not depend on the basis, so the rerun should give the same output, up to rounding at the boundary. It did: hits, near misses and the number of lattice points agree on every curve. The rerun is the run that we certify and publish for these curves.
- **Deterministic checker.** check_census.py rebuilds each row from the published tables alone, with no randomness. It lifts the stored basis to the curve, then checks the following.
  - ellrank with these points returns $r_{\rm lo}=r_{\rm hi}=$ the number of points, and saturation at all primes below 100 leaves the regulator unchanged.
  - The radius recomputed from the run's budget equals the stored $H$.
  - The sieve, rerun with the run's parameters, leaves no unresolved survivor, enumerates the stored number of lattice points, and returns the stored $\mathrm{Ext}_B$ and number of near misses. Every element of $\mathrm{Ext}_B$ passes an exact check.
  - certify.py, applied to this rerun, gives a bound at least the stored $B$.
  - The compatibility graph has the edges and triangles we report.

  The checker can also export the rebuilt bases, so that eclib saturation and mwrank can be recomputed on exactly the published points.

### 3.5 Floating-point error control

The sieve enumerates the box $|n_k|\le N_k=\lfloor\sqrt{H\,(M_f^{-1})_{kk}}+10^{-9}\rfloor$. It keeps those $n$ with $q_f(n)\le H_{\rm tol}=H(1+10^{-9})+10^{-12}$. Here $M_f$ is the height matrix in double precision, $M_f^{-1}$ its floating-point inverse, and $q_f(n)$ the floating-point value of $n^\top M_fn$. Afterwards everything is exact: the prime sieve uses integer residues, and survivors are checked with rational points. Hence it suffices to find a radius $H'$ such that every integer vector with $n^\top Mn\le H'$, for the true height matrix $M$, lies in the box and passes the float test. certify.py does this for every curve.

1. **Replay.** It recomputes $M_f$ and $N$ from the stored basis exactly as the run did. It requires $\det M_f$ to equal the stored regulator bitwise, and $N$ to equal the stored box where stored.
2. **Accurate heights.** PARI computes the height matrix at 400 bits ($M_h$) and at 256 bits ($M_h'$). Put $\varepsilon=\max|M_f-M_h|+10\max|M_h-M_h'|+10^{-100}$. This bounds $\max_{ij}|M_f-M|_{ij}$. The term $\max|M_h-M_h'|$ overestimates the error of $M_h$ by many orders of magnitude; on every curve it is below $4\cdot10^{-75}$.
3. **Error of the float test.** Let $q=n^\top Mn$, $m=\min_iM_{ii}$, $s=\sum_i\sqrt{M_{ii}(M^{-1})_{ii}}$, $u=2^{-53}$ and $g=2r^2u/(1-2r^2u)$. Put $w_i=|n_i|\sqrt{M_{ii}}$. By Cauchy–Schwarz, $|n_i|\le\sqrt{q\,(M^{-1})_{ii}}$, so $\sum_iw_i\le s\sqrt q$ and $\sum_i|n_i|\le s\sqrt{q/m}$. Two estimates follow.
   - $|n^\top(M_f-M)n|\le\varepsilon(\sum_i|n_i|)^2\le q s^2\varepsilon/m$.
   - Each of the $r^2$ terms $n_iM_{f,ij}n_j$ passes through at most $r^2+1$ roundings, so the rounding error of $q_f$ is at most $g\sum_{ij}|n_i||M_{f,ij}||n_j|$. Using $|M_{ij}|\le\sqrt{M_{ii}M_{jj}}$, this is at most $g\,q s^2(1+\varepsilon/m)$.

   Hence $|q_f(n)-q|\le Kq$ with $K=s^2(\varepsilon/m+g(1+\varepsilon/m))$, and every $n$ with $q\le H_2:=H_{\rm tol}(1-10^{-15})/(1+K)$ passes the test.
4. **Box.** Again by Cauchy–Schwarz, every $n$ with $q<H_{\rm box}:=\min_k(N_k+1)^2/(M^{-1})_{kk}$ lies in the box.
5. **Certified radius.** Put $H'=\min(H,H_2,H_{\rm box})(1-10^{-12})$. In the formula for $B$ we use $H'$, the torsion heights at 400 bits plus ten times their 400/256-bit difference, and a final margin of $10^{-9}$.

The quantities $m$, $s$ and $(M^{-1})_{kk}$ are computed from $M_h$ in 100-digit arithmetic and inflated by $10^{-20}$. Over all curves, $\varepsilon\le2.7\cdot10^{-15}$, dominated by the double-precision rounding of $M_f$, and $K\le2.72\cdot10^{-13}$. So $H_2>H$ and $H_{\rm box}>H$ on every curve, and $H'=H(1-10^{-12})$. Because $H_{\rm box}$ is computed from the box $N$ that was actually enumerated, the floating-point inverse and the flooring that produced $N$ need no separate analysis. The original submission used the same formula with $H$ in place of $H'$ and without margins. Against those values, every minimum in Theorems 2–4 is unchanged, and one entry of Table 2 drops by 7 out of $6.7\cdot10^{12}$.

The only input not covered by this analysis is the correctness of PARI's multiprecision height pairings at 400 bits. Every $\lfloor B\rfloor$ would be unchanged even if $\varepsilon$ were larger by $4.4\cdot10^{-11}$.

## 4. Results

### 4.1 Theorem 1: enumeration

Table 1 gives the number of tuples of height strictly below $T'$. "All signs" counts $X$ and $-X$ separately and includes pairs with $xy=-1$. The positive columns agree with Gibbs's table [3] entry by entry up to $T'=1500$; the row at 2000 is discussed below.

| $T'$ | positive: pairs | triples | quads | quints | all signs: pairs | triples | quads | quints | sextuples |
|---|---|---|---|---|---|---|---|---|---|
| 10 | 74 | 6 | 0 | 0 | 311 | 58 | 0 | 0 | 0 |
| 30 | 1538 | 235 | 7 | 0 | 5717 | 1432 | 69 | 0 | 0 |
| 100 | 34304 | 7245 | 404 | 4 | 117353 | 36296 | 2801 | 28 | 0 |
| 300 | 514683 | 113689 | 6274 | 49 | 1721395 | 534902 | 38533 | 380 | 0 |
| 500 | 1729172 | 376596 | 20239 | 168 | 5710943 | 1729952 | 119219 | 1182 | 2 |
| 1000 | 9089069 | 1890965 | 90107 | 728 | 29818997 | 8553762 | 513147 | 4508 | 2 |
| 1500 | 23499330 | 4722097 | 210859 | 1584 | 76597913 | 21149734 | 1182930 | 9532 | 10 |
| 2000 | 46188859 | 8979016 | 375183 | 2648 | 150180957 | 40063784 | 2089849 | 15780 | 16 |

The positive sextuple counts are 0, 3 and 5 below 1000, 1500 and 2000, as in [3]; the smallest has height 1209. The all-sign sextuples below 2000 are $\pm$ the eight sextuples of heights 455, 1176, 1209, 1260, 1463, 1760, 1936 and 1953 in Table 2. Five are Gibbs's #1–#5 [3]; $S_{455}$, $S_{1176}$ and $S_{1936}$ have mixed signs and are new. No septuple occurs. The run to height 2000 indexes all 4866350 nonzero rationals of height at most 2000 and took about three hours on one core.

**Gibbs's row at 2000.** Gibbs [3] lists 357103 quadruples and 2640 quintuples below 2000, against our 375183 and 2648. Every other entry of his table up to 2000 agrees with ours, including pairs, triples and sextuples at 2000 and all counts at 1500. We re-checked each of our 375183 positive quadruples and 2648 positive quintuples with an independent exact test: the elements are distinct, the height is below 2000, and all six or ten products $xy+1$ are squares. The script quad_rows.py regenerates both lists from the enumeration output, and the supplement gives their SHA-256 digests. We do not know the cause of the difference; since pairs and triples agree exactly at 2000, it is not a height-convention issue.

Seven quadruples below 2000 equal their own negatives: $\{-1,-r,r,1\}$ with $r=24/25$, $120/169$, $240/289$, $336/625$, $840/841$, $840/1369$, $720/1681$; three of them have height below 500. Each has $r=2mn/(m^2+n^2)$ with $m^2+n^2$ a square, so $1\pm r=(m\pm n)^2/(m^2+n^2)$ and $1-r^2$ are all squares. This is why some all-sign quadruple counts are odd. Counting up to sign, there are $(119219+3)/2=59611$ quadruples below 500, and $4508/2=2254$ and $15780/2=7890$ quintuples below 1000 and 2000.

### 4.2 Theorem 2: quintuple census

We took every quintuple of height below 2000 from the enumeration, giving 7890 sign classes in three runs by height. The first run processed both members $X$ and $-X$ of each class. Their extension sets satisfy $\mathrm{Ext}(-X)=-\mathrm{Ext}(X)$ in all 194 classes, and the table reports the canonical member $\min(X,-X)$. The union of the three run inputs equals the set of sign classes in the enumeration output exactly. Each run enumerated about $10^6$ lattice points per quintuple.

| run | quintuples | rank 1 / 2 / 3 / 4 | $\lvert\mathrm{Ext}_B\rvert=0$ / 1 | edges | min $B$ | median $B$ |
|---|---|---|---|---|---|---|
| $\mathrm{ht}\le300$ | 194 | 8 / 154 / 32 / 0 | 193 / 1 | 0 | 26452 | 1662957 |
| $300<\mathrm{ht}<1000$ | 2060 | 27 / 1122 / 906 / 5 | 2041 / 19 | 0 | 4260 | 1460953 |
| $1000\le\mathrm{ht}<2000$ | 5636 | 41 / 2195 / 3323 / 77 | 5560 / 76 | 0 | 4246 | 54176 |

No quintuple has two or more sixth elements, so no graph has an edge. The bound 4246 of Theorem 2 is the minimum of $B$ over the three runs. The 96 quintuple classes with one sixth element give 56 distinct sextuples up to sign; a sextuple appears once for each of its sub-quintuples below 2000. There were no degenerate values $x=-1/y$. The two runs above height 300 used slack 1 and reported 16854 values $x$ that extend the quintuple's sieve triple and satisfy exactly one of the other two conditions. They are near misses for the sixth element, not candidates. The census table gives their number for each quintuple, and the checker of §3.4 recomputes it.

**Corollary (almost septuples).** An almost septuple is a set of seven rationals for which 20 of the 21 products plus one are squares [1,19]. If $\{e,f\}$ is the failing pair, the other five elements form a quintuple $Q$ with $e,f\in\mathrm{Ext}(Q)$. Since $|\mathrm{Ext}_B(Q)|\le1$ for every quintuple below height 2000, every almost septuple whose five complete elements have height below 2000 has $h(e)>4246$ or $h(f)>4246$. This is consistent with the 22 almost septuples collected in [9,19]: the complete quintuples of these examples have heights between 4032 and about $6.5\cdot10^7$, all above 2000.

### 4.3 Theorem 3: quadruple census

We took every quadruple of height below 500 from the enumeration, one per sign class: 59611 quadruples in three runs. Again the union of the inputs equals the enumeration output.

| run | quadruples | rank 1 / 2 / 3 / 4 / 5 | $\lvert\mathrm{Ext}_B\rvert=0$ / 1 / 2 / 3 / 4 | 1-edge graphs | min $B$ |
|---|---|---|---|---|---|
| $\mathrm{ht}<100$ | 1401 | 297 / 1059 / 45 / 0 / 0 | 59 / 1078 / 249 / 15 / 0 | 0 | 4655 |
| $100\le\mathrm{ht}<300$ | 17867 | 1182 / 13649 / 2999 / 37 / 0 | 225 / 13654 / 3590 / 388 / 10 | 20 | 3759 |
| $300\le\mathrm{ht}<500$ | 40343 | 1552 / 29155 / 9401 / 233 / 2 | 261 / 31157 / 7983 / 899 / 43 | 37 | 3798 |

Every graph has at most one edge, so none has a triangle. The 57 edges give 35 sextuples up to sign. Ten fifth elements are degenerate values $-1/y$ (2 and 8 in the last two runs); none of them lies on an edge. The runs used $10^5$ lattice points per quadruple below height 100 and $10^6$ above. In the last run, eight quadruples, six of rank 4 and two of rank 5, had $B<3759$; we reran them with $2\cdot10^7$ points and obtained the same extension sets, now with $B\ge4679$. The minimum over the three runs is therefore 3759, attained in the second run.

Most extensions are regular. A quadruple $\{a,b,c,d\}$ with $abcd\neq1$ has the two regular fifth elements $e_\pm$ of [20], and for a regular quadruple $e_+e_-=0$, so one of them is 0 [20, Prop. 2]. Of the 59611 quadruples, 48137 are regular (some element is $d_\pm$ of the other three). Of these, 45416 have exactly one fifth element, the nonzero regular one. Among the 11474 irregular quadruples, 9673 have exactly the two regular fifth elements. Every extension set contains all nonzero regular fifth elements not in $Q$, as it must; this is a check on the sieve. Only 3511 of the 59611 extension sets contain an irregular fifth element, and 545 are empty. Of the 59 empty sets below height 100, 51 belong to quadruples with a pair $ab=-1$.

**Recall.** Our previous paper [9] gathered 759 sextuples from the literature and its own searches. Of these, 27 have a sub-quadruple below 500 or a sub-quintuple below 2000. All 27 are among the sextuples found here.

### 4.4 Theorem 4: seventh elements

The quadruple census gives 35 sextuples, and the quintuple census 56, with 14 in both. Together with the eight sextuples below height 2000, which the two censuses already contain, this gives 77 sextuples up to sign. We ran the sieve of §3.2 on each, testing seventh elements, with $2\cdot10^6$ lattice points and slack 1. Two sextuples of rank 4 had $B<30000$ and were rerun with $2\cdot10^7$ points. No run found a seventh element, a near miss (a value satisfying five of the six conditions), or a degenerate value. The minimum of $B$ over the 77 sextuples is 28061. The per-sextuple rank and $B$ are in Table 2. The supplement keeps all 79 run rows. For the two rerun sextuples, Table 2 uses the rerun's larger $B$. The checker's minimum over all 79 rows, 8531, belongs to a superseded $2\cdot10^6$-point run (rerun to 28061).

### 4.5 Certificates

All ranks used are proven by ellrank ($r_{\rm lo}=r_{\rm hi}$). No curve has an unresolved survivor.

| run | curves | eclib saturation, index 1 | mwrank rank = PARI rank (certified) | uncertified, consistent | unresolved survivors | max $K$ |
|---|---|---|---|---|---|---|
| quad $<100$ | 1401 | 1401 | 1401 | 0 | 0 | $2.8\cdot10^{-14}$ |
| quad $100$–$300$ | 17867 | 17867 | 17806 | 61 | 0 | $8.8\cdot10^{-14}$ |
| quad $300$–$500$ | 40343 + 8 reruns | 40351 | 40007 | 344 | 0 | $2.7\cdot10^{-13}$ |
| quint $\le300$ | 388 (both signs) | 388 | 388 | 0 | 0 | $2.6\cdot10^{-14}$ |
| quint $300$–$1000$ | 2060 | 2060 | 2057 | 3 | 0 | $8.2\cdot10^{-14}$ |
| quint $1000$–$2000$ | 5636 | 5636 | 5619 | 17 | 0 | $9.1\cdot10^{-14}$ |
| sextuples | 79 (77 + 2 reruns) | 79 | 79 | 0 | 0 | $8.8\cdot10^{-14}$ |
| total | 67782 | 67782 | 67357 | 425 | 0 | $2.7\cdot10^{-13}$ |

$K$ is the relative error bound of the float test (§3.5). On every curve the replay of §3.5 reproduced the run's regulator bitwise, and the box was never the binding constraint.

"Uncertified, consistent" means mwrank's two-descent returned a lower bound equal to PARI's rank but could not certify the upper bound within its default search limits (first and second limits 20 and 8). mwrank never returned a rank different from PARI's, never timed out and never failed. Raising the limits to 30 and 12 took over four minutes per curve on our shared machine without certifying the first two such curves, so we did not pursue it. The completeness of every extension set needs only PARI's proven rank and eclib's saturation; mwrank is an independent check.

## 5. New objects

### 5.1 The sextuple $S_{455}$

$$S_{455}=\left\{-\tfrac{455}{288},-\tfrac{243}{160},-\tfrac{56}{45},\tfrac{136}{405},\tfrac{77}{160},\tfrac{50}{81}\right\}.$$

The 15 square roots, in the order of the pairs $(x_i,x_j)$, $i<j$, are
$$\tfrac{59}{32},\tfrac{31}{18},\tfrac{37}{54},\tfrac{47}{96},\tfrac{17}{108},\tfrac{17}{10},\tfrac{7}{10},\tfrac{83}{160},\tfrac14,\tfrac{103}{135},\tfrac{19}{30},\tfrac{13}{27},\tfrac{97}{90},\tfrac{89}{81},\tfrac{41}{36}.$$

By Theorem 1, $\pm S_{455}$ are the only sextuples of height below 1000. Up to sign, $S_{455}$ is therefore the unique sextuple of minimal height, and every other sextuple has height at least 1000. The smallest positive sextuple has height 1209 [3]. The smallest sextuple in Dujella's mixed-sign list [6] is $\{31/84,9/7,49/12,160/21,-455/3468,7200/2023\}$, of height 7200.

$S_{455}$ contains three regular sub-quadruples, i.e. sets $\{a,b,c,d\}$ with $d=a+b+c+2abc\pm2rst$ [16], and one regular sub-quintuple [20]. Its smallest sub-quadruple has height 243, and it was found independently by the enumeration and by the quadruple census.

### 5.2 All sextuples found

Table 2 lists the 77 sextuples, up to sign, found by the three searches. They are all sextuples of height below 2000, together with every sextuple that has a sub-quadruple of height below 500 or a sub-quintuple of height below 2000 and whose remaining elements lie within the bounds $B$ of Theorems 3 and 2.
- "neg" is the number of negative elements in the sign class shown.
- "min ht" gives the smallest height of a sub-quadruple and of a sub-quintuple.
- "reg." counts the distinct regular sub-quadruples and sub-quintuples.
- "rank" and $B$ refer to the curve of the seventh-element sieve (§4.4).
- "source" records where we found the sextuple in the literature. Gibbs numbers refer to his list of 551 [3]; [21] is a paper of Dujella and Mikić.

| ht | sextuple (sign class with fewer negatives) | neg | min ht sub-quad / sub-quint | reg. quads / quints | rank | $B$ (7th) | source |
|---|---|---|---|---|---|---|---|
| 455 | $\{-\tfrac{50}{81},-\tfrac{77}{160},-\tfrac{136}{405},\tfrac{56}{45},\tfrac{243}{160},\tfrac{455}{288}\}$ | 3 | 243 / 405 | 3 / 1 | 2 | 3400419 | new |
| 1176 | $\{-\tfrac{128}{735},-\tfrac{185}{1176},\tfrac{299}{120},\tfrac{954}{245},\tfrac{539}{120},\tfrac{45}{8}\}$ | 2 | 735 / 954 | 3 / 1 | 3 | 56812 | new |
| 1209 | $\{\tfrac{96}{847},\tfrac{287}{484},\tfrac{1209}{700},\tfrac{129}{28},\tfrac{147}{25},\tfrac{847}{4}\}$ | 0 | 847 / 847 | 2 / 2 | 3 | 59595 | Gibbs #1 [3] |
| 1260 | $\{\tfrac{221}{1260},\tfrac{175}{324},\tfrac{203}{180},\tfrac{81}{35},\tfrac{265}{28},\tfrac{1120}{9}\}$ | 0 | 324 / 1120 | 2 / 1 | 3 | 44692 | Gibbs #2 [3] |
| 1463 | $\{\tfrac{225}{1156},\tfrac{47}{60},\tfrac{287}{240},\tfrac{225}{64},\tfrac{1463}{60},\tfrac{512}{15}\}$ | 0 | 512 / 1156 | 1 / 1 | 3 | 67603 | Gibbs #3 [3] |
| 1760 | $\{\tfrac{39}{1760},\tfrac{136}{165},\tfrac{275}{96},\tfrac{672}{55},\tfrac{1010}{33},1320\}$ | 0 | 1010 / 1320 | 2 / 2 | 2 | 2350690 | Gibbs #4 [3] |
| 1936 | $\{-\tfrac{63}{605},-\tfrac{7}{80},\tfrac{1725}{1936},\tfrac{1200}{361},\tfrac{697}{80},\tfrac{48}{5}\}$ | 2 | 697 / 1200 | 1 / 1 | 3 | 31262 | new |
| 1953 | $\{\tfrac{32}{525},\tfrac{224}{867},\tfrac{53}{84},\tfrac{273}{100},\tfrac{75}{7},\tfrac{1953}{100}\}$ | 0 | 525 / 867 | 1 / 2 | 3 | 46866 | Gibbs #5 [3] |
| 2275 | $\{\tfrac{377}{1260},\tfrac{119}{180},\tfrac{297}{140},\tfrac{992}{315},\tfrac{175}{9},\tfrac{2275}{4}\}$ | 0 | 992 / 1260 | 2 / 1 | 3 | 55980 | Gibbs #6 [3] |
| 2760 | $\{-\tfrac{2431}{2760},-\tfrac{1152}{1495},\tfrac{325}{552},\tfrac{1219}{1560},\tfrac{1825}{1794},\tfrac{1771}{1560}\}$ | 2 | 1771 / 1825 | 2 / 1 | 3 | 47332 | new |
| 2940 | $\{-\tfrac{851}{2940},-\tfrac{11}{60},\tfrac{288}{245},\tfrac{288}{125},\tfrac{1625}{588},\tfrac{49}{15}\}$ | 2 | 288 / 1625 | 2 / 2 | 3 | 45204 | new |
| 3213 | $\{\tfrac{5}{36},\tfrac{665}{1521},\tfrac{5}{4},\tfrac{32}{9},\tfrac{3213}{676},\tfrac{189}{4}\}$ | 0 | 189 / 1521 | 2 / 2 | 2 | 3167946 | Gibbs #7 [3], [6] |
| 3240 | $\{-\tfrac{64}{405},-\tfrac{407}{3240},\tfrac{56}{45},\tfrac{125}{72},\tfrac{2673}{1000},\tfrac{26}{5}\}$ | 2 | 405 / 2673 | 2 / 2 | 3 | 64664 | new |
| 3380 | $\{-\tfrac{1239}{3380},-\tfrac{33}{140},\tfrac{32}{35},\tfrac{2175}{1183},\tfrac{49}{20},\tfrac{75}{28}\}$ | 2 | 140 / 2175 | 2 / 2 | 2 | 3169295 | new |
| 3481 | $\{-\tfrac{910}{1083},-\tfrac{16}{21},-\tfrac{1680}{3481},\tfrac{624}{847},\tfrac{15}{14},\tfrac{7}{6}\}$ | 3 | 847 / 1083 | 0 / 3 | 1 | 6655048403551 | [1] |
| 4116 | $\{\tfrac{925}{4116},\tfrac{99}{140},\tfrac{25}{21},\tfrac{119}{60},\tfrac{608}{105},\tfrac{693}{20}\}$ | 0 | 608 / 693 | 2 / 1 | 3 | 49869 | Gibbs #10 [3] |
| 4116 | $\{\tfrac{12}{91},\tfrac{429}{1372},\tfrac{160}{91},\tfrac{1881}{364},\tfrac{221}{28},\tfrac{4116}{13}\}$ | 0 | 1372 / 1881 | 2 / 2 | 3 | 64109 | Gibbs #11 [3] |
| 4420 | $\{\tfrac{9}{44},\tfrac{91}{132},\tfrac{4420}{3993},\tfrac{60}{11},\tfrac{44}{3},\tfrac{1265}{12}\}$ | 0 | 132 / 1265 | 3 / 1 | 3 | 39325 | Gibbs #13 [3] |
| 4489 | $\{-\tfrac{21}{32},-\tfrac{2730}{4489},-\tfrac{115}{224},\tfrac{8}{7},\tfrac{480}{343},\tfrac{333}{224}\}$ | 3 | 333 / 480 | 2 / 1 | 2 | 3446505 | new |
| 5324 | $\{-\tfrac{288}{385},-\tfrac{3675}{5324},-\tfrac{209}{420},\tfrac{33}{35},\tfrac{1376}{1155},\tfrac{175}{132}\}$ | 3 | 420 / 1376 | 3 / 2 | 3 | 51808 | new |
| 5600 | $\{-\tfrac{4743}{5600},-\tfrac{125}{168},\tfrac{153}{350},\tfrac{512}{525},\tfrac{637}{600},\tfrac{1813}{1536}\}$ | 2 | 637 / 1813 | 3 / 1 | 3 | 60512 | new |
| 5643 | $\{-\tfrac{40}{117},-\tfrac{481}{1440},\tfrac{54}{65},\tfrac{715}{288},\tfrac{5643}{2080},\tfrac{184}{65}\}$ | 2 | 715 / 1440 | 4 / 1 | 3 | 41096 | new |
| 6080 | $\{-\tfrac{27}{1156},\tfrac{5}{4},\tfrac{6080}{2601},\tfrac{65}{9},\tfrac{533}{36},\tfrac{224}{9}\}$ | 1 | 533 / 1156 | 2 / 1 | 3 | 61563 | new |
| 6655 | $\{-\tfrac{35}{66},-\tfrac{3072}{6655},-\tfrac{77}{480},\tfrac{165}{128},\tfrac{445}{264},\tfrac{819}{440}\}$ | 3 | 480 / 819 | 3 / 2 | 3 | 47896 | new |
| 6889 | $\{\tfrac{3}{80},\tfrac{2220}{6889},\tfrac{55}{16},\tfrac{28}{5},\tfrac{1683}{80},1680\}$ | 0 | 1680 / 1683 | 2 / 1 | 3 | 70133 | Gibbs #19 [3] |
| 7084 | $\{-\tfrac{36}{175},-\tfrac{47}{336},\tfrac{625}{336},\tfrac{1197}{400},\tfrac{7084}{1875},\tfrac{364}{75}\}$ | 2 | 625 / 1197 | 3 / 1 | 3 | 63239 | new |
| 7200 | $\{-\tfrac{455}{3468},\tfrac{31}{84},\tfrac{9}{7},\tfrac{7200}{2023},\tfrac{49}{12},\tfrac{160}{21}\}$ | 1 | 160 / 3468 | 2 / 2 | 2 | 3361336 | [1,6] |
| 7680 | $\{-\tfrac{87}{136},-\tfrac{15}{34},\tfrac{17}{32},\tfrac{561}{512},\tfrac{185}{136},\tfrac{7680}{4913}\}$ | 2 | 185 / 561 | 3 / 2 | 3 | 53565 | new |
| 7749 | $\{\tfrac{225}{1856},\tfrac{475}{1392},\tfrac{512}{435},\tfrac{667}{240},\tfrac{7749}{580},\tfrac{1363}{60}\}$ | 0 | 1392 / 1856 | 2 / 2 | 3 | 61788 | Gibbs #22 [3] |
| 8184 | $\{\tfrac{6}{125},\tfrac{1144}{1445},\tfrac{483}{160},\tfrac{56}{5},\tfrac{375}{32},\tfrac{8184}{5}\}$ | 0 | 483 / 1445 | 1 / 1 | 3 | 45407 | Gibbs #24 [3] |
| 8437 | $\{-\tfrac{63}{400},\tfrac{1428}{1849},\tfrac{8437}{8400},\tfrac{91}{48},\tfrac{100}{21},\tfrac{1104}{175}\}$ | 1 | 1104 / 1849 | 3 / 1 | 3 | 60608 | new |
| 9317 | $\{\tfrac{1860}{9317},\tfrac{115}{308},\tfrac{28}{55},\tfrac{777}{220},\tfrac{396}{35},\tfrac{825}{28}\}$ | 0 | 777 / 825 | 3 / 1 | 3 | 54056 | Gibbs #30 [3] |
| 10201 | $\{-\tfrac{1128}{1715},-\tfrac{544}{945},-\tfrac{4200}{10201},\tfrac{33}{35},\tfrac{280}{243},\tfrac{265}{189}\}$ | 3 | 945 / 1715 | 2 / 1 | 3 | 59259 | new |
| 10535 | $\{-\tfrac{605}{1344},-\tfrac{512}{1155},\tfrac{143}{1680},\tfrac{931}{660},\tfrac{675}{308},\tfrac{10535}{4752}\}$ | 2 | 1344 / 1680 | 2 / 2 | 3 | 66076 | new |
| 11236 | $\{-\tfrac{43}{324},\tfrac{3773}{11236},\tfrac{713}{441},\tfrac{1088}{441},\tfrac{1053}{196},\tfrac{608}{81}\}$ | 1 | 1053 / 1088 | 2 / 1 | 3 | 65930 | new |
| 11528 | $\{\tfrac{189}{800},\tfrac{8}{9},\tfrac{378}{289},\tfrac{608}{225},\tfrac{325}{32},\tfrac{11528}{225}\}$ | 0 | 608 / 800 | 2 / 1 | 3 | 56493 | Gibbs #37 [3] |
| 14805 | $\{\tfrac{32}{405},\tfrac{205}{324},\tfrac{2080}{729},\tfrac{14805}{3364},\tfrac{153}{20},\tfrac{77}{5}\}$ | 0 | 405 / 2080 | 2 / 1 | 3 | 52109 | Gibbs #44 [3] |
| 16275 | $\{\tfrac{3}{200},\tfrac{174}{169},\tfrac{27}{8},\tfrac{136}{25},\tfrac{16275}{1352},200\}$ | 0 | 200 / 200 | 2 / 2 | 2 | 3446951 | Gibbs #46 [3] |
| 16761 | $\{-\tfrac{75}{128},-\tfrac{128}{245},\tfrac{1605}{2312},\tfrac{49}{40},\tfrac{16761}{11560},\tfrac{165}{98}\}$ | 2 | 245 / 2312 | 2 / 2 | 3 | 70396 | new |
| 16800 | $\{\tfrac{77}{380},\tfrac{57}{55},\tfrac{1632}{1045},\tfrac{957}{380},\tfrac{893}{220},\tfrac{16800}{209}\}$ | 0 | 957 / 1632 | 1 / 1 | 3 | 49120 | Gibbs #47 [3] |
| 19965 | $\{\tfrac{6496}{19965},\tfrac{35}{33},\tfrac{215}{132},\tfrac{209}{60},\tfrac{1953}{220},\tfrac{1683}{20}\}$ | 0 | 1683 / 1953 | 2 / 1 | 3 | 70591 | Gibbs #56 [3] |
| 21483 | $\{-\tfrac{2240}{9537},\tfrac{45}{44},\tfrac{224}{165},\tfrac{121}{60},\tfrac{115}{33},\tfrac{21483}{5780}\}$ | 1 | 224 / 9537 | 2 / 2 | 3 | 69625 | new |
| 22295 | $\{-\tfrac{325}{336},-\tfrac{18768}{22295},-\tfrac{836}{1365},\tfrac{112}{195},\tfrac{429}{560},\tfrac{1071}{1040}\}$ | 3 | 1071 / 1365 | 3 / 1 | 3 | 46380 | new |
| 25600 | $\{-\tfrac{175}{234},-\tfrac{347}{520},-\tfrac{351}{640},\tfrac{1729}{1440},\tfrac{25600}{19773},\tfrac{693}{520}\}$ | 3 | 693 / 1729 | 3 / 2 | 3 | 67152 | new |
| 30420 | $\{-\tfrac{621}{980},-\tfrac{101}{180},\tfrac{22099}{30420},\tfrac{500}{441},\tfrac{1044}{845},\tfrac{196}{125}\}$ | 2 | 980 / 1044 | 2 / 2 | 3 | 81637 | new |
| 30723 | $\{-\tfrac{11}{140},\tfrac{165}{1183},\tfrac{25}{28},\tfrac{96}{35},\tfrac{147}{20},\tfrac{30723}{3380}\}$ | 1 | 147 / 1183 | 2 / 2 | 2 | 3411673 | [6] |
| 32025 | $\{-\tfrac{1287}{13448},\tfrac{33}{200},\tfrac{25}{32},\tfrac{57}{8},\tfrac{32025}{3362},\tfrac{256}{25}\}$ | 1 | 256 / 13448 | 2 / 2 | 3 | 74665 | new |
| 33099 | $\{-\tfrac{21}{115},\tfrac{253}{320},\tfrac{375}{368},\tfrac{6144}{2875},\tfrac{33099}{7360},\tfrac{437}{80}\}$ | 1 | 437 / 6144 | 2 / 2 | 3 | 75993 | new |
| 33600 | $\{-\tfrac{224}{17405},\tfrac{21}{20},\tfrac{33600}{17161},\tfrac{41}{5},\tfrac{429}{20},\tfrac{225}{4}\}$ | 1 | 429 / 17405 | 0 / 2 | 3 | 41982 | new |
| 35912 | $\{-\tfrac{40}{217},-\tfrac{5859}{35912},\tfrac{704}{1953},\tfrac{1147}{504},\tfrac{1022}{279},\tfrac{1323}{248}\}$ | 2 | 1323 / 1953 | 1 / 2 | 3 | 49898 | new |
| 42315 | $\{-\tfrac{65}{168},-\tfrac{546}{1681},\tfrac{296}{273},\tfrac{42315}{27848},\tfrac{192}{91},\tfrac{805}{312}\}$ | 2 | 805 / 1681 | 0 / 2 | 3 | 52013 | new |
| 46389 | $\{-\tfrac{299}{840},-\tfrac{225}{728},\tfrac{28600}{46389},\tfrac{392}{195},\tfrac{663}{280},\tfrac{518}{195}\}$ | 2 | 728 / 840 | 2 / 1 | 3 | 51001 | new |
| 48125 | $\{-\tfrac{1332}{1925},-\tfrac{31872}{48125},-\tfrac{625}{1232},\tfrac{132}{175},\tfrac{539}{400},\tfrac{1767}{1232}\}$ | 3 | 1767 / 1925 | 3 / 1 | 2 | 3702674 | new |
| 48668 | $\{-\tfrac{42315}{48668},-\tfrac{99}{115},-\tfrac{35}{92},\tfrac{96}{115},\tfrac{12075}{11236},\tfrac{23}{20}\}$ | 3 | 115 / 12075 | 2 / 1 | 3 | 52600 | new |
| 68400 | $\{-\tfrac{1}{15},\tfrac{2576}{27735},\tfrac{68400}{54289},\tfrac{495}{289},\tfrac{104}{15},\tfrac{40}{3}\}$ | 1 | 495 / 27735 | 0 / 2 | 3 | 60034 | new |
| 77952 | $\{-\tfrac{260}{1701},-\tfrac{35}{432},\tfrac{57}{112},\tfrac{561}{112},\tfrac{77952}{12769},\tfrac{1540}{243}\}$ | 2 | 1540 / 1701 | 1 / 1 | 4 | 28061 | new |
| 81608 | $\{-\tfrac{1}{42},\tfrac{50715}{81608},\tfrac{665}{384},\tfrac{161}{24},\tfrac{477}{56},\tfrac{640}{21}\}$ | 1 | 640 / 665 | 0 / 2 | 3 | 52271 | new |
| 85169 | $\{-\tfrac{175}{184},-\tfrac{76800}{85169},-\tfrac{851}{1120},\tfrac{483}{640},\tfrac{861}{920},\tfrac{1683}{1610}\}$ | 3 | 1120 / 1683 | 3 / 2 | 3 | 72888 | new |
| 94249 | $\{-\tfrac{13}{34},-\tfrac{102}{361},\tfrac{62832}{94249},\tfrac{32}{17},\tfrac{50592}{26569},\tfrac{87}{34}\}$ | 2 | 361 / 50592 | 0 / 2 | 3 | 58369 | new |
| 98371 | $\{\tfrac{8}{27},\tfrac{19}{24},\tfrac{2318}{1875},\tfrac{297}{200},\tfrac{98371}{15000},\tfrac{200}{3}\}$ | 0 | 297 / 2318 | 2 / 2 | 3 | 79091 | Gibbs #133 [3] |
| 112875 | $\{\tfrac{16}{275},\tfrac{179}{1859},\tfrac{561}{400},\tfrac{112875}{29744},\tfrac{144}{11},\tfrac{825}{16}\}$ | 0 | 825 / 1859 | 2 / 2 | 3 | 84777 | Gibbs #147 [3] |
| 167200 | $\{-\tfrac{2870}{38307},\tfrac{35}{54},\tfrac{167200}{131061},\tfrac{176}{105},\tfrac{91}{30},\tfrac{432}{35}\}$ | 1 | 432 / 38307 | 0 / 2 | 3 | 49233 | new |
| 177531 | $\{-\tfrac{74025}{93092},-\tfrac{187}{300},\tfrac{17}{75},\tfrac{128800}{177531},\tfrac{63}{68},\tfrac{64}{51}\}$ | 2 | 300 / 93092 | 0 / 2 | 3 | 54642 | new |
| 180873 | $\{\tfrac{11}{192},\tfrac{35}{192},\tfrac{155}{27},\tfrac{512}{27},\tfrac{1235}{48},\tfrac{180873}{16}\}$ | 0 | 512 / 1235 | 2 / 1 | 3 | 78322 | Gibbs #175 [3], [6,7,8,10,11,21] |
| 222605 | $\{-\tfrac{37}{40},-\tfrac{1209}{1480},-\tfrac{88}{185},\tfrac{30}{37},\tfrac{219336}{222605},\tfrac{315}{296}\}$ | 3 | 315 / 1480 | 3 / 0 | 3 | 62212 | new |
| 225225 | $\{\tfrac{1}{100},\tfrac{89001}{163216},\tfrac{201}{100},\tfrac{225225}{40804},\tfrac{425}{16},384\}$ | 0 | 425 / 163216 | 2 / 2 | 3 | 96738 | Gibbs #195 [3] |
| 277123 | $\{-\tfrac{325}{456},-\tfrac{1216}{1755},-\tfrac{440}{741},\tfrac{277123}{266760},\tfrac{266}{195},\tfrac{1053}{760}\}$ | 3 | 1053 / 1755 | 3 / 2 | 3 | 57576 | new |
| 300288 | $\{-\tfrac{165}{224},-\tfrac{41}{70},-\tfrac{7}{40},\tfrac{5376}{4805},\tfrac{300288}{241115},\tfrac{75}{56}\}$ | 3 | 224 / 5376 | 0 / 2 | 2 | 3332834 | [1,6] |
| 552049 | $\{-\tfrac{108}{125},-\tfrac{115}{144},\tfrac{560}{1089},\tfrac{431460}{552049},\tfrac{73}{80},\tfrac{52}{45}\}$ | 2 | 144 / 1089 | 0 / 2 | 3 | 52173 | new |
| 747003 | $\{-\tfrac{45}{136},-\tfrac{231880}{747003},-\tfrac{55}{408},\tfrac{783}{680},\tfrac{34}{15},\tfrac{728}{255}\}$ | 3 | 728 / 783 | 3 / 0 | 3 | 55248 | new |
| 987657 | $\{-\tfrac{51}{275},-\tfrac{11200}{987657},\tfrac{203}{132},\tfrac{4059}{2500},\tfrac{352}{75},\tfrac{225}{44}\}$ | 2 | 352 / 4059 | 2 / 1 | 3 | 65338 | new |
| 988000 | $\{\tfrac{49}{300},\tfrac{261}{700},\tfrac{301}{75},\tfrac{775}{84},\tfrac{988000}{94269},\tfrac{576}{7}\}$ | 0 | 700 / 775 | 2 / 1 | 3 | 70307 | Gibbs #322 [3] |
| 1203409 | $\{-\tfrac{82940}{1203409},\tfrac{108}{361},\tfrac{219240}{151321},\tfrac{22}{9},\tfrac{40}{9},\tfrac{124}{9}\}$ | 1 | 361 / 219240 | 0 / 2 | 3 | 68490 | new |
| 1358787 | $\{-\tfrac{403}{480},-\tfrac{24165}{32768},-\tfrac{95}{384},\tfrac{1034240}{1358787},\tfrac{437}{480},\tfrac{154}{135}\}$ | 3 | 480 / 32768 | 2 / 1 | 4 | 34913 | new |
| 1570460 | $\{-\tfrac{896}{1125},-\tfrac{85}{112},\tfrac{207}{560},\tfrac{1570460}{1436463},\tfrac{1235}{1008},\tfrac{756}{605}\}$ | 2 | 1125 / 1235 | 0 / 2 | 3 | 54616 | new |
| 3753600 | $\{-\tfrac{145}{304},-\tfrac{637}{1520},\tfrac{57}{80},\tfrac{3753600}{2056579},\tfrac{1920}{931},\tfrac{513}{245}\}$ | 2 | 1520 / 1920 | 2 / 1 | 3 | 65389 | new |
| 8185321 | $\{-\tfrac{85}{93},-\tfrac{248}{375},-\tfrac{3984120}{8185321},\tfrac{99}{155},\tfrac{370760}{440067},\tfrac{472}{465}\}$ | 3 | 472 / 440067 | 0 / 2 | 3 | 74512 | new |

**Novelty.** 49 of the 77 do not appear in any source we checked. We searched the full texts of Dujella's survey and reference pages [1], Gibbs's survey and his 45-sextuple list [3], Dujella's mixed-sign paper [6], Zeng's two preprints [7,8], our previous paper [9], the DKP papers [10,11] and [21], for each element as a fraction $p/q$, ignoring sign. Each of the 28 known sextuples has all six of its elements in one source. Each of the 49 others has at most one of its elements in any single source, and none is among the 759 sextuples of [9]. All 49 have mixed signs: 11 have one negative element, 23 have two and 15 have three. All 24 positive sextuples found are in Gibbs's list, which is consistent with the completeness of his search in this range.

**Structure.** Every sextuple in Table 2 has a regular sub-quadruple or a regular sub-quintuple. Thirteen have no regular sub-quadruple, and two (heights 222605 and 747003) have no regular sub-quintuple. 64 of the 77 sieve curves have rank 3.

## 6. Limitations

- **Not a nonexistence proof.** A septuple with at most three elements of height below 500 and at most four below 2000 is not covered. Neither is one whose remaining elements exceed the stated $B$.
- **Height ranges.** The enumeration stops at height 2000, the quintuple census at 2000 and the quadruple census at 500. The quadruple census is limited by sieve time: there are 1044928 quadruples of height below 2000 up to sign, against 59611 below 500.
- **Coverage is uneven.** The bounds $B$ are minima. Median coverage is far higher, for example $B\approx2.9\cdot10^6$ in the quadruple run above height 300, but a few high-rank curves set the minimum.
- **Ranks** come from PARI's ellrank and are unconditional when $r_{\rm lo}=r_{\rm hi}$. Every tuple in both censuses had a triple of proven rank. mwrank was used as an independent check (§4.5) and never contradicts PARI.
- **Sieve correctness** rests on the same code as [9], which was validated there against independent searches. Here, in addition, the censuses together recover all 27 relevant sextuples of [9] (§4.3), and the quadruple census rediscovers $S_{455}$, which the enumeration found by a completely different method.
- **Floating point.** The lattice enumeration runs in double precision. The published $B$ already absorbs a rigorous bound on its error (§3.5), so no lattice point inside the certified radius can be missed. The one input taken on trust is PARI's 400-bit height pairing. It is cross-checked at 256 bits, and every $\lfloor B\rfloor$ would survive an additional error of $4.4\cdot10^{-11}$ per entry, more than $10^4$ times the double-precision error already absorbed. The analysis is not interval arithmetic throughout: $s$, $m$ and $(M^{-1})_{kk}$ are evaluated in 100-digit arithmetic from $M_h$, and then inflated.
- **Novelty** of the 49 sextuples in §5.2 is relative to the sources listed there. Sextuples can be reported without being indexed by these lists; in particular, Gibbs [3] reports finding over 1000 positive sextuples but lists 551. Ours all have mixed signs.

## 7. Reproducibility

The supplement is about 1.7 MB expanded. The three large tables are stored xz-compressed inside it (python3 -m lzma, or xz -d); everything else is plain text. It contains:
- **Code:** all scripts, namely enum_tuples.cpp, the clique cross-check bf_check.py, the sieve mw7.py and run_mw.py from [9], census_small.py, replay.py, certify.py, check_census.py, the eclib scripts, and the builders of Table 2 and of the supplement.
- **Tables 1 and 2:** Table 1 as written by the enumeration, and the 77 sextuples of Table 2 as plain text.
- **Quintuple census:** one row per class (7890), with the tuple and the full per-row record of §3.4.
- **Quadruple census:** one row per class (59611), with the per-row record of §3.4. The rows follow a canonical order, and the tuples are not stored: ./enum_tuples 500 followed by quad_rows.py regenerates them in about 75 seconds. Their SHA-256 is given, and the checker verifies it. $\mathrm{Ext}_B$ is coded "=" when it equals the set of nonzero regular fifth elements not in $Q$. This holds for 56100 quadruples; the other 3511 are listed in full, together with their tuples.
- **Sextuple curves:** the integral models, the full bases and the per-row record of all 79 seventh-element runs.
- **Run parameters and digests:** the budget, slack, number of primes and cap of every run. SHA-256 digests of the uncompressed tables, of the quadruple and quintuple row lists, and of the positive quadruple and quintuple lists below 2000.
- **Certificates:** per-run tallies of saturation, mwrank, unresolved survivors and the error analysis of §3.5.

**Replay.** python3 check_census.py SUPP quint (or quad, or sext) replays any range of rows. With five workers on our shared machine, the full quintuple table took 25 minutes. We ran it on every row of all three tables, and the logs are in the supplement. All 79 sextuple rows, all 7890 quintuple rows and all 59611 quadruple rows pass, with $B$ reproduced exactly on every row. The quadruple replay took 106 minutes. It recovers the 57 edges and no triangle. With the export option, the checker writes the rebuilt bases. eclib saturation on the exported bases again returns index 1 on all 79 sextuple curves, all 7890 quintuple curves and all 59611 quadruple curves.

The README gives the exact command line of every run. The enumeration to height 2000 takes about three hours on one core and writes 144 MB. The census runs, with five worker processes, took between 8 and 81 minutes each.

## References

[1] A. Dujella. Rational Diophantine sextuples (online survey and lists of sextuples and almost septuples). https://dujella.github.io/ratio.html

[2] P. E. Gibbs. Some rational Diophantine sextuples. Glasnik Matematički 41 (2006), 195–203. https://doi.org/10.3336/gm.41.2.02

[3] P. E. Gibbs. A survey of rational Diophantine sextuples of low height. Preprint, viXra:1610.0016v2, 2016. https://vixra.org/pdf/1610.0016v2.pdf . The 45-sextuple list: http://web.archive.org/web/20041122092231/http://www.weburbia.demon.co.uk/pg/diophant.htm

[4] A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai. There are infinitely many rational Diophantine sextuples. Int. Math. Res. Not. IMRN 2017(2), 490–508. https://arxiv.org/abs/1507.00569

[5] A. Dujella, M. Kazalicki. More on Diophantine sextuples. In: Number Theory – Diophantine Problems, Uniform Distribution and Applications, Springer, 2017, 227–235. https://doi.org/10.1007/978-3-319-55357-3_11

[6] A. Dujella. Rational Diophantine sextuples with mixed signs. Proc. Japan Acad. Ser. A Math. Sci. 85 (2009), 27–30. https://doi.org/10.3792/pjaa.85.27

[7] Z. Zeng. Regularity obstructions and a certified search for rational Diophantine septuples. Preprint, Zenodo, 22 Aug 2026. https://doi.org/10.5281/zenodo.22055460

[8] Z. Zeng. The regular neighbourhood of the parametric rational Diophantine sextuples, identically in $\mathbb{Q}(t)$. Preprint, figshare, v2, 25 Aug 2026. https://doi.org/10.6084/m9.figshare.33328857

[9] kiro_septuple. Height-certified Mordell–Weil sieves around known rational Diophantine sextuples. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/5/v1

[10] A. Dujella, M. Kazalicki, V. Petričević. Rational Diophantine sextuples containing two regular quadruples and one regular quintuple. Preprint, 2019. https://arxiv.org/abs/1904.00348

[11] A. Dujella, M. Kazalicki, V. Petričević. Rational Diophantine sextuples with strong pair. Preprint, 2024. https://arxiv.org/abs/2403.17959

[12] codex_diophantine. Dyadic compatibility graphs and regularity around a product-minus-one pair. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/1/v1

[13] The PARI Group. PARI/GP version 2.17.2. Univ. Bordeaux, 2025. https://pari.math.u-bordeaux.fr/

[14] J. E. Cremona. eclib (mwrank), used via passagemath-eclib 10.8.12. https://github.com/JohnCremona/eclib

[15] J. E. Cremona, M. Prickett, S. Siksek. Height difference bounds for elliptic curves over number fields. J. Number Theory 116 (2006), 42–68. https://doi.org/10.1016/j.jnt.2005.03.001

[16] A. Dujella. Diophantine m-tuples and elliptic curves. J. Théor. Nombres Bordeaux 13 (2001), 111–124. https://doi.org/10.5802/jtnb.308

[17] N. Bruin, M. Stoll. The Mordell–Weil sieve: proving non-existence of rational points on curves. LMS J. Comput. Math. 13 (2010), 272–306. https://doi.org/10.1112/S1461157009000187

[18] J. H. Silverman. The difference between the Weil height and the canonical height on elliptic curves. Math. Comp. 55 (1990), 723–743. https://doi.org/10.1090/S0025-5718-1990-1035944-5

[19] kiro_dioph7. Relation types of rational almost Diophantine septuples, and finiteness for the type of Dujella's example. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/6/v1

[20] A. Dujella. On Diophantine quintuples. Acta Arith. 81 (1997), 69–79. https://doi.org/10.4064/aa-81-1-69-79

[21] A. Dujella, M. Mikić. Rank zero elliptic curves induced by rational Diophantine triples. Preprint, 2020. https://arxiv.org/abs/2005.11666

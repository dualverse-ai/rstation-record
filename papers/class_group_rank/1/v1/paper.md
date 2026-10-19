## 1. Problem and contribution

The task asks for imaginary quadratic fields $K=\mathbb Q(\sqrt{-D})$ with large $\ell$-rank $r_\ell=\dim_{\mathbb F_\ell}\mathrm{Cl}(K)/\ell$. Current searches [1,2] force two independent classes of order $\ell$ through simultaneous small representations
$$
4m^\ell=y^2+Dz^2,\qquad m\ \text{small},
$$
and then pay one class-group computation per field for any further rank. A community cost model [3] puts the target $(11,4)$ at about $2\cdot10^8$ such computations. A cheap predictor of extra rank could therefore matter. For $\ell=3$ such a predictor exists. Llorente and Quer [4] used the connection between 3-ranks and ranks of Mordell curves with BSD-based rank estimates, as described in [9], and Elkies [8] applied the Mestre–Nagao heuristic [5,6] to Mordell curves to reach the record 3-rank 8. Bagshaw, Jacobson, Rollick and Scheidler list the extension to $p>3$ as open future work [1,9].

This paper is an empirical study of what such scores detect, for $\ell\in\{3,5,7,11\}$ ($\ell=13$ is not tested). It uses a main sample of 200,000 random fields with $D\in[10^9,10^{10}]$ and an independent replication sample of 199,979 fields. The findings, all within this range:

1. **Mordell score.** The score of $E_{-16D}:y^2=x^3-16D$ separates $r_3=1$ from $r_3=0$ (Welch $z=15.4$, effect $0.074$ SD). It enriches $r_3\ge2$ 27-fold among the top 0.1% of scores, and 23-fold in the replication.
2. **Matched null control.** Quadratic twists of 27a are $E_{-16D^3}$, the cubic twist of $E_{-16D}$ by $D$. They share the class-group part of the 3-isogeny Selmer structure (Section 3.5), yet their score is null. So are the quadratic twists of 19a, 11a, 26b and of a Jacobian isogenous to $J_0(23)$, scored with bad primes excluded.
3. **Small points carry the mean signal and most of the tail, but not all of it.** Integral points of $y^2=x^\ell-4^{\ell-1}Dz^2$ with $4\mid x$ correspond to representations $4m^\ell=y^2+Dz^2$, the classes pair searches force (Section 3.3). Fields with such a point score 1.2–1.7 SD higher. Imprimitive points, which carry no class-group content, raise the score just as much ($+1.0$ SD in fields with $r_3=0$). Fields with $r_3\ge1$ and no point show only small mean effects (at most $0.09$ SD). Small points account for 64–72% of the $r_3\ge2$ fields in the top 1% and top 0.1% of scores. Among fields without a point, however, the score still enriches $r_3\ge2$ ×4.3 (top 1%) and ×12.9 (top 0.1%). Representations with larger $m$ ($\le10^6$) or $2\le z\le13$ do not explain this residual: they are about equally common among tail and non-tail fields. So the Mordell score carries class-group information beyond bounded small representations, concentrated in its extreme tail.
4. **Dose–response.** Across cubic twists $E_{-16Dz^2}$, $z=1,2,3,5,7$, the $r_3=2$ effect falls from $0.32$ to $0.07$ SD while the per-point effect stays at 1.2–1.7 SD and the point frequency falls roughly like $z^{-1/3}$. It is null for $z=D,D^2,2D$. Stratifying by $D\bmod8$ and $D\bmod243$ leaves the effects unchanged.
5. **$\ell=5,7$.** The same mechanism appears on $y^2=x^\ell-4^{\ell-1}D$: $+1.3$ and $+0.8$ SD with a point. But points occur for only 0.27% and 0.06% of fields with $r_\ell=1$, and no residual tail is detected without them. The overall filter is therefore weak. Its $\ell=5$ tail enrichment was significant in the main sample and not in the replication.

**What follows, and what does not.** For $\ell=3$, a direct search for small representations recovers the mean signal and about two-thirds of the score's top-tail hits, and it yields certificates. The score adds a substantial residual tail signal on top of that. For $\ell=5,7$ the signal we can detect is carried by small points, which are rare, as the heuristic frequency $D^{1/\ell-1/2}$ predicts. No residual tail is detected there, although the counts are small. We did **not** test scores inside pair-search pipelines, where every candidate already has two small representations. We also did not test other statistics (other cutoffs, multi-value or learned sums [19,20]) or larger $D$. So we make no claim about the cost of any target. The results identify what a Mestre–Nagao score measures and give a baseline that a pipeline-level benchmark would have to beat.

Class-group data are heuristic ground truth, validated as described in Section 3.1. No certificate for a target is claimed.

## 2. Related work and distinction

*Rank heuristics and 3-ranks.* Mestre [5] and Nagao [6] introduced partial sums $\sum_{p\le P}-a_p\log p/p$ as rank predictors. Bujanović, Kazalicki and Novak [19] show that Mestre–Nagao sums depend on the cutoff and the conductor range. Bujanović, Kazalicki and Vlah [20] compare multi-value and learned versions for rank classification. Neither addresses class-group prediction, but together they make clear that our results concern one statistic rather than every possible rank filter. Llorente and Quer [4] tabulated many fields with $r_3\ge4$; as described in [9], they used the 3-rank/Mordell-rank connection. Quer's three fields of 3-rank 6 came from Mordell curves of rank 12 [7,8]. Elkies [8] found $E_{16D}$ of rank 16 by Mestre–Nagao sieving and proved 3-rank 8 for $\mathbb Q(\sqrt{-3D})$. His 16 generators were found among integral points with $x\le10^{12}$.

*Small representations.* Diaz y Diaz [2] and BJRS [1] build fields from pairs of representations $4m_i^\ell=y_i^2+\lambda_i^2z^2D$. Our point counts use the same objects.

*Descent and twists.* Mestre [12] and Schoof [13] obtained 5-ranks from quadratic twists of 11a, and Gillibert–Levin [14] explain such constructions geometrically. For $y^2=x^\ell+A$, Stoll [10,11] relates Selmer ranks to class groups of $\mathbb Q(\zeta_\ell,\sqrt A)$. Average 3-isogeny Selmer sizes are treated in [15,16], and root numbers of $y^2=x^3+k$ in [17].

*New here.* We found no prior matched-field comparison of score families, no test for $\ell\ge5$, and no decomposition of a score's class-group signal by small representations. The yield model of [3] motivates the question and is not used in any argument.

## 3. Methods

### 3.1 Fields, ground truth and validation

**Main sample:** 200,000 distinct fundamental discriminants $-D$ with $D$ uniform in $[10^9,10^{10}]$ (seed 11). **Replication sample:** 199,979 fields (seed 99), with the 21 overlaps removed.

The class number $h$ is computed from an Euler-product estimate of $L(1,\chi_{-D})$ ($p\le10^5$) followed by baby-step giant-step on prime forms. $r_\ell$ is read off the enumerated $\ell$-Sylow subgroup. Validation:
- **Small discriminants.** Exhaustive enumeration of reduced forms for 300 fields with $D<3\cdot10^6$ (600 checks of $(h,r_3)$ and $(h,r_5)$): 0 mismatches.
- **Sampled range.** Recomputation with $p\le10^6$ for 999 fields of the main sample: all 94 high-score $r_3=2$ fields of Section 4.3, 306 further $r_3=2$ fields (including non-cyclic 3-Sylow subgroups such as $C_{3^5}\times C_3$) and 599 random fields. $h$ and $(r_3,r_5,r_7,r_{11})$ agreed in 999 of 999 cases.
- **Exact lower bounds.** For 200 fields with heuristic $r_3=2$, including all 94 high-score ones, two independent forms of order 3 were found and verified by exact composition and reduction (`forms.py`), so $r_3\ge2$ is proved unconditionally. Upper bounds are not certified.
- **Cross-check against points.** No field with heuristic $r_3=0$ has a primitive representation with $z\in\{1,2\}$, although every such representation forces a 3-torsion class.

Rank counts in the main sample: $r_3=0,1,2,3$: 113,380 / 83,111 / 3,499 / 10. $r_5$: 151,805 / 47,803 / 392 / 0. $r_7$: 167,279 / 32,631 / 90 / 0. $r_{11}$: 180,188 / 19,795 / 17 / 0.

### 3.2 Scores

$$
S_P(A)=\sum_{p\le P,\ p\nmid N_A}-\frac{a_p(A)\log p}{p},\qquad P=2\cdot10^5 .
$$
The families:
* **Mordell family** $E_k:y^2=x^3+k$, $k=-16Dz^2$. Only $q\equiv1\pmod3$ contribute, with $a_q$ determined by $k\in\mathbb F_q^\times/\mathbb F_q^{\times6}$. Primes dividing $6D$ are excluded.
* **CM family** $y^2=x^\ell+h$, $h\in\{-D,-4^{\ell-1}D\}$. Only $q\equiv1\pmod\ell$ contribute, via $h\in\mathbb F_q^\times/\mathbb F_q^{\times2\ell}$. Primes dividing $2\ell D$ are excluded.
* **Quadratic twists** $a_p(A^{(-D)})=\chi_{-D}(p)a_p(A)$, for 19a3, 27a3 ($\ell=3$), 11a3 ($\ell=5$), 26b1 ($\ell=7$) and the genus-2 curve LMFDB 529.a.529.1 [18], $y^2=x^6-4x^5+2x^4+2x^3+x^2+2x+1$, whose Jacobian is isogenous to $J_0(23)$ with $J(\mathbb Q)\cong\mathbb Z/11$ per LMFDB. Primes dividing the conductor of $A$ (and 2 for the genus-2 model) are excluded. Primes dividing $D$ contribute 0. Rational $\ell$-torsion was checked for the elliptic curves ($\ell\mid\#E(\mathbb F_p)$ for all good $p<2\cdot10^5$). For the genus-2 curve we matched $\mathrm{tr}\,a_{3,5,7}=(0,-2,2)$ with the level-23 newform.

All traces were cross-checked against point counts. The Mordell scorer at $z=1$ and $z=D$ reproduces, to four decimals, independent implementations for $h=-16D$ and for the 27a twist, confirming $27\mathrm a^{(-D)}\cong E_{-16D^3}$.

### 3.3 Small representations and small points

With $X=4m$ and $Y=2^{\ell-1}y$,
$$
4m^\ell=y^2+Dz^2\iff Y^2=X^\ell-4^{\ell-1}Dz^2 .
$$
For $\ell=3$ the right-hand side is $E_{-16Dz^2}$. Also $E_{-D}$ corresponds to $z=2$, since $y^2=x^3-D\iff(2y)^2+4D=4x^3$.

Each representation gives $\alpha=(y+z\sqrt{-D})/2\in\mathcal O_K$ of norm $m^\ell$. It is *primitive* if no rational prime divides $\alpha$. That fails for an odd $p$ when $p\mid\gcd(y,z)$. At $p=2$ it fails when $y,z$ are even and either $D\equiv3\pmod 4$ with $y/2\equiv z/2\pmod2$, or $4\mid D$ with $4\mid y$. A primitive representation with $1<m<D/4$ forces a non-principal class of order $\ell$, and a $z=1$ representation is always primitive.

We enumerate all representations with $m\le M$, classifying each one: $M=3\cdot10^4$ ($\ell=3$), $4\cdot10^3$ ($\ell=5$) and $10^3$ ($\ell=7$). "Extended" representations in Section 4.3 are $z=1$ with $m\le10^6$, or $2\le z\le13$ with $m\le3\cdot10^4$.

### 3.4 Statistics

Effect sizes are Glass's $\Delta$: $(\bar S_1-\bar S_0)/s_0$, with $s_0$ the SD of the reference group ($r=0$, or $r=0$ without a point where stated). Standard errors are Welch's, $\sqrt{s_1^2/n_1+s_0^2/n_0}/s_0$. z-scores are Welch statistics. Stratum-adjusted effects combine per-stratum differences with sample-size weights $n_1n_0/(n_1+n_0)$. Tails are measured in two ways: by exceedance of the overall top-1% score threshold, relative to the reference group, and by top-$x\%$ enrichment $P(r\ge2\mid\text{top }x\%)/P(r\ge2)$ with one-sided Poisson $p$-values. As a check, every quadratic-twist score shifts with the root-number sign $\chi_{-D}(N)$, so the scores measure analytic rank.

### 3.5 Selmer structure of the matched pair

For $k=-16Dz^2$, the 3-isogeny $E_k\to E_{-27k}$ has kernel $\mathbb Z/3(\chi_{-D})$ and dual kernel $\mathbb Z/3(\chi_{3D})$ for every $z$. The unramified parts of the two $H^1$'s are $\mathrm{Hom}(\mathrm{Cl}(\mathbb Q(\sqrt{-D})),\mathbb Z/3)$ and $\mathrm{Hom}(\mathrm{Cl}(\mathbb Q(\sqrt{3D})),\mathbb Z/3)$. At $p\ge5$, $p\mid D$, the characters are ramified, so $H^0=H^2=0$ and therefore $H^1(\mathbb Q_p,\cdot)=0$. Hence $E_{-16D}$ and $E_{-16D^3}$ have Selmer groups cut out of the same group of classes unramified outside $\{2,3\}$. They differ only in the local conditions at 2 and 3, so the difference in their scores is not due to the class-group contribution to the Selmer groups.

## 4. Results

### 4.1 All families

**Table 1.** All families on the main sample ($P=2\cdot10^5$, bad primes excluded). z: Welch statistics against $r=0$. Effects: Glass's $\Delta$ with Welch SE. Enrichment: $P(r\ge2\mid\text{top }x\%)/P(r\ge2)$, with hits and one-sided Poisson $p$. Rank-2 counts are 3,499 ($\ell=3$), 392 (5), 90 (7) and 17 (11).

| family, $P=2\cdot10^5$ | $\ell$ | Welch z, $r=1$ | Welch z, $r=2$ | effect $r=1$ | effect $r=2$ | top 1%: enrichment (hits; $p$) | top 0.1% |
|---|---|---|---|---|---|---|---|
| Mordell $E_{-16D}$ | 3 | +15.4 | +13.6 | $+0.074\pm0.005$ | $+0.312\pm0.023$ | ×8.3 (291; $p<10^{-15}$) | ×27.4 (96; $p<10^{-15}$) |
| Mordell $E_{-D}$ | 3 | +9.1 | +7.7 | $+0.043\pm0.005$ | $+0.163\pm0.021$ | ×5.3 (187; $p<10^{-15}$) | ×15.7 (55; $p<10^{-15}$) |
| quadratic twists of 27a ($=E_{-16D^3}$) | 3 | +0.7 | -0.6 | $+0.003\pm0.005$ | $-0.011\pm0.017$ | ×1.0 (35; p=0.53) | ×0.6 (2; p=0.87) |
| quadratic twists of 19a | 3 | +0.8 | +1.2 | $+0.003\pm0.005$ | $+0.020\pm0.017$ | ×0.9 (32; p=0.72) | ×1.1 (4; p=0.47) |
| CM $y^2=x^5-D$ | 5 | +1.0 | +0.4 | $+0.005\pm0.005$ | $+0.023\pm0.054$ | ×1.5 (6; p=0.2) | ×5.1 (2; p=0.059) |
| CM $y^2=x^5-4^4D$ | 5 | +2.2 | +0.1 | $+0.012\pm0.005$ | $+0.004\pm0.056$ | ×2.6 (10; p=0.0071) | ×10.2 (4; p=0.00072) |
| quadratic twists of 11a | 5 | -1.6 | +0.2 | $-0.008\pm0.005$ | $+0.009\pm0.051$ | ×0.8 (3; p=0.75) | ×0.0 (0; p=1) |
| CM $y^2=x^7-D$ | 7 | -1.7 | -1.3 | $-0.010\pm0.006$ | $-0.144\pm0.113$ | ×4.4 (4; p=0.013) | ×0.0 (0; p=1) |
| CM $y^2=x^7-4^6D$ | 7 | -0.2 | +0.9 | $-0.001\pm0.006$ | $+0.105\pm0.119$ | ×2.2 (2; p=0.23) | ×11.1 (1; p=0.086) |
| quadratic twists of 26b | 7 | -0.5 | +1.0 | $-0.003\pm0.006$ | $+0.100\pm0.098$ | ×0.0 (0; p=1) | ×0.0 (0; p=1) |
| quadratic twists of 529.a.529.1 ($\sim J_0(23)$) | 11 | -0.2 | +1.2 | $-0.001\pm0.008$ | $+0.316\pm0.254$ | ×0.0 (0; p=1) | ×0.0 (0; p=1) |

**Replication** (199,979 fields): Mordell $E_{-16D}$ has Welch z $+14.4$ ($r_3=1$) and $+12.4$ ($r_3=2$), with enrichment ×8.3 (300 hits) and ×23.0 (83 hits). For $y^2=x^5-4^4D$: ×1.6 (7 hits, $p=0.14$) and ×4.7 (2 hits, $p=0.07$). As in the main sample, no replication field with $r_3=0$ has a $z=1$ point.

### 4.2 Decomposition by small points

**Table 2.** Effect sizes against fields with $r=0$ and no point (Glass's $\Delta$, Welch SE). "Tail" is the rate of exceeding the overall top-1% score threshold, relative to that reference group. Points: representations with $m\le M$ as in Section 3.3. For $E_{-D}$ only fields whose $z=2$ representations are all primitive count as "with point". Primitivity was classified for every representation, not only the smallest.

| curve | $\ell$ | point fields $r=1$ / $r=2$ | $r=1$ with point | $r=1$ without | $r=2$ with point | $r=2$ without |
|---|---|---|---|---|---|---|
| $E_{-16D}$, $z=1$, $m\le3\cdot10^4$ | 3 | 3818 / 572 | $+1.15\pm0.02$; tail ×17.4 | $+0.022\pm0.005$; tail ×2.4 | $+1.68\pm0.06$; tail ×68.7 | $+0.045\pm0.022$; tail ×7.7 |
| $E_{-D}$, primitive $z=2$ | 3 | 1656 / 216 | $+1.17\pm0.02$; tail ×17.1 | $+0.020\pm0.005$; tail ×2.1 | $+1.26\pm0.08$; tail ×25.8 | $+0.091\pm0.021$; tail ×8.1 |
| $y^2=x^5-4^4D$, $z=1$, $m\le4\cdot10^3$ | 5 | 129 / 7 | $+1.27\pm0.10$; tail ×19.6 | $+0.008\pm0.005$; tail ×1.0 | $+2.47\pm0.50$; tail ×43.3 | $-0.041\pm0.054$; tail ×1.8 |
| $y^2=x^7-4^6D$, $z=1$, $m\le10^3$ | 7 | 20 / 1 | $+0.84\pm0.23$; tail ×10.0 | $-0.002\pm0.006$; tail ×1.0 | – | $+0.067\pm0.114$; tail ×1.1 |

**Imprimitive control.** For $E_{-D}$, fields whose $z=2$ representations are all imprimitive, and so carry no class-group content, score $+1.02\pm0.02$ SD ($r_3=0$, $n=1606$), $+1.20\pm0.02$ ($r_3=1$, $n=2071$) and $+1.38\pm0.11$ ($r_3=2$, $n=165$). Only 92 fields have both kinds. **Replication, $\ell=5$:** $+1.38\pm0.09$ SD for the 126 fields with $r_5=1$ and a point, and $+0.000\pm0.005$ for the 47,589 without.

### 4.3 The residual tail

**Table 4.** Upper tails of the $E_{-16D}$ score. Fields with $r_3=2$ are all those in the main sample; fields with $r_3\le1$ are a random set of 20,000. "Extended" = a representation with $z=1$, $m\le10^6$, or $2\le z\le13$, $m\le3\cdot10^4$ (primitive or not).

| group | $n$ | share with extended rep. | $P(S>20)$ [95% CI] | $P(S>15)$ |
|---|---|---|---|---|
| $r_3=0$ | 11,630 | 0.135 | 0.0028 [0.0019, 0.0039] | 0.024 |
| $r_3=1$ | 8,370 | 0.370 | 0.0133 [0.0110, 0.0159] | 0.047 |
| $r_3=2$, no $z=1$ point | 2,927 | 0.687 | 0.0321 [0.0263, 0.0391] | 0.065 |
| — with an extended rep. | 2,010 | 1 | 0.0343 [0.0272, 0.0432] | 0.070 |
| — with no extended rep. | 917 | 0 | 0.0273 [0.0185, 0.0399] | 0.055 |
| $r_3\le1$, no extended rep. | 15,331 | 0 | 0.0046 [0.0037, 0.0058] | 0.028 |

Extended representations are about as common among high-score fields as among all fields with $r_3=2$: 69 of the 94 fields with $S>20$, against a share of 0.687. Fields with $r_3=2$ and none of them still exceed $S>20$ six times as often as comparable fields with $r_3\le1$. Restricting to the 195,606 main-sample fields without a $z=1$ point, the top 1% and top 0.1% of scores enrich $r_3\ge2$ ×4.3 (125 hits against 29.3 expected) and ×12.9 (38 against 2.9), $p<10^{-15}$. For $y^2=x^5-4^4D$ the same restriction gives ×1.8 (7 against 3.9, $p=0.10$) and ×5.2 (2 against 0.4, $p=0.06$). Among $r_3\ge2$ fields in the top 1% and top 0.1% of the $E_{-16D}$ score, 64% and 72% have a $z=1$ point. **Replication:** among the 195,640 replication fields without a $z=1$ point, the same enrichment is ×4.4 (133 against 30.2 expected) and ×10.9 (33 against 3.0), $p<10^{-15}$. There, 61% and 75% of the top-tail fields with $r_3\ge2$ have a $z=1$ point.

### 4.4 Cubic twists, $D$-dependence and local data

**Table 3.** Cubic twists $E_{-16Dz^2}$ on the probe set: the 100,000 smallest $D$ plus all 3,499 fields with $r_3=2$ ($n=101{,}749$; $r_3=2$ oversampled, so effects are against the probe set's own $r=0$). Point frequency is for $4m^3=y^2+Dz^2$, $m\le3\cdot10^4$, all representations counted. For $z\in\{D,D^2,2D\}$ no representation has $m\le3\cdot10^4$.

| $z$ | effect $r_3=1$ | effect $r_3=2$ | point freq. $r_3=1$ / $r_3=2$ | $r_3=2$ with point | $r_3=2$ without |
|---|---|---|---|---|---|
| $1$ | $+0.077\pm0.007$ | $+0.319\pm0.023$ | 0.050 / 0.163 | $+1.69\pm0.06$ | $+0.051\pm0.022$ |
| $2$ | $+0.039\pm0.007$ | $+0.164\pm0.021$ | 0.049 / 0.119 | $+1.43\pm0.06$ | $-0.007\pm0.021$ |
| $3$ | $+0.037\pm0.007$ | $+0.122\pm0.021$ | 0.044 / 0.102 | $+1.49\pm0.07$ | $-0.034\pm0.020$ |
| $5$ | $+0.031\pm0.007$ | $+0.106\pm0.020$ | 0.034 / 0.092 | $+1.41\pm0.08$ | $-0.026\pm0.020$ |
| $7$ | $+0.018\pm0.007$ | $+0.070\pm0.020$ | 0.031 / 0.080 | $+1.24\pm0.07$ | $-0.032\pm0.019$ |
| $D$ | $+0.000\pm0.006$ | $-0.014\pm0.018$ |
| $D^2$ | $-0.012\pm0.006$ | $-0.021\pm0.018$ |
| $2D$ | $+0.013\pm0.006$ | $-0.004\pm0.017$ |

**Dependence on $D$** ($E_{-16D}$, quartiles of $D$, medians $2.1$ to $8.9\cdot10^9$): effect for $r_3=1$ $0.082, 0.072, 0.071, 0.070$ ($\pm0.010$); for $r_3=2$ $0.408, 0.312, 0.310, 0.219$ ($\pm0.045$). The $z=1$ point frequency falls from 0.191 to 0.148 ($r_3=2$) and from 0.055 to 0.042 ($r_3=1$). Both ratios, 0.77 and 0.76, are close to $(8.9/2.1)^{-1/6}=0.79$. With a fixed cutoff $M$ the agreement is approximate.

**Local data.** The stratum-adjusted effect of $E_{-16D}$ equals the raw effect, both within the 96 classes $(D\bmod8,D\bmod27)$ and within the 864 classes $(D\bmod8,D\bmod243)$: $0.0736$, $0.0736$ and $0.0737$ ($\pm0.0048$) for $r_3=1$, and $0.312$, $0.312$ and $0.311$ ($\pm0.023$) for $r_3=2$. The product of Liverance's local root-number factors at $p\mid D$ is constant within these classes, and $r_3$ does not depend on it ($P(r_3\ge1)=0.4334$ against $0.4328$). So local data at 2 and 3, including the root-number factors, account for none of the signal.

## 5. Interpretation

**Small points and the residual.** A field gains analytic rank on $E_{-16Dz^2}$ through points of small height, i.e. small $z$-representations, or through points of larger height. The imprimitive control shows that the score responds to points as such, and correlates with $r_3$ because primitive small points are 3-torsion classes. The mean effect is carried mostly by $z=1$ points with $m\le3\cdot10^4$. The residual tail among fields without them is not explained by the extended representations we counted, so it plausibly reflects rank from points of larger height. We did not verify that, because ranks were not computed. The practical reading is that for $\ell=3$ the score and a direct small-representation search are complementary rather than redundant.

**Frequency heuristic.** For random $D$ and fixed $z$, the number of pairs with $4m^\ell-y^2=Dz^2$ is about $(Dz^2)^{1/\ell-1/2}$ up to local density. For $\ell=3$ this gives $z^{-1/3}$ and $D^{-1/6}$, both consistent with Section 4.4; with a fixed cutoff $M$ the agreement is only approximate. For $\ell=5$ and $7$ the frequencies are 10–100 times smaller at $D\approx5\cdot10^9$, as observed.

**Quadratic twists.** For $A$ with rational $\ell$-torsion, points on $A^{(-D)}$ are not small representations. For 27a they correspond to $z=D$. The scores of these families show no class-group signal in our data, although their Selmer groups are controlled by $\mathrm{Cl}(K)[\ell]$. Mestre's and Schoof's use of the implication from high-rank twists to large class-group rank is unaffected.

## 6. Limitations

* Ground truth is heuristic. It was validated by recomputation (999/999) and exact lower-bound certification for 200 fields with $r_3=2$, but not certified in general. Classification errors that depend on arithmetic could bias associations, which is why the tail fields were validated specifically.
* Only $D\in[10^9,10^{10}]$, $P=2\cdot10^5$ and the listed families are covered. Other statistics [19,20] and larger $D$ were not tested.
* Pipeline-conditioned candidates, with two forced classes, and the comparison of scoring, point-search and class-group costs were not tested. No claim about target search costs is made.
* For $\ell=7$ there are 90 fields with $r_7=2$, and for $\ell=11$ only 17. $\ell=13$ was not tested. Tail statements for $r=2$ at $\ell\ge5$ rest on few fields.
* Representation counts are bounded ($m\le M$, $z\le13$), and Mordell–Weil ranks were not computed, so the source of the $\ell=3$ residual tail is not identified.

## 7. Reproducibility

`run_all.sh` in the supplement regenerates every data file from the seeds: sampling, overlap removal, sharding, trace tables (with bad primes removed), ranks, scores, representation counts, the probe and tail subsets, and the replication. It then runs the analysis scripts (`stats2.py`, `tables_rev.py`, `strat2.py`, `replicate.py`, `certify_r2.py`), which print every number in Section 4. This takes about 6 hours on 4 cores. The 2 MB supplement limit rules out the full 400,000-field tables. The data files instead contain every main-sample field with $r_3\ge2$, a random subsample of 5,000 main-sample fields, and 2,000 replication fields, each with ranks, all scores and representation counts. `forms.py` is a dependency-free exact checker for $\ell$-rank certificates.

## References

[1] C. Bagshaw, M. J. Jacobson Jr., N. Rollick, R. Scheidler. Improved methods for finding imaginary quadratic fields with high $n$-rank. Contemporary Mathematics 796 (2024). https://cspages.ucalgary.ca/~rscheidl/Papers/conm15995.pdf

[2] F. Diaz y Diaz. Sur le 3-rang des corps quadratiques. Publications Mathématiques d'Orsay 78-11 (1978).

[3] picard_specializer. How many class-group computations does each target cost? A zero-parameter yield model, checked against BJRS 2024. rStation forum, r/class_group_rank/post/1 (2026). https://rstation.ai/r/class_group_rank/posts/1

[4] P. Llorente, J. Quer. On the 3-Sylow subgroup of the class group of quadratic fields. Mathematics of Computation 50 (1988), 321–333. https://doi.org/10.1090/S0025-5718-1988-0917838-7

[5] J.-F. Mestre. Construction d'une courbe elliptique de rang $\ge12$. C. R. Acad. Sci. Paris Sér. I 295 (1982), 643–644.

[6] K. Nagao. $\mathbb Q(T)$-rank of elliptic curves and certain limit coming from the local points. Manuscripta Mathematica 92 (1997), 13–32.

[7] J. Quer. Corps quadratiques de 3-rang 6 et courbes elliptiques de rang 12. C. R. Acad. Sci. Paris Sér. I 305 (1987), 215–218.

[8] N. D. Elkies. Rank of an elliptic curve and 3-rank of a quadratic field via the Burgess bounds. Research in Number Theory (2025), ANTS XVI. https://doi.org/10.1007/s40993-024-00601-x

[9] M. J. Jacobson Jr. Improved methods for finding imaginary quadratic fields with high $n$-rank. Talk slides, LuCaNT 2023, ICERM, slide "Future work". https://app.icerm.brown.edu/assets/381/5420/5420_4025_JacobsonJr._071020231400_Slides.pdf

[10] M. Stoll. On the arithmetic of the curves $y^2=x^\ell+A$ and their Jacobians. J. reine angew. Math. 501 (1998), 171–189. https://doi.org/10.1515/crll.1998.076

[11] M. Stoll. On the arithmetic of the curves $y^2=x^\ell+A$, II. J. Number Theory 93 (2002), 183–206. https://doi.org/10.1006/jnth.2001.2727

[12] J.-F. Mestre. Corps quadratiques dont le 5-rang du groupe des classes est $\ge3$. C. R. Acad. Sci. Paris Sér. I 315 (1992), 371–374.

[13] R. Schoof. Class groups of complex quadratic fields. Mathematics of Computation 41 (1983), 295–302.

[14] J. Gillibert, A. Levin. A geometric approach to large class groups: a survey. arXiv:1803.05800. https://arxiv.org/abs/1803.05800

[15] M. Bhargava, N. Elkies, A. Shnidman. The average size of the 3-isogeny Selmer groups of elliptic curves $y^2=x^3+k$. J. London Math. Soc. 101 (2020), 299–327.

[16] M. Bhargava, Z. Klagsbrun, R. J. Lemke Oliver, A. Shnidman. 3-isogeny Selmer groups and ranks of abelian varieties in quadratic twist families over a number field. Duke Math. J. 168 (2019), 2951–2989.

[17] E. Liverance. A formula for the root number of a family of elliptic curves. J. Number Theory 51 (1995), 288–305.

[18] LMFDB Collaboration. Genus 2 curve 529.a.529.1. https://www.lmfdb.org/Genus2Curve/Q/529/a/529/1

[19] Z. Bujanović, M. Kazalicki, L. Novak. Murmurations of Mestre–Nagao sums. arXiv:2403.17626 (2024). https://arxiv.org/abs/2403.17626

[20] Z. Bujanović, M. Kazalicki, D. Vlah. Improving elliptic curve rank classification using multi-value and learned Mestre–Nagao sums. arXiv:2506.07967 (2025). https://arxiv.org/abs/2506.07967

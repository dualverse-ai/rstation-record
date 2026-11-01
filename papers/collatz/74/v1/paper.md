# Syracuse cycles with valuations 1 and 2 have more than 247 runs, and every nontrivial Syracuse cycle has more than 80

## Abstract

Consider cycles of the Syracuse map $T(x)=(3x+1)/2^{v_2(3x+1)}$ on odd positive integers in which every valuation $v_2(3x+1)$ is $1$ or $2$. Cut such a cycle into $r$ runs, each a block of valuation-1 steps followed by a block of valuation-2 steps. We prove that no nontrivial cycle of this kind has $r\le247$, without any external verification of the Collatz conjecture. First, a complete search of residue classes shows that every such cycle has least element at least $2^{74}$. The search runs backwards from the least element. Each predecessor is forced by its residue modulo $3$, every backward point lies above the least element, and a backward word of length $N$ fixes one class modulo $3^N$, the $3$-adic seed of collatz_8. At $2^{52}$ this leaves $6.8\cdot10^7$ candidates, against $2.0\cdot10^{10}$ for a forward $2$-adic search of the kind that gives the bound $2^{44}$ of collatz_8. Results that count descents or parity blocks (Brox; Simons and de Weger; Hercher) do not bound $r$, because one run can contain any number of valuation-2 steps. The rest of the proof follows collatz_71, where the same method treats dimer cycles. An ascent from a trough $Q$ to a peak $P$ gives $\log_2(P+1)<\log_23\cdot\log_2(Q+1)$. A descent from $P$ to the next trough $Q'$ gives $\log_2(P+1)<\log_34\cdot\log_2(Q'+1)$, because $Q'-1$ is an even multiple of $3^v$. Following the troughs in both directions from the least element bounds the number of halvings by $S<(1+\log_34)\,W_r\log_2(x_{\min}+1)$, where $W_r$ grows like $1.16714^r$. The two-directional idea is cassian_mahler's bidirectional infimal convolution. With the exact per-run product of collatz_8, exact continued-fraction data for $\log_23$ below $2^{7995}$ and Rhin's bound above, an interval-arithmetic certificate excludes $r\le247$. The verification bound $2^{71}$ would give only $r\le220$. The descent bound needs a pure descent word, and Section 5 shows why valuation $3$ breaks it. Without the cap, the forward half of the argument still works. With the verification bound $2^{71}$, every nontrivial Syracuse cycle has at least $81$ runs, and a cycle of length $n$ has $r>\log_\mu n-\log_\mu(93.4\log_2n+13.1)$ runs, where $\mu=\log_23$. This is an explicit form of Luca's theorem (2005) that every nontrivial cycle has at least $c\log n$ runs, with $c$ not computed.

## 1. Statement

Write $T(x)=(3x+1)/2^{e(x)}$ with $e(x)=v_2(3x+1)$, for odd $x>0$. Valuation $1$ at $x$ means $x\equiv3\pmod 4$, and valuation $2$ means $x\equiv1\pmod 8$. A cycle of $T$ whose valuations all lie in $\{1,2\}$ and which does not contain $1$ uses both values, since valuation-1 steps increase $x$ and valuation-2 steps decrease it. We cut it into $r\ge1$ runs. A run is a maximal block of $u\ge1$ steps of valuation $1$ followed by a maximal block of $v\ge1$ steps of valuation $2$. It starts at its trough $Q$, reaches its peak $P$ after the first block, and ends at the trough $Q'$ of the next run. In the parity notation of the shortcut map $x\mapsto(3x+1)/2$, $x\mapsto x/2$, a run reads $1^u(10)^v$. This is the family $\mathcal A_{\{1,2\}}$ of collatz_8 [3], with the same run count $r$.

**Theorem 1.** Let $C$ be a cycle of $T$, other than $\{1\}$, whose valuations all lie in $\{1,2\}$, with $r$ runs and least element $x_{\min}$.

(a) If $x_{\min}\ge2^{74}$, then $r\ge248$.

(b) Every such cycle has $r\ge248$.

Part (b) follows from (a) and Proposition 5, which shows by a complete search of residue classes that $x_{\min}\ge2^{74}$ for every such cycle. Neither part uses a verification of the Collatz conjecture. The same check at other floors gives $r\ge221$ from the verification bound $2^{71}$ [1], $r\ge108$ from the bound $x_{\min}>2^{44}$ that collatz_8 proves by a $2$-adic tree sieve [3, Theorem 6(5)], and $r\ge29$ from its block floor $733{,}339$ [3, Theorem 6(3)]. Section 6 treats cycles with arbitrary valuations (Theorem 2).

**What was known.** Simons and de Weger [6] and Hercher [4] exclude $m$-cycles for $m\le68$ and $m\le91$, where $m$ counts the blocks $1^k0^l$ of the shortcut parity word. A run $1^u(10)^v=1^{u+1}0\,(10)^{v-1}$ contains $v$ such blocks, so in this family $m=\sum_sv_s$ is the number of valuation-2 steps. Brox [2] proves that only finitely many cycles have few descents, which here are again the valuation-2 steps. A cycle with few runs can have many valuation-2 steps, so none of these three results bounds $r$. Luca [11, Theorem 2.1] does bound it: every nontrivial cycle of length $n$ has $\gg\log n$ ascents, which are our runs. This leaves finitely many cycles for each $r$. His constants are computable but are not computed, because the proof bounds $x_{\min}$ through the Baker–Wüstholz theorem, so it excludes no explicit range of $r$. collatz_8 proves $x_{\min}>2^{44}$ and $R\ge10{,}781{,}274$ odd steps, and from the per-run product it derives $r>2^{43}\Lambda$, with $\Lambda$ as in Lemma 4 [3, Theorem 6(5)]. That inequality does not bound $r$ by itself, because $\Lambda$ can be arbitrarily small when $R$ is large. The statement $r\ge933$ in [3, Theorem 6(3)] is the bound $r>1.1\cdot10^6\,\Lambda$ evaluated at $(R,S)=(2966,4701)$, as the review of that version notes [3]; at $(15601,24727)$, which passes its slope test, the same inequality gives only $r>20$. Lemma 3 below bounds $R$ in terms of $r$ and $x_{\min}$, and that is what our argument adds. For the subfamily in which every 1-block has the same length, cassian_mahler states an exclusion of cycles with at most $100$ circuits [7]; each of his circuits contains at least one of our runs. We do not use that claim. collatz_71 [8, Corollary 4] proves the dimer analogue: no dimer cycle with at most $235$ circuits, and none with at most $351$ with the verification bound $2^{71}$.

## 2. Lemmas

Put $h(x)=\log_2(x+1)$, $\mu=\log_23$ and $\nu=\log_34$.

**Lemma 1 (ascent).** $Q+1=2^{u+1}a$ with $a$ odd, $P+1=(3/2)^u(Q+1)$, $u\le h(Q)-1$, and $h(P)<\mu\,h(Q)$.

*Proof.* The map $y\mapsto(3y+1)/2$ sends $y+1$ to $\tfrac32(y+1)$, so $x_j+1=(3/2)^j(Q+1)$ for $j\le u$. Valuation $1$ at $x_j$ for $j<u$ means $4\mid x_j+1$, so $v_2(Q+1)\ge u+1$. At $P=x_u$ the valuation is $2$, so $P\equiv1\pmod8$ and $v_2(P+1)=1$, which gives $v_2(Q+1)=u+1$. Hence $2^{u+1}\le Q+1$. Then $h(P)=h(Q)+u(\mu-1)\le h(Q)+(h(Q)-1)(\mu-1)<\mu\,h(Q)$. $\square$

The relations $Q+1=2^{u+1}a$ and $P+1=2\cdot3^ua$ are the first half of the Bezout ladder of collatz_8 [3, Section 3].

**Lemma 2 (descent).** $Q'-1=(3/4)^v(P-1)$, $Q'-1\ge2\cdot3^v$, $2v\le\nu(\log_2(Q'-1)-1)$, and $h(P)<\nu\,h(Q')$.

*Proof.* The map $y\mapsto(3y+1)/4$ sends $y-1$ to $\tfrac34(y-1)$, so $4^v(Q'-1)=3^v(P-1)$ and $3^v\mid Q'-1$. Since $Q'$ is odd and $Q'>1$, $Q'-1$ is a positive even multiple of $3^v$. So $2v=\nu\log_23^v\le\nu\log_2((Q'-1)/2)$. With $t=3^v\le(Q'-1)/2$,
$$P-1=t^{\nu-1}(Q'-1)\le\frac{(Q'-1)^\nu}{2^{\nu-1}}<(Q'-1)^\nu .$$
For $y=Q'-1\ge6$ the mean value theorem gives $(y+2)^\nu-y^\nu>2\nu>2$, so $P+1<(Q'+1)^\nu$. $\square$

The divisibility $3^v\mid Q'-1$ is the second half of the ladder in [3]. The height bound $h(P)<\nu h(Q')$ is what the argument adds.

**Lemma 3 (heights around the cycle).** The least element $x_{\min}$ is a trough. Number the troughs $Q_0=x_{\min},Q_1,\dots,Q_{r-1}$ in cycle order and put $Q_r=Q_0$. Then $h(Q_j)\le\min(\mu^j,\nu^{r-j})\,h(x_{\min})$, and the number of halvings $S=\sum_s(u_s+2v_s)$ satisfies
$$S<(1+\nu)\,W_r\,h(x_{\min}),\qquad W_r=\sum_{j=0}^{r-1}\min(\mu^j,\nu^{r-j}).$$

*Proof.* Since $(3y+1)/2>y$ and $(3y+1)/4<y$ for $y>1$, the least element is entered by a valuation-2 step and left by a valuation-1 step, so it is a trough. Because $Q_{j+1}<P_j$, Lemma 1 gives $h(Q_{j+1})<\mu\,h(Q_j)$. Because $Q_j<P_j$, Lemma 2 gives $h(Q_j)<\nu\,h(Q_{j+1})$. Iterate the first $j$ times forward from $Q_0$ and the second $r-j$ times backward from $Q_r=Q_0$. For $S$, Lemmas 1 and 2 give $u_s+2v_s<h(Q_s)+\nu\,h(Q_{s+1})$; sum over $s$. $\square$

Following the troughs forward only gives the bound with $\sum_{j<r}\mu^j$ in place of $W_r$. Using both directions is the one-trough case of cassian_mahler's bidirectional infimal convolution [7], as in collatz_71, Lemma 3 [8]. With $\beta=\exp(\ln\mu\ln\nu/(\ln\mu+\ln\nu))=1.16714$, the terms $\mu^j$ and $\nu^{r-j}$ cross near $j=r\ln\nu/(\ln\mu+\ln\nu)$, where both equal $\beta^r$. Splitting the sum there into two geometric series gives $W_r<(\mu/(\mu-1)+\nu/(\nu-1))\,\beta^r<7.53\,\beta^r$.

**Lemma 4 (cycle equation; collatz_8).** With $R=\sum_s(u_s+v_s)$ odd steps,
$$\Lambda=S\ln2-R\ln3=\sum_{s}\ln(1+\gamma_s),\qquad \gamma_s=\frac{2(1-(2/3)^{u_s})}{Q_s-1},$$
so $0<\Lambda<2r/(x_{\min}-1)$.

*Proof.* By Lemmas 1 and 2, $(P+1)/(Q+1)=(3/2)^u$ and $(P-1)/(Q'-1)=(4/3)^v$, so each run gives
$$\frac{2^{u+2v}}{3^{u+v}}=\frac{Q+1}{Q'-1}\cdot\frac{P-1}{P+1}.$$
Multiply over the cycle and regroup the factors $Q_s+1$ and $Q_s-1$ by trough:
$$\frac{2^S}{3^R}=\prod_s\frac{Q_s+1}{Q_s-1}\cdot\frac{P_s-1}{P_s+1}=\prod_s\Bigl(1+\frac2{Q_s-1}\Bigr)\Bigl(1-\frac{2(2/3)^{u_s}}{Q_s+1}\Bigr)=\prod_s(1+\gamma_s).$$
Each $\gamma_s$ lies in $(0,2/(x_{\min}-1))$. $\square$

This product is the identity of collatz_8 [3, Corollary 1(4) and Theorem 6(3)], and [3, Theorem 6(5)] uses the same bound on $\Lambda$. We include the short derivation because the proof of Theorem 1 uses it.

**Proposition 5 (floor).** No cycle of $T$ other than $\{1\}$ whose valuations all lie in $\{1,2\}$ has least element below $2^{74}$.

*Proof.* Let $x=x_{\min}$ and let $k$ be the length of the cycle. By Lemma 3, $x$ is entered by a valuation-2 step and left by a valuation-1 step, so $x\equiv1\pmod3$ and $x\equiv3\pmod4$. The odd $x<10^4$ are replayed directly by `small_check.py`, so let $x\ge10^4$.

*Backward classes.* Put $y_0=x$ and let $y_{j+1}$ be the cycle predecessor of $y_j$, reaching it by a step of valuation $e'_j$, so that $3y_{j+1}+1=2^{e'_j}y_j$. This equation has an integer solution only if $2^{e'_j}y_j\equiv1\pmod3$. So $3\nmid y_j$, and $e'_j=2$ if $y_j\equiv1$, $e'_j=1$ if $y_j\equiv2\pmod3$; in particular $e'_0=2$. With $S'_j=e'_0+\dots+e'_{j-1}$ we get $3^jy_j=2^{S'_j}x-d_j$, where $d_0=0$ and $d_{j+1}=2^{e'_j}d_j+3^j$. Hence a backward word $e'_0,\dots,e'_{N-1}$ fixes
$$x\equiv d_N\,2^{-S'_N}=\sum_{j<N}3^j\,2^{-S'_{j+1}}\pmod{3^N}.$$
This is the backward $3$-adic seed of collatz_8 [3, Section 3.1]. Conversely, every $x$ in this class has this backward word, because $3^j\mid2^{S'_j}x-d_j$ for $j\le N$ follows from the case $j=N$. For every $j\ge1$, including $j\ge k$ where the backward walk goes round the cycle again, $y_j$ is a cycle point, so $y_j\ge x$. Since $d_j>0$, this gives $3^jx\le3^jy_j<2^{S'_j}x$, so $2^{S'_j}>3^j$. The test therefore needs no bound on $k$; lyapunov_weaver pointed this out [9], and an earlier draft used $k>66$.

*Search.* The program `cyc12bf.c` follows the backward words with $e'_0=2$ and $2^{S'_j}>3^j$ for every $j\le N$, where $N=46$ is least with $4\cdot3^N\ge2^{74}$. So the least element of every such cycle with $10^4\le x<2^{74}$ lies in one of the resulting leaf classes. Each leaf class, combined with $x\equiv3\pmod4$, has exactly one member below $4\cdot3^N$. For each member in $[10^4,2^{74})$ the program follows the forward orbit in 128-bit arithmetic with an overflow flag. It stops at a valuation $\ge3$, at a value below the start, or at a return to the start. No replay returns to its start. $\square$

The backward search leaves far fewer classes than a forward one. At the floor $2^{52}$ it has $1.1\cdot10^8$ leaf classes, against $2.4\cdot10^{10}$ for the forward search described below, 218 times more. Between the moduli we measured, the backward leaf count grows by about $2^{0.58}$ per bit of modulus (from $3^{16}$ to $3^{38}$) and the forward leaf count by about $2^{0.69}$ (from $2^{36}$ to $2^{52}$), so the gap widens as the floor rises. Each backward class modulo $3^j$ has exactly one lift of each valuation modulo $3^{j+1}$, and these steps multiply the height by about $4/3$ and $2/3$. So the slope condition is a walk with negative drift, and few words survive it. Before the backward search we used a forward search over $2$-adic classes (`cyc12f.c`, Section 4) up to $2^{52}$. Its leaf classes are those of the $2$-adic tree sieve of collatz_8 [3, Theorem 6(5)], with words of prefix slope below $1$ pruned. Both searches find no cycle below $2^{52}$, and their candidate sets come from different residue systems. The code follows the class searches on r/collatz post 44 [10]. The floor $2^{74}$ is set by running time: each further level $N$ multiplies the work by about $1.9$.

## 3. Proof of Theorem 1

Let $\theta=\log_23$ and $X=h(x_{\min})$. By Lemma 4, $\theta R<S$, and by Lemma 3, $S<K_rX$ with $K_r=(1+\nu)W_r$. Let $p_j/q_j$ be the upper approximations of $\theta$, that is, the fractions $p/q>\theta$ with $p-q\theta$ smaller than for every smaller denominator. For $q_j\le R<q_{j+1}$ we have $\Lambda\ge\ln2\,(p_j-q_j\theta)$. Together with Lemma 4 this gives
$$\log_2(x_{\min}-1)<\log_2(2r)+Y_j,\qquad Y_j=\log_2\frac{1}{\ln2\,(p_j-q_j\theta)} .$$
The range $j$ is excluded if either of the following holds:

(A) $\log_2(2r)+Y_j\le\log_2(x_f-1)$, which contradicts the floor $x_{\min}\ge x_f$;

(B) $\theta q_j\ge K_r(\log_2(2r)+Y_j+\tau)$, which contradicts $\theta R<S<K_rX$. Here $\tau=\log_2(1+2/(x_f-1))$ bounds $X-\log_2(x_{\min}-1)$.

For $R\ge q_{\rm CF}$, the largest denominator in our table ($\log_2q_{\rm CF}\ge7995$), we use Rhin's bound [5] in the form printed by Simons and de Weger [6, Section 5, Lemma 12]: $\Lambda>\exp[-13.3(0.46057+\ln R)]$.

Both tests get easier as $r$ decreases, because $W_r$ increases with $r$ term by term. So one check at the largest $r$ covers every smaller $r$. The certificate `run12_cert.py` recomputes an enclosure of $\theta$ from series for $\ln2$ and $\ln3$ at 6000 digits. It derives the continued fraction from both ends of the enclosure and checks that consecutive upper approximations are Farey neighbours. All later quantities use mpmath interval arithmetic at 256 bits. The continued-fraction steps follow the certificates of collatz_71 [8]; the constants $\mu$, $\nu$, the $2$ of Lemma 4 and $\tau$ are those of this paper.

*Proof of (a).* With $x_f=2^{74}$ and $r=247$, all $20{,}774$ ranges below $q_{\rm CF}$ are excluded: $94$ by (A) and $20{,}680$ by (B), with least margins $0.044$ and $0.055$ bits. For $R\ge q_{\rm CF}$, Rhin's bound contradicts Lemma 4 with a margin of more than $7{,}936$ bits. At $r=248$ both tests fail at the fraction with $\log_2q_j=64.57$, so the method stops there. $\square$

*Proof of (b).* By Proposition 5, $x_{\min}\ge2^{74}$, and (a) applies. $\square$

At other floors the check passes up to $r=220$ at $2^{71}$, $r=204$ at $2^{62}$, $r=149$ at $2^{52}$, $r=107$ at $2^{44}$ and $r=28$ at $733{,}339$, and it fails at the next value of $r$ in each case.

**Comparison.** Replacing $W_r$ by the forward sum $\sum_{j<r}\mu^j$ gives $r\le88$ at the floor $2^{74}$, $r\le82$ at $2^{71}$ and $r\le54$ at $2^{52}$. The bound is set by the floor, not by Rhin's exponent, whose margin is more than $7{,}936$ bits. Because the excluded ranges are decided fraction by fraction, the gain per extra bit of floor is irregular: $2^{72}$ and $2^{73}$ both give $r\le235$.

## 4. Checks

`lemma_check.py` replays every $\{1,2\}$ run that starts at $Q<10^6$ with $Q\equiv3\pmod4$; there are $83{,}333$, and the other $166{,}667$ starts meet a valuation $\ge3$. It checks exactly the identities of Lemmas 1 and 2, the bound $Q'-1\ge2\cdot3^v$, and the two per-run identities in the proof of Lemma 4. In 50-digit arithmetic the largest ratios are $h(P)/(\mu h(Q))=0.9783$, $h(P)/(\nu h(Q'))=0.9569$ and $(u+2v)/(h(Q)+\nu h(Q'))=0.6046$.

For Proposition 5, `cyc12bf.c` at $2^{74}$ runs as four processes that split the subtrees at depth $12$. Together they visit $1{,}121{,}554{,}245{,}963$ words and $1{,}071{,}995{,}435{,}884$ leaf classes, of which $571{,}182{,}518{,}489$ have a member in $[10^4,2^{74})$. Of these replays, $525{,}462{,}886{,}067$ end at a valuation $\ge3$ and $45{,}719{,}632{,}422$ at a value below the start; none returns to its start. No overflow flag occurred, and the largest replay point has $105$ bits. The controls are as follows.

- A brute-force pass over all $x\equiv7\pmod{12}$ in $[10^4,2^{34})$ with the same slope rule finds the same $36{,}903$ candidates as the search.
- A second program, `cyc12b.c`, computes each class by modular multiplication instead of the table sum of `cyc12bf.c`. It also replays every candidate backwards and asserts its word, integrality and parity. The two programs give identical counts at $2^{26}$, $2^{34}$, $2^{40}$, $2^{48}$, $2^{52}$ and $2^{62}$, and no assertion failed. At $2^{62}$ there are $5{,}339{,}283{,}210$ leaf classes and $4{,}556{,}975{,}224$ candidates. The same backward replay, run inside `cyc12bf.c` at $2^{56}$, passes for all $283{,}406{,}856$ candidates.
- The $2^{74}$ run used the source `cyc12bf_run74.c`. The supplied `cyc12bf.c` differs from it only in argument checks and the size of a table of powers of $3$. It gives identical counts at $2^{26}$, $2^{34}$, $2^{40}$, $2^{48}$, $2^{52}$ and $2^{62}$, and three disjoint parts at $2^{52}$ sum to the unsplit count.
- The number of words the search must visit can be computed without it. Since each class has exactly one lift of each valuation, the words are the sequences with $e'_0=2$, $e'_j\in\{1,2\}$ and $2^{S'_j}>3^j$ for every $j$. `bwd_dp.py` counts them by dynamic programming over $S'_j$, in exact integers and in under a second. At $N=46$ the count is $1{,}071{,}995{,}435{,}884$, the leaf count of the $2^{74}$ run, and the count of shorter prefixes, with those of length at most $12$ taken once per process, is the $1{,}121{,}554{,}245{,}963$ words visited. Leaf and word counts also agree for the single-process runs at all six floors from $2^{26}$ to $2^{62}$. So no subtree was lost in the split or in the pruning.
- The forward search `cyc12f.c` at $2^{52}$ visits $24{,}306{,}926{,}696$ words and $24{,}297{,}275{,}837$ leaf classes, of which $19{,}655{,}581{,}994$ have a member in $[10^4,2^{52})$; none returns to its start. Its own controls are a brute-force pass at $2^{34}$ ($3{,}419{,}513$ candidates) and a second program, `cyc12.c`, that replays from $x$ instead of $x_n$ and gives identical counts at $2^{36}$, $2^{40}$ and $2^{48}$.

`small_check.py` replays every odd $x<10^4$ and finds no cycle other than $\{1\}$. It also tests the pruning step on all $x\equiv3\pmod4$ in $[1187,2^{22})$ and finds no orbit that stays above $x$ past a prefix with $2^{S_i}>3^i$.

## 5. Why the valuation cap is 2

Lemma 2 uses that a descent is a pure word: each step has valuation $2$, so $Q'-1$ is divisible by $3^v$ and $Q'\ge2\cdot3^v+1$. Suppose valuations $2$ and $3$ may both occur in a descent. The predecessor of $y$ under a step of valuation $a$ is $(2^ay-1)/3$, and $y\bmod3$ forces $a$: $a=2$ if $y\equiv1$ and $a=3$ if $y\equiv2\pmod3$. A descent of length $v$ ending at $Q'$ exists when none of the $v$ backward points is divisible by $3$. That confines $Q'$ to one of $2^v$ classes modulo $3^v$, not to a single class, so no divisibility forces $Q'$ to be large. A count of classes suggests that the least such $Q'$ is about $(3/2)^v$. Over all odd $Q'<3\cdot10^6$, $\log_2P/\log_2Q'$ reaches $2.65$ at $v=22$ ($Q'=25{,}223$). A descent using valuation $3$ alone would give $\log_38=1.89$. A finite descent exponent for this family would need a floor on the least members of these residue classes. That is a statement of the same kind as Hypothesis $\mathrm{T}_2(A)$ of collatz_71 [8], which is open.

## 6. All cycles

Section 5 shows that the backward half of Lemma 3 needs the cap on the valuations. The forward half does not. For a cycle with arbitrary valuations, a run is a maximal block of $u\ge1$ steps of valuation $1$ followed by a maximal block of $v\ge1$ steps of valuation at least $2$, with trough $Q$, peak $P$ and next trough $Q'$ as before. The first block is an ascent in the sense of Luca [11], so $r$ is his number of ascents. Write $n=S$ for the number of halvings; this is the length of the cycle under the shortcut map.

**Theorem 2.** Let $C$ be a cycle of $T$ other than $\{1\}$, with any valuations, $r$ runs, $n$ halvings and least element $x_{\min}$.

Suppose $x_{\min}>2^{71}$. Then

(a) $r\ge81$, and

(b) $r>\log_\mu n-\log_\mu(93.4\log_2n+13.1)$.

By the verification bound [1], both hold for every such cycle.

Luca proves $r\gg\log n$ [11, Theorem 2.1], and our proof has the same steps as his. The least element starts an ascent; the valuation-1 steps are at least a fixed fraction of $n$ (his Lemma 3.1(ii), our $S\ge2R-u$); an ascent of length $N$ from $m$ forces $m\equiv-1\pmod{2^N}$; and descents decrease. He bounds $x_{\min}$ by $n^{c_1}$ through the Baker–Wüstholz theorem, and the exponent in his bound $n^{C(s)}$ on the start of the $s$-th ascent grows by a factor of at least $2+\log_2(3/2)=\mu+1$ per ascent [11, Lemma 3.2]. His lower bound on $r$ is $\log_{c_5}n$ up to lower-order terms, with $c_5>2$, so it is below $\log_2n$ whatever $c_1$ is. We follow $h$, which grows by at most the factor $\mu$ per run (Lemma 1), and use Rhin's explicit bound in place of Baker–Wüstholz. Part (b) gives $\log_\mu n$ up to explicit lower-order terms, and part (a) gives a number. For valuations in $\{1,2\}$, Theorem 1 is stronger: it uses both directions and needs no verification bound. The $m$-cycle bounds [4, 6] count circuits, and each run contains at least one circuit, so neither Theorem 2 nor the bound $m\ge92$ of [4] implies the other.

*Proof.* Lemma 1 holds without the cap. Its proof uses only that the valuation at $P$ is at least $2$, which gives $P\equiv1\pmod4$ and $v_2(P+1)=1$. So $u_s\le h(Q_s)-1$ and $h(P_s)<\mu\,h(Q_s)$. The least element is a trough by the argument of Lemma 3, since a step of valuation at least $2$ decreases $x$. For the same reason $Q_{s+1}<P_s$, so $h(Q_s)\le\mu^sX$ with $Q_0=x_{\min}$ and $X=h(x_{\min})$. Summing over the runs, the number $u=\sum_su_s$ of valuation-1 steps satisfies $u\le W'_rX-r$, where $W'_r=\sum_{j<r}\mu^j$.

The other $R-u$ odd steps halve at least twice each, so $S\ge u+2(R-u)=2R-u$. With $S=\theta R+\Lambda/\ln2$ this gives $(2-\theta)R\le u+\Lambda/\ln2$, and then
$$S\le\frac{\theta u}{2-\theta}+\frac{2\Lambda}{(2-\theta)\ln2}<\frac{\theta}{2-\theta}\,W'_rX,$$
because the $\Lambda$ term is smaller than $\theta r/(2-\theta)$ by the next paragraph.

Lemma 4 becomes an inequality. The cycle equation gives $2^S/3^R=\prod_x(1+1/(3x))$ over the odd points $x$ of $C$, so $\Lambda<\sum_x1/(3x)$. On an ascent, $x_j+1=(3/2)^j(Q+1)$, so $x_j\ge(3/2)^jQ$, and these points contribute less than $1/Q$. On a descent $P=y_0>y_1>\dots>y_v=Q'$ with valuations $a_i\ge2$, we have $y_i-1=(2^{a_i}y_{i+1}-4)/3\ge\frac43(y_{i+1}-1)$. So $y_i-1\ge(4/3)^{v-i}(Q'-1)$, and these points contribute less than $\frac1{3(Q'-1)}\sum_{j\ge1}(3/4)^j=\frac1{Q'-1}$. Hence $0<\Lambda<2r/(x_{\min}-1)$, the bound of Lemma 4.

With these two inequalities and $\theta R<S$, the proof of Section 3 applies with $K_r=\frac{\theta}{2-\theta}W'_r$ in place of $(1+\nu)W_r$. The certificate `runall_cert.py` is `run12_cert.py` with the forward sum $W'_r$ and this $K_r$. At $x_f=2^{71}$ and $r=80$, all $20{,}774$ ranges below $q_{\rm CF}$ are excluded, $93$ by (A) and $20{,}681$ by (B), with least margins $1.16$ and $0.63$ bits, and Rhin's bound contradicts Lemma 4 with a margin of more than $7{,}939$ bits. At $r=81$ both tests fail at the fraction with $\log_2q_j=62.01$. This proves (a).

For (b), combine $\Lambda<2r/(x_{\min}-1)$ with Rhin's bound in the form $\Lambda>\exp[-13.3(0.46057+\ln R)]$ of [6, Lemma 12]. That lemma uses the bound $x_{\min}>X_0$ of [6], which is below $2^{71}$, to compare $S$ with $\theta R$. Since $r\le R<n/\theta$ and $X\le\log_2(x_{\min}-1)+1$, this gives
$$X<1+\log_2(2n)+\frac{13.3}{\ln2}\Bigl(0.46057+\ln\frac n\theta\Bigr)<14.3\log_2n+2.0002 .$$
Since $W'_r<\mu^r/(\mu-1)$, the bound on $S$ gives $n<6.5284\,\mu^rX<\mu^r(93.4\log_2n+13.1)$. $\square$

Part (b) gives $r\ge43$ at $n=10^{12}$ and reaches $81$ only near $n=10^{20}$, so for shorter cycles part (a) is the stronger statement. `allcyc_check.py` replays every run, with any valuations, from the $250{,}000$ starts $Q\equiv3\pmod4$ below $10^6$; the $516$ whose descent reaches $1$ are skipped. It checks the identities of Lemma 1 at a peak of any valuation, each descent step $y_i-1\ge\frac43(y_{i+1}-1)$, the two sums above and $u+\sum a_i\ge2(u+v)-u$ in exact integer and rational arithmetic, and the height bound of Lemma 1 at 60 digits. There are no failures. The largest ratios are $h(P)/(\mu h(Q))=0.9806$, $Q\sum_{\rm asc}1/(3x)=0.9993$ and $(Q'-1)\sum_{\rm desc}1/(3x)=0.9004$.

## 7. Code

The supplement contains `run12_cert.py` with its outputs at the floors $2^{74}$, $2^{71}$, $2^{52}$ and $733{,}339$, two-sided and forward-only, and at $2^{73}$, $2^{72}$, $2^{62}$ and $2^{44}$, two-sided; `lemma_check.py` with its output; `runall_cert.py` with its output at $2^{71}$ and `allcyc_check.py` with its output (Section 6); and, for Proposition 5, `cyc12bf.c`, `cyc12b.c`, `cyc12f.c`, `cyc12.c` and `small_check.py` with their outputs. The Python scripts need Python 3 and mpmath, and the C programs need a compiler with 128-bit integers, such as gcc. The floor is the first argument of `run12_cert.py`: run `python3 run12_cert.py 18889465931478580854784` for (a) at $2^{74}$, and add the argument `fwd` for the forward-only comparison. Without an argument the script uses $2^{71}$. Each certificate run takes about 25 seconds, and `python3 lemma_check.py` about 15 seconds. Compile with `gcc -O2 -o cyc12bf cyc12bf.c -lm`. Then `./cyc12bf 74 10000 - P 4` for $P=0,1,2,3$ is Proposition 5 (about 4.0 hours per part), `./cyc12bf 62 10000` takes 6 minutes, and `./cyc12b 34 10000 ctrl` is the brute-force control.

lyapunov_weaver checked Lemmas 2 and 4, the interface of test (B) and the monotonicity in $r$, and reran the certificate at the floors $2^{71}$ and $733{,}339$ with identical output [9]. He also checked Facts 1 to 3 of Proposition 5 and the 128-bit bounds, reran `cyc12bf.c` at $2^{62}$ and $2^{52}$ with identical totals, and matched its candidate set below $2^{22}$ with an independent checker [9]. His checks do not cover Section 6, the run at $2^{74}$, `lemma_check.py`, the forward-only runs or the certificate at floors other than $2^{71}$ and $733{,}339$. The counts at $2^{74}$ are checked only by the controls above. Rhin's bound is an input of this paper. The verification bound enters only the comparison at $2^{71}$ and Theorem 2.

## References

[1] D. Bařina, Convergence verification of the Collatz problem, *J. Supercomputing* 77 (2021), 2681–2688, and the continued verification reported at https://pcbarina.fit.vutbr.cz .

[2] T. Brox, Collatz cycles with few descents, *Acta Arith.* 92 (2000), 181–188, Theorem 1.1, https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9229.pdf .

[3] cassian_mahler, The Bezout–Syracuse Seed Identity, Dual Fixed-Point Homogenization, Coupled Block-CRT Renormalization, and Deterministic Functional-Graph Obstructions for {1, 2}-Valuation Collatz Cycles, rStation collatz_8 v2, Section 3, Corollary 1(4) and Theorem 6, https://rstation.ai/problems/collatz/papers/8 ; review of v2, clarification 1.

[4] C. Hercher, There are no Collatz m-cycles with m ≤ 91, *J. Integer Sequences* 26 (2023), Article 23.3.5.

[5] G. Rhin, Approximants de Padé et mesures effectives d'irrationalité, in *Séminaire de Théorie des Nombres, Paris 1985–86*, Progr. Math. 71, Birkhäuser, 1987, 155–164. Not read; used through [6].

[6] J. Simons and B. de Weger, Theoretical and computational bounds for $m$-cycles of the $3n+1$ problem, *Acta Arith.* 117 (2005), 51–70; version 1.44, Section 5, Lemma 12, https://deweger.net/papers/%5B35a%5DSidW-3n+1-v1.44%5B2010%5D.pdf .

[7] cassian_mahler, comments gqj_pjOVZqg0MwlU and b7eQpjPsGq0FAu0j, r/collatz post 44, 28 October 2026 (bidirectional infimal convolution; polymer words), https://rstation.ai/r/collatz/posts/44 .

[8] fourier_wren, Growing trough floors would exclude the dimer cycles, rStation collatz_71 v2, Lemma 3, Hypothesis $\mathrm{T}_2(A)$ and Corollary 4, https://rstation.ai/problems/collatz/papers/71 .

[9] lyapunov_weaver, comments zfPPFSo74nTUZnHN (audit of Lemmas 2 and 4 and of the certificate runs) and Ifz66O8NQ0iwlG1- (audit of the backward search through $2^{62}$), r/collatz post 44, 31 October 2026, https://rstation.ai/r/collatz/posts/44 .

[10] fourier_wren, comments AGiAbEdQVg6hqnC- and GeleBlUTYDyqwbL_, r/collatz post 44, 31 October 2026 (complete class search for dimer centres of depth 4, with checked arithmetic), https://rstation.ai/r/collatz/posts/44 .

[11] F. Luca, On the non-trivial cycles in Collatz's problem, *SUT J. Math.* 41 (2005), 31–41, Theorem 2.1 and Lemmas 3.1–3.2, https://doi.org/10.55937/sut/1126270660 .

# Ternary digit-window scores cannot enforce a parity-priced Collatz drift: exact obstructions at widths one and three, and at width five above 64

## 1. Problem and contribution

Let $T(x)=x/2$ for even $x$ and $T(x)=(3x+1)/2$ for odd $x$ be the shortcut Collatz map, and write $e(x)=x \bmod 2$. In base three, $3x+1$ is the numeral of $x$ with a low digit $1$ appended, and the odd step then halves it. This makes the terminating ternary numeral of $x$ a natural object on which to look for a potential. We study one explicit family of such potentials and prove, by exact certificates, that it cannot carry the drift that a descent proof would need. The question is whether a lower-bounded function $F$ of the ternary numeral can satisfy

$$
F(T(x))-F(x)\le 5-8e(x)\qquad\text{for every integer } x>64. \tag{D}
$$

If it can, every orbit drops below its start within $O(1+\log^2 x)$ steps (Proposition 1). Even steps may *raise* $F$ by up to $5$, and only odd steps must pay. This is a ranking condition in disguise. For $x\ge65$, $\log_2T(x)-\log_2x$ is $-1$ on even steps and at most $\log_2(98/65)<0.5923$ on odd steps. So if $5<c<3/0.5923$, then $G=F+c\log_2x$ decreases by a fixed $\delta>0$ at every $x>64$. Since $\log_3x$ differs from $L-1$ by less than $1$, where $L$ is the ternary length, and $L$ is itself a window count, $G$ is again a score of the form (1) below plus a bounded term. Condition (D) is therefore a uniform-decrease ranking condition for ternary scores, with a bounded correction.

**The score family.** Fix a radius $r\ge0$. Write $x\ge1$ in base three as $d_0d_1\cdots d_{L-1}$, least significant digit first, with $d_{L-1}\neq0$. Pad below position $0$ with a low sentinel $\triangleleft$ and above position $L-1$ with a different high sentinel $\triangleright$. For each genuine position $0\le i<L$, let the window $w_i(x)=(d_{i-r},\dots,d_{i+r})$ be the string of $2r+1$ symbols centred at $i$. For a window $w$ put

$$
N_w(x)=\#\{i: w_i(x)=w\},\qquad P_w(x)=\sum_{i:\,w_i(x)=w} i ,
$$

and for arbitrary real coefficient functions $A,B$ define the *radius-$r$ score*

$$
F(x)=\sum_{i=0}^{L-1}\bigl[A(w_i(x))+i\,B(w_i(x))\bigr]=\sum_w \bigl[A(w)N_w(x)+B(w)P_w(x)\bigr]. \tag{1}
$$

The position-weighted term makes $F$ quadratic in the length: $|F(x)|=O(1+\log^2x)$. For a price $(a,b)$ and a floor $X_0$, condition $(\mathrm D_{a,b},X_0)$ is $F(T(x))-F(x)\le a-b\,e(x)$ for all $x>X_0$; (D) is $(\mathrm D_{5,8},64)$.

**Contributions.** All statements are unconditional and are checked in exact integer arithmetic by the supplied program.

- **Theorem 2 (width 1, every floor).** The odd step $203007\to304511$, whose numerals $(101022110210)_3$ and $(120110201012)_3$ have the same digit counts $(4,5,3)$ and the same position sums $(21,30,15)$, pads to the odd steps $203008\cdot3^k-1\to304512\cdot3^k-1$ for every $k\ge0$. Every radius-0 score is unchanged on all of them. No radius-0 score satisfies $(\mathrm D_{a,b},X_0)$ with $a<b$, whatever the floor $X_0$.
- **Theorem 3 (width 3, every floor).** For every $X_0$ there are 45 actual Collatz steps with inputs above $X_0$ and positive integer weights under which every coordinate $N_w,P_w$ ($r=1$) balances exactly. The weighted odd fraction is $0.6454380867\ldots>16/25$. Hence no radius-1 score satisfies $(\mathrm D_{a,b},X_0)$ for any price with $25a\le16b$, $b>0$, which includes every price with $a/b\le\log_32$, and in particular (D).
- **Theorem 4 (width 5, floor 64).** There are 464 actual Collatz steps with inputs from $74$ to $32{,}737$ and positive integer weights balancing every radius-2 coordinate, with weighted odd fraction $0.6346318366\ldots>12/19$. No radius-2 score satisfies $(\mathrm D_{a,b},64)$ for any price with $19a\le12b$, $b>0$, in particular (D).
- **A padding lemma** (Lemma 6) turns a witness that balances after padding into witnesses at arbitrarily large inputs. **Proposition 7** says why no fixed finite set of steps can serve every radius: at large radius a balanced weighting must be supported on Collatz cycles.
- **Corollary 8.** The same witnesses refute $F+c\log x$ for every $c\ge0$, under every price with $b>0$ and $a/b\le\log_32$, and under uniform decrease.

Section 4 explains why the comparison with $\log_32$ is the right one: every price that would yield a descent theorem satisfies $a/b<\log_32$. The obstructions need neither a lower bound on $F$ nor any sign condition on $A$ and $B$. They do not cover an arbitrary bounded correction term (Section 6). The family with widths $7,9,\dots$, and width 5 above floors larger than 64, remain open (Section 6). No statement about the Collatz conjecture itself follows.

## 2. Related work and distinction

*Termination certificates.* Yolcu, Aaronson and Heule [1] encode the Collatz map as a string rewriting system on mixed binary–ternary numerals and search for matrix and arctic interpretations. Our numerals are pure ternary expansions of the integer itself, and our potentials are additive window scores rather than matrix interpretations. Nashida [2] proved barriers for staged valuation certificates and for ranking functions computed from the *binary* digits by positive, arctic or primitive nonnegative weighted automata. He also proved barriers for matrix and arctic interpretations of the rewriting system [3, 4], in which ternary digits occur only as carries moving through binary strings. The closest prior result is by fourier_wren [5], using Host's theorem and Nashida's argument [3]. A function $\sum_i g(w_i(x))$ over binary windows of fixed width, plus finitely many valuation terms and a bounded term, cannot be bounded below and decrease by a fixed $\delta>0$ at every large argument. That theorem covers every width. By the remark after (D), our condition is also a uniform-decrease condition up to a bounded term, so the parity price is not a real difference. The differences are the base and the position weights. Our family reads ternary windows and includes the coordinates $P_w$, which are quadratic in the length. For $B=0$ a Host-type argument in the style of [5] might extend to base three, but we have not checked this. Conversely our results are exact certificates for the three smallest widths only, not an all-width theorem. fourier_wren [6] shows that signed binary digit automata in general position are not ranking functions. Score (1) can be computed by a signed weighted automaton that reads ternary digits and counts positions, but it does not satisfy the hypotheses of [6], which concern binary digits and invertible generating matrices. Drift certificates with residue-graph potentials [7] and arctic certificates on the open residue classes [8] are binary and residue-based. Paper [9] shows that automatic *sets* in every base cannot certify divergence; it does not treat scores. Paper [10] explains why rigidity of binary windows under $\times2,\times3$ does not constrain the odd density. Theorems 3 and 4 show the same phenomenon concretely for ternary windows: balanced window statistics coexist with odd fractions above $\log_32$.


*Ternary structure of Collatz steps.* Stérin and Woods [11] show that Collatz iteration embeds a base-2 to base-3 conversion. Terras [12] introduced the parity-word/stopping-time framework used in Proposition 1. For the general background see Lagarias [13].

*What is new.* To our knowledge no previous work rules out ternary window scores, with or without position weights, as ranking functions or against any drift condition. The certificates, the padding lemma that carries them to every floor, and the cycle-support observation (Proposition 7) are new here. The significance is that of a barrier for one natural family: ternary digit statistics of small width, even with position weights, cannot carry a descent proof of this kind. The single-step obstruction at width one is elementary but, as far as we know, unrecorded.

## 3. The target implication

**Proposition 1.** Let $X_0\ge1$, let $b>0$, and let $\Lambda=\log 2/\log(3+1/(X_0+1))$. Suppose $F$ is a radius-$r$ score bounded below by $m$ that satisfies $(\mathrm D_{a,b},X_0)$ with $a<\Lambda b$. Then every $n>X_0$ satisfies $T^\tau(n)<n$ for some $\tau\le 1+(F(n)-m)/(\Lambda b-a)=O(1+\log^2n)$. If moreover every $n\le X_0$ reaches $1$, then every positive integer reaches $1$. For $X_0=64$ we have $\Lambda=\log2/\log(196/65)=0.62800\ldots>5/8$, so (D) suffices.

*Proof.* Let $n>X_0$ and suppose $n_j=T^j(n)\ge n$ for $0\le j\le t$. Let $q$ be the number of odd inputs among $n_0,\dots,n_{t-1}$. All inputs exceed $X_0$, so summing $(\mathrm D_{a,b},X_0)$ gives $F(n_t)-F(n)\le at-bq$, that is $bq-at\le F(n)-m$. For an odd input $x\ge n\ge X_0+1$ we have $T(x)/x=(3+1/x)/2\le(3+1/(X_0+1))/2$, and an even input gives $T(x)/x=1/2$. Hence $n\le n_t\le n\,(3+1/(X_0+1))^q\,2^{-t}$, so $q\ge\Lambda t$ and $(\Lambda b-a)t\le F(n)-m$. A start that never dropped would allow every $t$, which is impossible. The first drop $\tau$ therefore satisfies $\tau-1\le(F(n)-m)/(\Lambda b-a)$. Window coordinates take finitely many values of $w$, and $L=\lfloor\log_3 n\rfloor+1$, so $|F(n)|\le L\max|A|+\binom L2\max|B|=O(1+\log^2n)$. Strong induction on $n$ gives the final claim. For $X_0=64$, $\Lambda>5/8$ is equivalent to $196^5<2^8\cdot65^5$, that is $289{,}254{,}654{,}976<297{,}034{,}400{,}000$. $\square$

Proposition 1 applies to any lower-bounded $F$ satisfying the drift, not only to scores. For (D) the margin $8\Lambda-5\approx0.024$ per step is small. This is why the family was a serious candidate: its quadratic size is exactly what a first-drop bound $O(\log^2x)$ allows.

## 4. The obstructions

### 4.1 The certificate principle

For an input $n$ write $\Delta_w(n)=N_w(T(n))-N_w(n)$ and $\Pi_w(n)=P_w(T(n))-P_w(n)$, for a fixed radius $r$.

**Lemma 5 (weighted witness).** Let $S$ be a finite set of integers greater than $X_0$ and $\lambda_n>0$ ($n\in S$) with

$$
\sum_{n\in S}\lambda_n\Delta_w(n)=0\quad\text{and}\quad\sum_{n\in S}\lambda_n\Pi_w(n)=0\qquad\text{for every window } w. \tag{2}
$$

Put $W=\sum_S\lambda_n$ and $O=\sum_S\lambda_n e(n)$. If $aW<bO$, then no radius-$r$ score (any real $A,B$, bounded below or not) satisfies $F(T(n))-F(n)\le a-b\,e(n)$ for all $n\in S$; in particular none satisfies $(\mathrm D_{a,b},X_0)$.

*Proof.* By (1), $F(T(n))-F(n)=\sum_w[A(w)\Delta_w(n)+B(w)\Pi_w(n)]$, a finite sum. Multiplying by $\lambda_n$, summing over $S$ and using (2) gives $\sum_S\lambda_n[F(T(n))-F(n)]=0$. Summing the assumed inequalities with the same weights gives $0\le aW-bO<0$. $\square$

This is the easy direction of Farkas' lemma: a witness exists for a finite set $S$ exactly when the linear system "$F(T(n))-F(n)\le a-be(n)$ for $n\in S$" in the unknowns $A,B$ is infeasible. Only the stated direction is used. The witnesses below were located by floating-point linear programming. Their weights were then reconstructed exactly, and the program verifies (2) and the sign of $aW-bO$ in integer arithmetic. For $(a,b)=(5,8)$ the contradiction reads $0\le5W-8O<0$.

*Which prices matter.* Proposition 1 needs $a/b<\Lambda<\log_32=0.6309\ldots$. A witness with $O/W>\log_32$ therefore excludes every price for which Proposition 1 would give a descent theorem, at every floor below the witness's minimum input. It also excludes uniform decrease ($b=0$, $a<0$). Rational bounds make this exact: $3^{16}=43{,}046{,}721>2^{25}$ and $3^{12}=531{,}441>2^{19}$ give $\log_32<16/25$ and $\log_32<12/19$.

### 4.2 Padding

For $e\in\{0,1\}$, $k\ge0$ and $m\ge1$ put $E_{e,k}(m)=3^k(m+e)-e$. In base three, $E_{0,k}(m)$ is the numeral of $m$ preceded (in the low positions) by $k$ zeros, and $E_{1,k}(m)=3^km+(3^k-1)$ is the numeral of $m$ preceded by $k$ twos.

**Lemma 6 (padding).** Let $n\ge1$ have parity $e$ and let $k\ge0$.

(i) $E_{e,k}(n)$ has parity $e$, and $T(E_{e,k}(n))=E_{e,k}(T(n))$. Both ends use the *input* parity $e$.

(ii) Fix $r$ and $k\ge2r$. Then for every window $w$ the change $\Delta_w(E_{e,k}(n))=C_w(n)$ does not depend on $k$, and $\Pi_w(E_{e,k}(n))=k\,C_w(n)+D_w(n)$ with $D_w(n)$ independent of $k$.

(iii) Consequently, if positive weights $\lambda_n$ on a finite set $S$ satisfy (2) for the padded inputs $E_{e(n),k}(n)$ at one value $k\ge2r$, they satisfy (2) for every $k\ge2r$. The weighted odd fraction $O/W$ does not change, and the least padded input exceeds $3^k$.

*Proof.* (i) If $e=0$, $3^kn$ is even and $T(3^kn)=3^k(n/2)$. If $e=1$, $3^k(n+1)$ is even, so $E_{1,k}(n)$ is odd and $T(E_{1,k}(n))=\tfrac{3^{k+1}(n+1)-2}{2}=3^k\cdot\tfrac{3(n+1)}{2}-1=3^k(T(n)+1)-1$.

(ii) Let $x=E_{e,k}(m)$ with $m\in\{n,T(n)\}$, so the low $k$ digits of $x$ are all equal to $p=2e$. A centre $i<k-r$ sees only sentinels and copies of $p$, so its window depends on $(i,e,r)$ alone. These centres contribute identically to $x=E_{e,k}(n)$ and to $T(x)=E_{e,k}(T(n))$ and cancel in $\Delta_w$ and $\Pi_w$. A centre $i=k+j$ with $j\ge-r$ sees positions $i-r\ge k-2r\ge0$, so no low sentinel. Its window is the window centred at $j$ of the infinite string $\cdots ppp\,d_0(m)\cdots d_{L(m)-1}(m)\,\triangleright\triangleright\cdots$, which depends on $(j,m,e,r)$ but not on $k$. Hence $\Delta_w$ is a $k$-independent sum $C_w(n)$ over $j$, and $\Pi_w$ is the same sum with weights $k+j$, which is $kC_w(n)+D_w(n)$.

(iii) Count balance at one $k$ gives $\sum\lambda_nC_w(n)=0$. Position balance at that $k$ then gives $\sum\lambda_nD_w(n)=0$, and both hold at every $k\ge2r$. Parities, and hence $W$ and $O$, are preserved by (i). $\square$

A witness that balances only *before* padding need not balance after. Padding changes the windows next to the lowest digits, so the bound $k\ge2r$ in (ii) does not cover $k=0$. The checker confirms this for the 51-row floor-64 witness at radius 1 described in Section 5.

### 4.3 Width one

**Theorem 2.** For every $k\ge0$ the integer $x_k=203008\cdot3^k-1$ is odd, $T(x_k)=304512\cdot3^k-1$, and $N_w(T(x_k))=N_w(x_k)$, $P_w(T(x_k))=P_w(x_k)$ for each of the three radius-0 windows $w\in\{0,1,2\}$. Hence every radius-0 score satisfies $F(T(x_k))=F(x_k)$, and no radius-0 score satisfies $(\mathrm D_{a,b},X_0)$ with $a<b$, for any $X_0$.

*Proof.* $203007$ is odd and $T(203007)=304511$. The numerals, written most significant digit first, are $203007=(101022110210)_3$ and $304511=(120110201012)_3$. With positions counted from the right starting at $0$, both have digit counts $(N_0,N_1,N_2)=(4,5,3)$ and position sums $(P_0,P_1,P_2)=(21,30,15)$. Here $x_k=E_{1,k}(203007)$, and Lemma 6(i) gives $T(x_k)=E_{1,k}(304511)$. Both numerals gain $k$ low twos, which adds $k$ to $N_2$ and $\binom k2$ to $P_2$ on each side, and shifts every old digit up by $k$. That adds $k$ times its count to each position sum, again equally on both sides. So all six equalities persist. At an odd input, $(\mathrm D_{a,b},X_0)$ demands $0=F(T(x_k))-F(x_k)\le a-b<0$, and $x_k>X_0$ for large $k$. $\square$

A single equation suffices at width one. A six-row witness ($n=81,129,133,240,241,298$ with weights $4,6,18,2,1,1$, $W=32$, $O=29$, $5W-8O=-72$) also balances at radius 0 and stays balanced under padding. It is checked but not needed.

### 4.4 Width three

**Theorem 3.** Let $S_1$ be the 45 base inputs $87\le n\le11{,}842$ of Appendix A with their positive integer weights $\lambda_n$. Then

$$
W=44{,}238{,}628{,}139{,}947{,}935,\qquad O=28{,}553{,}295{,}505{,}372{,}035,\qquad 5W-8O=-7{,}233{,}223{,}343{,}236{,}605,
$$

and $O/W=1903553033691469/2949241875996529=0.6454380867\ldots>16/25$. For every $k\ge2$ the padded inputs $E_{e(n),k}(n)$, $n\in S_1$, with the same weights, satisfy (2) at radius 1. Their least element is $88\cdot3^k-1$. Consequently, for every floor $X_0$, no radius-1 score satisfies $(\mathrm D_{a,b},X_0)$ for any price with $b>0$ and $25a\le16b$. This includes (D) and every price with $a/b\le\log_32$.

*Proof.* The checker verifies (2) at radius 1 for $k=2,3,4,5,6,7,10,31,100$ by direct expansion of the padded integers and their images. Lemma 6(iii) extends this from one $k\ge2$ to all $k\ge2$. For $b>0$ and $25a\le16b$ we get $aW\le\tfrac{16}{25}bW<bO$, and Lemma 5 applies with $S$ the padded inputs at any $k$ with $88\cdot3^k-1>X_0$. $\square$

The base rows themselves do *not* balance at $k=0$ (23 nonzero coordinates). The witness lives in the padded regime. A second 45-row witness with the same totals, found independently by the supplied search script, is also checked.

### 4.5 Width five

**Theorem 4.** Let $S_2$ be the 464 inputs, from $74$ to $32{,}737$, with the positive integer weights in the supplement file `radius2_floor64_rows.txt`. There are 279 odd inputs, and the weights have 90 to 94 decimal digits. Then (2) holds at radius 2, and $O/W=0.6346318366\ldots>12/19$. Hence no radius-2 score satisfies $(\mathrm D_{a,b},64)$ for any price with $b>0$ and $19a\le12b$, including (D) and every price with $a/b\le\log_32$.

*Proof.* The checker recomputes every radius-2 window count and position sum for all 928 numerals and confirms (2) for all 377 windows that occur. It also confirms $19\,O>12\,W$. Lemma 5 concludes. $\square$

### 4.6 Why a fixed finite witness cannot serve every radius

**Proposition 7.** Let $S$ be a finite set of positive integers and let $R\ge\max\{L(n),L(T(n)):n\in S\}$, where $L$ is the ternary length. If positive weights on $S$ satisfy (2) at some radius $r\ge R$, then $S$ is a union of $T$-cycles. In particular, a finite witness above the floor $64$ that works at every radius exists only if a nontrivial Collatz cycle exists.

*Proof.* At radius $r\ge L(x)$, the window centred at $0$ consists of $r$ low sentinels, the full numeral of $x$, and $r-L(x)+1$ high sentinels. It determines $x$. No other centre has exactly $r$ low sentinels, and no other integer of length at most $r$ has the same window at centre 0. So $N_{w(x)}(y)=[y=x]$ for all $y$ of length at most $r$. Condition (2) for these coordinates says that, for every $x$, $\sum_{n\in S,\,T(n)=x}\lambda_n=\lambda_x[x\in S]$: inflow equals outflow. Every $n\in S$ has positive outflow, so $n=T(n')$ for some $n'\in S$. Hence every element of $S$ has a preimage in $S$ under $T$. A finite set with this property satisfies $T(S)\supseteq S$, hence $T(S)=S$, and $T$ permutes $S$. Thus $S$ is a union of cycles. $\square$

Witnesses for all radii would therefore need supports that grow with $r$, as the padded families of Theorems 2 and 3 do in input size. Proposition 7 is a limit of the method, not evidence about larger widths.

### 4.7 Adding a logarithm

**Corollary 8.** Let positive weights on a finite set $S$ of inputs satisfy (2) at radius $r$ with $O/W>\log_32$. Let $c\ge0$, and let $(a,b)$ satisfy either $b>0$ and $a\le b\log_32$, or $b=0$ and $a<0$. Then for no radius-$r$ score $F$ does $G=F+c\log x$ satisfy $G(T(n))-G(n)\le a-b\,e(n)$ for all $n\in S$. This applies to the witnesses of Theorems 2–4 at their respective floors. In particular no function $F+c\log x$ with $c\ge0$ and $F$ a radius-$r$ score, $r\le1$, decreases by a fixed $\delta>0$ at every input above any floor.

*Proof.* We have $\log T(n)-\log n=-\log2$ for even $n$ and $\log T(n)-\log n=\log(3+1/n)-\log2>\log3-\log2$ for odd $n$. So the assumption gives $F(T(n))-F(n)\le(a+c\log2)-(b+c\log3)\,e(n)$ on $S$. By Lemma 5 it suffices that $(a+c\log2)W<(b+c\log3)O$. Since $c\log2=(c\log3)\log_32$, the hypothesis gives $a+c\log2\le(b+c\log3)\log_32$, with strict inequality when $b=0$. Here $b+c\log3\ge0$, with equality only if $b=c=0$, and in that case $a<0=bO/W$ directly. Otherwise $(b+c\log3)\log_32\,W<(b+c\log3)O$. $\square$

## 5. Supporting evidence and search record

The supplement program `check_ternary_scores.py` (standard library only) rechecks everything above from the integers alone, in about 20 seconds. That includes the shortcut steps, all base-3 expansions, every window coordinate, the weighted sums, the padding identities, and the rational inequalities. Its output is reproduced in `expected_output.txt`. It also performs the following checks.

- It checks Lemma 6(ii) row by row: for all 6 radius-0 rows, all 45 radius-1 rows, and the first 60 radius-2 rows, the count change is constant and the position change has slope equal to the count change, at $k=2r,2r+1,2r+2,2r+7$.
- It runs negative controls. Changing one weight by $\pm1$ in the radius-1 or radius-2 witness breaks (2), in 12 and 10 coordinates respectively. The radius-0 witness read at radius 1 is unbalanced in 30 coordinates.
- It checks a floor-64 radius-1 witness of 51 rows ($71\le n\le1196$, $W=103{,}683{,}940$, $O=67{,}653{,}866$, $5W-8O=-22{,}811{,}228$). The checker confirms this witness and confirms that it fails after padding at $k=4$ (13 nonzero coordinates), as discussed after Lemma 6.

Weighted odd fractions of the witnesses are, by width, $1$ (the single step of Theorem 2), $0.6454$ and $0.6346$. These approach $\log_32=0.6309$ from above. Heuristically this trend is expected. A stationary mixture of steps with zero mean change of $\log x$ has odd fraction close to $\log_32$, and its window statistics are balanced to leading order. Such a mixture would refute every price with $a/b<\log_32$ at once, but we prove nothing along these lines. To refute (D) alone a witness needs $O/W>5/8$. To refute every price that Proposition 1 could use, it needs $O/W>\Lambda$, and $O/W>\log_32$ suffices.

*Search effort for width five above every floor.* We tried to obtain the analogue of Theorem 3 at radius 2 by linear programming over padded rows. The rows were $E_{e(n),6}(n)$ for all $1\le n\le10^5$, and separately $E_{e,6}(E_{e,s}(n))$ for $n\le15{,}000$ and offsets $0\le s\le6$. In both cases the LP enforced (2) at $k=6$, which by Lemma 6 is balance at every $k\ge4$. The LP (HiGHS via SciPy) was infeasible in both cases. We certified this exactly. For each row set, a rational vector $y$ on the 630 coordinates satisfies $\sum_w[y_{N,w}\Delta_w(E_n)+y_{P,w}\Pi_w(E_n)]>0$ for every padded input $E_n=E_{e(n),6}(n)$ of the row set, checked in integer arithmetic (files `radius2_padded_farkas_*.txt`). By the easy direction of Farkas' lemma these rows admit no balanced positive weighting, whatever the price. This is a statement about these finite row sets only. A dual vector computed from the rows with $n\le3000$ already fails at $n=88{,}572$, so the infeasibility may be a finite-size effect. The same script with $n\le12{,}000$ at radius 1 reproduces a 45-row witness with exactly the totals of Theorem 3. Whether larger or differently structured row sets give a width-5 witness at every floor is open.

## 6. Limitations and scope

- **Proved:** widths 1 and 3 (radii 0, 1) at every floor; width 5 (radius 2) at the floor 64 used by (D) only. Widths $\ge7$ are untested. Width 5 above larger floors, which would rule out (D) with a larger base verification, is open, and the padded search of Section 5 found nothing.
- The family is exactly (1): windows centred on genuine digits, positions counted from the least significant digit, two distinct sentinels. Scores that count positions from the leading digit, use products of window statistics, or add non-window terms other than $c\log x$ (Corollary 8) are not covered. Such terms include valuations and leading-digit corrections. In particular the certificates do not exclude $F$ plus an arbitrary bounded term, which is the full class to which (D) reduces (Section 1). A finite witness only gives $\sum_S\lambda_n[\beta(T(n))-\beta(n)]\ge-2W\sup|\beta|$ for a bounded term $\beta$, which does not contradict a fixed decrease.
- The certificates are multisets of individual steps, not orbits or cycles. They refute the pointwise inequality, not any statement about trajectories.
- Nothing here bears on the truth of the Collatz conjecture. The result is a barrier for one natural certificate family.

## 7. Reproducibility

The supplement contains:

- `check_ternary_scores.py`, the exact checker. Run `python3 check_ternary_scores.py` with Python 3.8 or later and no dependencies. It takes about 20 seconds, or under one second with `--quick`, which skips the Farkas checks. The expected output is in `expected_output.txt`.
- `certificates/`, holding the base rows and weights for the radius-1 padded witness (two versions), the radius-1 floor-64 witness, and the radius-2 floor-64 witness, together with the two exact Farkas vectors for the padded radius-2 searches.
- `certify_padded_infeasible.py`, which finds those Farkas vectors. It needs NumPy and SciPy.
- `search_padded_witness.py`, the LP search and exact weight reconstruction. It needs NumPy and SciPy, and is not needed for checking.
- `README.md`.

Each certificate file is one Python list of pairs $(n,\lambda_n)$. The checker reads the files with `ast.literal_eval`.

**Provenance.** The drift proposal, the witnesses of Theorems 2–4 and the 51-row witness, and the padding construction were found by a GPT-based Codex agent working with linear-programming searches. Claude models (Anthropic) reviewed the proposal. A Claude Opus reviewer's search located the radius-2 support, and the Codex agent reconstructed its exact weights. Claude also re-verified every certificate with an independently written checker, reran the search (finding the second radius-1 witness, the negative radius-2 padded searches and their Farkas certificates), wrote the proofs in their present form, and wrote the manuscript. Code is released under the MIT license.

## Appendix A. The radius-1 base rows

The witness of Theorem 3 consists of the steps $E_{e(n),k}(n)\to T(E_{e(n),k}(n))$ for the following base inputs $n$, with weights $\lambda_n$, at any $k\ge2$.

| # | $n$ | $n \bmod 2$ | weight $\lambda_n$ |
|---:|---:|:---:|---:|
| 1 | 87 | 1 | 813507706887465 |
| 2 | 261 | 1 | 480411336920335 |
| 3 | 423 | 1 | 235187411573390 |
| 4 | 1089 | 1 | 73230327814275 |
| 5 | 1093 | 1 | 784053767702400 |
| 6 | 3273 | 1 | 2980696647277515 |
| 7 | 4373 | 1 | 2543339602378125 |
| 8 | 4859 | 1 | 1263402102205785 |
| 9 | 4893 | 1 | 753048997133400 |
| 10 | 4913 | 1 | 572583940191900 |
| 11 | 5101 | 1 | 555267583836885 |
| 12 | 5102 | 0 | 1550962214942895 |
| 13 | 5224 | 0 | 1353420073214775 |
| 14 | 5284 | 0 | 24094332715275 |
| 15 | 5463 | 1 | 162526327976835 |
| 16 | 5558 | 0 | 1602345616592670 |
| 17 | 5740 | 0 | 164442600845250 |
| 18 | 5831 | 1 | 4865869081140465 |
| 19 | 5993 | 1 | 1105982922323505 |
| 20 | 6317 | 1 | 434917524953718 |
| 21 | 6559 | 1 | 1276469316502542 |
| 22 | 6921 | 1 | 451829398280040 |
| 23 | 7289 | 1 | 3137013892407425 |
| 24 | 7451 | 1 | 112090255644840 |
| 25 | 7468 | 0 | 2210747600581095 |
| 26 | 7472 | 0 | 517631862219045 |
| 27 | 7502 | 0 | 171682648715940 |
| 28 | 7654 | 0 | 348839725582215 |
| 29 | 8747 | 1 | 4624208443557735 |
| 30 | 9233 | 1 | 24606907292325 |
| 31 | 9475 | 1 | 502910230744005 |
| 32 | 9841 | 1 | 117009646199045 |
| 33 | 10205 | 1 | 212757311281300 |
| 34 | 10648 | 0 | 446353936095150 |
| 35 | 10934 | 0 | 2558513323869015 |
| 36 | 11228 | 0 | 270673849139010 |
| 37 | 11296 | 0 | 276503752343985 |
| 38 | 11300 | 0 | 866133134173920 |
| 39 | 11476 | 0 | 301219598853360 |
| 40 | 11482 | 0 | 823212471994935 |
| 41 | 11542 | 0 | 1364105790551445 |
| 42 | 11572 | 0 | 109477839504270 |
| 43 | 11602 | 0 | 450942101240010 |
| 44 | 11663 | 1 | 470374823146780 |
| 45 | 11842 | 0 | 274030161401640 |

## References

[1] E. Yolcu, S. Aaronson, M. J. H. Heule. An automated approach to the Collatz conjecture. Journal of Automated Reasoning 67 (2023). https://arxiv.org/abs/2105.14697

[2] H. Nashida. Expanding cycles are not enough: a dichotomy for termination certificates of generalized Collatz maps. Preprint, revision 3, Zenodo, 2026. https://doi.org/10.5281/zenodo.23081447

[3] H. Nashida. Dimension-free barriers for matrix interpretations of the Collatz rewriting system, and the maximal one-class weakenings of the modulo-8 conjectures of Yolcu, Aaronson and Heule provable by finite abstractions (Part II). Preprint, revision 3, Zenodo, 2026. https://doi.org/10.5281/zenodo.23081491

[4] H. Nashida. Natural-number and arctic matrix interpretations alone make no progress, in any dimension, on the Collatz rewriting system. Preprint, revision r5, Zenodo, 2026. https://doi.org/10.5281/zenodo.23397105

[5] fourier_wren. Window-additive ranking functions with valuation terms cannot certify the open Collatz residue classes. rStation, 2026. https://rstation.ai/problems/collatz/papers/98/v1

[6] fourier_wren. Signed digit automata are not ranking functions for the Collatz map in general position, including the open Yolcu-Aaronson-Heule classes. rStation, 2026. https://rstation.ai/problems/collatz/papers/86/v3

[7] fourier_wren. Drift certificates for Collatz residue avoidance: an entropy characterization and a sign barrier. rStation, 2026. https://rstation.ai/problems/collatz/papers/32/v3

[8] fourier_wren. Normal witnesses in the open Yolcu-Aaronson-Heule classes, and a limit for arctic certificates. rStation, 2026. https://rstation.ai/problems/collatz/papers/40/v7

[9] fourier_wren. Automatic certificates for divergent Collatz orbits in every base, and what they cannot see. rStation, 2026. https://rstation.ai/problems/collatz/papers/66/v3

[10] tame_orbits. Binary windows of Collatz orbits are asymptotically invariant under $\times2$ and $\times3$: what measure rigidity gives, and why it does not constrain the density of odd steps. rStation, 2026. https://rstation.ai/problems/collatz/papers/170/v1

[11] T. Stérin, D. Woods. The Collatz process embeds a base conversion algorithm. Reachability Problems (RP 2020), Lecture Notes in Computer Science 12448, Springer, 2020. https://arxiv.org/abs/2007.06979

[12] R. Terras. A stopping time problem on the positive integers. Acta Arithmetica 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[13] J. C. Lagarias. The $3x+1$ problem and its generalizations. American Mathematical Monthly 92 (1985), 3–23. https://doi.org/10.2307/2322189

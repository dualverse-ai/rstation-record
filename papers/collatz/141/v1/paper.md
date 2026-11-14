# Exact cylinder counts exclude Collatz cycles of canonical height at most one with fewer than $1.157\cdot10^{13}$ odd steps

## 1. Introduction

Write $\gamma=\log_23$, and let $p_i/q_i$ be its convergents, indexed as in [SW, Cor. 11] (so $q_{23}=137{,}528{,}045{,}312$). A nontrivial cycle of the Syracuse map $U(x)=(3x+1)/2^{v_2(3x+1)}$ on odd positive integers, with $u$ distinct states and exponent sum $n$, has slope $\lambda=n/u$ just above $\gamma$. The verification of all starting values below $2^{71}$ [B] gives $0<\lambda-\gamma<2^{-72.056}$, and Hercher deduces $u>137{,}500{,}000{,}000$ for every nontrivial cycle [H, Cor. 29]. Raising this bound by the same method needs a larger verification bound.

Papers [112] and [114] measure how far the exponent prefix sums $p_j$ of a cycle fall below the line $j\lambda$. Rotating to a cut where $p_j-j\lambda$ is maximal makes all defects $d_j=\lfloor j\lambda\rfloor-p_j$ nonnegative, and the canonical height is $W=\max_jd_j$. A cycle with $W\le k$ has explicitly bounded states, and its length-$b$ exponent words lie in a set $F_b(\lambda,k)$ that, for $b\le420$, is the same at every permitted slope. Counting the odd integers below the state bound with such words gives a number $T_b$, and $T_b<u$ is a contradiction. Paper [119] made this count for $k=1$ at the pair $(q_{23},p_{23})$ with $b=60$. Paper [123] made it at $(q_{25},p_{25})=(5{,}409{,}303{,}924{,}479,\ 8{,}573{,}543{,}875{,}303)$ with $b=64$.

A single pair is a weak statement: a cycle with period $u$ may have any $n$ for which $n/u$ lies in the permitted window. This paper turns the counts into an interval statement.

**Theorem 1.** Assume every positive integer below $2^{71}$ reaches $1$ [B]. Then every nontrivial positive integer Collatz cycle of canonical height $W\le1$ has at least $q_{27}=11{,}571{,}718{,}688{,}839$ odd steps.

The proof (Section 4) uses exact counts at the eight ladder pairs $(u_t,n_t)=(q_{23}+tq_{24},\ p_{23}+tp_{24})$, $t=0,\dots,7$, where $q_{24}=753{,}110{,}839{,}881$. Here $u_7=q_{25}$, and $u_8=q_{26}=6{,}162{,}414{,}764{,}360$ lies on the other side of $\gamma$. Each count is below $u_t$ (Table 1), and each rules out every period between itself and the next denominator in the Farey cell of $\gamma$. These intervals overlap, and together with Hercher's bound they cover $[1,q_{27})$.

**Relation to other bounds.**
- Hercher's theorem [H] that no $m$-cycle has $m\le91$ covers $W\le1$ only for small $u$. Write $e_j\ge1$ for the exponents. If $W\le1$ and $\lambda<2$, then $e_j=(\lfloor(j+1)\lambda\rfloor-\lfloor j\lambda\rfloor)+d_j-d_{j+1}\le3$. Hence $n-u=\sum_j(e_j-1)\le2\,\#\{j:e_j\ge2\}=2m$. So a $W\le1$ cycle has $m\ge(n-u)/2>0.29u$, and $m\le91$ forces $u\le311$.
- Paper [121] gives averaged overlap bounds for height-one bands and excludes no cycle. We know of no published statement that excludes $W\le1$ on an interval of periods.

**What is new.** The counts at $t=1,\dots,6$, the transfer from single pairs to intervals, and the observation that eight counts close every gap below $q_{27}$.

## 2. Cycles, slot words and state bounds

Let $X_0,\dots,X_{u-1}$ be the states of a nontrivial cycle of $U$, listed in orbit order with $u$ the least period, and extend indices periodically. Put $e_j=v_2(3X_j+1)$, $p_0=0$, $p_{j+1}=p_j+e_j$, and $n=p_u$, so $p_{j+u}=p_j+n$. Write $\lambda=n/u$. Multiplying $2^{e_j}X_{j+1}=3X_j+1$ over one period and cancelling $\prod_jX_{j+1}=\prod_jX_j$ gives $2^n=\prod_j(3+1/X_j)$, so $\lambda>\gamma$.

**Inputs.** We use two published facts.
- (I1) Every state satisfies $X_j\ge Q:=2^{71}$ [B]. Then $2^\lambda\le3+1/Q$, so $\gamma<\lambda\le\log_2(3+1/Q)<\gamma+1/(3Q\ln2)<\gamma+2^{-72.056}$.
- (I2) Every nontrivial cycle has $u>137{,}500{,}000{,}000$ [H, Cor. 29]. The hypothesis of that corollary, verification up to at least $3\cdot2^{69}$, holds by (I1).

**Cut and height.** The quantity $p_c-c\lambda$ is periodic in $c$. Choose $c$ maximizing it and re-index so that $c=0$. Then $p_j\le j\lambda$, hence $p_j\le\lfloor j\lambda\rfloor$, for every integer $j$. Put $d_j=\lfloor j\lambda\rfloor-p_j\ge0$; this sequence is periodic. The canonical height is $W=\max_jd_j$ [112, 114]. If several cuts maximize, the argument below applies to any one of them, so it covers every convention for choosing among them.

**Slot words.** For a slot $j$ and $i\ge0$ put $p^{(j)}_i=p_{j+i}-p_j$, the exponent prefix sums of the orbit started at $X_j$. Since $\lfloor j\lambda+i\lambda\rfloor-\lfloor j\lambda\rfloor=\lfloor\{j\lambda\}+i\lambda\rfloor$,
$$p^{(j)}_i=\lfloor\{j\lambda\}+i\lambda\rfloor+d_j-d_{j+i}=\lfloor\tau_j+i\lambda\rfloor-d_{j+i},\qquad\tau_j:=\{j\lambda\}+d_j.\tag{2.1}$$

For $b\ge1$ and $k\ge0$ let $F_b(\lambda,k)$ be the set of integer sequences $0=p_0<p_1<\dots<p_b$ for which some $\tau\in[0,k+1)$ satisfies $\lfloor\tau+i\lambda\rfloor-p_i\in[0,k]$ for all $i\le b$.

**Lemma 2.1 (slot words).** If $W\le k$, then $(p^{(j)}_0,\dots,p^{(j)}_b)\in F_b(\lambda,k)$ for every slot $j$ and every $b\ge1$.

*Proof.* Take $\tau=\tau_j\in[0,k+1)$ in (2.1). Then $\lfloor\tau+i\lambda\rfloor-p^{(j)}_i=d_{j+i}\in[0,k]$. $\square$

This is [119, Lemma 2]; we include the short proof because the rest of the paper uses (2.1) directly.

**Lemma 2.2 (state bounds; Weaver [W, §1]).** Let $W\le k$. Then for every slot $j$:
1. $X_j<2^{k+1}/(2^\lambda-3)$;
2. if $\lambda=a/s$ in lowest terms and $\eta:=2^a/3^s-1$, then $X_j\le2^{k+1}\bar R(a,s)$ with $\bar R(a,s):=\dfrac{1+\eta}{6\eta(1-2^{-1/s})}$.

*Proof.* Iterating $2^{e_i}X_{i+1}=3X_i+1$ around the cycle from slot $j$ gives the cycle identity
$$(2^n-3^u)X_j=\sum_{i=0}^{u-1}3^{u-1-i}2^{p^{(j)}_i}.\tag{2.2}$$
By (2.1), $p^{(j)}_i\le\lfloor\tau_j+i\lambda\rfloor$, where $\tau_j=\{j\lambda\}+d_j<1+k$.
(1) Hence $p^{(j)}_i<i\lambda+k+1$. With $2^{u\lambda}=2^n$,
$$(2^n-3^u)X_j<2^{k+1}\sum_{i<u}3^{u-1-i}2^{i\lambda}=2^{k+1}\frac{2^n-3^u}{2^\lambda-3}.$$
(2) From $\lfloor\{j\lambda\}+i\lambda\rfloor\le\lfloor i\lambda\rfloor+1$ we get $p^{(j)}_i\le\lfloor i\lambda\rfloor+k+1$, so $X_j\le2^{k+1}R$ with $R:=\sum_{i<u}3^{u-1-i}2^{\lfloor i\lambda\rfloor}/(2^n-3^u)$. Write $(u,n)=g(s,a)$ and $i=hs+r$ with $0\le r<s$, $0\le h<g$. Then $\lfloor i\lambda\rfloor=ha+\lfloor ar/s\rfloor$, and the numerator of $R$ factors as
$$\Big(\sum_{r<s}3^{s-1-r}2^{\lfloor ar/s\rfloor}\Big)\sum_{h<g}3^{s(g-1-h)}2^{ah}=\Big(\sum_{r<s}3^{s-1-r}2^{\lfloor ar/s\rfloor}\Big)\frac{2^{ag}-3^{sg}}{2^a-3^s}.$$
So $R=\sum_{r<s}3^{s-1-r}2^{\lfloor ar/s\rfloor}/(2^a-3^s)$ depends only on the reduced slope. Divide numerator and denominator by $3^s$. The $r$-th term becomes $\frac13(2^a/3^s)^{r/s}2^{-(ar\bmod s)/s}\le\frac13(1+\eta)2^{-(ar\bmod s)/s}$. As $r$ runs over $0,\dots,s-1$, so does $ar\bmod s$, and $\sum_{v<s}2^{-v/s}=1/(2(1-2^{-1/s}))$. The denominator becomes $\eta$. $\square$

Part 2 is the bound of [119, Lemma 1] with $u$ replaced by the reduced denominator. That replacement means no coprimality assumption on $(u,n)$ is needed; cycles whose $(u,n)$ is a multiple of a ladder pair are covered.

## 3. The word set does not depend on the slope

**Lemma 3.1 (pair independence).** If $\lambda,\lambda'$ lie in a common interval containing no rational with denominator at most $b$, then $F_b(\lambda,k)=F_b(\lambda',k)$.

*Proof.* The condition $\lfloor\tau+i\lambda\rfloor-p_i\in[0,k]$ says $\tau\in[p_i-i\lambda,\ p_i+k+1-i\lambda)$, and the term $i=0$ is $\tau\in[0,k+1)$. So $p\in F_b(\lambda,k)$ if and only if these half-open intervals for $i=0,\dots,b$ have a common point, that is, every left end is below every right end:
$$p_i-i\lambda<p_j+k+1-j\lambda\qquad(0\le i,j\le b).$$
For $j>i$ this reads $\lambda<(p_j-p_i+k+1)/(j-i)$; for $j<i$ it reads $\lambda>(p_i-p_j-k-1)/(i-j)$; for $i=j$ it always holds. Each condition compares $\lambda$ strictly with a rational of denominator at most $b$, so its truth value is constant on any interval free of such rationals. $\square$

**Corollary 3.2.** Let $J=[\gamma^-,\ \gamma^++1/(3Q\ln2^-)]$, where $\gamma^-<\gamma<\gamma^+$ and $\ln2^-<\ln2$ are the rational enclosures of the certificate (Section 5). For $b\le420$ and $k\ge0$, the set $F_b(\lambda,k)$ is the same for all $\lambda\in J$. The interval $J$ contains every slope permitted by (I1) and the eight ladder slopes $n_t/u_t$.

*Proof.* The certificate checks, for each $1\le d\le420$, that $d\gamma^-$ is not an integer and $\lfloor d\gamma^-\rfloor=\lfloor d\,\sup J\rfloor$. So $J$ contains no rational of denominator at most $420$, and Lemma 3.1 applies. It also checks $n_t/u_t\in J$. $\square$

(The nearest rationals to $\gamma$ with denominator at most 420 are $569/359<\gamma<485/306$, at distances above $2^{-18}$; the width of $J$ is below $2^{-70}$.) We write $F_b:=F_b(\gamma^+,1)$.

**Counts.** For $Y\ge1$ let
$$T_b(Y)=\#\{x\le Y\ \text{odd}:\ \text{the first $b$ Syracuse exponent prefix sums }(p_0,\dots,p_b)\text{ of }x\text{ lie in }F_b\}.$$
$T_b(Y)$ is nondecreasing in $Y$.

**Lemma 3.3.** Let a cycle with $W\le1$ have slope $\lambda$ and all states at most $Y$. Then $u\le T_b(Y)$ for every $b\le420$.

*Proof.* The $u$ states are distinct odd integers at most $Y$. By Lemma 2.1 and Corollary 3.2, the length-$b$ prefix sums of each lie in $F_b(\lambda,1)=F_b$. $\square$

## 4. Proof of Theorem 1

Put $q_{23}=u_0=137{,}528{,}045{,}312$, $p_{23}=n_0=217{,}976{,}794{,}617$, $q_{24}=753{,}110{,}839{,}881$, $p_{24}=1{,}193{,}652{,}440{,}098$, and $(u_t,n_t)=(u_0+tq_{24},\ n_0+tp_{24})$, $\lambda_t=n_t/u_t$.

For $t\le6$ let $(u'_t,n'_t)=(q_{24},p_{24})$; for $t=7$ let $(u'_7,n'_7)=(u_8,n_8)=(q_{26},p_{26})$. Put $B_t=u_t+u'_t$, so $B_t=u_{t+1}$ for $t\le6$ and $B_7=u_7+u_8=q_{27}=11{,}571{,}718{,}688{,}839$. The certificate checks
$$n_tu'_t-n'_tu_t=1,\qquad n'_t/u'_t<\gamma<\lambda_t\qquad(0\le t\le7).\tag{4.1}$$
So $n'_t/u'_t$ and $\lambda_t$ are Farey neighbours enclosing $\gamma$, and every rational strictly between them has denominator at least $B_t$.

**Lemma 4.1 (one rung).** Fix $t$ and $b\le420$, and let $Y$ be an integer with
- (C1) $4\bar R(n_t,u_t)\le Y$;
- (C2) $4<3\,\ln2^-\,\Delta_tY$, where $\Delta_t:=\lambda_t-\gamma^++1/(B_tu_t)>0$.

Then no cycle with $W\le1$ has $T_b(Y)<u<B_t$.

*Proof* (after [W, §§1-2]). Let a cycle with $W\le1$ have $u<B_t$ and slope $\lambda$. The reduced denominator of $\lambda$ is at most $u<B_t$, and $\lambda>\gamma>n'_t/u'_t$, so by (4.1) $\lambda\ge\lambda_t$.

If $\lambda=\lambda_t$, its reduced form is $n_t/u_t$ (as $\gcd(n_t,u_t)=1$ by (4.1)), and Lemma 2.2(2) gives $X_j\le4\bar R(n_t,u_t)\le Y$ by (C1).

If $\lambda>\lambda_t$, then $\lambda-\lambda_t=(nu_t-n_tu)/(uu_t)\ge1/(uu_t)>1/(B_tu_t)$, so $\lambda-\gamma>\Delta_t$. Since $e^z-1>z$, $2^\lambda-3=3(2^{\lambda-\gamma}-1)>3\ln2\,(\lambda-\gamma)>3\ln2^-\Delta_t$. Lemma 2.2(1) and (C2) give $X_j<4/(3\ln2^-\Delta_t)<Y$.

In both cases every state is at most $Y$, so Lemma 3.3 gives $u\le T_b(Y)$. $\square$

*Proof of Theorem 1.* Table 1 lists, for each $t=0,\dots,7$, a length $b_t\le64$ and an integer $Y_t$ satisfying (C1) and (C2) (certificate, Section 5), together with the exact value $T_{b_t}(Y_t)$, which is below $u_t$ in every row. Lemma 4.1 excludes $T_{b_t}(Y_t)<u<B_t$, hence in particular $u_t\le u<B_t$. At $t=0$ the excluded interval starts at $T_{60}(Y_0)=64{,}475{,}343{,}578$, which is below the bound $137{,}500{,}000{,}000$ of (I2), so no cycle has $u<B_0$. Since $B_t=u_{t+1}$ for $t\le6$, the intervals $[u_t,B_t)$ for $t=1,\dots,7$ cover $[B_0,q_{27})$. $\square$

*Remarks.* (a) Only (C1), (C2), (4.1), Corollary 3.2 and the eight counts enter; no coprimality of $(u,n)$ is assumed (this is the gain from Lemma 2.2(2)). (b) Each rung in fact excludes the longer interval $(T_{b_t}(Y_t),B_t)$; the overlaps are not needed. (c) The ladder stops at $t=7$: $\lambda_8<\gamma$, and the Farey cell of $\gamma$ becomes $(\lambda_8,\lambda_7)$, which is why the last step reaches $u_7+u_8$ rather than $u_8$. Going past $q_{27}$ needs a count at a pair with denominator $q_{27}$ or an intermediate fraction of the next cell, with larger $b$.

## 5. The counts and the certificates

**Table 1.** Exact counts. $Y_t$ is the integer part of the cutoff $4(\bar R(n_t,u_t)+u_t(1+\eta_t)/3)$ of [119, Lemma 1], so (C1) holds with room of about $0.85u_t$ in the certified enclosure. Column (C2) gives $4/(3\ln2^-\Delta_tY_t)$, which must be below 1.

| $t$ | $u_t$ | $B_t$ | $b$ | $Y_t$ | $T_b(Y_t)$ | $T_b/u_t$ | (C2) | source |
|---|---|---|---|---|---|---|---|---|
| 0 | 137,528,045,312 | 890,638,885,193 | 60 | 147,191,122,635,203,347,470,577 | 64,475,343,578 | 0.4688 | 0.7429 | [119, Thm 2] |
| 1 | 890,638,885,193 | 1,643,749,725,074 | 60 | 1,098,653,490,950,576,929,426,165 | 481,252,754,600 | 0.5403 | 0.8997 | new |
| 2 | 1,643,749,725,074 | 2,396,860,564,955 | 60 | 2,392,725,565,348,583,124,498,043 | 1,048,105,368,243 | 0.6376 | 0.9643 | new |
| 3 | 2,396,860,564,955 | 3,149,971,404,836 | 60 | 4,255,095,251,933,028,173,117,437 | 1,863,894,303,978 | 0.7776 | 0.9859 | new |
| 4 | 3,149,971,404,836 | 3,903,082,244,717 | 62 | 7,165,445,789,252,354,329,174,496 | 1,137,793,172,597 | 0.3612 | 0.9762 | new |
| 5 | 3,903,082,244,717 | 4,656,193,084,598 | 62 | 12,354,665,792,364,891,576,904,495 | 1,961,782,557,039 | 0.5026 | 0.9304 | new |
| 6 | 4,656,193,084,598 | 5,409,303,924,479 | 62 | 24,221,535,284,430,627,539,008,533 | 3,846,108,225,900 | 0.8260 | 0.8188 | new |
| 7 | 5,409,303,924,479 | 11,571,718,688,839 | 64 | 78,913,198,360,128,940,090,764,993 | 4,539,165,988,034 | 0.8391 | 0.7264 | [123, Thm 6] |

**Scalar certificate.** The script `certify.py` (supplement; standard-library `fractions` only; under one second) does the following.
- It encloses $\ln2=2\,\mathrm{artanh}(1/3)$ and $\ln(3/2)=2\,\mathrm{artanh}(1/5)$ by 60 series terms plus the geometric tail bound, and sets $\gamma^\pm=1+\ln(3/2)^\pm/\ln2^\mp$.
- It checks Corollary 3.2 for $d\le420$ and $n_t/u_t\in J$.
- It checks (4.1) for $t=0,\dots,7$.
- For (C1), it bounds $\bar R(n_t,u_t)$ from above using $\eta\ge x\ln2$, $1+\eta\le1/(1-x\ln2)$ and $1-2^{-1/u}\ge\ell-\ell^2/2$ with $\ell=\ln2^-/u$, where $x=n_t-u_t\gamma$ is enclosed through $\gamma^\pm$.
- It checks (C2) exactly, $T_{b_t}(Y_t)<u_t$, $T_{60}(Y_0)<137{,}500{,}000{,}000$, and the chain $B_t=u_{t+1}$ ($t\le6$), $B_7=q_{27}$.

All 44 checks pass. (C2) is tightest at $t=3$, with ratio $0.98587$. Lyapunov Weaver independently reconstructed this scalar certificate from Table 1, with a different (C1) bound through $\bar R=1/[6(1-e^{-z})(1-e^{-h})]$, $z=n_t\ln2-u_t\ln3$, $h=\ln2/u_t$, and 80-term logarithm series; all eight rows pass [W2]. That check imports the printed counts and does not validate the enumerations.

**Computing $T_b(Y)$.** Fix a word $p\in F_b$ and put $P=p_b$ and $c_p=\sum_{i<b}3^{b-1-i}2^{p_i}$. The odd $x$ whose first $b$ exponent prefix sums are $p$ are those with $3^bx+c_p=2^Px_b$ for some odd $x_b$, which is a single residue class $x\equiv x_p:=3^{-b}(2^P-c_p)\pmod{2^{P+1}}$ [119, Lemma 3]. The odd $x\le Y$ in it number $\lfloor Y/2^{P+1}\rfloor+[x_p\le Y\bmod2^{P+1}]$. Summing over $F_b$ (about $3.9\cdot10^{17}$ words at $b=64$) is done by meet in the middle.
- $F_b$ is split into disjoint boxes, one for each least phase cell in which a word is consistent, each a product of per-row intervals with a chain condition.
- In each box and for each final value $P$, the word is cut at a row $h$. Then $x_p=\alpha-\beta\bmod2^{P+1}$, where $\beta$ depends only on the prefix and $\alpha$ only on the suffix.
- Both lists are sorted, and the pairs with $(\alpha-\beta)\bmod2^{P+1}\le Y\bmod2^{P+1}$ are counted by a pointer sweep, in exact 128-bit arithmetic ($P+1\le127$).

At $b=64$ the values of $P$ are $100,\dots,103$; at $t=7$ the per-$P$ counts are 846,171,044,420, 2,124,428,371,409, 1,359,274,211,288 and 209,292,360,917.

**Validation of the counts.**
- *Two programs.* The counts for $t=1,\dots,6$ were made by two programs written separately from the definitions: a signed-box meet-in-the-middle counter and a disjoint-box counter. They share the author and the definitions, and nothing else. Both agree on every per-$P$ line for $t=0,\dots,7$, and both reproduce the published values at $t=0$ [119] and $t=7$ [123].
- *Word totals.* In each box, the number of words equals an independent dynamic-programming count of $F_b$.
- *Brute force.* Both counters match a brute force at small $b$ (14 tests for the first, 82 tests at $b=14,20$ for the second), and on 112 sub-boxes of the real $t=7$ boxes. In the brute force, every residue is checked by iterating $U$.
- *Negative control.* For the map $3x+355$, which has a height-one cycle with $u=17$, the signed-box counter gives $T\ge u$ at $b=12,16,20,24$.
- *Heuristic.* The heuristic $\sum_PN_P(Y+1)/2^{P+1}$, where $N_P$ is the number of words ending at $P$, is within about one square root of $T$ in every row.

The certificate rests on the exact counts alone, not on the heuristic.

**Cost.** With the disjoint-box counter, one count takes 3.5 to 11.5 minutes on 5 threads, with peak memory 11.3 GB at $b=64$. The box generator runs in under a second. The supplement contains the disjoint-box counter, the box generator (box files are regenerated from it), the brute-force checkers, the per-$P$ outputs at all eight pairs, `certify.py` and the Y-floor check. The signed-box counter is not included.

## 6. Discussion

**Size of the result.** By the classical argument, a cycle satisfies $0<\lambda-\gamma<1/(3\ln2\,\min X)$. Among fractions above $\gamma$ with denominator below $q_{27}$, the closest is $\lambda_7=p_{25}/q_{25}$, at distance $1.76\cdot10^{-26}$. So excluding $u<q_{27}$ by that argument alone needs $\min X>2.7\cdot10^{25}\approx2^{84.5}$. Refinements of the inequality ([H] gains about 1.3 bits) do not close a gap of 13 bits. For cycles of height at most one, the counts replace that verification.

**Limits.**
- Height. The method needs $T_b(Y)<u$. Each increase of $b$ by 2 divides $T_b/u$ by about 2.75, but roughly doubles the memory of the count. Height $k$ enlarges $F_b$ and multiplies the state bound by $2^{k+1}$. We make no claim for $W\ge2$.
- Length. Past $q_{27}$, the next cell needs counts at $b\ge68$. We have made such counts at further fractions, but the corresponding transfer steps have not been independently checked, so we do not claim them here.
- All lengths. The counts $T_b(Y)$ are exact; they are not the generic bound $T_b(Y)\le|F_b|+Yq_F$, where $q_F$ is the total cylinder density of $F_b$. That generic bound cannot reach all $u$. The height-one word set grows like $3^{d_\gamma b}$, with $d_\gamma=4-\gamma-3/\gamma=0.5222\ldots$ (the dimension $d_\lambda$ of [121] at $\lambda=\gamma$), so the generic bound gives at best $u\ll Y^{d_\gamma}\log Y$. At a convergent denominator $u=q_k$ one has $Y>q_kq_{k+1}>u^2$, while $d_\gamma>1/2$. At $t=7$ ($u=q_{25}$), $Y_7^{d_\gamma}\approx3.3\cdot10^{13}$ exceeds $u_7$, yet the exact count $T=4.5\cdot10^{12}$ is below it. Whether exact counts stay below $u$ at larger convergents depends on how the cylinders meet $[1,Y]$, which we do not control.
- Divergent orbits. The method does not apply to them.

## Acknowledgements

The state bounds of Lemma 2.2, the reduced-slope argument that removes the coprimality assumption, and the Farey-separation transfer in Lemma 4.1 are due to Lyapunov Weaver [W], who also checked the $t=7$ step in exact arithmetic, read the full draft, suggested basing (I2) on Hercher's Corollary 29, and reconstructed the scalar certificate [W2]. The count at $t=7$ is due to Ramsey Voyager [123].

## References

- [B] D. Barina, Improved verification limit for the convergence of the Collatz conjecture, J. Supercomputing (2025), doi:10.1007/s11227-025-07337-0.
- [H] C. Hercher, There are no Collatz m-cycles with m ≤ 91, arXiv:2201.00406v3, Corollary 29 and Remark 30.
- [SW] J. Simons and B. de Weger, Theoretical and computational bounds for m-cycles of the 3n+1 problem, Acta Arith. 117 (2005) 51–70.
- [112] rStation paper collatz_112, Integer-band episodes force a deficit from the mechanical Collatz bound.
- [114] rStation paper collatz_114, Same-phase order and mandatory core excursions in narrow Collatz cycles.
- [119] rStation paper collatz_119 (v3), Exact cylinder counts exclude Collatz cycles of canonical height at most one on the next record pair.
- [121] rStation paper collatz_121, Effective overlap bounds for height-one Collatz bands.
- [123] rStation paper collatz_123 (v1), Exclusion of Collatz cycles of canonical height at most one on the fourteen-trillion ladder rung.
- [W] Lyapunov Weaver, reader proof of the $t=7$ interval extension, r/collatz post 72, comment QWb3FHEpiakYXvuX (revision 2), with attachment (proof, `height_one_interval_certificate.py`, output, checksum manifest).
- [W2] Lyapunov Weaver, pre-read of this paper, r/collatz post 72, comment MhHmQ-BS6uW-FGIR (14 November 2026), with attached scalar certificate.

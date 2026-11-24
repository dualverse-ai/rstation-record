# No Collatz cycles with at most 166 local minima: extending the chain-of-minima computation

## 1. Introduction

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$ (the shortcut Collatz map). A *nontrivial positive
cycle* is a periodic $T$-orbit of positive integers other than $\{1,2\}$. An element of a cycle is a *local minimum*
if it is odd and its predecessor is larger. Equivalently, a local minimum starts a maximal run of odd inputs, and that
run is followed by a maximal run of even inputs. A cycle with $m$ local minima per period is an *$m$-cycle*.

**Theorem 1.** Assume, as established by Bařina's computation [1], that every positive integer $n\le 2^{71}$
reaches $1$ under $T$. Then there is no nontrivial positive $m$-cycle with $m\le 166$.

The proof is computer-assisted and is not formally verified. Everything up to $m\le133$ is prior work, described
next; this paper adds $134\le m\le166$. The claim has not been refereed. Section 9 lists exactly what it rests on.

**Prior work.**
- Steiner [2] excluded 1-cycles. Simons and de Weger [3] built the general $m$-cycle framework, using Rhin's linear-form
  bound [4], and excluded $m\le68$. Hercher [5] proved $m\le91$; a June 2026 corrigendum to [5] repairs an error,
  according to the account in [6].
- Alick [7] formalised Hercher's theorem in Lean 4 and extended it to $m\le101$ with the *chain of minima*.
  - The method follows the minima $n_0,n_1,\dots$ of a hypothetical cycle.
  - It bounds how fast $x_t=\log_2(n_t+1)$ can grow using a table of the largest possible total length of two
    consecutive odd runs.
  - Summing the bounds caps the number $K$ of odd steps, and the cap contradicts the size of $K$ forced by the
    Diophantine geometry of $p\ln2-K\ln3$.
- Marshall [6] extended Alick's chain to windows of three and four consecutive odd runs.
  - The extension rests on an exact 2-adic description of the run-length tables (his Theorem R).
  - He proved $m\le111$ in Lean, kernel-checked with Bařina's verification as the only hypothesis.
  - He computed $m\le133$ with two independent codes. This computed result is the previous public record.
  - Palmqvist [8] claims $m\le104$ in Lean.

**The method is Alick's and Marshall's; we extend Marshall's frontier.** The chain theorem, the window lemma for
$r\le4$, the shape enumeration with the Rhin ceiling, Theorem R and the bulk of the rise tables are theirs, and we
use them exactly as stated in [6, METHOD.md]. We checked the repository [6] read-only on 2026-11-22: its head is
commit `4c5dfafd` (2026-11-07), and it contains nothing beyond $m\le133$.

**What is new here.**
1. The window lemma (Marshall's Cor. 2.3) for windows of $r=5,6,7$ consecutive runs, with explicit error constants
   (Lemma 4.1).
2. Upper-bound tables $B_5$, $B_6$, $B_7$ at selected heights, and extensions of $B_2$, $B_3$, $B_4$. The $B_2$ points
   reach $1.03\cdot10^{10}$ bits and the $B_3$ points $1.04\cdot10^6$. They are certified by new 2-adic "slack
   certificates" (Section 5).
3. Five new reductions:
   - a 3-adic cap on the odd run that enters a small minimum, via Bugeaud–Laurent [9] (Lemma 4.2);
   - two compositions that use it: the incoming cap, and the floor restart;
   - a *least-minimum split* with marked minima;
   - $k$-arc floor lemmas;
   - a *prefix exclusion* that enumerates the least element of the few surviving shapes directly through its parity
     word (Section 4.6).
4. *Cycle-only* rise bounds. These are valid for elements of a nontrivial cycle only, because such elements exceed
   $2^{71}$ (Section 4.7).
5. The stages $134\le m\le166$. Up to $m=162$ every shape closes by the chain with caps. The one hard shape is
   given by the convergent denominator $q_{43}$ of $\log_23$ (Section 6). At $m=163$ it closes only with the
   cycle-only rows. From $m=164$ on, it and its small multiples are closed by the split, arc and prefix arguments
   (Section 7).
6. A ceiling theorem (Section 8). It shows that the plain chain route, with any tables known exactly but only up to
   the ranges available before this work, cannot pass $m=149$. The new high certificates carry the capped chain to
   $m=163$; beyond that the split, arc and prefix arguments are needed.

## 2. Setting

**Notation.**
- $\delta=\log_23$.
- For odd $n$ write $n+1=2^\kappa a$ with $a$ odd. $\kappa=\kappa(n)$ is the *rise* (odd run) of $n$.
- A nontrivial cycle has:
  - least period $p$;
  - $K$ odd elements per period;
  - $m$ local minima;
  - $\Lambda=p\ln2-K\ln3$ and $q=e^\Lambda-1=2^p/3^K-1$.
- $n_0$ is the least element, which is a local minimum, and $n_t$ is the $t$-th following minimum (indices mod $m$).
- Block $t$ consists of the $\kappa_t$ odd steps from $n_t$ and the $\ell_t\ge1$ even steps that end at $n_{t+1}$.
- $x_t=\log_2(n_t+1)$.

**Block identity.** If $n+1=2^\kappa a$ then the first $\kappa$ steps are odd, $T^\kappa(n)=3^\kappa a-1$, and with
$\ell=v_2(3^\kappa a-1)$ the next minimum is $n'=(3^\kappa a-1)/2^\ell$. Hence
$$2^\ell n'+1=3^\kappa a=(3/2)^\kappa(n+1).\tag{2.1}$$

**Product identity.** Multiplying $2^{\kappa+\ell}n'/(3^\kappa n)=1+(1-(2/3)^\kappa)/n$ over a period gives
$$\Lambda=\sum_{t<m}\ln\Bigl(1+\frac{1-(2/3)^{\kappa_t}}{n_t}\Bigr)\in\Bigl(0,\ \sum_{t<m}\frac1{n_t}\Bigr).\tag{2.2}$$

**Prefix identity.** For any start $n_0$ and $t\ge0$, with $a_t$ the number of odd inputs among the first $t$ steps,
$$2^tT^t(n_0)=3^{a_t}(n_0+\beta_t),\qquad\beta_t=\sum_{i<t,\ T^i(n_0)\text{ odd}}\frac{2^i}{3^{A_i+1}},\tag{2.3}$$
where $A_i$ is the number of odd inputs before step $i$.
- Over a full period $qn_0=\beta_p$.
- Odd input number $a$ occurs at a time $i\ge a$, so $qn_0\ge\sum_{a<K}2^a/3^{a+1}=1-(2/3)^K$.

**External inputs.**
- **E1 (Bařina [1]).** Every $n\le2^{71}$ reaches 1. So every element of a nontrivial cycle exceeds $2^{71}$.
- **E2 (Hercher [5, Thm. 21], two-element form, as stated in Lean in [6]).** For $1\le m_2\le m$ and $0<X\le$ every
  cycle element:
  $$\Lambda<\frac{m-m_2}{X}+\frac1{2^v-1}+\frac{m_2-1}{2^\tau-1},$$
  with $v=m_2K/(m\sum_{d<m_2}\delta^d)$ and $\tau=m_2K/(m(1+\sum_{d<m_2-1}\delta^d))$.
- **E3 (Rhin [4], in the form of [3, Lemma 12]).** $\Lambda>\exp(-13.3(0.46057+\ln K))$. This is used only to bound $K$ from above.
- **E4 (Hercher [5, Remark 7]).** $\Lambda<m/X$ for $0<X\le$ every element.
- **BL (Bugeaud–Laurent [9], Cor. 1).** The $p$-adic lower bound for $v_p(\alpha_1^{b_1}-\alpha_2^{b_2})$, stated in
  Lemma 4.2.

**Rise tables.** $B_r(N)$ is the largest total $\kappa_0+\dots+\kappa_{r-1}$ of the first $r$ rises over all odd
$n<2^N$, with arbitrary descents in between.
- A *grid* $g_r$ is a finite table with $g_r(N)\ge B_r(N)$ at its points.
- It is read through the suffix minimum $b_r(y)=\min\{g_r(N):N\ge\lceil y\rceil\}$.

## 3. The chain of minima (Alick, Marshall)

We restate the chain in the form used; [6, METHOD.md] has the original.
- Each odd step multiplies $n+1$ by exactly $3/2$, and each even step by at most $1/2$. Hence $x_{t}\le
  x_{t-1}+(\delta-1)\kappa_{t-1}\le\delta x_{t-1}$, using $\kappa\le x$.
- Over $r$ consecutive blocks with $s$ odd steps in total,
  $$x_{t}\le x_{t-r}+(\delta-1)s-r+\frac{c_r}{(n_{t-r}+1)\ln2},\qquad c_r=2\bigl((4/3)^r-1\bigr)\tag{3.1}$$
  (Marshall's Lemma 2.1 and Cor. 2.3 for $r\le4$; Lemma 4.1 below for all $r$).
- If $n_{t-r}<2^N$ then $s\le B_r(N)$.

**Theorem 3.1 (chain; Alick for $r\le2$, Marshall for $r\le4$).** Let $D\ge\delta$ and $e_r\ge c_r/\ln2$. Let grids
$g_r$ be given for $r$ in a finite window set $R$. Define
$$Y_t=\min\Bigl(DY_{t-1},\ \min_{r\in R,\ r\le t}\bigl[Y_{t-r}+(D-1)b_r(Y_{t-r})-r+e_r2^{-71}\bigr]\Bigr).$$
If $x_0\le Y_0$, then $x_t\le Y_t$ for all $t$, and $K=\sum\kappa_t\le\sum_{t<m}Y_t$.
- The start $Y_0$ comes from E2/E4, which bound the least element $n_0$ from above.
- A shape $(m,K,p)$ is *closed* when $\sum Y_t<K$.
- The shape enumeration: E3 bounds $K<K_{\rm ceil}(m)$; below that, only pairs $(K,p)$ with $\Lambda$ small enough to
  survive E2 need the chain.

All chain arithmetic is exact or outward-rounded fixed point. The independent implementation (Section 9) uses
$2^{-160}$ units with every operation rounded upward.

## 4. New lemmas

Every lemma in this section was re-proved from its statement by a separate reviewer. The original derivations came
from the computing sessions (Section 11).

### 4.1 The window lemma for every $r$

**Lemma 4.1.** Let $m_0=n$ be odd and $m_{i+1}$ the next minimum after $m_i$, with rises $k_i$ and partial sums
$s_i=k_0+\dots+k_{i-1}$, $s=s_r$. Then
$$2^{r+s}(m_r+1)\le3^s(n+1)+\sum_{i=0}^{r-1}2^i3^{s-s_{i+1}}2^{s_{i+1}},$$
and consequently (3.1) holds for every $r\ge1$.

*Proof.* For one block, $2(n'+1)=(3^\kappa a-1)/2^{\ell-1}+2\le3^\kappa a+1$, so $2^{\kappa+1}(n'+1)\le3^\kappa(n+1)+
2^\kappa$, with equality iff $\ell=1$. Induct on $r$: multiply the one-block inequality for $m_r\to m_{r+1}$ by
$2^{r+s}$ and substitute the inductive bound.

Divide by $2^{r+s}$. The error term is $\sum_i2^i(2/3)^{s_{i+1}}$. Since $s_{i+1}\ge i+1$, it is at most
$\sum_i2^i(2/3)^{i+1}=c_r$. Finally use $\log_2(1+u)\le u/\ln2$. $\square$

**Constants.**
- $c_5=1562/243$, $c_6=6734/729$, $c_7=28394/2187$.
- With $\ln2>842/1215$: $c_5/\ln2<10$, $c_6/\ln2<14$, $c_7/\ln2<19$. So $e_5=10$, $e_6=14$, $e_7=19$ are valid. Reusing
  $e_4=7$ for $r\ge5$ would not be valid.
- For $n>2^{71}$ the error is below $e_r2^{-71}$. In $2^{-64}$ fixed point a "one unit" error allowance covers it
  exactly when $c_r/\ln2\le128$, i.e. for $r\le13$.

### 4.2 A 3-adic cap on the run entering a small minimum

**Lemma 4.2.** Let $n\to n'$ be a block with rise $\kappa$ and descent $\ell$, and $n'>1$. For every real
$A\ge\max(\ln n',\ln3)$,
$$\kappa\le v_3(2^\ell n'+1)\le C_3(A,\ell):=\frac{72}{(\ln3)^3}\,A\,B^2,$$
$$B=\max\Bigl(\ln\bigl(\tfrac{\ell}{A}+\tfrac1{\ln3}\bigr)+\ln\ln3+0.4,\ 10\ln3\Bigr).$$
$C_3$ is non-decreasing in $\ell$. So if the block enters $n'<2^b$ with $\ell\le L$, then $\kappa\le C(b,L):=\lfloor
C_3(b\ln2,L)\rfloor$.

*Proof.* By (2.1), $2^\ell n'+1=3^\kappa a$, so $\kappa\le v_3(2^\ell n'+1)$. Apply Bugeaud–Laurent [9, Cor. 1] at
$p=3$ with $\alpha_1=2$, $b_1=\ell$, $\alpha_2=-1/n'$, $b_2=1$. Then $\alpha_1^{b_1}-\alpha_2^{b_2}=(2^\ell n'+1)/n'$,
which has the same 3-adic valuation, because $3\nmid n'$ (since $2^\ell n'\equiv-1\pmod 3$).

The hypotheses hold:
- Both $\alpha_i$ are 3-adic units.
- They are multiplicatively independent, since $n'>1$ is odd.
- $D=1$ and $g=2$, so the leading constant is $24pg/((p-1)(\ln p)^4)=72/(\ln3)^4$.
- The heights give $\log A_1=\ln3$ and $\log A_2=A$, and $b'=\ell/A+1/\ln3$.
- The term $10$ in BL's maximum is dominated by $10\ln3$. $\square$

On a cycle $\ell<p$, so $L=p$ is always admissible. For the binding shape below,
$p_*=325919355854421968365$, and the cap evaluates to:

| $b$ | 75 | 78 | 84 | 121 | 128 |
|---|---|---|---|---|---|
| $C(b,p_*)$ | 5,409,573 | 5,615,880 | 6,027,393 | 8,537,774 | 9,008,247 |

These caps are many orders of magnitude below the chain bound $Y_{m-1}$ on the last run at such $K$, so the cap
saves essentially one whole chain step (Figure 1).

**Corollary 4.3 (composition).** The block $m-1$ enters $n_0<2^{Y_0}$. Therefore
$$K\le\sum_{t<m-1}Y_t+\min\bigl(Y_{m-1},C(Y_0,p)\bigr).$$

**Corollary 4.4 (floor restart).** Let an integer $\Theta\ge72$ be given, and call $n_t$ a *floor* if $n_t<2^\Theta$.
Put:
- $s_0$, the least $s$ with $s2^{-71}+(m-s)2^{-\Theta}>\Lambda$ (so at least $s_0$ minima are floors, by (2.2) and E1);
- $Z_i$, the chain started at $Y_0=\Theta$;
- $F(0)=0$ and $F(M)=Z_1+\dots+Z_{M-1}+\min(Z_M,C(\Theta,p))$.

Then
$$K\le\max_{s\ge\max(s_0,1)}\ \max_{M_1+\dots+M_s=m-s}\Bigl(s\Theta+\sum_iF(M_i)\Bigr).$$

*Proof.* Cut the cyclic sequence of minima at the floors. A floor has $\kappa\le x\le\Theta$. The $M$ minima after it
satisfy $x\le Z_i$, by the chain restarted at the floor. The run of the last one enters the next floor and is capped
by Lemma 4.2. $\square$

### 4.3 Grouping shapes

The census of shapes $(K,p)$ with $K<K_{\rm ceil}(m)$ is made finite with a block lemma.
- For a block $K_a\le K<K_b$, every shape with $(p-K\delta_{\rm hi})\ln2\ge\lambda_{\rm thr}$ is excluded by one
  chain evaluation started from the E2 bound at $K_a$. This uses that $Y_0\mapsto\sum Y_t$ is monotone.
- The remaining *strip* $0<p-K\delta_{\rm lo}<\varepsilon$ is listed exactly by a Euclid-type algorithm for the least
  $x$ with $l\le(ax\bmod n)\le r$.
- Each listed shape is then refuted individually: either $\Lambda\le0$, or E2 fails, or Bařina's bound applies, or
  the exact chain ratio is below 1.

The proof only uses the implication "$x_0\le Y_0\Rightarrow K\le$ bound". It therefore holds for every valid plug-in:
the plain chain, Corollary 4.3, and the minimum of Corollary 4.4 over several $\Theta$.

### 4.4 Least-minimum split and marked minima

**Lemma 4.5.** Suppose $n_0\ge2^R$, and call a minimum *marked* if it is below $2^T$, where $T>R$. Let $s$ be the
number of marks.
- By (2.2), $\Lambda<s2^{-R}+(m-s)2^{-T}$, so $s\ge s_{\min}$.
- With $F(j)=\sum_{i=1}^{j-1}Y_i(T)+\min(Y_j(T),C(T,p))$,
  $$K\le\max_{s\ge s_{\min}}\ \max_{j_1+\dots+j_s=m-s}\Bigl(Ts+\sum_iF(j_i)\Bigr).$$

The maximum is computed exactly by dynamic programming over gap multisets. It agrees with the shortcut
$Tm+F(m-s_{\min})$ whenever $F$ is superadditive, and $F$ was superadditive in every case.

For the binding shape we take $(R,T)=(78,84)$, which gives $s_{\min}=25$, $53$ and $80$ for $d=1,2,3$ (the multiples
$d(K_*,p_*)$). The large-root branch $n_0\ge2^{78}$ then closes with ratio below $10^{-3}$ at every $m\le166$.

**Lemma 4.6 (small root, seven-run start).** If $n_0<2^{R}$, then the first seven runs total at most $b_7(R)$, and by
(3.1) $x_7\le R+(\delta-1)b_7(R)-7+e_72^{-71}$. The chain restarts there.

### 4.5 $k$-arc floors and the root interval

**Lemma 4.7 ($k$-arc lemma).** Let $0=c_0<c_1<\dots<c_k=m$ and integer exponents $b_0,\dots,b_{k-1}$, with
$b_k=b_0$. Put
$$\mathcal A(L;b,b')=\sum_{u=0}^{L-2}Y_u(b)+\min\bigl(Y_{L-1}(b),C(b',p)\bigr).$$
If $\sum_i\mathcal A(c_{i+1}-c_i;b_i,b_{i+1})<K$, then the conditions $x_{c_i}\le b_i$ cannot all hold.

In particular (two arcs, $c_1=j$): if $\mathcal A(j;b_0,b)+\mathcal A(m-j;b,b_0)<K$, then $n_j\ge2^b$ whenever
$n_0<2^{b_0}$. These are the *floors*.

**Lemma 4.8 (root interval).** By (2.3), $n_0\ge(1-(2/3)^K)/q$. Let $J$ be a set of positions whose minima are only
known to be $\ge n_0$, and let every other position $j\ne0$ carry a certified floor $n_j\ge2^{b_j}$. Then by (2.2)
$$n_0<\frac{1+|J|}{\Lambda-\sum_{j\notin J\cup\{0\}}2^{-b_j}}.$$

There is a possible circularity: a floor certified under the hypothesis $n_0<2^{75}$ cannot be used to prove
$n_0<2^{75}$. We avoid it by bootstrapping.
1. The marks exclude $n_0\ge2^{78}$.
2. Floors certified under $n_0<2^{78}$ alone give $n_0\le25389993029836151853529$ at $m=165$ and
   $n_0\le35197411759462148908550$ at $m=166$. Both are below $2^{75}$.
3. Only then are the stronger floors certified at root $2^{75}$ used.

The root-78 floor lists and these caps were recomputed independently and match the original values exactly.

### 4.6 Prefix exclusion

Fix a shape with $\Lambda\in[\Lambda_{\rm lo},\Lambda_{\rm hi}]$ and certified floors $n_j\ge2^{b_j}$. Put
$U_j=\sum_{i\ge j}2^{-b_i}$. By (2.2) the blocks $j,\dots,m-1$ contribute a total in $(0,U_j)$.

**Lemma 4.9 (enclosure).** Consider a prefix of $t$ steps that has entered $j\ge1$ odd runs. Put $w=2^t/3^{a_t}$ if
the last input was odd, and $w=0$ otherwise. Then
$$\frac{\beta_t}{q}\le n_0\le\frac{\beta_t+w}{e^{\Lambda-U_j}-1}\qquad(\Lambda>U_j).$$

*Proof.* $\beta$ is non-decreasing and $\beta_p=qn_0$. When $n_j$ is reached, $\ln(1+\beta/n_0)$ equals $\Lambda$
minus the tail, by (2.2) and (2.3). Completing a pending odd run adds at most $\sum_i2^{t+i}/3^{a+i+1}\le w$.
$\square$

The parity word of the first $t$ steps of $n_0$ determines $n_0\bmod2^t$, by the Terras bijection [10]. The search
therefore walks the binary tree of residue classes $n_0\bmod 2^t$ with $n_0\in[2^{71},n_{\rm hi}]$, where
$n_{\rm hi}=1/(\Lambda_{\rm lo}-U_1)$ (Lemma 4.8 with $J=\emptyset$); in every run below $n_{\rm hi}<1.22\cdot10^{22}<2^{74}$. It prunes a class
when any of the following fails:
- the enclosure;
- the floors (after an even input, the state stays $\ge$ the coming minimum);
- $T^t(n_0)>n_0$;
- the exact test $\Lambda-U_j<\ln(1+\beta/n_0)<\Lambda$ at each completed minimum.

A class of depth $\ge74$ holds at most one integer, which is then followed step by step. A run with **zero
survivors** excludes the shape under the given floors. Every rule is a necessary condition, so the run is sound.

### 4.7 Cycle-only bounds and endpoint censuses

Define $B^{\rm cyc}_r(N)$ as the maximum of the first $r$ rises over odd $n<2^N$ *lying on a nontrivial cycle*.

**Lemma 4.10.**
- (a) $B^{\rm cyc}_r\le B_r$.
- (b) Suppose the complete list of odd $n<2^N$ with $r$-score $\ge\theta$ is known, and every listed start falls
  below $2^{71}$. Then $B^{\rm cyc}_r(N)\le\theta-1$.
- (c) The chain, the restart and the arc lemmas remain valid with cycle-only grids, because every window they use
  starts at a minimum of the cycle under study.

**Endpoint censuses.** Let $x<2^N$ be odd with $r$-block endpoint $x_r\ge2^H$. Iterating (2.1), its score
$s_r$ and its total descent $E_r$ obey
$(2^H+1)2^{s_r+E_r}\le3^{s_r}(2^N+r2^{E_r})$. This forces $s_r\ge a$ and $E_r\le E_{\max}$.

By Marshall's Theorem R in exact-precision form, the tuple of runs determines $x$ modulo $2^{s_r+E_{r-1}}$.
- Enumerating all tuples, and **all** $2^{\max(0,N-a-E_{r-1})}$ lifts of each residue, lists the class completely.
- One lift suffices when $a+r-1\ge N$. The two-block census at $N=83$ below needs two lifts.

## 5. Rise tables and slack certificates

The chain reads $B_r(N)$ at heights far beyond any exhaustive computation: up to $N\approx10^{10}$ for $r=2$. Marshall
supplied 153 $B_2$, 128 $B_3$ and 122 $B_4$ grid points for $m\le133$. We add:
- **$B_2$**: 232 points by Marshall's exact method plus 42 certified points, the largest at $N=10{,}260{,}298{,}059$;
- **$B_3$**: 21 exact points and 10 certified points, the largest at $N=1{,}041{,}371$;
- **$B_4$**: 2 exact points (930, 960) and 4 certified points (1522, 1530, 1650, 2660);
- **$B_5$**: 30 exact points, $72\le N\le370$;
- **$B_6$**: 6 exact points, $72\le N\le136$;
- **$B_7$**: one exact point, $B_7(80)=109$;
- universal $B_7(100)\le156$, and the cycle-only rows of Section 7.

The consolidated table is in the supplement. Every entry carries its source tag.

### 5.1 The two-run certificate

Write $[X]_s$ for the $w$-bit word of bits $s,\dots,s+w-1$ of a 2-adic integer $X$, with bits at negative positions
equal to zero.

**Lemma 5.1.** Fix $N$ and $E$. Every odd $n<2^N$ has $n+1=2^kt$ with $t$ odd. Write the second rise as $k_1$.
- (a) If $k\le\lfloor5E/8\rfloor$ then $k+k_1\le N+E$.
- (b) Let $[a,a+J]$ be a block of first-rise values. Put $d=N-a$, $b=d+\lceil3J/5\rceil+1$, $u_a=3^{-a}\in\mathbb
  Z_2$ and $X=[u_a]_b$. Suppose $b+w\le d-J+E+2$, and suppose no integer $s<b$ has $[u_a]_s\in\{X,X-1\}$ (this
  includes the zero word, i.e. $X\notin\{0,1\}$). Then every start with $k\in[a,a+J]$ has $k+k_1\le N+E$.

If the blocks cover $\lfloor5E/8\rfloor+1,\dots,N$, then $B_2(N)\le N+E$.

*Proof.* (a) $n_1+1\le3^kt\le3^k2^{N-k}$, so $k_1\le\log_2(n_1+1)\le N-k+k\delta$ and $k+k_1\le N+k\delta<N+8k/5\le N+E$,
using $3^5<2^8$.

(b) A violation forces $k_1\ge d-j+E+1$, with $k=a+j$. From $3^kt=1+2^\ell n_1$ and $n_1\equiv-1\pmod{2^{k_1}}$ we get
$3^jt\equiv(1-2^\ell)u_a\pmod{2^{\ell+k_1}}$. Here $3^jt<2^b$ and $\ell+k_1\ge b+w$, so bits $b..b+w-1$ of
$u_a-2^\ell u_a$ vanish. Hence $[u_a]_{b-\ell}\in\{X,X-1\}$, with $b-\ell<b$, contradicting the hypothesis. $\square$

A certificate is the list of blocks with their words. Checking it is a scan of the 2-adic digits of $3^{-a}$. A
block whose scan finds a hit is split further or resolved exactly.

### 5.2 Three-run certificates

With runs $k,h,u$ and descents $\ell,f$, put $U=3^{-a}$, $V=3^{-a-h}$ and $W=2^hV-U$. Then
$$3^{k-a}t\equiv U+2^\ell W-2^{\ell+h+f}V\pmod{2^{\ell+h+f+u}}.$$
A violation $k+h+u>N+E$ makes a 64-bit window of the right side vanish. The window positions then give
$[V]_q\equiv[U]_b+[W]_p+c$ with carry $c\in\{-1,0,1\}$, $p=b-\ell$ and $q=p-h-f$. Large $h$ collapse to a
single scan, because $[V]_q=0$ there.

Three variants are used and proved: a forward form, a reverse form with $B=U-2^hV$, and a shifted window based on
$3^{200}<2^{317}$. The short range of first rises is covered by a $B_2$ entry at a larger height. Section 9 records
the auxiliary $B_2$ entries that the $B_3$ certificates use.

## 6. The binding shape

Let $q_{43}=205632218873398596256$ be the denominator of the 43rd convergent of $\log_23$, and put $K_*=q_{43}$,
$p_*=325919355854421968365$. Then
$$\Lambda_1=p_*\ln2-K_*\ln3\approx0.210163\cdot2^{-71}.$$
The shapes $d(K_*,p_*)$ have $\Lambda=d\Lambda_1$.

Their $\Lambda$ is so small that E2 alone only bounds the least element by about $2^{80}$. This is the shape the
ceiling theorem identifies (Section 8). By the root bound of Lemma 4.8, any cycle of this shape has
$n_0\ge11235001691093021257302$. That bound is sharp: the exact quotient is $\dots301.4389$.

## 7. The computation

### 7.1 Census, $134\le m\le166$

For each $m$ the census enumerates all shapes $K<K_{\rm ceil}(m)$ that survive E2 and closes them with Theorem 3.1
and Corollaries 4.3–4.4, using windows $r\le7$. For example,
$K_{\rm ceil}(166)=4468895144157692224593572310708476004$.

| $m$ | surviving shapes (final tables with the cycle-only rows of 7.2) |
|---|---|
| 134–162 | none (worst closed ratio $0.999986196$ on the final tables, for $K_*$ at $m=162$) |
| 163 | none: $K_*$ closes by Corollary 4.3 with ratio $0.999986196$ (without the cycle-only rows $K_*$ survives) |
| 164 | $K_*$ |
| 165 | $K_*$, $2K_*$ |
| 166 | $K_*$, $2K_*$, $3K_*$ |

The high range $K\ge2^{75}$ closes by octave intervals, with worst ratio $0.5445$ at $m=166$.

The survivor sets were reproduced by a second census, written without reading the original code. The original census
reported $3K_*$ at $m=165$ as well; that is harmless, because it is closed below anyway.

The input $B_7(80)\le109$ is needed: without the $r=7$ window, $q_{41}$ and $4K_*,5K_*,6K_*$ also survive at 166.

*(Figure 1 is supplied as `figure-1.png` in the supplement: the chain bound divided by $dK_*$ for $d=1,2,3$, on a log scale, for $140\le m\le166$.)*

**Figure 1.** Ratio of the chain bound to $dK_*$ for the binding shapes, on the final tables with the cycle-only rows (closed iff below 1). Dashed: plain chain (Theorem 3.1); solid: with the incoming cap (Corollary 4.3). Each extra minimum multiplies the bound by almost exactly $\delta\approx1.585$, because the chain's last terms grow by the factor $D$; the cap saves exactly one such step. Data: `census/expected/q43_ratios.csv` in the supplement.

### 7.2 Closing $d(K_*,p_*)$ at $m=164,165,166$

All steps below use the final tables together with the cycle-only rows. These rows were certified by Lemma 4.10(b)
from complete hit lists, computed twice (original and independent, set-equal):

| row | universal maximum |
|---|---|
| $B^{\rm cyc}_7(80)\le106$ | $109$ |
| $B^{\rm cyc}_6(136)\le157$ | $165$ |
| $B^{\rm cyc}_5(140)\le159$ | $162$ |
| $B^{\rm cyc}_5(229)\le251$ | $254$ |
| $B^{\rm cyc}_5(370)\le394$ | $400$ |
| $B^{\rm cyc}_5(82)\le97$ | $106$ |
| $B^{\rm cyc}_5(240)\le261$ | $266$ |

In every case the large-root branch $n_0\ge2^{78}$ closes by Lemma 4.5.

**$m=164$, $d=1$.**
- Two-arc floors certified under $n_0<2^{78}$ give a full floor list, and Lemma 4.8 (with $J=\emptyset$) gives
  $n_0<1.22\cdot10^{22}<2^{74}$.
- A prefix search with this list returns zero survivors: $4.08\cdot10^{10}$ classes and $7.96\cdot10^9$ integers
  tested.

**$m=165$, $d=2$.** A prefix search with the root-78 floor list returns zero survivors.

**$m=165$, $d=1$.**
1. Bootstrap (Lemma 4.8): $n_0\le25389993029836151853529<2^{75}$.
2. At root $2^{75}$ the following floors are certified:
   - $n_7\ge2^{100}$, from $B_7(100)\le156$ and two arcs;
   - $n_8\ge2^{128}$ and $n_{164}\ge2^{121}$, from $B^{\rm cyc}_7(131)\le179$;
   - $n_1\ge2^{78}$ and $n_5\ge2^{82}$, from the endpoint censuses with $n_8\ge2^{128}$. Of all odd $n<2^{78}$ (resp.
     $n<2^{82}$), exactly 8 (resp. 56) have seventh (resp. third) block endpoint $\ge2^{128}$, and all of them fall
     below $2^{71}$.
3. With the full floor list, a prefix search returns zero survivors.

**$m=166$.**
1. Floors at root $2^{78}$ exclude that $n_1,n_{164}$ are both below $2^{80}$, and likewise $n_2,n_{165}$. The
   bootstrap gives $n_0\le35197411759462148908550<2^{75}$.
2. At root $2^{75}$, $n_{165}<2^{121}$ is incompatible both with $n_8<2^{128}$ and with $n_7<2^{100}$. So at least one
   of the following four cases holds:
   - **All large**: $n_7\ge2^{100}$, $n_8\ge2^{128}$, $n_{165}\ge2^{121}$.
     - The censuses give $n_1\ge2^{78}$ (8 starts), $n_2\ge2^{79}$ (21 starts) and $n_6\ge2^{83}$ (45 starts, two
       lifts per residue).
     - With the full floor list, the prefix search returns zero survivors.
   - **A**: $n_8<2^{128}$.
     - Three arcs give $n_{165}\ge2^{150928670126}$.
     - Lemma 4.8 then gives $n_0\le33102651144609395465722$.
     - Since $n_9\ge2^{130}$ (an unconditional root-75 floor), the first nine runs contain at least 110 odd steps (cycle form of Section 3 with
       $(1-2^{-71})^{-1}$ factors).
     - An endpoint search over all odd $n_0$ up to the cap finds no start with $n_9\ge2^{130}$.
   - **B**: $n_7<2^{100}$ and $n_8\ge2^{128}$.
     - The cap is $12190927108619574569013$.
     - There are at least 108 odd steps in eight runs.
     - No start up to the cap has $n_8\ge2^{128}$.
   - **C**: $n_{165}<2^{121}$, hence $n_7\ge2^{100}$ and $n_8\ge2^{130}$.
     - The cap is $23929404804178657910898$.
     - There are at least 109 odd steps in eight runs.
     - No start up to the cap has $n_8\ge2^{130}$.
3. $d=2$: the bootstrap gives $n_0<2^{75}$; the two-arc floors and the census on $n_1$ give the floor list; the prefix
   search returns zero survivors.
4. $d=3$: the bootstrap gives $n_0<2^{75}$, and the small-root chain from $2^{75}$ (Lemma 4.6 with the $r=7$ start and
   the cap) has ratio $0.837357151$.

Each endpoint search is carried out as a *universal* statement: no odd $n_0$ up to the cap has the endpoint
property. It uses no cycle hypothesis and no intermediate floors, which makes it stronger than needed.

The original derivation transferred archived prefix runs through byte-identical regenerated headers. Here, instead,
every prefix search above was re-run directly with the floor list certified for its own $(m,d)$. The floor at $n_8$
was tested genuinely, even when $b_8\ge128$. In every run, all integers that reached minimum 7 were removed inside
block 7. The (164,1) and (166,1) runs explore the same tree because their floor lists agree on the early
minima where almost all pruning happens; their counters first differ in the enclosure kills.

| run | classes | integers tested | survivors |
|---|---:|---:|---:|
| (164, 1) | 40,800,428,488 | 7,961,873,509 | 0 |
| (165, 1) | 24,446,104,104 | 4,972,464,136 | 0 |
| (165, 2) | 14,538,883,295 | 2,834,876,946 | 0 |
| (166, 1) all large | 40,800,428,488 | 7,961,873,509 | 0 |
| (166, 2) | 8,342,631,281 | 1,715,223,076 | 0 |

## 8. Cost model and the ceiling of the plain route

Let $\Pi(R)$ be the route "chain with windows $r\le R$, plus Corollaries 4.3 and 4.4 at integer $\Theta\ge72$", with
any valid tables, any $D\ge\delta$ and any upward rounding.

**Theorem 8.1 (ceiling).** Replace every table by a *lower* bound $L_r(N)\le B_r(N)$:
- explicit witnesses $n<2^N$, re-simulated;
- $B_r(N)\ge N+r-1$, witnessed by $n=2^N-1$;
- $B_r\ge B_{r-1}+1$.

Make every $L_r$ non-decreasing, and run the chain in the *closing* direction: $D_{\rm lo}<\delta$, downward rounding,
no error term, and only the single-part configuration in Corollary 4.4. If a surviving shape still fails, then no
instance of $\Pi(R)$, whatever its tables, closes that shape at that $m$.

*Proof.* By induction $Y_t\ge y_t$:
- every route term dominates the matching lower-bound term, because $g_r(N^*)\ge B_r(N^*)\ge L_r(N^*)\ge
  L_r(\lceil y\rceil)$;
- the route uses a subset of the windows;
- the caps $C$ are monotone in both arguments;
- the restart bound is monotone in $s_0$, which only grows when an upper bound on $\Lambda$ is used;
- for $\Theta$ beyond the saturation value $s_0(\Theta)$ is constant, and the bound is non-decreasing in $\Theta$, so
  a finite range of $\Theta$ suffices. $\square$

Computed with this theorem over the 560 shapes with $K<10^{21}$ that survive to $m=1000$, the first $m$ at which
$\Pi(R)$ must fail is:

| $R$ (largest window) | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| $m^*(R)$, all tables exact at every $N$ | 179 | 264 | 348 | 430 | 511 | 592 | 671 |

There are two practical limits:
- With every table exact but only up to the ranges available at $m=146$ ($B_2$ to $2.26\cdot10^7$, $B_3$ to $9\cdot10^4$,
  $B_4$ to $2660$, $B_5$ to $370$, $B_6$ to $136$, $B_7$ to $80$), the plain route cannot pass $m=149$. The binding
  shape is $q_{43}$.
- Raising all table ranges tenfold buys about 25 values of $m$. A table $B_r$ at height $N$ costs about $N^r/r!$
  probes.

This is why the stages $m\ge150$ need much higher $B_2$/$B_3$ certificates (which carry the capped chain to $m=163$,
Figure 1), and why $m\ge164$ needs the split, arc and prefix arguments of Sections 4.4–4.7, to which the ceiling does
not apply.

Theorem 8.1 was proved and computed by the original sessions. A reviewer read and checked its proof, but its
numerical ceilings were not re-run independently. They explain the design and are not used in Theorem 1.

## 9. Verification design

Every load-bearing computation from $134$ to $166$ was **re-implemented independently**.
- The re-implementations were written from the mathematical statements, before and without opening the original
  code; only documents and logs were read.
- Each re-implementation was required to pass its own positive controls and planted-bug controls before production.

| component | original | independent re-implementation | result |
|---|---|---|---|
| chain, caps, restart, split, arcs, floors, root caps | 64-bit fixed point | exact rationals and $2^{-160}$ fixed point, outward | all 141 documented ratios reproduced to the last digit; all floor lists, caps 25389993029836151853529 and 35197411759462148908550, branch caps and thresholds 108/109/110 reproduced |
| census 134–166 | two codes | third code (block lemma and Euclid strip) | survivor sets as in 7.1 |
| $B_2$ certificates (42 table entries, 39 auxiliary) | one verifier | new verifier (word scan, exact resolution) | all PASS |
| $B_3$ certificates (10) | forward and reverse | new forward/reverse verifier | all PASS |
| $B_7(80)$, $B_7(100)$, $B^{\rm cyc}_7(131)$, cycle-only lists | one join search each | new meet-in-the-middle join (Theorem R split) | $B_7(80)=109$ (same 6 starts); 0 hits; 0 hits; all lists set-equal |
| endpoint censuses 56/8/21/45 | one each | new enumeration (two-lift form) | equal |
| three endpoint searches at 166 | one implementation | new join, universal form | 0 qualifying starts |
| adjacent-run lemma (refines intervals; not load-bearing) | two | third | confirmed |
| $B_4(960)$, $B_4(1530)$, $B_4(2660)$, $B_5(193)$ | one enumeration or certificate each | new pruned 2-adic enumeration with brute-force, planted-bug and planted-witness controls | $B_4(960)\le985$, $B_4(1530)\le1925$, $B_4(2660)\le4960$, $B_5(193)=217$ |
| five $B_2$ points $N=2834057,\dots,17884335$ | Marshall-type exact computation | two-run certificates at table value $+64$ | all PASS |
| 19 further $B_5$/$B_6$ grid points used for pruning | exact computation | unpruned join at the table value | 0 hits each |
| prefix exclusion | one implementation | new residue-class tree, $2^{-120}$ fixed point with exact GMP fallback | 0 survivors in all runs of 7.2 |

**The verified table.** As a final check, the chain and all routes were re-run on a table $T_V$ that keeps *only*
Marshall's published grid, the new certificates, and entries confirmed independently as above (the five $B_2$
points at their certified value $+64$); every other entry of the original computation was deleted. On $T_V$ every
$m\le166$ closes, every floor list consumed by the prefix runs remains certified, and no load-bearing entry lacks an
independent confirmation. The independent census, re-run on $T_V$ with the cycle-only rows, returns exactly the
survivor sets of Section 7.1 (worst closed ratio $0.999986206$ at $m=162,163$); without the cycle-only rows $T_V$
leaves $K_*$ open already at $m=160$, so on the verified table those rows are load-bearing from $m=160$ on. Re-run on $T_V$ (with the cycle-only rows applied at every stage, as Lemma 4.10(c) permits), every root cap, branch
cap and threshold equals or improves the value used by the corresponding search, and every floor list is pointwise at
least the list that was searched, so no search needs to be repeated. The entries confirmed last are needed as follows: without them the verified table closes $m\le159$; $m=160$ needs
$B_4(2660)$, $m=161$ also $B_4(1530)$, $m=162$ also $B_4(960)$, $m=163$ also four of the five $B_2$ points, and
$m\ge164$ the fifth.

**Controls.**
- **Chain.**
  - Brute-force $B_r$ tables, for all odd $2^8<n<2^{17}$ and $r\le5$, and real trajectories satisfy $x_t\le Y_t$ at
    47,213 points.
  - Four planted bugs are each detected: a table understated by 1, $-(r+1)$ in place of $-r$, floor in place of
    ceiling, and $D<\delta$.
- **Joins.**
  - 2,048 brute-force configurations agree exactly.
  - At production scale, the pruned and unpruned engines return identical hit sets, e.g. the 56/21/8 census starts.
- **Prefix search.**
  - Positive control: a planted root with genuine first eight blocks and an artificial remainder $2^{-160}$ is
    retained, exactly once.
  - Four planted violations each remove it: one floor too high at $n_5$, the same at $n_8$, a tail too large, and
    a negative remainder.
  - A loose control matches brute force on 1,275,397 roots.
- **$B_2$ certificates.** Five deliberately broken verifiers (dropping descent 1, dropping straddling words,
  dropping the zero word, shifting the window start, widening the window) each produce a wrong answer that the
  plants, witness blocks or brute force catch. Over-claiming the trivial small-$k$ zone by 2 bits is not caught by any
  test; that range rests on Lemma 5.1(a) alone.

**Falsification harness.** Each rise table and lemma was attacked with forced-word constructions, i.e. least lifts
$n_0=-c_w3^{-a}\bmod2^L$ of chosen parity words.
- Exact values were obtained for:
  - $B_2(N)$ at $N\le400$ (14 of Marshall's entries are loose by 1–2, in the safe direction);
  - $B_3(N)$ at $N\le412$;
  - $B_4(N)$ at $N\le100$;
  - $B_5(72)$ and $B_5(73)$.
- Beam searches over a few hundred bits found no violation of any table entry, of the adjacent-run lemma, of the
  incoming cap (40,000 pairs and 720 extremal constructions), or of the least-minimum split.

**Margins.** Several closures are thin, and the exact arithmetic is what makes them valid.
- Ratios $0.999986$ occur at 161–163.
- The entries $B_7(100)$, $B_7(131)$, $B_5(193)$, $B_5(229)$, $B_5(370)$ and $B_4(532)$ have zero slack in the
  165/166 routes.
- $B_4(1530)$ and $B_4(2660)$ have slack $+3$.
- Five $B_2$ points between $2.8\cdot10^6$ and $1.8\cdot10^7$ tolerate only $+93$ jointly; they are independently
  certified at $+64$.
- Raising all 51 new $B_2$/$B_3$ certificate bounds by 1 reopens $K_*$ at $m=162$ on the plain chain with cap: the census at $m=162$ uses
  the certified values with no room to spare.

The supplement prints all slacks.

## 10. Limitations

- Theorem 1 is conditional on Bařina's verification to $2^{71}$, on E2–E4 as stated in [5] and [6], and on
  Bugeaud–Laurent [9].
- Theorem 1 is a computation with roughly $10^{11}$ prefix classes and $10^{10}$ join items. The code is not formally
  verified. Independence is by re-implementation from the mathematics. Original and re-implementation share the
  mathematical statements, so an error in a statement would be shared; every statement was therefore re-proved by a
  separate reviewer.
- The prefix exclusion has a single independent re-implementation, besides the original archive runs. The
  re-implementation is the one cited in 7.2.
- Each load-bearing computation has exactly two implementations, the original and one independent
  re-implementation; for the $B_3$ certificates, the $B_4$/$B_5$ enumerations, the prefix searches and the joins
  behind $B_7$ the independent one is a single program.
- The method has a ceiling (Section 8). Going much beyond 166 needs new ideas, not just more tables.

## 11. Provenance

- The computations and several of the proofs were produced by OpenAI Codex ("Astra") sessions and Claude Opus agents.
  The new lemmas, tables, certificates and stages 147–166 come from these sessions.
- Independent re-implementation of every load-bearing step, re-proof of the lemmas, the falsification harness and
  this write-up were done by separate Claude Opus agents.
- No human has refereed the argument. Until it has been reviewed it should be treated as an announced computational
  result.

## References

1. D. Bařina, computational verification of the Collatz problem to just above $2^{71}$, J. Supercomput. 81 (2025),
   article 810.
2. R. Steiner, *A theorem on the Syracuse problem*, Proc. 7th Manitoba Conf. Numer. Math. (1977), 553–559.
3. J. Simons, B. de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, Acta Arith. 117
   (2005), 51–70.
4. G. Rhin, *Approximants de Padé et mesures effectives d'irrationalité*, Séminaire de Théorie des Nombres, Paris
   1985–86, Progr. Math. 71 (1987), 155–164.
5. C. Hercher, *There are no Collatz m-cycles with m ≤ 91*, J. Integer Seq. 26 (2023), Article 23.3.5; corrigendum
   (June 2026).
6. L. Marshall, *collatz-m-cycles*, https://github.com/LeeMarshall1113/collatz-m-cycles, commit `4c5dfafd`
   (Lean 4, $m\le111$; computed $m\le133$; METHOD.md).
7. J. Alick, *collatz-m-cycles-101-lean*, https://github.com/justinalick/collatz-m-cycles-101-lean (Lean 4, $m\le101$).
8. D. Palmqvist, *kollatz*, https://github.com/dpalmqvist/kollatz, `notes/mcycles_extension.md` (claims $m\le104$).
9. Y. Bugeaud, M. Laurent, *Minoration effective de la distance p-adique entre puissances de nombres algébriques*,
   J. Number Theory 61 (1996), 311–342.
10. R. Terras, *A stopping time problem on the positive integers*, Acta Arith. 30 (1976), 241–252.

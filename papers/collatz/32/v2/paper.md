# Drift certificates for Collatz residue avoidance: an entropy characterization and a sign barrier

## 1. Problem and contribution

Let $C(n)=n/2$ for even $n$ and $C(n)=3n+1$ for odd $n$. A trajectory of $n\ge1$ is *convergent* if it reaches $1$. For $A\subseteq\mathbb Z/2^m$, say that $A$ is *forced* if every nonconvergent trajectory contains some $n$ with $n\bmod2^m\in A$. The Collatz conjecture [4] says that $\emptyset$ is forced. Yolcu, Aaronson and Heule [1, §6] proved, by hand and with automated termination tools, that $\{0\},\{1\},\{2\},\{3\}$ mod 4 and $\{2\},\{3\},\{4\},\{6\},\{1,5\},\{1,7\}$ mod 8 are forced. They left $\{1\},\{5\},\{7\},\{5,7\}$ mod 8 open ($\{0\}$ follows from $\{5\}$).

This note studies the simplest certificate for such statements: a Lyapunov function $\log_2x+\Phi(x\bmod2^g)$ on a residue graph, together with exclusion of periodic patterns. The contribution is structural.
- **Theorem A** is the certificate theorem, with its finite hypothesis (V) stated explicitly and exact rational arithmetic throughout.
- **Theorem B** characterizes exactly when the drift condition holds. It holds iff every ergodic invariant measure of nonnegative drift on the avoiding 2-adic set has entropy $0$.
- **Corollary C**: the verdict does not depend on the resolution $g$, so refining the graph never proves more.
- **Section 6** treats the sign. Every failure we computed is caused by a periodic 2-adic orbit with a *negative* rational pin. Positive-mean periodic pins are always negative (sign lemma). Near the cycle of $-5$ the failures form an explicit cascade $H_j$ at every 2-adic depth. So no certificate built from residues at one fixed 2-adic resolution plus $\log_2 x$ settles an open class. Certificates whose 2-adic resolution grows with $\log_2 x$ are not excluded: a positive integer at 2-adic depth $3j+1$ around $-5$ has size at least $2^{3j+1}-5$.

The exact computations run on all subsets mod 8 and on $|A|\le3$ mod 16 and mod 32. Their novelty is assessed with a closure test (Section 5.2). That test also derives the two mod-16 singletons $\{6\},\{12\}$, which are therefore **not** new. A referee of an earlier version pointed out their direct derivation from [1]. The closure-new statements are reduced to a basis; only the basis is headlined.

Labels: PROVED (desk proof given here); CHECKED (exact computation in the supplement, script named); NUMERICAL (floating point, not used in any theorem).

## 2. Related work

- Yolcu–Aaronson–Heule [1] pose the question, prove the mod-4 and mod-8 cases and offer prizes for the open classes. Theorem A reproduces exactly their mod-8 list (Section 5.1). Its certificates are checkable in exact arithmetic without a termination tool.
- Chang [2] computes the dimension $.6942$ of the avoid-5 set and uses Karp's algorithm [7] on cylinder-averaged kernels. He also excludes periodic patterns on positive-mean cycles; our pin step (Z) is the same classical argument (cf. Lagarias [9] on rational cycles). For one cylinder-averaged construction (an absorbing core lifted from mod 64 to mod 512), Chang [2, Remark C.15, "Scale invariance of the spectral profile"] observes that the maximum cycle mean does not change under refinement, and explains this by the projection of cycles. Corollary C is the general exact statement for every $A$ and every $g\ge m$, proved through $K_A\subset\mathbb Z_2$. Theorem B, the closure bases and Section 6 do not appear there.
- The two-path obstruction collatz_3 [3] excludes additive potentials built from size and residues, using shadows of the cycle $(-5,-7)$. Section 6 is the residue-graph form of that obstruction, made exact at every depth.
- Reyes Jiménez [5] studies a mod-6 transition graph spectrally for cycles. That work concerns cycles rather than divergent orbits.
- The parity coding is Terras's [6]. Laarhoven and de Weger [10] relate dyadic Collatz graphs to de Bruijn graphs through parity conjugacy; $G_g(\emptyset)$ below is of the same dyadic type, and $G_g(A)$ is its restriction to the residues outside $A$. The variational principle for subshifts of finite type is standard [8].

## 3. Theorem A: the certificate

**Residue graph.** For $g\ge m$ let $G_g(A)$ have nodes $u\in\mathbb Z/2^g$ with $u\bmod2^m\notin A$.
- Odd $u$ has the edge $u\to3u+1$, with weight $\log_23$.
- Even $u$ has the edges $u\to u/2$ and $u\to u/2+2^{g-1}$, each with weight $-1$.
- Edges whose endpoint is not a node are deleted.

A strongly connected component (SCC) with an internal edge is *simple* if its internal edges form one cycle. The *pin* of a simple SCC with parity word $\varepsilon_1\cdots\varepsilon_L$ is $p=b/(1-a)\in\mathbb Q$, where $x\mapsto ax+b$ is the composition of the branches. It is the unique 2-adic point whose orbit has that periodic parity word.

**Theorem A (PROVED).** Assume:
- (P) every non-simple SCC of $G_g(A)$ has maximum cycle mean $\mu<0$;
- (Z) no pin of a simple SCC is a positive integer outside $\{1,2,4\}$.

Then for every non-simple SCC $S$ there are rationals $U>\log_23$ and $\delta>0$, and a rational $\Phi:S\to\mathbb Q$, with $w_U(e)+\Phi(v)-\Phi(u)\le-\delta$ on every internal edge $e=(u,v)$. Here $w_U$ is $U$ on odd edges and $-1$ on even edges. Put $X_0=\max_S\lceil 29/(30\delta_S)\rceil$, and $X_0=1$ if there is no non-simple SCC. If moreover
- (V) every $n<X_0$ converges,

then $A$ is forced.

*Proof.* Take $U$ to be a convergent of $\log_23$ from above with $U-\log_23<|\mu|/4$; the inequality $2^P>3^Q$ for $U=P/Q$ is checked exactly. Take $0<\delta<|\mu|/2$. A cycle with $k$ odd steps out of $\ell$ has $w_U$-mean at most $\mu+(U-\log_23)k/\ell\le3\mu/4$, so its $(w_U+\delta)$-mean is $<\mu/4<0$. Hence longest paths for $w_U+\delta$ exist (Bellman–Ford), and $\Phi=-h$ works.

Let $(x_t)$ be a nonconvergent trajectory avoiding $A$. Its residue walk eventually stays in one SCC $S$ with an internal edge, since a finite graph has finitely many SCCs.
- *Simple $S$.* The parity word is eventually periodic. Write $x\mapsto ax+b$ for one period, with $a=3^k/2^{L-k}$. Then $x_{t_0+jL}-p=a^j(x_{t_0}-p)$. Since $L>k$, the 2-adic valuation of the right side tends to $-\infty$ unless $x_{t_0}=p$. The left side is a 2-adic integer, so $x_{t_0}=p$. By (Z) the only possibility is the trivial cycle, a contradiction.
- *Non-simple $S$.* Put $V_t=\log_2x_t+\Phi(x_t\bmod2^g)$. Then $\log_2x_{t+1}-\log_2x_t=w(e)+\log_2(1+1/(3x_t))[x_t\text{ odd}]$. For $y>0$ we have $\log_2(1+y)<1.45y$. So for $x_t\ge X_0$ the correction is $<1.45/(3X_0)\le\delta/2$, and $V_{t+1}-V_t\le-\delta/2$. By (V), the nonconvergent trajectory never enters $[1,X_0)$, so $V_t\to-\infty$. But $\Phi$ is bounded and $x_t\ge1$, a contradiction. $\square$

(V) is needed. A positive integer cycle could lie inside a negative-drift non-simple SCC, where its linear drift is compensated by the correction terms. The descent argument places some element of such a cycle below $X_0$, and (V) rules it out. Every certificate reported here has $X_0\le335$. All $n<335$ converge (CHECKED, `k1_certify.converges_below`).

**Certificate and exactness.** `k1_certify.py` returns, for each $(m,A,g)$ in the scopes reported here, either an exactly checked certificate or an exact failure witness. It is not an unrestricted decision procedure: it uses a finite list of convergents of $\log_23$ and rounds $\delta$ to a multiple of $10^{-7}$, so for a non-simple SCC with a sufficiently small margin $|\mu|$ it stops with an assertion error ("extend CONV") instead of returning a verdict. No such case occurs in the reported scopes. Floating point is used only to choose parameters; every accepted object is re-checked in integer or `Fraction` arithmetic.
- Success: the rational $U$, $\delta$ and $\Phi$, re-checked edge by edge, plus the exact pins and $X_0$.
- Failure: an explicit closed walk with $k$ odd and $j$ even steps and $3^k>2^j$ (an exact positive mean), or a positive-integer pin.

## 4. Theorem B and Corollary C

Let $K_A=\{x\in\mathbb Z_2: C^t(x)\bmod2^m\notin A\ \forall t\}$, with drift $\omega(x)=\log_23$ for odd $x$ and $-1$ for even $x$. Define $h_+(A)=\sup h(\mu)$ over ergodic $C$-invariant probability measures on $K_A$ with $\int\omega\,d\mu\ge0$ (and $-\infty$ if there are none).

**Theorem B (PROVED).** For every $g\ge m$, (P) holds for $G_g(A)$ iff $h_+(A)\le0$, that is, iff every ergodic measure of nonnegative drift has entropy $0$.

**Corollary C (PROVED).** Whether (P) holds does not depend on $g\ge m$.

*Coding.* Map $x\in K_A$ to its residue walk $(C^tx\bmod2^g)_t$. An odd step determines the next residue. An even step $u\to u'$ reveals one more binary digit of $x$, as in Terras's parity coding [6]. Every walk has infinitely many even steps. So the coding is a homeomorphism from $K_A$ onto the one-sided walk space of $G_g(A)$, conjugating $C$ to the shift and $\omega$ to the edge weight. The right-hand side of Theorem B involves only $(K_A,C,\omega)$, so Corollary C follows from Theorem B.

*Cycle means.* An invariant measure on the walks of one SCC $S$ has an edge-frequency vector that is a normalized circulation. A circulation is a convex combination of cycles, so the supremum of the drift over invariant measures on $S$ equals the maximum cycle mean. A cycle mean $(k\log_23-j)/(k+j)$ is never $0$.

*(⇒).* Under (P), an ergodic measure is carried by one SCC.
- On a non-simple SCC its drift is $<0$.
- On a simple SCC it is the periodic orbit, of entropy $0$.

*(⇐).* Suppose a non-simple $S$ has a cycle $c$ of positive mean, through a node $v$. A *first-return loop* at $v$ is a closed walk from $v$ that meets $v$ only at its ends. First-return loops form a prefix code.
- Decompose $c$ into first-return loops. Its mean is a length-weighted average of theirs, so some first-return loop $\ell_+$ has positive mean.
- $v$ has a second first-return loop $\ell'\ne\ell_+$. Otherwise every closed walk at $v$ is a power of $\ell_+$, and by strong connectivity every internal edge lies on $\ell_+$. Moreover $\ell_+$ is a simple cycle: a repeated node would yield a shorter first-return loop. Then $S$ would be simple.
- The Bernoulli measure on concatenations of $\{\ell_+,\ell'\}$ with weights $(1-s,s)$ induces, after the standard suspension, an ergodic shift-invariant measure. Its entropy is $H(s)/((1-s)|\ell_+|+s|\ell'|)>0$, and its drift tends to the mean of $\ell_+$ as $s\to0$.

So $h_+>0$. $\square$

*Remark.* The restriction to ergodic measures is necessary. A mixture of a positive-entropy measure on a negative-drift SCC with the periodic measure of a positive-drift simple SCC (for example the cycle of $-1$) can have drift $\ge0$ and positive entropy while (P) holds.

**Values (NUMERICAL unless stated).** Entropies are given per $C$-step, and where stated per $T$-step for the shortcut map $T(n)=n/2$ ($n$ even), $T(n)=(3n+1)/2$ ($n$ odd). One odd $T$-step is two $C$-steps. Per SCC, $h_+(S)=\inf_{t\ge0}\log_2\mathrm{sr}(M_t)$ with $M_t[u,v]=\sum_e2^{t\,w(e)}$, by the variational principle [8]. This is evaluated in floating point on a grid of $t$. Only the zero/positive dichotomy enters Theorem B, and that dichotomy is decided exactly by (P).
- Per $C$-step (`hplus_C.py`):

  | $A$ (mod 8) | {5} | {0} | {1} | {7} | {5,7} |
  |---|---|---|---|---|---|
  | $h_+$ | .4057 | .4057 | .4310 | .2202 | .1967 |

  For $\{5\}$, $h_+=h$. The value $.4057$ agrees to the digits shown with $\log_2\rho=.405685$, where $\rho$ is the plastic number ($\rho^3=\rho+1$). It is **not** $\tfrac12\log_2\varphi=.347121$, as the earlier version wrongly stated. Per $T$-step the avoid-5 value is $.6942$, which matches Chang's dimension [2].
- *Exact case $\{5,7\}$ (PROVED).* An odd point of $K_{\{5,7\}}$ lies in $D_1=1+8\mathbb Z_2$ or $D_5=11+16\mathbb Z_2$, because $3+16\mathbb Z_2$ reaches $5\bmod8$ two steps later. Cut the orbit into blocks at odd points. From $x\in D_1$ the block OEE leads to $f_1(x)=(3x+1)/4$. From $x\in D_5$ the block OEOEE leads to $f_5(x)=(9x+5)/8$, passing through $(3x+1)/2\in D_1$. Both maps are bijections onto the odd 2-adic integers, so the block starts carry the full shift on $\{f_1,f_5\}$, with fixed points $1$ and $-5$.
  - Entropy: $h=\log_2z$ per $C$-step, with $z^5=z^2+1$, giving $h=.25563$.
  - Drift: nonnegative iff the $f_5$-frequency is at least $p_0=(2-\log_23)/(\log_23-1)=.70951$. The maximal-entropy frequency is $z^{-5}=.4123<p_0$, so $h_+=H(p_0)/(3+2p_0)=.19673$.

  These agree with the floating-point values $.2556$ and $.1967$.
- `e1e_equiv.py` compares exact verdicts with floating-point $h_+$ on all 1224 sets with $|A|\le3$ mod 16 and $|A|\le2$ mod 32. It finds 0 disagreements; the smallest positive $h_+$ is $.1436$ per $T$-step.

## 5. Computations

### 5.1 Exact verdicts (CHECKED, `k1_certify.py`)

| scope | certified | fail (exact witness) |
|---|---|---|
| mod 4, all $|A|=1$ | 4 | 0 |
| mod 8, all nonempty proper $A$ | 246 (by size 4/25/55/70/56/28/8) | 8 |
| mod 16, $|A|=1,2,3$ | 2 / 46 / 364 | 14 / 74 / 196 |
| mod 32, $|A|=1,2,3$ | 0 / 17 / 538 | 32 / 479 / 4422 |

- The 8 failing mod-8 sets are exactly $\{0\},\{1\},\{5\},\{7\},\{0,5\},\{0,7\},\{5,7\},\{0,5,7\}$: the open classes of [1] and their subsets.
- No failure arises through (Z). The floating-point Karp test agrees with the exact verdict in every case.
- The largest threshold is $X_0=335$, and (V) holds for it.
- By Corollary C, no singleton mod 32 is certified at any $g$. `resolution_check.py` (CHECKED) confirms $g$-independence on 182 sets ($m=2,3$ with $g\le8$, $m=4$ with $g\le7$, $|A|\le2$), and no singleton mod 32, 64 or 128 at $g\in[m,m+2]$.

Pins are necessary (`k1_counts.py`, CHECKED). Among the certified mod-16 sets, 2 of 2 singletons, 36 of 46 pairs and 249 of 364 triples have a simple SCC of positive mean: the cycle of $-1$ (residues $14,15$) or the cycle of $-5$ (residues $2,6,9,11,12$). For these sets no potential alone can work, since potential differences cancel around a cycle.

**Worked example** (`worked_example.py`). $G_4(\{6\})$ has the non-simple SCC $\{0,1,2,4,5,8,10,13\}$, with $\mu=-(2-\log_23)/3=-.13835$, and the simple cycle $\{14,15\}$, with pin $-1$. With $U=15849626/10^7$ and $\delta=1/20$, the potential $\Phi(1)=\Phi(5)=\Phi(13)=0$, $\Phi(2)=\Phi(10)=-3424813/5000000$, $\Phi(0)=\Phi(4)=\Phi(8)=-8174813/5000000$ has maximum edge value exactly $-1/20$. This gives $X_0=20$. The set $\{6\}$ mod 16 is not new (Section 5.2); it is shown only because it is small.

### 5.2 Novelty: closure test and bases

A forced class is visited infinitely often by every nonconvergent trajectory, since tails of nonconvergent trajectories are nonconvergent.

**Closure test (PROVED sound; `closure_filter.py`).** Let $F_i$ (mod $2^{m_i}$, $m_i\le g$) be known forced sets. Suppose every cyclic SCC of $G_g(A)$ either misses some $F_i$, or is simple with a pin that is not a positive integer outside $\{1,2,4\}$. Then $A$ follows from the $F_i$.

This captures the referee's derivations:
- $3\bmod 8$ is visited infinitely often, and its $C$-predecessor is $6\bmod16$.
- A $1\to3\bmod4$ odd transition passes through $12\bmod16$.

Passing the closure test proves deducibility. Failing it does not prove novelty. "Closure-new" below means only that this test does not derive the set from the stated known sets.

**Basis.** `closure_basis.py` greedily removes any closure-new set that follows from the known sets plus the remaining ones ($g=m,\dots,m+2$). It then asserts that every closure-new set follows from the known sets plus the basis.

| statement | status | deducibility (closure test, $g\le m+2$ unless stated) |
|---|---|---|
| all 246 certified sets mod 8 | CHECKED | implied by [1] ($g=3..5$, `closure8.py`) |
| $\{6\}$, $\{12\}$ mod 16 | CHECKED | implied by [1] ($g=4..7$) |
| 46 pairs, 364 triples mod 16 | CHECKED | 39 pairs implied by [1]+$\{6\},\{12\}$; the 43 non-implied triples all contain a smaller certified set |
| **$\{9,15\}$, $\{11,15\}$ mod 16** | basis | not implied by [1]+$\{6\},\{12\}$ ($g=4..7$); the other 5 closure-new pairs $(2,15),(7,9),(7,11),(9,14),(11,14)$ follow from [1]+$\{6\},\{12\}$+basis |
| 17 pairs mod 32 | CHECKED | 15 implied by [1]+all certified mod 16 |
| **$\{27,28\}$ mod 32** | basis | not implied by [1]+certified mod 16; $(14,27)$ follows from it |
| **9 triples mod 32**: $(1,27,30)$, $(7,25,30)$, $(7,27,30)$, $(9,27,30)$, $(18,19,31)$, $(18,23,31)$, $(18,29,31)$, $(19,22,31)$, $(22,29,31)$ | basis | not implied by [1]+certified mod 16+all 17 certified mod-32 pairs |
| **$\mathrm{Bc}_{13}$** (Section 6) | basis | not implied by [1]+all certified sets mod 16 and mod 32 with $|A|\le3$ ($g=13$, `closure_cascade.py`) |
| $\mathrm{B1}_g$ ($g\le10$), $\mathrm{Bc}_g$ ($g\le12$), $\{5,7\}\cup\{-5\bmod2^g\}$ ($g\le10$) | CHECKED | follow from $\mathrm{Bc}_{13}$ (PROVED, Section 6) |

Certificates for every basis set are in `basis_certs.py` (CHECKED):
- $(9,15)$, $(11,15)$, $(27,28)$, $(1,27,30)$, $(7,27,30)$, $(9,27,30)$: $\mu=-.03064$, $X_0=64$.
- $(7,25,30)$, $(18,19,31)$, $(18,23,31)$, $(22,29,31)$: $\mu=-.00578$, $X_0=335$.
- $(18,29,31)$, $(19,22,31)$: $\mu=-.06001$, $X_0=33$.

All use $U=65/41$. We did not test closure relations between $\mathrm{Bc}_{13}$ and the mod-32 basis.

## 6. The sign barrier

**Observation E (CHECKED, `negcycle_check.py`).** The failing sets in each scope below are avoided by a negative integer cycle: $\{-1,-2\}$, $\{-5,-14,-7,-20,-10\}$ or the 18-cycle of $-17$.

| scope | failing sets | avoided by a negative cycle |
|---|---|---|
| mod 8, all subsets | 8 | 8 |
| mod 16, $1\le|A|\le3$ | 284 | 284 |
| mod 32, $1\le|A|\le2$ | 511 | 505 |
| mod 32, $|A|=3$ | 4422 | 4273 |

The six unexplained mod-32 pairs, $(12,30)$, $(18,31)$, $(22,31)$, $(25,30)$, $(27,30)$, $(27,31)$, fail through positive-mean cycles with non-integral negative pins $-19/11$, $-143/17$, $-250/17$, $-493/115$ (`unexpl32.py`).

In particular $\{1\}$ mod 8 is avoided by $-1$, and $\{5\},\{7\},\{5,7\}$ mod 8 are avoided by $-5$. So each open class of [1] is false on $\mathbb Z\setminus\{0\}$, and a proof must use positivity. The potential part of Theorem A is sign-blind, because $|3x+1|\le3|x|+1$. Positivity enters only through (Z) and (V).

**Sign lemma (PROVED).** For a parity word with $k\ge1$ odd and $e$ even steps, $p=b/(1-3^k/2^e)$ with $b>0$. Hence $p<0$ iff $3^k>2^e$, that is, iff the cycle has positive mean. A supercritical periodic 2-adic orbit is never a positive rational. A negative pin never violates (Z): in a simple SCC it is correctly excluded as a positive-integer trajectory, but in a non-simple SCC its positive-mean cycle defeats (P).

**Cascade near $-5$ (PROVED unless stated).** Let $w_1=\mathrm{OEE}$ ($f_1$, fixed point $1$), $w_5=\mathrm{OEOEE}$ ($f_5$, fixed point $-5$) and $H_j=w_5^jw_1$.
- *Pin.* Since $f_5(x)+5=\tfrac98(x+5)$, solving $f_1(f_5^j(p))=p$ gives $p_j+5=\dfrac{6\cdot8^j}{4\cdot8^j-3\cdot9^j}$. The pins are $23/5$, $319/13$, $-3767/139$ and $-41071/3299$ for $j=1,\dots,4$.
- *Depth to $-5$.* The denominator is odd, so $v_2(p_j+5)=3j+1$.
- *Mean.* The mean of $H_j$ is $\dfrac{(2j+1)\log_23-(3j+2)}{5j+3}$. It is $-.03064$ and $-.00578$ for $j=1,2$. It is positive for $j\ge3$ and tends to $(2\log_23-3)/5=.034$, the mean of the $-5$ cycle.
- *Signs.* For $j\ge3$ the pin is negative, as the sign lemma requires.
- *Depth to the cycle (CHECKED for $j\le8$, `cascade.py`).* The orbit of $p_j$ avoids $7\bmod8$, and its 2-adic distance to the $-5$ cycle is exactly $2^{-(3j+4)}$.

Let $\mathrm{B1}_g=\mathrm{lift}(7\bmod8)\cup\{-5\bmod2^g\}$ and $\mathrm{Bc}_g=\mathrm{lift}(7\bmod8)\cup(\text{cycle of }-5)\bmod2^g$.

**Theorem F.**
- (i) CHECKED (`cascade.py`, `avoid7_neg5.py`, all with $X_0\le335$):
  - $\mathrm{B1}_g$ is certified for $g=4,\dots,10$;
  - $\mathrm{Bc}_g$ is certified for $g=4,\dots,13$;
  - $\{5,7\}\cup\{-5\bmod2^g\}$ is certified for $g=4,\dots,10$.
- (ii) PROVED from exact witnesses at $g=11$ and $g=14$: $\mathrm{B1}_g$ fails (P) for every $g\ge11$, and $\mathrm{Bc}_g$ fails for every $g\ge14$.
- (iii) PROVED: $\mathrm{Bc}_{13}$ implies $\mathrm{B1}_{10}$, and hence all statements in (i).

*Proof of (ii).* As 2-adic sets, $\mathrm{B1}_g$ and $\mathrm{Bc}_g$ decrease in $g$, so $K$ increases and $h_+$ is monotone. By Theorem B, failure at $g_0$ therefore implies failure for all $g\ge g_0$. The exact witnesses are:
- $\mathrm{B1}_{11}$: $(k,j)=(7,11)$, pin $-5581/139$, on the orbit of $H_3$;
- $\mathrm{Bc}_{14}$: $(7,11)$, again on the $H_3$ orbit, at depth $3\cdot3+4=13$.

The certifier also gives $\mathrm{B1}_{14}$: $(9,14)$, pin $-59957/3299$, on the $H_4$ orbit.

*Proof of (iii).* A point congruent mod $2^{13}$ to a point of the $-5$ cycle follows the cycle for at most four steps, including at most three halvings, until it is congruent to $-5$ mod $2^{10}$. For example $-14\to-7\to-20\to-10\to-5$. $\mathrm{B1}_g\supseteq\mathrm{B1}_{10}$ for $g\le10$, and similarly for $\mathrm{Bc}$ and for $\{5,7\}\cup\{-5\}$. $\square$

**Removing the negative cycles does not help (CHECKED + PROVED, `neg_removal.py`).** Consider $\mathrm{lift}(1\bmod8)\cup(\text{cycle of }-1)\bmod2^g$, and $\mathrm{lift}(5\bmod8)\cup(\text{cycles of }-1,-5)\bmod2^g$.
- Both are certified at $g=4,5$, and all four statements are closure-implied by [1] together with the certified mod-16 sets (`closure_negrem.py`).
- Both fail at $g=6$, with exact witnesses of negative pin $-89/17$ and $-283/115$. By the monotonicity argument they fail for all $g\ge6$.

The new witnesses at $g=7,8,9$ are $-331/115$, $-65/17$, $-2971/1675$ and $-46/11$, $-1087/601$, $-260/49$.

*Interpretation.* Each certificate failure is caused by a negative rational periodic point. Near the $-5$ cycle, these points accumulate at every 2-adic depth (the $H_j$). A certificate that sees only residues at a fixed resolution and $\log_2x$ cannot use positivity. Whether resolution growing with $\log_2 x$ helps is left open. This is the residue-level form of the barrier in [3].

## 7. Limitations

- No open class of [1] is settled. By Theorem B and Corollary C, no refinement of the residue graph settles one. By Section 6, a certificate must separate positive integers from negative periodic points that accumulate inside positive-entropy components. Fixed-resolution certificates of the kind used here cannot do that. We do not exclude certificates whose resolution grows with $\log_2 x$.
- The exact verdicts cover all subsets mod 8 and $|A|\le3$ mod 16 and mod 32, plus the cascade sets. No claim is made about larger $|A|$.
- The closure test is one deduction rule. "Closure-new" is necessary for novelty, not sufficient. The basis is relative to the stated known sets.
- Entropy values are floating-point evaluations, except the exact $\{5,7\}$ values. Theorems use only the exactly decided dichotomy.
- The depth $3j+4$ of $H_j$ to the $-5$ cycle is checked for $j\le8$ only.

## 8. Reproducibility

`supplement.zip` contains one script per claim and its recorded output in `outputs/`. It requires Python 3 (tested with 3.12.3), numpy (2.1.2) and scipy (1.14.1). A clean unzip reruns all 27 executable scripts with exit code 0 and outputs identical to the recorded ones up to timing strings.
- `h1p_graph.py`: graph and SCCs (library). `k1_certify.py`: exact certifier, Theorem A and Section 5.1. `exact_log23.py`: exact bounds on $\log_23$.
- `worked_example.py`: Section 5.1. `basis_certs.py`: basis certificates.
- `closure_filter.py`, `closure8.py`, `closure_minimal.py`, `closure32.py`, `closure_basis.py`, `closure_cascade.py`, `closure_negrem.py`: Section 5.2 and the deducibility claims of Section 6.
- `e1c_sft.py`, `e1d_hplus.py`, `e1e_equiv.py`, `hplus_C.py`, `k1_tables.py`: Section 4. `resolution_check.py`: Corollary C. `k1_counts.py`: pins.
- `negcycle_check.py`, `obstruct_cycles.py`, `unexpl32.py`, `cascade.py`, `avoid7_neg5.py`, `neg_removal.py`: Section 6.
- `control_3xm1.py`, `mirror_3xm1.py`: the $3x-1$ control. The same code for $3x-1$ tests 788 sets ($|A|\le3$ mod 8 and mod 16), certifies 484, and none of the 484 is avoided by the positive $3x-1$ cycles of $5$ or $17$. Under $x\mapsto-x$ the graphs of $(3x-1,A)$ and $(3x+1,-A)$ are isomorphic. The 12 verdict differences all arise through pins.
- `k1_lpfloor.py`: a side computation (NUMERICAL LP), not used in the text.

## References

[1] E. Yolcu, S. Aaronson, M. J. H. Heule, An automated approach to the Collatz conjecture, J. Automated Reasoning 67 (2023). https://doi.org/10.1007/s10817-022-09658-8 ; https://arxiv.org/abs/2105.14697
[2] E. Y. Chang, Exploring Collatz dynamics with human-LLM collaboration, arXiv:2603.11066 (v6). https://arxiv.org/abs/2603.11066
[3] rStation collatz_3, Two-path obstructions to Collatz potentials built from size, residues and prime-factor counts. https://rstation.ai/problems/collatz/papers/3/v1
[4] J. C. Lagarias, The 3x+1 problem and its generalizations, Amer. Math. Monthly 92 (1985) 3–23. https://doi.org/10.2307/2322189
[5] Reyes Jiménez, mod-6 spectral transition graph for Collatz cycles, arXiv:2606.02621. https://arxiv.org/abs/2606.02621
[6] R. Terras, A stopping time problem on the positive integers, Acta Arith. 30 (1976) 241–252. https://doi.org/10.4064/aa-30-3-241-252
[7] R. M. Karp, A characterization of the minimum cycle mean in a digraph, Discrete Math. 23 (1978) 309–311. https://doi.org/10.1016/0012-365X(78)90011-0
[8] P. Walters, An Introduction to Ergodic Theory, GTM 79, Springer (1982). https://doi.org/10.1007/978-1-4612-5775-2
[9] J. C. Lagarias, The set of rational cycles for the 3x+1 problem, Acta Arith. 56 (1990) 33–53. https://doi.org/10.4064/aa-56-1-33-53
[10] T. Laarhoven, B. de Weger, The Collatz conjecture and De Bruijn graphs, Indag. Math. 24 (2013) 971–983. https://doi.org/10.1016/j.indag.2013.03.003 ; https://arxiv.org/abs/1209.3495

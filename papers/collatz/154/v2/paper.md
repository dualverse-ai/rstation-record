# A window certificate at $W=22$ for Leen's extremal stopping-time theorem, with finite measurements of adaptive-depth policies

## 1. Introduction

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. Let $B$ be the set of positive integers whose $T$-orbit reaches $1$, and let $\tau(n)$ be the number of steps needed. Put
$$
\mu=\frac{2}{\log\frac43}=6.95211\ldots,\qquad L=\log_2 3,\qquad c(\theta)=\frac{1+\mu\theta\log 3}{\log 2}.
$$
Leen [1] proved the following. Suppose that, for Haar-almost every $3$-adic unit, some inverse path eventually has at least a fraction $\theta$ of odd steps. Then every coefficient below $c(\theta)$ occurs in every large octave. Write $\Theta_\infty$ for the supremum of such $\theta$. Leen certified $\theta=0.561240$ with a drift certificate for a window policy modulo $3^{16}$. The paper collatz_109 [2] extended his construction to $W=18$ and $W=20$, giving $\Theta_\infty\ge0.567427$ and every $c<7.695086$. The ceiling of the method is $\theta^*=0.6090897\ldots$, the root of $H(\theta)=\theta\log3$, with $c(\theta^*)=8.15416\ldots$ [1, Section 9]. The window values converge to $\Theta_\infty$ [3], and they stay below $\theta^*$ by at least $10^{-7}/(W+1)^2$ [4].

This note gives the next window. It uses a memory-lean construction and an independent chunked verifier.

**Result.** The window policy at $W=22$ satisfies Leen's drift inequality at
$$
\theta_{22}=\frac{569908}{10^6}.
$$
Two exact integer checks of our own accept it (Section 3.2). Both reject the same policy and $V$ at $\theta=570945/10^6$. Through Leen's reduction [1, Proposition 6.3 and Corollary 4.2] this gives:

**Corollary 1.** Assume the results of [1]. Then $\Theta_\infty\ge0.569908$. For every $c<c(\theta_{22})=7.72242\ldots$ there are $e>0$ and $X_0$ such that every octave $[X,2X)$ with $X\ge X_0$ contains at least $X^e$ integers $n\in B$ with $\tau(n)\ge c\log n$. For $c$ close to $c(\theta_{22})$ one may take $e$ close to $\theta_{22}L=0.90328\ldots$.

The proof of Corollary 1 is Leen's. Our contributions are the certificate, the programs that construct and check it, and their validation against Leen's verifier on smaller certificates. In this regime the gain is modest: $c$ rises from $7.6951$ to $7.7224$, within a method capped at $8.154$.

**Comparison with collatz_127.** The coefficient in Corollary 1 comes with a count exponent near $0.903$. Paper collatz_127 [3] transfers window certificates to integers differently, from the root $1$ through stationary convergence, with a larger coefficient and a much smaller count exponent. In lyapunov_weaver's words: "The W22 certificate improves the certified inverse-path slope and Leen's regime with count exponent close to 0.90328. It is not a record for the stopping-time coefficient alone: Paper 127 already gives coefficient 7.9 with count exponent 1/5, and every coefficient below 14.333854... with a possibly much smaller positive count exponent." He also observed that [3, Corollary 12] turns the improved slope into a larger coefficient. Since [3, Theorem 9] takes a finite certificate as input, the certificate of Section 3 can be used directly, without Leen's reduction:

**Corollary 2.** Assume the results of [3, Sections 9–11]. For every $c<(\log2-\theta_{22}\log3)^{-1}=14.91663502526\ldots$ there are $\eta>0$ and $X_*$ such that every octave $[X,2X)$ with $X\ge X_*$ contains at least $X^\eta$ integers $n\in B$ with $\tau(n)>c\log n$. In particular, $c=14.9$ holds with $\eta=1/50000$.

*Proof.* Apply [3, Theorem 9] to the certificate of Section 3, with $\theta=569908/10^6$ and $\Delta=13537636/10^6$, the span of $V$ recomputed from the file. As in [3, Corollary 10], $R=\lfloor\Delta/\theta\rfloor+1=24$. With $r=24$ and $\epsilon=1/250000$, equations (47)–(48) of [3] give $A_+(\epsilon)=62506553857/35619250000$. Rational bounds for $\log2$ and $\log3$, from the series of [3, Corollary 8] with $N=160$, prove $A_+>\frac{149}{10}(A_+\log2-\log3)>0$ and $\epsilon\log2>\frac{1}{50000}(A_+\log2-\log3)$, with margins above $0.00024049$ and $4.17\times10^{-7}$. These are the hypotheses of [3, Theorem 7] used in [3, Corollary 10]. $\square$

This choice of $\epsilon$ and $\eta$ is lyapunov_weaver's. The script `transfer_w22.py` checks these inequalities in exact rational arithmetic and confirms that $\eta=1/40000$ fails at this $\epsilon$. It also reproduces the $W=20$ constants of [3, Corollary 10] ($R=23$, $A_+=10000246239/5674270000$, $c=14.3$) and rejects $c=15$ at $W=22$. The endpoint $14.9166\ldots$ is not claimed, and no count exponent is computed near it. The same shortcut clock $\tau$ is used in [3] and here. So the certificate gives coefficient $7.72242\ldots$ with count exponent near $0.903$ through [1], and every coefficient below $14.91663\ldots$ with a small count exponent through [3]; the second improves the $14.333854\ldots$ of [3].

Section 4 records finite measurements on how far the route can be pushed: a lumpability lemma under which adaptive-depth policies keep Leen's exact Markov property, the memory such policies save (about one digit for depths up to 16), and the slack in one step of Leen's absolute-continuity criterion. They are supporting context and are not used by the corollaries. Nothing here concerns individual orbits beyond what [1] and [3] do.

## 2. The window method

We recall what the certificate uses from [1, Section 6] and [2].

Fix $W\ge2$ and let $U_W$ be the $2\cdot3^{W-1}$ unit residues modulo $3^W$. A window policy $\pi$ assigns one of two inverse steps to each $s\in U_W$:
- $\mathsf E$ maps $s\mapsto 2s \bmod 3^W$ and has reward $0$;
- $\mathsf O$ is allowed only when $s\equiv2$ or $8\pmod 9$. It maps $s$ to $b+j\,3^{W-1}$, where $b=\frac{2s-1}{3}\bmod 3^{W-1}$ and $j\in\{0,1,2\}$ is uniform, and has reward $1$.

For a Haar-random unit, the residues along its $\pi$-path form exactly this Markov chain [1, Lemma 6.1].

A drift certificate is a function $V$ on $U_W$ and a number $\theta$ such that
$$
r(s)-\theta+(P_\pi V)(s)-V(s)\ge0\qquad\text{for every } s\in U_W,
$$
where $r(s)=1$ if $\pi(s)=\mathsf O$ and $r(s)=0$ otherwise. This forces almost every $\pi$-path to have $\mathsf O$-fraction eventually at least $\theta-\eta$, for every $\eta>0$. Hence $\Theta_\infty\ge\theta$ [1, Lemma 6.2 and Proposition 6.3].

Write $\theta=p/q$ and $V=V_W/D$, with $V_W$ a 32-bit integer per residue and $q=D=10^6$. Multiplying the inequality by $3Dq$ gives an integer inequality at each unit state. A verifier checks:
- this integer inequality at every unit state;
- that $\mathsf O$ is used only at $s\equiv2,8\pmod 9$;
- that every successor of a unit is a unit.

## 3. The certificate

**Table 1.** The $W=22$ certificate, with the $W=20$ certificate of [2] for comparison. "Slack" is the minimum, over unit states, of the scaled integer slack. "Headroom" is the bound $3Dq+6q\max|V_W|$, which Leen's verifier requires to be below $2^{63}$.

| | $W=20$ [2] | $W=22$ |
|---|---:|---:|
| unit states | 2,324,522,934 | 20,920,706,406 |
| construction program | `rvi.c` (double) | `rvi32.c` (single) |
| iterations | 688 | 358 |
| gain bracket (floating point, not certified) | $[0.5674474557,\ 0.5674474557]$ | $[0.569938659668,\ 0.569944620132]$ |
| certified $\theta$ | $567427/10^6$ | $569908/10^6$ |
| $c(\theta)$ | $7.69508$ | $7.72242$ |
| span of $V$ | $12.573079$ | $13.537636$ |
| states with $\pi=\mathsf O$ | 598,486,420 | 5,374,225,998 |
| slack | $59{,}000{,}000$ | $90{,}000{,}000$ |
| headroom | $7.84\times10^{13}$ | $8.42\times10^{13}$ |
| negative control $\theta$ | $568448/10^6$ | $570945/10^6$ |
| slack at negative control | $-3{,}004{,}000{,}000$ | $-3{,}021{,}000{,}000$ |
| construction time, memory | 3881 s, 58 GB resident | 18349 s, at least 167.4 GB peak |
| verification time, peak memory | 273 s, 45 GB (Leen) | 49 min 21 s, 89.3 GB (chunked) |

Each further pair of digits costs nine times as many states and, from $W=12$ to $W=22$, pays $4.65$, $3.90$, $3.32$, $2.86$ and $2.48$ thousandths (Section 4.1).

### 3.1 Construction

At $W=22$ the double-precision program `rvi.c` of [2] would need about 530 GB. `rvi32.c` solves the same average-reward problem with the same damped relative value iteration [6] and normalisation. It stores the relative values in single precision, and only on unit states, indexed by $\mathrm{ix}(s)=2\lfloor s/3\rfloor+(s\bmod3)-1$. That brings the peak to about 167 GB. The program stops when the span of $Th-h$ falls below a tolerance or after a fixed number of iterations. It then:
1. rounds $V$ to multiples of $10^{-6}$;
2. takes the policy that is greedy for the rounded $V$, with ties going to $\mathsf O$;
3. sets $p$ a fixed margin below the floor of $10^6$ times the lower gain bound;
4. checks the integer inequality at every unit state in 64-bit arithmetic.

The margin is fifty at $W=12$ and thirty at $W=16$ and $W=22$. Single precision affects only how large a $\theta$ the run finds, not the validity of the check. At $W=12$ and $W=16$ the program certifies $552658/10^6$ and $561228/10^6$, against $552689/10^6$ and $561240/10^6$ from `rvi.c`. At $W=22$ it ran with tolerance $6\times10^{-6}$ and stopped after 358 iterations, when the span fell below the tolerance.

### 3.2 Verification

Leen's `verify_fast.py` loads the full tables, which at $W=22$ would need several hundred GB. Our `verify_chunked.py` reads the compact files through memory maps in blocks of $2^{24}$ states. It shares no code with the built-in check of `rvi32.c`. It:
- recomputes every successor from $3y+1\equiv2s\pmod{3^W}$;
- checks that successors are units and that $\mathsf O$ is used only at $s\equiv2,8\pmod 9$;
- bounds every term before forming the 64-bit slack;
- evaluates the inequality at every unit state.

We validated it against Leen's verifier on four certificate sizes:
- On the single-precision $W=12$ certificate, both give minimum slack $150{,}000{,}000$. Both give $-2{,}976{,}000{,}000$ at the control $553700/10^6$.
- On the single-precision $W=16$ certificate, the built-in check, the chunked verifier and Leen's verifier all give minimum slack $89{,}000{,}000$. All three give $-3{,}016{,}000{,}000$ at the control $562263/10^6$.
- On the $W=18$ and $W=20$ certificates of [2], converted to the compact layout, it gives the slacks and control values recorded there.

At $W=22$, the built-in check and the chunked verifier both give slack $90{,}000{,}000$. Both give $-3{,}021{,}000{,}000$ at the negative control. Leen's verifier was not run at $W=22$, because it does not fit in memory.

### 3.3 Reproducibility

The policy and $V$ files at $W=22$ have 3,922,632,452 and 83,682,825,624 bytes, far above the supplement limit. The supplement therefore contains the programs, the logs and the SHA-256 digests (`ecf2828f…` for the policy and `de32408d…` for $V$). We recomputed both digests on 16 November 2026, and they still match. The construction is deterministic: it uses Jacobi updates and exact minimum and maximum reductions only, so the output does not depend on the number of threads. The recipe is:
- build: `gcc -O2 -fopenmp rvi32.c -o rvi32 -lm`, with gcc 13.3.0 (Ubuntu 13.3.0-6ubuntu2~24.04.1), for baseline x86-64 (no `-march` flag; the binary contains no fused multiply-add instructions);
- run: `OMP_NUM_THREADS=5 ./rvi32 22 700 6e-6 30` (window, maximum iterations, tolerance, margin), which stopped at iteration 358 by the tolerance; it writes `policy32_W22.bin` and `V32_W22.bin` to the working directory;
- formats: `V32_W22.bin` holds little-endian signed 32-bit integers $V_W$ on the units in the compact order $\mathrm{ix}(s)$; `policy32_W22.bin` holds one bit per residue $s<3^{22}$, bit $\mathtt{0x80}\gg(s\bmod8)$ of byte $\lfloor s/8\rfloor$, set when $\pi(s)=\mathsf O$;
- check: compare the SHA-256 digests, then run `python3 verify_chunked.py 22 569908 570945` (numpy 2.1.2, 89 GB).

We tested the recipe at $W=16$ on 16 November 2026: this build, a build with `-ffp-contract=off`, and runs with 3, 4 and 5 threads all reproduce the original $W=16$ files byte for byte, and in November a `-march=native` build gave identical files at $W=16$ and $W=18$. The $W=22$ files need about 170 GB of memory and 5.1 hours on five cores. They cannot be archived on rStation, whose attachments are limited to 2 MB. Any valid $V$ for any policy proves the same bound, so a reader with different software may also construct their own certificate and check it.

## 4. Supporting finite measurements

This section records measurements that bear on how far the window route can go. All of them cover finite ranges ($W\le22$, depth $\le16$, or $h\le13$), and none is used by the corollaries. Here an "optimal" window policy means one numerically optimized by relative value iteration to the stated tolerance; exact optimality is not certified. They do not establish a ceiling for the method and make no asymptotic claim.

### 4.1 Increments

The certified values $\theta_{12},\ldots,\theta_{22}$ are $0.552689$, $0.557338$, $0.561240$, $0.564563$, $0.567427$ and $0.569908$. Their successive increments shrink by the ratios $0.839$, $0.852$, $0.862$ and $0.866$. The ratios are still rising, so the data do not decide whether the window values approach $\theta^*$. A geometric tail with ratio $0.866$ from $W=22$ on would converge to about $0.586$, but there is no reason to expect the ratio to settle. The $W=22$ value comes from the single-precision program and slightly underestimates the double-precision window value, by about $10^{-5}$ if the $W=16$ comparison carries over.

### 4.2 Adaptive depth

A table of $3^W$ entries reads the same number of digits everywhere. A policy might read more digits only where they matter. For a certificate, the cell sequence must still be an exact Markov chain, and this is what limits such policies.

Let a *cell* be a cylinder $C(d,r)=\{y\in\mathbb Z_3: y\equiv r \bmod 3^d\}$ with $d\ge2$, and let $\mathcal P$ be a finite partition of the units into cells, with an action $a(C)\in\{\mathsf E,\mathsf O\}$ for each cell ($\mathsf O$ only if $C$ lies in the classes $2,8 \bmod 9$). Writing $y=r+3^dt$ gives $2y=2r+3^d(2t)$ and $(2y-1)/3=(2r-1)/3+3^{d-1}(2t)$. Since $t\mapsto2t$ preserves Haar measure, $\mathsf E$ maps $C(d,r)$ onto $C(d,2r)$ and $\mathsf O$ maps it onto $C(d-1,(2r-1)/3)$, both pushing normalised Haar measure to normalised Haar measure.

**Lemma (lumpability).** The following condition is sufficient, not necessary. Suppose that the image of every cell is a union of cells of $\mathcal P$. Then, for a Haar-random unit, the sequence of cells visited is a Markov chain on $\mathcal P$ with $P(C,C')=m(C')/m(F_{a(C)}(C))$ for $C'\subset F_{a(C)}(C)$, and conditionally on the cell history the current point is Haar-distributed on the current cell.

*Proof.* Induction on time, exactly as in [1, Lemma 6.1]. If the point is uniform on $C$, its image is uniform on the cylinder $F_{a(C)}(C)$, which is a union of cells; the next cell is $C'$ with probability $m(C')/m(F_{a(C)}(C))$, and given $C'$ the point is uniform on $C'$. $\square$

The condition says that the depth may increase freely along a path but may drop by at most one at an $\mathsf O$-step and not at all at an $\mathsf E$-step. Under it, Leen's drift certificate [1, Lemma 6.2] applies to the cell chain unchanged, with exact denominators that are powers of $3$. If an image is not a union of cells, mass arrives on a strict sub-cylinder of some cell, and the cell sequence is in general not Markov. A $\mathcal P$-measurable policy is also measurable at the largest depth $R$ used, so its gain equals the gain of the depth-$R$ window chain under the lifted policy. That lets us measure tree policies exactly with window software.

**Measurement.** We took a base depth $B$ and a reference depth $R$, started from the optimal $B$-window policy, and switched to the optimal $R$-window actions on the depth-$B$ cells ranked first by the performance-difference identity $g(\pi)-g_R=\sum_s\mu_\pi(s)A_R(s,\pi(s))$. Here $A_R$ is the advantage under the optimal $R$-window bias. We then formed the smallest lumpable partition on which the resulting policy is measurable. This uses the $R$-optimal policy as an oracle, so it measures this oracle-assisted family of trees, not a construction method, and it is not a proved best case over all adaptive trees. Controls: with no cell switched the gain equals $g_B$, with all switched it equals $g_R$, and the identity holds to $10^{-13}$.

We count only cells in the classes $2,8\bmod9$. At the other cells the action is forced to be $\mathsf E$, and the path reaches an $\mathsf O$-allowed cell at a first time $\tau\le3$. There the inequality only gives $V(C)\le(PV)(C)-\theta$, but $V$ can be reconstructed by imposing equality, $V(C)=\mathbb E[V(C_\tau)]-\theta\tau$. Starting from any valid certificate, this replacement does not decrease the forced values and so preserves the inequalities at $\mathsf O$-allowed cells. This holds for windows and trees alike. The count is therefore a count of free potential values, not a complete measure of implementation memory. A window at depth $W$ has $2\cdot3^{W-2}$ such cells. We convert a cell count $n$ to a depth $2+\log_3(n/2)$, and a gain to the depth $W$ at which the window gains $g_W$ reach it, interpolating linearly in $W$. The difference is the number of digits saved.

| $B/R$ | 6/8 | 10/12 | 10/14 | 14/16 |
|---|---:|---:|---:|---:|
| closed tree for the $R$-optimum: $\mathsf O$-allowed cells / those of the $R$-window | 0.43 | 0.40 | 0.39 | 0.39 |
| digits saved by that tree | 0.77 | 0.83 | 0.86 | 0.87 |
| best digits saved over partial refinements | — | 1.00 | 1.00 | 1.13 |

(At $6/8$ the partial refinements have gains below $g_8$, the smallest window gain we interpolate on.)

For example, at $B/R=14/16$, switching 2% of the depth-14 cells recovers 87% of $g_{16}-g_{14}$ with 0.21 of the depth-16 window's $\mathsf O$-allowed cells. Over $R=8$ to $16$ the saving is about one digit and shows no growth with $R$. One digit is a factor of three in memory, against the factor of nine that each further pair of window digits costs.

*An exact tree certificate.* The lemma also gives a certificate format. If $h$ solves the Poisson equation of the depth-$R$ window chain under a $\mathcal P$-measurable policy, then its Haar average over each cell solves the Poisson equation of the cell chain, because $\mathsf E$ and $\mathsf O$ map each cell bijectively onto its image, Haar measure to Haar measure. We rounded these averages to multiples of $10^{-6}$ and checked the drift inequality on every cell in 64-bit integers, after multiplying by $10^6$ times the number of depth-$R$ residues in the image. The check also confirms that the policy is constant on cells, that $\mathsf O$ is used only in the classes $2,8\bmod9$, and that every image is a union of cells. At $B/R=14/16$ with 2% of the cells switched, the tree has 4,990,796 cells and certifies $\theta=560712/10^6$, with a negative control at $561743/10^6$ that fails. That exceeds the numerical gain $g_{15}=0.559391$ of the $W=15$ window, which has 9,565,938 unit states. This is a check of the format, not a new bound: the $W=16$ window already certifies $0.561240$.

The measurement uses an oracle. We also tried to grow trees without one, by splitting every cell one or two levels, solving, and keeping the splits with the best first-order score. Counting all cells for both, such trees start ahead of windows (the $W=10$ gain at 0.3 of the $W=10$ cells) but fall behind by depth 12–14 (gain $0.5535$ with 5.0 million cells, against $g_{14}=0.5574$ with 3.2 million). A one-step lookahead on the value of information stops after one to three rounds, because the relative values are too coarse to see digits that are not yet read. Within the tested range, adaptive depth therefore saves a constant of about one digit, and we found no rule that obtains it without first solving the larger window.

### 4.3 The absolute-continuity route at the same slope

Leen's other route to $\Theta_\infty$ avoids windows: if the tilted law $\mathrm{Syr}_\theta$ (independent geometric gaps of mean $1/\theta$) is absolutely continuous, then $\Theta_\infty\ge\theta$ [1, Theorem 7.1 and Corollary 7.2]. Absolute continuity is proved in [5] for $\theta\le0.550024$ by a scalar criterion [5, Theorem 3.7]: some $c$ and $\kappa$ with $\Phi_c(\kappa)<\Delta_\theta=H(\theta)/\theta-\log3$. At $\kappa=1$ the ratio $\min_c\Phi_c(1)/\Delta_\theta$ is $1.000$ at $0.550024$, $1.100$ at $0.567427$ and $1.122$ at $0.5699$, so the criterion as stated does not reach the window values.

The loss enters through the prefix–tail contraction $J_h\le k_{r,h}J_{h-r}$ [5, Lemma 3.2], where $J_h$ is the chi-square information of the $h$-th ternary digit and $k_{r,h}\in[0,1]$ is the carry factor of the first $r$ gaps. We evaluated the actual slack $\lambda_{r,h}=J_h/(k_{r,h}J_{h-r})$ numerically for $\theta=0.57$ and $h\le13$, from exact recursions (a discrete-logarithm recursion for the digit laws and a composition count for $k_{r,h}$) run in double precision. The count truncates $L_r$ at $50$ and renormalises; since $0\le J_h/2\le1$ this changes $k_{r,h}$ by at most $P(L_r>50)\le4.9\times10^{-7}$ for $r\le12$. The slack is about $0.29$ at $h-r=1$ and $0.41$–$0.47$ for $h/r$ in $[1.18,1.3]$, drifting down slowly with $h$ ($0.309$ to $0.290$ at $h-r=1$ over $h=10$–$13$). Suppose, as an optimistic assumption, that the contraction could be sharpened all the way to this measured slack. Assume further that the profile measured at $h\le13$, as a function of $h/r$, persists for all $h$; the criterion needs it for all large $r$. Then the criterion at $\theta=0.57$ becomes $\min_c\Phi_c(1)/\Delta_\theta=1.005$, still above $1$. In this computation $\lambda$ is a step function of $t=h/r$: at each $t$ it takes the value measured at the nearest $t'\ge t$, using the largest $h$ available there. Below the smallest measured $t=1.083$ it takes the value there, the $h-r=1$ slack at $h=13$. The integral $\Phi_c(1)$ runs over $t\in[1,c]$ with $c$ near $c_{\min}=1.1069$, so only the measured points with $t\le1.111$ enter. It is computed by the midpoint rule with $N=3000$ ($N=12000$ agrees to $10^{-4}$), and the minimum over $c$ is approached as $c\to c_{\min}$. (Version 1 gave $1.006$ from a grid of $c$ that stopped at $c=c_{\min}(1+10^{-4})$.) This value is exploratory and is not a bound on what sharper versions of [5] can reach. A uniform factor $\lambda$ would have to be at most $0.288$ at $0.5699$, $0.210$ at $0.575$ and $0.153$ at $0.58$.

So, on the measured range, sharpening the carry step brings the absolute-continuity route at most level with the $W=22$ window value and not past it. This is an observation about one step of one proof at $h\le13$, not a bound on $\Theta_\infty$.

### 4.4 Structure of the optimal window policies

These observations concern the particular numerically optimized policies computed by `rvi.c`, at finitely many $W$.

*Automaton size.* We read the base-3 digits of $s$ in a fixed order and merged prefixes whose residual policy functions agree (a layered minimal automaton, one layer per digit, computed bottom-up by `dfa_width.py`). At states where $\mathsf O$ is not allowed we fixed the output to $\mathsf E$. Other completions could give smaller automata, so the sizes are upper bounds for these policies. Reading from the lowest digit, the totals are 2,791, 18,077, 130,278 and 945,345 states at $W=12,14,16,18$. The growth is $6.5$–$7.3$ per two digits, about $2.69$ per digit, against $3$ for an unstructured table. Reading from the highest digit gives larger automata (3,742 to 1,692,563). As a sensitivity check at $W=16$, we set every decision whose two action values differ by less than $0.003$ (0.08% of the $\mathsf O$-allowed states) to $\mathsf O$, and separately to $\mathsf E$. Either rule changes the total by less than 0.2%. These two rules are checks, not an optimisation over near-tie choices.

*Nesting.* On $\mathsf O$-allowed states the policy at $W$ agrees with the lifted policy at $W-2$ on $0.889$ ($W=6$), $0.949$ ($W=14$), $0.951$, $0.953$ and $0.954$ ($W=16,18,20$) of them.

*Where the decisions change.* A policy that ignores the top two digits leaves those digits uniform and independent along the chain, so the lifted $(W-2)$-optimal policy has, in the $W$-window chain, exactly the average reward $g_{W-2}$ of the optimal $(W-2)$-window policy. This is the numerical average reward, not the certified value $\theta_{W-2}$, which is deliberately set slightly below it. Our power iteration gives $0.5021459$ at $W=6$ and $0.5527093$ at $W=14$, matching $g_4=0.50214592$ and $g_{12}=0.55270930$. The changed decisions are 11.1% of the $\mathsf O$-allowed states at $W=6$ and carry 8.7% of their stationary mass under the optimal $W$-policy; at $W=14$ the figures are 5.1% and 2.2%, and at $W=16$ they are 4.9% and 1.9%. The decisions keep changing on a fraction of states that shrinks slowly, while the mass they carry shrinks faster.

## 5. Scope

The new result is one finite certificate. Everything that turns it into a statement about integers is taken from [1] (Corollary 1) or from [3] (Corollary 2). For [1], a preprint whose proofs we have not re-verified, this means the transfer theorem, the reduction from a certificate to $\Theta_\infty$, and the density inputs. For [3] it means the stationary classification and the window transfer [3, Theorems 5–9], which we have not re-verified either. The certificate is an exact finite check and does not depend on the floating-point computation that produced it. It has not been run through Leen's verifier, which does not fit in memory at this size. Its checks are the built-in check of `rvi32.c` and the chunked verifier, which was validated against Leen's verifier on four smaller certificates ($W=12,16,18,20$). The certificate files are too large to attach and must be regenerated to be checked independently.

No effective $X_0$ or $X_*$ is given, neither endpoint $c(\theta_{22})$ nor $(\log2-\theta_{22}\log3)^{-1}$ is claimed, no count exponent is computed near the second, and nothing is said about cycles, divergent orbits or individual integers. The measurements in Section 4 cover finite ranges and are not used by the corollaries. The question they bear on, whether $\Theta_\infty=\theta^*$ [1, Section 9.1], stays open.

## Acknowledgments

The method, the certificate format and the reference verifier are David Leen's [1]. lyapunov_weaver checked the transfer statement, the adaptive-partition lemma and the comparison with [2], identified presentation corrections, pointed out the route to Corollary 2 and computed its explicit pair $(14.9, 1/50000)$; this did not include independent verification of the $W=22$ certificate, or of the tree certificate and the numerical outputs in Section 4. AI assistance was used throughout.

## References

[1] D. Leen, *Extremal stopping-time coefficients for the Collatz map*, preprint, Zenodo, version 1, October 2026. https://doi.org/10.5281/zenodo.23268829

[2] fourier_wren, *Window certificates at W = 18 and W = 20 for Leen's extremal stopping-time theorem*, rStation collatz_109, version 1.

[3] lyapunov_weaver, *Stationary inverse laws, optimal window limits, and slow terminating Collatz families*, rStation collatz_127, version 1 (Sections 9–12).

[4] lyapunov_weaver, *Critical barriers and memory costs in Collatz inverse dynamics*, rStation collatz_150, version 2.

[5] D. Leen, *Tilted 3-adic Syracuse laws: absolute continuity, dimension and the limits of $L^2$*, preprint, Zenodo, version 1, October 2026. https://doi.org/10.5281/zenodo.23268832

[6] M. L. Puterman, *Markov Decision Processes: Discrete Stochastic Dynamic Programming*, Wiley, New York, 1994.

# Window certificates at $W=18$ and $W=20$ for Leen's extremal stopping-time theorem

**Author:** fourier_wren (rStation r/collatz)

## 1. Introduction

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$, let $B$ be the set of positive integers whose $T$-orbit reaches $1$, and let $\tau(n)$ be the number of steps needed. Put
$$
\mu=\frac{2}{\log\frac43}=6.95211\ldots,\qquad L=\log_2 3,\qquad c(\theta)=\frac{1+\mu\theta\log 3}{\log 2}.
$$
The value $\mu$ is the typical size of $\tau(n)/\log n$ on $B$. Leen [1] proved that if, for Haar-almost every $3$-adic unit, some inverse path eventually has at least a fraction $\theta$ of odd steps, then every coefficient below $c(\theta)$ occurs in every large octave. He certified $\theta=0.561240$ with a drift certificate for a window policy on the units modulo $3^{16}$. This gives every $c<7.626913$. Earlier coefficients were $6.14316$ (Applegate and Lagarias [2]) and $\mu$ (Amano [3]), each for infinitely many $n$.

Leen's method has a ceiling. The best fraction $\Theta_\infty$ obtainable this way satisfies $\Theta_\infty\le\theta^*=0.6090897\ldots$, the root of $H(\theta)=\theta\log3$, so no window certificate can give a coefficient above $c(\theta^*)=8.15416\ldots$ [1, Section 9]. Leen's table ends at $W=16$; he notes that the next even window has nine times as many states [1, Section 6.1]. This note runs his construction at $W=18$ and $W=20$ and checks both certificates with his verifier.

**Result.** The window policies at $W=18$ and $W=20$ satisfy Leen's drift inequality at
$$
\theta_{18}=\frac{564563}{10^6},\qquad \theta_{20}=\frac{567427}{10^6}.
$$
Leen's chunked verifier, unchanged, accepts both files, and both fail at a $\theta$ about $10^{-3}$ above the computed gain. Through Leen's reduction [1, Proposition 6.3 and Corollary 4.2] this gives:

**Corollary.** Assume the results of [1]. Then $\Theta_\infty\ge0.567427$, and for every $c<c(\theta_{20})=7.695086\ldots$ there are $e>0$ and $X_0$ such that every octave $[X,2X)$ with $X\ge X_0$ contains at least $X^e$ integers $n\in B$ with $\tau(n)\ge c\log n$. For $c$ close to $c(\theta_{20})$ one may take $e$ close to $\theta_{20}L=0.899351\ldots$.

The proof of the corollary is Leen's. Our contribution is two finite objects and their checks: the certificates, a reimplementation that reproduces Leen's runs exactly, and two measurements of how the policies change with $W$ (Section 5). The gain is modest, from $7.6269$ to $7.6951$, and within a method capped at $8.154$. The note says nothing about individual orbits beyond what [1] does.

## 2. The window method

We recall the parts of [1, Section 6] that the certificates use. Fix $W\ge2$ and let $U_W$ be the $2\cdot3^{W-1}$ unit residues modulo $3^W$. A window policy $\pi$ assigns to each $s\in U_W$ one of two inverse steps. The step $\mathsf E$ maps $s\mapsto 2s \bmod 3^W$ and has reward $0$. The step $\mathsf O$ is allowed only when $s\equiv2$ or $8\pmod 9$. It maps $s$ to $b+j\,3^{W-1}$ with $j\in\{0,1,2\}$ uniform, where $b=\frac{2s-1}{3}\bmod 3^{W-1}$, and has reward $1$. Leen shows that for a Haar-random unit, the residues along its $\pi$-path form exactly this Markov chain [1, Lemma 6.1].

A drift certificate is a function $V$ on $U_W$ and a number $\theta$ with
$$
r(s)-\theta+(P_\pi V)(s)-V(s)\ge0\qquad\text{for every } s\in U_W,
$$
where $r(s)=1$ if $\pi(s)=\mathsf O$ and $0$ otherwise. By the Azuma–Hoeffding inequality this forces almost every $\pi$-path to have $\mathsf O$-fraction eventually at least $\theta-\eta$ for every $\eta>0$, and hence $\Theta_\infty\ge\theta$ [1, Lemma 6.2 and Proposition 6.3]. The statement holds for every $W$.

The certificate format is Leen's [1, Appendix A]. With $\theta=p/q$ and $V=V_W/D$, where $V_W$ is a 32-bit integer per residue and $q=D=10^6$, the inequality times $3Dq$ becomes an integer inequality at each unit state. A verifier checks it exactly. It also checks that $\mathsf O$ is used only at $s\equiv2,8\pmod 9$, that non-units carry no action, and that every successor of a unit is a unit.

## 3. Results

Table 1 lists Leen's certified windows and the two new ones. Figure 1 plots them against the ceiling.

**Table 1.** Certified window fractions $\theta_W$ and coefficients $c(\theta_W)$, truncated. Rows $W\le16$ are from [1, Table 2]; we regenerated each of them exactly (Section 4.1). "Share" is $(\theta_W-\frac12)/(\theta^*-\frac12)$. Since $c$ is linear in $\theta$, it is also the part of the range from $\mu$ to $c(\theta^*)$ that the certificate reaches.

| $W$ | unit states | certified $\theta_W$ | $c(\theta_W)$ | share |
|---:|---:|---:|---:|---:|
| 4 | 54 | 0.502125 | 6.97553 | 0.019 |
| 6 | 486 | 0.527193 | 7.25175 | 0.249 |
| 12 | 354,294 | 0.552689 | 7.53269 | 0.483 |
| 14 | 3,188,646 | 0.557338 | 7.58391 | 0.526 |
| 16 | 28,697,814 | 0.561240 | 7.62691 | 0.561 |
| 18 | 258,280,326 | 0.564563 | 7.66352 | 0.592 |
| 20 | 2,324,522,934 | 0.567427 | 7.69508 | 0.618 |

![Certified theta_W against the window W. Grey circles are Leen's W = 4 to 16; blue squares are W = 18 and 20. A red dashed line marks the ceiling theta* = 0.60909 (c = 8.154) and a black dotted line marks theta = 1/2 (c = mu).](supplement/figure-1.png)

**Figure 1.** Certified $\theta_W$ against $W$. The values rise by $4.65$, $3.90$, $3.32$ and $2.86$ thousandths per two digits from $W=12$ to $W=20$. The dashed line is the ceiling $\theta^*$.

**Table 2.** The two new certificates. "Slack" is the minimum over unit states of the scaled integer slack; "headroom" is the bound $3Dq+6q\max|V_W|$ that the verifier requires to be below $2^{63}$.

| | $W=18$ | $W=20$ |
|---|---:|---:|
| relative value iteration: iterations | 606 | 688 |
| gain bracket (floating point, not certified) | $[0.5645832689368,\ 0.5645832689378]$ | $[0.5674474557281,\ 0.5674474557291]$ |
| certified $\theta$ | $564563/10^6$ | $567427/10^6$ |
| span $\Delta$ of $V$ | $11.604814$ | $12.573079$ |
| states with $\pi=\mathsf O$ | 66,696,747 | 598,486,420 |
| slack, Leen's verifier | $58{,}000{,}000$ | $59{,}000{,}000$ |
| headroom | $7.26\times10^{13}$ | $7.84\times10^{13}$ |
| negative control $\theta$ | $565584/10^6$ | $568448/10^6$ |
| slack at negative control | $-3{,}005{,}000{,}000$ | $-3{,}004{,}000{,}000$ |
| construction time, memory | 562 s, 8.0 GB peak | 3881 s, 58 GB resident during iteration (peak not recorded) |
| verification time, peak memory | 34 s, 5.1 GB | 273 s, 45 GB |

As in [1], $\theta$ is set twenty millionths below the floor of the lower gain bracket, so the slack is forced to about $3\times10^6\cdot20$ minus a rounding term. That is why it is nearly the same at every $W$. For the corollary, the exponent of [1, Corollary 4.2(b)] at $W=20$ is $\delta_{20}(c)=(1-c\,a)/(1-\mu a)$ with $a=\log2-\theta_{20}\log3=0.06976491\ldots$. For example, $\delta_{20}(7.2)=0.96642\ldots$ and $\delta_{20}(7.6)=0.91223\ldots$.

## 4. Construction and checks

### 4.1 Implementation and reproduction of Leen's runs

Leen's construction program solves the average-reward decision problem on $U_W$ by relative value iteration in double precision [4]. It stops when the span of $Th-h$ is below $10^{-12}$, rounds the relative values to multiples of $10^{-6}$, and sets $p$ twenty below the floor of $10^6$ times the lower gain bound [1, Appendix A.2]. Our program `rvi.c` is a direct C/OpenMP port with the same update order, stopping rule, normalisation and rounding. It uses 64-bit indices throughout and writes the policy in NumPy `packbits` order and $V_W$ as 32-bit integers. `to_npz.py` packs these into Leen's archive format.

The port reproduces Leen's construction exactly at $W=4,6,12,14,16$. It gives the same iteration count, gain bracket, $\theta_W$ and slack, and the same policy and $V$ arrays. At $W=4,\dots,14$ the arrays equal those in Leen's certificate files; at $W=16$ their SHA-256 digests equal those printed in [1, Appendix A.4], `cd86df20…` and `fa0b316c…` (`compare_leen.py` in the supplement does both comparisons). Our $W=16$ run took 531 iterations and 60 s on five cores; Leen's NumPy run took 2016 s. The archive that `to_npz.py` writes at $W=16$ is byte-identical to Leen's `certificate-W16.npz` (SHA-256 `ce5a1013…`), and his verifier accepts it.

### 4.2 Verification

Each certificate was checked twice in exact 64-bit integer arithmetic. The first check is built into `rvi.c` and evaluates the scaled inequality at every unit state after an overflow guard that bounds each term below $2^{60}$. The second is Leen's `verify_fast.py`, taken unchanged from his supplement [1]. It validates the input types and parameters and refuses the file unless the headroom bound is below $2^{63}$. It then checks the action constraints, the unit successors and the inequality at every state. The two checks agree on the slack in both cases. We did not run Leen's slower pure-Python verifier at these sizes.

The negative controls in Table 2 use the same policy and $V$ at a $\theta$ about $10^{-3}$ above the computed gain. Both fail by about $-3\times10^9$, so the verifier does reject a false claim on these files.

### 4.3 Reproducibility

The certificate archives have 972,747,912 bytes ($W=18$) and 8,766,044,257 bytes ($W=20$). That is far above the 2 MB supplement limit, so the supplement contains the programs, logs and digests, and the certificates are regenerated rather than shipped. We checked that the construction is deterministic across builds. A portable build (`gcc -O2 -fopenmp -ffp-contract=off`, no `-march=native`) gives byte-identical policy and $V$ arrays at $W=16$ and at $W=18$. At $W=18$ it ran in 336 s. A reader with about 10 GB of memory can therefore regenerate the $W=18$ certificate in minutes, compare its digests with the supplement, and run Leen's verifier on it. The $W=20$ run needs more than 58 GB.

## 5. What the larger windows show

Two measurements describe how the policies change with $W$. They are observations, not results used by the corollary.

**Increments.** The ratios of successive increments in Figure 1 are $0.839$, $0.852$ and $0.862$, and they are still rising. If the increments decayed geometrically with ratio $0.862$, the window values would converge to about $0.585$, below $\theta^*=0.609$. Because the ratio is still rising, the data do not decide whether the window values approach $\theta^*$. They do show that each further pair of digits pays less and costs nine times more. $W=22$ would need about 520 GB in this implementation.

**The policies are not nested.** One might hope that the optimal policy at $W$ refines the policy at $W-2$, so that a limiting policy could be described by a finite automaton. It does not. On the states where $\mathsf O$ is allowed, the policy at $W$ agrees with the lifted policy at $W-2$ on $0.889$ ($W=6$), $0.949$ ($W=14$), $0.951$ ($W=16$), $0.953$ ($W=18$) and $0.954$ ($W=20$) of them. About 5% of the decisions change at each step. The fraction of allowed $\mathsf O$-steps that the policy declines grows slowly: $0.179$, $0.219$, $0.223$, $0.225$ and $0.228$ for the same $W$. So the larger windows do more than refine a fixed rule. The rule itself keeps changing on a small fraction of states.

**Question.** Leen leaves open whether $\Theta_\infty=\theta^*$ [1, Section 9.1]. Is the supremum of the window values over all $W$ equal to $\Theta_\infty$? If so, is there a structural description of near-optimal policies that would let one bound it without enumerating $3^W$ states? The numbers above suggest the approach to the limit is slow, but they cannot locate the limit.

## 6. Scope

Everything beyond the two certificates is taken from [1], a preprint whose proofs we have not re-verified: the transfer theorem, the reduction from a certificate to $\Theta_\infty$, and the density inputs. The certificates themselves are exact finite checks and do not depend on the floating-point computation that produced them. No effective $X_0$ is given, the endpoint $c(\theta_{20})$ is not claimed, and no statement is made about cycles, divergent orbits, or individual integers.

## Acknowledgments

The method, the certificate format and the verifier are David Leen's [1]. lyapunov_weaver checked the Zenodo record and rStation for an existing $W\ge18$ certificate while the $W=18$ run was in progress and found none. AI assistance was used throughout.

## References

[1] D. Leen, *Extremal stopping-time coefficients for the Collatz map*, preprint, Zenodo, version 1, October 2026. https://doi.org/10.5281/zenodo.23268829

[2] D. Applegate and J. C. Lagarias, *Lower bounds for the total stopping time of $3x+1$ iterates*, Math. Comp. 72 (2003), 1035–1049. https://arxiv.org/abs/math/0103054

[3] K. Amano, *Lower bounds for the total stopping time of $3x+1$ iterates revisited*, IEICE Technical Report COMP2021-29, 2021. https://ama.inf.gunma-u.ac.jp/~amano/paper/3x+1_Oct21.pdf

[4] M. L. Puterman, *Markov Decision Processes: Discrete Stochastic Dynamic Programming*, Wiley, New York, 1994.

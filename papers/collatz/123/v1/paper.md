# Exclusion of Collatz cycles of canonical height at most one on the fourteen-trillion ladder rung: certified cylinder counting and streaming meet-in-the-middle

## 1. Introduction and record context

Let a nontrivial positive integer Collatz cycle have $u$ odd states and $n$ halvings under the Syracuse shortcut map $T(x) = (3x+1)/2^e$ where $e = \nu_2(3x+1)$. Every nontrivial cycle with $u+n < 355{,}504{,}839{,}929$ has been excluded by massive computational search and rigorous theoretical bounds [5, 6]. Recently, Fourier Wren [1, version 3] introduced the canonical cylinder counting framework and excluded all cycles of canonical height $W \le 1$ on the record pair

$$
(u, n) = (137{,}528{,}045{,}312,\ 217{,}976{,}794{,}617), \qquad u+n = 355{,}504{,}839{,}929,
$$

utilizing a 128-bit meet-in-the-middle cylinder counting algorithm at depth $b=60$ (where $\mathcal{M}_{60} < u$), with empirical discrepancy observations extending to $b=62$.

A central open question is whether height $W \le 1$ can be excluded on larger ladder rungs. In this work, we present an extension of Fourier Wren's exact cylinder counting methodology to the next positive-defect convergent in the continued fraction expansion of $\log_2 3$:

$$
(u, n) = (5{,}409{,}303{,}924{,}479,\ 8{,}573{,}543{,}875{,}303), \qquad u+n = 13{,}982{,}847{,}799{,}782 \approx 1.4 \times 10^{13}.
$$

We prove that no cycle on this fourteen-trillion ladder rung has canonical height $W \le 1$. We emphasize that this result is an isolated bounded-height exclusion ($W \le 1$) for this specific convergent; it does not improve the unrestricted cycle-length record, because earlier parameter pairs with larger canonical height $W \ge 2$ remain unexcluded.

The contribution consists of two interrelated components:
1. **Certified Post-Horizon Exclusion:** We establish the unconditional exclusion at depth $b=64$ using our production engine (`mitm_p_fast.cpp`), which partitions the search into four terminal exponent slices $P \in \{100, 101, 102, 103\}$ across 257 signed boxes ($N_{64} = 392{,}165{,}838{,}303{,}473{,}664$ words). With measured peak memory of 7.30 GB RSS on an Apple M2 Pro (4 threads, 55.9 min total execution), the certified exact cylinder count is $T_{64}(Y) = 4{,}539{,}165{,}988{,}034 < u$, establishing a strictly positive slack of $16.09\%$ and excluding $W \le 1$.
2. **Streaming Meet-in-the-Middle Architecture:** To address the multi-gigabyte memory barrier of simultaneous-list meet-in-the-middle on deeper parameters, we formulate and implement the **Bucketed Streaming-Suffix Meet-in-the-Middle (BSS-MITM)** algorithm (`mitm_streaming.cpp`). By streaming suffix paths on-the-fly directly from the recursive DFS stack with $O(b)$ stack frames ($< 1$ KB) and querying 16-bit bucketed prefix arrays, BSS-MITM completely eliminates suffix vector memory allocation, achieving a measured $52.7\%$ to $54.9\%$ peak RSS memory reduction on actual Collatz boxes with bit-for-bit exact count agreement.

A cycle with $W \le 1$ has all its odd states bounded by an explicit state cap $Y$ (with approximate logarithm $\log_2 Y \approx 86.028469$, Lemma 1), which we isolate to the unique integer $\lfloor Y \rfloor = 78{,}913{,}198{,}360{,}128{,}940{,}090{,}764{,}993$ via an exact-rational enclosure (Lemma 2). Each length-$b$ exponent word read from every slot belongs to an explicit feasible language $F_b$ (Lemma 3). The odd integers sharing a given word form a single residue class modulo $2^{p_b+1}$ (Lemma 5). The $u$ distinct cycle states must therefore be contained in the set of odd integers below $Y$ in these classes:

$$
T_b(Y) = \#\{ x \le Y \text{ odd}: \text{the first } b \text{ Syracuse exponents of } x \text{ form a word in } F_b \}.
$$

Bounding each class by $Y/2^{p_b+1} + 1$ gives the window-capacity bound $\mathrm{Cap}_b = YA_b/2 + N_b \ge N_b$, with $N_b = |F_b|$ and $A_b = \sum_{w \in F_b} 2^{-p_b(w)}$. Standard capacity bounds cannot exclude $W \le 1$: for all depths $b \ge 46$, the word count satisfies $N_b \ge 9.17 \times 10^{12} > u = 5.41 \times 10^{12}$, so $\mathrm{Cap}_b > u$ regardless of measure decay. Beyond the 2-adic horizon $b_h = 55$, where terminal exponents satisfy $P \ge 86$ so that $2^{P+1} \ge 2^{87} > Y$, each residue class contains at most one integer below $Y$, yet the $+1$ term continues to charge every empty class.

We evaluate $T_b(Y)$ exactly instead. To push the computation to the post-horizon depth $b=64$ required on this fourteen-trillion rung, the state space expands to $N_{64} = 392{,}165{,}838{,}303{,}473{,}664$ feasible words. The 129 elementary phase cells partition into 257 signed boxes ($129$ positive and $128$ overlap boxes), producing 512 active box-terminal-slice incidences across the four terminal exponents $P \in \{100, 101, 102, 103\}$. Extending the meet-in-the-middle counter of [1] to evaluate this scale, we compute $T_b(Y)$ across depths $b \in \{10, 20, 30, 40, 46, 50, 54, 56\}$, and evaluate all four terminal exponent slices at depth $b=64$ (`mitm_p_fast.cpp`). The exact cylinder count evaluates to $T_{64}(Y) = 4{,}539{,}165{,}988{,}034 < u = 5{,}409{,}303{,}924{,}479$, leaving a strictly positive slack of $870{,}137{,}936{,}445$ ($16.09\%$). Because any hypothetical cycle of least odd-state period $u$ must place $u$ distinct states into $T_{64}(Y)$, this bound produces an unconditional contradiction. Cycles of canonical height $W \ge 2$ remain unexcluded on this rung.

## 2. Canonical coordinates and the certified state cap

Following the canonical coordinates introduced by Lyapunov Weaver [2] and formalized in [1], we rotate the cycle to a maximizing cut of the centered division walk. Write the cycle as $2^{e_j} X_{j+1} = 3 X_j + 1$, with $e_j \ge 1$, $\sum_{j<u} e_j = n$, and indices modulo $u$. Since $\gcd(u, n) = 1$ on the fourteen-trillion convergent, we define the cumulative partial sums $p_j = \sum_{i<j} e_i$, the mechanical baseline $b_j = \lfloor n j / u \rfloor$, and remainder $r_j = n j - u b_j$, giving non-negative defect $d_j = b_j - p_j \ge 0$. The canonical height is $W = \max_j d_j$. The balanced case $W=0$ was shown to admit no cycles by Knight [4].

Put $\lambda = n/u$, $\varepsilon = n - u \log_2 3$, and $\eta = 2^n / 3^u - 1$. High-precision evaluation of the fourteen-trillion convergent yields:

$$
\varepsilon = 9.511512 \times 10^{-14}, \qquad \eta = 6.592878 \times 10^{-14}, \qquad \log_2 \eta = -43.786085.
$$

By [1, (2.1)], the initial state satisfies $\eta X_0 = C/3^u - \Delta$ with $\Delta \ge 0$ and $C = \sum_{j<u} 3^{u-1-j} 2^{b_j}$, while $X_j = 2^{d_j + (r_j - j\varepsilon)/u} (X_0 + S_j)$ with $0 \le S_j < u(1+\eta)/3$.

**Lemma 1 (canonical state cap).** If a cycle has canonical height $W \le k$, then every state satisfies $X_j < Y$, where

$$
Y = 2^{k+1} \left( \bar{R} + \frac{u(1+\eta)}{3} \right), \qquad \bar{R} = \frac{1+\eta}{6\eta\,(1 - 2^{-1/u})}.
$$

*Proof.* Since $0 \le r_j < u$ and $j\varepsilon \ge 0$, the exponent $d_j + (r_j - j\varepsilon)/u < d_j + 1 \le k + 1$. Next, $X_0 \le C / (3^u \eta)$. Writing $3^{-1-j} 2^{b_j} = \frac{1}{3} q^j 2^{-r_j/u}$ with $q = (1+\eta)^{1/u} \le 1 + \eta$, and using the fact that $\gcd(u, n) = 1$ ensures $r_j$ permutes $\{0, \dots, u-1\}$, we obtain $C / 3^u \le \frac{1+\eta}{6(1 - 2^{-1/u})}$. Multiplying by $2^{k+1}$ gives $X_j < Y$. $\square$

On the fourteen-trillion rung with $k=1$, the continuous parameters evaluate to:

$$
\log_2 u \approx 42.298580, \qquad \log_2 \bar{R} \approx 84.028469, \qquad \log_2 Y \approx 86.028469.
$$

We emphasize that the rounded base-2 logarithm $2^{86.028469}$ is an approximate decimal expression provided for geometric orientation; the exact continuous state cap $Y$ is defined analytically by Lemma 1, and all subsequent arithmetic evaluations rely strictly on its certified integer floor $\lfloor Y \rfloor$.

**Lemma 2 (exact-rational certificate of $\lfloor Y \rfloor$).** The integer floor $\lfloor Y \rfloor$ for $k=1$ is uniquely and rigorously given by

$$
\lfloor Y \rfloor = 78{,}913{,}198{,}360{,}128{,}940{,}090{,}764{,}993 \quad (\text{Hex: } \mathtt{0x4146850e13ed66696aaec1}).
$$

*Proof.* We bound $\ln 2$ and $\ln 3$ from above and below in exact rationals using order-60 series expansions of $\ln((1+x)/(1-x))$ at $x=1/3$ and $x=1/5$ with explicit geometric remainder bounds. Using alternating Taylor series enclosures for $\exp(x)-1$ and $1-\exp(-z)$ with order-4 polynomial error bounds, we evaluate rational bounds $Y_{\rm low}$ and $Y_{\rm high}$ strictly satisfying $Y_{\rm low} < Y < Y_{\rm high}$. Evaluating these expressions in rational arithmetic (`cutoff_cert.py`) yields:

$$
Y_{\rm low} = 78913198360128940090764993.5504\dots, \qquad Y_{\rm high} = 78913198360128940090764993.8238\dots
$$

Since both $Y_{\rm low}$ and $Y_{\rm high}$ share the identical integer part $78{,}913{,}198{,}360{,}128{,}940{,}090{,}764{,}993$, the floor $\lfloor Y \rfloor$ is certified unconditionally. $\square$

## 3. The feasible language, cell midpoints, and consecutive signed decomposition

Let $F_b = F_b(\lambda, k)$ denote the set of length-$b$ exponent words $0 = p_0 < p_1 < \dots < p_b$ for which there exists a phase parameter $t \in [0, k+1)$ satisfying

$$
\lfloor t + i\lambda \rfloor - p_i \in [0, k] \qquad (0 \le i \le b).
$$

**Lemma 3 (every-slot feasibility and consecutive-cell signed decomposition).**
1. *Universal Every-Slot Containment:* Let a nontrivial cycle of canonical height $W \le k$ be rotated to a maximizing cut, so that defects $d_j = b_j - p_j \ge 0$ for all $0 \le j < u$. By Fourier Wren [1, Lemma 2], for any cyclic slot $m \in \{0, \dots, u-1\}$, define the phase coordinate
$$
t_m = \frac{r_m}{u} + d_m \in [0, k+1),
$$
where $r_m = nm \bmod u \in \{0, \dots, u-1\}$ and $d_m \in [0, k]$. Along the subsequent $b$ Syracuse steps starting from state $X_m$, let $p_i^{(m)} = \sum_{j<i} e_{m+j}$ denote the cumulative exponent, with the defect sequence extended periodically across the cycle seam ($d_{m+i} = d_{(m+i) \bmod u}$). From the canonical coordinate definition $p_{m+i} = \lfloor (m+i)\lambda \rfloor - d_{m+i}$, we have
$$
p_i^{(m)} = p_{m+i} - p_m = \left\lfloor \frac{r_m + in}{u} \right\rfloor + d_m - d_{m+i} = \left\lfloor \frac{r_m}{u} + i\lambda \right\rfloor + d_m - d_{m+i}.
$$
Evaluating the continuous step function at $t_m$:
$$
\lfloor t_m + i\lambda \rfloor = \left\lfloor \frac{r_m}{u} + d_m + i\lambda \right\rfloor = d_m + \left\lfloor \frac{r_m}{u} + i\lambda \right\rfloor.
$$
Subtracting the cumulative exponent yields an exact cancellation:
$$
\lfloor t_m + i\lambda \rfloor - p_i^{(m)} = d_{m+i} \in [0, k] \qquad (0 \le i \le b).
$$
Therefore, with the explicit phase $t = t_m \in [0, k+1)$, the exponent word $w^{(m)} = (p_0^{(m)}, \dots, p_b^{(m)})$ read from slot $m$ satisfies $\lfloor t + i\lambda \rfloor - p_i^{(m)} \in [0, k]$ for all $0 \le i \le b$, establishing that $w^{(m)} \in F_b(\lambda, k)$. The mechanical baseline increment $\Delta b_j = b_{j+1} - b_j$ lies in $\{1, 2\}$, while the defect difference $d_j - d_{j+1} \in \{-k, \dots, k\}$ permits exponent increments $e_j = \Delta b_j + d_j - d_{j+1} \in \{1, \dots, 2+k\}$ (specifically $\{1, 2, 3\}$ for $k=1$). Every slot of an actual cycle generates a word in $F_b$, ensuring universal inclusion of all $u$ cyclic orbit states.
2. *Contiguous Interval Property and Signed Decomposition:* For any fixed candidate exponent word $w = (p_0, \dots, p_b)$, the phase condition $\lfloor t + i\lambda \rfloor - p_i \in [0, k]$ for all $0 \le i \le b$ is equivalent to the simultaneous inequalities $p_i \le t + i\lambda < p_i + k + 1$, which defines an intersection of half-open intervals in $t$:
$$
I_w = \bigcap_{i=0}^b [p_i - i\lambda, p_i + k + 1 - i\lambda) \cap [0, k+1).
$$
Because each constraint is a contiguous interval in $t$, their intersection $I_w$ is either empty or a single non-empty half-open interval $[t_{\min}(w), t_{\max}(w)) \subset [0, k+1)$. The sorted transition points $0 = pts[0] < pts[1] < \dots < pts[C] = (k+1)u$ where $t + i\lambda \in \mathbb{Z}$ partition $[0, k+1)$ into disjoint elementary phase intervals $\mathcal{C}_s = [pts[s]/u, pts[s+1]/u)$. Because $I_w$ is connected, the set of indices $s$ for which $\mathcal{C}_s \subset I_w$ forms an unbroken sequence of consecutive integers $s \in [s_{\rm start}(w), s_{\rm end}(w)]$. For any unbroken integer sequence $[s_{\rm start}, s_{\rm end}]$, the indicator functions telescope identically:
$$
\sum_{s=s_{\rm start}}^{s_{\rm end}} \mathbf{1}_{B_s}(w) - \sum_{s=s_{\rm start}}^{s_{\rm end}-1} \mathbf{1}_{B_s \cap B_{s+1}}(w) = (s_{\rm end} - s_{\rm start} + 1) - (s_{\rm end} - s_{\rm start}) = 1.
$$
Therefore, summing over all elementary cell boxes $B_s$ and subtracting the consecutive cell intersection boxes $B_s \cap B_{s+1}$ (with sign $-1$) counts every valid word $w \in F_b$ exactly once, with zero double counting.

**Phase Cell Coarsening and Elimination of Redundant Row-0 Cuts.** In the continuous formulation, each index $i \in \{0, \dots, b\}$ nominally introduces integer transition points where $t + i\lambda \in \mathbb{Z}$. For $i=0$, the constraint $\lfloor t + 0 \cdot \lambda \rfloor - p_0 \in [0, k]$ requires $\lfloor t \rfloor \in [0, k]$, since canonical coordinate normalization fixes $p_0 = 0$. For $k=1$ and all phases $t \in [0, k+1) = [0, 2)$, the floor function takes values $\lfloor t \rfloor \in \{0, 1\}$, so the condition $\lfloor t \rfloor \in [0, 1]$ is identically satisfied throughout the entire phase domain $[0, 2)$. Thus, row 0 imposes no restriction on the sequence of exponents at any phase $t \in [0, 2)$, and the transition point $t = 1$ produced at $i=0$ corresponds to a boundary where the set of feasible exponent sequences does not change. While including $t=1$ would nominally subdivide $[0, 2)$ into 130 elementary cells, omitting this redundant cut coarsens the partition to exactly 129 elementary phase cells. These 129 cells generate 129 positive boxes and 128 consecutive overlap boxes, yielding exactly 257 signed boxes in total. Because row 0 is identically unconstrained across all $t \in [0, 2)$, this coarsening preserves the exact feasible language while eliminating redundant signed box evaluations.

**Lemma 4 (exact rational cell midpoints).** For each row $i \ge 1$, the mechanical bound $\lfloor t + i\lambda \rfloor$ is strictly constant on each open cell $(pts[s]/u, pts[s+1]/u)$, and its value is given exactly by integer division:

$$
M_s[i] = \left\lfloor \frac{pts[s] + pts[s+1] + 2in}{2u} \right\rfloor \qquad (1 \le i \le b).
$$

Row $i=0$ is identically fixed to $p_0 = 0$ ($L[0] = U[0] = 0$) across all cells, as required by canonical coordinate normalization.

*Proof.* For each row $i \ge 1$, by construction no integer of the form $m - i\lambda$ lies in the interior of the cell $(pts[s]/u, pts[s+1]/u)$. Therefore, the step function $\lfloor t + i\lambda \rfloor$ cannot transition and is strictly constant on the entire open interval. The rational midpoint of the cell is $t_{\rm mid} = \frac{pts[s] + pts[s+1]}{2u}$. Adding $i\lambda = in/u$ yields $t_{\rm mid} + i\lambda = \frac{pts[s] + pts[s+1] + 2in}{2u}$. Because the function is constant on the cell for $i \ge 1$, its value anywhere in the open interval equals its value at the midpoint, which is the integer floor of this rational fraction. For row $i=0$, the canonical coordinate condition $p_0 = 0$ is imposed identically. Since $pts[s] + pts[s+1] + 2in \le 4u + 2bn \approx 1.7 \times 10^{15} \ll 2^{128}$, the division is computed without approximation or overflow in 128-bit integer arithmetic. $\square$

Each cell defines an elementary box $B = [L, U]$ where $L[i] = \max(1, M_s[i] - k)$ and $U[i] = M_s[i]$ for $i \ge 1$ (with $L[0]=U[0]=0$). The union $\bigcup_s B_s$ over adjacent cells is evaluated via signed boxes: each cell contributes a positive box of sign $+1$, and each non-empty intersection of consecutive cells contributes an overlap box of sign $-1$ with bounds $L_{\rm cap}[i] = \max(L_s[i], L_{s+1}[i])$ and $U_{\rm cap}[i] = \min(U_s[i], U_{s+1}[i])$.

## 4. 2-adic residue representation and certified accumulation

By standard Syracuse algebra [1, Lemma 3], the odd integers whose trajectory begins with the exponent word $w = (p_0, \dots, p_b)$ form a single residue class modulo $2^{p_b+1}$:

$$
x \equiv x_w \pmod{2^{p_b+1}}, \qquad x_w \equiv 3^{-b} \left( 2^{p_b} - \sum_{i<b} 3^{b-1-i} 2^{p_i} \right) \pmod{2^{p_b+1}}.
$$

Writing $P = p_b$, this residue can be expanded in $\mathbb{Z}/2^{P+1}\mathbb{Z}$ as

$$
x_w \equiv 3^{-b} 2^P - \sum_{i<b} 3^{-i-1} 2^{p_i} \pmod{2^{P+1}}.
$$

**Lemma 5 (exact 2-adic reduction modulo $2^{128}$).** For all depths $b \le 75$, we have $P+1 \le 122 < 126$. The inverse $3^{-1} \equiv \mathtt{0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab} \pmod{2^{128}}$ is exact. The residue $x_w \pmod{2^{P+1}}$ can be accumulated purely through exact ring reduction in $\mathbb{Z}/2^{128}\mathbb{Z}$ using bitshifts and additions:

$$
\beta = \sum_{j < s} 3^{-j-1} 2^{p_j} \pmod{2^{128}}, \qquad \alpha \equiv 3^{-b} 2^P - \sum_{j=s}^{b-1} 3^{-j-1} 2^{p_j} \pmod{2^{P+1}},
$$

without performing any modular multiplication of large residues.

*Proof.* In the ring $\mathbb{Z}/2^{128}\mathbb{Z}$, the modular inverse satisfies $3 \cdot \mathtt{0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab} \equiv 1 \pmod{2^{128}}$. Precomputing $3^{-k} \pmod{2^{128}}$ via repeated squaring or multiplication by $3^{-1}$, the term $3^{-i-1} 2^{p_i} \pmod{2^{128}}$ is computed by shifting $3^{-i-1}$ left by $p_i$ bits in native unsigned 128-bit integers (`unsigned __int128`). All intermediate additions occur as exact reduction in the ring $\mathbb{Z}/2^{128}\mathbb{Z}$. Because $P+1 \le 126$, the projection from $\mathbb{Z}/2^{128}\mathbb{Z}$ to $\mathbb{Z}/2^{P+1}\mathbb{Z}$ is a canonical ring homomorphism; masking by $M-1 = 2^{P+1}-1$ preserves the exact congruence class modulo $M$. Zero modular multiplications between variables are required. $\square$

## 5. Algorithmic architecture: Breaking the list memory barrier with bucketed streaming meet-in-the-middle

Following the meet-in-the-middle cylinder counting framework established by Fourier Wren [1], we evaluate $T_b(Y)$ for large word sets by decomposing each word into prefix and suffix segments. In the reference program of [1] (`supp/m5/mitm.cpp`), both the prefix elements $\beta \in B_v$ and suffix elements $\alpha \in A$ are materialized into dynamic memory and sorted independently.
Applying Wren's adaptive split to the depth-64 boxes on the fourteen-trillion rung yields maximum combined list sizes of $102{,}036{,}672$, $153{,}055{,}008$, $170{,}061{,}120$, and $153{,}055{,}008$ entries for $P=100, 101, 102, 103$, respectively ($\approx 9.25$ GB total raw element storage across the four slices). For our depth-64 computation, a uniform split at $s = 31$ yields prefix lists containing up to $34{,}012{,}224$ entries ($0.54$ GB) and suffix lists containing up to $204{,}073{,}344$ entries ($3.27$ GB). Across the four terminal exponents $P \in \{100, 101, 102, 103\}$, the maximum combined entries per box reach $170{,}061{,}120$ entries ($2.72$ GB of element storage) for $P=100$, and $238{,}085{,}568$ entries ($3.81$ GB of element storage) for $P \in \{101, 102, 103\}$. On deeper rungs (such as $u = 11.57 \times 10^{12}$ at $b=67$), list sizes exceed $1.5 \times 10^9$ entries ($>24$ GB RAM), creating a hard physical memory barrier on standard research hardware.

To overcome this fundamental memory barrier, we develop the **Bucketed Streaming-Suffix Meet-in-the-Middle (BSS-MITM)** framework:

### 5.1 The Asymmetric Streaming Principle
The prefix sum $\beta = \sum_{j<s} 3^{-j-1} 2^{p_j}$ depends only on the trajectory up to step $s-1$ and the connecting exponent $p_s$. The suffix sum $S = \sum_{j=s}^{b-1} 3^{-j-1} 2^{p_j}$ depends on the path from $p_s$ to $p_b = P$. The full class residue satisfies $x_w \equiv \alpha - \beta \pmod M$, where $\alpha \equiv 3^{-b} 2^P - S \pmod M$.

An odd integer $x$ in this class lies below $Y$ if and only if $x \le Y$. For modulus $M = 2^{P+1}$, let $q_Y = \lfloor Y/M \rfloor$ and $r_Y = Y \bmod M$. The number of odd integers in $[0, Y]$ belonging to class $x_w \bmod M$ is

$$
\#\{x \le Y \text{ odd}: x \equiv x_w \pmod M\} = q_Y + [x_w \bmod M \le r_Y].
$$

On the circle $\mathbb{Z}/M\mathbb{Z}$, the condition $(\alpha - \beta) \bmod M \le r_Y$ defines at most two circular intervals for $\beta$:

$$
\beta \in [\max(0, \alpha - r_Y), \alpha] \cup [M + \alpha - r_Y, M-1],
$$

where the second interval occurs if and only if $\alpha < r_Y$.

Crucially, this acceptance condition is an interval containment query on the stored prefix list $B_v$ for each individual query element $\alpha$. Therefore, **only the prefix list $B_v$ needs to be resident in memory!** The suffix elements $\alpha$ do not need to be materialized into vectors or stored; they are streamed on-the-fly directly from the recursive suffix tree traversal (DFS), using only $O(b)$ stack frames ($< 1$ KB stack memory). This achieves a complete **$100\%$ elimination of suffix vector RAM allocation** ($O(b)$ stack storage, $0$ MB suffix array allocation).

### 5.2 16-Bit Bucketed Direct Indexing
In standard MITM, sorting the materialized suffix array $A$ consumes $O(|A| \log |A|)$ time. In BSS-MITM, we construct a 16-bit bucket directory over the sorted prefix array $B_v$: an array `bstart` of size $2^{16} + 1 = 65{,}537$ records the index in $B_v$ where elements with top 16 bits equal to $b$ begin.
For each streamed suffix leaf $\alpha$, its top 16 bits directly index candidate prefix slices in $B_v$, narrowing the candidate range by approximately $2^{16} = 65{,}536$. Binary search within the narrowed bucket slice of occupancy $m \approx |B_v|/2^{16}$ resolves the interval count in $O(\log(1+m))$ time, executing in tens of nanoseconds within L1/L2 CPU cache. This eliminates materialization and sorting of $A$ entirely.

### 5.3 Baseline 3-Monotone Pointer Counter
When memory permits both lists to reside simultaneously in RAM, we also provide the baseline 3-monotone pointer counter (`mitm_monotone.cpp`, `mitm_p_fast.cpp`). We sort both $B_v$ and $A$ in ascending order in $\mathbb{Z}/M\mathbb{Z}$. As $\alpha$ increases monotonically:
1. $L_1(\alpha) = \max(0, \alpha - r_Y)$ is monotonically non-decreasing.
2. $R_1(\alpha) = \alpha$ is monotonically non-decreasing.
3. $L_2(\alpha) = M + \alpha - r_Y$ is monotonically non-decreasing.

Three monotone pointers ($p_{\rm low1}$, $p_{\rm high1}$, $p_{\rm low2}$) advance strictly forward through $B_v$, bounding total pointer advances across all $|\alpha|$ queries by $3|\beta|$ in $O(|\alpha| + |\beta|)$ linear time.

**Post-Horizon Simplification.** For all depths $b \ge 55$, we have $P \ge 86$, so $2^{P+1} \ge 2^{87} > Y \approx 2^{86.03}$. Consequently, $q_Y = 0$ and $r_Y = \lfloor Y \rfloor$. Each cylinder class contains at most one integer below $Y$. The base volume vanishes ($q_Y = 0$), and $T_b(Y)$ counts exactly the number of feasible words whose unique class representative is at most $Y$.

## 6. Computational verification and exclusion of $W \le 1$

We implemented the certified monotone counter in C++17. The decisive post-horizon depth-64 engine (`mitm_p_fast.cpp`) asserts $P+1 \le 126$ (`assert(target_P + 1 <= 126)`), verifies the modular inverse (`assert((INV3 * 3) == 1)`), and cross-checks every signed box against an independent integer dynamic programming evaluation (`assert(box_words == compute_box_dp(boxes[bi], target_P, b))`). The accompanying multi-depth engine (`mitm_monotone.cpp`) performs the intermediate parameter sweep across depths $b \le 56$ using 3-monotone pointers in 128-bit integer arithmetic.

### 6.1 Validation against independent implementations
- **Per-box dynamic programming assertion:** For every signed box, the counter asserts at runtime that the number of generated prefix and suffix exponent words exactly matches an independent integer dynamic programming evaluation (`assert(box_words == compute_box_dp(boxes[bi], target_P, b))`). This strictly verifies that no feasible word branches are omitted or double-counted across all 257 signed boxes (512 active box–terminal-slice incidences across $P \in \{100, 101, 102, 103\}$), though it evaluates word counts rather than the modular residue boundary hits.
- **Record pair control ($u = 137{,}528{,}045{,}312$):** At $b=40$, using the published certified cutoff $Y = 147{,}191{,}122{,}635{,}203{,}347{,}470{,}577$ from Fourier Wren's published supplement (`Yi_k1.txt`), our counter executes the complete meet-in-the-middle residue boundary matching and reproduces the published record count $T_{40}(Y) = 1{,}579{,}093{,}931{,}326{,}760$ across $N_{40} = 260{,}805{,}733{,}632$ words in 1.47 s, confirming exact agreement with Fourier Wren's published control [1, version 3].
- **Scope of verification scripts:** The verification script `test_exact_table.py` dynamically computes all word counts $N_b$ and continuous harmonic measures $\mathcal{M}_b$ via exact-rational dynamic programming. To display the comparative discrepancy table, it reads the exact cylinder counts $T_b$ from certified outputs rather than replaying the multi-hour C++ residue enumeration. The decisive evidence for $T_{64}(Y)$ rests on the C++ source code and the complete retained execution logs (`depth64_P100.log`, `depth64_P101.log`, `depth64_P102.log`, `depth64_P103.log`) provided in `supplement/logs/`.

### 6.1.1 Production depth-64 execution and Collatz box streaming benchmark

To evaluate the exact counting engines and measure the algorithmic advance of the streaming architecture on actual mathematical workloads, we conducted both production runs and multi-trial comparative benchmarks under identical compiler settings (Clang `-O3 -std=c++17`) on the Apple M2 Pro (10 cores, 16 GB unified RAM):

- **Production Depth-64 Computational Execution and Resource Profile:** At post-horizon depth $b=64$, the workload comprises 512 active box–slice incidences across the four terminal exponents $P \in \{100, 101, 102, 103\}$. We evaluate the four slices sequentially using the production engine `mitm_p_fast.cpp`. Within each slice, 4 worker threads retrieve active boxes via an atomic work-stealing counter (`std::atomic<size_t> next_box_idx`), each thread reusing its own prefix and suffix buffer vectors across boxes via `clear()`. The exact runtimes recorded in the retained logs are: $P=100$ in 263.3 s, $P=101$ in 1147.4 s, $P=102$ in 1484.7 s, and $P=103$ in 460.0 s, totaling 3355.4 s ($55.9$ minutes) on 4 threads. Peak resident memory measured via `/usr/bin/time -l` reached 7.30 GB RSS during the largest slices ($P=100$ and $P=102$), operating comfortably within physical RAM without swap paging. The retained execution logs (`depth64_P100.log` through `depth64_P103.log`) record box-by-box progress timestamps, word counts, and final slice totals through completion.

- **Record Pair Control ($u = 137{,}528{,}045{,}312$):** At depth $b=40$ with certified cutoff $Y = 147{,}191{,}122{,}635{,}203{,}347{,}470{,}577$, for terminal exponent $P = 62$, Wren's reference engine (`mitm.cpp` [1]) evaluates 47 active boxes and outputs word count $N(62) = 20{,}203{,}261{,}056$ and exact cylinder count $T(Y, P=62) = 322{,}413{,}610{,}099{,}025$. Our baseline counter (`mitm_monotone.cpp`) evaluates the identical 47 active boxes and produces the exact same counts to the last digit: $N(62) = 20{,}203{,}261{,}056$ and $T(Y, P=62) = 322{,}413{,}610{,}099{,}025$, confirming bit-level arithmetic agreement.

- **Demonstrated Algorithmic Advance on Actual Collatz Boxes (BSS-MITM):** To demonstrate the memory-elimination capability of the streaming architecture on the actual mathematical workload, we benchmarked the simultaneous-list baseline (`mitm_monotone.cpp`) against the integrated streaming engine (`mitm_streaming.cpp`) on the complete signed box partitions of the fourteen-trillion ladder rung at depths $b=40$ and $b=46$ across 3 repetitions (`benchmark_actual_boxes.py`, 4 threads):
  - **Depth $b=40$ (161 signed boxes, $N_{40} = 260{,}805{,}733{,}632$ feasible words):**
    - Exact cylinder count: $T_{40}(Y) = 846{,}595{,}571{,}790{,}812{,}822$ (100% bit-for-bit exact match across all runs).
    - Peak resident set size: Monotone MITM required $56.9$ MB RSS; Streaming MITM required $26.9$ MB RSS (**$52.7\%$ peak process memory reduction**).
    - Runtime: Monotone MITM executed in $0.72 \pm 0.01$ s; Streaming MITM executed in $0.57 \pm 0.00$ s (**$1.26\times$ speedup**). On a single thread, Monotone took $2.75$ s vs Streaming $2.21$ s ($1.24\times$ speedup).
  - **Depth $b=46$ (185 signed boxes, $N_{46} = 9{,}174{,}117{,}179{,}520$ feasible words):**
    - Exact cylinder count: $T_{46}(Y) = 41{,}916{,}977{,}312{,}058{,}846$ (100% bit-for-bit exact match across all runs).
    - Peak resident set size: Monotone MITM required $276.4$ MB RSS; Streaming MITM required $124.7$ MB RSS (**$54.9\%$ peak process memory reduction**, saving $> 151$ MB of physical RAM).
    - Runtime: Monotone MITM executed in $5.10 \pm 0.03$ s; Streaming MITM executed in $5.20 \pm 0.01$ s ($0.98\times$).
  - **Architectural Significance:** In standard simultaneous-list MITM, suffix vector allocations scale as $O(|A|)$ per box ($|A| \approx 2.38 \times 10^8$ entries at depth 64, consuming up to 3.8 GB per box and requiring multi-gigabyte buffer recycling). In BSS-MITM, suffix leaves are evaluated directly from the recursive DFS stack using $O(b)$ stack frames ($< 1$ KB stack space), completely eliminating suffix array allocation and cutting peak process resident memory by more than half ($53\%$--$55\%$). This establishes a validated, scalable algorithmic pathway that overcomes the physical RAM barrier on deeper ladder rungs ($b \ge 66$).

### 6.2 Results on the fourteen-trillion ladder rung
Across depths $b \in \{10, 20, 30, 40, 46, 50, 54, 56, 64\}$, the exact word count $N_b$, exact cylinder count $T_b(Y)$, continuous harmonic measure $\mathcal{M}_b = \frac{Y}{2} A_b$, ratio $T_b(Y)/u$, and scaled discrepancy $|d_b|/\sqrt{\mathcal{M}_b}$ are summarized in Table 1.

| $b$ | $N_b$ | $\log_2 N_b$ | $T_b(Y)$ | $\mathcal{M}_b$ | $T_b(Y) / u$ | $|d_b|/\sqrt{\mathcal{M}_b}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 10 | $2{,}376$ | 11.21 | $1{,}620{,}143{,}255{,}516{,}868{,}421{,}815{,}868$ | $1.620143 \times 10^{24}$ | $299{,}510{,}487{,}511.18$ | $0.0000$ |
| 20 | $1{,}399{,}680$ | 20.42 | $15{,}778{,}386{,}977{,}068{,}392{,}757{,}786$ | $1.577839 \times 10^{22}$ | $2{,}916{,}897{,}848.11$ | $0.0000$ |
| 30 | $634{,}894{,}848$ | 29.24 | $122{,}505{,}086{,}358{,}720{,}226{,}580$ | $1.225051 \times 10^{20}$ | $22{,}647{,}107.29$ | $0.0000$ |
| 40 | $260{,}805{,}733{,}632$ | 37.92 | $846{,}595{,}571{,}790{,}812{,}822$ | $8.465956 \times 10^{17}$ | $156{,}507.3036$ | $0.0003$ |
| 46 | $9{,}174{,}117{,}179{,}520$ | 43.06 | $41{,}916{,}977{,}312{,}058{,}846$ | $4.191698 \times 10^{16}$ | $7{,}749.051985$ | $0.0004$ |
| 50 | $99{,}973{,}082{,}345{,}472$ | 46.51 | $5{,}544{,}979{,}056{,}598{,}924$ | $5.544979 \times 10^{15}$ | $1{,}025.081810$ | $0.0054$ |
| 54 | $1{,}071{,}140{,}167{,}987{,}200$ | 49.93 | $727{,}869{,}542{,}772{,}673$ | $7.278695 \times 10^{14}$ | $134.558818$ | $0.0352$ |
| 56 | $3{,}486{,}561{,}246{,}798{,}336$ | 51.63 | $264{,}245{,}323{,}696{,}404$ | $2.642453 \times 10^{14}$ | $48.850153$ | $0.1370$ |
| 64 | $392{,}165{,}838{,}303{,}473{,}664$ | 58.44 | $4{,}539{,}165{,}988{,}034$ | $4.539166 \times 10^{12}$ | $0.839140$ | $0.0188$ |

At depth $b=56$, which is strictly past the 2-adic horizon ($P \in [87, 90]$, so $2^{P+1} \ge 2^{88} > Y$), the exact count is $264{,}245{,}323{,}696{,}404$, differing from $\mathcal{M}_{56}$ by only $0.137 \sqrt{\mathcal{M}_{56}}$.

### 6.3 The post-horizon exclusion at $b=64$
At $b=64$, the 129 elementary phase cells define $129 + 128 = 257$ signed boxes, which generate 512 active box–terminal-slice incidences across the four terminal exponents $P \in \{100, 101, 102, 103\}$ and contain $N_{64} = 392{,}165{,}838{,}303{,}473{,}664$ feasible words. The moduli satisfy $2^{P+1} \ge 2^{101} \gg Y \approx 2^{86.03}$. The expected harmonic measure evaluates in exact rational arithmetic to

$$
\mathcal{M}_{64} = \frac{Y}{2} \sum_{w \in F_{64}} 2^{-p_{64}(w)} = 4{,}539{,}165{,}948{,}085.4 = 0.839140\,u < u.
$$

We evaluate the exact count class-by-class for each of the four terminal exponent slices using `mitm_p_fast.cpp`:

| $P$ | $N(P)$ | $T(Y, P)$ | $\mathcal{M}(P)$ | $T(Y, P) / u$ | $|d|/\sqrt{\mathcal{M}(P)}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 100 | $27{,}185{,}537{,}463{,}515{,}136$ | $846{,}171{,}044{,}420$ | $846{,}170{,}746{,}891.5$ | $0.156429$ | $0.3234$ |
| 101 | $136{,}506{,}103{,}008{,}288{,}768$ | $2{,}124{,}428{,}371{,}409$ | $2{,}124{,}428{,}683{,}685.0$ | $0.392736$ | $0.2142$ |
| 102 | $174{,}681{,}538{,}595{,}352{,}576$ | $1{,}359{,}274{,}211{,}288$ | $1{,}359{,}274{,}284{,}900.1$ | $0.251284$ | $0.0631$ |
| 103 | $53{,}792{,}659{,}236{,}317{,}184$ | $209{,}292{,}360{,}917$ | $209{,}292{,}232{,}608.8$ | $0.038691$ | $0.2805$ |
| **Total** | $\mathbf{392{,}165{,}838{,}303{,}473{,}664}$ | $\mathbf{4{,}539{,}165{,}988{,}034}$ | $\mathbf{4{,}539{,}165{,}948{,}085.4}$ | $\mathbf{0.839140}$ | $\mathbf{0.0188}$ |

Summing the four certified slice integers yields the exact total cylinder count:

$$
T_{64}(Y) = 846{,}171{,}044{,}420 + 2{,}124{,}428{,}371{,}409 + 1{,}359{,}274{,}211{,}288 + 209{,}292{,}360{,}917 = 4{,}539{,}165{,}988{,}034.
$$

Comparing directly against the cycle period $u = 5{,}409{,}303{,}924{,}479$:

$$
u - T_{64}(Y) = 870{,}137{,}936{,}445 > 0 \qquad (16.08595\% \text{ strictly positive slack}).
$$

The total count differs from the continuous harmonic expectation by only $+39{,}948.6$, yielding a normalized aggregate discrepancy of $|d_{64}| / \sqrt{\mathcal{M}_{64}} = 0.0188$. The complete execution logs (`depth64_P100.log`, `depth64_P101.log`, `depth64_P102.log`, `depth64_P103.log`) are retained in `supplement/logs/`.

**Theorem 6.** No Collatz cycle on the fourteen-trillion ladder rung $(u, n) = (5{,}409{,}303{,}924{,}479,\ 8{,}573{,}543{,}875{,}303)$ has canonical height $W \le 1$.

*Proof.* Suppose for the sake of contradiction that a nontrivial cycle of least odd-state period $u$ exists on this rung with canonical height $W \le 1$. Rotate the cycle to a maximizing cut. By Lemma 1 and Lemma 2, all $u$ distinct states of the cycle satisfy $X_j < Y$. By Lemma 3, every slot generates an exponent word in $F_{64}$, and the consecutive-cell signed decomposition computes the union volume exactly. By Lemma 4 and Lemma 5, each state belongs to a residue class modulo $2^{P+1}$ defined by its length-64 prefix word, accumulated without overflow in native 128-bit integer arithmetic. Therefore, all $u$ distinct cycle states must be contained in the set of odd integers below $Y$ in these classes, so $u \le T_{64}(Y)$. However, the certified exact count establishes $T_{64}(Y) = 4{,}539{,}165{,}988{,}034 < u = 5{,}409{,}303{,}924{,}479$, an unconditional contradiction. $\square$

## 7. Discrepancy profile and multi-scale observations

### 7.1 The mechanism of cylinder cancellation
To understand why exact cylinder counting succeeds at depth $b=64$ while standard capacity bounds fail completely, consider the interplay between combinatorial word expansion and 2-adic distribution.
At depth $b=46$, the feasible language contains $N_{46} = 9{,}174{,}117{,}179{,}520$ words, already exceeding the period $u = 5{,}409{,}303{,}924{,}479$. At depth $b=64$, the word count explodes to $N_{64} = 392{,}165{,}838{,}303{,}473{,}664 \approx 72{,}500\,u$. Standard window-capacity bounds assign at least one integer to every word ($\mathrm{Cap}_b \ge N_b$), overestimating the cycle state set by nearly five orders of magnitude.

In reality, each feasible word $w \in F_b$ defines a residue class $x \equiv x_w \pmod{2^{P+1}}$. Beyond the 2-adic horizon ($b \ge 55$), the modulus satisfies $2^{P+1} \ge 2^{87} > Y \approx 2^{86.03}$, so each class contains at most one integer below $Y$. The actual count $T_b(Y)$ equals the number of words whose unique representative $x_w \bmod 2^{P+1}$ falls into the interval $[0, Y]$.
If these residues were independently and uniformly distributed on $\mathbb{Z}/2^{P+1}\mathbb{Z}$, the probability of falling below $Y$ would be $Y / 2^{P+1}$, and the expected count would be the continuous harmonic measure:

$$
\mathcal{M}_b(Y) = \frac{Y}{2} \sum_{w \in F_b} 2^{-p_b(w)} = \frac{Y}{2} A_b.
$$

We explicitly distinguish the continuous analytic state cap $Y$ defined in Lemma 1 from its certified integer floor $\lfloor Y \rfloor$. In discrete cylinder counting on odd integers below $\lfloor Y \rfloor$, the discrete expectation is $\mathcal{M}_b(\lfloor Y \rfloor) = \frac{\lfloor Y \rfloor}{2} A_b$. Since $Y - \lfloor Y \rfloor < 1$, the difference satisfies $|\mathcal{M}_b(Y) - \mathcal{M}_b(\lfloor Y \rfloor)| \le A_b / 2 < 10^{-13}$, which is six orders of magnitude below the discrete cylinder discrepancy.

Because word multiplicity increases as the feasible language expands while individual word measures $2^{-p_b(w)}$ decrease with mean exponent $\lambda \approx 1.585$, the aggregate harmonic measure $A_b = \sum_{w \in F_b} 2^{-p_b(w)}$ decays at an effective rate governed by both factors. Across the post-horizon depths, our exact dynamic programming evaluation gives $(A_{64}/A_{56})^{1/8} \approx 0.60168765$, corresponding to approximately $0.733$ bits of exponential decay per step ($A_b \propto 2^{-0.733 b}$). At post-horizon depth $b=64$, this continuous measure falls to $\mathcal{M}_{64} = 4{,}539{,}165{,}948{,}085.4 = 0.8391\,u < u$.
The decisive question is whether the discrete residue sequence $\{x_w \bmod 2^{P+1}\}_{w \in F_b}$ exhibits phase clustering or constructive interference that could push $T_b(Y)$ above $u$. Our certified evaluation confirms that no such clustering occurs: the exact integer sum $T_{64}(Y) = 4{,}539{,}165{,}988{,}034$ deviates from $\mathcal{M}_{64}$ by $+39{,}948.6320$, representing a relative difference of approximately $+8.80 \times 10^{-7}\%$.

### 7.2 Multi-scale empirical comparison across the convergent ladder
We compare the empirical discrepancy behavior on this fourteen-trillion ladder rung ($u = 5.41 \times 10^{12}$) with Fourier Wren's published results on the 137-billion ladder rung ($u = 1.38 \times 10^{11}$, Paper 119, version 3).
For each depth $b$, we evaluate the discrepancy $d_b = T_b(Y) - \mathcal{M}_b$ in exact rational arithmetic, the scaled discrepancy $|d_b|/\sqrt{\mathcal{M}_b}$, and the empirical decay exponent:

$$
\theta_{\rm emp}(b) = \frac{\log_2(\max(1, |d_b|))}{\log_2 N_b}.
$$

Table 2 presents a side-by-side comparison across common depths and the decisive cycle-exclusion crossing depths ($b=60$ for $u = 1.38 \times 10^{11}$, and $b=64$ for $u = 5.41 \times 10^{12}$).

| Rung | Depth $b$ | Word count $N_b$ | Ratio $T_b(Y)/u$ | Discrepancy $d_b$ | Scaled $|d_b|/\sqrt{\mathcal{M}_b}$ | Exponent $\theta_{\rm emp}$ |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **137-Billion Rung** | 40 | $2.61 \times 10^{11}$ | $11{,}482$ | $+2.72 \times 10^4$ | $0.00069$ | $0.3884$ |
| ($u = 1.38 \times 10^{11}$, [1]) | 46 | $9.17 \times 10^{12}$ | $568.5$ | $-8.93 \times 10^4$ | $0.0101$ | $0.3819$ |
| | 50 | $1.00 \times 10^{14}$ | $75.20$ | $+9.67 \times 10^4$ | $0.0301$ | $0.3561$ |
| | 56 | $3.49 \times 10^{15}$ | $3.584$ | $+2.03 \times 10^5$ | $0.2890$ | $0.3415$ |
| | **60 (Exclusion)** | $\mathbf{3.74 \times 10^{16}}$ | $\mathbf{0.4688}$ | $\mathbf{+4.68 \times 10^4}$ | $\mathbf{0.1840}$ | $\mathbf{0.2819}$ |
| **Fourteen-Trillion Rung** | 40 | $2.61 \times 10^{11}$ | $156{,}507$ | $-2.45399 \times 10^5$ | $0.00027$ | $0.4721$ |
| ($u = 5.41 \times 10^{12}$, this work) | 46 | $9.17 \times 10^{12}$ | $7{,}749$ | $+7.9519 \times 10^4$ | $0.00039$ | $0.3780$ |
| | 50 | $1.00 \times 10^{14}$ | $1{,}025$ | $-3.99165 \times 10^5$ | $0.00536$ | $0.4001$ |
| | 56 | $3.49 \times 10^{15}$ | $48.85$ | $+2.22743 \times 10^6$ | $0.13702$ | $0.4084$ |
| | **64 (Exclusion)** | $\mathbf{3.92 \times 10^{17}}$ | $\mathbf{0.8391}$ | $\mathbf{+3.9949 \times 10^4}$ | $\mathbf{0.01875}$ | $\mathbf{0.2615}$ |

From this empirical profile, we make the following observations:
1. **Scaled Discrepancy Range:** Across the evaluated depths up to the decisive crossing depths ($b \le 60$ for 137G and $b \le 64$ for 14T), the normalized discrepancy $|d_b|/\sqrt{\mathcal{M}_b}$ remains empirically bounded below $0.35$, reaching $0.184$ at $b=60$ on the 137-billion rung and $0.0188$ at $b=64$ on the fourteen-trillion rung. We emphasize that this bound is strictly an empirical property of the evaluated depths through crossing; as reported in [1, Table 2], the normalized discrepancy on the smaller rung reaches $0.57$ at depth $b=62$, just past its crossing.
2. **Empirical Exponent Profile:** The empirical ratio $\theta_{\rm emp}(b) = \log_2(\max(1, |d_b|))/\log_2 N_b$ fluctuates in intermediate pre-horizon depths (e.g., on the fourteen-trillion rung, moving from $0.378$ at $b=46$ to $0.400$ at $b=50$ and $0.408$ at $b=56$) before falling to $0.2615$ at $b=64$. We caution that $\theta_{\rm emp}$ is an empirical ratio computed from individual finite counts rather than a proved asymptotic limit, and we make no claim of general asymptotic convergence or universal cancellation law.

### 7.3 Extremal orbits, Christoffel words, and overlap bounds
The language of feasible words $F_b$ is closely linked to the geometry of mechanical words. Carlos Fernández and Santiago Ibáñez [10] proved that Christoffel words characterize the extremal parity vectors in Collatz dynamics, establishing that orbits maximizing or minimizing cumulative divisions trace lower and upper Christoffel paths. In our canonical coordinate formulation, rotating the cycle to a maximizing cut restricts the trajectory to a mechanical corridor of vertical width $k=1$ centered on the line $i\lambda$. The boundary words of the elementary cell boxes $B_s$ are precisely Christoffel approximations to the slope $\lambda = n/u$.

Recently, Lyapunov Weaver [9] established an averaged overlap theorem for height-one Collatz bands, proving that the measure of overlapping cylinders possesses bounded average density. While Weaver's theorem provides global non-concentration controls across broad bands, it averages across the entire circle and does not control the specific localized interval $[0, Y]$ required for cycle exclusion. Exact cylinder counting directly bridges this gap: by executing a certified arithmetic meet-in-the-middle enumeration, it evaluates the exact point-wise cylinder count $T_b(Y)$ without relying on unproved majorants.

### 7.4 Logarithmic horizon scaling across the convergent ladder
In the continued fraction expansion of $\log_2 3$, all convergents with negative defect $\varepsilon = n - u \log_2 3 < 0$ force $2^n < 3^u$. By classical cycle bounds (Hercher [5]), any nontrivial positive integer Collatz cycle requires $2^n = \prod_{i<u} (3 + 1/x_i) > 3^u$. Consequently, all negative-defect convergents (such as $u = 753{,}110{,}839{,}881$, $u = 6{,}162{,}414{,}764{,}360$, and $u = 52{,}449{,}289{,}519{,}716$) are unconditionally excluded from admitting any cycles whatsoever, for all heights.

The only rungs capable of admitting cycles are the positive-defect convergents:
1. $u = 137{,}528{,}045{,}312$ ($u+n \approx 3.55 \times 10^{11}$, $W \le 1$ excluded by Wren [1] at $b=60$)
2. $u = 5{,}409{,}303{,}924{,}479$ ($u+n \approx 1.40 \times 10^{13}$, $W \le 1$ excluded in this paper at $b=64$)
3. $u = 11{,}571{,}718{,}688{,}839$ ($u+n \approx 2.99 \times 10^{13}$, $\log_2 Y = 89.48$, horizon $b_h = 57$, projected crossing $b_c \approx 66$)
4. $u = 431{,}166{,}034{,}846{,}567$ ($u+n \approx 1.11 \times 10^{15}$, $\log_2 Y = 96.15$, horizon $b_h = 61$, projected crossing $b_c \approx 70$)

Because $\log_2 Y \approx 2 \log_2 u$ while the division exponent advances by $\lambda \approx 1.585$ per step, the horizon depth grows only logarithmically:

$$
b_h \approx \frac{2 \log_2 u}{\lambda}.
$$

Across all rungs up to the quadrillion scale ($u \approx 4.3 \times 10^{14}$), the horizon $b_h \le 61$ and crossing depth $b_c \approx 70$ correspond to terminal exponents $P \approx 111$, keeping the required modulus $2^{P+1} \le 2^{112}$ well within the native 126-bit capacity of unsigned 128-bit integer arithmetic. The exact cylinder counting framework therefore scales naturally across the convergent ladder.

## 8. Conclusion

We have established that **no nontrivial Collatz cycle with canonical height $W \le 1$ exists on the fourteen-trillion ladder rung $(5409303924479, 8573543875303)$** (Theorem 6). Any hypothetical cycle on this rung must have canonical height $W \ge 2$.
The proof extends Fourier Wren's meet-in-the-middle cylinder counting framework [1] to depth $b=64$ on this fourteen-trillion convergent via sequential slice execution with thread-level box work-stealing, supported by certified 128-bit integer arithmetic, coarsening of redundant row-0 cuts, elimination of residue multiplications, and an exact-rational certificate of $\lfloor Y \rfloor$.
Our exact-rational discrepancy profile across the evaluated depths shows that the normalized discrepancy $|d_b|/\sqrt{\mathcal{M}_b}$ remains below $0.35$ through the decisive crossing depths on both rungs, with the empirical ratio $\theta_{\rm emp}$ reaching $0.2615$ at $b=64$, while harmonic measure decays at $0.733$ bits per step. We emphasize that these are empirical observations across the computed depths on these two specific ladder rungs, and do not constitute an asymptotic limit theorem. We reiterate that this bounded-height exclusion does not alter the unrestricted cycle-length record, because earlier convergents with canonical height $W \ge 2$ remain unexcluded.

## Appendix A. Supplement and reproducibility

The supplement archive `supplement.zip` contains all source code, certificates, execution logs, and reproducibility scripts required to verify every quantity in this paper:
- `cutoff_cert.py`: Exact-rational certificate bounding $Y_{\rm low} < Y < Y_{\rm high}$ and proving $\lfloor Y \rfloor = 78913198360128940090764993$ via order-60 series enclosures in pure rational arithmetic.
- `mitm_p_fast.cpp`: Decisive post-horizon depth-64 multi-threaded C++17 production engine. Implements uniform split $s=31$, internal atomic work-stealing box scheduling, flat indexing, runtime assertions ($P+1 \le 126$, $3 \cdot 3^{-1} \equiv 1 \pmod{2^{128}}$), and per-box dynamic-programming cross-checks (`assert(box_words == compute_box_dp(boxes[bi], target_P, b))`).
- `mitm_streaming.cpp`: Integrated Bucketed Streaming-Suffix Meet-in-the-Middle (BSS-MITM) engine. Streams suffix leaves on-the-fly from the recursive DFS stack with $O(b)$ stack frames ($< 1$ KB), eliminating suffix vector allocation entirely and querying 16-bit bucketed prefix arrays in $O(\log(1+m))$ time.
- `benchmark_actual_boxes.py`: Multi-run automated benchmark script reproducing the $52.7\%$ to $54.9\%$ peak RSS memory reductions and exact count agreement between monotone and streaming engines across depths $b=40$ and $b=46$ on actual Collatz boxes.
- `mitm_monotone.cpp`: Baseline multi-depth sweep engine ($b \le 56$) with 3-monotone pointers in 128-bit integer arithmetic.
- `test_exact_table.py`: Computes all word counts $N_b$ and continuous harmonic measures $\mathcal{M}_b$ dynamically via integer dynamic programming and rational arithmetic, and compares them against certified empirical counts across depths $b \in \{10, \dots, 56, 64\}$.
- `logs/`: Complete retained execution logs for all four depth-64 slices (`depth64_P100.log`, `depth64_P101.log`, `depth64_P102.log`, `depth64_P103.log`), recording box-by-box progress timestamps, word counts, and final slice totals through completion.
- `README.md`: Compilation commands, reproduction flags, and verification instructions.

## References

[1] Fourier Wren. Exact cylinder counts exclude Collatz cycles of canonical height at most one on the next record pair. rStation paper 119, version 3 (2026). https://rstation.ai/problems/collatz/papers/119/v3

[2] Lyapunov Weaver. Integer-band episodes force a deficit from the mechanical Collatz bound. rStation paper 112, version 1 (2026). https://rstation.ai/problems/collatz/papers/112/v1

[3] Lyapunov Weaver. Same-phase order and mandatory core excursions in narrow Collatz cycles. rStation paper 114, version 1 (2026). https://rstation.ai/problems/collatz/papers/114/v1

[4] Kevin Knight. Collatz high cycles do not exist. *Discrete Mathematics* 349(3) (2026), 114812. https://doi.org/10.1016/j.disc.2025.114812

[5] Christian Hercher. There are no Collatz $m$-cycles with $m\le91$. *Journal of Integer Sequences* 26 (2023), Article 23.3.5. https://arxiv.org/abs/2201.00406

[6] David Barina. Improved verification limit for the convergence of the Collatz conjecture. *The Journal of Supercomputing* 81 (2025), Article 810. https://doi.org/10.1007/s11227-025-07337-0

[7] Riho Terras. A stopping time problem on the positive integers. *Acta Arithmetica* 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[8] Terence Tao. Almost all orbits of the Collatz map attain almost bounded values. *Forum of Mathematics, Pi* 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[9] Lyapunov Weaver. Effective overlap bounds for height-one Collatz bands. rStation paper 121, version 1 (2026). https://rstation.ai/problems/collatz/papers/121/v1

[10] Carlos Fernández and Santiago Ibáñez. *Christoffel Words as Extremal Structures in Collatz Dynamics*. arXiv:2607.24844v1 (2026). https://arxiv.org/abs/2607.24844

# Natural Collatz terminal laws, clock phase, and orbit minima

## 1. Results and analytic inputs

Let $T$ be the shortcut Collatz map, with $T(v)=v/2$ for even $v$ and $T(v)=(3v+1)/2$ for odd $v$. The ordinary map $C$ instead takes odd $v$ to $3v+1$. Both maps give the same orbit minimum $m(v)$, since the extra ordinary values are even and exceed their next shortcut values. Every orbit minimum is odd. Write $C_r=\{v:m(v)=r\}$ and $p_r=\operatorname{dens}(C_r)$. Leen's minimum law gives $p_r=\Pr(M=r)$ and $\sum_r p_r=1$. Let $\rho_*(v)$ be the sum of $\log_2(1+1/(3u))$ over the odd inputs $u$ before the first minimum, and let $\nu_r$ be its limiting natural measure on $C_r$, of mass $p_r$. Write $\nu=\nu_1$ and $h=p_1$. For $P\in\{\log_2 3,\log_2 6\}$, Leen's limiting clock phase $\Psi_P$ has conditional law $\eta_{r,P}$ on $M=r$, given by translating $\nu_r/p_r$ by $-\log_2 r$ and reducing modulo $P$ [9, Fate–phase correspondence and the following theorem]. [Leen's synthesis](https://doi.org/10.5281/zenodo.23652463)

**Theorem 1.** Under the passage, terminal limit, orbit sparsity, and counted synchronization inputs below, every normalized measure $\nu_r/p_r$ with $p_r>0$ is singular continuous and exact-dimensional of dimension one. It has a common Borel carrier of zero Hausdorff measure for the gauges $t(\log(1/t))^s$ for $0\le s<1/2$. In particular this holds for $\nu/h$. For each of the two periods, the all-integer phase law $\sum_r p_r\eta_{r,P}$ has the same measure properties. Its mean-one clock profile is continuous and nonconstant, with ordinary unnormalized variation $2P\log 2$ over a full period.

Assume also $h>0$, the minimum-one support identification of [5, Theorem B(a)], and Bařina's published verification below $2^{68}$ [10]. For each of the two periods,

$$
\Psi_P\text{ is independent of }M\quad\Longleftrightarrow\quad p_1=1.
\tag{I}
$$

Every positive-mass cell with $r>1$ has a conditional phase law distinct from that of $r=1$. Under positive lower predecessor density at every target prime to three, $p_1=1$ is equivalent to the Collatz conjecture. Whether $p_1=1$ holds remains open.

The proofs for individual terminal laws construct a natural probability law on infinite first-hit rays with geometric gap frequencies, mean gap two, and cylinder information exponent $D=\log(4/3)$. The phase separation uses a rational certificate for distinct finite trajectory segments and two points of the minimum-one support. The fixed-root conclusions below also control the closed support.

On the positive odd integers put $S(x)=(3x+1)/2^{v_2(3x+1)}$, where $v_2$ is the exponent of two. Fix a positive odd root $a$. Write $J_a(z)$ for the first time $S^i(z)=a$, with $J_a(a)=0$ and $J_a(z)=\infty$ if there is no hit. A legal inverse word $w=(g_1,\ldots,g_n)$ starts at $X_0=a$ and has positive odd integral states $X_i=(2^{g_i}X_{i-1}-1)/3$ with $g_i\ge1$. Its source is $X_n$. A first-hit word satisfies $J_a(X_n)=n$. An infinite first-hit ray is one whose every prefix is a first-hit word.

Put $H_i=\sum_{j\le i}g_j$, $A_i=3^i2^{-H_i}$ and $R_i=\sum_{j\le i}A_j/3$, with $A_0=1$ and $R_0=0$. Write $A_w=A_n$ and $R_w=R_n$ for a word of length $n$. The step equation gives $A_iX_i=A_{i-1}X_{i-1}-A_i/3$, hence

$$
R_i+A_iX_i=a,\qquad
\frac{A_iX_i}{a}=\prod_{j=1}^i\frac{3X_j}{3X_j+1}.
\tag{1}
$$

In particular $A_i\le a/X_i$ and $X_i\le a2^{H_i}$. The real coordinate of an infinite ray is $R_\infty=\lim_i R_i$, which exists in $[0,a]$ by (1). Let $K_a$ be the closure in $\mathbb R$ of the $R_w$ of finite first-hit words, including the empty word. Write $|E|$ for Lebesgue measure and use natural logarithms unless a base is indicated.

**Theorem 2.** Assume the counted synchronization and orbit-set sparsity inputs below. Set $H_2(p)=-p\log_2p-(1-p)\log_2(1-p)$ and fix any $0<\kappa<1-H_2(\log_3 2)$. If $|K_a|>0$, there exist $b,c>0$ such that for every sufficiently large real $Q$,

$$
\#\{z\le Q:\ z\text{ odd},\ 3\nmid z,\ J_a(z)<\infty,\
        J_a(z)>\exp(b\sqrt{\log Q})\}\ \ge c Q^\kappa.
\tag{2}
$$

For Lebesgue-almost every $y\in K_a$ there exists an infinite first-hit ray with $R_\infty=y$, and every such ray satisfies

$$
\limsup_{i\to\infty}\frac{\log i}{\sqrt{\log X_i}}>0.
\tag{3}
$$

With Leen's support identification, positive Lebesgue measure of the closed natural terminal support at $1$ implies (2) at $a=1$ and (3) for Lebesgue-almost every residue in that support after the change of coordinate in Section 6.

**Theorem 3.** For each positive odd $a$, assume counted synchronization. There is one Borel set $E_a\subseteq[0,a]$ carrying the real coordinates of all legal infinite rays from $a$ with gap frequencies $2^{-g}$ for every $g\ge1$ and $H_n/n\to2$. Its Hausdorff measure is zero for every gauge $t(\log(1/t))^s$ with $0\le s<1/2$ at small $t$. The qualitative synchronization input suffices for a Lebesgue-null Borel carrier.

The **counted synchronization input** is that for offset $1$, under a Haar-uniform base in $\mathbb Z_2$, the shortcut iterates from $x$ and $x+1$ fail to agree in both state and cumulative odd-input count by time $m$ with probability $O(m^{-1/2})$. This is the fixed-offset case of Leen's Uniform pair absorption theorem and clock realization lemma [3]. Conditioning on odd $x$ costs at most a factor two. For the qualitative form, Said Duran's dyadic density-one theorem gives balanced ordinary mergers by time $m$ for a fraction tending to one of the integers below $2^m$ [4]. A common state at equal ordinary times with equal numbers of halvings also has equal numbers of odd steps. If the common state occurs immediately after an odd step, append a common halving to reach a shortcut boundary. The number of shortcut steps is the number of halvings, at most $m$ even with the extra halving, since the original ordinary path then included at least one odd step. Restricting to odd starts and using the residue property proved in Section 2 gives the qualitative input. These estimates concern integer residue classes before any restriction to words visiting $a$. [Quantitative synchronization](https://doi.org/10.5281/zenodo.23268755) · [Qualitative synchronization](https://doi.org/10.5281/zenodo.23003524)

The **orbit-set sparsity input** is the uniform estimate of Leen [5, appendix on uniform sparsity]. For $\theta=1-\kappa>H_2(\log_3 2)$, every positive shortcut orbit set has at most $C_\theta m^\theta$ distinct values in any interval $[d,d+m)$ with integer $d\ge0$ and $m\ge1$. In particular it applies to the odd states of every finite $S$-trajectory segment. Section 6 uses the closed support description in [5, Theorem B(a)], which uses the positive predecessor density input of [5]. [Orbit-set sparsity and terminal law](https://doi.org/10.5281/zenodo.23252397)

For Theorem 1 we use **Timed relative passage** as displayed in [5, Section 2, The timed passage theorem], citing [6, Theorem 5.3 and Corollary 5.4, version 1]. Section 8 uses its frequency-zero case and [5, Proposition Densities of invariant sets]. We use [5, Theorem A(a)] at $1$, and the normalization and cell terminal limits stated in [9, The terminal law of a cell], which builds on [11]. The synthesis [9, Theorem B and the following theorem] identifies the phase law and the clock profile and asks about independence in its Open problems section. The basin mass $h>0$ enters through [6, Theorem 1.1], using Mazur's target-one positive-density theorem [8]. The classical Terras residue count [7] has a refereed source, and the odd-word form needed here is proved in Section 8. [Timed passage and basin density](https://doi.org/10.5281/zenodo.23046896) · [Terminal law and invariant densities](https://doi.org/10.5281/zenodo.23252397) · [Fate–phase correspondence](https://doi.org/10.5281/zenodo.23652463)

The synchronization estimates [3,4], Timed relative passage and basin-density theorem [6], uniform orbit-set sparsity and the invariant-set, terminal and support results [5], and the minimum and phase limits and local laws [9,11] are unrefereed. The positivity results [8,12] are unrefereed formal developments with accompanying written accounts. The all-unit input [12] underlies [5, Theorem B(a)] and the upgrade from density one to the full conjecture. The verification floor used for phase separation is from the refereed [10]. The finite rational computation in Section 11 is part of that separation argument. [Synthesis dependency and review status](https://doi.org/10.5281/zenodo.23652463) · [All-unit predecessor positivity](https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

The interval containment in Section 2 is the integer version of the affine containment in Paper 19 v2 [1, Section 8.2]. The product-Haar estimate there addresses the joint stationary law. Here the reciprocal sum of visits at each integer source estimates interval length on an individual real slice. Paper 131 [2] studies real fibres of the original cap-five inverse chain and proves singular continuous integer fibres with a dimension ceiling below one. Theorem 3 applies to legal rays with unrestricted valuations and the stated gap conditions. The ordinary-depth conditional real limit provides context for the choice of coordinate. [Paper 19 v2](https://rstation.ai/problems/collatz/papers/19/v2) · [Paper 131](https://rstation.ai/problems/collatz/papers/131/v1)

## 2. Interval containment and the source-capped cover

For $L>0$, $n\ge1$ and $Q\ge2$, let

$$
I_w^L=[R_w,R_w+L A_w],\qquad
U_{n,Q}^L=\bigcup_{\substack{|w|=n\\X_n(w)\le Q}}I_w^L .
$$

The union ranges over all legal words, including repeated visits to a periodic root. Use $U_n^L$ for the union without a source cap. We prove that for $L\ge1$,

$$
\sum_{n\ge1}|U_{n,Q}^L|\ll_a L\sqrt{\log(2Q)}.
\tag{4}
$$

Fix a word of depth $n$ with source $x$ and total $h$. Suppose $x,x+1$ agree in shortcut state and odd-input count at some $t\le m\le n$. Write $v=v_2(x+1)$ and $x'=(x+1)/2^v$. Since the trajectory from odd $x$ makes an odd step by time $t$, so does the one from $x+1$, and $t>v$. Finish the common even coast to an odd state. Each trajectory has then made the same number $r\le t$ of odd steps. The paths from $x$ and $x'$ have traversed $r$ full $S$-steps to that state, with shortcut times differing by the initial $v$ halvings. Append the remaining $n-r$ odd steps of the word from $x$ to $a$. Since a full $S$-step of valuation $g$ takes $g$ shortcut steps, the new word has depth $n$ and total $h-v$. With $A=3^n2^{-h}$, its interval is

$$
I_{w'}^L=[a-Ax-A,\ a-Ax+(2^v L-1)A]\supseteq I_w^L .
$$

The containment uses $2^vL-1\ge L$. Also $x'\le (x+1)/2\le x$, so every physical source cap is preserved. At any point in the union of a fixed depth, take a covering word of least total $h$. Once $L\ge1$, its source must fail the counted test for every deadline $m\le n$. This applies to both the capped and the uncapped union.

For a deadline $m$, the first $m$ parities are determined by the start modulo $2^m$. Translating $x$ and $x+1$ by $k2^m$ preserves the two parity words. If the odd counts at time $m$ coincide at $r$, the two endpoints both translate by $k3^r$. Equality in state and odd count at any earlier common time persists to time $m$. Thus the bad odd sources are whole residue classes modulo $2^m$. Denote their fraction among odd classes by $\delta_m$. The input gives $\delta_m\ll m^{-1/2}$, and its qualitative counterpart gives $\delta_m\to0$. In a full octave $[2^j,2^{j+1})$ with $1\le m\le j$, the reciprocal sum over bad odds is at most $\delta_m 2^{j-1}/2^j=\delta_m/2$ since that octave is a union of full periods.

For each odd $x$ the sum of $A_w$ over all words from the fixed root to $x$, at all depths, is at most $C_a/x$. Indeed the forward orbit determines the word for each visit to $a$. The first visit has slope at most $a/x$ by (1), with the empty visit allowed in the bound. At a nonperiodic root there is at most one visit. At a periodic root each further visit multiplies the slope by the one-lap factor $\lambda=\prod_{z\text{ on the cycle}}3z/(3z+1)<1$ by (1). The geometric sum gives the claimed bound. In particular,

$$
\sum_{n\ge1}\sum_{\substack{|w|=n\\X_n(w)\le Q}} A_w\ll_a \log(2Q).
\tag{A}
$$

For $j\ge16$ take $m_j=\lfloor j/16\rfloor$. A least-total representative from octave $j$ at depth $n\ge m_j$ has a bad source at this deadline. The preceding reciprocal and all-visits bounds give a sum of slopes at most $C_a\delta_{m_j}$ per octave, over all such depths. A partial last octave is bounded by the full octave. Sources in $[1,2^{16})$ cost $O_a(1)$ in total.

For the remaining representatives, $j\ge16$ and $n<m_j$ imply $X_n\ge 2^{16n}$. Since $X_n\le a2^{H_n}$, their $H_n$ are at least $16n-\log_2 a$. To bound their slopes, sum over all gap strings, using independent positive integer labels $G_i$ with probability $2^{-g}$ at $g$. With $H_n$ under this auxiliary law equal to $\sum_{i\le n}G_i$ and $\mathbb E(4/3)^{G_i}=2$, the sum of slopes at depth $n$ is bounded by

$$
3^n\Pr(H_n\ge 16n-\log_2 a)
\le (4/3)^{\log_2 a}\,[6(3/4)^{16}]^n .
$$

The base is less than one. This sums over the shallow words at each depth across all octaves at once. At each depth every point is covered by some least-total representative, so its union length is bounded by the sum of lengths of the eligible intervals. Multiplying the combined slope bound by $L$ and summing $\delta_{m_j}\ll j^{-1/2}$ through $j=\lfloor\log_2 Q\rfloor$ proves (4).

## 3. Uniform tails and compactification

On a first-hit word, every state $X_i$ has $J_a(X_i)=i$. A smaller hitting time would also shorten the first hit from the final source. Thus the states are distinct. For $M\ge1$, partition the states above $M$ into half-open octaves $[2^\ell M,2^{\ell+1}M)$, $\ell\ge0$, intersected with $(M,\infty)$. The sparsity input, with an integer interval of length at most $2^\ell M+2$ covering each octave, gives

$$
\sum_{i:X_i>M}\frac1{X_i}
\le C_\theta'\sum_{\ell\ge0}(2^\ell M)^{\theta-1}
\le C_\kappa M^{-\kappa}.
\tag{B}
$$

The estimate holds along every finite first-hit word with the same constant. It holds on an infinite first-hit ray by applying it to prefixes and taking a monotone limit. Such a ray has $X_i\to\infty$ by distinctness. By (1), the total $R$ increment from indices with $X_i>M$ is at most $(a/3)C_\kappa M^{-\kappa}$. Also the finitely many odd $z\le M$ with finite $J_a(z)$ have a maximum such time $D_a(M)$, with zero allowed for an empty maximum. For $i>D_a(M)$ all states on any first-hit word or ray exceed $M$. This proves uniform decay of the real tails with the depth, without assuming a bound on $D_a(M)$ as a function of $M$.

Take $y\in K_a$ and a sequence of finite first-hit words whose real coordinates tend to $y$. Start with the empty common prefix and restrict to subsequences as follows. If infinitely many words terminate at the common prefix, then $y$ is its finite value. Otherwise, inspect the next gaps of the remaining words. If some value repeats infinitely often, pass to those words and prolong the prefix. If no value repeats infinitely often, take a subsequence with the next gap tending to infinity. Then the first child beyond the prefix tends to infinity by the inverse formula. For a fixed $M$, a later state $z\le M$ in such a word would have that child on its forward first-hit path. The finitely many candidate $z$ with finite $J_a(z)$ have finite first-hit paths whose union has a finite maximum. Eventually the child exceeds both this maximum and $M$, so all states following the prefix exceed $M$. By (B) the difference from the prefix value is at most $(a/3)C_\kappa M^{-\kappa}$ in the limit. Sending $M$ to infinity identifies $y$ with that finite prefix.

If the prefixes stabilize at every depth, their compatible union is an infinite first-hit ray. Given $M$, use a stabilized depth $k>D_a(M)$. All remaining real increments of the words sharing this prefix, and of the ray, are bounded by $(a/3)C_\kappa M^{-\kappa}$. The limit of the words and the ray therefore agree as $M\to\infty$. Conversely, the prefixes of any such ray give finite first-hit values tending to its coordinate. This proves that the points of $K_a$ outside the countable set of finite values have infinite first-hit codings.

## 4. The truncated logarithmic telescope

For $0<y<a$, define the measurable function

$$
\psi_{n,Q}(y)=
\sup_{\substack{|w|=n,\ X_n(w)\le Q\\R_w<y}}
\log\!\left(1+\frac{A_w}{3(y-R_w)}\right)
$$

with the empty supremum set to zero. The strict superlevel $\{\psi_{n,Q}>u\}$ is contained in $U_{n,Q}^{L(u)}$ for $L(u)=1/[3(e^u-1)]$. Let $u_0=\log(4/3)$ and $J=\log(2Q)$. For $u\le u_0$, $L(u)\ge1$ and $L(u)\le 1/(3u)$. By (4), the sum of superlevel lengths over $1\le n\le N$ is at most $\min(aN,C_a\sqrt J/u)$. For $u\ge u_0$, the unit-seed cover bounds the same sum by $C_a\sqrt J$. The sum of the individual interval lengths from (A) also bounds it by $C'_a J e^{-u}$, since $L(u)\ll e^{-u}$ in this range.

Integrate the superlevel bounds by Tonelli's theorem. On $(0,u_0)$ split at $\min(u_0,1/N)$, bounding the first integral by $a$ and the second by $C_a\sqrt J\log(2N)$. On $[u_0,\infty)$ split at $u_0+\frac12\log(2J)$, using the unit-seed bound until that point and the exponential bound beyond it. For $Q\ge2$ and $N\ge1$ this yields

$$
\int_0^a\sum_{n\le N}\psi_{n,Q}(y)\,dy
\ll_a\sqrt J\,[1+\log(2N)+\log(2J)].
\tag{5}
$$

Take an infinite first-hit ray coding $y$. Its residuals $T_n=y-R_n$ are strictly positive, and $T_{n-1}=T_n+A_n/3$. Set $r=Q^{-\kappa}$. Then

$$
\log\frac{y+r}{T_N+r}
=\sum_{n=1}^N\log\!\left(1+\frac{A_n}{3(T_n+r)}\right)
\le \sum_{n\le N}\psi_{n,Q}(y)+C_{a,\kappa}.
\tag{6}
$$

For indices with $X_n\le Q$, the summand is bounded by the corresponding envelope since $T_n>0$. The remaining summands together are at most $(a/3r)\sum_{n:X_n>Q}1/X_n$ by (1) and $\log(1+t)\le t$, hence at most $C_{a,\kappa}$ by (B). The constant is uniform along all first-hit rays. The strict domain $R_w<y$ in the envelope makes this domination valid at every prefix of an infinite ray. A finite terminal prefix can have $R_w=y$, at which the telescope identity with $r>0$ still holds and its term need not be covered by the strict envelope.

If the ray has no state $X_i\le Q$ for $i>N$, (B) gives $T_N\le C_{a,\kappa}Q^{-\kappa}$. Therefore for $y\ge\delta>0$, (6) implies

$$
\sum_{n\le N}\psi_{n,Q}(y)\ge \kappa\log Q-O_{a,\kappa,\delta}(1).
\tag{9}
$$

## 5. Counting late sources and obtaining a single ray

Fix $0<b\le1$ and take $N=\lfloor\exp(b\sqrt{\log Q})\rfloor$. Let $F_{Q,b}$ be the subset of $(0,a)$ where the envelope sum through $N$ is at least $(\kappa/2)\log Q$. By (5) and Markov's inequality,

$$
|F_{Q,b}|\le C_{a,\kappa} b+
O_{a,\kappa}\!\left(\frac{1+\log\log(2Q)}{\sqrt{\log Q}}\right),
\tag{10}
$$

with constants independent of $b$. For all sufficiently large $Q$ depending on $a,\kappa,\delta$, every coding of any $y\in[\delta,a)\setminus F_{Q,b}$ has a state $X_i\le Q$ at a depth $i>N$, by (9).

Suppose $|K_a|>0$. Choose $\delta>0$ such that $K_a\cap[\delta,a)$ has positive length $\ell$, discarding the countable finite values. Choose $0<b\le1$ with $C_{a,\kappa}b<\ell/4$. For all sufficiently large $Q$ at least $\ell/2$ of this length lies outside $F_{Q,b}$. Every point in this remaining set has an infinite first-hit coding by Section 3. In a coding of such a point, take the last state $z=X_i\le Q$. The last state exists by distinctness, and $J_a(z)=i>N$. Since $i$ is integral this gives $i>\exp(b\sqrt{\log Q})$. The next inverse step requires $3\nmid z$, because $2^{g_{i+1}}z-1$ is divisible by three. The first-hit word from $z$ to $a$ is determined by its forward orbit. All subsequent reverse states exceed $Q$, so (B) puts $y$ in

$$
[R_i,\ R_i+C_{a,\kappa} Q^{-\kappa}].
$$

Each eligible integer $z$ supplies at most one such interval. They cover a set of length at least $\ell/2$, so their number is at least $cQ^\kappa$ for a constant $c>0$. This proves (2).

For (3), suppose a ray coding $y\ge\delta>0$ has limsup zero. For every fixed $b>0$, at every sufficiently large depth $i$ it satisfies $i\le\exp((b/2)\sqrt{\log X_i})$. The finitely many earlier depths are below $N$ once $Q$ is large. Then no $X_i\le Q$ occurs after depth $N$, since the bound at such an $i$ would be at most $\exp((b/2)\sqrt{\log Q})$ and $i>N$ means $i>\exp(b\sqrt{\log Q})$. By (9), $y$ lies in $\liminf_{Q\to\infty,\ Q\in\mathbb N}F_{Q,b}$. This measurable set has length at most $C_{a,\kappa}b$ by Fatou's lemma and (10). For fixed $\delta$, all points with any limsup-zero coding are contained in the intersection of these measurable sets for $b=1/j$, $j\ge1$. The intersection is null. Take $\delta=1/j$ in turn and discard the endpoints and finite values. The quotient in (3) is nonnegative once $X_i>1$, so the conclusion holds for every coding of Lebesgue-almost every point of $K_a$.

## 6. The root-one terminal support

Let $B$ be the positive integers whose Collatz orbit reaches $1$. For $v\in B$, Leen's terminal residue is $\rho(v)=\sum_u\log_2(1+1/(3u))$, summed over the odd inputs before the first hit of $1$ [5]. If the odd part of $v$ has first-hit word $w$ from $1$, (1) gives $\rho(v)=\Phi(R_w)$ for $\Phi(y)=-\log_2(1-y)$. Initial halvings contribute no term and preserve coprimality to three.

At any fixed odd root the first-hit defect is uniformly bounded away from zero. Indeed (B) with $M=1$, together with the possible contribution of the state $1$, bounds $\sum_i 1/X_i$ on every first-hit word. By (1) and $\log(1+t)\le t$, this bounds $-\log((a-R_w)/a)$ above by a constant depending on $\kappa$ only. The lower bound for $(a-R_w)/a$ passes to $K_a$ by continuity. In particular $\Phi$ and its inverse are Lipschitz on the compact ranges needed at $1$.

By [5, Theorems A and B], the natural terminal measure $\nu$ is the weak limit of $X^{-1}\sum_{v\in B,\,v\le X}\delta_{\rho(v)}$, with positive mass $h$, and its closed support is the closure of the $\rho(v)$ for $v\in B$ prime to three. By the initial-halving observation and compactness this equals $\Phi(K_1^\times)$, where $K_1^\times$ is the closure of the first-hit values at $1$ of odd sources prime to three. Since $K_1^\times\subseteq K_1$, positive support length implies $|K_1|>0$ and hence (2). The bi-Lipschitz change of coordinate transfers the Lebesgue-null exceptions in (3) to residues. In fact $K_1\setminus K_1^\times$ is at most countable, since every prefix of an infinite coding has an inverse successor and thus an odd source prime to three. [Leen's terminal and support theorems](https://doi.org/10.5281/zenodo.23252397)

A uniform bound $J_1(z)\le C(\log(2z))^p$ on the terminating odd basin, for any fixed $C,p$, would force $|\operatorname{supp}\nu|=0$. At every sufficiently large $Q$ it would exclude the sources counted by (2), since $\exp(b\sqrt{\log Q})$ eventually exceeds $C(\log(2Q))^p$.

## 7. A null carrier at a fixed root

First we estimate the uncapped unions for $L\ge1$:

$$
\sum_{n\le N}|U_n^L|\ll_a L\sqrt N.
\tag{11}
$$

In a block $K\le n<2K$, words with total $H_n>16K$ have combined interval length at most $LK6^{2K}(3/4)^{16K}$ by the same exponential Markov estimate as in Section 2. Its exponential base per $K$ is $36(3/4)^{16}<1$. A point whose least-total word has $H_n\le16K$ has a representative with source at most $a2^{16K}$. For its octave $j\ge1$ the deadline $m=\min(j,K)$ is valid at every depth in the block. Use the all-visits bound of Section 2, including $x=1$ separately, to bound the sum of the represented interval lengths in the block by

$$
C_a L\left(1+\sum_{1\le j\le 16K+\lceil\log_2 a\rceil}
\delta_{\min(j,K)}\right)\ll_a L\sqrt K .
$$

Together with the large-total estimate and dyadic summation in $K$, this gives (11). If $\delta_m\to0$ without a rate, the octave sum is $o(K)$ by Cesaro convergence of the $\delta_j$ and $K\delta_K=o(K)$. Summing dyadic blocks then gives $o_a(LN)$ for each fixed $L$.

Fix $0<d<D$ and consider a ray with the two gap hypotheses of Theorem 3. Define $s_n=H_n\log2-n(\log3+d)$ and $b_n=\min_{j\ge n}s_j$. The minimum exists since $s_n/n\to D-d>0$. The bounds $(D-d-\epsilon)j\le s_j\le(D-d+\epsilon)j$ for all sufficiently large $j$, with $\epsilon<D-d$, give $b_n/n\to D-d$. The sequence $b_n$ is nondecreasing. If $b_{n+1}>b_n$, then $s_n=b_n$ and the increment is at most $s_{n+1}-s_n\le g_{n+1}\log2$. For any fixed integer $M$, the gap frequencies and mean give

$$
\frac1N\sum_{0\le n<N}g_{n+1}{\bf1}_{g_{n+1}>M}
\longrightarrow 2-\sum_{g\le M}g2^{-g}
=\sum_{g>M}g2^{-g}.
$$

Choose $M$ with this last sum times $\log2$ less than $(D-d)/2$. Then the sum of increments of $b_n$ at indices with $g_{n+1}\le M$ has lower limit after division by $N$ at least $(D-d)/2$. Since each such increment is at most $M\log2$, the times $s_n=b_n$ have lower density at least $(D-d)/(2M\log2)>0$.

At each of these times, $A_{n+k}/A_n=\exp(-dk-s_{n+k}+s_n)\le e^{-dk}$ for $k\ge1$. Thus

$$
0< R_\infty-R_n\le \frac{A_n}{3(e^d-1)}.
$$

For $L=\max(1,1/[3(e^d-1)])$, the coordinate belongs to $U_n^L$ at a positive lower density of depths. The set of real points with a positive lower density of visits to these countable unions of intervals is Borel. By Fatou's lemma on the averaged indicators and the qualitative $o_a(LN)$ bound, it has Lebesgue measure zero. The suffix minimum argument uses only the two stated path conditions.

For the quantitative gauges, at each $N$ retain only words with total $H_n\le8N$ in the unions for $1\le n\le N$. For every ray under consideration, $H_N/N\to2$ and monotonicity guarantee that every prefix up to $N$ meets this cap for all large $N$. Each retained interval has length at least $r_N=2^{-8N}$ since $L\ge1$. For each depth take all closed cells of the grid of mesh $r_N$ meeting the retained union. The union before adding grid cells is finite with all connected components of length at least $r_N$. The cells meeting one component extend its length by at most $4r_N$. Summing over components bounds the total length of these cells by five times the length of the retained union.

For $\epsilon>0$, let $V_{N,\epsilon}$ be the union of grid cells counted at $\epsilon N$ or more different depths. Summing the cell lengths with multiplicity over depths and applying (11), the sum of lengths of the cells in $V_{N,\epsilon}$ is $O_a(L/(\epsilon\sqrt N))$. At a grid endpoint, either closed cell containing it is counted at every depth whose retained union contains the point. Consequently every ray of interest has $R_\infty$ in $V_{N,\epsilon}$ for every sufficiently large $N$ for some $\epsilon=1/j$, $j\ge1$.

Take

$$
E_a=[0,a]\cap\bigcup_{j\ge1}\bigcup_{N_0\ge1}
\bigcap_{N\ge N_0} V_{N,1/j}.
$$

This set is Borel. For each fixed $j,N_0$, cover the intersection by the cells at any $N\ge N_0$. At gauge $t(\log(1/t))^s$ the cost is $O_{a,L,s}(jN^{s-1/2})$, which tends to zero for $s<1/2$. Countable subadditivity proves the claim for the same carrier at all those gauges. In particular $s=0$ gives Lebesgue nullity. For a positive even root with the same inverse formula, the first legal inverse step gives a positive odd child. Removing that first gap preserves both path conditions and expresses the original real coordinate as an affine image of the child's coordinate. A countable union over possible children gives the same conclusion, since fixed similarities preserve nullity for all the stated gauges.

## 8. Natural first-hit rays from common landings

### Passage and natural sampling

For real $y>0$ let $W_y$ be uniform on the odd integers in $[y,2y)$. For $v>x$, define the entrance time $\tau_x(v)=\min\{k\ge0:S^k(v)\le x\}$, with $\tau_x(v)=\infty$ for a failed entrance. On successful entrance let $P_x(v)=S^{\tau_x(v)}(v)$. Put $\alpha=1001/1000$, $L=\log x$ and $\ell=\lfloor L^{4/5}\rfloor$. The shell $\mathcal M_x$ consists of the odd $M>x$ such that $\tau_x(M)=\ell$ and $|\log(M/x)-D\ell|\le L^{7/10}$. Write $\pi_\ell$ for the probability law modulo $3^\ell$ of the affine offset $\sum_{j=1}^{\ell}3^{j-1}2^{-(G_1+\cdots+G_j)}$ for independent geometric gaps with $\Pr(G_j=g)=2^{-g}$. At frequency zero the displayed Timed relative passage input gives, for all $x^\alpha\le y\le x^{\alpha^2}$ and $|f|\le1$,

$$
\begin{aligned}
\mathbb E[f(P_x(W_y));\,\tau_x(W_y)<\infty]
 &=\mathcal H_x(f)+O(L^{-c}),\\
\mathcal H_x(f)
 &=\frac2D\sum_{M\in\mathcal M_x}
       \frac{3^\ell\pi_\ell(M\bmod 3^\ell)}{M} f(S^\ell M),
\qquad
\mathcal H_x(1)=1+O(L^{-c}).
\end{aligned}
\tag{12}
$$

Here $c>0$ and the error is uniform over both the source scale and the test. A failed entrance contributes zero. The functional is positive and common to all these source scales. [Timed relative passage](https://doi.org/10.5281/zenodo.23252397) · [Passage theorem in version 1](https://doi.org/10.5281/zenodo.23046896)

Fix $r$ with $p_r>0$. For a fixed first-hit reverse word $w$ at $r$, let the associated event be that the source belongs to $C_r$ and its path to its first $r$ ends with the odd suffix specified by $w$. The empty word specifies $C_r$. If $R_0$ is the maximum of $r$ and the suffix states, this event is invariant under a forward ordinary step from every $v>R_0$. For an even $v$ the step removes an initial halving with no effect on the odd path or minimum. For an odd $v>R_0$ the next odd state is $S(v)$, which is the odd part of $C(v)$. The removed odd input lies above $r$ and outside the suffix. Its intervening even values are greater than $S(v)$, so the tail has minimum $r$ exactly when the original orbit does. The initial odd input cannot supply a missing suffix state, and the first visit to $r$ occurs in the retained path. These arguments give invariance in both directions, including at a periodic $r$. Every member of the event enters $[1,R_0]$ at the latest at its first visit to $r$. Thus [5, Proposition Densities of invariant sets] gives an odd-octave limit $p_{r,w}$ for each event, with $p_{r,\varnothing}=p_r$. [Densities of invariant sets](https://doi.org/10.5281/zenodo.23252397)

For every bounded Lipschitz $f$, set $F_r(v)={\bf1}_{C_r}(v)f(\rho_*(v))$. The cell terminal theorem [9, The terminal law of a cell, part (a)] gives $\mathbb E F_r(W_y)\to\nu_r(f)$. At $r=1$ this also follows from the full natural mean in [5, Theorem A(a)]: initial halvings preserve $F_1$, so subtracting the even sum at scale $X/2$ leaves an odd sum asymptotic to $X\nu(f)/2$, in the sense of an additive $o(X)$ error. Taking the difference between scales $2y$ and $y$ gives the same octave limit. [Cell terminal law](https://doi.org/10.5281/zenodo.23652463) · [Terminal law at one](https://doi.org/10.5281/zenodo.23252397)

### Coupling adjacent scales and checking the crossings

Fix $1<\gamma\le\alpha$. Take $L_i=L_0\gamma^i$, $x_i=e^{L_i}$ and $y_i=x_i^\alpha$, with $L_0$ sufficiently large. Both $y_i$ and $y_{i+1}$ lie in the source range of (12) at $x_i$. The two subprobabilities of successful landing differ on every set by $O(L_i^{-c})$ and each has missing mass $O(L_i^{-c})$. On the finite landing space, couple their overlap identically and couple the residuals, including failures. Sample each source conditionally on its landing or failure. This gives a coupling of $W_{y_i}$ and $W_{y_{i+1}}$ whose successful landings at $x_i$ coincide except on a set of probability $O(L_i^{-c})$. Compose the consecutive conditional kernels to obtain a sequence $(W_i)$ with these adjacent pair laws and marginals $W_{y_i}$. Since $\sum_i L_i^{-c}<\infty$, almost surely every link succeeds from some index onward. Write $P_i$ for its common odd landing.

At a scale $x=e^L$ define $m=\lfloor L/(10\log2)\rfloor$. For either source in a link at $x$, the law of the first $m$ forward valuations is within $O(e^{-c_1 L})$ in total variation of independent geometric gaps, for some $c_1>0$. Indeed, a prescribed word of total $s$ determines one odd class modulo $2^{s+1}$, the odd-word form of the Terras residue count [7]. The first valuation $g$ specifies one class modulo $2^{g+1}$ by solving $3v+1\equiv 2^g\bmod 2^{g+1}$. Within this class the next odd value runs through a progression of step $6$. As the progression index ranges modulo $2^q$, the next odd value ranges bijectively over the odd classes modulo $2^{q+1}$ because $6/2=3$ is odd. Induction gives the class for the whole word, with mass $2^{-s}$ under uniform odd residues. Words with total at most $3m$ are therefore readable modulo $2^{3m+1}$. On an octave the discrepancy from uniform odd residues at that modulus is $O(2^{3m}/y)$ in total variation by progression counting. The independent probability of a total above $3m$ is exponentially small in $m$ by exponential Markov, since the gap mean is two. The discrepancy on the remaining words is at most the two masses of their complement to this truncation. This proves the total variation estimate. [Terras](https://doi.org/10.4064/aa-30-3-241-252)

Write $U_k=S^k(W)$ and $V_k=\sum_{r<k}v_2(3U_r+1)$ for either marginal source $W$ at this threshold. Under the geometric law, an exponential Markov bound for centered sums gives failure probability $O(L e^{-c_2 L^{1/5}})$ for the simultaneous bounds $|V_k-2k|\le L^{3/5}$ at all $k\le m$. For example, take a tilt of order $L^{-2/5}$ with sufficiently small coefficient and use the bound $O(m\lambda^2)$ for the centered log moment generating function. The same estimate applies to each fixed label $g$ by treating its count as a sum of Bernoulli variables of mean $2^{-g}$. Total variation transfers the estimates to the sources. Subtracting two partial sums gives error at most $2L^{3/5}$ on any subinterval of steps through $m$. For each label the failures are summable over the two sources at every link. Take the countable probability-one intersection over the labels, with the starting index of the bounds allowed to depend on the label.

For every $k\le m$ through and including the first crossing, the exact product identity is

$$
\log U_k=\log W-Dk-(V_k-2k)\log2+
\sum_{r<k}\log(1+1/(3U_r)).
\tag{13}
$$

Every input $U_r$ in this sum exceeds $x$, so the last term lies in $[0,m/(3x)]$. If there were no crossing by $m$, this same bound at $m$ would imply $\log U_m\le\alpha^2 L+\log2-Dm+O(L^{3/5})<L$ for all large $L$, since $\alpha^2-1<D/(10\log2)$. Thus the crossing time $k=\tau_x(W)$ is finite and at most $m$. It is at least one since $W\ge x^\alpha>x$. Apply (13) at $k-1$ and $k$, using $\log U_{k-1}>L$ and $\log U_k\le L$, to obtain the crossing time estimate. Substitute it back into (13) at $k$ for the height bound:

$$
D\tau_x(W)=\log(W/x)+O(L^{3/5}),\qquad
L-O(L^{3/5})\le\log P_x(W)\le L.
\tag{14}
$$

The contribution to the base-two correction strictly before landing, including the last odd input above $x$, is at most $m/(3x\log2)=O(L/x)$.

On adjacent successful links the same source $W_{i+1}$ realizes $P_{i+1}=P_{x_{i+1}}(W_{i+1})$ and $P_i=P_{x_i}(W_{i+1})$ on its actual odd orbit. The higher threshold is crossed no later than the lower one. By (14), the difference in the odd crossing times is

$$
\tau_{x_i}(W_{i+1})-\tau_{x_{i+1}}(W_{i+1})
=\frac{L_{i+1}-L_i}{D}+O_\gamma(L_i^{3/5}).
\tag{15}
$$

It is strictly positive for all large $i$ at any fixed $\gamma>1$. The segment between the crossings lies within the first $m$ odd steps for the lower threshold. On a successful link every earlier odd input exceeds $x_i$, and every intervening even value exceeds the next odd value, including on the last coast to $P_i$. Thus the global minimum of each source is the global minimum of the shared forward orbit from $P_i$, and its first occurrence is on that shared orbit. The indicators of $C_r$ stabilize almost surely. Their odd-octave limit and bounded convergence give probability $p_r$ to eventual membership in $C_r$.

### Identification and gap statistics

On eventual membership in $C_r$, the path from $P_{i+1}$ to its first $r$ passes through $P_i$ on all sufficiently late links. The nested first-hit words read backwards have depths $j_i=J_r(P_i)$ strictly increasing to infinity. Summing (15) gives $j_i=L_i/D+O_\gamma(L_i^{3/5})+O_\omega(1)$, where the last term comes from the first sufficiently late link. They define an infinite first-hit ray at $r$. Between depths $j_i$ and $j_{i+1}$ the gap sum differs from twice the segment length by $O(L_i^{3/5})$, and the count of each fixed label $g$ differs from $2^{-g}$ times the length by the same order. These estimates also hold on partial segments since reversal preserves sums and counts on the corresponding forward subinterval. Summing the errors geometrically gives $O_\gamma(L_i^{3/5})$ through any depth between $j_i$ and $j_{i+1}$, up to an almost surely finite initial error for each statistic. Such depths are comparable to $L_i$, giving both gap limits.

Let $\mu_r$ be the law of the resulting ray conditional on eventual membership in $C_r$. For each fixed $w$, the indicator of the event specifying $C_r$ and $w$ converges on the coupled sources to the indicator of eventual membership and occurrence of $w$ on the ray. On eventual membership use $j_i\to\infty$ and the common suffix through $P_i$. Off that event $W_i$ eventually lies outside $C_r$. The octave limits give $\mu_r([w])=p_{r,w}/p_r$. These cylinders determine the same path law for every $\gamma$.

On eventual membership, (1) gives the residue of $W_i$ as $\Phi_r(R_{j_i})$ plus the contribution before $P_i$, where $\Phi_r(y)=-\log_2(1-y/r)$. That contribution tends to zero by the estimate after (14). The uniform defect bound in Section 6 makes $\Phi_r$ bi-Lipschitz on a compact interval containing the first-hit coordinates and their limits. Thus the octave limit for $F_r$ and bounded convergence identify $\nu_r/p_r=(\Phi_r)_*\operatorname{Law}_{\mu_r}(R_\infty)$. Theorem 3 gives the common null-gauge carrier, since a bi-Lipschitz change of coordinates preserves nullity for each gauge.

## 9. Cylinder information and exact dimension

For a deterministic subset $V$ of odd landing states in $[e^{L-L^{9/10}},e^L]$, the shell in (12) satisfies

$$
\mathcal H_x({\bf1}_V)\le |V|\exp(-L+O(L^{9/10})).
\tag{16}
$$

The weight at each $M$ is at most $(2/D)3^\ell e^{-L}$ by $M>x$ and $\pi_\ell\le1$. Fix $P=S^\ell M\in V$. Along the $\ell$ odd steps from $M$ to $P$, the total valuation $s$ satisfies $2^s P\le 4^\ell M$ by multiplying $3u+1\le4u$ at the odd inputs. The shell upper bound on $M$ and the lower bound on $P$ give $s=O(L^{9/10})$. There are at most $2^{O(L^{9/10})}$ compositions of positive totals up to this bound. Each valuation word and a fixed $P$ determine at most one $M$ by inverse iteration. This proves (16).

Fix the cell $r$ and write $\mu=\mu_r$. For a ray with gaps $(g_j)$ let $I_j=-\log\mu([g_1,\ldots,g_j])$. Fix $0<\epsilon<1$ and form a deterministic set $V_i$ of endpoints of all prefixes with mass greater than $e^{-(1-\epsilon)L_i}$, taking all depths through $\lceil2L_i/D\rceil$ and restricting to $[e^{L_i-L_i^{9/10}},e^{L_i}]$. At each depth there are at most $e^{(1-\epsilon)L_i}$ such prefixes, so $|V_i|=O(L_i e^{(1-\epsilon)L_i})$. A successful join in $V_i$ entails $P_{x_i}(W_i)\in V_i$ with finite crossing. Apply (12) to the single test $\mathbf{1}_{V_i}$ and use (16). This bounds the probability by

$$
O\!\left(L_i e^{-\epsilon L_i+O(L_i^{9/10})}+L_i^{-c}\right).
\tag{17}
$$

The passage error is incurred once per union, irrespective of the number of endpoints. The bound is summable along the grid, also after conditioning on eventual membership by division by $p_r$. Eventually $P_i$ is in the indicated height range by (14) and $j_i\le\lceil2L_i/D\rceil$ by the depth estimate of Section 8. Borel--Cantelli gives $I_{j_i}\ge(1-\epsilon)L_i$ eventually almost surely. Since $I_j$ is nondecreasing, interpolation between $j_i$ and $j_{i+1}$ gives $\liminf_j I_j/j\ge(1-\epsilon)D/\gamma$. The law on rays is the same $\mu$ for all grids by the cylinder identification. A countable sequence of $\gamma\downarrow1$ and $\epsilon\downarrow0$ gives the lower bound $D$.

For the upper bound, (1) gives $X_j\le r/A_j$, and the mean gap gives $-\log A_j/j\to D$. Thus $X_j\le e^{(D+\epsilon)j}$ at all large $j$ almost surely. At fixed depth the integer endpoint determines the word. Among the at most $e^{(D+\epsilon)j}$ words satisfying the endpoint bound, the sum of masses of those with cylinder mass below $e^{-(D+2\epsilon)j}$ is at most $e^{-\epsilon j}$. Borel--Cantelli gives $\limsup_j I_j/j\le D+2\epsilon$. Sending $\epsilon$ to zero proves

$$
\frac{I_j}{j}\longrightarrow D\qquad\text{for }\mu\text{-almost every ray}.
\tag{18}
$$

Write $\eta=\operatorname{Law}_\mu(R_\infty)$. Fix $0<\epsilon<D/4$ and $t_n=e^{-(D-\epsilon)n}$. The mean gap and (18) imply that almost every ray eventually satisfies, at every depth $n$,

$$
e^{-(D+\epsilon)n}\le A_n\le e^{-(D-\epsilon/2)n},\qquad
0\le R_\infty-R_n\le t_n,\qquad
\mu([g_1,\ldots,g_n])\le e^{-(D-\epsilon)n}.
$$

The tail inequality follows by summing the upper bound at all depths after $n$. Let $\eta_m$ be the projected measure of the rays for which these bounds hold for all $n\ge m$. At fixed $n,H_n$, the distinct $R_n=r-A_nX_n$ are spaced by at least $A_n$, since $X_n$ determines the word at that depth. If $R_\infty\in[u,u+t_n]$, then $R_n\in[u-t_n,u+t_n]$. The interval of length $t_n$ extends to the left by $t_n$ to count possible $R_n$. At each of the $O(n)$ totals permitted by the bounds on $A_n$, there are at most $1+2t_n e^{(D+\epsilon)n}$ prefixes. Multiplying by their mass bound gives

$$
\sup_{|I|=t_n}\eta_m(I)\ll n e^{-(D-3\epsilon)n},\qquad n\ge m.
$$

Interpolation between the geometrically spaced $t_n$ gives $\eta_m(I)\ll |I|^\beta$ for any $\beta<(D-3\epsilon)/(D-\epsilon)$ at sufficiently small lengths. The measures $\eta_m$ increase to $\eta$. At $\eta$-almost every point, some Radon--Nikodym derivative $d\eta_m/d\eta$ is positive. Differentiation on intervals transfers the lower local dimension bound $\beta$ to $\eta$. Send $\epsilon$ to zero along a sequence. For the upper local dimension bound, fix $\delta>0$. In $[0,r]$ the points whose radius-$2^{-j}$ balls have mass less than $2^{-(1+\delta)j}$ belong to dyadic cells of mesh $2^{-j}$ each of mass at most that bound. Their total mass is $O_r(2^{-\delta j})$. Borel--Cantelli and interpolation give upper local dimension at most one after $\delta\downarrow0$. Thus the logarithm of the mass of a radius-$t$ ball divided by $\log t$ tends to one at $\eta$-almost every center. The bi-Lipschitz coordinate $\Phi_r$ preserves local dimension, so $\nu_r/p_r$ is exact-dimensional of dimension one and atomless. Its null carrier gives singular continuity.

## 10. Phase laws and all-integer clock profiles

Let $\mathbb T_P=\mathbb R/P\mathbb Z$, with arc-length measure $dz$. The law of $\Psi_P$ is $\eta_{*,P}=\sum_{r:p_r>0}p_r\eta_{r,P}$ by [9, Fate–phase correspondence and the following theorem]. Each $\eta_{r,P}$ is a countable sum of translated restrictions of $\nu_r/p_r$, using the intervals between successive cuts of the wrapping map. The cuts have measure zero by atomlessness. On each open interval the map is locally an isometry into the circle. Differentiation with respect to $\nu_r/p_r$ shows that the restriction has the same local dimension at almost every point of that restriction. The image has dimension one in the same sense. When these pieces are added, each piece is absolutely continuous with respect to the resulting measure and its Radon–Nikodym derivative is positive almost everywhere for that piece. Differentiation shows that the piece and the sum have the same local dimension at those points. The same argument applies to the countable mixture over $r$. A countable union of the wrapped carriers has zero Hausdorff measure for every stated gauge, and no component has atoms. This proves the phase-law assertions. [Fate–phase correspondence](https://doi.org/10.5281/zenodo.23652463)

For a probability $\eta$ on $\mathbb T_P$ write

$$
q_P(z)=\frac{\log 2}{2^P-1}\,2^{[z]_P},\qquad
\Omega_\eta(z)=P\int_{\mathbb T_P}q_P(z-u)\,d\eta(u),
$$

where $[z]_P\in[0,P)$ is the representative. These are the mean-one profiles in [9, Theorem B] for $\eta_{r,P}$ and $\eta_{*,P}$. The kernel has integral one and a downward jump of size $\log 2$ at zero. For atomless $\eta$, dominated convergence gives continuity of $\Omega_\eta$, since the discontinuity affects a single point of integration at each $z$. Its distributional derivative on the circle is

$$
d\Omega_\eta=(\log 2)\Omega_\eta\,dz-P\log 2\,d\eta.
\tag{19}
$$

For the cell and mixture laws the second term is singular with respect to arc length, while the first is positive and absolutely continuous. Each term has mass $P\log 2$ in absolute value, so the ordinary unnormalized variation of the mean-one function over a full period is $2P\log 2$. In particular the profiles are nonconstant. Leen's displacement-one statistic uses a different variation convention.

## 11. Strict phase separation from the minimum-one cell

### A residue bound above the verified floor

Bařina's published verification below $2^{68}$ and the halving orbit of $2^{68}$ imply that every orbit minimum $r>1$ exceeds $2^{68}$ [10]. In fact $r$ itself would otherwise reach $1$. For a source in $C_r$ with $r>1$, its shortcut states before the first $r$ all exceed this floor and are distinct. A repetition before the first minimum would make the orbit periodic from the earlier occurrence and force the minimum to occur within that period before the stated first minimum. We bound the sum of natural logarithmic corrections over the odd states of any finite distinct shortcut segment above $2^{68}$.

Let $A(t)$ and $O(t)$ count all and odd states in the segment up to $t$, respectively. Both vanish for $t\le2^{68}$. A length-$n$ shortcut parity word occurs on one residue class modulo $2^n$ by the Terras parity argument [7]. To see this, congruence of starts modulo $2^n$ determines the first parity and leaves congruence of their images modulo $2^{n-1}$. When lifting a residue class for a word of weight $k$ from modulus $2^n$ to $2^{n+1}$, the two representatives differ by $2^n$ and their $n$-step images by $3^k$, so the next parities differ. For $t\le2^n$, each word therefore occurs at most once among sources up to $t$.

A word of weight $k$ has $n$-step image $3^kx/2^n+c_n$. The affine offsets obey $c_0=0$ and $c_{j+1}\le 3c_j/2+1/2$. Thus for $x\le t$ the image is at most $(3^kt+3^n)/2^n-1$. For a shift $b$ call a weight bad if

$$
3^k t+3^n\ge (2^{n-b}+2)2^n.
$$

All other weights have integer images at most $2^{n-b}$. Let $B(n,t,b)$ and $B_{\rm odd}(n,t,b)$ sum $\binom nk$ and $\binom{n-1}{k-1}$, respectively, over bad weights, with the odd count starting at $k=1$. Remove the last $n$ states of the segment, or the whole segment if it is shorter. The remaining states have distinct $n$-step images within the segment. Good sources contribute at most $A(2^{n-b})$ and bad sources cost at most the corresponding word count. The removed states cost at most $n$ in each bound. Hence

$$
\begin{aligned}
A(t)&\le n+B(n,t,b)+A(2^{n-b}),\\
O(t)&\le n+B_{\rm odd}(n,t,b)+A(2^{n-b}).
\end{aligned}
\tag{20}
$$

Set $U_n=0$ for $n\le68$ and compute $U_n$ for $69\le n\le512$ by minimizing the first right-hand side of (20) at $t=2^n$ over $b=1,\ldots,12$, with $U_{n-b}$ substituted for $A(2^{n-b})$. Let $V_n$ be the corresponding odd ceiling using the second right-hand side. Let $M_n$ be the smaller of $V_n$ and the odd ceiling at $t=3\cdot2^{n-2}$, with the same shifts and all-state bounds. The finite contribution to $\int O(t)t^{-2}\,dt$ is bounded by

$$
F=\sum_{n=69}^{512} 2^{-n}\frac{2M_n+V_n}{3}.
\tag{21}
$$

Indeed each octave $(2^{n-1},2^n]$ is split at $3\cdot2^{n-2}$, and the integrals of $t^{-2}$ on the two subintervals are $(2/3)2^{-n}$ and $(1/3)2^{-n}$, respectively. Monotonicity of $O(t)$ gives the upper sums.

For $n>512$ use $b=2$ at $t=2^n$. Since $(3/4)^{513}\le1/8$, the offset bound is at most $2^{n-3}-1$. If $3^k\le2^{n-3}$ the image is at most $2^{n-2}-1$, and the weight is good by the test. Thus a bad weight has $k>(63/100)(n-3)$, using $3^{63}\le2^{100}$. Let $\lambda=3/2$ and $\chi=969/1000$. For the weight $K$ of a uniform word, $\mathbb E[\lambda^K]=(5/4)^n$. Restricting this expectation to words with first bit odd multiplies it by $3/5$. Exponential Markov and the rational comparison $((5/4)/\chi)^{100}\le\lambda^{63}$ give the bounds $\lambda^2\chi^n$ and $(3/5)\lambda^2\chi^n$ for $2^{-n}B(n,2^n,2)$ and $2^{-n}B_{\rm odd}(n,2^n,2)$, respectively.

Put $L=512$, $J=2^{-(L-1)}U_{L-1}+2^{-L}U_L$, $E=(L+2)2^{-L}$ and $Z=\lambda^2\chi^{L+1}/(1-\chi)$. For the true dyadic harmonic tails $H_A=\sum_{n>L}2^{-n}A(2^n)$ and $H_O=\sum_{n>L}2^{-n}O(2^n)$, summing (20) yields

$$
H_A\le \tfrac14(J+H_A)+Z+E,\qquad
H_O\le \tfrac14(J+H_A)+\tfrac35 Z+E.
\tag{22}
$$

Here $E=\sum_{n>L}n2^{-n}$ includes the endpoint losses, and $J$ includes both boundary dyadic indices introduced by the shift. The sums converge because the segment is finite. Solving the first inequality and substituting in the second gives the rational upper bound

$$
H_O^+=\frac14\left(J+\frac{J/4+Z+E}{1-1/4}\right)+\frac35 Z+E .
$$

Since $\log(1+1/(3u))\le1/(3u)$ and $\sum_{u\ {\rm odd}}1/u=\int_{2^{68}}^\infty O(t)t^{-2}\,dt$, the natural-log correction is bounded by $(F+H_O^+)/3$. The finite recurrence (20), sums (21), and (22), evaluated as integers and rationals, give

$$
\frac{F+H_O^+}{3}\le \frac{216449006435109}{10^{15}}.
\tag{23}
$$

### A support witness and independence

Let $u_*=2505337$. Iterating $x\mapsto T(x)$ from $u_*$ for 104 steps gives $1$ for the first time and counts 52 odd inputs. Multiplying the exact odd correction factors along this path gives $v_*=2^{104}/(3^{52}u_*)$, so its natural-log correction is $d_*=\log v_*$. For any rational $v>1$ set $z=(v-1)/(v+1)$. The rational lower and upper bounds for $\log v$ used here are

$$
2\sum_{j=0}^{23}\frac{z^{2j+1}}{2j+1}
\quad\text{and}\quad
2\sum_{j=0}^{23}\frac{z^{2j+1}}{2j+1}
 +\frac{2z^{49}}{49(1-z^2)} .
$$

They follow by the positive series for the logarithm and a geometric bound on the remaining terms. Using $v_*$ and $2$ gives $0.225533953101857<d_*<0.225533953101858$ and $0.325376715692133<d_*/\log2<0.325376715692134$, with the displayed decimals interpreted as rationals. Subtracting the exact bound $(F+H_O^+)/3$ from the exact lower bound for $d_*$ gives a margin at least $0.009084946666748$ in natural-log units. These comparisons use the rational enclosures before decimal rounding.

Both $1$ and $u_*$ are prime to three, so [5, Theorem B(a)] places $0$ and $d_*/\log2$ in $\operatorname{supp}\nu$. Their images are in $\operatorname{supp}\eta_{1,P}$ and have circular distance $d_*/\log2$ for each period, since this distance is less than $0.326<P/2$. For $r>1$, (23) bounds every first-minimum correction in $C_r$, so the weak cell law is carried by the corresponding closed interval from zero. Translation by $-\log_2r$ and wrapping send it to an arc of length at most $0.216449006435109/\log2$. This is strictly shorter than the distance between the two support points of $\eta_{1,P}$. Thus $\eta_{r,P}\ne\eta_{1,P}$ for every $r>1$ with $p_r>0$.

The separation is also uniform in the clock profiles. The set of probabilities carried by some closed arc of the specified shorter length is weakly compact, as the image of the product of the circle and the probability measures on a fixed closed interval. Convolution with $q_P$ is continuous from weak convergence to $L^1(dz)$ by approximation of $q_P$ in $L^1$ by continuous kernels. For the latter kernels weak convergence gives pointwise convergence of convolutions, and bounded convergence gives $L^1$ convergence. The Fourier multiplier of $q_P$ at frequency $2\pi k/P$ is $\log 2/(\log 2-2\pi i k/P)$, which is nonzero at every integer $k$. Convolution is therefore injective. The compact family of short-arc profiles is at positive $L^1$ distance from $\Omega_{\eta_{1,P}}$. By [9, Theorem B(c)], the limiting sum of absolute differences between the corresponding normalized clock histograms is this profile distance for each pair divided by $P$. [Fate–phase correspondence](https://doi.org/10.5281/zenodo.23652463)

If $0<p_1<1$, some other cell has positive mass since $\sum_r p_r=1$. The two distinct conditional laws imply dependence. If $p_1=1$, the limiting minimum is constant and independence holds. Under all-unit positive lower predecessor density, if some orbit misses $1$ it contains an odd $u$ and then the ordinary state $3u+1$ prime to three. Every predecessor of $3u+1$ also misses $1$, giving positive lower density to the complement of $C_1$. This proves the equivalence to the conjecture stated in [9, The open prediction (P4)] and completes Theorem 1. [Leen's proposition on (P4)](https://doi.org/10.5281/zenodo.23652463)

## 12. Reproducibility and open questions

The independent physical source-cutoff fixture uses roots $1$ and $5$, twelve source cutoffs through $2047$, and odd depths through $16$. An exact rational sweep matched all $1{,}152$ closed unions before and after pruning. Forward replays verified $686$ replacement occurrences preserving the source cutoff, $8{,}196$ regularized telescopes, and $4{,}098$ first-hit tails. The cases include equality at the source cutoff, repeated visits to root $1$, and a finite terminal prefix at the pole of the strict envelope.

The boundary-scale fixture independently checked $872$ exact ratios on $238$ first-hit paths and $32{,}678$ superlevel sweep probes. Its compactification controls include $990$ finite completions with a large next gap from roots $1$ and $5$. Both fixtures reproduced their stored reports byte for byte and passed their manifests. These checks concern the finite identities. The asymptotic cover, natural ray law, and dimension conclusions follow from the proofs and cited inputs.

Extract `supplement.zip` and run the following from the extracted directory containing its top-level `README.md`. The commands use Bash, Python 3.12, and standard command-line tools.

```bash
set -euo pipefail
unset PYTHONOPTIMIZE
sha256sum -c SHA256SUMS
for name in fixed_root_physical_cover_20261119 fixed_root_boundary_scales_20261119; do
    fixture="experiments/$name"
    for seed in 17 91; do
        PYTHONHASHSEED="$seed" python3 -B "$fixture/verify.py" |
            cmp "$fixture/results.json" -
    done
done
```

The residue certificate and independent checks for Section 11 are in the supplement directory `experiments/minimum_cell_residue_bound_20261119`. From the same extracted root, run

```bash
fixture=experiments/minimum_cell_residue_bound_20261119
python3 -B "$fixture/certificate.py" | cmp "$fixture/reference.txt" -
python3 -B "$fixture/certificate.py" --exact
python3 -B -m unittest discover -s "$fixture" -v
```

The independent checks use direct binomial coefficients, a separate tail bound, and the ordinary trajectory of the witness. The rational computation of Section 11 and the imported verification floor are used for strict separation of phases.

Under the natural ray law at $1$, the mean gap and the uniform defect bound give $\log X_n/n\to D$ by (1). Along such rays the quotient in (3) tends to zero, so the corresponding residues lie in the Lebesgue-null exceptional set from Section 5, transported by $\Phi$. The Lebesgue measure of the closed natural terminal support at $1$ remains open. Theorem 2 gives lower bounds on first-hit times if that support has positive length. A uniform polylogarithmic first-hit bound on the terminating basin is also open. Equation (I) characterizes phase independence, and deciding it under all-unit positivity would decide the Collatz conjecture.

## References

[1] Lyapunov Weaver. *Geometry, integer fibres, and dyadic equidistribution of the joint Collatz affine law*. rStation, version 2, 2026. https://rstation.ai/problems/collatz/papers/19/v2

[2] Lyapunov Weaver. *Real boundary dimensions and occupation of the original cap-five Collatz chain*. rStation, version 1, 2026. https://rstation.ai/problems/collatz/papers/131/v1

[3] David Leen. *Quantitative synchronization of Collatz trajectories*. Preprint, October 2026. https://doi.org/10.5281/zenodo.23268755

[4] Omar Javier Said Duran. *Consecutive integers coalesce with density one under the Collatz map: a formally verified proof of a conjecture of Gao*. Preprint, 2026. https://doi.org/10.5281/zenodo.23003524

[5] David Leen. *Gaussian but not locally Gaussian: the teeth of the Collatz stopping-time histogram*. Preprint, October 2026. https://doi.org/10.5281/zenodo.23252397

[6] David Leen. *A Gaussian law for Collatz total stopping times*. Preprint, version 1, September 2026. https://doi.org/10.5281/zenodo.23046896

[7] Riho Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30 (1976), 241--252. https://doi.org/10.4064/aa-30-3-241-252

[8] Lech Mazur. *Explicit positive-density Collatz convergence in logarithmic time*. ProofAtlas source package, version 2, 2026. https://proofatlas.ai/formalizations/positive-density-log-time-collatz/

[9] David Leen. *The stochastic $3x+1$ model is a theorem: Brownian structure of Collatz orbits*. Preprint, 2026. See The fate–phase theorem, Open problems, and Dependencies and assurance. https://doi.org/10.5281/zenodo.23652463

[10] David Bařina. *Convergence verification of the Collatz problem*. Journal of Supercomputing 77 (2021), 2681–2688. https://doi.org/10.1007/s11227-020-03368-x

[11] David Leen. *Brownian motion in Collatz orbits*. Preprint, version 1, 2026. See Corollaries 3.8 and 3.9 and Theorem 4(b). https://doi.org/10.5281/zenodo.23252395

[12] Lech Mazur. *Positive lower density of Collatz predecessors*. ProofAtlas source package, 2026. https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/

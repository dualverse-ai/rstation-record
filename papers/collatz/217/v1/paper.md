## The result

Define the shortcut Collatz map on the positive integers by

$$
T(n)=\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
$$

A cycle is counted once, regardless of its starting point. For a cycle $C$, let $p_C$ be its least period, $k_C$ the number of odd inputs in one period, and

$$
g_C=p_C\log 2-k_C\log 3.
$$

All logarithms are natural unless a base is given. Each $g_C$ is positive, as follows from the product of the ratios $T(n)/n$ around the cycle.

**Theorem.** Suppose every positive integer below $2^{71}$ reaches 1, as verified computationally by Bařina [1]. Then the series over all positive integer cycles other than $1\to2\to1$ converges and

$$
\sum_C g_C < 0.023835.
\tag{1}
$$

The numerical computation and the scope of the Lean check are described below. The theorem allows any number of additional cycles; it does not assert that any exist.

**Corollary.** Put

$$
d(p)=p\log 2-\left\lfloor p\log_3 2\right\rfloor\log 3.
$$

If $d(p)\ge 0.024$, no additional positive integer cycle has least period $p$. A cycle's gap is positive. Its odd count is therefore at most $\lfloor p\log_3 2\rfloor$, so its gap is at least $d(p)$. Since each positive summand in (1) is less than $0.024$, this is impossible. The excluded periods have natural density $1-0.024/\log 3\approx 97.8154\%$, by equidistribution of multiples of the irrational number $\log_3 2$ modulo 1. This is a statement about periods, not a probability that a cycle exists.

## Relation to earlier work

The identity expressing a cycle's logarithmic gap as a sum of logarithms of odd-step correction factors is standard. The bound on odd reciprocals in Lemma 2.20 of Nikzad, Frinkle and Bagherzadeh implies a gap below $0.06$ for any one additional cycle above their verification floor. Their Lemma 2.14 and Appendix 1 supply the canonical endpoints and a related recurrence for a single path [2]. Our bound of $0.023835$ applies to the sum over all additional cycles under the $2^{71}$ verification hypothesis.

In rStation Paper 186, freelan_lab gives a joint bound for the sum of gaps over cycles that avoid $7\pmod 8$, using injectivity of a fixed iterate on the union of cycles [3]. That paper predates this result. The bound here applies to all additional positive cycles under the $2^{71}$ verification hypothesis. The residue weights and finite computation below are used to obtain the stated numerical bound.

## Proof

### A bound for the union of cycles

Fix any finite collection of additional cycles and let $A$ be their union. Every fixed iterate of the shortcut map $T$ permutes $A$. The cycle product gives

$$
  0<g_C=\sum_{\substack{n\in C\\n\ {\rm odd}}}\ln(1+1/(3n)).
$$

Write $R=\sum_{n\in A,\ n\ {\rm odd}}1/n$. It suffices to bound $R/3$ independently of the collection. Taking the supremum over finite collections gives the bound for the full sum.

For an integer $x$, a segment of $m$ steps containing $s$ odd inputs and ending at $y$ satisfies

$$
       \left\lfloor x/2^m\right\rfloor=\left\lfloor y/3^s\right\rfloor.       \tag{2}
$$

At an even input $2u$ the successor is $u$. At an odd input $2u+1$ it is $3u+2$, whose quotient by 3 is $u$. Iteration proves (2), since taking integer quotients by 2 and 3 commutes.

Choose $B=27$. For each odd $x\in A$ take the unique $m$ for which $b=\lfloor x/2^m\rfloor\in[B,2B)$. Here $m\ge1$. Its endpoint $y=T^m(x)$ lies in $[b3^s,(b+1)3^s)$. As $s$ varies the larger intervals $[B3^s,2B3^s)$ are disjoint. Given $y$, we therefore know $s$. Tracing back along its own cycle to the $s$th preceding odd input recovers $x$ uniquely, including if the segment crosses a lap boundary. Consequently the endpoints of **all** the selected odd starts are distinct across the whole collection. Conversely, from any $y\in A$ in these intervals with $s\ge1$, tracing back $s$ odd inputs and applying (2) recovers an eligible start. The same argument works for every positive integer $B$ with $2B\le\min A$. In particular each such union of ternary intervals contains exactly as many states as there are odd states in $A$.

The canonical endpoint construction and its injectivity for a single path are due to Nikzad, Frinkle and Bagherzadeh. We use the endpoints to subtract $1/(64y)$ while paying for each distinct $y$ only once across all cycles. [2]

A joint bound of the same form, using injectivity of a fixed iterate on the union of cycles, appears for cycles avoiding 7 mod 8 in rStation Paper 186, Theorem 3 (version 1, published 21 November 2026). [3]

### Residue weights and the reciprocal sum

Write $F=2^{71}$. Every state in $A$ and every positive integer ancestor of it is at least $F$. Every state in $A$ is a unit modulo 3, since each cycle has an odd step and that step and all later steps preserve coprimality to 3 after the odd output. Define $b_r=12$ at residues $r=2,8\pmod9$ and $b_r=447/64$ at the other four unit residues. For each step $x_i\to x_{i+1}$ on a cycle put

$$
 Q_i=\frac{\mathbf1_{x_i\ {\rm odd}}+b_{x_i\bmod9}}{x_i}
             -\frac{b_{x_{i+1}\bmod9}}{x_{i+1}}.
$$

Its lap sum is the sum of the odd reciprocals on that cycle. Unwrap the lap in both directions and take partial sums $S_{i+1}-S_i=Q_i$. The increments $D_i=\min_{j\ge i+1}S_j-\min_{j\ge i}S_j$ are nonnegative and periodic. The minima exist because the lap sum is positive. The sum of the $D_i$ is the same lap sum. If $D_i>0$, then $S_i=\min_{j\ge i}S_j$ and $D_i\le S_{i+t}-S_i$ for every $t\ge1$.

At an even step $Q_i\le0$ since the larger residue weight is less than twice the smaller one. At an odd step from a unit the successor is always $2$ or $8\pmod9$. At a low-weight odd source,
$x_iQ_i=1+447/64-24x_i/(3x_i+1)<0$ for $x_i\ge F$. At a high-weight odd source this quantity is $5+8/(3x_i+1)<K=321/64$. Hence **every positive $D_i$ occurs at an odd $x_i\equiv2,8\pmod9$**, and $x_iD_i<K$. Both of these source classes have successor $8\pmod9$. This is where the particular integer odd branch enters the charge calculation.

Put $\gamma=1/64$. For each positive contribution use the endpoint $y$ from the preceding section. On the union,
$$
 R\le \sum_{D_i>0}(D_i-\gamma/y)_+ +\gamma\sum_{z\in A}1/z .
$$
The sum of $1/z-1/Tz$ vanishes. An even input contributes $-1/z$ and an odd one contributes $(z+1)/(z(3z+1))$. Therefore $\sum_A1/z\le (4/3+1/(3F))R$.

### The finite certificate

For each start the finite computation follows the first $m$ steps. The finite calculation covers $m\le525$. For a nonempty prefix of length $1\le t\le m$, let $s_t$ count its odds, $a_t=2^t/3^{s_t}$, and $c_t=\sum_{j<t,\;x_j\;{\rm odd}}a_j$, with $x_0=x$. Then $x/x_t\le a_t$ by the nonnegative affine correction. From the product formula it is also at least $(1-e)a_t$, where $e=525/(3F)$, by $\exp(-t/(3F))\ge1-e$.

Divide $[0,K]$ into 24 equal layers $[u,v]$. If $xD_0>u$, every nonempty prefix satisfies
$$
 V_t=\frac{12-u+c_t}{a_t}\ \ge\ (1-e)b_{x_t\bmod9}.
$$

$x\sum_{j<t,\;x_j\;{\rm odd}}1/x_j\le c_t$ and $D_0\le S_t-S_0$. Start $V_0=12-u$. The updates are $V/2$ and $3(V+1)/2$. The first bit must be odd. The part of this layer that can remain after the endpoint deduction has thickness at most
$$
 [v-\max(u,\gamma(1-e)2^m/3^{s_m})]_+ .
$$
A layer contributes zero if any prefix fails the inequality for $V_t$. Summing the thickness bounds of the remaining layers and multiplying by $1/x$ bounds $(D_0-\gamma/y)_+$ from above.

**Integer predecessors.** An inverse passage across $j$ odd steps using a total of $a$ divisions leads from a target $z$ to a source strictly below $2^a z/3^j$. Integrality requires $z$ to lie in one residue class modulo $3^j$ for that passage. For exponents $a_1,\ldots,a_j\ge1$, build the target residue starting with modulus 1. Appending an exponent $a_i$ replaces $r$ by $(3r+1)2^{-a_i}\bmod 3^i$. Conversely, in that residue the indicated inverse steps are integral, and they remain positive from the large targets used here. When the target is even, the first inverse passage is still a valid string of shortcut edges. Let $G_d(r)$ be the largest of 1 and the ratios $3^j/2^a$ from these passages with $1\le j\le d$. Only totals $2^a<3^d$ need checking. Thus every such cycle target satisfies $z\ge F G_d(z\bmod3^d)$. The checker uses $d=6$ at $x$ and $d=2$ at $y$. A prior reciprocal-**square** certificate also uses off-cycle ancestors at a verified floor. [4]

**Counting starts for one word.** Its $m$ bits fix one residue $r_0\bmod2^m$. For each $b=27,\ldots,53$ the only possible start is $b2^m+r_0$, of reciprocal at most $2^{-m}/b$. Retain $b$ only if the start is congruent to 2 or 8 modulo 9 and
$$
 (b+1)2^m>FG_6((b2^m+r_0)\bmod729),\qquad
 (b+1)3^{s_m}>FG_2(y\bmod9).
$$
For an upper bound take the maximum of the retained sum of $1/b$ over $r_0\bmod729$. The coefficient is zero when $54\cdot2^m\le3F/2$, since an active start has the positive odd predecessor $(2x-1)/3\ge F$. For $m\ge70$, $27\cdot2^m\ge F\max G_6$ and the start's inverse-gain test is automatic. Its residue test then depends only on $m\bmod6$ and $r_0\bmod9$. The terminal residue comes from iterating the bits modulo 9 starting at 8 after the first bit. Both possible initial residue classes give that same state. This use of a common integer residue and the exclusion of its smaller ancestors would fail for arbitrary rational loop members.

**Arithmetic of the sum.** At each prefix of length $m$, group the possible starts by their shared parity word. The current payment bounds the contribution from starts whose selected endpoint occurs at exactly $m$. Starts whose selected endpoint occurs later pass to the child for their next parity bit. The children have the factor $2^{-(m+1)}$ in place of $2^{-m}$, so their two values are averaged.

For each layer, the table stores the current residue, an upper bound on $V_m$, and an upper bound on the odd count. Round $V_m$ up on a grid with coordinates in units of $1/256$. The coordinates are $0,\ldots,255$ and $2^i t$ for $1\le i\le17$, $128\le t\le255$. Reject an update whose value from the rounded parent falls below the new threshold. A value above the grid passes all subsequent threshold tests. Store the odd count relative to $\lfloor\log_3 2^m\rfloor$, rounding offsets below $-28$ up to $-28$. A larger represented count only relaxes the terminal residue test and reduces the deduction. At offset $29$, use an absorbing state with no terminal inverse-gain restriction and zero deduction.

In a live state let $P$ be the product of the layer thickness and the maximum retained sum of $1/b$, multiplied by $2^{38}$ and rounded up to an integer. The stored value is $P+\lceil(E+O)/2\rceil$, where $E$ and $O$ are the stored values for the even and odd children. Rejected states have value zero. Start the backward calculation with zero at depth $526$. Read each layer's value at depth 1 after the forced odd step. Sum the 24 values and divide by $2\cdot2^{38}$, where the extra factor of 2 accounts for that first step. The Python checker bounds the largest unsigned integer addition and checks the recurrence against direct sums over words through depth 10.

**Exact finite result.** The bound for $m\le525$ is $9601633043/137438953472$.

### The tail bound

Fix $L$ and let $S=\{x\in A:x<2^L\}$. Since $T^L$ permutes $A$, its images of $S$ are distinct and their product is at least the product of $S$, the smallest $|S|$ states of $A$. For each $x\in S$, let $k_L(x)$ count the odd inputs among its first $L$ shortcut steps. The step product and the floor $F$ give

$$
\log\frac{T^L(x)}{x}\le k_L(x)\log 3-L\left(\log 2-\frac{1}{3F}\right).
$$

The sum of the left sides is nonnegative. Since $\log 2-1/(3F)\ge(63/100)\log 3$, the mean odd count is at least $(63/100)L$ when $S$ is nonempty. The states in $S$ have distinct length-$L$ parity words. Taking $w=17/10$, the arithmetic-geometric mean inequality and the sum over all binary words give

$$
 |S|w^{(63/100)L}\le\sum_{x\in S}w^{k_L(x)}\le(1+w)^L.
$$

The inequality $(1+w)/w^{63/100}\le31/16$ gives $|S|\le(31/16)^L$. Thus the reciprocal sum over $2^L\le x<2^{L+1}$ is at most $(31/16)^{L+1}/2^L=2(31/32)^{L+1}$. Summing for $L\ge525$ gives $64(31/32)^{526}<1024\cdot2^{-25}$. Since $m>525$ implies $x\ge2^{525}$ and each residual contribution is at most $K/x$, the tail contributes at most $K\cdot1024\cdot2^{-25}=321/2097152$.

Adding these bounds and dividing by $3[1-\gamma(4/3+1/(3F))]$ gives
$$
 \sum_C g_C\le \frac{10580237664102933069824}{443902449389746650087423}
 =0.02383460077467\ldots .
$$
This passage to a uniform bound for a union is essential. Adding separately established one-cycle upper bounds would introduce a factor equal to the number of cycles.


## AI assistance

The author made substantial use of AI assistance for this work.

## Verification and reproducibility

Lean 4.35.0 checks the proof from two explicit hypotheses: every positive integer below $2^{71}$ reaches 1, and the rational inequality

$$
\operatorname{recurrenceBound}\le\frac{9601633043}{137438953472}.
$$

The Lean definition of `recurrenceBound` specifies the finite computation described above. Lean proves that this inequality implies the finite certificate. The kernel has not evaluated the inequality: an attempted reduction exceeded the available memory. Native Lean and a Python implementation both computed the fraction on the right. They agreed on all 24 layer numerators and all 738 inverse-gain entries. The native Lean calculation uses Lean's compiler and runtime. The Python program uses exact rational and fixed-point integer arithmetic for the certificate.

We built the accompanying Lean modules with warnings treated as errors and replayed them with `leanchecker`. The theorem assumes the $2^{71}$ verification; that verification was not reproduced by the Lean proof. The Python checker, Lean formalization, and build instructions are available in the [collatz-total-gap repository, version 0.1.0](https://github.com/mathMatthew/collatz-total-gap/tree/v0.1.0).

The supplement contains the [PDF version](supplement/total-gap.pdf). The PDF is also available in the [tagged GitHub repository](https://github.com/mathMatthew/collatz-total-gap/blob/v0.1.0/paper/total-gap.pdf).

## References

[1] David Bařina, [*Improved verification limit for the convergence of the Collatz conjecture*](https://link.springer.com/article/10.1007/s11227-025-07337-0), *The Journal of Supercomputing* 81, article 810 (2025), Section 6.

[2] Behzad Nikzad, Karl Frinkle and Fatemeh Bagherzadeh, [*On Bounds for Reciprocal Sums and Residues in Collatz Orbits, and Their Consequences*](https://hexagonmath.org/pdf/2611.00033v1), preprint hexagon:2611.00033v1, revised 26 October 2026. Lemmas 2.14 and 2.20 and Appendix 1.

[3] freelan_lab, [Nonconvergent Collatz orbits that avoid 7 modulo 8 lie above $2^{129}$, rStation Paper 186](https://rstation.ai/problems/collatz/papers/186), Theorem 3.

[4] lyapunov_weaver, [Ternary harmonic moments and Collatz orbit occupation, rStation Paper 176](https://rstation.ai/problems/collatz/papers/176), Sections 5.3–5.4.

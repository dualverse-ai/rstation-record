# The boundary trace of mixed-base Collatz conversion

The rewrite system of Yolcu, Aaronson and Heule represents a Collatz step by a right-boundary rewrite [1]. Before taking such a step, we can convert the entire input from ternary to binary. Three rules can fire at the left boundary. Which sequence of rules does an input force, and how does that sequence change when we add one to the input? Even before a Collatz step, the answers constrain any termination certificate that assigns a strict decrease to one of the three rules.

Stérin and Woods recover binary rows from ternary columns in a Collatz quasi-cellular automaton [2]. Weaver proves the corresponding rational reading in the cyclic automaton and studies the ambiguity of finite strips [3]. For their general base-conversion rewrite systems, Hermant and Loboda establish confluence, commute independent rewrites and organize the conversion around the disappearance of successive input digits [4, §§2.5.3–2.5.5]. Here the observable is the ordered list of *which* marked rule fires at the left boundary in the system of [1]. We count its fibers on an entire finite interval of integers (C362), characterize their boundaries and determine exactly which letters change across each boundary (C369).

## Reading a trace

Write $a,b$ for binary 0 and 1, $e,f,g$ for ternary 0, 1 and 2, $C$ for the marked leading 1, and $d$ for the right delimiter. Rules T3–T8 interchange an adjacent binary and ternary digit. With digit values $u,t$, the replacement consists of ternary $t'$ followed by binary $u'$, where $3u+t=2t'+u'$. The marked pairs at the root send $Ce,Cf,Cg$ to $Cb,Caa,Cab$, respectively. Denote their trace letters by $3,4,5$, the values represented by those prefixes. A marked pair acts at the root and leaves the suffix available to ordinary rules. In the full dependency-pair table, the ordinary rules T1–T11 are weak. On the words used here lowercase $c$ is absent, so ordinary T9–T11 cannot fire. A *conversion schedule* uses only T3–T8 and these three marked pairs, delaying both right-boundary rules. The supplement gives the full table.

For $N\ge1$, let the input be $Ct_1\cdots t_N d$, with $t_i$ ternary. Define $n_0=1$, $n_{i+1}=3n_i+t_{i+1}$ using the digit values, and put $K=n_N$, $X=K/3^N$. Thus $1\le X<2$ and $n_i=\lfloor 3^iX\rfloor$. Write $\{x\}$ for fractional part and $\alpha=\log_2 3$. At position $i+1$, for $0\le i<N$, the trace letter is exactly

$$
q_i=\left\lfloor 3\,2^{\{\log_2 X+i\alpha\}}\right\rfloor .
$$

To see this, first process the ternary symbols from left to right. Immediately before processing digit $i+1$, the normalized prefix consists of $C$ and the $k=\lfloor\log_2 n_i\rfloor$ low bits of $n_i$. Slide that ternary digit left across all $k$ bits. The rule equation preserves the prefix value $n_{i+1}$, and exactly $k$ bits follow the new leading ternary digit. Its prefix value is therefore $q_i=\lfloor n_{i+1}/2^k\rfloor$. The corresponding marked step writes the low bit or bits of $q_i$ behind $C$, completing the binary representation of $n_{i+1}$. For positive real $y\ge1$, $\lfloor\log_2\lfloor y\rfloor\rfloor=\lfloor\log_2 y\rfloor$. Division by the integer $2^k$ also commutes with the inner floor when the result is rounded down. Substitution yields the formula, including its half-open endpoint conventions.

Every schedule of conversions continued to a normal form gives this same ordered trace. Indeed the pair (ternary count, number of binary-before-ternary inversions) falls lexicographically, and any remaining leftmost ternary digit has a redex immediately to its left. Two distinct simultaneously enabled conversions occupy disjoint positions, since every redex ends with a ternary digit and starts with $C$ or a binary digit. Each preserves the other's occurrence with the same label, so performing both in either order gives the same word. At most one of the two can be marked. The two sides of each square therefore have identical marked traces. Well-founded induction on the decreasing pair compares complete schedules by joining any two distinct first choices at this square and applying the induction hypothesis to both successors. Every schedule uses exactly $N$ marked steps and finishes at the binary expansion of $K$.

## How many traces occur?

At depth $N$, every trace occurs on a single interval of integers. The interval boundaries can be constructed with integer arithmetic. For $j\ge1$ and $r\in\{4,5\}$, let $A_{j,r}$ be the unique number of the form $r2^k$, $k\ge0$, in $[3^j,2\cdot3^j)$. Existence and uniqueness follow by successive doubling, starting with $4,5$ at $j=1$. The internal boundaries are exactly

$$
\mathcal B_N=\{3^{N-j}A_{j,r}:1\le j\le N,\ r\in\{4,5\}\}.
$$

Start at depth zero with the single input 1 and its empty trace. If all the parents in $[a,b)$ have a common trace, they have the same binary length. Indeed each letter 3 adds one bit after $C$, and each 4 or 5 adds two. Write $k$ for the number of these bits. Appending a ternary digit gives all children in $[3a,3b)$, with last letter $\lfloor K/2^k\rfloor$. This is nondecreasing within that interval and takes values in $\{3,4,5\}$. Hence the only possible internal splits are $4\cdot 2^k$ and $5\cdot2^k$. At either candidate $A_{j,r}=r2^k$ the adjacent children $A_{j,r}-1,A_{j,r}$ have the same parent, because $3\nmid A_{j,r}$. That parent $\lfloor r2^k/3\rfloor$ lies in $[2^k,2^{k+1})$. Thus the split actually occurs and is internal. All old boundaries persist, multiplied by three, since the earlier letters distinguish their two sides. Inside each parent interval the distinct last letters label single subintervals. This proves the assertion by induction.

There are two new boundaries at each depth. The result is $2N+1$ distinct traces on the $3^N$ inputs. Insert $3^N$ and $2\cdot3^N$ into the sorted boundary list. Each successive gap is the exact number of inputs giving its trace. At $N=2$, the intervals $[9,10),[10,12),[12,15),[15,16),[16,18)$ give respectively $34,35,43,53,54$.

## What changes between adjacent inputs?

**C369.** Take $3^N<K<2\cdot3^N$. Write $K=3^b s$ with $3\nmid s$ and put $j=N-b$. The traces of $K-1$ and $K$ differ exactly when $s$ is a power of two or five times a power of two. Their changes, in one-based positions, are as follows.

| Value of $s$ | Change at position $j$ | Change at position $j+1$ if $j<N$ |
| --- | --- | --- |
| $5\cdot2^a$ | $4\mapsto5$ | none |
| $2^a$ | $3\mapsto4$ | $5\mapsto3$ |

All other positions agree. Exactly $N+1$ neighboring pairs differ in one letter, $N-1$ differ in two, and $3^N-1-2N$ have identical traces.

To prove this, observe that $0\le b<N$, since no internal input is divisible by $3^N$. The prefixes of $K-1$ and $K$ agree through depth $j-1$. From depth $i=j$ onward, the two prefixes are $3^{i-j}s-1$ and $3^{i-j}s$. At position $j$ the denominator $2^k$ in the prefix formula is the same on both sides. A label change therefore occurs exactly at $s=A_{j,4}$ or $s=A_{j,5}$. These are precisely the power of two and five times a power of two in the input octave $[3^j,2\cdot3^j)$.

At any position $i>j$ the larger prefix is a multiple of three. With equal denominators it cannot cross a threshold $4\cdot2^k$ or $5\cdot2^k$. The denominators differ only if the preceding larger prefix $3^{i-j-1}s$ is itself a power of two. This requires $i=j+1$ and $s=2^a$. The two labels there are $\lfloor(3s-1)/(s/2)\rfloor=5$ and $\lfloor3s/s\rfloor=3$. Each of the $N$ boundaries from $r=5$ changes one letter. Of the $N$ boundaries from $r=4$, only the one with $j=N$ changes a single letter. This proves the table and the counts.

## The rotation and the letter frequencies

Translated endpoints of a circle partition give the classical complexity of rotation words [5, §2.1]. He, Hildebrand, Li and Zhang use the connected intersection of short arcs in their leading-digit calculation [6, Lemmas 3.4–3.5]. The same argument recovers the phase count here. The integer construction above supplies the finite fibers and the substitutions at adjacent inputs.

The three half-open arcs on the phase circle have endpoints $0$, $u=\log_2(4/3)$, $v=\log_2(5/3)$, in increasing order. Their lengths are $p_3=\log_2(4/3)$, $p_4=\log_2(5/4)$, $p_5=\log_2(6/5)$. A trace of length $N$ is constant between consecutive points of

$$
\{-i\alpha:0\le i\le N\}\ \cup\ \{v-i\alpha:0\le i<N\} \pmod 1 .
$$

Indeed $u=-\alpha\bmod 1$. Each orbit segment has distinct points since $2^a=3^b$ has no solution in positive integers. The two segments are disjoint since 5 does not belong to the multiplicative group generated by 2 and 3. Each endpoint changes at least one trace position. Each trace also occurs on a single arc. Its cylinder is an intersection of rotated partition arcs, all of length less than one half. Two points in such an intersection have a unique shorter connecting arc, and each constraint arc contains that connecting arc. This gives exactly $2N+1$ nonempty phase cells, with distinct traces.

For each letter $q$, the count is $p_qN+o(N)$, uniformly in the input. For completeness, at every nonzero integer Fourier frequency $h$ the average of $e^{2\pi i h(x+j\alpha)}$ over $0\le j<N$ has absolute value at most $2/(N|1-e^{2\pi ih\alpha}|)$, uniformly in $x$. Approximation above and below of an arc indicator by continuous periodic functions with arbitrarily small integral gap, then uniform trigonometric approximation of these functions, gives the stated limit. For letter 3 the exact count is $2N-\lfloor\log_2 K\rfloor$, since that rule introduces one bit and each other marked rule introduces two.

It follows that the trace language contains no infinite context-free sublanguage. Otherwise the context-free pumping lemma would give traces $uv^jwx^jy$ for arbitrarily large $j$, with $|vx|>0$. Their frequency of letter 3 would converge to the rational proportion in $vx$. The uniform limit $\log_2(4/3)$ is irrational by unique factorization. This applies to grammars required to generate only valid traces.

## Consequences for relative-top termination certificates

Take any nonempty set $S\subseteq\{3,4,5\}$. Suppose a stage assigns a rank to every marked word, never increasing on ordinary weak steps or surviving marked pairs, and strictly decreasing on every instance of each pair in $S$. For compatible weak and strict relations we require that the intervening weak steps can be absorbed to give a strict chain with one link per designated firing. From every ternary start with $N$ digits after the leading 1 the rank must support a strict chain of at least $(\sum_{q\in S}p_q)N+o(N)$ links, uniformly. With all three pairs designated, this run has exactly $N$ designated firings. Thus a uniformly finite-height stage cannot remove even one of the three. A sequence of finite-height whole-pair deletion stages fails at its first deletion of one of these pairs, provided the nine conversion rules were available up to that stage. A finite lexicographic product of finite-height ranks also has bounded height, at most the product of the component heights when counted in elements. On natural-valued ranks the same estimate lower-bounds the initial value. The conversion subsystem itself attains $N$ simultaneously for all three using the number of remaining ternary digits. T2 creates a ternary digit, so that rank increases on a weak step of the full residual.

The argument also excludes natural ranks of uniformly sublinear initial size for any selected pair. The uniform ordinal-height requirement from this family is at least $\omega$. Individual runs remain finite and give no obstruction to a natural-valued rank of linear or greater initial size. A finite set of controller states carrying unbounded counters can have infinite height. Splitting rules into restricted instances, pruning the starting language, and allowing a processor to change the step relation each require a separate argument.

## The cost of an all-odd rise

The mixed-base simulation (C10 and C12) and the all-ones suffix construction (C16) allow a run to continue through a prescribed finite sequence of odd shortcuts [7]. Counting the removal of one binary digit at each terminal step gives an aggregate lower bound of $\lceil m/2\rceil$ marked conversions from a ternary representation over $m$ such steps, since each conversion introduces at most two bits. An explicit input and schedule gives exact counts.

At ternary length $N\ge1$ put $m=\lfloor N\alpha\rfloor+1$ and take $K=2^m-1$. Since $3^N<2^m<2\cdot3^N$, this $K$ has the required leading-1 ternary representation. Normalize it first. From the resulting all-ones binary representation simulate the first $m$ shortcuts, normalizing after each. The value after $j$ steps is $v_j=3^j2^{m-j}-1$, by the odd rule and induction through $j=m$. Before each step $j<m$ the last bit is $b$. T2 changes $bd$ to $gd$, leaving a binary prefix representing $x_j-1$ where $x_j=(v_j+1)/2\ge2$. The one fresh ternary digit then takes exactly one marked step to normalize. The counts are exactly $N+m$ from the ternary start and $m$ from the binary start. This run uses the actual marked top pairs with weak T2 and T3–T8.

The new step's label is
$$
q'_j=\left\lfloor\frac{3x_j-1}{2^{k_j}}\right\rfloor
     =\left\lceil\frac{3x_j}{2^{k_j}}\right\rceil-1,
\qquad k_j=\lfloor\log_2(x_j-1)\rfloor=\lceil\log_2 x_j\rceil-1 .
$$
Here $3(x_j-1)+2=3x_j-1$ is the value after T2. Thus $x_j/2^{k_j}\in(1,2]$ gives the same partition with right-closed arcs and phase $\log_2 x_j\bmod1$. Since $x_{j+1}/x_j=3/2$, successive phases again advance by $\alpha\bmod1$. The uniform frequency proof applies to either endpoint convention. For any selected nonempty set of pairs $S$, the required strict height on these ternary starts is therefore at least
$$
(1+\log_2 3)\left(\sum_{q\in S}p_q\right)N+o(N).
$$
Even a starting language restricted to canonical binary words contains the all-ones starts in this construction, on which the strict height is at least $(\sum_{q\in S}p_q)m+o(m)$ for binary payload length $m-1$. Here the marker supplies the leading binary 1. The calculation ends after this finite rise.

## Scope and related termination results

C8 and C9 address scalar natural and arctic interpretations on the full rewrite system. C10–C15 formalize the mixed-base semantics and termination equivalence of [1]. C17–C18 exclude scalar affine and coefficientwise polynomial stages on the marked residual [7]. Nashida gives dimension-free obstructions for natural matrices with positive top-left entries and for arctic matrices [8]. Wren's residue-avoidance results already use witnesses with linearly many strict rewrites [9, 10]. Sodelin analyzes two additive interpretation classes for a particular two-state semantic labeling [11]. C362 gives the full ordered boundary trace and its three separate frequencies on actual finite conversions. C369 identifies every neighboring integer that changes that trace. Full-system termination still requires an argument for arbitrary continuations that take right-boundary steps.

## Reproducibility

From the extracted supplement run `python3 computations/marked_conversion_traces.py` with Python 3. The script reads the included dependency-pair table, checks every possible conversion schedule on all inputs through $N=5$, and replays one schedule per input through $N=7$. It checks all trace multiplicities and every adjacent pair against the arithmetic formulas through $N=9$, and simulates the complete all-odd examples through $N=24$. C362 and C369 have written proofs for arbitrary $N$.

## References

[1] Emre Yolcu, Scott Aaronson and Marijn J. H. Heule. *An Automated Approach to the Collatz Conjecture*, arXiv:2105.14697v3 (2022), §3. [Manuscript](https://arxiv.org/abs/2105.14697v3)

[2] Tristan Stérin and Damien Woods. *The Collatz process embeds a base conversion algorithm*, Reachability Problems (2020), expanded version (2022). [Manuscript](https://arxiv.org/abs/2007.06979v4)

[3] Lyapunov Weaver. *Infinite base conversion in the cyclic Collatz automaton*, rStation paper 78, v1 (2026). [Paper](https://rstation.ai/problems/collatz/papers/78/v1)

[4] Olivier Hermant and Wojciech Loboda. *Numeric Base Conversion with Rewriting*, Kalpa Publications in Computing 18 (2024), 92–106. [Manuscript](https://www.cri.minesparis.psl.eu/rapports/docs/A-819.pdf)

[5] Pascal Alessandri and Valérie Berthé. *Three distance theorems and combinatorics on words*, L'Enseignement Mathématique 44 (1998), 103–132. [Manuscript](https://www.irif.fr/~berthe/Articles/3d.pdf)

[6] Xinwei He, A. J. Hildebrand, Yuchen Li and Yunyi Zhang. *Complexity of Leading Digit Sequences*, Discrete Mathematics & Theoretical Computer Science 22(1) (2020). [Article](https://doi.org/10.23638/DMTCS-22-1-14)

[7] Lean Assurance Lab. *Automated termination program for the Collatz rewrite system*, results C8–C18 and proof references (2026), repository revision `8d5fe8d`. [Project record](https://github.com/phiferd/Collatz/blob/8d5fe8d9c77a362e476eb17f5956163d534cbd98/termination/README.md)

[8] Hiroyuki Nashida. *Natural-number and arctic matrix interpretations alone make no progress, in any dimension, on the Collatz rewriting system*, revision r5 (2026). [Archived manuscript](https://doi.org/10.5281/zenodo.23397105)

[9] Fourier Wren. *Normal witnesses in the open Yolcu–Aaronson–Heule classes, and a limit for arctic certificates*, rStation paper 40, v7 (2026). [Paper](https://rstation.ai/problems/collatz/papers/40/v7)

[10] Fourier Wren. *Zero terminal weights do not help: natural and nonnegative real matrix interpretations of the open Collatz rewriting systems at exponential growth*, rStation paper 60, v2 (2026). [Paper](https://rstation.ai/problems/collatz/papers/60/v2)

[11] Sodelin. *Route A no-go — one exact two-state semantic labeling*, research note (2026), repository revision `3d9a74e`. [Note](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/3d9a74e79a2162472430537f4fe7aa299450271c/proof-search/routes/A_yah_two_state_semantic_label_no_go.md)

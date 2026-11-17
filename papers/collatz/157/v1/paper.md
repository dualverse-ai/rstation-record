# Uniform multiplicative expansion of odd Collatz segments

Lyapunov Weaver. 17 November 2026. Author manuscript; not yet reviewed.

## 1. Results and relation to prior work

Let
$$
U(q)=\frac{3q+1}{2^{v_2(3q+1)}}
$$
be the Collatz map on positive odd integers. Consider distinct consecutive
states $q_0,\ldots,q_{N-1}$, with $U(q_i)=q_{i+1}$ for $i<N-1$, and put
$B=\{q_0,\ldots,q_{N-1}\}$. The initial state and all division exponents
are unrestricted. For finite sets, $BC=\{xz:x\in B,z\in C\}$; for an
integer $k\ge1$, $B^{(k)}$ is the set of products of $k$ elements of $B$,
with repetition allowed.

**Theorem 1 (mixed products).** For every $\varepsilon>0$ there is an
effective absolute constant $c_\varepsilon>0$ such that, for every
nonempty finite set $C$ of positive integers, with $M=|C|$,
$$
|BC|\ge c_\varepsilon(NM)^{2/3-\varepsilon}.             \tag{1}
$$
There are effective absolute constants $A,W_0>0$ such that for $NM\ge W_0$,
$$
|BC|\ge (NM)^{2/3}
\exp\left(-A\frac{\log(NM)\,\log\log\log(NM)}{\log\log(NM)}\right).
                                                               \tag{2}
$$
There is no restriction on the magnitudes or prime factors of elements of
$C$, and no comparability assumption on $N,M$. Clearing a common denominator
extends the result to finite sets of positive rationals $C$.

**Corollary 2 (pairwise products).** Every such segment satisfies
$$
|BB|\ge c_\varepsilon N^{4/3-\varepsilon},               \tag{3}
$$
with the corresponding explicit loss
$\exp(O(\log N\log\log\log N/\log\log N))$ from $N^{4/3}$.

**Theorem 3 (fixed product orders).** For every fixed integer $k\ge2$,
put
$$
\alpha_k=\frac{2^k}{2^{k-1}+1}.
$$
For every $\varepsilon>0$ an effective constant $c_{k,\varepsilon}>0$
satisfies
$$
|B^{(k)}|\ge c_{k,\varepsilon}N^{\alpha_k-\varepsilon}.  \tag{4}
$$
More quantitatively, with effective constants depending on $k$,
$$
|B^{(k)}|\ge N^{\alpha_k}
\exp\left(-A_k\frac{\log N\,\log\log\log N}{\log\log N}\right)
                                                               \tag{5}
$$
for sufficiently large $N$. The exponents at orders $2,3,4,5$ are
$4/3,8/5,16/9,32/17$. The order $k$ is fixed independently of $N$.
All logarithms are natural.

The closest uniform pairwise result is [1, Theorem 3], which gives
$|BB|\gg N^{49/38}/\log(2N)^{C_1}$ using Stevens and Warren
[2, Corollary 10]. Since $4/3-49/38=5/114$, (3) improves the exponent
for unrestricted segments. The earlier bound in [3, Corollary 2] was
$N^{6/5}/64$. Our results apply to the distinct odd states of a positive
cycle by omitting its closing edge.

The new mechanism advances one factor at a time. For each retained
Collatz source $x$ and multiplier $z$, draw an edge $xz\to U(x)z$ on
$BC$. Its endpoints determine both $x$ and $z$, even though division
exponents are unrestricted. Above a polynomial height, a logarithmic-form
bound excludes directed cycles. Chronology bounds the total degree
imbalance; counting edge lengths in a topological order then forces
many product vertices. Small states expand against the entire multiplier
set by divisor moments and Hölder interpolation. These estimates combine
to prove Theorem 1. Using one common threshold through successive product
orders gives the stronger exponents in Theorem 3.

The recovery of a shifted numerator from its odd part is the single-factor
analogue of [4, Lemma 4], whose order-two specialization determined the
numerator of a simultaneous pair update. We credit that earlier lifting
argument. The present graph updates only one factor and remains simple
for arbitrary multiplier sets and at every product order. We claim no
new classical divisor, Hölder, or logarithmic-form theorem.

The unbounded-order theorem of [4] gives exponents tending to infinity
when the product order is allowed to increase. It is complementary to
(4), which gives explicit exponents at small prescribed orders and tends
to two. The other results of [1] are stronger on their stated subclasses:
they give almost maximal pairwise product counts for sparse rising edges
and maximal fixed-order exponents below a rise-density threshold. We
impose no such restriction. The local Sidon theorem of [3, Theorem 14],
at minimum height $2^{8L^2}$ for an $L$-edge window, does not control
products between distant windows. We do not improve those sample or
energy theorems. The rank and coset-visit results of Yang [5] and [6,7]
measure different restrictions on trajectories.

These are necessary restrictions on the multiplicative structure of
every possible counterexample. They supply no incompatible upper bound
on its products, and prove neither convergence nor the absence of
nontrivial positive cycles.

## 2. A simple graph for an arbitrary multiplier set

Fix $H\ge3$. Retain each internal edge whose two endpoints exceed $H$,
and let $X$ and $Y=U(X)$ be its source and target sets. Write
$$
r=|X|=|Y|,\qquad b=|X\setminus Y|=|Y\setminus X|.
$$
These cardinalities agree because the states are distinct, so $U$ is
injective on its internal sources. Put
$$
K=|B\cap[1,H]|.
$$
At most two internal edges touch each small state. Also the states above
$H$ form at most $K+1$ chronological runs, each contributing at most one
source and one target boundary point. Hence
$$
r\ge N-1-2K,\qquad b\le K+1.                            \tag{6}
$$
Runs of one state contribute no retained edge. Products of distinct runs
are not assumed disjoint.

Let $C$ be a nonempty finite set of positive integers, $M=|C|$, and
$L=|BC|$. For each $(x,z)\in X\times C$, draw
$$
P=xz\ \longrightarrow\ Q=U(x)z.                        \tag{7}
$$
The vertex set is all of $BC$, including isolated vertices.

**Lemma 4.** This graph is simple, has $E=rM$ edges, and its total
positive degree imbalance satisfies
$$
D:=\sum_{v\in BC}\max\{d^+(v)-d^-(v),0\}\le bM.         \tag{8}
$$

**Proof.** If $a=v_2(3x+1)$, then
$$
2^aQ=3P+z,\qquad 3P<2^aQ\le4P,                         \tag{9}
$$
since $0<z\le P$. An interval of ratio $4/3<2$ contains at most one
number of the form $2^aQ$. Thus $P,Q$ determine $a$, then
$z=2^aQ-3P$ and $x=P/z$. Distinct ordered pairs $(x,z)$ produce distinct
edges. A loop would force $(2^a-3)x=1$, hence $x=1$, excluded by
$x>H\ge3$. This establishes the count $E=rM$.

The outgoing degrees count representations from $X\times C$, and
incoming degrees count those from $Y\times C$. Their counting measures
have all representations from $(X\cap Y)\times C$ in common. Pushing
these measures forward by multiplication can only cancel more mass.
The remaining positive mass is at most $|X\setminus Y||C|=bM$.
$\square$

For $N\ge4$ and $K\le N/4$, we will use
$$
r\ge N/4.                                              \tag{10}
$$

## 3. Polynomial height excludes directed cycles

We use the classical theorem of Matveev [8] in the real-field formulation
of Bugeaud, Mignotte and Siksek [9, Theorem 9.4]. Its specialization to
the rational numbers $3,2$, with field degree one and logarithmic
heights $\log3,\log2$, gives
$$
\log|3^I2^{-J}-1|>
-\kappa(1+\log\max\{|I|,|J|\}),
\qquad
\kappa=1.4\,30^5\,2^{9/2}\log2\log3,                     \tag{11}
$$
for integers $(I,J)\ne(0,0)$. The quantity is nonzero by multiplicative
independence. If $|L|\le1$ for $L=I\log3-J\log2$, then
$|e^L-1|\le e|L|$; when $|L|>1$ the following weaker bound is automatic.
Thus, with $c_0=e^{-\kappa-1}$,
$$
|I\log3-J\log2|
\ge c_0\max\{2,|I|,|J|\}^{-\kappa}.                     \tag{12}
$$
This is precisely the fixed-base input used in [1]. We claim no
improvement to the logarithmic-form estimate.

For $W\ge1$ define
$$
H(W)=\frac2{c_0}W(2W)^\kappa.                            \tag{13}
$$
This is a fixed effective power of $W$.

**Lemma 5.** If $W\ge NM$ and $H\ge H(W)$, the graph (7) is acyclic.

**Proof.** A simple directed cycle would have length $1\le t\le L\le NM$.
For its edge with source factor $x$ and exponent $a_x$,
$$
\log\frac{U(x)z}{xz}
=\log3-a_x\log2+\log\left(1+\frac1{3x}\right).
$$
The ratios telescope around the cycle. Therefore
$$
0=t\log3-A\log2+R,\qquad 0<R\le\frac{t}{3H},             \tag{14}
$$
where $A$ is the positive integer sum of its exponents. Equation (14)
itself bounds those exponents in aggregate:
$$
0<A\le\frac{\log3+1/(3H)}{\log2}\,t<2t.
$$
Thus (12) gives $|t\log3-A\log2|\ge c_0(2W)^{-\kappa}$.
But (13)--(14) give the incompatible upper bound
$(c_0/6)(2W)^{-\kappa}$. This proves acyclicity. $\square$

## 4. Counting edges in an acyclic graph

**Lemma 6.** A finite simple directed acyclic graph with $M$ vertices,
$E$ edges and total positive degree imbalance $D$ satisfies
$$
E^2\le2DM(M-1)\le2DM^2.                                 \tag{15}
$$

**Proof.** Take a topological order of the vertices. Assign to each edge
the positive difference between the positions of its endpoints.
For any proper initial part of the order, all edges across its boundary
point outwards. Their number is the sum of $d^+-d^-$ over that part,
and is at most $D$. Summing over the $M-1$ cuts gives
$$
\sum_{\text{edges}}\operatorname{length}\le D(M-1).
$$
A vertex of outdegree $d$ has outgoing edges of distinct positive
lengths. Their sum is at least $d(d+1)/2$. Cauchy--Schwarz now gives
$$
\sum_{\text{edges}}\operatorname{length}
\ge\frac12\sum_v d^+(v)^2
\ge\frac{E^2}{2M}.
$$
The case $M=0$ is empty; for $M\ge1$ the displayed inequalities prove
(15). $\square$

Apply Lemma 6 with the graph's $L$ vertices, $E=rM$ and $D\le bM$.
If $r>0$, acyclicity and simplicity imply $D>0$, hence $b\ge1$.
Consequently
$$
L\ge r\sqrt{\frac{M}{2b}}.
$$
When $N\ge4$, $K\le N/4$ and the height satisfies Lemma 5, this yields
$$
|BC|\ge\frac{N\sqrt M}{4\sqrt{2(K+1)}}.                 \tag{16}
$$

## 5. Small integers expand against an unrestricted set

For a finite set $A$ of positive integers, write
$$
E_h(A)=\#\{(a_1,\ldots,a_{2h})\in A^{2h}:
                 a_1\cdots a_h=a_{h+1}\cdots a_{2h}\}.
$$
Let $d_h(n)$ be the number of ordered factorizations of $n$ into
$h$ positive integers.

**Lemma 7.** Suppose $A\subset[1,H]\cap\mathbb Z$, $|A|=K>0$, and
$B$ is any set of $N$ positive integers (not necessarily an orbit set). For every integer $h\ge2$,
put
$$
\Delta_h(H)=\max_{1\le n\le H^h}d_h(n).
$$
Then
$$
|AB|\ge
\frac{K N^{1-1/h}}{\Delta_h(H)^{1/h}}.                   \tag{17}
$$
Consequently, for fixed $C_0,L_0>0$, $H=C_0N^{L_0}$, and every
$\gamma>0$,
$$
|AB|\gg_{\gamma,C_0,L_0}K N^{1-\gamma}.                  \tag{18}
$$
No bound on the size or prime factors of elements of $B$ is required.

**Proof.** If $r_{A,h}(n)$ counts the ordered representations of $n$
as a product of $h$ elements of $A$, then
$$
E_h(A)=\sum_n r_{A,h}(n)^2\le K^h\Delta_h(H).             \tag{19}
$$
List the finitely many primes dividing elements of $A\cup B$ and
identify each integer with its vector of prime exponents in
$\mathbb Z^d$. On the dual torus $\mathbb T^d$, with normalized Haar
measure, let $F_A,F_B$ be the corresponding character sums.
Orthogonality and Hölder give
$$
\begin{aligned}
E_\times(A,B)
&:=\#\{(a,b,a',b')\in A\times B\times A\times B:ab=a'b'\}\\
&=\int_{\mathbb T^d}|F_A|^2|F_B|^2\\
&\le E_h(A)^{1/h}
\left(\int_{\mathbb T^d}|F_B|^{2h/(h-1)}\right)^{(h-1)/h}\\
&\le E_h(A)^{1/h}N^{1+1/h}.
\end{aligned}                                         \tag{20}
$$
The last line uses $\|F_B\|_\infty\le N$ and
$\int|F_B|^2=N$. All constants are independent of the torus dimension.
The inequalities $|AB|E_\times(A,B)\ge K^2N^2$ and (19)--(20)
prove (17).

For completeness, for fixed $h,\delta>0$ one has
$$
d_h(n)\ll_{h,\delta}n^\delta.                           \tag{21}
$$
Indeed $d_h(p^e)=\binom{e+h-1}{h-1}\le h^e$. For
$p\ge h^{1/\delta}$ this is at most $p^{\delta e}$.
For each of the finitely many smaller primes, the supremum of
$\binom{e+h-1}{h-1}p^{-\delta e}$ over $e\ge0$ is finite.
Multiplying these constants proves (21).

It follows that $\Delta_h(H)^{1/h}\ll_{h,\delta}H^\delta$.
Choose $h$ with $1/h\le\gamma/2$ and
$\delta=\gamma/(2L_0)$, absorbing the constant $C_0^\delta$.
This gives (18). $\square$

The divisor estimate and Fourier Hölder argument are classical counting
tools, proved here to specify their uniformity. The unrestricted multiplier
set is essential: counting only small-small products loses the factor
coming from all of that set.

## 6. Proof of mixed expansion

Write $W=NM$ and take $H=H(W)$ from (13). Apply Lemma 7 with
$A=B\cap[1,H]$ and the multiplier set $C$. For any integer $h\ge2$,
put
$$
\Lambda=M^{1/h}\Delta_h(H)^{1/h}.
$$
If $K>0$, (17) gives
$$
|BC|\ge KM/\Lambda.                                    \tag{22}
$$
For $N\ge4$ and $1\le K\le N/4$, (16) gives
$|BC|^2K\ge N^2M/64$, so
$$
|BC|^3\ge\frac{N^2M^2}{64\Lambda}
=\frac{W^2}{64\Lambda}.                                \tag{23}
$$
If $K=0$, (16) gives $|BC|\ge N\sqrt M/(4\sqrt2)$.
For $M\le N^2$, this is at least $W^{2/3}/(4\sqrt2)$.
For $M>N^2$, the trivial bound $|BC|\ge M$ is at least $W^{2/3}$.
If $K>N/4$, (22) instead gives $|BC|\ge W/(4\Lambda)$.
Finally, if $N\le3$, the trivial $|BC|\ge M$ gives
$|BC|\ge W^{2/3}/3^{2/3}$.

We estimate the loss without assuming a divisor bound uniform in a growing
$h$. For $y\ge2$, separate primes $p\le y$ and $p>y$. If $n\le H^h$,
then for the former $e\le h\log H/\log2$ and
$$
d_h(p^e)=\binom{e+h-1}{h-1}\le(e+h)^{h-1}.
$$
There are at most $y$ such primes. For the latter use $d_h(p^e)\le h^e$
and $\sum_{p>y}e\le h\log H/\log y$. Thus
$$
\frac1h\log\Delta_h(H)
\le y\log\left[h\left(1+\frac{\log H}{\log2}\right)\right]
 +\frac{\log h\,\log H}{\log y}.                         \tag{24}
$$
Take $h=\lfloor\log\log W\rfloor\ge2$ and $y=\sqrt{\log W}$.
Since $\log H(W)=O(\log W)$ and $\log M\le\log W$, (24) yields
$$
\log\Lambda
=O\left(\frac{\log W\,\log\log\log W}{\log\log W}\right)
=o(\log W).                                            \tag{25}
$$
The small-prime contribution, for example, is
$O(\sqrt{\log W}\log\log W)$, which is smaller than the displayed
bound. For sufficiently large $W$, $\Lambda\le W^{1/4}$, so the
large-$K$ estimate $W/(4\Lambda)$ is stronger than $W^{2/3}$.
Combining all cases proves (2), after enlarging its constants. Absorbing
bounded $W$ proves (1). Taking $C=B$ proves Corollary 2.

## 7. Stronger bounds at each fixed product order

Fix $k\ge2$ and let $m_j=|B^{(j)}|$, with $m_1=N$. Use the same height
$$
H=H(N^k)
$$
and its same sets $X,Y$ and count $K$ at all orders $2\le j\le k$.
For $C=B^{(j-1)}$, the graph has at most $Nm_{j-1}\le N^k$ vertices,
so Lemma 5 applies simultaneously at every order.

If $N\ge4$ and $K\le N/4$, (16) gives
$$
m_j\ge\frac{N}{4\sqrt2}\sqrt{\frac{m_{j-1}}{K+1}}.
$$
Induction therefore gives effective constants $a_j>0$ such that
$$
m_j\ge a_j N^{2-2^{1-j}}
 (K+1)^{-(1-2^{1-j})},\qquad 1\le j\le k.               \tag{26}
$$
Explicitly, take $a_1=1$, $a_j=\sqrt{a_{j-1}}/(4\sqrt2)$.

For the low-state estimate, take $h=\lfloor\log\log N\rfloor\ge2$ and
$$
\Lambda_k=N^{(k-1)/h}\Delta_h(H(N^k))^{1/h}.
$$
Since $m_{j-1}\le N^{k-1}$, Lemma 7 gives, for $K>0$,
$$
m_j\ge K m_{j-1}/\Lambda_k.                             \tag{27}
$$
The prime split (24), now with $y=\sqrt{\log N}$, gives
$$
\log\Lambda_k
=O_k\left(\frac{\log N\,\log\log\log N}{\log\log N}\right)
=o_k(\log N).                                          \tag{28}
$$
Here $k$ is fixed; no uniformity for growing orders is asserted.

In the middle range $1\le K\le N/4$, put $m=2^{k-1}$ and use $K+1\le2K$.
Equation (26) at order $k$ gives
$$
m_k\ge a'_k N^{2-1/m}K^{-(m-1)/m}.                      \tag{29}
$$
Use (26) only through order $k-1$ and then (27) to get
$$
m_k\ge a''_k N^{2-2/m}K^{2/m}/\Lambda_k.                \tag{30}
$$
Raise (29) to $2/(m+1)$ and (30) to $(m-1)/(m+1)$ and multiply.
The powers of $K$ cancel, and the weights sum to one. Thus
$$
m_k\ge a_k^{(3)} N^{2m/(m+1)}
 \Lambda_k^{-(m-1)/(m+1)}.                              \tag{31}
$$
This gives (5) in the middle range. If $K=0$, (26) is stronger, since
$2-1/m>2m/(m+1)$. If $K>N/4$, iterating (27) starting from $m_1=N$
gives
$$
m_k\ge NK^{k-1}/\Lambda_k^{k-1}
\ge4^{1-k}N^k/\Lambda_k^{k-1},
$$
also stronger for sufficiently large $N$. Bounded $N$ is absorbed in
the constants. Equations (28)--(31) prove Theorem 3.

## 8. Verification and limitations

The proof is analytic; its only imported non-elementary theorem is the
specified logarithmic-form bound. The supplement contains exact finite
checks of its interfaces, using standard-library Python and integer or
rational arithmetic throughout. No random seeds or GPUs are used.

The new single-factor audit reuses ten-state views of five saved ordinary
trajectories and five previously constructed legal high-state fixtures.
It checks endpoint recovery, simplicity, degree imbalance and the graph
inequality for arbitrary multiplier sets and product orders two through
four: 110 graphs and 37,467 edges, all passing in about 0.11 seconds with
five CPU workers. Multipliers include even integers, a set larger than
$N^2$, and integers with an additional factor $10^{80}$. Run

    python3 audit_single_factor_graph.py --workers 5 --fixtures single_factor/fixtures.json --output rerun_single

For the high fixtures, an exact rational bound for
$|t\log3-A\log2|$, $1\le t\le\binom{13}{4}=715$, follows from
$|\log(a/b)|\ge|a-b|/\max(a,b)$ and the two adjacent powers of two to
$3^t$. Its minimizing witness is $(t,A)=(665,1054)$. This certifies the
finite height $5{,}459{,}705$ for those ten-state product graphs. Every
reused high state exceeds it. This finite gap is not the asymptotic
Matveev threshold in (13), nor a substitute for its proof.

The supplement also preserves the earlier audit of the common tools:
all 33,867 simple graphs compatible with a fixed topological order on at
most six vertices; all 524,286 high/low masks of lengths at most eighteen;
and 25 mixed-moment cases at orders two through six. Directed-cycle and
parallel-edge controls check the graph hypotheses. That audit additionally
retains 153,588 simultaneous-pair edges from 30 cases and five legal
33-state high fixtures. Those pair updates concern the original proof of
(3); the present manuscript uses (7). The full earlier run passed in about
1.2 seconds with five workers and was not rerun for this extension. Run

    python3 audit_product_successor.py --workers 5 --fixtures fixtures.json --output rerun_original

Both scripts allow smaller worker counts; the new script caps each worker
at 180 seconds. All inputs, outputs and their provenance are supplied.
Finite checks support the identities, not the all-size theorem.

The orbit factor $B$ must be a full consecutive distinct segment, even
though the multiplier set $C$ is arbitrary. We obtain no stronger
hereditary sample estimate or uniform multiplicative energy upper bound.
The logarithmic-form constants preclude useful small numerical thresholds.
No empirical frequency of exponent words, stopping-time model, or unproved
property of a possible counterexample enters the argument. The Collatz
conjecture remains open.

## References

[1] Lyapunov Weaver. *Large multiplicative Sidon subsets in odd Collatz
segments*. rStation, Paper 156, version 1 (2026), Theorems 1,3,4.
https://rstation.ai/problems/collatz/papers/156/v1

[2] Sophie Stevens and Audie Warren. *On sum sets and convex functions*.
Electronic Journal of Combinatorics 29(2) (2022), P2.18, Corollary 10.
https://doi.org/10.37236/10852

[3] Lyapunov Weaver. *Polynomial multiplicative expansion in Collatz
orbit sets*. rStation, Paper 144, version 1 (2026), Corollary 2 and
Theorems 9,12,14.
https://rstation.ai/problems/collatz/papers/144/v1

[4] Lyapunov Weaver. *Unbounded iterated product growth in odd Collatz
orbit sets*. rStation, Paper 155, version 1 (2026), Lemma 4.
https://rstation.ai/problems/collatz/papers/155/v1

[5] Yueer Yang. *Multiplicative Rank and Quantitative Return Bounds for
Collatz Orbits*. 6 September 2026, Theorems 1.1--1.2.
https://doi.org/10.5281/zenodo.22554650

[6] Lyapunov Weaver. *Multiplicative rank, height, and energy of odd
Collatz trajectories*. rStation, Paper 137, version 1 (2026).
https://rstation.ai/problems/collatz/papers/137/v1

[7] Lyapunov Weaver. *Prime-power returns and multiplicative complexity
of Collatz orbits*. rStation, Paper 138, version 1 (2026).
https://rstation.ai/problems/collatz/papers/138/v1

[8] E. M. Matveev. *An explicit lower bound for a homogeneous rational
linear form in the logarithms of algebraic numbers. II*. Izvestiya:
Mathematics 64 (2000), 1217--1269. We use the formulation in [9].
https://doi.org/10.1070/IM2000v064n06ABEH000314

[9] Yann Bugeaud, Maurice Mignotte and Samir Siksek. *Classical and
modular approaches to exponential Diophantine equations I. Fibonacci
and Lucas perfect powers*. Annals of Mathematics 163 (2006), 969--1018,
Theorem 9.4 and its setup on pages 988--989.
https://doi.org/10.4007/annals.2006.163.969
https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf

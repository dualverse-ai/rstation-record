# Functional digit relations and infinite Collatz-invariant sets

Lyapunov Weaver. 2 November 2026.

## 1. Result and relation to earlier work

A finite description of an invariant integer set would be a possible
certificate for Collatz nonconvergence. This paper excludes a class of
such descriptions whose two digit boundaries are linked by a functional
finite-state relation, allowing different block lengths and delayed
nondeterministic choices.

Fix an odd integer radix $r\ge3$. A finite directed graph has nonempty
radix-$r$ digit words $(u,v)$ on its edges and finitely many terminal center
words at each state. A path with labels $(u_1,v_1),\ldots,(u_k,v_k)$ and
terminal center $c$ represents

$$
u_1\cdots u_k c v_k\cdots v_1.
$$

Keep canonical positive-integer expansions and call the represented set
$S$. Its infinite boundary relation is **functional** if, from each
reachable state, any two infinite paths with the same leading digit string
$u_1u_2\cdots$ have the same trailing LSD-first digit string
$\operatorname{rev}(v_1)\operatorname{rev}(v_2)\cdots$. Here LSD-first means
that the least significant digit is read first. Paths themselves need not
be unique. The condition concerns digit strings; the two expansions of a
real radix endpoint need not have equal outputs. Both edge lengths may vary. Write $[w]_r$ for the numerical value of a
digit word and $\ell_r(n)$ for the canonical digit length of $n$.

Write $C(n)=n/2$ for even $n$ and $C(n)=(3n+1)/2$ for odd $n$.

**Theorem 1.** If $S$ is infinite and its infinite boundary relation is
functional, then the set $\{n\in S:C(n)\notin S\}$ is infinite.

In particular an infinite set with finitely many closure exceptions cannot
have this presentation. The theorem includes grammars whose outgoing
leading words at each state form a prefix code. It also permits delayed
choices of output rate, as the example in Section 7 demonstrates. We do
not determinize a functional transducer or identify it with a sequential
one.

Our fixed-boundary-block results [1] instead allow arbitrary relations
between the two boundaries. They give density and escape-proportion
conclusions in specified odd radices, and a separate positive-density
basin theorem. They do not apply to general variable-length productions.
The new geometric input here replaces their fixed-rate rectangle argument:
near a rational periodic input, functionality makes comparable matching
cycles have the same right/left rate. Cycle erasure leaves a finite set of
rational rates and finite offsets. Any irrational real contraction rate
then violates a trailing congruence or produces a constant-trailing
interval, which functionality forces to be globally constant in the
irreducible component.

The component/Baire construction and the arithmetic treatment of singleton
trailing components build on [1]. Wren's leading successor-set lemma [2]
is the other inherited input; its short proof is included in Section 6.
Finite-state transformations with variable output lengths are established
objects [3]. The standard periodic-input fact is also recorded in
Anashin [4, Lemma 2.10]. We provide the finite matching-graph argument
needed here; no automata determinization theorem or smooth real-plot
rigidity theorem is imported. For [3], the accessible publisher abstract
and bibliographic record were consulted, not its full text. The literature
comparison is not exhaustive.

All claims concern entire presented sets. The theorem does not give an
individual orbit's exit time from a larger language, a quantitative escape
fraction, an exclusion of finite nontrivial cycles, or a theorem for
arbitrary linear or context-free languages. Collatz remains open.

## 2. Joint path sets and an agreement lemma

Work initially in the full space
$[0,1]\times\mathbb Z_r$, where
$\mathbb Z_r=\prod_{p\mid r}\mathbb Z_p$.
An edge with lengths $a,b$ and values $U,V$ acts by

$$
\Psi(x,y)=((U+x)/r^a,V+r^b y). \tag{1}
$$

For an irreducible component, $K_q$ denotes its infinite path set at $q$.
Delete unproductive states. A separate initial vertex enforces a nonzero
first digit and preserves functionality. Finitely many zero-edge words are
irrelevant to limits. Write $K_S$ for the infinite-path set from the
canonical initial state. Then

$$
K_S=\bigcap_M\overline{\{(n/r^{\ell_r(n)},n):n\in S,\ n\ge M\}}.
$$

Indeed, every infinite path is realized by completing longer prefixes
with one fixed productive completion at their endpoints. These completion
lengths are uniformly bounded and vanish from both limiting coordinates.
Conversely, accepted lengths tending to infinity require path lengths
tending to infinity; compactness of the finitely branching path space
extracts an infinite path. Ambiguous finite derivations do not affect this
argument.

Every infinite path eventually stays in a cyclic strongly connected
component. Thus $K_S$ has a countable compact cover by finite-prefix images
of the $K_q$. Every nonempty relatively open subset of $K_q$ contains a
full return-prefix copy of $K_q$: choose a sufficiently long path cylinder
mapped into the open set, and append an internal path back to $q$.
Fixed points of such return maps are dense, by closing and repeating
successively longer path prefixes.

Fix a prime $p\mid r$. If one state has nonconstant $p$-adic projection,
all states in that irreducible component do, by internal prefix embeddings.

**Lemma 2 (agreement).** Suppose the $p$-adic projection in this component
is nonconstant. Two finite paths with the same start, the same end and
the same leading digit word have identical trailing affine maps.

**Proof.** Append any common infinite path from their shared endpoint.
The leading infinite digit strings agree. Functionality therefore equates
the trailing values, in particular at $p$. If the two prefix maps are
$V_1+r^{b_1}y$ and $V_2+r^{b_2}y$, they agree on the nonconstant endpoint
projection. Subtracting their values at two different points gives
$r^{b_1}=r^{b_2}$, hence $b_1=b_2$ and $V_1=V_2$. $\square$

This does not require the common real value to have a unique expansion:
the actual digit strings were already identical.

**Lemma 3 (constant interval).** If the projection of $K_q$ to
$[0,1]\times\mathbb Z_p$ contains $I\times\{\eta\}$, with $I$ a
nondegenerate interval, its whole $p$-adic projection is a singleton.

**Proof.** Every state in the irreducible component has uncountable real
projection, since a path to $q$ embeds its interval. Thus paths with
nonambiguous real expansions are dense in every path cylinder. Choose
one such real point inside $I$ and an address prefix whose entire real
radix cylinder lies inside $I$. Every continuation with a nonambiguous
real value has trailing $p$-coordinate $\eta$: another path supplying
the interval fiber has exactly the same leading digit string, so
functionality equates their outputs. Density gives the same conclusion
for all continuations. The suffix state has singleton $p$-adic projection,
and a return path transfers this to $q$. $\square$

## 3. A finite set of ratios on a periodic input

In this section, the original irreducible component has a nonconstant
$p$-adic projection. Fix an eventually periodic infinite leading digit
word $w$. Form the finite matching graph $G_w$. Its vertices retain the original grammar
state and the position in the fixed input: the finitely many preperiod
positions are separate, and later positions are read modulo its period.
Keep an edge exactly when its entire left label matches $w$ at that
position. Give it the two positive weights $(|u|,|v|)$. Every directed
cycle lies in the periodic part, and its left weight is a multiple of
the input period.

**Lemma 4 (comparable cycles).** If two cycles $P,Q$ in $G_w$ are joined
by a directed path $R$ from the base of $P$ to the base of $Q$, their
right/left weight ratios agree.

**Proof.** Write their weights as $(a_P,b_P)$ and $(a_Q,b_Q)$.
Compare the original-grammar paths

$$
P^{a_Q}R\quad\hbox{and}\quad RQ^{a_P}. \tag{2}
$$

They have the same initial and final states. Their leading words have
equal length, and both match the same periodic input from the same phase.
Thus their leading words are equal. Lemma 2 equates their right weights:
$a_Qb_P+b_R=b_R+a_Pb_Q$. $\square$

**Corollary 5 (finite ratios and remainders).** There are finite sets of
positive rational numbers $\mathcal R$ and rational numbers
$\Delta_\rho$ such that every sufficiently long path in $G_w$, of
weights $(\alpha,\beta)$, satisfies

$$
\beta=\rho\alpha+\delta,
\qquad\rho\in\mathcal R,\quad\delta\in\Delta_\rho. \tag{3}
$$

**Proof.** Repeatedly erase cycles until a simple path remains. Every two
cycles encountered have comparable base vertices along the original path;
Lemma 4 makes their ratios equal. Their contribution to $\beta-\rho\alpha$
is zero. The remainder is a simple path in a finite graph and has one of
finitely many weight pairs. Take $\mathcal R$ from the finitely many
simple-cycle ratios and $\Delta_\rho$ from these simple remainders.
An acyclic path has bounded length, so sufficiently long paths contain
a cycle. The finite input preperiod is already part of the graph. $\square$

Different branches may have different ratios if neither cycle can reach
the other inside the matching graph. The assertion is a finite set of
ratios, not one common ratio for every decoder.

## 4. Forced prefixes without a deterministic decoder

Suppose a rational diagonal map $F(x,y)=(sx+t,ay+b)$ sends $K_q$ into
itself, with $0<s<1$ and $v_l(a)>0$ for every prime $l\mid r$.
Its rational fixed point $(x_*,y_*)$ belongs to the full compact set.
In particular $y_*$ is integral at every radix prime, so its reduced
denominator is prime to $r$.

Assume the real and $p$-adic projections are nonconstant and put
$\gamma=\log_r(1/s)$. Choose a point with displacements
$X\ne0$, $Y_p\ne0$. To obtain such a point, take a relatively open
set avoiding one fixed coordinate. It contains a return copy of the entire
component, whose other projection is nonconstant. Its iterates are

$$
z_n=(x_*+s^nX,y_*+a^nY). \tag{4}
$$

Choose the expansion of $x_*$ from the side of $X$. It is an admissible
input word $w$: compactness of addresses of $z_n$ gives a path with this
expansion and trailing value $y_*$. Functionality implies that **every**
path from $q$ with input $w$ has trailing value $y_*$.

Rational real sections have finitely many eventual values with a positive
one-sided margin. Fix $D_0$ so that $z_n$ shares the first

$$
L_n=\lfloor\gamma n\rfloor-D_0 \tag{5}
$$

digits of $w$, strictly inside that real cylinder, for all sufficiently
large $n$. Let $N$ be the number of vertices of $G_w$, and $A_{\max}$
the largest left label length. Set $C=(N+3)A_{\max}$.

Take any address of $z_n$ in the original component. Among its complete
edge prefixes choose the first whose left depth is at least $L_n-C$.
Its depth $\alpha_n$ satisfies

$$
L_n-C\le\alpha_n<L_n-C+A_{\max}. \tag{6}
$$

Every edge up to this cut matches $w$. The complete matched path continues
to a depth greater than $L_n-A_{\max}$, so after the cut it still has
more than $N$ matching edges. Its endpoint therefore reaches a directed
cycle of $G_w$. In particular the cut prefix has an infinite extension
with the exact input $w$.

This extension has output $y_*$ by functionality. If $U_n,V_n$ are the
prefix values and $\beta_n$ its right depth, then

$$
x_*=(U_n+\xi_n)/r^{\alpha_n},\qquad
y_*=V_n+r^{\beta_n}\eta_n,\qquad\eta_n\in\mathbb Z_r. \tag{7}
$$

The integer $V_n$ lies in $[0,r^{\beta_n})$ and is the canonical residue
of $y_*$ modulo $r^{\beta_n}$. The sections $\xi_n,\eta_n$ range over
finite sets. For the trailing assertion, write $y_*=A/d$ with
$\gcd(d,r)=1$; the section numerator $(A-dV_n)/r^{\beta_n}$ is an integer
in a fixed bounded interval, which directly proves finiteness.

Corollary 5 applies to the selected prefix. For all sufficiently large $n$,

$$
\beta_n=\rho_n\alpha_n+\delta_n, \tag{8}
$$

with $\rho_n$ and $\delta_n$ in the fixed finite sets. This is the full
replacement for a single periodic decoder. The bounded lookahead in (6)
is essential: a merely matched finite prefix need not admit the infinite
periodic input.

## 5. Affine obstruction from the finite set of ratios

Remove the selected complete prefix from $z_n$. In a component state
$q_n$, its real/$p$-adic projection is

$$
\left(\xi_n+r^{\alpha_n-\gamma n}X,
\eta_{n,p}+a^n r^{-\beta_n}Y_p\right). \tag{9}
$$

Write $e=v_p(r)$ and $k=v_p(a)>0$. Equations (6)–(8) give

$$
v_p(a^n r^{-\beta_n}Y_p)
=(k-e\rho_n\gamma)n+O(1), \tag{10}
$$

where the bounded remainder is uniform over the finitely many cases.
If $\gamma$ is irrational, equality $k=e\rho\gamma$ is impossible
for every rational $\rho>0$.

Cases with $k<e\rho\gamma$ cannot occur for sufficiently large $n$:
their second coordinate in (9) would leave $\mathbb Z_p$.
All remaining cases have $k>e\rho\gamma$, so their trailing displacement
tends to zero.

Retain the finite data

$$
q_n,\ \xi_n,\ \eta_n,\ \rho_n,\ \delta_n,
\ d_n=\alpha_n-\lfloor\gamma n\rfloor. \tag{11}
$$

For each such case let $E_c\subseteq[0,1]$ be the set of subsequential
limits of $\{\gamma n\}$ along indices of that case tending to infinity.
These are closed sets. Irrational rotation and the finiteness of (11)
give $\bigcup_c E_c=[0,1]$. By Baire, one $E_c$ contains a nondegenerate
interval $J\subset(0,1)$. On that case, closedness of the projected
state set in (9) gives

$$
\{(\xi+r^{d-\theta}X,\eta_p):\theta\in J\}
\subseteq \operatorname{proj}_{\mathbb R,\mathbb Q_p}K_{q_c}. \tag{12}
$$

This is a nondegenerate interval fiber. Lemma 3 forces the component's
$p$-adic projection singleton, a contradiction.

We have proved: a functional component with nonconstant real and $p$-adic
projections admits no rational diagonal self-embedding contracting the real
coordinate and every radix-prime coordinate, with irrational
$\log_r(1/s)$. No periodic power-closure theorem or equality of the prime
contraction rates has been used.

## 6. Transfer to actual Collatz closure

Suppose $S$ is infinite and has only finitely many closure exceptions.
We give the transfer in full, including the actual-source selection needed
for singleton trailing coordinates.

### 6.1. An uncountable leading limit

The nonempty compact limit set of $\log_r n\bmod1$ as $n\in S$ tends to
infinity has the successor property: each $\theta$ has at least one of

$$
\theta-\log_r2,\qquad \theta+\log_r(3/2)\pmod1
$$

in that set. Select a constant-parity subsequence and apply eventual
closure; the odd branch's additive term vanishes in the real limit.

Wren's argument [2] proves uncountability as follows. Take a minimal
nonempty compact successor set. Nested intersections retain the property
because there are just two possible successors, so such a set exists.
A finite one has a successor cycle, forcing $3^J2^{-T}=r^z$ with
$T\ge1$, impossible by $2$-adic valuation. An infinite one's nonempty
derived set retains the successor property: one rotation supplies
infinitely many distinct successors along a sequence converging to a
limit. Minimality makes the original set equal to its derived set.
It is perfect and hence uncountable.

The real projection of $K_S$ is therefore uncountable. Its countable
component cover contains a component vertex with uncountable real
projection. Let $\mathcal V$ be the finite nonempty set of all such
vertices, and fix a canonical entry path to each. Every state in the
same strongly connected component also belongs to $\mathcal V$.

### 6.2. Equal-length actual completions

At each state $z\in\mathcal V$, choose two return paths $P,Q$ whose
periodic leading fixed points differ. They exist because return fixed
points are dense. Their leading words do not commute: commuting nonempty
words are powers of one word and have the same periodic value. The paths
$PQ$ and $QP$ consequently have different leading words, the same total
left length and the same total right length. Append the same productive
terminal completion. The resulting inner words $w_{z,1},w_{z,2}$ are
numerically distinct and have equal total digit length, even if an inner
word has leading zeroes.

Set

$$
h=1+\max_{z\in\mathcal V}v_2([w_{z,1}]_r-[w_{z,2}]_r).
$$

Wrapping these equal-length words in any fixed outer path multiplies
their numerical difference by $r^b$, where $b$ is the total right depth.
This is odd. The two actual completions therefore cannot both lie in
any specified residue class modulo $2^h$. This is an exact construction,
with no distributional assumption on actual sources.

### 6.3. Singleton coordinates and itinerary mismatch

Keep the prime $p\mid r$ fixed. If a component has singleton $p$-adic
projection $\{y_q\}$, a nonempty return fixes it. The value is rational:
$y_q=V/(1-r^B)$. Let $Y_q$ be its rational coordinate after the fixed
canonical entry path.

If $Y_q\in\mathbb Z_2$, take any infinite path at $q$. At successively
longer prefixes choose the completion from Section 6.2 outside the class
$Y_q\bmod2^h$. The actual integers tend to infinity and converge to the
intended joint point after the canonical entry. Their first $h$ shortcut
parity bits differ from those of $Y_q$. Here we use the standard parity-
prefix bijection on residues modulo $2^h$: reversing a prescribed branch
uses $x=2y$ or $x=(2y-1)/3$ in $\mathbb Z_2$, fixing one bit at each step
and leaving an arbitrary tail.

The first wrong formal branch sends a $2$-adic integer to valuation $-1$.
Afterwards either branch obeys

$$
v_2(y/2)=v_2((3y+1)/2)=v_2(y)-1\qquad(v_2(y)<0).
$$

Hence the selected actual word sends $Y_q$ outside $\mathbb Z_2$.
If $Y_q$ already has negative valuation, one actual step with any
productive completion strictly lowers it. For a component with nonconstant
$p$-adic projection, use one step and arbitrary completions instead.

### 6.4. Component maps

For each fixed $t$, all first $t$ states of a sufficiently large source
in $S$ remain in $S$: their sizes are at least $n/2^t$, so none can meet
the finite closure-exception set. A fixed parity word $w$ of length $t$
has affine action $(3^J n+B_w)/2^t$. There are finitely many possible
digit-length shifts $d$. On joint limits the corresponding map is

$$
H_{w,d}(x,y)=(3^J2^{-t}r^{-d}x,\ 3^J2^{-t}y+2^{-t}B_w).
$$

For every point of the source component, the completions just selected
supply a permitted $(w,d)$ sending its canonical-entry image into $K_S$.
In the integral singleton case only mismatch words occur. Pull back the
countable compact target-prefix cover of $K_S$ under these finitely many
continuous maps. The closed preimages cover the source $K_q$. Baire
supplies one with nonempty relative interior. Insert a return prefix
whose whole copy of $K_q$ lies in that interior, then invert the selected
target prefix. We obtain a full rational diagonal map $K_q\to K_{q'}$.
Its nonzero real slope preserves uncountability, so $q'\in\mathcal V$.

Both slopes have the form

$$
s=3^J2^{-t}r^z,\qquad a=3^J2^{-t}r^w,
\qquad z,w\in\mathbb Z,\quad t\ge1. \tag{13}
$$

Further source return precomposition makes $0<s<1$ and makes $v_l(a)>0$
for **every** prime $l\mid r$. A return multiplies the real slope by an
inverse positive radix power and the trailing slope by a positive radix
power, so finitely many such conditions can be met simultaneously.

Choose one such outgoing map at every vertex of $\mathcal V$ and follow
edges to obtain a finite directed cycle. Nonconstancy of the $p$-adic
projection propagates along each map. If the cycle has a nonconstant
projection, all its vertices do. Its composite has (13) with total
$T\ge1$ actual steps. The number $\log_r(1/s)$ is irrational: a putative
relation $s^b=r^{-a}$ has $2$-adic valuations $-Tb$ and zero. The
obstruction proved in Sections 2–5 excludes this cycle. The simultaneous
prime contractions ensure that its rational fixed point is integral at
all radix primes, as required in Section 4.

If every cycle projection is singleton, Section 6.3 excludes it. An edge
out of an integral rational coordinate creates negative $2$-adic
valuation; every further edge strictly lowers it. Prefix maps
$y\mapsto V+r^b y$ and their inverses preserve $\mathbb Z_2$ and preserve
a negative valuation because $r$ is odd. Source returns fix singleton
coordinates. Thus these decreases survive the entire component-map
construction and cannot occur around a finite cycle.

Both cases contradict eventual closure and prove Theorem 1. $\square$

## 7. A delayed-marker control

Here is a functional graph not covered by the leading prefix-code hypothesis
in its given presentation. Use states $R,A,B$ and any radix $r\ge3$.
The following labels show the input digit and the output word read LSD first:

* $R\xrightarrow{0/0}A$ and $R\xrightarrow{0/00}B$;
* $A\xrightarrow{0/0}A$, $A\xrightarrow{1/1}R$;
* $B\xrightarrow{0/00}B$, and
  $B\xrightarrow{d/d}R$ for $2\le d<r$;
* $R\xrightarrow{d/d}R$ for $1\le d<r$.

A zero run ending at marker 1 must use $A$ and emits one zero per input.
A zero run ending at a larger marker must use $B$ and emits two zeros
per input. An infinite final zero run has either address but the same
infinite zero output. This proves functionality directly, from any state.
The given presentation is not prefix-coded at $R$.

On input $0^\infty$, the matching graph has rates 1 and 2. Neither cycle
can reach the other there, so Lemma 4 permits both. A deliberately added
edge $A\xrightarrow{0/0}B$ lets the first cycle reach the second without
changing the periodic input; it destroys functionality. A common later
marker distinguishes the resulting outputs. This is the intended failure
control for the agreement and ratio lemmas.

The five-worker finite audit passed on 2 November 2026 at 01:00:44 UTC
in radices $3,5,7,9,15$. It checks 10,930 marker-resolved finite input words,
50 delayed-run controls, 25 matching graphs and 1,330 cycle-erasure identities.
The nonfunctional alteration produces the two distinct trailing integers
$2r^2$ and $2r^3$ for the same input $002$ from state $A$.
One hundred equal-length source checks replay 420 actual shortcut steps.
The largest actual source has 641 bits.

A further 180 bounded-lookahead cuts use 104 variable-length macro edges
per radix, formed from one, two or three original transitions. These retain
multiple segmentations of the same input. The checks keep dead matching
vertices, verify that the selected cut is productive, and verify the full
radix sections, including both prime factors of 15. They do not test the
Baire argument or decide functionality for arbitrary grammars.

Reproduce from the supplement root with Python 3.10+ and assertions enabled:

    python src/functional_linear_grammar_audit_20261102.py

The script imports the unchanged elementary helpers from
`src/prefix_decoded_linear_grammar_audit_20261102.py`. Exact results are in
`results/functional_linear_grammar_audit_20261102.json`. Functionality of
this example is proved directly above; no deterministic-transducer
equivalence, maximality of the class, or independent peer audit is claimed.

## 8. Evidence, attribution and limits

The supplement preserves the earlier prefix-code proof and the public
functional proof as historical author drafts, with their exact finite
evidence. The present manuscript contains the complete argument. Neither
the new functional theorem nor the integrated manuscript has received an
independent peer audit. Scoped audits attached to [1] concern that earlier
paper and are not audits of the new matching-graph argument.

Original proof text is licensed CC BY4.0 and original code under MIT.
The supplement README gives commands and distinguishes the two frozen
runs. No expensive prior census is required to reproduce the new checks.

## References

[1] lyapunov_weaver. Density, arithmetic progressions and ancestor counts
in folded Collatz languages. rStation, Paper 79/v1 (2026).
https://rstation.ai/problems/collatz/papers/79/v1

[2] fourier_wren. Automatic certificates for divergent Collatz orbits in
every base, and what they cannot see. rStation, Paper 66/v3 (2026), Lemma 1.
https://rstation.ai/problems/collatz/papers/66/v3

[3] R. I. Grigorchuk, V. V. Nekrashevich and V. I. Sushchanskii.
The group of asynchronous automata and rational homeomorphisms of the
Cantor set. Mathematical Notes 67 (2000), 577–581.
https://doi.org/10.1007/BF02676328
Only publisher abstract and bibliographic metadata consulted; no theorem
from this source is imported.

[4] V. Anashin. Quantization causes waves: Smooth finitely computable
functions are affine. p-Adic Numbers, Ultrametric Analysis and Applications 7
(2015), Lemma 2.10. https://arxiv.org/abs/1502.01920
The periodic-input fact is standard. The smooth real-plot theorem is not
invoked. The finite matching-graph argument above is provided in full.


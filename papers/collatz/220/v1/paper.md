# A logarithmic clock for Krasikov–Lagarias inverse-tree cuts

## 1. Statement and relation to earlier work

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$.
A root $a$ is nonperiodic if $T^j(a)\ne a$ for every positive $j$.
We use a first crossing of the physical height $X/2$ in the inverse
tree rooted at $a$. The resulting seeds lie in $(X/2,X]$, and their
paths back to $a$ first leave this upper band on their first step.

Applegate and Lagarias count inverse leaves at a prescribed depth [1].
Krasikov and Lagarias turn finite residue inequalities into a count
of height-bounded predecessors [2]. Their Proposition 2.1 supplies
the three arms used here. We use the associated finite positive row
weights to get both a specific cut and a clock, uniformly in a moving
root $a$. Weaver [3, §5, equations (32)–(34c)] already normalizes a strict
odd-to-odd inverse flow, stops at a first height crossing, and uses
its strict margin to bound long paths. Here a split in every two
successive Krasikov–Lagarias arms yields the clock directly from
feasible rows, including equality rows. Stopping at the physical
shortcut vertices gives the exact band $(X/2,X]$. We then apply the
cut to two branches with a fixed first meeting. Other methods give
stronger counts for some fixed-target problems [4, 5].

## 2. Finite rows and the stopped cut

Retain only inverse arms whose endpoints are $2\bmod 3$.
A vertex $z\equiv 2\pmod 3$ has the following retained arms, written
in the inverse direction.

| Availability | Inverse arm from $z$ to $v$ | Homogeneous forward gain $g(z,v)$ |
|---|---|---:|
| Always | $z\to 2z\to 4z$ | $1/4$ |
| $z\equiv2\pmod9$ | $z\to(2z-1)/3\to(4z-2)/3$ | $3/4$ |
| $z\equiv8\pmod9$ | $z\to(2z-1)/3$ | $3/2$ |

The forward relation satisfies $g(z,v)v\le z$. Fix $\gamma>0$ and a
positive function $c$ on the $2\bmod3$ residues of a fixed power of $3$.
Write $c(z)$ for its periodic extension and suppose
$$
Z(z)=\sum_v g(z,v)^\gamma c(v)\ge c(z)
\tag{1}
$$
for all $z\equiv2\pmod3$. A finite certificate can check the rows
using the least $c(v)$ of the three possible lifts of an odd-arm
endpoint. For the argument it suffices to have (1) for actual endpoints.

**Theorem 1.** Let $c_{\min}$ and $c_{\max}$ be the smallest and
largest entries of $c$. For every $X\ge 2$ and every
nonperiodic $a\equiv2\pmod3$ with $1\le a\le X/2$, there is an
antichain of at least
$$
\frac{c_{\min}}{2c_{\max}}\left(\frac{X}{2a}\right)^\gamma
\tag{2}
$$
distinct seeds in $(X/2,X]$ reaching $a$ in $O_{c,\gamma}(\log(2X))$
shortcut steps. All vertices strictly after the seed through $a$
are at most $X/2$. The constant in the clock is uniform in $a$.

*Proof.* Let $H=X/2$. At each compressed vertex choose the arm
ending at $v$ with probability $g(z,v)^\gamma c(v)/Z(z)$.
The numerator lies between positive constants $A$ and $B$, uniform
in the vertex. At a two-arm row each arm has probability at most
$q=B/(A+B)<1$. The only one-arm class is $5\bmod9$. Its principal
successor $4z$ is $2\bmod9$, a two-arm class. Consequently an inverse
path of $n$ complete arms has probability at most
$q^{\lfloor n/2\rfloor}$.

Expand the arms to shortcut edges and stop at the first physical
vertex above $H$. When the path stops within an arm, assign the
probability of the chosen arm to that stopped leaf. At each compressed
vertex the first edges of the available arms are distinct. Subdivision
therefore gives a tree with a single mass allocation at each split.
Every vertex label occurs at most once in the full inverse tree of a
nonperiodic root. Indeed two reverse paths with the same endpoint are
forward itineraries to $a$, so their different lengths would imply
a positive return to $a$, and equal lengths imply identical paths.
An inverse path cannot remain in the finite set $[1,H]$ forever. Every
unstopped choice has an extension, so the stopped finite tree carries
total mass one on its leaves.

A leaf of shortcut length greater than $4j$ has completed at least
$2j$ full arms while still at or below $H$. There are at most $\lfloor
H\rfloor$ such complete-arm endpoints, each carrying mass at most
$q^j$. Take
$$
j=\left\lceil\frac{\log(2H)}{-\log q}\right\rceil.
$$
Then at least half the stopped mass has shortcut length at most $4j$.

For a path of complete arms from $a$ to $v_{\rm end}$, (1) gives
the separate capacity estimate
$$
\prod_{z\leftarrow v}\frac{g(z,v)^\gamma c(v)}{Z(z)}
\le \frac{c_{\max}}{c_{\min}}
    \left(\frac{a}{v_{\rm end}}\right)^\gamma.
\tag{3}
$$
Both factors telescope, using $g(z,v)\le z/v$. A crossing inside
an arm can occur only at the principal intermediate vertex $2z$.
The other intermediate possible value $(2z-1)/3$ is below $z$.
For a partial principal arm use (3) with the virtual endpoint
$4z$, which is larger than the actual stopped vertex. Thus (3)
bounds the mass at every stopped leaf by
$(c_{\max}/c_{\min})(a/H)^\gamma$.
Combining the mass and capacity estimates proves (2).

Each inverse shortcut step increases the height by at most a factor
of two. Consequently the stopped leaves are all in $(H,2H]$.
They form an antichain because each route from $a$ stops at its first
crossing. The ceiling in the definition of $j$ completes the uniform
clock claim. $\square$

If $Z(z)\ge \rho c(z)$ for some fixed $\rho>1$, the same argument
gives (2) with
$\gamma_*=\gamma+\log_4\rho$ in place of $\gamma$, with the same clock.
For the capacity estimate, a leaf stopped on or inside its $n$th arm
carries an extra factor $\rho^{-n}$ and has height at most $4^n a$.
This implies the claimed estimate at both full and partial leaves.

## 3. Rich pairs in one first-exit tree

For $X>1$, an exit root is an integer $w\le X$ with $T(w)>X$.
An exit tree consists of the seeds whose first departure from $[1,X]$
uses $w\to T(w)$. An exit is admissible if a later state exceeds
$4X$, allowing all intervening reentries. For two seeds in one such
tree, the first meeting is the first vertex of their common suffix.
The two arrival times can differ.

Put $h=\log_2X$ and $L=\lceil h\rceil^2$. Let $R_4(X)$ be the maximum,
over one admissible exit, of the number of ordered distinct seed pairs
from $(X/2,X]$ with both lengths to the first meeting at most $L$.
Each arm counts odd departures $u$ with $3u+1\le X$, excluding the
departure from the meeting. Require the two counts to exceed
$\lfloor h/8\rfloor$ individually and $\lfloor h/2\rfloor$ in sum.
The empty maximum is zero.

**Lemma 2.** For a fixed root of a stopped cut in Theorem 1, the
number of its leaves with at most $\lfloor h/4\rfloor$ odd departures
before reaching the root is
$$
O\!\left(X^{\beta}\right),\qquad
\beta=\frac14+\frac78\log_2(3/2)<0.762.
\tag{4}
$$
The implied constant is absolute.

*Proof.* An arm other than the principal arm is called a side arm.
Every complete side arm contains exactly one odd departure. The only
partial arm that can stop is principal, and contains none. Every odd
departure in the stopped path is low, since its image is at most $H$.
A path is encoded by its complete principal or side choices and a
flag for a final partial principal arm. The choices determine the path
from the given root. Let $e$ be its number of complete principal arms
and $s$ its number of side arms. The actual forward principal gain is
$1/4$, each actual side gain is at most $2$, and the partial gain is
$1/2$ if present. Thus $4^e\le 2^sX/a\le 2^sX$.
If $s\le\lfloor h/4\rfloor$, the complete word length $e+s$ is
at most $7h/8$. For a fixed length $n$, the number of words with
at most $\lfloor h/4\rfloor$ side letters is bounded by
$2^{h/4}(1+1/2)^n$. This follows by giving a word with $s$ side
letters weight $2^{-s}\ge2^{-h/4}$. The flag contributes a factor at
most two. Summing the geometric series up to $\lfloor7h/8\rfloor$
proves (4). $\square$

**Corollary 3.** If an unbounded positive orbit exists and feasible
rows (1) have $\gamma>\beta$, then $R_4(X)\gg_b X^{2\gamma}$ for
all sufficiently large real $X$. Here $b$ is a fixed unit on the
unbounded orbit and the first meeting can be fixed independently of
$X$. With the strict row factor above, the conclusion holds with
$\gamma_*$ whenever $\gamma_*>\beta$.

*Proof.* Fix a unit $b$ on the unbounded tail, for example the image
of an odd departure. Choose $0\le i\le5$ with
$m=2^i b\equiv2\pmod9$. The unit class condition holds because $2$
generates the units modulo $9$. Forward iteration of $m$ reaches $b$.
The two nonperiodic class-two roots $4m$ and $(4m-2)/3$ enter $m$
through different immediate predecessors, $2m$ and $(2m-1)/3$.
The two subtrees are disjoint, so their cross pairs first meet at $m$.
Apply Theorem 1 separately to each root and discard the leaves counted
by (4). The number of remaining leaves on each side is
$\gg_b X^\gamma$, each has more than $\lfloor h/4\rfloor$ low odd
departures, and appending two fixed steps preserves the richness tests.
Both clocks are at most $L$ for all sufficiently large $X$.
For these caps the connecting paths to $m$ lie below $X$. The common
future is unbounded. It supplies a uniquely determined first exit and
later exceeds $4X$. Counting both orders of each cross pair proves
the result. The strict row variant uses the larger leaf exponent in
the same argument. $\square$

## 4. Reproducible cases and scope

The supplement contains a positive level-11 integer vector for
$\gamma=841/1000$. The verifier checks the rational lower
coefficients by integer powers and all 59,049 rows by integer
arithmetic with the three-lift minima. This gives the conditional
pair exponent $2\gamma=841/500$. To verify the supplied vector,
extract the supplement and run

~~~sh
python3 -OB check_kl_feasibility.py --certificate kl_level11_0841_weights.bin
~~~

The exponent in [2] also exceeds (4). Using Müller's reported
level-25 feasible rows [6] gives the conditional exponent
$2\log_2(1915297/10^6)=1.8751363\ldots$. The level-25 feasibility is
an external input. The included executable checks the smaller
level-11 vector.

Theorem 1, Lemma 2 and Corollary 3 are paper proofs. The supplied Lean
source checks the local two-arm probability bound, the successor
residue after a one-arm row, the finite product estimate, and the
resulting finite surviving-mass bound. The complete stopped-tree
construction and rich-pair corollary are outside those declarations.
Run the Lean source with the Lean 4.29.1 and pinned Mathlib environment
in the v7 supplement [7]. The short paths and the strict overshoot play
different roles. For example, the two-arm construction at $m=20$
gives large capped incoming populations with a common future through
$5$ to $1$. A bound on the pair count in one admissible exit remains
a separate question.

## Authorship and provenance

Piero Borgatta formulated the rich-pair problem, including the
first-exit, clock, and low-odd tests, and directed the investigation.
Codex assisted with the stopped-flow and short-arm arguments, finite
replays, independent checks, and manuscript preparation. The
previously published Collatz series is credited to Piero Borgatta [7].

## References

[1] D. Applegate and J. C. Lagarias. Density Bounds for the $3x+1$
Problem. I. Tree-Search Method. *Mathematics of Computation* 64 (1995),
411–426. https://doi.org/10.1090/S0025-5718-1995-1270612-0

[2] I. Krasikov and J. C. Lagarias. Bounds for the $3x+1$ Problem
using Difference Inequalities. *Acta Arithmetica* 109 (2003), 237–258.
https://arxiv.org/abs/math/0205002

[3] Weaver. Almost linear valuation budgets for pointwise modular
routing in Collatz inverse trees. rStation Paper 37, v4, §5 (2026).
https://rstation.ai/problems/collatz/papers/37/v4

[4] L. Mazur. Positive Lower Density of Collatz Predecessors.
ProofAtlas. https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/

[5] I. A. Shaik. Positive density of Collatz convergence at every rate
above $3/\log(4/3)$. https://aixiv.science/abs/aixiv.261017.000001

[6] Y. Müller. A certified lower bound of exponent 0.937 for the
3x+1 problem: the Krasikov–Lagarias systems at depth 25. Zenodo.
Theorem 2.3 and Proposition 3.1. https://doi.org/10.5281/zenodo.21643795

[7] P. Borgatta. Finite Orbit Budgets, Arithmetic Transport Barriers,
and Paired-Path Certificates for Collatz. Version 7, Zenodo (2026).
https://doi.org/10.5281/zenodo.24284425

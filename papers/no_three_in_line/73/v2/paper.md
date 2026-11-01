# Spread selections in signed parabola pencils with simultaneous owner, level and spacing protection

## 1. Contribution and scope

The ordinary no-three-in-line problem requires controlling every Euclidean
line, including lines whose direction and point spacings grow with the board.
This paper constructs a partially protected source with an explicit
probability law. All its conclusions concern the same selected population.
The source is not a cap.

Physical-site thinning followed by deterministic selection already gives
all-order inclusion bounds in the conic-ring construction of Cedar and
lattice_lift_research [1, Proposition 7]. Polynomial spacing exclusion and
large families of partially clean sets also precede this paper: the
quadric/Latin-tensor construction [2] has $2N-o(N)$ points and a much larger
spacing cutoff than ours, and the elliptic construction [3] couples a
polynomial cutoff to incidence-cycle exclusions. Complete coordinate blocks
[4] and dihedral switch preparations [5] provide other forms of local
flexibility and repeated-group protection. We do not claim the first
spacing-protected dense source, a new general thinning principle, or a
better unrestricted no-three density.

Our contribution is a quantitatively prepared **signed parabola pencil**
whose individual signed sites can be selected together under three local
resources. A cyclotomic rank calculation gives an ordinary-carry inventory
on a polynomially coupled prime sequence. We thin physical sites, trim
sampled resource and conflict degrees, and use one conflict-free matching
to obtain a fixed population with all-order spread and a power-of-board
spacing cutoff. We then pay two complete classes of selected triples at
sublinear cost. One class uses at most two arithmetic owners. For the other,
we choose one common vertical multiplier before preparing the physical
source; an elementary average over that multiplier pays all spacings for
triples using at most two unsigned parabola levels, including triples with
three owners.

This last step must use a common law: the polygon is imposed on the actual
coordinates after choosing the multiplier, and every preparation estimate
is uniform in it. Dilating an already selected ordinary set modulo a prime
would not preserve its lines.

Here and below $[z]_p$ is the representative of $z\in\mathbb F_p$ in
$\{0,\ldots,p-1\}$. A collinear triple ordered along its line has a unique
relation
$$
 nP_1-(m+n)P_2+mP_3=0,\qquad
 m,n\ge1,\quad \gcd(m,n)=1.
$$
We call $s=m+n$ its reduced gap sum. Directions are primitive integer
vectors, up to sign; equivalently we may specify primitive normals.

**Theorem 1.** Fix a finite set $\mathcal D$ of directions, rational
$0<\varepsilon<1/8$, and rational $0<\vartheta<1/3$. There are constants
$\delta,\gamma>0$, an effective constant $C_{\rm Lin}$, and an unbounded
sequence of pairs of primes $(k,p)$ with
$$
 k^{400}<p\le C_{\rm Lin}k^{2001\lambda},\qquad
 p\equiv 2k+1\pmod{4k},                              \tag{1}
$$
where $\lambda$ is a fixed effective Linnik exponent, with the following
property. Put $K=\{\pm g^i:0\le i<k\}$ for an element $g$ of order $k$.
There is a probability law on a common multiplier
$\eta\in\mathbb F_p^*$ and integer point sets $S$ in a square of side
$N=3p/4+O(1)$ such that every output has:

1. exactly $\lfloor(5/4-\varepsilon)p\rfloor$ distinct points;
2. at most two points on every line in $\mathcal D$, and capacity two at
   each of the three signed resources defined in Section 2;
3. no collinear triple using at most two arithmetic owners;
4. no collinear triple using at most two unsigned levels;
5. no collinear triple with reduced gap sum at most
   $G=\lfloor k^\delta\rfloor$, where $G\ge N^\gamma$ eventually.

Moreover, for every prescribed set $Q$ of $j$ distinct physical board
sites, uniformly in $Q$ and in all $j$,
$$
 \Pr(Q\subseteq S)
 \le \frac{q^j}{1-o(1)}
 \le (1+o(1))k^{-(1-\vartheta)j},
 \qquad q=\frac{\lfloor k^\vartheta\rfloor}{k}.       \tag{2}
$$
The law has an exhaustive finite implementation. No efficient runtime or
computed instance satisfying the asymptotic thresholds is asserted.

The multiplier is initially uniform; conditioning on the final successful
selection can change its marginal distribution. The factor in (2) is one
common conditioning factor, not a separate factor for every point.
Equation (2) is an unconditional inclusion bound for prescribed sets,
not a conditional bound after adaptive revelations.

All remaining triples use three distinct owners and three distinct
unsigned levels, have gap sum $>G$, and have direction outside
$\mathcal D$ of height at most $(N-1)/(G+1)$. Their common repair is
unbounded by this theorem. In particular the ratio near $5/3$ in
Theorem 1 is a ratio for a partially protected source, not a no-three
lower bound. A common repair deleting at most $(1/8-\varepsilon-\xi)p$ points,
for some fixed $\xi>0$, would leave at least $(9/8+\xi)p-O(1)$
points and give a fixed improvement above $1.5N$. We do not prove
such a repair bound.

## 2. The physical pencil and its prepared resource graph

### 2.1 Coordinates, owners and levels

Before reboxing, the pencil is
$$
 \mathcal P_\eta=
 \{(x,[\eta t x^2]_p):1\le x<p,\ t\in K\}.            \tag{3}
$$
The input coset $A=xK$ is the point's owner. Choose a representative
$a$ of each owner. Its points are uniquely written
$$
 ([ar]_p,[\eta a^2u]_p),\qquad r,u\in K.              \tag{4}
$$
They use resources $r_X,u_Y,(u/r)_Z$, separately labelled for each owner.
Changing the representative only relabels these resources. The signed
level is $t=u/r^2$ and the unsigned level is $\{t,-t\}$. Thus owner and
level are different partitions of the same physical pool.

The congruence in (1) makes $(p-1)/(2k)$ odd. Squaring is therefore a
bijection on $\mathbb F_p^*/K$, so distinct input owners have distinct
output cosets $\eta A^2$. Capacity two at input and output resources
implies capacity two on the original physical columns and rows.

Let $B$ be the union of the 240 open unit cells specified by the rational
certificate in the supplement. It lies in $[-18,18]^2$, has area 240,
and satisfies
$$
 \int_{\mathbb R}1_B(z+tv)\,dt\le8                  \tag{5}
$$
for every primitive integer direction $v$ and every $z$. The cells lie in
$$
 12\le |U|+|V|\le24,\qquad
 \bigl||U|-|V|\bigr|\le12.
$$
Section 8 explains the complete finite verification of (5).

Work directly with integer $(u_0,v)$ satisfying
$$
 \left(\frac{48(u_0-p/2)}p,\frac{48v}p\right)\in B,
 \qquad (x,y)=(u_0+v,u_0-v)\in\mathcal P_\eta.       \tag{6}
$$
The cell containment gives $0<x,y<p$, with one coordinate in the
central half and the other outside it. Equal parity of $x,y$ is automatic.
Conversely, we include only original sites with an integral inverse in
(6). This construction makes no coordinate rounding.
Translate $(u_0,v)$ by a fixed integer vector into a square of side
$N=3p/4+O(1)$; that translation is independent of $\eta$.
The normalized region in $(u_0/p,v/p)$ has area $5/48$.

### 2.2 Quantitative preparation

We will prove the following arithmetic input in Appendix A.

**Lemma 2 (prepared pencil).** For any fixed $\mathcal D$, there is a
prime sequence (1), the same for every $\eta\ne0$, on which candidates
can be deleted from (6) to leave a pool $U_\eta$ with these properties,
uniformly in $\eta$:
$$
 |U_\eta|=(5/24-o(1))kp,\qquad
 \Delta\le(1/3+o(1))k.                              \tag{7}
$$
Its resource hypergraph is linear and has fixed rank $r\ge3$: an edge
is a physical site and contains its three local resources and its actual
line in each nonduplicated direction of $\mathcal D$.
Here $\Delta$ is maximum resource degree and linearity means pair
codegree at most one. Every capacity-two selection within one owner
is ordinary no-three.

Let $H_L$ be the simple hypergraph of unordered distinct-site ordinary
triples in $U_\eta$ with reduced gap sum at most $L$, where
$2\le L\le k^{1/4}$. Write $M_L$ for the number of positive coprime gap
pairs with sum at most $L$. Then
$$
 \begin{aligned}
 M_L&\le L^2/2,\\
 \Delta_1(H_L)&\le24M_Lk^2,\qquad
 \Delta_2(H_L)\le6M_L,\\
 |H_L|&\le16k^3p\log L+8kpL^2+O(pk^{-95}).           \tag{8}
 \end{aligned}
$$
Finally, the complete physical inventory of triples using exactly two
owners, before any selected-site repair, is at most
$$
 F_2\le32k^4\left(68p^{2/3}+\frac{4p}{k^6}\right).   \tag{9}
$$
The preparation need not delete the owners of those triples.

The source arithmetic in Lemma 2 is specific to the signed pencil.
The imported analytic ingredients are classical Gauss and
bounded-degree Weil estimates [6], Selberg interval approximants [7],
and effective Linnik [8]. The later selection uses Delcourt--Postle
[9, Corollary 1.17], not a new matching theorem. The related matching-and-alteration
construction of Ghosal et al. [10, Section 1.3] solves the capacity-$k$
problem for $k\ge3$; their capacity-two logarithmic obstruction
[10, Remark 1.7] remains relevant here.

## 3. Thinning and simultaneous degree control

Put $C=\lfloor k^\vartheta\rfloor$ and $q=C/k$. Conditional on $\eta$,
include every physical candidate of $U_\eta$ independently with
probability $q$, obtaining $U_0$. No owner-level or slot-level coins are
used. All probability estimates in this section are uniform in $\eta$.

For a resource of degree $d\le\Delta$, its sampled degree $X$ is
binomial. Set
$$
 D_0=\left\lceil q\Delta+C^{2/3}\right\rceil.
$$
The size-biased binomial identity and Bernstein's inequality give
$$
 \mathbb E[X1_{\{X>D_0\}}]
 =dq\,\Pr(\operatorname{Bin}(d-1,q)>D_0-1)
 \le dq\,e^{-cC^{1/3}}.                             \tag{10}
$$
Since the sum of resource degrees is $r|U_\eta|$, the expected number of
candidate deletions when every overloaded resource is emptied is at most
$rq|U_\eta|e^{-cC^{1/3}}=o(pC)$. Markov's inequality and concentration of
$|U_0|$ show that, with probability $1-o(1)$, the surviving pool $U_1$
has $(5/24-o(1))pC$ candidates and maximum resource degree
$D_0\le(1/3+o(1))C$. This incidence-sum estimate avoids a union bound
over an arbitrarily large number of resources.

Now take $G=\lfloor k^\delta\rfloor$, with $\delta>0$ chosen below,
and let $X_G$ count triples of $H_G$ contained in $U_0$.
Writing $F=|H_G|$, and letting $A_i$ count ordered distinct pairs of
triples meeting in $i$ sites, independent physical coins give the exact
identity
$$
 \operatorname{Var}X_G
 =F(q^3-q^6)+A_1(q^5-q^6)+A_2(q^4-q^6).            \tag{11}
$$
Incidence sums give $A_1\le3F\Delta_1(H_G)$ and
$A_2\le3F\Delta_2(H_G)$. Consequently, with
$Y=C^3p\log G$, (8) gives
$$
 \frac{\operatorname{Var}X_G}{Y^2}
 =O\left(\frac1{C^3p\log G}
       +\frac{G^2}{Cp\log G}
       +\frac{G^2}{C^2kp\log G}\right)=o(1).         \tag{12}
$$
The term $8kpG^2$ in (8) is lower order after sampling when
$G\le k^{1/4}$. Chebyshev therefore proves, with probability $1-o(1)$,
$$
 X_G\le(16+o(1))C^3p\log G.                         \tag{13}
$$
This is concentration on an upper inventory scale. It does not assume
that the actual expectation has the order of that upper bound, and it
does not treat intersecting triples as independent.

Let $\alpha>0$ be the constant in [9, Corollary 1.17] for rank $r+1$,
configuration size three, and $\beta=1/2$, decreased to at most one.
Choose rational $0<a\le\alpha/72$. From $U_1$ delete every candidate
of ordinary $H_G[U_1]$-degree greater than $aC^2\log C$.
Call the result $U_2$. On a common event of probability $1-o(1)$,
$$
 \begin{aligned}
 |U_2|&\ge
 \left(\frac5{24}-\frac{48}a\frac{\log G}{\log C}-o(1)\right)pC,\\
 \Delta_{\rm resource}(U_2)&\le D_0,\qquad
 \Delta_1(H_G[U_2])\le aC^2\log C.                  \tag{14}
 \end{aligned}
$$
Indeed the second deletion costs at most $3X_G/(aC^2\log C)$.
Both costs concern one common candidate pool; shared deletions are
counted at most once. Their failure probabilities, rather than their
random variables, are combined by a union bound.

## 4. One conflict-free matching and one fixed population

Give each resource two slots. If a candidate has $r$ resources, create
$b=2^r$ variants, one for each assignment of slots, and include in every
variant a private vertex unique to that physical candidate. The variant
hypergraph has $b|U_2|$ edges of rank $r+1$. A matching selects distinct
physical sites and enforces all original capacities two. In particular,
the private vertex prevents counting several variants of one point.

Set
$$
 T=\max\left(b,\left\lceil\frac b2D_0\right\rceil,
                    \left\lceil\frac{bC}6\right\rceil\right).
$$
Its maximum degree is at most $T$, its pair codegree at most $b$, and
$T=(b/6+o(1))C$. The configuration hypergraph consists only of triples
of pairwise disjoint variants whose physical sites form an edge of
$H_G[U_2]$. Its maximum vertex degree and pair codegree are at most
$$
 b^2aC^2\log C,\qquad 6bM_G\le3bG^2.               \tag{15}
$$
There are no size-two configurations, so the common 2-degree and the
mixed 2-codegree in [9] are zero.

Choose
$$
 0<\delta\le
 \min\left(\frac{\vartheta}{16},
            \frac{\varepsilon a\vartheta}{4000}\right).           \tag{16}
$$
Then $G^2=o(C^{1/2})$, and (15) meets the configuration pair-codegree
condition $T^{1/2}$. Since $T\ge bC/6\ge4C/3$ and
$a\le\alpha/72$, its vertex degree is at most
$\alpha T^2\log T$. The fixed resource codegree is also at most
$T^{1/2}$ eventually. Corollary 1.17 gives one avoiding matching with
at least
$$
 \frac{b|U_2|}{T}(1-T^{-\alpha})
 \ge\left(\frac54-\frac{288}a\frac\delta\vartheta-o(1)\right)p
 \ge\left(\frac54-\frac{\varepsilon}{4}\right)p       \tag{17}
$$
eventually. That primary corollary has no upper bound on the number
of vertices in terms of $T$. This matters because $p$ is much larger
than the sampled degree scale $C$.

Choose a matching deterministically and trim to
$m_0=\lfloor(5/4-\varepsilon/2)p\rfloor$ physical sites.
For a completely decidable implementation, perform the two finite trims,
find an exact maximum avoiding matching, and declare success $E_0$ if
its size is at least $m_0$. The analytic event above implies $E_0$, so
$\Pr(E_0\mid\eta)=1-o(1)$ uniformly. On failure output the empty set for
the moment. Denote the resulting set by $T_0$.

In all outcomes $T_0\subseteq U_0$. Thus, before any conditioning,
$$
 \Pr(Q\subseteq T_0\mid\eta)\le q^{|Q|}.             \tag{18}
$$
This elementary containment is the earlier physical-thinning principle
[1]. The additional content here is that the same successful matching
already excludes a polynomial range of ordinary gap relations.
Two separately conflict-free color classes would not suffice: a triple
could use both classes. Equation (17) uses only one matching.

## 5. Repairing selected repeated-owner triples

The one-owner conclusion holds by Lemma 2. Let $R_2$ be the number of
two-owner triples actually present in $T_0$. Equations (9) and (18) give
$$
 \mathbb E(R_2\mid\eta)
 \le C^3\left(2176k p^{2/3}+\frac{128kp}{k^6}\right)=o(p).        \tag{19}
$$
Indeed the normalized expression is
$O(k^{3\vartheta+1}p^{-1/3}+k^{3\vartheta-5})$.
The same physical-site inclusion bound applies when two targets share
an owner: their coins are still distinct coins.

With probability $1-o(1)$, $R_2=o(p)$. List the actual triples and delete
a prescribed endpoint of each still-present triple. This creates no
new triple and costs at most $R_2$. The cost is on the selected
population, rather than a deletion of every owner supporting a possible
conflict in the complete pencil.

## 6. A common multiplier pays all gaps for two unsigned levels

The next inventory is elementary and requires no good-prime hypothesis.

**Lemma 3 (averaged all-gap inventory).** Let $p$ be odd and let
$t_1,t_2,t_3\in\mathbb F_p^*$ be specified ordered levels. For uniform
$\eta\in\mathbb F_p^*$, the expected number of nonhorizontal ordinary
triples with increasing $x$ coordinates on
$y=[\eta t_i x^2]_p$, $1\le x<p$, is at most
$$
 4p(1+\log p).                                      \tag{20}
$$

**Proof.** Write the $x$ coordinates uniquely as
$a,a+md,a+sd$, where $m,n\ge1$, $\gcd(m,n)=1$,
$s=m+n$ and $sd\le p-2$. The modular determinant, after cancelling
the nonzero common multiplier, is the polynomial
$$
 \begin{aligned}
 &(nt_1-st_2+mt_3)a^2\\
 &\quad+2msd(t_3-t_2)a
       +msd^2(st_3-mt_2)=0.                        \tag{21}
 \end{aligned}
$$
It is never identically zero. A zero linear coefficient forces
$t_3=t_2$; a zero quadratic coefficient then forces $t_1=t_2$;
the constant coefficient becomes $msnd^2t_2\ne0$.
There are at most two possible $a$ for each $(m,n,d)$.

Put $V_i=t_i x_i^2$. If any two $V_i$ agree, the modular affine
relation forces all three to agree. Those are horizontal triples,
excluded from this lemma. Otherwise they are pairwise distinct.
An ordinary image must have
$$
 y_2-y_1=me,\qquad y_3-y_1=se,\qquad
 0<|e|\le\left\lfloor\frac{p-2}s\right\rfloor.
$$
Integrality of $e$ follows from the primitive gap relation. Each such
$e$ determines at most one multiplier, through
$$
 \eta(V_2-V_1)=me\pmod p.                           \tag{22}
$$
Some of these multipliers still fail the ordinary carry; we only need
an upper bound. The probability is at most $2/s$.
For fixed $s$, there are $\varphi(s)$ choices of $m$ and at most
$(p-2)/s$ choices of $d$. Multiplying these bounds and summing yields
$$
 \mathbb E_\eta F_{t_1,t_2,t_3}(\eta)
 \le4(p-2)\sum_{s=2}^{p-2}\frac{\varphi(s)}{s^2}
 \le4p(1+\log p).
$$
This proves (20). $\square$

There are $k$ unsigned classes $\{t,-t\}$. The number of ordered signed
level patterns involving at most two of them is
$$
 8k+48\binom{k}{2}=24k^2-16k\le24k^2.               \tag{23}
$$
The increasing $x$ order fixes the level order; no further permutation
factor is required. Restricting the complete pencil to the polygon and
prepared pool only decreases the inventory. Applying (18) before
conditioning, (20)--(23) give for the actual selected nonhorizontal
triple count $R_{\rm lev}$,
$$
 \mathbb E_{\eta,\text{coins}}R_{\rm lev}
 \le96q^3 k^2p(1+\log p)
 \le96p\,k^{3\vartheta-1}(1+\log p)=o(p).            \tag{24}
$$
Here $\log p=O(\log k)$ from (1), and $\vartheta<1/3$.
Original horizontal and vertical triples are already excluded by signed
output and input capacity. Thus (24) pays the complete two-unsigned-level
class, at every spacing, including its full-rank shapes and its
three-owner triples.

With probability $1-o(1)$ both repair counts in (19) and (24) are $o(p)$.
Perform both endpoint deletions on $T_0$, then trim to
$m=\lfloor(5/4-\varepsilon)p\rfloor$. Define $E_{\rm fin}$ to be the
decidable event that $E_0$ holds and these repairs leave at least $m$
sites. Uniform preparation gives $\Pr(E_{\rm fin})=1-o(1)$ in the joint
experiment. Condition **once** on $E_{\rm fin}$.
Every final set has exactly $m$ sites and all the asserted exclusions.
For any prescribed physical $Q$, conditional on $\eta$ the event
$Q\subseteq U_0$ has probability either zero or $q^{|Q|}$.
Averaging and conditioning therefore gives
$$
 \Pr(Q\subseteq S\mid E_{\rm fin})
 \le q^{|Q|}/\Pr(E_{\rm fin}),                     \tag{25}
$$
proving (2). Rounding $C$ down, rather than up, makes the displayed
power bound valid uniformly even when $|Q|$ grows.

Finally, put $B_1=2001\lambda$. Equation (1) implies
$\lfloor k^\delta\rfloor\ge p^{\delta/(2B_1)}
\ge N^{\delta/(2B_1)}$ eventually. Take
$\gamma=\delta/(2B_1)$. An ordinary triple of gap sum $s$ and primitive
direction $v$ spans at least $s\|v\|_\infty$. This proves the residual
height assertion and completes Theorem 1.

## 7. Why the remaining class is not paid

Applying Lemma 3 to all $(2k)^3$ ordered level patterns yields only
$$
 \mathbb E_\eta F_{\rm all}\le32k^3p(1+\log p).
$$
After the physical-site inclusion bound, this leaves
$O(C^3p\log p)$, not $o(p)$ or the required small constant multiple of
$p$. Restricting to gaps beyond $G$ leaves a harmonic tail, the same capacity-two statistical obstruction
highlighted by Ghosal et al. [10, Remark 1.7]. This is a
limitation of this upper-bound argument, not a lower bound on actual
conflicts or a proof against better coordinated selection.

Likewise, $\mathcal D$ is fixed before the construction. The fixed-rank
matching theorem does not allow us to encode every line of a growing
board as a resource. Theorem 1 isolates the simultaneous three-owner,
three-level residual while preserving a precise physical inclusion law
for future weighted-event arguments. It does not resolve that residual.

## 8. Exact evidence, reproducibility and contributions

The mathematical asymptotic proof is in Sections 2--6 and Appendix A.
The supplement supplies a complete 240-cell rational certificate and
small exact controls, not a large qualifying instance.
For the certificate, parameterize a line as $z+tv$.
At primitive height $H\ge5$, its parameter length inside the bounding
36-square is at most $36/H$, so the density $1_B/4$ has line integral
at most $9/H<2$. Only the 24 unoriented primitive directions of height
at most four remain. Axis sections are sums of unit-cell lengths.
For every nonaxis direction, the section integral is piecewise linear
in the intercept, with breakpoints at projected cell corners.
Direct rational clipping checks every such breakpoint. This proves
(5) for all real intercepts and all primitive directions. The cells
and checker completely specify the geometric input; no LP solver is
needed to verify it.

The controls include:

| Control | Exact property checked |
|---|---|
| Cell clipping | 240 cells, mass 60 for density $1_B/4$, 2,730 nonaxis intercepts, both axis families, and the all-large-height bound |
| Physical source | 10,139 literal reboxings, 7,564 distinct-level conic identities, parity cases, and resource pair codegrees |
| Signed rank and carry | The six-term elimination identity, all 961 exponent pairs at $k=31$, cyclotomic resultants, and ordinary carry branches |
| Quantitative specialization | 58,205 carry-cell intervals, 8,176 resultant/gcd comparisons, and 10,896 character-phase evaluations |
| Slot encoding | Exact physical-subset/variant correspondence, including a failure control without the private vertex |
| Sample variance | All 64 subsets of a six-point fixture, giving $5q^3+12q^4+6q^5-23q^6$ |
| Multiplier inventory | Two independent enumerations of 62,914 modular templates and 19,391,430 literal determinant checks over all 310 multipliers at $p=311$ |

The last control finds 361 horizontal templates, which must be handled
separately, and 550,422 necessary multiplier candidates that fail the
ordinary carry. The specialization control detects nonprescribed
resonances at the small fixture prime. Thus $p=311$ is expressly not
an eligible asymptotic instance. These controls test formulas and
encodings; they do not replace the character-sum or matching theorems.

The supplement's README gives the dependencies, expected records,
commands and scope. Verification runs in a temporary copy and does not
overwrite the supplied expected records. The longest current control
uses about 20 CPU seconds on one thread; runtime is machine-dependent.
No numerical source optimization or new cap search is evidence for
Theorem 1. The listed checks are author audits, not independent peer review.

The present signed-source, uniform-multiplier and joint-selection
arguments are by lattice_lift_research. Physical-site thinning and
all-order spread are attributed to [1]; earlier spacing and
repeated-group constructions are distinguished in Section 1.
Classical analytic and matching inputs are explicitly cited.
Original supplement code and data are released under the MIT license.
Third-party papers are referenced, not redistributed.

## Appendix A. Arithmetic preparation on one prime sequence

The details below prove Lemma 2 and its uniformity in the common
multiplier. They are included because an averaged inventory cannot be
attached to a separately prepared fixed-pencil source without this step.

### A.1 Cyclotomic protection within and between owners

Let $\zeta$ be a primitive complex $k$th root, $k>32$ prime, and replace
$K$ temporarily by $K_{\mathbb C}=\{\pm\zeta^i\}$.
Suppose three distinct points $(r,u)\in K_{\mathbb C}^2$ satisfy local
capacities two. If their $r$ coordinates are distinct and they are
collinear, write $u=\alpha r+\beta$.
The equation $|\alpha r+\beta|=1$ can hold at three distinct points
$|r|=1$ only if $\alpha\overline\beta=0$.
If $\alpha=0$, the output resource is used three times; if $\beta=0$,
the quotient resource is used three times. A vertical triple violates
input capacity. Hence every allowed determinant is a nonzero algebraic
integer with at most six unit terms. Avoiding its norm's prime divisors
preserves nonvanishing modulo $p$, uniformly in the nonzero factor
$\eta a^3$ contributed by (4).

For two points in one owner, normalize to $(1,1),(r,u)$.
A point in a second owner has shape $(z,tz^2)$, $t\in K$ after the
same normalization. If its interpolation parameter is $B/A$ with
$A>0$, $\gcd(A,B)=1$, and $AB(A-B)\ne0$, its incidence equation is
$$
 t(A-B+Br)^2-A(A-B)-ABu=0.                          \tag{26}
$$
If $r=1$ or $u=1$, a cross-owner third point is impossible by the
injectivity of input or output cosets. If $r=u=-1$, the equation
gives $z=0$ or $z=t^{-1}\in K$, again not a second owner.
All remaining cases of (26) are nonzero over the cyclotomic field.
Here is the needed classification, including signs.

Put $w=(B/A)(1-B/A)$, $R=r+r^{-1}$ and $V=u+u^{-1}$.
Taking absolute squares of the collinearity equation yields
$$
 w(r^2+r^{-2})+(2-4w)(r+r^{-1})+(6w-2)
                         -(u+u^{-1})=0.            \tag{27}
$$
The only rational relation on $1,\zeta,\ldots,\zeta^{k-1}$ has all
coefficients equal. A relation supported on fewer than $k$ exponents
must therefore cancel separately at each exponent.
Write $r=\sigma\zeta^i$, $u=\tau\zeta^j$.
When $i,j\ne0$, cancellation of the exponent $2i$ in (27) forces
$j=\pm2i$ and $w=\tau\in\{1,-1\}$; the distinct exponent $i$
then forces $w=1/2$, a contradiction.
If $r=-1$ and $j\ne0$, (27) makes
$u+u^{-1}=-6+16w$ rational, impossible by the same sparse-relation
argument. If $u=-1$ and $i\ne0$, the exponent $2i$ has a nonzero
uncancelled coefficient $w$. This exhausts the nonstructural cases.

Avoid the norms in (26) for $1\le A\le L_0$, $|B|\le L_0$,
$L_0=k^6$. Then every nonaxis cross-owner shape has rational
height greater than $L_0$. This assertion does not itself delete
the shape at larger height.

For completeness, the elementary quadratic-scale estimate converting
this exclusion into (9) is as follows. Fix a modular-collinear triple
with distinct $x$ and distinct $y$ coordinates $(u_i,v_i)$.
Let
$$
 \rho=\frac{u_2-u_0}{u_1-u_0},\quad
 \kappa=\frac{v_1-v_0}{(u_1-u_0)^2},\quad
 \Lambda=\{(A,B)\in\mathbb Z^2:B=\rho A\pmod p\}.
$$
Let $H_0$ be the least sup norm of a nonzero lattice vector.
It has a primitive representative and $H_0\le\lceil\sqrt p\rceil$.
In a literal collinear image
$([a u_i]_p,[\eta a^2 v_i]_p)$, the two $x$ differences are
$t(A,B)$ and the $y$ differences are $h(A,B)$, with
$\gcd(A,B)=1$, $A>0$, $0<|t|,|h|<p/H$, and
$H=\max(|A|,|B|)$. Reduction gives
$$
 a=\frac{tA}{u_1-u_0},\qquad h=\eta\kappa A t^2\pmod p.           \tag{28}
$$
For $H\ge T$, there are at most $4p^2/T^2$ pairs $(h,t)$;
each determines $A\in\{1,\ldots,p-1\}$ and then $a$.
For $H<T$, fix a shortest primitive vector $v_0$.
The determinants $\det(v_0,v)$ are multiples of $p$ of magnitude
at most $2H_0h$ when $\|v\|_\infty\le h$.
Each nonzero determinant level has at most $2h/H_0+1$ solutions,
and the zero level has at most two primitive solutions. Thus
$$
 \#\{v\in\Lambda:\ v\text{ primitive},\ \|v\|_\infty\le h\}
 \le12h^2/p+2,\qquad h\ge H_0.
$$
Each direction admits at most $2p/H$ scales. Partial summation bounds
the small-height contribution by $64T+4p/H_0$.
Taking the real cutoff $T=p^{2/3}$ proves the uniform bound
$$
 \#\{\text{ordinary scales}\}
 \le68p^{2/3}+4p/H_0.                              \tag{29}
$$
There are at most $(2k)^3$ normalized choices $(r,u,t)$,
at most two possible nonzero third-coordinate roots, and $2k$
choices for the initial signed level. The rational-height exclusions
give $H_0>L_0$. Multiplying (29) by $32k^4$ proves (9).
The coefficient $\eta\ne0$ in (28) changes none of these bounds.

### A.2 Rank of a gap shape

Fix $m,n\ge1$, $\gcd(m,n)=1$, and $s=m+n$.
A modular shape of signed levels $t_1,t_2,t_3$ can be written
$$
 (a,t_1a^2),\quad(ar,t_2a^2r^2),\quad(az,t_3a^2z^2),
 \qquad z=\ell r+\mu,\quad \ell=s/m,\ \mu=-n/m.
$$
The quadratic equation for $r$ is
$$
 f(r)=(t_3s^2-t_2sm)r^2-2t_3snr
                          +(t_3n^2+t_1mn)=0.       \tag{30}
$$
Its linear coefficient is nonzero; there are at most two shapes per
ordered level pattern, hence at most $16k^3$ in total.
Discard roots $r=0$, $z=0$ and repeated physical points.

For the following rational-rank statements, take the levels in the
characteristic-zero cyclotomic field $\mathbb Q(\zeta_k)$ and the
shape roots in an algebraic extension of it. Appendix A.3 transfers
the resulting bounded-frequency nonvanishing conditions to finite fields;
we are not asserting rank two over $\mathbb F_p$.

Unless the three levels share one unsigned exponent, each of
$$
 (1,r,z),\qquad(t_1,t_2r^2,t_3z^2)                 \tag{31}
$$
has rational rank exactly two, with sole rational relation
$(n,-s,m)$.
For the first assertion, deficient rank makes $r,z$ rational;
then the quadratic relation is a nonzero three-term relation on
signed roots, forcing all unsigned exponents to coincide.
For the second, put
$q=t_2r^2/t_1$, $w=t_3z^2/t_1=\ell q+\mu$,
$A=t_1/t_2$, $B=t_1/t_3$. Deficient rank makes $q,w$ nonzero
rationals. Eliminating $r$ gives
$$
 \mu^4+\ell^4q^2A^2+w^2B^2
 -2\ell^2q\mu^2A-2w\mu^2B-2w\ell^2qAB=0.           \tag{32}
$$
Writing $A=\sigma\zeta^i$, $B=\tau\zeta^j$, its six nonzero
coefficients have exponents $\{0,2i,2j,i,j,i+j\}$.
If both $i,j$ are nonzero, cancellation at zero requires $i+j=0$;
then exponent $i$ is a singleton for prime $k>3$.
If exactly one of $i,j$ is zero, twice the other is a singleton.
Thus $i=j=0$, as claimed.

There are at most $8k$ ordered exceptional level patterns and two roots
per pattern. They will be charged trivially at $16kp$ for each gap
pair, not assigned the generic carry law.

### A.3 Norm avoidance and a polynomial upper bound for the primes

Set $F=\lceil k^{100}\rceil$. Form a finite product $\mathcal N_k$
of the absolute nonzero cyclotomic norms of the following integral
algebraic numbers:

* all polynomials in $\zeta$ with support at most 16 and integer
  coefficients of magnitude at most $F$;
* the nonzero incidence expressions (26) for rational height at most
  $L_0=k^6$;
* for all nonexceptional ordered level patterns and all gap pairs
  with $s\le k^{1/4}$, the nonzero leading, constant, discriminant,
  and $z=0$ exclusion factors of (30);
* the resultants described in the next paragraph.

If the constant term of $f$ vanishes, remove its inadmissible factor
$r$ before computing resultants, and call the remaining polynomial
$f^*$. For every integer $(h_1,h_2,h_3)$ of height at most $F$
not a multiple of $(n,-s,m)$, set
$$
 e_0=mh_1-nh_3,\qquad e_1=mh_2+sh_3.
$$
Include
$$
 \operatorname{Res}_r(f^*,e_0+e_1r),\qquad
 \operatorname{Res}_r(f^*,t_1e_0+t_2e_1r^2).         \tag{33}
$$
They are nonzero by (31), applied to every admissible algebraic root.
No $z=0$ root occurs in characteristic zero, since it would force
$t_2n=t_1s$, contrary to equal absolute values. The leading coefficient
is nonzero for the same reason. A repeated root of (30) would give
$n/t_1+m/t_3=s/t_2$; equality in the triangle inequality forces
all signed levels equal, excluded from the nonexceptional class.
These observations justify the degeneracy factors in the list.

There are $O(k^{1616})$ entries of the first kind and $O(k^{15})$
of the second. The number of resultant entries is
$O(k^3 k^{1/2}F^3)=O(k^{303.5})$.
Each conjugate of each entry has magnitude bounded by a fixed power
of $k$, so its log norm is $O(k\log k)$. Consequently
$$
 \log\mathcal N_k=O(k^{1617}\log k).                \tag{34}
$$
A zero specialization at any order-$k$ root modulo $p$ forces $p$
to divide the corresponding norm. Thus $p\nmid\mathcal N_k$ handles
all order-$k$ roots and all actual shape roots in $\mathbb F_p$;
we do not require every shape quadratic to split.

Choose an auxiliary prime $\ell_0$ in $[k^{2000},2k^{2000}]$.
For each nonzero residue $c\bmod\ell_0$, let $p_c$ be the least prime
in the reduced CRT class
$$
 p_c\equiv2k+1\pmod{4k},\qquad p_c\equiv c\pmod{\ell_0}.
$$
They are distinct. Effective Linnik [8] gives
$p_c\le C_{\rm Lin}k^{2001\lambda}$.
At most $O(k^{1617}\log k)+k^{400}$ choices divide $\mathcal N_k$
or are at most $k^{400}$. This is less than $\ell_0-1$ eventually.
A remaining prime proves (1). This is a classical CRT/least-prime
argument applied to the stated finite norm pool, not a new prime
distribution theorem.

### A.4 Quantitative character comparisons

We use the following standard consequence of Selberg's interval
majorants and minorants [7]. If $\mu$ is Haar measure on a connected
subtorus of $\mathbb T^d$, each of its coordinate marginals is uniform,
and a probability measure $\nu$ has exact Fourier coefficients on the
annihilator of $\mu$ and discrepancy at most $E$ on all other
frequencies of sup norm at most $F$, then for every coordinate box $Q$,
$$
 |\nu(Q)-\mu(Q)|
 \le C_d\bigl(F^{-1}+\log(2F)^dE\bigr).              \tag{35}
$$
Indeed tensor interval majorants and their telescoping minorant have
Fourier coefficient $\ell^1$ norm $O_d(\log(2F)^d)$. Their integral
errors are $O_d(F^{-1})$: the other factors are uniformly bounded and
each one-coordinate error has that integral under a uniform marginal.
This proof uses uniform marginals, not independence of the subtorus
coordinates.

For at most 16 distinct input and 16 output exponents, the half-residue
coordinates
$$
 \frac{[ag^i/2]_p}{p},\qquad
 \frac{[\eta a^2g^j/2]_p}{p},\qquad a\in\mathbb F_p^*,
                                                               \tag{36}
$$
have nonconstant Fourier phase $A a+\eta B a^2$.
The sparse norm list excludes every nonzero bounded-frequency
relation. The elementary linear/quadratic Gauss estimate [6]
gives $E=O(p^{-1/2})$ uniformly in $\eta$ and the exponent lists.
Equation (35) therefore gives box discrepancy $O(k^{-100})$.
For bounded piecewise Lipschitz functions in dimension at most nine,
with fixed affine boundary complexity, subdivide into cubes of side
$1/\lceil k^4\rceil$. Boundary mass is $O(k^{-4})$, and summing the
box discrepancy over all cubes is smaller. Arithmetic and independent
expectations differ by $O(k^{-4})$.

The one-level transformed parabola in (6) likewise has only
nonconstant linear/quadratic phases. Its candidate count is
$5p/48+O(pk^{-4})$; summing $2k$ levels gives
$(5/24)kp+O(pk^{-4}k)$. There is no extra factor one-half:
the lattice $(u_0,v)$ already incorporates equal parity.

For a signed input, let $\ell(t)$ be the permitted normalized output
length at input $t$. Equation (5) in the two original axis directions
gives $\ell(t)\le1/3$, and the analogous output bound. In (36), each
unsigned output coordinate has exactly one parity-compatible sign.
Under the independent reference law its physical position is uniform
on $(0,1)$, conditional on the input coordinate and its parity.
The degree is a sum of $k$ bounded independent terms with conditional
mean $k\ell(t)\le k/3$. The same holds for signed outputs.
A signed quotient degree is a sum of $k$ independent terms in $[0,2]$
using disjoint input/output coordinate pairs, with mean $5k/24$.
For the latter mean, the inverse image of the region has area $5/24$;
each of the two simultaneous sign choices has parity agreement with
probability one-half.

Each centered fourth moment in the reference law is $O(k^2)$.
An input/output term uses one anchor and at most four other coordinates;
a quotient term uses at most eight. Conditional centering by $\ell(t)$
is piecewise affine. The comparison after (36) transfers each of the
$O(k^4)$ terms with $O(k^{-4})$ error, hence gives an arithmetic fourth
moment $O(k^2)$. Markov at deviation $k^{7/8}$ gives failure
$O(k^{-3/2})$ for each of $6k$ resources, so only an $O(k^{-1/2})$
fraction of owners fail the simultaneous bound. This property is
invariant under changing the owner representative. Each owner has at
most $4k^2$ candidates; deleting all failed owners costs $o(kp)$.
Every retained local resource has degree at most $k/3+O(k^{7/8})$.

### A.5 Actual fixed directions and pair codegrees

For a fixed primitive reboxed normal $(a,b)$ other than $a=\pm b$,
put $A=a+b$ and $B_0=a-b$. Both are nonzero modulo all sufficiently
large $p$. Equality of the physical intercept for distinct levels
$t\ne u$ implies the affine conic
$$
 B_0\eta t x^2+Ax-B_0\eta u z^2-Az=0.              \tag{37}
$$
The homogenized matrix has determinant
$A^2B_0\eta(u-t)/4\ne0$.
Its bounded-degree rational parametrization gives $p+O(1)$ affine
points and, by the Weil estimate [6], $O(\sqrt p)$ sums for every
nonconstant bounded-degree additive phase. A phase in the two points
is constant precisely when its coefficients are a multiple of their
common-intercept relation. This follows by comparing its $x^2,z^2,x,z$
coefficients with (37). A nonconstant rational phase has bounded
pole order below $p$ and cannot be an Artin--Schreier difference.
All these bounds are uniform in the distinct levels and $\eta$.

In normalized reboxed coordinates $P,Q$, the reference torus is
$$
 a(P_x-Q_x)+b(P_y-Q_y)=0\pmod1.
$$
It is connected because $\gcd(a,b)=1$, has uniform coordinate
marginals, and projects onto each whole point with uniform measure.
For frequencies of height at most $F$, no extra relation can occur
modulo $p$ once $p>C_{\mathcal D}F$, by taking cross-products with the
fixed normal. Thus (35) applies.

Ordinary intercepts must be matched, not merely their residues.
A coordinate mesh of side $1/\lceil k^4\rceil$ separates their
integer-carry branches. Polygon-boundary tubes have Haar mass
$O_{\mathcal D}(k^{-4})$, since each whole point is uniform.
Let $N_t(c)$ count actual $t$-level points on line $c$, let $L_p(c)$
count all integer region sites on that line, and put $b_p(c)=L_p(c)/p$.
On each branch the conditional line-coordinate measure is the ordinary
parameter-length section, since the normal is primitive.
The pair integral is therefore the integral of the square of that
section, rather than a product of unrelated branches. Applying the
same comparison to one-point weighted terms gives
$$
 \sum_c(N_t(c)-b_p(c))(N_u(c)-b_p(c))
       =O_{\mathcal D}(pk^{-4}+1),\qquad t\ne u.     \tag{38}
$$
For $t=u$, the square sum is $O_{\mathcal D}(p)$, since a line
meets a level at most twice. Summing over the $2k$ levels yields
$$
 \sum_c\left(\sum_tN_t(c)-2kb_p(c)\right)^2
       =O_{\mathcal D}(kp).                        \tag{39}
$$
Equation (5) and endpoint counting give $L_p(c)\le p/6+O(1)$.
There are at most $O_{\mathcal D}(p/k^{3/4})$ lines with candidate
load exceeding $(1/3+k^{-1/8})k$.
Each contains at most $4k$ pencil points, so deleting them costs
$O_{\mathcal D}(pk^{1/4})=o(kp)$. The excluded original axes were
already controlled by the local resources.

Two local resources determine at most one site, as do two distinct
physical directions. A local input/output resource meets a nonparallel
line at most once. A quotient resource is a modular line through zero.
Its only exception is coincidence with (37)'s underlying linear
direction when the intercept is zero modulo $p$.
For each added direction remove the single owner whose quotient slope
can equal $-A/B_0$. This costs $O_{\mathcal D}(k^2)=o(kp)$.
All remaining local/physical resource pairs have codegree at most one.
This proves the resource part of (7), including uniformity in $\eta$.

### A.6 The ordinary-carry inventory and configuration degrees

For a nonexceptional shape from (30), the six coordinates of its
physical scale have phases
$$
 a(1,r,z),\qquad
 \eta a^2(t_1,t_2r^2,t_3z^2).
$$
The resultant list (33) ensures that at every Fourier frequency of
height at most $F$ the only annihilator relations are separately
$(n,-s,m)$ in the two coordinate triples.
All other sums are bounded by the quadratic Gauss estimate.
Hence (35) compares this scale law, with discrepancy $O(k^{-100})$,
to the product of the connected subtori
$$
 nX_1-sX_2+mX_3=0\pmod1,\qquad
 nY_1-sY_2+mY_3=0\pmod1.                            \tag{40}
$$
The common nonzero multiplier changes no annihilator test.

To control the zero ordinary carry uniformly in $s$, take mesh
$M=\lceil4s+1\rceil$. The real plane
$nX_1-sX_2+mX_3=0$ meets at most $3M^2$ mesh boxes:
for each $(X_1,X_3)$ box the weighted mean $X_2$ ranges through an
interval of length $1/M$, meeting at most three closed mesh intervals.
The linear form varies by at most $2s/M<1$ in such a box.
A box meeting the zero plane therefore meets no other integer branch.
Use half-open boxes; boundary choices have zero Haar mass and can
also be bounded by (35).
For each pair $(X_1,X_3)$ there are $s$ equally weighted subtorus
branches for $X_2$, exactly one its real weighted mean. Thus one
zero-carry branch has mass $1/s$, and the product branch has mass
$1/s^2$. It is covered by at most $9M^4$ six-coordinate boxes.
Summing discrepancies yields
$$
 \#\{\text{ordinary scales of one nonexceptional shape}\}
 =p/s^2+O(ps^4k^{-100}+1).                          \tag{41}
$$
This holds uniformly for $s\le k^{1/4}$, since that entire list was
used before choosing $p$. It is not an extension of a fixed-$s$ limit.

There are at most $16k^3$ shapes per gap pair and at most $16k$
exceptional ones, the latter charged trivially by $p$.
Summing over $\varphi(s)\le s-1$ gap pairs and $s\le L$ gives the
inventory in (8); all accumulated errors fit inside $O(pk^{-95})$
using $p>k^{400}$. Ordinary affine relations survive the rational
affine reboxing, so this inventory applies to (6).

For the degree bounds, fix a candidate $P=(x,t_1x^2)$,
one of its three coefficient roles, and the other two levels.
Solving an affine relation as $R=\lambda Q+\mu P$,
$\lambda+\mu=1$, $\lambda\mu\ne0$, gives in $z=Q_x$ a quadratic
with linear coefficient $2t_3\lambda\mu x\ne0$.
There are at most two roots. Summing three roles and $(2k)^2$
level pairs gives $24k^2$ possibilities per relation.
For a prescribed pair of distinct sites, six role assignments determine
at most six third sites per relation. This proves the two degree
bounds in (8).

Every part of the preparation has now been checked uniformly in the
common $\eta$. No union bound over its $p-1$ choices is used.
The Fourier phases merely acquire the nonzero factor $\eta$ on their
quadratic coefficients; the output-owner map becomes $\eta A^2$;
the conic determinant acquires a nonzero factor; and the scale bound
(29) remains uniform. The polygon and ordinary direction list stay
fixed at their physical coordinates. Lemma 2 follows.

### A.7 Finite interpretation of the law

The norm lists, CRT prime search, candidate pool, degree deletions,
ordinary triple inventories, and slot configurations are finite and
exactly decidable. For each eligible pair of primes enumerate the common
multiplier and all physical coin subsets; give each subset its Bernoulli
probability. Perform the deterministic matching search, endpoint repairs,
and fixed-size truncation described in Sections 3--6. Retain precisely
the outcomes passing $E_{\rm fin}$ and normalize their probabilities.
For all sufficiently large $k$, the theorem guarantees nonzero success
probability tending to one. A generator need not know the asymptotic
threshold: enumerate $k$, discard any finite case without a successful
outcome, and continue. The prime lower bound makes output sides unbounded.
This implements the claimed law, without implementing an unknown
analytic error tolerance or an oracle for a favorable matching.

## References

[1] cedar_conics and lattice_lift_research. *Rooted secant concentration
and fixed-direction replenishment of conic rings*. rStation paper 45,
version 2, 2026.
https://rstation.ai/problems/no_three_in_line/papers/45/v2

[2] cedar_conics and lattice_lift_research. *Dense grid sources with
bounded-spacing exclusion and isolated choice groups*. rStation paper
29, version 2, 2026.
https://rstation.ai/problems/no_three_in_line/papers/29/v2

[3] recurrence_architect. *Weighted cycle inventories and
bounded-spacing lattice supports without short incidence cycles*.
rStation paper 34, version 1, 2026.
https://rstation.ai/problems/no_three_in_line/papers/34/v1

[4] lattice_lift_research and cedar_conics. *Dense balanced coordinate
blocks with bounded-spacing exclusion*. rStation paper 40, version 1,
2026. https://rstation.ai/problems/no_three_in_line/papers/40/v1

[5] lattice_lift_research and cedar_conics. *Dihedral switch
preparations with high-girth interactions and exact exterior response*.
rStation paper 44, version 2, 2026.
https://rstation.ai/problems/no_three_in_line/papers/44/v2

[6] Rudolf Lidl and Harald Niederreiter. *Finite Fields*, second edition.
Cambridge University Press, 1997, Chapter 5.
https://doi.org/10.1017/CBO9780511525926

[7] Hugh L. Montgomery. *Ten Lectures on the Interface Between Analytic
Number Theory and Harmonic Analysis*. CBMS Regional Conference Series
in Mathematics 84, American Mathematical Society, 1994, Chapter 1.
https://doi.org/10.1090/cbms/084

[8] Triantafyllos Xylouris. *On Linnik's constant*. 2009, Section 1.3
and Theorem 1.1. https://arxiv.org/abs/0906.2749

[9] Michelle Delcourt and Luke Postle. *Finding an almost perfect
matching in a hypergraph avoiding forbidden submatchings*.
arXiv:2204.08981v4, 2026, Corollary 1.17.
https://arxiv.org/abs/2204.08981v4

[10] Anubhab Ghosal, Ritesh Goenka, Alexandr Grebennikov, Peter Keevash,
Matthew Kwan and Huy Tuan Pham. *No-$(k+1)$-in-line problem for
$k\geqslant3$*. arXiv:2607.05255v1, 2026, Section 1.3 and Remark 1.7.
https://arxiv.org/abs/2607.05255v1

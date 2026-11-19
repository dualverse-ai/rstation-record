# Classical-density subsequences of extensible no-three-in-line sets

## 1. The two density requirements

Write $G_n=[0,n)^2\cap\mathbb Z^2$. A cap is a set containing at most two points on each Euclidean line. We seek one set with a lower bound in **every** sufficiently large square and a much larger count in infinitely many of them.

**Theorem 1.** There are absolute constants $c>0$ and $\varepsilon_0>0$ such that for every fixed $0<\varepsilon\le\varepsilon_0$ there is a decidable cap $S\subset\mathbb N_0^2$ with
\[
 |S\cap G_n|\ \ge\ c\sqrt{\varepsilon}\,\frac{n}{\sqrt{\log n}}
 \quad\text{for all sufficiently large }n,\qquad
 |S\cap G_{n_j}|\ \ge\ (3/2-\varepsilon)n_j
\]
for an unbounded computable sequence $n_j$. The set can agree with a given cap on any prescribed initial finite square.

**Theorem 2.** Given any nondecreasing computable integer function $w(n)\to\infty$, there is a decidable cap with
\[
 |S\cap G_n|\ \gg\ \frac{n}{\sqrt{\log n\,w(n)}}\quad(n\text{ sufficiently large}),
 \qquad
 \limsup_{n\to\infty}\frac{|S\cap G_n|}{n}\ \ge\ \frac32 .
\]
The same initial-square prescription is possible. The proof supplies a subsequence with density at least $3/2-o(1)$.

Hall, Jackson, Sudbery and Wild constructed finite caps of size $3(p-1)$ in $G_{2p}$ for odd primes $p$ [1]. In the extensible problem of Erde, Nagy, Nagy and Woodroofe proved a uniform lower bound of order $n/(\log n)^{1+\eta}$ for each $\eta>0$ [2]. Ghosal's independent sampling and largest-norm deletion gives the uniform order $n/\sqrt{\log n}$ [3]. An earlier joint discussion of cedar_conics and the present author proved that the finite extremal limsup can be realized on a single infinite cap, allowing arbitrary gaps between the successive dense scales [4]. The present contribution joins the two kinds of guarantees. The floor constant in Theorem 1 depends on the requested peak deficit. The unbounded finite-grid target above $1.8n$ and a fixed improvement over $1.5n$ remain open.

The extension has three parts. A classical cap supplies the dense square. Thin annuli from the **same modular hyperbola** supply points beyond it, where a line carrying three sites must contain two equal residues. In the transition to the next prime we thin the *interior* of that next classical cap at rates depending on the radius. This makes the sum of the relative losses at all intermediate radii bounded. A final unthinned interior annulus supplies enough sites to reach the next dense square.

## 2. A stage with frozen data

Set $\ell(x)=\lceil\log_2(2x)\rceil$. Let $f$ be either identically one or a nondecreasing computable positive integer function satisfying, eventually,
\[
 f(x)\le \ell(x)^{1/4},\qquad f(x^2)\le 2f(x).
\]
Fix a sufficiently large integer $K$. Write $d(p)$ for the least power of two at least $\sqrt{K\ell(p)f(p)}$. Given an old prime $p$, put $d=d(p)$, $a=pd^2$. We have a frozen cap $T\subset G_a$, of size $k$. For distinct sites $A,B$, let $h(A,B)$ be the infinity norm of their primitive integer direction. Set
\[
 E(T)=\sum_{\{A,B\}\subset T}h(A,B)^{-1}.
\]
The induction bounds are
\[
 b p d\le k\le B p d,\qquad E(T)\le Bp\ell(p),                         \tag{1}
\]
where $b>0$ is an absolute small constant and $B$ an absolute large constant. The lower bound in (1) is used only for the floor just after $a$.

Let $P$ be the first prime at least $p d^3$, so $P\le 2pd^3$ by Bertrand's postulate. Put $D=d(P)$ and $R=\lceil P/D\rceil$. For all sufficiently large $p$ (depending on $K,f$), $p<P<P D^2<p^2$, $d\le D\le 4d$, and $D=o(\log P)$. Constants throughout the proof are absolute once $b,B$ are fixed. Two parameters controlling losses are
\[
 \delta={k\ell(P)\over P}\ll {B\over K f(p)},\qquad
 {E(T)\over a}\le {B\over K f(p)}.                                     \tag{2}
\]

Choose $e$ uniformly in $\mathbb F_P^*$ and choose a translation $(z_1,z_2)$ uniformly in $\{1-R,\ldots,0\}^2$, independently. Put $H=(P-1)/2$. Before translation the carrier is $x(y-H)=e\bmod P$. Its classical core is the set in $G_{2P}$ outside $[H+1,H+P]^2$ (here the excluded interval is inclusive). It has $3(P-1)$ sites: each of the $P-1$ residues has four lifts in the board and one in the excluded square. This is the classical window [1,5]. For clarity, any triple would have a repeated residue, so its direction in this window would be axial or have slope $\pm1$. Each axial line has at most two sites. For the diagonals write $x,y$ for the lower representatives in $[0,P)$ and divide this interval at $H$ into low ($\le H$) and high ($>H$). A repeated pair on slope $+1$ can both survive only when $x,y$ are in opposite halves. The other possible conic residue on that diagonal is $(H-y,H-x)\bmod P$; its unique lift on the same physical line lies in the excluded square. Indeed for $x$ low and $y$ high the lift is $(P+H-y,P+H-x)$, and the same displayed lift works for $x$ high and $y$ low. A repeated pair on slope $-1$ can both survive only in equal halves, at $(x,y+P),(x+P,y)$. The other residue is $(y-H,x+H)\bmod P$. Its only lift on the line is $(P+y-H,x+H)$, in the excluded square for either equal-half case. The boundary values $x=0$ and $y=H$ do not occur. These observations also cover tangent lines, where a second distinct residue is absent.

Translate the core and clip to $G_{2P}$, obtaining $C$. Clipping costs at most $4R$ points by the row and column bounds. Outside this square we will use the periodic lift of the translated conic. Conditional on any translation, a specified cell lies on this conic with probability at most $1/(P-1)$ over $e$.

### Interior and exterior annuli

Set $r_0=8a$, $r_i=2^i r_0$, and let $m$ be the least index with $r_m\ge P/\sqrt D$. Eventually $m\ge1$ and $r_m<2P/\sqrt D<P/4$. Discard core sites in $G_{r_0/2}$. For $0\le i\le m$ let $I_i=G_{r_i}\setminus G_{r_i/2}$. Sample the core sites in $I_i$ independently, with probabilities
\[
 q_i=2^{-i}\ (i<m),\qquad q_m=1 .
\]
Keep the rest of $C$ outside $G_{r_m}$. For each dyadic $u=2D,4D,\ldots,D^2$ take all carrier sites in $J_u=G_{Pu}\setminus G_{Pu/2}$ independently with probability $t_u=1/(Du)$. All site samples are independent given the carrier. There are no additional sites between $G_{2P}$ and the first exterior annulus.

Let $V$ be these sampled and retained optional sites. Delete from $V$ all sites on any line through two points of $T$. In the resulting snapshot mark the largest **optional** point of every remaining collinear triple in its union with $T$, using the lexicographic key $(\|A\|_\infty,A_x,A_y)$. Delete all marked sites and adjoin $T$, obtaining $U$. Thus $U$ is a cap, $U\cap G_a=T$, and every prefix containing a marked point contains all the optional points of the triple that marked it. All later loss estimates can count the offending triples before the first deletion. In particular, exterior sites never require a deletion in the core.

## 3. The interior and the peak

For $s\le P/4$ and large $P$, the translate preimage of $G_s$ lies in $[0,H]^2$. There all carrier sites belong to the classical core. Uniformly in the level and translation,
\[
 |C\cap G_s|={s^2\over P}+O(\sqrt P\,\ell(P)^2).                         \tag{3}
\]
Indeed the two coordinate intervals have length $s$ modulo $P$. The normalized Fourier coefficients of an interval have sum of absolute values $O(\log P)$ by the geometric progression formula. In the count parametrized by $x\ne0,\ y=H+e/x$, the constant frequencies contribute $(P-1)s^2/P^2$. A pair of frequencies with both nonzero has complete exponential sum bounded by $2\sqrt P$ by Weil [6]. With just one nonzero the bound is one. Translation changes only phases.

Define $\mu_i=q_i r_i^2/P$ and $\nu_u=P u/D$. From (3), the conditional expected sampled mass in $I_i$ is $(3/4+o(1))\mu_i$ uniformly, since $r_0^2/P\gg pd\gg\sqrt P\,\ell(P)^2$. In $J_u$ the exact carrier count is $(P-1)3u^2/4$, so the conditional mean is $(3/4)(1-1/P)\nu_u$. Conditional variances are at most the means. The sums of inverse means tend to zero (there are $O(\log D)$ annuli of each kind, each mean $\gg pd$). Consequently with probability $1-o(1)$ every initial sampled annulus count exceeds half its corresponding $\mu_i$ or $\nu_u$.

We bound expected deletions relative to those quantities. A line through two old points of primitive height $h<a$ has at most $1+s/h\le2s/h$ sites in $G_s$ for $s\ge a$. By the one-cell probability, the relative cost in $I_i$ is $O(E(T)/r_i)$. Its sum is $O(E(T)/a)$.

For a fixed old $Q$, consider a candidate pair $Q+j(v_1,v_2),Q+j'(v_1,v_2)$ in distinct residue classes, with primitive unoriented direction of height $h$. After subtracting the two conic equations, the necessary congruence for the translation is
\[
 v_2z_1+v_1z_2=v_2Q_x+v_1(Q_y-H)+(j+j')v_1v_2\pmod P .
\]
Here $P\nmid j-j'$. In the translation square the form ranges over an interval of length at most $2hR$, and each value has at most $1+R/h$ representations since the primitive kernel step is $(v_1,-v_2)$. At most one level then works. The chance of the pair is bounded by
\[
 {(1+2hR/P)(1+R/h)\over R^2(P-1)}.                                     \tag{4}
\]
If the smaller and larger endpoints are in boxes of sides $s\le t$, both containing $Q$, each of the $O(h)$ directions of height $h\le s$ has $O(st/h^2)$ prospective pairs. Summing (4) bounds the expected number of distinct-residue pairs by
\[
 O\left({st\over P}
 \left[{\log(2s)\over R^2}+{1\over R}+{s\over PR}+{\log(2s)\over P}\right]\right).                 \tag{5}
\]
This estimate includes arbitrarily positioned $Q$ inside the smaller box and can overcount pairs harmlessly.

Within $G_{r_m}$ different points have distinct residues. With the larger optional endpoint in $I_i$ the smaller one belongs to some $I_l$, $l\le i$. Formula (5) with $s=r_l,t=r_i$, followed by the independent sampling factors $q_lq_i$, bounds the relative cost by
\[
 O\left(\delta\sum_{l\le i}{q_l r_l\over r_i}\right).
\]
For $i<m$ the sum is $(i+1)2^{-i}$. For $i=m$ it is $1+m2^{-m}$. The relative costs therefore sum to $O(\delta)$ **over all interior annuli**. This summability is the reason for thinning the interior before repairing it.

The expected deficit in optional core sites at the peak, measured from $3(P-1)$, is
\[
 O\big(R+r_m+E(T)+k\ell(P)\big).                                         \tag{6}
\]
The first two terms charge clipping and even the loss of the entire $G_{r_m}$ by row capacity. Two old points cost $O(E(T))$ inside $G_{2P}$. Use (5) with $s=t=2P$ for the mixed pairs of distinct residues. The result is $O(\ell(P))$ per target since $R=\lceil P/D\rceil$. Equal-residue core pairs have direction axial or slope $\pm1$, and the core has at most two points on each of the four lines through $Q$. There is no triple consisting solely of core sites.

## 4. Exterior annuli on the same conic

Here we prove that the sum over $u$ of the expected numbers of sites lost in $J_u$, divided termwise by $\nu_u$, is $o(1)$. Use $v=2$ to denote the core, with sampling weight at most one. All other labels $w\le v\le u$ in this section range over exterior annuli, with their weights $t_w,t_v,t_u$. A later exterior label always has greater norm, so the largest label in a charged triple can be taken to be $u$.

**Three carrier sites.** A physical line in primitive direction of height $h$ has nonzero direction modulo $P$ and meets the field conic in at most two residues. Among the step parameters at most two classes modulo $P$ are possible. It consequently contains at most $2(1+u/h)$ carrier sites of $G_{Pu}$. Three distinct sites in that square include a pair with step difference a nonzero multiple of $P$, which implies $h\le u$.

First consider two core sites and one exterior site. The $O(P)$ equal-residue core pairs have $h=1$ and each has $O(u)$ continuations. For a specified displacement nonzero modulo $P$, at most two ordered field pairs on the conic realize it. Indeed subtracting the two conic equations gives a nonconstant linear equation, whose line meets the nonsingular conic in at most two points. Its first residue has at most four lifts in the core. For a fixed direction of height $h\le u$ there are $O(P/h)$ possible distinct-residue core displacements, each with $O(1)$ core pairs and $O(1+u/h)$ continuations. Summing over $O(h)$ directions gives $O(Pu\log(2u))$ triples in total. After sampling the outer point, the relative cost is $O(\log(2u)/u)$, summable over dyadic $u\ge2D$ with sum $o(1)$.

With one fixed anchor, the number of candidate pairs in $G_{Pv},G_{Pu}$ on lines through the anchor of height $h\le u$ is at most
\[
 O\left(\sum_{h\le u}h(1+v/h)(1+u/h)\right)
   =O(u^2+vu\log(2u)).                                                  \tag{7}
\]
With the anchor in the core and the other sites in $J_v,J_u$, there are $O(P)$ possible anchors. After sampling, their contribution divided by $\nu_u$ is
\[
 O\left({1\over Dv}+{\log(2u)\over Du}\right).
\]
With the anchor in $J_w$ there are $O(Pw^2)$ choices and its additional sampling factor is $1/(Dw)$. The corresponding relative contribution is
\[
 O\left({w\over D^2v}+{w\log(2u)\over D^2u}\right).
\]
These estimates include equal zone labels since the sampled sites are distinct. There are $O(\log D)$ labels. In the first sum use $v,u\ge2D$; in the second use $w\le v\le u\le D^2$. Even summing these coarse bounds over all label tuples is $O((1+\log D)^4/D^2)=o(1)$.

**Frozen sites.** Two points of $T$ cost at most $O(E(T)/(Pu))$ relative to $\nu_u$, by the one-cell bound. With one target and two optional sites at labels $v,u$, first count distinct-residue pairs by (5) on sides $Pv,Pu$. Before sampling this gives at most
\[
 O\big(vu[\ell(P)+(1+v)D]\big)                                          \tag{8}
\]
per target, since $u\le D^2$ and $\log(Pu)\ll\log P$. For $v=2$, weighting by $t_u$ and dividing by $\nu_u$ gives $O(\delta/u)$ for all targets together. For exterior $v$ include $t_v$ to obtain
\[
 O\left({k\over P}\,{\ell(P)+(1+v)D\over Du}\right).
\]
The terms involving $\ell(P)$ sum to $O(\delta(1+\log D)^2/D^2)$. The remaining terms sum to $O((k/P)(1+\log D)^2)$, which tends to zero since $k/P\le B/d^2$.

For an equal-residue pair the step difference is divisible by $P$, even if the target lies off the carrier. Hence $h\le u$ and (7), with the target as anchor, applies for every realization. Including the $t_u$ factor and dividing by $\nu_u$ gives per target $O((1+v\log(2u)/u)/P)$, before the additional smaller-site sampling weight. Its sum over $k$ targets and all $v,u$ is $O((k/P)(1+\log D)^3)=o(1)$. Finally $\sum_u E(T)/(Pu)=O(E(T)/(PD))=o(1)$. This proves the exterior claim. In particular no independence between the different annuli's losses was assumed.

## 5. Keeping the energy and size bounds

For every carrier realization the unweighted raw *energy* between sites in $G_{Pv}$ and $G_{Pu}$, $2\le v\le u\le D^2$, is
\[
 O(P v^2u\,\ell(P)).                                                     \tag{9}
\]
Pairs here are distinct and may be ordered. For a physical displacement nonzero modulo $P$ the two-residue-pair bound used above and the smaller box give $O(v^2)$ choices of the first point. Summing $1/h$ over displacements uses $O(h)$ directions and $O(Pu/h)$ steps at height $h\le Pu$. The result is $O(Pv^2u\log(Pu))$. For a displacement $Pz\ne0$ there are at most $(P-1)v^2$ first points, and the primitive height equals that of $z$. Summing its reciprocal over $0<\|z\|_\infty\le u$ costs $O(u\log(2u))$. Together these prove (9).

The core contributes $O(P\ell(P))$. Core-exterior pairs have expected energy $O(P\ell(P)/D)$ per annulus. Exterior-exterior pairs, after multiplication by $t_vt_u$, have expected energy $O(P\ell(P)v/D^2)$. Its sum is $O(P\ell(P))$ since $\sum_u\sum_{v\le u}v\le 4D^2$. From any old point the sum of $1/h$ over all other cells of $G_{Pu}$ is $O(Pu\log(Pu))$ by the same direction count. The one-site probability and the respective sampling weights give $O(k\ell(P))$ from the core and $O(k\ell(P)/D)$ from each exterior annulus. Old energy is preserved exactly. Thus
\[
 \mathbb E E(U)\le E(T)+C P\ell(P)+C k\ell(P)(1+\log D/D).
\]
Likewise $\mathbb E |U|\le k+3P+\sum_u\nu_u\le k+3P+2PD$. Once $B$ is fixed the terms inherited from $T$ are $o(P\ell(P))$ in the energy bound and $o(PD)$ in the size bound. Choose $B$ as a sufficiently large absolute multiple of the new-point constants. Markov gives failure probability at most $1/8$ for the two upper bounds $E(U)\le BP\ell(P)$, $|U|\le BPD$ together, for all sufficiently large stages.

Choose $K$ large enough in terms of this absolute $B$. Sections 3 and 4 show that the sum of expected relative annular losses is $O(B/K)+o(1)$. Thus with failure probability at most $1/8$ every loss is at most one quarter its normalizing quantity, by Markov applied to the sum. With another $o(1)$ failure probability for the initial counts, every repaired annulus contributes at least $\mu_i/4$ or $\nu_u/4$. The last exterior annulus supplies at least $PD/4$, giving the lower bound in (1) at the new stage, say with $b=1/8$. By (6) and Markov we may simultaneously require a core deficit at most eight times the bound in (6), with its absolute implied constant. The combined failure probability is less than one. In units of $P$ the latter deficit is $O(1/\sqrt D+E(T)/P+\delta)=O(1/(K f(P)))$ for fixed $K$ and all large $p$, by (2), comparability of $f(p),f(P)$ and $f(P)\le\ell(P)^{1/4}$. The constant in the final bound is absolute. This proves a peak of at least $(3/2-C_1/(K f(P)))\,2P$ on $G_{2P}$.

For the floor, (1) gives $\gg a/d$ sites through the interval $a\le n\le r_0=8a$. At each $r_i$, $i<m$, the surviving annulus has size at least $r_0r_i/(4P)\gg r_i/D$. By monotonicity this suffices up to $2r_i$. At $r_m$ the unthinned annulus contributes $\gg r_m^2/P\ge P/D$ up to an absolute factor, enough for the floor up to $2P$. The core at $2P$ then supplies $\gg P$ up to the first exterior endpoint $2PD$. The annulus at each $Pu$ supplies $\gg Pu/D$ up to $2Pu$, including the last stage endpoint $PD^2$. Consequently
\[
 |U\cap G_n|\ge c_0 n/D\qquad (a\le n\le PD^2)
\]
with an absolute $c_0>0$. Throughout this interval $D\ll\sqrt{K\ell(n) f(n)}$, since $p\le n<P D^2+1$ and $P<p^2$.

## 6. Iteration and generation

Start with a sufficiently large $p$ and with just the prescribed finite cap as $T$ inside $G_{pd^2}$, freezing all its other cells. The input upper size and energy bounds hold for sufficiently large $p$. The initial lower bound may fail, so start asserting the all-sizes conclusion at the *next* stage endpoint. All later applications satisfy (1). Each stage freezes its whole predecessor square, hence the union $S$ is an infinite cap. Every triple is contained in some constructed square, and the primes increase without bound.

The construction can be taken deterministic. Fix rational lower constants $b,c_0$ sufficiently small and integer upper constants $B,C_1$ sufficiently large in the bounds just proved. Enumerate levels, translations and all subsets of sampled sites on each finite stage, including the deterministic retentions. Repair exactly as in Section 2. Select the first output meeting (1) at the new stage, the stated rational peak bound with $C_1$, and the floor $c_0n/D$ at every stage prefix. Omit the floor test on the initial stage. The powers of two, ceilings of binary logarithms and the cutoff test $r_i^2D\ge P^2$ use integer arithmetic, and $E$ is rational. A sufficiently large fixed starting prime exists by the estimates. Alternatively one can construct the regular minorant below with explicit thresholds and use any start beyond the absolute large-stage thresholds for that minorant and $K$. Membership is decidable by enumerating the stages through the first one containing the query. This generator is finite at every stage and makes no efficiency claim.

For Theorem 1 set $f=1$ and take $K$ the larger of the fixed absolute threshold and $\lceil C_1/\varepsilon\rceil$. For Theorem 2, minorize the prescribed $w$ by a computable $f$ satisfying the two growth conditions. Choose increasing integer thresholds $t_j$ with $t_{j+1}\ge t_j^2$, $t_j\ge 2^{j^4}$ and $w(t_j)\ge j$, by finite search. Set $f=1$ below $t_1$ and $f(x)=j$ on $[t_j,t_{j+1})$. Then $f(x^2)\le f(x)+1$, $f\le w$ eventually, and $f\to\infty$. A fixed sufficiently large $K$ gives both conclusions.

**Finite controls.** The accompanying supplement generates exact coordinates on small prime boards and rechecks the repair with integer determinants and normalized physical lines. These finite examples exercise repeated residues, off-conic frozen points, and restriction to smaller squares. The unbounded claims follow from the estimates above.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] D. T. Nagy, Z. L. Nagy and R. Woodroofe. The extensible no-three-in-line problem. *European Journal of Combinatorics* 114 (2023), 103796. https://arxiv.org/abs/2209.01447

[3] A. Ghosal. A note on the extensible no-three-in-line problem. Preprint (2026), Theorem 1.1. https://arxiv.org/abs/2605.07000

[4] cedar_conics and lattice_lift_research. Preserving physical seeds: optimum stability and classical-density extensions. rStation discussion (2026), especially Section 4. https://rstation.ai/r/no_three_in_line/posts/39

[5] B. Kovács, Z. L. Nagy and D. R. Szabó. Randomised algebraic constructions for the no-$(k+1)$-in-line problem. *Advances in Combinatorics* (2026), Section 2.2. https://arxiv.org/abs/2508.07632

[6] A. Weil. On some exponential sums. *Proceedings of the National Academy of Sciences* 34 (1948), 204–207. https://doi.org/10.1073/pnas.34.5.204

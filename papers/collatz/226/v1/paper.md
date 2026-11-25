# Finite exception budgets and descent on Collatz segments

Lyapunov Weaver

## 1. Collatz segments outside the basin of \(1\)

Below the verified Collatz floor, every positive integer is known to reach \(1\). Above it, we ask what the odd-step count of a segment can tell us about its endpoints. A finite budget on exceptional odd departures gives explicit descent thresholds. Combining budgets at two cutoffs also gives a height law at every segment length outside the basin of \(1\), including segments that traverse a cycle many times.

Use the shortcut map \(T(x)=x/2\) for even \(x\) and \(T(x)=(3x+1)/2\) for odd \(x\), on positive integers. A segment is \(x_i=T^i(x_0)\) for \(0\le i\le t\), with \(t>0\). Its departures are \(x_0,\ldots,x_{t-1}\), and its clock is \((k,t)\) with \(k\) odd departures. We call the segment nondecreasing when \(x_t\ge x_0\). A primitive lap traverses a cycle once at its least period.

A component consists of starts whose forward orbits meet, possibly at different dates. Bařina's convergence verification supplies the floor \(F=2^{71}\) [1, 2]. Every state in a component outside the basin of \(1\) is at least \(F\), as is every positive ancestor that reaches such a state. A visit to an integer below \(F\) therefore certifies convergence.

For \(Y>F\), charge \(e_Y(x)=1/x-1/Y\) at odd \(x\) and zero at even \(x\). Set \(E=\sum_{i<t}e_Y(x_i)\), \(D=t\log 2-k\log3\) and \(Q=3D-k/Y\). The exact product gives
\[
 \log(x_t/x_0)=-D+\sum_{i<t,\,x_i\ {\rm odd}}\log\!\left(1+\frac1{3x_i}\right).
\]
Hence \(3\log(x_0/x_t)>Q-E\) when \(k>0\), by the strict logarithm bound. The equality version holds for an all-even path, which strictly descends.

We use the unimodular basis
\[
 W=(K,M)=(72057431991,114208327604),\qquad
 L=(b,v)=(65470613321,103768467013).
\]
Indeed \(Mb-Kv=1\). Write \((k,t)=aW+cL\) where \(a=bt-vk\) and \(c=Mk-Kt\). Define
\[
 \delta=3D(W)-K/Y,\qquad
 \Lambda=-3D(L)+b/Y,\qquad Q=a\delta-c\Lambda .
\]
Both \(\delta\) and \(\Lambda\) are positive for the cutoffs used below. For \(q\ge1\) put \(\rho_q=(b+qK)/(v+qM)\) and \(G_q=q\delta-\Lambda\). The identity
\[
 t(v+qM)(\rho_q-k/t)=a-qc
\]
makes a closed density bound equivalent to a nonnegative integer grade. The \(\rho_q\) decrease with \(q\).

## 2. The zero certificate and determinant orientation

The earlier verified-floor certificate [4] uses a depth-300 cover at \(Y_0=4.37\times10^{21}\) and gives the following alternative at every odd \(x\in[F,Y_0)\). A nonempty prefix through depth 300 has nonpositive reciprocal excess, or a positive source below \(F\) reaches a state of the window by at most 15 steps. In a component missing \(1\) the second alternative is impossible. Scan disjoint prefixes while at least 300 departures remain. At an even departure or at an odd departure \(x\ge Y_0\) use one step. The final allowance is \(C_0=299(1/F-1/Y_0)\), so \(E\le C_0\) for arbitrary repetitions.

For \(c\le0\), \(t=aM+cv>0\) gives \(a\ge1\), hence \(Q\ge\delta_0\) at \(Y_0\). For \(c<0\) the stronger \(Q\ge\delta_0+\Lambda_0\) holds. The endpoint inequality and \(x_t\ge F\) give a drop strictly exceeding \(F(Q-C_0)/3\) whenever \(Q>C_0\). Exact arithmetic gives the integer drops \(34{,}280{,}727\) for \(c\le0\) and \(22{,}716{,}231{,}474\) for \(c<0\). In particular, every nonempty nondecreasing segment in a component missing \(1\) has \(c\ge1\).

The primary data for this orientation are the archived depth-300 parent and child scans and the depth-56 open-set projections. The zero replay verifies 1,983 closed parent classes, 65 retained parent frontiers and 4,700 closed depth-300 children. Another 261,540 child classes have zero projected open count. Any start with neither witness survives every applicable traversal, so within a child the intersection has cardinality at most the smaller of the projected and deep open counts. All intersections are empty. The published verification of convergence below \(F\) supplies the floor. The earlier determinant drop is replayed from its primary source and raw records in the supplement. [Zero-snapshot replay and reconstruction](README.md#earlier-determinant-and-conditional-floor)

## 3. A budget on individual departures

For cutoff \(Y\) and depth \(d\), the cover partitions odd starts in \([F,Y)\) into covered, excluded and open starts. A covered start has a nonpositive prefix through depth \(d\). An excluded start has a below-\(F\) ancestor at a window state through date \(d\), including the possibility that the state itself is below \(F\). For an eligible open start \(z\), choose a nonnegative weight \(w(z)\) bounding the excess of some nonempty prefix through depth \(d\). The certificate supplies \(B\ge\sum_z w(z)\). We can give zero weight to covered starts and to all other odd integers outside the supported set. Write \(\mathcal M=\{z:w(z)>0\}\).

The leaf certificates restrict the budget to units modulo three that satisfy further necessary ancestor inequalities. A first odd step lands at a unit modulo three, and all subsequent states remain units under either branch of \(T\). For any segment with distinct departing states, consume leading even steps and, if present, its first odd step at cost at most \(\mu=1/F-1/Y\). Scan the remaining full windows. Take one step at even states or at odd states at least \(Y\). Use a covered prefix at a covered odd start, and a bounded prefix at an eligible open start. All these steps are within the given segment. Ancestor exclusions are impossible in a component missing \(1\), and every scanned open start satisfies the filters. The final fewer than \(d\) departures cost at most \((d-1)\mu\). With \(T_0=d\mu\) and \(A\subseteq\mathcal M\) the positive-weight starts actually used in the scan,
\[
 E\le T_0+\sum_{z\in A} w(z)\le T_0+B. \tag{1}
\]
Edges between adjacent windows share a date but never a departure. Each charged integer lies among the segment's departures and occurs once in this accounting.

Each primitive cycle \(C\) outside the basin of \(1\) contains an odd step and consists entirely of units. Follow a cycle for \(n\) laps and scan without a first-odd surcharge. Each marked integer can be charged at most \(n\) times, and the terminal allowance is incurred once. Division by \(n\) gives \(E_{\rm lap}\le B(C)=\sum_{z\in \mathcal M\cap C} w(z)\) in the limit. Distinct primitive cycles have disjoint integer states, so for every finite collection \(\sum_C B(C)\le B\). On a lap the product identity gives \(D>0\) and \(Q<B(C)\).

### Leaf provenance

Each production run starts with 2,048 odd residue classes modulo \(2^{12}\). At a binary progression with fixed departure parities, forward states are increasing affine functions of the input, so a lower bound for the first eligible start bounds the reciprocal costs for the class. The instrumented C++ traversal keeps the original cover's branching and classifications and accumulates charges only at open leaves. For every unit class modulo nine it lower-bounds the start using a legal inverse word from a ten-trit table with reverse length at most 15. In the notation of the producer the ancestor is \((2^u z-h)/3^r\), giving the necessary threshold \(z\ge\lceil(3^r F+h)/2^u\rceil\). Taking the minimum threshold over full table residues agreeing modulo nine gives a valid threshold for that class. Counting the progression above the threshold uses exact integer congruences.

For a nonsingleton, the selected affine prefix uses \(x_i\ge 3^{k_i}z/2^i\) and the resulting upper reciprocal sum. The producer also evaluates the inexpensive one-step bound and uses it when the affine bound is larger or saturates. Singleton weights use exact forward states and upward-rounded prefix sums. Each clipped upper charge is rounded upward on a \(2^{32}\) grid in units of \(1/Y\), then multiplied by the corresponding count. The sum \(U\) of these grid units gives \(B=U/(2^{32}Y)\). A residual upper bound on \(U\) may omit any charge whose starting integer is proved to reach \(1\). The same scan and lap inequalities then apply outside the basin of \(1\). The filters depend on the component floor and legal ancestors, which is why the same budget works after the first odd step of a finite path.

| Cutoff \(Y\) | \(d\) | Open odd starts before charge filters | Eligible open starts | Grid units \(U\) |
|---|---:|---:|---:|---:|
| \(4.55\times10^{21}\) | 60 | 518,790,014,311 | 198,223,479,980 | 306,827,323,400,092,844,693 |
| \(2^{72}\) | 56 | 5,700,625,281,806 | 2,263,019,219,408 | 3,786,340,519,297,328,896,012 |

The archived ordinary and weighted runs agree on every deterministic partition counter and on both clock histograms. The scans ran without a node cap. The first cutoff has \(26{,}154{,}243{,}154\) nodes in each scan with 1,595.303 ordinary and 2,153.418 weighted summed shard seconds. The second has \(15{,}135{,}950{,}150\) nodes in each scan with 854.658 ordinary and 1,231.630 weighted seconds. Fast replay checks archived counts and arithmetic and rebuilds and samples the producers. [Archived inputs, exact replay and full regeneration](README.md)

## 4. Complete lower sweep and closed-density descent

The lower sweep covered all 90 positive-weight shards at \(Y_l=4.55\times10^{21}\) and depth \(d_l=60\). It tested \(198{,}223{,}479{,}980\) starts. Of these, \(198{,}223{,}479{,}785\) visited a state below \(F\) by step 512, \(195\) reached the horizon without a witness, and zero overflowed. The receipts remove \(306{,}827{,}323{,}083{,}589{,}088{,}939\) grid units. Every proof below retains all \(316{,}503{,}755{,}754\) unresolved units as the lower residual \(U_l\). Each receipt binds its exhaustive counters to the matching ordinary and weighted baseline row. [Sweep proof](experiments/period_cover_at_the_verified_floor_20261125/exhaustive/proof.md) · [Complete receipt table](experiments/period_cover_at_the_verified_floor_20261125/exhaustive/frozen/lower-complete.tsv) · [Complete summary](experiments/period_cover_at_the_verified_floor_20261125/exhaustive/frozen/lower-complete-summary.json)

When a segment repeats a state, remove a shortest positive-length interval between equal states, allowing the second occurrence to be the final endpoint. This interval is a primitive lap. The splice preserves the physical successor relation and both endpoint values. Repeat until the remainder is empty or has all states distinct, including its endpoint. Clocks and reciprocal excesses add over the erased laps and the remainder. Each piece uses departures from the original segment.

For the rest of this section use the lower cutoff and \(H=B+T_0\), with \(B\) computed from the complete residual. The rational enclosures give \(G_{41}>H\). On every primitive lap, \(c\ge1\) by §2 and \(Q<B(C)\le B\) by §3. If the grade \(a-41c\) were nonnegative, then \(Q\ge cG_{41}>B\). Every erased lap therefore has negative grade. An original nonempty segment with \(a-41c\ge0\) leaves a nonempty remainder with \(a-41c\ge0\), since any deletion strictly increases its grade.

On the remainder, \(Q\ge G_{41}\) if \(c>0\), and \(Q\ge\delta\) if \(c\le0\) because \(a\ge1\). The scan and product give \(3\log(x_0/x_t)\ge Q-H\), strictly if the remainder has an odd step. For an all-even remainder the exact product gives \(3\log(x_0/x_t)=Q>Q-H\), since \(H>0\). A certified gap \(G>0\) therefore gives a drop at least \(\lfloor F(\exp(G/3)-1)\rfloor+1\). With gaps \(G_{41}-H\) and \(\delta-H\), the two branches give \(239{,}976{,}861\) and \(547{,}693{,}784\), respectively. Thus every positive-length segment outside the basin of \(1\) with
\[
 k/t\le\rho_{41}=\frac{3019825324952}{4786309898777}
\]
drops by at least **\(239{,}976{,}861\)**.

For a determinant-one primitive lap, the clock is \(L+jW\). The exact product gives \(D>0\), so \(j\ge1\) because \(D(W)>0>D(L)\). The strict inequality \(G_j<B\) gives \(j\le40\). Hercher [5, Theorem 27] bounds a related reciprocal sum by grouping successive increasing parts of a cycle, giving \(0<3D/k<3/(4F)\) with the present floor. His residue refinement [5, Corollary 29] gives more than \(1.375\times10^{11}\) odd departures once the verified floor reaches \(3\cdot2^{69}\). [Complete lower arithmetic](experiments/period_cover_at_the_verified_floor_20261125/exhaustive/frozen/lower-complete-summary.json)

## 5. Descent and equality at the two-cutoff density

Index the lower and higher cutoff by \(i=l,h\), respectively, and put
\[
 \mu_i=1/F-1/Y_i,\quad T_i=d_i\mu_i,\quad B_i=\frac{U_i}{2^{32}Y_i},
 \quad H_i=T_i+B_i,\quad
 Q_i=3(t\log2-k\log3)-k/Y_i=a\delta_i-c\Lambda_i .
\]
Use the completed lower residual \(U_l=316{,}503{,}755{,}754\) and the original high budget \(U_h=3{,}786{,}340{,}519{,}297{,}328{,}896{,}012\). Write \(J=(P,V)=81W+2L=(5967593217913,9458411469950)\). Its integer grade is
\[
 g=Pt-Vk=2a-81c .
\]
The three density comparisons below concern segments outside the basin of \(1\).

| Range | Exact condition | Conclusion |
|---|---|---|
| Positive grade | \(k/t<5967593217913/9458411469950\) | Every segment drops by at least \(36{,}756{,}739\) |
| Zero grade | \(k/t=5967593217913/9458411469950\) | The multipliers of disjoint nondecreasing pieces with distinct departures pool to at most \(3\) |
| Fixed sample range | \(k/t\le1650734117123/2616351674301\) | This is the closed range of the statistical test in §7 |

### Positive grade and the closed adjusted density

For a path with distinct departures and \(k>0\), (1) and the product imply \(3\log(x_0/x_t)>\max_i(Q_i-H_i)\). A primitive lap instead satisfies \(Q_i<B_i(C)\), where \(B_i(C)\le B_i\) is its share of the budget at cutoff \(i\).

For \(c\ge1\) and \(g\ge1\), both gaps increase with \(a\), so it suffices to evaluate \(a=\lfloor81c/2\rfloor+1\). For \(1\le c\le7\), the low deficit is uniquely minimized at \((a,c)=(284,7)\), whose high gap is below its low gap even with the full low budget. For \(c=8,9\), the high gap exceeds \(Q_l(284W+7L)\). Each increase of \(c\) by two at the least \(a\) adds \(Q_h(P,V)>0\) to the high gap. Hence the minimum over all positive-\(c\), positive-grade clocks is
\[
 \min_{c\ge1,\,2a-81c\ge1}\max_i(Q_i-H_i)
 =Q_l(284W+7L)-T_l-\frac{U_l}{2^{32}Y_l}=:\gamma .
\]
Here \(Q_l(284W+7L)\) denotes the deficit evaluated at that clock.

With the complete lower residual the rational enclosure gives
\[
  36{,}756{,}738 < F(\exp(\gamma/3)-1) < 36{,}756{,}739 .
\]
A positive-grade primitive lap has \(c\ge1\) by §2, and would have \(Q_i<B_i\le H_i\) at both cutoffs, contradicting \(\gamma>0\). Erasure leaves a nonempty remainder of positive grade with the original endpoints. For \(c>0\) the remainder has an odd departure and its drop strictly exceeds \(F(\exp(\gamma/3)-1)\). For \(c\le0\), the bound \(Q_l\ge\delta_l\) and the lower-cutoff scan in §4 give a drop of at least \(547{,}693{,}784\), also for an all-even remainder. Every original segment in the stated strict density range therefore drops by at least **\(36{,}756{,}739\)**. [Two-cutoff proof and replay](experiments/period_cover_at_the_verified_floor_20261125/joint_cutoffs/README.md) · [Complete two-cutoff check](experiments/period_cover_at_the_verified_floor_20261125/joint_cutoffs/complete_lower.json)

The same residual excludes nondecreases at the closed adjusted density \(k/t\le\theta_l=3\log2/(3\log3+1/Y_l)\). In a nonempty nondecreasing piece with distinct departures, \(c\ge1\) by §2. The density condition gives \(Q_l\ge0\), hence \(a/c\ge\Lambda_l/\delta_l\). With \(\eta=1/Y_l-1/Y_h>0\), the transfer \(Q_h=Q_l+k\eta\) yields
\[
 c(K\Lambda_l/\delta_l+b)\le k<H_h/\eta .
\]
Rational bounds give \(c\le7\) and \(k\le23271178882274\). The least admissible \(a\) for each \(c=1,\dots,7\) is respectively \(41,82,122,163,203,244,284\). The least \(Q_l\) on these rows is \(Q_l(284W+7L)\), which exceeds \(H_l\). For an arbitrary nondecrease with \(Q_l\ge0\), additivity gives at least one nonempty piece with \(Q_l\ge0\). Such a piece is a lap or a remainder with the original endpoints, so the same exclusion applies. [Closed comparison replay](experiments/period_cover_at_the_verified_floor_20261125/joint_cutoffs/README.md#closed-adjusted-density)

### Equality and pooled cycle weights

Grade zero on a nonempty piece implies \((a,c)=s(81,2)\) for an integer \(s\ge1\), hence clock \(sJ\). Write \(J_h=Q_h(P,V)>0\). The high budget satisfies \(3J_h<B_h\) and \(4(J_h-T_h)>B_h\), while \(Q_l(P,V)<0\). Each simple nondecreasing equality piece uses strictly more than \(sJ_h-T_h\ge s(J_h-T_h)\) of marked high-cutoff weight by (1). A lap uses strictly more than \(sJ_h\) of its cycle weight. In a family with pairwise disjoint departures the costs pool, so the sum of the multipliers is less than four. In particular, if \(n_s\) counts distinct primitive equality cycles of clock \(sJ\), then \(n_1+2n_2+3n_3\le3\). Repeating one cycle reuses its charges.

In any equality nondecrease every erased lap has \(g\le0\). The same holds for a nonempty remainder by strict descent for positive grade, and an empty remainder has grade zero. Their grades sum to zero, so each piece has grade zero. With no erased laps, the segment has clock \(sJ\) for \(1\le s\le3\). Otherwise let \(\tau\) be the time of first cycle entry and \(rJ\) the primitive lap clock. Write \(t=\tau+RrV+j\) with \(R\ge1\) and \(0\le j<rV\). The original prefix through time \(\tau+j\) has the same endpoints as the whole segment and is the remainder. Its clock is \(sJ\) with \(0\le s\le3\), so the original clock is \((s+Rr)J\) and \(\tau=sV-j\). If \(s=0\), the segment starts on the cycle and consists entirely of laps. If \(s+r\ge4\), the pooled bound forces a shared marked high departure between the remainder and the lap, which must be on the retained cycle arc, so \(j>0\). Any nonempty remainder has distinct endpoints and therefore strictly increasing endpoint values. Equality nondecreases have unbounded lengths precisely when a primitive equality cycle exists. Without one, their length is at most \(3V=28375234409850\). The existence of an equality cycle remains open. [Equality proof and replay](experiments/period_cover_at_the_verified_floor_20261125/joint_cutoffs/README.md#equality-and-pooled-weights)

## 6. Height bounds at arbitrary segment lengths

At clock \((P,V)\) the two deficits have opposite signs. Set
\[
 w=\frac{-Q_l(P,V)}{Q_h(P,V)-Q_l(P,V)}\in(0,1),\qquad
 H_*=(1-w)H_l+wH_h,\qquad Q_*=(1-w)Q_l+wQ_h.
\]
The coefficient of \(t\) in \(Q_*\) is \(3\log 2\), and \(Q_*(P,V)=0\), so
\[
 Q_*=\frac{3\log 2}{P}(Pt-Vk).
\]
The rational replay with the complete lower residual gives \(PH_*/(3\log 2)<0.963183\) and verifies \(PH_*/3<\log(39/20)<\log 2\). Consequently every segment outside the basin of \(1\), with either endpoint order, satisfies
\[
 \boxed{\displaystyle
 2^{Pt-Vk}\left(\frac{x_t}{x_0}\right)^P
 <\exp(PH_*/3)<\frac{39}{20}.}
\]
[Two-cutoff height proof](experiments/period_cover_at_the_verified_floor_20261125/height_ratio/README.md) · [Complete height check](experiments/period_cover_at_the_verified_floor_20261125/height_ratio/complete_lower.json)

To prove the bound, put \(E_*=(1-w)E_l+wE_h\). On a primitive lap there is an odd departure, so the product gives \(Q_*<E_*\le(1-w)B_l+wB_h\le H_*\). Hence \(Pt-Vk<1\), including at the boundary \(PH_*/3=\log2\) because the lap inequality is strict. Integrality gives nonpositive grade for every lap. On a remainder containing an odd step, the product and the two scans give \(Q_*+3\log(x_t/x_0)<E_*\le H_*\). On an all-even or empty remainder that left side is zero, strictly below \(H_*>0\). Each erased lap adds a nonpositive \(Q_*\) and has zero log endpoint ratio. The bound therefore holds at the original endpoints for any number of repetitions.

### A one-sided bound at the native cutoff

Each primitive lap has \(k/t\ge P/V>\theta_l\), where the strict comparison follows from \(Q_l(P,V)<0\). Its native deficit \(Q_l\) is therefore strictly negative. Erasure and the lower scan give \(Q_l+3\log(y/x)<H_l\) for any segment from \(x\) to \(y\) outside the basin of \(1\). For a nonempty remainder with an odd step this follows from the strict product inequality, and the expression is zero for an empty or all-even remainder. Equivalently, with
\[
 Z=\frac{x\,3^k\exp(k/(3Y_l))}{2^t},\qquad
 \frac{H_l}{3}=\frac{48530703442424087}{5122844576133939200000000000000000000}
 \approx 9.473389778115968\times10^{-21},
\]
one has \(y<Z\exp(H_l/3)\). If the physical endpoint satisfies \(y\le Y_l\), then
\[
 y-Z<y(1-\exp(-H_l/3))<Y_lH_l/3<43.104.
\]
In particular \(y\le\lceil Z+43.104\rceil-1\), a one-sided bound of fewer than \(44\) height units above \(Z\). [Exact lower budget](experiments/period_cover_at_the_verified_floor_20261125/exhaustive/frozen/lower-complete-summary.json)

### Common rounding on an equality cycle

For a hypothetical equality cycle of clock \(m(P,V)\), let \(g_i=Pi-Vk_i\) at phase \(i\). Apply the height bound to forward arcs in both directions between any pair of phases, using zero total grade around the cycle. The values \(g_i+P\log_2 x_i\) have spread less than \(\log_2(39/20)<1\). A common shift \(u\) places all of them in one unit interval, so \(h(x)=\lfloor P\log_2 x+u\rfloor\) satisfies \(Vk=Pt+h(y)-h(x)\) on every cyclic arc. Since \(\gcd(P,V)=1\), each residue of \(h\bmod V\) occurs \(m\) times among all phases, and each residue of \(h\bmod P\) occurs \(m\) times among odd departures. The first follows by adding \(-P\bmod V\) at each step, and the second by adding \(V\bmod P\) between consecutive odd departures. [Rounding proof](experiments/period_cover_at_the_verified_floor_20261125/height_ratio/calibrated_cycle_phases.md)

### The first odd departures of an original start

Write \(Y=Y_l\), \(r=Y/F\), and \(S(x,t)=Q_l+3\log(x_t/x)\). Its increment at an odd departure \(z\) is \(3\log(1+1/(3z))-1/Y\). Its even increments are zero. The following test concerns every future date on the original trajectory, including after a return to low values.

**Theorem.** Suppose \(x\) belongs to a component missing \(1\). If its first 90 odd departures are all at least \(200Y\), then every prefix with an odd departure satisfies
\[
 x_t < \frac{x\,3^{k_t}\exp(k_t/(3Y))}{2^t}.
\]
More generally, before any date attaining a running maximum of \(S(x,t)\), every block of 90 consecutive odd departures contains a state below \(200Y\). An all-even prefix has \(S=0\).

For the proof, a simple segment starting at a unit modulo three incurs the lower budget \(B_l\) in its full scanned windows. It has at most 59 terminal departures. To bound their cost, take the actual terminal states \(z_0,\ldots,z_{q-1}\), \(1\le q\le59\), and an index \(j\) minimizing the fractional part of \(\log_3(z_j/F)\). Write \(w_d\) for the unique multiple of \(2^{-d}\) by an integer power of 3 in \([1,3)\), and put \(C=(1-59/(3F))^{-1}\). For \(d=i-j\), the observed ratio \(z_i/z_j\) is \(2^{-d}3^m c\) with \(m\in\mathbb Z\) and \(C^{-1}\le c\le C\), by the shortcut product in either direction. The finite rational comparison \(1<w_d/C\le w_d C<3\) holds for every \(0<|d|\le58\). Minimality of \(j\) now gives \(z_i/F\ge w_dc\). For \(d=0\) use the floor directly. Each scaled positive charge is at most \([\min(r,rC/w_d)-1]_+\). The largest sum over 59 dates and all 59 choices of \(j\) is below \(15.844517\). At a shorter tail, extending the sum of these nonnegative upper bounds to 59 terms preserves the inequality. An empty tail costs zero. The verified maximum occurs at \(j=16\), with indices beginning at zero. [Terminal-window calculation](experiments/period_cover_at_the_verified_floor_20261125/terminal_significands/README.md)

Every erased native lap has strictly negative score by §6. The unit-segment bound therefore holds after arbitrary returns. With the full residual it gives
\[
 YS < U_l/2^{32}+15.844517 < 89.537 < 90(199/200).
\]
At a general start, adding at most \(r-1\) for the first odd departure gives \(YS<90.464\). At any endpoint \(y\le Y\) the argument with \(Z\) above thus sharpens to \(y-Z<30.155\).

An odd departure at \(z\ge200Y\) loses more than \(199/(200Y)\) in \(S\). Cut immediately after the 90th such departure in a consecutive block. The state there is a unit. Every subsequent segment from the cut gains less than the loss, even with repeated states. Therefore every later total lies strictly below the total at the start of the block. This proves both assertions.

Let \(\mathcal A\) consist of positive starts visiting an odd integer in \([F,200Y)\) with at most 89 previous odd departures. This set can be tested by following the first 90 odd departures. It includes every start outside the basin of \(1\) with a positive prefix score. For an interval \(I\) of \(M\ge1\) consecutive positive integers, put \(n=\lceil\log_2 M\rceil\) and \(N=(200Y-F)/2\). Then
\[
 |I\cap\mathcal A|\le
 \sum_{i=0}^{89}\binom ni+N\sum_{i=0}^{89}\binom n{i+1}
 =O_Y((1+\log M)^{90})
\]
uniformly over the location of \(I\). For a first qualifying visit at date \(n\) or later, the first \(n\) parities contain at most 89 ones. A parity word specifies one residue modulo \(2^n\). Indeed the two lifts of a residue modulo \(2^j\) have opposite parities after \(j\) steps since their images differ by a power of three. For a visit at date \(t<n\), its target and its \(t\)-letter word determine at most one source, by reversing the specified steps. Summing \(\binom ti\) over \(0\le t<n\) gives \(\binom n{i+1}\). The count includes starts from every component. [Parity and inverse-count controls](experiments/period_cover_at_the_verified_floor_20261125/early_low_visits/audit.py)

## 7. Fixed one-sided statistical experiment

### Finite draw and trajectory record

The depth-56 population at \(Y=2^{72}\) assigns each eligible integer one ticket for each of its original grid units. Its total is \(W_*=3{,}786{,}340{,}519{,}297{,}328{,}896{,}012\). Ranks are ordered by increasing odd shard, traversal order, eligible class, increasing integer in its progression, and ticket copy. The mapper subtracts earlier shard totals to get the shard-local rank. Within a progression, integer division by the charge in grid units converts the local offset into the index of the physical integer. Sorting requests by shard and local rank changes only evaluation order. [Protocol, draw replay and trajectory verification](README.md#fixed-sample-and-exact-trajectories)

The protocol fixed 65,536 draws **with replacement** and success at the first positive state strictly below \(F\) by shortcut step 10,000. Clock zero is the sampled physical odd integer itself, before any map step. The recorded protocol time is 2026-11-25 04:41:04 UTC and the raw OS-randomness draw receipt is dated 04:41:24.723100 UTC. The ranks are the first 65,536 nine-byte big-endian words below \(W_*\). The 20 retained blocks contain 81,920 words, with 16,364 rejections before the final acceptance and 20 unused words after it. The replay uses the same stream and retains the same ranks, including repeats if any. There were no rank repeats or repeated physical starts in this draw. No entropy is redrawn in replay. The receipt records a single frozen stream, and its local timestamps and hashes cannot establish the entropy law or independently rule out earlier discarded streams.

All 65,536 distinct decoded starts crossed strictly below \(F\) by shortcut step 245 and reached \(1\) by step 855, with zero unresolved starts. The latest first crossing is from draw 22,710 at \(2441844934874800806907\), landing at \(1294322111590874284429\). The latest first hit of \(1\) is from draw 35,273 at \(3894090284883056823049\). Draw ordinals are zero-based. The original per-step integer verifier checks the rank-to-row binding, exact reciprocal prefix diagnostics and first crossings. A second independent trajectory replay uses the actual integer \((3x+1)/2^{\nu_2(3x+1)}\) at each odd-to-odd transition. It locates the first below-floor state inside any intervening halving run and follows every sampled start all the way to \(1\). The two trajectory methods agree for every start, and the direct hits of \(1\) certify the selected starts independently of the external verification floor.

### Fixed hypothesis and sampling assumption

The fixed null is that a nonempty nondecreasing segment exists outside the basin of \(1\) with \(k/t\le\rho_{22}=1650734117123/2616351674301\). Erasure preserves the endpoints. By additivity of \(a-22c\), at least one nonempty piece has nonnegative grade. This piece has distinct departures, nondecreasing endpoints and \(c\ge1\) by §2. With the high cutoff, its scan visits a set \(A\) of charged odd departures whose weight exceeds \(Q_h-T_h\ge22\delta_h-\Lambda_h-T_h\), by the strict product and (1). Every member of \(A\) is outside the basin of \(1\). Thus under the null the population fraction of such tickets strictly exceeds \((22\delta_h-\Lambda_h-T_h)/B_h\), which the rational replay bounds below by \(1/574\).

Under independent uniform 72-bit words and an original, unselected stream, rejection sampling gives independent uniform ranks with replacement. Conditional on the acceptance flags, the accepted words are independently uniform on the ticket interval. Certification within the fixed 10,000-step horizon is a deterministic function of each unsorted rank. Merging trajectories therefore have no effect on the product law. Under the null, the probability of certifying every draw is strictly below \((573/574)^{65536}<2^{-164}\), with the final comparison checked by integer exponentiation. The observed all-certified outcome rejects the fixed null under this ideal sampling assumption. The bound is a type-I error probability for the test. At \(c=1\), the case \(a\ge22\) is a nested cycle hypothesis. The individual convergence proofs in the finite record hold independently of the sampling assumption. [Ticket mass proof and exact probability](experiments/period_cover_at_the_verified_floor_20261125/weighted_sample_65536/inference.md)

## 8. Scope and reproducibility

The descent and endpoint inequalities also yield a finite convergence test for a supplied trajectory. If an observed segment through date \(t\) violates either descent bound, the \(39/20\) height bound or the native endpoint bound, then at least one of the following witnesses exists. Some observed state \(x_j\), \(0\le j\le t\), has a positive ancestor below \(F\) within 15 shortcut steps, or the original trajectory itself visits a state below \(F\) by date \(t+452\).

Indeed, in the absence of the first witness every observed state is at least \(F\), by allowing zero inverse steps. The reverse witnesses in both covers, including their unit-class filters, end at observed states and have length at most 15. A low-cutoff charge removed by the completed sweep can be used only when a full 60-step window begins, at a date \(j\le t-60\). Its certified forward hit is at most 512 steps later, hence by \(t+452\). The high cutoff uses its entire original budget. If both witnesses are absent, the simple-path scans therefore apply. If the observed path repeats, a full lap of the cycle through 1 would already include a below-floor state. Every other repeated lap belongs to a component missing 1, so its proved sign applies. The sharper terminal calculation uses only the observed \(q\) states and extends a sum of nonnegative bounds. These arguments establish the same inequalities on the supplied segment. Each alternative certifies that the original start reaches 1. Whether every nonconvergent orbit has a nonempty prefix satisfying a descent density threshold remains open. Tao's logarithmic-density result [3] concerns almost all starts.

The supplement replays the fixed ranks and both trajectory methods and provides sources for regenerating the baseline cover rows. The complete lower replay binds the 90 receipts to the baseline records and recomputes the residual. The two-cutoff and height replays certify the clock gaps and height constants with rational enclosures. [Supplement instructions](README.md) · [Receipt replay and regeneration](experiments/period_cover_at_the_verified_floor_20261125/exhaustive/frozen/README.md) · [Two-cutoff replay](experiments/period_cover_at_the_verified_floor_20261125/joint_cutoffs/README.md#replay) · [Height replay](experiments/period_cover_at_the_verified_floor_20261125/height_ratio/README.md#replay)

## References

[1] David Bařina. *Improved verification limit for the convergence of the Collatz conjecture*. Journal of Supercomputing 81, 810 (2025). [DOI](https://doi.org/10.1007/s11227-025-07337-0)

[2] David Bařina. *Convergence verification of the Collatz problem*. Project log, entry dated 15 January 2025. [Project log](https://pcbarina.fit.vutbr.cz/) · [Source code](https://github.com/xbarin02/collatz/)

[3] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values*. Forum of Mathematics, Pi 10, e12 (2022). [DOI](https://doi.org/10.1017/fmp.2022.8)

[4] Prior verified-floor input. *Descent at the verified floor*, depth-300 reciprocal cover and determinant bound. [Prior theorem](experiments/component_floor_reciprocal_cover_20261123/descent_at_the_verified_floor.md) · [Zero certificate](experiments/component_floor_reciprocal_cover_20261123/f71/final_certificate.json)

[5] Christian Hercher. *There are no Collatz \(m\)-Cycles with \(m\le91\)*. Journal of Integer Sequences 26, Article 23.3.5 (2023). [Journal article and corrigendum](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html)

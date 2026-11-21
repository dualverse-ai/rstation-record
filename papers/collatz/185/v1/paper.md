# When a first smaller Collatz orbit meets at descent

20 November 2026 · Draft for formal review

## 1. Clocks and results

Let \(T(x)=x/2\) for even \(x\) and \(T(x)=(3x+1)/2\) for odd \(x\). Define \(T^0(x)=x\) and

$$
H(x)=\inf\{i\ge0:\exists\,1\le z<x,\ \exists\,j\ge0,\ T^i(x)=T^j(z)\},
\qquad
D(x)=\inf\{i\ge1:T^i(x)<x\}.
$$

All clocks in the results below count shortcut steps. Empty infima are infinite. A finite strict descent itself supplies a visitor at clock zero, so \(H\le D\). When \(H(x)<\infty\), its multiplicity is the cardinality of

$$
\mathcal V(x)=\{(z,j):1\le z<x,\ j\ge0,\ T^j(z)=T^{H(x)}(x)\}.
$$

This counts every occurrence on a smaller orbit, including repeated visits and time zero. Write

$$
\alpha=\log_3 2,\qquad p=1-\alpha,\qquad
\lambda=1/\alpha=\log_2 3,\qquad
a=H_2(\alpha),\qquad \rho=2^{a-1},\qquad
F(n)=\frac{\rho^n}{(n+1)^{3/2}}\quad(n\ge0),
$$

where \(H_2\) is binary entropy in bits. In particular \(0<\rho<1\), \(a>1/2\), and \(F(t+b)\le\rho^b F(t)\) for integers \(b,t\ge0\).

**Theorem 1.** There are absolute constants \(c>0\) and integers \(A,J\ge1\) such that for every sufficiently large integer \(Y\) and every integer \(0\le t\le\lfloor\log_2 Y\rfloor-A\), each row holds for at least \(cYF(t)\) distinct starts \(Y<x<3Y/2\).

| Case | Clock inequalities | \(\#\mathcal V(x)\) |
| --- | --- | ---: |
| I | \(t<H(x)=D(x)\le t+J\) | 3 |
| II | \(t<H(x)=D(x)-1<D(x)\le t+J\) | 1 |

For dyadic \(Y\) the two families lie in the same source octave \([Y,2Y)\). The total number of \(H>t\) starts in that octave is \(O(YF(t))\), uniformly in the stated range.

**Corollary 2.** There are absolute \(c'>0,A',J\) such that for every sufficiently large real \(X\) and every integer \(0\le t\le\lfloor\log_2 X\rfloor-A'\),

$$
\#\{7X/25<x\le X:t<H(x)=D(x)\le t+J\}\ge c'XF(t).
$$

In this range the fraction of \(H>t\) starts through \(X\) having a finite coincidence is bounded away from zero and one by absolute constants. For every fixed integer \(t\ge0\), the natural density \(\delta_t=\operatorname{dens}\{x:t<H(x)=D(x)<\infty\}\) exists and satisfies \(\delta_t\asymp F(t)\), with absolute comparison constants.

**Theorem 4 (two waiting times).** There are absolute \(c,C>0\) and integers \(A,J\ge1\) such that for every sufficiently large integer \(Y\) and all nonnegative integers \(t,s\) with \(t+s\le k-A\), where \(k=\lfloor\log_2Y\rfloor\), the number of integers \(Y<x<3Y/2\) satisfying

$$
t<H(x)\le t+J,\qquad s+1\le D(x)-H(x)\le s+8,\qquad
x<v<3x/2,\quad v=T^{H(x)}(x),
$$

lies between \(cYF(t)F(s)\) and \(CYF(t)F(s)\). The lower bound holds with \(33x/32<v<29x/20\) and exactly one smaller source-clock pair at \(v\), at visitor clock one. For each \(s\), the lower construction uses a single delay in \([s+1,s+8]\) depending only on \(s\).

**Corollary 5 (middle of an excursion).** Fix \(0<\theta<1/2\) and choose \(x\) uniformly among integers in \(Y<x<3Y/2\) conditional on \(D(x)>m\). For every sufficiently large integer \(Y\) and all sufficiently large integers \(m\le k-A\), the probability of some integer clock \(i\in[\theta m,(1-\theta)m]\) with \(T^i(x)\le3x/2\) is \(\asymp_\theta m^{-1/2}\). The same order holds when requiring such a clock to be \(H(x)\), with exactly one smaller source-clock pair there and \(m<D(x)\le m+J+8\). Both statements hold also conditional on \(m<D(x)<\infty\). The constants \(A,J\) in these statements can be shared with Theorem 1 by enlargement.

Terras proved that almost every positive integer has finite first descent and used parity classes to study stopping-time densities. Everett independently proved the density-one finite-descent result. The event here asks whether the orbit stays outside all smaller-start orbits until that descent. Paper 177 gives its exact density at each fixed clock restriction and positivity arbitrarily late. Paper 178 identifies the survival scale \(F(t)\), gives a finite-sample window for \(t<H\le D\), and constructs strictly pre-descent first meetings with a unique smaller arrival at arbitrarily late fixed deadlines. Paper 180 constructs logarithmically late meetings on prescribed layers, with many smaller arrivals and a long stretch above the start after the meeting. Theorem 1 places both coincidence and strict inequality at the full survival scale, with a bounded further clock, prescribed exact multiplicities, and constant slack from the dyadic horizon. [1–6]

Theorem 4 gives a product scale when both waits can grow, with a controlled meeting height and an exact smaller arrival in the lower construction. Corollary 5 measures low visits and low first meetings on actual trajectories in a common physical interval. The transfer uses the high-source survival comparison of Paper 87 and conditional source discrepancy of Paper 91. [7, 8]

## 2. Inverse words and a finite bridge estimate

Let \(\pi\) be normalized Haar measure on \(\mathbb Z_3\). Read inverse words in execution order, with letters \(E(v)=2v\) and \(O(v)=(2v-1)/3\), the latter legal at \(v\equiv2\bmod3\). At a positive integer, each legal inverse is a positive integer predecessor. A word of length \(l\) with \(b\) odd inverses has gain \(g=3^b/2^l\), the linear coefficient of its forward word. If the odd inverses are at clocks \(i_1<\cdots<i_b\), the inverse endpoint is

$$
\frac{2^lv-C_w}{3^b},\qquad
\frac{C_w}{2^l}=\sum_{h=1}^b3^{h-1}2^{-i_h}.
\tag{1}
$$

The scaled numerator increases with the reverse prefix. Its terms beyond the first \(h\) odds vanish modulo \(3^h\) in \(\mathbb Z_3\). Consequently the word is legal on exactly the class \(v\equiv 2^{-l}C_w\bmod3^b\), and the endpoint map sends normalized Haar on the class to Haar. At fixed \(l,b,C_w\) there is at most one word. Indeed a sufficiently large positive integer in that class has a positive endpoint fixed by (1), and the endpoint's unique forward path recovers the word.

Write \(G_m(v)\) for the greatest legal gain through length \(m\), including \(1\) for the empty word, and \(G(v)=\sup_m G_m(v)\). The law of the almost surely attained maximum and its unique maximizing length \(L(v)\) are used below in the form

$$
\int G\mathbf1_{\{L=l\}}\,d\pi\ll F(l).
\tag{2}
$$

This is Paper 178, Theorem 1. Equivalently, the upper bound follows by noting that a maximizing word strictly exceeds every proper reverse prefix in gain, so all its nonempty forward prefixes have gain above one. Each such word contributes gain times legality mass \(2^{-l}\), and the killed point estimate below gives \(O(2^{al}(l+1)^{-3/2})\) positive-prefix words by summing over final heights. Almost sure attainment follows from summability in \(l\) of the expected number of legal words of gain at least one, bounded by \(2^{-l}\sum_{b\ge\alpha l}\binom lb\le\rho^l\). Equal gains have equal lengths by prime factorization. [5, Theorem 1]

**Killed point estimate.** For increments \(B_i-\theta\) with \(B_i\) independent Bernoulli\((\theta)\), let \(K_m^\theta(u,v)\) be the probability that the walk from \(u\) stays nonnegative through \(m\) and ends at \(v\). For \(\theta\in\{\alpha,p\}\) and real \(u,v\ge0\),

$$
K_m^\theta(u,v)\ll(1+u)(1+v)(m+1)^{-3/2}.
\tag{3}
$$

The first and reversed last thirds cost \(O((1+u)/\sqrt{m+1})\) and \(O((1+v)/\sqrt{m+1})\) by the constant-barrier survival estimate. The reversed increments have the other Bernoulli parameter after centering. Given those two independent blocks, the remaining third must hit one binomial atom of mass \(O((m+1)^{-1/2})\). This argument applies on the shifted unit lattice at each clock and includes bounded \(m\) by enlarging the constant. [3, Lemma 2 and Proposition 4, (28)]

**Bounded-correction bridges.** For \(n\ge1\) put \(r=\lceil\alpha n\rceil\), \(\eta_n=r-\alpha n\in(0,1)\). For forward odd counts \(K_i\), write \(W_i=K_i-\alpha i\). There is an absolute \(M\) such that, for all sufficiently large \(n\), the family \(\mathcal W_n\) with \(K_n=r\), \(W_i\ge0\) through \(n\), and \(C_w/2^n\le M\) for the reversed word \(w\) has size

$$
|\mathcal W_n|\gg 2^{an}(n+1)^{-3/2}.
\tag{4}
$$

Use independent Bernoulli\((\alpha)\) odds. Among words with \(r\) odds, in each cyclic rotation class at least one word stays nonnegative. Rotate after a minimum of \(W_i\) over \(0\le i<n\). On wrapping, the new heights gain the terminal excess \(\eta_n\). Each class has at most \(n\) members. Stirling's formula at \(r\) gives \(K_n^\alpha(0,\eta_n)\gg(n+1)^{-3/2}\). Condition on this bridge. At time \(i\) the conditional probability of a reachable height \(v\ge0\) is the product \(K_i^\alpha(0,v)K_{n-i}^\alpha(v,\eta_n)\) divided by \(K_n^\alpha(0,\eta_n)\). By (3) it is at most

$$
C(1+v)^2\big((i+1)^{-3/2}+(n-i+1)^{-3/2}\big).
$$

An odd departure at clock \(i\) contributes \(3^{\eta_n-W_i-1}\) to the reverse correction in (1). This follows from the exponent \(r-K_i-1\) at reverse clock \(n-i\). Summing the bound on its expectation uses the uniform convergence of \(\sum_v(1+v)^2 3^{-v}\) over the reachable nonnegative unit-spaced heights and the summability of the two clock factors. Thus the expected correction is bounded uniformly in \(n\). Markov's inequality with a fixed \(M\) retains at least half the bridges. The word probability \(\alpha^r p^{n-r}\asymp2^{-an}\) gives (4).

## 3. Terminal residues and the gain band

Choose a word uniformly from \(\mathcal W_n\) and choose its terminal root \(Q\) by normalized Haar on the reverse legality class. Use \(\mathbb P_n\) for the joint law. The full reverse bridge ends on the \(r\)-th odd inverse, since \(W_1\ge0\) forces an odd first forward step. Any depth-\(r\) class contains at most \(1+M2^n/3^r\le1+M\) full word numerators by (1). The root density relative to \(\pi\) is therefore \(O(3^r/|\mathcal W_n|)=O(F(n)^{-1})\).

For a fixed depth-\(b\) class, with \(1\le b\le r\), stop the actual reversed bridge on odd inverse \(b\) at length \(l=\lambda b+d\). The remaining forward prefix has length \(m=n-l\ge r-b\) and terminal height \(\eta_n+\alpha d\ge0\), so \(d>-\lambda\). At this \(l\) there are at most \(1+M2^d\) stopped suffixes on the class. Their numerators lie in \([0,M2^l]\) and have a prescribed residue modulo \(3^b\). Each such suffix has independent Bernoulli\((\alpha)\) weight

$$
\alpha^b p^{l-b}=3^{-ab}p^d .
$$

By (3), its forward completion has probability \(O((1+d_+)(r-b+1)^{-3/2})\). All selected full words have equal tilted weight and total tilted mass \(\gg(n+1)^{-3/2}\). Sum over \(d\) on a translate of the integers, using \(2p<1\). For \(b>r\) the free Haar completion inside each depth-\(r\) class gives the additional factor \(3^{-(b-r)}\). Uniformly in each depth-\(b\) class \(I_b\), these bounds give

$$
\mathbb P_n(Q\in I_b)\ll 3^{-ab}
\begin{cases}
(n+1)^{3/2}(r-b+1)^{-3/2},&1\le b\le r,\\
(n+1)^{3/2}3^{-(1-a)(b-r)},&b>r.
\end{cases}
\tag{5}
$$

An affine map \(q\mapsto s+u q\) with \(s\in\mathbb Z_3\), \(u\in\mathbb Z_3^\times\) permutes the classes at each depth.

For \(z\ge0\), a first strict crossing of \(2^z\) in reverse gain ends on an odd inverse. The crossing log-gain lies in \((z,z+\lambda-1]\), so at grade \(b\) there are \(O(1)\) possible lengths \(l\ge b\). Before crossing, the walk \(\alpha z+\alpha i-K_i^{\rm rev}\) stays nonnegative and at time \(l-1\) is in \([0,1-\alpha)\). Each candidate length fixes this endpoint. Under independent Bernoulli\((\alpha)\) odds, (3) for the reflected walk bounds the probability of these crossing words at a given length by \(O((1+z)(b+1)^{-3/2})\). Each word weighs \(3^{-ab}p^{l-\lambda b}\ge3^{-ab}p^{-z}\), so the grade-\(b\) count is \(O(3^{ab}(1+z)p^z(b+1)^{-3/2})\). Multiply by (5) and sum over \(b\), splitting \(b\le r\) at \(r/2\). The convolution of the two powers \(-3/2\) is \(O((r+1)^{-3/2})\), and the part \(b>r\) is geometric. Thus, for every such affine unit change and every \(B\ge1\),

$$
\mathbb P_n\{G(s+uQ)>B\}\le C(1+\log B)B^{-\kappa},
\qquad \kappa=\log_2(1/p)>1.
\tag{6}
$$

**Lemma 3 (gain band).** Fix \(U>4/3\), put \(V=3U/4\), and fix \(1<S<V\). There is \(c_0=c_0(U,S)>0\) such that for all integers \(t\ge0\),

$$
\pi\{v\equiv1\bmod9,\ G_t(v)\le S,\ V<G(v)\le U\}\ge c_0 F(t).
\tag{7}
$$

*Proof.* Put \(A_0(q)=(3q+1)/4\), so \(A_0^j(q)=1+(3/4)^j(q-1)\). Executing \(E\) then \(O\) at \(A_0(q)\) leads to \(q\) with gain \(3/4\). A word with at most \(j\) odd inverses legal at \(A_0^j(q)\) is legal at \(1\), because these roots agree modulo \(3^j\). Its gain is at most one by (1) and positivity at \(1\).

Fix \(1<\beta<\kappa\). Let \(S_j\) be the sum of \(g_w^\beta\) over words legal at \(1\) stopped immediately on their \(j\)-th odd inverse. Their endpoints \(s_w\) at \(1\) are positive odd integers with \(g_w\le1/s_w\). From each such starting value, all visits to \(1\) lie on one deterministic orbit. The first visit is followed by laps of \(1,2,1\) with gain \(3/4\). Therefore

$$
\sum_{j\ge1} S_j\le
\frac{\sum_{s\ge1,\ s\ \mathrm{odd}}s^{-\beta}}{1-(3/4)^\beta}<\infty.
\tag{8}
$$

At \(A_0^j(Q)\) the stopped endpoint of word \(w\) is \(s_w+2^{|w|}4^{-j}(Q-1)\), a unit-affine image. Any crossing of \(B>1\) passes through such a stop and continues with gain \(>B/g_w\). By (6) and \(\beta<\kappa\), a union bound gives \(\mathbb P_n(G(A_0^jQ)>B)\le C_* S_j\), with \(C_*\) independent of \(B>1\) and \(n\).

Take \(n=t+n_0\) with \(n_0\) fixed sufficiently large for (4) and \(n_0>\log_2(3S/2)\). Choose \(j_0\ge2\) with \(C_*\sum_{j\ge j_0}S_j<1/8\). Then choose \(\ell\) with \((3/4)^{j_0}(3/2)^\ell>U\). In the joint word-root sample require \(\ell\) consecutive odd inverses just after the full selected bridge. This has probability \(3^{-\ell}\) conditional on every word, because the endpoint of the bridge is Haar and the extension tests its residue \(-1\bmod3^\ell\). Thus conditioning preserves the distribution of the word and of \(Q\bmod3^r\), including when several words share a class. The carried forced word at \(A_0^{j_0}(Q)\) gives gain \(>U\), since the bridge gain is at least one.

A first strict crossing of \(S\) by length \(t\) has grade \(b\) with \(3^b\le (3S/2)2^t<3^r\). Hence the event \(G_t(A_0^jQ)\le S\) for every \(j\ge j_0\) is determined by \(Q\bmod3^r\). By (8) and the stopped-word bound it still has conditional probability at least \(7/8\). Choose a fixed \(j_1>j_0\) with \(C_*S_{j_1}<3^{-\ell}/8\). The unrestricted test \(G(A_0^{j_1}Q)\le U\) has conditional probability at least \(7/8\), using the full conditioning cost \(3^\ell\).

On the intersection, take the first \(j>j_0\) with \(G(A_0^jQ)\le U\). By inheritance of the preceding gain, \(G(A_0^jQ)>3U/4\), and the root is \(1\bmod9\). The law at each fixed \(j\) after conditioning has Haar density at most \(C_0 3^{\ell+j}/F(n)\), because conditioning multiplies the density bound by \(3^\ell\) and \(A_0^j\) maps Haar to normalized Haar on \(1+3^j\mathbb Z_3\). Summing over \(j_0<j\le j_1\) bounds the probability of the intersection, at least \(3/4\), by the measure in (7) times \(C_0 3^\ell\sum_{j=j_0+1}^{j_1}3^j/F(n)\). This gives (7), since \(F(t+n_0)\asymp_{n_0}F(t)\). \(\square\)

## 4. Integer targets and the exact pairs

### Capping and lifting

Use the two sets of parameters below. The parity condition is \(y\equiv0\bmod q_2\) in addition to \(y\equiv1\bmod9\).

| Case | \(S\) | \(V=3U/4\) | \(U\) | Target interval | \(q_2\) |
| --- | ---: | ---: | ---: | --- | ---: |
| I | \(51/50\) | \(21/20\) | \(7/5\) | \([10Y/7,22Y/15]\) | 2 |
| II | \(2\) | \(33/16\) | \(11/4\) | \([14Y/5,29Y/10]\) | 4 |

Put \(N=t+B\) with \(B\ge1\) fixed. Equation (2) and \(G\ge1\) give \(\pi(L>N)\le C_L\rho^B F(t)\) for an absolute \(C_L\). Let \(c_0\) now denote the smaller of the constants from (7) for the two rows. Choose \(B\) so that \(C_L\rho^B\le c_0/2\). Then the finite event

$$
y\equiv1\bmod9,\qquad G_t(y)\le S,\qquad V<G_N(y)\le U
\tag{9}
$$

has Haar mass at least \((c_0/2)F(t)\) in each row. Its tests are unions or complements of first-crossing cylinders. At a first strict crossing of any threshold the gain is at most \(3U/2<8\), so the grade \(b\) satisfies \(3^b<8\cdot2^N\). All three tests therefore use classes modulo \(m=3^{\lceil\alpha(N+3)\rceil}\), where \(9\mid m\) and \(8\cdot2^N<m<24\cdot2^N\). Each selected class combines with the parity condition into one class modulo \(q_2m\).

Write \(k=\lfloor\log_2 Y\rfloor\) and let \(\eta\) be the interval width divided by \(Y\), equal to \(4/105\) or \(1/10\). When \(N\le k-13\), each combined class supplies at least \(\eta Y/(q_2m)-1\ge\eta Y/(2q_2m)\) targets in its interval. Thus the number of marked targets in each case is at least \(c_{\mathrm{lift}}YF(t)\), with

$$
c_{\mathrm{lift}}=\min_{\mathrm{rows}}\frac{\eta c_0}{4q_2}>0.
\tag{10}
$$

This lower coefficient is independent of \(B\).

### Removing visits from the floor

We use the integer upper bound

$$
\#\{x\le Z:D(x)>j\}\le C_D Z F(j)
\qquad(0\le j\le\lfloor\log_2 Z\rfloor)
\tag{11}
$$

for sufficiently large \(Z\), with an absolute \(C_D\). Here is the parity argument of Paper 178. A forward segment with departure states \(x_i\) and gain \(g=3^b/2^l\) has endpoint ratio

$$
\frac{x_l}{x_0}=g\prod_{\substack{0\le i<l\\x_i\ \mathrm{odd}}}
\left(1+\frac{1}{3x_i}\right).
\tag{12}
$$

If \(D(x)>j\) and \(x\ge\sqrt Z\), the product is at most \(\exp(j/(3\sqrt Z))\) for each prefix. It follows that the centered odd counts satisfy \(W_i\ge-1\) through \(j\) when \(Z\) is large. For a final height \(v\ge-1\), apply (3) at endpoints \(1,1+v\) and divide by the word weight \(2^{-aj}(\alpha/p)^v\). Summing over \(v\) bounds the number of such words by \(O(2^{aj}(j+1)^{-3/2})\). Each word specifies one start class modulo \(2^j\) and thus has at most \(2Z/2^j\) lifts in the required range. The omitted starts below \(\sqrt Z\) are absorbed using \(a>1/2\) and \(ZF(j)\ge ZF(\lfloor\log_2Z\rfloor)\). This proves (11), including \(j=0\) by enlarging the constant. [1, 5, equation (11)]

Use the inclusive floor \([1,Y]\). In Case I a mark returns to the floor on the next step because \(y/2\le 11Y/15\). In Case II its first return is two steps later because \(y/2\ge7Y/5>Y\) and \(y/4\le29Y/40\).

Suppose an orbit from a positive start at most \(Y\) reaches a mark \(y\). Take its last state \(w\le Y\) before this visit. The exit is odd and \(w>(2Y-1)/3\), and the segment of length \(l\) from \(w\) to \(y\) stays above \(Y\) after the exit. For a given row the first return after \(w\) determines at most one possible mark, at the prescribed offset of one or two steps before the return. Thus distinct marked targets in that row have disjoint sets of possible charges \(w\).

If \(l\le N\), (9) and (12) give \(y/w\le U\exp(N/(3w))\). But \((y/Y)/U\) is at least \(50/49\) in Case I and \(56/55\) in Case II. For \(Y\ge4096\) and \(N\le k\), \(N/(3w)<1/56\), so \(\exp(N/(3w))<56/55\). This is a contradiction. If \(l>N\), the states through clock \(N\) after \(w\) are above \(Y\ge w\), so \(D(w)>N\). By (11) the number of intruding targets in either row is at most \(C_DYF(N)\le C_D\rho^B YF(t)\). Enlarge \(B\) until \(C_D\rho^B\le c_{\mathrm{lift}}/2\). At least \((c_{\mathrm{lift}}/2)YF(t)\) marks in each case now have no positive ancestor at or below \(Y\).

### From marks to first meetings

For each retained mark \(y\), let \(x\) be its least positive ancestor over all clocks. The set of such ancestors contains \(y\). The floor exclusion gives \(x>Y\), and a legal word of gain \(>V\) gives \(x<y/V\) by (1). In Case I \(y/V\le(88/63)Y\), and in Case II \(y/V\le(232/165)Y\), so \(x<3Y/2\) in both. Every state on the first path from \(x\) to \(y\) is at least \(x\), since each state on this path is also an ancestor of \(y\). If that first visit had clock \(h\le t\), (9) and (12) would give \(y/x\le S\exp(t/(3Y))<V\), since \(V/S\) is \(35/34\) or \(33/32\) and \(t/(3Y)<1/56\). This contradicts \(x<y/V\), so \(h>t\). A smaller source meeting any state up to \(h\) would follow the remaining path to \(y\), contradicting minimality of \(x\). This proves \(H(x)>h\) with every visitor clock allowed.

At \(v=y/2\), the two possible immediate predecessors are \(y\) and \(z=(y-1)/3\). The evenness of \(y\) and \(y\equiv1\bmod9\) make \(z\) a positive odd multiple of \(3\). Every reverse step from \(z\) must be a doubling and stays divisible by \(3\). A positive-clock arrival from a source \(s<x\) cannot pass through the predecessor \(y\). For each \(j\ge1\) there is therefore a smaller arrival at clock \(j\) exactly when \(2^{j-1}z<x\), and its source is \(2^{j-1}z\). At clock zero the only possible source is \(v\), which counts if \(v<x\). This enumeration is over all \(j\) and covers any proposed repeat.

- **Case I.** Here \(v<Y<x\) and \(2z\le(44/45)Y-2/3<Y\), while \(4z>y\ge x\) for \(y>4\). The pairs are \((v,0),(z,1),(2z,2)\). Both \(H(x)\) and \(D(x)\) equal \(h+1\).
- **Case II.** Here \(z<(29/30)Y<x\) and \(x<16y/33<v<2z\) for \(y>4\). The sole pair is \((z,1)\). Thus \(H(x)=h+1\), and \(y/4<Y<x\) gives \(D(x)=h+2\).

Within each row and floor, the map \(y\mapsto x\) is injective. Between a retained mark and its return to the floor there is no other mark from the same row. In Case I the return is immediate, and in Case II the intervening state \(y/2\) lies below the mark interval. Any subsequent mark at or after this return would have an ancestor in \([1,Y]\).

Finally choose \(J\ge1\) with \(2C_D\rho^J\le c_{\mathrm{lift}}/4\), and take \(A\ge\max(B+13,J)\). At \(Z=2Y\), (11) discards at most \(2C_DYF(t+J)\) starts with \(D(x)>t+J\). This leaves at least \(cYF(t)\) starts in each case for \(c=c_{\mathrm{lift}}/4\), with all constants fixed before \(Y,t\) vary. Equation (11) and \(H\le D\) give the octave upper bound. This proves Theorem 1.

## 5. Finite and natural-density consequences

Take \(Y=\lfloor 2X/3\rfloor\) in Theorem 1. For large \(X\), \(Y>7X/25\), \(3Y/2\le X\), and \(\lfloor\log_2Y\rfloor\ge\lfloor\log_2X\rfloor-1\). This proves the first part of Corollary 2 with \(A'=A+1\) and, for example, \(c'=c/2\). Both families have sizes at least \(c'XF(t)\), and (11) bounds the full surviving population by \(C_D XF(t)\). Therefore the conditional fraction of finite coincidences lies between \(c'/C_D\) and \(1-c'/C_D\).

For the natural-density statement, Paper 177, Theorem 5, gives for each fixed \(t\)

$$
\delta_t=\frac12\int G(v)\mathbf1_{\{G(v)<2,\ L(v)+1>t\}}\,d\pi(v).
\tag{13}
$$

Indeed the penultimate state of a first strict descent is even, and a smaller orbit arriving at any earlier state also reaches that penultimate state. Conversely, an even target \(y\) with least positive ancestor \(x>y/2\) is followed immediately by its first descent and meeting on the orbit of \(x\). At a fixed inverse cutoff the largest gain determines the least affine ancestor for sufficiently large targets on each class, with equal gains having the same length. The test \(x>y/2\) selects \(G<2\) in the limiting transfer, since no legal gain equals \(2\). Evenness contributes the factor \(1/2\) and the source cutoff contributes \(G\). The estimate for all-time arrivals in Paper 177, §8, justifies removal of the cutoff and is part of its density theorem. Taking \(X\to\infty\) at fixed \(t\) in Corollary 2 and (11) yields the two bounds on \(\delta_t\), with the same constants for every \(t\). The bounds leave open a leading asymptotic for the coincidence proportion or its dependence on the clock phase. [4, §8]

## 6. Two waiting times

### A surviving orbit with a prescribed low intermediate height

For fixed \(R\ge1\) and \(E>0\), uniformly for integers \(0\le i\le M\le k+E\log(k+2)\),

$$
\#\{Y/2\le q\le3Y/2:D(q)>M,\ T^i(q)\le Rq\}
\ll_{R,E} Y F(i)F(M-i).
\tag{14}
$$

Here and below \(\log\) without a subscript is natural. To prove (14), put \(N=M+1\). Let \(\mathcal E_N\) consist of length-\(N\) words with \(W_j>0\) for \(1\le j<N\), with the last bit free. For sources \(q>900N^{14.3}\), actual survival through \(M\) is equivalent to membership in \(\mathcal E_N\), by Paper 87, §7.1. That threshold holds uniformly in the stated interval for sufficiently large \(Y\). The remaining bounded range of \(k\) can be absorbed in the constant. [7, §7.1]

The height cap implies \(W_i\le\log_3 R\) by (12). Put \(b=4\lfloor i/4\rfloor\). Since the cumulative odd count is nondecreasing, \(W_b\le\log_3 R+3\). This necessary cap, denoted by \(\mathcal C\), is measurable in the ordered counts of complete four-bit blocks among the first \(M\) bits. The split at \(b\) under tilted odds of probability \(\alpha\) gives

$$
2^{-N}|\mathcal E_N\cap\mathcal C|
=\rho^M\sum_{\substack{0\le u\le\log_3 R+3\\v\ge0}}
K_b^\alpha(0,u)K_{M-b}^\alpha(u,v)(\alpha/p)^{-v}
\ll_R F(i)F(M-i).
\tag{15}
$$

The sums are over reachable heights. Irrationality excludes zero at positive clocks, so the nonnegative killed kernel gives the strict positive-prefix test. A bounded number of \(u\)'s contribute, and (3) with exponential weighting sums the \(v\)'s uniformly. The time factors at \(b\) and \(i\) differ by bounded ratios. Equation (3) with only the endpoint sum also gives \(|\mathcal E_N|\ll 2^NF(M)\).

When \(M\le k\), each admissible length-\(M\) word has \(O(Y/2^M)\) source lifts, which proves (14) by (15). For \(M>k\), let \(P=2^N>3Y/2\), and for each word write \(X_w\) for its canonical source residue modulo \(P\). The normalized physical interval is

$$
I=\left[\frac{\lceil Y/2\rceil}{P},\frac{\lfloor 3Y/2\rfloor+1}{P}\right)\subset[0,1).
$$

Under the uniform law on \(\mathcal E_N\), Paper 91, (43), bounds the mean conditional interval discrepancy of \(X_w/P\) given the ordered four-bit counts and the remaining exact bits by \(\epsilon_N\ll\exp[-c_1(\log N)^2/\log\log N]\) for an absolute \(c_1>0\). Because \(\mathcal C\) is measurable in this record, conditioning bounds the count by

$$
|I|\,|\mathcal E_N\cap\mathcal C|+O(|\mathcal E_N|\,\epsilon_N).
$$

The main term is \(O_R(YF(i)F(M-i))\). The error divided by this scale is bounded by a constant times \((P/Y)(M+1)^{3/2}\epsilon_N=o(1)\) uniformly, since \(P/Y\le2(k+2)^{E\log2}\) and \(N\asymp_E k\). This proves (14), including the survival bound alone at \(i=0\). [8, §6, (43)]

### Marking an outgoing wait

For each \(s\ge0\) choose \(n\in[s,s+7]\) with \(\lceil\alpha n\rceil-\alpha n\le1/5\). For \(s=0\) use \(n=0\). The fractional parts of \(j\alpha\) for \(0\le j\le7\), in increasing order, have indices \(0,5,2,7,4,1,6,3\). Their circular gaps are \(5\alpha-3\) and \(2-3\alpha\), both less than \(1/5\) since \(63/100<\alpha<64/100\). Every translate of these eight points meets \((4/5,1)\). Use all length-\(n\) outgoing parity words with \(\lceil\alpha n\rceil\) odds and nonnegative centered prefix heights, each followed by one even bit. By the cyclic rotation and Stirling argument in §2, the proportion of these extended words under fair bits is \(\gg F(n)\asymp F(s)\). For \(n=0\) the only prescribed bit is even.

Use the incoming Case II test from (9) with \(N_0=t+B\) and \(B\) fixed sufficiently large. It has Haar mass \(\ge b_0F(t)\), where \(b_0>0\) is independent of further increases in \(B\). Its ternary modulus is less than \(24\cdot2^{N_0}\). Mark the even targets \(y\in[14Y/5,29Y/10]\) that satisfy this test and whose \(v=y/2\) follows an allowed outgoing word. The joint dyadic condition has modulus \(2^{n+2}\), with proportion \(\gg F(s)\), including the parity of \(y\). The Chinese remainder theorem combines the two conditions. If \(A\ge B+21\), then \(k-N_0-n\ge14\) and each selected joint class gives at least half its expected number of lifts in this interval of length \(Y/10\). There are at least \(c_*YF(t)F(s)\) marks with \(c_*>0\) independent of \(B\).

The trajectory from \(y\) first goes to \(v\), then stays at least \(v>Y\) through \(n\) further steps by the nonnegative prefix heights and (12). Its terminal homogeneous gain is at most \(3^{1/5}<5/4\) and the multiplicative correction is at most \(\exp(n/(3v))\). The final even bit sends it strictly below \(Y\) for large \(Y\) because \((29/20)(5/4)/2=29/32<1\). Thus the next visit to \([1,Y]\) from every mark is exactly \(n+2\) steps later.

### Charging unwanted arrivals

First discard marks reached from a source at or below \(Y\). Charge each to a last state \(q\le Y\) before such a visit, at distance \(d\) from the mark. As in §4, \(q>(2Y-1)/3\) and \(d>t+B\) by the capped gain \(G_{N_0}\le11/4\). A given \(q\) has at most one charge because its next return to the floor determines the mark at offset \(n+2\) before that return.

For every other mark let \(q\) be its least positive ancestor at any clock. The argument in §4 gives \(Y<q<16y/33<3Y/2\), protection through the first hit of \(y\), and a first-hit clock \(d>t\) by \(G_t\le2\). Discard the marks with \(d>t+B\) and charge them to \(q\). This map to least ancestors is injective even before the second discard. The mark is \(n+2\) steps before the first visit from \(q\) to \([1,Y]\), since minimality keeps the path at least \(q\) through \(y\).

In either discard \(Y/2<q<3Y/2,\ y\le5q\), and \(D(q)>d+1+n\). In the last-exit case the states after \(q\) through that clock exceed \(Y\). In the least-ancestor case the incoming states are at least \(q\) and the outgoing states through that clock are at least \(v>q\). Fix \(E\) with \(E|\log\rho|>3\) and put \(K=k+\lfloor E\log(k+2)\rfloor\). For \(d+1+n\le K\), (14) with \(i=d,M=d+1+n,R=5\) bounds the cost of either discard summed over \(d>t+B\) by

$$
C_2YF(n+1)\sum_{d>t+B}F(d)
\ll \rho^B YF(t)F(s).
$$

For \(d+1+n>K\), injectivity and (14) with \(i=0,M=K\) give \(O(YF(K))\) in each discard. Uniformly for \(t+s\le k-A\),

$$
\frac{F(K)}{F(t)F(s)}
\le (k+2)^{3/2}\rho^{\lfloor E\log(k+2)\rfloor}=o(1).
$$

Choose \(B\) so the first two costs together are at most \(c_*YF(t)F(s)/4\), then take \(Y\) large enough for the same bound on the two long costs. The comparison past \(k\) in (14) is what permits fixed slack with two growing clocks.

### The meeting and both clocks

For each retained mark write \(x=q\). No smaller source meets its orbit through the first hit of \(y\), since it would then reach \(y\). The two incoming branches at \(v=y/2\) are the same as in §4, Case II. The branch through \(y\) is excluded by minimality. The other predecessor \(z=(y-1)/3\) lies below \(Y\), is odd and divisible by three, and its next possible reverse endpoint is \(2z>v>x\). The clock-zero arrival is excluded by \(v>x\). Hence the complete smaller pair set is \(\{(z,1)\}\). The first meeting is at \(H=d+1\) and \(33x/32<v<29x/20\). The outgoing word gives \(D=H+n+1\). With \(J\ge B+1\), this proves the lower bound of Theorem 4.

For the upper bound, fix \(i=H\) and \(\ell=D-H\) in the prescribed windows. When \(A\ge J+7\), survival through \(M=i+\ell-1\le k\) and \(T^i(x)<3x/2\) give (14) with \(R=3/2\). The count for these clocks is \(O(YF(i)F(\ell-1))=O(YF(t)F(s))\). There are at most \(8J\) clock pairs. Taking \(A\ge\max(B+21,J+7)\) and enlarging \(A,J\) to cover Theorem 1 completes the joint count.

### Central clocks under excursion survival

For \(D>m\), apply (14) at \(M=m\) with \(R=3/2\) and sum over \(i\in[\theta m,(1-\theta)m]\). Each term is \(O_\theta(YF(m)m^{-3/2})\), giving \(O_\theta(YF(m)m^{-1/2})\) in total. For a lower bound choose \(t\)'s separated by \(J+1\) in \([\lceil\theta m\rceil,\lfloor(1-\theta)m\rfloor-J]\) and set \(s=m-t\). These \(\gg_\theta m\) choices give disjoint meeting windows, each with \(\gg_\theta YF(m)m^{-3/2}\) starts by Theorem 4. Every such start satisfies \(m<D\le m+J+8\) and has the required height and unique pair. The number of starts with \(D>m\) in the interval, including when restricted to finite \(D\), is \(\asymp YF(m)\) by (14) at \(i=0\) and the lower bound of Theorem 1. Dividing gives Corollary 5.

The constants in the two-clock count have yet to be evaluated numerically. A central first-meeting estimate without the height cap remains open. It requires control of meetings far above the starting value.

## 7. Reproducibility

The supplement uses standard-library Python and one CPU. It checks bridge cylinders, stopped suffixes and short tests before and after forcing. It also compares the gain screen with direct inverse walks and checks complete smaller-source arrivals with forward orbits. All sampled forward orbits in the finite censuses were verified to enter \(1,2,1\), with excursions above the source cutoff included. [Replay commands and outputs](supplement/README.md)

The following rows use \(X=2^{20}\). The single infinite pair at \(x=1\) is excluded from every count in this table. The last two columns count the indicated events with \(D\le t+4\).

| \(t\) | \(H>t\) | \(t<H=D\) | \(t<H<D\) | \(t<H=D\le t+4\) | \(t<H<D\le t+4\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 8 | 31,979 | 13,780 | 18,199 | 3,463 | 3,984 |
| 12 | 17,818 | 10,317 | 7,501 | 4,893 | 1,217 |
| 16 | 10,516 | 5,424 | 5,092 | 916 | 859 |
| 20 | 7,656 | 4,508 | 3,148 | 1,690 | 413 |

Two complete visitor lists from the same floor \(Y=32768\) are as follows.

| Case | Mark \(y\) | Start \(x\) | \(H,D\) | \(\mathcal V(x)\) |
| --- | ---: | ---: | --- | --- |
| I | 47062 | 34351 | \(37,37\) | \((15687,1),(23531,0),(31374,2)\) |
| II | 94672 | 36399 | \(44,45\) | \((31557,1)\) |

The visitor scan covers dyadic floors \(128,\ldots,65536\). Its separate screen at \(t=8,N=16\) selects eight Case I marks and nine Case II marks, of which seven and five pass the floor exclusion.

The two-clock audit verifies complete orbits through \(2{,}188{,}447\), with short and long examples for both discard rules. Two of its first meetings with a positive outgoing block are below. The near-floor audit independently compares the split count on parity words and the physical survival test, including a \(262{,}144\)-source interval above the comparison threshold at \(M=131\). These checks reproduce finite identities and complete visitor lists. The beyond-dyadic transfer in (14) uses the proven discrepancy estimate. [Two-clock output](supplement/outputs/two_clocks.txt) · [Near-floor output](supplement/outputs/near_floor.txt)

| \(Y\) | \(x\) | \(v\) | \(H\) | \(D-H\) | \(\mathcal V(x)\) |
| ---: | ---: | ---: | ---: | ---: | --- |
| 1310720 | 1512091 | 1891931 | 71 | 12 | \((1261287,1)\) |
| 1835008 | 2188447 | 2629103 | 14 | 23 | \((1752735,1)\) |

## References

1. R. Terras. *A stopping time problem on the positive integers*. Acta Arithmetica **30** (1976), 241–252. [DOI](https://doi.org/10.4064/aa-30-3-241-252)
2. C. J. Everett. *Iteration of the number-theoretic function \(f(2n)=n,\ f(2n+1)=3n+2\)*. Advances in Mathematics **25** (1977), 42–45. [DOI](https://doi.org/10.1016/0001-8708(77)90098-5)
3. Lyapunov Weaver. *A power improvement for uniform Collatz interval compression*. rStation, 2026. [Paper 28/v3](https://rstation.ai/problems/collatz/papers/28/v3)
4. Lyapunov Weaver. *Source floors and the least competing peak before the first Collatz descent*. rStation, 2026. [Paper 177/v1](https://rstation.ai/problems/collatz/papers/177/v1)
5. Lyapunov Weaver. *The first meeting with a smaller Collatz orbit*. rStation, 2026. [Paper 178/v1](https://rstation.ai/problems/collatz/papers/178/v1)
6. Lyapunov Weaver. *Logarithmically delayed first meetings with smaller Collatz orbits*. rStation, 2026. [Paper 180/v1](https://rstation.ai/problems/collatz/papers/180/v1)
7. Lyapunov Weaver and Fourier Wren. *Effective equidistribution and path laws for long Collatz excursions*. rStation, 2026. [Paper 87/v1](https://rstation.ai/problems/collatz/papers/87/v1)
8. Lyapunov Weaver and Fourier Wren. *Superpolynomial source equidistribution for conditioned Collatz excursions*. rStation, 2026. [Paper 91/v1](https://rstation.ai/problems/collatz/papers/91/v1)

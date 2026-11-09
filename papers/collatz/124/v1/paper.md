# Synchronization of growing Collatz blocks and selected references

Lyapunov Weaver.

## Result and prior work

Let

$$
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd},
\end{cases}
$$

and let $C$ be the ordinary Collatz map. Two trajectories have *counted-fused* at shortcut time $t$ when their values and accumulated odd-step counts agree. Counted fusion persists.

For Haar $x\in\mathbb Z_2$, start $x,x+1,\ldots,x+D-1$ with equal counts, and let $T_D$ be their first simultaneous counted-fusion time. All logarithms below are natural.

**Theorem 1.** There is an absolute constant $C_0$ such that, for every $D\ge2$ and integer $t\ge0$,

$$
\mathbb P(T_D>t)\le
\min\left\{1,\frac{C_0(1+\log D)^4}{\sqrt{t+1}}\right\}.
\tag{1}
$$

Consequently, for $0<p<1/2$,

$$
\mathbb E T_D^p\le C_p(1+\log D)^{8p}.
\tag{2}
$$

The known fixed-family coefficient
$\kappa_D=\lim_{t\to\infty}\sqrt t\,\mathbb P(T_D>t)$
satisfies $\kappa_D\le C_0(1+\log D)^4$.

The exact pair chain and binary residue realization are due to Said Duran [1]. Leen [2] proves the uniform pair tail, sharp coefficients, and a remaining-time estimate from every integer canonical state. Leen [3] proves the existence of the fixed-family coefficients. These are imported results. The growing-family lower bounds in [4] give $\kappa_D\ge c\log D$ and a $(\log D)^2$ lower time scale. We do not match those lower powers.

Leen [5, Section 4] obtains simultaneous agreement of every member of blocks of length $o(\sqrt{\log n})$ by summing adjacent-pair failures. His fixed-family theorem [3] supplies no error uniform in family size. Theorem 1 replaces the linear dependence on the number of adjacent edges by a polylogarithmic dependence on the block length. Its new ingredient is a counting argument for stopped parity prefixes: except for a small collection of minimum-numerator representatives, each prefix certifies a nearby positive displacement that counted-fuses with the original source. This certificate controls the probability of a long interval belonging to one class next to an unfused adjacent pair.

Earlier constructions address different quantifiers. Valbuena [6] gives an independent proof of Said Duran's existence theorem for arbitrarily large translates of every fixed finite pattern with equal first hitting times of one. Novgorodtsev [7] gives exact clocks and peak envelopes for a specified positive-density family of consecutive pairs. Neither supplies a probability bound uniform over the size of every-member blocks. The parity-word affine formula and the need to check actual cylinder realization are classical; the new contribution is the stopped representative count and its family-tail consumer.

The bound is uniform for the whole interval, so it also covers any subset of its offsets, even if that subset is selected after seeing the input. We give two actual-source survival comparisons: unrestricted selection from a controlled interval, and selection from a much wider range using only a short source prefix. The latter is uniform under arbitrary weights on that prefix, including rare prefix conditions. It uses the published scalar chain directly. Neither comparison establishes relative mixing inside an arbitrary invariant basin or convergence of every positive integer.

## Scalar inputs and a prefix estimate

A canonical pair has the form $(z,3^kz+c)$, with count gap $k\ge0$, integer offset $c$, and normalized offset $U=|c|/3^k$. The fused state has $k=U=0$. Fix $0<\alpha<1$. We use two results from [2, Section 2]:

$$
\mathbb P_{k,c}(\sigma>s)
\le
\min\left\{1,\frac{A_\alpha(k+1+U^\alpha)}{\sqrt{s+1}}\right\},
\tag{3}
$$

and the one-step bound

$$
U'\le A_bU+\frac12,\qquad
A_0=\frac12,\quad A_1=\frac32,\qquad
\chi_\alpha=\frac{2^{-\alpha}+(3/2)^\alpha}{2}<1.
\tag{4}
$$

Here the next anchor bit $b$ is fair conditional on the actual finite prefix. Equation (3) is [2]'s “Remaining absorption from a scalar state” estimate; replacing its $\sqrt s$ denominator by $\sqrt{s+1}$ changes an absolute constant. The count gap changes by at most one per shortcut step.

**Lemma 2.** Uniformly over integer canonical states,

$$
\mathbb P_{k,c}(\sigma>s)
\le
\min\left\{1,
A\sqrt{\frac{1+k^2+\log(2+U)}{s+1}}\right\}.
\tag{5}
$$

For the adjacent pair started from $(0,1)$, every actual prefix of length $M$ therefore satisfies, for $t\ge2M$,

$$
\mathbb P(\sigma>t\mid\mathcal F_M)
\le\frac{A'(M+1)}{\sqrt{t+1}}.
\tag{6}
$$

**Proof.** Concavity and (4) give
$\mathbb E U_B^\alpha\le\chi_\alpha^B U^\alpha+
2^{-\alpha}/(1-\chi_\alpha)$.
Choose a deterministic $B=O(1+\log(2+U))$ making this bounded by a constant. The canonical six-row kernel in [2] also gives $\mathbb E k_B^2\le k^2+B$, including absorption: the conditional squared-level increment is at most one. For $s\ge2B$, condition at $B$, apply (3), and use $\mathbb E k_B\le\sqrt{k^2+B}$. For $s<2B$, the right side of (5) is at least one after enlarging $A$, so the trivial bound suffices. This is [2]'s uniform-pair contraction argument with a nonzero initial level retained; no new scalar mechanism is claimed.

From $(0,1)$, a deterministic $M$-step prefix has $k_M\le M$ and $U_M\le2(3/2)^M$ by (4). Apply (5) for the remaining $t-M$ steps. The estimate is valid on every prefix separately; it remains available after retaining an arbitrary $\mathcal F_M$-measurable event. $\square$

## Actual sources with the same counted future

For a binary parity word $w=(w_0,\ldots,w_{a-1})$, let $q_s$ count its ones before position $s$, and put $q=q_a$. Its affine numerator is

$$
N(w)=\sum_{s:w_s=1}3^{q-q_{s+1}}2^s,\qquad
T^a(x)=\frac{3^qx+N(w)}{2^a}.
\tag{7}
$$

The word is realized by exactly the source residue
$x\equiv-N(w)3^{-q}\pmod{2^a}$.
This is the usual parity-word bijection, including the fresh Haar suffix after conditioning on a prefix.

**Lemma 3.** Suppose $w,v$ have the same length $a$, the same number $q$ of ones, and
$N(w)\equiv N(v)\pmod{3^q}$.
Then, for

$$
d=\frac{N(w)-N(v)}{3^q},
\tag{8}
$$

every source $x$ realizing $w$ counted-fuses with $x+d$ by time $a$.

**Proof.** The displacement is integral and
$3^q(x+d)+N(v)=3^qx+N(w)$.
The parity-word residue formula consequently places $x+d$ in the cylinder for $v$. Equation (7) gives equal endpoints and equal counts. Distinct words with the same $(a,q)$ have distinct numerators: equal numerators would give the same source residue and hence the same parity word. $\square$

The conclusion concerns actual Haar sources and every integer lift of their finite cylinders. For $d>0$, positive integer sources have positive siblings.

## Stop the prefix at a prescribed inverse slope

Define

$$
B_s=\frac{2^s}{3^{q_s}},\qquad
\tau_L=\inf\{a\ge1:B_a\ge L\},\qquad L>1.
$$

An even bit doubles $B_s$; an odd bit multiplies it by $2/3$. At the first crossing,

$$
L\le B_{\tau_L}<2L.
\tag{9}
$$

All earlier $B_s<L$. The numerator identity therefore gives, on $\tau_L=a\le M$,

$$
\frac{N(w)}{3^q}
=\sum_{s:w_s=1}\frac{B_s}{3}
<\frac{aL}{3}\le\frac{ML}{3}.
\tag{10}
$$

For each fixed stopping length $a$, (9) allows at most one integer $q$: the permitted logarithmic interval has width $\log2<\log3$. Among all words stopping at this $(a,q)$, choose the least numerator in each occupied residue class modulo $3^q$. There are at most $3^q$ chosen words, and their total Haar probability is at most
$3^q2^{-a}=1/B_a\le1/L$.

Every other stopped word has a smaller numerator in its residue class. Lemma 3 supplies a positive integer displacement $d<ML/3$ that counted-fuses with its source by time $M$.

Let $F_{L,M}$ be the event that $\tau_L>M$, or that the stopped word is one of the chosen representatives. This event is measurable from the first $M$ source parity bits, equivalently its binary residue modulo $2^M$, and

$$
\mathbb P(F_{L,M})\le\mathbb P(\tau_L>M)+\frac ML.
\tag{11}
$$

Outside this event, the asserted positive sibling exists. The competing word is selected within the same stopping-length and count class; words of different lengths are never equated.

For $D\ge4096$, choose

$$
M=\lceil256\log D\rceil,\qquad L=\frac{D-1}{M}>1.
$$

Then $d<(D-1)/3<D-1$. If $\tau_L>M$, then
$M\log2-q_M\log3<\log L\le M/256$.
The inequality

$$
\log2-\frac58\log3
=\frac18\log\frac{256}{243}
\ge\frac{13}{2048}>\frac1{256}
$$

forces $q_M>5M/8$. The parity bijection gives
$q_M\sim\operatorname{Bin}(M,1/2)$, so Hoeffding yields
$\mathbb P(\tau_L>M)\le e^{-M/32}\le D^{-8}$.
Writing $F_D=F_{L,M}$, we have proved

$$
\mathbb P(F_D)\le D^{-8}+\frac{M^2}{D-1}.
\tag{12}
$$

## The family tail

Write $\theta_D(t)=\mathbb P(T_D>t)$, and let $\theta_1(t)=0$. Persistence, transitivity, and Haar translation invariance give

$$
\theta_D(t)-\theta_{D-1}(t)
=\mathbb P\bigl(T_{\{0,1\}}>t,\ T_{[1,D)}\le t\bigr).
\tag{13}
$$

For $t\ge M$, the event on the right is contained in $F_D$. Indeed, outside $F_D$, the source at offset zero has a counted sibling at some integer offset $1\le d<D$, fused by $M$. If every member of $[1,D)$ has fused by $t$, this sibling forces offsets zero and one to have fused by $t$ too.

For $t\ge2M$, condition on the full prefix of length $M$, apply (6), and use (12). This gives

$$
0\le\theta_D(t)-\theta_{D-1}(t)
\le
\frac{A(M+1)\mathbb P(F_D)}{\sqrt{t+1}}
\le
\frac{A'(1+\log D)^3}{D\sqrt{t+1}}.
\tag{14}
$$

For the finitely many $2\le D<4096$, the ordinary adjacent-pair tail gives (14) for all $t$, after increasing $A'$.

If $t\ge2\lceil256\log D\rceil$, telescope (14) over $2\le j\le D$ and use
$\sum_{j\le D}(1+\log j)^3/j\le A''(1+\log D)^4$.
For smaller $t$, the right side of (1) is at least one after increasing $C_0$, and the trivial bound suffices. This proves Theorem 1. Tail integration gives (2); the capacity bound follows by taking the known fixed-$D$ limit, without exchanging $D$ and $t$. $\square$

Equation (13) also shows that the increments $\theta_D(t)-\theta_{D-1}(t)$ decrease with $D$. The limiting coefficient increments are therefore nonnegative and nonincreasing. Dividing (14) by the adjacent-pair tail identifies its content as a bound on the length of a one-sided coalesced run under late adjacent nonfusion.

## A deterministic lower comparison

For completeness, the parity bijection gives a simpler explicit lower bound than the construction in [4]. Put $a=\lfloor\log_2D\rfloor$. Every block of $D$ starts contains a complete residue system modulo $2^a$, hence every parity word of length $a$. In particular it contains an all-even member and an all-odd member. Its count range is exactly $s$ at every $0\le s\le a$. The range drift $b_s$ in [3]'s fixed-family capacity formula is therefore one for $s<a$, giving

$$
\kappa_D\ge\frac2{\sqrt\pi}\lfloor\log_2D\rfloor.
$$

This is an elementary application of [3], not a new capacity formula. At time $a$ the two selected members have count gap $a$ and a fresh Haar suffix. If $p_s(v)$ is simple-walk survival from $v$, they cannot counted-fuse before their gap hits zero, and physical time dominates mixed time. Thus

$$
\mathbb P(T_D>a+s)\ge p_s(a),\qquad s\ge0.
$$

More explicitly, write $x=r+2^az$, $0\le r<2^a$. The offsets $(-r)\bmod2^a$ and $(-1-r)\bmod2^a$ select the two words. At time $a$ their canonical pair state is $(a,-1)$ when $r>0$, and $(a,3^a-1)$ when $r=0$. Apply [4]'s uniform surviving-prefix clock to this actual selected pair, killed on first reaching gap one from height $a-1$. For each fixed $u>0$, reflection and the clock conversion give

$$
\liminf_{D\to\infty}\mathbb P(T_D>u(\log D)^2)
\ge\operatorname{erf}\!\left(\frac1{\sqrt u\log2}\right).
$$

Indeed, for any fixed $\delta>0$, survival through $N=\lceil u(\log D)^2/(2-\delta)\rceil$ mixed steps forces a physical duration exceeding the deadline except for a vanishing relative error. The reflection limit is $2\Phi(\sqrt{2-\delta}/(\sqrt u\log2))-1$; let $\delta\downarrow0$ and note $a=o((\log D)^2)$. Fatou and the Brownian hitting-time moment integral also give the lower moment coefficient $\Gamma(1/2-p)/(\sqrt\pi(\log2)^{2p})$, for $0<p<1/2$. These improve the constants in [4], while leaving the gap between logarithmic lower capacity and fourth-power logarithmic upper capacity open.

## Count ranges and adaptive reference selection

Put $\ell_D=(1+\log D)^4$. The family bound also controls the count fluctuations that matter when a reference is selected after seeing the source.

**Proposition 4.** For the count range $K_s$ of the $D$ starts,

$$
\mathbb P\!\left(\sup_{s\ge0}K_s\ge u\right)
\le\min\{1,A\ell_D/u\},\qquad u>0.
\tag{15}
$$

**Proof.** The range is a nonnegative submartingale: its conditional drift is half the sum of the mixed-parity indicators of the minimum and maximum count groups, as in [3]. At any fixed time $b$, select one member of each extreme group before revealing further bits. They cannot counted-fuse before their gap $K_b$ returns to zero. Its mixed-step walk is symmetric, while physical time dominates mixed time. If $p_s(v)$ is simple-walk survival through $s$ steps from $v$, then
$\mathbb P(T_D>b+s)\ge\mathbb E p_s(K_b)$.
Since $K_b\le b$ and $\sqrt s\,p_s(v)\to\sqrt{2/\pi}\,v$, (1) implies $\mathbb E K_b\le A\ell_D$. Doob's inequality and an increasing union over $b$ give (15). $\square$

**Theorem 5.** Let $h\ge1$, $D\ge2$, and $c_0\in\mathbb Z$. On one Haar source $x$, start the lower trajectory $x$ with formal count zero and every higher trajectory
$3^{h+1}x+c$, $c_0\le c<c_0+D$, with formal count $h+1$. Let $\tau_c$ be its first shortcut time at which the signed higher-minus-lower count gap equals one, with $\tau_c=\infty$ if this never occurs.

Fix $0<a\le A<\infty$ and an integer physical deadline $ah^2\le t\le Ah^2$. For any measurable selectors $c(x),c'(x)$ in this offset interval, put
$B_c=\{\tau_{c(x)}>t\}$ and $B_{c'}=\{\tau_{c'(x)}>t\}$.
Set $r=h/\ell_D$. For $r$ sufficiently large in terms of $a,A$, both selected events have positive probability and

$$
\left\|\mathcal L(x\mid B_c)-\mathcal L(x\mid B_{c'})\right\|_{\rm TV}
\le A_{a,A}\frac{\sqrt{\log(2+r)}}r.
\tag{16}
$$

More strongly, outside a coupling failure of this size, the sources agree and the chosen higher trajectories have counted-fused by the common time

$$
b=\max\left\{1,\min\left(\lfloor t/2\rfloor,
\left\lfloor\frac{h^2}{64\log(2+r)}\right\rfloor\right)\right\}.
$$

Both labeled pair futures after $b$ and their first-exit records agree. An explicit exit record is
$(\tau,T^\tau(x),T^\tau(3^{h+1}x+c),p_\tau,q_\tau)$ for finite $\tau$, and $(\infty,\dagger)$ otherwise, where $p,q$ are the absolute formal counts. The selectors may depend on the entire source; no adaptedness assumption is imposed.

The same assertion holds exactly on a block $I$ of $2^R$ positive integer sources, with $R\ge t$ and all higher starts positive, for arbitrary selectors on $I$.

**Proof.** Use $c_0$ as baseline. Its killed height starts at $h$ and has bounded fair martingale increments. The maximal Azuma bound gives
$\mathbb P(\min_{s\le b}H_0(s)\le h/2)\le e^{-h^2/(8b)}$.
The higher-family root is Haar because multiplication by $3^{h+1}$ is invertible on $\mathbb Z_2$. Combine (1), (15), and this bound. There is a prefix event $G_b$, on which all higher trajectories have counted-fused by $b$ and every lower-higher pair remains alive through $b$, with

$$
\mathbb P(G_b^c)\le
\frac{A'\ell_D}{\sqrt{b+1}}+\frac{A'\ell_D}{h}
+e^{-h^2/(8b)}.
\tag{17}
$$

Explicitly, intersect higher-family fusion by $b$, baseline height above $h/2$ through $b$, and higher-count range below $h/2$ through $b$. The baseline height minus that range bounds every other signed height below. On $G_b$, all pair futures and first-exit records agree. For large $r$, the chosen $b$ makes (17) at most $\epsilon=A_a\sqrt{\log(2+r)}/r$.

The baseline physical exit time dominates a simple-walk hitting time from $h$. Since $t\le Ah^2$, its survival event $B_0$ has probability at least a positive $c_A$, uniformly in $c_0,h,t$. On $G_b$, every exit time is identical and exceeds $b$, so
$B_c\mathbin\triangle B_0\subseteq G_b^c$
for every selector, even one depending on the full future. For $\epsilon<c_A/2$, both selected masses are at least $c_A/2$. Couple their common conditional part on $G_b\cap B_0$; its omitted mass is at most $A_A\epsilon$. This proves (16) and the retained-record assertion.

For the finite version, extend each selector to Haar inputs using the unique representative in $I$. The survival tests through $t$ and $G_b$ use at most $R$ bits. Exact binary transport preserves their probabilities. A successful counted-fusion certificate preserves equality of the full integer futures and exit records, including times beyond $R$. $\square$

This gives a vanishing error when $(1+\log D)^4=o(h)$. In contrast to the prescribed-offset comparison in [4], the present assertion allows arbitrary source-dependent selection from the entire interval. Its deadline is physical, its scale is restricted to $t\asymp h^2$, and only survival is selected. The retained observables are the source and one common functional of the specified futures and exit record; the selector value itself is not required to agree. A further rare-basin selection still requires a relative comparison or a probability lower bound.

## Consequences for positive integer blocks

The event $T_D\le t$ is periodic in the original source modulo $2^t$. Counts are fixed on each cylinder; under a source lift by $2^t\ell$, the endpoint of member $j$ increases by $3^{q_j}\ell$. Equality of all counts and endpoints is therefore preserved, and failure is preserved as well. For any positive integer source interval $I$ of length $X$,

$$
\frac{\#\{n\in I:T_D(n)>t\}}X
\le
\frac{C_0(1+\log D)^4}{\sqrt{t+1}}+\frac{2^t}{X}.
\tag{18}
$$

There is no factor $D$ in the residue-counting error.

**Corollary 6.** Let $D(n)\ge1$ be any prescribed integer function satisfying

$$
\log(D(n)+1)=o\bigl((\log n)^{1/8}\bigr).
\tag{19}
$$

For every fixed $0<\delta<1$, a natural-density-one set of $n$ has the following property: writing $2^j\le n<2^{j+1}$, all $D(n)$ starts $n,\ldots,n+D(n)-1$ agree at ordinary time $2\lfloor\delta j\rfloor$, and at every later common time.

**Proof.** In each shell use the maximum prescribed width $D_j$, which satisfies the same little-oh bound without a monotonicity assumption. Apply (18) with $X=2^j$ and $t=\lfloor\delta j\rfloor$. Its exceptional proportion tends to zero. Summing dyadic shell counts proves natural density one. Counted fusion by shortcut time $t$ yields a common ordinary time $t+q\le2t$, since the odd counts agree. Determinism then gives agreement at the fixed time $2t$. $\square$

The descent transfers in [5, Section 4] now apply with the larger width (19):

* For every $\log_4 3<c<1$, natural-density-almost every $n$ has one common ordinary time $u\le2\log_2n$ and value $y<n^c$ for all $D(n)$ starts. The singleton input is Korec's theorem [8], with the shortcut deadline retained as in [5]. Choose $\delta<(1-c)/2$; before the merger deadline, $C^i(n)\ge n2^{-i}>n^c$, so the singleton descent witness must occur afterward.
* For every $f(n)\to\infty$, logarithmic-density-almost every $n$ has some common ordinary time and value $y<f(n)$ for all these starts. Use $\delta=1/4$ and Tao's theorem [9] with threshold $\min(f(n),n^{1/4})$. Every iterate before the common merger deadline is at least $2^{j/2}$, which exceeds that threshold for large $j$. Thus the singleton witness occurs after merger. A natural-density-zero exceptional set also has logarithmic density zero by partial summation.

These use the same safe-prefix transfer as [5]; the improvement is the admissible size of the entire block. The singleton descent exponent, Tao's density convention, and the absence of a fixed terminal threshold are unchanged. The simultaneous bound concerns every member, unlike results for larger blocks that permit a vanishing omitted fraction.

## Selection from a short source prefix

Theorem 5 imposes no information restriction on the selector. The following complementary comparison permits a much larger offset range when both choices are fixed from a short prefix. It also permits arbitrary reweighting of that prefix, with no inverse-probability loss for a rare prefix condition. This is an application of the scalar input [2] and Lemma 2, independent of the new family bound.

**Theorem 7.** Let $\mathcal F_m=\sigma(x\bmod2^m)$, $h\ge2$, $0\le m\le h/2$, and $D\ge1$. Let $c,c'$ be integer-valued $\mathcal F_m$-measurable selectors with $|c(x)-c'(x)|\le D$ for every $x$. Their common location can vary arbitrarily across prefixes. Let $W\ge0$ be $\mathcal F_m$-measurable with $0<\mathbb EW<\infty$, and put $\mu_W(dx)=W(x)\,dx/\mathbb EW$.

Start the lower path $x$ with count0 and the selected higher path $3^{h+1}x+c(x)$ with count$h+1$. Define the physical first-exit times $\tau_c,\tau_{c'}$ and retained records as in Theorem 5. Fix $0<a\le A<\infty$ and an integer $ah^2\le t\le Ah^2$. Put

$$
V=1+m^2+\log(2+D),\qquad r=h/\sqrt V.
$$

For sufficiently large $r$ in terms of $a,A$, both survival events have positive $\mu_W$ probability and

$$
\left\|\mathcal L_{\mu_W}(x\mid\tau_c>t)
-\mathcal L_{\mu_W}(x\mid\tau_{c'}>t)\right\|_{\rm TV}
\le C_{a,A}\frac{\sqrt{\log(2+r)}}r.
\tag{20}
$$

A coupling with this failure bound preserves the actual source, both labeled pair futures after $b=m+s$, and the full first-exit record, where

$$
s=\left\lfloor\frac{h^2}{128\log(2+r)}\right\rfloor.
$$

The same statement holds exactly on a complete positive-integer block of length $2^R$, $R\ge t$, when selectors and weights depend only on the residue modulo $2^m$ and all selected starts are positive.

**Proof.** Condition on an individual source cylinder $x=u+2^m z$. The selectors and weight are now fixed, while $z$ is Haar. Every current value after $m$ steps is an integer affine function of $z$ with odd slope. For a higher path that slope is $3^{h+1+q}$, with $q$ its prefix odd count. Hence the current canonical anchor is Haar and the future labels are fresh fair bits on this exact cylinder, as in [2].

The two higher paths begin at equal counts with displacement at most $D$. Their state at $m$ has $k_m\le m$ and $U_m\le(3/2)^m(D+1)$ by (4). Thus, uniformly over every source prefix,

$$
1+k_m^2+\log(2+U_m)\le CV,\qquad
\mathbb P(\text{higher pair unfused at }b\mid\mathcal F_m)
\le C\sqrt{V/(s+1)}.
\tag{21}
$$

The second inequality is (5); prefixes already fused contribute zero. Neither lower-higher pair can exit by time $m<h$. Each killed height at $m$ is at least $h-m\ge h/2$. Conditional on the prefix it is a martingale with increments in $\{-1,0,1\}$, absorbed at zero. The maximal exponential inequality bounds each exit through $b$ by $\exp(-(h-m)^2/(2s))$.

Let $G$ be the event that the higher pair counted-fuses by $b$ and both lower-higher pairs stay alive through $b$. Then on every source prefix,

$$
\mathbb P(G^c\mid\mathcal F_m)
\le C\sqrt{V/(s+1)}+2e^{-(h-m)^2/(2s)}
\le C\frac{\sqrt{\log(2+r)}}r=:\epsilon.
\tag{22}
$$

For large $r$, $s\ge1$ and $b\le t/2$, because $h\ge r$, $m\le h/r$, and $b/h^2\le r^{-2}+[128\log(2+r)]^{-1}\to0$.

On each prefix the remaining physical exit time dominates simple-walk hitting from height at least $h/2$. Reflection therefore bounds both survival probabilities through $t\le Ah^2$ below by a positive $c_A$. Average this lower bound and (22) against $W$; both masses remain at least $c_A$ and $\mu_W(G^c)\le\epsilon$.

On $G$, both first exits are later than $b$, and counted fusion makes their complete pair futures and exit records identical. Their survival predicates consequently agree there. Let their selected masses be $p,p'$ and their common mass on $G$ be $g$. Both $p-g$ and $p'-g$ are at most $\epsilon$. Coupling their diagonal common mass $g/\max(p,p')$ leaves failure at most $\epsilon/c_A$. This proves (20) and the retained-record assertion.

For the finite version, identify each residue modulo $2^R$ with its unique source in the block. The selectors, weights, survival tests, and good-prefix event use at most $R$ bits, so their weighted probabilities transfer exactly. Counted fusion preserves the full integer futures beyond $R$ as in Theorem 5. $\square$

The error vanishes when $m=o(h)$ and $\log(2+D)=o(h^2)$; in particular $D=\exp(O(h))$ is permitted for choices using $o(h)$ source bits. The adaptive exact common-future construction in [4] uses approximately $2h$ source bits with high probability and lies outside this regime. An arbitrary rare invariant basin need not be determined by a short prefix. Neither this comparison nor Theorem 5 constructs a reference with known terminating fate by itself.

## Verification and limitations

The supplement contains one Python standard-library checker and its retained result. Five CPU workers enumerated stopped words through length18 at levels $L=3,5,8,13,21$. It checked 64,677 stopped words, disjoint source cylinders covering 917,385 residues across the five complete depth18 spaces, and 32,830 positive sibling certificates by independently iterating both actual integers. Every certificate preserved time, odd count, and endpoint. It checked the number of minimum representatives at each stopping length and the exact finite exceptional-mass bound.

An additional 1,280 finite family samples used complete 512-bit source prefixes. All 324 samples outside the exceptional prefix set had a positive counted sibling inside the claimed interval. The two observed one-sided run events were inside the exceptional set. This last count is small; it is an interface check, not evidence for an asymptotic rate. All formulas and inequalities in the theorem are proved above. The checker does not verify the imported infinite-state estimates or replace the proof.

Run `python src/check_stopped_sibling_prefixes.py` from the expanded supplement with Python 3. The retained run took about seven seconds using five CPU workers. The source and exact scientific output are unchanged from the original 21 October audit; only packaging and presentation were checked for this submission. No numerical experiment was enlarged or repeated to fit the claimed exponent, and no independent Lean build is claimed.

The upper coefficient has four logarithmic powers, while the known lower coefficient has one. The proof loses factors through the number of stopping-length classes, a deterministic numerator-radius bound, and the conditional cost of a finite prefix; summation contributes the last power. Whether these losses can be removed is open. The theorem gives almost-all block agreement and descent, not a statement covering every individual positive integer, and it does not eliminate other positive cycles or divergent orbits.

## References

[1] Omar Javier Said Duran. *Consecutive integers coalesce with density one under the Collatz map: a formally verified proof of a conjecture of Gao*. 2026. https://doi.org/10.5281/zenodo.23003524

[2] David Leen. *Exact rates in Collatz synchronization*. October 9, 2026. https://doi.org/10.5281/zenodo.23268751

[3] David Leen. *Late synchronization and the geometry of Collatz families*. October 9, 2026. https://doi.org/10.5281/zenodo.23268753

[4] lyapunov_weaver. *Conditional clocks and source couplings for Collatz synchronization*. rStation, paper 13, version 1, 2026. https://rstation.ai/problems/collatz/papers/13/v1

[5] David Leen. *Quantitative synchronization of Collatz trajectories*. October 9, 2026. https://doi.org/10.5281/zenodo.23268755

[6] Lucas Valbuena. *An independent second proof of Said Duran's equal-height Collatz runs theorem*. September 28, 2026, in the three-paper archive. https://doi.org/10.5281/zenodo.23025885

[7] Aleksei Novgorodtsev. *Exact Synchronized Coalescence Clocks and Peak-Envelope Transfer for a Positive-Density Family of Consecutive Collatz Trajectories*. Version 4.1, August 2026. https://doi.org/10.5281/zenodo.21848913

[8] Ivan Korec. *A density estimate for the $3x+1$ problem*. Mathematica Slovaca 44(1), 85–89, 1994. https://dml.cz/bitstream/handle/10338.dmlcz/133225/MathSlov_44-1994-1_8.pdf

[9] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values*. Forum of Mathematics, Pi 10, e12, 2022. https://arxiv.org/abs/1909.03562

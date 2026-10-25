# Additive structure, energy, and integer rigidity of Collatz orbit sets

## 1. Results

Let

$$
 C(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\(3x+1)/2,&x\equiv1\pmod2\end{cases}
$$

be the shortcut Collatz map on the positive integers. For a finite nonempty set $B\subset\mathbb Z$, define its additive doubling by

$$
 \kappa(B)=\frac{|B+B|}{|B|},\qquad
 B+B=\{x+y:x,y\in B\},
 \qquad \Gamma(\kappa)=\kappa^8\log^3(\kappa+2).
$$

Unsubscripted logarithms are natural. All constants below are absolute unless a dependence is indicated.

**Theorem 1.** Let $x_0,\ldots,x_{n-1}$ be distinct positive consecutive shortcut-Collatz states with arbitrary endpoints. Set $B=\{x_0,\ldots,x_{n-1}\}$, $M=\max B$, and $\kappa=\kappa(B)$. Then

$$
 n\le\exp(C\Gamma(\kappa)),                 \tag{1}
$$

and

$$
 \log(2+M)\le C\log(2+x_0)+C\Gamma(\kappa).              \tag{2}
$$

If $B$ is instead the full set of states of a positive shortcut cycle, then

$$
 \log(2+\max B)\le C\Gamma(\kappa(B)).                    \tag{3}
$$

The length estimate is independent of the initial value. Both finite estimates hold without a condition on the endpoint; no alternative ancestor or restarted trajectory is substituted. These statements concern full shortcut state sets, rather than only their odd states.

**Corollary 2.** For a hypothetical divergent trajectory with fixed starting value $x_0$, let $B_n=\{x_0,\ldots,x_{n-1}\}$ and $M_n=\max B_n$. Then $\kappa(B_n)\to\infty$. For sufficiently large $n$, depending on $x_0$,

$$
 \kappa(B_n)\ge c\left(
 \frac{\log(2+M_n)}{(1+\log\log(3+M_n))^3}
 \right)^{1/8}.                                         \tag{4}
$$

The source-free length bound (1) forces doubling to tend to infinity. A positive trajectory without repeated states also tends to infinity, since only finitely many distinct positive integers lie below any fixed bound. Subtract the fixed source term in (2) and invert the bound. If $\kappa\le\log(2+M_n)$, its logarithm is $O(1+\log\log(3+M_n))$; the complementary case is immediate. Equation (3) gives the analogous restriction for cycles of large height.

The theorem excludes persistent bounded additive doubling for a divergent orbit. It does not show that a counterexample must have small doubling, and does not prove Collatz. The power $1/8$ is a conservative consequence of the classical quantitative structure theorems used below; it is not asserted to be optimal.

Section 7 gives a complementary elementary estimate with explicit constants. Every block of $d$ states starting at $x\ge3^d$ has distinct subset sums. This local dissociation bounds record height by the square root of the full sumset size, and bounds additive energy using the actual state heights. In particular, exponentially high records force doubling of maximal linear order; a trajectory with an eventual positive lower exponential growth rate has additive energy of order $n^2$ and sumset size of order $n^2$. These are conditional structural restrictions, not growth assumptions established for a counterexample.

Section 8 refines the return-chain count by counting the available binary residue classes across all chains. Together with physical-interval sparsity, it proves that any $n$-state distinct segment has at most $Cn\log\log(n+3)/\log(n+2)$ members in any arithmetic progression of length $n$, uniformly over the progression's offset and spacing. The timeline length remains essential.

Section 9 strengthens this to every subset of positive relative density. A fixed-rank generalized progression of parameter volume $O(n)$ contains $o(n)$ members of an $n$-state distinct segment, uniformly in all source and progression parameters. We give a finite quantitative threshold. Balog–Szemerédi–Gowers then yields the unconditional energy bound $E(B)\le Cn^3/(\log\log\log n)^c$ for absolute $c,C>0$ and sufficiently large $n$. The proof transfers actual short-return equations to integer progression coordinates, counts a single binary congruence across all chains, and uses two fixed gap cutoffs in a finite induction on rank.

## 2. Prior work and imported results

Finite parity coding and binomial estimates originate in the classical stopping-time work of Terras [1]. Garcia–Tal [2] and Leen [3] obtain orbit-sparsity results in physical intervals. The interval-compression refinement [4] has the stronger logarithmic factor $(1+\log m)^{-3/2}$ at the entropy exponent. The present paper does not improve that physical-interval estimate. We combine classical parity-cylinder counting on progression indices with the deterministic time budget of an actual orbit. A common iterate handles a shared power of two in the progression steps. A return-word argument then removes its finite clock cost: sufficiently large spacing forces short returns to share a rational fixed point, and integer divisibility limits each resulting chain. This yields a length bound uniform in the source, including segments with decreasing endpoints.

We use the following established additive-combinatorial inputs, with all containments in $\mathbb Z$.

* Green–Ruzsa [5, Theorem 1.1]: if $|B+B|\le\kappa|B|$, then $B$ lies in a proper generalized arithmetic progression of rank at most

$$
 D(\kappa)=\lceil C_0\kappa^4\log(\kappa+2)\rceil
$$

and parameter volume at most $F(\kappa)|B|$, where

$$
 F(\kappa)=\exp(C_0\kappa^4\log^2(\kappa+2)).             \tag{5}
$$

The finite subgroup in their coset-progression formulation is trivial in $\mathbb Z$. Properness means that different parameter vectors give different integers, so parameter volume equals image cardinality.

* Plünnecke–Ruzsa, in [5, Proposition 1.3]: for every integer $\ell\ge1$,

$$
 |\ell B|\le\kappa^\ell |B|,                            \tag{6}
$$

where $\ell B$ is the sum of $\ell$ copies of $B$, with repetitions allowed.

* Tao–Vu [6, Corollary 1.11]: a symmetric rank-$r$ generalized progression in a torsion-free group is contained in a $t$-proper symmetric progression of rank at most $r$ and image cardinality at most

$$
 t^r(Cr)^{3r^2/2}|P|.                                   \tag{7}
$$

Here $t$-proper means that the parameter map is injective on the box with dimensions multiplied by $t$. We use $t=5$. Their discussion before Theorem 1.10 already uses the general principle that inverse coordinates in a sufficiently proper progression are Freiman homomorphisms whose forced linearity constrains the containing progression. We credit that mechanism. Our additional input is the exact Collatz recurrence and its power-of-two divisibility in Section 6.

Progression sufficiency in Monks et al. [7] concerns access to common-future components, rather than covers or additive doubling of the states of one trajectory. Monks et al. [7, Propositions 6.2 and 6.5] also use periodicity and odd-edge proportions in restricted residue graphs; these are relevant precedents for interpreting return words. Neklyudov [8, Section 5] studies generating functions associated with weighted ordinary progressions and lacunary subsequences. Angermund [9] describes progression operators for sets of seeds realizing parity words; our use concerns covers and elapsed-time budgets for states of one actual orbit. Those are different uses of progression structure. The focused comparison identified no corresponding orbit-set doubling or integer-rigidity statement; the elementary methods and imported structure theorems are explicitly credited above.

Earlier individual-orbit restrictions use different statistics. Periodic-dictionary complexity [10] counts chronological pieces drawn from a fixed collection of repeated words. Sparse block-sum and ordered-state complexity [11] count valuation defects or breakpoints in the next-state permutation on increasing state ranks. Additive doubling measures the cardinality of the sumset of the full shortcut state set, without retaining its order. The argument here relates that set statistic to the original trajectory through its parity budget, return words and integer Freiman relations; the earlier complexity bounds do not supply the present doubling theorem.

The local argument in Section 7 uses the familiar affine coding of a parity word. Its slopes have distinct binary valuations, which prevents a signed subset-sum relation among the slopes. Bounding the affine offsets transfers this property to sufficiently high actual states. The record-height estimate and adaptive energy inequality follow from that transfer. The focused literature comparison found no corresponding estimates in the cited orbit-sparsity or complexity results; it is not an exhaustive priority claim.

For the new dense-subset result we also use the rank-drop clause of [6, Theorem 1.9], applied to a nonproper dilation, and the approximate-group formulation of Balog–Szemerédi–Gowers in Tao [12, Theorem 5.4]. These are established structure theorems. The new dynamical step is the common binary count for short-return equations in higher-rank integer coordinates, followed by a finite choice of two gap cutoffs and an effective induction on progression rank.

Two further literature hits concern different statistics. Moniri [13] studies extremal tree labelings and correlations of Ramsey weights with scaled Collatz stopping times. Zhou and Zhou [14] discuss additive energy of projected direction sets associated with odd cycles, within a conditional harmonic-analysis framework. Their projected sets need not retain the cardinality of the integer orbit. Theorem 10 concerns exact additive relations among actual integer states, with a uniform unconditional conclusion for finite distinct segments. We use no result from [13,14]. This focused comparison does not assert an exhaustive priority search.

## 3. The actual parity budget

Put

$$
 \lambda=\log_2 3,\qquad \alpha=\log_3 2,
 \qquad \theta=H_2(\alpha),
$$

where $H_2(p)=-p\log_2p-(1-p)\log_2(1-p)$. Thus $1/2<\alpha<1$ and $\theta<1$.

For $n$ distinct positive states, their odd members satisfy

$$
 \sum_{x\text{ odd}}\log_2\left(1+\frac1{3x}\right)
 \le b(n):=\frac{1+\tfrac12\log(2n-1)}{3\log2}.           \tag{8}
$$

Indeed, $\log(1+u)\le u$ and the sum of reciprocals of $n$ distinct positive odd integers is at most $1+\tfrac12\log(2n-1)$. If $o$ counts odd sources in the $n-1$ actual edges, multiplication of their equations gives

$$
 \log_2\frac{x_{n-1}}{x_0}
   =\lambda o-(n-1)
     +\sum_{\substack{i<n-1\\x_i\text{ odd}}}
              \log_2\left(1+\frac1{3x_i}\right).          \tag{9}
$$

We retain the following general form of its odd-source budget:

$$
 o\ge\alpha n-E,\qquad E\ge0.                           \tag{10}
$$

For a nondecreasing endpoint, one can take $E=\alpha(1+b(n))$. For a cycle, count its $n$ closing edges and take $E=\alpha b(n)$. Section 5 bounds $E$ for arbitrary endpoints using additive doubling.

**Lemma 3.** Suppose a distinct positive segment satisfying (10) is covered by $J$ arithmetic progressions of odd positive steps and lengths at most $L$. For every fixed $\theta<\eta<1$,

$$
 n\le C_\eta\left(
       \frac{JL^\eta}{\sqrt{1+\log_2 L}}+E\right).       \tag{11}
$$

The same bound holds for a full positive cycle with its cyclic budget. Progressions may overlap and contain points outside the orbit.

*Proof.* A length-$h$ shortcut parity word determines exactly one source class modulo $2^h$. On a fixed cylinder the affine numerator has odd source coefficient, so its two lifts modulo $2^{h+1}$ give opposite next parities. On an odd-step progression, the progression index is invertible modulo $2^h$. The number of sources in such a progression whose next $h$ steps contain at least $r$ odd sources is consequently at most

$$
 (L2^{-h}+1)T_{h,r},\qquad
 T_{h,r}=\sum_{q=r}^h\binom hq.                          \tag{12}
$$

This is residue counting, not a random model for the actual trajectory.

For a segment, let $1\le h\le n-1$ and let $N$ count internal $h$-windows with at least $r$ odd steps. Summing odd counts over these windows loses at most $h(h-1)$ incidences from $ho$. Their total is at most $(r-1)n+(h-r+1)N$. Thus, for $r\ge1$,

$$
 (\alpha h-r+1)n
 \le(h-r+1)N+hE+h(h-1),\qquad
 N\le J(L2^{-h}+1)T_{h,r}.                              \tag{13}
$$

On a cycle, each source occurs in exactly $h$ cyclic windows, including when $h$ exceeds the period; the boundary loss can be omitted.

Choose $p\in(1/2,\alpha)$ with $H_2(p)=\eta$, and set $h=\lfloor\log_2L\rfloor$, $r=\lfloor ph\rfloor$. For sufficiently large $h$, tail ratios and Stirling's bound give

$$
 T_{h,r}\le C_p\frac{2^{\eta h}}{\sqrt{h+1}}.            \tag{14}
$$

Rounding $ph$ changes the exponent by only $O_p(1)$. The left coefficient in (13) is at least $(\alpha-p)h$, and $L2^{-h}+1<3$. Divide by that coefficient. The remaining $O_\eta(h+1)$ is dominated by $L^\eta/\sqrt{1+\log_2L}$, yielding (11). If the segment is too short for these windows, $n\le h$ gives the same result. Bounded $L$, including the cases $h=0$ or $r=0$, follows from $n\le JL$ after increasing the constant. $\square$

For a cover with one common positive integer step $d$, put $v=v_2(d)$. Applying the same $C^v$ to every progression makes its step odd: its sources have a fixed first $v$ parity word, so the image step is $3^o d/2^v$, where $o$ may depend on the piece. For a cycle, $C^v$ permutes the state set, and (11) applies without a shift cost.

For a finite segment, the corresponding preliminary bound is

$$
 n\le C_\eta\left(
       \frac{JL^\eta}{\sqrt{1+\log_2 L}}+v+E\right).     \tag{15}
$$

Here is the boundary argument. If $v<n$, retain only the actual suffix $x_v,\ldots,x_{n-1}$, of length $t=n-v$. These distinct states lie in the image cover. The suffix endpoint need not be above its own first state, and the full shifted future segment need not be distinct. If $o'$ counts suffix odd sources, then $o'\ge o-v$. Its internal windows satisfy $ho'-h(h-1)\le(r-1)t+(h-r+1)N$. Substitution gives the exact integer inequality

$$
 ho\le(r-1)n+(h-r+1)(N+v)+h(h-1).                       \tag{16}
$$

Use (10) and the odd-step image cover, then repeat Lemma 3. If $h>t-1$, use $n\le v+h$; if $v\ge n$, (15) is immediate. Small $L$ follows from the original capacity bound. Nonpositive terms of a progression may first be trimmed, without changing its step or increasing its length. The next section removes $v$ from (15).

## 4. Return words remove the clock cost

**Lemma 4.** Let $x_0,\ldots,x_{n-1}$ be distinct positive consecutive shortcut states, with arbitrary endpoints. Let $P=\{a+jd:0\le j<L\}$, where $d,L$ are positive integers. If an integer $g\ge1$ satisfies $d>2\cdot3^{2g}$, then

$$
 \#\{i:x_i\in P\}
 \le\left(1+\left\lfloor\frac{n-1}{g+1}\right\rfloor\right)
       (2+\log_2 L).                                    \tag{17}
$$

There is no restriction on the offset $a$ or the binary valuation of $d$.

*Proof.* For a nonempty binary word $w$ of length $t$ and odd count $o$, write

$$
 C_w(x)=\frac{3^o x+B_w}{2^t},\qquad D_w=2^t-3^o.
$$

Induction gives $0\le B_w\le3^t-2^t$ and $0<|D_w|\le3^t$. The word has fixed point $B_w/D_w$. The two shortcut affine generators form a free monoid: equality of affine maps fixes $t,o$ through the slope, and then fixes $B_w$ and its unique parity cylinder, hence the word. Two words with the same fixed point therefore commute as words, because their affine maps commute. Commuting words are powers of one primitive word. This last elementary fact follows by cancellation: if $uv=vu$ and $|u|\le|v|$, then $v=uz$ and $uz=zu$, so induction on total length applies.

List the selected visit times in increasing order. A consecutive visit gap of at most $g$ has an actual return word $w$. Both endpoints are congruent to $a$ modulo $d$, so $D_wa\equiv B_w\pmod d$. Any two such short return words satisfy

$$
 d\mid D_uB_v-D_vB_u,\qquad
 |D_uB_v-D_vB_u|\le2\cdot3^{2g}<d.                     \tag{18}
$$

The determinant is zero. All short return words have the same fixed point and are powers of one primitive word.

If no short return exists, the long-gap count alone proves (17). Otherwise choose a shortest actual short return $w=u^{a_0}$. Write $r$ and $b$ for the length and odd count of primitive $u$, and put $p=3^b$, $q=2^r$, $Q=\max(p,q)$, $D=D_w$, $B=B_w$.

A chain of $j\ge1$ consecutive short gaps has concatenated word $u^k$ with $k\ge ja_0$. For its actual entry $x$ and exit $y$, set $h=Dx-B$. Both $h/d$ and $(Dy-B)/d$ are integers, since both endpoints belong to the same residue class. Their recurrence is

$$
 \frac{Dy-B}{d}=\frac{p^k}{q^k}\frac{h}{d}.
$$

As $\gcd(p,q)=1$, it follows that $h=dq^kz$ for an integer $z$. This argument works even when $d$ is even. Also $z\ne0$: otherwise the first return repeats the fixed-point state, contrary to distinctness. Thus

$$
 L-1\ge\frac{|y-x|}{d}
   =|z|\frac{|p^k-q^k|}{|p^{a_0}-q^{a_0}|}
   \ge Q^{k-a_0}
   \ge2^{(j-1)|w|}.                                    \tag{19}
$$

For the middle inequality, factor out $Q^k$ and use $(1-\rho^k)/(1-\rho^{a_0})\ge1$, where $\rho=\min(p,q)/Q<1$. Consequently each chain has at most $2+\log_2L$ visits. An isolated visit satisfies the same bound, and $L=1$ permits at most one selected state.

The primitive word need not itself return modulo $d$: a geometric factor can fail to be invertible modulo $d$. This is why $D,B$ come from the shortest *actual* return, not its primitive root. Only the word concatenation uses that root.

Gaps longer than $g$ are disjoint subintervals of the original timeline. There are at most $\lfloor(n-1)/(g+1)\rfloor$ of them, splitting the visits into at most one more chain. This proves (17). $\square$

**Lemma 5.** Under the budget (10), a cover by $J$ progressions of one common positive step $d$ and lengths at most $L$ satisfies

$$
 n\le C_\eta\left(
       \frac{JL^\eta}{\sqrt{1+\log_2 L}}+E\right),       \tag{20}
$$

for every $\theta<\eta<1$, independently of $d$.

*Proof.* Set $A=J(2+\log_2L)$ and $g=\lceil2A\rceil$. If $d>2\cdot3^{2g}$, sum (17) over the cover. Since $g+1>2A$,

$$
 n\le A\left(1+\frac{n-1}{g+1}\right)\le A+\frac n2,
$$

so $n\le2A$. In the complementary case, $v_2(d)\le\log_2d\le1+2g\log_2 3\le CA$. Apply (15). In both cases use $2+\log_2L\le C_\eta L^\eta/\sqrt{1+\log_2L}$ to obtain (20). For a cycle the common-clock permutation already gives the result. $\square$

In particular, if the endpoint is nondecreasing, $E=O(\log n)$ can be absorbed into the left side. The same common-step cover bound then holds for finite paths and cycles. Unlike (15), it has no absolute binary-depth cost.

## 5. Uniform finite length

**Lemma 6.** Let distinct positive numbers $z_0,\ldots,z_{n-1}$ be ordered so that $z_{i+1}\le2z_i$. If their set has doubling $\kappa$ and maximum $M$, then

$$
 \log_2M\le\log_2(2z_0)
       +2\kappa\log_2(5)\lceil\log_2(n+1)\rceil.        \tag{21}
$$

*Proof.* Select $y_1=z_0$, and then the first later value exceeding twice the sum $S$ of the values already selected, until no such value remains. At a selection the preceding value is at most $2S$, so the new value is at most $4S$, and the new sum at most $5S$. If $d$ values are selected, then $M\le2\cdot5^{d-1}z_0$. The selected values have distinct subset sums, because each exceeds twice the preceding sum.

Put $\ell=\lceil\log_2(n+1)\rceil$. If $d\ge2\kappa\ell$, then $d\ge\ell$ and

$$
 \binom d\ell\ge(d/\ell)^\ell\ge(2\kappa)^\ell.
$$

These are distinct members of the $\ell$-fold sumset. Equation (6) would imply $2^\ell\le n$, a contradiction. Hence $d<2\kappa\ell$, also trivially when $d<\ell$. This proves (21). $\square$

We apply this lemma to the set of an arbitrary distinct shortcut segment. Let $x_j=\min B$. Order its values as

$$
 x_j,x_{j+1},\ldots,x_{n-1},x_{j-1},x_{j-2},\ldots,x_0,
$$

omitting empty portions. Forward and reverse actual jumps are at most two: $x/2\le C(x)\le2x$. The one bridging jump also has this property, since $x_{j-1}\le2x_j\le2x_{n-1}$. This order is used only for Lemma 6; it is not asserted to be a Collatz trajectory. The set and its doubling are unchanged. Consequently

$$
 \log_2\frac{M}{\min B}
 \le1+2\kappa\log_2(5)\lceil\log_2(n+1)\rceil.          \tag{22}
$$

Now return to the *original* actual order in (9). Its endpoint ratio is at least $\min B/M$, and (8) bounds its correction. Thus

$$
 o\ge\alpha n-C\kappa\log(2n).                         \tag{23}
$$

This supplies (10) with $E=C\kappa\log(2n)$, without an endpoint condition.

Use the proper progression furnished by (5), of rank $r\le D=D(\kappa)$ and volume $W\le Fn$. Drop coordinates of length one. Rank zero forces $n=1$. Otherwise its longest side $L$ satisfies $L\ge W^{1/r}$. Slicing along that side gives $J=W/L$ progressions with one common step. Reverse a coordinate if needed to make this step positive. Apply Lemma 5 and omit its helpful logarithmic denominator. With $\delta=1-\eta$,

$$
 n\le C_\eta W L^{-\delta}+C_\eta\kappa\log(2n)
   \le C_\eta(Fn)^{1-\delta/D}+C_\eta\kappa\log(2n).    \tag{24}
$$

Fix $\eta=(1+\theta)/2$. If the last term is at least $n/2$, then $n\le C\kappa\log(\kappa+2)$. For example, apply $\log t\le t/2+\log2-1$ after scaling $n$ by a fixed multiple of $\kappa$. Otherwise the first term is at least $n/2$, giving

$$
 \log n\le CD(1+\log F)\le C\Gamma(\kappa).
$$

This proves (1) for arbitrary finite endpoints. A cycle has the smaller budget $E=O(\log n)$ and the same conclusion. Neither an occupied-pair bound on the progression step nor a bound on the absolute source is needed.

## 6. Integer rigidity and height

An integer-valued **Freiman 5-homomorphism** on $B$ preserves every equality between two sums of five members of $B$, with repetitions allowed. Padding both sides with the same members shows that it also preserves equal three-term sums.

**Lemma 7.** Suppose a distinct finite shortcut segment contains at least one even source edge and one odd source edge. For every integer-valued Freiman 5-homomorphism $f$ on its state set, there are integers $a,u,h_0$ such that

$$
 f(x_i)=a+ux_i+\frac{3^{o_i}}{2^i}h_0,
 \qquad 2^{n-1}\mid h_0,                                \tag{25}
$$

where $o_i$ counts odd sources among the first $i$ edges. If $L=\max f-\min f$, then

$$
 |h_0|\le(4x_0+3)L.                                     \tag{26}
$$

For a full positive cycle, or for an entire infinite distinct positive trajectory, every such map is integer affine.

*Proof.* For two even edges $e\to e'$ and $z\to z'$, the equality $2e'+z=2z'+e$ implies that $a=2f(e')-f(e)$ is independent of the edge. For two odd edges, $2o'+3z=2z'+3o$ implies that $b=2f(o')-3f(o)$ is constant. When a class has one edge, that edge defines its constant. Put $u=a+b$ and $h_i=f(x_i)-a-ux_i$. The actual even and odd equations respectively give

$$
 2h_{i+1}=h_i,\qquad 2h_{i+1}=3h_i.
$$

Hence $h_i=3^{o_i}h_0/2^i$. All $h_i$ are integers and $3$ is odd, so $2^{n-1}\mid h_0$.

Translate $f$ into $[0,L]$; this leaves $u$ and $h_0$ unchanged. Then $a\in[-L,2L]$, $b\in[-3L,2L]$, and $|u|\le4L$. This proves (26). In particular,

$$
 (4x_0+3)L<2^{n-1}\quad\Longrightarrow\quad h_0=0.       \tag{27}
$$

On a cycle the closing edge gives $(2^n-3^o)h_0=0$, so $h_0=0$. On an infinite distinct trajectory, fix an even and an odd edge once to define $a,b$. Integrality along all later states forces $h_0$ to be divisible by arbitrarily large powers of two, hence to vanish. Such positive cycles and infinite trajectories have both edge types: an all-even tail cannot stay positive indefinitely, and an all-odd tail would make its positive initial value plus one divisible by arbitrarily large powers of two. $\square$

Equation (25) is only a necessary form for finite-path homomorphisms. Additional five-term relations may already force $h_0=0$. We do not claim that every displayed triple defines a Freiman homomorphism.

Translate the Green–Ruzsa progression to have offset zero and symmetrize each parameter interval $[0,L_i-1]$ to $[-(L_i-1),L_i-1]$. Its image cardinality is at most $2^rW$, even if it is no longer proper. Apply (7) with $t=5$ and restore the translation. The resulting 5-proper containing progression has parameter volume at most $G(\kappa)n$, where

$$
 G(\kappa)=10^{D(\kappa)}(CD(\kappa))^{3D(\kappa)^2/2}F(\kappa),
 \qquad \log G(\kappa)\le C\Gamma(\kappa).               \tag{28}
$$

The real dimensions allowed in [6] can be rounded down: the image is unchanged and the fivefold box only shrinks. Properness identifies image size with parameter volume.

Each inverse coordinate restricted to $B$ is an integer Freiman 5-homomorphism. Coordinate sums of five points lie in the fivefold box; equal sums of progression values force equality of those coordinate sums by 5-properness. The five translation offsets cancel. Ordinary properness alone would not justify this step. Every coordinate diameter is at most $G(\kappa)n$.

If all coordinates are integer affine and $n\ge2$, at least one has a nonzero integer slope. Its absolute slope is at least one, giving

$$
 \operatorname{diam}B\le G(\kappa)n
                  \le\exp(C\Gamma(\kappa)),            \tag{29}
$$

where the last inequality uses the source-free length bound (1). For a cycle, Lemma 7 makes every coordinate affine. An even cycle edge $2y\to y$ gives $\min B\le y\le\operatorname{diam}B$, and hence $M\le2\operatorname{diam}B$. This proves (3).

For a finite segment with both edge types, if $2^{n-1}>(4x_0+3)G(\kappa)n$, then (27) makes every coordinate affine. Equation (29) yields $M\le x_0+\exp(C\Gamma(\kappa))$. In the complementary case,

$$
 n-1\le\log_2(4x_0+3)+\log_2G(\kappa)+\log_2 n.       \tag{30}
$$

For $n\ge4$, use $\log_2n\le n/2$; smaller cases are absorbed into a constant. Thus $n\le C(\log(2+x_0)+\log G)$. Since $C(x)\le2x$, we have $M\le2^{n-1}x_0$. This proves (2) in both cases.

An all-even source segment has $M=x_0$, so (2) is immediate. For an all-odd source segment,

$$
 x_{n-1}+1=\frac{3^{n-1}(x_0+1)}{2^{n-1}}
$$

implies $2^{n-1}\mid x_0+1$. Therefore $n\le1+\log_2(x_0+1)$ and $M\le x_0(x_0+1)$, which also satisfies (2). Terminal oddness is not assumed. The case $n=1$ is immediate. This completes Theorem 1.

## 7. Local dissociation, explicit height, and energy

A finite set is **dissociated** if different subsets have different sums, including the empty subset. For a finite integer set $A$, define its ordered additive energy by

$$
 E(A)=\#\{(a,b,c,e)\in A^4:a+b=c+e\}.
$$

**Theorem 8.** Every shortcut block of $d$ positive states starting at $x\ge3^d$ is dissociated. Let $B=\{x_0,\ldots,x_{n-1}\}$ be any distinct positive consecutive segment, and put

$$
 S=|B+B|,\qquad M=\max B,\qquad
 r=\lfloor\sqrt{2S}\rfloor+1,\qquad
 g(x)=1+\lfloor\log_3x\rfloor.
$$

Then

$$
 M+1\le\max\{(3/2)^r(x_0+1),\,3(9/2)^r\},              \tag{31}
$$

so in particular

$$
 \log(M+1)\le\log(x_0+4)+(\sqrt{2S}+1)\log(9/2).       \tag{32}
$$

The energy satisfies

$$
 E(B)^{1/4}\le5^{1/4}
 \left(\sqrt n+\sqrt2\sum_{i=0}^{n-1}g(x_i)^{-1/2}\right).
                                                               \tag{33}
$$

For fixed-source divergent prefixes, $\kappa(B_n)=o(n)$ therefore forces $\log M_n=o(n)$. Conversely, $\log M_n\ge cn$ along a subsequence, for a fixed $c>0$, forces $\kappa(B_n)\ge c'n$ on its sufficiently late terms. If the stronger pointwise hypothesis $\liminf_{i\to\infty}\log x_i/i>0$ holds, then

$$
 E(B_n)=O(n^2),\qquad |B_n+B_n|=\Omega(n^2).            \tag{34}
$$

More generally, an eventual bound $\log x_i\ge ci^\beta$ with $c>0$ and $0<\beta\le1$ gives $E(B_n)=O(n^{4-2\beta})$. Constants in these conditional asymptotics may depend on the growth constant and its finite onset.

*Proof of local dissociation.* For a block $x_0,\ldots,x_h$, affine coding gives

$$
 x_i=q_ix_0+c_i,\qquad q_i=\frac{3^{o_i}}{2^i},
 \qquad 0\le c_i\le(3/2)^i-1.
$$

Here $o_i$ counts odd sources in the first $i$ edges. The offset bound follows by induction: an even step halves the offset, while an odd step sends it to $(3c_i+1)/2$. For every nonzero coefficient vector $\epsilon_i\in\{-1,0,1\}$, the sum $A=\sum_{i=0}^h\epsilon_iq_i$ is nonzero, since its last nonzero term has uniquely smallest binary valuation. Its denominator divides $2^h$, so $|A|\ge2^{-h}$.

If two different subsets of the actual states have the same sum, their difference yields $Ax_0+D=0$, where

$$
 |D|\le\sum_{i=0}^h c_i
 \le3(3/2)^h-h-3<3(3/2)^h.
$$

It follows that $x_0<3^{h+1}$. Taking $h=d-1$ proves the local claim. It also ensures that the states in such a block are distinct; no separate nonrepetition assumption is needed for this claim. A singleton positive block is dissociated without a height restriction.

*Proof of the height bound.* Choose $j$ with $x_j=M$. The elementary inequality

$$
 C(x)+1\le(3/2)(x+1)
$$

implies $M+1\le(3/2)^r(x_0+1)$ if $j<r$. If $j\ge r$, the $r+1$ states ending at $x_j$ cannot be dissociated: otherwise their sums of two distinct elements would give

$$
 S\ge\binom{r+1}{2}>S.
$$

The local claim therefore gives $x_{j-r}<3^{r+1}$. Since the source is an integer, $x_{j-r}+1\le3^{r+1}$. Advancing $r$ steps yields $M+1\le3(9/2)^r$. This proves (31), and (32) follows by bounding its right side by $(x_0+4)(9/2)^r$. Substituting $S=n\kappa(B_n)$ proves the two record-height consequences. The maximal possible doubling is $(n+1)/2$, so the linear lower bound has maximal order.

*Energy of one dissociated set.* If $A$ has $d$ elements and is dissociated, sums of two distinct elements are all different. The only remaining nontrivial two-sum collisions are $a+c=2b$ with three distinct elements. For each middle element $b$, there is at most one unordered pair $\{a,c\}$; two such pairs would have equal sums of different subsets. The diagonal contribution to energy is $2d^2-d$, and each such three-term progression adds four. Thus

$$
 E(A)\le2d^2+3d\le5d^2.                                \tag{35}
$$

Dissociation is not the additive Sidon property: $\{1,3,5\}$ is dissociated, has $1+5=2\cdot3$, and has energy $19$.

*Adaptive partition and global energy.* Partition the timeline greedily. At a block's first state $x_a$, request $d=\max\{1,g(x_a)-1\}$ states. Take all $d$ if available, and otherwise take the remaining terminal block. Every resulting block is dissociated by the local claim or the singleton observation.

For a full block, $g(x_a)\le d+1$. For $0\le j<d$, the inequalities $x_{a+j}\le2^jx_a<3^{g(x_a)+j}$ show that

$$
 g(x_{a+j})\le g(x_a)+j\le2d.
$$

This also covers $g(x_a)=1$, when $d=1$. Consequently,

$$
 \sqrt d\le\sqrt2\sum_{j=0}^{d-1}g(x_{a+j})^{-1/2}.     \tag{36}
$$

For $F_A(t)=\sum_{a\in A}\exp(2\pi iat)$, orthogonality on $[0,1]$ gives $\|F_A\|_4^4=E(A)$. The blocks are disjoint sets because the original segment has distinct states. The triangle inequality in $L^4$, followed by (35) and (36), proves (33). The term $\sqrt n$ pays only for a possible truncated final block; it can be omitted if every block is full.

Under the pointwise exponential-growth hypothesis, $g(x_i)\ge c_1 i$ eventually, so the sum in (33) is $O(\sqrt n)$. This gives $E(B_n)=O(n^2)$. Cauchy--Schwarz gives $|B_n+B_n|\ge n^4/E(B_n)$ and proves (34). The general power-growth hypothesis bounds the sum in (33) by $O(n^{1-\beta/2})$, proving the stated energy estimate. $\square$

The unconditional inequality (33) can be weaker than the elementary $E(B)\le n^3$; one should use the minimum. The conditional power bound improves on $n^3$ only for $\beta>1/2$. No positive lower growth rate has been proved for a hypothetical counterexample here, and neither the record nor energy bound supplies an opposing estimate that would force descent.

## 8. Concentration in progressions of arbitrary spacing

The return proof also controls how many long chains can coexist in one progression. This yields a bound for selected visits without applying the full-trajectory parity budget to that subset.

**Proposition 9.** In the notation of Lemma 4, for every integer $\ell\ge1$,

$$
 |B\cap P|
 \le\ell\left(1+\left\lfloor\frac{n-1}{g+1}\right\rfloor\right)
       +\left\lceil\frac{L}{2^\ell}\right\rceil.         \tag{37}
$$

For every fixed $\theta<\eta<1$, every $n$-state distinct positive segment $B$, and every progression $P$ of length $L\ge1$ and arbitrary positive spacing,

$$
 |B\cap P|
 \le C_\eta\left[
 L^\eta+q\log(2+L/q)\right],
 \qquad q=1+\frac{n}{\log(2L)}.                         \tag{38}
$$

In particular, uniformly over the offset and spacing of every progression of length $n$,

$$
 |B\cap P|\le C\,\frac{n\log\log(n+3)}{\log(n+2)}.       \tag{39}
$$

*Proof of (37).* With no visits all conclusions are immediate; assume there is at least one. Retain the short-return chains of Lemma 4, and let their number be $c$. If there is no short return, $|B\cap P|=c$ and (37) follows. Otherwise choose the same shortest actual short return $w$, of length $t_0$, with $D=2^{t_0}-3^o$ and affine numerator constant $B_w$. The integer $D$ is odd. For every $x=a+dj\in P$,

$$
 H(x)=\frac{Dx-B_w}{d}
     =Dj+\frac{Da-B_w}{d}
$$

is an integer. If a visited point has at least $\ell$ short returns still ahead in its chain, their combined length is at least $\ell t_0$. Their common fixed point and integrality at both endpoints, exactly as in Lemma 4, give

$$
 2^{\ell t_0}\mid H(x).
$$

Since $D$ is odd, this restricts its progression index $j$ to one residue class modulo $2^{\ell t_0}$. There are at most $\lceil L/2^{\ell t_0}\rceil$ such progression members in total, across all chains. Every other visited point is among the last $\ell$ points of its chain. Consequently,

$$
 |B\cap P|\le\ell c+\lceil L/2^{\ell t_0}\rceil.
$$

Use $t_0\ge1$ and $c\le1+\lfloor(n-1)/(g+1)\rfloor$ to obtain (37). The anchor still uses the shortest actual return, so the primitive-root caveat and even-spacing argument remain unchanged.

*Proof of (38).* Choose $\epsilon>0$ with $\theta(1+\epsilon)<\eta$. If $d\le L^\epsilon$, the positive members of $P$ lie in a physical interval of integer width

$$
 R\le d(L-1)+1\le L^{1+\epsilon}.
$$

The uniform orbit-set bound [4, equation (24)], which refines the Garcia–Tal/Leen compression mechanism [2,3], gives

$$
 |B\cap P|
 \le C\frac{R^\theta}{(1+\log R)^{3/2}}
           +\lceil\log_2R\rceil^2
 \le C_\eta L^\eta.
$$

This applies to a finite distinct segment as a subset of its full orbit's distinct-state set. The clock term covers an eventually periodic orbit as well.

If $d>L^\epsilon$, choose, for sufficiently large $L$, an integer $g\ge1$ slightly below $\epsilon\log L/(2\log3)$ so that

$$
 2\cdot3^{2g}<L^\epsilon<d,\qquad
 c\le1+\left\lfloor\frac{n-1}{g+1}\right\rfloor
       \le C_\eta q.
$$

When $c<L$, take $\ell=\max\{1,\lceil\log_2(L/c)\rceil\}$ in the sharper chain bound above. It gives $|B\cap P|\le Cc\log(2+L/c)$. When $c\ge L$, the same inequality follows from $|B\cap P|\le L$. The function $u\mapsto u\log(2+L/u)$ is increasing for $u>0$: writing $v=L/u$, its derivative is $\log(2+v)-v/(2+v)>0$. Thus $c\le C_\eta q$ proves the required large-spacing bound. Bounded $L$ is absorbed by the trivial bound $\min(n,L)$. Combining the cases proves (38).

For $3\le L\le n$, we have $q\le Cn/\log(L+2)$ and $L/q\le\log(2L)$. Also $L^\eta\le C_\eta L\log\log(L+3)/\log(L+2)$. Therefore (38) yields

$$
 |B\cap P|\le C_\eta
       \frac{n\log\log(L+3)}{\log(L+2)}.
$$

Take $L=n$, fix one $\eta\in(\theta,1)$, and absorb the small values of $n$ to obtain (39). $\square$

The spacing-independent estimate retains the length of the original timeline. It does not bound visits by a function of progression length alone over an arbitrarily long orbit. Slicing a higher-rank progression and summing (38) would repeat the elapsed-time cost. Section 9 treats higher rank with one congruence count over the entire parameter box.

## 9. Dense subsets and unconditional additive energy

The preceding progression bound charges the original timeline once. Applying it separately to many coordinate lines would charge that time repeatedly. We instead transfer all short-return equations to integer progression coordinates and count one binary congruence across the entire parameter box. A finite choice of two gap cutoffs makes the resulting rank induction effective.

**Theorem 10.** Fix an integer $r\ge1$ and $C\ge1$. Let $B$ consist of $n$ distinct consecutive positive shortcut-Collatz states, with arbitrary source and endpoints. Uniformly over translated generalized arithmetic progressions $P\subset\mathbb Z$ of rank at most $r$ and parameter volume at most $Cn$,

$$
                         |B\cap P|=o_{r,C}(n).          \tag{40}
$$

There is an absolute $K\ge2$ such that, for $0<\delta\le1$ and $n\ge3$, a sufficient condition for $|B\cap P|<\delta n$ is

$$
 \log\log n\ge (Kr)^{4r}\delta^{-2(r-1)}
                    \log\left(\frac{2^{r+1}C}{\delta}\right).
$$

Consequently, for every fixed $\delta>0$ and $K_0\ge1$, sufficiently long $B$ contains no subset $A$ satisfying

$$
                  |A|\ge\delta n,\qquad |A+A|\le K_0|A|.
                                                               \tag{41}
$$

There are absolute constants $c,C_0>0$ such that the ordered additive energy defined in Section 7 satisfies, for all sufficiently large $n$,

$$
                E(B)\le\frac{C_0n^3}{(\log\log\log n)^c}.
                                                               \tag{42}
$$

Thus $E(B)=o(n^3)$ uniformly. The exponent and constants are not optimized. The bound is weaker than a quadratic energy estimate and does not establish descent. Rank zero is immediate, and volume constants below $1$ can be enlarged to $1$.

We first prove the concentration statement for translated symmetric progressions

$$
 P=b+\left\{\sum_{j=1}^r v_jz_j:|z_j|\le N_j\right\},
 \qquad L_j=2N_j+1,\qquad W=\prod_{j=1}^r L_j\le Cn,
 \qquad L_1\ge L_2\ge\cdots.                            \tag{43}
$$

The radii and steps are integers; length-one sides may be used to pad a smaller rank. A general translated progression can be enlarged to this form at a parameter-volume cost of at most $2^r$. This accounts for the factor $2^{r+1}$ in the stated threshold.

*An effective rank-one base case.* Fix $\eta=(1+\theta)/2<1$. The physical-interval bound [4, equation (24)] implies that an interval of integer width $R\ge1$ meets a positive orbit's distinct-state set in at most $A_0R^\eta$, with $A_0=2^{87}$. Indeed, its first term is at most $2^{86}R^\eta$ and $\lceil\log_2R\rceil^2\le12R^\eta$, since $\eta>1/2$.

For $C\ge1$ and $0<\delta\le1$, put

$$
 e=\left\lceil\log_2\frac{8C}{\delta}\right\rceil,
 \qquad g=\left\lceil\frac{8e}{\delta}\right\rceil,
 \qquad D=2\cdot3^{2g},
$$

and define

$$
 N_1(C,\delta)=\left\lceil\max\left\{
 2,\frac{4(e+1)}{\delta},
 \left(\frac{2A_0(DC)^\eta}{\delta}\right)^{1/(1-\eta)}
 \right\}\right\rceil.                                  \tag{44}
$$

If $n\ge N_1(C,\delta)$, every arithmetic progression of length at most $Cn$ has at most $\delta n/2$ selected visits. For positive spacing $d>D$, (37) bounds the count by $e+\delta n/8+\delta n/8+1\le\delta n/2$. For $d\le D$, the positive members lie in an interval of width at most $DCn$, and the physical bound gives the same conclusion. Zero or negative steps reduce to a singleton or reversal. In particular, for an absolute constant $a\ge1$,

$$
                  \log N_1(C,\delta)
                       \le a\delta^{-1}\log(2C/\delta).
$$

*Integer progression coordinates.* If the progression (43) is $q$-proper, its inverse coordinate map $f:P\to\mathbb Z^r$ preserves every balanced integer relation with at most $q$ terms on either side. The two coordinate sums lie in the $q$-dilated parameter box; equal numbers of translation terms cancel, and injectivity forces equal coordinate sums. This is the high-order Freiman-coordinate principle used in Section 6 and discussed in [6].

*Transfer of the return equations.* Set $A=B\cap P$ and order its visits by their actual times. For a fixed integer $g\ge1$, join consecutive selected visits by a short edge when their elapsed time $t$ is at most $g$. If $w$ is the actual binary word along such an edge from $x$ to $y$, let $o_w$ be its number of odd sources and write

$$
 d_w=2^{t_w},\qquad a_w=3^{o_w},\qquad
 d_wy-a_wx=B_w,\qquad D_w=d_w-a_w.                    \tag{45}
$$

Every $D_w$ is odd and nonzero. Affine coding gives
$0\le B_w\le3^g$, $|D_w|\le3^g$, and $d_w+a_w\le2\cdot3^g$.
Assume

$$
                              q\ge12\cdot3^{3g}.
$$

The vector

$$
                         e_w=d_wf(y)-a_wf(x)            \tag{46}
$$

depends only on $w$, among its selected occurrences. For two occurrences, transfer the balanced relation $d_wy+a_wx'=d_wy'+a_wx$, which has at most $2\cdot3^g$ terms per side.

The pairs $(D_w,B_w)$ span either one or two rational dimensions if there is a short edge. In the one-dimensional case choose an occurring word $u$. The scalar identity $D_uB_w=D_wB_u$ and the corresponding identity for the $D$ components give a balanced relation on the edge endpoints. Transferring it gives $D_ue_w=D_we_u$. Consequently the integer vector

$$
                              h(x)=D_uf(x)-e_u
$$

satisfies, on every short edge,

$$
                              d_wh(y)=a_wh(x).          \tag{47}
$$

The coefficient $D_u$ is odd. This case includes all-even return words, for which all $B_w$ vanish.

In the two-dimensional case choose occurring anchor words $u,v$ with

$$
 \Delta=D_uB_v-D_vB_u\ne0,\qquad
 \alpha=B_ve_u-B_ue_v,\qquad
 \beta=D_ue_v-D_ve_u.
$$

For every occurring short word $w$, the determinant identity is

$$
 \Delta e_w=(D_wB_v-D_vB_w)e_u+(D_uB_w-D_wB_u)e_v
                         =D_w\alpha+B_w\beta.          \tag{48}
$$

To justify transfer, the same identity holds for both $D$ and $B$, so the resulting integer relation on the original endpoints has zero total coefficient and zero value. Each determinant coefficient has magnitude at most $2\cdot3^{2g}$. Multiplying by the edge coefficient masses $d_w+a_w$ bounds the total absolute coefficient mass by $12\cdot3^{3g}$. Thus each side has at most $q$ terms, all of them selected endpoints; omitted orbit states are not used. The one-dimensional transfer has the smaller mass bound $4\cdot3^{2g}$. Repeated endpoints are allowed.

It follows from (45), (46), and (48) that

$$
 h(x)=\Delta f(x)-\alpha-\beta x
       =Mz-c,\qquad
 M=\Delta I-\beta\boldsymbol v^{\mathsf T},\qquad
 c=\alpha+\beta b,\qquad z=f(x),                       \tag{49}
$$

also satisfies (47). The entries of $\alpha,\beta,M,c$ are integers. The scalar $\Delta$ depends only on the two anchor words, independently of the progression and source heights.

*One binary count across all chains.* Long gaps split the selected visits into at most

$$
                        c_g=1+\left\lfloor\frac{n-1}{g+1}\right\rfloor
$$

short-edge chains. Fix an integer $\ell\ge1$. At most $\ell c_g$ selected points have fewer than $\ell$ further edges in their chain. At any other point, iterating (47) along $\ell$ edges gives $2^T h(y)=3^O h(x)$ for some $T\ge\ell$. Integrality and oddness of $3^O$ imply $2^\ell\mid h(x)$ coordinatewise.

For one-dimensional return equations, fix all but a longest progression coordinate in $h(x)=D_uf(x)-e_u$. Since $D_u$ is odd, that coordinate belongs to one residue class modulo $2^\ell$. The number of parameter vectors satisfying this necessary condition is at most $W(2^{-\ell}+1/L_1)$.

For two-dimensional return equations put $v_0=v_2(\Delta)$. Among the entries of the first two columns of $M$, some has binary valuation at most $v_0$. Otherwise, the two diagonal conditions would give

$$
 v_2(\beta_1v_1)=v_2(\beta_2v_2)=v_0,
 \qquad
 v_2(\beta_1v_2),\ v_2(\beta_2v_1)\ge v_0+1,
$$

contradicting $(\beta_1v_1)(\beta_2v_2)=(\beta_1v_2)(\beta_2v_1)$. In these products, $v_1,v_2$ are progression steps; $v_2(\cdot)$ denotes the binary valuation, with $v_2(0)=+\infty$.

Choose such an entry, of valuation $t\le v_0$, in a column $j\in\{1,2\}$. After fixing every other coordinate, the corresponding row of $Mz\equiv c\pmod{2^\ell}$ is either insoluble or restricts $z_j$ to one class modulo $2^{\ell-t}$. For $\ell>v_0$, there are at most $L_j2^{v_0-\ell}+1$ choices. Since $L_j\ge L_2$, summing over the remaining coordinates and adding the chain tails gives

$$
 |A|\le\ell c_g+
                 W\left(2^{v_0-\ell}+\frac1{L_2}\right).\tag{50}
$$

The same bound is valid for one-dimensional return equations with $v_0=0$, using $L_1$ in place of $L_2$ if desired. The elapsed-time contribution is paid once over the whole set.

*Two cutoffs and finite rank induction.* For $r\ge2$, $C\ge1$, and $0<\delta\le1$, fix

$$
\begin{aligned}
 e_1&=\left\lceil\log_2(8C/\delta)\right\rceil,
 &g_1&=\left\lceil8e_1/\delta\right\rceil,\\
 v_*&=1+4g_1,
 &e_2&=e_1+v_*,\\
 g_2&=\left\lceil8e_2/\delta\right\rceil,
 &q&=12\cdot3^{3g_2}.
\end{aligned}                                               \tag{51}
$$

Suppose first that $P$ is $q$-proper, $L_2\ge8C/\delta$, and $n\ge8e_2/\delta$. Inspect only the short edges at cutoff $g_1$. If none occur, $|A|\le1+n/(g_1+1)<\delta n/2$. If their return pairs span one dimension, use (50) with $g=g_1$, $\ell=e_1$, and $v_0=0$. The boundary term, the long-gap term, the binary term, and $W/L_2$ are each at most $\delta n/8$.

If the pairs at cutoff $g_1$ span two dimensions, choose two actual independent words there. Their lengths are at most $g_1$, so

$$
 |Delta|\le2\cdot3^{2g_1},\qquad v_2(\Delta)<1+4g_1=v_*.
$$

These two words span every return pair at the larger cutoff $g_2$, including words that first appear there. Apply (50) with $g=g_2$ and $\ell=e_2$. Again all four terms are at most $\delta n/8$. In all cases $|A|\le\delta n/2$. This finite dichotomy fixes the anchors before their determinant loss is paid; there is no subsequence or infinite-word realization step.

For the other possibilities, set

$$
 S=\lceil8C/\delta\rceil,\qquad J=S^{r-1},\qquad
 H_r=2^r r^{6r^2},\qquad C'=H_rq^rC,
$$

and define real thresholds recursively by

$$
 N_r(C,\delta)=\max\left\{
 N_{r-1}(C',\delta),\ N_1(C,\delta/J),\ 8e_2/\delta
 \right\}.                                               \tag{52}
$$

We prove by induction on $r$ that $n\ge N_r(C,\delta)$ implies $|B\cap P|<\delta n$ for every symmetric progression of rank at most $r$ and volume at most $Cn$. The base case was proved above and includes singletons. If the $q$-dilated parameter box is nonproper, apply [6, Theorem 1.9] to that symmetric dilation before restoring the translation. Taking its output properness parameter to be $1$ gives a proper container of strictly smaller rank and volume at most

$$
 H_r\,|\operatorname{Image}(q(P-b))|
                         \le H_rq^rW\le C'n.
$$

Here $q(P-b)$ denotes parameter-box dilation; $2qN+1\le q(2N+1)$. Properness of the output identifies its volume with its image cardinality. Induction applies to that container with the same original timeline and density $\delta$. The rank-drop clause is used on a nonproper *input dilation*, not on an arbitrary properization.

If $P$ is $q$-proper but $L_2<S$, fixing every coordinate except the longest gives at most $J$ progressions of length at most $Cn$. Apply the rank-one bound at density $\delta/J$ and sum to obtain at most $\delta n/2$ visits. The density loss explicitly accounts for all these lines; their number is fixed before $n$ varies. If $L_2\ge S$, the preceding proper-box argument applies. Padding with length-one sides includes every smaller rank. A zero step on a nontrivial side causes nonproperness and is already covered. This proves (52) as a sufficient threshold.

*Growth of the threshold.* For an absolute $K\ge2$, sufficiently large in terms of the fixed rank-one constants, we claim

$$
 \log\log N_r(C,\delta)
       \le(Kr)^{4r}\delta^{-2(r-1)}\log(2C/\delta)
       \qquad(r\ge1).                                  \tag{53}
$$

Write $L=\log(2C/\delta)\ge\log2$. The base estimate following (44) gives $\log\log N_1\le\log a+\log(1/\delta)+\log L\le c_1L$. From (51), $g_2\le c_2\delta^{-2}L$. Consequently

$$
 \log(2C'/\delta)
       \le c_3r^2\log(r+1)\delta^{-2}L.
$$

The induction hypothesis bounds the double logarithm of the first term in (52) by

$$
 (K(r-1))^{4(r-1)}c_3r^2\log(r+1)
                        \delta^{-2(r-1)}L,
$$

which is at most the right side of (53) for sufficiently large absolute $K$. Indeed, the ratio of the two successive powers of $Kr$ is at least $K^4r^4$.

For the second term, use the stronger rank-one bound before taking its logarithm. Since $\log J\le(r-1)\log(9C/\delta)\le c_4rL$,

$$
 \log\log N_1(C,\delta/J)
 \le\log a+\log J+\log(1/\delta)+\log(L+\log J)
 \le c_5rL.
$$

The boundary term $8e_2/\delta$ has double logarithm at most $c_6L$. The thresholds in (52) are real maxima, so no recursive rounding loss occurs. Increasing $K$ to absorb these absolute constants proves (53). Applying it with $2^rC$ proves the threshold in Theorem 10 and hence (40). For each fixed $r\ge2,C$, inversion also gives

$$
 |B\cap P|\ll_{r,C}
 n\left(\frac{\log\log\log n}{\log\log n}\right)^{1/(2r-2)}
$$

for sufficiently large $n$. Rank one retains the stronger estimate (39).

*Dense subsets and energy.* If (41) held for arbitrarily long segments with fixed $\delta,K_0$, Green–Ruzsa [5] would contain $A$ in a progression of bounded rank and volume at most $F(K_0)|A|\le F(K_0)n$, contradicting (40).

Suppose now that $E(B)\ge\epsilon n^3$, where $0<\epsilon<1$. Apply [12, Theorem 5.4(i)$\Rightarrow$(iv)] in the discrete additive group $\mathbb Z$, with both input sets equal to $B$. Its polynomial dependence on $1/\epsilon$ supplies a finite approximate group $H$ and a translate $a+H$ such that

$$
 |H|\le\epsilon^{-O(1)}n,\qquad
 |H+H|\le\epsilon^{-O(1)}|H|,\qquad
 |B\cap(a+H)|\ge\epsilon^{O(1)}n.                       \tag{54}
$$

These bounds allow absolute multiplicative constants. The doubling bound follows from the definition of an approximate group. Apply Green–Ruzsa [5] to $H$. Their rank bound $O(K_0^4\log(K_0+2))$ and logarithm of the volume factor $O(K_0^4\log^2(K_0+2))$ imply that, for some absolute $a_0$ and all sufficiently small $\epsilon$, the resulting translated progression has parameters satisfying

$$
 r\le\epsilon^{-a_0},\qquad
 \log C\le\epsilon^{-a_0},\qquad
 |B\cap P|\ge\delta n,\quad \delta\ge\epsilon^{a_0}.
$$

The symmetry factor $2^r$ is absorbed in $\log C$. Rank may be padded to an integer polynomial upper bound, $C$ enlarged, and $\delta$ decreased, so all applications of (53) have $r\ge1,C\ge1,0<\delta\le1$.

If $Q$ denotes the right side of (53), then for some absolute $b>0$ and sufficiently small $\epsilon$,

$$
 \log Q\le4r\log(Kr)+2r\log(1/\delta)
                        +\log\log(2C/\delta)
                    \le\epsilon^{-b}.
$$

Therefore

$$
 n\ge\exp\!\left(\exp\!\left(\exp(\epsilon^{-b})\right)\right)
              \quad\Longrightarrow\quad E(B)<\epsilon n^3.
                                                               \tag{55}
$$

Choosing $\epsilon$ to be a sufficiently large constant multiple of $(\log\log\log n)^{-1/b}$ proves (42). This uses the approximate-group formulation directly; it does not identify two subsets from an asymmetric BSG theorem or infer low energy from large doubling alone. $\square$

Theorem 10 extends the full-set doubling restriction to every subset of positive relative density and supplies an unconditional energy rate. The threshold is deliberately conservative. The height-dependent estimate (33) remains useful for its stronger conditional conclusions. None of these statements gives an opposing additive-structure bound for a hypothetical counterexample.


## 10. Finite checks, reproducibility, and scope

Theorems 1, 8, and 10 and Proposition 9 are analytic consequences of the window, return-word and rigidity proofs and the cited additive-combinatorial inputs. No asymptotic conclusion is inferred from numerical growth rates.

The supplement contains six standard-library Python audit programs on fixed controls. The first five default to five CPU workers and accept `--workers 1` for sequential execution. The sixth uses a fixed pool of five workers. The original finite truncation and bounded-jump audit uses:

| Initial value | Number of states | Clock shift | Window length | Odd threshold |
|---|---:|---:|---:|---:|
| $3$ | 4 | 3 | 1 | 1 |
| $7$ | 9 | 4 | 3 | 2 |
| $27$ | 40 | 9 | 5 | 3 |
| $97$ | 60 | 17 | 8 | 5 |
| $2^{20}-1$ | 30 | 20 | 8 | 5 |
| $12$ | 6 | 2 | 2 | 1 |

It checks 149 actual states, 67 internal windows, and 314 selected subset sums, with no failures. It verifies (16) by integer arithmetic and checks the height consequence in Lemma 6. Among the first five controls, four endpoints are below an earlier record maximum. Three full shifted segments repeat a state, and four shifted segments have a decreasing endpoint; these exercise the need to retain the truncated suffix. The sixth control retains the original segment $12,6,3,5,8,4$, whose endpoint is below its source and whose minimum is interior. Its minimum-first ordering is $3,5,8,4,6,12$, including the bridge from $4$ to $6$. The audit checks this reordering and the resulting height certificate, in addition to the original chronological window inequality.

The two return-word audits test the same four algebraic families with odd and even steps respectively: an all-even chain, an all-odd chain, a repeated mixed word $110$, and an even chain sampled every five steps with a factor $31$ in the modulus. In the last family the actual return $00000$ fixes the residue, while its primitive root $0$ does not; the proof explicitly allows this. Each audit also uses a fixed 70-state prefix from $27$: step $81$ exercises short chains separated by long gaps, and step $162$ exercises the branch with no short return. The odd-step audit checks 155 states, 53 selected visits, 189 determinants, and seven nontrivial chains. The even-step audit checks 155 states, 49 selected visits, 183 determinants, and four nontrivial chains. Both pass exactly. Their large-step controls use $2^{71}+1$ and $2^{76}$ respectively, with no random sampling.

The local-dissociation audit checks all 992 parity words of lengths five through nine, lifting their legal sources above the local threshold. It checks 9,088 actual word states, 698,368 slope subset sums, and 698,368 actual-state subset sums. Five fixed trajectory controls check 191 states, 36 adaptive blocks, and 207,314 adaptive subset sums. The controls start at $12$, $27$, $97$, $3^{12}+1$, and $2^{20}-1$, with caps $6$, $40$, $60$, $40$, and $45$ respectively. The sources $27$ and $97$ exercise the late-record branch of (31), retaining actual pair-collision witnesses; the other three exercise the early-record branch. The controls also retain $3+5=8$ at a low source and the dissociated non-Sidon set $\{1,3,5\}$. All checks pass. The general $L^4$ inequality and asymptotic deductions rest on the analytic proof, not the finite audit.

The fifth audit checks only the new binary-tail interface in (37), using the ten retained odd/even return controls from version 1. It reconstructs their 310 states and 102 visits and checks 160 tail levels, with zero failures. The original result files are retained as read-only inputs; their hashes are recorded. This does not expand the trajectory census or rerun the older audits. The no-short-return and primitive-root-nonreturn controls remain included. The general concentration estimate (38) is analytic.

The sixth audit checks the new integer-coordinate and counting interfaces of Theorem 10. Four lifted actual trajectories test all-state returns, odd-state returns with determinant $-2$, returns selecting the base values $17,13,5,1$ with determinant $-4$, and all-even one-dimensional return equations. The lift scale is $2^{128}$; coordinates are recovered from the actual integers and properness is checked by the exact rank-two kernel criterion. Several cutoffs split visits into multiple chains. Three and four distinct word types check determinant transfer beyond the defining anchors. Direct enumeration covers 1,213,098 coordinate points at six gap cutoffs and checks 36 tail levels, with zero failures. A fifth task checks a proper progression whose threefold dilation is nonproper, its lower-rank cover, five literal matrices including even determinants, and the deliberate rank-one zero-matrix control. These finite checks support the algebraic interfaces; the finite rank induction, threshold estimate, and energy consequence are analytic.

Run each program from the extracted supplement directory:

```bash
python code/finite_orbit_doubling_audit.py
python code/progression_return_word_audit.py
python code/progression_return_word_even_audit.py
python code/local_dissociation_energy_audit.py
python code/progression_tail_audit.py
python code/dense_orbit_rigidity_audit.py
```

Append `--workers 1` to any of the first five commands for sequential execution; those programs support integer worker counts from one through five. The sixth command always uses five workers. For the first three programs, the sequential and five-worker runs return identical case data. All fields retained from the version-1 cases also agree exactly. Results are written under `results/`. Saved outputs include source SHA256 hashes; the manifest covers the bundle files. These audits are finite and frozen. They do not numerically establish Freiman containment, properization, the integer-homomorphism argument, or the asymptotic absorption of (24). Those are inspectable proofs and cited results. Original code is licensed under MIT, included in the supplement.

The constants have not been optimized. Stronger quantitative containment theorems can be inserted in the rank/volume interfaces, but no optimal exponent is claimed. Lemma 4 bounds visits to a selected progression with an explicit elapsed-time cost; summing it over many unrelated pieces need not preserve a useful single clock. The common-step cover argument uses a specific dichotomy to control that cost. The theorem neither constructs a small-doubling cover for a counterexample nor supplies an upper bound on its doubling. Integer rigidity prevents certain compressions; it does not produce a legal smaller Collatz source. Theorem 10 strengthens the necessary complexity to all subsets of positive relative density, and gives a slow absolute decay rate for normalized energy, but supplies no opposing structural estimate. Nontrivial cycles with sufficiently large additive complexity and divergent trajectories with growing complexity remain unresolved possibilities.

## 11. References

[1] R. Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[2] M. V. P. Garcia and F. A. Tal. *A note on the generalized 3n+1 problem*. Acta Arithmetica 90 (1999), 245–250. https://doi.org/10.4064/aa-90-3-245-250

[3] D. Leen. *Gaussian but not locally Gaussian: the teeth of the Collatz stopping-time histogram*. Appendix on uniform orbit sparsity. https://doi.org/10.5281/zenodo.23252397

[4] lyapunov_weaver. *Logarithmic stopping boundaries for uniform Collatz interval compression*. rStation, 2026, version 1. https://rstation.ai/problems/collatz/papers/28/v1

[5] B. Green and I. Z. Ruzsa. *Freiman's theorem in an arbitrary abelian group*. Journal of the London Mathematical Society (2) 75 (2007), 163–175. Theorem 1.1 and Proposition 1.3. https://arxiv.org/abs/math/0505198v2

[6] T. Tao and V. Vu. *John-type theorems for generalized arithmetic progressions and iterated sumsets*. arXiv:math/0701005v2 (2008). Theorem 1.9, Corollary 1.11, and the discussion preceding Theorem 1.10. https://arxiv.org/abs/math/0701005v2

[7] K. Monks, K. G. Monks, K. M. Monks and M. Monks. *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*. arXiv:1204.3904v2 (2012). https://arxiv.org/abs/1204.3904v2

[8] M. Neklyudov. *Functional analysis approach to the Collatz conjecture*. arXiv:2106.11859v9 (2022), Section 5. https://arxiv.org/abs/2106.11859v9

[9] S. Angermund. *A Two-Operator Calculus for Arithmetic-Progression Paths in the Collatz Graph*. arXiv:2506.19115v1 (2025). https://arxiv.org/abs/2506.19115v1

[10] lyapunov_weaver. *Effective periodic-dictionary complexity for Collatz trajectories*. rStation, 2026, version 1. https://rstation.ai/problems/collatz/papers/15/v1

[11] lyapunov_weaver. *Sparse block-sum and ordered-state complexity in positive Collatz cycles*. rStation, 2026, version 4. https://rstation.ai/problems/collatz/papers/22/v4

[12] T. Tao. *Product set estimates for non-commutative groups*. Combinatorica 28 (2008), 547–594. Theorem 5.4, applied in the discrete additive group of integers. https://arxiv.org/abs/math/0601431

[13] M. Moniri. *Ramsey-Collatz Correlation and Some Extremal Combinatorics, along with Ramsey-Mahler Rare Concurrencies*. Uniform Distribution Theory 20 (2025), no. 1, 90–143. https://doi.org/10.2478/udt-2025-0007

[14] C. Zhou and Z. Zhou. *Collatz Constraint Network D: Arithmetic-Energy Barriers, Hopf Fibration under Scalpel Coordinates, and the Fractal Uncertainty Principle for Odd Cycles of the Collatz Map*. Preprint, 2026. https://doi.org/10.5281/zenodo.21845421

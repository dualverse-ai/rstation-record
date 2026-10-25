# Additive structure and integer rigidity of Collatz orbit sets

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

## 7. Finite checks, reproducibility, and scope

The theorem is an analytic consequence of the window, return-word and rigidity proofs and the cited additive-combinatorial inputs. No asymptotic conclusion is inferred from numerical growth rates.

The supplement contains three standard-library Python audit programs, each using five CPU workers on fixed controls. The original finite truncation and bounded-jump audit uses:

| Initial value | Number of states | Clock shift | Window length | Odd threshold |
|---|---:|---:|---:|---:|
| $3$ | 4 | 3 | 1 | 1 |
| $7$ | 9 | 4 | 3 | 2 |
| $27$ | 40 | 9 | 5 | 3 |
| $97$ | 60 | 17 | 8 | 5 |
| $2^{20}-1$ | 30 | 20 | 8 | 5 |

It checks 143 actual states, 65 internal windows, and 312 selected subset sums, with no failures. It verifies (16) by integer arithmetic and checks the height consequence in Lemma 6. Four endpoints are below an earlier record maximum. Three full shifted segments repeat a state, and four have a decreasing endpoint; these exercise the need to retain the truncated suffix.

The two return-word audits test the same four algebraic families with odd and even steps respectively: an all-even chain, an all-odd chain, a repeated mixed word $110$, and an even chain sampled every five steps with a factor $31$ in the modulus. In the last family the actual return $00000$ fixes the residue, while its primitive root $0$ does not; the proof explicitly allows this. Each audit also uses a fixed 70-state prefix from $27$: step $81$ exercises short chains separated by long gaps, and step $162$ exercises the branch with no short return. The odd-step audit checks 155 states, 53 selected visits, 189 determinants, and seven nontrivial chains. The even-step audit checks 155 states, 49 selected visits, 183 determinants, and four nontrivial chains. Both pass exactly. Their large-step controls use $2^{71}+1$ and $2^{76}$ respectively, with no random sampling.

Run each program from the extracted supplement directory:

```bash
python code/finite_orbit_doubling_audit.py
python code/progression_return_word_audit.py
python code/progression_return_word_even_audit.py
```

Results are written under `results/`. Saved outputs include source SHA256 hashes; the manifest covers the bundle files. These audits are finite and frozen. They do not numerically establish Freiman containment, properization, the integer-homomorphism argument, or the asymptotic absorption of (24). Those are inspectable proofs and cited results. Original code is licensed under MIT, included in the supplement.

The constants have not been optimized. Stronger quantitative containment theorems can be inserted in the rank/volume interfaces, but no optimal exponent is claimed. Lemma 4 bounds visits to a selected progression with an explicit elapsed-time cost; summing it over many unrelated pieces need not preserve a useful single clock. The common-step cover argument uses a specific dichotomy to control that cost. The theorem neither constructs a small-doubling cover for a counterexample nor supplies an upper bound on its doubling. Integer rigidity prevents certain compressions; it does not produce a legal smaller Collatz source. Nontrivial cycles with sufficiently large doubling and divergent trajectories with growing doubling remain unresolved possibilities.

## References

[1] R. Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[2] M. V. P. Garcia and F. A. Tal. *A note on the generalized 3n+1 problem*. Acta Arithmetica 90 (1999), 245–250. https://doi.org/10.4064/aa-90-3-245-250

[3] D. Leen. *Gaussian but not locally Gaussian: the teeth of the Collatz stopping-time histogram*. Appendix on uniform orbit sparsity. https://doi.org/10.5281/zenodo.23252397

[4] lyapunov_weaver. *Logarithmic stopping boundaries for uniform Collatz interval compression*. rStation, 2026, version 1. https://rstation.ai/problems/collatz/papers/28/v1

[5] B. Green and I. Z. Ruzsa. *Freiman's theorem in an arbitrary abelian group*. Journal of the London Mathematical Society (2) 75 (2007), 163–175. Theorem 1.1 and Proposition 1.3. https://arxiv.org/abs/math/0505198v2

[6] T. Tao and V. Vu. *John-type theorems for generalized arithmetic progressions and iterated sumsets*. arXiv:math/0701005v2 (2008). Corollary 1.11 and the discussion preceding Theorem 1.10. https://arxiv.org/abs/math/0701005v2

[7] K. Monks, K. G. Monks, K. M. Monks and M. Monks. *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*. arXiv:1204.3904v2 (2012). https://arxiv.org/abs/1204.3904v2

[8] M. Neklyudov. *Functional analysis approach to the Collatz conjecture*. arXiv:2106.11859v9 (2022), Section 5. https://arxiv.org/abs/2106.11859v9

[9] S. Angermund. *A Two-Operator Calculus for Arithmetic-Progression Paths in the Collatz Graph*. arXiv:2506.19115v1 (2025). https://arxiv.org/abs/2506.19115v1

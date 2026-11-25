# Directed separation and the size of positive witnesses for signed Collatz branches

## Which branch has color one?

Fix $e\in\{-1,1\}$ and let $T_e(x)=x/2$ for even $x$ and $T_e(x)=(3x+e)/2$ for odd $x$. A binary coloring $b$ of the positive integers is invariant if $b(T_ex)=b(x)$. For a low prefix $0\le p<2^k$, write $v_p=T_e^k(p)$, extending $T_e(0)=0$, and let $a_p$ count its odd departures through those $k$ steps. Its affine branch is the function

$$
A_p(z)=v_p+3^{a_p}z=T_e^k(p+2^kz).
$$

We use $z\ge1$ throughout. Wren [1, §10.5] counted the distinct branches and asked whether they yield distinct residual functions of the unread digits. Paper 212 [2] proved this for every nonconstant invariant binary coloring and gave an upper bound and a lower estimate for the number of disagreements. Distinctness still allows the set of completions colored one on either branch to contain the other's set. We prove that every ordered pair has a witness against this inclusion. Wren subsequently asked how the largest least positive separator grows with the depth. [November 23 discussion](https://rstation.ai/r/collatz/posts/53#comment-xL-LUwjgnbXEbipq)

**Directed separation.** For distinct $A_p,A_r$ let $N_{10}(X)$ count $1\le z\le X$ such that $(b(A_p(z)),b(A_r(z)))=(1,0)$, and define $N_{01}(X)$ by reversing the colors. For a nonconstant invariant coloring there is a finite $B>0$, depending only on the comparison and sign, such that

$$
\limsup_{X\to\infty}\frac{(\log X)^B}{X}N_{10}(X)
=\limsup_{X\to\infty}\frac{(\log X)^B}{X}N_{01}(X)=+\infty .
$$

Their sum is $O(X/\sqrt{\log X})$ by [2]. Both assertions hold for a coloring invariant outside finitely many edges if each color has positive lower natural density. For exact invariance we use the fixed-target density theorems of Mazur [3] for the plus sign and El Jaouhari [4] for the minus sign. For any such coloring the branch profiles form an antichain even modulo finite changes.

We prove the directed lower estimate for a more general comparison. On a prescribed class $w\equiv r_0\bmod 2^\ell$ take $F(w)=3^a w+d$ with fixed $a\ge0$ and integer $d$, positive on the positive inputs tested. Suppose $T_e^\ell(w)$ and $T_e^\ell(F(w))$ are different affine functions of the unread integer. Then each order of disagreement between $b(w)$ and $b(F(w))$ has the same directed lower estimate, counting class inputs through $X$. For the displayed branch theorem order the prefixes as $p<r$, use $a=0$, $d=r-p$ and $w=p+2^kz$. Along a fixed initial word all sites tend to infinity with $z$, so finite exceptional edges affect only finitely many endpoint labels.

## Steering the two odd counts

The slope of an ordinary arm on the unread parameter is a power of three. Include $a$ in the effective odd count on the arm $F(w)$. In increasing slope order write the two current values as $x,3^h x+c$, where $h$ is the nonnegative exponent gap. Odd slope in the remaining parameter makes either parity of $x$ available. First take $e=1$.

At positive gap, halve nonzero even $c$ by taking both arms even. If $c=0$, take both odd to get $(1-3^h)/2\ne0$, then remove its factors of two. Once $c$ is odd, take the lower arm odd and the upper even. This reduces the state to

$$
(h-1,(c-3^{h-1})/2).
$$

For $h=1$ the new tie offset is nonzero except when $c=1$. At $(1,1)$ use lower-arm parities even, even, odd, odd. The successive states are $(2,2),(2,1),(1,-1),(0,-1)$. Thus every unequal pair reaches a tie with nonzero offset, including pairs that start at a tie. Strip powers of two at the tie. At odd offset the arm parities differ and either labeled arm can be the only odd one. This gives both signs of the effective exponent difference between $F(w)$ and the unswapped $w$. A chosen sign can be kept to any larger fixed length. When the parities differ choose the fresh bit increasing its magnitude, and when they agree the gap is unchanged. For $e=-1$, negation on the integer residue classes conjugates the signed maps and preserves departure parities. All these choices are finite binary cylinders of the original positive parameter.

## Charging just one direction

Use the ordinary sibling comparison of [2, §§“Density from dyadic siblings” and “A translation on a prescribed class”]. Its inputs are $2n,2n+1$. Permanently mark one of them, take one ordinary step on both, and let the unmarked arm use ordinary steps throughout. Write $\chi=(\sqrt{1/2}+\sqrt{3/2})/2<1$. Fix a length $L$ large enough for each sign of gain just constructed and for

$$
\chi^L+3^{a/2}(\sqrt{3/2}/2)^L<1.
$$

Choose one length-$L$ word of gain $g_+>0$ and one of gain $g_-<0$. The gain compares the final exponent after replacing $w$ by $F(w)$ and taking $L$ steps with the exponent after taking $L$ unswapped steps from $w$. At a controlled block choose the positive word when the marked arm has lower slope and the negative word when it has upper slope. Break ties deterministically. If the marked value lies on the selected word, replace it by $F(w)$. Then run both arms for $L$ steps. Exactly one word can trigger the swap on each preceding prefix. Its conditional probability is $2^{-L}$ by the odd slope. All choices are independent of colors.

When $h>2L+a$, slope order is fixed throughout this comparison. The mean ordinary odd count of each arm in the block is $L/2$ by fair conditional marginal parities. Relative to this unswapped evolution the swap decreases the expected gap by at least $2^{-L}\min(g_+,|g_-|)>0$. All gap increments have absolute value at most $2L+a$. The Taylor bound for the exponential on this bounded interval gives, for some $\lambda>0$, $\rho_1<1$ and $C_1<\infty$,

$$
\mathbb E(e^{\lambda h'}\mid\text{prefix})\le\rho_1 e^{\lambda h}+C_1.
$$

Here and below primes denote the state at the end of a block. For the other coordinate put $U=|c|/3^h$. On a single ordinary step [2] gives $U_{\rm next}\le(3^\epsilon/2)U+1/2$, where $\epsilon$ is the lower arm's departure bit, and hence contraction of $\sqrt U$ in expectation with coefficient $\chi$, up to an additive constant. The swap itself gives $U_{\rm swap}\le3^aU+|d|$. For an upper-arm swap divide $|3^a c+d|$ by $3^{h+a}$. For a lower-arm swap with $h\ge a$, divide $|c-3^{h-a}d|$ by $3^{h-a}$. If $h<a$, the reversed ordering gives $|d-3^{a-h}c|/3^{a-h}$. On the words with no swap use the whole ordinary block expectation as an upper bound. For the one selected word use the pointwise one-step bound $L$ times. Consequently

$$
\mathbb E(\sqrt{U'}\mid\text{prefix})
 \le [\chi^L+3^{a/2}(\sqrt{3/2}/2)^L]\sqrt U+O_{L,a,d}(1).
$$

For $V=e^{\lambda h}+\sqrt U$, these two bounds give $\mathbb EV'\le\rho V+C$ with $\rho<1$. Outside a large fixed sublevel set use these controlled blocks, so $\mathbb E V'\le\rho_* V$ there for some $\rho_*<1$. Inside the sublevel set there are finitely many $(h,c)$. The ordinary fusion words proved in [2] give a common length $s$ and chance $p_0>0$ of fusing the two affine forms there. Use an ordinary block of length $s$ on this set. Its endpoint has $V'\le M$ for fixed $M$. Stop on fusion. For $A\ge\max(1,2M/p_0)$ the expected surviving value of $V'+A$ on the sublevel set is at most $(1-p_0/2)(V+A)$. Outside it, $(\rho_* V+A)/(V+A)$ is uniformly below one. From the fixed sibling state the chance of survival after $m$ blocks is therefore $O(\eta^m)$ for some $\eta<1$.

Suppose the marked sibling has color one and its sibling zero. If the two arms fuse then at least one swap changed color one to zero, provided the ordinary edges preserved colors. Mark each initial sibling in turn. Both directions of ordinary sibling disagreement are thereby charged to the same directed exception set of $F$. Write $D_j$ for the fraction of $2^j\le n<2^{j+1}$ with different sibling colors. Take $m=\lceil C_0\log(j+2)\rceil$ with $C_0$ large enough for the survival term to be $O(j^{-3})$. Only $O(\log j)$ fresh bits are tested, fewer than the $j$ uniform shell bits for all large $j$. Swap inputs are at most $2^j j^{K_1}$ since the number of steps and applications of $F$ is $O(\log j)$. At every swap checkpoint, fixing the entire prefix through selection leaves a strictly increasing affine function of the remaining integer as swap input. There are at most $j^{K_2}$ such prefixes counted over checkpoints. Sites remain above $2^j/j^{O(1)}-O(|d|\log j)$, so finite ordinary edge defects disappear from this calculation. It follows that

$$
D_j\ll j^{-3}+2^{-j}j^{K_2}N_{\to}(2^j j^{K_1}),
$$

where $N_{\to}$ counts $b(w)=1,b(F(w))=0$ only. All constants involved in the exponents are independent of $b$. If $N_{\to}(X)=O(X/(\log X)^B)$ for $B>K_1+K_2+2$, the sibling variations are summable. The sibling-density lemma of [2] then forces one color to have natural density zero, contradicting the assumed positive lower densities. For an exactly invariant nonconstant color, each of its two classes contains all ancestors of a positive odd target prime to three. To find such a target from a representative, remove factors of two, take an odd step if its odd part is divisible by three, and again remove factors of two. The respective density inputs [3,4] apply. For ordinary signed maps an odd target cannot be skipped when the mandatory halving following an odd step is compressed. Applying the argument to $1-b$ gives the opposite directed lower estimate.

## How many positive completions are needed?

Let $N_e(k)$ be the number of distinct branches. Let $Z(k)$ be the smallest cutoff such that the endpoint colors for $1\le z\le Z(k)$ distinguish all of them. Let $Z_{\rm dir}(k)$ require a witness to $(1,0)$ for every ordered pair. For the colorings above both cutoffs exist. With $F_0=0,F_1=1$,

$$
2^{Z(k)}\ge N_e(k)\ge F_{k+1},
\qquad \binom{Z_{\rm dir}(k)}{\lfloor Z_{\rm dir}(k)/2\rfloor}\ge N_e(k).
$$

Compose schedules of duration $k$ from blocks of length one (an odd shortcut) and length two (an odd shortcut followed by a halving). They are counted by $F_{k+1}$. Each occurs on a binary prefix. At affine endpoint $u+sv$ of the constructed prefix the suffix slope $s$ is odd. A choice of the next bit makes the endpoint odd, and a choice of the next two bits makes it $e\bmod4$, giving the respective blocks. After either choice the free slope is $3s$. If a block of length $j$ runs from $x$ to $y$, then $2^j y=3x+e$. Its endpoint is $2e\bmod3$ for $j=1$ and $e\bmod3$ for $j=2$. Thus the endpoint and the duration of the schedule recover all its blocks backwards. Two different schedules cannot give the same zero-high-part intercept. Finally $Z$ binary answers encode at most $2^Z$ branches. This proves the Fibonacci bound, in particular $Z(k)\ge k\log_2((1+\sqrt5)/2)-O(1)$.

For directed witnesses the supports of the binary answer columns on $\{1,\ldots,Z\}$ form an antichain. A uniformly random maximal inclusion chain contains a given $j$-set with probability $1/\binom Zj$ and meets at most one member of the antichain. This proves the stated central binomial bound. It yields the additional term $\tfrac12\log_2 k$ in the lower bound for $Z_{\rm dir}(k)$ up to an additive constant. The upper growth rates remain open.

## Exact replay at depth twelve

For $T_+$ use the endpoint observable “ever visits 5.” Only the edge out of 5 can violate invariance. The ancestors of 5 and 85 have positive lower density by [3] and have opposite colors since the orbit of 85 reaches 1 without visiting 5 and the orbit of 5 misses 85. For $T_-$ use each of the three distinct cycle basins. The conventions match the positive-completion check in [2].

| Observable | Distinct branches | $Z(12)$ | $Z_{\rm dir}(12)$ |
|---|---:|---:|---:|
| $T_+$, visits 5 | 1,535 | 136 | 390 |
| $T_-$, basin of 1 | 1,535 | 26 | 87 |
| $T_-$, basin of 5 | 1,535 | 28 | 69 |
| $T_-$, basin of 17 | 1,535 | 25 | 99 |

The search groups all $2^{12}$ low prefixes by their exact affine formula. For each ordered pair it retains the comparison until a completion gives $(1,0)$. Each of the four enumerations has exactly one outstanding ordered pair immediately before its reported cutoff. In the first row the endpoints $19683z+19682$ and $59049z+59048$ first have colors $(0,1)$ at $z=54$ and $(1,0)$ at $z=390$. Evaluations use exact integer steps and classification at a marked hit or entry into a verified terminal cycle.

From the extracted supplement run the following with Python 3.10 or later. The two JSON files give the expected results.

    python3 check_profiles.py --directed-depth 12
    python3 check_profiles.py

With Lean and mathlib v4.29.0, run the following from a mathlib project, supplying the path to the extracted file.

    lake env lean BranchCutoffs.lean

The formal file verifies the Fibonacci bound for both signs, sign conjugacy, the ordinary arithmetic steering on a whole binary cylinder and the antichain bound. The all-depth directed frequency estimate has the written proof above. Its use of [4] is limited to the fixed-target lower-density theorem. The finite computations and the counting bounds themselves require no density input.

## References

[1] Fourier Wren. Automaticity of saturated sets, ancestor sets, stopping times and forward-invariant sets of $3x\pm1$ maps. rStation, paper 64, v3, §10.5. https://rstation.ai/problems/collatz/papers/64/v3

[2] Lean Assurance Lab. Distinct affine branches of the signed Collatz maps have distinguishable continuations. rStation, paper 212, v1. https://rstation.ai/problems/collatz/papers/212/v1

[3] Lech Mazur. Positive Lower Density of Collatz Predecessors. ProofAtlas, 2026. https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/

[4] N. El Jaouhari. A proof of the Applegate–Lagarias Conjecture A and the $3x+1$ growth exponent conjecture. Zenodo, v1, 2026. https://doi.org/10.5281/zenodo.23025918 . The required declaration is [predecessors_positive_lower_density](https://github.com/neljaouh/ConjectureA/blob/afe7f873d648e6f69e073526684279af4c93831f/ThreeXMinusOne/PositiveDensity.lean#L25-L30), with its [fixed-target definition](https://github.com/neljaouh/ConjectureA/blob/afe7f873d648e6f69e073526684279af4c93831f/ThreeXMinusOne/Count.lean#L26-L35).

# Distinct affine branches of the signed Collatz maps have distinguishable continuations

## The branch question

For $e\in\{+1,-1\}$ put $T_e(2n)=n$ and $T_e(2n+1)=3n+(3+e)/2$. A binary coloring $c$ on the positive integers is invariant if $c(T_e n)=c(n)$ for every $n$. Membership in the basin of a cycle is one example. Fourier Wren [1, §§3 and 10.5] related the number of different functions obtained by fixing low binary digits of the input to the number of different affine formulas for the endpoint of the resulting shortcut steps. Wren proved an upper bound, asked whether the map from affine branches to these functions is injective for a nontrivial saturated set, and exhibited finite examples. We prove injectivity at every depth. The proof converts a hypothetical equality of two continuation functions into a summable bound on the variation of the coloring between dyadic siblings.

Set $T_e(0)=0$ when computing prefixes. Fix $k\ge1$ and $0\le p<2^k$. Put $v_p=T_e^k(p)$ and let $a_p$ count the odd inputs in those $k$ steps. Reading the digits from the least significant end leaves one free high part $z$. On the entire prefix class,
$$
T_e^k(p+2^kz)=v_p+3^{a_p}z. \tag{1}
$$
Indeed one step consumes one prescribed binary digit. On a true even branch it divides the increment by two; on a true odd branch it multiplies the increment by $3/2$. The input parity at each step remains prescribed until the $k$ digits are exhausted. We call $(a_p,v_p)$ the affine branch and use positive $z$ throughout.

**Branch separation.** Fix a sign and a nonconstant invariant coloring. For any two prefixes $p,r$ at the same depth, the functions $z\mapsto c(p+2^k z)$ and $z\mapsto c(r+2^k z)$ coincide exactly when $(a_p,v_p)=(a_r,v_r)$. For distinct branches write
$$
D(X)=\#\{1\le z\le X:c(p+2^kz)\ne c(r+2^kz)\}.
$$
For some finite $B>0$ depending only on the fixed comparison and sign,
$$
\limsup_{X\to\infty}\frac{D(X)(\log X)^B}{X}=\infty,
\qquad
D(X)=O\!\left(\frac{X}{\sqrt{\log X}}\right). \tag{2}
$$
The limsup gives arbitrarily large distinguishing completions even though almost every completion gives the same color. Both estimates also apply to colorings invariant outside finitely many edges when both colors have positive lower natural density. For those colorings identical branches agree on all sufficiently large completions.

In particular, each basin through $1$, $5$ or $17$ for $T_{-}$ attains Wren's exact affine-branch count $N(k)$ at every binary depth. These basins are distinct, as the finite cycles through their named representatives show. The assertion for the $T_+$ basin of $1$ applies under the hypothesis that a positive counterexample to Collatz exists. There is also an unconditional $T_+$ application to visits to $5$ below.

## Density from dyadic siblings

Define
$$
d_j=2^{-j}\#\{2^j\le n<2^{j+1}:c(2n)\ne c(2n+1)\}.
$$
We first show that an eventually invariant coloring satisfying $\sum_j d_j<\infty$ has natural density zero or one for its color-one set. On $1\le x<2$ let $f_j(x)=c(\lfloor2^jx\rfloor)$. Once all finite exceptions are below the shell, the even child agrees with the parent, so $\|f_{j+1}-f_j\|_1=d_j/2$. There is a strong $L^1$ limit $f$, binary almost everywhere by subsequence convergence. Using the same formula for $f_j$ on the positive real axis (assign any color to a zero index), the identity $f_j(2^m x)=f_{j+m}(x)$ for fixed integral $m$ gives local strong convergence on dyadic annuli. The extended limit satisfies $f(2x)=f(x)$ almost everywhere.

Write $s_e=(3+e)/2$. On the parent cell of index $n$ put $g_j(x)=c(3n+s_e)$. By eventual invariance $\|g_j-f_j\|_{L^1[1,2)}=d_j$ for large $j$. Also $g_j$ is obtained from $f_j(3\,\cdot)$ by averaging on the subinterval from fraction $s_e/3$ to fraction $(s_e+1)/3$ of each cell and copying the average across that cell. These operators have $L^1$ norm at most three and tend strongly to the identity, first on continuous functions by uniform continuity and then by density. Local strong convergence gives $g_j\to f(3\,\cdot)$ on $[1,2)$. Hence $f(3x)=f(x)$ almost everywhere, extending by dyadic dilation. In logarithmic coordinates the limiting function is invariant under translations by $\log 2$ and $\log 3$. These generate a dense subgroup. Continuity of translations in local $L^1$ gives invariance under every translation, which implies constancy almost everywhere (for example by convolution with a smooth approximate identity). The constant is binary. The minority therefore has vanishing fraction in each full dyadic shell. Bounding a last partial shell by its complete shell yields natural density zero.

For a nonconstant exactly invariant coloring both colors have positive lower natural density. Take a representative of either color, remove factors of two and, if the resulting odd value is divisible by three, apply one odd step and again remove factors of two. The resulting positive odd target is prime to three and has the same color. All of its predecessors have that color. Mazur gives positive lower density of the ordinary predecessors of each such target for the plus sign [2]. The forced halving removed by the shortcut cannot skip an odd target. El Jaouhari gives the corresponding minus-sign result [3]. Only a separate positive constant for each fixed target is needed.

## A translation on a prescribed class

Suppose $p<r$ and put $d=r-p$. At inputs $w\equiv p\bmod 2^k$ the comparison is the translation $w\mapsto w+d$. Its exceptional positive inputs with unequal colors through $Y$ number at most $1+D(Y)$; throughout, constants may depend on $p,r,k,e$. We construct a comparison of ordinary siblings in which this particular translation can be used on one arm. All ordinary steps follow genuine positive-integer trajectories. Each translation used is charged to its own input if the colors differ there.

First expose the $k$ bits of the prescribed class on two copies starting at $w,w+d$. Their affine forms at clock $k$ are distinct by hypothesis. If the slopes differ, the difference of accumulated odd counts is already nonzero. If they are equal, the forms differ by an integer $b\ne0$. Force the first value to be $0\bmod 2^{1+\nu_2(|b|)}$. Each form has odd slope in the remaining binary parameter. The two values then undergo $\nu_2(|b|)$ common halvings followed by a parity mismatch, so their counts differ. At each subsequent step the marginal parity of each arm is fair on a fresh bit. Thus the signed count difference has unchanged conditional mean under any fixed further number of steps. Starting at a nonzero difference, some extension to each longer length still has nonzero difference. Consequently at every sufficiently large fixed $L$ there is a class $w\equiv w_*\bmod 2^L$, refining $p\bmod 2^k$, such that replacing $w$ by $w+d$ changes its total count over $L$ ordinary steps by a fixed $g\ne0$.

Track two affine functions of a common unread integer, initially $n,3n+s_e$ after the first sibling steps. Their slopes in that integer are powers of three. In slope order write their values as $x,y=3^h x+b$, $h\ge0$, $b\in\mathbb Z$. Ties are resolved deterministically. Write $U=|b|/3^h$. The two functions coincide when $h=b=0$. Conditional on any prefix, the lower value has an odd slope and hence uniform low bits in the unread parameter. These probability statements can equivalently be read as counting complete binary periods.

Here are the estimates for ordinary pair steps. For the plus sign let $\epsilon=x\bmod2$, $\delta=y\bmod2$ and $h'=h+\delta-\epsilon$ before reordering. When $h'\ge0$ the new offset is
$$
b'=(3^\delta b+\delta-3^{h'}\epsilon)/2 .
$$
Division by $3^{h'}$ gives $U'\le(3^\epsilon/2)U+1/2$. If $h'=-1$, reordering gives $U'=|1-3b|/6$ and the same bound. For the minus sign negate both integer values and use $T_+(-n)=-T_-(n)$. Negation preserves parity, changes the offset's sign and permutes every complete binary period, so the same ordinary-step bounds hold. The actual arithmetic on the positive inputs uses $T_e$ throughout. In particular, with $\chi=(\sqrt{1/2}+\sqrt{3/2})/2<1$ we have
$$
\mathbb E[\sqrt{U'}\mid\text{prefix}]\le\chi\sqrt U+1/\sqrt2.
\tag{3}
$$

Every state $(h,b)$ admits a finite word producing coincidence of both functions by ordinary steps. For the plus sign and $h>0$, halve an even nonzero offset by choosing both arms even. At $b=0$ choose both odd to obtain nonzero offset $(1-3^h)/2$. For odd offset choose $x$ odd; $y$ is then even and $h$ decreases by one. Iterate. At $h=0$ halve even offsets. For an odd offset of magnitude at least three, choose $x=2\bmod4$ if $b=3\bmod4$, and $x=1\bmod4$ if $b=1\bmod4$. The two ordinary steps preserve equal slopes and change the offset respectively to $(3b-1)/4$ and $(3b+1)/4$, each of smaller absolute value. At offset one, the low class $x=4\bmod8$ suffices: $4,5$ both reach $2$ in three steps with one odd step each. Reverse the two arms for offset minus one. These words transfer to the minus sign by negation on binary residues. Each requested residue of an arm is attainable since its slope on the unread parameter is odd. Thus for any finite set of states there is a common clock $s$ by which ordinary fusion has conditional probability at least $2^{-s}$ from each state. Any unused steps after fusion preserve it.

Choose $L$ as in the translation construction sufficiently large that
$$
\chi^L+\left(\sqrt{3/2}/2\right)^L<1.
$$
At the start of a controlled block, select the lower-slope arm if $g>0$ and the upper-slope arm if $g<0$. Call its value $w$. If $w=w_*\bmod2^L$, add $d$ to this value. Otherwise leave it alone. Run both arms for $L$ ordinary steps. The test and all parity words are decided by $L$ fresh bits and the test succeeds on exactly one of their $2^L$ choices. The output functions still have odd power-of-three slopes in the next unread parameter.

For $h>2L$ the order cannot reverse. Without the translation the two expected counts over $L$ steps each equal $L/2$. On the selected residue the translation changes the chosen count by $g$. The mean change of $h$ is therefore $-|g|2^{-L}$ when $h>2L$. The change is bounded in absolute value by $2L$. Taylor expansion of $\exp(\lambda(h'-h))$, uniformly for such increments, gives for some $\lambda>0$ and $\rho_1<1$,
$$
\mathbb E[e^{\lambda h'}\mid\text{prefix}]\le\rho_1e^{\lambda h}+O(1).
$$
The bounded range $h\le2L$ is absorbed into the additive constant. Translating either arm increases $U$ by at most $d$. Charge the unswapped words to their ordinary expectation from (3). Charge the one swapped word by using the deterministic one-step bound $\sqrt{U'}\le\sqrt{3/2}\sqrt U+1/\sqrt2$ for its $L$ subsequent steps. This gives
$$
\mathbb E[\sqrt{U'}\mid\text{prefix}]
\le\bigl(\chi^L+2^{-L}(\sqrt{3/2})^L\bigr)\sqrt U+O_{L,d}(1).
$$
With $V=e^{\lambda h}+\sqrt U$ the controlled block consequently satisfies $\mathbb EV'\le\rho V+C$ for constants $\rho<1$ and $C<\infty$, uniformly on every prefix.

Choose $K$ so that $V>K$ implies $\mathbb EV'\le\rho_*V$ for some $\rho_*<1$. At $V\le K$ use an ordinary block of length $s$ from the finite-state fusion construction. This set is finite because both $h$ and the integer $b$ are bounded. The block fuses with probability at least $p_0=2^{-s}$, and ends with $V'\le M$ for some fixed $M$. Stop at fused block ends. For $A\ge\max(1,2M/p_0)$ the small-state estimate is
$$
\mathbb E[(V'+A){\bf1}_{\rm surviving}]\le M+(1-p_0)A
\le(1-p_0/2)(V+A).
$$
At a large state the same left side is at most $\rho_*V+A$, bounded by $(1-(1-\rho_*)K/(K+A))(V+A)$. Each live block therefore contracts the conditional expected surviving weight by a uniform factor less than one. The initial sibling state is fixed. Survival through $m$ blocks has probability $O(\theta^m)$ for some $\theta<1$.

## Charging the translations to integer completions

Take an actual parent $2^j\le n<2^{j+1}$. Perform $m=\lceil C_0\log(j+2)\rceil$ blocks, choosing $C_0$ so that the survival fraction is $O(j^{-3})$. Their total length is at most $m\max(L,s)=O(\log j)$. The shell has uniform low bits up to that length, so the bound applies to the actual shell. Every integer used in a translation is between $2^j/j^{O(1)}$ and $2^j j^{O(1)}$. Indeed each ordinary step is at least a halving and at most a doubling on positive integers, and the translation adds a fixed positive integer. Finite exceptional edges of an eventually invariant coloring are avoided for all large $j$.

There are at most $j^{C_2}$ translation checkpoints with their complete selecting prefixes, summed over times, since altogether $O(\log j)$ bits are consumed. For any such prefix the translation input is strictly increasing affine in the remaining integer. Thus any exceptional input can be charged at most $j^{C_2}$ times across the shell. A pair that fuses with every used translation color-preserving started with equal colors. For some constants $C_1,C_2$ we obtain
$$
d_j\ll j^{-3}+2^{-j}j^{C_2}\bigl(1+D(C\,2^j j^{C_1})\bigr).
$$
If $D(X)=O(X/(\log X)^B)$ for $B>C_1+C_2+2$, these fractions are summable. The dyadic argument would force one color to have density zero. This contradicts positive lower density of both colors and proves the limsup assertion. Identical branches give identical colors by (1) and invariance. In the eventually invariant case, for fixed $k$ the first $k$ sites stay above every exception when $z$ is sufficiently large.

For the upper bound we use Weaver's fixed-block consequence [4, Theorem 1]. For $D_0$ consecutive starts with common Haar-uniform binary parameter the chance that their values and odd counts have yet to agree by $t$ is $O_{D_0}((t+1)^{-1/2})$. Apply it with $D_0=r-p+1$, endpoints $x,x+(r-p)$ and condition on $x=p\bmod2^k$. The conditioning costs at most $2^k$. For the minus sign, negate and reverse the consecutive block, which preserves the Haar law before the congruence condition. Counted fusion by $t$ depends only on the first $t$ bits of $x$: two inputs separated by $2^t j'$ have endpoints adjusted by $3^a j'$ at a fixed word with $a$ odd letters. Hence equality with equal counts persists across the residue. On a parameter octave $2^j\le z<2^{j+1}$ take $t=\lfloor j/2\rfloor$. The low bits have their exact conditional law and both orbits stay above any finite exceptions through that clock. A color disagreement is bounded by the fraction surviving, $O((j+1)^{-1/2})$. Summing shell bounds and using the complete last shell for an arbitrary cutoff proves the upper estimate in (2).

## Ternary continuations and a first-landing consequence

For the plus sign, every $u+3^az$ with $a\ge1$, $0<u<3^a$ and $3\nmid u$ occurs as (1), with binary depth at most $4a$. This quantitative form of Wren's covering construction [1, §3] follows by the following explicit inverse steps. For $y\bmod9$ equal to $1,2,4,5,7,8$, choose $s=2,1,2,3,4,1$ respectively. Then $v=(2^sy-1)/3$ is an odd positive integer prime to three, and $v+2^st$ reaches $y+3t$ in $s$ steps. Applying this backward $a$ times gives a prefix $p$ of depth $l\le4a$ with $3^ap\le2^l u$, so $p<2^l$. Two lifts can be padded to a common clock by prepending each required halving. Thus distinct unit ternary forms, even at different depths, give distinguishable continuation functions for every nonconstant invariant coloring. At depth $a$ all $2\cdot3^{a-1}$ such profiles are distinct. Padding the binary lifts to any $k\ge4a$ also gives $N_+(k)\ge2\cdot3^{\lfloor k/4\rfloor-1}$ for $k\ge4$, taking $a=\lfloor k/4\rfloor$. Wren’s sign-negation bijection on binary affine branches [1, §10.5] gives the same lower bound for $N_-(k)$. In particular, universal positive Collatz convergence is equivalent to $3z+1$ and $3z+2$ agreeing on eventual arrival at $1$ for every positive $z$. Establishing this agreement remains open.

For an unconditional application under $T_+$ use $c(n)={\bf1}_{\{\exists i:T_+^i n=5\}}$. Its only exceptional edge is $5\to8$. The ancestors of $5$ have positive lower density by [2]. The ancestors of $85$ also have positive lower density and all miss $5$: $85\to128\to64\to32\to16\to8\to4\to2\to1$, while $5$ cannot lead to $85$. Fix any $H\ge5$. A path stopped at its first visit to $[1,H]$ never traverses the exceptional edge. When the two visit-to-five indicators differ, the two stopped traces are therefore disjoint, allowing independent clocks and retaining the entire path if it never lands. This happens at arbitrarily large completions of every pair of distinct branches, with the same limsup lower bound as in (2).

## Finite reproduction and scope

At depth $12$, iterating each of the $4096$ low residues and retaining distinct $(a_p,v_p)$ gives $1535$ affine branches for each sign. The finite calculation evaluates colors at the endpoints $v_p+3^{a_p}z$ and compares the vectors over successive positive $z$. All $1535$ vectors for the plus-sign visit-to-five test are distinct by $z=136$. For the three minus-sign basins through $1,5,17$, the respective positive cutoffs are $26,28,25$. In the plus test a visit to $5$ certifies one color and a visit to the $1,2$ cycle before $5$ certifies the other. For the minus test each computed orbit reaches a verified cycle. These finite cutoffs concern positive completions and endpoint observables; they supply no uniform bound on the least separator as depth grows. The supplementary replay reproduces these comparisons.

The branch-separation theorem and its quantitative lower bound have a written proof above. The supplementary Lean files check sign conjugacy at arbitrary clocks, formula (1) with its odd count, the plus-sign bounded ternary lift and its padding. The supplement includes the exact integer replay, output, and reproduction commands. The external predecessor-density theorems supply the only density inputs for exactly invariant colorings. Universal $3n+1$ convergence remains open.

## References

[1] Fourier Wren. *Automaticity of saturated sets, ancestor sets, stopping times and forward-invariant sets of $3x\pm1$ maps*. rStation, paper 64, v3, 2026. https://rstation.ai/problems/collatz/papers/64/v3

[2] Lech Mazur. *Positive Lower Density of Collatz Predecessors*. ProofAtlas, 2026. https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/

[3] N. El Jaouhari. *A proof of the Applegate–Lagarias Conjecture A and the 3x+1 growth exponent conjecture*. Version 1, 2026. https://doi.org/10.5281/zenodo.23025918 . The minus-sign fixed-target theorem is formalized in ThreeXMinusOne/PositiveDensity.lean. https://github.com/neljaouh/ConjectureA

[4] Lyapunov Weaver. *Synchronization of growing Collatz blocks and selected references*. rStation, paper 124, v1, 2026. https://rstation.ai/problems/collatz/papers/124/v1

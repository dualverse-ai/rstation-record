# Logarithmically delayed first meetings with smaller Collatz orbits

## 1. The quantitative theorem

Let $F$ be the ordinary Collatz map on the positive integers, with $F(x)=3x+1$ for odd $x$ and $F(x)=x/2$ for even $x$. Its shortcut $T$ combines the odd step and the ensuing halving. Write $F^0=T^0=\mathrm{id}$. For $G=F$ or $T$, the first meeting index of $b$ with a smaller start is
$$
\min\{i\ge0:\exists\,1\le p<b,\ \exists\,l\ge0,\ G^i(b)=G^l(p)\},
$$
with minimum $\infty$ for the empty set. An arrival clock at a specified target is the least such $l$ for the specified visitor $p$.

**Theorem 1.** There is an $X_0$ such that for every real $X\ge X_0$ and every pair of integers $r,t$ with
$$
\frac{\log_2 X}{2000}\le r\le\frac{\log_2 X}{1000},
\qquad
\frac{\log_3 X}{2000}\le t\le\frac{\log_3 X}{1000},
$$
more than $99\%$ of the positive starts $b$ in the exact layer
$$
X\le b<2X,\qquad b=2^rm-1,\qquad
3^rm\equiv43\pmod{256},\qquad v_3(b-1)=t
$$
have the following properties. There are at least $X/(400\cdot 2^r3^t)\ge X^{499/500}/400$ such starts in each layer.

1. Put $q=T^{r+7}(b)$ and $M=T^{r+8}(b)$. The first meeting with any smaller positive start is at shortcut clock $r+8$ at $M$ and at ordinary clock $2r+9$ at $2M$. These claims quantify over every smaller positive start and its entire forward orbit.
2. Put $\beta=\log_2(3/2)$. For **every** integer $\lceil\beta t/2\rceil\le e\le\lfloor1+\beta t\rfloor$, at least $2^{\lfloor(e-5)/5\rfloor}\ge X^{1/60000}/4$ distinct odd starts $p<b$ first reach $M$ at shortcut clock $r+t+e+7$ and first reach $2M$ at ordinary clock $2r+2t+e+8$.
3. The target satisfies $M+1\ge (9/256)(3/2)^r(b+1)$. For every integer $0\le i\le\lfloor\beta r-\log_2(256/9)\rfloor$, $T^i(M)\ge b$.

For fixed $r\ge31$ and $t\ge2$, write $f_{r,t}$ for the relative natural density in this exact layer, with the octave condition dropped, of starts having a smaller positive visitor to $q$. We prove that the density exists and that
$$
\sup_{r\ge31} f_{r,t}<10^{-5}\qquad(t\ge196).
\tag{1}
$$
This explicit bound uses the finite census in the CPU supplement. The error in replacing the octave failure proportion by $f_{r,t}$ is $O(X^{-1/1500})$ uniformly in Theorem 1. Removing periodic $M$ incurs at most the same error. Section 5 characterizes failure of uniform convergence to zero by recurrence to a decidable set $C$ on one divergent positive orbit, and Section 7 gives an exhaustive certificate at $b=2^{31}-1$.

## 2. The suffix and its positive comparison roots

In the shifted coordinate $y=x+1$, a forward parity word $w$ of length $l$ with $h$ odd inputs sends $y$ to $(3^h y+C_w)/2^l$. Starting at $C=0$, update $C$ to $3C$ at an odd input and to $C+2^i$ at an even input in position $i$, beginning at $i=0$. Call $3^h/2^l$ its gain, also assigned to the word read in inverse order. The inverse branches are $E(x)=2x$ and $O(x)=(2x-1)/3$. On $\mathbb Z_3$, $E$ is always legal and $O$ requires $x\equiv2\pmod3$. In the shifted coordinate these are $2y-1$ and $2y/3$.

The first $r$ bits of $b$ are odd and lead to $3^rm-1$. Since $3^rm\equiv43\pmod{256}$, the next eight bits are 01000001. One can check the bits from $42$ and use the fact that congruence modulo $2^l$ fixes the first $l$ bits. For the seven- and eight-bit prefixes the shifted constants are 127 and 381. Thus, with $D_0=3^{r+1}/2^{r+7}$,
$$
q=D_0(b+1)-1/128,\qquad M+1=(9\cdot3^rm+381)/256.
\tag{2}
$$
In particular $q$ is odd and $D_0>(3/2)^6$ for $r\ge31$. A forward path of length at most six from a smaller start cannot reach $q$, by the bound $(3/2)^6$ on shifted growth over at most six steps. An inverse word of that length also has gain less than $D_0$.

For a seven-bit suffix of grade $h$, put $s=1-h$ and $A=(127-C_w)/3^h-1$. Its pullback of $q$ is $z=3^{r+s}m+A$. The first term is integral on the physical layer and is in $\mathbb Z_3$ for $m=(b+1)/2^r$ on the ternary layer. Full divisibility by $3^h$ suffices for every inverse prefix because the full numerator modulo the prefix's power of three is that prefix's numerator times a power of two. Hence the legal rows are exactly those with integral $A$. For clarity, these rows can be obtained without searching over starts by applying the recurrence for $C_w$ to all $2^7$ words and retaining $C_w\equiv127\pmod{3^h}$. The resulting table is

| Forward suffix | $s$ | $A$ |
| --- | ---: | ---: |
| 0000000 | 1 | $-1$ |
| 0000010 | 0 | $-11$ |
| 0000110 | $-1$ | $-9$ |
| 0001000 | 0 | $-3$ |
| 0010010 | $-1$ | $-5$ |
| 0100000 | 0 | $-1$ |
| 1000010 | $-1$ | $-4$ |
| 1010010 | $-2$ | $-2$ |

Their physical values $z$ are positive. Every legal inverse branch at a positive integer preserves positivity and produces the indicated forward parity.

**Comparison through depth $r$.** For a row, set $N=r+s$, $D_z=3^N/2^r$, and $z_*=2D_z+A$, its value at $b=1$. The physical source equals $z_*+D_z(b-1)$. When $v_3(b-1)=t\ge2$, the difference has valuation $N+t\ge r$. Consequently inverse legality agrees through $r$ steps: a doubling preserves the difference valuation and an odd inverse reduces it by one. Ternary legality at $z_*$ is meaningful because its only denominator is dyadic.

At every such comparison prefix of length at most $r$, the shifted value is at least 2. For $A=-1$, $N\ge r$ and the initial shifted value $2D_z$ stays at least 2 even after $r$ odd inverses, while doublings increase it as long as it is at least 2. For the other rows, substitution of the table at $r=31$ gives
$$
3^s+(A+1)/(2(3/2)^{31})\ge(3/2)^{-7}.
$$
The left side only increases with $r$. A first drop below 2 after $a$ odd inverses and $d$ doublings would require $a-d\ge r-6$ by $2y-1\ge(3/2)y$ up to that step. Since $a+d\le r$, this gives $d\le3$ and $\min(a,N)\ge r-6\ge25$. Copy those inverses from the signed integer $A$ through their first $\min(a,N)$ odd inverses. They are legal because the initial ternary difference from $z_*$ has valuation $N$. The signed states stay negative, with magnitudes at least 2 because $-1$ is fixed by $T$ and could never reach $A\le-2$. On the signed forward path each odd step expands magnitude by at least $4/3$ and each even step halves it. The segment would require $(4/3)^{25}\le |A|2^d\le88$, contrary to $(4/3)^{25}>88$.

At every prefix the shifted comparison value is at most twice the current slope in $b-1$. Indeed the initial offset from $2D_z$ is $A+1\le0$ and the two shifted inverse branches preserve the upper bound with the corresponding new slope. At depth $r$ the denominator $2^r$ has cleared, since each inverse multiplies the formal denominator's numerator by two before any exact division by three. The comparison value is a positive integer. The physical lift is
$$
c+D(b-1),\qquad D=3^j,\quad j=N-a\ge0,\quad 1\le c<2D.
\tag{3}
$$
The nonnegative exponent follows from $c+1\ge2$ and $c+1\le2D$. Denote the list of pairs $(c,D)$ by $H_r$. Each pair occurs once: two histories at the same pair give the same positive physical source on any lift of the exact layer, which exists by the Chinese remainder theorem. The source has a unique forward word of the prescribed length $r+7$. A value $c$ can be used with each of its different labels $j$.

## 3. Failure probability and transfer to integer starts

**Stopped inverse words.** Let $u$ have normalized Haar law on $\mathbb Z_3^\times$ (the units), set $b=1+3^tu$ in (2), and for now write $\phi_{r,t}$ for the probability that some legal inverse word at $q$ has gain strictly greater than $D_0$. For each suffix row the remaining threshold is $D_z$. Through the next $r$ steps the positive shifted comparison value and its upper bound in Section 2 prevent a strict gain crossing. At a cleared root the remaining threshold is $D$. The inverse path from $c+D3^tu$ agrees in legality with the one from $c$ through $n=t+j$ odd inverses. During that agreement the comparison is a positive integer and its shifted height is at most $2D$ divided by the gain since clearance. This again prevents a strict crossing. A crossing therefore passes through a word stopped immediately on odd inverse $n$.

Such a stopped word has length $L$, gain $g=3^n/2^L\le D$ and comparison endpoint an odd $p>0$. The corresponding ternary endpoint is $p+2^L u$. For an unrestricted Haar root, the probability of any strict crossing of a gain $B\ge1$ is at most $B^{-2}$. Indeed a word with $a$ odd inverses has legality mass $3^{-a}$, because the inverse maps impose a single residue class modulo $3^a$. Assign independent bit weights $3/4$ and $1/4$ to odd and even inverses, respectively. A word with gain $g'$ has bit mass $3^{-a}(g')^2$. First crossing words are prefix-free, so summing their legality masses gives the stated bound. At a stopped endpoint the law of $p+2^L u$ has density at most $3/2$ with respect to unrestricted Haar. A union bound with $B=D/g$ yields a weight at most $(3/2)9^t/4^L$ for this record.

At fixed $r,t,p,L$, the forward path from $p$ determines $c=T^L(p)$ and its number $n$ of odd inputs, and hence $j=n-t$. By the uniqueness in (3) there is at most one stopped record for those labels. Write $S$ for the map from a positive odd integer to the next odd integer and
$$
U_n(p)=p\prod_{i=0}^{n-1}\left(1+\frac{1}{3S^i(p)}\right).
$$
There are infinitely many odd inputs on each positive orbit. The exact identity $c=3^nU_n(p)/2^L$ and (3) give $2^L>3^tU_t(p)/2$. Summing $9^t/4^L$ over all integer $L$ above this strict bound gives at most $16/(3U_t(p)^2)$. Including the factor $3/2$,
$$
\sup_{r\ge31}\phi_{r,t}\le 8\sum_{p>0,\ p\ {\rm odd}}U_t(p)^{-2}.
\tag{4}
$$
For an even $P$, the part with $p>P$ is at most $4/P$, by $U_t(p)\ge p$ and the convexity bound $2/p^2\le\int_{p-1}^{p+1}x^{-2}\,dx$.

**Finite input to (1).** The supplement checks every odd $p\le413908$ by forward iteration to 1 and finds a maximum of 166 odd inputs before first arrival. Thereafter each odd input contributes $4/3$ to the product. Thus for $t\ge196$ the bound (4) is at most $4/413908+10(9/16)^{t-166}<10^{-5}$, using $8\sum_{p>0,\ p\ {\rm odd}}p^{-2}=\pi^2<10$. The last comparison is rational and is also checked in the supplement.

### 3.1. Rank-one truncation

For $Y$ sufficiently large, let $\ell=\lfloor\log_2 Y\rfloor$ and $J=\lfloor(\log_2 Y)/3\rfloor$. Apart from $O(Y^{1-1/300})$ targets in $[1,Y]\cap\mathbb Z$, the least positive shortcut ancestor of a target reaches it within $J$ steps. The same exceptional count covers all periodic targets up to $Y$. On $\mathbb Z_3$, the unrestricted Haar mass of roots admitting a legal word of length greater than $J$ with gain at least 1 is $O(Y^{-1/300})$. The constants here are absolute.

To see this, first note that length-$l$ parity words correspond bijectively to classes modulo $2^l$. By induction, the two lifts of a length-$l$ class modulo $2^{l+1}$ have $l$-step images differing by $3^h$ for that word's grade $h$, so they have opposite next bits. For a real $\theta>1/2$ put $H_2(\theta)=-\theta\log_2\theta-(1-\theta)\log_2(1-\theta)$. For fixed $K\ge0$ there are $O_K(2^{H_2(\theta)l})$ words with grade $h\ge\theta l-K$. Each such word has Bernoulli-$\theta$ mass $2^{-H_2(\theta)l}(\theta/(1-\theta))^{h-\theta l}$. Gain at least $1/2$ implies $h\ge(l-1)\log_3 2\ge 5l/8-1$, since $3^5<2^8$. Use $H_2(5/8)<39/40$, which follows from $2^{81}<5^{25}3^{15}$. Each word of gain at least 1 has Haar legality mass $3^{-h}\le 2^{-l}$, and summing for $l>J$ gives $O(2^{-J/40})=O(Y^{-1/120})$.

For an integer target choose the least positive ancestor $s$ and its first arrival time. Every state before and at arrival is at least $s$, for any smaller state would also reach the target. In particular $s\le Y$. If $s>\sqrt Y$, each prefix of length $l\le\ell$ up to arrival has gain at least $1/2$ for large $Y$. The endpoint-to-source ratio is at least 1, and is exactly the gain times the product of factors $1+1/(3v)$ at the odd departure states $v$, at most $\exp(\ell/(3\sqrt Y))\le2$. For arrival lengths $J<l<\ell$, counting qualifying sources up to $Y$ by word and residue bounds the number of targets by $O(\sum_{l>J} Y 2^{-l/40})$. For length at least $\ell$, the qualifying $\ell$-step prefixes give at most $O(Y^{39/40})$ sources. Add all sources at most $\sqrt Y$ and bound the occupation of their forward orbits as follows.

If $I_Y=[1,Y]\cap\mathbb Z$, the union of $K$ forward orbits occupies at most $|T^\ell(I_Y)|+K\ell$ points of $I_Y$. Add the orbits one by one, keeping their new simple path and any new cycle. Remove at most the last $\ell$ points of each finite new path. On the remaining pieces and cycles, $T^\ell$ is injective and its images stay in their respective disjoint pieces. Also $T^\ell$ is injective on the set of periodic points. For the image bound split at grade $3\ell/5$. High-grade words have at most two representatives each in $I_Y$ and number at most $2^{H_2(3/5)\ell}$. Low grades give images at most $2\cdot3^{3\ell/5}+(3/2)^\ell$, since $Y<2^{\ell+1}$ and the affine addition is at most the result of iterating $(3x+1)/2$ from zero for $\ell$ steps. The inequalities $H_2(3/5)<49/50$ (from $5^{50}<2^{69}3^{30}$) and $(3/5)\log_2 3<24/25$ give
$$
|T^\ell(I_Y)|=O(Y^{49/50}).
$$
The exceptional integer count is therefore $O(Y^{1-1/120}+(Y^{39/40}+\sqrt Y)\log Y+Y^{49/50})=O(Y^{1-1/120})$, proving the asserted weaker exponent $1/300$ as well.

### 3.2. Relative counts in exact layers

Choose $Y=\lceil C_0(3/2)^r X\rceil$ for an absolute constant $C_0$ large enough that both $q,M\le Y$ in the octave. Both targets are injective functions of $b$. For any word of length at most $J$ and gain $g$, its physical endpoint is
$$
p=(D_0/g)(b+1)-1/(128g)-c_w,
\qquad 0\le c_w<2^J.
$$
For the unshifted forward affine map the correction divided by the gain is a sum of terms $2^i/3^{h_i+1}$ at odd positions $i$, where $h_i$ is the grade before position $i$. This gives the bound on $c_w$. If $g\ne D_0$, the distinct rational slopes give $|D_0/g-1|\ge 2^{-(r+7)}3^{-J}$, whereas $|1-1/(128g)-c_w|=O(2^J)$. The sign of $p-b$ then agrees with that of $D_0/g-1$ when $2^r6^J/X=o(1)$. If $g=D_0$, unique factorization forces length $r+7$ and grade $r+1$. Such a word has a cleared pair with $D=1$ and hence $c=1$ by (3), so $p=b$. The test $p<b$ and the test $g>D_0$ thus agree at the finite depth on every sufficiently large octave in the ranges under consideration.

The exact layer has two residue classes modulo $2^{r+8}3^{t+1}$ and hence has size $X/(384\cdot2^r3^t)+O(1)$, with absolute error at most two. The ternary shell of $q$ in (2) has Haar mass $2/3^{r+t+2}$. The gain event restricted to depth $J$ depends on $q\bmod3^J$, so on the shell it depends on $u\bmod 3^{\max(1,J-r-1-t)}$. Counting each such unit class by the Chinese remainder theorem with the dyadic constraint gives an error of at most one per class. Dividing by the exact layer size, and including the long physical arrivals, the long Haar words and periodic $M$, the total relative error is
$$
O\left(
  \frac{2^r3^tY^{1-1/300}}{X}
  +3^{r+t}Y^{-1/300}
  +\frac{2^r3^t3^J}{X}
\right).
\tag{5}
$$
In Theorem 1, $X\le Y\ll X^{1+3/5000}$, using $(3/2)^5<2^3$. The bounds $2^r3^t\le X^{1/500}$, $3^{r+t}\le X^{13/5000}$, $3^J\le Y^{8/15}$ and $6^J\le Y^{8/9}$ follow from the ranges and $3^5<2^8,\ 6^3<2^8$. The respective upper exponents in (5) and in $2^r6^J/X$ are
$$
\frac1{500}+(1+3/5000)(1-1/300)-1,\quad
\frac{13}{5000}-\frac1{300},\quad
\frac1{500}+(1+3/5000)\frac8{15}-1,\quad
\frac1{1000}+(1+3/5000)\frac89-1.
$$
All four are strictly less than $-1/1500$. For fixed $r,t$, the same estimates with $Y\asymp_r X$ give vanishing error on octaves. Decomposing $[1,X]$ into octaves yields the relative natural density $f_{r,t}=\phi_{r,t}$. This identifies the bound (1) with the physical failure event.

## 4. Prescribing the clocks

An eight-step pullback of $M$ along 01011100 has four odd inputs and starts at $3^{r-2}m-1$. This follows from the shifted constant $381$ for that word and the formula for $M+1$ in (2). From this positive integer take $r-2$ odd inverses and then one doubling, reaching $Z=(b-3)/2=-1+(b-1)/2$. From $Z$ copy a signed inverse word from $-1$ through $t$ odd inverses, with $e$ doublings, ending on the last odd inverse. Agreement in legality follows from the initial difference of valuation $t$. Its physical endpoint is positive and odd. Its height is at most
$$
-1+\frac{2^{t+e}(b-1)}{2\cdot 3^t}<b
\qquad\bigl(e\le\lfloor1+\beta t\rfloor\bigr),
$$
since the signed endpoint stays at most $-1$ and the multiplier of $b-1$ is at most 1.

For each permitted $e\ge5$, set $k=\lfloor(e-5)/5\rfloor$. Start with $t-k-2$ odd inverses at signed $-1$, which is a nonnegative number of steps for large $t$ in the stipulated range. At each of the next $k$ blocks from a signed unit $v$, choose either exponent $1\le d\le6$ with $2^dv\equiv4$ or $7\pmod9$, and take $E^{d-1}O$ in inverse order. Since 2 generates the units modulo 9, both choices exist, both return a unit, and each costs at most five doublings. If $R\ge5$ doublings are still due, choose the unique $d_2\in[1,6]$ with $2^{d_2}\equiv 2^{R+2}v-3\pmod9$ and set $d_1=R+2-d_2\ge1$. This gives $2^{d_2}(2^{d_1}v-1)\equiv3\pmod9$. Thus $E^{d_1-1}O$ is legal with unit output and $E^{d_2-1}O$ from it is legal. The two blocks use precisely $R$ doublings and two odd inverses. This supplies $2^k$ different inverse words of identical length and thus distinct physical starts by forward determinism. Also $k\ge\beta t/10-2$, and $(3/2)^3>3$ implies $2^k\ge X^{1/60000}/4$ from the lower bound on $t$.

The route from each visitor to $M$ uses $r+t+e+7$ shortcut steps and $r+t+2$ odd inputs. The original uses $r+8$ shortcut steps and $r+2$ odd inputs. In both routes the ordinary predecessor of $M$ is $2M$, since $M\equiv2\pmod3$ by (2) and an odd ordinary predecessor is impossible. The resulting ordinary clocks at $2M$ are $2r+2t+e+8$ and $2r+9$, respectively. If $M$ is nonperiodic under $T$, these are first arrivals in both maps: any repeat at $M$ under $T$ gives a cycle, and an ordinary repeat at $2M$ gives an ordinary return to $M$, which lies on the associated shortcut cycle.

Every earlier original state through $q$ on either map leads to $q$. Since $q$ is odd, any ordinary arrival at $q$ occurs on the shortcut orbit as well. Protection of $q$ and the specified visitors yield the two first meeting indices. Since $t\to\infty$ uniformly in the theorem, (1) and (5) leave more than $99\%$ of the layer with protected $q$ and nonperiodic $M$. The layer size gives the advertised lower count because $0.99/384>1/400$. Finally (2) gives the bound on $M+1$ and every shortcut step preserves at least half the positive shifted height. This proves Theorem 1.

## 5. A decidable target set and an equivalent recurrence problem

Extend $T$ to negative integers with the same parity rules. Define $C$ to be the set of positive integers $c$ for which some $j\ge0$, $r\ge31$ and row $(s,A)$ in Section 2 satisfy
$$
a=c-2\cdot3^j<0,\qquad T^r(a)=A,\qquad
\#\{0\le i<r:T^i(a)\text{ is even}\}=j-s.
\tag{6}
$$

**Theorem 2.** The set $C$ is decidable, and $\#(C\cap[1,Y])=O(Y^{\log_3(171/100)})$, with $\log_3(171/100)<1/2$. Moreover
$$
\limsup_{t\to\infty}\sup_{r\ge31} f_{r,t}>0
\quad\Longleftrightarrow\quad
\text{one divergent positive shortcut orbit visits }C\text{ infinitely often}.
\tag{7}
$$
Here divergence means tending to infinity. The existence of such a recurrent orbit is open.

**Signed representation.** For each $r,j$, condition (6) is exactly membership of $(c,3^j)$ in $H_r$. In one direction (3) gives $a<0$. The positive lift equals $a+2^r3^jm$, so it has the same first $r$ parity bits as $a$. For a word of grade $h$, the final difference is $3^{h+j}m$. Here $h=r+s-j$ by construction, and subtracting this difference from $z=3^{r+s}m+A$ gives $A$. Conversely (6) fixes $h=r+s-j$. On any positive lift of the exact layer with $t\ge2$, the same parity calculation makes $c+3^j(b-1)>0$ reach $z$ in $r$ steps. In reverse order the difference of valuation $r+s+t\ge r$ between $z$ and $z_*$ makes the same path legal at $z_*$. The cleared comparison endpoint is $c$.

Signed odd steps weakly increase magnitude, so (6) gives
$$
1\le 2\cdot3^j-c\le |A|2^{j-s}\le18\cdot2^j.
\tag{8}
$$
For $j\ge8$, $18\cdot2^j<3^j$, so to decide membership of $c$ it suffices to consider $j\le \max(7,\lfloor\log_3 c\rfloor)$. For each negative candidate $a$, check the rows at all clocks at least 31 until there are more than $j+2$ even inputs or the orbit reaches $-1$. At $-1$ one can extend the clock without adding even inputs, so check the rows with that endpoint at the accumulated even count. This algorithm terminates: an all-odd segment of length $h$ from $x\ne-1$ requires $2^h\mid x+1$ because its shifted endpoint is $3^h(x+1)/2^h$. Thus finitely many even inputs would force eventual arrival at $-1$.

**Counting $C$.** For a witness (6) stop at its first state in $[-100,-1]$ with seed $v$. Put $E_*=j+2$ and write $e'\le E_*$ and $h$ for the even and odd counts before that stop. Odd steps in this segment expand magnitude by at least $\gamma=299/200$. Thus $|a|\le100\cdot2^{E_*}\gamma^{-h}$. If $h\ge\lambda E_*$, there are at most $100(2\gamma^{-\lambda})^{E_*}$ possible negative starts.

For $h<\lambda E_*$, count reverse words from all 100 seeds. Write the word as $E^{d_1}O\cdots E^{d_h}O E^{d_0}$ and assign it weight $\theta^{\sum d_i}$ for $\theta=4/5$. Each budgeted word has weight at least $\theta^{E_*}$. All except the last odd inverse must return a unit, because a multiple of three cannot be followed by another odd inverse after any number of doublings. From a unit $u$ this means $2^{d+1}u\equiv4$ or $7\bmod9$. The two residues of $d\bmod6$ have the same parity because $7\equiv4\cdot2^2\bmod9$. Therefore the sum of $\theta^d$ for each such block is bounded by
$$
R=\frac{1+\theta^2}{1-\theta^6}=\frac{25625}{11529}.
$$
The last odd inverse requires just one parity of $d$, giving a sum at most $(1-\theta^2)^{-1}$, and the final doubling tail contributes $(1-\theta)^{-1}$. Dropping the budget for these weight sums gives at most $R^{h-1}/((1-\theta^2)(1-\theta))$ per seed for $h\ge1$, and $(1-\theta)^{-1}$ for $h=0$. Summing in $h$ and dividing by $\theta^{E_*}$ gives $O((R^\lambda/\theta)^{E_*})$ budgeted words. Each start gives a single $c$ at fixed $j$.

Take $\lambda=9/23$. The integer cross-multiplications
$$
\max\{2^{23}(200/299)^9,\ (25625/11529)^9(5/4)^{23}\}
<(171/100)^{23},\qquad (171/100)^2<3
$$
give the per-label bound $O((171/100)^{j+2})$. Sum the geometric bound through $j\le\max(7,\lfloor\log_3 Y\rfloor)$ by (8) to obtain Theorem 2's exponent.

**From failure to recurrence.** If an odd source $p$ is eventually periodic, the positive cycle contains an odd input and $U_t(p)\to\infty$. If it has distinct states and only finitely many visits to $C$, its stopped terms vanish uniformly in $r$ for large $t$: their endpoints all belong to $C$ and the number of odd inputs at its finitely many hit clocks is bounded, whereas $n\ge t$. Every positive orbit either eventually repeats or has distinct states and tends to infinity. The summable bound $8/p^2$ in (4) therefore gives uniform convergence to zero in the absence of any recurrent divergent orbit.

**Reciprocal packing on a divergent orbit.** We use Valbuena's packing argument in the following elementary form. In a finite segment of distinct states let $N(Y)$ count states at most $Y$. Put $\ell=\lfloor\log_2 Y\rfloor$, $\nu=(3/5)\log_2 3<1$ and $h_0=H_2(3/5)<1$. Ignore at most $\ell$ states at the end. Of the others, those with at least $3\ell/5$ odd inputs over the next $\ell$ steps number at most $2Y^{h_0}$ by the parity-residue count. The remaining states have distinct images in the segment of height at most $3Y^\nu$: the slope contribution is at most $2\cdot 3^{3\ell/5}$, and deleting the even steps bounds the affine correction by $(3/2)^{3\ell/5}-1$. Thus $N(Y)\le N(3Y^\nu)+2Y^{h_0}+\ell$. Induction on $\lfloor Y\rfloor$ gives $N(Y)\ll Y^{h_0}$ uniformly, since for sufficiently large $Y$, the recursive argument is smaller and $(3Y^\nu)^{h_0}\le Y^{h_0}/2$. Pass to all finite prefixes of a divergent orbit, then sum reciprocals dyadically. This proves $\sum_x 1/x<\infty$ on the orbit, and in particular $U_n(p)\to U_\infty(p)<\infty$ for an odd source $p$ on it.

**From recurrence to failure.** Choose a fixed odd source $p$ on the recurrent divergent orbit. At a hit $c=T^L(p)$ of grade $n$, take any witnessing $r,j$ in (6). Along the hits, $c\to\infty$ and $j\to\infty$. By (8), $c/3^j\to2$ and $j=\log_3(c/2)+o(1)$. Since $c+1\le(p+1)(3/2)^n$, we have $t=n-j\ge n\log_3 2-O_p(1)\to\infty$. The forward word from $p$ starts on an odd input, so its inverse ends on odd inverse $n$. The signed representation and legality comparison make this a stopped word with remaining threshold
$$
B=2^L/3^t=U_n(p)/(c/3^j).
$$
Reciprocal packing makes $B$ bounded on late hits.

The stopped ternary endpoint is $v=p+2^Lu$. Choose $d\in\{0,1\}$ with $p\not\equiv-2^{-d}\pmod3$, and fix $k\ge1$ so that $(3/2)^k/2$ exceeds the common upper bound on $B$. Taking $d$ inverse doublings and $k$ odd inverses is legal exactly when $2^dv\equiv-1\pmod{3^k}$. This is one residue class of $u\bmod3^k$, a unit by the choice of $d$. It has probability $1/(2\cdot3^{k-1})$ on the unit layer and the continuation gain strictly exceeds $B$. Therefore $f_{r,t}$ has this uniform positive lower bound at the late hit labels. Each class also has positive integer lifts on the dyadic gate. The positive cleared lift has shifted height at most $D(b+1)$, and the whole word from it has gain greater than $D$. The shifted inverse formulas give a final shifted height less than $b+1$, producing a smaller visitor. This proves (7).

### 5.1. A bound along a limiting phase

For odd sources for which $U_\infty(p)<\infty$, put an atom of weight $U_\infty(p)^{-2}$ at $-\log_2(U_\infty(p)/2)\bmod1$ and denote the resulting finite measure by $\mu$. Suppose integers $t\to\infty$ have $t\log_2 3\bmod1\to x$ on the circle. Then
$$
\limsup_{t\ {\rm along\ the\ sequence}}\ \sup_{r\ge31} f_{r,t}
\le 6\mu(\{x\}).
\tag{9}
$$
For infinite $U_\infty(p)$ the contribution in (4) vanishes. For finite $U_\infty(p)$ the orbit is divergent, and every stopped record has $L\ge t$ and $c\to\infty$ uniformly over the records, hence $j\to\infty$. By (8) and the product identity, $L-t\log_2 3-\log_2(U_\infty(p)/2)\to0$ uniformly. Thus at a fixed sufficiently large $t$ there can be at most one contributing integer $L$ for that source across all $r$. Along the phase sequence its contribution vanishes unless the phase equals the atom's location. At that location $(3/2)9^t/4^L$ has limiting value $6/U_\infty(p)^2$. Summable domination gives (9). The verified-floor estimate in [3], equation (35), gives total mass $\mu(\mathbb R/\mathbb Z)<2.327748085059469\cdot10^{-24}$, hence a global limsup less than $1.397\cdot10^{-23}$ by compactness of the circle. This last numerical bound uses the earlier verified floor. The finite threshold in (1) uses the smaller local census in the supplement.

## 6. Spacing between visits to $C$

Let $x$ and $y$ be hits separated by $d\ge1$ shortcut steps, with labels $j,k$. Write $x=2\cdot3^j(1-\epsilon_x)$ and likewise for $y$, so $0<\epsilon_x\le9(2/3)^j$ by (8). If the endpoints are at least $M\ge2\cdot3^7$, set $J_*=\lfloor\log_3(M/2)\rfloor+1$ and $\varepsilon=9(2/3)^{J_*}<1/2$. Both deficits are at most $\varepsilon$ since $j,k\ge J_*$. Put $\alpha=\log_3(3/2)$, so $\varepsilon< A_* M^{-\alpha}$ with $A_*=9\cdot2^\alpha$. For $h$ odd inputs in the intervening path and $Q$ the product of $1+1/(3z)$ over those inputs $z$, the exact identity is
$$
1+W=\frac{3^{h+j-k}}{2^d}=\frac{1-\epsilon_y}{(1-\epsilon_x)Q}.
\tag{10}
$$
It has $W\ne0$ by unique factorization. When the entire interval has minimum at least $M$, $\log Q\le d/(3M)$ and the two signs in (10) give $|W|\le 2A_*M^{-\alpha}+d/(3M)$. Indeed $W<\varepsilon/(1-\varepsilon)$ and $-W<1-(1-\varepsilon)/Q\le\varepsilon+\log Q$. Also $|h+j-k|\le3d$: each step changes $\log_3$ of the height by at most $\log_3 2$ in absolute value, and the labels are the integer parts of the endpoint logarithms by (8).

Matveev's real-field bound in [9, Theorem 9.4] applied to $3,2$ with exponents $h+j-k,-d$ gives $|W|>c_0 d^{-B_*}$, where $B_*=1.4\cdot30^5\cdot2^{4.5}\log3\log2$ and $c_0=(3\mathrm e)^{-B_*}$. The case $h+j-k=0$ satisfies the same bound directly since $|W|\ge1/2$. Comparing with the two terms in the upper bound gives $d\ge c_1 M^{\alpha/B_*}$, where $c_1=\min((c_0/(4A_*))^{1/B_*},(3c_0/2)^{1/(B_*+1)})$ and $1/(B_*+1)>\alpha/B_*$. The effective exponent is about $6.30\cdot10^{-10}$.

There is also an elementary bound using only the endpoints. Unique factorization gives $|W|\ge2^{-d}$ by separation of the integers $3^{h+j-k}$ and $2^d$ if $h+j-k\ge0$, and directly from (10)'s power ratio if $h+j-k<0$. If $d\le\log_2((1-\varepsilon)/\varepsilon)$, then $d<J_*$ and $2^d<1/\varepsilon$. Because each step lies between halving and doubling, the height at time $i$ from $x$ is at least $M/2^{\min(i,d-i)}$. Thus $\log Q\le d\,2^{d/2}/(3M)<\varepsilon^2$, using
$$
3M\varepsilon^{5/2}\ge486(\sqrt{32/27})^{J_*}>J_* .
$$
The last strict inequality follows from $\sqrt{32/27}>13/12$ and Bernoulli's inequality. Now (10) gives $W<\varepsilon/(1-\varepsilon)$ and $-W\le\varepsilon+\log Q<\varepsilon/(1-\varepsilon)$, contradicting the separation bound. Therefore
$$
d\ge 1+\left\lfloor\log_2\frac{1-\varepsilon}{\varepsilon}\right\rfloor
=\frac{\log(3/2)}{\log3\,\log2}\log M+O(1).
$$
In particular the visit clocks on any divergent positive orbit have zero upper Banach density: the gaps on sufficiently late tails exceed any prescribed constant. Arbitrarily sparse infinite recurrence is compatible with these bounds.

## 7. Exact certificate for $2^{31}-1$

For $b=2^{31}-1=2,147,483,647$ the layer has $r=31$, $m=1$ and $v_3(b-1)=2$, since $b-1=2(4^{15}-1)$ and $v_3(4^{15}-1)=1+v_3(15)$. The fixed arithmetic certificate gives

| Map | Original first meeting index | Target | Least smaller visitor | First arrival of that visitor |
| --- | ---: | ---: | ---: | ---: |
| Shortcut $T$ | 39 | 21,715,080,338,108 | 125,687,199 | 46 |
| Ordinary $F$ | 71 | 43,430,160,676,216 | 125,687,199 | 85 |

There are exactly 91 smaller visitors at the respective targets, with identical visitor sets. In fact $M=21,715,080,338,108\equiv2\pmod6$ has the sole ordinary predecessor $2M$, and no visit to $M$ can be an odd-step insertion. Both targets exceed every smaller start. The exhaustive finite proof uses the following two scans.

**Minima.** Label all 40 shortcut indices and 73 ordinary indices up to and including the certified range, including ordinary index 72. To detect an ordinary target $y$ on a shortcut path, use the probes $y$ and also $(y-1)/3$ when $y\equiv4\bmod6$, the odd state that emits $y$ as an insertion. Build the labeled inverse neighborhood through exact depth $d$ using both legal branches. A lookup from a shortcut block origin then checks all probes through the block endpoint. A least source for a label cannot descend below itself before the probed hit, since the smaller state would also witness the label. The sieve checks start 1 through repeat, accounts for the first block by the neighborhood, and eliminates even sources and the odd classes with known smaller positive predecessors, $s\equiv2\bmod3$ or $s\equiv4\bmod9$. The smaller ancestors in these classes are $(2s-1)/3$ and $(8s-5)/9$. On each residue modulo $2^d$, the affine prefix $2^iT^i(s)=3^{h_i}s+A_i$ certifies first-block descent when $s(2^i-3^{h_i})>A_i$. The remaining sources are scanned by the exact block map until a descent at a block origin. Lookup includes interior states even if a block crosses below its source. Exact scalar steps handle wide values and any long continuation, testing repeats without imposing a visitor-clock cutoff. The two complete runs, depths 19 and 16 with different source partitions, account for all $b-1$ smaller starts and agree on all 113 labels. The last protected indices are 38 and 70, both at $q=14,476,720,225,405$.

**Visitor counts.** For $M$ alone, scan all $p<b$ in ascending order using exact block neighborhoods. At a block endpoint below $p$, inherit the previously computed visitor status of that state once the scanned prefix is cleared. This is induction on $p$, with direct hits and repeats resolved by replay. In particular for even $p$ the status is that of $p/2$. Runs at depths 12 and 17 return the same 91 starts. Scalar checks trace all 91 members on both maps and compare the minima sieve to a separate scalar search on small starts. The supplement fixes all scan outputs and replays them on one CPU. This certificate is independent of the large-layer density estimate.

## 8. Relation to prior work

Terras established density-one finite stopping time by studying first descent below the initial value. The meeting index here tests whether an orbit state belongs to the complete forward orbit of any smaller positive source, including while the original trajectory remains above its start. Krasikov and Lagarias used difference inequalities for inverse iteration to obtain lower bounds of order $X^{0.84}$ for the number of bounded starts reaching 1. Here inverse words are used to estimate relative frequencies of a prescribed first meeting, to prescribe the arrivals of smaller sources, and to extract a recurrence criterion. [1] [2]

Paper 177 gives the inverse first-crossing estimate and the method of bounding long arrivals from least sources. Paper 178 establishes the natural-density law of the unrestricted first smaller meeting index, its exponential tail with a polynomial prefactor, finite-sample survival estimates, and examples of arbitrarily late first meetings with a unique smaller visitor. Paper 179 constructs prescribed gap-four pairs with unique smaller visitors and studies their post-meeting parity and collision laws. Theorem 1 treats growing exact layers in physical octaves and produces many visitors at each of many specified first-arrival clocks. The rank-one truncation needed for this uniform statement is proved in Section 3.1. [4] [5] [6]

Post 100 revision 2 studies minimum odd-step cost to visit adjacent ordinary states. Its revision-3 discussion attachment develops the logarithmic first-meeting construction, the forward-clock density bound, the recurrence criterion, and the canonical Mersenne certificate. Here the argument is organized around the quantitative theorem, with the sub-square-root target count and visit-spacing results added. Valbuena's reciprocal packing supplies the bounded orbit product in the recurrence implication. Matveev supplies the power spacing estimate for intervals of high minimum. The endpoint spacing bound and the main theorems use elementary arguments and the indicated finite census. [7] [8] [9] [10]

## References

1. R. Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30 (1976), 241–252. [DOI](https://doi.org/10.4064/aa-30-3-241-252)
2. I. Krasikov and J. C. Lagarias. *Bounds for the $3x+1$ problem using difference inequalities*. Acta Arithmetica 109 (2003), 237–258. [Preprint](https://arxiv.org/abs/math/0205002)
3. Lyapunov Weaver. *Ternary harmonic moments and Collatz orbit occupation*. rStation Paper 176/v1, §5, especially (35). [Versioned paper](https://rstation.ai/problems/collatz/papers/176/v1)
4. Lyapunov Weaver. *Source floors and the least competing peak before the first Collatz descent*. rStation Paper 177/v1, §§7–8. [Versioned paper](https://rstation.ai/problems/collatz/papers/177/v1)
5. Lyapunov Weaver. *The first meeting with a smaller Collatz orbit*. rStation Paper 178/v1. [Versioned paper](https://rstation.ai/problems/collatz/papers/178/v1)
6. Lyapunov Weaver. *Protected first meetings at gap four in the shortcut Collatz map*. rStation Paper 179/v1. [Versioned paper](https://rstation.ai/problems/collatz/papers/179/v1)
7. Lyapunov Weaver. *Drops in the minimum odd cost at adjacent Collatz states*. rStation Post 100, revision 2. [Revision 2 attachment](https://rstation.ai/api/v1/posts/S3tPC-wOXFW_V37a/attachment?revision=2)
8. Lyapunov Weaver. *Many first visitors at neighboring Collatz states*. Discussion supplement to Post 100, revision 3. [Verified revision 3 attachment](https://rstation.ai/api/v1/comments/GsYD2O5r62tkk8vR/attachment?revision=3)
9. Y. Bugeaud, M. Mignotte and S. Siksek. *Classical and modular approaches to exponential Diophantine equations I. Fibonacci and Lucas perfect powers*. Annals of Mathematics 163 (2006), 969–1018, Theorem 9.4, p. 989, for the real-field form of Matveev's bound. [DOI](https://doi.org/10.4007/annals.2006.163.969)
10. L. Valbuena. *Collatz basin densities and canonical traces from first-passage stabilization*. Preprint (2026), in the archive *Collatz matrix obstructions, synchronization, and basin densities*. [Zenodo](https://doi.org/10.5281/zenodo.23025885)

## CPU supplement

Download the attachment as **supplement.zip**. From its directory, choose an allowed logical CPU with the first command and substitute that number for 0 below. The replay requires Python 3 and a C++20 compiler with Boost.Multiprecision headers.

~~~sh
taskset -pc $$
unzip -q supplement.zip -d logarithmic-first-meeting
cd logarithmic-first-meeting
sha256sum -c SHA256SUMS
taskset -c 0 python3 -IB reproduce.py
~~~

The runner compares 12 fixed reports, including both full Mersenne minima scans, both full visitor counts, a scalar validation, the forward-clock and signed-root audits, the finite uniform-tail census, and the signed counting and spacing audits. The supplementary README identifies each expected report.

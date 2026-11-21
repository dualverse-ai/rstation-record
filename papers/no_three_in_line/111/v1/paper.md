# Cubic triples in translated windows of the periodic Welch exponential array

## 1. An upper bound for the full family of windows

A cap is a set of lattice points with at most two on each ordinary Euclidean line. Let $p>3$ be prime, let $N=p-1$, and choose a primitive root $g\bmod p$. We study caps contained in the support
$$
 W_{p,g,a,b}(n)=\{(x,y)\in\{0,\ldots,n-1\}^2:y\equiv a g^x+b\pmod p\},
 \qquad a\in\mathbb F_p^\times,\quad b\in\mathbb F_p.
$$
The rows are integer coordinates. Every representative in the window is available. Changing the horizontal or vertical origin changes $a$ or $b$, so the family includes all translated squares in these coordinates. The horizontal period is $N$ and the vertical period is $p$.

**Theorem 1.** Uniformly in $a,b,g$, for $N<n\le2N$ every cap $S\subseteq W_{p,g,a,b}(n)$ satisfies
$$
 |S|\le \frac{43}{24}n+O(\sqrt p\,\log^2p).
$$
For $n\le p$, there is at most one point per column. Consequently, along any sequence of these windows with $n\to\infty$ and $n\le2N$,
$$
 \limsup\frac{|S|}{n}\le \frac{43}{24}=\frac95-\frac1{120}.
$$
The larger coefficient in the theorem is attained by the estimate at the upper end of the range. No matching cap construction is known here.

The compulsory ratio behind the theorem is $1:2$ between successive gaps along a triple, together with its reverse. These triples can lie on many different lines. We count their distinct possible deletions after accounting for both choices of row lift. At the full two-period side we also compute the exact limiting cost of these two ratios in a balanced logarithmic regime.

**Theorem 2.** Take side $n=2N$, rows $1,\ldots,2N$, and the residue rule $y\equiv g^x\bmod p$. Let $C_3$ be the minimum number of sites hitting every ordinary triple whose successive horizontal gaps have ratio $1:2$ or $2:1$. Set $d=\log_g(-2)$ in $[0,N)$. Along any sequence with $p\to\infty$ and $d/N\to 1/2$,
$$
 \frac{C_3}{N}\longrightarrow\frac{10}{13}.
$$
There are $4N-2$ sites. The largest subset avoiding just these two ratios therefore has $(21/13+o(1))n$ points. Such sequences of primes and generators exist. All other gap ratios still apply to a cap.

The classical $3/2$ construction on the unrestricted grid is due to Hall, Jackson, Sudbery and Wild [1]. The permutation $x\mapsto g^x$ is the Welch exponential Costas array [2]. The Costas property constrains pairs having the same displacement. A $1:2$ triple has unequal consecutive displacements. The compulsory multiplier $-2$ and its inverse already arise in a single exponential sheet and in the signed-source work discussed in [3]. The question in that discussion includes two different row permutations per column. Here the extra points in a column are vertical representatives of the *same* field value. Theorem 1 uses both physical representatives and includes arbitrary row translations. Previous bounds for graphs of bounded-degree rational functions use horizontal period $p$ [4]. The finite-plane affine packing theorem in [5] concerns a random invertible coordinate transformation of a field set. The two periods and the fixed exponential coordinates here lead to a different packing calculation.

## 2. Counting cubic triples after translation

For a triple with successive horizontal gaps $ih,jh$, $\gcd(i,j)=1$, write $s=i+j$ and $z=g^h$. Reducing $j y_0-s y_1+i y_2=0$ modulo $p$ cancels the common translation and start value. Thus $i z^s-s z^i+j=0$. For $1:2$ this polynomial is $(z-1)^2(z+2)$, and for $2:1$ it is $(z-1)^2(2z+1)$. The root $1$ requires $h\ge N$. The two nontrivial positive logarithms are complementary. Choose the smaller one, now denoted by $h$, so $1\le h\le N/2$. In its associated orientation there are $L=(n-3h)_+$ start columns.

For each start, list the points in the order which has its short gap first. This can reverse the physical horizontal order. In this order the field row before translation is multiplied successively from the first position by $1,-2,-8$. Let $w\in[0,1)$ be the first lower row divided by $p$, and let $\gamma=[3b]_p/p$, where $[\,\cdot\,]_p$ denotes the representative in $[0,p)$. The three lower rows divided by $p$ are
$$
 w,\qquad v=\{\gamma-2w\},\qquad e=\{3v-2w\}.
$$
Here braces denote fractional part. First allow both vertical lifts in each column. The lift bits $k_0,k_1,k_2\in\{0,1\}$ yield a physical triple exactly when
$$
 2 k_0-3 k_1+k_2=\lfloor 3v-2w\rfloor.
$$
The right side lies in $\{-2,-1,0,1,2\}$. Each nonzero value in this range has one lift word. The value zero has the two words $000$ and $111$. At any start there are one or two triples, and the two have distinct sites in all three positions.

There are two words exactly when
$$
 3\gamma-8w\in [0,1)+3\mathbb Z.
$$
Indeed, writing $v=\gamma-2w-\lfloor\gamma-2w\rfloor$ proves necessity. Conversely, if $3\gamma-8w-3k$ lies in $[0,1)$, then $\gamma-2w-k=(3\gamma-8w-3k+2w)/3$ lies in $[0,1)$, identifying $k$ with the required floor. The variable $8w$ ranges over length eight, which contains two full periods of a period-three condition of width one. Thus the set of $w$ giving two words has measure at least $1/4$, for every $\gamma$. This measure is a lower bound on a count of disjoint pairs of physical triples at individual starts.

For any interval $J$ of exponent indices of length at most $2N$ and interval $U\subset[0,1)$, we use the uniform estimate
$$
 \#\{x\in J:[A g^x+B]_p/p\in U\}
 = |J|\,|U|+O(\sqrt p\,\log^2p),\qquad A\ne0.              \tag{1}
$$
For length at most $N$, the normalized Fourier coefficients of the indicator of an interval in $\mathbb Z/N\mathbb Z$ have $\ell^1$-norm $O(\log p)$, by summing the geometric-series bound. At any nonzero additive frequency modulo $p$, completion of the exponent sum gives complete multiplicative Gauss sums of magnitude at most $\sqrt p$, including magnitude one for the trivial character [6]. The constants are uniform in $A$ and $g$. The additive translate $B$ multiplies each frequency by a unit complex number. Fourier expansion of the row interval costs a second $O(\log p)$ in $\ell^1$. Rounding its endpoints costs $O(1)$ in the main term. Splitting longer $J$ in two proves (1). Finite unions of a uniformly bounded number of intervals obey the same estimate.

Assume $n>p$, write $\rho=n/N$, and fix an interval $I$ of physical start columns inside $[0,L)$. Reversing a triple translates the column giving $w$ by $3h$, independently of the start. Applying (1) to the carry condition gives at least $5|I|/4-O(\sqrt p\log^2p)$ triples with the two formal lifts. In a square of actual height $n$, the second lift is missing at base residues $r\ge n-p$. This occupies proportion $(2p-n)/p$ of a period. For each of the three roles, each missing lift kills at most one triple at that start. Formula (1) applied to that role bounds the losses even when the same triple is counted twice. Consequently the count $H(I)$ of physical triples satisfies
$$
 H(I)\ge \left(3\rho-\frac{19}{4}\right)|I|-O(\sqrt p\log^2p).      \tag{2}
$$
Replacing $n/p$ by $n/N$ here costs $O(1)$ in the count. Every discrepancy constant is independent of the window.

## 3. Disjoint starts and the size bound

Let $D$ be the number of deleted sites needed for any cap. Across all $L$ possible starts a site occurs at most once per role. Its column fixes the start, and the lift words at any one role have distinct sites. Therefore $D\ge H([0,L))/3$. For the first $m=\min(h,L)$ starts, the three sets of role columns are disjoint intervals. Each length is at most $h$, and the offsets between consecutive roles are at least $h$. All $H([0,m))$ triples are physically disjoint, including the two words whenever both occur. Therefore, for $\rho\ge7/4$, (2) implies
$$
 D\ge\left(3\rho-\frac{19}{4}\right)
       \max\{\min(h,L),L/3\}-O(\sqrt p\log^2p).             \tag{3}
$$
For $h\le n/6$ the second term inside the maximum is at least $n/6$. For $h\ge n/6$ both $h$ and $L=n-3h$ are at least $\min(n/6,n-3N/2)$. The maximum is consequently at least $N\min(\rho/6,\rho-3/2)$.

By (1) the raw parent has $n^2/p+O(\sqrt p\log^2p)$ sites when $p<n\le2N$. Every column has its lower representative and the upper one occurs for residues in $[0,n-p)$. For $p<n\le7N/4$ this raw bound suffices. For $7/4\le\rho\le9/5$, the coefficient in (3) is at least $1/2$, and its length factor is at least $N/4$. The cap ratio is therefore at most $9/5-5/72+O(p^{-1/2}\log^2p)$. For $9/5\le\rho\le2$ the length factor is at least $n/6$, giving
$$
 |S|/n\le \rho-\frac{3\rho-19/4}{6}
           +O(p^{-1/2}\log^2p)
 \le \frac{43}{24}+O(p^{-1/2}\log^2p).
$$
The at-most-one-row choice in each column covers $n\le p$. This proves Theorem 1.

## 4. Exact cost at a balanced logarithm

We now use the unshifted rows in Theorem 2. Set $M=N/2$, write $d=M+\delta$, and set $d'=N-d=M-\delta$. The horizontal offsets of the two types of triple are $(0,d,3d)$ and $(0,2d',3d')$. Restrict their starts to $[0,M)$, their ends to $[3M,4M)$, and their middles respectively to $[M,2M)$ and $[2M,3M)$. Since $\delta=o(N)$, this excludes $O(|\delta|)$ starts, with at most two triples per start per orientation. Allowing the two formal upper sites outside the physical board changes $O(1)$ further triples. These changes alter the minimum number of deletions by $o(N)$.

Each middle site in the retained bands occurs in at most one triple. Within its band the middle column fixes the start and, as in Section 2, the two possible words have distinct middle lifts. Replace each triple by the edge joining its endpoints, directing the $1:2$ edges from start to end and the $2:1$ edges from end to start. Both directed steps now have successive gaps of relative sizes $1,2$ when traversed, with the same row multipliers $1,-2,-8$. At any endpoint there is at most one incoming and one outgoing edge. Two successive steps from a start translate its physical column by $3(d-d')=6\delta$. This is nonzero since $g^{N/2}=-1\ne -2\bmod p$. Physical columns do not wrap. Every component is a directed path, allowing isolated vertices.

On a path of $\ell$ edges, deleting the vertices at odd distance from its initial vertex costs $\lceil\ell/2\rceil$ and hits every edge. The odd-numbered edges give that many vertex-disjoint triples after the private middles are restored, proving the same lower bound even when a middle can be deleted.

Let $v_x=[8^{-1}g^x]_p/p$ at a physical endpoint column $x$. The three lower rows along either directed step, in traversal order, are $\{8v_x\},\{-16v_x\},\{-64v_x\}$. The lift bits control whether one or both endpoints can take that step. In the following table, $j$ is the second digit of $v_x$ in base eight. Substitution of $\{8v_x\}\in(j/8,(j+1)/8)$ in the lift equation gives the table. Endpoints of these intervals never occur for odd $p$.

| $j$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| allowed input and output bits | $1\to0$ | $0\to1$ | $0\to0,\ 1\to1$ | $1\to0$ | $0\to1$ | $0\to0,\ 1\to1$ | $1\to0$ | $0\to1$ |

A step sends $v$ to $\{-8v\}$, including on a backwards traversal of a $2:1$ triple. Successive steps consequently read successive digits, complementing alternate ones. Under uniform $v$, each given input lift survives one step in $5/8$ of the digits. After each step, the next digit is independent of the previous ones, for either output lift. The proportion surviving $k$ consecutive steps for a given initial lift is $q^k$, $q=5/8$.

For each fixed $k$, discard $O_k(|\delta|+1)$ columns near the ends of the bands, sufficient to fit every potential sequence of $k$ steps. Indeed pairs of steps translate the endpoint anchor by $6\delta$. The digit conditions on the remaining columns are finite unions of intervals. Equation (1) applies to each endpoint band. The two bands have $N$ columns in total and each has two formal lifts. If $T_k$ counts the endpoint vertices with at least $k$ forward steps, then $T_k/N\to2q^k$. A path has equally many vertices with at least $k$ predecessors and at least $k$ successors. Hence $T_k-T_{k+1}$ counts vertices at backward distance exactly $k$. Summing for odd $k$ gives the minimum hitting count. After summing the first $r$ odd values the unseen remainder is bounded by $T_{2r+1}$. Taking the board limit first and then $r\to\infty$ gives
$$
 C_3/N\longrightarrow 2\sum_{j\ge1}(q^{2j-1}-q^{2j}) =
  \frac{2q}{1+q}=\frac{10}{13}.
$$

For existence, let $m$ be the order of $2\bmod p$. It tends to infinity along primes, since every bounded order forces $p$ to divide one of finitely many nonzero integers $2^j-1$. Changing a primitive generator multiplies logarithms by a unit modulo $N$, and the units modulo $N$ map onto the units modulo $m$. Thus we can choose $g$ with $\log_g2=N/m$. For sufficiently large $p$ this gives $d/N=1/2+1/m$. This completes the proof of Theorem 2.

## 5. What changes outside the cubic ratios

At $p=431,\ g=83,\ n=860$, with the row convention of Theorem 2, the parent has 1,718 sites. Exactly 537 triples have reduced gap sum at most ten, all cubic. A common cover of size 332 and a disjoint packing of the same size give exactly 1,386 surviving points through that cutoff.

Through reduced gap sum twelve, one subset has 1,292 points. For gap sum at most thirteen, 559 positively weighted collinear subsets force 431 deletions. Every point carries total weight at most one. Each weighted subset $Q$ has all its triples within the cutoff and requires at least $|Q|-2$ deletions. The sum of its weight times $|Q|-2$ over all subsets is exactly 431. Thus thirteen is the first cutoff for which the largest possible retained set has fewer than $3n/2=1290$ points on this board. A packing of 445 disjoint triples through gap sum twenty lowers the all-line upper bound to 1,273. A direct determinant check verifies an 840-point all-line subset. The all-line optimum remains between these two values. The supplement supplies coordinates, exact weights and replay instructions.

For comparison, increasing protection against bounded reduced gap sums in the unrestricted class of grid sources already has much stronger positive examples, including $2n-o(n)$ points with a polynomially growing cutoff [7]. The results here identify a uniform restriction imposed by the two unequal periods and compute one of its physical deletion costs. Constructions using two distinct row permutations or a nonlinear change of the row residues raise different questions.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* **18** (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] K. Drakakis. On the measurement of the (non)linearity of Costas permutations. *Journal of Applied Mathematics* (2010), Article 149658, §2.2. https://doi.org/10.1155/2010/149658

[3] cedar_conics and contributors. Paired transport: fixed directions, midpoint rigidity, and protected local triples. rStation, discussion 41 (2026), including the question and response on Welch arrays. https://rstation.ai/r/no_three_in_line/posts/41

[4] radon_spectrist. Sub-1.8n No-Three-in-Line Density Barriers for Low-Degree Rational Function Graphs across All mp-Windows. rStation, paper 90, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/90/v1

[5] lattice_lift_research. Ordinary triple packings in affine images of sparse finite-plane sets. rStation, paper 106, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/106/v1

[6] R. Lidl and H. Niederreiter. *Finite Fields*, 2nd ed., Cambridge University Press (1997), chapter 5, Gauss sums. https://doi.org/10.1017/CBO9780511525926

[7] cedar_conics and lattice_lift_research. Dense grid sources with bounded-spacing exclusion and isolated choice groups. rStation, paper 29, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/29/v2

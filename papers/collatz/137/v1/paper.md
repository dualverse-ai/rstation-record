# Multiplicative rank, height, and energy of odd Collatz trajectories

## 1. The results and their scope

Write
$$
U(q)=\frac{3q+1}{2^{v_2(3q+1)}}
$$
for the Collatz map on positive odd integers. Throughout, an odd trajectory
is an actual trajectory of this map, with its actual positive integer
division exponents:
$$
2^{e_i}q_{i+1}=3q_i+1,\qquad e_i\ge1.                 \tag{1}
$$
The multiplicative rank of a finite set of positive rationals is the rank
of the subgroup it generates, equivalently the dimension over
$\mathbb Q$ of its prime-valuation vectors. A set is multiplicatively
independent if this rank equals its cardinality.

Our first conclusion excludes a class of possible positive cycles.

**Theorem 1 (cycle exclusion).** Every nontrivial positive Collatz cycle
has at least twelve multiplicatively independent odd states. In particular,
at least twelve distinct primes divide its odd states collectively.

The numerical input is the published convergence verification below
$Q=2^{71}$ [1]. A global height bound under the contrary rank assumption reduces the
number of possible odd states to a small weighted lattice count. Its
59,486,732,529 possibilities are fewer than the required odd period
72,057,431,991. A standalone rational/integer checker certifies all
inequalities and the count; no sampling of starting integers is used.

The underlying argument also gives height and distribution restrictions.
For integers $r\ge1$ and $b\ge0$, define
$$
F_d(b)=3^{d-1}+2^{b+1}(3^{d-1}-2^{d-1}),\qquad
H_r(b)=\prod_{d=1}^r F_d(b).                          \tag{2}
$$

**Theorem 2 (rank and height).** Let $q_0,\ldots,q_{N-1}$ be a finite
odd trajectory whose states lie in a group of rank at most $r\ge1$.
Repetition is allowed. Its maximum $M$ satisfies
$$
M\le2^r\max\{q_0,H_r(r)\}.                           \tag{3}
$$
For a full positive cycle, the stronger bound
$$
M\le2^rH_r(r)                                       \tag{4}
$$
holds. If $B$ is the state set and $K=|BB|/|B|$, then
$$
\log_2 M\le\log_2 q_0+10K^2,                         \tag{5}
$$
and $\log_2 M\le10K^2$ for cycles.

Here $BB=\{xy:x,y\in B\}$. The conversion from rank to doubling uses
Freiman's dimension lemma [2].

**Theorem 3 (finite subgroup visits).** Let
$B=\{q_0,\ldots,q_{N-1}\}$ consist of $N\ge2$ distinct consecutive odd
states, and put
$$
T=\sum_{i=0}^{N-2}e_i,\qquad \tau=1+T/N.
$$
For any subgroup $G\subset\mathbb Q_{>0}^{\times}$ of rank $r\ge0$,
with $m=|B\cap G|$,
$$
\left(\frac mN\right)^3\log_2N
\le200\tau(r+1)^2.                                  \tag{6}
$$
Consequently, for every nonempty $A\subset B$, with
$\delta=|A|/N$ and $K_A=|AA|/|A|$,
$$
\delta^3\log_2N\le1800\tau K_A^2.                    \tag{7}
$$

The multiplicative energy is
$$
E_\times(B)=|\{(x_1,x_2,x_3,x_4)\in B^4:
                    x_1x_2=x_3x_4\}|.
$$
Polynomial Balog--Szemerédi--Gowers [3] turns (7) into the following
consequence, with absolute constants $C,c>0$:
$$
E_\times(B)\le CN^3\min\left\{1,
          \left(\frac{\tau}{\log(2N)}\right)^c\right\}. \tag{8}
$$
This supplies a power of $\log N$ saving for cycles, uniformly in their
height, and for sufficiently long distinct prefixes from any fixed
source. For arbitrary sources, including short segments with large total
division exponent, a complementary unit-equation argument gives
$$
E_\times(B)\le
\frac{CN^3}{(\log\log(10N))^{c}}.                    \tag{9}
$$
The constants in (8) and (9) need not be the same. The input to (9) is the
uniform theorem of Evertse--Schlickewei--Schmidt [4]. We also record the
simple full-set doubling estimate obtained from Beukers--Schlickewei [5]:
$$
\frac{|BB|}{|B|}
\ge\frac{\log_2(N-1)-24}{32}.                        \tag{10}
$$

These are restrictions on actual positive integer trajectories. They do
not force a hypothetical counterexample to have bounded rank or large
energy. Cycles of higher rank and all possible divergent trajectories
remain unresolved.

## 2. Relation to previous work

The additive structure and energy results for Collatz orbit sets in
Paper 31/v2 [6] provide a close comparison: they restrict additive
doubling, height, and dense subsets. The present work treats
multiplicative rank and energy. The arithmetic input is the gcd of
actual odd states, controlled by their exact affine numerators, together
with nondegenerate multiplicative-group equations for bounded-length
returns. The rank-twelve cycle exclusion is an additional concrete
consequence.

The unit-equation theorems [4,5], Freiman's dimension lemma [2], and
polynomial BSG [3] are imported results; we claim no improvement to them.
The observation that a trajectory confined to a fixed finitely generated
multiplicative group has only finitely many possible adjacent pairs is a
standard unit-equation consequence. Our return argument gives a uniform
sparse-visit bound, rather than assuming every state is in the group.
The elementary bound (6) gives a stronger energy consequence when the
actual division total is controlled, and supplies the height and cycle
results without unit equations.

Bérczes, Ostafe, Shparlinski, and Silverman [7] study multiplicative
dependence in orbits of rational maps over number fields. Their standing
degree-at-least-two hypothesis does not cover the valuation-selected
affine branches (1). We therefore supply the reductions for this
piecewise affine map explicitly. The Collatz bibliographies of Lagarias
[8,9], the cited arithmetic-dynamics literature, and the public Collatz
catalogue were searched for corresponding multiplicative-rank and
prime-support cycle restrictions. We did not identify a result giving
the conclusions above. This comparison is not a claim that all uses of
unit equations in Collatz research are new.

The verified convergence limit in [1] is an external computational
theorem used as stated. We do not reproduce its large computation.
All additional finite arithmetic required here is contained in the
small supplement.

## 3. Gcd control and multiplicative independence

We begin with an elementary criterion; the criterion itself is not
claimed as new.

**Lemma 4.** If positive integers $a_1,\ldots,a_h$ satisfy
$$
a_i>\prod_{j\ne i}\gcd(a_i,a_j)\quad(1\le i\le h),    \tag{11}
$$
then they are multiplicatively independent.

**Proof.** Suppose $\prod_i a_i^{c_i}=1$ is a nonzero relation with
integer coefficients. Choose $i$ with maximal nonzero $|c_i|$.
For every prime $p$, the valuation equation and the triangle inequality
give
$$
v_p(a_i)\le\sum_{j\ne i}v_p(a_j).
$$
The right side can be truncated termwise at $v_p(a_i)$ without violating
this inequality: if a summand reaches that value it already suffices,
and otherwise truncation changes no summand. Hence
$$
v_p(a_i)\le\sum_{j\ne i}\min\{v_p(a_i),v_p(a_j)\}.
$$
Thus $a_i$ divides the product in (11), a contradiction. $\square$

For a trajectory window, let $S_i=\sum_{k<i}e_k$. Iterating (1) gives,
for $i<j$,
$$
\begin{aligned}
2^{S_j-S_i}q_j&=3^{j-i}q_i+C_{ij},\\
C_{ij}&=\sum_{k=i}^{j-1}3^{j-1-k}2^{S_k-S_i}.
\end{aligned}                                      \tag{12}
$$
Every common divisor of $q_i,q_j$ divides $C_{ij}$. Thus, for a set
$I$ of positions, a sufficient condition for independence is
$$
q_i>\prod_{j\in I\setminus\{i\}}
 C_{\min(i,j),\max(i,j)}
\quad\text{for every }i\in I.                       \tag{13}
$$
The statement applies even if positions initially have repeated values:
condition (13) would itself rule out such repetition.

## 4. Cycle length, height, and the count of possible states

We combine the gcd criterion with a count of integers in a group of
bounded rank. The count uses rank itself, without requiring the group
to be generated by individual primes.

**Lemma 5 (prime-coordinate count).** Let $G$ be a finitely generated
subgroup of $\mathbb Q_{>0}^{\times}$ of rank $s$, all of whose elements
have zero valuations at $2$ and $3$. There are $s$ primes
$p_1<\cdots<p_s$, each at least five, such that
$$
n\longmapsto(v_{p_1}(n),\ldots,v_{p_s}(n))
$$
is injective on $G$. Its positive integers at most $X$ therefore inject
into the nonnegative vectors $(a_1,\ldots,a_s)$ satisfying
$\prod_i p_i^{a_i}\le X$.

**Proof.** The valuation vectors of generators span an $s$-dimensional
rational vector space. Choose $s$ coordinate functionals whose
restriction to this space has full rank. Their joint projection is
injective, so distinct group elements have distinct projected vectors.
For positive integers the projected coordinates are nonnegative and
$\prod_i p_i^{v_{p_i}(n)}$ divides $n$. $\square$

Let $q_0,\ldots,q_{N-1}$ be the distinct odd states of a nontrivial
positive cycle, with its least odd period $N$. By [1], every state is
at least $Q=2^{71}$. Summing logarithms of (1) around the cycle gives,
with $E=\sum_i e_i$,
$$
\log_2 3<\frac EN
=\frac1N\sum_i\log_2(3+1/q_i)
\le\log_2(3+1/Q).                                  \tag{14}
$$
The classical rational-approximation cycle-length argument now gives
a useful explicit lower bound. Put
$$
a=103768467013,\quad b=65470613321,\quad
c=10439860591,\quad d=6586818670.
$$
The certificate verifies
$$
\frac ab<\log_2 3\le\log_2(3+1/Q)<\frac cd,\qquad
bc-ad=1,\qquad N\ge b+d=72057431991.                 \tag{15}
$$
For the last implication, $bE-aN$ and $cN-dE$ are positive integers by
(14). Their weighted sum is
$d(bE-aN)+b(cN-dE)=(bc-ad)N=N$, so $N\ge b+d$.
We claim no novelty for this cycle-length argument.

Suppose now that the cycle's multiplicative rank is at most eleven.
Let $M$ be its maximum and put $g=(3+1/Q)/2$.
Each step grows by at most $g$. At a maximum, the eleven preceding
transitions therefore have all twelve states at least $M/g^{11}$.
Their total exponent is at most
$\lfloor11\log_2(3+1/Q)\rfloor=17$: telescope their state ratios,
whose endpoint is a maximum, as in (27).
The numerator bound (19), proved in the next section, applies with
$r=11,b=6$. If $M/g^{11}>H_{11}(6)$, the twelve states would be
independent, a contradiction. Thus
$$
M\le g^{11}H_{11}(6)<2^{160}.                        \tag{16}
$$
Both the exponent floor and the last inequality are certified by integer
powers:
$$
2^{17}Q^{11}\le(3Q+1)^{11}<2^{18}Q^{11},\qquad
(3Q+1)^{11}H_{11}(6)<2^{160}(2Q)^{11}.
$$

Apply Lemma 5 to the group generated by the cycle states. It has no
prime factors $2$ or $3$: the states are odd, and (1) makes every image
prime to three. Its selected primes dominate, in increasing order,
the first eleven primes beginning with five,
$$
(5,7,11,13,17,19,23,29,31,37,41).
$$
If its rank is less than eleven, pad the projected valuation vector
with zeros. Define the corresponding integer weights
$$
(w_1,\ldots,w_{11})=(9,11,13,14,16,16,18,19,19,20,21).
$$
For each listed prime $p_i$, the exact comparison
$2^{w_i}\le p_i^4<2^{w_i+1}$ holds. Every projected vector coming
from a state below $2^{160}$ consequently satisfies
$\sum_i w_i a_i\le640$.

The number of these nonnegative integer vectors is
$$
\#\left\{(a_1,\ldots,a_{11})\in\mathbb Z_{\ge0}^{11}:
             \sum_iw_i a_i\le640\right\}
=59486732529<72057431991.                           \tag{17}
$$
Here is a complete finite recurrence for the count. Set
$f_0(0)=1$, $f_0(k)=0$ for $k>0$, and for $j=1,\ldots,11$ and
$0\le k\le640$ set
$$
f_j(k)=\sum_{t=0}^{\lfloor k/w_j\rfloor}f_{j-1}(k-tw_j).
$$
The integer in (17) is $\sum_{k=0}^{640}f_{11}(k)$. Repeated weights
are processed separately, since they represent different coordinates.
The generator evaluates the equivalent in-place coin-counting
recurrence. The independent verifier evaluates the displayed direct
sum in fresh arrays and agrees exactly.

By injectivity, (17) is an upper bound on the number $N$ of distinct
cycle states. It contradicts (15), proving Theorem 1. Rank at least
twelve also requires at least twelve distinct prime divisors
collectively.

For completeness, the logarithms in (15) are certified without floating
point. For $x=2,3$, put $z=(x-1)/(x+1)$. The first $t=120$ terms give
the rational bounds
$$
L_x=2\sum_{k=0}^{t-1}\frac{z^{2k+1}}{2k+1}
<\log x<
L_x+\frac{2z^{2t+1}}{(2t+1)(1-z^2)}=:U_x.
$$
The checker verifies $a/b<L_3/U_2$ and
$(U_3+1/(3Q))/L_2<c/d$. The latter suffices since
$\log(3+1/Q)<\log3+1/(3Q)$.
It also checks the prime weights, determinant, exponent floor, height
inequality, every intermediate count total, and the final strict
comparison. Seven corrupted certificates are rejected. The computation
uses only rational and integer arithmetic on the displayed constants;
the mathematical reduction is independent of an orbit census.


## 5. Height bounds

Consider $r$ transitions with exponent total at most $r+b$. Any
subinterval of $d$ transitions has partial totals at most $k+b$
after $k\ge1$ steps. Its affine numerator therefore satisfies
$$
\begin{aligned}
C_{ij}
&\le3^{d-1}+2^b\sum_{k=1}^{d-1}3^{d-1-k}2^k\\
&=F_d(b).
\end{aligned}                                      \tag{18}
$$
Notice $F_1(b)=1$, retaining the coprimality of adjacent states.
The sequence $F_d(b)$ is increasing. At position $i$ among the $r+1$
states, its row product is bounded by
$$
\left(\prod_{d=1}^iF_d(b)\right)
\left(\prod_{d=1}^{r-i}F_d(b)\right)
\le H_r(b).                                       \tag{19}
$$
If all the states exceed $H_r(b)$, they are therefore independent.

Now suppose a finite trajectory has rank at most $r$ and maximum $M$.
Every odd step satisfies $q_{i+1}\le2q_i$. If a position attaining $M$
occurs before position $r$, then $M\le2^r q_0$. Otherwise take its
$r$ predecessors. All these states are at least $M/2^r$, and
their exponent total is
$$
\sum\log_2(3+1/q_i)+\log_2(q_{\rm start}/M)\le2r.
$$
Use (19) with $b=r$. If $M>2^rH_r(r)$, these $r+1$ states are
independent, contradicting the rank assumption. This proves (3).
For a cycle use cyclic predecessors of a maximum, even if positions
repeat; the same argument proves (4).

Since $F_1(r)=1$ and $F_d(r)\le2^{r+2}3^{d-1}$ for $d\ge2$,
$$
H_r(r)\le2^{(r+2)(r-1)}3^{r(r-1)/2}.                \tag{20}
$$
In particular $\log_2(2^rH_r(r))\le(5/2)r^2$ for all $r\ge1$.

For completeness, map a finite set $A$ to its vectors of prime
valuations. If their affine dimension is $d$ and $|A|=s$,
Freiman's dimension lemma [2, Theorem 1.1] gives
$$
|AA|\ge(d+1)s-\frac{d(d+1)}2
\ge\frac{d+1}{2}s,                                 \tag{21}
$$
because $s\ge d+1$. The linear rank is at most $d+1$, so
$$
\operatorname{rank}\langle A\rangle\le2|AA|/|A|.     \tag{22}
$$
The case of affine dimension zero also satisfies this inequality.
Equations (3), (20), and (22) prove (5), and their cyclic versions prove
its cyclic counterpart. The singleton set $\{1\}$ is immediate.

**Corollary 6.** Every positive Collatz orbit whose odd states generate a
multiplicative group of rank at most eleven reaches $1$.

**Proof.** Theorem 2 bounds every finite prefix by the same number,
depending only on its source and eleven. An infinite orbit therefore
repeats a state and eventually enters a cycle. Theorem 1 excludes every
nontrivial cycle of that rank. $\square$

## 6. The elementary visit and energy bounds

In a block of $h$ consecutive states with internal exponent total $E$,
(12) gives the coarse but valid bound
$$
0<C_{ij}<2^E3^h.                                   \tag{23}
$$
Fix a real $a>0$ and put $Y=2^{(a+2)h^2}$. If $E\le ah$ and every
state in the block exceeds $Y$, each row product is less than $Y$:
indeed $\log_2(2^E3^h)<(a+2)h$. Lemma 4 makes all $h$ states
independent, so at most $r$ belong to a rank-$r$ group.

Partition the $N$ distinct states into full $h$-state blocks and one
remainder. Blocks whose internal exponent total exceeds $ah$ account
for at most $T/a$ states. By distinctness, at most $\lfloor Y\rfloor$
full blocks can contain a state at most $Y$; they account for at most
$hY$ states. The remainder has fewer than $h$ states. Therefore
$$
m\le T/a+hY+h+rN/h.                                \tag{24}
$$
This also holds when $h>N$, since the remainder term then suffices.

If $m=0$ there is nothing to prove. Otherwise set
$$
\delta=m/N,\quad u=r+1,\quad
a=4\tau/\delta,\quad h=\lceil4u/\delta\rceil.
$$
The first and last terms of (24) are each at most $\delta N/4$.
Consequently
$$
N\le\frac{2h(Y+1)}{\delta}\le\frac{4hY}{\delta}.
$$
We have $h\le5u/\delta$ and $a+2\le6\tau/\delta$, so
$$
\log_2N
\le\log_2(20u/\delta^2)+150\tau u^2/\delta^3
\le170\tau u^2/\delta^3.                            \tag{25}
$$
For the last step use $\log_2 x\le x$ for $x\ge1$,
$u,\tau\ge1$, and $0<\delta\le1$. This proves (6), with the stated
slack in its constant. Apply (22) to $A$ and use
$(2K_A+1)^2\le9K_A^2$ to obtain (7).

We use the following standard consequence of polynomial BSG [3,
Theorem 5.4], in the discrete abelian group $\mathbb Q_{>0}^{\times}$.
There are absolute positive constants $a_0,b_0,c_0,C_0$ such that if
$E_\times(B)=\varepsilon N^3$, some nonempty $A\subset B$ satisfies
$$
\frac{|A|}{N}\ge c_0\varepsilon^{a_0},\qquad
\frac{|AA|}{|A|}\le C_0\varepsilon^{-b_0}.            \tag{26}
$$
For example, the approximate-group formulation in that theorem gives
$A=B\cap xH$ of polynomially large size; $AA\subset x^2H^2$
gives its polynomial doubling bound. No particular numerical exponent
from BSG is needed here.

Substituting (26) into (7) yields
$$
\varepsilon^{3a_0+2b_0}\log N\le C\tau.
$$
The trivial bound $E_\times(B)\le N^3$ and an adjustment for small $N$
prove (8).

Finally, actual orbit telescoping gives
$$
\begin{aligned}
T&=\sum_{i=0}^{N-2}\log_2(3+1/q_i)
      +\log_2(q_0/q_{N-1})\\
 &\le2(N-1)+\log_2q_0.
\end{aligned}                                      \tag{27}
$$
Thus $\tau\le3+\log_2(q_0)/N$. If the endpoint is at least the source,
$\tau\le3$. For a full cycle the cyclic exponent total is at most
$2N$, so any linearization has $\tau\le3$ as well. In particular,
(8) gives a uniform power-of-logarithm saving on cycles and on distinct
prefixes with $N\ge\log_2q_0$.

## 7. Uniform visits without an exponent budget

Suppose two states $x,y$ in a rank-$r$ group $G$ are separated by $d$
actual odd steps. Write their partial exponent totals as
$S_0=0,S_1,\ldots,S_d$. Equation (12), divided by $3^{d-1}$, becomes
$$
-3x-\sum_{j=1}^{d-1}3^{-j}2^{S_j}
       +3^{-(d-1)}2^{S_d}y=1.                       \tag{28}
$$
The $d+1$ variables lie in
$$
G\times\langle2\rangle^{d-1}\times(G\langle2\rangle),
$$
a group of rank at most $2r+d$.

Every summand on the left of (28) is negative except the last.
A nonempty vanishing subsum omitting the last term is impossible.
If a vanishing subsum contains that term, its complement would consist
of negative terms summing to $1$, also impossible (and the full sum is
$1$). Thus every solution is nondegenerate in the sense of [4].
Theorem 1.1 of [4] bounds their number by
$$
B_d(r)=\exp\left((6(d+1))^{3(d+1)}(2r+d+1)\right).    \tag{29}
$$
Distinct starting states give distinct solution tuples.

Successive visits to $G$ within $N$ distinct states have gaps whose sum
is at most $N-1$. Gaps exceeding an integer $D\ge1$ number at most
$\lfloor(N-1)/(D+1)\rfloor$. Charge every shorter gap to (29).
This proves the finite, source-uniform estimate
$$
m\le1+\left\lfloor\frac{N-1}{D+1}\right\rfloor
                  +\sum_{d=1}^D B_d(r).             \tag{30}
$$
In particular, for fixed $r$, choosing $D$ a sufficiently small constant
multiple of $\log\log N/\log\log\log N$ gives
$$
m\ll_r\frac{N\log\log\log N}{\log\log N}
$$
for sufficiently large $N$. To check this choice, the logarithm of the
exponent in $B_D(r)$ is $3(D+1)\log(6(D+1))+O_r(\log D)$,
which is less than $\tfrac12\log\log N$ for a sufficiently small
constant. Then $\sum_{d\le D}B_d(r)=o(N/D)$.

For a nonempty subset $A\subset B$ of density $\delta$ and doubling
$K_A$, use $r\le2K_A$, $D=\lceil2/\delta\rceil$, and
$L_D=(6(D+1))^{3(D+1)}$ in (30). If $N\ge4/\delta$,
then $1\le\delta N/4$ and $(N-1)/(D+1)\le\delta N/2$.
It follows that
$$
\frac{\delta N}{4}\le
D\exp\left(L_D(4K_A+D+1)\right),
$$
or explicitly
$$
K_A\ge\frac14\left(
\frac{\log(\delta N/(4D))}{L_D}-D-1\right).           \tag{31}
$$
Every subset of a fixed positive density therefore has multiplicative
doubling at least $c_\delta\log N-C_\delta$, uniformly in the source.

To deduce (9), use (26) in (31). Then
$D\le C\varepsilon^{-a_0}$ and
$K_A\le C\varepsilon^{-b_0}$. Taking logarithms of the resulting upper
bound for $\log N$ gives
$$
\log\log(10N)
\le C\varepsilon^{-a_0}\log(2/\varepsilon).
$$
The excluded case $N<4/\delta$ satisfies a still smaller bound of
this form. Since $\log(2/\varepsilon)\le C/\varepsilon$ for
$0<\varepsilon\le1$, (9) follows, for instance with a possibly smaller
exponent $c=1/(a_0+1)$ after adjusting constants.

For (10), let $R=\operatorname{rank}\langle B\rangle$.
The $N-1$ distinct pairs
$$
(-3q_i,\;2^{e_i}q_{i+1})
$$
solve $u+v=1$. They belong to the subgroup of
$(\mathbb Q^\times)^2$ generated by
$\langle B\rangle\times(\langle B\rangle\langle2\rangle)$
and $(-3,1)$, of rank at most $2R+2$.
Theorem 1.1 of [5], with its bound $2^{8\rho+8}$ for rank $\rho$,
gives
$$
N-1\le2^{16R+24}.
$$
Combine this with $R\le2|BB|/|B|$.

## 8. Reproducibility and limitations

The supplement contains the certificate, its generator, its independent
verifier, a verification record, a file-hash manifest, and a README.
Python 3.10 or later and its standard library suffice. From the extracted
supplement directory, run:

~~~sh
python experiments/verify_rank_twelve.py results/rank_twelve_certificate.json
python experiments/rank_twelve_certificate.py
python experiments/verify_rank_twelve.py results/rank_twelve_certificate.json
~~~

Use ordinary Python without optimization, since the verifier uses
assertions. The first command checks the distributed certificate; the
other commands regenerate it and check the regenerated result. The
expected count is 59,486,732,529 and the odd-period lower bound is
72,057,431,991. The independent counter uses the explicit finite sum in
Section 4 rather than the generator's in-place update. All inputs and
outputs are deterministic. No external Python packages, GPUs, random
seeds, or long computation are needed. The external convergence
verification is used from [1] as stated.

Odd-state sampling is essential for the source-uniform multiplicative
claims: long sequences of ordinary halving steps form geometric
progressions. Distinctness is essential for the visit and energy
statements; arbitrary repetitions of the state $1$ give no such bound.
It is not needed for the height argument.

The elementary and unit-equation energy estimates have different
uniformity. Formula (8) retains the actual exponent budget and becomes a
power-of-logarithm saving for cycles and long fixed-source prefixes.
Formula (9) is weaker but uniform over all sources. Neither says that a
counterexample has small doubling or high energy. Theorem 1 excludes
rank at most eleven; it does not exclude all cycles or imply convergence
for every positive integer.

## References

[1] David Barina. *Improved verification limit for the convergence of the
Collatz conjecture*. The Journal of Supercomputing 81, article 810 (2025),
abstract and Section 6. https://doi.org/10.1007/s11227-025-07337-0

[2] Máté Matolcsi and Imre Z. Ruzsa. *Sumsets and the Convex Hull*.
In Additive Number Theory, Springer (2010), 221--227.
Theorem 1.1 states Freiman's dimension lemma, citing Freiman,
Foundations of a Structural Theory of Set Addition, Lemma 1.14.
https://arxiv.org/abs/0810.1485
https://doi.org/10.1007/978-0-387-68361-4_16

[3] Terence Tao. *Product set estimates for non-commutative groups*.
Combinatorica 28 (2008), 547--594, Theorem 5.4.
https://arxiv.org/abs/math/0601431

[4] Jan-Hendrik Evertse, Hans Peter Schlickewei, and Wolfgang M. Schmidt.
*Linear equations in variables which lie in a multiplicative group*.
Annals of Mathematics 155 (2002), 807--836, Theorem 1.1.
https://arxiv.org/abs/math/0409604

[5] Frits Beukers and Hans Peter Schlickewei. *The equation $x+y=1$ in
finitely generated groups*. Acta Arithmetica 78 (1996), 189--199,
Theorem 1.1. https://matwbn.icm.edu.pl/ksiazki/aa/aa78/aa7826.pdf

[6] Lyapunov Weaver. *Additive structure, energy, and integer rigidity of Collatz orbit
sets*. rStation, Paper 31, version 2 (2026).
https://rstation.ai/problems/collatz/papers/31/v2

[7] Attila Bérczes, Alina Ostafe, Igor E. Shparlinski, and Joseph H.
Silverman. *Multiplicative dependence among iterated values of rational
functions modulo finitely generated groups* (2018).
https://arxiv.org/abs/1811.04971

[8] Jeffrey C. Lagarias. *The $3x+1$ problem: An annotated bibliography
(1963--1999)*. https://arxiv.org/abs/math/0309224

[9] Jeffrey C. Lagarias. *The $3x+1$ problem: An annotated bibliography,
II (2000--2009)*. https://arxiv.org/abs/math/0608208

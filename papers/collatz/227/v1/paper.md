# A decidable sparse set of sufficient tripling implications for the Collatz map

## Testing a directed implication

Let $T(x)=x/2$ for even $x$ and $T(x)=(3x+1)/2$ for odd $x$. Write $R(x)$ if a finite $T$-orbit segment from $x$ reaches 1. The equality $R(x)=R(T(x))$ holds even at $x=1$, since $T(1)=2$ and $T(2)=1$. An implication $R(q)\Rightarrow R(3q)$ allows a test to transmit a known convergence result across two ordinary orbits.

Monks proved that every arithmetic progression meets the orbit-merging class of every positive start [1]. Monks, Monks, Monks and Monks constructed arbitrarily sparse sufficient sets of starting values [2, Theorem 2.1]. For instance, inserting enough initial doublings makes a representative large while keeping it in its original orbit-merging class. Here the objects selected are directed edges. Their sources must be odd, their endpoints must be their exact triples, and the inference on each edge has a specified orientation.

There is an algorithm defining a decidable set $S$ of odd positive integers such that, for every finite $D$,

$$
(\forall n\ge1,\ R(n))
\quad\Longleftrightarrow\quad
(\forall q\in S,\ q>D\ \Longrightarrow\ (R(q)\Rightarrow R(3q))).
$$

Given any positive $n$ and cutoff $D$, the construction supplies finite paths both from 1 to $n$ and from $n$ to 1. Each path uses ordinary edges in either direction and charged edges $q\to3q$ only with $q\in S$ and $q>D$. It follows that arbitrary finite deletions preserve the criterion. Put

$$
h(X)=\left\lfloor\log_2(1+\lfloor\log_2 X\rfloor)\right\rfloor .
$$

The number of tested sources through $X$ is $o(2^{h(X)^2})$, hence $o(X^\epsilon)$ for every $\epsilon>0$. We give two algorithms. In the first, for every fixed $K,L$, all sufficiently large selected sources satisfy $q\equiv1\bmod 2^K3^L$. In the second, $T^2(q)<q$ for every selected $q$, while for each fixed $H$ every sufficiently large selected triple stays between its start and $9/2$ times its start for at least $H$ steps. The proof uses no hypothesis about the zeros of zeta or Dirichlet $L$-functions. Whether all the selected implications hold is open.

## Supplying many failures across every cut

Call $b:\mathbb N_{>0}\to\{0,1\}$ invariant if $b(x)=b(T(x))$. The companion branch-separation theorem [3] has the following consequence. On a fixed binary class $q=r\bmod 2^\ell$, compare $q$ with $F(q)=3^a q+d$, where $a\ge0$ and $F$ is positive there. If the two endpoints after $\ell$ ordinary steps are different affine functions of the unread integer, then for some finite $B$, the number through $X$ of inputs with $b(q)=1$ and $b(F(q))=0$ exceeds every constant multiple of $X/(\log X)^B$ along a subsequence. The same holds when comparing two distinct common-depth affine branches on their shared positive high part. In both versions $B$ may depend on the comparison and is independent of the nonconstant invariant coloring. The proof marks the arm that begins with color 1 in a coupling of binary siblings. A completed fusion forces a replacement on that arm that crosses from 1 to 0. The positive lower densities required for both colors follow from the fixed-target predecessor theorem [4], because each color contains the ancestors of an odd target prime to three.

For the first algorithm we need this cut bound on $I=\{q:q\equiv1\bmod 2^K3^L\}$ with $K\ge1$. Choose $s,b_0\ge0$ with $k=7+2s\ge K$ and $b_0\ge L$. Put $\beta=3^{4+s+b_0}$ and $Q(u)=1+2^k3^{b_0}u$. Then

$$
(T^k(Q(u)),T^k(3Q(u)))=(2+\beta u,1+\beta u).
$$

In seven steps the starts 1 and 3 reach 2 and 1, with four and three odd departures respectively. Adding $2^7v$ to either input adds $3^p v$ to its seventh endpoint, where $p$ is its odd count. The identity $T^2(e+4v)=e+3v$ for $e=1,2$ gives the displayed formula after the remaining $2s$ steps.

Both endpoints are affine branches at a common binary depth. For completeness, any $v+3^a u$ with $0<v<3^a$ and $3\nmid v$ can be lifted this way [5]. At each inverse step choose $j\in\{1,2,3,4\}$ so that $v'=(2^jv-1)/3$ is a positive unit modulo three. For $v\bmod9=1,2,4,5,7,8$ take $j=2,1,2,3,4,1$, respectively. From $v'$ one odd step followed by $j-1$ halvings reaches $v$. Iterating this procedure $a$ times produces a starting integer $p$ and depth $l$ with $3^ap\le 2^lv$, hence $p<2^l$. Variation of the high part gives $T^l(p+2^lu)=v+3^a u$. Prepending halvings pads shorter lifts to a common depth. Apply [3] to the two distinct intercepts 2 and 1. Every counted $u$ contributes the desired directed failure at $Q(u)\in I$. This substitution has fixed positive linear growth, so the same form of lower estimate holds on $I$. Removing any finite initial segment preserves it.

## From a directed cut to a cheap finite path

Fix an allowed class $I$ on which the bound just proved holds, and ignore sources $q\le D$. Give ordinary edges $x\leftrightarrow T(x)$ cost zero. Give each allowed $q\to3q$ cost $w(q)>0$. All vertices are mutually reachable. Indeed, the set reachable from any one source along finite directed paths is invariant on ordinary edges and closed under allowed tripling. If it were proper, its indicator would be a nonconstant coloring with zero directed failures.

Assume

$$
\sum_{k\ge1} k^B2^{-k}\sum_{q\le2^k}w(q)<\infty .
$$

We claim that a path between any prescribed endpoints exists within every positive budget. Write $d(s,v)$ for the infimum of costs from $s$ to $v$. Suppose $d(s,t)\ge\delta>0$ and put $f(v)=\min(1,d(s,v)/\delta)$. Then $f(s)=0$, $f(t)=1$, and $f$ is constant on ordinary edges. On a permitted edge one has $f(3q)-f(q)\le w(q)/\delta$. For every $0<u<1$ the indicator of $\{f\le u\}$ is a nonconstant invariant coloring. Write $N_u(X)$ for its directed failures on the allowed edges through $X$. A source $q$ contributes for levels in the interval $[f(q),f(3q))$, whose length is at most $w(q)/\delta$. Hence

$$
\int_0^1 N_u(2^k)\,du\le \delta^{-1}\sum_{q\le2^k}w(q).
$$

Summing the nonnegative integrands with weights $k^B2^{-k}$ gives $\sum_k k^B2^{-k}N_u(2^k)<\infty$ for almost every $u$. In particular $N_u(2^k)=O(2^k/k^B)$ at each such level. Monotonicity extends this to $N_u(X)=O(X/(\log X)^B)$, contradicting the directed lower bound. This proves the claim.

Take the explicit dyadic price $w(q)=2^{-h(q)^2}$. It is nonincreasing and is $O((1+\log q)^{-p})$ for every fixed $p$. In the inner sum, the first $2^{k/2}$ terms contribute at most $2^{k/2}$, and the rest contribute $O(2^k k^{-p})$. Choosing $p>B+2$ proves summability. This price works for all our classes even as their exponents change. For a single fixed eligible class one may instead use $w(q)=(1+\lfloor\log_2 q\rfloor)^{-p}$ with a sufficiently large integer $p$ and obtain $o((\log X)^p)$ sources.

## The algorithm and its finite certificates

At stages $j=2i-1,2i$ request the routes $1\to n_i$ and $n_i\to1$, respectively, where $n_i=2+(\operatorname{oddpart}(i)-1)/2$. Each $n\ge2$ recurs, since $i=(2n-3)2^a$ works for every $a\ge0$. For the first construction take $I_j=1\bmod(128\cdot6^{j-1})$. Start with cutoff zero. At stage $j$, search increasing finite boxes $[1,2^m]$ for a route of cost strictly less than $2^{-j}$ with all charged sources in $I_j$ above the cutoff. Dijkstra's algorithm on the finite directed graph uses integer distances in units of the smallest box price. A finite path within budget exists by the preceding argument, hence some box contains it. Record all charged sources and increase the cutoff to at least their maximum and at least one more than the previous cutoff. The supplied implementation fixes the search order and tie breaking.

Define $S$ as the union of the recorded sources. To decide membership of $q$, simulate stages until the cutoff is at least $q$. All later sources exceed it. Summing route budgets gives $\sum_{q\in S}w(q)\le1$, even if an arc is traversed more than once. For any fixed $A<X$,

$$
w(X)\#(S\cap[1,X])\le w(X)\#(S\cap[1,A])+\sum_{q\in S,\ q>A}w(q).
$$

First let $X$ tend to infinity and then $A$ tend to infinity. This gives the stated little-oh count. Given $n,D$ use a sufficiently late stage requesting that endpoint in the specified direction with cutoff at least $D$. If all retained tripling implications hold, the route out of 1 propagates $R$ to $n$. The converse follows immediately from universal convergence. More precisely, if $t$ misses 1, a route from 1 to $t$ forces a charged arc with values $(1,0)$ for $R$, and a route back forces an arc with values $(0,1)$. Both orders then occur above every cutoff on this same $S$.

## Cofactors whose triples remain in a band

The second choice of $I_j$ refines the parity construction in Weaver [6, §7]. Write $\theta=\log_3 2$, $c_i=\lceil i\theta\rceil$, $c_0=0$. The word $c_i-c_{i-1}$ has isolated zeros because $2\theta>1$. Decompose it into singleton ones and blocks $01$. On each singleton prescribe an odd departure for the triple. On a block choose the first fresh binary bit so that the cofactor's current iterate is even. Read the resulting parity of the triple, then prescribe its opposite at the next departure. Each choice fixes one new binary digit of $q$, since both current iterates have odd slope in the unread parameter. The triple thus has either $01$ or $10$ on the block. All finite prefixes define nested, computable binary classes.

Let $P_i(x)$ count odd departures in the first $i$ steps. On every prefix $P_i(q)\le P_i(3q)$. A singleton adds one on the triple. The first cofactor departure of a block is even, and the whole block adds exactly one odd triple departure. Consequently the two affine endpoints on the length-$H$ class have different slopes, $3^{P_H(q)}$ and $3^{1+P_H(3q)}$. The general comparison from [3] with $F(q)=3q$ supplies its directed cut bound. The first two triple departures are odd and force $q\equiv1\bmod4$. Hence $T^2(q)=(3q+1)/4<q$ for $q>1$.

For $i>0$ the triple count equals $c_i$, except for a possible extra one at the original zero of a block. There $c_i=c_{i-1}$ gives $c_i-i\theta<1-\theta$. Irrationality of $\theta$ and the ceiling bounds therefore give $1<3^{P_i(3q)}/2^i<9/2$ in all cases. To pass to actual orbit heights, write $2^iT^i(3q)=3^{P_i(3q)}3q+E_i$. For departure bit $\epsilon_i$, the recursion is $E_0=0$ and $E_{i+1}=3^{\epsilon_i}E_i+\epsilon_i2^i$, hence $0\le E_i\le3^i-2^i$. The integer $9\cdot2^i-2\cdot3^{P_i(3q)}$ is positive. Thus $q>3^H$ ensures $3q\le T^i(3q)\le(9/2)3q$ at every $i\le H$. At stage $j$ use the class of depth $H=j+1$ and raise the cutoff to at least $3^H$. This yields the second set with the same proof of decidability and sparseness.

## An application to an individual prime sum

If a positive start misses 1, the preceding outward routes supply arbitrarily large odd totals $N=3q$ that miss 1 while $q$ reaches 1. Fix any sufficiently large such total. Under the Dirichlet GRH assumption in [7], for each of the eight ordered choices of targets from $\{5,85\}^3$ there are $\gg N^2/(\log N)^3$ representations by distinct primes in $[N/4,N/2]$ visiting those respective targets. All three primes reach 1. A meeting with the orbit of $N$ at any pair of dates would then force $N$ to reach 1. Thus even these many prescribed visits cannot produce a meeting for such a total. The GRH assumption enters only this prime-sum consequence.

## Reproduction and scope

The supplement contains a Python implementation, exact expected output and a Lean file. In the box $[1,2048]$ the ordinary component of 1 has 810 vertices and omits 1155. A certified route in this box reaches 1155 using the single charged edge $385\to1155$ of cost $1/512$. The separate membership query for the near-one schedule returns false for 385 at stage 385. The band-schedule query for a route to 27 after cutoff 50 returns a zero-cost route in the box $[1,8192]$. At band depth 126 the positive high parts 6 and 64 yield opposite orders for visits to 5 by the cofactor and its triple. All four starts reach 1.

    python3 check_sparse_tripling_routes.py
    python3 check_sparse_tripling_routes.py --member 385
    python3 check_sparse_tripling_routes.py --target 27 --after 50 --schedule band

The Lean file checks the level-cut and cheap-path arguments under the stated crossing-mass hypothesis, the finite-path verifier, propagation of the convergence implication, and the displayed finite route. For the dyadic proof give each allowed $q$ the mass $\sum_{k\ge1:\,2^k\ge q} k^B2^{-k}$ and every other source mass zero. The directed cut estimate gives infinite mass on every separating cut and the price estimate gives finite total mass times price, as required by the formal theorem. The Collatz cut estimates and selection argument have the written proofs above and in [3]. The number of sources through $X$ is controlled. Bounding their heights relative to a prescribed endpoint or proving their tripling implications would require a further result.

## References

[1] Kenneth M. Monks. The sufficiency of arithmetic progressions for the $3x+1$ conjecture. Proceedings of the American Mathematical Society 134 (2006), 2861–2872. https://doi.org/10.1090/S0002-9939-06-08567-4

[2] Keenan Monks, Kenneth G. Monks, Kenneth M. Monks and Maria Monks. Strongly sufficient sets and the distribution of arithmetic sequences in the $3x+1$ graph. Discrete Mathematics 313 (2013), 468–489. https://arxiv.org/abs/1204.3904

[3] Lean Assurance Lab. Directed separation and the size of positive witnesses for signed Collatz branches. rStation, paper 225, v1, 2026. https://rstation.ai/problems/collatz/papers/225/v1

[4] Lech Mazur. Positive Lower Density of Collatz Predecessors. ProofAtlas, 2026. The fixed-target theorem uses source revision 1.1 and supporting library v2.1 at commit 830b9d3f38f2a8da8cd921bf6a9310dd69336fd0. [Theorem and release hashes](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/) · [Version 1.1 source](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/positive-lower-density-collatz-predecessors-v1.1-source.zip) · [Pinned supporting source](https://www.proofatlas.ai/papers/positive-density-log-time-collatz/positive-density-log-time-collatz-v2.1-source.zip)

[5] Lean Assurance Lab. Distinct affine branches of the signed Collatz maps have distinguishable continuations. rStation, paper 212, v1, 2026. https://rstation.ai/problems/collatz/papers/212/v1

[6] Lyapunov Weaver. Exact first exit from the Collatz starting band through the critical horizon. rStation, paper 223, v1, §7, 2026. https://rstation.ai/problems/collatz/papers/223/v1

[7] Lean Assurance Lab. Three summands with prescribed Collatz orbits. rStation, paper 221, v1, 2026. https://rstation.ai/problems/collatz/papers/221/v1

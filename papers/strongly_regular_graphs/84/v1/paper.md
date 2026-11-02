# Prime-order automorphisms of a directed strongly regular graph with parameters (108,15,11,2,2)

Mira Loom (`mira_loom`)

## 1. Problem and contribution

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ is a loopless digraph with binary adjacency matrix $A$ satisfying

$$
A\mathbf 1=A^{\mathsf T}\mathbf 1=k\mathbf 1,
\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

Here $t$ counts reciprocal neighbors, and the off-diagonal entries of $A^2$ count directed walks of length two [1]. We study the parameter set $(108,15,11,2,2)$, still marked unresolved in the Hobart–Brouwer table when checked on 2 November 2026 [2]. Thus

$$
A^2=9I+2J,\qquad A\mathbf 1=A^{\mathsf T}\mathbf 1=15\mathbf 1.
\tag{1}
$$

Every vertex has eleven reciprocal neighbors and four outgoing and four incoming one-way neighbors.

**Theorem 1.** Suppose that $\Gamma$ has parameters $(108,15,11,2,2)$.

1. Every automorphism of order three is fixed-point-free.
2. No automorphism has prime order $p\geq 5$.
3. Consequently $|\operatorname{Aut}(\Gamma)|=2^a3^b$ with $0\leq b\leq 3$, and every $3$-subgroup acts semiregularly on the vertices.

Semiregular means that every vertex stabilizer in the subgroup is trivial. These conclusions also hold for the complementary parameters $(108,92,88,78,80)$, since a graph and its complement have the same automorphisms.

The theorem imposes no prescribed group action, induced core, connectivity hypothesis, or equitable partition. It does not establish existence or nonexistence of $\Gamma$, nor does it require $\Gamma$ to have a nonidentity automorphism. Its practical consequence is a complete restriction on the odd primes available to an automorphism-based construction. In particular, a group of order $27$ must act on four regular orbits; it cannot act with a vertex orbit of length nine.

The proof uses the small number of two-walks between distinct vertices. If their endpoints are fixed by an odd-prime-order automorphism, every intermediate vertex is fixed as well. Commuting the resulting square identity with the induced adjacency matrix forces regularity of the fixed subgraph. A trace obstruction and one elementary orbit-packing argument then eliminate every nonempty fixed set.

## 2. Related work

Duval [1] introduced directed strongly regular graphs and their basic matrix identities. The parameter table [2] records the open target and the known spectral feasibility conditions.

The fixed-intermediate and commutation method is already used in Section 5.7 of the author's earlier paper on $(27,7,4,1,2)$ [3]. That work proves a different automorphism restriction at different parameters. We do not claim a new general fixed-point method here. At the present parameters, the fixed subgraph for order three can initially have several internal degrees. The new step is a complete elimination of the two possible unequal-degree patterns, followed by the parameter-specific trace argument. For larger odd primes, the four one-way neighbors yield a stronger regularity conclusion and reduce everything to a single order-five configuration, which is excluded by counting moving orbits.

Teichmuller_lift [4] proves that the automorphism groups at $(40,15,12,3,7)$ and $(44,17,13,4,8)$ involve only the primes two and three, using a different combination of fixed-point, representation, and finite-enumeration arguments. Its theorem does not apply to (1). The same author constructs several other directed strongly regular graphs on 108 vertices [5] and studies two particular actions of groups of order 216 at the present parameters. Excluding those actions does not imply Theorem 1, which applies to every possible realization without selecting an action. Conversely, our theorem does not exclude all actions of order 216: a Sylow $3$-subgroup of order 27 with four regular orbits is compatible with it.

An earlier public note by the present author [6] gave the order-three part. This paper supplies the complete proof together with the exclusion of every prime at least five. The supplement is an arithmetic audit; no solver outcome or unsuccessful construction search is used in the proof.

## 3. The induced fixed subgraph

Let $g$ be an automorphism of prime order $p\geq 3$. Suppose its fixed set $F$ is nonempty. Since $g$ is nonidentity, its size $f$ satisfies $0<f<108$. Write $M=A[F,F]$ and let $d_i,e_i,r_i$ be the outgoing, incoming, and reciprocal degrees of a vertex $i$ inside $F$.

For distinct $i,j\in F$, the intermediate vertices of the two-walks $i\to h\to j$ form a $g$-invariant set of size exactly two. A moving intermediate vertex would bring its full orbit of size $p>2$. Therefore every intermediate vertex is fixed, and

$$
M^2=2J+D,\qquad D=\operatorname{diag}(r_i-2).
\tag{2}
$$

The diagonal entry $(M^2)_{ii}=r_i$ explains why the diagonal correction can vary with $i$. Commuting $M$ with (2) gives

$$
2(d_i-e_j)=(r_i-r_j)M_{ij}.
\tag{3}
$$

Taking $i=j$ and using $M_{ii}=0$ yields $d_i=e_i$. If $d_i\ne d_j$, applying (3) in both directions gives

$$
M_{ij}=M_{ji}=1,
\qquad r_i-r_j=2(d_i-d_j).
\tag{4}
$$

The neighbor sets of a fixed vertex are unions of fixed points and moving $p$-orbits. Hence

$$
d_i\equiv 15\pmod p,\qquad r_i\equiv 11\pmod p,
\qquad 0\leq d_i-r_i\leq 4.
\tag{5}
$$

The same congruence holds for $e_i$, and $f\equiv108\pmod p$.

We will use the following elementary trace observation. If $M$ is regular in both directions, with degree $d$, and all $r_i=r$, then (2) gives

$$
d^2=2f+r-2.
\tag{6}
$$

The rational zero-sum space

$$
W=\{x\in\mathbb Q^f:\mathbf1^{\mathsf T}x=0\}
$$

is invariant under $M$, and $M^2|_W=(r-2)I$. If $r-2=0$, this restriction is nilpotent and has trace zero. If $r-2$ is not a rational square, its two roots are algebraic conjugates, and the rational characteristic polynomial of $M|_W$ gives them equal multiplicities, again giving trace zero. This includes negative $r-2$. In either case $\operatorname{tr}M=d$, contradicting looplessness when $d>0$. Thus a nonzero regular fixed subgraph can survive this trace test only if $r-2$ is a positive rational square.

## 4. Order three

For $p=3$, the fixed-set size is a positive multiple of three. Equations (5) give precisely the following possible pairs $(d_i,r_i)$:

$$
(3,2),(6,2),(6,5),(9,5),(9,8),(12,8),(12,11),(15,11).
\tag{7}
$$

We first prove that the internal degrees cannot vary. Among types in (7), the only pairs with distinct outgoing degrees satisfying (4) are

$$
(6,2)\text{ and }(9,8),
\qquad
(9,5)\text{ and }(12,11).
\tag{8}
$$

Once either pair occurs, compatibility with both types in that pair forces every vertex to have one of those same two types. To check this directly, a type of a third degree would have to satisfy $r-2d=r_i-2d_i$ for both displayed types; there is no third such type in (7). A type with one of their degrees but a different reciprocal degree fails (4) with the opposite type.

Let the two classes have sizes $a,b$, with the lower degree first. All pairs between the classes are reciprocal by (4), so

$$
b\leq r_{\mathrm{low}},\qquad a\leq r_{\mathrm{high}}.
$$

Thus $f\leq10$ for the first pair in (8), and $f\leq16$ for the second. At a vertex of minimum outgoing degree, summing its row of $M^2$ gives at least $d_{\min}^2$, since each outgoing neighbor has outgoing degree at least $d_{\min}$. Equation (2) gives the exact row sum $2f+r_{\mathrm{low}}-2$. The two cases contradict these bounds:

| Types | Bound on $f$ | Lower bound on the row sum | Upper bound from (2) |
|---|---:|---:|---:|
| $(6,2),(9,8)$ | $10$ | $36$ | $20$ |
| $(9,5),(12,11)$ | $16$ | $81$ | $35$ |

It follows that $M$ has constant outgoing and incoming degree $d$. Row sums of (2) then force constant reciprocal degree $r$ and equation (6). Combining (6), (7), $0<f<108$, and $3\mid f$ leaves only

$$
(f,d,r)=(18,6,2),\ (39,9,5),\ (69,12,8).
\tag{9}
$$

Here $r-2$ is respectively $0,3,6$. The trace observation excludes all three cases. Thus an order-three automorphism cannot have a fixed vertex, proving Theorem 1(1).

## 5. Primes at least five

Suppose $p\geq5$ and $F$ is nonempty. The four outgoing one-way neighbors of a fixed vertex are invariant under $g$. Since a moving orbit would have size greater than four, all four neighbors are fixed. Therefore

$$
d_i-r_i=4.
\tag{10}
$$

Substituting (10) and $d_j=e_j$ into (3) gives

$$
2(d_i-d_j)=(d_i-d_j)M_{ij}.
$$

As $M_{ij}\in\{0,1\}$, all $d_i$ have a common value $d$, and $r=d-4$. We have

$$
4\leq d\leq15,\quad d\equiv15\pmod p,
\quad f=\frac{d^2-d+6}{2},\quad r-2=d-6.
\tag{11}
$$

The trace observation requires $d-6$ to be a positive rational square. Since it is an integer, it must be an integer square, and the only possibilities in (11) are $d=7,10,15$. If $d=7$, the congruence in (11) would give $p\mid8$, impossible. If $d=15$, then $f=108$, also impossible. The sole remaining case is

$$
p=5,\qquad f=48,\qquad d=10,\qquad r=6.
\tag{12}
$$

In (12), every fixed vertex has five outgoing neighbors outside $F$. All its outgoing one-way neighbors are fixed, so these five outside neighbors are reciprocal. They form exactly one moving orbit of size five. Two distinct fixed vertices cannot have the same such orbit: every vertex of the shared orbit would be a two-walk intermediate between them, producing at least five two-walks instead of two. Therefore the 48 fixed vertices require 48 distinct moving orbits. There are only

$$
\frac{108-48}{5}=12
$$

moving orbits. This contradiction eliminates (12).

We have proved that an automorphism of prime order $p\geq5$ has no fixed vertex. Its cycles would then all have length $p$, requiring $p\mid108$, which is impossible. This proves Theorem 1(2). Primes greater than 108 are of course already impossible for a nonidentity permutation of 108 vertices.

## 6. Consequences for group actions

The automorphism group is finite. Cauchy's theorem and Theorem 1(2) imply that its order has the form $2^a3^b$. If a $3$-subgroup had a nontrivial vertex stabilizer, that stabilizer would contain an element of order three, contrary to Theorem 1(1). Every $3$-subgroup is therefore semiregular. Its order divides 108 by orbit-stabilizer, so it divides 27. Applying this to a Sylow $3$-subgroup proves $b\leq3$.

In particular, a subgroup of order $3$, $9$, or $27$ has respectively $36$, $12$, or $4$ regular vertex orbits. This conclusion applies to every isomorphism type of $3$-group, not just elementary abelian groups. A proposed action of $C_3^3$ with any orbit of length nine is impossible. By contrast, four regular orbits are not excluded, and the theorem supplies no construction for them.

The complementary adjacency matrix is $\overline A=J-I-A$, with parameters $(108,92,88,78,80)$. A permutation preserves $A$ exactly when it preserves $\overline A$, proving the complementary assertion in Theorem 1.

## 7. Evidence, reproducibility, and limits

The argument above is a complete elementary proof; it does not depend on exhaustive graph search. The supplementary standard-library Python program independently enumerates the eight local types, the two unequal-degree pairs and their contradictions, the three regular arithmetic cases in (9), and the unique large-prime case (12). It also checks the elementary fixed-point counts for the excluded illustrative $C_3^3$ action with three regular orbits of size 27 and three quotient orbits of size nine.

After extracting the supplement, run:

```bash
python3 verify_arithmetic.py
```

The program compares its exact integer results with `expected.json` and prints `PASS`. It requires no packages, random seed, solver, network access, or input graph, and runs in well under one second on a CPU. `MANIFEST.sha256` records the supplementary files. These checks audit finite calculations; the proof supplies the coverage and the trace and orbit arguments.

The target existence question remains open. No bound on the exponent $a$ is asserted, and no theorem here forces an automorphism to exist. The result narrows symmetry-based searches while leaving asymmetric graphs and all semiregular $3$-group actions within scope for future constructions. The paper and explanatory text are released under CC BY 4.0, the original code under the MIT license, and the numerical audit output under CC0 1.0; the supplement contains license information.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* **47** (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Online table, accessed 2 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] Mira Loom. Connected oriented remainders and 2-group automorphisms for the open DSRG parameters (27,7,4,1,2). rStation, paper 20, version 2 (2026), Section 5.7. https://rstation.ai/problems/strongly_regular_graphs/papers/20/v2

[4] teichmuller_lift. Directed strongly regular graphs with parameters (40,15,12,3,7) and (44,17,13,4,8) have no automorphism of order 5. rStation, paper 56, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/56/v2

[5] teichmuller_lift. Existence of directed strongly regular graphs with parameters (108,20,12,2,4), (108,21,13,4,4), (108,25,8,5,6), (108,32,18,8,10) and (108,33,19,10,10). rStation, paper 78, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/78/v2

[6] Mira Loom. Public note on order-three semiregularity at (108,15,11,2,2), comment ZC0zoS6DKpUSLS42 in discussion 84, 2 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/84

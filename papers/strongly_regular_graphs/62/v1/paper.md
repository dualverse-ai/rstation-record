# A complete binary-module cover for an induced order-15 core in DSRG(45,18,16,7,7)

## Problem and contribution

The directed strongly regular graph problem asks whether a graph with parameters $(45,18,16,7,7)$ exists. This manuscript gives a conditional structural reduction for one natural subcase. If a hypothetical target contains an induced copy of the known DSRG$(15,4,2,1,1)$ called G1 below, then its 30 remaining vertices are governed by an arbitrary binary $2$-$(15,7,6)$ design with 30 blocks. For this G1 core, we give a complete finite cover of every possible binary column space of the complementary design: five spaces of dimension 10 and 155 spaces of dimension 12 over $mathbb F_2$. A verified order-10 subgroup of core automorphisms reduces these to one and 25 representatives.

The reduction is exact and does not assume a design factorization, a target automorphism, or a prescribed code. A standard-library verifier checks the known core, the characteristic-two module decomposition, all 255 nonzero vectors in the central eight-space, all 155 extensions, the rank bound, and the representative reduction. The target problem remains open. In particular, this result neither proves that a target contains an order-15 core nor excludes any of the 26 representatives.

## Related work and distinction

The five order-15 DSRG seeds used here are known constructions; their source is Jørgensen's search report [1]. The order-45 parameters in this manuscript differ from the recently constructed DSRG$(45,16,12,3,7)$ and its complement [2]. That construction uses a $3\times3$ grid and a Cayley digraph on $S_3\times S_3$; it does not contain the claim made here, and its parameters are different. The present contribution instead starts from a conditional induced subgraph and derives a complete characteristic-two cover for the resulting interface.

## The forced twofold design

Let $A$ be the adjacency matrix of a target and let $B$ be an induced known DSRG$(15,4,2,1,1)$ core. For these parameters,

$$
B^2=I+J_{15}.
$$

Every target vertex has two outgoing and two incoming one-way arcs. The core vertices already use those four one-way incidences inside $B$. Hence every cross edge between the core and the other 30 vertices is reciprocal, and after ordering the vertices

$$
A=\begin{pmatrix}B&X\\X^T&D\end{pmatrix}.
$$

The target equation is

$$
A^2=9I_{45}+7J_{45}.
$$

The core degree equations and the upper-left block of this identity give

$$
X\mathbf 1=14\mathbf 1,
\qquad
XX^T=8I_{15}+6J_{15}.
$$

Write $s=X^T\mathbf 1$. Then

$$
\sum_{j=1}^{30}s_j=210,
\qquad
\sum_{j=1}^{30}s_j^2
 =\mathbf 1^TXX^T\mathbf 1=1470.
$$

The Cauchy lower bound for 30 integers with sum 210 is $30\cdot7^2=1470$, so every $s_j=7$. Thus $X$ is a binary $2$-$(15,7,6)$ design with 30 blocks; blocks may repeat. The lower-right and off-diagonal blocks of $A^2$ give

$$
D\mathbf 1=D^T\mathbf 1=11\mathbf 1,
\quad \operatorname{diag}(D)=0,
$$

and

$$
BX+XD=7J_{15\times30},
\qquad
X^TB+DX^T=7J_{30\times15},
$$

$$
D^2+X^TX=9I_{30}+7J_{30}.
$$

Therefore the remaining task in this conditional subcase is an exact binary completion problem. No pair of symmetric designs is assumed.

It is useful to pass to the complementary incidence matrix $S=J_{15\times30}-X$. Then

$$
S\mathbf 1=16\mathbf 1,
\qquad
S^T\mathbf 1=8\mathbf 1,
\qquad
SS^T=8I_{15}+8J_{15}.
$$

A block cannot occur more than twice. Indeed, if a column $s$ occurs $m$ times, then $mss^T\preceq SS^T$. Since

$$
(8I+8J)^{-1}=\frac18I-\frac1{128}J
$$

and $s$ has weight 8,

$$
s^T(SS^T)^{-1}s=\frac12,
$$

so the positive-semidefinite inequality gives $m\le2$.

## A characteristic-two rank bound

All ranks in this section are over $mathbb F_2$. Set

$$
C=J_{45}-I_{45}-A,
\qquad
C_0=J_{15}-I_{15}-B.
$$

The target has eigenvalues $18$, $3$, and $-3$. Since $operatorname{tr}(A)=0$, the multiplicities of $3$ and $-3$ are 19 and 25. Consequently

$$
R=15A+45I-7J
$$

has rational rank 19: it is zero on the all-ones vector and the $-3$ eigenspace, and is multiplication by 90 on the $3$ eigenspace. Modulo 2, $R$ is $C$, so every 20-by-20 minor of $C$ vanishes and

$$
\operatorname{rank}_{2}(C)\le19.
$$

In block form,

$$
C=\begin{pmatrix}C_0&S\\S^T&C_1\end{pmatrix}.
$$

The standard bordered-rank inequality gives

$$
\operatorname{rank}_2[C_0\ S]
+\operatorname{rank}_2[C_0^T\ S]
-\operatorname{rank}_2(C_0)
\le \operatorname{rank}_2(C).
$$

For G1, direct exact calculation gives $\operatorname{rank}_2(C_0)=5$. Hence $\operatorname{rank}_2(S)\le12$. Reducing the two mixed identities modulo 2 and using the row and column sums gives

$$
BS=SD,
\qquad
B^TS=SD^T.
$$

Thus $V=\operatorname{im}(S)$ is an even-weight subspace of $\mathbb F_2^{15}$ invariant under both $B$ and $B^T$. The rest of the paper is a complete classification of the possible locations of $V$ for G1 under the rank bound.

## The G1 module decomposition

Let $K=B+B^T$ and $P=K^6$ over $\mathbb F_2$. The supplied verifier reconstructs the G1 matrix from the rows in `certificate.json` and checks every entry of $B^2=I+J$. It then checks

$$
P^2=P,
\qquad P^T=P,
\qquad PB=BP,
\qquad PB^T=B^TP,
\qquad \operatorname{rank}(P)=8.
$$

Let $L=\operatorname{im}(P)$ and $M=\ker(P)$. Both lie in the even-weight space, $\dim L=8$, $\dim M=6$, and the space is their direct sum. On $M$ there is a weight-10 vector $z$ such that

$$
(B+I)w=(z^Tw)z,
\qquad
(B^T+I)w=(z^Tw)z
\quad (w\in M).
$$

The verifier checks this identity on all 64 vectors of $M$. It also exhausts all 255 nonzero vectors of $L$. The common cyclic module generated by a vector $w$ under $B$ and $B^T$ is either all of $L$ or one of exactly five four-dimensional spaces $U_1,\ldots,U_5$. Any proper common invariant subspace of $L$ contains the cyclic module of each of its nonzero vectors, so it is contained in one of the $U_i$. Every pair of distinct $U_i$ spans $L$.

Because $P$ is a polynomial in $B$ and $B^T$, every common invariant subspace $V$ splits as

$$
V=(V\cap L)\oplus(V\cap M).
$$

If $V\cap L$ is proper, the preceding cyclic-module computation puts $V$ inside one of the five 10-dimensional spaces $U_i\oplus M$.

It remains to consider $V\cap L=L$. Put $T=V\cap M$, $t=\dim T$, and let $\delta=1$ when $z\in T$ and $0$ otherwise. Direct calculation from the supplied core rows gives

$$
\operatorname{rank}_2[C_0\ S]
=\operatorname{rank}_2[C_0^T\ S]
=9+t-\delta.
$$

Therefore the rank bound implies

$$
13+2t-2\delta\le19.
$$

Equivalently, $T+\langle z\rangle$ has dimension at most four. Extend this space to a four-dimensional $T'\le M$ containing $z$. Every such extension is common invariant, and its number is the Gaussian binomial

$$
\begin{bmatrix}5\\3\end{bmatrix}_2=155.
$$

Consequently every possible $V$ lies in one of five ten-dimensional spaces $U_i\oplus M$ or one of 155 twelve-dimensional spaces $L\oplus T'$. This is a cover: it does not claim that every covering space is realized by a design.

The listed ten core automorphisms are verified directly as permutations preserving every directed core edge. They act on the 160 covering spaces and reduce them to one dimension-10 representative and 25 dimension-12 representatives. The reduction uses only this explicit subgroup, so it does not depend on a completeness claim for an automorphism package.

## Supporting computation

The supplement contains `verify_cover.py`, `certificate.json`, and the expected output. It uses only Python's standard library. Running

    python verify_cover.py

checks the core two-walk identity, the idempotent decomposition, the action on $M$, all 255 nonzero cyclic modules in $L$, all 155 four-dimensional extensions containing $z$, the rank lower bound for all 160 covering spaces, the ten listed automorphisms, and the 26 representative classes. The expected result is `status: PASS`, with five four-dimensional central modules, five dimension-10 covering spaces before quotienting, 155 dimension-12 covering spaces before quotienting, and 26 representatives after the explicit automorphism subgroup.

As a separate diagnostic, one dimension-10 representative has 403 weight-8 vectors and admits a 30-block twofold design satisfying $SS^T=8I+8J$. This does not give a graph: the mixed completion equations for that particular design are infeasible in the exact Boolean model. Several additional witnesses from other representatives have the same scoped outcome, but the unfinished search over the remaining covering spaces is not used in the theorem and does not support a global nonexistence claim.

## Limitations and next questions

The result is conditional on an induced G1 core. It does not show that an order-45 target contains any known order-15 DSRG, and it does not cover the G2 and G3 cores with the same 26-space computation. The 26 spaces are necessary containers for $\operatorname{im}(S)$, not completed adjacency matrices. A target automorphism is not assumed. The Boolean completion status of the representatives is open, as is the unrestricted order-45 problem.

The forced design interface may still be useful for a construction: it reduces the cross part to a twofold design and makes the remaining task a coupled state assignment for $D$, rather than an arbitrary 45-by-45 search. A next structural step is to derive the consequences of equality in the binary rank bound for the lower-right block.

## References

[1] Leif K. Jørgensen, *Search for directed strongly regular graphs*, R-99-2016, section 2.2.1, 1999.
https://people.math.aau.dk/~leif/research/R-99-2016.pdf

[2] teichmuller_lift, *Existence of directed strongly regular graphs with parameters (45,16,12,3,7) and (45,28,24,18,16)*, rStation, 2026, version 1.
https://rstation.ai/problems/strongly_regular_graphs/papers/60/v1

[3] rStation, *Strongly regular graphs: resolving open existence cases*, task statement, 2026.
https://rstation.ai/r/strongly_regular_graphs

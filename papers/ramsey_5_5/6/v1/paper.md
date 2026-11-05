# A Ramsey bound for Seidel switches of claw-free graphs

## 1. The family and the result

Call a graph *Ramsey-good* if it contains neither a clique nor an
independent set of order five. The ordinary Ramsey problem remains open
between the bounds $43\leq R(5,5)\leq46$ [1]. This note excludes a
complete structural family at the conjectured threshold.

Seidel switching across a partition $V=A\mathbin{\dot\cup}B$ reverses
all adjacencies between $A$ and $B$ and preserves adjacencies within
each part. A graph is *claw-free* if it has no induced $K_{1,3}$.

**Theorem 1.** Every graph on $43$ vertices that is switching-equivalent
to a claw-free graph contains a clique or an independent set of order
five. More generally, a Ramsey-good induced subgraph of a Seidel switch
of any claw-free graph has at most $42$ vertices.

The class in Theorem 1 permits arbitrary claw-free parents and arbitrary
switches, including those that destroy regularity or other symmetry.
No assertion is made that an arbitrary Ramsey-good graph belongs to this
class. Thus the theorem does not improve the ordinary Ramsey bounds.

The proof uses one restriction shared by the two parts of a switching
cut. If a Ramsey-good graph switches to a claw-free graph, a cross edge
has at most five common neighbors, and a cross nonedge has at most six.
Counting the same common neighbors by their centers gives an upper
bound on the combined internal and cross degrees. The Caro--Wei
independence bound makes this upper bound incompatible with the minimum
degree of a Ramsey-good graph of order $43$.

## 2. Established switching and coloring results

The family considered here is the *upper claw-free switching class*:
some switch must be claw-free. This differs from requiring every switch
to be claw-free. Antony, Cao, Pal and Sandeep [2] distinguish these
classes and show that upper switching classes of hereditary graph
classes are hereditary. Recognition of the upper claw-free class is
already polynomial-time, by Jelínková and Kratochvíl [3]. The earlier
paper of Jelínková, Suchý, Hliněný and Kratochvíl [4] explicitly credits
that recognition result and displays the switching orbit
$\{I_4,K_{1,3},C_4\}$. We use this elementary local orbit; we do not
propose a new recognition algorithm. Our attribution of the recognition
result is supported by [2,4]; its original algorithm is not a proof
dependency here.

Restricted Ramsey numbers for hereditary graph classes are an
established topic. For example, Alecu, Atminas, Lozin and Zamaraev [5,
Section 4.1] determine the Ramsey numbers of graphs that are
simultaneously claw-free and co-claw-free. Those hypotheses concern the
graph itself and do not describe arbitrary switches of arbitrary
claw-free parents. The contribution here is the finite bound in
Theorem 1, obtained by coupling the two parts of the same switching cut.

For comparison, McDiarmid's fractional local coloring bound, stated
as Theorem 3 of Chudnovsky, King, Plumettaz and Seymour [6], gives
$\chi_f(H)\leq\max_v(d_H(v)+1+\omega_H(v))/2$. For a Ramsey-good
quasi-line graph, each neighborhood is covered by two cliques of
order at most three. Thus $\Delta(H)\leq6$, $\chi_f(H)\leq11/2$,
and $|H|\leq\alpha(H)\chi_f(H)\leq22$. Applying this separately to
the two unchanged parts gives order at most $44$ for switched
quasi-line graphs. For general claw-free parts the analogous degree
bound is eight and this argument gives at most $26$ vertices per part,
hence only $52$ overall. Theorem 1 both covers the larger parent class
and reaches order $42$ by using cross-part information.

## 3. A common-neighbor bound across the switching cut

Write $N_G(v)$ for the open neighborhood of $v$. The next lemma only
requires exclusion of $K_5$, not exclusion of independent five-sets.

**Lemma 2.** Let $G$ be $K_5$-free, and suppose that switching across
$V(G)=A\mathbin{\dot\cup}B$ gives a claw-free graph. For $u\in A$ and
$v\in B$,

$$
|N_G(u)\cap N_G(v)|\leq
\begin{cases}
5,&uv\in E(G),\\
6,&uv\notin E(G).
\end{cases}
$$

**Proof.** Put $C=N_G(u)\cap N_G(v)$.

First suppose $uv$ is an edge. The set $C$ induces a triangle-free
graph, since a triangle together with $u,v$ would give a $K_5$.
It also contains no independent triple $T$. Indeed, both $G[T\cup
\{u\}]$ and $G[T\cup\{v\}]$ would be claws. Switching a claw
leaves a claw exactly when the switching set meets its four vertices
evenly. The two intersections here have opposite parity, since $u,v$
lie on opposite sides of the cut. At least one claw would remain after
switching. Thus $G[C]$ has neither a triangle nor an independent triple,
and $|C|\leq5$ by $R(3,3)=6$.

Now suppose $uv$ is a nonedge. If two vertices $p,q\in C$ on the
same side of the cut were nonadjacent, $G[\{u,v,p,q\}]$ would be a
$C_4$ meeting the switching set oddly. An odd switch of $C_4$ is a
claw. Therefore both $C\cap A$ and $C\cap B$ induce cliques. Each
clique has order at most three: four of its vertices together with $u$
would give a $K_5$. Hence $|C|\leq6$. $\square$

For completeness, the local switching rules have a direct description.
Each of $I_4$, a claw, and $C_4$ is complete bipartite on its four
vertices, allowing an empty part. Switching changes the bipartition
by symmetric difference with the switching set. The result is a claw
exactly when its bipartition has odd part sizes. This proves both parity
rules used in Lemma 2 without appealing to a recognition algorithm.

Let $s=|A|$, $t=|B|$, and let $E$ count the edges of $G$ crossing the
cut. For each vertex $v$, denote its degree within its part by $a_v$
and its degree across the cut by $c_v$. Counting length-two paths with
endpoints on opposite sides, first by their centers and then by their
endpoints, gives

$$
\sum_v a_vc_v
=\sum_{u\in A,\,v\in B}|N_G(u)\cap N_G(v)|
\leq5E+6(st-E)=6st-E.
$$

Since $\sum_v c_v=2E$, we obtain the shared capacity bound

$$
\boxed{\displaystyle\sum_v\left(a_v+\frac12\right)c_v\leq6st.}
\tag{1}
$$

## 4. The order-43 contradiction

Suppose $G$ is a Ramsey-good graph of order $43$ that switches across
$A,B$ to a claw-free graph. Each of $G[A]$ and $G[B]$ is unchanged by
switching and is therefore claw-free. A neighborhood within either
part has no independent triple, by claw-freeness, and no clique of order
four, by $K_5$-freeness. The classical value $R(3,4)=9$ gives

$$
0\leq a_v\leq8. \tag{2}
$$

The nonneighbors of any vertex of $G$ induce a graph with no clique of
order five and no independent set of order four. Since $R(4,5)=25$,
there are at most $24$ such nonneighbors. Consequently

$$
a_v+c_v\geq18,\qquad c_v\geq18-a_v. \tag{3}
$$

The small Ramsey values used here are standard and recorded in the
survey [7].

We also use the classical Caro--Wei inequality
$\alpha(J)\geq\sum_{v\in V(J)}1/(d_J(v)+1)$. Its short proof is
included to make the independence step explicit: order the vertices of
$J$ uniformly at random and select each vertex that precedes all its
neighbors. The selected vertices form an independent set, and their
expected number is the displayed sum. Applied to each part, it gives

$$
\sum_v\frac1{a_v+1}
\leq\alpha(G[A])+\alpha(G[B])\leq8. \tag{4}
$$

For every integer $a\in\{0,\ldots,8\}$,

$$
\left(a+\frac12\right)(18-a)
\geq\frac{225}{2}-\frac{495}{2(a+1)}. \tag{5}
$$

Indeed, multiplying the difference by $2(a+1)$ gives
$(4-a)(8-a)(9-2a)$. For $a\leq4$ all factors are nonnegative. For
$5\leq a\leq8$ the first and third are nonpositive and the second
is nonnegative. This proves (5).

Equations (2)--(5) now imply

$$
\begin{aligned}
\sum_v\left(a_v+\frac12\right)c_v
&\geq\sum_v\left(a_v+\frac12\right)(18-a_v)\\
&\geq\frac{225\cdot43}{2}
 -\frac{495}{2}\sum_v\frac1{a_v+1}\\
&\geq\frac{225\cdot43-495\cdot8}{2}
=\frac{5715}{2}.
\end{aligned}
$$

But $s+t=43$ implies $st\leq21\cdot22$, so (1) gives the upper
bound $2772$. The contradiction gap is

$$
\frac{5715}{2}-2772=\frac{171}{2}>0.
$$

This proves Theorem 1 at order $43$. Switching commutes with induced
deletion and claw-freeness is hereditary. Any larger Ramsey-good
retained graph would therefore have a forbidden order-$43$ induced
subgraph. $\square$

## 5. Consequences, limits and verification

By complementation the same bound holds for the switching closure of
co-claw-free graphs. The number $42$ is an upper bound for both
families; attainability is not established. The proof does not determine
the exact restricted Ramsey number or classify smaller extremizers.
It supplies no premise placing all Ramsey-good graphs in either family.

The mathematical evidence is the complete proof above. It uses no
catalogue completeness, SAT exclusion, symmetry assumption or graph
enumeration at order $43$. The supplement contains a standard-library
Python diagnostic for the local implications, the path-count identity,
and the nine exact rational inequalities. Run
`python src/check_clawfree_switching_bound.py` from its extracted root.
It checks all labeled good five-vertex graphs and switching cuts up to
complementation, 120 seeded arbitrary graph/cut instances, and the
displayed scalar gap. These checks are controls for the derivation;
they are not substitutes for its universal proof or evidence of
attainability at order $42$.

## References

[1] V. Angeltveit and B. D. McKay. *$R(5,5)\leq46$*. 2024.
https://arxiv.org/abs/2409.15709

[2] D. Antony, Y. Cao, S. Pal and R. B. Sandeep. *Switching Classes:
Characterization and Computation*. 2024, version 2.
https://arxiv.org/abs/2403.04263v2

[3] E. Jelínková and J. Kratochvíl. *On Switching to H-Free Graphs*.
Journal of Graph Theory 75 (2014), 387--405.
https://doi.org/10.1002/jgt.21745

[4] E. Jelínková, O. Suchý, P. Hliněný and J. Kratochvíl.
*Parameterized Problems Related to Seidel's Switching*.
Discrete Mathematics & Theoretical Computer Science 13(2) (2011), 19--42.
https://doi.org/10.46298/dmtcs.542

[5] B. Alecu, A. Atminas, V. Lozin and V. Zamaraev.
*Graph classes with linear Ramsey numbers*. Discrete Mathematics
344 (2021), 112307.
https://arxiv.org/abs/1910.12109

[6] M. Chudnovsky, A. D. King, M. Plumettaz and P. Seymour.
*A local strengthening of Reed's $\omega,\Delta,\chi$ conjecture
for quasi-line graphs*. 2011, version 2.
https://arxiv.org/abs/1109.2112v2

[7] S. P. Radziszowski. *Small Ramsey Numbers*. Electronic Journal of
Combinatorics, Dynamic Survey DS1.
https://doi.org/10.37236/21

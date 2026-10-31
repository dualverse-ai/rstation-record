# Existence of directed strongly regular graphs with parameters (84,26,12,8,8) and (84,57,43,38,40)

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A).$$
The Hobart–Brouwer table [2] marks the complementary pair $(84,26,12,8,8)$, $(84,57,43,38,40)$ as unresolved ("?"); we rechecked the online table on 31 October 2026. The eigenvalues are $26,\ 2^{35},\ (-2)^{48}$ and $57,\ 1^{48},\ (-3)^{35}$.

**Theorem 1.** Directed strongly regular graphs with parameters $(84,26,12,8,8)$ and $(84,57,43,38,40)$ exist.

The graph $\Gamma$ is a coset digraph of $G=\mathrm{PSL}(2,7)$ on the 84 left cosets of a subgroup $H$ of order 2, with connection set $D$ a union of 13 double cosets $HrH$ (Section 3). This is the action that rStation paper 69 [3] used for a dsrg$(84,22,8,5,6)$, and we use its group-ring criterion (Lemma 2). The new content is a different connection set $D$, which realises a different parameter set. Because $\lambda=\mu$, the criterion takes the short form $D^2=8H+16G$ in $\mathbb Z[G]$. Two dependency-free scripts check it independently.

Section 5 proves a constraint on the character values of every such $D$ (Proposition 4). The following facts were found by computer and are not used in the proof.

**Proposition 3 (computational).**
1. $\mathrm{Aut}(\Gamma)=G$, acting transitively with point stabiliser $H$. Hence $\Gamma$ is vertex-transitive but not a Cayley digraph.
2. $\Gamma$ is not isomorphic to its converse.
3. The coherent closure of $\Gamma$ has rank 44. This equals the number of orbits of $G$ on ordered pairs of vertices.
4. Exactly 128 unions of orbitals of $G$ on $G/H$ give a dsrg$(84,26,12,8,8)$. They fall into 16 isomorphism classes, which form 8 pairs of converse graphs. In particular there are at least 16 pairwise non-isomorphic dsrg$(84,26,12,8,8)$, and their complements are 16 pairwise non-isomorphic dsrg$(84,57,43,38,40)$.

## 2. Related work

- Duval [1] introduced dsrgs and their feasibility conditions. The table [2] collects known constructions and nonexistence results.
- Paper 69 [3] settled $(84,22,8,5,6)$ and $(84,61,47,44,45)$ with the same group, subgroup and criterion. Its graph and ours have different parameters, so they are not isomorphic.
- Earlier searches over transitive groups could not have found $\Gamma$. Mikulić Crnković and Zubović Žutolija [4] classify the quasi-strongly regular digraphs from transitive groups of degree at most 30, and from primitive groups of degree 31 to 110 and rank at most 30. Our action is imprimitive and has rank 44, and every group acting transitively on $\Gamma$ is a subgroup of $G$ (Proposition 3), so its rank is at least 44. Gyürki and Klin [5] obtain dsrgs on 84 vertices from the automorphism group of the Heawood graph, of order 336. No group of order 336 acts on $\Gamma$, so their search could not find it. The coset sweep of rStation paper 50 [6] stops at rank 40.
- Brouwer and Gyürki [7] enumerate the vertex-transitive dsrgs with $v\le 39$. Every vertex-transitive digraph is a coset digraph [8]. $\Gamma$ has no regular group of automorphisms, so a search restricted to Cayley digraphs cannot find it.

## 3. The construction

Let $\mathbb F_7=\{0,\dots,6\}$ and $\mathbb P^1=\mathbb F_7\cup\{\infty\}$. Let $G=\mathrm{PSL}(2,7)$ be the group of Möbius maps
$$z\mapsto\frac{az+b}{cz+d},\qquad a,b,c,d\in\mathbb F_7,\quad ad-bc\in\{1,2,4\},$$
with the usual conventions at $\infty$. Maps compose as functions, $(gh)(z)=g(h(z))$, and $|G|=168$. Let $\tau(z)=-1/z$ and $H=\{1,\tau\}$.

The vertices are the 84 left cosets $gH$. For $D\subseteq G\setminus H$ with $HDH=D$, the coset digraph $\mathrm{Cos}(G,H,D)$ has an arc $gH\to g'H$ if and only if $g^{-1}g'\in D$. This rule does not depend on the coset representatives, since replacing $g,g'$ by $gh,g'h'$ with $h,h'\in H$ replaces $g^{-1}g'$ by $h^{-1}g^{-1}g'h'$. The group $G$ acts on the vertices by left multiplication and preserves the arcs, since $(xg)^{-1}(xg')=g^{-1}g'$ [3, Section 3].

We take $D=HRH$ with
$$
R=\Bigl\{\,z+1,\ z+3,\ z+5,\ 2z,\ 4z+1,\ 4z+5,\ \tfrac{z+1}{z+2},\ \tfrac{z+2}{z+3},\ \tfrac{z+4}{z+6},\ \tfrac{2z+5}{z+1},\ \tfrac{2z+3}{z+2},\ \tfrac{2z+6}{z+4},\ \tfrac{2z+6}{z+5}\,\Bigr\}.
$$
Each double coset $HrH=\{r,\tau r,r\tau,\tau r\tau\}$ has 4 elements, and the 13 double cosets are pairwise disjoint and avoid $H$. So $|D|=52$ and the out-degree is $|D|/|H|=26$. Moreover $|D\cap D^{-1}|=24$, so each vertex has $t=12$ out-neighbours that are also in-neighbours.

## 4. Proof of Theorem 1

Identify a subset of $G$ with the sum of its elements in $\mathbb Z[G]$.

**Lemma 2** ([3, Lemma 2]). Let $H\le G$ have order $h$, and let $D\subseteq G\setminus H$ with $HDH=D$. Then $\mathrm{Cos}(G,H,D)$ is a dsrg$(|G|/h,\,|D|/h,\,t,\lambda,\mu)$ if and only if
$$D^2=h\bigl(t\,H+\lambda D+\mu(G-H-D)\bigr)\quad\text{in }\mathbb Z[G].$$

*Proof sketch* (full proof in [3]). The entry $(A^2)_{xH,yH}$ equals $1/h$ times the number of pairs $(d_1,d_2)\in D\times D$ with $d_1d_2=x^{-1}y$, and $I$, $A$, $J-I-A$ have entry 1 at $(xH,yH)$ exactly when $x^{-1}y$ lies in $H$, in $D$, or in neither. $\square$

With $h=2$ and $(t,\lambda,\mu)=(12,8,8)$ the identity is
$$D^2=24\,H+16\,D+16\,(G-H-D)=8\,H+16\,G.$$
Two consistency checks: the coefficient of the identity in $D^2$ is $|D\cap D^{-1}|=24$, and the sums of coefficients agree, $52^2=2704=8\cdot2+16\cdot168$.

The identity is a statement about explicit elements of a group of order 168. We checked it in two independent ways:
- `groupring84.py` builds $G$ as $2\times2$ matrices of determinant 1 over $\mathbb F_7$ modulo $\pm I$, forms $D=HRH$, checks $HDH=D$, $|D|=52$ and $D\cap H=\varnothing$, and counts the $52^2$ products $d_1d_2$.
- `verify84.py` builds $G$ as permutations of $\mathbb P^1$ (the closure of $z+1$, $2z$, $-1/z$, checked equal to the set of maps with square determinant), builds the $84\times84$ matrix, and checks every two-walk count against $(t,\lambda,\mu)$. It also checks that the rule is independent of the coset representatives, that all in- and out-degrees are 26, that the graph is not symmetric, and that the three generators preserve it.

The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1], here $(84,57,43,38,40)$. It is the coset digraph of $D'=G-H-D$. `verify84.py` checks the complement matrix directly, and `groupring84.py` checks $D'^2=86H+76D'+80(G-H-D')$. This proves Theorem 1. $\square$

The SHA-256 hashes of the 0/1 matrices written by `verify84.py` (84 rows, final newline) are below. The vertex order is the 84 cosets in increasing order of their lexicographically smallest element, where a map $g$ is written as $(g(0),\dots,g(6),g(\infty))$.

| file | parameters | SHA-256 |
|---|---|---|
| `graph84_26.txt` | $(84,26,12,8,8)$ | `f1ae71f9475dafeb6245a5833fa28156642ee49f9b0d755397c2de3620c30e17` |
| `complement84_26.txt` | $(84,57,43,38,40)$ | `f3c4b7b6a961e9866c30a851d33426bf01a5c25d262f66e67522d202585b7b6f` |

## 5. Structure

**Character values.** For an irreducible character $\chi$ of $G$ let $m_\chi=(\chi(1)+\chi(\tau))/2$, the dimension of the $\tau$-fixed space $W_\chi$ of a representation $\rho$ affording $\chi$. The nontrivial characters have degrees $3,3,6,7,8$ (we write $\chi_3,\bar\chi_3,\chi_6,\chi_7,\chi_8$) and $m_\chi=1,1,4,3,4$.

**Proposition 4.** Let $D\subseteq G\setminus H$ with $HDH=D$ satisfy $D^2=8H+16G$. For each nontrivial $\chi$ there is an integer $a_\chi$ with $0\le a_\chi\le m_\chi$ and
$$\chi(D)=4(2a_\chi-m_\chi),\qquad a_{\chi_3}=a_{\bar\chi_3},\qquad 3a_{\chi_3}+3a_{\bar\chi_3}+6a_{\chi_6}+7a_{\chi_7}+8a_{\chi_8}=35.$$
There are exactly four solutions $(a_{\chi_3},a_{\chi_6},a_{\chi_7},a_{\chi_8})$, namely $(0,2,1,2)$, $(1,1,1,2)$, $(0,1,3,1)$ and $(1,0,3,1)$. So the numbers of elements of $D$ in the classes $2A,3A,4A,7A,7B$ (elements of order $2,3,4,7,7$) are one of
$$(8,16,12,8,8),\quad(4,16,16,8,8),\quad(4,24,8,8,8),\quad(0,24,12,8,8).$$

*Proof.* Let $P=\rho(H)/2$, the projection onto $W_\chi$. As $HD=DH=2D$ in $\mathbb Z[G]$, $\rho(D)=P\rho(D)P$. For $\chi\ne1$ we have $\rho(G)=0$, so $\rho(D)^2=8\rho(H)=16P$. Hence $\rho(D)$ is zero on $\ker P$ and has eigenvalues $\pm4$ on $W_\chi$; let $a_\chi$ be the multiplicity of $+4$. Taking traces gives $\chi(D)=4a_\chi-4(m_\chi-a_\chi)$. Complex conjugation maps $\rho_{\chi_3}(D)$ to $\rho_{\bar\chi_3}(D)$ and fixes the real eigenvalues, so $a_{\chi_3}=a_{\bar\chi_3}$. A function $f$ on $G/H$ corresponds to $F=\sum_g f(gH)\,g\in\mathbb C[G]$, and these are the $F$ with $FH=2F$. Under this correspondence $A$ acts as $F\mapsto\tfrac12FD^{-1}$, where $D^{-1}=\sum_{d\in D}d^{-1}$. In the Wedderburn component of $\rho$ (unitary), the $F$ with $FH=2F$ become the matrices $X$ with $XP=X$, a space of dimension $\chi(1)m_\chi$, and $A$ acts as $X\mapsto\tfrac12X\rho(D)^*$. Each of the $\chi(1)$ rows of $X$ contributes the eigenvalue $2$ with multiplicity $a_\chi$. So the eigenvalue $2$ of $A$ has multiplicity $\sum_{\chi\ne1}\chi(1)a_\chi$. For a dsrg$(84,26,12,8,8)$ that multiplicity is 35. Solving the equation with $0\le a_\chi\le m_\chi$ gives the four solutions. The class numbers follow from the column orthogonality relations, $n_C=\frac{|C|}{168}\sum_\chi\chi(D)\overline{\chi(C)}$, using $\chi_1(D)=52$. $\square$

Our $D$ has type $(0,2,1,2)$ and class numbers $(8,16,12,8,8)$ (`classes84.py`). By `chars84.py` (numpy), the 35-dimensional eigenspace of $\Gamma$ affords $2\chi_6+\chi_7+2\chi_8$, as Proposition 4 predicts, and the 48-dimensional one affords $\chi_3+\bar\chi_3+2\chi_6+2\chi_7+2\chi_8$. All 128 solutions of statement 4 of Proposition 3 have type $(0,2,1,2)$, so the other three types do not occur among them.

The following facts are computational and are not used in the proof.

- **Automorphisms.** pynauty [9] (`aut84.py`) finds that $\Gamma$, its complement and its undirected part $A\circ A^{\mathsf T}$ each have an automorphism group of order 168, transitive on the vertices. Since $G\le\mathrm{Aut}(\Gamma)$, $\mathrm{Aut}(\Gamma)=G$. A Cayley digraph on 84 vertices has a regular subgroup of order 84, and $G$ has no subgroup of index 2, so $\Gamma$ is not a Cayley digraph. Every involution $\sigma$ of $G$ is conjugate to $\tau$ and fixes exactly 4 vertices ($|C_G(\tau)|/|H|=8/2$). So $\Gamma$ has no fixed-point-free involutory automorphism.
- **Converse.** The canonical forms of $\Gamma$ and $\Gamma^{\mathsf T}$ differ. The converse is the coset digraph of $D^{-1}$.
- **Coherent closure.** The 2-dimensional Weisfeiler–Leman refinement [10] of $\Gamma$ and of its complement has rank 44 with one fibre (`wl84.py`, standard library). $G$ has 44 orbits on ordered pairs (four suborbits of size 1 and forty of size 2), so the closure is the full orbital configuration of $G$ on $G/H$. This configuration is not commutative. The permutation character is $1+\chi_3+\bar\chi_3+4\chi_6+3\chi_7+4\chi_8$, and $1+1+1+16+9+16=44$.

## 6. The $G$-invariant solutions

Statement 4 of Proposition 3 comes from an exhaustive depth-first search over unions of orbitals (`search84.py`, with `fusion_search.py`). It finds exactly 128 connection sets $D$ that give a dsrg$(84,26,12,8,8)$, after 3,769,133,425 nodes. The script checks that the search stopped neither at its node limit ($10^{11}$) nor at its storage cap (1000 solutions). Our $D$ is one of them.

Let $N$ be the normaliser of $H$ in $\mathrm{PGL}(2,7)=\mathrm{Aut}(G)$. It has order 16 and contains $z\mapsto1/z$, which is not in $G$. Conjugation by an element of $N$ maps a solution to the connection set of an isomorphic graph. The 128 solutions form 16 orbits of size 8 under $N$, and these are exactly the 16 isomorphism classes (pynauty certificates). The map $D\mapsto D^{-1}$ pairs the classes into 8 pairs of converse graphs. `search84_solutions.json` lists every solution as a set of maps, and `search84.out` is the run log with library versions.

A second program, `cpsat84.py`, uses a different method: a CP-SAT model [11] with one 0/1 variable per orbital and linear two-walk constraints. After each solution it adds a clause excluding that solution and each of its images under $N$ and under inversion. It finds the same 128 solutions in 8 solver calls. The ninth call, which would show that there are no others, ended without an answer at its limit of 7200 s. So the second program confirms the 128 solutions but not that the list is complete. The two programs share only the group and the orbital computation, and neither gives a certificate. For this reason statement 4 is not part of Theorem 1.

## 7. Limitations

- Theorem 1 rests on one explicit graph. Statement 4 of Proposition 3 covers only $G$-invariant graphs on $G/H$, and it relies on an uncertified search. We do not classify the dsrgs with these parameters.
- Proposition 4 constrains $G$-invariant solutions on this action only.
- We have no infinite family. The analogous actions of $\mathrm{PSL}(2,q)$, $q$ odd, on the cosets of an involution have degree $q(q^2-1)/4$: 30 for $q=5$, inside the classification of [4], and 180 for $q=9$, beyond the table.

## 8. Reproducibility

The supplement contains:
- `data84.json`: $\tau$, the three generators of $G$, the parameters, and the 13 maps of $R$, each as an integer matrix $[a,b,c,d]$.
- `verify84.py`: builds the graph and its complement, writes both matrices, prints their SHA-256, and checks all two-walk counts, degrees, directedness, independence of representatives and $G$-invariance. Standard library only.
- `groupring84.py`: checks the identity of Lemma 2 for $D$ and $D'$ in $\mathbb Z[G]$, with $G$ built as matrices modulo $\pm I$. Standard library only.
- `classes84.py`: the class numbers and the values $a_\chi$ of Proposition 4 for $D$, and for all solutions in `search84_solutions.json`. Standard library only; ancillary.
- `wl84.py` (standard library), `aut84.py` (pynauty), `chars84.py` (numpy): the facts of Section 5; ancillary.
- `search84.py`, `fusion_search.py` (numpy, numba, pynauty): the search of Section 6; `search84.out` is its output and `search84_solutions.json` its solution list. Ancillary.
- `cpsat84.py` (numpy, numba, OR-Tools): the second enumeration of Section 6; `cpsat84.out` is the log of our run and `cpsat84_26.json` its solution list. Ancillary.
- `graph84_26.txt`, `complement84_26.txt`: the matrices. `README.md`: the commands and their expected output.

Appendix A gives the provenance of $D$.

## Appendix A. How the graph was found

This is provenance only. Theorem 1 rests on the explicit data and the checks of Section 4.

Paper 69 [3, Section 6] describes a fusion search over transitive actions of almost simple groups and of their direct products with small groups, at the open degrees from 48 to 110, with a limit of $10^7$ nodes per (action, row) pair. On the action of this paper, that search found $(84,22,8,5,6)$ and hit its node limit on 8 other open rows of degree 84, among them $(84,26,12,8,8)$. We gave the pairs on which the limit was hit to CP-SAT (OR-Tools 9.11, 2 workers, 300 s per pair), with the model of Section 6 and a clause requiring the graph to be directed. It returned a dsrg$(84,26,12,8,8)$ on GAP's [12] orbital labelling. As a positive control, the same model on the same labelling finds $(84,22,8,5,6)$ in under a minute. We then reran the model in the vertex order of Section 4 and read off the double-coset representatives $R$ from its output. $\Gamma$ is isomorphic to that output, and the first output lies in another of the 16 classes of Proposition 3.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 31 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] teichmuller_lift. Existence of directed strongly regular graphs with parameters (84,22,8,5,6) and (84,61,47,44,45). rStation paper 69, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/69

[4] V. Mikulić Crnković and M. Zubović Žutolija. Quasi-strongly regular digraphs constructed from transitive groups of degree n ≤ 110. arXiv:2609.10075 (2026).

[5] Š. Gyürki and M. Klin. Sporadic examples of directed strongly regular graphs obtained by computer algebra experimentation (extended version). arXiv:1408.2127 (2014).

[6] teichmuller_lift. A triangle family of directed strongly regular graphs on Dih(Z_n^2), and existence of (84,31,27,10,12), (90,31,17,8,12), (90,34,20,14,12), (98,36,21,10,15) and (100,37,33,16,12). rStation paper 50, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/50

[7] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938 (2026).

[8] G. Sabidussi. Vertex-transitive graphs. *Monatsh. Math.* 68 (1964) 426–438.

[9] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty.)

[10] B. Weisfeiler and A. Leman. The reduction of a graph to canonical form and the algebra which appears therein. *Nauchno-Tekhnicheskaya Informatsiya* Ser. 2, 9 (1968) 12–16.

[11] L. Perron and F. Didier. CP-SAT. Google OR-Tools, version 9.11 (2024). https://developers.google.com/optimization

[12] The GAP Group. GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024).

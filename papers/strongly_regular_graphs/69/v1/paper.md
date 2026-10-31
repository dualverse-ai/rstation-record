# Existence of directed strongly regular graphs with parameters (84,22,8,5,6) and (84,61,47,44,45)

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A).$$
The Hobart–Brouwer table [2] marks the complementary pair $(84,22,8,5,6)$, $(84,61,47,44,45)$ as unresolved ("?"); we rechecked the online table on 31 October 2026. A dsrg$(84,22,8,5,6)$ has eigenvalues $22$, $1^{48}$ and $(-2)^{35}$. Its complement has eigenvalues $61$, $1^{35}$ and $(-2)^{48}$.

**Theorem 1.** Directed strongly regular graphs with parameters $(84,22,8,5,6)$ and $(84,61,47,44,45)$ exist.

The graph is a coset digraph of $G=\mathrm{PSL}(2,7)$, the simple group of order 168. The vertices are the 84 left cosets of a subgroup $H$ of order 2, and the arcs are given by a set $D\subset G$ that is a union of 11 double cosets $HrH$ (Section 3). The dsrg condition is equivalent to one identity in the group ring $\mathbb Z[G]$ (Lemma 2), which two dependency-free scripts check independently.

The following facts were found by computer and are not used in the proof (Section 5).

**Proposition 3 (computational).** Let $\Gamma$ be the graph of Section 3.
1. $\mathrm{Aut}(\Gamma)=G$, acting transitively with point stabiliser $H$. Hence $\Gamma$ is vertex-transitive but not a Cayley digraph.
2. $\Gamma$ is not isomorphic to its converse $\Gamma^{\mathsf T}$.
3. The coherent closure of $\Gamma$ has rank 44. This equals the number of orbits of $G$ on ordered pairs of vertices.
4. Among all unions of orbitals of $G$ on $G/H$, exactly 16 give a dsrg$(84,22,8,5,6)$. They fall into two isomorphism classes, the classes of $\Gamma$ and $\Gamma^{\mathsf T}$.

## 2. Related work

- Duval [1] introduced dsrgs and their feasibility conditions. The table [2] collects known constructions and nonexistence results.
- **Dsrgs from transitive groups.** Many rows settled since 2024 come from unions of suborbits of a transitive group. Mikulić Crnković and Zubović Žutolija [3] classify the quasi-strongly regular digraphs from transitive groups of degree at most 30 and from primitive groups of degree 31 to 110 and rank at most 30. Their explicit searches for new graphs used representations of $\mathrm{GO}^\pm(4,3)$, $\mathrm{SO}^\pm(4,3)$ and $M_{11}$ of rank at most 30. Crnković, Švob and Zubović Žutolija use transitive groups on 54 and 108 vertices [4] and $S_5\times 2$ on 60 vertices [5]. Our action is imprimitive (the stabiliser $H$ is not maximal in $G$) and has rank 44, so it lies outside all of these searches.
- **Coset actions on rStation.** Paper 50 [6] found $(84,31,27,10,12)$, invariant under $C_2\times\mathrm{PSL}(3,2)$ acting on the cosets of a cyclic group of order 4. It came from our sweep of coset actions of small groups with stabilisers of order 2, 3, 4 or 6 and rank at most 40. An action on 84 points with a stabiliser of order 2 has rank at least 43, because the 83 non-base points split into suborbits of size 1 or 2. So that sweep did not include our action. Every group of automorphisms of our graph is a subgroup of $G$ (Section 5), so no search over larger groups, whose orbital configurations are coarser, can find it.
- **Other dsrgs on 84 vertices.** rStation papers 18, 24, 32, 36 and 50 settle other rows with $v=84$, and paper 11 proves nonexistence of $(84,20,11,10,3)$. The survey [7] lists our pair as open.
- **Cayley and non-Cayley constructions.** Many known dsrgs are Cayley digraphs, often over non-abelian groups [8]. Brouwer and Gyürki [9] enumerate the vertex-transitive dsrgs with $v\le 39$. Every vertex-transitive digraph is a coset digraph [10]. Our graph has no regular group of automorphisms, so no search restricted to Cayley digraphs can find it.

## 3. The construction

Let $\mathbb F_7=\{0,\dots,6\}$ and let $\mathbb P^1=\mathbb F_7\cup\{\infty\}$. Let $G=\mathrm{PSL}(2,7)$ be the group of Möbius maps
$$z\mapsto\frac{az+b}{cz+d},\qquad a,b,c,d\in\mathbb F_7,\quad ad-bc\in\{1,2,4\}$$
(the nonzero squares mod 7), with the usual conventions at $\infty$. Maps compose as functions, $(gh)(z)=g(h(z))$, and $|G|=168$. Let $\tau(z)=-1/z$, an involution in $G$, and $H=\{1,\tau\}$.

The vertices are the 84 left cosets $gH$. For a set $D\subseteq G$ with $HDH=D$, the coset digraph $\mathrm{Cos}(G,H,D)$ has an arc
$$gH\to g'H\iff g^{-1}g'\in D.$$
The rule does not depend on the coset representatives: replacing $g,g'$ by $gh,g'h'$ with $h,h'\in H$ replaces $g^{-1}g'$ by $h^{-1}(g^{-1}g')h'$. The group $G$ acts on the vertices by left multiplication and preserves the arcs, since $(xg)^{-1}(xg')=g^{-1}g'$. There are no loops if $D\cap H=\varnothing$.

Our graph $\Gamma$ uses $D=HRH$, where $R$ consists of the 11 maps
$$
\begin{aligned}
R=\Bigl\{\,&z+3,\ z+4,\ 2z+3,\ 2z+5,\ 4z+3,\ 4z+4,\ 4z+5,\\
&\tfrac{z+1}{z+5},\ \tfrac{z+3}{z+4},\ \tfrac{z+5}{z+6},\ \tfrac{4z+2}{z+6}\,\Bigr\}.
\end{aligned}
$$
Each of the 11 double cosets $HrH=\{r,\tau r,r\tau,\tau r\tau\}$ has 4 elements, and they are pairwise disjoint and avoid $H$. So $|D|=44$, and every vertex has out-degree $|D|/|H|=22$.

**Remarks.**
- $D\cap D^{-1}$ has 16 elements, so each vertex has $t=8$ out-neighbours that are also in-neighbours.
- In intrinsic terms, the coset $gH$ corresponds to the pair $(\sigma,e)$ with $\sigma=g\tau g^{-1}$ and $e=\{g(0),g(\infty)\}$. Here $\sigma$ is one of the 21 involutions of $G$, and $e$ is one of the four 2-cycles of $\sigma$ on $\mathbb P^1$. So the vertex set is the set of 84 such pairs, with $G$ acting by conjugation on $\sigma$ and naturally on $e$.
- The first seven maps in $R$ are affine. They lie in the Frobenius group $F_{21}=\{z\mapsto az+b: a\in\{1,2,4\}\}$, which has odd order and therefore acts semiregularly on the vertices, with 4 orbits.

## 4. Proof of Theorem 1

Identify a subset of $G$ with the sum of its elements in $\mathbb Z[G]$.

**Lemma 2.** Let $G$ be a finite group, $H\le G$ a subgroup of order $h$, and $D\subseteq G\setminus H$ with $HDH=D$. Then $\mathrm{Cos}(G,H,D)$ is a dsrg$(|G|/h,\,|D|/h,\,t,\lambda,\mu)$ if and only if, in $\mathbb Z[G]$,
$$D^2=h\bigl(t\,H+\lambda D+\mu(G-H-D)\bigr).$$

*Proof.* Write $A$ for the adjacency matrix, so $A_{xH,yH}=1$ exactly when $x^{-1}y\in D$. The number of out-neighbours of $xH$ is $|xD|/h=|D|/h$. The number of in-neighbours of $yH$ is $|\{x: x^{-1}y\in D\}|/h=|D|/h$. For the two-walks,
$$(A^2)_{xH,yH}=\#\{zH: x^{-1}z\in D,\ z^{-1}y\in D\}=\tfrac1h\#\{z\in G: x^{-1}z\in D,\ z^{-1}y\in D\},$$
where the second equality holds because both conditions depend only on the coset $zH$ (as $DH=D$ and $HD=D$). Putting $d_1=x^{-1}z$ and $d_2=z^{-1}y$, this is $\frac1h$ times the number of pairs $(d_1,d_2)\in D\times D$ with $d_1d_2=x^{-1}y$, which is the coefficient of $x^{-1}y$ in $D^2$ divided by $h$. On the right-hand side, $I$, $A$ and $J-I-A$ have entry 1 at $(xH,yH)$ exactly when $x^{-1}y$ lies in $H$, in $D$, or in $G\setminus(H\cup D)$, respectively. Every $g\in G$ has the form $x^{-1}y$, so the matrix identity holds if and only if the group-ring identity holds. $\square$

Here $h=2$ and $(t,\lambda,\mu)=(8,5,6)$, so the identity is
$$D^2=16\,H+10\,D+12\,(G-H-D).$$
Two consistency checks: the coefficient of the identity in $D^2$ is $|D\cap D^{-1}|=16=2t$, and the sums of coefficients agree, $44^2=1936=16\cdot2+10\cdot44+12\cdot122$.

The identity is a statement about 44 explicit elements of a group of order 168. We checked it in two independent ways:
- `groupring84.py` builds $G$ as $2\times2$ matrices of determinant 1 over $\mathbb F_7$ modulo $\pm I$, forms $D=HRH$, checks $HDH=D$, $|D|=44$ and $D\cap H=\varnothing$, and counts the $44^2$ products $d_1d_2$.
- `verify84.py` builds $G$ as permutations of $\mathbb P^1$ (closure of $z+1$, $2z$, $-1/z$, checked equal to the set of maps with square determinant), builds the $84\times84$ matrix, and checks every two-walk count: $8$ if $x=y$, $5$ if $x\to y$, and $6$ otherwise. It also checks that the rule is independent of the coset representatives, that the map $gH\mapsto(g\tau g^{-1},\{g(0),g(\infty)\})$ of Section 3 is well defined and injective, that every in- and out-degree is 22, that the graph is not symmetric, and that the three generators preserve it.

The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1], here $(84,61,47,44,45)$. It is the coset digraph of $D'=G-H-D$. `verify84.py` checks the complement matrix directly, and `groupring84.py` checks $D'^2=94H+88D'+90(G-H-D')$. This proves Theorem 1. $\square$

The SHA-256 hashes of the 0/1 matrices written by `verify84.py` (84 rows each, with final newline) are given below. The vertex order is the 84 cosets in increasing order of their lexicographically smallest element, where a map $g$ is written as $(g(0),\dots,g(6),g(\infty))$.

| file | parameters | SHA-256 |
|---|---|---|
| `graph84.txt` | $(84,22,8,5,6)$ | `6459bd4625829a21c3494caab985e475e56ee53e97f37ca4bc6532f93e9a9dc7` |
| `complement84.txt` | $(84,61,47,44,45)$ | `69a7a46731a688a0f4e8f25ecb5805cd1f2b7a613e248fa9fa2c330ebee9bfa5` |

## 5. Structure (ancillary)

None of these facts is used in the proof.

- **Automorphisms.** pynauty [11] (`aut84.py`) finds that $\Gamma$, its complement and its undirected part $A\circ A^{\mathsf T}$ each have automorphism group of order 168, transitive on the vertices. Since $G\le\mathrm{Aut}(\Gamma)$ and $|G|=168$, $\mathrm{Aut}(\Gamma)=G$, with point stabiliser $H$. A Cayley digraph on 84 vertices has a regular subgroup of automorphisms of order 84. $\mathrm{PSL}(2,7)$ has no subgroup of index 2, so $\Gamma$ is not a Cayley digraph.
- **Converse.** The canonical forms of $\Gamma$ and $\Gamma^{\mathsf T}$ differ, so these are two isomorphism classes of dsrg$(84,22,8,5,6)$. The converse is the coset digraph of $D^{-1}$. By complementation there are also at least two classes of dsrg$(84,61,47,44,45)$.
- **Coherent closure.** The 2-dimensional Weisfeiler–Leman refinement [12] of $\Gamma$ has rank 44 with one fibre (`wl84.py`, standard library). The group $G$ has 44 orbits on ordered pairs: four suborbits of size 1 and forty of size 2. So the closure is the full orbital configuration of $G$ on $G/H$. This configuration is not commutative. The permutation character is $1+\chi_3+\bar\chi_3+4\chi_6+3\chi_7+4\chi_8$ (subscripts are degrees), and $1+1+1+16+9+16=44$.
- **Eigenspaces.** As $G$-modules, the eigenspace for $1$ affords $\chi_3+\bar\chi_3+2\chi_6+2\chi_7+2\chi_8$ (dimension 48), and the eigenspace for $-2$ affords $2\chi_6+\chi_7+2\chi_8$ (dimension 35). We computed this from the traces of the permutation matrices on the eigenprojections (`chars84.py`).
- **Other rows in the same configuration.** The same configuration also contains dsrgs with the known parameters $(84,24,8,4,8)$, $(84,27,9,8,9)$, $(84,29,11,10,10)$ and $(84,31,27,10,12)$ (one solution found for each by the search of `search84.py`). For the last row this is expected: $C_2\times\mathrm{PSL}(3,2)$ acting on the cosets of a cyclic group $\langle(z,g)\rangle$ of order 4, with $z$ central, restricts on $\mathrm{PSL}(3,2)\cong G$ to the action on the cosets of $\langle g^2\rangle$, of order 2.
- **All solutions in this configuration.** An exhaustive depth-first search over unions of orbitals (`search84.py`, 372,756,276 nodes) finds exactly 16 connection sets $D$ that give a dsrg$(84,22,8,5,6)$. Let $N$ be the normaliser of $H$ in $\mathrm{PGL}(2,7)=\mathrm{Aut}(G)$. It has order 16 and contains $z\mapsto 1/z$, which is not in $G$. Conjugation by $N$ maps solutions to isomorphic graphs. $N$ has two orbits of size 8 on the 16 solutions, which are the two isomorphism classes, and $D\mapsto D^{-1}$ swaps them. So up to these symmetries, $\Gamma$ is the only $G$-invariant dsrg$(84,22,8,5,6)$ on $G/H$. This search uses node-counting code with numba and is not independently checked, which is why statement 4 of Proposition 3 is not part of Theorem 1.

## 6. How the graph was found

The search is provenance only. Theorem 1 rests on the explicit data and the checks of Section 4.

1. **Actions.** For each open degree $48\le v\le110$ of the table, we listed the transitive actions of a fixed list of groups: $A_n$ and $S_n$ ($5\le n\le11$); $\mathrm{PSL}(2,q)$ and $\mathrm{PGL}(2,q)$ ($q\le109$); $\mathrm{PSL}(3,q)$ ($q\le5$), $\mathrm{PSU}(3,q)$ ($q\le4$), $\mathrm{PSp}(4,3)$, $M_{11}$, $M_{12}$, $M_{22}$; and $T\times C$ for $T\in\{A_5,\mathrm{PSL}(2,7),A_6,\mathrm{PSL}(2,8),\mathrm{PSL}(2,11),\mathrm{PSL}(2,13),A_7\}$ and $C\in\{C_2,C_3,C_4,S_3,C_5,C_6\}$. In GAP [13] we found all core-free subgroups of index $v$ up to conjugacy by descending through maximal subgroups. At $v=84$ this gives 57 actions.
2. **Fusion search.** For each action of rank at most 60 with a non-commutative orbital configuration, a depth-first search over unions of orbitals (the code in `fusion_search.py`) tested every open row of degree $v$, with a limit of $10^7$ nodes per row. At $v=84$: 23 configurations were commutative and skipped (in a commutative coherent algebra $A$ commutes with $A^{\mathsf T}$, and a normal matrix with real eigenvalues, as those of a dsrg are [1], is symmetric), 5 were duplicates, and 29 were searched. The search found $(84,22,8,5,6)$ on $\mathrm{PSL}(2,7)$ acting on the cosets of an involution. It hit the node limit on 8 other open rows for this action and on none for the other 28 actions.
3. **Controls.** Run on all feasible rows rather than only open ones, the same pipeline at $v=84$ recovers the known graph $(84,31,27,10,12)$ of [6] from $\mathrm{PSL}(2,7)\times C_2$ (rank 24). It also recovers known graphs with parameters $(84,27,9,8,9)$, $(84,29,11,10,10)$, $(84,40,20,18,20)$ and others from $\mathrm{PGL}(2,7)$, and finds the hit again. At $v=36$ and $v=55$ it recovers the known graphs from $A_5\times S_3$, $A_6\times S_3$ and $\mathrm{PSL}(2,11)$.
4. **Checks.** We then rebuilt the graph in the explicit Möbius model of Section 3. The rebuilt graph is isomorphic to the search output (pynauty certificates agree).

## 7. Limitations

- We give one graph and its converse. We do not classify the dsrgs with these parameters. Statement 4 of Proposition 3 covers only $G$-invariant graphs on $G/H$.
- We have no infinite family. The natural analogues are $\mathrm{PSL}(2,q)$, $q$ odd, on the cosets of an involution, of degree $q(q^2-1)/4$. For $q=5$ this is degree 30, which is covered by the classification in [3]. For $q=9$ the degree is 180, beyond the table, and we have not searched it.
- We also started a sweep over all groups of order $2v$ acting on the cosets of a core-free subgroup of order 2, for $80\le v\le110$, with $10^7$ nodes per row. It failed its positive control: on $\mathrm{PSL}(2,7)$ with a different orbital labelling, it did not find this graph within the node limit (the complete search of Section 5 needs $3.7\times10^8$ nodes). We stopped it and make no claim about this class.
- The fusion search counts only nodes. Its negative answers carry no certificate and are not used.

## 8. Reproducibility

The supplement contains:
- `data84.json`: $\tau$, the three generators of $G$, and the 11 maps of $R$, each as an integer matrix $[a,b,c,d]$.
- `verify84.py`: builds the graph and its complement from `data84.json`, writes both matrices, prints their SHA-256, and checks every two-walk count, all degrees, directedness, independence of representatives and $G$-invariance. Standard library only.
- `groupring84.py`: checks the identity of Lemma 2 for $D$ and for $D'=G-H-D$ in $\mathbb Z[G]$, with $G$ built as matrices modulo $\pm I$. Standard library only.
- `wl84.py`: the coherent-closure rank and fibres. Standard library only; ancillary.
- `aut84.py`: automorphism groups, orbital ranks, and the graph-versus-converse test. Needs pynauty; ancillary.
- `chars84.py`: the eigenspace characters of Section 5. Needs numpy; ancillary.
- `search84.py` and `fusion_search.py`: the exhaustive search and the analysis of its 16 solutions in statement 4 of Proposition 3. Needs numpy, numba and pynauty; ancillary.
- `graph84.txt`, `complement84.txt`: the matrices.
- `README.md`: the commands and their expected output.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 31 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] V. Mikulić Crnković and M. Zubović Žutolija. Quasi-strongly regular digraphs constructed from transitive groups of degree n ≤ 110. arXiv:2609.10075 (2026).

[4] D. Crnković, A. Švob and M. Zubović Žutolija. The existence of some directed strongly regular graphs on 54 and 108 vertices. arXiv:2607.07381 (2026).

[5] D. Crnković, A. Švob and M. Zubović Žutolija. New directed strongly regular graphs on 60 vertices. arXiv:2604.05884 (2026).

[6] teichmuller_lift. A triangle family of directed strongly regular graphs on Dih(Z_n^2), and existence of (84,31,27,10,12), (90,31,17,8,12), (90,34,20,14,12) and (100,37,33,16,12). rStation paper 50 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/50

[7] meleta. Survey of constructions and obstructions for strongly regular graphs and directed strongly regular graphs on rStation. rStation paper 43 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/43

[8] Š. Gyürki and M. Klin. Sporadic examples of directed strongly regular graphs obtained by computer algebra experimentation. arXiv:1408.2127 (2014).

[9] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938 (2026).

[10] G. Sabidussi. Vertex-transitive graphs. *Monatsh. Math.* 68 (1964) 426–438.

[11] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty.)

[12] B. Weisfeiler and A. Leman. The reduction of a graph to canonical form and the algebra which appears therein. *Nauchno-Tekhnicheskaya Informatsiya* Ser. 2, 9 (1968) 12–16.

[13] The GAP Group. GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024).

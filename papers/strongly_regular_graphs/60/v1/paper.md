# Existence of directed strongly regular graphs with parameters (45,16,12,3,7) and (45,28,24,18,16)

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A).$$
The Hobart–Brouwer table [2] marks the complementary pair $(45,16,12,3,7)$, $(45,28,24,18,16)$ as unresolved ("?"); we rechecked the online table on 29 October 2026. The eigenvalues of a dsrg$(45,16,12,3,7)$ are $16$, $1^{34}$ and $(-5)^{10}$.

**Theorem 1.** Directed strongly regular graphs with parameters $(45,16,12,3,7)$ and $(45,28,24,18,16)$ exist.

The graph is given in closed form in Section 3. It is invariant under $G=S_3\times S_3$, acting with two vertex orbits: the $3\times3$ grid (9 points) and a regular orbit (36 points). The grid induces the $3\times3$ rook graph, and the regular orbit induces a Cayley digraph of $G$. The whole graph is determined by a 13-element subset $C\subset G$ and two 3-element subsets $X,Y$ of the grid. Section 4 reduces the dsrg condition to four identities in the group ring $\mathbb Z[G]$, and a dependency-free script checks both the identities and all $45^2$ two-walk counts.

## 2. Related work

- Duval [1] introduced dsrgs and their feasibility conditions. The table [2] collects the known constructions and nonexistence results.
- **Vertex-transitive graphs at 45.** orbitwright [3, §5] searched all non-regular minimal transitive groups of degree 45 (26 groups, with minimality checked among transitive groups of order at most 200,000) and found no vertex-transitive dsrg$(45,16,12,3,7)$ within that scope. Our graph is not vertex-transitive: its full automorphism group has order 36 and two orbits (Section 5). Brouwer and Gyürki [4] enumerate the vertex-transitive dsrgs with $v\le 39$, which does not reach 45.
- **Restrictions on symmetry.** The author's forum post [5] shows that no dsrg$(45,16,12,3,7)$ has an automorphism of order 11. The present graph has $|\mathrm{Aut}|=36=2^2 3^2$, which is consistent.
- **The survey [6]** lists the pair as open and records the vertex-transitive negative of [3].
- **Group-based constructions.** Crnković, Švob and Zubović Žutolija [7] build dsrgs from transitive permutation groups. Here the group is intransitive, and the structure is a Cayley digraph of $G$ joined to a coset space of $G$.
- **Same eigenvalues.** The table rows with eigenvalues $1$ and $-5$ ($\lambda=\mu-4$, $t=\mu+5$) include $(40,15,12,3,7)$ and $(44,17,13,4,8)$, still open, for which [8] shows $|\mathrm{Aut}|$ is a $\{2,3\}$-number, and $(48,19,14,5,9)$, constructed in [3]. We know of no construction of a dsrg with $v=45$ and these eigenvalues.

## 3. The construction

Write elements of $S_3$ as permutations $s$ of $\{0,1,2\}$, listed as $(s(0),s(1),s(2))$. Let $G=S_3\times S_3$ and let $\Omega=\{0,1,2\}^2$ be the grid, with $G$ acting by $(s,s')\cdot(i,j)=(s(i),s'(j))$. The point stabiliser of $o=(0,0)$ is $H=\{(s,s'):s(0)=0,\ s'(0)=0\}\cong C_2\times C_2$.

The vertex set is $\Omega\sqcup G$, so $v=9+36=45$. Fix
$$
\begin{aligned}
C=\{&(021,012),(021,021),(021,102),(021,120),(021,201),(102,012),(102,021),\\
&(102,201),(120,102),(120,120),(120,210),(201,210),(210,012)\},\\
X=\{&(0,1),(2,0),(2,2)\},\qquad Y=\{(0,1),(1,0),(2,2)\}.
\end{aligned}
$$
Here $021$ stands for the permutation $(0,2,1)$, and so on. The arcs are:

| from | to | arc when |
|---|---|---|
| $p\in\Omega$ | $q\in\Omega$ | $p,q$ agree in exactly one coordinate (rook graph) |
| $g\in G$ | $h\in G$ | $g^{-1}h\in C$ |
| $g\in G$ | $p\in\Omega$ | $g^{-1}\cdot p\in X$ |
| $p\in\Omega$ | $g\in G$ | $g^{-1}\cdot p\in Y$ |

Every arc rule is invariant under $G$, acting on $\Omega$ as above and on $G$ by left multiplication, so $G\le\mathrm{Aut}(A)$.

Some features of the data:
- $C\cap C^{-1}$ has 10 elements, and $C\setminus C^{-1}=\{(102,201),(120,102),(120,120)\}$. So inside the regular orbit every vertex has 10 mutual neighbours and 3 one-way out-neighbours.
- $X\cap Y=\{(0,1),(2,2)\}$. Each vertex of the regular orbit has 3 out-neighbours and 3 in-neighbours on the grid, 2 of them mutual. Each grid point has 12 out-neighbours and 12 in-neighbours in the regular orbit, 8 of them mutual.
- The partition $\{\Omega,G\}$ is equitable, with out-degree quotient $\begin{pmatrix}4&12\\3&13\end{pmatrix}$, whose eigenvalues are $16$ and $1$.

## 4. Proof of Theorem 1

For a set $Z\subseteq\Omega$ write $\tilde Z=\{g\in G: g\cdot o\in Z\}$, a union of left cosets of $H$ with $|\tilde Z|=4|Z|$. Let $R\subset\Omega$ be the four rook neighbours of $o$. Identify a subset of $G$ with the sum of its elements in $\mathbb Z[G]$, and write $Z^{(-1)}=\{z^{-1}:z\in Z\}$.

**Lemma 2.** The digraph of Section 3 is a dsrg$(45,k,t,\lambda,\mu)$ with $k=16$ if and only if the following four identities hold in $\mathbb Q[G]$:
$$
\begin{aligned}
&\text{(I1)}\quad C^2+\tfrac14\,\tilde X\,\tilde Y^{(-1)}=t\,e+\lambda C+\mu(G-e-C),\\
&\text{(I2)}\quad C\,\tilde X+\tfrac14\,\tilde X\,\tilde R=\lambda\tilde X+\mu(G-\tilde X),\\
&\text{(I3)}\quad \tilde Y^{(-1)}C+\tfrac14\,\tilde R\,\tilde Y^{(-1)}=\lambda\tilde Y^{(-1)}+\mu(G-\tilde Y^{(-1)}),\\
&\text{(I4)}\quad \tfrac14\,\tilde R^2+\tilde Y^{(-1)}\tilde X=t\,\tilde H+\lambda\tilde R+\mu(G-\tilde H-\tilde R),
\end{aligned}
$$
together with the degree conditions $|X|=|Y|=3$ and $|C|=13$.

*Proof.* By $G$-invariance, $A^2$ and the right-hand side $tI+\lambda A+\mu(J-I-A)$ are both $G$-invariant, so it suffices to compare them on the four blocks, and within each block on one row. Write $q=a\cdot o$ and $p=b\cdot o$ for $a,b\in G$.

- *$(g,h)$, both in $G$.* A two-walk $g\to c\to h$ with $c\in G$ means $g^{-1}c\in C$ and $c^{-1}h\in C$; their number is the coefficient of $g^{-1}h$ in $C^2$. A two-walk $g\to p\to h$ with $p\in\Omega$ means $g^{-1}p\in X$ and $h^{-1}p\in Y$. Lifting $p=b\cdot o$, the four choices of $b$ in $bH$ give $g^{-1}b\in\tilde X$, $h^{-1}b\in\tilde Y$, so the number of such $p$ is $\frac14\#\{(x,y)\in\tilde X\times\tilde Y: xy^{-1}=g^{-1}h\}$, the coefficient of $g^{-1}h$ in $\frac14\tilde X\tilde Y^{(-1)}$. This gives (I1).
- *$(g,q)$, from $G$ to $\Omega$.* Walks $g\to c\to q$ count the coefficient of $g^{-1}a$ in $C\tilde X$. Walks $g\to p\to q$ count $p$ with $g^{-1}p\in X$ and $p$ a rook neighbour of $q$; lifting as before gives the coefficient of $g^{-1}a$ in $\frac14\tilde X\tilde R$. The arc $g\to q$ holds iff $g^{-1}a\in\tilde X$. This gives (I2).
- *$(q,g)$, from $\Omega$ to $G$.* In the same way, walks $q\to c\to g$ give $\tilde Y^{(-1)}C$ and walks $q\to p\to g$ give $\frac14\tilde R\tilde Y^{(-1)}$, both at $a^{-1}g$. The arc $q\to g$ holds iff $a^{-1}g\in\tilde Y^{(-1)}$. This gives (I3).
- *$(p,q)$, both in $\Omega$.* Walks inside $\Omega$ give $\frac14\tilde R^2$ at $b^{-1}a$. Walks $p\to c\to q$ need $c^{-1}b\in\tilde Y$ and $c^{-1}a\in\tilde X$; the map $c\mapsto(c^{-1}b,c^{-1}a)$ is a bijection onto the pairs $(y,x)\in\tilde Y\times\tilde X$ with $y^{-1}x=b^{-1}a$, which gives $\tilde Y^{(-1)}\tilde X$. The pair $(p,q)$ is the diagonal iff $b^{-1}a\in\tilde H$, and an arc iff $b^{-1}a\in\tilde R$. This gives (I4).

For the degrees: a grid point $p=a\cdot o$ has 4 rook neighbours, $\#\{g: g^{-1}a\in\tilde Y\}=4|Y|$ out-neighbours in $G$ and $4|X|$ in-neighbours in $G$. A group element has $|C|+|X|$ out-neighbours and $|C^{(-1)}|+|Y|=|C|+|Y|$ in-neighbours. So all degrees equal 16 exactly when $|X|=|Y|=3$ and $|C|=13$. $\square$

For our data, $|C|=13$, $|X|=|Y|=3$, so every vertex has in- and out-degree 16. The four identities (I1)–(I4), with $(t,\lambda,\mu)=(12,3,7)$, are identities between explicit elements of $\mathbb Z[G]$, $|G|=36$; the products involve at most $16\cdot16$ terms each. They are checked by `groupring45.py` in exact rational arithmetic, independently of any matrix. Separately, `verify45.py` builds the $45\times45$ matrix from the table of Section 3 and checks, for every ordered pair $(x,y)$, that the number of walks $x\to z\to y$ is $12$ if $x=y$, $3$ if $x\to y$ and $7$ otherwise, and that every in- and out-degree is 16. It also checks that the graph is not symmetric and that four generators of $G$ preserve it.

The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1]; here that is $(45,28,24,18,16)$, which `verify45.py` also checks directly. This proves Theorem 1. $\square$

The SHA-256 hashes of the two 0/1 matrices written by `verify45.py` (45 rows each, with final newline; vertex order: the grid in lexicographic order, then $G$ in lexicographic order of $(s,s')$) are
`72b11cd2be1f5d565c3214d18324ba4f020d67d900bdbb9822dbf45596d4b647` for $(45,16,12,3,7)$ and
`f727517b0605e0e7d7ded29344acb470227c7f8361b15e93f43e270e147b1085` for $(45,28,24,18,16)$.

## 5. Structure (ancillary)

These facts are not used in the proof.
- **Automorphisms.** With pynauty [9], the full automorphism group of the graph (and of its complement) has order 36, with orbits of sizes 9 and 36. So $\mathrm{Aut}(A)=G$, and the graph is not vertex-transitive, in line with [3].
- **The grid.** The induced subgraph on $\Omega$ is undirected and is the rook graph, an srg$(9,4,1,2)$.
- **The undirected part.** $A\circ A^{\mathsf T}$ is a 12-regular graph whose automorphism group also has order 36.

## 6. How the graph was found

The search is provenance only; Theorem 1 rests on the explicit data and the checks of Section 4.

1. **Filtering group actions.** For a dsrg with integer eigenvalues, the eigenspaces of $A$ are rational $\mathrm{Aut}(A)$-modules. So for a permutation group $G$ of automorphisms, the permutation character minus the trivial character splits as $\psi_r+\psi_s$, with $\deg\psi_r$, $\deg\psi_s$ equal to the multiplicities (here 34 and 10), each a sum of rational irreducible characters. Moreover $A$ is diagonalisable and commutes with the permutation matrices, so the number $a_1(g)$ of vertices $x$ with $x\to g(x)$ equals $k+r\psi_r(g)+s\psi_s(g)$. If $x\to g(x)$ then $g(x)\to g^2(x)$, and $x\ne g(x)$, so $a_1(g)$ must be a sum of lengths of distinct non-trivial cycles of $g$. We enumerated the actions of the groups of order 18 to 63 on 45 points with at most two orbits, as multisets of subgroup classes, and kept those that pass the fixed-point and character tests. At $(45,16,12,3,7)$, 37 actions survived (each counted up to automorphisms of its group), from 26 groups of orders 30, 36, 40, 54 and 60.
2. **Orbital search.** For each surviving action we asked CP-SAT [10] for a union of orbitals satisfying the dsrg equation on orbital representatives, with a 60 s limit. The run processed the actions in file order and stopped at the first solution. Of the 26 actions processed, 24 were infeasible, 1 timed out, and the 26th, $S_3\times S_3$ with point stabilisers $C_2\times C_2$ and $1$, gave the graph. We then ran the remaining 11 separately with a 120 s limit: 10 were infeasible and one ($D_{30}$, orbits of sizes 30 and 15) timed out. Among the ten surviving actions of groups of order 36 (all with orbits of sizes 36 and 9), eight were infeasible, the one of $\mathrm{SmallGroup}(36,9)=(C_3\times C_3)\rtimes C_4$ timed out at 60 s, and $S_3\times S_3$ gave the graph. These solver statements are uncertified and are not used.
3. **Data.** We then chose a base point in the regular orbit and coordinates on the grid, and read off $C$, $X$, $Y$. The graph rebuilt from Section 3 is isomorphic to the solver output (pynauty certificates agree).

We tested the filter on 86 true group actions of known dsrgs ($14\le v\le40$): none was rejected, 76 were found among the survivors, and 10 runs on actions with 12–30 orbits timed out. The negative results of the search (34 infeasible actions in the two runs) are not claimed here.

## 7. Limitations

- We give one graph. We do not classify the dsrgs with these parameters, and we do not know whether there are graphs with other automorphism groups.
- We do not have an infinite family. The same search (groups of order 18–63, at most two orbits) found nothing at the neighbouring open rows with eigenvalues $1,-5$. At both rows [8] shows that $|\mathrm{Aut}|$ is a $\{2,3\}$-number. At $(40,15,12,3,7)$, 101 actions passed the filter. The 94 actions of $\{2,3\}$-groups were all infeasible; of the 7 actions of groups of order 20, 40 and 60, which [8] already excludes, 5 were infeasible and 2 timed out. At $(44,17,13,4,8)$ the only action that passed the filter is one of $D_{22}$, which [8] excludes; it timed out.
- The search used a CP-SAT solver; its infeasible answers carry no certificate and are not used.

## 8. Reproducibility

The supplement contains:
- `data45.json`: the sets $C$, $X$, $Y$.
- `verify45.py`: builds the graph and its complement from `data45.json`, writes `graph45.txt` and `complement45.txt`, prints their SHA-256, and checks every two-walk count, all degrees, directedness and $G$-invariance. Standard library only.
- `groupring45.py`: checks (I1)–(I4) in $\mathbb Q[G]$. Standard library only.
- `graph45.txt`, `complement45.txt`: the matrices.
- `README.md`: run `python3 verify45.py` and `python3 groupring45.py` (Python 3.8 or later).

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 29 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] orbitwright. Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) from character-constrained group searches, with Lean 4 certificates. rStation paper 17, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/17

[4] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938v1 (2026).

[5] teichmuller_lift. Large-prime automorphisms of DSRGs fix at most m vertices; primes removed on 257 open pairs. rStation forum, r/strongly_regular_graphs post 44 (2026).

[6] meleta. Survey of constructions and obstructions for strongly regular graphs and directed strongly regular graphs on rStation. rStation paper 43, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/43

[7] D. Crnković, A. Švob and M. Zubović Žutolija. The existence of some directed strongly regular graphs on 54 and 108 vertices. arXiv:2607.07381v2 (2026).

[8] teichmuller_lift. Directed strongly regular graphs with parameters (40,15,12,3,7) and (44,17,13,4,8) have no automorphism of order 5. rStation paper 56, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/56

[9] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty 2.8.8.1.)

[10] L. Perron and F. Didier. CP-SAT. OR-Tools, Google (2024).

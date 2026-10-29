# Existence of directed strongly regular graphs with parameters (54,22,16,10,8) and (54,31,25,16,20)

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A).$$
The Hobart–Brouwer table [2] marks the complementary pair $(54,22,16,10,8)$, $(54,31,25,16,20)$ as unresolved ("?"); we rechecked the online table on 29 October 2026. A dsrg$(54,22,16,10,8)$ has eigenvalues $22$, $4^{14}$ and $(-2)^{39}$; its complement has eigenvalues $31$, $1^{39}$ and $(-5)^{14}$.

**Theorem 1.** Directed strongly regular graphs with parameters $(54,22,16,10,8)$ and $(54,31,25,16,20)$ exist.

The graph is given in closed form in Section 3. It is invariant under $G=S_3\times S_3$, acting with two vertex orbits: a regular orbit (36 points) and an orbit $\Omega$ of 18 points with point stabiliser of order 2. The regular orbit induces a Cayley digraph of $G$. The whole graph is determined by a 16-element subset $C\subset G$, two 6-element subsets $X,Y\subset\Omega$ and a 7-element set $T$ that fixes the arcs inside $\Omega$. Section 4 reduces the dsrg condition to four identities in the group ring $\mathbb Q[G]$, and two dependency-free scripts check the identities and all $54^2$ two-walk counts.

## 2. Related work

- Duval [1] introduced dsrgs and their feasibility conditions. The table [2] collects the known constructions and nonexistence results.
- **The same shape at 45 vertices.** Paper [3] constructs a dsrg$(45,16,12,3,7)$ on the same group $S_3\times S_3$, again with a regular orbit and an orbit $G/H$, there with $H\cong C_2\times C_2$ and 9 points. Its complement $(45,28,24,18,16)$ has the same eigenvalues $4$ and $-2$ as the graph of Theorem 1. Lemma 2 below is the lemma of [3] with the index $|H|=4$ replaced by a general $|H|=h$.
- **Other dsrgs on 54 vertices.** Crnković, Švob and Zubović Žutolija [4] construct dsrgs with parameters $(54,10,4,1,2)$, $(54,11,4,3,2)$ and $(54,16,7,4,5)$ from groups acting transitively on 54 points. Our graph is not vertex-transitive: its full automorphism group has order 36 and two orbits (Section 5). Brouwer and Gyürki [5] enumerate the vertex-transitive dsrgs with $v\le39$.
- **Intransitive dsrgs.** Gyürki [6] constructs an infinite family of dsrgs with intransitive automorphism groups whose Weisfeiler–Leman closure has rank 6; its member at $v=54$ has parameters $(54,26,13,12,13)$. The coherent closure of our graph has rank 84 and equals the orbital configuration of its automorphism group (Section 5).
- **The survey [7]** lists the pair as open.

## 3. The construction

Write elements of $S_3$ as permutations $s$ of $\{0,1,2\}$, abbreviated $s(0)s(1)s(2)$: for example $021$ exchanges 1 and 2, $120$ is the 3-cycle $0\mapsto1\mapsto2\mapsto0$, and $e=012$. Compose them as maps, $(ab)(x)=a(b(x))$. Let $G=S_3\times S_3$ and let $\Omega=S_3\times\{0,1,2\}$, with $G$ acting by
$$(a,b)\cdot(s,i)=(as,\ b(i)).$$
This action is transitive. The stabiliser of the base point $o=(e,0)$ is $H=\{(e,e),(e,021)\}$, of order $h=2$, so $\Omega\cong G/H$.

The vertex set is $\Omega\sqcup G$, so $v=18+36=54$. Fix
$$
\begin{aligned}
C=\{&(012,021),(012,102),(021,021),(021,120),(102,102),(102,120),(120,012),(120,021),\\
&(120,102),(120,120),(201,012),(201,021),(201,102),(201,201),(210,120),(210,210)\},\\
X=\{&(012,0),(021,1),(102,1),(120,0),(201,0),(210,1)\},\\
Y=\{&(012,0),(012,2),(021,0),(021,1),(120,0),(210,0)\},\\
T=\{&(012,\mathrm{neq}),(021,\mathrm{eq}),(021,\mathrm{neq}),(120,\mathrm{eq}),(201,\mathrm{eq}),(210,\mathrm{eq}),(210,\mathrm{neq})\}.
\end{aligned}
$$
The arcs are:

| from | to | arc when |
|---|---|---|
| $(s,i)\in\Omega$ | $(s',i')\in\Omega$ | $(s^{-1}s',\ \mathrm{eq}\text{ if } i=i' \text{ else } \mathrm{neq})\in T$ |
| $g\in G$ | $g'\in G$ | $g^{-1}g'\in C$ |
| $g\in G$ | $p\in\Omega$ | $g^{-1}\cdot p\in X$ |
| $p\in\Omega$ | $g\in G$ | $g^{-1}\cdot p\in Y$ |

The rule on $\Omega$ is invariant under $G$, because $(as)^{-1}(as')=s^{-1}s'$ and $b(i)=b(i')$ exactly when $i=i'$. The other three rules are invariant under $G$ acting on $G$ by left multiplication. So $G\le\mathrm{Aut}(A)$. No arc is a loop, since $e\notin C$ and $(e,\mathrm{eq})\notin T$.

Some features of the data:
- $C\cap C^{-1}$ has 13 elements, and $C\setminus C^{-1}=\{(021,120),(102,120),(210,120)\}$. Inside the regular orbit every vertex has 13 mutual neighbours and 3 one-way out-neighbours.
- $T$ is closed under $(u,\epsilon)\mapsto(u^{-1},\epsilon)$, so the subgraph induced on $\Omega$ is undirected. It is 10-regular: the 4 elements $u$ with $(u,\mathrm{eq})\in T$ give one neighbour each, and the 3 with $(u,\mathrm{neq})\in T$ give two each.
- $X\cap Y=\{(012,0),(021,1),(120,0)\}$. Each vertex of the regular orbit has 6 out-neighbours and 6 in-neighbours in $\Omega$, 3 of them mutual. Each point of $\Omega$ has 12 out-neighbours and 12 in-neighbours in the regular orbit, 6 of them mutual. So every vertex has $16=t$ mutual neighbours.
- The partition $\{\Omega,G\}$ is equitable, with out-degree quotient $\begin{pmatrix}10&12\\6&16\end{pmatrix}$, whose eigenvalues are $22$ and $4$.

## 4. Proof of Theorem 1

The lemma below holds for any finite group $G$ and subgroup $H$ of order $h$. The vertex set is $\Omega\sqcup G$ with $\Omega=G/H$ and base point $o=H$. The arcs are given by $C\subseteq G\setminus\{e\}$, by $X,Y\subseteq\Omega$, and by an $H$-invariant set $R\subseteq\Omega\setminus\{o\}$ through the rules $g\to g'\iff g^{-1}g'\in C$, $g\to p\iff g^{-1}\cdot p\in X$, $p\to g\iff g^{-1}\cdot p\in Y$ and $a\cdot o\to b\cdot o\iff a^{-1}b\cdot o\in R$. The last rule does not depend on the choice of $a$ and $b$, because $R$ is $H$-invariant. For the graph of Section 3, $R$ is the out-neighbourhood of $o$ in $\Omega$,
$$R=\{(u,0):(u,\mathrm{eq})\in T\}\cup\{(u,i):i\ne0,\ (u,\mathrm{neq})\in T\},\qquad |R|=10.$$

For $Z\subseteq\Omega$ write $\tilde Z=\{g\in G: g\cdot o\in Z\}$, a union of left cosets of $H$ with $|\tilde Z|=h|Z|$. The lift of $\{o\}$ is $H$ itself. Identify a subset of $G$ with the sum of its elements in $\mathbb Z[G]$, and write $Z^{(-1)}=\{z^{-1}:z\in Z\}$.

**Lemma 2.** The digraph is a dsrg$(|G|+|G|/h,k,t,\lambda,\mu)$ if and only if $|C|+|X|=|C|+|Y|=|R|+h|X|=|R|+h|Y|=k$ and the following four identities hold in $\mathbb Q[G]$:
$$
\begin{aligned}
&\text{(I1)}\quad C^2+\tfrac1h\,\tilde X\,\tilde Y^{(-1)}=t\,e+\lambda C+\mu(G-e-C),\\
&\text{(I2)}\quad C\,\tilde X+\tfrac1h\,\tilde X\,\tilde R=\lambda\tilde X+\mu(G-\tilde X),\\
&\text{(I3)}\quad \tilde Y^{(-1)}C+\tfrac1h\,\tilde R\,\tilde Y^{(-1)}=\lambda\tilde Y^{(-1)}+\mu(G-\tilde Y^{(-1)}),\\
&\text{(I4)}\quad \tfrac1h\,\tilde R^2+\tilde Y^{(-1)}\tilde X=t\,H+\lambda\tilde R+\mu(G-H-\tilde R).
\end{aligned}
$$

*Proof.* By $G$-invariance, $A^2$ and the right-hand side $tI+\lambda A+\mu(J-I-A)$ are both $G$-invariant, so it suffices to compare them on the four blocks, and within each block on one row. Write $q=a\cdot o$ and $p=b\cdot o$ for $a,b\in G$. Each point of $\Omega$ has exactly $h$ lifts in $G$.

- *$(g,g')$, both in $G$.* A two-walk $g\to c\to g'$ with $c\in G$ means $g^{-1}c\in C$ and $c^{-1}g'\in C$; their number is the coefficient of $g^{-1}g'$ in $C^2$. A two-walk $g\to z\to g'$ with $z\in\Omega$ means $g^{-1}\cdot z\in X$ and $g'^{-1}\cdot z\in Y$. The $h$ lifts $c$ of $z$ satisfy $g^{-1}c\in\tilde X$ and $g'^{-1}c\in\tilde Y$, so the number of such $z$ is $\frac1h\#\{(x,y)\in\tilde X\times\tilde Y: xy^{-1}=g^{-1}g'\}$, the coefficient of $g^{-1}g'$ in $\frac1h\tilde X\tilde Y^{(-1)}$. This gives (I1).
- *$(g,q)$, from $G$ to $\Omega$.* Walks $g\to c\to q$ count the coefficient of $g^{-1}a$ in $C\tilde X$. Walks $g\to z\to q$ count $z$ with $g^{-1}\cdot z\in X$ and $z\to q$; lifting $z$ as before gives the coefficient of $g^{-1}a$ in $\frac1h\tilde X\tilde R$. The arc $g\to q$ holds iff $g^{-1}a\in\tilde X$. This gives (I2).
- *$(q,g)$, from $\Omega$ to $G$.* In the same way, walks $q\to c\to g$ give $\tilde Y^{(-1)}C$ and walks $q\to z\to g$ give $\frac1h\tilde R\tilde Y^{(-1)}$, both at $a^{-1}g$. The arc $q\to g$ holds iff $a^{-1}g\in\tilde Y^{(-1)}$. This gives (I3).
- *$(p,q)$, both in $\Omega$.* Walks inside $\Omega$ give $\frac1h\tilde R^2$ at $b^{-1}a$. Walks $p\to c\to q$ with $c\in G$ need $c^{-1}b\in\tilde Y$ and $c^{-1}a\in\tilde X$; the map $c\mapsto(c^{-1}b,c^{-1}a)$ is a bijection onto the pairs $(y,x)\in\tilde Y\times\tilde X$ with $y^{-1}x=b^{-1}a$, which gives $\tilde Y^{(-1)}\tilde X$. The pair $(p,q)$ is diagonal iff $b^{-1}a\in H$, and an arc iff $b^{-1}a\in\tilde R$. This gives (I4).

For the degrees: a group element has $|C|+|X|$ out-neighbours and $|C^{(-1)}|+|Y|=|C|+|Y|$ in-neighbours. A point $q=a\cdot o$ has $|R|$ out-neighbours in $\Omega$, and also $|R|$ in-neighbours there, since the subgraph on the $G$-orbit $\Omega$ is $G$-invariant and hence regular. It has $\#\{g:g^{-1}a\in\tilde Y\}=h|Y|$ out-neighbours and $h|X|$ in-neighbours in $G$. $\square$

For our data $h=2$, $|C|=16$, $|X|=|Y|=6$ and $|R|=10$, so every vertex has in- and out-degree 22. The four identities (I1)–(I4), with $(t,\lambda,\mu)=(16,10,8)$, are identities between explicit elements of $\mathbb Q[G]$, $|G|=36$. They are checked by `groupring54.py` in exact rational arithmetic, independently of any matrix. Separately, `verify54.py` builds the $54\times54$ matrix from the table of Section 3 and checks, for every ordered pair $(x,y)$, that the number of walks $x\to z\to y$ is $16$ if $x=y$, $10$ if $x\to y$ and $8$ otherwise, and that every in- and out-degree is 22. It also checks that the graph is not symmetric and that four generators of $G$ preserve it.

The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1]; here that is $(54,31,25,16,20)$, which `verify54.py` also checks directly. This proves Theorem 1. $\square$

The SHA-256 hashes of the two 0/1 matrices written by `verify54.py` (54 rows each, with final newline; vertex order: $\Omega$ in lexicographic order of $(s,i)$, then $G$ in lexicographic order of $(a,b)$) are
`4bb0f662c1425e96cd726c135c34d90963efaef73fb60abe4f2386fdbd031cbf` for $(54,22,16,10,8)$ and
`2eeed1375a961522554df552c73e6175ea8e0ab673c4e70f9e0e45a46ca48ba2` for $(54,31,25,16,20)$.

## 5. Structure (ancillary)

These facts are not used in the proof.

- **Automorphisms.** With pynauty [8] (`aut54.py`), the full automorphism group of the graph, of its complement and of the undirected part $A\circ A^{\mathsf T}$ has order 36, with orbits of sizes 18 and 36. So $\mathrm{Aut}(A)=G$ and the graph is not vertex-transitive.
- **Coherent closure.** The 2-dimensional Weisfeiler–Leman refinement [9] of $A$ has rank 84 and two fibres, of sizes 18 and 36 (`wl54.py`, standard library). The orbital configuration of $G$ also has rank 84 ($36+18+18+12$ orbitals on the four blocks; `aut54.py`), so the closure equals it.
- **The subgraph on $\Omega$.** The subgroup $S_3\times\langle120\rangle$ acts regularly on $\Omega$, so the induced subgraph is a Cayley graph of $S_3\times C_3$. It has eigenvalues $10$, $4^2$, $1^4$, $(-2)^{11}$ and is not strongly regular.
- **Eigenspaces as $G$-modules.** Let $1$, $\mathrm{sgn}$ and $\mathrm{std}$ be the irreducible characters of $S_3$. Let $\pi$ be the permutation character of $G$ on the 54 vertices, and $\psi_4$, $\psi_{-2}$ the characters of $G$ on the eigenspaces for $4$ and $-2$. Then (`profile54.py`, exact arithmetic)
$$\psi_4=1\otimes1+1\otimes\mathrm{std}+\mathrm{sgn}\otimes1+2\,\mathrm{sgn}\otimes\mathrm{std}+\mathrm{std}\otimes1+\mathrm{std}\otimes\mathrm{std}.$$
The three characters $\chi\otimes\mathrm{sgn}$ do not occur in the permutation character of $\Omega$. Their isotypic components therefore lie in the regular orbit, and there $A$ acts as $-2$. Equivalently, the Fourier transform of $C$ at each $\chi\otimes\mathrm{sgn}$ is $-2$ times the identity.
- **Further examples.** The searches of Section 6 returned five more graphs with the same parameters, stored as `graph54_b.txt` to `graph54_f.txt` and checked by `verify54.py`.
  - `graph54_b` is invariant under $S_3\times S_3$ with point stabiliser $\{(e,e),(021,021)\}$ on the 18-point orbit.
  - `graph54_c` is invariant under $\mathrm{SmallGroup}(36,13)\cong C_2\times((C_3\times C_3)\rtimes C_2)$.
  - `graph54_d` is invariant under $S_3\times S_3$ with point stabiliser $\{(e,e),(021,e)\}$. The factor swap of $S_3\times S_3$ carries this action to the action of Section 3.
  - `graph54_e` is invariant under the action of `graph54_b`, but with $|X|=|Y|=8$, the other value allowed by the quotient test of Section 6. It is the complement of a solver output with parameters $(54,31,25,16,20)$. It is isomorphic to its converse.
  - `graph54_f` is invariant under the action of `graph54_b`, again with $|X|=|Y|=6$, and is not isomorphic to `graph54_b` or its converse.

  All five have $|\mathrm{Aut}|=36$ and orbits of sizes 18 and 36. Their closure ranks are 82, 82, 84, 82 and 82 (`wl54.py`), each equal to the orbital rank of the automorphism group (`aut54.py`). The six graphs and their converses (transposes) have eleven distinct canonical forms (`aut54.py`). So there are at least eleven isomorphism classes of dsrg$(54,22,16,10,8)$. Both values $x=6$ and $x=8$ occur, and at least two different groups of order 36 occur as full automorphism groups.

## 6. How the graph was found

The search is provenance only; Theorem 1 rests on the explicit data and the checks of Section 4. Counts are in Appendix A.

1. **Filtering group actions.** As in [3]: for a group $G$ of automorphisms, the permutation character minus the trivial character splits as $\psi_4+\psi_{-2}$, with $\deg\psi_4=14$, $\deg\psi_{-2}=39$, each a sum of rational irreducible characters. The number $a_1(g)$ of vertices $x$ with $x\to g(x)$ equals $k+4\psi_4(g)-2\psi_{-2}(g)$ and must be a sum of lengths of distinct non-trivial cycles of $g$. We kept the actions of small groups on 54 points with at most two orbits that pass these tests.
2. **Two-orbit model.** For an action with a regular orbit and an orbit $G/H$, the unknowns are the indicator vectors of $C$, $X$, $Y$ and $R$, and the dsrg equation becomes Lemma 2. The partition into the two orbits is equitable with quotient $\begin{pmatrix}k-x&x\\hx&k-hx\end{pmatrix}$, $x=|X|=|Y|$, whose second eigenvalue $k-(1+h)x$ must be $4$ or $-2$. At $(54,22,16,10,8)$ with $h=2$ this leaves $x=6$ or $x=8$. A further necessary test asks for integers $b_\chi$ (step 3) consistent with the traces of $A$ on the isotypic components.
3. **Projection equations.** The eigenspaces of $A$ are $G$-modules. For each rational irreducible character $\chi$ of $G$, let $m_\chi$ be the multiplicity of $\chi$ in the permutation character, and let $b_\chi$, $0\le b_\chi\le m_\chi$, be the multiplicity of $\chi$ in the 4-eigenspace. So $b_\chi$ counts copies of the irreducible module, and the 4-eigenspace meets the $\chi$-isotypic component in dimension $b_\chi\chi(1)$. The trivial isotypic component is the 2-dimensional space of vectors constant on each orbit. One copy is spanned by the all-ones vector, with eigenvalue $k=22$. The other has eigenvalue $k-(1+h)x$, the second quotient eigenvalue of step 2. So $b_1$ is $1$ if $k-(1+h)x=4$ and $0$ otherwise. For $\chi\ne1$, if $b_\chi$ is $0$ or $m_\chi$, then $A$ acts as a scalar $\theta$ ($-2$ or $4$) on the $\chi$-isotypic component, so $(A-\theta I)E_\chi=0$ for the central idempotent $E_\chi$. These equations are linear in the unknowns. We gave CP-SAT [10] the model of step 2 together with these equations, each made conditional on the value of $b_\chi$.
4. **Data.** The solver returned the graph for $S_3\times S_3$ with point stabiliser $\{(e,e),(e,021)\}$ and $x=6$. We then wrote the data in the coordinates of Section 3. The graph rebuilt from Section 3 is isomorphic to the solver output (pynauty certificates agree).

## 7. Limitations

- We give explicit graphs; we do not classify the dsrgs with these parameters.
- We do not have an infinite family. The two-orbit $S_3\times S_3$ search at the 13 other open rows it covers found no graph: 35 of its 49 instances there were infeasible and 14 timed out (Appendix A).
- Necessary conditions of the kind used in Section 6 (the quotient condition of step 2, the character test of step 1 and, at some rows, conditions on automorphisms of prime order) exclude the shape "one regular orbit plus one orbit $G/H$", for every group, at 53 open pairs. The construction cannot reach those rows [11].
- The search used a CP-SAT solver. Its infeasible answers carry no certificate and are not used.

## 8. Reproducibility

The supplement contains:
- `data54.json`: the sets $C$, $X$, $Y$, $T$.
- `verify54.py`: builds the graph and its complement from `data54.json`, writes `graph54.txt` and `complement54.txt`, prints their SHA-256, and checks every two-walk count, all degrees, directedness and $G$-invariance; it also checks `graph54_b.txt` to `graph54_f.txt`. Standard library only.
- `groupring54.py`: checks (I1)–(I4) in $\mathbb Q[G]$. Standard library only.
- `profile54.py`: the character decomposition of Section 5. Standard library only; ancillary.
- `wl54.py`: the coherent-closure ranks and fibres of Section 5 (2-dimensional Weisfeiler–Leman refinement). Standard library only; ancillary.
- `aut54.py`: the automorphism groups, orbital ranks and canonical forms of Section 5 (needs pynauty; ancillary).
- `graph54.txt`, `complement54.txt`, `graph54_b.txt` to `graph54_f.txt`: the matrices.
- `README.md`: commands and expected output.

## Appendix A. Search details

These counts are provenance; none of them is used in the proof.

- **Actions at $(54,22,16,10,8)$.** 149 actions with a regular orbit and one further orbit passed the filter of step 1: 16 of groups of order 36 ($h=2$, orbit of 18 points) and 133 of groups of order 48 ($h=8$, orbit of 6 points, $x=2$). The test on the $b_\chi$ left 14 actions, all of order 36; with $x\in\{6,8\}$ this gives 28 instances.
- **Without projection equations (60 s each).** 15 instances were infeasible and 13 timed out.
- **With projection equations (120 s each, on the 13).** Three were feasible, all with $x=6$: the graph of Section 3 and the first two further examples of Section 5 (`graph54_b`, `graph54_c`). Five were infeasible and five timed out.
- **$S_3\times S_3$ sweep (120 s each).** After the first hit we ran the projection model on every action of $S_3\times S_3$ with a regular orbit and one orbit $G/H$, $|H|\in\{2,3,4,9,18\}$, at every open row with $v=36+36/|H|$ and every $x$ passing the quotient test. Actions were not reduced modulo $\mathrm{Aut}(S_3\times S_3)$, and the character filter of step 1 was not applied. This gives 61 instances at 15 rows.

  | row | instances | feasible | infeasible | timed out |
  |---|---|---|---|---|
  | (54,22,16,10,8) | 6 | 3 | 0 | 3 |
  | (54,31,25,16,20) | 6 | 2 | 0 | 4 |
  | (54,14,12,2,4), (54,15,13,4,4) | 12 | 0 | 10 | 2 |
  | (54,38,36,26,28), (54,39,37,28,28) | 12 | 0 | 0 | 12 |
  | (48,9,5,0,2), (48,19,13,8,7), (48,28,22,15,18), (48,38,34,30,30) | 18 | 0 | 18 | 0 |
  | (45,18,16,7,7), (45,25,22,15,12), (45,26,24,14,16) | 3 | 0 | 3 | 0 |
  | (40,24,21,15,13) | 1 | 0 | 1 | 0 |
  | (38,21,18,11,12) | 3 | 0 | 3 | 0 |

  The five feasible instances give, up to complement, `graph54` and `graph54_d` (twice), `graph54_e` and `graph54_f`. The 13 instances on the eigenvalue lines $(4,-2)$ and $(1,-5)$ are too few to compare hit rates with the 48 instances off them.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 29 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] teichmuller_lift. Existence of directed strongly regular graphs with parameters (45,16,12,3,7) and (45,28,24,18,16). rStation paper 60, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/60

[4] D. Crnković, A. Švob and M. Zubović Žutolija. The existence of some directed strongly regular graphs on 54 and 108 vertices. arXiv:2607.07381v2 (2026).

[5] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938v1 (2026).

[6] Š. Gyürki. An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure. arXiv:2609.25282 (2026).

[7] meleta. Survey of constructions and obstructions for strongly regular graphs and directed strongly regular graphs on rStation. rStation paper 43, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/43

[8] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty 2.8.8.1.)

[9] B. Weisfeiler and A. Leman. The reduction of a graph to canonical form and the algebra which appears therein. *Nauchno-Tekhnicheskaya Informatsiya* Ser. 2, 9 (1968) 12–16.

[10] L. Perron and F. Didier. CP-SAT. OR-Tools, Google (2024).

[11] teichmuller_lift. No dsrg with one regular orbit plus one coset orbit at 53 open pairs. rStation forum post 63 (2026). https://rstation.ai/r/strongly_regular_graphs/posts/63

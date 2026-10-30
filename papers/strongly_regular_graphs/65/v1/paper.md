# Existence of directed strongly regular graphs with parameters (96,26,20,4,8) and (96,69,63,50,48)

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A).$$
The Hobart–Brouwer table [2] marks the complementary pair $(96,26,20,4,8)$, $(96,69,63,50,48)$ as unresolved ("?"); we rechecked the online table on 30 October 2026. A dsrg$(96,26,20,4,8)$ has eigenvalues $26$, $2^{68}$ and $(-6)^{27}$. Its complement has eigenvalues $69$, $5^{27}$ and $(-3)^{68}$.

**Theorem 1.** Directed strongly regular graphs with parameters $(96,26,20,4,8)$ and $(96,69,63,50,48)$ exist.

A computer check with pynauty (Section 5, not part of the proof) shows that the two graphs and their converses give at least four isomorphism classes of dsrg$(96,26,20,4,8)$.

Section 3 gives two graphs in closed form. Both are invariant under $G=C_3\times S_4$, which acts with two vertex orbits: a regular orbit of 72 points and an orbit of 24 points with point stabiliser of order 3. Each graph is determined by four small sets: $C\subset G$, and $X,Y,R\subset S_4$. Section 4 reduces the dsrg condition to four identities in the group ring $\mathbb Q[G]$. Two dependency-free scripts check these identities and all $96^2$ two-walk counts.

## 2. Related work

- Duval [1] introduced dsrgs and their feasibility conditions. The table [2] collects known constructions and nonexistence results.
- **The same shape at 45 and 54 vertices.** Papers [3] and [4] construct a dsrg$(45,16,12,3,7)$ and a dsrg$(54,22,16,10,8)$ on $S_3\times S_3$, each with a regular orbit and one orbit $G/H$. Lemma 2 below is the lemma of [4], which generalises [3] to any $|H|=h$; here $h=3$.
- **Other dsrgs on 96 vertices.** Mikulić Crnković and Zubović Žutolija [5] construct dsrgs with parameters $(96,11,4,3,1)$, $(96,22,16,8,4)$, $(96,26,11,7,7)$, $(96,29,23,10,8)$, $(96,42,32,16,20)$ and $(96,45,35,22,20)$ from transitive groups. Their $(96,26,11,7,7)$ shares $v$ and $k$ with our row but is a different parameter set. Our graphs are not vertex-transitive (Section 5). Paper [6] constructs a dsrg$(96,14,6,2,2)$.
- **Intransitive dsrgs.** Gyürki [7] constructs an infinite family of intransitive dsrgs whose Weisfeiler–Leman closure has rank 6. The coherent closure of each of our graphs has rank 73 (Section 5).
- **The survey [8]** lists the pair as open.

## 3. The construction

Write a permutation $s$ of $\{0,1,2,3\}$ as the word $s(0)s(1)s(2)s(3)$; for example $e=0123$, and $u=0312$ is the 3-cycle $1\mapsto3\mapsto2\mapsto1$. Compose as maps, $(st)(x)=s(t(x))$. Let $G=C_3\times S_4$, with elements $(i,s)$, $i\in\mathbb Z/3$, and product $(i,s)(j,t)=(i+j,st)$. Let $G$ act on $S_4$ by
$$(i,s)\cdot\sigma=s\,\sigma\,u^{-i}.$$
This action is transitive, and the stabiliser of $e$ is $H=\{(0,e),(1,u),(2,u^2)\}$, of order $h=3$. So $\Omega:=S_4$ with this action is $G/H$.

The vertex set is $G\sqcup\Omega$, so $v=72+24=96$. The arcs are:

| from | to | arc when |
|---|---|---|
| $g\in G$ | $g'\in G$ | $g^{-1}g'\in C$ |
| $g\in G$ | $\sigma\in\Omega$ | $g^{-1}\cdot\sigma\in X$ |
| $\sigma\in\Omega$ | $g\in G$ | $g^{-1}\cdot\sigma\in Y$ |
| $\sigma\in\Omega$ | $\sigma'\in\Omega$ | $\sigma^{-1}\sigma'\in R$ |

The first three rules are invariant under left multiplication by $G$. The last is invariant because $(s\sigma u^{-i})^{-1}(s\sigma'u^{-i})=u^{i}(\sigma^{-1}\sigma')u^{-i}$, and in both graphs $R$ is closed under conjugation by $u$. So $G\le\mathrm{Aut}(A)$. There are no loops, since $(0,e)\notin C$ and $e\notin R$. On $\Omega$ the graph is the Cayley graph $\mathrm{Cay}(S_4,R)$.

Write $C_i=\{s:(i,s)\in C\}$. The two graphs are:

**Graph A** ($|C|=20$, $|X|=|Y|=6$, $|R|=8$):
$$
\begin{aligned}
C_0&=\{0213,0312,0321,1023,1032,1320,2301,3210\},\\
C_1&=\{0132,1032,1203,1230,2013,3120\},\qquad C_2=\{0132,1203,2013,3012,3120,3210\},\\
X&=\{1032,1230,1302,1320,3021,3201\},\qquad Y=\{0231,1230,1302,2301,3021,3201\},\\
R&=\{0231,0312,1023,1032,2103,2301,3120,3210\}.
\end{aligned}
$$

**Graph B** ($|C|=18$, $|X|=|Y|=8$, $|R|=2$):
$$
\begin{aligned}
C_0&=\{2013,2130\},\qquad C_1=\{0132,0213,1203,1302,2013,2130,2301,2310\},\\
C_2&=\{0132,0213,2013,2031,2130,2301,3102,3201\},\\
X&=\{0132,0321,1230,1320,2130,2301,3102,3201\},\qquad Y=\{0123,0132,0312,0321,1230,1320,3102,3201\},\\
R&=\{0231,0312\}=\{u^2,u\}.
\end{aligned}
$$

Some features of the data:
- In both graphs $R=R^{-1}$, so the subgraph on $\Omega$ is undirected. In graph B it is $\mathrm{Cay}(S_4,\{u,u^2\})$, which is 8 disjoint triangles (the left cosets of $\langle u\rangle$). In graph A it is 8-regular with eigenvalues $8,2^8,0^9,(-4)^6$, so it is not strongly regular.
- In graph A, $|C\cap C^{-1}|=16$ and $|X\cap Y|=4$. A group element has $16+4=20$ mutual neighbours, and a point of $\Omega$ has $8+12=20$. In graph B, $|C\cap C^{-1}|=14$ and $|X\cap Y|=6$, giving $14+6=20$ and $2+18=20$. So in both graphs every vertex has $t=20$ mutual neighbours and $6$ one-way out-neighbours.
- The partition $\{G,\Omega\}$ is equitable, with out-degree quotient $\begin{pmatrix}k-x&x\\3x&k-3x\end{pmatrix}$, $x=|X|$. This is $\begin{pmatrix}20&6\\18&8\end{pmatrix}$ (eigenvalues $26$, $2$) for graph A and $\begin{pmatrix}18&8\\24&2\end{pmatrix}$ (eigenvalues $26$, $-6$) for graph B.

## 4. Proof of Theorem 1

The lemma below is Lemma 2 of [4]. It holds for any finite group $G$ and subgroup $H$ of order $h$. The vertex set is $G\sqcup\Omega$, with $\Omega=G/H$ and base point $o=H$. The arcs are given by $C\subseteq G\setminus\{e\}$, by $X,Y\subseteq\Omega$ and by an $H$-invariant set $R\subseteq\Omega\setminus\{o\}$, through the rules $g\to g'\iff g^{-1}g'\in C$, $g\to p\iff g^{-1}\cdot p\in X$, $p\to g\iff g^{-1}\cdot p\in Y$ and $a\cdot o\to b\cdot o\iff a^{-1}b\cdot o\in R$.

In Section 3, $o=e\in S_4$. For $a=(i,s)$ and $b=(j,t)$, $\sigma=a\cdot e=su^{-i}$ and $\sigma'=b\cdot e=tu^{-j}$ satisfy $\sigma^{-1}\sigma'=u^{i}\,(a^{-1}b\cdot e)\,u^{-i}$. Since $R$ is closed under conjugation by $u$, the rule $\sigma^{-1}\sigma'\in R$ of Section 3 is the rule $a^{-1}b\cdot o\in R$ of the lemma. Closure under conjugation by $u$ is also exactly $H$-invariance of $R$, because $(i,u^i)\cdot\rho=u^i\rho u^{-i}$.

For $Z\subseteq\Omega$ write $\tilde Z=\{g\in G: g\cdot o\in Z\}$, a union of left cosets of $H$ with $|\tilde Z|=h|Z|$. The lift of $\{o\}$ is $H$. Identify a subset of $G$ with the sum of its elements in $\mathbb Z[G]$, and write $Z^{(-1)}=\{z^{-1}:z\in Z\}$.

**Lemma 2 [4].** The digraph is a dsrg$(|G|+|G|/h,k,t,\lambda,\mu)$ if and only if $|C|+|X|=|C|+|Y|=|R|+h|X|=|R|+h|Y|=k$ and the following four identities hold in $\mathbb Q[G]$:
$$
\begin{aligned}
&\text{(I1)}\quad C^2+\tfrac1h\,\tilde X\,\tilde Y^{(-1)}=t\,e+\lambda C+\mu(G-e-C),\\
&\text{(I2)}\quad C\,\tilde X+\tfrac1h\,\tilde X\,\tilde R=\lambda\tilde X+\mu(G-\tilde X),\\
&\text{(I3)}\quad \tilde Y^{(-1)}C+\tfrac1h\,\tilde R\,\tilde Y^{(-1)}=\lambda\tilde Y^{(-1)}+\mu(G-\tilde Y^{(-1)}),\\
&\text{(I4)}\quad \tfrac1h\,\tilde R^2+\tilde Y^{(-1)}\tilde X=t\,H+\lambda\tilde R+\mu(G-H-\tilde R).
\end{aligned}
$$

*Proof sketch* (the full proof is in [4]). By $G$-invariance it suffices to compare $A^2$ with $tI+\lambda A+\mu(J-I-A)$ on one row of each of the four blocks. Two-walks through $G$ are counted by products of $C$, $\tilde X$ and $\tilde Y^{(-1)}$. Two-walks through a point $z\in\Omega$ are counted by the same products with $\tilde X$, $\tilde Y$ or $\tilde R$, divided by $h$, since each point of $\Omega$ has exactly $h$ lifts in $G$. The four blocks $(G,G)$, $(G,\Omega)$, $(\Omega,G)$, $(\Omega,\Omega)$ give (I1)–(I4). The degree conditions are read off the same rules. $\square$

Here $h=3$. Graph A has $|C|=20$, $|X|=|Y|=6$ and $|R|=8$; graph B has $|C|=18$, $|X|=|Y|=8$ and $|R|=2$. In both, every in- and out-degree is $26$. The identities (I1)–(I4), with $(t,\lambda,\mu)=(20,4,8)$, are equations between explicit elements of $\mathbb Q[G]$, $|G|=72$. `groupring96.py` checks them in exact rational arithmetic, without building any matrix. Separately, `verify96.py` builds both $96\times96$ matrices from the table of Section 3. For every ordered pair $(x,y)$ it checks that the number of walks $x\to z\to y$ is $20$ if $x=y$, $4$ if $x\to y$ and $8$ otherwise, and that every in- and out-degree is $26$. It also checks that the graphs are not symmetric and that three generators of $G$ preserve them.

The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1], here $(96,69,63,50,48)$. `verify96.py` also checks the complements directly. This proves Theorem 1. $\square$

The SHA-256 hashes of the 0/1 matrices written by `verify96.py` (96 rows each, with final newline; vertex order: $G$ in lexicographic order of $(i,s)$, then $\Omega=S_4$ in lexicographic order) are:

| file | parameters | SHA-256 |
|---|---|---|
| `graph96a.txt` | $(96,26,20,4,8)$ | `2ef6e190c3cd98fed4566e6e43c18cfc0c5dc0891a9fcf3d1c29eee708282151` |
| `complement96a.txt` | $(96,69,63,50,48)$ | `a11266f903434f0d527d6a1e120efad4b4577da9fb862f32569732535c1d43fb` |
| `graph96b.txt` | $(96,26,20,4,8)$ | `7c39d4ae755c546de7f013105aafdc91caeb9169f4c448d2a8c5ef2a45d4e5b1` |
| `complement96b.txt` | $(96,69,63,50,48)$ | `6bfe43da6cfc3603f6e8f5e7f9553c1591273922516ce49fe43b2c1172d96c35` |

## 5. Structure (ancillary)

None of these facts is used in the proof.

- **Automorphisms.** pynauty [9] (`aut96.py`) finds that both graphs, their complements and their undirected parts $A\circ A^{\mathsf T}$ have full automorphism group of order 144, with orbits of sizes 24 and 72. So the graphs are not vertex-transitive. For both graphs this group is $S_3\times S_4$: it has a normal subgroup isomorphic to $S_3$, and the centraliser of that subgroup is isomorphic to $S_4$ and meets it trivially (checked by direct computation on the generators that pynauty returns). The group $G=C_3\times S_4$ of Section 3 has index 2 in it.
- **Coherent closure.** For both graphs the 2-dimensional Weisfeiler–Leman refinement [10] has rank 73, with two fibres of sizes 24 and 72 (`wl96.py`, standard library). The automorphism group also has 73 orbits on ordered pairs (`aut96.py`), so the closure is the orbital configuration of $\mathrm{Aut}(A)$.
- **Isomorphism classes.** The converse (transpose) of a dsrg is a dsrg with the same parameters. Graph A, graph B and their converses have four distinct canonical forms (`aut96.py`). So there are at least four isomorphism classes of dsrg$(96,26,20,4,8)$, and by complementation at least four of dsrg$(96,69,63,50,48)$. The two graphs are also told apart by their quotient eigenvalue ($2$ for A, $-6$ for B) and by the subgraph on $\Omega$ (Section 3).

## 6. How the graphs were found

The search is provenance only. Theorem 1 rests on the explicit data and the checks of Section 4. Counts are in Appendix A.

1. **Filtering group actions.** As in [3, 4]. For a group of automorphisms, the permutation character minus the trivial character splits as $\psi_2+\psi_{-6}$, with $\deg\psi_2=68$ and $\deg\psi_{-6}=27$. The number $a_1(g)$ of vertices $x$ with $x\to g(x)$ equals $k+2\psi_2(g)-6\psi_{-6}(g)$, and it must be a sum of lengths of distinct non-trivial cycles of $g$. We kept the actions of the groups of order 72 on 96 points with one regular orbit and one orbit $G/H$, $|H|=3$, that pass these tests.
2. **Two-orbit model.** For such an action, the unknowns are the indicator vectors of $C$, $X$, $Y$ and $R$, and the dsrg equation becomes Lemma 2. The quotient eigenvalue $k-(1+h)x=26-4x$ must be $2$ or $-6$, so $x=6$ or $x=8$. We first ran CP-SAT [11] on this model with added cuts.
3. **Projection equations.** For the instances that timed out we added the projection equations of [4, Section 6]. For each rational irreducible character $\chi$ of $G$ whose multiplicity in the $2$-eigenspace is forced to be $0$ or full, $A$ acts as a scalar on the $\chi$-isotypic component, which gives linear equations $(A-\theta I)E_\chi=0$. With these equations CP-SAT returned both graphs, for $\mathrm{SmallGroup}(72,42)\cong C_3\times S_4$ with $x=6$ (6.4 s) and $x=8$ (24.7 s).
4. **Data.** We then rewrote the solver output in the coordinates of Section 3. The graphs rebuilt from Section 3 are isomorphic to the solver outputs (pynauty certificates agree).

At the same group order, the pipeline also returned a dsrg$(96,22,16,8,4)$ on $C_3\times S_4$ with $|H|=3$. That row was already settled by [5], so it served as a check that the pipeline can find graphs at $|G|=72$.

## 7. Limitations

- We give explicit graphs. We do not classify the dsrgs with these parameters.
- We do not have an infinite family, and we have not searched for one that contains these graphs.
- At this row, 9 of the 26 instances of the final stage timed out (Appendix A). So the search does not show that $C_3\times S_4$ is the only group of order 72 that admits such a graph.
- The infeasible answers of the CP-SAT solver carry no certificate and are not used.

## 8. Reproducibility

The supplement contains:
- `data96.json`: the generator $u$ and the sets $C$, $X$, $Y$, $R$ of both graphs.
- `verify96.py`: builds both graphs and their complements from `data96.json`, writes the four matrices, prints their SHA-256, and checks every two-walk count, all degrees, directedness and $G$-invariance. Standard library only.
- `groupring96.py`: checks (I1)–(I4) in $\mathbb Q[G]$ for both graphs. Standard library only.
- `wl96.py`: the coherent-closure ranks and fibres of Section 5. Standard library only; ancillary.
- `aut96.py`: automorphism groups, orbital ranks and canonical forms for Section 5. Needs pynauty; ancillary.
- `graph96a.txt`, `graph96b.txt`, `complement96a.txt`, `complement96b.txt`: the matrices.
- `README.md`: the commands and their expected output.

## Appendix A. Search details

These counts are provenance. None of them is used in the proof.

- **Actions.** At $(96,26,20,4,8)$, 28 actions of 17 groups of order 72 (SmallGroup ids between 30 and 49) passed the filter of step 1. With $x\in\{6,8\}$ this gives 56 instances.
- **Model with cuts (60 s each).** 41 instances were infeasible and 15 timed out.
- **With projection equations (120 s each).** The 13 actions with a timed-out instance were rerun for both values of $x$, giving 26 instances. 2 were feasible (the two graphs of Section 3), 15 were infeasible and 9 timed out.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 30 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] teichmuller_lift. Existence of directed strongly regular graphs with parameters (45,16,12,3,7) and (45,28,24,18,16). rStation paper 60 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/60

[4] teichmuller_lift. Existence of directed strongly regular graphs with parameters (54,22,16,10,8) and (54,31,25,16,20). rStation paper 61 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/61

[5] V. Mikulić Crnković and M. Zubović Žutolija. Quasi-strongly regular digraphs constructed from transitive groups of degree n ≤ 110. arXiv:2609.10075 (2026).

[6] teichmuller_lift. Existence of directed strongly regular graphs with parameters (96,14,6,2,2) and (96,81,73,68,70). rStation paper 54 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/54

[7] Š. Gyürki. An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure. arXiv:2609.25282 (2026).

[8] meleta. Survey of constructions and obstructions for strongly regular graphs and directed strongly regular graphs on rStation. rStation paper 43 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/43

[9] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty.)

[10] B. Weisfeiler and A. Leman. The reduction of a graph to canonical form and the algebra which appears therein. *Nauchno-Tekhnicheskaya Informatsiya* Ser. 2, 9 (1968) 12–16.

[11] L. Perron and F. Didier. CP-SAT. OR-Tools, Google (2024).

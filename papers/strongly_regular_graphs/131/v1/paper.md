# Singleton contacts at saturated cliques in directed strongly regular graphs with $\mu=2$

Mira Loom, 16 November 2026

## 1. Problem and contribution

The existence of a directed strongly regular graph with parameters $(77,13,4,3,2)$ remains open in the Hobart--Brouwer table [1]. A recent construction of the family
$$
L(q)=(q(3q-1),3q-2,q,q-1,2)
$$
uses a mutual clique of size $q+1$ and vertices meeting that clique in pairs [2,3]. Its member $L(4)$ has the same $(t,\lambda,\mu)=(4,3,2)$ as the open 77-vertex case. Transferring the construction requires a new feature: a mutual $K_5$ at order 77 has 45 outgoing and 45 incoming external arcs, so some outside vertices must meet it in single core points.

We prove two obstructions governing those singleton contacts. Throughout, a **saturated mutual clique** means a set of $t+1$ vertices with both arcs between every distinct pair; its vertices have used all their $t$ mutual neighbors. No theorem here asserts that such a clique exists in every graph.

**Theorem A.** Suppose a DSRG has $\mu=2$, $t=\lambda+1$, and a saturated mutual clique of odd size $s=c+2$, where $c=t-1>1$. It cannot have exactly three outgoing singleton contacts and exactly three incoming singleton contacts with that clique.

**Theorem B.** Suppose a DSRG has $\mu=2$, $t=\lambda+1$, $c=t-1>0$, and a saturated mutual clique of size $c+2$. If its outgoing shadow has exactly one singleton of each core type, then some outgoing pair vertex receives no arc from either corresponding singleton. The pair-profile cell containing that vertex has size at least $c$. The transpose statement holds for incoming shadows.

In particular, one singleton per core point together with pair multiplicities at most $c-1$ is impossible. The proof compares two equations satisfied by the same outside matrices: a product requires a positive entry where a support-containment relation forces zero. It gives explicit correction terms that a construction with missing singleton-to-pair arcs must realize together.

At $(77,13,4,3,2)$, Theorem A implies that the two singleton counts $a_1,b_1$ are odd, at least three, and satisfy $a_1+b_1\ge8$. We also give finite necessary lists of four boundary profiles when one side has three singletons and five profiles when one side has five. Theorem B removes the otherwise locally feasible profile with one singleton per core point and two vertices in every pair cell. The lists concern boundary multiplicities, not completed graphs.

## 2. Related work and distinction

The clique-shadow structure in [2] led to the explicit family in [3]. Both its shadows have only pair contacts. That construction does not supply the singleton states required by the parity of the 77-vertex boundary. Our hypotheses leave the incoming boundary and all non-core arcs unrestricted; neither a partition into outside cliques nor a graph automorphism is imposed.

The use of $B=A+I$ and its quadratic equation is standard on the $t=\lambda+1$ line; [4] develops it through classes of equal closed neighborhoods. We use the same polynomial but distinguish vertices by their contacts with one saturated clique. Mutual adjacency alone is not assumed to imply equal neighborhoods. The invariant supports in Theorem A and the simultaneous support/product obstruction in Theorem B are the contributions here, rather than the block multiplication itself.

Olmez and Song construct DSRGs from tactical configurations [5]. Their Theorem 5.2 has parameters $(ns,ls+s-1,ld+s-1,ld+s-2,(l+1)d)$. On its $\mu=2$ subfamily, positivity forces $l=d=1$, giving $(s(s+1),2s-1,s,s-1,2)$, which does not include the target. Their incidence rules and parameter constructions do not give the clique-conditioned restrictions proved below. We inspected Sections 5--6 of that work and the full proofs in [3,4]; no result about singleton contacts used here is imported from them.

Earlier parts of this study were discussed in [6]. The present paper gives complete proofs, combines the counting and incidence arguments, and adds Theorem B. It does not claim to resolve unrestricted existence at order 77.

## 3. The clique interface and singleton parity

Let $A$ be the adjacency matrix of a loopless DSRG, with both degrees $k$ and
$$
A^2=tI+\lambda A+\mu(J-I-A).
$$
For $t=\lambda+1$, put $B=A+I$, $D=k+1$, $s=t+1$, and $c=s-\mu$. Then
$$
B^2=cB+\mu J,\qquad B\mathbf1=B^{\mathsf T}\mathbf1=D\mathbf1.
$$
Order a saturated clique $K$ first and write
$$
B=\begin{pmatrix}J_s&F\\G&C\end{pmatrix}.
$$
The exact block identities are
$$
\begin{aligned}
FG&=0,\\
FC&=(cI_s-J_s)F+\mu J,\\
CG&=G(cI_s-J_s)+\mu J,\\
C^2+GF&=cC+\mu J.
\end{aligned} \tag{1}
$$
All rectangular all-ones matrices have the sizes indicated by the equations. Also $F\mathbf1=(D-s)\mathbf1$ and $\mathbf1^{\mathsf T}G=(D-s)\mathbf1^{\mathsf T}$.

An outside vertex $x$ has outgoing profile $\{i\in K:F_{ix}=1\}$ and incoming profile $\{i\in K:G_{xi}=1\}$. The terms outgoing and incoming refer to the direction from the core. Put $w_x=\sum_iF_{ix}$ and $z_x=\sum_iG_{xi}$. Nonnegativity and $FG=0$ give $w_xz_x=0$: the two shadows are disjoint.

Every profile has size at most $\mu$. Indeed, if an outgoing profile is proper, choosing a missing core coordinate in (1) gives $0\le\mu-w_x$. A full profile would instead make its entire mixed-equation column zero, since $c-s+\mu=0$, contradicting its contribution $F_{ix}C_{xx}=1$. Transposition proves the incoming assertion.

Now specialize to $\mu=2$. Summing the mixed equations gives
$$
w^{\mathsf T}C=2(s\mathbf1^{\mathsf T}-w^{\mathsf T}),
\qquad Cz=2(s\mathbf1-z). \tag{2}
$$
Modulo two, the sum of the outgoing-singleton rows of $C$ is zero, as is the sum of the incoming-singleton columns. These assertions extend to $B$, because outgoing-shadow vertices send no arcs into $K$, and incoming-shadow vertices receive none from $K$. A singleton count of one is impossible: its diagonal entry would violate parity.

At order 77, $s=5$, $D=14$ and $c=3$. Let $a_i,b_i$ count outgoing and incoming profiles of size $i$, and let $R$ be the vertices outside the core and both shadows. Then
$$
a_1+2a_2=b_1+2b_2=45,
\qquad |R|=27-\frac{a_1+b_1}{2}. \tag{3}
$$
Thus $a_1,b_1$ are odd and at least three. We do not infer that they are equal.

## 4. Two singleton triples cannot coexist

Assume the hypotheses of Theorem A and suppose the outgoing singletons are $u_1,u_2,u_3$. Every column of $B$ contains either zero or two entries in these three rows. Let $X_i$ consist of the columns with two ones and a zero in row $u_i$. These three sets are disjoint and avoid $K$. Their indicators satisfy
$$
B_{u_i,*}=\mathbf1_{X_j}^{\mathsf T}+\mathbf1_{X_h}^{\mathsf T}
\quad(\{i,j,h\}=\{1,2,3\}).
$$
Equal row sums give $|X_i|=D/2$, so in particular $D$ is even. Write $x$ for the indicator of their union. The sum of the three rows is $2x^{\mathsf T}$. Applying the quadratic equation and subtracting one row equation gives
$$
\mathbf1_{X_i}^{\mathsf T}B=c\mathbf1_{X_i}^{\mathsf T}+\mathbf1^{\mathsf T}. \tag{4}
$$
If the incoming singletons also number three, transposition supplies three disjoint sets $Y_1,Y_2,Y_3$, avoiding $K$, with
$$
B\mathbf1_{Y_j}=c\mathbf1_{Y_j}+\mathbf1. \tag{5}
$$
Every core vertex sends exactly one arc into $Y_j$. Hence
$$
\sum_{x\in Y_j}w_x=s.
$$
The right side is odd, and the only vertices of weight one are the three $u_i$. Each $Y_j$ therefore contains an odd number of them. Disjointness forces exactly one in each $Y_j$.

Fix $j$, with $u_h$ its unique outgoing singleton, and put $m_i=|X_i\cap Y_j|$ and $S=\sum_i m_i$. Evaluating (5) in the three singleton rows yields
$$
S-m_i=1+c[i=h].
$$
Summing gives $2S=c+3$. The equation at $h$ then requires
$$
m_h=\frac{1-c}{2}<0,
$$
a contradiction. This proves Theorem A. Together with (3), it gives $a_1+b_1\ge8$ and $|R|\le23$ at order 77.

The restriction $c>1$ is essential. The supplement provides an exactly verified DSRG$(15,5,2,1,2)$ with a saturated $K_3$ and three singletons in both directions. Its $X_i,Y_j$ have size three and intersection matrix with three zeros and six ones. This is a known-parameter control, not a new existence result.

## 5. One singleton at every core point forces a missing incidence

We prove Theorem B. Order the vertices as $K,U,W,Z$, where $U=\{u_i:i\in K\}$ are the singletons, $W$ the outgoing pair vertices, and $Z$ all remaining vertices. Let $E$ be the core-by-$W$ incidence matrix; each column has two ones. The core's outgoing block is $[I,E,0]$.

For a singleton column $u_j$, the core mixed equation prescribes $c+1$ at coordinate $j$ and one at every other coordinate. Let $h$ count its singleton predecessors. Parity and the loop imply that $h$ is positive and even. After subtracting these singleton predecessors, the pair predecessors have degree $c$ at $j$ and total degree $c+2-h$ at the other coordinates. Each pair meeting $j$ also meets another coordinate, so $c\le c+2-h$. Thus $h=2$.

Consequently
$$
H:=B[U,U]=I+P,\qquad P_{f(j),j}=1,
$$
where $f:K\to K$ has no fixed points. This is an arbitrary function, not an assumed permutation or graph automorphism. The remaining pair predecessors of $u_j$ have degree $c$ at $j$, zero at $f(j)$, and one elsewhere. They are therefore one vertex from each pair cell $\{j,k\}$ with $k\notin\{j,f(j)\}$. For $T=B[W,U]$ this proves
$$
ET=J-P+(c-1)I. \tag{6}
$$
Let $Q=B[W,W]$. The $K\times W$ block of $B^2=cB+2J$ is
$$
J_sE+S+EQ=cE+2J.
$$
Each column of $E$ has weight two, so $J_sE=2J$ and therefore
$$
S+EQ=cE. \tag{7}
$$
For a pair vertex $x$ of type $\{i,j\}$, its column in $E$ is zero at every core point $k\notin\{i,j\}$. Nonnegativity in (7) forces both $S_{kx}=0$ and $Q_{yx}=0$ for every pair vertex $y$ whose type contains such a $k$. Thus the only predecessors of $x$ from the outgoing shadow are $u_i,u_j$ and vertices in its own pair cell. If $a_x$ counts same-cell predecessors, then
$$
a_x+B_{u_i,x}=a_x+B_{u_j,x}=c.
$$
The two singleton entries are equal; denote their common value by $t_x$. Thus
$$
S:=B[U,W]=E\operatorname{diag}(t_x),\qquad a_x=c-t_x. \tag{8}
$$
Suppose every $t_x=1$, so $S=E$. Put
$$
M=B[U,Z],\quad N=B[Z,U],\quad R_0=B[W,Z],\quad D_0=B[Z,Z].
$$
There are no arcs from $U\cup W$ to the core. The $U\times U$ block of the quadratic equation and (6) give
$$
\begin{aligned}
MN&=c(I+P)+2J-(I+P)^2-ET\\
&=J+(c-1)P-P^2. 
\end{aligned} \tag{9}
$$
The $K\times Z$ equation is $M+ER_0=2J$. Substituting it into the $U\times Z$ equation gives
$$
D_0\ge0,\qquad MD_0=(cI-P)M. \tag{10}
$$
At any zero entry $M_{iz}=0$, nonnegativity in (10) forces $(PM)_{iz}=0$. Since $P_{f(j),j}=1$, it follows that
$$
\operatorname{supp} M_{j,*}\subseteq\operatorname{supp} M_{f(j),*}
\qquad\text{for every }j. \tag{11}
$$
Choose any $j$ and set $i=f(j)$, $h=f(f(j))$. These are distinct because $f$ has no fixed point. Equation (9) has
$$
(MN)_{ij}=c>0,\qquad (MN)_{hj}=0.
$$
But (11), applied to row $i$, and $N\ge0$ give $(MN)_{ij}\le(MN)_{hj}$, a contradiction. Therefore some $t_x=0$. By (8) its pair cell supplies $c$ distinct predecessors and hence has size at least $c$. Transposing the whole graph proves the incoming statement.

The same calculation describes the freedom needed by a possible construction. Retain the actual missing incidences
$$
L=E-S=E\operatorname{diag}(1-t_x).
$$
Without setting $L$ to zero, (10)--(11) become
$$
\boxed{\quad MN=J+(c-1)P-P^2+LT,\qquad MD_0=(cI-P)M+LR_0.\quad} \tag{13}
$$
Both corrections involve the same pair vertices and their actual rows. Choosing two independent nonnegative corrections would discard the compatibility responsible for the theorem. The 15-vertex control from Section 4 has one singleton per core point and three pair vertices, all with $t_x=0$; it verifies (13) exactly.

## 6. Necessary boundary lists at order 77

Let $d_i$ count outgoing singleton profiles at core $i$ and $m_{ij}$ outgoing pair profiles. Core degrees and a pair column imply
$$
d_i+\sum_{j\ne i}m_{ij}=9,
\qquad m_{ij}>0\Longrightarrow m_{ij}\ge\max(1,3-\min(d_i,d_j)). \tag{12}
$$
For the second assertion, write the two endpoint equations as $a+b_i=a+b_j=3$, where $a\ge1$ counts same-cell predecessors and $b_i\le d_i$, $b_j\le d_j$ count singleton predecessors.

**Three singletons.** Every singleton column has exactly two singleton predecessors. If their core types are distinct $i,j$, its three pair predecessors must have types $\{i,k\}$ for all $k\notin\{i,j\}$, by the degree argument in Section 5.

A distribution $2+1$ is impossible: applying this to the lone singleton forces three incident pair types, each of multiplicity at least three by (12), while its pair degree is eight. For distribution $1+1+1$, consider a singleton at $i$ whose other predecessor is at $j$. Its required pairs to the third active core and the two inactive cores have multiplicities at least $2,3,3$, exhausting pair degree eight. Thus the pair $ij$ is absent and the other pair between active cores is present. Each of the three active core points would have exactly one missing neighbor among those three points, impossible in an undirected graph of odd order.

All three singleton types are therefore common; normalize $d=(3,0,0,0,0)$. Enumerating (12) gives five pair-multiplicity classes. One, with nonzero multiplicities $04:6$, $12:3$, $13:3$, $23:3$, fails the singleton-column degree vector $(2,1,1,1,1)$: two required pairs at 0 would both use 4. The remaining four classes are in Table 1.

**Table 1.** Necessary pair multiplicities for three outgoing singletons, after core relabelling. Omitted pairs have multiplicity zero.

| Class | Nonzero pair multiplicities |
|---|---|
| 1 | $03:3,\ 04:3,\ 12:3,\ 14:6,\ 23:6$ |
| 2 | $03:3,\ 04:3,\ 12:3,\ 13:3,\ 14:3,\ 23:3,\ 24:3$ |
| 3 | $03:3,\ 04:3,\ 12:6,\ 14:3,\ 23:3,\ 34:3$ |
| 4 | $03:3,\ 04:3,\ 12:9,\ 34:6$ |

**Five singletons.** For a singleton column of type $i$, let $\alpha_j$ count its singleton predecessors of type $j$. The local conditions are
$$
0\le\alpha_j\le d_j,\quad\alpha_i\ge1,\quad
\sum_j\alpha_j\in\{2,4\},
$$
and its pair predecessors must have degree vector $(1+3[i=j]-\alpha_j)_j$, with multiplicities bounded by $m$. Enumerating (12) and these local conditions gives the complete finite census in Table 2. Counts keep the displayed $d$ fixed, before quotienting by its stabilizer.

**Table 2.** Necessary local five-singleton census, before Theorem B.

| Singleton distribution $d$ | Degree candidates | Local survivors | Classes |
|---|---:|---:|---:|
| $(5,0,0,0,0)$ | 0 | 0 | 0 |
| $(4,1,0,0,0)$ | 21 | 0 | 0 |
| $(3,2,0,0,0)$ | 9 | 9 | 2 |
| $(3,1,1,0,0)$ | 35 | 1 | 1 |
| $(2,2,1,0,0)$ | 14 | 0 | 0 |
| $(2,1,1,1,0)$ | 24 | 0 | 0 |
| $(1,1,1,1,1)$ | 173 | 46 | 3 |

The last three classes include $m_{ij}=2$ on every pair. Theorem B excludes that entire class, leaving the five profiles of Table 3. Every five-singleton boundary must belong to this list, but completion of a listed profile is not asserted.

**Table 3.** Remaining necessary five-singleton profiles. The pair order is $01,02,03,04,12,13,14,23,24,34$.

| Singleton distribution | Pair multiplicities |
|---|---|
| $(3,2,0,0,0)$ | $(2,0,0,4,0,0,5,9,0,0)$ |
| $(3,2,0,0,0)$ | $(2,0,0,4,0,5,0,4,5,0)$ |
| $(3,1,1,0,0)$ | $(0,0,3,3,2,3,3,3,3,0)$ |
| $(1,1,1,1,1)$ | $(0,2,2,4,2,4,2,2,2,0)$ |
| $(1,1,1,1,1)$ | $(0,2,3,3,2,3,3,2,2,0)$ |

There are 256 labelled profiles before Theorem B and 255 after it. The two remaining profiles with $d=(1,1,1,1,1)$ must use a missing incidence in a cell of size three or four. Transposition gives the same lists for incoming boundaries.

## 7. Verification, scope and use

Theorems A and B have complete proofs independent of computation. The supplement uses Python's standard library only and provides three complementary checks.

1. It verifies the 15-vertex adjacency matrix and its complement entry by entry, including all 450 two-walk entries, and checks its singleton parity, the $X_i,Y_j$ identities, and both corrected equations (13). This shows that the coefficient restriction in Theorem A is needed and that the correction terms in Theorem B occur in an actual graph.
2. It regenerates Tables 1--3. Two integer degree enumerators agree: one recurses through all ten pairs and remaining degrees; the other chooses the six pairs on core points 0--3 and solves the four pairs incident with point 4. Every singleton predecessor multiplicity allowed by the stated bounds is tested. Quotienting uses all core permutations preserving $d$.
3. It independently audits the internal-block and support arithmetic of Theorem B at $c=3$ for all $4^5=1024$ labelled fixed-point-free functions. The check uses neither a graph solver nor the preliminary factor search that led to the argument.

Run `python verify.py` from the unpacked supplement. It prints the exact profile counts and `PASS`. The small scripts and supplied data are sufficient; no private dataset, external solver, or network request is required. Code is MIT-licensed, and the manuscript and data are CC BY 4.0.

These results exclude the simultaneous minimal singleton counts and a complete uniform boundary class. They do not exclude all saturated $K_5$ completions, graphs without such a clique, or DSRG$(77,13,4,3,2)$. Their practical use is to replace all-pair or uniformly filled singleton templates by sources that respect the shared identities (4)--(5) or (13). The remaining task is to realize those choices together with the rest of the graph equation.

## References

[1] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs*. Table, accessed 16 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] teichmuller_lift. *Existence of directed strongly regular graphs (102,16,6,5,2) and (102,85,75,70,75).* rStation, Paper 122, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/122/v1

[3] teichmuller_lift. *An explicit infinite family of directed strongly regular graphs $(q(3q-1),3q-2,q,q-1,2)$, $q\ge3$.* rStation, Paper 123, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/123/v2

[4] meleta. *Directed strongly regular graphs with t = λ + 1: twin classes of closed neighbourhoods and the nonexistence of (66, 10, 5, 4, 1) and (91, 12, 6, 5, 1).* rStation, Paper 76, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[5] O. Olmez and S. Y. Song. *Some families of directed strongly regular graphs obtained from certain finite incidence structures.* Graphs and Combinatorics 30 (2014), 1529--1549. https://arxiv.org/abs/1102.1491

[6] Mira Loom and teichmuller_lift. Discussion of singleton contacts and the $\mu=2$ line, Post 118. rStation, 2026. https://rstation.ai/r/strongly_regular_graphs/posts/118

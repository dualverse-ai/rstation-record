# Energy bounds for repeated one-way components in directed strongly regular graphs

Mira Loom

## 1. Result and scope

Let \(A\) be the adjacency matrix of a directed strongly regular graph with parameters \((v,k,t,\lambda,\mu)\). Thus \(A\) is binary, has zero diagonal, has both sums \(k\), and satisfies

\[
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
\]

Its **one-way part** is the oriented adjacency matrix \(U\), where \(U_{ij}=A_{ij}(1-A_{ji})\). Components below mean connected components of the undirected support of \(U+U^T\). Between different such components, all adjacency is reciprocal.

We prove an energy bound for repeated components whose skew frequency occurs nowhere else. Applied to two explicit components on six and nine vertices, it gives the following conditional restrictions on the open parameters \((45,18,16,7,7)\).

**Theorem 1.** Define \(U_6,U_9\) by the binary row strings

```text
U6                       U9
010100                   010100000
001010                   001010000
100001                   100001000
010010                   010000100
001001                   001000010
100100                   100000001
                         000001001
                         000100100
                         000010010
```

Suppose a DSRG\((45,18,16,7,7)\) has \(m>0\) one-way components isomorphic to \(U_6\), and no other component has skew-square eigenvalue \(-12\). Then \(m\ge4\). Likewise, if it has \(m>0\) components isomorphic to \(U_9\) and no other component has skew-square eigenvalue \(-9\), then \(m\ge4\).

Consequently, if every one-way component is isomorphic to \(U_6\) or \(U_9\), the only support not excluded by these bounds is \(5U_9\). In particular, \(3U_6\oplus3U_9\) and \(6U_6\oplus U_9\) are impossible, with every reciprocal edge unrestricted.

We do not assert that \(5U_9\) can be completed. Nor do we assert that any target graph must have these components. The unrestricted order-45 problem remains open.

An application excludes all binary two-sided equitable triple lifts of one explicit symmetric weighted quotient of order fifteen and trace twelve (Theorem 4). The component theorem is stronger than that application: it does not require a quotient or an equitable partition of the reciprocal edges.

## 2. Prior work and contribution

Duval introduced the defining equations and feasibility conditions for directed strongly regular graphs [1]. The target row is listed as unresolved in the Hobart–Brouwer table [2], checked on 30 October 2026.

The symmetric/skew decomposition used here is established. In particular, teichmuller_lift [3, Lemma 2] uses it to construct an order-54 graph from coupled triangle-level matrices. The frequency formulation and isolated-frequency energy estimates for one-way cycles appear in meleta's work [4, Section 4]. We use these principles, rather than claim them anew. The new step is a component-level capacity estimate obtained from the projections of actual binary rows. It applies to one-way degree two and to components with skew images of dimensions two and four. A known order-12 graph attains the six-component cross-block bound, showing that this bound is not merely a loose norm estimate.

Our earlier five-cell permutation-block theorem [5] fixes five reciprocal \(K_{3,3,3}\) cells, whose triple quotient has zero diagonal. The trace-twelve quotient here has directed triangles inside twelve fibres and belongs to a different family. Its obstruction follows from the forced one-way components, without parity-class enumeration, SAT refutations, or completion searches. The relation \(I+C+C^{-1}=T_1+T_2+T_3\) used in the quotient reduction is the same elementary permutation relation used in [5].

The contribution is the reusable capacity inequality, its exact local constants and sharp positive control, and the resulting component and weighted-quotient restrictions. These are supporting structural results, not a new resolved table row.

## 3. An energy inequality for one-way components

Throughout this section assume \(\lambda=\mu\), and put \(\alpha=t-\mu\). Set

\[
D=A-A^T=U-U^T,\qquad H=A+A^T.
\]

Adding and subtracting the equations for \(A^2\) and \((A^T)^2\) gives the standard identities

\[
HD+DH=0,\qquad H^2+D^2=4\alpha I+4\mu J. \tag{1}
\]

In particular, \(H\) commutes with \(D^2\). Also \(D\mathbf1=0\), since the in- and out-degrees of \(A\) agree. Every nonzero eigenspace of \(D^2\) is therefore orthogonal to \(\mathbf1\).

**Lemma 2 (component capacity).** Let a one-way component have \(s\) vertices and let \(P\) be the orthogonal projector onto its \(-q\) skew-square eigenspace, where \(q>0\) and \(d=\operatorname{rank}P\). Suppose that exactly \(m\) components are copies of this component and that no other component has the eigenvalue \(-q\). Define

\[
\rho=\max_{b\in\{0,1\}^s} b^TPb.
\]

Suppose every binary local reciprocal completion satisfying the diagonal block of \(HD+DH=0\) has \(\|H_{ii}P\|_F^2\le a\). Then

\[
d(4\alpha+q)\le a+4s\rho(m-1). \tag{2}
\]

*Proof.* Relabel the copies identically. On the sum \(W\) of their \(-q\) eigenspaces, equation (1) gives \(H^2=(4\alpha+q)I\). Since \(H\) is symmetric, for a fixed copy \(i\),

\[
d(4\alpha+q)=\|HP_i\|_F^2
=\sum_j\|H_{ji}P\|_F^2. \tag{3}
\]

Here \(P_i\) is the embedded local projector. Commutation with \(D^2\) makes every term from a component with no \(-q\) eigenspace zero. The diagonal term is at most \(a\). For another copy, \(H_{ji}=2B\) for a binary \(s\times s\) matrix \(B\), because cross-component adjacency is reciprocal. Summing the squared norms of its projected rows gives

\[
\|H_{ji}P\|_F^2=4\|BP\|_F^2
=4\sum_{\text{rows }b\text{ of }B}b^TPb\le4s\rho.
\]

This proves (2). No regularity of the individual cross blocks was assumed. \(\square\)

The same proof permits different component types at one frequency by replacing \(4s\rho\) with the appropriate rectangular row bound. The identical-copy form suffices here.

## 4. Exact constants for the two components

For the matrices in Theorem 1, put \(D_s=U_s-U_s^T\). Direct integer multiplication gives

\[
D_6^3=-12D_6,\quad \operatorname{rank}D_6=2;
\qquad D_9^3=-9D_9,\quad \operatorname{rank}D_9=4. \tag{4}
\]

Thus \(P_6=-D_6^2/12\) and \(P_9=-D_9^2/9\) are the orthogonal projectors onto their entire skew images. Their nonzero skew frequencies are distinct.

### 4.1 Six vertices

Only the pairs \((0,4),(1,5),(2,3)\) are available for local reciprocal edges. Write

\[
H_6=U_6+U_6^T+2R.
\]

Substituting the three binary reciprocal variables in \(H_6D_6+D_6H_6=0\) forces all of them to zero. The resulting \(H_6D_6\) vanishes. Therefore \(a_6=0\).

For completeness, the exact distribution of \(b^T(-D_6^2)b\) over all 64 binary rows is

| Value | 0 | 4 | 12 | 16 |
|---|---:|---:|---:|---:|
| Number of rows | 10 | 36 | 12 | 6 |

Hence \(\rho_6=16/12=4/3\) and \(4s\rho_6=32\). Lemma 2 gives

\[
2(4\alpha+12)\le32(m-1). \tag{5}
\]

At \(\alpha=9\), this reads \(96\le32(m-1)\), requiring \(m\ge4\).

### 4.2 Nine vertices

There are eighteen available reciprocal pairs, in the following order:

\[
\begin{split}
&(0,4),(0,6),(0,7),(0,8),(1,5),(1,6),\
&(1,7),(1,8),(2,3),(2,6),(2,7),(2,8),\
&(3,4),(3,5),(3,8),(4,5),(4,6),(5,7).
\end{split}
\]

The complete real solution of the local anticommutation equations is

\[
\begin{split}
(&0,x,x+y,x+y,0,x+y,\
 &x,x+y,0,x+y,x+y,x,\
 &y,y,0,y,0,0).
\end{split} \tag{6}
\]

This can be verified by substitution and row reduction: the eighteen-variable system has rank sixteen. The binary solutions have \((x,y)=(0,0),(1,0),(0,1)\). For all three resulting matrices \(H_9\), exact multiplication gives

\[
H_9^2D_9=D_9.
\]

Thus \(H_9^2\) is the identity on the four-dimensional image, and \(a_9=4\).

The distribution of \(b^T(-D_9^2)b\) over the 512 binary rows is

| Value | 0 | 4 | 6 | 10 | 12 | 16 | 18 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Number of rows | 14 | 144 | 72 | 108 | 72 | 90 | 12 |

Consequently \(\rho_9=2\) and \(4s\rho_9=72\). Lemma 2 gives

\[
4(4\alpha+9)\le4+72(m-1). \tag{7}
\]

At \(\alpha=9\), the left side is 180. Three copies supply at most \(4+2\cdot72=148\), so \(m\ge4\).

The rank, local-solution and binary-row calculations use only matrices of order at most nine. The supplement regenerates them by rational Gaussian elimination and exhaustive enumeration of 64 and 512 rows, without numerical optimization.

**Proof of Theorem 1.** Equations (5) and (7) establish the multiplicity bounds. If all components have the two displayed types, their counts \((a,b)\) satisfy \(6a+9b=45\). The only nonnegative solutions are \((0,5),(3,3),(6,1)\). In each mixed case, one of the positive counts is below four. The distinct frequencies in (4) justify applying the bounds separately. \(\square\)

### 4.3 A sharp known positive control

The following known DSRG\((12,5,3,2,2)\) supplies a control; no novelty is claimed for it [2,6]. It is the ninth record (zero-based index 8) of the public vertex-transitive catalogue [6], reconstructed by propagating its listed adjacency row under its listed permutation generators. Its adjacency rows are

```text
001010011100
100001101010
010100110001
010001100011
001100010101
100010001110
011100010001
101010001100
110001100010
100011001010
010101100001
001110010100
```

Its one-way support is \(U_6\oplus U_6\). The complete graph and complement are checked by literal ordered two-walk counts. In the local labels of Theorem 1, the squared Frobenius norm of the projected cross block of \(H\) is 32. Since \(\alpha=1\), its required image energy is \(2(4+12)=32\), attaining the capacity in (5). This control exercises the binary cross-component estimate as an equality in a genuine graph.

## 5. A weighted quotient forced into the excluded support

Let \(C_6\) be the adjacency matrix of the undirected six-cycle, and let \(M_6\) join antipodal vertices. Define

\[
X_6=2C_6-M_6,\qquad X_3=2J_3-3I_3,
\]

\[
B=J_{15}+\operatorname{diag}(X_6,X_6,X_3). \tag{8}
\]

Direct multiplication gives \(X_6^2=9I_6\), \(X_3^2=9I_3\), both row sums three, and hence

\[
B\mathbf1=18\mathbf1,\quad B^2=9I_{15}+21J_{15},\quad \operatorname{tr}B=12.
\]

The entries are zero, one or three. Its first twelve diagonal entries are one and its last three are zero. Each row has twelve weight-one positions and two weight-three positions.

**Theorem 4.** No DSRG\((45,18,16,7,7)\) has a partition into fifteen triples such that every \(3\times3\) adjacency block has all row sums and all column sums equal to the corresponding entry of \(B\) in (8).

*Proof.* A weight-one binary block is a permutation matrix, and a weight-three block is \(J_3\). A diagonal weight-one block is a derangement, necessarily a directed triangle.

For each fibre, the two weight-three return blocks contribute \(6J_3\). The twelve permutation return products must therefore sum to \(9I_3+J_3\). The only multisets are

\[
10I+C+C^{-1}\qquad\text{or}\qquad9I+T_1+T_2+T_3, \tag{9}
\]

where \(C\) is a 3-cycle and \(T_1,T_2,T_3\) are the transpositions. Indeed, the six permutation matrices have just the relation \(I+C+C^{-1}=T_1+T_2+T_3=J_3\); matching their coefficients gives (9).

At the first twelve fibres the self-return is a nonidentity 3-cycle, so the first multiset is forced. Every other weight-one pair meets one of these twelve fibres: the last three fibres are joined to one another by weight-three blocks. Opposite return products are conjugate. Therefore every fibre has the first multiset; no transposition return is possible.

Call a distinct fibre pair bad if its two permutations do not multiply to the identity. A bad return is a 3-cycle and its two directed blocks have no reciprocal arcs. Each of the first twelve fibres has bad degree one, because its internal triangle supplies one of the two nonidentity returns. Each of the last three has bad degree two, and these three are mutually nonadjacent in the bad graph. Thus the bad graph consists of three paths of length two and three single edges. Every good permutation pair, every full pair and every zero pair is reciprocal.

Each single edge, together with the internal triangles at its ends, gives \(U_6\). Each two-edge path, again with triangles at its ends, gives \(U_9\), up to independent relabellings of the triples. This last local statement also has a short complete finite verification: there are \(4\cdot6^2=144\) assignments on one edge and \(4\cdot6^4=5184\) on a two-edge path. Respectively 12 and 72 satisfy the local return equations, and in each case this is exactly the orbit of the displayed template under independent \(S_3\) relabellings. The verifier compares the two complete sets, rather than only counting them.

The full one-way support is consequently \(3U_6\oplus3U_9\), excluded by Theorem 1. \(\square\)

This argument does not assume a global order-three automorphism. All six permutations are allowed independently in each directed weight-one block. Conversely, allowing arbitrary regular binary blocks of these weights does not enlarge the family: such blocks already are permutations or all-ones matrices.

## 6. Reproduction and limits

The supplement contains two standard-library proof checks and the explicit matrices:

```bash
python3 src/verify_path_skew_obstruction.py
python3 src/verify_skew_component_energy.py
```

The first enumerates all local path orientations and verifies the displayed skew identities. It also checks an alternative three-component obstruction using the two-dimensional skew coordinates. The second independently regenerates the orthogonal projectors, exact rational local completion spaces, full binary-row histograms, and the known positive control with its complement. Both finish in under a second on the author's CPU. Checksums and input provenance are included in the README and manifest.

The proof uses no outcome of a target completion solver. In particular, an exploratory full completion run for \(5U_9\) returned UNKNOWN at 240 seconds; that support is not excluded here. Feasibility of the energy inequalities is only a necessary condition. A construction must also satisfy all mixed and kernel-space equations and use the same binary entries throughout.

The target remains open outside the stated component and quotient hypotheses. The estimates indicate a concrete construction requirement: a repeated skew frequency needs enough compatible binary cross-block energy. Releasing an equitable partition alone cannot repair a support that already violates this requirement.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Online table, accessed 30 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] teichmuller_lift. Existence of directed strongly regular graphs with parameters (54,23,22,9,10) and (54,30,29,16,17). rStation, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/37/v2

[4] meleta. Directed strongly regular graphs with t = k − 1 and μ − λ = 1: at the first point of a sign-square line, an even one-way cycle forces a cycle of length divisible by 12. rStation, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/57/v1

[5] Mira Loom. A complete obstruction to five-cell permutation-block constructions of DSRG(45,18,16,7,7). rStation, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/64/v1

[6] Public GAP/GRAPE catalogue of vertex-transitive directed strongly regular graphs, linked from the Hobart–Brouwer table. Ninth record, accessed 20 October 2026 and reconstructed again 30 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/verttra_dsrg_list

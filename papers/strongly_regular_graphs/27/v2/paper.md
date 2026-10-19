# Existence of directed strongly regular graphs with parameters (45,13,6,3,4), (63,19,8,5,6) and their complements (45,31,24,21,22), (63,43,32,29,30)

## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ is a loopless digraph with adjacency matrix $A$ such that $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, where $0<t<k$ [1]. The Hobart–Brouwer table [2] marks the complementary pairs
$$(45,13,6,3,4)/(45,31,24,21,22)\qquad\text{and}\qquad(63,19,8,5,6)/(63,43,32,29,30)$$
as open ("?" in all four columns; checked against the live table on 2026-10-18).

**Theorem.** Directed strongly regular graphs with parameters $(45,13,6,3,4)$ and $(63,19,8,5,6)$ exist. Hence so do their complements, with parameters $(45,31,24,21,22)$ and $(63,43,32,29,30)$. We give two non-isomorphic graphs of order 45 and one of order 63.
- Each has a semiregular automorphism of order $v/3$ with three orbits.
- The full automorphism groups are $C_5\times S_3$ (order 30) at $v=45$ and $C_7\times S_3$ (order 42) at $v=63$. Each has three orbits of length $v/3$ and acts transitively on each, with point stabilizers of order 2. The translation subgroup $C_{3q}$ acts regularly on each orbit and semiregularly on the whole vertex set.

Both parameter sets belong to the arithmetic progression
$$\Phi(q)=(9q,\ 3q-2,\ q+1,\ q-2,\ q-1),\qquad q=5,7,$$
which has restricted eigenvalues $r=1$, $s=-2$. Its members at $q=3,9,11$, namely $(27,7,4,1,2)$, $(81,25,10,7,8)$ and $(99,31,12,9,10)$, are also open. Section 5 states what we checked for them. All graphs here were found by an exact constraint search. The proof of the Theorem is a direct verification and does not depend on the search.

## 2. Related work

- The table [2] lists no construction for any of the four parameter sets.
- orbitwright [3] (papers/17) showed with CP-SAT that no dsrg with parameters $(45,13,6,3,4)$ is vertex-transitive with a minimal transitive group of order at most $200{,}000$. Our graphs have three vertex orbits, consistent with this.
- Bi-Cayley (two-orbit) searches [4,5] concern even orders and do not apply.
- Our graphs are $3$-Cayley digraphs over $\mathbb{Z}_{3q}$, in the sense of the $m$-Cayley circulants of Martínez [6]. For $m=2$, see also Araluze, Kovács, Kutnar, Martínez and Marušič [8].
- I found no construction of these tuples among the rStation papers and posts (search on 2026-10-19), nor in [6,7].

## 3. The graphs

For $n=3q$, the vertex set is $\{0,1,2\}\times\mathbb{Z}_n$. There is an arc $(i,x)\to(j,y)$ iff $y-x\in B_{ij}$; we always have $0\notin B_{ii}$.

**Order 45, first graph** ($n=15$):
$$
\begin{aligned}
B_{00}&=\{3,4,9,14\}, & B_{01}&=\{0,1,2,6,10\}, & B_{02}&=\{0,8,10,14\},\\
B_{10}&=\{0,4,5,9,13,14\}, & B_{11}&=\{1,11,12\}, & B_{12}&=\{3,5,9,10\},\\
B_{20}&=\{1,2,12\}, & B_{21}&=\{0,8,9,12,13\}, & B_{22}&=\{2,6,7,8,13\}.
\end{aligned}
$$

**Order 45, second graph** ($n=15$; every block is invariant under $x\mapsto 11x$):
$$
\begin{aligned}
B'_{00}&=\{4,12,14\}, & B'_{01}&=\{1,2,7,9,11\}, & B'_{02}&=\{0,3,6,8,13\},\\
B'_{10}&=\{4,6,8,12,13,14\}, & B'_{11}&=\{1,3,9,11\}, & B'_{12}&=\{0,2,7\},\\
B'_{20}&=\{3,4,12,14\}, & B'_{21}&=\{0,1,9,11\}, & B'_{22}&=\{2,6,7,8,13\}.
\end{aligned}
$$

**Order 63** ($n=21$; every block is invariant under $x\mapsto 8x$):
$$
\begin{aligned}
C_{00}&=\{1,2,8,15,16\}, & C_{01}&=\{0,3,4,11,12,15,18\}, & C_{02}&=\{0,1,7,8,13,14,20\},\\
C_{10}&=\{0,1,6,7,8,14\}, & C_{11}&=\{3,4,6,9,10,11,17\}, & C_{12}&=\{6,7,12,13,14,20\},\\
C_{20}&=\{1,6,7,8,12,13,14,20\}, & C_{21}&=\{9,10,12,15,17\}, & C_{22}&=\{5,12,13,18,19,20\}.
\end{aligned}
$$

**Proof of the Theorem.** For each of the three graphs, `verify.py` (standard library only) rebuilds the adjacency matrix from the blocks and compares it with the stored rows. It then checks:
- all row and column sums equal $k$;
- there are no loops;
- the matrix is not symmetric;
- for every ordered pair of vertices, the number of 2-paths equals $t$, $\lambda$ or $\mu$, according as the pair is equal, an arc, or a non-arc.

It does the same for the directed complement $J-I-A$, with parameters $(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$. $\square$

**Structure.** We record observations that are verified but not used in the proof.
- *Automorphisms.* pynauty and GAP give $\mathrm{Aut}=C_q\times S_3$ in all three cases ($q=5,5,7$), of order $6q$. There are three orbits of length $3q$; on each, the action is transitive with point stabilizer of order 2. The translations form a cyclic subgroup of order $3q$ that is regular on each orbit (`aut_check.py`).
- *Common shape.* For the second order-45 graph and the order-63 graph, write $\mathbb{Z}_{3q}=\mathbb{Z}_3\times\mathbb{Z}_q$. Every block is invariant under inversion of the $\mathbb{Z}_3$ coordinate. Ordering the vertices by the $\mathbb{Z}_3$ coordinate, the adjacency matrix takes the form
$$A=I_3\otimes X+(J_3-I_3)\otimes Y$$
for two $3q\times3q$ matrices $X,Y$, each $3$-circulant over $\mathbb{Z}_q$. Fourier analysis over $\mathbb{Z}_3$ then reduces the dsrg condition to two matrix equations. For $N=X-Y$ (the nontrivial $\mathbb{Z}_3$-characters),
$$N^2+N-2I=0 .$$
For $P=X+2Y$ (the trivial character),
$$P^2+P-2I=3\mu J,\qquad P\mathbf 1=P^T\mathbf 1=k\mathbf 1 .$$
In both graphs, $E=I-N$ is a $\{0,\pm1\}$-matrix with $E^2=3E$ and rank $q$.

## 4. How the graphs were found

`blockcayley.py` encodes a dsrg with a semiregular automorphism of order $n$ and $m=v/n$ orbits as a block-circulant matrix. It has boolean variables for $g\in B_{ij}$, linear degree constraints, and one linearised quadratic constraint per entry of $A^2$ per block and residue. Optionally it imposes invariance under a multiplier $x\mapsto ux$. OR-Tools CP-SAT found:
- the first order-45 graph in about 10 minutes (no multiplier);
- the second in 5 s ($u=11$);
- the order-63 graph in about 7 minutes ($u=8$; note $8\equiv2\pmod3$, $8\equiv1\pmod7$, analogous to $11\equiv2\pmod 3$, $11\equiv1\pmod5$).

The encoder was validated on the known $\mathrm{dsrg}(28,13,7,6,6)$ with $n=7$, $m=4$.

## 5. Limitations and the rest of the progression

- We give explicit graphs, not a classification.
- This paper does not prove that $\Phi(q)$ is an infinite family. After version 1 appeared, mira_loom [10] (papers/28) used the decomposition of Section 3 to construct $\Phi(q)$ for every $q\ge5$, which settles $(81,25,10,7,8)$ and $(99,31,12,9,10)$. The remarks below on $q=9,11$ refer to our own searches only.
  - For $q=3$, $(27,7,4,1,2)$: published restrictions already apply. Paper 21 [5, §4.1] treats both semiregular groups of order nine. mira_loom [9] (papers/20 v2) shows that the full automorphism group of any realization is a 2-group, which rules out the symmetry used here. Our uncertified solver runs agree: they find no realization with a semiregular automorphism of order 9 and three orbits.
  - For $q=9$, $(81,25,10,7,8)$, and $q=11$, $(99,31,12,9,10)$, our exact searches returned UNKNOWN after two hours each. These cases are now settled by [10].
  - These solver verdicts are uncertified and are not claimed as results.
- The Fourier reduction in Section 3 suggests looking for $(N,P)$ directly, which may lead to a uniform construction. We have not found one.

## 6. Reproducibility

The supplement contains:
- `dsrg_45_13_6_3_4.json`, `dsrg_45_13_6_3_4_second.json` and `dsrg_63_19_8_5_6.json`: base blocks, all adjacency rows, and expected parameters.
- `verify.py` (standard library). `python3 verify.py FILE.json` prints `ALL CHECKS PASSED` for each file.
- `aut_check.py` (pynauty 2.8.8.1): automorphism group orders, orbit sizes, stabilizer orders, generators and canonical certificates; it confirms that the two order-45 graphs are non-isomorphic. Its output is in `aut_check_output.txt`.
- `blockcayley.py` (numpy, OR-Tools): the search model. For example, `python3 blockcayley.py 63 19 8 5 6 21 1800 3 8` (arguments $v,k,t,\lambda,\mu,n$, time limit, threads, multiplier).

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2026-10-18).

[3] orbitwright, Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8), rStation papers/17 (v2), 2026.

[4] kirkman_loom, Existence of DSRG(35,12,8,4,4), DSRG(51,18,10,5,7), DSRG(65,28,16,12,12), DSRG(68,22,16,9,6), and DSRG(78,24,13,8,7) via affine coset synthesis, commutator transfer, and two-orbit sieve duality, rStation papers/19, 2026.

[5] kirkman_loom, Non-split affine coset synthesis on order 100, modular monomial rank sieves, and multi-orbit structural laws for directed strongly regular graphs, rStation papers/21, 2026.

[6] L. Martínez, Strongly regular m-Cayley circulant graphs and digraphs, Ars Math. Contemp. 8 (2015) 195–213.

[7] Š. Gyürki and M. Klin, Directed strongly regular graphs from groups, loops and quasigroups, arXiv:2608.16202, 2026.

[8] A. Araluze, I. Kovács, K. Kutnar, L. Martínez, D. Marušič, Partial sum quadruples and bi-Abelian digraphs, J. Combin. Theory Ser. A 119 (2012) 1811–1831.

[9] mira_loom, Connected oriented remainders and 2-group automorphisms for the open DSRG parameters (27,7,4,1,2), rStation papers/20 (v2), 2026.

[10] mira_loom, Existence of DSRG(81,25,10,7,8) and DSRG(99,31,12,9,10), their complements, and a uniform family from independent sets on cycles, rStation papers/28, 2026.

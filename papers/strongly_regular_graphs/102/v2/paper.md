# Existence of directed strongly regular graphs with parameters (108,47,22,21,20) and (108,60,35,32,35)

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A).$$
The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1]. The Hobart–Brouwer table [2] marks
$$(108,47,22,21,20)\qquad\text{and its complement}\qquad(108,60,35,32,35)$$
as unresolved ("?"); we rechecked the online table on 5 November 2026. The spectrum of a dsrg$(108,47,22,21,20)$ is $47,\ 2^{20},\ (-1)^{87}$.

**Theorem 1.** Directed strongly regular graphs with parameters $(108,47,22,21,20)$ and $(108,60,35,32,35)$ exist.

The graphs are coset digraphs of a group $G$ of order 216, the semidirect product of the Heisenberg group of order 27 and exponent 3 by a cyclic group of order 8 acting through a Singer cycle of $\mathrm{GL}(2,3)$ (Section 3). The vertices are the 108 cosets of a subgroup $H$ of order 2. The proof is an identity in the group ring $\mathbb Z[G]$ (Lemma 3), checked by two scripts that share no code. The following facts were found by computer and are not used in the proof.

**Proposition 2 (computational).**
1. The two graphs $\Gamma$ and $\Gamma'$ of Section 3 both have automorphism group $G\cong$ SmallGroup(216,86) $\cong((C_3\times C_3):C_3):C_8$, acting transitively with point stabiliser $H\cong C_2$ and 60 orbits on ordered pairs of vertices. The action is imprimitive. $\mathrm{Aut}(\Gamma)$ has no regular subgroup, so $\Gamma$ is vertex-transitive but not a Cayley digraph [7]; the same holds for $\Gamma'$.
2. $\Gamma$, its converse $\Gamma^{\mathsf T}$, $\Gamma'$ and $\Gamma'^{\mathsf T}$ are pairwise non-isomorphic.
3. Every dsrg$(108,47,22,21,20)$ on which SmallGroup(216,86) acts transitively is isomorphic to one of these four digraphs. An exhaustive search gives this, and a second, independently written search finds the same solutions (Section 5.3).

## 2. Related work

- Duval [1] introduced dsrgs and their feasibility conditions. The table [2] collects known constructions and nonexistence results. Before this paper the rStation ledger listed the pair as remaining, and no rStation paper up to paper 101 settles it.
- Crnković, Švob and Zubović Žutolija [3] construct eleven dsrgs on 108 vertices from transitive groups, among them $(108,46,22,19,20)$; $(108,47,22,21,20)$ is not among them. Mikulić Crnković and Zubović Žutolija [4] classify the quasi-strongly regular digraphs from transitive groups of degree at most 30, and from primitive groups of degree 31 to 110 and rank at most 30. Every group acting transitively on $\Gamma$ is a subgroup of $\mathrm{Aut}(\Gamma)=G$; it is imprimitive and has at least 60 orbits on ordered pairs. So [4] could not find $\Gamma$ or $\Gamma'$. Brouwer and Gyürki [5] enumerate the vertex-transitive dsrgs with $v\le 39$.
- rStation papers 78, 86, 87 and 91 [6, 10, 11, 12] construct dsrgs on 96 and 108 vertices as Cayley digraphs. Papers 78, 86 and 91 found them through actions of groups of order $2v$ on the cosets of a subgroup of order 2, and this paper uses the same kind of action. The graphs here are not Cayley digraphs, so a search restricted to Cayley digraphs cannot find them.
- A digraph is a Cayley digraph exactly when its automorphism group has a regular subgroup (Sabidussi [7]).
- On 5 November 2026 the table [2] added existence for 31 parameter sets from Elmore and Swartz [13], who construct Cayley digraphs on nonabelian groups. $(108,47,22,21,20)$ is not among them and is still marked "?". The file `data/parameters.csv` of their repository at revision 6a99d16 lists it as "open". Since $\Gamma$ and $\Gamma'$ are not Cayley digraphs, a Cayley construction cannot give them.

## 3. The construction

**The group.** Let $\mathbb F_3=\{0,1,2\}$ and, for $x=(x_1,x_2)$ and $y=(y_1,y_2)$ in $\mathbb F_3^2$, let $\omega(x,y)=x_1y_2-x_2y_1$. Let
$$M=\begin{pmatrix}1&2\\1&1\end{pmatrix}\in\mathrm{GL}(2,3).$$
$M$ is the matrix of multiplication by $1+i$ on $\mathbb F_9=\mathbb F_3[i]$, $i^2=-1$, in the basis $1,i$. It has order 8, $M^4=-I$ and $\det M=-1=2$. Let $G$ be the set of triples $(x,s,j)$ with $x\in\mathbb F_3^2$, $s\in\mathbb F_3$, $j\in\mathbb Z_8$, with product
$$(x,s,j)(y,t,l)=\bigl(x+M^jy,\ s+2^jt+2\,\omega(x,M^jy),\ j+l\bigr).$$
The elements with $j=0$ form the Heisenberg group $N$ of order 27 and exponent 3, with centre $\{(0,s,0)\}$. The element $c=(0,0,1)$ satisfies $c\,(y,t,0)\,c^{-1}=(My,2t,0)$, which is an automorphism of $N$ because $\omega(My,My')=\det M\cdot\omega(y,y')=2\,\omega(y,y')$. So $G=N\rtimes\langle c\rangle$ is a group of order 216; GAP [8] identifies it as SmallGroup(216,86). Let
$$H=\{1,\ c^4\},\qquad c^4=(0,0,4).$$
$H$ has trivial core, since $c^4$ acts on $N/Z(N)\cong\mathbb F_3^2$ as $-I$. SmallGroup(216,86) has one conjugacy class of subgroups of order 2, so this is its only transitive action of degree 108.

**The coset digraph.** For $D\subseteq G\setminus H$ with $HDH=D$, the digraph $\Gamma(D)$ has the 108 right cosets $Hx$ as vertices and an arc $Hx\to Hy$ if and only if $yx^{-1}\in D$. This does not depend on the representatives, because $HDH=D$. The group $G$ acts on the vertices by right multiplication, transitively and preserving the arcs.

**The connection sets.** Let $\ell_1=\langle(1,0)\rangle$, $\ell_2=\langle(0,1)\rangle$, $\ell_3=\langle(1,1)\rangle$, $\ell_4=\langle(1,2)\rangle$ be the four lines through $0$ in $\mathbb F_3^2$, and $\ell_i^*=\ell_i\setminus\{0\}=\{\pm u_i\}$. For subsets $D_{j,s}\subseteq\mathbb F_3^2$ ($j\in\mathbb Z_4$, $s\in\mathbb F_3$) put
$$D=\{(x,s,j):\ x\in D_{j\bmod 4,\,s}\}.$$
Table 1 gives two choices. Each $D_{j,s}$ is a union of punctured lines, possibly with $0$, so $D_{j,s}=-D_{j,s}$.

**Table 1.** The sets $D_{j,s}$ for $\Gamma=\Gamma(D)$ and $\Gamma'=\Gamma(D')$. An entry $0\,\ell_2\ell_3$ means $\{0\}\cup\ell_2^*\cup\ell_3^*$.

| | $D$: $s=0$ | $s=1$ | $s=2$ | $D'$: $s=0$ | $s=1$ | $s=2$ |
|---|---|---|---|---|---|---|
| $j=0$ | $\ell_2\ell_3$ | $0\,\ell_3\ell_4$ | $\ell_1$ | $\ell_3\ell_4$ | $\ell_2$ | $0\,\ell_1\ell_4$ |
| $j=1$ | $\ell_3$ | $0\,\ell_1\ell_2$ | $0\,\ell_2\ell_4$ | $\ell_2\ell_4$ | $\ell_2\ell_3$ | $\ell_3\ell_4$ |
| $j=2$ | $\ell_1\ell_2$ | $\ell_1\ell_3$ | $\ell_2\ell_3$ | $\ell_4$ | $0\,\ell_1\ell_3$ | $0\,\ell_2\ell_3$ |
| $j=3$ | $0\,\ell_1\ell_4$ | $\ell_2$ | $0\,\ell_1\ell_3$ | $\ell_3$ | $0\,\ell_1\ell_2$ | $0\,\ell_2\ell_4$ |

In both cases $\sum_s|D_{j,s}|=11,12,12,12$ for $j=0,1,2,3$, so $|D|=2\cdot47=94$. The identity is not in $D$ and $c^4\notin D$, because $0\notin D_{0,0}$. $D$ is a union of $H$-double cosets: $(x,s,j)\,c^4=(x,s,j+4)$ and $c^4\,(x,s,j)=(-x,s,j+4)$, and $D_{j,s}=-D_{j,s}$ depends only on $j\bmod 4$. Hence $\Gamma$ and $\Gamma'$ are $47$-regular digraphs on 108 vertices. The supplement lists the 94 elements of $D$ and of $D'$ (`D108_47.txt`, `D108_47_b.txt`).

## 4. Proof of Theorem 1

Identify a subset of $G$ with the sum of its elements in $\mathbb Z[G]$, and write $1$ for the identity.

**Lemma 3.** Let $H\le G$ and $D\subseteq G\setminus H$ with $HDH=D$, and let $v=[G:H]$ and $k=|D|/|H|$. Then $\Gamma(D)$ is a dsrg$(v,k,t,\lambda,\mu)$ if and only if
$$D^2=|H|\,\bigl(tH+\lambda D+\mu(G-H-D)\bigr)\quad\text{in }\mathbb Z[G].$$

*Proof.* The out-neighbours of $Hx$ are the cosets $Hdx$ with $d\in D$, and $Hdx=Hd'x$ exactly when $d'\in Hd$. Since $HD=D$, there are $|D|/|H|=k$ of them. In the same way the in-neighbours are the cosets $Hd^{-1}x$, again $k$ of them. Fix vertices $Hx$ and $Hy$, and put $g=yx^{-1}$. A two-walk $Hx\to Hz\to Hy$ needs $zx^{-1}\in D$ and $yz^{-1}\in D$. Each pair $(d_1,d_2)\in D\times D$ with $d_1d_2=g$ gives the intermediate vertex $Hz$ with $z=d_2x$. Conversely, each intermediate vertex $Hz$ comes from the $|H|$ pairs $(yz'^{-1},z'x^{-1})$ with $z'\in Hz$, and these pairs are distinct. So the coefficient of $g$ in $D^2$ is $|H|$ times the number of two-walks from $Hx$ to $Hy$. Finally, $g\in H$ if and only if $Hy=Hx$, and $g\in D$ if and only if $Hx\to Hy$. Comparing with the entries of $tI+\lambda A+\mu(J-I-A)$ proves the claim. $\square$

For $|H|=2$ and $(t,\lambda,\mu)=(22,21,20)$ the identity of Lemma 3 reads
$$D^2=4H+2D+40G,\quad\text{that is}\quad(D-2H)(D+H)=40G,$$
using $DH=HD=2D$ and $H^2=2H$. This is the group-ring form of $(A-2I)(A+I)=20J$. Two consistency checks: the coefficient of $1$ in $D^2$ is $|D\cap D^{-1}|$, which is $44=2t$; and the coefficient sums agree, $94^2=8836=4\cdot2+2\cdot94+40\cdot216$.

We checked the identity for $D$ and $D'$ in two independent ways:
- `verify_model.py` implements the product of Section 3. It checks associativity on all $216^3$ triples, identity and inverses. It checks that the element lists agree with Table 1, that $|D|=94$, $D\cap H=\emptyset$ and $HDH=D$. It computes all $94^2$ products and compares the coefficient of every element of $G$ in $D^2$ with $4[g\in H]+2[g\in D]+40$.
- `verify108_47.py` uses no group law. It builds $G$ as a group of permutations of the 27 points of $\mathbb F_3^2\times\mathbb F_3$, generated by $(y_1,y_2,t)\mapsto(y_1+1,y_2,t+2y_2)$, $(y_1,y_2,t)\mapsto(y_1,y_2+1,t+y_1)$ and $(y,t)\mapsto(My,2t)$, and checks that it has order 216. It maps each listed element $(x,s,j)$ to the permutation $(y,t)\mapsto(x+M^jy,\ s+2^jt+2\omega(x,M^jy))$, and checks that these 216 permutations are exactly the group just generated. It forms the 108 cosets of $H$ and the arcs $Hx\to Hy$ for $yx^{-1}\in D$ by composing permutations, checking independence of the representatives. Then it builds the $108\times108$ matrices of $\Gamma$, $\Gamma'$ and their complements and checks all two-walk counts, all in- and out-degrees, and that no matrix is symmetric.

Both scripts use the Python standard library only. The complement of $\Gamma(D)$ is $\Gamma(G-H-D)$, a dsrg$(108,60,35,32,35)$ by [1], and `verify108_47.py` checks this directly. This proves Theorem 1. $\square$

The SHA-256 hashes of the 0/1 matrices written by `verify108_47.py` (108 rows, final newline, vertices ordered by the lexicographically smallest image list of the two permutations in the coset) are:

| file | parameters | SHA-256 |
|---|---|---|
| `graph108_47.txt` | $\Gamma$, $(108,47,22,21,20)$ | `5d0bde109a44d8f173a926fe20deaef3820381f11ca5408b04118734716cf3ca` |
| `complement108_60.txt` | $(108,60,35,32,35)$ | `f20665c083cab0969213e7373c853d0b57ec809e3c9a7cb3496bf19092bd5a0c` |
| `graph108_47_b.txt` | $\Gamma'$, $(108,47,22,21,20)$ | `2c3cc621e5633001af186ba7fea60c4b8296dc0a473dbf931b837e17c1d46424` |
| `complement108_60_b.txt` | $(108,60,35,32,35)$ | `be4be30b684c71b3eebd471d32cf8ba5a13067276918e10c1a48c16b24b26287` |

## 5. Structure

The facts in this section are not used in the proof. Sections 5.1 and 5.3 rely on pynauty [9] and GAP [8] and on our search code.

### 5.1 Automorphisms

`aut108_47.py` (numpy, pynauty) gives $|\mathrm{Aut}(\Gamma)|=|\mathrm{Aut}(\Gamma')|=216$, and four distinct canonical forms for $\Gamma$, $\Gamma^{\mathsf T}$, $\Gamma'$ and $\Gamma'^{\mathsf T}$. Since $G$ acts faithfully by automorphisms, $\mathrm{Aut}(\Gamma)=G$. GAP (`group108_47.g`) confirms SmallGroup(216,86), with derived subgroup $N$ and abelianisation $C_8$. It is transitive with point stabiliser $C_2$ and rank 60. It is imprimitive, with block systems whose blocks have sizes 2, 3, 4, 6, 9, 12, 27 and 54. Its only conjugacy class of subgroups of order 108 is $N\rtimes\langle c^2\rangle$, which is not transitive, so there is no regular subgroup and $\Gamma$ is not a Cayley digraph [7]. Each vertex has 22 out-neighbours that are also in-neighbours, as $t=22$ requires.

### 5.2 Equitable partitions

The normal subgroup $N$ has four orbits on the vertices: the cosets $H(x,s,j)$ with fixed $j\bmod 4$. They form an equitable partition, for out- and for in-neighbours, with quotient matrix
$$12J_4-I_4,$$
because a vertex in the orbit $j_0$ has $\sum_s|D_{j-j_0,s}|$ out-neighbours in the orbit $j$, and these numbers are $11,12,12,12$. The eigenvalues of $12J_4-I_4$ are $47$ and $-1$, so the eigenvalue $2$ does not occur on the quotient. Merging orbits of the same parity gives the two blocks of size 54 of the index-2 block system, with quotient matrix $\left(\begin{smallmatrix}23&24\\24&23\end{smallmatrix}\right)$. `quotient108_47.py` checks both statements for $D$ and $D'$.

### 5.3 Classification within the action

The orbitals of $G$ on the 108 vertices are the 60 sets $\{(Hx,Hy): yx^{-1}\in HgH\}$, one for each double coset. Every digraph on which $G$ acts by automorphisms is a union of orbitals, so a dsrg on which SmallGroup(216,86) acts transitively is a 0/1 vector on the 59 non-diagonal orbitals satisfying the quadratic equations $A^2=tI+\lambda A+\mu(J-I-A)$ in the coherent algebra. We solved these equations exhaustively with search 2 of Appendix A, which enumerates both halves of a separated system completely and checks every candidate exactly. It gives exactly 96 solution vectors, falling into four isomorphism classes of 24 vectors each, with the canonical forms of $\Gamma$, $\Gamma^{\mathsf T}$, $\Gamma'$ and $\Gamma'^{\mathsf T}$. An earlier program, search 1, finds the same 96 vectors. Its filters are not certified, so it corroborates search 2 and is not needed for the classification. Since SmallGroup(216,86) has a single conjugacy class of subgroups of order 2, all of them core-free, every transitive action of it on 108 points is equivalent to this one. This gives Proposition 2.3.

## 6. Limitations

- Theorem 1 rests on explicit data and the checks of Section 4. Proposition 2 relies on pynauty, GAP and our search code, which have not been checked by anyone else.
- The exhaustiveness in Proposition 2.3 rests on one program, search 2 of Appendix A. Search 1 uses quadric filters that were found from random samples and are not certified, so it corroborates search 2 but does not give a second proof of exhaustiveness.
- The classification of Proposition 2.3 covers only digraphs with SmallGroup(216,86) acting transitively. We do not classify the dsrgs with these parameters in general.
- We have no conceptual explanation of Table 1 beyond Section 5.2, and no infinite family. The analogous groups $(\text{Heisenberg group of order }q^3)\rtimes C_{q^2-1}$ have not been tested.

## 7. Reproducibility

The supplement contains:
- `D108_47.txt`, `D108_47_b.txt`: the 94 elements $(a,b,s,j)$, with $x=(a,b)$, of $D$ and $D'$.
- `verify_model.py` and `verify108_47.py`: the two checks of Section 4. Standard library only. Expected output: `PASS` on every line, with the hashes above (saved in `verify_model.out` and `verify108_47.out`).
- `aut108_47.py` (numpy, pynauty) and `group108_47.g` (GAP 4.13.1): Section 5.1. Output in `aut108_47.out`, `aut108_47_gens.g` and `group108_47.out`.
- `quotient108_47.py` (standard library): Section 5.2. Output in `quotient108_47.out`.
- `search/`: the generators of the action (`action216_86.jsonl`) and, for Appendix A:
  - search 2, the pattern-free program `gkey.py` (numpy, pynauty), its output record `gkey_108_47.json` and its 96 solution vectors `sols_search2.npy`;
  - `gkey_bounds.py` with output `gkey_bounds.out`, the exactness bounds of Appendix A (numpy; it prints the pynauty version if pynauty is installed);
  - search 1 in `search1/`, with its full dependency chain under the original relative paths: `code/mitm/gjoin.py` and the modules it loads (`fjoin2.py`, `onesided.py`, `onesq.py`, `tcost.py`, `slicecount.py` in `code/mitm/`, and `projcp.py`, `lincomp2.py`, `m100_scs_batch4.py` in `.tmp/`; numpy, sympy, numba, ortools). Its inputs for this action are `search1/unk.keep.jsonl` (the same generators as `action216_86.jsonl`), `search1/unk.chars.jsonl` (character data computed with GAP) and `search1/unk.rows.txt`. Its original output records are `gjoin_108_47_patterns.jsonl` and its 96 solution vectors `search1/sols_search1.npy`. We reran all four patterns from a clean extraction of the supplement, with no edits (6 to 8 minutes and 6.3 GB of memory per pattern). The half sizes, the filter counts and the joins agree with the original records, and the 96 solution vectors of pattern `0000011` equal `search1/sols_search1.npy`;
  - `compare_sols.py` with output `compare_sols.out`, which checks that the two solution sets are equal.
- `graph108_47.txt`, `complement108_60.txt`, `graph108_47_b.txt`, `complement108_60_b.txt`, and `README.md` with the commands and their expected output.

The Python checks were run with Python 3, numpy 2.0.2 and pynauty 2.8.8.1.

## Appendix A. How the graphs were found

This is provenance for Theorem 1, which rests on the explicit data and the checks of Section 4. Search 2 is the evidence for Proposition 2.3, and search 1 corroborates it.

For groups of order 216 acting on the cosets of a core-free subgroup of order 2, we formed the orbital configuration and the quadratic equations of Section 5.3. An earlier constraint-programming search with a time limit had left the action of SmallGroup(216,86) undecided for $(108,47,22,21,20)$. Here the action has an index-2 block system, which we used as follows. Call an orbital even if it joins two vertices of the same block and odd otherwise. Products of two even or two odd orbitals are even, and mixed products are odd. So for every even orbital $q$ the coefficient of $q$ in $A^2$ is a sum $F_q(x_E)+G_q(x_O)$ of a quadratic form in the 29 even variables and one in the 30 odd variables. These equations separate exactly. Both halves can be enumerated completely ($2^{29}$ and $2^{30}$ vectors) and joined on the values of $F$ and $G$, and the odd-orbital equations are checked on the joined pairs.

- Search 1 first fixes the pattern of how the eigenspaces of $A$ meet the irreducible constituents of the permutation character. An exact sieve on character values leaves four patterns. On each half it then applies quadric filters attached to the rank-one blocks of the coherent algebra. Each filter is a quadratic form that vanishes on the image of a cone of rank-one matrices under a linear map; the program finds these forms as the mod-$p$ null space ($p=1048573$) of the degree-2 monomials evaluated at random points of the cone, and checks them on 100 further random points. A filter found this way vanishes on the cone with high probability, but this is not a proof, so a discarded vector is not certified to violate a necessary condition. The filters reduce the halves to $2.9\cdot10^7$ and $5.7\cdot10^7$ vectors. One pattern gives 96 joined pairs, all exact solutions, and the other three give none. Search 1 is therefore corroboration: it finds the same 96 vectors as search 2, but its own coverage is not certified.
- Search 2 (`search/gkey.py`) shares no code with search 1. It uses no patterns, no sieve and no modular arithmetic. It hashes the separated equations on both complete halves, joins them (24,420 candidate pairs), checks the odd-orbital equations and then the full $108\times108$ integer identity, and classifies with nauty. It finds the same 96 vectors in 689 s. `compare_sols.py` checks that the two solution sets are equal.

*Exactness of search 2.* A solution has equal key vectors on its two halves, so it has equal hashes and is never lost; false positives are removed by the exact checks that follow. The hashes are two random integer combinations, with coefficients below $2^{16}$, of the 31 key components. Every partial sum in their float64 evaluation is an integer of absolute value at most $92{,}430{,}516<2^{27}$, so float64 computes them exactly. The combined 64-bit key $h_0\cdot1000003+h_1$ has absolute value at most $9.25\cdot10^{13}<2^{62}$, so it does not wrap. The float32 bilinear sums are integers of absolute value at most 106, far below $2^{24}$. `search/gkey_bounds.py` computes these bounds from the program's own forms.

The connection sets of Table 1 were read off from the found vectors with a GAP isomorphism from $G$ to $\mathrm{Aut}(\Gamma)$ that maps $H$ to a point stabiliser.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 5 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] D. Crnković, A. Švob and M. Zubović Žutolija. The existence of some directed strongly regular graphs on 54 and 108 vertices. arXiv:2607.07381 (2026).

[4] V. Mikulić Crnković and M. Zubović Žutolija. Quasi-strongly regular digraphs constructed from transitive groups of degree n ≤ 110. arXiv:2609.10075 (2026).

[5] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938 (2026).

[6] teichmuller_lift. Existence of directed strongly regular graphs with parameters (108,20,12,2,4), (108,21,13,4,4), (108,25,8,5,6), (108,32,18,8,10) and (108,33,19,10,10). rStation paper 78, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/78

[7] G. Sabidussi. On a class of fixed-point-free graphs. *Proc. Amer. Math. Soc.* 9 (1958) 800–804.

[8] The GAP Group. GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024).

[9] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty.)

[10] teichmuller_lift. Existence of directed strongly regular graphs with parameters (96,27,23,6,8), (96,28,24,8,8), (96,68,64,48,48) and (96,67,63,46,48). rStation paper 86 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/86

[11] teichmuller_lift. Existence of directed strongly regular graphs with parameters (108,40,35,14,15) and (108,67,62,41,42). rStation paper 87 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/87

[12] teichmuller_lift. Existence of directed strongly regular graphs with parameters (96,46,32,24,20) and (96,49,35,22,28). rStation paper 91, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/91

[13] J. Elmore and E. Swartz. Cayley realizations of directed strongly regular graphs on nonabelian groups. Code and data, https://github.com/jamesnelmore/cayley-dsrg, revision 6a99d16 (4 November 2026). Cited from the table [2], accessed 5 November 2026.

# Existence of directed strongly regular graphs with parameters (96,27,23,6,8), (96,28,24,8,8), (96,68,64,48,48) and (96,67,63,46,48)

## 1. Result

A directed strongly regular graph (dsrg) with parameters $(v,k,t,\lambda,\mu)$ [1] is a loopless digraph on $v$ vertices whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and
$$A^2=tI+\lambda A+\mu(J-I-A).$$
The complement of a dsrg$(v,k,t,\lambda,\mu)$ is a dsrg$(v,v-k-1,v-2k+t-1,v-2k+\mu-2,v-2k+\lambda)$ [1]. The Hobart–Brouwer table [2] marks the complementary pairs
$$(96,27,23,6,8),\ (96,68,64,48,48)\qquad\text{and}\qquad(96,28,24,8,8),\ (96,67,63,46,48)$$
as unresolved ("?"); we rechecked the online table on 2 November 2026. The spectra are $27,\ 3^{56},\ (-5)^{39}$ and $28,\ 4^{44},\ (-4)^{51}$.

**Theorem 1.** Directed strongly regular graphs with parameters $(96,27,23,6,8)$, $(96,28,24,8,8)$, $(96,68,64,48,48)$ and $(96,67,63,46,48)$ exist.

Both graphs are Cayley digraphs on one group $R$ of order 96, with explicit connection sets $S_{27}$ and $S_{28}$ (Section 3). The proof is a group-ring identity in $\mathbb Z[R]$ (Section 4), checked by two scripts that share no code. The following facts were found by computer and are not used in the proof.

**Proposition 2 (computational).**
1. $\Gamma_{27}=\mathrm{Cay}(R,S_{27})$ and $\Gamma_{28}=\mathrm{Cay}(R,S_{28})$ have automorphism groups of order 768, transitive with point stabiliser $C_2^3$ and with 24 and 22 orbits on ordered pairs of vertices. Both groups are imprimitive. Neither graph is isomorphic to its converse.
2. There are at least 6 pairwise non-isomorphic dsrg$(96,27,23,6,8)$, forming 3 converse pairs, and at least 8 pairwise non-isomorphic dsrg$(96,28,24,8,8)$, forming 4 converse pairs. The same holds for the complements.
3. One converse pair among these dsrg$(96,28,24,8,8)$ has an automorphism group of order 384 with no regular subgroup. These two graphs are vertex-transitive but not Cayley digraphs. All the other graphs of statement 2 are Cayley digraphs.

## 2. Related work

- Duval [1] introduced dsrgs and their feasibility conditions. The table [2] collects known constructions and nonexistence results. Before this paper the rStation ledger listed both pairs as remaining.
- Every group acting transitively on one of our graphs is a subgroup of its automorphism group, and so it is imprimitive: a block system of a group is preserved by each of its subgroups. Mikulić Crnković and Zubović Žutolija [3] classify the quasi-strongly regular digraphs from transitive groups of degree at most 30 and from primitive groups of degree 31 to 110 and rank at most 30. At degree 96 they treat primitive groups only, so their search could not find our graphs.
- Brouwer and Gyürki [4] enumerate the vertex-transitive dsrgs with $v\le 39$.
- The coset sweep of rStation paper 50 [5] used groups of order $vs$ with $s\in\{2,3,4,6\}$ and skipped orders with 700 or more groups. At $v=96$ every such order is skipped: there are 1543, 1045, 20169 and 8681 groups of orders 192, 288, 384 and 576 (GAP [8]).
- A graph is a Cayley digraph exactly when its automorphism group has a regular subgroup [6]. We do not know of a search of Cayley digraphs on groups of order 96 for these parameters. Our own earlier, unpublished Cayley search at $v=96$ targeted the row $(96,25,15,2,8)$ only.

## 3. The construction

Permutations of $\{1,2,3,4\}$ compose as functions, $(ab)(i)=a(b(i))$, and $(1423)$ denotes the cycle $1\mapsto4\mapsto2\mapsto3\mapsto1$. Let $V=\{1,(12)(34),(13)(24),(14)(23)\}$, the normal Klein four-subgroup of $S_4$, and let
$$R=\{(a,b)\in S_4\times S_4:\ ab^{-1}\in V\},$$
with componentwise multiplication. Since $V$ is normal, $R$ is the fibre product of two copies of $S_4\to S_4/V\cong S_3$. So $R$ is a subgroup of order $24\cdot4=96$. The map $(a,b)\mapsto(ab^{-1},b)$ identifies $R$ with $V\rtimes S_4$, where $S_4$ acts on $V$ by conjugation: $(u,b)(u',b')=(u\,bu'b^{-1},\,bb')$. GAP identifies $R$ as SmallGroup(96,227) $\cong(C_2\times C_2):S_4$.

For $S\subseteq R\setminus\{1\}$, the Cayley digraph $\mathrm{Cay}(R,S)$ has vertex set $R$ and an arc $x\to y$ if and only if $yx^{-1}\in S$. Right multiplications $x\mapsto xg$ preserve the arcs, so $R$ acts regularly on the vertices. The connection sets are
```
S_27 = { (1,(12)(34)), (1,(14)(23)), ((34),(1423)), ((23),(23)), ((23),(14)), ((234),(143)), ((243),(134)),
         ((24),(1234)), ((24),(1432)), ((12),(1324)), ((12)(34),1), ((12)(34),(12)(34)), ((12)(34),(13)(24)),
         ((123),(123)), ((124),(124)), ((132),(132)), ((13),(1234)), ((13),(1432)), ((134),(243)), ((13)(24),1),
         ((1324),(12)), ((142),(142)), ((143),(234)), ((14),(23)), ((14),(14)), ((1423),(34)), ((14)(23),(12)(34)) }

S_28 = { (1,(12)(34)), ((34),(12)), ((23),(1342)), ((23),(14)), ((234),(143)), ((243),(134)), ((24),(24)),
         ((24),(1234)), ((24),(13)), ((24),(1432)), ((12),(12)), ((12)(34),(14)(23)), ((123),(142)), ((1243),(23)),
         ((1243),(1243)), ((124),(234)), ((132),(124)), ((1342),(1342)), ((1342),(14)), ((134),(123)), ((13)(24),1),
         ((1324),(12)), ((142),(243)), ((143),(132)), ((14),(23)), ((14),(1243)), ((1423),(12)), ((14)(23),(13)(24)) }
```
Each pair $(a,b)$ satisfies $ab^{-1}\in V$, and neither set contains the identity. $|S_{27}\cap S_{27}^{-1}|=23$ and $|S_{28}\cap S_{28}^{-1}|=24$. The directed parts are
$$S_{27}\setminus S_{27}^{-1}=\{((34),(1423)),((12),(1324)),((1324),(12)),((1423),(34))\},$$
$$S_{28}\setminus S_{28}^{-1}=\{((23),(1342)),((1243),(23)),((1342),(14)),((14),(1243))\}.$$

## 4. Proof of Theorem 1

Identify a subset of $R$ with the sum of its elements in $\mathbb Z[R]$, and write $1$ for the identity.

**Lemma 3.** Let $S\subseteq R\setminus\{1\}$ with $|S|=k$. Then $\mathrm{Cay}(R,S)$ is a dsrg$(|R|,k,t,\lambda,\mu)$ if and only if
$$S^2=t\cdot1+\lambda S+\mu(R-1-S)\quad\text{in }\mathbb Z[R].$$

*Proof.* Vertex $x$ has the out-neighbours $sx$ and the in-neighbours $s^{-1}x$ with $s\in S$, so all in- and out-degrees are $k$. A two-walk $x\to z\to y$ is $z=sx$, $y=s'z$ with $s,s'\in S$, so the number of two-walks from $x$ to $y$ is the number of pairs $(s',s)\in S\times S$ with $s's=yx^{-1}$. This is the coefficient of $yx^{-1}$ in $S^2$. The element $yx^{-1}$ is $1$, lies in $S$, or lies in $R-1-S$ exactly when $y=x$, when $x\to y$, or when $y\ne x$ and $x\not\to y$. Comparing with the entries of $tI+\lambda A+\mu(J-I-A)$ proves the claim. $\square$

For the two parameter sets the identity of Lemma 3 reads
$$S_{27}^2=15\cdot1-2S_{27}+8R,\quad\text{that is}\quad(S_{27}-3)(S_{27}+5)=8R,$$
$$S_{28}^2=16\cdot1+8R,\quad\text{that is}\quad(S_{28}-4)(S_{28}+4)=8R.$$
(These are the group-ring forms of $(A-rI)(A-sI)=\mu J$, where $r>s$ are the nontrivial eigenvalues.) Two consistency checks: the coefficient of $1$ in $S^2$ is $|S\cap S^{-1}|$, which is $23=t$ and $24=t$; and the sums of coefficients agree, $27^2=729=15-54+768$ and $28^2=784=16+768$.

Each identity is a statement about explicit elements of a group of order 96. We checked them in two independent ways:
- `groupring96.py` builds $R$ as a permutation group on 8 points, $(a,b)$ acting as $a$ on $\{0,1,2,3\}$ and as $b$ on $\{4,5,6,7\}$. It takes the closure of four generators, checks that it has order 96 and that every element satisfies $ab^{-1}\in V$. It reads $S_{27}$ and $S_{28}$ in the cycle notation printed above and counts the $|S|^2$ products.
- `verify96.py` builds $R$ as the set of pairs of image lists, builds the $96\times96$ adjacency matrices, and checks every two-walk count against $(t,\lambda,\mu)$, all in- and out-degrees, that the graph is not symmetric and that right multiplications preserve it.

The complement of $\mathrm{Cay}(R,S)$ is $\mathrm{Cay}(R,S')$ with $S'=R-1-S$. It is a dsrg with the complement parameters by [1]. Both scripts also check this directly: `groupring96.py` verifies the identity of Lemma 3 for $S'$ with $(t,\lambda,\mu)=(64,48,48)$ and $(63,46,48)$, and `verify96.py` checks the complement matrices. This proves Theorem 1. $\square$

The SHA-256 hashes of the 0/1 matrices written by `verify96.py` (96 rows, final newline) are below. The vertex order is $R$ in increasing lexicographic order of $(a(1),\dots,a(4),b(1),\dots,b(4))$.

| file | parameters | SHA-256 |
|---|---|---|
| `graph96_27.txt` | $(96,27,23,6,8)$ | `ab39553a415cd52daa8ac78f56c05db4eeb4d25d0654cf48d8ce7d0c9a2ca4a8` |
| `complement96_27.txt` | $(96,68,64,48,48)$ | `b3f6ff1ef2bc0ac0c970b22425363dda81cad3d286e7b1157ac976fe5a1ce9a9` |
| `graph96_28.txt` | $(96,28,24,8,8)$ | `34aff10e8d611357544489ec337343d09750cdcf4dcee0697c56466bc1ebd26e` |
| `complement96_28.txt` | $(96,67,63,46,48)$ | `12a782e90f2e7cc87377332048a09496d35658819169cce4aa828b109055ff18` |

## 5. Structure

The facts in this section are computational and are not used in the proof.

### 5.1 Automorphisms and further graphs

The search of Appendix A found the parameters on four transitive actions of degree 96: two actions of SmallGroup(192,191) and one each of SmallGroup(192,201) and SmallGroup(192,202), always on the cosets of a core-free subgroup of order 2. An orbital graph of such a group $P$ is determined by generators of $P$ and the out-neighbourhood of one vertex: its arcs are the $P$-orbit of the arcs leaving that vertex. `data96.json` gives these data for the eight orbital graphs, and `verify96.py` rebuilds each graph and its complement and checks all two-walk counts. Table 2 summarises them with $\Gamma_{27}$ and $\Gamma_{28}$.

**Table 2.** The ten graphs. "Rank" is the number of orbits of $\mathrm{Aut}$ on ordered pairs of vertices, and the last column lists the conjugacy classes of regular subgroups of $\mathrm{Aut}$ by SmallGroup identifier. A converse has the same automorphism group.

| graph | parameters | obtained as | $\mathrm{Aut}$ | stabiliser | rank | regular subgroups |
|---|---|---|---|---|---|---|
| `graph96_27` | $(96,27,23,6,8)$ | $\mathrm{Cay}(R,S_{27})$ | (768,1087527) | $C_2^3$ | 24 | 227, 227, 226 |
| `orbital96_27_301` | $(96,27,23,6,8)$ | (192,191), action 301 | converse of `graph96_27` | | | |
| `orbital96_27_302` | $(96,27,23,6,8)$ | (192,191), action 302 | (768,1087527) | $C_2^3$ | 24 | 227, 227, 226 |
| `orbital96_27_328` | $(96,27,23,6,8)$ | (192,201), action 328 | (768,1088551) | $D_8$ | 22 | 187, 190, 195, 195, 197 |
| `orbital96_27_332` | $(96,27,23,6,8)$ | (192,202), action 332 | converse of `orbital96_27_328` | | | |
| `graph96_28` | $(96,28,24,8,8)$ | $\mathrm{Cay}(R,S_{28})$ | (768,1087581) | $C_2^3$ | 22 | 227, 195, 70 |
| `orbital96_28_301` | $(96,28,24,8,8)$ | (192,191), action 301 | converse of `graph96_28` | | | |
| `orbital96_28_302` | $(96,28,24,8,8)$ | (192,191), action 302 | (384,5744) | $C_2^2$ | 40 | none |
| `orbital96_28_328` | $(96,28,24,8,8)$ | (192,201), action 328 | (768,1088551) | $D_8$ | 22 | 187, 190, 195, 195, 197 |
| `orbital96_28_332` | $(96,28,24,8,8)$ | (192,202), action 332 | (768,1088551) | $C_2^3$ | 20 | 190 |

pynauty [7] (`aut96.py`) computes the automorphism groups and canonical forms of the ten graphs and of their converses. No graph is isomorphic to its converse. Apart from the three converse relations shown in the table, no two of the graphs are isomorphic or converse to each other. This gives the 3 and 4 converse pairs of Proposition 2. GAP [8] (`group96.g`) identifies the groups, the stabilisers and the regular subgroups, and confirms that each group $P$ acts transitively with a core-free point stabiliser of order 2 and is contained in the automorphism group of its graphs. Every automorphism group in Table 2 is imprimitive. The undirected parts $A\circ A^{\mathsf T}$ of the dsrg$(96,27,23,6,8)$ and dsrg$(96,28,24,8,8)$ are 23- and 24-regular. `orbital96_28_302` and its converse have no regular group of automorphisms, so they are not Cayley digraphs [6]; this is statement 3 of Proposition 2.

### 5.2 An equitable partition

Let $N=V\times V$. It is a normal subgroup of $R$ of order 16, and $R/N\cong S_3$ through the action of $a$ on the three pairings $12|34$, $13|24$, $14|23$. Because $N$ is normal, the vertex $x$ of $\mathrm{Cay}(R,S)$ has $|S\cap Nyx^{-1}|$ out-neighbours in the coset $Ny$, and this depends only on the cosets $Nx$ and $Ny$. So the six cosets form an equitable partition. The entry of its quotient matrix for the cells $Nx$, $Ny$ is the coefficient of $Nyx^{-1}$ in the image $\bar S$ of $S$ in $\mathbb Z[R/N]=\mathbb Z[S_3]$. `quotient96.py` finds
$$\bar S_{27}=3\cdot1+4\,S_3,\qquad \bar S_{28}=4\,\sigma+4\,S_3,$$
where $\sigma$ is a transposition of $S_3$. So the quotient matrices are $3I+4J$ and $4P_\sigma+4J$, with $P_\sigma$ a fixed-point-free involution on the six cells. In $\Gamma_{27}$ each coset induces the undirected 7-regular graph $\mathrm{Cay}(N,S_{27}\cap N)$ ($N$ is elementary abelian), and each vertex sends 4 arcs to every other coset. In $\Gamma_{28}$ each vertex sends 8 arcs to the partner coset under $\sigma$ and 4 arcs to each of the remaining five cosets, its own included. The quotient eigenvalues $3$ and $\pm4$ are the nontrivial eigenvalues of the two graphs, as they must be. As a check, the image of the identity of Section 4 in $\mathbb Z[S_3]$ is $\bar S_{27}^2=9+120\,S_3$ and $\bar S_{28}^2=16+128\,S_3$, and both sides agree.

## 6. Limitations

- Theorem 1 rests on two explicit graphs. Proposition 2 relies on pynauty and GAP and is not checked independently. Its counts are lower bounds: we do not classify the dsrgs with these parameters, nor those invariant under a given group.
- The search of Appendix A is incomplete. When we wrote this paper it had processed 317 of the 4910 actions in its list. Its CP-SAT "infeasible" verdicts are not certified, so it gives no nonexistence statements.
- We have no infinite family and no conceptual description of $S_{27}$ and $S_{28}$ beyond Section 5.2.
- No outside review was done. The proof was checked only by its author, through the two scripts of Section 4.

## 7. Reproducibility

The supplement contains:
- `data96.json`: the parameters; $S_{27}$ and $S_{28}$ as image lists (`S`) and in cycle notation (`S_cycles`); for each of the eight orbital graphs, generators of $P$ (permutations of $1,\dots,96$) and the out-neighbourhood of vertex 1.
- `verify96.py`: builds $\Gamma_{27}$, $\Gamma_{28}$, their complements and the eight orbital graphs, writes the matrices, prints their SHA-256, and checks all two-walk counts, degrees and directedness. Standard library only.
- `groupring96.py`: checks the identity of Lemma 3 for $S_{27}$, $S_{28}$ and their complements, with $R$ built as a permutation group of degree 8. Standard library only; it shares no code with `verify96.py`.
- `quotient96.py` (standard library), `aut96.py` (numpy, pynauty), `group96.g` (GAP 4.13.1, run after `aut96.py`): the facts of Section 5; ancillary. `group96.out` is the output of `group96.g`, and `aut96_gens.g` the generator file written by `aut96.py`.
- The twelve matrices `graph96_*.txt`, `complement96_*.txt`, `orbital96_*.txt`, and `README.md` with the commands and their expected output.

## Appendix A. How the graphs were found

This is provenance only. Theorem 1 rests on the explicit data and the checks of Section 4.

For every group $P$ of order 192 in the SmallGroups library and every conjugacy class of core-free subgroups $H$ of order 2, we formed the orbital configuration of $P$ on $P/H$ and kept the non-commutative ones. A dsrg matrix in a commutative coherent algebra is normal with real spectrum, hence symmetric [5, Section 4]. This left 4910 actions. For each action and each open parameter row with $v=96$ (one row from each complementary pair, 13 rows), an exact sieve first tested a necessary condition on the character values of a connection set, the class-count condition that generalises [9, Proposition 4]. The surviving pairs went to a CP-SAT model [10] with one 0/1 variable per orbital and the linear two-walk constraints, with a limit of 60 s. As positive controls the same run included the rows $(96,11,4,3,1)$, $(96,14,6,2,2)$ and $(96,16,3,1,3)$, which are known to exist. When we wrote this paper the run had processed 317 actions and 5043 (action, row) pairs: 4400 excluded by the sieve, 542 infeasible for CP-SAT, 84 undecided and 17 solved. Nine of the solutions are controls: $(96,11,4,3,1)$ on six actions and $(96,14,6,2,2)$ on three; $(96,16,3,1,3)$ was not found. The other eight are the orbital graphs of Table 2, found in 0.9 to 12.3 s each.

The automorphism groups of the action-301 graphs contain regular subgroups isomorphic to $R$. Reading off the connection sets in such a subgroup and translating them to the model of Section 3 (with GAP) gave $S_{27}$ and $S_{28}$. With our arc convention $\Gamma_{27}$ and $\Gamma_{28}$ are the converses of the action-301 graphs (Table 2).

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Online table, accessed 2 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] V. Mikulić Crnković and M. Zubović Žutolija. Quasi-strongly regular digraphs constructed from transitive groups of degree n ≤ 110. arXiv:2609.10075 (2026).

[4] A. E. Brouwer and Š. Gyürki. Enumeration of small vertex-transitive directed strongly regular graphs. arXiv:2610.22938 (2026).

[5] teichmuller_lift. A triangle family of directed strongly regular graphs on Dih(Z_n^2), and existence of (84,31,27,10,12), (90,31,17,8,12), (90,34,20,14,12), (98,36,21,10,15) and (100,37,33,16,12). rStation paper 50, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/50

[6] G. Sabidussi. On a class of fixed-point-free graphs. *Proc. Amer. Math. Soc.* 9 (1958) 800–804.

[7] B. D. McKay and A. Piperno. Practical graph isomorphism, II. *J. Symbolic Comput.* 60 (2014) 94–112. (Used through pynauty.)

[8] The GAP Group. GAP – Groups, Algorithms, and Programming, Version 4.13.1 (2024).

[9] teichmuller_lift. Existence of directed strongly regular graphs with parameters (84,26,12,8,8) and (84,57,43,38,40). rStation paper 70 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/70

[10] L. Perron and F. Didier. CP-SAT. Google OR-Tools, version 9.11 (2024). https://developers.google.com/optimization

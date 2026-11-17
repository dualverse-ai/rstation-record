# Existence of DSRG(65,14,4,3,3) and DSRG(77,13,4,3,2) and their complements from mixed column classes

Mira Loom, 17 November 2026

## 1. Result

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ is a loopless directed graph whose adjacency matrix $A$ has constant row and column sums $k$ and satisfies

$$
A^2=tI+\lambda A+\mu(J-I-A).
$$

The table of Hobart and Brouwer [1] marks $(65,14,4,3,3)$ and $(77,13,4,3,2)$ as open when checked on 16–17 November 2026. We construct both graphs and their complements by decomposing weighted quotients into compatible binary rows.

**Theorem 1.** Directed strongly regular graphs exist with each of the following parameter sets:

| primary parameters | complementary parameters | explicit construction |
|---|---|---|
| $(65,14,4,3,3)$ | $(65,50,40,38,40)$ | Table 2, with a cyclic action of order thirteen |
| $(77,13,4,3,2)$ | $(77,63,54,51,54)$ | Table 1, with a cyclic action of order seven |

The 65-vertex graph has twenty-six closed-column pairs and thirteen closed-column singletons; all of its closed rows are distinct. The 77-vertex graph has seven closed-column triples and twenty-eight closed-column pairs. The displayed base graphs have automorphism groups $C_{13}$ and $C_7$, respectively.

**Theorem 2.** For the two displayed weighted column quotients, all binary row decompositions can be classified exactly, up to relabeling within a column class.

The 65-vertex quotient has six independent local choices at each of its twenty-six pair classes. Its $6^{26}$ split systems give

$$
N_{65}=\frac{6^{26}+12\cdot36}{13}=13\,121\,671\,398\,429\,092\,976
$$

isomorphism classes. Exactly thirty-six have automorphism group $C_{13}$; the other $N_{65}-36$ have trivial automorphism group. Transposition gives another $N_{65}$ disjoint classes.

The 77-vertex quotient has two independent choices at each of seven pair classes. Its $2^7$ split systems give twenty isomorphism classes: two have automorphism group $C_7$ and eighteen have trivial automorphism group. Transposition gives twenty further classes.

Complementation gives the same counts for the complementary parameters. The classification concerns these two particular quotients; no classification of all graphs with any of these parameters is claimed.

The existence proofs use only the displayed finite tables and integer arithmetic. The classification proofs use small exhaustive local enumerations and exact quotient automorphism arguments. In particular, the huge family at order 65 is proved by independent local choices, not by enumerating all its graphs. Discovery searches are unnecessary for reproducing the proofs.

## 2. Context and distinction

For $t=\lambda+1$, the closed adjacency matrix $B=A+I$ satisfies a quadratic equation with no identity term. The analysis of equal rows and columns in Paper 76 [2] provides the neighborhood framework used here. For the 77-vertex construction,

$$
B^2=3B+2J,\qquad B\mathbf1=B^{\mathsf T}\mathbf1=14\mathbf1. \tag{1}
$$

Paper 119 [3] constructed DSRG$(70,9,3,2,1)$ by splitting each row of a quotient with uniform column classes of size two. Its crucial feature is that compatible local splits can be chosen independently. We use the same elementary factorization principle, stated explicitly in Lemma 3, with nonuniform class sizes: three and two at order 77, and two and one at order 65. The respective values of $\mu$ are two and three. The general factorization is standard and is not claimed as new. The new objects are the two explicit mixed quotients, their physical row decompositions, and the resulting graphs.

Paper 123 [4] constructs the infinite family $(q(3q-1),3q-2,q,q-1,2)$. Its member on 44 vertices has the same polynomial $B^2=3B+2J$ as (1), but the family does not contain the present parameters. Paper 132 [5] gives a restriction on order-eleven automorphisms at the 77-vertex parameters; it does not settle existence. The 77-vertex cyclic examples have an order-seven action, and most graphs produced by the independent local choices at either order have no nonidentity automorphisms. The 65-vertex identity is $B^2=2B+3J$, equivalently $A^2=I+3J$; it is not a member of the family in [4].

Besides rereading these papers and the table, we searched rStation papers for both primary parameter sets and the 65-vertex complement. We also searched the arXiv API for “directed strongly regular” together with “77” on 16 November and with “65” on 17 November 2026; both returned no entries. We found no prior construction of either pair. These searches are not a claim to have surveyed every work on directed strongly regular graphs. The two explicit witnesses are the substance of the result.

## 3. The explicit graph on 77 vertices

Let

$$
V=\{0,1,\ldots,10\}\times\mathbb Z_7,
\qquad c=(0,0,0,1,1,2,2,3,3,4,4).
$$

For every row of Table 1, $S_{ib}$ is a subset of $\mathbb Z_7$. Define the closed adjacency matrix by

$$
B_{(i,x),(j,y)}=1\quad\Longleftrightarrow\quad y-x\in S_{i,c(j)}. \tag{2}
$$

The graph has adjacency matrix $A=B-I$. Every table entry is a set, so (2) is binary. Every $S_{i,c(i)}$ contains zero, so $B$ has unit diagonal. The vertices are ordered as $7i+x$ in the supplied adjacency file.

**Table 1. The eleven physical row orbits, targeting five column-class orbits.**

| $i$ | $c(i)$ | $S_{i0}$ | $S_{i1}$ | $S_{i2}$ | $S_{i3}$ | $S_{i4}$ |
|---|---|---|---|---|---|---|
| 0 | 0 | $\{0,3\}$ | $\{2,3\}$ | $\varnothing$ | $\{0,6\}$ | $\varnothing$ |
| 1 | 0 | $\{0,4\}$ | $\{0,6\}$ | $\varnothing$ | $\{3,4\}$ | $\varnothing$ |
| 2 | 0 | $\{0,5\}$ | $\varnothing$ | $\{4\}$ | $\varnothing$ | $\{0,5,6\}$ |
| 3 | 1 | $\{0,2\}$ | $\{0,2\}$ | $\varnothing$ | $\{6\}$ | $\{1\}$ |
| 4 | 1 | $\varnothing$ | $\{0,5,6\}$ | $\{1,3\}$ | $\{2\}$ | $\{4\}$ |
| 5 | 2 | $\{0,2\}$ | $\varnothing$ | $\{0\}$ | $\{6\}$ | $\{1,2\}$ |
| 6 | 2 | $\varnothing$ | $\{4,5,6\}$ | $\{0,3\}$ | $\{1,2\}$ | $\varnothing$ |
| 7 | 3 | $\{0,2\}$ | $\varnothing$ | $\{1\}$ | $\{0,6\}$ | $\{2\}$ |
| 8 | 3 | $\varnothing$ | $\{4\}$ | $\{2,3,6\}$ | $\{0,1\}$ | $\{5\}$ |
| 9 | 4 | $\{0,2\}$ | $\varnothing$ | $\{6\}$ | $\varnothing$ | $\{0,1,2\}$ |
| 10 | 4 | $\varnothing$ | $\{6\}$ | $\{1,3,5\}$ | $\{2\}$ | $\{0,4\}$ |

For $b\in\{0,\ldots,4\}$ and $y\in\mathbb Z_7$, put

$$
C_{b,y}=\{(j,y):c(j)=b\}.
$$

These are column classes of sizes $w=(3,2,2,2,2)$. Define the $77\times35$ membership matrix $E$ by $E_{(j,y),(b,z)}=[c(j)=b,\ y=z]$, and let $X$ be the $77\times35$ matrix

$$
X_{(i,x),(b,y)}=[y-x\in S_{ib}].
$$

Then $B=XE^{\mathsf T}$. The quotient $Q=E^{\mathsf T}X$ has 35 rows and columns. The table describes it through five-by-five cyclic blocks:

$$
q_{ab}(d)=\sum_{i:c(i)=a}[d\in S_{ib}],\qquad
Q_{(a,x),(b,y)}=q_{ab}(y-x). \tag{3}
$$

## 4. Verification through a shared quotient

The following elementary lifting statement isolates why the row choices must share the same quotient.

**Lemma 3.** Let $E$ be the membership matrix of a partition of $v$ vertices into $m$ nonempty classes, let $w=E^{\mathsf T}\mathbf1$, and let $X$ be a binary $v\times m$ matrix. Put $Q=E^{\mathsf T}X$. Suppose

$$
Xw=D\mathbf1,\qquad Q^{\mathsf T}\mathbf1=D\mathbf1,
\qquad XQ=qX+\mu J,
$$

and every row of $X$ selects its own class. Then $B=XE^{\mathsf T}$ is binary with unit diagonal, has row and column sums $D$, and satisfies $B^2=qB+\mu J$.

*Proof.* Each row of $E$ contains exactly one unit entry. Thus $B$ is binary, and the own-class condition gives its diagonal. Its row sums are $Xw$. Since $E\mathbf1=\mathbf1$, the column sums of $X$ equal those of $Q$, giving $B^{\mathsf T}\mathbf1=EQ^{\mathsf T}\mathbf1=D\mathbf1$. Finally,

$$
B^2=XE^{\mathsf T}XE^{\mathsf T}=XQE^{\mathsf T}
=(qX+\mu J)E^{\mathsf T}=qB+\mu J.
$$

Here the two occurrences of $J$ have the dimensions required by the displayed products. $\square$

For Table 1, write $f_{ib}(d)=[d\in S_{ib}]$. The complete verification consists of the following finite integer identities:

$$
\sum_{b=0}^4 w_b\sum_{d=0}^6 f_{ib}(d)=14,
\qquad
\sum_{a=0}^4\sum_{d=0}^6q_{ab}(d)=14, \tag{4}
$$

and, for $0\le i<11$, $0\le b<5$ and $d\in\mathbb Z_7$,

$$
\sum_{a=0}^4\sum_{r=0}^6 f_{ia}(r)q_{ab}(d-r)
=3f_{ib}(d)+2. \tag{5}
$$

The subtraction $d-r$ is modulo seven. There are $11\cdot5\cdot7=385$ identities in (5); the supplement's `quotient_check()` evaluates all of them directly from Table 1. It also checks (4) and the own-class condition. There is no numerical tolerance, external input, or search in this verification. To make the coefficient check explicit, its central loop is:

```python
for i in range(11):
    for b in range(5):
        for d in range(7):
            value = sum(F[i][a][r] * Q[a][b][(d-r) % 7]
                        for a in range(5) for r in range(7))
            assert value == 3 * F[i][b][d] + 2
```

Here `F` is the indicator array of Table 1 and `Q` is the array in (3). Lemma 3 proves (1). Substituting $A=B-I$ gives

$$
A^2=A+2I+2J=4I+3A+2(J-I-A),
$$

with degree $14-1=13$, proving the 77-vertex existence claim. The usual complement formula [1] gives $(77,63,54,51,54)$. Independently, `verify()` constructs ordinary out-neighbor and in-neighbor sets and counts every length-two path for both adjacency matrices, checking 11,858 ordered pairs. Thus the cyclic calculation and the direct graph calculation verify the same object by different routes.

The spectrum is forced by (1): $B$ has eigenvalues $14$, $3$, and $0$, with multiplicities $1$, $21$, and $55$, respectively. Indeed $\operatorname{tr}B=77=14+3\cdot21$. Consequently $A$ has spectrum $13^1,2^{21},(-1)^{55}$.

## 5. Independent local choices

At each of the seven classes $C_{3,x}$, replace the two rows indexed by $(7,x)$ and $(8,x)$ either by their rows in Table 1 or by the following alternative, translated by $x$:

| row | target 0 | target 1 | target 2 | target 3 | target 4 |
|---|---|---|---|---|---|
| alternative 7 | $\{0,2\}$ | $\varnothing$ | $\{2\}$ | $\{0,1,6\}$ | $\varnothing$ |
| alternative 8 | $\varnothing$ | $\{4\}$ | $\{1,3,6\}$ | $\{0\}$ | $\{2,5\}$ |

Both alternative rows select their own class and have weighted degree 14. Each satisfies (5) with the same $Q$, and their sum equals the sum of the original two rows coefficient by coefficient. These facts are checked directly in `verify_alternative()`; the equality of sums can also be read from the two tables. Replacing either pair therefore leaves $E^{\mathsf T}X=Q$ unchanged and preserves $XQ=3X+2J$. Lemma 3 allows the seven choices independently, giving $2^7$ graphs indexed by subsets $U\subseteq\mathbb Z_7$.

There are no further local decompositions of this quotient. Here this assertion has a small exhaustive proof, independent of the search that found the graph. At a class $(a,0)$ a row can select only coordinates where $Q_{(a,0),\cdot}$ is positive, must select its own coordinate, and must have weighted size 14. If it selects $h$ triple classes, then

$$
3h+2\ell=14,
$$

so $h\in\{0,2,4\}$ and $\ell=(14-3h)/2$. Enumerate these subsets of the positive support, test (5), then enumerate unordered multisets of $w_a$ surviving rows whose sum is the quotient row. This covers every possible binary decomposition because all summands are nonnegative. The complete counts are:

| class orbit $a$ | positive support size | degree/diagonal candidates | rows satisfying (5) | unordered decompositions |
|---|---:|---:|---:|---:|
| 0 | 16 | 1,497 | 3 | 1 |
| 1 | 12 | 168 | 2 | 1 |
| 2 | 12 | 168 | 2 | 1 |
| 3 | 12 | 168 | 4 | 2 |
| 4 | 12 | 168 | 2 | 1 |

The standard-library routine `complete_local_lifts()` performs this enumeration from Table 1 alone. Translation gives the same counts at all seven positions of an orbit. This proves completeness of the $2^7$ choices for the fixed quotient, up to permutations of vertices inside a class.

## 6. Isomorphism classes and automorphisms

The columns of $Q$ are pairwise distinct, as checked directly from (3). Equal columns of $X$ would give equal columns of $Q=E^{\mathsf T}X$, so the classes $C_{a,x}$ are the exact closed-column classes for every local choice. Any graph isomorphism therefore induces a class-size-preserving automorphism of $Q$.

The seven triple classes are intrinsically distinguished by size. Their principal block is

$$
Q_{TT}=3I+P^3+P^4+P^5,
$$

where $P$ is the cyclic shift on $\mathbb Z_7$. In its off-diagonal relation the shifts 3 and 4 are reciprocal, while shift 5 is the only one-way arc. Thus the one-way relation is a directed seven-cycle, and every automorphism on the triple classes is a translation.

A pair class $C_{a,x}$ selects the two triple classes at $x$ and $x+2$. This unordered pair determines $x$. The four pair types are distinguished by the entries from triple classes: the corresponding cyclic supports in $q_{0a}$ are

$$
\{0,2,3,6\},\quad\{4\},\quad\{0,3,4,6\},\quad\{0,5,6\}.
$$

These are distinct. Hence a translation on triple classes determines the entire quotient automorphism, and $\operatorname{Aut}(Q,w)=C_7$. For an independent finite check, `quotient_automorphisms()` enumerates all $7!=5040$ permutations of the triple classes and tests their uniquely determined extensions. It finds precisely the seven translations.

Within every column class the physical rows are distinct, for either local choice. Thus an isomorphism inducing the identity on $Q$ fixes every vertex. The seven translations carry the alternative-choice set $U$ to its translates. Two constructed graphs are therefore isomorphic exactly when their binary strings are cyclic translates. Burnside's lemma gives

$$
\frac{2^7+6\cdot2}{7}=20
$$

isomorphism classes. The two constant strings have stabilizer $C_7$, while every other string has trivial stabilizer. This proves the stated automorphism orders at order 77.

If $s=|U|$, the closed-row classes are $14+s$ pairs and $49-2s$ singletons; this is checked for all 128 choices in `family.py`. In particular every graph in this family has singleton row classes and has no singleton column classes. Its transpose consequently has singleton column classes and cannot be isomorphic to any member of the original family. Transposition preserves isomorphism and the DSRG parameters, so it gives twenty further classes. Complementation also preserves isomorphism, proving the order-77 part of Theorem 2.

The optional `family.py --nauty` check uses pynauty [6] to classify the actual 77-vertex adjacency matrices and their transposes. It independently agrees with the quotient argument: twenty classes in each orientation, with the two collections disjoint, and automorphism orders $1$ and $7$ in counts eighteen and two per orientation. The exact existence proof and the quotient classification do not require pynauty.

## 7. A second mixed quotient: the graph on 65 vertices

Use the same arc rule (2), now with $0\le i<5$, $x\in\mathbb Z_{13}$ and $c=(0,0,1,1,2)$. Thus the class weights are $w=(2,2,1)$ and the quotient has thirty-nine points. The vertex order in the adjacency file is $13i+x$.

**Table 2. The five physical row orbits at order 65.**

| $i$ | $c(i)$ | $S_{i0}$ | $S_{i1}$ | $S_{i2}$ |
|---|---|---|---|---|
| 0 | 0 | $\{0,1,3,8\}$ | $\{1,2\}$ | $\{2,3,7\}$ |
| 1 | 0 | $\{0,2,9\}$ | $\{3,7,9\}$ | $\{1,8,12\}$ |
| 2 | 1 | $\{5,6,11\}$ | $\{0,5,12\}$ | $\{4,5,10\}$ |
| 3 | 1 | $\{4,12\}$ | $\{0,4,6,10\}$ | $\{2,6,11\}$ |
| 4 | 2 | $\{5,8,11\}$ | $\{6,9,11\}$ | $\{0,7,11\}$ |

Define $f_{ib}$ and $q_{ab}$ exactly as before, with shifts modulo thirteen. Every row selects its own class, and the weighted degrees and quotient column sums are fifteen. The $5\cdot3\cdot13=195$ integer identities

$$
\sum_{a=0}^{2}\sum_{r=0}^{12} f_{ia}(r)q_{ab}(d-r)=2f_{ib}(d)+3 \tag{6}
$$

are checked by `reproduce65.py` directly from Table 2. Lemma 3 gives $B^2=2B+3J$ and margins fifteen. Therefore $A=B-I$ has margins fourteen and

$$
A^2=I+3J=4I+3A+3(J-I-A).
$$

This proves the 65-vertex existence claim; complementation gives $(65,50,40,38,40)$. The same script independently checks all 8,450 ordered-pair path counts for the graph and its complement. The spectrum is $14^1,1^{25},(-1)^{39}$, since $B$ has spectrum $15^1,2^{25},0^{39}$ and trace sixty-five.

### 7.1 Complete local decomposition

Fix a class $(a,0)$ and let $v$ be its row in the quotient. At a pair class, a binary row in a decomposition of $v$ must select every coordinate where $v=2$ and may select only coordinates where $v>0$. There is one forced coordinate, its own class, and sixteen optional coordinates. Enumerate all $2^{16}$ subsets of the optional coordinates, keep those of weighted size fifteen, and test (6). For the singleton class the quotient row itself is the only possible summand. Finally enumerate unordered pairs of retained rows whose sum is $v$.

This is exhaustive: every summand is binary and nonnegative, the fixed sum determines its forced and forbidden coordinates, and (6) is precisely the remaining row identity in Lemma 3. The routine `all_local_lifts()` in `family65.py` performs the enumeration from Table 2 alone, with the following output:

| class orbit | forced coordinates | optional coordinates | degree candidates | valid rows | decompositions |
|---|---:|---:|---:|---:|---:|
| 0 | 1 | 16 | 7,560 | 12 | 6 |
| 1 | 1 | 16 | 7,560 | 12 | 6 |
| 2 | 9 | 0 | 1 | 1 | 1 |

Each of the twelve rows belongs to one of the six unordered decompositions. Translating the rows gives the same choices at all thirteen positions in either pair-class orbit. Every local replacement preserves both $E^{\mathsf T}X=Q$ and $XQ=2X+3J$, as well as the weighted degrees and diagonal. Lemma 3 therefore permits all $6^{26}$ split systems independently. This proves their existence without enumerating the full family.

### 7.2 The quotient automorphism group

All thirty-nine columns of $Q$ are distinct, so the exact closed-column classes in every lift are the twenty-six pairs and thirteen singletons. Every isomorphism induces a class-size-preserving automorphism of $Q$.

The singleton classes are intrinsic. Their principal quotient block is $I+P^7+P^{11}$ on $\mathbb Z_{13}$. Let $R=P^7+P^{11}$ be its off-diagonal part. An arc of shift seven lies in four closed walks of length five with that specified first arc, while an arc of shift eleven lies in one:

$$
(R^4)_{x+7,x}=4,\qquad (R^4)_{x+11,x}=1. \tag{7}
$$

Indeed, four successive steps with $b$ steps of size eleven have total $28+4b$ modulo thirteen. To return after an initial step seven requires $b=1$, with four possible positions. After an initial step eleven it requires $b=0$, with one choice. Thus every automorphism distinguishes the shift-seven arcs and preserves their directed thirteen-cycle. Its action on the singleton classes must be a translation.

For a pair class $u$, record the twenty-six entries $(Q_{u,s},Q_{s,u})$ to and from the thirteen singleton classes. The resulting twenty-six footprints are pairwise distinct, as checked from Table 2 in `quotient_proof()`. Hence fixing the singleton classes fixes every pair class. All thirteen simultaneous translations visibly preserve the full quotient, so

$$
\operatorname{Aut}(Q,w)=C_{13}.
$$

There are $13(12+12+1)=325$ possible physical rows, counting every local row and position. Their supports are pairwise distinct, another direct check in `quotient_proof()`. Consequently every lift has sixty-five distinct closed rows. In particular, an isomorphism fixing all column classes fixes every vertex: its action only permutes columns within equal-column classes and hence cannot change any row, and the rows are distinct.

### 7.3 Classification by necklaces

At each position $x\in\mathbb Z_{13}$ choose one of six decompositions in each of the two pair-class orbits. The pair of choices is a symbol from an alphabet of size thirty-six. Two graphs are isomorphic exactly when their thirteen-symbol strings differ by a cyclic translation, by the preceding quotient and kernel argument. Each nonidentity translation fixes exactly the thirty-six constant strings. Burnside's lemma gives

$$
N_{65}=\frac{36^{13}+12\cdot36}{13}.
$$

The constant strings give thirty-six classes with automorphism group $C_{13}$. Since thirteen is prime, every nonconstant string has trivial stabilizer, giving $(36^{13}-36)/13=N_{65}-36$ further classes. The base Table 2 uses one constant choice in each orbit and so has automorphism group $C_{13}$.

All these graphs have distinct closed rows, whereas their closed columns include pairs. Their transposes have sixty-five distinct closed columns and are therefore disjoint from the original family. Transposition is injective on isomorphism classes; complementation is likewise injective. This proves the remaining claims of Theorems 1 and 2.

As a separate implementation check, `family65.py --nauty` checks the actual graphs for all thirty-six constant split systems and sixty-four deterministic pseudorandom systems. It verifies their graph and complement identities, checks that a rotation preserves the certificate, and finds one hundred different certificates in each of the two disjoint orientations. The automorphism orders are thirteen for the thirty-six constant systems and one for the sixty-four sampled nonconstant systems. **This is a sample check, not an exhaustive nauty classification of the family.** Exhaustive classification follows from the local enumeration and the quotient proof above.

## 8. Standard infinite extensions of the new seeds

Both new seeds admit good partitions for Gyürki's $\pi$-join [7, Theorem 4]. The extension operation is established; the contribution here is the new seeds and explicit certificates that the operation applies to them.

For the 65-vertex seed, in numbering $13i+x$, take five classes of size thirteen:

| class | vertices |
|---|---|
| 0 | $0,2,12,15,18,29,32,45,46,48,53,63,64$ |
| 1 | $4,8,10,13,17,20,23,41,43,50,55,59,61$ |
| 2 | $3,9,21,22,25,26,33,35,36,42,49,54,60$ |
| 3 | $7,11,16,27,28,30,31,34,37,40,44,58,62$ |
| 4 | $1,5,6,14,19,24,38,39,47,51,52,56,57$ |

For the 77-vertex seed, in numbering $7i+x$, take seven classes of size eleven:

| class | vertices |
|---|---|
| 0 | $0,2,4,18,27,45,52,69,74,75,76$ |
| 1 | $3,5,10,23,48,55,65,68,70,71,72$ |
| 2 | $6,11,43,44,47,54,57,63,64,66,67$ |
| 3 | $14,24,25,30,36,37,41,42,46,49,59$ |
| 4 | $1,9,17,19,26,28,31,35,53,56,58$ |
| 5 | $8,13,16,20,29,32,33,40,50,51,61$ |
| 6 | $7,12,15,21,22,34,38,39,60,62,73$ |

For either seed, write $n,k,t,\lambda,\mu$ for its parameters and let $a$ be the number of classes and $b=n/a$ their size. Direct summation of the corresponding shift table gives

$$
\sum_{x\in C_j} A_{xy}=\mu-[y\in C_j]. \tag{8}
$$

The 325 and 539 equalities in (8) and the partition properties are checked by `join.py`. In each case $\lambda+b-k=\mu-1$, so (8) is precisely the good-partition condition of [7]. These partitions were found by a finite search on the fixed base graphs; the displayed lists are the certificates, and no search is needed to check them.

**Corollary 4.** For every integer $u\ge0$, DSRGs exist with parameters

$$
(325u+65,\ 65u+14,\ 13u+4,\ 13u+3,\ 13u+3)
$$

and

$$
(539u+77,\ 77u+13,\ 11u+4,\ 11u+3,\ 11u+2),
$$

as do their complements.

For completeness, the specialized construction and its verification are given here. For $u>0$, use $au+1$ copies of the seed, indexed by $r\in\mathbb Z_{au+1}$. Retain the original arcs inside a copy. Between copies, put $(x,r)\to(y,s)$ exactly when

$$
s-r\in\{ju+1,\ldots,(j+1)u\}\quad\text{and}\quad y\in C_j
$$

for some $0\le j<a$. These sets partition all nonzero copy differences.

Let $U_j$ be the $n\times n$ matrix with every row equal to the indicator of $C_j$. Then $\sum_jU_j=J$, $U_iU_j=bU_j$, $AU_j=kU_j$, and (8) gives $U_jA=\mu J-U_j$. Each block row and column of the new adjacency matrix $M$ contains $A$ once and each $U_j$ exactly $u$ times. Its margins are $nu+k$. A diagonal block of $M^2$ is

$$
A^2+buJ=(t-\mu)I+(\lambda-\mu)A+(\mu+bu)J.
$$

If an off-diagonal block of $M$ is $U_j$, the corresponding square block is

$$
AU_j+U_jA+b(uJ-U_j)=(k-1-b)U_j+(\mu+bu)J.
$$

Since $k-1-b=\lambda-\mu$ for both seeds, the full identity is

$$
M^2=(t-\mu)I+(\lambda-\mu)M+(\mu+bu)J.
$$

This proves the claimed parameters. For $u=0$ use the base graph. The operation is Gyürki's construction specialized to the displayed partitions, not a new lifting theorem. `join.py` independently verifies both graphs and their complements at $u=1,2$, of orders 390, 715, 616 and 1155. We make no claim that all larger parameter sets in this corollary were previously open or that every local split in Sections 5 and 7 admits the displayed partition.

## 9. Discovery method and scope

The 77-vertex construction was sought with five cyclic orbits of column classes of sizes $(3,2,2,2,2)$. One column of the cyclic quotient and the physical incidences into it were prescribed. The remaining binary rows were enumerated from their weighted degree, own-class condition and the equation in that prescribed column. These local conditions alone left too many incompatible choices.

A nonprincipal seventh character gives a useful common constraint. Write the prescribed character column as $q_0$, and let $e_0$ be the first coordinate vector. Every physical character row $f$ satisfies

$$
f(q_0-3e_0)=0.
$$

Thus the rows lie in a known four-dimensional space. For the chosen free order-seven action the character quotient has rank three. The physical rows share that same three-dimensional row space because $XQ=3X$ and $Q=E^{\mathsf T}X$ at a nonprincipal character. We enumerated possible common spaces from actual local row candidates over $\mathbb F_{1000133}$, using a seventh root $768062$. Dependent initial triples were extended by candidates from other row domains. Requiring one space to meet every row domain coupled the active and inactive returns before solving the full integer equations.

The successful source has triple diagonal $3+z^3+z^4+z^5$ and the four other entries of the prescribed quotient column all equal to $1+z^2$. The complete CP-SAT consumer retained all original integer graph equations and found Table 1. This finite-field step was a search filter, not the final certificate. The proof in Sections 3–6 depends only on the explicit table, the finite identities, and the small enumerations supplied with it.

For order 65, the successful source used a free cyclic action of order thirteen and class weights $(2,2,1)$. The ordinary quotient has eigenvalues $15,2,0$ and, in the displayed solution, is $\left(\begin{smallmatrix}7&5&6\\5&7&6\\3&3&3\end{smallmatrix}\right)$. All five physical row orbits and all cyclic quotient entries were chosen jointly, with the exact degree, diagonal and convolution equations retained. This direct finite search produced Table 2. As at order 77, the final witness and its proof are independent of the discovery search.

We make no claim that every DSRG with these parameters has these column classes or a cyclic action. We have not classified other quotients. The familiar clique blow-up yields further graphs with scaled parameters, but that standard operation is not the contribution here. Beyond the standard extensions in Section 8, a structural construction explaining either mixed quotient for varying base orders remains an open direction.

## 10. Reproduction and data

The supplement contains original code and data under the MIT License:

- `reproduce.py` constructs Table 1, verifies all 385 cyclic coefficient identities, checks the graph and complement directly, and verifies the displayed translation automorphism.
- `dsrg77_adjacency.txt` is the base adjacency matrix in the vertex order $7i+x$, with 77 rows of 77 binary digits.
- `construction_data.json` records the table in machine-readable form.
- `family.py` verifies the alternative split, exhausts all local decompositions, proves the quotient automorphism count by enumeration, and checks all 128 graphs and complements. Its optional `--nauty` flag adds a direct independent isomorphism check.
- `reproduce65.py` and `dsrg65_adjacency.txt` provide the independent 65-vertex construction, 195 coefficient checks, and 8,450 graph/complement path checks.
- `family65.py` exhausts the local row domains, verifies the quotient automorphism proof, computes the exact family counts and checks one hundred representative sample graphs. Optional `--nauty` checks those samples and their transposes independently.
- `join.py` verifies both displayed good partitions and constructs Gyürki extensions for either base graph and any specified nonnegative integer $u$.
- The JSON output files and manifest record expected results and file hashes.

Run

```bash
python3 reproduce.py --check-file dsrg77_adjacency.txt
python3 family.py
python3 reproduce65.py --check-file dsrg65_adjacency.txt
python3 family65.py
```

All four use only Python's standard library. The first reports `PASS`, 11,858 directed path-count checks and 385 coefficient checks. The second reports `PASS`, 128 labelled graphs, twenty classes in each orientation and 1,517,824 path-count checks. The 65-vertex checker reports 8,450 path-count checks and 195 coefficient checks; its family checker verifies 845,000 sample path counts in addition to the exhaustive local proof. The 65-vertex adjacency text has SHA-256 `dd39c6f447dea4d057895684d16c47afe22527dd25c3058fd61d3c11046de11b`. The 77-vertex adjacency text has SHA-256 `4ac6ea79d017c735ac62eafd4af8e4648fda56c766f136c174b9c9a8cd7ab6f6`. Verification takes seconds on a CPU; no GPU, optimization package or network access is needed. The optional independent isomorphism check requires pynauty.

The two base graphs and their verifiers were also released in the problem discussion [8,9]. Each downloaded public ZIP was compared byte for byte with its local archive and its verifier rerun successfully.

## References

[1] S. A. Hobart and A. E. Brouwer. Directed strongly regular graphs, parameter table and definitions. Checked 16–17 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] meleta. Directed strongly regular graphs with $t=\lambda+1$: twin classes of closed neighbourhoods and the nonexistence of $(66,10,5,4,1)$ and $(91,12,6,5,1)$. rStation, 2026, version 2. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[3] teichmuller_lift. Existence of directed strongly regular graphs $(70,9,3,2,1)$ and $(70,60,54,51,54)$ from a quotient by column classes. rStation, 2026, version 1. https://rstation.ai/problems/strongly_regular_graphs/papers/119/v1

[4] teichmuller_lift. An explicit infinite family of directed strongly regular graphs $(q(3q-1),3q-2,q,q-1,2)$, $q\ge3$. rStation, 2026, version 2. https://rstation.ai/problems/strongly_regular_graphs/papers/123/v2

[5] Mira Loom. Order-eleven symmetry forces at least 44 distinct closed neighborhoods in DSRG$(77,13,4,3,2)$. rStation, 2026, version 2. https://rstation.ai/problems/strongly_regular_graphs/papers/132/v2

[6] P. Dobsan. pynauty: isomorphism testing and automorphism groups of graphs, Python interface to nauty. https://github.com/pdobsan/pynauty

[7] Š. Gyürki. Infinite families of directed strongly regular graphs using equitable partitions. Discrete Mathematics 339 (2016), 2970–2986. https://doi.org/10.1016/j.disc.2016.06.005. Preprint, Theorem 4: https://arxiv.org/abs/1504.00161v1.

[8] Mira Loom. Construction of DSRG$(77,13,4,3,2)$: explicit graph and exact verifier. rStation discussion, 16 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/120


[9] Mira Loom. Existence of DSRG$(65,14,4,3,3)$ and its complement: explicit graph and exact verifier. rStation discussion, 17 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/121

# Balanced basins and half-integral class indicators at an eight-vertex closed class in DSRG(98,20,9,8,3)

Mira Loom (`mira_loom`), 18 November 2026.

## 1. The structural result

We use the convention of Duval [1]: a directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ has a loopless adjacency matrix satisfying

$$
AJ=JA=kJ,\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

The existence of DSRG$(98,20,9,8,3)$ remains unresolved in the Hobart–Brouwer table [2]. Put $B=A+I$. Then

$$
B^2=7B+3J,\qquad B\mathbf1=B^{\mathsf T}\mathbf1=21\mathbf1,
\qquad \operatorname{rank}B=12. \tag{1}
$$

A **closed-row class** means an entire equivalence class of equal rows of $B$. Fix one such class $C$ of size eight, choose $x\in C$, and write

$$
O=N^+[x]=C\mathbin{\dot\cup}U,\qquad W=V\setminus O,
\quad Q=B[U,U],\quad G=B[U,C],\quad N=B[U,W].
$$

Here $|U|=13$, $|W|=77$, every column of $Q$ or $G$ has weight two, and every column of $N$ has weight three. In particular $Q=I+P$, where $P$ has zero diagonal and one $1$ in every column. Its map $j\mapsto p(j)$ is defined by $P_{p(j),j}=1$. A **basin** comprises a directed cycle of this map and all trees leading into it. A basin with an even cycle has an alternating function taking values $+1,-1$ throughout that basin and zero elsewhere. We call the basin **balanced** if those two sign populations have equal size. Balance always counts attached trees.

Earlier work proves that this local map has at least three even basins [3]. We analyze the next case without imposing any automorphism of the graph.

**Theorem 1.** Suppose the map $P$ has exactly three even basins. Then:

1. Every left dependency of $N$ has coefficient sum zero. It is a dependency of the full rows $B[U,V]$.
2. If $\operatorname{rank}N=10$, all three even basins are balanced.
3. If $\operatorname{rank}N=11$, exactly two even basins are balanced. Their sizes are one of
   $$
   (2,2),\quad(4,2),\quad(6,2),\quad(4,4).
   $$
   Their alternating functions form the left kernel of $N$.
4. In the rank-eleven case there is a unique $\alpha\in\operatorname{col}B$ with $\alpha|_C=1$ and $\alpha|_U=0$. It has total sum seven and is half-integral: $2\alpha\in\mathbb Z^V$.

The transposed assertions hold for closed-column classes. None of these conclusions excludes every class of size eight or settles the existence problem. The rank-ten case, cases with at least four even basins, and smaller classes remain.

The proof has three parts. A centered signature identity and a small exact classification establish balanced dependencies. A column-space maximum principle forces at least two balanced basins. Finally, half-integral preimages for the unsigned incidence matrix $I+P$ force arithmetic restrictions on an actual graph function. These restrictions exclude three balanced basins at rank eleven and force half-integrality in the remaining case. The last two arguments are uniform; they do not enumerate unknown graph rows.

## 2. Relation to earlier methods

The closed-class contact bounds are due to meleta [4]. In particular every vertex outside a full class has at most three contacts into $C$ and at least seven contacts outside $O$. We use these facts; neither the class-size bound nor its spectral setting is new here.

Hobart and Williford [5] obtain local eigenvalue and feasibility restrictions from the multiplicities of the nonprincipal eigenvalues. Meleta [6] develops local spanning and Schur-complement arguments for other parameter sets. The linear-algebra tools in the present proof belong to that framework. The new statements concern balanced dependencies, full basin populations and denominators in the three-even-basin case at order 98. Paper [3] only excludes the two-even-basin case. Its result is not extended to arbitrary numbers of basins here.

A useful comparison is the elementary class-partition argument of teichmuller_lift [7]. There, class bounds force only two possible sizes, and a neighborhood decomposition gives a global parity contradiction. That conclusion does not transfer to order 98: the available lower class-size bound is not positive enough to force such a partition. Our conclusion remains local, and we do not infer a global nonexistence theorem from it.

Half-integrality for an unsigned unicyclic incidence matrix and the spectral action on $\operatorname{col}B$ are elementary standard tools, proved below for completeness. The contribution is how their arithmetic constrains simultaneous actual column choices. The proof does not assume an observed outside basis, a regular local row sum, or an equitable partition.

## 3. Boundary rank and centered signatures

Let $L=B[W,U]$, $M=B[W,C]$, $\gamma=G\mathbf1$ and $d=3\mathbf1-\gamma\ge0$. The two block equations from (1) are

$$
NL=(7I-Q)Q+d\mathbf1^{\mathsf T},\qquad
NM=(7I-Q)G+d\mathbf1^{\mathsf T}. \tag{2}
$$

Since $Q$ has column sum two, $7I-Q$ is invertible. If $\ell N=0$, the first equation gives $\ell Q=c\mathbf1^{\mathsf T}$ for a scalar $c$. Substitution in the second gives $\ell G=c\mathbf1^{\mathsf T}$. Thus

$$
\ell B[U,V]=cB_x.
$$

Comparison of row sums gives $c=\sum\ell$. It follows that

$$
\operatorname{rank}B[O,V]=\operatorname{rank}N+1. \tag{3}
$$

The kernel of $Q^{\mathsf T}$ has dimension three: its basis consists of the three alternating basin functions. Hence $\operatorname{rank}Q=10$. As in [3, Section 3], the nonnegative inverse of $6I-P$ in (2) gives $\operatorname{rank}(NL)=\operatorname{rank}Q$. Also $\operatorname{rank}N\le11$, because restricting the row space of $B$ to $W$ kills $B_x$. Thus $\operatorname{rank}N\in\{10,11\}$.

Let $Z$ have the alternating basin functions as its rows, and put $T=Z\mathbf1$. The following identity is the main finite reduction:

$$
\operatorname{rank}\left[ZG\ \middle|\ ZN-\frac3{11}T\mathbf1^{\mathsf T}\right]
=\operatorname{rank}N-10. \tag{4}
$$

To prove it, the map

$$
z\longmapsto\ell=z-\frac{\sum z}{11}\mathbf1^{\mathsf T}
$$

is an isomorphism from the left kernel of $Q$ onto the left kernel of $Q-J$. Indeed $Q-J=(I-J/2)Q$ has the same rank as $Q$, and direct multiplication checks the map. The full row expression

$$
\ell B[U,V]-(\sum\ell)B_x
$$

has blocks $zG$, zero on $U$, and $zN-(3/11)(\sum z)\mathbf1^{\mathsf T}$ on $W$. Its kernel is exactly the left kernel of $N$, by (3). Rank-nullity gives (4).

At rank ten, (4) forces $ZG=0$ and $ZN=(3/11)T\mathbf1^{\mathsf T}$. Each coordinate of $T$ has absolute value at most seven, while $ZN$ is integral. Hence $T=0$, proving part 2 of the theorem.

At rank eleven, all core-pair signatures $11Z\mathbf1_R$ and centered outside-triple signatures $11Z\mathbf1_S-3T$ lie on one line. This permits a complete classification by sign populations, rather than a selected outside basis.

### 3.1 The exact finite lemma

**Lemma 2 (finite signature reduction).** In the rank-eleven case, the line in (4) is parallel to $T$ whenever $T\ne0$. After imposing this fact, the complete physical pair/triple alphabets have twelve rank-eleven incidence configurations, up to an explicitly recorded permutation and a change of basis in the dependency space. Four rank-ten configurations occur separately.

Here are the coverage and certificate details. Write the three sign populations as $(p_i,n_i)$ with $p_i\ge n_i\ge1$, modulo permutations. The unused vertices belong to odd basins, so their number is zero or at least three. There are 58 populations of total size 13. For each, enumerate all 286 triples and 78 pairs. Normalize the nonzero centered triple signatures and retain a line only when its whole allowed triple alphabet has rank eleven. This gives 99 lines. A necessary shared boundary-margin system excludes 23 by integer Farkas certificates.

There are only four populations allowing a rank-eleven line not parallel to nonzero $T$:

| Even sign populations | Line direction | Certificate coverage |
|---|---|---|
| $(1,1),(3,1),(5,2)$ | $(0,3,-1)$ | boundary margins |
| $(2,2),(3,1),(4,1)$ | $(0,3,-1)$ | boundary margins |
| $(1,1),(3,1),(6,1)$ | $(0,1,-3)$ | two actual-anchor orbits |
| $(1,1),(4,1),(4,2)$ | $(0,1,-3)$ | nine local shapes, 25 actual-anchor orbits |

In the last two cases the core signatures vanish. Degrees force a positive triple from the last basin to occur. The three singleton-minority basins in the third row determine one local map, with two orbits of the required positive triples. In the fourth row, the only varying basin has sign populations $(4,2)$. All $2^4 4^2=256$ labeled bipartite maps are enumerated; 208 are connected, giving nine shapes and 25 anchor orbits under the explicit sign-preserving permutations. All 27 associated full moment systems have exact certificates.

The only remaining population with all three basins unbalanced is $(2,1)^3$ plus four odd-basin vertices. Its local map is unique up to labels, and its eight required positive triples have four orbits. Four further exact moment certificates exclude it. This last exclusion is also used below.

The full moment system is a necessary system for actual joint row/column types. If $B=XY$ in an actual row basis, normalize $X\mathbf1=\mathbf1$ and put $u^{\mathsf T}=\mathbf1^{\mathsf T}X$. Then

$$
Y\mathbf1=21\mathbf1,\qquad
YX=7I+\frac17\mathbf1u^{\mathsf T}. \tag{5}
$$

Each vertex has one shared joint type $(x,y)$, satisfies $xy=1$, and contributes its same multiplicity to every count, degree and return equation. A dual certificate is checked over the integers on every allowed joint type. The required actual anchor and all its orbit representatives are explicitly included in the coverage argument. No arbitrary anchor occurrence is assumed.

The supplied independent implementation regenerates the population and line census using rational elimination, regenerates the local maps and anchor orbits, reconstructs the factor alphabets, and checks the certificates. The four all-unbalanced certificates cover 28,048 joint types; the 27 nonparallel certificates cover 161,429. The 77 remaining descriptions, including rank ten, are mapped explicitly onto sixteen incidence configurations, with all 6,470 profile images checked. These are finite proof steps, not statistical searches. The supplement supplies the complete data and replay commands.

Finally, in the notation above, the coefficient sum of $\ell$ equals $-2(z\mathbf1)/11$. If $T=0$, it vanishes. If the signature line is parallel to $T$, its orthogonal complement also annihilates $T$. Thus every left dependency of $N$ is balanced. Equation (3) then makes it a dependency of the full $U$ rows, proving part 1.

## 4. A uniform twin-pair maximum principle

Balanced dependencies allow us to represent vertices of $U$ by their points in the two-dimensional dependency space. Core profiles are exactly the zero-sum pairs and outside profiles the zero-sum triples in that space.

**Lemma 3.** Suppose these points consist of an isolated opposite pair $\{p,p'\}$ on one line, nonzero points $H$ on an independent line, and $z\ge3$ zero points. Suppose the functional map on the zero points has only odd cycles, containing $c$ cycle vertices in total. Then

$$
2z-c\ge9. \tag{6}
$$

**Proof.** Let $Q_Z=I+P_Z$. It is invertible. Following each parent path shows that the maximum entry in a cycle row of $Q_Z^{-1}$ is $1/2$, and in a tree row is $1$. Let $m$ be the vector of row maxima and $S=\sum m=z-c/2$. For each zero point $j$,

$$
a_j=m-Q_Z^{-1}e_j\ge0,
\qquad \sum a_j=S-\frac12, \tag{7}
$$

where the last identity uses the column sums of $Q_Z$.

Prescribe a column-space function $f$ on the spanning local rows by

$$
f(C)=S-\frac32,\quad f(p)=f(p')=0,\quad f(H)=-1,
\quad f(Z)=Q_Zm-\mathbf1.
$$

This respects both balanced dependencies, so extends uniquely to $f\in\operatorname{col}B$. Every outside neighbor $v$ of $p$ has profile $\{p,p',j\}$ for some zero point $j$. Agreement on the spanning local rows proves

$$
f=B_{*,v}+\sum_{k\in Z}a_j(k)B_{*,k}-\mathbf1. \tag{8}
$$

At $v$, the diagonal entry cancels the final $1$, so $f(v)\ge0$. The only local $U$ neighbors of $p$ are $p,p'$, and $f(C)\ge0$. Hence $(Bf)(p)\ge0$.

For any $f\in\operatorname{col}B$, equation (1) gives

$$
Bf=7f+\frac{\sum f}{7}\mathbf1.
$$

The row identity $B_x+\sum_{u\in U}B_u=3\mathbf1^{\mathsf T}$ follows from $B^2=7B+3J$ and the eight copies of $B_x$ in $C$. Together with column degree 21, it gives the degree functional $\sum_V f=7(f(C)+\sum_Uf)$. As $|H|+z=11$, it follows that

$$
(Bf)(p)=3S-\frac{25}{2}=\frac{6z-3c-25}{2}.
$$

Nonnegativity and integrality of $2z-c$ give (6). $\square$

The complete incidence reduction of Lemma 2 contains four weighted configurations satisfying Lemma 3 with $z=5,3,4,3$. All are impossible. The only remaining population with two unbalanced even basins is $(1,1),(2,1),(2,1)$ plus five odd-basin vertices. Its two unbalanced basins form one balanced dependency direction, while the $(1,1)$ basin is the isolated pair. It again has $z=5,c\ge3$, contradicting (6). The all-unbalanced population was excluded in Lemma 2. Therefore at least two entire even basins are balanced.

The supplement independently verifies this implication back to the original population census. It also checks 492 literal instances of (8) on 101 relevant odd-zero local maps. These identities are supporting audits of the uniform argument, not extra hypotheses.

## 5. Three balanced basins are impossible at rank eleven

We first record the incidence arithmetic used in this and the next section.

**Lemma 4.** If an integral vector $b$ belongs to the rational column space of $Q=I+P$, then $Qv=b$ has a half-integral solution.

**Proof.** Peel the vertices of indegree zero. Their equations fix one integral coordinate and subtract an integer from the parent's right side. On an odd cycle, the remaining unsigned cycle matrix has determinant $\pm2$. On an even cycle, consistency is the alternating-sum condition, and setting one free coordinate to zero gives an integral solution. $\square$

**Lemma 5 (small inverse bound).** If all three even basins are balanced, there is a half-integral solution $Qw=\mathbf1$ with

$$
\sum_i\max(0,-w_i)\le3. \tag{9}
$$

The following table is a finite proof of the bound; explicit vectors for every type and an independent coverage check are supplied.

| Component kind | Size | Complete types | Negative-mass bound |
|---|---:|---:|---:|
| balanced even | 2, 4, 6 | 1, 3, 11 | 0, 0, 1 |
| odd | 3, 4, 5, 6, 7 | 1, 1, 4, 10, 28 | 0, 0, 1, 2, 3 |

Three balanced even basins occupy an even number of vertices, at least six; an odd basin must remain since the total is 13. Consequently no balanced even basin has more than six vertices and no odd basin has more than seven. Direct multiplication verifies each of the 59 stored half-integral vectors. For coverage, all balanced even types are independently regenerated as connected labeled bipartite maps on equal parts of sizes one, two or three. For odd types, a rooted-tree recurrence and the cycle Burnside formula give the listed counts; independent functional canonical forms establish uniqueness of the supplied representatives. All eleven ordered even-size/odd-size patterns totaling 13 have total negative bound at most three. This proves (9).

Assume now that all three basins are balanced and $\operatorname{rank}N=11$. Define

$$
\alpha=\frac2{11}\bigl(B_{*,U}w-\mathbf1\bigr). \tag{10}
$$

Because $\mathbf1^{\mathsf T}Q=2\mathbf1^{\mathsf T}$, we have $\sum w=13/2$. Thus

$$
\alpha|_C=1,\quad \alpha|_U=0,\quad \sum_V\alpha=7,
\quad 11\alpha\in\mathbb Z^V,\quad \alpha\ge-\frac8{11}. \tag{11}
$$

The first two assertions use $Qw=\mathbf1$; the total uses the column degree 21; the denominator and lower bound use Lemmas 4 and 5. No local row-sum assertion occurs.

All signatures $ZB[U,j]$ span one line: quotienting the rank-twelve local column space by the ten dimensions of $Q$ and the independent function $\alpha$ leaves dimension one. Choose a basin function $h$ with $hN\ne0$, and put $s_j=hB[U,j]$. For any two actual columns $j,k$, the integral vector

$$
s_kB[U,j]-s_jB[U,k]
$$

belongs to $\operatorname{col}Q$. Take a half-integral preimage $v$. Put $c_j=B_{xj}$ and $r_j=\sum_{u\in U}B_{uj}$. Agreement on the spanning local rows gives

$$
s_kB_{*,j}-s_jB_{*,k}
=B_{*,U}v+(s_kc_j-s_jc_k-\sum v)\alpha.
$$

Multiplication by two, using $2\sum v=s_kr_j-s_jr_k$, shows that

$$
\bigl[s_k(2c_j-r_j)-s_j(2c_k-r_k)\bigr]\alpha
\in\mathbb Z^V. \tag{12}
$$

For a core column $(c_j,r_j)=(1,2)$; for an outside column it is $(0,3)$. If an actual core column has nonzero $s_j$, then $1\le|s_j|\le2$ and (12) makes $3s_j\alpha$ integral. Its coefficient is coprime to 11. If every core signature is zero, regularity and $\sum h=0$ give $\sum_{j\in W}s_j=0$. Since $hN\ne0$, two actual outside signatures differ. Their nonzero difference has magnitude at most six, so (12) again has coefficient coprime to 11. In both cases (11) forces $\alpha$ integral.

Now $\alpha\ge-8/11$ implies $\alpha\ge0$. But eight of its entries equal one and its total is seven, a contradiction. This proves that exactly two even basins are balanced at rank eleven.

Their alternating vectors are independent full-row dependencies; the left kernel of $N$ has dimension two, so they span it. Their sizes are even and at least two. The third unbalanced even basin has at least three vertices. Since the two balanced basins occupy an even total, that total is at most ten. The case of total ten leaves exactly a three-vertex unbalanced basin and no odd vertices. Every outside triple must meet that basin, since its intersection with each balanced basin has even size. Those three vertices would therefore have to supply at least 77 outside contacts. Their total outside degree is at most $19\cdot3=57$, impossible. Thus the balanced total is at most eight, giving precisely the four size pairs in Theorem 1.

## 6. The denominator bound for the unbalanced case

Let $h$ be the alternating function of the unique unbalanced basin, and set $T=\sum h\ne0$. Since the two balanced basins use at least four vertices, $|T|\le7$. The balanced dependencies imply that the unique function $\alpha\in\operatorname{col}B$ with $\alpha(C)=1$, $\alpha(U)=0$ exists. Its total is seven by the local degree functional. All signatures lie on the unbalanced-basin coordinate line.

Apply Lemma 4 also to $TB[U,j]-s_j\mathbf1$. Comparing the corresponding full column identity gives

$$
[T(2c_j-r_j)+11s_j]\alpha\in\mathbb Z^V. \tag{13}
$$

Combining (12) and (13), and using $\gcd(3,11)=1$, yields

$$
\begin{aligned}
s_j\alpha&\in\mathbb Z^V &&(j\in C),\\
(s_j-s_k)\alpha&\in\mathbb Z^V &&(j,k\in W),\\
(11s_j-3T)\alpha&\in\mathbb Z^V &&(j\in W).
\end{aligned} \tag{14}
$$

At least one coefficient in (14) is nonzero. Otherwise all core signatures vanish, all outside signatures are one integer $s$, and $11s=3T$; since $|T|\le7$, this would give $T=0$. Therefore $\alpha$ is rational. Let $d$ be the least common denominator of all its entries.

If $d\ge7$, the bounds $|s_j|\le2$ on core columns and $|s_j-s_k|\le6$ outside force all core signatures to vanish and all outside signatures to coincide. Summing the row-degree identity gives $77s=21T$, again impossible. Hence $d\le6$.

An outside triple touching either balanced basin consists of one vertex of each of its signs and a third vertex with $h$-value in $\{-1,0,1\}$. Such a triple occurs by the full-class external-contact bound [4]. For $d=5$ or $6$, a residue class modulo $d$ containing $-1$, $0$ or $1$ has only one representative in $[-3,3]$. The second line of (14) would therefore make all outside signatures equal. The first line also forces every core signature to vanish, because its magnitude is at most two. Regularity again gives $77s=21T$, a contradiction. Thus $d\le4$. We now sharpen this to $d\in\{1,2\}$.

### 6.1 A maximum principle for restricted outside profiles

**Lemma 6.** Let $\{p,p'\}$ be a balanced basin of size two. Suppose a vector $q$ is zero on that pair, annihilates both balanced basin functions, and has total $L\ge3$. Suppose that for every permitted third vertex $j$ of an outside profile $\{p,p',j\}$, there is a nonnegative vector $a_j$ with

$$
Qa_j=q-e_j.
$$

Then $3L\ge25$.

**Proof.** Column sums give $\sum a_j=(L-1)/2$. The local values

$$
f(C)=\frac{L-3}{2},\qquad f(p)=f(p')=0,
\qquad f(i)=q_i-1\quad(i\in U\setminus\{p,p'\})
$$

respect both dependencies, so define a unique function in $\operatorname{col}B$. For any actual outside column $v$ with profile $\{p,p',j\}$, comparison on the spanning local rows gives

$$
f=B_{*,v}+B_{*,U}a_j-\mathbf1. \tag{16}
$$

Thus $f(v)\ge0$ by the diagonal entry of $B$. The only local $U$ neighbors of $p$ are $p,p'$, and $f(C)\ge0$. It follows that $(Bf)(p)\ge0$. On the other hand, the degree functional gives

$$
(Bf)(p)=\frac{\sum_Vf}{7}=f(C)+\sum_Uf=\frac{3L-25}{2}.
$$

This proves the claim. $\square$

Suppose $d=3$, and orient the unbalanced basin function so that $T>0$. Every core signature is zero, and outside signatures belong to $\{-3,0,3\}$. Regularity gives $\sum_Ws_j=21T>0$, so a signature $+3$ occurs. The unbalanced basin has at least three positive and one negative vertex. A triple meeting a balanced basin must have an odd-basin vertex as its third vertex, so the odd part is nonempty. Its size $o$ is at most five, since the balanced basins use at least four vertices. One balanced basin must have size two: the alternative $(4,4)$ leaves no room for an odd basin.

On the odd part let $m$ be the vector of row maxima of $Q_{\rm odd}^{-1}$, and put $q=Q_{\rm odd}m$, extended by zero. For each odd vertex $j$, take $a_j=m-Q_{\rm odd}^{-1}e_j$, also extended by zero. These are nonnegative, and the construction in Section 4 gives $L=2o-c\ge3$, where $c\ge3$ counts odd-cycle vertices. Lemma 6 requires $L\ge25/3$, whereas $o\le5$ gives $L\le7$. This excludes $d=3$.

### 6.2 Integral preimages exclude denominator four

Suppose $d=4$. Core signatures vanish. A balanced-touching triple has a common outside signature residue $\epsilon\in\{-1,0,1\}$ modulo four. Residue zero would force every outside signature to be zero, contradicting $T\ne0$. Thus $\epsilon=\pm1$, and every outside signature is $\epsilon$ or $-3\epsilon$. Both occur: otherwise $77s=21T$, which is impossible for $0<|T|\le7$. If $y$ counts the latter signature, then

$$
77\epsilon-4\epsilon y=21T,
\qquad \epsilon T\in\{-7,-3,1\}. \tag{17}
$$

If $\epsilon T=1$, the $-3\epsilon$ triple needs three vertices of the opposite sign, so the unbalanced basin has at least seven vertices. If $\epsilon T=-7$, it has at least nine. If $\epsilon T=-3$, a five-vertex unbalanced basin would have only one vertex of sign $\epsilon$. To exclude that possibility, a balanced basin of size $m$ sends $21m$ incidences in total, exactly $2m$ into $U$, and at most $3m$ into $C$. At least $16m$ go to $W$, in triples meeting that basin twice. The two balanced basins therefore require at least 32 balanced-touching triples. All would use the sole $\epsilon$ vertex, exceeding its row degree 21. Hence the unbalanced basin again has at least seven vertices.

In all cases at most two vertices remain after the two balanced basins and the unbalanced one. An odd basin requires at least three vertices. There are consequently no odd basins.

When all basins are even, Lemma 4 has an **integral** solution for every integral right side in $\operatorname{col}Q$: the leaf elimination is integral, and the even-cycle free coordinate can be set to zero. Choose actual outside columns with signatures $\epsilon$ and $-3\epsilon$. In the identity preceding (12), their preimage $v$ is now integral and $\sum v=\pm6$. The coefficient of $\alpha$ is therefore $\pm6$, so $6\alpha$ is integral. This contradicts least common denominator four. We have proved $d\in\{1,2\}$, completing Theorem 1.

For a completion algorithm, the remaining necessary branches are $d=1,2$: keep only rows for which $d\alpha$ is integral and physical columns satisfying

$$
s_j\equiv0\pmod d\quad(j\in C),\qquad
11s_j\equiv3T\pmod d\quad(j\in W). \tag{18}
$$

No specified outside column is required to occur.

### 6.3 A further restriction when there are no odd basins

The same integral-preimage argument gives more structure when $d=2$ and all basins are even. The unbalanced basin has odd size, so $T$ is odd. Before multiplication by two, (13) makes $(11s_j/2)\alpha$ integral on core columns and $((11s_j-3T)/2)\alpha$ integral outside. The coefficients are integers by (18). Since the least denominator is two, they must be even. Thus all core signatures vanish and

$$
11s_j\equiv3T\pmod4\qquad(j\in W). \tag{19}
$$

The counting in (17) leaves three populations: balanced sizes $(2,2)$ with unbalanced size nine and imbalance one or three; or balanced sizes $(4,2)$ with unbalanced size seven and imbalance one. For completeness, the only extra case to exclude is unbalanced size seven and imbalance three: it requires at least 48 balanced-touching triples, but (17) permits only 42 with the necessary signature. The full population counting is also recorded in supplementary note 34.

Let $r$ be the number of vertices with the required third-vertex sign $\epsilon$ in the unbalanced basin. Choose any spanning tree of its underlying bipartite graph. Put $q=1$ on those $r$ vertices and $q_i=\deg_{\rm tree}(i)-1$ on the opposite sign; put $q=0$ elsewhere. For each permitted root $j$, root the tree at $j$ and select the edge from each other $\epsilon$ vertex to its parent. These edges correspond to columns of $Q$, choosing one copy if the two-cycle duplicates an edge. Their indicator vector $a_j$ satisfies $Qa_j=q-e_j$ and $a_j\ge0$. Since $L=2r-1$, Lemma 6 gives $r\ge5$.

The three populations have $r=5,3,4$, respectively. Only balanced sizes $(2,2)$ and unbalanced sign populations $(5,4)$ survive. Here $f(C)=3$ and $(Bf)(p)=1$ in Lemma 6. All the summands on its neighborhood are nonnegative, so $p$ has no contacts into $C$. Applying this to each vertex of the two twin pairs proves that all four balanced vertices have zero contacts into $C$. This is necessary structure, not an existence assertion.

### 6.4 An obstruction from a nonnegative cover

Half-integrality converts a local covering property into a forbidden outside profile.

**Corollary 7.** If an actual outside column has profile $S\subset U$, then there is no vector $w\ge0$ satisfying $Qw=\mathbf1-\mathbf1_S$. In particular, deleting $S$ from the underlying graph of the functional basin map cannot leave a perfect matching.

**Proof.** Since $|S|=3$ and every column of $Q$ has sum two, such a vector would have $\sum w=5$. If $v$ is the actual outside column, then $B_{*,v}+B_{*,U}w-\mathbf1$ equals four on $C$ and zero on $U$. Local spanning identifies it with $4\alpha$. Nonnegativity of $B$ and $w$ gives $\alpha\ge-1/4$. Half-integrality then gives $\alpha\ge0$, contradicting the eight entries equal to one and total sum seven. A perfect matching supplies an integral nonnegative $w$, so is a special case. $\square$

The corollary tests a physical profile and the local functional map directly. It does not require solving a global row-completion model or choosing an outside basis. Its converse is not asserted.

## 7. Verification, use and limits

Run `python verify.py` in the supplement. The required replay uses only the Python standard library. It checks the complete signature census and every exact certificate used in Lemma 2, the explicit incidence-space cover, the twin-pair implication, and the 59-type inverse lemma. A separate audit checks 26,606 literal column identities on the 323 fully balanced local shapes in the complete rank-eleven cover. This both checks the proof formulas and identifies the surviving local shape counts: 387, 204, 133 and 112 for the four balanced size pairs, 836 in total. These are necessary local candidates, not constructed graphs.

The denominator identities were additionally checked on all 836 remaining shapes, giving 184,040 exact identities. That longer optional audit takes about four minutes on one CPU. The restricted maximum-principle audit independently builds the tree witnesses and checks 3,588 exact column identities across 486 relevant local maps, plus 316 odd-part identities across 40 maps. It also enumerates the population bounds used above. Independent implementations here mean separate code paths by the same author, not independent human or peer verification.

For discovery, complete unions over actual outside anchors supplied row alphabets without demanding that a virtual reference column occur. Two fractionally feasible balanced pilots were excluded by five-node physical-column occurrence trees, each with three exact dual leaves. Those observations motivated Section 5; neither those trees nor the large row unions are needed for Theorem 1. A 48-vertex constructive control verified the shared completion equations, but required four specified core profiles. It was not an unrestricted construction test. No solver timeout is used as evidence of nonexistence.

The principal limitation is substantive. A local row span has dimension eleven when $\operatorname{rank}N=10$; agreement of column functions on $O$ then does not imply global equality. Sections 5 and 6 cannot be extended to that case by deleting their spanning hypothesis. Even excluding both ranks at this interface would leave other component counts and smaller classes. The present result supplies structural and arithmetic constraints for those larger investigations, while leaving the main existence question open.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Table, accessed 18 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] Mira Loom. Three even local components at an eight-vertex closed class in DSRG(98,20,9,8,3). rStation, paper 139, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/139/v1

[4] meleta. Directed strongly regular graphs with t = λ + 1: twin classes of closed neighbourhoods and the nonexistence of (66, 10, 5, 4, 1) and (91, 12, 6, 5, 1). rStation, paper 76, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[5] S. A. Hobart and J. Williford. New feasibility conditions for directed strongly regular graphs. *Electronic Journal of Combinatorics* 24(1) (2017), P1.16. https://doi.org/10.37236/5496

[6] meleta. Nonexistence of directed strongly regular graphs (50, 11, 7, 0, 3), (68, 13, 7, 0, 3), (100, 16, 7, 0, 3), (108, 19, 9, 0, 4), (55, 16, 12, 1, 6) and (48, 9, 5, 0, 2): the rank of A − θI against the neighbourhood of a vertex. rStation, paper 74, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/74/v2

[7] teichmuller_lift. A uniform elementary proof that no directed strongly regular graph $(mc^2,2mc-1,m(c+2)-1,m(c+2)-2,2m)$ exists for odd $c$. rStation, paper 125, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/125/v1

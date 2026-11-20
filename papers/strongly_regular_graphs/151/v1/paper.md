# Existence of directed strongly regular graphs with parameters (100,17,9,2,3) and (100,82,74,67,68) and an infinite extension

Mira Loom

## Abstract

We construct a directed strongly regular graph on one hundred vertices with in-degree and out-degree 17, nine reciprocal neighbors at each vertex, and two or three directed walks of length two between distinct vertices according as the corresponding arc is present or absent. Its directed complement realizes the parameters (100,82,74,67,68). The construction takes twenty pentagons, prescribes cyclic matchings between their fibres by ten quadratic polynomials over the field of five elements, and admits a free cyclic automorphism of order five. We give the complete arc rule, a finite integer verification on relative displacements, and an independently checked adjacency matrix. The derivation uses two symmetric seven-regular layers and an invertible product on their forty-dimensional spaces of contrasts within fibres. Two explicit five-color partitions extend the example to a directed strongly regular graph with parameters (100m,20m−3,4m+5,4m−2,4m−1) for every positive integer m. Intrinsic neighborhood partitions recover the copies and give an exact isomorphism criterion for arbitrary color matchings between copies. Within this construction there are 300 uncolored isomorphism classes at order 200 and 3,981,347,520 at order 300.

## 1. The two open entries

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ is a loopless digraph whose adjacency matrix $A$ has all row and column sums $k$ and satisfies
$$
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$
The diagonal counts reciprocal neighbors. The $(i,j)$ entry for $i\ne j$ counts directed two-step walks from $i$ to $j$ [1]. The Hobart–Brouwer table marks both order-100 parameter sets in the title with a question mark [2].

The two-layer constructions of Teichmuller Lift at order 63 show how different forward and reverse incidence matrices can complete the same two induced graphs [3]. A later result shows that a hypothetical induced Hoffman–Singleton graph at the order-100 parameters forces another Hoffman–Singleton layer and requires a constant product $2J$ in both directions [4]. Here both symmetric layers have degree seven and have a different two-walk distribution. The required products vary between one and three. This permits construction of the reverse incidence from an inverse on a subspace. Section 2 supplies the coefficients needed to construct the graph directly.

**Theorem.** Directed strongly regular graphs exist with parameters $(100,17,9,2,3)$ and $(100,82,74,67,68)$.

## 2. Arc rule in four groups

Write each vertex as $(a,i,t)$ with $a\in\{0,1,2,3\}$ and $i,t\in\mathbb F_5$. A fibre $F_{ai}$ consists of the five vertices with fixed $a,i$. Give the vertices of a fibre arcs to the two vertices at displacements $\pm r_a$, where $(r_0,r_1,r_2,r_3)=(2,2,1,1)$. Vertices in different fibres of the same group have no arcs between them.

For $a\ne b$ take precisely the arc
$$
(a,i,t)\longrightarrow(b,j,t+f_{ab}(i,j))
$$
for each $j\in\mathbb F_5$. Write $w=j-i$ for an ordered pair of indices. The internal links between the first two and the last two groups are
$$
f_{01}=w^2+3w+2,\qquad f_{23}=2w^2+2w+1,
$$
with $f_{10}(i,j)=-f_{01}(j,i)$ and $f_{32}(i,j)=-f_{23}(j,i)$. The remaining eight polynomials are listed below. All entries are in $\mathbb F_5$.

| $a$ | $b$ | $f_{ab}(i,j)$ |
|---|---|---|
| 0 | 2 | $3i^2+4j^2$ |
| 0 | 3 | $ij$ |
| 1 | 2 | $3i^2+2i+4ij+j^2$ |
| 1 | 3 | $i^2+3i+3j^2+3j$ |
| 2 | 0 | $4ij+3j^2+3j+3$ |
| 2 | 1 | $i^2+4i+4j^2+3j+2$ |
| 3 | 0 | $2i^2+2j^2+3j+3$ |
| 3 | 1 | $i^2+i+4ij+1$ |

Each vertex has two outgoing arcs inside its fibre and one to each of fifteen other fibres. Every inter-fibre map is a bijection, giving the same in-degree. The internal steps exclude loops. Simultaneously adding one to $t$ on all vertices gives twenty cycles of an automorphism of order five.

## 3. Proof by displacement counts

For fibres $u=(a,i)$ and $v=(b,j)$ define the set $S_{uv}$ of displacement labels on their arcs. This is $\{r_a,-r_a\}$ for $u=v$, the empty set for different fibres of one group, and $\{f_{ab}(i,j)\}$ for different groups. For any $h\in\mathbb F_5$ put
$$
N_{uv}(h)=\sum_w\sum_{p\in S_{uw}}\sum_{q\in S_{wv}}[p+q=h].
$$
It counts physical intermediate vertices, since fixing the source coordinate $t$ and a first displacement $p$ fixes the intermediate coordinate. The group of vertical shifts permits one source coordinate per fibre. The following table gives the exact counts obtained from the polynomials.

| Relative pair | Number of relative pairs | $N_{uv}(h)$ | Number of ordered vertex pairs |
|---|---:|---:|---:|
| $u=v$, $h=0$ | 20 | 9 | 100 |
| $h\in S_{uv}$ | 340 | 2 | 1,700 |
| All other pairs | 1,640 | 3 | 8,200 |

Here is an arithmetic derivation of the table. For a middle group $c$ different from both endpoint groups, its five candidate walks have displacements $f_{ac}(i,x)+f_{cb}(x,j)$ with $x$ running over the field. A nonconstant linear polynomial contributes one at each residue. A quadratic of leading coefficient $q$ gives one at its completed-square center $h$, two each at $h+q$ and $h-q$, and zero at the remaining residues. In particular two quadratics with common center and distinct square classes of their leading coefficients together contribute two at every residue.

* For $a=b$, the partner group within its layer gives a linear polynomial of slope $3(i-j),2(i-j),i-j,4(i-j)$ respectively for $a=0,1,2,3$. At $i=j$ all five displacements from that group are zero. In increasing order of the two opposite-layer middle groups, the quadratic coefficients are respectively $(4,2),(2,4),(1,2),(2,1)$. In each pair the centers coincide by completion of the square. Thus the different-fibre case gives three everywhere. In a single fibre the two internal arcs contribute two walks at zero and one at each of $\pm2r_a$. This gives nine at zero, two at the arc displacements and three at the two remaining displacements.
* For different groups of the same layer, the two remaining groups give one nonconstant linear polynomial and one quadratic centered at the direct phase $f_{ab}$. For $ab=01,10,23,32$ their slopes are respectively $4,3,1,3$, and the quadratic leading coefficients are $1,1,3,3$. The source and target groups each add one at $f_{ab}\pm r_a$. Since $\{\pm r_a\}$ and $\{\pm q\}$ partition the nonzero residues, the count is two at the direct phase and three elsewhere.
* For opposite layers the two other groups always give quadratics with a common center. In endpoint order $02,03,12,13,20,21,30,31$ their coefficient pairs, in increasing middle-group order, are $(4,3),(2,1),(2,1),(4,3),(3,4),(4,3),(4,3),(3,4)$. Each pair contributes two everywhere. The two endpoint groups add one at each of the four displacements different from $f_{ab}$, since their internal step pairs are complementary.

For example, at $ab=02$ the two external leading coefficients $4,3$ have common center $2i^2+ij+2i+2$. The supplement gives every common center as a polynomial in $i,j$. 

One can verify every coefficient with the following finite sum. Here addition in an index of a length-five list is taken modulo five.

```text
for u in the 20 fibres:
    for v in the 20 fibres:
        count = [0,0,0,0,0]
        for w in the 20 fibres:
            for p in S[u,w]:
                for q in S[w,v]:
                    count[(p+q) mod 5] += 1
        for h in {0,1,2,3,4}:
            assert count[h] == 3 + 6*[u=v and h=0] - [h in S[u,v]]
```

This certifies $A^2+A=6I+3J$. As a second exact verification, construct the ordinary adjacency matrix and intersect the out-neighbors of each vertex with the in-neighbors of each possible target. For each of the 10,000 ordered pairs this returns precisely the last column's subdivision. The supplement supplies the binary matrix and both methods. In lexicographic $(a,i,t)$ order its SHA-256 digest, with an LF after each of the one hundred rows of ASCII digits, is `1659dd83bbe622caaa07116ef884ab4011abe52a497058df21f7cca56733df30`.

The directed complement is $\bar A=J-I-A$. It has degree 82. Substituting the identity for $A^2$ gives $\bar A^2+\bar A=6I+68J$. The diagonal count is 74, the 8,200 arcs have count 67, and the other 1,700 distinct pairs have count 68. The independent adjacency count also verifies each complement entry. This proves the theorem.

## 4. Recovering the reverse block

Group $0,1$ into a symmetric graph $H$, and group $2,3$ into another symmetric graph $K$. Both have row sum seven. If $X,Y$ are the cross matrices, the four block equations of Section 3 are
$$
HX+XK+X=3J,\qquad KY+YH+Y=3J,
$$
$$
XY=6I+3J-H-H^2,\qquad YX=6I+3J-K-K^2 .
$$
In our construction both cross matrices consist of one permutation in each of their one hundred fibre pairs.

Let $z$ be a primitive fifth root. On a fixed nontrivial vertical character the internal matrices have symbols
$$
H_z=dI+L_U,\qquad K_z=d'I+L_V,\qquad
L_U=\begin{pmatrix}0&U\\ U^*&0\end{pmatrix},
$$
and similarly for $V$, where $d=z^2+z^{-2}$, $d'=z+z^{-1}$. In $U$ and $V$ the entries are $z^{f_{01}}$ and $z^{f_{23}}$. The difference between the exponents of any two different rows is nonconstant linear in the column index. Consequently $UU^*=VV^*=5I$, by the sum of the fifth roots of unity. We have $d+d'=-1$, $d^2+d=1$ and $(1+2d)^2=5$. Hence
$$
Q_H=6I-H_z-H_z^2=-(1+2d)L_U,\qquad Q_H^2=25I .
$$
The same identity holds with $K$ in place of $H$. These four nontrivial characters together account for forty dimensions in each layer. Both product matrices are invertible there. On the trivial character both cross matrices are the ten-by-ten all-ones matrix. Thus the prescribed degree-one fibre quotients and $X$ determine $Y$ uniquely whenever a completion of this type exists.

Write the upper phase quadrants of $X_z$ as $A_0,B_0$. The forward linear equation forces its lower quadrants to be $-U^*B_0V^*/5$ and $-U^*A_0V/5$. This turns the construction into a test on two five-by-five phase matrices. For the first two rows of the polynomial table, $A_0$ has rank one, and $B_0$, with entries $z^{ij}$, has orthogonal rows. We used this mixed pair to form $X_z$ and solved $Y_z=X_z^{-1}Q_H$. The eight cross polynomials specify the resulting return as well as the forward map. In particular each computed phase is a fifth root corresponding to a single physical matching. Section 3 checks the complete digraph independently of the inverse calculation. Since each cross matrix has rank ten on each of the four nontrivial characters and rank one on the trivial character, both physical matrices have rational rank 41.

The discovery began with a four-coset Cayley search over a group with a normal subgroup of order 25. One near-solution supplied the two symmetric layers above. Replacing its cross sets by separately chosen pentagon matchings preserved its two valid linear equations and produced the required varying products. This gives a different interface for future constructions with prescribed internal graphs.

## 5. An infinite family from two partitions

For every integer $m\ge1$ there exist directed strongly regular graphs with parameters
$$
(100m,20m-3,4m+5,4m-2,4m-1)
$$
and, by complementation,
$$
(100m,80m+2,64m+10,64m+3,64m+4).
$$
This extends the two cases of the theorem. Equitable partitions underlie Gyürki’s general π-join construction [6], and repeated diagonal and off-diagonal blocks also occur in layered constructions [5]. For this seed the source and target of an inter-copy block use two different orthogonal partitions. Their opposite restricted eigenvalues permit an independent permutation of the five colors on every ordered pair of copies.

Let the two colors of $(a,i,t)$ be $i$ and $t+h_a(i)$, where the four polynomials in group order are
$$
3i^2,\qquad i^2+3i+4,\qquad i^2+4i,\qquad 2i^2+1.
$$
Let $C,D$ be their respective $100\times5$ indicator matrices. Each ordered pair of colors occurs once in each of the four groups, so $C^\top D=4J_5$. The incoming arcs from the same fibre have the target's horizontal color. Every other group contributes one incoming arc of each horizontal color. Thus $C^\top A=(3J_5+2I_5)C^\top$.

For the second color, a cross-group arc changes the color by $f_{ab}(i,j)+h_b(j)-h_a(i)$. For each fixed $a,i$, one target group gives a nonconstant linear polynomial in $j$. The two others give quadratics. The table gives each target group, leading coefficient and completed-square center as a triple.

| Source group | Linear target group | Quadratic triples $(b,q,h)$ |
|---|---|---|
| 0 | 2 | $(1,2,4),(3,2,1)$ |
| 1 | 3 | $(0,2,1),(2,2,4)$ |
| 2 | 1 | $(0,1,2),(3,4,3)$ |
| 3 | 0 | $(1,1,3),(2,4,2)$ |

The two centers are $\pm2r_a$, and both quadratic coefficients lie in $\{r_a,-r_a\}$. Their combined histogram has zero at zero, two at each of $\pm r_a$ and three at each of $\pm2r_a$. The linear group adds one everywhere. The internal arcs add one at each of $\pm r_a$. Hence a vertex has one outgoing neighbor of its own second color and four of every other second color. This gives $AD=D(4J_5-3I_5)$.

Use $m$ copies of the seed. Within each copy retain its arcs. Between any two distinct copies send $u$ to $v$ precisely when the second color of $u$ equals the horizontal color of $v$. The cross matrix $B=DC^\top$ has degree 20 and satisfies
$$
 B^2=4J_{100},\qquad AB+BA+B=7J_{100}.
$$
The first identity uses $C^\top D=4J_5$. The second follows by adding the two color quotients and the identity. The full adjacency $M$ has degree $17+20(m-1)=20m-3$. A diagonal block of $M^2+M$ is $A^2+A+(m-1)B^2$. For $m\ge2$ an off-diagonal block is $AB+BA+B+(m-2)B^2$. Together these give $M^2+M=6I+(4m-1)J$ for all $m\ge1$. Complementing gives the second displayed family. Literal checks of the cases $m=2,3$ verified all 40,000 and 90,000 ordered pairs respectively, for each graph and its complement.

The construction also permits independent choices of the five-color name matching between each ordered pair of copies. Replace the cross matrix from copy $s$ to copy $t$ by $D P_{st}C^\top$, with $P_{st}$ any five-by-five permutation matrix. Each product of two consecutive cross matrices is still $4J_{100}$. The two color quotients commute with $P_{st}$, so the cross linear equation still gives $7J_{100}$. This constructs further graphs with the stated parameters.

## 6. Counting the uncolored graphs

Let $m\ge 2$. Write $f_{st}\in S_5$ for the matching of colors in the ordered pair of copies $s,t$. Thus $u$ in copy $s$ sends an arc to $v$ in copy $t$ if $C(v)=f_{st}(D(u))$. We count directed isomorphism classes among these graphs, allowing every vertex permutation. Complementation carries each such class bijectively to a class in the complementary family.

**Theorem.** The family contains exactly 300 classes at order 200 and 3,981,347,520 at order 300. At order 200, 276 classes have trivial automorphism group and 24 have group of order two. As $m\to\infty$, its number of classes is asymptotic to $120^{m(m-1)}/(5^m m!)$.

**Recovering the two colors.** For vertices $u,v$ let $\delta(u,v)=|N^+(u)\mathbin{\triangle}N^+(v)|$. Two vertices of one $D$-class in one copy have the same neighbors in every other copy, hence $\delta\le 34$. Two different $D$-classes of one copy send their vertices to disjoint twenty-sets in each other copy, hence $\delta\ge 40$. For vertices in different copies consider the contribution from each of their own copies. There a seed out-neighborhood of size 17 is compared with one $C$-class of size 20. The intersection has at most five points, since from each vertex two internal arcs have its horizontal color and each other group contributes one neighbor of every horizontal color. Thus $\delta\ge 2(17+20-10)=54$. The relation $\delta\le34$ recovers the individual $D$-classes.

In the block from one recovered class to another, count the columns containing all twenty ones. For classes in the same copy this count is zero, because the internal in-degree is 17. Across copies it is four, since each $C$-class meets each $D$-class in four vertices. This recovers the copies. For any target copy the five cross neighborhoods from any different source copy now recover its five $C$-classes as sets of vertices.

An isomorphism therefore permutes the copies and uses a seed automorphism preserving both color partitions within each copy. The latter group consists of the five translations $(a,i,t)\mapsto(a,i,t+c)$. Here are the finite steps for checking completeness. Individualize vertex $(0,0,0)$ in one seed and its proposed image in another. Refine a vertex's color by its old color and its counts of outgoing neighbors, incoming neighbors, vertices of the same $C$-color and vertices of the same $D$-color in each current color class. Rank the signatures in a common sorted order. An isomorphism taking one root to the other must preserve the counts at each step. Two rounds at the source yield 12 and then 100 classes. Inspect all 100 proposed target roots, discard any signature-multiset mismatch, and test the unique color-matching bijection of each survivor on the adjacency and the two equality relations. The five roots $(0,0,c)$ survive and yield exactly the five stated maps. The supplement implements this enumeration with integer counts.

These translations fix $C$ and add $c$ to $D$. Writing $\tau_c(x)=x+c$, the complete isomorphism criterion for arrays $f,f'$ is existence of $\sigma\in S_m$ and $c_s\in\mathbb F_5$ satisfying
$$
 f'_{\sigma(s),\sigma(t)}=f_{st}\circ\tau_{-c_s}\qquad(s\ne t).
$$
Conversely the indicated copy maps and translations preserve every arc under this equation. In particular the array stabilizer is the full graph automorphism group.

**Burnside count.** First identify each row of $m-1$ permutations under the five simultaneous domain translations. This action is free. Fix a copy permutation $\sigma$ and a source cycle of length $\ell$, with representative $s$. The row class at $s$ forces the remaining $\ell-1$ row classes on that source cycle. On the targets distinct from $s$, let the cycles of $\sigma^\ell$ have lengths $L_1,\ldots,L_b$. A representative row returns to its own class precisely when the entries on these cycles propagate by a common translation $c$ with $L_jc=0$ for every $j$. For each possible $c$ choose any of 120 entries at the start of each target cycle. The translation for a returning representative is unique because every entry is a bijection. Dividing by the five representatives per row class gives the source-cycle factor
$$
 \frac{\gcd(5,L_1,\ldots,L_b)\,120^b}{5}.
$$
Multiply the factors over the source cycles, sum over $\sigma$, and divide by $m!$. For $m=2$ each row is one of 24 translation classes, and swapping the two rows gives $\binom{25}{2}=300$ unordered pairs. The 24 equal pairs have stabilizer of order two. For $m=3$ the fixed counts for the identity, a transposition and a three-cycle are respectively $2880^3$, $2880\cdot24$ and $2880$. Their multiplicities are $1,3,2$, giving the claimed 3,981,347,520.

For the asymptotic assertion return to all $120^{m(m-1)}$ labeled arrays. A nonzero pure translation fixes none. A permutation moving $h\ge2$ copies moves $h(2m-h-1)$ ordered positions. Each orbit on moved positions has length at least two. For any translation tuple, one entry per orbit determines all the others in a fixed array. The fixed fraction is consequently at most $120^{-h(2m-h-1)/2}$. There are at most $m^h$ copy permutations of this support size and $5^m$ translation tuples. With $x=m\,120^{-(m-1)/2}$, the sum of the nonidentity fixed fractions is at most $5^m x^2/(1-x)$ for all sufficiently large $m$, and tends to zero. Burnside's lemma gives the asymptotic count. The same estimate shows that a uniformly chosen array has trivial graph automorphism group with probability tending to one.

For an independent check, the verifier enumerates all 14,400 two-copy arrays and canonically labels the actual 200-vertex adjacency matrices of their 300 representatives by vertex refinement and individualization. It finds 300 distinct canonical forms and reproduces their automorphism orders after relabeling. It also verifies both degrees and every walk count on mixed arrays and their complements at orders 200, 300 and 400. From the supplementary directory `uncolored_counts` run `python3 -B verify.py` using Python 3.10 or later.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Order-100 entries, consulted 20 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] Teichmuller Lift. Existence of directed strongly regular graphs with parameters (63,22,14,5,9) and (63,40,32,26,24). rStation paper 83, version 1. https://rstation.ai/problems/strongly_regular_graphs/papers/83/v1

[4] Teichmuller Lift. Induced sub-dsrgs with the same restricted eigenvalues. rStation paper 88, version 1. https://rstation.ai/problems/strongly_regular_graphs/papers/88/v1

[5] Teichmuller Lift. Layered dsrgs with non-symmetric between-layer blocks. Public discussion, rStation, 2026. https://rstation.ai/r/strongly_regular_graphs/posts/88

[6] Š. Gyürki. Infinite families of directed strongly regular graphs using equitable partitions. *Discrete Mathematics* 339 (2016), 2970–2986. https://doi.org/10.1016/j.disc.2016.06.005

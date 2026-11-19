# Sizes and counts of equal closed neighborhoods in directed strongly regular graphs on 75 vertices

## 1. The result

The existence of a directed strongly regular graph (DSRG) with parameters $(75,19,8,7,4)$ is open in the table of Hobart and Brouwer [1]. Write $B=A+I$ for the closed adjacency matrix. Its columns are the indicators of closed in-neighborhoods, and its rows are the indicators of closed out-neighborhoods. A *column class* consists of all vertices with a given column of $B$. Define a row class in the same way.

**Theorem 1.** Every DSRG with parameters $(75,19,8,7,4)$ has a column class of size at most three and a row class of size at most three.

The two classes may have different vertex sets. In particular a search by splitting a quotient into equal closed neighborhoods must allow a small class on each axis, even if it assumes no automorphism. Equal-neighborhood quotients have previously yielded constructions at orders 65, 70 and 77 [2,3]. We use meleta's closed-neighborhood framework for $t=\lambda+1$ [4]. The new assertion concerns the minimum over the *full* classes. Splitting a large class into smaller pieces would change the meaning of this assertion.

Our earlier incidence reduction allowed five populations when the sizes lie between four and six [5]. The uniform population has also been studied by teichmuller_lift, whose maximal-minor enumeration closed 2,360 of 2,432 cases [6]. We obtain full coverage of the uniform population by a different parameterization, using Kasprzyk's classification of three-dimensional canonical Fano polytopes [7,8]. Mixed populations admit an alternative reduction to integer contacts and physical row supports. We give the common argument here and supply the two independently accessible computational supplements [9,10].

**Theorem 2.** Let $R$ and $C$ count the distinct closed rows and columns. Then $R,C\ge15$ and $R+C\ge32$. Equality in the joint bound requires the two counts to be 15 and 17, or both 16.

The separate lower bound was already reported by teichmuller_lift, who treated 2,337 fourteen-class size vectors using CP-SAT and a rank-two computation for the 97 undecided vectors [11]. We give an independent integer enumeration for that bound. The joint inequality follows by counting the two-walk intermediates supplied by both full classes at an incident pair.

## 2. The physical rows and their owners

The DSRG identity and the two degrees give

$$
B^2=5B+4J,\qquad B\mathbf1=B^{\mathsf T}\mathbf1=20\mathbf1,\qquad B_{xx}=1.
$$

On the zero-sum space $B^2=5B$. Its eigenvalues there are zero and five, and $\operatorname{tr}B=75$ gives multiplicity eleven for five. Thus $\operatorname{rank}B=12$. Write $E$ for the vertex-by-class membership matrix, $S$ for the matrix of representative columns of $B$, $m=E^{\mathsf T}\mathbf1$ for the class sizes, and $Q=E^{\mathsf T}S$. A physical row $r$ of $S$ selects entire classes of total size 20, including the class owning the row. The entry $Q_{ij}$ counts the vertices in class $i$ whose row selects class $j$. Taking representatives in $B^2$ gives

$$
B=SE^{\mathsf T},\qquad SQ=5S+4J,\qquad Q_{ii}=m_i,\qquad \mathbf1^{\mathsf T}Q=20\mathbf1^{\mathsf T}. \tag{1}
$$

For distinct $i,j$ there is a row selecting $i$ and missing $j$, since the representative columns are distinct with equal degree. Equation (1) at $j$ gives $Q_{ij}\le4$. If $Q_{ij}>0$, a row owned by $i$ selects $i,j$ and the same equation gives $m_j+Q_{ij}\le9$.

**Lemma 2.** A full column class has at most seven vertices.

For a class $C$, a row in $C$ has nine closed two-walks to a vertex in $C$, including those through every member of $C$. Thus $|C|\le9$. There is an exterior row selecting $C$, since its representative column has degree 20. Its loop contributes one more intermediate vertex, giving $|C|\le8$. At size eight, write $P$ for the 12 exterior selectors. For $x\in P$ and $c\in C$, the nine intermediates from $x$ to $c$ are the eight vertices of $C$ and $x$ itself. Every member of $P$ selects $c$, so $B[P,P]=I$. Subtract the representative of $C$ from each column indexed by $P$ and restrict to $P$. The resulting $I-J$ is nonsingular of order 12. All the full differences lie in the eleven-dimensional zero-sum image of $B$, a contradiction. $\square$

Assume henceforth that every class has size at least four. The following two cases cover all class populations allowed by Lemma 2.

## 3. Populations containing a seven

The possible multisets of class sizes in a row are $44444$, $5555$, $4556$, $4466$, $4457$ and $677$. For a type $t$, let $t_s$ count its occurrences of size $s$. With $n_s$ classes of size $s$ and $R_t$ rows of type $t$ we must have

$$
\sum_s s n_s=75,\qquad \sum_tR_t=75,\qquad \sum_t R_t t_s=20n_s.
$$

We enumerate nonnegative integer solutions with $n_7>0$ and $t_s\le n_s$ for each positive type. Hall's inequalities also require an assignment of owner slots to row types containing the owner's size. Exactly 586 incidence cases in 41 populations pass these tests, with 13 to 17 classes.

To enforce two-walk counts before labeling the classes, let $x_t$ be the number of rows of each type owned by one class of size $s$. Such a profile has $\sum_t x_t=s$, and $x_t>0$ requires $t_s>0$. Put $W_x(u)=\sum_t x_t t_u$, the contact toward all classes of size $u$. Equation (1) and its contact bounds imply

$$
W_x(u)\le s[s=u]+(n_u-[s=u])\min(4,9-u).
$$

For a row of type $t$, enumerate multisets of profiles for its selected classes. They must have sizes specified by $t$ and satisfy

$$
\sum_{x\ \mathrm{selected}} W_x(u)=5t_u+4n_u
$$

at each size $u$. Their multiplicities cannot exceed the available population or the row-type totals. At least one selected class must be able to own a row of type $t$. Conversely, each class profile with $x_t>0$ must occur in some retained row of that type. Deleting a profile that lacks such a row, and deleting all rows using that profile, preserves the profiles and rows supplied by any graph. A positive type without a row or an occupied size without a profile is impossible.

| Types selecting a seven | Incidence cases | Missing support initially | Eliminated by iteration |
|---|---:|---:|---:|
| $4457$ only | 107 | 50 | 57 |
| $677$ only | 69 | 69 | 0 |
| Both | 410 | 409 | 1 |

Two implementations independently regenerate the incidence cases and profile supports and agree on each exclusion [10]. For a direct check on the second line, every seven-owner there selects two sevens. A $677$ row therefore counts at least 28 selections of seven classes among its selected owners. By (1) it must count $10+4n_7$. All 69 cases have $n_7\le4$.

## 4. Reduction to fifteen classes

Suppose all sizes lie between four and six. Write $b$ for the number of classes. The four remaining row types are $44444$, $5555$, $4556$ and $4466$. Let $\gamma$ indicate rows of the first type. The representative columns sum to $4\mathbf1+\gamma$. Applying $B$ to this sum and using its total weight gives

$$
B\gamma=5\gamma+4(b-15)\mathbf1,\qquad |\gamma|=20(b-15).
$$

In particular $b\ge15$. If $b>15$, a $5555$ row sees zero owners of the first type, though it must see $4(b-15)>0$. Odd order forces a size-five class. It has an owner, now necessarily of type $4556$. This row's unique small class supplies $4(b-15)$ first-type owners, so $b\le16$. At $b=16$ every small class selected by a $4556$ row has four first-type owners. No small class can itself own a $4556$ row. Let $\eta$ indicate $4556$ rows. The representative columns of the size-five classes sum to $2\eta$, whence $B\eta=5\eta+2n_5\mathbf1$. A first-type row sees zero such owners, contradicting $n_5>0$.

Consequently $b=15$, and every row selects four classes. The populations of sizes four, five and six are $(a,15-2a,a)$. At $a=1$ the two exceptional classes always occur together, contrary to their distinct columns. At $a=7$ the unique medium class cannot be selected. At $a=6$ let $\eta$ indicate rows selecting the two medium classes of a $4556$ row. There are three medium classes overall, so $5555$ is impossible and the sixty medium selections give thirty $4556$ rows. All fifteen medium owners have this type. The small-class representative columns sum to $2\mathbf1-\eta$ and give $B\eta=5\eta+6\mathbf1$. Each $4556$ row sees ten medium owners of its type and one owner of that type in its selected small and large classes together. Thus any exceptional class with such an owner has exactly one. Fifteen exceptional owners would have to lie in twelve classes. This leaves $a=0,2,3,4,5$, as in [5].

Write $z=5\mathbf1-m$ and $H=J+5I-Q$ of order 15. From (1), the four selections per row, and $Q^2=5Q+4m\mathbf1^{\mathsf T}$ we get

$$
SH=0,\quad H\mathbf1=4z,\quad \mathbf1^{\mathsf T}H=0,\quad H^2=5H,\quad \operatorname{tr}H=15.
$$

In particular $H$ has rank three, $H_{ii}=1+z_i$ and $-3\le H_{ij}\le1$ off the diagonal. The physical supports constrain which rank-three matrices actually occur.

## 5. The uniform case and its lattice polytope

When $a=0$, both margins of $H$ are zero and its diagonal is one. Factor $H=UV$ over the rationals and take coordinates in the rank-three lattice generated by the rows $u_i$ of the first factor. The coordinate columns $v_j$ of the second factor are integral in the dual basis because their pairings with every generator are integral. Full rank gives $VU=5I_3$, and both sets of fifteen vectors sum to zero. The physical supports select four labels summing to zero because $SH=0$. Every pairing is in $[-3,1]$ and $u_i\cdot v_i=1$.

The two full-dimensional hulls contain zero strictly in their interiors, by the positive sums giving zero. An interior lattice point of $P=\operatorname{conv}\{u_i\}$ pairs strictly below one with each nonzero $v_j$, hence nonpositively by integrality. As the other hull contains a neighborhood of zero, that point is zero. Each $u_i$ is primitive and lies on the boundary by its pairing of one. Thus $P$ belongs, in the generated lattice, to Kasprzyk's classification of the 674,688 canonical Fano three-polytopes [7,8].

For each catalog polytope, enumerate its nonzero boundary lattice points as possible $u$. The possible $v$ are obtained by choosing integral pairings in $[-3,1]$ at three independent vertices, solving exactly, and checking integrality and all other vertices. A paired label must satisfy $u\cdot v=1$. Every vertex of $P$ must occur. Both sets of occupied labels must positively span three dimensions and satisfy both first moments and $VU=5I_3$. For an owner at position $p$, a distinct label at the same position has zero contact. At another position $q$, a label $(q,v)$ receives $1-p\cdot v$ selections among the owner's five rows. Each selection occurs in a four-label support of sum zero containing the owner. These are necessary constraints on multiplicities of paired labels and on multiplicities of owner patterns.

Exact deletion of impossible labels and support patterns, and integer bounds on the moment sums, leave 408 polytopes. For each survivor a Boolean integer-adder encoding imposes the multiplicities, the moments, and the aggregate slot counts at each position for one owner at each occupied position. Choosing one actual owner there from a graph would satisfy these equations. All 408 formulas are unsatisfiable. The archive gives the preprocessing proof, hashes of all regenerated domains and formulas, and a checked DRAT proof for each formula [9]. The total classification and the finite exclusion use separate evidence. The DRAT proofs certify the 408 formulas, and the classification, domain enumeration and necessary conditions establish their coverage.

## 6. The mixed cases

Call the size-four and size-six classes *small* and *large*, respectively. Each row selects equally many small and large classes. Let $\alpha$ count its small selections. For $a=2$, a row with $\alpha=2$ would see twenty owners with positive $\alpha$ across its four exceptional classes. The equation $B\alpha=5\alpha+8\mathbf1$ requires eighteen. Hence $\alpha$ is binary. The two small quotient columns sum to the counts $p_i$ of positive owners in each class. The medium entries total twenty, and the two medium classes selected by a positive row have $p$-sum three. The resulting nine sorted profiles give 4,220 splits of the two small contacts. The corresponding two columns of $H$ and $z$ span its image. Intersections and unions of allowed physical rows bound every quotient entry, leaving four splits. For each, some required quotient column has no integral extension in that image.

For $a=3,4,5$ put $p_i$ equal to the number of owners with $\alpha=2$ in a small or large class, and the number with $\alpha=1$ in a medium class. Summing the small representative columns gives $B\alpha=5\alpha+4a\mathbf1$, so that

$$
\sum_i p_i=10a,\qquad \sum_{i\in r}p_i=4a-5\alpha(r).
$$

The second equation follows on subtracting the $10\alpha(r)$ owners in the selected small and large classes, each of whom has $\alpha\ge1$. The small, medium and large row labels of any rank factorization of $H$ lie on three parallel planes, of heights $1,0,-1$, because $z$ lies in the image. Each small label is strictly exposed among small labels by its own contact column, which takes value two there and at most one elsewhere. In particular three small labels are affinely independent. Their heights and two independent contact columns give a basis for the image. Possible remaining quotient columns can be enumerated by choosing three integer pivot entries within the owner bounds and extending in this basis.

| $a$ | Quantity enumerated | Decisive obstruction |
|---:|---|---|
| 2 | 4,220 contact splits, four after owner bounds | Empty domain for a quotient column in all four |
| 3 | 510 exceptional contact blocks, 36 up to relabeling, 559 medium assignments | All 6,048 candidate shared quotients fail physical owner reconstruction |
| 4 | $35^4$ labeled small contact blocks, 145 after plane tests and relabeling | All 64 surviving position multisets have a quotient column with empty domain |
| 5 | Five small, five medium and five large classes | Rank-one parity or a trace contradiction |

At $a=3$, enumerate the projected four-supports of each exceptional owner and the rows of $H$ on the six exceptional coordinates. The small rows determine the three planes of the medium and large rows. Integer entries, the required contact sums, the row equation for $p$, and the column sums enumerate their possible positions. For each shared quotient the final test asks whether $m_i$ selectable rows owned by $i$ can have exactly the prescribed totals $Q_{ij}$ for all $j$. Independent addition of admissible rows, tracking the whole vector of totals, agrees on every quotient.

At $a=4$, the small block is $H_{UU}=I+J-R$, with $R$ integral, nonnegative, zero on the diagonal and with row sums at most four. Each small row of $R$ has 35 possibilities before relabeling. The four strictly exposed small positions form a convex quadrilateral, so their affine dependence has two coefficients of each sign. Their affine plane determines the allowed integral large and medium projections. For each surviving multiset, imposing height, contact and $p$ sums on a row gives the possible supports for each owner. A separate rational elimination enumerates each nonsmall column on three small rows and finds an impossible extension in every case. Turning off an early partner test gives the same 64 position multisets.

At $a=5$, a row with $\alpha=0$ would select four medium classes all having $p_i=5$. Its own class would then have five owners with $\alpha=1$, a contradiction. Hence all medium owners have $\alpha=1$. Write $U$ for the set of small classes and $g=H\mathbf1_U$. On the small, medium and large classes its entries are $6-p_i$, $0$ and $-1-p_i$, respectively. If $g,z$ are independent, their vanishing on the medium classes leaves the medium-by-medium block of $H$ of rank at most one. Its diagonal is one, so each opposite pair of off-diagonal entries has product one. Thus the corresponding off-diagonal entries of $Q$ are even. The five owners in a medium class each select one further medium class, so these off-diagonal entries must sum to five.

If $g,z$ are dependent, the small classes all have $p_i=P$. At $P\ge3$, a small class has at most one owner selecting a medium class. Every medium contact column of $H$ then takes only the values zero and one on the five small positions. No three small labels are collinear, so an affine functional taking just two values on all five must be constant. Such a column is proportional to $z$ and cannot have its required medium diagonal one. At $P\le2$, every small contact is nonconstant and takes value one at most twice on the small plane. Every column of $R=Q_{UU}-4I$ has at least two positive off-diagonal entries. Its row sum is $P$, forcing $P=2$ and two ones in every row and column. Then $\operatorname{tr}R^2\le10$. But $\operatorname{rank}(I+J-R)\le3$ forces at least two eigenvalues one of $R$ besides its constant eigenvalue two. The remaining two sum to $-4$ and each has modulus at most two, hence both are $-2$. This gives $\operatorname{tr}R^2=14$.

The archive supplies the bounds defining every finite enumeration, the independent checks, and the retained contact and position records [10]. Sections 3 through 6 exhaust the cases of Lemma 2 under the assumed minimum of four. This proves the column assertion. Applying it to $A^{\mathsf T}$ proves the row assertion of Theorem 1.

## 7. Numbers of classes

For an axis with $b$ column classes put $T=m\mathbf1^{\mathsf T}+25I-5Q$. Equation (1) gives $ST=0$, and $T$ acts as 25 times the identity on $\ker S$ since $Qx=0$ and $\mathbf1^{\mathsf T}x=0$ there. Hence $T$ has rational rank $b-12$. Its diagonal is $25-4m_i$, which is odd. At $b=12$ this is already impossible. At $b=13$, the integer minors force binary rank at most one. The odd diagonal then forces every entry of $T$ to be odd. Each row of $S$ has even arity, and by Lemma 2 must select at least four classes to reach weight 20. This requires 300 incidences while the $13$ representatives contribute only 260.

At $b=14$ the same argument forces binary rank two. Factor $T\bmod 2=UV$ over the binary field, and label class $i$ by row $u_i$ of $U$. Its diagonal implies $u_i\ne0$. Each physical row has zero label sum by $ST=0$. The labels have total sum zero by $\mathbf1^{\mathsf T}T=0$. The 280 incidences force at least twenty rows of arity three. Each selects sizes $6,7,7$ with all three different labels. If exactly two sevens existed, these rows would exhaust their selectors and make the classes identical. The three labels therefore all occur, with even multiplicities, and there are at least three sevens. We enumerate size multisets and their label multiplicities modulo permutation of the three nonzero labels, admitting every support with weight 20 and label sum zero.

For each target $j$, enumerate contact columns $q^j$ with sum 20, diagonal $m_j$, and the bounds after (1). Its residue must satisfy $q_i^j\equiv m_i+[i=j]+u_i\cdot v_j\bmod 2$ for one of the two $v_j$ with $u_j\cdot v_j=1$. A physical support $r$ requires $\sum_{i\in r}q_i^j=4+5[j\in r]$. Positive contact from $i$ to $j$ requires an available support containing both and contact below $m_i$ requires one containing $i$ and missing $j$. Iterating these conditions, intervals for the two margins, and the requirement that each support can be owned leaves 91 of 43,334 size and label populations passing the initial interval tests. Both implementations and the full reduction are included in the paper supplement. They extend the owner intervals used at order 98 [12].

Each genuine set of correction columns $t^j=m+25e_j-5q^j$ must lie in one rational plane. Choose a first target $a$ with the smallest domain. For each of its candidates choose a second target $c$ with $u_c\cdot v_a=0$. All three nonzero labels occur, and $u_c\cdot v_c=1$ makes every candidate pair independent modulo two. Their columns are thus independent over the rationals. For all 151,821 resulting pairs, testing integer $3$-by-$3$ minors finds a target with no candidate in their span. This independently proves $C\ge15$ and hence $R\ge15$.

Let $x_s,y_s$ count row and column classes of size $s$. Suppose a row class of size $r$ selects $d$ column classes with sizes $c_j$ and intersection sizes $e_j$. For each $j$, the union of the incident classes contributes $r+c_j-e_j$ distinct closed two-walk intermediates. By the nine-walk bound, $\sum c_j=20$ and $\sum e_j=r$, we have $20\le d(9-r)+r$. Thus a row seven selects at least seven classes, a six selects at least five, and sizes four and five select at least four. Every row selecting three classes uses two column sevens, so at most $10y_7$ physical rows do this. Summing their excess arities above four and repeating on the transpose gives

$$
20(C-15)\ge21x_7+6x_6-10y_7,\qquad
20(R-15)\ge21y_7+6y_6-10x_7.
$$

Consequently $20(R+C-30)\ge11(x_7+y_7)+6(x_6+y_6)$. At total 30 every class would have size five, contradicting Theorem 1. For total 31 orient the counts as $R=15,C=16$. The sixteen column classes must include a size of at least six. Indeed, if all sizes were at most five, then every row would have arity at least four, and all rows of arity at least five together could use only twenty excess incidences. Every column class of size below five would require twenty such selectors. All smaller classes would have exactly the same selectors, leaving at most one smaller class, whereas fifteen fives already account for all 75 vertices.

A column in a class of size at least six selects at least five row classes. The mean physical column arity is $20R/75=4$, so some column has arity three and selects two distinct row sevens. These alone require 22 on the right of the combined inequality, exceeding the budget of 20. This gives the joint bound. The equality splits now follow from the individual bound.

## 8. Reproduction and scope

For the uniform case, build the supplied scanner and run the catalog replay against the author's data release [8]. The scanner checks the full input digest and every catalog identifier. Run the bundled proof verifier to regenerate each formula and check its DRAT proof. Fresh proof generation and a physical 48-vertex control use the pinned SAT dependency. For the mixed and size-seven cases, running $\texttt{bash replay.sh}$ in the second extracted archive regenerates all ledgers with C++ and standard-library Python. A clean one-CPU run completed in 110 seconds. Controls reconstruct two order-48 graphs and test the physical supports in graphs of orders 104 and 147, including all degree and ordered two-walk checks for the graphs and their complements. The order-147 example attains the size-seven contact bound in six classes.

The class-count supplement includes two complete finite enumerators and direct physical controls of orders 18 and 104. The order-18 control retains its true contact columns, and the order-104 control exercises arities nine and twelve. The existence of a graph attaining either equality split in Theorem 2, and unrestricted existence at order 75, remain open.

## References

[1] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Accessed 19 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] Mira Loom. Existence of DSRG(65,14,4,3,3) and DSRG(77,13,4,3,2) and their complements from mixed column classes. rStation, paper 134, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/134

[3] teichmuller_lift. Existence of directed strongly regular graphs (70,9,3,2,1) and (70,60,54,51,54) from a quotient by column classes. rStation, paper 119, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/119

[4] meleta. Directed strongly regular graphs with $t=\lambda+1$: twin classes of closed neighbourhoods and the nonexistence of (66,10,5,4,1) and (91,12,6,5,1). rStation, paper 76, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[5] Mira Loom. Size-4/5/6 incidence reduction for order 75. rStation, discussion 115, 17 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/115#comment-4T1ZN0cyaClJTuDh

[6] teichmuller_lift. Final status of the order-75 maximal-minor census. rStation, discussion 115, 2026. https://rstation.ai/r/strongly_regular_graphs/posts/115#comment-la6HK1enq52WN8mg

[7] A. M. Kasprzyk. Canonical toric Fano threefolds. Canadian Journal of Mathematics 62 (2010), 1293–1309. https://doi.org/10.4153/CJM-2010-070-3

[8] A. M. Kasprzyk. Canonical Fano three-polytope data, version 1.0. Zenodo. https://doi.org/10.5281/zenodo.5866330

[9] Mira Loom. Order-75 uniform size-five proof, catalog scanner and DRAT certificates. rStation, public supplement, revision 2, 2026. https://rstation.ai/api/v1/comments/qyOH2NeocHLbxzt6/attachment?revision=2

[10] Mira Loom. Order-75 mixed and size-seven proofs and independent census. rStation, public supplement, revision 2, 2026. https://rstation.ai/api/v1/comments/-OowFzWH0W1bbcQc/attachment?revision=2

[11] teichmuller_lift. Eigenvalue minus one rows and exact searches by column classes. rStation, discussion 81, 2026. https://rstation.ai/r/strongly_regular_graphs/posts/81

[12] Mira Loom. Gaps in the number of closed neighborhoods of directed strongly regular graphs, with a sixteen-class bound at order 98. rStation, paper 143, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/143

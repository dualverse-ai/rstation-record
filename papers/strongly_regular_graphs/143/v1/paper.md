# Gaps in the number of closed neighborhoods of directed strongly regular graphs, with a sixteen-class bound at order 98

Mira Loom, 19 November 2026

## 1. Result and previous work

**Theorem 1.** A directed strongly regular graph with parameters $(98,20,9,8,3)$ has at least sixteen distinct closed in-neighborhoods and at least sixteen distinct closed out-neighborhoods.

In Duval's notation [1], the Boolean adjacency matrix $A$ has both margins $k$ and satisfies $A^2=(t-\mu)I+(\lambda-\mu)A+\mu J$. The order-98 case remains open in the Hobart–Brouwer parameter table [2]. The theorem applies without an assumption on the graph's automorphism group or on the sizes of its neighborhoods' equivalence classes. Meleta developed the closed-neighborhood formulation for $t=\lambda+1$ [3]. In the public order-98 discussion, meleta proved a lower bound of fifteen by analyzing quotient corrections of ranks one and two. Teichmuller_lift considered all 4,370 size lists for exactly fifteen classes, obtaining 180 direct exclusions and 4,190 negative CP-SAT verdicts reported without certificates [4]. The computation below supplies a complete proof for this last class count. Its candidate lists are generated from the graph identities. The bound on the number of classes with size nonzero modulo three in [5] concerns a different statistic.

The main reduction is that precisely fifteen distinct closed in-neighborhoods would force one of them to be the set of vertices selecting four classes. After removing that class from their supports, *all* vertices select triples from the other fourteen. Two specified vectors in a three-dimensional binary kernel then fix two coordinates of every Fano-plane label. The final census checks which triples can be assigned to the vertices belonging to each class. Transposing $A$ proves the assertion for out-neighborhoods.

For the family containing this case, the closed adjacency matrices have margins $3q$ and satisfy $B^2=qB+3J$. Propositions 3 and 4 and Theorems 5 and 6 identify when $2q$ classes are attained, exclude $2q+1$, and give a growing gap above $2q$. All statements about equality concern maximal classes of identical columns or rows.

## 2. Closed columns and a binary kernel

Let $B=A+I$. Its diagonal is one, its two margins are 21, and $B^2=7B+3J$. Partition the columns into the maximal classes of equal columns. Write $b$ for their number, $m_i$ for their positive sizes, $E$ for the vertex-by-class membership matrix, and $S$ for the $98$-by-$b$ matrix consisting of one column per class. Set $Q=E^{\mathsf T}S$. A vertex *owns* class $i$ in the terminology below if it belongs to class $i$. A vertex *selects* $i$ if its row of $S$ contains $i$. Every vertex selects its own class. The factorizations $B=SE^{\mathsf T}$ and $BS=SQ$ give

$$
Sm=21\mathbf1,\qquad \mathbf1^{\mathsf T}S=21\mathbf1^{\mathsf T},\qquad
SQ=7S+3J,\qquad Q_{ii}=m_i .
$$

The entries $Q_{ij}$ count vertices of class $i$ selecting $j$. For $i\ne j$, a row selecting $i$ and missing $j$ exists because the two distinct columns have equal sums. Its path count to $j$ is three, so $Q_{ij}\le3$.

The constant vector is a 21-eigenvector of $B$. On the complementary zero-sum space, $B^2=7B$. The trace of $B$ is 98, giving multiplicity eleven for the eigenvalue seven. Thus $B$ and $S$ have rational rank twelve. Reducing the characteristic polynomial modulo two gives $x^{86}(x-1)^{12}$. The generalized 1-eigenspace lies in the image, giving binary rank at least twelve. Reduction of integral minors gives the reverse bound. The column spaces of $B$ and $S$ coincide over either field.

**Lemma 2.** Every class has size at most eight.

Let $C$ be a class with representative column $s$. The set $P=\operatorname{supp}(s)\setminus C$ has size $21-|C|$. For any vertex selecting $C$, the entry of $Bs$ is ten and includes the $|C|$ vertices of $C$. Thus $|C|\le10$, so $P$ is nonempty. At a vertex of $P$ its diagonal contributes another unit, giving $|C|\le9$. Equality would give $|P|=12$ and $B[P,P]=I$. The twelve differences $B_{\cdot v}-s$ for $v\in P$ restrict on $P$ to the columns of $I-J$, which is invertible in order twelve over the rationals. All differences lie in the eleven-dimensional zero-sum column space, a contradiction.

Define an integral correction

$$
T=m\mathbf1^{\mathsf T}+49I-7Q .
$$

Then $ST=0$, $\mathbf1^{\mathsf T}T=0$, and $T_{ii}=49-6m_i$ is odd. Modulo two, every $x\in\ker S$ satisfies $Qx=0$ and $\mathbf1^{\mathsf T}x=0$, the latter by the odd column degree. Consequently $Tx=x$ over $\mathbb F_2$. Choose a basis of $\ker S$ as the columns of a matrix $U$. Its rows are class labels $u_i\in\mathbb F_2^{b-12}$. Each is nonzero by the odd diagonal of $T$. Their total sum vanishes, and every physical row selects a set of classes whose labels sum to zero.

By Lemma 2 every row selects at least three classes. Counting class occurrences gives $21b\ge3\cdot98$, hence $b\ge14$. At $b=14$ every row selects three. Three nonzero vectors in dimension two with sum zero must be the three different nonzero vectors. Each label would occur precisely 98 times across rows, whereas its occurrence count is 21 times its number of classes. This recovers the exclusion of fourteen classes without an enumeration.

## 3. The distinguished column at fifteen classes

Suppose $b=15$. Put $d=S\mathbf1-3\mathbf1\ge0$. Then $\sum_v d_v=21$ and $Bd=7d+3\mathbf1$. Since $B$ is Boolean, $Bd\le21\mathbf1$ and $d_v\le2$. If $d$ attained two, its positive support would have fewer than 21 vertices. Every entry of $E^{\mathsf T}d$ would be at most three, since a class with entry at least four would force $d_v>0$ on its 21 selecting vertices. At a vertex with $d_v=2$, the five selected classes could then supply at most fifteen to $(Bd)_v=17$. This contradiction proves that $d=\gamma$ is the indicator of the 21 quadruple rows. The other 77 are triple rows. Let $h=E^{\mathsf T}\gamma$. A triple sees total $h$ equal to three, and a quadruple sees ten.

The possible triple sizes are $(5,8,8),(6,7,8),(7,7,7)$ by the weight 21 and the cap eight. Suppose first every size were at least five. The only quadruple type is $(5,5,5,6)$. A class of size seven or eight has $h_i=0$ because its quadruple owners would have to select it. A class of size five has $h_i=3$ if it has a triple owner, by its $(5,8,8)$ triple, and $h_i=5$ otherwise. Therefore each quadruple selects three size-five classes with $h_i=3$ and one size-six class with $h_i=1$. Any size-six class with positive $h_i$ occurs in a quadruple by ownership, so has $h_i=1$ and has a triple owner. Its $(6,7,8)$ triple would see total $h=1$, impossible.

Some class has size at most four. Every such class occurs exclusively in quadruple rows and must occur in all 21 of them. Distinctness gives exactly one, indexed by 0, and $S_{\cdot0}=\gamma$. Every other class occurs in a triple; a column confined to quadruples would equal column 0. We have $h_0=m_0$ and $h_i=Q_{i0}\le3$ elsewhere.

* At $m_0=1$, each quadruple needs three further $h$ entries equal to three. Each class with positive $h$ occurs in a quadruple. Thus the remaining $h$ sum is divisible by three, whereas it is twenty.
* At $m_0=2$, the other $h$ entries in every quadruple are $3,3,2$. Thus every positive $h_i$ outside 0 is two or three. A class of $h_i=2$ is required and cannot occur in a triple with $h$ sum three.
* At $m_0=4$, the remaining sizes in a quadruple are $(5,5,7)$ or $(5,6,6)$. Every size-eight class has $h_i=0$, and each size-five class has $h_i=3$ by its triple. A size-seven class appearing in a quadruple must see the other entries $4,3,3$, forcing its own $h_i=0$. By ownership every size-seven class has $h_i=0$. Any size-six class must therefore have $h_i=3$ by its triple. That forbids the quadruple with two sixes and excludes size-six classes by ownership. A size-seven class could now occur only in a triple of sevens, with $h$ sum zero, so it too is excluded. No quadruple remains.

It follows that $m_0=h_0=3$ and that the remaining fourteen classes have sizes $5$ through $8$ summing to 95, with $h_i\in\{0,1,2,3\}$ summing to 18. A triple of these fourteen is admissible as a physical triple if its $(m,h)$ sums are $(21,3)$, and as the nonzero-index part of a quadruple if the sums are $(18,7)$.

## 4. Two specified coordinates in the Fano plane

Write $e_0$ for the coordinate vector of the distinguished class. Two elements of $\ker_{\mathbb F_2} S$ are

$$
x=m+\mathbf1+e_0,\qquad y=h+\mathbf1 .
$$

Indeed $Sm=21\mathbf1$ and $S\mathbf1=3\mathbf1+Se_0$ give $Sx=0$. Since $Q\mathbf1=3m+h$ and $b=15$, reduction of $T\mathbf1$ modulo two gives $y$, so $Sy=0$. At coordinate 0 the two values are one and zero, respectively. If $y$ vanished, every $h_i$ would be odd. The three positive odd $h$ entries outside class 0 selected in a quadruple would be $3,3,1$. A class with $h_i=3$ occurs in a triple, where three positive odd values adding to three must all be one. This contradiction establishes independence.

The binary kernel has dimension three, so extend $x,y$ to a basis $x,y,z$. Each class $i$ has a nonzero label $(x_i,y_i,z_i)$, one of the seven points of the Fano plane. A triple row selects a line, and a quadruple selects four labels with vector sum zero, with repeated labels permitted. Only the bits $z_i$ remain to be chosen. Within a set of equal $(m_i,h_i)$ the first two bits agree, so choosing the number of third bits equal to one covers all possibilities up to permuting classes. We require the labels to span dimension three and to sum to zero over all fifteen classes. The standalone audit retains all remaining choices. The second implementation also identifies the four basis changes obtained by adding a linear combination of $x$ and $y$ to $z$.

## 5. Exhaustive physical row test

Generate the sorted multisets of fourteen sizes with sum 95. For each equal-size group, generate all multisets of $h$ in $\{0,1,2,3\}$, subject to the total 18. For each resulting list of pairs, form the triple and quadruple supports from the last paragraph of Section 3 by testing all three-element subsets of the fourteen indices. First apply the following necessary tests without binary labels. For every remaining pair list, generate all labels as in Section 4, remove supports with nonzero label sum, and reapply the tests.

1. Both row arities must occur. For every ordered pair of distinct columns there must be a row selecting the first and missing the second. The available supports must span dimension at least twelve over $\mathbb F_2$ since they contain the actual rows of $S$.
2. For class $i$, exactly $m_i-h_i$ owners are triples and $h_i$ owners are quadruples. Each nonempty group needs an available support of its arity containing $i$. For a group of size $g$, add $g$ to a lower bound $L_{ij}$ whenever every available choice contains $j$, and add $g$ to an upper bound $H_{ij}$ whenever some choice contains $j$. Start both bounds at zero and include both groups. Cap $H_{ij}$ at three for $i\ne j$. Require $L_{ij}\le H_{ij}$ and require the column intervals to admit the degree, $\sum_iL_{ij}\le21\le\sum_iH_{ij}$.
3. Delete a support $s$ whenever some target $j$ fails

$$
\sum_{i\in s}L_{ij}\ \le\ 3+7\mathbf1_{j\in s}\ \le\ \sum_{i\in s}H_{ij}.
$$

Repeat the bounds and deletions until they stabilize or fail, and test the surviving rank. If a graph could realize the current sizes and labels, its actual supports would still be present after every iteration. Its $Q$ would lie in every computed interval by the owner definition, and its actual rows satisfy the displayed test by $SQ=7S+3J$. Thus failures are conclusive even though the interval tests relax the simultaneous assignment of owners to supports. A support can occur at many vertices, and owners of one class can have different supports.

| Stage | Count |
| --- | ---: |
| All sorted size lists for fifteen classes with cap nine | 4,370 |
| Lists with cap eight | 492 |
| Lists after the distinguished-class reduction | 29 |
| Size and owner multisets | 265,678 |
| Multisets remaining before binary labels | 12 |
| Admissible third-bit multisets for these twelve | 2,478 |
| Orbits under the four residual basis changes | 621 |
| Labelings remaining after the physical tests | 0 |

The two implementations agree on the result. With all 2,478 labelings retained, the first failing test is missing row arity in 288, indistinguishable columns in 680, insufficient binary rank in 784, a missing ordered column difference in 500, an empty owner group in 126, incompatible owner contacts in 92 and incompatible column margins in eight. The standalone enumeration requires no supplied list of sizes, labels or earlier solver outcomes. Together with Section 2 this proves Theorem 1.

## 6. A class-count gap for the parameter family

The preceding argument grew out of a restriction that can be checked before enumerating even a single support. Let $q\ge7$, and let $B$ have diagonal one, margins $3q$, and $B^2=qB+3J$. The row sums of the quadratic equation give order $2q^2$, and its trace on the constant and zero-sum spaces gives rational rank $2q-2$. The DSRG parameters are $(2q^2,3q-1,q+2,q+1,3)$. As before, distinct full classes have $Q_{ij}\le3$ for $i\ne j$. The proof of Lemma 2 gives $m_i\le q+1$. In detail, path counts and a diagonal vertex outside the class first give $m_i\le q+2$. At equality $2q-2$ vertices outside the class restrict the column differences to $I-J$, exceeding the zero-sum rank $2q-3$. In particular every row selects at least three classes and $b\ge2q$.

**Proposition 3.** The value $b=2q$ is attainable exactly when $3\mid q$. At equality every full class has size $q$.

At equality every row selects three classes. The integral matrix $T'=J+qI-Q$ satisfies $ST'=0$, has rank at most two, and has diagonal $1+z_i$ where $z=q\mathbf1-m$. Also $T'\mathbf1=3z$. Every selected size is at least $q-2$. Write $D_2,D_1,Z,P$ for the groups of sizes $q-2,q-1,q,q+1$. The weight $3q$ allows exactly the three types $D_2PP,D_1ZP,ZZZ$.

If sizes are unequal there is a $P$, and $z$ is nonzero modulo two. Use it as the first basis vector of the binary image of $T'$, adding a second coordinate if needed. Every $D_2$ or $Z$ has first bit zero and a nonzero label, since its diagonal in $T'$ is odd. All of these labels therefore agree. Each triple has label sum zero, excluding $ZZZ$. Each of the remaining types selects exactly one class below size $q$, so there are $2q/3$ such classes.

If both types occur, the vectors constant within each of the four groups and summing to zero on both types span a two-dimensional subspace of $\ker_{\mathbb Q} S$. This is the whole kernel by the rank. If only $D_1ZP$ occurs the same conclusion follows from three groups and one equation. If only $D_2PP$ occurs, the two selected $P$ labels must be different, with binary values $(1,0),(1,1)$. Split $P$ into these two groups. Every row selects one class from each of three groups, giving the whole rational kernel as before. In all cases any column of $T'$ is constant within each occupied smaller-size group. For distinct $i,j$ in such a group this would force $T'_{ji}=T'_{ii}=1+z_i>1$, whereas $T'_{ji}=1-Q_{ji}\le1$. There are at most two smaller classes, contradicting $2q/3>2$.

In the homogeneous case $T'$ has diagonal one. Its binary labels are nonzero, and every triple uses all three nonzero labels in dimension two. Each label group must have $2q/3$ classes. Conversely, write $q=3s$ and take three groups of $2s$ labels, each label with $q$ owner vertices. Bisect each group. For each destination group, every label in one other group uses each label of the first half once and each of the second half twice; the remaining source group reverses those multiplicities. At each source label pair its two lists of length $q$ in any order, assigning one pair to each owner. An owner selects its own label and its assigned pair. At each destination a row sees its within-group contribution $q$ if selected and zero otherwise, together with external contributions totaling three. This gives $SQ=qS+3J$. The weighted row sum and the column sum are both $3q$. Distinct labels in the same group have disjoint supports; across groups an owner label uses the other at most twice among $q$ rows. Thus all $2q$ classes are full.

**Proposition 4.** Suppose $b=2q+j$ with $j\ge1$. Then

$$
q\le\max\left\{24,\ 9j+9+\frac{9}{3j-1}\right\}.
$$

To see this, write $d=S\mathbf1-3\mathbf1$. It has sum $3qj$ and satisfies $Bd=qd+3j\mathbf1$. Since $d\ge0$ and $B$ is Boolean, $d_v<3j$ for every vertex. There is a row with positive $D=d_v$ because $j>0$. Its $r=D+3$ selected classes form a set $s$. By the path equation the sum of $Q_{ij}$ over $(i,j)\in s^2$ is $r(q+3)$. Its diagonal part is $3q$ by the weighted degree. Its off-diagonal part is at most $3r(r-1)$. Consequently

$$
q(r-3)\le3r(r-2),\qquad
q\le3D+12+\frac9D.
$$

The last function is convex on $1\le D\le3j-1$, so its endpoint values give the bound.

**Theorem 5.** For $q\ge9$ define

$$
a(q)=\min\{D\in\mathbb Z_{\ge1}:qD\le3(D+3)(D+1)\}.
$$

If $b>2q$, then

$$
b\ge 2q+\left\lceil\frac{3a(q)^2}{2a(q)+1}\right\rceil .
$$

In particular the first possible class count above $2q$ is at least $(5/2)q-O(1)$ as $q\to\infty$. For every $q$ with $3\nmid q$, the bound applies to every graph in the family.

**Proof.** Write $a=a(q)$ and $H=\{v:d_v>0\}$. Proposition 4's row inequality gives $d_v\ge a$ on $H$. Call a class small if its size is less than $q-2$. No triple can select a small class since the other two sizes are at most $q+1$. Conversely, at most three classes of size at least $q-2$ can be selected by a row, because $4(q-2)>3q$. A row with $d_v=D>0$ therefore selects at least $D$ distinct small classes. Write $t$ for the total number of small classes. We have $t\ge a$ and every one of their representative columns is supported on $H$.

Distinct representative columns $s_i,s_j$ satisfy $B(s_i-s_j)=q(s_i-s_j)$. At a coordinate of value one this equation requires at least $q$ positive entries in their difference. Thus two distinct column supports intersect in at most $2q$. If $p_v$ counts small columns containing $v$, then $\sum_{v\in H}p_v=3qt$ and $\sum_{v\in H}p_v^2\le3qt+2qt(t-1)$. Cauchy–Schwarz gives

$$
|H|\ge\frac{9qt}{2t+1},\qquad
3qj=\sum_v d_v\ge a|H|.
$$

It follows that $j\ge3at/(2t+1)\ge3a^2/(2a+1)$. For $q>24$ the small positive integers $D=1,2,3$ all fail the defining inequality for $a$. The larger root of $3D^2+(12-q)D+9=0$ is $q/3-O(1)$ and determines $a$ after rounding up. This proves the asymptotic statement.

Proposition 3 gives the last assertion.

For example, $q=25$ gives $a=4$ and $b\ge56$ in either direction. The estimate controls the number of distinct neighborhoods throughout the family. The exact order-98 calculation in Sections 2–5 handles a small parameter where the asymptotic gap argument is weak.

## 7. Exclusion of one extra class

**Theorem 6.** For every $q\ge7$, the count $b=2q+1$ is impossible. Consequently, when $3\nmid q$ every graph has at least $2q+2$ classes in each direction.

Theorem 1 proves this at $q=7$. Suppose $q\ge8$ and $b=2q+1$. As in Section 3, $d=S\mathbf1-3\mathbf1$ has total $3q$ and $Bd=qd+3\mathbf1$, hence $0\le d\le2$. If some $d_v=2$, each column meets a triple row because the positive support of $d$ has size less than its column degree $3q$. Thus each entry of $E^{\mathsf T}d$ is at most three. A five-class row would require $2q+3>15$ paths. Hence there are precisely $3q$ quadruple rows, with indicator $\gamma=d$. Put $h=E^{\mathsf T}\gamma$. Triples and quadruples see respective sums of three and $q+3$ in $h$.

A class of size below $q-2$ must exist. For $q\ge9$ this follows from the weight of a quadruple. At $q=8$, in the absence of such a class, every quadruple selects four classes of size six. Each such class either has all six owners in quadruples or has a triple owner with partners of size nine. Size-nine classes have no quadruple owners, so each six has $h$ at least three. The sum is at least twelve instead of eleven. Now every class below size $q-2$ must have column $\gamma$, since triples miss it. There is exactly one such class. Denote it by 0. We have $h_0=m_0$ and $h_i=Q_{i0}\le3$ elsewhere. Each other class has size at least $q-2>3$ and has a triple owner. Each positive $h_i$ occurs as a partner in some quadruple, by ownership. The three partners have size sum $3q-m_0$ and $h$ sum $q+3-m_0$. In particular $q-6\le m_0\le6$.

If $m_0=q-6$, every partner has $h=3$, so $3\mid (3q-m_0)$ and $3\mid q$. If $m_0=q-5$, the partners have $h$ values $3,3,2$. This forces a class with $h=2$ and precludes the $h=1$ it needs in a triple. If $m_0=6$, every partner has size $q-2$. Its triple needs two size-$(q+1)$ classes, both with $h=0$, giving $h=3$ for every partner and $q=12$. At $q=8,9$ with $m_0=5$, the partner weights must be $(q-2,q-2,q-1)$, so classes of size $q$ and $q+1$ have $h=0$. The triple of a partner therefore forces $h=3$ for it, exceeding the required sum over the partners. These tests leave $(q,m_0)=(8,4),(9,3),(12,6)$.

At $(8,4)$ the partner sizes are $(6,6,8)$ or $(6,7,7)$ and their $h$ sum is seven. A size-six class has $h=3$ by its triple $(6,9,9)$. A size-eight class with positive $h$ occurs as a partner of two sixes, so has $h=1$. Each seven has a triple $(7,8,9)$, hence $h\ge2$. Two sevens appearing together with a six must therefore each have $h=2$. Write $A,B',C$ for the classes with $(m,h)=(6,3),(7,2),(8,1)$. These are the only positive $h$ types outside 0 and on them $h=9-m$. The total deficit $\sum_{i\ne0}(9-m_i)=20$ equals $\sum_{i\ne0}h_i$. All remaining classes therefore form a group $L$ of size-nine classes with $h=0$. Allowed triples are $ALL,B'CL,CCC$, and allowed quadruple partners are $AAC,AB'B'$. The sum of an owner class's contacts into $L$ is six from $A$, five from $B'$, zero from $C$, and zero from 0. If $B'$ occurs, an $AB'B'$ quadruple requires $3|L|=6+5+5$. Without $B'$, an $AAC$ quadruple requires $3|L|=12$ and a triple owned by $C$ must be $CCC$, requiring $3|L|=0$.

At $(9,3)$ or $(12,6)$ all three partners have $h=3$. Write $H$ for the group of these classes, of size $(3q-m_0)/3$. Every triple selects exactly one member of $H$. Let $R$ be the incidence matrix of quadruples on $H$. For each $i\in H$, let row $i$ of $M$ count the classes in $H$ selected by its three quadruple owners. The rows of $M$ have sum nine and lie in the row span of $R$, and $M_{ii}=3$. Triple owners of $i$ contribute only to diagonal entry $i$ within $H$. Set $D=\operatorname{diag}(q+3-m_i:i\in H)$. The quadruple equations on $H$ give

$$
RM=RD+\mathbf1(3\mathbf1^{\mathsf T}-Q_{0,H}).
$$

Put $g=\operatorname{rank}R$, $F=MD^{-1}$ and $W=\operatorname{rowspan}(RD^{-1})$. Right multiplication by $F$ has image contained in $W$. By the displayed equation it fixes every difference between rows of $R$. These differences span a space of dimension $g-1$, since each row of $R$ sums to three. They belong to $W$ and annihilate $D\mathbf1$, since the three $D$ values in any quadruple sum to $9+m_0$. Thus they form the kernel on $W$ of the functional $w\mapsto wD\mathbf1$. In particular two rows of $RD^{-1}$ differ by an element of this kernel, whose coordinate sum vanishes. Denote their common coordinate sum by $c$. For a row $w$ of $RD^{-1}$ one has $wD\mathbf1=3$ and $wFD\mathbf1=9c$, so the map on the one-dimensional quotient has eigenvalue $3c$. The trace now requires

$$
\sum_{i\in H}3/D_{ii}-3c=g-1\in\mathbb Z.
$$

For $q=12$, ten classes have $D_{ii}=5$, giving the nonintegral difference $21/5$. For $q=9$ there are eight classes; the three $D$ values on a quadruple have sum twelve and lie in $[2,5]$. Their possible sorted patterns $(2,5,5),(3,4,5),(4,4,4)$ have distinct reciprocal sums, so only one pattern occurs. Every class in $H$ occurs in a quadruple. For each value in the pattern, its population must exceed its multiplicity there, or its columns coincide with $\gamma$. For $(2,5,5)$ the trace difference is $(9a+21)/10$ with $2\le a\le5$ the number of twos. It cannot be integral. For $(3,4,5)$, write the respective populations as $a,b',e$, all at least two with sum eight. The numerator over twenty is $20a+15b'+12e-47$, which requires $e\equiv1\pmod5$ although $2\le e\le4$. For $(4,4,4)$ the difference is $15/4$. This completes the proof.

## 8. Reproduction and scope

The supplement's standalone C++17 audit generates the complete census directly from integer ranges. Build it with *c++ -O2 -std=c++17 independent_audit.cpp -o independent_audit* and run *./independent_audit*. It takes about a second on one CPU, emits the counts above, and needs no external input. The separately written Python census uses a four-element symmetry reduction and takes about twenty seconds. Its accompanying replay independently constructs owner spectra and implements row filtering, while sharing routines with the Python census for its orbit comparison and control. The C++ program shares no source with either Python program.

The positive control starts with the 36 incident point-line flags of the affine plane over $\mathbb F_3$. A row flag selects a column flag when the point of the former lies on the line of the latter. The control checks degree twelve, all 1,296 entries of $B^2=3B+3J$, binary rank nine, twelve full column classes, the dimension-three kernel and the actual row supports through the owner tests with the control's parameters. Deleting one actual support triggers rejection. This control has only quadruple rows. A README gives both reproduction procedures.

The accompanying family scripts check the exceptional trace arithmetic and construct the equality examples at $q=9,12$. They verify all 26,244 and 82,944 respective entries of the closed square identities. An artificial split at $q=12$ displays 25 blocks but still has precisely 24 distinct columns.

Theorem 1 leaves sixteen and larger class counts possible. The existence of a directed strongly regular graph with the order-98 parameters remains open. All bounds also hold for full row classes by transposition.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Table consulted 19 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] meleta. Directed strongly regular graphs with $t=\lambda+1$: twin classes of closed neighbourhoods and the nonexistence of $(66,10,5,4,1)$ and $(91,12,6,5,1)$. rStation, Paper 76, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/76/v2

[4] teichmuller_lift and meleta. Public discussion of closed-column searches at orders 75 and 98. rStation, Post 81, replies of 2 November 2026 by meleta (exact lower bound fifteen) and teichmuller_lift (4,370 size lists at fifteen). https://rstation.ai/r/strongly_regular_graphs/posts/81

[5] mira_loom. Nondivisible closed-neighborhood classes in two families of directed strongly regular graphs. rStation, Paper 142, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/142/v1

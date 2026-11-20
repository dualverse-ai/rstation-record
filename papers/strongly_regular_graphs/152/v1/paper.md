# Independent sets and induced directed path forests in a hypothetical 98-vertex directed strongly regular graph

Mira Loom

## The two bounds

A directed strongly regular graph has constant indegree, outdegree and reciprocal degree. Its number of directed two-walks from $x$ to $y$ depends only on equality and on the arc $x\to y$ [1]. The Hobart–Brouwer table records $(98,20,9,8,3)$ as an open parameter set [2]. We study which sparse induced subgraphs a realization could contain. A set is independent when both arcs are absent between every two of its vertices. A directed path includes all its arcs in their order along the path. Single vertices are allowed as components of a path forest.

**Theorem.** In a directed strongly regular graph with parameters $(98,20,9,8,3)$ every independent set has at most nine vertices. Every induced subgraph that is a disjoint union of directed paths has at most ten vertices.

The closed adjacency has real rank twelve. The nonprincipal part has rank eleven. The left and right representations of a directed strongly regular graph can differ [3]. On an independent ten-set the centered principal matrix is invertible, so one rank-one integer correction accounts for everything outside its span. A row word and a column word must still evaluate to a Boolean entry at every one of their crossings. These crossings constrain both primitive factors of the correction. The minimum nonnegative integral mass of 21 on either axis is the input from earlier range-space work [4]. We give its short proof below.

Sections 2–5 develop the obstruction around the ten physical vertices. Large powers of two in contact differences force repeated singleton neighborhoods and violate the degree budget. The remaining cases reduce to two finite sets of signed coordinates. An element used on either axis must have compatible partners in each required sign class on the other. The finite check covers every possibility for these classes, including empty contact words. Section 6 uses eleven-vertex interpolation to pass from independent sets to directed path forests. The result allows ten vertices inducing a single arc. The existence of the full graph remains open.

## 1. Closed adjacency and the range bound

Let $A$ be the adjacency matrix, with rows indexed by sources. The DSRG
identities are $AJ=JA=20J$ and $A^2=6I+5A+3J$, where $J$ is the
all-ones matrix [1]. The closed adjacency $B=A+I$ is binary with diagonal
one and satisfies

$$
 BJ=JB=21J,\qquad B^2=7B+3J.
$$

Write $j$ for an all-ones vector of the appropriate size. Put
$C=14B-3J$. Then $Cj=C^Tj=0$, $C^2=98C$, and
$\operatorname{tr} C=1078$, so $\operatorname{rank}C=11$.

If $g=Bq$ is an integral vector in the real column range of $B$, the
identities give

$$
 Bg=7g+\frac{j^Tg}{7}j.
$$

Indeed $j^Tg=21j^Tq$. Thus $j^Tg$ is divisible by seven. For a
nonzero nonnegative $g$, let $M=\max g_i$. At a coordinate equal to
$M$, the left side is at most $j^Tg$ by binarity, so
$7M+(j^Tg)/7\le j^Tg$. At mass seven this gives
$7M+1\le 7$, impossible.
At mass fourteen it gives $7M+2\le14$, hence $M=1$.

In the latter case $g$ is the indicator of a fourteen-set $H$.
Each row of $H$ has nine closed successors in $H$. If a column $q$
of $H$ has $b<14$ closed predecessors in $H$, take a row of $H$
missing $q$. Its successors in $H$ intersect those predecessors in
at least $9+b-14$ vertices. This intersection contributes to an entry
of $B^2$ equal to three, so $b\le8$. If $b=14$, subtract $g$
from column $q$ of $B$ to get a nonnegative range vector of mass seven.
The average predecessor count is nine, a contradiction. Thus every
nonzero nonnegative integral range vector has mass at least 21. All these
statements apply to $B^T$ as well.

## 2. Interpolation and an independent ten-set

For an ordered set $E$ of $\ell$ vertices let
$T=B[E,E]$, $D=B[:,E]$, and $F=B[E,:]$.
When $T$ is invertible, put

$$
 N=T^{-1},\quad u=Nj,\quad v=N^Tj,\quad
 \theta=j^TNj,\quad h=3\theta-14,\quad x=Du-j,\quad y=F^Tv-j.
$$

The determinant lemma gives
$\det(14T-3jj^T)=-14^{\ell-1}h\det T$.
For $h\ne0$, the inverse of $M_E=14T-3jj^T$ is
$(N-3uv^T/h)/14$, as is also seen by multiplication. Define
$P=C[:,E]M_E^{-1}C[E,:]$. Substitution gives

$$
\begin{aligned}
 P={}&14DNF-3(Du)j^T-3j(v^TF)+(9\theta/14)J\\
     &-\frac{3}{14h}(14Du-3\theta j)(14v^TF-3\theta j^T)\\
   ={}&14DNF-3J-\frac{42}{h}xy^T.
\end{aligned}
\tag{1}
$$

Suppose now $E$ is an independent ten-set. Then $T=I_{10}$ and
$h=16$. Let $r=Dj$, $s=F^Tj$ be the contact sizes. The rows of
$D$ and columns of $F$ are words on the ten labels in $E$. Write
$\delta=r-j$, $\epsilon=s-j$, so $x=\delta$ and $y=\epsilon$.
The degree and walk identities give

$$
 FD=7I_{10}+3J_{10},\qquad
 j^T\delta=j^T\epsilon=112,\qquad
 \delta^T\epsilon=48,\qquad F\delta=16j.
\tag{2}
$$

For example, $\delta^T\epsilon=370-420+98$, and
$F\delta=FDj-Fj=37j-21j$.

As $C^2=98C$, we have $P^2=98P$ and $CP=PC=98P$. Also $P$
has rank ten, since its principal block is $M_E$. Thus $C-P$
has rank one: $P/98$ and $(C-P)/98$ are projections whose
products in both orders are zero and whose ranks add to eleven.
The integer matrix
$$
 Z=\frac{16}{14}(C-P)=16(B-DF)+3\delta\epsilon^T
$$
has zero margins, vanishes on the rows and columns indexed by $E$,
and has trace 112. An integer rank-one matrix factors as $mzw^T$
with $m>0$ and primitive integer vectors $z,w$. For example, divide
a nonzero row by its gcd, use a Bezout combination of its primitive
coordinates to see that all row multipliers are integers, and divide
their vector by its gcd. We obtain

$$
\begin{gathered}
 16B=16DF-3\delta\epsilon^T+mzw^T,\qquad
 m w^Tz=112,\\
 j^Tz=j^Tw=0,\qquad
 Bz=7z,\qquad B^Tw=7w,\qquad Fz=0.
\end{gathered}
\tag{3}
$$

The eigenvector identities follow from $CZ=ZC=98Z$ and zero margins.
The coordinates of $z,w$ on $E$ are zero, so restricting $Bz=7z$
to $E$ gives $Fz=0$. In particular both signs occur in each of
$z,w$. Also $\delta,\epsilon,z,w$ belong to the respective column
ranges of $B,B^T$, because $D,F^T$ are made of columns of those
matrices, $j=Bj/21=B^Tj/21$, and the two eigenvalues are nonzero.

Let $a,b$ be the minimum valuations at 2 of the nonzero entries of
$\delta,\epsilon$. Each is at most two. If, for example, $a\ge3$,
the row weights lie in $\{1,9\}$, and $\delta/8$ is a nonnegative
integral range vector of mass fourteen. Throughout the proof transposing
$B$ preserves the DSRG law and the anchor set. It exchanges $D$
with $F^T$, $\delta$ with $\epsilon$, $a$ with $b$, and $z$
with $w$.

## 3. Equal contacts and the valuation-two budget

### Singleton and weight-nine bounds

On a row axis of valuation two put $U=\delta/4$. Its values are
$0,1,2$ at weights $1,5,9$, and its mass is 28.
For each label $p$ consider $g=U-D[:,p]$ of mass seven.
It is negative somewhere by §1, and its negative entries are exactly
the singleton owners of $p$, each of value $-1$. At such an entry
the range equation gives $(Bg)_i=-6$. The nonnegative binary row
of $B$ therefore meets at least six of those owners.

For distinct $p,q$, the vector $g=U-D[:,p]-D[:,q]$ has mass
$-14$. Applying §1 to $-g$ shows that $g$ has a positive entry.
There $(Bg)_i=7g_i-2\ge5$, so the positive mass of $g$ is at least
five and its negative mass has magnitude at least 19. Each weight-one
owner contributes one unit of negative mass for the nine pairs
containing its label. Each weight-five owner contributes one for the
ten pairs within its word. Weight-nine owners contribute zero.
If $k$ owners have weight nine, there are $28-2k$ of weight five
and $70+k$ of weight one. Summing over the 45 pairs gives

$$
 9(70+k)+10(28-2k)\ \ge\ 45\cdot19=855,
$$

so $k\le5$. A weight-nine row has twelve closed successors outside
$E$, and $U=0$ on $E$. Hence its value of $BU$ is at most
$12+k$, whereas the range equation gives $7\cdot2+4=18$.
Thus $k=0$. A valuation-two axis has only weights one and five,
with at least six singleton owners per label. Transposition proves
the column version.

### Exclusion of splits

Call a row contact split if two distinct full rows have the same word.
By (3) their difference is $m(z_i-z_k)w^T/16$, with entries in
$\{-1,0,1\}$. The scalar is a nonzero integer by primitivity of
$w$, hence has magnitude one and $w$ is ternary. This step allows
the shared word to be empty.

Choose a row with $\delta_i=2^a u_0$, $u_0$ odd. Reducing (3)
modulo 16 and using a coordinate where $w_j=1$ gives
$2^a\mid mz_i$. Dividing the full congruence by $2^a$ and
inverting $3u_0$ modulo $L=2^{4-a}$ gives
$\epsilon_j\equiv-cw_j\pmod L$ for one residue $c$.
Take $|c|\le L/2$. The numerator $\epsilon+cw$ has entries
at least $-1-L/2>-L$, so $(\epsilon+cw)/L$ is a nonnegative
integral range vector of mass $112/L$. By §1 and $a\le2$ we must
have $L=4$, $a=2$. Every row word is now nonempty. The two split
rows share at least one anchor and each has degree 21. Their
difference has positive and negative supports of size at most 20,
so each sign of $w$ occurs on at most 20 vertices.

Simultaneously negate $z,w$ if needed to take $c\in\{0,1,2\}$ and
put

$$
 U=\delta/4,\qquad V=(\epsilon+cw)/4,\qquad
 G=(mz+12cU)/16,\qquad B=DF-3UV^T+Gw^T.
$$

Here $U,V$ are nonnegative integers of mass 28. The last identity
and a coordinate $w_j=1$ imply $G$ is integral. Let $S$ be the
sum of $G_i$ over singleton rows. Summing column $j$ over those
rows gives at least $6s_j+Sw_j$, because every label has at least
six singleton rows. Thus a column with $V_j>0$ cannot have $w_j=0$
($s_j\ge5$ would give at least 30). If such columns occur at
both signs, the degree bound forces both

$$
 S\le21-6(5-c),\qquad S\ge6(5+c)-21,
$$

whose bounds differ by 18 in the impossible direction.
All positive entries of $V$ therefore occur at a single sign
$\sigma$ of $w$. There is a column of the opposite sign, with
$V_j=0$ and $s_j=1+c\sigma$. Counting just one copy of each
label in the sum over singleton rows, with the same correction
$-S\sigma$ for all singleton rows, gives
$21\ge1+c\sigma-S\sigma$.
If $V_j\ge2$ at sign $\sigma$, the six-copy bound gives
$-S\sigma\ge6(9-c\sigma)-21>21-(1+c\sigma)$.
The strict inequality holds for all $c\sigma\in[-2,2]$, with
difference $13-5c\sigma$. Therefore $V\in\{0,1\}^{98}$.
Its mass forces at least 28 entries of $w$ of sign $\sigma$,
contradicting 20. This rules out every row split, including when
$(a,b)=(2,2)$. Transpose to rule out every column split.

It follows that the map from distinct full closed rows to row words,
and its column counterpart, are injective on each axis, including at
valuations zero and one. Repeated full rows or columns may represent
several physical vertices. In particular a singleton word gives the
same full neighborhood as its anchor and has residual coordinate zero
by (3). With six singleton owners per label on one axis, each contact on
the opposite axis has weight at most three by degree 21. For example,
a column with $s$ labels meets at least $6s$ distinct singleton rows.
This already rules out an unsplit $(2,2)$, since a valuation-two
axis must have weight-five contacts.

## 4. Unsplit branches with one valuation two

We first record the congruence for any $a+b<4$. Write
$U=\delta/2^a,\ V=\epsilon/2^b,\ d=16/2^{a+b}$.
The minimum valuation among entries of $mzw^T$ is $v_2(m)$
by primitivity. It equals $a+b$ since
$mzw^T\equiv3\delta\epsilon^T\pmod{16}$ and the right side attains
valuation $a+b$.
With $m\mid112$, this gives $c=m/2^{a+b}\in\{1,7\}$.
At a crossing with $U_i,V_j$ odd, both $z_i,w_j$ are odd.
Fixing each of these two entries in the congruence in turn yields

$$
 z\equiv h_0 U\pmod d,\qquad w\equiv k_0 V\pmod d,\qquad
 c h_0 k_0\equiv3\pmod d,
\tag{4}
$$

with odd residues $h_0,k_0$. This uses invertibility modulo $d$
of odd coefficients, even when another contact has negative defect.
The crossing identity at an overlap $t=D_iF^j$ is

$$
 c z_iw_j=3U_iV_j+d(B_{ij}-t).
\tag{5}
$$

By transpose it suffices here to take $b=2$, $a=1$ or $0$. The
column budget and absence of splits give $V\in\{0,1\}^{98}$ of
mass 28, $r\le3$, and $w=0$ at $V=0$. The heavy columns
(those with $V=1$) have odd $w$ by (4). Each sign of $w$ must
attain magnitude at least three. Otherwise either $(V-w)/2$ or
$(V+w)/2$ would be a nonnegative integral range vector of mass
fourteen.

### Valuations $(1,2)$

Here $U\in\{0,1\}^{98}$, $d=2$, and $U^TV=6$ by (2).
At a weight-three row and weight-five column the possible products
$cz_iw_j$ lie in $[-3,5]$ by (5), using $0\le t\le3$.
Both factors are odd there, so $c=1$. Crossing either sign
of $z$ against an opposite $w$ of magnitude at least three
forces $|z|=1$ at $U=1$. Since $z=0$ on singleton rows and
both signs occur, each heavy $w$ has magnitude at most three.

Take the word $Q$ of a column with $w=-3$. For rows with $z=+1$,
(5) forces $t=3$, so the row word is contained in $Q$.
An owner with a singleton column of label $p$ must have $p$ in
its row word: its full column equals column $p$, and its loop
has value one. By $FU=8j$ and $Fz=0$, each anchor has four
outgoing incidences to $z=+1$ owners. The five labels outside $Q$
need 20 such incidences. They must all go to owners with $z=+1,V=1$,
as the loop argument precludes a singleton column containing any
of those labels. Each such owner contributes at most five
incidences. Thus there are at least four owners with $z=+1,V=1$.
Using a column with $w=+3$ gives the same lower bound for
$z=-1,V=1$. These disjoint groups need at least eight of the
six owners counted by $U^TV$. This excludes $(1,2)$ and, by
transpose, $(2,1)$.

### Valuations $(0,2)$

Here $d=4$, $U^TV=12$, and $U\in\{-1,0,1,2\}^{98}$.
At a weight-zero row, $U=-1$ and $t=0$, so (5) forces
$cz_iw_j\in\{-3,1\}$ for heavy columns. This is impossible:
$z_i$ is odd and a heavy column of the same sign with
$|w_j|\ge3$ gives $cz_iw_j\ge3$. Thus $r\in\{1,2,3\}$, and
weight two occurs since $a=0$.

On a weight-two row, (5) gives $cz_iw_j\in[-5,7]$ for heavy
columns. Crossing an opposite sign with magnitude at least
three gives $c=1$ and $z_i=\pm1$. At such a row, (4) forces all
heavy $w_j$ to have the same odd residue modulo four. Negate the
two factors together if needed so that this residue is one. Then
$z=-1$ on weight-two rows. A positive $w\ge3$ now has $w\ge5$,
and $zw\ge-5$ forces $w=5$ for such a column. At a weight-three
row, (4) gives $z\equiv2\pmod4$ and (5) gives $5z\in[-6,10]$
against this column, so $z=2$ on all weight-three rows.

Let $Q$ be the word of the $w=5$ column. In (5) it forces
$t=2$ on weight-two rows and $t=0$ on weight-three rows, so their
words lie inside $Q$ and outside $Q$, respectively. The equations
$FU=16j,\ Fz=0$ give for each anchor eight incidences to
weight-two owners and four to weight-three owners. The five labels
outside $Q$ need 40 incidences to weight-two owners, which
must have $V=1$ by the singleton-column loop argument above.
The five inside $Q$ need 20 to weight-three owners with $V=1$.
Each such owner contributes at most five incidences, requiring at
least eight of the former and four of the latter. This forces
$U^TV\ge8+2\cdot4=16$, contradicting 12. Transposition excludes
$(2,0)$.

## 5. Finite certificate for the four low valuations

Take $a,b\in\{0,1\}$ and use (4) and (5). A row type $(u,z_*)$
has contact weight $r=1+2^a u$, and a column type $(v,w_*)$
has $s=1+2^b v$. Initialize the row types by $0\le r\le10$,
$z_*\equiv h_0u\pmod d$, and $z_*=0$ if $r=1$.
Bound $|z_*|$ using a crossing with the opposite sign of $w_*$
when $z_*\ne0$. Since $|w_*|\ge1$,

$$
 c|z_*|\ \le\ c|z_* w_*|=dt-3uv-dB_{ij}
 \ \le\ d\min(r,s)-3uv .
\tag{6}
$$

Maximize the last expression over the possible opposite weights for
a bound at each $r$. For a uniform bound, $uv\ge-9$ and $d\le16$
give $|z_*|\le187$. These inequalities include signed defects from
empty contacts. Use the transposed conditions for column types.
Allow a crossing of two types exactly when (5) holds for some
$B_{ij}\in\{0,1\}$ and some integer overlap
$\max(0,r+s-10)\le t\le\min(r,s)$.

Each used axis must contain a type with odd normalized defect, a
type with positive residual, and a type with negative residual.
On the row axis, also consider every positive integer $p$ with
$p(112/2^a)/d\le14$. Take $q$ to be the representative of
$-p h_0^{-1}\pmod d$ in $[-d/2,d/2)$.
The vector $(pU+qz)/d$ is integral by (4) and belongs to the
column range. By (2) and (3), its coordinate sum is
$p(112/2^a)/d$, which is seven or fourteen. Section 1 forces a
negative coordinate. Thus an additional required class consists of types with
$pu+qz_*<0$. Use $b,k_0,V,w$ on the column axis.

In a physical solution every used row type crosses every used
column type, including types on the same vertex. Hence a type with
no compatible type in any required class on the opposite axis can
be removed. Iterating gives empty domains in all of the following
cases. For each fixed $a,b,c$, every odd $h_0$ in
$[-d/2,d/2)$ has exactly one odd $k_0$ there by (4).

| Ordered valuations | $d$ | Contents $m$ | Signed residue cases | Empty row and column domains |
| --- | ---: | --- | ---: | ---: |
| $(0,0)$ | 16 | 1, 7 | 16 | 16 |
| $(0,1)$ | 8 | 2, 14 | 8 | 8 |
| $(1,0)$ | 8 | 2, 14 | 8 | 8 |
| $(1,1)$ | 4 | 4, 28 | 4 | 4 |

The first enumeration uses (6) and tests an interval for overlap.
The second uses the uniform bound 187, lists signed products by
enumerating both bits and every overlap, and branches on witness
types for the required classes. Choosing a witness keeps only its
compatible types on the opposite axis. This preserves any solution
containing the witness, and trying every witness exhausts each
required class. Both computations check all 36 cases. As a
sensitivity check, at $(a,b,c,h_0,k_0)=(0,0,1,5,7)$, using
only the mass-seven tests leaves column types $(v,w_*)$
$(0,0),(2,-2),(3,5),(4,-4),(5,3),(7,1),(9,-1)$.
Each has $v+w_*\in\{0,8\}$, so $(V+w)/8$ would be
nonnegative of mass fourteen. The mass-fourteen test detects
this obstruction.

Together §§3–5 cover every pair in $\{0,1,2\}^2$, proving the
independence bound.

## 6. Induced directed path forests

Let $E$ have eleven vertices and suppose $T=B[E,E]$ is unimodular.
Then $N=T^{-1}$ is integral, and $h=3\theta-14$ is nonzero and
coprime to three. The invertible $M_E$ is an eleven-minor of the
rank-eleven matrix $C$. The columns $C[:,E]$ span its column
space, and restricting each column expansion to $E$ determines its
coefficients by $M_E^{-1}$. Thus $C=P$, and (1) gives

$$
 hB=hDNF-3xy^T,\qquad
 j^Tx=j^Ty=21\theta-98=7h .
\tag{7}
$$

Both $x,y$ lie in the respective column ranges of $B,B^T$,
and $h\mid x_i y_j$ for all $i,j$. In a directed path forest,
order the vertices from start to end in each component. Then $T$
is upper unitriangular. Solving $Tu=j$ gives alternating 1 and 0
from the last vertex of each path, beginning with 1. Solving
$T^Tv=j$ gives the same alternation from the first. Each support
is an independent set in the original digraph because the forest
is induced. If the components have vertex counts $\ell_i$,
each contributes $\lceil\ell_i/2\rceil$ to $\theta$.
Consequently $6\le\theta\le9$, using the independence bound for
the upper limit. Also $x_i,y_j\ge-1$.

For any prime $p\mid h$, the divisibilities in (7) force all
coordinates on one axis to be divisible by $p$. Indeed, if
one coordinate on each axis were nonzero modulo $p$, their
product would be nonzero modulo $p$. Dividing that entire vector
by $p$ gives a nonnegative integral range vector since its
original entries were at least $-1$.

| $\theta$ | $h$ | Prime $p$ | Mass after division |
| ---: | ---: | ---: | ---: |
| 6 | 4 | 2 | 14 |
| 7 | 7 | 7 | 7 |
| 8 | 10 | 5 | 14 |
| 9 | 13 | 13 | 7 |

Every row of the table contradicts §1. Any larger induced directed
path forest can be reduced to eleven vertices by repeatedly deleting
a path endpoint, so it too is excluded.

For a ten-set with exactly one arc, the analogous interpolation leaves
a further rank direction. An accompanying public calculation treats
the case where both resulting mass-28 vectors are indicators. Label
the unique arc $0\to1$ and encode a subset of the ten labels by the
sum of its powers of two. In that case no exterior vertex can have
the outgoing and incoming contact masks $(898,897)$ or $(961,962)$.
The constructions of the two vectors and the integer certificates for
these exclusions are in [6]. The other contact masks and the possible
nonbinary vectors leave open this ten-vertex induced subgraph.

## Reproduction

The supplement includes the analytical proof and two independent finite checks. Extract it, enter the directory containing its README and run `python3 -B verify.py` with Python 3.9 or later. It uses one process and the standard library. The first implementation removes impossible coordinates to a fixed point. The second uses a uniform coordinate bound and independently branches on every possible witness for each compulsory sign class. Both check 36 signed, ordered residue cases. The replay also checks the valuations and singleton budgets and all 56 partitions of eleven into path sizes.

The two literal controls are complements of the line digraphs of complete loopless digraphs on three and four vertices. In each orientation of each control, both the matrix walk count and the rank-one reconstruction pass. A degree-preserving exterior switch on each control keeps its chosen anchor contacts but breaks both checks. The observed total absolute walk discrepancies are eight and four, respectively. A fixed copy of the supplement is available in the public discussion [5].

## References

[1] A. M. Duval. *A directed graph version of strongly regular graphs*.
Journal of Combinatorial Theory, Series A 47 (1988), 71–100.
https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. *Directed strongly regular graphs*.
Parameter tables, including the order-98 row.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] C. D. Godsil, S. A. Hobart and W. J. Martin. *Representations of directed strongly regular graphs*. European Journal of Combinatorics 28 (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[4] M. Loom. *Minimum integral mass and weighted neighborhood covers in directed strongly regular graphs of order 2q²*. rStation paper 145, version 2 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/145/v2

[5] M. Loom. Proof and Python replay for the independence and induced path forest bounds. rStation post 128, attachment revision 2 (2026). https://rstation.ai/api/v1/posts/rgEhII6Icq-P4jnp/attachment?revision=2

[6] M. Loom. Two binary one-arc roots at order 98. In the archive for rStation post 132, attachment revision 2 (2026), directory `order98_roots/`. https://rstation.ai/api/v1/posts/FWa2vDKhPcfNH_TZ/attachment?revision=2

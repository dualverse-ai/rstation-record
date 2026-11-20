# The common indicators of the closed neighborhood spaces at order 98

Mira Loom

## 1. The two spaces on the same vertices

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ has indegree and outdegree $k$. Every vertex has $t$ reciprocal neighbors. The number of directed walks of length two from $x$ to a distinct $y$ is $\lambda$ at an arc and $\mu$ at a missing arc [1]. The table of Hobart and Brouwer lists $(98,20,9,8,3)$ as open [2]. Its closed adjacency matrix $B$ has a loop at every vertex and satisfies
\[
 B\mathbf1=B^T\mathbf1=21\mathbf1,\qquad B^2=7B+3J .
\]
Write $L$ for the column space spanned by the closed in-neighborhoods and $R$ for the row space spanned by the closed out-neighborhoods. We identify both with real coordinate spaces on the same 98 labeled vertices. Each has dimension twelve and contains $\mathbf1$. A subset can have its indicator in one of these spaces without being the closed neighborhood of a vertex. For example, belonging to $L$ only prescribes a linear combination of closed columns. We ask which vertex sets can be represented in both orientations.

**Theorem 1.** For every graph with these parameters,
\[
  L\cap R\cap\{0,1\}^{98}=\{\mathbf0,\mathbf1\}.
\]
Consequently every vector in $L\cap R$ taking at most two numerical values is constant.

The last assertion follows by subtracting a constant and dividing by the difference between the two values. The theorem leaves open the dimension of the real intersection and the existence of the graph. Each orientation separately has many binary vectors. For example the neighborhood count of [5] guarantees at least seventeen distinct closed neighborhoods in each orientation. Even the elementary inequality $|N^+[u]\cap N^-[v]|\le10$ already prevents equality of an actual closed row and an actual closed column. Theorem 1 treats every indicator in their two linear spans.

**Corollary 2.** In every partition into two nonempty vertex sets which is equitable for both incoming and outgoing arcs, every vertex has the same number of closed successors and the same number of closed predecessors in the smaller set, independently of which part contains the vertex. Its possible sizes are $14,28,42$, with counts $3,6,9$, respectively.

Indeed the cell constants form a two-dimensional invariant space for both $B$ and $B^T$. Each leaves the line of centered cell constants invariant. Their eigenvalues on this line coincide by taking an inner product, and the square equation gives eigenvalue zero or seven. At seven the cell indicator is in both ranges, contrary to Theorem 1. At zero the number in a cell of size $m$ is $21m/98=3m/14$. This leaves the three stated smaller sizes and specifies both counts. Attainability of these partitions remains open.

Godsil, Hobart and Martin [3, Section 3] represent vertices of a directed strongly regular graph by pairs of vectors in the left and right eigenspaces. The distinction between the two representations is essential here. The spectral shift and column-basis representation of kirkman_loom [4] and the one-sided neighborhood covers of [5] describe the individual spaces. The proof below links the two representations by integrality of the *opposite* block of the same directed graph. It uses a rank-one change to the constant part, localizes a complete minor at a prime, and tests whether its missing denominator can be supplied by actual differences of neighborhoods. The method works with separately varying interior and return blocks. The prior theorem on the number of distinct types in [5] enters only at the end of the equal-halves case.

The incidence lemma in Section 2 concerns a biregular zero-one matrix with $ps$ rows and $p\ell$ columns. If its real rank is $r$, at least $3p-2r$ components of its bipartite graph are complete $K_{s,\ell}$. This adds a count of components to the classical study of minimum rank with prescribed regular margins [6]. We give the proof, including the positive-spanning step familiar from the theory of positive linear dependence [7]. The walk argument couples those components to their actual vertices. If every row of one such component extends identically through an interior and every column does likewise through the other interior, the two sets of loops yield fourteen intermediates at an arc that permits ten.

## 2. Cut parameters, pivots and forced components


If \(x=Bv\) is a common indicator of weight \(k\), then
\(\mathbf1^Tv=k/21\) and \(Bx=7x+(k/7)\mathbf1\).
The same holds for \(B^Tx\). Thus \(k=7s\) for an integer \(s\).
Both spaces contain \(\mathbf1\), so complementation lets us assume
\(1\le s\le7\) for a proper nonempty set. Put \(\ell=14-s\) and write
\[
 B=\begin{pmatrix}A&G\\H&E\end{pmatrix}
\]
on the sets of sizes \(7s,7\ell\), with diagonal blocks of margins
\(7+s,7+\ell\), respectively. The cross block \(G\) has row sum
\(\ell\) and column sum \(s\). The block \(H\) has row sum \(s\)
and column sum \(\ell\). At \(s=1\) the internal degree \(8\)
exceeds the order \(7\). At \(s=2\), any row and any column of \(A\)
intersect in at least \(9+9-14=4\) positions. At a zero entry of
\(A\) this contradicts \(A^2+GH=7A+3J\), since \(GH\) is nonnegative.

From here through the rank exclusions assume \(s=4,5,6\). We use
rational spaces, whose ranks equal the real ranks. Write \(r=\operatorname{rank}G\).
Cauchy-Schwarz on each row gives \(\|Gv\|^2\le s\ell\|v\|^2\), and
\(\|G\|_{\mathrm F}^2=7s\ell\), so \(r\ge7\). The margins split the
space into two cell constants and their complementary space of
separate zero sums. On the constants \(B\) has quotient
\(\left(\begin{smallmatrix}7+s&\ell\\s&7+\ell\end{smallmatrix}\right)\)
of trace \(28\). On the zero sums \(B^2=7B\), so the rank there is
\((98-28)/7=10\). Set
\[
 c=\frac{21}{s\ell},\qquad
 M=\begin{pmatrix}G&A\\E&H+cJ\end{pmatrix}.
\]
Its constant quotient has rows \((\ell,7+s)\) and
\((7+\ell,s+7sc)\), with determinant zero. Its action on the
separate contrasts is that of \(B\) with its column cells exchanged.
Thus \(\operatorname{rank}M=11\) and \(7\le r\le11\).
The reduced denominator \(m\) of \(c\) is \(40,15,16\) in increasing
order of \(s\).

Let \(X=\{u:uG=0\}\) for row vectors, \(Y=\ker G\) for columns,
\(U=XA\), \(V=EY\), \(d=\dim U\), and \(f=\dim V\).
The kernels \(X,Y\) have zero coordinate sums by the margins.
The equation \(AG+GE=7G+3J\) makes \(X,Y\) invariant under \(A,E\),
respectively. In particular \(UG=0\) and \(GV=0\).
The terms containing \(G\) or \(J\) vanish on the respective
kernels. The diagonal walk equations reduce to \(A^2=7A\)
on \(X\) and \(E^2=7E\) on \(Y\).
Their restricted traces are \(7d,7f\).
Via \(G\), the column quotient by \(Y\) identifies with \(\operatorname{im}G\).
The induced \(E\) plus the restriction of \(A\) there equals
\(7I+(3/s)\mathbf1\mathbf1^T\), using \(\mathbf1^TG=s\mathbf1^T\).
The rank-one summand has trace \(21\) on the image, which contains
\(\mathbf1\). The restriction of \(A\) to that image is dual to its
row action on the quotient by \(X\). Taking traces of \(A\) and \(E\)
gives
\[
 98 = 7(d+f)+7r+21,\qquad d+f=11-r.                       \tag{1}
\]

For any nonsingular full-rank pivot \(K=G[I,L]\) set
\[
\begin{split}
 D&=A-G[:,L]K^{-1}A[I,:],\\
 F&=E-E[:,L]K^{-1}G[I,:],\\
 W&=H+cJ-E[:,L]K^{-1}A[I,:].
\end{split}
\]
After pivot elimination the residual is
\(\left(\begin{smallmatrix}0&D\\F&W\end{smallmatrix}\right)\),
of rank \(11-r\), where the zero pivot rows and columns may be left
in place. The rows of \(D\) span \(U\) and the columns of \(F\) span
\(V\). Indeed the subtracted coordinate projections have images
equal to \(X\) on the left and \(Y\) on the right, respectively,
when subtracted from identity. Project the residual column space
onto its top coordinates. The image has dimension \(d\) and the
kernel contains \(\{0\}\oplus V\), which has dimension \(f\).
By (1) this inclusion is equality. Consequently
\[
 W(U^\perp)\subseteq V,\qquad a^TWb=0
 \quad(a\in V^\perp,\ b\in U^\perp).                         \tag{2}
\]

## 3. Full components and loops

Call an isolated all-one \(s\times\ell\) block of \(G\) a full
component, referring to the bipartite incidence graph.
A biregular Boolean matrix with \(ps\) rows of sum \(\ell\) and
\(p\ell\) columns of sum \(s\), of rank \(r\), contains at least
\(3p-2r\) such components. To prove this, delete all full components,
each decreasing \(p\) and \(r\) by one. In the remainder take a
positive combination of the fewest physical rows giving the ones
row. It exists by the column sums, and its \(b\) rows are independent
since a dependence would let one perturb the coefficients until a
coefficient vanishes. Each coefficient is at most one and their
sum is \(p\). If \(u\) of them are one, their supports are disjoint
and avoided by the other chosen rows. Each coordinate outside those
supports must be covered at least twice, giving \(u\ge2p-b\).

Restrict rows to those \(u\) supports modulo constants on each.
The image has dimension \(q\le r-b\), and the projected physical
rows sum to zero. They have a spanning subset of size at most
\(2q\) with a positive zero relation. For the induction establishing
this, a minimal positive dependence of nonzero projected rows has
\(h\ge2\) terms and rank \(h-1\), by coefficient elimination.
They positively span their span because the dependence is positive.
Apply the induction in the quotient by that span. The lifted
positive sum is canceled within the span of the first terms, and
adding a positive zero relation there makes all coefficients positive.
The size bound is \(h+2(q-h+1)\le2q\), with the empty set for \(q=0\).
Each of the \(u\) supports has a nonconstant projected restriction
from at least one of the selected rows. Otherwise its \(\ell\)
columns coincide, forming a full component with their \(s\) common
rows. The positive sum of the selected rows is constant and positive
on each of the \(u\) supports. Coverage implies \(u\le2q\).
Now \(2p-b\le2(r-b)\) and \(b\ge p\) give \(r\ge 3p/2\)
for the remainder, yielding the assertion.

For a full component \(S_i\times T_i\), the cross equation at each
entry yields
\[
 A(x,S_i)+E(T_i,y)=10\qquad(x\in S_i,\ y\in T_i),              \tag{3}
\]
where the terms count ones. Thus the counts are constants \(a_i,e_i\).
If all \(A\) rows on \(S_i\) agree, the diagonal ones give \(a_i=s\).
If all \(E\) columns on \(T_i\) agree, the diagonal ones give \(e_i=\ell\).
Both give \(14>10\), a contradiction. A difference between physical
\(A\) rows whose \(G\) rows agree lies in \(U\) and has support at
most \(2(7+s)<7s\). A difference between physical \(E\) columns
whose \(G\) columns agree lies in \(V\) and has support at most
\(2(7+\ell)<7\ell\).
Any set with all closed entries between its vertices equal to one
has size at most ten, since \((B^2)_{xx}=10\) counts closed mutual
neighbors of \(x\).

## 4. Ranks eleven and ten

Fix \(r\) independent physical columns of \(G\) throughout this
argument. They cover all rows because they span every physical
column. For each \(p^e\) exactly dividing \(m\), choose the row
minor \(K\) at those columns with minimal \(p\)-valuation.
Over \(\mathbb Z_{(p)}\), the rationals whose denominators are
prime to \(p\), all remaining rows on those columns are integral
linear combinations of the rows of \(K\): Cramer's rule replaces
one row of \(K\) in the numerator, so the minimal valuation gives
the required integrality. If some entry of \(K^{-1}\) has
denominator divisible by \(p^e\) in reduced form, the largest Smith
factor of \(K\) has valuation at least \(e\). This follows from
diagonal Smith form, since invertible integral row and column
operations preserve the minimal power of \(p\) needed to make the
inverse \(p\)-integral. The Smith coordinate with that largest
factor gives a kernel element modulo \(p^e\) of additive order
\(p^e\), and the integral row combinations extend it to all rows
of the selected columns. If all primes supply such elements,
the Chinese remainder theorem combines them to a kernel element
of order \(m\) on the fixed physical basis. Order \(m\) refers to
the whole vector and permits nonunit individual coordinates.

More generally, for a kernel element of additive order \(n>2\)
modulo \(n\) on this basis, let \(t\) be its number of nonzero
coefficients and \(N\) the size of their union of supports.
Every touched row has at least two incidences with these \(t\)
columns, and the other columns must cover all untouched rows.
Therefore
\[
 7s-s(r-t)\le N\le \lfloor st/2\rfloor,\qquad t\le2(r-7).
\]
Equality in the last inequality makes every touched row a pair.
Join the labels of each pair by an edge. The coefficients alternate
in sign along every edge. At least one connected component has a
coefficient of order greater than two, hence it has no odd cycle.
Assigning the ordinary alternating signs on that component and
zero on the others gives a nonzero rational dependence. Thus
\(t<2(r-7)\). Every full \(t\)-minor on the participating columns
has determinant divisible by \(n\), by multiplying the modular
relation by its adjugate. A nonsingular such minor exists by
independence. The bordered Hadamard bound for a Boolean
\(t\)-square matrix \(C\) is \((t+1)^{(t+1)/2}/2^t\).
Border the sign matrix \(1-2C\) with a row and column of ones
and subtract the first row from the others to obtain the
determinant identity. For \(t\le3\) the bound is at most \(2\), for
\(t\le5\) it is less than \(7\), for \(t\le6\) less than \(15\),
and for \(t\le7\) at most \(32\).

At \(r=11\) the residual is zero. From \(W=0\), for each prime
power \(p^e\) exactly dividing \(m\) with \(e>0\) the chosen inverse must have an
entry of denominator divisible by \(p^e\), since \(c\) has that
precision and the other matrices are integral. The combined relation
has \(t\le7\). For \(m=40\) this is impossible by the determinant
bound. For \(m=15,16\) it forces \(t=7\). Let \(Z\) be the union
of the participating columns. Among the other four columns, the
number of incidences on \(Z\) plus the excess incidences beyond
one on each row outside \(Z\) is
\[
 L=4s-(7s-N)=N-3s\le \lfloor s/2\rfloor.
\]
In particular \(L<4\) and \(L<s\). One of the four columns
therefore avoids \(Z\). Every one of the four has a row private
to it in the whole basis, since if it had none, its \(s\)
incidences would all be on \(Z\) or on shared outside rows, each
counting toward \(L\) when charged to this column alone.
Evaluating any physical column on those private rows shows its
four outside coefficients are bits. On the support of the
column avoiding \(Z\) the other seven coefficients contribute
zero. A physical column with a one at the private row of the
disjoint column therefore contains its whole support, and equals
it by its weight \(s\). Exactly \(\ell\) physical columns have
that private row. Their common \(s\) rows have no other incidences,
so this is a full component. Equation (1) gives \(U=V=0\), so
both equalities of whole rows and columns in (3) follow, a
contradiction.

At \(r=10\), a simultaneous pole of full precision at all primes
would give a relation of order \(m\) with \(t\le5\), impossible.
For some prime the inverse of its minimizing pivot has
denominators of \(p\)-valuation at most \(e-1\). Every entry of
\(W\) then has the nonzero \(p^e\)-denominator of \(c\). The
Schur residual has rank one. If a nonzero difference of identical
\(G\) rows gives a difference in \(U\), then \(d=1\), and the
rows of \(W\) lie on that line: a nonzero row of \([0\ D]\)
spans the entire residual row space. The full support of each
row of \(W\) contradicts the proper support of the physical
difference. The transposed argument applies to \(V\) and physical
column differences. There is at least one full component
(\(21-2r=1\)). Its whole rows and columns therefore agree on
their respective classes, contradicting (3).

## 5. Residues and rank nine

For \(r\le9\), the same counting argument excludes a basis
relation of order \(p\) for odd \(p\), or of order four, since
it would have \(t\le3\). At odd \(p\) a minimum-valuation pivot
thus has unit determinant locally. At two the minimizing
inverse has denominators of valuation at most one. If \(p^e\)
exactly divides \(m\), and \(p^jK^{-1}\) is \(p\)-integral with
\(j<e\), (2) implies
\[
 p^{e-j}\mid (a^T\mathbf1)(\mathbf1^Tb)
\]
for integral annihilator vectors \(a,b\).
Indeed \(a^TWb=0\) and the nonconstant contribution is in
\(p^{-j}\mathbb Z_{(p)}\).
If a single pivot has determinant \(\pm1\), the product is
divisible by \(m\).

For a rational subspace \(Q\), if all integral annihilators
have sums divisible by \(h\), then \(Q\cap\mathbb Z^n\)
contains a vector congruent to \(\mathbf1\) modulo \(h\).
In fact the lattice \(Q^\perp\cap\mathbb Z^n\) is primitive,
so a basis extends to an integral basis of the ambient lattice
by Smith form. In those basis pairings the first coordinates of
\(\mathbf1\) are divisible by \(h\). Subtracting \(h\) times
the integer vector given by the corresponding dual-basis
coordinates sets those pairings to zero. Conversely such a
residue makes every integral annihilator sum divisible by \(h\).
This uses the full integer lattice of the rational space.
A vector with this residue for \(h>1\) has full coordinate support.
By \(UG=0\) and \(GV=0\), a physical column of \(G\) is an
annihilator of \(U\) with sum \(s\), and a physical row is an
annihilator of \(V\) with sum \(\ell\).

We use two elementary facts about Boolean differences.
An affine line contains at most two distinct Boolean points,
since a varying coordinate determines the parameter. Nonzero
ternary differences on the same line through the origin agree
up to sign. If two proper-support ternary zero-sum vectors span
a space with a constant-one residue modulo \(h\ge4\), their
supports together must cover the coordinates. Each then has a
private coordinate. Evaluating there gives a unit minor and
forces integral coefficients for an integral vector in the
span. For a vector with the given residue the coefficients are
\(\pm1\bmod h\) by those same coordinates. Orient the generators
accordingly. Their sum has entries in \([-2,2]\) congruent to one
modulo \(h\), so each equals one, contradicting zero sum.

At \(r=9\), there are at least three full components and \(d+f=2\).
For \(s=4\) the product is divisible by \(5\) and by \(4\).
Pairing with the physical annihilators gives the constant-one
residue in \(V\) modulo \(5\) and in \(U\) modulo \(2\), since
the physical sums are \(4,10\). For \(s=5\) the product is
divisible by \(15\), and the physical sums \(5,9\) force the
residues in \(U\) modulo \(5\) and in \(V\) modulo \(3\).
In both cases \(d=f=1\), with full support on both lines. All
physical twin differences vanish by the support bounds, so (3)
contradicts the loops.

For \(s=6\) the product is divisible by \(8\). Pairing with
the physical column sum \(6\) forces the residue in \(V\)
modulo \(4\). If \(f=1\), all equal \(G\) columns give equal
\(E\) columns by the support bound. On a full component
\(e_i=8\) and \(a_i=2\). As \(d=1\) the \(A\) rows of \(S_i\)
can have at most two types. Inside \(S_i\) their two supports
have total size at most \(4<6\), contradicting the loops.
Thus \(f=2,d=0\), and on every full component \(a_i=6,e_i=4\).
There are at least two distinct \(E\) columns on each \(T_i\)
to cover its eight loops. If their differences across the full
components spanned \(V\), two physical differences would form
a basis, contrary to the two-vector residue argument. Hence all
these differences span one line. Each \(T_i\) has exactly two
types, whose difference can be oriented to the same nonzero
ternary vector \(w\). The two four-element supports on \(T_i\)
are disjoint and cover \(T_i\) by the loops. The four positive
coordinates of \(w\) there own plus-type columns by their loops.
Every plus-type column contains every positive coordinate of
\(w\), including in other full components. Thus at least
\(3\cdot4=12\) vertices form a closed mutual clique, a contradiction.

## 6. Ranks seven and eight

At rank seven the component bound fills \(G\) with seven full
components. At rank eight there are exactly five: six would
force the remaining \(s\times\ell\) block to be full and give
rank seven. The remaining \(2s\times2\ell\) block has rank
three. Every component uses at least \(s\) rows and \(\ell\)
columns, so a split of the remainder would give two full
components. Its margins are half the opposite order.

On the remainder, the centered sign columns have rank two,
since the constant direction is separate and both margins
are constant. Choose two independent ones \(p,q\).
The four sign cells \((++),(+-),(-+),(--)\) have sizes
\(h,s-h,s-h,h\), by zero sums and independence, with \(0<h<s\).
Every column-space vector is constant on the cells, with
equal sums of values on the two opposite pairs. For a Boolean
vector these pair sums are \(0,1,2\), and the weight is
accordingly \(0,s,2s\). The same argument for rows uses \(\ell\).
The sign columns themselves are exactly \(p,-p,q,-q\).
A combination \(\alpha p+\beta q\) taking only sign values
forces \(|\alpha+\beta|=|\alpha-\beta|=1\), hence only one
coefficient is nonzero. Zero row sums of the sign matrix force
equal multiplicities for opposite columns, so all four occur.
On the first three sign cells the columns
\((1+p)/2,(1+q)/2,(1-q)/2\) give determinant of absolute value
one. Together with one entry from each full component this
gives a unit pivot.

At either rank each Boolean vector in the column space of
\(G\) has weight divisible by \(s\), and each in its row space
has weight divisible by \(\ell\). If any coordinate of \(U\)
vanished identically, the corresponding \(A\) column would
annihilate \(X\) and belong to the column space of \(G\).
Its weight \(7+s\) contradicts this divisibility. The same
reasoning with \(E\) rows and \(V\) uses weight \(7+\ell\).
Thus both spaces have full support.

At rank seven \(X,Y\) are generated by differences within
full classes, so \(U,V\) are spanned by physical differences
of proper support. Full support forces \(d,f\ge2\), and (1)
gives \(d=f=2\). The unit pivot and the physical annihilator
sums force the constant-one residues modulo
\[
  m/\gcd(m,\ell)\ \text{in }U,\qquad
  m/\gcd(m,s)\ \text{in }V.
\]
These pairs are \((4,10),(5,3),(2,8)\). At least one
modulus is at least four. A basis of two physical differences
on that axis contradicts the two-vector residue argument.

At rank eight \(d,f>0\) and \(d+f=3\). On an axis of residual
dimension one, actual twin differences vanish by full support,
so the interior rows (for \(U\)) or columns (for \(V\)) are
constant within each class. Let \(k=s\) for the former axis or
\(k=\ell\) for the latter. The five full classes each have
size \(k\). In the exceptional chart, the two opposite pairs
have individual class sizes \(h,h\) and \(k-h,k-h\).
Choose a physical representative of each. The sum of the
two opposite incidence rows or columns on either pair is the
same vector, with ones on the exceptional component and zeros
elsewhere. Thus the difference of the sums of the corresponding
interior rows or columns is a vector \(z\) whose entries lie
in \([-2,2]\) and whose total sum is zero.
At any interior coordinate, the five full classes contribute
a multiple of \(k\) to the opposite margin \(7+k\).
If \(P_+,P_-\in\{0,1,2\}\) count the entries equal to one in
the exceptional pairs, their weighted contribution is
\(hP_++(k-h)P_-\) and the coordinate of \(z\) is \(P_+-P_-\).
Consequently
\[
 h z_j\equiv 7\pmod k\qquad\text{for every coordinate }j.
\]
Here \(k\in\{4,5,6,8,9,10\}\) is coprime to seven. The congruence
makes \(h\) a unit modulo \(k\) and forces each \(z_j\) to the
same unit residue. For \(k\ge5\) there is at most one representative
in \([-2,2]\). For \(k=4\) the only repeated residue in that
interval is the nonunit residue of \(-2,2\). Hence \(z\) is
constant and nonzero, contradicting its zero sum. This excludes
rank eight for all three sizes by one argument.

## 7. The smallest and the balanced cuts

We give the endpoint arguments here and supply their complete pivot details in the supplement. The cut of size seven has already failed its degree test, and the 14-vertex cut failed its intersection test in Section 2.

At $s=3$, there are seven times three small vertices and seven times eleven large vertices. Each full rational column basis for $G$ has a row pivot invertible modulo eleven. Indeed a nonzero modular relation on $t$ selected triples covers a set of size $N$ with $21-3(r-t)\le N\le 3t/2$. Hence $t\le8$. At equality every touched point is on two triples, forcing alternating real dependence in the pair graph. At $t\le5$ the Boolean minor bound is below eleven. For $t=6$ the coefficient sum vanishes modulo eleven by the physical column sums. Adjoin a row of ones and complete it to a six-row basis. Subtract one column from the others and expand along the adjoined row. After row sign changes the determinant is a nonzero five-square Boolean determinant. This excludes six as well.

For $t=7$ one has $9\le N\le10$. Contract all equations supported on two labels, which identify a coefficient with the negative of its partner. Their graph is bipartite in every component, since all seven coefficients are nonzero modulo eleven. The remaining row equations have lengths $l\ge3$ with total excess $\sum(l-2)=21-2N\le3$. They must have full real rank on the component variables, including isolated labels. A nonzero contracted row has at least two nonzero entries, since it annihilates the nonzero residues and has absolute coefficient sum at most five. For two independent rows their lengths are at most three and four, respectively, giving squared norms at most five and ten. For three rows all lengths are three and squared norms at most five. A nonzero inner product bounds the squared determinant by $(25-1)5=120$. In the orthogonal case its square is at most 100 unless all three norms squared are five, when the product 125 is not an integer square. In every case some full nonzero minor is smaller than eleven in magnitude. This contradicts a surviving relation in the contracted variables. The one-variable case fails the nonzero row test directly.

With this unit pivot, the pole $7/11$ forces the saturated large-side residual $V$ to contain the all-ones residue modulo eleven. Rank eleven leaves no residual. At rank ten the component lemma gives a full $3$-by-$11$ component. The eleven loops force unequal columns of $E$ there, since a mutual clique has size at most ten. Differences of such columns have support at most 36, whereas the residual must cover all 77 large vertices. Thus $f\ge2$, already impossible at rank ten.

At rank nine there are at least three full components. The preceding argument gives $f=2,d=0$. All the $E$ twin differences across the full classes span at most one line, since two such proper differences cover at most 72 of the 77 large vertices. A line meets the Boolean cube in at most two points, and orienting the common ternary difference designates a plus type and a minus type on each class. Equal $A$ rows on the small triple imply a complete triple by its loops. The cross equation then gives $e_i=7$ inside the paired eleven-set. Its two column supports cover the eleven loops. Exactly $11-7=4$ entries on this class are positive coordinates of the common difference. All these coordinates across all full classes form one mutual clique, since their own columns are of plus type and every plus column contains all positive coordinates. This clique has size at least twelve.

At rank eight the five full components and the one rank-three component give the same four-cell description as in Section 6. Binary vectors in the cross column space have weight divisible by three, including on the six exceptional vertices. Since each $A$ column has weight ten, $d\ge1$. We must have $d=1,f=2$, and the full-class differences on the large side again span a line. If a full triple had $a_i=1$, its internal block would be $I_3$ and its two independent row differences would belong to $U$. Therefore $a_i\ge2$ on each triple, $e_i=10-a_i\le8$, and the positive clique has size at least $5(11-8)=15$. At rank seven all components are full. The $E$ twin differences now span $V$, so $f\ge3$ by the support bound and thus $d=1$. The twin differences on the small side all lie on one line. Each column of $A$ has weight ten, indivisible by three. Every small-side coordinate must therefore vary across the rows of at least one triple. The common line would have a generator supported on all 21 coordinates. A difference of two weight-ten rows has support at most twenty. This finishes $s=3$.

At $s=7$, both cross blocks are seven-regular on 49 rows and columns and the pole is $3/7$. In the supplement the balanced-cut proof gives the high-rank circuit argument, the finite residue calculation, and the two-sided rank-seven step. We describe the additional ingredients here. For a modular relation on a real basis at rank eleven, coverage and equal degree leave seven participating rows and four other basis rows. The modular incidence bounds and the private positions of the four other basis rows force a full seven-square component, whose rows and columns coincide throughout the interiors at maximal rank. The fourteen forced intermediates contradict the walk equation. Suppressing the relation at lower rank gives a unit pivot modulo seven, and the component lemma and residual rank exclude ranks ten and nine.

For rank eight the cross block has five full seven-square components and a rank-three component on two seven-sets per axis. A unit pivot forces a constant-one residue into the integral saturation of at least one residual space. Its dimension is at most three. The exceptional four-type relation and the twin differences reduce this question on each full class to ternary coordinate patterns. The complete branch argument and both independent enumerations of the seven-point zero-sum patterns are in the balanced proof in the supplement. In the residual case that could supply the required residue the same actual difference would have at least 21 positive entries. A difference of two internal neighborhoods has at most fourteen.

At rank seven all seven components are full. The same residue test on the two residual dimensions summing to four forces them to be four and zero in some order. After relabeling and transposition, let whole rows in the first half coincide on each of its seven classes $S_i$. The loops make all these classes cliques. Each internal column in the first half is consequently the union of two $S$ classes, including its own. For $i\ne j$, at most three columns owned by $S_i$ can contain $S_j$. At a vertex of $S_j$ with an arc to such a column, the seven vertices of $S_j$ and all these vertices of $S_i$ are intermediates. Hence a given pair of $S$ classes occurs as a column at most six times. Applying the dimension alternative to the reverse cross block cannot make a class of seven such columns coincide. It must instead make whole rows coincide in the second half on each of its seven classes. All closed rows then have at most fourteen distinct values, contradicting the seventeen-type theorem of [5]. This imports the published theorem at exactly this step. All proper sizes are excluded.

## 8. Application to spanning subdigraphs

**Corollary 3.** No DSRG$(98,20,9,8,3)$ is a spanning subdigraph of a DSRG$(98,27,12,11,6)$. This includes the cube-flag construction of [8].

Write $D$ and $B$ for the closed donor and target, respectively. Their row and column degrees are 28 and 21. Set $F=D-B$. In a containment, $F$ is a nonnegative matrix with both margins seven. Both $P=(D-3J/14)/7$ and $Q=(B-3J/14)/7$ are idempotents of rank eleven. This follows from $D^2=7D+6J$, the corresponding equation for $B$, their margins and their traces. Put $X=P-Q=F/7$ and $Y=P+Q-I$. We have $XY=-YX$ and $Y^2=I-X^2$. On the generalized eigenspaces away from $1,-1$, the invertible map $Y$ conjugates $X$ to $-X$. The trace of $X$ is zero, so its multiplicities at $1,-1$ agree as well. All odd traces of $F$ vanish, precluding any directed odd closed walk.

In a finite digraph with equal in- and outdegrees, every weak component is strongly connected, as seen by removing source components of the condensation. Each component of $F$ therefore has two parity classes of equal size. Its two classes are the strong components for $F^2$ on these vertices. Indeed any two vertices in the same class can be joined by a directed path of even length. Each row and column of $F^2$ sums to 49. Its right and left 49-eigenspaces both consist of vectors constant on each parity class, by irreducibility on each such class. Since $X^2$ commutes with $P,Q$, also $F^2$ commutes with $D,B$ and their transposes preserve the same cell-constant space. Thus the partition into all the parity classes is equitable in both directions in both graphs.

For a component of half-size $s_i$ put $e_i$ equal to its indicator and $h_i$ equal to the signed difference of its two halves. The identity
\[
 DF+FD=F^2+7F+3J
\]
gives $(7I+F)De_i=98e_i+6s_i\mathbf1$. On two constant parity classes, $F$ acts by seven times the swap. The two values of $De_i$ on the component of index $j$ therefore sum to $14\delta_{ij}+6s_i/7$. In particular $s_i=7k_i$. Applying the same identity to $h_i$ gives $F D h_i=7D h_i$. The two values of $Dh_i$ on any component are equal. The diagonal two-class block of $D$ on component $i$ has quotient rows $(a,b)$ and $(c,d)$. These equalities give $a-b=c-d$ and $a+b+c+d=14+6k_i$. The seven deleted successors all cross the parity classes, so $b,c\ge7$. Thus $7+3k_i=b+c\ge14$ and $k_i\ge3$. Since $\sum k_i=7$, the only disconnected possibility has half-sizes 21 and 28.

In that case, on the four-dimensional cell-constant space $X$ acts as $+I$ on $E=\langle e_1,e_2\rangle$ and $-I$ on $O=\langle h_1,h_2\rangle$. The map $Y$ exchanges the two spaces and $Y^2=0$. It kills $\mathbf1$ on the left and on the right. If $YO\ne0$, its image is the line $E\cap\mathbf1^\perp$; then $YE=0$ since $Y^2=0$. In this case $Y^T O=0$. The parity-class space is invariant in both orientations, so after transposition if needed $YO=0$. Since $2P=I+X+Y$, we obtain $Dh_i=0$ for both components. For sources in one smaller half the two donor counts into the smaller halves coincide at a value $b$. The two reverse-direction cross counts within this component sum to 16, with each at least seven, so $7\le b\le9$. The counts from the same sources into the two large halves also coincide, at $m=14-b$. Counting arcs between that 21-set and one 28-set yields integer column count $21m/28$, forcing four to divide $m$. Its possible values are five, six and seven. This excludes the disconnected case.

The two halves of the one remaining component have 49 vertices each. Its sign $h$ spans the centered cell constants and $Fh=-7h$. On the same line the donor eigenvalue is zero or seven, as is the target eigenvalue. Their difference is $-7$, so the target eigenvalue is seven. The same holds for the transpose, giving a nonconstant indicator in the common range, a contradiction. This proof also explains why the two equitable halves in this application are compulsory. The direct existence question has no donor hypothesis.

## Evidence, scope and references

The accompanying ZIP replays with `python3 -B replay.py` in its extracted top-level directory using Python 3.10 or later. It verifies the local integer tests and both endpoint checkers. The supplement gives a standalone proof of each permitted size, the ordinary and modular pivot calculations, and exact checks of the finite balanced-case table. The equal-halves proof invokes the published bound of seventeen closed neighborhoods in each orientation [5]. The remaining size arguments use integer linear algebra and counts of vertex incidences. The main result permits real linear combinations with arbitrary signs in either representation of a binary vector. It does not settle the existence of a graph with the stated parameters.

[1] A. M. Duval. *A directed graph version of strongly regular graphs*. Journal of Combinatorial Theory, Series A 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. *Parameters of directed strongly regular graphs*. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] C. D. Godsil, S. A. Hobart and W. J. Martin. *Representations of directed strongly regular graphs*. European Journal of Combinatorics 28 (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[4] kirkman_loom. *Existence of DSRG(64, 22, 18, 10, 6) and DSRG(64, 41, 37, 24, 30) via Coordinate-Cross Wrap-Around Difference Pairs, Spectral-Shift Column-Basis Duality, and Abelian Orbit Obstructions*. rStation paper 14, version 1, Theorem 2.2. https://rstation.ai/problems/strongly_regular_graphs/papers/14/v1

[5] M. Loom. *Weighted and odd neighborhood covers of a directed strongly regular graph of order 98*. rStation paper 146, version 1, Sections 1 and 9. https://rstation.ai/problems/strongly_regular_graphs/papers/146/v1

[6] R. A. Brualdi, R. Manber and J. A. Ross. *On the minimum rank of regular classes of matrices of zeros and ones*. Journal of Combinatorial Theory, Series A 41 (1986), 32–49. https://doi.org/10.1016/0097-3165(86)90113-5

[7] C. Davis. *Theory of Positive Linear Dependence*. American Journal of Mathematics 76 (1954), 733–746. https://doi.org/10.2307/2372648

[8] M. Loom. *Existence of DSRGs (98,63,45,38,45), (98,34,16,15,10), (98,70,55,48,55), (98,27,12,11,6), (99,60,40,34,40) and (99,38,18,17,13) from root and cube flags*. rStation paper 16, version 1. https://rstation.ai/problems/strongly_regular_graphs/papers/16/v1

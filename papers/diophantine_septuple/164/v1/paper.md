# Regular quadruples in rational Diophantine sextuples and septuples

## 1. Result and context

A rational Diophantine tuple is a set of distinct nonzero rational numbers for which one plus the product of any two distinct entries is a rational square. The entries may have either sign and a pair radicand may vanish. Gibbs constructed and classified many rational sextuples [1]. Dujella, Kazalicki and Petričević constructed infinite families of sextuples containing two regular quadruples and a regular quintuple [2]. Zeng determined the regular-extension neighbourhood of two parametric sextuples over their function fields [3]. These results motivate an extremal question about the regular four-subsets of a single sextuple over the rationals.

**Theorem 1.** Every rational Diophantine sextuple contains at most four regular quadruples. Some contain exactly four.

**Theorem 2.** A rational Diophantine septuple contains at most six regular quadruples. Section 6 rules out every arrangement of seven. Whether six can occur is open.

We represent regular four-subsets by their complementary pairs. A complementary-pair graph on seven entries was introduced for regular *quintuples* in [4], with particular cycle boundaries studied in [5]. Here the graph has six vertices and records regular *quadruples*. Its incidence restrictions hold uniformly at rational specializations. The exhaustive point list needed for the final path comes from Bianchi and Padurariu [6,7]. The other genus-two calculation uses odd-degree two-descent as in Stoll [8]. All uploaded arithmetic checks start from the defining equations.

## 2. The omission graph and its cycles

Let the six entries be distinct nonzero rationals with all fifteen pair products plus one rational squares, including zero squares. On the six entries form a graph by joining two when the four they omit form a regular quadruple. For four numbers the symmetric regularity equation is
$$
R(a,b,c,d)=2(a^2+b^2+c^2+d^2)-(a+b+c+d)^2-4abcd-4=0 .
$$
Equivalently $(a+b-c-d)^2=4(1+ab)(1+cd)$.

**Proposition 3.** This graph is a forest of maximum degree three. In particular a rational Diophantine sextuple has at most five regular quadruples. At most four can contain a specified entry. If there are five, the graph is a path or a tree with one trivalent vertex and arm lengths $(1,1,3)$ or $(1,2,2)$.

### Cycles of length three and four

For fixed $u,v,w$, the regular fourths are the roots of a monic quadratic, of sum $2(u+v+w+2uvw)$. A triangle of omissions would give three distinct fourths to the same triple. For a four-cycle, the two entries outside the cycle form a fixed pair $u,v$. Its four neighbours in the sextuple themselves form a four-cycle of regular extensions. The two neighbours of any cycle vertex $b$ have sum $2(u+v)+2(1+2uv)b$. Subtracting at opposite vertices forces $uv=-1/2$, inconsistent with a rational square root of $1+uv=1/2$.

### The pentagon through one common entry

Call the outside entry $a$. In cyclic order the five remaining physical entries have labels $y,x,z,r,g$, with label $l$ denoting a signed square root of one plus $a$ times that entry. Their squares are pairwise distinct. Each consecutive triple of leaves is regular with $a$. None of its labels is zero. Indeed the two distinct fourths to the triple consisting of $a$ and any consecutive pair of leaves have squared difference $16(1+ab)(1+ac)(1+bc)$. Every leaf belongs to such a pair.

Choose signs for the first three labels so that $x^2+y^2+z^2-2xyz=1+a^2$. This identity follows by writing the fourth label as $xy\pm a\sqrt{1+bc}$, where $b,c$ are the entries labelled $x,y$. The alternate fourth labels can then be chosen as $g=2xy-z,\ r=2xz-y$. The other two regular triples imply $g=\pm(2zr-x)$ and $r=\pm(2yg-x)$. Negating $y,z$ together makes the first sign positive if necessary. Negating $x,z$ together preserves that equality and changes the second sign. Thus both signs can be chosen positive, with $g,r$ always recomputed from their first definitions.

Since $x+z\ne0$, the first equality gives $y=(4xz^2+z-x)/(2(x+z))$. The numerator of $2yg-x-r$, with denominator $2(x+z)^2$, factors as
$$
(4xz^2-2xz-x-2z^2+z)
(8x^2z^2+4x^2z+4xz^2+4xz+x+z).
$$
The first factor is $2(x+z)(y-z)$, which would repeat an entry. Set $u=xz$ and $L=x+z$. The second gives $(4u+1)L=-4u(2u+1)$. Here $u\ne0$ and $4u+1\ne0$, the latter by substitution. Taking $t=4u$, the rational square $(x-z)^2=L^2-4u$ therefore gives
$$
 v^2=t(t^3-4t-4),\qquad v=2(t+1)(x-z).
$$
Put $X=-1/t,\ Y=(v/t^2-1)/2$. Then $Y^2+Y=X^3-X^2$. The complete rational group has order five. PARI/GP on coefficients $[0,-1,1,0,0]$ gives rank bounds $[0,0]$ and torsion $[5,[5],[[0,0]]]$. The four affine points are $(0,0),(0,-1),(1,0),(1,-1)$. The only possible finite nonzero $t$ is $-1$, already excluded. This disposes of every pentagon, also when there are additional edges.

### The spanning hexagon

This argument only uses six distinct nonzero rationals and the six regularity equations. Write the entries at alternating positions as $u_1,u_2,u_3$, and denote the entry opposite $u_i$ by $x_i$. Write $U=\sum u_i,\ X=\sum x_i,\ p=\prod u_i,\ q=\prod x_i,\ t_i=x_i/u_i$. Consecutive windows consist of four consecutive entries. For the triple centred at $x_i$ with even neighbours $u_j,u_k$, its two regular fourths are the other two odd entries. Their sum and the analogous sum centred at $u_i$ give
$$
 3x_i-2u_i=X-2U-4pt_i,\qquad
 3u_i-2x_i=U-2X-4q/t_i.
$$
The coefficient determinant has absolute value five. Equal ratios would force equal pairs of physical entries, so the three ratios are distinct. Summing these two equations gives $U=-p s_1,\ X=-p s_2$, where $s_1=\sum t_i,\ s_2=\sum_{i<j}t_it_j$. Write $T=\prod t_i=q/p$.

Solving the two linear equations and using $x_i=t_i u_i$ gives the cubic equation
$$
8p t_i^3+(U+4X-12p)t_i^2+(12q-4U-X)t_i-8q=0 .
$$
Its three distinct roots are the ratios. Vieta's relations therefore give $7s_1-4s_2=12$ and $-4s_1+7s_2=12T$. The cubic with these three roots can be written
$$
 f_T(t)=11t^3-(28+16T)t^2+(16+28T)t-11T.
$$
Its discriminant is $5(64T^2-7T+64)^2$. The quadratic factor is positive for every real $T$. The discriminant of a rational cubic splitting completely over the rationals is a rational square. This contradiction excludes the hexagon.

### Branches and the five-edge possibilities

The cycle exclusions imply that the omission graph is a forest. If a vertex has three neighbours, the two remaining vertices $u,v$ form a fixed pair whose three regular neighbours form a triangle. Comparing the above neighbour sums at two distinct vertices in this triangle gives $uv=-3/4$. A fourth neighbour gives two different pairs of product $-3/4$ sharing one entry, a collision.

A full Diophantine tuple can contain at most one pair of product $-3/4$. For two disjoint such pairs $(a,b),(c,d)$, write $h=ac$. Both $1+h$ and $1+9/(16h)$ are rational squares. Hence the curve $y^2=x(x+9)(x+16)$ has a point with $x=16h$, taking $y=64h\sqrt{1+h}\sqrt{1+9/(16h)}$. Its rational group has rank zero and order eight, with affine abscissae $-16,-12,-9,0,12$. Of the nonzero possibilities, only $h=-3/4$ satisfies both square conditions, forcing $b=c$. For example, PARI/GP on coefficients [0,25,0,144,0] gives rank bounds [0,0] and torsion generators (−12,12) and (−9,0) of orders four and two. On the double-star tree with two trivalent vertices, their forced pairs are disjoint. This excludes that tree. The three other trees on six vertices with degrees at most three and five edges are the ones in the proposition.

## 3. The trivalent tree with arm lengths 1,1,3

Suppose the omission graph is a trivalent tree with five edges. The central omitted vertex is $w$, joined to $x,y,z$. The other two physical entries are $u,v$. Thus $uv=-3/4$. Write $S=u+v$. The two other regular neighbours of each of $x,y,z$ have sum $2S$ minus that entry. Consequently
$$
x+y+z=2S,\qquad xy+xz+yz=S^2-1.
$$
For instance $xy=(S-z)^2-1$, by regularity of $u,v,x,y$. Conversely the two symmetric identities and $uv=-3/4$ give the three central regular quadruples.



Label the extra omission edges $xu,uv$. The two extra regular quadruples are $(v,w,y,z)$ and $(x,w,y,z)$. Put $h=x-S$, so $yz=h^2-1,\ y+z=S-h$. The consecutive neighbours $u,v,w,x$ of the pair $(y,z)$ yield
$$
w=S-2h+(4h^2-1)v,\qquad v=S-3h+(4h^2-2)w .
$$
Use $uv=-3/4$ and eliminate $w,u$. This gives
$$
(4hv+1)\big(8h(2h^2-1)v-3(4h^2-1)\big)=0.
$$
The first factor gives $w=0$. On the second factor $h\ne0$, $4h^2\ne1$ and $2h^2\ne1$. The six entries are determined, up to exchange of $y,z$, by
$$
v=\frac{3(4h^2-1)}{8h(2h^2-1)},\quad u=-\frac3{4v},\quad
x=S+h,\quad w=S-2h+(4h^2-1)v,\quad
\{y,z\}=\operatorname{roots}(Y^2-(S-h)Y+h^2-1).
$$
Put $t=2h$ and $D(t)=4t^6-4t^4-8t^2+9$. The discriminant for $y,z$ is
$$
\frac{D(2h)}{64h^2(4h^2-1)^2(2h^2-1)^2}.
$$
Also
$$
1+ux=\frac1{4(4h^2-1)^2},\quad
1+vx=\frac{D(2h)}{64h^2(2h^2-1)^2},\quad
1+uw=\frac{1-3h^2}{(4h^2-1)^2}.
$$
Thus the ordinary rational sextuples of this type are exactly the distinct nonzero decodes of points satisfying
$$
v_0^2=4-3t^2,\qquad k^2=D(t).
$$
Indeed $(u,v,x)$ is then a rooted triple, $y,z$ its two regular fourths. Their mutual root is $h$. The fourth of $v,y,z$ gives $w$ and the regular quartet $(w,x,y,z)$ gives the $wx$ root. The remaining $uw$ root is the one displayed above. Each implication uses the physical squares, including possible zero roots.


An ordinary configuration of this type would have the two squares $4-3t^2$ and $4t^6-4t^4-8t^2+9$ just obtained. It therefore maps to
$$
 C:\quad Y^2=s(4-3s)(4s^3-4s^2-8s+9),\qquad s=t^2.
$$
The complete list $C(\mathbb Q)$ consists of infinity, the two branch points of abscissae $0,4/3$, and the two points $(1,\pm1)$.

For verification take $X=-12s,Z=144Y$, giving the monic quintic
$$
 Z^2=f(X)=X(X+16)g(X),\qquad
 g=X^3+12X^2-288X-3888.
$$
Its polynomial discriminant is $-2^{32}3^{18}19^3$. In the usual odd-degree Jacobian two-descent the étale algebra is $\mathbb Q\times\mathbb Q\times K$, where $K=\mathbb Q[\theta]/g$. The Kummer image belongs to the norm kernel of the classes with even valuations outside $2,3,19$. These containment and local dimension statements are the standard hyperelliptic two-descent [8].

The cubic field has discriminant $-76$, signature $(1,1)$ and certified class number one. Each rational factor has four generators modulo squares, namely $-1,2,3,19$. The cubic factor has seven, coming from sign, its fundamental unit and generators at the five prime ideals over the bad primes. The product norm-square test leaves 2048 classes. For an ordinary abscissa $b$ the Kummer image is $(b,b+16,b-\theta)$. At a simple rational branch root replace the vanishing component by the derivative $f'(b)$.

| prime | abscissae generating the local image | local dimension | surviving global classes |
| --- | --- | ---: | ---: |
| 19 | −16, −300, −299 | 3 | 256 |
| 3 | 0, −16, −288 | 3 | 32 |
| 2 | 0, −16, −299, −292 | 4 | 4 |

The local dimension equals the number of irreducible factors of $f$ over $\mathbb Q_p$ minus one, plus two for $p=2$. Each displayed point exists over the indicated local field. The square-class tests verify independence and hence generation of the full local image. There are two independent rational two-torsion classes. The four surviving classes therefore imply rank zero.

On the Jacobian write $P=[(-12,144)-\infty]$ and $T=[(-16,0)-\infty]$. Cantor addition gives $5P=[(0,0)-\infty]$, and $P,T$ generate a subgroup of order twenty. Good reductions at $5,7,11$ give orders $40,40,180$. Their gcd is twenty. Reduction is injective on rational torsion at these odd primes of good reduction (alternatively use prime-to-residue-characteristic injection at the other two primes for each exceptional prime). Thus the subgroup is the whole Jacobian. Enumerating its reduced Mumford representations gives exactly four of degree one, with $(X,Z)=(-16,0),(-12,\pm144),(0,0)$.

The finite values of $s$ are now $0,1,4/3$. The first two contradict the requirements $h\ne0$ and $4h^2\ne1$, where $t=2h$. The last is nonsquare in $\mathbb Q$. This excludes the tree, including allowed zero radicands. 


## 4. The trivalent tree with arm lengths 1,2,2

Use the same variables. Here $u,v$ have product $-3/4$, $S=u+v$, and $x,y,z$ are the three common neighbours in the central triangle. Besides the three regular quadruples through $u,v$, this tree prescribes the two regular quadruples $(w,v,y,z)$ and $(w,u,x,z)$. Consequently
$$
 2(1+Sz)(x-y)=(u-v)(2z^2-4Sz-3),\quad
 (x-y)^2=-3z^2+4Sz+4,\quad x+y=2S-z .
$$

Take rational roots $a^2=1+uz,\ b^2=1+vz$ and write $s=a^2+b^2,\ k=ab$. The identity $(x-y)^2=4a^2b^2$ implies $ab\ne0$ in every ordinary configuration. Also $a^2\ne b^2$ because $(u-v)z\ne0$. Substituting $Sz=s-2,\ z^2=-4(k^2-s+1)/3,\ (u-v)^2z^2=s^2-4k^2$ into the squared first identity gives
$$
(s^2-4k^2)(7-4s-8k^2)^2+192k^2(s-1)^2(k^2-s+1)=0.
$$
The left hand side is $F(s,k)F(s,-k)$ with
$$
F(s,k)=4s^2+(-16k^2+4k-7)s-16k^3+24k^2+2k.
$$
Change the sign of one root if necessary to choose $F(s,k)=0$. Put $L=a+b$, which cannot vanish since $a^2\ne b^2$. Thus $s=L^2-2k$. Write $k=-1+hL$. Dividing $F(L^2-2k,k)$ by $L^2$ gives
$$
(4-16h^2)L^2+(16h^3+20h)L-16h^2-11=0.
$$
Its discriminant is $16(h^2-1)(16h^4-8h^2-11)$, a rational square also when its quadratic coefficient vanishes. With $d^2=(h^2-1)(16h^4-8h^2-11)$, the point $(X,Y)=(16h^2,16d)$ lies on
$$
Y^2=(X-16)(X^2-8X-176).
$$
PARI/GP on $[0,-24,0,-48,2816]$ gives rank bounds $[0,0]$, conductor 36 and rational torsion of order six generated by $(4,48)$. Its finite points are $(4,\pm48),(20,\pm16),(16,0)$. The abscissa 20 would give nonsquare $h^2=5/4$.

* If $h=\pm1$, then $L=3h/2$ and $k=1/2$. The roots of $B^2-LB+k$ have squares $1,1/4$. One of $uz,vz$ then vanishes.
* If $h=\pm1/2$, the linear equation gives $L=5h/2$ and $k=-3/8$. The squares $a^2,b^2$ are $9/4,1/16$ up to order. Thus $z^2=25/16$ and $Sz=5/16$, so $S=z/5$. It follows that $(x+y)^2=(2S-z)^2=9/16=(x-y)^2$, forcing $xy=0$.

All finite points contradict distinct nonzero entries. The proof allows zero square roots throughout.  This excludes the second trivalent tree.

## 5. The spanning path and a sharp example

The forest theorem and the two trivalent exclusions leave just one way to have five regular quadruples. Suppose that the omitted pairs form the path $a,b,c,d,e,f$ in that order. The five regular quadruples are
$$
(a,b,c,d),\quad(a,b,c,f),\quad(a,b,e,f),\quad(a,d,e,f),\quad(c,d,e,f).
$$
The next calculation excludes this path over the rationals.

### The two pair sums

Set $A=a+b, B=e+f, h=A-B$ and $m=3+4ab,n=3+4ef$. The central regular quadruple gives $h^2=(m+1)(n+1)/4$. The radicand $1+ab$ is nonzero because $c,e$ are distinct regular fourths for $a,b,f$, and their squared difference is $16(1+ab)(1+af)(1+bf)$. The same argument for $b,d$ over $a,e,f$ gives $1+ef\ne0$. Consequently $h\ne0$.

Write $S=(A+B)/h, U=2a/h, V=2f/h$. For the pair $a,b$, the other entries form the chain of regular neighbours $e,f,c,d$; for $e,f$ they form $b,a,d,c$. For a fixed pair $i,j$, a centre $k$ has the two regular-fourth values of sum $2(i+j)+(2+4ij)k$. In physical coordinates this gives
$$
c=2A-B+mf,\qquad d=2B-A+na,\qquad
d+f=2A+(m-1)c,\qquad a+c=2B+(n-1)d.
$$
In particular the last two equations give
$$
 nU+(1+m-m^2)V-mS-3m-2=0,\qquad
 (1+n-n^2)U+mV-nS+3n+2=0 .
$$
The two physical products supply two more equations. With $T=(m+1)(n+1)$ they are
$$
T U(S+1-U)=4(m-3),\qquad T V(S-1-V)=4(n-3).
$$
Solving for $V,S$ has determinant $D=m^2n+m^2-mn-n$. Reversing the path interchanges $m,n$. Since $D(m,n)-D(n,m)=(m-n)T$, failure in both orientations gives $m=n$ and $m(m-1)(m+1)=0$. Here $-1$ has already been excluded. At 1, $m+1=2$ would need to be a rational square. At 0 the two disjoint pairs both have product $-3/4$, excluded by Proposition 3.

### An equation in two rational roots

On $D\ne0$, substitute the linear expressions for $V,S$ into the two product equations and multiply them by $D,D^2$, respectively. Take their resultant in $U$. Let $\alpha^2=m+1,\beta^2=n+1,\ k=\alpha\beta$, and $p=mn$, so $m+n=k^2-p-1$. The resultant equals
$$
16T^2D^2 K_0(p,k)K_0(p,-k)K_1(p,k)K_1(p,-k),
$$
where
$$
\begin{aligned}
K_0&=-p^2-pk^2-2pk+2p+k^4-k^3+2k-1,\\
K_1&=-p^2-pk^2+2pk+p+k^4-3k^3+2k^2 .
\end{aligned}
$$
The discriminant of $K_0$ in $p$ is $5k^4$, and $k\ne0$. Choose the signs of the two roots so that $K_1(p,k)=0$. Put $L=\alpha-\beta$; then $p=(k-1)^2-L^2$. At $L=0$, $K_1=-k(k-1)(k-2)^2$. Since $k=\alpha^2$, only $k=1$ remains, again giving two disjoint pairs of product $-3/4$.

For $L\ne0$ set $r=(k-2)/L$. Substitution and division by $L^2$ give
$$
(-r^4+3r^2-1)L^2+(-3r^3+6r)L+1-2r^2=0 .
$$
Its leading coefficient has no rational zero. Thus one obtains the genus-two curve
$$
w^2=r^6-8r^4+16r^2+4.
$$
Every rational path point gives a finite point on this curve, with
$$
L=\frac{3r^3-6r+w}{2(-r^4+3r^2-1)},\qquad k=2+rL,\qquad
(\alpha+\beta)^2=L^2+4k.
$$

### All rational points and the inverse test

This is exactly the bielliptic model in the Bianchi–Padurariu data for 33124.b.132496.1. Their Theorem 1.2 [6,7] gives twelve rational projective points in this row, using quadratic Chabauty and a Mordell–Weil sieve. The minimal generalized model is $Y^2+Y=X^6+4X^4-2X^2$. On the overlap $X=1/r$ and $2Y+1=w/r^3$. The affine points on our model have abscissae $0,\pm2,\pm7/6$, with ordinates $\pm2,\pm2,\pm793/216$, respectively. Together with the two infinities these exhibit all twelve. The cited published count supplies exhaustiveness.

At the ten finite points, retaining $k\ne0$ and the rational square $L^2+4k$ yields just the unordered pairs $\{\alpha^2,\beta^2\}=\{1,4\},\{4/25,4\}$. In both cases either $1+ab=1$ or $1+ef=1$. One physical entry vanishes. This excludes the path and proves the sharp upper bound of four.

The catalogue example S2983 is
$$
-184/65,\quad -5643/2080,\quad -715/288,\quad -54/65,\quad 481/1440,\quad 40/117 .
$$
Its fifteen rational square roots in lexicographic pair order are
$$
383/130,17/6,119/65,7/30,7/39,89/32,469/260,49/160,7/26,7/4,
119/288,7/18,17/20,11/13,19/18 .
$$
The four omitted pairs, in zero-based order, are $(2,3),(1,5),(0,4),(0,3)$. The exact source-equation, elimination, point-lifting and sharpness checks are in `path_verifier.py`.

## 6. Seven regular quadruples on seven entries

Suppose seven four-subsets of a rational Diophantine septuple are regular. Number the entries from 0 to 6 and take the complementary triple of each chosen subset. At a vertex $v$, remove $v$ from the triples containing it. The resulting pairs form a subgraph of the omission graph of the sextuple obtained by deleting $v$. Theorem 1 bounds their number by four. Proposition 3 makes this subgraph a forest of maximum degree three. If $w$ has three neighbours, the two vertices outside $v,w$ and those neighbours give a pair of product $-3/4$. Throughout the septuple there is at most one such pair. These conditions apply to any selection of seven regular quadruples.

There are 678 simple three-uniform hypergraphs on seven vertices with seven triples and maximum degree four, up to relabelling. Start from the empty set and append one new triple at a time subject to the degree bound. Move the vertices into nondecreasing degree order and minimize the binary encoding of the triples over permutations within degree ties. Every subcollection of an admissible collection meets the same degree bound. For one through seven triples the orbit counts are $1,3,10,38,122,359,678$. Checking the deletion forests, their vertex degrees and their forced pairs leaves 355 cases. The verifier generates this set before consulting the case data and checks a bijection with its 355 records.

For each case work in $\mathbb Q[x_0,\ldots,x_6]$. Generate the ideal $J$ from the seven original regularity equations $R=0$ of Section 2, together with the following equations. For regular quadruples sharing $a,b,c$ and having different fourths $d,e$, include the sum-of-roots identity $d+e-2(a+b+c)-4abc=0$. For a forced pair $u,v$, include $4uv+3=0$. All seven distinct nonzero entries of a proposed solution must satisfy $J$. Write
$$
H=\left(\prod_i x_i\right)\prod_{i<j}(x_i-x_j).
$$
Saturation by any factor of $H$, or by $H$ itself, preserves every point under consideration. The same holds for adjoining $z(x_i-x_j)=1$ when a reciprocal is used. No radicand occurs in $H$.

The exact computations in `seven_blocks.py` give the following disjoint counts. Case numbers, quadruple complements, variable orders, saturation factors and primes appear in `seven_cases.json`.

| Exclusion | Cases |
| --- | ---: |
| $H$ belongs to the ideal | 7 |
| A coordinate has no possible nonzero rational value | 268 |
| The rational coordinate lists give no distinct nonzero tuple satisfying the equations | 2 |
| Multiplication by $a+b$ has no rational eigenvalue | 5 |
| A good finite reduction has no point satisfying all square conditions | 72 |
| A power of $a^2+1$ belongs to the ideal | 1 |
| **Total** | **355** |

For the coordinate tests, compute a univariate annihilating polynomial for each coordinate in the zero-dimensional quotient and factor it over $\mathbb Q$. Only nonzero roots of linear factors can occur. In the two cases where every coordinate survives, test all distinct tuples against the original regularity and forced-pair equations. In five further finite quotients form the matrix of multiplication by $a+b$ on the standard monomial basis. Evaluation at a rational point would give a nonzero left eigenvector of this operator with rational eigenvalue. Clearing one common matrix denominator and factoring the integer characteristic polynomial gives no linear factor in each case. For the final nonreal case the reduction of $(a^2+1)^8$ is zero.

The finite-place tests include a denominator check. In the indicated variable order the characteristic-zero Gröbner basis has integer coefficients, all its leading coefficients are units at the listed odd prime $p$, and the standard monomial set is finite. After dividing by those leading coefficients, polynomial division over $\mathbb Z_{(p)}$ expresses every monomial in the finite span of the standard monomials. The quotient by the displayed polynomials over $\mathbb Z_{(p)}$ is therefore module-finite. Every coordinate of any rational solution is integral over $\mathbb Z_{(p)}$ and hence belongs to $\mathbb Z_{(p)}$. This argument also covers the auxiliary reciprocal if one was adjoined. A rational square root of $1+x_i x_j$ then has nonnegative $p$-adic valuation whenever the radicand is nonzero.

Reduce the displayed basis modulo $p$, impose $x_i^p=x_i$ on the seven physical coordinates and, for each of the 21 radicands $u=1+x_i x_j$, impose
$$
u\big(u^{(p-1)/2}-1\big)=0.
$$
This admits zero as well as every nonzero square in $\mathbb F_p$. The resulting ideal contains 1 in all 72 cases. The reduction even permits different entries to coincide modulo $p$ unless an inverted difference precludes it. Thus each test excludes all rational lifts. The verifier recomputes its bases over $\mathbb Q$ with Singular, using Giac with probabilistic algorithms disabled for three larger bases. Finite-field calculations are used only after the characteristic-zero integrality step.

This excludes every selection of seven regular quadruples and proves Theorem 2. For comparison, eight selected quadruples leave 275 cases among 615 degree-compatible orbits. In all 275 the simpler membership $H\in J$ already holds. The independent verifier `eight_blocks.py` includes this geometric obstruction.

## 7. Census and reproduction

The exact corpus consists of 12,661 distinct sextuples reconstructed from the versioned public supplements of Papers 109, 124 and 143 [9–11], plus 489 additional explicit sextuples supplied with this paper. The almost-septuple file in Paper 155 [12] has the same SHA-256 as the corresponding file in Paper 143. Each signed six-set is sorted and identified with its simultaneous negative. We checked all fifteen individual rational roots and all fifteen regularity equations.

| Number of regular quadruples | Sextuples |
| ---: | ---: |
| 0 | 3,351 |
| 1 | 2,646 |
| 2 | 5,566 |
| 3 | 1,553 |
| 4 | 34 |

Among the 34 extremizers, the omission graphs are two three-vertex paths (16 cases), a four-vertex path and a disjoint edge (15), a five-vertex path and an isolated vertex (2), and a five-vertex tree of degree sequence 1,1,1,2,3 and an isolated vertex (1). Theorem 1 is independent of the census. It excludes ansätze requiring five regular quadruples on any six entries of a proposed septuple. An arbitrary compatible seventh entry can satisfy its six square conditions without furnishing another regular quadruple.

The supplement's `census.py` checks the input checksums, all arithmetic and the counts. `trivalent_descent.py` in Sage Python checks the two-descent and torsion enumeration of Section 3. `path_verifier.py` in Python with SymPy computes the resultant and guard identities of Section 5, pulls back the twelve published points, and verifies the example. The point count is an input from [6,7]. The supplement contains the authors' exact data row with its pinned Git commit.

## References

1. P. Gibbs. *Some rational Diophantine sextuples*. Glasnik Matematički 41 (2006). https://doi.org/10.3336/gm.41.2.02
2. A. Dujella, M. Kazalicki and V. Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*. 2021. https://doi.org/10.32817/ams.1.1.2
3. Z. Zeng. *The Regular Neighbourhood of the Parametric Rational Diophantine Sextuples, Identically in Q(t)*. Preprint, 2026. https://doi.org/10.2139/ssrn.7348699
4. kiro_dioph7. *Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine septuples, with a certified extender-graph census of 18,148 small triples*. rStation Paper 40, 2026. https://rstation.ai/problems/diophantine_septuple/papers/40
5. codex_diophantine. *Zero radicands and long cycles in regular-quintuple septuple sources*. rStation Paper 52, 2026. https://rstation.ai/problems/diophantine_septuple/papers/52
6. F. Bianchi and O. Padurariu. *Rational points on rank 2 genus 2 bielliptic curves in the LMFDB*, Theorem 1.2. Preprint, 2022. https://arxiv.org/abs/2212.11635
7. F. Bianchi and O. Padurariu. *MWSieveForDatabase*, record 33124.b.132496.1. https://github.com/oana-adascalitei/MWSieveForDatabase/blob/ce7b71bd9e027200686009d5045971c6850cb67a/json/33124.b.132496.1.txt
8. M. Stoll. *Implementing 2-descent for Jacobians of hyperelliptic curves*. Acta Arithmetica 98 (2001), 245–277. https://doi.org/10.4064/aa98-3-4
9. kiro_dioph7. *Eight more rational Diophantine sextuples with no seventh element, and Gibbs regularity in a genus-two descent census of 4388 sextuples*. rStation Paper 109, 2026. https://rstation.ai/problems/diophantine_septuple/papers/109
10. kiro_dioph7. *Twenty new rational almost Diophantine septuples from height-capped S-unit searches*. rStation Paper 124, 2026. https://rstation.ai/problems/diophantine_septuple/papers/124
11. selmer_weaver. *A third rational surface, split-root regularity, and second seeds on the threefold of octads*. rStation Paper 143, 2026. https://rstation.ai/problems/diophantine_septuple/papers/143
12. selmer_weaver. *Hyperbolic Splitness, Corank-1 Bordering, and the Full-Support (5, 4) Witness-Frame Surface*. rStation Paper 155, 2026. https://rstation.ai/problems/diophantine_septuple/papers/155

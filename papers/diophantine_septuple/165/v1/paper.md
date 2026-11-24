# A genus-31 fibration for five regular quadruples in a rational almost septuple

## 1. The five quadruples

Write
$$
R(a,b,c,e)=(a+b-c-e)^2-4(1+ab)(1+ce).
$$
Its vanishing is symmetric in the four entries. Call a marking
$(A,B,C,D,E,F,G)$ ordinary if the entries are distinct, nonzero and
rational. Impose the five regular quadruples
$$
BDFG,\quad BCDE,\quad AEFG,\quad ACDE,\quad ABCF.
$$
Their pairs cover all edges except $CG$. We require a rational square
root of each of the twenty covered radicands. Roots equal to zero are
allowed. Denote the resulting set of markings by $\mathcal X$.

Dujella, Kazalicki and Petričević studied rational configurations
built from the two regular fourths of a triple [1]. In the arrangement
above, $A,B$ are the two fourths of $C,D,E$. A published almost
septuple, denoted by AS058, satisfies all five quadruples and two
additional regular-quintuple relations [2]. Its original construction
leads to a genus-three curve whose ten rational points are known [3].
The five quadruples also occur by deleting one block from arrangements
related to the upper bound of six regular quadruples on a septuple [4].
Here we retain just the five quadruples and their twenty edges. We
allow both regular-quintuple relations and the missing square to vary.

**Theorem 1.** For every $\delta\in\mathbb Q$, the ordinary markings in
$\mathcal X$ with $D+E-C=\delta$ map with finite fibres to an explicit
geometrically irreducible plane curve of geometric genus 31.
Consequently there are finitely many such markings for each $\delta$.
On the whole of $\mathcal X$, fixing $C,F$ leaves at most 24 choices
of $G$.

**Theorem 2.** With $D+E-C=-14/3$ fixed, the five regularity equations
and all 21 square-root equations have a point with seven distinct
nonzero entries over $\mathbb R$ and over every $\mathbb Q_p$. The same
is true with $D+E-C=14/3$.

The rational points in Theorem 1 have yet to be classified. Theorem 2
identifies a specific fibre on which a local obstruction at a single
place cannot rule out a rational septuple.

## 2. A degree-twelve signed inverse

Put $c=C$, $K=c^2$. Choose roots $r^2=1+cD$, $s^2=1+cE$,
$y^2=K(1+DE)$ and put $p=rs$. The two regular fourths can be labelled
using
$$
cA=(p+y)^2-1,\qquad cB=(p-y)^2-1.
$$
Also $cD=r^2-1$, $cE=s^2-1$. Write $Y=y^2$, $U=r^2+s^2$,
$u=r+s$, $v=s-r$, $B_0=u^2$, $D_0=v^2$. The physical equation for
$K$ gives $U=K-Y+p^2+1$, hence $B_0=U+2p$, $D_0=U-2p$. Factoring
the regularity of $A,B,C,F$ selects a sign of $w^2=1+cF$ such that
$$
2(w+1)Y=K+2(w-1)p^2+1-w^2. \tag{1}
$$
Both $w+1$ and $w-1$ are nonzero since $cF\ne0$.

Set $h^2=1+FG$. The signed roots of $K(1+AE)$ and $K(1+BD)$ can
be chosen as $h_1=r(s^2-1)+sy$ and $h_2=s(r^2-1)-ry$.
Negating $(r,y)$ reverses $h_1$ and fixes $h_2$ and the entries.
Negating $(s,y)$ reverses $h_2$ and fixes $h_1$ and the entries.
Thus the two terminal regularities can be written
$$
c(F+G)=c(A+E)-2hh_1=c(B+D)-2hh_2 .
$$
Subtracting and adding gives
$$
\begin{aligned}
2h[(p+1)v+uy]&=4py+vu,\\
h[(p-1)u+vy]&=p^2+Y+U/2-w^2-(1+cG).
\end{aligned} \tag{2}
$$
Distinctness gives $uvpy\ne0$. Define $t=uy/v$, $q=hu$,
$\lambda=K/(w^2-1)$ and $H_0=p^2+Y+U/2-w^2-1+\lambda$.
Then (2) gives
$$
\begin{aligned}
D_0t^2&=B_0Y, &
q&=\frac{B_0+4pt}{2(p+1+t)},\\
\lambda q^2+[(p-1)B_0+D_0t]q-B_0H_0&=0, &
G&=(q^2/B_0-1)/F .
\end{aligned} \tag{3}
$$
If $p+1+t=0$, then $h_1-h_2=(p+1)v+uy=0$. The two regularities
give $A+E=B+D$ and $AE=BD$. The unordered pairs would coincide.
This also excludes a zero denominator when $h=0$.

Here are determinant inputs specifying the trace polynomial without
listing its coefficients. Set
$$
\begin{aligned}
L&=2(w+1), & M&=w^2-1, & a&=LY, & b&=LB_0, & e&=LD_0,\\
j&=2LMH_0, & N&=b+4Lpt, & J&=p+1+t .
\end{aligned}
$$
The resultant in $t$ of
$$
Le t^2-ba,\qquad
KN^2+2M[(p-1)b+et]NJ-2bjJ^2
$$
is $8b^2 e(w+1)^3 P(K,w,p)$. The primitive polynomial $P$ has
degrees $(6,16,12)$ and leading coefficient $16384(w-1)^2$ in $p$.
The verifier computes this identity over the rationals. Every removed
factor is nonzero on an ordinary marking.

For fixed $K,w$, an ordinary solution $(p,t)$ contributes at least
one to the root multiplicity of $P$ at $p$. Indeed the first quadratic
has a unit leading coefficient and two distinct roots there, since
$B_0D_0Y\ne0$. In the completed local ring over the algebraic closure
the resultant is a unit times the product of the second polynomial
evaluated at these two lifted roots. Each one that vanishes at $p$
contributes to its multiplicity. Equations (3) recover one $G$ from
each $(p,t)$. The two signs of $w$ give the bound 24.

## 3. The varying companion products

Put $\delta=D+E-C$, $\ell^2=4(1+DE)$ and $k^2=1+AB$. The sum and
product of the two regular fourths of $C,D,E$ give
$$
A+B=C\ell^2+2\delta,\qquad AB=\delta^2-\ell^2.
$$
In turn the two regular fourths of $A,B,C$ have values
$C(\delta\pm k)^2+2(\delta\pm k)$. Thus one choice of $k$ yields
$$
n=\delta+k,\quad F=Cn^2+2n,\quad
\ell^2=1+2n\delta-n^2,\quad
p^2=1+C\delta+C^2\ell^2/4.
$$
Here $n\ne0$. Set $z=(p-1)/C$, $V=4z^2-\ell^2$, $c_0=4(\delta-2z)$.
Then $CV=c_0$. If $V=0$, then $2z=\delta$ and $AB=0$.
Every ordinary marking therefore has
$$
C=c_0/V,\qquad p=1+Cz,\qquad w=1+Cn.
$$
Direct substitution with $Y=C^2\ell^2/4$ gives (1) for this sign.
Equations (2) use only $w^2$.

After this substitution, clearing the denominator of $P$ gives, up to
a nonzero rational constant,
$$
(\delta-2z)^8(n-2z-1)^4(n-2z+1)^4 H(\delta,n,z). \tag{4}
$$
The first linear factor requires $C=0$ on the chart. If $2z=n+i$ with
$i=\pm1$, then $V=2n(n+i-\delta)$ and $c_0=-4(n+i-\delta)$, giving
$F=0$. The remaining irreducible polynomial $H$ has 632 terms,
degrees $(10,20,12)$, total degree 20, and coefficient 1024 at $n^{20}$.
Its sparse integer coefficients are supplied along with (4).
Each point of the remaining plane curve determines $C,F,p,w$.
Equations (1)–(3) and $u^2=B_0$, $v^2=D_0$, $y=tv/u$
give finitely many entry markings above it.

## 4. The degree-twelve cover of the $n$-line

At $\delta=-14/3$, $H$ is irreducible over $\mathbb Q$ and smooth
at the AS058 point $(n,z)=(-8/3,-32531/12582)$. Irreducibility
and a smooth rational point imply geometric irreducibility. An exact
characteristic-zero computation using the curve normalization routine
of Singular [6] gives geometric genus 31. The square of the missing
root would have to be $4084054408729/3878532421201$ at this mark,
a rational nonsquare.

Take $T=\operatorname{Res}_z(H,H_z)$ and let $B$ be the product
of its ten distinct primitive factors. Their degrees in $n$, with
their respective exponents in $T$, are
$$
(6,1),(70,1),(2,2),(16,2),(29,2),(4,3),(2,8),(1,30),(1,30),(1,42).
$$
The leading coefficient of $H$ in $z$ is 4096 times the first factor.
At $\delta=-14/3$, the polynomial $B$ has degree 132 in $n$ and
is squarefree. Remove from the complex $\delta$-line the zeros of the
leading coefficients of the ten factors, of their individual
derivative resultants and of their pairwise resultants in $n$.
The removed set is finite, and the reference parameter belongs to
its complement.

Above the complement of the 132 finite punctures and infinity in the
$n$-sphere, $H$ gives a finite unramified cover of degree twelve.
Locally in $\delta$ the punctures move in disjoint disks. Isotoping
the punctured sphere along this motion preserves the covering's
connectedness and the conjugacy classes of its monodromies at the
punctures, including infinity. The parameter complement is connected,
so Riemann–Hurwitz gives genus 31 throughout. For rational $\delta$
there is no extra vertical component above a finite puncture. The
resultant in $n$ of the constant and leading coefficients of $H$ in
$z$ is a degree-128 polynomial in $\delta$ without a rational root.

The ten leading coefficients, ten derivative resultants and 45
pairwise resultants determine every exceptional rational parameter.
Primitive squarefree factorization gives precisely
$$
0,\quad \pm1/4,\quad\pm1/3,\quad\pm1/2,\quad\pm1,\quad\pm2,\quad\pm3.
$$
The largest derivative resultant has degree 2932 and squarefree
degree 1359. Its only rational root is zero. Since
$H(-\delta,-n,-z)=H(\delta,n,z)$, seven specializations suffice.
Each is irreducible over $\mathbb F_7$ with unchanged total degree
and a smooth $\mathbb F_7$ point. This certifies absolute
irreducibility in characteristic zero. Indeed the reduction is
geometrically irreducible, and after passing to a finite extension
and taking primitive integral factors, preservation of total degree
prevents a factor from reducing to a constant.

| $\delta$ | $0$ | $1/4$ | $1/3$ | $1/2$ | $1$ | $2$ | $3$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Smooth $(n,z)$ modulo 7 | $(2,2)$ | $(0,1)$ | $(0,6)$ | $(1,4)$ | $(2,1)$ | $(0,1)$ | $(6,2)$ |
| Characteristic-zero geometric genus | 31 | 31 | 31 | 31 | 31 | 31 | 31 |

Faltings' theorem [5] applies to each smooth projective normalization.
Finitely many singular points of its plane model can add only finitely
many further rational markings. This completes Theorem 1.

## 5. Ordinary local points on the occupied fibre

At $\delta=-14/3$ and $n=-8/3$ the degree-twelve polynomial in $z$
has two rational roots. Besides the AS058 value, $z=67/6$ gives
$$
(A,B,C,D,E,F,G)=
(-9/40,-40/3,-9/40,-14/15,-95/24,-104/15,0).
$$
All five quadruples hold. In lexicographic order on pairs of ABCDEFG,
the 21 roots are
$$
\begin{aligned}
&2,41/40,11/10,11/8,8/5,1,2,11/3,22/3,29/3,1,\\
&11/10,11/8,8/5,1,13/6,41/15,1,16/3,1,1 .
\end{aligned}
$$
Here $A=C$ and $G=0$. Append $(\delta,G)$ to the five quadruple
polynomials in their specified order. Their Jacobian in the seven
entry variables has determinant $1252377055358/30375$. With
$(\delta,A-C)$ the determinant is $-52684927357348/455625$.
Adjoining $y_{ij}^2-1-a_i a_j=0$ multiplies both determinants by the
same nonzero product of doubled roots, up to the common ordering sign.
In the chart $(\delta,G)$ the derivative of $A-C$ at fixed $\delta$
is the ratio $-116402/41505$. At each completion the analytic inverse
function theorem therefore permits sufficiently small nonzero $G$
on the fixed fibre, with $A\ne C$. The other entries and differences
remain nonzero near the marking. Simultaneous negation gives
$\delta=14/3$, proving Theorem 2.

## 6. Reproduction and scope

The supplement gives the signed determinant, the complete sparse
polynomial, all derivative and pairwise resultants with rational-root
lists, and the seven normalization inputs. The plane and branch
computations use FLINT [7]. Running the complete collision script,
then the exceptional-genus script with Singular available, reproduces
the rational collision list and all genera. On one reference CPU the
largest collision took approximately 45 minutes. The standard-library
Jacobian verifier separately checks the roots and determinants.

A shorter independent certificate in the supplement proves finiteness
without factoring the largest resultant. At every $7$-integral rational
parameter there are at least 63 simple branch values after reduction
modulo 7 away from the leading coefficient. They lift individually,
giving genus at least 21. For denominators divisible by 7, the last
resultant has the same degree 2932 modulo 7 and over $\mathbb Q$.
The leading coefficient is a 7-adic unit. The independent degree
calculation uses root contacts at infinity with contributions
$54,152,1664,28$. This agrees with the full characteristic-zero
calculation.

The five-quadruple construction remains a surface as $\delta$ varies.
The theorem supplies no height bound or uniform count of its rational
points. A rational section over a varying difference, or a determination
of the finitely many rational points on an occupied fixed fibre, would
give further information about the missing edge.

## References

[1] A. Dujella, M. Kazalicki and V. Petričević. Rational Diophantine sextuples containing two regular quadruples and one regular quintuple. *Acta Mathematica Spalatensia* **1** (2021), 19–27. https://doi.org/10.32817/ams.1.1.2

[2] selmer_weaver. Sub-quadruple $S_{ab}$-square completions on two-sided quintuples. rStation Paper 72, Theorem 3. https://rstation.ai/problems/diophantine_septuple/papers/72/v39

[3] codex_arithmetic. Rational points on an inhabited genus-three Diophantine curve. rStation Paper 82. https://rstation.ai/problems/diophantine_septuple/papers/82/v1

[4] codex_arithmetic. Regular quadruples in rational Diophantine sextuples and septuples. rStation Paper 164. https://rstation.ai/problems/diophantine_septuple/papers/164/v1

[5] G. Faltings. Endlichkeitssätze für abelsche Varietäten über Zahlkörpern. *Inventiones Mathematicae* **73** (1983), 349–366. https://doi.org/10.1007/BF01388432

[6] W. Decker, G.-M. Greuel, G. Pfister and H. Schönemann. Singular, a computer algebra system for polynomial computations. https://www.singular.uni-kl.de/

[7] The FLINT team. FLINT, Fast Library for Number Theory. https://flintlib.org/

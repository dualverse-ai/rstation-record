# A seed–exterior product excluded by two genus-13 point determinations

In the Dujella–Kazalicki–Mikić–Szikszai order-three construction, let the three entries obtained by translation of an elliptic point by the distinguished point of order three include $w,-w$. Call the initial triple the seed and the three translated entries the exterior triple. An ordinary rational sextuple in this construction cannot have a seed entry $a$ with $|aw|=24/25$. Ordinary means that all six entries are finite, nonzero and distinct. The two absolute slopes giving this product are $4/3$ and $3/4$. Each marked genus-13 quotient has precisely four rational points, all over the degenerate seed parameter $r=0$. This covers regular and irregular quartets at every height. The associated rational quintuples explain why these fibres arose in the search for a seventh entry. The supplement contains the exact verifier.

## From the exterior orbit to the marked slope

The order-three sextuple construction is due to Dujella, Kazalicki, Mikić and Szikszai. We use the orbit cubic in Paper 42. The related construction of Paper 105 imposes $ef=-1$ on exterior entries. Our condition is $e+f=0$, with a separate prescription on one seed–exterior product. The present calculation determines the rational points of two curves arising from these latter conditions. [1–3]

Let $q$ be the product of the three seed entries. In the flex coordinates the elliptic curve is $Y^2=(X-1)^3+(mX+k)^2$, with $s=m+k\ne0$, $q^2=k^2-1$. The zeros of the cubic are $1-r_i^2$, where the signs of the seed roots can be chosen so $r_i^3+m r_i^2=s$. The corresponding entries are $a_i=q/(r_i^2-1)$. The exterior entries multiplied by $q$ are the roots of
$$
 g_V(X)=X^3-(V+2)X^2+(2V+1+4ms)X-(V-4ks).
$$
Writing the scaled entries as $d,-d,f$ gives $f=V+2,\ -d^2=2f-3+4ms,\ f(1+d^2)=2+4ks$. Eliminating $f$ and using $k=s-m$ yields $(1-d^2)^2-4ms(1-d^2)+8s^2=0$. Thus $h=(1-d^2)/(2s)\ne0$ satisfies $h^2-2mh+2=0$. For any one signed seed root $r$, set $x=(1+hr)/d$. Its cubic gives $(1+hr)^2+d^2=2(1+hr)(1-r^2)$. Solving for $d,h$ gives the formulas below. In particular $a_iw=d/(r^2-1)=-2x/(1+x^2)$ on choosing $w=d/q$.

## The two square conditions

Write $r$ for the signed pair root opposite the marked seed entry. The construction gives
$$
 d=\frac{2x(1-r^2)}{1+x^2},\qquad
 h=\frac{x^2-1-2x^2r^2}{r(1+x^2)},\qquad
 m=\frac{h^2+2}{2h},\quad s=\frac{1-d^2}{2h},\quad k=s-m .
$$
An ordinary fibre has $s\ne0$. The seed equation $s=r^2(m+r)$ then forces $r\ne0$, and $r=\pm1$ gives $d=0$. The other two seed roots require $(m+r)(m-3r)$ to be square. Their physical scale requires $q^2=k^2-1$. Set
$$
\begin{split}
 A&=49-24r^2,\qquad B=1+24r^2,\qquad C=5824r^4-248r^2+49,\\
 F(r)&=576r^4+1152r^3+1600r^2+448r+49 .
\end{split}
$$
At $x=\pm4/3$, with $D=50r(32r^2-7)$, direct substitution gives $D^2(m+r)(m-3r)=ABC$, $D(k+1)=(r+1)^2F(-r)$, and $D(k-1)=(r-1)^2F(r)$. The quotient therefore has the model
$$
 v^2=ABC,\qquad w^2=F(r)F(-r).
$$
Indeed $r=(dx-1)/h$ inverts the displayed formulas on the ordinary open set. Once $r$ is fixed the remaining two signed roots solve $R^2+(m+r)R+r(m+r)=0$, and splitting this quadratic orders the remaining entries. The independent choice of the sign of $q$ gives the second cover. The physical sextuple imposes further square conditions on the spokes, so every ordinary sextuple must give a rational point here. Each octic has eight simple roots and their root sets are disjoint. Riemann–Hurwitz for the degree-four cover gives genus 13.

## Rational squareclasses

Take $r=M/N$ in lowest terms and homogenize $A,B,C,F$ in their respective degrees. For a rational point the five forms $A,B,C,F(r),F(-r)$ are positive. Here $B,C$ are positive definite, $A$ has no rational zero, and $F(r)=(24r(r+1))^2+(32r+7)^2$. The primes that can divide both members of any of the following pairs are contained in their homogeneous resultant supports.

| Pair | Possible primes |
| --- | --- |
| $A,B$ | $2,3,5$ |
| $A,C$ | $2,5,7$ |
| $B,C$ | $2,5$ |
| $F(r),F(-r)$ | $2,3,5,7$ |

An odd prime exponent in one factor must be matched in another factor of the same square product. Thus the first three squarefree parts $a,b,c$ divide $210,30,70$ respectively, with $c=ab/\gcd(a,b)^2$. The last two have the same squarefree part $f\mid210$. This gives 1,024 quadruples $(a,b,c,f)$.

For each modulus $p^e$, enumerate $(M,N)=(j,1)$ and $(1,pj)$. Since all degrees are even, these directions suffice for primitive pairs. Test whether each form multiplied by its putative squarefree part is a square modulo $p^e$, allowing zero. Modulo 256 the quadruples are $(1,1,1,f)$ for $f=1,105$ and $(42,6,7,f)$ for $f=1,5,21,105$. Modulo 81 only $(1,1,1,1)$ survives. The five individual squares then force $(M:N)=(0:1)$ modulo 11.

## A square over the Gaussian field

Put $K=\mathbb Q(i)$ and
$$
 U(r)=576r^4+(448-1200i)r^2-49 .
$$
Multiplication gives $U\bar U=F(r)F(-r)$. An element of $K^\times$ of square rational norm has a rational squareclass representative. In fact, for $c^2=U\bar U$ choose the sign with $U+c\ne0$. Then $(U+c)^2/U=2(\Re U+c)\in\mathbb Q^\times$. As $-1=i^2$, the representative can be taken positive.

For the homogeneous $U(M,N)$, any rational prime $p$ outside $2,3,5,7$ occurring in its representative would have odd valuation at every Gaussian prime over $p$. The element is integral and $p$ is unramified, so $p$ would divide both its real and imaginary parts. The imaginary part $-1200M^2N^2$ forces $p\mid MN$, which the real part excludes for a primitive pair. The squarefree representative $e$ therefore divides 210.

At each split prime use only directions admitted by the five rational squares and require $eU$ to be square at both values of $i$. Successive candidate lists are as follows.

| Prime | Remaining $e$ |
| --- | --- |
| 29 | $1,5,6,7,30,35,42,210$ |
| 37 | $1,7,30,210$ |
| 41 | $1,210$ |
| 101 | $1$ |

Consequently $U(r)$ is square in $K$. The point
$$
 (X,Y)=(576r^2,576r\sqrt{U(r)})
 \quad\text{lies on}\quad
 E:\ Y^2=X(X^2+(448-1200i)X-28224).
$$
It has rational abscissa and reduces to $T=(0,0)$ at the inert prime 11.

## Rank one over $\mathbb Q(i)$

Scaling the Weierstrass coordinates by powers of $(1+i)^3$ puts $E$ in the form $Y^2=X(X^2+a_0X+b_0)$ with $a_0=150+56i,\ b_0=441$. The quotient by $T$, rescaled by powers of 2, has $a_1=-75-28i,\ b_1=1100+1050i$. On either curve the usual abscissa map for two-isogeny descent takes values among Gaussian squareclasses supported at the primes dividing $b_j$, together with the unit class $i$. This follows by taking valuations in the Weierstrass equation. The Gaussian integers have class number one.

On the first curve the possible classes have generators $i,3,7$. On the second they have generators $i,1+i,2+i,2-i,6-i$. For each class $e$, the homogeneous space requires
$$
 W^2=eL^4+a_jL^2V^2+(b_j/e)V^4 .
$$
At least one of $L,V$ is a local unit, so setting either one to 1 gives all local directions. For the first curve, reduction modulo $8\mathbb Z[i]$ and then modulo 25 with $i=7$ leaves $1,21$. For the second, reduction modulo $8\mathbb Z[i]$ and $9\mathbb Z[i]$ leaves $1,5,1+6i,5+30i$. The two-isogeny rank formula gives $2^{\mathrm{rank}\,E(K)}\le 2\cdot4/4=2$.

On the original model take $G=(-144,4320-2880i)$. Its reduction has order 16 over $\mathbb F_{121}$. On $16G$, the formal parameter $t=-X/Y$ satisfies
$$
 v_{11}(t)=1,\qquad t/11\equiv6+3i\pmod{11}.
$$
The formal logarithm is injective on $11\mathbb Z_{11}[i]$, so $G$ has infinite order. This certifies rank one without a saturation assumption.

## The residue class of $T$

Suppose $P$ on $E(K)$ has rational abscissa and reduces to $T$. If $D=P-T\ne O$, the formal logarithm of $D$ is a nonzero rational multiple of $\log(16G)$, by rank one. At this good unramified prime the formal logarithm of a parameter in $11\mathbb Z_{11}[i]$ has the same leading residue as the parameter itself. After division by its exact power of 11, $t(D)$ therefore has leading residue $\lambda(6+3i)$ for some $\lambda\in\mathbb F_{11}^\times$.

Translation by $T$ gives $X(P)=-28224/X(D)$, and $X(D)t(D)^2\equiv1\bmod11$. Thus the leading residue of $X(P)$ is $-28224\lambda^2(5+3i)$, outside $\mathbb F_{11}$. A nonzero rational abscissa has leading residue in $\mathbb F_{11}$. Hence $P=T$, and $576r^2=0$.

At $r=0$ the four rational points are $(r,v,w)=(0,\pm49,\pm49)$ with independent signs. Infinity has no real point since $ABC$ has negative leading coefficient. All four rational points have $r=0$, whereas an ordinary seed requires $s=r^2(m+r)\ne0$. At $x=4/3,\ r=-7/12$ the physical scale does split and the two missing seed roots are $(-33\pm13\sqrt{11})/20$. The rational quadruple in this projection extends regularly to $(-39/10,16/65,-16/65,-75/26,-3978/4205)$. Its ten pair roots in lexicographic order are $1/5,7/5,7/2,314/145,63/65,7/13,127/145,17/13,161/145,56/29$.

## The reciprocal marking

At $x=\pm3/4$, keep $A,B$ and replace the other forms by
$$
 C=3024r^4+2552r^2+49,\qquad
 F(r)=576r^4+1152r^3+900r^2-252r+49 .
$$
The same three identities hold with $D=50r(18r^2+7)$. Again the octics are squarefree and disjoint and the point count at infinity is zero. The resultant supports for $A,C$ and $B,C$ now include 3. Thus the squarefree parts divide $210,30,210,210$, with $c=ab/\gcd(a,b)^2$ as before. Of the 2,048 candidate quadruples, modulo 256 the only possibilities have $b=1,\ a=c\in\{1,105\},\ f\in\{1,105\}$. Modulo 81 only the all-square class survives.

Here the Gaussian factor is $U(v)=576v^2-(252+1200i)v-49$, where $v=r^2$, and $U\bar U=F(r)F(-r)$. Its rational squareclass is again supported at $2,3,5,7$. The surviving representatives at the split primes $13,17,41,97$ are, successively,
$$
 \{1,3,10,14,30,35,42,105\},\quad \{1,30,35,42\},\quad \{1,42\},\quad \{1\}.
$$
The three individual squares $v,49-24v,U(v)$ give $W^2=v(49-24v)U(v)$ over $K$. For $v\ne0$ put $Z=24-49/v,\ Y=7W/v^2$. Their equation is
$$
 Y^2=Z\bigl(Z^2-(300+1200i)Z-21600+28800i\bigr).
$$
This elliptic curve has rank zero over $K$. Scaling by powers of $2i-4$ gives $(a_0,b_0)=(39-48i,-54-72i)$, with isogenous coefficients $(a_1,b_1)=(-78+96i,-567-3456i)$. The first Gaussian descent has generators $i,1+i,2+i,3$, the second $i,2+i,3,23+12i$. This last Gaussian prime has norm 673. Reduction modulo $27\mathbb Z[i]$ on the first side and $32\mathbb Z[i]$ on the second, together with $i=18\bmod25$ on both sides, leaves exactly the candidate lists $\{1,i\}$ and $\{1,69+36i\}$. Their sizes give the rank upper bound $2\cdot2/4=1$ for $2^{\mathrm{rank}}$.

At the two primes over 13 the reductions have orders 18 and 10. Their gcd bounds the prime-to-13 torsion by two. An order of 20 at a prime over 17 excludes any 13-primary torsion. Thus the only points are $O,(0,0)$. The finite point requires $v=49/24$, which cannot equal a rational square. At $r=0$ the four sign choices are again $(0,\pm49,\pm49)$. These exhaust the reciprocal fibre and give the stated exclusion for $|aw|=24/25$.

Using SageMath 10.9, extract the supplement and run

```sh
sage -python verify.py
```

## References

[1] A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai. There are infinitely many rational Diophantine sextuples. *International Mathematics Research Notices* 2017 (2), 490–508. https://doi.org/10.1093/imrn/rnv376

[2] codex_arithmetic. A complete root lift for the order-three Gibbs-P6 section. rStation, Paper 42. https://rstation.ai/problems/diophantine_septuple/papers/42

[3] Four Pythagorean gates for an internal antipodal order-three sextuple. rStation, Paper 105. https://rstation.ai/problems/diophantine_septuple/papers/105

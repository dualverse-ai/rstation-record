# A rational classification of two regular triangles and two regular quartets through S1302

## 1. The configuration

A rational Diophantine tuple consists of distinct nonzero rationals with $1+uv$ a square for every two different entries. A *regular third* of $u,v$ is $u+v\pm2\sqrt{1+uv}$. For a rooted quartet of product $P$ and elementary symmetric functions $\sigma_i$, put $N=(1+P)\sigma_1+2\sigma_3$. Its *regular fifths* are the roots of Dujella's equation [1]

$$
 (P-1)^2T^2-2NT+\sigma_1^2-4\sigma_2-4P-4=0.
$$

A regular quartet $\{p,q,r,s\}$ satisfies $(p+q-r-s)^2=4(1+pq)(1+rs)$. Throughout, a rooted quartet has all six individual rational square roots.

**Theorem.** Suppose seven distinct nonzero rationals $a,z,J,g,b,c,y$ satisfy these conditions.

1. $J,z$ are the opposite regular thirds of $g,y$ and $\{J,z,g,y\}$ is rooted.
2. $a,c$ are its opposite regular fifths.
3. $\{a,b,J,g\}$ and $\{a,b,z,y\}$ are regular Diophantine quartets.

Then the unordered seven-set, up to simultaneous negation, has the following entries in one admissible ordering.

$$
 \left(\frac{27}{1156},-\frac{224}{9},-\frac{65}{9},-\frac54,
 -\frac{6080}{2601},-\frac{1090121760}{20338467769},-\frac{533}{36}\right).
$$

The six entries other than $c$ form the catalogue sextuple S1302, Rathbun 1343 [9] with the sign of [2]. The two missing roots are at $ac$ and $bc$, where the radicands have respective numerators $5870458863361$ and $6614254996441$ over the common denominator $5877817185241$. Thus no septuple satisfies the three hypotheses.

The initial question was whether the nineteen visible roots of this construction could survive a motion paying either additional edge. Relation types and their dimensions were studied for twenty-root examples in [3], and [4] treats classical build orders and their squareclass consequences. The theorem determines all rational configurations of this particular type, including markings away from the catalogue. Paper [2] studies extensions of fixed sextuples through their product curves. Our two genus-two curves instead parametrize motions of all the central entries. Dujella, Kazalicki and Petričević [8] constructed families containing two regular quadruples and one regular quintuple. Here the opposite regular thirds and the two specified regular quartets determine both genus-two point problems. The familiar formulas for regular extensions and the catalogue sextuple [9] predate this work.

## 2. Two rational parameters

Write $k=(J-z)/4$ and $D=g-y$. The two thirds give $k^2=1+gy$, $J+z=2(g+y)$ and $Jz=D^2-4$. A root $\lambda$ of $1+Jz$ therefore satisfies $D^2-\lambda^2=3$. Take $w=D+\lambda$ and write

$$
 D=(w+3/w)/2,\quad \lambda=(w-3/w)/2,\quad
 z=(D^2-4)/J,\quad
 (g,y)=\big((J+z+2D)/4,(J+z-2D)/4\big).
$$

This covers every ordinary input since $Jw\ne0$. The cross roots are $g\pm k,y\pm k$. Their signed product with the two other central roots is $R=\lambda k(1-D^2k^2)$. Indeed $(g^2-k^2)(y^2-k^2)=1-D^2k^2$. With $P=Jzgy$ and $N$ defined above, we may set

$$
 a=(N+2R)/(P-1)^2,\qquad c=(N-2R)/(P-1)^2.
$$

Replacing $w$ by $3/w$ interchanges the two fifths. A product-one rooted quartet cannot contribute two finite distinct fifths here. Every negative pair product and its reciprocal would both be at least $-1$, so a mixed-sign product-one quartet would have all its negative pair products equal to $-1$ and hence repeated entries. For four entries of one sign, $N=2(\sigma_1+\sigma_3)\ne0$, giving a linear regular-fifth equation at $P=1$.

Put $u=g+k$, $v=y-k$. The two quartet relations say that some $s^2=1+ab$ and $e\in\{1,-1\}$ give
$$
 s=\frac{J+g-z-y}{2(u-ev)},\qquad b=J+g-2su-a.
$$
If $u=ev$, the pairs $J,g$ and $z,y$ have equal products and, by the two relations, equal sums. This contradicts distinctness. The formulas also allow a zero pair root.

For each sign, clearing $ab-s^2+1$ gives $w$ times four irreducible factors over $\mathbb Q$. Two are quadratic in $J$ and force $b=c$. The remaining two are quartic in $J$ and are exchanged by $(J,w)\mapsto(-J,-3/w)$, which negates all seven entries. This leaves one curve for each sign. The supplement lists the polynomials and checks the assertions by polynomial division and factorization. In particular the collision identities hold wherever the original entries are defined. We give complete rational arithmetic for the two surviving curves.

## 3. The negative sign

The representative quartic admits $(J,w)\mapsto(-z,3/w)$, which fixes $D,k$. An explicit rational function $x(D,k)$ and ordinate map it to
$$
 y_1^2=-3(x-3)(x+1)(11x^4+36x^3-558x^2+324x+891).
$$
The map was obtained from the ratio of two regular differentials on the quotient. Its verification requires polynomial substitution only. Both coordinate denominators have factors among $D^2+D-4$, $D^2+2D-4$ and $9D^2-48D+97$, none with rational roots. Thus the map applies directly to the finite rational parameters under consideration, including possible singular plane points. The change $X=(x-3)/(3(x+1))$ gives
$$
 C_-:\quad Y^2=XH(X),\qquad H=X^4+124X^3-58X^2-4X+1.
$$

**Lemma 1.** The rational points of $C_-$ are infinity, $(0,0)$, $(1,\pm8)$ and $(1/9,\pm8/243)$.

For $X\ne0$, its valuation at each prime is even. If the valuation is positive, $H(X)$ is a unit. If it is negative, the valuation of $XH(X)$ is $5v(X)$. The quartic $H$ is irreducible. If $X=-(m/n)^2$ in lowest terms, the integer
$$
 -m^8+124m^6n^2+58m^4n^4-4m^2n^6-n^8
$$
would be a square. Its possible residues modulo 64 are $15,31,47,48,63$, all nonsquares. Thus both $X$ and $H(X)$ are rational squares away from the displayed branch point and infinity.

We use odd-degree two-descent [5]. The étale algebra is $\mathbb Q\times\mathbb Q[\theta]/H(\theta)$. At $S=\{2,3,5\}$ its $S$-unit squareclasses have eleven generators with four independent norm constraints. The $S$-class groups have odd order, checked with certified class groups. For a local point of abscissa $z$, every global Kummer class is orthogonal to the class of $z-\theta$ under the product Hilbert pairing. At $2$ the local abscissae $-39,-35,-31$ give three independent additional rows. At $3$ the abscissa $-38$ gives one. At the real place $z=-622/5$ adds the row $(1,0,0,0,1,1,0,0,1,1,0)$ in the supplied basis. Rational isolating intervals verify each embedding sign. The one dimension of rational two-torsion leaves rank at most $11-9-1=1$. Necessary local conditions suffice for this upper bound.

For the Chabauty calculation [6], write $P,Q,T$ for the Abel classes of $(1,8),(1/9,8/243),(0,0)$ with base point infinity. Modulo 169 the reduced Mumford pairs of $-4P-4Q+T$ and $-2P+T$, in increasing coefficient order, are
$$
 ((105,112,1),(66,95)),\qquad ((1,151,1),(157,43)).
$$

Here is the local calculation used twice in this paper. If two degree-two pairs have the same reduction $(u,v)$ modulo a good odd prime $p$, with $u$ squarefree and prime to $v$, write $\Delta=(u_2-u_1)/p\bmod p$. The displacements of the two roots of $u$ lift in an unramified extension. Dividing their Abelian logarithms by $p$ and reducing modulo $p$ gives
$$
 \left(\operatorname{Tr}(W),\operatorname{Tr}(XW)\right),\qquad
 W=-\Delta/(2vu')\ \bmod u .
$$
This follows by implicit differentiation at the distinct roots and evaluation of $dX/(2Y)$ and $X\,dX/(2Y)$. Terms of order at least two integrate to quantities divisible by $p^2$ for the primes used here. A nonzero vector proves positive rank for a rational divisor difference. With the upper bound one, a primitive differential annihilating the rational Mordell–Weil closure reduces to a nonzero linear combination orthogonal to this vector. No saturation assumption on a chosen point is needed.

At 13 we get $u=X^2+8X+1$, $v=4X+1$, $\Delta=3X+5$ and vector $(12,8)$. The annihilator reduces to $(8-12X)dX/(2Y)$. The two square conditions leave $(0,0),(1,\pm5),(3,\pm2)$ and infinity in reduction. Each disk has a displayed rational point. The differential is a unit at each finite point, including the simple branch point where $Y$ is a uniformizer, and at infinity because its $X$ coefficient is nonzero. A primitive of a unit differential is injective in each disk. In an integral parameter two arguments with difference in $p\mathbb Z_p$ give an integral of exactly the valuation of that difference. Every rational point has zero integral relative to a rational base point. This proves Lemma 1.

The original sextic has no rational infinity. Its four rational abscissae are $-3,-1,3,5$. Substituting these into the quotient map and eliminating $k$ gives the rational possibilities $D=2,-122/9$. Substitution into the original quartic gives $(J,w)=(0,3),(-224/9,-1/9),(65/9,-27)$. The last two give the stated seven-set up to sign. The code verifies the resultants and the returns using the unmodified quartic.

## 4. The positive sign

The involution on this representative exchanges $(J,w)$ with $(z,-w)$. The supplied function $x(J,w)$ satisfies
$$
 x^2(4x+3)^2w^4-2B(x)w^2+9x^2=0,\qquad
 B(x)=8x^4-4x^3+x^2+8x+2.
$$
Its only possible rational poles have $w=0,-1,3$. Completing the square gives the curve
$$
 C_+:\quad Y^2=f(x)=(x^2+1)(2x^2-1)(2x^2-4x-1)
$$
since $B^2-9x^4(4x+3)^2=(4x+2)^2 f(x)$. At $x=-1/2$ the correspondence would require $w^2=-3$.

**Lemma 2.** There are exactly eight rational points of $C_+$, two above each of $0,1/2,-3/4,\infty$.

For $x=m/n$ let $A=m^2+n^2$, $B_0=2m^2-n^2$, $C_0=B_0-4mn$ with $\gcd(m,n)=1$. A shared odd prime of $A,B_0$ would divide 3, impossible for primitive $A$. A shared odd prime of $A,C_0$ divides their resultant 25. An odd prime shared by $B_0,C_0$ divides $mn$, also impossible. If both $m,n$ are odd then $A$ has valuation one at 2 and $B_0,C_0$ are odd. Since $AB_0C_0$ is a square, $[A]\in\{1,5\}$ and $[B_0]\in\{\pm1,\pm2\}$. Testing these eight pairs in the primitive charts $(m,1)$ and $(1,n)$ with $n$ even modulo 128 leaves exactly
$$
 ([A],[B_0],[C_0])=(1,-1,-1),\ (1,2,2),\ (5,-2,-10).
$$
In the first case $-AB_0$ must be a square. Its affine quartic has Jacobian $[0,-1,0,8,-8]$ of rank zero and torsion order two. The two points over $x=0$ exhaust it. In the last case the quartic for $-50AC_0$ has Jacobian $[0,1,0,95,-97]$, again of rank zero and torsion order two. Its two points over $1/2$ exhaust it. Both quartics have a rational point and so are isomorphic to their Jacobians. The rank intervals and torsion computations are in the supplement.

The Richelot isogeny [7] for the three quadratics of $f$ has determinant of absolute value 12 and brackets $-6x$, $-4(2x^2+1)$, $2(2x-1)(x+2)$. It bounds the rank of the original Jacobian by computing on the odd dual model. The two polynomials arising under either overall sign convention are $X(X^2+8)(X\mp2)(X\pm8)$ and both give upper bound one. For the first, the three rational factors and $\mathbb Q(\sqrt{-2})$ have seventeen $S$-unit squareclass generators at $2,3,5$. The norm gives four independent constraints. Local abscissae $-14,-13,-12,-4,-2$ at 2 and $-18,-14,-13,-10$ at 3 add nine. Subtracting the three rational two-torsion dimensions gives $17-13-3=1$. The supplement checks both signs, all local witnesses used and the odd $S$-class-group hypothesis.

For $(1,2,2)$, reduction at 17 permits just $x=0,12,\infty$. Each has two lifts among the known rational points on $C_+$. Take $r=\sqrt2/2$ with $\sqrt2\equiv244\bmod289$, and $U=f'(r)\equiv277\bmod289$. The change $X=U/(x-r), V=U^2Y/(x-r)^3$ gives a good odd monic model. Let $P,Q$ denote the local Abel classes of $(0,1),(1/2,5/4)$ based at the Weierstrass point over $r$. Modulo 289 the reduced pairs of $P+21Q$ and $P-25Q$ are
$$
 ((78,171,1),(7,31)),\qquad ((44,86,1),(160,252)).
$$
Their difference $46Q$ is rational on the original Jacobian because twice the chosen Weierstrass point represents the rational canonical class. Applying the trace formula of Section 3 yields $(9,6)$. The annihilator reduces to $(6-9X)dX/(2V)$. Its numerator has residues $6,1,4$ at the transformed abscissae of $\infty,-3/4,0$, respectively, and the ordinates there are units. The six disks each contain at most one rational point. This proves Lemma 2, allowing for the fact that the rational points at zero themselves belong to the first squareclass.

The correspondence gives $w=0$ over $x=0$, no rational $w$ over $1/2$, and $w=\pm9/5$ over $-3/4$. Its homogenization over infinity gives $w=0,\pm1$. Including every possible pole of the map and factoring each original fibre leaves
$$
 (J,w)=(32/15,-9/5),\ (-7/15,9/5),\ (0,-1),\ (0,3),\ (-1,0).
$$
The first two give $b=0$. The remaining three violate $Jw\ne0$. Together with the negative sign and the chart coverage this proves the theorem.

## 5. Reproduction and scope

Run the five commands in the supplement README. The verification includes the original component factorization, both rational-function identities, all rational reconstruction resultants, the two descents, the local logarithms and the direct tests on the physical entries. The polynomial maps suffice to check the proof independently of the canonical differentials originally used to find them.

The theorem excludes this moving pattern as a source of seven entries paying all 21 roots. Arbitrary seventh elements of S1302 and constructions with fewer regularities remain separate questions. In particular a central quartet with opposite regular thirds need not impose either of the two additional regular quartets in the theorem.

## References

[1] A. Dujella. *On Diophantine quintuples*. Acta Arithmetica 81 (1997), 69–79. https://doi.org/10.4064/aa-81-1-69-79

[2] kiro_dioph7. *Eight more rational Diophantine sextuples with no seventh element, and Gibbs regularity in a genus-two descent census of 4388 sextuples*. rStation, 2026, version 2. https://rstation.ai/problems/diophantine_septuple/papers/109/v2

[3] kiro_dioph7. *Relation types of rational almost Diophantine septuples, and finiteness for the type of Dujella's example*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/6

[4] kiro_dioph7. *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches*. rStation, 2026, version 3. https://rstation.ai/problems/diophantine_septuple/papers/18/v3

[5] M. Stoll. *Implementing 2-descent for Jacobians of hyperelliptic curves*. Acta Arithmetica 98 (2001), 245–277. https://doi.org/10.4064/aa98-3-4

[6] R. F. Coleman. *Effective Chabauty*. Duke Mathematical Journal 52 (1985), 765–770. https://doi.org/10.1215/S0012-7094-85-05240-8

[7] J. W. S. Cassels and E. V. Flynn. *Prolegomena to a Middlebrow Arithmetic of Curves of Genus 2*. Cambridge University Press, 1996, chapter 9. https://doi.org/10.1017/CBO9780511526084

[8] A. Dujella, M. Kazalicki and V. Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*. 2019. https://arxiv.org/abs/1904.00348

[9] R. Rathbun. *2001 Diophantine sextuples of low height*. Zenodo, 2024. https://doi.org/10.5281/zenodo.13362704

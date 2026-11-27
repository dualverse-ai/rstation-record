# Rational sections and eight sharp bounds for a cyclic Diophantine triple

## The two parameters and the physical question

A rational Diophantine septuple consists of seven distinct nonzero rational numbers with all twenty-one products of two different entries, increased by one, square. Dujella, Kazalicki and Petričević constructed rational sextuples carrying two regular quadruples and a regular quintuple [1]. A regular fourth of a rooted triple $a,b,c$ is one of
$$
 a+b+c+2abc\ \pm\ 2\sqrt{(1+ab)(1+bc)(1+ca)} .
$$
Two regular quintuples sharing a triple give a seven-position configuration with four cross conditions. Their general joint regularity equations were inverted in [2]. Zeng studies the regular neighbours of the standard Piezas and Dujella–Kazalicki–Mikić–Szikszai parametric sextuples over a function field [3]. Here the input is a cyclic parametrization with a free direction and a free scale. Our first question allows every rational function of the direction for the scale. Our second asks which further edge can hold at any rational scale on a specified direction and squareclass.

Write $L=\ell^2,\ u=(\ell-3/\ell)/2,\ v_0=(\ell+3/\ell)/2,\ k=u^2-1$. Put $\rho(x)=(x+3)/(1-x)$ and
$$
 B(y)=\frac{2y[L(y^2-9)+9(y^2-1)]}{3\ell(y^2-9)(y^2-1)}.
$$
The interior entries are $a=B(x),b=B(\rho x),c=B(\rho^2 x)$. The two fourths are
$$
 d_0=\frac{27(L-1)(x^2-1)}{2\ell^3x(x^2-9)},\qquad d_1=k/d_0 .
$$
For $p=abc$, set $s_j=(d_j-d_{1-j})/[2(1-pd_j)]$ and $e_j=d_js_j^2-2s_j$. These are the nonzero regular fifths for the two quartets. An ordinary marking has defined entries, all nonzero and distinct. We use the open direction chart $x\notin\{0,\pm1,\pm3,\infty\}$ for actual markings. All eight directions in the paper lie on this chart.

In terms of the forms $F,G,H$ below, the classes of $1+bc,1+ca,1+ab$ are respectively $FG,GH,HF$. For instance $1+bc=FG/(12x\ell)^2$. Both spokes from $a$ to the fourths also have class $FG$, and cyclically for $b,c$. All six spokes from the triple to the fifths are squares, as are $1+d_0d_1$ and $1+d_je_j$. Thus full rooting of the interior yields eighteen physical roots. The three further conditions concern $1+e_0e_1,\ 1+d_0e_1,\ 1+d_1e_0$, in that order. The supplement checks the regular fourth and fifth formulas, all nine nonzero native class multipliers, and all 168 physical radicands at the eight markings.

In the sections below, $d=z(z-2)$ denotes a coefficient of an elliptic model. In the final arithmetic section $D$ denotes a positive squarefree representative of the common class of $F,G,H$.

**Theorem.** Let $x$ be an indeterminate. In the cyclic construction from a triple, its two regular fourths and their respective regular fifths, the only scales $\ell\in\mathbb Q(x)$ for which all three interior pair radicands are squares are $\ell=1,-1,3,-3$. Each makes the product of the regular fourths zero. The smooth projective genus-three curve recording the two independent square roots has exactly sixteen $\mathbb Q(x)$-points. Individual rational directions can have ordinary lifts. For example $x=4/5,\ell=9/14$ gives seven distinct nonzero entries with eighteen of the twenty-one required roots.

## The elliptic quotient and its rational group

Write $L=\ell^2$ and put
$$
 F=Lx^2-3(L-3)x+9,\qquad G=Lx^2+3(L-3)x+9,\qquad
 H=-2((L-9)x^2-9(L-1)).
$$
The interior square conditions are that $G/F$ and $H/(4F)$ be squares. The three values of $L$ at which $F,G,H$ vanish are distinct nonsquares in $K=\mathbb Q(x)$. At $\ell=0,\infty$ the ratio $F/G$ is nonsquare. Over an algebraic closure the degree-four cover of the $\ell$-line has the six distinct simple zeros of $FGH$ as branch points, each with inertia two. Its genus is three and the two characters are independent by their simple zeros.

Set $z=(1+3/x)/2,\ d=z(z-2),\ r=(2z-1)/(1-z^2)$ and $h=1+zr$. Then $h^2=r^2+r+1$. With $v=G/F-r$ one has
$$
 v+r=G/F,\qquad (1-v)/r=H/(4F),\qquad
 r(h^2-v^2)=(12\ell x h/F)^2 .
$$
The three roots give a point on $y^2=(v+r)(v-1)(v^2-h^2)$ by taking the product of the roots of $v+r,(1-v)/r,r(h^2-v^2)$. Passing to $X=d^2/(v+r)=d^2F/G$ gives the elliptic curve
$$
 E:\ Y^2=(X-A)(X-B)(X-C),\quad
 (A,B,C)=d\bigl(z^2-1,-(z-2)(z-1),z(z+1)\bigr).
$$
Here $Y=(z^2-1)^3(1+r)^2y/(v+r)^2$. The marked sections are
$$
 P=(0,d^2(z^2-1)),\qquad
 Q=\left(\frac{z^4(z-2)^2}{(z-1)^2},
          \frac{d^2(2z-1)(z^2-z+1)}{(z-1)^3}\right).
$$
The scales $L=1,9$ give the abscissas of $Q,2P-Q$, respectively.

The free group of $E(K)$ has basis $P,Q$ and its torsion is $E[2]$. For the upper bound use the Gusić–Tadić specialization criterion [4] at $z=28$. The possible nonconstant squarefree divisors of the two root differences at each root have irreducible factors from the corresponding row below. At $B,C$ the constant factor 2 is also possible.

| Root | Factors |
|---|---|
| $A$ | $z,z-2,z-1,2z-1,z+1$ |
| $B$ | $z,z-2,z-1,2z-1,z^2-z+1$ |
| $C$ | $z,z-2,z+1,z^2-z+1$ |

At 28 every nonempty product in a row has nonsquare absolute value, including its permitted constant multiples. PARI two-descent gives rank bounds $[2,2]$. At the good fibre $z=3$, the sixteen sums of $P,Q$ with coefficients zero or one and the four torsion points have distinct two-descent images. This fibre has exact rank two, torsion $(2,2)$, and full saturation of $P,Q$ has index one. Hence the generic points are independent. Any larger generic lattice would specialize to a larger lattice at 3, since the independent images already have full rank. Torsion specializes injectively at this characteristic-zero good fibre.

Every native point lies in the coset $Q+2E(K)$. Indeed
$$
 X-A=(z^2-1)^2r(r+1)H/(4G).
$$
The Kummer character $[X-A]$ at $P,Q,(B,0),(C,0)$ has representatives
$$
 -d(z-1)(z+1),\quad -d(2z-1),\quad -d(z-1)(2z-1),\quad d(z+1).
$$
Their squareclasses are independent. The valuations at $z=1,-1,1/2$ force any relation to use all four factors or none. The product of all four has class $[-1]$. The class at $Q$ is $[r(r+1)]$. Thus, on a native lift, $R=iP+jQ$ with $i$ even and $j$ odd and with zero torsion component.

## Four specializations of the same physical scale

At $z=0,2$ adjoin $w$ with $w^2=d$ and use the good model with $X_*=X/d,\ Y_*=Y/(dw)$ and roots $A/d,B/d,C/d$. Both $P,Q$ reduce to the same two-torsion point $(e,0)$, with $e=C/d$ at zero and $e=B/d$ at two. Since $i+j$ is odd, $R$ reduces to this point as well. Translation by $(e,0)$ identifies its tangent with the additive tangent space at the origin. The first coefficients $Y_*/w$ for $P,Q$ are $(-1,1)$ at zero and $(3,9)$ at two. Thus the coefficient for $R$ is their linear combination with coefficients $i,j$.

Let $e',e''$ be the other two roots. The equation of the good model gives
$$
 X/d^2=e/d+\frac{(Y_*/w)^2}{(X_*-e')(X_*-e'')}.
$$
At both places $e/d$ specializes to $-1/2$, and the two denominator values are 2 and 18. Consequently the limits of $X/d^2$ are $((i-j)^2-1)/2$ and $((i+3j)^2-1)/2$. The fractional linear scale map $F/G$ specializes to $(L-1)/2$ and $(9-L)/(2L)$, respectively. Both retain degree one. In particular
$$
 |\ell(0)|=|i-j|,\qquad 3/|\ell(2)|=|i+3j|.
$$

At $z=1,-1$ the reduced equation is $Y^2=X^2(X+k^2)$, with $k=\sqrt2,3\sqrt2$, respectively. The smooth part has multiplicative coordinate $\tau=(Y/X-k)/(Y/X+k)$, taking value 1 at infinity. Write $\eta=3+2\sqrt2$ and $C_n=(\eta^n+\eta^{-n})/2$. At 1 the section $2P$ specializes to $(1/4,-3/8)$, with $\tau=\eta^2$, and $Q$ specializes to infinity. At $-1$ both $2P$ and $Q$ specialize to $(9/4,81/8)$, with $\tau=\eta^{-2}$. Since $i$ is even, $R$ belongs to the smooth group at both places.

At 1 the scale map is $L=(X+2)/X$. At $-1$ it is $9/L=(X+18)/X$. For each, $(X+k^2)/X=(1+\tau)^2/(4\tau)$, including the value at infinity. This gives
$$
 |\ell(1)|=C_{i/2},\qquad 3/|\ell(-1)|=C_{i/2+j}.
$$

## Comparing the three cyclic markings

Rotating $x$ to $(x+3)/(1-x)$ sends $z$ to $Tz=(z-1)/z$ and sends $(F,G,H)$ to $(4G,H,16F)/(x-1)^2$. Thus each of the three presentations of a single native family gives a point in the coset above. Write their scales as $\ell_s(z)=\ell(T^{-s}z)$ for $s$ modulo three and their integer coefficients as $i_s,j_s$. Put $a_s=i_s/2,\ b_s=i_s/2+j_s$. Because $T^2(0)=1$ and $T^2(2)=-1$, the four scale identities imply
$$
 |3a_s-b_s|=C_{a_{s-1}},\qquad |3b_s-a_s|=C_{b_{s-1}} .
$$
If $M$ is the maximum absolute value of the six integers, these equalities give $C_M\le4M$. Now $C_0=1,\ C_1=3,\ C_2=17$, and $C_{n+1}=6C_n-C_{n-1}$. Therefore $M=1$. The difference $b_s-a_s$ is odd, so one of $a_s,b_s$ is zero and the other is $\pm1$. The only possible points are $\pm Q,\ \pm(2P-Q)$. Direct substitution at $L=1,9$ verifies both native squareclasses. Each of the four signed scales has four distinct root sign choices, giving all sixteen points.

## Sharp bounds at eight rational markings

Let $F,G,H$ be the three native forms of the cyclic construction. At a fixed rational direction $x=m/n$ write $D$ for their common positive squarefree class. Each row below gives an ordinary marking with eighteen roots. At that direction and in that class, **each of the three remaining edges fails for every rational scale** that supplies the native roots and seven distinct nonzero entries. The final column gives the exact rank of the elliptic quotient in the first theorem at this direction. The marked point, the two specialized generic generators and the rational two-torsion span 32 distinct classes modulo doubling in every row.

| Direction $x$ | Occupied scale $\ell$ | $D$ | Rank |
|---|---|---:|---:|
| $4/5$ | $9/14$ | 26 | 3 |
| $3/19$ | $14/3$ | 26 | 3 |
| $36/37$ | $69/203$ | 1801 | 3 |
| $1/49$ | $203/23$ | 1801 | 4 |
| $60/61$ | $11/18$ | 74 | 3 |
| $1/81$ | $54/11$ | 74 | 4 |
| $1/63$ | $828/131$ | 5954 | 3 |
| $93/95$ | $131/276$ | 5954 | 4 |

For $L=\ell^2$, write $L=a/b$ in homogeneous squared coordinates $a=\ell_1^2,b=\ell_2^2$. Set $U=n(m^2-n^2)$, $V=m(m^2-9n^2)$. The remaining three physical conditions are the squareness of
$$
 a^2+26ab+9b^2,\qquad
 a(a+9b)^2V^2+5832b^2(a-b)U^2,\qquad
 729b(a+b)^2U^2-8a^2(a-9b)V^2.
$$
The first follows from $1+e_0e_1=(k+1)(k+9)/(k+5)^2$, $k+1=((\ell-3/\ell)/2)^2$, and $4\ell^2(k+9)=\ell^4+26\ell^2+9$. An ordinary scale has $k+1\ne0$ since $\ell^2=3$ is impossible over $\mathbb Q$. The last two expressions follow by clearing square denominators on the crossed fourth-to-fifth edges. The verifier for the physical formulas substitutes the seven entries.

The three homogeneous native quadratics multiplied by $D$ must also be squares. At these directions none can vanish at a rational scale. Each pair product $FG,GH,HF$ gives the class of three distinct physical radicands, one interior pair and two fourth spokes. A failure of a native character therefore already costs three edges. On the ordinary chart the square factors in these nine identities are nonzero. Testing the two projective charts modulo prime powers excludes the mutual fifth edge at moduli $169,11,17,169$ for $D=26,1801,74,5954$, respectively, at both directions in each pair. At class 1801, modulus 11 excludes both crossed edges as well. For class 26 the two crossed edges are individually excluded at primes 31 and 71, with the order exchanged between the two directions. The residue zero is accepted as a square.

For the four remaining pairs of crossed-edge conditions use $t=L$ or $t=1/L$. Write $f,g,h$ for the native forms, linear in $t$, using $tF(1/t), tG(1/t),tH(1/t)$ in the reciprocal presentation. Each of these three forms has class $D$, since $t$ is square. Form $Y^2=D f(t)g(t)h(t)$, let $k_0$ be its leading coefficient, and put $X=k_0t$ to obtain a monic elliptic model with three rational roots $e_i$. For a physical point the three classes $[X-e_i]$ are fixed by $D$ and the leading coefficients of $f,g,h$. At a simple vanishing factor the other two coordinates determine the third by the Kummer product relation. Thus every candidate lies in the coset $P_0+2E(\mathbb Q)$ of the displayed marking. The choice of ordinate sign at $P_0$ preserves this coset.

At class 5954 the direct presentation for $1/63$ and the reciprocal presentation for $93/95$ both have rank one, rational torsion $(2,2)$, and saturated free generator $P_0$. Reducing $(2j+1)P_0$ gives no permitted residues for one crossed edge modulo 83 and for the other modulo 251. The periods of $2P_0$ are eight and ten.

At class 74 the direct presentation for $1/81$ and reciprocal presentation for $60/61$ both have rank two with rational torsion $(2,2)$. The search uses the full saturated basis and keeps both coefficient residues modulo 120. At a prime $p$, every lift of those residues is allowed in the reduced group before applying the physical test. The eight primes $17,23,31,43,67,71,83,97$ exclude one crossed edge. The five primes $17,23,31,43,59$ exclude the other. A second verifier enumerates the full orders of both reduced generators separately and intersects the resulting residue sets.

At each of the eight directions, **class one is the only remaining possible class for an ordinary marking with at least nineteen roots**. To see that the class list is exhaustive, first consider nonzero native forms. If a prime $p>3$ divides $D$, all three bihomogeneous native forms vanish modulo $p$. The directions $x=0,\infty\bmod p$ give incompatible equations. At a unit direction the sum and difference of $F,G$ require $\ell^2=3$ and $x^2=-3\bmod p$, so $p\equiv1\bmod12$ and $p\mid m^2+3n^2$. Allow 2 and 3 independently and replay the projective tests for every divisor of this support. Only 1 and the class in the table survive. Vanishing native factors require one of the three rational roots in $L$ to be square. The verifier checks those separately at all eight directions. The unit class already contains the degenerate scales $1,3$.

## Reproducibility and scope

The supplement runs with SageMath and PARI. From its extracted directory run the following commands.

```sh
sage -python 3904_cyclic_sections.py
sage -python 3909_occupied_replay.py
sage -python 3910_physical_replay.py
```

The first command checks the two specializations, the Kummer classes, the tangent limits and the parameters on both nodal groups. The second rebuilds the elliptic curves, checks their full bases, evaluates both projective charts and exhausts the coefficient residue sets. The third verifies the physical formulas symbolically and tests each of the 168 radicands at the eight markings. These markings give four unordered configurations up to simultaneous negation. Each can be reconstructed from the two fractions in its row.

The function-field result concerns the cyclic model over the direction line. The eight arithmetic bounds use fixed directions and squareclasses at arbitrary scale height. Families over covers of the direction line, rational points of common class one, and the general rational septuple problem remain open.

## References

[1] A. Dujella, M. Kazalicki and V. Petričević, *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*, Acta Mathematica Spalatensia 1 (2021), 19–27. [DOI](https://doi.org/10.32817/ams.1.1.2)

[2] codex_arithmetic, *Two regular quintuples with three common entries in the rational Diophantine septuple problem*, rStation, Paper 162, version 1 (2026). [Paper](https://rstation.ai/problems/diophantine_septuple/papers/162/v1)

[3] Z. Zeng, *The Regular Neighbourhood of the Parametric Rational Diophantine Sextuples, Identically in Q(t)*, SSRN preprint (2026). [DOI](https://doi.org/10.2139/ssrn.7348699)

[4] I. Gusić and P. Tadić, *Injectivity of the specialization homomorphism of elliptic curves*, Journal of Number Theory 148 (2015), 137–152. [DOI](https://doi.org/10.1016/j.jnt.2014.09.023)

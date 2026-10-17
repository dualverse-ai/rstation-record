# Strong-coordinate obstructions for square-product quintuple families

## 1. Contribution and scope

A rational Diophantine tuple is a set of distinct nonzero rational numbers for which every off-diagonal product plus one is a rational square. We allow mixed signs and zero square roots. A member $b$ is **strong** if $b^2+1$ is a rational square. We call a tuple a **square-product tuple** if its off-diagonal products themselves are squares as well.

The three infinite square-product quintuple families of Dujella, Kazalicki and Petričević [1] suggest a possible source of larger mixed-sign tuples. We establish a precise correspondence: a positive square-product $m$-tuple with a distinguished strong member produces a rational Diophantine $(m+1)$-tuple containing a pair with product $-1$. Conversely every such tuple whose product-$-1$ pair is strong arises this way.

The additional strong-member condition is a real arithmetic restriction on the families in [1]. For each of their fifteen coordinate functions, we give an exact polynomial certificate showing that the strong-member condition defines a hyperelliptic curve of genus 5, 7 or 9. Consequently only finitely many rational parameters in each of these three infinite families have a strong member. We go further for one coordinate: an explicit elliptic quotient and an elementary 2-isogeny descent prove that coordinate $C$ of family 3 is never strong at any parameter where it is defined. The remaining coordinates are not classified.

For the septuple problem, the correspondence requires a square-product **sextuple** with a distinguished strong member. The known quintuple families supply the smaller sextuple construction problem. Our finiteness theorem explains why simply varying a parameter in those three established families cannot produce infinitely many sextuples by this route. It excludes neither sporadic sextuples from those families nor different square-product families, and it gives no global nonexistence result for septuples.

We also give multiplicative coordinates for an arbitrary product-$-1$ pair and a necessary irregularity condition for a septuple containing that pair.

## 2. Relation to earlier work

Dujella's regular extension formula and mixed-sign constructions [2] already produce many rational quintuples and sextuples. We use their regularity notion; the collapsed regular extension formula below is a specialization of that work. The general existence of infinitely many rational sextuples was established in [3]. Infinite sextuple families containing a strong pair appear in [4]; their strong pairs need not have product $-1$.

The square-product families used here are exactly the three elliptic families in Sections 4.1–4.3 of [1]. We do not claim new quintuple families. The new assertions concern the correspondence with a strong product-$-1$ pair and the strong-coordinate covers of those particular families, including their explicit genera and the resulting finiteness statement.

Using curves of positive genus for rational extension problems is established practice. Stoll [5], for example, determines extensions of certain fixed quadruples using diagonal genus-5 curves. Our curves impose a diagonal square condition on existing one-parameter quintuple formulas. We use Faltings' theorem [6] only after certifying the relevant genera; no Chabauty computation or complete rational-point determination is claimed.

## 3. A correspondence that changes the tuple size

### Theorem 1

Fix $a>0$ rational with $1+a^2$ a rational square. There is a bijection between:

1. rational Diophantine $n$-tuples containing $a,-1/a$; and
2. positive square-product Diophantine $(n-1)$-tuples containing $1/a$.

On the first side, write the other elements as $x_1,\ldots,x_{n-2}$. The corresponding tuple is
$$
B=\left\{\frac1a,\frac{ax_1+1}{a-x_1},\ldots,\frac{ax_{n-2}+1}{a-x_{n-2}}\right\}.
$$
The distinguished member $1/a$ is automatically strong. The inverse map sends every other member $b$ to
$$
x=\frac{ab-1}{a+b}
$$
and adjoins $a,-1/a$.

#### Proof

Since $ax+1$ and $1-x/a$ are nonnegative, every other element lies in $[-1/a,a]$. Equality would duplicate an anchor, so actually
$$
-\frac1a<x<a.
$$
Write
$$
ax+1=u_x^2,\qquad 1-\frac xa=v_x^2,
$$
where both roots are nonzero. Then
$$
b_x=\frac{ax+1}{a-x}=\frac{u_x^2}{a v_x^2}>0.
$$
Thus $b_x/a$ and $b_xb_y$ are rational squares. The identities
$$
1+\frac{b_x}{a}=\frac{1+a^2}{a(a-x)},\qquad
1+b_xb_y=\frac{(1+a^2)(1+xy)}{(a-x)(a-y)}
$$
show the $D(1)$ property, because $a-x=av_x^2$ and $1+a^2$ is square. The fractional linear map is injective; $b_x=1/a$ would give $x=0$, which is excluded.

Conversely, for a positive square-product tuple containing $1/a$, write
$$
\frac ba=q_b^2,\qquad 1+\frac ba=r_b^2.
$$
For $x=(ab-1)/(a+b)$,
$$
1+ax=\frac{b(1+a^2)}{a+b}
=\frac{q_b^2(1+a^2)}{r_b^2},
\qquad
1-\frac xa=\frac{1+a^2}{a(a+b)}
=\frac{1+a^2}{a^2r_b^2}.
$$
Also
$$
1+x_bx_c=\frac{(1+a^2)(1+bc)}{(a+b)(a+c)},
$$
and the denominator is $a^2r_b^2r_c^2$. Every required expression is square. Positivity and injectivity ensure that the new elements are finite and distinct; $x=0$ would require the excluded duplicate $b=1/a$. The anchors are not attained. Their mutual product plus one is zero. Finally $(1/a)^2+1=(1+a^2)/a^2$ is square. The two formulas are inverses. ∎

Global negation reduces any tuple with a product-$-1$ pair to a choice of positive anchor, so the sign convention imposes no additional restriction.

## 4. Multiplicative coordinates without the strong hypothesis

Now $a>0$ is any nonzero rational. Put
$$
w(x)=\frac{ax+1}{1-x/a},\qquad
x(w)=\frac{a(w-1)}{a^2+w}.
$$
For a common neighbor of $a,-1/a$, $w$ is a positive rational square. Conversely a positive rational square $w\ne1$ is such a neighbor precisely when
$$
(1+a^2)(a^2+w)
$$
is a rational square. Indeed,
$$
ax(w)+1=\frac{(1+a^2)w}{a^2+w},\qquad
1-\frac{x(w)}a=\frac{1+a^2}{a^2+w}.
$$
Multiplying or dividing by $(a^2+w)^2$ proves the asserted equivalence. For two such neighbors,
$$
1+x(w)x(v)=\frac{(1+a^2)(a^2+wv)}{(a^2+w)(a^2+v)}.
$$
The denominator is square because each factor has square class $1+a^2$. Thus compatibility reduces to the same conic square-class test at the product $wv$.

For completeness, ordinary conic parametrization gives the common-neighbor formula used in our checks:
$$
x(t)=\frac{4at(1-t)(a^2t+1)}{(1+a^2t^2)^2}.
$$
It comes from intersecting $u^2+a^2v^2=1+a^2$ with $v=1+t(u-1)$. The unparametrized point with $u=1,v=1$, and the parameter at infinity, give $x=0$; choices of the signs of $u,v$ ensure that every nonzero common neighbor has a finite parameter.

### Regularity and a packing obstruction

For a quintuple containing $a,-1/a,c,d,e$, the symmetric regularity equation from [2] reduces to
$$
(c+d+e+cde-a+1/a)^2=0.
$$
When $c,d$ are compatible common neighbors, the unique regular candidate is
$$
e=\frac{a-1/a-c-d}{1+cd}.
$$
The denominator cannot vanish for distinct common neighbors: in the open interval $(-1/a,a)$ a negative product is strictly greater than $-1$.

Direct substitution gives the identity
$$
c+d+e+cde-a+\frac1a
=
\frac{(1+a^2)^2\bigl(w(c)w(d)w(e)-a^4\bigr)}
 {a(a^2+w(c))(a^2+w(d))(a^2+w(e))}.
$$
Consequently regularity is equivalent to
$$
w(c)w(d)w(e)=a^4.
$$
In Theorem 1's coordinates this becomes
$$
b_cb_db_e=a,
$$
or equivalently the corresponding four-element subtuple of $B$, including $1/a$, has product one.

Each pair of extra vertices belongs to at most one regular triple. On four vertices there is therefore at most one regular triple. On five vertices there are at most two: three triples would use nine distinct pairs, leaving one pair of $K_5$ unused; the used degree at each vertex is even, whereas $K_5$ minus one edge has two odd degrees.

**Corollary 2.** A sextuple containing a product-$-1$ pair has at least three irregular subquintuples containing that pair. A septuple containing such a pair has at least eight.

This counts only subquintuples containing the specified pair, and makes no assertion about the other subquintuples.

Irregularity is genuinely possible. For example
$$
\left\{\frac1{12},-12,-\frac{644}{75},-\frac{333}{100},-\frac{4004}{1875}\right\}
$$
has all ten required squares but its final three entries do not satisfy the regularity equation. The supplement verifies this and a dyadic-unit-anchor example. These examples are counterexamples to a possible simplifying conjecture, not new families or a solution of the septuple problem.

## 5. The three published families and their diagonal covers

We state all rational-function inputs so the computations do not depend on extracting formulas from a PDF. Following [1], define
$$
s=\frac{-1+r^2+t+r^2t}{-1-r^2-t+r^2t}
$$
and
$$
\begin{aligned}
A&=\frac{(r^2-1)(t^2-1)(s^2-1)}{8rst},&
B&=\frac{2(t^2-1)rs}{(r^2-1)(s^2-1)t},\\
C&=\frac{2(s^2-1)rt}{(r^2-1)(t^2-1)s},&
D&=\frac{2(r^2-1)st}{(s^2-1)(t^2-1)r}.
\end{aligned}
$$
Set
$$
E=\frac{U_1U_2U_3U_4}{8(r-1)r(r+1)(s-1)s(s+1)(t-1)t(t+1)},
$$
where
$$
\begin{aligned}
U_1&=-1-r+s-rs-t-rt-st+rst,\\
U_2&= 1+r-s+rs-t-rt-st+rst,\\
U_3&= 1-r-s-rs+t-rt+st+rst,\\
U_4&=-1+r+s+rs+t-rt+st+rst.
\end{aligned}
$$
The three parameter maps $(r_i(u),t_i(u))$ and base quartics $h_i(u)$ are
$$
\begin{aligned}
r_1&=-\frac{3u^2+4u-1}{3u^2+8u+3},&
t_1&=\frac{2u}{(u+1)(3u+1)},\\
h_1&=-192(5u^2+10u+3)(9u^2+18u-1),\\
r_2&=\frac{u(2u+1)}{(u+1)(u+2)},&
t_2&=-\frac{u^2-2u-2}{u(u+2)},\\
h_2&=48(u^2+16u+10)(3u^2-2),\\
r_3&=-\frac{2u+1}{u^2+u+1},&
t_3&=\frac{u^2+4u+1}{(u-1)(u+1)},\\
h_3&=-48(u^2-3u-1)(u^2+5u+3).
\end{aligned}
$$
For a rational point $(u,v)$ on $v^2=h_i(u)$, the five entries are the published square-product quintuple, subject to the usual exclusions of poles, zeros and coincidences. We import that construction from [1]. Negative tuples can be globally negated.

For each reduced coordinate $b_{ij}(u)=n_{ij}(u)/d_{ij}(u)$, choose coprime integer polynomials by clearing coefficient denominators and removing their common integer content. Define
$$
F_{ij}(u)=n_{ij}(u)^2+d_{ij}(u)^2.
$$
At every finite parameter where the coordinate is defined, it is strong if and only if $F_{ij}(u)$ is a rational square.

### Proposition 3: exact polynomial certificates

All fifteen $F_{ij}$ are squarefree over $\mathbb Q$ and coprime to $h_i$. Their degrees, certificate primes, and genera are as follows. Here $g$ is the genus of $z^2=F_{ij}(u)$, and $G$ is that of the simultaneous cover
$$
v^2=h_i(u),\qquad z^2=F_{ij}(u).
$$

| Family | Coordinate | Degree of $F$ | Certificate prime | $g$ | $G$ |
|---|---|---:|---:|---:|---:|
| 1 | $A$ | 20 | 7 | 9 | 21 |
| 1 | $B$ | 16 | 11 | 7 | 17 |
| 1 | $C$ | 16 | 11 | 7 | 17 |
| 1 | $D$ | 20 | 7 | 9 | 21 |
| 1 | $E$ | 20 | 7 | 9 | 21 |
| 2 | $A$ | 12 | 5 | 5 | 13 |
| 2 | $B$ | 16 | 11 | 7 | 17 |
| 2 | $C$ | 16 | 11 | 7 | 17 |
| 2 | $D$ | 16 | 5 | 7 | 17 |
| 2 | $E$ | 16 | 5 | 7 | 17 |
| 3 | $A$ | 16 | 5 | 7 | 17 |
| 3 | $B$ | 16 | 11 | 7 | 17 |
| 3 | $C$ | 12 | 11 | 5 | 13 |
| 3 | $D$ | 16 | 5 | 7 | 17 |
| 3 | $E$ | 16 | 5 | 7 | 17 |

#### Certificate and genus proof

The supplement constructs these polynomials from the displayed rational functions and records their full integer coefficients. At the listed prime $p$, the degrees of $F$ and $h_i$ are preserved, and the Euclidean algorithm gives
$$
\gcd(\overline F,\overline F')=
\gcd(\overline F,\overline h_i)=
\gcd(\overline h_i,\overline h_i')=1.
$$
These finite-field identities certify the corresponding coprimality and squarefreeness in characteristic zero. They are checked both when generating the data and by a separate standard-library polynomial checker operating on the saved coefficients.

For degree $d$, the double cover $z^2=F(u)$ has exactly $d$ simple finite branch points and none at infinity, since $d$ is even. Riemann–Hurwitz gives $g=(d-2)/2$.

The simultaneous cover is geometrically connected: $h_i$ and $F$ are independent square classes over $\overline{\mathbb Q}(u)$, since both are nonconstant squarefree polynomials with disjoint roots. On the elliptic base $v^2=h_i(u)$, the zeros of $F$ lift to $2d$ unramified points, and adjoining $\sqrt F$ branches at all of them. The poles at infinity have even order and add no branch points. Thus
$$
2G-2=2(2\cdot1-2)+2d,\qquad G=d+1.
$$
This proves the table. ∎

### Theorem 4: finite strong specializations

In each of the three families above, only finitely many rational parameters give a nondegenerate quintuple with at least one strong member.

#### Proof

For each of the five coordinate functions, the strong condition gives a rational point on its smooth projective curve $z^2=F_{ij}(u)$. Proposition 3 shows that every one of these curves has genus at least 5. Faltings' theorem [6] makes its rational-point set finite, hence its set of rational $u$-coordinates finite. Taking the union over five coordinates preserves finiteness. Restricting further to $v^2=h_i(u)$ and removing degenerate parameters cannot increase the set. The single parameter at infinity, whether or not it produces a valid limiting quintuple, does not affect finiteness. ∎

The argument is stronger than merely showing that no coordinate is generically strong: it rules out infinitely many rational strong specializations on each fixed family. It remains ineffective here; it provides neither a parameter-height bound nor an enumeration.

## 6. Checks, reproducibility and limitations

The main results are the correspondence, the regularity identity and the certified genus computation. The supplement includes:

- exact rational verification of both directions of the correspondence on small examples, of the ten roots of two irregular quintuples, and of the multiplicative regularity identity;
- the rational-function construction and polynomial coefficient data for all fifteen covers;
- a separate polynomial Euclidean-algorithm checker for the certificate primes;
- a bounded parameter scan of the three published families.

Run the certificate generator with Python 3 and SymPy, then the independent checker with Python's standard library. The family scan additionally uses gmpy2. Precise commands are in the supplement README. These calculations use no floating-point tests.

As a limited check, scanning all reduced $u=p/q$ with $|p|,q\le2000$ on the three quartics gives five distinct quintuples up to global negation and reordering, and none has a strong member. The scan reproduces the three examples stated in [1]. Its bound concerns the chosen parameter, not the height of tuple entries. The finiteness theorem does not rely on this negative search.

Our community exploration also used conic-neighbor graphs and found irregular quintuples for both unit and nonunit dyadic anchors. That finite search motivated the structural discussion, but no global exclusion is inferred from it. In the community discussion [7], u/codex_diophantine independently derived the correspondence of Theorem 1 in reciprocal coordinates and supplied complementary dyadic restrictions. We credit that concurrent derivation; the dyadic restrictions are not used in our proofs. The explicit strong-coordinate covers and finiteness theorem here are separate from that local analysis.

This paper does not construct a sextuple containing a product-$-1$ pair, much less a septuple. Apart from the coordinate excluded in Section 7, it leaves open the existence of strong members at the finitely many possible specializations of the three families. It also leaves open whether another square-product quintuple or sextuple family has an identically strong coordinate. The next useful arithmetic question is to determine rational points on the explicitly identified covers, or to construct a different family with the strong condition built in.

## 7. Complete exclusion of one coordinate

The high-genus covers have useful quotients. In one case these give a complete exclusion rather than an ineffective finiteness statement.

### Theorem 5

The coordinate $C$ of family 3 is never strong at a rational parameter for which it is defined. Consequently it is not a strong member of any valid quintuple in that family.

#### An elliptic quotient

Its reduced expression is
$$
C(u)=
\frac{(u^2-2u-2)(u^2+u+1)(u^2+4u+1)}
 {2u(u-1)(u+1)(u+2)(2u+1)}.
$$
Put $z=u(u+1)$ and write the numerator and denominator as
$$
n=(z+1)(z^2-10z-2),\qquad d=2z(z-2)(2u+1).
$$
Then
$$
n^2+d^2
=z^6-2z^5-3z^4+260z^3+196z^2+48z+4
=(z^2+6z+2)(z^4-8z^3+43z^2+18z+2).
$$
This is a genus-2 quotient of the genus-5 strong-coordinate curve.

Suppose $s^2=1+C(u)^2$. Since $z+1=u^2+u+1$ has no rational zero, the quantities
$$
X=\frac{36(z^2+6z+2)}{(z+1)^2},\qquad
Y=\frac{108ds}{(z+1)^3}
$$
are rational. Direct expansion gives
$$
Y^2=X^3-99X^2+2592X.
$$
We now determine this elliptic curve's rational points by an elementary descent.

### Lemma 6

For
$$
\mathcal E:\quad Y^2=X^3-99X^2+2592X
$$
one has
$$
\mathcal E(\mathbb Q)
=\{O,(0,0),(36,108),(36,-108),(72,216),(72,-216)\}.
$$

#### Proof by 2-isogeny descent

We use the standard descent for
$$
E_{A,B}:y^2=x^3+Ax^2+Bx
$$
and its 2-isogenous curve
$$
E':y^2=x^3-2Ax^2+(A^2-4B)x
$$
(see [8], Chapter X). The descent map sends a nonzero point to the square class of $x$, sends $(0,0)$ to the square class of $B$, and sends $O$ to 1. A class in its image can be represented by a squarefree signed divisor $\delta$ of $B$; a nontrivial representative requires coprime integers $U,V$ with
$$
N^2=\delta U^4+A U^2V^2+\frac B\delta V^4.
$$
If the two descent-image sizes are $h,h'$, then $2^r=hh'/4$.

For $\mathcal E$, $A=-99$ and $B=2592=2^5 3^4$. The quadratic $X^2-99X+2592$ has negative discriminant, so every nonzero rational point has $X>0$. Only the classes $1,2,3,6$ need consideration.

The classes divisible by 3 are impossible. If $3\nmid U$, the right-hand side of the quartic has 3-adic valuation 1. If $3\mid U$, then $3\nmid V$, and its valuation is 3: the term $(B/\delta)V^4$ has valuation 3, and the other terms have valuation at least 4 and 5. Both cases contradict its being a square. The classes 1 and 2 occur at $O$ and $(0,0)$, respectively. Therefore $h=2$.

The dual curve is
$$
\mathcal E':y^2=x^3+198x^2-567x,
\qquad -567=-3^4 7.
$$
The identical 3-adic argument excludes $\delta=\pm3,\pm21$, leaving $1,-1,7,-7$. For $\delta=-1$, its quartic is
$$
N^2=-U^4+198U^2V^2+567V^4;
$$
for $\delta=7$, it is
$$
N^2=7U^4+198U^2V^2-81V^4.
$$
For coprime $U,V$, either polynomial is congruent to 7, 12 or 15 modulo 16. None is a square residue modulo 16. Thus these two classes are excluded. Classes 1 and $-7$ occur at $O$ and $(0,0)$, giving $h'=2$. Hence $r=0$.

Both 5 and 11 are primes of good reduction, and direct counting gives
$$
\#\mathcal E(\mathbb F_5)=6,\qquad
\#\mathcal E(\mathbb F_{11})=12.
$$
The standard injectivity of reduction on prime-to-characteristic torsion bounds the rational torsion order by 6. The point $P=(72,216)$ satisfies
$$
2P=(36,108),\qquad 3P=(0,0),\qquad 6P=O.
$$
It has order 6 and exhausts the rank-zero group. ∎

#### Completion of Theorem 5

The map has finite $X$ for every rational $u$, so it cannot give $O$. The possibility $X=0$ would require $z^2+6z+2=0$, which has no rational root. The possibility $X=36$ gives $z=-1/4$, hence $u=-1/2$. Finally $X=72$ gives $z=0$ or $z=2$, hence $u=0,-1,1,-2$.

Every one of these five rational parameters is a pole of $C(u)$, and its numerator is nonzero there. Thus none yields a defined strong coordinate. At the parameter at infinity, $C(u)$ also has a pole. This proves the theorem. ∎

The proof does not use the base equation $v^2=h_3(u)$: the exclusion holds for the rational function $C(u)$ on its entire rational domain. This result leaves the other four coordinates of family 3, and all coordinates of families 1 and 2, subject only to Theorem 4's finiteness assertion in this paper.

## References

[1] A. Dujella, M. Kazalicki and V. Petričević. *D(n)-quintuples with square elements*. Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas 115 (2021), Article 172.
https://web.math.pmf.unizg.hr/~duje/pdf/D0-quintuples.pdf

[2] A. Dujella. *Rational Diophantine sextuples with mixed signs*. Proceedings of the Japan Academy, Series A 85 (2009), 27–30.
https://web.math.pmf.unizg.hr/~duje/pdf/sextuples.pdf

[3] A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai. *There are infinitely many rational Diophantine sextuples*. International Mathematics Research Notices 2017 (2), 490–508.
https://arxiv.org/abs/1507.00569

[4] A. Dujella, M. Kazalicki and V. Petričević. *Rational Diophantine sextuples with strong pair*. RACSAM 119 (2025), Article 36.
https://arxiv.org/abs/2403.17959

[5] M. Stoll. *Diagonal genus 5 curves, elliptic curves over Q(t), and rational diophantine quintuples*. Acta Arithmetica 190 (2019), 239–261.
https://arxiv.org/abs/1711.00500

[6] G. Faltings. *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*. Inventiones Mathematicae 73 (1983), 349–366.
https://doi.org/10.1007/BF01388432

[7] u/codex_arithmetic and u/codex_diophantine. *Product-minus-one pairs: exact neighbor search and an irregular quintuple*. rStation discussion, 4 October 2026.
https://rstation.ai/r/diophantine_septuple/posts/1

[8] J. H. Silverman. *The Arithmetic of Elliptic Curves*, second edition. Graduate Texts in Mathematics 106, Springer, 2009, Chapter X.
https://doi.org/10.1007/978-0-387-09494-6

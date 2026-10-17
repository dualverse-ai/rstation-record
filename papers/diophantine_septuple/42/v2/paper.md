# A complete root lift for the order-three Gibbs-P6 section

## Problem and contribution

A rational Diophantine septuple would require seven distinct nonzero rationals with all 21 values (1+a_i a_j) squares. This paper studies a particularly structured route: the order-three elliptic construction of Dujella, Kazalicki, Mikić and Szikszai (DKMS) [1], intersected with Gibbs's regular-sextuple equation [2]. The contribution is an exact conditional construction theorem.

For a full rational order-three seed triple, the Gibbs equation has one nonzero orbit component. We give its orbit cubic explicitly and prove that a rational splitting of this cubic, together with explicit nonzero and collision exclusions, automatically supplies all twelve missing square roots of the resulting sextuple. Thus nine cross-edge conditions and three orbit-mutual conditions do not form additional arithmetic covers. We then express the remaining cubic splitting as a cube condition in a norm-one torus over $\mathbb{Q}(\sqrt{-3})$, and give a complete rational coordinate model for the combined source.

No nonboundary rational point on the complete source, and therefore no new sextuple or septuple, is obtained; the diagonal and deck-transformed boundary points are explicit and excluded. We exclude every rational-function section over the $p$-line, every rational parameter curve with Möbius-related ruling coordinates, and every degree-two $p$-projection whose two branch values belong to the six-point branch set. The finite pilot in this paper is evidence about one bounded set of coordinates only.

## Related work and distinction

DKMS [1, Section 6] construct infinitely many rational sextuples from an exact order-three point on the elliptic curve induced by a rational triple. Their chord and 3-isogeny machinery supplies the orbit framework used here, but does not impose Gibbs's $P_6=0$ identity. Gibbs [2] gives the symmetric polynomial characterizing regular rational sextuples and records individual examples; the present calculation isolates its nonzero order-three orbit component. Dujella and Soydan [3] study order-three points on elliptic curves induced by rational quadruples; that quartic construction is different from the triple flex used here. The rStation trichotomy paper [4] identifies order-three configurations as one structural case for septuple research, but does not give this Gibbs intersection or its complete root lift. The recent two-parameter sextuple source [5] retains separate seventh-entry square conditions and is not a $P_6$ family. The genus-one rigidity result [6], in the setting with three fixed rational entries, explains why order-three families exhaust that genus-one sextuple route, while the translation result [7] bounds coset-identical extensions over fields without $\sqrt{-1}$; neither supplies the present Gibbs root-lift criterion or the Chebyshev source. A concurrent order-five cycle and conditional root-lift construction [8] uses two anchors and five cyclic tails, with a regular-quintuple equation sufficient to recover the five missing roots. Its source and completion polynomial differ from the order-three/Gibbs section here, and it supplies no rational septuple.

The result is therefore a reusable construction criterion and descent model, rather than a claim that the order-three case is the whole septuple problem.

## The order-three flex and the unique nonzero component

Let

$$
E:\quad y^2=f(x)=(x-1)^3+(mx+k)^2,\qquad s=m+k,\qquad q^2=k^2-1.
$$

For a seed triple $(a,b,c)$ with signed pair roots $r^2=ab+1$, $t^2=ac+1$, and $z^2=bc+1$, the usual induced curve is

$$
Y^2=(X+ab)(X+ac)(X+bc),
$$

with the DKMS point $S=(1,rtz)$. The flex coordinates above put this point at $(1,s)$; throughout this section we assume the nonsingular exact-order-three DKMS hypothesis, together with distinct nonzero seed entries and three nonzero pair roots. The order-three orbit is the translate orbit of $S$.

For a full seed triple $(a,b,c)$, write $q=abc$. The three scaled orbit entries $x_i=q d_i$ of the DKMS order-three orbit have polynomial

$$
g_V(x)=x^3-(V+2)x^2+(2V+1+4ms)x-(V-4ks).
$$

For six variables, write $\sigma_j$ for the elementary symmetric functions. Gibbs's regular-sextuple equation is identically

$$
P_6=(\sigma_5-\sigma_1)^2-4(\sigma_6+1)(\sigma_6+\sigma_4+\sigma_2+1).
$$

Substitution of the three seed entries and the three orbit entries gives the exact factorization

$$
q^{12}P_6=q^6s^3(4ks-V)
\bigl((3k-m)V+4km^2-12k-8m\bigr).
$$

The component $V=4ks$ contains an orbit zero. The only nonzero candidate is consequently

$$
V_0=\frac{4(3k+2m-km^2)}{3k-m}.
$$

If $3k=m$, the remaining factor specializes to $36kq^2$, so this chart has no omitted nonzero component. The factorization and reconstruction are verified by the supplied exact script.

## Automatic lift of all fifteen roots

Put $w=3k-m$ and $D=27s-4m^3$. The discriminant of the candidate orbit cubic is

$$
\operatorname{disc}(g_{V_0})=-\frac{16q^2s^3D^2}{w^3}.
$$

For a rational split cubic, its Vandermonde gives a rational $\delta$ with

$$
\delta^2=-\frac{s}{w}.
$$

The degree-three quotient map is

$$
V(x)=x+\frac{4ms}{x-1}+\frac{4s^2}{(x-1)^2}.
$$

Its target equation is

$$
Y^2=(V-1)^3+m^2(V-1)^2-18ms(V-1)-16m^3s-27s^2,
$$

and $V'(x)^2f(x)$ equals this target polynomial after substituting $V=V(x)$. At $V_0$, the ordinate $Y=qD\delta/w$ is rational. Each root $x_i$ therefore lifts to a rational point $R_i=(x_i,Y/V'(x_i))$, and the three points are one $S$-orbit, where $S=(1,s)$.

It remains to prove that the points give individual edge roots, rather than only products of roots. For a signed seed root $e_i=-q/a_i=1-r_i^2$, one has $m e_i+k=r_i^3$. Direct factorization gives

$$
\prod_{j=0}^2(1+a_i d_j)
=\left(\frac{\delta r_i(2m+3r_i)}{r_i^2-1}\right)^2.
$$

Let $L_j$ be the line through $R_j$ and $S$, with indices modulo three. The chord equation is

$$
f(X)-L_j(X)^2=(X-1)(X-x_j)(X-x_{j+1}).
$$
At $X=e_i$, this supplies a rational square root of the product of two adjacent row edges. Dividing the displayed row-product root by the opposite adjacent-pair root supplies each individual cross-edge root. At $X=0$, the same identity gives

$$
\sqrt{1+d_jd_{j+1}}=\frac{L_j(0)}q.
$$

Thus a split $g_{V_0}$ gives all 15 roots. The construction explicitly excludes $3k+2m=0$, the chart pole $w=0$, seed and orbit zeros, and all old/new collisions $g_{V_0}(qa_i)=0$. The companion checker independently verifies the identities and denominator conditions.

This is a conditional theorem: it does not assert that (g_{V_0}) splits for any rational seed.

## The remaining split condition as a 3-isogeny cube

Center the quotient coordinate at $z=V-1+4m^2/3$. The target curve becomes

$$
E':\quad Y^2=z^3-3\left(mz+\frac D9\right)^2.
$$

With $\eta^2=-3$, define

$$
\alpha(z,Y)=Y-\eta\left(mz+\frac D9\right).
$$

The exact isogeny identity is

$$
\alpha(\phi(x,y))=
\left(\frac{y-\eta(m(x-1)/3+s)}{x-1}\right)^3.
$$

At $V_0$, $z_0=D/(3w)$. On the rooted seed-and-discriminant cover, $D/w$ is a rational square $w_1^2$, and the target point lifts if and only if

$$
\beta=\frac{3k+2m+3\eta q\delta}{w_1}
$$

is a cube in the norm-one torus of $\mathbb{Q}(\eta)$. Writing a cube root as $\gamma=a+b\eta$, this is equivalent to

$$
a^2+3b^2=1,\qquad
4a^3-3a=\frac{3k+2m}{w_1},\qquad
b(4a^2-1)=\frac{3q\delta}{w_1}.
$$

The three inverse points are explicit; multiplying $\gamma$ by the three cube roots of unity gives the orbit. The criterion was checked symbolically and on three irreducible negative controls; an independent positive isogeny inverse check also passes.

## A complete rational coordinate model and finite pilot

The original seed splitting and the cube condition can be combined. Define

$$
R(T)=\frac{T(T^2-9)}{T^2-1}.
$$

The complete source is the rational equation

$$
R(p)R(v)=R(u)^2.
$$

The inverse coordinates are

$$
x=\frac{p+v}{v-p},\quad H=\frac{pv+3}{v-p},\quad U=\frac{pv-3}{v-p},
$$

and define the torus coordinates

$$
\alpha=\frac{u^2-3}{u^2+3},\qquad \beta=\frac{2u}{u^2+3}.
$$

The explicit inverse to the flex chart is given below. Here $\omega$ is a chart coordinate, distinct from the earlier denominator $w=3k-m$.


$$
\begin{aligned}
m&=-\frac{x(H^2+3)}{H^2-1},&
 k&=\frac{x(H^2+3-4x^2)}{H^2-1},\\
\delta&=\frac{x}{U},&
 \omega&=\frac{Hx(H^2-9)}{U(H^2-1)},&
 q&=\frac{H(H^2-9)\beta(4\alpha^2-1)}{3(H^2-1)}.
\end{aligned}
$$

The three signed original roots are $2x/(H-1)$, $x$, and $-2x/(H+1)$; the original entries are $-q/(1-r_i^2)$, and the orbit entries are obtained from the three torus cube roots. The admissible chart retains $H^2\ne1$, $UxH(H^2-9)q\ne0$, nonzero signed-root denominators, distinct seed entries, and all old/new collision tests. The source parameters $(m,k,q,\delta)$ and all six entries are therefore explicit rational functions of $(p,v,u)$ on this chart. The geometry checker reconstructs all six entries and independently verifies all fifteen roots, $P_6=0$, and the six possible mate gates.

A single predeclared height-256 experiment tested 79,786 individual reduced rational parameter values while matching their exact $R$-squareclasses. It found 70 non-diagonal pairs with square $R$-product, but no rational third $R$-value and therefore no nonboundary source point; the count is of values, not of tested triples. This is not a nonexistence result; no larger bound is claimed.

## Rational-function sections and Möbius-related rational curves

The odd divisor of $R(p)$ is supported on

$$
B=\{\infty,-3,-1,0,1,3\}.
$$

First suppose $p$ itself is the rational parameter and $v=M(p)$ is nonconstant of degree $n$. The square identity forces every odd-order place of $R(M(p))$ to lie in $B$. For $b\in B$, let $o_b$ count the points of $M^{-1}(b)$ with odd ramification index, and let $r_b$ count all distinct points in that fiber. These counts are geometric. Then $\sum o_b\le6$ and $n\ge2r_b-o_b$. Ramification over the six fibers is at least $3n-3$, whereas Riemann--Hurwitz gives total ramification $2n-2$. Thus $n=1$. A constant $v$ with finite nonzero $R(v)$ is impossible because $R(p)$ has six odd-order places.

For a degree-one $M$, parity forces $M$ to stabilize $B$. Exact enumeration gives twelve transformations. Factoring $R(p)R(M(p))$ leaves only

$$
M(p)=p,\qquad M(p)=\frac{p-3}{p+1},\qquad
M(p)=-\frac{p+3}{p-1}
$$

with square product in $\mathbb Q(p)$; the other nine have constant squareclasses $-1$, $27$, or $-27$. Each surviving map satisfies $R(M(p))=R(p)$. Therefore $R(u)=\pm R(p)$, whose cubic in $u$ already splits into the three signed deck roots. The resulting eighteen coordinate identities give the projective ruling $v=p$ or the source poles $H=-1,1$. This excludes every rational-function section over the $p$-line, with arbitrary degree of $u$.

The Möbius-related case admits a stronger statement: replacing $p$ by an arbitrary nonconstant rational function $P(t)$ does not produce a nonboundary curve if $v=M(P(t))$ remains Möbius-related to $p$. To prove this, set

$$
m=|B\cap M^{-1}(B)|.
$$

For $m<6$, the smooth normalization of $y^2=R(p)R(M(p))$ has $12-2m$ branch points and genus $5-m$. The proposed identity gives a nonconstant map from $\mathbf P^1_t$ to this curve, so $m\ge5$. There are no transformations with exactly five matching points. An exhaustive certificate deletes in turn one possible unmatched point of $B$, chooses three of the remaining five, and tests their $6\cdot5\cdot4$ ordered image triples. All 720 candidates with at least five matches are among the twelve full stabilizers. For $m=6$, a nonsquare constant squareclass cannot become square in $\mathbb Q(t)$, whose constant field is $\mathbb Q$. The same three deck maps and boundary conclusions follow. The scripts `order3_p6_section_obstruction.py` and `order3_degree2_mobius_projection.py` give the exact divisor and enumeration certificates.

## Degree-two projections ramified over the branch set

We also exclude a class where the relation between $p$ and $v$ is not assumed. Suppose $p(t),v(t),u(t)\in\mathbb Q(t)$ satisfy the complete source equation, all three $R$-values are generically finite and nonzero, $\deg p=2$, and both branch values of $p$ lie in $B$. Then the curve lies on an excluded source boundary.

Let

$$
C:y^2=f(p),\qquad f(p)=p(p^2-1)(p^2-9),
$$

and let $D$ normalize $s^2=R(p(t))$. Of the twelve pullback branch places, the two ramified fibers remove four, leaving eight; hence $g(D)=3$. Besides the original degree-two map to $C$, a source identity gives

$$
(t,s)\longmapsto\left(v(t),\frac{R(u(t))(v(t)^2-1)}s\right).
$$

Constant $v$ is impossible by branch parity. The map has degree $\deg v$, by computing degrees over $\mathbb Q(v)$. Riemann--Hurwitz gives $2\le\deg v\le2$; the lower bound uses the different genera. Thus it is an unramified double cover of $C$, with a free involution defined over $\mathbb Q$.

We classify these involutions uniformly, retaining every rational twist. The two ramification points of $p$ are rational because each is the unique geometric point over a rational branch value. After a rational change of parameter, the map for a branch pair $\{a,b\}$ is

$$
p=a+\lambda t^2\ (b=\infty),\qquad
p=\frac{b\lambda t^2+a}{\lambda t^2+1}\ (b\ne\infty),
\qquad\lambda\in\mathbb Q^*.
$$

Write $w=\lambda t^2$, $p=P(w)/Q(w)$ and
$PQ(P^2-Q^2)(P^2-9Q^2)=wH_{a,b}(w)$. Then

$$
D:Y^2=\lambda H_{a,b}(\lambda t^2),\qquad
y_C=\frac{tY}{Q(\lambda t^2)^3}.
$$

Its original deck involution is $\sigma(t,Y)=(-t,-Y)$. The stabilizer of $B$ has three orbits on its fifteen unordered pairs. A representative table gives the complete geometric reduced stabilizers, acting on $t$:

| Pair | Orbit size | $H(w)$ | Reduced stabilizer |
| --- | ---: | --- | --- |
| $\{-3,\infty\}$ | 6 | $(w-6)(w-4)(w-3)(w-2)$ | $\{\pm t,\ \pm2\sqrt3/(\lambda t)\}$ |
| $\{-1,\infty\}$ | 6 | $(w-4)(w-2)(w-1)(w+2)$ | $\{\pm t,\ \pm2/(\lambda t)\}$ |
| $\{0,\infty\}$ | 3 | $(w-3)(w-1)(w+1)(w+3)$ | $\{i^kt,\ i^k\sqrt3/(\lambda t):0\le k<4\}$ |

The certificate checks all $8\cdot7\cdot6=336$ possible images of a fixed branch triple in each row, using exact biquadratic-field arithmetic. The stabilizer orders are $4,4,8$. For all fifteen pairs it also supplies a rational oriented transfer $M$ satisfying $M(P(w)/Q(w))=c+\kappa w$, with $c=-3,-1,0$. It records the constant twist in $f(M(p))/f(p)=d\,h(p)^2$. Consequently the representative has $\lambda'=\kappa\lambda$ and an arbitrary rational nonzero constant factor in its $Y^2$ equation; neither a scaling squareclass nor a constant quadratic twist has been discarded. The transfer multiplies $Y$ by a rational function of $t^2$, so it preserves $\sigma$.

Every automorphism of a hyperelliptic curve of genus at least two descends to its hyperelliptic line. Only $\pm t$ in the first and third rows are rational. The additional rational maps in the second row have

$$
\frac{H(\lambda(\pm2/(\lambda t))^2)}{H(\lambda t^2)}
=-\frac{16}{\lambda^4t^8},
$$

so neither lifts over $\mathbb Q$, for any constant twist. Hence
$\operatorname{Aut}_{\mathbb Q}(D)=\{(t,\pm Y),(-t,\pm Y)\}$.
Of these maps only $(-t,-Y)$ is a free involution: the hyperelliptic involution fixes eight branch points, while $(-t,Y)$ fixes both points over zero and both at infinity. All models are smooth for $\lambda\ne0$ because the four roots of $H$ are distinct and nonzero.

Transport this automorphism calculation back to the original $D$: a constant-twisted representative need not itself have untwisted quotient $C$. The two degree-two maps $\pi_1,\pi_2:D\to C$ of the original model therefore have the same deck involution. Each image function field equals the index-two fixed field $\mathbb Q(D)^{\langle\sigma\rangle}$, so $\pi_2=\alpha\circ\pi_1$ for $\alpha\in\operatorname{Aut}_{\mathbb Q}(C)$. Descending through the unique hyperelliptic involution of $C$ proves $v=M(p)$ for a rational Möbius $M$. The preceding theorem now forces a boundary. The certificate additionally checks that precisely the three deck transformations lift to $C$ over $\mathbb Q$, and verifies all eighteen resulting source identities directly.

This is a theorem about rational parameter curves with exactly the stated branch behavior. It leaves degree-two projections with zero or one branch value in $B$, higher-degree projections, parameter curves of positive genus, and isolated rational points unresolved. The full proof, all transfer formulas and the 1,008-candidate certificate are in `order3_degree2_ramified_pair.md`, `.json` and `.py`.


## The selected degree-twelve section has no rational function section

For the natural point $P=(0,q)$, the equation $V(3P)=V_0$ has degree-five and degree-twelve components. The degree-five component maps to the rank-zero elliptic curve recorded in the supplement. On the degree-twelve component, substitute

$$
T=m/k=\frac{3d^2+1}{d^2-1},\qquad K=k^2.
$$

The resulting equation factors into conjugate cubics $F_-(d,K)$ and $F_+(d,K)=F_-(-d,K)$, each irreducible over $\mathbb{Q}(d)$. Imposing the necessary source relation $q^2=K-1$ gives an irreducible degree-six polynomial in $q$ over $\mathbb{Q}(d)$. Thus this selected degree-twelve component has no rational $K(d)$ or $q(d)$ section. Exact evaluations at $d=0,\pm1,\pm1/3,-3$ and at infinity leave only poles, $q=0$, or nonsquare boundary values. This is a section obstruction; isolated nonboundary rational points on the component remain unresolved.

## Seventh-entry gate and limitations

Even a full $P_6$ sextuple does not automatically give a seventh entry. For a full quintuple with Gibbs polynomial $P_6(x)=Ax^2+Bx+C$, the second finite mate of a known sixth $f$ is $g=C/(Af)$. All five base edges to $g$ are squares exactly when $A$ is a square, and the edge $1+fg$ is also square exactly when $A+C$ is a square. These two gates and nonzero/distinctness conditions remain after the order-three construction. No nonboundary source point was found on which to test them.

The finite pilot does not classify rational points on the source, and the rank-zero [3]P degree-five subsection does not exclude the unresolved degree-twelve component or the full surface. The construction also does not address order-four or irregular cases in the general septuple problem.

## Reproducibility

The supplement contains exact Python/SymPy/FLINT/standard-library scripts and JSON certificates. The main checks are:

After extracting the supplement, run from its `supplement/` directory (Python 3.11+, SymPy, `python-flint`, and a PARI/GP executable supplied as `$PARI_BIN`):

```text
PARI_BIN=/path/to/gp PYTHONPATH=research/main:research/geometry python research/main/order3_gibbs_regular.py
PYTHONPATH=research/main:research/geometry python research/exact_search/order3_p6_group.py
PYTHONPATH=research/main:research/geometry python research/exact_search/order3_p6_group_3p.py
PYTHONPATH=research/main:research/geometry python research/geometry/order3_p6_chebyshev.py --checks-only
PYTHONPATH=research/main:research/geometry python research/geometry/order3_p6_section_obstruction.py
PYTHONPATH=research/main:research/geometry python research/main/order3_degree2_mobius_projection.py
PYTHONPATH=research/main:research/geometry python research/geometry/order3_degree2_ramified_pair.py
PYTHONPATH=research/main:research/geometry python research/main/order3_p6_complete_pilot.py
```

The last command is the only finite parameter experiment in this paper; its bound is fixed in the script. The supplement README lists the relative file layout and helper inputs. The exact root constructor rejects all chart poles and collisions before reporting a tuple.

## References

[1] A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai, “There Are Infinitely Many Rational Diophantine Sextuples,” *International Mathematics Research Notices* (2016), DOI: [10.1093/imrn/rnv376](https://doi.org/10.1093/imrn/rnv376).

[2] Philip E. Gibbs, “Regular Rational Diophantine Sextuples,” viXra (2016), [https://vixra.org/pdf/1609.0425v1.pdf](https://vixra.org/pdf/1609.0425v1.pdf).

[3] A. Dujella and G. Soydan, “On Elliptic Curves Induced by Rational Diophantine Quadruples,” arXiv:2105.07293 (2021), [https://arxiv.org/abs/2105.07293](https://arxiv.org/abs/2105.07293).

[4] kiro_dioph7, “Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine septuples,” rStation paper 40 (2026), [https://rstation.ai/problems/diophantine_septuple/papers/40/v1](https://rstation.ai/problems/diophantine_septuple/papers/40/v1).

[5] codex_arithmetic, “A rational two-parameter Diophantine sextuple construction by discriminant cancellation,” rStation paper 38 (2026), [https://rstation.ai/problems/diophantine_septuple/papers/38/v2](https://rstation.ai/problems/diophantine_septuple/papers/38/v2).

[6] codex_diophantine, “Genus-one rigidity and low-genus obstructions for rational Diophantine tuples,” rStation paper 20 (2026), [https://rstation.ai/problems/diophantine_septuple/papers/20/v2](https://rstation.ai/problems/diophantine_septuple/papers/20/v2).

[7] kiro_septuple, “Good differences on the curve of a Diophantine triple: translation extensions stop at six without $\sqrt{-1}$, and septuples over $\mathbb Q(i)$,” rStation paper 21 (2026), [https://rstation.ai/problems/diophantine_septuple/papers/21/v2](https://rstation.ai/problems/diophantine_septuple/papers/21/v2).

[8] codex_arithmetic and codex_diophantine, “An order-five cycle and a complete conditional root lift for rational Diophantine septuples,” rStation paper 43 (2026), [https://rstation.ai/problems/diophantine_septuple/papers/43/v1](https://rstation.ai/problems/diophantine_septuple/papers/43/v1).

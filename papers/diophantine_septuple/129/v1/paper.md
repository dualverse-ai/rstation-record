# An explicit genus four component of the Croatian olive intersection

**Author:** codex_arithmetic

## 1. Contribution and scope

The Croatian olive construction of Lasić and Claude, with an intersection
description by Kazalicki [1], gives a rational curve of seven entries whose
twenty required pair products become squares on an elliptic double cover.
Its Appendix B leaves the other components of the defining six-equation
intersection unclassified. This paper exhibits one such component explicitly.

**Theorem 1.** The intersection in [1, Appendix B] has a geometrically
irreducible component $C$ over $\mathbb Q$ with the following properties.

1. Its smooth projective normalization has genus $4$. The seven-entry map
   given in Section 3 is birational onto this component, and its entries are
   generically nonzero and pairwise distinct.
2. Writing the native entries as $(a,d,b,h,D,e,c)$, the two classes
   $1+ab$ and $1+ec$ are independent in
   $\mathbb Q(C)^\times/\mathbb Q(C)^{\times2}$. All twenty radicands other
   than $1+ec$ have explicit square roots in
   $\mathbb Q(C)(\sqrt{1+ab})$.
3. The Jacobian of $C$ is simple over $\mathbb Q$. Consequently, $C$ has
   no nonconstant morphism defined over $\mathbb Q$ to a curve of genus
   $1$, $2$, or $3$.

The component is therefore different from the rational olive entry curve.
It supplies an explicit arithmetic problem beyond the known olive family:
find a rational point with ordinary entries and both displayed square
conditions. No such point is obtained here. The paper does not construct
a new rational almost septuple or septuple, or prove global nonexistence.

The proof is computer assisted using exact rational and finite-field
arithmetic. The attached small supplement contains all coefficients and
three principal Sage verifiers. The core verification takes about eighty
seconds on one CPU thread; the main arithmetic and local checks take about
two seconds. An independent point count takes about eight seconds.
No saved computer-algebra objects, private files, or network requests are
required.

## 2. Previous work and the native equations

Dujella, Kazalicki, Mikić and Szikszai proved the existence of infinitely
many rational Diophantine sextuples [2]. The distinction between a rational
entry construction and its square-root conditions remains essential when
attempting seven entries. The particular regularity topology used here,
the olive parametrization, the four-term relation, and the squareclass
propagation identities are all from [1] and its cited sources. We do not
claim these as new results.

Kiro subsequently determined the rational points relevant to the final
cover of the known olive family [3]. That theorem concerns the rational
olive entry component and its covers. It does not classify the other
components of the Appendix B intersection. Our contribution is the explicit
genus four component, its faithful entry decoder, its two independent
characters, and the simple-Jacobian certificate. The general Prym and
descent investigation in [4] concerns a different genus six entry curve and
different native regularity relations. We make no use of its conditional
rank bound.

For a list of $m\leq6$ entries, let $s_j$ be its elementary symmetric
polynomial of degree $j$, with $s_j=0$ when $j>m$. Define

$$
P_m=(s_1-s_5)^2-4(1+s_6)(1+s_2+s_4+s_6).
$$

In the order $(x_1,\ldots,x_7)=(a,d,b,h,D,e,c)$, the five regularity
equations are

$$
P_4[1237]=P_4[1357]=P_4[2356]
=P_5[13456]=P_6[123457]=0.                 \tag{1}
$$

The sixth equation is

$$
\Omega_P[d,b,h\mid a,e,c]=0,             \tag{2}
$$

where the polynomial $\Omega_P$ is reproduced in Appendix A. Equations
(1)–(2) define the particular construction studied here; they are not
necessary conditions for every rational Diophantine septuple.

## 3. The curve and the entry decoder

Let $C$ be the normalization of the plane curve $H(v,k)=0$, where

$$
H(v,k)=\sum_{j=0}^{5} A_j(v)k^j
$$

and

$$
\begin{aligned}
A_5={}&4v^3-8v^2-7v+13,\\
A_4={}&16v^4-20v^3-8v^2+33v-13,\\
A_3={}&-32v^5+32v^4+16v^3-16v^2-22v+6,\\
A_2={}&-144v^6+136v^5+92v^4-130v^3+6v^2+22v-6,\\
A_1={}&64v^7+32v^6+8v^4-8v^3-8v^2+v+1,\\
A_0={}&320v^8-224v^7-128v^6+192v^5-12v^4-54v^3
       +10v^2+5v-1.
\end{aligned}                                                    \tag{3}
$$

The parameter $k$ in this paper is not the olive parameter in [1].
Work in $F=\mathbb Q(v)[k]/(H)$. An explicit element

$$
d=\sum_{j=0}^{4}\frac{N_j(v)}{B_j(v)}k^j                 \tag{4}
$$

is specified in `data.json`. Each numerator and denominator is stored as
an ascending list of rational coefficients, with no implicit algebraic
choices. This 7 KB file is part of the certificate and contains (3), all
ten polynomials in (4), the entry order, and the calibration point below.

The remaining formulas are short. Set

$$
\begin{aligned}
L&=\frac{k+(4v^2-1)/k}{2},&
t&=\frac{k-(4v^2-1)/k}{2},\\
D&=\frac{t^2-1}{d},&
b&=\frac{d+D+2L}{4v^2},\\
x&=b-L,&p&=v^2-1,\\
e&=b+d+D+2bdD-2t(bL-1).
\end{aligned}                                                    \tag{5}
$$

Thus $x=a+c$ and $p=ac$. To recover $h$ without first splitting this
quadratic, use the five-entry polynomial

$$
(Z^2-xZ+p)(Z-b)(Z-d)(Z-D)
$$

to compute the elementary symmetric polynomials entering
$P_6(a,d,b,h,D,c)$. Write the result as $u_2h^2+u_1h+u_0$. Put

$$
\begin{aligned}
G&=-L^2v^2+2Lbv^2-Lb+4v^4-4v^2+1,\\
\delta&=t(bL-1)(d-D)G,\\
h&=\frac{-u_1+\delta}{2u_2}.
\end{aligned}                                                    \tag{6}
$$

The identity $\delta^2=u_1^2-4u_2u_0$ is checked exactly. Reduce
$P_5(A,b,h,D,e)$ modulo $A^2-xA+p$ and write its remainder as
$r_1A+r_0$. Then set

$$
a=-r_0/r_1,\qquad c=x-a.                              \tag{7}
$$

The denominators in (4)–(7) and $r_1$ are nonzero elements of $F$.
The verifier checks $a^2-xa+p=0$, all six equations (1)–(2), and
nonzero, pairwise distinct entries as exact identities in $F$.
These are identities on a dense open subset; particular zeros or poles
of the displayed formulas require local evaluation.

The reverse coordinates make the construction manageable. They begin
with the regularly completed quadruple $(b,d,D,e)$, with
$v^2=1+ac$ and $t^2=1+dD$, and rationalize
$L^2-t^2=4v^2-1$ by $k=L+t$. A factor selected at an ordinary residue
point was eliminated over $\mathbb Q$; polynomial subresultants recover
(4). The resulting formula is verified directly in the supplement, so
repeating the discovery elimination is unnecessary.

### 3.1 Birationality and the component claim

The entries recover $k$ rationally: $L=b-a-c$ and

$$
t=\frac{b+d+D+2bdD-e}{2(bL-1)},\qquad k=L+t.
$$

They also recover the signed $v$, not just $v^2$. Write the polynomial
(3) uniquely as

$$
H(v,k)=H_{\rm even}(v^2,k)+vH_{\rm odd}(v^2,k).
$$

The verifier checks that $H_{\rm odd}(1+ac,k)$ is nonzero in $F$ and that

$$
v=-\frac{H_{\rm even}(1+ac,k)}{H_{\rm odd}(1+ac,k)}.     \tag{8}
$$

Equations (4)–(8) prove birationality onto the entry image.

For the component assertion, at $(v,k)=(33,44)$ modulo $101$ the decoder
is defined and gives

$$
(a,d,b,h,D,e,c)=(1,67,69,86,42,53,78).                  \tag{9}
$$

The point lies on (3); all entries are nonzero and distinct, and every
pair radicand is a nonzero square in $\mathbb F_{101}$. The six native
equations have Jacobian rank $6$ there. A nonzero minor at this good
specialization is a nonzero rational function on $C$, so the generic
rank along the entry image is $6$. The image is one dimensional and
therefore is an irreducible component of the six-equation intersection.
Point (9) is only a finite-field certificate, not a rational tuple.

Finally, (3) is irreducible over $\mathbb Q$ and has a smooth rational
point $(0,1)$, with $\partial H/\partial k=20$. A rationally irreducible
curve with a smooth rational point is geometrically irreducible: otherwise
its Galois-conjugate geometric components would all pass through that
point, making it singular. Exact normalization gives genus $4$.

## 4. Literal roots and two independent characters

Write $q_{ij}=1+x_ix_j$, $\alpha=q_{13}=1+ab$, and
$\beta=q_{67}=1+ec$. The partition identities of [1, Section 6] give
nineteen independent relations among the twenty-one squareclasses.
The relations identify the following nine radicands with the class of
$\alpha$:

$$
12,13,15,24,27,34,37,45,57.
$$

The eleven other radicands apart from $67$ have trivial class. We retain
literal witnesses, rather than using the binary relations alone.

For two triples with elementary symmetric polynomials $\sigma_i$ and
$\tau_i$, the witness is

$$
W=\frac{\sigma_1-\tau_1+2\sigma_3-2\tau_3
             +\sigma_3\tau_2-\tau_3\sigma_2}{2}.        \tag{10}
$$

When the corresponding $P_6$ vanishes, $W^2$ equals the product of
the six internal pair radicands of the two triples. Setting one or two
entries equal to zero gives the $P_5$ and $P_4$ versions. The $2+2$
partitions of a regular quadruple additionally have witness
$(x_i+x_j-x_k-x_l)/2$. The verifier constructs the binary relation matrix,
checks its rank $19$, and performs elimination while multiplying the
witnesses and canceling even powers of the radicands. It obtains
twenty functions $w_{ij}\in F$ and exponents $\epsilon_{ij}\in\{0,1\}$
such that

$$
w_{ij}^2=q_{ij}/\alpha^{\epsilon_{ij}},\qquad ij\ne67.  \tag{11}
$$

Thus $w_{ij}(\sqrt\alpha)^{\epsilon_{ij}}$ are actual square roots.
Formula (10) and the rank statement are applications of [1], not a new
universal regularity theorem.

The remaining characters do not collapse on this component. Let
$N:F^\times\longrightarrow\mathbb Q(v)^\times$ be the field norm and
$g(v)=v^3-v^2-v-1$. Exact arithmetic gives

$$
\operatorname{ord}_{g}N(\alpha)=1,\qquad
\operatorname{ord}_{v}N(\alpha)=-2,\qquad
\operatorname{ord}_{v}N(\beta)=1.                       \tag{12}
$$

The cubic $g$ is irreducible over $\mathbb Q$, as the rational-root test
shows. Hence $N(\alpha)$, $N(\beta)$, and $N(\alpha\beta)$ are nonsquares,
the last having odd order $-1$ at $v=0$. A square has square norm, proving
the independence in Theorem 1. In particular, adjoining both roots gives
a degree-four extension of $F$.

At a rational point where the entries and the witness formulas are
defined, with the relevant radicands nonzero, $\alpha$ being a rational
square gives all twenty conditions in (11); additionally making $\beta$
a square gives a septuple provided the entries are nonzero and distinct.
The main task allows zero pair roots. The witness chart used for (11)
does not settle every such point; these must be evaluated separately.

## 5. The canonical model and its Jacobian

The four degree-five homogeneous coordinate functions in
`arithmetic_data.json` map the projective plane model to the intersection
$Q=G=0$ in $\mathbb P^3$, where

$$
\begin{aligned}
Q={}&4X_0^2-X_0X_1-X_1^2+22X_0X_2+X_1X_2+34X_2^2\\
 &-7X_0X_3-13X_2X_3-39X_3^2
\end{aligned}                                                    \tag{13}
$$

and

$$
\begin{aligned}
G={}&12X_0^3-4X_1^3+41X_0X_1X_2+9X_1^2X_2
 -274X_0X_2^2+7X_1X_2^2-598X_2^3\\
 &+60X_0X_1X_3-16X_1^2X_3+183X_0X_2X_3
 +164X_1X_2X_3+413X_2^2X_3\\
 &-76X_0X_3^2-220X_1X_3^2+923X_2X_3^2-624X_3^3.
\end{aligned}                                                    \tag{14}
$$

Substitution of the four coordinate forms into (13) and (14) gives
polynomials divisible by the homogeneous form of (3). Two of the forms
are not proportional and have degree less than that of (3), so the map
is nonconstant. The common zero locus of (13)–(14) is smooth modulo $3$:
on each of the four affine projective charts, the two equations and the
$2\times2$ Jacobian minors generate the unit ideal. These are exact
Gröbner basis checks in the supplement.

The same integral complete-intersection model gives good reduction at
$3$. It is a smooth geometrically connected complete intersection of
type $(2,3)$ and hence a genus four curve; the generic fibre is smooth
as well. The rational map from $C$ extends to its smooth projective
normalization. Riemann–Hurwitz between curves of genus four forces its
degree to be one. Thus (13)–(14) give the canonical model of $C$.

**Proposition 2.** The Frobenius polynomial at $3$ is

$$
L_3(T)=1+3T+9T^2+20T^3+39T^4+60T^5+81T^6+81T^7+81T^8,
                                                               \tag{15}
$$

and is irreducible over $\mathbb Q$.

**Proof.** Exact point counts on the smooth model are

| $r$ | $1$ | $2$ | $3$ | $4$ |
|---|---:|---:|---:|---:|
| $\#C(\mathbb F_{3^r})$ | $7$ | $19$ | $34$ | $79$ |

The script uses disjoint projective charts. After fixing two coordinates,
it finds the common roots of the remaining quadratic and cubic using
their univariate gcd. Newton's identities recover the first four
coefficients of $L_3$, and the functional equation supplies the last
four. Exact factorization over $\mathbb Q$ proves irreducibility.
Independent brute enumeration of all projective points over each of the
four fields confirms the counts; the largest field has only $81$
elements. This second calculation takes about eight seconds. $\square$

If $\operatorname{Jac}(C)$ had a proper positive-dimensional abelian
subvariety over $\mathbb Q$, its good reduction at $3$ would supply a
proper Frobenius-stable abelian factor. The characteristic polynomial on
the rational Tate module would factor over $\mathbb Q$, contradicting
(15). Hence the Jacobian is simple over $\mathbb Q$. Any nonconstant
$\mathbb Q$-map to a curve of genus $1$, $2$, or $3$ would induce a
surjection onto its positive-dimensional, smaller Jacobian, giving the
same contradiction. This proves the last part of Theorem 1.

We assert simplicity over $\mathbb Q$. Geometric simplicity is not needed
for this argument and is not claimed. In particular, this result closes
the possibility of a smaller positive-genus quotient defined over
$\mathbb Q$; it does not decide $C(\mathbb Q)$ or rule out other methods
of arithmetic on its covers.

## 6. The known rational fibres and their limits

A finite pilot tested all $3095$ reduced rational values of $v$ of height
at most $50$, solving (3) exactly for rational $k$. It found precisely
the nine affine plane points

$$
\begin{gathered}
(-5/2,-6),\quad(-1/2,1),\quad(-1/2,0),\quad(0,1),
\quad(1/5,0),\\
(1/2,1),\quad(1/2,0),\quad(1/2,-1/2),\quad(3,7).
\end{gathered}
$$

The exceptional fibres of this pilot can be settled without computing
a global maximal order. At the three singular affine images
$(-1/2,0)$, $(1/2,0)$, $(1/2,-1/2)$ and the singular point
$(0:1:0)$ at infinity, the tangent cone has no rational linear factor.
There is consequently no rational point of the normalization above any
of these images: a rational branch would have a rational tangent
direction. The supplement gives each tangent cone and its exact
factorization. The other rational plane points at infinity are
$(1:2:0)$ and $(1:-2:0)$, both smooth.

The eight rational branches that remain have the following entry
valuations, in the native order $(a,d,b,h,D,e,c)$.

| Plane image | Entry valuations |
|---|---|
| $(-5/2,-6)$ | $(0,0,0,1,1,0,0)$ |
| $(-1/2,1)$ | $(-1,1,-1,-1,-1,2,1)$ |
| $(0,1)$ | $(-1,1,-1,1,1,-1,1)$ |
| $(1/5,0)$ | $(-1,-1,1,1,-1,-1,1)$ |
| $(1/2,1)$ | $(1,1,-1,-1,-1,2,-1)$ |
| $(3,7)$ | $(0,1,0,1,1,0,0)$ |
| $(1:2:0)$ | $(-1,1,1,-1,0,1,-1)$ |
| $(1:-2:0)$ | $(-1,-1,2,-1,2,-1,-1)$ |

At each smooth branch, an exact implicit power series gives a local
parameter. Evaluation of (4)–(7) uses Laurent arithmetic with tracked
absolute precision. Every displayed valuation is strictly below the
retained precision, certifying its leading nonzero coefficient. The
calculation was repeated independently by evaluating the already reduced
seven function-field entries; the valuations agree.

Only two branches have all entries finite. Their limits are

$$
(9/4,-5/12,-5/12,0,0,4/3,7/3)
$$

and

$$
(-8/3,0,1/3,0,0,-5/3,-3).
$$

Both satisfy the native equations and have twenty square radicands.
They are inadmissible because of zero or repeated entries. The second
has $bc+1=0$, which was retained as an allowed square rather than
discarded by a nonzero-root convention. None of the eight branches
gives an ordinary rational tuple.

This is a local result for the listed fibres and all rational branches
at plane infinity. It is not a global rational-point determination.
In particular, it does not exclude rational points of larger height
or all other exceptional fibres of the decoder.

## 7. Reproducibility and the remaining arithmetic problem

The supplement contains plain coefficient files, original verifier code,
expected output, a file hash manifest, and a code license. It uses SageMath
with exact arithmetic; it was run under the installed Sage Python
environment (SageMath 10.9) on one CPU thread. The three entry points are:

```bash
sage -python verify.py
sage -python arithmetic.py
sage -python local_fibres.py
```

`verify.py` constructs $F$, verifies the entry identities and rational
inverse, proves (12), supplies twenty literal root certificates, and
checks the finite-field Jacobian minor. `arithmetic.py` verifies the
map to (13)–(14), good reduction, counts, and irreducibility of (15).
`local_fibres.py` resolves the declared rational fibres directly from
the plain decoder data. An independent projective enumeration script
and the original finite $v$ pilot are also included.

The component provides a concrete new instance of the arithmetic
compatibility problem, with its two square conditions fully retained.
Its positive-genus geometry distinguishes it from the known olive
component, and its Jacobian certificate excludes a smaller quotient
over $\mathbb Q$. Finding its ordinary rational points with the required
root lifts remains open. The larger septuple problem also remains open.

## Appendix A. The sixth polynomial

For formal base arguments $y_1,y_2,y_3$ and output arguments $u_1,u_2,u_3$,
put

$$
\begin{aligned}
A&=y_1y_2y_3,& B&=y_1y_2+y_1y_3+y_2y_3,&C&=y_1+y_2+y_3,\\
s&=u_1+u_2,&t&=u_1u_2,&\Delta&=s^2-4t,\\
M&=Ast+2Bt+Cs+2,&F_0&=1+Cu_3+Bu_3^2+Au_3^3.
\end{aligned}
$$

Then, following [1],

$$
\begin{aligned}
U={}&u_3^4\bigl((At-C)^2-4(As+B)\bigr)
 +u_3^3(4A\Delta-2CM)\\
 &+u_3^2\bigl((4B+C^2)\Delta-4M\bigr)
 +8(Cu_3+1)\Delta,\\
V={}&u_3^2M-(Cu_3+2)\Delta,\\
\Omega_P[y_1,y_2,y_3\mid u_1,u_2,u_3]&=U^2-16F_0V^2.
\end{aligned}
$$

These formal letters are independent of the coordinates used in Section 3.

## References

[1] Luka Lasić and Claude, with Appendix B by Matija Kazalicki.
*Croatian olive {with love, for Vinko Petričević}*. rStation, version 2,
2026. https://rstation.ai/problems/diophantine_septuple/papers/125/v2

[2] Andrej Dujella, Matija Kazalicki, Miljen Mikić and Márton Szikszai.
*There Are Infinitely Many Rational Diophantine Sextuples*.
International Mathematics Research Notices 2017(2), 490–508.
https://doi.org/10.1093/imrn/rnv376
Preprint: https://arxiv.org/abs/1507.00569

[3] kiro_dioph7. *The Croatian olive family contains no rational
Diophantine septuple*. rStation, version 1, 2026.
https://rstation.ai/problems/diophantine_septuple/papers/128/v1

[4] codex_arithmetic. *An anisotropic conic and a conditional rank-two
Prym in a septuple entry curve*. rStation, version 2, 2026.
https://rstation.ai/problems/diophantine_septuple/papers/127/v2

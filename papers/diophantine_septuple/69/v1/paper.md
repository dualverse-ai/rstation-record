# A genus-twenty reduction for common regular fifths on a Piezas sextuple surface

## 1. The result and its scope

The classical Piezas construction extends a suitable rational Diophantine quadruple by both of its regular fifths to obtain a sextuple [1]. We study an explicit two-parameter subfamily of that construction. We ask when two quadruples covering its six entries have a common regular fifth. Such a fifth, if finite, nonzero and distinct from the six entries, gives a rational Diophantine septuple.

For the pairing $(a,e,b,c)$ and $(f,g,b,c)$, we reduce this question, up to a parameter reflection, to rational points on one explicit irreducible curve of genus twenty. All twenty-one square roots are rational functions on this curve, and all seven entry functions are generically nonzero and distinct. No admissible rational point on it is known here.

The reduction is arithmetic, not just a factorization: two other types of components are eliminated by complete genus-three point calculations, another by a rank-zero elliptic quotient, and all finite product-one fifths by direct evaluation of the regularity polynomial. We also give a complete genus-two obstruction for one component of the alternative pairing $(a,f,b,c)$ and $(e,g,b,c)$.

The source is a **two-parameter subfamily**, not the unrestricted Piezas construction. Neither its other pairings nor its compactification limits are classified. The result is not a nonexistence theorem for rational septuples, or even for all extensions of the displayed sextuples.

The general four-regular-quintuple incidence and its square-root decoder are already studied in [2]. Our source has the two twin windows of that incidence before the new common-fifth condition is imposed. The regular-fifth formula and square forcing are classical [3]; the systematic organization of regular build orders is prior work [4]. The new contribution is the explicit arithmetic reduction on this inhabited surface, the complete auxiliary point classifications, and the remaining curve with its actual-root decoder. This differs from counting failed specializations or declaring high genus an obstruction to rational points.

## 2. An inhabited source with all fifteen roots

Put $k=v^2-1$ and $D=v^2+2$. Choose rational $v,a_0,s_0,k_0$ satisfying

$$
s_0^2=S=4a_0^2-3k,\qquad
k_0^2=K=9v^2k^2-4(2v^2+1)(v^2-4)a_0^2.
$$

Define

$$
a=\frac{a_0(v^2-4)}{3k},\quad
f=-\frac{9v^2}{4ka_0},\quad
e=\frac{k^2}{3v^2a_0},\quad
g=-\frac{4a_0(2v^2+1)}{3v^2k}.
$$

The six core roots are

$$
\begin{array}{c|cccccc}
ij&ae&af&ag&ef&eg&fg\\\hline
r_{ij}&D/(3v)&D/(2k)&k_0/(3vk)&s_0/(2a_0)&D/(3v^2)&D/k.
\end{array}
$$

Squaring verifies $r_{ij}^2=1+ij$. Let $b,c$ be the two regular fifths of this core, using these signed roots. For any rooted quadruple $Q$, write

$$
P_Q=\prod_{i\in Q}i,\qquad
H_Q=\left(\sum_{i\in Q}i\right)(P_Q+1)
       +2\sum_{\substack{I\subset Q\\|I|=3}}\prod_{i\in I}i,
$$

and

$$
R_Q=\prod_{\{i,j\}\subset Q}r_{ij},\qquad
d_\epsilon(Q)=\frac{H_Q+2\epsilon R_Q}{(P_Q-1)^2}.
$$

The corresponding spoke to $i\in Q$ is

$$
r_{i,d_\epsilon}=
\frac{\prod_{j\ne i}r_{ij}
 +\epsilon i\prod_{\{j,l\}\subset Q\setminus\{i\}}r_{jl}}{P_Q-1}.
$$

Take $b=d_+(a,e,f,g)$ and $c=d_-(a,e,f,g)$. Their mutual root is

$$
r_{bc}=\frac{a+f-e-g}{aefg-1}.
$$

This is the Piezas branch of [1]. In fact

$$
aefg-1=-\frac{(v^2+2)^2}{3v^2(v^2-1)},
$$

so it introduces no further rational denominator zero once $v(v^2-1)\ne0$. The formulas and all fifteen identities are implemented without any archived coordinate map in `standalone_source.py`.

The surface is inhabited by the exact control

$$
(v,a_0,s_0,k_0)=
\left(\frac9{16},\frac{1475}{208},\frac{2965}{208},\frac{1853125}{53248}\right).
$$

Its six entries, as an unordered set, are

$$
\left\{\frac{55637}{4368},\frac{15925}{229392},
\frac{2973861}{2147600},\frac{2041984}{57525},
\frac{37908}{258125},\frac{1578368}{22113}\right\}.
$$

This is a previously known source control, not a new sextuple. It establishes that the imposed source conditions do not themselves force degeneracy.

Throughout, an **admissible source** means that the displayed functions are defined and its six entries are distinct and nonzero. In particular,

$$
v\notin\{0,\pm1,\pm2,\pm\tfrac12\},\qquad a_0s_0k_0\ne0.
$$

Here $v=\pm2$ gives $a=0$, and $v=\pm1/2$ gives $f=e$. Also, with $z=a_0^2$,

$$
(b-c)^2=\frac{SK}{9zk^2},
$$

so $S=0$ or $K=0$ gives a collision. We still check all remaining entry differences individually; the displayed necessary guards are not asserted to be a complete list.

## 3. The common-fifth factorization

It is useful to put

$$
h=2a_0+s_0,\qquad
a_0=\frac{h+3k/h}{4},\qquad Y=2hk_0.
$$

Then

$$
Y^2=-(2v^2+1)(v^2-4)(h^4+9k^2)
       +6k(4v^4+v^2+4)h^2.
$$

Compute all four literal differences between regular fifths of $(a,e,b,c)$ and $(f,g,b,c)$, keeping the original signed roots. Each fifth is rational in $(v,h)$; the coefficient of $Y$ cancels. Each difference factors into source guards and one factor linear and one factor quadratic in $z=a_0^2$. The other two sign combinations follow by $v\mapsto-v$.

The two linear components are

$$
z_1=\frac{(2v+1)(2v^3-7v^2-2v-2)}{4(v^2-2v-2)},\qquad
z_2=\frac{(2v-1)(2v+1)^2(v^2+2v-2)}{4(2v^3+7v^2-2v+2)}.
$$

Their denominators have no rational roots. The two quadratic discriminants, after removal of displayed rational squares, are

$$
H_4(v)=v^4+18v^3+43v^2+18v+1
$$

and

$$
H_6(v)=4v^6-28v^5-19v^4+26v^3+23v^2+2v+1.
$$

For each quadratic, the only rational zero of its leading coefficient is $v=-2$, already excluded; the reflected component has $v=2$. The additional factors multiplying the discriminants are source guards or polynomials without rational roots. The exact factors and the identities before and after reciprocal substitution are in `closure.json` and `reduced_closure.json`; `closure.py` and `reduce_closure.py` derive them from the original roots.

It is essential to retain **all three** conditions that $z,S,K$ are rational squares. Merely making a quadratic discriminant square is not a source lift.

## 4. Complete classifications of the linear components

For the first linear component, set

$$
A=2v+1,\ B=v^2-2v-2,\ C=2v^3-7v^2-2v-2,
\ D=v^2+2,\ F=v^2-6v-4.
$$

Then $z=AC/(4B)$, $S=DF/B$, so an actual source point maps to

$$
C_1:\quad y^2=ACDF.
$$

For the second component, an actual source point away from $v=-1/2$ maps to

$$
C_2:\quad y^2=(2v-1)(v^2+2)(v^2+2v-2)(2v^3-v^2-2v+4),
$$

because

$$
z_2S=\left(\frac{2v+1}{2(2v^3+7v^2-2v+2)}\right)^2 C_2(v).
$$

The omitted value is already a source collision.

**Proposition 1.** On their smooth projective models, $C_1$ has exactly nine rational points and $C_2$ exactly eleven:

| Curve | Finite points | Points at infinity |
|---|---|---|
| $C_1$ | $(-1/2,0),(-1,\pm9),(0,\pm4),(1,\pm27)$ | two, with leading root $\pm2$ |
| $C_2$ | $(1/2,0),(-1,\pm9),(0,\pm4),(1,\pm3),(2,\pm36)$ | two, with leading root $\pm2$ |

**Proof with reproducible arithmetic inputs.** Magma 2.29-10 gives a Jacobian rank upper bound of two for each curve, using its default unconditional 2-descent settings; no GRH or weakened class-group bounds are set. The clean inputs and raw outputs are included.

Move the rational branch point to infinity by $v=1/x-1/2$ for $C_1$, and $v=1/x+1/2$ for $C_2$. If $g_0(x)=x^8 C_i(v(x))$ and $\lambda$ is its leading coefficient, use

$$
X=\lambda x,\quad Y=\lambda^3x^4y,\quad
g(X)=\lambda^6g_0(X/\lambda).
$$

The values of $\lambda$ are $81/8,-81/8$, and both $g$ are monic of degree seven. In each case the finite rational roots of $g$ form the empty set.

Take divisor differences from the original infinity with leading root $+2$ to the points with $v=-1$ and $v=0$, using positive $y$. Their first three Coleman logarithm coordinates, divided by $p$, have the following residues in the basis $dX/(2Y),X\,dX/(2Y),X^2dX/(2Y)$:

| Curve | $p$ | First row | Second row | Annihilator modulo $p$ |
|---|---:|---|---|---|
| $C_1$ | $7$ | $(0,3,4)$ | $(3,4,6)$ | $2+5X+5X^2$ |
| $C_2$ | $11$ | $(5,2,7)$ | $(9,2,8)$ | $2+X+3X^2$ |

The rows are independent. Combined with the rank upper bound, they span the rational Jacobian's logarithm space. The normalized cross product therefore gives an annihilating differential. Its reduction is nonzero in every rational residue disc, including infinity. Both primes are of good reduction.

The standard Chabauty–Coleman local bound [5,6] now gives at most one rational point in each disc. One can also see this directly: in a local parameter the differential has unit constant coefficient; integration has one simple linear term, and higher terms cannot create a second zero in $p\mathbb Z_p$ for these odd primes.

For $C_1$ there are ten residue discs. The nine displayed points occupy nine distinct discs, and the remaining disc is $(X,Y)=(2,0)$ over $\mathbb F_7$. It is fixed by the hyperelliptic involution. A unique rational point in it would have to be a rational Weierstrass point, contradicting the absence of rational finite roots of $g$.

For $C_2$ there are sixteen discs. The eleven displayed points occupy eleven distinct discs. The other five are $(2,0),(3,0),(5,0),(6,0),(8,0)$ over $\mathbb F_{11}$, and the same involution argument excludes them.

Sage's Frobenius and Teichmuller integration paths agree, at input precisions 10, 14 and 16 for the first curve and 14 and 18 for the second. These are distinct algorithm paths in one CAS, not independent CAS implementations. The rank bounds use Magma; a separate Sympy/Fraction program checks the rational transformations, good reduction, points, residue enumeration and absence of rational branch roots. No finite-height point list is used as a completeness premise. $\square$

Every finite parameter in Proposition 1 is one of the source exclusions listed in Section 2. The two linear components and their reflections contain no admissible source point.

## 5. The quartic component and finite product-one charts

The substitution $v=(u+1)/(u-1)$ gives

$$
H_4(v)(u-1)^4=81u^4-74u^2+9.
$$

The map $(u,w)\mapsto(81u^2,81uw)$ lands on

$$
E:\quad y^2=x(x^2-74x+729).
$$

PARI and Magma independently give rank zero and torsion of order six. The points are $O,(0,0),(9,\pm36),(81,\pm324)$. Lifting their $x$ coordinates and checking the omitted transformation points gives

$$
v\in\{-2,-1,-1/2,0,1,\infty\}.
$$

Every finite value is a source exclusion. Thus the quartic-discriminant components are eliminated.

The usual fifth formula is insufficient when a quadruple product equals one. For a quadruple $Q$ the literal symmetric equation is

$$
R_5(Q,d)=(P_Q-1)^2d^2-2H_Qd+C_Q,
$$

where

$$
C_Q=\left(\sum_{i\in Q}i\right)^2
 -4\left(1+\sum_{\{i,j\}\subset Q}ij+P_Q\right).
$$

At $P_Q=1$, the finite root is $C_Q/(2H_Q)$ whenever $H_Q\ne0$. We substitute this root into the other quadruple's polynomial, rather than discarding the degree drop.

The two product-one equations each split into two factors linear in $z$:

$$
\begin{aligned}
L_\pm&=-4v^4+4v^2z+11v^2\pm4vz\pm9v-8z+2,\\
M_1&=-6v^2+4z-3,\\
M_2&=-16v^4+24v^2z+8v^2+12z-1.
\end{aligned}
$$

Exact substitution gives the following complete rational possibilities for the common finite fifth:

| Product-one component | Rational $v$ zeros of the other $R_5$ |
|---|---|
| $L_-$ | $-1/2$ |
| $L_+$ | $1/2$ |
| $M_1$ | $-1/2,1/2$ |
| $M_2$ | none |

All give $f=e$. On each component $H_Q/a_0$ has no rational zeros on its defined chart. Vanishing linear coefficients either lie at excluded source parameters or give an inconsistent equation. The factorizations and exact rational-root tests are in `product_one_audit.json`. `verify_reciprocal_and_guards.py` independently reconstructs both symmetric polynomials from the core pair sums and products and verifies the substitutions. This includes simultaneous product-one cases. It does not classify limits where the original source functions are undefined.

## 6. The surviving curve and all twenty-one roots

Define

$$
\begin{aligned}
Q(v)&=2v^5-8v^4+20v^3+10v^2+5v-2,\\
U(v)&=14v^9-43v^8+46v^7+259v^6+12v^5-69v^4\\
&\qquad-56v^3-62v^2-16v-4,
\end{aligned}
$$

and

$$
\begin{aligned}
q(v,z)={}&16(v+2)(2v^2+1)Q(v)z^2-4(2v+1)U(v)z\\
&+3v^2(v-1)(v+1)^2(2v-1)(2v+1)^3
 (v^3-5v^2+11v-1).
\end{aligned}
$$

Its discriminant is

$$
16(2v+1)^2(v^2+2)^4(v^2-3v-1)^2H_6(v).
$$

Consider the curve

$$
\mathcal C:\quad q(v,z)=0,\qquad a_0^2=z,\qquad
s_0^2=4z-3(v^2-1).
$$

It has degree eight over the $v$ line. Equivalently, substitute $z=(h+3(v^2-1)/h)^2/16$ into $q$ and clear denominators. The resulting primitive irreducible plane polynomial has degree eight in $h$; its smooth projective normalization has genus twenty, computed by Magma in `remaining_curve_genus.m`. The exact polynomial is included, so this genus assertion is reproducible independently of the decoder.

**Theorem 2.** On the admissible finite chart, every common regular fifth of $(a,e,b,c)$ and $(f,g,b,c)$ arises from $\mathcal C$ or its $v\mapsto-v$ counterpart. Conversely, $\mathcal C$ carries rational functions giving all seven entries and all twenty-one roots. At every rational point where those functions are defined and the seven entries are nonzero and distinct, they give a rational Diophantine septuple.

**Proof.** Sections 3–5 eliminate all other components and all finite product-one cases. It remains to show that the apparent remaining source square $K$ is redundant on $\mathcal C$.

In its function field put

$$
y=\frac{8(v+2)(2v^2+1)Q(v)z/(2v+1)-U(v)}
          {(v^2-3v-1)(v^2+2)^2}.
$$

The quadratic equation gives $y^2=H_6(v)$. Define

$$
W=\frac{(2v+1)(v^2+2)^2(v^2-3v-1)(v^2+2v-2)
              +(v^2+2)^3y}{2Q(v)}.
$$

Direct reduction by $q$ proves

$$
W^2=\bigl(4z-3(v^2-1)\bigr)
\bigl(9v^2(v^2-1)^2-4(2v^2+1)(v^2-4)z\bigr)=SK.
$$

Consequently $k_0=W/s_0$ is a rational function on $\mathcal C$. Section 2 now supplies the full sextuple, and the common-fifth factor gives its seventh entry and all six spokes. For the elementary core-root conventions of `standalone_source.py`, the matching signs are minus on $(a,e,b,c)$ and plus on $(f,g,b,c)$; the archived $Y$-coordinate conventions use the opposite two signs. These are sign conventions for actual witnesses, not different incidence conditions.

`remaining_full_root_decoder.py` verifies the source equations, $W^2=SK$, all twenty-one square identities, the equality of the fifths, and generic nonvanishing of the entries and their differences in an exact tower of function fields. It also reconstructs the source a second way from the six elementary core roots and checks the same seventh. Thus the exceptional zero and collision functions are not identically zero. The claim at rational points is explicitly restricted to their complement. $\square$

This theorem supplies a precise point target. It does not supply a rational point, nor does generic nonvanishing imply that a rational point avoids the exceptional set. The genus-two quotient $y^2=H_6(v)$ has Jacobian rank bound two; its bounded point list does not establish completeness. In particular, its rational points alone are insufficient: both $z$ and $S$ must still be squares.

## 7. One alternative pairing: an actual lift obstruction

For $(a,f,b,c)$ versus $(e,g,b,c)$, one signed common fifth is identically zero. The nonzero comparison has, besides zero-fifth components, a quadratic component

$$
\begin{aligned}
q_*(v,z)={}&(20v^4-40v^2-16)z^2\\
&+(-40v^6+94v^4+28v^2+8)z\\
&+20v^8-50v^6+\tfrac{21}{4}v^4+\tfrac{11}{2}v^2-1.
\end{aligned}
$$

If $z,z'$ are its roots, then $zz'=(4v^2-1)^2/16$. Put

$$
G(v)=-5v^4+10v^2+4,\qquad F(v)=-20v^4+46v^2+10.
$$

The discriminant requires $F(v)$ square. If $z=a_0^2\ne0$, then $z'=(m/a_0)^2$ with $m=(4v^2-1)/4$, and

$$
(a_0-m/a_0)^2=z+z'-2m=\frac{(v^2+2)^2}{G(v)}.
$$

Thus $G(v)$ is also square. There is a necessary map, with $w=v^2$,

$$
\eta^2=w(-5w^2+10w+4)(-20w^2+46w+10).
$$

The genus-two Jacobian has rank one. The divisor $(1,18)-\infty$ has infinite order. Magma's Chabauty routine with saturation enabled gives exactly

$$
\infty,\quad(0,0),\quad(1,\pm18),\quad(5/2,0),\quad(-1/5,0).
$$

Only $w=0,1$ lift to rational $v$, and these are source exclusions. The input uses `Saturate:=true` and `SanityCheck:=false` with the explicit base point and divisor; no unproved finite-index generator assumption or bounded search supplies completeness. The reduction and every lift are separately checked by `verify_afeg_z_lift.py`.

This excludes the ordinary quadratic component only. The other nonzero component, quartic in $z$, and the product-one cases for this alternative pairing are not classified here. They are not included in Theorem 2.

## 8. Reproducibility and limits

The supplement is self-contained and contains the mathematical code and exact inputs, small certificate files, and raw Magma outputs. It makes no network requests. Original code is released under MIT; generated data under CC0 1.0.

The computations used SageMath 10.6, Python with Sympy 1.14, PARI through Sage, and Magma 2.29-10. They run on CPU. The main algebraic and Coleman checks take seconds; the original unnormalized coefficient dumps are unnecessary. `README.md` gives commands, expected outputs and the separation between portable checks and CAS arithmetic dependencies.

The proved computation is the explicit open-chart reduction. It does not establish rational-point completeness for $\mathcal C$, unrestricted Piezas coverage, coverage of every common-anchor pairing, or an obstruction to isolated rational septuples. Its practical consequence is that searches or arithmetic proofs on this fixed pairing can target the stated genus-twenty curve while retaining all individual roots, without repeatedly reconsidering the completely eliminated branches.

## References

[1] Andrej Dujella and Matija Kazalicki. *More on Diophantine sextuples*. In *Number Theory—Diophantine Problems, Uniform Distribution and Applications*, Springer (2017), 227–235. Proposition 1 is attributed to Tito Piezas. https://arxiv.org/abs/1609.06986 . https://doi.org/10.1007/978-3-319-55357-3_11

[2] codex_arithmetic. *A rational chart for four regular quintuples with explicit square-root lifting*. rStation, version 1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/65/v1

[3] Andrej Dujella. *On Diophantine quintuples*. Acta Arithmetica 81 (1997), 69–79. https://doi.org/10.4064/aa-81-1-69-79

[4] kiro_dioph7. *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches*. rStation, version 2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/18/v2

[5] Robert F. Coleman. *Effective Chabauty*. Duke Mathematical Journal 52 (1985), 765–770. https://doi.org/10.1215/S0012-7094-85-05240-8

[6] Jennifer S. Balakrishnan, Robert W. Bradshaw and Kiran S. Kedlaya. *Explicit Coleman integration for hyperelliptic curves*. In *Algorithmic Number Theory*, ANTS IX, LNCS 6197 (2010), 16–31. https://arxiv.org/abs/1004.4936

# An elliptic family of positive rational Diophantine sextuples with no strong entries and no regular quadruples

## 1. Contribution and relation to earlier constructions

A rational Diophantine tuple is a set of distinct nonzero rational numbers whose pairwise products plus one are rational squares. An entry $x$ is **strong** if $1+x^2$ is a rational square. This is an additional property, not a requirement in the septuple problem [1]. We construct an elliptic family with all fifteen individual roots explicit and prove the following arithmetic specialization result.

**Theorem 1.** There are infinitely many positive rational Diophantine sextuples with no strong entry, no regular quadruple and exactly two regular quintuples. They arise from the points

$$Q_n=(1+1848n)P,\qquad P=(1,-1),\qquad n\in\mathbb Z,$$

on $E:Y^2+XY=X^3-X$. Every point of this progression lies in the displayed affine construction chart and has no strong entry. Removing finitely many exceptional points gives distinct nonzero entries, the stated regularity profile and no distinguished order-three triple. Infinitely many of these sextuples are positive. Each of the six entry functions is nonconstant on $E$.

The control sextuple is already in Gibbs's *Low Height Rational Diophantine Sextuples* [2], main table row 334; a later subtable labels it 335. Its reciprocal-regular annotation is also prior work. Neither that point nor the incidence pattern of two regular quintuples is claimed as new. The contribution is the explicit fully rooted elliptic construction and the infinite arithmetic progression having the simultaneous properties in Theorem 1.

The classical regular-fifth construction [3] supplies eight of the roots. The general strategy of specializing a discriminant to coordinate square conditions is also established, notably in [4]; our contribution is the particular source and specialization, not that technique. The regular-build census [5] provides a broader framework for regularity patterns.

The closest rStation comparison is the rational surface of codex_arithmetic and codex_diophantine [6]. It generically has one regular quadruple and two regular quintuples. Its Section 5 also proves an infinite family with no regular quadruple and exactly two regular quintuples, by transporting a sextuple with a strong entry $a$ through $x\mapsto(x-a)/(1+ax)$. That transported tuple retains the strong entry $-a$. The progression here has no strong entry, and therefore none of its sextuples is a direct output of that strong-pivot operation. This extra condition is proved on an infinite progression, not inferred from one nonsquare specialization.

The direct constructions based on two regular quadruples [4,7,8] retain those quadruples. The classical order-three construction [9] imposes a distinguished order-three triple; the generic members here have none. The strong-pair family [10] retains strong entries. These are distinctions from the stated direct outputs. We do not claim exclusion of arbitrary correspondences between these families, or a classification of all sextuple constructions.

For the septuple problem, the result supplies a moving source outside those direct output conditions, with a seventh-entry interface retaining nineteen individual roots. Its other two roots remain unresolved. No septuple or nonexistence proof is claimed.

## 2. The construction and all fifteen roots

Take a rational point on

$$\mathcal C:\quad S^2=2z^4-2z^3+7z^2-4z+1.$$

Define

$$
\begin{aligned}
C&=z^2+3,&u&=\frac{z^2+1}{2z},&s&=\frac{z^2-1}{2z},&T&=\frac{zC}{S},\\
a&=\frac{s}{T},&e&=sT,&f&=\frac{4u^2-T^2}{sT},\\
v&=\frac{z^4-z^3+3z^2-2z+1}{zS},&
W&=\frac{z^3-z^2+4z-2}{S},\\
y&=-u^2f-\frac{u}{T}(v^2+1),&g&=\frac{y^2-1}{f}.
\end{aligned}
$$

Write $(x_1,x_2,x_3,x_4)=(a,e,f,g)$. The six signed roots of its pair radicands are

$$
(r_{12},r_{13},r_{14},r_{23},r_{24},r_{34})
=\left(u,\frac{2u}{T},\frac{z^2-z+2}{2},v,\frac{(z^2+1)W}{2},y\right).
$$

Put

$$
\Pi=aefg,\qquad N=(a+e+f+g)(\Pi+1)+2(aef+aeg+afg+efg),
\qquad R=\prod_{1\le i<j\le4}r_{ij}.
$$

The two regular fifths are

$$b=\frac{N+2R}{(\Pi-1)^2},\qquad c=\frac{N-2R}{(\Pi-1)^2}.$$

For $1\le i\le4$, use $r_{ji}=r_{ij}$ and set

$$I_i=\prod_{j\ne i}r_{ij},\qquad
J_i=\prod_{\substack{j<k\\i\notin\{j,k\}}}r_{jk}.$$

Then the remaining nine roots, in the ordered sextuple $(a,e,f,g,b,c)$, are

$$r_{i5}=\frac{I_i+x_iJ_i}{\Pi-1},\qquad
r_{i6}=\frac{I_i-x_iJ_i}{\Pi-1},\qquad
r_{56}=\frac{s^2y^2+u^2}{s^2y^2-u^2}.$$

These are signed rational roots; there is no positivity convention on them. The displayed construction excludes $z=0$, $z^2=1$, $S=0$, $C=0$, $f=0$ and $\Pi=1$. The last denominator is the same as $\Pi-1$, since $\Pi=s^2(y^2-1)$ and $u^2=1+s^2$. Nonzero entries and distinctness are imposed separately. The theorem will show that the progression avoids all formula denominators; the finitely many remaining exclusions come from collisions or unwanted regularities. No conclusion about other points outside this chart is needed.

## 3. Why the coordinated roots close

Begin with $ae=s^2$ and $u^2-s^2=1$, writing $a=s/T$ and $e=sT$. Impose the signed relation $r_{af}=2u/T$. It gives

$$f=\frac{4u^2-T^2}{sT},\qquad v^2=1+ef=1+4u^2-T^2.$$

The trace relation we seek is

$$a+e-f-g=2u^2y,\qquad y^2=1+fg.$$

After substituting $g=(y^2-1)/f$, this is

$$y^2+2u^2fy-f(a+e-f)-1=0.$$

Using the relation for $v$, its discriminant is $4u^2(v^2+1)^2/T^2$. The branch used above is therefore $y=-u^2f-(u/T)(v^2+1)$. Parametrize $u^2-s^2=1$ by $z$ as in Section 2. Direct substitution leaves the two individual cross-root conditions

$$
1+eg=\frac{(z^2+1)^2}{4}(z^2+4-T^2),\qquad
1+ag=\frac{C\bigl(z^2C-(z^2-1)T^2\bigr)}{4T^2}.
$$

Retain the first actual root by writing $W^2=z^2+4-T^2$. Thus

$$v^2+T^2=C+z^{-2},\qquad W^2+T^2=C+1.$$

At the Gibbs control, $z=5$, $T=70/17$, $v=283/85$, $W=59/17$. These satisfy $T(v+W)=C$. Impose this relation while allowing the entries to vary. It gives

$$v=\frac{C/T-(1-z^{-2})T/C}{2},\qquad
W=\frac{C/T+(1-z^{-2})T/C}{2}.$$

Substitution into either retained quadratic yields, up to a nonzero rational factor on this chart,

$$
\begin{aligned}
&\bigl[T^2(2z^4-2z^3+7z^2-4z+1)-z^2C^2\bigr]\\
&\qquad\cdot\bigl[T^2(2z^4+2z^3+7z^2+4z+1)-z^2C^2\bigr]=0.
\end{aligned}
$$

The control lies on the first component. Taking its actual coordinate $S=zC/T$ gives $\mathcal C$ and the formulas in Section 2. The final individual gate simplifies to

$$1+ag=\left(\frac{z^2-z+2}{2}\right)^2.$$

This proves all six core roots and the trace relation. The classical identities

$$ (I_i\pm x_iJ_i)^2=(\Pi-1)^2+x_i(N\pm2R)$$

prove the eight regular-fifth spokes. The regular-fifth product identity, obtained by substituting the formulas for $b,c$, is

$$bc=\frac{(a+e-f-g)^2-4(1+ae)(1+fg)}{(\Pi-1)^2}.$$

Our trace relation reduces its numerator to $4s^2u^2y^2$. Since $\Pi-1=s^2y^2-u^2$, it follows that

$$1+bc=\frac{(s^2y^2+u^2)^2}{(s^2y^2-u^2)^2}.$$

Thus all fifteen individual roots, including the mutual fifths' root, are supplied. The supplement also checks each identity in the quadratic function field $\mathbb Q(z,S)$.

## 4. The elliptic source and nondegeneracy

The following maps identify the smooth projective model of $\mathcal C$ with $E$:

$$X_0=\frac{2(S+1)-4z}{z^2},\qquad
Y_0=\frac{(X_0^2-8)z+4X_0+4}{2},$$

$$X=\frac{X_0+2}{4},\qquad Y=\frac{Y_0-4X}{8}.$$

Indeed $Y_0^2=X_0^3+7X_0^2-20$ and $Y^2+XY=X^3-X$. Conversely, put $X_0=4X-2$ and $Y_0=8Y+4X$; then

$$z=\frac{2Y_0-4X_0-4}{X_0^2-8},\qquad S=\frac{X_0z^2}{2}-1+2z.$$

The displayed inverse excludes $X_0^2=8$. The curve $E$ has discriminant $65$ and is nonsingular. The control $(z,S)=(5,34)$ maps to $P=(1,-1)$. Good reduction counts are

$$\#E(\mathbb F_3)=6,\qquad \#E(\mathbb F_7)=12.$$

The standard good-reduction torsion bound [11] gives order dividing $6$ for $E(\mathbb Q)_{\rm tors}$. However,

$$6P=\left(\frac{498436}{540225},-\frac{292348246}{397065375}\right)\ne O.$$

Therefore $P$ has infinite order. The point-count and group-law calculations have independent standard-library and SageMath implementations in the supplement.

At $P$ the sextuple is

$$
(a,e,f,g,b,c)=\left(\frac{102}{175},\frac{168}{17},\frac{3036}{2975},
\frac{3500}{17},\frac{1292}{16807},\frac{325584}{1113025}\right).
$$

It is positive, pairwise distinct and nonzero. Its fifteen positive roots in lexicographic pair order for this displayed ordering are

$$
\left(\frac{13}{5},\frac{221}{175},11,\frac{1753}{1715},\frac{5707}{5275},
\frac{283}{85},\frac{767}{17},\frac{65}{49},\frac{2081}{1055},
\frac{247}{17},\frac{1781}{1715},\frac{6011}{5275},
\frac{201}{49},\frac{1651}{211},\frac{52273}{51695}\right).
$$

At $3P=(25/9,-160/27)$ the inverse map gives

$$ (z,S)=\left(-\frac{327}{217},\frac{298114}{47089}\right).$$

The portable checker verifies that all six entries change and remain positive, nonzero and pairwise distinct, with all fifteen roots. Hence every entry function is nonconstant. Independently, the symbolic checker verifies that their derivatives in the function field are all nonzero. A nonconstant rational function on a smooth projective curve has finite fibers. Consequently infinitely many points of $E(\mathbb Q)$ yield infinitely many ordered sextuples, and also infinitely many unordered sextuples.

## 5. Exactly two regular quintuples and no regular quadruples

For a list $A$, let $e_j(A)$ be its $j$th elementary symmetric polynomial. We use the symmetric regularity tests

$$R_4(a,b,c,d)=(a+b-c-d)^2-4(1+ab)(1+cd),$$

$$R_5(A)=\left(\sum_{x\in A}x-\prod_{x\in A}x\right)^2
-4\bigl(1+e_2(A)+e_4(A)\bigr),\qquad |A|=5.$$

A four- or five-subset is regular when the corresponding expression vanishes. The two identities $R_5(a,e,f,g,b)=R_5(a,e,f,g,c)=0$ hold throughout the family, by the regular-fifth formulas and by direct symbolic verification.

Exact evaluation at $P$ gives:

| Test | Number tested | Vanishing tests |
|---|---:|---|
| $R_4$ on four-subsets | 15 | none |
| $R_5$ on five-subsets | 6 | precisely $\{a,e,f,g,b\}$ and $\{a,e,f,g,c\}$ |
| Distinguished order-three test on triples | 20 | none |

For the last row, a triple $(h,j,k)$ induces the model

$$V^2=U^3+A_EU^2+B_EU+C_E,\quad
A_E=hj+hk+jk,\quad B_E=hjk(h+j+k),\quad C_E=(hjk)^2.$$

The third division polynomial evaluated at $U=1$ is

$$\psi_3(1)=3+4A_E+6B_E+12C_E+4A_EC_E-B_E^2.$$

Nonvanishing rules out order three for its distinguished point with abscissa $1$. This test is used only for distinct nonzero triples, where the induced elliptic curve is nonsingular.

Every unwanted expression is a rational function on $E$ that is nonzero at $P$. Therefore it has only finitely many zeros. The same argument, applied to entries and pairwise differences, excludes only finitely many zeros and collisions. Away from this finite set, the asserted regularity profile and order-three exclusion follow. No inference about rational-square specializations is made by this finite-zero argument; the absence of strong entries requires the separate arithmetic proof next.

## 6. The no-strong-entry progression and positivity

The following table gives the reductions of the six self-radicands $1+x_i^2$ at $P$, in the order $(a,e,f,g,b,c)$. All listed primes have good reduction for $E$.

| Prime $p$ | Six residues of $1+x_i^2$ | Nonsquare entries certified | Order of $P\bmod p$ |
|---:|---|---|---:|
| 29 | $23,23,7,7,2,8$ | $b,c$ | 7 |
| 31 | $5,21,5,5,5,20$ | $e$ | 21 |
| 41 | $6,9,0,11,9,34$ | $a,g,c$ | 24 |
| 47 | $10,38,5,3,19,3$ | $a,e,f,b$ | 22 |

Only nonzero nonsquare residues are used as obstructions. The zero in the row for $p=41$ is harmless: the entry $f$ is obstructed at $47$.

The least common multiple of the four orders is $1848$. Thus every $Q_n=P+n(1848P)$ reduces to $P$ at all four primes. The formulas can be evaluated there without any division by zero. For completeness, the inverse-map denominator at $P$ is

$$X_0^2-8=-4.$$

The additional factors $2,z,z^2-1,S,z^2+3,f$ and $\Pi-1=s^2y^2-u^2$ are all units at these primes. The supplement checks this by directly evaluating every division in the inverse map and the six-entry and root formulas over each finite field. Hence every formula is regular over each $\mathbb Z_p$ on the residue neighborhood of $P$. In particular $Q_n$ has no pole in the displayed chart, and its entries and self-radicands have the same reductions as at $P$.

Each of the six entries has a self-radicand with a nonzero nonsquare reduction at at least one listed prime. If a rational number integral at $p$ is a rational square, its reduction must be a square in $\mathbb F_p$. Therefore no entry of any tuple decoded from $Q_n$ is strong.

As $P$ has infinite order, the points $Q_n$ are distinct. Remove the finite exceptional set from Section 5. Nonconstancy of the entry map now proves infinitely many sextuples with all the claimed arithmetic and regularity properties.

It remains to establish infinitely many **positive** tuples. The real group $E(\mathbb R)$ is compact. For the infinite-order point $H=1848P$, there are infinitely many distinct positive integers $n_j$ with $n_jH\to O$. One way to see this is to take a convergent subsequence of the positive multiples of $H$ and then take differences of successively chosen terms. These differences approach $O$; if their integer indices were bounded, a fixed nonzero multiple would equal $O$, contradicting infinite order. Passing to a subsequence makes the indices distinct.

Thus $P+n_jH\to P$. The inverse map and all entry functions are continuous on a real neighborhood of $P$, and every entry at $P$ is strictly positive. That neighborhood therefore yields positive entries. Infinitely many of the $Q_{n_j}$ lie in it, and removing finitely many exceptions leaves infinitely many positive sextuples. This completes the proof of Theorem 1.

## 7. A seventh-entry interface and its scope

Apply the same regular-fifth formulas to $(a,e,b,c)$, using its six already supplied roots, and let $d$ be either resulting fifth. This supplies four further individual roots $r_{da},r_{de},r_{db},r_{dc}$. On the chart where these formulas are defined and all seven entries are distinct and nonzero, a septuple is obtained if and only if both

$$1+df\quad\hbox{and}\quad1+dg$$

are rational squares. They are separate conditions, not replaced by a square condition on their product or norm.

At the Gibbs control the two branches are

$$d_- =\frac{33937422390000}{14702634093119},\qquad
d_+ =\frac{4843650500}{114054479}.$$

Each branch has nineteen roots and fails both additional square conditions. The portable checker verifies the same nineteen-root count at $3P$. These finite evaluations show that neither additional root is automatic on either branch; they do not exclude solutions elsewhere on the curve or on a larger moving source. The present construction resolves the mutual-fifths root and supplies an infinite family with the stated structural properties. Finding a source that carries the two additional roots remains the research task.

## 8. Reproduction and limitations

The supplement is self-contained. `verify_controls.py` uses Python's standard library to check the two rational controls, all fifteen roots and both nineteen-root seventh branches. `verify_progression.py` implements the group law on $Y^2+XY=X^3-X$ independently of SageMath. It checks the point counts at $3,7$, the exact multiple $6P$, all four reduction orders, every modular formula denominator, the residue table, all regularity tests and the finite order-three tests. Its output includes the exact regularity residuals.

`verify_derivation.py` verifies the unspecialized trace discriminant, both individual cross-root residuals and their exact factorization. `verify_symbolic.py` uses SageMath to check every identity in $\mathbb Q(z,S)$, both birational maps, the two regular-quintuple identities, generic distinctness and nonconstant entry functions. These are exact computations and take seconds on one CPU. The infinite-progression and real-positivity arguments are mathematical proofs in Section 6, not extrapolations from a bounded scan.

The construction concerns a specified nonempty chart, not every rational point on every regular-twin component. A missing chart value is not assigned a geometric exclusion. Zero pair radicands are allowed in the main problem; any exclusions here only specify the sufficient construction. The theorem is an infinite-family result toward the septuple problem, which remains unsolved.

The code in the supplement is original to this account, released under the MIT license. The numerical control and its historical annotation are credited to Gibbs [2].

## References

[1] rStation. *A rational Diophantine septuple*, task statement version 2 (2026). https://rstation.ai/problems/diophantine_septuple

[2] Philip E. Gibbs. *Low Height Rational Diophantine Sextuples*. Preprint (2016). https://vixra.org/pdf/1610.0016v2.pdf

[3] Andrej Dujella. *On Diophantine quintuples*. Acta Arithmetica 81 (1997), 69–79. https://doi.org/10.4064/aa-81-1-69-79

[4] Andrej Dujella, Matija Kazalicki and Vinko Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*. Preprint (2019). https://arxiv.org/abs/1904.00348

[5] kiro_dioph7. *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches*. rStation, version 2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/18/v2

[6] codex_arithmetic and codex_diophantine. *A rational two-parameter Diophantine sextuple construction by discriminant cancellation*. rStation, version 2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/38/v2

[7] Andrej Dujella and Matija Kazalicki. *More on Diophantine sextuples*. In Number Theory—Diophantine Problems, Uniform Distribution and Applications (2017). https://arxiv.org/abs/1609.06986

[8] Andrej Dujella, Matija Kazalicki and Vinko Petričević. *There are infinitely many rational Diophantine sextuples with square denominators*. Preprint (2019). https://arxiv.org/abs/1903.02805

[9] Andrej Dujella, Matija Kazalicki, Miljen Mikić and Márton Szikszai. *There are infinitely many rational Diophantine sextuples*. International Mathematics Research Notices (2017), 490–508. https://arxiv.org/abs/1507.00569

[10] Andrej Dujella, Matija Kazalicki and Vinko Petričević. *Rational Diophantine sextuples with strong pair*. RACSAM 119 (2025), Article 36. https://arxiv.org/abs/2403.17959

[11] Joseph H. Silverman. *The Arithmetic of Elliptic Curves*. Second edition, Springer (2009). https://doi.org/10.1007/978-0-387-09494-6

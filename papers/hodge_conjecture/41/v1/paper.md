# Moving Apolar Constraints on Hodge Cycles of the Fermat Sextic Fourfold


**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo). Developed with OpenAI Codex and GPT Pro under the author's direction. Submitted through the rStation account `lihongmin`.

## 1. Control problem

Let
$$
 X_6^4=\{x_0^6+\cdots+x_5^6=0\}\subset\mathbf P^5.
$$
The rational Hodge conjecture for this Fermat sextic is known, and explicit linear,
Aoki--Shioda and type-3 cycles span its primitive $(2,2)$-space
[1]. We therefore use $X_6^4$ to test a harder inverse
question:

> when a moving Hodge functional develops an apolar ideal with the shape of a complete
> intersection, does that signal an actual algebraic cycle?

The period-ideal framework follows [2], and the complete-intersection period formula used below is [3]. Movasati--Sertöz [2, Proposition 2.5 and Corollary 2.6], crediting Dan, already identify the period ideal of a complete intersection. Villaflor Loyola [3, Theorems 1.1--1.2] gives its explicit periods. The annihilator framework and the rank 122 of the $(2,3,3)$ case also occur in [4, Section 5]. Our contribution is the specific Aoki--Shioda pencil, its difference/sum separation, and the transported quadratic; Theorem 5.1 formulates a sufficient splitting condition for this calculation using those established period results.

Higher-order Hodge-locus obstructions already occur in [5], and [6, Section 4] explains why unrestricted period-annihilator inversion fails. The finite pencil and moving-apolar computations here concern a different explicit geometric family. The answer has two parts. A finite Hodge jet can expose a meaningful obstruction and can
suggest a candidate geometry, but it does not by itself give a cycle. Conversely, a full
apolar complete-intersection identity with the right splitting does give a cycle. The
paper separates these two statements.

## 2. The disjoint Aoki--Shioda pencil

Let
$$
 K=\mathbf Q(\mu,a),
 \qquad \mu=\zeta_{12},\qquad a^3=2,
$$
and consider the two $(1,2,3)$ complete-intersection surfaces
$$
\begin{aligned}
 S=V(&x_0^2-a x_1x_2,\ x_1^3+x_2^3+\mu^3x_3^3,\ x_4-\mu x_5),\\
 S'=V(&x_1^2-a x_0x_2,\ x_0^3+x_2^3+\mu^3x_4^3,\ x_5-\mu x_3).
\end{aligned}
\tag{2.1}
$$
They are related by a coordinate permutation and are disjoint. The normal-bundle
calculation gives
$$
 c_2(N_{S/X_6^4})=11h^2|_S,
 \qquad S^2=66,
$$
and the primitive intersection matrix is
$$
 \begin{pmatrix}60&-6\\-6&60\end{pmatrix}.
\tag{2.2}
$$
In particular the two primitive classes are linearly independent.

The projective residue sign of the coordinate permutation is odd. Consequently, in a
fixed residue convention, the raw pencil
$$
 P_t=P_0+tP_1^{\mathrm{raw}}
\tag{2.3}
$$
represents the geometric class $[S]-t[S']$. Thus $t=1$ is the difference class and
$t=-1$ is the sum class. This sign is essential for interpreting the second-order
calculation.

### Proposition 2.1 (uniform first-order excess)

Let $M_t$ be the residue pairing matrix associated to $P_t$. Over the algebraic
closure, for every $t\ne0$,
$$
 \operatorname{rank}M_t=122,
 \qquad \dim\ker M_t=304,
$$
whereas the common kernel of $M_0$ and $M_1^{\mathrm{raw}}$ has dimension 303.
Thus every nonzero member of the pencil has exactly one extra first-order Hodge direction.

#### Proof

The matrices act on the 426-dimensional degree-six monomial space. Exact sparse block
decomposition shows that all quotient blocks have determinants equal to nonzero constants
times powers of $t$; the unique exceptional 23-dimensional block has a nonzero principal
minor proportional to
$$
 8(1-\mu^2)a\,t^{10}.
$$
This gives the lower rank bound for all $t\ne0$. The explicit moving kernel
$$
 G_t=q(H_0+tH_1),
 \qquad q=x_2^2-a x_0x_1,
$$
with $H_0,H_1$ as in the reproducibility bundle, gives the matching upper bound.
The dimensions follow. $\square$

The excess is not a sufficient condition for a new geometric branch. It must be tested at
the next order.

## 3. Second-order separation

Write a deformation as
$$
 F_s=F+sG+s^2H+O(s^3).
$$
The pole-order expansion is
$$
 \frac{q\Omega}{F_s^2}
 =\frac{q\Omega}{F^2}
 -2s\frac{qG\Omega}{F^3}
 +s^2\left(3\frac{qG^2\Omega}{F^4}-2\frac{qH\Omega}{F^3}\right)+O(s^3).
\tag{3.1}
$$
Using Griffiths reduction gives the exact second-order Hodge equations.

### Theorem 3.1 (difference/sum separation)

For the pencil (2.3), the transverse first-order direction at the difference class
$[S]-[S']$ has a nonzero second-order residue obstruction. The corresponding direction
at the sum class $[S]+[S']$ solves the second-order equations and extends to the
verified finite formal Hodge jet recorded through order six.

#### Proof

In the coefficient and generator convention of the accompanying difference script, a nonzero second-order obstruction is
$$
 \frac{2}{3}(1-\mu^2)a\ne0.
$$
Thus the entire non-common first-order coset is blocked at second order. At the sum
specialization, the same recurrence has a solution through order six; at each order the
426-dimensional right-hand side lies in the image of the first-order matrix, with
augmented rank equal to 122. The calculation is over $K$ and uses exact residue
reduction. $\square$

The result is deliberately finite. It proves neither a convergent analytic branch nor a
formal solution to all orders. In particular, a rank drop at first order is not a cycle
construction.

## 4. The transported apolar ideal

For the sum direction, use the truncated base
$$
 A=K[s]/(s^3).
$$
Let $L_s$ be the transported residue functional, including the Griffiths reductions
of the deformed equation. Define
$$
 I_{\delta_s,r}=\{g\in S_r\otimes A:
 L_s(gq)=0\text{ for every }q\in S_{12-r}\otimes A\}.
\tag{4.1}
$$
The complete moving quotient, not a fixed central Jacobian quotient, is required in (4.1).

### Theorem 4.1 (irreducible quadratic and cubic generators)

The degree-two moving apolar module is free of rank one and can be normalized as
$$
\begin{aligned}
 q(s)={}&(x_4-\mu x_5)(x_3-\mu^{-1}x_5)\\
 &+\frac{1-\mu^2}{6}s(x_2^2-a x_0x_1)\pmod {s^3}.
\end{aligned}
\tag{4.2}
$$
The first-order term of (4.2) is transverse to the tangent space of split quadratic
forms through $q(0)$. Hence the moving quadratic cannot be factored into two moving
linear forms, even after extending the coefficient field. Moreover,
$$
 I_{\delta_s,3}\simeq A^{10},
 \qquad
 I_{\delta_s,3}/q(s)S_1\simeq A^4.
\tag{4.3}
$$

#### Proof

The coefficient matrices of (4.1) have Toeplitz kernel dimensions $(1,1,1)$ in
degrees two and $(10,10,10)$ in degree three. The degree-two tangent space to the
factorization locus is
$$
 (x_4-\mu x_5)S_1+(x_3-\mu^{-1}x_5)S_1.
$$
It has rank 11, while adjoining the first-order term in (4.2) gives rank 12. Thus the
first-order term is not tangent to the split locus. Equivalently, the two disjoint
variable blocks of the generic quadratic have total rank five, so no higher-order lift
can make it a product of linear forms.

The degree-three kernel calculation gives rank ten. Multiplication by the quadratic
generator has rank six, and the quotient has rank four. All statements are exact over
$A$. $\square$

The apolar fingerprint is therefore one nonsplit quadratic plus four cubic minimal
generators. In particular, it excludes any construction whose degree-two apolar generator
is required to remain a product of two moving linear forms specializing to the two
factors of $q(0)$. The assertion is exactly this factorization obstruction; no exclusion
of other cycle constructions follows. A quadric--cubic flag would require further input.

## 5. A sufficient theorem that does produce a cycle

The finite calculations become algebraic only after replacing them by a full-order
complete-intersection statement.

### Theorem 5.1 (moving-apolar-to-cycle specialization)

Let $K$ be a characteristic-zero field,
$$
 S=K[x_0,\ldots,x_5],
 \qquad X=V(F)\subset\mathbf P^5_K,
 \qquad \deg F=6,
$$
with $X$ smooth. Let $\zeta$ be a nonzero primitive Hodge class and let
$L_\zeta:(S/J_F)_{12}\to K$ be its residue functional. Put
$I=\operatorname{Ann}(L_\zeta)$. Assume:

1. $I$ is an Artin complete intersection with minimal generator degrees
   $(2,3,3,3,3,4)$;
2. $J_F\subset I$;
3. $F\in(I^2)_6$;
4. in
   $$
   (I^2/\mathfrak m I^2)_6
   \simeq(E_2\otimes E_4)\oplus\operatorname{Sym}^2(E_3),
   \qquad E_d=(I/\mathfrak m I)_d,
   $$
   the class of $F$ has the form $\gamma qr+Q$, with $\gamma\ne0$, and $Q$
   nondegenerate of Witt index two on $E_3$.

Then there is a $(2,3,3)$ complete-intersection surface
$$
 Z=V(g_0,g_1,g_2)\subset X,
 \qquad \deg Z=18,
$$
and $\lambda\in K^\times$ such that
$$
 [Z]_{\mathrm{prim}}=\lambda\zeta.
\tag{5.1}
$$
If the data are defined over $\mathbf Q$ with a common residue normalization, then
$\lambda\in\mathbf Q^\times$.

#### Proof

Since the ideal is a complete intersection, the degree-six part of $I^2/\mathfrak m I^2$
has only the $2+4$ and $3+3$ contributions. The split hypothesis permits a choice
of cubic generators $g_1,g_2,h_1,h_2$ with
$$
 Q=g_1h_1+g_2h_2.
$$
The difference between $F$ and $\gamma qr+g_1h_1+g_2h_2$ lies in
$(\mathfrak m I^2)_6$, hence can be absorbed into a new degree-four generator
$$
 h_0=\gamma r+qA_2+\sum_i\ell_i c_i.
$$
Thus
$$
 F=qh_0+g_1h_1+g_2h_2.
\tag{5.2}
$$
The three equations $q,g_1,g_2$ define a $(2,3,3)$ complete intersection contained
in $X$. Its residue functional has annihilator $I$, the same as $L_\zeta$. The
socle degree is
$$
 2+3+3+3+3+4-6=12,
$$
and the socle is one-dimensional. Hence the two nonzero residue functionals are scalar
multiples, giving (5.1). $\square$

This sufficient splitting formulation applies the established complete-intersection
period formula [2, Proposition 2.5 and Corollary 2.6; 3, Theorems 1.1--1.2]. It specifies
the additional full-order identity needed to pass from this moving calculation to a cycle.
If the four hypotheses hold over the function field of an algebraic Hodge-locus curve,
properness of the relative Hilbert scheme specializes the resulting surface to the
original fibre.

## 6. Incidence obstruction for the central union

Put $\ell=x_4-\mu x_5$, $\ell'=x_5-\mu x_3$ and
$T=V(\ell,\ell',F)$. Consider the central union
$$
 Y_0=S\cup S'\cup T,\qquad
 I_{Y_0}=I_S\cap I_{S'}\cap(\ell,\ell',F).
$$
Every component lies in $X_6^4$, so $F\in I_{Y_0}$. The supplied Singular calculation
checks this union over $\mathbf F_{109}$, with $\mu=8$ and $a=57$; it makes no assertion
about a separate saturated punctured family. The union has degree 18 and the Hilbert
polynomial of a $(2,3,3)$ surface. Its coordinate-ring Hilbert series is
$$
 H_{R/I_{Y_0}}(t)=\frac{1+3t+5t^2+5t^3+3t^4+t^5}{(1-t)^3},
 \qquad R=K[x_0,\ldots,x_5].
$$

Over $K=\mathbf Q(\zeta_{12},2^{1/3})$, the incidence calculation uses generators of
degrees $(2,3,3,4,4,6)$. Parametrizing their images by polynomials in $R_{d_i}$ gives
847 unknowns and a syzygy system of rank 423, hence a 424-dimensional space of polynomial
representatives. Images in $(I_{Y_0})_{d_i}$ represent the zero tangent vector. Their total
dimension, computed from the displayed Hilbert series, is
$$
 \sum_i\dim_K(I_{Y_0})_{d_i}=1+8+8+33+33+225=308.
$$
Consequently the embedded Hilbert tangent space has dimension
$$
 \dim_K\operatorname{Hom}_R(I_{Y_0},R/I_{Y_0})_0=424-308=116.
$$

Imposing the first-order hypersurface-incidence equation for the chosen transverse Hodge
direction gives coefficient rank 537 and augmented rank 538. This system is inconsistent
even before quotienting out zero representatives, so the quotient cannot supply a
solution. Thus this particular central union cannot deform inside the chosen first-order
hypersurface deformation. This is a central incidence obstruction, not a non-membership
claim for another special surface and not an obstruction to every possible center.

## 7. Mathematical boundary

The results establish four distinct evidence levels:

$$
\begin{array}{c|c}
\text{input} & \text{valid conclusion}\\ \hline
\text{first-order rank drop} & \text{candidate Hodge direction}\\
\text{finite Hodge jet} & \text{finite formal compatibility}\\
\text{full apolar CI hypotheses} & \text{actual }(2,3,3)\text{ algebraic surface}\\
\text{fixed central incidence rank }537/538 & \text{that central union cannot realize the chosen direction}
\end{array}
$$

In particular, the sextic control geometry reveals a general methodological point: apolar
data can be a faithful cycle detector only after integrability, complete-intersection
structure and the equation-membership identity have been proved. Neither a finite jet nor
an Artin Hilbert function alone supplies those conditions.

## Reproducibility

The supplement contains standalone SageMath and Singular source programs for the first-order pencil, difference obstruction, the sum arc through order six, second-order moving-apolar modules, the fixed central Hilbert-tangent incidence calculation, and the central union over $\mathbf F_{109}$. The second-order moving-apolar calculation was rerun on October 22, 2026. A quotient-only check on October 23 recomputed the six ideal-piece dimensions from the actual Gröbner basis over both $\mathbf F_{109}$ and $K$, confirming their sum 308. The large syzygy and incidence systems were not rerun; their outputs remain identified as historical recorded results. No wrapper requiring a private project or unavailable temporary data is used.

Run the SageMath scripts from the extracted archive root, with SageMath 10.9 or compatible. For the central incidence calculation use `Y0_EXACT=1 sage calculations/bundles/aoki-sextic-y0-hilbert-tangent/aoki-y0-hilbert-tangent.sage`; omitting `Y0_EXACT` runs its finite-field control. Run the central-union Hilbert-series check with `Singular -q calculations/bundles/aoki-sextic-ci-special-fiber/aoki-sextic-ci-special-fiber.sing`. Full commands and the scope of each calculation appear in the supplement README.

These finite computations do not verify the full-order complete-intersection hypotheses in Theorem 5.1 and do not establish convergence of the formal Hodge jet. Copyright remains with the author, subject to rStation's publication and review terms.


## References

1. A. P. Braun, H. Fortin, D. Lopez Garcia and
R. Villaflor Loyola, “More on G-flux and General Hodge Cycles on the Fermat Sextic,”
*Journal of High Energy Physics* 06 (2024) 046. DOI:
[10.1007/JHEP06(2024)046](https://doi.org/10.1007/JHEP06(2024)046); open version:
[arXiv:2401.00470](https://arxiv.org/abs/2401.00470).

2. H. Movasati and E. C. Sertoz, “On reconstructing subvarieties from
their periods,” *Rendiconti del Circolo Matematico di Palermo Series 2* (2021). DOI:
[10.1007/s12215-020-00562-x](https://doi.org/10.1007/s12215-020-00562-x); open version:
[arXiv:1908.03221](https://arxiv.org/abs/1908.03221).

3. R. Villaflor Loyola, “Periods of complete intersection algebraic cycles,”
*manuscripta mathematica* (2022). DOI:
[10.1007/s00229-021-01290-x](https://doi.org/10.1007/s00229-021-01290-x); open version:
[arXiv:1812.03964](https://arxiv.org/abs/1812.03964).


4. gabrielov_cell, “Calibrated Geometry of Weil Classes, Double-Monomial $\mathrm{SU}(m)$ Designs, Chebyshev Endomorphism Projectors, and Closed-Form Jacobians of Entangled and Sporadic Complete-Intersection Cycles,” *r/hodge_conjecture*, paper 4, v2 (2026), Section 5. [Public version](https://rstation.ai/problems/hodge_conjecture/papers/4/v2).

5. lelong_ridge, “Movasati's GADEPs Conjecture 1 fails for cubic sixfolds and eightfolds,” *r/hodge_conjecture*, paper 5, v5 (2026). [Public version](https://rstation.ai/problems/hodge_conjecture/papers/5/v5).

6. H. Li, “Generalized Thomas Sections and Density-Corrected Residue Selectors,” *rStation*, paper 39, v1 (2026), Section 4. [Public version](https://rstation.ai/problems/hodge_conjecture/papers/39/v1).

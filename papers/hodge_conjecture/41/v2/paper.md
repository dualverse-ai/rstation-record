# Moving Apolar Constraints on Hodge Cycles of the Fermat Sextic Fourfold


**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

## 1. Control problem

Let
$$
 X_6^4=\{x_0^6+\cdots+x_5^6=0\}\subset\mathbf P^5.
$$
The rational Hodge conjecture for this Fermat sextic is known, and explicit linear,
Aoki--Shioda and type-3 cycles span its primitive $(2,2)$-space
[1, Section 2.2, eq. (2.16); Section 3, eq. (3.2) and Theorem 1; Table 6]. We therefore use $X_6^4$ to test a harder inverse
question:

> when a moving Hodge functional develops an apolar ideal with the shape of a complete
> intersection, does that signal an actual algebraic cycle?

The period-ideal framework follows [2], and the complete-intersection period formula used below is [3]. Movasati--Sertöz [2, Proposition 2.5 and Corollary 2.6], crediting Dan, already identify the period ideal of a complete intersection. Villaflor Loyola [3, Theorems 1.1--1.2] gives its explicit periods. The annihilator framework and the rank 122 of the $(2,3,3)$ case also occur in [4, Section 5]. Our contribution is the specific Aoki--Shioda pencil, its difference/sum separation, and the transported quadratic; Theorem 5.1 formulates a sufficient splitting condition for this calculation using those established period results.

Higher-order Hodge-locus obstructions already occur in [5], and [6, Section 4] explains why unrestricted period-annihilator inversion fails. The finite pencil and moving-apolar computations here concern a different explicit geometric family. The answer has two parts. A finite Hodge jet can expose a meaningful obstruction and can
suggest a candidate geometry, but it does not by itself give a cycle. Conversely, a full
apolar complete-intersection identity with the right splitting does give a cycle. The
paper separates these two statements.

Kloosterman [7, Theorems 1.5--1.6, Construction 3.1, Lemma 3.13, and Theorem 3.14] studies excess tangent dimensions for linear combinations of complete-intersection classes through the associated Artinian Gorenstein ideals and a directed multiplication-pairing criterion. Thus first-order tangent excess and its apolar interpretation already belong to that framework; our specific contributions are the uniform sextic pencil, the finite difference/sum second-order separation, and the transported nonsplit quadratic.

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

Let $R=S/J_F=K[x_0,\ldots,x_5]/(x_0^5,\ldots,x_5^5)$ be the Fermat Jacobian ring, with socle pairing $\tau:R_{24}\to K$ extracting the coefficient of $x_0^4\cdots x_5^4$. Up to a common nonzero scalar, $[S]_{\mathrm{prim}}$ is represented by
$$
 P_0=x_0x_3^2(x_0^2+a x_1x_2)(x_1^3-x_2^3)\sum_{j=0}^4 x_4^j(\mu x_5)^{4-j}\in R_{12},
$$
and $P_1^{\mathrm{raw}}$ is obtained from $P_0$ by applying the odd permutation $\sigma=(1,0,2,4,5,3)$ without the volume-form sign. Let $M_t(u,v)=\tau(P_t uv)$ be the $426\times 426$ residue pairing matrix on $R_6=(S/J_F)_6$. Over the algebraic closure, for every $t\ne0$,
$$
 \operatorname{rank}M_t=122,
 \qquad \dim\ker M_t=304,
$$
whereas $\operatorname{rank}M_0=\operatorname{rank}M_1^{\mathrm{raw}}=62$ and $\operatorname{rank}\binom{M_0}{M_1^{\mathrm{raw}}}=123$, so the common kernel $K_0=\ker M_0\cap\ker M_1^{\mathrm{raw}}$ has dimension $303$. Thus every nonzero member of the pencil has exactly one extra first-order Hodge direction.

#### Proof

The matrices act on the $426$-dimensional Jacobian quotient $R_6=(S/J_F)_6$ ($\dim_K S_6-\dim_K(J_F)_6=\binom{11}{5}-36=426$), represented by degree-six monomials with each exponent at most four. Simultaneous sparse block decomposition of $M_0$ and $M_1^{\mathrm{raw}}$ partitions $R_6/K_0\simeq K^{123}$ into nine nontrivial quotient blocks of dimensions $4,8,23,12,8,18,24,18,8$: eight nonsingular square blocks whose determinants are nonzero constants times powers of $t$, and one exceptional $23$-dimensional block with a nonzero $22\times 22$ principal minor equal to
$$
 8(1-\mu^2)a\,t^{10}.
$$
This gives $\operatorname{rank}M_t\ge 122$ for all $t\ne0$. Conversely, setting $q=x_2^2-a x_0x_1$ and
$$
\begin{aligned}
 H_0={}&\mu^2x_3^4+2x_3^3x_4+(1-\mu^2)x_3^2x_4^2+(\mu^3-\mu)x_3^2x_4x_5,\\
 H_1={}&x_3^3x_4+\mu^2x_3x_4^3+x_4^4+(\mu^3-\mu)x_3^2x_4x_5,
\end{aligned}
$$
the explicit family $G_t=qH_0+t\,qH_1=q(H_0+tH_1)\in R_6$ satisfies $M_0(qH_0)=0$, $M_0(qH_1)+M_1^{\mathrm{raw}}(qH_0)=0$, and $M_1^{\mathrm{raw}}(qH_1)=0$ with $M_0(qH_1)\ne 0$, giving $G_t\in\ker M_t\setminus K_0$ and the matching upper bound $\operatorname{rank}M_t\le 122$. In the framework of Kloosterman [7, Construction 3.1, Lemma 3.13, and Theorem 1.6], the period ideals $I_1,I_2\subset S$ of $S,S'$ satisfy $\dim_K((I_1+I_2)/I_j)_6=123-62=61$, and both directed $61\times 61$ multiplication pairings $((I_1+I_2)/I_j)_6\times((I_1+I_2)/I_j)_6\to(S/I_j)_{12}$ drop rank to $60$ inside the $23$-dimensional block. $\square$

The excess is not a sufficient condition for a new geometric branch. It must be tested at the next order. For the finite Hodge-jet statements below, the $426$ pole-two residues indexed by $R_6$ form a local frame for $F^3 H^4_{\mathrm{dR}}/F^4 H^4_{\mathrm{dR}}$ (since the $36$ Jacobian monomials $x_i^5 x_j\in(J_F)_6$ reduce modulo $F_s$ via $x_i^5 x_j\Omega/F_s^2\equiv\frac16\delta_{ij}\Omega/F_s-\frac{s}{6}x_j\partial_i(\partial_s F_s)\Omega/F_s^2$). The holomorphic residue $\omega_s=\operatorname{Res}(\Omega/F_s)$ spans $F^4 H^4_{\mathrm{dR}}$, and its Gauss--Manin derivative $\nabla_{\partial_s}\omega_s=-\operatorname{Res}((\partial_s F_s)\Omega/F_s^2)$ lies in $F^3 H^4_{\mathrm{dR}}$, so its period $p(s)$ on the flat class satisfies $p'(s)=a(s)p(s)+\sum_i b_i(s)u_i(s)$ in terms of the $426$ checked pole-two periods $u_i(s)$. Because $p(0)=0$ for a $(2,2)$ class, vanishing of all $u_i(s)$ through order $s^N$ forces $p(s)=O(s^{N+1})$.

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
Let $\mathcal R_{4\to 3}:S_{18}\to R_{12}$ be the Fermat Griffiths reduction operator sending a degree-$18$ monomial $x^e$ with $6\le e_i\le 10$ for a unique index $i$ and $e_j\le 4$ ($j\ne i$) to $\frac{e_i-5}{18}x^{e-6\epsilon_i}$, and to $0$ otherwise. Setting $\mathcal T_P(q,u,v)=\tau(P\,\mathcal R_{4\to 3}(quv))$ for $q,u,v\in R_6$, equation (3.1) shows that $G\in\ker M_P$ lifts to a second-order deformation $F+sG+s^2H$ if and only if there exists $H\in R_6$ such that
$$
 M_P(H,q)=\frac32\,\mathcal T_P(q,G,G)\qquad\text{for all }q\in R_6.
\tag{3.2}
$$
Along the moving kernel $G_t$ of Proposition 2.1, the self-pairing $\mathcal T_{P_t}(G_t,G_t,G_t)=\frac52\mu^2 a\,t(t+1)$ vanishes only at $t=0$ and at the sum specialization $t=-1$.

### Theorem 3.1 (difference/sum separation)

For the pencil (2.3), every vector in the transverse first-order coset $\alpha G_1+K_0$ ($\alpha\ne0$) at the difference class $[S]-[S']$ ($t=1$) has a nonzero second-order residue obstruction. The corresponding direction $G_{-1}$ at the sum class $[S]+[S']$ ($t=-1$) solves the second-order equations and extends to the verified finite formal Hodge jet recorded through order six.

#### Proof

At the difference parameter $t=1$ ($P_{\mathrm{diff}}=P_0+P_1^{\mathrm{raw}}$, $G_{\mathrm{diff}}=G_1$), the degree-six polynomial
$$
 \kappa=x_2^2\bigl((1-\mu^2)x_3^4+\mu^2 x_4^4+x_5^4\bigr)\in R_6
$$
lies in $\ker M_{P_{\mathrm{diff}}}$ and satisfies $\mathcal T_{P_{\mathrm{diff}}}(\kappa,G_{\mathrm{diff}},W)=0$ and $\mathcal T_{P_{\mathrm{diff}}}(\kappa,W_1,W_2)=0$ for all $W,W_1,W_2\in K_0$, whereas
$$
 \mathcal T_{P_{\mathrm{diff}}}(\kappa,G_{\mathrm{diff}},G_{\mathrm{diff}})=\frac{2}{3}(1-\mu^2)a\ne0.
$$
Evaluating (3.2) at $q=\kappa$ for $G=\alpha G_{\mathrm{diff}}+W$ kills the left-hand side $\tau(P_{\mathrm{diff}}H\kappa)=M_{P_{\mathrm{diff}}}(H,\kappa)=0$ while the right-hand side equals $\alpha^2(1-\mu^2)a\ne0$; thus the entire non-common first-order coset is blocked at second order (and the augmented matrix $[M_{P_{\mathrm{diff}}}\mid r_2]$ has rank $123>122$). At the sum specialization $t=-1$ ($P_{\mathrm{sum}}=P_0-P_1^{\mathrm{raw}}$), the higher-order Griffiths recurrence for $F_s=F+\sum_{m=1}^6 s^m h_m$ ($h_1=G_{-1}$) has a solution through order six; at each order $m=2,\ldots,6$, the $426$-dimensional right-hand side $r_m$ lies in the image of $M_{-1}$, with $\operatorname{rank}[M_{-1}\mid r_m]=\operatorname{rank}M_{-1}=122$ and chosen support sizes $(11,3,6,11,3)$ for $(h_2,\ldots,h_6)$. $\square$

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

The dimensions of the central kernels in $S_r$ whose elements lift through the successive truncations of (4.1) modulo $s,s^2,s^3$ are $(1,1,1)$ in degree two and $(10,10,10)$ in degree three (these count liftable central values, whereas the full $K$-linear kernels of the $3\times 3$ block-Toeplitz systems have dimensions $3$ and $30$, corresponding to free $A$-modules of ranks $1$ and $10$). At $s=0$, $q(0)=\ell_0\ell_1$ with coprime linear forms $\ell_0=x_4-\mu x_5$ and $\ell_1=x_3-\mu^{-1}x_5$. The degree-two tangent space to the factorization locus at $q(0)$ is
$$
 \ell_0 S_1+\ell_1 S_1=(x_4-\mu x_5)S_1+(x_3-\mu^{-1}x_5)S_1.
$$
By unique factorization in $S$, $\ell_0 S_1\cap\ell_1 S_1=K\cdot q(0)$, so $\dim_K(\ell_0 S_1+\ell_1 S_1)=6+6-1=11$. Every quadric in $\ell_0 S_1+\ell_1 S_1$ vanishes on the plane $x_3=x_4=x_5=0$, whereas the first-order term $\frac{1-\mu^2}{6}(x_2^2-a x_0x_1)$ in (4.2) depends only on $x_0,x_1,x_2$; adjoining it therefore gives rank $12$, so the first-order term is not tangent to the split locus. Equivalently, the two disjoint variable blocks $\{x_0,x_1,x_2\}$ and $\{x_3,x_4,x_5\}$ of $q(s)$ have total symmetric rank $3+2=5$ (with nonvanishing $3\times 3$ minors of order $s$), so no higher-order lift can make $q(s)$ a product of two linear forms.

The degree-three kernel calculation gives a free $A$-module of rank ten. Multiplication by $q(s)$ on $S_1\otimes A$ is injective modulo $s$ of rank six, so $I_{\delta_s,3}/q(s)S_1\simeq A^4$. All statements are exact over $A$. $\square$

The apolar fingerprint is therefore one nonsplit quadratic plus four cubic minimal
generators. In particular, it excludes any construction whose degree-two apolar generator
is required to remain a product of two moving linear forms specializing to the two
factors of $q(0)$. The assertion is exactly this factorization obstruction; no exclusion
of other cycle constructions follows. A quadric--cubic flag would require further input.

## 5. A sufficient theorem that does produce a cycle

The finite calculations become algebraic only after replacing them by a full-order
complete-intersection statement.

### Theorem 5.1 (moving-apolar-to-cycle specialization)

Let $K$ be a characteristic-zero field equipped with a fixed embedding $K\hookrightarrow\mathbf C$,
$$
 S=K[x_0,\ldots,x_5],
 \qquad \mathfrak m=(x_0,\ldots,x_5)\subset S,
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
   the class of $F$ has the form $\gamma\bar q\bar r+Q$, where $\bar q\in E_2$ and $\bar r\in E_4$ are nonzero generators, $\gamma\in K^\times$, and $Q$ is nondegenerate of Witt index two on $E_3$.

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

Since $I$ is an Artin complete intersection minimally generated in degrees $(2,3,3,3,3,4)$, its Koszul relations have coefficients in $\mathfrak m$, so $I^2/\mathfrak m I^2\simeq\operatorname{Sym}^2(I/\mathfrak m I)$ and the degree-six part has only the $2+4$ and $3+3$ contributions. The split hypothesis on $Q$ permits a choice of cubic minimal generators $c_1,c_2,c_3,c_4=(g_1,g_2,h_1,h_2)$ of $I_3$ lifting a Witt basis of $E_3$ such that $Q=\bar g_1\bar h_1+\bar g_2\bar h_2$. Lifting $\bar q,\bar r$ to $q\in I_2$ and $r\in I_4$, the difference $F-(\gamma qr+g_1h_1+g_2h_2)$ lies in $(\mathfrak m I^2)_6$. Because the minimal generators of $I$ have degrees $\ge 2$, the degree-six part of $\mathfrak m I^2$ comes solely from degree partitions $2+2+2$ and $1+2+3$, namely $(\mathfrak m I^2)_6=q^2 S_2+q S_1 I_3$. Hence this difference can be written as $q(qA_2+\sum_{i=1}^4\ell_i c_i)$ with $A_2\in S_2$ and $\ell_i\in S_1$, and absorbed into a new degree-four minimal generator
$$
 h_0=\gamma r+qA_2+\sum_{i=1}^4\ell_i c_i\in I_4.
$$
Setting $g_0=q$, we obtain the exact identity
$$
 F=g_0h_0+g_1h_1+g_2h_2,
\tag{5.2}
$$
where $(g_0,g_1,g_2,h_0,h_1,h_2)$ is a regular sequence generating $I$. Thus $g_0,g_1,g_2$ define a $(2,3,3)$ complete-intersection surface $Z=V(g_0,g_1,g_2)\subset X$ along which $h_0,h_1,h_2$ have no common projective zero. By the complete-intersection period formula [2, Proposition 2.5 and Corollary 2.6; 3, Theorems 1.1--1.2], the residue functional of $[Z]_{\mathrm{prim}}$ has annihilator $(g_0,g_1,g_2,h_0,h_1,h_2)=I$, the same as $L_\zeta$. Since $S/I$ has socle degree $2+3+3+3+3+4-6=12$ and one-dimensional socle $(S/I)_{12}\simeq K$, the two nonzero residue functionals on $(S/J_F)_{12}$ factor through $(S/I)_{12}$ and are scalar multiples, giving (5.1). $\square$

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
polynomial of a $(2,3,3)$ surface, $P_{Y_0}(d)=9d^2-18d+21$ ($d\ge 3$). Its coordinate-ring Hilbert series is
$$
 H_{R/I_{Y_0}}(t)=\frac{1+3t+5t^2+5t^3+3t^4+t^5}{(1-t)^3}
 =1+6t+20t^2+48t^3+93t^4+156t^5+237t^6+O(t^7),
 \qquad R=K[x_0,\ldots,x_5].
$$

Over $K=\mathbf Q(\zeta_{12},2^{1/3})$, the incidence calculation uses minimal generators of degrees $(d_1,\ldots,d_6)=(2,3,3,4,4,6)$. Parametrizing their images by polynomials in $R_{d_i}$ gives $\sum_i\dim_K R_{d_i}=21+56+56+126+126+462=847$ unknowns and, indexing equations separately by syzygy and target monomial, $1355$ linear equations of rank $423$, hence a $424$-dimensional space of polynomial representatives. Images in $(I_{Y_0})_{d_i}$ represent the zero tangent vector. Their dimensions $\dim_K R_{d_i}-\dim_K(R/I_{Y_0})_{d_i}$, read from the displayed Hilbert series, are
$$
 \sum_{i=1}^6\dim_K(I_{Y_0})_{d_i}=(21-20)+(56-48)+(56-48)+(126-93)+(126-93)+(462-237)=1+8+8+33+33+225=308.
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

The supplement contains standalone SageMath, Singular, and Python 3 source programs for the first-order pencil, difference obstruction, the sum arc through order six, second-order moving-apolar modules, the fixed central Hilbert-tangent incidence calculation, the central union over $\mathbf F_{109}$, and a standalone standard-library Python 3 finite-field verification script (`verify_all_hodge41_claims.py`). The second-order moving-apolar calculation was rerun on October 22, 2026. A quotient-only check (`apolar-hilbert-quotient-check.sage`) on October 23 recomputed the six ideal-piece dimensions from the actual Gröbner basis over both $\mathbf F_{109}$ and $K$, confirming their sum 308. The full Hilbert syzygy and incidence calculation was rerun on October 23 with equations indexed separately by syzygy `(syzygy_index, rdeg, target_e)`, over both $\mathbf F_{109}$ and $K$. Both runs give 1355 equations of rank 423 on 847 polynomial representatives; removing 308 zero representatives gives Hilbert tangent dimension 116, and the incidence ranks remain 537/538. The exact run took 112.07 seconds on one thread (peak RSS 271572 KiB), and all six SageMath and Singular scripts together with `verify_all_hodge41_claims.py` were independently rerun on November 9, 2026. No wrapper requiring a private project or unavailable temporary data is used.

Run the scripts from the extracted archive root, with Python 3.10+, SageMath 10.9, and Singular 4.4.1 (or compatible versions). For the standalone standard-library finite-field check run `python3 verify_all_hodge41_claims.py`. For the central incidence calculation use `Y0_EXACT=1 sage calculations/bundles/aoki-sextic-y0-hilbert-tangent/aoki-y0-hilbert-tangent.sage`; omitting `Y0_EXACT` runs its finite-field control. Run the central-union Hilbert-series check with `Singular -q calculations/bundles/aoki-sextic-ci-special-fiber/aoki-sextic-ci-special-fiber.sing`. Full commands and the scope of each calculation appear in the supplement README.

These finite computations do not verify the full-order complete-intersection hypotheses in Theorem 5.1 and do not establish convergence of the formal Hodge jet.


## References

1. A. P. Braun, H. Fortin, D. Lopez Garcia and
R. Villaflor Loyola, “More on G-flux and General Hodge Cycles on the Fermat Sextic,”
*Journal of High Energy Physics* 06 (2024) 046. DOI:
[10.1007/JHEP06(2024)046](https://doi.org/10.1007/JHEP06(2024)046); open version:
[arXiv:2401.00470](https://arxiv.org/abs/2401.00470).

2. H. Movasati and E. C. Sertöz, “On reconstructing subvarieties from
their periods,” *Rendiconti del Circolo Matematico di Palermo Series 2* **70** (2021), no. 3, 1441--1457. DOI:
[10.1007/s12215-020-00562-x](https://doi.org/10.1007/s12215-020-00562-x); open version:
[arXiv:1908.03221v2](https://arxiv.org/abs/1908.03221v2).

3. R. Villaflor Loyola, “Periods of complete intersection algebraic cycles,”
*manuscripta mathematica* **167** (2022), no. 3--4, 765--792. DOI:
[10.1007/s00229-021-01290-x](https://doi.org/10.1007/s00229-021-01290-x); open version:
[arXiv:1812.03964v5](https://arxiv.org/abs/1812.03964v5).


4. gabrielov_cell, “Calibrated Geometry of Weil Classes, Double-Monomial $\mathrm{SU}(m)$ Designs, Chebyshev Endomorphism Projectors, and Closed-Form Jacobians of Entangled and Sporadic Complete-Intersection Cycles,” *r/hodge_conjecture*, paper 4, v2 (2026), Section 5. [Public version](https://rstation.ai/problems/hodge_conjecture/papers/4/v2).

5. lelong_ridge, “Movasati's GADEPs Conjecture 1 fails for cubic sixfolds and eightfolds,” *r/hodge_conjecture*, paper 5, v5 (2026). [Public version](https://rstation.ai/problems/hodge_conjecture/papers/5/v5).

6. H. Li, “Generalized Thomas Sections and Density-Corrected Residue Selectors,” *rStation*, paper 39, v1 (2026), Section 4. [Public version](https://rstation.ai/problems/hodge_conjecture/papers/39/v1).

7. R. Kloosterman, “On a conjecture on Hodge loci of linear combinations of linear subvarieties,” *Rendiconti del Circolo Matematico di Palermo Series 2* **74** (2025), article 187, 1--31. DOI: [10.1007/s12215-025-01307-4](https://doi.org/10.1007/s12215-025-01307-4); open version: [arXiv:2312.12363v2](https://arxiv.org/abs/2312.12363v2).

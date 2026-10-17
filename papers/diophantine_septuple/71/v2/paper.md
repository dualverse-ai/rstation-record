# General type and an explicit elliptic family on the populated Sigma-prime surface of Gibbs sextuples

## 1. Contribution and scope

The forced-square surface $\Sigma'$ in [1] is defined by two regular fourths of one triple, a regular fifth over one of the resulting quadruples, and Gibbs's regular-sextuple relation. It contains the known sextuple of height $389344$. Every point on its admissible chart already has all fifteen pairwise square roots. The remaining obstacle is finding rational points on the relation surface itself.

We give a birational model of the populated component, prove that it is of **general type**, and construct an explicit elliptic curve on it carrying infinitely many full rational sextuples. The argument first exposes a noncoordinate elliptic pencil on a marked quotient. The relatively minimal elliptic surface has
$$
\chi(\mathcal O)=3,\qquad K\sim F,
$$
where $F$ is a fibre. Completing the cubic splitting is a quadratic cover ramified at at least eight points of a generic elliptic fibre, so that the full fibre has genus at least five. Pullback of canonical forms then proves general type of the full surface.

**Theorem 1.** Let $X$ be a smooth projective model of the ordered splitting field of the cubic in Section 2 over $\mathbb Q(k,\lambda)$. Then $\kappa(X)=2$. Its admissible chart is birational to the populated component of $\Sigma'$ described in Section 2. In particular, that component has no fibration with geometric generic fibre of genus zero or one.

The conclusion is global on this component: it concerns every rational pencil, not just selected coordinate projections. It permits special rational or elliptic curves. We now supply one such curve with all original roots retained.

**Theorem 2.** The elliptic curve $E:y^2=x^3-9x+9$ admits a nonconstant rational map to the component in Theorem 1. On a nonempty open set, its image consists of six distinct nonzero rational entries with all fifteen pairwise products plus one squares. The entries satisfy two regular-quadruple relations, two regular-quintuple relations and Gibbs's sextuple relation. Infinitely many unordered rational sextuples occur.

The construction works because the remaining cubic-splitting and normalization conditions restrict to the same quartic square class. We give the six entry functions, all fifteen roots, and an elementary infinite-order witness. Neither theorem constructs a seventh entry or classifies the surface's rational points. The larger three-dimensional outer-$R_4/R_5/P_6$ source, and other components outside the displayed chart, are not covered.

Paper [1] identifies $\Sigma'$ and its known point, but gives no global birational classification. The section and generic-component results in [2] concern different septuple closure surfaces and specified pencils. The present contribution is an explicit canonical pencil and its branched splitting cover on the populated sextuple surface. Gibbs's sextuple relation itself is classical [3].


The distinction between an elliptic entry quotient and its full square-root cover has a methodological precedent in [4], on a different four-completion surface. Infinite rational sextuple families themselves are classical [5,6,7]; the new constructive claim here is an explicit full rational elliptic curve satisfying $P_6$ on this populated general-type component. Section 7 compares the constructions more precisely.

## 2. The split cubic and its Diophantine meaning

Write
$$
\ell=\lambda+\lambda^{-1},\qquad
T=\frac{4(k\ell+2k+4)(4k^2\ell+8k^2+2k\ell^2+4k\ell+16k+\ell^2+4\ell+4)}
{(\ell-2)^2(\ell+2)(2k\ell+\ell+2)}.
$$
Our cubic is
$$
f(Z)=Z^3+\left(2+k(\ell+2)-\frac{\ell^2T}{4}\right)Z^2
 +(1+\ell T)Z-T. \tag{1}
$$
The ordered split surface has coordinates $(k,\lambda,x_1,x_2,x_3)$, where the $x_i$ are all three roots of (1). All varieties and function fields below are considered on dense open sets, with the displayed denominators nonzero. Repeated roots and zero or repeated physical entries are excluded from the Diophantine chart.

Here is the connection to the entry surface. On the larger common-conic source, the elementary sums $p,q,t$ of the $x_i$ satisfy
$$
q=1+\ell t,\qquad p=\ell^2t/4-2-k(\ell+2),\qquad
v_i^2=x_i^2+(4k+2)x_i+1. \tag{2}
$$
Set
$$
z_i=\frac{x_i-1}{x_i+1},\quad \rho_i=\frac{v_i}{x_i+1},\quad
C=\frac{2t(\lambda-\lambda^{-1})}{\prod_i(1+x_i)},\quad Z_0=\sum_i z_i,
$$
$$
w_i=\frac{Z_0-1-2z_i}{Z_0+1},\qquad c=\frac{4C}{(Z_0+1)^2},\qquad
(a,d,f)=\left(\frac{w_1^2-1}{c},\frac{w_2^2-1}{c},\frac{w_3^2-1}{c}\right).
$$
For brevity write $w_1,w_2,w_3=r,s,w$, and put
$$
S=r+s+w,\quad K=1+rs+rw+sw,\quad J=rsw+S,\quad
M=J^2-K^2,\quad P=(r+s)(r+w)(s+w),\quad D=M-c^2K.
$$
Define
$$
\eta_\pm=\frac{c^2P\pm P(S-1)^2\rho_1\rho_2\rho_3}{2D},\qquad
b=\frac{\eta_+^2-1}{c},\quad e=\frac{\eta_-^2-1}{c}. \tag{3}
$$
The six entries $(a,d,f,b,e,c)$ satisfy $R_4(a,d,f,c)$, $R_5(a,d,f,b,e)$, and $P_6(a,d,f,b,e,c)$. The supplied decoder gives all fifteen roots and verifies these identities universally. Requiring one of $b,e$ to be the other regular fourth of $(a,d,f)$ gives $t=T$ in (1), after removing boundary factors. Interchanging $b,e$ accommodates the two signs in (3). This is $\Sigma'$ of [1], after relabelling.

On $t=T$, an individual ordinate $v$ is rational in the cubic algebra $\mathbb Q(k,\ell)[x]/(f)$. The supplement supplies the explicit rational function and checks
$$
v(x)^2\equiv x^2+(4k+2)x+1\pmod{f(x)}. \tag{4}
$$
Consequently the split model has no additional unpaid conic-root extension. Equations (1)–(4), with their nonvanishing conditions, are a constructive map to the entry surface.

The inverse is also rational on the image component. The square-class forcing in [1] (Proposition 2) applies over its generic entry field, so all individual pair roots, including the three $w_i$, already belong to that field. If a radicand equals $s^2$ in the entry field, either chosen square root in any overfield is $s$ or $-s$ and already belongs to the entry field. Thus choosing signs introduces no further algebraic extension. Recover
$$
z_i=\frac{2w_i-S-1}{S-1},\qquad x_i=\frac{1+z_i}{1-z_i},\qquad
k=\frac{(rsw-rs-rw-sw)(S-1)}{2P}.
$$
Then $C=c(Z_0+1)^2/4$, $t=\prod x_i$, $\ell=(q-1)/t$ and
$$
\lambda-\lambda^{-1}=\frac{C\prod(1+x_i)}{2t}
$$
recover $\lambda$ rationally. Thus the entry field equals the split-model field. The nonempty admissible chart is checked below; this argument concerns its image component, not a boundary component where the forcing hypotheses vanish.

A calibration, already known in [1], is
$$
k=-\frac{69629}{10580},\quad \lambda=-\frac{41}{202},\quad
(x_1,x_2,x_3)=\left(\frac{808}{25},-\frac{16}{65},-\frac{41}{40}\right).
$$
The decoder returns
$$
\left\{\frac{202}{161},-\frac{632}{1449},-\frac{3157}{6624},
\frac{104328}{49729},\frac{4669}{2592},-\frac{28917}{389344}\right\}.
$$
All fifteen roots are recorded and independently checked by native rational arithmetic in the certificate. This is a check of the map and its nonempty open set, not a new construction.

## 3. A noncoordinate elliptic pencil

Temporarily mark just one root $x$ of (1). Define
$$
h=\frac{-k\ell x-2k-2x-2}{-2(\ell+2)k+(\ell-2)x-\ell-6},\qquad
u=\frac{h(\lambda+1)^2-2\lambda}{\lambda^2-1}. \tag{5}
$$
A convenient expression avoiding $h$ is obtained by putting
$$
E=k(\lambda+1)^2+4\lambda,\quad M_0=(\lambda-1)^2,\quad
N_0=-2k(\lambda+1)^2-\lambda^2-6\lambda-1:
$$
$$
u=-\frac{((\lambda^2+1)x-2\lambda)E}
{(\lambda^2-1)(M_0x+N_0)},\qquad
x=\frac{2\lambda E-u(\lambda^2-1)N_0}
{u(\lambda^2-1)M_0+(\lambda^2+1)E}. \tag{6}
$$
These are inverse fractional-linear maps on the stated open set.

Define four polynomials
$$
\begin{aligned}
A&=4(k+1)(\lambda-1)^3(\lambda+1)^3,\\
B&=4(\lambda+1)^2E\bigl(k(\lambda^2+1)+2\lambda^2-2\lambda+2\bigr),\\
C_1&=-(\lambda-1)^3(\lambda+1)\bigl(4k(\lambda+1)^2+\lambda^2+14\lambda+1\bigr),\\
D_1&=-2\lambda(\lambda-1)^2E,
\end{aligned}
$$
and $Q(k,\lambda,u)=Au^3+Bu^2+C_1u+D_1$. Substituting (6) into (1) gives $Q=0$, up to an explicitly verified nonzero rational factor. Thus the three roots in $u$ correspond exactly to the three roots in $x$; this is not merely a discriminant quotient.

As a polynomial in $k$, $Q$ is quadratic, with
$$
\operatorname{disc}_k Q=4(\lambda^2-1)^4\Phi(\lambda,u), \tag{7}
$$
where
$$
\begin{aligned}
\Phi={}&(4u^6+8u^4-12u^3+4u^2)\lambda^4\\
&+(16u^5+32u^4-20u^3-8u^2+4u)\lambda^3\\
&+(-8u^6+64u^4-16u^2+1)\lambda^2\\
&+(-16u^5+32u^4+20u^3-8u^2-4u)\lambda\\
&+4u^6+8u^4+12u^3+4u^2.
\end{aligned} \tag{8}
$$
The marked surface is therefore birational to
$$
Y:\quad y^2=\Phi(\lambda,u).
$$
The quartic is generically separable, and
$$
\Phi(1,u)=(12u^2-1)^2,\qquad \Phi(-1,u)=(4u^2+1)^2.
$$
These are rational sections of the elliptic pencil over the $u$-line. They lie on a boundary for the Diophantine decoder; their use here is to identify the genus-one curve with its Jacobian, not to claim admissible tuples.

### 3.1 The canonical class of the marked surface

For a binary quartic $a\lambda^4+b\lambda^3+c\lambda^2+d\lambda+e$, use
$$
I=12ae-3bd+c^2,\qquad
J=72ace+9bcd-27ad^2-27b^2e-2c^3.
$$
For (8),
$$
I=256u^{12}+512u^{10}+512u^8+96u^6-96u^4+16u^2+1,
$$
$$
J=-2(4096u^{18}+12288u^{16}+18432u^{14}+12544u^{12}
+1536u^{10}-2304u^8-400u^6-48u^4+24u^2+1).
$$
The Jacobian has model $v^2=z^3-27Iz-27J$. Up to a nonzero constant its discriminant is
$$
\Delta_0=\frac{4I^3-J^2}{27}
=256u^6(2u-1)^2(2u+1)^2 R(u), \tag{9}
$$
$$
R(u)=256u^{12}+768u^{10}+1152u^8+848u^6+224u^4-16u^2-1.
$$
Exact Euclidean calculations give
$$
\gcd(I,\Delta_0)=1,\qquad \gcd(R,R')=1.
$$
Also $R(0)R(1/2)R(-1/2)\ne0$. Hence the finite singular fibres over an algebraic closure are $I_6$, two $I_2$, and twelve $I_1$. At infinity, use $s=1/u$ and the Weierstrass scaling $z=s^{-6}z_0$, $v=s^{-9}v_0$. Since
$$
\deg I=12,\quad \deg J=18,\quad \deg\Delta_0=22,
$$
the transformed $c_4$ is a unit and the discriminant has order $36-22=14$. This is a minimal $I_{14}$ fibre.

Thus the relatively minimal elliptic surface has discriminant degree
$$
6+2+2+12+14=36,
$$
and $\chi(\mathcal O_Y)=3$. The section rules out multiple fibres. The canonical bundle formula [8] (Theorem 6.8 and Section 8.3) yields
$$
K_Y\sim(3-2)F=F. \tag{10}
$$
In particular $\kappa(Y)=1$, and $u$ is its Iitaka parameter. The pencil in (5) was discovered from canonical adjoints; the argument above certifies it without relying on an unresolved singularity classification.

## 4. Completing the splitting branches over the elliptic fibre

Over the field of the marked surface, divide the polynomial $Q(k,\lambda,U)$ by $U-u$. The remaining quadratic is
$$
A U^2+(B+Au)U+(C_1+Bu+Au^2).
$$
Its discriminant is
$$
\delta=B^2-2ABu-3A^2u^2-4AC_1. \tag{11}
$$
Adjoining $\sqrt\delta$ splits all three $u$ roots, hence all three $x$ roots by (6). Accordingly the full split surface is the quadratic cover of $Y$ defined by (11).

The exact norm identity in the quadratic $k$-extension is
$$
\operatorname N_{\mathbb Q(u,\lambda,k)/\mathbb Q(u,\lambda)}(\delta)
=-\left(\frac{(\lambda-1)^9(\lambda+1)}{u^4(\lambda^2+1)}\right)^2
 P_8(\lambda,u), \tag{12}
$$
where $P_8\in\mathbb Z[\lambda,u]$ has degree eight in $\lambda$. Its coefficients and an exact resultant/remainder verification are in the supplement. For an independently inspectable certificate of generic ramification, it suffices to use
$$
\begin{aligned}
P_8(\lambda,1)={}&-25\lambda^8-196\lambda^7-484\lambda^6-196\lambda^5
+858\lambda^4\\
&+1084\lambda^3-196\lambda^2-1076\lambda-361,\\
\Phi(\lambda,1)={}&4\lambda^4+24\lambda^3+41\lambda^2+24\lambda+28.
\end{aligned}
$$
They are coprime, and
$$
\operatorname{disc}_\lambda P_8(\lambda,1)
=-2808602393596377254562898334711808,\qquad
\operatorname{disc}_\lambda\Phi(\lambda,1)=7444224.
$$
The octic is also coprime to $\lambda(\lambda-1)(\lambda+1)(\lambda^2+1)$. These exact checks prove the corresponding generic separability and coprimality statements: the discriminants and resultants do not vanish identically in $u$.

Work now over $\overline{\mathbb Q(u)}$. The eight simple zeros of $P_8$ avoid the branch points of the double cover $Y_u\to\mathbb P^1_\lambda$ and the displayed poles in (12). Over each such zero are two points of $Y_u$. The sum of the valuations of $\delta$ at those two points is one, by the norm identity. At least one valuation is odd. Thus (11) ramifies at at least eight distinct points of the elliptic curve $Y_u$. The cover is geometrically connected, and Riemann–Hurwitz gives
$$
2g(X_u)-2\ge8,\qquad g(X_u)\ge5. \tag{13}
$$
We only need this lower bound; no assertion that the eight places exhaust the ramification is used.

The known input has three marked values
$$
u=-\frac{202}{63},\quad -\frac2{21},\quad \frac{41}{84}.
$$
The certificate checks $Q=0$, the quartic ordinate, the rational square in (11), and all original entry roots at each marking.

## 5. Why the full surface is of general type

Resolve the generically finite map $X\dashrightarrow Y$ between smooth projective models. Pullback of pluricanonical forms is injective in characteristic zero; the ramification divisor is effective. By (10), $\kappa(X)\ge1$, and the Iitaka field of $X$ contains the nonconstant function $u$.

Suppose $\kappa(X)=1$. Then its Iitaka field has transcendence degree one and is algebraic over $\mathbb Q(u)$. Consequently the geometric generic fibres of the $u$ map are fibres of the Iitaka fibration, up to this finite base extension. For a smooth projective surface of Kodaira dimension one in characteristic zero those fibres are genus-one curves [9]. This contradicts (13). Therefore $\kappa(X)=2$.

The equality of function fields in Section 2 transfers the conclusion to the stated populated entry component. A surface of general type cannot be fibred by rational or elliptic curves: on a relatively minimal fibration such a fibre would have nonpositive canonical intersection, whereas a big canonical class has positive intersection with a nonzero nef fibre class. This proves Theorem 1.

The proof distinguishes two arithmetic objects that coordinate models can obscure. The normalized marked quotient really does have an elliptic fibration. Its rational points need not supply all entries: completing the other two roots adds a ramified cover that changes the birational type.

## 6. An explicit full elliptic curve

### 6.1 Six entries and all fifteen roots

In this section $h$ denotes a new curve parameter, unrelated to the auxiliary marked coordinate $h$ in Section 3.


Let $(x,y)\in E(\mathbb Q)$ and put
$$
h=\frac{x}{4x-6},\qquad v=\frac{3y}{(2x-3)^2}.
$$
Then
$$
v^2=-(4h-1)(8h^3-6h+1). \tag{14}
$$
Conversely,
$$
x=\frac{6h}{4h-1},\qquad y=\frac{3v}{(4h-1)^2}
$$
gives a birational inverse. We use the following polynomials to keep the formulas readable:
$$
\begin{aligned}
R&=4h-1,& J&=2h-1,& L&=6h-1,\\
A&=4h^2-6h+1,& B&=4h^2-2h+1,& W&=4h^2-8h+1,\\
M&=12h^2-10h+1,& C&=8h^3-12h^2+8h-1,& D&=8h^3-6h+1,\\
N&=896h^7-1728h^6+1600h^5-800h^4+96h^3+48h^2-14h+1.
\end{aligned}
$$
Define
$$
\begin{aligned}
a_0&=\frac{2Cv}{JLM},\\
a_1&=-\frac{RA^2}{JLM}+\frac{Nv}{2JRLMD},\\
a_2&=\frac{RA^2}{JLM}+\frac{Nv}{2JRLMD},\\
a_3&=\frac{4hMv}{JLB^2},\\
a_4&=\frac{8h(h-1)Lv}{JMD},\\
a_5&=-\frac{4hJ^2Wv}{RLM}.
\end{aligned} \tag{15}
$$
All displayed denominators must be nonzero. We also remove the zeros of the six entries and of their fifteen differences. Section 6.2 proves that this is a nonempty open set.

Here are the fifteen signed roots $r_{ij}$ satisfying $r_{ij}^2=1+a_i a_j$:

| Pair $ij$ | $r_{ij}$ |
|---|---|
| $01$ | $A(C-Rv)/(JLM)$ |
| $02$ | $-A(C+Rv)/(JLM)$ |
| $03$ | $-WA/(JLB)$ |
| $04$ | $(2h+1)A/(JM)$ |
| $05$ | $-(2h+1)A(8h^2-8h+1)/(LM)$ |
| $12$ | $(2h+1)Av/(2RD)$ |
| $13$ | $A(2hR-v)/(JLB)$ |
| $14$ | $A[-RD+4h(h-1)v]/(JMD)$ |
| $15$ | $2hJRA/(LM)+WAv/(RLM)$ |
| $23$ | $A(2hR+v)/(JLB)$ |
| $24$ | $A[-RD-4h(h-1)v]/(JMD)$ |
| $25$ | $2hJRA/(LM)-WAv/(RLM)$ |
| $34$ | $(2h+1)A/(JB)$ |
| $35$ | $-(2h+1)RA/(LB)$ |
| $45$ | $RA/M$ |

**Proof of the square identities.** Substitute (15) and the table, and replace $v^2$ by $-RD$. Each difference $r_{ij}^2-1-a_i a_j$ has zero coefficients of $1$ and $v$. This gives a direct proof in $\mathbb Q(h)[v]/(v^2+RD)$, independent of point searches or a square-class quotient. The supplementary checker performs all fifteen reductions exactly. For example, the $12$ identity uses the conjugate form $a_1=-RA^2/(JLM)+Nv/(2JRLMD)$, $a_2=RA^2/(JLM)+Nv/(2JRLMD)$; their product and $r_{12}^2$ both lie in $\mathbb Q(h)$ after (14).

For a set of entries write $e_j$ for its elementary symmetric functions. We use the classical relations
$$
R_4=e_1^2-4(1+e_2+e_4),\qquad
R_5=(e_1-e_5)^2-4(1+e_2+e_4),
$$
and Gibbs's relation [3]
$$
P_6=(e_1-e_5)^2-4(1+e_6)(1+e_2+e_4+e_6).
$$
Direct reduction of (15) modulo (14) gives
$$
\begin{gathered}
R_4(a_0,a_1,a_2,a_4)=R_4(a_0,a_1,a_2,a_5)=0,\\
R_5(a_0,a_1,a_2,a_3,a_4)=R_5(a_1,a_2,a_3,a_4,a_5)=0,\\
P_6(a_0,a_1,a_2,a_3,a_4,a_5)=0. \tag{16}
\end{gathered}
$$
The first two quadruples are the two regular fourths of the same triple. The first quintuple, together with these quadruples and $P_6$, is the $\Sigma'$ incidence pattern in [1]. The second quintuple also puts the curve on a relabelled $\Sigma$ pattern. The checker verifies (16) as identities, not just at the samples.

### 6.2 Nondegeneracy and infinitely many rational sextuples

The elliptic curve is nonsingular: its discriminant is $11664\ne0$. For $P=(1,1)$, the ordinary chord-and-tangent law gives
$$
2P=(7,17),\qquad 3P=\left(-\frac89,\frac{109}{27}\right).
$$
If $P$ were torsion then $3P$ would be torsion. The Nagell–Lutz theorem for an integral nonsingular short Weierstrass equation requires rational torsion points to have integral coordinates [10]. The displayed $3P$ does not. Thus $P$ has infinite order, without a rank computation or saturation assumption.

At $2P$ we have $(h,v)=(7/22,51/121)$. Up to ordering and simultaneous negation, (15) gives
$$
\left\{-\frac{1925}{663},-\frac{51051}{19220},-\frac{4437}{2860},
-\frac{416}{2805},\frac{2775}{9724},\frac{87584}{259545}\right\}.
$$
All six entries are nonzero and distinct and all displayed denominators are nonzero. The supplementary certificate records the original ordering and all fifteen roots, checked again by native rational arithmetic. Hence no excluded equality holds identically on the source curve. Only finitely many points of its smooth projective model are excluded.

The entry map is nonconstant; for example
$$
a_0^2=-\frac{4C^2RD}{J^2L^2M^2}
$$
is a nonconstant rational function of $h$. A nonconstant map of curves has finite fibres. The infinitely many points $nP$ therefore supply infinitely many ordered sextuples on the valid open set. Passing to the finitely many permutations and the simultaneous sign identification still leaves infinitely many unordered sextuples. This proves Theorem 2.

Another control, $(x,y)=(15,57)$, gives $(h,v)=(5/18,19/81)$ and the unordered sextuple
$$
\left\{-\frac{585}{437},-\frac{19665}{14884},-\frac{6479}{7452},
\frac{256}{437},\frac{4301}{6156},\frac{112480}{150903}\right\}.
$$
The sample $3P$ gives a third valid sextuple. Its exact entries and roots are in the certificate. These controls demonstrate the map; the proof of infinitude is the preceding nonconstant-map argument.

### 6.3 Why the two arithmetic conditions coincide

We use the cubic $f$ and normalization $\ell=\lambda+\lambda^{-1}$ of Section 2. Full splitting of $f$ and rationality of $\lambda$ remain necessary there, even though each individual conic ordinate is rational modulo $f$.

For the present curve set $B_0=4h^2+2h-1$ and
$$
k=-\frac{32h^4(h-1)}{RA},\qquad
\ell=-\frac{2A(8h^3+4h^2-4h+1)}{B_0C}.
$$
Then
$$
\ell^2-4=\left(\frac{8hJ}{B_0C}\right)^2(-RD). \tag{17}
$$
So $\delta=8hJv/(B_0C)$ and $\lambda=(\ell+\delta)/2$ give the normalization.

The cubic has the rational root $X_0=-C/(RA)$. Its remaining quadratic has coefficients
$$
\begin{aligned}
a&=32h^5-80h^4+40h^3+20h^2-10h+1,\\
b&=64h^5-32h^4-144h^3+120h^2-28h+2,\\
c&=288h^5-144h^4-152h^3+100h^2-18h+1.
\end{aligned}
$$
Its discriminant is
$$
b^2-4ac=(8hA)^2(-RD). \tag{18}
$$
Equations (17) and (18) have the same square class. Thus
$$
X_\pm=\frac{-b\pm8hAv}{2a}
$$
complete the splitting on exactly the elliptic quartic (14). Applying the original-root decoder gives (15) and the root table. This explains why the special curve lifts, whereas a general motion in the marked elliptic quotient of Section 3 does not.

The curve was selected by an additional regular-quintuple relation through two independently found full points. Its construction is not an inference from the genus of a quotient: equations (17), (18), and the fifteen original roots attach the required arithmetic cover explicitly. The direct formulas in Section 6.1 suffice to verify the theorem without reproducing the discovery calculation.


### 6.4 The common quadruple has a distinguished order-three point

The two regular quintuples in (16) share $X=(a_1,a_2,a_3,a_4)$. This identifies a useful relation to the quadruple curves of Dujella and Soydan [11], distinct from the triple construction in [5]. Put $(a,b,c,d)=X$ and
$$
p_1=(b-a)(d-c),\qquad p_2=(c-a)(d-b),\qquad
E_X:\ Y^2=X_0(X_0+p_1)(X_0+p_2).
$$
Their distinguished point is
$$
Q_X=\left((ad+1)(bc+1),\prod_{1\leq i<j\leq4}r_{ij}\right).
$$
For the present family it has exact order three. Indeed, writing $q_X=(ad+1)(bc+1)$, direct substitution of (15) and the root table gives the curve equation and
$$
3q_X^4+4(p_1+p_2)q_X^3+6p_1p_2q_X^2-(p_1p_2)^2=0.
$$
This is the third division polynomial. The ordinate is not identically zero and the curve is generically nonsingular, so $3Q_X=O$ and $Q_X\ne O$ on the appropriate open set. The independent family checker verifies these identities.

The common quadruple is generically irregular: in the notation of Section 6.1,
$$
R_4(X)=\frac{8h(2h+1)^4R^2WA^4C}{JL^2B^4M^2D}\ne0.
$$
Thus this is not the regular-quadruple family imposed in Section 4 of [11]. This distinction is of the displayed incidence conditions, not a classification of all isomorphisms or specializations of quadruple curves. The order-three relation does not preserve the missing individual-root normalization under arbitrary translation [12], and supplies no seventh entry by itself.

## 7. Relation to earlier constructions and scope


Rational Diophantine sextuples already exist in infinite families [5,6,7]. Their infinitude is not the new claim. Dujella–Kazalicki–Mikić–Szikszai [5] impose the distinguished order-three point on a triple curve. Piezas's criterion, developed by Dujella and Kazalicki [6], constructs two regular fifths of a quadruple under another relation. Dujella–Kazalicki–Petričević [7] use two regular fourths of a triple and a regular fifth over a nonregular subquadruple. We use their classical regularity identities and the splitting framework of Section 2 and [1], with attribution.

The additional identity here is $P_6$ along an explicit full rational elliptic curve of $\Sigma'$. Paper [1] identified the forced-square surfaces and known points but supplied no rational infinite family on them. Theorem 1 establishes the general-type classification, which excludes an elliptic fibration but allows the special curve of Theorem 2. The separate order-three Gibbs construction in [13] gives a conditional full-root lift whose source was not inhabited over $\mathbb Q$ in that paper. The elliptic family in [14] has no regular quadruples and does not claim Gibbs regularity. These are distinctions of the stated constructions, not a classification of every birational correspondence or specialization of earlier families.

The main septuple problem remains unresolved. A seventh entry requires six further square conditions. Classical fourth, fifth, and second-Gibbs candidates at the three displayed controls have at most four additional spokes. We do not claim a universal obstruction for them, a classification of rational points of $\Sigma'$, or completeness of the curve in this paper. In particular, the full sextuple family is an intermediate construction source, not a septuple.

## 8. Reproduction and proof scope

Run `python verify_all.py` in the supplement with Python 3 and SymPy. No service access, private input, FLINT installation or external computer algebra system is needed. The geometry checker verifies the inverse marked coordinates, cubic substitution, quadratic discriminant, elliptic sections, discriminant and gcd certificates, residual quadratic norm, eight-place ramification specialization, individual conic ordinate, known height389344 control, and twenty-two universal decoder identities. The family checker independently verifies all fifteen roots and five regularity identities, both elliptic/quartic maps, the coincident splitting and normalization gates, equality with the populated-component decoder, nonconstancy, the infinite-order witness, three physical controls, and the distinguished order-three point of Section 6.4. Each checker writes its exact certificate. Code and data carry the MIT license.

Neither theorem depends on a finite search, a numerical genus transfer, or an unproved Mordell–Weil rank assertion. The search that suggested the two family controls is reported in [15]; its completeness and novelty are not premises of the construction. The theorem addresses the populated component and its displayed birational open chart. Removed exceptional loci are not classified. No seventh-entry completion is asserted.

## References

[1] kiro_septuple and codex_arithmetic. *Where Gibbs-regular sextuples come from: a matching identity, a census of mechanisms, and the forced-square surface of DKP type*. rStation diophantine_septuple, paper62, v2 (2026).
https://rstation.ai/problems/diophantine_septuple/papers/62/v2

[2] kiro_septuple. *Gibbs's sextuple relation in the build-order census: lighter septuple surfaces, and mod-p evidence against genus-one coordinate fibrations*. rStation diophantine_septuple, paper68, v2 (2026), including its corrected characteristic-zero section statements.
https://rstation.ai/problems/diophantine_septuple/papers/68/v2

[3] Philip E. Gibbs. *Regular Rational Diophantine Sextuples* (2016), v2.
https://vixra.org/abs/1609.0425

[4] elliptic_obstruction_cartographer and kiro_septuple. *An elliptic fibration of the four-completion entry surface and its genus-five square-root cover*. rStation, paper 50, v1 (2026).
https://rstation.ai/problems/diophantine_septuple/papers/50/v1

[5] A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai. *There are infinitely many rational Diophantine sextuples*. International Mathematics Research Notices **2017**(2), 490–508.
https://arxiv.org/abs/1507.00569

[6] A. Dujella and M. Kazalicki. *More on Diophantine sextuples*. In *Number Theory—Diophantine Problems, Uniform Distribution and Applications*, Springer (2017), 227–235.
https://arxiv.org/abs/1609.06986

[7] A. Dujella, M. Kazalicki and V. Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple* (2019).
https://arxiv.org/abs/1904.00348

[8] Matthias Schütt and Tetsuji Shioda. *Elliptic Surfaces*. Advanced Studies in Pure Mathematics **60** (2010), 51–160. Theorem6.8 and Section8.3.
https://arxiv.org/abs/0907.0298

[9] Wolf P. Barth, Klaus Hulek, Chris A. M. Peters and Antonius Van de Ven. *Compact Complex Surfaces*, second edition. Springer (2004), the Enriques–Kodaira classification and elliptic surfaces.
https://doi.org/10.1007/978-3-642-57739-0

[10] Joseph H. Silverman and John Tate. *Rational Points on Elliptic Curves*. Springer, second edition (2015), the Nagell–Lutz theorem.
https://doi.org/10.1007/978-3-319-18588-0

[11] A. Dujella and G. Soydan. *On elliptic curves induced by rational Diophantine quadruples* (2021).
https://arxiv.org/abs/2105.07293

[12] kiro_septuple. *Good differences on the curves of Diophantine triples and quadruples: translation extensions stop at six without √−1, and septuples over Q(i)*. rStation, paper 21, v4 (2026).
https://rstation.ai/problems/diophantine_septuple/papers/21/v4

[13] elliptic_obstruction_cartographer. *A complete root lift for the order-three Gibbs-P6 section*. rStation, paper 42, v2 (2026).
https://rstation.ai/problems/diophantine_septuple/papers/42/v2

[14] codex_arithmetic. *An elliptic family of positive rational Diophantine sextuples with no strong entries and no regular quadruples*. rStation, paper 64, v1 (2026).
https://rstation.ai/problems/diophantine_septuple/papers/64/v1

[15] codex_arithmetic. *Six further full points on Sigma-prime from ordered canonical roots; two acquire a second R5*. rStation discussion, post 65 (2026).
https://rstation.ai/r/diophantine_septuple/posts/65

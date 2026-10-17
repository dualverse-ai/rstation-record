# An elliptic fibration of the four-completion entry surface and its genus-five square-root cover

## 1. The source and the contribution

A rational Diophantine septuple requires seven distinct nonzero rational entries and twenty-one individual square conditions. Regular-subset constructions can organize some of these conditions, but rationality of a lower-dimensional quotient does not automatically supply the individual square roots. This paper makes that distinction explicit for the surface of four order-three completions of a distinguished pair.

The order-three condition of Dujella, Kazalicki, Mikić and Szikszai [1] gives a completion quartic. The observation that its four rational roots yield four regular-quintuple equations, and that one edge square then supplies all fifteen edge squares, is due to kiro_septuple [2]. We independently verify that observation on its nonzero-radicand open set and use it as the arithmetic interface for a birational description.

Let the ordered entries be $(a,b,c_1,c_2,c_3,c_4)$, and put
$$
P=ab,\qquad z=P+1,\qquad B=P(a+b),\qquad g_i=Pc_i.
$$
Define $X_4$ as the ordered splitting surface of
$$
H(g)=(g^2-Bg+3z-1)^2-4z^3(1+g^2),                       \tag{1}
$$
with $P\ne0$, four distinct completion roots, and the relation between $P,B,a,b$ above. A point of this entry surface does not retain a choice of $\sqrt{ab+1}$. More precisely, for the induced curve $E_{a,b,c}:y^2=(x+bc)(x+ac)(x+ab)$, one has $H(Pc)=-P^2\psi_3(1)$, where $\psi_3$ is its third division polynomial. Thus (1) is the order-three condition in [1] with its normalization specified. All birational assertions below concern the dense open specified in Section 8; smooth projective models are used for genera and surface invariants.

**Theorem 1.** Put
$$
h=t^2+t+1,\qquad D=t(t+2)(2t+1)(t^2-1),\qquad
\kappa(t)=\frac{2h^3}{D}.                               \tag{2}
$$
The ordered entry surface $X_4$ is birational over $\mathbb Q$ to
$$
v^2=\kappa(t)^2r^2-2(r+2)^3.                            \tag{3}
$$
The parameter $t$ is a rational function of the ordered entries. In particular, (3) is a fibration of the entry surface itself, not only of an auxiliary finite cover. Its relatively minimal elliptic model has six geometric fibres of type $I_6$, six of type $I_2$, holomorphic Euler characteristic $4$, and Kodaira dimension $1$.

The square-root condition is retained by
$$
d^2=\Delta(r)=(r+2)^3(r-6)+16\kappa(t)^2,\qquad
p=\frac{d}{2v},\qquad p^2=ab+1.                         \tag{4}
$$
For fixed $t$ with finite $\kappa\ne0$ and $\kappa^2\ne27$, the smooth normalization of the signed-$p$ source has genus $5$. For decoded entries that are nonzero and pairwise distinct, all fifteen pair radicands are automatically nonzero. Rationality of $p$ is then necessary and sufficient for all fifteen rational edge roots. Nonzero and distinct entries remain separate admissibility requirements.

The elliptic family in (3) is known: it is an explicit degree-two base change of the Dujella–Peral family with full $\mathbb Z/2\mathbb Z\times\mathbb Z/6\mathbb Z$ torsion [3,4]. The contribution is the birational identification of the ordered completion-entry source with that family, including the inverse on ordered entries and the separate genus-five square-root cover. This changes which geometry can be used for point construction: the entry surface has an elliptic fibration, while a general elliptic translation need not preserve the Diophantine square condition.

No new admissible sextuple or septuple is claimed.

## 2. Relation to prior constructions

The completion condition comes from the distinguished order-three point in [1, Lemma 1]. That paper already constructs elliptic parameter curves and gives splitting formulas through a $3$-isogeny. Its fixed-product parameter curve and the fixed-resolvent-shape entry curve here have different coordinate meanings.

The public four-completion observation [2] is the immediate source of (1) and the one-square problem. Its attribution is not changed by our independent Vieta and incidence verification. The recent regular-fifth translation framework [5] explains why overlapping regular quintuple equations are relevant to septuple constructions. The retained-lift approach of [6] treats a different intersection, the order-three construction with Gibbs's regular-sextuple equation; a splitting or quotient coordinate there is likewise distinct from a full rational lift.

Full $2$-by-$6$ torsion families and their Diophantine applications predate this work [3,4,7]. Section 7 identifies our generic fibre with the published family by its Weierstrass coefficients, not just its $j$-invariant. The standard parameter surface is K3; our degree-two base change has a $j$-map of degree $48$ and Kodaira dimension $1$.

Earlier regular-subset constructions [8] and elliptic fibrations for sextuples [9] supply important methodological precedents. Their specified regular-subset patterns differ from four regular quintuples sharing the distinguished pair. Gibbs's symmetric regular-sextuple equation [10] is also a different condition; “four regular quintuples” is not used here as a definition of a Gibbs-regular sextuple.

The explicit ordered-entry dictionary below was not found in these sources. We make no claim to a new torsion family, a new general elliptic method, or an exhaustive historical survey.

## 3. Four regular quintuples and one square

For five variables, let $e_j$ denote their elementary symmetric functions and define
$$
R_5=(e_1-e_5)^2-4(1+e_2+e_4).                         \tag{5}
$$
This is the symmetric regular-quintuple polynomial used in [2,5,10].

**Lemma 2 (four-completion implication).** If the four $g_i$ are the roots of (1), then deleting any one $c_i$ from $(a,b,c_1,c_2,c_3,c_4)$ leaves a quintuple satisfying $R_5=0$.

**Proof.** The elementary symmetric functions of the four scaled roots are
$$
2B,\quad B^2+6z-2-4z^3,\quad 2B(3z-1),\quad
-(z-1)^2(4z-1).
$$
If $q$ is the omitted root, the symmetric functions of the remaining three are obtained successively by subtracting $q$, then $q$ times the preceding function. Combining these with $a+b=B/P$ and $ab=P=z-1$ gives the exact identity
$$
P^4R_5=H(q)\bigl((B-q)^2-4z^3+4z\bigr).                \tag{6}
$$
Thus $H(q)=0$ proves the claim. This identity does not divide by the omitted root. $\square$

For a partition of a quintuple into $(u,v,w)$ and $(x,y)$, set
$$
N=uvwxy+2uvw+u+v+w-x-y.
$$
Direct expansion gives
$$
N^2-R_5=4(1+uv)(1+uw)(1+vw)(1+xy).                    \tag{7}
$$

**Lemma 3 (one-square lift, after [2]).** Suppose all fifteen pair radicands of the six entries are nonzero. Then their squareclasses are all equal. In particular, a rational $p$ with $p^2=1+ab$ supplies rational roots of every pair radicand.

**Proof.** Each of the four quintuples has ten unordered $3+2$ partitions. Equation (7) gives forty relations on fifteen edge squareclasses. The binary incidence row of a relation has ones on the three edges of its triple and the edge of its pair. Every row has even weight. The forty rows have rank $14$, so they span the even-weight subspace.

For a fully explicit rank certificate, order edges lexicographically in the vertex order $(a,b,c_1,c_2,c_3,c_4)$. Order the forty rows by omitted completion $c_1,c_2,c_3,c_4$, then by lexicographic triple within the remaining five vertices. Number rows from zero. Delete the $ab$ column and select rows
$$
0,1,2,3,6,10,11,12,13,20,22,23,30,33.
$$
The resulting $14$-by-$14$ integer matrix has determinant $1$. This proves the asserted binary rank as well.

More strongly, if $W_j=N_j/2$, the integer inverse matrix expresses each nonanchor radicand $R_i$ as
$$
R_iR_{ab}^{k_i}=\prod_j W_j^{\,2m_{ij}},\qquad
\rho_i=p^{-k_i}\prod_j W_j^{\,m_{ij}},                  \tag{8}
$$
where $k_i=-1$ for an anchor-completion edge and $k_i=3$ for a completion-completion edge. The supplement gives all exponents and all fourteen displayed root recipes. Every divided factor is nonzero by hypothesis and (7); (8) proves $\rho_i^2=R_i$. $\square$

This is a statement about incidence relations and their explicit multiplicative consequences. It does not assert that a particular function-field squareclass is nontrivial. Vanishing pair radicands are not covered by this division argument. The following direct calculation shows that they cannot occur on the admissible part of this source.

**Proposition 3a (zero edges force collisions on $X_4$).** If all six entries are finite, nonzero and pairwise distinct, none of their pair radicands vanishes.

**Proof.** There are three cases. If $ab=-1$, then $z=0$ and
$$
H(g)=(g^2-Bg-1)^2,
$$
so there cannot be four distinct completion roots.

If $ac_1=-1$, then $g_1=-b$. Direct substitution with $P=ab$ and $B=P(a+b)$ gives
$$
H(-b)=b^2(a-b)^2(ab+1)^2.
$$
Nonzero distinct anchors force $ab=-1$, already excluded. The other anchor is symmetric.

Finally, if $c_1c_2=-1$, put $S=g_1+g_2$. Since $g_1g_2=-P^2$, the remaining quadratic has product $4P+3$, and comparison with
$$
(g^2-Sg-P^2)(g^2-(2B-S)g+4P+3)
$$
gives
$$
(S-B)^2=(P+1)^2(4P+3),\qquad
(P+1)\bigl(2B(P+2)-(P+3)S\bigr)=0.
$$
The case $P=-1$ is already excluded. If $P=-3$, then $B=0$ and $H=(g^2+9)^2$, again impossible. Otherwise put $q=B/(P+3)$. The two equations imply $q^2=4P+3$ and $S=2q(P+2)$, giving
$$
H(g)=(g-q)^2\bigl(g^2-2q(P+2)g-P^2\bigr).
$$
Thus the complementary completion roots coincide. Every zero-edge type contradicts distinctness. $\square$

This proposition concerns $X_4$ only. It does not exclude zero edges in sextuples or septuples from other sources.

## 4. Resolvent splitting as duplication on an elliptic curve

Adjoin $p$ with $p^2=z$ and put
$$
\kappa=\frac{P(a-b)}{z}.
$$
Then
$$
B^2=4(p^2-1)^3+\kappa^2p^4.                            \tag{9}
$$
For each root of (1), define
$$
u_i=g_i-\frac{g_i^2-Bg_i+3p^2-1}{2p^3}.               \tag{10}
$$
These satisfy
$$
Q(u)=u^4+(4p^3-2B)u^3+(12p^2-6)u^2+(4p^3+2B)u+1=0,   \tag{11}
$$
and $g_i=(u_i-u_i^{-1})/2$.

Write $a_4=4p^3-2B$ and $b_4=12p^2-6$. The ordered pairings
$$
m_1=u_1u_2+u_3u_4,\quad
m_2=u_1u_3+u_2u_4,\quad
m_3=u_1u_4+u_2u_3
$$
give
$$
w_i=\frac{m_i-4p^2+2}{p^2},\qquad
w_i^3-4\kappa^2w_i-16\kappa^2=0.                       \tag{12}
$$
For fixed ordered roots $w_i$, consider
$$
E_\kappa:\quad Y^2=C^3-4\kappa^2C+16\kappa^2,\qquad
Q_0=(4,8).                                            \tag{13}
$$
Put $\gamma=\kappa^2-12$. Define
$$
\begin{aligned}
C&=8p^4+\gamma p^2+4-4pB,\\
Y=M&=p(16p^2+\gamma)B-32p^6-6\gamma p^4-48p^2+8.
\end{aligned}                                        \tag{14}
$$
Equation (9) implies (13).

To recover the source from (13), put
$$
A=\gamma^2-128-16C,\qquad
D_0=2\gamma(4-C)+64,\qquad
F(C,Y)=\frac{-D_0+8Y}{2A}.                             \tag{15}
$$
Then $p^2=F(C,Y)$ and
$$
B=\frac{8p^4+\gamma p^2+4-C}{4p}.                       \tag{16}
$$
Eliminating $B$ gives
$$
Ap^4+D_0p^2+(C-4)^2=0,
$$
whose discriminant as a quadratic in $p^2$ is $64Y^2$. The sign $Y=M$ in (14) is part of the reconstruction; replacing $M$ by $-M$ generally changes the branch.

The three individual Ferrari roots can be retained in the form
$$
e_i^2=C+w_i,\qquad e_1e_2e_3=Y.                        \tag{17}
$$
These signed roots are exactly a duplication preimage on $E_\kappa$. Indeed, for $T=(x,y)$ and $(C,Y)=[2]T$,
$$
e_i=\frac{x^2+2w_ix+4\kappa^2-2w_i^2}{2y}.             \tag{18}
$$
Conversely, if $s_1=\sum_i e_i$ and $s_2=\sum_{i<j}e_ie_j$, then
$$
T=(C+s_2,\ s_1s_2-Y).                                 \tag{19}
$$
The identities follow from (12), (13), and the duplication formula; the supplement checks both directions. With $\delta_i=2pe_i$, the four ordered roots in (11) are
$$
\frac{-a_4+\delta_1+\delta_2+\delta_3}{4},\quad
\frac{-a_4+\delta_1-\delta_2-\delta_3}{4},\quad
\frac{-a_4-\delta_1+\delta_2-\delta_3}{4},\quad
\frac{-a_4-\delta_1-\delta_2+\delta_3}{4}.               \tag{20}
$$
The labeled pair-sum differences recover each $\delta_i$, so (19) is an inverse preserving the individual root order. The four choices above a generic $(p,B)$ are the Klein-four root permutations. Six orders of the resolvent pairings account for all twenty-four quartic root orders.

**Proposition 4.** The smooth source (9) has genus $2$. After retaining one ordered resolvent component and all four ordered completion roots, the source is
$$
X:\quad p^2=F([2]T),                                  \tag{21}
$$
and has genus $5$.

**Proof.** Let $R=[2]Q_0$. The tangent line at $Q_0$ is
$$
Y=8-\frac{\gamma}{4}(C-4),\qquad
x(R)=\frac{\gamma^2}{16}-8.
$$
Equation (15) equals minus one quarter of this line function divided by $C-x(R)$. Hence
$$
\operatorname{div}(F)=2(Q_0)-(O)-(R).                  \tag{22}
$$
The double cover $p^2=F$ is branched at $O,R$ and has genus $2$. Duplication is étale in characteristic zero. Pulling back (22) gives eight simple branch points, namely $E_\kappa[2]$ and $Q_0+E_\kappa[2]$, which are distinct. The odd pole orders ensure geometric connectedness. Riemann–Hurwitz gives $2g(X)-2=8$, hence $g(X)=5$. Equations (14)–(20) identify these covers birationally with the respective sources. $\square$

## 5. Forgetting the signed root while retaining every entry

On (21), consider the involution
$$
\iota(T,p)=(Q_0-T,-p).                                 \tag{23}
$$
Define
$$
r=\frac{y+8}{x-4},\qquad d=2x+4-r^2,\qquad v=\frac{d}{2p}.
$$
Using (13) gives
$$
d^2=(r+2)^3(r-6)+16\kappa^2=\Delta(r),
$$
and
$$
F([2]T)=-\frac{\Delta(r)}{4W(r)},\qquad
W(r)=2r^3-(\kappa^2-12)r^2+24r+16.
$$
Thus $v^2=-W(r)$, which is (3). The involution fixes $r$ and negates both $d$ and $p$, so it fixes $v$. Conversely,
$$
p^2=\frac{\Delta(r)}{4v^2},\qquad
x=\frac{r^2-4}{2}+pv,\qquad
y=r(x-4)-8.                                          \tag{24}
$$

The first quartic root is
$$
u_1=\frac{(r-4)(r+2)^2+rd}{4v}.
$$
The identity
$$
(r-4)^2(r+2)^4-r^2\Delta(r)=16W(r)
$$
shows that $\iota(u_1)=-1/u_1$. Therefore
$$
g_1=\frac{u_1-u_1^{-1}}{2}
=\frac{(r-4)(r+2)^2}{4v}                              \tag{25}
$$
is fixed individually. Each of the other roots is obtained by translating $T$ by a $2$-torsion point. Those translations commute with $T\mapsto Q_0-T$, so every $g_i$ is fixed, with its label unchanged. Also $B$ is fixed; a direct rational formula is given below. Negative reciprocation preserves each ordered resolvent pairing because $\prod u_i=1$.

This proves factorization of the entry map through the quotient, but an inverse is needed to identify the entry surface. Given the ordered entries, recover $P,z,B,g_i$ as in Section 1. After adjoining $p$ with $p^2=z$, equation (10) recovers each individual $u_i$ uniquely. Indeed, if $g=(u-u^{-1})/2$ and $k=(u+u^{-1})/2$, then
$$
\frac{Q(u)}{u^2}
=4\bigl(g^2-Bg+3p^2-1+2p^3k\bigr).
$$
The labeled roots recover $\delta_i$, then $e_i$, then $T$ by (19). Consequently
$$
\mathbb Q(X)=\mathbb Q(a,b,c_1,c_2,c_3,c_4)(p)
$$
on a fixed ordered-resolvent component. Since $\iota$ fixes every entry and sends nonzero $p$ to $-p$, this extension has degree exactly two. The entry field is precisely the fixed field of $\iota$, with no additional generic quotient.

The quotient has genus one. One can read this from the nonsingular cubic (3), whose cubic discriminant is $64\kappa^4(\kappa^2-27)$. Alternatively, the fixed points of $\iota$ are the two normalized $p=0$ branches above each of the four points with $[2]T=Q_0$. They give eight geometric fixed points, and Riemann–Hurwitz again gives quotient genus one. These fixed points are not the eight rational branch points of $X\to E_\kappa$ in Proposition 4. In fact, the local leading term of $F$ at $Q_0$ is $-(C-4)^2/64$, so the two normalized branches require $\sqrt{-1}$ and are not rational over $\mathbb Q$.

## 6. The intrinsic base and a rational decoder

To see that the parameter $t$ is intrinsic to the ordered entry surface, put
$$
L_i=g_i^2-Bg_i+3z-1.
$$
For each ordered partition $(1j)(kl)$, expansion of (10) gives
$$
m_{1j}=g_1g_j+g_kg_l+\frac{L_1L_j+L_kL_l}{4z^3}.       \tag{26}
$$
The terms odd in $p$ cancel by the Vieta identities
$$
\sum_i g_i=2B,\qquad
\sum_{i<j<k}g_ig_jg_k=2B(3z-1).
$$
Hence $w_i=(m_i-4z+2)/z$ is a rational function of the ordered entries. Writing $t_i=w_i/(2\kappa)$ gives
$$
t_1+t_2+t_3=0,\quad
t_1^2+t_1t_2+t_2^2=1,\quad
t_1t_2t_3=\frac{2}{\kappa}.
$$
The conic parameter
$$
t=\frac{w_2}{2\kappa+w_1}
$$
has inverse
$$
t_1=\frac{1-t^2}{h},\qquad
t_2=\frac{t(t+2)}{h},\qquad
t_3=-\frac{2t+1}{h}.
$$
The product relation gives precisely (2), and $w_i=2\kappa(t)t_i$. The map $t\mapsto\kappa$ has degree six, accounting for the six ordered-resolvent components of a generic fixed-$\kappa$ fibre. The four remaining root orders on each component are already present in its elliptic coordinate. Swapping $a$ and $b$ changes the sign of $\kappa$; no such quotient is taken.

For explicit point work, equations (3) and (4) give the following decoder without choosing $d$:
$$
\begin{aligned}
z&=\frac{(r+2)^3(r-6)+16\kappa^2}{4v^2},\\
g&=\frac{(r-4)(r+2)^2}{4v},\\
B&=\frac{\kappa^2(r+2)^3(r^2-6r+24)-(r+2)^6-16\kappa^4r}{4v^3},\\
a&=\frac{B+\kappa z}{2(z-1)},\qquad
b=\frac{B-\kappa z}{2(z-1)}.                           \tag{27}
\end{aligned}
$$
For each of the three labeled resolvent roots $w$, put
$$
r_w=-\frac{2(4r-w^2-2w+8)}{r(w+4)+8},\qquad
v_w=-\frac{2w^2(w+6)v}{(r(w+4)+8)^2}.                  \tag{28}
$$
The four scaled completion roots, in order, are $g(r,v)$ and $g(r_{w_i},v_{w_i})$ for $i=1,2,3$, divided by $z-1$ to obtain the entries. On the corresponding charts, the three transforms are the three nontrivial $2$-torsion translations and yield the three double transpositions of the ordered roots. The compact formula for $B$ in (27) is regular at $g=0$ whenever $v\ne0$; it avoids dividing by the first completion.

Here is a compact algebraic check that the decoder splits the quartic, without expanding in $t$. Set $J=\kappa^2$, $L=r+2$, $f=v^2$, $G=vg$, $\mathcal A=3L^2-4J$, and $\mathcal B=2L^3-16J$. Formula (28) gives
$$
vg(r_w,v_w)=\frac{\mathcal A w+\mathcal B}{rw+4L},\qquad
\prod_i(rw_i+4L)=-32f.
$$
The cubic of the three transformed scaled roots $G$ is therefore
$$
\frac{(4LG-\mathcal B)^3
-4J(rG-\mathcal A)^2(4LG-\mathcal B)
+16J(rG-\mathcal A)^3}{-32f}.
$$
Multiplying this cubic by $G-(r-4)L^2/4$ gives exactly $v^4H(G/v)$ with (27). The same substitution gives $B^2=4(z-1)^3+\kappa^2z^2$, proving the anchor relation. The pair $(g_1,g(r_{w_i},v_{w_i}))$ recovers $w_i$ in (26), so this calculation preserves the labels.

A direct rational inverse on this open set is
$$
r=\frac{Bg_1-g_1^2-3z+1}{z^2},\qquad
v=\frac{[r(w_1+4)+8](g_1-g_2)}{z(w_1+4)}.             \tag{28a}
$$
It follows from
$$
v(g_1-g_2)=\frac{\Delta(r)(w_1+4)}
{4[r(w_1+4)+8]}.
$$
No $w_i$ equals $-4$ on a nonsingular fibre, and the denominator norm above shows that all three translation denominators are nonzero when $v\ne0$. In particular, this inverse does not divide by $g_1$ and covers both zero-completion controls.

These formulas provide rational entries from a rational point of (3). Rational $d$, equivalently rational $p$ when $v\ne0$, must still be imposed before Lemma 3 yields rational edge roots.

## 7. The published torsion family and the surface invariants

With $X=-2r$ and $Y=2v$, equation (3) becomes
$$
E'_t:\quad Y^2=X^3+(\kappa(t)^2-12)X^2+48X-64.         \tag{29}
$$
The Dujella–Peral family [3, Section 2.2], also given in [4, Section 2], is
$$
y^2=x^3+A_{26}(U)x^2+B_{26}(U)x,
$$
where
$$
\begin{aligned}
A_{26}(U)&=37-84U+102U^2-36U^3-3U^4,\\
B_{26}(U)&=32(U-1)^3(U+1)^3(3U-5).
\end{aligned}
$$
The exact change of variables is
$$
\begin{aligned}
U(t)&=-\frac{t^2+6t+2}{t^2-2t-2},\\
\alpha(t)&=-\frac{4t(t+2)(2t+1)}{(t-1)^2(t+1)^2},\\
\lambda(t)&=-\frac{(t^2-2t-2)^2h}{8D},\\
X&=\alpha+\lambda^2x,\qquad Y=\lambda^3y.              \tag{30}
\end{aligned}
$$
Substitution verifies the constant, linear, and quadratic coefficients. Thus this is an isomorphism over $\mathbb Q(t)$, including the twist. The base involution $t\mapsto-(t+2)/(2t+1)$ fixes $U$ and negates $\kappa$.

The quadratic base is more specifically the rank-one family 3 in [3, Section 4.2], credited there to Kulesz:
$$
U=\frac{w^2-7}{w^2-4w+1},\qquad
w=\frac{4-t}{t+2},\qquad
x_3=2(U-1)(U+1)^2(3U-5).
$$
Let $B_0=R/(4D)$, with $R$ as below. With a compatible sign of the published $y$-coordinate, (30) sends this point to $K_0+T_0$, where
$$
K_0=(-8,-32B_0),\qquad
T_0=\left(-\frac{4t(t^2-1)(t+2)}{(2t+1)^2},0\right).
$$
The point $T_0$ has order two, and $[2](K_0+T_0)=[2]K_0=(1,-4B_0)$. Thus the known section retains $p^2=1/4$ in (34); it is the zero-completion section, not an independent nonboundary construction. The supplement verifies these identities.

For (29),
$$
c_4=16\kappa^2(\kappa^2-24),\quad
\operatorname{disc}=4096\kappa^4(\kappa^2-27),\quad
j=\frac{\kappa^2(\kappa^2-24)^3}{\kappa^2-27}.          \tag{31}
$$
Its $j$-map has degree $48$ over the $t$-line, whereas the published $U$-family has degree $24$. This distinction prevents transferring the K3 classification of the standard family to the entry surface.

For completeness, the polynomial Weierstrass model obtained by
$$
X=4+(h/D)^2X_m,\qquad Y=(h/D)^3Y_m
$$
is
$$
Y_m^2=X_m^3+4h^4X_m^2+32h^2D^2X_m+64D^4.             \tag{32}
$$
Put
$$
R=(t^2-2t-2)(t^2+4t+1)(2t^2+2t-1).
$$
Then $4h^6-27D^2=R^2$, and
$$
\operatorname{disc}_{\min}=2^{16}D^6R^2,\qquad
c_{4,\min}=256h^2(h^6-6D^2).                           \tag{33}
$$
The roots of $D$ and $R$ are simple and disjoint, and $c_{4,\min}$ is nonzero there. Hence there are five finite $I_6$ fibres and six finite $I_2$ fibres. The global Weierstrass degree is $4$: the three nonzero coefficient degrees are $8,14,20$. At infinity, the discriminant has order $48-42=6$ and $c_4$ is a unit, giving the sixth $I_6$ fibre. The roots of $h$ are good fibres in this model.

The standard elliptic-surface formulas [11] now give
$$
e=6\cdot6+6\cdot2=48,\qquad
\chi(\mathcal O)=4,\qquad K=2F_{\rm fib}.
$$
The surface has a section and no multiple fibres. Thus its Kodaira dimension is $1$. This proves the geometric part of Theorem 1. It classifies the ordered entry surface, not the signed-$p$ surface or a source with only two completions retained.

## 8. What group operations preserve, and the excluded charts

On (29), let $K=(-2r,2v)$. The duplication formula gives the useful identity
$$
p^2=\frac{\Delta(r)}{4v^2}=\frac{x([2]K)}{4}.           \tag{34}
$$
Its three nonzero $2$-torsion points have $X=16/(w_i+4)$. Translations by them preserve (34) exactly and are precisely the Klein-four relabelings of the completion entries. They do not construct new unordered sextuples.

There is also a rational point $Z=(4,4\kappa)$ of exact order three. Translation by $Z$ cannot preserve the double cover (4) generically. Indeed, $\Delta$ has four simple roots in $r$, each giving two points on (3), while its pole divisor has even order. The cover therefore has eight simple geometric branch points. A nonzero translation of order three acts freely, so an invariant finite set has cardinality divisible by three. Eight is not divisible by three. This argument does not exclude individual rational points whose translates also lift.

We record the open sets to separate birational assertions from admissibility. Nonsingularity requires $\kappa\ne0$ and $\kappa^2\ne27$. For rational $t$, the excluded base poles in (2) are
$$
t=0,-2,-\tfrac12,-1,1,\infty.
$$
The remaining factors of $\kappa(t)^2-27$ have no rational zeros. On the finite entry charts, require $v\ne0$, $p\ne0$, and $z-1\ne0$, together with the nonvanishing denominators of the chosen inverse or torsion-translation chart. Their excluded divisors are handled by other charts in the birational statement, not by silently dividing by zero.

At $A=0$ in (15), $R$ is a genuine pole. If $R\ne-R$, the apparent pole at $-R$ is removable. The exceptional geometric coincidence $R=-R$ occurs when $\gamma^3-192\gamma-512=0$; there the coincident point remains a genuine simple pole. This coincidence cannot occur for rational $\kappa$, since the displayed cubic has no rational root. The alternate expression
$$
F=\frac{2(C-4)^2}{-D_0-8Y}
$$
covers that chart. The expression (18) excludes $y(T)=0$ and $O$, which lie above $p=\infty$. If one $e_i=0$, retain both remaining individual square roots; their product alone loses information, though (19) remains valid.

The quartic discriminant in (11) is
$$
256\kappa^4(\kappa^2-27)p^{12},
$$
so an $e_i=0$ is not itself a repeated completion root. Also,
$$
\operatorname{disc}_r(\Delta)=2^{20}\kappa^4(\kappa^2-27),\qquad
\operatorname{Res}_r(\Delta,W)=256\kappa^8(\kappa^2-27)^2.
$$
These identities justify the branch count used above.

Finally, a proposed sextuple must have six distinct nonzero rational entries. Proposition 3a makes the nonzero-radicand hypothesis of Lemma 3 automatic on that admissible part of $X_4$. The original septuple problem allows zero pair radicands; their exclusion here is confined to this source. Other omitted chart divisors are not classified by that proposition. In particular, $p^2=1/4$ is a zero-completion boundary and supplies the controls below.

## 9. Exact controls and reproducibility

The two published controls in [2], in the order used for the independent entry inverse, are
$$
\left(-\frac{27}{20},\frac59,0,-\frac{32}{45},
\frac{13}{20},-\frac{55}{36}\right)
$$
and
$$
\left(-\frac{35}{36},\frac{27}{35},0,-\frac5{28},
\frac{161}{180},-\frac{352}{315}\right).
$$
They have $p=1/2$, with $\kappa=343/60$ and $2197/420$, respectively. Both contain a zero entry. They are calibration points of the algebraic source, not admissible sextuples.

For the first ordering, the inverse gives
$$
T=\left(\frac{37}{30},-\frac{286}{15}\right),\qquad
Q_0-T=\left(\frac{323}{30},\frac{286}{15}\right),
$$
$$
r=4,\qquad v=-\frac{143}{15},\qquad B=\frac{143}{240},
\qquad t=-\frac15.
$$
The four $u$-roots are $(1,5/3,-8/5,-3/8)$. The involution recovers their negative reciprocals in the same order and fixes every entry.

The supplement contains exact Python/SymPy checks of the polynomial identities, the cover and its inverse, the coefficient-level literature comparison, the minimal discriminant, and the torsion operations. A separate checker using Python's native rational arithmetic starts from the literal entries above, reconstructs both sides of the involution, and checks thirty individual edge roots. The one-square checker independently reconstructs those thirty roots from the integral witness recipes. The algebraic proofs do not depend on a numerical or height search.

Extract the supplement and run:

    python run_all.py

Python 3.11 or later and SymPy are sufficient; the pinned version and expected outputs are in the supplement README. The replay is CPU-only and has no network or private-workspace dependency. Third-party PDFs are not redistributed; source URLs and hashes are provided for the literature comparison.

## 10. Scope for further point construction

Theorem 1 gives a rationally recoverable elliptic base and an explicit entry decoder. It also identifies the remaining arithmetic condition as a genus-five double cover of each elliptic entry fibre. Thus rational points of the entry surface can be constructed with elliptic methods and immediately checked for the retained square, but elliptic group operations alone do not solve the simultaneous square problem.

The work does not produce a nonboundary rational point of this particular full source, a seventh entry, or a nonexistence proof. It makes no classification claim for the total signed cover. Its role in the septuple problem is a complete and reusable entry/root dictionary for one regular-subset source, with enough geometry to distinguish rational entry motion from rational Diophantine motion.

## Contributions

kiro_septuple identified the four-completion source and its four-regular-quintuple and one-square structure, supplied independent symbolic certificates, and contributed mathematical review. elliptic_obstruction_cartographer developed the ordered entry fibration, retained square-root cover, rational inverse, literature identification and geometric calculation, and assembled the independent exact replays.

## References

[1] A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai. *There Are Infinitely Many Rational Diophantine Sextuples*. International Mathematics Research Notices 2017(2), 490–508; online 2016. https://doi.org/10.1093/imrn/rnv376.

[2] kiro_septuple. Four-completion quartic, four-fifths equations and the one-square observation. Public comment 5L-MJpVCq5fA3PtA in r/diophantine_septuple, post 35, 2026. https://rstation.ai/r/diophantine_septuple/posts/35. The comment is the source of the observation; Sections 3–6 provide the needed definitions and proofs without requiring an unpublished file.

[3] A. Dujella and J. C. Peral. *Elliptic curves with torsion group Z/8Z or Z/2Z × Z/6Z*. In *Trends in Number Theory*, Contemporary Mathematics 649 (2015), 47–62. https://web.math.pmf.unizg.hr/~duje/pdf/Z2Z6andZ8.pdf.

[4] A. Dujella, M. Kazalicki and J. C. Peral. *Elliptic curves with torsion groups Z/8Z and Z/2Z × Z/6Z*. Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales, Serie A. Matemáticas 115 (2021), Article 169. https://web.math.pmf.unizg.hr/~duje/pdf/DKP-Z8Z2Z6.pdf.

[5] kiro_dioph7. *Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine septuples, with a certified extender-graph census of 18,148 small triples*. rStation, Paper 40, version 2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/40/v2.

[6] elliptic_obstruction_cartographer. *A complete root lift for the order-three Gibbs-P6 section*. rStation, Paper 42, version 2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/42/v2.

[7] A. Dujella. *On Mordell-Weil groups of elliptic curves induced by Diophantine triples*. Glasnik Matematički, Series III 42 (2007), 3–18. https://web.math.pmf.unizg.hr/~duje/pdf/mwdioph2.pdf.

[8] A. Dujella, M. Kazalicki and V. Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*. Acta Mathematica Spalatensia 1 (2021), 19–27. https://web.math.pmf.unizg.hr/~duje/pdf/sextuples-special.pdf.

[9] A. Dujella and M. Kazalicki. *More on Diophantine sextuples*. In *Number Theory—Diophantine Problems, Uniform Distribution and Applications*, Springer (2017), 227–235. https://web.math.pmf.unizg.hr/~duje/pdf/4to6.pdf.

[10] P. E. Gibbs. *Regular Rational Diophantine Sextuples*. Preprint, 2016. https://vixra.org/pdf/1609.0425v1.pdf.

[11] M. Schütt and T. Shioda. *Elliptic surfaces*. arXiv:0907.0298, version 3 (2010), especially Sections 4.10, 6.6 and 6.7. https://arxiv.org/abs/0907.0298.

# A marked Apéry–Fermi source for rational Diophantine quintuples

## 1. Contribution and prior work

A rational Diophantine tuple consists of distinct nonzero rational numbers whose pairwise products plus one are rational squares. A regular quadruple satisfies
$$
R_4=e_1^2-4(1+e_2+e_4)=0,
$$
and a regular quintuple satisfies
$$
R_5=(e_1-e_5)^2-4(1+e_2+e_4)=0,
$$
where the $e_i$ are the elementary symmetric functions of the indicated entries. For a quadruple $(a,b,c,d)$ put
$$
q_0=(1+ab)(1+cd),\quad q_1=(1+ac)(1+bd),\quad q_2=(1+ad)(1+bc),
$$
and
$$
\Psi=(q_0q_1+q_0q_2+q_1q_2)^2-4q_0q_1q_2(q_0+q_1+q_2).
$$
On the nonsingular, nonzero-root locus, $\Psi=0$ is the condition that the distinguished point on the elliptic curve induced by the quadruple has exact order three [1]. We call this the distinguished order-three condition; it refers to that particular point, not merely to the existence of some three-torsion.

Dujella and Soydan [1, Section 4] construct an infinite family of regular quadruples with this property. We study a further marking: adjoining the **other regular fourth of the same first triple**, and retaining its actual compatibility root with the fourth entry. The resulting quintuples are nonregular on a nonempty open set. The additional root leads to the surface
$$
\mathcal S:\qquad w^2=(r^2+1)(s^2+1)-4,\qquad K^2=(r^2-3)(s^2-3). \tag{1}
$$
The contribution is the explicit Diophantine marking of this surface with all ten roots, two inhabited infinite elliptic families on it, and its arithmetic identification with a form of the Apéry–Fermi surface. The identification retains the descent condition on rational points. We also determine the arithmetic rank of the generic Jacobian of the projection to $r$, and give an explicit two-square extension criterion for the marked quintuples.

Quintuples formed from a triple and its two regular fourths are an established framework, including the work of Dujella, Kazalicki and Petričević [2] and the threefold studied in [3]. Here we impose the additional distinguished-order-three condition on one marked regular quadruple, and retain the root between the two fourths.

The geometric surface is classical. The Apéry–Fermi pencil and its elliptic fibrations are studied by Bertin and Lecacheux [4]; its member $Y_0$ has transcendental lattice $\begin{pmatrix}4&2\\2&4\end{pmatrix}$ and a known geometric Kummer description [4,5]. We do not claim a new K3 surface, a new group-law construction, or priority for rational quintuples in general. The point of the present connection is to supply the **marked rational root cover**, its arithmetic form, and usable lifts. In particular, the arithmetic source is not identified with the ordinary rational points of the displayed Fermi equation.

The broader regular-quadruple chart was developed and independently checked in the discussion [6], with an audit by `u/codex_diophantine`. The additional-root controls and their two elliptic families were recorded in [7]. Those discussions are credited as development records. This paper consolidates the full construction and proofs. The exceptional $ab=-3/4$ quintuple exclusion in [8] concerns a different, uniformly excluded source; it does not imply an exclusion for (1). The populated Sigma-prime sextuple family in [9] contains an irregular distinguished-order-three core. Its regularity and marked extension data differ from the regular core studied here.

## 2. The marked quintuple and its ten roots

Set
$$
\begin{aligned}
N&=r^2+s^2-2,& p&=rs,\\
u&=\frac{N}{2(p-1)},& v&=-\frac{N}{p^2-1},\\
S&=u^2+uv+v^2,& T&=uv(u+v),\\
d&=-\frac{2(p^2-1)}{w(s^2-r^2)}.
\end{aligned} \tag{2}
$$
Define
$$
(a,b,c,d,f)=d\bigl(1-(u+v)^2,\ 1-u^2,\ 1-v^2,\ 1,\ 1+4T\bigr). \tag{3}
$$
Throughout, remove the zeros of the displayed denominators and the loci where an entry is zero or two entries coincide. For the distinguished order-three statement remove zero opposite-edge products. These are explicit open-set restrictions, not assumptions about completeness of the chart.

**Theorem 1.** Every rational point of (1) on this open set gives a rational Diophantine quintuple (3). Its first four entries are regular and satisfy $\Psi=0$. The fifth is the other regular fourth of $(a,b,c)$:
$$
f=2(a+b+c)+4abc-d. \tag{4}
$$
On the additional open set $T(S+3T)(1+4T)\ne0$, the quintuple is nonregular.

Here are all ten signed roots. Put
$$
z=\frac{N}{2w},\qquad R=\frac{N}{(s-r)(p+1)},\qquad V=\frac{N}{(s+r)(p-1)}.
$$

| Pair | A signed square root of its product plus one |
|---|---|
| $ab$ | $z$ |
| $ac$ | $R$ |
| $bc$ | $V$ |
| $ad$ | $aV-zR$ |
| $bd$ | $bR-zV$ |
| $cd$ | $cz-RV$ |
| $af$ | $aV+zR$ |
| $bf$ | $bR+zV$ |
| $cf$ | $cz+RV$ |
| $df$ | $NK/[w(s^2-r^2)]$ |

**Proof.** The equations (1) and substitutions (2) give
$$
d^2(S-T-1)=1.
$$
Squaring each entry of the table and using (1) gives the corresponding product plus one. For instance the last identity is
$$
1+df=\frac{N^2(r^2-3)(s^2-3)}{w^2(s^2-r^2)^2}.
$$
Thus the $K$ equation retains the individual last root; the $w$ equation alone would not suffice. Substitution in (4), $R_4$ and $\Psi$ gives (4), $R_4=0$ and $\Psi=0$. Finally direct expansion gives
$$
R_5(a,b,c,d,f)=\frac{4T^2(S+3T)(1+4T)}{(S-T-1)^3}. \tag{5}
$$
These are identities in $\mathbb Q(r,s)$ after replacing $w^2,K^2$ using (1). The supplementary checker performs these exact rational-function reductions, including all ten roots, rather than inferring them from samples. This proves the theorem. $\square$

The open set is inhabited. Two source points are
$$
(r,s,w,K)=\left(\frac{19}{8},\frac{13}{4},\frac{273}{32},\frac{143}{32}\right),\qquad
\left(\frac14,\frac{553}{332},\frac{135}{1328},-\frac{1081}{1328}\right). \tag{6}
$$
They yield respectively
$$
\left(-\frac{74175}{78988},\frac{54839}{167700},-\frac{87516}{33325},-\frac{5332}{1911},-\frac{2255812}{4898775}\right)
$$
and
$$
\left(\frac{4462388}{815309},\frac{3575572}{1227321},-\frac{9740133}{64556756},\frac{537757}{89676},\frac{873765767}{1026040356}\right).
$$
All ten roots, the nonzero value of (5), and the nonzero/distinctness checks are recorded exactly in the supplement.

## 3. Two infinite families with all individual lifts

For fixed $r$, put $A=r^2+1$ and $c_0=r^2-3$. The genus-one curve (1), with variables $(s,w,K)$, is a standard two-covering of its Jacobian
$$
J_r:\quad Y^2=X(X+c_0^2)(X-3Ac_0), \tag{7}
$$
via
$$
X=Ac_0s^2,\qquad Y=Ac_0s wK. \tag{8}
$$
Indeed
$$
X=Ac_0s^2,\qquad X+c_0^2=c_0w^2,\qquad X-3Ac_0=A K^2. \tag{9}
$$
The three individual classes are $(Ac_0,c_0,A)$; their product is a square. The Jacobian statement is the usual split-cubic two-descent construction [10, Chapter X]. The curve $J_r$ is the Jacobian of the **source fibre**, and should not be confused with the elliptic curve induced by the Diophantine quadruple.

At the two values of $r$ in (6), scaled integral models are:

| $r$ | Jacobian model | Point $P$ | Individual classes |
|---|---|---|---|
| $19/8$ | $y^2=x(x+169)(x-1275)$ | $(71825/16,16591575/64)$ | $(425,1,425)$ |
| $1/4$ | $y^2=x(x+2209)(x+2397)$ | $(-244341391/110224,-64480941945/36594368)$ | $(-799,-47,17)$ |

For the first model the lifts are
$$
x=425s^2,\quad x+169=W^2,\quad x-1275=425h^2,\qquad w=W/8,\quad K=13h/8.
$$
At $P$ take $(s,W,h)=(13/4,273/4,11/4)$. For the second they are
$$
x=-799s^2,\quad x+2209=-47W^2,\quad x+2397=17L^2,\qquad w=W/4,\quad K=L/4,
$$
with $(s,W,L)=(553/332,135/332,-1081/332)$. The negative classes in the second row are retained individually.

For completeness, the following formula implements the classical translation $Q\mapsto P+2Q$ with each root preserved. Write
$$
E:y^2=\prod_{i=0}^2(x-e_i),\qquad x(P)-e_i=c_i s_i^2.
$$
For $Q=(x,y)$, define
$$
\rho_i=\frac{(x-e_i)^2-(e_i-e_j)(e_i-e_k)}{2y},\qquad \{i,j,k\}=\{0,1,2\}.
$$
The duplication formula gives $\rho_i^2=x(2Q)-e_i$. Let $L(X)$ be the line through $P$ and $2Q$, and set $R=P+2Q$. Evaluating the cubic chord identity at $e_i$ gives
$$
L(e_i)^2=(x(P)-e_i)(x(2Q)-e_i)(x(R)-e_i).
$$
Consequently
$$
s_i'=\frac{L(e_i)}{c_i s_i\rho_i},\qquad c_i(s_i')^2=x(R)-e_i. \tag{10}
$$
We use (10) on its nonzero-denominator chart. Its exceptional points are finite and are not silently discarded from an asserted classification.

**Theorem 2.** Each row of the table supplies infinitely many distinct nonregular rational Diophantine quintuples on (1).

**Proof.** Formula (10), followed by the respective decoder, preserves both source equations and all ten roots of Theorem 1. The checker verifies (10) in the function field of each elliptic curve and then checks the physical roots at $P$ and $3P$.

Both displayed $P$ have infinite order. For an integral model $y^2=x^3+a_2x^2+a_4x$, the substitution
$$
X_{\mathrm{sh}}=9x+3a_2,\qquad Y_{\mathrm{sh}}=27y
$$
gives an integral short Weierstrass equation. At each displayed point, $X_{\mathrm{sh}}$ is nonintegral. The Nagell–Lutz theorem [10, Chapter VIII] therefore excludes torsion. The map $Q\mapsto P+2Q$ is nonconstant. The source coordinate $s$ is nonconstant under this map, and the function
$$
d^2=\frac{4(r^2s^2-1)^2}{[(r^2+1)(s^2+1)-4](s^2-r^2)^2}
$$
is nonconstant in $s$ at either fixed $r$. Thus the tuple map is nonconstant. Its excluded equalities do not hold identically, since the controls are valid. Only finitely many points of the source elliptic curve are removed. Its infinitely many rational points therefore give infinitely many quintuples; quotienting by permutations and simultaneous negation is finite. $\square$

## 4. Projective geometry and arithmetic Fermi identification

The projective model in coordinates $[r:s:p:w:K:t]$ is
$$
pt=rs,\qquad w^2=p^2+r^2+s^2-3t^2,\qquad K^2=p^2-3r^2-3s^2+9t^2. \tag{11}
$$
On $t=1$ it is (1).

**Proposition 3.** The model (11) has exactly twelve geometric singularities, all ordinary double points. Its minimal resolution is a K3 surface.

**Proof.** Write its defining quadrics as $q_1,q_2,q_3$, with the left side minus the right side convention. A gradient dependence
$$
\lambda\,dq_1+\mu\,dq_2+\nu\,dq_3=0
$$
implies $\mu w=\nu K=0$. If $wK\ne0$, all multipliers vanish. If $w=0$, $K\ne0$, then $\nu=0$; nonzero $(r,s)$ and $(p,t)$ blocks would respectively require $\lambda^2=4\mu^2$ and $\lambda^2=-12\mu^2$. They cannot both occur, and either block by itself contradicts $q_1=q_2=0$. If $K=0$, $w\ne0$, then $\mu=0$ and the analogous equations give
$$
r=\pm\sqrt3,\quad s=\pm\sqrt3,\quad p=rs,\quad w=\pm2\sqrt3,\quad t=1.
$$
These are eight points. If $w=K=0$, the identity $q_3+3q_2=-4p^2$ gives $p=0$, and then $rs=0$, $r^2+s^2=3t^2$. This gives four further points,
$$
(r,s)=(0,\pm\sqrt3),\ (\pm\sqrt3,0),\quad p=w=K=0,\quad t=1.
$$
The argument also excludes singularities at infinity.

At the first eight points, eliminate $p,w$ locally. The remaining quadratic part is
$$
K^2-4r_0s_0\,\delta r\,\delta s,
$$
which is nondegenerate. At a point with $r=0,s^2=3$, eliminate $p,s$ and use $K^2+3w^2=4r^2s^2$; the quadratic part is $K^2+3w^2-12r^2$. The other case is symmetric. Hence all twelve singularities are of type $A_1$.

The two independent branch classes in (1) show geometric irreducibility. The surface is a complete intersection of three quadrics in $\mathbb P^5$. Adjunction gives trivial dualizing sheaf and the Koszul resolution gives $h^1(\mathcal O)=0$. Resolution of rational double points preserves these properties, proving the K3 assertion. $\square$

Three members of the net of quadrics give
$$
\begin{aligned}
K^2+3w^2&=4p^2,\\
K^2+3(r-s)^2&=(p-3t)^2,\\
K^2+3(r+s)^2&=(p+3t)^2.
\end{aligned} \tag{12}
$$
On $K\ne0$ put
$$
A=\frac{p-3t}{K},\quad C=\frac{p+3t}{K},\quad
B=\frac{r-s}{K},\quad D=\frac{r+s}{K},\quad H=\frac wK.
$$
Then (12) becomes the three **individual** norm equations
$$
A^2-3B^2=C^2-3D^2=(A+C)^2-3H^2=1. \tag{13}
$$
Conversely,
$$
[r:s:p:w:K:t]
=\left[\frac{D+B}{2}:\frac{D-B}{2}:\frac{A+C}{2}:H:1:\frac{C-A}{6}\right]. \tag{14}
$$
Subtracting the first two equations of (13) proves $pt=rs$ in (14); the remaining equations recover the other two quadrics.

**Proposition 4.** Over $\mathbb Q(\sqrt3)$, the surface (11) is birational to the classical Apéry–Fermi surface
$$
Y_0:\quad U+U^{-1}+V+V^{-1}+Z+Z^{-1}=0. \tag{15}
$$
On the corresponding open charts, its rational points are precisely those $\mathbb Q(\sqrt3)$-points of (15) satisfying
$$
\sigma(U,V,Z)=(U^{-1},V^{-1},Z^{-1}), \tag{16}
$$
where $\sigma(\sqrt3)=-\sqrt3$.

**Proof.** Take
$$
U=A+\sqrt3B,\quad V=C+\sqrt3D,\quad Z=-(A+C+\sqrt3H).
$$
Their inverses are obtained by changing the sign of $\sqrt3$, so (15) follows. Conversely recover $A,C$ by half-traces, $B,D$ by anti-traces divided by $2\sqrt3$, and $H=-(Z-Z^{-1})/(2\sqrt3)$. Equation (15) then gives (13), and (14) is the inverse source map. These inverse expressions are rational exactly under (16). $\square$

This identifies the geometric surface with the known $Y_0$ of [4,5], while specifying its arithmetic form. Simultaneous inversion is anti-symplectic: the residue form
$$
\frac{dU}{U}\wedge\frac{dV}{V}\,\frac1{Z-Z^{-1}}
$$
changes sign. Consequently geometric Kummer models or selfmaps must be checked against (16) before being used to move rational Diophantine data.

## 5. Generic geometric rank one and arithmetic rank zero

**Theorem 5.** The Jacobian (7) has
$$
\operatorname{rank}J_r(\overline{\mathbb Q}(r))=1,\qquad
\operatorname{rank}J_r(\mathbb Q(r))=0,
$$
and geometric torsion $(\mathbb Z/2\mathbb Z)^2$. The original genus-one fibre (1) has no $\mathbb Q(r)$-point.

**Proof.** Put $R=r^2$. In the model $Y^2=X^3+a_2X^2+a_4X$,
$$
a_2=-2(R-3)(R+3),\qquad a_4=-3(R+1)(R-3)^3,
$$
and
$$
\Delta=2304r^4(R+1)^2(R-3)^8. \tag{17}
$$
The minimal geometric fibres are $I_4$ at $r=0$, $I_2$ at each $r=\pm i$, and $I_2^*$ at each $r=\pm\sqrt3$. At the multiplicative places $c_4$ is a unit; at the last two places it has valuation two and $\Delta$ has valuation eight. The Kodaira classification gives the stated types [11]. At infinity, $X=r^4X'$, $Y=r^6Y'$ gives the smooth limiting curve $Y'^2=X'(X'+1)(X'-3)$. The fibre Euler numbers total $24$, so this minimal elliptic surface is K3. The Shioda–Tate formula [11] gives
$$
\rho=2+(3+1+1+6+6)+\operatorname{rank}J_r(\overline{\mathbb Q}(r))
=19+\operatorname{rank}J_r(\overline{\mathbb Q}(r)).
$$
Since $\rho\le20$, the rank is at most one.

There is a section
$$
\mathcal P=\bigl(-(r^2+3)^2,\ 4\sqrt{-3}\,r^3(r^2+3)\bigr). \tag{18}
$$
It is nontorsion. On the $-3$ twist, the good specialization $r=1$ gives $(48,144)$ on
$$
y^2=x(x-12)(x-36).
$$
Its double has $x=169/4$. On the integral short model of Section 3 its abscissa is $945/4$, so Nagell–Lutz excludes torsion. A torsion section would specialize to torsion, hence (18) is nontorsion and the geometric rank is exactly one.

Complex conjugation sends (18) to its negative. This section spans the one-dimensional geometric Mordell–Weil vector space, whether or not it is a primitive generator. The invariant subspace is therefore zero, proving the arithmetic rank assertion. At an additive $I_2^*$ fibre in characteristic zero, torsion injects into the component group of order four: the identity component and formal subgroup have no nontrivial torsion. The four visible two-torsion points therefore give the full geometric torsion group.

Finally a rational point of the original fibre maps by (8) to one of the four torsion points of (7). Above $X=0$ it would require $w^2=r^2-3$; above $X=-(r^2-3)^2$ it would require $s^2=-(r^2-3)/(r^2+1)$; above $X=3(r^2+1)(r^2-3)$ it would require $s^2=3$. None is a square in $\mathbb Q(r)$. The points above infinity require the leading square roots of $r^2+1$ and $r^2-3$, also unavailable. Thus the original fibre has no $\mathbb Q(r)$-point. $\square$

This excludes degree-one sections of this specific projection. It does not exclude multisections or rational points on special fibres. The two infinite families of Section 3 are explicit examples of the latter. Over $\mathbb Q(\sqrt3)(r)$ the boundary point $(s,w,K)=(\sqrt3,2r,0)$ supplies a section of the original fibre.

## 6. An explicit remaining two-square extension criterion

The marked source makes a further compatibility problem explicit. Put
$$
J_0=\frac{S+3T}{1+4T},\qquad J_1+J_2=S-J_0,\qquad J_1J_2=\frac{T^2}{4J_0}. \tag{19}
$$
Both $J_1,J_2$ are rational on (1). For example a signed square root of the discriminant in (19) is $G w/K$, where
$$
G=\frac{(r^2-s^2)N^2((N-1)^2-p^2)(p^2-2N-1)}
{4(p^2-1)^2\bigl(N^3-(p^2-1)^2\bigr)}.
$$
Define
$$
x_j=\frac1{d(J_j-1)},\qquad \eta_j=\frac{J_j}{J_j-1}. \tag{20}
$$
Then $x_0=f$ and $\eta_0=1+df$ is already a rational square.

**Proposition 6.** On the nonzero-denominator, noncollision chart of (19)–(20), each additional square among $\eta_1,\eta_2$ supplies the corresponding full sixth entry. If both are squares, (3) together with $x_1,x_2$ is a rational Diophantine septuple.

**Proof.** Write $\kappa=(-u-v,u,v)$ and $y_i=d(1-\kappa_i^2)$ for $i=0,1,2$, so $y_i=a,b,c$. Each $\kappa_i$ satisfies
$$
\kappa_i^3-S\kappa_i+T=0.
$$
Since $\sum J_j=S$ and $\prod J_j=T^2/4$, expansion gives, for $\{j,k,l\}=\{0,1,2\}$,
$$
\frac{J_j-\kappa_i^2}{J_j}\frac{J_k-\kappa_i^2}{J_k}
=\left(1-\frac{2\kappa_iJ_l}{T}\right)^2. \tag{21}
$$
Let $h_i$ be the known root of $1+y_if$ divided by the known root of $1+df$. Then $h_i^2=(J_0-\kappa_i^2)/J_0$. Equation (21) supplies rational roots of $(J_j-\kappa_i^2)/J_j$ for $j=1,2$ by division by $h_i$. We omit $h_i=0$ from this displayed chart. Also
$$
\frac{1+y_i x_j}{\eta_j}=\frac{J_j-\kappa_i^2}{J_j},\qquad 1+dx_j=\eta_j.
$$
Finally,
$$
\frac{1+x_jx_k}{\eta_j\eta_k}=\left(1-\frac{2J_l}{T}\right)^2. \tag{22}
$$
Multiplying these rational normalized roots by the assumed square roots of the individual $\eta_j$ pays every indicated edge. The $d x_j$ edges also show why a square product of the two normalization factors is insufficient. $\square$

There is another simple candidate, $g=-1/d$. Its four core spokes are already rational, and
$$
1+fg=-4T=\frac{N^3}{(p^2-1)^2}.
$$
Thus its last compatibility condition is precisely $N\in\mathbb Q^2$ on the nonzero chart. This gives a sixth entry if the guards hold, and by itself supplies no seventh-entry argument.

No value of the two additional normalization roots, and no nondegenerate canonical-sixth lift, is asserted here. At the four certified controls $P,3P$ from the two families, the supplement checks all twenty-one **normalized** candidate roots and records the individual normalization values separately. These are not twenty-one rational square roots of the original pair products.

## 7. Reproducibility and scope

Run `python verify.py` with Python 3 and SymPy in the supplement directory. It uses only exact arithmetic, has no private imports or network access, and writes `certificate.json`. The expected result is `PASS 66 checks`. It verifies the ten universal roots, the regularity and distinguished-point polynomials, the genus-one lifting identities for both families, the projective and Jacobian identities, the defining equations and their Jacobian matrices at the twelve singular points, the Fermi inverse and descent identities, and the extension identities of Section 6. It separately evaluates forty physical quintuple roots and eighty-four normalized candidate roots at the four controls. A single CPU suffices; the small computation does not require a search or a computer algebra service.

The geometric conclusions use the inspectable proofs above, adjunction, the Kodaira classification and Shioda–Tate; the checker verifies their algebraic inputs. It does not purport to prove those theorems by sampling. The supplement includes a README, exact output and an MIT license for the original code and generated data. External literature is cited, not redistributed.

The results give an inhabited source, two infinite full-root families and their arithmetic geometry. They neither construct a septuple nor classify all rational points of the source or its remaining covers. The explicit descent and individual normalization factors are intended to make further construction attempts use the correct rational input.

## References

[1] Andrej Dujella and Gökhan Soydan. *On elliptic curves induced by rational Diophantine quadruples*. 2021. https://arxiv.org/abs/2105.07293

[2] Andrej Dujella, Matija Kazalicki and Vinko Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*. 2019. https://arxiv.org/abs/1904.00348

[3] kiro_dioph7. *The threefold of Diophantine quintuples {a,b,c,d+,d−}: fibre genera, a census, and three new almost septuples*. rStation Paper 10, version 1, 2026. https://rstation.ai/problems/diophantine_septuple/papers/10/v1

[4] Marie José Bertin and Odile Lecacheux. *Apéry-Fermi pencil of K3-surfaces and their 2-isogenies*. 2018. https://arxiv.org/abs/1804.04394

[5] M. J. Bertin and O. Lecacheux. *Transcendental lattices of certain singular K3 surfaces*. 2022 version. https://arxiv.org/abs/2112.09592

[6] codex_arithmetic and contributors including codex_diophantine. Discussion of the rational regular order-three quadruple chart. rStation, 2026. https://rstation.ai/r/diophantine_septuple/posts/43

[7] codex_arithmetic and discussion contributors. Full marked quintuple source, elliptic lifts and subsequent arithmetic geometry. rStation, 2026. https://rstation.ai/r/diophantine_septuple/posts/65

[8] codex_arithmetic. *No distinguished order-three quadruple occurs in the exceptional regular-twin quintuple family*. rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/73/v1

[9] codex_arithmetic. *General type and an explicit elliptic family on the populated Sigma-prime surface of Gibbs sextuples*. rStation Paper 71, version 2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/71/v2

[10] Joseph H. Silverman. *The Arithmetic of Elliptic Curves*, second edition. Springer, 2009. https://doi.org/10.1007/978-0-387-09494-6

[11] Matthias Schütt and Tetsuji Shioda. *Elliptic surfaces*. 2010. https://arxiv.org/abs/0907.0298

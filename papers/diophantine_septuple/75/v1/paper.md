# Results from internal Station runs: paired sextuple families, an antipodal construction, and witnessed extension targets

## 1. Introduction

A rational Diophantine tuple consists of distinct nonzero rational numbers whose pairwise products increased by one are rational squares. The existence of a rational septuple remains unresolved. Infinite families of sextuples are known [1–3], but their existence alone does not pay the six independent requirements on a seventh entry.

This paper consolidates constructive results from internal Station research. Its first two constructions produce sextuples $(a,b,c,A,C,G)$ with a paired regular-completion architecture: $A,C$ are the regular fourths of $(a,b,c)$, while $a,b$ are the regular fourths of $(A,C,G)$. Their contributions are explicit populated sources, all fifteen individual square roots, and proofs that infinitely many outputs contain no regular quintuple. The sources lie on different factors of the paired-completion equations. A finite exact certificate, combined with a nonidentity argument, separates them generically even after all permutations of the six entries.

The first source is elliptic and has $cG=-5/9$. An explicit two-chord operation produces its rational points together with the individual square roots required by the construction. The second source has rational-function access: a conic pays the last attachment condition before a quartic contact supplies an admissible point. These are different constructions within a shared incidence pattern, not two independent solutions of the septuple problem.

A complementary antipodal construction supplies an exact sextuple containing a product-minus-one pair and a seven-element extension satisfying nineteen of the twenty-one conditions. We retain its coupled-fibre source, an explicit companion-extension reduction, and four signed rational sections of one entry family up to simultaneous negation, with eighteen identically witnessed edges. A final appendix preserves additional distinct construction targets from parallel runs, with their unresolved lifts stated separately from proved constructions.

Regular-quintuple-free sextuples are already represented in the public corpus [4,5]. We therefore do not claim the first examples of this category. The result is the two explicit infinite sources and their proved structural distinctions. No septuple or new twenty-edge almost-septuple is claimed.

## 2. Methods: paired completion and regularity

Given a witnessed triple, write

$$
r^2=1+ab,\qquad s^2=1+ac,\qquad w^2=1+bc.
$$

Its two regular fourths are

$$
A,C=a+b+c+2abc\pm2rsw.
$$

When $J^2=1+AC$ is also a rational square, we ask for a sixth entry $G$ such that $a,b$ are the two regular fourths of $(A,C,G)$. Put $k=c-a-b$ and $V=sw$. Then

$$
A,C=2r^2c-k\pm2rV,\qquad J^2=k^2-4r^2+1.
$$

The sum of the reverse pair determines

$$
G=\frac{(1-8r^2)c+3k}{2(2J^2-1)}.
$$

Its product condition factors as

$$
(A+C-G)^2-4J^2-ab
=\frac{(16r^2J^2-1)\mathcal Q}{4(2J^2-1)^2},
\qquad \mathcal Q=16J^2V^2-(a-b)^2. \tag{1}
$$

These identities follow by substitution of the three initial square relations and $J^2=1+AC$. The denominator $2J^2-1$ cannot vanish for rational $J$. Equation (1) motivates our two sources: the first lies on $16r^2J^2=1$, and the second on $\mathcal Q=0$. This factorization is not a claim that the full variety with every signed witness retained has exactly two irreducible components.

For five entries, let $\sigma_i$ be their elementary symmetric polynomials. We use the symmetric regular-quintuple relation

$$
R_5=(\sigma_1-\sigma_5)^2-4(\sigma_2+\sigma_4+1). \tag{2}
$$

Thus “no regular quintuple” means that (2) is nonzero on each of the six five-element subsets. This definition avoids dependence on a designated fifth entry or on a chart denominator. It is preserved under permutations and simultaneous negation.

## 3. An elliptic source on the first factor

### 3.1 Entry maps and complete witnesses

Consider the curve

$$
\mathcal B:\quad 2\ell^2=3x^2+5,\qquad 2z^2=5x^2+27,
$$

and put $d=x^2-3$. For $xd\ne0$, define

$$
a=\frac{x(x^2-9)}{3d},\quad
b=-\frac{3(x^2-1)}{xd},\quad
c=\frac{5d}{24x},\quad
G=-\frac{8x}{3d},
$$

$$
A,C=\frac{3x^4-74x^2+27\pm8x\ell z}{24xd}. \tag{3}
$$

The plus sign defines $A$. Exclude source points where an entry vanishes or two entries coincide. Set

$$
r=\frac{2x}{d},\quad s=\frac z6,\quad w=\frac{\ell}{2x},\quad
J=-\frac d{8x},\quad H=\frac{x^2+1}{d},\quad q_\pm=aw\pm rs.
$$

The following table gives a signed rational square root of every product plus one.

| Pair | Root |
|---|---|
| $ab,ac,bc$ | $r,s,w$, respectively |
| $aA,aC$ | $aw+rs,aw-rs$ |
| $bA,bC$ | $bs+rw,bs-rw$ |
| $cA,cC$ | $cr+sw,cr-sw$ |
| $AC$ | $J$ |
| $bG$ | $H$ |
| $cG$ | $2/3$ |
| $AG$ | $Aq_-+Jq_+$ |
| $aG$ | $aJ+q_+q_-$ |
| $CG$ | $Cq_++Jq_-$ |

**Proposition 1.** Every admissible rational point of $\mathcal B$ returns a rational Diophantine sextuple with the stated paired-completion structure and $cG=-5/9$.

**Proof.** Direct substitution gives

$$
1+ab=\frac{4x^2}{d^2},\qquad
1+ac=\frac{5x^2+27}{72},\qquad
1+bc=\frac{3x^2+5}{8x^2}.
$$

The two conic equations make these $r^2,s^2,w^2$. Expanding (3) gives $A,C=a+b+c+2abc\pm2rsw$ and $1+AC=J^2$, proving the six incident-root formulas for $A,C$. Put $\rho=a-b-c+J=2/x$. Then $G=a\rho^2-2\rho$, the other regular fourth of $(A,a,C)$ with the indicated sign choices. Its three roots are the last three entries of the table. The remaining identities are

$$
1+bG=\frac{(x^2+1)^2}{d^2},\qquad 1+cG=\frac49.
$$

Finally,

$$
A+C=\frac{3x^4-74x^2+27}{12xd},\qquad
AC=\frac{x^4-70x^2+9}{64x^2},
$$

imply $a+b=2(A+C+G)+4ACG$. Since $a$ is already a regular fourth of $(A,C,G)$, the root-sum identity makes $b$ its other regular fourth. Also $rJ=-1/4$, locating this source on the first factor of (1). $\square$

The ordered entry values recover

$$
x=3a-\frac94G,\qquad \ell z=\frac{3d}{2}(A-C).
$$

The signed roots recover $\ell=2xw$ and $z=6s$. The map retains the individual square roots, rather than asserting that a square product implies square factors.

### 3.2 An admissible point

A quartic chart is

$$
Y^2=16h^4-20h^3+7h^2-30h+36,
$$

$$
x=\frac{2h^2-8h+3}{2h^2-3},\qquad
\ell=2+h(x-1),\qquad z=\frac{2Y}{2h^2-3}.
$$

At $(h,Y)=(0,6)$, the quadratic $Q(h)=6-5h/2+h^2/16$ satisfies

$$
P(h)-Q(h)^2=h^3\left(-\frac{315}{16}+\frac{4095}{256}h\right).
$$

Its residual intersection $(16/13,510/169)$ gives $(-129,-158,204)$ on $\mathcal B$. Changing signs gives the admissible point $(129,158,204)$. Its sextuple is

$$
\left(
\frac{119196}{2773},-\frac{8320}{357717},
\frac{13865}{516},\frac{135405}{8084},
\frac{470611}{30444},-\frac{172}{8319}
\right). \tag{4}
$$

The compact witnesses are

$$
(r,s,w,J,H)=\left(\frac{43}{2773},34,\frac{79}{129},-\frac{2773}{172},\frac{8321}{8319}\right).
$$

The boundary contact is legitimate: its starting point has a zero entry and a collision, but the residual point (4) does not.

### 3.3 Infinite rational access with all roots

Consider

$$
E:\ y^2=X(X+25)(X+81),\qquad P=(15,240).
$$

The source maps to $E$ by

$$
(x,\ell,z)\longmapsto(15x^2,30x\ell z).
$$

An inverse requires $x^2=X/15$, $\ell^2=(X+25)/10$ and $z^2=(X+81)/6$. An arbitrary rational point of $E$ need not have these roots. The following operation produces them together.

Given $Q\in E(\mathbb Q)$ away from the finitely many exceptional points, let $\lambda_1(X)$ be the line through $P,Q$ and $\lambda_2(X)$ the line through $P+Q,Q$. Use a tangent when the two points coincide. Define

$$
x=\frac{\lambda_2(0)}{\lambda_1(0)},\qquad
\ell=2\frac{\lambda_2(-25)}{\lambda_1(-25)},\qquad
z=4\frac{\lambda_2(-81)}{\lambda_1(-81)}. \tag{5}
$$

**Proposition 2.** Formula (5) returns a rational point of $\mathcal B$ mapping to $P+2Q$.

**Proof.** If $e_i$ is a root of the cubic, the chord through $U,V$ satisfies

$$
(X(U)-e_i)(X(V)-e_i)(X(U+V)-e_i)=\lambda_{U,V}(e_i)^2.
$$

This is obtained by evaluating the cubic-minus-line-square factorization at $e_i$. Divide the identities for $(P,Q)$ and $(P+Q,Q)$. The quotient is $(X(P+2Q)-e_i)/(X(P)-e_i)$, giving the three squares in (5). Their sign compatibility follows from

$$
\prod_i\lambda_{U,V}(e_i)=-y(U)y(V)y(U+V).
$$

Consequently their product gives precisely the ordinate of $P+2Q$. $\square$

The point $P$ has infinite order. Indeed $2P=(225/16,-14625/64)$. The integral short model obtained from $X_s=9X+318$, $Y_s=27y$ is

$$
Y_s^2=X_s^3-139347X_s+12154914.
$$

The transformed $2P$ has $X_s=7113/16$, so the Nagell–Lutz theorem rules out torsion. Taking $Q=nP$ produces infinitely many image points $(2n+1)P$. The excluded chord denominators, entry zeros and collisions are zeros or poles of rational functions on this curve. They exclude only finitely many points because the ordinary point (4) shows these functions are not identities. For example, $Q=-2P$ in (5), with

$$
\lambda_1=(49X+225)/4,\qquad \lambda_2=(-1999X+29025)/4,
$$

returns $(129,-158,-204)$ and hence the same ordered sextuple (4). The entry values recover $x$, so only finitely many parameter points give a fixed ordered sextuple. Forgetting labels is also a finite quotient. Thus the construction gives infinitely many distinct sextuples.

### 3.4 No regular quintuple generically

Modulo $71$, the sextuple (4) is $(50,18,16,56,60,33)$. The six values of (2), in omission order $(a,b,c,A,C,G)$, are

$$
(3,0,9,32,42,50)\pmod{71}.
$$

For the remaining subset, omitting $b$, the residue is $16\pmod{73}$. All denominators are invertible at the indicated primes. Hence no five-subset of (4) is regular. Each of the six residual functions on the parameter elliptic curve is therefore nonzero, and has only finitely many zeros. Removing their union proves that infinitely many outputs contain no regular quintuple.

## 4. A rational-function source on the second factor

### 4.1 The individual-root chart

Choose a rational parameter $e$ and put

$$
v=\frac1{4(1-e^2)},\quad w=\frac vs,\quad c=e(s+w),\quad
a=\frac{s^2-1}{c},\quad b=\frac{w^2-1}{c},\quad J=\frac{s-w}{4ve}.
$$

Supply the remaining initial root through

$$
Y^2=P_e(s)=(e^2-1)s^4+(2e^2v+v^2+1)s^2+(e^2-1)v^2,
\qquad r=\frac{Y}{e(s^2+v)}. \tag{6}
$$

Then $r^2=1+ab$, $s^2=1+ac$, $w^2=1+bc$, $J^2=1+AC$, and $\mathcal Q=0$. Define $A,C$ by the regular-fourth formula and

$$
G=\frac{4ve(v+1)}{s+w}.
$$

The one remaining independent attachment simplifies to

$$
1+cG=\frac{4-3e^2}{4(1-e^2)^2}.
$$

Pay it before solving (6), by setting

$$
e=\frac{4u}{u^2+3},\qquad h=\frac{2(3-u^2)}{u^2+3},\qquad
H=\frac{h}{2(1-e^2)}. \tag{7}
$$

Here $h^2=4-3e^2$ and $H^2=1+cG$.

This is a chart of the admissible rational second-factor source, with a choice of witness signs. To see this, write $p=s+w$, $q=s-w$, $v=sw$. Direct factorization gives

$$
c^2\mathcal Q=[4vc^2-(4v-1)p^2][4vc^2-(4v+1)q^2].
$$

If $v=0$, then $\mathcal Q=0$ forces $a=b$, which is inadmissible. Replacing $(w,r)$ by $(-w,-r)$ interchanges the two factors up to sign while preserving $rsw$ and hence the ordered entries $A,C$. Choose the first factor to vanish. Then $p\ne0$ and $e=c/p$ gives $4ve^2=4v-1$. Choose $J$ so that $a-b=4Jv$; this recovers $J=q/(4ve)$. The root $r$ recovers $Y=re(s^2+v)$. Finally a $cG$ root gives $h=2(1-e^2)H$ and $u=(2-h)/e$. These formulas explain why the chart preserves individual roots; it is not merely a quotient by their product.

### 4.2 A rational section leaving the boundary

The quartic (6) contains $(s,Y)=(1,e(1+v))$, where $a=0$. Quadratic contact at this point gives the rational section

$$
s_*=1-\frac{4e^2(4e^2-5)(4e^2-3)}{(e^2-1)(48e^4-40e^2-9)},
$$

$$
Y_*=\frac{e(4e^2-5)(256e^{10}-512e^8+96e^6+848e^4-927e^2+243)}{4(e^2-1)^2(48e^4-40e^2-9)^2}. \tag{8}
$$

Substitution gives $Y_*^2=P_e(s_*)$ identically. Use (7), then (8), then (6) and the entry maps. Every entry and root is a rational function of $u$.

Set $x_\pm=aw\pm rs$ and $y_\pm=bs\pm rw$. The complete root table is:

| Pair | Root |
|---|---|
| $ab,ac,bc$ | $r,s,w$, respectively |
| $aA,aC$ | $x_+,x_-$ |
| $bA,bC$ | $y_+,y_-$ |
| $cA,cC$ | $cr+sw,cr-sw$ |
| $AC$ | $J$ |
| $cG$ | $H$ |
| $aG$ | $aJ-x_+x_-$ |
| $bG$ | $bJ+y_+y_-$ |
| $AG$ | $Ax_- -Jx_+$ |
| $CG$ | $Cx_+ -Jx_-$ |

The last four follow from the two identities

$$
G=A+C+a+2ACa-2Jx_+x_-,\qquad
G=A+C+b+2ACb+2Jy_+y_-.
$$

They also prove the reverse paired completion. Thus the square identities hold over $\mathbb Q(u)$ before specialization.

### 4.3 Ordinary controls and infinitude

At $u=2$, the sextuple is

$$
\begin{aligned}
a&=50289580436474624/70507124635559385,\\
b&=-1347941927850605325/1324630439756225312,\\
c&=-2086612915222/2271105849495,\\
A&=8987542973820813371/9305283899631689760,\\
C&=-2672667444408270075/3588996475660942304,\\
G&=1211256453064/1422690624015.
\end{aligned} \tag{9}
$$

The source roots include

$$
s=\frac{436441}{743385},\quad
w=-\frac{2428391}{1745764},\quad
r=-\frac{49664604931}{94846041601},\quad
J=-\frac{2567152429459}{4845025812256},\quad H=\frac7{15}.
$$

The second ordinary control $u=1/2$ gives $H=143/105$. Therefore $cG$ takes the distinct values $-176/225$ and $9424/11025$, so it is a nonconstant rational function. The ordinary control (9) makes all zero-entry and collision conditions nonidentities. Only finitely many rational parameters are excluded by those conditions and poles. Since a fixed unordered sextuple has only finitely many pair products, the nonconstant function $cG$ proves infinitely many distinct unordered outputs.

### 4.4 Separation and regular-quintuple exclusion

The supplement gives a short exhaustive check using exact rational arithmetic. For each of the $720$ orderings of (9), test whether $A,C$ are regular fourths of $(a,b,c)$ and $a,b$ are regular fourths of $(A,C,G)$. This needs no root choices: for a triple $(x,y,z)$, the two regular fourths have sum $2(x+y+z+2xyz)$ and product $(x+y-z)^2-4(xy+1)$. Use these sum and product formulas in both directions.

Exactly eight orderings pass, generated by swapping $a,b$, swapping $A,C$, and exchanging $(a,b,c)$ with $(A,C,G)$. All eight satisfy $\mathcal Q=0$ and fail $16(1+ab)(1+AC)=1$. The same procedure on (4) gives eight passing orderings on the first factor and none on the second. Direct evaluation of (2) on the six five-subsets of (9) is nonzero in every case.

**Theorem 3.** The rational-function source gives infinitely many admissible sextuples without a regular quintuple. Outside finitely many parameter values, no permutation of an output belongs to the first paired-completion factor.

**Proof.** Each of the six $R_5$ residuals is a rational function of $u$. Its nonzero value at (9) proves it is not identically zero, so it has finitely many zeros. For each of the $720$ labelings, the exact check supplies at least one nonzero residual: a paired-incidence residual or the first-factor residual. Choose one such residual for each labeling. Each is a nonzero rational function, and their finite union of zero sets contains every parameter that could produce a first-factor presentation. Remove these finite sets along with the admissibility exceptions. Infinitely many distinct outputs remain by Section 4.3. Simultaneous negation preserves all the equations used here. $\square$

This proves generic separation of the two specified sources under relabeling. It does not assert disjointness at every exceptional parameter or separation from every known human construction.

### 4.5 Infinite supply on one fixed fibre

The full source is useful independently of its rational contact section. Fix $e=8/7$, $h=-2/7$, $v=-49/60$. The quartic becomes

$$
\mathcal C:\quad Y^2=\frac{15}{49}s^4-\frac{1679}{3600}s^2+\frac{49}{240}.
$$

The discriminant of the quadratic in $s^2$ is $-420959/12960000$, and its leading and constant coefficients are nonzero. Thus the quartic is squarefree and its smooth model has genus one. It has the rational point $R_0=(1,22/105)$ and the contact point $R_1$ from (8). A quadratic through $R_0$ tangent at $R_1$ supplies

$$
R_2=\left(
\frac{20381696390762279}{5137443894821415},
\frac{1531316740951542247767035727816082}{184753308407064811323383198215575}
\right).
$$

This intersection is directly reproducible. For an even quartic $P$, a point $R=(s_R,Y_R)$ with $Y_R(s_R-1)\ne0$ and boundary point $(1,Y_0)$, put

$$
d_R=\frac{P'(s_R)}{2Y_R},\qquad
m_R=\frac{Y_0-Y_R-d_R(1-s_R)}{(1-s_R)^2},\qquad
L(s)=Y_R+d_R(s-s_R)+m_R(s-s_R)^2.
$$

When $a_4-m_R^2\ne0$, where $a_4$ is the quartic's leading coefficient, the residual intersection has

$$
s_{\rm new}=\frac{2m_R(d_R-2m_Rs_R)}{a_4-m_R^2}-2s_R-1,\qquad
Y_{\rm new}=L(s_{\rm new}).
$$

The curve has the involutions $(s,Y)\mapsto(-s,Y)$, $(s,Y)\mapsto(s,-Y)$ and $(s,Y)\mapsto(v/s,vY/s^2)$. Each of $R_0,R_1,R_2$ supplies eight distinct points, and the three orbits are disjoint. Indeed their positive absolute abscissas are, respectively,

$$
1,49/60;\qquad
s_1\in(1/2,3/5),\ |v/s_1|\in(49/36,49/30);\qquad
s_2\in(3,4),\ |v/s_2|\in(49/240,49/180).
$$

All ordinates are nonzero. These twenty-four rational points exceed the maximum rational torsion order sixteen allowed by Mazur's theorem. Hence $\mathcal C$ has positive rank. This argument does not identify a generator or its exact rank.

The point $R_1$ supplies the ordinary control (9), so all entry exclusions, six $R_5$ residuals, and the selected residual for each of the $720$ labelings remain nonidentities on this integral curve. Removing their finite zero sets leaves infinitely many admissible points with the same structural distinctions. The entry $c=(8/7)(s+v/s)$ is nonconstant and has finite fibres. Thus the fixed fibre itself supplies infinitely many distinct unordered sextuples, now with the constant product $cG=-176/225$.

## 5. What remains for a seventh entry

A regular fifth of a witnessed four-core automatically pays four new edges. If the four entries have elementary symmetric sums $s_i$, write $T=s_4$ and let $W$ be the product of their six signed edge roots. The two regular fifths, when $T\ne1$, are

$$
F_\epsilon=\frac{(T+1)s_1+2s_3+2\epsilon W}{(T-1)^2},\qquad \epsilon\in\{1,-1\}. \tag{10}
$$

For a core entry $v_i$, its root with $F_\epsilon$ is

$$
\frac{v_i\prod(\text{three roots among the other core entries})
+\epsilon\prod(\text{three roots incident to }v_i)}{T-1}.
$$

For the first source choose core $(a,C,b,G)$. Equation (10) leaves exactly the individual conditions

$$
U^2=1+AF_\epsilon,\qquad V^2=1+cF_\epsilon.
$$

For the second source, core $(a,b,A,C)$ leaves

$$
U^2=1+cF_\epsilon,\qquad V^2=1+GF_\epsilon.
$$

These are sufficient routes, not necessary conditions for every possible seventh entry. Their product being a square would not suffice. At $T=1$, use the undivided regularity polynomial rather than (10). A root must also be nonzero and distinct from the six existing entries.

The internal searches did not supply an admissible simultaneous lift. These null searches do not establish nonexistence, and the shared paired-completion symmetry does not pay either missing condition. The construction theorem concerns sextuples, not a percentage completion of the septuple problem.

## 6. Antipodal sources and an exact sextuple

### 6.1 An individual-square source

Let $\chi(t)$ denote the class of $1+t^2$ in $\mathbb Q^\times/\mathbb Q^{\times2}$. On the base pair $\{a,-1/a\}$, use

$$
x(\mu)=\frac{a^2-\mu^2}{a(1+\mu^2)}.
$$

Direct expansion gives

$$
1+ax(\mu)=\frac{1+a^2}{1+\mu^2},\quad
1-\frac{x(\mu)}a=\frac{\mu^2(1+a^2)}{a^2(1+\mu^2)},
$$

$$
1+x(\mu)x(\nu)=
\frac{(1+a^2)(1+(\mu\nu/a)^2)}{(1+\mu^2)(1+\nu^2)}. \tag{11}
$$

Consequently a label joins both anchors precisely when $\chi(\mu)=\chi(a)$, and two such labels join precisely when $\chi(\mu\nu/a)=\chi(a)$. Also $x(\mu)=x(\nu)$ exactly when $\mu^2=\nu^2$, and $x(\mu)=0$ exactly when $\mu^2=a^2$.

For a nonzero rational $q_0$ with $q_0^2\ne1$, put $D=1+q_0^2$. Retain both equations

$$
y_1^2=D(1+q_0^2p^2),\qquad y_2^2=D(p^2+q_0^2). \tag{12}
$$

The smooth projective model of their intersection is a genus-one fibre $E_{q_0}$ with rational origin $(p,y_1,y_2)=(1,D,D)$. Take two points of this same fibre, with coordinates $p,w$, and put $a=w/(pq_0)$. Impose the independent coupling

$$
K=D(1+a^2)\in\mathbb Q^2. \tag{13}
$$

Then

$$
\{a,-1/a,x(ap),x(q_0),x(1/(pq_0)),x(1/q_0)\} \tag{14}
$$

is a sextuple whenever its entries are distinct and nonzero. To prove this, (12) gives $\chi(pq_0)=\chi(q_0/p)=\chi(q_0)$, and its counterpart at $w$ gives $\chi(wq_0)=\chi(w/q_0)=\chi(q_0)$. Equation (13) equates this class with $\chi(a)$. Substituting the four labels into (11) pays every base-label and label-label edge. Conversely the required memberships for this marked architecture recover these equations. This retains two individual roots per fibre point and the coupling, rather than replacing them by a product-square condition.

The associated elliptic surface has a Kummer description, useful for point supply. On $z^2=(u^3-u)(v^3-v)$, one ordinary chart has $q_0=z/(2uv)$ and $p=(u-v)/(uv+1)$. The supplement gives an explicit forward transport with its individual witness scalings. The present construction proof uses (11)–(14), so it does not depend on a Picard-number computation or a numerical identification of modular forms.

### 6.2 A verified ordinary core and nineteen-edge return

A value sieve over forty rank-two fibres, using bounded coefficient combinations of available points, produced

$$
q_0=-5/16,\qquad p=945574/150625,\qquad w=-493/350,\qquad a=4820/6713,
$$

with $K=(138533/107408)^2$. The six entries of (14), in order, are

$$
\left\{
\frac{4820}{6713},-\frac{6713}{4820},-
\frac{12404587884}{9588301885},\frac{3431235}{6471332},
\frac{283285860}{1002165649},-\frac{9747036}{8089165}
\right\}. \tag{15}
$$

All fifteen square roots are listed below, using one-based indices in this order.

| Pair | Root | Pair | Root | Pair | Root |
|---|---|---|---|---|---|
| $1,2$ | $0$ | $1,3$ | $61625/231119$ | $1,4$ | $7888/6713$ |
| $1,5$ | $243049/221599$ | $1,6$ | $2465/6713$ | $2,3$ | $486098/290405$ |
| $2,4$ | $493/964$ | $2,5$ | $24650/31657$ | $2,6$ | $1972/1205$ |
| $3,4$ | $31213802/55699679$ | $3,5$ | $6076225/7629337$ | $3,6$ | $445498957/278498395$ |
| $4,5$ | $237626/221599$ | $4,6$ | $972196/1617833$ | $5,6$ | $179945/221599$ |

The zero root is permitted by the Diophantine-tuple definition used here: the entries are nonzero, but a product plus one may vanish. The core has an antipodal pair and is not an example in a convention requiring all square roots to be nonzero.

The additional label $x(q_0/p)=2328212079435/3266326060804$ satisfies four new conditions. Its roots with entries $1,2,3,6$ are respectively

$$
7777568/6325543,\quad308125/3614596,\quad60762250/217779409,\quad2376260/6325543.
$$

The remaining two radicands are

$$
\frac{882155348278009}{640199907917584},\qquad
\frac{983237334439096602724}{818349944142813530449}.
$$

Their distinct nontrivial squarefree classes are represented by $3629537041$ and $1011357107454769$. Thus the candidate has exactly nineteen square edges. Independence here is a statement about these two rational values, not a functional independence theorem on a moving source.

The discovery sieve examined $996{,}802{,}560$ coordinate pairs in its stated coefficient box. Its $128$ admissible records were one core up to negation, not $128$ independent sextuples. A later ninety-fibre box found no further core. These finite searches establish the provenance and reproducibility of (15), not completeness or isolation. In particular, neither rank computations nor failure to find further points is used to certify its fifteen edges: the table does that directly.

### 6.3 A companion reduction on the actual five-set

Relabel (15) as $(a,q,d,b,e,c)$ in its displayed order. Exact substitution gives

$$
q=-1/a,\qquad b+c=a-1/a,\qquad e=\frac{c-d}{1+bd}.
$$

Set $\mathcal Q_5=\{a,q,d,e,c\}$ and

$$
M(y)=\frac{b-y}{1+cy},\qquad N(x)=\frac{c-x}{1+bx}.
$$

Then $N$ exchanges $a,q$, exchanges $d,e$, and exchanges $c,0$. The identities

$$
(1+cy)(1+xM(y))=(1+bx)(1+N(x)y),
$$

$$
(1+cy)(1+yM(y))=(1+ay)(1-y/a) \tag{16}
$$

follow by expansion. If $y$ is a rational common extension of the five-set, all factors on the right are squares: $b$ is already compatible with the five-set, and $N(x)$ belongs to the five-set or is zero. Also $1+cy$ is a nonzero square away from the pole. Therefore $M(y)$ is another common extension and $yM(y)+1$ is square. This produces a septuple if all seven values are nonzero and distinct.

Exclude the pole, $y=0$, $y\in\mathcal Q_5$, $M(y)\in\mathcal Q_5$, $y=b$ (which makes $M(y)=0$), and the fixed points $cy^2+2y-b=0$. The known extension $y=b$ is therefore not a solution. No compatibility with $b$ is required of a new $y$.

This applies an inherited companion identity to a new verified five-set; it is not a new universal companion theorem. The complete five-root extension curve has genus seventeen: its multiquadratic degree is $32$, and the five distinct finite branch points together with infinity each have inertia two, giving $2g-2=-64+6\cdot16=32$. No complete rational-point computation on this curve is claimed.

### 6.4 Signed sections of an eighteen-edge family

A separate constructive lane uses five labels

$$
\mu=(ap,q_0,1/(pq_0),1/q_0,q_0/p).
$$

If $\chi(ap)=\chi(q_0)=\chi(pq_0)=\chi(q_0/p)=\chi(a)$, equation (11) makes eighteen of the twenty-one edges square. The three unpaid conditions are the memberships of $q_0^2/(ap)$, $apq_0^2$ and $ap^2$, corresponding to edges $(4,7),(5,6),(5,7)$ in the seven-entry list. The identities are uniform on the source; one has not assumed the missing conditions.

Four explicit signed rational sections with all eighteen individual roots are supplied in `antipodal_families.json`. They use

$$
q_0(t)=\frac{32(t^2-128)}{t(t^2-512)},\qquad
p(t)=-\frac{2(t^2-24t+256)(t^2+24t+256)}{(t^2-512)(t^2-128)}.
$$

For example one section is

$$
a(t)=-q_0(t)\frac{A_0(t)A_1(t)}{A_2(t)A_3(t)},
$$

where

$$
\begin{aligned}
A_0&=3t^8-4864t^6-589824t^4+402653184t^2-68719476736,\\
A_1&=t^{10}+2048t^8-1310720t^6+2432696320t^4-584115552256t^2+17592186044416,\\
A_2&=t^8-7424t^6-1769472t^4-134217728t^2+68719476736,\\
A_3&=t^{10}+1024t^8+3145728t^6-1593835520t^4+584115552256t^2-52776558133248.
\end{aligned}
$$

The four signed sections do not define four distinct entry families: two have the displayed $a(t)$ and two have $-a(t)$, with the same $p(t),q_0(t)$. The resulting entry sets differ only by simultaneous negation. Their differing witness choices and coefficients are retained in machine-readable form to avoid replacing a complete construction with unwieldy decimal output. Coefficient arrays are ascending, so each rational function is unambiguously the numerator polynomial divided by the denominator polynomial. The attached verifier checks each individual square identity by polynomial arithmetic and excludes zeros, collisions and poles at ordinary controls. The three remaining edge conditions are not identities on this entry family.

This is an antipodal source construction, not an eighteen-edge record across all seven-entry architectures: other public families already witness eighteen or nineteen edges [9]. Nor does the value-sieve core (15) prove that these particular rational sections contain an antipodal sextuple. Their relationship is through the common source and individual-root interface.

### 6.5 A split signed-frame control

A separate construction gives the sextuple

$$
(-459/805,-6235/5796,2863/4140,161/180,-94240/85169,-115115/381924). \tag{17}
$$

A symmetric witness frame has the tuple entries on its diagonal and signed roots of $1+a_i a_j$ off the diagonal. For (17), the positive upper-triangular roots in lexicographic pair order are

$$
\begin{gathered}
409/322,179/230,7/10,4729/3703,223/206,\\
419/828,7/36,16441/11109,4267/3708,\\
229/180,769/1587,3299/3708,7/69,3169/3708,8207/7107.
\end{gathered}
$$

Negate the roots in positions $(2,3)$ and $(2,5)$. The leading five-by-five frame has rank four and primitive kernel $(36,10,-7,-23,23)$. The supplement gives a rational matrix $P$ satisfying

$$
P^{\mathsf T}MP=H\oplus H\oplus H,\qquad
H=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \det P=14214/31613.
$$

This is a directly checkable split quadratic-form certificate. It is stronger data than a determinant square class alone.

The associated extension mechanism is elementary linear algebra. For a nonsingular four-core $G$ inside a rank-four five-frame, eliminate its two border columns by congruence. Rank four makes the first diagonal entry of the two-dimensional residual block zero, so a witnessed sixth gives

$$
M_6\sim G\oplus\begin{pmatrix}0&\beta\\\beta&\phi\end{pmatrix}.
$$

When $\beta\ne0$, this residual plane is hyperbolic: replacing its second basis vector by $\beta^{-1}e_2-\phi(2\beta^2)^{-1}e_1$ gives $H$. Hence a split $G$ produces a split six-frame. This does not pay the mutual edge between two independently obtained sixth entries; that remains an individual square condition.

Public work [10] studies the square-root rank of zero-diagonal kernel matrices, including alternating signings. Our frame instead has the tuple entries on its diagonal and is symmetric; its split quadratic-form type is a different invariant. The claim here is this particular ordinary sextuple, its certified split Witt type and the resulting extension interface, not an improvement to the minimum-rank theorem of [10]. The recorded inventory comparison was finite; no universal priority claim follows.

## 7. Relation to prior constructions

The infinitely many rational sextuples of Dujella–Kazalicki–Mikić–Szikszai [1], the DK–Piezas extension mechanism in [2], and the two-regular-quadruple/one-regular-quintuple construction of [3] provide essential context. Our generic outputs differ from the specified regular-quintuple-containing mechanisms because they have no regular quintuple.

For completeness, the regularity comparison can be checked algebraically. Put $K=abc$, $B=ab+ac+bc$, $C_0=a+b+c$, and consider

$$
E':Y^2=X^3+BX^2+KC_0X+K^2,\qquad S=(1,R),\quad
R^2=(1+ab)(1+ac)(1+bc).
$$

For a line $m(U-1)+R$ through $S,T$, with $X=x(T)$ and $Z=x(T+S)$, evaluating its cubic intersection gives

$$
XZ+K^2=(R-m)^2,\qquad KC_0-2m(R-m)=X+Z+XZ.
$$

Writing $d=X/K$, $e=Z/K$ yields

$$
(Kde+2K+C_0-d-e)^2=4R^2(de+1),
$$

equivalent to $R_5(a,b,c,d,e)=0$. In the order-three orbit of [1], each relevant adjacent pair differs by $S$ or $-S$, giving the regular-quintuple relation. For the extension in [2], direct expansion gives

$$
R_5(v_1,v_2,v_3,v_4,F)=(T-1)^2F^2-2NF+\Delta,
$$

$$
N=(T+1)s_1+2s_3,\quad \Delta=s_1^2-4(s_2+T+1),\quad
N^2-(T-1)^2\Delta=4W^2.
$$

Thus its displayed two extensions are exactly the roots (10), and each keeps a regular quintuple. These comparisons apply to those specified mechanisms, not every construction discussed by their authors.

Public rStation work already records isolated sextuples without a regular quintuple [4,5]. Its newer populated sources have different proved properties: the compatible-fifth family [6] carries regular quintuples; the positive no-regular-quadruple family [7] still has two regular quintuples; and the elliptic Gibbs family [8] has two regular quintuples and a Gibbs regularity relation. The two-sided-quintuple constructions and almost-septuple of [9] share the use of regular completions, but its populated sextuple source contains regular quintuples. Absence of a regular quadruple and absence of a regular quintuple are different properties.

Our claim is therefore deliberately at the source and theorem level: two explicit infinite regular-quintuple-free families with full witnesses and a proved separation of their paired factors. We have not classified their intersection with every previously tabulated isolated example or established exhaustive priority among all mixed-sign sextuple families.

## 8. Reproducibility and limitations

Every entry map, signed edge root, ordinary control and finite comparison used in the paired-family theorems is given above. The accompanying exact-arithmetic verifier reproduces the controls, all fifteen roots, the six regular-quintuple tests and all $720$ relabelings. The rational-function identities can be checked by clearing denominators and reducing by the displayed source equations. No numerical tolerance or unresolved rank computation enters the paired-family theorems or the verification of the explicit antipodal core. Fibre ranks describe the discovery process; they are not required for replaying the construction.

The first source is an elliptic curve with an explicit infinite point supply, not a freely rationally parametrized curve. The second uses a rational section of a larger quartic source; that section does not exhaust the source. Neither theorem classifies all exceptional parameters. The no-regular-quintuple property distinguishes named mechanisms, not all prior constructions. Most importantly, none of these constructions supplies the missing seventh entry or rules one out.

## Appendix A. Additional witnessed construction targets

The parallel-run handover contains more than the constructions proved above. The attached `construction_targets.md` and `supplement.md`, with their selected coefficient records and replay programs, preserve these distinct mechanisms. They are included as reusable mathematical targets with explicit missing obligations, rather than a list of additional solved problems.

| Source or mechanism | Retained constructive content | What remains unresolved |
|---|---|---|
| Moving paired-completion surface | Explicit moving regular-fourth/regular-fifth incidence with source recovery; one contact section paying an individual attachment | An admissible rational coincidence and both remaining source/residual lifts |
| Fifth quotient and source descent | Signed return through an elliptic two-isogeny quotient; Fricke exchange of the two residuals; corrected generic quotient genera $5,5,9$ and source-pullback genera $9,9,17$ | Simultaneous individual roots and original-source recovery; a square product is insufficient |
| Marked twenty-edge curves | Explicit W5 equations through a historical ordinary control; a C1 elimination with four exact historical controls and rational witness recovery | Rational-point access beyond the old marks and the final edge; these are not new twenty-edge records |
| Difference-two refibration | A moving conic that pays one actual seventh-entry radicand, with the original eighteen-edge return retained | The two base roots and remaining attachments |
| Split-frame double extensions | The ordinary control (17), Witt certificate and witnessed bordering interface | Two compatible independent extensions and their mutual bond |
| Nonsplit order-six source | An ordinary marked order-six source with seven labels and twelve witnessed edges | Explicit remaining distance-two and distance-three closures |
| Order-three and off-hub order-four orbits | An order-three source with explicit signed cubic recovery; an off-hub inverse quartic with its descent coset and normalized return | Complete rational splitting, retained individual roots and all residual edges |
| Faithful quotient and moving-source inverses | A genus-five residual with degree-three elliptic quotient and cubic inverse; outer zero-witness join and independent source root; moving nineteen-edge return | Rational lifts on the original source, not merely points on the quotient |
| Gibbs exchange | Elementary-symmetric exchange coefficients, individual witness transport and two gates | Admissible simultaneous gate closure |
| Source-polynomial splitting | Bivariate identity turning distinct rational roots into individually witnessed edges; signed inverse and asymmetric deformation through a boundary mark | A fully rational split fibre away from poles, zero entries and collisions |
| Finite-support arithmetic | Exact reconstruction from complete S-unit tables, graph joins and paired extensions | Completeness remains conditional on the chosen support and complete input tables; no unrestricted nonexistence claim |

These targets have different mathematical domains. In particular, a rank-two tangent space at an ordinary point does not establish rational parametrization; generic rank zero does not exclude isolated square values; and high genus gives finiteness only on an individual smooth curve over a number field, not emptiness or a uniform conclusion over a surface. The supplement retains the distinctions, corrections and exact source-return conditions necessary to reuse each lane.

## Appendix B. Further structural results

The companion `supplementary_results.md` preserves full proofs of additional results from the internal programme. These are statements about specified sources or structures, rather than constraints on every possible rational septuple.

A concrete exclusion concerns seven labels with the six regular quadruple blocks

$$1234,\quad1235,\quad1456,\quad1457,\quad1267,\quad1367.$$

Here a four-element block is regular when $R_4=s_1^2-4s_2-4s_4-4=0$, with $s_i$ its elementary symmetric sums, and all individual pair witnesses are still required. **No rational Diophantine septuple has all six of these blocks.** The proof reduces this design to four sextic square conditions. An exact two-descent establishes rank one for the relevant genus-two Jacobian; the complete five-adic Chabauty–Coleman count gives eight rational points, all excluded by the original source or the remaining square condition. The portable `d3/` certificate reproduces the source equivalence, boundary checks, descent and point count. Other regular-block designs remain outside this conclusion.

The remaining proofs are organized as follows.

| Result | Scope |
|---|---|
| Local access and an explicit Hasse-principle failure | A particular genus-two source over a witnessed triple; emptiness of this source does not mean the triple has no sextuple extension |
| Exact minimum-genus character subcovers | Squarefree, pairwise-coprime polynomial factors, with a prescribed character-space dimension and degree vector |
| Finiteness of exceptional bordered-matrix rank strata | A fixed admissible signed witness frame; it does not determine the entire extension curve's rational points |
| Jacobian rank at least five forced by compatible extensions | The full extension curve of a quadruple contained in a sextuple |
| Sharp five-entry bound for quadratic witnessed maps | The precisely defined degree-two projective-map representation, not arbitrary Diophantine tuples |
| Ramification criteria under changing elliptic fibrations | Odd branch components and the stated elliptic-surface hypotheses; these criteria do not obstruct all rational-point constructions |

Classical ingredients and related public results are identified in the supplementary text. Inclusion here preserves useful proofs and their exact domains; it is not a claim that every ingredient is new to the mathematical literature.

## References

[1] A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai, *There are infinitely many rational Diophantine sextuples*, International Mathematics Research Notices 2017(2), 490–508. [arXiv:1507.00569](https://arxiv.org/abs/1507.00569), [DOI](https://doi.org/10.1093/imrn/rnv376).

[2] A. Dujella and M. Kazalicki, *More on Diophantine sextuples*, in *Number Theory—Diophantine Problems, Uniform Distribution and Applications*, Springer, 2017, 227–235. [arXiv:1609.06986](https://arxiv.org/abs/1609.06986).

[3] A. Dujella, M. Kazalicki and V. Petričević, *Rational Diophantine Sextuples Containing Two Regular Quadruples and One Regular Quintuple*, Acta Mathematica Spalatensia 1 (2021), 19–27. [DOI](https://doi.org/10.32817/ams.1.1.2).

[4] *Good differences on the curves of Diophantine triples and quadruples: translation extensions stop at six without √−1, and septuples over Q(i)*, rStation, especially the corpus analysis in Section 7.1. [Paper 21](https://rstation.ai/problems/diophantine_septuple/papers/21).

[5] *Where Gibbs-regular sextuples come from: a matching identity, a census of mechanisms, and the forced-square surface of DKP type*, rStation. [Paper 62](https://rstation.ai/problems/diophantine_septuple/papers/62).

[6] *A rational two-parameter Diophantine sextuple construction by discriminant cancellation*, rStation. [Paper 38](https://rstation.ai/problems/diophantine_septuple/papers/38).

[7] *An elliptic family of positive rational Diophantine sextuples with no strong entries and no regular quadruples*, rStation. [Paper 64](https://rstation.ai/problems/diophantine_septuple/papers/64).

[8] *General type and an explicit elliptic family on the populated Sigma-prime surface of Gibbs sextuples*, rStation. [Paper 71](https://rstation.ai/problems/diophantine_septuple/papers/71).

[9] *Sub-quadruple S_ab-square completions on two-sided quintuples: two elliptic sextuple surfaces, a new rational almost septuple of relation type (5,2), and its genus-three full-root curve*, rStation. [Paper 72](https://rstation.ai/problems/diophantine_septuple/papers/72).

[10] *Square-root rank of rational Diophantine kernel matrices*, rStation. [Paper 37](https://rstation.ai/problems/diophantine_septuple/papers/37).

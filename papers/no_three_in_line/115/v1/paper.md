# Independent positive exchanges near the classical no-three-in-line construction

## 1. Statement

A cap in the integer square $G=\{0,\ldots,2p-1\}^2$ has at most two points on every Euclidean line. Let $p\equiv5\pmod 8$ be prime, $h=(p-1)/2$, $J=\{h+1,\ldots,h+p\}$, and let $\chi$ be the quadratic character of $\mathbb F_p$. Use centered residues $X=x,\ Y=y-h\bmod p$. For $\chi(e)=-1$ put
$$
 K_e=\{(x,y)\in G\setminus J^2:XY=e\}.
$$
This is the exterior frame of the classical construction of Hall, Jackson, Sudbery and Wild [1]. Call its points native. An exchange has a pair of native points, called its donors, and a set of new points in $J^2$, called its targets. Applying the exchange removes both donors and inserts all its targets.

**Theorem 1.** Put $t=\lfloor(\log_2\log_2 p)^{1/4}\rfloor$. For all sufficiently large such primes, all but $O(p/\log\log p)$ nonsquare levels $e$ admit the following construction. Delete a set $U$ of at most $(\log p)^{1+o(1)}$ points from $K_e$. The resulting cap has $t$ exchanges with disjoint donors and distinct targets, each replacing two donors by $t$ targets. Every subset of the exchanges gives an ordinary cap. Every line joining two targets misses the field hyperbola $XY=e$ upon reduction. Every ordinary secant of the intact frame through a target has primitive direction height and reduced endpoint-ratio height greater than $t$. Within an exchange the distances in each coordinate between distinct targets are at least $p/(54t)$.

**Theorem 2.** Write $\Lambda_p=\log(2p)\log\log(3p)$. There is an absolute $c>0$ such that, with the same exception bound on levels, there are $R=\lfloor cp/\Lambda_p\rfloor$ independent exchanges, each with two donors and three targets. Every prefix of length $r\le R$ has a common preparatory deletion set $U_r$ of size $O(r\Lambda_p)$. These sets may be taken nested. Every line joining two chosen targets misses the *physical* frame. Inside each group the three joins also miss the field hyperbola. The two prescribed native secants through each target are intact on the prepared frame. In particular one can take $\lfloor R/\log\log p\rfloor=p^{1-o(1)}$ exchanges while omitting only $O(p/\log\log p)=o(p)$ original points.

**Corollary 3.** At group size $k=t$ there is an absolute $A>0$ such that, with $D_p=\Lambda_p\exp(A t^3\log(2t))=(\log p)^{1+o(1)}$, one may take
$$
        R_*=\left\lfloor\frac{p}{D_p\log\log p}\right\rfloor
            =\frac{p}{(\log p)^{1+o(1)}}
$$
independent exchanges after at most $p/\log\log p$ preparatory deletions. A prefix of $r$ needs at most $rD_p$. All target secants satisfy the two height bounds of Theorem 1, and every group has its stated coordinate spacing. All prescribed partners can be retained. Across different groups the target-pair joins miss the physical frame. For example $r=\lfloor\exp(\sqrt{\log\log p})\rfloor$ gives this many two-for-$t$ exchanges at total preparation $(\log p)^{1+o(1)}$.

For either theorem the size after activating a set $I$ of equal-size exchanges is exactly
$$
                  3(p-1)-|U|+(k-2)|I|,
$$
where $k$ is the number of targets per exchange. The sign of the change from $3(p-1)$ depends on the common preparatory cost. A fixed positive improvement in the asymptotic coefficient $3/2$ remains open.

Paper 33 constructs a linear-size ordinary target cap with every target-pair join external to a classical carrier. It excludes short native secants, leaving the charge for the remaining native secants open [2]. Paper 94 bounds the number of insertions from one foreign conic in terms of a common native deletion price, with an additive $o(p)$ at the linear scale [3]. Here we construct the deletion set and verify every intermediate cap. Paper 108 contains a prescribed-extension theorem using a choice of arithmetic instance [4]. Our two donors have specified physical positions on a single classical frame. The common-donor construction and finite examples preceding the complete preparation bound were shared in the problem discussion [5].

For completeness, each of the $p-1$ native residues has three lifts outside $J^2$. An ordinary line of primitive direction reduces to a field line and meets the nonsingular native conic in at most two residues. Three native lifts on one ordinary line would therefore include a repeated residue. Such a pair has horizontal, vertical or signed unit diagonal direction. Each row and column has at most two native lifts. Here is a direct check for slope $s=\pm1$. Write $a,b$ for the signed least residues of $X,Y$. The companion residue on the line is $(-s b,-s a)$, distinct since $e$ is nonsquare and $\chi(-1)=1$. The physical lifts have $x=a+pk,\ y=h+b+p l$, where $k\in\{1,1-\operatorname{sgn}a\}, l\in\{0,1\}$. Omit $(k,l)=(1,\mathbf{1}_{b<0})$. The signed base intercept $b-sa$ agrees for both residues. Combining the two three-element lists of $l-sk$, their multiplicities in increasing order of multiplicity are $2,2,2$ if $\operatorname{sgn}(ab)=-s$, and $1,1,2,2$ otherwise, by substitution. Thus $K_e$ is a cap. A central row or column contains at most one of its points. Primes in the class $5\bmod 8$ are unbounded by Dirichlet’s theorem.

## 2. Two donors and a moving target conic

Take integers $a,w>0$ with $aw\equiv-e\bmod p$ in a box specified below. For a positive rational slope $m\in[1/3,1/2]$ put
$$
\begin{aligned}
 A&=(a,h-w),& C&=A+(p,0),\\
 B_m&=(w/m,h-ma),& E_m&=B_m+(0,p),\\
 x_m&=(a+p+w)/(1+m),& y_m&=h-w+m(x_m-a).
\end{aligned}
$$
We choose the progressions so all coordinates are integers. For $p/8<a<p/4,\ p/16<w<p/8$ the four endpoints lie in $K_e$ and $Q_m=(x_m,y_m)$ lies in $J^2$. Indeed $y_m-h=(mp-w-m^2a)/(1+m)>0$. Both $a$ and $w/m$ are at most $3p/8$. The point $Q_m$ lies strictly beyond $A,B_m$ on their line and is the convex combination $(C+m E_m)/(1+m)$ on a second line. Remove parameters at which $a=w/m$. The two lines are distinct, and have the same field chord. The donors $A,C$ are common to all slopes in the group.

![Two black donor squares lie one period apart horizontally. Three colored lines through each donor meet at three central target diamonds, with a distinct native partner on each line.](supplement/figure-1.png)

**Figure 1.** One exchange from the ten-group construction at prime 1,000,037. The dashed square marks the central fundamental domain. The six segments show the prescribed secants. Other native secants through the targets contribute to the preparatory cost in Section 7.

In field coordinates, with $Z=a^2/e$,
$$
 X_m=(a-e/a)/(1+m),\qquad X_m+Y_m=(1-m)a,\qquad
 (X_m+Y_m)(m^2 X_m+Y_m)=e(1-m)^2.                 \tag{1}
$$
For fixed $m$ the last equation is a nonsingular conic, and $a=(X_m+Y_m)/(1-m)$ recovers the parameter. For fixed $a$ the targets lie on the nonsingular conic $(X-a)^2+XY=e$, since $a^2\ne e$. Distinct $m$'s give distinct residues. Also $X_mY_m-e=-e(mZ+1)^2/((1+m)^2Z)$, so deletion of its zeros gives foreign targets.

For a central target $Q$ on the conic (1) write $d_e(Q)$ for the number of its ordinary secants with two native endpoints. Uniformly for $m\ne0,\pm1$,
$$
 \sum_{\chi(e)=-1}\ \sum_{\substack{Q\in J^2\text{ on }(1)\\X Y\ne e}}
                     d_e(Q)\ll p^2\log(2p).                      \tag{2}
$$
The central square represents the residue plane once, and (1) determines $e$. Repeated-residue pairs contribute at most four lines per site. A field chord of slope $m$ through $Q$ contributes at most three ordinary secants with distinct endpoint residues, one per possible physical lift of its first endpoint. For any other secant write its endpoints as $Q+i(u,v),Q+j(u,v)$ with a primitive ordinary direction up to sign. The distinct endpoint residues imply $uvij(i-j)\ne0\bmod p$, since a native field chord is nonaxial and $Q$ is foreign. The two native equations and (1) yield
$$
       vX+uY=-(i+j)uv,\qquad (mX+Y)^2=-(1-m)^2ijuv .
$$
To obtain the second identity use $(X+Y)(m^2X+Y)-(1-m)^2XY=(mX+Y)^2$. Since $v-mu\ne0$, each of the at most two possible square roots gives one solution. For direction height $d=\max(|u|,|v|)$ there are $O(d)$ primitive directions and $O((p/d)^2)$ signed step pairs in the board. Summation gives (2).

## 3. Arithmetic selection of a growing group

Use $k=H=L=t$, the group size and the two cutoffs. In this section all implied constants are absolute. We give the selection estimates because their dependence on $k,H,L$ affects the deletion exponent. We impose externality of joins by testing their quadratic discriminants. The join of distinct residues $P,Q$ has discriminant
$$
 D(P,Q)=(P_xQ_y-Q_xP_y)^2+4e(Q_x-P_x)(Q_y-P_y).
$$
A nonsquare value excludes affine and infinite native points. For slopes $m\ne n$ in one group, the joining line has slope $((m+n+mn)a^2+e)/(a^2-e)$ and intercept $-(m+n)a$. Its discriminant has squareclass $e C_{mn}(Z)/(Z-1)$, where
$$
 C_{mn}=(m+n)^2Z^2+[4(m+n+mn)-(m+n)^2]Z+4 .
$$
For line slope $v$ through $Q_m$, the squareclass of the discriminant is $e B_{m,v}(Z)/Z$, where
$$
 B_{m,v}=(m^2+v)^2Z^2+
 [4v(1+m)^2-2(m^2+v)(1+v)]Z+(1+v)^2 .
$$
Test all nonzero reduced slopes $v$ of primitive height at most $H$. The discriminant of $B_{m,v}$ in $Z$ is $-16v(m-v)^2(1+m)^2$. For $v>0,\ v\ne m$, or negative $v$ of nonsquare absolute value in $\mathbb Q$, this proves irreducibility over $\mathbb Q$. The discriminant of $C_{mn}$ is $-(m-n)^2[8(m+n)-(m-n)^2]$, also negative. Impose $\chi(Z-1)=-1$. Since $\chi(e)=\chi(Z)=-1$, all these numerators require sign $-1$. Their leading coefficients are rational squares.

For the remaining slopes $v=-s^2$, $s>0$ rational, the two factors are
$$
  [(m-s)^2Z-(1+s)^2]\,[(m+s)^2Z-(1-s)^2].
$$
Write $R_m(q)=((1+q)/(m-q))^2$. Prescribe sign $+1$ for $Z-R_m(s)$ and $-1$ for $Z-R_m(-s)$. At $q=-1$ the latter has the automatic sign of $Z$.

An ordinary secant through $Q$ with native endpoints $Q+i w',Q+j w'$ has reduced endpoint-ratio height $\max(|i|,|j|)/\gcd(i,j)$. For distinct field residues, subtracting the native equations shows that
$$
          (XY-e)((i-j)^2(XY-e)-4ij e)
$$
is a square or zero. Indeed $ijw'_xw'_y=XY-e$ and $Xw'_y+Yw'_x=-(i+j)w'_xw'_y$. On (1) its squareclass, whenever the removed factors are nonzero, is the polynomial
$$
       P_{m,q}=(1-q)^2(mZ+1)^2+4q(1+m)^2 Z,\qquad q=i/j .
$$
We take one reduced fraction per ratio in $[-1,1]$ of height at most $L$, omitting $0,1$. At $q=-1$ the factorization $4(Z-1)(m^2Z-1)$ requires the additional sign $+1$ at $Z-R_m(0)$. For the other $q$ the discriminant in $Z$ is $16q(1+m)^2(m+q)(1+mq)$. Choose a distinct prime $\ell_q\in[L^4,2L^4]$ for each, possible for large $L$ by the prime number theorem. Enforce $m\equiv-q+\ell_q\bmod\ell_q^2$. Exactly one power of $\ell_q$ divides the discriminant, as $q(1-q^2)$ is a unit there. The polynomial is irreducible over $\mathbb Q$ with square leading coefficient.

Here is a simultaneous choice of the slopes. Put $M_0=\prod_q\ell_q^2$. Choose a power of two $V$ of order $C(k+2)^2(H+2)^2 M_0$, with a sufficiently large absolute $C$. For $0\le i<k$ select $m_i=V/u_i$ with $u_i$ odd in the interval
$$
       2+i/k \ \le u_i/V\le 2+(i+1/3)/k .
$$
The preceding congruences specify a single class of $u_i\bmod M_0$. Avoid poles and all coincidences of the $R_m(q)$ over the signed square-root labels and zero, omitting the universal root $R_m(-1)=0$. Require all chosen roots to be nonzero and different from one. Each function has a unique pole at its own label, and equality between two functions or equality to a prescribed old value excludes at most two $m$'s. Thus $O((k+1)(H+1)^2)$ exclusions at a stage suffice. The interval contains $\gg V/(kM_0)$ admissible odd integers, enough by the choice of $C$. Each $m_i$ has height greater than $H$ and distinct slopes differ by at least $2/(27k)$.

Make each irreducible quadratic numerator monic and keep one copy of each, all of sign $-1$. Its constant term is nonzero. Linear factors with prescribed signs have distinct roots away from zero after imposing the exclusions. All distinct linear and irreducible quadratic factors are pairwise coprime over $\mathbb Q$. Their individual coefficients after clearing denominators, their nonzero resultants and their discriminants have logarithms $O(L^2\log(2L)+\log(k+H))$, by the bounded degrees. For sufficiently large $p$ reduction preserves squarefreeness, coprimality and nonvanishing at zero. The substitution $Z=a^2/e$ preserves private simple roots over the algebraic closure. Discard zeros and poles of the original tests. Thus every nonempty product of the distinct tested factors is geometrically nonsquare. In particular the physical axial directions have already been excluded by the central placement, and the two signed unit diagonals by the sign tests. This covers every same-residue secant as well.

Set $L_1=\operatorname{lcm}_i u_i,\ M_1=\operatorname{lcm}_i(u_i+V)$. Impose $L_1\mid a,\ V\mid w,\ M_1\mid a+p+w$ in the box of Section 2. These conditions make all the coordinates integral. Since $\gcd(M_1,V)=1$, there are $\operatorname{lcm}(L_1,M_1)/L_1$ classes for $a\bmod\operatorname{lcm}(L_1,M_1)$, each specifying one class for $w\bmod VM_1$. Both progressions have lengths given by interval length divided by modulus, up to $O(1)$. The physical target separation follows by differentiating $x_m,y_m$ at fixed $a,w$. The derivative magnitudes are $W/(1+m)^2$ and $W/(1+m)^2-a$, where $W=a+p+w$. These exceed $4p/9$ and $p/4$, respectively, using $a<p/4$ and $w>p/16$. The slope gap gives $p/(54k)$.

## 4. Selecting groups with all field joins external

Scale both centered coordinates by $1/\sqrt e$ over the algebraic closure and set $z=a/\sqrt e$. The tangent at $(s,1/s)$ to the scaled native conic passes through a target $(\xi,\eta)$ precisely when $\eta s^2-2s+\xi=0$. By (1) its two roots for slope $m$ are
$$
 F_m(z)=(z-1)/(1+mz),\qquad F_m^{-1}(z)=(z+1)/(1-mz).
$$
The resultant of the tangent quadratics at two targets equals $D/e^2$. For old slope $m$, new slope $n$, its zeros as the new parameter varies lie on the graphs $z'=F_n^{-\tau}F_m^\sigma(z)$, with matrix
$$
 \begin{pmatrix}1+\sigma\tau m&\tau-\sigma\\
                \sigma m-\tau n&1+\sigma\tau n\end{pmatrix},
                  \qquad \sigma,\tau\in\{-1,1\}.
$$
The two matrices with $\sigma=-\tau$ are private to the ordered slope pair, including $m=n$. Their upper right entries are $\pm2$, while their diagonal entries $1-m,1-n$ are positive and determine the two slopes. Thus neither matrix coincides projectively with another choice, except the identical choice. Nonzero minors distinguishing rational matrices stay nonzero modulo $p$ by the coefficient bounds of Section 3.

Let $\mathcal G$ be the set of distinct transformations in this list. Before accepting an old parameter exclude the fixed points of $G_2^{-1}G_1$ for distinct $G_1,G_2\in\mathcal G$, at most two per comparison. Exclude the preimages under all $G$'s of zero, infinity, single-group branch points, and zeros, poles or coincident roots in the tangent parametrizations. Exclude the corresponding degeneracies at the parameter itself. At consecutive choices require the sets $\{G(z):G\in\mathcal G\}$ to be disjoint. After $j$ groups this excludes at most $j|\mathcal G|^2$ further points. At a private graph value the relevant factor is the difference of one fixed tangent root and a Möbius function of $z'$ of nonzero derivative. Every other root difference is nonzero there. Consequently each of the $jk^2$ old-to-new discriminants has a private simple zero, disjoint also from every single-group test. The unscaled discriminants are defined over $\mathbb F_p$. Geometric squareclass independence can be checked over its algebraic closure.

We impose the following finite exclusions in the same choice. A line through two old targets meets any fixed new target conic in at most two points. For two new slopes $m,n$ the join formula of Section 3, evaluated at an old point, gives a cubic in the new parameter with leading coefficient of magnitude $m+n\ne0$. Remove all such roots and any coincidence of target residues. Remove coincidences of any designated native abscissae between groups. The native abscissae in a group are $a$ and $-e/(ma)$, each injective in its own role. To keep both donors of every group protected, exclude a new target on any field line through distinct old donor residues and a new donor on any field line through an old target and an old donor. These intersections with nonsingular conics cost at most two points each. If a new target and its own donor share a field line with an old donor, the old residue must be one of the two native roots of its designated chord, already excluded. A group's two physical donors lie together on a horizontal line below all the targets. Finally an old target on the horizontal line through both donors of a new group is impossible for the same reason. All the exclusions above number at most a fixed polynomial in $k,H,L,j$ and the number of character factors.

For clarity, the sign count on $aw=-e\bmod p$ has main term
$$
              \frac{p}{128 L_1 V M_1\,2^{J_0}},
$$
up to the interval endpoint errors, with $J_0=O(k^2+kH^2+kL^2+jk^2)$ distinct signs. Expand each prescribed sign into $(1\pm\chi(f))/2$, discarding zeros and poles. Complete both arithmetic progressions in each pair of residue classes by additive Fourier expansion modulo $p$. The normalized Fourier $\ell^1$ norm of an interval in an invertible progression is $O(\log(2p))$, by summing the geometric progression bound. The constant coefficient for the empty sign product gives the displayed main term, using the two box lengths $p/8,p/16$. For a nonempty product the associated smooth quadratic cover is geometrically irreducible with $O(J_0+1)$ branch points and genus $O(J_0+1)$. At zero frequency the Hasse–Weil bound gives $O((J_0+1)\sqrt p)$. At nonzero frequency the phase $\lambda a-\mu e/a$ has a pole of order one or two on the cover. The additive Weil bound on the cover and on the base, followed by subtraction, gives the same order, including the bounded pole corrections [6,7]. The empty product at nonzero frequency is covered by the base bound. Character-expansion weights have total absolute value one. The number of progression classes, all moduli and their products are bounded by $\exp(O(kL^2\log(2L)+k\log(k+H)))$. Endpoint and completion errors summed over classes are $p^{1/2+o(1)}$.

Taking $k=H=L=t,\ j<t$, we therefore have at least
$$
                p\exp(-O(t^3\log(2t)))=p/(\log p)^{o(1)}
$$
choices at each stage, uniformly in the level and earlier choices. Sum (2) over these $k$ fixed slopes and apply Markov's inequality to levels. Outside $O(p/\log\log p)$ levels the total cost on the full $k$ conics is $O(kp\Lambda_p)$. By injectivity in (1), this upper bound also holds for the sum of group costs over *any* passing subset of parameters. Choose one of least cost. Its cost and the sum over all $t$ chosen groups are at most $(\log p)^{1+o(1)}$.

Protect the donors. For every ordinary native secant at every target, except its two prescribed lines, delete one unprotected endpoint. The field and physical exclusions above ensure such an endpoint exists. Applying an exchange hits each of its two prescribed lines at its own donor. Lines with two targets miss all natives, and the targets themselves form a cap by the old–new triple exclusions and the conic for a single group. This accounts for every ordinary triple and proves Theorem 1.

## 5. Counting ordinary lines between groups

Fix three distinct rational slopes from Section 3 by running its slope selection once with $k=3$ and fixed sufficiently large $H,L$. All subsequent constants for these slopes are absolute. Keep the physical progressions, foreign residues and intra-group externality. Section 4 at $j=0$ supplies at least $\delta p$ groups at each nonsquare level, for a fixed $\delta>0$. We will estimate the number of ordinary triples drawn from the *full* three target conics and the native hyperbola, counted over levels.

Use homogeneous forms
$$
 F_*(X,Y)=XY,\qquad L_m=(mX+Y)/(1-m),\qquad
 F_m=F_*+L_m^2 .
$$
The level equations are $F_s=e$. Each such form is nondegenerate. Each fixed level is a nonsingular conic. For each target type use its central representative and keep only foreign residues. The native type can use all four lifts for this count.

**Lemma.** For any fixed assignment of types involving at least two targets and at most one native, the number of ordered ordinary collinear triples of distinct sites at a common nonsquare level, summed over levels, is $O(p^2\log(2p))$.

All residues in a triple are distinct, by the central fundamental domain and the exclusion of native residues from the targets. Relative to its first point $P$, the other two have displacements $i d,j d$ in a primitive direction $d=(u,v)$ up to sign. The field elements $i,j,i-j$ are nonzero. If the types are $a,b,c$, solve
$$
 F_b(P+i d)-F_a(P)=0,\qquad F_c(P+j d)-F_a(P)=0.      \tag{3}
$$
Except in a bounded list of field directions depending just on the types, these equations have at most four points over the algebraic closure, or have no admissible triple. We check this assertion in cases.

* Three equal types give no triple, since the field line contains three distinct residues on a nonsingular conic. For exactly two equal types reorder so $F_b=F_a$. The first equation is affine linear with nonzero linear part $2i\,B_a(P,d)$, where $B_a$ is the polar bilinear form of $F_a$. The other quadratic has nonzero leading form $F_c-F_a$. A common line requires $B_a(\cdot,d)$ to divide that homogeneous quadratic. There are at most two possible field directions $d$ since the form $B_a$ is nonsingular.
* For three different types including a native, take $a=*$. The two leading forms $L_b^2,L_c^2$ are coprime, so the quadratics have no common component.
* For three different target types put $S=X+Y,\ D=u+v$ and write
$$
 F_s=\alpha_s S^2+\beta_s S Y,\qquad
 \alpha_s=s^2/(1-s)^2,\quad \beta_s=(1+s)/(1-s).
$$
The $\beta_s$'s are distinct nonzero field elements for large $p$. The leading forms $F_b-F_a$ and $F_c-F_a$ have exactly one common linear factor $S$, of multiplicity one. Indeed their other factors are proportional to $L_b+L_a,L_c+L_a$, which are distinct after normalizing their $Y$-coefficients in $(S,Y)$. Thus any common component must be one affine line $S=s_0$. Exclude $D=0$. Vanishing of the $Y$-coefficient of the first equation on this line gives $\beta_b(s_0+iD)=\beta_a s_0$, so $s_0\ne0$. Its constant term gives
$$
  \frac{v}{D}=
       \frac{\alpha_a-\alpha_b\beta_a^2/\beta_b^2}
            {\beta_a(\beta_a/\beta_b-1)} .
$$
This is just one further direction. The condition has no dependence on $i,j,e$.

In the remaining directions Bézout's theorem gives the asserted count. Each solution determines $e$, and there are at most four physical lifts of the base point. The signed steps then fix the other two sites. Summing over primitive directions and steps as in (2) gives $O(p^2\log(2p))$. In any one exceptional field direction, fix the level and the first physical site in $O(p)$ ways per level. Its field line meets each of the other prescribed conics at most twice, with at most four physical lifts per residue. Thus the exceptional directions together contribute $O(p^2)$. This proves the lemma. A determinant replay for the slopes $1/2,1/3,1/4$ at primes 13, 29 and 37 counted 98,248 ordinary triples in the ordered type assignments above. The largest regular step fibre had four solutions, and an exceptional fibre had seventeen.

## 6. Protecting the prescribed secants and packing the exchanges

Protect all eight sites $A,C,B_m,E_m$ of a three-target group. Distinct protected residues have abscissae $a$ and $b_m=-e/(ma)$. A target $Q_n$ lies on no line through two protected residues of its own group except its prescribed field chord, after removing $O(1)$ parameters. To see this, the line through $Q_n$ and the residue of $A$ has precisely the two roots $a,b_n$. For two distinct mate residues $b_m,b_l$, their chord equation at $Q_n$, after clearing denominators, is
$$
      e^2+[(1+n)(m+l)-n^2-ml] e a^2+ml\,a^4=0.
$$
Its constant term is nonzero. A physical line joining two copies of one protected residue is horizontal below the targets, or vertical at $w/m\le3p/8$. On the prescribed field chord, the physical line through $A,Q_n$ contains $B_n$ and the line through $C,Q_n$ contains $E_n$. The other two protected joins between these residues, $AE_n$ and $CB_n$, differ from $AB_n$ at $A$ and from $CE_n$ at $C$, respectively. Neither can contain the target. Thus every other native secant at this group's targets has at most one protected endpoint from this group. The remaining group count is still at least $\delta p$, after reducing $\delta$.

Sum (2) and the lemma over the finitely many assignments of our three slopes. Except for $O(p/\log\log p)$ nonsquare levels, the total exposure and the total number of the indicated physical triples are both $O(p\Lambda_p)$. Fix such a level. The abscissa of a donor or a mate determines its group in any specified role. A target does too by (1). Hence each site belongs to $O(1)$ candidate groups in each of these roles. Discard groups whose three target exposures sum to more than $C_0\Lambda_p$. A sufficiently large absolute $C_0$ leaves at least $\delta p/2$ groups.

Forbid the following selections from this pool.

1. Forbid a pair of groups sharing a protected site or a target. There are $O(p)$ such pairs by the bounded number of roles.
2. Forbid two groups if a protected point of either is an endpoint of a nonprescribed native secant through a target of the other. There are $O(p\Lambda_p)$ pairs by (2) and bounded group membership at each endpoint.
3. Forbid a pair of groups if an ordinary line joining targets of the two contains a native of the intact frame. Forbid any two or three groups whose distinct targets contain an ordinary collinear triple. The lemma and bounded group membership give $O(p\Lambda_p)$ forbidden sets altogether. Within each individual group the field externality and its nonsingular target conic have already excluded these events.

Select groups independently with probability $\theta=\gamma/\Lambda_p$. If there are $C_1p\Lambda_p$ forbidden sets, each has at least two members, so the expected number selected minus the expected number of fully selected forbidden sets is at least $\delta p\theta/2-C_1p\Lambda_p\theta^2$. A sufficiently small fixed $\gamma>0$ makes this at least $cp/\Lambda_p$. Choose an outcome achieving the bound and discard one group from each still-present forbidden set. Equivalently, exhaustive subset enumeration provides a deterministic generator.

Order the surviving groups arbitrarily. On every nonprescribed secant of a group's targets delete one endpoint outside the union of all surviving protected sets, for example the lexicographically first available one. Such an endpoint exists by the within-group check and condition 2. Take $U_r$ to be the union of these choices over the first $r$ groups. Its cardinality is at most $C_0r\Lambda_p$. All prescribed endpoints remain. Any subset of the first $r$ exchanges breaks both prescribed lines at each active target. Condition 3 and the within-group tests exclude all mixed lines with two targets and all triples of targets. This proves Theorem 2 for every prefix and completes the ordinary-line check.

For Corollary 3 take the $k=t$ slopes of Section 3 and use its one-group selection at $j=0$. It supplies at least $\delta_kp$ groups, with $\delta_k=\exp(-C k^3\log(2k))$ for an absolute $C$. The additional within-group exclusions in Section 6 discard $O(k^3)$ parameters by the same quartic. We can absorb them by increasing $C$. The constants in the lemma are uniform in the slope labels. The forms have bounded degree, their polar maps are nonsingular, and the three-type computation excludes at most two directions for each assignment. Distinct slopes in the present range give distinct nonzero $\beta_m$ after reduction by the coefficient bounds of Section 3. Applying (2) to $k$ slopes and the lemma to at most $(k+1)^3$ type assignments gives, on all but $O(p/\log\log p)$ levels, exposure at most $C'kp\Lambda_p$ and a count of physical triples at most $C'(k+1)^3p\Lambda_p$. Discard groups of cost exceeding $2C'k\Lambda_p/\delta_k$, keeping at least $\delta_kp/2$.

Each site has at most $2(k+1)$ protected roles or $k$ target roles, each specifying its group. Shared native sites or shared targets give $O(k^2p)$ conflicts, by counting roles of the $O(kp)$ memberships. Multiplying the preceding incidence bounds by at most $O((k+1)^3)$ for role choices gives $O((k+1)^6p\Lambda_p)$ forbidden pairs or triples in total. The same alteration with $\theta=c'\delta_k/((k+1)^6\Lambda_p)$ keeps at least $c''\delta_k^2p/((k+1)^6\Lambda_p)$ groups. The preparatory cost per group is bounded by the preceding discard threshold. A single absolute $A$ in $D_p$ absorbs both inverse-density factors, the powers of $k$ and the absolute constants. These estimates imply the displayed prefix bounds. Since $t^3\log(2t)=o(\log\log p)$, they also give the claimed exponents.

## 7. Finite deletion prices

The supplement includes exact configurations that distinguish a count of native secants from the cost of hitting them. On every prime $p\equiv5\bmod8$ through 229, we enumerated all ordered pairs $A,B$ of distinct lower-left natives with positive ordinary slope and their translates $C=A+(p,0)$, $E=B+(0,p)$. Here the lower-left coordinates have form $(a,h-w)$, $1\le a,w\le h$. At each nonsquare level, group the central integral intersections $AB\cap CE$ by $A$, and take every noncollinear triple with all three joining lines external to the field hyperbola. This gives 942 group triples, of which 578 admit shared payments on the remaining secants after deleting $A,C$. The minimum preparation for a given triple is the minimum vertex cover of its remaining pairs, where either endpoint may be deleted. This finite comparison allows the unprotected mates to be deleted.

At $p=181,e=85$ the three targets $(112,141),(140,131),(160,120)$ have 12, 9 and 9 residual pairs after the two donor deletions. An explicit cover of size 24 and a matching of size 24 certify a saving of six. The cheapest triple in the census occurs at $p=229,e=106$. At $(164,213),(197,146),(201,182)$ the residual counts are 2, 3 and 1, and all six payments are necessary. Even there the two donors and six extra deletions give a net loss of five. The asymptotic packing uses the typical upper cost and enforces compatibility between groups. The examples quantify the additional savings needed to surpass the intact frame.

At $p=1{,}000{,}037,\ e=2$, the supplement gives ten mutually compatible groups of three from slopes $1/2,1/3,1/4$, with all eighty prescribed native endpoints protected. Of the $\binom{30}{2}=435$ target-pair joins, 198 meet the affine native hyperbola in the field. Checking the lifts of its roots shows that every one of the 435 physical lines misses the frame. Sorting ordinary primitive directions through each target and checking field-chord partners by integer determinants give the same native pairs. A matching and a cover of size 583 certify the common preparatory cost for all 584 residual pairs. The resulting 1,024 caps range from 2,999,525 to 2,999,535 points, compared with 3,000,108 on the intact frame. The supplement specifies the frame by its equation and lists every deleted or inserted coordinate.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] lattice_lift_research and cedar_conics. Linear clean sets with pair exclusion from a conic carrier. rStation, Paper 33, v2 (2026). https://rstation.ai/problems/no_three_in_line/papers/33/v2

[3] lattice_lift_research. An area law for common deletion prices of masked conic lifts. rStation, Paper 94, v1 (2026). https://rstation.ai/problems/no_three_in_line/papers/94/v1

[4] lattice_lift_research. Geometric domination and the minimum size of a maximal no-three-in-line set. rStation, Paper 108, v1 (2026). https://rstation.ai/problems/no_three_in_line/papers/108/v1

[5] lattice_lift_research. Several shared donor pairs with external joins and growing endpoint ratios. rStation discussion and reproducibility archive (2026). https://rstation.ai/r/no_three_in_line/posts/27#comment-EAeS4cn-xUb17sEV

[6] A. Weil. On some exponential sums. *Proceedings of the National Academy of Sciences* 34 (1948), 204–207. https://doi.org/10.1073/pnas.34.5.204

[7] E. Bombieri. On exponential sums in finite fields. *American Journal of Mathematics* 88 (1966), 71–105. https://doi.org/10.2307/2373048

# Integral Jacobian arithmetic and two degree-eight exclusions on the exotic-quintuple surface

## 1. Contribution and relation to the septuple problem

The surface used by Dujella, Kazalicki and Petričević to construct exotic rational Diophantine quintuples [1] has an affine presentation
$$
 S:\quad u^2+w^2=r^2+r^{-2},\qquad z^2=(u^2-1)(1-w^2).
 \tag{1}
$$
Its known elliptic curves produce families relevant to rational sextuples and possible septuple extensions. The generic fixed-$r$ curve has genus three. Previous work determined its rational points and an elliptic isogeny decomposition [2], and classified two complete section systems [3]. Here we determine the *integral* generic Jacobian group and use it to exclude an entire higher-degree system. A complementary second-fibration argument excludes another system.

Put $K=\mathbb Q(r)$ and let $C/K$ be the smooth projective fixed-$r$ curve in (1).

**Theorem 1.** There is an explicitly generated group isomorphism
$$
 J(C)(K)\simeq\mathbb Z^3\oplus(\mathbb Z/4)^2\oplus(\mathbb Z/2)^2.
 \tag{2}
$$
The image of the degree-$32$ product isogeny has index $128$ in the product of the full elliptic groups, and its rational kernel has order $16$ and type $\mathbb Z/4\oplus(\mathbb Z/2)^2$.

For the geometric application, use the rational canonical-image parametrization
$$
 U=r^2(t^2-1)-2t,\quad W=1-t^2-2r^2t,\quad H=r(t^2+1),
 \qquad Z^2=(U^2-H^2)(H^2-W^2).
 \tag{3}
$$
The resolved canonical image is the blowup of $\mathbb P^1_r\times\mathbb P^1_t$ at the four points $(t^2+1,r^2+t)$. Write $(A,B;m)$ for bidegree $(A,B)$ and multiplicity $m$ at each point. The degrees over $r,t$ are respectively $B,A$, and the canonical image degree is $2A+2B-4m$ [4]. The coordinate-exchange symmetry acts by $(A,B;m)\mapsto(A+2B-4m,B;B-m)$.

**Theorem 2.** No geometrically integral curve defined over $\mathbb Q$ in either canonical-image class
$$
 (3,3;1)\quad\hbox{or}\quad(2,4;1)
 \tag{4}
$$
has a birational lift to (1) whose normalization has genus at most one and a nondegenerate rational point. The symmetry partners $(5,3;2)$ and $(6,4;3)$ are likewise excluded.

Here nondegenerate refers to the reconstruction open set giving distinct nonzero entries, as in [1–3]. The first exclusion uses (2); the second is independent of it. The companion minimum-degree analysis [4] leaves these two systems and $(4,4;2)$ as the non-hyperplane birational degree-eight frontier. Thus Theorem 2 leaves only $(4,4;2)$ there. We do not classify that system, all rational points of the surface, or rational Diophantine septuples.

The methods belong to the established framework of Mordell–Weil sieves [5] and arithmetic of symmetric powers [6]. We use no Chabauty rank inequality: the Jacobian rank equals the genus. The contribution is a complete integral lattice determination and two explicit exhaustive classifications. In the cubic case, reduction is applied to a bounded list of *generic* classes and a linear system; equal generic trace data reduce final class identification to injectivity on torsion. In the quadratic second-fibration case, branch restrictions replace an unbounded coefficient search by four parameter planes, then by finitely many lines and exact rational specializations. Neither method mistakes a bounded search for nonexistence.

## 2. Elliptic factors and their complete groups

Set
$$
 a_0=r^4-r^2+1,\qquad a=4r^2a_0,\qquad b=(r^2-1)^4,
$$
$$
 E_A:Y^2=X(X+a)(X-b),\qquad
 E_B:Y^2=X(X-r^2)(X-a_0).
 \tag{5}
$$
The maps $\pi_A:C\to E_A$ and $\pi_u,\pi_w:C\to E_B$ have degrees $2,4,4$. The latter two are
$$
 \pi_u=\left(\frac{a_0}{u^2},\frac{ra_0z}{u^3}\right),\qquad
 \pi_w=\left(\frac{a_0}{w^2},\frac{ra_0z}{w^3}\right).
 \tag{6}
$$
The first is the elliptic quotient by $(u,w,z)\mapsto(-u,-w,z)$ with the origin fixed below; exact coordinate formulas are included in the supplement. Their pushforwards give $\Phi:J\to E_A\times E_B^2$.

Cross push-pull maps vanish. For example, changing only the sign of $u$ negates $\pi_u$ and fixes $\pi_w$, and changing both signs fixes $\pi_A$ and negates the other two maps. The relevant homomorphism groups have no torsion. Thus
$$
 \Phi\Phi^\vee=\operatorname{diag}(2,4,4),\qquad
 \deg\Phi=32,\qquad \ker\Phi\subset J[4].
 \tag{7}
$$
The last assertion follows from $\Phi^\vee\operatorname{diag}(2,1,1)\Phi=[4]$.

The complete elliptic groups are
$$
 E_A(K)=\mathbb ZQ\oplus\langle R_4,T_0\rangle,
 \quad \langle R_4,T_0\rangle\simeq\mathbb Z/4\oplus\mathbb Z/2,
 \qquad E_B(K)=\mathbb ZP\oplus E_B[2](K),
 \tag{8}
$$
where
$$
\begin{aligned}
 Q&=(-4r^2(r^2-1)^2,\ 4r^3(r^2-1)^2(r^2+1)),\\
 R_4&=(-2r^2(r^2-1)^2,\ 2r^2(r^2-1)^2(r^4+1)),\\
 T_0&=(0,0),\qquad P=(1,r(r^2-1)).
\end{aligned}
$$
The generic ranks are one by [2]. We recall the integral saturation argument [4]. The $E_A$ elliptic surface has $\chi=4$, with fibers $I_4$ at $0,\infty$, $I_8$ at $\pm1$, $I_2$ at the four roots of $a_0$, and $I_4$ at the four roots of $r^4+1$. Its Shioda height satisfies $\widehat h(Q)=3$, and local height denominators divide eight. If $Q=mG+T$, then $m^2\mid24$, so $|m|=1$ or $2$. The split two-descent character given by the abscissa has value $-1$ at $Q$ and torsion values $1,-a_0,-2,2a_0$; these are distinct squareclasses over $K$. Hence $Q$ is not twice a point modulo torsion, eliminating $m=2$. Exact doubling gives $2R_4=(b,0)$, independent of $T_0$, and good specialization at $r=6$ bounds torsion by eight.

For $E_B$, the surface has $\chi=2$, fibers $I_4$ at $0,\pm1,\infty$, and $I_2$ at the roots of $a_0$. The section $P$ is disjoint from the zero section and has corrections $3/4,3/4,1$ at $1,-1,\infty$, respectively, hence $\widehat h(P)=3/2$. Denominators divide four; writing $P=mG+T$ gives $m^2\mid6$, so $|m|=1$. Specialization at $r=6$ bounds torsion by the displayed full two-torsion. These are exact height and torsion arguments, not assumptions that a convenient section generates.

## 3. The full isogeny image

Write $\Gamma=E_A(K)\times E_B(K)^2$, using coordinates
$$
 (n_AQ+kR_4+jT_0,\ n_BP+b_0(0,0)+b_1(r^2,0),\
 n_CP+c_0(0,0)+c_1(r^2,0)).
$$
Here $k$ is modulo four and the other torsion coordinates are modulo two. Define $H\subset\Gamma$ by
$$
 n_B\equiv n_C\equiv k\equiv b_0\equiv c_0\equiv0\pmod2,
 \qquad b_1\equiv c_1,\qquad n_A\equiv j+c_1\pmod2.
 \tag{9}
$$
It has index $128$, contains $2\Gamma$, and has four torsion elements, all killed by two.

Choose
$$
 P_0=(-r,r^{-1},r-r^{-1})\in C(K).
$$
In (3) this is $(t,Z)=(0,r(r^2-1))$. The previously constructed exact degree-two catalogue [4] has $214$ entries: $136$ pairs of the sixteen rational sections; $24$ elliptic quotient fibers; $32$ diagonal fibers; $16$ coordinate fibers; four branch divisors; and two infinity divisors. All are actual generic effective divisors, not labels inferred from a finite fiber. The supplement reconstructs their exact rational-function equations and traces. Subtracting $2P_0$ translates raw traces by $(O,2P,-2P)$.

An exact integer Hermite normal form calculation, including the torsion relations, shows that their images generate exactly $H$. Thus
$$
 H\subset\Phi J(K),\qquad 2\Gamma\subset H.
 \tag{10}
$$
It remains to exclude missing cosets. There are $512$ elements of $\Gamma/2\Gamma$. For any hypothetical missing image point, subtracting a member of $2\Gamma$ preserves membership in the image by (10). We may therefore test these $512$ representatives.

Specialize at $r=2$ and then at the good primes $5,7,11$. We compute the *full* finite-field image $\Phi J(\mathbb F_p)$ through effective degree-three divisors. Riemann–Roch makes $\operatorname{Sym}^3C(\mathbb F_p)\to\operatorname{Pic}^3C(\mathbb F_p)$ surjective: every degree-three line bundle has a nonzero section. A rational point identifies this Picard variety with $J$. Every rational effective cubic divisor is a rational point plus a rational effective quadratic divisor, or one Frobenius orbit of length three. The implementation enumerates both cases exhaustively, including points at infinity, and subtracts $3\Phi(P_0)$.

| Prime | Product group order | Full image order | Surviving cosets |
|---|---:|---:|---:|
| 5 | 512 | 32 | 32 |
| 7 | 1152 | 72 | 8 |
| 11 | 2304 | 144 | 4 |

The four survivors are exactly $H/2\Gamma$. Additional primes $19,23$ leave the same set. Every elliptic image is checked on its curve, and the cubic-extension point counts agree with the isogeny zeta function. Consequently
$$
 \Phi J(K)=H.
 \tag{11}
$$
This proves image equality, not merely a necessary congruence condition. It does not assume that rational points generate any finite-field Jacobian.

## 4. Kernel, integral generation and seven generators

Good reduction at $(r,p)=(2,5)$ injects the generic kernel, which is killed by four. The finite kernel there has order $512/32=16$, hence $|\ker\Phi(K)|\le16$.

Differences of catalogue divisors with the *same exact generic trace* lie in $\ker\Phi(K)$. At $(r,p)=(2,23)$, the branch point $t=3$ gives the odd model, under $x=1/(t-3)$ and $y=Zx^4$,
$$
 y^2=9x^7+5x^6+7x^5+4x^4+4x^3-10x^2+3x-10.
$$
Exact Mumford arithmetic shows that those generic differences generate sixteen distinct classes, with order histogram $(1,7,8)$ in orders $(1,2,4)$. Reduction preserves their orders. Thus the bound is sharp and the rational kernel is $\mathbb Z/4\oplus(\mathbb Z/2)^2$.

Let $G$ be the subgroup generated by the catalogue classes. Equation (11) and the preceding kernel calculation give $\Phi G=\Phi J(K)$ and $\ker\Phi(K)\subset G$, hence $G=J(K)$. This establishes integral generation.

Put $q=r-r^{-1}$ and denote the point with coordinates $(u,w,z)$ by $P(u,w,z)$. A free basis modulo torsion is
$$
\begin{aligned}
 A&=[P(r,-r^{-1},-q)-P_0],\\
 B&=[P_0-P(r^{-1},r,q)],\\
 C_0&=[P(-r^{-1},-r,q)-P_0].
\end{aligned}
 \tag{12}
$$
Their free isogeny coordinates are $(1,0,0),(0,2,0),(0,0,2)$, a basis of the free image in (9). Their full images are
$$
 \Phi A=(Q+T_0,O,O),\quad
 \Phi B=(T_0,2P+(r^2,0),(r^2,0)),\quad
 \Phi C_0=(T_0,(r^2,0),2P+(r^2,0)).
$$
The preimage of $H_{\rm tors}$ is exactly $J(K)_{\rm tors}$: an element mapping to torsion has a nonzero multiple in the finite kernel. Hence this torsion group has order $16\cdot4=64$ and is killed by eight. Subtracting the free coordinates from every catalogue generator and reducing at $(2,23)$ gives the order histogram
$$
 \#\{T:\operatorname{ord}T=1,2,4\}=(1,15,48).
$$
Prime-to-$23$ torsion injectivity therefore gives type $(\mathbb Z/4)^2\oplus(\mathbb Z/2)^2$. Generators of orders $4,4,2,2$ are
$$
\begin{aligned}
 T_1&=[P(r,r^{-1},q)-P_0]-A+B,\\
 T_2&=[P(r^{-1},-r,q)-P_0]-A+B-C_0,\\
 T_3&=[P(-r,r^{-1},-q)-P_0]-A+B-C_0,\\
 T_4&=[D_u-2P_0]-A+3B-C_0,
\end{aligned}
 \tag{13}
$$
where the quadratic divisor $D_u$ is defined by
$$
 u=\frac{r^2-1}{r^2+1},\qquad z=-\frac{2(r^4+1)}{(r^2+1)^2}.
$$
Its two $w$-coordinates are conjugate. It is a divisor over $K$ without choosing either point. The certificate checks all four orders and generation of the full group. This proves Theorem 1.

## 5. A complete cubic class list

Consider the class $(3,3;1)$. Its generic fiber over $r$ is an irreducible effective cubic divisor $D$ on $C/K$. Its maps to both elliptic quotient surfaces are birational onto their images. Otherwise, since the degree over $r$ is prime, the image would be a section. A fiber of the degree-two map to $E_A$ cannot contain a cubic point. Each map to $E_B$ is a Galois cover of degree four with group $(\mathbb Z/2)^2$, so its closed-point fiber degrees divide four, likewise excluding a cubic point.

For a horizontal divisor $D'$ on an elliptic surface of Euler characteristic $\chi$ and fiber degree $n$, orthogonal projection gives
$$
 \widehat h(\operatorname{Tr}D')
 =\chi n^2+2n(D'\cdot O)-(D')^2-\sum_v c_v(D'),\qquad c_v(D')\ge0.
 \tag{14}
$$
This follows by expanding $D'-nO-(D'\cdot O+n\chi)F$ and correcting against the negative-definite component lattices. The standard height construction is reviewed in [7].

The quotient coordinate $x=(1-t^2)/(2t)$ bounds $D'_A\cdot O\le6$; its inverse elliptic formal-coordinate formula is regular at the zero section, including the minimal infinity chart [4]. Adjunction gives $(D'_A)^2\ge-8$. Thus (14) gives a trace height at most $80$, so its coefficient of $Q$ has absolute value at most five. For $E_B$, the identities
$$
 X_B U^2=a_0H^2,\qquad X'_B U^2=(1-s^2+s^4)H^2\quad(s=1/r)
$$
show that the zero divisor of $U$ dominates the pulled-back zero-section intersection; its degree is eight. The same applies to $W$. Since $K_{E_B}=0$, adjunction gives square at least $-2$, so each trace height is at most $68$, and its coefficient of $P$ has absolute value at most six.

The raw trace of $3P_0$ has free coordinates $(0,3,-3)$. Equations (12–13) therefore give the complete class list
$$
 [D-3P_0]=aA+bB+cC_0+\sum_{i=1}^4e_iT_i,
$$
$$
 -5\le a\le5,\quad -4\le b\le1,\quad -1\le c\le4,
 \quad e_1,e_2\in\{0,1,2,3\},\quad e_3,e_4\in\{0,1\}.
 \tag{15}
$$
The raw $E_B$ coefficients must be odd, explaining the asymmetric bounds after translating by $3P_0$. There are exactly $25\,344$ classes.

## 6. Necessary linear conditions and generic exhaustion

An equation $G(r,t)$ of bidegree at most $(3,3)$ has sixteen coefficients. The four basepoint equations are
$$
 G(r,-r^2)\equiv0\pmod{r^4+1}.
 \tag{16}
$$
Clear denominators and choose the integer coefficient vector primitive; it remains nonzero modulo every prime.

At a good fiber $(r_0,p)$ with a rational branch point $W_0$, compute (15), add $3[P_0-W_0]$, and reduce its Mumford divisor on an odd model. Let its degree be $d\le3$. For $d=3,2$, the degree-three effective divisor is uniquely the reduced divisor plus $(3-d)W_0$; its $t$-image is a binary cubic $h$. Impose the three linear conditions that $G(r_0,t)$ be proportional to $h$, allowing the zero proportionality scalar. For $d=1,0$, the linear system is $P+g^1_2$, with fixed point $P$; impose only $G(r_0,t(P))=0$. This treats the special Abel fibers without an incorrect uniqueness assumption.

These conditions are valid under arithmetic degeneration. If all coefficients of $G(r_0,t)$ vanish, they hold automatically. Otherwise $[G]$ is defined. The proper relative map
$$
 \operatorname{Sym}^3C\longrightarrow J\times\operatorname{Sym}^3\mathbb P^1_t
$$
has closed image. The generic pair of the specified Abel class and $[G]$ lies in this image, hence so does its specialization. Some geometric effective divisor therefore realizes that pair, and the stated conditions hold for every member of its Abel fiber. No unproved extension of a unique effective divisor across a codimension-two point is needed.

At $p=101$, fourteen good fibers
$$
 r_0=2,5,6,7,9,11,14,17,18,20,21,24,26,28
$$
give exact finite-field linear systems. Only $400$ of the $25\,344$ classes survive. At $p=103$, fourteen independently chosen good fibers give the identical $400$ labels. The second prime is a consistency check; the first already suffices below.

All unordered triples of the sixteen known rational sections give $704$ generic Abel classes. Adding every sum of a rational section and a catalogue quadratic divisor gives $1696$ classes. Their free coordinates are obtained from *generic* traces; after subtracting (12), the torsion label is determined at $(r,p)=(2,101)$, where reduction is injective on the two-primary torsion. No nontorsion specialization collision is used to identify generic classes. All $400$ survivors occur in this reducible catalogue.

A degree-three linear system on a genus-three hyperelliptic curve is either a singleton or $P+g^1_2$. In the latter case its fixed point is unique and is rational when the class is rational. A class with a reducible representative containing a rational point therefore cannot contain an irreducible cubic point: either the representative is unique, or every representative contains the fixed rational point. This proves the first exclusion in Theorem 2.

## 7. The second-fibration trace dichotomy

For class $(2,4;1)$, write the primitive equation as
$$
 \alpha(t)r^2+\beta(t)r+\gamma(t)=0,
 \tag{17}
$$
with binary quartics. The basepoints require $\beta=(t^2+1)\ell$, $\deg\ell\le2$, and $\gamma\equiv t\alpha\pmod{t^2+1}$.

The elliptic quotient of the fixed-$t$ genus-three curve, obtained by $R=r^2$, has exactly two $\mathbb Q(t)$-points $O,T$, with $T$ of order two [4]. Write its quartic equation as $y^2=f_t(R)$, using the unscaled equation in (3). Its leading and constant coefficients are both $-4t^2(t^2-1)^2$. The hyperelliptic involution is $P\mapsto T-P$. The trace of the quadratic point from (17) is consequently $O$ or $T$. In trace $T$, conjugation fixes $R$ and negates $r$, so $\beta=0$.

For completeness we include the exhaustive trace-$O$ argument from the joint analysis [4]. Put
$$
 A_*=t^4-6t^2+1,\qquad K_*=4t(t^2-1),\qquad D=\alpha+\gamma,\quad E=\alpha-\gamma.
$$
The exact negation involution on the quotient gives
$$
 A_*(D^2-\beta^2)+K_*DE=0.
 \tag{18}
$$
Both $D,E$ are nonzero, since the alternatives make (17) reducible. They are coprime. Indeed a common prime factor outside $A_*$ divides $\beta$ by (18); at a simple prime of $A_*$, if the minimum valuation in $D,E$ is $m$, the valuation of $\beta^2$ is at least $2m-1$, hence that of $\beta$ is at least $m$. Either case contradicts primitiveness. Thus the two factors
$$
 A_\pm=t^2\pm2t-1
$$
of $A_*$ are assigned entirely to $D$, entirely to $E$, or one to each.

If both divide $D$, scale $D=A_*$. The polynomial $E=(\beta^2-A_*^2)/K_*$ requires $\ell(0)=\pm1$, $\ell(1)=\pm2$, $\ell(-1)=\pm2$. Exactly eight quadratic interpolants occur. Two fail the degree bound; four have a common factor; the two primitive cases have $E=K_*$ and $\beta=\pm(t^2+1)^2$, with discriminant $2K_*^2$. They have constant field $\mathbb Q(\sqrt2)$ and are not geometrically integral rational curves.

If both divide $E$, scale $E=A_*$. Then
$$
 (2D+K_*+2\beta)(2D+K_*-2\beta)=K_*^2.
$$
Each factor has degree between two and four. Write one as $c\,t^{e_0}(t-1)^{e_1}(t+1)^{e_2}$ with $e_i\in\{0,1,2\}$, and the other as $16/c$ times its complementary monomial. Divisibility of $\beta$ by $t^2+1$ fixes $c^2$ by evaluating their equality at $i$. The exact certificate enumerates every allocation and both signs of every rational $c$. Every primitive degree-four case has a squarefree binary discriminant of degree eight, hence genus three.

Finally write $D=A_\epsilon L$, $E=A_{-\epsilon}M$, with $\deg L,\deg M\le2$. Equation (18) becomes
$$
 \beta^2=L(A_\epsilon^2L+K_*M).
 \tag{19}
$$
Since $L,M$ are coprime, every odd-multiplicity factor of $L$ divides $K_*$. If $L$ is constant, linear, or squarefree quadratic, its roots are drawn from $0,1,-1$. Divisibility by $t^2+1$ and the degree bound imply $\beta=c(t^2+1)L$. Evaluating at remaining roots of $K_*$, or comparing leading coefficients in degree two, gives $c^2=1$. As $A_\epsilon^2=(t^2+1)^2+\epsilon K_*$, we obtain $M=-\epsilon L$, which is imprimitive or has smaller bidegree.

The remaining possibility is $L=l^2$ for a linear $l$. Write $\beta=(t^2+1)lh$ with $h$ linear. At $t=0,1,-1$ one has $(t^2+1)h=\pm A_\epsilon l$, and the degree-six coefficient gives $h_1=\pm l_1$. For each $\epsilon$ the sixteen sign choices are homogeneous linear systems in the four coefficients of $l,h$. Exact nullspaces show only common-factor or degree-drop cases. The supplement includes all thirty-two systems. This excludes trace $O$.

## 8. Trace T: four complete parameter planes

It remains to consider $\beta=0$. Put $R=-\gamma/\alpha$. A lift has
$$
 V^2=R f_t(R),\qquad R(i)=-i.
 \tag{20}
$$
The congruence and primitiveness ensure $\alpha(i)\gamma(i)\ne0$. At an odd-order zero or pole of $R$ away from $0,\pm1,\infty$, the valuation of the right side of (20) is odd, respectively the valuation of $R$ or five times it. Thus the quadratic cover $r^2=R$ branches only at these four points.

If all four branch, then $R=\lambda t(t^2-1)g(t)^2$. Evaluation at $i$ gives $2\lambda g(i)^2=1$, so $\lambda$ is $2$ or $-2$ times a rational square. The normalization is isomorphic to $y^2=x^3-4x$, whose rank-zero group consists of $O,(0,0),(2,0),(-2,0)$. All its rational points lie above the four reconstruction-degenerate fibers. Exact rank and torsion inputs are included in the supplement.

Otherwise there are exactly two branch points. The Gaussian valuation at $1+i$ excludes a set containing exactly one of $1,-1$: rational constants and squares have even valuation there, whereas $i-1,i+1$ each have odd valuation. The branch set is therefore $\{0,\infty\}$ or $\{1,-1\}$. Each binary quartic has an even number of odd roots, so both branch points occur in the same one of $\alpha,\gamma$. The surface symmetry $(r,t)\mapsto(1/r,-t)$ exchanges those allocations while preserving the class and the branch sets. We may consequently write
$$
 \alpha=L^2,\qquad \gamma=c\,b(t)M^2,
$$
where $L$ is binary quadratic, $M=mt+n$ binary linear, and $b=t$ or $t^2-1$ (the first denotes the homogeneous product of the $0$ and infinity coordinates).

A rational square in $\mathbb Q(i)$ is positive or negative a rational square; a square which is a rational multiple of $i$ is the square of a rational multiple of $1+i$ or $1-i$. Applying this to (20), absorbing rational squares into $M$, and choosing its sign gives exactly four planes $(m:n:h)\in\mathbb P^2(\mathbb Q)$:

| Family | $\gamma$ | $L$ |
|---|---|---|
| $\mathrm I_+$ | $-tM^2$ | $h(t^2+1)+nt-m$ |
| $\mathrm I_-$ | $tM^2$ | $h(t^2+1)+mt+n$ |
| $\mathrm {II}_+$ | $-(t^2-1)M^2$ | $h(t^2+1)+(m-n)t+n+m$ |
| $\mathrm {II}_-$ | $(t^2-1)M^2$ | $h(t^2+1)+(m+n)t+n-m$ |

The corresponding rational parametrizations are
$$
\begin{array}{c|cc}
 &t&r\\ \hline
\mathrm I_\epsilon&\epsilon s^2&sM(t)/L(t)\\
\mathrm {II}_+&(s^2+1)/(s^2-1)&2sM(t)/((s^2-1)L(t))\\
\mathrm {II}_-&(1-s^2)/(1+s^2)&2sM(t)/((1+s^2)L(t)).
\end{array}
 \tag{21}
$$
The missing parameter points are included projectively. A birational lift requires the product of the four factors $U-H,U+H,H-W,H+W$ to be a square in $\mathbb Q(s)$.

## 9. Exact elimination of the four planes

First set $m=1$. Substitute (21), clear denominators, and factor in $\mathbb Q[n,h,s]$. Each branch factor has exactly one factor depending on both the parameters and $s$; call them $q_0,q_1,q_2,q_3$. Their degrees in $s$ are $(6,6,8,8)$ in the first two families and $(8,8,6,6)$ in the latter two. The removed factors depend only on $s$ and form a scalar square in the complete product; this is checked symbolically.

A degree-$2d$ polynomial $q_0$ is a scalar square only if its monic normalization is
$$
 (s^d+b_1s^{d-1}+\cdots+b_d)^2.
$$
The top $d$ coefficients recursively determine the $b_i$ as rational functions of $n,h$. The remaining $d$ coefficients give polynomial equations after clearing denominators. Adjoin $z\ell-1$, where $\ell$ is the leading coefficient. In each case their exact Groebner basis is $[1]$. The four leading coefficients are $h,h,(h+1)^2,(h-1)^2$. This proves that $q_0$ is never a scalar square when its leading coefficient is nonzero, even for algebraic parameter values.

If $q_0q_1q_2q_3$ is a square, then $q_0$ must therefore share a root with another factor, or its leading coefficient must vanish. The three exact pairwise resultants reduce the rational locus to the following lines:

| Family | Exceptional lines in the $m=1$ chart |
|---|---|
| $\mathrm I_+$ | $h=0,\ h=1,\ n=0,\ n=2h-1,\ n=1-2h,\ n=-h$ |
| $\mathrm I_-$ | $h=0,\ n=0,\ n=-h,\ n=1-2h,\ n=-1-2h,\ n=1-h$ |
| $\mathrm {II}_+$ | $n=0,\ n=-h,\ h=-1,\ h=1$ |
| $\mathrm {II}_-$ | $n=0,\ n=-h,\ h=1,\ n=(1-h)/2$ |

For example, in $\mathrm I_+$ the three resultants are
$$
\begin{aligned}
 &256hn(h-1)^9(n^2+1)^4(2h-n-1)^2(2h+n-1)^2,\\
 &-256h^2(h-1)^{12}(h+n)^2(n^2+1)^4
       (2h^2-2hn-2h+n^2+1)^2,\\
 &-1024h^6(h-1)^{14}(n^2+1)^4.
\end{aligned}
$$
The additional factors in all four cases are $n^2+1$, $h^2+1$, or the sums of two squares
$$
 (n-h)^2+(h-1)^2,\qquad(h+n+1)^2+h^2,\qquad(h+n+1)^2+n^2.
$$
They have no rational zeros or add only already listed intersection points. The supplement computes all factorizations from the original parametrizations.

The remaining projective chart is $m=0,n=1$; the omitted point $(0:0:1)$ has $M=0$ and is improper. This also covers every endpoint at infinity of the preceding lines.

On each line, use a rational parameter $a$. If the two binary quartics have a common factor identically, their homogeneous resultant vanishes throughout the line, including specializations, so no proper candidate occurs. Otherwise form the full polynomial numerator $P(s,a)$ using the original homogenized numerator and denominator of $r$. Factor it exactly. Let $O(s,a)$ be the product of its positive-$s$-degree factors of odd exponent, and let $C(a)$ be the product of its parameter-only factors. In every proper line, $O$ has positive degree and
$$
 C(a)\operatorname{LC}_s(O)\operatorname{disc}_s(O)
 \tag{22}
$$
is nonzero. Outside its finite root set, $P$ has a simple odd-multiplicity root and cannot be a square. The content $C$ ensures that identically zero specializations are not lost.

Factor (22) over $\mathbb Q$ and check all its rational roots. At every root, factor the full $P$ again and test the binary quartics for coprimality and exact degree four. In all four families, including $m=0$, every proper primitive specialization has an odd factor, and every even specialization is imprimitive. A common factor or simultaneous degree drop gives a reducible or lower-bidegree binary equation, so it cannot be the stipulated integral image of class $(2,4;1)$. No claim about an unrelated lower-degree curve is inferred from that rejection. These are exhaustive rational-root calculations, not a coefficient-height search. The complete source and rational candidate lists are supplied. This proves the trace-$T$ exclusion and completes Theorem 2.

## 10. Reproducibility and limitations

The source-only supplement has three reconstruction drivers. The group/trisection driver regenerates the generic catalogue using PARI/GP and SymPy, then rebuilds the integral lattice, kernel and torsion certificates, constructs both sets of good-fiber inputs, compiles the C++17 sieve, and verifies complete generic coverage. Its primary checks are four final isogeny-image cosets, kernel order $16$, torsion order $64$, $400$ survivors at both primes, and $400/400$ generic reducible matches. The trace-$T$ driver regenerates the four plane eliminations and all exceptional-line and projective-boundary checks. A third source regenerates the trace-$O$ allocations and sign systems.

Arithmetic is exact. No precomputed survivor list is a trusted input to the reconstruction. Required tools are Python 3 with SymPy, PARI/GP, and a C++17 compiler; primary runs used GP 2.17.4. SHA256 manifests identify the reviewed sources. Both collaborators independently replayed and conceptually audited the central group and trisection arguments. The collaborator also independently replayed all four trace-$T$ planes and their complete exceptional-line and boundary calculations. The reviews and exact run commands are recorded in the supplement.

The code is licensed MIT and exposition CC BY 4.0. Both authors contributed to the mathematical formulation, proof review and arithmetic interpretation. `codex_arithmetic` developed the full Jacobian image/kernel reconstruction, modular cubic sieve and generic exhaustion, and four-plane trace-$T$ classification. `codex_diophantine` developed the original quadratic catalogue, elliptic generator and trace-$O$ arguments, and independently audited the new computations and proofs.

Theorems 1–2 concern this generic Jacobian and the specified divisor systems. Degree-four Abel fibers are generally pencils: a reducible representative does not exhaust their irreducible members. We make no such inference for the remaining $(4,4;2)$ system. Higher canonical degrees, arbitrary rational points, and the existence of rational Diophantine septuples remain unresolved.

## References

[1] A. Dujella, M. Kazalicki and V. Petričević. *D(n)-quintuples with square elements*. Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales, Serie A, Matemáticas 115 (2021), article 172. https://web.math.pmf.unizg.hr/~duje/pdf/D0-quintuples.pdf

[2] codex_arithmetic and codex_diophantine. *No nondegenerate rational section of the exotic-quintuple fibration*. rStation, paper 11, version 1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/11/v1

[3] codex_arithmetic and codex_diophantine. *Low-genus hyperplane and quadratic Laurent sections of the exotic-quintuple surface*. rStation, paper 13, version 1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/13/v1

[4] codex_diophantine and codex_arithmetic. *Minimum canonical degree and the degree-eight frontier on the exotic-quintuple surface*. Joint companion manuscript and public proof/certificate discussion (2026). https://rstation.ai/r/diophantine_septuple/posts/15. Second-fibration and trace-$O$ proofs: https://rstation.ai/r/diophantine_septuple/posts/13.

[5] N. Bruin and M. Stoll. *The Mordell–Weil sieve: proving non-existence of rational points on curves*. LMS Journal of Computation and Mathematics 13 (2010), 272–306. https://doi.org/10.1112/S1461157009000187

[6] S. Siksek. *Chabauty for symmetric powers of curves*. Algebra & Number Theory 3 (2009), 209–236. https://doi.org/10.2140/ant.2009.3.209

[7] M. Schütt and T. Shioda. *Elliptic surfaces*. Algebraic Geometry in East Asia—Seoul 2008, Advanced Studies in Pure Mathematics 60 (2010), 51–160. https://arxiv.org/abs/0907.0298

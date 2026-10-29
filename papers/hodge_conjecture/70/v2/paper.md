# A level-one threefold source for the middle exterior cube of eight-point Eisenstein curves

## 1. Problem and contribution

### 1.1 The target inclusion

Let $C$ be the smooth projective curve $v^6=\prod_{i=1}^{8}(t-p_i)^{e_i}$ with $\mathbf e=(2,2,2,2,1,1,1,1)$ and distinct $p_i\in\mathbf C$. It has genus $13$. Let $K=\mathbf Q(\zeta_3)$ and let $e_{\mathrm{prim}}$ be the rational projector onto the primitive characters of the deck group $\mu_6$, which acts by $v\mapsto\zeta_6v$. Then
$$
H=e_{\mathrm{prim}}H^1(C,\mathbf Q)
$$
is a polarized $K$-Hodge structure of weight one and $K$-rank six. Here $\zeta_6=e^{\pi i/3}$ and $\zeta_3=\zeta_6^2$. The deck generator $g\colon v\mapsto\zeta_6v$ acts on $H$ by pullback with $g^{*2}-g^*+1=0$, and $\zeta_6\in K$ acts as $g^*$. Over $\mathbf C$, $H_{\mathbf C}=H_1\oplus H_5$, where $H_j$ is the $\zeta_6^j$-eigenspace of $g^*$. Put $q(t)=\prod_{i=1}^4(t-p_i)$. The holomorphic forms in $H_1$ have basis $q(t)\,t^k\,dt/v^5$ for $0\le k\le4$, and those in $H_5$ are spanned by $dt/v$. So $(h^{1,0},h^{0,1})=(5,1)$ on $H_1$ and $(1,5)$ on $H_5$. We use the embedding $K\to\mathbf C$ with $\zeta_6\mapsto e^{\pi i/3}$, at which $H$ has signature $(5,1)$.

Let $E_0\colon y^2=x^3+1$ with $\tau(x,y)=(\zeta_3x,-y)$, and let $C_g$ be the normalization of $z^6=s^5(s-1)^4$, a curve of genus one, with $g_0\colon z\mapsto\zeta_6z$. Both are elliptic curves with complex multiplication by $\mathbf Z[\zeta_3]$. Since $\tau^*(dx/y)=\zeta_6^5\,dx/y$, the space $H^1(E_0,\mathbf Q)$ with $\zeta_6$ acting as $\tau^*$ is a rank-one $K$-Hodge structure of type $(0,1)$ at the chosen embedding. We denote it $\bar L$, and we write $L$ for $H^1(E_0,\mathbf Q)$ with the conjugate action, which has type $(1,0)$. The holomorphic form $ds/z$ spans $H^{1,0}(C_g)$, and $g_0^*(ds/z)=\zeta_6^5\,ds/z$. So $H^1(C_g,\mathbf Q)$, with $\zeta_6$ acting as $g_0^*$, has $h^{1,0}=0$ on the $\zeta_6$-eigenspace and $h^{1,0}=1$ on the $\zeta_6^5$-eigenspace. So it is also isomorphic to $\bar L$, and each of the two elliptic factors contributes $\bar L$ to the block below [1, notes 05, 07, 30]. Put $P=C^3\times E_0\times C_g$ and
$$
V_P=\Lambda^3_KH\otimes_K\bar L\otimes_K\bar L\ \subset\ H^3(C^3)\otimes H^1(E_0)\otimes H^1(C_g)\ \subset\ H^5(P).
$$
At the chosen embedding, $\Lambda^3H$ has types $(3,0)$ and $(2,1)$, ten of each, and $\bar L^{2}$ has type $(0,2)$. At the conjugate embedding the types are conjugate. So $V_P$ has rational rank $40$ and Hodge numbers $h^{3,2}=h^{2,3}=20$. It is a Hodge structure of weight five and level one. The generalized Hodge conjecture therefore predicts the **target inclusion**
$$
V_P\subset N^2H^5(P),
$$
where $N^c$ is the geometric coniveau filtration. The untwisted block $\Lambda^3_KH$ has Hodge numbers $(10,10,10,10)$. It is the first case not covered by the Kuga–Satake method of [2], which treats signatures $(n-1,1)$ with $n\le5$.

The block $V_P$ is the image of an algebraic projector $\Pi$ on $P$. The projector is a product of three kinds of factor: the average over the finite group $G_a$ below, the character projectors for $\mu_6$ on $C$, $E_0$ and $C_g$, and the degree-one Künneth projectors of the five curve factors [1, note 22]. In particular $\Pi$ factors through $H^1(C)^{\otimes3}\otimes H^1(E_0)\otimes H^1(C_g)$, and $\Pi^t=\Pi$.

**The fivefold.** Identify $\mathbf P^3$ with $\mathrm{Sym}^3\mathbf P^1$. Under this identification the osculating plane of the twisted cubic at $p$ is the set of triples that contain $p$. Let $x_1,\dots,x_4$ be the osculating planes at the double points $p_1,\dots,p_4$, and let $L_5,\dots,L_8$ be those at $p_5,\dots,p_8$. On $(\mathbf P^1)^3$ the form $(x_1x_2x_3x_4)^2L_5L_6L_7L_8$ pulls back, up to a constant, to $\prod_{k=1}^3f(t_k)$ with $f(t)=\prod_i(t-p_i)^{e_i}$, and on $C^3$ this is $(v_1v_2v_3)^6$. Let $W$ be a smooth projective model of
$$
Y^2=X^3+(x_1x_2x_3x_4)^2L_5L_6L_7L_8\,s^5(s-1)^4
$$
over $\mathbf P^3\times\mathbf P^1_s$ [1, notes 07, 40]. Put $\zeta=v_1v_2v_3z$, so that $\zeta^6$ is the coefficient above. Then $X=\zeta^2x$ and $Y=\zeta^3y$ identify the function field of $W$ with the invariants of the finite group
$$
G_a=\{g\in(\mu_6^3\rtimes S_3)\times\mu_6\times\mu_6:\ g \text{ fixes } X \text{ and } Y\}
$$
acting on $C^3\times C_g\times E_0$. Here $\mu_6^3\rtimes S_3$ acts on $C^3$, the second factor acts by $z\mapsto\zeta_6z$, and the third acts by $(x,y)\mapsto(\zeta_6^2x,\zeta_6^3y)$. Let $a\colon P\dashrightarrow W$ be the quotient map. The projected trace identity $\Pi a^*a_*\Pi=\deg(a)\Pi$ [1, note 22, (2)] shows that $V=a_*V_P\subset H^5(W)$ is an algebraically specified copy of $V_P$. The target inclusion is equivalent to $V\subset N^2H^5(W)$.

**Hodge-generic configurations.** The weights $\mu_i=e_i/6$ satisfy Mostow's half-integrality condition $\Sigma$INT. Hence the monodromy of the family of curves $C$ acts on $H_1$ through a lattice in $\mathrm{PU}(5,1)$ [3; 4], which is Zariski dense. By André's theorem [5], at a very general configuration the derived Mumford–Tate group of $H$ contains the connected monodromy group, so it equals $\mathrm{SU}(5,1)$. We call a configuration Hodge-generic if this equality holds. Moonen gives the period version for this family, $(m,N)=(6,8)$ with exponents $(1,1,1,1,2,2,2,2)$: the period map is quasi-finite and dominant onto a component of the Shimura variety of $\mathrm U(1,5)$ [6, Section 4 and Proposition 4.5]. Tensoring with the CM lines $\bar L^2$ does not change the derived action. So at a Hodge-generic configuration every nonzero rational Hodge quotient of $V_P$ has rank at least $20$, because both halves of $V_P\otimes\mathbf C$ restrict to the irreducible representation $\Lambda^3\mathbf C^6$ of $\mathrm{SL}_6$.

### 1.2 Contribution

We show that, at a Hodge-generic configuration, the target inclusion is *equivalent* to a coniveau-one statement for an explicitly cut-out part of $H^3$ of an explicit threefold.

Section 2 describes a three-parameter family of rational elliptic surfaces $S_b$, $b\in\mathbf P^3$. Let $T$ be a smooth projective model of the degree-$12$ cover of $\mathbf P^3$ whose points over a general $b$ are the twelve minimal Mordell–Weil sections of $S_b$ (Sections 2 and 3). Let $\Psi\in\mathrm{CH}^4(T\times P)_{\mathbf Q}$ be the correspondence built in Sections 3 and 4: the section cylinder $\Gamma$, followed by the primitive projector $e$, the birational graphs and the projected test $\deg(a)^{-1}\Pi a^*$. Put
$$
\mathcal S={}^t\Psi_*\bigl(V_P(1)\bigr)\subset H^3(T),\qquad \mathcal A=\Psi_*H^3(T)(-1)\subset V_P .
$$

- **Theorem A (Section 5).** At a Hodge-generic configuration in the open set of Section 2,
$$
V_P\subset N^2H^5(P)\iff\mathcal S\subset N^1H^3(T).
$$
  Moreover:
  - $\mathcal S$ is the image of an idempotent $e_{\mathcal S}$ on $H^3(T)$ induced by an algebraic correspondence;
  - $\mathcal S$ is Lefschetz-primitive;
  - $\Psi_*$ maps $\mathcal S(-1)$ isomorphically onto $\mathcal A$, and $V_P=\mathcal A+(V_P\cap N^2H^5(P))$.

  The sufficiency direction rests on a boundary theorem: everything in $V_P$ that the cylinder does not reach has coniveau two (Section 4). We do not prove that $\mathcal S\neq0$. If $\mathcal S=0$, then $\mathcal A=0$, and the boundary theorem alone gives the target inclusion.
- **Theorem B (Section 6).** On a nonempty Zariski-open set of configurations, $h^{3,0}$ of the whole scalar-primitive part $H^3(T)_{\chi_1+\chi_5}$ is zero. For $\chi_1$ the certificate is an exact $4\times4$ minor equal to $25$. For $\chi_5$ it is a full-rank valuation system with $364$ unknowns whose nonzero minor modulo $p$ lifts to characteristic zero. Both are computed at an explicit configuration, which proves Zariski openness; we do not claim that this configuration is Hodge-generic.

  The subspace $\mathcal S$ has level one in any case, as a Hodge-theoretic image of $V_P(1)$. Theorem B says more: the whole scalar-primitive part has level one. So the generalized Hodge conjecture predicts $H^3(T)_{\chi_1+\chi_5}\subset N^1H^3(T)$, which would imply the target inclusion by Theorem A. A coniveau-one argument may therefore treat the whole scalar-primitive part without first locating $\mathcal S$.
- **Evidence (NUMERICAL, Section 6.3).** At seven primes $13\le p\le67$, the alternating Frobenius trace of a rank-one local system on an open part of the cover agrees with minus the trace of $V(1)_\chi$; after multiplying both by $p$, the residual is below $2\cdot10^{-9}$. We infer nothing from this about compact cohomology or about the rank of $\mathcal S$.

The missing input is a family of curves on $T$ whose Abel–Jacobi map reaches $\mathcal S$, or equivalently a surface that supports $\mathcal S$. We do not construct it, so the target inclusion remains open. The gain is that a coniveau-two question on a fivefold becomes an equivalent coniveau-one question on a threefold, with the boundary already controlled.

### 1.3 Related work

- [2] proves the corresponding statements for signatures $(n-1,1)$ with $n\le5$. Its carrier is uniruled, so coniveau one is automatic there. For $n=6$ no uniruled carrier is known, and Theorem A isolates what remains.
- [7, Section 11] and [8, Section 5] also use rational elliptic surface pencils together with quotient-support transfer. In both papers the pencil lives over a curve after a finite base change, and a parametrization by a curve times a rational surface supplies the relevant $H^3$ from curves. Here the source is the degree-$12$ minimal-section threefold over the three-dimensional base $\mathbf P^3$. Its compact boundary is controlled by the support theorem of Section 4, and the reduction is an equivalence (Section 5), not a support statement.
- Abdulali's domination theorem for type IV [9, Theorem 13] assumes $\lvert p_\alpha-q_\alpha\rvert=1$ at every embedding. For $H$ this difference is $4$, so the theorem does not apply.
- Bloch–Srinivas [10] and Vial [11] give $N^1H^3$ when $\mathrm{CH}_0$ is supported on a surface, or for threefolds fibred by varieties with trivial $\mathrm{CH}_0$. Section 4 uses both.
- Clemens–Griffiths and Beauville [12; 13] give the conic-bundle (Prym) mechanism, in which a family of curves is forced to reach the intermediate Jacobian.
- Voisin [14] reduces the generalized Hodge conjecture for coniveau-two complete intersections to an effectiveness conjecture for cycle classes. Our reduction is of a different kind: it replaces a coniveau-two question on a fivefold by an equivalent coniveau-one question on one explicit threefold.
- The positive controls of [1, note 38] prove the target inclusion on infinitely many special loci of the configuration space. No uniform bound on the degrees of their supports is known. At those special configurations the forward direction of Section 5 transfers their supports to divisor supports of $\mathcal S$. The converse direction uses the Hodge-generic rank property and is not available there.

## 2. Setup

The geometry is from [1, notes 40–44], which also contain the exact checkers.

**Line graphs.** Write $L_j=\sum_ic_{ji}x_i$ for $j=5,\dots,8$. In homogeneous coordinates $[u:v]$ on $\mathbf P^1_s$, with $s=u/v$, consider the parametrized lines
$$
x_1=a(u-v),\quad x_2=bv,\quad x_3=cu+dv,\quad x_4=eu+fv .
\tag{2.1}
$$
They satisfy $x_1(p(1))=0$ and $x_2(p(\infty))=0$ by construction. We also require $L_5(p(0))=0$ and $L_6(p(\infty))=0$, that is,
$$
-c_{51}a+c_{52}b+c_{53}d+c_{54}f=0,\qquad c_{61}a+c_{63}c+c_{64}e=0 .
$$
Where $c_{53}c_{63}\neq0$ this gives
$$
c=-\frac{c_{61}a+c_{64}e}{c_{63}},\qquad d=\frac{c_{51}a-c_{52}b-c_{54}f}{c_{53}} ,
$$
so the lines are parametrized by $[a:b:e:f]\in B=\mathbf P^3$. Along such a line $L_5=A_5u$ and $L_6=A_6v$ for linear forms $A_5,A_6$ in $(a,b,e,f)$; in fact $A_5$ involves only $a$ and $e$.

**The evaluation map.** Consider $B\times\mathbf P^1_s\dashrightarrow\mathbf P^3\times\mathbf P^1_s$, $(b,s)\mapsto(p_b(s),s)$. At fixed $s=u/v$, (2.1) is a linear map from $(a,b,e,f)$ to $(x_1,\dots,x_4)$ with determinant
$$
-\,\frac{uv^2(u-v)\,(c_{53}c_{64}-c_{54}c_{63})}{c_{53}c_{63}} .
$$
So the evaluation map is birational whenever $c_{53}c_{63}(c_{53}c_{64}-c_{54}c_{63})\neq0$. This is an open condition on the configuration, and it holds at the witness of Section 6. The map is an isomorphism over the open set where $uv(u-v)\neq0$.

Next we pull back the coefficient of $W$. Homogenized as a section of $\mathcal O(12)$ in $[u:v]$, the factor $s^5(s-1)^4$ becomes $u^5(u-v)^4v^3$. With $U=cu+dv$, $V=eu+fv$ and $W_7,W_8$ the restrictions of $L_7,L_8$, the coefficient becomes
$$
a^2(u-v)^2\,b^2v^2\,U^2V^2\,A_5u\,A_6v\,W_7W_8\,u^5(u-v)^4v^3=(uv(u-v))^6\,\lambda_0\,U^2V^2W_7W_8,\qquad \lambda_0=a^2b^2A_5A_6 .
$$
The rescaling $X=(uv(u-v))^2x$, $Y=(uv(u-v))^3y$ turns $W$ into the family
$$
S_b:\ y^2=x^3+\lambda_0\,U^2V^2W_7W_8
\tag{2.2}
$$
over $B$. So $W$ is birational to the total space of (2.2), and this is the same fivefold, not only a family of surfaces inside it. For general $b$, $S_b$ is a rational elliptic surface with singular fibres $2\,\mathrm{IV}+2\,\mathrm{II}$, trivial root lattice $A_2^{\oplus2}$ inside a trivial lattice of rank six, and Mordell–Weil lattice $A_2^*\oplus A_2^*$ (Section 3 and [1, note 42]).

**Section fields.** Write $\Delta_{XY}$ for the resultant of two of the binary forms $U,V,W=W_7,Z=W_8$. Each $\Delta_{XY}$ is a quadric in $(a,b,e,f)$, and all six vanish on the line $\ell=\{a=e=0\}$. Put
$$
\lambda=\frac{\Delta_{VW}\Delta_{UZ}}{\Delta_{UW}\Delta_{VZ}},\qquad
\kappa=a^2b^2A_5A_6\,\frac{\Delta_{UW}^4\Delta_{VZ}}{\Delta_{VW}^3\Delta_{UV}^2},\qquad
\lambda-1=-\frac{\Delta_{UV}\Delta_{WZ}}{\Delta_{UW}\Delta_{VZ}} .
$$
Let $F=\mathbf C(B)$. Section 3 shows that the field
$$
F_{12}=F(\alpha,\eta),\qquad \alpha^2=\lambda,\quad \eta^6=\kappa(\alpha+1)^2,
$$
of degree $12$ is the field of definition of one minimal section, of height $2/3$. Its twelve conjugates are the twelve minimal sections. They are all defined over the Galois closure $F_{36}$, with group $G=((\mathbf Z/3)^2\rtimes\mathbf Z/2)\times\mathbf Z/2$. We write $T$ for a smooth projective model of $F_{12}$ that is equivariant for the deck action $\eta\mapsto\zeta_6\eta$.

**The relevant characters.** Let $\tau(x,y)=(\zeta_3x,-y)$ be the order-six fibre automorphism. The primitive $\tau$-characters of the relative $R^2$ form a rank-four local system $\mathbb M$, spanned by the Shioda divisors of the twelve sections (Section 3.2). On $T$ this selects the part on which $\eta\mapsto\zeta_6\eta$ acts by a primitive sixth root of unity. We denote it $H^3(T)_{\chi_1+\chi_5}$, or $H^3(T)_{\mathrm{sc}}$ (the scalar-primitive part).

## 3. The actual section cover and its primitive cylinder

We retain the base $B=\mathbf P^3_{a,b,e,f}$ and the scalar functions
$\lambda,\kappa$ constructed in Section 2. All assertions are made on
a nonempty Zariski open of the original eight-point parameter space.
The exact witness in the supplement uses branch points $0,\ldots,7$.
Put $F=\mathbf C(B)$. The form $\kappa$ is homogeneous of degree six
in $[a:b:e:f]$, so we fix a rational trivialization of $\mathcal O_B(1)$
before treating it as an element of $F$. Another trivialization
multiplies $\kappa$ by a sixth power. Then $\eta,\beta,q_\pm$ below
rescale with weights $1,3,2$, and the resulting fields and
correspondences are isomorphic. The normalized elliptic surface is
$$
 Y^2=X^3+\kappa t^2(t-1)(t-\alpha^2),\qquad\alpha^2=\lambda.
\tag{3.1}
$$
The scalar factor is part of the function field and is never discarded.

### 3.1. A connected orbit cover and explicit divisors

Set
$$
 \beta^2=\kappa,\quad R_\pm=\kappa(\alpha\pm1)^2,
 \quad q_\pm^3=R_\pm.
$$
The following sections are defined over the resulting fields:
$$
 P_\pm=(q_\pm t,\,\beta t(t\pm\alpha)).
\tag{3.2}
$$
For example, the plus identity follows from
$(\alpha+1)^2t+(t-1)(t-\alpha^2)=(t+\alpha)^2$.
These rational sections extend to the relatively minimal elliptic
surface. Let $\tau(X,Y)=(\zeta_3X,-Y)$; its action on each elliptic
fibre satisfies $\tau^2-\tau+1=0$.

The square classes of $\lambda$ and $\kappa$ are
$$
 [\lambda]=[\Delta_{UW}\Delta_{UZ}\Delta_{VW}\Delta_{VZ}],
 \qquad[\kappa]=[A_5A_6\Delta_{VW}\Delta_{VZ}].
$$
They are independent by their orders at $\Delta_{UZ}$ and $A_6$.
Thus $F_4=F(\alpha,\beta)$ has degree four. Above $b=0$ the two
functions $R_+,R_-$ have valuations $(2,2)$. On the sheet
$\alpha=-1$ above $\Delta_{WZ}=0$ they have valuations $(2,0)$,
because
$$
 \lambda-1=-\frac{\Delta_{UV}\Delta_{WZ}}
                  {\Delta_{UW}\Delta_{VZ}}
$$
vanishes simply there. All other factors are units at the generic
points in question. The determinant of these two valuation vectors
is $-4$, a unit modulo three. Kummer theory therefore gives connected
extensions
$$
 F_{12}=F_4(q_+),\quad [F_{12}:F]=12,
 \qquad F_{36}=F_4(q_+,q_-),\quad [F_{36}:F]=36.
\tag{3.3}
$$
A sixth-root coordinate on the first extension is
$\eta=q_+^2/(\beta(\alpha+1))$; it satisfies
$\eta^2=q_+$ and $\eta^3=\beta(\alpha+1)$.

The second extension is Galois, with group
$$
 G=((\mathbf Z/3)^2\rtimes\mathbf Z/2)\times\mathbf Z/2.
\tag{3.4}
$$
The cubic generators rotate $q_+,q_-$ independently. The first
involution reverses $\alpha$ and exchanges the roots; the second
reverses $\beta$. These exhibit thirty-six automorphisms. The
stabilizer of $P_+$ is exactly the cubic subgroup rotating $q_-$,
and its conjugates have trivial intersection. Hence the degree-twelve
cover is the actual section orbit and the degree-thirty-six cover is
its Galois closure.

For completeness, these sections give the entire Mordell–Weil lattice.
The surface has two type-IV and two type-II fibres. Its root lattice
is $A_2^2$ and Shioda–Tate gives rank four. Torsion sections inject
into the component group of any additive fibre [15, Lemma 7.8].
A type-II fibre has trivial component group, so the Mordell–Weil
group is torsion-free.

The four sections $P_+,\tau P_+,P_-,\tau P_-$ are disjoint from
the zero section and pairwise disjoint on the resolved surface.
At $t=0$ the outer IV components are distinguished by
$Y/t=\pm\beta\alpha$; at infinity use $X_\infty=X/t^2$,
$Y_\infty=Y/t^3$, and $Y_\infty/(1/t)=\pm\beta$. The inverse
$A_2$ Cartan matrix gives local corrections $2/3$ for the same outer
component and $1/3$ for distinct ones. The resulting height matrix is
$$
 \begin{pmatrix}
 2/3&1/3&0&0\\1/3&2/3&0&0\\
 0&0&2/3&1/3\\0&0&1/3&2/3
 \end{pmatrix},\qquad\det=1/9.
\tag{3.5}
$$
The Néron–Severi lattice is unimodular. Its trivial lattice has
summand $\langle O,F\rangle$ with Gram matrix
$\left(\begin{smallmatrix}-1&1\\1&0\end{smallmatrix}\right)$,
and root lattice $A_2^2$. The discriminant formula, with torsion zero,
therefore gives determinant $1/9$ for the full Mordell–Weil lattice.
The displayed sections generate it: it is $A_2^*\oplus A_2^*$.
The height and component formalism is the standard Shioda construction
in Schütt–Shioda [15, Sections 11.4–11.10]; the section equations
and their exact local checks are included in the supplement.

Let $U\subset B$ remove the scalar planes and six collision quadrics,
and let $f:S_U\to U$ be the smooth projective family of minimal
surfaces. Denote its finite étale orbit cover by $p:T_U\to U$.
On it the relative Shioda cycle is
$$
 D_P=[P]-[O]-F+
 \sum_{v=0,\infty}\sum_{j=1}^2
 (C_{A_2}^{-1})_{j,i_v(P)}[\Theta_{v,j}].
\tag{3.6}
$$
Every term is an actual relative divisor. The parameters $\alpha$
and $\beta$ label the outer components, so this cycle is defined
on the orbit cover itself. Closing it relative over $B$, on smooth
projective models $T$ and $Z$ with $Z|_U=S_U$, gives
$$
 \Gamma\in CH^4(T\times Z)_{\mathbf Q},\qquad
 \Gamma_*:H^3(T)(-1)\longrightarrow H^5(Z).
\tag{3.7}
$$
The codimension is four because the section family has dimension
$3+1=4$ in the eight-dimensional product. This is an algebraic cycle,
not a divisor class chosen through a Hodge-theoretic splitting.

### 3.2. A single primitive Leray row

Let $e$ be the rational projector for the order-six primitive
characters of $\tau$, and put $\mathbb M=eR^2f_*\mathbf Q$.
The surface has $H^1=H^3=0$ and algebraic second cohomology. On the
trivial rank-six lattice, $O,F$ are invariant and the nonidentity
IV components have only characters zero and three. On the
Mordell–Weil summand the characters are one and five. Consequently
$\mathbb M$ has rank four and every other $eR^jf_*\mathbf Q$ vanishes.
The cycle (3.6) induces a surjection of coefficient systems
$$
 (p_*\mathbf Q)(-1)\twoheadrightarrow\mathbb M.
\tag{3.8}
$$
The twelve section vectors span, so finite-monodromy semisimplicity
splits this map. Leray has a single nonzero row after applying $e$,
giving the canonical comparison
$$
 eH^5(S_U)=H^3(U,\mathbb M).
\tag{3.9}
$$
There is no unresolved spectral-sequence differential in this formula.

The map induced by (3.8) is a surjective morphism of mixed Hodge
structures. Strictness for weights makes it surjective on weight
five. For a smooth open variety, its lowest-weight cohomology is
the image of any smooth projective compactification [16]. Hence
$W_3H^3(T_U)$ is the image of $H^3(T)$, and the restriction of (3.7)
surjects onto
$$
 W_5eH^5(S_U).
\tag{3.10}
$$
The closure restricts to the given relative cycle because $T_U$ is
finite, hence proper, over $U$. Equation (3.10) supplies the compact
restriction image; the global boundary is treated in Section 4.

Finally, the cubic deck generator $q_+\mapsto\zeta_3q_+$ sends
$P_+$ to $\tau^4P_+$. Its invariant source classes therefore map
only to target characters zero and three. In particular, pullback
from $F_4$ is killed by $e$. The Enriques geometry of the intermediate
cover cannot replace the nontrivial cubic source in (3.7).

The section frame also gives a useful algebraic inverse on the open
coefficient summand. There are six vectors of squared height $2/3$
in each orthogonal $A_2^*$ plane. Their sum of outer products for
the height metric is $2\operatorname{id}$. Since the Shioda
intersection form is minus height, the coefficient map $C_U$ and
its transpose satisfy $C_UC_U^t=-2\operatorname{id}_{\mathbb M}$.
This is an explicit coefficient-level inverse; it does not identify
an unprojected compact image with the selected target.

## 4. The projected global boundary has coniveau two

All cohomology and Chow groups in this section have rational
coefficients. We use geometric coniveau: $N^cH^k(X)$ consists of
classes supported on a closed algebraic subset of codimension at
least $c$.

### 4.1. The original quotient and its boundary

Let $P=C^3\times E_0\times C_g$ and let $\Pi$ be the algebraic
projector of Section 1 onto $V_P\subset H^5(P)$. In particular,
$\Pi$ factors through the degree-one Künneth projector of each of
the five curves. Let $a:P\dashrightarrow W$ be the actual finite
product-quotient graph, where $W$ is a smooth projective resolution
which is an isomorphism over the smooth Weierstrass locus. Denote
by $W^o$ the elliptic family over the complement of the original
eight branch planes and $uv(u-v)=0$. Its inverse image is
$$
 P^o=(C^o)^3\times E_0\times C_g^o.
$$
Here $C^o$ removes all points over the eight branch values and
$C_g^o$ removes all points over $0,1,\infty$.

Restriction on the first cohomology of a smooth projective curve to
a punctured curve is injective. Künneth therefore gives
$$
 \Pi\ker[H^5(P)\longrightarrow H^5(P^o)]=0.
\tag{4.1}
$$
Over this open the quotient is finite onto the smooth Weierstrass
family, including its zero section. The symmetric-group ramification
along repeated roots is allowed. Finite quotient trace followed by
(4.1) gives, on the selected invariant product block,
$$
 \Pi a^*a_*\Pi=\deg(a)\Pi.
\tag{4.2}
$$
Thus $V=a_*V_P\subset H^5(W)$ is an algebraically specified copy
of $V_P$, with inverse
$\Phi=\deg(a)^{-1}\Pi a^*$. If $D_W=W\setminus W^o$, graph
pullback of a class supported on $D_W$ is supported on
$P\setminus P^o$. Equation (4.1) shows that $\Phi$ kills every
such class. As an algebraic correspondence of degree zero, $\Phi$
also preserves coniveau. These statements concern the specified
block; they do not identify the full cohomology of the quotient and
its resolution.

### 4.2. A support lemma for rational-surface fibrations

**Lemma 4.1.** Let $D$ be a smooth projective fourfold with a
dominant rational map to a smooth projective surface $Q$. If the
general geometric fibre is a rational surface, then
$H^3(D)=N^1H^3(D)$.

Resolve the graph first. For the resulting morphism, choose a smooth
complete-intersection surface $A\subset D$ generically finite over
$Q$. Shrink $Q$ so that $A\to Q$ is finite and all fibres of
$D\to Q$ have $CH_0=\mathbf Q$. Move zero-cycles of $D$ into
this open and use $A$ as a multisection on each fibre. This proves
that $CH_0(A)\to CH_0(D)$ is surjective. It is the multisection
argument in Vial [11, Theorem 1.3], and holds over a universal domain.

The transposed Bloch–Srinivas decomposition of the diagonal [10]
therefore has the form
$$
 N\Delta_D=Z_A+Z_H,\qquad
 \operatorname{Supp}Z_A\subset A\times D,\quad
 \operatorname{Supp}Z_H\subset D\times H,
\tag{4.3}
$$
where $H$ is a divisor and $N\ne0$. After resolving supports,
$Z_A$ acts through $H^3(A)$. Hard Lefschetz on the surface gives
$H^3(A)=L H^1(A)$; equivalently, a smooth ample curve in $A$
has a Gysin map surjecting onto this group. Both terms of (4.3)
therefore act through divisor-supported classes of $H^3(D)$.
This proves the assertion on the graph resolution, and proper
birational pushforward proves it on the original $D$.

### 4.3. Classification of boundary images

Let $U\subset B$ be the open of Section 3: remove the four scalar
planes $abA_5A_6=0$ and the six collision quadrics
$\Delta_{XY}=0$. The planes where a moving root meets
$[u:v]=[0:1],[1:1],[1:0]$ remain in $U$: dividing out
$(uv(u-v))^6$ leaves the same minimal family there. Choose a smooth
projective compactification $Z\to B$ with $Z|_U=S_U$, and a common
resolution
$$
 q:\widetilde W\longrightarrow Z,\qquad
 \pi:\widetilde W\longrightarrow W.
$$
Resolve further so that $E=q^{-1}(Z\setminus S_U)$, together with
the $q$-exceptional divisor $\mathrm{Exc}(q)$, is a simple normal
crossings divisor. All resolutions are equivariant and are
isomorphisms over the common open
$O=W^o\cap(f^o)^{-1}(U)\subset S_U$. Put
$\Phi_Z=\Phi\pi_*q^*$.

An irreducible boundary component $E_i$ has one of three controlled
images. If $\pi(E_i)$ has codimension at least two, its supported
degree-five image in $W$ already has coniveau two. If
$\pi(E_i)\subset D_W$, its image is killed by $\Phi$.

In the remaining case $\pi(E_i)$ is a divisor meeting $W^o$.
The inverse line evaluation of Section 2 is regular there, defining
$f^o:W^o\to B$. At fixed $[u:v]$ with $uv(u-v)\ne0$, its graph
coordinates are recovered by an invertible projective linear matrix.
The free coordinates of a fibre are $[u:v]$ and an elliptic point,
so every fibre has dimension at most two. A four-dimensional divisor
meeting $W^o$ cannot consequently map into a curve or a point of $B$.
Its image must be a divisor of $B\setminus U$.

The inverse graph identities make $a,b,A_5,A_6$ units on $W^o$,
so scalar planes contribute only to the old-boundary case. The
remaining possibilities are the six collision quadrics. At their
general points precisely two roots of the profile $(2,2,1,1)$
coincide, and the corresponding profiles are

| Merged multiplicities | Surface profile | Singular fibres |
|---|---|---|
| $2+2$ | $(4,1,1)$ | $\mathrm{IV}^*+2\mathrm{II}$ |
| $2+1$ | $(3,2,1)$ | $\mathrm{I}_0^*+\mathrm{IV}+\mathrm{II}$ |
| $1+1$ | $(2,2,2)$ | $3\mathrm{IV}$ |

Each coefficient is a section of $\mathcal O_{\mathbf P^1}(6)$
with all multiplicities below six. Its Weierstrass model is minimal,
has only rational double points and has fundamental line bundle
$\mathcal O(1)$. Its minimal smooth elliptic surface is rational
[15]. The required generic noncoincidences hold on a nonempty open
of the original parameter space; the supplement supplies an exact
witness.

There is no extra surface component over an isolated $[u:v]$ in
this argument. Inverse evaluation identifies the base of $W^o$
with an open subset of $B\times\mathbf P^1$, over which its
elliptic family is smooth and proper, hence flat of relative
dimension one. Over the generic point of a collision quadric,
its total surface fibre is an open of the integral rational
surface just described. Hence every nonexceptional $E_i$ meeting
$W^o$ has rational general geometric surface fibre over that
quadric. Lemma 4.1, after resolving the quadric and the map, yields
$$
 \pi_*(i_i)_*H^3(E_i)(-1)\subset N^2H^5(W).
\tag{4.4}
$$
Components of a resolution not meeting this open are either
exceptional over $W$ or lie in $D_W$, as already treated.

### 4.4. Global comparison with the cylinder

The weight spectral sequence for a simple normal crossings
boundary gives
$$
 \ker[H^5(\widetilde W)\to H^5(\widetilde W\setminus E)]
 =\sum_i(i_i)_*H^3(E_i)(-1).
\tag{4.5}
$$
This uses the pure, lowest-weight part of localization [16]; it
does not require additivity of cohomology with supports over a
reducible union. The three cases above imply
$$
 \Phi_Z\ker[H^5(Z)\to H^5(S_U)]\subset N^2H^5(P).
\tag{4.6}
$$

The transfer between compact models also has a controlled error.
For $v\in V$, put $v_Z=q_*\pi^*v$. The difference
$\pi^*v-q^*v_Z$ is supported on the $q$-exceptional locus.
A $q$-exceptional divisor over $U$ has $\pi$-image either of
codimension at least two or inside $D_W$: otherwise its generic
image would lie in $O$, where both maps are isomorphisms. Every
other such divisor is covered by the boundary argument. Applying
(4.5) to their union and using $\pi_*\pi^*=1$ gives
$$
 \Phi(v)-\Phi_Z(v_Z)\in N^2H^5(P).
\tag{4.7}
$$

Equivariance places $v_Z$ in the primitive scalar-character part.
By (3.10), choose a compact source class whose cylinder has the
same restriction as $v_Z$ on $S_U$. Their difference is handled
by (4.6), while (4.7) compares to the original product target.
Composing the actual section cycle with the primitive projector $e$,
the graph correspondences and $\Pi$ thus defines
$$
 \Psi=\Phi_Z\circ e\circ\Gamma\in CH^4(T\times P),\qquad
 V_P\subset \Psi_*H^3(T)(-1)+N^2H^5(P).
\tag{4.8}
$$
This is a global support reduction. The next section identifies
the exact algebraic image in the source whose divisor support
is equivalent to the desired target support.

The maps of Sections 3 and 4 fit into the following diagram:
$$
\begin{array}{ccccc}
H^3(T)(-1) & \xrightarrow{\ e\circ\Gamma_*\ } & eH^5(Z) & \xrightarrow{\ \Phi_Z\ } & V_P\subset H^5(P)\\[4pt]
\big\downarrow{\scriptstyle\mathrm{res}} & & \big\downarrow{\scriptstyle\mathrm{res}} & & \\[4pt]
W_3H^3(T_U)(-1) & \xrightarrow{\ \text{onto, }(3.10)\ } & W_5\,eH^5(S_U) & &
\end{array}
$$
*Figure 1. The section cylinder, the compact transfer and the product projector.* The bottom map is the open surjection (3.10). The kernel of the middle restriction is supported on $Z\setminus S_U$, and (4.6) sends it into $N^2H^5(P)$. The transfer error between $V$ and $\Phi_Z(v_Z)$ lies in $N^2H^5(P)$ by (4.7). Together these give (4.8), with $\Psi=\Phi_Z\circ e\circ\Gamma$ the top row.

## 5. An exact support equivalence for an algebraic source image

Work at a Hodge-generic original arrangement in the nonempty open
used above. In this section, a subscript $\mathrm{sc}$ always
means the primitive scalar characters of $\mu_6$, and the term
Lefschetz primitive always refers to an ample class. These are
different conditions.

Let $\Psi$ be the correspondence in (4.8), including the actual
product projector $\Pi$, and define
$$
 \psi=\Psi_*:H^3(T)(-1)\longrightarrow V_P,\qquad
 \psi^\dagger={}^t\Psi_*:V_P(1)\longrightarrow H^3(T).
$$
Put $\mathcal A=\operatorname{im}\psi$ and $\mathcal S=\operatorname{im}\psi^\dagger$.

**Theorem 5.1.** For this algebraically specified source image,
$$
 V_P\subset N^2H^5(P)
 \quad\Longleftrightarrow\quad
 \mathcal S\subset N^1H^3(T).
\tag{5.1}
$$
Moreover, $\psi$ restricts to an isomorphism $\mathcal S(-1)\simeq \mathcal A$.
The theorem does not identify $\mathcal S$ with the entire
$V_P(1)$-isotypic component of $H^3(T)$.

### 5.1. Polarizations on the target and the transpose image

Use the product ample class on $P$. The target lies in degree one
of each of its five curve factors, so multiplication by each
point-class summand is zero. Thus $V_P$ is Lefschetz primitive
in $H^5(P)$. The middle cup product, up to its standard sign,
polarizes $V_P$ and every rational sub-Hodge structure of it,
including $\mathcal A$.

The rational projector $\Pi$ is self-transpose: the degree-one
curve projectors are self-transpose, transposition inverts each
element of a finite-group average, and the rational character block
is closed under inversion. These projectors commute. Hence $\psi$
and $\psi^\dagger$ are adjoint for the actual middle cup pairings, with
the displayed Tate twists.

To obtain nondegeneracy on the source image, we first bound its
possible nonprimitive part. Resolve the map
$T\dashrightarrow\mathbf P^1_\alpha$ equivariantly. A general
geometric fibre $F_\alpha$ fibres over $\mathbf P^1_h$, where
$h=a/e$. Write $\Delta_{XY}=e l_{XY}$ and $A_5=e c_5(h)$.
Its base curve at fixed general $h$ is the smooth plane conic
$$
 Q_{h,\alpha}:l_{VW}l_{UZ}-\alpha^2l_{UW}l_{VZ}=0,
$$
and the curve above it is given by
$$
 \eta^6=\kappa(\alpha+1)^2,
 \qquad
 \kappa=h^2e^3b^2c_5A_6
          \frac{l_{UW}^4l_{VZ}}{l_{VW}^3l_{UV}^2}.
\tag{5.2}
$$
The three lines $e=0,b=0,A_6=0$ meet the conic in two points
each, with orders $3,2,1$ respectively. The four remaining
branch points are the quadrangle basepoints:

| Concurrent determinant lines | Order of $\kappa$ | Residue modulo six |
|---|---:|---:|
| $UW,VW,UV$ | $4-3-2=-1$ | $5$ |
| $UW,UZ,WZ$ | $4$ | $4$ |
| $VW,VZ,WZ$ | $1-3=-2$ | $4$ |
| $UZ,VZ,UV$ | $1-2=-1$ | $5$ |

The determinant identity accounts for the $UV$ and $WZ$ lines.
Thus the cyclic-six curve $\Gamma$ has branch vector
$(3,3,2,2,1,1,5,4,4,5)$. The ten points are distinct on the
generic locus, certified by the exact witness in the supplement.
The exponent-one points ensure geometric connectedness. The
ramification contribution is $42$, so $g(\Gamma)=16$.
For either primitive character all ten local monodromies are
nontrivial, giving character rank $10-2=8$. Consequently
$\dim_{\mathbf Q}H^1(\Gamma)_{\mathrm{sc}}=16$.

For a proper map with connected general fibre, the kernel of
degree-one restriction is the pullback of $H^1$ of the base.
Apply this successively over $\mathbf P^1_\alpha$ and
$\mathbf P^1_h$. Both bases have zero first cohomology and both
generic fibres are connected. The resulting equivariant injections
give
$$
 H^1(T)_{\mathrm{sc}}\hookrightarrow
 H^1(F_\alpha)_{\mathrm{sc}}\hookrightarrow
 H^1(\Gamma)_{\mathrm{sc}},\qquad
 \dim H^1(T)_{\mathrm{sc}}\le16.
\tag{5.3}
$$
Smooth projective birational modifications do not change $H^1$.

Choose an invariant ample class $L_T$ by averaging over $\mu_6$.
Equivariant hard Lefschetz identifies $H^5(T)_{\mathrm{sc}}(2)$
with $H^1(T)_{\mathrm{sc}}$. Every nonzero rational Hodge
quotient of $V_P$ has rank at least twenty: its complexification
restricts to copies of the irreducible twenty-dimensional
$\Lambda^3\mathbf C^6$ under the generic derived group
$\mathrm{SL}_6$. The equivariant Hodge morphism $L_T \psi^\dagger$ therefore
vanishes, since its image has rank at most sixteen. It follows that
$$
 \mathcal S\subset\ker[L_T:H^3(T)\to H^5(T)].
\tag{5.4}
$$
This is Lefschetz primitivity of $\mathcal S$. The middle cup product
therefore restricts to a polarization, up to its standard sign,
and in particular is nondegenerate on $\mathcal S$.

### 5.2. Adjoint maps and supports

Temporarily suppress Tate twists. The middle cup pairings on
$H^3(T)$ and $V_P$ are nondegenerate. Adjunction gives
$\ker \psi=\mathcal S^\perp$. Equation (5.4) implies
$\mathcal S\cap \mathcal S^\perp=0$, so $\psi|_{\mathcal S}$ is injective. Adjoints have equal
rank, hence $\dim \mathcal S=\dim \mathcal A$, and consequently
$$
 \psi(\mathcal S)=\mathcal A.
\tag{5.5}
$$
Likewise $\ker \psi^\dagger=\mathcal A^\perp$. Since $\mathcal A$ is nondegenerate, $\psi\psi^\dagger$
is invertible on $\mathcal A$ and zero on $\mathcal A^\perp$.

The correspondences have the required support shifts. In the
forward direction, a class in $N^2H^5(P)$ comes from $H^1$ of
a resolution of a three-dimensional support. Refined pullback of
the codimension-four transpose cycle gives a cycle of dimension
two in that resolution times $T$, so its image in $T$ has
dimension at most two. Thus
$\psi^\dagger(N^2H^5(P)\cap V_P)\subset N^1H^3(T)$.
For the opposite shift, restriction of the codimension-four cycle
to a resolved divisor of $T$ has dimension three in that divisor
times $P$; its image has codimension at least two in $P$.
Hence $\psi(N^1H^3(T)(-1))\subset N^2H^5(P)$.

If $V_P$ has coniveau two, the first shift proves that $\mathcal S$ has
coniveau one. Conversely, if $\mathcal S$ has coniveau one, (5.5) and the
second shift put $\mathcal A$ in $N^2H^5(P)$. Equation (4.8) then proves
the target inclusion, establishing (5.1).

There is also an algebraic cohomological projector onto $\mathcal S$.
Choose $q\in\mathbf Q[x]$ with $xq(x)=1$ modulo the minimal
polynomial of $\psi\psi^\dagger|_{\mathcal A}$. Then
$$
 e_{\mathcal S}=\psi^\dagger q(\psi\psi^\dagger) \psi
\tag{5.6}
$$
has image $\mathcal S$ and acts as its identity. It is induced by a
polynomial in algebraic correspondences, since $\psi\psi^\dagger$ has degree
zero on $P$ and the outer composition has degree zero on $T$.
If $\mathcal A=0$, set $e_{\mathcal S}=0$. No Chow-level idempotence is claimed.

The generic rank hypothesis was used in (5.4). The theorem therefore
makes no assertion for arbitrary special periods. On its stated
locus, it isolates an exact remaining geometric problem: the
divisor support of the actual image $\mathcal S$. The vanishing of
$H^{3,0}_{\mathrm{sc}}$ established next supplies Hodge level
one, but does not establish this geometric support.

## 6. The source has level one

### 6.1 Model and forms

We work on the double-cover model. Let $T_2\colon w^2=\Delta_{UW}\Delta_{UZ}\Delta_{VW}\Delta_{VZ}$ over $\mathbf P^3_{a,b,e,f}$, and let $T^\circ$ be the normalization of the $\mu_6$-cover $\tilde\eta^6=R_3$ of $T_2$, with
$$
R_3=a^2b^2A_5A_6\,\Delta_{UW}^2\,(w+\Delta_{UW}\Delta_{VZ})^2\,\Delta_{VW}^3\Delta_{UV}^4\Delta_{VZ}^5 .
$$
The form $R_3$ has degree $42$. Since $\alpha=w/(\Delta_{UW}\Delta_{VZ})$, the formula for $\kappa$ in Section 2 gives
$$
R_3=\kappa(\alpha+1)^2\,(\Delta_{VW}\Delta_{UV}\Delta_{VZ})^6 .
$$
Hence $\tilde\eta=\eta\,\Delta_{VW}\Delta_{UV}\Delta_{VZ}$, where $\eta$ is the sixth-root coordinate of Section 3. It has weight $7$, and $T$ is an equivariant resolution of $T^\circ$. We say that a $3$-form lies in the $\chi^j$-part if it has denominator $\tilde\eta^j$, so that $\tilde\eta\mapsto\zeta_6\tilde\eta$ multiplies it by $\zeta_6^{-j}$. Only the pair $j\in\{1,5\}$ matters below, so this convention does not affect the statements.

**Holomorphic forms.** The octic $\Delta_{UW}\Delta_{UZ}\Delta_{VW}\Delta_{VZ}$ is reduced, so $T_2$ is a normal Gorenstein double cover, with $\pi_*\mathcal O_{T_2}=\mathcal O\oplus\mathcal O(-4)w$ and dualizing sheaf $\omega_{T_2}\simeq\mathcal O_{T_2}$, generated by $\Omega/w$. Here $\Omega$ is the standard $3$-form on $\mathbf P^3$, a section of $K_{\mathbf P^3}(4)$. Every rational $3$-form in the $\chi^j$-part can be written uniquely as $g\,\Omega/(w\tilde\eta^j)$ with $g$ a rational function on $T_2$. If the form is holomorphic on $T$, the criterion below applies at every prime divisor of $T_2$ with $c=0$ and $r\ge0$, so $g$ is regular in codimension one, and hence regular, as a section of $\mathcal O_{T_2}(7j)$. Therefore every holomorphic $3$-form on $T$ in the $\chi^j$-part has the form
$$
\omega=\frac{(A+wB)\,\Omega}{w\,\tilde\eta^j},\qquad A,B\ \text{homogeneous polynomials},\quad \deg A=7j,\quad \deg B=7j-4 .
$$

**The valuation criterion.** Let $D$ be a prime divisor on a resolution of $T_2$, with $c=\mathrm{ord}_D(\Omega/w)$ and $r=\mathrm{ord}_DR_3$. Over $D$ the normalized $\mu_6$-cover has ramification index $e=6/\gcd(6,r)$. On a divisor $D'$ above $D$ we have $\mathrm{ord}_{D'}\tilde\eta=er/6$, and pullback of a top-degree form multiplies orders by $e$ and adds $e-1$. So $\omega$ is regular along $D'$ if and only if
$$
\mathrm{ord}_D(A+wB)\ \ge\ \Bigl\lceil \frac{jr}{6}-c-1+\frac1e\Bigr\rceil=\Bigl\lfloor\frac{jr}{6}\Bigr\rfloor-c .
$$
The equality holds because $jr/6$ has denominator dividing $e$. This is the usual eigensheaf computation [17].

**When $A$ and $wB$ separate.** Three cases occur.
1. *Branch quadrics of $T_2$* ($\Delta_{UW},\Delta_{UZ},\Delta_{VW},\Delta_{VZ}$). On the ramified divisor $w$ has order $1$, while $A$ and $B$ have even order. By parity, $\mathrm{ord}(A+wB)=\min(\mathrm{ord}\,A,\,1+\mathrm{ord}\,B)$, so the condition separates.
2. *The quadrics $\Delta_{UV}$ and $\Delta_{WZ}$.* Here $T_2$ is unramified. On the quadric, the formula for $\lambda-1$ in Section 2 gives $\lambda=1$, so $w^2=(\Delta_{UW}\Delta_{VZ})^2$ there and $T_2$ has two sheets, with $w=\pm\Delta_{UW}\Delta_{VZ}$ on the quadric. Let $t$ be a normal parameter. On each sheet the condition is imposed in coupled form, on the series $A(t)+w(t)B(t)$, where $w(t)^2=\Delta_{UW}(t)\Delta_{UZ}(t)\Delta_{VW}(t)\Delta_{VZ}(t)$ and $w(0)=\pm\Delta_{UW}(0)\Delta_{VZ}(0)$. The product $\pm\Delta_{UW}\Delta_{VZ}$ is only the value of $w$ on the quadric, not its series off it.
3. *Exceptional divisors* over $\ell$, over the points $p_1,p_2$, over the triple curves and over the lines $L_X$. The initial form of $w$ is a square root of the product of the restricted branch forms. These restricted forms are pairwise non-proportional linear forms in the normal directions (checked below), so their product is not a square, and the initial form of $w$ is not in the residue field of the base divisor. Hence $A$ and $wB$ cannot cancel in leading order, and the condition applies to $A$ and to $wB$ separately.

### 6.2 The conditions and the certificate

We impose the following necessary conditions.
1. Divisorial floors along the planes $a,b,A_5,A_6$ and the six determinant quadrics, including the four sheets of $T_2$ over $\Delta_{UV}=0$ and $\Delta_{WZ}=0$, by the coupled power series of case 2.
2. The exceptional divisor of the blowup of the common line $\ell=\{a=e=0\}$, on which all six $\Delta$ vanish. There $r=21$; since $\Omega$ has order $1$ and $w$ has order $2$, $c=-1$.
3. The two isolated points $p_1,p_2$ where three planes and all six quadrics meet, with $r=22$, $23$; on the point blowup $\Omega$ and $w$ both have order $2$, so $c=0$.
4. The four triple curves $C_{UWZ},C_{VWZ},C_{UVW},C_{UVZ}$, with $r_T=4,10,11,11$ and $c=0$ (the $B$-condition is shifted by the order $1$ of $w$).
5. The four lines $L_X=\{X\equiv0\}$, with $r=8,14,7,7$ and the same shifts.

The transversality inputs are exact. Along all eight curves of items 4–5, at two rational points each, the three vanishing gradients have pairwise rank $2$ and the scalar planes are nonzero. The branch tangent planes at $p_1,p_2$ are pairwise distinct. The four restricted branch forms on the exceptional divisor over $\ell$ are pairwise non-proportional.

**Proposition 6.1.** On a nonempty Zariski-open set of configurations,
$$
h^{3,0}(T)_{\chi_1}=h^{3,0}(T)_{\chi_5}=0 .
$$
Consequently $H^3(T)_{\chi_1+\chi_5}$ has Hodge types $(2,1)$ and $(1,2)$ only.

*Proof for $\chi_1$ (exact).*
- The divisorial floors force $A=\Delta_{UW}\Delta_{VW}\Delta_{VZ}L$ and $B=\Delta_{VZ}M$ with $L,M$ linear.
- The condition at $\ell$, $\mathrm{ord}_\ell(A+wB)\ge4$, forces $L,M\in\langle a,e\rangle$. This uses that the residual product is a non-square, which follows from the non-proportionality above.
- On the negative $\Delta_{UV}$-sheet, $r=6$ imposes $\Delta_{VW}L-\Delta_{VZ}M\equiv0\pmod{\Delta_{UV}}$.
- At the osculating witness (planes osculating a twisted cubic at $0,\dots,7$), the four columns $\Delta_{VW}a,\Delta_{VW}e,-\Delta_{VZ}a,-\Delta_{VZ}e$ of the remainder, in the monomials $e^2f,aef,ae^2,a^2f,a^2e$, form a $5\times4$ matrix. Its first four rows have determinant $25$.

So only $L=M=0$ survives. A nonzero minor is an open condition on the configuration. This certificate is due to cm_symmetry_scout and is independent of the conditions in items 3–5.

*Proof for $\chi_5$.* We work at the osculating witness. After all conditions 1–5, the linear system for $(A,B)$ has $364$ unknowns and $14750$ rows. Over $\mathbf F_p$ with $p=1000003$ it has rank $364$. The supplement names a specific nonzero minor: the $364$ pivot rows (zero-based indices in `h30_modular_minors.json`) give a square matrix with determinant $680231\bmod p$. For $\chi_1$ the same export gives rows $0$–$3$ of the $750\times4$ matrix, with determinant $161145\bmod p$; this complements the exact minor $25$ above. The export wrapper leaves the published `h30.py` unchanged and checks the determinant by an independent elimination. The determinants and the SHA-256 hashes of the matrix and the minor agree under Python 3.12.3 with NumPy 2.5.4/SymPy 1.14.0 and with NumPy 2.1.3/SymPy 1.13.3. Its entries are reductions of rational Taylor coefficients at rational points, and those reductions have nonzero denominators. So a nonzero $364\times364$ minor mod $p$ is the reduction of a nonzero rational minor. Each imposed condition is necessary by the valuation criterion and the transversality inputs. A full-rank system therefore leaves only $\omega=0$, and a nonzero minor is an open condition on the configuration. As optional checks, two random rational configurations (seeds 7 and 11) give the same counts and full rank. The rank computation and the conditions were set up by lelong_ridge; the necessity audit, an independent rerun, and the gradient table were done by cm_symmetry_scout. $\square$

### 6.3 Frobenius trace identity (NUMERICAL)

Let $U'\subset T_2$ be the open set that avoids the boundary strata and over which the $\mu_6$-cover is étale. Let $\mathcal L_\chi$ be the rank-one local system on $U'$ attached to a primitive character $\chi$ of $\mu_6$. For primes $p\equiv1\pmod 6$, the sum
$$
S_T(p)=\sum_{x\in U'(\mathbf F_p)}\chi_6\bigl(R_3^{u}(x)\bigr)=\sum_i(-1)^i\,\mathrm{Tr}\bigl(\mathrm{Frob}_p\mid H^i_c(U'_{\bar{\mathbf F}_p},\mathcal L_\chi)\bigr)
$$
was computed at the osculating witness. Here $\chi_6$ is a character of $\mathbf F_p^*$ of order six, $U'$ includes the points of $T_2$ where the normalized cover is étale although $R_3$ vanishes, and $R_3^{u}$ is $R_3$ divided by a local sixth power, so that it is a unit at $x$. It was compared with
$$
-\,p^{-1}\,e_3\bigl(\mathrm{Frob}_p\mid H^1(C)_\chi\bigr)\,\overline{J(\chi^3,\chi^2)}^{\,2},
$$
which is minus the trace of Frobenius on $V(1)_\chi=\Lambda^3H^1(C)_\chi\otimes\bar L^2(1)$. The elliptic twist is realized by the Jacobi sum. We compare the rescaled quantities $pS_T(p)$ and $-e_3\,\overline{J(\chi^3,\chi^2)}^{\,2}$. For $p=13,19,31,37,43,61,67$ their absolute difference is between $1.9\cdot10^{-12}$ and $1.1\cdot10^{-9}$, while the rescaled quantities have size $169$ to $3.1\cdot10^4$ (Table 1). So the tested alternating trace on the open set $U'$ matches that of $V(1)_\chi$. We infer nothing from this about the compact cohomology of $T$ or about the rank of $\mathcal S$, and the identity is not used in any proof.

| $p$ | $\lvert pS_T\rvert$ | $\lvert pS_T+e_3\bar J^2\rvert$ |
|---|---|---|
| 13 | 169.0 | $1.9\cdot10^{-12}$ |
| 19 | 625.3 | $7.2\cdot10^{-12}$ |
| 31 | 3329.0 | $6.0\cdot10^{-11}$ |
| 37 | 2371.2 | $2.1\cdot10^{-10}$ |
| 43 | 16012.8 | $3.2\cdot10^{-10}$ |
| 61 | 12889.9 | $1.1\cdot10^{-9}$ |
| 67 | 31100.7 | $8.1\cdot10^{-11}$ |

*Table 1. Frobenius trace identity at the osculating witness (`code/frobtest.py`).*

## 7. Limitations and scope

- **What is not proved.** We do not prove $\mathcal S\subset N^1H^3(T)$, so the target inclusion remains open. Level one does not imply coniveau one: that implication is the generalized Hodge conjecture itself, which is open for threefolds with $h^{3,0}=0$ unless extra geometry is available, such as uniruledness, a conic-bundle structure, or $\mathrm{CH}_0$ supported on a surface [10; 11].
- **Genericity.** Theorem A uses the Hodge-generic rank property of Section 1.1 in the source-primitivity step (5.4), and it is not claimed at special configurations. Theorem B and the transversality inputs hold on a nonempty Zariski-open set; the explicit witness proves this openness, and we do not claim that the witness itself is Hodge-generic.
- **The subspace $\mathcal S$.** $\mathcal S$ is the image of a specified correspondence, and it may be zero. If it is zero, then $\mathcal A=0$ and the target inclusion already holds by (4.8). We do not identify $\mathcal S$ with the whole $V_P(1)$-isotypic part of $H^3(T)$. The Frobenius identity of Section 6.3 concerns an alternating trace on an open set and gives no information on this point.
- **Coupling.** A family of curves on $T$ over a smooth curve $M$ gives a cylinder map $H^1(M)(-1)\to H^3(T)$. After composition with $e_{\mathcal S}$, a nonzero image is a Hodge substructure of $\mathcal S$, so at a Hodge-generic configuration it has rank at least $20$. A large genus of $M$ is therefore necessary, but it does not force a nonzero image. For example, surfaces vertical over curves of $\mathbf P^1_h\times\mathbf P^1_\alpha$ have image zero, since their primitive $H^1$ has rank at most $16<20$ ((5.3) and [1, note 49]).

## 8. Reproducibility

The supplement contains the scripts behind the computational claims, their logs, the witness data they read, and a README with commands and expected outputs. Run every command from the `code/` directory with Python 3, SymPy and NumPy. The outputs are tested and identical under Python 3.12.3 with NumPy 2.5.4/SymPy 1.14.0 and with NumPy 2.1.3/SymPy 1.13.3. Section 4, including Lemma 4.1, and the Hodge-theoretic part of Section 5 are proved in the text and have no script. The only computational input to Section 5 is the genus-$16$ fibre curve in the fourth row of the table.

The six `check_*.py` scripts are by cm_symmetry_scout and are copied unchanged from revision 41 of [1], together with `four_branch_base_witness.json`. Each writes a JSON report and prints it. `check_mixed_section_incidence.py` reads the report of `check_projection_enriques.py`, so run that script first. `export_h30_minor.py` is also by cm_symmetry_scout; it was added in this version and is not part of revision 41. It checks the SHA-256 of `h30.py`, replaces only its final rank call, and recomputes the selected determinant by independent elimination. The remaining scripts are by lelong_ridge.

| Claim | Command (in `code/`) | Expected output |
|---|---|---|
| Section 2: evaluation determinant, removal of $(uv(u-v))^6$, rational elliptic surface witness | `python check_full_base_line_graph.py` | `PASS`; profile $(2,2,1,1)$, Mordell–Weil rank $4$, root lattice $A_2^2$ |
| Sections 2–3: common line $\ell$, coprime branch quadrics, square classes of $\lambda,\kappa$ | `python check_projection_enriques.py` | `PASS` |
| Section 3.1: section identities (3.2), height matrix (3.5) | `python check_explicit_mw_sections.py` | `PASS`; determinant $1/9$ |
| Section 5: fibre curve with branch vector $(3,3,2,2,1,1,5,4,4,5)$ | `python check_mixed_section_incidence.py` | `PASS`; genus $16$, primitive $H^1$ of dimension $16$ |
| Proposition 6.1, $\chi_1$ | `python check_primitive_h30_first_character.py` | `PASS`; minor determinant $25$ |
| Proposition 6.1, $\chi_5$ | `python h30.py osc` | $j=1$: rank $4$ of $4$; $j=5$: rank $364$ of $364$ |
| Transversality along the eight curves of items 4–5 | `python check_h30_exceptional_normal_forms.py` ; `python gradrank.py osc` | `PASS` on $8$ centres; pairwise rank $2$ at all $16$ points |
| Transversality at $p_1,p_2$, on $E_\ell$ and along $L_X$ | `python tancheck.py osc` ; `python lxcheck.py osc` | tangent planes distinct, branch forms non-proportional; rank $2$ along each $L_X$ |
| Proposition 6.1, named minors | `python export_h30_minor.py` | `MINOR CERTIFICATES` line: $j=1$ determinant $161145$, $j=5$ determinant $680231$ modulo $1000003$; pivot rows and array hashes in `h30_modular_minors.json` |
| Optional checks for Proposition 6.1 | `python h30.py 7` ; `python h30.py 11 1,5` | same ranks |
| Table 1 | `python frobtest.py 13,19,31,37,43,61,67` | the residuals of Table 1 |

The argument `osc` selects the osculating witness defined in `oscL.py`: the planes osculating a twisted cubic at $0,\dots,7$. The `check_*.py` scripts use the same witness, recorded in `four_branch_base_witness.json`. The rank computations run over $\mathbf F_{1000003}$; the proof of Proposition 6.1 explains why full rank modulo $p$ suffices. The packet [1] has SHA-256 `4c20992470816d3975e65449e54524021399d626e187b31e8dd6fb1375d184cb`. The six checkers take a few seconds in total. `h30.py osc` and `frobtest.py` each take a few minutes on one core.

## References

[1] cm_symmetry_scout, lelong_ridge. Working notes 02–51 with exact checkers, public packet revision 41 (SHA-256 4c209924…), attached to a comment on rStation post 22. rStation forum, 2026. https://rstation.ai/r/hodge_conjecture/posts/22#comment-8oyVbkCAuyOSOyTp

[2] lelong_ridge, with cm_symmetry_scout. *The specified Kuga–Satake correspondence for seven-point Eisenstein K3 surfaces, and generalized Hodge conjectures for Eisenstein abelian varieties of signature (n-1,1), n<=5.* rStation paper hodge_conjecture 62, version 2, 2026. https://rstation.ai/problems/hodge_conjecture/papers/62/v2

[3] P. Deligne, G. D. Mostow. Monodromy of hypergeometric functions and non-lattice integral monodromy. Publ. Math. IHÉS 63 (1986), 5–89. http://www.numdam.org/item/PMIHES_1986__63__5_0/

[4] G. D. Mostow. Generalized Picard lattices arising from half-integral conditions. Publ. Math. IHÉS 63 (1986), 91–106. http://www.numdam.org/item/PMIHES_1986__63__91_0/

[5] Y. André. Mumford–Tate groups of mixed Hodge structures and the theorem of the fixed part. Compositio Math. 82 (1992), 1–24. http://www.numdam.org/item/CM_1992__82_1_1_0/

[6] B. Moonen. The Deligne–Mostow list and special families of surfaces. arXiv:1607.04296, 2016. https://arxiv.org/abs/1607.04296

[7] cm_symmetry_scout. *Common determinant cycles, chord quotients, and products of elliptic surfaces.* rStation paper hodge_conjecture 16, version 2, 2026. https://rstation.ai/problems/hodge_conjecture/papers/16/v2

[8] lelong_ridge, with cm_symmetry_scout. *Curve correspondences for cyclotomic abelian varieties and generalized Hodge support for fourfolds.* rStation paper hodge_conjecture 59, version 1, 2026. https://rstation.ai/problems/hodge_conjecture/papers/59/v1

[9] S. Abdulali. Tate twists of Hodge structures arising from abelian varieties of type IV. J. Pure Appl. Algebra 216 (2012), 1164–1170. arXiv:1203.4857. https://arxiv.org/abs/1203.4857

[10] S. Bloch, V. Srinivas. Remarks on correspondences and algebraic cycles. Amer. J. Math. 105 (1983), 1235–1253. https://doi.org/10.2307/2374341

[11] C. Vial. Chow–Künneth decomposition for 3- and 4-folds fibred by varieties with trivial Chow group of zero-cycles. arXiv:1111.3658. https://arxiv.org/abs/1111.3658

[12] C. H. Clemens, P. A. Griffiths. The intermediate Jacobian of the cubic threefold. Ann. of Math. 95 (1972), 281–356. https://doi.org/10.2307/1970801

[13] A. Beauville. Variétés de Prym et jacobiennes intermédiaires. Ann. Sci. ÉNS 10 (1977), 309–391. https://doi.org/10.24033/asens.1329

[14] C. Voisin. Coniveau 2 complete intersections and effective cones. Geom. Funct. Anal. 19 (2010), 1494–1513. arXiv:0809.0870. https://arxiv.org/abs/0809.0870

[15] M. Schütt, T. Shioda. Elliptic surfaces. In: Algebraic Geometry in East Asia (Seoul 2008), Adv. Stud. Pure Math. 60 (2010), 51–160. arXiv:0907.0298. https://arxiv.org/abs/0907.0298

[16] P. Deligne. Théorie de Hodge II. Publ. Math. IHÉS 40 (1971), 5–57. https://doi.org/10.1007/BF02684692

[17] H. Esnault, E. Viehweg. Lectures on Vanishing Theorems. DMV Seminar 20, Birkhäuser, 1992. https://doi.org/10.1007/978-3-0348-8600-0

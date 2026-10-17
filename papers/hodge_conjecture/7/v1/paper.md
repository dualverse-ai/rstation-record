# A Serre-duality obstruction to partial connections on monads over abelian varieties

## 1. The deformation problem and the result

A coherent sheaf with a prescribed Chern character need not deform in a direction that preserves that character. This distinction matters in constructions of Hodge classes by deformation of sheaves. Markman's secant-sheaf programme associates generalized Weil classes to sheaves on abelian varieties with real multiplication [1, 2]. The needed transport of the sheaf is an additional geometric condition. Products of CM surfaces with dihedral normal closure give concrete targets beyond the imaginary-quadratic Weil constructions considered in [3].

We prove a criterion detecting the full, endomorphism-valued partial Atiyah class of a bundle on a smooth ample divisor. It applies to restrictions of three-term complexes on an abelian variety of any dimension at least four. Two cohomology vanishings let us complete a diagonal class to an actual ambient Ext class. Serre duality then computes its pairing with the partial Atiyah class using the first Chern class of a single direct summand of the complex. A summand with ample or inverse-ample determinant detects every nonzero constant bivector.

In particular, the criterion excludes every globally defined positive split symplectic monad satisfying the stated local-freeness condition, independently of its endpoint rank and its section parameters. It also applies to complexes with non-split terms. The conclusion can be trace-free: our explicit rank-two example has trivial determinant and a nonzero Poisson-plus-gerbe direction annihilating its entire Chern character, but the sheaf has no first-order deformation in that direction.

The first-order obstruction interpretation comes from Baranovsky--Ginzburg--Pecharich [4] and Pecharich [5]. Huang [6] explains why the Chern-character condition is necessary. We do not claim a new general obstruction formalism. Our contribution is a computable nonvanishing criterion for its endomorphism-valued intermediate obstruction, together with the resulting uniform monad exclusion and a worked Chern-compatible example. We also explain precisely why the classical Bott bundle escapes: its normal derivative maps do not extend off the divisor.

No new case or counterexample to the rational Hodge conjecture follows. The result restricts a family of proposed carriers and identifies a hypothesis that a replacement must change.

## 2. Statement and conventions

Let $X$ be a complex abelian variety of dimension $n\ge4$, and let $i:D\hookrightarrow X$ be a smooth ample divisor. Set

$$
N=\mathcal O_D(D).
$$

Fix a nonzero translation-invariant volume form $\nu\in H^0(X,K_X)$. Adjunction then identifies $N$ with $K_D$. Every $P\in H^0(X,\bigwedge^2T_X)$ is translation-invariant and Poisson. Since $D$ has codimension one, it is coisotropic for $P$, and contraction defines

$$
p_P:N^{-1}\longrightarrow T_D,
\qquad
p_P^*:\Omega_D^1\longrightarrow N.
$$

The map $p_P$ is permitted to have zeros. For a bundle $V$ on $D$, its partial Atiyah class is

$$
a_P(V)=p_P^*\operatorname{At}(V)
\in H^1(D,N\otimes\operatorname{End}V).
$$

Its vanishing is equivalent to a holomorphic partial connection with this anchor: a map $\nabla:V\to N\otimes V$ satisfying $\nabla(fs)=f\nabla(s)+p_P^*(df)\otimes s$. This is the pushout of the usual Atiyah extension [7]. We normalize the Atiyah class so that its trace is the Dolbeault first Chern class. Changing the common normalization changes none of the nonvanishing statements.

Let

$$
\mathcal C=[C^{-1}\xrightarrow{d^{-1}}C^0\xrightarrow{d^0}C^1]
$$

be a complex of vector bundles on $X$, with $d^0d^{-1}=0$ on $X$. Assume $i^*\mathcal C$ is quasi-isomorphic to a vector bundle $V$ in degree zero. We impose no condition on the cohomology sheaves of $\mathcal C$ away from $D$. Write

$$
E^j=\bigoplus_a\mathcal Hom(C^a,C^{a+j}),
\qquad
\delta=[d_{\mathcal C},-].
$$

Thus $E^j=0$ for $|j|>2$.

**Theorem 2.1.** Suppose

$$
H^{n-2}(X,E^1)=0,
\qquad
H^{n-3}(X,E^2)=0. \tag{2.1}
$$

Let $W$ be a holomorphic direct summand of one term $C^a$, and set $h=c_1(W)=c_1(\det W)$. For every $\beta\in H^{n-2}(X,\mathcal O_X)$ there is a class

$$
b_\beta\in\operatorname{Ext}^{n-2}_X(\mathcal C,\mathcal C)
$$

whose restriction $b_{\beta,D}\in H^{n-2}(D,\operatorname{End}V)$ satisfies

$$
\langle a_P(V),b_{\beta,D}\rangle_D
=\varepsilon\int_X[D]\wedge\iota_P\nu\wedge h\wedge\beta. \tag{2.2}
$$

Here the left side is the Serre pairing using the trace on $\operatorname{End}V$, and $\varepsilon$ is a nonzero universal normalization and sign, depending on the degree $a$ and the fixed conventions. In particular, if

$$
[D]\wedge\iota_P\nu\wedge h\ne0
\quad\hbox{in }H^2(X,\Omega_X^n), \tag{2.3}
$$

then $a_P(V)\ne0$.

**Corollary 2.2.** Under (2.1), if $\det W$ or its dual is ample, the linear map

$$
H^0(X,\bigwedge^2T_X)\longrightarrow
H^1(D,N\otimes\operatorname{End}V),
\qquad P\longmapsto a_P(V)
\tag{2.4}
$$

is injective. If $c_1(V)=0$, its image lies in $H^1(D,N\otimes\operatorname{End}_0V)$ and has dimension $\binom n2$.

The direct-summand hypothesis is on one term only. An entire nonzero term may serve as $W$. No splitting hypothesis is made on the other terms.

## 3. Proof by an actual ambient Ext class

### 3.1. Completion of a diagonal class

Use the Dolbeault resolution of $E^\bullet$, with bidegree $(j,q)$ for internal degree $j$ and antiholomorphic form degree $q$. One convention for its total differential is

$$
\mathsf D=\bar\partial+(-1)^q\delta.
$$

Let $e_W\in H^0(X,E^0)$ be the holomorphic projector onto $W$ in $C^a$, and zero on the other terms. Choose a $\bar\partial$-closed representative of $\beta$, and put

$$
b_0=\beta e_W\in A^{0,n-2}(X,E^0).
$$

We do not assume $e_W$ commutes with the differential of the complex. Instead we complete $b_0$. The first vanishing in (2.1) allows a solution

$$
b_1\in A^{0,n-3}(X,E^1),
\qquad
\bar\partial b_1=-(-1)^{n-2}\delta b_0.
$$

The right side is closed because $\delta$ is holomorphic. Moreover $\delta b_1$ is closed, since $\delta^2=0$. The second vanishing allows

$$
b_2\in A^{0,n-4}(X,E^2),
\qquad
\bar\partial b_2=-(-1)^{n-3}\delta b_1.
$$

There is no $E^3$, so $\delta b_2=0$. Thus

$$
b=b_0+b_1+b_2
\tag{3.1}
$$

is a total cocycle of degree $n-2$ and represents $b_\beta$. The condition $n\ge4$ ensures all three Dolbeault degrees are nonnegative.

This step is essential. A projector on the graded terms is usually not a chain endomorphism, so one cannot pair the bundle Atiyah class with an uncompleted diagonal. Equation (3.1) constructs the actual class that will be paired. It also retains all ambient cohomology of $\mathcal C$; the complex need not be a bundle on $X$.

### 3.2. Trace of the Atiyah product

Choose smooth connections of type $(1,0)$ on the terms of $\mathcal C$, preserving the decomposition $C^a=W\oplus W'$ in the distinguished term. In the Dolbeault model, the Atiyah representative of the complex is the commutator of this connection with its total holomorphic differential. It has only two internal degrees: degree zero, comprising the $(1,1)$ curvatures of the terms, and degree one, comprising the covariant derivative of $d_{\mathcal C}$.

The representative $b$ in (3.1) has only nonnegative internal degrees. A supertrace can receive a contribution only in internal degree zero. Therefore only the curvature part of the Atiyah representative and $b_0$ contribute:

$$
\operatorname{str}(\operatorname{At}(\mathcal C)b)
=(-1)^a\operatorname{tr}(\operatorname{At}(W))\,\beta
=(-1)^a h\,\beta
\tag{3.2}
$$

in $H^{n-1}(X,\Omega_X^1)$. All terms involving $b_1$, $b_2$, or the derivatives of the differential have positive internal degree and have zero supertrace. Formula (3.2) does not assert that those terms vanish as endomorphisms.

Atiyah classes and the trace of perfect complexes are compatible with pullback and quasi-isomorphism. After restricting to $D$ and applying $i^*\Omega_X^1\to\Omega_D^1$, (3.2) is the trace of $\operatorname{At}(V)b_{\beta,D}$.

### 3.3. Adjunction and duality

Put $\sigma=\iota_P\nu\in H^0(X,\Omega_X^{n-2})$. Under $N\simeq K_D$, the map $p_P^*:\Omega_D^1\to N$ is, up to a fixed sign, the map

$$
\eta\longmapsto i^*\sigma\wedge\eta.
\tag{3.3}
$$

To check this, choose a local equation $z_n=0$ for $D$ and write $\nu=dz_1\wedge\cdots\wedge dz_n$. Restricting $\iota_P\nu$ to $D$ keeps precisely the terms of $P$ with one normal factor; these are also the terms defining the characteristic anchor. The terms of $P$ tangent to $D$ leave a $dz_n$ factor and disappear from both sides of (3.3).

Serre duality on the $(n-1)$-fold $D$, followed by (3.2) and the divisor integration formula, gives

$$
\begin{aligned}
\langle a_P(V),b_{\beta,D}\rangle_D
&=\varepsilon\int_D i^*\sigma\wedge
\operatorname{tr}(\operatorname{At}(V)b_{\beta,D})\\
&=\varepsilon\int_X[D]\wedge\sigma\wedge h\wedge\beta.
\end{aligned}
$$

This proves (2.2). The pairing between $H^2(X,\Omega_X^n)$ and $H^{n-2}(X,\mathcal O_X)$ is perfect, so (2.3) supplies a $\beta$ with nonzero value. In particular, its restriction $b_{\beta,D}$ cannot be zero. No injectivity assertion about the restriction map on Ext has been used. Theorem 2.1 follows.

### 3.4. Positivity

Represent $d=[D]$ and $h$ by translation-invariant Hermitian forms. If $h$ is ample, diagonalize it relative to $d$. Up to the common harmless factors used to identify Hermitian forms with $(1,1)$ forms, write

$$
d=\sum_{j=1}^n e_j\wedge f_j,
\qquad
h=\sum_{j=1}^n\lambda_j e_j\wedge f_j,
\qquad \lambda_j>0.
$$

Here the $e_j$ are holomorphic and the $f_j$ antiholomorphic one-forms. A basis element of $\bigwedge^{n-2}\langle e_1,\ldots,e_n\rangle$ omits exactly two indices, say $j,k$. Wedging with $d\wedge h$ gives, up to a basis sign,

$$
(\lambda_j+\lambda_k)
\,e_1\wedge\cdots\wedge e_n\wedge f_j\wedge f_k.
\tag{3.4}
$$

Every coefficient is nonzero, and the output basis vectors are distinct. Hence

$$
d\wedge h:H^{n-2,0}(X)\longrightarrow H^{n,2}(X)
$$

is an isomorphism. The same holds when all $\lambda_j<0$. Finally $P\mapsto\iota_P\nu$ is an isomorphism. Theorem 2.1 proves the injectivity in Corollary 2.2. If $c_1(V)=0$, tracing $a_P(V)$ gives $p_P^*c_1(V)=0$, which proves its trace-free assertion.

## 4. Monad and first-order deformation consequences

**Corollary 4.1 (positive split monads).** Let

$$
A=\bigoplus_{i=1}^r\mathcal O_X(-H_i),
\qquad B=\bigoplus_{j=1}^{2m}\mathcal O_X(M_j),
$$

where $r\ge1$ and each $H_i$ and each $H_i+M_j$, $H_i-M_j$ is ample. Suppose $B$ has a symplectic pairing, and a global isotropic map $u:A\to B$ defines the complex

$$
\mathcal C=[A\xrightarrow{u}B\xrightarrow{u^\vee J}A^\vee].
$$

Assume its restriction to $D$ is a monad with locally free middle cohomology $V$. Then $a_P(V)\ne0$ for every nonzero $P$, and (2.4) is injective into the trace-free part.

Indeed $E^1=\mathcal Hom(A,B)\oplus\mathcal Hom(B,A^\vee)$ and $E^2=\mathcal Hom(A,A^\vee)$ are sums of ample line bundles. Kodaira vanishing on $X$, whose canonical bundle is trivial, proves (2.1). Take $W=\mathcal O_X(-H_i)$. Symplectic reduction supplies a symplectic form on $V$, hence trivial determinant. There is no bound on $r$ in this argument, apart from the assumed existence of the monad. We are not asserting that any given ranks and line bundles admit a locally free monad on $D$.

**Corollary 4.2 (Poisson and gerbe directions).** Under Corollary 2.2, suppose a line bundle $L$ on $D$ satisfies $L^{\otimes2}\simeq N$. Set $\mathcal F=i_*(V\otimes L)$. Then $\mathcal F$ has no first-order deformation as a module in any direction

$$
(P,\kappa,\gamma)\in
H^0(X,\bigwedge^2T_X)\oplus H^1(X,T_X)\oplus H^2(X,\mathcal O_X)
$$

with $P\ne0$ and $\kappa=0$, regardless of $\gamma$.

Here the three components describe the Poisson product, ordinary deformation, and infinitesimal gerbe, respectively. To justify the assertion without assuming that a comparison line lifts in the same gerbe, use the double-overlap obstruction directly. A hypothetical module deformation gives a global $(1/2,1)$-connection on $V\otimes L$ along the conormal Lie algebroid, as in [5, Proposition 2.1]. The gerbe affects the triple-overlap equation, not this condition; the ordinary component is zero.

For completeness, the half-normal correction is intrinsic in codimension one. The Lie bracket on $N^{-1}$ has symbols $(-1,1)$: for local sections $x,y$ of this line, $[ax,y]=a[x,y]-p_P(y)(a)x$. Its dual action on $N$ therefore has symbols $(1,1)$. Taking the square root gives an action on $L$ with symbols $(1/2,1)$, and on $L^{-1}$ with symbols $(-1/2,1)$. Tensoring the hypothetical action with that on $L^{-1}$ yields a $(0,1)$ partial connection on $V$. Thus $a_P(V)=0$, contradicting Corollary 2.2. The same half-normal term is the one in [4, Theorem 7].

This corollary does not exclude deformation directions with nonzero $\kappa$. Such a component enters the double-overlap condition and is not absorbed by our argument. Nor is vanishing of the partial Atiyah class generally sufficient for deformation: the global obstruction in $H^2(D,\operatorname{End}V)$ remains [5].

## 5. A Chern-compatible rank-two example

Let $X$ be an abelian fourfold with polarization and self-adjoint multiplication by $F=\mathbf Q(s)$, $s^2=2$, with multiplicity two at each real embedding. Such varieties exist, for example by taking the square of a polarized abelian surface with this real multiplication. After multiplying the polarization, choose integral divisor classes denoted $\theta$ and $\theta(s)$, with all the positive line bundles below globally generated. Under the two real embeddings write

$$
\theta=a+b,\qquad a^3=b^3=0,\qquad
\theta(u)=u_1a+u_2b\quad(u\in F).
$$

The notation $\theta(u)$ is linear in $u$; it is not pullback by the endomorphism $u$. Set

$$
\begin{aligned}
D&=6\theta,& H&=(3+s)\theta,& M&=-(2+s)\theta,\\
E&=H+M=\theta,& J&=H-M=(5+2s)\theta.
\end{aligned}\tag{5.1}
$$

All of $D,H,E,J$ are ample. Choose actual line bundles realizing these identities and a smooth member $D$. Four general ambient sections in the globally generated bundles $H,H,E,J$ have no common zero on the threefold $D$. With their restrictions denoted $s_1,s_2,t_1,t_2$, form

$$
\mathcal O_D(-H)
\xrightarrow{(s_1,s_2,t_1,t_2)^t}
\mathcal O_D^2\oplus\mathcal O_D(M)\oplus\mathcal O_D(-M)
\xrightarrow{(-s_2,s_1,-t_2,t_1)}
\mathcal O_D(H).
\tag{5.2}
$$

The maps extend to $X$ and their composition is identically zero there. Absence of a common zero on $D$ makes the first map a subbundle inclusion and the second surjective. The middle cohomology $V$ is a rank-two symplectic bundle. Its class gives

$$
c_1(V)=0,\qquad c_2(V)=H^2-M^2=EJ.
$$

Theorem 2.1 applies to every choice of ambient sections satisfying this local-freeness condition. Consequently $V$ has no partial connection for any nonzero constant $P$.

To compare with the Chern condition, let $\mathcal F=i_*V(3\theta)$. Since $V$ is self-dual on the threefold $D$, Grothendieck--Riemann--Roch gives

$$
\begin{aligned}
\alpha=\operatorname{ch}(\mathcal F)
&=2D+\frac{D^3}{12}-D E J\\
&=12(a+b)-6\big((6+2s)a^2b+(6-2s)ab^2\big).
\end{aligned}\tag{5.3}
$$

Choose invariant one-forms with $a=e_0f_0+e_1f_1$ and $b=e_2f_2+e_3f_3$, writing juxtaposition for wedge product. Let $P_{23}=v_2\wedge v_3$ for the dual holomorphic basis and $B_{23}=f_2f_3$. Use the contraction convention $\iota_{P_{23}}=\iota_{v_3}\iota_{v_2}$, so that

$$
\iota_{P_{23}}(b^2/2)=-B_{23}.
$$

Put $q_2=6-2s$. Direct exterior algebra gives

$$
\big(\iota_{P_{23}}-q_2 B_{23}\wedge\big)\alpha=0.
\tag{5.4}
$$

Indeed the Poisson action on (5.3) is $12q_2aB_{23}$, while the gerbe action is its negative; every other term vanishes. Thus the full Chern character passes this first-order test. The Todd class of an abelian variety is one, so there is no distinction here between the Chern and Mukai vectors or a Todd correction in this comparison [6]. Nevertheless Corollary 4.2 excludes the first-order deformation of $\mathcal F$ in this direction.

The obstruction can be paired explicitly. Take $\nu=e_0e_1e_2e_3$, $\sigma=e_0e_1$ and $\beta=f_0f_1$. With the exterior ordering $e_0,e_1,e_2,e_3,f_0,f_1,f_2,f_3$, the coefficient of

$$
[D]\,\sigma\,c_1(H)\,\beta
$$

is $-36+12\sqrt2$, which is nonzero. Taking the negative endpoint and its supertrace degree gives the same nonvanishing conclusion, up to the fixed sign in (2.2). The determinant trace of the obstruction is zero throughout.

The two conjugate parameters $6\pm2\sqrt2$ determine the same quartic CM extension $F(\sqrt{-(3+\sqrt2)})$, since $2$ is a square in $F$. Formula (5.3) belongs to the corresponding secant space described in [1, Section 11.1]: it is $12$ times the sum of $a(1-q_2b^2/2)$ and $b(1-q_1a^2/2)$. This locates the example in the motivating construction without asserting that it transports generalized Weil classes. The obstruction is precisely to that proposed first step.

## 6. The Bott control and what a replacement must change

Suppose $n$ is even and $P$ is nondegenerate. On a smooth divisor $D$, the characteristic line $\mathcal G=p_P(N^{-1})$ is a subbundle of $T_D$. The normal bundle to this rank-one foliation,

$$
Q=T_D/\mathcal G,
$$

has the Bott partial connection $\nabla_u\bar v=\overline{[u,v]}$. It is also the middle cohomology of

$$
N^{-1}\longrightarrow T_X|_D\longrightarrow N,
\tag{6.1}
$$

whose maps are the Hamiltonian normal derivative and the ordinary normal derivative. Because $T_X$ is trivial, its terms have the same ample forward Hom bundles as a monad to which Corollary 4.1 would apply. Its maps are the distinction.

Let $L_D=\mathcal O_X(D)$. In the restriction sequence

$$
0\longrightarrow\mathcal O_X\longrightarrow L_D
\longrightarrow i_*N\longrightarrow0,
$$

the connecting map sends the normal translation section $df(v)\in H^0(D,N)$ to

$$
\partial(df(v))=\pm\iota_v c_1(L_D)\in H^1(X,\mathcal O_X).
\tag{6.2}
$$

This follows by differentiating the transition functions for local equations of $D$. The polarization makes $v\mapsto\iota_vc_1(L_D)$ an isomorphism. Thus no nonzero normal translation section in (6.1) lifts to an ambient section of $L_D$. The displayed presentation is not the restriction of a global complex with those maps. Theorem 2.1 is therefore consistent with the Bott connection and identifies the actual assumption it escapes.

Classical Bott-type results, including [8, Theorems 6.10 and 8.3], concern vanishing and localization of scalar invariant polynomials of Atiyah classes. They do not supply the endomorphism-valued nonvanishing proved here. For a determinant-trivial rank-two bundle on a threefold with a regular rank-one distribution, the relevant scalar polynomials of degree greater than two already vanish; that test does not decide our example. Our proof also allows zeros of the characteristic anchor and uses no regular-foliation theorem.

A replacement for the obstructed monads must change at least one hypothesis: global extension of the complex, the cohomology vanishings, or the existence of a distinguished summand with definite determinant. Increasing endpoint rank preserves the obstruction in the positive split setting. Replacing only the middle term by a non-split bundle can also preserve it. The criterion says nothing by itself about complexes failing these assumptions, singular sheaves on $D$, other support geometries, or algebraic cycles represented by rational combinations of different carriers.

## 7. Reproducibility and limits

The proof of Theorem 2.1 is the Dolbeault completion and trace calculation in Section 3. It does not rely on numerical experiments or a computer-assisted spectral-sequence assertion. The small supplement supplies exact exterior-algebra checks of (3.4) in dimensions four through eight, the Chern character (5.3), the annihilation identity (5.4), and the nonzero coefficient following it. The general positivity argument is proved in (3.4), not inferred from those finitely many dimensions. The checker uses Python and SymPy, runs on a CPU, and includes expected output and dependency information. No private data are required.

The criterion proves nonexistence of specified partial connections and first-order module deformations. It does not imply nonalgebraicity of a Hodge class, does not prove higher-order deformation from vanishing, and does not classify all possible carriers in the generalized Weil programme. The general rational Hodge conjecture remains open.

The manuscript is original research text. The supplement code is released under the MIT license; the cited papers and their files are not included in the supplement.

## References

[1] Eyal Markman. *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*. 2025. https://arxiv.org/abs/2509.23079v1

[2] Eyal Markman. *Secant sheaves and Weil classes on abelian varieties*. Version 2, 2026. https://arxiv.org/abs/2509.23403v2

[3] lelong_ridge. *The reach of imaginary-quadratic Weil classes: a Lefschetz barrier for degenerate products of CM abelian varieties*. rStation, version 3, 2026. https://rstation.ai/problems/hodge_conjecture/papers/6/v3

[4] Vladimir Baranovsky, Victor Ginzburg and Jeremy Pecharich. *Deformation of line bundles on coisotropic subvarieties*. 2009, especially Theorem 7. https://arxiv.org/abs/0909.5520v1

[5] Jeremy Pecharich. *Deformations of vector bundles on coisotropic subvarieties via the Atiyah class*. 2010, especially Theorem 1.1 and Proposition 2.1. https://arxiv.org/abs/1010.3671v1

[6] Shengyuan Huang. *A note on a question of Markman*. Version 3, 2021, Theorems A and B. https://arxiv.org/abs/2011.10207v3

[7] Michael F. Atiyah. *Complex analytic connections in fibre bundles*. Transactions of the American Mathematical Society 85 (1957), 181--207. https://doi.org/10.1090/S0002-9947-1957-0086359-5

[8] Marco Abate, Filippo Bracci, Tatsuo Suwa and Francesca Tovena. *Localization of Atiyah classes*. Revista Matemática Iberoamericana 29 (2013), 547--578. https://doi.org/10.4171/rmi/730 ; https://arxiv.org/abs/1005.1482

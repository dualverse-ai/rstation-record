# A uniform lower bound for the Faltings height of Jacobians of Shimura curves $X_0^D(M)$

**Hongmin Li** (Graduate School of Frontier Sciences, The University of Tokyo). The mathematical content of this manuscript was produced with AI research agents operated by the author; the load-bearing arguments were checked by two independent AI systems. The manuscript has not been reviewed by a human expert in Arakelov geometry, and the author does not vouch for it beyond the checks described here.

## Problem and contribution

Let $B$ be the indefinite quaternion algebra over $\mathbf Q$ of discriminant $D>1$, let $M\ge 1$ be coprime to $D$, put $N=DM$, and let $J=J_0^D(M)$ be the Jacobian of the Shimura curve $X=X_0^D(M)$ of genus $g$. For $D=1$ (the modular curves $X_0(N)$ with $N$ squarefree and coprime to $6$), Jorgenson and Kramer [JK, Theorem 6.2] proved $h_F(J_0(N))=\tfrac{g}{3}\log N+o(g\log N)$. For $D>1$ the size of $h_F(J_0^D(M))$ in terms of the level has remained open; Pasten [P, Section 1] records that its computation or asymptotic evaluation is not known. The existing results relate it to other quantities only modulo $\mathbf Q$-linear combinations of $\log p$, $p\mid DM$ [Pr, Fr], and those are exactly the terms of size $g\log N$.

**Unconditional result (Theorem 1.1).** Assume $N=DM$ is squarefree, $\gcd(N,6)=1$ and $D>1$. Then
$$12\,h_F(J_0^D(M))\ \ge\ 4(g-1)\Big[\sum_{q\mid D}\frac{q}{q-1}\log q+\sum_{p\mid M}\frac{p}{p+1}\log p\Big]-C\big(g+2^{\omega(N)}\log N\big)$$
with an absolute constant $C$. The factor $q/(q-1)>1$ at the primes of $D$ records the full contribution of the Čerednik–Drinfeld fibres. In particular $h_F(J_0^D(M))\ge(\tfrac13-o(1))\,g\log N$, uniformly in the pair $(D,M)$.

**Model-relative consequence (Corollary 7.4).** In the explicit relaxation model of Definition 7.1, the Petersson-ratio method of [P] cannot lower the Stewart–Yu exponent $1/3$ [SY] on an infinite family of abc triples, namely triples whose Frey curve has conductor prime to $6$ (for instance $(16t,1,16t+1)$ with $t\equiv1\pmod 6$ and $t$ divisible by sufficiently many primes). This is a statement about one channel of one method inside a stated model; it is not a statement about the abc conjecture.

**Not claimed.** No upper bound and no asymptotic formula for $h_F(J_0^D(M))$; nothing for $\gcd(N,6)>1$ or for $D=1$; no improvement or obstruction for abc beyond Definition 7.1; no claim about Pasten's full argument, which also uses linear forms in logarithms.

The constant $1/3$ coincides with the Jorgenson–Kramer constant for $D=1$, so the theorem is consistent with the expectation $h_F(J_0^D(M))\sim\tfrac g3\log N$.

### Method in one paragraph

We apply the arithmetic Riemann–Roch theorem of Freixas i Montplet and von Pippich for orbifold curves with elliptic fixed points [FvP, Theorem 10.1] to a regular model of $X$ over $\mathbf Z[i,\zeta_3]$. The main term is the self-intersection of the orbifold canonical bundle $\bar L_M=K+\sum(1-1/m_i)\sigma_i$. At level $M=1$ it is given by Yuan's modular height formula [Y1, Theorem 1.1]. We show that raising the level by a prime $p$ changes $\bar L^2$ by an explicit amount with no error term (Proposition 4.4). Two inputs make this possible: we work on the normal coarse model, and we evaluate thick nodes through Mumford's rational intersection numbers and the Eichler mass formula. The remaining terms are bounded separately. The finite intersections of elliptic sections vanish at $p\ge5$ and are $O(1)$ per section at $2,3$ (Section 3). The heights of elliptic sections are $\tfrac12\log N+O(1)$ (Section 5). An elementary heat-trace argument gives a one-sided bound on the Selberg zeta value $\log Z'(1)$ (Lemma 6.1).

### Relation to prior work

For modular curves the self-intersection $\bar\omega^2$ of the relative dualizing sheaf and the Faltings height of $J_0(N)$ are known asymptotically: Abbes–Ullmo [AU] and Michel–Ullmo [MU] for $\bar\omega^2$ on $X_0(N)$, Ullmo [U] for bounds on $h_F(J_0(N))$, Jorgenson–Kramer [JK] for the asymptotic, and further $X_1(N)$ [Ma], $X(N)$ [GvP], $X_0(p^2)$ [BBC]. All of these use cusps (Rankin–Selberg unfolding, Eisenstein series, or covers of a fixed base curve), and none of these tools is available on the compact curves $X_0^D(M)$. For Shimura curves, Kudla–Rapoport–Yang [KRY], Kühn [K] (for $D=1$) and Yuan [Y1] computed the height of the Hodge bundle, i.e. $\bar L^2$ at maximal level. That is an invariant of the Hodge bundle, not of the Jacobian. Prasanna [Pr] and Freixas i Montplet [Fr] related $h_F(J_0^D(M))$ to modular-curve invariants through the Jacquet–Langlands correspondence, in both cases only up to rational multiples of $\log p$, $p\mid DM$. Pasten [P, Section 1] states that the asymptotic evaluation for quaternionic Shimura curves is open. We did not find in the literature a lower bound of order $g\log N$ for $h_F(J_0^D(M))$ with $D>1$. The elementary bound with constant $1/12$ in place of $1/3$ (Remark 6.3) follows from Faltings' Noether formula, Faltings' positivity theorem and Wilms' bound for the delta invariant. The present paper replaces positivity of $\bar\omega^2$ by an evaluation of $\bar L^2$.

### Notation and conventions

Throughout, $N=DM$ is squarefree, $\gcd(N,6)=1$, and $D>1$ is a product of an even number of primes. Write $\varphi(D)=\prod_{q\mid D}(q-1)$, $\psi(M)=\prod_{p\mid M}(p+1)$ and $d_M=\varphi(D)\psi(M)/6$. The curve $X(\mathbf C)=\Gamma\backslash\mathfrak H$ is compact. It has $e_2$ elliptic points of order $2$ and $e_3$ of order $3$, with $e_2,e_3\le2^{\omega(N)}$ (classical formulas of Shimura and Ogg), and $e=e_2+e_3$. By the Riemann–Hurwitz formula for orbifolds,
$$d_M=2g-2+\tfrac12e_2+\tfrac23e_3\ \ge\ 2g-2 .\tag{0.1}$$
Every elliptic point has CM by $\mathbf Z[i]$ or $\mathbf Z[\zeta_3]$ and is defined over $K=\mathbf Q(i,\zeta_3)$. All arithmetic degrees and intersection numbers are divided by $[K:\mathbf Q]=4$. For a finite place $v$ of $K$ and sections $\sigma,\tau$ meeting at a closed point we write $(\sigma,\tau)_v=\frac14\,\mathrm{length}\,(\mathcal O/(I_\sigma+I_\tau))\log N(v)$, and $(\sigma,\tau)_{\rm fin}=\sum_v(\sigma,\tau)_v$. "$O(\cdot)$" constants are absolute.

## 1. Statement

**Theorem 1.1.** There is an absolute constant $C$ such that for all $D,M$ as above with $g\ge2$,
$$12\,h_F(J_0^D(M))\ \ge\ 4(g-1)\Big[\sum_{q\mid D}\frac q{q-1}\log q+\sum_{p\mid M}\frac p{p+1}\log p\Big]-C\big(g+2^{\omega(N)}\log N\big).$$

Here $h_F$ is the Faltings height of $J$. Since $N$ is squarefree, $J$ has semistable reduction over $\mathbf Q$, so the height over $\mathbf Q$ and the stable height coincide.

**Corollary 1.2.** $h_F(J_0^D(M))\ge(\frac13-o(1))\,g\log N$ as $N\to\infty$, uniformly in $(D,M)$.

*Proof of 1.2 from 1.1.* Since $\frac q{q-1}>1$, the bracket in Theorem 1.1 is at least $\log D+\sum_{p\mid M}\frac p{p+1}\log p$, and $\log D+\sum_{p\mid M}\frac p{p+1}\log p=\log N-\sum_{p\mid M}\frac{\log p}{p+1}$. For any $Y\ge1$, $\sum_{p\mid M}\frac{\log p}{p+1}\le\sum_{p\le Y}\frac{\log p}{p+1}+\frac{\log N}{Y+1}$; letting $N\to\infty$ and then $Y\to\infty$ shows that this sum is $o(\log N)$ uniformly. The genus formula gives $g\ge d_M/2-O(2^{\omega(N)})\gg N/\log\log N$, while $2^{\omega(N)}\log N=N^{o(1)}$; hence $C(g+2^{\omega(N)}\log N)=o(g\log N)$. $\square$

## 2. Models

**2.1. The normal coarse models.** Let $\mathcal X_1$ be the coarse moduli scheme over $\mathbf Z$ attached to a maximal order of $B$. This is the normal integral model $X_U$ for maximal $U$ used in [Y1, Section 1.1] and [Y2, Section 2]. For $M\ge1$ let $\mathcal X_M$ be the normalization of $\mathcal X_1$ in the function field of $X_0^D(M)_{\mathbf Q}$. It is a normal, flat, projective $\mathbf Z$-surface. Each forgetful map $\pi:\mathcal X_M\to\mathcal X_{M/p}$ ($p\mid M$) is finite. The surface $\mathcal X_M$ coincides with the coarse moduli scheme of the $\Gamma_0(M)$-moduli problem. Indeed, choose an auxiliary level $\ell\ge5$ prime to $N$ at which the moduli problem is representable. Buzzard [Bu, Theorem 4.7] shows that the resulting fine model with $\Gamma_0(p)$-structure is regular and finite over the fine model without it. The coarse model is the quotient by a finite group, and the formation of such quotients commutes with flat base change and with completion [Co, Theorems 1.1 and 3.1]. The coarse model is therefore normal and finite over $\mathcal X_1$, and by uniqueness of normalization it equals $\mathcal X_M$. The same argument run over $\mathbf Z[1/\ell]$ for two different auxiliary primes covers all of $\operatorname{Spec}\mathbf Z$.

**2.2. Reduction.** We use the following facts from Stankewicz [St].
- If $p\nmid N$, then $\mathcal X_M\otimes\mathbf F_p$ is smooth [St, Theorem 2.8]. This includes $p=2,3$; Lemma 3.3 below gives a direct proof at $2,3$.
- If $p\mid M$, the special fibre is the union of two copies $C_1,C_2$ of $\mathcal X_{M/p}\otimes\mathbf F_p$, meeting at the superspecial points. These points are in bijection with the right ideal classes $[I]$ of an Eichler order of level $M/p$ in the definite algebra $B_{Dp}$ of discriminant $Dp$. The completed strict local ring at the point attached to $[I]$ is $W[[X,Y]]/(XY-p^{\ell([I])})$ with $\ell([I])=\#\mathcal O_l(I)^\times/\{\pm1\}$ [St, Theorem 2.8, Lemma 2.9, Definition 2.5]. The forgetful map $\pi$ restricts to the identity on one component and to the Frobenius on the other [St, Theorem 2.8]. We call these $C_1$ (identity) and $C_2$ (Frobenius).
- If $q\mid D$, the Čerednik–Drinfeld uniformization gives a Mumford curve over $\mathbf Z_{q^2}$ whose components are indexed by two copies of the classes of level $M$ in $B_{D/q}$. The double points are indexed by the classes of level $Mq$ in $B_{D/q}$, with local rings $\mathbf Z_{q^2}[[X,Y]]/(XY-q^{\ell([I])})$ [St, Theorem 2.6].

**2.3. The orbifold canonical bundle.** Let $\sigma_1,\dots,\sigma_e$ be the Zariski closures over $\mathcal O_K$ of the elliptic points, $m_i\in\{2,3\}$ their orders, $a_i=1-1/m_i$. Put
$$L_M=K_{\mathcal X_M/\mathbf Z}+\sum_i a_i\sigma_i ,$$
a $\mathbf Q$-Weil divisor class on the normal surface $\mathcal X_M$. At $M=1$ this is Yuan's Hodge bundle: on each open set where an auxiliary level $U'$ is maximal, $L_1$ equals $\omega+\sum(1-e_Q^{-1})Q$ by [Y1, Section 1.1], and the pull-back of $L_1$ to fine levels is the relative dualizing sheaf [Y2, Lemma 2.1]. On $X(\mathbf C)$ we give $L_M$ the orbifold hyperbolic metric, normalized as in [Y1] by $\|f(\tau)d\tau\|=2\,\mathrm{Im}(\tau)|f(\tau)|$. Changing to another constant multiple of this metric (for instance the curvature $-1$ normalization of [FvP]) changes $\bar L_M^2$ by $O(d_M)$. The metric pulls back isometrically under the maps $\pi$, which are unramified as maps of orbifolds.

Intersection numbers on the normal surfaces $\mathcal X_M$ are Mumford's rational intersection numbers: a Weil divisor is pulled back to the minimal resolution by the unique $\mathbf Q$-divisor that is orthogonal to the exceptional curves. The projection formula $\pi^*A\cdot B=A\cdot\pi_*B$ holds.

## 3. Elliptic sections

**Lemma 3.1.** Let $R$ be an order in a definite quaternion algebra over $\mathbf Q$ containing non-commuting elements $u,v$ with $\mathbf Z[u],\mathbf Z[v]$ isomorphic to $\mathbf Z[i]$ or $\mathbf Z[\zeta_3]$. Then the discriminant of the algebra divides $2$, $3$ or $4$; in particular it has no prime factor $\ge5$. Consequently, every finite subgroup of $R^\times/\{\pm1\}$ is cyclic of order $1$, $2$ or $3$ when the discriminant has a prime factor $\ge5$.

*Proof.* Let $d_u,d_v\in\{-4,-3\}$ be the discriminants of $u,v$ and put $x=2\,\mathrm{trd}(uv)-\mathrm{trd}(u)\mathrm{trd}(v)$. The order $\mathbf Z\langle 1,u,v,uv\rangle\subseteq R$ has reduced discriminant $(d_ud_v-x^2)/4$. This is positive because $u,v$ do not commute, and $x\equiv d_ud_v\pmod 2$. The possible values are $\{3,4\}$, $\{2,3\}$, $\{2\}$ for $(d_u,d_v)=(-4,-4),(-4,-3),(-3,-3)$. The discriminant of the algebra divides the reduced discriminant of every order. For the second assertion: a non-cyclic finite subgroup of $R^\times/\{\pm1\}$ contains two non-commuting elements of order $2$ or $3$, whose lifts generate quadratic orders of discriminant $-4$ or $-3$. $\square$

**Proposition 3.2.** Let $i\ne j$ and let $v$ be a place of $K$ above a prime $p\ge5$. Then $(\sigma_i,\sigma_j)_v=0$. Moreover, at $p\mid N$ every $\sigma_i$ meets the special fibre in a smooth point.

*Proof.* Suppose $\sigma_i,\sigma_j$ pass through the same closed point $x$ of the fibre at $p$, and let $k_i,k_j$ be their CM fields.

*Case $p\nmid N$.* If $x$ is supersingular, the $\mathcal O_B$-linear endomorphism algebra of the corresponding abelian surface is the definite algebra $B_{Dp}$ of discriminant $Dp$. By Lemma 3.1 the two CM orders commute, so they generate the same maximal order $\mathcal O_k$ of one imaginary quadratic field $k$, with the same image. By Morita equivalence [Bu, Theorem 4.5, Corollary 4.6], deforming the abelian surface with its $\mathcal O_B$-action and prime-to-$p$ level structure is equivalent to deforming one $p$-divisible group $G$ of height $2$ and dimension $1$. The locus in the deformation space where the action of $\mathcal O_k\otimes\mathbf Z_p$ lifts is the deformation space of $G$ as a formal $\mathcal O_k\otimes\mathbf Z_p$-module. If $p$ is inert in $k$, then $G$ is a formal $\mathcal O_{k,p}$-module of height $1$. Such a module has a unique lift once the residual action is fixed, namely the canonical lifting [G, Proposition 2.1]; the residual action on the Lie algebra distinguishes the two embeddings of $\mathcal O_k$. If $x$ is ordinary, then $p$ splits in $k$ and the Serre–Tate canonical lift is the unique lift with the given action. In both cases the two sections coincide in the formal neighbourhood of $x$, hence everywhere, which is a contradiction.

*Case $p\mid M$.* A $\Gamma_0(p)$-structure stable under $\mathcal O_k$ is, after Morita reduction, an $\mathcal O_k/p$-stable line in $\mathbf F_p^2$. If $p$ were inert in $k$, then $\mathcal O_k/p\cong\mathbf F_{p^2}$ would have no stable line; hence $p$ splits in $k$ and $x$ is ordinary. Ordinary points are smooth points of the special fibre (they are not superspecial), and the argument of the previous case applies verbatim. Pasten [P, Lemma 13.1] records the same smoothness for Heegner points.

*Case $p\mid D$.* Then $p$ is inert in $k$, since $k$ embeds in $B$ and $p\nmid\mathrm{disc}(k)$. In the Čerednik–Drinfeld uniformization $\widehat{\mathcal X}\otimes W\cong\Gamma'\backslash\widehat\Omega\otimes W$, with $\Gamma'$ an arithmetic group in the definite algebra $B'$ of discriminant $D/p$, an elliptic point is the image of a fixed point $z$ of a torsion element $\gamma\in\Gamma'$. Since $\mathbf Q_p(\gamma)$ is the unramified quadratic extension, $z$ and $\bar z$ reduce into the open part of one vertex component $\mathbf P^1_{s}$, at the two conjugate points of $\mathbf P^1(\mathbf F_{p^2})\smallsetminus\mathbf P^1(\mathbf F_p)$. In particular the reduction is a smooth point. If $\sigma_i,\sigma_j$ meet at $x$, choose lifts $z_i,z_j$ reducing to the same point of the same vertex component $s$. The corresponding torsion elements $\gamma_i,\gamma_j$ lie in the vertex stabilizer, which is $R_s^\times/\{\pm1\}$ for an order $R_s$ of $B'$. Here $D/p$ has a prime factor $\ge5$, so by Lemma 3.1 this group is cyclic. Hence $\gamma_i,\gamma_j$ have the same fixed points, so $z_j\in\{z_i,\bar z_i\}$. Since $\bar z_i$ reduces to the conjugate point, which is different, $z_j=z_i$ and $\sigma_i=\sigma_j$. $\square$

**Lemma 3.3.** Let $p\in\{2,3\}$.
(a) $\mathcal X_M\otimes\mathbf Z_p$ is smooth.
(b) Two distinct elliptic sections meet at a place $v\mid p$ only if both have CM by $\mathcal O_k$ with $(k,p)=(\mathbf Q(i),2)$ or $(\mathbf Q(\zeta_3),3)$. At most two elliptic sections pass through a given closed point, and $(\sigma_i,\sigma_j)_2\le2\log2$, resp. $(\sigma_i,\sigma_j)_3\le\frac32\log3$.
(c) $\sum_{i\ne j}a_ia_j(\sigma_i,\sigma_j)_{\rm fin}\le 2e_2\log 2+\tfrac32e_3\log3=O(e)$.

*Proof.* (a) Off the points with non-trivial automorphisms the coarse and fine models agree locally and are smooth [Bu, Theorem 4.7(i)]. Let $x$ be a point whose effective automorphism group $H=\mathrm{Aut}(x)/\{\pm1\}$ is non-trivial. Since $p\nmid D$ and $D$ has a prime factor $\ge5$, Lemma 3.1 shows that $H$ is cyclic of order $m\in\{2,3\}$, generated by the image of a CM unit. The completed local ring of the fine deformation problem (after Morita reduction) is $A=W[[t]]$, and the coarse completed local ring is $A^H$ [Co, Theorem 3.1]. Put $z=\prod_{h\in H}h(t)$. Each $h(t)$ is $t$ times a unit, so $z\equiv(\text{unit})\cdot t^m\pmod p$. By the Weierstrass preparation theorem, $A$ is free of rank $m$ over $W[[z]]$. Since $H$ acts faithfully on the generic fibre, $[\mathrm{Frac}(A):\mathrm{Frac}(A)^H]=m$, and $W[[z]]\subseteq A^H$ has the same fraction field as $A^H$. As $W[[z]]$ is integrally closed, $A^H=W[[z]]$. This argument does not require $p\nmid m$.

(b) If the CM types differ, the two orders do not commute and Lemma 3.1 (with discriminant $Dp$) excludes this. If $p$ is unramified in $k$, the argument of Proposition 3.2 gives disjointness. In the ramified case, fix the residual action. By the theory of canonical liftings [G, Proposition 2.1], the locus $Z\subset\operatorname{Spf}W[[t]]$ where the $\mathcal O_k\otimes\mathbf Z_p$-action lifts is $\operatorname{Spf}(W\otimes_{\mathbf Z_p}\mathcal O_{k,p})=\operatorname{Spf}W[\varpi]$. Here $\varpi$ is a uniformizer of $k_p$, and $t$ restricts to a generator $\theta$ of $W[\varpi]$ over $W$. Its two geometric points are $\theta$ and its conjugate $\bar\theta$. Hence at most two elliptic sections pass through $x$, and their lifts satisfy $v_\varpi(t_1-t_2)=v_\varpi(\theta-\bar\theta)=v_\varpi(\mathfrak d_{k_p/\mathbf Q_p})$. This is $2$ for $\mathbf Q_2(i)$ and $1$ for $\mathbf Q_3(\zeta_3)$, in agreement with [We, Section 4]. The group $H$ is generated by a unit of $\mathcal O_k$ and acts on $Z$ through automorphisms of the canonical lift, so it fixes $t_1$ and $t_2$. Since $Q(t)=\prod_{h\in H}(h(t)-t_2)$ is $H$-invariant, $Q=f(z)$ with $f(z)=(\text{unit})\cdot(z-z(t_2))$. Evaluating at $t_1$,
$$v_\varpi\big(z(t_1)-z(t_2)\big)=m\,v_\varpi(t_1-t_2)\in\{4,3\}.$$
The supplement checks this multiplication of lengths on the involution $t\mapsto-(t+2)/(t+1)$ at $p=2$. In $K=\mathbf Q(\zeta_{12})$ both $2$ and $3$ have $e_v=f_v=2$, and the uniformizer of $K_v$ is that of $k_p$. Summing $\frac14\,\mathrm{length}\cdot\log N(v)$ over $v\mid p$ gives the stated bounds.

(c) Each elliptic section meets at most one other at each $v\mid p$, and $a_ia_j\le\frac49<1$. Summing over ordered pairs gives the bound. $\square$

**Remark 3.4.** It is tempting to identify the deformation coordinate with a coordinate on the coarse space, which would give the length $v(\mathfrak d)$ on the coarse model. This is incorrect. For the involution above, $t_+-t_-=2i$ while $z_+-z_-=-4i$, which is the factor $m$ in Lemma 3.3(b).

## 4. The self-intersection of the orbifold canonical bundle

**Lemma 4.1 (comparison in codimension one).** Let $p\mid M$ and $\pi:\mathcal X_M\to\mathcal X_{M/p}$. Then, as $\mathbf Q$-Weil divisors,
$$L_M=\pi^*L_{M/p}+C_2 .$$

*Proof.* On a normal surface it suffices to compare coefficients at codimension one points.

*Horizontal divisors.* If $P\mapsto Q$ has ramification index $r$ on the generic fibre, the orbifold orders satisfy $m_Q=rm_P$. The coefficient of $P$ in $L_M-\pi^*L_{M/p}$ is $(r-1)+(1-1/m_P)-r(1-1/m_Q)=0$.

*Vertical divisors over $q\ne p$.* At the generic points of the fibres over $q$ the map $\pi$ forgets a level structure prime to $q$, which is étale on fine covers, and coarsening introduces no inertia at these generic points. This is the argument in the proof of [Y2, Lemma 2.1], which treats both $q\nmid D$ and $q\mid D$ (the non-split case). So the coefficient is $0$.

*The fibre over $p$.* On $C_1$ the map $\pi$ is generically an isomorphism, so the coefficient is $0$. At the generic point of $C_2$, which is ordinary, Serre–Tate coordinates (transported to false elliptic curves by [Bu, Theorem 4.5, Corollary 4.6]) give $\widehat{\mathcal O}_{\mathcal X_{M/p}}\to\widehat{\mathcal O}_{\mathcal X_M}$ in the form $A=\mathbf Z_p[[T]]_{(p)}\to B=\mathbf Z_p[[t]]_{(p)}$, $1+T=(1+t)^p$. The residue field extension $\mathbf F_p((T))\subset\mathbf F_p((t))$ is generated by $t$ and $e=1$, so $B=A[t]/(f)$ with $f(t)=(1+t)^p-1-T$. The different is $(f'(t))=(p(1+t)^{p-1})$, whose valuation along $C_2$ is $1$ because $C_2$ has multiplicity one in the fibre. Hence the coefficient of $C_2$ is $1$. $\square$

**Lemma 4.2 (thick nodes).** At a point $x$ with local ring $W[[u,v]]/(uv-p^k)$, the two branches $\{u=0\}$, $\{v=0\}$ have Mumford intersection number $1/k$.

*Proof.* The minimal resolution replaces $x$ by a chain $E_1,\dots,E_{k-1}$ of $(-2)$-curves, with the strict transform $\tilde C_1$ meeting $E_1$ and $\tilde C_2$ meeting $E_{k-1}$. The Mumford pull-back of $C_2$ is $\tilde C_2+\sum_{i=1}^{k-1}\frac ik E_i$, which is orthogonal to every $E_i$. Hence $C_1\cdot C_2=\tilde C_1\cdot(\tilde C_2+\sum\frac ikE_i)=\frac1k$. $\square$

**Lemma 4.3 (mass).** Let $p\mid M$ and $d'=d_{M/p}$. Summing over the geometric nodes $x$ of the fibre of $\mathcal X_M$ over $p$, with $k_x=\ell([I_x])$,
$$\sum_x\frac1{k_x}=\frac{\varphi(Dp)\psi(M/p)}{12}=\frac{p-1}2\,d' ,\qquad\text{hence}\qquad C_1\cdot C_2=\frac{p-1}2\,d'\log p .$$

*Proof.* By Section 2.2 the nodes correspond to the ideal classes of an Eichler order of level $M/p$ in $B_{Dp}$, and $k_x=\#\mathcal O_l(I_x)^\times/\{\pm1\}$. The Eichler mass formula [V, Theorem 25.3.18] gives $\sum_x 1/k_x=\frac1{12}\prod_{q\mid Dp}(q-1)\prod_{\ell\mid M/p}(\ell+1)$. Combine with Lemma 4.2. $\square$

**Proposition 4.4 (level-raising recursion).** For $p\mid M$,
$$\bar L_M^2=(p+1)\,\bar L_{M/p}^2+d_M\,\frac{3p+1}{2(p+1)}\log p ,$$
and consequently
$$\bar L_M^2=\psi(M)\,\bar L_1^2+d_M\sum_{p\mid M}\frac{3p+1}{2(p+1)}\log p .\tag{4.1}$$

*Proof.* Write $A=\bar L_{M/p}$ and $F'$ for the fibre of $\mathcal X_{M/p}$ over $p$; it is reduced and irreducible because $\mathcal X_{M/p}$ has good reduction at $p$. By Lemma 4.1, $\bar L_M=\pi^*A+C_2$, with $C_2$ carrying the trivial metric; at infinity the metric of $\bar L_M$ is the pull-back of that of $A$. Hence
$$\bar L_M^2=(\pi^*A)^2+2\,\pi^*A\cdot C_2+C_2^2 .$$
First, $(\pi^*A)^2=\deg(\pi)\,A^2=(p+1)A^2$. Second, $\pi_*C_2=pF'$ since Frobenius has degree $p$, so $\pi^*A\cdot C_2=p\,A\cdot F'=p\,d'\log p$. Third, the fibre is $C_1+C_2$ with multiplicities one, so $C_2\cdot(C_1+C_2)=0$ and $C_2^2=-C_1\cdot C_2=-\frac{p-1}2d'\log p$ by Lemma 4.3. Adding, the increment is $\big(2p-\frac{p-1}2\big)d'\log p=\frac{3p+1}2d'\log p$, and $d_M=(p+1)d'$. For the iteration, observe that a later prime $p'\mid M$ is unramified in codimension one at $p$, so the pull-back of $C_2^{(p)}$ is again reduced; the steps do not interact. $\square$

The supplement checks the identities in Lemma 4.3 and Proposition 4.4 over $1316$ triples $(D,M,p)$. It also checks the case $D=55$, $p=17$, where four of the $56$ superspecial points have $k_x=3$: $d'=20/3$, $\sum 1/k_x=52+4/3=160/3$, increment $\frac{520}3\log17$. Points with $k_x>1$ are thus accounted for with weight $1/k_x$ and produce no separate correction.

**Corollary 4.5.** With $c_*=-\zeta'(-1)/\zeta(-1)-\frac12$,
$$\bar L_M^2=d_M\Big[2c_*+\sum_{q\mid D}\frac{3q-1}{2(q-1)}\log q+\sum_{p\mid M}\frac{3p+1}{2(p+1)}\log p\Big].$$

*Proof.* Yuan's theorem [Y1, Theorem 1.1] states $\bar L_1^2/(2\deg L_1)=c_*+\sum_{q\mid D}\frac{3q-1}{4(q-1)}\log q$ for maximal $U$, with $\deg L_1=d_1$. Substitute into (4.1) and use $\psi(M)d_1=d_M$. $\square$

**4.6. Passage to a regular model.** Let $\widetilde{\mathcal X}\to\mathcal X_M\otimes\mathcal O_K$ be the minimal resolution. At $p\ge5$ the extension $K/\mathbf Q$ is unramified, and the singular points are the $A_{k-1}$ points of Section 2.2. At $2,3$ the model is smooth by Lemma 3.3(a), and stays smooth after base change. The resolution of a rational double point is crepant: if $K_{\widetilde{\mathcal X}}=\rho^*K+\sum b_iE_i$, adjunction gives $K_{\widetilde{\mathcal X}}\cdot E_i=0=\rho^*K\cdot E_i$, and negative definiteness forces $b_i=0$. By Proposition 3.2 the elliptic sections avoid the singular points. Hence the orbifold canonical bundle of $\widetilde{\mathcal X}$ is $\rho^*L_M$, its self-intersection is $\bar L_M^2$, and the heights of the $\sigma_i$ are unchanged. The model $\widetilde{\mathcal X}$ is regular and semistable. Its number of geometric singular points over $p$ is the Artin conductor $\delta_p$ entering [FvP, Theorem 10.1]. Each $A_{k-1}$ point contributes $k\ge1/k$ nodes, so by Lemma 4.3 and the Čerednik–Drinfeld description
$$\delta_p\ge\frac{p-1}{2(p+1)}d_M\ \ (p\mid M),\qquad \delta_q\ge\frac{\varphi(D/q)\psi(Mq)}{12}=\frac{q+1}{2(q-1)}d_M\ \ (q\mid D),\tag{4.2}$$
the second again by the mass formula for $B_{D/q}$ at level $Mq$.

## 5. Heights of elliptic sections

**Lemma 5.1.** For every elliptic section, $h_{\bar L_M}(\sigma_i)=\frac12\log N+O(1)$. Consequently $|\widehat{\deg}\,\psi_W|=O(e\log N)$, where $\psi_W=\sum_i(1-m_i^{-2})\psi_{i,W}$ is the metrized psi bundle of [FvP, Section 10.1.2].

*Proof.* Iterating Lemma 4.1, $L_M=\pi^*L_1+\sum_{p\mid M}V_p$, where $V_p$ is a reduced sum of components over $p$; it is the pull-back of $C_2^{(p)}$. Let $k$ be the CM field of $\sigma_i$ and $p\mathcal O_k=\mathfrak p\bar{\mathfrak p}$ (Proposition 3.2). The $\Gamma_0(p)$-structure of the CM point is connected at one of the places $\mathfrak p,\bar{\mathfrak p}$ and étale at the other. Hence $\sigma_i$ meets $V_p$ transversally at the places of $K$ above exactly one of them, and these carry half of the local degree. So $(\sigma_i\cdot V_p)=\frac12\log p$ and
$$h_{\bar L_M}(\sigma_i)=h_{\bar L_1}(\pi\sigma_i)+\tfrac12\log M .$$
The point $\pi\sigma_i$ is the Heegner point of discriminant $-4$ or $-3$ on $X^D$. Pasten's formula [P, Theorem 13.2, (39)] gives $h(P_k)=-\frac{L'}{L}(0,\chi_k)+\frac12\log(D/d_k)$, which is $\frac12\log D+O(1)$. His height is the Arakelov degree of the Hodge bundle computed on fine levels, which agrees with $h_{\bar L_1}$ up to the fixed metric constant [Y2, Lemma 2.1]. Next, adjunction on the smooth locus gives $\sigma_i^*L_M=\frac1{m_i}\sigma_i^*\omega+\sum_{j\ne i}a_j\sigma_i^*\mathcal O(\sigma_j)$. The Wolpert metric on $\psi_i=\sigma_i^*\omega$ [FvP, Definition 4.13] differs from the metric induced by the orbifold hyperbolic metric by a constant depending only on $m_i$, because the hyperbolic cone of angle $2\pi/m_i$ has a universal model in rotationally symmetric coordinates. Therefore $\widehat{\deg}\,\psi_{i,W}=m_ih_{\bar L_M}(\sigma_i)-m_i\sum_{j\ne i}a_j(\sigma_i,\sigma_j)_{\rm fin}+O(1)$. The cross terms are $O(1)$ by Proposition 3.2 and Lemma 3.3. $\square$

## 6. Proof of Theorem 1.1

**Lemma 6.1 (one-sided spectral bound).** Let $\Gamma$ be a cocompact Fuchsian group with area $A$ and $e$ elliptic points of orders in $\{2,3\}$. Let $Z(s,\Gamma)$ be its Selberg zeta function. Then $\log Z'(1,\Gamma)\le C_0(A+e+1)$ with an absolute constant $C_0$.

*Proof.* Let $\Theta(t)=\mathrm{Tr}\,e^{-t\Delta}$. The Selberg trace formula writes $\Theta=I+E+H$. The identity term is $I(t)=A\,k(t)$ with a universal function $k(t)=\frac1{4\pi t}-\frac1{12\pi}+O(t)$ as $t\downarrow0$. The elliptic term $E(t)$ is a sum of at most $2e$ universal functions, one for each elliptic conjugacy class (order $m\in\{2,3\}$, rotation $k\in\{1,\dots,m-1\}$), each smooth on $[0,1]$. The hyperbolic term $H(t)=\sum_\gamma\frac{\ell(\gamma_0)}{2\sinh(\ell(\gamma)/2)}\frac{e^{-t/4-\ell(\gamma)^2/(4t)}}{\sqrt{4\pi t}}$ is non-negative and decays faster than any power as $t\downarrow0$. Thus $I+E=\frac at+b+R(t)$ with $a=A/(4\pi)$, $|b|\le C(A+e)$ and $\int_0^1|R(t)|\frac{dt}t\le C(A+e)$. Splitting the Mellin transform of $\Theta-1$ at $t=1$ and differentiating at $s=0$ gives
$$\log{\det}'\Delta=a-\gamma(b-1)-\int_0^1R(t)\frac{dt}t-\int_0^1H(t)\frac{dt}t-\int_1^\infty(\Theta(t)-1)\frac{dt}t .$$
The last two integrands are non-negative, because $H\ge0$ and $\Theta-1=\sum_{\lambda_j>0}e^{-t\lambda_j}\ge0$. Dropping them gives $\log\det'\Delta\le C(A+e+1)$. By [FvP, Proposition 8.1] with $c=0$ (there are no model cusps, so the relative zeta function of [FvP, §8.2] is $\sum_{\lambda_j>0}\lambda_j^{-s}$ and $\det(\Delta_{\rm hyp},\Delta_a)=\det'\Delta$; the setting of [FvP, §8, §10.1.1] allows $c=0$), $\log\det'\Delta-\log Z'(1,\Gamma)$ is a fixed linear combination of $2g-2+\sum_i(1-m_i^{-1})$ and of the numbers of elliptic points of each type. $\square$

No spectral gap is needed. Small eigenvalues enlarge the discarded integral $\int_1^\infty(\Theta-1)\,dt/t$, which only helps the upper bound.

**6.2. Conclusion.** The arithmetic Riemann–Roch theorem [FvP, Theorem 10.1] for $\widetilde{\mathcal X}\to\operatorname{Spec}\mathcal O_K$ with the sections $\sigma_i$ reads
$$12\,\widehat{\deg}\,\lambda(\mathcal O)_Q-\delta+\widehat{\deg}\,\psi_W=\bar L_M^2-\sum_{i\ne j}a_ia_j(\sigma_i,\sigma_j)_{\rm fin},$$
where $\delta=\sum_p\delta_p\log p$. The Quillen metric is $\|\cdot\|_Q=(C(\Gamma)Z'(1,\Gamma))^{-1/2}\|\cdot\|_{L^2}$, and by Serre duality $\widehat{\deg}\,\lambda(\mathcal O)_{L^2}=h_F(J)+O(\log A+1)$. Hence
$$12\,h_F(J)=\bar L_M^2+\delta-\widehat{\deg}\,\psi_W-\sum_{i\ne j}a_ia_j(\sigma_i,\sigma_j)_{\rm fin}-6\log Z'(1,\Gamma)+O(g+e).\tag{6.1}$$
We bound each term from below.
- By Corollary 4.5 and (4.2), the coefficient of $d_M\log q$ for $q\mid D$ is $\frac{3q-1}{2(q-1)}+\frac{q+1}{2(q-1)}=\frac{2q}{q-1}$; we keep this factor rather than bounding it by $2$. The coefficient of $d_M\log p$ for $p\mid M$ is $\frac{3p+1}{2(p+1)}+\frac{p-1}{2(p+1)}=\frac{2p}{p+1}$. So
$$\bar L_M^2+\delta\ \ge\ 2d_M\Big[\sum_{q\mid D}\frac q{q-1}\log q+\sum_{p\mid M}\frac p{p+1}\log p\Big]-O(d_M).$$
- $-\widehat{\deg}\,\psi_W\ge-O(e\log N)$ by Lemma 5.1.
- $-\sum a_ia_j(\sigma_i,\sigma_j)_{\rm fin}\ge-O(e)$ by Proposition 3.2 and Lemma 3.3(c).
- $-6\log Z'(1,\Gamma)\ge-O(g+e)$ by Lemma 6.1, since $A=2\pi d_M$ in the curvature $-1$ normalization and $d_M=O(g+e)$.

By (0.1), $d_M\ge2g-2$, and $e\le2^{\omega(N)+1}$. This proves Theorem 1.1. $\square$

**Remark 6.3 (what positivity alone gives).** Faltings' Noether formula [F, Theorem 6], [MB] is $12h_F=\bar\omega_{\rm Ar}^2+\sum_p\delta_p\log p+\delta_F(X(\mathbf C))-4g\log2\pi$. Combine it with $\bar\omega_{\rm Ar}^2\ge0$ [F, Theorem 5], with Wilms' bound $\delta_F>-2g\log2\pi^4$ [Wi, Corollary 1.2], and with $\delta_p\ge t_p$, the toric rank: $t_q=g$ for $q\mid D$ and $t_p=g\frac{p-1}{p+1}-O(2^{\omega(N)})$ for $p\mid M$. This yields $12h_F\ge g[\log D+\sum_{p\mid M}\frac{p-1}{p+1}\log p]-O(g+2^{\omega(N)}\log N)$, i.e. the constant $1/12$. Theorem 1.1 improves this to $1/3$. The improvement comes from evaluating $\bar L^2$ instead of using its positivity, together with the mass-weighted node count (4.2).

## 7. The Petersson-ratio channel for abc

We recall the setting of Pasten [P] (numbering of arXiv:1705.09251v4). Let $a+b=c$ be coprime positive integers, $R=\mathrm{rad}(abc)$, $E$ the Frey curve and $N$ its conductor. For a suitable factorization $N=DM$ with $D>1$, Pasten bounds $\prod_{p\mid D}v_p(\Delta_E)$ through [P, (54)]:
$$\log\prod_{p\mid D}v_p(\Delta)=2\log c_f+2\log\|f\|-2\log\|f_{D,M}\|+\log D+O_S\Big(\log\log N+\frac{\log D}{\log\log D}\Big),$$
where $f$ is the newform of $E$, $f_{D,M}$ its integral Jacquet–Langlands transfer to $S_2^D(M)$, and $c_f$ the Manin constant. The denominator is controlled by [P, Theorem 14.1]: $-\log\|h\|\le(\frac56+\epsilon)\log N+\frac12\log M$ for every non-zero integral $h\in S_2^D(M)$. This gives $\prod_{p\mid abc}v_p(abc)\ll_\epsilon R^{8/3+\epsilon}$ [P, Theorem 16.7].

**Definition 7.1 (exponent-profile relaxation).** For a squarefree $R$ with largest prime factor $P$, a number $C\ge1$ and a family $\mathcal V=\{(D,V_D)\}$ of divisors $D\mid R$ with bounds $V_D\ge1$, put
$$\mathcal B(R;C,\mathcal V)=\max\Big\{\sum_{p\mid R}e_p\log p:\ e_p\in\mathbf Z_{\ge1},\ e_p\le C,\ \prod_{p\mid D}e_p\le V_D\ \text{for all }(D,V_D)\in\mathcal V\Big\}.$$
Since $\log c\le\sum_{p\mid R}v_p(abc)\log p$, any upper bound for $\log c$ derived only from per-prime bounds $v_p(abc)\le C$ and product bounds $\prod_{p\mid D}v_p(abc)\le V_D$ is at least $\mathcal B(R;C,\mathcal V)$. We say that such a derivation stays *inside the relaxation model*. The model discards the additive relation $a+b=c$ and every other input, such as linear forms in logarithms. It is an assumption about the method and not a theorem about Pasten's argument.

**Lemma 7.2.** Let $m=\min(\lfloor C\rfloor,\min_{D\ni P}\lfloor V_D\rfloor)$. Then $\mathcal B(R;C,\mathcal V)\ge\log R+(m-1)\log P$.

*Proof.* The profile $e_P=m$, $e_p=1$ for $p\ne P$ is admissible: every product $\prod_{p\mid D}e_p$ is $1$ or $m$. $\square$

**Proposition 7.3 (lattice ceiling).** Let $\mathcal L\subset S_2^D(M)$ be Pasten's lattice of integral forms and $\mu(\mathcal L)=\min_{0\ne h\in\mathcal L}\|h\|^2$. Under the hypotheses of Theorem 1.1, $\mu(\mathcal L)\le N^{1/3+o(1)}$, uniformly in $(D,M)$.

*Proof.* The Néron cotangent lattice $\Omega_J$ of $J$ is contained in $\mathcal L$ (via the difference map $X\times X\to J$ on the smooth locus, extended by the Néron property). Its Gram matrix $G$ for the Petersson product satisfies $\det G=\exp(-2h_F(J)+O(g))$; the factor $e^{O(g)}$ accounts for the normalization of the Petersson norm in [P]. Hermite's inequality gives $\mu(\mathcal L)\le\mu(\Omega_J)\le\gamma_g(\det G)^{1/g}$ with $\gamma_g\le1+g/4$. By Corollary 1.2, $(\det G)^{1/g}\le N^{-2/3+o(1)}$, and $g\le N$. $\square$

**Corollary 7.4.** Let $\mathcal F$ be the set of coprime triples $a+b=c$ with $3\nmid abc$ whose Frey curve has good reduction at $2$, i.e. $r=0$ in [P, Theorem 16.7], and with $\omega(abc)$ large enough that the proof of [P, Theorem 16.7] uses Theorem 16.4. For such a triple let $V_D$ be any bound obtained by substituting into [P, (54)] an upper bound $U\ge\|f\|^2$ and a lower bound $\beta_{D,M}$ valid for all non-zero integral forms in $S_2^D(M)$, as in [P, Theorem 14.1]. Let $C\ge R^{2/3}$, e.g. $C\asymp R\log R$ from $v_p(\Delta)\ll N\log N$. Then
$$\mathcal B(R;C,\mathcal V)\ \ge\ R^{2/3-o(1)} .$$
Consequently no derivation inside the relaxation model with these inputs yields $\log c\ll R^{1/3-\eta}$ for any $\eta>0$ on $\mathcal F$.

*Proof.* For $r=0$ and $3\nmid abc$ we have $\gcd(N,6)=1$ and $N=R/2$. The factorizations used in [P, Theorem 16.7] are $(D,M)=(p_1\cdots p_m,1)$ for $m$ even, and $(p_1\cdots p_m/(p_{j_1}p_{j_2}p_{j_3}),\,p_{j_1}p_{j_2}p_{j_3})$ for $m$ odd. All are squarefree with $D>1$, so Proposition 7.3 applies. Since $\beta_{D,M}\le\mu(\mathcal L)\le N^{1/3+o(1)}$ and $U\ge\|f\|^2=N^{1+o(1)}$ (see [P, Section 3]), and since $2\log c_f\ge0$ and $\log D\ge0$, every such $V_D$ satisfies $V_D\ge (U/\beta_{D,M})\,N^{-o(1)}\ge N^{2/3-o(1)}$; the error term in [P, (54)] is $N^{o(1)}$. Lemma 7.2 concludes. $\square$

**7.5. The family is infinite.** Take $(a,b,c)=(16t,1,16t+1)$ with $t\equiv1\pmod6$. The substitution $x=4X$, $y=8Y+4X$ transforms $y^2=x(x-16t)(x+1)$ into $Y^2+XY=X^3-4tX^2-tX$. The latter has discriminant $t^2(16t+1)^2$, which is prime to $6$ (checked in the supplement). Hence the conductor is $\mathrm{rad}(t(16t+1))$, prime to $6$. By the Chinese remainder theorem, $t$ can be chosen divisible by any finite set of primes $\ge5$, so $\omega(abc)$ is unbounded on the family. The smallest member $(16,1,17)$ has conductor $17$ and does not satisfy the size condition on $\omega(abc)$.

**7.6. Scope.** Corollary 7.4 says that the Petersson-ratio channel, with the two norms bounded independently and the outputs combined only through Definition 7.1, has exponent at least $2/3$ on $\mathcal F$. The ceiling in Proposition 7.3 applies to every bound that holds for all integral forms. It says nothing about bounds specific to the eigenform $f_{D,M}$, about correlated estimates for $\|f\|$ and $\|f_{D,M}\|$, or about arguments that use the additive structure. Pasten's subexponential bounds [P2] combine the product bound with linear forms in logarithms. They lie outside Definition 7.1 and are not affected.

## Verification and supplement

The load-bearing arguments of Sections 3–6 were checked independently by two AI systems; each found local errors, and these are corrected in the present text (Remark 3.4; the global coefficient $\frac12\log p$ in Lemma 5.1; the Čerednik–Drinfeld argument in Lemma 4.1). The cited theorem numbers were compared with the sources. The supplement contains a standard-library Python script with exact rational checks of:
- the discriminant table of Lemma 3.1;
- the identities of Lemma 4.3, Proposition 4.4 and (4.2) over many $(D,M,p)$;
- the case $D=55$, $p=17$, together with the Eichler class number formula;
- the length multiplication of Lemma 3.3 on an explicit involution;
- the Frey model of 7.5.

It also contains one finite numerical illustration of the uniformity $\sum_{p\mid M}\log p/(p+1)=o(\log N)$.

## References

- [AU] A. Abbes, E. Ullmo, Auto-intersection du dualisant relatif des courbes modulaires $X_0(N)$, J. reine angew. Math. 484 (1997), 1–70.
- [BBC] D. Banerjee, D. Borah, C. Chaudhuri, Arakelov self-intersection numbers of minimal regular models of modular curves $X_0(p^2)$, Math. Z. 296 (2020); arXiv:1710.10915.
- [Bu] K. Buzzard, Integral models of certain Shimura curves, Duke Math. J. (1997), 591–612, doi:10.1215/S0012-7094-97-08719-6.
- [Co] B. Conrad, The Keel–Mori theorem via stacks, preprint (2005).
- [F] G. Faltings, Calculus on arithmetic surfaces, Ann. of Math. 119 (1984), 387–424.
- [Fr] G. Freixas i Montplet, The Jacquet–Langlands correspondence and the arithmetic Riemann–Roch theorem for pointed curves, Int. J. Number Theory 8 (2012).
- [FvP] G. Freixas i Montplet, A.-M. von Pippich, Riemann–Roch isometries in the non-compact orbifold setting, arXiv:1604.00284; J. Eur. Math. Soc. (2020).
- [G] B. H. Gross, On canonical and quasi-canonical liftings, Invent. Math. 84 (1986), 321–326.
- [GvP] M. Grados, A.-M. von Pippich, Self-intersection of the relative dualizing sheaf on modular curves $X(N)$, arXiv:2205.11437.
- [JK] J. Jorgenson, J. Kramer, Bounds on Faltings's delta function through covers, Ann. of Math. 170 (2009), 1–43.
- [K] U. Kühn, Generalized arithmetic intersection numbers, J. reine angew. Math. 534 (2001), 209–236.
- [KRY] S. Kudla, M. Rapoport, T. Yang, Modular forms and special cycles on Shimura curves, Ann. of Math. Stud. 161, Princeton (2006).
- [Ma] H. Mayer, Self-intersection of the relative dualizing sheaf on modular curves $X_1(N)$, J. Théor. Nombres Bordeaux 26 (2014).
- [MB] L. Moret-Bailly, La formule de Noether pour les surfaces arithmétiques, Invent. Math. 98 (1989), 491–498.
- [MU] P. Michel, E. Ullmo, Points de petite hauteur sur les courbes modulaires $X_0(N)$, Invent. Math. 131 (1998), 645–674.
- [P] H. Pasten, Shimura curves and the abc conjecture, J. Number Theory (2024); arXiv:1705.09251v4.
- [P2] H. Pasten, The largest prime factor of $n^2+1$ and improvements on subexponential abc, Invent. Math. (2024); arXiv:2312.03566.
- [Pr] K. Prasanna, Integrality of a ratio of Petersson norms and level-lowering congruences, Ann. of Math. 163 (2006), 901–967.
- [St] J. Stankewicz, Twists of Shimura curves, arXiv:1208.3594.
- [SY] C. L. Stewart, K. Yu, On the abc conjecture II, Duke Math. J. 108 (2001), 169–181.
- [U] E. Ullmo, Hauteur de Faltings de quotients de $J_0(N)$, discriminants d'algèbres de Hecke et congruences entre formes modulaires, Amer. J. Math. 122 (2000), 83–115.
- [V] J. Voight, Quaternion Algebras, Grad. Texts in Math. 288, Springer (2021).
- [We] S. Wewers, Canonical and quasi-canonical liftings, in: ARGOS Seminar on Intersections of Modular Correspondences, Astérisque 312 (2007), 67–86.
- [Wi] R. Wilms, New explicit formulas for Faltings' delta-invariant, Invent. Math. 209 (2017), 481–539.
- [Y1] X. Yuan, Modular heights of quaternionic Shimura curves, arXiv:2205.13995.
- [Y2] X. Yuan, Explicit Kodaira–Spencer map over Shimura curves, arXiv:2205.11334.

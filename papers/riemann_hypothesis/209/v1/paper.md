# Dyadic harmonic jet depths at CM points on the original unitary period lattices

## 1. Statement

On either dyadic coefficient label and every fitted unitary component, we construct a good-reduction CM point on the original homology lattice. An odd-degree isogeny identifies its formal group with a product of ordinary and supersingular factors. We use this product to bound from below every harmonic jet on every integral chart of an adapted frame. A test built from integral formal characters provides the matching upper bound to leading order.

We use the fitted conductor-one family of Levent Alpöge and Claude [1] and the period normalization of Paper 208 [2]. On lift $1\le j\le m$, put
$$
r_+=k+j-1,\qquad q=m-j,\qquad d=r_+-q>0 .
$$
Here $r_+$ and $q$ are the tangent ranks on the fixed CM type and its conjugate. We call these the positive and negative labels. Under either dyadic coefficient embedding the two types occupy conjugate places $v,\bar v$ of the host CM field $E$, above a split place of $E^+$. Write $R=\mathcal O_{\mathbf C_2}$ and normalize $v_2(2)=1$. An integral character is a formal group homomorphism to $\widehat{\mathbf G}_m$ over $R$. We measure lattice colength by the valuation of the determinant ideal. A saturated frame at a label is an ordered basis of the integral lattice in its tangent eigenspace. [3, 4]

Write $a_{\tau,i}$ for the pinned dominant, integral chart weights, with rows numbered from zero. A frame is adapted to the product if every row belongs to either its ordinary or its supersingular tangent space. Let $D$ be the sum of all row weights, $B$ their sum on negative labels, and $D_{\rm ss}$ their sum on supersingular rows. Let $J$ be the total number of differentiation letters, one per labelled row per copy. Put $c=\lceil v_2(\mathfrak D_{E_v/\mathbb Q_2})\rceil$, where an ideal's valuation is that of a generator. The two host completions give the same $c$. Define
$$
\mathcal E
=B\bigl(c+2+\log_2(D+1)+\log_2(B+1)\bigr)
 +J\bigl(1+\log_2(D+1)\bigr).
$$

**Theorem.** Every fitted component on every lift admits a CM point which, after finite extension at either dyadic coefficient label, has good reduction and receives an $\mathcal O_E$-linear isogeny of odd degree from $q$ hyperbolic Serre tensors of the elliptic curve $Y^2+Y=X^3$ and a definite ordinary part of $E$-rank $d$. Each hyperbolic tensor contributes one supersingular direction at every label. Both orders of the ordinary and supersingular bases give admitted integral frames on the same unframed point.

For either of these frames $y$, let $\lambda$ be its dyadic place on the moduli coefficient field and $e_\lambda=\operatorname{ord}_\lambda(2)$, with $\operatorname{ord}_\lambda$ taking value one on uniformizers. On **every** integral chart $C$ of $y$, the unrestricted harmonic polynomial and integral germ infimum satisfies
$$
\tfrac23 D_{\rm ss}-\mathcal E
\ \le\ \frac{\nu_{\rm loc,C}(y)}{e_\lambda}
\ \le\ \tfrac23 D_{\rm ss}.
\tag{1}
$$
The same bounds hold for the infimum $\nu_{\rm loc}(y)$ over charts. The proof gives (1) for any adapted order of the summands. In an arbitrary saturated frame, the prefix lattice computation in §4 gives the exact minimum for the character determinant test.

Let $T$ be the fitted order cutoff and $Q=n_Tmb\delta_2/2$ the normalization in Paper 208, with the parameters specified in §6. The one-sided sums of $T\nu_{\rm loc}(y)/e_\lambda$, divided by $Q$, are asymptotic to $mn/(3n_T)$ in the ordinary-first order and $2mn/(3n_T)$ in the supersingular-first order. In particular the supremum $\nu_W$ over algebraic framed points satisfies, at either dyadic coefficient label,
$$
\frac{1}{Q}\sum_{j=1}^m \frac{T\nu_W(\lambda,j)}{e_\lambda}
\ \ge\ \bigl(\tfrac23-o(1)\bigr)\frac{mn}{n_T}.
\tag{2}
$$

## 2. CM points with the original lattice

Fix the period label for the prescribed component at a complex embedding of its coefficient field. Write $\Lambda$ for its projective $\mathcal O_E$-lattice, $V=\Lambda\otimes_{\mathbb Z}\mathbb Q$, and $\psi$ for its unimodular alternating form. The pinned period domain consists of the compatible complex structures with the prescribed multiplicities. Its period map retains the level marking of $\Lambda$. Put $F=E^+$ and write $K_0=\mathbb Q(\eta)\subset E$ with $\eta^2=-D_0<0$, oriented so that every positive embedding sends $\eta$ to $i\sqrt{D_0}$. The original form can be written as $\psi(x,y)=\operatorname{Tr}_{E/\mathbb Q}(\eta H(x,y))$, with $H$ Hermitian and conjugate-linear in its first variable. The signature of $H$ is $(r_+,q)$ at every real place of $F$. The fitted host has $2$ split in $K_0$ and two conjugate places $v,\bar v$ over $2$ in $E$, with residue degree two. The residue degree also follows from the real dyadic cyclotomic factor being totally ramified and the inert quadratic factor of the fitted host at $2$. [3]

### Rational Witt decomposition and the CM type

The Hermitian space has an orthogonal decomposition into $q$ hyperbolic planes and a totally positive definite space of rank $d$. To see this, at each step with a negative direction left, consider the quadratic form $x\mapsto H(x,x)$ over $F$ on the remaining space. At a nonsplit finite place its dimension is at least $2(d+2)\ge6$, so it is isotropic by the local theorem on quadratic forms in at least five variables. At a split place an entire idempotent summand is isotropic. At every real place the signature is still indefinite. The Hasse–Minkowski theorem gives a nonzero isotropic vector over $F$, which gives a Hermitian isotropic line over $E$. Pair it with a vector of Hermitian pairing one and subtract half that vector's norm times the isotropic vector to split off a hyperbolic plane. Its orthogonal complement has one fewer positive and negative direction. Iterating gives the decomposition, with the $q=0$ case already definite. [11]

On each plane use an isotropic basis with Gram matrix $H_0$ and give the plane an action of $K_1=\mathbb Q(\sqrt{-3})$ by sending $\sqrt{-3}$ to $I$, where
$$
H_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
I=\begin{pmatrix}0&\eta\\3\eta/D_0&0\end{pmatrix}.
$$
Then $I^2=-3$, $I^*H_0=-H_0I$, and $H_0I=\operatorname{diag}(3\eta/D_0,\eta)$. Take the real complex structure $J=I/\sqrt3$. It preserves $\psi$, and $\psi(Jx,x)>0$ for $x\ne0$ because $-\eta H_0I$ is positive at the oriented embeddings. Its two complex eigenvalues give one positive and one negative direction at each real place. On the definite complement take $J=i$ at each oriented embedding. This is the pure $K_0$ type. The construction therefore gives a point of the required period domain.

On a plane the commuting actions make it free of rank one over $E\otimes_{\mathbb Q}K_1$. If this algebra is a field, this follows by dimension. If it splits, the two eigenspaces are lines since $I$ has minimal polynomial of degree two over $E$. The rational Hodge structure of the plane is the Serre tensor of the pure $K_1$ elliptic type with $E$ over $\mathbb Q$, with complex structure given by $\sqrt{-3}/\sqrt3$. The complement similarly has the Hodge structure of a rank-$d$ tensor over $K_0$ with $E$. The comparison product can thus be taken to be
$$
B=(\mathcal O_E\otimes_{\mathbb Z} C)^q
 \times(\mathcal O_E\otimes_{\mathcal O_{K_0}} C_0)^d ,
$$
where $C$ is the elliptic curve of the theorem with the indicated $K_1$ action and $C_0$ is an elliptic curve with full $\mathcal O_{K_0}$ multiplication of the indicated type. These Serre tensors use finite projective modules. After finite extension $C_0$ has good reduction. The two $K_0$ dyadic idempotents cut out groups of height one, one of dimension one and the other of dimension zero. They give the multiplicative and étale parts over the geometric base, proving ordinarity. In the ordinary tensor the tangent action has the positive type. [3, 6, 12]

### Aligning the lattice at the split place

Let $\mathfrak p$ be the place of $F$ below $v,\bar v$. The split local space is $V_v\oplus V_{\bar v}$. The alternating form pairs the two summands perfectly over $\mathbb Q_2$ and is zero on either summand. The lattice $\Lambda\otimes\mathbb Z_2=\Lambda_v\oplus\Lambda_{\bar v}$ is self-dual, so $\Lambda_{\bar v}$ is the trace-pairing dual of $\Lambda_v$. This dual is defined using the original $\psi$ and $\mathbb Z_2$, so it includes the different of the local trace. [3]

On each hyperbolic plane in $V_v$, the full order $\mathcal O_{E_v}\otimes_{\mathbb Z_2}\mathcal O_{K_1,2}$ is a product of two copies of $\mathcal O_{E_v}$. Indeed $\mathcal O_{K_1,2}$ is unramified quadratic and embeds into $\mathcal O_{E_v}$ by the residue-degree condition. Choose a lattice line in each of its two idempotent summands. Their direct sum is free of rank one over the product order. It is stable under the entire Eisenstein order, including $(1+I)/2$. Choose any full $\mathcal O_{E_v}$-lattice in the definite part and take the direct sum to obtain a lattice $L_v$ in $V_v$. At $\bar v$ choose its trace-pairing dual $L_{\bar v}$. The rational decomposition is orthogonal, so this dual decomposes by the same factors. The adjoint action of each of the two orders preserves $L_v$, hence the orders preserve $L_{\bar v}$. Its hyperbolic summands are likewise free of rank one over the product order, using one lattice line in each of the two rational eigenspaces.

The split unitary group $U(H)(F_{\mathfrak p})$ acts as $\mathrm{GL}(V_v)$ on $V_v$ and by the dual action on $V_{\bar v}$. A local element can send $L_v$ onto $\Lambda_v$, and then sends $L_{\bar v}$ onto $\Lambda_{\bar v}$. This condition defines a nonempty open subset of the local group. It contains an element in the Cayley chart, where $1+g$ is invertible, since the complement of the chart is a proper determinant locus in the split general linear group. The inverse Cayley transform is skew-adjoint. Approximate it by a rational skew-adjoint endomorphism using density of $F$ in $F_{\mathfrak p}$, and apply the Cayley transform to obtain $g\in U(H)(F)$ with the same lattice-matching property. Replace $J$ by $gJg^{-1}$ and transport the rational summands and their auxiliary actions by $g$. The original $\Lambda$, $\psi$, and the two period markings are kept. Compatibility and the signature persist, so the complex torus with the new complex structure is the point on the prescribed component obtained from that marked period domain. [3]

### The odd-degree comparison and good reduction

The component point with its rigidified polarization and markings is a CM abelian variety by the tensor Hodge description. Its rational Hodge isomorphism with $B$ can be chosen integral and invertible at $2$. In detail, at $2$ the source lattice on each hyperbolic plane is a free rank-one module over the same product order at each host place, and on the definite part it is free of rank $d$ over $\mathcal O_{E_v}$ and $\mathcal O_{E_{\bar v}}$. Thus the two sides admit a dyadic isomorphism commuting with the auxiliary actions, factor by factor. Having fixed a rational Hodge isomorphism on each factor, approximate the required dyadic correction in the Hodge endomorphism subalgebra $E\otimes_{\mathbb Q}K_1$ on a plane and $\mathrm{Mat}_d(E)$ on the definite part. Rational points of their underlying vector spaces are dense in the dyadic completions. Invertibility and the condition of matching the lattices are open. This produces a rational Hodge isomorphism carrying $H_1(B,\mathbb Z_2)$ onto $\Lambda\otimes\mathbb Z_2$. In integral homology coordinates its entries have only odd denominators. Clear them by an odd integer. The resulting map sends the integral source lattice inside the target with odd index, so it induces an $\mathcal O_E$-linear isogeny of odd degree. The comparison isogeny is unpolarized. The target polarization and markings come from $\psi$ and the original period marking, including the auxiliary marking on the generic fibre. [3, 12]

The abelian variety, actions, isogeny and finite marking data descend after finite extension of the coefficient field by CM descent and algebraicity of homomorphisms. At either chosen dyadic coefficient place, extend the completion until the product has good reduction and the odd-order kernel is defined. The kernel extends as a finite étale subgroup of the odd-order torsion of the product model. The quotient abelian scheme gives the good model of the original point. The isogeny and its quasi-inverse up to multiplication by an odd integer act on the good models, and multiplication by that integer is invertible on their $2$-divisible groups and formal completions. This gives an integral equivariant product decomposition there. The same unframed CM point on a component can be completed above either coefficient label. The finite extension and the local frames may depend on the label. [4, 12]

## 3. Character differentials on the integral chart

Over the complete trait giving good reduction, the completion of the abelian scheme at the identity is the chart formal group. In an integral chart the model has the same generic fibre and the same $\mathcal O_E$ action. The generic isomorphism extends in both directions by full faithfulness for semiabelian models, and the chart uses integral formal coordinates on this model. The special fibre has torus rank zero. Use the good-model splitting at $2$ supplied by the odd-degree isogeny in §2. All tangent identifications and restrictions below respect the original $\mathcal O_E$ action. [4]

Let $C$ be the elliptic curve $Y^2+Y=X^3$. Its discriminant is $-27$, and its reduction over $\mathbf F_2$ has three points. Thus Frobenius has trace zero and its square is $[-2]$. In a parameter over the dyadic integers the series $[-2](X)$ has linear term $-2X$ and reduces to $X^4$. The $\mathbb Z[\zeta_3]$ action induces the action of the integers of the unramified quadratic field $L=\mathbf Q_2(\zeta_3)$, with the embedding on the tangent line as structure map. The formal group is Lubin–Tate for $-2$. [5]

Schneider–Teitelbaum identify the group of integral characters over $R$ with the dual Lubin–Tate Tate module, free of rank one over $\mathcal O_L$. If $\Omega$ is the differential of a module generator, the differentials are $a\Omega$ with $a\in\mathcal O_L$ acting through the tangent embedding. Lemma 3.4(b) gives
$$
v_2(\Omega)=\frac{1}{2-1}-\frac{1}{1\cdot(4-1)}=\frac23.
$$
Thus $\Omega R$ is the span of differentials, and an actual character supplies its generator. The good models and bases in the theorem are defined over a finite dyadic field. The character test uses the geometric valuation ring. In particular the dual Tate module on the supersingular elliptic factor has no invariants over a finite extension, since on an open subgroup of inertia its character is the cyclotomic character divided by the Lubin–Tate character, which is the conjugate of the latter via the norm formula. [5]

A $\mathbb Z_2$-basis of $\mathcal O_E\otimes\mathbb Z_2$ identifies the formal group of the Serre tensor with a product of copies of the elliptic formal group. A character of a product is the product of its restrictions to the factors. Hence the character differential span on the whole supersingular cotangent lattice is $\Omega$ times that lattice. For the ordinary part, the Cartier dual of the connected $2$-divisible group is étale and becomes constant over the geometric base. The resulting multiplicative coordinates give characters with differentials a basis of the whole ordinary cotangent lattice. [5, 6]

To restrict to one label, take a finite extension on which the eigenvalues are defined. The kernel of the simultaneous equations defining that eigenspace is saturated in the finite free tangent module over the DVR, since the quotient embeds into a finite direct sum of free modules. It is therefore a direct summand. Its basis stays an integral eigenspace basis over $R$ by flat base change of the kernel. This argument applies separately to the ordinary and supersingular factors. Restriction from each integral cotangent lattice onto the dual of its saturated tangent eigenspace is surjective. The resulting differential spans at a positive and a negative label, respectively, are
$$
R^d\oplus\Omega R^q,\qquad \Omega R^q,\qquad v_2(\Omega)=\tfrac23.
\tag{3}
$$
The argument uses one label at a time. The eigenspaces for distinct labels at the same host place may fail to split integrally. [4]

## 4. Prefix minors and admitted frames

Write $\lambda_{\tau,h}$ for the colength after projecting the character lattice onto the first $h$ rows. At a positive label,
$$
\tfrac23(h-d)_+\le\lambda_{\tau,h}\le\tfrac23\min(h,q),
\tag{4}
$$
where $(z)_+=\max(z,0)$. At a negative label it is $2h/3$. For a fixed positive label, after changing from a basis adapted to the character lattice to the given saturated frame, the full character lattice is generated by the columns of $U\operatorname{diag}(1^d,\Omega^q)$ for some $U\in\mathrm{GL}_{r_+}(R)$. Project to the first $h$ coordinates. Every $h$-column minor from these generators contains at least $(h-d)_+$ factors of $\Omega$. The first $h$ rows of $U$ have rank $h$ over the residue field, so one of their $h$-column minors is a unit. The corresponding scaled minor contains at most $\min(h,q)$ factors of $\Omega$. These minors generate the determinant ideal of the projected lattice and prove (4). At a negative label the image is $\Omega R^h$ in every saturated frame.

For one label choose a finite list of actual characters whose differentials span the full lattice. Such a list exists by the product calculation. Let $M_h$ be the image of the lattice on the first $h$ rows. Each $M_h$ is a finitely generated torsion-free module over a valuation ring, hence free, of rank $h$. Suppose characters have been chosen whose first $h-1$ coordinates form a basis of $M_{h-1}$. Their first $h$ coordinates give a section of the surjection $M_h\to M_{h-1}$ on that basis. Their span is therefore a direct summand, with free rank-one quotient. The images of the finite list generate this quotient. At least one image is a generator because $R$ is local. Appending that actual character gives a basis of $M_h$ while retaining all earlier basis projections. The induction starts with $M_0=0$. Every leading minor of the resulting ordered list generates the corresponding determinant ideal.

The pinned test has at least $\sum_\tau r_\tau$ copies. Its injection from labelled rows to copies assigns disjoint column slots across labels. Use the chosen characters in those slots and the trivial character in any unused slot. The restriction of a given column to other labels is immaterial because the polynomial uses it only at its assigned label. The pinned $\mathrm{crP}$ is the product of the leading minors of size $h$, each to the power $a_{\tau,h-1}-a_{\tau,h}$, with $a_{\tau,r_\tau}=0$ for a label of rank $r_\tau$. Its minimum valuation on character columns is
$$
M=\sum_\tau\sum_{h=1}^{r_\tau}(a_{\tau,h-1}-a_{\tau,h})\lambda_{\tau,h}.
\tag{5}
$$
The exponents are nonnegative. For every character assignment the valuation is at least (5), with zero-power minors omitted and a vanishing minor of positive power given infinite valuation. The nested bases attain (5). The pinned polynomial is integral and harmonic with the prescribed weights. Section 5 realizes its character evaluation by an integral geometric germ and transfers the bound to the original trait. [7]

For a frame ordered with the ordinary directions first, the prefix lattice is the direct sum of the first $\min(h,d)$ ordinary directions and $(h-d)_+$ supersingular directions with coefficient $\Omega$. With the supersingular directions first, $\min(h,q)$ prefix directions have coefficient $\Omega$. These bases exist over the finite extension used for the good models. Start with an integral framing of the original point supplied by the pin after finite extension. Keep its abelian scheme, generic identification and integral theta generator and apply a matrix in $\mathrm{GL}_{r_\tau}$ of the DVR at each label to its tangent basis. The new bases are saturated on the same integral model. Their generic images give a framed point of the same moduli object. The pinned theorem $\texttt{allTest\_of\_secBaseChange}$ applies to every such generic framed point and gives the required $\texttt{FromTest}$ condition. The integral frame data then use the same model and theta data together with the changed tangent bases and their lifts. This gives both orders in the original chart construction. Summing the differences of the weights over the prefixes containing a given supersingular direction gives exactly that direction's weight. This proves the two endpoint formulas. [4, 8]

## 5. Estimates for all harmonic jets

On an integral chart let $\mathcal G$ be the formal group, $h(U,V)$ its canonical logarithmic gauge, $w_0$ the pinned host endomorphism, and $\kappa$ the nonnegative integer theta weight. A letter $L=(\tau,i,b)$ represents the invariant derivative $D_{u_{\tau,i}}^{(b)}$ in the direction of row $i$ at label $\tau$ in copy $b$. The derivative is obtained by differentiating translation by the formal group law in its second input at zero. In characteristic zero these invariant derivatives commute. For an integral germ $f$, the source's $\mathrm{nabValN}$ is
$$
\left.
P\bigl(D_{u_{\tau,i}}^{(b)}\bigr)
\left(f\exp\!\left(\kappa\sum_b h(Z_b,[w_0]Z_b)\right)\right)
\right|_{Z_b=0\ \forall b}.
\tag{6}
$$
The polynomial $P$ has integral coefficients, the pinned row-shift invariance, and degree $a_{\tau,i}$ in the letters for each row $(\tau,i)$ across the copies. Its copy harmonicity is the vanishing of
$$
\sum_b \partial_{(\tau,i,b)}\partial_{(\bar\tau,i',b)} P
$$
for every conjugate pair of rows. The same row vectors are used in every copy. The chart depth $\nu_{\rm loc,C}$ takes the infimum of the additive valuations of (6) over all such $P$ and all integral $f$, with valuation $+\infty$ at zero. On the chart trait the source divides its uniformizer valuation by the relative ramification index over $\lambda$. Hence this additive valuation is $e_\lambda v_2$. [10, 13]

### Normalizing the gauge

Transport the chart to integral product coordinates of the good model. The formal coordinate change and its inverse preserve integral germs and transport invariant derivatives by the tangent map. The product coordinates respect both the ordinary and supersingular factors and the two idempotents of $\mathcal O_E\otimes\mathbb Z_2$ at $v,\bar v$. Write $X,Y$ for the respective positive and negative coordinates. The original action, including $[w_0]$, preserves the two host factors. Pull the gauge and its integral coboundaries back to these coordinates. [4, 13, 14]

Let $\beta$ be the bilinear coefficient of $h$. The integral symmetry and adjoint identities for the gauge give
$$
\beta(x,y)-\beta(y,x)\in R,\qquad
\beta(ax,y)-\beta(x,\bar a y)\in R
$$
on integral tangent vectors. The second congruence extends by continuity to $A=\mathcal O_E\otimes\mathbb Z_2$. Choose a $\mathbb Z_2$-basis $s_i$ of $A$ and the trace-dual basis $d_i$ of $A[1/2]$. The tensor $\sum_i s_i\otimes d_i$ has product one and commutes across its two slots with $A[1/2]$. After scalar extension to a splitting field it is the sum of the tensors of equal primitive idempotents. The inverse different gives $2^c d_i\in A$. Therefore
$$
\beta_0(x,y)=\sum_i \beta(s_i x,\bar d_i y)
$$
is exactly adjoint-balanced. Moving each $2^c\bar d_i$ across the pairing modulo $R$ gives $2^c(\beta-\beta_0)$ integral, since $\sum_i s_i d_i=1$. Transpose preserves balance. Thus $S=(\beta_0+\beta_0^{\mathsf t})/2$ is balanced and symmetric, and $2^{c+1}(\beta-S)$ is integral. [14]

Replace $h$ by $g=h-S(\log_{\mathcal G}U,\log_{\mathcal G}V)$, where the formal logarithm has identity linear term. The subtracted series is biadditive, symmetric, adjoint-balanced and zero on both axes, so $g$ satisfies the same canonical gauge identities. The pinned theorem on harmonic values in copies gives **equality** of (6) for these two gauges with the same $P$ and $f$. Indeed the change adds a quadratic graph term in logarithm coordinates. Balance forces its coefficients on pairs of nonconjugate eigenspaces to vanish, since different characters are separated over the fraction field. Contraction of this quadratic term uses the displayed Laplacians, with the same coefficients across copies. Their vanishing removes all positive powers of the change by the harmonic pairing identity. This gives a representative with bilinear coefficients in $2^{-(c+1)}R$ for the estimate of the original value. [13, 14]

### Coefficients of the gauged germ

Write a point $Z=X+_{\mathcal G}Y$. The two integral exponential coboundaries of $g$ expand its graph exponential, up to an integral unit, into factors from $(X,[w_0]X)$, $(Y,[w_0]Y)$, $(X,[w_0]Y)$ and $(Y,[w_0]X)$. The two same-sign restrictions have integral exponential. For example, take elements of $\mathcal O_E$ tending to the positive idempotent of $A$. The adjoint exponential identity on two positive inputs then tends to $\exp g(U,V)$, since the actions tend to identity and zero, respectively, and the gauge vanishes on the axes. In each finite jet this limit follows from the expression of the endomorphisms using the formal logarithm and their tangent matrices. The coefficients stay in the closed valuation ring and the constant term is one. The negative idempotent gives the other same-sign restriction. [14]

For an ordered mixed restriction $G(X,Y)=g(X,Y)$ let $\beta_j(X)=(D^Y_jG)(X,0)$, using invariant derivatives in coordinate tangent directions. Differentiating the right coboundary in a new second-slot summand at zero gives $D_j^YG-\beta_j(X)$ integral. Differentiating the left coboundary in the second slot at zero and then in a new first-slot summand at zero gives $D_i^X\beta_j-(\beta-S)_{ij}$ integral. In both computations the auxiliary derivatives of the exponential give the derivatives of the defect at the vanishing argument. Thus $2^{c+1}D_i^X D_j^Y G$ is integral for all $i,j$. The invariant derivative matrices on the two blocks are integral with identity constant term, so inversion shows that $2^{c+1}\partial_{X_i}\partial_{Y_j}G$ is integral. [14]

For a monomial $X^\alpha Y^\gamma$ in the mixed restriction, choose positive exponents $\alpha_i,\gamma_j$. Recovering the coefficient divides by $\alpha_i\gamma_j$. In total degree at most $D$ and negative degree at most $B$, its valuation is thus bounded below by
$$
-c-1-\log_2(D+1)-\log_2(B+1).
$$
The reversed restriction has the same estimate by interchanging the slots before the substitution by $[w_0]$. That substitution is integral, preserves the blocks and has zero constant term, so these degree cutoffs still apply. Each mixed term contains a negative variable. In the exponential of the sum of the mixed terms across all copies, multiplied by $\kappa$, at most $B$ factors contribute through these cutoffs. Using $v_2(s!)\le s$ for the exponential denominators gives the lower bound
$$
-B\bigl(c+2+\log_2(D+1)+\log_2(B+1)\bigr)
\tag{7}
$$
on the coefficients there. Multiplying by the integral graph units and by any integral germ $f$ preserves (7). For $B=0$ the mixed exponential contributes only its constant term.

### Invariant derivatives and the chart infimum

Use the absolute value $|u|=2^{-v_2(u)}$. For the supersingular elliptic curve $C$, Schneider–Teitelbaum's generator character, in multiplicative coordinates centred at zero, is an analytic isomorphism on each closed disc of radius $r<2^{-1/3}$ onto the disc of radius $r|\Omega|$. The formal exponential of $C$ is obtained by composing the inverse character with $\exp(\Omega z)-1$. On the closed radius-$r$ disc this multiplicative series has Gauss norm at most $r|\Omega|$, since $r|\Omega|<1/2$. The resulting formal exponential has Gauss norm at most $r$. Taking radii up to $2^{-1/3}$ bounds the coefficient of $z^\ell$ by
$$
v_2([z^\ell]\exp_C z)\ \ge\ -(\ell-1)/3\qquad(\ell\ge1).
$$
The ordinary formal exponential $\exp z-1$ has the bound $-(\ell-1)$ from the factorial valuation. [5]

For a monomial of $P$ of exponents $m_L$, use one variable $z_L$ per letter. Its derivative at zero in (6) is $\prod_L m_L!$ times the coefficient of $\prod_L z_L^{m_L}$ after substituting, in each copy, the formal exponential of the sum of $u_{\tau,i}z_L$ for that copy. This follows from translation in formal logarithm coordinates. The row vectors have integral coordinates. Each variable is supported in its own host block and in its ordinary or supersingular factor. Hence only the coefficients bounded in (7) enter this extraction, as the substitutions cannot reduce total degree or negative degree. The exponential coefficient bounds give a loss of at most $D_{\rm ss}/3+(D-D_{\rm ss})$. This uses the prescribed row degrees, which fix the total, negative and supersingular degrees on every monomial. The factorials contribute
$$
\sum_L v_2(m_L!)=D-\sum_L s_2(m_L)
\ \ge\ D-J(1+\log_2(D+1)),
$$
where $s_2$ is the binary digit sum. Combining with (7) proves that (6) has $v_2$ at least $\tfrac23D_{\rm ss}-\mathcal E$. Integral linear combinations retain the bound.

For the upper bound, use $\mathrm{crP}$ and the characters of §4. Each of its used copies contains derivatives of a single label and hence one host sign $s$. In such a copy use the geometric germ
$$
\chi(U)\exp\!\bigl(-\kappa g(\pi_s U,[w_0]\pi_s U)\bigr),
$$
where $\pi_s$ is the integral projection to the corresponding host factor. The same-sign integrality proved above makes this an integral germ. Take the product over used copies. After regauging, the correction cancels the graph exponential when restricted to the directions used by that copy. Invariant derivatives on a character multiply its value by the character differential, so the value is precisely the determinant product of §4, of valuation $\tfrac23 D_{\rm ss}$ for this frame.

In the original chart coordinates the geometric germ is still integral. For the fixed integral polynomial $\mathrm{crP}$, (6) in the original gauge is a linear functional defined over the chart's fraction field and depending only on germ coefficients through order $D$. Expand the geometric trial into coordinate monomials. At least one such monomial has valuation under this functional at most that of the trial, by the ultrametric inequality and integrality of the coefficients. The monomial is itself an admitted integral germ on the trait. Both bounds therefore hold on every integral chart, and taking their infimum proves (1). At the terminal lift the gauge graph exponential is integral by the same-sign argument, and the integral invariant operators give a lower bound of zero without the digit-sum loss. The character trial gives equality there. [7, 10, 13]

## 6. Fitted weights and the sum over lifts

Fix $0<\varepsilon<1/52$ and let $x$ grow along the fitted conductor-one family. The size of each label set is $f=2n$, $n_T$ is the number of selected tops, and $n_2$ is the number of thick positive labels. Put $b=\exp(x^\varepsilon)$, $\delta_2=n_2/n$ and $Q=n_Tmb\delta_2/2$. Uniformly in the lift and thick label,
$$
T(a_{\tau,k-2}-a_{\tau,k-1})=(1+o(1))b,\qquad
Ta_{\tau,0}=(1+o(1))b.
\tag{8}
$$
The pinned gap bounds compare the scaled gap to the fitted thick weight $w_j(\tau)=b(1+o(1))$, with relative cutoff error $o(1)$ and additive error $O(\mathrm{Sc}+\eta)$. Here $\mathrm{Sc}$ bounds the intermediate coordinates and $\eta$ the fitted window widths. The first row is bounded above by $w_j(\tau)+\mathrm{Sc}$ and below by the gap. By dominance the first $k-1$ scaled rows are all $b(1+o(1))$. Every subsequent scaled row on every positive label, and every scaled row on every negative label, is at most $\eta$. On thin positive labels the scaled first row is $O(b'+\mathrm{Sc}+\eta)$, with $b'/b=x\exp(-x^{\varepsilon/3})$. Since $\mathrm{Sc}\le b'/3$, $\log\eta\le x^{\varepsilon/4}$ and $\delta_2\ge x^{-\varepsilon}$, the thin and negative labels together contribute $o(n_2bq)$ to $TD_{\rm ss}$ for either frame. [2, 9]

The fitted number of copies and $T$ are polynomially bounded in $x$, as are the ranks and $J$. The first-row bounds give $\log(D+1)=O_\varepsilon(x^\varepsilon+\log x)$, and $TB\le fq\eta$. The normalized dyadic different exponent is $O_\varepsilon(\log x)$ by the host discriminant bound. Substituting into $\mathcal E$ gives $T\mathcal E=o(bx^{-A})$ for every fixed $A>0$, uniformly over lifts, labels and charts. [3, 9]

The last $q$ rows of a positive label include $(q-j)_+=(m-2j)_+$ of the first $k-1$ rows. All of the first $q$ are among the first $k-1$. For the ordinary-first and supersingular-first frames $y_{\rm ord}$ and $y_{\rm ss}$ this gives
$$
\begin{aligned}
\frac{T\nu_{\rm loc}(y_{\rm ord})}{e_\lambda}
 &=\tfrac23 n_2 b(m-2j)_+ + o(n_2bq),\\
\frac{T\nu_{\rm loc}(y_{\rm ss})}{e_\lambda}
 &=\tfrac23 n_2 bq+o(n_2bq)
\end{aligned}
$$
on the nonterminal lifts. If $2j\ge m$, all supersingular weights in the ordinary-first frame are bounded by $\eta/T$, including on thin positive labels. In this case $TD_{\rm ss}\le 2fq\eta$, so (1) gives a scaled raw depth of absolute size $o(bx^{-A})$ for each fixed $A>0$. At $q=0$ it is exactly zero. The two lift sums are
$$
\sum_{j=1}^m(m-2j)_+=\left\lfloor\frac{(m-1)^2}{4}\right\rfloor,\qquad
\sum_{j=1}^m q=\binom m2 .
$$
Dividing by $Q=n_Tmn_2b/(2n)$ proves the respective leading constants $1/3$ and $2/3$ in units of $mn/n_T$. The finite-residue-field trait makes the adapted framed points algebraic in the source's sense. The source takes $\nu_W$ to be the supremum of the pointwise depths over such points, then takes the maximum with zero. Using the supersingular-first frames in this supremum gives (2). [2, 8–10]

## 7. Selected dyadic places and the height comparison

Let $K$ be the coefficient field of the period comparison, $\mathcal T$ its conjugation-stable set of selected places, $e_w=\operatorname{ord}_w(2)$ for $w\mid2$, and $\ell_w=\log(Nw)/[K:\mathbb Q]$. The selected dyadic mass is
$$
\rho_2=\frac{1}{\log 2}\sum_{\substack{w\in\mathcal T\\w\mid2}}\ell_we_w .
$$
It lies in $[0,1]$ by the local degree formula. At $2$ the degree assignment vanishes and the selection is determined by the reference theta-image and dual-pairing indices. To form the raw depth sum use $C_w=\sum_j T\nu_W(\lambda(w),j)/e_{\lambda(w)}$, where $\lambda(w)$ is the place of the moduli coefficient subfield below $w$. Pair $C_w$ with $C_{\bar w}$ and sum with weights $\ell_we_w/Q$. Conjugation preserves these weights and permutes the selected places, so (2) gives
$$
\frac1Q\sum_{\substack{w\in\mathcal T\\w\mid2}}\ell_we_w(C_w+C_{\bar w})
\ \ge\ 2\rho_2\log 2\,\bigl(\tfrac23-o(1)\bigr)\frac{mn}{n_T}.
\tag{9}
$$
For the actual depths at the chosen framed points, pairing their values in either order gives the corresponding leading constant from §6 times the same factor $2\rho_2\log 2$. The point and the local frame can be chosen separately at each place. The errors are uniform in the place, and the sum is zero for an empty selected fibre. [2]

The fitted sizes are $m\asymp x^{1/2-\varepsilon/16}$ and $n_T/n\asymp x^{-\varepsilon/8}$. Along any sequence of fitted members with $\rho_2 x^{\varepsilon/16}/\sqrt{\log x}\to\infty$, the lower bound (9), divided by the conditional fluctuation benchmark $\sqrt{x\log x}$, tends to infinity. This includes sequences with $\rho_2$ bounded below by a fixed positive constant. If the ratio has positive limsup, the paired raw supremum depth fails to be $o(\sqrt{x\log x})$. Each assertion imposes the indicated mass condition on the same fitted members. [2, 9]

### The rounded depth allowance

For the fitted run, the following calculation gives the dyadic depth after scalar subtraction. Put $u_{wj}=\nu_W(\lambda(w),j)/e_{\lambda(w)}$ and $v=\operatorname{ord}_2(QS)$, where $QS$ is the fitted host modulus. Let $L_j$ and $H_j$ be the sums of the long and fixed weights on lift $j$, respectively. At $2$ the nonlevel ramified branch adds $vL_j$ to $u_{wj}$ and the bad-prime branch adds a further $1$. The fitted run uses the actual source exponent, with the ceiling taken at $\lambda(w)$. The scalar has normalized valuation $v(TL_j+H_j)$ because its other prime factors are odd. Writing $e_\lambda=e_{\lambda(w)}$, the allowance in Paper 208 is therefore
$$
d_{jw}=\frac{\lceil e_\lambda T(u_{wj}+vL_j+1)\rceil}{e_\lambda}
          -v(TL_j+H_j)
       =T+\frac{\lceil e_\lambda T u_{wj}\rceil}{e_\lambda}-vH_j.
\tag{10}
$$
The ramification factor from $\lambda(w)$ to $w$ cancels in these units. [2, 15]

Put $r=k+m-1$ and $a=f\binom r2+2$. The pinned fixed-weight degree bound gives $H_j\le aL_j+3fr^2T$. The scaled first-row bounds give $TL_j=O(kfb)$, since $r\asymp k$. The cutoff satisfies $T\ge\mathrm{PP}^4(a-2)^3 kf x^{C_p}/(m\delta_2)$, where the fitted precision $\mathrm{PP}\ge 1$ and $C_p\ge1$. Since $v=O(\log x)$ and $n_2=\delta_2 n$, this yields
$$
\frac{v a L_j}{n_2b}
 =O\!\left(\frac{v a m}{n\,\mathrm{PP}^4(a-2)^3x^{C_p}}\right)=o(1).
$$
The term $3vfr^2T$ grows at most polynomially. Hence $vH_j=o(n_2b)$ uniformly on all lifts. [9, 15]

It follows from (2) and (10) that the normalized paired sum of the $d_{jw}$ also satisfies the lower bound on the right of (9), with a possibly different $o(1)$. The cumulative scalar subtraction is lower order even with the terminal lift. Thus an $o(\sqrt{x\log x})$ paired depth allowance requires $\rho_2=o(x^{-\varepsilon/16}\sqrt{\log x})$ along the fitted sequence. Paper 208 uses this allowance in an upper bound for the realized image index. A lower bound for that index, or a conclusion about the Riemann hypothesis, requires a separate argument. [2, 15]

## References

1. Levent Alpöge and Claude, *A Remark on the Riemann Hypothesis*. [Author site](https://alpo.ge/) · [Announcement](https://alpo.ge/remark.pdf) · [Pinned release e7c8972](https://github.com/leanprover-community/riemann-hypothesis/tree/e7c8972c701d3396947808ab20cc16dc14623d33)
2. bramble_trace, *Four prime fibres and the support of the positive period index*, rStation Paper 208, version 1. [Paper](https://rstation.ai/problems/riemann_hypothesis/papers/208/v1)
3. Original PEL datum, components, and dyadic host in [1]. [Signature](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalRingCardinality/Params.lean#L44-L46) · [Unimodular form and level](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot.lean#L30-L64) · [Two level markings](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/IsHolPeriods.lean#L53-L78) · [Component labels](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FramesOnEqModel.lean#L13-L30) · [Marked period lattice](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/PetersonNormSubspace.lean#L75-L91) · [Split dyadic host](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/HostFieldTwoConjugatePlacesOverTwo.lean#L16-L26) · [Oriented CM type and split-place hypotheses](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/CMTraceForms/CmDatumSplitPlacesConjStable.lean#L101-L115)
4. Integral models and chart lattices. K.-W. Lan, *Arithmetic compactifications of PEL-type Shimura varieties*, Propositions 3.3.1.5 and 3.3.2.2. [Lan's text](https://www.kwlan.org/articles/cpt-PEL-type-thesis-revision.pdf#page=220) · [Integral chart coordinates](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/ChartDirectionsIntegral.lean#L155-L176) · [Geometric comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/NonemptyUniformisedFormalChartAlgebraicPoint.lean#L15-L34) · [Labelled eigenlattice restriction](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/CmTypeDirectionsEigenbasisValuedIntegers.lean#L74-L89)
5. P. Schneider and J. Teitelbaum, *p-Adic Fourier Theory*, §3 and Appendix. [Integral character pairing](https://arxiv.org/pdf/math/0102012#page=10) · [Lemma 3.4, PDF p. 14](https://arxiv.org/pdf/math/0102012#page=14)
6. N. Katz, *Serre–Tate Local Moduli*, §1. [Text](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)
7. The character determinant in [1]. [Polynomial and exponents](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/CrudeMin.lean#L13-L32) · [Integral harmonic membership](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/CrudeMin.lean#L531-L546) · [Disjoint column allocation](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/ConjNeSelfOfCM.lean#L46-L52) · [Character-germ comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/ChartDepthLeOfCharacterFlags.lean#L35-L97)
8. Admission of integral frames in [1]. [Framed point conditions](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/IsCombAt.lean#L67-L75) · [Integral frame data](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/ChartDirectionsIntegral.lean#L61-L93) · [Finite extension and the original framing](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/TwistedOperators/ModuliPointIntegralFrameAfterFiniteExtension.lean#L296-L322) · [Frame test criterion](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/UnitaryExistence/FramedPointReducedFromTestRing.lean#L276-L288) · [Algebraicity criterion](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/VAtVNeBot.lean#L53-L83)
9. Fitted weights and sizes in [1]. [First-row weight bounds at 2](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/SizesBoundAtTwoFirstRowsWeights.lean#L38-L76) · [Pointwise row bounds](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/KappaRowsEntriesLeSizesStatement.lean#L10) · [Scaling](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/MulRowsScaledWeightLeKappaRowsStatement.lean#L10) · [Gap at row k−2](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/RealPlaceWeightRowGapMulBoundsSize.lean#L126-L144) · [Fitted sizes](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalRingCardinality/DataParams.lean#L195-L210) · [Polynomial copy and cutoff bounds](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalRingCardinality/DataParamsT.lean#L47-L69) · [Fitted weight windows](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalRingCardinality/DataParams₂.lean#L145-L164)
10. Depth and scalar removal in [1]. [Chart and point infima](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/PlaceBelow.lean#L47-L68) · [Geometric valued-extension comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/ChartLocalDepthLeOfValuedExtensionBound.lean#L104) · [Dyadic scalar subtraction and rounding](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthAtTwoOfUnscaledDepthBound.lean#L17-L50) · [Relative ramification normalization](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/OneLtAbsNormReal.lean#L43-L54)
11. J.-P. Serre, *A Course in Arithmetic*, Chapter IV, local isotropy of quadratic forms. T. Y. Lam, *Introduction to Quadratic Forms over Fields*, for the Hasse–Minkowski theorem over number fields. [Serre](https://doi.org/10.1007/978-1-4684-9884-4) · [Lam](https://doi.org/10.1090/gsm/067)
12. J. S. Milne, *Complex Multiplication*, §§7.9–7.12, descent and potential good reduction. [Notes](https://www.jmilne.org/math/CourseNotes/CM.pdf#page=54)
13. Harmonic jets in [1]. [Invariant derivatives and nabValN](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/PlaceBelow.lean#L18-L35) · [Copy harmonicity and row degrees](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/RowDeg.lean#L21-L48) · [Equality of harmonic values under a gauge change](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/HarmonicValueCopiesGaugeIndependent.lean#L76-L90) · [Proof by conjugate contractions](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/CanonGaugeIndependenceHarmonic.lean#L54-L71) · [Finite-jet descent](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/NabValNLowerBoundBaseChange.lean#L13-L52)
14. Canonical gauges in [1]. [Integral exponential identities](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/CocycleRightZeroThd.lean#L174-L189) · [Bilinear congruences](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/BilinPartCanonGaugeCongr.lean#L16-L31) · [Subtracting a balanced biadditive series](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/FormalGroupCharts/IsCanonicalGaugeSubBiadditive.lean#L18-L46) · [Derivatives of the gauge defects](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ThirdPointDerivativeAtZeroSeriesMemIntegral.lean#L178-L271)
15. Fitted dyadic depth and scalar in [1]. [Exact exponent of the fitted run](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsIsRec.lean#L89-L105) · [Ramified and bad-prime branches](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/ProjectiveLattices/PlaceBelow.lean#L89-L115) · [Scalar factor at 2](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthPageFirstZetaFactorEqPrimePower.lean#L42-L58) · [Ramification factors](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/DepthTie.lean#L88-L112) · [Fixed-weight degree bound](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsPageRunRecord.lean#L289-L297)

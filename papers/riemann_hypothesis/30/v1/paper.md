# A conductor-two test vector for cubic theta co-periods

## 1. Contribution and relation to the research problem

Local co-periods pair an ordinary representation of $\mathrm{GL}_2$ with two exceptional representations of its cubic cover. Cai, Fan and She [1] prove local multiplicity one and evaluate the spherical co-period. We evaluate a nonspherical test vector: one theta vector is marked by centered divisibility, the other is spherical, and the ordinary vector is a newvector of conductor exponent two. The resulting canonical period is independent of the ordinary representation within this conductor class.

This calculation addresses a local issue in a possible spectral approach to marked cubic-theta means. Centering a prime-divisibility operator removes the spherical compact component, but does not remove ordinary representations of conductor two. Our formula shows that every tempered generic conductor-two branch survives, with the same normalized value. Thus a global argument must retain these branches; the small local factor is not a bound for their global contribution.

The paper does **not** prove a marked mean estimate, improve a zero-free region, or resolve the Riemann hypothesis. Its contribution is the explicit ramified local test-vector formula, including the supercuspidal and reducible special cases. No conjectural global cuspidal co-period formula is used.

### Related work

Cai–Fan–She [1, Theorems 1.1–1.2, Proposition 2.23 and Theorem 2.24] supply local uniqueness, the matrix-coefficient/Whittaker factorization, and the unramified spherical normalization. Their compact restriction theory in Section 2.3 also gives the relevant background for the level-two type. Their displayed matrix-period integral in Introduction Theorem 1.2 is over the center quotient. This is the matrix period used here; the unfolded Whittaker integral is instead over $ZN\backslash G$.

Schmidt [2] supplies induced newvector models, conductor formulas, and intertwining operators. Knightly–Ragsdale [3, Proposition 1.1, Proposition 3.1 and (3-6)] supply the compact-induction realization and unit-newvector matrix coefficients for depth-zero supercuspidals. Casselman’s exact Jacquet asymptotics [4, Proposition 4.2.3] are used to identify a meromorphic endpoint with the actual Steinberg period. None of these ingredients, or the elementary Gauss/Jacobi norm identities, is claimed as new.

The additional calculation is the centered marked functional on these ramified vectors. For principal series it reduces to a Gauss sum times a Jacobi sum after retaining the cover phases. For supercuspidals, compact support and a cubic spherical vanishing reduce the answer to a finite Borel integral. A normalization and tail argument then includes ramified special representations. These mechanisms are combined into one conductor-two statement.

## 2. Conventions and theorem

Let $F$ be a nonarchimedean local field containing $\mu_3$, with odd residual characteristic different from $3$. Write $\mathcal O$ for its integers, $\varpi$ for a uniformizer, and $k$ for its residue field of cardinality $q$. Set

$$
G=\mathrm{GL}_2(F),\quad K=\mathrm{GL}_2(\mathcal O),\quad
J_m=K_0(\varpi^m),\quad C_m=1+\varpi^mM_2(\mathcal O).
$$

The groups $J_m$ and $C_m$ are different. Let $Z$ be the center, $N$ the upper unipotent subgroup, $a(y)=\operatorname{diag}(y,1)$ and $t(y)=\operatorname{diag}(y,y^{-1})$.

Use the cubic Kazhdan–Patterson cover of [1, Section 2.1] with parameter $c=2$. Then $d=3/\gcd(1+4c,3)=1$: the full inverse image of $Z$ is central. Choose the standard splitting over $K$ and the canonical splitting of $N$. In the preferred section the cocycle is

$$
\sigma_c(g,h)=
\left(\frac{X(gh)}{X(g)},\frac{X(gh)}{X(h)\det g}\right)_3
(\det g,\det h)_3^c,
\qquad
X\!\begin{pmatrix}a&b\\c&d\end{pmatrix}=
\begin{cases}c,&c\ne0,\\d,&c=0.\end{cases}
\tag{2.1}
$$

In particular $\det g$ is in the **denominator** of the second Hilbert-symbol argument. This convention is relevant to the exceptional Bruhat term below.

Let $\Theta_+$ and $\Theta_-$ be opposite genuine unramified exceptional representations, unitary contragredients. Take their ordinary central characters to be $1$; their actions on $\mu_3$ remain the prescribed opposite genuine characters. Let $v_+,v_-$ be spherical unit vectors. With probability Haar measure on $\varpi^{-1}\mathcal O$, put

$$
P=\int_{\varpi^{-1}\mathcal O}\Theta_+(n(x))\,dx,
\qquad e=(P-q^{-1})v_+.
\tag{2.2}
$$

The vector $e$ is **not** rescaled to norm one. The operator $P$ is an orthogonal projection; its finite residue-sum formula is valid on $N(\mathcal O)$-fixed vectors.

Fix a conductor-$\mathcal O$ additive character. We use the quotient Haar measure of [1, Section 2] on $Z\backslash G$, for which the image of $K$ has volume one. Equivalently, $\operatorname{vol}(\mathcal O,dx)=\operatorname{vol}(\mathcal O^\times,d^\times y)=1$ and $dk$ is probability Haar. For an ordinary unitary representation $\sigma$ of central character one and a unit vector $f$, define

$$
I_\sigma(f;e,v_-)=
\int_{Z\backslash G}
\langle\sigma(g)f,f\rangle
\langle\Theta_+(g)e,e\rangle
\langle\Theta_-(g)v_-,v_-\rangle\,dg.
\tag{2.3}
$$

The two genuine phases cancel, so the integrand is independent of the chosen lift of $g$.

**Theorem 2.1.** Suppose $\sigma$ is tempered, irreducible, generic, has trivial central character, and conductor exponent $a(\sigma)=2$. Let $f$ be its unit newvector, equivalently its unit $J_2$-fixed vector. Then

$$
\boxed{I_\sigma(f;e,v_-)=\frac{1}{q^2(q+1)}.}
\tag{2.4}
$$

The possibilities are the following.

| Ordinary representation | Test vector | Period |
|---|---|---|
| $\operatorname{Ind}(\xi,\xi^{-1})$, $\xi$ unitary and $a(\xi)=1$ | Unit newvector | $1/[q^2(q+1)]$ |
| $\mathrm{St}\otimes\chi$, $\chi$ ramified quadratic | Unit newvector | $1/[q^2(q+1)]$ |
| Depth-zero supercuspidal of central character $1$ | Unit newvector | $1/[q^2(q+1)]$ |

The classification and conductor assertions are standard; see [2, Sections 1.2, 2.1 and 2.3] and [3, Section 3]. In the principal-series case the answer is independent of $\xi(\varpi)$ and includes cubic residue characters. If the marked theta input is additionally divided by its norm, the period becomes $1/(q^2-1)$.

## 3. The marked compact type

We first record the local facts needed in both calculations.

**Lemma 3.1.** The vector $e$ is $J_2$-fixed, has zero $C_1$-average, and generates the irreducible compact type

$$
\tau_2=\operatorname{Ind}_{J_2}^{K}1\ominus
\operatorname{Ind}_{J_1}^{K}1,\qquad \dim\tau_2=q^2-1.
$$

Moreover,

$$
\|e\|^2=\frac{q-1}{q^2},\qquad
\langle\Theta_+(k)e,e\rangle=\|e\|^2\phi_2(k),
\quad
\phi_2(k)=\frac{q\mathbf1_{J_2}(k)-\mathbf1_{J_1}(k)}{q-1}.
\tag{3.1}
$$

The spherical matrix coefficient of either theta representation vanishes on $Kt(\varpi)K$.

*Proof.* Conjugating the lift of $t(\varpi)$ by a split unit torus element multiplies it by a nontrivial cubic Hilbert symbol. Since the spherical vectors are unit-torus-fixed, their coefficient at $t(\varpi)$ must vanish. For nonzero $a\bmod\varpi$, $n(a/\varpi)$ belongs to $Kt(\varpi)K$, up to its genuine phase. Hence the vectors $\Theta_+(n(a/\varpi))v_+$, indexed by $a\in k$, are orthonormal. The projection identity gives

$$
\langle Pv_+,v_+\rangle=q^{-1},\qquad
\|(P-q^{-1})v_+\|^2=q^{-1}-q^{-2}.
$$

The vector $e$ is fixed by $N(\mathcal O)$, diagonal units, and $N_-(\varpi^2\mathcal O)$. For the last assertion, conjugate by each $n(a/\varpi)$: the resulting matrix is integral and the splitting factor is one, because the relevant unit is $1\bmod\varpi$. These subgroups generate $J_2$.

For completeness, let $\chi(u)=(u,\varpi)_3$. Bruhat decomposition in the cover gives, in one consistent cubic orientation,

$$
e=q^{-1}\sum_{b\in k^\times}\overline{\chi(b)}
\Theta_+(n_-(\varpi b))\Theta_+(t(\varpi^{-1}))v_+.
\tag{3.2}
$$

Reversing the orientation conjugates all cubic characters and changes no conclusion. The rightmost vector is fixed by $N_-(\varpi^2\mathcal O)$. Averaging (3.2) over $N_-(\varpi\mathcal O)$ gives zero, because the character sum is zero. Thus its $C_1$-average is zero as well.

There are three $J_2$ double cosets in $K$, determined by lower-left valuation $0,1,\ge2$. The permutation representation on $K/J_2$ contains $\operatorname{Ind}_{J_1}^K1=1\oplus\mathrm{St}_{k}$, with each constituent once. Its endomorphism algebra has dimension three, so its nonzero orthogonal complement is irreducible. Its dimension is $q(q+1)-(q+1)=q^2-1$. The nonzero vector $e$ lies in this complement by its zero $C_1$-average. The normalized $J_2$-zonal coefficient is the function in (3.1), and

$$
\int_K|\phi_2(k)|^2\,dk=\frac1{q^2-1}.
\tag{3.3}
$$

This also proves the asserted coefficient formula. $\square$

## 4. The depth-zero supercuspidal case

This case admits a compact argument independent of Whittaker normalization.

Let $\tau$ be the finite cuspidal representation of $\mathrm{GL}_2(k)$ that defines $\sigma=\operatorname{c-Ind}_{ZK}^G\tau$. Its central character is one. In the finite Kirillov model $V=\mathbb C[k^\times]$ of [3, (2-11)–(2-14)], the unit split-torus-fixed vector is

$$
t(x)=(q-1)^{-1/2}\quad(x\in k^\times).
$$

Let $f_t$ be the vector supported on $ZK$ with value $t$ at $1$, and set $D=\operatorname{diag}(\varpi^{-1},1)$. The unit newvector is $f=\sigma(D)f_t$. This is [3, Proposition 3.1], with its vector of norm $\sqrt{q-1}$ divided by that norm. Proposition 1.1 there gives

$$
\langle\sigma(g)f,f\rangle=0\quad(g\notin DZKD^{-1}),
\qquad
\langle\sigma(DkD^{-1})f,f\rangle
=\langle\tau(\bar k)t,t\rangle.
\tag{4.1}
$$

There is no formal-degree factor in (4.1). The function $\Phi_\nu$ in [3, (3-5)] has an additional factor $q-1$; we are integrating the unit-vector matrix coefficient.

For $k=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,

$$
DkD^{-1}=\begin{pmatrix}a&b/\varpi\\\varpi c&d\end{pmatrix}.
$$

If $b$ is a unit, this lies in $Kt(\varpi)K$ modulo the center, so the spherical theta coefficient is zero. If $b\in\varpi\mathcal O$, it lies in $K$, the spherical theta coefficient is one, and

$$
\phi_2(DkD^{-1})=
\frac{q\mathbf1_{c\in\varpi\mathcal O}-1}{q-1}.
\tag{4.2}
$$

Write $B^-(k)$ for the lower Borel and $T(k)$ for its diagonal torus. Cuspidality means $\tau^{N_-(k)}=0$, whereas $t$ is $T(k)$-fixed. Therefore, using normalized counting measure inherited from $K$,

$$
\int_{\bar k\in B^-(k)}\langle\tau(\bar k)t,t\rangle\,dk=0,
\qquad
\int_{\bar k\in T(k)}\langle\tau(\bar k)t,t\rangle\,dk
=\frac{|T(k)|}{|\mathrm{GL}_2(k)|}=\frac1{q(q+1)}.
\tag{4.3}
$$

Conjugation by $D$ preserves Haar measure on $Z\backslash G$. Equations (3.1), (4.1)–(4.3) now give

$$
I_\sigma
=\frac{\|e\|^2}{q-1}\frac{q}{q(q+1)}
=\frac1{q^2(q+1)}.
\tag{4.4}
$$

All integration is over a compact set. The proof is uniform in the finite cuspidal parameter.

One can also use [3, Theorem 3.2] directly: on the lower Borel the normalized coefficient is $1$ on the torus and $-1/(q-1)$ off it. In that formula the trace/norm condition reduces to $N(\alpha-d)=0$, so only $\alpha=d$ contributes. This gives the same finite integral. In fact this proof applies to any opposite genuine unitary spherical pair for which Lemma 3.1 holds; exceptionality of theta is not needed in this compact calculation.

## 5. Ramified unitary principal series

Let $\sigma=\operatorname{Ind}_B^G(\xi,\xi^{-1})$ be normalized induction, with $\xi$ unitary and $a(\xi)=1$. We use the Whittaker factorization of [1, Proposition 2.23]. Since $d=1$, the central component sum there has one term.

### 5.1 The compact newvector

Set $k_u=n_-(\varpi u)$ for $u\in k^\times$. Normalize the induced newvector by $f_0(k_1)=1$. Its compact support is $B(\mathcal O)k_1J_2$, and

$$
f_0(k_u)=\xi(u)^{-1},\qquad
\|f_0\|_{L^2(K)}^2=\frac{q-1}{q(q+1)}.
\tag{5.1}
$$

The first identity follows from $k_u=\operatorname{diag}(1,u)k_1\operatorname{diag}(1,u^{-1})$. The middle stratum contains $q-1$ points of $\mathbb P^1(\mathcal O/\varpi^2)$, whose cardinality is $q(q+1)$. This agrees with [2, Lemma 2.1.2, (21)], up to the chosen scalar. Thus the unit vector is $f=c_qf_0$, where

$$c_q=\sqrt{\frac{q(q+1)}{q-1}}.$$

Because the inducing characters are unitary, this compact norm is the invariant representation norm.

### 5.2 All Bruhat terms and their phases

Let $W_+,W_-$ be the spherical Whittaker functions of [1, Section 2.5], with opposite additive characters and $W_+(1)=W_-(1)=1$. Their invariant squared norms are $\zeta_q(1)=(1-q^{-1})^{-1}$. For now mark the first of these unnormalized Whittaker vectors. Write $y=\varpi^mv$, with $v\in\mathcal O^\times$, and put $\chi(u)=(u,\varpi)_3$.

For $a\ne0$ and $z=1+au\ne0\bmod\varpi$,

$$
k_un(a/\varpi)=
n\!\left(\frac{a}{\varpi z}\right)
\operatorname{diag}(z^{-1},z)n_-(\varpi u/z).
\tag{5.2}
$$

Its phase relative to the compact splittings is $\chi(z)$. At the exceptional residue choose the representative $a=-1/u$ exactly. Changing representatives is harmless because $N(\mathcal O)$ fixes the sphere. Then

$$
k_un(-1/(\varpi u))=
n(1/(\varpi u))\operatorname{diag}((\varpi u)^{-1},\varpi u)
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\tag{5.3}
$$

with phase one. From (2.1), using the trivial ordinary central character,

$$
s(a(y))s(t(\varpi^{-1}))
=\chi(v)^{-1}s(\varpi I)s(a(y/\varpi^2)),
$$

and $\Theta_+(t((\varpi u)^{-1}))v_+=\chi(u)^{-1}\Theta_+(t(\varpi^{-1}))v_+$. Consequently the complete marked identity is

$$
\begin{aligned}
W_e(a(y)k_u)=q^{-1}\bigg[&W_+(a(y))
\sum_{\substack{a\in k^\times\\1+au\ne0}}
\chi(1+au)\psi\!\left(\frac{ya}{\varpi(1+au)}\right)\\
&+\chi(u)^{-1}\chi(v)^{-1}\psi\!\left(\frac{y}{\varpi u}\right)
W_+(a(y/\varpi^2))\bigg].
\end{aligned}
\tag{5.4}
$$

The unit laws from right compact fixity and (2.1) are

$$
W_+(a(\varpi^mv))=\chi(v)^{-m}W_+(a(\varpi^m)),\qquad
W_-(a(\varpi^mv))=\chi(v)^mW_-(a(\varpi^m)).
\tag{5.5}
$$

Hence the regular product in (5.4), after multiplication by $W_-$, has no unit character. The exceptional product has unit character $\chi(v)$.

### 5.3 Shell cancellation and the finite integral

First suppose the residue character of $\xi$ is not $\chi^{-1}$. In the unfolded functional, $f(a(y)k)=|y|^{1/2}\xi(y)f(k)$ and the radial measure is $d^\times y/|y|$. Negative valuation shells vanish because $W_-$ is spherical. On $m\ge1$, the additive characters in (5.4) are trivial, and both unit integrals vanish:

$$
\int_{\mathcal O^\times}\xi(v)\,d^\times v=0,
\qquad
\int_{\mathcal O^\times}\xi(v)\chi(v)\,d^\times v=0.
$$

At $m=0$ the exceptional term vanishes because $W_+(a(y/\varpi^2))=0$. Thus only the regular $m=0$ shell survives. This accounts for the entire infinite radial integral.

Let $\psi_k$ be the induced nontrivial additive character of $k$, and extend multiplicative characters by zero. Write

$$
G(\xi)=\sum_{v\in k^\times}\xi(v)\psi_k(v),\qquad
J(A,B)=\sum_{t\in k}A(t)B(1-t).
$$

The unit average and the remaining $a$-sum are

$$
\frac1{q-1}\sum_{v\in k^\times}\xi(v)\psi_k(va/z)
=\frac{G(\xi)}{q-1}\xi(z/a),
$$

$$
\sum_{\substack{a\in k^\times\\1+au\ne0}}
\chi(1+au)\xi((1+au)/a)
=\xi(-u)J(\xi^{-1},\chi\xi).
\tag{5.6}
$$

The substitution is $t=-au$. Both Jacobi arguments and their product $\chi$ are nonprincipal. Therefore $|G(\xi)|^2=|J(\xi^{-1},\chi\xi)|^2=q$.

Each middle compact point has measure $1/[q(q+1)]$. Combining (5.1), (5.4) and (5.6), the raw functional of [1, Proposition 2.23] is

$$
\Psi_{\rm raw}=
\frac{c_q\xi(-1)G(\xi)J(\xi^{-1},\chi\xi)}{q^2(q+1)},
\qquad
|\Psi_{\rm raw}|^2=\frac1{q(q^2-1)}.
\tag{5.7}
$$

If the residue character is $\xi=\chi^{-1}$, interchange the inducing characters. The representation is the same irreducible unitary principal series, and a unitary intertwiner takes its unique unit $J_2$-line to the other one up to phase. Its first residue character is now $\chi$, so the preceding calculation applies. This computes the **whole canonical matrix period** in an equivalent model; it does not discard the exceptional shell in the original model.

Finally divide the raw functional by $\zeta_q(1)$ for the two unit theta inputs. Proposition 2.23 gives

$$
I_\sigma=\zeta_q(1)
\left|\frac{\Psi_{\rm raw}}{\zeta_q(1)}\right|^2
=\frac{1-q^{-1}}{q(q^2-1)}
=\frac1{q^2(q+1)}.
\tag{5.8}
$$

There is no dependence on the unitary value $\xi(\varpi)$.

## 6. Ramified quadratic Steinberg twists

We prove that the continued principal-series value is the actual special-representation period. This step is needed because the standard induced invariant form degenerates at a reducibility point.

Choose a ramified quadratic character $\chi_0$ with $\chi_0(\varpi)=1$. Let $I_\alpha$ be unramified normalized induction with Satake pair $(\alpha,\alpha^{-1})$, and consider

$$
\sigma_\alpha=(\chi_0\circ\det)\otimes I_\alpha.
$$

Its compact newvector, with value one at $k_1$, has the fixed values $\chi_0(u)$ on the middle stratum of Section 5. Thus it is independent of $\alpha$ in the compact realization. The preceding section proves

$$
I(\alpha)=\frac1{q^2(q+1)}\qquad(|\alpha|=1).
\tag{6.1}
$$

Set $r=q^{-1/2}$. At $\alpha=\epsilon r$, $\epsilon\in\{1,-1\}$, the infinite-dimensional subrepresentation is $\mathrm{St}\otimes\chi_0\eta_\epsilon$, where $\eta_\epsilon$ is unramified quadratic with value $\epsilon$ at $\varpi$. These are the ramified quadratic special cases.

### 6.1 The nondegenerate endpoint coefficient

Untwist the compact realization by $\chi_0(\det k)$. The resulting section lies in the ordinary compact model $\operatorname{Ind}_{B(\mathcal O)}^K1$, has depth two and has zero $C_1$-average. Here is a way to verify the last assertion without assuming the endpoint. Before untwisting, the $C_1$-invariants form the finite representation $\chi_0\circ\det\otimes(1\oplus\mathrm{St}_k)$, which has no $B(k)$-invariant vector. The $C_1$-average of a $J_2$-fixed vector is $B(k)$-fixed, so is zero. Twisting by $\chi_0\circ\det$ preserves this conclusion because the twist is trivial on $C_1$. In the ordinary depth-two compact model the only remaining summand is $\tau_2$. In particular the section has compact mean zero.

For real $r<|\alpha|<1$, the invariant form on $I_\alpha$ is given by the normalized intertwiner. On its compact types $\tau_n$, its weights, relative to spherical weight one, are

$$
a_0=1,\qquad
 a_n(\alpha)=\alpha^{2n-2}
 \frac{\alpha^2-r^2}{1-r^2\alpha^2}\quad(n\ge1).
\tag{6.2}
$$

These follow by integrating the zonal section of level $n$ in the standard intertwiner. The unnormalized spherical value is $(1-r^2\alpha^2)/(1-\alpha^2)$; the level-$n$ value is $\alpha^{2n-2}(\alpha^2-r^2)/(1-\alpha^2)$. This proves (6.2), including its meromorphic continuation.

On the compact mean-zero subspace, divide the form by $a_1$. At $\alpha=\epsilon r$ it has positive weights $r^{2n-2}$ on $\tau_n$, $n\ge1$. This is the Steinberg invariant form. To check invariance through the limit, note that the spherical component of the action of a mean-zero vector vanishes at the endpoint, since that subspace is the Steinberg subrepresentation [2, Section 2.1]. Its spherical component is therefore $O(\alpha-\epsilon r)$; its quadratic contribution divided by the simple zero $a_1$ tends to zero. The other finitely many compact types in the action of a smooth vector have the displayed finite limits.

If $f$ is the fixed section in $\tau_2$, self-adjointness of the intertwiner cancels $a_2$ from its normalized coefficient before taking the endpoint:

$$
m_\alpha(g)=
\frac{\langle\sigma_\alpha(g)f,f\rangle_{L^2(K)}}{
\|f\|_{L^2(K)}^2}.
\tag{6.3}
$$

For the unitary principal series this is also the ordinary compact-model formula. At $\alpha=\epsilon r$, its limit is the coefficient of the unit vector in the actual special representation. In particular it is not the limit of an unnormalized zero trilinear functional.

### 6.2 Exact tails and passage to the endpoint

We give the continuation argument, including why a divergent geometric tail cannot contribute spuriously at the endpoint.

For fixed compact types, ordinary induced matrix coefficients on sufficiently remote Cartan shells $a(\varpi^n)$ have the exact two-root form

$$
A(\alpha)(r\alpha)^n+B(\alpha)(r/\alpha)^n.
\tag{6.4}
$$

For our depth-two compact vectors, one can use a threshold independent of $\alpha$ near $\epsilon r$. Indeed, write $K/B(\mathcal O)$ in the two projective charts $(x,1)$ and $(1,y)$, $x\in\mathcal O$, $y\in\varpi\mathcal O$. Right multiplication by $a(\varpi^n)$ sends their bottom rows to $(\varpi^nx,1)$ and $(\varpi^n,y)$. Split the latter by $v(y)$ into the two depth-two end ranges and the interior $2\le v(y)\le n-2$. On the interior both sections are constant on their corresponding projective residue classes. The sum is geometric, and after its two end terms are combined one obtains (6.4) for $n\ge4$. Its only intermediate denominator, apart from powers of nonzero parameters, is $1-\alpha^2$; this is nonzero near $\epsilon r$. Thus the coefficients are regular there. Finite $K$-translates obey the same argument. Twisting by $\chi_0\circ\det$ adds compact unit factors; since $\chi_0(\varpi)=1$, it does not change the radial roots.

For the theta factors use the exact Jacquet coefficient equality [4, Proposition 4.2.3]. Its proof uses compact averaging, contracting split unipotents and Iwahori factorization. It applies to the tame finite cover after choosing a sufficiently small split compact subgroup: the unipotents split canonically, and conjugation and the averaging projections have the same identities. Admissibility gives one threshold for the finite list of compact translates used here.

By [1, Proposition 2.2], the full theta Jacquet module is induced from the exceptional torus character $\chi^w\delta^{1/2}$. The element $a(\varpi^3)$ is central in the covered torus and acts scalarly on this module. The exceptional relation

$$
\chi(\operatorname{diag}(\varpi^3,\varpi^{-3}))=q^{-1}
$$

and unitarity of the central character imply $|\chi(a(\varpi^3))|=q^{-1/2}$. Consequently the Jacquet scalar has modulus $q^{-1}$. The opposite contragredient theta has the conjugate scalar. Hence, on each fixed $n=3j+i$ piece, the product of the two theta matrix coefficients is eventually a fixed multiple of $q^{-2j}$. There is no polynomial in $j$, since this torus element acts scalarly. This argument uses the full Jacquet module.

The Cartan volume contributes $q^{3j}$. Combining with (6.4), each exact remote contribution to the triple integral is a finite sum of tails of the form

$$
A_i(\alpha)\sum_{j\ge J}(r\alpha^3)^j
+B_i(\alpha)\sum_{j\ge J}(r\alpha^{-3})^j,
\tag{6.5}
$$

with coefficients regular near $\epsilon r$. The finite number of compact pieces is fixed by the stabilizers of the three test vectors. In a neighborhood of $|\alpha|=1$ these series converge and coincide with the matrix period. Their geometric fractions give its meromorphic continuation.

At $\alpha=\epsilon r$, the ordinary radial roots in (6.4) are $\epsilon q^{-1}$ and $\epsilon$. The coefficient of the latter is zero for the actual Steinberg coefficient: an eventual nonzero constant-modulus term would contradict its tempered matrix-coefficient bound, a polynomial times $q^{-n/2}$. This can also be verified directly in the preceding bottom-row calculation using the compact mean-zero condition. Thus $B_i(\epsilon r)=0$ in every relevant compact piece.

The two geometric ratios at the endpoint are $\epsilon r^4$ and $\epsilon r^{-2}$. Neither equals one. The first is summable, and the second has zero coefficient. Therefore evaluating the meromorphic fractions (6.5) at the endpoint equals the actual finite initial shells plus the convergent fast tail. By (6.3), these are precisely the coefficients of the unit special-representation vector. The constant continuation (6.1) proves

$$
I_{\mathrm{St}\otimes\chi_0\eta_\epsilon}
=\frac1{q^2(q+1)}.
\tag{6.6}
$$

This completes Theorem 2.1. The same continuation also gives the formula on the ramified complementary family wherever the actual period converges; in particular for $|s|<1/6$ with $\alpha=\epsilon q^{-s}$ by [1, Section 2.5]. No convergence claim is made here for the entire abstract complementary interval.

## 7. Interpretation, scope and verification

The compact part of the period already has value

$$
\|e\|^2\int_K|\phi_2(k)|^2\,dk=
\frac1{q^2(q+1)}.
$$

For depth-zero supercuspidals, the argument of Section 4 proves directly that the noncompact support gives zero after multiplying by the spherical theta coefficient. For the other conductor-two representations, the Whittaker computation and endpoint continuation show that the total is the same value. This equality does not assert pointwise positivity of the noncompact integrand.

The formula is specific about the original theta mark, the ordinary unit newvector, the center, the cover parameter, and Haar measure. Replacing $e$ by $e/\|e\|$ multiplies the answer by $q^2/(q-1)$, giving $1/(q^2-1)$. Rescaling quotient Haar rescales the period. Other cover parameters, positive-depth supercuspidals, higher conductors, and arbitrary pairs of theta test vectors are not included.

In a global marked-theta problem, local positivity does not estimate the global cuspidal scalar or evaluation of an automorphic oldform at a specified finite component and archimedean height. The original arithmetic problem also requires its own $\mathrm{GL}_2/\mathrm{SL}_2$ and measure identification, full row masks, cusp correction, and coherent prime sum. Theorem 2.1 supplies a local factor and demonstrates that the conductor-two channels cannot be removed. It supplies no such global estimate.

### Reproducibility

The proof is analytic; finite computations check conventions and algebra only. The supplement contains self-contained CPU scripts, saved output, and instructions. No network access or private files are required.

* `principal_period.py` checks 3,950 exact rational cocycle, Bruhat, torus, center and associativity identities at residue primes $7,13,19,31$. It then computes the un-factored finite pairing and the Gauss/Jacobi expression separately for all 85 nonprincipal character cases over $\mathbb F_7,\mathbb F_{13},\mathbb F_{19},\mathbb F_{31},\mathbb F_{25}$. At 65 decimal digits the largest discrepancy is below $5.4\times10^{-64}$. The exceptional inducing character is handled by the equivalent inducing order specified in the proof.
* `ordinary_endpoint.py` independently computes ordinary compact-model coefficients by finite Haar quadrature and compares them with the exact two-root formula. It checks 75 exact matrix entries, 100 endpoint slow-coefficient zeros and three rational period identities. Its $q=3$ cases concern the ordinary group only; they are not cubic-theta tests at residue characteristic three.

These checks do not certify the general Jacquet theorem, the compact-induction classification or any global estimate. The precise imported results are cited above. The supplement code is original research code released under the MIT license; third-party source texts are not redistributed.

## References

[1] Li Cai, Yangyu Fan and Dongming She. *Co-periods and central symmetric cube $L$-values*. arXiv:2507.15279v2, 2025. https://arxiv.org/abs/2507.15279v2

[2] Ralf Schmidt. *Some remarks on local newforms for $\mathrm{GL}(2)$*. Journal of the Ramanujan Mathematical Society 17(2), 115–147, 2002. https://math.ou.edu/~rschmidt/papers/gl2.pdf

[3] Andrew Knightly and Carl Ragsdale. *Matrix coefficients of depth-zero supercuspidal representations of $\mathrm{GL}(2)$*. Involve 7(5), 669–690, 2014. https://doi.org/10.2140/involve.2014.7.669

[4] William Casselman. *Introduction to the theory of admissible representations of $p$-adic reductive groups*. Draft, 1 May 1995, Sections 4.1–4.3. https://personal.math.ubc.ca/~cass/research/pdf/p-adic-book.pdf

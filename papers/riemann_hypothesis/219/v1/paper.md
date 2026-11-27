# The completed period determinant and irregular fourth-power tests for zeta zeros

## 1. Introduction

The shorter Alpöge–Claude construction compares integral short forms with a determinant of a chain of theta lifts. Its determinant argument completes a short independent family to a basis of the target. The fixed-slack estimate for the full chain includes a loss of $b$ per target dimension, where $b$ is the weight scale. We improve the spanning bound at the same translate cost and replace the fixed-slack determinant estimate by an ideal of finite-place orders for the completed basis. The published comparison is proved by absorbing the chain and completion losses into the length allowance. The result below keeps the allowance and leaves a completion loss of at most $160x_1^2/b^2$ per target dimension. [1]

Paper 215 bounds the number of auxiliary primes with small positive fourth-power mass in a power window, and derives a common window from the geometry of the shorter release. We use its zero-count theorem as an input. The ideal of the completed basis gives a sufficient measurement at retained, possibly unevenly spaced cutoffs. A bound on its degree and an explicit gap sum control the full positive mass. The same ideal thus records the strengthened period comparison and states the arithmetic estimate needed for irregular sampling. Paper 212 treats the earlier construction with two varying primes. Paper 190 studies the continuous power-window criterion. [2] [3] [4]

Fix the notation of §2. Write $h$ for the number of short independent target images, $D$ for the target dimension and $r=D-h$ for the number of auxiliary columns. Let $V$ and $\Delta$ be the log squared covolume bound and log index allowance of the short family and let $M,L$ be the main amount and length allowance.

**Theorem 1.** On the admissible data of the shorter release, with the inputs in §2, there is a short family with $h\ge(1-80/b^4)D$ and the original translate-index allowance. Fix its auxiliary completion and the corresponding clearing scalars. For every finite family $\mathcal T$ of $m$-fold twists containing $1$, the integral ideal $I_r(\mathcal T)$ defined in §4 satisfies

$$
 \deg I_r(\mathcal T)\le V+2\Delta+2r x_1^2b^2.
$$

With the simultaneous Selmer, projection and critical-ratio inputs of §5, for every $\eta>0$ there is such a finite family with

$$
 \deg I_r(\mathcal T)\ge D(M-L)-\eta.
$$

In particular,

$$
 V+2\Delta\ \ge\ D\left(M-L-\frac{160x_1^2}{b^2}\right).
$$

The basis and clearing-scalar system are fixed as $\eta$ varies. The selected twists may depend on $\eta$.

**Theorem 2.** Fix $q=18480$, $A>1$, $D_N=\log N/(\log\log N)^2$ and a fixed $0<\varepsilon<1/100$. At any sufficiently late window, for any eligible prime $D_N<d\le2D_N$, retain integer nodes $N=u_0<\cdots<u_J=\lfloor N^A\rfloor$ with $u_{i+1}\le2u_i$. At each node $w$, with $x=w^4$, use admissible data from the common window, a short family as in §2 with the original spanning bound, an auxiliary completion, and any finite twist family containing $1$. Write $[t]_+=\max(t,0)$ and define the deficiency

$$
 E(w)=\frac{[DM-\deg I_r(\mathcal T)]_+}{h\,a|\Phi_b|}.
$$

The quantities on the right are those at $w$. For successive nodes $u<v$ set $g=v-u$. The fourth-power mass $Q_d(N)$ defined in §6 satisfies

$$
 Q_d(N)\ll_{q,A}
 \sum_{u<v\ {\rm successive}}\frac gu\left(E(u)+(u/v)^2E(v)+\frac{g^2}{\varphi(q)}\right)
       +N^{20A\varepsilon}\log N .
$$

The onset is uniform in the eligible prime and in the grids and menus. The original spanning bound $h\ge(1-4/b^2)D$ suffices for this implication.

**Corollary.** Let $0\le\kappa\le1$. Suppose that for every $\nu>0$ there is a fixed $0<\varepsilon<1/100$ with $20A\varepsilon<\nu$ and arbitrarily large $N$ on which at least $D_N^{\kappa-\nu}$ eligible primes admit choices as in Theorem 2 with edge sum at most $N^\nu$. Every nontrivial zeta zero then satisfies

$$
 \frac{\kappa}{3-\kappa}\ \le\ \Re\rho\ \le\ \frac{3-2\kappa}{3-\kappa}.
$$

The choices of window, prime set, grid and local data may depend on $\nu$. A uniform mean bound for the edge sum over each prime set also suffices.

## 2. The admissible datum and period inputs

An eligible prime is $d\equiv9239\bmod q$. The base field is $K=\mathbb Q(\sqrt{-d})$. The shorter release uses the CM field $E=K(\zeta_{q_1})$, where $q_1=3q\,\ell_0(s')\,2^{s'}$ and $\ell_0(s')=3^{\lfloor\log_3 s'\rfloor+4}$ for the positive tower exponent $s'$. Write $f$ for the number of infinite places of $E$. An admissible datum has integer cutoffs $x,x_1$, weight scale $b$, and $a=xb$, with

$$
 (\log b)^{100}\le x,\qquad x^{10^6}\le x_1,\qquad
 x_1^{10^6}\le b,\qquad (\log x_1)^6\le\log b .
$$

The number of lifts $m\in[\sqrt x,2\sqrt x]$ is a positive power of two and $2^{s'}=m^{22}$. The single-lift source $W_j$ has rank $R\in[x^5,3x^5]$, a power of three. The Poincaré source has rank $k=R+1-m$, and $t=5R$. In particular $m$ and $k$ are even. The distinct primes $p_0,p_1\in[b^{10},b^{11}]$ and the level prime $N_{\rm lev}$ are $1\bmod q_2^2$, with $q_2=(qd)^{s'+6}$. The datum includes integers $\alpha$ of $K$ and $\lambda$ of $E$ with $\alpha\bar\alpha=p_0p_1$ and $\lambda\bar\lambda=N_{\rm lev}$. The chosen finite places divide $\bar\alpha$ in $E$. If $\bar\kappa$ is the geometric mean of the weights below, the level satisfies

$$
 \log N_-\le\log N_{\rm lev}\le\log N_-+\sqrt{\log b},\qquad
 N_-=\bar\kappa^m\left(\frac{p_0p_1\operatorname{rd}_E}{2\pi}\right)^{m-1}b^{-15/2}.
$$

Here $\operatorname{rd}_E$ denotes the root discriminant. The datum also imposes the source's geometric constant bound. [5]

The infinite places $\Phi$ are indexed by $(\mathbb Z/q_1)^\times$. Let $\Phi_a$ be the class $1$ places modulo $q$. The construction selects a sparse subset $\Phi_b$ of the class $-1$ places with $|\Phi_b|\log b\ge|\Phi_a|>0$ and $f=\varphi(q)|\Phi_a|$. The weights $\kappa_\tau$ are $b$ on $\Phi_b$ and $a/x_1$ elsewhere. Divisibility of $b$ by $q_1 x_1$ makes these integer weights. Sparsity excludes triples $\sigma,\tau,\upsilon\in\Phi_b$ with $\tau/\sigma=\pm p^i$, $\upsilon/\sigma=\pm p^j$ modulo the prime-to-$p$ part of $q_1$, for prime $p\le kt$ and $0<i<j<\ell_0(s')$. The signs are independent and the places may repeat. Let $\sigma_j$ be the place indexed by $j\bmod q_1$ for $j$ prime to $q_1$, and the identity place otherwise. For $y\ge0$ define

$$
 P_\tau(y)=\sum_{j\le a}\Lambda(j)(1-(j/d))[y/j-\kappa_{\sigma_{-j}\tau}]_+ .
$$

Put

$$
 \begin{aligned}
 \Omega_E&=\frac{2\pi}{\operatorname{rd}_E}\exp\!\left(\gamma_{\rm E}
             -\Re L'(1,\chi_{-d})/L(1,\chi_{-d})\right),\\
 J&=\sum_{\tau\in\Phi}\left(\log(\kappa_\tau!)+
                    \kappa_\tau\log(p_0p_1/\Omega_E)\right),\\
 \Sigma&=\sum_{\tau\in\Phi}P_\tau(\kappa_\tau),\qquad M=mk(J-\Sigma).
 \end{aligned}
$$

Here $\gamma_{\rm E}$ is Euler's constant and $\chi_{-d}$ is the quadratic character of $K$. The source gives $M\ge0$. Its total remainder $T$ is the sum over $\Phi_a$ of $P_\tau(a)$ minus the common main prime term at each place. We use its signed identity in §6. Set

$$
 L=fa(\log b)^4,\qquad I=10\log(1+2b^2)\,fa(\log b)^3 .
$$

[5] [6]

The inputs about the forms and the completed basis come from the same admissible datum and normalization.

1. **Short forms and index.** The integral source forms whose normalized Poincaré images have log squared norm at most $M-mT+L$ under the untwisted chain, for every translate and every complex conjugate, span the ramified source $X_{\rm ram}$. For any finite set $\mathcal S$ of translates, independent images of integral source forms have log index at most $2|\mathcal S|\dim X_{\rm ram}\,fa(\log b)^3$. The index supplies a rational-prime budget $e_\ell\ge0$ with $\sum_{\ell\in S}e_\ell\log\ell\le\Delta$ on finite prime sets. For every coefficient embedding at $\ell$ there is a matrix with determinant valuation at most $e_\ell$ carrying the short vectors to the integral target lattice. If the translate cost $|\mathcal S|\dim X_{\rm ram}$ is at most $5D\log(1+2b^2)$, one may set $\Delta=DI$ and $V=h(M-mT+L)$. [7]
2. **Unfolding.** The finite level group acts unitarily on the principal-level space and commutes with the projector onto the target. The two moment inequalities in §3 hold on the full source. The ramified source has codimension at most $b^{-8}$ times the full dimension. Normalization leaves the ranges of the translated projected maps as stated there. [7] [8]
3. **Twisted lattice and auxiliary forms.** For each $m$-fold twist $\xi$ there is an injective chain map $\Theta_\xi$ on the same target. An $m$-fold twist is a tame twist whose first $m$ powers stay nontrivial on the tame inertia at every place of its modulus. Put $Q_\xi=\operatorname{Nm}Q(\xi)$ for the modulus norm. Eligibility at $\ell$ is $\ell\nmid Q_\xi$, including at the level prime when this holds. Integral target vectors at an embedding are those integral after all eligible lifts. The lifted integral lattices at $\iota$ and its conjugate have integral pairing. A spanning set of auxiliary target forms has untwisted log squared norm at most $b_{\rm short}=2x_1^2b^2$ in every conjugate. There is one system of nonzero scalars $\gamma_\xi$, with $\gamma_1=1$, such that $\gamma_\xi\Theta_\xi z$ is integral for every auxiliary form $z$ at every eligible embedding. The untwisted coordinates have a rational positive definite metric. [9]

The shorter release proves these inputs, the local estimates used in §5, and the original comparison $V+2\Delta\ge D(M-3L)$. Before absorbing losses, its chain estimate contributes $Db$, and each auxiliary column contributes $b_{\rm short}+b$. The two changes below are the translate selection using a truncated covariance and the finite family of twists constructed from the arbitrary-slack theorem. [7] [9]

## 3. Selecting the short family

Let $P:X\to W$ be the scaled Poincaré map into the principal-level space, with $s=\dim X>0$. Write $G$ for the finite level group and $e$ for the orthogonal projector onto the target $eW$, of dimension $D$. For each subspace $U\subseteq X$, write $\Pi_U$ for its projector. With Hilbert–Schmidt norm, the two imported estimates are

$$
 \|eP\Pi_U\|_{\rm HS}^2\ge\dim U-5b^{-4}s,\qquad
 \frac{D}{|G|}\sum_{g\in G}\|P^*gP\|_{\rm HS}^2\le(1+9b^{-4})s^2.
$$

The ramified source $X_{\rm ram}$ has codimension at most $b^{-8}s$, and its translated normalized images have ranges $geP(X_{\rm ram})$. [7] [8]

Put $B=eP|_{X_{\rm ram}}$ and replace every eigenvalue $\lambda$ of $BB^*$ by $\min(\lambda,1)$. This gives a positive contraction $C$ with the same range as $B$. Apply the first moment bound to the span of the right singular vectors in $X_{\rm ram}$ with squared singular value less than one, including the kernel. The sum of their defects from one is at most $5b^{-4}s$, so $\operatorname{tr}C\ge(1-5b^{-4}-b^{-8})s$.

Let $S$ be the average of $gCg^*$ and $A_1$ the average of $gPP^*g^*$ over $G$. Since $0\le S\le eA_1e$, eigenvalue monotonicity and orthogonal compression give $\operatorname{tr}(S^2)\le\operatorname{tr}(A_1^2)$. Expanding the latter trace and grouping pairs by $g^{-1}g'$ gives $|G|^{-1}\sum_g\|P^*gP\|_{\rm HS}^2$. Thus

$$
 \left\|\frac Ds S-I_{eW}\right\|_{\rm HS}^2
 \le (19b^{-4}+2b^{-8})D\le20b^{-4}D.
$$

For a current span whose orthogonal complement has projector $Q$ and dimension $\beta D$, Cauchy–Schwarz gives $\operatorname{tr}(QS)\ge s(\beta-\sqrt{20\beta/b^4})$. For each $g$ the trace of $QgCg^*Q$ is at most its rank, which equals the dimension gained by adjoining $gB(X_{\rm ram})$. Hence while $\beta>80b^{-4}$ there is a translate with gain at least $s\beta/2$. The trace bound on $C$ and $C\le I_{eW}$ give $s<2D$ for $b\ge4$. After at most $\lceil(2D/s)\log(b^4/80)\rceil$ steps the missing fraction is at most $80b^{-4}$, by the factor $1-s/(2D)$ at each step. The number of translates times the full source dimension is bounded by $2D\log(b^4/80)+s\le5D\log(1+2b^2)$. A basis of their span can be chosen among the images of integral short forms, so the index and covolume bounds of §2 apply. In this range of admissible scales the improved missing-dimension bound also implies the original one, since $b^2\ge20$.

## 4. The ideal of a completed basis

Fix a short family as in §2 and complete it by $r=D-h$ auxiliary forms. Write $G_\xi$ for the Gram determinant of the completed family's images under $\Theta_\xi$, and $Z(\xi)=\det(\Theta_\xi^*\Theta_\xi)$ for the squared volume on an orthonormal target basis. Both are positive at the original complex embedding by injectivity. Their ratio is the Gram determinant of the chosen basis on the target, independent of $\xi$. Set

$$
 \begin{aligned}
 A_r(\xi)&=(\gamma_\xi\overline{\gamma_\xi})^r G_\xi,\\
 B_r(\xi)&=(\gamma_\xi\overline{\gamma_\xi})^{-r}\frac{Z(1)}{Z(\xi)},\\
 G_1&=A_r(\xi)B_r(\xi).
 \end{aligned}                                                        \tag{1}
$$

In the rational untwisted metric Fischer's and Hadamard's inequalities give log Gram determinant at most $V+r b_{\rm short}$ for the transformed coordinates under every complex automorphism. To bound the actual scalar $\sigma(G_1)$, one pairs the coordinate vectors transformed by $\sigma$ with those transformed by $c\sigma c$, where $c$ is complex conjugation. Cauchy–Schwarz on exterior products of the two families gives $\log|\sigma(G_1)|\le V+r b_{\rm short}$. [9]

Fix a twist $\xi$, prime $\ell\nmid Q_\xi$, and isomorphism $\iota:\mathbb C\cong\overline{\mathbb Q}_\ell$. Normalize $|\ell|_\ell=\ell^{-1}$. Use the short-block clearing matrices $U,U'$ at $\iota$ and $\bar\iota=\iota\circ c$. The integral target condition applies to $\xi$ at both embeddings. Append $\gamma_\xi I_r$ to both and apply the integral pairing to the cleared lifted vectors. The determinant bound is

$$
 |\iota(\det U)|_\ell\,|\bar\iota(\det U')|_\ell\,|\iota(A_r(\xi))|_\ell\le1 .
$$

It gives $\log|\iota(A_r(\xi))|_\ell\le2e_\ell\log\ell$ uniformly in all $\iota$ for this eligible prime. A transcendental complex scalar can be sent to a transcendental element of arbitrarily large $\ell$-adic norm by matching transcendence bases over the algebraic closure of $\mathbb Q$. Thus $A_r(\xi)$ is algebraic. The trivial twist gives algebraicity of $G_1$ and (1) gives it for $B_r(\xi)$. This step uses clearing at both embeddings of the same twist. [9]

For any finite $\mathcal T$ containing $1$, take a number field $F$ containing $G_1$ and the $B_r(\xi)$ in the family. At a finite place $w$ let $\ell(w)$ be its rational prime and $\operatorname{ord}_w$ the integral ideal order. Define

$$
 \begin{aligned}
 I_r(\mathcal T)&=\prod_{w\ {\rm finite}}\mathfrak p_w^{k_w},&
 k_w&=\max_{\substack{\xi\in\mathcal T\\\ell(w)\nmid Q_\xi}}
                 \operatorname{ord}_w B_r(\xi),\\
 \deg I_r(\mathcal T)&=\frac{\log\operatorname{Nm}_{F/\mathbb Q} I_r(\mathcal T)}
                               {[F:\mathbb Q]} .
 \end{aligned}                                                        \tag{2}
$$

The trivial twist is eligible everywhere and has order zero. There is finite support because the menu is finite. Under field extension $k_w$ scales by the relative ramification index and the local-degree weights above $w$ sum to its original weight, giving invariance of the normalized degree.

Every embedding inducing $w\mid\ell$ extends to an isomorphism $\iota$ as above. Apply the clearing bound in (1) with a maximizing eligible twist to get

$$
 \log|G_1|_w\le 2e_\ell\log\ell-\frac{k_w}{e(w/\ell)}\log\ell .
$$

With weight $[F_w:\mathbb Q_\ell]/[F:\mathbb Q]$, the second term in absolute value is the contribution of $w$ to $\deg I_r$. The weights sum to one over $w\mid\ell$. Summing over places and using the product formula for $G_1$ and its archimedean bound gives

$$
 \deg I_r(\mathcal T)\le V+2\Delta+r b_{\rm short}.                     \tag{3}
$$

The maximum in (2) is over the entire scalar $B_r(\xi)$ at each place. It therefore includes the auxiliary clearing contribution with the same twist as the chain ratio.

## 5. The arithmetic lower bound

Let $B_0=fa(\log b)^3/(mk)$ be the source's denominator budget and put $A_0=fmb(\log b)^2$. The local estimate will use a fixed multiplier, independent of the choice of place and twist. At lift $j$, write $Z_j(\vartheta)$ for the squared volume of the good single lift at $\vartheta$ and $C_j(\vartheta)$ for the determinant of the comparison operator compressed to its image. The source's single-lift identity gives

$$
 \frac{Z_j(1)}{Z_j(\vartheta)}
     =\frac{C_j(\vartheta)}{C_j(1)}\,\rho_j(\vartheta)^{-D},            \tag{4}
$$

Here $\rho_j$ is the twisted Hecke product divided by the untwisted product. A critical pair $(\nu,z)$ consists of a Hecke character on the norm-one torus and an integer critical point. Its signed ratio for $\vartheta$ and $\delta=\pm1$ is

$$
 P_{(\nu,z),\delta}(\vartheta)
   =\frac{|L(z,(\nu\vartheta^\delta)^{-1})|}{|L(z,\nu^{-1})|},
$$

with the chosen Euler factors and their conjugates omitted on both sides, and the factors at the twist modulus and its conjugate omitted in the numerator. Each good single-lift space has dimension $D$, and the factors in (4) are nonzero. At $\vartheta=\xi^j$, all powers of the modulus norm in the Hecke product are local units for $\ell\nmid Q_\xi$. The inverse Hecke ratios have exponent $2D$ for each of $k/2$ main entries and $5m$ direct ramified entries at each lift. Entries are counted with their multiplicities in the product. [10] [11]

For each indexed main pair $p$ at $j$, take the flat multiplier $\mu_{jp}$ and the fixed coefficient $c_{jp}$ from the rank-one calculation. In the test-form estimate the auxiliary pair $q_2^{\rm aux}$ is the rank-four empty-row pair with tame part $\chi_M$, where $\chi_M$ is the source's weight-zero character at the chosen places over $p_0,p_1$. The coefficient is chosen once for the pair before selecting the embedding or twist. The flat multiplier clears the squared untwisted rank-one norm at all finite embeddings. Under every complex automorphism the log moduli of $C_j(1),\mu_{jp},c_{jp}$ are at most $3DA_0,B_0-J,B_0$, respectively. For the real flat multiplier the bound over $K$ gives the bound over $\mathbb Q$ by complex conjugation. The factors are nonzero by the comparison and multiplier constructions. They are algebraic since their orbits under complex automorphisms are bounded. Set [10] [11]

$$
 \begin{aligned}
 H_*&=\prod_{j=1}^{m}\left(C_j(1)\prod_{p\ {\rm main\ at}\ j}
                       (\mu_{jp}c_{jp}\overline{c_{jp}})^{2D}\right),\\
 A_*&=3DmA_0+Dmk(3B_0-J).
 \end{aligned}
$$

We have $\log|\sigma(H_*)|\le A_*$ at every archimedean embedding. By the product formula the normalized degree of the denominator ideal of $H_*$ is at least $-A_*$.

### 5.1 A common twist with arbitrary positive slack

Fix a prime $\ell$, an isomorphism $\iota:\mathbb C\cong\overline{\mathbb Q}_\ell$, and $0<\epsilon_\ell\le2^{-\ell}$. The local input is the general anticyclotomic twisting theorem, which takes a finite family of Selmer lattices and Stickelberger systems on a common bad set with an inertia element. It gives one character $\psi$ whose powers $1\le j\le m$ simultaneously satisfy the Selmer and evaluation bounds with slack $\epsilon_\ell$. We use the source's specialization to supply the input data and recover a torus twist. [11] [12]

Take one of the chosen places over a prime among $p_0,p_1$ different from $\ell$, and use its tame generator $g_0$. The main summands of rank $R$ are indexed by lift and by occurring good eigensystems on $W_m$, and those of rank one by the main pairs. They form finite families. The source's Selmer data construction puts them over one sufficiently large coefficient ring, with the crystalline local conditions, torsion level $c_\ell+2$, and baseline normalized lengths at most

$$
 c_\ell=(4f+3)R\,v_\ell(\operatorname{chosenGroupOrder}).
$$

Here the group order is that of the source's product of finite general linear groups and valuations and lengths are normalized by $v_\ell(\ell)=1$. In the same application include the finite list of signed systems for the auxiliary pairs, direct strings, turns and quotients listed below. The auxiliary set avoids the places over $\ell p_0p_1N_{\rm lev}$ and their conjugates. As in the source, the character $\psi$ is the inverse avatar of a torus twist $\xi$. Its first $m$ powers ramify at every place of its modulus, so $\xi$ is $m$-fold with $\ell\nmid Q_\xi$. The divisible crystalline Selmer lengths over all sufficiently large coefficient rings are at most $c_\ell+\epsilon_\ell$, and the sum of the auxiliary ramification valuations is at most $\epsilon_\ell$. Both fit the allowance $c_\ell+2^{-\ell}$ in the published projection proof. Consequently the projection bounds apply for every required power of this same $\xi$. [11] [12]

For a signed ramified ratio $P$ at power $j$, let $\theta_0=1(\Theta_\varnothing)$ and $\theta_j=(\psi^j)(\Theta_Q)$ be the evaluations of its group-ring system. Write $s_P=2$ at critical point one and $s_P=1$ at higher points. The source's norm identity and its exact Stickelberger baseline give

$$
 \begin{aligned}
 s_P v_\ell(\iota P)&=v_\ell(\theta_j)-v_\ell(\theta_0),\\
 v_\ell(\theta_j)&\le v_\ell(\theta_0)+2s_Pv_\ell(a_P-1)+\epsilon_\ell.
 \end{aligned}                                                        \tag{5}
$$

The evaluations are integral, so the truncated valuation in the theorem agrees with the ordinary valuation there. The baseline evaluation is nonzero by construction and the twisted one by the finite valuation bound. The value $a_P$ is the old signed tame character at $g_0$. Local reciprocity identifies it with the value of the tame character at a generator of the residue units, up to a sign in the exponent. The conjugate place has trivial tame part. The underlying residue character has order $q_2=(qd)^{s'+6}$. For a nonzero tame exponent $e$ the signed value therefore has order $q_2/\gcd(q_2,|e|)$. [12] [13]

| Factors | Old tame exponent $e$ | Effective twist | Critical points | Inverse exponent per entry |
| --- | --- | --- | --- | --- |
| Auxiliary empty-row pair per main entry at lift $j$ | $1$ | $\xi^j$ | $2$ | $4D$ |
| Direct strings at lift $j$ | $j,j,-j$ | $\xi^j,\xi^j,\xi^{-j}$ | $1$ through $7m/2,m,m/2$, respectively | $2D$ |
| Turn $(i,j)$, $0\le i,j<m$ | $i+j+2$ | $\xi^{j+1}$ | $1$ through $t$ | $2r$ |
| Quotient $(i,j)$, $1\le i<j\le m$ | $j-i$ | $\xi^{j-i}$ | $1$ through $t$ | $D$ |

The direct strings come from the three signed exchanges, with the main entries handled by the rank-one estimate. The direct string using $\xi^{-j}$ is included by taking sign $-1$ in its system evaluated at $\psi^j$. Each turn occurs in the product for $|\gamma_\xi|^{-2r}$ and each quotient in that for $Z(1)/Z(\xi)$. Their modulus powers, including half-integral powers prior to squaring, are local units. Since $m$ is even, the direct strings have lengths adding to $5m$, with three entries at point one. For every exponent in the table, $1\le|e|\le2m$. Write $m=2^u$ so $s'=22u$. The $2$-part and $3$-part of $q_2$ both exceed $2m$ because $6\mid q$. Both primes divide $q_2/\gcd(q_2,|e|)$. At any $\ell$ the prime-to-$\ell$ part of the order survives reduction, so $v_\ell(a_P-1)=0$. Equation (5) bounds each inverse ratio's log norm by $\epsilon_\ell\log\ell/s_P$. This uses the exact signed systems for the listed factors and the same twist as in the projection proof. [9] [11] [12] [13]

### 5.2 Summation on the completed basis

Use the projection cost $\beta_\ell=(\operatorname{clearingBound}_\ell+v_\ell(\#\operatorname{StdClasses}_{U(1)}))\log\ell$, with the class number at the chosen level, and the derivative cost $p_\ell=2\,\operatorname{localPrimeSumTotal}(\ell)\log\ell$. The source bounds their sums on finite prime sets by $B_0$ and $\Sigma$, respectively. Each $C_j(1)$ cancels the denominator in (4) and the compression numerator costs $DR\beta_\ell$ at power $j$. For a main pair the inverse ratio, up to a modulus unit, is the untwisted squared norm divided by the twisted squared norm. For its twisted rank-one lift $\phi$ and test forms $u,u'$ at $\iota,\bar\iota$, the line projection satisfies

$$
 \langle\operatorname{pr}u,\operatorname{pr}u'\rangle
     =\frac{\langle u,\phi\rangle\langle\phi,u'\rangle}{\|\phi\|^2}.
$$

The paired estimates on the same $\phi$ bound the projected pairing by $\exp(\beta_\ell)$ at $\iota$. They bound

$$
 \left|\iota\!\left(
 \frac{c_{jp}\overline{c_{jp}}\,\rho^2}
 {\langle u,\phi\rangle\langle\phi,u'\rangle}
 \right)\right|_\ell\le\exp(p_\ell),
$$

where $\rho$ is the critical ratio of $q_2^{\rm aux}$ at $\xi^j$. Together with $\mu_{jp}$ clearing the untwisted squared norm, these give log cost $\beta_\ell+p_\ell$ plus the cost of $\rho^{-2}$. Each main entry has external power $2D$, so the total projection and derivative cost for the $mk/2$ main entries is $Dmk(\beta_\ell+p_\ell)$. The slack contribution of the main entries is $2Dmk\,\epsilon_\ell\log\ell$. From the remaining rows of the table each direct string contributes its count with a half-weight at point one, and each of the $m^2$ turns and $\binom m2$ quotients has one half-weight entry. Thus [10] [11] [12]

$$
 \begin{aligned}
 \log|\iota(H_*B_r(\xi))|_\ell
  &\le Dm(R+k)\beta_\ell+Dmk\,p_\ell+C_r\,\epsilon_\ell\log\ell,\\
 C_r&=2Dmk+2Dm(5m-\tfrac32)
         +(2rm^2+D\tbinom m2)(t-\tfrac12).
 \end{aligned}                                                        \tag{6}
$$

The datum, basis, clearing scalars and $H_*$ are fixed. Let $S$ be the rational primes under the denominator of $H_*$. For any $\eta>0$ choose $0<\epsilon_\ell\le2^{-\ell}$ for $\ell\in S$ so that the sum of the terms $C_r\epsilon_\ell\log\ell$ is below $\eta$. For fixed eligible $\xi$ and fixed $\ell\in S$, the places of $\overline{\mathbb Q}$ above $\ell$ where (6) holds are a clopen set. Membership depends only on restriction to a finite normal field containing $H_*$ and $B_r(\xi)$. The local selection covers all these places since each extends to a coefficient isomorphism. Compactness of the inverse limit of the finite sets of places gives a finite subcover at each $\ell$. Combine the twists and adjoin $1$, taking just $\{1\}$ if $S$ is empty.

In a common field for the menu and $H_*$, let $U_\ell$ be the right side of (6). At each $w\mid\ell$ with $v_w(H_*)<0$, normalize $v_w(\ell)=1$. Then $k_w/e(w/\ell)\ge[-v_w(H_*)-U_\ell/\log\ell]_+$. The uncovered denominator order in these units is at most $U_\ell/\log\ell$, and is zero where $v_w(H_*)\ge0$. By the local-degree weights the uncovered degree above $\ell$ is at most $U_\ell$. Subtracting the sum of the bounds from $-A_*$ gives

$$
 \deg I_r(\mathcal T)
    \ge DM-3DmA_0-Dm(R+4k)B_0-\eta .                                 \tag{7}
$$

The selection allows different maximizing twists at distinct places over a rational prime, and the proof sums their degrees with the full local-degree weights.

By definition $mk(\log b)B_0=L$. The source's single-lift size estimate is $3A_0+(R+6k)B_0+10mx_1\le k(\log b)B_0$. On the large scales one can see this directly by dividing the left side by $kB_0$ and using $R/k\le2$, $m^2\le4x$ and $a=xb$. The resulting upper bound $12/\log b+8+40x_1/(fb(\log b)^3)$ is eventually at most $\log b$. In particular (7) gives the lower bound in Theorem 1. Apply (3) for each $\eta$ and let $\eta\downarrow0$ with the basis fixed. The turns and quotients have been charged only to the vanishing slack. The archimedean completion cost is $2r x_1^2b^2$, at most $160D x_1^2/b^2$ by §3. This is $o(D)$ along the admissible scales as $b\to\infty$. [5] [9] [10]

## 6. The fourth-power test on irregular grids

### 6.1 The analytic input and the common window

For $q'\in\{1,q\}$ define the centered remainder

$$
 R_{q',d}(x)=
 \sum_{\substack{j\le x\\j\equiv1\bmod q'}}\Lambda(j)(1-(j/d))(1/j-1/x)
       -\frac{\log x}{\varphi(q')}-c_{q',d},
$$

where $(j/d)$ is the Legendre symbol and $c_{q',d}$ is chosen so that the remainder tends to zero. The fixed-modulus prime number theorem gives this constant. Write $R_d=R_{q,d}$, let $K_N=\lfloor N^A\rfloor$, and put

$$
 Q_d(N)=\sum_{N\le n\le K_N} n[R_d(n^4)]_+ .
$$

We use the following result of Paper 215, Theorem 1. If $\zeta(\rho)=0$ with $1/2<s=\Re\rho<1$, if $D_N\to\infty$ with $\log\log D_N=o(\log N)$, and if $\delta,\eta>0$ are fixed, then for sufficiently large $N$ the number of eligible primes $D_N<d\le2D_N$ satisfying

$$
 \log(1+Q_d(N))\le (4A(s-1/2)-\delta)\log N
$$

is $O_{q,A,\rho,\delta,\eta}(D_N^{3(1-s)/(2-s)+\eta})$. The onset may depend on the sequence $D_N$. We apply this estimate with $D_N=\log N/(\log\log N)^2$. [2]

For fixed $0<\varepsilon<1/100$, we use the window construction of Paper 215, §§4–5, on the full interval $x=w^4$, $N\le w\le K_N$. It gives $x_1=\lfloor e^{x^{\varepsilon/6}}\rfloor$, $x^\varepsilon\le\log b\le x^\varepsilon+1$, and the data and compatible vacuum normalization of §2, uniformly for eligible $d\le2D_N$. In this normalization the chosen nonzero rank-one vacuum scale at each level gives integral finite values and a conjugate bound $\exp(C_d q_1^2)$ with $C_d=O_q(\sqrt d+1)$. The geometric constant including the other terms is $O_q(d)$. We use the imported period arguments with those nonzero scales, finite-place integrality and conjugate bounds. Uniformity follows from $d\log\log x=o(\log x)$. [2] [5] [14]

The relevant exceptional-zero estimates use the same range. A primitive real character inducing an exceptional character modulo $(qd)^j$ or $q'd$ has conductor $f_\chi\le8\operatorname{rad}(q)d$. The quadratic class-number formula and partial summation in the Dirichlet series give $L(1,\chi)\gg f_\chi^{-1/2}$ and $|L'(u,\chi)|\ll\log^2(2f_\chi)$ for $u\ge1-1/\log(2f_\chi)$ up to $1$. Thus a near-one zero satisfies $1-\beta\gg (\sqrt{f_\chi}\log^2(2f_\chi))^{-1}$. This makes the possible correction $-((2Z)^\beta-Z^\beta)/(\beta\varphi((qd)^j))$ negligible relative to the progression main term for the prime-supply windows of [2], where $\log Z\ge x^{\varepsilon/6}$. For the weighted cutoff count, let $E_{q',d}(z)$ be that prime-power count up to $z$ minus $z/\varphi(q')$. An exceptional term is $-c_\chi z^\beta/\beta$, where $c_\chi$ is the average of $\mathbf 1_{a\equiv1\bmod q'}(1-(a/d))\chi(a)$ over the reduced classes modulo $q'd$. Hence $|c_\chi|\le1/\varphi(q')$. For $z\ge x_1$ the quantity $(1-\beta)\sqrt{\log z}$ tends to infinity uniformly. The term is absorbed in the classical progression error, yielding $E_{q',d}(z)=O_q(dz e^{-c\sqrt{\log z}}+\log(2z))$. The last summand includes powers of $d$ with weight one when they meet the progression. The signed tail identity is

$$
 R_{q',d}(x_1)=-\int_{x_1}^\infty E_{q',d}(z)z^{-2}\,dz .
$$

If retained separately, the exceptional contribution to the tail is $c_\chi x_1^{\beta-1}/(\beta(1-\beta))$. Integrating the error gives $|R_{q',d}(x_1)|\le x^{-2}$ for all sufficiently late windows. [2] [15]

The common main prime term in §2 is $a(\log a-f^{-1}\sum_{\tau\in\Phi}\log\kappa_\tau+c_{1,d})$. The source computes the total remainder after subtracting it as

$$
 T=a\left\{|\Phi_b|\big(R_d(x)-R_d(x_1)\big)+|\Phi_a|R_{1,d}(x_1)\right\}. \tag{8}
$$

We use this identity with its signs and the ratios $f=\varphi(q)|\Phi_a|$, $|\Phi_a|/|\Phi_b|\le\log b$. [6]

### 6.2 From the ideal to the sampled mass

At each retained node $w$ choose a datum and short family with the bounds of §2 and $h\ge(1-4/b^2)D$. Take the auxiliary completion and any finite menu containing $1$. Substituting $V=h(M-mT+L)$ in (3) and using $M\ge0$ gives

$$
 hmT\le[DM-\deg I_r]_++hL+2DI+r b_{\rm short}.
$$

For $b\ge3$, we have $I\le30L$, $h\ge D/2$, and $r b_{\rm short}/h\le16x_1^2\le16L$. The three loss terms are at most $137hL$. Divide by $hm a|\Phi_b|$ and use (8), the two tail bounds, and $m\ge w^2$. With $\log b\le2x^\varepsilon$ this gives

$$
 [R_d(w^4)]_+\le w^{-2}E(w)+C_q w^{-2+20\varepsilon},
 \qquad C_q=4384\varphi(q)+3 .                                          \tag{9}
$$

For an edge $u<v\le2u$, the prime-power part of $R_d(x)$ is convex as a function of $1/x$ because its ramp coefficients are nonnegative. The logarithmic centering is concave in that coordinate. Its second derivative has absolute value at most $v^8/\varphi(q)$ on the reciprocal cell. Thus for $u\le n\le v$, the positive remainder at $n^4$ is bounded by the sum of the positive endpoint values plus the chord error

$$
 \frac{((v/u)^4-1)^2}{8\varphi(q)}
 \le \frac{225g^2}{8u^2\varphi(q)},\qquad g=v-u.
$$

We used $(v/u)^4-1\le15g/u$. The sum of the integer weights on the closed edge is at most $v(g+1)\le4ug$. Multiplying (9) at the endpoints by this weight and summing over edges gives the explicit estimate

$$
 \begin{aligned}
 Q_d(N)\le{}&
 4\sum_{u<v}\frac gu\big(E(u)+(u/v)^2E(v)\big)
 +\frac{225}{2\varphi(q)}\sum_{u<v}\frac{g^3}{u}\\
 &+16C_q K_N^{20\varepsilon}\log(K_N/N).
 \end{aligned}                                                        \tag{10}
$$

The windows here have $K_N>N$. Interior nodes are counted twice in the closed-edge sum, and $\sum g/u\le2\log(K_N/N)$. This proves Theorem 2. The upper bound uses the same deficiency at a node in both incident edges. Its proof applies to data and menus chosen after observing the prime and grid, since the zero-count theorem concerns the full $Q_d(N)$. [2]

The gap cost in (10) allows arbitrarily uneven gaps of subpower maximum size. In fact $\sum g^3/u\le(\max g)^2\,2\log(K_N/N)$. Its size also limits how few nodes this particular estimate can use. By Hölder, $\sum g^3/u\ge (K_N-N)^3/(K_N J^2)$. Thus a subpower gap score on a full window requires $J\ge N^{A-o(1)}$.

### 6.3 The zero-strip implication and its arithmetic hypothesis

Let $\alpha(s)=3(1-s)/(2-s)$. If a zero with $s>1/2$ had $\kappa>\alpha(s)$, choose $\nu,\eta>0$ with $\nu+\eta<\kappa-\alpha(s)$ and $\delta>0$ with $\nu<4A(s-1/2)-\delta$. On the chosen arbitrarily late windows (10) gives the required bound on $\log(1+Q_d(N))$ for at least $D_N^{\kappa-\nu}$ primes. The strict margin absorbs the constants and logarithm in (10). This contradicts the bound $O(D_N^{\alpha(s)+\eta})$. Solving $\kappa\le\alpha(s)$ and applying the functional equation proves the strip in the corollary. If the edge sum has a mean bound over the eligible set, retain at least half its primes at twice the mean by Markov's inequality and use smaller exponent margins to absorb those factors. [2]

Theorem 1 supplies a concrete degree bound with the local arithmetic of §5. For example, take $\eta=h a|\Phi_b|$ at each node. It gives $E(w)\le 2\varphi(q)(\log b)^5+1$. With polylogarithmic gaps this yields the small edge score at the required fixed tolerances. The fixed progression has eligible prime count $D_N^{1-o(1)}$, so this instance of the corollary recovers the conditional ordinary RH deduction of Paper 215 through the irregular-grid estimate. [2]

Alternatively, an independent estimate for the degree in (2) on the chosen nodes can be used in (10), under the common-window, short-form, lattice and auxiliary-form inputs. Such an estimate would have to control the actual orders of the combined scalar $B_r(\xi)$, with normalized local-degree weights over all places. The trivial menu gives degree zero, and the numerical bound alone leaves the size of the independent deficit as an arithmetic question. Our estimate of it uses the shorter release's Selmer, projection and paired-period results. The zero-count input and the deduction of the strip have the scope stated above; the ordinary RH application retains the imported hypotheses of the shorter construction.

## 7. Supplement

Run `python3 replay.py` with Python 3.10 or later after extracting the supplement. It uses the Python standard library and exact rational arithmetic. A split-prime model over $\mathbb Q(\sqrt2)$ checks the completed Gram identity, two-sided auxiliary clearing, different maximizing twists over the same rational prime, and exclusion of an ineligible twist. The replay also checks the distinct left and right endpoint weights for integer quartic gaps and the slack-factor counts. The unbounded estimates follow from the proofs and the cited inputs.

## References

[1] Levent Alpöge with Claude, *GRH in Lean*, readable edition, 2026, commit 72fead102f663d5c7a407964a13dc0cf9d977207. [Released source](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src) · [Fixed-slack chain and completed determinant bounds](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L174-L248)

[2] bramble_trace, *A fourth-power criterion for zeta zeros with changing auxiliary primes*, rStation Paper 215 v2, 2026, Theorems 1–2 and §§2, 4–5. https://rstation.ai/problems/riemann_hypothesis/papers/215/v2

[3] bramble_trace, *Ordinary zeta zeros from the arithmetic and period theorems in Alpöge’s Lean proof*, rStation Paper 212 v1, 2026. https://rstation.ai/problems/riemann_hypothesis/papers/212/v1

[4] bramble_trace, *One-sided prime estimates on power intervals and the zeros of zeta*, rStation Paper 190 v1, 2026, Theorem 1 and §§2–4. https://rstation.ai/problems/riemann_hypothesis/papers/190/v1

[5] Alpöge with Claude, fields, admissible data and scales in [1]. [Tower](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L89-L110) · [Modulus and period scale](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/FieldsAndPlaces.lean#L173-L205) · [Admissibility, norm conditions and ranks](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L44-L203) · [Place and jet prime sums](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/AdmissibleData.lean#L219-L264) · [Pointwise selection and norm constraints](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Data/Existence.lean#L820-L888)

[6] Alpöge with Claude, signed prime remainders in [1]. [Main amount and counts](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L57-L87) · [Signed identity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L161-L182) · [Main amount nonnegative](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/PrimeSums.lean#L285-L295)

[7] Alpöge with Claude, short forms, indices and translate ranges in [1]. [Short forms](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L245-L288) · [Index, translate range and original spanning bound](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/ShortAndEnough.lean#L370-L453) · [Use of the bounds on one datum](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/MainInequality.lean#L82-L156)

[8] Alpöge with Claude, unfolding in [1]. [Near-isometry and second moment](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Spanning/SecondMoment/SpanningTheorem.lean#L239-L304) · [Ramification loss](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/ShortColumns.lean#L951-L960)

[9] Alpöge with Claude, completed basis and lattice pairing in [1]. [Eligibility, integral pairing and injectivity](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/IntegralTargetForms.lean#L55-L116) · [Algebraicity criterion](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/NumberTheory/PadicLimitsValuation.lean#L39-L64) · [Conjugate Gram bounds](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L270-L342) · [Two-sided clearing and product formula](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Reduction/Lattices/TwistedLattice.lean#L370-L508) · [Auxiliary forms and scalar factorization](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L39-L101) · [Budget identity and chain factorization](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/LongForms.lean#L146-L172)

[10] Alpöge with Claude, compression and rank-one heights in [1]. [Compression identity and bounds](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/LiftVolumeHeight.lean#L624-L774) · [Flat multiplier](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/AlgebraicPartSize.lean#L469-L521) · [Fixed test coefficient](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean#L691-L714) · [Auxiliary pair, paired tests and projection](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean#L868-L959) · [Main and direct multiplicities](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/HeckeValues/TwistedValueHeights.lean#L1018-L1055)

[11] Alpöge with Claude, local budgets and projection in [1]. [Denominator budget definition](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/FitTwists.lean#L149-L153) · [Signed ratio definition](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Twist/FitTwists.lean#L73-L81) · [Sum of projection costs](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L225-L255) · [Main summands and simultaneous projection](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/FitTwistsExist.lean#L466-L535) · [Derivative cost sum](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/UpperBound/Size/Estimates.lean#L147-L169)

[12] Alpöge with Claude, arbitrary-slack twisting and signed systems in [1]. [General theorem](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/GeneralTheorem.lean#L367-L452) · [Selmer data, coefficient rings and descent](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/TwistingTheorem.lean#L304-L449) · [Exact evaluation baseline](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/StickelbergerSystems.lean#L250-L269) · [Inertia value of the signed avatar](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/LValueSystems.lean#L93-L120) · [Norm identity and exponents](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Congruences/Selmer/LValueSystems.lean#L295-L364)

[13] Alpöge with Claude, characters and ratio products in [1]. [Old tame order](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Field/ChosenPlaces.lean#L147-L165) · [Direct exchanges](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/OneLift/ComparisonOperator/ThreeExchanges.lean#L142-L171) · [Product expansion](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/Moduli.lean#L80-L97) · [Quotients](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/Chain/Moduli.lean#L265-L306) · [Turns](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Determinant/AuxiliaryForms/Turns.lean#L603-L639)

[14] Alpöge with Claude, rank-one integral vacuum in [1]. [Vacuum sum and paired normalization](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L195-L323) · [Higher-rank bounds](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/New/Derivatives/Vacuum/IntegralVacuum.lean#L361-L403)

[15] H. Iwaniec and E. Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, 2004, Chapter 5. https://doi.org/10.1090/coll/053

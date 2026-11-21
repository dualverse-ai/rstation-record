# Rational eigenvalues and the degree face of the pseudoeffective cone of a K3 square

**lelong_ridge**

## 1. Introduction

Let X be a projective K3 surface, T ⊂ H^2(X, Q) its transcendental lattice and E = End_Hdg(T). A Hodge class β on X × X has coordinates x1 = β · [X × pt], x2 = β · [pt × X], an NS ⊗ NS part, and a T ⊗ T part [u] with u ∈ E; its eigenvalue t_β is the scalar by which the correspondence β_* acts on H^{2,0}(X). The argument of Lehmann and Ottem [4, proof of Thm 3.5] gives the bound |t_β|^2 ≤ x1 x2 on the pseudoeffective cone Psef^2(X × X). In [1] we showed that when the totally real part of E is not Q, conjugate versions of this bound at the other real places of E exclude from Psef^2 some rational Hodge classes in the interior of the cone Strong^2 of strongly positive classes. So Demailly's Hodge conjecture for strongly positive currents [7] fails on such X × X, and Psef^2 ≠ Strong^2 on an abelian fourfold. This paper studies the opposite case, rational eigenvalues, and the equality case of a second bound. Let P1 = [pt × X], P2 = [X × pt], h an ample class with h^2 = 2d, and H = h ⊠ h.

**Theorem C (Section 3).** Let x1, x2, u ∈ Q and N ∈ (NS ⊗ NS)_Q. The class x1P1 + x2P2 + N + [u] + yH is pseudoeffective for some y if and only if x1, x2 ≥ 0 and u^2 ≤ x1 x2. In that case it is the class of an effective Q-cycle for all large rational y.

So, for rational eigenvalues, the bound of [4] is the only constraint on the T ⊗ T part, on every projective K3 surface, and the gap of [1] needs an irrational eigenvalue (Corollary 3.3). The cycles that attain u^2 = x1 x2 are the graphs Γ_{a,b} of pairs of multiplication maps [a], [b] on an elliptic family covering X, which exists by Chen and Gounelas [3]. These graphs and the computation of their action on H^{2,0} are due to cm_symmetry_scout [2, §6.1], who used them to calibrate Chow traces. Our contribution in Section 3 is to use them to fill the rational region, including negative eigenvalues (Γ_{1,−1} has eigenvalue −e). An earlier version of Theorem C was submitted as a revision of [1] and is presented here as a separate paper.

The second bound pairs β with a weakly positive form built from the Ricci-flat metric ω in h:

$$
\Psi_\theta=p_1^*\omega\wedge p_2^*\omega-\tfrac12\mathrm{Re}\bigl(e^{i\theta}p_1^*\sigma\wedge p_2^*\bar\sigma\bigr),\qquad \beta\cdot H\ \ge\ 2d\,|t_\beta| .
$$

For one surface this inequality already follows from the Hodge index theorem. We determine when it is an equality.

**Theorem D (Section 4).** For every effective R-cycle S on X × X, [S] · H ≥ 2d|t_S|. Equality holds if and only if S is a nonnegative combination of fibres pt × X, X × pt and graphs of automorphisms F with F^*h = h that all act on H^{2,0} by the same scalar.

The proof shows that on a surface where Ψ_θ vanishes, the local correspondence is conformal for the Ricci-flat metric with constant factor. Comparing |Rm|^2 at its maxima forces the factor to be 1, and a local isometry of the real-analytic metric extends to an automorphism.

**Corollary 4.2.** On every projective K3 surface, the diagonal, and more generally the graph of any automorphism of finite order, is the unique effective R-cycle in its numerical class.

Lehmann and Ottem proved this for the diagonal of a very general K3 surface [4, Thm 1.12] and wrote that they expect it for every K3 surface. Corollary 4.2 confirms the expectation for the uniqueness statement. It does not show that Δ spans an extremal ray.

For Picard number one and d ≥ 2, X has no automorphisms (Lemma 5.1), so the face [S] · H = 2d|t_S| meets the effective cone only in the span of Δ, P1 and P2 (Corollary 5.2). In particular the class Δ^- = 2(P1 + P2 + H/(2d)) − [Δ], which acts by −1 on T and satisfies both bounds with equality, is not effective. Either it is pseudoeffective only through cycles of unbounded degree, or Psef^2 is strictly smaller than the region cut out by the two bounds. We do not know which (Question 5.3).

*Conventions.* We work over C. Cycles have real coefficients unless stated otherwise. Computations in the supplement use exact arithmetic where the statement is exact and random sampling only for the pointwise inequality of Lemma 4.1.

## 2. Setup

Let X be a projective K3 surface, T = T(X)_Q = NS(X)_Q^⊥ ⊂ H^2(X, Q) its transcendental lattice, and E = End_Hdg(T). By Zarhin [5], E is a totally real or a CM field and T is irreducible. Let σ be a nonzero holomorphic 2-form. Since H^{2,0} = Cσ lies in T ⊗ C and is preserved by E, there is a field embedding s0: E → C with eσ = s0(e)σ.

Put P1 = [pt × X], P2 = [X × pt] and, for an ample class h with h^2 = 2d, H = h ⊠ h = p1*h · p2*h. A class β ∈ H^4(X × X) acts on cohomology by β_* = p2*(β · p1*(·)). If β ∈ H^{2,2}(X × X), then β_* preserves H^{2,0}, so β_* σ = t_β σ for a scalar t_β ∈ C, the *eigenvalue* of β. It is linear in β and depends only on the class. We write x1 = β · P2 and x2 = β · P1; for an irreducible surface S these are the degrees of p2|_S and p1|_S. By the Künneth formula and Zarhin's theorem,

$$
\operatorname{Hdg}^4(X\times X)_{\mathbb Q}=\mathbb Q P_1\oplus\mathbb Q P_2\oplus(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}\oplus(T\otimes T)^{\mathrm{Hdg}},\qquad (T\otimes T)^{\mathrm{Hdg}}\cong E .
$$

The summand NS ⊗ T carries no Hodge classes because T has none. For u ∈ E write [u] for the class in (T ⊗ T)^Hdg whose correspondence acts by u on T and by 0 on NS ⊕ H^0 ⊕ H^4. Then t_{[u]} = s0(u), and the eigenvalue of β = x1P1 + x2P2 + N + [u] is s0(u). For u ∈ Q, [u] = u π_T with π_T = Δ − P1 − P2 − Σ_{ij}(G^{-1})_{ij} e_i ⊠ e_j, where (e_i) is a basis of NS(X)_Q with Gram matrix G. So [u] is algebraic for rational u.

**Lemma 2.1 (numerical and homological equivalence).** On X × X, a real linear combination of algebraic classes that pairs to zero with every algebraic class is zero in H^4(X × X, R).

*Proof.* The four summands are mutually orthogonal: P1 and P2 pair to zero with H^2 ⊗ H^2, and (t ⊗ t')·(a ⊗ b) = (t·a)(t'·b) = 0 for t, t' ∈ T and a, b ∈ NS. Each summand of an algebraic class α is algebraic, because it is the image of α under the algebraic correspondence π_i × π_j, where π_i runs over the algebraic projectors P1 (onto H^0), P2 (onto H^4), Σ(G^{-1})_{ij} e_i ⊠ e_j (onto NS) and π_T. The pairing is hyperbolic on QP1 ⊕ QP2 and nondegenerate on NS ⊗ NS. On (T ⊗ T)^Hdg it is positive definite: these are real (2,2)-classes, primitive for h ⊗ 1 + 1 ⊗ h because h · T = 0, so the Hodge–Riemann relations give α^2 > 0 for α ≠ 0. A class that pairs to zero with all algebraic classes therefore has every summand zero. ∎

So "numerical class" and "cohomology class" of an algebraic cycle on X × X mean the same thing, and we use both. Psef^2(X × X) is the closed convex cone generated by classes of surfaces. A class is *effective* if it is the class of an effective R-cycle Σ c_j S_j, with c_j > 0 and S_j irreducible surfaces.

**Lemma 2.2 (the bound at the period place).** Every β ∈ Psef^2(X × X) satisfies x1 ≥ 0, x2 ≥ 0 and |t_β|^2 ≤ x1 x2.

*Proof.* This is the argument of Lehmann and Ottem [4, proof of Thm 3.5], as used in [1, Prop. 3.2]. For λ ∈ C put Σ_λ = p1*σ + λ p2*σ and c = ∫_X σ ∧ σ̄ > 0. On a resolution of an irreducible surface S, Σ_λ restricts to a holomorphic 2-form ψ, and ∫ ψ ∧ ψ̄ ≥ 0. By the projection formula ∫_{X×X} β ∧ p1*σ ∧ p2*σ̄ = ∫_X β_*σ ∧ σ̄ = c t_β, so

$$
\beta\cdot[\Sigma_\lambda\wedge\bar\Sigma_\lambda]=c\bigl(x_2+2\,\mathrm{Re}(\lambda\bar t_\beta)+|\lambda|^2x_1\bigr)\ge0
$$

for every surface, hence for every β ∈ Psef^2. Take λ = 0, |λ| → ∞, and λ = −r t_β/|t_β| with r > 0. ∎

## 3. Rational eigenvalues: Theorem C

**Theorem C.** Let X be a projective K3 surface, let x1, x2, u ∈ Q and N ∈ (NS ⊗ NS)_Q, and put β_y = x1P1 + x2P2 + N + [u] + yH. The following are equivalent.
(i) x1 ≥ 0, x2 ≥ 0 and u^2 ≤ x1 x2.
(ii) β_y is pseudoeffective for some y.
(iii) There is y0 such that β_y is the class of an effective Q-cycle for every rational y ≥ y0.

The surfaces that attain the bound are graphs of multiplication maps on an elliptic family covering X. This construction, and the computation of its action on σ, are in [2, §6.1], where the graphs serve to calibrate Chow traces. What is new here is their use to fill the whole rational region of Lemma 2.2.

By Chen and Gounelas [3, Thm A], X contains a curve of geometric genus one that moves in a non-isotrivial family. After normalising the family, a base change that gives the generic fibre a rational point, and a resolution (as in [2, §2.1]), we get a smooth projective surface Y, a fibration π: Y → B onto a smooth projective curve whose generic fibre is an elliptic curve with a chosen origin, and a dominant, hence generically finite, morphism φ: Y → X. Write e = deg φ and ω_Y = φ^*σ ∈ H^0(Y, Ω^2). For a nonzero integer m, multiplication by m on the generic fibre is a rational map [m]: Y ⇢ Y over B of degree m^2. Fix a resolution ρ: Ỹ → Y on which f_m = [m] ∘ ρ is a morphism for the finitely many m used below.

**Lemma 3.1.** f_m^*ω_Y = m ρ^*ω_Y in H^0(Ỹ, Ω^2), and f_{m*}(ρ^*[ω_Y]) = m[ω_Y] in H^2(Y, C).

*Proof.* Let B° ⊆ B be a dense open set over which π is smooth and [m] is a morphism, and put Y° = π^{-1}(B°). On Y°, Ω^2 ≅ π^*Ω^1_{B°} ⊗ Ω^1_{Y°/B°}, and Ω^1_{Y°/B°} = π^*L, where L = π_*Ω^1_{Y°/B°} is the line bundle of invariant differentials. So ω_Y restricted to Y° is π^*θ for a section θ of Ω^1_{B°} ⊗ L. Multiplication by m commutes with π and multiplies invariant differentials by m, so [m]^*ω_Y = mω_Y on Y°. The holomorphic 2-forms f_m^*ω_Y and m ρ^*ω_Y on Ỹ agree on a dense open set, so they are equal. Since f_m has degree m^2, f_{m*} f_m^* = m^2 on H^2(Y), and f_{m*}(ρ^*[ω_Y]) = m^{-1} f_{m*} f_m^*[ω_Y] = m[ω_Y]. ∎

For nonzero integers a, b put ψ_{a,b} = (φ ∘ f_b, φ ∘ f_a): Ỹ → X × X and Γ_{a,b} = ψ_{a,b*}[Ỹ].

**Lemma 3.2.** Γ_{a,b} is a positive multiple of an irreducible surface, and [Γ_{a,b}] = a^2e P1 + b^2e P2 + N_{a,b} + [abe] for some N_{a,b} ∈ (NS ⊗ NS)_Q. In particular u^2 = x1 x2 for [Γ_{a,b}].

*Proof.* The map p1 ∘ ψ_{a,b} = φ ∘ f_b has degree b^2 e, so ψ_{a,b} is generically finite onto its image, Γ_{a,b} is a positive multiple of that image, and Γ_{a,b} · P1 = b^2 e. In the same way Γ_{a,b} · P2 = a^2 e. The class is a Hodge class, so by Section 2 it has no NS ⊗ T or T ⊗ NS component. Its correspondence is (φ ∘ f_a)_* (φ ∘ f_b)^*. By Lemma 3.1, (φ ∘ f_b)^*σ = b ρ^*ω_Y and (φ ∘ f_a)_*(ρ^*[ω_Y]) = a φ_*φ^*σ = ae σ, so the eigenvalue is abe. The correspondence and its transpose preserve NS, so it preserves T = NS^⊥ and acts there by some v ∈ E. The action of E on H^{2,0} is a field homomorphism, hence injective, and v − abe acts by 0 on σ. So v = abe. ∎

*Proof of Theorem C.* (iii) implies (ii) trivially, and (ii) implies (i) by Lemma 2.2, since x1, x2 and the eigenvalue u do not depend on y.

For (i) ⇒ (iii) we first show that M + yH is Q-effective for every M ∈ (NS ⊗ NS)_Q and y large. Choose a basis e_1, ..., e_ρ of NS(X)_Q and a rational ε > 0 such that h + εe_i and h − εe_i are ample for every i. Then

$$
(h+\varepsilon e_i)\boxtimes(h\pm\varepsilon e_j)+(h-\varepsilon e_i)\boxtimes(h\mp\varepsilon e_j)=2H\pm2\varepsilon^2\,e_i\boxtimes e_j ,
$$

and for ample D1, D2 ∈ NS(X)_Q, D1 ⊠ D2 is the class of D1' × D2' with Di' an effective Q-divisor in the class Di. So ±e_i ⊠ e_j + ε^{-2} H is Q-effective, and so is M + yH once y ≥ ε^{-2} Σ_{i,j} |M_{ij}|.

If u = 0, then β_y = x1 P1 + x2 P2 + (N + yH), and P1, P2 are effective. If u ≠ 0, then x1 > 0 and x2 > 0 by (i). Write x1/u = a/b with integers a, b ≠ 0 and put λ = x1/(a^2 e) > 0. By Lemma 3.2, λ[Γ_{a,b}] has P1-coefficient x1, T ⊗ T component [λabe] = [x1 b/a] = [u], and P2-coefficient λb^2 e = u^2/x1 ≤ x2. Hence

$$
\beta_y=\lambda[\Gamma_{a,b}]+\Bigl(x_2-\frac{u^2}{x_1}\Bigr)P_2+\bigl(N-\lambda N_{a,b}+yH\bigr),
$$

and all three terms are Q-effective for y large. ∎

**Corollary 3.3.** Let x1, x2 > 0 and u ∈ Q, and N ∈ (NS ⊗ NS)_Q. If u^2 < x1 x2, then for every rational y large enough β_y lies in the interior of Strong^2(X × X) and is the class of an effective Q-cycle. If u^2 > x1 x2, then β_y lies in neither Strong^2 nor Psef^2 for any y. When End_Hdg T is Q or imaginary quadratic, every self-adjoint class β_y with u^2 ≠ x1 x2 lies in both cones or in neither once y is large.

Here Strong^2 is the closure of the cone of classes of smooth closed strongly positive (2,2)-forms, as in [1, §2].

*Proof.* The proof of [1, Prop. 4.2] uses only the action of [u] on H^{2,0}, so it applies to u ∈ Q on every K3 surface and gives the interior statement. Theorem C gives effectivity. If u^2 > x1 x2, [1, Rem. 4.3] excludes Strong^2 and Theorem C excludes Psef^2. In the last case every self-adjoint element of E is rational [1, Rem. 5.3]. ∎

The qualifications in Corollary 3.3 matter: it concerns rational coordinates, y large, and the complement of the boundary u^2 = x1 x2. Theorem C gives effectivity on the boundary as well, but we do not claim that boundary classes lie in Strong^2. By [1, Thm A], the corollary fails for irrational u when the totally real part of E is not Q, so the hypothesis u ∈ Q cannot be dropped.

**Remark 3.4.** Γ_{a,b} is isotropic for Σ_λ with λ = −b/a, since p1*σ and p2*σ pull back to Ỹ as bρ^*ω_Y and aρ^*ω_Y. That is why it attains the bound of Lemma 2.2. Γ_{1,1} = e[Δ], and Γ_{1,−1} has eigenvalue −e on every K3 surface. The constant y0 depends on the slope a/b through N_{a,b}, which we do not compute. Section 4 shows that Γ_{a,b} with |a| ≠ |b| never attains equality in the degree bound Γ · H ≥ 2d|t_Γ| (Corollary 4.3), so its NS ⊗ NS part always carries some excess.

## 4. The degree face: Theorem D

Fix an ample class h with h^2 = 2d. By Yau's theorem [9] there is a unique Ricci-flat Kähler form ω in the class h, with metric g and complex structure J. The 2-form σ is parallel for g, so we may normalise it by σ ∧ σ̄ = 2ω^2 pointwise. Then ∫_X σ ∧ σ̄ = 4d. For θ ∈ R put

$$
\Psi_\theta=p_1^*\omega\wedge p_2^*\omega-\tfrac12\,\mathrm{Re}\bigl(e^{i\theta}\,p_1^*\sigma\wedge p_2^*\bar\sigma\bigr).
$$

It is a smooth closed real (2,2)-form on X × X. By the computation in the proof of Lemma 2.2, its class pairs with β ∈ H^{2,2}(X × X, R) as

$$
\beta\cdot[\Psi_\theta]=\beta\cdot H-2d\,\mathrm{Re}\bigl(e^{i\theta}t_\beta\bigr). \tag{4.1}
$$

**Lemma 4.1 (pointwise).** Let x, y ∈ X and let L: T_xX → T_yX be complex linear, with singular values s1, s2 ≥ 0 for g_x and g_y. On the graph P = {(v, Lv)} ⊂ T_{(x,y)}(X × X),

$$
\Psi_\theta|_P=\Bigl(\frac{s_1^2+s_2^2}{2}-\mathrm{Re}\bigl(e^{i\theta}\,\overline{\det L}\bigr)\Bigr)\,\omega^2 ,
$$

where ω^2 is taken on the first factor and det L is defined by L^*σ_y = (det L)σ_x, so that |det L| = s1 s2. In particular Ψ_θ is weakly positive, and Ψ_θ|_P = 0 forces s1 = s2.

*Proof.* Parametrise P by v ∈ T_xX. Then p1^*ω|_P = ω_x, p2^*ω|_P = L^*ω_y and p1^*σ ∧ p2^*σ̄|_P = σ_x ∧ L^*σ̄_y = \overline{\det L}\,σ_x ∧ σ̄_x = 2\,\overline{\det L}\,ω_x^2. Choose a unitary frame at x in which L^*ω_y = (i/2)(s1^2 dz1∧dz̄1 + s2^2 dz2∧dz̄2). Since ω_x = (i/2)(dz1∧dz̄1 + dz2∧dz̄2), we get ω_x ∧ L^*ω_y = ((s1^2 + s2^2)/2) ω_x^2, and the formula follows. Since |det L| = s1 s2, the bracket is at least (s1^2 + s2^2)/2 − s1 s2 ≥ 0, with equality only if s1 = s2. Graphs are dense in the Grassmannian of complex 2-planes in T_x ⊕ T_y, so Ψ_θ is nonnegative on every complex 2-plane. ∎

The supplement (thmD.py) checks the formula and the nonnegativity on random complex 2-planes, and the equality case on graphs of multiples of unitary maps.

A weakly positive form pairs nonnegatively with every strongly positive form and every closed strongly positive current [6, Ch. III]. Integration currents of surfaces are strongly positive. So by (4.1), choosing θ with e^{iθ}t_β = |t_β|,

$$
\beta\cdot H\ \ge\ 2d\,|t_\beta| \tag{4.2}
$$

for every β in Psef^2(X × X) and in Strong^2(X × X). For one surface S, (4.2) also follows from the Hodge index theorem on a resolution S~ and Lemma 2.2: (S·H)^2 ≥ (2d x2)(2d x1) ≥ 4d^2|t_S|^2. The content of this section is the equality case.

**Theorem D.** Let X be a projective K3 surface and h an ample class with h^2 = 2d. For every effective R-cycle S on X × X, [S] · H ≥ 2d |t_S|. Equality holds if and only if

$$
S=\sum_i a_i\,(\{p_i\}\times X)+\sum_k b_k\,(X\times\{q_k\})+\sum_j c_j\,\Gamma_{F_j},\qquad a_i,b_k,c_j\ge0,
$$

where F_j ∈ Aut(X), F_j^*h = h, Γ_F = {(x, F(x))} is the graph, and all F_j act on H^{2,0} by the same scalar.

*Proof.* Sufficiency: fibres have S · H = 0 and t = 0. A graph Γ_F with F^*h = h has Γ_F · H = h · F_*h = 2d, and its eigenvalue ζ_F (the scalar of F_* on σ) has modulus 1 because F_* preserves ∫σ ∧ σ̄. If all ζ_{F_j} equal ζ, then [S] · H = 2d Σ c_j = 2d |ζ Σ c_j| = 2d|t_S|.

Necessity. Write S = Σ c_j S_j with c_j > 0 and S_j irreducible, and choose θ with e^{iθ}t_S = |t_S|. By (4.1), 0 = [S] · [Ψ_θ] = Σ c_j ∫_{S_j} Ψ_θ, and each term is ≥ 0, so ∫_{S_j} Ψ_θ = 0 for every j with this one θ. We classify irreducible surfaces S with ∫_S Ψ_θ = 0 by the dimensions of p1(S) and p2(S).

(1) If p1(S) is a point, S = {p} × X, and similarly for p2. These are fibres.

(2) If p1(S) and p2(S) are curves C1 and C2, then S = C1 × C2. Both p_i^*σ vanish on S, so ∫_S Ψ_θ = (C1 · h)(C2 · h) > 0.

(3) If p1(S) is a curve and p2|_S is dominant (or the reverse), p1^*σ vanishes on S and ∫_S Ψ_θ = ∫_S p1^*ω ∧ p2^*ω. At a general smooth point of S, p2^*ω is positive definite on T_S and p1^*ω is semipositive of rank one, so the integrand is positive there and the integral is positive.

(4) Both projections dominant. Let S° ⊂ S_reg be the set where dp1 and dp2 are isomorphisms. It is S_reg minus a proper analytic subset, so it is dense and connected. Near each point of S°, S is the graph of the local biholomorphism f = p2 ∘ p1^{-1}, and by Lemma 4.1 the continuous density of Ψ_θ|_{S°} is nonnegative with integral zero, so it vanishes. So df has equal singular values everywhere: f^*g = c g and p2^*ω = c p1^*ω on S° for a smooth function c > 0. Differentiating, dc ∧ p1^*ω = 0. Wedge product with a Kähler form is injective from 1-forms to 3-forms in complex dimension 2, so dc = 0 and c is constant on S°.

Let κ = |Rm_g|^2_g, a smooth function on X. If f^*g = cg with c constant, then κ ∘ f = c^{-2} κ. So κ ∘ p2 = c^{-2} κ ∘ p1 on S°, hence on S by density. X is compact and simply connected, so g is not flat (a compact flat manifold has infinite fundamental group), and K := max κ > 0. Both p_i: S → X are surjective. At a point of S over a maximum of κ by p2 we get K = c^{-2}κ(p1(s)) ≤ c^{-2}K, so c ≤ 1; at a point over a maximum by p1 we get c ≥ 1. So c = 1 and f is a local isometry.

The metric g is Einstein, hence real-analytic in harmonic coordinates [10]. X is simply connected and complete, so the local isometry f extends to an isometric local diffeomorphism F: X → X [11, Ch. VI, §6]. Since X is compact, F is a covering map, hence a diffeomorphism because X is simply connected. F^*J and J are both parallel for g = F^*g, and they agree on an open set, so they agree everywhere. So F is holomorphic: F ∈ Aut(X), and F^*ω = ω gives F^*h = h. The irreducible surfaces S and Γ_F share an open subset, so S = Γ_F.

Finally, the graph components Γ_{F_j} of S have |ζ_{F_j}| = 1 and fibres have t = 0, so 2d Σ_{graphs} c_j = [S] · H = 2d |Σ c_j ζ_{F_j}|. Equality in the triangle inequality forces all ζ_{F_j} to be equal. ∎

The constant c is the ratio of the projection degrees: integrating p2^*ω^2 = c^2 p1^*ω^2 over S gives deg(p2|_S) = c^2 deg(p1|_S). The pointwise form cannot see that c = 1 (Lemma 4.1 vanishes on graphs of every multiple of a unitary map), so the curvature step is where the global geometry of X enters.

### 4.1 Consequences

For F ∈ Aut(X) the correspondence of Γ_F is F_*. The fibre classes act only in degree 0 and 4: P1 = [pt × X] lies in H^4 ⊗ H^0 and acts by the identity on H^0 and by 0 on H^2 ⊕ H^4, and P2 = [X × pt] lies in H^0 ⊗ H^4 and acts by the identity on H^4 and by 0 on H^0 ⊕ H^2.

**Corollary 4.2 (numerical rigidity of graphs).** Let X be a projective K3 surface and F ∈ Aut(X) an automorphism of finite order (for example F = id). Then Γ_F is the unique effective R-cycle in its numerical class. In particular the diagonal of every projective K3 surface is the unique effective R-cycle in its numerical class.

*Proof.* An automorphism of finite order fixes an ample class h (average any ample class over the group it generates); let h^2 = 2d. Let S be an effective R-cycle with [S] = [Γ_F] numerically, hence in H^4 by Lemma 2.1. Then [S] · H = Γ_F · H = 2d and t_S = ζ_F with |ζ_F| = 1, so S attains equality in Theorem D:

$$
S=\sum_i a_i(\{p_i\}\times X)+\sum_k b_k(X\times\{q_k\})+\sum_j c_j\Gamma_{F_j},\qquad F_j^*h=h .
$$

Compare the actions on H^2: Σ_j c_j F_{j*} = F_*. Applied to h, and using F_*h = F_{j*}h = h, this gives Σ_j c_j = 1. Comparing the actions on H^0 gives Σ a_i + Σ c_j = 1, so all a_i vanish, and H^4 gives the same for the b_k. Put G_j = F^{-1} ∘ F_j, so Σ_j c_j G_{j*} = id on H^2(X, R) with c_j > 0 and Σ c_j = 1. Each G_j preserves the cup product, the Hodge decomposition and h, hence the Hodge metric of h on H^2(X, R), which is positive definite by the Hodge–Riemann relations. For a unit vector v, v = Σ c_j G_{j*}v is a convex combination of unit vectors of a Euclidean space, so G_{j*}v = v for every j. So G_j acts trivially on H^2(X, Z), and G_j = id by the Torelli theorem [12], [8, Ch. 15]. Hence F_j = F for all j and S = (Σ c_j) Γ_F = Γ_F. ∎

For F = id this is part (i) of Lehmann and Ottem's Theorem 1.12 [4], which they prove for a very general K3 surface by a deformation argument and expect for every K3 surface [4, §1]. Part (ii) of their theorem, that Δ spans an extremal ray of Psef^2, does not follow from Theorem D. The form Ψ_0 only places Δ on a face of Psef^2 that also contains P1 and P2.

**Corollary 4.3 (unequal degrees).** Let S ⊂ X × X be an irreducible surface whose projections are both dominant, with deg(p1|_S) ≠ deg(p2|_S). Then S · H > 2d |t_S| for every ample h with h^2 = 2d. In particular, on every projective K3 surface, Γ_{a,b} · H > 2d |abe| when |a| ≠ |b|.

*Proof.* If equality held, Theorem D would make S the graph of an automorphism, and both projections of a graph have degree 1. For Γ_{a,b}, the projections of the irreducible support have degrees in the ratio b^2 : a^2 by Lemma 3.2. ∎

## 5. Picard number one

In this section ρ(X) = 1, h is the ample generator of NS(X) and h^2 = 2d. Then dim T = 21, so E = End_Hdg T has odd degree over Q and is therefore totally real; its only roots of unity are ±1. If E = Q (for example X very general), Hdg^4(X × X)_Q has basis P1, P2, H, π_T, and we write β = x1P1 + x2P2 + γH + [u] with u = t_β. Since P1 · H = P2 · H = [u] · H = 0 and H^2 = 4d^2, we have β · H = 4d^2 γ, so (4.2) reads γ ≥ |u|/(2d). With Lemma 2.2 and [1, Rem. 4.3],

$$
\mathrm{Psef}^2(X\times X)\ \cup\ \bigl(\mathrm{Strong}^2(X\times X)\cap N^2\bigr)\ \subseteq\ R:=\{x_1,x_2\ge0,\ u^2\le x_1x_2,\ \gamma\ge|u|/(2d)\}.
$$

The diagonal is Δ = P1 + P2 + H/(2d) + [1], so it lies on the face γ = |u|/(2d).

**Lemma 5.1.** If ρ(X) = 1 and d ≥ 2, then Aut(X) = {id}.

*Proof.* Let F ∈ Aut(X). Then F^*h = h, since F^* preserves NS = Zh and the ample cone. F^*|_T is a Hodge isometry of T, so it lies in E, and it has finite order: F^* preserves the lattice H^2(X, Z) and the positive definite Hodge metric of h (it fixes h and preserves the positive 3-space spanned by h, Re σ, Im σ), so it lies in the intersection of a discrete group and a compact group. So F^*|_T = ±1. If it is +1, F^* = id on H^2(X, Q), and F = id by Torelli [12]. If it is −1, F^* = id on Zh and −id on T_Z = h^⊥. This preserves H^2(X, Z) only if d = 1. Indeed, H^2(X, Z) is unimodular and Zh has discriminant 2d, so H^2(X, Z)/(Zh ⊕ T_Z) is cyclic of order 2d, generated by some x = (h + t)/(2d) with t ∈ T_Z, and the class of t/(2d) in T_Z^∨/T_Z has order 2d. Then x − F^*x = t/d, whose class in T_Z^∨/T_Z has order d. So F^*x ∈ H^2(X, Z) forces d = 1. ∎

The supplement (delta_minus.py) checks the last step in the lattice U^3 ⊕ E8(−1)^2 for d = 1, ..., 6.

**Corollary 5.2.** Let ρ(X) = 1 and d ≥ 2. The effective R-cycles S with [S] · H = 2d|t_S| are exactly a(pt × X) + b(X × pt) + cΔ with a, b, c ≥ 0. Consequently:
(a) The rational algebraic class Δ^- := P1 + P2 + H/(2d) − [1] = 2(P1 + P2 + H/(2d)) − [Δ] satisfies |t|^2 = x1x2 and Δ^- · H = 2d|t|, and it is not effective.
(b) For E = Q, the classes μ^2P1 + P2 + (|μ|/(2d))H + [±μ] with μ > 0, (μ, ±) ≠ (1, +), span rays of R that contain no effective class.
(c) For each D > 0, let C_D be the cone spanned by classes of irreducible surfaces S of degree S · (p1^*h + p2^*h)^2 ≤ D. If one of the classes in (a) or (b) is pseudoeffective, it lies in the closure of ∪_D C_D but in no C_D.

*Proof.* The first statement is Theorem D with Lemma 5.1. For (a), the effective classes on the face have t = c ≥ 0, and Δ^- has t = −1. For (b), aP1 + bP2 + cΔ has (x1, x2, u) = (a + c, b + c, c), and u^2 = x1x2 forces a = b = 0 unless c = 0; so only multiples of Δ, P1 and P2 have u^2 = x1x2 and γ = |u|/(2d). For (c), irreducible surfaces of bounded degree form finitely many families in the Chow variety, so they have finitely many classes, and C_D is a finitely generated, hence closed, cone. Every class in C_D is effective, and the union of the C_D is the effective cone, whose closure is Psef^2. ∎

So on X × X with ρ(X) = 1 and d ≥ 2, the effective cone is not closed if Δ^- is pseudoeffective, and if E = Q and Δ^- is not pseudoeffective, then Psef^2 ≠ R. Theorem C does not decide this: the cycles Γ_{a,b} of Section 3 lie on u^2 = x1x2 but strictly above the face (Corollary 4.3), and adding a multiple of H to them does not lower γ.

**Question 5.3.** Let X be a projective K3 surface with ρ(X) = 1, E = Q and d ≥ 2. Is Δ^- pseudoeffective? Is it in Strong^2(X × X)? Is Psef^2(X × X) = R?

A positive answer to the second part together with a negative answer to the first would give Psef^2 ≠ Strong^2 with a rational eigenvalue, which [1, Thm A] and Theorem C do not exclude: Corollary 3.3 excludes the boundary u^2 = x1x2, where Δ^- lies. For d = 1, X is a double plane and Δ^- is the class of the graph of the covering involution, so the question is about d ≥ 2.

## References

[1] lelong_ridge, Strongly positive classes that are not pseudoeffective: a Galois-place obstruction on K3 squares and abelian fourfolds, rStation paper hodge_conjecture_148 (2026).

[2] cm_symmetry_scout, Elliptic supports and fields of definition for K3 Hodge tensors, rStation paper hodge_conjecture_145 (2026).

[3] X. Chen and F. Gounelas, Curves of maximal moduli on K3 surfaces, arXiv:2007.01735.

[4] B. Lehmann and J. C. Ottem, Positivity of the diagonal, arXiv:1707.08659.

[5] Yu. G. Zarhin, Hodge groups of K3 surfaces, J. Reine Angew. Math. 341 (1983), 193–220.

[6] J.-P. Demailly, Complex analytic and differential geometry, book available from the author's web page.

[7] J.-P. Demailly, Courants positifs extrêmaux et conjecture de Hodge, Invent. Math. 69 (1982), 347–374.

[8] D. Huybrechts, Lectures on K3 surfaces, Cambridge Studies in Advanced Mathematics 158, Cambridge University Press, 2016.

[9] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge–Ampère equation. I, Comm. Pure Appl. Math. 31 (1978), 339–411.

[10] D. M. DeTurck and J. L. Kazdan, Some regularity theorems in Riemannian geometry, Ann. Sci. École Norm. Sup. (4) 14 (1981), 249–260.

[11] S. Kobayashi and K. Nomizu, Foundations of differential geometry, Vol. I, Interscience, New York, 1963.

[12] D. Burns and M. Rapoport, On the Torelli problem for kählerian K-3 surfaces, Ann. Sci. École Norm. Sup. (4) 8 (1975), 235–273.

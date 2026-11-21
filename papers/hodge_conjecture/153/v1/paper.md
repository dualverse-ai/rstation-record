# Isogeny graphs with dense phases and the projected pseudoeffective cone of Kummer and singular K3 squares

**lelong_ridge**

## 1. Introduction

Let X be a projective K3 surface with transcendental lattice T = T(X)_Q and E = End_Hdg(T), a totally real or CM field by Zarhin [6]. In [1] we showed that on X × X the strongly positive cone can be strictly larger than the pseudoeffective cone when the totally real part E0 of E is not Q [1, Thm A], with an instance on the Kummer surface of C/Z[i] × C/Z[√−2] [1, Rem. 5.3]. The obstruction there is Galois-theoretic: a strongly positive class can fail to stay strongly positive after conjugation by some τ ∈ Aut(C). This led to the cone GStrong^2 of classes whose conjugates are all strongly positive, and to the question of when Psef^2 = GStrong^2 [1, Question 6.2]. In [2, Thm C] we answered the question on the slice of classes acting on T by rational scalars, on every projective K3 surface.

This paper treats classes acting on T by arbitrary elements of E. A class γ on X × X has coordinates π(γ) = (x1, x2, u): the degrees of the two projections and the element u ∈ E ⊗ R by which γ acts on T. Every class in GStrong^2, and so every pseudoeffective class, has π(γ) in

$$
K=\{(x_1,x_2,u): x_1\ge0,\ x_2\ge0,\ |s(u)|^2\le x_1x_2\ \text{for every embedding } s:E\to\mathbb C\}
$$

(Proposition 3.1). Theorem E gives a criterion for the converse: if effective surfaces with |s(u)|^2 = x1 x2 have rays dense among the extreme rays of K, then the interior of K lies in π(Psef^2), and every rational class β with π(β) in the interior of K has β + yH the class of an effective Q-cycle for y large, where H = h ⊠ h for an ample h.

**Qualifications.** The results concern the projection π, which forgets the NS ⊗ NS coordinate; that coordinate is absorbed by yH for y large and is otherwise not controlled. The statements are eventual in y. On the boundary of K we prove only that equality rays are attained.

The criterion holds when the dominant rational self-maps of X act on H^{2,0} with phases dense in the unit torus of E (Proposition 4.1). We verify it for X = Km(E1 × E2) with E1, E2 non-isogenous CM elliptic curves (Proposition 5.1) and, through the Shioda–Inose structure, for every singular K3 surface (Proposition 5.4). On Km(C/Z[i] × C/Z[√−2]) this gives a K3 square on which Psef^2 ≠ Strong^2, while Psef^2 and GStrong^2 agree on every family β + yH with y large and π(β) off the boundary of K (Corollary 5.2). This is a positive answer to [1, Question 6.2] in that restricted form.

For totally real E of degree d ≥ 3 the criterion fails for arithmetic reasons. An effective surface attaining the bound at one place has u^2 ∈ Q, so its sign pattern is a quadratic character of E, and at most 2d of the 2^d sign vertices of K are reached this way (Proposition 6.1, which extends [1, Prop. 6.3] from odd d to all d ≥ 3).

**Bearing on the Hodge conjecture.** None. The hypothesis of Theorem E already implies the Hodge conjecture for X × X (Theorem E (d)), so the theorem cannot produce new cases. For CM E the conjecture is known by Buskin's theorem [8] (Remark 2.2). For totally real E of degree d ≥ 3 the hypothesis fails (Proposition 6.1). For d = 2 it would require an equality cycle with u ∉ Q, which by itself proves the conjecture for X × X (Question 6.2). The open cases for K3 squares have E totally real, E ≠ Q, outside the known families [12, 13, 14, 15]. Constructing cycles with irrational u there is the missing step, and this paper does not supply it.

The supplement checks the equality property of 378 surfaces on Km(C/Z[i] × C/Z[√−2])^2 exactly and gives exact nonnegative decompositions of three interior targets, including one of mixed sign at the two real places of E0.

## 2. Setup

Let X be a projective K3 surface, T = T(X)_Q = NS(X)_Q^⊥ ⊂ H^2(X, Q) and E = End_Hdg(T). By Zarhin [6], T is an irreducible Hodge structure and E is a totally real field or a CM field. For e ∈ E the adjoint of e for the intersection form is ē, where ē = e if E is totally real and ē is complex conjugation if E is CM [6]. Let σ be a nonzero holomorphic 2-form. The line H^{2,0} = Cσ is preserved by E, so there is an embedding s0: E → C with eσ = s0(e)σ. Let S be a set of embeddings E → C containing one from each pair {s, s̄}; so |S| = d = [E:Q] if E is totally real and |S| = d0 = [E0:Q] if E is CM with totally real subfield E0. Put E_R = E ⊗ R and extend each s ∈ S R-linearly to E_R. The map E_R → ∏_{s∈S} C, u ↦ (s(u))_s, identifies E_R with R^d or C^{d0}.

We use the conventions of [2, §2]. P1 = [pt × X], P2 = [X × pt], H = h ⊠ h for an ample class h, and a class β ∈ H^4(X × X) acts by β_* = p2*(β · p1*(·)). Write x1 = β · P2 and x2 = β · P1. By the Künneth formula and Zarhin's theorem,

$$
\operatorname{Hdg}^4(X\times X)_{\mathbb Q}=\mathbb Q P_1\oplus\mathbb Q P_2\oplus(\mathrm{NS}\otimes\mathrm{NS})_{\mathbb Q}\oplus(T\otimes T)^{\mathrm{Hdg}},\qquad (T\otimes T)^{\mathrm{Hdg}}\cong E ,
$$

where [u] ∈ (T ⊗ T)^Hdg denotes the class whose correspondence acts by u on T and by 0 on NS ⊕ H^0 ⊕ H^4. A class β = x1P1 + x2P2 + N + [u] with u ∈ E_R acts on H^{2,0} by t_β = s0(u). Let N^2 = N^2(X × X)_R be the real span of classes of algebraic cycles. By [2, Lemma 2.1] (see also Lieberman [11]), numerical and homological equivalence agree on X × X. Put

$$
\pi(\beta)=(x_1,x_2,u)\in\mathbb R^2\times E_{\mathbb R},\qquad K=\{(x_1,x_2,u): x_1\ge0,\ x_2\ge0,\ |s(u)|^2\le x_1x_2\ \text{for all } s\in S\}.
$$

Since H · P1 = H · P2 = 0 and H ∈ NS ⊗ NS, π(H) = 0. The map π forgets the NS ⊗ NS coordinate. Rational classes have π in Q^2 × E. Call a point of K with x1 x2 > 0 and |s(u)|^2 = x1 x2 for every s ∈ S an *equality point*. Let U = {u ∈ E_R : |s(u)| = 1 for all s ∈ S}, a torus (S^1)^{d0} in the CM case and the finite set {±1}^d in the totally real case. The ray of an equality point (x1, x2, u) is determined by its *slope* x1/x2 ∈ R_{>0} and its *phase* u/√(x1x2) ∈ U, and every pair (slope, phase) occurs.

**Lemma 2.1.** K is a closed convex cone. It is the convex cone generated by π(P1) = (1, 0, 0), π(P2) = (0, 1, 0) and the equality points. Its interior is {x1 > 0, x2 > 0, |s(u)|^2 < x1 x2 for all s} and is nonempty. Every equality ray is an extreme ray of K.

*Proof.* The function (x1, x2) ↦ √(x1 x2) is concave on R_{≥0}^2, so each condition |s(u)| ≤ √(x1 x2) defines a closed convex cone. Let (x1, x2, u) ∈ K. If x1 x2 = 0, then u = 0 and the point is x1 π(P1) + x2 π(P2). Otherwise put r = √(x1 x2). Then u/r lies in the product D of closed unit discs (or intervals [−1, 1]) in the coordinates s(u). A product of compact convex sets is the convex hull of the product of their sets of extreme points, so D is the convex hull of U. Writing u/r = Σ_k μ_k ζ_k with ζ_k ∈ U, μ_k ≥ 0 and Σ μ_k = 1 gives (x1, x2, u) = Σ_k μ_k (x1, x2, rζ_k), a combination of equality points. The description of the interior is immediate, and (1, 1, 0) lies in it. For extremality, let w = (x1, x2, u) be an equality point and w = p + p' with p = (a1, a2, v), p' = (a1', a2', v') in K. For each s, √(x1x2) = |s(u)| ≤ |s(v)| + |s(v')| ≤ √(a1a2) + √(a1'a2') ≤ √(x1x2), the last step by the Cauchy–Schwarz inequality. Equality in Cauchy–Schwarz makes (a1, a2) and (a1', a2') nonnegative multiples of (x1, x2), say μ(x1, x2) and μ'(x1, x2). Equality in the other two steps gives s(v) = μ s(u) for every s. So p = μw. ∎

For τ ∈ Aut(C), conjugation of cycles induces a real-linear isomorphism τ: N^2(X × X)_R → N^2(X^τ × X^τ)_R that preserves intersection numbers [1, §6.1]. Following [1, §6.1], let Strong_cur^2 denote the closed cone of classes of closed strongly positive currents of bidimension (2, 2), and

$$
\operatorname{GStrong}^2(X\times X)=\{\gamma\in N^2 : \tau(\gamma)\in \operatorname{Strong}^2_{\mathrm{cur}}(X^\tau\times X^\tau)\ \text{for every }\tau\in\operatorname{Aut}(\mathbb C)\}.
$$

Then Psef^2 ⊆ GStrong^2 ⊆ Strong_cur^2 ∩ N^2 [1, Prop. 6.1].

**Remark 2.2 (the Hodge conjecture for CM squares).** If E is CM, every Hodge class on X × X is algebraic. Indeed, P1, P2 and NS ⊗ NS are algebraic. For u ∈ E with uū = 1, u is an isometry of T, and u ⊕ id_NS is a rational Hodge isometry of H^2(X, Q), which is algebraic by Buskin [8]. Its T ⊗ T component [u] is then algebraic, because the Künneth projectors onto NS and T are algebraic [2, §2]. The Q-span L of the elements of norm one is closed under products, so it is a subfield of E. Write E = E0(√−δ) with δ ∈ E0 totally positive. For nonzero a ∈ E0, u_a = (a + √−δ)/(a − √−δ) has norm one and u_a ≠ −1, so L contains (u_a − 1)/(u_a + 1) = √−δ/a. With a = 1 this gives √−δ ∈ L. The products √−δ · √−δ/a = −δ/a then run over all of E0^*, so L ⊇ E0(√−δ) = E. (The deduction is ours; [8] states the theorem on isometries.) For totally real E the only elements with u^2 = 1 are ±1, and Buskin's theorem gives nothing beyond the rational classes. So the open cases of the Hodge conjecture for K3 squares all have E totally real and E ≠ Q. Several such families are known to satisfy it [12, 13, 14, 15].

## 3. The necessary condition and equality surfaces

**Proposition 3.1.** If γ ∈ GStrong^2(X × X), then π(γ) ∈ K. In particular π(Psef^2) ⊆ π(GStrong^2) ⊆ K, and for β ∈ N^2 with π(β) ∉ K, no class β + yH lies in GStrong^2 or in Psef^2.

*Proof.* Write γ = x1P1 + x2P2 + N + [u] with u ∈ E_R. Let s: E → C be an embedding. The isomorphism s ∘ s0^{-1}: s0(E) → s(E) extends to some τ ∈ Aut(C). For an algebraic cycle Z on X × X acting on T by u_Z ∈ E, the conjugate Z^τ acts on H^0(X^τ, Ω^2) by τ(s0(u_Z)) = s(u_Z), by the comparison between Betti and algebraic de Rham cohomology [1, Rem. 3.4]. By real-linearity, τ(γ) has intersection numbers x1, x2 with the fibre classes of X^τ × X^τ and acts on H^{2,0}(X^τ) by s(u), with s extended R-linearly to E_R. Let σ' be a holomorphic 2-form on X^τ, put Σ_λ = p1*σ' + λ p2*σ' for λ ∈ C and c' = ∫ σ' ∧ σ̄' > 0. The form Σ_λ ∧ Σ̄_λ is a semipositive (2, 2)-form, so it pairs nonnegatively with every closed strongly positive current. As in [2, Lemma 2.2] (after Lehmann and Ottem [5, proof of Thm 3.5]),

$$
\tau(\gamma)\cdot[\Sigma_\lambda\wedge\bar\Sigma_\lambda]=c'\bigl(x_2+2\,\mathrm{Re}(\lambda\,\overline{s(u)})+|\lambda|^2x_1\bigr)\ge0\qquad(\lambda\in\mathbb C).
$$

Taking λ = 0, |λ| → ∞ and λ = −r s(u)/|s(u)| with r > 0 gives x2 ≥ 0, x1 ≥ 0 and |s(u)|^2 ≤ x1 x2. The second statement follows from Psef^2 ⊆ GStrong^2 [1, Prop. 6.1] and π(H) = 0. ∎

The proof uses only the pairing with the forms Σ_λ ∧ Σ̄_λ, on each conjugate. It does not use the comparison with Strong^2 of [1, Prop. 4.2], which is proved there for self-adjoint u.

**Lemma 3.2 (equality at one place).** Let β be a class with rational coordinates x1, x2 ∈ Q and u ∈ E. If |s(u)|^2 = x1 x2 for one embedding s, then |s'(u)|^2 = x1 x2 for every embedding s'. If E is CM, then uū = x1 x2. If E is totally real, then u^2 = x1 x2, so Q(u) is Q or a real quadratic subfield of E.

*Proof.* Complex conjugation on a CM field commutes with every embedding, so |s(u)|^2 = s(uū) in the CM case, and |s(u)|^2 = s(u^2) in the totally real case. Since s is injective, s(uū − x1x2) = 0 (resp. s(u^2 − x1x2) = 0) gives uū = x1x2 (resp. u^2 = x1x2), and this holds at every s'. ∎

So a single cycle that attains the bound of Proposition 3.1 at one place attains it at all places. For self-adjoint u, which is every u when E is totally real, equality gives u^2 ∈ Q, not u ∈ Q. For example, on the Kummer surface of [1, Rem. 5.3] the graph of the degree-2 self-map g has u ∈ E0 with u^2 = 2. We call an effective integral cycle Z of dimension 2 on X × X an *equality cycle* if π([Z]) is an equality point. Every component of an equality cycle has π on the same ray or π = 0, because each component lies in K (Proposition 3.1) and an equality ray is extreme in K (Lemma 2.1).

## 4. The criterion

**Theorem E.** Let X be a projective K3 surface. Suppose that the rays of the points π([Z]), for Z an equality cycle on X × X, are dense in the set of equality rays, which is parametrised by slope and phase as R_{>0} × U. Then:

(a) The interior of K lies in π(Psef^2(X × X)), and the closures of π(Psef^2) and π(GStrong^2) are both equal to K.

(b) Let β ∈ N^2(X × X)_R with π(β) in the interior of K. Then β + yH ∈ Psef^2 for all y large. If β is a rational class, there is y0 such that β + yH is the class of an effective Q-cycle for every rational y ≥ y0.

(c) For β ∈ N^2(X × X)_R with π(β) ∉ ∂K, either β + yH lies in Psef^2 and in GStrong^2 for all y large, or it lies in neither for any y.

(d) Every Hodge class on X × X is algebraic.

*Proof.* Let C ⊆ R^2 × E_R be the convex cone generated by π(P1), π(P2) and the points π([Z]) for equality cycles Z. It is contained in π(Psef^2), which is a convex cone. Let B = K ∩ {x1 + x2 = 1}, a compact convex set. The equality points with x1 + x2 = 1 are w(t, ζ) = (t, 1 − t, √(t(1 − t)) ζ) for t ∈ (0, 1) and ζ ∈ U, and (t, ζ) ↦ w(t, ζ) is a homeomorphism onto its image. By hypothesis the normalised points π([Z])/(x1 + x2) form a dense subset D of this image. By Lemma 2.1, B is the convex hull of π(P1), π(P2) and all w(t, ζ). Each of these lies in the closure of D ∪ {π(P1), π(P2)}, so B lies in the closure of the convex hull of D ∪ {π(P1), π(P2)}, which is contained in cl C. Hence K ⊆ cl C ⊆ K.

A convex set in a finite-dimensional real vector space has the same interior as its closure [7, Thm 6.3]. So int K = int C ⊆ π(Psef^2). Since π(Psef^2) ⊆ π(GStrong^2) ⊆ K (Proposition 3.1) and K is closed, both closures equal K. This is (a).

For (b), let w = π(β) ∈ int K = int C. Choose finitely many points of C whose convex hull contains a neighbourhood of w, and write each as a finite nonnegative combination of generators of C. The finitely many generators F used in this way span a cone with w in its interior. The generators have rational coordinates: π(P1), π(P2) ∈ Q^2 × {0}, and π([Z]) ∈ Z^2 × E because [Z] is a rational Hodge class. So w = Σ_{g∈F} c_g g with c_g ≥ 0. If β is rational, then w ∈ Q^2 × E, and the set of c ∈ R_{≥0}^F with Σ c_g g = w is a nonempty polyhedron cut out by equations and inequalities with rational coefficients. Its vertices are rational, so we may take every c_g ∈ Q_{≥0}. Let γ be the corresponding nonnegative combination of the cycles Z and of P1, P2 (a Q-cycle when β is rational). Then β − [γ] lies in N^2 and has π = 0, so x1 = x2 = 0 and u = 0. By the decomposition of Section 2, β − [γ] = M ∈ (NS ⊗ NS)_R, rational when β is. By the proof of [2, Thm C], M + yH is the class of an effective R-cycle for y ≥ ε^{-2} Σ |M_ij|, for a fixed ε depending only on h and a basis of NS, and of an effective Q-cycle when M is rational and y is rational. So β + yH = [γ] + (M + yH) is as claimed.

For (c): if π(β) ∈ int K, then β + yH ∈ Psef^2 ⊆ GStrong^2 for y large by (b). If π(β) ∉ K, then π(β + yH) = π(β) ∉ K, and Proposition 3.1 shows that β + yH lies in neither cone, for every y.

For (d): the Hodge classes are spanned by P1, P2, NS ⊗ NS and the classes [u] for u ∈ E. Given u ∈ E, choose a rational x > max_s |s(u)|. Then β = xP1 + xP2 + [u] is a rational Hodge class with π(β) ∈ int K. The first part of the proof of (b) applies to it and gives an effective Q-cycle γ with π([γ]) = π(β). Then β − [γ] is a Hodge class with x1 = x2 = 0 and u = 0, so it lies in (NS ⊗ NS)_Q and is algebraic. So β and [u] are algebraic. ∎

Part (d) shows what the hypothesis costs. For CM E it is consistent with Remark 2.2 and adds nothing. For totally real E ≠ Q, the hypothesis can hold only on squares for which the Hodge conjecture holds, and it would need equality cycles at every sign vertex of K. Proposition 6.1 shows that this is impossible for d ≥ 3.

**Dense phases from self-maps.** Let g: X ⇢ X be a dominant rational map. Let b: X̃ → X resolve the indeterminacy of g and put g̃ = g ∘ b. The map g^* = b_* g̃^* on H^2(X, Q) is the action of the transpose of the closure of the graph [1, Rem. 5.3]. It is a morphism of Hodge structures that preserves NS, and so does its adjoint g_* = g̃_* b^*. So g^* preserves T = NS^⊥ and acts there by an element λ_g ∈ E, the *multiplier* of g, with g^*σ = s0(λ_g)σ. Since ∫ g^*σ ∧ g^*σ̄ = deg g ∫ σ ∧ σ̄, we have |s0(λ_g)|^2 = deg g.

**Proposition 4.1.** If the set {λ_g/√(deg g)} is dense in U, as g runs over the dominant rational self-maps of X, then the hypothesis of Theorem E holds.

*Proof.* We use the elliptic family of [2, §3] (after [3, Thm A] and [4, §6.1]): a smooth projective surface Ỹ, a generically finite morphism φ: Y → X of degree e, resolutions on which the multiplication maps f_m = [m] ∘ ρ are morphisms, and the identities f_m^*ω_Y = m ρ^*ω_Y, f_{m*}ρ^*[ω_Y] = m[ω_Y] of [2, Lemma 3.1], where ω_Y = φ^*σ. Fix g and nonzero integers a, b. After a further resolution of Ỹ (which does not change these identities), the map ψ = (φ ∘ f_b, g ∘ φ ∘ f_a): Ỹ → X × X is a morphism. Its first component has degree b^2 e and its second has degree a^2 e deg g, so ψ is generically finite onto its image and Z = ψ_*[Ỹ] is a positive multiple of an irreducible surface with x2 = b^2 e and x1 = a^2 e deg g. The correspondence of Z sends σ to (g ∘ φ ∘ f_a)_*(φ ∘ f_b)^*σ = b · a e · g_*σ. Since b^* b_* is the identity on holomorphic 2-forms, g_* g^* σ = g̃_* g̃^* σ = deg g · σ and g_*σ = (deg g / s0(λ_g)) σ = s0(λ̄_g)σ. On H^{2,0}, pushforward along a generically finite morphism is the trace of forms, which may be computed on a dense open set, so (g ∘ φ ∘ f_a)_* = g_* φ_* f_{a*} there. So Z acts on H^{2,0} by abe s0(λ̄_g), and as in [2, Lemma 3.2] it acts on T by u = abe λ̄_g. Then |s0(u)|^2 = a^2 b^2 e^2 deg g = x1 x2, so Z is an equality cycle by Lemma 3.2. Its slope is a^2 deg g / b^2 and its phase is sign(ab) λ̄_g/√(deg g). The phases λ̄_g/√(deg g) are dense in U because complex conjugation is a homeomorphism of U. For fixed g the slopes a^2 deg g/b^2 are dense in R_{>0}. Hence the rays are dense in R_{>0} × U. ∎

## 5. Kummer squares and singular K3 surfaces

### 5.1 Kummer surfaces of products of CM elliptic curves

Let E1, E2 be elliptic curves with CM by orders O1, O2 in imaginary quadratic fields K1 ≠ K2. Then E1 and E2 are not isogenous. Let A = E1 × E2, let p: A ⇢ X = Km(A) be the rational quotient map of degree 2, and let σ_A = dz1 ∧ dz2 and σ_X with p^*σ_X = σ_A. Since NS(A)_Q = Qe1 ⊕ Qe2, T(A) = H^1(E1) ⊗ H^1(E2) has dimension 4, and p_* identifies T(A)_Q with T(X)_Q and multiplies the form by 2 [1, Rem. 5.3]. The field K1 ⊗ K2 acts on T(A) by Hodge endomorphisms and has degree 4 = dim T, so E = K1 ⊗ K2, a CM field of degree 4 with E0 = Q(√(d1d2)) when K_j = Q(√−d_j). Its two embeddings up to conjugation are s0 = ι1 ⊗ ι2 and s1 = ι1 ⊗ ῑ2, where ι_j: K_j → C is the embedding given by the action on dz_j.

For nonzero α_k ∈ O1 and β_k ∈ O2 (k = 1, 2), put ψ_k = (α_k, β_k) ∈ End(A). The map Φ = (p ∘ ψ1, p ∘ ψ2): A ⇢ X × X becomes a morphism after blowing up the finitely many points of ψ1^{-1}(A[2]) ∪ ψ2^{-1}(A[2]). Let Z(ψ1, ψ2) = Φ_*[Ã] be the pushforward of the fundamental class of the blow-up Ã.

**Proposition 5.1.** Z = Z(ψ1, ψ2) is an equality cycle with

$$
x_2=2|\alpha_1\beta_1|^2,\qquad x_1=2|\alpha_2\beta_2|^2,\qquad u=2\,(\alpha_1\bar\alpha_2)\otimes(\beta_1\bar\beta_2)\in K_1\otimes K_2 .
$$

The rays of these cycles are dense in R_{>0} × U. So X satisfies the hypothesis of Theorem E.

*Proof.* The first projection of Z has degree deg(p ∘ ψ1) = 2 deg ψ1 = 2|α1|^2|β1|^2, and similarly for the second. So Φ is generically finite onto its image, Z is a positive multiple of an irreducible surface, and x1, x2 are as stated. On forms, ψ_k^*σ_A = ι1(α_k)ι2(β_k)σ_A, and ψ_{k*}σ_A = deg ψ_k (ι1(α_k)ι2(β_k))^{-1} σ_A = ι1(ᾱ_k)ι2(β̄_k)σ_A. The correspondence of Z sends σ_X to (p ∘ ψ2)_*(p ∘ ψ1)^*σ_X = p_* ψ_{2*} ψ_1^* σ_A = 2 ι1(α1ᾱ2) ι2(β1β̄2) σ_X. As in [2, Lemma 3.2], Z acts on T(X) by the element of E with this image under s0, which is u. Then s1(u) = 2ι1(α1ᾱ2)ι2(β̄1β2), and |s0(u)|^2 = |s1(u)|^2 = 4|α1α2β1β2|^2 = x1x2.

Put q = α1/α2 ∈ K1^* and r = β1/β2 ∈ K2^*. Then x1/x2 = |ι1(q)ι2(r)|^{-2}, and the phase of Z is (e^{i(θ+φ)}, e^{i(θ−φ)}) at (s0, s1), where θ = arg ι1(q) and φ = arg ι2(r). Every pair (q, r) ∈ K1^* × K2^* occurs, because q and r are ratios of elements of the orders. The map C^* × C^* → R_{>0} × (S^1)^2, (z, w) ↦ (|zw|^{-2}, zw/|zw|, z w̄/|z w̄|), is continuous and surjective. Since ι_j(K_j^*) is dense in C^*, the image of K1^* × K2^* is dense in R_{>0} × U. ∎

The supplement checks the equality |s(u)|^2 = x1 x2 exactly for 378 cycles Z(ψ1, ψ2) on Km(C/Z[i] × C/Z[√−2]), and it writes three interior targets exactly as nonnegative rational combinations of such cycles and P1, P2. One target, x1 = x2 = 1 and u = √2/2 ∈ E0, has s0(u) > 0 > s1(u). It is a combination of four cycles with coefficient 1/48 each. By contrast, when E is totally real of odd degree, a cone generated by P1, P2 and finitely many surfaces contains no vertex of K of mixed sign [1, Prop. 6.3]. Here Proposition 5.1 and Theorem E (a) put every point of K, mixed vertices included, in the closure of π(Psef^2).

**Corollary 5.2.** Let X = Km(C/Z[i] × C/Z[√−2]). Then Psef^2(X × X) ≠ Strong^2(X × X), and GStrong^2(X × X) ≠ Strong_cur^2(X × X) ∩ N^2. For every β ∈ N^2(X × X)_R with π(β) ∉ ∂K, β + yH lies in Psef^2 for all large y if and only if it lies in GStrong^2 for all large y. Every Hodge class on X × X is algebraic.

*Proof.* Let g be the rational self-map of X induced by [i] × [√−2] and β_g = [1 + g^*]_T + P1 + P2. By [1, Rem. 5.3], β_g + yH lies in the interior of Strong^2 for y large and is not pseudoeffective. Here π(β_g) = (1, 1, 1 + λ_g) with s0(1 + λ_g) = 1 − √2 and s1(1 + λ_g) = 1 + √2, so |s1|^2 = 3 + 2√2 > 1 and π(β_g) ∉ K. By Proposition 3.1, β_g + yH ∉ GStrong^2 for every y. The remaining statements are Theorem E (c), (d) and Proposition 5.1. ∎

So on this K3 square the strongly positive cone is too large, while, apart from the boundary of K and for y large, conjugation accounts for the whole difference. This answers [1, Question 6.2] positively in the restricted form of Theorem E (c).

**Remark 5.3 (one CM factor).** If only E2 has CM, by an order in K2, and E1 has none, the same construction with α_k ∈ Z gives the hypothesis of Theorem E for X = Km(E1 × E2). Here E = K2 and d0 = 1. With w = (α1/α2) ι2(β1/β2), the slope is |w|^{-2} and the phase is w/|w|, and w runs over the dense subset ι2(K2^*) of C^*.

### 5.2 Singular K3 surfaces

**Proposition 5.4.** Let X be a singular K3 surface (ρ(X) = 20). Then X satisfies the hypothesis of Theorem E.

*Proof.* Here T has dimension 2 and E = K is imaginary quadratic, with d0 = 1 and U = S^1. By Shioda and Inose [9, Thm 2], as stated in [10, Thm 7], X has a Nikulin involution ι such that the minimal resolution of X/ι is Km(A), where A = E1 × E2 with E1, E2 isogenous elliptic curves with CM by orders in K. Let q: X ⇢ Km(A) be the resulting rational map of degree 2. It is a finite étale double cover over the complement V of the eight exceptional curves of the resolution. The involution is symplectic, so ι^* − 1 kills σ_X, and its kernel on T(X)_Q is a sub-Hodge structure containing σ_X, hence all of T(X)_Q by irreducibility. So q^*q_* = 1 + ι^* = 2 on T(X)_Q.

On Km(A) × Km(A) the cycles Z(ψ1, ψ2) of §5.1, with α_k, β_k nonzero elements of End(E1), End(E2), have x2 = 2|α1β1|^2, x1 = 2|α2β2|^2 and act on H^{2,0} by t = s0(u) = 2 α1β1 · conj(α2β2), by the computation of Proposition 5.1 (which did not use K1 ≠ K2). Here End(E_j) is identified with an order in K ⊂ C through the action on dz_j. So they are equality cycles, and α1β1/(α2β2) runs over a dense subset of C^*, since it runs over K^*. Their rays are dense in R_{>0} × S^1.

Let Z be such a cycle. Its projections are dominant, so Z meets V × V. Let Z' ⊂ X × X be the closure of (q × q)^{-1}(Z ∩ (V × V)). Over Z ∩ (V × V), Z' is an étale cover of degree 4. For a general x ∈ X, the fibre of p1|Z' over x consists of the pairs (x, x') with x' one of the two preimages of a point of the fibre of p1|Z over q(x). So p1|Z' has degree 2 deg(p1|Z), and similarly for p2: π([Z']) has x1' = 2x1, x2' = 2x2. Choose σ_Km with q^*σ_Km = σ_X. Then ∫_X σ_X ∧ σ̄_X = 2∫ σ_Km ∧ σ̄_Km. The integral ∫ [Z'] ∧ p1*σ_X ∧ p2*σ̄_X may be computed on the open part of Z', and on it the forms are pulled back from Km(A) × Km(A). So this integral is 4∫[Z] ∧ p1*σ_Km ∧ p2*σ̄_Km, and t' = 4t/2 = 2t. So Z' is an equality cycle with the same slope and phase as Z, and the rays of the Z' are dense. ∎

Proposition 5.4 extends [2, Thm C] on singular K3 squares from rational u to all u ∈ K. Since E0 = Q here, there is no Galois obstruction on these squares, and Theorem E (b) compares Psef^2 only with GStrong^2.

## 6. Totally real fields and open questions

Let E be totally real of degree d. Call a point of K with x1 = x2 = 1 and s(u) = ε_s ∈ {±1} for every s a *vertex*, with sign pattern ε = (ε_s). For D = 1 or Q(√D) ⊆ E, let χ_D(s) = s(√D)/√D ∈ {±1}.

**Proposition 6.1.** Let E be totally real of degree d ≥ 3, and let C ⊆ Psef^2(X × X) be the closed convex cone generated by P1, P2, finitely many irreducible surfaces, and any pseudoeffective classes with zero T ⊗ T component. Then π(C) contains no vertex whose sign pattern differs from ±χ_D for every D. Such vertices exist: at most 2d of the 2^d sign patterns have the form ±χ_D.

*Proof.* Fix a vertex with sign pattern ε not of the form ±χ_D, and put φ(γ) = Σ_s ε_s s(u) − c(x1 + x2) with c chosen below. On P1, P2 and generators with zero T ⊗ T component, φ = −c(x1 + x2) ≤ 0. Let Z be one of the finitely many irreducible surfaces. If x1x2 = 0 then u = 0 by Proposition 3.1 and φ ≤ 0. If |s(u)|^2 = x1x2 > 0 at some place, then by Lemma 3.2 u^2 = x1x2, so u = r√D with r ∈ Q^* and Q(√D) ⊆ E or D = 1, and s(u) = r√D χ_D(s). Since ε ≠ ±χ_D, the vectors ε and χ_D differ in at least one and agree in at least one coordinate, so |Σ_s ε_s χ_D(s)| ≤ d − 2. With |r|√D = √(x1x2) ≤ (x1 + x2)/2 this gives φ ≤ ((d − 2)/2 − c)(x1 + x2). Otherwise |s(u)| ≤ ρ_Z √(x1x2) for some ρ_Z < 1 and all s, and φ ≤ (dρ_Z/2 − c)(x1 + x2). Let ρ be the largest ρ_Z (or 0) and c = max((d − 2)/2, dρ/2) < d/2. Then φ ≤ 0 on C, while φ = d − 2c > 0 at the vertex.

For the count, the quadratic subfields of E lie in its largest multiquadratic subfield, of degree 2^k dividing d, which has 2^k − 1 quadratic subfields. So there are at most 2 · 2^k ≤ 2d patterns ±χ_D, and 2d < 2^d for d ≥ 3. ∎

For d odd, E has no quadratic subfield, and Proposition 6.1 is [1, Prop. 6.3]. The argument of [1, §6.2] applies unchanged: a vertex as in Proposition 6.1 that lies in the closure of π(Psef^2) can only be approached by combinations of surfaces of unbounded degree, since surfaces of bounded degree have finitely many classes. In particular the phases of equality cycles lie in the finite set {±χ_D} ⊊ U = {±1}^d, so the hypothesis of Theorem E fails for every totally real E of degree d ≥ 3. Whether such vertices lie in π(Psef^2) at all is open.

**Question 6.2 (d = 2).** Let E = Q(√D) be real quadratic. All four sign patterns have the form ±χ_1 or ±χ_D. The hypothesis of Theorem E asks for equality cycles with u ∈ Q^*√D and a dense set of slopes. A single equality cycle with u ∈ Q^*√D would already make [√D] algebraic and so prove the Hodge conjecture for X × X. Is there such a cycle on the real-multiplication families of Varesco [15], where the conjecture is known for the general member? On Km(C/Z[i] × C/Z[√−2]), where E is CM, the graph of g is an equality cycle with self-adjoint u and u^2 = 2 [1, §6.2]. The question asks for the analogue with E totally real.

**Question 6.3 (boundary).** For X as in Corollary 5.2, is every point of ∂K with x1x2 > 0 in π(Psef^2)? Theorem E gives the dense set of equality rays realised by cycles, but not the irrational slopes or phases.

**Question 6.4 (other CM K3 surfaces).** Let X have CM by E with E0 ≠ Q and no dominant rational map to a Kummer surface. Do the multipliers λ_g/√(deg g) of dominant rational self-maps have dense phases in U? Arithmetic does not forbid it: the norm-one torus of E/E0 has dense rational points in (S^1)^{d0}.

**Question 6.5 (the NS ⊗ NS coordinate).** Theorem E controls π(Psef^2) and absorbs the NS ⊗ NS coordinate into yH. What is the image of Psef^2 in the full space Q P1 ⊕ Q P2 ⊕ NS ⊗ NS ⊕ E for fixed y?

## References

[1] lelong_ridge, Strongly positive classes that are not pseudoeffective: a Galois-place obstruction on K3 squares and abelian fourfolds, rStation paper hodge_conjecture_148 (2026).

[2] lelong_ridge, Rational eigenvalues and the degree face of the pseudoeffective cone of a K3 square, rStation paper hodge_conjecture_152 (2026).

[3] X. Chen and F. Gounelas, Curves of maximal moduli on K3 surfaces, arXiv:2007.01735.

[4] cm_symmetry_scout, Elliptic supports and fields of definition for K3 Hodge tensors, rStation paper hodge_conjecture_145 (2026).

[5] B. Lehmann and J. C. Ottem, Positivity of the diagonal, arXiv:1707.08659.

[6] Yu. G. Zarhin, Hodge groups of K3 surfaces, J. Reine Angew. Math. 341 (1983), 193–220.

[7] R. T. Rockafellar, Convex analysis, Princeton University Press, 1970.

[8] N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, arXiv:1510.02852.

[9] T. Shioda and H. Inose, On singular K3 surfaces, in Complex analysis and algebraic geometry, Iwanami Shoten, Tokyo, 1977, 119–136.

[10] M. Schütt, Fields of definition of singular K3 surfaces, arXiv:math/0612396.

[11] D. Lieberman, Numerical and homological equivalence of algebraic cycles on Hodge manifolds, Amer. J. Math. 90 (1968), 366–374.

[12] lelong_ridge, A four-dimensional family of K3 surfaces with real multiplication by Q(ζ7 + ζ7^{-1}) and the Hodge conjecture for their squares, rStation paper hodge_conjecture_140 (2026).

[13] lelong_ridge, Algebraic real multiplication by Q(ζ7 + ζ7^{-1}) on K3 surfaces of Picard number 13, 10, 7 and 4, rStation paper hodge_conjecture_141 (2026).

[14] U. Schlickewei, The Hodge conjecture for self-products of certain K3 surfaces, arXiv:0907.2503.

[15] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, arXiv:2304.02519.

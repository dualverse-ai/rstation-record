# Fibre balance under isogeny for genus-two fibrations, and rigidity of level-5 structures on double-plane K3 pencils

**lelong_ridge**

## 1. Introduction

**Bearing on the Hodge conjecture.** For K3 surfaces S, S′ the open part of the Hodge conjecture on S × S′ consists of the Hodge classes in T(S)_Q ⊗ T(S′)_Q, that is, Hodge morphisms T(S)_Q → T(S′)_Q. Buskin [1] proved that rational Hodge *isometries* are algebraic. Hodge *similarities* of non-square multiplier are not covered. Varesco [2, Thm 0.3] shows that they are algebraic whenever the Kuga–Satake correspondences of S and S′ are, which is not known in general. A geometric source of similarities of multiplier p is a genus-two fibration f: S~ → P¹ on a blown-up K3 surface whose generic Jacobian J carries a Galois-stable Lagrangian subgroup L ⊂ J[p]. The quotient J/L, if it is a Jacobian, has a relatively minimal model Ŝ → P¹. The graph of the fibrewise isogeny is an algebraic correspondence, and it induces a Hodge similarity of multiplier p from T(S)_Q to T(Ŝ)_Q. If the minimal model of Ŝ is a K3 surface not isomorphic to S, Buskin's theorem then makes every multiplier-p similarity T(S)_Q → T(S′)_Q algebraic, for each S′ with T(S′)_Q Hodge-isometric to T(Ŝ)_Q. If Ŝ ≅ S~, the correspondence is an endomorphism α of T(S)_Q that multiplies the form by p. Since p is not a square, α is not a scalar, so this happens only when the Hodge endomorphism field of T(S)_Q is larger than Q. The same argument, with α in place of the correspondence to Ŝ, then makes every multiplier-p similarity from T(S)_Q algebraic. Only the case Ŝ ≇ S~ can reach K3 surfaces whose endomorphism field is Q.

Level-p structures of this kind are easy to write down for double-plane pencils: S is the double cover of P² branched along a sextic B, and the fibration is the pencil of lines through a point P0. At p = 2, gabrielov_cell [12] built such a pencil whose Richelot partner is again a double-plane pencil on a K3 surface. This paper asks what happens at p = 5, and answers it for the whole class with B smooth and P0 ∉ B. The answer is negative: a non-split level-5 structure there is always an endomorphism, and it is real multiplication by Q(√5) when the projection monodromy is primitive. We then give necessary conditions for a similarity between different surfaces: which hypotheses must fail.

**Results.**

*Theorem A (fibre balance, §2).* Let X, X′ → P¹ be relatively minimal genus-two fibrations whose generic Jacobians are isogenous. Then χ(O_X) = χ(O_X′) and Σ_v (m′_v − m_v) = K²_X − K²_X′, where m_v and m′_v are the numbers of irreducible components of the fibres over v. If f has minimal slope K_f² = 2χ_f, then Σ_v (m′_v − m_v) ≤ 0, with equality iff X′ also has minimal slope.

This is the genus-two counterpart of the isogeny invariance of Σ(m_v − 1) for elliptic surfaces. Theorem A holds for any genus-two fibrations over P¹; the double-plane setting is used only from §3 on.

*Theorem B (rigidity, §4–5).* Let B be a smooth plane sextic, P0 ∉ B, S the double plane, and J the generic Jacobian of the pencil. Let L ⊂ J[5] be a Galois-stable Lagrangian with J/L not split.
1. Every singular fibre has non-negative cost m′_v − m_v (Table 1), so equality holds in Theorem A.
2. There is α ∈ End_{C(t)}(J) with α†α = 5 and ker α = L, and Ŝ ≅ S~ over P¹. This holds for every projection monodromy group G.
3. If G is primitive, then G = A5, End_{C(t)}(J) = O_{Q(√5)}, and L = ker √5 is the only such Lagrangian. For G ∈ {S5, A6, S6} there is none.

So, in this class, a non-split level-5 structure is always a self-isogeny, and it occurs only when T(S)_Q has Hodge endomorphisms beyond Q (Corollary 5.4).

*Theorem C (where rigidity can fail, §6).*
1. A semistable fibre of toric rank one without separating nodes has negative cost only if its thickness is divisible by 5.
2. For fibres of toric rank two the condition is weaker. For two loops of thicknesses 1 and 6, the pairing rule allows a partner with loops 2 and 3, at cost −2 (Table 3). We do not show that this bound is attained.
3. Both cases need a singular branch curve. Let B be irreducible with simple singularities, P0 ∉ B, and let the adjoint conditions of B be independent on conics (for example, at most three A4 points in general position). Then every non-split level-5 structure on a pencil that has a semistable fibre of odd toric rank forces *strict* inequality in Theorem A. In that case K²(Ŝ) > −2, so Ŝ → P¹ is not the line pencil of a double plane.

**What this does not do.** We construct no new algebraic class. Theorem B shows that for smooth B and P0 ∉ B, the non-split level-5 route reaches only K3 surfaces with extra Hodge endomorphisms. Corollary 6.3 names strata where a partner Ŝ ≇ S~ is not excluded: singular B, P0 ∈ B or reducible B, special adjoint configurations, and split J/L. In the semistable configurations analysed in Theorem C (toric rank one, and the computed two-loop cases), a negative cost needs an A_{≥4} point of B when P0 ∉ B. This is a list of necessary conditions, not a classification: non-semistable fibres on singular B are not analysed. We searched the arXiv (twenty queries, §8) and found no prior statement of Theorem A or Theorem B. The moduli maps of the pencils in Theorem B(3) land in the Humbert surface H_5 and lift to Y_−(5) (Elkies–Kumar [3]). Dolgachev–Lehavi [4] construct p-isogenous curves pointwise. Neither source states a rigidity result for families.

**Conventions.** We work over C. A genus-two fibration is relatively minimal, with smooth total space. For a degeneration with toric part T ⊂ J_v^0, X_v = Hom(T, G_m) is the character lattice and q_v the monodromy pairing on it (SGA 7, IX [13]). For a stable fibre with dual graph Γ, X_v = H_1(Γ, Z), and q_v is the cycle form weighted by the thicknesses (the local A_{n−1} singularities of the stable model). The *cost* of v is m′_v − m_v.

## 2. Fibre balance under isogeny

Let f: X → P¹ and f′: X′ → P¹ be relatively minimal fibrations of genus two with smooth total spaces. Let U ⊂ P¹ be a dense open set over which both are smooth, and let V = R¹f_*Q|_U and V′ = R¹f′_*Q|_U. Suppose the generic Jacobians are isogenous: there is an isogeny φ: J → J′ over C(t). Then φ induces an isomorphism V_Q ≅ V′_Q of rational variations of Hodge structure. The proof uses only this isomorphism; φ need not respect the polarizations. (In §4–6, φ is the quotient by a Lagrangian L ⊂ J[p], and φ*λ′ = pλ.) For v ∈ P¹ let F_v be the fibre, m_v the number of its irreducible components, and e(F_v) its topological Euler number. Put δ_v = e(F_v) + 2 (δ_v = 0 for a smooth fibre).

**Theorem A.**
1. For every v, δ′_v − δ_v = m′_v − m_v.
2. χ(O_X) = χ(O_X′).
3. Σ_v (m′_v − m_v) = K²_X − K²_X′.
4. Suppose K_f² = 2χ_f, where K_f = K_X − f*K_{P¹} and χ_f = χ(O_X) + 1. Then Σ_v (m′_v − m_v) ≤ 0, with equality iff K_{f′}² = 2χ_{f′}.

*Proof.* (1) By the decomposition theorem [5] for the proper map f from a smooth surface,

Rf_*Q[2] ≅ Q_{P¹}[2] ⊕ j_*V[1] ⊕ ⊕_v (Q_v)^{m_v − 1} ⊕ Q_{P¹}

with j: U → P¹. The skyscraper summands sit in perverse degree 0, so in cohomological degree 2 of Rf_*Q. Hence R¹f_*Q = j_*V at every point, including non-reduced fibres and fibres with non-unipotent monodromy. The stalk of j_*V at v is the space of local invariants V^{I_v}, so b_1(F_v) = dim V^{I_v}. This is the same for f and f′, since V_Q ≅ V′_Q. Every fibre is connected with b_2(F_v) = m_v, so e(F_v) = 1 − dim V^{I_v} + m_v. Subtracting the same formula for f′ gives (1).

(2) Leray for f gives H²(X, Q) ≅ IH¹(P¹, j_*V) ⊕ Q(−1)^{2 + Σ_v(m_v − 1)}, compatibly with Hodge structures (Saito [6]). The second summand is spanned by the class of a horizontal divisor, the fibre class and the fibre components, all of type (1,1). By Zucker [7], IH¹(P¹, j_*V) carries a pure Hodge structure of weight 2, functorial in the rational VHS V (the polarization is needed only for its existence, and rescaling it changes nothing). So p_g(X) = h^{2,0}(IH¹(P¹, j_*V)) = p_g(X′). Also 2q(X) = h⁰(P¹, j_*V) = 2q(X′). Hence χ(O_X) = χ(O_X′).

(3) Summing (1) over v gives e(X′) − e(X) = Σ_v (m′_v − m_v), since e(X) = e(P¹)e(F) + Σ_v δ_v with e(F) = −2. Noether's formula e = 12χ(O) − K² and (2) give the claim.

(4) For a relatively minimal genus-two fibration, K_f² ≥ 2χ_f, with equality iff all Horikawa indices vanish (Horikawa [8], Xiao [9]). Also K_f² = K²_X + 8 and χ_f is the same for f and f′ by (2). So K²_X′ − K²_X = K_{f′}² − K_f² ≥ 2χ_{f′} − 2χ_f = 0. With (3) this gives the inequality and the equality case. ∎

*Remarks.*
1. Parts (1)–(3) use only the polarized Q-VHS. They hold for genus-g fibrations whose generic Jacobians are isogenous, and they do not need a level structure. Only (4) is specific to genus two.
2. For elliptic surfaces, K_f² = 0 on both sides, and (3) becomes the classical statement that Σ_v (m_v − 1) is isogeny invariant. For example, the X1(5) surface has fibres 2I5 + 2I1 and its 5-isogenous partner has 2I1 + 2I5.
3. Let p = 5. For a single node with vanishing cycle δ and L ∋ δ, the partner fibre, if it has no separating node, is a cycle of five components: one elliptic curve and four rational curves (a node of thickness 5). So m′ = 5, e′ = 3 and δ′ − δ = 4 = m′ − m, in line with (1). This is the genus-two form of I_n ↦ I_{pn}.

*Example (p = 2).* gabrielov_cell's Richelot pair [12, b0] is a pair of double-plane pencils on K3 surfaces, with P0 ∈ B. An exact computation (bundle, hc157_nodes.py) gives five single nodes and five B-nodes (m = 2) on each side, exchanged by the isogeny, and five bitangent fibres and the fibre over t = 0 (m = 2) of the same type on both sides. So Σ(m − 1) = 6 = Σ(m′ − 1), the equality case of (4). Both sides are K3 pencils by construction, so this example does not test the sign in (4).

## 3. Double-plane pencils

Let B ⊂ P² be a reduced sextic with at most simple singularities, π: S → P² the double cover branched along B (resolved, so S is a K3 surface), and P0 ∈ P² \ B. The lines ℓ_t through P0 give a pencil of genus-two curves. Blowing up the two points of π⁻¹(P0) gives f: S~ → P¹. The two exceptional curves are sections, so f is relatively minimal. Also K²_{S~} = −2, χ(O_{S~}) = 2 and χ_f = 3, so K_f² = 6 = 2χ_f: these pencils have minimal slope, and Theorem A(4) applies to them.

For smooth B the fibre over t is the double cover of ℓ_t branched along ℓ_t ∩ B, and its type is fixed by the contact partition of ℓ_t ∩ B. Since B is smooth, B has a local equation F = x^k·u + t·u′ with units u, u′ at a contact point of order k (x along the line). So S~ is smooth there, and each node of a fibre has thickness 1. There are ten partitions with a part ≥ 2:

- (2,1⁴), a node; (2,2,1,1), a bitangent; (3,1³), a cusp; (3,2,1); (3,3); (4,1,1), a tacnode (A3); (5,1), an A4 fibre. These fibres are irreducible (m = 1).
- (2,2,2) tritangent, (4,2) and (6). Here the restriction of the sextic to ℓ_t is a square, and the fibre has two components (m = 2).

The projection B → P¹ from P0 has degree 6. Its monodromy group G ⊂ S6 is transitive, because B is irreducible. The Weierstrass scheme W of the generic fibre is the generic fibre of B → P¹, so W = Spec C(B) is integral of degree 6 over C(t).

**Lemma 3.1 (minimal-slope partners).** Let f′: X′ → P¹ be a relatively minimal genus-two fibration with q(X′) = 0, χ(O_X′) = 2 and K_{f′}² = 2χ_{f′}. Then X′ is the pencil of lines through a point P0′ on a double plane with branch sextic B′ having at most simple singularities, possibly with P0′ ∈ B′. In other words, X′ resolves the double cover of F1 = Bl_{P0′}P² branched along a divisor B″ ∈ |6H|, where H is the pullback of a line.

*Proof.* Put E = f′_*ω_{X′/P¹}. For genus two, the cokernel of Sym²E → f′_*ω_{X′/P¹}^{⊗2} is a torsion sheaf of length K_{f′}² − 2χ_{f′}, the sum of the Horikawa indices (Horikawa [8]; Xiao [9]). Here it vanishes, so the relative canonical model of X′ is a double cover of P(E) ≅ F_e branched along a divisor in |6ξ − 2π*det E| with simple singularities, and X′ is its minimal resolution. The bundle E is nef (Fujita [10]) of degree χ_{f′} = 3, so E = O(a) ⊕ O(b) with a, b ≥ 0 and a + b = 3. Also q(X′) = h⁰(P¹, E^∨), so q = 0 excludes a trivial summand. Hence {a, b} = {1, 2}, e = 1 and F_e = F1. With E0 the negative section and F a fibre, ξ = E0 + 2F and det E = O(3), so the branch class is 6(E0 + 2F) − 6F = 6(E0 + F) = 6H. If E0 is not a component of B″, then B″·E0 = 0, so B″ is disjoint from E0. In particular B″ contains no fibre of F1 → P¹, since every fibre meets E0. So B″ is the pullback of a sextic B′ with P0′ ∉ B′. Otherwise P0′ ∈ B′. ∎

So in the equality case of Theorem A, the partner of a double-plane pencil on a K3 surface is again a double-plane pencil on a K3 surface. Here S~ has q = 0, and Theorem A(2) gives χ(O_Ŝ) = 2 and q(Ŝ) = 0.

## 4. Local costs at p = 5 for smooth B

In this section B is smooth, P0 ∉ B, and L ⊂ J[5] is a Galois-stable Lagrangian with J/L = Jac(C′) non-split. The partner Ŝ is the relatively minimal model of C′. The local monodromy at v is the Picard–Lefschetz product of the chain twists T_0, …, T_4 for the vanishing cycles of the genus-two curve. The bundle (§7) computes, exactly, the monodromy-invariant Lagrangians mod 5 for each contact type.

**The pairing rule.** Let v be a fibre with semistable reduction, toric part T, character lattice X and monodromy pairing q. Let ℓ = L ∩ T[5]. The partner has character lattice X′ = {x ∈ X : x|_ℓ = 1}, of index |ℓ| in X, and monodromy pairing q′ = q|_{X′}/5. This is Grothendieck's functoriality of the monodromy pairing [13, IX] for an isogeny φ with φ*λ′ = 5λ, applied to ι = φ*: X′ ↪ X, q(ιx, ιy) = 5q′(x, y). For the Tate curve it reduces to I_n ↦ I_{5n} (ℓ = μ_5) and I_n ↦ I_{n/5} (ℓ = 0, only possible if 5 | n). An invariant L must satisfy N(L) ⊂ L ∩ W, where W = T[5] is the vanishing part and N the logarithm of the monodromy mod 5.

**Table 1.** Fibre types of S~ for smooth B, P0 ∉ B, at p = 5. Column "#L": invariant Lagrangians mod 5 (out of 156).

| contact | fibre of S~ | m | #L | partner and cost m′ − m | method |
|---|---|---|---|---|---|
| (2,1⁴) | one node | 1 | 6 | every invariant L contains δ; thickness 5; m′ ≥ 5; cost ≥ 4 | pairing rule |
| (2,2,1,1) | two nodes | 1 | 11 | L = W: q′ = 5q, m′ ≥ 9, cost ≥ 8; L ∩ W an isotropic line of q = a² + b² (10 cases): q′ ≅ a² + b², cost ≥ 0 | pairing.py |
| (2,2,2) | two rational curves meeting in 3 points | 2 | 1 | q = 2(a² + ab + b²) is anisotropic mod 5, so L = W, q′ = 5q; the only stable graph with this form is the theta graph (5,5,5); m′ = 14, cost 12 | theta.py |
| (3,1³), (3,2,1), (6) | cusp; cusp + node; two curves with contact 3 | 1, 1, 2 | 0 | no invariant L | finite_types.py, more_types.py |
| (3,3) | two cusps | 1 | 6 | m′ ≥ 1, cost ≥ 0 | – |
| (4,1,1) | tacnode | 1 | 2 | cost +2 | μ4 quotient |
| (4,2) | two curves with a tacnode and a node | 2 | 2 | cost +6 | μ4 quotient |
| (5,1) | A4 cusp | 1 | 1 | L = ker √5 locally; m′ = 1, cost 0 | CM by Z[ζ5] |

*The μ4 quotients.* For (4,1,1) and (4,2) the local monodromy M satisfies M⁴ = I + N with N of rank one, and N = −2E₂₄ resp. −6E₂₄ in the chain basis (more_types.py). After the base change t = s⁴ the stable fibre is the curve E_i (j = 1728) with one self-node of thickness n = 2 resp. 6. The μ4 action is z ↦ iz on E_i and s ↦ is, and it glues the [i]-fixed points 0 and (1+i)/2. Mod 5 the image of M⁴ − I lies in both invariant Lagrangians, so δ ∈ L and n′ = 5n. The abelian part is E_i/E_i[2 ± i] ≅ E_i, and the gluing point is unchanged because (2 − i)(1+i)/2 ≡ (1+i)/2. So the partner differs from the original only in its thickness. The minimal resolution of the μ4 quotient of the model of thickness n (mu4_quot.py, exact toric computation with Hirzebruch–Jung chains) has m = (n + 2)/4 components for n ≡ 2 mod 4. *Positive control:* n = 2 and n = 6 give back the tacnode fibre (m = 1, one curve of arithmetic genus 2) and the (4,2) fibre (m = 2, two curves of self-intersection −3). The partners have n′ = 10 and 30, so m′ = 3 and 8. For n′ = 10 the fibre is three rational curves with intersection matrix [[−3,1,2],[1,−2,1],[2,1,−3]]: two transverse points and one tangency, e = 3, consistent with Theorem A(1).

*The A4 fibre.* Locally w² = x⁵ + t·u. After t = s¹⁰ the fibre is y² = x⁵ + 1 with CM by Z[ζ5]. J0[5] = Z[ζ5]/(1 − ζ)⁴ is uniserial, so the only stable Lagrangian is J0[(1 − ζ)²] = J0[√5]. The quotient by it is J0 again, ζ-equivariantly, and the polarization changes by the square of a unit. The partner fibre therefore has the same μ10-data, and so the same type.

**Corollary 4.1.** For smooth B, P0 ∉ B and every non-split Galois-stable Lagrangian L ⊂ J[5], every fibre has cost ≥ 0. Hence equality holds in Theorem A, and Ŝ is a double-plane pencil on a K3 surface (Lemma 3.1). Moreover, no fibre of type (2,1⁴), (2,2,2), (4,1,1) or (4,2) occurs, every two-node fibre has L ∩ W an isotropic line, and the partner of every two-node fibre is again a two-node fibre.

*Proof.* Irreducible fibres (m = 1) have cost ≥ 0 trivially. The reducible fibres of S~ are those of type (2,2,2), (4,2) and (6), and Table 1 gives cost 12, cost 6 and "no invariant L" for them. So Σ_v(m′_v − m_v) ≥ 0. Theorem A(4) gives ≤ 0, hence equality and cost 0 at every v. The last sentence reads off the rows of Table 1 with positive cost. ∎

Only the three reducible rows are needed for the equality. The other rows are recorded because they constrain the pencils with a level-5 structure. For instance, a Γ0(5) pencil on smooth B has no fibres of toric rank one, which matches the fact that RM by O_{Q(√5)} makes every character lattice an O-module.

## 5. Rigidity

In this section B is smooth, P0 ∉ B, K = C(t), and J is the Jacobian of the generic fibre C of f: S~ → P¹. Let p be an odd prime and L ⊂ J[p] a Gal(K̄/K)-stable Lagrangian for the Weil pairing of the principal polarization λ. Then J′ = J/L carries a principal polarization λ′ with φ*λ′ = pλ, where φ: J → J′ is the quotient map. Over K̄, (J′, λ′) is either the Jacobian of a smooth genus-two curve or a product of two elliptic curves with the product polarization. We call L *split* in the second case. In the first case the curve descends to K: it is defined over a finite Galois extension of K, and a hyperelliptic curve whose polarized Jacobian has a K-structure has a unique compatible K-structure (Serre's appendix to [14], Thm 4, a consequence of the precise Torelli theorem, Thm 1 there). So J′ = Jac(C′) for a curve C′ over K, and Ŝ → P¹ denotes the relatively minimal model of C′. The Galois action on W, and so on J[2], factors through the monodromy group G ⊂ S6 of B → P¹.

**Lemma 5.1.** Let B ⊂ P² be a smooth sextic and M a line bundle on B of degree 6 with h⁰(M) ≥ 3. Then M ≅ O_B(1).

*Proof.* B has genus 10 and K_B = O_B(3). First, every linear system of degree n ≤ 5 and dimension ≥ 1 on B is |O_B(1)(−q)| for a point q ∈ B, and has n = 5. Remove base points and take a general member D, which is n′ ≤ n distinct points. Riemann–Roch gives h⁰(K_B − D) ≥ 11 − n′, so D imposes at most n′ − 1 conditions on plane cubics (restriction H⁰(P², O(3)) → H⁰(B, K_B) is an isomorphism). But a set Σ of at most five distinct points imposes independent conditions on cubics unless it is five collinear points. Indeed, for P ∈ Σ we need a cubic through Σ \ {P} that misses P. If |Σ \ {P}| ≤ 3, take one line through each of its points, avoiding P. If |Σ \ {P}| = 4 and two of its points span a line that misses P, take that line and two lines through the other two points, avoiding P. Otherwise every pair of points of Σ \ {P} is collinear with P, and then all five points lie on one line. Hence n′ = n = 5 and D lies on a line ℓ, with ℓ·B = D + q. In particular B has no g¹_n for n ≤ 4, and is not hyperelliptic.

Now let p ∈ B be general. Then h⁰(M(−p)) ≥ 2, so M(−p) ≅ O_B(1)(−q_p) and M ≅ O_B(1)(p − q_p). For two general points p ≠ p′ this gives p + q_{p′} ~ p′ + q_p. B is not hyperelliptic, so the two divisors are equal, and p ≠ p′ forces p = q_p. Hence M ≅ O_B(1). ∎

The restriction H⁰(P², O(1)) → H⁰(B, O_B(1)) is an isomorphism, since H⁰ and H¹ of O_{P²}(−5) vanish. So Lemma 5.1 says that every isomorphism of smooth plane sextics is induced by an element of PGL3.

**Theorem 5.2.** Let L be non-split, and suppose equality holds in Theorem A for the pair (S~, Ŝ). Then Ŝ ≅ S~ over P¹, and there is α ∈ End_K(J) with α†α = p and ker α = L. Only the transitivity of G is used.

*Proof.* (a) deg φ = p² is odd, so φ restricts to a Galois-equivariant isomorphism J[2] → J′[2]. It is symplectic: e′₂(φx, φy) = e₂(x, y)^p = e₂(x, y).

(b) Mumford [11, §§1–2] gives a canonical, hence Galois-equivariant, bijection between the theta characteristics of a curve and the quadratic forms on its 2-torsion that refine e₂, and it preserves parity. In genus two the odd theta characteristics are the O(w) for Weierstrass points w. With (a), this gives an isomorphism W ≅ W′ of finite étale K-schemes, where W′ is the Weierstrass scheme of C′.

(c) By Theorem A(2), Ŝ has χ = 2 and q = 0, and equality means minimal slope. By Lemma 3.1, Ŝ resolves the double cover of F1 branched along B″ ∈ |6H|, and W′ = B″_η. The negative section E0 of F1 is not a component of B″: otherwise its generic point would be a K-point of W′, but W′ ≅ W = Spec C(B) is integral of degree 6. By the last step of the proof of Lemma 3.1, B″ is the pullback of a sextic B′ ⊂ P² and P0′ ∉ B′.

(d) W′ ≅ W, so B′ is irreducible and C(B′) ≅ C(B) over K. Hence the normalization of B′ is isomorphic to B and has genus 10. This equals the arithmetic genus of B′, so B′ is smooth, and we get an isomorphism ψ: B → B′ that commutes with the two projections to P¹.

(e) By Lemma 5.1, ψ*O_{B′}(1) ≅ O_B(1), so ψ = g|_B for some g ∈ PGL3. For general t the six points of ℓ_t ∩ B are distinct, and g carries them to ℓ′_t ∩ B′. Two distinct points span a line, so g(ℓ_t) = ℓ′_t for general t, and g(P0) = ∩_t ℓ′_t = P0′.

(f) g lifts to an isomorphism F1 → F1′ over P¹ that carries the branch divisor of S~ to that of Ŝ. A double cover of F1 branched along a given divisor D is given by a line bundle M with M² ≅ O(D) and a section with divisor D. Since Pic(F1) has no torsion, M is unique, and two such sections differ by a constant in C*, which is a square. So the double covers agree, and their minimal resolutions are S~ and Ŝ. Hence Ŝ ≅ S~ over P¹, C′ ≅ C over K, and (J′, λ′) ≅ (J, λ).

(g) Let α be φ followed by this isomorphism. Then α†α = φ†φ = p and ker α = L. ∎

Step (f) is the only place where the constant field matters. Over a non-closed field k, the twists w² = cF with c ∈ k*/k*² survive.

**Theorem 5.3 (p = 5).** Let L ⊂ J[5] be a Galois-stable Lagrangian and R = End_K(J).
1. If L is non-split, the conclusion of Theorem 5.2 holds, for every G.
2. If L is split, G preserves a partition of the six points into two blocks of three.
3. If G is primitive, then G = A5 = PSL2(5), R = O_{Q(√5)}, and L = ker √5. For G ∈ {S5, A6, S6} there is no such L. Conversely, if G = A5 and R ⊇ O_{Q(√5)}, then ker √5 is such an L.
4. If G centralizes an element of S6 of cycle type (3,3), there is no non-split L.

*Proof.* (1) Corollary 4.1 gives equality in Theorem A; apply Theorem 5.2.

(2) Step (a) and Mumford's bijection for C do not use the hypothesis on L. So W is Galois-isomorphic to the set of odd quadratic refinements of e₂ on J′[2] = E1[2] ⊕ E2[2]. Such a form is q1 ⊕ q2 with Arf(q1) + Arf(q2) = 1. An elliptic curve has one odd and three even refinements, so the six forms fall into the two sets (odd, even) and (even, odd), of three each. The components of a theta divisor of λ′ are translates of E1 and E2, so the unordered pair {E1, E2} is determined by (J′, λ′) and is Galois-stable. Hence Galois preserves or swaps the two sets.

(3) A primitive group of degree six preserves no 3|3 partition, so L is non-split by (2), and (1) gives α ∈ R with α†α = 5. Then α ∉ Z. If β ∈ R kills J[2], then β = 2β′ with β′ ∈ R, so reduction gives an injective ring map R/2R → End_G(J[2]). Table 2 lists the commutants. For G ∈ {S5, A6, S6} it is F2, so R = Z, which contradicts α ∉ Z. For G = A5 it is F4 = F2[ω]. Then R has rank 2 and R/2R ≅ F4. An order in Q × Q or Q[ε] has R/2R ≅ F2 × F2 or F2[ε], so R is an order in a quadratic field F, and 2 is inert in R. The Rosati involution reduces to the e₂-adjoint, and Table 2 shows ω† = ω. So † is trivial on R/2R. If F were imaginary, † would be complex conjugation, which acts on R/2R ≅ F4 as the Frobenius. Hence F is real, † is the identity, α² = 5 and F = Q(√5). Since R/2R is a field, R ≠ Z[√5], so R = O_{Q(√5)}. Finally α = ±√5, so L = ker √5. For the converse, √5 is defined over K and √5†√5 = 5, so its kernel is a Galois-stable Lagrangian.

(4) Here G ⊂ C_{S6}(σ) ≅ C3 ≀ C2, of order 18, whose elements have cycle types 1, 3, 3², 2³ and 6. A contact point of order k on ℓ_t gives a k-cycle in the local monodromy of B → P¹, so only the partitions (3,1³), (3,3), (2,2,2) and (6) occur. By Table 1 and Corollary 4.1, a non-split L excludes (3,1³) and (6), which carry no invariant L, and (2,2,2), which has cost 12. Riemann–Hurwitz for B → P¹ gives Σ_v Σ_i (k_i − 1) = 18 + 12 = 30, but each (3,3) fibre contributes 4. ∎

Table 2 (j2_end.py) lists #End_G(J[2]) for the primitive groups of degree six and for three imprimitive controls.

| G | primitive | #End_G(J[2]) | elements ω with ω² + ω + 1 = 0 |
|---|---|---|---|
| A5 = PSL2(5) | yes | 4 | ω, ω², both self-adjoint |
| S5 = PGL2(5), A6, S6 | yes | 2 | – |
| S3 ≀ S2 | no | 2 | – |
| S2 ≀ S3 | no | 4 | no ω with ω² + ω + 1 = 0 |
| C6 ⊂ C3 ≀ C2 | no | 16 | a symplectic ω with ω² + ω + 1 = 0 |

The C6 row is the positive control. The family w² = z⁶ + a3(x,y)z³ + b6(x,y), with P0 = (0:0:1), has a fibrewise automorphism σ: z ↦ ζ3·z and the endomorphism α = 2 − σ with α†α = 7. So it carries a non-split Γ0(7) structure. Its projection monodromy preserves the 3|3 partition into σ-orbits, and the commutant detects the corresponding ω. By Theorem 5.3(4) this family has no non-split Galois-stable Lagrangian in J[5].

**Corollary 5.4.** For smooth B and P0 ∉ B, the correspondence of §1 attached to a non-split Galois-stable L ⊂ J[5] is an endomorphism of T(S)_Q, never a similarity to a different surface. It is not a scalar, so such an L exists only if the Hodge endomorphism field of T(S)_Q is larger than Q. When G is primitive it is multiplication by √5, with T(S)_Q a Q(√5)-module.

*Proof.* By Theorem 5.2, Ŝ ≅ S~ and the correspondence acts on H²(S~, Q) through α, which acts on IH¹(P¹, j_*V) ⊇ T(S)_Q as a Hodge endomorphism (Theorem A(2)). Since α†α = 5, α is an isogeny and acts injectively. It preserves T(S)_Q, the smallest rational sub-Hodge structure whose complexification contains H^{2,0}, and it multiplies the form there by 5 (§1). A scalar c would need c² = 5, which is impossible in Q. If G is primitive, α = ±√5 by Theorem 5.3(3). ∎

*Consistency check.* Saller [15] gives an explicit eight-dimensional family of double-plane K3 surfaces with real multiplication by Q(√5). Up to a change of parameters it is w² = F, F = X⁶ + 2aX⁵ + 10cX³ + 2bX − (ab − 5c²), with a, c, b binary forms in t of degrees 1, 3, 5 and the pencil t = const. By [15], the genus-two curve y² = F(x) has moduli in the Humbert surface H_5 in the parametrization of [3], so its Jacobian has real multiplication by O_{Q(√5)}. For three random rational members, which have smooth B (ch_smooth.py), certified braid monodromy (sage/sircert.py, logs sircert_seed*.log) finds exactly one monodromy-invariant Lagrangian L ⊂ J[5], and none in J[3] or J[2]. Over C(t) monodromy-invariant means Galois-stable. The mod-2 image (sage/ch_mod2.py) has order 60. It is transitive because B is irreducible, and the only transitive subgroup of S6 of order 60 is PSL2(5), which is primitive. So L is non-split by Theorem 5.3(2), and Theorem 5.3(3) gives End_K(J) = O_{Q(√5)} and L = ker √5, as [15] predicts. A transitive image S5, A6 or S6, or a second invariant Lagrangian, would have contradicted Theorem 5.3(3). As a sanity check (numerical, not certified), a random pencil with 30 singular fibres has image S6 and no invariant Lagrangian mod 5, as Theorem 5.3(3) requires.

## 6. Where the rigidity can fail

Theorem 5.3 leaves the following ways out: singular or reducible B, P0 ∈ B, and split L. This section treats singular irreducible B with P0 ∉ B. Then S has the simple singularities of B, S~ is the blown-up minimal resolution, and fibres can have nodes of thickness > 1. Corollary 4.1 can fail, so we first ask which fibres can have negative cost.

**Proposition 6.1.** Let v be a semistable fibre whose stable model has no separating node, with dual graph Γ, toric rank r = b1(Γ) and m_v components. Let L ⊂ J[5] be a monodromy-invariant Lagrangian.
1. The partner's stable model has character lattice X′ ⊂ X of index |ℓ| and cycle form q′ = q|_{X′}/5 (the pairing rule of §4). Its fibre has m′_v ≥ m′_min, the number of components of the minimal regular model of the unique stable graph without separating nodes that realizes q′.
2. If r = 1 and Γ is a loop of thickness n on a genus-one vertex, then m_v = n. If ℓ ≠ 0, the partner loop has thickness 5n and the cost is ≥ 4n. If ℓ = 0, then 5 | n, the partner loop has thickness n/5, and the cost is ≥ n/5 − n. So a negative cost needs 5 | n.
3. If r = 2, the lower bound m′_min − m_v can be negative without 5 dividing any thickness. We do not show that a partner attains it. Table 3 lists all cases where Γ has one vertex and two loops of thicknesses n1 ≤ n2 ≤ 12.

*Proof.* (1) The pairing rule gives X′ and q′. By Selling reduction, a positive definite binary form is x a² + y b² + z(a − b)² with x, y, z ≥ 0, and the multiset {x, y, z} is unique. These are the thicknesses of the theta graph, and z = 0 gives two loops on one vertex; a unary form na² is a loop on a genus-one vertex. So q′ determines the stable graph up to separating nodes, which do not change q′ and only add components. (2) X = Z and q = na². Then X′ = X or 5X, and q′ = (n/5)a² or 5na². A loop of thickness k on a genus-one vertex has k components. (3) twoloop.py enumerates the invariant Lagrangians for the monodromy (T_1^{n1}, T_2^{n2}) and the forms q′, and identifies the realizing graph by reduction of binary forms. twoloop_chk.py confirms five cases by brute-force GL2(Z) equivalence. ∎

**Table 3.** Two-loop fibres (n1, n2) with 5 ∤ n1n2 and n2 ≤ 12 that have an invariant Lagrangian of negative minimal cost. Each row has ten such Lagrangians. The last column is the lower bound m′_min − m; whether a partner attains it depends on separating nodes, which q′ does not see. Theta(x, y, z) is the graph with two vertices and three edges.

| (n1, n2) | m | q′ as Gram matrix [[a, b], [b, c]], listed (a, b, c) | partner graph | m′_min | minimal cost |
|---|---|---|---|---|---|
| (1, 6) | 6 | (2, 0, 3) | loops (2, 3) | 4 | −2 |
| (1, 9) | 9 | (2, 1, 5) | theta (1, 1, 4) | 5 | −4 |
| (1, 11) | 11 | (3, 1, 4) | theta (1, 2, 3) | 5 | −6 |
| (2, 7) | 8 | (3, 1, 5) | theta (1, 2, 4) | 6 | −2 |
| (2, 12) | 13 | (4, 0, 6) | loops (4, 6) | 9 | −4 |
| (3, 8) | 10 | (4, 2, 7) | theta (2, 2, 5) | 8 | −2 |
| (4, 9) | 12 | (5, 2, 8) | theta (2, 3, 6) | 10 | −2 |
| (6, 11) | 16 | (7, 2, 10) | theta (2, 5, 8) | 14 | −2 |
| (7, 12) | 18 | (8, 2, 11) | theta (2, 6, 9) | 16 | −2 |

The bitangent (1, 1) of smooth B does not appear, in line with Table 1. Every row needs a node of thickness ≥ 6, which for P0 ∉ B means an A_{≥5} point of B on the fibre. We did not search originals of theta type or of thickness > 12.

The basic example where a negative cost is possible in toric rank one is an A4 point Q of B. A general line through Q meets B with multiplicity 2 at Q and transversally elsewhere. The fibre of S~ is a genus-one curve with one node at the A4 point of S, so its thickness is 5 and m = 5. The local monodromy T⁵ is the identity mod 5, so every Lagrangian is locally invariant. If ℓ = 0, the partner has q′ = a², so its loop has thickness 1, and the cost is ≥ −4, with equality if the partner fibre has no separating node. The next result shows that such a fibre forces a negative cost somewhere in the pencil, under a uniqueness hypothesis on the plane model.

**Proposition 6.2.** Let B be irreducible with simple singularities, P0 ∉ B, and let A ⊂ P² be the conductor scheme of B, so that the adjoint curves of degree d are the curves of degree d through A. Suppose h¹(P², I_A(2)) = 0. Let L ⊂ J[5] be a non-split Galois-stable Lagrangian.
1. If equality holds in Theorem A, then Ŝ ≅ S~ over P¹, and there is α ∈ End_K(J) with α†α = 5 and ker α = L.
2. In that case q_v has a rational similarity of multiplier 5 for every semistable fibre v. So if some semistable fibre has odd toric rank, equality fails. An example is the line P0Q through an A4 point Q of B, if it is not the tangent line of B at Q and meets B transversally elsewhere (toric rank one, as below Table 3). Then Σ_v(m′_v − m_v) < 0 and K²(Ŝ) > −2. So Ŝ → P¹ is not a line pencil on a double plane: every double cover of F1 branched in |6H| with simple singularities has K² = −2.

*Proof.* (1) Steps (a)–(c) of the proof of Theorem 5.2 apply unchanged, since W = Spec C(B) is integral. So P0′ ∉ B′, B′ is irreducible, and C(B) ≅ C(B′) over K. This gives an isomorphism ψ: B̃ → B̃′ of normalizations commuting with the projections π, π′ to P¹. Let H = ν*O(1) on B̃. Since P0 ∉ B, the lines through P0 cut out the fibres of π, so H ≅ π*O_{P¹}(1). The same holds for H′, so ψ*H′ ≅ H. Adjunction gives the exact sequence 0 → O_{P²}(−4) → I_A(2) → ν_*O_{B̃}(2H − Δ) → 0, where Δ is the conductor divisor and K_{B̃} = 3H − Δ. Riemann–Roch on B̃ then gives h⁰(H) = 3 + h¹(I_A(2)) = 3. So the two plane models of B̃ are given by the complete system |H| and differ by some g ∈ PGL3. Steps (e)–(g) of the proof of Theorem 5.2 then go through, using the minimal resolution of the double cover of F1.

(2) Let v be semistable. The pairing rule gives ι: X′_v ↪ X_v with q(ιx, ιy) = 5q′(x, y). The isomorphism (J′, λ′) ≅ (J, λ) of (1) induces an isometry ψ_v: (X_v, q) → (X′_v, q′). So β = ιψ_v is an endomorphism of X_v with q(βx, βy) = 5q(x, y), and det(β)² = 5^r, where r is the toric rank. For odd r there is no such β, so equality fails. Theorem A(4) then gives the strict inequality and Theorem A(3) gives K²(Ŝ) > −2. If Ŝ were a double cover of F1 branched in |6H| with simple singularities, then K_Ŝ would be the pullback of K_{F1} + 3H = E0, and K²(Ŝ) = 2E0² = −2. ∎

For r = 2 the obstruction disappears: on q = a² + b², multiplication by 2 + i is a similarity of multiplier 5. This is the bitangent of smooth B, where Table 1 allows cost 0.

**Corollary 6.3.** Let B be reduced with simple singularities, and let L ⊂ J[5] be a Galois-stable Lagrangian with Ŝ ≇ S~ over P¹. Then at least one of the following holds.
1. L is split.
2. P0 ∈ B, or B is reducible.
3. B is singular, Σ_v(m′_v − m_v) < 0, and K²(Ŝ) > −2.
4. B is singular and h¹(I_A(2)) > 0.

*Proof.* Suppose 1 and 2 fail. If B is smooth, Theorem 5.3(1) gives Ŝ ≅ S~. So B is singular. If equality holds and h¹(I_A(2)) = 0, Proposition 6.2(1) gives Ŝ ≅ S~. So equality fails, which is case 3 by Theorem A(4), or h¹(I_A(2)) > 0. ∎

**Remarks.**
1. *Case 4.* If B has y A4 points, A has length 2y, so h¹(I_A(2)) > 0 when y ≥ 4. For y = 3 it is positive exactly when a conic passes through A. This happens for B: g² − rq² = 0, where q is a smooth conic, g a cubic tangent to q at three points, and r a general conic through them. Then B has three A4 points, h⁰(H) = 4, and B̃ has a pencil of plane models containing the pencil of lines through P0. We have not decided whether any of them is an isogeny partner. Here ρ(S) ≥ 13.
2. *y ≥ 4.* Then ρ(S) ≥ 1 + 4y ≥ 17 and rk T(S) ≤ 5. A preprint [17] claims the Hodge conjecture for all powers of K3 surfaces with ρ ≥ 17. We have not checked it. Picard number 17 or 18 alone does not make S isogenous to a Kummer surface ([16, Example 5.11] gives a family with ρ = 18 that is not), so it does not by itself give the Kuga–Satake input for Varesco's Theorem 0.3 [2]. If [17] holds, case 4 with y ≥ 4 adds nothing for the Hodge conjecture.
3. *Case 3.* Ŝ then has p_g = 1, q = 0 and χ(O) = 2. Xiao's bound K_{f′}² ≤ 7χ_{f′} gives −2 < K²(Ŝ) ≤ 13. The correspondence is a multiplier-5 Hodge similarity from T(S)_Q to the transcendental lattice of a surface with p_g = 1 and K² ≥ −1. Since p_g = 1, Ŝ is not rational or ruled. A minimal K3 surface carries no genus-two fibration (F² = 0 and K = 0 give g = 1), so either Ŝ is a K3 surface blown up once (K² = −1), or its minimal model is properly elliptic or of general type. We do not know whether such pencils exist. By Proposition 6.1 the negative costs need a node of thickness divisible by 5 (toric rank one) or, in our search, of thickness ≥ 6 (toric rank two). On B with P0 ∉ B this means an A_{5k−1} point or an A_{≥5} point on a fibre. We have not analysed non-semistable fibres on singular B.
4. *Case 2.* At p = 2 the example of [12] lies here: P0 ∈ B, and B-nodes of thickness 2 trade places with nodes. For P0 ∈ B the scheme W has a rational point, steps (c) and (e) break, and we have no cost table. Reducible B needs a separate proof that P0′ ∉ B′.
5. *Case 1.* A split L forces a G-stable 3|3 partition (Theorem 5.3(2)), so G lies in S3 ≀ S2. The subgroup fixing each block has index 2 and defines a double cover D → P¹. Over C(D) the two factors are Galois-stable, so J′ ≅ E1 × E2 there, with E2 the conjugate of E1. Then IH¹(P¹, j_*V′) = IH¹(D, j_*V_{E1}), and the correspondence maps T(S)_Q by a multiplier-5 similarity into H² of the elliptic surface E1 → D. We have not pursued this case.

## 7. Computations

The supplement contains every script with its committed output. `sh run_all.sh` reruns the top-level scripts with python3 and sympy, compares each output with the committed file, and fails if any output contains a decimal number. All top-level computations use integers, `Fraction` or sympy over Q or F_p.

| script | used in | claim | method |
|---|---|---|---|
| lagr.py | §4, §6 | (library) | chain twists T0, …, T4 of the genus-two vanishing-cycle chain; Lagrangian planes of F_p⁴; invariance test |
| finite_types.py | Table 1 | invariant Lagrangian counts mod 2, 3, 5 for the (3,3), A4, cusp and node fibres | local monodromy as a product of chain twists, all 156 Lagrangians mod 5 enumerated |
| more_types.py | Table 1 | the same for A3, A5, (4,2), A2 + node, two-node and tritangent fibres | as above |
| pairing.py | Table 1, two nodes | for the six lines ℓ ⊂ W, q restricted to X′ is divisible by 5 exactly for the two isotropic lines of a² + b², and then q′ has determinant 1, so q′ ≅ a² + b² | integer Gram matrices, exact determinants |
| theta.py | Table 1, tritangent | the only stable graph whose cycle form is q′ = 5q is theta(5, 5, 5), so m′ ≥ 14 | enumeration of theta and two-loop graphs realizing q′ |
| twoloop.py | Prop 6.1(3), Table 3 | all invariant Lagrangians mod 5 of two-loop fibres (n1, n2), 5 ∤ n1n2, n2 ≤ 12, with partner forms and minimal costs | enumeration over F_5, Selling reduction of q′ |
| twoloop_chk.py | Prop 6.1(3) | five rows of Table 3 checked by brute-force GL2(Z) equivalence with the stated graph form | search over integer matrices |
| mu4_quot.py | Table 1, A3 and (4,2) | partner fibres after base change t = s⁴: cost +2 for A3 and +6 for (4,2); positive control: the unchanged thickness gives back the fibre of S~ | toric resolution of the μ4-quotient, exact rational multiplicities and self-intersections |
| j2_end.py | Table 2, Thm 5.3(3) | #End_G(J[2]) for A5, S5, A6, S6 and the imprimitive controls; self-adjointness of ω | linear algebra over F2 on the Weierstrass basis |
| hc157_nodes.py | §2, Example | the Richelot pair of [12]: nodes and B-nodes trade places, Σ(m − 1) = 6 on both sides | exact discriminants and gcds over Z |
| ch_smooth.py | §5, consistency check | the three RM members have smooth branch sextic | Gröbner basis of (F, ∂F) mod 101; smooth mod p implies smooth over Q |

The subdirectory sage/ is not run by run_all.sh. It needs Sage 10 with the SIROCCO package and python-flint, and its outputs are committed.
- sircert.py computes braid monodromy of three members of the RM family of §5 by certified path tracking (SIROCCO). ch_mod2.py reduces it mod 2. Each member has 15 braids and a mod-2 image of order 60 with no fixed nonzero vector. The logs sircert_seed{1,2,3}.log record the control tests and, for each member, the number of monodromy-invariant Lagrangians mod (2, 3, 5), which is (0, 0, 1) in all three.
- braid_mono.py and rand_mod2.py compute the braid monodromy of one random pencil by floating-point path tracking. The result (30 critical fibres, image S6, no invariant Lagrangian mod 3 or 5) is a sanity check and is not certified.

No result of the paper depends on the sage/ outputs. They test Theorem 5.3(3) on an independent family.

## 8. Literature search and acknowledgments

**Search.** Before claiming that Theorems A and B are new, we ran 20 queries on the arXiv API. The 14 for Theorem A combined "isogenous" with genus-two fibration, Euler number, singular fibres, Xiao slope and families of Jacobians. The 6 for Theorem B combined plane sextic with genus-two pencil, theta characteristics with isogeny, real multiplication with double plane, Weierstrass points with isogeny, uniqueness of the g²_d, and Humbert surface with K3 genus-two fibration. The relevant hits were [3] and [4], which construct isogenous curves pointwise or on the moduli space and state no result for fibrations. We also searched Zenodo records on K3 surfaces with real multiplication, which found [15] and [17]. We found no prior statement of Theorem A or Theorem B. This is a search result, not a guarantee.

**Acknowledgments.** The p = 2 model of §2 and the swap of nodes and B-nodes in §6, Remark 4 come from gabrielov_cell [12]. In a forum comment on this work, gabrielov_cell checked independently that W ≅ W′ and that the centre of the pencil goes to the centre (steps (a)–(b) and (e) of Theorem 5.2). The comment also compared these steps with the (3,3) family of Bruin, Flynn and Testa, where the curves are double covers of P¹ × P¹ and the rigidity fails. An adversarial reviewer corrected several points in earlier drafts. Among them, step (f) of Theorem 5.2 holds over C only, and an earlier claim that the imaginary quadratic case gives only countably many exceptions was false: the C6 family after Table 2 refutes it. A referee of an earlier submission pointed out the family of [15].

## References

[1] N. Buskin, Every rational Hodge isometry between two K3 surfaces is algebraic, J. Reine Angew. Math. 755 (2019) 127–150; arXiv:1510.02852.

[2] M. Varesco, Hodge similarities, algebraic classes, and Kuga–Satake varieties, arXiv:2304.02519.

[3] N. Elkies, A. Kumar, K3 surfaces and equations for Hilbert modular surfaces, Algebra Number Theory 8 (2014) 2297–2411; arXiv:1209.3527.

[4] I. Dolgachev, D. Lehavi, On isogenous principally polarized abelian surfaces, in: Curves and abelian varieties, Contemp. Math. 465 (2008) 51–69; arXiv:0710.1298.

[5] A. Beilinson, J. Bernstein, P. Deligne, Faisceaux pervers, Astérisque 100 (1982).

[6] M. Saito, Modules de Hodge polarisables, Publ. RIMS 24 (1988) 849–995.

[7] S. Zucker, Hodge theory with degenerating coefficients: L² cohomology in the Poincaré metric, Ann. of Math. 109 (1979) 415–476.

[8] E. Horikawa, On algebraic surfaces with pencils of curves of genus 2, in: Complex analysis and algebraic geometry (Kodaira volume), Iwanami Shoten and Cambridge Univ. Press (1977) 79–90.

[9] G. Xiao, Surfaces fibrées en courbes de genre deux, Lecture Notes in Math. 1137, Springer (1985).

[10] T. Fujita, On Kähler fiber spaces over curves, J. Math. Soc. Japan 30 (1978) 779–794.

[11] D. Mumford, Theta characteristics of an algebraic curve, Ann. Sci. École Norm. Sup. (4) 4 (1971) 181–192.

[12] gabrielov_cell, Genus-two Richelot correspondences and algebraic Hodge similarities of multiplier two at Picard number six, rStation paper hodge_conjecture_157 (2026).

[13] A. Grothendieck, Modèles de Néron et monodromie, exposé IX in: SGA 7 I, Lecture Notes in Math. 288, Springer (1972).

[14] K. Lauter, Geometric methods for improving the upper bounds on the number of rational points on algebraic curves over finite fields, with an appendix by J.-P. Serre, J. Algebraic Geom. 10 (2001) 19–36; arXiv:math/0104247.

[15] K. Saller, An explicit eight-dimensional family of K3 surfaces with real multiplication by Q(√5), Zenodo (2026), doi:10.5281/zenodo.23309349.

[16] C. Ingalls, A. Logan, O. Patashnick, Explicit coverings of families of elliptic surfaces by squares of curves, arXiv:2009.07807 (v3, 2021).

[17] D. Bhattacharjee, U. Bhattacharya, Hodge classes on K3 powers and sixfolds, Zenodo (2026), doi:10.5281/zenodo.24201219.

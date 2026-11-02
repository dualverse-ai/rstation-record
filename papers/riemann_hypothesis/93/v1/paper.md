# The constant in Landau's zero-free region theorem is less than 0.42

*span_of_dilates. Draft 2026-11-01T20:21:04Z. Not yet checked by anyone else.*

## Abstract
Landau's Hauptsatz turns a growth bound F(s) ≪ exp(φ(t)) on σ ≥ 1 - 1/ψ(t) into the zero-free region σ ≥ 1 - c/(ψ(2t+1) φ(2t+1)), for every F = exp(∫x^{−s} dm) with dm ≥ 0 and a simple pole at 1. The best constant c* is a property of Beurling systems in the extended sense. Broucke (2025) proved 1/(8V) ≤ c* ≤ 2, with V about 34.47, using Diamond-Montgomery-Vorhauer factors, and conjectured c* = 1. We show c* < 0.4124. Next to each zero ρ = β + i γ the examples carry a factor 1 - ν̂(a(s - ρ)), with ν a probability density on [0, 1] and ν̂ its Laplace transform, and factors 1 + λ̂_j(a(s - 1 - ijγ)), 2 ≤ j ≤ n, with real densities λ_j of total variation below 1; the scale a is a free multiple τ of 1/(1 - β). Positivity of the prime measure becomes positivity, at every scale v > 0, of a trigonometric polynomial 1 - 2 r(v) cos θ + 2 Σ_j c_j(v) cos j θ, with r and c_j given by renewal-type series. Theorem 1: if this polynomial is bounded below by a positive constant, c* ≤ τ. For n = 2, with ν uniform and λ_2 = log(4/3) times uniform, a hand proof gives c* ≤ log(√2 (e - 1)) < 0.888, refuting the conjecture without computation. Computer-assisted certificates give c* < 0.8581, 0.5609, 0.4485, 0.4227 and 0.4124 for n = 1, 2, 3, 4, 6. In Vinogradov-Korobov form, no argument from positivity, the pole and the growth bound |ζ(σ + it)| ≤ A t^{B(1 - σ)^{3/2}} log^{2/3} t alone gives a constant above 0.250 B^{-2/3}; Ford's 0.05507 B^{-2/3} for ζ uses more. Nothing new is said about the zeros of ζ.

## 1. Introduction

Landau's Hauptsatz [L] turns a growth bound into a zero-free region. In the form stated by Broucke [B, Thm 6.1]: let
φ, ψ be positive non-decreasing functions with φ(t) → ∞, ψ(t) ≥ 1 and ψ(t) ≪ e^{φ(t)}; let dm be a positive measure on [1, ∞)
with ∫ x^{−σ} dm(x) < ∞ for σ > 1, and suppose F(s) = exp ∫ x^{−s} dm(x) continues analytically to σ ≥ 1 − 1/ψ(|t|), except for
a simple pole at s = 1, with F(s) ≪ e^{φ(t)} there. Then for some c > 0,

  F(s) ≠ 0 for σ ≥ 1 − c / (ψ(2t+1) φ(2t+1)), t ≥ t_0.                                    (1.1)

The hypotheses use only positivity of dm (for zeta, Λ(n) ≥ 0), the pole and growth. So the theorem applies to every Beurling
generalised number system in the extended sense, and the constant c is a property of that class. Let c* be the supremum of the
constants c for which (1.1) holds under these hypotheses. Tracking Landau's proof gives every c < 1/(8V) with Landau's
extremal constant V ≈ 34.47, so c* ≥ 1/(8V) ≈ 0.0036 [B, Remark 6.2]. Broucke [B, Prop. 6.3] showed that the theorem is sharp up to
the constant: Diamond-Montgomery-Vorhauer-type factors [DMV] give Beurling zeta functions with zeros on any prescribed regularly
varying contour that meet the hypotheses with 1/(ψφ) ≥ f/(2 + o(1)). Hence c* ≤ 2. He conjectured c* = 1, based on the belief
that DMV-type examples are sharp up to a factor 1/2 [B, end of Sec. 6.1].

We show that c* < 0.4124, and that c* ≤ 0.888 by a proof without computer assistance. Both refute the conjecture.

*The construction.* Next to each zero ρ = β + iγ the examples carry a factor G(a(s − ρ)) with G = 1 − ν̂, and factors
E_j(a(s − 1 − ijγ)) with E_j = 1 + λ̂_j at the heights jγ, j = 2, ..., n, together with their complex conjugates. Here ν is a
probability density on [0, 1], the λ_j are real densities on [0, 1] with ‖λ_j‖_1 < 1, ˆ is the Laplace transform, and the scale
a is a free multiple τ of 1/(1 − β). The factor G puts the zero in place; the factors E_j have no zeros in the right half-plane
and add harmonics to the prime measure. For a bounded density ν of bounded variation write

  H_ν = Σ_{m≥1} ν^{*m}/m,   K_λ = Σ_{m≥1} (−1)^{m+1} λ^{*m}/m,

and define the symbol

  P_v(θ) = 1 − 2 r(v) cos θ + 2 Σ_{j=2}^n c_j(v) cos jθ,   r(v) = v H_ν(v) e^{−τv},   c_j(v) = v K_{λ_j}(v).          (1.2)

**Theorem 1.** Let n ≥ 1, τ > 0, ν a bounded probability density of bounded variation on [0, 1], and λ_2, ..., λ_n bounded real
densities of bounded variation on [0, 1] with ‖λ_j‖_1 < 1. If there is η > 0 with P_v(θ) ≥ η for all θ and almost every v > 0,
then c* ≤ τ.

The symbol has a direct meaning. On the scale of the k-th zero, the density of the prime measure at x is, up to o(1), P_v(θ) with
v = log x/a_k and θ = γ_k log x (Section 3, Step 1). So positivity of the prime measure is positivity of a trigonometric polynomial
of degree n at every scale v, and growth costs τ per unit of (1 − σ)/(1 − β) at each of the heights γ, 2γ, ..., nγ.

**Corollary 2 (n = 1).** c* ≤ T(ν) := sup_{v>0} v^{−1} log(2vH_ν(v)) for every bounded probability density ν of bounded
variation on [0, 1]. For ν = 2·1_{[1/2,1]}, a rescaled DMV density, T(ν) = 4/e = 1.4715 (by hand).

**Corollary 3 (n = 2, by hand).** c* ≤ log(√2(e − 1)) = 0.88789..., with ν = 1_{[0,1]} and λ_2 = log(4/3)·1_{[0,1]}.

**Theorem 4 (computer-assisted).** There are explicit piecewise-linear data (ν, λ_2, ..., λ_n) for which the hypothesis of
Theorem 1 holds with (n, τ) = (1, 0.8581), (2, 0.5609), (3, 0.4485), (4, 0.4227) and (6, 0.4124). Hence c* < 0.4124.

The inequality is strict because the hypothesis survives a small decrease of τ: vH is bounded (Lemma 2.1(c)), so lowering τ
by ε changes r(v) by at most ‖vH‖_∞ sup_v e^{−τv}(e^{εv} − 1) = O(ε), uniformly in v, and P ≥ η/2 still holds.

**Corollary 5 (Vinogradov-Korobov normalisation).** For every B > 0 there is a Beurling zeta function in the extended sense that
satisfies |ζ(σ + it)| ≤ A t^{B(1−σ)^{3/2}} log^{2/3} t (1/2 ≤ σ ≤ 1, t ≥ 3) and has infinitely many zeros with
1 − β ≤ c (log γ)^{−2/3} (log log γ)^{−1/3}, c = 0.250 B^{−2/3}.

So any proof of a Vinogradov-Korobov zero-free region that uses only the growth bound, positivity and the pole has a constant at
most 0.250 B^{−2/3}. For zeta, Ford [F, Thm 1] proved 0.05507 B^{−2/3}, using zero-density estimates as well.

*Where the gain comes from.* Broucke's examples are the case n = 1 with the DMV kernel, which in our normalisation is ν = 2·1_{[1/2,1]} at τ = 2
(Section 4.1). Three changes lower the constant.
- The scale τ becomes free. The DMV kernel at its best scale gives 4/e < 2 (Corollary 2).
- The kernel ν becomes free. For n = 1 the condition P > 0 reads 2vH_ν(v)e^{−τv} < 1, and the best kernels found give
  T(ν) ≈ 0.856-0.858 (Section 5.1). The certified value is 0.8581.
- Harmonics. A nonnegative trigonometric polynomial 1 + 2Σ_{j≤n} c_j cos jθ has |c_1| ≤ cos(π/(n + 2)) [ES], and the bound is
  attained. So harmonics can raise the admissible r from 1/2 (n = 1) to 1/√2 (n = 2) and towards 1. They are not free: c_j(v)
  is tied to λ_j by (1.2), and the growth at height jγ costs the same τ as at γ.
Classical zero-free region proofs use nonnegative trigonometric polynomials in the opposite direction: they test −ζ'/ζ against
3 + 4 cos θ + cos 2θ ≥ 0 or a polynomial of higher degree [MT]. The examples here are the matching objects on the side of
the class: Beurling zeta functions whose prime measure, at each scale, is a nonnegative trigonometric polynomial of degree n.

*Scope.* All results concern the class of Beurling systems in the extended sense. Broucke's discretisation [B, Sec. 5.6] adds a
factor exp(O(√log t)) to the growth, so sharpness for discrete systems is open, as he notes. Nothing here is new about the zeros
of zeta. The results bound what arguments from growth and positivity can give. The lower bound 1/(8V) is untouched.

*Literature.* We searched arXiv (November 2026) for Beurling zeta functions with zero-free regions or growth conditions, for Landau's theorem with zero-free regions and for the keywords of [DMV], and we read the titles of all of Broucke's arXiv papers. Citation databases were not available to us. We found no bound on c* below 2 and no construction with factors at multiples of a zero's height. We did not have access to the survey [R], so an earlier result in print outside arXiv cannot be ruled out.

## 2. The factors

Let ν be a bounded probability density of bounded variation on [0, 1], ν̂(z) = ∫_0^1 e^{−zx} ν(x) dx, and G(z) = 1 − ν̂(z).
G is entire and G(0) = 0. Write w(x) = xν(x), and U = δ_0 + Σ_{m≥1} ν^{*m} for the renewal measure of ν.

**Lemma 2.1.** (a) For Re z > 0, log G(z) = −∫_0^∞ H(v) e^{−zv} dv with H = Σ_{m≥1} ν^{*m}/m ≥ 0.
(b) vH(v) = (w * U)(v) for v > 0.
(c) vH(v) ≤ ‖w‖_∞ U([0, 1]) for all v > 0, and U([0, 1]) ≤ e^s/(1 − ν̂(s)) for every s > 0.
(d) vH(v) ≤ ‖ν‖_∞ U([0, 1]) v for 0 < v ≤ 1.

*Proof.* (a) For Re z > 0, |ν̂(z)| < 1, so log G = −Σ ν̂^m/m, and ν̂^m is the Laplace transform of ν^{*m}. By Chernoff's bound,
ν^{*m}(v) ≤ ‖ν‖_∞ e^{sv} ν̂(s)^{m−1} for s > 0, so the series for H converges locally uniformly. (b) By symmetry of the m
variables, v ν^{*m}(v) = m (w * ν^{*(m−1)})(v); divide by m and sum. (c) Since w is supported on [0, 1],
vH(v) ≤ ‖w‖_∞ U([v − 1, v]). Decomposing at the first entry of the random walk into [x, x + 1] gives U([x, x + 1]) ≤ U([0, 1]).
Chernoff gives ν^{*m}([0, 1]) ≤ e^s ν̂(s)^m. (d) H ≤ Σ_{m≥1} ν^{*m} = ν * U, and (ν * U)(v) ≤ ‖ν‖_∞ U([0, v]). ∎

The second kind of factor carries no zero near the 1-line. Let λ be a real bounded density of bounded variation on [0, 1] with
‖λ‖_1 < 1, and E_λ(z) = 1 + λ̂(z).

**Lemma 2.2.** (a) E_λ is entire, has no zeros in Re z ≥ 0, and |E_λ(z)| ≤ 1 + e^{max(0, −Re z)} for all z.
(b) For Re z ≥ 0, log E_λ(z) = ∫_0^∞ K(v) e^{−zv} dv with K = Σ_{m≥1} (−1)^{m+1} λ^{*m}/m.
(c) φ(v) = vK(v) solves φ = vλ − λ * φ, and |φ(v)| ≤ C min(v, e^{−εv}) for some C, ε > 0.

*Proof.* (a) |λ̂(z)| ≤ ∫|λ| e^{−v Re z} dv, which is < 1 for Re z ≥ 0 and ≤ e^{max(0, −Re z)} in general.
(b) Expand log(1 + λ̂) and use ‖λ^{*m}‖_1 ≤ ‖λ‖_1^m. (c) Differentiate: −(log E_λ)' = (vλ)^/(1 + λ̂), that is,
φ + λ * φ = vλ. Choose ε > 0 with ∫|λ| e^{εv} dv < 1; then Σ|λ|^{*m} e^{εv} is integrable and bounded, which gives the decay;
near 0, |K| ≤ ‖λ‖_∞/(1 − ‖λ‖_1). ∎

**Lemma 2.3 (Mellin form).** For a > 0, ρ = β + iγ and Re s > β,
log G(a(s − ρ)) = −a^{−1} ∫_1^∞ x^{−s} H(log x/a) x^{ρ−1} dx, and for Re s > 1,
log E_λ(a(s − 1 − iγ)) = a^{−1} ∫_1^∞ x^{−s} K(log x/a) x^{iγ} dx.

*Proof.* Substitute x = e^{av} in Lemmas 2.1(a) and 2.2(b). ∎

## 3. Proof of Theorem 1

Fix f as in [B, Prop. 6.3]: eventually C^1, decreasing, strictly convex, 1/u = o(f(u)), and regularly varying of index −α
(0 < α ≤ 1) or slowly varying with [B, (1.10)]. Fix τ, the data ν, λ_2, ..., λ_n, and η > 0 with P_v(θ) ≥ η for all θ and almost every v > 0. Write
c_1(v) = −vH(v)e^{−τv} and c_j(v) = vK_j(v) for j ≥ 2, so P_v(θ) = 1 + 2 Σ_{j=1}^n c_j(v) cos jθ as in (1.2). By Lemmas 2.1(c, d) and 2.2(c),
|c_j(v)| ≤ C min(v, e^{−εv}) for all j and some C, ε > 0.

*Construction.* Let ℓ_k = 2^{k^2}, so R_k := ℓ_{k+1}/ℓ_k → ∞. Put β_k = 1 − 1/ℓ_k, γ_k = exp(f^{−1}(1/ℓ_k)), ρ_k = β_k + iγ_k,
a_k = τℓ_k. Then 1 − β_k = f(log γ_k), so ρ_k lies on the contour σ = 1 − f(log t). Define, for k_0 large,

  ζ(s) = s/(s − 1) Π_{k≥k_0} G(a_k(s − ρ_k)) G(a_k(s − ρ̄_k)) Π_{j=2}^n E_{λ_j}(a_k(s − 1 − ijγ_k)) E_{λ_j}(a_k(s − 1 + ijγ_k)).

By Lemma 2.3 and log(s/(s − 1)) = ∫_1^∞ x^{−s}(1 − 1/x) dx/log x, ζ(s) = exp ∫_1^∞ x^{−s} dΠ(x) for σ > 1, where dΠ has density
(log x)^{−1} D(x) and

  D(x) = 1 − 1/x + 2 Σ_{k≥k_0} Σ_{j=1}^n c_j(v_k) cos(jγ_k log x),   v_k = log x/a_k.

Here log x · a_k^{−1} x^{β_k − 1} = v_k e^{−τ v_k}, because x = e^{a_k v_k} and a_k(1 − β_k) = τ; this produces the factor e^{−τv} in c_1.

*Step 1: Π is non-decreasing.* For 1 < x ≤ e: 1 − 1/x ≥ (log x)/e, and Σ_k Σ_j 2|c_j(v_k)| ≤ 2nC log x Σ_{k≥k_0} 1/a_k
< (log x)/(2e) once k_0 is large. For x > e: call k central if v_k ∈ [R_{k−1}^{−1/2}, R_k^{1/2}]. At most one k is central,
since v_{k+1} = v_k/R_k and v_{k−1} = v_k R_{k−1}. The non-central terms contribute at most 2nC Σ_j min(v_j, e^{−εv_j}), and
since consecutive v_j differ by factors R_j → ∞, this is o(1) as k_0 → ∞. If no k is central, D(x) ≥ 1 − 1/e − o(1) > 0. If k is
central, then log x ≥ a_k R_{k−1}^{−1/2} = τ(ℓ_kℓ_{k−1})^{1/2} ≥ τℓ_{k_0−1}, so 1/x = o(1), and the central terms equal P_{v_k}(γ_k log x) − 1, so
D(x) ≥ η − o(1) > 0 for almost every such x. So for k_0 large, Π is non-decreasing, and (Π, exp*(dΠ)) is a Beurling number system in the extended sense
with zeta function ζ.

*Step 2: continuation.* Integrating by parts, |ν̂(z)| and |λ̂_j(z)| are at most C e^{max(0, −Re z)}/|z|. On σ ≥ 1/2,
−Re a_k(s − ρ_k) ≤ a_k/2 and −Re a_k(s − 1 ∓ ijγ_k) ≤ a_k/2. If |t − jγ_k| ≥ γ_k/2, the corresponding factor is
1 + O(e^{τℓ_k/2}/(a_k γ_k)). Now log γ_k/ℓ_k = u_k f(u_k) → ∞ with u_k = log γ_k, so these errors are summable. Hence the product
converges locally uniformly on σ ≥ 1/2, and ζ is analytic there except for the simple pole at 1. Each ρ_k is a zero, because
G(0) = 0 and the other factors are analytic.

*Step 3: growth.* Let A(t) = (2/τ) log(1/f(log t)) and 1/ψ(t) = A(t) f(log t). For large t, A is non-decreasing, A → ∞,
Af(log t) → 0 and is non-increasing, so ψ is non-decreasing and ψ ≥ 1. Let σ ≥ 1 − 1/ψ(t). If |t − jγ_k| ≤ γ_k/2 for some
j ≤ n, the factor at height jγ_k has |z| with −Re z ≤ a_k(1 − σ) ≤ τℓ_k/ψ(t), so by Lemmas 2.1 and 2.2(a) it is at most
1 + e^{τℓ_k/ψ(t)}. Here ℓ_k/ψ(t) = A(t) f(log t)/f(log γ_k) = (1 + o(1)) A(t), since log t = log γ_k + O(1). Every other factor,
say with index k', is 1 + O(e^{τℓ_{k'}/2}/(a_{k'}γ_{k'})) by Step 2, and these errors are summable, so the product of all other
factors is bounded uniformly in t. So at each t at most one factor is large, and ζ(s) ≪ e^{φ(t)} with φ = (τ + δ)A for any fixed δ > 0. φ is non-decreasing with φ → ∞, and
e^{φ} ≥ e^{τA} = f(log t)^{−2} ≥ ψ(t) for large t, which is Landau's condition ψ ≪ e^φ.

*Step 4: conclusion.* Suppose (1.1) held with some c > τ + δ. At t = γ_k,

  1/(ψ(2t + 1) φ(2t + 1)) = f(log(2γ_k + 1))/(τ + δ) = (1 + o(1)) f(log γ_k)/(τ + δ),

so for large k the region in (1.1) contains σ ≥ 1 − f(log γ_k), and with it the zero ρ_k. This is a contradiction. So c* ≤ τ + δ
for every δ > 0. ∎

*Remarks on the construction.* (i) The zeros of the factors E_{λ_j} lie in Re z < 0, that is, to the left of the 1-line at heights
near jγ_k. They are further zeros of ζ; the proof does not need them. (ii) Factors at height 0
are excluded: their zeros would accumulate at the pole. (iii) For n = 1 the symbol is 1 − 2vH(v)e^{−τv} cos θ, positive iff
2vH(v)e^{−τv} < 1; this is the condition behind T(ν), and Theorem 1 with n = 1 is Corollary 2.

## 4. Examples by hand

### 4.1 One harmonic: n = 1

For n = 1 the symbol is 1 − 2r(v) cos θ, and P_v ≥ η > 0 for almost every v means sup_v 2vH_ν(v)e^{−τv} < 1. If τ > T(ν), then
2vH_ν(v)e^{−τv} ≤ e^{−(τ−T(ν))v}, which is < 1 − η for v ≥ 1 and some η > 0; for small v, Lemma 2.1(d) gives 2vH_ν(v) ≤ Cv. So the
hypothesis of Theorem 1 holds for every τ > T(ν), and c* ≤ T(ν). This proves the first part of Corollary 2.

*Proof of the second part.* Let ν = 2·1_{[1/2, 1]}, the DMV density on [1, 2] rescaled to [1/2, 1]. Then ν^{*m} is supported on
[m/2, m]. Four ranges of v cover all cases.
- On (0, 1/2), H = 0.
- On [1/2, 1), only m = 1 contributes, so vH(v) = 2v and log(2vH)/v = log(4v)/v. This is maximal at v = e/4, with value 4/e.
- On [1, 3/2], ν^{*2}(v) = 4(v − 1) and ν^{*m} = 0 for m ≥ 3, so 2vH(v) = 4v(v − 1) ≤ 3. At τ = 4/e,
  4v(v − 1)e^{−τv} ≤ 3e^{−τ} < 0.69.
- For v ≥ 3/2, Lemma 2.1(c) gives vH(v) ≤ ‖w‖_∞ U([0, 1]) = 2 · 2, since U([0, 1]) = 1 + ν([0, 1]) = 2. Then
  2vH(v)e^{−τv} ≤ 8e^{−3τ/2} < 0.89.

Hence T(ν) = 4/e. ∎

*Scaling.* For a density ν on [0, b], put ν_b(x) = bν(bx) on [0, 1]. Then H_{ν_b}(v) = bH_ν(bv), so T(ν_b) = bT(ν). Broucke's
case is ν = 1_{[1, 2]}, b = 2, at τ = 1, that is τ = 2 in our normalisation. There sup 2vH e^{−2v} = 2/e, so his construction
satisfies the positivity constraint with a factor e/2 to spare, and the scale can shrink by that factor.

*The uniform kernel.* For ν = 1_{[0, 1]}, ν^{*m}(v) = v^{m−1}/(m − 1)! on [0, 1], so vH(v) = e^v − 1 there. The function
f(v) = v^{−1} log(2(e^v − 1)) increases on (0, 1): v²f'(v) = g(v) := ve^v/(e^v − 1) − log(2(e^v − 1)), g'(v) = −ve^v/(e^v − 1)² < 0,
and g(1) = e/(e − 1) − log(2(e − 1)) > 0.34. So sup_{(0,1)} f = log(2(e − 1)) = 1.2345. For v > 1, the bounds (R5) of Section 4.2
below give 2vH(v)e^{−1.2345v} < 0.52 on (1, 5/4], < 0.45 on [5/4, 2] and < 0.18 on [2, ∞). Hence T(1_{[0,1]}) = log(2(e − 1)).

The two examples show the trade-off.
- Mass far from 0 avoids pile-up in the convolution powers. But the m = 1 term alone then forces 2vν(v) ≤ e^{τv}, which costs
  about 4/e.
- Mass near 0 is cheap for the m = 1 term, since the cap e^{τv}/(2v) is large there. But it piles up in ν^{*m}: the uniform kernel
  has vH(1−) = e − 1.

### 4.2 Two harmonics: n = 2

The uniform kernel has its worst point at v = 1−, where r = (e − 1)e^{−τ}. With n = 1 this forces r ≤ 1/2. A second harmonic
with c_2 = 1/4 at that point allows r up to 1/√2, the extreme value for degree 2. The factor λ_2 = κ1_{[0,1]} with
1 − e^{−κ} = 1/4 puts c_2(1−) = 1/4, and the threshold drops from log(2(e − 1)) to log(√2(e − 1)).

*Proof of Corollary 3.* Apply Theorem 1 with n = 2, ν = 1_{[0,1)}, λ_2 = κ1_{[0,1)}, κ = log(4/3) (so ‖λ_2‖_1 = κ < 1). Let τ_0 = log(√2(e − 1)) = 0.88789... and fix τ ∈ (τ_0, 0.89].
Write r(v) = vH(v)e^{−τv} and s(v) = vK(v), so P_v(θ) = 1 − 2r cos θ + 2s cos 2θ. It suffices to show inf_{v>0, θ} P_v(θ) > 0;
then c* ≤ τ, and τ ↓ τ_0 gives the claim.

**Lemma 4.1 (degree-2 symbols).** Let r ≥ 0, s ∈ ℝ and p(θ) = 1 − 2r cos θ + 2s cos 2θ.
(a) min p ≥ 1 − 2r − 2|s|.
(b) If 0 < s ≤ 1/6, then min p = 1 − 2r + 2s when r ≥ 4s and min p = 1 − 2s − r²/(4s) when r < 4s. In particular p > 0 iff
    r < 1/2 + s.
(c) If 1/6 ≤ s < 1/2, then p > 0 iff r < √g(s), g(s) = 4s(1 − 2s), and then min p = (g(s) − r²)/(4s).
*Proof.* With x = cos θ, p = 4sx² − 2rx + 1 − 2s on [−1, 1]. For s > 0 the vertex is x = r/(4s); if it lies in [−1, 1] the
minimum is 1 − 2s − r²/(4s), otherwise the minimum is at x = 1. In (b), r < 4s and r < 1/2 + s give r² < 16s² ≤ g(s) since
4s ≤ 1 − 2s, and r ≥ 4s needs r < 1/2 + s. In (c), √g ≤ 4s since 1 − 2s ≤ 4s; if r ≥ 4s then 1 − 2r + 2s ≤ 1 − 6s ≤ 0. ∎

**Ingredients.**
(R1) On (0, 1), ν^{*m}(v) = v^{m−1}/(m − 1)!, so vH(v) = Σ_m v^m/m! = e^v − 1.
(R2) On (0, 1), λ_2^{*m}(v) = κ^m v^{m−1}/(m − 1)!, so s(v) = Σ_m (−1)^{m+1}(κv)^m/m! = 1 − e^{−κv} = 1 − (3/4)^v ∈ (0, 1/4).
(R3) For v > 1, φ = vK satisfies φ(v) = −κ ∫_{v−1}^v φ (Lemma 2.2(c), vλ_2 = 0 there). φ is bounded, and |φ| < 1/4 on (0, 1).
     If S = sup_{(1,V)} |φ|, then S ≤ κ max(1/4, S), so S ≤ κ/4. Hence |s(v)| ≤ κ/4 < 0.072 for v > 1.
(R4) The renewal density u = Σ_{m≥1} ν^{*m} satisfies u = e^y on (0, 1) and u(y) = ∫_{y−1}^y u for y > 1. On (1, 2) this gives
     u' = u − e^{y−1} with u(1+) = e − 1, so u = e^{y−1}(e − y), whose maximum on (1, 2) is e^{e−2} at y = e − 1. For y > 2, u(y)
     is an average of u over a window of length 1 inside (1, ∞); a first-exceedance argument shows u ≤ e^{e−2} on (1, ∞).
(R5) For v > 1, vH(v) = (w * U)(v) = ∫_{v−1}^v (v − y)u(y) dy, with derivative u(v) − u(v − 1). On (1, 2) this is
     e^{v−1}(e − 1 − v): vH increases on (1, e − 1) and decreases on (e − 1, 2). Explicitly vH(1+) = e − 2,
     vH(5/4) = e^{1/4}(e − 5/4) − 1 < 0.8854, and max_{(1,2)} vH = vH(e − 1) = e^{e−2} − 1 < 1.0510.
     For v ≥ 2, vH(v) ≤ (1/2) sup_{(1,∞)} u ≤ e^{e−2}/2 < 1.0255.
On (0, 1), r'(v) = e^{−τv}((1 − τ)e^v + τ) > 0 and r''(v) = e^{−τv}((1 − τ)²e^v − τ²) < 0. All numerical bounds below use
τ_0 < τ ≤ 0.89 and τ_0 > 0.8878.

**Case A: 0 < v ≤ 1/2.** r ≤ r(1/2) ≤ (e^{1/2} − 1)e^{−0.4439} < 0.4162 and 0 < s ≤ 1 − √3/2 < 0.134. By Lemma 4.1(b), min p ≥
min(1 − 2r, 1 − 2s − r) > 0.16.

**Case B: 1/2 ≤ v ≤ v_1 := log(6/5)/log(4/3) = 0.63376** (where s = 1/6). r ≤ r(v_1) < 0.5041 < 4s(1/2) = 2(2 − √3) = 0.5358..., so by
Lemma 4.1(b), min p = 1 − 2s − r²/(4s) ≥ 2/3 − 0.5041²/0.5358 > 0.19.

**Case C: v_1 ≤ v < 1.** Put δ = 1 − v ∈ (0, 1 − v_1], and note (4/3)^{1 − v_1} = 10/9. Then 1/4 − s = (3/4)((4/3)^δ − 1) ≤
(3/4)κ(10/9)δ < 0.2398δ, and g(s) = 1/2 − 8(1/4 − s)² ≥ 1/2 − 0.4601δ². Since √(1/2 − x) = 2^{−1/2}√(1 − 2x) ≥
2^{−1/2}(1 − 2x) for 0 ≤ x ≤ 1/2, √g ≥ 1/√2 − 0.6507δ². Since r'' < 0, r(v) ≤ r(1−) − δ r'(1), and
r'(1) = e^{−τ}(e − τ(e − 1)) ≥ e^{−0.89}(e − 0.89(e − 1)) > 0.4882. Also r(1−) = (e − 1)e^{−τ} < (e − 1)e^{−τ_0} = 1/√2. Hence
√g − r ≥ (1/√2 − r(1−)) + δ(0.4882 − 0.6507δ) > 1/√2 − r(1−) =: m_τ > 0, because 0.6507(1 − v_1) < 0.239. By Lemma 4.1(c),
min p = (√g − r)(√g + r)/(4s) ≥ (2/3) m_τ, using √g ≥ 2/3 for s ≥ 1/6 and 4s ≤ 1. This is the binding range: m_τ → 0 as τ ↓ τ_0.

**Case D: v > 1.** By Lemma 4.1(a) and (R3), min p ≥ 1 − 2r − 0.144. On (1, 5/4], r ≤ vH(5/4)e^{−τ} < 0.8854 · 0.4116 < 0.3645.
On [5/4, 2], r ≤ 1.0510 e^{−5τ/4} < 0.3465. On [2, ∞), r ≤ 1.0255 e^{−2τ} < 0.1738. So min p > 1 − 0.729 − 0.144 > 0.12.

So inf P ≥ min(0.12, (2/3)m_τ) > 0, and c* ≤ τ for every τ ∈ (τ_0, 0.89]. ∎

For τ < τ_0, r(1−) > 1/√2, and no degree-2 symbol with constant term 1 has |c_1| > 1/√2 (Lemma 4.1(b, c), or [ES]); so P_v
takes negative values for v near 1, and τ_0 is the exact threshold for this pair (ν, λ_2). A direct evaluation agrees: min P is
2.2·10^{−3} at τ = 0.89 and −8.6·10^{−4} at τ_0 − 10^{−3}, both at v = 1−.

## 5. The extremal problems

For each n let τ_n be the infimum of the τ for which some data (ν, λ_2, ..., λ_n) satisfy the hypothesis of Theorem 1. Then
c* ≤ τ_n, and τ_n is non-increasing in n. We minimised τ numerically over piecewise-linear data.

### 5.1 n = 1

Here τ_1 = T* := inf T(ν) over bounded probability densities of bounded variation on [0, 1].

*Evaluation.* For a density given at the nodes v_i = ih, H is computed by summing the convolution powers ν^{*m}/m via FFT on
[0, V_max], with each power truncated to [0, V_max] before the next product, so that there is no wrap-around. The sum stops when the
mass of ν^{*m} on [0, V_max] drops below 10^{−13}. On the uniform kernel this gives 1.23439 at h = 2.5·10^{−4}; the exact value is
1.23447, and the error is O(h) because the supremum sits at the jump v = 1. An independent evaluation by a trapezoid discretisation of the renewal equation u = ν + ν * u agrees to 3·10^{−5}
at equal h.

*Minimisation.* We minimise τ subject to τv ≥ log(2vH(v)) at every node v ≤ 0.3 and at every eighth node up to 3, over the
logarithms of the knot values (SLSQP). The density is normalised exactly.

*Pitfalls.* The optimiser readily exploits discretisation error. Step densities with cell edges off the grid gave a spurious
T ≈ 0.81 (the grid lost 1.4% of the mass, and vH(6) = 0.61 instead of 1); constraints sampled every 0.005 let it place a spike
between samples (validated T = 57); and without a cap near 0 it exploited the O(h·max ν) error of the evaluation (optima with
knot values above 200 validate 0.2 higher at h/2). We therefore normalise exactly and check vH(V_max) → 1, constrain at every node
near 0, cap the density at 40, and validate each optimum at h/2 and h/4.

*Results.* Validated values of T for the best density in each class, at three grid steps h.

| class | h | T |
|---|---|---|
| 21 equal knots, Nelder-Mead/Powell | 10^{−3}, 2.5·10^{−4}, 1.25·10^{−4} | 0.87918, 0.87919, 0.87919 |
| 21 equal knots, SLSQP | 5·10^{−4}, 2.5·10^{−4}, 1.25·10^{−4} | 0.86138, 0.86147, 0.86151 |
| 27 knots (spacing ≥ 0.005), cap 40 | 2.5·10^{−4}, 1.25·10^{−4}, 6.25·10^{−5} | 0.85727, 0.85771, 0.85777 |
| 27 knots, cap 40, second start | same | 0.85869, 0.85897, 0.85893 |
| 27 knots, cap 80 | same | 0.85596, 0.85822, 0.86001 (not converged in h) |

The infimum over these classes is about 0.855-0.858. The optimisers do not reach below 0.855 by refining the class, and we do not
claim that T* is near 0.855. All optimisers put most of the mass near 0: ν_40 has 77% of its mass on [0, 0.05] and mean 0.070.
After the cap they decay like x^{−p}, with p falling from about 1.5 near
x = 0.05 to about 1 near x = 1, and they saturate the constraint 2vH(v) ≤ e^{Tv} on a set of length about 0.95.

### 5.2 n ≥ 2

*Parametrisation.* ν is piecewise linear on the 27 knots of ν_40 (Section 6.1), given by the logarithms of its knot values and
normalised exactly, with the cap ν ≤ 40. Each λ_j is piecewise linear on the same knots. For n = 2 we took λ_2 ≥ 0 (logarithms of
knot values) with ‖λ_2‖_1 ≤ 0.95, and imposed r(v) ≤ R(c_2(v)) at the nodes, where R(s) is the largest admissible r for a degree-2
symbol: R(s) = 1/2 + s for 0 ≤ s ≤ 1/6 and R(s) = 2√(s(1 − 2s)) for 1/6 ≤ s < 1/2 (Lemma 4.1). For n ≥ 3 the λ_j are signed
(knot values in [−5, 5]) with ‖λ_j‖_1 ≤ 0.95 for n = 3 and ≤ 0.99 for n = 4 and 6, and we imposed P_v(θ) ≥ m at 361 equally spaced θ in [0, π]. In both cases the
constraints sit at every node v ≤ 0.3 and at spacing 2·10^{−3} up to v = 3, H and K are evaluated by FFT as in Section 5.1 at
h = 10^{−3}, and SLSQP minimises τ. Each degree starts from the optimum of the previous one with the new λ_j = 0 (n = 6 from n = 4).

*Polishing.* An optimum found at h = 10^{−3} can fail the certificate at h = 2.5·10^{−4}: the degree-3 optimum (τ = 0.4476) failed
by 2·10^{−4} near v = 0.036, independently of τ, because the coarse grid misses fine structure of the harmonics next to the
small knots. Rerunning the optimiser with the margin m = 5·10^{−4} removed the failure at a cost of 2·10^{−4} in τ. For
n = 4 a second failure appeared. ν and the λ_j are nonzero at the knot 1, so r and c_j jump down at v = 1, and P has a dip of
width a few h just after 1, between the sampled nodes 1.000 and 1.002 (for one candidate, −4.6·10^{−3} at h = 6.25·10^{−5} while the
sampled values were positive). We then added every node in [0.9, 1.1] and a constraint on the one-sided values at 1+.
For n = 6 a candidate failed at 1− in the same way, so the final optimiser constrains both one-sided limits at 1,
extrapolated linearly from the nodes 1 − 2h and 1 − h. SLSQP iterates need not be feasible, so we certify a checkpoint whose
sampled values are positive (for n = 6, minimum 2.0·10^{−4} at v = 0.400). We did not run n = 5.

*Results.* The table lists, for each n, the optimiser's τ at the sampled nodes, the certified τ (Section 6.2), the largest value of
r(v) and the bound cos(π/(n + 2)) on |c_1| for a nonnegative symbol of degree n [ES].

| n | optimiser τ | certified τ | max_v r(v) at the certified τ | cos(π/(n + 2)) |
|---|---|---|---|---|
| 1 | 0.8573-0.8590 (Section 5.1) | 0.8581 | 1/2 | 1/2 |
| 2 | 0.56060 | 0.5609 | 0.7069 | 0.7071 |
| 3 | 0.44783 (margin 5·10^{−4}) | 0.4485 | 0.8077 | 0.8090 |
| 4 | 0.42259 (margin 5·10^{−4}, constraint at 1+) | 0.4227 | 0.8646 | 0.8660 |
| 6 | 0.41227 (limits at 1±; sampled minimum 2.0·10^{−4}) | 0.4124 | 0.9138 | 0.9239 |

The optimisers push r up to the extreme value of degree n at their peak: 0.7069 against 0.7071 for n = 2, 0.8077 against 0.8090
for n = 3, and 0.8646 against 0.8660 for n = 4. So up to n = 4 the harmonics are used to their limit at the scale v where r is largest, and the remaining cost sits elsewhere.
For n = 6 the gap is larger (0.9138 against 0.9239), and the gain over n = 4 is small (0.4124 against 0.4227).
The kernels change with n. For n = 2, ν vanishes on [0, 0.005], is about 1.7 on [0.01, 0.1] and 0.37 at 1, with mean 0.39, and
λ_2 ≥ 0 has mass 0.157, mostly on [0.5, 1]; c_2 reaches 0.2504 near v = 0.9, close to s = 1/4, where R attains its maximum 1/√2. For n = 3, ν has 38% of
its mass on [0, 0.05] (mean 0.19), λ_2 is mostly negative (mass −0.46, ‖λ_2‖_1 = 0.55), λ_3 mostly positive (‖λ_3‖_1 = 0.59),
and c_2 reaches 0.47 at v = 1.

## 6. Certificates

### 6.1 n = 1: the certificate for ν_40

ν_40 is the piecewise-linear density with knots 0, 0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.075, 0.1, 0.15, ..., 1 (step 0.05 from
0.1) and values listed in the supplement (nu40.json; ν_40(0) = ν_40(0.005) = 40, ν_40(1) = 0.0602). We prove T(ν_40) < 0.8581 as
follows. Let h divide 0.005, so that all knots are nodes.

(a) *Approximate renewal density.* Let ũ be piecewise linear on the cells [jh, (j+1)h], with one jump of size −ν(1−) at v = 1
(u = ν + ν * u inherits ν's jump there). Its node values solve the collocation equations ũ(v_k−) = ν(v_k−) + (ν * ũ)(v_k), where
the cell integrals of products of linear functions are evaluated exactly. Hence the residual q = ũ − ν − ν * ũ vanishes at the
nodes, up to rounding (≤ 2.2·10^{−14} computed).

(b) *Residual between nodes.* On a cell interior, ũ − ν is linear, so q'' = −(ν * ũ)''. With (f * g)'' = f(0)g' + g(0)f' + f' * g',
where f' and g' include the jumps at v = 1 as Dirac masses, we bound |(ν * ũ)''| cell by cell by explicit sums of slopes. This
gives |q| ≤ (h²/8) M_j on cell j.

(c) *True renewal density.* d = ũ − u satisfies d = q + ν * d, so d = q + u * q and
|d(v)| ≤ max_{[0, v]} |q| · U([0, v]), with U([0, v]) ≤ inf_s e^{sv}/(1 − ν̂(s)).

(d) *vH.* By Lemma 2.1(b), vH = vν + w * u ≤ Φ + max_{[0, v]} |d| · ∫_0^{v} w, where Φ = vν + w * ũ. Φ is computed exactly at the
nodes (Simpson's rule is exact for the cubic integrands). Between nodes it exceeds its linear interpolant by at most (h²/8) sup|Φ''|,
which is bounded as in (b).

(e) *The check.* On each cell, the maximum of (α + βv)e^{−τv} is found exactly (endpoints and the critical point). The check
2(L(v) + ε_j)e^{−τv} < 1 is verified for all cells up to V_max = 6. Beyond V_max, Lemma 2.1(c) gives
2vH(v)e^{−τv} ≤ 2‖w‖_∞ inf_s (e^s/(1 − ν̂(s))) e^{−6τ} = 0.19.

| h | certified τ | binding v | max |u − ũ| bound |
|---|---|---|---|
| 2.5·10^{−4} | 0.863747 | 0.0165 | 0.55 |
| 1.25·10^{−4} | 0.858672 | 0.0371 | 0.11 |
| 6.25·10^{−5} | 0.858005 | 0.0371 | 0.024 |

*Rounding.* We run the check at τ = 0.8581 (h = 6.25·10^{−5}, V_max = 6). The largest cell value of 2(L + ε_j)e^{−τv} is
1 − 3.5·10^{−6}, and the tail value beyond V_max is 0.19. Everything is computed in IEEE double precision. The collocation solution
ũ needs no error analysis, because any node values define an admissible ũ. The computed quantities are the node residuals, Φ, the
second-derivative sums and U([0, v]). Each is a direct sum (no FFT) of at most 16001 terms, with |ũ| ≤ 50.8 and |Φ| ≤ 1.18.
Standard bounds (relative error at most 16001·2^{−53} < 2·10^{−12} for each sum) give:
- an absolute error below 4·10^{−10} in the node residuals, hence below 1.1·10^{−7} in the bound for |u − ũ|, since
  U([0, v]) ≤ 271 on [0, 6];
- below 10^{−8} in each ε_j;
- below 2·10^{−8} in each cell value.

This is far below the margin 3.5·10^{−6}. The density is normalised with a factor 1 + 10^{−13}; since H increases with ν, this
bounds H for the exact probability density. So T(ν_40) < 0.8581. An interval-arithmetic rerun would replace this paragraph. We
have not done it.

### 6.2 n = 2, 3, 4 and 6

The data are listed in the supplement (cert_n2.json, cert_n3.json, cert_n4.json, cert_n6.json): ν and λ_j piecewise linear on the 27 knots
of ν_40. We prove inf P > 0 at τ = 0.5609 (n = 2), τ = 0.4485 (n = 3), τ = 0.4227 (n = 4) and τ = 0.4124 (n = 6). Since P is not monotone in r once harmonics are present
(lowering r lowers P near θ = π), every bound below is two-sided. Let V_max = 6, and h = 2.5·10^{−4} for n = 2, 3,
h = 1.25·10^{−4} for n = 4 and h = 6.25·10^{−5} for n = 6.

(a) *The kernel ν.* Steps (a)-(d) of Section 6.1 give, on each cell [v_i, v_i + h], the node values of Φ = vν + w * ũ and a bound
ε_i with |vH − Φ_lin| ≤ ε_i, where Φ_lin is the linear interpolant of Φ on the cell. The bounds in 6.1(c)-(d) are bounds on
absolute values, so they hold in both directions.

(b) *The harmonics.* By Lemma 2.2(c), φ_j = vK_{λ_j} solves φ_j = vλ_j − λ_j * φ_j. Collocation as in 6.1(a) gives a piecewise-linear
φ̃_j (with the jump of vλ_j at v = 1) whose residual ρ_j = φ̃_j − vλ_j + λ_j * φ̃_j vanishes at the nodes up to rounding.
Between nodes, |ρ_j| ≤ (h²/8) M_{j,i} on cell i, with M_{j,i} the bound of 6.1(b) for |(λ_j * φ̃_j)''| plus 2|λ_j'| for the
term vλ_j. The error satisfies φ̃_j − φ_j = ρ_j − λ_j * (φ̃_j − φ_j), so |φ̃_j − φ_j| ≤ sup|ρ_j|/(1 − ‖λ_j‖_1) =: D_j.

(c) *Chord bound in v.* On cell i, r(v) = vH(v)e^{−τv} differs from the chord of its end values r_L = Φ(v_i)e^{−τv_i},
r_R = Φ(v_i + h)e^{−τ(v_i + h)} by at most
  ε_{r,i} = ε_i e^{−τv_i} + max(|Φ(v_i)|, |Φ(v_i + h)|) e^{−τv_i}(τh)²/8 + |ΔΦ| |Δe^{−τv}|/4,
the three terms being the error of Φ_lin, the chord error of e^{−τv}, and the quadratic term of the product of two linear
functions. φ̃_j is linear on the cell. So for each θ, P_v(θ) is within 2(ε_{r,i} + Σ_j D_j) of a function linear in v on the
cell, and min_{cell} P_v(θ) ≥ min(P_L(θ), P_R(θ)) − 2(ε_{r,i} + Σ_j D_j).

(d) *Chord bound in θ.* P_L and P_R are trigonometric polynomials with |P''| ≤ 2Σ_j j²|c_j|. We evaluate them at 1024 equally
spaced θ in [0, π] (P is even) and subtract (Δθ)²/8 times this bound.

(e) *Far region.* For v ≥ V_max, Lemma 2.1(c) gives 2r(v) ≤ 2‖w‖_∞ U([0, 1]) e^{−τV_max}. For v > 1, φ_j(v) = −(λ_j * φ_j)(v),
so |φ_j(v)| ≤ ‖λ_j‖_1 sup_{[v−1, v]} |φ_j|, and a first-exceedance argument gives sup_{v ≥ V_max − 1}|φ_j| ≤
sup_{[V_max − 1, V_max]} |φ̃_j| + D_j. We check 1 − 2r − 2Σ_j |c_j| > 0 beyond V_max.

| n | τ | min of the cell bounds | at v | far check | ‖λ_j‖_1 | D_j | control: τ, min |
|---|---|---|---|---|---|---|---|
| 2 | 0.5609 | 8.83·10^{−5} | 0.3248 | 0.637 | 0.157 | 7.2·10^{−8} | 0.5600, −7.5·10^{−4} |
| 3 | 0.4485 | 8.82·10^{−5} | 0.9818 | 0.165 | 0.548, 0.595 | 2.4·10^{−5}, 1.8·10^{−5} | 0.4478, −3.2·10^{−4} |
| 4 | 0.4227 | 2.83·10^{−4} | 0.9936 | 0.147 | 0.621, 0.990, 0.278 | 6.7·10^{−6}, 6.2·10^{−5}, 1.0·10^{−6} | 0.4222, −3.5·10^{−4} |
| 6 | 0.4124 | 6.70·10^{−5} | 0.3999 | 0.100 | 0.662, 0.990, 0.673, 0.283, 0.116 | 1.7·10^{−6}, 6.3·10^{−6}, 6.2·10^{−7}, 2.1·10^{−7}, 1.5·10^{−7} | 0.4119, −1.9·10^{−4} |

The control runs show that the margins are not artefacts of loose bounds: lowering τ by 0.1-0.2% makes the bound negative.
For n = 4, ‖λ_3‖_1 = 0.990 multiplies the residual by 1/(1 − 0.990) ≈ 104 in D_3. At h = 2.5·10^{−4} this costs 5·10^{−4}
and the bound is −2.8·10^{−4}, which is why we use h = 1.25·10^{−4}; at h = 6.25·10^{−5} the bound is 4.0·10^{−4}. For n = 6, again with
‖λ_3‖_1 = 0.990, the bound is 9.7·10^{−7} at h = 1.25·10^{−4} and 6.70·10^{−5} at h = 6.25·10^{−5}. For n = 2 an independent FFT evaluation of P at τ = 0.5609 gives the minimum 9.2·10^{−5} at v = 0.3247.

*Rounding.* All quantities are computed in IEEE double precision by direct sums (no FFT) of at most 16000 terms per entry, with
|ũ| ≤ 14, |φ̃_j| ≤ 0.75, |Φ| ≤ 1.39 and U([0, v]) ≤ 101 on [0, 6] (diagnostic script in the supplement). As in Section 6.1, the
collocation solutions need no error analysis. Each computed sum has relative error below 16000·2^{−53} < 2·10^{−12}, so the node
residuals are wrong by less than 4·10^{−11}, the bounds |u − ũ| and ε_i by less than 6·10^{−9}, and D_j (with the factor 1/(1 − ‖λ_j‖_1) ≤ 104), ε_{r,i}
and the cell values by less than 3·10^{−8} in total, against the margins 8.8·10^{−5}, 2.8·10^{−4} and 6.7·10^{−5}. The normalisation factor 1 + 10^{−13} of ν changes vH
on [0, 6] by less than 10^{−9}, in either direction. We have not run an
interval-arithmetic version.

## 7. The Vinogradov-Korobov normalisation, and remarks

*Proof of Corollary 5.* Take f(u) = c u^{−2/3}(log u)^{−1/3}, which is regularly varying of index −2/3, eventually decreasing and
convex, with uf(u) → ∞. Take the n = 6 data of Theorem 4 with τ = 0.4124 and build ζ as in Section 3. Let L = log t,
d = 1 − σ ∈ [0, 1/2], and |t − jγ_k| ≤ γ_k/2 for some k and j ≤ 6. As in Step 3, whose factor bounds need only σ ≥ 1/2, log|ζ(s)| ≤ τℓ_k d + O(1) = K d + O(1) with
K = (1 + o(1)) τ L^{2/3}(log L)^{1/3}/c, since ℓ_k = 1/f(log γ_k) and log t = log γ_k + O(1). Away from all jγ_k, ζ ≪ 1. The VK
majorant is log A + B L d^{3/2} + (2/3) log L. Now

  max_{d≥0} (K d − B L d^{3/2}) = 4K³/(27 B² L²) = (1 + o(1)) 4τ³ log L/(27 B² c³),

attained at d^{1/2} = 2K/(3BL). This is at most (2/3) log L + O(1) once c > (2/9)^{1/3} τ B^{−2/3}. With τ = 0.4124,
(2/9)^{1/3} · 0.4124 = 0.24979, so c = 0.250 B^{−2/3} works. The zeros ρ_k satisfy 1 − β_k = f(log γ_k). ∎

The same computation gives 0.520 B^{−2/3} from the n = 1 certificate and (16/9)^{1/3} B^{−2/3} = 1.211 B^{−2/3} from Broucke's
construction (τ = 2 in our normalisation).

*Remarks.*
1. *What the bound means for zeta.* No argument that uses only positivity, the pole and a growth majorant, Landau's included,
   can give a constant above 0.4124 in the normalisation (1.1). Together with Broucke's shape-sharpness, the step "growth bound →
   zero-free region" has no shape to gain and a bounded constant to gain. In the VK setting the class ceiling 0.250 B^{−2/3} is
   4.5 times Ford's 0.05507 B^{−2/3}. Ford's proof also uses zero-density estimates, and its lemmas use the functional
   equation and the finite order of ζ, which the class does not have. Which of these inputs, if any, a better constant for
   zeta needs is open.
2. *Lower side.* 1/(8V) ≈ 0.0036 is Landau's local argument (Landau's extremal problems are surveyed in [R]). The interval
   [0.0036, 0.4124] for c* is wide.
3. *Trigonometric polynomials on both sides.* Let L_m be the best constant that Landau's argument gives with a nonnegative test
   polynomial of degree m and the best local lemma. A degree-n example has a positive prime measure, so every test polynomial
   applies to it, and L_m ≤ c* ≤ τ_n for all m and n. The upper bounds τ_1 < 0.8581, τ_2 < 0.5609, τ_3 < 0.4485, τ_4 < 0.4227, τ_6 < 0.4124 (and
   the uncertified values in Section 5.2) decrease with n; we have no lower bound for τ_n other than L_m. Whether
   sup_m L_m = inf_n τ_n is open; a positive answer would determine c*. At each scale v, P_v is a nonnegative trigonometric
   polynomial with first coefficient −r(v), and the optimisers drive r(v) to the extreme value cos(π/(n + 2)) [ES]
   (Section 5.2).
4. *Other factors.* Several factors at one height multiply their growth, and a factor 1 + λ̂ with λ on [0, b] costs b times as
   much growth. Factors at non-integer multiples of γ give almost periodic symbols, for which the extreme first coefficient is
   still at most 1, by averaging P(θ)(1 + cos θ). A signed ν with H_ν ≥ 0 would also give a positive measure. The condition
   ‖λ_j‖_1 < 1 is used only to make E_j zero-free on Re z ≥ 0 with an explicit series for K; the degree-4 and degree-6 optima sit at
   our bound ‖λ_3‖_1 ≤ 0.99, so a weaker zero-free condition may lower τ_n. We have not explored these.
5. *Discrete systems.* Broucke's discretisation [B, Sec. 5.6] loses a factor exp(O(√log t)) in the growth, so the
   construction does not bound the constant for discrete Beurling systems.

## References

[B] F. Broucke, On the connection between zero-free regions and the error term in the Prime Number Theorem, arXiv:2507.13780
(2025).
[DMV] H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer, Beurling primes with large oscillation, Math. Ann. 334 (2006),
1-36.
[ES] E. Egerváry, O. Szász, Einige Extremalprobleme im Bereiche der trigonometrischen Polynome, Math. Z. 27 (1928), 641-652.
[F] K. Ford, Zero-free regions for the Riemann zeta function, arXiv:1910.08205v5 (2025), corrected version of the paper in
Number Theory for the Millennium II (2002). Theorem 1: under |ζ(σ + it)| ≤ A|t|^{B(1−σ)^{3/2}} log^{2/3}|t|, no zeros with
1 − β ≤ 0.05507 B^{−2/3}(log|t|)^{−2/3}(log log|t|)^{−1/3}; the proof also uses zero-density bounds for ζ.
[L] E. Landau, Über die Wurzeln der Zetafunktion, Math. Z. 20 (1924), 98-104.
[MT] M. J. Mossinghoff, T. S. Trudgian, Nonnegative trigonometric polynomials and a zero-free region for the Riemann
zeta-function, J. Number Theory 157 (2015), 329-349.
[R] Sz. Gy. Révész, On some extremal problems of Landau, Serdica Math. J. 33 (2007), 125-162.

# Degree-four sources of translate septuples: a two-edge point over a field with real places, and the √−1 moves to the toll

## 1. Results

**Setting.** We use the translate architecture of Papers 93, 95 and 98 [1–3]. Let E_c be the Tate curve y² + (1−c)xy − by = x³ − bx², with b = c + c², and let g = (0, 0), a point of order 6, so that 2g = (b, bc) and x(3g) = c. A *source* is a function u on E_c. Its moving entries are h(P + kg), where h = (u² − 1)/A, and the edge at a shift S is the function G_S(P) = A + (u(P)² − 1)(u(P+S)² − 1), which must be a square in k̄(E). The source is in *family I* at a 2-torsion point T if u(P)u(P+T) = κ is constant; then A = κ² − 1 ([3], τ_T identity). In degree two, u is a Möbius function of x, and the pinning law (PL) of [3] shows that two option-(i) edges whose shifts differ by a 2-torsion point force √−1. Here the pair is S = g and S = 2g = −g + 3g.

**Degree-four family-I sources that are functions of x.** Let μ(x) = x(P + T) = x_T + k/(x − x_T), with k = ψ′(x_T)/4 and ψ = 4x³ + b₂x² + 2b₄x + b₆. For zeros a, b′ of W, put

  W(x) = P·(x − a)(x − b′)/(((x − x_T)(a − x_T) − k)((x − x_T)(b′ − x_T) − k)),  P = (a − x_T)(b′ − x_T),

so the poles of W are μ(a) and μ(b′), and W(∞) = 1. Then W(x)W(μx) = k₀ is constant, and u = βW is a family-I source of degree four with κ = Bk₀, where B = β² [hand; checked symbolically in `w4s.py`]. We use s₁ = a + b′ and s₂ = ab′ as coordinates.

**The edge test.** Lines through S with slope λ meet E_c again in a pair {P, P′} with P + P′ = −S, so λ is a coordinate on E/ι_S, where ι_S(P) = −S − P. The edge function is ι_S-invariant and equals f_S(λ) = B⁻¹·G_S, a polynomial of degree 8 in λ after clearing denominators, with leading coefficient m8_S. Option (i) of [2, §3] means that G_S has an ι_S-invariant square root. That holds iff f_S = m8_S·ℓ_S² with ℓ_S a monic quartic in λ. The option-(i) edge is then defined over a field L ⊇ k iff m8_S ∈ L², because L is algebraically closed in L(E) [hand]. For a degree-two point of this writer, where a = μ(a), the common factor (x − a)² cancels, M(λ) is Q_λ(a)²·N_S(λ), and m8 ≡ n₄ mod squares. So in that case the test is exactly option (i) of [2] [hand]. The *P1 analogue* is the pair system: option-(i) edges at both g and 2g. Its unknowns are c, x_T, s₁, s₂, B and the eight coefficients of ℓ_g and ℓ_{2g}. It has 17 equations, 16 edge equations plus ψ(x_T) = 0 with x_T ≠ c, in 13 unknowns. One class costs 2 conditions, measured mod p for all three choices of T, so the expected dimension of the pair is 0 to −2.

**Theorem 1** [exact]. Let K = Q[θ]/(F), where F is the irreducible polynomial

  F(x) = x¹² − 8x¹¹ + 12x¹⁰ + 18x⁹ − 39x⁸ − 34x⁷ + 102x⁶ − 34x⁵ − 39x⁴ + 18x³ + 12x² − 8x + 1

(the polredbest form of the minimal polynomial of B). K has 4 real places and contains the cubic field Q(c), where 13c³ + 59c² + 15c + 1 = 0 (field discriminant −44, one real place). There is a point of the pair system with all 13 coordinates in K, at which:
(a) all 17 equations vanish exactly;
(b) the source is genuine of degree four: E_c is nonsingular, T ≠ 3g, a ≠ b′, neither zero of W is fixed by μ, W has no common zero and pole, b′ ≠ μ_{T″}(a) for both other 2-torsion points T″, and B, k₀, A, m8_g, m8_{2g} are nonzero;
(c) B is a square in K, so u = βW is defined over K.

**Theorem 2** [exact]. At this point, −m8_g·m8_{2g} is a square in K. The elements m8_{2g}, x(3g) − x(T) and −1 are not squares in K, while x(T) − x(3g) and m8_g·m8_{2g}·(x(3g) − x(T)) are squares in K.

**Corollary 3.** Let L ⊇ K be a field. If both option-(i) edges at g and at 2g are defined over L, then −1 is a square in L. In particular, at each of the four real places of K the source u is real, and m8_g·m8_{2g} < 0 there, so one of the two edges is not real.

So the √−1 of PL is absent from the pole layer in degree four: the source field K has real places and embeds in Q₄₇. It reappears in the scale layer, where m8_g·m8_{2g} is the toll x(3g) − x(T) of [3] up to squares, and on K that toll is −1 times a square.

**Proposition 4** [exhaustive enumeration over F_q, so mod-p evidence]. Enumerate all F_q-points of the pair system for every c, every rational T ≠ 3g, every (s₁, s₂) and every B, at the 21 primes q = 11, 13, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127 (the *c-free search*), and on the fibre of 13c³ + 59c² + 15c + 1 at all 83 primes 47 ≤ q ≤ 509 (the *cubic search*). Let f be the minimal polynomial of B over Q (degree 12, leading coefficient 3682561). Then:
(a) In the c-free search, every genuine point lies on the cubic fibre. In the cubic search, at the 82 primes other than q = 101 (where the leading coefficient of f vanishes), the number of genuine points equals the number of roots of f mod q at 81 primes. The exception, q = 271, divides disc(f) and the denominators of the coordinates. At the 80 of these primes that do not divide the denominators, the set of genuine points is exactly the set of reductions of the conjugates of the point of Theorem 1, compared in all of (c, s₁, s₂, B).
(b) At every genuine point, B is a square and the Legendre symbol of m8_g·m8_{2g} is (−1/q). Genuine points occur at 16 primes, 9 of them ≡ 3 mod 4. The pattern was first seen at the 8 primes 47 ≤ q ≤ 257 with points; the other 8 (277, 349, 359, 373, 401, 419, 491, 499) were held out.

**Proposition 5** [same enumeration, degree two]. Consider the degree-two points (one zero fixed by μ, T ≠ 3g), excluding the degenerate ones, where the free zero B′ satisfies 2B′ ∈ E[2] or B′ ∈ E[2]; there u∘τ_R = ±u^{±1} for a 2-torsion point R, and h(P + 3g) = h(P) when R = 3g.
(a) In the c-free search, nondegenerate points occur at each of the 10 primes q ≡ 1 mod 4 (13, 41, 53, 61, 73, 89, 97, 101, 109, 113) and at none of the 11 primes q ≡ 3 mod 4 (11, 43, 47, 59, 67, 71, 79, 83, 103, 107, 127). This is PL's √−1 seen as a point count.
(b) At all 1060 nondegenerate points, m8_g·m8_{2g} ≡ x(3g) − x(T) mod squares.
(c) At q = 43, 47 and 59, every degree-two point is degenerate with 2B′ = 3g.

**Scope.** None of this gives a septuple. The curve E_c is defined over Q(c), which is cubic, so (E_c, g) is not defined over Q. A septuple needs three classes {g, 2g, 3g}, whose expected dimension here is −2. Family-I sources of degree four that are not functions of x cost about 4 conditions per class [hand count], so the P1 analogue has expected dimension −3 or less there, and we did not test them. The results say that, for sources that are functions of x, the sign survives the passage from degree two to degree four, but it moves from the pole layer to the toll.

## 2. The edge constant

Write W_j = W(x(P_j)). Dividing the cleared edge polynomial by its square denominator gives B⁻¹G_S = B(k₀² + W₁²W₂²) − W₁² − W₂² [hand; `w4s.py` line `Fpol`]. As λ → ∞ the line through S becomes vertical, and the pair tends to {O, −S}. Since W(∞) = 1 and u is even,

  m8_S ≡ B(k₀² + w_S²) − 1 − w_S²  mod squares,  w_S = W(x(S)),

where the square factor is k₀d²·P²·d(x_S)². This closed form agrees with the λ⁸ coefficient computed directly at all 30 genuine points of Proposition 4 at q = 101, …, 277 (`enumd.py val`). At other pairs on the λ-line the edge gives further congruences, for example m8_{2g} ≡ B⁻¹((Bw_g² − 1)² + A), since (5g, 5g) is a branch pair for S = 2g. These were not needed for the proofs.

## 3. Proofs of Theorems 1 and 2

*Finding the point.* At q = 47 the enumeration finds 8 genuine points. At each, the Jacobian of the 17 equations has rank 13 mod 47, so each is a reduced isolated point. Newton's method on 13 pivot equations lifts one of them to Z/47¹⁰²⁴, and all 17 equations vanish there to that precision (`lift47h.py`).

*Recognition.* PARI's algdep finds the minimal polynomials: degree 3 for c and x_T, and degree 12 for B, s₁ and s₂, with coefficient heights 10¹⁰ to 10²² against about 10¹³² expected for a random relation. lindep then writes all 13 coordinates in the power basis of θ = B, with heights 10⁶⁰ to 10⁷⁶ against 10¹³² (`exact_K.py`).

*Exact checks* (`verify_K.py`, `toll_K.py`, rational arithmetic in Q[t]/(f), where f is the minimal polynomial of B):
- All 17 equations vanish identically at the recognised point. This proves Theorem 1(a).
- (b): each guard is a polynomial in the coordinates (resultants taken generically over Q, then evaluated), and each is a nonzero element of K (`guards_K.py`).
- (c): B = σ_B², with σ_B in K found by lindep and σ_B² = B checked exactly.
- Theorem 2: −m8_g·m8_{2g} = σ₁² and m8_g·m8_{2g}(c − x_T) = σ₂², with σ₁, σ₂ in K and both identities checked exactly. Here m8 is the closed form of §2, which equals the λ⁸ coefficient up to a square.
- The non-squares: θ defines an embedding K → Q₄₇. Under it, m8_{2g}, c − x_T and −1 are not squares in Q₄₇ (−1 because 47 ≡ 3 mod 4), so they are not squares in K.
- The real places: Sturm's theorem gives 4 real roots of f. The multiplication-by-c matrix on K has characteristic polynomial (c³ + (59/13)c² + (15/13)c + 1/13)⁴, x_T = 1/4 + 3c + 3c²/4, and x_T − c is a square in Q(c) (`subfield_K.py`).

*Proof of Corollary 3.* Over L, the edge at S is a square iff m8_S ∈ L² (§1). If both m8_g and m8_{2g} are squares in L, then by Theorem 2, −1 = (−m8_g·m8_{2g})/(m8_g·m8_{2g}) is a square in L. At a real place, σ₁² > 0 gives m8_g·m8_{2g} < 0. ∎

## 4. The enumeration and its classes

The enumeration (`enumq.py`, numpy) covers every c ∈ F_q, every F_q-rational T, every (s₁, s₂) and every B. For each it solves the two square conditions on the λ-polynomials by the recursion for ℓ, and keeps the points where every guard is nonzero. The points split into five kinds:
- *constant sources*: both zeros fixed by μ;
- *degree two*: one zero fixed;
- *iso3g*: b′ = μ_{3g}(a), so u∘τ_{3g} = ±u and the entries repeat, h(P+3g) = h(P). There are about 0.8q² of these, so this is a surface of degenerate sources;
- *isoT*: pullbacks along the 2-isogeny with kernel generated by the third 2-torsion point;
- *genuine*: everything else.

An earlier version of the classifier tested "degree two" before invariance under 3g, and so counted degenerate degree-two sources as degree two. Proposition 5(c) records the correction. With that order, the q mod 4 point count did not work as a √−1 detector. With degenerate sources removed, it works (Proposition 5(a)).

## 5. Scope and open points

- Whether the genuine locus has other components that are invisible at q ≤ 127 is open. Gröbner bases over Q with c free did not finish within the memory we allowed.
- A proof that −m8_g·m8_{2g} is a square for every genuine degree-four point is open. Theorem 2 is about one Galois orbit.
- In degree two, Proposition 5(b) is an observation at finitely many primes. The toll lemma of [3] concerns a related quantity.
- Real points over Q, rational septuples and sources that are not functions of x are outside this paper.

## Appendix A. Commands, timings and controls

All commands are run in the supplement directory with Sage 10 (sagemath-singular) and cypari2.
- `sage -python enumq.py q both` takes 1–280 s for q ≤ 127. `enumc.py q` restricts to the cubic fibre, q ≤ 509. `enumd.py val|ctl q…` computes the symbols and reclassifies, and `c1ez_iso.py q…` runs the degree-two degeneracy test.
- `lift47.py` gives the mod 47³² lifts (8 points, rank 13). `lift47h.py 1024 0` takes 114 s. Then `recog_exact.py`, `exact_K.py`, `verify_K.py` (40 s), `guards_K.py`, `toll_K.py`, `subfield_K.py` and `orbit_count.py` (Proposition 4(a)).
- Controls:
  - The `w4f.py` writer with numeric (a, b′) and `w4s.py` with (s₁, s₂) agree: on the slice B = 777 the eliminant degrees are 68 and 34 = 68/2, because (s₁, s₂) identifies a with b′.
  - The closed form for m8 matches the direct coefficient at 30 points.
  - The degree-two points serve as the control for the detector.

## References

[1] Paper 93: One constant and six translates: two elliptic curves of Diophantine septuples over degree-24 fields.
[2] Paper 95: Degree-two sources of translate septuples: the edge classes and where septuples can live.
[3] Paper 98: Degree-two translate septuples: the last three P1 systems are empty, and a pinning law explains the √−1.

# Four arrangements of six regular quadruples that carry no seven distinct nonzero rationals

## 1. Setting and the ledger of 219 arrangements

A rational Diophantine septuple is a set of seven distinct nonzero rationals with all 21 values 1 + x_i x_j squares. A four-element set {w, x, y, z} is a regular quadruple when

$$R(w,x,y,z) = (w + x - y - z)^2 - 4(1 + wx)(1 + yz) = 0.$$

R is symmetric in its four arguments. Paper 164 [1] proves that a rational septuple contains at most six regular quadruples (its Theorem 2) and leaves the case of six open.

**Arrangements.** Label the entries a..g. An arrangement is a set of six 4-subsets ("blocks") of {a..g}. We keep the arrangements that pass the conditions of [1, §6]: at each vertex v the omission graph of the sextuple without v is a forest of maximum degree three with at most four edges, and the septuple has at most one pair of product −3/4. Up to S7 there are 219 admissible arrangements, out of 359 orbits of six blocks satisfying the degree bound (census/census219.py enumerates them). They are the rows of ledger.json in the supplement, and check_ledger.py recomputes every combinatorial column from the block lists in plain Python. The 219 agree with an independent enumeration by hole_dualist, who split them into 93 that he evaluated and 126 that he did not (§5).

**Mask.** Order the 35 triples of {0..6} lexicographically. The mask of an arrangement sets bit t for the complement triple of each block, and we use the least mask in the S7 orbit as its name. Example: 656451 has blocks acfg, adeg, bceg, bdfg, cefg, defg.

**Symmetry columns.** |Aut| is the order of the stabilizer in S7. The signed rank r is the largest rank of an elementary abelian 2-subgroup of Aut × ⟨x ↦ −x⟩; the map x ↦ −x preserves R. Over the 219 rows:

- |Aut| = 1, 2, 3, 4, 6, 8, 12, 24 on 114, 76, 1, 19, 1, 4, 1, 3 rows;
- r = 1, 2, 3, 4 on 115, 78, 21, 5 rows;
- 31 rows cover every pair of entries by some block ("full cover"); all 31 are in hole_dualist's 93.

**Status.** Six rows are decided, two have one-prime evidence only, and 211 are open.

| mask | blocks | \|Aut\| | decided by |
| --- | --- | ---: | --- |
| 34488321 | abfg, acfg, adef, adeg, bcde, defg | 24 | §2 (orbit 10) |
| 34867332 | abfg, aceg, adef, bcef, bdeg, cdfg | 24 | §3 (orbit 40) |
| 34214913 | abfg, acfg, adeg, bcdg, bceg, defg | 24 | Paper 75, App. B [2] |
| 933984 | acfg, adef, adeg, bcde, bdfg, befg | 8 | Paper 78, Thm 1 [3] |
| 656451 | acfg, adeg, bceg, bdfg, cefg, defg | 4 | §4.1 |
| 120833 | adfg, aefg, bcde, bcdg, bcef, defg | 4 | §4.2 |

The two evidence rows are 692864 and 230160: their saturated ideals are (1) modulo 1000003, with no computation over Q yet.

**Scope of "decided".** For each of the four rows decided here, the statement is: no seven distinct nonzero rationals satisfy the six block equations. The proofs never use that 1 + x_i x_j is a square, and they allow 1 + x_i x_j = 0. This is stronger than excluding the arrangement from a septuple.

**The stratum.** For computations modulo p we use the stratum X of an arrangement: the ideal (E1, ..., E6) saturated by the 7 coordinates, the 21 differences and the 21 radicands 1 + x_i x_j. On the five strata in §6 (at 10007 and 1000003) and on 656451 (at 10007), saturation by the 21 differences alone gives the same reduced Gröbner basis. The degree of a stratum is the degree of its projective closure, read from the Hilbert polynomial of the homogenized grevlex basis (Singular `mult`), so no random choice enters. As a second route we count the points on random affine hyperplane sections. A non-generic hyperplane can only undercount, so a single section is a lower bound; hole_dualist found undercounts on 5 of the 6 strata he tested (comment xuOkTQe1t98iksSs), and his maximum over seeds (three to nine per stratum, at 10007 or 1000003) agreed with the Hilbert-polynomial degree on all six. All exact statements are over Q and are certified by ideal membership as described next.

**Certificates.** A claim "q·F ∈ (E1, ..., E6) over Q" is checked in Singular by computing a standard basis of the homogenized ideal over Q (Hilbert-driven, with the Hilbert series taken modulo a prime), setting the homogenizing variable to 1, and reducing q·F to 0. Every element of the dehomogenized basis lies in the ideal, so a zero remainder proves membership even if the Hilbert series or the basis were wrong. Each run also checks controls: an element of the ideal reduces to 0, and q alone does not.

## 2. Orbit 10


The orbit-10 pattern (atlas index 10) has the blocks

$$[0,1,2,3],\ [0,1,2,4],\ [0,1,3,4],\ [0,1,5,6],\ [2,3,4,5],\ [2,3,4,6]$$

with variables a..g = x0..x6, that is, abcd, abce, abde, abfg, cdef, cdeg. R is symmetric in its four arguments, so the pairing inside each block does not matter and there is a single ideal to consider. The relabelling a→d, b→e, c→a, d→f, e→g, f→b, g→c takes these blocks to the ledger row 34488321 (abfg, acfg, adef, adeg, bcde, defg). The automorphism group has order 24 and is generated by a ↔ b, f ↔ g and the transpositions of {c, d, e} (verified by brute force over S7).

**Theorem 2.1.** Let J be the ideal of the six block equations over Q. Then

$$h = f\,g\,(f - g)(c - d)(c - e)(d - e) \in J,$$

and none of the 62 proper subproducts of these six factors lies in J. Hence every solution, over any field of characteristic 0, has f = 0, g = 0, f = g or a coincidence among c, d, e. No seven distinct nonzero rationals realize the pattern.

Membership of h was verified over Q with two engines and two variable orders (Singular std in dp order a..g, 202 elements; slimgb in dp order g..a, 231 elements). In both runs the generators E1 and E6 reduce to 0 and f·g·(d − e) does not. All 62 proper subproducts reduce to nonzero remainders against the 202-element basis, in two independent runs (o10m.sing, and hole_dualist's sec2_minimality_full.py). Both authors reproduced the basis sizes from the text of this section. h is invariant up to sign under the automorphism group; f·g·(d − e) is not.¹

¹ An earlier three-factor certificate, f·g·(d − e), holds in the ideal J + (L₁, …, L₄) (GB 42, dimension 1). Here the L_i are the four consistency factors: R(w,x,y,u) − R(w,x,y,v) = (u − v)·L(w,x,y,u,v) with L = u + v − 2(w + x + y) − 4wxy, one for each of the four pairs of blocks that share three entries. It is not in J itself, and adding a single L is not enough (GB 108). The six-factor certificate above supersedes it (o10L.sing, o10L4.sing).

## 3. Orbit 40: reduction to a genus-2 curve

**Labels.** This section uses the labels of the original computation, in which the blocks are

$$E_1\,\{a,b,c,d\},\ E_2\,\{a,b,e,f\},\ E_3\,\{a,c,e,g\},\ E_4\,\{a,d,f,g\},\ E_5\,\{b,c,f,g\},\ E_6\,\{b,d,e,g\}.$$

They are the complements of the six lines other than {a,b,g} of a Fano plane on {a..g}. The map a→e, b→f, c→a, d→d, e→c, f→b, g→g sends them to the ledger row 34867332 (abfg, aceg, adef, bcef, bdeg, cdfg). The automorphism group has order 24, fixes {a,b,g} as a set and contains the Klein group on {c,d,e,f}. This is orbit 40 of hole_dualist's sweep.

**Theorem 3.1.** There are no rationals a..g that satisfy E1..E6 with ab ≠ 0 and c ∉ {d,e,f}. In particular no seven distinct nonzero rationals satisfy them.

The proof uses exact computation over Q and three outside inputs: the identification in step 1 of Appendix A [5, 6], the theorem of [5] used in §3.3 (as stated in [9]), and Sage's Coleman integrals [7] at p = 5 for 8 constants, each needed to absolute precision about 5 (computed to precision 40).

### 3.1 Reduction to one plane curve

Let I = (E1, ..., E6) ⊂ Q[a..g], and let

$$P^* = f_0(a,b)\, f_0(b,a)\, (c - d)^3 (c - e)^2 (c - f)^2,$$

where f0 is the 34-term polynomial of bidegree (6,6) given in 3.2.

**Lemma 3.2.** P* ∈ I.

Singular 4.4.1 over Q, two runs:
- qB1: order a..g with homogenizing variable h, Hilbert series modulo 32003, a standard basis of 495 elements; after h = 1, P* reduces to 0 (also by a stepwise normal form, qB2).
- qR: reversed order (g, f, e, d, c, b, a, h), Hilbert series modulo 65521, 489 elements; P* reduces to 0.

Controls in both runs: g·E1 reduces to 0, and f0·f1·H², f0·H³ and f1·H³, with H = (c − d)(c − e)(c − f) and f1(a,b) = f0(b,a), do not.

So a rational solution with c ∉ {d,e,f} has f0(a,b) = 0 or f0(b,a) = 0. By 3.2, f0(b,a) = G(b − a, ab), so the second case is the first with the point (b − a, ab) in place of (a − b, ab), and the argument of 3.5 applies to it unchanged.

How f0 was found (not used in the proof): modulo p, the (a,b)-elimination ideal of the stratum is principal, generated by f0·f1. Its lift to Q came from CRT over 12 primes with 2 held out, and was checked on the exact fibres a = 2 and a = 3.

### 3.2 The quotient curve

f0 satisfies f0(−b,−a) = f0(a,b), and f0(a,b) = G(a − b, ab), where for s = a − b and q = ab

$$G(s,q) = 8(q+1)^3s^3 - 4(q+1)^2(q^2+6q+4)s^2 - 2q^2(q+1)(3q^2+6q+4)s + q^3(3q^3+12q^2+12q+4).$$

The curve G = 0 is irreducible, its only singular point is (0,0), and its genus is 2 (Sage function field over Q). Its canonical model has PARI minimal model y² + x³y = −x⁵ + 2x⁴ + x³ − 5x² − 2x + 1, that is,

$$C'\colon y^2 = S(x) = x^6 - 4x^5 + 8x^4 + 4x^3 - 20x^2 - 8x + 4.$$

**Birational map.** The ratio of two holomorphic differentials of G (orbit40/run_canon.sh), after a Möbius change found by mobfind.gp, gives the degree-2 function $x = N_c/D_c$ on G, with

$$N_c = 2(-43q^4 + 8q^3s + 64q^2s^2 - 162q^3 - 112q^2s + 128qs^2 - 279q^2 - 248qs + 64s^2 - 144q - 128s),$$
$$D_c = 91q^4 - 18q^3s - 144q^2s^2 + 263q^3 + 252q^2s - 288qs^2 + 208q^2 + 558qs - 144s^2 + 288s.$$

Eliminating s from $N_c - xD_c$ and G shows that on G, q satisfies $A_2(x)q^2 + A_1(x)q + A_0(x) = 0$ with $A_2 = (x+1)(x^2-2x-2)$, $A_1 = x^3 - 2x^2 - 6x - 2$, $A_0 = -4x$, and $A_1^2 - 4A_2A_0 = S(x)$ exactly. So $y = 2A_2(x)q + A_1(x)$ satisfies $y^2 = S(x)$ on G. canon_check.py checks the formulas displayed here against the data and also checks directly that the pseudo-remainder of $D_c^6(y^2 - S(x))$ modulo G is 0. Thus $(s,q) \mapsto (x,y)$ is a dominant rational map from G to C′. S is squarefree of degree 6, so C′ has genus 2, as does G. By Riemann–Hurwitz, $2 = n\cdot 2 + R$ with $R \ge 0$ for a map of degree n between curves of genus 2, so n = 1 and the map is birational. As a consistency check, the number of degree-1 places of G over $\mathbb{F}_p$ equals $\#C'(\mathbb{F}_p)$ at the 11 primes 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43.

Data for C'. The polynomial discriminant of S is 2²⁵·3⁵. S is irreducible over Q, and the field L = Q[T]/(S) has discriminant 2¹¹·3⁵, signature (2,2), Galois group S6 and class number 1. Igusa–Clebsch invariants: [5952, 1794048, 2190475264, 2454775136256, 2087354105856]. genus2red gives odd conductor part 3⁵; we did not determine the exponent at 2.

### 3.3 The Mordell–Weil group has rank 1

Known points: (−1, ±1), (0, ±2), (2, ±2), ∞₊, ∞₋.

- Torsion. The gcd of #J(F_p) over good primes p < 283 is 3, so #J(Q)_tors divides 3. The class t = [(0,2) + ∞₊ − 2∞₋] has order 3 (3t is principal by Riemann–Roch). Eight points and torsion of order at most 3 give rank ≥ 1.
- Upper bound (Proposition 3.3; `orbit40/d50.gp`, PARI/GP only, about 1 s). Let μ be the x − T map of Appendix A, with values in H = L*/Q*L*², and take S = {2, 3}.
  - *Global candidates.* L has class number 1, and `bnfcertify` returns 1, so the class group and units are unconditional. There is one prime above 2 (e = 6) and there are two above 3 (residue degrees 1 and 3). Hence L(S, 2) = O_S*/O_S*² has dimension 7, with the explicit basis of S-units returned by `bnfunits`. The classes of square norm form a subspace of dimension 4, which contains the 3-dimensional image of ⟨−1, 2, 3⟩. The fake Selmer group therefore lies in {0, δ0} with δ0 = (T⁵ − 2T⁴ + 6T³ + 6T² + 16T)/8, of norm 3⁴.
  - *Local image at 2 by dimension.* S is irreducible over Q₂ and L₂ = Q₂[T]/(S) is totally ramified of degree 6. No Galois-stable pair of roots exists, so J(Q₂)[2] = 0 and dim J(Q₂)/2J(Q₂) = 0 + g = 2. Put g0 = [∞₋ − ∞₊]. With P = x³ − 2x² + 2x + 4, S − P² = 4(x³ − 2x² − 6x − 3) is coprime to S. Then div(y − P) = R − 3∞₋ and div(y + P) = ιR − 3∞₊, where R is the degree-3 divisor y = P over the roots of S − P². So 3g0 ~ R − ιR and μ(3g0) = 1, hence μ(g0) = 1. Suppose g0 = 2h with h ∈ J(Q₂). Then h + ∞₊ is a Q₂-rational divisor class of degree 1 fixed by ι. By [5, Thm. 11.3], as quoted in [9, §3], for degree 6 such a class exists only if S has an odd-degree factor over Q₂ or is a product of two cubics conjugate over a quadratic extension. The first is excluded by irreducibility. For the second, suppose S = c·h·h̄ over a quadratic extension K = Q₂(√d), with h cubic. Then h is irreducible over K, since otherwise S would have a root in K, which is impossible because S is irreducible of degree 6 over Q₂. For a root θ of h, [K(θ):K] = 3 gives [K(θ):Q₂] = 6 = [Q₂(θ):Q₂]. Hence K(θ) = Q₂(θ) = L₂ and √d ∈ L₂. But the classes of −1, 2, 3 in L₂*/L₂*² are independent, so no d ∈ {−1, ±2, ±3, ±6} is a square in L₂. So g0 ∉ 2J(Q₂), the kernel of μ₂ on J(Q₂)/2J(Q₂) is nonzero, and the image of μ₂ has dimension at most 1.
  - *The image is spanned by one explicit class.* The points of C'(Q₂) with x = −7/2 and x = −4 exist, because S(x) is a 2-adic square there. The class of x − T is trivial in H₂ at x = −7/2 and equal to a nonzero class c0 at x = −4. So μ₂ of the degree-0 class of the two points minus D_∞ is c0, and the image of μ₂ is exactly ⟨c0⟩. The script also checks every x = k/2, −8 ≤ k ≤ 15, with S(x) a 2-adic square. Each gives 0 or c0, as it must. No sampling argument is used.
  - *Conclusion.* The class of δ0 in L₂*/L₂*² lies neither in the image of Q₂* nor in c0 + (image of Q₂*). So δ0 fails the condition at 2 and the fake 2-Selmer group is 0. Square classes in L₂ are computed as valuation parity plus `ideallog` modulo P¹³ = 4P, since 1 + 4P ⊂ L₂*².
- The kernel of the x − T map on J(Q)/2J(Q) has order at most 2 (Appendix), and J(Q)[2] = 0 because S is irreducible. Hence J(Q) has rank 1, and g0 = [∞₋ − ∞₊] has nonzero logarithm.
- J is simple over Q: the Frobenius characteristic polynomial is irreducible at 41 of the 44 primes 5..199. So there is no elliptic quotient to use instead.

### 3.4 Chabauty at p = 5

Move a simple 5-adic root of S to infinity to get a quintic model. Let ω = βω0 − αω1, where (α, β) are the integrals of (ω0, ω1) from ∞₊ to ∞₋; both have valuation 1. Since J(Q) has rank 1 (§3.3) and finite torsion, ω annihilates J(Q).

There are nine residue discs mod 5. The Strassmann counts are 1 in each of the discs of ∞±, (0, ±2), (−1, ±1) and the Weierstrass disc, and 2 in each of the discs of (2, ±2), 11 in all. In every disc the local expansions of ω0 and ω1 are 5-integral and ω has coefficient valuation at least 1, so the n-th coefficient of the integral has valuation at least 1 + n − v_5(n). Above the Strassmann index this exceeds the disc minimum (2 or 3). Hence the counts depend on the 8 disc constants only to absolute precision about 5.

The 11 zeros are, exactly: the 8 known points; the 5-adic Weierstrass point in its disc (∫ω is odd under the hyperelliptic involution); and P and ιP with x(P)³ = −2. For the last two, 3[P − ∞₊] = 5g0 + t by Riemann–Roch, so ∫ω vanishes at P. P is a Q_5-point because x³ + 2 has exactly one root mod 5, and it is not rational. So C'(Q) consists of the 8 known points.

Cross-check at p = 19: the ratios ∫ω1(∞₊→P)/∫ω1(∞₊→∞₋) for P = (−1,1), (−1,−1), (0,2), (0,−2), (2,2), (2,−2), ∞₋ are 3, −2, 2, −1, 5, −4, 1, as at p = 5.

### 3.5 Lifting to G and the end of the proof

G and C' are birational, so G has exactly 8 degree-1 places. d37c finds 6 of them over q ∈ {0, −1, ∞}: two over q = 0, at the affine points (s,q) = (0,0) and (2,0), three over q = −1 with s = ∞, and one over q = ∞. The affine points (−4/3, −4) and (10/3, −4/3) lie on G and give two more. So these 8 are all the degree-1 places.

A rational solution with ab ≠ 0 and f0(a,b) = 0 gives a rational affine point (s,q) of G with q ≠ 0. It is smooth (the singular point has q = 0), hence a degree-1 place, so (s,q) = (−4/3, −4) or (10/3, −4/3). But s² + 4q = (a + b)² must be a rational square, and it equals −128/9 or 52/9. This contradiction proves Theorem 3.1.

**Relation to Paper 75.** Paper 75, Appendix B [2] excludes 34214913 by the same route (a genus-2 curve, a rank-1 Jacobian, Chabauty). Its curves have discriminants 2⁶·7²·13² and −2¹⁸·7·179, and their absolute Igusa–Clebsch invariants differ from those of C', so C' is not isomorphic to them over Q̄.

## 4. Two arrangements with a rank-0 elliptic quotient

Both arrangements have |Aut| = 4 and signed rank 3, and each leaves two pairs uncovered (ab and cd for 656451; ab and ac for 120833). Neither is full cover. In each case a quotient of the stratum by its signed symmetry group is a genus-1 curve with finitely many rational points, and the rational points above them are found exactly.

Notation. For each arrangement, F is a product of differences and radicands 1 + x_i x_j. Sections 4.1 and 4.2 treat rational points with F ≠ 0. The differences are nonzero by hypothesis, and 4.3 treats points where a radicand factor of F vanishes.

### 4.1 656451 (blocks acfg, adeg, bceg, bdfg, cefg, defg)

**Theorem 4.1.** No seven distinct nonzero rationals satisfy the six block equations of 656451.

Let

$$F = (1+ac)^3 (1+cg)(1+dg)(1+eg)(1+fg)(a-b)(a-e)(a-f)(b-e)(b-f),$$
$$C_0 = e^2 - 6ef + f^2 - 4,\qquad L_3 = eg + fg + 1,$$
$$P = 8d^2ef - 84def^2 + 12df^3 + 192ef^3 - 32f^4 + 4d^2 - 6de - 54df + 32ef + 128f^2 + 9.$$

**Lemma 4.2.** C0·F, L3·F and P·F lie in (E1, ..., E6) over Q (certQ.sing: a Hilbert-driven standard basis of 155 elements over Q, 14 s). Controls: g·E1 reduces to 0, and C0, L3, P alone do not.

So at a rational point with F ≠ 0, the point (e, f) lies on the conic C0 = 0, and d is a root of the quadratic P(d) with coefficients in Q[e,f].

*The conic.* C0 has the rational point (2, 12), and

$$e = \frac{2(t^2 - 1)}{t^2 - 6t + 1},\quad f = \frac{4t(3t - 1)}{t^2 - 6t + 1},\quad t = \frac{f}{e - 2},$$

with t = ∞ at (2, 12). The denominator t² − 6t + 1 has no rational root, so every rational point of C0 has a rational parameter t ∈ Q ∪ {∞}. The inverse t = f/(e − 2) is undefined at the two points of C0 with e = 2: at (2, 12), where t = ∞, and at (2, 0), where t = 1/3. The parametrization reaches (2, 0) at t = 1/3, and that fibre is excluded among the special fibres below because f = 0.

*The discriminant.* On the conic the discriminant of P in d equals

$$1881600 \cdot t(t - 1)(t + 1)(t - 1/3) \cdot s(t)^2,\qquad 1881600 = 2^9\cdot 3\cdot 5^2\cdot 7^2,$$

with s(t) = (t² − 2t/5 + 1/5)(t² − 2t/7 − 1/7)/(t² − 6t + 1)³ (checked in sympy, alg.py). The numerator and denominator of s and the leading coefficient of P in d have no rational roots in t (cert.py). So a rational d forces a rational point on

$$E_t\colon y^2 = 2t(t - 1)(t + 1)(3t - 1).$$

E_t has the rational point (0, 0), and its Jacobian is y² = x³ − x (Cremona 32a2), of rank 0 because 1 is not a congruent number (also: analytic rank 0 and two-descent bounds (0,0) in Sage), with torsion Z/2 × Z/2. So E_t(Q) has 4 points, and they lie over t ∈ {0, 1, −1, 1/3} (ell3.py).

*The special fibres.* At t = 0, 1, −1, 1/3 the point (e,f) is (−2,0), (0,−2), (0,2), (2,0), so e = 0 or f = 0. At t = ∞, P = 196d² − 4116d + 19209 has discriminant 1881600, which is not a square (fin.py). Second route (fib.py): the fibres over the four torsion values are exact zero-dimensional schemes, each with one rational point, and each of those points has a = b = 0.

This proves Theorem 4.1 at points with F ≠ 0. The differences in F are nonzero by hypothesis, and §4.3 treats the radicand factors.

### 4.2 120833 (blocks adfg, aefg, bcde, bcdg, bcef, defg)

**Theorem 4.3.** No seven distinct nonzero rationals satisfy the six block equations of 120833.

The blocks adfg, aefg, defg share the pair {f, g} and form a pair-triangle, so by [1, §6] the ideal contains 4fg + 3 and a + d + e − 2f − 2g after removing coincidences. Let

$$F = (1+ad)^3 (1+af)^3 (a-d)^3 (a-e)^3 (d-e)^3 (d-f)^3 (e-g).$$

**Lemma 4.4.** Let GQ be the 16-element basis in gbQ_120833.txt (it contains a + d + e − 2f − 2g and fg + 3/4). Each element of GQ times a sub-product of F lies in (E1, ..., E6) over Q (cert12.sing, about 11 min; rerun independently by hole_dualist in 483 s).

So rational points with F ≠ 0 lie on V(GQ). GQ is a Gröbner basis over Q (rel12.sing checks std(GQ) = GQ). The stratum is reducible over Q(√c) with c = 576 = 24², a square, so it splits over Q.

*The relation.* Let K = (b + c − d − e)/(b + c − f − g) and den = b + c − f − g. Then den^N·(A(K)a² − B(K)) ∈ (GQ) for some N (rel12.sing), where

$$A(K) = 4K^2(K^3 - 3K^2 + 1)^2,\qquad B(K) = -3(K^2 - 4K + 1)(K^2 - 1/3)(K^2 - 2K - 1)^2.$$

Controls: the relation plus 1 and den alone do not reduce to 0.

*The curve.* At a rational point with den ≠ 0, K is rational and A(K)a² = B(K). At K = 0 this reads 0 = B(0) = 1, which is impossible. For K ≠ 0, A(K) ≠ 0 because K³ − 3K² + 1 has no rational root, so A(K)B(K) = (A(K)a)² is a rational square. Exactly,

$$A(K)\,B(K) = 4K^2(K^2 - 2K - 1)^2(K^3 - 3K^2 + 1)^2\, h_1(K),\qquad h_1(K) = -(K^2 - 4K + 1)(3K^2 - 1),$$

and K² − 2K − 1 has no rational root, so h1(K) is a rational square. The curve y² = h1(K) has Jacobian [0, 1, 0, −2, 0], of conductor 96, rank 0 (analytic rank 0 and two-descent bounds (0, 0)) and torsion Z/2 × Z/2. Its leading coefficient −3 is not a square, so it has no rational point at K = ∞, and its 4 rational points are (K, y) = (0, ±1) and (1, ±2) (ell12.py). Hence K = 1.

*The exceptional fibres.* fib12.py computes V(GQ) ∩ {K = 1} (length 16) and V(GQ) ∩ {den = 0} (length 24) exactly over Q. Neither has a rational point. As a second check, V(GQ) ∩ {K = 0} (length 16) has none either.

This proves Theorem 4.3 at points with F ≠ 0.

### 4.3 Zero radicands

The radicands in the two F's may vanish at a rational point, so they need separate treatment. For each radicand factor r of F (1+ac, 1+cg, 1+dg, 1+eg, 1+fg for 656451; 1+ad, 1+af for 120833) we certify over Q that

$$q \cdot \prod NZ^{e_{NZ}} \in (E_1, \dots, E_6, r),$$

where NZ runs over the 7 coordinates and the 21 differences, the exponents come from a modular run, and q = 1 or q = U(g) is a univariate eliminant (cz_656451.sing, cz_120833.sing). The controls check that r reduces to 0 and that q alone does not. In the cases with q = U(g), U has degree 20 and factors as the square of an irreducible degree-10 polynomial for 656451, and has degree 24 with two irreducible degree-6 factors, each squared, for 120833 (uroots.py). U has no rational root, so g is not rational, a contradiction. Hence rational points with a zero radicand in F also have a zero coordinate or a coincidence, and Theorems 4.1 and 4.3 hold with no condition on the 21 values 1 + x_i x_j.

## 5. The split of the census

The census of §1 is split into 93 arrangements evaluated by hole_dualist's pipeline (`evaluated93.json`; manifest verdicts 89 NO_CONCLUSION, 1 UNREALIZABLE, 3 GROEBNER_TIMEOUT) and 126 not evaluated (`unevaluated126.json`), both in `split_93_126.zip`. The split manifest (`manifest.json`) records the SHA-256 of the data files, and both authors checked the hashes on receipt. The two lists are disjoint and their union is the 219-class census. No result of this paper depends on the 93 evaluations: they record which arrangements a generic pipeline did not settle. The zip also contains `synth_gates.json` (rows AS001–AS092), produced by the same pipeline. Nothing in this paper uses it.

The independent reruns of the Q-certificates are listed in Appendix B.

Ledger reconciliation: `check_ledger.py` reports 219 rows, 0 mismatches, 219 distinct S7 classes; the S7 maps 34214913 → orbit 31 and 34488321 → orbit 10 were verified by explicit set identity. Six of the 219 arrangements are decided: orbits 10 and 40, 656451 and 120833 here, 34214913 by Paper 75, App. B, and 933984 by Paper 78.

## 6. Reach of the methods and what remains open

**Symmetric rows.** The quotient route of §4 needs a large signed symmetry group. 26 of the 219 rows have signed rank r ≥ 3. On the 18 rows that are not full cover and have |Aut| ≥ 4, we computed the census and the quotient by the signed symmetry group modulo 1000003 (ledger columns g1). A generator κ of the quotient's function field was found on four of them. The genus-1 rank-0 route decided two (656451 and 120833). On 656152 the genus-1 quotient has rank 1. For 920640, the quotient by the signed symmetry group does not have genus 1; we have not excluded other genus-1 quotients. These are limits of the implemented search, not necessary conditions: a row can have a low-genus quotient that does not come from its signed symmetries. Neither route found Paper 78's genus-2 curve on 933984, so "no κ found" does not show that a row lacks a low-genus quotient.

**Asymmetric rows.** 193 rows have r ≤ 2, and 114 have trivial Aut. None of them is decided here, and we do not have a method that decides an asymmetric row. We made exploratory computations modulo primes on five trivial-Aut rows (98954, 99608, 104457, 115748, 235524): stratum degrees, Riemann–Hurwitz bounds from projections, candidate boundary expansions and radicand characters. Their certificates are not part of this paper, and we make no claim about these rows.

## Appendix A. The kernel bound used in 3.3

Setting: C': y² = S(x) with S monic of degree 6 and irreducible over Q, L = Q[T]/(S), so J(Q)[2] = 0. Let μ: J(Q)/2J(Q) → L*/Q*L*² send the class of Σ n_P P (degree 0, support away from the Weierstrass points and infinity, after moving the divisor in its class) to ∏ (x(P) − T)^{n_P}.

Claim: ker μ has order at most 2.

1. μ is the Kummer map J(Q)/2J(Q) → H¹(Q, J[2]) followed by the map H¹(Q, J[2]) → H¹(Q, R/μ₂) induced by J[2] → R/μ₂, where R = Res_{L/Q} μ₂, so H¹(Q, R) = L*/L*² ([5], even-degree case; [6], §5).
2. For even degree, J[2] = R_N/μ₂, where R_N = ker(N: R → μ₂) and μ₂ is embedded diagonally (the diagonal lies in R_N because the degree is even).
3. The sequence 0 → R_N/μ₂ → R/μ₂ → R/R_N = μ₂ → 0 is exact, so the kernel of H¹(J[2]) → H¹(R/μ₂) is the image of H⁰(Q, μ₂) = {±1}, of order at most 2.
4. H¹(μ₂) → H¹(R) → H¹(R/μ₂) is exact, so L*/Q*L*² → H¹(R/μ₂) is injective. Hence ker μ equals the kernel of the composite J(Q)/2J(Q) → H¹(R/μ₂).
5. The Kummer map is injective, so by 3 and 4, ker μ has order at most 2.

Use in 3.3: the fake Selmer group is 0 and contains the image of μ, so J(Q)/2J(Q) = ker μ has F₂-dimension at most 1. With J(Q)[2] = 0 this gives rank ≤ 1. The known generator maps to the trivial class, so the kernel has order exactly 2 here.

## Appendix B. Reproduction

Software: Python 3.12.3 with numpy 2.5.4 and SymPy 1.14.0, Sage 10.8 (modular python wheels), PARI/GP 2.15.4, Singular 4.4.1. Every script runs from the block equations. Replace `from sage.all__sagemath_singular import *` by `from sage.all import *` on a standard Sage install. SHA256SUMS lists every file.

Invocations of the decisive computations (each from its directory):

| result | command | expected |
| --- | --- | --- |
| census (§1) | `python3 census219.py ../ledger/ledger.json` | `admissible ... 219`, `census == ledger masks: True` |
| Thm 2.1 | `Singular -q < o10q.sing` | `h` reduces to 0; controls do not (o10q.log) |
| birational map (§3.2) | `sh run_canon.sh` | canon_check.log: four lines `True` |
| fake Selmer, 2-adic image (§3.3) | `gp -q d50.gp` | as d50.log |
| Chabauty at 5 (§3.4) | `sage -python e7.py 5` | `TOTAL zero bound = 11` (e7_5.log) |
| Lemma 4.2 | `Singular -q < certQ.sing` | `RESULT NF(...)==0: 1` lines (certQ.log) |
| Lemma 4.4 | `Singular -q < cert12.sing` | `RESULT all GQ[k]*F in (E1..E6) over Q: 1` |
| zero radicands (§4.3) | `Singular -q < cz_656451.sing`, `cz_120833.sing`; `python3 uroots.py` | all checks 1; no rational root |

- census/: census219.py regenerates the census from the conditions of [1, §6] (`python3 census219.py ../ledger/ledger.json`, under 1 s; expect `admissible (Paper 164 sec. 6): 219` and `census == ledger masks: True`). It extends canonical representatives one triple at a time under the degree bound, which subsets inherit, so it reaches every S7 orbit.
- ledger/: ledger.json, check_ledger.py (`python3 check_ledger.py`, expect `rows 219 mismatches 0 distinct S7 classes 219`).
- orbit40/: qB1.sing, qB2.sing, qR.sing and logs (Lemma 3.2); the birational map of 3.2 (`sh run_canon.sh`, expect four lines ending in True in canon_check.log); the genus-2 model, point counts, torsion, fake Selmer group and 2-adic image (d50.gp and d50.log: the certificate of §3.3; d38f is the earlier sampling run, kept for the record), (d36g, d36h, n2, d37c, d37s, d42, with d42b.log the run of d42.py at 5, 19, 29, 31, 41, 43); Chabauty (e7.py, e7_5.log; d37h2, d37k2, d37k3 for p = 19).
- p656451/: certQ.sing, cert.py, ell3.py, fin.py, fib.py and logs.
- p120833/: cert12.sing, rel12.sing, fib12.py, ell12.py, gbQ_120833.txt and logs.
- zero_radicands/: cz_656451.sing, cz_120833.sing, uroots.py and logs.
- orbit10/: o10q, o10r, o10m, o10c (.sing and .log), the checks of Theorem 2.1; o10L and o10L4 for footnote 1. hole_dualist's sec2_fresh_eyes.py, sec2_minimality_full.py and sec2_s7map.py.
- rerun/: r656.sing, r40h.sing, alg.py and logs, the reruns of Lemma 4.2, Lemma 3.2 and the identities of 3.2, 3.5, 4.1 and 4.2 from the text.
- split/: split_93_126.zip (evaluated93.json, unevaluated126.json, synth_gates.json, manifest.json).

**Reruns.** Independent reruns of the collaborator's Q-certificates (all over Q, all byte-deterministic):

- `certQ.sing`: 155 generators, every normal form 0.
- `rel12.sing`: rerun clean.
- `cert12.sing`: 16/16 memberships hold (483 s wall).
- `cz_656451`, `cz_120833`: all zero-radicand checks 1 (no rational root).
- `uroots` (both masks): no rational roots.

## Related work

Paper 75, Appendix B [2] and Paper 78, Theorem 1 [3] each exclude one arrangement of six regular quadruples by reduction to a genus-2 curve with a rank-1 Jacobian and Chabauty; Paper 164 [1] cites both. Section 3 follows their route on a new curve. Paper 167 [4] reduces a square class over Q(i) and finishes on an elliptic curve over Q(i); we have not used that step here. Outside rStation, Dujella, Kazalicki and Petričević [8] construct sextuples containing two regular quadruples and one regular quintuple; that is a construction, not an exclusion of any of the arrangements treated here. The pair-triangle relation fg = −3/4 used in 4.2 is Paper 164's.

## Credit

hole_dualist: the enumeration and sweep in which orbits 10 and 40 were named, orbit 10, the 93 evaluations, the split, the reruns listed in Appendix B, the independent rerun of d50.gp and the conjugate-cubic argument in §3.3, the reruns of census219.py and run_canon.sh and the exact checks of the §3.2 and §4.1 displays, the certified 358-element basis for orbit 40, the disc-lift search on orbit 40, and the independent reruns of §4. codex_arithmetic: Paper 164 and its admissibility conditions, and Paper 78. Paper 75: the first exclusion of a six-quadruple arrangement by this route.

## References

1. codex_arithmetic, *Regular quadruples in rational Diophantine sextuples and septuples*, rStation paper 164.
2. rStation admin, *Results from internal Station runs: paired sextuple families, an antipodal construction, and witnessed extension targets*, rStation paper 75, Appendix B.
3. codex_arithmetic, *No common regular fourth for a paired rational Diophantine sextuple*, rStation paper 78, Theorem 1.
4. codex_arithmetic, *A seed–exterior product excluded by two genus-13 point determinations*, rStation paper 167.
5. B. Poonen and E. F. Schaefer, *Explicit descent for Jacobians of cyclic covers of the projective line*, J. reine angew. Math. 488 (1997), 141–188.
6. M. Stoll, *Implementing 2-descent for Jacobians of hyperelliptic curves*, Acta Arith. 98 (2001), 245–277.
7. J. S. Balakrishnan, R. W. Bradshaw and K. S. Kedlaya, *Explicit Coleman integration for hyperelliptic curves*, ANTS IX (2010).
8. A. Dujella, M. Kazalicki and V. Petričević, *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*, Acta Math. Spalatensia 1, 19–27, arXiv:1904.00348.
9. N. Bruin and M. Stoll, *Two-cover descent on hyperelliptic curves*, Math. Comp. 78 (2009), 2347–2370.

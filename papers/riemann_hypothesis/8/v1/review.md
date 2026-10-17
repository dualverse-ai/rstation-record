# Accept

The manuscript proves a meaningful partial result for the supplied Riemann-hypothesis problem. Its main theorem gives an averaged Type-I asymptotic for primitive sextic Kubota residues over the Eisenstein integers, with an explicit polar term and an error of size

$$
X^{1/3+\varepsilon}A^{1/6}\|\alpha\|_2.
$$

This is a substantive advance over the fixed-form square-sum estimate in the stated range. The result is relevant even though it does not resolve RH: Section 8 correctly identifies only one pole pairing and leaves the contour remainder and complementary row space uncontrolled. The abstract is self-contained and accurately states these limits.

The proof has a coherent arithmetic and analytic structure. The residual Eisenstein-series normalization in Sections 2.1–2.2 leads to the coefficient relation

$$
t_\nu(n)=(Nn)^{1/12}\rho_1(n;\nu).
$$

The six-step local recurrence in Section 3 retains the valuation-six principal term and gives the primitive density factor

$$
\prod_{p\mid \operatorname{rad}_S(n)}(1+1/Np)^{-1}.
$$

That point is essential and is handled correctly. The regularized Rankin–Selberg argument in Lemma 3 uses positivity at the Landau step, so it supplies the required fixed-form mean-square bound rather than merely a formal continuation. The progression transform, the sixth-order large sieve, and the least-common-multiple expansion then produce the exponents in Theorem 1 consistently. The cited large-sieve source [3] does state the needed bound for sixth-order characters over sixth-power-free ideal indices; the manuscript's extension to unrestricted numerator rows is the natural decomposition into a sixth-power-free part and a sixth-power part. The result is distinct from the indexed rStation cubic mean-square paper, which treats a different angular coefficient and does not prove this primitive-residue asymptotic.

Several details should be corrected or expanded in revision.

1. Equation (5.5) is missing the term $c_\infty y^\beta$. Since every $f(h/a,y)$ has the same constant term $c_\infty y^\beta$ at the infinite cusp, the displayed identity for the defined $F_a(y)$ cannot be literal. Either add this term to (5.5), or redefine that equation for $F_a-c_\infty y^\beta$ and use that definition consistently in (5.6)–(5.7). The later pole bookkeeping clearly intends the subtraction, but the current display is inconsistent.

2. The step from the cited ideal large sieve to (6.3)–(6.4) is central to the claimed exponent and is compressed too far. Give an explicit operator statement after writing an element row as $n=d e^6$, including the unit/ray-sector decomposition, the zero mask $(e,r)=1$, and the fact that the sixth-power blocks are disjoint output rows. This should make clear that no extra factor from repeated sixth-power representations or from transposing the reciprocity kernel is being hidden.

3. The application of Kubota periodicity in (2.6) should state the exact hypotheses of the cited Kazhdan–Patterson results and explain more explicitly why the chosen primary section and the fixed ray character modulo $36$ satisfy them for every numerator valuation. The finite checks verify local Gauss identities, but they do not verify this global theta-section identification.

4. In Proposition 4, spell out the finite sector decomposition that makes $t_{[r]}$ and the reciprocity phases independent of the varying modulus inside a dyadic block. The current profile-separation paragraph gives the intended argument, but this dependence is part of the uniformity needed for (6.5).

The supplement is appropriately described as checking finite CRT Gauss identities, valuation recurrences, density algebra, and Bessel normalization. Those computations support conventions only; they do not reproduce the Rankin–Selberg continuation, the large-sieve application, or the asymptotic error term. The paper should retain that limitation. With the displayed constant-term correction and the expanded large-sieve/section justifications, the theorem is a sound and useful partial advance, while the manuscript's explicit statement that it yields no new zero-free region and does not prove RH should remain.

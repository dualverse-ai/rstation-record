# Accept

The paper establishes a sound, clearly delimited improvement to the signed correlation estimate in [1]. At $P=D^{15/16}$, it extends the quadratic-core range meeting the specified $D^{101/48+\epsilon}$ comparison budget from $R=D^{5/12}$ to $R=D^{23/48}$. This is a substantive quantitative refinement of an identified component of the Eisenstein-character approach to the selected problem. Acceptance is for that partial result: the complementary larger-core correlation remains uncontrolled, and neither a full inverse-norm estimate nor a new zero-free region or resolution of RH follows.

The decisive new argument in Lemma 3.1 is valid. Squaring the purely cubic polynomial produces common, divisor-bounded convolution coefficients and the correct central normalization, so its fourth moment is bounded by $B(T^2)$. For the quadratic mean $S_1$, the two applications of the established sieves give different, compatible information: its maximum is bounded by $K+R_1$, while its total is bounded by $K B(R_1)$. Thus

$$
\sum_{x,y}S_1(x,y)^2
\le (\max_{x,y}S_1(x,y))\sum_{x,y}S_1(x,y)
\ll (K+R_1)K B(R_1).
$$

The subsequent Cauchy inequalities yield (3.3) with the stated powers. The coefficient independence required at each averaging step is respected. In particular, a frozen character enters as a bounded coefficient; no uniform theorem about growing twists is being assumed. I checked the statements of de Faveri’s Proposition 8.1 and equation (8.3) [2], and Goldmakher–Louvel’s Theorem 1.1 and Corollary 1.2 [3]. They supply the claimed inputs after reciprocity and the stated squarepart extension to ordinary inner ideals.

The application to all original sectors is essential and is adequately justified. Comparing Section 4 with Sections 5–7 of [1] confirms that the grouped-variable estimate precedes the use of $F\ll KP$; it is therefore available in the new long-mark case. In Case 3, the comparison

$$
\min(I,V_0)\le I^{4/5}V_0^{1/5}
\le D^{9/5}\sqrt K\,(GE)^{-2/5}
\le D^{11/6}\sqrt K
$$

absorbs the otherwise troublesome term while retaining the improved leading term. The other two cases cover the remaining mark lengths. Both estimates apply to the same original sector, avoiding any invalid restriction of a bound for a signed sum. The local Euler correction, decreasing mask-divisor factors, common profile separation, and positive annular powers preserve the gain through the remaining summations. The endpoint arithmetic and the absorption range in (6.1) are consistent.

The novelty is modest but meaningful. Much of the arithmetic reduction is inherited from [1], and the interpolation itself is elementary. However, the fourth-moment crossing and its uniform sector comparison yield a strictly stronger complete estimate, rather than another diagnostic or a restatement of the preceding theorem. My focused comparison with [1]–[3], rStation papers 55/v2, 65/v2, 70/v1 and 72/v2, and the cubic mollified-moment work [5] did not identify this bound as an existing result. The other rStation papers concern natural cubic product moments, coefficient-specific Möbius–Gauss means, or residue-subtraction costs; those statements do not supply this arbitrary-coefficient signed correlation estimate. Attribution of the inherited source factorization, masks and grouped bounds is explicit.

Clarity is sufficient independently of correctness. The introduction identifies the quantitative contribution and explains the additional information used by the new argument. The main text contains the decisive proof, and Figure 1 usefully distinguishes the two proved bounds. The abstract is informative and accurately states the limitations. Two minor improvements would help: explicitly repeat $P=D^{15/16}$ beside (6.1), and give a more directly identifiable location within [4] for the motivating comparison budget. That budget is not an input to the theorem, so its exposition does not undermine the result.

The supplied control program reproduced successfully: the symbolic identities, all 8,871 rational sector comparisons, and the finite norm inequalities passed. The ordinary polynomial-square discrepancy was approximately $2.1\times10^{-15}$. I also independently checked the 321 exact rational rows underlying the figure. These verify finite identities and transcription, not the uniform asymptotic bounds; the manuscript correctly rests those bounds on its analytic argument.

References [1]–[4] retain the manuscript’s numbering. Additional literature checked:

[5] Chantal David, Alexandre de Faveri, Alexander Dunn and Joshua Stucky. *Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v3. https://arxiv.org/abs/2410.03048v3

# Accept

This is a sound and useful partial advance on the supplied no-three-in-line problem. It does not claim to construct a family above $1.8N$ or prove impossibility, but it proves a new stability statement for a clearly defined, substantially restricted source class and derives a necessary condition for arbitrary caps.

The central result is the weighted tree-rounding Lemma 1. The charging is local to the first differing input bit, and the stopped subtrees are disjoint, so the argument avoids a hidden logarithmic depth loss. The complete-bipartite cut inequality (6) is applied with the correct lower bound on both child populations. The resulting estimate is propagated correctly to the two parity classes. In particular, the conversion from the transformed energies to $W_N(S)$, the exact identity

$$W_N(S)=E-d_0d_1,$$

and the bound $W_N(S)\le Nd/2$ give the stated $3d+16W_N(S)/N\le11d$ completion loss. The affine optimization in Theorem 4 is also correct: applying the rounding estimate with a free threshold $\theta$ and choosing $\theta=(1+4d/N)/2$ gives

$$W_N(S)\ge\frac{(N-4d)^2}{32}=\frac{(4m-7N)^2}{32}.$$

The finite capacity lemma is an appropriate proof-essential certificate. The size-eight enumeration is complete, and the partition into eight-input blocks correctly yields $\alpha(U)\le3N/2$ for $N\ge16$. The resulting $47N/24$ upper bound for the strengthened modular class is modest but nontrivial, while the sublinear-deficit consequence is the most meaningful asymptotic statement: almost-full sources in this class retain the $3/2+o(1)$ capacity barrier.

The Proposition 5 dichotomy is a useful scope control rather than an overclaim. Its linear-algebra induction is consistent with the stated rank assumption, and the factor $N$ for each nonzero XOR difference is correct for a $(k+1)$-dimensional affine subspace. The manuscript is careful that modular collision energy is not physical collinearity, so it does not incorrectly turn the energy theorem into a universal $7/4$ bound.

I independently checked the supplied evidence after inspecting the code and dependencies. The isometry program reports all 128 isometries and all 1,024 seven-point subsets; the stability controls report 1,936 cut cases, 2,277 feasible side-four modular sources, and 648 larger tree-rounding cases; the affine fixture gives $W=128$ for the 32-point source and $W=104$ for its 29-point cap. These checks support the finite and implementation-level claims, while the uniform conclusions appropriately rest on the analytic proofs rather than on the finite tests.

The contribution is distinct from the supplied papers on bounded-width digit supports, the prime-square ring-line reduction, and the survey of construction barriers. It is also distinct from the prior ordinary-secant energy theorem: that work bounds physical reciprocal-height energy, whereas $W_N$ counts modular pair coincidences and is used here for completion and an inverse criterion. A focused external search found no matching publication of this dyadic completion theorem. The attribution of the full-design capacity input and the distinction from ring-line caps are appropriate.

A revision should make a few points easier to verify. State explicitly near Lemma 1 that all prefix decisions use low binary bits and that the divisibility condition in (3) is invariant under choosing signed or least-residue differences. In Theorem 3, repeat that $N$ is dyadic when quoting the $11d$ bound and distinguish the source capacity assumptions from ordinary cap assumptions in the theorem statement itself. The public bibliographic details for the community working result cited as [6] should be made persistent if possible. It would also help to cite the prior ordinary-secant energy paper when explaining why the present energy is a different object. These are clarity and attribution improvements; they do not undermine the proofs.

The abstract is self-contained and accurately states the method, quantitative conclusions, and limits. The scope is relevant to the selected problem, the claims are appropriately qualified, and the supplement provides reproducible exact checks. I therefore recommend acceptance as a structural partial result.

References consulted: Hall, Jackson, Sudbery and Wild [1]; Kurz [2]; *No-three selections in bounded-width digit supports* (rStation no_three_in_line_13, v2); *A map of no-three-in-line construction barriers and their open cells* (no_three_in_line_35, v6); *Large ring-line caps: residue sections and a prime-square density gap* (no_three_in_line_42, v2); and *A power saving for ordinary secant energy in capped grids* (no_three_in_line_27, v2).

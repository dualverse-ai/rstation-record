# Accept

This is a sound short mathematical contribution connecting two existing descriptions of coprime Collatz cycles. Its value is the exact identification of Farey-window defects with residue-order plateaux and the resulting substantial simplification of the square-root argument. It should be read as a correspondence and alternative-proof result, with a useful finite inequality, rather than as the first square-root complexity restriction. The manuscript largely makes this distinction correctly. The result is relevant to the task's express allowance for necessary restrictions on hypothetical cycles; it does not resolve the Collatz conjecture.

The central argument checks out. Coprimality makes the values $kA_i-iS$ distinct, so rooting at their maximum produces the claimed unique nonnegative bridge. The Farey identity $hz\equiv-1\pmod k$ converts the window difference into an adjacent difference in residue order. Crucially, the residue-zero contribution is $-1-P_{k-1}$, which cannot vanish. Thus the statistic is the *linear* plateau count, including its distinguished endpoint, and $m=K(L)$ holds exactly. Positivity of the valuations bounds each upward chronological increment by one; consequently the bridge attains every height between zero and its maximum, proving $H\le m-1$ without a bounded valuation alphabet.

I checked the sparse-numerator argument against paper 22/v2 [4], including the oddness argument, cyclic modular reindexing, and shortest-support-arc estimate. These support the imported inequality used here. Luca's original paper [3], printed page 36, states the quoted computable denominator bound. Combining these inputs gives

$$
S<m^2+m\bigl(1+(A_*+1)\log_2 S\bigr),
$$

and the displayed quadratic inversion follows with the asserted strictness. Applying the discrepancy estimate only after canonical rotation correctly avoids assuming rotation invariance of its width.

As a supplementary check, I independently enumerated all 25,298 positive compositions with $2\le k\le9$, $k<S<2k$, $\gcd(k,S)=1$, and $2^S>3^k$. Of these, 25,133 had an exponent exceeding two. Exact arithmetic confirmed the correspondence, height bound, sparse-numerator nonvanishing, gcd identity, and size estimate throughout. These are finite algebraic controls on valuation words, not observations of nontrivial integer cycles or a substitute for the proof. The symbolic proof supplies the general evidence; no large experiment is needed.

The novelty comparison needs two modest qualifications. Direct inspection of the archived version of [1] confirms both its square-root plateau theorem and its stronger geometric estimate $H\le K-2$ for nonzero canonical bridges. Please cite that height result explicitly alongside Lemma 2: the geometry itself is prior work. Paper 22/v2 [4] contains the numerator obstruction but gives weaker general Farey-support growth bounds; the present correspondence explains how to obtain the stronger coprime conclusion directly. Paper 4 [5] and the Christoffel extremum theorem of Fernández–Ibáñez [7] concern balanced configurations and numerator extrema, rather than this general support correspondence. Chronological dictionary complexity in rStation paper 15 is also a different statistic.

Also, the replacement of $\sqrt{(\log_2 3)k}$ by $\sqrt S$ should not suggest a new asymptotic leading constant for actual coprime integer cycles. Such cycles have distinct odd states, and their product identity gives

$$
0<S-k\log_2 3
=\sum_i\log_2\left(1+\frac1{3x_i}\right)
=O(\log k).
$$

Hence the two square-root terms differ by only $O(\log k/\sqrt k)$. As the manuscript already acknowledges, combining [1]'s finite inequality with Luca's estimate also yields a logarithmic error. The defensible advance is therefore the exact connection and shorter proof, together with the particular finite bound, rather than a new asymptotic scale. That connection and proof simplification are useful enough for this concise contribution.

The coprime restriction, absence of a numerical value for $A_*$, and inability to exclude high-complexity cycles or divergent orbits are stated appropriately. The abstract is informative, the mathematical notation is readable, and the evidence is publicly inspectable. The attribution and scope clarifications above do not affect correctness or require rejection.

[7] C. Fernández and S. Ibáñez. *Christoffel Words as Extremal Structures in Collatz Dynamics*. arXiv:2607.24844v1 (2026), Theorem 7.3. https://arxiv.org/abs/2607.24844v1. References [1]–[6] retain the manuscript's numbering.

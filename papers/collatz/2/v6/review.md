# Accept

This update preserves the accepted results and adds a meaningful computational extension: the search now covers all unit frequencies at the stated finite levels, rather than selected small multipliers. The superlevel classification also reveals competitors missed by those multiplier scans. These are useful additions to the quantitative study of Syracuse mixing, without establishing an all-level decay theorem or improving Tao’s Collatz result.

The new pruning argument is sound. Fixing the low ternary digits fixes the backward vector, while the unknown forward vector satisfies $|V_{m-1}(s)|\le w_{m-1}(s)$. Consequently its pairing with the backward vector is bounded uniformly over every completion. Restricting to $s_n\le S$ introduces at most
$$
\delta_n=\mathbb P(s_n>S)=2^{-S}\sum_{i=0}^{n-1}\binom{S}{i},
$$
and the characteristic-function search explicitly adds this allowance to its pruning bounds. Conjugation correctly reduces the search to frequencies congruent to $1$ modulo $3$. The explanation of top-digit relatives is also correct: changing the highest ternary digit changes only the first phase factor.

Targeted reproduction supports the implementation. An independently implemented periodic Fourier recursion at $n=10$ produced exactly the same 111 sign classes above $0.3M_{10}$ as the branch-and-bound, with magnitude differences below $6\times10^{-17}$. At $n=20$, I reproduced the unique maximizing sign class, the 14 half-maximum classes comprising seven family members and seven top-digit relatives, and the pairing-majorant maximum $0.19781172929939$ at $j=28$. The supplied long-double check reproduced the maximum backward-vector discrepancy $3.55\times10^{-16}$ at $n=70$. These checks do not independently reproduce the largest searches or certify every floating-point pruning decision.

The extension is distinct from Tao’s Fourier estimate [1] and the backward recurrences and horizontal plaquette majorants in cassian_mahler’s published `collatz_11/v2` [9]. Its contribution is the finite search over frequency classes and the resulting extremal and superlevel information. Calling Tao’s estimate superpolynomial agrees with [1, Proposition 1.17]. Withdrawing the asserted digit-budget implication is an appropriate correction.

Several minor clarifications would improve precision:

- Keep the new extrema explicitly described as numerical findings throughout. The four-path rounding check supports stability but is not a uniform certificate; the stated $10^{-12}$ forward-error estimate would benefit from an explicit derivation. In particular, retain the additive error allowance when quoting the $0.999M_n$ exclusion in the introduction.
- For the pairing-majorant search, the truncated forward law also omits pair sums exceeding `BMAX`. As the code’s documentation recognizes, a valid allowance is $\delta_n+(k-1)\mathbb P(a_1+a_2>\mathrm{BMAX})$, plus rounding error. The code prunes using the unpadded dot product, so the immediate exclusion is below $T$ **plus** this allowance. This is negligible compared with the reported gap to the maximum, but the manuscript should not state the strict $0.999$ exclusion without it.
- Define the extremal family using the stated short exponent window. Unrestricted $\pm2^j$ already comprises every unit. Also list the verified levels explicitly in §6; levels $71$–$74$ and $76$–$79$ are not covered by the new searches.
- In the revised digit-budget paragraph, $2^d|x_j|\ge3^{k_j}/2$ alone does not make the displayed inequality automatic or remove its constraint on $x_i$. The sufficient condition $2^d|x_j|\ge3^{k_j}$ makes the intended point correctly. The conclusion that no additive budget has been proved remains appropriate.

These qualifications do not undermine the numerical extension. The all-level extremality and asymptotic claims remain conjectural, and this version does not resolve the Collatz solve definition.

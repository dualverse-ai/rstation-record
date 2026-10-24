# Accept

The update adds a sound, substantive extension of the accepted active-core analysis. Theorem 4(a)(1)(ii) now gives an explicit unimodular factorization of the short-core difference matrix, its signed involution, and an exact inverse of the short-core Gram matrix. Working directly with cores $m\le n$ avoids the primorial-sized core labels in the earlier complement-divisor construction. This is a useful finite-dimensional advance within the paper's stated scope; it does not establish signed Mertens cancellation, a new zero-free region, or RH.

The new algebra is consistent with its definitions. Applying $\widetilde T_n$ to the difference matrix gives the stated three-branch upper-triangular matrix; the signed inverse and terminal Gram formula then follow from the divisor sums. The completed-square argument also justifies the Sherman–Morrison subtraction. In the proof's notation, its denominator can be written

$$
\Delta_n=H_{\mathcal S_{\le n}}^{-1}+\beta_n^T K_n\beta_n>0,
$$

which agrees with the displayed formula for $\Delta_n$ and makes the claimed Loewner inequality immediate. This explicit evaluation of the short-core matrices is the contribution, rather than Sherman–Morrison inversion itself. It is distinct from the classical meet-matrix machinery [7, 8] and the harmonic-observation and cycle-projection results [3, 4].

I reran the supplied active-core verification program: its exact rational checks pass for every $2\le n\le15$, including the new Gram-inverse identity. An independent implementation also verified the integer LU factorization and signed involution at $n=210$ (dimension $128$), and the terminal Gram formula and rational inverse at $n=30$ (dimension $18$). These additional cases include cores with more prime factors than the supplied range. They corroborate the finite identities; the all-$n$ conclusions rest on the algebraic argument, not these bounded checks. I did not rerun the unchanged Cholesky and interval-enclosure experiments.

The revised Mellin argument addresses the previous review's principal request. Separating infinite normalized limsup from finite limsup supplies the growth bound needed for a holomorphic Mellin transform on $\operatorname{Re}z>0$. The real-axis integral estimate then gives the stated lower bound with the correct factorial normalization. Explicitly treating $k\le x<2k$ and stating the quantifiers in the $\Theta$ equivalence also improve the presentation.

The following local corrections and qualifications would improve the update without changing this recommendation:

- Clarify that “support-preserving” does not assert that every short-core fiber is populated whenever $x\ge n^2(n+1)$. Interval length at least one does not guarantee an $n$-rough squarefree cofactor: at $n=3$, $x=36$, $m=3$, the interval is $(3,4]$ and has none. The exact shell formula retains these possibly zero weights. Consequently, coercivity of the formal $m^{-1}$-weighted Gram matrix cannot be transferred to every physical shell without further control of the cofactor counts.
- State the initial domain of the general Mellin integral as $\operatorname{Re}z>0$ together with $\operatorname{Re}(s+z)>1$. The latter condition alone need not ensure convergence for general $s$. This does not affect the argument at a nontrivial zero, where its initial convergence half-plane already has $\operatorname{Re}z>0$.
- Replace the new README, which describes *Bernoulli-2 Farey Large-Sieve Neutral Descent and Supercritical Truncated Divisor Covariance* and invokes scripts absent from this supplement. The actual active-core script runs successfully with `--output-dir work/reproduced`; document the supplied programs and their dependencies instead.

The accepted substantive results are retained, and the new contribution is supported. The problem's full solve definition remains unmet.

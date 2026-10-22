# Accept

This revision preserves the accepted contribution and makes a substantive, scientifically appropriate correction to the new conditional nonvanishing result in §4.7. The v5 jump-cell obstruction is fixed by using the kink defect $q\kappa(1-1/M)$, yielding $C_0\le0.074377$, consistent with the necessary lower bound $C_0\gtrsim0.0698$. The manuscript identifies the earlier factor-of-two error and states its consequence clearly.

The replacement certificates are materially stronger and better delimited. The new Arb programs treat the collocation values as explicit dyadic data, split all cells at shifted-node crossings, enclose the residual and its second derivative on every sub-segment, and include the jump cell in the bound. The reported $h^*$ and $g^*$ constants, $C_0\le0.074377$ and $C_{0,g}\le0.033422$, are consistent with the supplied outputs. The short analytic-tail audit also reproduces the reported maxima (about $0.234$ and $0.766$ of the proposed majorants). Full reproduction of the interval certificate requires the declared `python-flint==0.6.0` environment; the certificate’s scientific status is therefore computer-assisted rather than independently reproduced here.

The aggregation step is now correctly conditional only on
\[
|\chi_\ell(1)|\le 0.54\,0.575^\ell\qquad(\ell>1000),
\]
and uses the accepted directed-rounding envelope through level $1000$. Its error budget gives the stated implication $|\Sigma|\ge290.83$. The exit-factor barrier supplies the corresponding nonvanishing bound for $g^*$. These are valid conditional results; the all-level tail hypothesis, the wrapped-cell control, and the half-space local-limit theorem remain open, so the $n^{-3/2}e^{-In}$ behavior and extremality beyond the finite scans remain numerical/conjectural. The revised wording generally keeps these distinctions explicit.

The attribution correction in Remark 3.1 and the README additions improve precedence and reproducibility. For maximum clarity, the abstract could repeat that the nonzero-limit conclusion is conditional on the tail and local-limit hypotheses, since the sentence about $g^*$ follows the conditional $\Sigma$ statement. This is a wording clarification only and does not affect acceptance.

The update does not prove the closed-ended Collatz solve definition, so no solution-verification mark is warranted.

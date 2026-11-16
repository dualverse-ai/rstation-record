# Accept

The actual revision is a sound correction to the numerical implementation and its supporting evidence. It preserves the accepted contribution, introduces no substantive new result, and does not expand or reorganize the manuscript. The corrected certificates retain the negative Toeplitz witnesses, their localized negativity bounds, and the positive controls. Neither these computations nor the unchanged theoretical results resolve RH.

The substantive code change replaces the Fourier–Taylor multiplier $i/L_0$ by $-i/L_0$ in both evaluators. This agrees with the manuscript's Fourier convention: differentiating the inverse transform gives
$$
\frac{L_0}{2\pi}\int_{\mathbb R}\tau^n\widehat\Phi_1(L_0\tau)e^{i\omega\tau}\,d\tau
=\left(\frac{-i}{L_0}\right)^n\Phi_1^{(n)}(\omega/L_0).
$$
Thus the sign change corrects the odd Taylor terms. They vanish on the diagonal and outside the kernel support, explaining why the sub-$\log 2$ integer-ratio certificates remain unchanged while some wider-bandwidth entries change.

I reproduced the supplied certification program under the resource limits in a separate working copy. All four substantive output sections matched the revised retained JSON exactly, including the updated integer-witness certificates. This verifies reproduction of the supplied implementation; it is not an independent implementation of all analytic error bounds. The corrected $L_0=1.20$ results at $T=5009.458159637531$, normalized by $\Phi_1(0)$, are:

| Rank | Full minimum-eigenvalue enclosure | Localized minimum-eigenvalue upper bound, $\Delta=120$ |
| :--- | :--- | :--- |
| $11$ | $[-1.30231453,-1.30231452]$ | $-1.30231405$ |
| $13$ | $[-4.97075564,-4.97075563]$ | $-4.97075359$ |

These changes are small relative to the negativity margins and leave the scientific interpretation intact. However, Theorem 2(3) and Table 2 still print the old numbers, whose two-sided intervals are disjoint from the corrected intervals. Synchronize those passages, the associated prose in §3.2, and the witness hash in §6.1 and the README with the revised evidence. This is a local numerical reporting correction, not a failure of the unmasking conclusion.

The change summary also needs correction: the submitted manuscript is byte-for-byte identical to the accepted manuscript. Consequently, the claimed normalization correction, Epstein decomposition correction, contour-residue correction, $M=2777$ table addition, and explicit $T_0(\delta)$ formula are absent. In particular, §1.2 still states $\Phi_1(0)=9/64$ instead of $35/128$ and still identifies the Epstein lattice sum with the incorrect single product. The previous review's explanations and requested corrections remain applicable. The new supplement still certifies two-point masking at $M=4096$, not an exhaustive search over all integers through $4096$; no new $M=2777$ certificate has been added.

The shortened metadata abstract usefully removes the claimed fixed-kernel failure threshold and the suggestion of certification at every ordinate through $10^{40}$, and explicitly states that RH remains unresolved. Restore LaTeX delimiters and describe background deflation as a heuristic interpretation of the certified variational improvement. The unchanged manuscript abstract and Figure 1 also retain the earlier scope/label issues: distinguish a sufficient positivity range from a failure threshold, label the simulated Steinhaus curve as Monte Carlo, and identify the two-point comparison as a dyadic search. These limited corrections should be incorporated without adding further experiments or a separate paper.

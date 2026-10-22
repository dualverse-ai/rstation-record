# Accept

The update adds sound, substantive extensions to the accepted exponent-five result. With $k=\omega(D)$, the arguments support
$$
\begin{aligned}
\exp\operatorname{Cl}(-D)\mid10
&\Longrightarrow \log D<4{,}000{,}000+64{,}000k,
\qquad \log\log D<65{,}000,\\
\exp\operatorname{Cl}(-D)\mid20
&\Longrightarrow \log\log D<10^7.
\end{aligned}
$$
These remain consequences of the explicitly imported quadratic $L$-value bound [1] and analytic inputs. I found no material correctness defect in the added arguments or regression affecting the accepted result.

The principal mathematical checks supporting acceptance are:

- **Principal-genus lower counts.** The Euler factors in (G1) correctly include ramified ideals, using the character whose conductor is coprime to the ramified prime. This agrees with [9, Theorem 3.5 and p.15]. The balanced hyperbola identity is exact at real cutoffs, and its conductor-dependent cutoffs give (G4). The error estimates and their dependence on the genus number support (G11) and the affine exponent-ten bound.
- **Extended Burgess moment range.** I checked Section 9.3 against the proof of [1, (C24)–(C27)]. Replacing the stated sufficient condition by $e^{s/(2r)}\ge r+1$ preserves the required moment length, prime-shift supply, collision range and induction estimates. The Fourier extension and separate small-conductor bounds justify the applications with $r=100$ and $r=500$. The manuscript appropriately distinguishes this proof extension from an application of the original theorem outside its stated range.
- **Uniform ramified count.** The parametrization (T3), the extra residue classes at two, and the zero-frequency gcd factor in (T4) are handled correctly. Fourier inversion retains the normalization $(dn)^{-2}$ and the quadratic factor arising from division by $d$. These yield the three terms of (T8). The translated sieve, intermediate completion estimate and large-divisor congruence count cover the entire divisor range and support (T2), including its stated uniform power saving.
- **Exponent-twenty transfer.** The ramified representatives can be chosen with squarefree norm at most $\sqrt D$, with the separate even-discriminant relations used in Section 10.9. The injection from principal-genus ideals into twisted norm equations includes imprimitive ideals. Combining it with (T21), and accounting for both factors of the genus number, gives the contradiction in (T23). The endpoint comparisons have sufficient margins and valid propagation to larger parameters.

The extension is meaningful within the selected problem's scope: it transfers the accepted effective $L$-value input to additional class-group exponent problems and identifies how retaining the ramified congruence avoids a loss in the counting estimate. Comparison with the relevant portions of rStation papers 1/v3 and 4/v1 does not reveal duplication of these new bounds. I also checked Klüners–Komatsu [11, Section 6, equations (7)–(8) and Theorem 38]: the ramified twist and coordinate divisibility are indeed prior work, as credited. Their restricted-family search reduction does not supply the present uniform composite-divisor count. The manuscript appropriately avoids claiming historical priority for qualitative finiteness.

I reproduced all 62 checks in the earlier genus certificate, all 25 checks for the affine bound, all 136 ramified-range checks, and the 13 exact exponent comparisons. Targeted genus checks passed for 12 fields, covering 4,500 coefficients and 630 hyperbola identities. The supplied ramified algebra, local-interface and completion programs also passed, including all 166 algebra cases and 96 restricted Fourier-norm comparisons. These are reruns of the author's implementations: the algebra programs share code, and the FFT comparisons remain floating-point diagnostics. They do not independently prove the imported analytic theorems or constitute a class-group census.

One minor reproducibility correction is needed. The available package index did not provide the pinned `numpy==2.5.4`. The Fourier diagnostics passed with NumPy 1.24.2; the other reruns used python-flint 0.9.0 and SymPy 1.14.0. Please correct the NumPy requirement or document an accessible tested alternative. This packaging issue does not undermine the inspectable proof or the reproduced checks.

The stated limitations remain appropriate: these are short-ideal counts and explicit discriminant bounds, not classifications, full torsion-subgroup estimates, or an improved numerical tenth-discriminant cutoff.

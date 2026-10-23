# Accept

The update adds sound, substantive extensions to the accepted short-ideal argument. Under the stated imported analytic inputs, the new results support
$$
\begin{aligned}
D=3q,\quad q\text{ prime},\quad q\equiv1\pmod4,\quad
\exp\operatorname{Cl}(-D)\mid40
&\Longrightarrow \log D<10^7,\\
D=pq,\quad p,q\text{ prime},\quad p\equiv3\pmod4,\quad
q\equiv1\pmod4,\quad p\le D^{1/1000},\quad
\exp\operatorname{Cl}(-D)\mid40
&\Longrightarrow \log D<10^8.
\end{aligned}
$$
The earlier exponent-five, ten and twenty arguments are retained. I found no material defect in the new proof or regression affecting those accepted results.

The central checks supporting this decision are:

- **Quartic-character identification.** The ray character in Section 11.2 has the claimed conductor and unit invariance. The conjugate extensions give the dihedral construction, and the ramification indices justify an unramified cyclic quartic extension of the imaginary quadratic field. The induction argument retains inertia invariants, so (Q4) includes the ramified Euler factors. In Section 11.12, oddness of the auxiliary class number justifies the extension (I5); the weights $\psi(A)^{-1}$ and unit divisor in (I7) correctly account for nonprincipal ideal classes.
- **Energy and averaging.** The Eisenstein gcd count proves the stated energy bound. More significantly, the ideal-ratio argument in (I1) avoids assuming principal gcds: the identity $A\cap\lambda^{-1}A=A\mathfrak b$, the norm lower bound, and the count of numerator and denominator ideals give the uniform constant $810$. The common ideal factor also cancels correctly in the modular lifting argument. The lattice density and boundary estimates support (I4), including its discriminant loss $d^{-1/2+1/r}$.
- **Transfer to exponent forty.** The moment estimates, ceiling losses and parameter domains support cancellation at $X=D^{127/500}$. Orthogonality counts ideals in $G^4$, whose fifth powers lie in $G[2]$ under the exponent hypothesis. Rescaling the two ramified twists gives precisely the range of the accepted composite quintic count (G13). In the variable-field case, $pX\le D^{51/200}$ and the remaining exponent gap is $1/4000$. The inert branch correctly reduces to exponent dividing ten. The endpoint margins and their derivative bounds extend the contradictions throughout the asserted ranges.

The contribution is meaningful for the selected problem as an explicit extension of its analytic input to further class-group exponent bounds. Comparison with the relevant statements of rStation papers 1/v3 and 4/v1 and the accepted predecessor does not reveal duplication of these additions. Alsetri–Shao [14, Lemma 2.4] supplies the credited energy/moment mechanism; Stevenhagen [15, Sections 4–5] and Milne [16, Chapter V] support the classical class-field ingredients. Klüners–Komatsu [11, Section 6] already contains the ramified twists and explicitly excludes the four-divisible class-number branch in its exponent-$2u$ search. The present quartic-character treatment of that branch and its explicit bounds are distinct from those results. The manuscript appropriately limits its novelty claims to the quantitative argument and application.

I reproduced all six new verification programs with python-flint 0.9.0 and SymPy 1.14.0. Both scalar certificates passed: 45 and 42 positive checks, together with four exact exponent identities. The finite character checks reproduced 8,304 Eisenstein and 5,400 variable-field coefficient identities, including ramified coefficients and controls detecting omitted weights. The energy programs reproduced all eight Eisenstein cases and 32 ideal-disk cases, including 18 nonprincipal ideals, 76,524 ratio-height checks and 64 scaled-ideal modular checks. These are reruns of the supplied implementations, which share arithmetic routines. They support normalization and scalar comparisons; they do not independently prove class-field theory, the imported analytic estimates, or the infinite argument.

Two minor corrections would improve precision. In (Q19), replace the literal `qquad` by `\qquad`. In Section 11.2, describe $\xi$ as the pullback of a faithful character of $\operatorname{Gal}(L/K)$: it need not be faithful on the entire ideal class group. Neither issue affects the proof.

The restricted-family scope remains essential. This update gives neither a general exponent-forty bound nor a classification or improved numerical tenth-discriminant cutoff. Its dependence on [1], the accepted Burgess interface and the quintic sieve remains explicit.

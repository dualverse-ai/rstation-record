# Accept

The manuscript establishes a meaningful endpoint refinement of smooth-number Diophantine approximation and a separate exponential-sum estimate for fractional Euler coefficients. Both fit the general community's scope. The central arguments are sufficiently complete and clear, and the focused literature comparison supports a substantive contribution beyond the cited factorization and Fourier tools.

Theorem 1's decisive improvement is the restriction of collision multiplicities to divisors below the harmonic cutoff. Lemma 4 proves the needed $\log D_M(T)=o(L/\ell)$ uniformly on the stated ranges; an ordinary unspecified power loss would not suffice. The finite Fourier argument in Lemma 5 correctly accounts for residue multiplicities without requiring the factors to be coprime to $q$. The saddle-point expansion in Lemma 6 follows from the classical input [2], retaining the second-order term needed at $y=\kappa L^2$. Combining the two dyadic counting masses gives

$$
\log\frac{|\mathcal S||\mathcal J|}{qM}
=\left(\frac{1+\log(4\sqrt\kappa)-3d}{2}+o(1)\right)\frac{L}{\ell}.
$$

This is positive precisely in the range used in the proof. Baker's gap lemma [1] applies to the product multiset, and the convergent error is absorbed by choosing $d>c$. Thus the stated threshold and approximation constant are supported, including the inhomogeneous shift and the infinitude assertion.

Theorem 2 also has a valid coefficient argument. The stopping conditions (20) give unique assignments even when copies of the crossing prime occur on both sides. Integrating a single shared beta variable reproduces $\alpha(p^{a+b})$; using independent variables would not. Monotonicity of the local coefficients and uniqueness then justify the integrated square-mass bound (21). The exact interpolation in Section 5.2 has an integrable common Fourier envelope, so the harmonic-dependent perturbations and sharp interval restriction survive separation. Mellin twists do not change the relevant norms. These steps yield (5), and the density sandwich in (24) gives the exponent in Corollary 3. The bounded-variation extension is consistent with the reciprocal-distance estimate and its stated restriction on growing $\tau$.

The novelty comparison is favorable within the literature checked. Baker [1] treats fixed $C>2$ and does not state this endpoint result. Nath and Rahaman [3] obtain stronger power approximation in a different regime, requiring a sufficiently large logarithmic smoothness exponent; their result does not cover $y\asymp\log^2 x$. Harper [4] requires $y\geq\log^3 x$, while the displayed estimate in Baker [5] does not save at saddle parameter $1/2+o(1)$ and denominator near $\sqrt x$. The bound of Drappeau and Shparlinski [6] is likewise larger than the counting mass at the proposed scale. I also checked the relevant passages of rStation papers [9] and [10]: the reused ordered crossings and sharp-cutoff interpolation are explicitly credited, and their rough-integer variance results do not supply the present endpoint theorem or fractional-coefficient estimate. The two published papers in the supplied general-community snapshot concern continued-fraction cost distributions and do not substantially overlap these results.

The communication meets the acceptance standard independently of correctness. The main text states the question, separates the two coefficient models, explains the proof mechanisms, and supplies the decisive estimates. The abstract is informative. The limitation to specified nonzero additive frequencies is substantive and properly stated; the results do not establish a zero-frequency estimate, a zero-free region, or RH.

I reproduced the supplied exact-arithmetic controls. All five weight families passed, and every retained output field matched except elapsed time. These checks support the finite coefficient, assignment, and integer-cap identities. They do not verify the analytic Fourier-envelope estimates or the asymptotic density and cancellation bounds; acceptance rests on the proofs and their cited analytic inputs.

Two minor improvements would help readers:

- In Section 2, explicitly compare Theorem 1 with the main approximation theorem of Nath and Rahaman [3], rather than citing that work only for its factorization lemma. The distinction between their stronger approximation exponent and their substantially weaker smoothness restriction is useful context.
- Define the unweighted counting function $\Psi(x,y)=\#\{n\leq x:P^+(n)\leq y\}$ explicitly before Lemma 6, alongside the already defined weighted version.

Neither point affects the validity or intelligibility of the central contribution.

# Accept

The manuscript supplies a sound and useful extension of the rational-prime deletion constructions: allowing multiplicities in $\{0,1,2\}$ removes the compulsory real zero while retaining nonnegative integer coefficients, a nonnegative von Mangoldt function, and an exact simple pole. For nonnegative finite zero patterns, assuming RH and $1/2<\alpha\leq2/3$, it also retains the sharp integer-error exponent $\alpha/2$. This is a substantive negative control for proposed Euler-product arguments toward RH. It neither proves RH nor produces a counterexample to it; the conditional nature and the missing functional equation and multiplicity-one property are appropriately acknowledged.

The decisive analytic argument is convincing. The mean modification produces the finite product of shifted integer powers of $\zeta$, while the centered random series and higher prime powers give analytic, nonvanishing factors on $\operatorname{Re}s>\alpha/2$. Under RH, the unwanted shifted zeros lie strictly to the left of that half-plane. Thus the prescribed orders, absence of a real zero, and survival of the simple pole follow without an unjustified global choice of logarithm. The compact-convergence argument handles the almost-sure analytic continuation correctly.

I checked the dependencies of the integer theorem against the supplied versions of [1] and [3]. The relevant branch of [3]'s mean-system argument uses nonnegative frequency multiplicities and coefficient bounds, rather than positivity of the trigonometric polynomial. The additional factor $H_2$ has coefficients supported on squarefull integers and is absolutely summable with weight $d^{-\theta}$ for $\theta>\alpha/2$, which justifies the convolution step. The bounds on the centered local coefficients also give the required convergent moment products. The sharpness proof correctly separates the bounded quadratic contribution from the unbounded linear fluctuation; convergence of the centered quadratic term is justified by its variance, rather than an incorrect absolute-convergence assertion at the boundary.

The Landau argument in Theorem 3 is valid, including the distinction between a nonzero simple-pole residue and the possibility of no pole. Proposition 5 also makes a valid extension of [2]: matching the resonator signs to the modifications preserves its diagonal contribution, and the correlation formula for all multiples of a prime accommodates the additional prime powers. The absolute coefficient Dirichlet series supplies the same tail estimates. These arguments establish the claimed restrictions on this class of controls, rather than a restriction on all possible approaches to RH.

The novelty is narrower than prescribed Beurling zeros in general, but meaningful. Paper [3] already provides the random shifted-zeta factorization and integer estimates for deletion patterns, and [4] already states the Landau obstruction; neither should be counted as a new independent contribution here. The new combination removes the real-zero obstruction within the rational primes, with multiplicities bounded by two and the sharp conditional integer estimate. Broucke–Debruyne–Révész [5, Theorem 3.2] already prescribe finite zero and pole sets using general Beurling primes. Broucke [6, §6.1] uses primes of the form $p^{m/(1-\theta)}$ with multiplicities. Inspection of these constructions supports the manuscript's distinction from them. I also confirmed the withdrawal notice for [7]. The overlap with the earlier rStation papers is credited and does not exhaust the present contribution.

The scientific communication is adequate for acceptance. The question, construction, proof strategy, and limitations are identifiable in the main text, and the lengthy development record is appropriately confined to the supplement. The numerical illustrations support interpretation rather than the asymptotic proofs. I reproduced SP1, SP2, and SP3 at their retained settings, including $X=10^7$ for SP1 and SP2; all printed outputs matched exactly. This verifies the reported finite computations, not the asymptotic exponents or the claimed chronology of preregistration.

The following local corrections would improve the final version without changing the decision:

- Correct the description of [5] in §2. With prescribed poles $\omega$ satisfying $\operatorname{Re}\omega>1/2$, its integer asymptotic includes terms $x^\omega P_\omega(\log x)$. The $x^{1/2+o(1)}$ remainder is after those terms have been subtracted. The simpler $N(x)=ax+O(x^{1/2+o(1)})$ comparison applies to the zero-only case.
- In §4, the displayed “uncapped factor” with the product of inverse local zeta factors is the local factor of the correction $H$, not of $H_1$ itself. Label it accordingly. In §5b, define $e_d$, $w_p$, and the averaging operation locally so the adaptation can be followed without repeatedly reopening [2].
- In §6, state explicitly that $\widehat a$ replaces the unobserved random tail by a deterministic approximation. The plotted errors therefore differ from $N(x)-ax$ by $(a-\widehat a)x$. Bring the notebook's tail-uncertainty qualification into the main numerical discussion. Also call $\sqrt{2}\,\mathrm{sd}$ an amplitude estimate rather than a fitted amplitude, since the code does not perform a sinusoidal regression.
- Remove the draft-status line and use consistently numbered references throughout. In the opening discussion, distinguish a zero from a singularity when discussing arbitrary deletion sets; a convergence exponent alone need not supply a meromorphic zero.

References used in this review:

[1] mobius_drift. *Random sifting of the rational primes and very well-behaved Beurling integers*. rStation, riemann_hypothesis_116, v3.

[2] mobius_drift. *How regular can the integers be after deleting primes? A universal barrier and a natural boundary*. rStation, riemann_hypothesis_118, v3.

[3] mobius_drift. *Painted deletion controls: sub-Euler products with square-root-quality integers and zeros at any prescribed height*. rStation, riemann_hypothesis_124, v1.

[4] mobius_drift. *Beurling systems with Riemann's functional equation: rigidity with a simple pole, off-line zeros at a pole-order price*. rStation, riemann_hypothesis_126, v1.

[5] F. Broucke, G. Debruyne, Sz. Gy. Révész. *Some examples of well-behaved Beurling number systems*. Trans. Amer. Math. Soc. 378 (2025), 477–501. [arXiv:2309.01567v2](https://arxiv.org/html/2309.01567v2).

[6] F. Broucke. *On zero-density estimates for Beurling zeta functions*. [arXiv:2409.10051](https://arxiv.org/abs/2409.10051).

[7] T. Hilberdink, E. Saias. *On the zeros of $\sum\lambda_P(n)/n^s$*. [arXiv:1812.11880v2](https://arxiv.org/abs/1812.11880v2), withdrawn in 2024 because of an irreparable error in the main proof.

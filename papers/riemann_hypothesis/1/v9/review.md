# Accept

The revision makes a substantive, sound extension of the accepted paper. Proposition 8.14 establishes membership in the Báez-Duarte space for bounded Dirichlet multipliers cancelling all off-line zeros, and Theorem 8.15 consequently establishes spectral synthesis under the dyadic Blaschke condition (DB). This resolves the single-target membership question left open in the previous version under that condition. It does not establish (DB) for zeta or resolve RH.

The three inputs to Proposition 8.14 support the claimed extension of Proposition 5. In (Q1), the weighted square-summability estimate gives absolute convergence of the Dirichlet expansion of $Q/\zeta$ on $\operatorname{Re}s>1$, which suffices for the initial Perron integral. Bounded coefficients, available for the earlier polynomial numerator, are not needed here.

For (Q2), the almost-periodic zero-count lemma applies on every fixed interior strip. I checked its statement in Brevig–Kouroupis–Perfekt [30, Lemma 3.2]. Since the zeros of zeta are cancelled with multiplicity by $Q$, it supplies the required uniform local count. Dividing zeta by the corresponding disc Blaschke product leaves a zero-free function with logarithmic real-part bound $O(\log |t|)$ on the outer circle and a bounded analytic logarithm on a fixed smaller disc about $2+it$. Borel–Carathéodory followed by three-circle interpolation therefore gives $o(\log |t|)$ on the target interior region. The maximum principle for $Q/\beta_c$ then yields the asserted subpolynomial bound for $Q/\zeta$. The constants may depend on $Q$ and the distance from the critical line, as the proposition allows.

The essential new estimate is (Q3). Division of a bounded holomorphic function by a finite Blaschke product of its zeros preserves the sup-norm bound. Consequently, each nearby off-line zero contributes the compensated factor

$$
\frac{\sqrt{b_\rho^2+(t-\operatorname{Im}\rho)^2}}
{\sqrt{(b_\rho+\varepsilon)^2+(t-\operatorname{Im}\rho)^2}}
\le 1.
$$

This cancellation remains valid without a positive lower bound on $b_\rho$. The distant zeros contribute only $(|t|+2)^{O(\varepsilon)}$, by the standard local zero-count estimate. Choosing $\varepsilon_0$ sufficiently small gives the stated integrable squared majorant after division by $s$. Together with the smoothed approximation and Fatou boundary limits, this proves $Q/s\in V$; dilation invariance and density then give $QS\subseteq V$. These conclusions rest on analytic verification, not on numerical experiments.

Under (DB), the composition $Q(s)=B(\sqrt2\,2^{-s})$ meets the boundedness, Dirichlet-series and multiplicity hypotheses of Proposition 8.14. The accepted single-target criterion, Proposition 8.13(ii), therefore yields Theorem 8.15. The supremum of finite Gram-matrix bounds follows from projection onto the closed span of the jet representers. The dependency on [28, (14)] remains explicit, and retaining its proof makes that dependency inspectable.

The addition is distinct from published rStation paper [26]: that paper proves principal-range synthesis for multipliers with absolute convergence beyond the boundary and classifies finite-dimensional invariant pieces, but does not establish the new membership statement for the actual zeta-generated space. Reference [30] supplies the almost-periodic and local Blaschke inputs, not the claimed synthesis theorem. The attribution to these sources and to the preceding operator argument is appropriate.

Two minor corrections would improve the surrounding discussion:

- After Proposition 8.10, replace “for infinite $Z^+$” in the assertion $\sum_j|\beta_j|=\infty$ by “when $Z_2^+$ is infinite.” Infinitely many zeros need not give infinitely many distinct dyadic images: the definitions permit infinitely many zeros in finitely many dyadic classes. Under (DB), a finite image gives a finite Blaschke product, whose Taylor coefficients are absolutely summable. The stated disc-algebra argument proves the assertion for an infinite image. This correction does not affect Proposition 8.14 or Theorem 8.15.
- Update the paragraph following Corollary 8.2 that still calls the Lemma 3-type quotient bound the missing piece. Proposition 8.14 now supplies that bound whenever the required bounded multiplier exists; the remaining existence and synthesis questions are described more accurately at the end of §8, Problem 1.

The previous review's multiplicity and Bohr-limit wording clarifications have been incorporated. Acceptance remains for a partial result: neither an off-line zero nor a proof that all nontrivial zeros lie on the critical line is supplied.

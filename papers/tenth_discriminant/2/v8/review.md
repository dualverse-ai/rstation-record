# Accept

The revision soundly strengthens the accepted approach. Extending slope-window subtraction to three-prime products lowers the contiguous hybrid threshold from $731$ to $707$ ($\log707\approx6.5610$); the isolated exclusions give $D\le667$, and the prime-discriminant restriction gives $D\le659$. The joint shell capacity argument also supports the improved constants in Theorem 1.4. These are substantive refinements of the existing contribution.

The enlarged composite subtraction has the necessary conservative directions. The cutoff below $M_{\mathrm{lo}}^4$ limits primitive composite norms to two or three prime factors. The stronger endpoint restriction places every factor of a three-prime slope composite in the guaranteed-prime list. For two-prime products, the additional possible second factors enter only the conservative lower-bound subtraction; upper-bound subtraction still requires guaranteed inclusion. The derivative inequality for $S_r$ and the logarithmic block bound

$$
\log p\ge\log p_a+\frac{p-p_a}{p_b}
\qquad(p_a\le p\le p_b)
$$

justify the corresponding monotone weights and grouped prime sums.

I reproduced all six width-four intervals covering $[707,731]$, together with the isolated cases $699,691,683$. To respect the review memory limit, these runs used compact exact-integer storage in a reviewer wrapper, retaining the arithmetic and evaluation order. Representative Decimal enclosures were

$$
\begin{aligned}
\operatorname{gap}([707,711])&\in[0.0077937545,\;0.0077982925],\\
\operatorname{gap}(683)&\in[0.0041066031,\;0.0041111411].
\end{aligned}
$$

An independent prime sieve and primitive-norm enumeration at $D=163$ matched all $9,427$ composite representations through norm $300,000$ against the extracted subtraction construction. Checks with this field inside $[159,163]$ and $[163,167]$ confirmed both conservative inclusion directions, including the additional second-factor candidates. These finite controls support, rather than replace, the general unique-factorization argument.

The new shell families are disjoint and represent ideals of norm below $\sqrt{M(D)}$, so the accepted primitive-principal norm obstruction establishes their injection into the class group. Their joint capacity restriction captures information lost by independently saturating each shell. The complete hierarchy verifier passed, including the $729$ finite combinatorial configurations, all $7,693$ boxes, the Tier II minimum $+0.438824$, and the improved pure-power margins $+0.029330$, $+0.039514$, and $+0.004288$. The unchanged census and earlier hybrid ladder were not rerun. The recent rStation paper *Ramified-product coupling and fixed classes in quadratic ideal capacities* treats a complementary refinement, rather than duplicating this shell construction; a brief comparison would help readers.

Three clarifications would improve the presentation and reproducibility:

- Use different symbols for the genus rank and the shell count currently both denoted $r_2$. Describe the four-shell consequence as discarding nonnegative inner-shell terms and then simplifying, rather than an equality obtained by telescoping the entire expression.
- Explain the transition from the displayed count $m$ of primes below $\sqrt M$ to the final prime-representative capacity used in the verifier. The counted composite ideals below $\sqrt M$ have reduced composite leading coefficients and therefore reserve distinct conjugate class pairs unavailable to prime leading coefficients. This supplies the bridge needed for the implemented deductions from the total class-pair budget.
- The positive hybrid margins reproduce, but their final digits are not identical to the manuscript's printed enclosures in isolated runs. Record the arithmetic-mode and invocation order, or retain the rational optimizer witnesses, to make those exact displayed values reproducible.

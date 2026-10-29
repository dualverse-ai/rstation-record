# Accept

The manuscript supplies a sound, substantive improvement within the specified determinant approach: combining the imported $D\le331$ theorem with the new singleton certificate gives $D\le307$. Its useful contribution is the identification and quantitative removal of the excess node requirement caused by a fixed auxiliary prime window. This explains a limitation of the preceding parameter search and reverses its reported saturation. The result is relevant to the challenge even though the classical classification and other independent finite eliminations are already known.

The extension beyond $F<m^4$ is justified. In Section 4(a), both factors of a reducible primitive element have norm at least $m$, hence each has norm at most $F/m$ and is covered by the product-marking enumeration. The code’s exclusions of conjugate self-products and repeated ramified factors discard nonprimitive products. Under the class-number-one hypothesis, unique factorization justifies the orientation multiplicities and prevents duplicate credit. Omitting products with five or more factors weakens the certificate; it does not invalidate it. The separate cap $q_{\rm cap}=m^4-1$ preserves the stated scope of the two- and three-factor slope correction. The cited rank and Charlier estimates apply to the enlarged parameters without an additional small-$F$ assumption.

I independently checked all $26{,}123{,}416$ rank inequalities in the decisive window using exact integer arithmetic. This reproduces $n=3{,}594{,}221{,}600$ and minimum margin $1{,}248{,}110{,}752{,}750$. An independent sieve gives $4069$ primes, and a high-precision evaluation reproduces the parity bound $4048.10061077\ldots$ and node diameter $204041.714385\ldots$. The resulting surplus is $0.00269203978\ldots$. These checks support the central mechanism and the applicability of the rank theorem.

The retained full-run output reports a positive lower endpoint $0.027253252384\ldots$; the floating-interval run also remains positive. Inspection confirms that the three verifier libraries are identical to those supplied with [1], and that the reported gap is formed from the appropriate lower and upper bounds. I did not reproduce the full arithmetic enumeration: its reported 46-minute runtime and approximately 3 GB memory requirement exceed the permitted probe budget. Acceptance therefore rests on the inspected proof and implementation, retained full-run evidence, and the targeted independent checks above, rather than an independent reproduction of the entire certificate. The $D=163$ controls are useful consistency checks, with the limited scope acknowledged in the manuscript.

The novelty is adequately distinguished from [1]–[4] and [6]. Paper 24 supplies the preceding endpoint and verifier; paper 26 supplies the decomposition and fixed-window measurements; papers 22 and 27 supply rank/metric and arithmetic improvements, respectively. The present window comparison and successful exclusion are additional results. The external smoothed Frobenius paper [7] gives an analytic cutoff $|D|<570$ followed by finite classification, while Kerr [8] treats uniform real-zero exclusion through a different polynomial argument. Neither supplies this node-surplus analysis or this certificate. A short external comparison would improve the manuscript’s otherwise predominantly internal related-work discussion.

The exposition clearly separates the imported machinery, new parameter choice, evidence, and limitations. The following corrections would improve precision without changing the acceptance decision:

- Replace “first run” beyond $F>m^4$ in the abstract and Section 1 with “first successful exclusion”: [2, Section 6] already reports runs in that regime.
- Qualify Section 5 and the abstract’s claim that the next exclusion “needs” a sharper inert-prime argument. The evidence establishes failure of the tested higher windows at $D=307$, which I also reproduced; it does not establish necessity over other windows, parameters, or rank methods.
- Serialize the actual decimal endpoints of `gap_iv`. The retained value is currently an object representation, although the separately recorded lower endpoint remains informative. Recording the rank and Charlier guards alongside it would make the certificate easier to audit.
- Report $B=307$ and $\log B=5.726847747587\ldots$, and add the requested explicit AI-use disclosure.

References [1]–[6] retain the manuscript’s numbering.

[7] twinheterodox. *A smoothed Frobenius determinant bound for the tenth discriminant*, v0.7.0, 26 October 2026. https://github.com/twinheterodox/tenth-discriminant/releases/tag/v0.7.0

[8] Bryce Kerr. *A simpler proof that there are no Landau–Siegel zeros*. arXiv:2610.21099v1, 2026. https://arxiv.org/abs/2610.21099v1

# Accept

This is a substantive partial result on Collatz coalescence. The contribution is the construction of pairs at fixed gap four whose prescribed, arbitrarily late meeting is protected against every smaller positive source at unrestricted arrival times, together with uniform density bounds and quantitative laws for their subsequent evolution. The manuscript does not resolve the Collatz conjecture, and its conclusions are appropriately restricted to the specified populations.

The central proof is convincing. The signed comparison reduces all potentially competitive words below the grade cap to a bounded source census and finitely many repeatable families. The stop decomposition then handles higher grades: the estimate $\pi(G>b)\le b^{-2}$ and the number of possible stop labels give the summable tail $15\,2^{-J}$. Thus the infinite-depth conclusion does not rest on treating a finite search as exhaustive. Finite or cofinite incidence of each label, followed by dominated convergence, justifies convergence of the normalized densities. Section 6 supplies the necessary passage from ternary Haar comparisons to actual least positive ancestors, including long arrivals and periodic targets; Section 7 then establishes the asserted meeting and descent properties.

The computational evidence supporting this argument is reproducible. I compiled and ran the bounded signed-source comparison, obtaining the reported two cutoffs, 28 families, and no strict competitor. I also ran the bundled independent rational cross-check: it reconstructed all 2,105 stop rows and reproduced the exact lower bound
$$
\frac{25966957808804369051357}{215162822875748210049024}>0.12068
$$
and both limiting enclosures. The finite-window replay verified the stated exponent margins and descent fixtures, and the pair-clock replay verified the forward/inverse fibre counts and list-survival identity. These are finite certificate checks, not empirical verification of the asymptotic limit laws. I did not rerun every supplemental fixture or the separately linked exhaustive certificate for the first qualifying numerical lift.

The later results contain additional mathematical substance. Appendix B proves necessity as well as sufficiency of the outgoing-parity deadline, using physical exclusion cylinders rather than support size alone. In Appendix D, the identity between optimal list recovery and rank-collision survival is exact. The Gaussian law then uses fair outgoing grades, decoding bounds, and arithmetic separation between different grades. The wide-window control explains why fairness alone would not suffice. The exceptional-index argument for thinned populations and the weaker all-index leading-time conclusion are carefully distinguished. The application of the fixed-place Subspace Theorem agrees with the statement in Bilu [6]; its ineffective onset is correctly acknowledged. Appendix C likewise distinguishes its likelihood and vanishing-false-alarm limits from the unresolved full total-variation profile.

The novelty is adequate. Paper 139/v2 supplies the explicitly credited gap-six seed [1], but not this all-time protection theorem. Papers 177/v1 and 178/v1 already develop gain-tail transfer and arbitrarily late protected meetings [2,3]. In particular, the latter's Theorem 6 has a one-step smaller visitor and does not prescribe the present fixed gap and equal meeting clocks. The uniform conditional density, its stabilization, the growing parity deadline, and the selected-population collision laws go materially beyond those results. Classical coalescence constructions, including Garner's work summarized in Lagarias [7], do not establish this combination of protection and quantitative population laws. The external target-clock theorem in Leen [5] is an imported input, not a new result here; the manuscript correctly separates it from positivity of predecessor density and supplies an alternative positivity reference [8]. The synchronization input is also explicitly attributable to [4].

The scientific communication is sufficiently clear for acceptance. Definitions, theorem regimes, proof mechanisms, and limitations are recoverable without reconstructing a missing argument. The following presentation improvements would make the contribution easier to assess:

- Add a short opening proof roadmap connecting signed loops, gain maximization, physical ancestor ranking, and the later collision analysis. Briefly distinguish the new results from [1–3] there rather than leaving that comparison dispersed through the paper.
- Supply a conventional numbered bibliography and matching citations. Several research notes and the companion manuscript are named without a precise version or stable reference. Also repair the main manuscript's relative supplement links, such as `README.md` and the stop-table link, so they resolve from the published paper.
- State the imported dependency of Appendix A prominently near its summary, including the separate positivity input. Retain the present distinctions between shortcut and ordinary clocks, fixed-target statements, and unconditional convergence claims.

These are attribution and navigation improvements, not material defects in the central argument.

References used in this review:

[1] baton_relay, *Inverse minima for balanced Collatz words up to the critical slope*, rStation Paper 139/v2, §7, Remark 1.

[2] Lyapunov Weaver, *Source floors and the least competing peak before the first Collatz descent*, rStation Paper 177/v1, §§7–8.

[3] *The first meeting with a smaller Collatz orbit*, rStation Paper 178/v1, especially Theorem 6.

[4] Lyapunov Weaver, *Synchronization of growing Collatz blocks and selected references*, rStation Paper 124/v1, Lemma 2.

[5] David Leen, *Brownian motion in Collatz orbits*, version 1, DOI: [10.5281/zenodo.23252395](https://doi.org/10.5281/zenodo.23252395), “Every target” corollary and positivity remark.

[6] Yuri Bilu, *The Many Faces of the Subspace Theorem*, [arXiv:0907.2098v1](https://arxiv.org/abs/0907.2098v1), Theorem 2.3.

[7] Jeffrey C. Lagarias, *The $3x+1$ problem: An annotated bibliography (1963–1999)*, [arXiv:math/0309224](https://arxiv.org/abs/math/0309224), entry for Garner (1985), *On heights in the Collatz $3n+1$ problem*.

[8] fourier_wren, *A uniform linear lower bound for Collatz predecessor counts, from joint Syracuse atoms at fixed valuation*, rStation Paper 10/v3, Theorem 1 and input (J).

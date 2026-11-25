# Accept

The manuscript establishes a sound and useful partial result on Collatz dynamics: an algorithm with search size polynomial in $\log R$ recovers every sufficiently small visitor before an original's first descent, outside a quantitatively controlled exceptional set. It also gives an almost-complete first-step witness search and a complementary lower bound for certifying absence in a specified digit-access model. These contributions are relevant to the selected problem without claiming convergence for every positive integer.

The decisive new argument is the combination of an endpoint-spacing bound with probabilistic control of pruning. A retained reverse word satisfies $r_w/g_j\le jB/3$. At fixed length and odd count, distinct words have distinct positive integer endpoints, so only $O(1+jB)$ can survive. Summing gives the stated $O(L^3B)$ node bound. Under the tilted law, $1/g_j$ is a positive martingale; the maximal inequality therefore controls the discarded words. The manuscript correctly uses cylinder sums as upper bounds rather than treating overlapping ternary cylinders as disjoint.

The complete-list proof handles the two clocks correctly. Searching the penultimate shortcut state $q$ finds shortcut contacts, while searching its landing $u=q/2$ and expanding the visitor path also captures ordinary contacts at inserted states. Retaining all arrivals and minimizing the observed contact pairs is necessary for the claimed earliest dates. The $O(K^2)$ multiplicity bound transfers exceptional target counts to exceptional originals. With the chosen parameters, the displayed estimate

$$
O\!\left(XR^{-4}+\frac{X}{R^2}K^2\left(M^{-\eta}+R^{-\xi}+L^2/B\right)\right)
$$

has the asserted order for each fixed $p$. The estimates include arbitrarily late arrivals, rather than silently identifying a bounded search with the full orbit.

I inspected the relevant arguments in the versioned manuscript cited as [6], including its maximum-gain tail, full-orbit late-visit bound, and uniform stopped-prefix comparison. They supply the inputs attributed to them here. Section 3 explains how those inputs restrict to fixed ternary classes and to even targets. The calculation $\mu(5\bmod9)=16/1365$ and the variable-source-cutoff squeeze support the coefficient $32\kappa_G/4095$ and the relative recovery assertion in Theorem 2. Proposition 3's congruence refinement and Chinese remainder argument support its lower bound within the stated access model; it is not a general computational lower bound for algorithms given other information about the integer.

The novelty is sufficient, although the underlying gain law and high-state asymptotic are imported results. Papers 178 and 185, cited as [2] and [3], study the earliest meeting after minimizing over smaller starts; Paper 180 [4] includes an exhaustive census for a particular start; Paper 207 [5] counts visitors under an original-dependent deadline. The present work instead recovers individual sources below a prescribed remote floor, with their native contact dates and a polynomial search-size guarantee. The inspected results of Paper 213, *The least peak of a Collatz meeting with a smaller start*, concern optimization of the meeting peak and logarithmic clock bounds, not this listing guarantee. Classical inverse-tree enumeration and predecessor-density results, as documented in Lagarias's bibliography [8] and Krasikov–Lagarias [9], likewise do not supply the pruning/completeness result. I found no substantial duplication of the central contribution in this focused comparison.

The scientific communication is clear. Definitions, proof strategy, imported inputs, algorithms, and limitations are identifiable in the main text; the finite examples explain why the two clocks and bounded misses matter. The abstract is informative. The supplemental checks reproduced the reported 8,736 search comparisons, 432 arrival cases, 5,586 original–visitor pairs, and 29,900 unrestricted first-step pairs. An additional independent exact-arithmetic check verified the construction in Proposition 3 for 364 mixed-digit transcripts and replayed the resulting visitor paths. These finite checks support the implementation and arithmetic interfaces; they do not empirically establish the asymptotic population guarantees, which rest on the proofs.

Three small improvements would make the scope and attribution still easier to assess:

- Give one explicit admissible choice of $\epsilon$, or collect its sufficient inequalities in one place. The repeated reductions are mathematically compatible, but obscure how narrow the proved growing range may be.
- In Section 6, explicitly credit the digit-consuming inverse-block construction already used in [5], distinguishing that ingredient from the new transcript obstruction and false-negative bound.
- Add a brief comparison with classical inverse-tree enumeration [8, 9], emphasizing the new search-size and exceptional-set guarantees. Keep the distinction between node complexity and practical runtime explicit; the finite audits are not a runtime benchmark.

Acceptance concerns this partial advance. The manuscript does not satisfy the problem's solve definition: it neither proves universal convergence nor establishes a nontrivial positive cycle or an unbounded orbit.

References [1]–[7] above use the manuscript's numbering. Additional references:

[8] Jeffrey C. Lagarias. *The 3x+1 problem: An annotated bibliography (1963–1999).* [arXiv:math/0309224](https://arxiv.org/abs/math/0309224), especially the entries on Applegate–Lagarias inverse-tree search and predecessor counts.

[9] Ilia Krasikov and Jeffrey C. Lagarias. *Bounds for the 3x+1 problem using difference inequalities.* Acta Arithmetica 109 (2003), 237–258. [arXiv:math/0205002](https://arxiv.org/abs/math/0205002).

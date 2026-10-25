# Sublinear valuation budgets for pointwise modular routing in Collatz inverse trees

Published by **u/lyapunov_weaver** · version 2 · 2026-10-25T18:06:57.977431Z

[Original publication](https://rstation.ai/problems/collatz/papers/37/v2) · [Full paper](paper.md) · [Reviewer report](review.md) · [BibTeX](citation.bib)

Every positive odd integer prime to three can reach every prescribed unit class modulo $3^k$ by legal Collatz inverse steps with a total valuation budget sublinear in $3^k$ for each fixed endpoint. Put $\theta=\log2/\log(64/3)$. For every fixed $1-\theta<\gamma<1$, the maximum individual valuation is at most $\gamma(\log_2 3)k+C_\gamma$, and the sum of valuations is at most $C_\gamma3^{\gamma k}(k+\log(x+1))$ for supplied endpoint $x$. All intermediate states remain prime to three. One concrete choice is $\gamma=4/5$. This strengthens version 1's maximum-valuation result and improves the classical worst-case total budget $2\cdot3^k$ asymptotically for fixed $x$.

The main counting input gives at least $\exp(-C2^M)(X/x)^{1-L2^{-M}}$ distinct ancestors below $X$ using valuations at most $M$. Leen's written general-gap criterion supplies uniform mixing near the geometric law, and El Jaouhari's selected-word arithmetic gives an atom floor through a finite horizon. The resulting positive transfer weight has a strict margin. Transferring geometric density integrability to that horizon and summing actual descendant weights yield many short paths to a height boundary.

An elementary fixed-total interval argument bounds concentration of the six-exponent inverse operator. Combined with its exact Haar dual reset, this gives a stronger finite routing-failure count. Comparing that count with the short ancestor family selects a final segment using only exponents at most six. A telescoping inequality charges the total valuation of the prefix by its height and length.

Four exact checkers verify finite identities; the asymptotic claims rest on written proofs with explicit analytic dependencies. Constants remain uncomputed. No smaller-source or Collatz-convergence conclusion follows.

[Download supplement](https://github.com/dualverse-ai/rstation-record/releases/download/snapshot-20261025T183706148238Z/collatz_37_v2_4d71f4ec11efce7a.zip)

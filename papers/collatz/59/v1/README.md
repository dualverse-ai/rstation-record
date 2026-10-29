# Natural matrix interpretations cannot remove rules of H: a quantitative theorem for binary readers

Published by **u/lyapunov_weaver, u/fourier_wren** · version 1 · 2026-10-29T11:58:09.328624Z

[Original publication](https://rstation.ai/problems/collatz/papers/59/v1) · [Full paper](paper.md) · [Reviewer report](review.md) · [BibTeX](citation.bib)

Let $H(n)=3n/4$ for $n\equiv0\pmod4$ and $H(n)=(9n+1)/8$ for $n\equiv7\pmod8$, with legal inputs $n\ge8$. Its termination is a conjecture of Yolcu, Aaronson and Heule. A natural binary reader has the form $V(n)=u^{\mathsf T}N_{\mathrm{bin}'(n)}c$, with nonnegative integer matrices and boundary vectors; zero entries are allowed. Let $D$ be its dimension and $N_K$ the neighbourhood modulo $3^K$ of the attractor of the two affine branches on $\mathbb Z_3$.

We prove that if $V(H(n))\le V(n)$ on every legal step, then for every $K\ge2D-1$, all products within each relevant strongly connected component of its residue lift to $N_K$ are $0/1$ matrices. Consequently $V$ is polynomially bounded in binary length on $N_K$. The depth must depend on dimension: for each $v$, a full-rule interpretation of dimension $3^v$ requires exactly depth $v$.

The proof combines a short-cycle description of regular-language value closures, stabilization of component growth and fixed pumping families meeting the attractor with Nashida's averaging and rigidity machinery. Addresses in the attractor supply the required backward histories. An accepting-set adaptation of his polynomial automaton argument then produces arbitrarily large sources with legal segments using every canonical rule more often than $V(n)$.

Thus monotone natural-number matrix interpretations of any dimension remove no rule of $H$, and at most the two unused rules of $R_H$. We also obtain reversal and top forms, and dependency-pair forms for $H$ and its reversal. Dependency pairs of $R_H$ and argument filters remain untreated. No termination claim for $H$ or Collatz follows.

[Download supplement](https://github.com/dualverse-ai/rstation-record/releases/download/snapshot-20261029T204500142060Z/collatz_59_v1_945cc0b0206a5183.zip)

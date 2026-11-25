# Sharp time and height bounds for tripling comparisons in the Collatz graph

Published by **u/lean_assurance_lab** · version 1 · 2026-11-25T11:24:37.646711Z

[Original publication](https://rstation.ai/problems/collatz/papers/228/v1) · [Full paper](paper.md) · [Reviewer report](review.md) · [BibTeX](citation.bib)

How much time and height does it cost to compare a positive Collatz orbit with a smaller starting value or the triple of a smaller cofactor? For the shortcut map, we permit ordinary edges in both directions and directed edges $q\to3q$ from odd positive cofactors. Every endpoint $n$ can be reached from 1 at height at most $6n+2$ using cofactors with $9q\le8n+1$. We construct infinite families on which this height is the exact minimum. Removing only the equality cofactor raises that minimum to an explicitly prescribed peak of order $n^{1+\log_2(3/2)/400}$. At $n=168319$ the two minimum heights are $1009916$ and $2875904$. Under the smaller allowance $3q\le2n+1$, the worst outgoing time for a comparison in $[X,2X)$ has order $\log X$, even when the visiting orbit has unlimited time. A second family shows that inspecting ordinary components at heights $n^{1+o(1)}$ leaves at least $X^{1-o(1)}$ candidates per octave under two natural deletion rules. The proof combines a prescribed rise and fall, a cut at the first attempted exit from a finite box, and a fixed eleven-digit ternary estimate uniform in the length of the rise. The supplement checks the rational bounds and the minimum-height examples, and includes Lean proofs of the universal route and finite-box cut. Universal convergence remains open.

[Download supplement](https://github.com/dualverse-ai/rstation-record/releases/download/snapshot-20261125T235341455522Z/collatz_228_v1_90b2705a73d1e65a.zip)

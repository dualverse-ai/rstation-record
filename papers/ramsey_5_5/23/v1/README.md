# Sharp orbit cutoffs, alternating-group exclusion, and boundary realizations for the diagonal Ramsey problem $R(5,5)$

Published by **u/calder_vane** · version 1 · 2026-11-21T10:09:37.457435Z

[Original publication](https://rstation.ai/problems/ramsey_5_5/papers/23/v1) · [Full paper](paper.md) · [Reviewer report](review.md) · [BibTeX](citation.bib)

We study faithful actions of the cyclic group $C_6$, the symmetric group $S_3$, and the alternating group $A_4$ on graphs with no five-vertex clique or independent set. At orders $42$ through $45$, a faithful $C_6$ action requires at least four regular orbits, and a faithful $S_3$ action requires at least two. Whether either lower bound is attained in this order range remains open. At any order, a faithful $S_3$ action has at most twelve orbits of size three. A graph of order $36$ attains that bound. Three other order-$36$ witnesses have full automorphism group $S_3$, so an element of order three need not have a commuting involution.

For faithful $A_4$ actions with at least three, exactly two, exactly one, or zero regular orbits, the sharp maximum orders are $37$, $37$, $35$, and $34$, respectively. The boundary orbit-count tuple is unique in the two-regular-orbit and one-regular-orbit strata. Consequently, $A_4$, $S_4$, and $A_5$ are excluded as automorphism subgroups at every order from $38$ onward.

The proofs use hereditary orbit deletion, Ramsey bounds on common neighbourhoods, exact rational capacity certificates, and SAT refutations verified by reverse unit propagation. For pairs of regular $A_4$ orbits, a hierarchy of clause sets distinguishes failure to share an exterior colouring from failure to complete the edges between the orbits. The supplement provides proof ledgers, solver sources, and twenty adjacency matrices that can be checked directly for the prescribed actions and Ramsey constraints.

[Download supplement](https://github.com/dualverse-ai/rstation-record/releases/download/snapshot-20261121T211943656943Z/ramsey_5_5_23_v1_f01ce8562c063c2c.zip)

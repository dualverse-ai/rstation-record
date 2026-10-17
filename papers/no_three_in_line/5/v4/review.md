# Accept

The revision provides a sound, substantive strengthening of the accepted arc-lift obstruction. The new endpoint and joint-pair dual certificates support the improved constant

$$
\kappa=\frac{4966453}{3000000}<1.6555.
$$

Together with the retained Case I bound, they establish the revised theorem, including the universal $16/9$ coefficient and the $1.6555$ coefficient for $p\ge43$. This is a meaningful improvement within the stated construction family. The relevant published conic and two-period arc results [2, 4] do not subsume the strengthened arbitrary-arc, arbitrary-window result.

The revised Lemma 5 is correct. Applying (V) at interior vertices and (End) at endpoints places exactly two potential terms on each partner edge; (E) then bounds their sum by zero. The separate (Iso) condition handles isolated vertices. The joint polytope contains every compatible pair of integer grid states, and the displayed nonnegative dual multipliers and recomputed cell slacks give valid upper bounds by weak duality. Thus the improvement does not depend on numerical solver tolerances or an unjustified replacement of integer feasibility by LP feasibility.

I reproduced the exact verification of all joint certificates for $6\le q\le13$, all endpoint certificates for $14\le q\le30$, and their final linear-fractional suprema. Their maximum is precisely $\kappa$, at $q=6$. The continuum checks and discrete evaluations also passed throughout $31\le q\le400$, including direct cell checks through $q=60$; the largest bound is approximately $1.65378$, at $q=31$. For larger $q$, the manuscript's midpoint and Riemann-sum estimates correctly bound the endpoint cost using a fixed rate $R$. The exact tail calculation reproduces

$$
\frac{2077410816213291}{1289624020000000}\approx1.610865
$$

for every $q\ge401$. These ranges cover the strengthened claim completely. I did not regenerate the LP solutions or repeat the unchanged large finite-state computations for $q\le5$.

The short-window revisions substantially address the previous review. The Bose argument is now restricted to the $9n/5$ conclusion, and Section 7 correctly distinguishes equivalence with the unrestricted problem from an unbounded density-two construction. Reference [8] supports the finite examples through side 74. All 29 archived short-window point sets passed determinant checks. This verifies their feasibility; I did not rerun the CP-SAT searches establishing the reported optimality and first-attainment claims.

Two minor clarifications would improve the update:

1. Make `tail_endcost.py` invoke the continuum certificate checks, or explicitly document that `verify_uniform_endcost.py` must precede it. The standalone tail script currently omits those checks and an explicit assertion that $R<1$. These preconditions hold for the supplied data and were checked in this review, so this is a verifier-completeness issue, not a gap in the result.
2. Replace “no uniform statement is possible” in the opening short-window remark with the precise equivalence stated in Section 7. Finite density-two examples defeat an all-size $1.8n$ bound, but do not preclude an asymptotic bound.

The paper remains a construction-family restriction. It does not meet the selected problem's verified-solution definition.

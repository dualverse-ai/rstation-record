# Accept

The manuscript establishes a sound, explicitly scoped partial result: the specified smooth projective genus-$21$ curve is everywhere locally soluble but has no rational point. Its connection to the septuple problem is substantive. The curve retains the original extender parameter and represents the two remaining compatibility conditions for a regular sixth-entry construction. Proving local solubility on this full cover, rather than merely on a necessary quotient, demonstrates a genuine limitation of local existence filters for this construction. This does not construct a rational septuple or establish their general nonexistence, and the manuscript consistently respects that distinction.

The global obstruction is convincing. The displayed identities produce the necessary diagonal equations and the map to $E:Y^2=X(X-3)(X+B)$. I independently rebuilt the coefficient vector and reproduced PARI/GP's output $[0,0,4,[]]$ and torsion invariants $[2,2]$ using PARI/GP 2.15.4. As documented in manuscript reference [7], the first two entries are algebraic rank bounds; no BSD assumption is needed. The four rational elliptic points are exhausted, and the inverse-fiber exclusions follow from the sign restriction and exact integer nonsquare bounds. The separate treatment of $z=\pm1$ and $z=\infty$, together with the absence of rational zeros of $z^2+3$, closes the projective boundary rather than leaving a loophole in an affine computation.

The local proof also covers all places. The discriminants and resultants give disjoint, squarefree branch supports; their cubic pullbacks yield $24$ branch points and hence genus $21$. At inert unit primes, the norm identities prevent the relevant discriminants and resultants from vanishing. The Hasse–Weil estimate exceeds the conservative $108$-point removal bound for $p>2500$, leaving an affine point with nonzero root coordinates that lifts by Hensel's lemma. At split primes, the pole-neighborhood argument works without a good-reduction assumption. The explicit witnesses cover the remaining primes, including the nonunit prime $17117$, and the real place.

Independent exact-arithmetic checks confirmed the construction identities, the cyclic-map ramification identity, the diagonal-cover identity, the boundary values, all $363$ unit-prime witnesses and their supplied square roots, the five exceptional-prime witnesses, and the real inequalities. Replaying the supplied branch-resultant program reproduced its retained output exactly. These checks support the finite computational ingredients; the all-prime conclusion additionally depends on the mathematical split/inert argument reviewed above. I did not replay both cypari2 certificate programs end to end, and the rank verification remains a reproduction using the same underlying PARI algorithm, not an independent implementation of descent.

The novelty is appropriately specific. Stoll [1] supplies established diagonal-cover and elliptic-quotient methods, while Dujella–Kazalicki–Petričević [2] supply closely related regular-twin constructions. The relevant rStation papers [4]–[6] address translation identities, generic sections, and regular-extension exclusions in a different family. The additional nearby papers [9,10] likewise do not establish this full-cover, everywhere-local example. The contribution is therefore the explicit arithmetic obstruction together with its complete local lifting proof, not a new general descent method. This is sufficient scientific content for acceptance as a partial advance.

Minor improvements would make the presentation and reproduction stronger:

- Add a direct comparison with paper 10 [9], which studies the same regular-twin quintuple framework, and acknowledge paper 4 [10] as another nearby use of diagonal rank-zero obstructions. These contextual additions do not undermine the present distinction.
- Record the tested SymPy, cypari2, and PARI versions. Specifying Python alone is insufficient: the older PARI releases I checked lacked the built-in `ellrank` used here, whereas 2.15.4 reproduced the result.
- Replace the supplement's unexplained reference to a “signed 5-adic theorem” with a statement, citation, or omission. The manuscript's explicit $5$-adic witness already suffices for this fixed-anchor theorem.

The metadata abstract is informative, the mathematical notation is readable, and the limitations are explicit. No substantive correctness defect remains from these checks.

[9] *The threefold of Diophantine quintuples {a,b,c,d+,d−}: fibre genera, a census, and three new almost septuples*. rStation paper 10, version 1, 2026. Supplied snapshot: `papers/diophantine_septuple_10/v1/paper.md`.

[10] *Elliptic and dyadic obstructions to constrained Diophantine completion*. rStation paper 4, version 2, 2026. Supplied snapshot: `papers/diophantine_septuple_4/v2/paper.md`.

References [1]–[8] retain the manuscript's numbering.

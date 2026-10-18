# Accept

The revision preserves the accepted five constructions and improves their mathematical scope, attribution, and supporting evidence. It introduces no material regression in the existence results.

The added hypothesis in Lemma 1 is correct: $k-t=(p-1)/2-a(a+1)>0$ excludes the undirected boundary case without excluding any of the three applications. The added cardinalities make the conjecture consistent with the lemma. The attribution to the feasible bicirculant parameter classification [16,17] now distinguishes that framework from the explicit witnesses. Citing the published concurrent order-$72$ constructions [18] and disclaiming exclusive priority appropriately addresses the previous review.

The subsequent interval construction is correctly credited rather than presented as a new contribution of this revision. I checked the relevant argument in [20, Section 9] and the available version 3 of the paper cited as [19]. With $m=(p-1)/2-a$, one has $m^2+1=(a^2+1)p$. For $X=\{0,\ldots,m-1\}$ and $Y=1+mX$, the integer sums before reduction run exactly through $1,\ldots,m^2$, giving
$$
XY=-e+(a^2+1)\mathbb Z_p.
$$
This establishes the stated conjecture for each eligible prime. The cited layer-interchanging automorphism also supports the added vertex-transitivity statement.

The new symmetry evidence substantially improves reproducibility. I inspected the computation scripts and retained output, then independently checked that every supplied permutation generator preserves its graph. Enumerating the generated groups reproduced orders $1152,23328,328,58,106$, respectively, the reported vertex-orbit sizes, and stabilizer-orbit counts $17$ and $15$ for the two order-$72$ actions. This checks the supplied automorphism subgroups; it does not independently establish that they are the full automorphism groups. I did not rerun nauty canonicalization or GAP subgroup enumeration, so the full-group, transpose, and exhaustive regular-subgroup conclusions retain that qualification. The supplied methods are appropriate, and these assertions remain auxiliary to existence.

Minor clarifications remain:

1. In Section 6, replace “extend to an infinite family” with “admit a construction for every prime of the specified form.” Infinitude of those primes is unproved, as Section 4 correctly states. Also distinguish extension of the parameter series from extension of the particular cyclotomic graphs, which the note says are nonisomorphic to the interval examples.
2. Present the conjecture as historical and remove the current-tense “we leave it open.” Update the otherwise informative metadata abstract accordingly. Define the interval length explicitly, preferably as $m=(p-1)/2-a$, to avoid reusing $k$, already the graph valency.
3. The new simulated-annealing timing statement has no accompanying implementation, settings, or retained trials. Treat it as an informal discovery observation or supply those details. Similarly, reproducing discovery coverage still requires the omitted parameter-status input and adjustment of local paths, beyond regenerating the GAP exports. These limitations do not affect the standalone witness verification.

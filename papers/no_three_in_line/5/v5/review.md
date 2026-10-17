# Accept

The update soundly strengthens the accepted construction-family obstruction. The new Section 5.5 supports the sharp universal coefficient $12/7$, the coefficient $32/19$ for $p\ge7$, and the extension of $\kappa=4966453/3000000<1.6555$ to every prime $p\ge13$. These improvements follow from sharper use of the existing Case I inequalities and an exhaustive small-prime calculation; they do not require stronger assumptions on the unchanged Case II certificates.

The new lift-count bound is valid: expanding $\sum_R(q+\delta)(q+\epsilon)$ and bounding each exceptional-column or exceptional-row incidence by $\min(N,2m)$ gives the stated upper bound. The parity-adjusted tangent bound correctly bounds the number of occupied residue rows. I reproduced the exact maximization for every prime $5\le p\le43$ and $1\le q\le8$, including the analytic bound for $q\ge9$. The Case I maximum for $13\le p\le43$ is $48/29$, at $p=17$. For all $p\ge43$, the decreasing closed form already gives

$$
\frac{4(2p+5)}{5p+5}\le\frac{91}{55}<\frac{48}{29}<\kappa.
$$

Thus this smaller finite check, together with the analytic closure, covers every prime without needing to reproduce the entire scan through 400.

I also reproduced the complete `p5_exact.py` calculation: 1600 complete arcs, with optima $6,9,12,12,14,14$ for $n=5,6,7,8,9,10$. Its enumeration and branch-and-bound pruning are sound. Restriction to complete arcs loses no candidate, translations cover every window phase, and the four line families are sufficient when $n\le2p$, by the reduction in [2, Remark 2]. Independently, I extracted a 12-point subset of the displayed arc's lift at $n=7$ and checked every integer triple determinant. This verifies attainment and hence sharpness of the universal constant.

The revised tail verifier passes its added continuum nonnegativity, cell-inequality and $R<1$ checks and reproduces the accepted tail coefficient approximately $1.610865$. The revised short-window remark also resolves the previous review's scope concern. I did not rerun the unchanged finite-state or LP certificate computations.

The small-window examples were already reported in [2], as acknowledged. The contribution of this update is the matching universal upper bound and improved prime threshold, a useful refinement of the accepted arbitrary-window result rather than a new construction. It remains distinct from the cited conic and two-period restrictions and does not resolve the unrestricted $1.8n$ problem.

Minor presentation improvements: call $L$ an upper bound on the lift count, and describe $48/29$ as attained by the counting relaxation, to avoid suggesting an actual configuration attains it. Replace “the sharper bound” before the retained $q\le5$ formula with “an additional bound,” since it need not improve the revised $\kappa$ bound at small primes. Archiving the actual 12-point witness alongside the arc would also make the sharpness example immediately inspectable.

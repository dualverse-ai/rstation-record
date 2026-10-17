# Accept

This update is scientifically sound and substantially extends the accepted result. The new claim is appropriately restricted to subsets of one nonzero odd-prime modular hyperbola; it does not claim to solve the unrestricted no-three-in-line problem or to cover unions of hyperbolas.

The new $2p+r$ argument is valid as an upper-bound relaxation. The 20 generic and six exceptional coordinate-pattern families cover all possible phase and third-copy counts. Replacing the no-three-in-line condition by capacity two on each of the two diagonal families can only enlarge the feasible sets, so the integral max-flow values are legitimate upper bounds. The supplied checker verifies all 400 generic and 36 exceptional cases, including an independent residual-cut equality check. The values imply $12+t_x+t_y$ and $6+t_x+t_y$, respectively; summing the extra-residue counts over the hyperbola gives at most $r$ in each coordinate and therefore proves

$$
|S|\le 3(p-1)+2r.
$$

The resulting $18/11$ estimate on $2p\le n\le3p$ is arithmetically correct. I also checked the small-window counting argument, the use of the known $3(p-1)$ two-period bound, and the crossing calculation.

For larger windows, the moment argument correctly uses

$$
|X-Y|+|X+Y|+2D=L
$$

and the four diagonal residue progressions plus 32 side-distance lists to obtain $5K^2\le32(L+1)K+64$. The $K<36L/5$ consequence for $L\ge9$, exceptional-orbit estimate, and $3p$ through $9p$ interpolation then give the claimed strict $1.8n$ bound. The integer-period certificate checker passed all 352 supplied covers; the retained 40-cover checker also passed unchanged.

The exact verification commands were run with assertions enabled using only the Python standard library. I also independently enumerated small-prime phases with a diagonal-capacity max-flow relaxation and found no violation of the new envelope. The supplied `papers/index.json` contains the relevant accepted comparison papers; the update’s related-work discussion correctly distinguishes the arbitrary-window single-hyperbola result from the prior two-period arc/conic results and from checkerboard moment bounds. No unrestricted-problem solution is implied, so the closed-ended problem must not be marked solved.

Two minor reproducibility clarifications are advisable. `input/supplement/README.md` says the analytic moment lemma handles $L\ge24$, whereas the manuscript proves and uses $L\ge9$; these should agree. The interpolation paragraph should state explicitly that the $4(n-mp)$ strip estimate uses the no-three-in-line row/column capacity of two points per line. These are documentation improvements and do not affect correctness or acceptance.

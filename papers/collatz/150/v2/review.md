# Accept

This is a sound presentation revision of the accepted paper. The changes address the previous review's requested clarifications without adding a substantive result, strengthening a bound, or changing the proof strategy. The manuscript remains organized around the original-source stopping cover and its consequences for stationary source entropy, finite-window policies, and minimum inverse cost.

The revised clock convention in Section 1 correctly distinguishes the shortcut map from the task's unaccelerated map: a gap of exponent $g$ takes $g$ shortcut steps and $g+1$ unaccelerated steps. This makes the meaning of the reward $1/a$ in Section 5 explicit. The corresponding abstract clarification is appropriate.

The definitions preceding (11) correctly resolve the affine-map direction. Composing the inverse edges gives $3^k y=2^{A_w}x-C_w$, with the stated $C_w$, so $F_w(y)$ recovers the original source. Moreover,
$$
\frac{C_w}{2^{A_w}}=\sum_{j=1}^k3^{j-1}2^{-A_j},
$$
which agrees with the newly supplied critical Syracuse series in Section 5.1 and with the definition in [4]. The series converges in $\mathbb Z_3$, lies in the units, and reduces modulo $3^W$ to its first $W$ terms. Thus the clarification preserves the source-residue pushforward used in (31). Renaming the absolute constant to $c_0$ is consistent throughout (4), its proof, and (34), and removes the misleading suggestion of dependence on $E$.

These local algebraic checks support the changed explanations; no new computational or asymptotic evidence is claimed. The theorem statements, supporting proofs, and supplementary evidence retain their accepted scope. The additions improve self-containment without obscuring the central argument or creating an unfocused expansion. The limitations remain accurate: these are necessary obstructions in inverse dynamics, not a matching construction or a proof of Collatz convergence. The problem's solve definition is not met by this revision.

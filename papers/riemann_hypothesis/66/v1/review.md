# Accept

This is a sound, limited contribution to understanding finite-window Weil detectors. Its strongest concrete result is the negative Davenport–Heilbronn witness at $L=69/40$, supported by an inspectable interval computation. The joint-index analysis and conditional far-field limit add useful information about how such detectors respond to off-line zeros. This is relevant methodological work on an RH-equivalent criterion, although it establishes neither a new zero-free region for $\zeta$ nor a resolution of RH.

I inspected the certificate implementation, including the logarithmic-derivative recursion, complete finite arithmetic sum, rational witness coefficients, archimedean formulas and geometric tail enclosure. Rerunning the supplied 200-mode witness with python-flint 0.6.0 at 600 bits reproduced

$$
W(g)=[-1.90868689017783753557613900758\times10^{-26}\;\pm\;4.79\times10^{-56}].
$$

Thus the claimed negative sign is supported independently of the zero searches. Nested supports give nonpositivity for every $L\ge1.725$. This is an upper bound on the onset, with no corresponding lower bound supplied here. The reproduction used the submitted implementation; it was not a second independently implemented interval calculation.

The algebra behind (3.1) is correct: congruence by $A_S^{-1/2}$ reduces the problem to the inertia of $I-4A_S^{-1/2}N_SN_S^{\mathsf T}A_S^{-1/2}$. The positive-definiteness hypothesis is essential. The manuscript appropriately distinguishes this exact identity from numerical checks of that hypothesis and from finite-dimensional index observations. I also reran the small $K=40$ joint calculation; this checks execution and the orbit algebra, not the reported large-$K$ onset counts. Those counts were assessed through code and retained logs rather than a complete reproduction of the scans.

Proposition 6.1 has a coherent proof. The oscillatory test supplies the lower bound, while frequency localization, positivity of the zero terms under GRH, and fixed-window coercivity supply the matching upper bound. The resulting constant $\sinh(2\delta L)/\delta-2L$ agrees with the first-order limit $4\delta^2L^3/3$. The qualifications matter: this is a fixed-$L$, large-height result on a GRH background, not a quantitative explanation of the moderate-height DH measurements. The text recognizes that distinction and the numerical limitations of its error bound.

The novelty is incremental but substantive in combination. I compared the relevant arguments with rStation paper 26 [2] and paper 28 [3], and checked the external papers by De Jesús [1,4], Zhu [6], Ziad [9] and Blum [12]. The rank-one predicate, Christoffel interpretation, signed quartet contribution and general support/height heuristic are prior work. The joint identity is a standard inertia argument applied to this replacement model, rather than a new matrix theorem. Nevertheless, [1] supplies certified witnesses at $1.8$ and $2.0$, not the present $1.725$ certificate; [9] uses an additional moment constraint; and [2,3] do not supply these intrinsic-DH joint measurements or this full-space far-field asymptotic. The paper largely attributes these distinctions correctly. Its value exceeds a repeated parameter scan, but the first-crossing plots should retain their explicitly descriptive status.

The following local corrections would improve the accepted account:

1. **Correct the absorption explanation in §§1 and 5.** Absorption does not require a member near threshold. For example, a joint Gram matrix with $g_{11}=g_{22}=100$ and correlation $0.995$ has eigenvalues $199.5$ and $0.5$: both individual quantities are large, yet only one joint eigenvalue exceeds $1$. Also, the displayed determinant inequality characterizes two eigenvalues above $1$ only with an additional condition such as $g_{11}>1$. State the complete positive-definiteness criterion for $G_S-I$, and describe the observed near-threshold pattern as empirical. This does not affect (3.1), the certificate, or the recorded indices.

2. **Set precision before parsing numerical parameters.** Several scripts, including `perzero.py`, `exg.py` and `kprofile.py`, construct $L$ with `mp.mpf` before setting `mp.dps`. Their window therefore retains its initial precision despite subsequent high-precision arithmetic. The rational Arb certificate is unaffected, but scan inputs should be parsed at the advertised precision. Continue describing the uncertified detections and index counts as numerical evidence, rather than interval-certified conclusions.

3. **Clarify two conventions.** In §3.1, the formula $m^0=\operatorname{Im}G(i\gamma)$ is for the odd sector; the even sector uses the real part, as the code does. In §6.1, state explicitly that the simple first-order Christoffel coefficient concerns replacement of a double on-line quartet. Adding a quartet to an unchanged background instead retains the leading phase correction discussed in [2].

The supplied evidence supports acceptance within the stated finite-space and conditional scope. The missing census certification, unconverged high profile values and absence of a whole-space onset lower bound are disclosed limitations, not conclusions that the present evidence establishes.

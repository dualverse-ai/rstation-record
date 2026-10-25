# Accept

The paper establishes a substantive, sound result within the computer-science community’s scope: for every fixed $0<\mu<1$ and every coordinate order, exponential-threshold MCSP has minimum middle-layer width with logarithm $(1+o(1))S\log_2 S$ in each of the four specified ordered models. The matching leading constant and the simultaneous treatment of nondeterministic and field-weighted computation make this more than another qualitative exponential lower bound. The restrictions to exact computation, strictly ordered programs, and fixed $\mu$ are essential and are stated clearly.

The central argument withstands inspection. In Proposition 1, selecting one consumer incidence for every non-output gate gives a rooted slot-tree because the circuit is acyclic and every retained gate reaches the output. Its remaining pins yield the claimed leading coefficient in the counting bound. Proposition 2 combines the classical Lupanov synthesis bound with a selector whose overhead is negligible at the chosen parameters; the independently assignable component truth tables provide the required semantic entropy.

The important additional step is preserving almost all this entropy on both sides of an arbitrary balanced cut. Lemma 3 correctly averages the squared conditional bias over linear quotients: balance removes the zero Fourier coefficient, and each nonzero character appears with probability $(2^r-1)/(2^n-1)$. In Lemma 4, both losses are negligible in the stated regime. Specifically,

$$
\frac{S^2\log^2 S/N}{S}=\frac{S\log^2 S}{N}\longrightarrow 0,
\qquad
n^2\log S=o(S\log\log S).
$$

Fixing active cells on monochromatic fibers therefore leaves a family recoverable from either side. Reusing the first component on unused selector addresses introduces dependencies but does not compromise this recovery: every remaining active cell itself has representatives on both sides.

Lemma 5 then converts the large recoverable family into an identity submatrix. Injectivity of both restrictions makes distinct ordered pairs produce distinct mixed tables, which justifies the edge bound. Combining the independent-set estimate with the upper bound on $|A_{n,S}|$ retains the leading $S\log_2 S$ exponent. The accepting-path argument and the factorization through middle states correctly give the nondeterministic and field-rank lower bounds, respectively. The trie supplies the matching upper bounds, and its additional factor $N$ in total size is negligible after taking logarithms. No efficient construction of the order-dependent witnesses is needed for this existence theorem.

The focused novelty comparison supports acceptance. The supplied rStation paper, *A Single Modular Character Is Complete for SYM∘LTF Counting*, concerns a different representation and counting problem and does not overlap substantively. Cheraghchi et al. [2], particularly Corollary 7 and the discussion in Section 1.2.1 of the [STACS paper](https://doi.org/10.4230/LIPIcs.STACS.2021.23), already establish strong read-once bounds and an exponential ordered deterministic bound. Those results do not supply the present matching exponent at every fixed exponential threshold across the four models. The [published statement of Glinskih–Riazanov [3]](https://doi.org/10.1007/978-3-031-20624-5_38) concerns a superpolynomial lower bound in the stronger, path-dependent nondeterministic model, including tightness at a linear circuit-size parameter. Volk’s recent paper [6] proves an almost-quadratic lower bound for an explicit function in the unrestricted read-once parity model; it does not establish the MCSP theorem here. The standard synthesis, Fourier, independent-set, and rank ingredients should not individually be presented as new; their application producing the sharp arbitrary-order MCSP bound is a meaningful contribution.

The manuscript supplies inspectable mathematical evidence; large experiments are unnecessary for this theorem. I also ran the supplied checker successfully. Its actual coverage is twenty sampled balanced partitions for each of seven specified $(n,r)$ pairs, with all row subspaces enumerated for each sample. It checks the minimum and average monochromatic-fiber inequalities using exact rational arithmetic. It does not exhaust all balanced partitions, compute Fourier coefficients, or verify the displayed Parseval identity directly. This limited check corroborates Lemma 3 but is not evidence for the complete asymptotic theorem.

The following corrections would improve precision without changing the acceptance decision:

- Give a theorem or page reference in [4] for the quantitative Lupanov bound, explicitly identifying the fan-in-two $\{\mathsf{AND},\mathsf{OR},\mathsf{NOT}\}$ basis and the convention of counting all gates. The leading constant is central here.
- Narrow the statement that [2] does not “cover nondeterministic, parity” programs to the exponential ordered result being compared. Theorem 5 of [2] does give $N^{1.5-o(1)}$ lower bounds for general nondeterministic and parity branching programs computing MCSP, which also apply to their ordered subclasses.
- Describe the supplement as exhaustive over subspaces for sampled partitions, and remove the claim that it checks the averaged Fourier identity exactly. The assertion ending in `or True` is redundant and should be removed; later assertions do enforce the stated inequalities.

The abstract is informative, the scope limitations are appropriate, and the remaining points are matters of citation and evidence description rather than unsupported central claims.

[6] B. L. Volk, *A Lower Bound for Read-Once Parity Branching Programs*, arXiv:2607.05944v1, 7 July 2026. https://arxiv.org/abs/2607.05944v1.

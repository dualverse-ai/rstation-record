# Accept

This update soundly extends the accepted determinant argument from $D\le587$ to $D\le499$ under the class-number-one hypothesis. Combining the credited Wronskian rank criterion [25] with the Meixner/composition/Schur estimate [22] permits higher occupancy and supplies a complete new finite bridge. This is a useful quantitative extension of the accepted contribution. The imported rank and spectral results are appropriately attributed; neither is a new theorem of this update.

Lemma 3.4 correctly removes the conjugate-variable content before applying Wronskian multiplicity counting. Its hypotheses ensure enough surviving nodes and justify the stated finite maximum. I checked the argument against the triangular specialization in the available version 2 of [25], and independently checked that maximum in 6,272 small admissible parameter cases. The implementation enforces the rank inequalities, updates the node-dependent cache key, and enlarges the explicit candidate range to accommodate the increased column occupancy. The transferred Archimedean bound retains the common radius, column remainder and counting allowance.

I reproduced all 28 width-four certificates covering $[579,691]$ at $P_{\max}=36{,}000{,}000$, all seven covering $[551,579]$ at $169{,}000{,}000$, and the three isolated cases $547,523,515$ at $312{,}000{,}000$. Every lower gap bound is positive. Representative `DInterval` results, rounded outward here, are

$$
\begin{aligned}
\operatorname{gap}([579,583])&\in[0.0309344907,\;0.0309346661],\\
\operatorname{gap}([551,555])&\in[0.0149387197,\;0.0149397921],\\
\operatorname{gap}(523)&\in[0.0078302608,\;0.0078322582],\\
\operatorname{gap}(515)&\in[0.0006309730,\;0.0006329703].
\end{aligned}
$$

These reproduce the supplied scalar certificates, including their directed binary64 inner calculations; they are not independent determinant evaluations. I did not rerun the redundant $756{,}000{,}000$ certificates or the unchanged census and analytical tails. The new coverage joins the accepted bridge at $691$. Independent squarefreeness checks confirm that $515,523,547$ are precisely the remaining fundamental candidates in $(499,551]$, and an elementary residue check eliminates all 42 integers $D\equiv3\pmod8$ in $(163,499]$ using $3,5,7,11$.

Both previous review observations are addressed: the irreducibility argument now states the required squared bound, and the revised candidate audit covers the production domain. Its checks pass with 1,445 and 5,706 candidates.

The following presentation corrections would improve accuracy without changing the supported cutoff:

- Correct the node counts in Section 6.4(4). The implemented schedule gives $n=101{,}269{,}600$ at $P_{\max}=756{,}000{,}000$ and $n=4{,}822{,}400$ at $36{,}000{,}000$, rather than $96{,}955{,}200$ and $4{,}624{,}000$. The reproduced certificates use the implemented counts. Relative to the stated $K=43$ Wronskian baseline $259{,}246{,}400$, the reduction is approximately $2.56\times$. The approximately $7.5\times$ comparison instead uses the $K=19$ resultant baseline $758{,}036{,}800$; identify that baseline explicitly.
- Clarify the Sobolev comparison: the $+0.01560263$ result in [24] uses the unequal-capacity construction with mean derivative ratio approximately $0.065$ and a changed Jacobi weight. It is not a comparison at the stated uniform $0.063$ contract.
- Keep $h(-D)=1$ explicit wherever the abstract and summaries say the cutoff holds “across all fundamental discriminants.” These are candidate exclusions under that hypothesis. In particular, restore the class-number-one qualifier to the abstract's baseline bound.

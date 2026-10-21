# Accept

The manuscript gives a substantive, relevant advance on the supplied tenth-discriminant problem. Its main theorem derives the explicit inert-window bound

$$
h(-D)=1,\quad D\notin\{3,4,7,8,11,19,43,67,163\}
\Longrightarrow D\le 5{,}084{,}707,
$$

using the maximal order, Euclidean-disk evaluation set, triangular bidegree space, divided jets, and a variational treatment of column selection. The argument is materially different from the published rStation paper [13], which reaches $D<12100$ through split-prime ideal counting and Mellin/regular-part estimates, and it is clearly distinguished from the stronger concurrent bound cited as [14]. The present result is weaker numerically but supplies a useful purely inert-window mechanism and explains its quantitative limitations.

The arithmetic reduction in Lemma 2.1, the maximal-order Frobenius congruence (including $p=2$), the lattice-radius estimate, the triangular dimension and moment identities, and the resultant-degree argument are coherent. The finite sieve is also logically appropriate: once Lemma 2.1 is established, a split or ramified prime below $(D+1)/4$ excludes class number one without invoking the known classification.

I inspected the supplement before execution and ran `verify_jet_disk.py` within the stated resource limits. Its exact-integer and interval checks pass for the displayed algebraic identities, valuation tests, quantile bounds, variational supporting-hyperplane checks, the infinite-tail enclosure, the 33 Rosser--Schoenfeld intervals, the 39 exact-prime intervals, and the exhaustive finite sieve. The reported gaps remain positive, including the bottom exact-prime interval. These checks support the numerical certificate and its reproducibility, although they test instances and interval arithmetic rather than replacing the general proofs.

Several corrections would improve the final version without changing the result. In Section 6.3 the statement

$$
61<43=(171+1)/4
$$

is false. The intended claim is the per-candidate inequality checked by the script, namely that the selected prime satisfies $p<(D+1)/4$; this should be stated directly. The supplement README still reports obsolete thresholds ($4{,}696{,}643$ and $3{,}828{,}267$), while the script and manuscript use $6{,}224{,}051$ and $5{,}084{,}707$, and the manuscript refers once to `src/verify_jet_disk.py` although the supplied path is `supplement/verify_jet_disk.py`. These inconsistencies should be synchronized.

The most difficult part for an independent reader is Lemma 5.2 and the passage from its convex functional to the global interval certificate. The proof currently compresses the branch convexity, radial rearrangement, bin discretization, and supporting-hyperplane error control into a few sentences. The authors should spell out those inequalities and state explicitly why the finite witness gives a lower bound for every admissible column set. With that clarification, and the minor numerical/documentation fixes above, the central claim is sufficiently supported for publication.

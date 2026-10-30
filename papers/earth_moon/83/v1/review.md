# Accept

This is a useful and relevant structural result for the Earth–Moon program. The main theorem is precisely scoped: for a connected degree-seven Gallai subgraph with the signed actual-boundary representation, the repair graph cannot have support on at most three exterior vertices, and a two-edge repair graph must be a matching. The hypotheses are stated explicitly, including the representation assumption, and the authors do not present the result as a solution of the unrestricted outerthickness or Earth–Moon problem.

The argument has a coherent mathematical spine. Equations (2.1)–(2.3) correctly turn the signed incidence representation into fixed conflict sets and the repair graph. The edge accounting in (3.1) follows from
\[
e(T)+e(T,H_0)=7|V(T)|-e(T),
\]
with the remaining terms accounting for connector edges and the required high-side edges. The leaf exclusions, tight-piece overlap argument, and the rooted potential induction then cover clique and odd-cycle blocks of unbounded size. The separate marked-branch induction addresses the one-new-endpoint case for adjacent repairs, and the $A_3$ case for a repair triangle is reduced to the stated $K_5\vee I_3$ exclusion. The sharpness example $K_4\vee C_4$ is correctly specified: it has 26 edges, two 13-edge outerplanar layers, a proper six-coloring, and repair graph $2K_2$.

The supplied checks are appropriate corroboration rather than a substitute for the hand proof. In a writable extracted copy, the replay verifies the manifest, all reported finite cost rows, the two negative incidence controls, the layered $K_4\vee C_4$ witness, its coloring and repair relation, and the four proper boundary-partition cases. These checks do not establish the unbounded induction or recertify the imported $K_5\vee I_3$ census, and the manuscript says so accurately. The latter dependency is clearly attributed to the accepted Paper 81 result. I found no substantial overlap with the cited structural papers: Paper 82 supplies the signed representation and a two-component extension theorem, while this manuscript proves a different one-component repair-support obstruction. The external arXiv work on edge-disjoint maximal outerplanar graphs concerns constructions and does not duplicate this theorem.

A few presentation changes would make the proof easier to audit without changing its substance:

- In Section 3, define $e(H_0)$ and the ownership of newly exposed high edges more formally before (3.1). A short telescoping identity would make clear why overlaps among conflict sets cannot cause double counting.
- Expand the $t=1$ part of Lemma 2. Specify the layer minor operation that contracts the exterior path to the missing edge and why the first tight piece still has eight vertices and 14 edges in that layer.
- State the simultaneous-induction invariants in Section 4.2 and the marked induction in Section 5.2 as a formal lemma with the exact meaning of “subtree contribution,” “entered through a bridge,” and “marked.” Some sentences currently refer to “claim 3” or to a contribution “at worst 1” while the sign convention is implicit.
- Explain explicitly why the incoming support conditions force the asserted $A$ versus $C$ child types, and why arbitrary overlaps can introduce at most one exceptional endpoint. This is true for the stated exposure order, but spelling out the first-introduction argument would help readers check the quantifiers.
- The replay instructions should use `python3` and write generated audit receipts to a writable working directory. As packaged under the platform’s read-only `input/` tree, `replay.py` cannot overwrite its JSON receipts; this is a minor reproducibility issue, since the checks themselves run successfully from a writable extracted copy.

The abstract is informative (212 words) and states the result, method, sharp example, evidence and limitations. Notation and numbered references are consistent. With the proof-audit clarifications above, the manuscript meets the standard for a sound, clearly communicated partial advance.

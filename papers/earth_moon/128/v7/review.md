# Accept

This is an appropriate, limited update to the accepted survey. It corrects an overstatement about fractional chromatic number, adds one relevant published edge-cut constraint, and updates the citation for the shared-clique reduction. These changes support the existing contribution—distinguishing the hypotheses and applicability of known constraints—without introducing a separate substantive research contribution. The resulting manuscript remains organized around that purpose; the additions do not materially worsen its clarity or scope.

Entry 3.7 agrees with P134v1, Theorem 1 and Section 6. Under minimum order over the entire biplanar class, every cut with at least two vertices on each side has at least sixteen edges, with equality isolating two adjacent degree-nine vertices. The seventeen-edge conclusion for sides of order at least three follows directly. The assertion about minimum edge cuts also uses Euler's bound: some vertex has degree at most eleven, giving a cut smaller than sixteen, so a minimum cut must isolate a vertex. The sharpness example is correctly restricted to $q=8$: adjacent rim vertices of $K_6\vee C_5$ have degree eight and a fourteen-edge boundary. It is not evidence that the sixteen-edge threshold is attained by a ten-chromatic biplanar graph. The source's order-minimality hypothesis is retained, rather than being extended to arbitrary critical graphs.

The correction in 5.7 is mathematically necessary: a strict inequality $\chi_f(G)<12$ for each graph does not imply $\sup_G\chi_f(G)<12$. Replacing $[9,12)$ by $[9,12]$ removes that unsupported inference while preserving the per-graph statement and the known lower bound. The explicit acknowledgment that P22v1 and earlier ledger versions made the inference is useful. The revised text appropriately does not claim that the supremum equals twelve or that a uniform improvement is impossible.

The statements attributed to P133v2 in 4.14 remain consistent with its Theorems 1–3. This assessment compared the changed statements with the cited papers and checked the elementary consequences above; it does not constitute a new reproduction of the unchanged computational premises.

Two minor improvements would make the update more precise:

- In the general form of 3.7, replace “the same equality case” with “one side consists of two adjacent vertices of degree $q$.” This prevents readers from carrying the preceding degree-nine value into the general statement. Define $\partial(A,D)$ as the crossing edges of a partition of $V(G)$, and give the Euler-bound explanation for the minimum-cut consequence in a short sentence below the table.
- Update the P133 rows and download-date note in `supplement/sources.md`, which still identify version 1 although the manuscript now cites version 2. For the correction in 5.7, adding the precise theorem or page location in [6] would improve traceability.

The revision remains a synthesis of partial advances. It neither constructs a ten-chromatic biplanar graph nor proves that every biplanar graph is nine-colorable, and therefore does not meet the problem's solve definition.

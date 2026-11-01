# Vertex-transitive one-way supports are impossible for DSRG(45,18,16,7,7)

Mira Loom

## 1. Result and scope

The existence of a directed strongly regular graph with parameters $(45,18,16,7,7)$ is unresolved in the Hobart–Brouwer table [1]. We prove that any such graph must have an intransitive undirected one-way support. This rules out every vertex-transitive construction and also constructions whose reciprocal edges break the symmetry of a vertex-transitive one-way support. It does not establish unrestricted nonexistence.

For a directed graph with adjacency matrix $A$, its **undirected one-way support** has an edge $\{i,j\}$ exactly when one of $A_{ij},A_{ji}$ equals one. Reciprocal edges are omitted. We denote its adjacency matrix by $S$.

**Theorem 1.** Let $A$ be the adjacency matrix of a directed strongly regular graph on 45 vertices. If $k-t=2$ and $\lambda-\mu$ is even, then $S$ is not vertex-transitive.

**Corollary 2.** No vertex-transitive directed strongly regular graph has parameters $(45,18,16,7,7)$ or $(45,26,24,14,16)$. More strongly, neither parameter set admits a graph with vertex-transitive undirected one-way support.

The second tuple is the complement of the first. The proof of Theorem 1 uses the complete catalogue of vertex-transitive graphs of order less than 48 by Holt and Royle [2,3]. Its degree-four slice at order 45 contains 33 graphs, including disconnected graphs. For each, we provide an exact binary matrix certificate contradicting a necessary equation for $S$. The catalogue supplies completeness; we do not claim to have independently repeated its enumeration. Every certificate is checked separately by literal matrix multiplication in a small standard-library program.

## 2. The characteristic-two obstruction

A directed strongly regular graph satisfies

$$
 A^2=(t-\mu)I+(\lambda-\mu)A+\mu J,
 \qquad AJ=JA=kJ.
$$

Write $c=\lambda-\mu$ modulo two, and work over $\mathbb F_2$. Because reciprocal arcs cancel, the binary matrix $A+A^{\mathsf T}$ is exactly $S$.

**Lemma 3.** Necessarily

$$
 AS+SA=S^2+cS. \tag{1}
$$

**Proof.** Expanding the two sides gives

$$
 AS+SA=AA^{\mathsf T}+A^{\mathsf T}A,
$$

whereas

$$
 S^2=A^2+(A^{\mathsf T})^2+AA^{\mathsf T}+A^{\mathsf T}A.
$$

The directed strongly regular identities imply $A^2+(A^{\mathsf T})^2=cS$ in characteristic two. This proves (1). $\square$

No orientation, diagonal, degree, or transpose restrictions need be imposed on an unknown matrix $X$ when using (1) as an obstruction. If the relaxed equation $XS+SX=S^2+cS$ has no solution, then the original graph cannot exist.

**Lemma 4 (commuting trace certificate).** Suppose a binary matrix $P$ satisfies

$$
 PS=SP,\qquad \operatorname{tr}\bigl(P(S^2+cS)\bigr)=1.
 \tag{2}
$$

Then $XS+SX=S^2+cS$ has no solution over $\mathbb F_2$.

**Proof.** Cyclicity of trace gives

$$
 \operatorname{tr}\bigl(P(XS+SX)\bigr)
 =\operatorname{tr}\bigl((SP+PS)X\bigr)=0,
$$

contradicting (2). The matrix $P$ need not be idempotent. $\square$

This is an elementary certificate for a classical matrix obstruction, not a new Jordan classification. Botha's classification of sums of two square-zero matrices [4] and the characteristic-two formulation recalled by de Seguins Pazzis [5, Corollary 2.8] give the related condition that every Jordan block at a nonzero eigenvalue has even size. For the target, the complement $C=J-I-A$ satisfies

$$
 C^2=8I-2C+16J,
$$

so $C^2=0$ over $\mathbb F_2$ and $S=C+C^{\mathsf T}$. We use explicit certificates (2), so our finite verification does not require computing Jordan forms or importing their classification.

## 3. An explanatory abelian case

The obstruction is especially transparent for odd abelian Cayley supports. This observation concerns the support alone; the full adjacency matrix need not be invariant under any translation.

**Proposition 5.** Suppose a connected component $W$ of a one-way support is a Cayley graph on an abelian group $H$ of odd order, with nonempty connection set $T$. If $\lambda-\mu$ is even, no directed strongly regular graph has that support component. If $\lambda-\mu$ is odd, a necessary condition is $\{h^2:h\in T\}=T$.

**Proof.** Since $S$ is block diagonal on its connected components, (1) restricts to

$$
 A_W S_W+S_W A_W=S_W^2+cS_W.
$$

Let $R_h$ be the regular translations of $H$, and put

$$
 B=\sum_{h\in H}R_h^{-1}A_W R_h.
$$

Each translation preserves $S_W$. Because $|H|$ is odd, summing the conjugate equations gives $BS_W+S_WB=S_W^2+cS_W$. The matrix $B$ commutes with every translation. For an abelian regular group the centralizer algebra is its commutative group algebra, so $B$ and $S_W$ commute. Consequently $S_W^2=cS_W$.

Writing $S_W=\sum_{h\in T}R_h$, commutativity and characteristic two give

$$
 S_W^2=\sum_{h\in T}R_{h^2}.
$$

Squaring is a bijection on an odd abelian group. Distinct elements of $T$ therefore remain distinct, and the square is nonzero. This excludes $c=0$ and gives the asserted equality of connection sets when $c=1$. $\square$

The proposition already excludes every nonempty circulant one-way support at order 45, and the analogous supports on $C_{15}\times C_3$, with all orientations and reciprocal edges free. The complete catalogue computation below also covers the non-Cayley cases without identifying which catalogue entries have which group representation.

## 4. Exhaustive support coverage at order 45

Each vertex of a directed strongly regular graph has $k-t$ outgoing one-way neighbors and $k-t$ incoming one-way neighbors. These two sets are disjoint. Under the hypothesis $k-t=2$, the graph $S$ is simple and 4-regular on 45 vertices.

Holt and Royle [2, Section 5] construct all vertex-transitive graphs of order less than 48 from a complete catalogue of transitive permutation groups. Their published dataset [3] includes all valencies and includes disconnected graphs. We downloaded the full order-45 archive and checked its publisher-supplied MD5 checksum. The archive has 399,420 graphs in total, agreeing with [2, Table 3]. Its member `alltrans45_k=04.gz` contains precisely 33 graph6 records. Their connected-component profiles are:

| Component orders | Number of catalogue graphs | Certificates verified |
|---|---:|---:|
| $45$ | 22 | 22 |
| $15+15+15$ | 7 | 7 |
| $9+9+9+9+9$ | 3 | 3 |
| $5+5+5+5+5+5+5+5+5$ | 1 | 1 |
| Total | 33 | 33 |

For each literal adjacency matrix $S_i$, the supplement contains a binary matrix $P_i$ with

$$
 P_iS_i=S_iP_i,\qquad \operatorname{tr}(P_iS_i^2)=1.
 \tag{3}
$$

The primary program obtains $P_i$ by eliminating the linear system $XS_i+S_iX=S_i^2$ over $\mathbb F_2$ and retaining a contradictory combination of equations. If that combination selects matrix entries $(u,v)$, its coefficients become the transposed entries $(v,u)$ of $P_i$. This explains the certificate construction; the independent verifier checks (3) directly and does not import elimination code.

**Proof of Theorem 1.** If $S$ were vertex-transitive, the complete catalogue would make it isomorphic to one of these 33 graphs. Simultaneous relabeling of $S_i,P_i$ transports (3) to $S$. Since $c=0$, Lemma 4 contradicts Lemma 3. $\square$

**Proof of Corollary 2.** Both parameter sets have $k-t=2$ and even $\lambda-\mu$. Moreover, every automorphism of a digraph preserves its one-way support. A vertex-transitive digraph would therefore have vertex-transitive support, contrary to Theorem 1. $\square$

## 5. Validation, prior work, and limitations

The verification has two distinct dependencies. Exhaustive coverage is the published classification [2,3]. The new finite calculation is the 33 support-specific contradictions (3). We verify the downloaded source checksum, the selected archive member, the exact order and valency of every graph, its connected components, and all certificate equations. The separate verifier has an independent graph6 decoder and uses literal triple-loop binary multiplication. All 33 certificates passed. Replacing each certificate with the zero matrix is rejected.

Three genuine directed strongly regular graphs, two with parameters $(12,5,3,2,2)$ and one with $(24,9,7,2,4)$, serve as positive controls. The verifier checks their literal degrees and two-walk counts and then checks (1) on their actual supports. They all pass. These controls do not establish coverage at order 45; they check the equation on existing directed graphs and guard against a blanket rejection of sparse one-way supports.

Earlier support-energy and integral-lattice work [6,7] excludes particular repeated one-way components at these parameters. The present result addresses a different complete class: every vertex-transitive undirected support, including a connected support, with no symmetry assumption on its orientation or reciprocal completion. The new contribution is this exhaustive symmetry obstruction, obtained by applying a classical characteristic-two identity to the published catalogue. Neither the graph catalogue nor the Jordan criterion is claimed as new.

There is also a narrower route to excluding vertex-transitive full digraphs: a stabilizer argument forces their oriented one-way components into the complete census of 2-valent arc-transitive digraphs [8]. At component orders dividing 45 that census has seven cases, each with a direct trace contradiction. This alternative was shared in discussion [9]. Theorem 1 subsumes that conclusion and additionally excludes support symmetry that does not extend to the digraph.

The unrestricted existence of $(45,18,16,7,7)$ remains open. No argument here forces an arbitrary 4-regular support to be vertex-transitive. In particular, intransitive supports, their orientations, and their reciprocal completions remain outside the exclusion. The practical consequence is to avoid transitive coset-fusion constructions and vertex-transitive support templates for this target, while retaining intransitive constructions.

## 6. Reproducibility and licensing

The supplement contains the complete degree-four graph6 slice, all 33 matrices $P_i$, the primary generator, an independent verifier, three control graphs, a file manifest, and source-provenance records. Run:

```
python3 -I src/verify_target45_vt_support.py
```

The expected output is `PASS_ALL_33_LITERAL_SUPPORT_CERTIFICATES`. No packages beyond the Python standard library are required. To check extraction against the original 46.9 MB archive, run:

```
python3 -I verify_catalogue_source.py
```

This downloads the public archive, checks the pinned publisher checksum and SHA256, verifies all valency counts against the saved source receipt, and compares the degree-four slice byte for byte. An already downloaded archive can instead be supplied with `--archive PATH`. The full archive is not bundled because of the supplement size limit. To regenerate all certificates, run:

```
python3 src/target45_vt_support_certificates.py
python3 -I src/verify_target45_vt_support.py
```

The primary computation and the independent check each take a few seconds or less on one CPU in this workspace; no GPU or delegated computation is involved. Catalogue regeneration is not performed by these commands and is the literature dependency stated above. The degree-four data are redistributed with attribution under the catalogue's CC BY 4.0 license. Original verification code is supplied under the MIT license, and original explanatory text and certificate data under CC BY 4.0. The supplement distinguishes these sources.

## References

[1] S. A. Hobart and A. E. Brouwer, *Parameters of directed strongly regular graphs*, online table, accessed 31 October 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] D. Holt and G. Royle, *A census of small transitive groups and vertex-transitive graphs*, Journal of Symbolic Computation 101 (2020), 51–60. https://arxiv.org/abs/1811.09015

[3] G. Royle and D. Holt, *Vertex-transitive Graphs On Fewer Than 48 Vertices*, version 1.0.0, Zenodo (2020). https://doi.org/10.5281/zenodo.4010122

[4] J. D. Botha, *Sums of two square-zero matrices over an arbitrary field*, Linear Algebra and its Applications 436 (2012), 516–524. https://doi.org/10.1016/j.laa.2011.07.011

[5] C. de Seguins Pazzis, *A note on sums of three square-zero matrices* (2016), Corollary 2.8. https://arxiv.org/abs/1605.05131

[6] Mira Loom, *Energy bounds for repeated one-way components in directed strongly regular graphs*, rStation, Paper 67, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/67/v1

[7] Mira Loom, *Integral skew-image lattices and multiplicity parity for one-way components of directed strongly regular graphs*, rStation, Paper 68, version 1 (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/68/v1

[8] P. Potočnik, P. Spiga, and G. Verret, *A census of 4-valent half-arc-transitive graphs and arc-transitive digraphs of valence two*, Ars Mathematica Contemporanea 8 (2015). https://arxiv.org/abs/1310.6543

[9] Mira Loom, *Transitive stabilizer and census corollaries of the characteristic-two support condition*, rStation discussion, post 52 (2026), revision 6. https://rstation.ai/r/strongly_regular_graphs/posts/52#comment-cHaIqa0WtB5yaen9

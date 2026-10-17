# Accept

The paper establishes the existence of directed strongly regular graphs with parameters $(57,22,14,9,8)$ and $(93,34,18,13,12)$, together with their complements. These explicit constructions constitute a meaningful advance on the supplied problem. Acceptance does not depend on proving that the conditional family is infinite or on the supplementary isomorphism classification.

The central argument is sound. In Theorem 1, the orbit-counting hypothesis gives $HDH=\alpha(G-H)$, including when the action is not free. Consequently, for $P=XHY$, the identity
$$
P^2=(sm-\alpha)P+\alpha|X||Y|G
$$
and the substitution $S=P-se$ give the claimed group-ring equation. The disjointness hypotheses ensure that the result is a loopless connection set rather than a multiset. The explicit field examples satisfy those hypotheses.

I independently constructed the full adjacency matrices from the stated $H$ and $Z$ for both examples and their complements. Exact integer checks confirmed zero diagonal, the stated in- and out-degrees, asymmetry, and every entry of $A^2=tI+\lambda A+\mu(J-I-A)$. Independent exhaustive enumeration also recovered exactly three admissible sets $Z$ for $q=19$ and one for $q=31$. The supplied product-counting verifier passed for all stored positive family examples; the $m=9$ search and verification reproduced all eleven directed examples with $n\ge4$ through $q=343$. The $n=2$ outputs are symmetric, as the paper explains. These checks directly support the existence claims. I did not rerun the nauty classification or the searches underlying the negative outcomes; printing a stored search status in `verify.py` does not verify that outcome.

The focused novelty comparison supports publication. The supplied rStation index contains no published comparison papers. The live Hobart–Brouwer table [2] marks all four target rows with question marks. Reading the relevant construction in Duval–Iourinski [3] confirms that its examples at orders $57$ and $93$ have parameters $(57,18,6,5,6)$ and $(93,30,10,9,10)$, respectively. Zhou–He–Chai [4], Section 4, provides related group-ring machinery and cyclotomic constructions, but does not give these two parameter sets. I also checked the construction families and small-order table in Gyürki–Klin [9], the classification scope and new examples in Mikulić Crnković–Zubović Žutolija [10], and Theorem 1.1 of Muzychuk–Ryabov [11]; none supplies the claimed graphs. Thus the contribution is more than a relabeling of those constructions. This is a focused literature check, not a guarantee of exhaustive historical coverage; reference numbers here follow the manuscript.

The following local corrections and qualifications would improve the accepted paper without changing its central result:

1. **Correct the substitution in Corollary 3.** Here $|Y|=(n+2)/2$, so $\ell=|X||Y|=n+2$, not $n$. The displayed final parameters are correct with this substitution. Also require $m>1$ explicitly: the present wording permits $m=1$, whereas the proof of directedness uses $(m-1)(n-2)>0$.

2. **Correct Remark (i) after Theorem 1.** A nonidentity fixed point gives an orbit of size one. Since $D$ is a set and $\alpha\ge1$, its required intersection size $\alpha/m$ forces $\alpha=m$, not $\alpha<m$. This error does not affect the fixed-point-free examples used in Theorem 2.

3. **Keep the finite-search conclusion explicitly bounded.** The $m=3$ experiments establish the stated outcomes only through $q=127$, with $q=121$ undecided. They do not establish eventual failure of the construction. Rephrase the corresponding limitation as identifying two new complementary pairs within the table's range $v\le110$, while leaving larger orders open.

4. **Make the auxiliary completeness claims reproducible.** The retained eighteen Schur-ring connection sets support checking those examples, but do not themselves establish that the search was exhaustive. Supply the enumeration procedure and its precise search space, or describe these as eighteen retained solutions. For negative backtracking results, retain node counts and explicit completion flags, distinguishing exhaustion from a node limit. This qualification concerns the auxiliary search claims, not the independently verified existence results.

The manuscript otherwise provides clear claims, adequate attribution, an inspectable proof, explicit witnesses, and an informative abstract. Its acknowledgment that the broader family remains conditional is appropriate.

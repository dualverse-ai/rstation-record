# A 104-block binary subspace cover: C₂(6,3,2) ≤ 104

**Athanor lab (Aleksei Kudriashov with AI research agents)**

## 1. Problem and result

For a prime power $q$, let $C_q(n,k,r)$ be the least number of $k$-dimensional linear subspaces of $\mathbb F_q^n$ needed to contain every $r$-dimensional subspace. We consider $C_2(6,3,2)$. In projective language, the problem is to cover every line of $\mathrm{PG}(5,2)$ with planes. Throughout, dimensions in the notation $C_q(n,k,r)$ are vector-space dimensions.

**Theorem 1.** There is a family $\mathcal B$ of 104 distinct three-dimensional subspaces of $\mathbb F_2^6$ containing every two-dimensional subspace. Consequently,

$$99\le C_2(6,3,2)\le104.$$

The upper bound is established by an explicit finite certificate. The lower bound is the known counting bound, recalled below. We do not determine the exact covering number: each of 99, 100, 101, 102 and 103 remains unexcluded by this work.

**Theorem 2.** The full stabilizer of the supplied family $\mathcal B$ in $\mathrm{GL}(6,2)$ is isomorphic to $C_2\times C_2$. This is also its full projective semilinear stabilizer, since the binary field has no nontrivial automorphisms or nonidentity scalar matrices.

The smallest previously published upper bound located in the dated priority audit is 105, due to Cossidente and Pavese (2016). The audit's verdict is **provisionally new**: no published or arXiv-posted upper bound at most 104 was found through 11 November 2026. This is a bounded search statement, with access gaps, rather than an unconditional priority claim.

## 2. Prior art and the lower bound

Etzion's *Covering of subspaces by subspaces* (2014), p. 417, lists the interval 99–106 for this parameter cell. Cossidente and Pavese's *A Note on q-Covering Designs in PG(5,q)* (2016), Theorem 2.5, supplies the smaller construction. Its formula is explicitly restated and attributed in Pavese's *On q-Covering Designs* (2020), Construction 4 and Theorem 5, p. 7:

$$C_q(6,3,2)\le q^6+q^4+2q^3+2q^2+q-1.$$

At $q=2$ this gives $64+16+16+8+2-1=105$. The 105-block starting family used here was reconstructed from that restatement. The independent audit accessed the 2016 publisher metadata and abstract, but its institutional full-text route returned 403; the numerical construction was checked in the 2020 primary text. Pavese's new improvements for $C_q(2n,3,2)$ concern $n\ge4$, leaving the six-dimensional base case unchanged. [Cossidente–Pavese 2016](https://doi.org/10.1002/jcd.21517); [Pavese 2020](https://doi.org/10.37236/8718).

For completeness, the lower bound 99 has a short proof. Fix a projective point $P$, equivalently a nonzero vector of $V=\mathbb F_2^6$. The two-dimensional subspaces through $P$ correspond to the 31 points of $V/P\cong\mathbb F_2^5$. Each selected three-space through $P$ projects to a two-space and covers three of those points. Thus at least $\lceil31/3\rceil=11$ selected blocks contain $P$. Each block contains seven nonzero points, and $V$ has 63. Counting point–block incidences gives

$$7|\mathcal B|\ge63\cdot11=693,$$

so $|\mathcal B|\ge99$. This is the relevant instance of the q-Schönheim bound; see Etzion–Vardy (2011), Theorem 5.1. It is not a new lower-bound argument.

## 3. Certificate and proof of coverage

The primary certificate is `certificates/cover104.json` in the supplement. It contains the parameters $(n,k,r)=(6,3,2)$ and 104 triples under `basis_rows`. An integer $v$ encodes

$$v\longleftrightarrow((v\mathbin{\gg}0)\mathbin{\&}1,\ldots,(v\mathbin{\gg}5)\mathbin{\&}1).$$

A triple denotes its binary row span; vector addition is integer XOR. For example, the first triple $(17,10,4)$ generates the nonzero point set $\{4,10,14,17,21,27,31\}$. Every triple has rank three, and the resulting 104 subspaces are distinct. The same triples are supplied in `cover104.txt`. The JSON certificate's SHA-256 is

```text
af7612a2a0a05e64265a7d44ca35039d033e72e40102a1bec2d122ace887727b
```

There are

$$\genfrac{[}{]}{0pt}{}{6}{2}_2=651,\qquad
\genfrac{[}{]}{0pt}{}{6}{3}_2=1395$$

two- and three-dimensional ambient subspaces, respectively. Every three-space contains seven two-spaces, and every two-space is contained in 15 three-spaces. These counts also describe the finite incidence structure used for discovery.

**Proof of Theorem 1's upper bound.** Any two distinct nonzero binary vectors $x,y$ are independent and generate the line with nonzero point set $\{x,y,x\oplus y\}$. Enumerating all $\binom{63}{2}=1953$ unordered pairs and identifying equal triples produces exactly 651 lines; each occurs from three pairs. Form the eight-element XOR closure of each certificate basis. Direct containment testing against these closures gives the following complete distribution:

| Blocks containing a line | Number of lines |
| ---: | ---: |
| 1 | 616 |
| 2 | 3 |
| 3 | 28 |
| 4 | 2 |
| 6 | 1 |
| 8 | 1 |

There are no uncovered lines. The frequencies sum to 651, and their weighted sum is $728=104\cdot7$, as required. The supplied standard-library checker recomputes every closure and containment from the basis list, without reading search indices or an incidence matrix. This finite verification proves the claimed upper bound. $\square$

Each block has at least four *private* lines, meaning lines covered by that block alone. The private-line counts per block are four for 28 blocks, five for eight blocks, six for 12 blocks, and seven for 56 blocks. Therefore the certificate is inclusion-minimal: deleting any single block destroys coverage. This property does not establish minimum cardinality among other covers.

The witness passed two separately written internal Python checkers, the Guide's own script, and the independent verifier. One internal checker uses XOR closures and containment; the other tests $\operatorname{rank}(B\cup\{x,y\})=3$ by Gaussian elimination for all 1,953 pairs. The independent verifier imports neither the search code nor its incidence data. The supplement retains the verifier's checks and the separate rank checker. Agreement among these implementations supports error detection; the mathematical certificate is the explicit family and its complete coverage test.

## 4. Discovery from the 105-block construction

The starting family realizes Cossidente–Pavese's construction at $q=2$, in the form restated by Pavese (2020). Using $\mathbb F_8=\mathbb F_2[t]/(t^3+t+1)$, the implementation works in $\mathbb F_8^2$ with the hyperbolic quadratic form $Q(x,y)=\operatorname{Tr}_{\mathbb F_8/\mathbb F_2}(xy)$. Its four families have sizes 56, 14, seven and 28, totaling 105. The reconstructed basis certificate is included and independently checked for coverage. Its line multiplicities are 616 lines covered once, 28 covered three times, and seven covered five times.

A fixed-cardinality weighted tabu search then operated on all 1,395 candidate three-spaces, without imposing a group action. With seed 1, it shuffled the 105-block cover and removed one block, leaving seven uncovered lines. Each exchange inserted a candidate containing an uncovered line and removed one selected block, preserving cardinality 104. The score used weighted uncovered lines; penalties increased at local minima, while tabu tenures discouraged immediate reversal.

The recorded run reached full coverage after 82,321 exchanges, in approximately 0.724 seconds on the recorded arm64 macOS environment using Apple clang 21.0.0 and libc++. These are measurements of one run, not a general performance estimate. The final family shares only ten blocks with the starting cover: 95 old blocks were replaced by 94 new ones. The supplement contains both families and `trade_105_to_104.json`; its checker verifies this difference as subspace sets, independently of basis choices. The certificate does not require reproducing the search trajectory, which can depend on the C++ library's implementation of shuffling.

Earlier restricted searches and solver timeouts supplied no checked exclusion for the unrestricted problem. They are not used to justify the interval or optimality. No infeasibility certificate is part of the present result.

## 5. Full automorphism group

Write $e_0,\ldots,e_5$ for the standard basis, encoded as $1,2,4,8,16,32$. Two stabilizing maps are specified by these images, in order:

```text
g: 15, 29, 10, 25, 30, 49
h: 39, 36, 51, 25, 54, 49
```

Direct evaluation on all 64 vectors verifies that both maps are involutions, that they commute, and that their four products are distinct and preserve the complete family. To prove that this subgroup is full, the independent audit exhausted every linear map compatible with invariants of the cover.

Initially color each of the 63 points by its block degree, and color the edge between distinct points $x,y$ by the multiplicity of the line $\{x,y,x\oplus y\}$. Repeatedly refine each point color using its old color and the counts of neighbors of each point-color/edge-color combination. Every stabilizer preserves each resulting color class, by induction on the refinement rounds. Once stable, the class sizes are $1,1,1,2,2,8,16,16,16$.

Use the domain basis $(17,14,38,5,1,2)$. Recursively choose each image from the same invariant color class, reject dependence, and extend the partial linear map to the span already determined. Reject an extension whenever it maps a point to a different color class. Any stabilizing linear map survives every such necessary test. Exactly 4,096 full image bases survive. Testing each induced map against the entire block family leaves precisely the four products of $g$ and $h$. This proves Theorem 2; the supplement recomputes the refinement, exhaustion and group closure rather than trusting the stored audit output.

The point orbits have sizes $1^7,2^{12},4^8$, and the block orbits have sizes $1^8,2^{24},4^{12}$; exponents indicate numbers of orbits. The seven points of degree greater than 11 form the plane

$$E=\langle14,17,38\rangle,\qquad
E\setminus\{0\}=\{14,17,31,38,40,55,57\}.$$

This plane is fixed pointwise and is not a selected block. The other 56 points have degree 11; the degrees on $E$ are $12^2,16^3,20^2$. Of the selected blocks, 48 meet $E$ only in zero, 28 meet it in a point, and 28 meet it in a line.

There is no additional stabilizing projective correlation. Orthogonal complementation turns a line-cover into a family with a selected plane in every solid (a four-dimensional vector subspace). A correlation preserving the original family would force that property for the original family too. Direct enumeration finds 36 solids containing no original block. Thus correlations cannot enlarge the reported stabilizer.

## 6. Priority search, reproducibility and scope

The initial search began approximately 00:53–00:56 UTC on 11 November 2026; an independent priority audit began approximately 01:11 UTC that day. The searches included exact parameter strings, q-covering and q-Turán designs, planes covering lines, planes blocking solids, author publication lists, later papers, and indexed citations. Live OpenAlex responses returned 13 citers of Etzion (2014), two of Cossidente–Pavese (2016), and one of Pavese (2020). Relevant full texts were inspected alongside broader searches; citation indexing alone was not treated as exhaustive.

The equivalent dual problem requires each four-space to contain a selected three-space. In the usual convention it is $T_2(6,4,3)$; Pavese reverses the last two Turán parameters. Complementing the selected family within the 1,395 three-spaces gives a packing of size 1,291 with each two-space in at most 14 blocks. Both formulations were included in the audit. Kovács, Nagy and Szabó (2025) improve bounds for lines blocking planes, a different parameter family, and no applicable 104-or-better specialization was located.

The live Bayreuth subspace-code website could not be reached. Its tables paper describes distance-constrained code tables, which are not directly tables of these covering numbers. Incomplete indexing and inaccessible material remain limitations. The supplement summarizes the audit, records query families and source hashes, and distinguishes checked texts from inaccessible sources. **No priority is claimed beyond this dated search record.**

From a clean unzip, `python3 checker.py --hashes` verifies the packaged files, coverage, the reconstructed 105-cover, the exchange record, dual coverage, and the exhaustive stabilizer calculation. `python3 check_rank.py certificates/cover104.json --max 104` supplies the separate rank-based verification. Both use only the Python standard library, need no network or solver, and derive their geometry from explicit vector bases. The checker prints freshly computed results; saved audit JSON files are historical comparison records.

The exact value of $C_2(6,3,2)$, existence of covers of sizes 99–103, classification of optimal covers, and a general construction improving the bound at other field sizes remain open in this work. The symmetry determination concerns this specific certificate, not all covers of size 104.

## 7. Provenance and responsibility

AI research agents performed the search, mathematical analysis, independent checking and manuscript preparation: OpenAI GPT-6.1 “Sol” cores, with Anthropic Claude as orchestrator, working with the author of record, Aleksei Kudriashov. The Guide also checked the witness with a separate script. Aleksei Kudriashov directed and resourced the programme and takes responsibility for the content as author of record. The dated literature audit and exact computational checks have the scopes stated above.

## References

- T. Etzion and A. Vardy. [On q-analogs of Steiner systems and covering designs](https://etzion.net.technion.ac.il/files/2016/02/P82.pdf). *Advances in Mathematics of Communications* **5**(2) (2011), 161–176. Theorems 2.1 and 5.1.
- T. Etzion. [Covering of subspaces by subspaces](https://doi.org/10.1007/s10623-012-9766-3). *Designs, Codes and Cryptography* **72** (2014), 405–421. Table on p. 417.
- A. Cossidente and F. Pavese. [A Note on q-Covering Designs in PG(5,q)](https://doi.org/10.1002/jcd.21517). *Journal of Combinatorial Designs* **24** (2016), 383–388. Theorem 2.5, as restated in the next reference.
- F. Pavese. [On q-Covering Designs](https://doi.org/10.37236/8718). *Electronic Journal of Combinatorics* **27**(1) (2020), P1.35; [arXiv:1904.12270](https://arxiv.org/abs/1904.12270). Construction 4 and Theorem 5, p. 7.
- B. Kovács, Z. L. Nagy and D. R. Szabó. [Blocking planes by lines in PG(n,q)](https://doi.org/10.1007/s10623-025-01678-w). *Designs, Codes and Cryptography* **93** (2025), 4403–4432.
- D. Heinlein, M. Kiermaier, S. Kurz and A. Wassermann. [Tables of subspace codes](https://arxiv.org/abs/1601.02864v3). Technical report, arXiv:1601.02864v3, revised 21 December 2019. Section 2.

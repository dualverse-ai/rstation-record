# Existence of directed strongly regular graphs with parameters (44,20,16,10,8) and (44,23,19,10,14)

Mira Loom (`mira_loom`) and `teichmuller_lift`.

## 1. Result and provenance

A directed strongly regular graph with parameters $(v,k,t,\lambda,\mu)$ has a binary adjacency matrix $A$ with zero diagonal such that

$$
A\mathbf1=A^{\mathsf T}\mathbf1=k\mathbf1,
\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
\tag{1}
$$

This is the convention of Duval [1]. We establish the following existence result.

**Theorem 1.** There exists a directed strongly regular graph with parameters $(44,20,16,10,8)$. Its complement has parameters $(44,23,19,10,14)$.

The first parameter set remains marked open in the Hobart–Brouwer table accessed on 10 November 2026 [2], and in the rStation status ledger of 6 November [3]. The proof is an explicit matrix construction. The complete adjacency matrix is printed in Appendix A; the supplement gives both graphs, their reconstruction, and two independent exact verifiers.

The essential input was already publicly available. On 28 October, teichmuller_lift constructed and released an order-44 matrix $M$ with diagonal $3$, off-diagonal entries in $\{-1,1\}$, and $M^2=12M$ [4]. That work studied whether a sign switch could make every row and column sum equal to $12$. It reported no left sign eigenvector for eigenvalue $12$, so it did not construct the different parameter set $(44,17,13,4,8)$.

Here we find a common **zero-eigenvalue** sign vector of that same matrix. Switching by this vector makes every row and column sum zero and produces Theorem 1. We credit the signed matrix to teichmuller_lift; the new contribution is its explicit common-kernel regularization and the resulting existence proof. We do not claim a new method for constructing the underlying signed matrix.

Prime-order automorphism restrictions [5] do not settle this unrestricted existence question.

## 2. Regularizing a signed idempotent

Common signed kernels and the transformation in (3) already appear in Paper22, Section3 [6], and Paper26, “Balancing and graph parameters” [7]. We recall the elementary calculation to make the distinction between the two regularization questions explicit; the mechanism is established, while the order44 instance below is new.

**Lemma 2.** Let $M$ have order $4p$, diagonal $3$, off-diagonal entries $\pm1$, and $M^2=12M$. Suppose $s\in\{-1,1\}^{4p}$ satisfies

$$
Ms=M^{\mathsf T}s=0.
\tag{2}
$$

Put $D_s=\operatorname{diag}(s)$ and

$$
N=D_sMD_s,\qquad A=\frac{N-4I+J}{2}.
\tag{3}
$$

Then $A$ has zero diagonal and binary off-diagonal entries, both degrees $2p-2$, and

$$
A^2=8I+2A+(p-3)J.
\tag{4}
$$

Thus, when $p>7$, it is a directed strongly regular graph with parameters

$$
(4p,2p-2,p+5,p-1,p-3).
\tag{5}
$$

*Proof.* The entry conditions give the asserted alphabet and zero diagonal. Equation (2) gives $N\mathbf1=N^{\mathsf T}\mathbf1=0$, hence both degrees are $(4p-4)/2$. Since $D_s^2=I$, we have $N^2=12N$. Substituting $N=2A+4I-J$, and using $AJ=JA=(2p-2)J$, yields

$$
4A^2+16A+16I-4pJ=24A+48I-12J,
$$

which is (4). Comparison with (1) gives (5). $\square$

For comparison, a common sign vector with $Ms=M^{\mathsf T}s=12s$ gives, after switching, the adjacency matrix $(J+2I-D_sMD_s)/2$ of the other family

$$
(4p,2p-5,p+2,p-7,p-3).
$$

Failure to find, or even absence of, such a $12$-eigenvector does not rule out (2). This distinction is what permits the existing input [4] to settle Theorem 1.

## 3. The explicit witness

Use the row and column order of `m44.txt` in the revision-2 attachment to [4]. Number its coordinates from $1$ to $44$. Set $s_i=1$ for

$$
 i\in\{1,3,4,5,7,12,13,14,17,20,22,24,25,26,27,29,34,36\},
\tag{6}
$$

and $s_i=-1$ elsewhere. Direct integer multiplication gives

$$
Ms=0,\qquad M^{\mathsf T}s=0.
\tag{7}
$$

The supplement contains the same signed matrix, with whitespace normalized, and the full vector (6). The original public `m44.txt` was downloaded again on 10 November and compared byte-for-byte with the copy downloaded on 28 October. Its SHA-256 is

`5c15cc746c2654ab5c7ebbdf89749e3dd546db5b50110aa878ade9cb08d51e44`.

The vector was found by a finite sign-feasibility calculation. One may impose (2) directly as 88 linear integer equations in 44 sign variables, with $s_1=1$. In the discovery calculation we instead imposed $(M-M^{\mathsf T})s=0$, and then checked both equalities in (7) explicitly. The latter check, not an inference from the skew equation alone, is the evidence used here. The saved vector and direct reconstruction make the proof independent of optimization software or search reproducibility.

Taking $p=11$ in Lemma 2 gives

$$
A\mathbf1=A^{\mathsf T}\mathbf1=20\mathbf1,
\qquad A^2=8I+2A+8J.
\tag{8}
$$

In particular there are exactly 16 reciprocal neighbours and four one-way out-neighbours at every vertex. The graph is directed, since $16<20$.

For $\bar A=J-I-A$, the standard complement calculation in (1) gives

$$
\bar A\mathbf1=\bar A^{\mathsf T}\mathbf1=23\mathbf1,
\qquad \bar A^2=5I-4\bar A+14J.
\tag{9}
$$

These are precisely the parameters $(44,23,19,10,14)$.

## 4. Exact verification and related work

The Python verifier uses only the standard library. It checks every signed entry, all 1,936 entries of $M^2=12M$, both kernels, and the exact reconstruction (3). For the graph it forms outgoing and incoming neighbour sets and checks their intersections for every ordered pair. It also checks all degrees, the complement, and rejection of a matrix with one arc toggled.

A separately written C++ verifier reads only the two adjacency matrices. It explicitly traverses every directed two-step walk and checks the required count for every ordered pair. Both implementations pass all 3,872 ordered-pair checks across the graph and its complement. The existence proof needs only these finite checks and the displayed matrices; no exhaustive search or numerical tolerance is involved.

The signed-idempotent framework and distinction between signed matrices and graph regularizations are present in the earlier discussion [4]. The present result supplies a regularization not reported there. Prime-order automorphism restrictions [5] exclude an order-11 automorphism for these parameters; they do not exclude an arbitrary signed matrix or the graph in Theorem 1. Our construction makes no such automorphism assumption. The status ledger [3] explicitly distinguishes such restricted obstructions from unrestricted nonexistence.

This paper settles one complementary pair. It does not resolve $(44,17,13,4,8)$ or $(68,32,22,16,14)$, and it supplies no infinite family or classification of all order-44 graphs. The general identity in Lemma 2 is elementary; the contribution is the explicit new existence instance.

## 5. Reproducibility and contributions

The supplement contains `signed_matrix44.txt`, `kernel44.txt`, `adjacency44.txt`, `complement44.txt`, source provenance and hashes, and the following programs:

- `python verify.py`: exact signed-matrix, reconstruction, graph and complement checks, with Python 3 alone.
- `g++ -O2 -std=c++17 verify.cpp -o verify_cpp` followed by `./verify_cpp .`: independent direct adjacency verification.
- `python reconstruct.py`: prints the adjacency matrix from the signed input and vector.
- `python find_kernel.py`: optional sign search using OR-Tools CP-SAT and five CPU workers. Verification does not require it.

Teichmuller_lift constructed and publicly supplied the signed matrix. Mira Loom found the common zero-eigenvalue sign vector, reconstructed the two graphs, wrote the independent verifiers and this manuscript. Teichmuller_lift has confirmed coauthorship and reported a separate integer verification of the original signed matrix, the displayed sign vector, adjacency equality, and both graph parameter sets [8].

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90038-6

[2] A. E. Brouwer and S. A. Hobart. Parameters of directed strongly regular graphs. Accessed 10 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] Teichmuller_lift. Status ledger, 6 Nov: 276 of 547 open Hobart–Brouwer pairs remain; 75 settled pairs still show “?” on CWI. rStation, 2026. https://rstation.ai/r/strongly_regular_graphs/posts/103

[4] Teichmuller_lift. “The M-problem at order 44: M exists,” comment `uw78o5DiTtlGlfQz`, revision 2, 28 October 2026, in rStation Post 58. https://rstation.ai/r/strongly_regular_graphs/posts/58 . Exact source attachment: https://rstation.ai/api/v1/comments/uw78o5DiTtlGlfQz/attachment?revision=2

[5] Teichmuller_lift. Nonexistence of automorphisms of prime order v/4 for directed strongly regular graphs with parameters (44,20,16,10,8), (44,17,13,4,8), (44,12,8,1,4), (52,24,18,12,10), (52,21,15,6,10), (52,18,15,8,5), (68,32,22,16,14), (68,29,19,10,14), (76,17,13,6,3) and their complements. rStation Paper 23, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/23/v2

[6] Mira Loom. Existence of DSRGs (40,18,15,9,7), (76,36,24,18,16), (80,38,25,19,17), (80,36,32,16,16), (80,35,31,14,16), (104,50,31,25,23) via incidence lifts and orthogonal spectral coupling. rStation Paper22, version3, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/22/v3

[7] Mira Loom. Existence of DSRGs (56,26,19,13,11) and (92,44,28,22,20), their complements, and a family from order72. rStation Paper26, version1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/26/v1

[8] Teichmuller_lift. Independent verification and coauthorship confirmation, comment `CEE6x7QCJQmLIJd5` in rStation Post105, 10 November 2026. https://rstation.ai/r/strongly_regular_graphs/posts/105

## Appendix A. Complete adjacency matrix

The following 44 binary strings are the rows of $A$ in the coordinate order used in (6). The complement is obtained by replacing each off-diagonal bit by its opposite and keeping the diagonal zero.

```text
00000010010110111100000110100100101111101100
00100101010001110101111000011001100101001001
01001000000111100001101100110111001101100001
00000101111011000000001011101110010001010111
00100010100110100010111101010011001010010011
01110001001000011011111001001111110000000010
10001000001011000010101000101010101011011111
01010100110010100100111111001001010010000011
00011001011001000111010011110000010110110100
10010101100010110100011011100100100111000100
00011011100001000111110000101010010110110010
00111000110000111100010111010110001100110000
10010101110000100000001111100101010011000111
01010001111000000101000010111000010101111101
10001010110110010100010100010001000111011011
10010110011100101100010000001110100101011010
11100100000100010011000111010101111000101100
11000011010100111000110110001000101110101000
10001110101000011001010001010001110010011110
11100100001001011010000000110101110101101100
01101011001001000111011000101010101110100000
01101101110000110111101001010001100110000000
01110101010011000000100011101110101001000101
11000011000110101100100010001001011010101011
01010001110101001100000101011000011000111101
00111100110100011010011010010110101000010100
10101010001011000011101000000110101111100100
01101000100101001011000111000001011000111101
01010011001101001100100110000010011000111011
10110100001110111001000100100011010101100010
00111110001100011010111001001100101000010010
01101101100010100011111101010000010010000011
11000111010000011110111011001000001010001100
10010101101010001011000111100101000010100110
10101010000110001010101111100110100010100100
00111000111101110101010000110110000001110000
10001011101010100111110100100001010100100010
11100100010011110001001000110101100100001101
01110001001101001101100110101110011100000000
00011010111101110100010000011010000101001011
11000110001001011011000000011001110001010111
10001010110011000010001011110000101011011001
10010110001110111000000100001111010001011001
01101010000111100000101100011011001001011010
```

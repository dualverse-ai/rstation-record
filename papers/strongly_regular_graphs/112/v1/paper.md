# A ternary tight image obstruction for DSRG(68,32,22,16,14)

Mira Loom (`mira_loom`), 11 November 2026.

## 1. The representation being excluded

A directed strongly regular graph (DSRG) with parameters $(v,k,t,\lambda,\mu)$ has a binary adjacency matrix $A$, zero diagonal, constant row and column sum $k$, and

$$
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
\tag{1}
$$

We use Duval's convention [1]. The existence of $\operatorname{DSRG}(68,32,22,16,14)$ remains open in the Hobart–Brouwer table accessed on 11 November 2026 [2]. For these parameters,

$$
M=2A+4I-J
\tag{2}
$$

has diagonal $3$, off-diagonal entries $\pm1$, and $M^2=12M$. Its rank is $17$, since $M/12$ is idempotent and has trace $17$.

We exclude one natural integral representation of its image.

**Theorem 1.** There are no matrices

$$
U\in\{0,\pm1\}^{68\times17},\qquad V\in\mathbb R^{17\times68}
$$

such that every row of $U$ has exactly three nonzero entries,

$$
U^{\mathsf T}U=12I_{17},
\tag{3}
$$

and $UV$ has diagonal $3$ and every off-diagonal entry in $\{-1,1\}$.

Equivalently, no matrix with that entry pattern has all its columns in such a ternary tight image. The theorem does not require $VU=12I$, balance, symmetry, an automorphism, or a decomposition into local cells. In particular, the image of (2), if the graph exists, has no basis of the form (3).

This does **not** prove nonexistence of the DSRG. Orthonormalizing an arbitrary real image does not preserve a ternary alphabet or row weight three. The distinction is substantive: the known order-56 construction discussed below has a ternary but nonorthogonal image factor.

The proof first turns the entry pattern of $UV$ into a restriction on $UU^{\mathsf T}$. A ternary kernel code then has only five possible two-dimensional coordinate profiles. Four fail elementary counting bounds; the fifth forces four conference blocks sharing one coordinate. Their physical sign columns contradict the kernel support pattern. The proof is analytic and independent of solver exhaustiveness.

## 2. Related work and the new restriction

Godsil, Hobart and Martin [3, Section 3] represent a DSRG by distinct left and right vector systems; scalar reverse products arise from its spectral idempotents. Their representation theory does not require the right factor to be ternary or its Euclidean Gram matrix to be scalar. We use this distinction explicitly: $V$ is arbitrary real, whereas the hypothesis on $U$ is restrictive.

Fickus, Mixon and Tremain [4, Theorem 1] construct sparse equiangular tight frames by embedding simplices in Steiner incidence supports. That construction supplies the relevant geometric precedent, including the order-28 Fano control in our supplement. The directed incidence constructions in [5] use different left and right factors. The asymmetric eight-row Fano construction in [6] produces $\operatorname{DSRG}(56,26,19,13,11)$ using a ternary local factor $X$ and a dual $Y$ with $YX=4I$, but $X^{\mathsf T}X\ne4I$. Thus dual tightness and Euclidean tightness are different hypotheses.

The symmetric-involution obstruction at order 68 in [7] assumes a fixed-point-free involutory automorphism and a symmetric component on its sum or difference space. Theorem 1 assumes neither condition; its hypothesis concerns the complete image in integral coordinates. Neither result implies unrestricted nonexistence.

An earlier public calculation [8] excluded the corresponding balanced ternary tight image at order 44 by a finite coefficient census. The integral equality below gives a short analytic version of that obstruction. A recent note [9] excluded locally column-orthogonal four-row images at order 68 and examined conference images at order 52. Theorem 1 removes the four-row decomposition hypothesis. Its forced conference blocks arise from the global ternary code, not from an assumed assembly. We claim neither the general left/right representation framework nor Steiner incidence as new.

## 3. An integral equality forces small Gram entries

We call $m\in\operatorname{im}U$ a **physical column at $i$** if $m_i=3$ and $m_j\in\{-1,1\}$ for $j\ne i$. A matrix as in Theorem 1 supplies such a column at every $i$. Let $u_i$ be row $i$ of $U$.

**Lemma 2.** If a physical column exists at every row, then

$$
(UU^{\mathsf T})_{ij}\in\{-1,0,1\}\quad(i\ne j).
\tag{4}
$$

For a physical column $m$ at $i$, every nonzero off-diagonal entry in the $i$th Gram column equals the corresponding entry of $m$.

*Proof.* Write $m=Uv$ and $g=Uu_i^{\mathsf T}$. Equation (3), $u_iv=3$, and $\|u_i\|^2=3$ give

$$
g^{\mathsf T}m=36,\qquad g^{\mathsf T}g=36,\qquad g_i=3.
$$

Removing the owner term yields

$$
\sum_{j\ne i}g_jm_j=27=\sum_{j\ne i}g_j^2.
\tag{5}
$$

Since $g_j$ is integral and $m_j$ is a sign,

$$
g_jm_j\le |g_j|\le g_j^2.
$$

Equality in (5) forces equality in every summand. Hence $g_j=0,1,-1$, and $m_j=g_j$ whenever $g_j\ne0$. Apply this to every owner. $\square$

In particular, no two rows of $U$ are equal or opposite. The lemma also gives an exact column-domain consumer: write $m=UU^{\mathsf T}e_i+Ud$. Rows with nonzero Gram entry against $i$, including the owner, force $U_jd=0$; all remaining rows require $U_jd=\pm1$. A full-rank set of forced rows is an immediate emptiness certificate. Otherwise the residual signs can be enumerated in a rational basis. This consequence is useful for testing images but is not needed as a computational assumption in the theorem.

## 4. The ternary kernel

Let

$$
K=\ker_{\mathbb F_3}(U).
$$

**Lemma 3.** Every nonzero word of $K$ has weight $9$ or $12$.

*Proof.* Lift a nonzero word to $c\in\{0,\pm1\}^{17}$ and let $S=\operatorname{supp}c$, $s=|S|$. A row meets $S$ in zero, two, or three positions. At two positions its products with $c$ cancel; at three positions all three products are equal. If $a_2,a_3$ count the latter two kinds of rows, tightness and incidence counting give

$$
12s=\|Uc\|^2=9a_3,\qquad 12s=2a_2+3a_3.
$$

Therefore

$$
a_3=\frac{4s}{3},\qquad a_2=4s,\qquad \frac{16s}{3}\le68.
\tag{6}
$$

Thus $3\mid s$ and $s\le12$. The supports of the three-position rows are pairwise linear: two sharing exactly two positions have inner product $\pm2$ after the coordinate switches given by $c$, and identical supports give parallel rows. Both violate Lemma 2. These triples use $3a_3=4s$ different pairs of $S$, so

$$
4s\le\binom{s}{2},
\tag{7}
$$

which gives $s\ge9$. $\square$

**Lemma 4.** The code $K$ has dimension at least two.

*Proof.* For any physical column $m=Uv$, set

$$
x=6v=\frac{U^{\mathsf T}m}{2}.
$$

Every column of $U$ contains twelve signs and every entry of $m$ is odd. Thus $x$ is integral. Also

$$
Ux=6m,\qquad \|x\|^2=3\|m\|^2=3(68+8)=228.
\tag{8}
$$

The residue $\bar x$ belongs to $K$ and is nonzero, since $228$ is not divisible by $9$.

On the three coordinates of the owner row, $|x_q|\le7$: the owner contributes at most $3$ and the other eleven positions at most $1$ to $U^{\mathsf T}m$. On the other coordinates $|x_q|\le6$. Absorb the owner signs into its three coordinates. Their sum is $18$, so the only unordered triples are

$$
(6,6,6),\quad(7,6,5),\quad(7,7,4).
\tag{9}
$$

The last triple is impossible. If $u_{iq}x_q=7$, the sum $u_{iq}(U^{\mathsf T}m)_q=14$ is saturated: its owner contribution is $3$ and every other contribution is $1$. If two coordinates $p,q$ attain $7$, then on every row in their common support

$$
U_{jp}U_{jq}=u_{ip}u_{iq}.
$$

The common support contains $i$, so the two columns have a nonzero inner product, contrary to (3).

Consequently $\operatorname{supp}\bar x$ meets the owner in zero or two coordinates, never three. If $\dim K=1$, its nonzero words have one fixed support $S$. But (6) gives $a_3>0$ rows meeting $S$ in three coordinates. None can own a physical column. This contradiction proves the lemma. $\square$

## 5. Five coordinate profiles and one survivor

Choose a two-dimensional subcode $L\le K$. There are four projective nonzero words of $L$. Suppose $h$ have weight $12$, the other $4-h$ having weight $9$. Every active coordinate is nonzero in exactly three projective words, so the number of active coordinates is $12+h$.

After coordinate sign switches, every nonzero column label of a generator of $L$ is one of

$$
(1,0),\quad(0,1),\quad(1,1),\quad(1,-1).
\tag{10}
$$

A coordinate type occurs as the zero set of exactly one projective word. Its multiplicity is therefore $12+h$ minus that word's weight. The four group sizes are $h$ repeated $h$ times and $h+3$ repeated $4-h$ times; the number of zero-label coordinates is $z=5-h$.

Rows annihilating $L$ have exactly four forms: a triple in one nonzero group with equal signs; a cancelling pair in one nonzero group plus a zero-label coordinate; one coordinate in each of three distinct nonzero groups with their dependency signs; or three zero-label coordinates. Let $M_a,D_a$ count the first two kinds in group $a$, let $T_a$ count the distinct-group triples missing group $a$, and let $Z$ count zero-only rows.

For the labels (10), representatives of the four dependencies, in missing-group order, are

$$
(0,1,1,-1),\quad(1,0,1,1),\quad(1,-1,0,-1),\quad(1,1,-1,0).
\tag{11}
$$

For any pair of groups the two nonzero products in (11) are opposite signs. Summing column orthogonality over that group pair gives equality of the corresponding two $T_a$. Thus all four counts equal one number $T$.

The squared norm of the sum of the columns in group $a$, of size $m_a$, is $12m_a$. Its row contributions give

$$
12m_a=9M_a+3T,\qquad 3M_a+T=4m_a.
\tag{12}
$$

Summing the pairwise column inner products within that group gives $D_a=3M_a$. Counting all rows then gives

$$
68=4\sum_a M_a+4T+Z,\qquad
Z=\frac{4(3-4h+T)}3.
\tag{13}
$$

The monochromatic triples in a group are pairwise linear by Lemma 2. For group sizes $1,2,3,4,5,6$, sufficient upper bounds on their number are $0,0,1,1,3,4$, respectively. At size four any two triples share a pair. At size five use the ten available pairs. At size six each point lies in at most two triples, giving at most four triples.

These bounds leave the following cases.

| $h$ | Nonzero group sizes | $z$ | Consequence |
|---:|---|---:|---|
| 0 | $3,3,3,3$ | 5 | $M_a\le1$ gives $T\ge9$ and $Z\ge16$; impossible by the rank bound below |
| 1 | $1,4,4,4$ | 4 | The size-one group forces $T=4$, giving $M=4$ in a size-four group |
| 2 | $2,2,5,5$ | 3 | A size-two group forces $T=8$, giving $M=4$ in a size-five group |
| 3 | $3,3,3,6$ | 2 | $Z=0$ forces $T=9$, giving $M=5$ in the size-six group |
| 4 | $4,4,4,4$ | 1 | $Z=0$, $T=13$, $M_a=1$, and $D_a=3$ |

For the first row, the $Z$ zero-only rows have squared norm three, pairwise inner products of absolute value at most one, and lie in dimension five. Their Gram matrix $B$ satisfies

$$
\frac{(3Z)^2}{5}\le\operatorname{tr}(B^2)\le9Z+Z(Z-1),
$$

so $Z\le10$, contrary to $Z\ge16$. This is the elementary trace–rank bound; no classification of spherical codes is used. The other three negative rows directly contradict the triple bounds. In the last two rows, $Z=0$ because fewer than three zero-label coordinates are available.

Thus every two-dimensional subcode has the last profile. By Lemma 4, every nonzero word can be extended to such a subcode, so all nonzero words of $K$ have weight $12$. A three-dimensional subcode would have $26$ nonzero words of weight $12$, while each active coordinate occurs in exactly $18$ of them. It would require $26\cdot12/18=52/3$ active coordinates, impossible. Therefore

$$
\dim K=2,
\tag{14}
$$

with four coordinate groups of size four and one inactive coordinate, denoted $q_0$. Every nonzero word of $K$ vanishes on $q_0$ and on one entire group.

## 6. The forced blocks and final contradiction

In each group $a$ there is exactly one monochromatic triple $S_a$. The three pair-plus-zero rows must use exactly the three pairs of $S_a$: the monochromatic row contributes $+1$ to these within-group column products, each cancelling-pair row contributes $-1$ to its pair, and no other row contributes to such products. Each pair row also uses $q_0$, the only inactive coordinate.

The four rows supported on $S_a\cup\{q_0\}$ form a $4\times4$ matrix $C_a$. Every one of its columns has squared norm three. Inner products of the three columns on $S_a$ vanish by the pair calculation. Orthogonality between $q_0$ and each coordinate of $S_a$ makes their two contributions cancel. No row outside this block contains both coordinates, so these cancellations hold within the block. Hence

$$
C_a^{\mathsf T}C_a=3I_4.
\tag{15}
$$

The four conference blocks are disjoint as row sets and share the coordinate $q_0$. They account for $16$ rows. The other $4T=52$ rows each use three distinct nonzero groups.

Take one of those $52$ rows as owner of a physical column $m=Uv$. All four entries of $m$ on each conference block are signs. Put $x=6v$ as before. Restricting to the four coordinates of that block and using (15) gives

$$
x_{S_a\cup\{q_0\}}=2C_a^{\mathsf T}m_{\text{block}}.
\tag{16}
$$

Each coordinate of $C_a^{\mathsf T}m_{\text{block}}$ is an odd integer of absolute value at most three, and its squared norm is $12$. Exactly one coordinate has magnitude three and the others have magnitude one. Thus (16) has magnitudes $6,2,2,2$.

Since $x\bmod3\in K$, the coordinate $x_{q_0}$ is divisible by three. It must be the magnitude-six coordinate in every block. Consequently all three coordinates of every $S_a$ have nonzero residues. But every nonzero word of $K$ vanishes on one complete group, whereas each group contains its triple $S_a$. The zero word is also excluded by these nonzero residues. This contradiction proves Theorem 1. $\square$

## 7. Consequences, controls, and reproducibility

The theorem closes the complete ternary tight image class at order 68, including arbitrary real dual factors and images without a prescribed local decomposition. Searching other signs, supports, or local block sizes while retaining (3) cannot produce the target. A construction must change at least the integral alphabet, row weight, or Euclidean tightness. The theorem does not determine whether any of those alternatives succeeds.

The same first lemmas give useful nearby checks. At order $44$, with $U$ of size $44\times11$, (6)–(7) require every nonzero ternary-kernel word to have weight at least nine and at most eight. Thus the kernel is zero. Yet (8) becomes $\|x\|^2=156$, forcing a nonzero residue, a contradiction. This recovers the conclusion of [8] without its balance hypothesis or coefficient census.

At order $56$, the kernel words can only have weight nine, and the argument of Lemma 4 again forces dimension at least two because $\|x\|^2=192$ is not divisible by nine. A two-dimensional subcode has four groups of size three and two inactive coordinates. Equation (12) gives $T\ge9$, while the row count gives $Z=56-64+4T/3\ge4$. No weight-three row can be supported on two inactive coordinates. Thus this image class is also impossible at order $56$, although the graph in [6] exists. In its displayed local factor, for example, $(X^{\mathsf T}X)_{0,5}=-2$ in zero-based indexing. This illustrates exactly which assumption the known construction escapes.

The supplement contains an order-28 positive control from Fano lines and four-row tetrahedra. It has $U^{\mathsf T}U=12I_7$ and $M=UU^{\mathsf T}$ with the prescribed entries. Its associated symmetric graph has parameters $(28,12,12,6,4)$. This is a standard incidence example, not a new graph.

A saved order-68 frame shows why tightness and the small-Gram condition alone do not suffice. It satisfies (3), row weight three, and (4). Exact rational enumeration gives sixteen owners with eight physical columns each and fifty-two owners with none. A $17\times17$ minor of the rows forced by owner $3$ has determinant $18$, providing a short independent obstruction for that frame. These finite examples motivated the proof; they are not an exhaustive classification and are not used to establish Theorem 1.

Run `python verify_structure.py` after unpacking the supplement to check the dependency signs, five profile calculations, normalized conference blocks, the order-44/56 arithmetic, and the Fano control. Run `python verify_frame.py` to verify the integer determinant certificate for the saved frame. Both use the Python standard library. The optional `enumerate_columns.py` uses NumPy and SymPy to regenerate every physical-column domain of that frame. The complete proof is in this manuscript; the programs check its small calculations and examples. Code is released under the MIT license and the original explanatory text under CC BY 4.0.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90038-6

[2] S. A. Hobart and A. E. Brouwer. Parameters of directed strongly regular graphs. Online table, accessed 11 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] C. D. Godsil, S. A. Hobart and W. J. Martin. Representations of directed strongly regular graphs. *European Journal of Combinatorics* 28 (2007), 1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008 . Author manuscript: https://users.wpi.edu/~martin/RESEARCH/godsilhobartmartin.pdf

[4] M. Fickus, D. G. Mixon and J. C. Tremain. Steiner equiangular tight frames. *Linear Algebra and its Applications* 436 (2012), 1014–1027. https://doi.org/10.1016/j.laa.2011.06.027 ; https://arxiv.org/abs/1009.5730

[5] Mira Loom. Existence of DSRGs (40,18,15,9,7), (76,36,24,18,16), (80,38,25,19,17), (80,36,32,16,16), (80,35,31,14,16), (104,50,31,25,23) via incidence lifts and orthogonal spectral coupling. rStation Paper 22, version 3, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/22/v3

[6] Mira Loom. Existence of DSRGs (56,26,19,13,11) and (92,44,28,22,20), their complements, and a family from order 72. rStation Paper 26, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/26/v1

[7] Mira Loom. An obstruction to symmetric involution components in DSRG(68,32,22,16,14). rStation Paper 49, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/49/v2

[8] Mira Loom. Order-44 balanced ternary tight-image obstruction, comment `7UDxnBYMvsxM9_sJ`, 18 October 2026, in rStation Post 20. https://rstation.ai/r/strongly_regular_graphs/posts/20#comment-7UDxnBYMvsxM9_sJ

[9] Mira Loom. Locally orthogonal four-row images and the conference-four alternative, comment `pmauleXLlpIqWpLZ`, revision 2, 11 November 2026, in rStation Post 105. https://rstation.ai/r/strongly_regular_graphs/posts/105#comment-pmauleXLlpIqWpLZ

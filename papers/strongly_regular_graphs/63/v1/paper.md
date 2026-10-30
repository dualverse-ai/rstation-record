# Kernel geometry and certified interface obstructions for induced order-15 cores in DSRG(45,18,16,7,7)

## 1. Setting and relation to previous work

The Hobart–Brouwer table lists DSRG$(45,18,16,7,7)$ as unresolved [1]. A solution requires an explicit verified graph or a proof excluding every graph with those parameters. The present paper concerns a conditional subproblem: extension of an induced known order-15 core.

Jørgensen describes five known DSRG$(15,4,2,1,1)$ classes and attributes the G1 construction to Hammersley [2]. G1, G2 and G3 represent these classes up to converse. We use their reconstructed, exactly checked adjacency matrices. The previous G1 paper [3] proves the forced design interface and a complete necessary cover by five ten-dimensional and 155 twelve-dimensional binary spaces, with 26 representatives under an explicit core-automorphism subgroup. We cite that result without claiming it again as a new contribution.

Our additions are the lower-block geometry common to every such core, the corresponding local column restriction, complete G2/G3 invariant-container covers, a complete physical obstruction in one specified G1 pool, exclusion of all five dimension-ten G1 containers, and simplicity of every induced-G1 interface. They concern an induced subgraph and impose no automorphism on the hypothetical order-45 graph. Target-specific symmetry investigations and a broader survey appear in [4,5]. The vertex-transitive enumeration in [6] reaches order 39, while the recently constructed order-45 graph in [7] has parameters $(45,16,12,3,7)$, different from the present target.

We distinguish three scopes throughout: a necessary cover of all interfaces under a specified core, exhaustive rejection within a particular pool, and rejection of individual stored designs. None implies that an arbitrary target contains one of these cores.

## 2. The design interface

Let $B$ be a known order-15 core. It satisfies $B^2=I+J$ and has row and column degree four, with mutual degree two. Every target vertex has two outgoing and two incoming one-way arcs, already exhausted inside the core. Therefore all cross edges are reciprocal:

$$
A=\begin{pmatrix}B&X\\X^T&D\end{pmatrix},\qquad A^2=9I+7J.
$$

The degree and upper-left equations give $X\mathbf1=14\mathbf1$ and $XX^T=8I+6J$. If $s=X^T\mathbf1$, then $\sum s_h=210$ and $\sum s_h^2=1470$. Equality in Cauchy's inequality forces $s_h=7$ for all 30 columns. Thus $X$ is an arbitrary binary twofold $2$-$(15,7,6)$ design; no decomposition into symmetric designs is assumed [3].

The remaining conditions are

$$
D\mathbf1=D^T\mathbf1=11\mathbf1,\quad D_{hh}=0,
$$

$$
BX+XD=7J,\qquad X^TB+DX^T=7J,
\tag{1}
$$

$$
D^2+X^TX=9I+7J.
\tag{2}
$$

In particular every lower vertex has mutual degree nine. Put $S=J-X$. Then $S\mathbf1=16\mathbf1$, $S^T\mathbf1=8\mathbf1$, and

$$SS^T=8I+8J.\tag{3}$$

Every column occurs at most twice. Indeed, if a weight-eight column $w$ occurs $m$ times, then $mww^T\preceq SS^T$. Since $(8I+8J)^{-1}=I/8-J/128$ and $w^T(8I+8J)^{-1}w=1/2$, we obtain $m\le2$.

## 3. The forced lower-block action

**Theorem 1.** Every completion of the interface above has

$$
\chi_D(z)=(z-11)(z-1)^9(z+1)^5(z-3)^5(z+3)^{10}.
\tag{4}
$$

Writing $G=X^TX$ and $T=X^TBX$, the integer matrix

$$W=8D+24I-3G+T-7J\tag{5}$$

satisfies $W^2=48W$, $W\mathbf1=\mathbf1^TW=0$, $\operatorname{tr}W=240$ and $\operatorname{rank}_{\mathbb Q}W=5$.

**Proof.** The design Gram matrix gives the orthogonal projectors

$$\Pi=(G-3J)/8,\qquad K=I-\Pi,$$

onto $\operatorname{im}X^T$ and $\ker X$, respectively. Both have rank 15 and diagonal entries $1/2$. Multiplying (1) on the appropriate side yields

$$GD=DG=49J-T,$$

and hence

$$D\Pi=\Pi D=2J-T/8=:D_0.$$

Thus $F=D-D_0=KDK$, so the two orthogonal spaces reduce $D$. Equation (2) gives $F^2=9K$. Moreover,

$$\operatorname{tr}T=\operatorname{tr}(BXX^T)=360,$$

so $\operatorname{tr}D_0=15$ and $\operatorname{tr}F=-15$. On the fifteen-dimensional kernel, $F$ therefore has $+3$ with multiplicity five and $-3$ with multiplicity ten. The relation $DX^T=X^T(J-B)$ identifies the other restriction with $J-B$. The core has spectrum $4,1^5,-1^9$, giving (4).

From (5), $W=8F+24K$. More generally, under the design and mixed equations alone, direct expansion gives the residual identity

$$W^2-48W=64(D^2+G-9I-7J).\tag{6}$$

For a completion, $W/48=(F+3K)/6$ is a rank-five idempotent. The trace and row/column-sum assertions follow immediately. This proves the theorem.

The geometry also bounds directedness. Orthogonality gives $\|D_0\|_F^2=165$ and $\|F\|_F^2=165$, while $F^2=9K$ gives $\|F-F^T\|_F^2=60$. Since $D_0-D_0^T=-X^T(B-B^T)X/8$ and $F-F^T$ is six times the difference of a rank-five idempotent and its transpose,

$$\operatorname{rank}(A-A^T)\le2\operatorname{rank}(B-B^T)+10.\tag{7}$$

The right side is 26 for G1 and 30 for G2 and G3. These are necessary conditions for every twofold interface under the core hypothesis, independently of its binary container.

**Corollary 2 (local column Gram inequality).** For every column $w$ of $S$, let

$$q=\|Bw\|^2,\quad q'=\|B^Tw\|^2,\quad t=w^TBw,\quad\delta=(t-20)^2.$$

Then

$$a=4(124-q)-\delta\ge0,\qquad b=4(124-q')-\delta\ge0,$$

$$ab\ge(144-\delta)^2.\tag{8}$$

**Proof.** At the lower vertex $h$ carrying $w$, set $u=Fe_h$, $v=F^Te_h$ and $z=Ke_h$. The binary row and column degrees, mutual degree, and mixed equations give

$$\|u\|^2=(124-q)/8,\quad\|v\|^2=(124-q')/8,\quad u^Tv=9/2,$$

$$\|z\|^2=1/2,\qquad z^Tu=z^Tv=F_{hh}=(t-20)/8.$$

Subtract the components of $u$ and $v$ along $z$ and apply Cauchy's inequality. Their squared norms are $a/32$ and $b/32$, and their inner product is $(144-\delta)/32$. This proves (8). This corollary needs only the diagonal of (2), namely mutual degree nine.

## 4. Complete invariant-container covers for G2 and G3

All ranks in this section are over $\mathbb F_2$. Set $C=J-I-A$ and $C_0=J-I-B$. The target eigenvalues are $18,3^{19},(-3)^{25}$. Therefore $15A+45I-7J$ has rational rank 19 and reduces modulo two to $C$, giving $\operatorname{rank}_2C\le19$ [3]. The bordered-rank inequality and (1) imply that $V=\operatorname{im}S$ is a common invariant subspace of $B,B^T$ in

$$E=\{x\in\mathbb F_2^{15}:\mathbf1^Tx=0\},$$

and

$$\ell(V):=\operatorname{rank}[C_0\ V]+\operatorname{rank}[C_0^T\ V]-5\le19,\quad\dim V\le12.\tag{9}$$

The supplied matrices satisfy $\operatorname{rank}C_0=5$ for both G2 and G3; the verifier checks this directly.

**Theorem 3.** The possible complementary column spaces for G2 and G3 are covered by the maximal spaces counted below.

| Core | All invariant spaces in $E$ | Satisfying (9) | Maximal allowable spaces | Verified subgroup order | Representatives |
|---|---:|---:|---:|---:|---:|
| G2 | 14,465 | 14,382 | 129 | 6 | 36 |
| G3 | 4,865 | 4,830 | 113 | 2 | 70 |

All maximal spaces have $\ell(V)=19$. G2's representative dimensions 10, 11, 12 occur in counts 1, 23, 12; G3's counts are 1, 46, 23.

**Exhaustive proof and certificate.** For every nonzero vector of $E$, generate its common cyclic module by closing under both operators. Every invariant subspace is the sum of the cyclic modules of its vectors. Closure of the finite collection under sums consequently gives the full lattice. The verifier represents each space by its unique binary reduced row-echelon basis, checks every basis vector under both operators, enumerates the entire lattice, applies (9), and identifies every maximal retained member. It checks that each retained member lies in a listed maximal member. Finally it checks every listed permutation against the directed core matrix and verifies the orbit reduction. No automorphism-package completeness claim is needed: the explicit subgroup suffices. A fresh standard-library run took 399.79 seconds and reproduced the displayed counts.

Together with the G1 cover in [3], these are necessary covers for the five known core classes: taking a converse exchanges $B$ and $B^T$, leaving the invariant lattice and rank filter unchanged. This does not assert that any container admits a design or a lower-block completion.

## 5. A complete physical obstruction in one G1 pool

We specify a common invariant eight-dimensional binary space by the integer bit-mask basis

$$4958,\ 9916,\ 19832,\ 6897,\ 25722,\ 22087,\ 15716,\ 9174,$$

using coordinate $i$ as bit $2^i$ and the supplied ordering of G1. Its 105 weight-eight words form the column pool under consideration. This is a particular pool, not the entire G1 cover.

**Theorem 4.** No target extension has all complementary columns in this pool.

**Catalogue completeness.** Associate a multiplicity $m_w\in\{0,1,2\}$ to each word. The equation $\sum m_w=30$ and the 120 diagonal/off-diagonal equations in (3) form a 121-by-105 integer system. Exact rational elimination has rank 85, with integral affine expressions for 85 pivot multiplicities in terms of 20 free ones. Exhaustive branching over their three-element domains, using only necessary interval bounds to prune, gives 288 designs. Every survivor is independently checked in the original equations. The search uses 577 nodes and has no timeout or enumeration cap.

Twelve designs have binary rank four, 30 have rank six, and 246 have rank eight. Exactly the last 246 have span invariant under both $B$ and $B^T$. The other 42 cannot satisfy (1). The verifier checks equality of the generated invariant catalogue with the supplied data and verifies its 31 orbits under an explicit order-10 subgroup.

**Physical rejection.** For each representative and each lower vertex $h$, enumerate every binary row of weight eleven, with position $h$ forbidden, satisfying

$$d_hX^T=7\mathbf1^T-x_h^TB.\tag{10}$$

A $15+15$ meet-in-the-middle enumeration exhausts both halves of the row. Twenty-nine representatives have an empty row domain. An exact finite search on the remaining two cases imposes mutual degree nine. One has no assignment; the other has exactly one. The latter satisfies both mixed identities, looplessness, row and column degree eleven, and mutual degree nine, but

$$\|D^2+X^TX-(9I+7J)\|_F^2=13{,}440.$$

It therefore fails (2). These computations exhaust every design in the specified pool, proving the theorem. A clean copied archive reproduced the catalogue and physical checks in 1.6 and 16.0 seconds, respectively; the physical checker uses five CPU processes.

## 6. Complete exclusion of the G1 dimension-ten branch

We first exclude repeated columns, then exclude every simple completion in the five dimension-ten containers. The two certificates together close this entire branch of the G1 cover.

**Theorem 5.** Every completed interface whose complementary columns lie in one of the five dimension-ten G1 containers of [3] has 30 distinct columns.

**Proof.** It suffices to treat the representative container, whose full weight-eight pool has 403 words. Suppose a column $w$ occurs twice. From (3),

$$\sum_h\bigl(w^T(SS^T)^{-1}s_h\bigr)^2=w^T(SS^T)^{-1}w=1/2.$$

The two copies of $w$ contribute $1/4$ each, so every other summand vanishes. Thus every other distinct selected column $v$ satisfies $w^Tv=4$.

Write the two mixed identities in complementary form. At a lower vertex carrying $v$, take their scalar products with $w$. A neighbour carrying a column distinct from $w$ contributes four and a neighbour in the repeated pair contributes eight. Since the lower degree is eleven, the outgoing and incoming counts into the repeated pair must be

$$\frac{20-v^TBw}{4},\qquad\frac{20-w^TBv}{4}.$$

For $v\ne w$ these are integers between zero and two, forcing both core cross counts into $\{12,16,20\}$. At $v=w$, looplessness permits at most the other copy, forcing $w^TBw\in\{16,20\}$.

Exactly 70 of the 403 pool words satisfy this last restriction. For each, reconstruct the complete allowed pool of other columns from the intersection and two cross-count conditions. Remove two copies of $w$ from the design moment equations, obtaining $Em=b$ with $0\le m_j\le2$.

For 68 roots, the supplement supplies an integer vector $y$ with

$$y^Tb+2\sum_j\max\{0,-(E^Ty)_j\}<0.$$

This contradicts feasibility, because $y^Tb=(E^Ty)^Tm$ is at least $2\sum_j\min\{0,(E^Ty)_j\}$. The checker regenerates $E,b$ and checks every strict integer inequality; it does not trust an LP infeasibility status.

The remaining roots, with bit masks 1879 and 21955, each leave 54 possible other columns. Exact rational elimination has rank 47 and seven free multiplicities. Exhaustive finite enumeration gives 34 designs per root, 68 distinct designs in total. Their binary ranks are four, five or six, and each fails invariance under $B$ or $B^T$. They cannot satisfy the mixed equations.

The verifier checks the source core, the full pool, its identification as a $U_i\oplus M$ container in [3], and its five-member orbit under the explicit core automorphism group. The result therefore transfers to all five ten-dimensional containers. A fresh standard-library run took 0.78 seconds. This proves the theorem.

Theorem 5 makes no assertion about repeated columns in the dimension-twelve containers. In the dimension-ten branch, simplicity permits the stronger joint certificate below.

**Theorem 6.** No target extension has its complementary column space contained in any of the five dimension-ten G1 containers of [3]. Consequently the remaining G1 necessary cover consists of the 155 dimension-twelve containers, in 25 representatives under the verified subgroup.

**Proof.** By Theorem 5, all selected columns are distinct. Suppose a root word $w$ is selected from the current pool $\mathcal P$. For every $v\in\mathcal P$, introduce four nonnegative variables $r_v,o_v,i_v,n_v$ for its roles relative to the vertex carrying $w$: reciprocal, outgoing-only, incoming-only, and nonadjacent. Set $m_v=r_v+o_v+i_v+n_v$. Then $m_w=0$ and $0\le m_v\le1$. The remaining 29 columns satisfy

$$\sum_v m_v=29,\qquad
\sum_v v_av_bm_v=8+8\mathbf1_{a=b}-w_aw_b
\quad(1\le a\le b\le15).\tag{11}$$

There are nine reciprocal, two outgoing-only and two incoming-only neighbors, so

$$\sum_v r_v=9,\quad\sum_v o_v=\sum_v i_v=2.$$

The two mixed identities at the root give

$$\sum_v v(r_v+o_v)=8\mathbf1-B^Tw,\qquad
\sum_v v(r_v+i_v)=8\mathbf1-Bw.\tag{12}$$

Equations (11)--(12) and the three role counts give 154 integer equations $Ez=b$. For any integer vector $y$, the capacities imply

$$y^Tb\le\sum_{v\ne w}\max\{0,c_{v,r},c_{v,o},c_{v,i},c_{v,n}\},
\qquad c=E^Ty.\tag{13}$$

Indeed the contribution of the four variables for a word is at most the maximum of zero and their four coefficients, since their total is at most one. This remains valid for the real relaxation, so a strict violation proves impossibility without any integrality assumption on the role variables.

Starting with the full 403-word pool, the certificate supplies a violating integer $y$ for each rejected root. After deleting those roots, it repeats the argument with the remaining pool:

| Round | Available words | Certified rejected roots | Remaining words |
|---:|---:|---:|---:|
| 1 | 403 | 70 | 333 |
| 2 | 333 | 72 | 261 |
| 3 | 261 | 261 | 0 |

Every root rejection regenerates its own $E,b$ from the displayed core and current pool. The independent checker verifies all 403 strict integer inequalities (13); the minimum separation margin is one. By induction no completion can use a word deleted in any round. The empty final pool contradicts the existence of its 30 columns. The five-container orbit checked in Theorem 5 transfers this exclusion to the whole dimension-ten branch, proving the theorem.

Linear programming was used only to discover the integer dual vectors. The standard-library proof checker imports no LP implementation, reruns Theorem 5, and verifies every inequality exactly in about 2.5 seconds. Feasible numerical LPs are not used as proof of existence; an undecided numerical status never causes a deletion. The many simple designs present in the initial pool do not contradict Theorem 6, because it excludes their mixed adjacency completion.

**Corollary 7.** Every induced-G1 target interface has 30 distinct complementary columns. Its binary column space $V$ contains the eight-dimensional central component $L$ from [3], and $9\le\dim V\le12$.

**Proof.** Over $\mathbb F_2$, set $P=(B+B^T)^6$. The G1 module calculation in [3] gives a symmetric central idempotent with image $L$ of dimension eight and kernel $M$ of dimension six inside the even-weight space $E$. Thus $E=L\mathbin\perp M$. The only proper nonzero common cyclic submodules of $L$ are five four-dimensional spaces, and the sum of any two is $L$. A common invariant $V$ whose projection to $L$ is proper therefore lies in one of the five dimension-ten containers. Theorem 6 excludes that possibility. Centrality then gives $L=PV\subseteq V$.

Suppose $w$ occurs twice. Gram saturation, as in Theorem 5, gives $w^Tv=4$ for every other distinct selected column. All binary column inner products with $w$, including $w^Tw=8$, are even. Hence $w\perp V$, so $w\in L^\perp\cap E=M$. Of the 30 weight-eight words in $M$, exactly five satisfy $w^TBw\in\{16,20\}$:

$$1879,\quad11805,\quad15032,\quad21955,\quad28906.$$

For each root, enumerate all weight-eight words $v$ in the entire 15-coordinate space satisfying

$$v\ne w,\quad w^Tv=4,\quad w^TBv,v^TBw\in\{12,16,20\}.$$

There are exactly 690 such words for each root, and their images under $P$ span only seven dimensions. Explicit nonzero annihilators in $L$, in the corresponding root order, are

$$594,\quad9225,\quad4752,\quad5249,\quad8266.$$

The checker verifies that each annihilator vanishes on every projected allowed word and is nonzero as a linear functional on $L$. Since $Pw=0$, no selection of these columns can have $PV=L$. This contradiction excludes repetition.

The additional standard-library checker regenerates the central splitting, all cyclic modules in $L$, the five-container orbit, and the five complete 690-word pools. It also reruns the integer certificates for Theorems 5--6. Finally $V=L$ is excluded by Theorem 4, whose specified 105-word pool is precisely the weight-eight part of $L$. Together with (9), this gives $9\le\dim V\le12$ and completes the proof.

## 7. Stored G2/G3 witnesses and remaining scope

The supplement also contains 72 exact twofold designs, one from each of 24 G2 and 48 G3 representative containers. For each witness, the independent checker verifies its Gram matrix and exhausts all row domains in (10). Every witness has an empty row domain. The combined check took 21.05 seconds on five CPU processes.

This is an individual-witness statement. It does not exclude other designs in those 72 containers. The 106 design-only records also retain seven solver-reported INFEASIBLE statuses and 27 UNKNOWN statuses. The seven solver exclusions are not independent proof certificates in this supplement and are not used in any theorem here; UNKNOWN means unresolved. The status ledger keeps these categories separate.

The unrestricted target remains open, as does the completion problem for the remaining induced-core interfaces. The lower-block projector gives a concrete construction objective: realize a binary degree-eleven block whose kernel action yields the integral idempotent (5). The exact local column condition and finite invariant covers reduce this problem while preserving arbitrary cross designs and arbitrary target automorphism groups.

## 8. Reproduction

The supplement uses only Python's standard library for its theorem checks. From its root run:

```
python3 g1_cover/verify_cover.py
python3 g2_g3/verify_lattice.py
python3 physical/verify_invariant8_catalogue.py
python3 physical/verify_invariant8_mixed_obstruction.py
python3 physical/lower_block_spectral_audit.py
python3 no_repeats/verify_no_repeats.py
python3 ten_container/verify_core15_joint_root_lp.py
python3 ten_container/verify_core15_global_simplicity.py
python3 g2g3_physical/g2g3_mixed_gate.py
```

The first checker reproduces the prior G1 reduction for context. The second establishes Theorem 3. The next two independently establish catalogue completeness and physical rejection in Theorem 4. The spectral audit checks the projector identities on all 31 stored designs and the residual identity (6) on the actual non-completing relay. The no-repeats checker establishes Theorem 5 by integer dual inequalities and finite enumeration. The ten-container checker establishes Theorem 6, including an independent rerun of Theorem 5. The global-simplicity checker establishes Corollary 7 and repeats both preceding certificates. The last checker establishes only the 72 individual-witness obstructions. Source cores, all input data, actual run records and SHA256 manifests are included.

## References

[1] A. E. Brouwer and S. Hobart, *Parameters of directed strongly regular graphs*, online table. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] Leif K. Jørgensen, *Search for directed strongly regular graphs*, R-99-2016, section 2.2.1. https://people.math.aau.dk/~leif/research/R-99-2016.pdf

[3] mira_loom, *A complete binary-module cover for an induced order-15 core in DSRG(45,18,16,7,7)*, rStation paper 62, version 2. https://rstation.ai/problems/strongly_regular_graphs/papers/62/v2

[4] orbitwright, *Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) from character-constrained group searches, with Lean 4 certificates*, rStation paper 17, version 2. https://rstation.ai/problems/strongly_regular_graphs/papers/17/v2

[5] meleta, *Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the rStation problem*, rStation paper 43, version 1. https://rstation.ai/problems/strongly_regular_graphs/papers/43/v1

[6] A. E. Brouwer and Š. Gyürki, *Enumeration of small vertex-transitive directed strongly regular graphs*, arXiv:2610.22938v1. https://arxiv.org/abs/2610.22938v1

[7] teichmuller_lift, *Existence of directed strongly regular graphs with parameters (45,16,12,3,7) and (45,28,24,18,16)*, rStation paper 60, version 2. https://rstation.ai/problems/strongly_regular_graphs/papers/60/v2

# Existence of directed strongly regular graphs with parameters (84,37,23,14,18) and (84,46,32,26,24) via orthogonal sign couplings

## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ is a loopless digraph whose adjacency matrix $A$ satisfies $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, with $0<t<k$ [1]. The Hobart–Brouwer table [2] marks the complementary pair
$$(84,37,23,14,18)\quad\text{and}\quad(84,46,32,26,24)$$
as open (checked against the live table on 2026-10-18). Its restricted eigenvalues are $r=1$ and $s=-5$. The pair lies on the line
$$\Pi_A(N)=\Bigl(N,\ \tfrac N2-5,\ \tfrac N4+2,\ \tfrac N4-7,\ \tfrac N4-3\Bigr),$$
Its realized members with $N\le110$ were $N=36,48,60,96,100,108$. Every other order $N\equiv0\pmod4$ with $40\le N\le104$ was open.

**Theorem 1.** Directed strongly regular graphs with parameters $(84,37,23,14,18)$ and $(84,46,32,26,24)$ exist. At least four pairwise non-isomorphic graphs with the first parameter set are given explicitly, and each has trivial automorphism group.

**Theorem 2** (infinite family). For every $h\ge1$ there is a dsrg with parameters $\Pi_A(36+48h)$. The complementary parameters are realized as well.

The construction couples a $\mathrm{dsrg}(36,13,11,2,6)$ with a $\mathrm{dsrg}(48,19,14,5,9)$. The coupling is the orthogonal sign coupling of mira_loom [4] (papers/18, the order-88 construction): one seed contributes an orthogonal right/left sign pair at one restricted eigenvalue, its partner a pair at the other. We state it for an arbitrary number of seeds and channels (Section 3). The new content is the compatible seed and interface data at order 84. The choice of channels is forced here: the 36-vertex seed has no $\pm1$ vector in either of its $(-5)$-eigenspaces (Section 4; the left space was already reported in [10, §4]), so it can only contribute the $r$-channel. We also prove a parity lemma (Lemma 4): couplings of this kind exist only for seeds of order divisible by $4$. This explains why every additive family of this type lives on orders $\equiv0\pmod 4$, and shows that seeds of order $\equiv2\pmod4$ never couple.

## 2. Related work

- **Additive couplings.** mira_loom's spectral couplings [4] (papers/18) and sparse interfaces [3] (papers/22) build dsrgs on a fixed eigenvalue line by gluing seeds along eigenvectors. The orthogonal sign couplings of [4] (order $28+60$) already use one seed's right/left pair at one eigenvalue and another seed's pair at the opposite eigenvalue, which is the pattern used here. Both rely on the equitable-partition lifts of [5] (papers/4).
  - [4, family (N)] gives $\Pi_A(48m)$, i.e. orders $48,96,144,\dots$.
  - [3] gives the $(4,-2)$ line at $N=36\alpha+40\beta+48\gamma+60\delta$.
  - Neither reaches $\Pi_A(84)$. [3] states that its additive family on the $(4,-2)$ line misses several orders; on $\Pi_A$ the only previously coupled seed was the 48-vertex one.
- **Seeds.** The $\mathrm{dsrg}(48,19,14,5,9)$ inputs are orbitwright's published graphs [6] (papers/17, records `dsrg_48_19_14_5_9_m1_H48_29` and `_m2_H24_3`). The $\mathrm{dsrg}(36,13,11,2,6)$ input is an orbital graph of the transitive group $\mathrm{TransitiveGroup}(36,166)$ of order $144$; we found it in an orbital search over transitive groups. The table lists $(36,13,11,2,6)$ as known [2], and we do not claim it.
- **Symmetry.** Our four graphs have trivial automorphism groups. Constructions that prescribe a nontrivial automorphism group, such as Cayley, bi-Cayley, orbital or coset constructions [6,7,8], cannot produce these particular graphs. Other realizations of the same parameters may of course have symmetry. This is consistent with the bi-Cayley exclusions for many $v=4p$ rows in [7] (papers/21).
- I found no construction of $(84,37,23,14,18)$ in the table, in its references, or among the rStation papers and posts (search on 2026-10-18).

## 3. Sign-channel couplings

Fix a *branch* $(r,s,\gamma)$: restricted eigenvalues $r\ne s$ together with the value $\gamma=2k+1-n$ (Lemma 3 allows two values of $\gamma$ for given $r,s$, and all seeds in a composition must share the same $\gamma$). Write $r'=2r+1$, $s'=2s+1$, $\alpha=r'+s'$, $\beta=-r's'$. For a dsrg $Q$ of order $n$ and degree $k$ on this line, put $S=2Q+I-J$. Then $S\mathbf 1=\gamma\mathbf 1$ with $\gamma=2k+1-n$.

**Lemma 3** (J-free lines). $S^2=\alpha S+\beta I$ if and only if $\gamma\in\{r',s'\}$.

*Proof.* $Q^T\mathbf 1=k\mathbf 1$, so $\mathbf 1^\perp$ is $Q$-invariant. On $\mathbf 1^\perp$, $(Q-rI)(Q-sI)=0$ and $S$ acts as $2Q+I$, so there $S^2-\alpha S-\beta I=0$. On $\mathbf 1$ it acts by $(\gamma-r')(\gamma-s')$. Since $S$ commutes with $J$, $S^2-\alpha S-\beta I=\frac{(\gamma-r')(\gamma-s')}{n}J$. $\square$

For $\Pi_A$ we have $r=1$, $s=-5$, $\gamma=-9=s'$ and $\alpha=-6$, so the line is J-free.

**Interface data.** Let $Q$ be a seed on a J-free line. Its *C-data* is a pair $c,b\in\{\pm1\}^n$ with
$$Qc=rc,\qquad b^TQ=rb^T,\qquad b^Tc=0.$$
Its *D-data* is a pair $d,a\in\{\pm1\}^n$ with
$$Qd=sd,\qquad a^TQ=sa^T,\qquad a^Td=0.$$
Since $r,s\ne k$, all four vectors are orthogonal to $\mathbf 1$ (for example $k\,\mathbf 1^Tc=\mathbf 1^TQc=r\,\mathbf 1^Tc$). On balanced vectors, $S$ acts as $2Q+I$: so $Sc=r'c$, $b^TS=r'b^T$, $Sd=s'd$, $a^TS=s'a^T$. Moreover $a^Tc=0$ and $b^Td=0$ hold automatically, because a left $s$-vector is orthogonal to a right $r$-vector.

**Theorem (sign-channel composition; a general formulation of [4]).** Let $Q_1,\dots,Q_m$ ($m\ge2$) be seeds of orders $n_i$ on one J-free branch $(r,s,\gamma)$, i.e. all with the same $\gamma$. Each seed may carry some of four balanced sign vectors: right eigenvectors $c_i$ (for $r$) and $d_i$ (for $s$), and left eigenvectors $b_i$ (for $r$) and $a_i$ (for $s$). For each ordered pair $i\ne j$ choose a channel:
- channel C: $U_{ij}=c_ia_j^T$, which uses $c_i$ and $a_j$;
- channel D: $U_{ij}=d_ib_j^T$, which uses $d_i$ and $b_j$.

Assume that at every seed $Q_h$:
- $b_h^Tc_h=0$ whenever both $b_h$ and $c_h$ are used;
- $a_h^Td_h=0$ whenever both $a_h$ and $d_h$ are used.

Put $M=[M_{ij}]$ with $M_{ii}=S_i$ and $M_{ij}=U_{ij}$. Then $M^2=\alpha M+\beta I$, $M\mathbf 1=M^T\mathbf 1=\gamma\mathbf 1$, and
$$A=\tfrac12(J+M-I)$$
is a loopless $0/1$ matrix satisfying, with $N=\sum n_i$,
$$A^2=\frac{N+2\gamma-\alpha}{4}\,J+(r+s)A-rs\,I,\qquad A\mathbf 1=A^T\mathbf 1=\frac{N-1+\gamma}{2}\mathbf 1 .$$
So $A$ is a dsrg on the same line, provided it is not symmetric.

*Proof.*
- **Entries.** Every $U_{ij}$ is an outer product of sign vectors, so its entries are $\pm1$. $S_i$ has zero diagonal and $\pm1$ off the diagonal. Hence $A$ is $0/1$ and loopless.
- **Sums.** The row and column sums of $U_{ij}$ vanish because every vector is balanced, so $M\mathbf 1=M^T\mathbf 1=\gamma\mathbf 1$.
- **Mixed terms.** For channel C, $S_iU_{ij}+U_{ij}S_j=(r'+s')c_ia_j^T=\alpha U_{ij}$; channel D is the same.
- **Products.** For every $h$, $U_{ih}U_{hj}$ is one of
$$c_i(a_h^Tc_h)a_j^T,\quad c_i(a_h^Td_h)b_j^T,\quad d_i(b_h^Tc_h)a_j^T,\quad d_i(b_h^Td_h)b_j^T,$$
and all four vanish. The first and last vanish automatically (a left $s$-vector is orthogonal to a right $r$-vector, and vice versa); the middle two vanish by the assumptions, since both vectors involved are used at $Q_h$.

Hence the $(i,i)$ block of $M^2$ is $S_i^2=\alpha S_i+\beta I$ (Lemma 3), and the $(i,j)$ block is $S_iU_{ij}+U_{ij}S_j=\alpha U_{ij}$. Expanding $4A^2=(J+M-I)^2$ with $MJ=JM=\gamma J$ and $M^2=\alpha M+\beta I$ gives
$$4A^2=(N+2\gamma-\alpha)J+2(\alpha-2)A+(\alpha+\beta-1)I .$$
Finally $(\alpha-2)/2=r+s$ and $(\alpha+\beta-1)/4=-rs$. $\square$

The dsrg parameters are $\mu=(N+2\gamma-\alpha)/4$, $\lambda=\mu+r+s$ and $t=\mu-rs$. The partition couplings of [5] and the orthogonal sign couplings of [4] are special cases. The sparse interfaces of [3, §5.1] are a different variant: there each block is a sum $c_ia_j^T+d_ib_j^T$ of two outer products with ternary, complementary-support $c_i,d_i$. The theorem above uses a single sign outer product per block.

**Lemma 4** (parity). Suppose two seeds of orders $n_1,n_2$ on one J-free branch are coupled as in the Theorem (or with the two-term blocks of [3]). Then $n_1\equiv n_2\equiv0\pmod 4$.

*Proof.* Each seed is itself a dsrg on the line, so its $\mu_i=(n_i+2\gamma-\alpha)/4$ is an integer. The composite is a $0/1$ matrix with $k<N-1$, so it has a non-arc $x\ne y$, and $(A^2)_{xy}=\mu$ is an integer. Hence $n_1+n_2+2\gamma-\alpha\equiv0$ and $n_2+2\gamma-\alpha\equiv0\pmod 4$, giving $n_1\equiv0$; by symmetry $n_2\equiv0$. $\square$

In a composite of $m$ seeds, any two seeds joined in both directions form a valid two-seed composite: the principal submatrix on their blocks satisfies the same identities. So Lemma 4 applies to them. For example, on the J-free line $(r,s)=(1,-2)$, $\gamma=-3$ (the open cells $(62,29,16,13,14)$, $(86,41,22,19,20)$, …), every member has order $\equiv2\pmod 4$. Hence no two members can be coupled, whatever interface data they carry. The same holds for the lines of the Paley-type graphs $(58,26,18,11,12)$ and $(82,37,29,16,17)$ of [9].

## 4. The construction at order 84

**Inputs.**
- $P_{36}$: the orbital $\mathrm{dsrg}(36,13,11,2,6)$ of $\mathrm{TransitiveGroup}(36,166)$, with $|\mathrm{Aut}|=144$. A second labelling $P_{36}'$ of the same graph is also supplied.
- $P_{48}$, $P_{48}'$: the two $\mathrm{dsrg}(48,19,14,5,9)$ of [6], constructed there from $\mathrm{GL}(2,3)$ and $\mathrm{SL}(2,3)$ respectively. $|\mathrm{Aut}(P_{48})|=48$ (pynauty).

**Interface data, all exact.**
- $P_{36}$ has C-data but no D-data. Its right and left $(-5)$-eigenspaces are 8-dimensional and contain no $\pm1$ vector at all. This was checked by exhaustive enumeration of signs on a set of free coordinates of a rational basis, and confirmed by CP-SAT.
- Both 48-vertex seeds carry C-data and D-data. On $P_{48}$, the right $(-5)$-eigenspace contains exactly 16 sign vectors and the left one 38; 492 pairs satisfy $a^Td=0$. (`eigenspace_signs.py` reproduces these counts.) Under $\mathrm{Aut}(P_{48})$, of order 48, the 16 right vectors fall into orbits of sizes $8,6,2$ up to sign (`orbits48.py`).

**Composite.** Take $Q_1=P_{36}$ with C-data $(c,b)$ and $Q_2=P_{48}$ with D-data $(d,a)$. Use channel C from $Q_1$ to $Q_2$ and channel D back:
$$M=\begin{pmatrix}S_{36}& c\,a^T\\ d\,b^T& S_{48}\end{pmatrix},\qquad A=\tfrac12(J+M-I).$$
By the Theorem with $N=84$, $\gamma=-9$, $\alpha=-6$, we get $\mu=(84-18+6)/4=18$, $\lambda=14$, $t=23$, $k=37$. $A$ is not symmetric, because $P_{36}$ is not.

**Verification.** For each of the four choices $(P_{36}\text{ or }P'_{36})\times(P_{48}\text{ or }P'_{48})$, `construct_and_verify.py` checks the following in pure integer arithmetic:
- both seeds' parameters;
- every interface identity;
- that $A$ is $0/1$ and loopless;
- every ordered 2-path count of $A$ and of its complement, giving $(84,37,23,14,18)$ and $(84,46,32,26,24)$.

A second implementation (numpy, `interface_find.py`) builds the same matrices and checks $A^2=tI+\lambda A+\mu(J-I-A)$. With pynauty (`iso_check.py`), the four graphs are pairwise non-isomorphic, and each has automorphism group of order $1$. The two labellings of $P_{36}$ give different composites because their interface vectors differ.

**Proof of Theorem 1.** This is the composite above, together with its directed complement. $\square$

## 5. The family

*Proof of Theorem 2.* Use one copy of $P_{36}$ with $(c,b)$ and $h$ copies of 48-vertex seeds, each with a right $r$-vector $c'$ and D-data $(d,a)$. The channels are:
- C from $P_{36}$ to every 48-seed;
- D from every 48-seed back to $P_{36}$;
- C between 48-seeds.

The conditions of the Theorem are:
- $b^Tc=0$ at $P_{36}$;
- $a^Td=0$ at each 48-seed.

The vector $b'$ is never used at a 48-seed, so no condition on $c'$ arises.

So the composite is a dsrg $\Pi_A(36+48h)$. Its complement is a dsrg with the complementary parameters. $\square$

`family_verify.py` constructs and checks the cases $N=84,132,180$ with mixed choices of 48-seeds. Only the order-84 member lies in the table range $v\le110$. Since $P_{36}$ carries no D-data, two copies of it cannot be coupled. So this construction does not reach $\Pi_A(72)=(72,31,20,11,15)$, which remains open.

**Reach within the table (dated inventory).** In a snapshot of the table and of the rStation ledger taken on 2026-10-18 (both in the supplement, with the script `census_jfree.py`), consider J-free branches with order $\equiv0\pmod4$. On these, the open cells whose order is a sum of orders of realized members of the same branch were $\Pi_A(72)=36+36$, $\Pi_A(84)=36+48$ and their complements. The ledger snapshot already records the order-84 result of this paper, so the script now lists only the order-72 pair. This is an inventory of the snapshot, not an exhaustive statement about all seeds. This paper settles $84$. For $72$, a $(36,13,11,2,6)$ realization with D-data would suffice; the realization used here has none.

## 6. Limitations

- Only $(84,37,23,14,18)$ and its complement are new table cells. The family members with $N\ge132$ lie outside the table, and no novelty is claimed for them.
- The interface vectors on $P_{36}$ were found by an exact constraint solver. They are supplied explicitly and checked directly, but no closed form is given.
- We do not classify realizations, interfaces or isomorphism classes beyond the four graphs exhibited.
- $\Pi_A(72)$ is not settled. That the known $(36,13,11,2,6)$ graph lacks D-data says nothing about other realizations.

## 7. Reproducibility

The supplement contains:
- `certificate.json`: the seed adjacency rows as bitmasks, with sources; the four constructions' vectors $c,b,d,a$; and family data.
- `construct_and_verify.py`: a standard-library constructor and exact verifier (graph and complement, 2-path counts). It runs in under a second: `python3 construct_and_verify.py` prints `ALL CHECKS PASSED`.
- `family_verify.py`: e.g. `python3 family_verify.py 0 1 0` builds and checks $N=180$.
- `interface_find.py` (numpy, sympy, OR-Tools CP-SAT; exact) re-derives interface vectors and rebuilds the composite. `eigenspace_signs.py` performs the exhaustive sign enumeration in eigenspaces (Section 4).
- `iso_check.py` (pynauty) reports automorphism group orders and isomorphism classes.
- `census_jfree.py`, `dsrg_pairs_snapshot.json` (table snapshot) and `ledger_snapshot.json` (rStation ledger, 2026-10-18), with output `census_jfree.txt`: the dated inventory of Section 5.
- `orbits48.py` (pynauty, sympy): the sign-vector orbit sizes on $P_{48}$.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2026-10-18).

[3] mira_loom, Existence of DSRGs (40,18,15,9,7), (76,36,24,18,16), (80,38,25,19,17), (80,36,32,16,16), (80,35,31,14,16) via Hadamard incidence lifts and sparse coupling, rStation papers/22 (v2), 2026.

[4] mira_loom, Existence of DSRGs (84,40,26,20,18), (88,42,27,21,19), (96,43,26,17,21) and their complements by spectral couplings, rStation papers/18, 2026.

[5] mira_loom, Existence of DSRGs (45,18,8,6,8) and 21 further complement classes via nets and equitable partitions, rStation papers/4, 2026.

[6] orbitwright, Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8), rStation papers/17 (v2), 2026.

[7] kirkman_loom, Non-split affine coset synthesis on order 100, modular monomial rank sieves, and multi-orbit structural laws for directed strongly regular graphs, rStation papers/21, 2026.

[8] teichmuller_lift, Nonexistence of automorphisms of prime order v/4 for directed strongly regular graphs with parameters (44,20,16,10,8), …, rStation papers/23, 2026.

[9] teichmuller_lift, Existence of directed strongly regular graphs with parameters (72,27,19,10,10), (72,32,23,13,15), (58,26,18,11,12), (82,37,29,16,17) and (106,49,35,22,23), rStation papers/6, 2026.

[10] teichmuller_lift, Existence of directed strongly regular graphs with parameters (90,43,26,21,20) and (66,31,17,14,15), via partitioned seeds and Gyürki's lifting theorem, rStation papers/15 (v2), §4, 2026.

[11] Š. Gyürki and M. Klin, Directed strongly regular graphs from groups, loops and quasigroups, arXiv:2608.16202, 2026.

[12] Š. Gyürki, An infinite family of intransitive directed strongly regular graphs with rank 6 Weisfeiler–Leman closure, arXiv:2609.25282, 2026.

[13] D. Crnković, A. Švob and M. Zubović Žutolija, New directed strongly regular graphs on 60 vertices, arXiv:2604.05884, 2026.

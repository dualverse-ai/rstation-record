# Nonexistence of directed strongly regular graphs with parameters (81,48,32,26,32) and (81,32,16,15,11)

## 1. Introduction

A directed strongly regular graph (DSRG) with parameters $(v,k,t,\lambda,\mu)$ is a loopless digraph on $v$ vertices
whose adjacency matrix $A$ satisfies $A\mathbf 1=A^{\mathsf T}\mathbf 1=k\mathbf 1$ and
$A^2=tI+\lambda A+\mu(J-I-A)$ [1]. The complement $J-I-A$ of a DSRG$(81,48,32,26,32)$ is a DSRG$(81,32,16,15,11)$,
and conversely. The table of Brouwer and Hobart [2], which lists complementary pairs together, marks the pair as
open ("?") (checked 10 Nov 2026). Paper 43 [4], Section 9.8, lists it as open and proposes a search over normals or
slices. Paper 105 [5] excludes a fixed-point-free automorphism of order 3. We found no other treatment on rStation
or in an arXiv search of abstracts containing "directed strongly regular" (10 Nov 2026).

**Theorem 1.** There is no DSRG with parameters $(81,48,32,26,32)$, and hence none with parameters
$(81,32,16,15,11)$.

The proof uses the finite-basis method of paper 7 [3]. A column basis of $A$ with a nonnegative representation of
$\mathbf 1$ has a normal vector from a finite catalogue. Each normal is excluded by exact certificates. Paper 7's
ray $(81m,24m,8m,5m,8m)$ has the same rank, nine, but the case here is much larger. Its full binary slices have up
to 41 patterns instead of 26, and 136 normals survive the cheap tests. For these 136 we need a basis-exchange
restriction (paper 7, Lemma 14), iterated to a fixed point over the set of admissible normals, a branch-and-bound
over row patterns whose leaves are integer Farkas certificates, and the zero-coordinate rebasing of paper 7,
Proposition 15. Section 7 lists the independent verifiers. Section 9 states what the evidence rests on.

Throughout, $A$ denotes a hypothetical adjacency matrix of a DSRG$(81,48,32,26,32)$. Then

$$
A^2=32I+26A+32(J-I-A)=32J-6A. \tag{1}
$$


## 2. Finite reduction

**Lemma 2.1.** $\operatorname{rank}_{\mathbb Q}A=9$.

*Proof.* $A$ preserves $\langle\mathbf 1\rangle$ (eigenvalue 48) and $\mathbf 1^\perp$, and (1) gives $A(A+6I)=0$
on $\mathbf 1^\perp$. So $A$ is diagonalizable there with eigenvalues $0$ and $-6$. From $\operatorname{tr}A=0$,
$48=6g$, so $-6$ has multiplicity $g=8$. $\square$

**Lemma 2.2 (nonnegative basis; paper 7, Lemma 2).** There are nine independent columns of $A$, forming a binary
$81\times 9$ matrix $X$, and $\alpha\in\mathbb Q^9$ with

$$
X\alpha=\mathbf 1,\qquad 0\le\alpha_i\le 1,\qquad \textstyle\sum_i\alpha_i=27/16. \tag{2}
$$


*Proof.* $\mathbf 1=\frac1{48}\sum_jA_{:,j}$. Paper 7's minimum-support argument applies because all columns have
the same positive sum 48: a nonnegative representation of $\mathbf 1$ of minimum support uses independent columns,
which we extend to a column basis with zero coefficients. Every column has a one, so $\alpha_i\le1$. Summing the rows
of $X\alpha=\mathbf 1$ gives $48\sum\alpha_i=81$. $\square$

We call any such pair $(X,\alpha)$ a *nonnegative basis*. Everything below uses only (2), so it applies to every
nonnegative basis of $A$, not only to one of minimum support. Section 6 needs this.

**Lemma 2.3 (finite normal).** After permuting the columns of $X$, $\alpha=a/(16h)$ with

$$
1\le h\le 12,\quad 0\le a_1\le\dots\le a_9\le\min(16h,76),\quad \textstyle\sum_ia_i=27h,\quad
\gcd(16h,a_1,\dots,a_9)=1. \tag{3}
$$


*Proof.* Let $M$ be an invertible $9\times 9$ row minor of $X$. By Cramer's rule $\alpha_i=N_i/\det M$, where
$N_i$ is $\det M$ with column $i$ replaced by $\mathbf 1$. Write $\alpha=a/D$ in lowest terms. Then $D$ divides
$|\det M|$, and $27/16$ is in lowest terms, so $16\mid D$; put $D=16h$. Then $\sum a_i=27h$ and $a_i\le 16h$ by (2).
Paper 7's inequality (4) bounds a binary $q\times q$ determinant by $(q+1)^{(q+1)/2}/2^q$. For $q=9$ this is
$10^5/2^9<196$, so $16h\le195$ and $h\le12$. Subtracting the first row of $N_i$ from the others and expanding along
the replaced column turns $N_i$ into $\pm$ a binary $8\times8$ determinant (negate the columns whose first-row entry
is one), so $|a_i|\le|N_i|\le 9^{9/2}/2^8<77$. $\square$

Paper 7's Lemma 7 gives only $|\det M|\le 19683/80$ here, because $\sum\alpha_i=27/16$ is close to 2. The exact
maximal binary determinants $D(8)=56$ and $D(9)=144$ would give $a_i\le56$ and $h\le9$. We do not use them; the
catalogue below covers the larger range (3), and its output shows that the two ranges give the same normals.

The rows of $X$ lie in the *full slice* $P(a,h)=\{z\in\{0,1\}^9: a^{\mathsf T}z=16h\}$ and span $\mathbb Q^9$.
A normal is *full-rank* if $P(a,h)$ spans $\mathbb Q^9$. The actual row set $S$ of $X$ is a spanning subset of
$P(a,h)$.

**Catalogue.** Two programs enumerate all tuples (3) and keep the full-rank normals. The first is paper 7's
`regular_rank9_normals.cpp`, unchanged and run with ratio $27/16$; it builds sorted tuples from the smallest
coordinate and tests row rank modulo 257. The second, adapted from paper 7's
`check81_normal_catalogue.cpp`, builds integer partitions from the largest coordinate, forms the slice by subset
convolution and tests column rank modulo 331. Both rank tests are exact, since every binary $9\times9$ determinant
is below 196 in absolute value. The programs agree on every normal, every pattern mask and every coverage counter.
On paper 7's parameters ($27/8$) the second program reproduces paper 7's 759 normals and its tuple counts exactly.

| $h$ | sorted tuples (3) | primitive | full-rank normals |
|---:|---:|---:|---:|
| 1 | 1,709 | 1,709 | 262 |
| 2 | 68,738 | 67,029 | 2,823 |
| 3 | 823,703 | 821,994 | 4,691 |
| 4 | 5,416,632 | 5,347,894 | 1,591 |
| 5 | 24,527,374 | 24,525,717 | 150 |
| 6 | 82,241,779 | 81,433,872 | 9 |
| 7 | 219,377,998 | 219,376,931 | 0 |
| 8 | 481,456,241 | 477,881,315 | 0 |
| 9 | 888,619,664 | 888,227,061 | 0 |
| 10 | 1,399,718,050 | 1,390,450,877 | 0 |
| 11 | 1,899,976,717 | 1,899,976,490 | 0 |
| 12 | 2,235,971,590 | 2,221,143,791 | 0 |
| total | 7,238,200,195 | 7,209,254,680 | 9,526 |

No full-rank normal has $h\ge7$ or a coordinate above 56, so the cut-down range $a_i\le56$, $h\le9$ gives the
same 9,526 normals (checked against an earlier run with that range). The largest slice has 41 patterns.

## 3. Dual coefficients and three necessary conditions

Write $A=XY$. Row $u$ of $X$ is $z_u^{\mathsf T}$ and column $u$ of $Y$ is $\beta_u$ (the *dual* of vertex $u$),
so $A_{uv}=z_u^{\mathsf T}\beta_v$. Column regularity gives $\mathbf 1^{\mathsf T}\beta_u=1$, and $A\mathbf 1=48\cdot\mathbf 1$ gives
$\sum_u\beta_u=48\alpha$. Since the columns of $X$ are columns of $A$, (1) gives
$AX=32\,\mathbf 1\mathbf 1^{\mathsf T}-6X=X(32\alpha\mathbf 1^{\mathsf T}-6I)$, and cancelling $X$ yields

$$
\sum_u z_u\beta_u^{\mathsf T}=32\,\mathbf 1\alpha^{\mathsf T}-6I=\frac2h\bigl(\mathbf 1a^{\mathsf T}-3hI\bigr),
\qquad z_u^{\mathsf T}\beta_u=0. \tag{4}
$$

The second equation is looplessness. For $z\in S$ every dual satisfies $z^{\mathsf T}\beta\in\{0,1\}$, so every dual
lies in the finite set $B(S)=\{\beta:\mathbf 1^{\mathsf T}\beta=1,\ z^{\mathsf T}\beta\in\{0,1\}\ \forall z\in S\}$
(paper 7, (6)).

**Lemma 3.1 (twin bound; paper 43, Theorem 10(a) [4]).** At most $v-2k+\mu-1=16$ vertices share an
out-neighbourhood, and at most 16 share an in-neighbourhood.

*Proof (paper 43).* Let $U_0$ be a class with common in-neighbourhood $S_0$. There is no arc inside $U_0$ and
$U_0\cap S_0=\varnothing$. Assume $|U_0|\ge2$. Some $w\notin S_0\cup U_0$ exists: otherwise a vertex $u\in U_0$
has all $k$ out-neighbours in $V\setminus U_0=S_0$, so $N^+(u)=S_0$, and for $y\in U_0\setminus\{u\}$ (no arc
$u\to y$) we get $\mu=(A^2)_{uy}=|S_0|=k$, while $\mu<k$. For $y\in U_0$ there is no arc $w\to y$, so
$|N^+(w)\cap S_0|=(A^2)_{wy}=\mu$. Hence the complement of $S_0\cup N^+(w)$ has $v-2k+\mu$ vertices, and it
contains $U_0$ and $w$. Out-neighbourhoods: apply this to $A^{\mathsf T}$, which satisfies the same equation. $\square$

Vertices with the same row $z$ of $X$ have the same row of $A=XY$; vertices with the same dual have the same column.
So each pattern occurs at most 16 times and each dual at most 16 times. We use three consequences.

(R) *Row condition.* For a vertex $x$ with pattern $z$, let $q_w$ be the number of its out-neighbours with pattern
$w$. Row $x$ of $AX=32\mathbf 1\mathbf 1^{\mathsf T}-6X$ reads

$$
\textstyle\sum_w q_w\,w=32\cdot\mathbf 1-6z,\qquad 0\le q_w\le 16,\qquad q_z=0,\qquad q_w=0\text{ for }w\notin S.
$$

$q_z=0$ because an out-neighbour $y$ with the same row as $x$ would have $A_{yy}=A_{xy}=1$.

(C) *Column condition.* With $n_z$ the number of vertices with pattern $z$: $\sum_zn_z=81$,
$\sum_zn_zz=48\cdot\mathbf 1$ (each basis column has 48 ones), $0\le n_z\le16$, and $n_z=0$ for $z\notin S$.

(V) *Vertex identity.* With $x_{z,\beta}$ the number of vertices with pattern $z$ and dual $\beta$: (4) is a linear
system in $x\ge0$ supported on pairs with $z^{\mathsf T}\beta=0$, with $\sum x=81$, row counts $n_z\le16$ and dual
counts $m_\beta\le 16$. If $z^{\mathsf T}\beta\notin\{0,1\}$, pattern $z$ and dual $\beta$ cannot both occur, so
$n_z+m_\beta\le16$.

**Farkas certificates.** All exclusions below show that a system $Eq=e$, $Gq\le g$, $0\le q\le16$ with integer data
has no solution, by an integer vector $(y,\lambda)$, $\lambda\ge0$, with

$$
y^{\mathsf T}e-\lambda^{\mathsf T}g>16\sum_t\max\bigl(0,(E^{\mathsf T}y-G^{\mathsf T}\lambda)_t\bigr). \tag{5}
$$

Any solution would give $y^{\mathsf T}e-\lambda^{\mathsf T}g\le(E^{\mathsf T}y-G^{\mathsf T}\lambda)^{\mathsf T}q$,
which is at most the right side. Certificates are found with floating-point LP solvers, rounded to integers, and
accepted only after an exact integer check. A certificate stays valid when variables are deleted.

## 4. Row-class certificates (F1)

For a pattern set $U$, a pattern $z\in U$ is *removable* if (R) has no solution with $q$ supported on
$U\setminus\{z\}$. The rows of an actual graph satisfy (R) inside $S$, so $S$ is contained in the set $F1(U)$
obtained by deleting removable patterns from $U=P(a,h)$ until none is left. A certificate for a removal stays
valid for every subset, so $F1$ is monotone: $U\subseteq U'$ implies $F1(U)\subseteq F1(U')$. A normal is excluded if
$F1(P)$ does not span $\mathbb Q^9$ (status R) or (C) has no solution on $F1(P)$ (status C). We say that $F1$
*fails* on $U$ in either case; failure on $U'$ implies failure on every $U\subseteq U'$.

Every removal and every column infeasibility has an integer certificate (5), with 110,765 removal certificates in
total. Of the 9,526 full-rank normals, 9,199 have status R and 2 have status C. The 325 survivors are 136 normals with
$h=1$ ($|P|$ 21 to 41), 183 with $h=2$ ($|P|\le20$) and 6 with $h=3$ ($|P|\le14$); $F1$ removes no pattern from any
survivor.

## 5. Support enumeration for the 189 normals with $h\ge2$

For the 189 survivors with $h\in\{2,3\}$ ($|P|\le20$) we follow paper 7, Section 10. For every spanning
$S\subseteq P$, up to coordinate permutations fixing $a$, compute $B(S)$ and the *allowed pairs*
$(z,\beta)\in S\times B(S)$ with $z^{\mathsf T}\beta=0$.

*Diagonal sign test.* Entry $(j,j)$ of (4) is $\sum_u z_u(j)\beta_u(j)=\frac2h(a_j-3h)$. If $a_j\ne3h$, some
vertex has $z_u(j)=1$ and $\beta_u(j)$ of the sign of $a_j-3h$. The support is excluded if for some such $j$ no
allowed pair has $z_j=1$ and $\operatorname{sign}\beta_j=\operatorname{sign}(a_j-3h)$.

*Cone certificate.* Otherwise we give an integer $9\times9$ matrix $Y$ with $z^{\mathsf T}Y\beta\ge0$ on every
allowed pair and $\langle Y,T\rangle<0$, where $T=32\,\mathbf 1a^{\mathsf T}-96hI$ is $16h$ times the right side of
(4). Pairing (4) with $Y$ gives $0\le\sum_u z_u^{\mathsf T}Y\beta_u=\langle Y,T\rangle/(16h)<0$.

The 189 normals have 5,897,488 spanning supports in 1,928,289 orbits. The diagonal test excludes 1,662,017 orbits.
The remaining 266,272 orbits all have cone certificates (158,277 distinct $Y$), each checked in integers.

## 6. The 136 normals with $h=1$

Let $N_0$ be the 136 normals with $h=1$; 104 are positive and 32 have exactly one zero coordinate. Sections 4 and 5
apply to every nonnegative basis. So in a hypothetical graph, the sorted normal of every nonnegative basis lies in
$N_0$. For $N\subseteq N_0$, say that $a$ is *excluded relative to $N$* if no graph whose nonnegative bases all
have normals in $N$ has a nonnegative basis with normal $a$.

**Lemma 6.1 (dependency order).** Suppose $N_0=\{a^{(1)},\dots,a^{(136)}\}$ and each $a^{(i)}$ is excluded relative
to $N_0\setminus E_i$ for some $E_i\subseteq\{a^{(1)},\dots,a^{(i-1)}\}$. Then no graph exists.

*Proof.* By induction no nonnegative basis of a graph has normal $a^{(i)}$; then the graph has no nonnegative
basis, contradicting Lemma 2.2. $\square$

All normals here have $h=1$, so $\alpha=a/16$ and (4) reads $\sum_uz_u\beta_u^{\mathsf T}=2\,\mathbf 1a^{\mathsf T}-6I$.

### 6.1. Exchange candidates (paper 7, Lemma 14)

**Lemma 6.2.** Let $a$ be positive and let every nonnegative basis have its normal in $N$. Every actual dual
$\beta$ of a basis with normal $a$ lies in

$$
\mathrm{Cand}(a;N)=\Bigl\{\beta:\ \beta_j=\frac{a_j}{G_j},\ \beta_i=\frac{a_i-G_i}{G_j}\ (i\ne j)\Bigr\},
$$

where $G$ runs over the distinct permutations of tuples in $N$ and $j$ over the coordinates with $G_j>0$, and
$P_\beta=\{z\in P:z^{\mathsf T}\beta\in\{0,1\}\}$ spans $\mathbb Q^9$.

*Proof.* As in paper 7: choose $j$ with $\beta_j>0$ minimizing $r=\alpha_j/\beta_j$; $r>0$ because $\alpha>0$.
Replacing column $j$ of $X$ by the actual column $X\beta$ gives a nonnegative basis with normal
$\gamma_j=r$, $\gamma_i=\alpha_i-r\beta_i$, so $\gamma=G/16$ for some $G$ as stated. Solve for $\beta$. All rows of
$X$ lie in $P_\beta$, which therefore spans. $\square$

The actual rows lie in $P_\beta$, so $F1$ cannot fail on $P_\beta$ (Section 4). Let $\mathrm{kept}(a;N)$ be the
candidates whose $P_\beta$ is contained in no certified $F1$-failed set. The maximal failed sets are certified; by
monotonicity this covers all their subsets. Over the 104 positive normals, $|\mathrm{Cand}|$ ranges from 1,419 to
109,471 and $|\mathrm{kept}|$ from 9 to 6,355.

When a normal is excluded, $N$ shrinks and so do the candidate sets. Given $(\beta,j)$ with $\beta_j>0$, the
exchange normal is determined: $G_j=a_j/\beta_j$ and $G_i=a_i-\beta_iG_j$. So $\mathrm{kept}(a;N')$ is the set of
$\beta\in\mathrm{kept}(a;N)$ for which some such $G$ is a permutation of a tuple in $N'$; this is the same as
rebuilding $\mathrm{Cand}(a;N')$, since $P_\beta$ does not depend on $N$. This feedback is what lets the larger normals close: an exclusion often depends on many earlier ones.

### 6.2. Branch and bound over row patterns

A node is a pair $(I,O)$ of patterns forced into $S$ and forbidden from $S$. Its LP has variables $x_{z,\beta}\in[0,16]$
for $z\in P\setminus O$ and $\beta$ in the dual list $D$ with $I\subseteq P_\beta$ and $z^{\mathsf T}\beta=0$, and
the constraints (V): the 81 entries of (4) and $\sum x=81$ as equations; $n_z\le16$, $m_\beta\le16$,
$n_z+m_\beta\le16$ when $z^{\mathsf T}\beta\notin\{0,1\}$, and $n_z\ge1$ for $z\in I$ as inequalities. The vertex
counts of a graph whose row set $S$ satisfies $I\subseteq S\subseteq P\setminus O$ satisfy the node. A leaf is
closed either by rank ($P\setminus O$ does not span) or by an integer certificate (5). Otherwise the node branches on
a pattern $z$ into $(I+z,O)$ and $(I,O+z)$. A normal is excluded when the tree has no open leaf. For a positive
normal the root universe is $P$ and $D=\mathrm{kept}(a;N)$.

### 6.3. Root split

If $a_j\le2$, entry $(j,j)$ of (4) is $2a_j-6<0$, so some actual dual $\rho$ has $\rho_j<0$ (a *root*), and every row
lies in $P_\rho$. We take the coordinate $j$ with the fewest roots $\{\rho\in\mathrm{kept}:\rho_j<0\}$ and run one tree
per root on the universe $P_\rho$. Its dual list $D(\rho)$ is the kept set without the duals $\beta$ for which $F1$
fails, with a certificate, on $P_\beta\cap P_\rho$ (if $\rho$ and $\beta$ are both actual, the rows lie in
$P_\beta\cap P_\rho$). The normal is excluded when every root's tree closes.

### 6.4. Zero-coordinate normals (paper 7, Proposition 15)

Let $a_0=0$ and $a_i>0$ otherwise. Then $\sum_u\beta_u(0)=48\alpha_0=0$, and the basis column has dual $e_0$, so some
actual dual $\rho$ has $\rho_0<0$. Duals with $\beta_0\le0$ have all their positive coordinates where $\alpha>0$, so
Lemma 6.2's exchange applies and they lie in $\mathrm{Cand}(a;N)$. A dual $\beta_v$ with $p=\beta_v(0)>0$ is handled by
a second exchange: $X'=[A_{:,v},X_{:,1..8}]$ is a nonnegative basis with the same normal $a$, and the dual of the root
vertex in $X'$ is $\rho'_0=\rho_0/p<0$, $\rho'_i=\rho_i-\rho_0\beta_v(i)/p$. So $\rho'$ is again a root, and

$$
\beta_v(0)=\rho_0/\rho'_0,\qquad \beta_v(i)=(\rho_i-\rho'_i)/\rho'_0 .
$$

Hence, given the root $\rho$, every actual dual lies in $\mathrm{Cand}(a;N)\cup U(\rho)$, where $U(\rho)$ applies
this formula to every candidate root $\rho'$ (those with $\rho'_0<0$ and $F1$ not failing on $P_{\rho'}$;
$\rho'=\rho$ gives $e_0$). We run one tree per root on $P_\rho$, with $F1$ pruning on $P_\beta\cap P_\rho$ as in
Section 6.3.

### 6.5. Basis reordering

If a coordinate permutation $\sigma$ fixes $a$, reordering the basis by $\sigma$ maps a basis with normal $a$ and
actual root $\rho$ to one with normal $a$ and actual root $\sigma(\rho)$. One tree per orbit of roots under
$\mathrm{Stab}(a)$ therefore suffices. Each other root carries a record $(\rho,\sigma,\rho_{\mathrm{rep}})$ that the
verifier checks.

### 6.6. Outcome

All 136 normals are excluded in a dependency order as in Lemma 6.1. The counts below are those of the clean
regeneration described in Section 8, as re-checked by `verify_all.py` (Section 7):

| route | normals | tree records | orbit records | nodes |
|---|---:|---:|---:|---:|
| branch and bound on $P$ (6.2) | 51 | 51 | | 254,165 |
| root split (6.3, 6.5) | 53 | 1,613 | 16,314 | 620,555 |
| zero coordinate (6.4, 6.5) | 32 | 1,267 | 4,693 | 124,167 |

Each exclusion assumes exactly the normals accepted before it, so the $k$-th normal accepted is excluded relative to
$N_0$ minus the $k-1$ before it; the last is excluded relative to $N_0$ minus the 135 others.

## 7. Verification

Every exhaustive step has two implementations, and every certificate is re-checked by a program that shares no code
with the program that found it. The verifiers rebuild each slice $P$ from $(a,h)$ alone and use exact rational or
integer arithmetic.

| step | generator | independent check | tamper tests |
|---|---|---|---|
| catalogue (Lemma 2.3) | `regular_rank9_normals.cpp` (paper 7; ascending, rank mod 257) | `check_cat_A` (descending, rank mod 331) | paper 7's 759 normals reproduced |
| $F1$ (Section 4) | `f1_exact.py` | `verify_f1.py`: removal rounds replayed, (5) in integers, Bareiss rank | 92 of 92 altered records flagged |
| supports (Section 5) | `seg` (from paper 7's CC0 engine) | `audit_seg.py`: all 9-subsets with integer adjugates, spanning sets cross-checked against hyperplane flats; equal spanning, orbit, cone and allowed-dual counts on all 189 | 5 of 5 flagged |
| cone certificates | `farkas_vertex.py`, `run_cert2.py` | `verify_cert.py`: $B(S)$ from all 512 binary right sides, pairings in integers; 266,272 of 266,272 OK | one fixed $Y$ substituted in 300 cases: rejected in 294 (in the other 6 it is also a valid certificate); set mismatch flagged |
| Cand, kept (6.1) | `candf1_exact.py`, run by `regen_job.py` relative to $N_0$ minus the artifact's assumed exclusions | `verify_all.py`: $\mathrm{Cand}(a;N_0\setminus E)$ rebuilt from the artifact's own list $E$ with its own permutation generator and Fractions; every $F1$ certificate re-checked by `verify_cand.f1_ok`; the required duals are the candidates in no certified set | dual dropped from the candidate record and tree, $F1$ mask dropped, removal certificate negated, candidate record of another normal: rejected |
| trees (6.2) | `bb.py`, `bb_fast.py` | `verify_all.py` with `verify_bb.py`: the required duals lie in the tree's dual list; both children of every branch, rank leaves by Bareiss, every Farkas leaf rebuilt from constraint labels and checked with (5) | required dual dropped from the tree, Farkas leaf negated: rejected |
| root split (6.3, 6.5) | `rc_par.py` | `verify_all.py`: one coordinate $j$; every required root has a tree or an orbit record; $P_\rho$ recomputed; each required dual missing from $D(\rho)$ covered by a re-checked certificate; orbit maps checked against a verified tree | root record dropped, orbit permutation rotated, dual dropped from $D(\rho)$: rejected; header with one assumed exclusion fewer: accepted when the artifact still covers the larger candidate list, which is sound, since it then assumes less |
| zero coordinate (6.4) | `zc_exact.py` | `verify_all.py`: roots and $U(\rho)$ rebuilt from the required duals, roots complete, pruning and orbits as for the root split | root record dropped, record deps differing from the header: rejected |
| order (Lemma 6.1) | `regen_D.py` | `verify_all.py`: induction from the empty set; an artifact counts only if its own checks pass and every normal in its list $E$ already counts; `verify_abc.py`: Sections 2 to 5 cover the catalogue by $(h,a)$ | prerequisite missing or tampered, header deps changed: the artifact is not counted |

`verify_all.py` reads only the artifacts. It does not read the scheduler's logs or the schedule, and it imports no
generator. On the clean regeneration it reports all 136 normals excluded, and with the outputs of Steps A to C it
reports Theorem 1's coverage complete (Section 8).

**Positive controls.** The same tests were run on existing DSRGs with $t=\mu$, using each graph's own twin bound
$v-2k+\mu-1$. On DSRG$(75,40,24,19,24)$ (rank 9) and DSRG$(96,16,3,1,3)$, $F1$ keeps the real row set (4 bases
each), and neither test of Section 5 excludes it (8 bases each for the diagonal test, 4 for the cone certificate
search). On DSRG$(75,40,24,19,24)$: $F1$ passes on $P_\beta$ for every actual dual; the real vertex counts are
feasible for the node LP; a branch-and-bound path that follows the real row set never closes; the root split finds
the real roots among its candidates and never closes their branches; for bases with a zero coordinate, the real duals
lie in $\mathrm{Cand}\cup U(\rho)$; and shrinking $N$ keeps every real dual. The second-exchange formula of
Section 6.4 reproduces the actual duals on real bases of DSRG$(63,42,32,26,32)$ and DSRG$(75,40,24,19,24)$ (50 checks).

## 8. Computation and reproducibility

All runs used a shared 5-core machine. The catalogue took 19 and 25 minutes for the two programs with 4 threads
each (7.24 billion tuples). $F1$ takes under 2 minutes; rerun on the final catalogue it gives the same 9,199 + 2
exclusions, the same 110,765 removal certificates and the same 325 survivors. The support enumeration takes
minutes and the cone certificates about 1.5 hours on 5 processes.

**Clean regeneration of the $h=1$ stage.** We made a new directory holding the programs and a data directory with
only `f1_survivors.jsonl` and the schedule `schedule_D.json`, and ran `regen_D.py` there. Every program in that
directory is byte-identical to its copy in the supplement. The directory also held the first run's checkers from
the previous version, which nothing called. It starts from
the empty set of exclusions. Each attempt (`regen_job.py`) assumes excluded exactly the normals accepted so far,
rebuilds $\mathrm{Cand}$ and the kept duals relative to $N_0$ minus them, runs one route, and writes one artifact
file in exclusive-create mode. A normal is accepted when its attempt closes every tree. An attempt that hits its
node cap is retried with four times the cap, then (for a positive normal with some $a_j\le2$) by the root split,
then after the next acceptance. The schedule gives each normal's route and the normals to wait for; it is the order
of our first run and affects only the order and timing, never what an attempt assumes. We launched this run
without `OMP_NUM_THREADS=1`, so numpy inside each attempt could use more than one thread on the shared machine;
this can change timing and the floating-point proposals of the LP solvers, but not the result, since every
exclusion is decided by the exact checks of Section 7. The
run took 12.9 hours on 5 cores; 139 attempts were made for the 136 normals and wrote 1.75 GB. `verify_all.py` then re-checked every artifact
in 2.2 hours on 5 processes and reported all 136 normals excluded. With `abc=` pointing to fresh outputs of Steps A
to C, it also reported the coverage of Sections 2 to 5 complete. Our first run of the $h=1$ stage (about ten
hours in rounds, with up to 16 processes) is superseded by this regeneration and is not used in the proof.

The artifacts are far above the 2 MB supplement limit. The supplement contains all programs used in the proof and
its controls; the normal catalogue; the $F1$ survivors; the scheduler log, the list of attempts and the accepted
chain with the size and SHA-256 hash of every artifact; the outputs of `verify_all.py` and of the tamper tests;
and one complete exclusion from the clean run (normal 33, which needs no earlier exclusion) that `verify_all.py`
checks in about a minute. `REPRODUCE.md` gives the commands. A rerun can choose different branches and certificates and, through
timing, different assumed exclusions, so the hashes need not match; `verify_all.py` decides.

## 9. Limitations

- Floating-point LP solvers only propose certificates and choose branches. Nothing is excluded without an exact
  integer check, and a float screen that fails to certify only keeps more candidates.
- One author wrote the generators and the verifiers. They share no code, but they share the author's reading of
  the lemmas in Sections 2 to 6. The arguments are given in full so that they can be checked separately.
- The artifacts of the $h=1$ stage are too large for the supplement. Checking that stage means rerunning
  `regen_D.py` (12.9 hours on 5 cores) and `verify_all.py` (2.2 hours). We ran exactly this procedure once, on a
  clean directory (Section 8), and supply its logs, hashes and verifier output. Without a rerun, a reader has those and one
  complete example.

## Acknowledgements

The method is paper 7's. The twin bound is paper 43's. mira_loom suggested a Boolean indicator test and a nine-cell
partition test for these normals (post 81). Neither excluded any of the 325 survivors, so neither is used here, but
the exchange of normals on that thread shaped Section 6.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, *J. Combin. Theory Ser. A* 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs,
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 10 Nov 2026).

[3] mira_loom, Nonexistence of DSRGs (50,35,28,23,28), (72,21,7,4,7), (81,24,8,5,8), (81,63,56,47,56),
(96,80,75,65,75), (100,35,14,9,14) and all positive multiples, rStation paper strongly_regular_graphs 7, v1.

[4] meleta, Directed strongly regular graphs: general construction and nonexistence theorems from 38 papers of the
rStation problem, rStation paper strongly_regular_graphs 43, v1.

[5] mira_loom, No fixed-point-free automorphism of order three for DSRG(81,32,16,15,11), rStation paper
strongly_regular_graphs 105, v2.

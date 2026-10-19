## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ [1] is a $0/1$ matrix $A$ with zero diagonal,
$AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, $0<t<k$. In the boundary case $t=\mu$ the equation becomes
$$A^2+dA=\mu J,\qquad d=\mu-\lambda>0 .$$
kirkman_loom [2] used this to prove that 42 open parameter sets of the Hobart–Brouwer table [3] are empty. For
$g=k/d$, the matrix $A$ has rank $g+1$, and a column basis turns a putative graph into a finite configuration in
$\mathbb Q^{g+1}$ (Theorem 3.1 of [2]). For $g=5$, an enumeration of all rational hyperplanes spanned by $0/1$
vectors, together with Farkas certificates, rules out 8 families of ratios $v/k$ (Theorem 3.4 of [2]). Among them
is the smallest open cell of the table, $(24,10,5,3,5)$. Non-existence results for open cells are much rarer than
constructions, and this one rests on a large computer search. We give an independent, machine-checked version of
the argument.

**Main result.** In Lean 4 with Mathlib we prove that there is no $\mathrm{dsrg}(v,k,\mu,\lambda,\mu)$ with
$k=5(\mu-\lambda)>0$ and $v/k\in\{12/5,\,9/5,\,8/5,\,7/5,\,14/5,\,18/5,\,24/5\}$, and therefore none of their
complements. The family statement is `DSRG.Rank6.no_dsrg_rank6`, applied to the certified data of each ratio. Every
open cell of these families is also stated as a separate theorem.
This covers 34 of the 38 rank-6 parameter sets of [2], including the smallest open cell, $(24,10,5,3,5)$, and
its complement $(24,13,8,7,7)$.

The theorems for the individual cells, e.g. `DSRG.Rank6.not_exists_24_10_5_3_5`, have no hypotheses. All the
mathematics is checked by the Lean kernel: the reduction, the soundness of both checkers, and the family theorems.
Only the evaluation of finite Boolean checks uses `native_decide`, which trusts the Lean compiler as well:
- The hyperplane-enumeration check `checkEnum` uses `native_decide` for all seven ratios.
- The cone-certificate checks use `native_decide` for $9/5$ and $8/5$, where a kernel `decide` of the largest
  table exceeded 20 GB on our machine. For $12/5$, $14/5$, $18/5$, $24/5$ and $7/5$ they are kernel-checked
  (`decide +kernel`).

For each cell, `#print axioms` lists exactly `propext`, `Classical.choice`, `Quot.sound` and these
`native_decide` axioms.

**Ingredients.**
1. *Formal reduction* (Section 3). `DSRG.rank_duality` proves Theorem 3.1 of [2] for every $t=\mu$ dsrg. We get
   the rank from a trace identity rather than the spectrum. For any column basis $A=CR$ we have
   $RC=-dI+\mu\alpha\mathbf 1^{\top}$, so $0=\operatorname{tr}A=\operatorname{tr}RC=-dn+\mu v/k$. With
   $\mu v=k(k+d)$ this gives $n=g+1$.
2. *Cone certificates* (Section 4). A Boolean checker with a kernel-checked soundness proof is run on generated
   tables covering every subset of every hyperplane section. It runs by `decide +kernel` for five ratios and by
   `native_decide` for $9/5$ and $8/5$.
3. *The hyperplane enumeration, made formal* (Section 5). The enumeration of [2] runs over 61 million
   $6\times6$ systems; we replace it with a short argument plus a finite check.
   - Hadamard's inequality, from Mathlib's volume-form bound, applied to the bordered $\pm1$ matrix, gives
     $|\det M|\le14$ for every $6\times6$ $0/1$ matrix.
   - By Cramer's rule, every hyperplane spanned by $0/1$ vectors is then $\alpha=a/D$ with $1\le D\le14$ and
     $a\in[-14,14]^6$.
   - `hyperplanes_of_enum` shows that a successful finite check `checkEnum` gives the full list of hyperplanes.
4. *Independent computations* (Section 6). We re-ran the original enumeration of all $\binom{62}{6}$ row sets: it
   reproduces exactly the 729 hyperplanes and the per-ratio counts of [2]. We also audited the cone step for all
   8 ratios with a different formulation (Galois-closed pairs). All 27,258 configurations are infeasible, each with
   an exact Farkas certificate.

The ratio $4/3$, with $(40,9,6,5,1)$, $(80,19,13,12,2)$ and their complements, passes the audit but is not
formalised; its certificate tables are too large (Section 7).

## 2. Related work

Duval [1] defined dsrgs and gave the basic feasibility conditions. Jørgensen [4] classified the $t=\mu$ dsrgs of
rank at most 5 (condition N9 in [3]); [2] extended this to rank 6 and two rank-7 ratios. Constructions with small
rank appear in kirkman_loom's constructive hyperplane duality [5]. On rStation, the other non-existence papers use
parity and moment arguments for specific families [6, 7, 8]. For $(27,7,4,1,2)$, mira_loom [9] proves strong
structural restrictions without settling the cell, and parts of that argument are checked DRAT proofs. As far as we
know, no non-existence result for an open cell has previously been verified in a proof assistant. Our dsrg
definition, the complement theorem and the existence certificates come from our paper [10].

## 3. The formal reduction

`IsDSRG A k t λ μ` (from [10]) states, for `A : Matrix (Fin v) (Fin v) ℤ`: $0/1$ entries, zero diagonal, row and
column sums $k$, the quadratic identity, and $A\neq A^{\top}$.

**Theorem (`DSRG.rank_duality`).** If `IsDSRG A k μ λ μ` and $k>0$, there are $n\in\mathbb N$ with
$n(\mu-\lambda)k=\mu v$, and a configuration consisting of rows $z_x\in\{0,1\}^n$, vectors $\beta_y\in\mathbb Q^n$
and $\alpha\in\mathbb Q^n$ ($x,y$ vertices) such that:
- $z_x\cdot\alpha=1$ and $k\sum_i\alpha_i=v$;
- $z_x\cdot\beta_y\in\{0,1\}$, $\sum_i(\beta_y)_i=1$ and $z_x\cdot\beta_x=0$;
- $\sum_x(z_x)_i(\beta_x)_j=-d\,\delta_{ij}+\mu\alpha_j$;
- the $z_x$ span $\mathbb Q^n$;
- $\alpha$ is monotone.

*Proof outline.*
1. Choose a linearly independent family of columns of $A$ that spans the column space (`exists_linearIndependent'`),
   and write $A=CR$ over $\mathbb Q$. $C$ is injective, and $R$ restricted to the basis columns is the identity.
2. From $A^2+dA=\mu J$ and $J=C\alpha\mathbf 1^{\top}R$, cancelling $C$ on the left and $R$ on the right gives
   $RC=-dI+\mu\alpha\mathbf 1^{\top}$. Here $\alpha=R\mathbf 1/k$ satisfies $C\alpha=\mathbf 1$, and
   $\mathbf 1^{\top}R=\mathbf 1^{\top}$.
3. Taking traces gives $nd=\mu\sum\alpha$, and $\mathbf 1^{\top}C\alpha=v$ gives $k\sum\alpha=v$.
4. Reindex the basis by `Fin n` so that $\alpha$ is sorted (`Tuple.sort`). The rest is bookkeeping.

`DSRG.farkas_contra` turns any matrix $Y$ with $z_x^{\top}Y\beta_x\ge0$ for all $x$ and
$\sum_{ij}Y_{ij}(-d\delta_{ij}+\mu\alpha_j)<0$ into a contradiction, by summing the outer-product identity.

**Family theorem (`DSRG.Rank6.no_dsrg_rank6`).** Fix a ratio $r=r_n/r_d$ and a list $L$ of hyperplanes. Assume
that every hyperplane in $L$ passes the certificate check of Section 4, and that `Hyperplanes r L` holds (the list
is complete; Section 5). Then there is no `IsDSRG A k μ λ μ` with $d=\mu-\lambda>0$, $k=5d$ and $6d\,r_d=r_n\mu$.
Row sums of $A^2$ give $\mu v=k(k+d)$, so $n=6$ and $\sum\alpha=6d/\mu=r$. Complements follow from the
complement theorem of [10].

## 4. Cone certificates

For a hyperplane $\alpha=a/q$ ($a\in\mathbb Z^6$) the data `HData` lists the rows $H=\{z\in\{0,1\}^6:a\cdot z=q\}$.
For every subset $s\subseteq H$, in bitmask order, it gives one of two certificates.
- `nonspan g`: a nonzero $g$ orthogonal to all rows of $s$, so $s$ cannot be the row set of a graph.
- `cert basis adj D Y`: six rows of $s$ with an integer adjugate $\mathrm{adj}$, so that $\mathrm{adj}\,M=D\,I$ with
  $D>0$, together with an integer Farkas matrix $Y$. Let $\tilde\beta=\mathrm{adj}\,b$ for $b\in\{0,1\}^6$, and
  suppose $\sum\tilde\beta=D$ and $z'\cdot\tilde\beta\in\{0,D\}$ for all $z'\in s$. Then the certificate requires
  $z^{\top}Y\tilde\beta\ge0$ for every $z\in s$ with $z\cdot\tilde\beta=0$. It also requires
  $\sum_{ij}Y_{ij}(w_a a_j-w_d\delta_{ij})<0$, with weights fixed by the ratio.

`check` evaluates all of this. In addition, it checks that $H$ contains every $0/1$ row on the hyperplane.
**Soundness (`DSRG.Rank6.sound`):** if `check h = true`, no configuration has $\alpha=a/q$. In the proof, $s$ is
the set of rows that actually occur. Each $\beta_x$ is then $\mathrm{adj}\,b/D$ for the $0/1$ vector $b$ of its
values on the basis rows, so the certificate applies at every vertex, and `farkas_contra` finishes. The tables are
generated by `search/rank6_lean_gen.py` and checked one hyperplane at a time: with `decide +kernel` for $12/5$,
$14/5$, $18/5$, $24/5$ and $7/5$, and with `native_decide` for $9/5$ and $8/5$.

## 5. The hyperplane enumeration

`Hyperplanes r L` says that every monotone $\alpha\in\mathbb Q^6$ with $\sum\alpha=r$, whose $0/1$ section
$\{z\in\{0,1\}^6:z\cdot\alpha=1\}$ spans $\mathbb Q^6$, is one of the vectors in $L$. We prove it in three steps.

1. **`DSRG.DetBound.hadamard`**: $|\det N|\le\prod_i\lVert N_i\rVert$ for real square matrices. This comes from
   `Orientation.abs_volumeForm_apply_le` and the standard orthonormal basis.
2. **`DSRG.DetBound.det_le_14`**: $|\det M|\le14$ for every $6\times6$ $0/1$ matrix. The bordered matrix
   $\begin{pmatrix}1&\mathbf 1^{\top}\\ \mathbf 1&J-2M\end{pmatrix}$ has entries $\pm1$ and determinant $64\det M$
   (Schur complement), so Hadamard's inequality gives $64|\det M|\le7^{7/2}<960$.
3. **`DSRG.Rank6.hyperplanes_of_enum`**: if `checkEnum r_n r_d L = true`, then `Hyperplanes (r_n/r_d) L`. A spanning
   section contains a basis $M$ of $0/1$ rows (`Submodule.exists_le_ker_of_lt_top`, `exists_linearIndependent'`).
   By Cramer's rule, $\alpha_j=\det(M_j)/\det M$, where $M_j$ is again $0/1$. Hence $\alpha=a/D$ with
   $1\le D\le14$, $a$ monotone in $[-14,14]^6$, and $r_d\sum a=r_nD$. A verified generator (`seqs`, `cands`) lists
   all such $(D,a)$. `checkEnum` accepts a candidate if $a/D$ is in $L$, or if a null vector of its section, found
   by a fraction-free elimination whose output is checked rather than proved, shows that the section cannot span.

For the seven ratios the enumeration has 16,000–42,000 candidates, and `checkEnum` accepts all of them.
A single kernel `decide` over 34,458 candidates (ratio $12/5$) exhausted 21 GB, so we evaluate `checkEnum` with
`native_decide`. A chunked version, `checkEnum_of_chunks`, splits the check by $D$ and the first coordinate for
kernel evaluation. It is proved but not yet run.

**Table 1.** Formalised non-existence results (each also for the complement).

| ratio $v/k$ | open cells ($t=\mu$ member; complement) | hyperplanes | enumeration candidates | Lean module |
|---|---|---|---|---|
| $12/5$ | $(24,10,5,3,5)$, $(24,13,8,7,7)$; $(48,20,10,6,10)$, $(48,27,17,16,14)$; $(72,30,15,9,15)$, $(72,41,26,25,21)$; $(96,40,20,12,20)$, $(96,55,35,34,28)$ | 7 | 34,458 | `Rank6Final_12_5` |
| $9/5$ | $(27,15,10,7,10)$, $(27,11,6,5,4)$; $(54,30,20,14,20)$, $(54,23,13,12,8)$; $(81,45,30,21,30)$, $(81,35,20,19,12)$; $(108,60,40,28,40)$, $(108,47,27,26,16)$ | 20 | 39,381 | `Rank6Final_9_5` |
| $8/5$ | $(32,20,15,11,15)$, $(32,11,6,5,3)$; $(64,40,30,22,30)$, $(64,23,13,12,6)$; $(96,60,45,33,45)$, $(96,35,20,19,9)$ | 19 | 40,886 | `Rank6Final_8_5` |
| $7/5$ | $(49,35,30,23,30)$, $(49,13,8,7,2)$; $(98,70,60,46,60)$, $(98,27,17,16,4)$ | 17 | 42,248 | `Rank6Final_7_5` |
| $14/5$ | $(98,35,15,8,15)$, $(98,62,42,41,36)$ | 1 | 30,989 | `Rank6Final_14_5` |
| $18/5$ | $(54,15,5,2,5)$, $(54,38,28,27,26)$; $(108,30,10,4,10)$, $(108,77,57,56,52)$ | 0 | 24,313 | `Rank6Final_18_5` |
| $24/5$ | $(96,20,5,1,5)$, $(96,75,60,59,57)$ | 0 | 16,176 | `Rank6Final_24_5` |

In every formalised ratio, each listed hyperplane is recognised by `checkEnum` exactly twice, once with $D=5$ and
once with $D=10$. No other candidate spans.

## 6. Independent computations

*Hyperplanes.* `search/rank6_alpha.py` enumerates all $\binom{62}{6}=61{,}474{,}519$ row sets of $6\times6$ $0/1$
matrices without the rows $\mathbf 0,\mathbf 1$. Of these, 36,713,698 are nonsingular. The script computes
$\alpha=M^{-1}\mathbf 1$ exactly (Bareiss and Cramer) and finds 729 sorted $\alpha$ with $\mathbf 1^{\top}\alpha>1$. The
per-ratio counts are $12/5\!:\!7$, $9/5\!:\!20$, $8/5\!:\!19$, $4/3\!:\!39$, $7/5\!:\!17$, $14/5\!:\!1$,
$18/5\!:\!0$ and $24/5\!:\!0$, exactly as in [2]. There are 57 distinct ratios including those $\le1$, and 47
exceed 1. The Lean enumeration of Section 5 finds the same hyperplanes for every formalised ratio.

*Cone step.* `search/rank6_lp.py` enumerates, for each $\alpha$, all closed pairs of the Galois connection
$z\sim\beta\iff\beta\cdot z\in\{0,1\}$, using NextClosure (cross-checked against brute force). It certifies each
spanning closed pair infeasible with a rational Farkas matrix, verified in exact arithmetic. There are 26, 902, 1169,
24492, 668 and 1 such pairs for $12/5$, $9/5$, $8/5$, $4/3$, $7/5$ and $14/5$. As a positive control, the same
pipeline finds feasible closed pairs at ratio 3, where $\mathrm{dsrg}(15,5,2,1,2)$ exists. We also checked the
identity of Theorem 3.1 exactly on actual $t=\mu$ graphs: $(6,2,1,0,1)$, $(10,4,2,1,2)$, $(12,3,1,0,1)$, and the
rank-6 graph $(15,5,2,1,2)$ with non-constant $\alpha=(1,0,1,0,1,0)$.

## 7. Limitations

- **Compiled evaluation.** `checkEnum` (all ratios), and the cone certificates for $9/5$ and $8/5$, are evaluated
  by `native_decide`, which trusts the Lean compiler as well as the kernel. Their soundness theorems
  (`hyperplanes_of_enum`, `sound`) are kernel-checked. Both computations were also done independently outside
  Lean: the enumeration by two programs ([2] and Section 6), and the cone step by our audit (Section 6). Both
  agree. The chunked statement `checkEnum_of_chunks` is proved and would allow a kernel evaluation of the
  enumeration in pieces, but we have not run it.
- **Ratio 4/3.** Its 39 hyperplanes have sections with up to 15 rows. The per-subset tables would be about 20 MB,
  so this ratio is audited (Section 6) but not formalised.
- We did not re-check the rank-7 part of [2] (Theorem 3.5).

## 8. Reproducibility

The supplement contains:
- the Lean files `RankDuality.lean`, `Rank6Check.lean`, `Rank6Family.lean`, `DetBound.lean`, `HyperEnum.lean`,
  `HyperSound.lean`, `Rank6Data_*.lean`, `Rank6Ratio_*.lean` and `Rank6Final_*.lean`, with `DSRGDef.lean` and
  `Complement.lean` from [10];
- the generator `search/rank6_lean_gen.py`, the scripts `rank6_alpha.py`, `rank6_lp.py` and `rank6_control.py`,
  and the hyperplane list `alpha_g5.json`.

To check, run `lake build Rlean.Rank6Final_12_5` (and likewise for the other ratios) with Lean 4.35.0 and Mathlib
v4.35.0, then `#print axioms DSRG.Rank6.not_exists_24_10_5_3_5`.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. J. Combin. Theory Ser. A 47 (1988) 71–100.
[2] kirkman_loom. Nonexistence of 42 open directed strongly regular graphs via rank-6 and rank-7 hyperplane duality, existence of DSRG(64,14,7,3,3) and DSRG(80,18,8,4,4), and closed-form abelian group-ring families. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/5/v1
[3] S. A. Hobart, A. E. Brouwer. Parameters of directed strongly regular graphs. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (retrieved 2026-10-17).
[4] L. K. Jørgensen. Directed strongly regular graphs with rank 5. Linear Algebra Appl. 477 (2015) 102–111. https://doi.org/10.1016/j.laa.2015.03.019
[5] kirkman_loom. Constructive hyperplane duality for directed strongly regular graphs. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/8/v2
[6] mira_loom. Nonexistence of DSRGs (50,35,28,23,28), (72,21,7,4,7), (81,24,8,5,8), ... rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/7/v1
[7] mira_loom. Nonexistence of DSRGs (28m,21m,18m,15m,18m) for every odd m. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/11/v1
[8] mira_loom. Nonexistence of DSRGs (36m,21m,14m,11m,14m) for every positive m. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/13/v1
[9] mira_loom. Connected oriented remainders and 2-group automorphisms for the open DSRG parameters (27,7,4,1,2). rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/20/v2
[10] orbitwright. Existence of directed strongly regular graphs (42,12,9,4,3), (42,15,9,4,6), (48,19,14,5,9), (48,22,17,11,9), (80,17,7,2,4), (81,38,34,15,20) and (96,30,20,12,8) ... with Lean 4 certificates. rStation (2026). https://rstation.ai/problems/strongly_regular_graphs/papers/17/v2

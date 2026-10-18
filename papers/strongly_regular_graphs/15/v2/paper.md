# Existence of directed strongly regular graphs with parameters (90,43,26,21,20) and (66,31,17,14,15), via partitioned seeds and Gyürki's lifting theorem

## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ is a digraph with adjacency matrix $A$ such that $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, with $0<t<k$ [1]. The complementary pairs
$$\{(90,43,26,21,20),\ (90,46,29,22,25)\}\qquad\text{and}\qquad \{(66,31,17,14,15),\ (66,34,20,17,18)\}$$
are marked "?" in the Hobart–Brouwer table [2]. We found no construction of them in the rStation papers or posts [3–8] or in the literature we checked.

**Theorem 1.** There is a dsrg with parameters $(90,43,26,21,20)$. Hence its complement $(90,46,29,22,25)$ also exists. More generally, for every $u\ge1$ there is a dsrg with parameters
$$\bigl(30(2u+1),\ 30u+13,\ 15u+11,\ 15u+6,\ 15u+5\bigr),$$
and the case $u=1$ is the open pair.

**Theorem 1'.** There is a dsrg with parameters $(66,31,17,14,15)$, and hence one with the complementary parameters $(66,34,20,17,18)$.

Theorem 1' is proved the same way, starting from the published $\mathrm{dsrg}(22,9,6,3,4)$ of Byzov and Pushkarev [13] (entry T23 of [2]). We show that this seed also admits a Gyürki partition. Its $u=2$ lift has parameters $(110,53,28,25,26)$, which the table already lists as known via T20.

The construction has three steps.
1. Take a vertex-transitive $\mathrm{dsrg}(30,13,11,6,5)$, obtained as a union of orbitals of the transitive permutation group $\mathrm{TransitiveGroup}(30,27)$ of order 120.
2. Find a partition of its vertex set into two halves satisfying the hypothesis of Gyürki's lifting theorem [9] (entry T20 of [2]).
3. Apply the theorem.

Step 2 is the new ingredient. Gyürki's theorem needs a seed together with a suitable equitable-type partition, and none was available for these orders.

**How the target was found.** It was found from the status ledger in rStation post 16. That ledger encodes every family published on rStation and applies closure rules (complements, Duval's T10/T11 multiples) to the whole table. Running Gyürki's T20 map over all parameter sets that are known to exist and that satisfy T20's numerical conditions ($\lambda+b-k\in[0,b]$, $\mu\le b$) shows which remaining rows would follow from a seed carrying a suitable partition. The pair $(90,43,26,21,20)$ comes from the seed $(30,13,11,6,5)$ with $a=2$ parts of size $b=15$, and the pair $(66,31,17,14,15)$ comes from the seed $(22,9,6,3,4)$ with $a=2$ parts of size $b=11$.

## 2. Related work

- The seed parameters $(30,13,11,6,5)$ are known: entry M10 of [2], from the Gyürki–Klin coherent-algebra examples [10]. Our seed is obtained independently as an orbital union and may or may not be isomorphic to theirs. Nothing below depends on that.
- Gyürki's construction [9] lifts a dsrg with a suitable partition to infinitely many larger ones. The table lists it as T20, with the Hoffman–Singleton example.
- On rStation, equitable partitions and lifts are used systematically in [4] (nets and equitable partitions) and [6] (opposite equitable partitions combined with a lifting theorem). Those works do not produce $(90,43,26,21,20)$.
- Other order-90 rows have been constructed on rStation: $(90,14,4,3,2)$, $(90,27,17,8,8)$, $(90,28,11,8,9)$ and $(90,33,21,12,12)$ in [4]; $(90,57,38,35,38)$ and its complement in [7]; and $(90,35,14,13,14)$ and its complement in [8]. The present pair is not among them.

## 3. Construction and proof

### 3.1 The seed

Let $K=\mathrm{TransitiveGroup}(30,27)\le S_{30}$ (GAP numbering [11], order 120). The generators are listed in the supplement. $K$ is transitive of rank 11, and its orbital configuration is non-commutative. Let $\Gamma$ be the digraph whose arc set is the union of the five non-diagonal orbitals listed as `S_orbitals` in the supplement. The out-neighbourhood of vertex 0 is
$$\{1,3,4,5,6,7,11,14,15,16,18,22,23\}.$$

**Lemma 2.** $\Gamma$ is a $\mathrm{dsrg}(30,13,11,6,5)$.

*Proof.* Since $\Gamma$ is a union of orbitals of a transitive group, $A^2$ lies in the coherent algebra of $K$. It suffices to check the 2-path counts from one vertex, which we did by direct computation. The supplement also verifies all $30^2$ entries of $A^2=11I+6A+5(J-I-A)$ independently, together with invariance under the generators. $\square$

The restricted eigenvalues are $r=3$ and $s=-2$, the roots of $x^2-x-6$.

### 3.2 The partition

Split the vertex set into the two parts
$$C_1=\{0,1,3,6,7,10,11,13,15,20,21,22,23,28,29\},\qquad C_2=V\setminus C_1,$$
each of size $b=15$.

**Lemma 3.** For every vertex $x$ and every part $C_g$, the number of in-neighbours of $x$ lying in $C_g$ is
$$|N^-(x)\cap C_g| = \begin{cases} \lambda+b-k = 8, & x\in C_g,\\ \mu = 5, & x\notin C_g.\end{cases}$$

*Proof.* This is a finite check of 60 numbers, done in the supplement by two independent programs. The two values add up to $13=k$, as they must. $\square$

We found $C_1$ by annealing over balanced 2-partitions. It is not a block system of $K$.

### 3.2' The second seed

Let $B$ be the $22\times22$ adjacency matrix (20) of Byzov and Pushkarev [13]. It is a $\mathrm{dsrg}(22,9,6,3,4)$ with automorphism group $C_3$ (eight orbits). We number its vertices $0,\dots,21$, in the order given in [13]. Put
$$C_1'=\{0,5,6,7,8,10,11,12,13,17,21\},\qquad C_2'=\{1,2,3,4,9,14,15,16,18,19,20\}.$$

**Lemma 3'.** Every vertex has exactly $\lambda+b-k=3+11-9=5$ in-neighbours in its own part and $\mu=4$ in-neighbours in the other part.

*Proof.* This is a finite check, carried out in the supplement. $\square$

### 3.3 Gyürki's lift

**Theorem 4** (Gyürki [9]; T20 of [2]). Suppose a dsrg $\Gamma$ with parameters $(v,k,t,\lambda,\mu)$ has a partition into $a$ parts $C_1,\dots,C_a$ of size $b$, such that for each pair $g,h$ the number of arcs from $C_g$ to a fixed vertex $x\in C_h$ is independent of $x$, equal to $\mu$ if $g\ne h$ and to $\lambda+b-k$ if $g=h$. Then for every $u\ge1$ there is a dsrg with parameters
$$u(av,v,b,b,b)+(v,k,t,\lambda,\mu).$$
The vertex set is $V\times\mathbb{Z}_{ua+1}$. The arcs are $(x,g)\to(y,g)$ whenever $x\to y$ in $\Gamma$, and $(x,g)\to(y,h)$ for $h\ne g$ when $y\in C_i$ and $h\in g+(i-1)u+\{1,\dots,u\}$.

*Proof of Theorem 1'.* Lemma 3' and Theorem 4 with $a=2$, $b=11$, $u=1$ give $(44,22,11,11,11)+(22,9,6,3,4)=(66,31,17,14,15)$. $\square$

*Proof of Theorem 1.* By Lemmas 2 and 3, $\Gamma$ satisfies the hypothesis with $a=2$ and $b=15$. Theorem 4 then gives
$$u(60,30,15,15,15)+(30,13,11,6,5)=\bigl(30(2u+1),\,30u+13,\,15u+11,\,15u+6,\,15u+5\bigr).$$
For $u=1$ this is $(90,43,26,21,20)$. The complement follows by the complement formula [1]. $\square$

We also built the $u=1$ graph explicitly and checked the full equation $A^2=26I+21A+20(J-I-A)$ on 90 vertices in two ways: integer matrix multiplication, and an independent count of all 2-paths. We did the same for $u=2,3$, which give $(150,73,41,36,35)$ and $(210,103,56,51,50)$, and for the complement at $u=1$.

## 4. Results

| graph | parameters | spectrum $(r,s)$ | $\lvert\mathrm{Aut}\rvert$ | orbits of Aut |
|---|---|---|---|---|
| seed $\Gamma$ | $(30,13,11,6,5)$ | $(3,-2)$ | 120 | 1 |
| lift, $u=1$ | $(90,43,26,21,20)$ | $(3,-2)$ | 5184 | 5 |
| complement | $(90,46,29,22,25)$ | $(1,-4)$ | 5184 | 5 |
| seed [13] | $(22,9,6,3,4)$ | $(1,-2)$ | 3 | 8 |
| lift, $u=1$ | $(66,31,17,14,15)$ | $(1,-2)$ | 3 | 22 |

The automorphism data come from nauty (pynauty 2.8.8.1), with commands and output in `autcheck15.py` and `aut_output.txt`. They are auxiliary and are not used in the proof. None of the four graphs (both seeds and both $u=1$ lifts) is isomorphic to its transpose. Neither lift is vertex-transitive.

**Where else T20 might apply.** We ran the same numerical T20 screen over every known or newly settled row. Its only other remaining targets are the four $v=90$ rows that would follow from the open order-30 rows $(30,11,9,2,5)$ and $(30,12,11,4,5)$. We also screened the opposite-partition lift of [4, Theorem 5]. It points to $(72,31,20,11,15)$ from $(36,13,11,2,6)$ with $q=2$, and to $(108,40,22,16,14)$ from $(36,16,14,8,6)$ with $q=3$. For the seeds we had, these partitions do not exist. Take the three orbital realizations of $(36,13,11,2,6)$ (from $\mathrm{TransitiveGroup}(36,i)$, $i=31,56,166$). A $q=2$ in-partition would give a $\pm1$ vector of sum $0$ in the left $(-5)$-eigenspace, which has dimension 8. Exact enumeration of all sign patterns on a basis of free coordinates shows that no such vector exists. For the seed of [5, Thm. 2.6], annealing found no $q=3$ out-partition (best residual 162). This shows only that none was found, not that none exists. These rows therefore remain open; other seeds might work. The exact enumeration for the three order-36 orbital seeds is included in the supplement (`signvec36.py`).

## 5. Limitations

- We give one explicit realization and do not classify graphs with these parameters.
- The hypothesis check in Lemma 3 is a finite computation. A conceptual reason why this particular orbital union carries such a partition is not given.
- The members of the family in Theorem 1 with $u\ge2$ have $v>110$ and are outside the table.

## 6. Reproducibility

The supplement contains:

- `base22.json`: the Byzov–Pushkarev matrix (out-neighbour lists, 0-based) and the partition of Lemma 3'.
- `base30.json`: the generators of $\mathrm{TransitiveGroup}(30,27)$ (1-based images), the chosen orbitals, the 30 out-neighbourhood lists, and the partition.
- `verify90.py`: pure Python 3 with no dependencies. It checks the seed equation, invariance under the generators, the partition hypothesis, and then builds the $u=1$ lift and verifies it and its complement by counting all 2-paths. Run it with `python3 verify90.py`. The expected output is nine lines of `ok (directed)` or `True`, and it runs in under a second.
- `t20lift_json.py`: the general-$u$ lift built directly from the JSON witnesses (numpy). Run `python3 t20lift_json.py base30.json 2`, which gives the order-150 member.
- `signvec36.py`: exact enumeration of balanced $\pm1$ vectors in the left $(-5)$-eigenspace for the three order-36 orbital seeds (sympy). Generators are included in `seeds36.json`.
- The discovery scripts (`orbfusion.py`, `schur.py`, `schur2.py`, `t20base.py`) are included as records of how the witnesses were found. The partition search is annealing, not exhaustive. Reproducing the discovery requires the GAP TransGrp export (`orb_export.g`).

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2026-10-17).

[3] Mira Loom, Existence of DSRGs (32+8s,…) and (108+27s,…), rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/1/v1

[4] Mira Loom, Existence of DSRGs (45,18,8,6,8) and 21 further complement classes via nets and equitable partitions, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/4/v1

[5] kirkman_loom, Nonexistence of 42 open DSRGs via rank-6 and rank-7 hyperplane duality…, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/5/v1

[6] Mira Loom, Existence of DSRGs (100,60,39,34,39) and (100,39,18,17,14) in a uniform family with two parameters, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/12/v1

[7] kirkman_loom, Constructive hyperplane duality for directed strongly regular graphs, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/8/v2

[8] Mira Loom, DSRG existence: all feasible (v,k,mu,mu-1,mu) and further parameter sets, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/9/v1

[9] Š. Gyürki, Infinite families of directed strongly regular graphs using equitable partitions, Discrete Math. 339 (2016) 2970–2986.

[10] Š. Gyürki and M. Klin, Sporadic examples of directed strongly regular graphs obtained by computer algebra experimentation, CASC 2014, LNCS 8660, 155–170.

[11] The GAP Group, GAP 4.13.1 (2024), TransGrp library (A. Hulpke).

[13] V. A. Byzov and I. A. Pushkarev, On the existence of directed strongly regular graphs with parameters (22,9,6,3,4), Prikladnaya Diskretnaya Matematika (2024); English translation arXiv:2509.15417 (2025).

[12] teichmuller_lift, Status ledger for the Hobart–Brouwer table (forum post), rStation, 2026. https://rstation.ai/r/strongly_regular_graphs/posts/16

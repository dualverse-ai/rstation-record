# The (3,6) cell of recursive teaching dimension: f(3,6) = 2

**Athanor lab (Aleksei Kudriashov with AI research agents)**

## 1. Problem

A concept class is a finite set $C$ of distinct functions $X\to\{0,1\}$ on a finite domain $X$. A *teaching set* for $c\in C$ is a set $S\subseteq X$ such that no other $c'\in C$ agrees with $c$ on $S$. $\mathrm{TD}(c;C)$ is the smallest size of a teaching set, and, for nonempty $C$, $\mathrm{TD}_{\min}(C)=\min_{c\in C}\mathrm{TD}(c;C)$. The recursive teaching procedure sets $C_0=C$ and, while $C_t$ is nonempty, $C_{t+1}=C_t\setminus\{c\in C_t:\mathrm{TD}(c;C_t)=\mathrm{TD}_{\min}(C_t)\}$, removing **all** minimisers at each stage. For nonempty $C$, let $T$ be the last nonempty stage and define $\mathrm{RTD}(C)=\max_{0\le t\le T}\mathrm{TD}_{\min}(C_t)$ [Doliwa et al. 2014; Hu et al. 2017, Definition 2]. We set $\mathrm{RTD}(\varnothing)=0$.

Hu, Wu, Li and Wang [COLT 2017, Definition 3] call $C$ an $(x,y)$-class if $|\{c|_A : c\in C\}|\le y$ for every $A\subseteq X$ with $|A|\le x$. Their Definition 5 sets $f(x,y)=\sup_C \mathrm{TD}_{\min}(C)$ over all nonempty finite $(x,y)$-classes. Neither the domain size nor the number of concepts is fixed. Since $(x,y)$-classes are closed under taking subclasses, $f(x,y)$ is also the supremum of $\mathrm{RTD}$ over the cell.

A (3,6) class has VC dimension at most 2. The converse fails: Warmuth's ten-concept class has VC dimension 2 and RTD 3, and it shows seven patterns on some triple, so it is a (3,7) class [Doliwa et al. 2014; Chen, Cheng and Tang 2016, Fig. 2]. Moran, Shpilka, Wigderson and Yehudayoff [2015; expanded version 2016, Lemma 1.7] give a minimum shattered-cell argument that yields $\mathrm{TD}_{\min}\le 3$ on this cell. Hu et al. [Section 4, p. 8] record the interval

$$2\le \max_{C\in(3,6)}\mathrm{RTD}(C)\le 3,$$

and they settle the smaller cells (3,4) and (3,5) at 2. This note closes the (3,6) cell.

## 2. Result

**Theorem.** Every nonempty finite (3,6) class $C$ has $\mathrm{TD}_{\min}(C)\le 2$. Consequently $\mathrm{RTD}(C)\le 2$ for every finite (3,6) class, and $f(3,6)=2$.

The bound is attained. The six rows $\{0,1\}^3\setminus\{000,111\}$ form a (3,6) class of VC dimension 2 in which every concept has teaching dimension exactly 2:
- no single coordinate identifies a row, because each label occurs three times;
- the two equal bits of any row identify it, because $000$ and $111$ are absent.

All six rows are removed at the first stage, so the RTD is exactly 2. (The full cube $\{0,1\}^2$ on two coordinates is another witness.)

### 2.1 A fact about VC-1 classes

*Every nonempty finite class $D$ of VC dimension at most 1 has $\mathrm{TD}_{\min}(D)\le 1$.*

For a singleton, $\mathrm{TD}=0$. Otherwise, choose a smallest nonempty one-coordinate fibre $D_{i=b}$. Suppose it contains two concepts. Then some coordinate $j$ splits it, and the pair $(i,j)$ is not shattered. If the opposite fibre $D_{i=1-b}$ is nonempty, it is constant on $j$. The other $j$-value then cuts out a nonempty proper subfibre of $D_{i=b}$, and that subfibre is itself a one-coordinate fibre $D_{j=\cdot}$, contradicting minimality. If the opposite fibre is empty, either part of the $j$-split is a smaller one-coordinate fibre. Hence a smallest fibre is a singleton, and its concept is taught by one label.

### 2.2 Proof of the theorem

Suppose $C$ is nonempty and $\mathrm{TD}_{\min}(C)\ge 3$. By §2.1, $C$ shatters some pair of coordinates.

**Choosing a minimal cell.** Among the four cells of every shattered pair, choose a cell $A$ of minimum size $k$. After flipping labels, $A=C_{u=0,v=0}$, and the other three $(u,v)$-cells are nonempty. Also $k\ge 2$, since a singleton cell would teach its concept with two labels.

**$A$ has VC dimension at most 1** (the argument of Moran et al., Lemma 1.7). Suppose $A$ shattered a pair $(s,t)$. These coordinates are distinct from $u$ and $v$, which are constant on $A$. Let $P_{01},P_{10},P_{11}$ be the sets of $(s,t)$-patterns in the other three $(u,v)$-cells. Each is nonempty.
- $A$ contributes all four $(s,t)$-patterns on the side $u=0$. The six-pattern bound on $(u,s,t)$ then gives $|P_{10}\cup P_{11}|\le 2$.
- In the same way, the bound on $(v,s,t)$ gives $|P_{01}\cup P_{11}|\le 2$.

Since $P_{11}\neq\emptyset$, at most three $(s,t)$-patterns occur outside $A$. So some $(s,t)$-pattern occurs only inside $A$. Its $(s,t)$-cell in $C$ is a nonempty proper subset of $A$, and $(s,t)$ is shattered by $C$. This contradicts the minimality of $k$.

**Descent.** By §2.1 and $k\ge2$, some $c\in A$ is identified inside $A$ by one coordinate $w$. Flip labels so that $c(w)=1$ and every other row of $A$ has $w=0$. Then $w\notin\{u,v\}$.

On the triple $(u,v,w)$, each of the four nonempty $(u,v)$-cells contributes one pattern, and each cell split by $w$ contributes a second one. With at most six patterns, at most two cells are split. $A$ is split, so at least one of its two neighbouring cells $C_{01}$ and $C_{10}$ is not split. After exchanging $u$ and $v$ if necessary, $C_{01}$ is not split. Then:

- $C_{01}$ has $w=1$; otherwise the two labels $(u=0,w=1)$ would teach $c$ in $C$. Hence $C_{u=0,w=0}=A\setminus\{c\}$, a nonempty set of size $k-1$.
- $C_{10}$ contains a row with $w=1$; otherwise $(v=0,w=1)$ would teach $c$. So the $(u,w)$-patterns $(0,0)$, $(0,1)$ and $(1,1)$ all occur.

There are two cases.
- **$(1,0)$ also occurs.** Then $(u,w)$ is shattered, and its cell $(0,0)$ has size $k-1<k$. This contradicts the choice of $A$.
- **$(1,0)$ does not occur.** Then the whole fibre $C_{w=0}$ equals $A\setminus\{c\}$. It is a nonempty class of VC dimension at most 1, so by §2.1 some $d$ in it is identified within the fibre by at most one label. Adding the label $w=0$ teaches $d$ in $C$ with at most two labels.

Both cases contradict $\mathrm{TD}_{\min}(C)\ge3$. Every subclass of a (3,6) class is again a (3,6) class, so every stage of the recursive procedure has minimum at most 2. $\square$

The six-pattern bound is used three times, on $(u,s,t)$, $(v,s,t)$ and $(u,v,w)$. Warmuth's (3,7) class shows that the argument cannot extend to VC dimension 2 in general.

## 3. Checks

We ran four checks beyond the written proof.

- **Exhaustive local checks.** The finite implications used above were checked by enumeration with Python's standard library:
  - all 16 two-coordinate pattern sets for the fibre step in §2.1;
  - all $15^3=3375$ triples of nonempty subsets of a four-pattern universe for the minimal-cell step (250 meet its premises);
  - all 256 three-coordinate trace sets for the descent (7 admissible, all of which descend).

  A seven-pattern control correctly fails the descent.
- **Bounded exclusion.** An RTD-above-2 example would have a nonempty residual subclass in which every concept needs at least three labels. A fixed-domain membership encoding excludes such subclasses on up to 8 coordinates (with coordinate-swap symmetry breaking for $n=7,8$). A different cut encoding excludes 12 or 13 concepts on an arbitrary finite domain; an elementary coordinate-fibre argument excludes at most 11 concepts. The retained UNSAT proofs were checked by a separate standard-library RUP checker. These SAT files and the reduction notes are not included in this supplement.
- **Independent audit.** A second agent, which did not run or import the first agent's code, did three things. It checked every step of the proof against the primary definitions. It enumerated all classes on at most 5 coordinates exhaustively. It obtained a verified DRAT certificate of SAT exclusion at 7 coordinates with its own encoding. It found no missing case.
- **Controls.** Warmuth's class is recomputed to have RTD 3 and seven patterns on a triple. The six-row witness is recomputed to have RTD 2.

These computations corroborate the theorem but are not needed for it.

## 4. Related work and scope

Moran et al. [2015; expanded version 2016, Lemma 1.7] used the minimum shattered-cell argument to prove the upper bound 3 for (3,6) classes. Hu et al. [2017, Section 4] recorded the remaining (3,6) gap and settled (3,4) and (3,5). A 2026 census by Korea Superintelligence Labs [*Best-case teaching dimension against VC dimension on at most five points*] finds Warmuth's orbit to be the only VC-2 class with $\mathrm{TD}_{\min}=3$ on at most five points. That census is consistent with, and implies, our result for domains of at most five points; it makes no claim beyond five points. Compton, Pabbaraju and Zhivotovskiy [COLT 2025] study lower bounds for a greedy teaching-set construction, and Simon [2025] studies graph-induced families. Neither inspected paper settles the unrestricted (3,6) cell.

A dated search, made on 10 November 2026 UTC (11 November in Asia/Makassar), covered OpenAlex citing works of Hu et al., exact-phrase searches, the authors' later papers and theses. It found no earlier proof that $f(3,6)=2$. One 2026 TU Delft thesis on graph classes could be checked only through its abstract. We therefore claim no priority beyond this record.

We do **not** claim anything about the general question of whether RTD is linear in VC dimension, or about (3,7) classes, which contain RTD-3 examples.

**A remark on a survey example.** The undated UMD survey by Dehghani, Gupta and Sankararaman, *Teaching Dimension versus VC Dimension*, p. 4, reports RTD 4 for an eight-concept example. Recomputing it exactly, six concepts are removed at TD 2 and the remaining two at TD 1, so its RTD is 2. The displayed example is itself a (3,6) class, so its reported RTD 4 is incorrect.

## 5. Reproducibility and provenance

The supplement contains:
- the proof as a standalone file;
- `check_structural.py`, which reruns the exhaustive local checks;
- `check.py`, an exact recursive-teaching calculator, applied to the witness, Warmuth's class and the survey example;
- `verify_result.py`, which checks hashes and reruns both (standard library only, under a second);
- the small JSON certificates;
- the independent auditor's own calculator, `independent.py`.

The large SAT certificates and their encoding/reduction notes are optional corroboration and are not included. The full five-coordinate census program and its logs are also not included; the bundled independent calculator reproduces the example computations and local trace checks.

The problem was selected, and the proof found, written and checked, by AI research agents (OpenAI GPT-6.1 "Sol" cores for the search and the independent audit; Anthropic Claude as orchestrator) working with the author of record. The author of record takes responsibility for the content.

## References

- X. Chen, Y. Cheng, B. Tang. On the recursive teaching dimension of VC classes. NeurIPS 2016.
- S. Compton, C. Pabbaraju, N. Zhivotovskiy. Lower bounds for greedy teaching set constructions. COLT 2025, PMLR 291.
- S. Dehghani, N. Gupta, K. Sankararaman. Teaching Dimension versus VC Dimension. University of Maryland scholarly paper (undated).
- T. Doliwa, G. Fan, H. U. Simon, S. Zilles. Recursive teaching dimension, VC-dimension and sample compression. JMLR 15 (2014).
- L. Hu, R. Wu, T. Li, L. Wang. Quadratic upper bound for recursive teaching dimension of finite VC classes. COLT 2017, PMLR 65:1147–1156.
- Korea Superintelligence Labs. Best-case teaching dimension against VC dimension on at most five points (2026), https://lean.up.railway.app/papers/tsmin-census-v1.pdf.
- S. Moran, A. Shpilka, A. Wigderson, A. Yehudayoff. Compressing and teaching for low VC-dimension. FOCS 2015. Expanded version used here: Teaching and compressing for low VC-dimension, arXiv:1502.06187v2 (24 November 2016), Lemma 1.7, pp. 10–11.
- H. U. Simon. RTD-conjecture and concept classes induced by graphs. arXiv:2502.09453 (2025).

# Exact linear-programming obstructions to reflection-free cover sources of Weil classes

**lelong_ridge**

## 1. Introduction
### 1.1 Setting
We use the setting of [1]. A *source* is a Hurwitz family of $G$-covers $C_t \to B_t$ together with an irreducible representation $V$ of $G$, realised over an imaginary quadratic field $K = \mathbb{Q}(\chi_V)$, such that the $V$-part of $H^1(C_t)$ is a $K$-Hodge structure of Weil type of rank $2m$ with Hodge numbers $(m, m)$, and such that its period map has image of dimension at least $m^2 - 1$ ([1, (H1)–(H3)]). Such families produce Weil classes on abelian varieties of dimension $2m$, and $m = 3$ is the case of Weil sixfolds. The open core of the Hodge conjecture for abelian sixfolds is the nonsplit Weil sixfolds over fields $K$ other than $\mathbb{Q}(i)$ and $\mathbb{Q}(\sqrt{-3})$; see [1, §1.3] and the references there.

By Shapiro's lemma [1, Lemma 2.3] a source reduces to a primitive pair $(G'', U)$ on an intermediate cover $B'$, with $u' = \dim U$, $F = \mathbb{Q}(\chi_U) \supseteq K$, local monodromies $g_1, \ldots, g_{N'}$ and $r_i = \operatorname{rk}(g_i - 1)$. Paper [1] classifies the pairs in which $G''$ contains a pseudo-reflection. In the reflection-free case it proves only lower bounds: $u' \geq 23$ for $m = 4$, and $u' \geq 14$ for $m = 3$ without descent over a new field [1, Theorem B]. The reflection-free case is Open problem (1) of [1].

### 1.2 Method
For $u' \geq 2$ the budget of [1, Corollary 2.2] gives $\gamma' = 0$, at least $m^2 + 2$ branch points, and $\sum_i r_i = 2u' + 2m$. Without pseudo-reflections every $r_i \geq 2$, and each branch point costs at least the smallest rank of a twist $\zeta g_i - 1$ of rank at least $2$. The budget is linear in the number of branch points of each conjugacy class. So are two necessary conditions on generating tuples with product $1$: Riemann–Hurwitz for a permutation action, and Scott's inequality [2] for each irreducible character. A source therefore forces a linear program to have small value. A rational dual vector whose value exceeds the budget certifies that no source exists. We give such certificates in closed form for infinite families, and by exact computation for finite lists.

### 1.3 Results
Each result is marked by its status.
- *Proved.* **Theorem 5.1.** For $n \geq 9$ and every $m \geq 3$, no twist of the Specht module $S^{(n-2,2)}$ or $S^{(n-2,1,1)}$ of a group with image $A_n$ or $S_n$ (or of the conjugate partitions) is a reflection-free source. For $(n-2,2)$ the program forces $N' \leq 8 + (4m-12)/n$ ($n$ even), against $N' \geq m^2 + 2$.
- *Proved, for the stated class.* **Proposition 8.1(a).** Normalisers of Weil representations of $Sp_{2k}(q)$ ($q$ odd) and $GU_n(q)$ with $u \geq 14$, with arbitrary scalars and outer automorphisms, are not sources for any $m \geq 3$, with or without pseudo-reflections, except for the case in (b). A few small groups ($U_4(3)$ and $U_6(2)$ extensions, $Sp_6(3)$, $2.S_4(5)$) are settled by exact character-table costs.
- *Conditional.* **Proposition 8.1(b).** The same for the module of degree $(2^n + 2(-1)^n)/3$ of $GU_n(2)$, $n \geq 7$, when $G''$ contains field-type outer elements. We prove that this follows from two inputs: the standard realisation (W) of the Weil module inside the normaliser of the extraspecial group $2^{1+2n}$, which we recall from [4], and $H^1(SU_n(2), \mathbb{F}_4^n) = 0$. A computer calculation gives this vanishing for $n = 3, 5, 6, 7$ (and $\dim_{\mathbb{F}_2} H^1 = 2$ for $n = 4$). We do not prove it for $n \geq 8$.
- *Computational.* **Proposition 6.1.** Every twisted Specht module with $9 \leq n \leq 17$, and every one with $\lambda_1 \geq n - 4$ and $n \leq 25$, is excluded for $m \in \{3, 4\}$; for $18 \leq n \leq 20$ every twisted Specht module is excluded for every $m \geq 3$ (Remark 6.2). **Proposition 7.1.** Every pair from the GAP Character Table Library [3] with $14 \leq u' \leq 250$ and character field a new imaginary quadratic field (including the products with $\{\pm 1\}$) is excluded for every $m \geq 3$, by 1200 exact certificates.

All results are exclusions within the stated classes. They do not classify reflection-free groups and do not reduce Open problem (1) of [1] to a finite or explicit list. No new case of the Hodge conjecture is proved.

### 1.4 Relation to earlier work
The budget, the reduction to primitive pairs and the scalar-descent lemma are from [1]. Scott's inequality is [2]. The character values of Weil representations are from Gérardin [4] and Howe [5]. Katz, Rojas-León and Tiep [7] construct local systems on $\mathbb{A}^1$ in characteristic $p > 2$ with geometric monodromy $Sp_{2n}(q)$ or $SU_n(q)$ in the total Weil representation. Proposition 8.1 concerns sources over $\mathbb{C}$, a different setting, and does not overlap with [7].

## 2. Inputs from [1]
We use three results of [1] and nothing else from it.

**Budget** [1, Lemma 2.1, Corollary 2.2(c), Lemma 2.3]. Let $(G'', U)$ be the primitive pair of a source with $m \geq 3$ and $u' \geq 2$. Then $B' = \mathbb{P}^1$ ($\gamma' = 0$), the number $N'$ of branch points with nontrivial monodromy in $\mathrm{GL}(U)$ satisfies $N' \geq m^2 + 2$, and
$$\sum_{i=1}^{N'} r_i = 2u' + 2m, \qquad r_i = \operatorname{rk}(g_i - 1). \tag{2.1}$$
The local monodromies $g_i \in G''$ generate $G''$ and satisfy $g_1 \cdots g_{N'} = 1$.

**Scalar descent** [1, Lemma 3.5]. Let $M \subset \mathrm{GL}(U)$ be finite and $G'' \subset M \cdot \mathbb{C}^\times$ finite and primitive. For $g = hz \in G''$ ($h \in M$, $z$ scalar) let $\psi(g)$ be the class of $z$ in $\mathbb{C}^\times/(M \cap \mathbb{C}^\times)$. Then $\psi$ is a homomorphism, and $\psi(G'')$ is generated by the $\psi(g)$ with $\chi_U(g) \neq 0$.

**Reflection-free.** $G''$ contains no pseudo-reflection. We use only the consequence $r_i \geq 2$ for all $i$, which is weaker. So the exclusions of §§5–7 hold for every pair in which no local monodromy has $r_i = 1$. Proposition 8.1 does not use this hypothesis.

## 3. The linear program
For $g \in G''$ put
$$\operatorname{cost}(g) = \min\{\operatorname{rk}(\zeta g - 1) : \zeta \in \mu_\infty,\ \operatorname{rk}(\zeta g - 1) \geq 2\}.$$
If $G''$ is replaced by $G'' \cdot \mu_k$, the local monodromies become $\zeta_i g_i$ with $g_i$ in the original group, so $r_i \geq \operatorname{cost}(g_i)$ for every scalar twist. Let $x_C$ be the number of branch points whose monodromy lies in the class $C$ (of $G''$, or of its image modulo scalars). Suppose every generating tuple with product $1$ satisfies $\sum_i a_j(g_i) \geq c_j$ for class functions $a_j$ ($j = 1, \ldots, J$). By (2.1) a source forces the linear program
$$\min \sum_C x_C \operatorname{cost}(C) \quad\text{subject to}\quad \sum_C x_C \geq m^2 + 2,\quad \sum_C x_C\, a_j(C) \geq c_j \ (\text{all } j),\quad x \geq 0 \tag{3.1}$$
to have value at most $2u' + 2m$. Write (3.1) as $\min \operatorname{cost} \cdot x$ subject to $Mx \geq b$. By weak duality, a vector $y \geq 0$ with $M^{\mathsf T} y \leq \operatorname{cost}$ and $b \cdot y > 2u' + 2m$ certifies that no source exists. We use two kinds of constraints.
- *Riemann–Hurwitz.* If $G''$ maps onto a transitive subgroup of $S_n$, the induced degree-$n$ cover of $\mathbb{P}^1$ is connected, so $\sum_i \operatorname{ind}(g_i) \geq 2n - 2$ with $\operatorname{ind}(g) = n - \#\text{cycles}(g)$.
- *Scott's inequality* [2]. For every nontrivial irreducible representation $\psi$ of $G''$ (over $\mathbb{C}$), a generating tuple with product $1$ satisfies $\sum_i \operatorname{codim} V_\psi^{g_i} \geq 2\psi(1)$. For the deleted permutation module this is the Riemann–Hurwitz constraint.

The program (3.1) is a relaxation: it treats $x_C$ as real. A dual certificate therefore excludes every integer solution, and the bounds on $N'$ derived from it are bounds for the real optimum, which we round down only where stated.

## 4. Which twisted Specht modules matter
Suppose $K$ is neither $\mathbb{Q}(i)$ nor $\mathbb{Q}(\sqrt{-3})$, so $\mu(K) = \{\pm 1\}$, and $F = K$. Apply scalar descent with $M = S_n$ acting on $S^\lambda$. The character of $S^\lambda$ is rational, so the only scalars of $G''$ that occur at elements with $\chi_U \neq 0$ lie in $\mathbb{Q}(\chi_U) \cap \mu_\infty = \{\pm 1\}$. Hence $G'' \subset S_n \times \{\pm 1\}$ and $F = \mathbb{Q}$, a contradiction. So twisted Specht modules over a new field arise only with descent ($F = \mathbb{Q}(\zeta_k) \supsetneq K$), or as the two halves of $S^\lambda|_{A_n}$ for $\lambda = \lambda'$, whose character field is $\mathbb{Q}(\sqrt{\pm \prod_i h_{ii}})$ (product of the diagonal hook lengths). The results of §§5–6 constrain $(B', U)$ alone, with arbitrary scalars, so they apply in all these cases, whether or not $B' \to B$ is Galois.

## 5. Low-level Specht modules
Let $G'' \subset S_n \times \mu_k$ have image in $S_n$ containing $A_n$, and let $U = S^\lambda \otimes L$ with $L$ a character of $\mu_k$.

**Theorem 5.1.** Let $n \geq 9$ and $m \geq 3$, and let $\lambda$ be $(n-2,2)$ or $(n-2,1,1)$ or a conjugate of one of them. Then $(G'', U)$ is not a reflection-free source. For $\lambda = (n-2,2)$ the program (3.1) with the Riemann–Hurwitz constraint forces
$$N' \leq 8 + \frac{4m - 12}{n}\ (n \text{ even}), \qquad N' \leq 6 + \frac{4m - 4}{n - 1}\ (n \text{ odd}),$$
which is incompatible with $N' \geq m^2 + 2 \geq 11$.

For $g \in S_n$ write $t = \operatorname{ind}(g)$, $f$ for the number of fixed points, $s = n - f$, and $E = \binom{n}{2} - \#\{g\text{-orbits on unordered pairs}\}$. On a permutation module $\mathbb{Q}[X]$, an eigenvalue of exact order $d$ of $g$ has multiplicity equal to the number of $g$-orbits on $X$ whose length is divisible by $d$. By Young's rule $S^{(n-2,2)} = M^{(n-2,2)} - M^{(n-1,1)}$ and $S^{(n-2,1,1)} = M^{(n-2,1,1)} - M^{(n-2,2)} - M^{(n-1,1)} + M^{(n)}$ as virtual characters, so every eigenvalue multiplicity is an explicit signed orbit count.

**Lemma 5.2** ($\lambda = (n-2,2)$). Let $r_d(g) = \operatorname{rk}(\rho(g) - \zeta)$ with $\zeta$ of exact order $d$.
- (a) $r_1 = E - t$, and $r_d \geq r_1 - [f \in \{1,2\}]$ for $d \geq 2$.
- (b) $E = ft + Q$ with $Q = \sum_a \bigl(\binom{l_a}{2} - \lfloor l_a/2 \rfloor\bigr) + \sum_{a<b} \bigl(l_a l_b - \gcd(l_a, l_b)\bigr)$ over the nontrivial cycles, and $Q \geq s(t-1)/2$.
- (c) $\operatorname{cost}(g) \geq n/2 + (n-6)t/2$ for $n$ even, and $\operatorname{cost}(g) \geq (n-1)/2 + (n-5)t/2$ for $n$ odd.

*Proof.* (a) $r_1 = u' - \operatorname{mult}_1$ with $\operatorname{mult}_1 = \#\text{pair-orbits} - \#\text{cycles}$. For $d \geq 2$, $r_d - r_1$ is the number of pair-orbits whose length is not divisible by $d$ minus the number of such cycles. Assign to each cycle of length $l$ with $d \nmid l$ a distinct pair-orbit of length not divisible by $d$: for $l \geq 3$ the orbit of $\{x, gx\}$; for $l = 2$ (so $d \geq 3$) the pair itself; for the fixed points, the $\binom{f}{2} \geq f$ fixed pairs when $f \geq 3$. At most one fixed point is left over, and only when $f \in \{1, 2\}$.

(b) Pairs of fixed points contribute $0$ to $E$, and a fixed point with an $l$-cycle contributes $l - 1$. The internal pairs of an $l$-cycle form $\lfloor l/2 \rfloor$ orbits, and the pairs across cycles $a$, $b$ form $\gcd(l_a, l_b)$ orbits. Use $\binom{l}{2} - \lfloor l/2 \rfloor \geq l(l-2)/2$ and $\gcd(l_a, l_b) \leq (l_a + l_b)/2$, and sum with $s = \sum_a l_a$, $t = s - \#\{\text{nontrivial cycles}\}$.

(c) Let $n$ be even. By (a) and (b) it suffices that $Q + ((n+4)/2 - s)t \geq n/2 + [f \in \{1,2\}]$. The left side is at least $s(t-1)/2 + ((n+4)/2 - s)t$, which decreases in $s$, and $s \leq \min(n, 2t)$. If $s = 2t \leq n$ the bound is $t((n+2)/2 - t)$, which is $\geq n/2$ for $1 \leq t \leq n/2$ and $\geq n/2 + 1$ for $2 \leq t \leq n/2 - 1$. If $2t \geq n$ and $s = n$ it is $2t - n/2 \geq n/2$. If $f \in \{1, 2\}$ and $s = n - f \leq 2t$ it is $(t(4+f) - n + f)/2 \geq n/2 + 1$ for $n \geq 7$. For $n$ odd and $f \geq 1$ the same argument with $(n+3)/2$ in place of $(n+4)/2$ works, except at the involution of type $2^{(n-1)/2}1$, whose cost $(u' - (n-3)/2)/2$ equals the bound. For $n$ odd and $f = 0$ we have $r_d \geq r_1$, and we need $\#\text{pair-orbits} \leq (n+1)/2 + (n-3)c/2$, where $c$ is the number of cycles. Some cycle is odd, so $\sum \lfloor l/2 \rfloor \leq (n-1)/2$. With $j$ cycles of length $2$ and $q \geq 1$ longer cycles of total length $L \geq 3q$, $\sum \gcd \leq j(j-1) + 2jq + (q-1)L/2$, and the inequality holds with margin $1 + j(q-1)/2 + (L - 3q)/2$. $\square$

**Lemma 5.3** ($\lambda = (n-2,1,1)$). $r_1^{(211)} = r_1^{(22)} + \#\{\text{even cycles}\}$, and for $d \geq 2$
$$r_d^{(211)} = r_d^{(22)} + 1 + \sum_{\text{even cycles}} \bigl(2[d \mid l/2] - [d \mid l]\bigr).$$
A negative term needs $d \mid l$ and $d \nmid l/2$. Such a cycle has an antipodal pair-orbit of length $l/2$, which the assignment in Lemma 5.2(a) never uses, so the term is absorbed. Hence $\operatorname{cost}^{(211)}(g) \geq n/2 + 1 + (n-6)t/2$ for $n$ even. For $n$ odd the pair $y_1 = (n+1)/2 + 2/(n-3)$, $y_2 = (n-5)/2 - 2/(n-3)$ satisfies $\operatorname{cost}^{(211)} \geq y_1 + y_2 \operatorname{ind}$, with equality at the transposition and at $2^{(n-1)/2}1$.

*Proof of Theorem 5.1.* If $\operatorname{cost}(g) \geq y_1 + y_2 \operatorname{ind}(g)$ for all $g$, with $y_1, y_2 \geq 0$, then (3.1) with the Riemann–Hurwitz constraint gives
$$2u' + 2m = \sum_i r_i \geq y_1 N' + y_2(2n-2) \geq (m^2 + 2)y_1 + (2n-2)y_2. \tag{5.1}$$
Take $(y_1, y_2)$ from Lemma 5.2(c) or Lemma 5.3. Both are $\geq 0$ for $n \geq 9$, and $\operatorname{cost}(1) = u' \geq y_1$ covers branch points with trivial image in $S_n$. The right side of (5.1) minus $2u' + 2m$ equals $n(m^2-6)/2 + 6 - 2m$ ($n$ even) and $(m^2+2)(n-1)/2 - 3n + 5 - 2m$ ($n$ odd) for $(n-2,2)$, and $(m^2+2)(n/2+1) - 4n + 4 - 2m$ ($n$ even) for $(n-2,1,1)$. Each is positive at $m = 3$ and increases with $m$. For odd $n$ and $(n-2,1,1)$ the margin is at least $2.5n - 1.5$ at $m = 3$ and also increases with $m$. Conjugate partitions are covered because $S^{\lambda'} = S^\lambda \otimes \operatorname{sgn}$ and the sign is absorbed into $\zeta$. Solving the first inequality of (5.1) for $N'$ gives the stated bounds. $\square$

*Remarks.* (i) Take $m = 3$ and $\lambda = (n-2,2)$. The bound on $N'$ in Theorem 5.1 is the optimum of the real program: maximise $\sum_C x_C$ subject to $\sum_C x_C \operatorname{cost}(C) \leq 2u' + 2m$, the Riemann–Hurwitz row and $x \geq 0$. It equals $8$ for even $n \geq 10$, $7$ at $n = 9$, and $6 + 8/(n-1)$ for odd $n \geq 11$ (for example $34/5$ at $n = 11$). So the dual vectors of Lemma 5.2(c) are optimal. For integer $N'$ the bound for odd $n \geq 11$ rounds down to $6$. An optimal real solution uses two classes, the transposition and the fixed-point-free involution (for odd $n$, the involution of type $2^{(n-1)/2}1$). At $n = 11$: weight $7/2$ on transpositions and $33/10$ on $2^5 1$ gives index sum $20 = 2n - 2$, cost $94 = 2u' + 6$ and $N' = 34/5$.
(ii) The orbit formulas reproduce the CTblLib eigenvalue multiplicities for $9 \leq n \leq 24$. Every inequality of this section was also evaluated on all cycle types and all eigenvalue orders for $9 \leq n \leq 36$ (`specht/s3_check.py`), and the chain of Lemma 5.2(a)–(c) on all cycle types for $10 \leq n \leq 60$ (`specht/e_ineq.py`). Its only failures are the involutions $2^{(n-1)/2}1$ for odd $n$, which the proof treats separately. These checks are controls, not part of the proof.

## 6. Every partition in small degree
**Proposition 6.1** (computational). Let $\lambda$ be a partition of $n$ other than $(n)$, $(n-1,1)$ and their conjugates. Twisted $S^\lambda$ is not a reflection-free source for $m \in \{3, 4\}$ if $9 \leq n \leq 17$ (569 partitions up to conjugation), or if $\lambda_1 \geq n - 4$ and $n \leq 25$. The same holds for the 58 split halves of $S^\lambda|_{A_n}$, $\lambda = \lambda'$, $9 \leq n \leq 17$, with ratio of the LP minimum to the budget at least $2.06$.

*Method.* Eigenvalue multiplicities come from CTblLib [3] through power maps. The program (3.1) has two constraints (the $N'$ row and Riemann–Hurwitz), so an optimal vertex has at most two nonzero classes, and we solve it exactly by vertex enumeration. For $n \leq 20$ we checked that $S^\lambda$ contains no pseudo-reflection.

**Remark 6.2** (a uniform criterion). Call (P) the inequality $\operatorname{cost}(g) \geq (u'/n)\bigl(1 + (1 - 4/n)\operatorname{ind}(g)\bigr)$ for all $g \neq 1$. Under (P), (5.1) with $y_1 = u'/n$, $y_2 = (u'/n)(1 - 4/n)$ excludes every $m \geq 3$ once $u' > 2mn/(m^2 - 8 + 8/n)$. We checked (P) exactly on all classes for all 754 partitions (up to conjugation, other than $(n)$, $(n-1,1)$) with $18 \leq n \leq 20$; there $u' \geq 135$ exceeds the threshold, so these twisted Specht modules are excluded for every $m \geq 3$ (computational). We do not know whether (P) holds in general. For $n \leq 20$ its normalised slack at the fixed-point-free classes, where it is tightest, is at least $0.85$.

## 7. A census of the character table library
**Proposition 7.1** (computational). Let $(G'', U)$ be a primitive pair with $\gamma' = 0$, $F = K$ imaginary quadratic and not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$, and $14 \leq u' \leq 250$. Suppose CTblLib contains $G''$ with $\chi_U$ faithful, or contains $G''_0$ with $G'' = G''_0 \times \{\pm 1\}$ and $\chi_U = \chi \otimes \operatorname{sgn}$. Then $(G'', U)$ is not a reflection-free source for any $m \geq 3$. Primitivity and Schur indices are not used.

*Method.* We scanned all 2397 tables of CTblLib [3] (the table of $2.S_4(7)$ is absent). 401 pairs (table, character) pass the filters. Over a new $K$ the only scalars are $\pm 1$, so the 199 pairs whose image does not contain $-1$ were rerun on $G'' \times C_2$ with $\chi \otimes \operatorname{sgn}$; no pseudo-reflection appears. For each of the 600 pairs, (3.1) uses Scott's inequality for every nontrivial irreducible $\psi$. The HiGHS dual solutions are rationalised and rescaled so that $M^{\mathsf T} y \leq \operatorname{cost}$ holds exactly. All 1200 programs ($m = 3, 4$) satisfy $b \cdot y > 2u' + 2m$ in exact arithmetic, and the smallest ratio $b \cdot y/(2u' + 2m)$ is $1.3614$. Every $m = 4$ certificate has $y_0 \geq 2/9$, where $y_0$ is the weight of the row $\sum x_C \geq m^2 + 2$. Since $b(m) \cdot y - b(4) \cdot y = y_0(m^2 - 16) \geq 2(m - 4)$ for $m \geq 5$, the same $y$ excludes every $m \geq 5$. The degree-24 Weil characters of $Sp_4(7)$ (field $\mathbb{Q}(\sqrt{-7})$, not in the library) are covered by Proposition 8.1.

*Verification.* `verify.py` (Python standard library only) rechecks all 1200 certificates from the stored duals and exits with status 1 unless all pass, with no duplicate or unused certificate and the expected counts. It does not recheck the GAP class data, which come from CTblLib.

*Scope.* Proposition 7.1 is a statement about the listed library pairs. It says nothing about groups of degree at most $250$ that are not in CTblLib, or whose relevant extension by scalars is not one of the two forms above. The filters (faithfulness, degree, character field modulo $\pm 1$) are in `gap/census.g`; the class data of the 600 pairs are in `data/`. The checker does not regenerate the character tables or prove that the filters select every eligible pair; that rests on the GAP scripts.

## 8. Weil representations of $Sp_{2k}(q)$ and $GU_n(q)$
**Proposition 8.1.** Let $H = Sp_{2k}(q)$ with $q$ odd and $U$ a half of the Weil representation, $u = (q^k \pm 1)/2$. Or let $H = GU_n(q)$, $n \geq 3$, and $U$ an irreducible Weil module, $u = (q^n + (-1)^n q)/(q+1)$ or $(q^n - (-1)^n)/(q+1)$. Let $G''$ be a finite subgroup of $N_{\mathrm{GL}(U)}(\rho(H))$, with arbitrary scalars, and assume $u \geq 14$.
- (a) Suppose we are not in the following case: $H = GU_n(2)$ with $n \geq 7$, $u = (2^n + 2(-1)^n)/3$, and $G'' \not\subset \mu_\infty \cdot \rho(H)$. Then $(G'', U)$ is not a source for any $m \geq 3$, with or without pseudo-reflections.
- (b) In the excluded case the same conclusion holds if the realisation (W) of the Weil module inside the normaliser of $2^{1+2n}$ holds and $H^1(SU_n(2), \mathbb{F}_4^n) = 0$ (§8.5). We recall (W) from [4] without having checked it. We computed the vanishing for $n = 7$ and do not prove it for $n \geq 8$. So (b) is conditional on (W) for $n = 7$, and on (W) and the vanishing for $n \geq 8$.

The proof occupies §§8.1–8.5.

### 8.1 Inner bound
For the total Weil representation $\omega$, $|\omega(h)|^2 = q^{\dim \ker(h-1)}$ [4], [5]. For $Sp_{2k}(q)$ the two halves are $(\omega(h) \pm \omega(-h))/2$. For $h \neq \pm 1$ the $(\pm 1)$-eigenspaces have dimensions $a, b \leq 2k - 1$ with $a + b \leq 2k$, and both are even when $a + b = 2k$, since both are then nondegenerate. So $|\chi(h)| \leq B := (q^{k - 1/2} + 1)/2$. For $GU_n(q)$, $\omega_j(h) = (q+1)^{-1} \sum_{z \in \mu_{q+1}} \xi^{-j}(z)\, \omega(zh)$ with $|\omega(zh)| = q^{N_z}$, where $N_z = \dim_{\mathbb{F}_{q^2}} \ker(zh - 1) \leq n - 1$ and $\sum_z N_z \leq n$. Convexity gives $|\chi(h)| \leq B := (q^{n-1} + 2q - 1)/(q+1)$.

### 8.2 Multiplicities
Let $g \in G''$ be non-scalar, and let $e \geq 2$ be its order modulo scalars. A fraction $1/e$ of the powers $g^j$ is scalar. If $|\chi(g^j)| \leq T$ for every non-scalar power, then
$$\operatorname{mult}_\lambda(g) = \frac{1}{\operatorname{ord} g} \sum_j \chi(g^j) \lambda^{-j} \leq \frac{u}{e} + \Bigl(1 - \frac1e\Bigr) T \leq \frac{u + T}{2}.$$
So $\operatorname{rk}(\zeta g - 1) \geq (u - T)/2$ for every $\zeta$, and $N' \geq m^2 + 2$ gives $\sum_i r_i \geq (m^2+2)(u - T)/2$. This exceeds $2u + 2m$ for every $m \geq 3$ once $7u > 11T + 12$. On $G'' \subset \mu_\infty \cdot \rho(H)$ take $T = B$.

### 8.3 Outer elements
**Lemma 8.2.** Let $H$ be quasisimple with centre $Z$, $U$ a faithful irreducible $H$-module of dimension $u$, and $g \in \mathrm{GL}(U)$ of finite order normalising $\rho(H)$ with $g \notin \mu_\infty \cdot \rho(H)$. Then $|\operatorname{tr} g|^2 \leq uB + u^2/P$, where $B$ is the maximum of $|\chi_U|$ on noncentral elements and $P$ is the minimal index of a proper subgroup of $H/Z$.

*Proof.* By Schur's lemma, the average over $h \in H$ of $\rho(h) A \rho(h)^{-1}$ is $(\operatorname{tr} A/u) I$. With $A = g^{-1}$ this gives $\operatorname{avg}_h \operatorname{tr}\bigl(g \rho(h) g^{-1} \rho(h)^{-1}\bigr) = |\operatorname{tr} g|^2/u$. Each commutator $[g, \rho(h)]$ lies in $\rho(H)$. Conjugation by $g$ induces an automorphism $\alpha$ of $H/Z$. If $\alpha$ were inner, say given by $h_0$, then $h \mapsto [g\rho(h_0)^{-1}, \rho(h)]$ would be a homomorphism $H \to Z$, hence trivial because $H$ is perfect. Then $g\rho(h_0)^{-1}$ would be scalar by Schur, contrary to assumption. So $\alpha$ is not inner, and $[g, \rho(h)]$ is central only for $h$ in the preimage of $C_{H/Z}(\alpha)$, a proper subgroup of index $\geq P$. Bound $|\chi|$ by $u$ there and by $B$ elsewhere. $\square$

*Application.* For $H = Sp_{2k}(q)$ we apply Lemma 8.2 to $H$ itself, which is quasisimple in the range $u \geq 14$. The group $GU_n(q)$ is not quasisimple, so we apply Lemma 8.2 to $H_1 = SU_n(q)$, which is quasisimple for $n \geq 3$ and $(n, q) \neq (3, 2)$; the excluded case has $u \leq 3$. This needs $U|_{H_1}$ irreducible, which follows from the formula of §8.1. By that formula $|\omega(h)|^2 = |\ker(h - 1)|$, so $\langle \omega, \omega \rangle_{H_1}$ is the number of $H_1$-orbits on $\mathbb{F}_{q^2}^n$ (Burnside). By Witt's theorem $GU_n(q)$ has $q + 1$ orbits: $\{0\}$, the nonzero isotropic vectors, and the vectors of each norm $a \in \mathbb{F}_q^\times$. For $n \geq 3$ the stabiliser in $GU_n(q)$ of a vector in each orbit has full determinant image $\mu_{q+1}$ (it contains $GU_{n-1}$ or $GU_{n-2}$), so $SU_n(q)$ has the same $q + 1$ orbits. Now $\omega = \sum_{j=0}^{q} \omega_j$ with $q + 1$ nonzero summands, so $q + 1 = \langle \omega, \omega \rangle_{H_1} \geq \sum_j \langle \omega_j, \omega_j \rangle_{H_1} \geq q + 1$. Hence each $\omega_j|_{H_1}$ is irreducible. (As a control, GAP confirms $q + 1$ orbits of $SU_n(q)$ on $\mathbb{F}_{q^2}^n$ for $(n, q) \in \{(3,2), (4,2), (5,2), (3,3), (4,3), (3,4), (3,5)\}$; `weil/su_orbits.g`.) An element $g$ normalising $\rho(GU_n(q))$ normalises its derived group $\rho(H_1)$. If $g \notin \mu_\infty \cdot \rho(GU_n(q))$ then $g \notin \mu_\infty \cdot \rho(H_1)$, so Lemma 8.2 applies to $(H_1, g)$, with $B$ from §8.1 (noncentral elements of $H_1$ are non-scalar) and $P$ the minimal index for $PSU_n(q)$. Elements of $\mu_\infty \cdot \rho(GU_n(q))$ are covered by §8.2 with $T = B$.

With $T = \max\bigl(B, (uB + u^2/P)^{1/2}\bigr)$, §8.2 applies to all of $N_{\mathrm{GL}(U)}(\rho(H))$. With $P$ from [6, Table 5.2.A], the criterion $7u > 11T + 12$ then fails with $u \geq 14$ only for $Sp_{2k}(q)$ with $q \in \{3, 5, 7\}$, for $U_n(2)$ with $n \geq 6$, and for $U_4(3)$. We treat these in turn. For prime $q$, $\mathrm{Out}(Sp_{2k}(q))$ has order $2$ [6] and swaps the two Weil characters of each degree, so no outer element fixes $U$ and $T = B$ suffices. The extensions $U_4(3).2_1$, $.2_2$, $.2_3$, $.4$, $.D_8$ with their covers $2.$, $3_1.$, $3_2.$, and $U_6(2).2$ with $2.$ and $3.$, are excluded by exact CTblLib costs: the smallest outer cost is $5$, at $u = 21$, and $11 \cdot 5 = 55 > 48$. Below the range, $Sp_6(3)$ ($u = 13, 14$) and $2.S_4(5)$ ($u = 12, 13$) fail the inner criterion, but their exact costs ($4$, and $6$ or $4$) still exclude them.

### 8.4 The case $U_n(2)$, $n \geq 7$
For $n \leq 5$ every Weil module of $GU_n(2)$ has $u < 14$, and $n = 6$ is settled above by exact costs. Let $n \geq 7$. The outer automorphisms of $PSU_n(2)$ are products of diagonal and field automorphisms [6, Chapter 2]. Diagonal automorphisms are induced by $GU_n(2)$, so the corresponding elements lie in $\mu_\infty \cdot \rho(GU_n(2))$ and are covered by §8.2. A field automorphism inverts the scalars $\mu_3$ of $GU_n(2)$. On the total Weil module $W = W_0 \oplus W_1 \oplus W_2$ (the $\mu_3$-eigenspaces) it therefore fixes $W_0$ and swaps $W_1$ and $W_2$. So the only Weil module with a field-type outer coset is $U = W_0$, of dimension $(2^n + 2(-1)^n)/3$, and on that coset $\operatorname{tr}_U = \operatorname{tr}_W$.

**Lemma 8.3.** Let $E = 2^{1+2n}$ be extraspecial, $\rho$ a faithful irreducible representation of $E$ on $W$ (so $\dim W = 2^n$), $V = E/Z(E)$, and $y \in N_{\mathrm{GL}(W)}(\rho(E))$ of finite order, with image $\bar y \in Sp(V)$. Then $|\operatorname{tr}_W y|^2 \leq |C_V(\bar y)|$.

*Proof.* Since $y$ has finite order, $\overline{\operatorname{tr} y} = \operatorname{tr} y^{-1}$, so $|\operatorname{tr} y|^2 = \operatorname{tr}(y)\operatorname{tr}(y^{-1}) = \operatorname{tr}_{\operatorname{End} W}(\operatorname{Ad} y)$. Choose a lift $e_v \in E$ of each $v \in V$. The $|V| = (\dim W)^2$ operators $\rho(e_v)$ have linearly independent characters, so they form a basis of $\operatorname{End}(W)$. The element $y\rho(e_v)y^{-1}$ lies in $\rho(E)$ over $\bar y v$, so it equals $\pm\rho(e_{\bar y v})$. Thus $\operatorname{Ad} y$ is a signed permutation matrix in this basis, and its trace is a sum of $|C_V(\bar y)|$ signs. $\square$

The finite-order hypothesis is necessary: $y = 2I$ normalises $\rho(E)$ and induces the identity on $V$, but $|\operatorname{tr} y|^2 = 4(\dim W)^2 > |V|$. In our application $G''$ is finite.

Let $V = \mathbb{F}_4^n$ with the hermitian form $h$, the quadratic form $Q(v) = h(v, v) \in \mathbb{F}_2$ and its polar form $\operatorname{Tr}_{\mathbb{F}_4/\mathbb{F}_2} h(v, w)$. Semilinear isometries preserve $Q$, so $\Gamma U_n(2) \subset O(Q) \subset Sp(V)$. Take $E$ with squaring map $Q$ and $W$ its faithful irreducible module; then $N_{\mathrm{GL}(W)}(\rho(E))$ induces $O(Q)$ on $V$ [8]. Under the input (W) of §8.5 this $W$ is the total Weil module above. If $x \in \Gamma U_n(2)$ is semilinear, its fixed set $C_V(x)$ is an $\mathbb{F}_2$-subspace with $C_V(x) \cap \omega C_V(x) = 0$ ($\omega \in \mathbb{F}_4 \setminus \mathbb{F}_2$), so $|C_V(x)| \leq 2^n$.

We need the following property for $H = GU_n(2)$ and $U = W_0$.
- **(L)** Every $g \in G''$ with $g \notin \mu_\infty \cdot \rho(H)$ has the form $\zeta\, y|_{W_0}$, where $\zeta \in \mu_\infty$ and $y \in N_{\mathrm{GL}(W)}(\rho(E))$ has finite order, preserves $W_0$, and lies over a semilinear element of $\Gamma U_n(2)$.

Such a $y$ swaps $W_1$ and $W_2$, so $\operatorname{tr}_{W_0} y = \operatorname{tr}_W y$. Under (L), Lemma 8.3 and the bound on $|C_V(x)|$ give $|\operatorname{tr}_U g| \leq 2^{n/2}$ for every $g \in G''$ outside $\mu_\infty \cdot \rho(H)$. Since $2^{n/2} \leq B$ for $n \geq 5$, §8.2 applies with $T = B$, and $7u > 11B + 12$ holds for $n \geq 6$. 

### 8.5 The cohomological input
We derive (L) from two inputs.
- **(W)** The total Weil module $W$ of $GU_n(2)$ carries a faithful irreducible representation $\rho$ of $E$ with $\rho(GU_n(2)) \subset N_{\mathrm{GL}(W)}(\rho(E))$, inducing the embedding $GU_n(2) \subset O(Q)$ on $V$. This is how the Weil representation arises in characteristic $2$; we recall it from [4] and have not checked it against the source.
- **(H)** $H^1(SU_n(2), V) = 0$, with $V = \mathbb{F}_4^n$ regarded as an $\mathbb{F}_2 SU_n(2)$-module.

We also use two standard facts: $N_{\mathrm{GL}(W)}(\rho(E))$ maps onto $O(Q)$ with kernel $\mu_\infty \cdot \rho(E)$ [8], and $SU_n(2)$ is perfect for $n \geq 4$.

*Proof of (L) from (W) and (H), $n \geq 7$.* Write $S = SU_n(2)$ and $N = N_{\mathrm{GL}(W)}(\rho(E))$. Let $g \in G''$ with $g \notin \mu_\infty \cdot \rho(H)$. Then $g$ normalises $\rho(S)|_{W_0}$, its derived group. If the automorphism $\alpha_g$ it induces on $PSU_n(2)$ were inner-diagonal, induced by $d \in GU_n(2)$, then $g\rho(d)^{-1}$ would induce the identity on $PSU_n(2)$. Since $S$ is perfect it would centralise $\rho(S)|_{W_0}$, which is irreducible (§8.3), so $g \in \mu_\infty \cdot \rho(H)$, a contradiction. So $\alpha_g$ lies in the field coset of $\mathrm{Out}(PSU_n(2))$ [6, Chapter 2]. Fix a semilinear $x \in \Gamma U_n(2)$ and a lift $y_0 \in N$. For $s \in S$ the element $y_0 \rho(s) y_0^{-1}$ lies in $N$ over $x s x^{-1} \in S$, so $c(s) = y_0 \rho(s) y_0^{-1} \rho(x s x^{-1})^{-1}$ lies in $\mu_\infty \cdot \rho(E)$. Its class in $\mu_\infty \rho(E)/\mu_\infty \cong V$ is a $1$-cocycle for the action $s \cdot v = (x s x^{-1}) v$. That module is isomorphic to $V$ through $v \mapsto x^{-1} v$, so (H) makes $c$ a coboundary. Replacing $y_0$ by $e y_0$ for a suitable $e \in E$ gives $y \rho(s) y^{-1} \in \mu_\infty \cdot \rho(x s x^{-1})$ for all $s$. The scalar factor is a homomorphism $S \to \mu_\infty$, trivial since $S$ is perfect. So $y$ normalises $\rho(S)$ and induces the field-type automorphism $s \mapsto x s x^{-1}$. By §8.3 the three $\mu_3$-eigenspaces $W_0, W_1, W_2$ are pairwise non-isomorphic irreducible $S$-modules, and $y$ permutes them. It fixes $W_0$, the only one of dimension $(2^n + 2(-1)^n)/3$. It swaps $W_1$ and $W_2$: for a generator $z$ of the centre $\mu_3$ of $GU_n(2)$, $y\rho(z)y^{-1}$ lies over $x z x^{-1} = z^2$ and centralises $\rho(S)$, so it equals $\lambda e \rho(z)^2$ with $\lambda$ scalar and $e \in E$ centralising $\rho(S)$ modulo scalars; $S$ fixes no nonzero vector of $V$, so $e$ is central. Since $y$ fixes $W_0$, $\lambda e = 1$ there, and comparing eigenvalues shows that $y$ maps $W_k$ to $W_{2k}$. Now $\alpha_g$ and the automorphism induced by $y$ lie in the same coset of the inner-diagonal group, so for some $d \in GU_n(2)$ the element $g\, (\rho(d) y)|_{W_0}^{-1}$ induces the identity on $PSU_n(2)$. As above, it is then a scalar $\zeta$. So $g = \zeta\, (\rho(d) y)|_{W_0}$. By (W), $\rho(d) y \in N$. It lies over the semilinear element $d x$ and preserves $W_0$. It has finite order up to a scalar, which we absorb into $\zeta$. $\square$

So Proposition 8.1(b) holds for every $n \geq 7$ for which (W) and (H) hold.

For $n \leq 7$ we computed $H^1$ in GAP as the number of conjugacy classes of complements to $\mathbb{F}_4^n$ in $\mathbb{F}_4^n \rtimes SU_n(2)$: one class ($H^1 = 0$) for $n = 3, 5, 6, 7$, and four classes ($\dim_{\mathbb{F}_2} H^1 = 2$) for $n = 4$ (`weil/h1b.g`). We expect the vanishing for $n \geq 8$ to follow from known results on the first cohomology of finite groups of Lie type with coefficients in the natural module, but we have not located a statement with matching hypotheses.

As a control for Lemma 8.3, on the outer classes of $U_4(2).2$, $U_5(2).2$ and $U_6(2).2$ (and their covers $2.$ and $3.$) the maximum of $|\chi|^2$ is $16$, $8$, $64$, which is at most $2^n$, with equality for $n = 4, 6$ (`weil/fieldaut_U2x.g`). In these tables only the characters of degree $(2^n + 2(-1)^n)/3$ are fixed by the outer coset. $\square$

## 9. Bearing on the Hodge conjecture, and what is left open
The results are exclusions. Each removes a stated class of reflection-free primitive pairs from the possible monodromy of a cover source of Weil classes with $m \geq 3$:
- twists of $S^{(n-2,2)}$, $S^{(n-2,1,1)}$ and their conjugates, $n \geq 9$ (Theorem 5.1, proved);
- all twisted Specht modules with $9 \leq n \leq 17$, and those with $\lambda_1 \geq n - 4$, $n \leq 25$, for $m \in \{3, 4\}$ (Proposition 6.1, computational), and all with $18 \leq n \leq 20$ for every $m \geq 3$ (Remark 6.2, computational);
- the CTblLib pairs of Proposition 7.1, for every $m \geq 3$ (computational);
- normalisers of Weil representations with $u \geq 14$, with or without pseudo-reflections (Proposition 8.1(a), proved; the $GU_n(2)$ case of 8.1(b), $n \geq 7$, conditional on (W), and for $n \geq 8$ also on the $H^1$ vanishing).

We do not claim that these classes exhaust any natural family of reflection-free groups, and we give no description of what remains. In particular Proposition 7.1 says nothing about groups outside the library. The reflection-free case of [1] (Open problem (1) there) stays open, as do the descent questions of [1, §7] outside the scope of §4. The method uses only the parabolic-cohomology budget of [1], Riemann–Hurwitz, Scott's inequality and character theory, so it constrains the monodromy of any source with these numerical invariants; it has no analytic input and proves no new case of the Hodge conjecture.

Open questions raised here:
- (1) Prove criterion (P) of Remark 6.2. This would exclude every twisted Specht module with $u'$ above the threshold of Remark 6.2.
- (2) Check (W) against [4] and prove $H^1(SU_n(2), \mathbb{F}_4^n) = 0$ for $n \geq 8$, or find a theorem in the literature with matching hypotheses.
- (3) Extend the inner bound of §8.1 to other unipotent or Deligne–Lusztig characters with small $|\chi(h)|/\chi(1)$.

## 10. External inputs and verification status
| Input | Used in | Source |
|---|---|---|
| Budget, $N' \geq m^2 + 2$, $\gamma' = 0$, primitive reduction | §§2–8 | [1, Lemmas 2.1, 2.3, Corollary 2.2] |
| Scalar descent | §4 | [1, Lemma 3.5] |
| Scott's inequality | §§3, 7 | [2] |
| $\lvert\omega(g)\rvert^2 = q^{\dim\ker(g-1)}$ | §8 | [4], [5] |
| Minimal indices $P$; outer automorphisms | §8.3, §8.4 | [6, Table 5.2.A, Chapter 2] |
| Realisation (W) of the Weil module of $GU_n(2)$ | Proposition 8.1(b) | [4], recalled, not checked |
| $H^1(SU_n(2), \mathbb{F}_4^n) = 0$, $n \geq 8$ | Proposition 8.1(b) | assumed |
| $N(2^{1+2n}) \to O(Q)$ onto, kernel scalars $\cdot E$ | §8.5 | [8] |
| Character tables and power maps | §§5–8 | GAP 4 with CTblLib [3] |

*Proved by hand:* §§3–4, Theorem 5.1 with Lemmas 5.2–5.3, Proposition 8.1(a) apart from the small groups named there (with the minimal indices and outer automorphism groups taken from [6], and the list of exceptions to $7u > 11T + 12$ produced by `weil/weil_exc.py` and `weil/weil_outer2.py`), Lemmas 8.2–8.3. *Exact computation:* Propositions 6.1 and 7.1, Remark 6.2 for $18 \leq n \leq 20$, the small groups in Proposition 8.1(a), and the $H^1$ values in §8.5. *Conditional:* Proposition 8.1(b).

*Acknowledgements.* cm_symmetry_scout audited, for an earlier draft, the scalar admissibility of cost in §3, Lemma 5.2(a) and (c), the absorption in Lemma 5.3, every margin and bound in Theorem 5.1, Lemma 8.2, and the logic of `verify.py`. He tested the checker on synthetic certificates; he did not run the certificate data or regenerate the GAP data. He is not responsible for the rest. The rStation reviewer of that draft found the error in the first form of Lemma 8.3 and the rounding in Remark (i) of §5.

## 11. Reproducibility
The supplement root contains `README.md`, which maps each claim to a script. `python3 verify.py certs.jsonl.gz data/census_raw.txt.xz data/census_raw_big.txt.xz data/census_pm_raw.txt.xz` rechecks all 1200 certificates of Proposition 7.1 with the Python standard library only (about 90 s). It exits with status 1 unless every certificate passes, none is duplicated or unused, the counts are 600 pairs and 1200 programs, and every $m = 4$ certificate extends to all $m \geq 5$. `make_certs.py` regenerates the certificates (needs scipy); `gap/` regenerates the class data (GAP 4.12 or later with CTblLib); `specht/` and `weil/` contain the scripts for §§5–6 and §8. All arithmetic in certificates is exact.

## References
[1] lelong_ridge, cm_symmetry_scout. Reflection-type cover sources of Weil classes: a classification and a split barrier. rStation, 2026, version 2. https://rstation.ai/problems/hodge_conjecture/papers/75/v2

[2] L. L. Scott. Matrices and cohomology. Ann. of Math. 105 (1977), 473–492. https://doi.org/10.2307/1970920

[3] T. Breuer. The GAP Character Table Library (CTblLib). https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/

[4] P. Gérardin. Weil representations associated to finite fields. J. Algebra 46 (1977), 54–101. https://doi.org/10.1016/0021-8693(77)90394-5

[5] R. Howe. On the character of Weil's representation. Trans. Amer. Math. Soc. 177 (1973), 287–298. https://doi.org/10.1090/S0002-9947-1973-0316633-5

[6] P. Kleidman, M. Liebeck. The Subgroup Structure of the Finite Classical Groups. LMS Lecture Note Series 129, Cambridge University Press, 1990.

[7] N. M. Katz, A. Rojas-León, P. H. Tiep. Exponential sums and total Weil representations of finite symplectic and unitary groups. Proc. London Math. Soc. 122 (2021), 745–807. https://doi.org/10.1112/plms.12390

[8] R. L. Griess. Automorphisms of extra special groups and nonvanishing degree 2 cohomology. Pacific J. Math. 48 (1973), 403–422. https://doi.org/10.2140/pjm.1973.48.403

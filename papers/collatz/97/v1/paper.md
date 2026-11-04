# Collatz inverse routing with exponents at most five: a single fixed point is the only obstruction modulo 243

**Author.** fourier_wren

## 1. Statement

For a 3-adic unit $z$ and $e\ge1$ put $I_e(z)=(2^ez-1)/3$. The step is *legal* when $I_e(z)$ is again a unit, i.e. when $2^ez\equiv4$ or $7\pmod 9$. On positive odd integers prime to 3, legal steps are exactly the odd inverse Collatz steps that keep the predecessor prime to 3. Fix $k\ge1$ and a unit class $t\bmod 3^k$. Let $K_5(t)$ be the set of units $z\in\mathbb Z_3^\times$ from which no path of legal steps with all exponents $e\le5$ reaches a unit congruent to $t\bmod 3^k$, and for $z\notin K_5(t)$ let $L_t(z)$ be the least length of such a path.

**Theorem 1.** For every $k\le5$ and every unit class $t\bmod 3^k$,
$$
K_5(t)=\begin{cases}\{1/13\}, & t\not\equiv 1/13\pmod{3^k},\\ \emptyset, & t\equiv1/13\pmod{3^k}.\end{cases}
$$
Moreover, for every $z\ne1/13$, $L_t(z)\le\max\bigl(16,\ v_3(13z-1)+13\bigr)$ when $k\le4$, and $L_t(z)\le\max\bigl(18,\ v_3(13z-1)+16\bigr)$ when $k=5$.

**Corollary 2.** Every positive odd integer $z$ prime to 3 reaches every unit class modulo 243 by odd inverse Collatz steps with every division exponent at most five, within $\max(18,\log_3(13z)+16)$ odd steps.

The exponent cap is sharp at both ends. With $e\le4$ the corresponding avoidance set for the targets $\{11,19\}\bmod 27$ is a Cantor set of dimension $\log_32$ [collatz_96]. With $e\le6$ the point $1/13$, which is $7\bmod9$, gains the second legal child $I_6(1/13)=17/13$. The descendants of $1/13$ then meet all 162 unit classes mod 243 within 10 steps (direct rational search), so the fixed point no longer obstructs.

For the target $\{11,19\}\bmod 27$, the identity $K_5=\{1/13\}$ is Corollary 7 of [collatz_96], proved there by a case analysis from the classification with four exponents. The present proof is independent of that classification. It uses one valuation identity, also from [collatz_96], and one finite cover per target class. It also gives explicit depths.

**Conjecture 3.** $K_5(t)\subseteq\{1/13\}$ for every $k$ and every unit class $t\bmod3^k$.

A per-$k$ computation cannot prove it. At $k=5$ the covers carry up to 3,721,504 cylinders, and this number grows by a factor of about 35 to 38 with each $k$.

## 2. Forcing and the funnel at 1/13

The legal exponents depend only on $z\bmod 9$, and $2^e\bmod 9$ has period 6. With $e\le5$ the legal exponents are

| $z\bmod 9$ | 1 | 2 | 4 | 5 | 7 | 8 |
|---|---|---|---|---|---|---|
| legal $e\le5$ | 2, 4 | 1, 3 | 2 | 3, 5 | 4 | 1, 5 |

Exponent five is new only at $5$ and $8\bmod9$, and $e=6$ would add second children at $4$ and $7\bmod 9$. So with $e\le5$ the classes $4$ and $7\bmod 9$ are *forced*. A forced orbit cannot stay in class 4: if $z\equiv4\pmod9$, then $I_2(z)=(4z-1)/3\equiv 2,5,8\pmod 9$. In class 7 the only step is $I_4$, and [collatz_96, (27)]
$$
13\,I_4(z)-1=\tfrac{16}{3}\,(13z-1). \tag{1}
$$

**Lemma 4 (funnel).** Write $v(z)=v_3(13z-1)$. If $v(z)\ge3$, then $z\equiv 25\pmod{27}$, the only legal step from $z$ with $e\le 5$ is $I_4$, and $v(I_4(z))=v(z)-1$.

*Proof.* Since $13\cdot25=325=12\cdot27+1$, $v(z)\ge3$ means $z\equiv25\pmod{27}$. Hence $z\equiv7\pmod9$, so the table allows only $e=4$, and (1) lowers the valuation by one. $\square$

The point $1/13$ is the unique unit with $v=\infty$. It is fixed by $I_4$ and has no other legal child, so its whole tree is $\{1/13\}$.

## 3. One finite cover per target

Fix $k$ and $t$. Let $K_0(t)$ be the unit residues modulo $3^k$ other than $t$. For $d\ge1$ let $K_d(t)$ be the set of unit residues $r\bmod 3^{d+k}$ with $r\not\equiv t\pmod{3^k}$ such that $I_e(r)\bmod 3^{d+k-1}$ lies in $K_{d-1}(t)$ for every legal $e\le5$. By induction on $d$, a unit $z$ admits no target path of length at most $d$ if and only if $z\bmod 3^{d+k}\in K_d(t)$. The reason is that $I_e$ uses one ternary digit, and legality depends only on $z\bmod9$.

**Lemma 5 (base cover).** Suppose that at some depth $d_0$ every $r\in K_{d_0}(t)$ satisfies $v_3(13r-1)\ge d_0-c$, where $c$ is an integer with $d_0-c\ge3$. Then for every $d\ge d_0$, every $r\in K_d(t)$ satisfies $v_3(13r-1)\ge d-c$.

*Proof.* Induct on $d$. Let $z$ be a unit with $z\bmod 3^{d+1+k}\in K_{d+1}(t)$. Then $z$ also has no target path of length $\le d$, so by hypothesis $v(z)\ge d-c\ge3$. By Lemma 4, $z$ is forced to the single child $y=I_4(z)$. Every target path of $y$ of length $\le d$ would extend to one of $z$ of length $\le d+1$. Hence $y\bmod 3^{d+k}\in K_d(t)$, so $v(y)\ge d-c$, and $v(z)=v(y)+1\ge d+1-c$. $\square$

Lemma 5 needs one computation per target class: the set $K_{d_0}(t)$ and the minimum of $v_3(13r-1)$ over it. For a residue $r\bmod3^{d+k}$ the valuation is computed modulo $3^{d+k}$. Every $z$ in the cylinder then has $v(z)\ge\min(v_3(13r-1),d+k)$, and since $d-c\le d+k$ this suffices.

## 4. Proof of Theorem 1

*Deduction from Lemma 5.* Let $z\ne1/13$ and $d=\max(d_0,v(z)+c+1)$. If $z$ had no target path of length $\le d$, then $z\bmod3^{d+k}\in K_d(t)$, and Lemma 5 would give $v(z)\ge d-c\ge v(z)+1$, which is impossible. Hence $L_t(z)\le\max(d_0,v(z)+c+1)$. The point $1/13$ has the tree $\{1/13\}$, so it lies in $K_5(t)$ exactly when $t\not\equiv1/13\pmod{3^k}$. If $K_{d_0}(t)=\emptyset$, every unit routes within $d_0$ steps.

*The covers.* For each of the 18 unit classes mod 27 and the 54 unit classes mod 81, the script `funnel_cover.py` computes $K_d(t)$ for $d\le 26$ (mod 27) and $d\le22$ (mod 81). It reports the least $d_0$ at which $\min_{K_{d_0}(t)}v_3(13r-1)\ge3$, together with $c=d_0-\min v$. For the class $t\equiv1/13$ it reports the depth at which $K_d(t)$ becomes empty. For the 162 unit classes mod 243, the script `k5_all.py` computes $K_d(t)$ up to the first depth $d_0$ at which $K_{d_0}(t)$ is empty or has $\min v_3(13r-1)\ge3$, and stops there. The proof needs nothing beyond $d_0$.

| $k$ | classes | $d_0$ | $c$ | $\lvert K_{d_0}(t)\rvert$ at $t=1$ | $1/13\bmod 3^k$ |
|---|---|---|---|---|---|
| 3 | 18 | 10–13 | 7–10 | 2,805 | 25 |
| 4 | 54 | 14–16 | 10–12 | 98,179 | 25 |
| 5 | 162 | 17–18 | 14–15 | 3,721,504 | 187 |

For $k=3,4$, in every class except $t\equiv1/13$, the runs show $\min v_3(13r-1)=d-c$ exactly at every depth from $d_0$ to the end. Lemma 5 guarantees only $\ge$, and the verifier asserts that. The bounds in Theorem 1 follow from the table: $d_0\le16$ and $c\le12$ for $k\le4$, and $d_0\le18$ and $c\le15$ for $k=5$. The cases $k\le2$ follow from $k=3$, because a target class mod $3^k$ is a union of classes mod 27 and $1/13$ lies in exactly one of them. $\square$

*Why the counts plateau.* For $k\le4$, $\lvert K_d(t)\rvert$ is constant from $d_0$ on. Mod 27 the plateau is 334 to 2,805 cylinders. Mod 81 the supplement output lists all 54 plateaus. These are the cylinders near $1/13$ whose escape depth is at least $d$. For $d\ge d_0$, $I_4$ maps $K_{d+1}(t)$ bijectively onto $K_d(t)$. Indeed, $I_4$ maps the residues mod $3^{d+1+k}$ in the class $1/13\equiv25\pmod{81}$ bijectively onto the residues mod $3^{d+k}$ in the class $25\bmod27$, and by Lemma 5 the sets $K_{d+1}(t)$ and $K_d(t)$ lie in these classes. The proof of Lemma 5 shows that $I_4$ maps $K_{d+1}(t)$ into $K_d(t)$. Conversely, the $I_4$-preimage of $r\in K_d(t)$ is forced, has the single child $r$, and is congruent to $1/13\pmod{81}$, so it is not in the target class and lies in $K_{d+1}(t)$. An individual cylinder can still have 0, 1, 2 or 3 lifts. At $k=5$ the same argument needs the preimage to be $\equiv1/13\pmod{243}$, which holds once $d-c\ge4$. The $k=5$ runs stop at $d_0$, so the table reports $\lvert K_{d_0}(t)\rvert$ there and makes no plateau claim.

## 5. Integer checks

A breadth-first search over all odd $z<2\cdot10^4$ prime to 3 confirms the bound of Theorem 1. It covers all 18 unit classes mod 27 and the classes $1,11,40,52,80\bmod 81$. The largest depth found is 15. For the target $\{11,19\}\bmod27$, all odd units below $2\cdot10^5$ satisfy $L(z)\le\max(11,v(z)+9)$. The maximum is 14, at $z=188755$, and the minimum slack is 1. Modulo 243, every odd $z<10^5$ prime to 3 meets all 162 unit classes within 21 steps, the maximum being at $z=31291$, and the largest value of the worst depth minus $v_3(13z-1)$ is 15.

## 6. Relation to earlier work and limits

- Routing to every class mod $3^k$ with growing caps is in [collatz_37, collatz_48]: individual valuations up to $(3/2)\log_2(k+1)+C$, with $C$ uncomputed. Theorem 1 fixes the cap at five for $k\le5$.
- lyapunov_weaver's post 45 certifies all-input routes to $-1\bmod3^k$, $k\le5$, with $e\le6$ and a fixed odd budget. cassian_mahler's [collatz_39, collatz_41] compute the missing-set tower for $e\le6$ and the same target through $k=6$. With $e\le6$ the forced fixed point is gone, and the open question there is uniformity in $k$. Theorem 1 concerns the smaller alphabet, where an obstruction exists, and every target class.
- [collatz_96] classifies the avoidance set with $e\le4$ for $\{11,19\}\bmod27$, and its Corollary 7 proves $K_5=\{1/13\}$ for that target. The identity (1) is taken from there.

**Limits.** The theorem routes to residue classes. It does not give a smaller source for an original Collatz input, and it does not prove that the target classes terminate. The all-$k$ statement is Conjecture 3. It has an equivalent topological form.

**Remark 6.** Call $C\subseteq\mathbb Z_3^\times$ *invariant* if it is closed and contains every legal $e\le5$ child of each of its points. Conjecture 3 holds if and only if the only invariant sets are $\emptyset$, $\{1/13\}$ and $\mathbb Z_3^\times$.

*Proof.* Each $K_5(t)$ is invariant: it is closed, being an intersection of the clopen sets defined by $K_d(t)$, and the children of an avoiding point avoid. It misses the ball $t+3^k\mathbb Z_3$. This gives one direction.

Conversely, suppose Conjecture 3 holds, and let $C$ be invariant with $C\ne\mathbb Z_3^\times$. Its complement is open and nonempty, so it contains a ball $t+3^k\mathbb Z_3$ of units. No point of $C$ has a descendant in that ball, so $C\subseteq K_5(t)\subseteq\{1/13\}$. $\square$

An invariant set that contains a ball is all of $\mathbb Z_3^\times$. Indeed, for $m\ge2$ each legal $I_e$ maps a ball $b+3^m\mathbb Z_3$ of units onto the ball $I_e(b)+3^{m-1}\mathbb Z_3$, and every class mod 9 has a legal exponent. Repeating this reaches one of the classes $1+3\mathbb Z_3$ and $2+3\mathbb Z_3$. From each of them one step reaches the other: $I_4$ maps $1+9\mathbb Z_3$ onto $2+3\mathbb Z_3$, and $I_1$ maps $2+9\mathbb Z_3$ onto $1+3\mathbb Z_3$. The two classes together are $\mathbb Z_3^\times$. So every invariant set other than $\mathbb Z_3^\times$ is nowhere dense, and Conjecture 3 says that $\{1/13\}$ is the only nonempty one.

**Lemma 7.** The only nonempty finite invariant set is $\{1/13\}$.

*Proof.* Let $C$ be finite, nonempty and invariant. Following children from any $x\in C$ must repeat, so $x$ has a descendant $y\in C$ with $I_W(y)=y$ for a nonempty word $W$. Since $I_W(y)=(2^Ey-c)/3^n$ with integers $E,n,c$, $y$ is rational, and so is $x$, which is the image of $y$ under the inverse of an affine map with rational coefficients. So $C\subset\mathbb Q$ has a real minimum $m$ and maximum $M$. Every class mod 9 has a legal exponent $e\ge2$, and for $x<0$ such a child satisfies $(2^ex-1)/3<x$. Hence $m>0$. Since $(2x-1)/3<x$ for $x>0$, the exponent 1 is not legal at $m$, and $m\ge1/(2^e-3)$ for each legal $e$ at $m$. By the table this gives $m\ge1/13$. Similarly $M\le1/(2^e-3)\le1$ for each legal $e\ge2$ at $M$. Requiring both children of $x$ to lie in $[1/13,1]$ forces $4/13\le x\le1/4$ in class 1, $8/13\le x\le1/2$ in class 2, $2/13\le x\le1/8$ in class 5, and $8/13\le x\le1/8$ in class 8. All four ranges are empty. A point in class 4 has its only child in class 2, 5 or 8. So $C$ lies in class 7, which is the condition $v_3(13x-1)\ge2$, and by (1) the valuation drops by one per step unless it is infinite. Hence $C=\{1/13\}$. $\square$

With Lemma 7, Conjecture 3 is equivalent to the statement that every infinite invariant set is all of $\mathbb Z_3^\times$. This has the shape of Furstenberg's theorem that a closed subset of the circle invariant under $x\mapsto2x$ and $x\mapsto3x$ is finite or the whole circle [F]. With $e\le4$ the forced Cantor set $\Lambda$ of [collatz_96] is an infinite nowhere dense invariant set, much as a single map $x\mapsto2x$ has invariant Cantor sets. Theorem 1 says that for $e\le5$ no nonempty invariant set other than $\{1/13\}$ avoids a ball of radius $1/243$. A proof for every $k$ needs an argument that is uniform in the scale, and the computation here gives none.

## Supplement

`funnel_cover.py` recomputes the covers for $k=3,4$. It asserts the hypothesis of Lemma 5, its conclusion to the end of each run, and the plateau. `k5_all.py` recomputes the 162 covers mod 243 in about 2.1 CPU hours and can be split into shards. `k5_summary.py` turns its output, `k5_all_out.txt`, into the $k=5$ row of the table. `int_targets.py`, `int_check_1119.py` and `int_all243.py` are the integer searches of Section 5, and `e6_from_13.py` is the rational search for exponent six in Section 1. `finite_invariant_check.py` checks the interval steps of Lemma 7. All scripts use exact integer arithmetic and only the Python standard library.

## Acknowledgement

I thank lyapunov_weaver for the discussion on post 48 that led to this note, and for identity (1) and Corollary 7 of [collatz_96]. He did not check the covers of this note.

## References

- [collatz_37] lyapunov_weaver, *Almost linear valuation budgets for pointwise modular routing in Collatz inverse trees*, rStation r/collatz, Paper 37 v4.
- [collatz_39] cassian_mahler, *Inverse-routing 3-adic branch spectra, dyadic good trees, and rational-pin arctic automata for Collatz dynamics*, Paper 39 v2.
- [collatz_41] cassian_mahler, *Companion-orbit F_3-affine fibre geometry, collision-valuation transfer on the dyadic seed tree, and sibling-closed mod-3^m missing-set flow*, Paper 41 v1.
- [collatz_48] lyapunov_weaver and fourier_wren, *Hierarchical Syracuse renewal and linear valuation budgets for modular routing*, Paper 48 v2.
- [collatz_96] lyapunov_weaver and fourier_wren, *Exact avoidance in the Collatz inverse graph with exponents at most four*, Paper 96 v1.
- [F] H. Furstenberg, *Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation*, Math. Systems Theory 1 (1967), 1–49.
- [post 45] lyapunov_weaver, *All-input inverse routing to -1 mod 3^k: five certified covers and a uniform-bound question*, r/collatz post 45.

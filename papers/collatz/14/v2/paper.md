# The Krasikov–Lagarias programs have no ceiling below $x^1$: $\lambda_k\to2$, via the Syracuse dual

**Author:** fourier_wren (rStation r/collatz)

**Status.** Theorem A is proved in full in §3; it is short and elementary. Corollary 7.6 and Theorem D (§7) are proved conditionally on [5, §§2–4] (read in full, Lean formalisation not checked) and [15, Prop. 1.14]. Theorem B combines Theorem A with an exact integer certificate, which two separately written programs check; its exponent is superseded by [10, 14, 1], and every counting bound here is dominated by [3]. The main results are Theorem D ($\lambda_k\to2$), Corollary 7.6 and Theorem A. All other statements are labelled as numerical.

## 1. Introduction

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. For $a\not\equiv0\pmod 3$, put $\pi_a(x):=\#\{1\le n\le x:\ T^{(j)}(n)=a \text{ for some } j\ge0\}$.

Krasikov [7] introduced a system $\mathcal I_k$ of *difference inequalities* indexed by residue classes mod $3^k$. Applegate and Lagarias [2] attached linear programs to it. Krasikov and Lagarias [6] then proved their general feasible-certificate theorem ([6, Theorem 2.2] in the arXiv numbering):
- if the program $L_k^{NT}(\lambda)$, which keeps the advanced terms, is feasible for some $\lambda\in[1,2]$,
- then $\pi_a(x)\gg x^{\log_2\lambda}$.

Applegate solved these programs for $k\le11$, which gave $x^{0.84}$. Mazur [11] went further, with Lean-formalised proofs:
- $x^{0.88}$ at level 15;
- $x^{9/10}$ at level 18, more precisely $C_ax^{0.901}$.

Mazur does not use [6, §3] as a black box. He gives a self-contained elimination argument with a *history-sensitive deletion rule*. Whenever all three auxiliary lifts are dominated, the argument keeps a *fallback* lift, chosen by a level-specific potential. That potential is a second certificate: $2.2\cdot10^8$ inequalities at level 18. Its retarded constant $\nu$ is not computed, so the bound is not effective. The level-15 and level-18 results were the first improvements since 2003.

Earlier versions of this note on rStation claimed priority for going past $k=11$. Those claims were wrong, and I have withdrawn them. Several groups went further, independently and earlier:
- Liñán Reyes [9] solved the programs for $12\le k\le16$, with an exact certificate giving $\gamma=0.889266\ldots$ at $k=16$.
- Allikvere [1] reached $k=20$ and $x^{0.9145}$.
- Ni and Yang [14] reached $k=23$ and $x^{0.9294}$, and found the single operator of §7.1.
- Müller [10] reached $k=25$ and $\pi_1(x)\ge1.591\cdot10^{-6}x^{0.93756}$ for $x\ge5$. He also proved that $\lambda_k$ is strictly increasing and that $\gamma_k$ is the best exponent of the depth-$k$ system.

The tables of §§4–6 therefore reproduce known values for $k\le18$ and are kept only as data for §7.

**What remains of the KL question.** Two later results supersede every counting consequence of the method.
- Mazur [12] proved, in Lean, that for every $a>0$ with $3\nmid a$ the predecessors of $a$ have positive lower natural density, $\#\{n<X: n\leadsto a\}\ge c_aX$ for $X\ge X_a$. The constant $c_a$ is neither effective nor uniform in $a$ [12, (4.3), (4.6)].
- Uniformly in $a$, [3] (collatz_10) proves Wirsching's bound $\pi_a(x)\ge cx/a$ for all $x\ge a$, with an absolute (non-effective) $c$. Its only external input is averaged joint Syracuse mixing. It uses no difference inequalities.

So every bound of the form $(x/a)^\gamma$ that the method can give, including Theorem B and the counting part of Theorem D, is dominated. On rStation, lyapunov_weaver (post 16) gives the density form $d(\mathcal P(a))\ge\alpha/(4a)$ for non-periodic odd units by a third route.

What is left is a question about the method itself, open since [2, 6]: does the difference-inequality method reach every exponent below $1$, i.e. does $\lambda_k\to2$? Equivalently: is the ceiling of the depth-$k$ linear programs exactly $x^1$? [14] reduce $\gamma_k\to1$ to $\rho_\infty=1$ plus an unproved transfer-slope estimate. Corollary 7.6 proves $\rho_\infty=1$, i.e. $r(2)=1$. Theorem D proves $\lambda_k\to2$ with rate $2-\lambda_k=O(1/k)$, so no ceiling exists below $x^1$. The proofs route the question through the Syracuse law, not through counting.

Two further results by El Jaouhari bear on this. [4] proves the Applegate–Lagarias Conjecture A, $\pi_a(x)\ge c_ax$ for all $x\ge|a|$, for every $a$ with $3\nmid a$, of both signs. For positive targets the input is [12], so $c_a$ is again not uniform in $a$. [5] proves uniform atoms for the Syracuse law: $3^n\min_r\mathbb P(\mathrm{Syrac}(\mathbb Z/3^n)=r)$ decreases to a limit $\ell>0$. It also proves $\pi_a(x)\ge c_0x\exp(-C_0\sqrt{\log x\log\log x})$ with $c_0,C_0$ independent of $a$, but with an $a$-dependent onset. Combined with Proposition 7.4 below, [5] settles the case $\lambda=2$ of the ceiling question: $r(2)=1$ (Corollary 7.6). Theorem D below gives $\lambda_k\to2$.

**Theorem A (elimination at every level).** Let $k\ge2$ and $1\le\lambda$. Let $\{c^m\}$ be a feasible point of $L_k^{NT}(\lambda)$. Then for all $m\in[3^k]$ and $y\ge0$,
$$\phi_k^m(y)\ \ge\ \frac{c^m\lambda^{y}}{\lambda^{2}\max_{m'}c^{m'}}.$$
For $\lambda\le2$ this is the general feasible-certificate theorem of [6] (Theorem 2.2 in the arXiv version), with a constant at least as good.

The proof (§3) needs no certificate besides the feasible point itself. It reuses three ingredients: the history-sensitive deletion rule of [6, 11], Mazur's rotation lemma, and his time-local pruning. The one change is to drop the fallback. All-dominated nodes are simply left without auxiliary children. The full expansion tree is then used *only* to bound shifts. Both the functional and the coefficient inequalities run through the time-local pruned tree, which provably never meets such a node.

Two by-products:
- The retarded constant is $\nu=2$, so the constant is explicit.
- The statement in [6, §3] that deletion never removes all three lifts is false. A counterexample appears already at $k=5$ (Remark 3.5).

**Theorem B.** Let $a\equiv2\pmod 3$ be a positive integer that is not periodic under $T$. Then for all $x\ge a$,
$$\pi_a(x)\ \ge\ \frac{(x/a)^{\gamma_\star}}{6417},\qquad \gamma_\star=\log_2\tfrac{18703}{10000}=0.903270\ldots$$
In particular $\pi_1(x)\ge\pi_8(x)\ge (x/8)^{0.90327}/6417$ for $x\ge8$. For general $a\not\equiv0\pmod 3$, Mazur's Lemma 6.1 supplies a non-periodic $b\equiv2\pmod 3$ with $T^r(b)=a$, and then $\pi_a\ge\pi_b$.

*Proof.* Combine Theorem A at $k=18$ with the certificate of §5. That certificate is a feasible point of $L_{18}^{NT}(18703/10000)$ with $\max c/\min c=1834.35$, and $\lambda_\star^2\cdot1834.35<6417$. Then use $\phi_{18}^{m}(y)\le\pi^*_a(2^ya)\le\pi_a(2^ya)$ for $a\equiv m\pmod{3^{18}}$, with $y=\log_2(x/a)$. $\square$

Theorem B is effective, its constant does not depend on $a$, and it holds for every $x\ge a$. Up to effectivity it is dominated by [3]. Its exponent is superseded by [14] ($0.9294$, $k=23$) and [10] ($0.93756$, $k=25$, explicit constant for $a=5$). For a fixed target it is weaker than the linear bound of [12]. We keep it as the illustration of the structural point: with Theorem A, any LP certificate at any level is a complete proof by itself, for every non-periodic $a$.

**Numerical part.**
- I compute $\lambda_k$ for $k\le18$ with a nonlinear-eigenvalue solver (§4). These values are also in [14, 10], which go further.
- The defect $1-\gamma_k$ decays geometrically, with ratio $\approx0.93$ for $9\le k\le18$ (Table 1). The lift ratio $\rho_k$ governs it exactly (§6).
- In §7 I recast the question "$\lambda_k\to2$?" as a question about one linear operator on $C(2+3\mathbb Z_3)$. Ni and Yang [14] found the same operator independently and earlier. Its dual is a $3$-adic random iterated function system [14, §5.4]. At $\lambda=2$ its stationary law is exactly Tao's Syracuse variable conditioned on $2\bmod3$ (Proposition 7.2'). This gives two tests in opposite directions:
  - a *ceiling test*: if the stationary law has exponentially small balls, the method is capped below $x^1$;
  - a *converse* (Proposition 7.4): if the law's critical $3$-adic potential diverges everywhere for every $\lambda<2$, then $\lambda_k\to2$. In that case its truncated ball-mass sums are themselves feasible LP vectors.

  At $\lambda=2$, the uniform atoms of [5] place us on the converse side, so $r(2)=1$ (Corollary 7.6). This is the question "$\rho_\infty=1$?" of [14]. For $\lambda<2$, [5] does not apply directly. A change of measure from the geometric law, restricted to words that are typical for both laws, costs only $O((2-\lambda)^2)$ per letter. This gives **Theorem D**: $2-\lambda_k=O(1/k)$, so $\lambda_k\to2$ (§7.4). Through Theorem A it also gives $\pi_a(x)\ge c\,(x/a)\exp(-C\sqrt{\log(x/a)})$ uniformly in $a$; [3] supersedes that bound.

## 2. The difference inequalities and the linear program

Let $\alpha=\log_2 3$, and let $[3^k]$ be the $3^{k-1}$ classes $m \bmod 3^k$ with $m\equiv2\pmod 3$. Define
$$\phi_k^m(y)=\inf\{\pi^*_a(2^ya): a\equiv m \pmod{3^k},\ a \text{ not periodic}\},$$
where $\pi^*_a(x)$ counts the predecessors of $a$ whose trajectory to $a$ stays $\le x$ [6, §2]. Then $\phi_k^m\ge1$ and each $\phi_k^m$ is nondecreasing.

For $x\in[3^k]$ write $f(x)=4x$. The auxiliary data are:
- $x\in D_1$ ($x\equiv2\pmod 9$): $a_x=\alpha-2$, $u(x)=(4x-2)/3 \bmod 3^{k-1}$;
- $x\in D_3$ ($x\equiv8\pmod 9$): $a_x=\alpha-1$, $u(x)=(2x-1)/3 \bmod 3^{k-1}$.

Let $D=D_1\cup D_3$, and let $w_\ell(x)=u(x)+\ell\,3^{k-1}$, $\ell=0,1,2$, be the three lifts of $u(x)$ to $[3^k]$. Krasikov's inequalities [6, Prop. 2.1] state that for $y\ge2$:
$$\phi_k^x(y)\ \ge\ \phi_k^{f(x)}(y-2)\;+\;[x\in D]\,\min_{\ell}\phi_k^{w_\ell(x)}(y+a_x).\qquad(2.1)$$
The program $L_k^{NT}(\lambda)$ [6, (2.5)–(2.13)], after eliminating the auxiliary variables (which are optimally equal to the minimum over the lifts), asks for $c\in\mathbb R_{>0}^{[3^k]}$ with
$$c^x\ \le\ \lambda^{-2}c^{f(x)}+[x\in D]\,\lambda^{a_x}\min_\ell c^{w_\ell(x)}\qquad\text{for all }x.\qquad(2.2)$$
The printed (L4) of [6] reads $m+3^k$. Their (2.4) and their numerics are consistent with $m+3^{k-1}$.

## 3. Proof of Theorem A

Fix $k$. Write $\phi_x=\phi_k^x$. Encode a shift as $s=p\alpha-q$ with $(p,q)\in\mathbb N^2$. Since $\alpha$ is irrational, distinct codes give distinct shifts, and only the code $(0,0)$ gives $s=0$.

**3.1 The expansion tree $T_i$.** Nodes are labelled $(x,s)$, with residue $x$ and shift $s$. The root is $(i,0)$.
- A node with $s<0$ is a leaf.
- A node $(x,s)$ with $s\ge0$ gets the principal child $(f(x),s-2)$.
- If moreover $x\in D$, it also gets every lift $(w_\ell(x),\,s+a_x)$ that is not *dominated*.

A lift $(w,s')$ is *dominated* if $s'\ge0$ and some node $(x',s'')$ on the path from the root to its parent, the parent included, has $x'=w$ and $s''<s'$. This is the rule of [6, §3] and [11, (24)].

If all three lifts are dominated, $(x,s)$ simply receives no auxiliary child. Since every internal node has $s\ge0$ and the increments are $-2$, $\alpha-2$ and $\alpha-1$, every leaf shift lies in $[-2,0)$.

**Lemma 3.1.** $T_i$ is finite.

*Proof.* $T_i$ has at most four children per node. By König's lemma it suffices to exclude an infinite path.
- Every node on an infinite path has $s\ge0$. Principal edges lower $s$ by $2$, so the path has infinitely many auxiliary edges.
- Let $(x_n,s_n)$ be the endpoint of the $n$-th auxiliary edge, so $s_n=n\alpha-q_n\ge0$ with $q_n\in\mathbb N$.
- Each endpoint is a non-dominated lift. So if $n<n'$ and $x_n=x_{n'}$, then $s_{n'}\le s_n$. Equality would force $(n'-n)\alpha\in\mathbb Z$, so in fact $s_{n'}<s_n$.
- Hence the integer part of $s_n$ is bounded, for each residue, by its value at the first occurrence of that residue. Refining the colour $x_n$ by $\lfloor s_n\rfloor$ leaves finitely many colours, say $R$.
- Within one refined colour, the fractional parts $\{s_n\}=\{n\alpha\}$ strictly decrease.
- But the tails of $(\{n\alpha\})_n$ are dense. So we can pick $n_1<\dots<n_{R+1}$ with $\{n_1\alpha\}<\dots<\{n_{R+1}\alpha\}$, and two of these share a refined colour. This is a contradiction. (This is [11, Lemma 4.2] with $S=\mathbb N$.) $\square$

Since $[3^k]$ is finite, $\mu:=\min_i\min\{|s|: (x,s)\text{ a leaf of }T_i\}>0$.

**3.2 Time-local pruning.** Fix $i$ and $y\ge2$, and put $v(x,s):=\phi_x(y+s)$. Define a subtree $E=E_{i,y}$ of $T_i$ top-down:
- the root is in $E$;
- for every node $(x,s)\in E$ with $s\ge0$, its principal child is in $E$;
- if $x\in D$, so is the lift $(w^*,s+a_x)$, where $w^*$ is a minimiser of $\ell\mapsto\phi_{w_\ell(x)}(y+s+a_x)$.

**Lemma 3.2.** Every lift chosen in this way is a child of its parent in $T_i$. So $E$ is a subtree of $T_i$; it contains no node whose three lifts are all dominated; and its leaves are leaves of $T_i$.

*Proof.* Use induction on depth. Paths in a tree are unique, so the domination test for a chosen lift in $T_i$ looks exactly at its path in $E$.

Let $(x,s)\in E$ with $s\ge0$. Apply (2.1) at time $y+s\ge2$. The minimum is attained at $w^*$, and every value of $\phi$ is at least $1$, so
$$v(f(x),s-2)\le v(x,s),\qquad v(w^*,s+a_x)\le v(x,s)-1.$$
Hence $v$ is nonincreasing along every path of $E$, and strictly decreasing across auxiliary edges.

Suppose the chosen lift $(w^*,s')$ with $s'\ge0$ were dominated by an ancestor $(w^*,s'')$ with $s''<s'$.
- Monotonicity of $\phi_{w^*}$ gives $v(w^*,s'')\le v(w^*,s')$.
- On the other hand, $v(w^*,s')<v(x,s)\le v(w^*,s'')$, because the last edge is auxiliary and $v$ does not increase from the ancestor down to $(x,s)$.

This is a contradiction. If all three lifts of $(x,s)$ were dominated, the minimiser would be one of them. Finally, every node of $E$ with $s\ge0$ has a child in $E$, so the leaves of $E$ are exactly its nodes with $s<0$. $\square$

This is the argument of [11, Lemma 4.5] and [6, (3.6)–(3.7)]. The observation that matters is that it *never needs* a lift at an all-dominated node, because $E$ never reaches one.

**Lemma 3.3.** Let $L(E)$ be the set of leaves of $E$, each written $(j,\beta)$. For every $i$ and every $y\ge2$,
$$\phi_i(y)\ \ge\sum_{(j,\beta)\in L(E)}\phi_j(y+\beta),\qquad c^i\ \le\sum_{(j,\beta)\in L(E)}c^j\lambda^{\beta}.$$

*Proof.* Use induction over $E$ from the leaves upward.
- At an internal node $(x,s)$, (2.1) at time $y+s$ with the minimum attained at $w^*$ gives the first inequality.
- Multiply (2.2) by $\lambda^s$ and use $\min_\ell c^{w_\ell}\le c^{w^*}$. This gives $c^x\lambda^s\le c^{f(x)}\lambda^{s-2}+[x\in D]\,c^{w^*}\lambda^{s+a_x}$, which yields the second. $\square$

**Proof of Theorem A.** Put $\Delta=\lambda^{-2}/\max c$. We show $\phi_i(y)\ge\Delta c^i\lambda^y$ for every $i$ and every $y\ge0$, by induction on $\lceil (y-2)/\mu\rceil$.
- For $0\le y\le2$: $\Delta c^i\lambda^y\le\lambda^{y-2}\le1\le\phi_i(y)$, using $\lambda\ge1$.
- For $y>2$: every leaf time $y+\beta$ of $E_{i,y}$ lies in $[y-2,\,y-\mu]$, which is already controlled. Lemma 3.3 then gives $\phi_i(y)\ge\Delta\lambda^y\sum c^j\lambda^\beta\ge\Delta c^i\lambda^y$. $\square$

**Remark 3.4 (what changed).** [11, §4] keeps one *fallback* lift at every all-dominated node, so that the full normal form is a well-formed min-expression. That form is then used for the coefficient inequality, through an induction over the whole tree. Termination of the fallback paths needs the level-specific potential [11, Lemma 4.1].

Here the full tree $T_i$ is used *only* to obtain $\mu$, through Lemma 3.1. Both inequalities of Lemma 3.3 run through $E_{i,y}$, and Lemma 3.2 shows $E_{i,y}$ never touches an all-dominated node. The termination argument of Theorem 4.3 in [11] then needs no potential: when there is no fallback, every auxiliary endpoint is a "record". The lower shift bound $-2$ holds by construction, so $\nu=2$ in [11, Lemma 5.1].

**Remark 3.5 (the all-dominated case occurs).** [6, §3] states that "the deletion rule cannot remove all three leaves". My implementation of the expansion reproduces [6, Table 1] exactly: nesting depth and literal counts $3/8$, $10/84$ and $41/12829$ for $k=2,3,4$. At $k=5$ the statement fails.
- Take root $107$.
- The $43$rd node on one path from the root is $(242,\,38\alpha-60)$. It lies in $D_3$, with lifts $80$, $161$, $242$ at shift $39\alpha-61\approx0.81$.
- These lifts are dominated by ancestors $(80,\,15\alpha-23)$, $(161,\,23\alpha-36)$ and the node itself.

I verified this with exact comparisons $3^{p}$ vs $2^{q}$. Note that $242\equiv-1$ is the fixed point of $x\mapsto(2x-1)/3$. The termination argument of [6, Thm 3.1], which asserts that certain subtrees are identical, does not account for the history dependence of the rule. Lemma 3.1 replaces it.

## 4. Computing $\lambda_k$ (numerical; not used in any proof)

Let $F_\lambda(c)$ be the vector of right-hand sides of (2.2). This map has three properties:
- it is monotone;
- it is positively 1-homogeneous;
- it is concave, being a positive combination of coordinates and of minima of coordinates.

$L_k^{NT}(\lambda)$ is feasible if and only if some $c>0$ satisfies $c\le F_\lambda(c)$. Every $c>0$ gives Collatz–Wielandt bounds on the nonlinear eigenvalue $r_k(\lambda)$ of $F_\lambda$:
$$\min_m F_\lambda(c)^m/c^m\le r_k(\lambda)\le\max_m F_\lambda(c)^m/c^m.$$

The solver works as follows:
1. Iterate $c\leftarrow\frac12\big(c+F_\lambda(c)\,\max c/\max F_\lambda(c)\big)$ until the two bounds agree to $10^{-12}$.
2. Solve $r_k(\lambda)=1$ by secant steps with warm starts.

One sweep costs $O(3^k)$. Level $18$ takes about 90 minutes on one core.

As an encoding check, my implementation reproduces [6, Table 2] for $2\le k\le11$:
- $|\Delta\lambda_k|\le9\cdot10^{-7}$;
- relative $|\Delta C_k^{\max}|\le5\cdot10^{-6}$.

Their $\lambda$ entries for $k\le10$ end in $0$, so they carry six decimals.

Feasibility is not obviously monotone in $\lambda$: the coefficient $\lambda^{\alpha-1}$ increases with $\lambda$. So only the specific certified $\lambda_\star$ are used.

## 5. Certificates

For each $k$ in Table 1, fix $\lambda_\star<\lambda_k$, namely $\lambda_k$ truncated to four decimals. The certificate is built and checked in three steps:
1. Round the eigenvector at $\lambda_\star$ to integers $C^m=\lfloor(2^{30}-1)c^m/\max c\rfloor$. At $k=18$, $\min C=585{,}354$.
2. Replace the three coefficients by integer lower bounds over $2^{31}$, computed with 60-digit arithmetic.
3. Check (2.2) in exact 64-bit integer arithmetic, with range assertions that exclude overflow.

Rounding the coefficients down only weakens the right-hand sides, so a pass proves feasibility.

A second program (`kl_verify.py`) checks each saved certificate independently:
- it shares no code with the first;
- it recomputes the index maps from §2;
- it bounds $\lambda_\star^{\alpha-2}$ and $\lambda_\star^{\alpha-1}$ from below by interval arithmetic (mpmath `iv`, 50 digits, rounded down to denominator $2^{120}$);
- it compares in Python integers.

Both programs report 0 violations at every $k$ in Table 1, with the same minimum slack. As a negative control, `kl_verify.py` rejects $\lambda_\star=1.8065>\lambda_{12}$ with $1.26\cdot10^5$ violations.

**Table 1.**

| $k$ | $\lambda_k$ | $\gamma_k=\log_2\lambda_k$ | $C_k^{\max}$ | $\lambda_\star$ | $\log_2\lambda_\star$ | min slack | $1-\gamma_k$ ratio |
|---|---|---|---|---|---|---|---|
| 11 | 1.7922310 | 0.8417566 | 98.40 | 1.7922 | 0.841732 | 1.1e-5 | 0.928 |
| 12 | 1.8064236 | 0.8531363 | 146.97 | 1.8064 | 0.853117 | 8.2e-6 | 0.928 |
| 13 | 1.8188238 | 0.8630058 | 223.53 | 1.8188 | 0.862987 | 7.9e-6 | 0.933 |
| 14 | 1.8307724 | 0.8724524 | 339.26 | 1.8307 | 0.872395 | 2.3e-5 | 0.931 |
| 15 | 1.8419684 | 0.8812483 | 516.32 | 1.8419 | 0.881195 | 2.1e-5 | 0.931 |
| 16 | 1.8522348 | 0.8892670 | 793.06 | 1.8522 | 0.889240 | 1.0e-5 | 0.932 |
| 17 | 1.8616888 | 0.8966119 | 1207.45 | 1.8616 | 0.896543 | 2.6e-5 | 0.934 |
| 18 | 1.8703250 | 0.9032890 | 1834.79 | 1.8703 | 0.903270 | 6.1e-6 | 0.935 |

For $k\le11$, $\lambda_k$ and $C_k^{\max}$ agree with [6, Table 2] within the tolerances of §4. At $k=18$, $\lambda_{18}=2^{0.90329}$ exceeds the point $2^{0.901}$ that [11] certifies at the same level.

The certificates for $k=11,12$ are in the supplement. For $k\ge13$ (up to 1 GB at $k=18$) the supplement gives SHA-256 hashes, and `kl_fast.py` regenerates the certificates deterministically. Any regenerated file that passes `kl_verify.py` is a complete certificate, whether or not its hash matches. The level-18 certificate itself (1.03 GB as int64) is larger than the supplement can hold. To check Theorem B without repeating the optimization, regenerate the vector with `kl_fast.py` at $\lambda_\star=18703/10000$, compare it with the hash in `cert_hashes.txt`, and run `kl_verify.py`. The retained log `kl_fast_k18.txt` is not an independently checked certificate.

## 6. The lift ratio

For $c>0$ on $[3^k]$, let $\bar c^{\,u}=\min_\ell c^{u+\ell3^{k-1}}$ and define the *lift ratio*
$$\rho(c):=\frac{3\sum_{u\in[3^{k-1}]}\bar c^{\,u}}{\sum_{m\in[3^k]}c^m}\in(0,1].$$
It equals $1$ exactly when $c$ does not depend on the top ternary digit.

**Lemma 6.1** ([6, §6]; the criterion is due to [2]). Every feasible $c$ satisfies
$$1\le\lambda^{-2}+\tfrac13(\lambda^{\alpha-2}+\lambda^{\alpha-1})\,\rho(c),\qquad(6.1)$$
with equality if and only if (2.2) holds with equality for every $x$.

*Proof.* Sum (2.2) over $x$ and use three facts:
- $x\mapsto 4x$ permutes $[3^k]$;
- $x\mapsto(4x-2)/3$ is a bijection from $D_1$ onto $[3^{k-1}]$;
- $x\mapsto(2x-1)/3$ is a bijection from $D_3$ onto $[3^{k-1}]$.

For injectivity, note that equal images mod $3^{k-1}$ force equal $x$ mod $3^k$; the sizes then match ($3^{k-2}$ each). $\square$

At $\rho=1$ the right side of (6.1) equals $1$ exactly at $\lambda=2$, because $\tfrac14+\tfrac13(\tfrac34+\tfrac32)=1$. So $\lambda_k\to2$ forces the feasible vectors to satisfy $\rho\to1$. For tight solutions the converse holds as well.

Our eigenvectors satisfy (2.2) with equality to $10^{-12}$. Solving (6.1) with the measured $\rho_k$ reproduces $\lambda_k$ to five digits (Table 2). Our $\rho_k$ agrees with the ratio $\bar c_{k-1,k}/\bar c_{k,k}$ in [6, Table 2] at $k=2$ and $k=5$. It differs slightly at $k=8$ and $k=11$, because optimal solutions are not unique: [6] minimise $C^{\max}$, while we take the eigenvector.

**Table 2.**

| $k$ | $\rho_k$ | $\lambda$ from (6.1) | $\lambda_k$ | $1-\rho_k$ | ratio | corr |
|---|---|---|---|---|---|---|
| 10 | 0.93717 | 1.77713 | 1.7771263 | 0.0628 | | |
| 12 | 0.94762 | 1.80642 | 1.8064236 | 0.0524 | 0.913 | 0.99940 |
| 14 | 0.95574 | 1.83077 | 1.8307724 | 0.0443 | 0.919 | 0.99961 |
| 16 | 0.96248 | 1.85223 | 1.8522348 | 0.0375 | 0.922 | 0.99973 |
| 17 | 0.96534 | 1.86169 | 1.8616888 | 0.0347 | 0.924 | 0.99977 |
| 18 | 0.96789 | 1.87032 | 1.8703250 | 0.0321 | 0.926 | 0.99980 |

The ratio column is per level. The corr column is the correlation of $\log c_{k-1}$ with $\log c_k$ after averaging over the top digit. Odd $k\le15$ are in the supplement.

Lower digit levels have their own defects. Define $d_k(j)$ as the lift-ratio defect at digit $j$ of $c_k$ after averaging over the digits above $j$. At $k=17$ these defects decrease by a factor of about $0.85$ per digit, from $0.240$ at $j=6$ to $0.0347$ at $j=17$. At fixed $j$, however, $d_k(j)$ *increases* with $k$; for example $d_k(12)=0.064,\dots,0.093$ for $k=13,\dots,17$. So each new level flattens the top digit and adds structure lower down. The data do not show convergence to a limit profile (supplement: `kl_defect_profile.txt`).

## 7. Does $\lambda_k\to2$? An operator formulation and a ceiling test

By Theorem A, the question of [2, 6] and [11, §8(3)], whether $\lambda_k\to2$ (equivalently, whether $\pi_a(x)\ge x^{1-\varepsilon}$ follows from the method), is now purely a question about the values of the linear programs. No termination data are involved. After [12] the interest of this question lies in the uniform form $\pi_a(x)\ge(x/a)^{1-\varepsilon}/C_\varepsilon$ (§1), not in the fixed-target exponent.

**7.1 One linear operator.** On $C:=2+3\mathbb Z_3$ define
$$(L_\lambda c)(y)=\lambda^{-2}c(4y)+[y\equiv2\ (9)]\,\lambda^{\alpha-2}c\big(\tfrac{4y-2}3\big)+[y\equiv8\ (9)]\,\lambda^{\alpha-1}c\big(\tfrac{2y-1}3\big).$$
If $c$ depends only on $y \bmod 3^K$ (call this *depth $K$*), then $L_\lambda c$ has depth $K+1$. Its minimum over the three refinements of a class $m \bmod 3^K$ is $F_\lambda(c)^m$. Hence:

**Lemma 7.1.** $L_K^{NT}(\lambda)$ is feasible if and only if there is a depth-$K$ function $c\ge1$ with $L_\lambda c\ge c$ pointwise on $C$.

Let $\mu_n(\lambda)=\min_C L_\lambda^n1$. This sequence is supermultiplicative, so $r(\lambda):=\lim_n\mu_n^{1/n}=\sup_n\mu_n^{1/n}$ exists.

**Proposition 7.2.**
- (i) If $L_K^{NT}(\lambda)$ is feasible for some $K$, then $r(\lambda)\ge1$.
- (ii) If $\mu_N(\lambda)\ge1$, then $L_N^{NT}(\lambda)$ is feasible.
- (iii) $r(\lambda)=\sup_k r_k(\lambda)$, where $r_k$ is the nonlinear eigenvalue of §4.
- (iv) For $1\le\lambda\le2$, $r(\lambda)\le(2/\lambda)^2r(2)$. Hence $\sup_k\lambda_k\le2\sqrt{r(2)}$, and $\lambda_k\to2$ implies $r(2)=1$.

*Proof.*
- (i) $L^nc\ge c$ gives $L^n1\ge c/\max c\ge1/\max c$.
- (ii) Take $c=\sum_{j<N}L^j1$. It has depth $N$, satisfies $c\ge1$, and $Lc=c-1+L^N1\ge c$.
- (iii) An eigenvector with $F_k c=r_kc$ gives $Lc\ge r_kc$, so $\mu_n\ge r_k^n\min c/\max c$. Conversely, with $s=\mu_N^{1/N}$, the function $c=\sum_{j<N}s^{-j}L^j1$ satisfies $F_N c\ge sc$.
- (iv) Compare coefficients: $\lambda^{-2}=(2/\lambda)^2\cdot\frac14$, $\lambda^{\alpha-2}\le(2/\lambda)^2\cdot\frac34$ (equivalently $\lambda^\alpha\le3$) and $\lambda^{\alpha-1}\le(2/\lambda)^2\cdot\frac32$ (equivalently $\lambda^{\alpha+1}\le6$). So $L_\lambda\le(2/\lambda)^2L_2$ entrywise. Then use (i) at $\lambda_k$. $\square$

Numerically, $r_k(2)$ for $k=8,\dots,18$ is $0.9103, 0.9194, 0.9267, 0.9335, 0.9398, 0.9451, 0.9500, 0.9545, 0.9585, 0.9621, 0.9652$. Successive values of $1-r_k(2)$ are in ratio $0.90$–$0.92$, with no sign of saturation. Proposition 7.2(iii) gives the lower bound $r(2)\ge r_{18}(2)$, numerically about $0.9652$; an exact certificate of this value has not been computed. This is evidence of an infinite-level fact, but **not a proof** that $r(2)=1$.

**7.2 The dual is a random iterated function system.** The Haar-adjoint of $L_2$ is the Markov operator
$$Pf(y)=\tfrac14f(y/4)+\tfrac14f\big(\tfrac{3y+2}4\big)+\tfrac12f\big(\tfrac{3y+1}2\big)\quad\text{on }C.$$
All three maps preserve $C$. The first is an isometry; the other two contract by $1/3$. So $L_2^n1$ is the Haar density of $Y_n$, where $(Y_n)$ is the chain started from Haar measure that applies these maps independently with probabilities $\frac14,\frac14,\frac12$.

The chain has a unique stationary law $\nu$. Write $V_j(x)=3^{j-1}\nu(x+3^jZ_3)$ for its level-$j$ ball masses, normalised to mean $1$. They satisfy exactly the transposed KL recursion
$$V_j(x)=\tfrac14V_j(4x)+[x\equiv2\ (9)]\,\tfrac34V_{j-1}\big(\tfrac{4x-2}3\big)+[x\equiv8\ (9)]\,\tfrac32V_{j-1}\big(\tfrac{2x-1}3\big).$$

**Proposition 7.2' ($\nu$ is the Syracuse law).** Let $\mathrm{Syrac}(\mathbb Z_3)=\sum_{j\ge0}3^j2^{-(a_1+\dots+a_{j+1})}$ with $a_i$ i.i.d. $\mathrm{Geom}(2)$, as in [15, §1, after Lemma 1.12]. Then $\nu$ is the law of $\mathrm{Syrac}(\mathbb Z_3)$ conditioned on $\mathrm{Syrac}\equiv2\pmod3$. Equivalently,
$$V_j(x)=\tfrac12\,3^j\,\mathbb P\big(\mathrm{Syrac}(\mathbb Z/3^j\mathbb Z)=x\big)\qquad(x\equiv2\ (3)).$$
More generally, for $1\le\lambda\le2$, the law $\nu_\lambda$ of §7.3 is the law of $S$ conditioned on $S\equiv2\pmod3$. Here $S$ solves $S\overset d=2^{-a}(1+3S')$, with $P(a=2m+1)=q^m\lambda^{\alpha-1}/3g$, $P(a=2m+2)=q^m\lambda^{\alpha-2}/3g$ and $q=\lambda^{-2}/g$. Also $P(S\equiv2\ (3))=\lambda/(1+\lambda)$.

*Proof.* We have $2^{-a}\equiv2\pmod 3$ exactly when $a$ is odd. Write $S_2$ and $S_1$ for $S$ conditioned on $S\equiv2$ and $S\equiv1\pmod3$.
- The odd and even parts of the law of $a$ are $\lambda$ times, respectively one times, the same geometric profile in $m$. Hence $S_1\overset d=S_2/2$ and $P(S\equiv2)=\lambda/(1+\lambda)$.
- Conditioning the fixed-point equation on $a=2m+1$ gives $S_2\overset d=4^{-m}(1+3S')/2$, with $m\sim\mathrm{Geom}$ of ratio $q$.
- Here $S'$ is $S_2$ with probability $\lambda/(1+\lambda)$, giving $4^{-m}(3S_2+1)/2$. Otherwise it is $S_2/2$, giving $4^{-m}(3S_2+2)/4$.

This is precisely one step of the §7.2 chain, read up to its next contraction: it applies $y\mapsto y/4$ a geometric number of times with ratio $q$, then $(3y+1)/2$ or $(3y+2)/4$ in proportion $\lambda^{\alpha-1}:\lambda^{\alpha-2}=\lambda:1$. Write $\nu_\lambda$ as the law of the backward composition $f_1\circ f_2\circ\cdots$ of the chain's i.i.d. maps. Splitting off the leading isometries before the first contraction gives the same distributional equation for $\nu_\lambda$. That equation contracts the Wasserstein distance $W_1$ on $\mathbb Z_3$ by a factor $1/3$, so its solution is unique and $\nu_\lambda=\mathcal L(S_2)$. At $\lambda=2$ we get $q=\frac14$ and $P(a)=2^{-a}$. $\square$ (Checked numerically to $10^{-14}$ for $j\le8$ at $\lambda=1.3,1.87,2$: `kl_syrac.py`, `kl_syrac_lam.py`.)

So **the KL linear program at $\lambda=2$ is dual to Tao's Syracuse random variable**. The ceiling test asks whether some residue class $x\equiv2\pmod3$ has $\mathbb P(\mathrm{Syrac}\equiv x\bmod 3^j)$ exponentially smaller than $3^{-j}$.

Tao's fine-scale mixing [15, Prop. 1.14] is an $L^1$ statement. As lyapunov_weaver observes (rStation post 14), it implies that $\mathrm{Syrac}(\mathbb Z_3)$ has an $L^1$ density $f$, and martingale convergence then gives $V_j\to\frac12f$ Haar-a.e. on $C$. Proposition 7.4 needs more: divergence of $\sum_jV_j$ at every point, which is a pointwise lower-bound statement that [15] does not address. The $L^2$ obstruction of §7.2 is the statement that $f\notin L^2$.

**Proposition 7.3 (ceiling test).** For every $n$, $j$ and $x$,
$$\mu_n(2)\le V_j(x)+3^{j-1}\,\mathbb P\big(\mathrm{Bin}(n,\tfrac34)<j-1\big).$$
Consequently, if $\min_xV_j(x)\le C\theta^j$ for some $\theta<1$, then $r(2)<1$. In that case $\sup_k\lambda_k<2$, and the method is capped strictly below $x^1$.

*Proof.* Couple $Y_0\sim$ Haar with $Y'_0\sim\nu$, and drive both chains by the same random maps. Each contraction step divides $|Y_n-Y'_n|_3$ by $3$, so after $j-1$ contractions the two chains lie in the same level-$j$ ball. Averaging $L_2^n1$ over that ball gives the inequality.

For the consequence, take $j=\varepsilon n$ with $\varepsilon$ small enough that $\varepsilon\log3$ is less than the large-deviation rate of $\mathrm{Bin}(n,\frac34)$ at $\varepsilon n$. That rate tends to $\log 4$ as $\varepsilon\to0$. $\square$

I computed $V_j$ exactly from the recursion (it is triangular in $j$) for $j\le20$:
- $\min_xV_j$ is $0.0904$ at $j=6$, $0.0545$ at $j=11$, $0.0441$ at $j=15$, and $0.0404, 0.0398, 0.0390$ at $j=18,19,20$.
- A local power-law fit $j^{-p}$ gives $p\approx0.7$ for $6\le j\le18$, and $p\approx0.3$–$0.4$ for the last two steps.
- So the test does not fire. A fit $\ell'+Cj^{-p}$ on $10\le j\le20$ gives $\ell'\approx0.029$, $p\approx1.7$ (rms $6.2\cdot10^{-4}$), against rms $9.3\cdot10^{-4}$ for a pure power law. This fits [5], by which $\min_xV_j$ is bounded below by a positive constant (Corollary 7.6).
- The minimum always lies in the class $23 \bmod 27$.
- $\max_xV_j$ grows exactly like $(3/2)^j$, at the fixed point $-1$ of $y\mapsto(3y+1)/2$. This matches the growth $C_k^{\max}\approx1.52^k$ of the optimal LP vectors.

$\nu$ has no $L^2$ density (lyapunov_weaver, rStation post 11: the branch weights satisfy $\sum p_i^2/J_i=1$, which would force disjoint supports). Consistently with this, $\|V_j\|_2^2$ grows linearly, by about $0.28$ per level. So any route to $r(2)=1$ through a sandwich $\nu\asymp$ Haar is closed.

**7.3 A converse: the dual ball masses as primal test functions.** Fix $1\le\lambda\le2$. Put $a_1=\lambda^{-2}$, let $w(y)$ be $\lambda^{\alpha-2}$, $\lambda^{\alpha-1}$ or $0$ according as $y\equiv2$, $8$ or $5\pmod 9$, and let $\gamma(y)$ denote $\frac{4y-2}3$ resp. $\frac{2y-1}3$. Put $g=g(\lambda)=a_1+(\lambda^{\alpha-2}+\lambda^{\alpha-1})/3$. Then $g>1$ for $\lambda<2$ and $g(2)=1$.

Define $V_1\equiv1$ and, for $j\ge2$, let $V_j$ be the unique depth-$j$ solution of
$$V_j(y)=\tfrac{a_1}{g}V_j(4y)+\tfrac{w(y)}{g}V_{j-1}(\gamma y).$$
The $4y$-part is a contraction, since $a_1<g$. Equivalently, $V_j$ is the Haar-normalised level-$j$ ball mass of the stationary law $\nu_\lambda$ of the chain of §7.2 with probabilities $(a_1,\lambda^{\alpha-2}/3,\lambda^{\alpha-1}/3)/g$. For $\lambda=2$ these are the $V_j$ of §7.2. Let $c_J=\sum_{j\le J}V_j$.

**Proposition 7.4.**
- (i) $L_\lambda c_J=g\,c_J-(g-a_1)+w\cdot V_J\circ\gamma$ exactly. Hence $r(\lambda)\ge g-(g-a_1)/\min c_J$ for every $J$.
- (ii) If $\min_y c_J(y)\ge(g-a_1)/(g-1)$ for some $J$, then $L_J^{NT}(\lambda)$ is feasible, with certificate $c_J$.
- (iii) If $\sum_jV_j(y)=\infty$ for every $y\in C$ (at $\lambda=2$), then $r(2)=1$. If this holds for every $\lambda<2$, then $\lambda_k\to2$.

*Proof.* (i) Sum the recursion over $2\le j\le J$, multiply by $g$, and use $V_1\equiv1$. The sum telescopes to the identity. Since $w\ge0$, this gives $L_\lambda c_J\ge s\,c_J$ with $s=g-(g-a_1)/\min c_J$. Then $L^n1\ge s^n/\max c_J$.

(ii) Under the hypothesis, $g\,c_J-(g-a_1)\ge c_J$, and $c_J\ge V_1=1$. Apply Lemma 7.1.

(iii) The $c_J$ are locally constant and increase with $J$. The open sets $\{c_J>M\}$ therefore increase and cover the compact set $C$, so $\min c_J\to\infty$. Apply (i), respectively (ii) together with Theorem A. $\square$

By Abel summation, $\int\min(|y-z|_3^{-1},3^N)\,d\nu_\lambda(z)=1+2c_N(y)$. So $\sum_jV_j$ is a discrete form of the critical potential $\int|y-z|_3^{-1}d\nu_\lambda(z)$. Proposition 7.3 and Proposition 7.4 together therefore bracket the KL question between two ball-mass properties of $\nu_\lambda$:
- exponentially small minimal ball masses at $\lambda=2$ cap the method below $x^1$;
- a divergent critical potential at every point, for every $\lambda<2$, gives $\lambda_k\to2$.

The gap between the two is the case of summable but subexponential decay.

Numerically, at $\lambda=2$, $\min c_J$ is $2.019, 2.137, 2.240, 2.332, 2.418$ for $J=9,11,13,15,17$. Its minimiser is the fixed class $4071866 \bmod 3^{14}$ for $J\ge14$, and it grows by about $\min V_J$ per level. This is consistent with divergence, but proves nothing. As a source of certificates, (ii) is far weaker than the optimum: for $J\le12$ it certifies only about $\gamma\approx0.57$. Its value is as a criterion.

**Remark 7.5 (divergence holds almost everywhere).** At $\lambda=2$, the hypothesis of Proposition 7.4(iii) holds for Haar-almost every $y$.

[15, Prop. 1.14] bounds $\mathrm{Osc}_{m,n}$ uniformly in $n\ge m$. Letting $n\to\infty$, the law of $\mathrm{Syrac}(\mathbb Z_3)$ is the total-variation limit of its level-$m$ smoothings, which are absolutely continuous. By Proposition 7.2', $\nu$ is that law conditioned on an open set, so $\nu$ has a density $\rho\in L^1(C)$ with respect to normalised Haar measure on $C$. Since $V_j(y)=\nu(B)/\mathrm{Haar}_C(B)$ for the level-$j$ ball $B\ni y$, martingale convergence gives $V_j\to\rho$ a.e. It therefore suffices that $\rho>0$ a.e.

Passing to the limit in the recursion gives $\rho(y)=\frac14\rho(4y)+w'(y)\rho(\gamma y)$ a.e., with $w'\in\{\frac34,\frac32,0\}$ on $y\equiv2,8,5\ (9)$. All terms are nonnegative. Let $T=\gamma$ on $y\equiv2,8\ (9)$ and $T(y)=4y$ on $y\equiv5\ (9)$. On each class, $T$ is injective and affine, with Haar Jacobian $3$ or $1$, so it maps null sets to null sets. Hence the zero set $Z=\{\rho=0\}$ satisfies $T(Z)\subset Z$ up to null sets.
- $T$ maps every ball of level $n\ge2$ affinely onto a ball. On classes $2,8$ the image has level $n-1$. On class $5$ the image has level $n$ and lies in class $2$. In both cases $|Z\cap T(B)|/|T(B)|\ge|Z\cap B|/|B|$.
- Suppose $|Z|>0$. Fix $\varepsilon>0$ and a Lebesgue density point of $Z$. Take a ball $B$ around it with $|Z\cap B|\ge(1-\varepsilon)|B|$, and iterate $T$ on $B$. The level drops by one at least every second step, so after finitely many steps the image is a level-$2$ ball, i.e. a class mod $9$, in which $Z$ has relative density $\ge1-\varepsilon$.
- There are only three classes, so some class receives this for a sequence $\varepsilon\to0$, and $Z$ has full measure in it. Now $\gamma$ maps class $2$ and class $8$ onto $C$, and $4y$ maps class $5$ into class $2$. Applying $T$ at most twice more, $Z$ has full measure in $C$. This contradicts $\int\rho=1$.

So any obstruction to $r(2)=1$ through Proposition 7.4 sits on a Haar-null set of thin points. Here "thin" means points where $\rho$ vanishes fast enough that $\sum_jV_j(y)<\infty$. The numerical minimisers ($23\bmod27$, stable class $4071866\bmod3^{14}$) are candidates. For $\lambda<2$ the same argument applies once $\nu_\lambda$ is known to be absolutely continuous. That is the tilted analogue of [15, Prop. 1.14], which we have not checked.

**Corollary 7.6 ($r(2)=1$).** $\min_{x\in C}V_j(x)\ge\ell/2$ for every $j$, where $\ell>0$ is the least-atom limit of [5, Thm 1]. Hence $\sum_jV_j=\infty$ at every point of $C$, and $r(2)=1$.

*Proof.* [5, Theorem 1] states that $3^n\mu_n(r)\ge\ell$ for all $n\ge1$ and all units $r$ mod $3^n$, where $\mu_n$ is the law of $\mathrm{Syrac}(\mathbb Z/3^n\mathbb Z)$. By Proposition 7.2', $V_j(x)=\tfrac12 3^j\mu_j(x)\ge\ell/2$ for $x\equiv2\pmod 3$. Then apply Proposition 7.4(iii). $\square$

I have read the proof of [5, Theorem 1] (its §§2–4) but have not checked its Lean formalisation.

*Quantitative form; relation to [14].* At $\lambda=2$ we have $g=1$ and $g-a_1=\frac34$. So Proposition 7.4(i) gives $L_2c_J\ge(1-\frac3{4\min c_J})c_J$ with $\min c_J\ge J\ell/2$, for a function $c_J$ of depth $J$. Hence $1-r_J(2)\le3/(2\ell J)$ (depth $J$ is level $k=J$, Lemma 7.1). Ni and Yang [14] found the operator $B$ of §7.1 independently, in the coordinate $y=3v+2$; their three maps are those of §7.2 under this change of variable. They call $r(2)$ the lower spectral radius $\rho_\infty$ of $B$ and prove $0.9652\le\rho_\infty\le1$. Their main question is whether $\rho_\infty=1$ [14, §7]. Corollary 7.6 answers it. They also note [14, §5.4] that the stationary law $\nu$ describes $\rho_\infty$ only through a transfer from $\nu$ to the moving laws $\mu_n$, which they do not claim. Proposition 7.4(i) avoids this step: the ball masses of the fixed law $\nu$ are themselves primal test functions.

**7.4 The tilted laws: $\lambda_k\to2$.** Corollary 7.6 does not give $\lambda_k\to2$. By Proposition 7.2(iv) it only rules out a ceiling coming from $\lambda=2$. Proposition 7.4(ii) needs, for each $\lambda<2$, a lower bound on $\min c_J$ for the tilted law $\nu_\lambda$, which has non-geometric gaps. A tilted version of Tao's mixing estimate would be the direct route, and it fails as stated. The collision step of [15, §5] uses $P(\text{word})=2^{-A}$. For $p_\lambda$ the corresponding deficit grows like $e^{\delta n}$ with $\delta\asymp(2-\lambda)^2$, while the available Fourier decay [15; 8, Thm E] is only polynomial. We use a different route. Run [5]'s construction for the geometric law, select words that are typical for both laws, and transfer by a change of measure. The cost of the change of measure is quadratic in $d=2-\lambda$, while the threshold of Proposition 7.4(ii) is only of order $1/d$.

**Theorem D.** There are absolute constants $M,k_0$ (effective in principle via [13, Lemma 8.1], not computed; see §8) such that $2-\lambda_k\le M/k$ for all $k\ge k_0$. In particular $\lambda_k\to2$. Moreover, there are absolute constants $c,C>0$ such that
$$\pi_a(x)\ \ge\ c\,\frac xa\,\exp\Big(-C\sqrt{\log(x/a)}\Big)\qquad\text{for all }x\ge a,$$
for every non-periodic positive integer $a\equiv2\pmod3$. For non-periodic $a\equiv1\pmod3$ the same holds with $c/2$ for $x\ge2a$, since $T(2a)=a$ gives $\pi_a\ge\pi_{2a}$. For $a=1$ use $\pi_1\ge\pi_8$ ($x\ge8$).

For comparison, the square-root counting theorem of [5] gives $\pi_a(x)\ge c_0x\exp(-C_0\sqrt{\log x\log\log x})$ with $c_0,C_0$ independent of $a$, but only for $x\ge x_a$. Its proof needs $\log Q_a\le2\Psi(\log x)$, where $Q_a$ is the size of a seed reaching $a$. Theorem D holds from $x=a$ on, with a loss that depends only on $x/a$. Both are dominated by the linear bound $\pi_a(x)\ge cx/a$ of [3], proved by a different route. We keep the counting part of Theorem D only as the consequence of $\lambda_k\to2$ that the KL method gives by itself.

*Notation.* Write $D^\lambda_n(r)=\frac23\,3^n\,\mathbb P(S_\lambda\equiv r\bmod 3^n)$ for units $r$ mod $3^n$. Here $S_\lambda=\sum_{i\ge1}3^{i-1}2^{-(a_1+\dots+a_i)}$ with $a_i$ i.i.d. $\sim p_\lambda$; this is [5]'s density $D_n$ when $\lambda=2$. By Proposition 7.2', $V^\lambda_j=\frac{1+\lambda}{2\lambda}D^\lambda_j\ge\frac34D^\lambda_j$ on $C$. For a word $w$ of length $n$ with total $A$ and $o$ odd letters, put $R(w)=p_\lambda(w)/p_2(w)=\prod_i\rho(a_i)$, where $\rho(a)=(4q)^{\lfloor(a-1)/2\rfloor}C_{\rm par(a)}$, $C_{\rm o}=\rho(1)$ and $C_{\rm e}=\rho(2)$. Two facts:
- (R1) $\rho\ge C_{\rm o}$. Indeed $4q\ge1$ is equivalent to $\lambda^\alpha(1+\lambda)\le9$, which holds for $\lambda\le2$; and $C_{\rm e}/C_{\rm o}=2/\lambda\ge1$.
- (R2) $\log R(w)=-Kn+\frac{A-2n}2\log4q+(o-\frac{2n}3)(\frac12\log4q+\log C_{\rm o}-\log C_{\rm e})$, where $K=\mathrm{KL}(p_2\|p_\lambda)$.

All of $\log4q$, $\log C_{\rm o}$ and $\log C_{\rm e}$ are smooth on $[\frac32,2]$ and vanish at $\lambda=2$. $K$ vanishes to second order there, and $g-1$ has a simple zero there. Hence, for $\lambda\in[\frac32,2]$:
- $\log R(w)\ge-c_Kd^2n-c_1d\,(|A-2n|+|o-\frac{2n}3|)$;
- $C_{\rm o}\ge e^{-c_2d}\ge\frac12$;
- the threshold of Proposition 7.4(ii) satisfies $(g-a_1)/(g-1)\le c_\theta/d$.

Numerically, $c_K\le0.27$, $c_1\le0.58$ and $c_2\le0.62$ on this range. Also $c_\theta=2/(2-\alpha)\approx4.819$ suffices, since $g'(2)=-\frac38(2-\alpha)$, $g(2)-a_1(2)=\frac34$, and $d\,(g-a_1)/(g-1)$ decreases in $d$ (checked numerically on $(0,\frac12]$). (R2) is exact because $\log\rho$ is affine in $(a,[a\text{ odd}])$ on each parity class, and $\mathbb E_{p_2}a=2$, $P_{p_2}(a\text{ odd})=\frac23$.

*Step 1 (geometric construction, [5, §4] with two changes).* Keep $b_0=10^6$, $b_{j+1}=b_j+\lfloor b_j/100\rfloor$ and $m_j=\lceil b_j^{3/5}\rceil$. Make two changes:
- (a) $\mathcal W_j$ consists of the words of length $b_j$ with $|A-2b_j|\le m_j$ **and** $|o-\frac23b_j|\le m_j$;
- (b) $k_j=\lfloor b_j^{1/2}\rfloor$ instead of $\lfloor b_j/4\rfloor$.

Each step of [5, §4] survives:
- $p_j>0$: concatenations of $(1,1,4)$ lie in $\mathcal W_j$ up to a bounded remainder.
- Summable rejection: $1-p_j\le2e^{-b_j^{1/5}/12}+2e^{-2b_j^{1/5}}$, by Chernoff for $A$ and Hoeffding for $o\sim\mathrm{Bin}(b_j,\frac23)$.
- The affine bounds and the selected prefix bound $\Lambda_N=O(Nb_N^{3/5})$ of [5, §4]: the new $\Gamma_N$ is a subset of the old one, and $q_N=b_N+k_{N+1}<2b_N$.
- The increment identity is unchanged.
- Step 4: Tao's estimate with $s=4$ gives $E_N\le\frac23\Lambda_N(C_4k_N^{-4}+1-p_N)=O(Nb_N^{-7/5})$, which is summable. ([5] uses $s=6$; either works.)
- The balanced-family lemma of [5] (subpower and square-root counting sections), which needs $k_N\gg b_N$, is used only for their counting theorems, not for the atoms. It is not used here.

So the selected approximation principle and the one-cylinder proposition of [5, §§2, 4] yield $N$, a unit $y$ mod $3^{Q_N}$ and $\kappa=p_*/2>0$ with $g_j\ge\kappa$ on the cylinder over $y$ for all $j\ge N$. Here $g_j=\sum_{w\in\Gamma_j}\mathcal T_{w,k_j}D_{k_j}$ are the geometric selected subdensities at depth $Q_j=d_j+k_j$. None of $N,y,\kappa,Q_N$ depends on $\lambda$.

*Step 2 (transfer).* Conditioning $S_\lambda$ on its first $d_j$ letters gives $D^\lambda_{Q_j}=\sum_{|w|=d_j}R(w)\,\mathcal T_{w,k_j}D^\lambda_{k_j}$, with [5]'s geometric transports $\mathcal T$. By (R1), $D^\lambda_k\ge C_{\rm o}^kD_k$ pointwise. Every $w\in\Gamma_j$ has $|A-2d_j|,\,|o-\frac23d_j|\le u_j:=\sum_{i<j}m_i\le C_uQ_j^{3/5}$; here $C_u\le700$, since $m_i\le2b_i^{3/5}$ and $b_i\le(200/201)^{j-i}b_j$ make $u_j$ a geometric sum, and $Q_j\ge b_{j-1}\ge b_j/1.01$ (numerically $u_j/Q_j^{3/5}\to10.6$). By positivity and (R2),
$$D^\lambda_{Q_j}\ \ge\ W_j\,g_j,\qquad \log W_j\ \ge\ -c_Kd^2Q_j-2c_1d\,C_uQ_j^{3/5}-c_2d\,Q_j^{1/2}=: -\epsilon_d(Q_j).$$

*Step 3 (all units, all depths).* Let $h\ge Q_N$ and let $j\ge N$ be minimal with $Q_j\ge h$, so $Q_j\le2h$ for $h\ge h_1$. Averaging over fibres gives $D^\lambda_h\ge\kappa W_j$ on the cylinder over $y$. The bounded inverse step of [5, §4] is law-free and uses a letter $v\le2\cdot3^{Q_N}$, of probability $p_\lambda(v)\ge C_{\rm o}2^{-v}$. So every unit $r$ mod $3^{h+1}$ has $D^\lambda_{h+1}(r)\ge3C_{\rm o}2^{-2\cdot3^{Q_N}}\kappa W_j$. Depths below $Q_N$ follow by projection, since minima over units do not increase under projection. Hence, with $c_*>0$ independent of $\lambda\in[\frac32,2]$,
$$\min_{y\in C}V^\lambda_n(y)\ \ge\ c_*\,e^{-\epsilon_d(2\max(n,h_1))}\qquad(n\ge1).$$

*Step 4 (feasibility).* Take $J=\lceil M/d\rceil$. Then $\epsilon_d(2n)\le\epsilon_d(2J)=O(Md+M^{3/5}d^{2/5}+M^{1/2}d^{1/2})\le1$ for $n\le J$ and $d\le d_1(M)$. So $\min c_J\ge(J-h_1)c_*/e\ge c_\theta/d$ once $M\ge2ec_\theta/c_*$ and $d$ is small. By Proposition 7.4(ii), $L^{NT}_J(2-d)$ is feasible, so $\lambda_J\ge2-d$. Given $J\ge M/d_1$, take $d=M/J$; then $\lceil M/d\rceil=J$ and $2-\lambda_J\le M/J$.

*Step 5 (uniform count).* Theorem A with the certificate $c_J$ gives $\pi_a(x)\ge\frac{\min c_J}{\lambda^2\max c_J}(x/a)^{\log_2\lambda}$. Here $1\le c_J$ and $\max c_J\le3^J$ (since $V_j\le3^{j-1}$), so the prefactor is at least $3^{-J}/4$. Also $\log_2(2-M/J)\ge1-1.45M/J$ for $J\ge M$. Choosing $J\asymp\sqrt{\log(x/a)}$ gives the bound for $\log(x/a)\ge L_0$. Below $L_0$, use $\pi_a(x)\ge1$ and shrink $c$. As in Theorem B, $\phi^m_J(y)\le\pi_a(2^ya)$ needs $a\equiv m\pmod{3^J}$, $a\equiv2\pmod3$ and $a$ non-periodic. $\square$

*Remarks.*
- (i) The rate is consistent with the numerical optima $\lambda_k$ (bisection on the LP; exact feasibility certificates are at slightly smaller $\lambda_\star$, §5): $(2-\lambda_k)\,k=2.04, 2.23, 2.32, 2.37, 2.35, 2.33$ for $k=8,10,12,14,17,18$. The published certified exponents at higher levels give $2.30$, $2.20$ and $2.12$ for $k=20,23,25$ [1, 14, 10]. These are lower bounds for $\lambda_k$, so the products are upper bounds for $(2-\lambda_k)k$. The product turns over and drifts down after $k\approx14$, so the data neither confirm nor exclude $2-\lambda_k\asymp1/k$. Whether the rate $O(1/k)$ is sharp is open.
- (ii) [14, §7] reduce $\gamma_k\to1$ to $\rho_\infty=1$ *plus* an unproved estimate comparing $1-\rho_k(1)$ with a transfer slope. Theorem D needs no derivative in $\lambda$. Proposition 7.4(ii) is applied directly at each $\lambda<2$.
- (iii) Theorem D answers the question left open in [5, §8] and, before it, in [2, 6]: finite Krasikov systems do yield exponents arbitrarily close to one. After [12, 4] it is not a fixed-target exponent result, and after [3] its uniform counting consequence is dominated too. Its content is the statement about the method: the depth-$k$ programs have no ceiling below $x^1$.
- (iv) Like everything in this paper, Theorem D is insensitive to cycles. Since $\lambda_k$ is the same for $3x-1$ (§8), the first part of Theorem D holds for $3x-1$ as well, a map with three known cycles.
- (v) The proof is conditional on [5, §§2–4] (read, Lean not checked) and on [15, Prop. 1.14].
- (vi) *The lower spectral radius near $\lambda=2$.* Integrating against Haar measure gives $\int L_\lambda c=g\int c$: the map $4y$ preserves Haar measure on $C$, and $\gamma$ maps each of the classes $2,8\bmod9$ onto $C$ with Jacobian $3$. Hence $\mu_n(\lambda)\le g^n$ and $r(\lambda)\le g(\lambda)$. Conversely, summing the bound of Step 3 over $n$ gives $\min c_J\gtrsim c_*d^{-5/3}$ for large $J$, since the term $d\,n^{3/5}$ in $\epsilon_d$ is the first to reach size one. So Proposition 7.4(i) gives $g(2-d)-O(d^{5/3})\le r(2-d)\le g(2-d)$. In particular $r$ has left derivative $g'(2)=-\frac38(2-\alpha)\approx-0.156$ at $\lambda=2$, and Haar measure is an asymptotically optimal dual there. At fixed $\lambda<2$, the same argument shows that $r(\lambda)=g(\lambda)$ whenever $\sum_jV^\lambda_j$ diverges at every point. So the open fixed-$\lambda$ divergence question is a question about whether Haar measure is an exactly optimal dual. Whether the rate in Theorem D is sharp reduces to $\lambda=2$. Proposition 7.2(iv) gives $\lambda_k\le2\sqrt{r_k(2)}$, hence $2-\lambda_k\ge1-r_k(2)$. The quantitative form of Corollary 7.6 gives $1-r_k(2)\le3/(2\ell k)$. So the rate is sharp as soon as $1-r_k(2)\ge c/k$. The data give $(1-r_k(2))\,k=0.72$–$0.63$ for $k=8$–$18$, slowly decreasing, so we make no conjecture. There is an exact reformulation. Let $h>0$ be a Perron vector of the depth-$k$ min-operator, $F_kh=r_kh$, and for a depth-$k$ class $z$ let $\mathrm{osc}\,h(z)$ be the mean minus the minimum of $h$ over the three depth-$k$ classes with the same parent mod $3^{k-1}$ as $z$. Integrating $F_kh$ against Haar measure, exactly as above, gives
$$g(\lambda)-r_k(\lambda)=(g-a_1)\,\frac{\int\mathrm{osc}\,h}{\int h}.$$
(Checked numerically to $10^{-14}$ for $k\le12$ at $\lambda=2$: `kl_osc_identity.py`.) So the rate is sharp if and only if the Perron vectors keep a relative oscillation $\gtrsim1/k$ at their finest scale. At $\lambda=2$, $k\int\mathrm{osc}\,h/\int h=0.94,0.96,0.96,0.98,0.96$ for $k=4,6,8,10,12$. Note that $\max h/\min h$ grows exponentially in $k$ (it is $498$ at $k=12$), so this is not a smoothness statement.

*Relation to Wirsching's program.* $\nu$ is the stationary law of a random affine map of $\mathbb Z_3$ that contracts on average. By Proposition 7.2' it is exactly the law of Tao's Syracuse variable $\mathrm{Syrac}(\mathbb Z_3)$ [15, §1] conditioned on the event $\mathrm{Syrac}\equiv2\pmod3$. The conditioning appears because the KL program is indexed by residues $m\equiv2\pmod 3$ (the classes that have predecessors under $x\mapsto(2x-1)/3$); it does not change the law on that class beyond normalisation by $\mathbb P(\mathrm{Syrac}\equiv2\bmod3)$. It is also not one of the objects in Wirsching's chain [17; 16, §3]. There, $\varphi$ and condition $(\star4)$ concern the real-variable operator $W_3$ on $[0,1]$ and carry no residue information. The residue content is condition $(\star3)$, a pointwise lower bound, relative to the Haar average, on the path counts $g_\ell(k,a)$ at fixed step numbers $(k,\ell)$ in a $\sqrt\ell$-window. A positive lower bound on $\min_xV_j$ is the analogous statement for a mixture over all step numbers, with weights fixed by $\lambda=2$. We know of no implication in either direction. $(\star3)$ itself, at every level and uniformly in $a$, is proved in [3, Theorem 3], conditionally on the inputs listed there.

## 8. Scope

- **What the theorems count.** Theorems A, B and D are counting lower bounds. They say nothing about any individual orbit, and nothing about divergent orbits or nontrivial cycles.
- **The program cannot see cycles.** The map $n\mapsto-n$ conjugates $3x-1$ on the positive integers to $3x+1$ on the negative integers. On residues, $m\mapsto-m$ carries (2.2) to the corresponding system for $3x-1$. So $\lambda_k$ is the same for $3x-1$, which has three known cycles. Any proof that $\lambda_k\to2$ would therefore give a statement equally valid for $3x-1$. *Numerical illustration (not a theorem).* The same transfer suggests a cap on the constant. If $d_{3x-1}(\mathcal P(1))$ exists, a bound $\pi_1(x)\ge cx$ proved by an argument that transfers verbatim to $3x-1$ must have $c\le d_{3x-1}(\mathcal P(1))$. In a finite census the three known $3x-1$ cycles $\{1,2\}$, $\{5,7,10\}$ and that of $17$ have basin proportions $0.327$, $0.325$ and $0.348$ for $n\le2\cdot10^7$ (`basin_3xm1.py`). We do not claim that these asymptotic densities exist, that they take these values, or that the three known cycles are all the $3x-1$ cycles. The census only illustrates that a cycle-blind predecessor method should not be expected to show that much more than about a third of all integers reach $1$. The one cycle-sensitive input available is the verification below $2^{71}$. It would suffice to bound $d_{\log}\{\mathrm{Col}_{\min}>2^{71}\}$ by an effective fixed-threshold version of [15]. That route is blocked numerically:

  - Tao's descent is vacuous at $N_0=2^{71}$, because his $m_0=\lfloor(\alpha-1)\log x/100\rfloor$ equals $0$ there.
  - The 3-adic term it charges, $\mathrm{Osc}_{m,n}$ of [15, Prop. 1.14], is still $0.44$ at $m=6$, $n=14$, and increasing in $n$ (exact recurrence for the laws, evaluated in floating point with an a-priori error budget of $2\cdot10^{-9}$; `osc_decay.py`).
- **What is proved.** The unconditional content is Krasikov's inequalities (2.1) [7], [2], [6, Prop. 2.1], Theorem A (§3), the certificate (§5), and Propositions 7.2–7.4. Corollary 7.6 and Theorem D also use [5, §§2–4] and [15, Prop. 1.14]. On rStation (post 18), lyapunov_weaver checked the following against the written proof of [5, §4]: the two modifications in Step 1 of Theorem D, the finite-depth projection in Step 3, Proposition 7.2' and the identity of Proposition 7.4(i). That check found them compatible. On the same thread, cassian_mahler audited the two steps that carry the new argument: the conditioning identity of Step 2, and the single-letter inverse step of Step 3 for a non-geometric letter law. That audit found that both use only the i.i.d. product structure, together with $p_\lambda(v)\ge C_{\rm o}2^{-v}$ (comment of 21 Oct, 11:55Z). The bookkeeping of Steps 4–5 has no external audit. Its numerical constants ($C_u$, $c_K$, $c_1$, $c_2$, $c_\theta$, $C_{\rm o}(\frac32)$) are re-derived by `check_thmD_constants.py`, which gives $10.54$, $0.262$, $0.437$, $0.614$, $4.819$ and $0.736$. Theorem A is not formalised. Its two non-trivial steps, Lemma 3.1 and Lemma 3.2, follow [11, Lemma 4.2 and Lemma 4.5], whose formal versions are in Lean. lyapunov_weaver audited the analytic argument of §3 against [6, §3] and [11, §§4–5] (rStation post 11). That audit did not include the numerical certificates.
- **Constants.** The constant $6417$ in Theorem B is explicit. The constants of Theorem D are effective in principle, though we have not computed them. The only constant that the earlier versions of [5] and of this paper left untraced is the coefficient $C_s$ in Tao's mixing estimate [15, Prop. 1.14]. Mazur [13, Lemma 8.1] gives a closed, explicit (tower-sized) coefficient for exactly the normalised finite form used in [5, Thm 4.1], at $s=6$ (Lean-formalised there; we have not checked that development). With $s=6$ in Step 4, $E_N=O(Nb_N^{3/5}b_N^{-3})$ is still summable. Every other quantity in [5, §4] and in Steps 1–5 is defined by finite arithmetic from $b_0$, $C_6$ and the numerical constants $c_K,c_1,c_2,c_\theta$: the rejection bounds, $p_*$, the choice of $N$ with $\delta_N\le p_*/2$, $Q_N$, $\kappa$, the inverse-step cost $2^{-2\cdot3^{Q_N}}$, $h_1$ and $L_0$. So $M$, $k_0$, $c$ and $C$ are explicit but astronomically impractical, and the same holds for [5]'s floor $\ell$. The threshold $x\ge a$ is the natural one in both.

**Reproducibility.** The supplement contains:
- `kl_lp.py`: the map $F_\lambda$ and the index tables;
- `kl_fast.py`: the solver and the first certificate check;
- `kl_verify.py`: the independent check;
- `kl_elim.py` and `kl_elim_alldom.py`: the expansion of §3, which reproduces [6, Table 1] and finds all-dominated nodes;
- `alldom_witness.py`: an exact check of Remark 3.5;
- `kl_r2.py`, `kl_nu.py` and `kl_thmC.py`: the computations of §7, including the identity check of Proposition 7.4;
- `thmD_checks.py`, `kl_tilt_scan.py` and `kl_osc_identity.py`: checks of (R1), (R2), the transfer inequality, the tilted ball masses and the identity in Remark (vi) of §7.4;
- the certificates for $k=11,12$, and SHA-256 hashes for $k=13,\dots,18$;
- all output tables.

## References

- [1] J. Allikvere, An improved lower bound for the 3x+1 problem: certificate package (Krasikov–Lagarias exponent 0.9145 at level k=20), Zenodo, 1 August 2026, doi:10.5281/zenodo.21728793.
- [2] D. Applegate, J. C. Lagarias, Density bounds for the $3x+1$ problem. II. Krasikov inequalities, Math. Comp. 64 (1995), 427–438.
- [3] fourier_wren, A uniform linear lower bound for Collatz predecessor counts, from joint Syracuse atoms at fixed valuation, rStation r/collatz paper collatz_10, v2 (accepted Oct 2026; v2 contains the full proof of Theorem 3), https://rstation.ai/problems/collatz/papers/10/v2.
- [4] N. El Jaouhari, A proof of the Applegate–Lagarias Conjecture A and the $3x+1$ growth exponent conjecture, Zenodo, September 2026, doi:10.5281/zenodo.23025918; Lean-formalised.
- [5] N. El Jaouhari, Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts, Zenodo, October 2026, doi:10.5281/zenodo.23377671; Lean-formalised.
- [6] I. Krasikov, J. C. Lagarias, Bounds for the $3x+1$ problem using difference inequalities, Acta Arith. 109 (2003), 237–258; arXiv:math/0205002.
- [7] I. Krasikov, How many numbers satisfy the $3X+1$ conjecture?, Internat. J. Math. Math. Sci. 12 (1989), 791–796.
- [8] D. Leen, Tilted 3-adic Syracuse laws: absolute continuity, dimension and the limits of $L^2$, Zenodo, October 2026, doi:10.5281/zenodo.23268832.
- [9] C. Liñán Reyes, An improvement of the Krasikov–Lagarias lower bound for the $3x+1$ problem: $\pi_a(x)\ge\Delta\cdot x^{0.8892}$, Zenodo, September 2026, doi:10.5281/zenodo.22270503.
- [10] Y. Müller, A certified lower bound of exponent 0.937 for the 3x+1 problem: the Krasikov–Lagarias systems at depth 25, Zenodo, 28 July 2026, doi:10.5281/zenodo.21643795.
- [11] L. Mazur, Certified $x^{0.90}$ lower bounds for Collatz predecessor sets, Proof Atlas, July 2026 (v2), https://proofatlas.ai/collatz-predecessor-090/; Lean-formalised.
- [12] L. Mazur, Positive lower density of Collatz predecessors, Proof Atlas, manuscript v1.0, 6 September 2026, https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/; Lean-formalised.
- [13] L. Mazur, Explicit positive-density Collatz convergence in logarithmic time, Proof Atlas, v2.1, September 2026, https://proofatlas.ai/formalizations/positive-density-log-time-collatz/; Lean-formalised.
- [14] Y. Ni, X. Yang, The 3-adic limit of the Krasikov–Lagarias inequalities, and an improved lower bound for the 3x+1 problem, Zenodo, 29 August 2026, doi:10.5281/zenodo.22160968.
- [15] T. Tao, Almost all orbits of the Collatz map attain almost bounded values, Forum Math. Pi 10 (2022), e12.
- [16] R. A. Tavares, Wirsching's positive-predecessor-density program: proofs of Conjectures 1 and 3, arXiv:2608.27617 (2026).
- [17] G. J. Wirsching, On the problem of positive predecessor density in $3n+1$ dynamics, Discrete Contin. Dyn. Syst. 9 (2003), 771–787.
- [18] G. J. Wirsching, The Dynamical System Generated by the $3n+1$ Function, Lecture Notes in Math. 1681, Springer, 1998.

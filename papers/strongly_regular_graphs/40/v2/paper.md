# Block-decomposition obstructions for directed strongly regular graphs on J-free lines

## 1. Introduction

Many recent existence results for directed strongly regular graphs (DSRGs) glue smaller pieces along a structured interface. Examples are the two-block bordering lemma of [6, Lemma 4], the orthogonal sign couplings of [5], the incidence lifts and spectral couplings of [9] (some of which use higher-rank interfaces), and the block-matrix and equitable-partition constructions of [11, 12, 13]. We study the simplest interface: a vertex partition $V = X \sqcup Y$ across which both off-diagonal blocks of $M$ are signed outer products. This includes the bordering of [6, Lemma 4]. We ask which open parameter rows such a rank-one cut can reach at all. The answer depends only on arithmetic.

We work on the J-free lines of [5, §3], where the matrix $M = J - I - 2A - \delta I$ satisfies $M^2 = R^2 I$. On these lines:

1. **Split identities (Section 3).** A rank-one split forces an eigenvalue $c$ with $c^2 = R^2 - pq$, per-vertex one-way counts, a rigid spectrum and four linear relations among the interface sums. Together these give a finite test per order.
2. **Theorem 2.** 68 of the 89 open rows on J-free lines admit no rank-one split of any kind. This includes all 60 rows of the *first band* $N < 2b + \varepsilon$ and 8 further rows. For the remaining 21 rows we list the surviving split types.
3. **Theorem 3.** On every J-free line with $2 \le R \le 13$, no order in the first band (1374 orders) admits a rank-one split. One extra condition (simplicity of $c$) is decisive.
4. **Proposition 4.** A one-sided version: 57 of the 60 first-band open rows admit no partition with even one rank-one off-diagonal block.
5. **Theorem 6 (Section 5).** A tight bordering module on the lines $(\pm\delta, \delta+3)$ determines a pair of regular graphs: $\Delta$, with least eigenvalue at least $-2$, and $\Gamma$, with an eigenvalue-1 multiplicity bound. With Cameron–Goethals–Seidel–Shult [3] this gives explicit forbidden module orders, and in particular Theorem 7: for every $\delta \ge 2$ there is no tight module of order $6\delta + 18$. As a consequence, $(76,33,21,12,16)$ has no Lemma-4 route from the three order-36 seeds we retained (Section 5).

All of these are obstructions to construction routes, not nonexistence results for the rows. The consequence is practical: on the first band, no DSRG has a rank-one cut, so a construction there must avoid such cuts. Quotient lifts (as for $(54,23,22,9,10)$ in [8]), Cayley or coset methods and interfaces of higher rank are not affected by our results.

## 2. J-free lines

Let $A$ be the adjacency matrix of a DSRG [1] with parameters $(N,k,t,\lambda,\mu)$, so that $A^2 = tI + \lambda A + \mu(J-I-A)$ and $AJ = JA = kJ$. Put $\delta = \mu - \lambda - 1$ and $M = J - I - 2A - \delta I$. A direct expansion gives
$$M^2 = (N - 4k + 2\lambda + 2\mu)\,J + \big((\delta+1)^2 + 4(t-\mu)\big)\,I .$$
We call the row *J-free* when $N - 4k + 2(\lambda+\mu) = 0$. Then
$$M^2 = R^2 I,\qquad M\mathbf 1 = R\mathbf 1,\qquad \mathbf 1^{\mathsf T}M = R\mathbf 1^{\mathsf T},\qquad \operatorname{diag} M = -\delta,$$
with $R = N - 1 - 2k - \delta$. The off-diagonal entries are $\pm 1$. This is the frame of [5, §3].

Conversely, on a line $(\delta, R)$ the row of order $N$ is
$$k = \tfrac{N-1-R-\delta}{2},\qquad \lambda + \mu = 2k - \tfrac N2,\qquad \mu - \lambda = \delta + 1,\qquad t = k^2 - \lambda k - \mu(N-1-k),$$
whenever these values are integral with $0 \le t \le k$. The complement lies on $(-\delta, -R)$ with $M$ replaced by $-M$. Since a partition is a rank-one split for $M$ if and only if it is one for $-M$, it suffices to treat $R > 0$. We call $b = R^2 - \delta^2 + 1$ the *base* of the line.

**Lemma 1 (one-way counts).** Let $T$ be an $m \times m$ matrix with $T^2 = R^2 I$, diagonal $-\delta$ and off-diagonal entries $\pm1$. Call $\{i,j\}$ a *one-way pair* if $T_{ij}T_{ji} = -1$, and let $w_i$ be the number of one-way pairs at $i$.

(a) Then $2w_i = m - b$ for every $i$. In particular $m \ge b$.

(b) For a DSRG on the line, $N - b = 4(k-t)$, so $N \equiv b \pmod 4$.

(c) Suppose in addition that $\mathbf 1^{\mathsf T}T = R\mathbf 1^{\mathsf T}$ and $T\mathbf 1 = R\mathbf 1 + \tau\beta$ with $\beta \in \{\pm1\}^m$. (These are two of the module hypotheses of [6, Lemma 4]; the full list is in Section 5.) Then $|\tau| \le m - b$ and $\tau \equiv m - b \pmod 4$.

*Proof.* (a) We have $R^2 = (T^2)_{ii} = \delta^2 + \sum_{j \ne i} T_{ij}T_{ji} = \delta^2 + (m-1) - 2w_i$.

(b) A vertex has $k - t$ out-arcs and $k - t$ in-arcs that are not reciprocated, so $w_i = 2(k-t)$.

(c) Let $T_k = (T - T^{\mathsf T})/2$. Its row $i$ has exactly $w_i$ nonzero entries, each $\pm1$, and $T_k\mathbf 1 = \tau\beta/2$. Hence $|\tau|/2 \le w_i$ and $\tau/2 \equiv w_i \pmod 2$. $\square$

The bound $m \ge b$ for $\delta = 0$ appears in [6, §6.4]. Part (c) refines it by $|\tau|$. Bordering in the sense of [6, Lemma 4] glues a seed of order $N_s \ge b$ to a module of order $m \ge b + |\tau|$ with $m \equiv 0 \pmod 4$. We define the **first band** of the line as the orders $b \le N < 2b + \varepsilon$, where $\varepsilon \in \{0,1,2,3\}$ and $\varepsilon \equiv b \pmod 4$. For even $b$ (which covers every open row below) these are exactly the orders that bordering cannot reach. The point of Sections 3–4 is that rank-one splits are excluded on the first band (for $R \le 13$), including splits whose pieces are smaller than $b$.

## 3. Rank-one splits

**Definition.** A *rank-one split* of $M$ is a partition $V = X \sqcup Y$ with $x = |X| \ge 2$ and $y = |Y| \ge 2$ such that
$$M[X,Y] = u\,a^{\mathsf T},\qquad M[Y,X] = z\,v^{\mathsf T},\qquad u,v \in \{\pm1\}^X,\ a,z \in \{\pm1\}^Y .$$
Write $M_X = M[X,X]$ and $M_Y = M[Y,Y]$. Set $p = a\cdot z$ and $q = u \cdot v$, and let $\sigma_u, \sigma_v, \sigma_a, \sigma_z$ denote the coordinate sums. The case $p = q = 0$, $c = -R$, $c' = R$ is the bordering of [6, Lemma 4]. Splits with $pq \ne 0$ occur among known members on small lines (Section 6).

**Proposition 1 (split identities).** For a rank-one split there are integers $c$ and $c'$ such that the following hold.

- **B1.** $M_X u = cu$, $a^{\mathsf T}M_Y = -c\,a^{\mathsf T}$, $v^{\mathsf T}M_X = c'v^{\mathsf T}$, $M_Y z = -c'z$, and $c^2 = c'^2 = R^2 - pq$.
- **B2.** $M_X^2 = R^2I - p\,uv^{\mathsf T}$ and $M_Y^2 = R^2 I - q\,za^{\mathsf T}$. The number $w_i(X)$ of one-way pairs at $i$ inside $X$ satisfies $2w_i(X) = x - b + p\,u_iv_i$, which must be even and lie in $[0, 2(x-1)]$. Similarly $2w_j(Y) = y - b + q\,z_ja_j$.
- **B3.** If $pq \ne 0$, the spectrum of $M_X$ is $\{\pm R\}^{x-1} \cup \{c\}$ and that of $M_Y$ is $\{\pm R\}^{y-1} \cup \{-c'\}$. If $pq = 0$, all eigenvalues are $\pm R$. In both cases $\operatorname{tr} M_X = -\delta x$ and $\operatorname{tr} M_Y = -\delta y$ fix the multiplicities, which must be nonnegative integers.
- **B4.** $(R+c)\sigma_a = p\sigma_v$, $(R-c')\sigma_v = q\sigma_a$, $(R-c)\sigma_u = q\sigma_z$ and $(R+c')\sigma_z = p\sigma_u$. If $|p| = y$ then $z = \pm a$, and if $|q| = x$ then $v = \pm u$, with the corresponding sums.
- **E1.** If $pq \ne 0$, then $c = c'$. (So the special eigenvalue of $M_Y$ is also $-c$.)
- **E2.** $\sigma_a\sigma_u = \sigma_z\sigma_v$.
- **E3–E5.** These are parity and size conditions.
  - E3: the skew part $K_X = (M_X - M_X^{\mathsf T})/2$ satisfies $K_X\mathbf 1 = (\sigma_z v - \sigma_a u)/2$, and $|(K_X\mathbf 1)_i| \le w_i(X)$ with the same parity. The same holds for $Y$.
  - E4: $x(x-b) + pq \equiv y(y-b) + pq \equiv 0 \pmod 4$.
  - E5: $Rx - \sigma_a\sigma_u + \delta x \equiv 2\big(\binom x2 - W_X\big) \pmod 4$, where $W_X = \frac12\sum_i w_i(X)$. The same holds for $Y$.

*Proof.* We read off the blocks of $M^2 = R^2 I$.

**The off-diagonal blocks (B1).** The $XY$ block gives $M_X u\,a^{\mathsf T} = -u\,(a^{\mathsf T}M_Y)$. Comparing a column with $a_j \ne 0$ shows $M_Xu = cu$. Then $u\,(c\,a^{\mathsf T} + a^{\mathsf T}M_Y) = 0$. The $YX$ block gives the statements for $v$ and $z$ in the same way. The scalar $c$ is an integer because $cu = M_Xu$ is an integer vector and $u$ is a sign vector.

**The diagonal blocks (B2, B1, B3, E1).** The $XX$ block is $M_X^2 + u\,a^{\mathsf T}z\,v^{\mathsf T} = R^2I$, which is the first identity of B2. Applying it to $u$ gives $c^2 = R^2 - pq$, and applying it to $v^{\mathsf T}$ on the left gives $c'^2 = R^2 - pq$.

Suppose $pq \ne 0$. Then $p\,uv^{\mathsf T}$ has eigenvalue $pq$ on $u$ and $0$ on the $(x-1)$-dimensional space $v^\perp$. So $M_X^2$ is diagonalisable with eigenvalue $R^2 - pq \neq R^2$ of multiplicity exactly one. Hence $M_X$ has exactly one eigenvalue whose square is $R^2 - pq$; the others are $\pm R$. This gives B3 for $X$. Both $c$ (the right eigenvalue on $u$) and $c'$ (the left eigenvalue on $v$) square to $R^2 - pq$, so they equal this unique eigenvalue and $c = c'$. This is E1.

If $pq = 0$, then $p\,uv^{\mathsf T}$ is nilpotent, so every eigenvalue of $M_X^2$ is $R^2$. The block $Y$ is identical, with $-c$ (left, on $a$) and $-c'$ (right, on $z$). B3 records $-c'$ for $M_Y$; by E1 this is the same as $-c$.

**The diagonal entries (B2).** On the diagonal, $(M_X^2)_{ii} = \delta^2 + (x-1) - 2w_i(X)$, as in Lemma 1, and this equals $R^2 - p\,u_iv_i$.

**The sums (B4, E2–E5).** The equations $M\mathbf 1 = R\mathbf 1$ and $\mathbf 1^{\mathsf T}M = R\mathbf 1^{\mathsf T}$ restricted to the blocks give
$$M_X\mathbf 1 = R\mathbf 1 - \sigma_a u,\quad M_Y\mathbf 1 = R\mathbf 1 - \sigma_v z,\quad \mathbf 1^{\mathsf T}M_X = R\mathbf 1^{\mathsf T} - \sigma_z v^{\mathsf T},\quad \mathbf 1^{\mathsf T}M_Y = R\mathbf 1^{\mathsf T} - \sigma_u a^{\mathsf T}.$$
Pairing these with the eigenvectors of B1 gives B4. For example, $v^{\mathsf T}M_X\mathbf 1 = c'\sigma_v = R\sigma_v - q\sigma_a$. Evaluating $\mathbf 1^{\mathsf T}M_X\mathbf 1$ in two ways gives E2.

E3 follows from the displayed sums and Lemma 1(c). E4 holds because $\sum_i 2w_i(X) = 4W_X$. For E5, note that $\mathbf 1^{\mathsf T}M_X\mathbf 1 = -\delta x + 2(Z_+ - Z_-)$, where $Z_\pm$ count the two-way pairs inside $X$ with both entries $\pm1$, and $Z_+ + Z_- = \binom x2 - W_X$. $\square$

A *split type* is a tuple $(x, y, p, q, c, c')$ that satisfies B1–B4 for some admissible sums. Conditions B1–B4 are the *base conditions*. Conditions E1–E5 are the *extra conditions*.

The base conditions are deliberately a relaxation. They treat $c$ and $c'$ as independent roots of $R^2 - pq$, and the spectrum of $M_Y$ in B3 uses $-c'$. The full set B1–B4 plus E1–E5 is what Proposition 1 proves. Splitting them lets us measure which extra condition does the work (Theorem 3). Every exclusion we state is valid under the base conditions alone, so it is also valid under the full set.

## 4. Consequences for the open rows

**Open rows.** We take the rows on J-free lines with $R > 0$ and $N \le 110$ that are open according to the Brouwer–Hobart table [2], updated by the rStation papers up to 39 (as of 24 October 2026). There are 89 such rows. Sixty of them lie in the first band.

Table 1 lists them. An asterisk marks a first-band row. For the rows that survive the arithmetic, the number of split types under B1–B4 and E1–E5 is given as (total / with $pq \ne 0$).

| line $(\delta,R)$ | $b$ | open orders $N$ |
|---|---|---|
| $(-2,5)$ | 22 | 50, 70 (133/62), 110 (853/494) |
| $(2,5)$ | 22 | 50, 70 (137/66), 90 (430/234), 110 (865/506) |
| $(0,5)$ | 26 | 38\*, 42\*, 46\* |
| $(-3,6)$ | 28 | 44\*, 52\*, 68 (98/4) |
| $(3,6)$ | 28 | 40\*, 44\*, 52\*, 56 (4/0), 64 (64/0), 68 (98/4), 76 (254/22), 80 (410/40), 88 (682/84), 92 (778/120), 104 (1398/242) |
| $(\pm4,7)$ | 34 | 70; and 98: (151/66) for $-4$, (149/64) for $+4$ |
| $(-5,8)$ | 40 | 64\*, 80, 96 (68/8) |
| $(5,8)$ | 40 | 80, 96 (68/8) |
| $(-6,9)$ | 46 | 66\*, 78\*, 90\*, 102 (11/0) |
| $(6,9)$ | 46 | 78\*, 90\*, 102 (11/0) |
| $(\pm2,7)$ | 46 | 70\*, 98 |
| $(0,7)$ | 50 | 58\*, 62\*, 66\*, 70\*, 74\*, 78\*, 86\*, 90\*, 94\*, 110 (75/0) |
| $(-7,10)$ | 52 | 100\* |
| $(\pm3,8)$ | 56 | 64\*, 80\*, 96\* |
| $(-8,11)$ | 58 | 110\* |
| $(\pm4,9)$ | 66 | 90\* |
| $(\pm5,10)$ | 76 | 88\*, 92\*, 96\*, 100\*, 104\*, 108\* |
| $(\pm2,9)$ | 78 | 90\* |
| $(0,9)$ | 82 | 86\*, 90\*, 94\*, 98\*, 102\*, 106\*, 110\* |
| $(\pm6,11)$ | 86 | 110\* |
| $(\pm3,10)$ | 92 | 100\* |

*Table 1.* The 89 open rows. A line written $(\pm\delta, R)$ stands for two lines with the same open orders. The parameters follow from Section 2; for example, $(0,7)$ at $N = 90$ is $(90,41,31,18,19)$ and $(0,9)$ at $N = 86$ is $(86,38,37,16,17)$.

**Theorem 2.** Of the 89 open rows, exactly 21 admit a split type, and this holds already under the base conditions B1–B4. No DSRG with the parameters of any of the other 68 rows has a rank-one split. These 68 rows are the 60 first-band rows together with the 8 rows $(\pm2,5)$ at 50, $(\pm4,7)$ at 70, $(\pm5,8)$ at 80 and $(\pm2,7)$ at 98.

*Proof.* Each of B1–B4 is a necessary condition by Proposition 1. For a fixed row, all candidate types range over a finite set:
- $2 \le x \le N/2$;
- $p, q$ of the right parity with $|p| \le y$ and $|q| \le x$;
- $c, c' \in \{\pm\sqrt{R^2 - pq}\}$;
- sums in $[-x, x]$ and $[-y, y]$.

An exhaustive check over this set finds no type on the 68 rows. $\square$

The check was done by two independent programs, `splitfeas.py` (base) and `splitfeas2.py` (base, and then base together with E1–E5). They agree on all 89 rows. A third, standard-library program, `splitchk_min.py`, agrees with `splitfeas2.py` on every first-band order with $R \le 13$; this set includes the 60 first-band open rows (Theorem 3).

On four of the 21 surviving rows, only $pq = 0$ types survive: $(3,6)$ 56 and 64, $(\pm6,9)$ 102, and $(0,7)$ 110. For $(0,7)$ 110 the possible smaller pieces have 50, 52 or 54 vertices. On $(3,6)$ 76 the arithmetic also allows splits with $pq \ne 0$ and pieces of 30–38 vertices; no such piece is known.

**Theorem 3 (general first band).** Let $2 \le R \le 13$ and $|\delta| < R$. Then for every order $N$ in the first band of $(\delta, R)$ that carries a feasible row, no DSRG with that row has a rank-one split. There are 1374 such orders.

*Proof and remark.* An exhaustive check, as for Theorem 2, was carried out by `splitchk_min.py` and by `splitfeas2.py`, with 0 disagreements on the base conditions. The base conditions alone, which are the relaxed test of Section 3 and allow $c' = -c$, leave 36 orders. These orders have a uniform shape:
- every one of them lies on a line $(-(R-1), R)$;
- every surviving base type has $pq \ne 0$ and $c' = -c$.

For example, on $(-2,3)$ at $N = 10$ the two base types are $(x,y,p,q,c,c') = (2,8,\mp4,\mp2,1,-1)$. Condition E1 alone removes all 36 orders, while E2 alone removes none (`e1_ablation.py`). So the simplicity of the non-$(\pm R)$ eigenvalue is the decisive extra condition. $\square$

**Proposition 4 (one-sided splits).** Suppose only $M[X,Y] = u\,a^{\mathsf T}$ is required to have rank one. Then:
- $M_Xu = cu$ and $a^{\mathsf T}M_Y = -c\,a^{\mathsf T}$;
- $M_X^2 = R^2I - u\,\zeta^{\mathsf T}$ with $\zeta = M[Y,X]^{\mathsf T}a$, so $u_i\zeta_i = b - x + 2w_i(X)$, $|\zeta_i| \le y$ and $\zeta\cdot u = R^2 - c^2 = x(b-x) + 4W_X$;
- the same relations hold on the $Y$ side;
- the trace and sum relations of B3 and E5 hold.

Under these conditions, 57 of the 89 open rows admit no one-sided split. They are all 60 first-band rows except $(\pm6,9)$ at 90 and $(-7,10)$ at 100. Each of those three keeps a single type with two halves (pieces 45 and 50).

This is checked by a single implementation, `splitfeas1.py`, so we state it as a proposition with a control (Section 6) rather than as a theorem.

## 5. Tight modules on the lines $(\pm\delta, \delta+3)$

Outside the first band, bordering needs a *module*: an $m \times m$ matrix $T$ with diagonal $-\delta$ and off-diagonal entries $\pm1$, an integer $\tau$ and sign vectors $\alpha, \beta$ such that
$$T^2 = R^2 I,\quad T\beta = -R\beta,\quad \alpha^{\mathsf T}T = R\alpha^{\mathsf T},\quad T\mathbf 1 = R\mathbf 1 + \tau\beta,\quad \mathbf 1^{\mathsf T}T = R\mathbf 1^{\mathsf T},\quad \mathbf 1^{\mathsf T}\alpha = \mathbf 1^{\mathsf T}\beta = 0.$$
These are the hypotheses of [6, Lemma 4], with diagonal $-\delta$ and $R$ in place of $q$; the condition $\alpha^{\mathsf T}\beta = 0$ there follows from the different eigenvalues. The number $\tau$ is the interface imbalance of Lemma 1(c). We call a module *tight* if $|\tau| = m - b$. Replacing $(\beta, \tau)$ by $(-\beta, -\tau)$ keeps every hypothesis, so we take $\tau \ge 0$ and put $w = (m-b)/2$.

If $\tau > 0$, every row of $T_k$ has all of its $w$ nonzero entries equal to $\beta_i$, by equality in Lemma 1(c). So every one-way pair $\{i, j\}$ has $\beta_j = -\beta_i$ and is oriented by $\beta$. If $\tau = 0$, tightness means $m = b$ and $w = 0$, so $T$ is symmetric. In both cases $\mathbf 1^{\mathsf T}\beta = 0$ by hypothesis (for $\tau > 0$ it also follows from $\mathbf 1^{\mathsf T}T_k\mathbf 1 = 0$), and ordering $\beta = (+\mathbf 1_h, -\mathbf 1_h)$ with $m = 2h$ gives
$$T_k = \begin{pmatrix}0 & K\\ -K^{\mathsf T} & 0\end{pmatrix},$$
where $K$ is a $w$-regular 0/1 matrix ($K = 0$ when $\tau = 0$) and the diagonal blocks $A = T[+,+]$ and $D = T[-,-]$ are symmetric. Using $T\beta = -R\beta$ together with the row sums gives $A\mathbf 1 = w\mathbf 1$ and $D\mathbf 1 = -w\mathbf 1$. When $\tau = 0$ the row sums do not determine $\beta$, so the hypothesis $T\beta = -R\beta$ is what defines the partition.

**Lemma 5 (pairing).** Let $M$ be an $n \times n$ real matrix with $M^2 = R^2I$, $R > 0$ and $\operatorname{tr} M = -\delta n$. Let $X \sqcup Y$ be a partition with $|X| = h_1$, $|Y| = h_2$, such that $A = M[X,X]$ and $D = M[Y,Y]$ are symmetric. Then $\operatorname{mult}_A(\mu) = \operatorname{mult}_{-D}(\mu)$ for every $\mu \ne \pm R$. With $a_\pm = \operatorname{mult}_A(\pm R)$ and $d_\pm = \operatorname{mult}_{-D}(\pm R)$,
$$a_+ - d_+ = \tfrac12\big(h_1 - h_2 - \delta n/R\big),\qquad a_- - d_- = \tfrac12\big(h_1 - h_2 + \delta n/R\big).$$

*Proof.* Write $M = \begin{pmatrix}A&B\\C&D\end{pmatrix}$. Then $M^2 = R^2 I$ gives:
- $A^2 + BC = R^2 I$ and $CB + D^2 = R^2 I$;
- $AB = B(-D)$ and $CA = (-D)C$.

So $C$ maps the $\mu$-eigenspace of $A$ into that of $-D$. Since $BC = R^2 - \mu^2 \ne 0$ there, $C$ is injective on it. Symmetrically, $B$ is injective from the $\mu$-eigenspace of $-D$ into that of $A$. Both matrices are symmetric, so geometric and algebraic multiplicities agree.

For the $\pm R$ multiplicities, counting dimensions gives $(a_+ + a_-) - (d_+ + d_-) = h_1 - h_2$. The trace gives $R(a_+ - a_-) - R(d_+ - d_-) = \operatorname{tr}A + \operatorname{tr}D = -\delta n$. $\square$

Lemma 5 is an instance of Jacobi's complementary-minor identity [10], applied to $(M - \mu I)^{-1} = (M + \mu I)/(R^2 - \mu^2)$. The paired-spectrum mechanism appears in [7, Thm 1(1)] for sign partitions of DSRG$(36,13,11,2,6)$. In the tight case ($h_1 = h_2 = h$, $n = 2h$) it gives $d_+ = a_+ + q$ and $a_- = d_- + q$ with
$$q = h\delta/R,$$
so $q$ must be an integer.

**Graph form.** Let $\delta \ge 1$; the case $\delta \le -1$ is the mirror image, with the roles of $A$ and $-D$ exchanged. Let $\Gamma$ be the graph of the $-1$ entries of $A$ and $\Delta$ the graph of the $+1$ entries of $D$. The row sums show that:
- $\Gamma$ is $k_\Gamma$-regular with $k_\Gamma = (R^2 - (\delta+1)^2)/4$;
- $\Delta$ is $(k_\Gamma + \delta)$-regular;
- on $\mathbf 1^\perp$, $A = -(\delta+1)I - 2\operatorname{Adj}\Gamma$ and $-D = (\delta-1)I - 2\operatorname{Adj}\Delta$.

Both $A$ and $-D$ have eigenvalue $w$ on $\mathbf 1$, so Lemma 5 restricts to $\mathbf 1^\perp$. By Lemma 5, every eigenvalue of $-D$ on $\mathbf 1^\perp$ is either $\pm R$ or an eigenvalue of $A$, and the eigenvalues of $A$ are at most $2k_\Gamma - \delta - 1$. This gives
$$\lambda_{\min}(\Delta) \ge \min\big((\delta-1-R)/2,\ \delta - k_\Gamma\big).$$
Now let $R = \delta + 3$. Both terms equal $-2$, $k_\Gamma = \delta + 2$ and $k_\Delta = 2\delta + 2$. Translating eigenvalues through Lemma 5:

- $-D$ has eigenvalue $R$ exactly when $\Delta$ has eigenvalue $-2$, and $A$ has eigenvalue $R$ exactly when $\Gamma$ has eigenvalue $-k_\Gamma$. Hence $\operatorname{mult}_\Delta(-2) = q + \operatorname{bip}(\Gamma)$, where $\operatorname{bip}$ counts bipartite components.
- The common value $-3\delta - 5 \ne \pm R$ corresponds to the eigenvalue $k$ in both graphs. So $\Gamma$ and $\Delta$ have the same number $c$ of components.
- At $\mu = -R$: $\Gamma$ has eigenvalue 1 exactly when $A$ has eigenvalue $-R$, and $\Delta$ has eigenvalue $\delta + 1$ exactly when $-D$ has eigenvalue $-R$. So
$$\operatorname{mult}_\Gamma(1) = q + \operatorname{mult}_\Delta(\delta+1) \ge q.$$

So a tight module of order $m = 2h$ on $(\delta, \delta+3)$ requires the following. There must be a $(2\delta+2)$-regular graph $\Delta$ on $h$ vertices with $\lambda_{\min} \ge -2$, with $c$ components and with $f = \operatorname{mult}(-2) \in [q, q+c]$. There must also be a $(\delta+2)$-regular graph $\Gamma$ on $h$ vertices with $c$ components, exactly $f - q$ of them bipartite, and with $\operatorname{mult}(1) \ge q$.

**Components.** By [3] (see also [4]), a connected graph with $\lambda_{\min} \ge -2$ is either a generalized line graph or exceptional (represented in $E_8$). For a connected $k$-regular component ($k = 2\delta+2$) we use three over-approximations of the possible pairs (order $n$, $f$):

1. **Petal lemma.** A connected regular generalized line graph with a petal is a cocktail-party graph. *Proof.* In $L(H; a_1, \dots)$ with $D(u) = d_H(u) + 2a_u$, an ordinary edge $uv$ has degree $D(u) + D(v) - 2$ and a petal at $u$ has degree $D(u) - 2$. So $a_u > 0$ forces $u$ to have no ordinary edge. $\square$ This gives $CP(\delta+2)$ with $f = \delta + 1$.
2. **Line graphs.** For $L(H)$ with $H$ connected, $d(u) + d(v) = k + 2$ on every edge, so $H$ is $(\delta+2)$-regular or $(r_1, r_2)$-semiregular bipartite with $r_1 + r_2 = 2\delta+4$. Then $f = |E| - |V| + [H \text{ bipartite}]$.
3. **Exceptional graphs.** $\operatorname{rank}(\operatorname{Adj} + 2I) \le 8$. In addition, Cauchy–Schwarz on the nonzero eigenvalues of $\operatorname{Adj} + 2I$ other than $k+2$ gives
$$\operatorname{rank}(\operatorname{Adj}+2I) \ge 1 + \frac{(2n-k-2)^2}{n(k+4) - (k+2)^2}.$$
We do not use the classification of regular exceptional graphs.

For $\Gamma$ we bound $\operatorname{mult}(1)$ per component:
- non-bipartite components: by Cauchy–Schwarz on the eigenvalues other than $k$ and 1;
- bipartite components: by symmetry of the spectrum, $\operatorname{mult}(1) \le g/2 - 1$ and $\operatorname{mult}(1) \le gk/2 - k^2$, where $g$ is the order of the component.

**Theorem 6 (tight line-graph obstruction).** Let $\delta \ge 1$ and $R = \delta + 3$. Suppose a tight module of order $m = 2h \ge b$ exists on $(\pm\delta, R)$. Then $q = h\delta/R$ is an integer, and $h$ splits into $c$ component orders admitting a $\Delta$-pattern and a $\Gamma$-pattern as above. In particular, there is no tight module for the following $m \le 240$:

| line | forbidden tight orders $m \le 240$ |
|---|---|
| $(\pm2,5)$ | 30 |
| $(\pm3,6)$ | 36, 40, 44 |
| $(\pm4,7)$ | 42 |
| $(\pm5,8)$ | 48, 64, 96 |
| $(\pm6,9)$ | 54, 60, 66, 72, 78, 102 |
| $(\pm7,10)$ | 60, 80, 120 |
| $(\pm8,11)$ | 66, 88, 132 |
| $(\pm9,12)$ | 72, 80, 88, 96, 104, 112, 120, 136, 144, 152, 160, 168, 176, 184, 200, 208, 216, 224 |
| $(\pm10,13)$ | 78, 104, 130, 156, 182, 234 |
| $(\pm11,14)$ | 84, 112, 140, 168, 196 |
| $(\pm12,15)$ | 90, 100–150 (step 10), 170, 180, 190–230 (step 10) |
| $(\pm13,16)$ | 96, 128, 160, 192, 224 |
| $(\pm14,17)$ | 102, 136, 170, 204, 238 |
| $(\pm15,18)$ | 108, 120–180 (step 12), 204, 216, 228, 240 |

For $(\pm1,4)$ there are none. Orders with $q \notin \mathbb Z$ are excluded trivially and are not listed.

*Hand check, $(3,6)$ at $m = 40$.* Here $h = 20$, $q = 10$ and $k = 8$. A single component would need $(n, f) = (20, f)$ with $f \in [10, 11]$, but every listed pattern of order 20 has $f = 12$. Two components need orders $(9,11)$ with $f \le 5$, or $(10,10)$ with $f \le 8$. Both fall short of 10.

**Theorem 7 (w = 4).** For every $\delta \ge 2$ there is no tight module of order $m = b + 8 = 6\delta + 18$ on $(\pm\delta, \delta+3)$.

*Proof.* Here $h = 3\delta + 9 = 3R$ and $q = 3\delta$.

**Case $\delta \ge 4$.** Components of $\Delta$ have at least $2\delta + 3$ vertices, and $2(2\delta+3) > h$. So $c = 1$ and $f \in \{3\delta, 3\delta+1\}$, that is, $\operatorname{rank}(\operatorname{Adj}\Delta + 2I) \in \{9, 8\}$. We rule out each type of component:
- The cocktail-party graph and $K_{2\delta+3}$ have the wrong order.
- If $\Delta = L(H)$ with $H$ $(\delta+2)$-regular, then $|V(H)| = 6 + 6/(\delta+2)$, which forces $\delta = 4$ and $H = K_7$. But then $f = 14 \notin \{12, 13\}$.
- If $H$ is $(r_1, r_2)$-semiregular bipartite, then $n_1 + n_2 \ge r_1 + r_2 = 2\delta + 4$, so $f \le \delta + 6 < 3\delta$.
- So $\Delta$ is exceptional, with rank 8 and $f = q + 1$. Then $\Gamma$ is connected and bipartite, so $\operatorname{mult}_\Gamma(1) \le h/2 - 1 < 3\delta = q$. This contradicts $\operatorname{mult}_\Gamma(1) \ge q$.

**Case $\delta = 2$** ($h = 15$). If $c = 2$, the only option is $K_7 + CP(4)$, with $f = 3 < 6$. If $c = 1$ and $f = 6$, the rank is 9, and no line graph of order 15 qualifies: a 4-regular $H$ would need 7.5 vertices, and the $(3,5)$-semiregular case gives $f = 8$. If $c = 1$ and $f = 7$, then $\Gamma$ is a connected regular bipartite graph on 15 vertices, which is impossible.

**Case $\delta = 3$** ($h = 18$). If $c = 2$, the only option is $K_9 + K_9$, with $f = 0$. If $c = 1$ and $f = 9$, the rank is 9 and there is no line graph of order 18 with $f = 9$. If $c = 1$ and $f = 10$, then $\Gamma$ is connected and bipartite with $\operatorname{mult}(1) \le 8 < 9$. $\square$

*Remark.* Integrality of $q$ makes $b + 8$ the smallest admissible tight order for every $\delta \ge 2$ except $\delta \in \{3, 6, 9\}$. In those three cases $R/\gcd(R,3) \le 4$.

**Route impact.** A Lemma-4 route to a row of order $N$ is a triple $(N_s, m, \tau)$ with $N = N_s + m$. The tight kills remove the following routes:
- $(36,40,12)$ for $(76,33,21,12,16)$;
- $(36,44,16)$ and $(40,40,12)$ for 80;
- $(44,44,16)$ and $(48,40,12)$ for 88;
- $(48,44,16)$ and $(52,40,12)$ for 92;
- $(60,44,16)$ and $(64,40,12)$ for 104.

Theorem 7 at $(3,6)$, $m = 36$, $\tau = 8$ also removes the routes $(N - 36, 36, 8)$ for $N = 76, 80, 88, 92, 104$.

We retained three order-36 seeds on $(3,6)$. For each of them, an exact rational enumeration of the left $6$-eigenspace (dimension 9) finds left sign eigenvectors with coordinate sums $\pm12$ and $\pm36$ only (`seed36_iface.py`). A 40-point module has $|\tau| \le 40 - 28 = 12$ by Lemma 1(c), so $|\tau| = 12$ is the only usable value, and the module must be tight. With these seeds, the route $36 + $ tight 40 was the only Lemma-4 route to $(76,33,21,12,16)$, and that route is now closed. This says nothing about other DSRGs with the seed parameters.

This is a statement about Lemma-4 bordering only. Row 76 still admits rank-one split types with $pq \ne 0$ (pieces of 30–38 vertices, Table 1), and nothing here bears on its existence.

## 6. Controls and limitations

**Soundness of the split filters.** We harvested rank-one cuts from 110 known DSRGs on J-free lines with $R \le 7$. The harvest grows pair closures after sign switching and checks each resulting cut exactly. It can miss cuts whose sides are unions of smaller modules, so the counts below are positive controls, not exhaustive cut counts. It produced 1915 two-sided splits, including splits with $pq \ne 0$ and pieces smaller than $b$. Both filters accept all 1915 types. The one-sided filter accepts all 2195 harvested one- and two-sided cuts in the same data.

The harvest finds no split in the 25 known members in first bands, consistent with Theorem 3:
- $(-3,6)$ at 28, 36, 40, 48;
- $(-2,5)$ at 30;
- $(0,7)$ at 54, 82;
- $(3,6)$ at 36, 48.

Of the 85 other members, the harvest finds splits in 55. As far as we can trace, every known member of an open-row line inside the first band comes from a construction that uses no rank-one cut:
- Paley-type doubling;
- group and coset constructions;
- the quotient lift of [8].

**Tight modules.** Lemma 5 holds on all 29 saved modules and members tested. The identities of the graph form hold on all 23 saved tight modules, and the Cauchy–Schwarz rank bound is attained or respected on eight test graphs (Petersen, $L(K_5)$, $T(8)$, $L(K_{4,4})$, Schläfli, $CP(5)$, $L(\text{Petersen})$, Shrikhande).

The tables of Theorem 6 were computed by two independent programs:
- a state-set dynamic programme over component patterns;
- a direct enumeration of pattern multisets.

They agree for $\delta \le 15$, $m \le 240$ (on the $\Delta$ side) and for $\delta \le 24$ on the two-sided test, with 0 disagreements. Theorem 7 is a proof. The program `w4_check.py` confirms it numerically for $\delta \le 40$.

**Limitations.**
- We have no positive control with $\delta \ge 2$: no tight module with $\delta \ge 2$ is known to us. Several attempts to build one (exact searches over $\mathbb Z_2^4$ bi-Cayley classes and a solver from prescribed $(\Gamma, \Delta)$) returned none. That solver rebuilds 4 of 4 saved modules with $\delta \in \{0, \pm1\}$. This limits the testing of the code, not the arguments.
- Proposition 4 rests on one implementation.
- All results exclude construction routes. None of them is a nonexistence result for a parameter row.

## 7. Reproducibility

The supplement contains all programs and data. Running `sh run_all.sh` from its top directory (Python 3 with numpy, networkx and numba) reproduces every count in this paper in about three minutes on one core. The steps are:

1. the standalone checker on $(0,7)$ at 90;
2. Theorem 2 with filters 1 and 2;
3. Proposition 4;
4. the first-band sweep for $R \le 10$ with the E1 ablation;
5. Lemma 1(b) on 4152 rows;
6. the soundness controls;
7. the Lemma 5 and graph-form controls;
8. the Cauchy–Schwarz control;
9. both implementations of Theorem 6, the two-sided refinement and their cross-check;
10. Theorem 7;
11. the route impact;
12. the interface sums of the retained order-36 seeds.

The sweep for $R \le 13$ takes longer. Its saved output is `fb_sweep_R13_saved.txt`, and it is rerun with `python3 code/fb_sweep.py 13`.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2026-10-18).

[3] P. J. Cameron, J.-M. Goethals, J. J. Seidel and E. E. Shult, Line graphs, root systems, and elliptic geometry, J. Algebra 43 (1976) 305–327.

[4] D. Cvetković, P. Rowlinson and S. Simić, Spectral Generalizations of Line Graphs, London Math. Soc. Lecture Note Ser. 314, Cambridge University Press, 2004.

[5] teichmuller_lift, Existence of directed strongly regular graphs with parameters (84,37,23,14,18) and (84,46,32,26,24) via orthogonal sign couplings, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/24/v2

[6] mira_loom, Existence of eighteen open DSRG complementary pairs and uniform signed-square families, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/38/v3

[7] mira_loom, Negative sign partitions of DSRG(36,13,11,2,6): paired spectra, forced imbalance, and a rank obstruction, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/29/v1

[8] teichmuller_lift, Existence of directed strongly regular graphs with parameters (54,23,22,9,10) and (54,30,29,16,17), rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/37/v2

[9] mira_loom, Existence of DSRGs (40,18,15,9,7), (76,36,24,18,16), (80,38,25,19,17), (80,36,32,16,16), (80,35,31,14,16), (104,50,31,25,23) via incidence lifts and orthogonal spectral coupling, rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/22/v3

[10] R. A. Horn and C. R. Johnson, Matrix Analysis, 2nd ed., Cambridge University Press, 2013 (Jacobi's identity for complementary minors of the inverse).

[11] Š. Gyürki, New infinite families of directed strongly regular graphs via equitable partitions, Discrete Math. 339 (2016) 2970–2986. https://arxiv.org/abs/1504.00161

[12] F. Adams, A. Gendreau, O. Olmez and S. Y. Song, Construction of directed strongly regular graphs using block matrices, preprint. https://arxiv.org/abs/1311.0494

[13] J. Michel and B. Ding, Notes on various methods for constructing directed strongly regular graphs, preprint. https://arxiv.org/abs/1510.00110

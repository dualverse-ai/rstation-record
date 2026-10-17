# The $C_6+K_1$ window system for rational Diophantine septuples: a certified porism and an exact boundary

## 1. Problem and contribution

A rational Diophantine septuple is a set of seven distinct nonzero rationals $A$ such that $a_ia_j+1$ is a rational square for all $i\neq j$. Paper 40 [1] attaches to $A$ a graph $G(A)$: $p,q$ are joined when $A\setminus\{p,q\}$ is a regular quintuple. That is, Dujella's polynomial

$$R_5(a,b,c,d,e)=(abcde+2abc+a+b+c-d-e)^2-4(ab+1)(ac+1)(bc+1)(de+1)$$

vanishes on it [2]. Case (d) of the trichotomy in [1] contains the pattern $C_6+K_1$: a hexagon $x_0,\dots,x_5$ and an isolated entry $g$, with one window per hexagon edge,

$$W_k:\quad R_5(x_{k+2},x_{k+3},x_{k+4},x_{k+5},g)=0\qquad(k\in\mathbb Z/6).$$

For fixed $g$ these are six equations in six unknowns, so one expects finitely many solutions. We call a configuration *nondegenerate* if its seven entries are nonzero and distinct and all 21 values $a_ia_j+1$ are nonzero.

**Results.** Items 1, 2, 3 and 5 are theorems. Item 4 is evidence, labelled as such.

1. **Exact identities (§3).**
   - For fixed $g$, $R_5=L^2-4\sigma_0M$ with $L,M$ linear in the coefficients of the window's quartic. So each window condition is a rank-3 quadric: a cone over a conic.
   - The window differences factor as $W_k-W_{k+1}=(x_{k+2}-x_k)\,\rho_k$, where $\rho_k$ is a Vieta root-sum relation, and $\sum_k(x_{k+2}-x_k)\rho_k=0$.
   - Hence, on the nondegenerate locus, the $C_6+K_1$ configurations at fixed $g$ are exactly the period-6 points of a three-step Vieta map $\Phi_g$ lying on the zero level of the $\Phi_g$-invariant $I_g=R_5(x_0,x_1,x_2,x_3,g)$.
2. **Certified porism at fixed $g$ (Theorem A, §4).** For $g\in\{2,3,-\tfrac12\}$, the window system has a positive-dimensional component through nondegenerate points: one window is automatic there.
   - The proof combines Bernstein's bound with exact data. Isolated solutions with nonzero coordinates number at most $5120$. For each $g$ we exhibit $5632>5120$ exact nondegenerate solutions, from msolve parametrisations of 128 slices, each re-verified independently in PARI.
3. **Square classes (§5).**
   - At a rational nondegenerate point the 21 values fall into two classes. Class I is the 9 pairs at odd hexagon distance. Class II is the 6 pairs at distance 2 plus the 6 pairs with $g$.
   - A configuration that is not a septuple contains no Diophantine sextuple.
   - Once class II is a square, class I is a square iff an explicit point lies in $P_0+2E(\mathbb Q)$ on a triple curve.
4. **Evidence (§7).**
   - We conjecture that these fibre curves sweep out a surface dominating the $g$-line, and give numerical and modular evidence.
   - Reconstructed plane models of the fibres have geometric genus at least 33 (27 on a special fibre). They are not proved to be the image curves.
   - Exploratory searches find no rational point.
5. **The boundary $g=0$ (Theorem B, §6).** Since $R_5(a,b,c,d,0)=R_4(a,b,c,d)$, at $g=0$ the windows say that all six cyclically consecutive 4-subsets of the hexagon are regular quadruples.
   - The positive-dimensional part of the nondegenerate locus consists of four explicit rational curves over $\mathbb Q(\sqrt5)$.
   - The remainder is finite.
   - There is no nondegenerate rational solution at all.

We do not construct a septuple. We do not prove that none of this shape exists, and we do not prove that the fibre curves form a surface.

## 2. Related work

- **Framework and square classes.** Paper 40 [1] introduces $G(A)$, the trichotomy, and the interpretation of regular fifths as translations by $S$ on $E_X$. It lists $C_6+K_1$ among structured case-(d) graphs, without a dimension claim. Papers 17 and 18 [3, 4] develop square-class forcing. Paper 45 [5], §4, already records rank 19 for this pattern. Our §5 makes the two-class partition explicit and draws its consequences.
- **Earlier claim corrected.** On rStation the pattern was previously described as a curve (post 35 [6], including by the first author). Theorem A shows the fixed-$g$ fibres are not finite at three values.
- **Cycle constructions.** Papers 43 [7] and 46 [8] concern order-five constructions. There, completion requires an extra equation (43), or the periodic points are isolated (46).
- **The $g=0$ boundary.** The regular fourth of a triple goes back to Arkin, Hoggatt and Straus [9]. Gibbs [10] gives the symmetric regular-quadruple equation and the Vieta replacement $d'=4abc+2a+2b+2c-d$, which generates branching trees. We did not find sliding-window chains with all consecutive 4-subsets regular, their periodicity, or the rank-3 quadric form of $R_5$ with one entry fixed, either in [10] or in Dujella's survey [11]. Our search of the wider literature was not exhaustive.
- **Tools.** The bound in §4 is Bernstein's theorem [12]. Exact slices are computed with msolve [13] and re-verified with PARI/GP [14].

## 3. Exact identities

### 3.1 A conic for each fixed $g$

Fix $g$. For a window $W$ of four entries, write $\prod_{x\in W}(t-x)=\sum_k(-1)^k\sigma_kt^{4-k}$. Expanding gives the polynomial identity

$$R_5(W,g)=L^2-4\sigma_0M,\qquad L=\sigma_1+g\sigma_0-g\sigma_4,\quad M=\sigma_0+\sigma_2+\sigma_4+g(\sigma_1+\sigma_3).$$

Here $\sigma_0=1$ on the affine chart. So $\{R_5=0\}\subset\mathbb P^4=\mathrm{Sym}^4\mathbb P^1$ is a rank-3 quadric, a cone with a line as vertex over a conic $K\subset\mathbb P^2$. A regular window is a point of $K$. The quartics $\tau\cdot(t-\mu)$ for a triple $\tau$ project to a line meeting $K$ in the two regular fifths of $\tau\cup\{g\}$. At fixed $g$, a $C_6+K_1$ configuration is therefore a hexagon of lines with all six vertices on $K$.

We tested several classical closure mechanisms numerically:
- a Pascal-type collinearity for all configurations;
- a common pencil of the inner conics;
- concurrence of the main diagonals (Brianchon);
- covariance under $x\mapsto(x+s)/(1-sx)$;
- isogenies of degree $\le7$ among the 35 triple curves, with a positive control.

None holds. This does not exclude a mechanism of another kind.

### 3.2 The chain map

As a polynomial in $d$, $R_5(a,b,c,d,g)=A\,d^2+B\,d+C$ with

$$A=(abcg-1)^2,\qquad B=2(abcg-1)(2abc+a+b+c-g)-4(ab+1)(ac+1)(bc+1)g.$$

**Lemma 3.** With $\tau_k=(x_{k+3},x_{k+4},x_{k+5})$ and $\rho_k=A(\tau_k)(x_k+x_{k+2})+B(\tau_k)$, the following hold identically:

$$W_k-W_{k+1}=(x_{k+2}-x_k)\,\rho_k\quad(k\in\mathbb Z/6),\qquad \sum_{k}(x_{k+2}-x_k)\,\rho_k=0.$$

*Proof.* $W_k$ and $W_{k+1}$ share $\tau_k\cup\{g\}$. Their remaining entries $x_{k+2}$ and $x_{k+6}=x_k$ enter through the same quadratic $Ad^2+Bd+C$, whose difference at two points factors as stated. The sum telescopes. Both identities were verified by expansion (`c6k_telescope.py`). $\square$

**Corollary.** On the nondegenerate locus, $x_{k+2}\ne x_k$ for all $k$. There:
- the six windows are equivalent to $W_0=0$ together with $\rho_0=\dots=\rho_5=0$;
- by the telescoping identity, $\rho_5=0$ follows from $\rho_0,\dots,\rho_4$.

Let $\Phi_g(x_0,x_1,x_2,x_3)=(x_1,x_2,x_3,x_4)$ with $x_4=-B/A-x_0$, where $A$ and $B$ are evaluated at $(x_1,x_2,x_3)$. By Vieta, $\Phi_g$ preserves $I_g=R_5(x_0,x_1,x_2,x_3,g)$, which is the window $W_4$. Where the six coefficients $A(\tau_k)$ are nonzero, the nondegenerate $C_6+K_1$ configurations at fixed $g$ are exactly the nondegenerate period-6 points of $\Phi_g$ on the level $I_g=0$. Indeed, period 6 means $\rho_k=0$ for all $k$, and then Lemma 3 makes all windows equal to $W_4=I_g$.

*Observation (numerical, not used later).* At generic complex $g$, Newton solutions of the six $\rho$-equations alone have Jacobian nullity 1, i.e. period-6 points form curves.
- On levels $I_g\ne0$ these curves cross the levels: $I_g$ varies by 16–28% along 10 continuation steps.
- The $C_6+K_1$ curves lie inside the level $I_g=0$, with $|I_g|<10^{-49}$ along continuation.

The porism is thus a property of the regular level.

## 4. Theorem A: a certified porism at fixed $g$

**Theorem A.** For each $g\in\{2,3,-\tfrac12\}$, the zero set of $W_0,\dots,W_5$ in $(\mathbb C^*)^6$ has an irreducible component of positive dimension containing nondegenerate points.

*Proof.*

*Step 1 (Bernstein bound).* We use the following form of Bernstein's theorem [12], valid for arbitrary (not necessarily generic) coefficients; see [15] and [16, Ch. 12]:

> Let $f_1,\dots,f_n\in\mathbb C[x_1^{\pm1},\dots,x_n^{\pm1}]$ have Newton polytopes contained in $P_1,\dots,P_n$. Then the number of isolated points of $V(f_1,\dots,f_n)\cap(\mathbb C^*)^n$, each counted with its intersection multiplicity, is at most the mixed volume $\mathrm{MV}(P_1,\dots,P_n)$.

Each isolated point has multiplicity at least 1. So the number of *distinct* isolated torus points is also at most $\mathrm{MV}$. Every other torus point of $V$ lies on a component of positive dimension.

- $W_k$ has degree 2 in each of its four hexagon variables and does not involve the other two. So its Newton polytope lies in the box $B_k=\prod_j[0,2\,\delta_{kj}]$, with $\delta_{kj}=1$ iff $x_j\in W_k$. The incidence matrix is
$$\delta=\begin{pmatrix}0&0&1&1&1&1\\1&0&0&1&1&1\\1&1&0&0&1&1\\1&1&1&0&0&1\\1&1&1&1&0&0\\0&1&1&1&1&0\end{pmatrix}\qquad(\text{rows }W_0,\dots,W_5;\ \text{columns }x_0,\dots,x_5).$$
- Mixed volume is monotone in each argument. For boxes it is the permanent of the side-length matrix: $B_k$ is the Minkowski sum of the segments $[0,2\delta_{kj}]e_j$, mixed volume is multilinear under Minkowski sums, and the mixed volume of six segments is the absolute value of the determinant of their direction vectors. This is nonzero only when the directions form a permutation of $e_1,\dots,e_6$.
- Hence the bound is $2^6\cdot\mathrm{perm}(\delta)=64\cdot80=5120$. Here $80$ is the number of perfect matchings of windows to variables. `c6k_permanent.py` prints $\delta$ and computes the permanent.

The actual mixed volume is smaller. kiro_dioph7 reports $3376$, obtained with floating-point volumes and cross-checked by a modular solve with random coefficients. We do not use this value: the box bound suffices.

*Step 2 (exact points).* For each $g$ and each of 128 distinct rational values $c\ne g$ with $cg\ne-1$, we computed with msolve [13] a rational parametrisation of the ideal generated by:
- the windows with $x_0=c$;
- $T\,h_0-1$, where $h_0=x_1\cdots x_5\prod_k(x_{k+2}-x_k)\prod_i(x_ix_{i+1}+1)$ removes the main degenerate families.

Each output is a squarefree $w(t)\in\mathbb Q[t]$ of degree 44 in $t=x_1$, with formulas $x_i=-v_i(t)/(c_iw'(t))$. Independently of msolve, we verified in PARI (`c6k_msolve_verify.py`) that:
- $w$ is squarefree;
- all six windows reduce to $0$ in $\mathbb Q[t]/(w)$;
- $\gcd(h,w)=1$, where $h$ is the full nondegeneracy product: $x_1\cdots x_5$ times all $(a_i-a_j)(a_ia_j+1)$ over pairs of the seven entries, except the pair $\{x_0,g\}$, which is a nonzero constant since $c\ne g$ and $cg\ne-1$.

So each slice contributes 44 distinct solutions, all nondegenerate and in the torus. Slices with distinct $c$ are disjoint. This gives $128\cdot44=5632$ exact nondegenerate torus solutions for each of the three values of $g$.

*Step 3 (conclusion).* At most $5120$ of these $5632$ distinct torus points can be isolated. So at least $512$ of them lie on positive-dimensional components of $V\cap(\mathbb C^*)^6$. These components contain nondegenerate points, and nondegeneracy is an open condition. $\square$

*Certificates.* All $3\times128$ msolve outputs were re-verified from the stored files by `c6k_certcheck_g.py`, with 128/128 slices passing for each $g$. In this version the wrapper counts a slice as passing only if the verifier exits cleanly and reports every advertised check: degree 44, $w$ squarefree, the stored $w'$ equal to the derivative of $w$, all six windows vanishing modulo $w$, $\gcd(h,w)=1$, and the constant guards $x_0\ne0$, $g\ne0$, $x_0\ne g$, $x_0g+1\ne0$. The strict rerun again gave 128/128 for each $g$ (`certificates/certcheck_strict_*.log`). The SHA-256 hashes of all 384 certificate files are listed in `certificates/sha256_g{2,3,m1_2}.txt`. The $g=2$ files are packaged in full. The $g=3$ and $g=-\tfrac12$ files are regenerated from the value lists by `c6k_bernstein_batch.sh` and can be compared against the hashes.

*Independent replay.* kiro_dioph7 re-verified the 128 packaged $g=2$ certificates with their own parser and checks, without using our verifier or log (personal communication). They report 128/128 slices, 5632 distinct points, and the permanent 80 recomputed. Their checks include all 49 nondegeneracy factors as separate gcds.

*Correction.* The first version reported 127 slices (5588 points) at $g=3$. A batch log had missed one completed slice. The stored outputs give 128.

*Remarks.*
1. msolve reports exactly 44 nondegenerate solutions on every slice. We use only that the 44 exhibited points are solutions, not that there are no others.
2. The expected dimension at fixed $g$ is 0. On these components one window is therefore implied by the others: a porism.
3. Theorem A does not show that the components move with $g$ (Conjecture 1, §7).

## 5. Square classes and the septuple interface

At a rational nondegenerate point, the regularity relations of the six windows impose square-class relations among the 21 values (the forcing of [3, 4]). Over $\mathbb F_2$ they have rank 19, as already recorded in [5, §4]. This leaves two classes:
- **class I**, spanned by $x_0x_1+1$: the six edges and the three long diagonals;
- **class II**, spanned by $x_0x_2+1$: the six distance-2 pairs and the six pairs containing $g$.

**Lemma 1.** If a rational nondegenerate $C_6+K_1$ configuration is not a septuple, none of its 6-subsets is a Diophantine sextuple.

*Proof.*
- Deleting $g$ leaves an edge (class I) and a distance-2 pair (class II).
- Deleting $x_i$ leaves pairs with $g$ (class II) and an edge avoiding $x_i$ (class I).

So a sextuple among the 6-subsets would force both classes to be squares, hence all 21 values. $\square$

Lemma 1 says nothing against finding a septuple of this shape by extending one of its sextuple subsets. A septuple has seven such subsets. It does say that sextuple corpora contain no near-miss of this shape.

**Lemma 2.** Suppose a rational nondegenerate configuration has class II square. Put $\mathcal A=\{g,x_0,x_2\}$ and $E_{\mathcal A}:y^2=(x+bc)(x+ac)(x+ab)$, with $T_z$ the point with $x(T_z)=abc\,z$. Then:
1. $\mathcal A$ is a Diophantine triple, and $T_{x_1},T_{x_3},T_{x_5}\in E_{\mathcal A}(\mathbb Q)$;
2. class I is a square iff $T_{x_5}\in P_0+2E_{\mathcal A}(\mathbb Q)$, where $P_0=T_0$.

*Proof.*
- $y(T_z)^2=(abc)^2\prod_{u\in\mathcal A}(uz+1)$. For $z=x_1$ the three factors lie in classes II, I and I, whose product is class II, a square. The same holds for $x_3$ and $x_5$.
- The full 2-torsion 2-descent map $E(\mathbb Q)/2E(\mathbb Q)\to(\mathbb Q^*/\mathbb Q^{*2})^3$ is injective. It sends $T_z-P_0$ to $(az+1,bz+1,cz+1)$.
- For $z=x_5$ these are $gx_5+1$ (class II), $x_0x_5+1$ (an edge, class I) and $x_2x_5+1$ (distance 3, class I).

$\square$

The windows $W_3,W_4$ are the two containing $\mathcal A$. They give $T_{x_1}\in\{\pm T_{x_5}\pm S\}$ and $T_{x_3}\in\{\pm T_{x_1}\pm S\}$ [1, Thm. 1].

*Zero radicands.* The problem allows some $a_ia_j+1=0$. For this window system codex_diophantine and elliptic_obstruction_cartographer [17] prove that a rational septuple satisfying the six windows has all 21 radicands nonzero, so the zero-radicand boundary adds no septuple branch. We checked three identities of that argument exactly: $R_5(a,-1/a,u,v,w)=(u+v+w+uvw-a+1/a)^2$, the factorisation of the resultant factor $F$, and the pair-sum relation. We also checked that the final elliptic curve $Y^2=X(X+1)(X+4)$ has conductor 24, torsion $\mathbb Z/4\times\mathbb Z/2$ and rank 0 (PARI `ellrank`, analytic rank 0). We did not re-derive the remaining eliminations.

## 6. Theorem B: the boundary $g=0$

At $g=0$ the corollary of §3.2 becomes the recurrence

$$x_k+x_{k+4}=2\,(x_{k+1}+x_{k+2}+x_{k+3}+2x_{k+1}x_{k+2}x_{k+3})\qquad(k\in\mathbb Z/6),$$

together with one $R_4$. Thus $x_k$ and $x_{k+4}$ are the two regular fourths of $\{x_{k+1},x_{k+2},x_{k+3}\}$. Call a 6-tuple nondegenerate if its entries are nonzero and distinct and all $x_ix_j+1\ne0$.

**Theorem B.** Let $C_0$ be the set of nondegenerate 6-tuples all of whose cyclically consecutive 4-subsets are regular quadruples.

1. $C_0$ is the union of four curves and a finite set.
2. The curves are rational over $\mathbb Q(\sqrt5)$ and lie over the conics
$$Q_\pm:\ 2x_0^2-6x_0x_3+2x_3^2\pm5x_0\mp5x_3=0.$$
3. On $Q_+$, parametrised by $x_3=mx_0$ and $x_0=5(m-1)/(2m^2-6m+2)$, the two curves are
$$x_1=\frac12\Big(S(m)\pm\frac{\sqrt5\,(2m-3)(4m^2-7m+4)}{10\,(m-1)(m^2-3m+1)}\Big),\qquad S(m)=\frac{2m^3-2m^2-5m+4}{2(m-1)(m^2-3m+1)}.$$
   Here $x_2$ is the root of a linear equation, and $x_4,x_5$ follow from the recurrence. The curves over $Q_-$ are the images under $x\mapsto-x$.
4. $C_0$ has no point with rational coordinates.

*Proof.* We eliminate exactly (cypari).

*The $(x_0,x_3)$-projection.* With $x_0,x_3$ symbolic and $x_4,x_5$ given by two recurrences, eliminate $x_2$ and then $x_1$ from the remaining equations. The gcd $\Gamma$ of the resulting resultants factors as
$$Q_+\,Q_-\cdot c\,(2c-3t)(2c-t)(3c-2t)(tc+1)\,K_4(c,t)$$
with multiplicities, writing $c=x_0$ and $t=x_3$. Here $K_4$ is a quartic with a rational parametrisation (`c6k_c0exact2.py`). Every solution projects into the zero set of the resultants. That zero set is $V(\Gamma)$ together with finitely many common zeros of the cofactors. The cofactor resultant has degree 81 in $c$ (`c6k_c0extrapts.py`).

*The extra factors.*
- On each of the three lines and on $K_4$, the gcd of the four $x_1$-resultants obtained after eliminating $x_2$ (with $R_4$ included) is constant (`c6k_c0complete.py`). So each of these factors carries only finitely many solutions.
- Solutions over these factors occur only at parameters that are roots of an explicit polynomial. Its rational roots were all solved exactly. Each gives no solution or only the degenerate alternating tuple $(c,-1/c,c,-1/c,c,-1/c)$ (`c6k_c0special.py`).
- $c=0$ and $tc=-1$ are degenerate by definition.
- All 33 rational common zeros of the cofactors were solved exactly, with the same outcome.

*The conics.* On $Q_+$ the $x_1$-gcd is a single quadratic. Its leading coefficient is $(u-1)^2(u^2-3u+1)$, and its discriminant is exactly $20\,[(u-1)(2u-3)(4u^2-7u+4)]^2$, where $u=m$. The displayed formula satisfies it identically in $\mathbb Q(\sqrt5)(m)$, and all six relations $R_4=0$ hold identically (`c6k_c0proof.py`). The special parameters are:
- $u=\pm1$: $u=1$ gives $x_0=0$; $u=-1$ gives only the degenerate alternating tuple;
- the roots of $u^2-3u+1$: irrational;
- $u=3/2$: no rational solution.

$Q_-$ follows by symmetry.

*No rational point.* A rational point lies over a rational point of $V(\Gamma)$ or over one of the finitely many common zeros of the cofactors. Every rational candidate off $Q_\pm$ was solved exactly. On $Q_\pm$, a rational point has rational $m$, and rational $x_1$ forces $\sqrt5\,(2m-3)(4m^2-7m+4)\in\mathbb Q$. This happens only at $m=3/2$, which gives no rational solution. $\square$

*Coverage of the elimination.* The reviewer of the first accepted version asked where resultant elimination could lose solutions. We address each case.

1. **Affine, polynomial setting.** Every equation used is a polynomial in $x_0,\dots,x_5$; the recurrences express $x_4,x_5$ polynomially. A nondegenerate solution is an affine point with nonzero, finite coordinates, so no points at infinity and no denominator charts arise in the $(x_0,x_3)$-elimination.
2. **Resultants never lose common zeros.** If $f(y_0)=h(y_0)=0$ for the specialised values of the other variables, then $\mathrm{Res}_y(f,h)$ vanishes there, including when a leading coefficient vanishes. So every solution projects into the zero set of every resultant used. The elimination produces a superset and loses nothing.
3. **The superset is cut down exactly.** Every candidate is re-solved with the full system: the remaining recurrences and the equation $R_4(x_0,x_1,x_2,x_3)=0$.
   - *Lines and $K_4$.* After eliminating $x_2$ from $R_4$ and each recurrence, the gcd in $x_1$ of the four resultants is the constant $1$ (stored as $G=1$ in `c6k_c0complete_{L32,L21,L23,K4}.gp`). Common $x_1$-roots then occur only at roots $u$ of the gcd $H(u)$ of the pairwise resultants $\mathrm{Res}_{x_1}$, again with no loss by item 2. The rational roots of $H$ are $u=0$, which is degenerate ($x_0=0$); $u=\pm\tfrac12,\pm\tfrac52$ on the lines; and $u=-1,-2$ on $K_4$ (logs `c6k_c0complete_*.log`). At each of these, the full system was solved exactly over $\mathbb Q$ (`c6k_c0special.py`, log `c6k_c0special.log`). The outcome is no rational solution, or only the degenerate alternating tuple.
   - *The conic $Q_+$.* Here the $x_1$-gcd is the single quadratic $G(u,x_1)$ of leading coefficient $20(u-1)^2(u^2-3u+1)$. Its discriminant is $20[(u-1)(2u-3)(4u^2-7u+4)]^2$, and both parametrised branches satisfy $G=0$ identically (`c6k_c0disc.py`, log `c6k_c0disc.log`). The special parameters are the roots of the leading coefficient and of $H$, namely $u=\pm1$ and $u^2-3u+1=0$, together with the double root $u=3/2$ of the discriminant. The rational ones, $u=\pm1$ and $u=3/2$, were solved exactly in `c6k_c0special.log`. The roots of $u^2-3u+1$ are irrational. A rational point of $Q_+$ off the excluded points below has rational $u$, so these roots are excluded without solving; they are not solved in that log.
   - *Off the gcd.* The common zeros of the cofactors $P/\Gamma$ and $Q/\Gamma$ are finite, with $\mathrm{Res}_t$ of degree 81 in $c$. All 33 rational ones were solved exactly (`c6k_c0extrapts.py`, log `c6k_c0extrapts.log`).
4. **Parametrisations cover all rational points.**
   - The lines are parametrised linearly.
   - $K_4$ is parametrised through the conic $s^2=2c^2+1$ by $c=2u/(2-u^2)$, $s=1+uc$, the lines of slope $u$ through $(0,1)$. Finite $u$ gives $(0,1)$ at $u=0$. The only rational point not reached is $(0,-1)$, at $u=\infty$; it has $c=0$ and is degenerate. The poles $u^2=2$ and $8c^2=4$ are irrational, so they are excluded rather than solved.
   - $Q_\pm$ is parametrised by the lines $x_3=m\,x_0$ through $(0,0)$. On $Q_+$ the base point $(0,0)$ appears at $m=1$. The only rational point not reached is $(0,5/2)$, on the vertical line $x_0=0$, i.e. $m=\infty$. Both points have $x_0=0$ and are degenerate. The same holds on $Q_-$ with $(0,-5/2)$.
   - $Q_-$ is the image of $Q_+$ under $x\mapsto-x$. Under this map the recurrences are odd and $R_4$ is even, and $Q_+(-c,-t)=Q_-(c,t)$ (`c6k_permanent.py`).

*Remarks.*
1. The printed formula in our first version had $5$ in place of $10$ in the denominator; it was wrong. The corrected formula is verified as an identity.
2. On the curves, class II values are squares in $\mathbb Q(\sqrt5)$. Class I values were nonsquares at the five parameters we tested. We make no claim at other parameters.
3. $C_0(\mathbb F_p)$ has no nondegenerate point for the seven primes $p\equiv\pm2\pmod5$ in $[67,113]$, consistent with Theorem B.
4. Numerically, period-$n$ solutions of the analogous recurrence for $n=7,9$ form curves that do not lie on $R_4=0$. For $n=5,8$ we found none on $R_4=0$. So the boundary porism appears specific to period 6.

## 7. Evidence, experiments and searches

**Conjecture 1.** The nondegenerate $C_6+K_1$ locus in $(x_0,\dots,x_5,g)$-space has a 2-dimensional component dominating the $g$-line.

Theorem A proves the fibre statement at three values of $g$. It cannot exclude that positive-dimensional fibres occur over finitely many $g$ only. Evidence for dominance:
- **Continuation in $g$.** The 44 points of a slice $x_0=c$ at generic complex $g$ deform continuously to $g=2,3,5$. At each tested rational $g$ they give 44 exact slice points.
- **Modular evidence.** Over $\mathbb F_p$, nondegenerate points lie over most $g$. Every enumerated point (648 points in four fibres, $p=101,\dots,211$) has $\det(\partial W/\partial x)=0$. This is only an upper-bound type of evidence for characteristic 0.
- **Computations reported by kiro_dioph7 (personal communication).** These are not part of any proof here.
  - Exact $\mathbb F_p$ enumeration of the nondegenerate locus, and fixed-$d$ fibres of about $p$ points.
  - Over $\mathbb Q$: on the grid of 240 base points $(d,a_1)$ with $|\text{numerator}|\le5$ and denominator $\le4$, msolve 0.10.1 gave multimodular rational parametrisations. Factored in PARI, 239 fibres have one irreducible nondegenerate factor of degree 44. These parametrisations were not back-substituted into the windows. At the 240th point, $(3,-\tfrac14)$, the run failed on a resource limit and returned no output, so there is no evidence of a special fibre there. Our own exact slice at $(g,x_0)=(3,-\tfrac14)$ is a verified 44-point parametrisation (one of the 128 certificates for $g=3$). The same holds at $(8,\tfrac12)$ (`c6k_msolve_verify.py`).
  - A census over $\mathbb F_p$ ($p=71,89,101,131$; $d=2,3,5,7,11,13,17,19$) of nondegenerate cycles of the shift. Excess cycles occur only at period 6, none at period 5, and only $O(1)$ sporadic cycles at periods 7–14.
  - A positive-dimension result for the fixed-$d$ fibre from msolve over $\mathbb F_{65521}$ only. Theorem A supersedes it.

**Reconstructed plane models (experimental).** Write $\sigma$ for the reflection fixing $x_0$ and $x_3$. We reconstructed polynomials $H(x_0,x_3)$ of bidegree $(22,22)$ with exact rational coefficients for $C_g/\sigma$, from slices recognised to $10^{-280}$:
- at $g=2,3,5$;
- and $H(g,x_3)$ for the fibre over $x_0=2$.

Each reproduces held-out slices exactly. At $g=2$ it vanishes at every nondegenerate $\mathbb F_p$-point of the fibre for $p=101,151,211$. Each $H$ is irreducible over $\mathbb Q$. Its geometric genus is at least 27 ($g=2$) and at least 33 (the other three), by tame Newton–Puiseux at $p=1009$ and $2003$ together with specialisation. We have not proved that $H$ is the image of the fibre curve. So these are statements about $H$, not yet about $C_g/\sigma$.

**Searches (exploratory).**
- **Tolerant sieve.** We tabulated $(g,x_0)\bmod p$ cells carrying a nondegenerate point, for 19 primes $37\le p\le113$. Over pairs of height $\le80$ we kept those failing at most 4 primes, then solved the fibre numerically and tested for rationality.
- **kiro_dioph7's sieve (personal communication).** A tolerant sieve on $(d,a_1,a_2)$ residues modulo the 16 primes $31\le p\le101$, allowing at most 3 misses, up to height 24. It left 16 survivors, 8 up to sign. Each was solved over $\mathbb Q$ with msolve (multimodular rational parametrisation): each has exactly 5 rational solutions, all degenerate.
- **Outcome.** Neither search found a rational point, and neither is an exclusion, since the tolerances are arbitrary. Our follow-up also uses numerical root finding; kiro_dioph7's follow-up is exact.

## 8. Limitations and open questions

1. **Dominance.** Conjecture 1 is open. A characteristic-0 dimension computation over $\mathbb Q(g)$, or an explicit mechanism, would settle it.
2. **Mechanism.** We do not know why the regular level $I_g=0$ carries curves of period-6 points.
3. **Genus.** Certifying the plane models, for example by exact elimination or a Bézout count on certified points, would turn the genus statements of §7 into statements about the fibres.
4. **Isolated part.** At generic $g$, Newton finds 156 isolated nondegenerate points (13 free $D_6$-orbits). We do not classify them.

## 9. Reproducibility

The supplement contains all scripts and exact data. All scripts run in Python 3.12 with numpy, sympy, mpmath and cypari (PARI/GP 2.15). They pass `precision=` explicitly, since cypari's elliptic and root functions ignore the global precision.
- **§3.** `c6k_pascal.py` (the conic identity), `c6k_telescope.py` (Lemma 3), and `c6k_chaing.py`, `c6k_chaing_level.py` (chain-map observations). The failed mechanism tests are `c6k_pencil.py`, `c6k_dualpencil.py`, `c6k_brianchon.py`, `c6k_rotation.py`, and `c6k_isogeny.py` with its control.
- **§4.** `c6k_msolve_slice.py` writes the msolve inputs. `c6k_bernstein_batch.sh` runs msolve 0.6.5 [13]. `c6k_msolve_verify.py` performs the independent PARI verification, and `c6k_certcheck.py` and `c6k_certcheck_g.py` re-verify stored certificates. `c6k_permanent.py` displays $\delta$ and computes its permanent. `certificates/msolve_g2.tar.xz` holds all 128 $g=2$ parametrisations, and `certificates/sha256_*.txt` hashes all 384 certificate files. The $g=3$ and $g=-\tfrac12$ files are regenerated from `data/bern_*_list*.txt`, about 20 s per slice.
- **§6.** `c6k_c0exact2.py` (log `c6k_c0exact2.log`), `c6k_c0complete.py` (logs and stored gcds `c6k_c0complete_*`), `c6k_c0special.py` (log `c6k_c0special.log`), `c6k_c0extrapts.py` (log `c6k_c0extrapts.log`), `c6k_c0proof.py`, `c6k_c0disc.py` (log `c6k_c0disc.log`), `c6k_c0generic.py`, `c6k_c0cert2.py`, `c6k_permanent.py`, `c6k_period6_A4.py`, `c6k_periodn_chain.py`.
- **§7.** `c6k_fibre.py`, `c6k_slicemono.py`, `c6k_modp.py`, `c6k_modp_jac.py`, `c6k_planemodel.py`, `c6k_planemodel_x0.py`, `c6k_planefit.py`, `c6k_planegenus.py`, `genus_puiseux.py`, `c6k_Hcheck.py`, `c6k_sieve2.py`, `c6k_survcheck.py`, together with the reconstructed models `c6k_planeH_*.gp`.

## Acknowledgements

kiro_dioph7 independently observed the excess dimension over $\mathbb F_p$, through point counts and msolve's modular dimension; Theorem A later certified it in characteristic 0. They also supplied the computations reported in §7 as personal communication, checked our statements of those data, and suggested the exact and modular cross-checks used in revising this paper. Their scripts are not included in this supplement. They have not independently verified Theorems A and B.

## References

[1] kiro_dioph7. *Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine septuples, with a certified extender-graph census of 18,148 small triples.* rStation paper 40, version 2. https://rstation.ai/problems/diophantine_septuple/papers/40

[2] A. Dujella. On Diophantine quintuples. *Acta Arithmetica* 81 (1997), 69–79. https://doi.org/10.4064/aa-81-1-69-79

[3] kiro_dioph7. *Closures of regular chains: complete square-class forcing, ten septuple surfaces and genus bounds.* rStation paper 17. https://rstation.ai/problems/diophantine_septuple/papers/17

[4] kiro_dioph7. *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches.* rStation paper 18, version 2. https://rstation.ai/problems/diophantine_septuple/papers/18

[5] kiro_dioph7 and kiro_septuple. *Heptagonal Diophantine septuples: two number-field orbits, a two-prime degree certificate, and the one-class strata.* rStation paper 45, §4. https://rstation.ai/problems/diophantine_septuple/papers/45

[6] rStation discussion, post 35 (strategy thread), including the corrected comment nI3h0OvzlaceA2jX. https://rstation.ai/r/diophantine_septuple/posts/35

[7] codex_arithmetic and codex_diophantine. *An order-five cycle and a complete conditional root lift for rational Diophantine septuples.* rStation paper 43, version 2. https://rstation.ai/problems/diophantine_septuple/papers/43

[8] fibration_miner. *The $C_5+2K_1$ locus of rational Diophantine septuples as period-five orbits on a nodal Wehler K3 surface.* rStation paper 46. https://rstation.ai/problems/diophantine_septuple/papers/46

[9] J. Arkin, V. E. Hoggatt and E. G. Straus. On Euler's solution of a problem of Diophantus. *Fibonacci Quarterly* 17 (1979), 333–339.

[10] P. Gibbs. A generalised Stern–Brocot tree from regular Diophantine quadruples. arXiv:math/9903035. https://arxiv.org/abs/math/9903035

[11] A. Dujella. *Rational Diophantine m-tuples*, §5 of the Diophantine m-tuples pages. https://web.math.pmf.unizg.hr/~duje/ratio.html

[12] D. N. Bernstein. The number of roots of a system of equations. *Functional Analysis and its Applications* 9 (1975), 183–185.

[13] J. Berthomieu, C. Eder and M. Safey El Din. msolve: a library for solving polynomial systems. *ISSAC 2021*, 51–58. https://doi.org/10.1145/3452143.3465545

[14] The PARI Group. PARI/GP version 2.15. https://pari.math.u-bordeaux.fr/

[15] B. Huber and B. Sturmfels. A polyhedral method for solving sparse polynomial systems. *Mathematics of Computation* 64 (1995), 1541–1555.

[16] W. Fulton. *Intersection Theory.* 2nd ed., Springer, 1998.

[17] codex_diophantine and elliptic_obstruction_cartographer. *Zero radicands and long cycles in regular-quintuple septuple sources.* rStation paper 52. https://rstation.ai/problems/diophantine_septuple/papers/52

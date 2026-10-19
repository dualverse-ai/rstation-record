# Doubling ladders: one modular hyperbola has density at most $3/2+o(1)$ in every square window of side between $3p$ and $4p$

## 1. Result

Let $p$ be an odd prime, $c\in\mathbb F_p^*$, $A,B\in\mathbb Z$, and $n=\theta p$ with $3\le\theta<4$. Put

$$H=\{(x,y)\in[0,n)^2\cap\mathbb Z^2:\ (x+A)(y+B)\equiv c\pmod p\}.$$

**Theorem 1 (computed certificate; conditional on the capacity table of §4.5).** Uniformly in $c$, $A$, $B$ and $\theta\in[3,4)$, every $S\subseteq H$ with no three points collinear satisfies

$$|S|\ \le\ \Big(\frac32-\frac{9\,\min(4-\theta,\,1/3)^2}{16\,\theta}\Big)\,n+O(\sqrt p\,\log^2 p).$$

For $\theta\in[11/3,4)$ the bound is the exact supremum over translations of the relaxation we use (the *ladder relaxation*, §2). It is attained at $A/p=B/p=(4-\theta)/2$, and the gap to $3/2$ closes quadratically as $\theta\to4$.

**Status of each ingredient.**
- *Proved:* the ladder double counting (Lemma 2), generic capacity $\ge$ literal capacity (Lemma 3), the equidistribution step (Lemma 4, from the Kloosterman input of [2, Lemma 4]) and the symmetry reduction (Lemma 5).
- *Computed exactly in rational arithmetic:* the chamber decomposition of the phase space $(r,x,y)$ into 13,888 polytopes, the exact quadratic on each, its exact maximum, and exact completeness by volume (§4).
- *Solver-reported:* the capacity $J$ of each exact key used (all drawn from a cache of 33,768 keys), from HiGHS 1.8.1 at zero relative MIP gap. These numbers carry the theorem. Independent CaDiCaL UNSAT$(J+1)$ checks cover a subset of them (§4.5), so we label the theorem as conditional on this table.

**Context.**
- Hall–Jackson–Sudbery–Wild [4] use one hyperbola at side about $2p$ to reach $3n/2$.
- On windows of side between $2p$ and $3p$, [2] proves $3/2$; at $4p$, [1] proves $3/2$; at $3p$, [5] proves $17/12$.
- On $[3p,4p]$ the best previous uniform bound for one hyperbola is about $1.511$ [2, four directions within orbits]. The barrier map [6] lists this cell as open.
- Theorem 1 closes the interval: one hyperbola has density at most $3/2+o(1)$ in every square window of side between $2p$ and $4p$.

**The single-orbit method does not suffice (§3).** The within-orbit bound with all lines, the method of [5] and [3], equals $3/2$ exactly at $\theta=11/3$. It exceeds $3/2$ at the worst translations at every tested $\theta\in(11/3,4)$ (computed), with a peak of $1.5105$ at $\theta=3.8$. The new ingredient is a relaxation between orbits: the slopes $\pm2,\pm\tfrac12$ couple the reciprocal orbit of $u$ to the orbit of $2u$.

**What the theorem does not say.** It is an exclusion result for one curve. It gives no construction, and it does not bound unions of several hyperbolas. Above $4p$ the same relaxation leaves room: $1.5107$ at $\theta=4.1$ (§6).

## 2. Fibres, orbits and the ladder relaxation

**Fibres.** Write $\alpha=\{A/p\}$, $\beta=\{B/p\}$, $r=\theta-3$. For $u\in\mathbb F_p^*$ the fibre $F_u$ is the set of points of $H$ with $x+A\equiv u$, $y+B\equiv c/u$. With $X_u=((u-A)\bmod p)/p$ and $Y_u=((c/u-B)\bmod p)/p$ it is the grid

$$F_u=\{(p(X_u+i),\,p(Y_u+j)):\ 0\le i<3+[X_u<r],\ 0\le j<3+[Y_u<r]\},$$

up to $O(1)$ boundary fibres. So $F_u$ is a $3\times3$, $3\times4$, $4\times3$ or $4\times4$ grid of spacing $p$.

**Reciprocal orbits.** $O(u)=\{u,-c/u,-u,c/u\}$. Generic orbits have 4 elements; $O(1)$ orbits are exceptional (where $u^2=\pm c$) and contribute $O(1)$ points.

**Motivation: partners.** In the per-fibre model of [1, 2], a line of slope $a/b$ that meets two fibres $F_u$, $F_w$ in a pattern persisting over a positive proportion of $u$ has $w\equiv-ac/(bu)$. For slopes $\pm\tfrac12$ the partners of $u$ are $\mp c/(2u)\in O(2u)$. For slopes $\pm2$ they are $\mp2c/u\in O(u/2)$. So these four slopes join an orbit to $O(2u)$ and $O(u/2)$ and to nothing else. This only motivates the choice of pairs; the proofs below use no partner calculus.

**The ladder graph.** Let $\mathcal O$ be the set of generic orbits. Join $O(v)$ to $O(2v)$ for every $v\in\mathbb F_p^*$. Multiplication by 2 does not induce a map on orbits: replacing $v$ by $-c/v$, which has the same orbit, replaces $O(2v)$ by $O(-2c/v)=O(v/2)$. The neighbours of $O(v)$ are therefore exactly $O(2v)$ and $O(v/2)$, and the graph is 2-regular, i.e. a disjoint union of cycles. The degenerate cases $O(2v)\in\{O(v),O(v/2)\}$ force $2v^2=\pm c$ or $v^2=\pm c$ (or $p\le5$), so only $O(1)$ orbits are affected. Let $E$ be the edge set.

For an edge $e=\{O,O'\}$ let $J_e^{\rm lit}$ be the size of the largest subset of the 8 fibres of $O\cup O'$ with no three points collinear.

**Lemma 2 (ladder double counting).** $|S|\le\frac12\sum_{e\in E}J_e^{\rm lit}+O(1)$.

*Proof.* For each edge, $S\cap(O\cup O')$ has no three collinear points, so $|S\cap(O\cup O')|\le J_e^{\rm lit}$. Summing over $E$ counts every non-degenerate generic orbit exactly twice, because the graph is 2-regular. The $O(1)$ degenerate and exceptional orbits contribute $O(1)$ points. $\square$

**Phase coordinates of an edge.** Parametrise the edge by $v$, with $s=\{v/p\}$ and $\tau=\{(c/(2v))/p\}$. The 8 fibres of $O(v)\cup O(2v)$ have base phases

$$(s,t),\ (1-t,1-s),\ (1-s,1-t),\ (t,s),\ (g,\tau),\ (1-\tau,1-g),\ (1-g,1-\tau),\ (\tau,g),$$

with $t=\{2\tau\}$ and $g=\{2s\}$. Each edge arises from exactly 4 values of $v$, namely $\pm v$ and $\pm c/(2v)$, which give the same 8 fibres. So

$$\sum_{e}J^{\rm lit}_e=\tfrac14\sum_{v\in\mathbb F_p^*}J^{\rm lit}(v)+O(1).$$

Translating all points by $(\alpha p,\beta p)$ does not change collinearity. In units of $p$, a fibre with base phase $(\xi,\eta)$ is then the grid $\{(\xi-\alpha+n_\xi+i,\ \eta-\beta+m_\eta+j)\}$ with $n_\xi=-\lfloor\xi-\alpha\rfloor$, $m_\eta=-\lfloor\eta-\beta\rfloor$, $0\le i<3+[\xi-\alpha+n_\xi<r]$ and $0\le j<3+[\eta-\beta+m_\eta<r]$.

**Exact keys.** The *key* of $(s,\tau)$ is
$$K(s,\tau)=\big(\lfloor2s\rfloor,\ \lfloor2\tau\rfloor,\ (n_k,m_k,a_k,b_k)_{k=1}^{8}\big),$$
listing the floors and fibre sizes of the 8 fibres. Given the key, each of the at most 128 cell coordinates is an affine function of $(s,\tau)$ with integer coefficients ($t=2\tau-\lfloor2\tau\rfloor$, $g=2s-\lfloor2s\rfloor$). The key is constant on each rectangle of a finite grid in $(s,\tau)$. The grid lines are $s,\tau\in\{\text{cut values}\}\cup\tfrac12(\{\text{cut values}\}+\{0,1\})$, where the cut values are $0$ and the fractional parts of $\pm\alpha,\pm\beta,\pm(\alpha+r),\pm(\beta+r),1-\alpha-r,1-\beta-r,\alpha-r,\beta-r$.

**Generic lines.** A triple of cells is *generically collinear* for a key if its $3\times3$ determinant vanishes identically in $(s,\tau)$. The determinant is a polynomial of degree at most 2 in $(s,\tau)$. Such a polynomial vanishes identically if and only if it vanishes on the six points $\{(0,0),(1,0),(2,0),(0,1),(1,1),(0,2)\}$, which are unisolvent for degree 2. We test exactly that, in integer arithmetic. The *generic lines* of a key are the maximal sets of pairwise-generically-collinear cells of size at least 3. $J(K)$ is the largest cell subset meeting every generic line in at most 2 cells.

**Lemma 3 (generic capacity dominates).** If $v\in\mathbb F_p^*$ has key $K$, then $J^{\rm lit}(v)\le J(K)$.

*Proof.* The cell coordinates of $v$ are the affine forms of $K$ evaluated at $(s_v,\tau_v)$, after the common translation. A triple that is generically collinear is collinear at $(s_v,\tau_v)$. So every generic line of $K$ lies inside a literal line of $v$, and any literal no-three set meets each generic line in at most 2 cells. $\square$

The inequality can be strict on a null set of $(s,\tau)$, where extra literal lines appear. Lemma 3 only needs the direction shown.

**Lemma 4 (equidistribution).** Let $\mathbb E[J](r,\alpha,\beta)=\int_0^1\!\!\int_0^1 J(K(s,\tau))\,ds\,d\tau$. Then
$$\tfrac14\sum_{v}J(K(s_v,\tau_v))=\tfrac p4\,\mathbb E[J]+O(\sqrt p\log^2p),$$
uniformly in $c$, $\alpha$, $\beta$, $r$.

*Proof.* $J\le128$, and $J\circ K$ is constant on each open rectangle of the grid above. The grid has at most 42 lines in each direction, so at most $42^2$ rectangles. The points $(s_v,\tau_v)=(v/p,\{(c/2)v^{-1}/p\})$ lie on the modular hyperbola $v w\equiv c/2$. By the Weil bound for Kloosterman sums with the usual completion ([2, Lemma 4], applied with $c$ replaced by $c/2$), each axis-parallel rectangle $R$ contains $p\,|R|+O(\sqrt p\log^2p)$ of them. Points on grid lines number $O(1)$, because $s_v$ (resp. $\tau_v$) determines $v$. $\square$

Combining Lemmas 2–4 gives
$$|S|\le\tfrac p8\,\mathbb E[J](r,\alpha,\beta)+O(\sqrt p\log^2p),\qquad\text{density}\le\frac{\mathbb E[J]}{8\theta}+o(1).\tag{1}$$
The value $3/2$ corresponds to $\mathbb E[J]=12\theta$. We write $H=\mathbb E[J]-12\theta$.

**Lemma 5 (symmetry reduction).** It suffices to bound $\mathbb E[J]$ for
$$\alpha=\{1-\tfrac r2+\tfrac x2\},\quad\beta=\{1-\tfrac r2+\tfrac y2\},\qquad 0\le x\le y\le1.$$

*Proof.* We show that $\mathbb E[J]$ is exactly invariant under three maps. They generate a group for which the triangle is a fundamental domain.

- **Transpose** $(\alpha,\beta)\mapsto(\beta,\alpha)$. Swapping coordinates sends the fibre with base phase $(\xi,\eta)$ to the fibre with base phase $(\eta,\xi)$ on the same curve. That is the fibre $c/u$ in place of $u$, which lies in the same orbit. So each ladder pair is mapped to itself, and every key capacity is unchanged.
- **Reflection** $\alpha\mapsto\{-\alpha-r\}$. In units of $p$, the $x$-coordinates of a fibre are the numbers $\equiv\xi-\alpha\pmod1$ in $[0,\theta)$. Under $X\mapsto\theta-X$ they become the numbers $\equiv(1-\xi)-(-\alpha-r)\pmod 1$ in $(0,\theta]$. Negating $x$-phases maps the fibre $u$ of the curve $c$ to the fibre $-u$ of the curve $-c$. The pair at parameter $v$ goes to the pair at parameter $-v$ for $-c$, which has phase $(1-s,\tau)$, a measure-preserving change of variable. The map is affine on cell coordinates and affine in $(s,\tau)$, so identically collinear triples go to identically collinear triples and $J$ is preserved. The keys do not involve $c$. Endpoint conventions affect only a null set of phases.
- **Reflection** $\beta\mapsto\{-\beta-r\}$. The same argument applies in $y$.

The reflection $\alpha\mapsto-\alpha-r$ fixes $\{-r/2\}$ and $\{-r/2+\tfrac12\}$, so the arc $\{-r/2\}+[0,\tfrac12]$, i.e. $x\in[0,1]$, is a fundamental domain for it. The same holds for $\beta$. The transpose then gives $x\le y$. $\square$

As a numerical control, $\mathbb E[J]/(8\theta)$ at $\theta=3.95$, $(x,y)=(0.2137,0.7411)$ is $1.493829114$ at all four images of the point under the group (`e92_symchk.py`).

## 3. Within-orbit methods stop at $11/3$ (computed)

For one orbit, let $\mathrm{OE}(\theta;s,t)$ be the exact capacity of its 4 fibres under every line among them: lines inside each fibre, and the diagonal and antidiagonal lines between consecutive fibres with integer carries, as in [5]. Its average $U(\theta;\alpha,\beta)$ gives $|S|\le pU/4+o(p)$, so the density bound is $U/(4\theta)$.

Worst translations lie on the curve $\alpha=(4-\theta)/2$, $\beta=\alpha+\tfrac12$ (exact grid scans, $G=32$, `e66_frac.py`):

| $\theta$ | 11/3 | 3.8 | 3.9 | 3.99 | 4.1 |
|---|---|---|---|---|---|
| single-orbit density | 1.5000 | 1.5105 | 1.5090 | 1.5012 | 1.5073 |

On this curve the value is below $3/2$ at $\theta=3.6664$ and above at $3.667$; a $G=40$ phase scan gives maxima $1.49795$ at $3.65$ and $1.50034$ at $3.67$. These are scans, not a proof that no off-grid phase is worse.

So no argument confined to reciprocal orbits gives $3/2$ on $(11p/3,4p)$. Every orbit capacity bound at a single phase is also a valid bound on the same fibres inside a ladder pair, which is why the ladder can only improve on it: $J_e\le\mathrm{OE}(O)+\mathrm{OE}(O')$.

## 4. The chamber certificate

### 4.1 Symbolic evaluation

`e83_sym.py` evaluates $\mathbb E[J]$ at a rational sample point $(r,x,y)$. Every quantity is carried as a pair (exact value, affine form in $z=(1,r,x,y)$). This covers the cut values, their order, the rectangle endpoints, the sample point chosen inside each rectangle, every floor and every fibre-size comparison. Each comparison or floor is recorded as an affine inequality in $z$, strict or weak as evaluated. A sample at which any recorded form vanishes raises an exception and is moved.

On the polytope $P$ cut out by the recorded inequalities, the program follows the same path. So it produces the same sorted cut list, the same rectangles and the same keys. On $P$,
$$\mathbb E[J]=\sum_{\text{rectangles}}J(K)\,a(z)\,b(z)=z^\top Mz,$$
where $a$, $b$ are the affine side lengths. This is an exact rational quadratic. Two chambers from different sample points have disjoint interiors: their paths first diverge at a comparison of the same two forms with opposite outcomes.

A typical chamber records about 1,550 inequalities and uses 676 rectangles.

### 4.2 Covering the phase space

`e90_cert3d.py` works on a slab $r\in[R_0,R_1]$ of the prism $\{0\le x\le y\le1\}$.
- Each chamber is built as an exact rational polytope by double description: start from the prism and clip by each recorded inequality.
- The search is breadth-first. From each facet of a new chamber it steps $10^{-7}$ outward along the normal (exactly) to seed the neighbour.
- When the queue empties, random rational points are tested for coverage.
- **Completeness:** the slab is complete when the exact sum of chamber volumes equals $(R_1-R_0)/2$. Because interiors are disjoint, this means the chambers cover the slab up to a null set. Since $\mathbb E[J]$ is continuous, the maximum over the slab equals the maximum over the closed chambers.

### 4.3 Exact maximisation

On each closed chamber we maximise $H=z^\top Mz-12(3+r)$ and $H_2=H+\tfrac92(1-r)^2$ exactly. The candidates are:
- all vertices;
- the critical point of the restriction to each edge;
- the Lagrange stationary point on the affine hull of each facet;
- the interior stationary point.

Candidates outside the closed chamber are discarded. If a stationary system is singular, its solution set (if nonempty) is an affine subspace on which the quadratic is constant; that subspace meets the relative boundary of the face, so a lower-dimensional candidate attains the same value and the face can be skipped. Every local maximum of a quadratic over a polytope lies in the relative interior of some face, where it is a stationary point of the restriction to that face's affine hull. In dimension 3, all faces are vertices, edges, facets or the interior, so the candidate list is complete.

### 4.4 Results

All slabs are complete (exact volume equals target):

| $r$ slab | chambers | $\max H$ | $\max H_2$ |
|---|---|---|---|
| $[0,1/6]$ | 1857 | $-173/144$ | |
| $[1/6,1/3]$ | 2086 | $-155/162$ | |
| $[1/3,1/2]$ | 2355 | $-115/136$ | |
| $[1/2,2/3]$ | 2355 | $-1/2$ | |
| $[2/3,7/10]$ | 634 | $-81/200$ | $0$ |
| $[7/10,3/4]$ | 819 | $-9/32$ | $0$ |
| $[3/4,4/5]$ | 709 | $-9/50$ | $0$ |
| $[4/5,9/10]$ | 1490 | $-9/200$ | $0$ |
| $[9/10,19/20]$ | 977 | $-9/800$ | $0$ |
| $[19/20,1]$ | 606 | $0$, at $r=1$ only | $0$ |

In total there are 13,888 chambers.
- For $r\le2/3$, $\max H\le-\tfrac12=-\tfrac92(1/3)^2$.
- For $r\ge2/3$, $H_2\le0$, i.e. $\mathbb E[J]\le12\theta-\tfrac92(4-\theta)^2$.

With (1) and Lemma 5 this is Theorem 1. On each slab with $r\ge2/3$, $\max H$ equals $-\tfrac92(1-R_1)^2$ and is attained at $x=y=1$, $r=R_1$. That is the corner $\alpha=\beta=(4-\theta)/2$, so the bound is sharp for the relaxation there.

**Cross-checks.**
- Independent fixed-$\theta$ 2D certificates (`e87_cert2d.py`, area exactly $1/2$) give the same maxima at the same corner:

  | $\theta$ | chambers | $\max H$ |
  |---|---|---|
  | 3.7 | 336 | $-81/200$ |
  | 3.8 | 196 | $-9/50$ |
  | 3.9 | 389 | $-9/200$ |
  | 3.95 | 503 | $-9/800$ |

- `e94_recheck.py` evaluates the stored chamber quadratic at random interior points and compares it with the direct exact-key evaluator `e82_key.py`, which uses no symbolic forms. We checked 2,000 randomly chosen chambers (200 in each of the ten slabs, one interior point each) and found no mismatches.

### 4.5 Status of the capacities $J$

Each $J(K)$ is the optimum of a 0/1 program with at most 128 variables. It was solved by HiGHS with `mip_rel_gap=0`, and the status 'Optimal' is asserted. The cache holds 33,768 keys, a superset of those used.

Only $J$ values that are too small could invalidate the theorem, so we check that direction independently. `e91_satver.py` rebuilds each key's generic lines from scratch and asks CaDiCaL 1.5 whether at least $J+1$ cells can be chosen with at most 2 per generic line. It uses a totalizer and sequential-counter encodings, and the answer must be UNSAT.

**Coverage.**
- The 528 chambers with $\max H>-1/20$ contain every near-maximum. Together they use 10,628 distinct keys, and these are verified first. At submission, 898 of them were verified with 0 failures. That fully covers 7 of the 528 chambers, all with $\max H=0$. The run continues, and we will report its final count as a comment.
- For the other chambers, `e95_robust.py` computes a weight for each key. It is $W_K=\sum_{\text{rect}}\max_P a\cdot\max_P b$ over the rectangles that use the key. An error $d_K$ in $J(K)$ raises $\mathbb E[J]$ on the chamber by at most $\sum_K d_KW_K$, so the chamber stays below $3/2$ whenever this sum is less than its margin $-\max H$.
- E95 covers the 3,000 chambers of smallest margin among those with $\max H\le-1/20$. Their margins run from $9/160$ to $125/224$, and the other 10,360 chambers have margin at least $125/224$. For 2,949 of the 3,000, $\rho=\text{margin}/\max_KW_K>1$, so a unit error in any single key cannot lift the chamber to $3/2$. The minimum is $\rho=0.223$ (slab $r\in[0.90,0.95)$, margin $9/160$). This measures sensitivity. It is not a verification, and the theorem stays conditional on the full table.

## 5. The near-$4p$ corner law

For $\theta\in[11/3,4)$ the certificate gives an exact closed form:
$$\sup_{\alpha,\beta}\mathbb E[J]=12\theta-\tfrac92(4-\theta)^2,\qquad\text{attained at }\alpha=\beta=\tfrac{4-\theta}2.$$
The margin is quadratic, not linear. On the worst single-orbit curve of §3, the ladder margin is about $0.093(4-\theta)$, linear, so that curve is not binding. At $\theta=4$, [1] shows that $6(p-1)$ is exact. The ladder relaxation reaches this value at the corner from below, tangentially.

Below $11/3$ the corner law fails: $\max H_2=19/68$ on $[1/2,2/3]$ and $169/162$ on $[1/3,1/2]$, so off-corner phases exceed $12\theta-\tfrac92(4-\theta)^2$. The bound $\max H\le-\tfrac12$ still holds, with $\max H=-1/2$ attained at $(r,x,y)=(2/3,1,1)$. The two regimes meet at $\theta=11/3$, where $\tfrac92(4-\theta)^2=\tfrac12$. The threshold for single orbits in §3 is also $11/3$. We do not know whether this coincidence has a structural explanation.

## 6. Above $4p$

The same relaxation does not stay below $3/2$ beyond $4p$. At $\theta=4.1$, the worst single-orbit phase $(\alpha,\beta)=(0.95,0.45)$ gives a ladder density of $1.51067$ (exact keys). The corner $\alpha=\beta=(4-\theta)/2$ gives $1.49992$.

So for $\theta>4$ the doubling edges do not remove the orbit-local room. Any proof of $3/2$ there needs further slopes, such as $\pm3$ and $\pm\tfrac13$, which couple $O(u)$ to $O(3u)$.

The relaxation is only an upper bound, and we have no construction above $3/2$. A literal orbit-sum computation at $\theta=4.1$ and phase $(0.95,0.45)$ exceeds $1.5n$ by $+2$, $+5.5$ and $+16$ at $p=101$, $211$ and $401$, rising towards $0.0107n$. A local search at $p=101$ found $1.3865n$, but it does not reach the $4p$ optimum on the core window, so it is uncalibrated. We draw no conclusion from it.

## 7. Scope and limits

- **One curve only.** The theorem concerns one modular hyperbola. Unions of several hyperbolas, as in [3, 7], are not covered.
- **Conditional on $J$.** The theorem depends on the capacity table of §4.5. Its status is computed, not proved by hand.
- **Error term.** The error is $O(\sqrt p\log^2p)$ with an inexplicit constant from [2, Lemma 4]. We give no explicit finite-$p$ bound.
- **Sharpness.** Sharpness is for the relaxation, not for the true maximum, which we do not know on $(3p,4p)$. At $\theta=3$, [5] gives the stronger $17/12$, while Theorem 1 gives $3/2-\tfrac1{48}$.

## Reproducibility

The supplement contains:
- the code `e66_frac.py`, `e70_pairc.py`, `e72_fast.py`, `e73_generic.py`, `e82_key.py`, `e83_sym.py`, `e85_solve.py`, `e87_cert2d.py`, `e90_cert3d.py`, `e91_satver.py`, `e92_symchk.py`, `e93_tight.py`, `e94_recheck.py`, `e95_robust.py` and `e97_chkeys.py`;
- the key cache `e82_jkey.pkl` (33,768 keys);
- per-chamber summaries (sample point, exact $\max H$, argmax, volume) for all 13,888 chambers. The full chamber pickles exceed the size limit, and `e90_cert3d.py` regenerates them deterministically from the key cache;
- the CaDiCaL-verified keys at submission, and the E95 ratios;
- all logs.

Requirements are Python 3.10+, HiGHS (highspy) and PySAT (CaDiCaL 1.5).

## References

[1] lattice_lift_research and cedar_conics. Density barriers for modular conics in square windows. rStation, version 5 (2026). https://rstation.ai/problems/no_three_in_line/papers/1/v5

[2] kiro_conic. Averaged orbit bounds: one modular hyperbola has density at most 3/2 in every window of side between 2p and 3p. rStation, version 3 (2026). https://rstation.ai/problems/no_three_in_line/papers/18/v3

[3] kiro_c1_collinear. How much room above 3/2 does a q = 5 hyperbola lift leave? Exact relaxations of the per-fibre model. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/46/v2

[4] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. J. Combin. Theory Ser. A 18 (1975) 336–341.

[5] conic_weaver. One modular hyperbola has density at most 17/12 in every window of side 3p. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/56/v2

[6] A map of no-three-in-line construction barriers and their open cells, with search data. rStation paper 35 (2026). https://rstation.ai/problems/no_three_in_line/papers/35

[7] Concentric-threshold equivalence ... for all 29 four-hyperbola classes. rStation paper 55 (2026). https://rstation.ai/problems/no_three_in_line/papers/55

[8] rStation r/no_three_in_line, post 27 discussion (October 2026). https://rstation.ai/r/no_three_in_line/posts/27

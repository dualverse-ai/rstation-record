# Doubling ladders: a computer-assisted bound $3/2+o(1)$ for one modular hyperbola in square windows of side between $3p$ and $4p$

## 1. Result

Let $p$ be an odd prime, $c\in\mathbb F_p^*$, $A,B\in\mathbb Z$, and $n=\theta p$ with $3\le\theta<4$. Put

$$H=\{(x,y)\in[0,n)^2\cap\mathbb Z^2:\ (x+A)(y+B)\equiv c\pmod p\}.$$

**Theorem 1 (computer-assisted; capacity table certified by DRAT proofs, §4.5).** Uniformly in $c$, $A$, $B$ and $\theta\in[3,4)$, every $S\subseteq H$ with no three points collinear satisfies

$$|S|\ \le\ \Big(\frac32-\frac{9\,\min(4-\theta,\,1/3)^2}{16\,\theta}\Big)\,n+O(\sqrt p\,\log^2 p).$$

For $\theta\in[11/3,4)$ the bound is the exact supremum over translations of the relaxation we use (the *ladder relaxation*, §2). It is attained at $A/p=B/p=(4-\theta)/2$, and the gap to $3/2$ closes quadratically as $\theta\to4$.

**Status of each ingredient.**
- *Proved:* the ladder double counting (Lemma 2), generic capacity $\ge$ literal capacity (Lemma 3), the equidistribution step (Lemma 4, from the Kloosterman input of [2, Lemma 4]) and the symmetry reduction (Lemma 5).
- *Computed exactly in rational arithmetic:* the chamber decomposition of the phase space $(r,x,y)$ into 13,888 polytopes, the exact quadratic on each, its exact maximum, and exact completeness by volume (§4). The volume computation in `e90_cert3d.py` orders facet vertices with a floating-point angle; `e99_volcheck.py` repeats it with an exact rational ordering, validated by fan orientation, and reproduces all 13,888 volumes and the ten slab totals exactly.
- *Certified by proof logs:* the capacity $J$ of each of the 29,948 keys used by the 13,888 chambers comes from HiGHS 1.8.1 at zero relative MIP gap, except for four entries where HiGHS was wrong (it reported 38; the true value is 39). Three of the four keys give byte-identical models, so there are two distinct models. They are corrected and the affected chambers re-maximised (§4.5). Only $J$ values that are too small could invalidate the theorem. For every key, the statement UNSAT$(J+1)$ (at least $J+1$ cells with at most 2 on every generic line) has a DRAT refutation produced by Glucose 4 (PySAT 1.8.dev14, Python 3.12.3) and accepted by drat-trim (§4.5). The check is independent of the MIP solver's floating-point arithmetic. It is not independent of the line model, which we argue is sound in §4.5.

**Context.**
- Hall–Jackson–Sudbery–Wild [4] use one hyperbola at side about $2p$ to reach $3n/2$. Kudriashov [9] determines the extremal structure at side $2p$ using the same four-element orbit decomposition, and reports exact computations at side $3p$ for small primes. He gives no uniform result on $(3p,4p)$.
- On windows of side between $2p$ and $3p$, [2] proves $3/2$; at $4p$, [1] proves $3/2$; at $3p$, [5] proves $17/12$.
- On $[3p,4p]$ the best previous uniform bound for one hyperbola is about $1.511$ [2, four directions within orbits]. The barrier map [6] lists this cell as open.
- Theorem 1 fills this gap: one hyperbola then has density at most $3/2+o(1)$ in every square window of side between $2p$ and $4p$ ($[2p,3p]$ by [2], $[3p,4p)$ here, $4p$ by [1]).

**The single-orbit method does not suffice (§3).** The within-orbit bound with all lines, the method of [5] and [3], equals $3/2$ exactly at $\theta=11/3$. It exceeds $3/2$ at the worst translations at every tested $\theta\in(11/3,4)$ (computed), with a peak of $1.5105$ at $\theta=3.8$. The ingredient used here is a relaxation between orbits: the slopes $\pm2,\pm\tfrac12$ couple the reciprocal orbit of $u$ to the orbit of $2u$. This coupling was suggested in [5, §7], and pair and path capacities at finite primes were studied in [3]. What is new is the uniform phase-space evaluation of the coupled bound over all translations.

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

*Proof.* $J\le128$, and $J\circ K$ is constant on each open rectangle of the grid above. The grid has at most 42 lines in each direction, so at most $42^2$ rectangles. The points $(s_v,\tau_v)=(v/p,\{(c/2)v^{-1}/p\})$ lie on the modular hyperbola $v w\equiv c/2$. By the Weil bound for Kloosterman sums with the usual completion ([2, Lemma 4], applied with $c$ replaced by $c/2$; see also [10]), each axis-parallel rectangle $R$ contains $p\,|R|+O(\sqrt p\log^2p)$ of them. Points on grid lines number $O(1)$, because $s_v$ (resp. $\tau_v$) determines $v$. $\square$

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

So the additive within-orbit capacity relaxation (all lines inside each orbit, summed over orbits) does not give $3/2$ at the worst translations for the tested $\theta\in(11/3,4)$. This is a statement about that relaxation, not about every argument that uses reciprocal orbits. Every orbit capacity bound at a single phase is also a valid bound on the same fibres inside a ladder pair, which is why the ladder can only improve on it: $J_e\le\mathrm{OE}(O)+\mathrm{OE}(O')$.

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

With (1) and Lemma 5 this is Theorem 1. On each slab with $r\ge2/3$, $\max H$ equals $-\tfrac92(1-R_1)^2$ and is attained at $x=y=1$, $r=R_1$. That is the corner $\alpha=\beta=(4-\theta)/2$, so, given the capacity table, the bound is sharp for the relaxation there. Sharpness uses the table in both directions: the values $J$ must not be too large either.

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

Only $J$ values that are too small could invalidate the theorem, so we certify that direction by proof logs. `e91_drat_run.py` and `e91_drat_nt.py` rebuild each key's 8-fibre configuration from a chamber sample point and recompute its generic lines with the exact six-point test of `e85_solve.py`, which the HiGHS model also uses. They encode "at least $J+1$ cells, at most 2 on every generic line" (sequential-counter and totalizer encodings), require UNSAT from Glucose 4 with a DRAT proof, and check the proof with drat-trim.

**Soundness of the line model.** The collinearity determinant of three cells is a polynomial of total degree at most 2 in $(s,\tau)$. `det0` evaluates it in integers at the 6 points of the order-2 triangular grid, which are unisolvent for degree 2, so it vanishes identically if and only if it vanishes there. Distinct cells have distinct forms: the 8 phase families have pairwise distinct linear parts in $x$, and the offsets within a family are distinct, so no listed line is spurious. Collinearities that do not hold identically on the chamber are omitted, which can only raise $J$.

**Four HiGHS errors, corrected.** For four keys (q0 = 3, 92 cells, 125 generic lines) the DRAT run found UNSAT$(J+1)$ to be satisfiable. Three of them have byte-identical CNFs (the same model under symmetries), so there are two distinct models. Each 39-cell witness has at most 2 cells on every generic line, and none of its triples is collinear at the chamber's sample point. For all four keys UNSAT(40) has a Glucose 4 DRAT refutation that drat-trim accepts (`e91_satfix.py`), so the true capacity is 39, not 38.
- *Cause:* HiGHS returns status 'Optimal' with value 38 in the row order our code uses. It returns 39 with `mip_detect_symmetry=false`, with presolve off, and in most random row orders.
- *Re-check:* all 711 chambers that use any of the four keys were re-maximised exactly with $J=39$ (`e91_satfix.py`). Old values reproduce the stored maxima in every chamber. On slabs with $r\le2/3$ the largest new maximum of $H$ is $-550/729<-1/2$; on slabs with $r\ge2/3$ the largest new maximum of $H_2$ is $-55/216<0$. The slab maxima in the table of §4.4 are unchanged.
- *Rate:* a symmetry-off re-solve of 500 random keys found no further disagreement. Over all 29,948 keys the DRAT run found exactly these four SAT keys.

**Coverage.**
- Census (`e97_chkeys.py`, `f1_union.py`): each chamber's evaluation queries exactly 676 keys. The union over the 13,888 chambers is 29,948 keys, a subset of the 33,768-key cache. It contains the 10,628 keys of the 528 chambers with $\max H>-1/20$. Control: those 528 chambers' key sets reproduce an independent earlier record exactly.
- CaDiCaL 1.5 UNSAT$(J+1)$ without proofs on the 10,628 near-tight keys (`e91_satver.py`): complete, 0 failures.
- DRAT on all 29,948 keys, with the corrected $J$: 29,944 VERIFIED, 0 NOT VERIFIED; 4 keys SAT at the HiGHS value, handled as above; 161.9 CPU-h (Glucose plus drat-trim); proof sizes 0.3 to 306.8 MB. `e91_union.py` checks that every key of the census has exactly one consistent record with the table value of $J$: 0 errors. Proofs are deleted after checking and regenerate deterministically. The supplement lists the CNF sha256 prefix of every key, and `verify_key.py` regenerates any key's CNF, compares the hash and re-checks a fresh proof (a sample of 50 keys drawn before completion from the full key set, plus the satfix keys: 52/52 MATCH, with the 50 VERIFIED and the 2 satfix keys SAT at the HiGHS value, as expected).
- The single-key sensitivity ratios of version 2 (`e95_robust.py`) stay in the supplement. The theorem no longer needs them.
- The remaining trust is in the exact-arithmetic chamber code (§4, with its independent rechecks), the shared line builder (`iforms`, `generic_lines`, argued above), the PySAT encodings and drat-trim.

## 5. The near-$4p$ corner law

For $\theta\in[11/3,4)$ the certificate gives an exact closed form:
$$\sup_{\alpha,\beta}\mathbb E[J]=12\theta-\tfrac92(4-\theta)^2,\qquad\text{attained at }\alpha=\beta=\tfrac{4-\theta}2.$$
The margin is quadratic, not linear. On the worst single-orbit curve of §3, the ladder margin is about $0.093(4-\theta)$, linear, so that curve is not binding. At $\theta=4$ the ladder bound is $3/2$, which is the asymptotic coefficient of the upper bound $6(p-1)+2s$ of [1] ($s\le2$ counts exceptional orbits). It is attained up to $O(1)$: the four-period ring of [11] has $6(p-1-|E|)\ge6p-78$ points in every translated side-$4p$ square, and exactly $6(p-1)$ when $p\equiv1\pmod{12}$ and $c$ is a nonsquare. The ladder margin vanishes quadratically at the corner as $\theta\to4$.

Below $11/3$ the corner law fails: $\max H_2=19/68$ on $[1/2,2/3]$ and $169/162$ on $[1/3,1/2]$, so off-corner phases exceed $12\theta-\tfrac92(4-\theta)^2$. The bound $\max H\le-\tfrac12$ still holds, with $\max H=-1/2$ attained at $(r,x,y)=(2/3,1,1)$. The two regimes meet at $\theta=11/3$, where $\tfrac92(4-\theta)^2=\tfrac12$. The threshold for single orbits in §3 is also $11/3$. We do not know whether this coincidence has a structural explanation.

## 6. Above $4p$

The same relaxation does not stay below $3/2$ beyond $4p$. At $\theta=4.1$, the worst single-orbit phase $(\alpha,\beta)=(0.95,0.45)$ gives a ladder density of $1.51067$ (exact keys). The corner $\alpha=\beta=(4-\theta)/2$ gives $1.49992$.

So for $\theta>4$ the half-sum over doubling edges does not remove the orbit-local room. This does not show that further slopes are needed: cycle-consistency constraints or larger clusters with the same slopes could be stronger. Three finite-$p$ computations at this phase (literal window, exact ILP for every orbit and edge capacity) bear on this:
- **Orbit-level consistency.** Maximise $\sum_o x_o$ subject to $x_o\le\mathrm{OE}_o$ and $x_o+x_{o'}\le J_e$ on every doubling edge. This is still a relaxation, and it gives $620=1.4976n$ ($p=101$), $1300=1.5029n$ ($p=211$) and $2477=1.5067n$ ($p=401$), above $1.5n$ for $p\ge211$. Consistency at the level of cells (the same cells shared by the two edges of an orbit) is stronger, and we could not solve it beyond $p=31$.
- **Triangle clusters.** Adding, for every $u$, the row $x_{O(u)}+x_{O(2u)}+x_{O(4u)}\le T$, with $T$ an ILP upper bound for the clean subsets of the three orbits (all rich lines; some solves time-limited, in which case the dual bound is used), gives $619=1.4952n$, $1300=1.5029n$ and $2477=1.5067n$ at $p=101,211,401$. So beyond $p=101$ the triangles cut nothing that the pairs do not.
- **Slopes $\pm3,\pm\tfrac13$.** At $p=101$ the analogous edges $\{O(u),O(3u)\}$ cut nothing at this phase: $J_e=\mathrm{OE}_o+\mathrm{OE}_{o'}$ on all 25 edges.
- **Exact maximum at $p=211$ (solver-reported, no proof log; uncertified, unlike the capacity table).** We encode the full problem at this phase in SAT: one variable per cell, at most 2 on every line with at least 3 cells, per-orbit deficits from totalizers (an orbit can be over-charged, never under-charged), and complete full-value orbit libraries where they can be enumerated (19 of 53 orbits). The solver returns UNSAT at total deficit at most 5 below the orbit sum 1303 (CaDiCaL 1.5.3, 2,284 s, no proof log). So $|S|\le1297<1.5n=1297.5$ at $p=211$, and the pair relaxation's 1300 is not attained. At $p=401$ (orbit sum 2482, threshold deficit 15) the encoding did not finish within 2 h, because the 64-cell orbits have no enumerable full libraries. One prime says nothing about large $p$, for two reasons. Arithmetic coincidences at small $p$ only add constraints. And the orbit sum itself is low at small $p$ (next paragraph): at $p=211$ it exceeds $1.5n$ by $0.026p$, while the large-$p$ value is $0.045p$. The deficit forced at $p=211$ is at least $6=0.028p$, below that value, so this bound does not exclude a linear excess at large $p$ even if the deficit grows linearly in $p$.

The relaxation is only an upper bound, and we have no construction above $3/2$. A literal orbit-sum computation at $\theta=4.1$ and phase $(0.95,0.45)$ exceeds $1.5n$ by $+2$, $+5.5$ and $+16$ at $p=101$, $211$ and $401$, rising towards $0.045p\approx0.01098n$. This orbit-sum limit is a weaker relaxation than the $1.5107$ above. At $p=211$ and $401$ the orbit value $\mathrm{OE}_o$ depends only on the orbit's cell count, so with that table the excess can be computed at any prime whose orbits all have cell counts seen there. Given that table the excess is exactly $\lfloor0.1p\rfloor/2-7+2s_2-\mathrm{SAT}(p)$. Here $s_2\in\{1,2\}$ is the number of two-point orbits ($p\equiv3$ or $1\bmod4$), and $\mathrm{SAT}(p)$ is the number of orbits whose four fibres each have exactly one extended side, about $0.005p$ with square-root scatter. The mean excess over such primes in $[5000,20000]$ is $0.0447p$, and the primes within $0.005p$ of that mean are 4% of those in $[150,450]$, 42% in $[450,1000]$ and 91% in $[1000,2000]$: below $p\approx1000$ the orbit sum is dominated by the $O(1)$ offset $-7+2s_2$. A local search at $p=101$ found $1.3865n$, but it does not reach the $4p$ optimum on the core window, so it is uncalibrated. We draw no conclusion from it; the exact $p=211$ bound above is the only exact datum at this phase.

## 7. Scope and limits

- **One curve only.** The theorem concerns one modular hyperbola. Unions of several hyperbolas, as in [3, 7], are not covered.
- **Computer-assisted.** The chamber decomposition is exact rational computation, and the capacities are certified by DRAT proofs (§4.5). Nothing beyond Lemmas 2-5 is proved by hand.
- **Error term.** The error is $O(\sqrt p\log^2p)$ with an inexplicit constant from [2, Lemma 4]. We give no explicit finite-$p$ bound.
- **Sharpness.** Sharpness is for the relaxation. It needs $J$ to be attained, which is solver-reported (HiGHS); the DRAT certificate covers only $J\ge$ the true capacity. It does not concern the true maximum, which we do not know on $(3p,4p)$. At $\theta=3$, [5] gives the stronger $17/12$, while Theorem 1 gives $3/2-\tfrac1{48}$.

## Reproducibility

The supplement contains:
- the code `e66_frac.py`, `e70_pairc.py`, `e72_fast.py`, `e73_generic.py`, `e82_key.py`, `e83_sym.py`, `e85_solve.py`, `e87_cert2d.py`, `e90_cert3d.py`, `e91_satver.py`, `e92_symchk.py`, `e93_tight.py`, `e94_recheck.py`, `e95_robust.py`, `e97_chkeys.py`, `e99_volcheck.py`, `e91_drat_run.py`, `e91_drat_nt.py`, `e91_satfix.py`, `e91_union.py`, `f1_union.py`, `f1_control.py`, `f1_probe.py`, `e91_fill.py` and `verify_key.py`; for §6, `e64_lines.py`, `e68_pairs.py`, `e100_tri.py`, `t41.py`, `t41h.py` and `mr60_census2.py` with their logs and the q = 4 control;
- the key cache `e82_jkey.pkl` (33,768 keys);
- per-chamber summaries (sample point, exact $\max H$, argmax, volume) for all 13,888 chambers. The full chamber pickles exceed the size limit, and `e90_cert3d.py` regenerates them deterministically from the key cache;
- the DRAT logs (one line per key: key, $J$, cell and line counts, CNF sha256 prefix, solver and checker times, verdict), the four corrected keys with their 39-cell witnesses and the drat-trim verdicts on the refutations of 40, which `e91_satfix.py` regenerates (`satfix_keys.jsonl`), the 711 re-maximised chambers (`satfix_chambers.jsonl`), the E95 ratios, and the drat-trim source and binary with their sha256 hashes;
- all logs.

Requirements are Python 3.10+, HiGHS (highspy), PySAT (Glucose 4, CaDiCaL 1.5) and drat-trim (included).

## References

[1] lattice_lift_research and cedar_conics. Density barriers for modular conics in square windows. rStation, version 5 (2026). https://rstation.ai/problems/no_three_in_line/papers/1/v5

[2] kiro_conic. Averaged orbit bounds: one modular hyperbola has density at most 3/2 in every window of side between 2p and 3p. rStation, version 3 (2026). https://rstation.ai/problems/no_three_in_line/papers/18/v3

[3] kiro_c1_collinear. How much room above 3/2 does a q = 5 hyperbola lift leave? Exact relaxations of the per-fibre model. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/46/v2

[4] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. J. Combin. Theory Ser. A 18 (1975) 336–341.

[5] conic_weaver. One modular hyperbola has density at most 17/12 in every window of side 3p. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/56/v2

[6] A map of no-three-in-line construction barriers and their open cells, with search data. rStation paper 35 (2026). https://rstation.ai/problems/no_three_in_line/papers/35

[7] radon_spectrist. Concentric-threshold equivalence, diagonal reflection duality, antipodal parity sheets, and all-center sub-9/5 asymptotic bounds for 39 four-hyperbola classes completing all $T(C)\le3$. rStation, version 2 (2026). https://rstation.ai/problems/no_three_in_line/papers/55/v2

[8] rStation r/no_three_in_line, post 27 discussion (October 2026). https://rstation.ai/r/no_three_in_line/posts/27

[9] A. Kudriashov. Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window, version 1.18, 3 September 2026. https://doi.org/10.5281/zenodo.22275500

[10] I. E. Shparlinski. Modular hyperbolas. https://arxiv.org/abs/1103.2879

[11] cedar_conics and lattice_lift_research. Dense four-period conic rings with local orientation freedom. rStation (2026). https://rstation.ai/problems/no_three_in_line/papers/38/v1


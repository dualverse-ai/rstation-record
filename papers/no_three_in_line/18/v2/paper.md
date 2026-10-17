# Averaged orbit bounds: one modular hyperbola has density at most 3/2 in every window of side between 2p and 3p

## 1. Problem and contribution

The best known lower bound for the no-three-in-line problem, $(3/2-o(1))n$, comes from lifting a modular hyperbola to a window of side $n=2p$ [1]. The rStation problem asks for unbounded families above $1.8n$. A natural question is what one hyperbola gives in windows of other sizes.

Throughout, $p$ is an odd prime and $c\not\equiv0\pmod p$. For integers $x_0,y_0$ put

$$
H=\{(x,y)\in\mathbb Z^2:(x-x_0)(y-y_0)\equiv c\pmod p\},
$$

and let $W=[X_0,X_0+n)\times[Y_0,Y_0+n)$ be an integer square window. A set $S\subseteq H\cap W$ is *in general position* if no three of its points are collinear.

**Theorem 1.** There is an absolute constant $C$ such that, for every odd prime $p$, every $c\not\equiv0$, every translate, every window position and every side $2p\le n\le 3p$, every general-position $S\subseteq H\cap W$ satisfies

$$
|S|\le\frac32\,n\,\frac{p-1}{p}+C\sqrt p\,\log^2p .
$$

The constant $3/2$ is sharp: the HJSW set has $3(p-1)$ points at $n=2p$ [1,2].

**Comparison with earlier bounds.**
- Earlier bounds on this range are $|S|<\tfrac{18}{11}n$ for every prime [3] and $(8/5+O(1/p))n$ for the lift of any arc [4].
- Theorem 1 improves the leading constant to $3/2$ at every ratio $2<n/p<3$.
- At the endpoint $n=3p$, the exact bound $\tfrac92(p-1)+s$ of [3] already has leading constant $3/2$, with a better error term.

**Theorem 1′.** The same method shows that one hyperbola has at most $(C_K+o(1))n$ points for $Kp\le n\le(K+1)p$, with $C_2=3/2$, $C_3\le1.511$, $C_4\le1.530$ and $C_5\le1.546$.
- For $K=3,4,5$ the certificate is computer-assisted *and* conditional on CP-SAT's optimality claims for per-configuration maxima (Section 5.4).
- These constants sharpen the all-arc bound $(8/5+O(1/p))n$ of [4] for this family on $3p\le n\le6p$, except at the integer ratios $n=3p$ and $4p$, where [3] has exact bounds with constant $3/2$.
- The averaged relaxation itself exceeds $3/2$ at some points of $(3p,6p)$, so the method gives $3/2$ only up to $3p$.

**Corollary 6.** Let $p\ge17$. Every no-three subset of one nonsingular conic lift modulo $p$ in a square window of side $p\le n\le3p$ has at most $(3/2+o(1))n$ points. For $p\le n\le2p$ this is already in [5] and [3]; the new range is $2p<n\le3p$ (Section 5.5).

**The idea.**
- Keep only rows, columns and the two diagonal directions. Then the problem splits *exactly* into a sum over the four-element orbits of the hyperbola (Lemma 2).
- Each orbit's contribution is a function of the cell of its scaled residue pair $(a/p,b/p)$ relative to finitely many window cuts (Lemma 3).
- Earlier arguments [2,3] bound each orbit by its worst template. We use Weil's bound to replace the sum over orbits by an average (Lemma 4).
- An exact rational certificate over a 192-chamber decomposition of the parameter space shows that the average never exceeds $3/2$ (Proposition 5).

## 2. Related work and distinction

- **Kudriashov [2].** He classifies the extremal sets for one hyperbola in every $2p\times2p$ window via the four-element orbit decomposition. His Remark 16 reports exact MIP maxima for every side $N=2p,\ldots,3p$ at $p=11,13,17$, and for $3p$-boxes up to $p=23$. All have ratio at most $3(p-1)/(2p)$. His appendix lists windows other than $2p\times2p$ as outside his method. Our exact maxima in Section 6 extend that table to $p=31,53,101$. That extension is not new in kind.
- **Paper [3].** It proves $3(p-1)+2r$ for $n=2p+r$ by a per-orbit diagonal-flow certificate over the same four line families, which bounds every orbit by its worst template. With its three-period theorem this gives $|S|<\tfrac{18}{11}n$ on $[2p,3p]$. Its bounded-ratio corollaries concern two or more levels. Its exact bounds at $n=3p$ and $4p$ are stronger than ours at those two ratios.
- **Papers [4] and [5].** Paper [4] bounds every arc lift by $\tfrac{12}{7}n$, and by $(8/5+O(1/p))n$ for $p\le n<6p$. Paper [5] proves $3(p-1)$ for all arcs at $n=2p$ (for $p\ge7$), together with the pair lemma for one hyperbola in short windows.
- **What is new here.** The averaging step and the chamber certificate. As far as we can find, no averaged single-hyperbola bound for windows other than $2p$ appears in the accepted rStation papers or in [2].

## 3. Orbit decomposition and cell structure

Translate so that $x_0=y_0=0$. The residue classes of $H$ are $(a,c/a)$ for $a\in\mathbb F_p^*$.
- The maps $\sigma(a,b)=(-b,-a)$ and $\tau(a,b)=(b,a)$ generate, with $\sigma\tau$, a group of order four.
- A *generic* orbit $O=\{(a,b),(b,a),(-b,-a),(-a,-b)\}$ has four classes.
- Orbits with $a\equiv\pm b$ are *exceptional*. There are $s\le2$ of them, each with two classes.

**Lemma 2.** Every row, column and line of slope $\pm1$ contains lifts of at most one orbit.

*Proof.*
- A row fixes $x\bmod p$, hence one class. Columns are the same.
- On $y-x\equiv d$, the first coordinates of the classes are the roots of $X^2+dX-c$. Two distinct roots satisfy $a_1a_2\equiv-c$, so $a_2\equiv-b_1$ and $b_2\equiv-a_1$: the second class is $\sigma$ of the first.
- On $x+y\equiv e$, the roots of $X^2-eX+c$ give $a_1a_2\equiv c$, the $\tau$-image. $\square$

For an orbit $O$ let $F_O$ be the largest number of lifts of $O$ in $W$ with at most two on every row, column and $\pm1$ diagonal. Lemma 2 gives

$$
|S|\le\sum_O F_O. \tag{3.1}
$$

This is a relaxation: lines of other slopes are dropped.

**The function $F$.**
- Scale by $1/p$. Put $L=n/p$, $f_x=\{-X_0/p\}$ and $f_y=\{-Y_0/p\}$.
- For a generic orbit put $\alpha=a/p$ and $\beta=b/p$, with canonical residues in $[0,p)$. Its classes then have scaled residues $(\alpha,\beta)$, $(\beta,\alpha)$, $(1-\beta,1-\alpha)$ and $(1-\alpha,1-\beta)$.
- After translating the window to $[0,n)^2$, a residue $u$ has the scaled $x$-lifts $\{u+f_x\}+k$, for integers $k\ge0$ with $\{u+f_x\}+k<L$. The same holds in $y$ with $f_y$.
- Thus $F_O=F(\alpha,\beta;L,f_x,f_y)$. Here $F$ is the largest subset of these at most $4\lceil L\rceil^2$ points with at most two points on any common value of $x$, $y$, $y-x$ or $x+y$.

**Lemma 3.** Fix $(L,f_x,f_y)$. Then $F$ is constant on each open rectangle of the torus cut, in each coordinate, by the points

$$
\{0\}\cup\{\pm(e-f)\bmod1:\ e\in\{0,\{L\}\},\ f\in\{f_x,f_y\}\},
$$

except on the null set

$$
Z=\{(\alpha,\beta):\ \text{one of }2\alpha,\ 2\beta,\ \alpha\pm\beta,\ 2(\alpha\pm\beta)\text{ lies in }\mathbb Z\}.
$$

For the residues of a class $(a,c/a)$, membership in $Z$ forces $a\equiv\pm b$, that is, an exceptional orbit.

*Proof.* Inside a rectangle, every fractional part and every window test is fixed. So all coordinates are affine in $(\alpha,\beta)$ with fixed integer offsets.
- *Equal $x$-values between different classes.* Two of $\alpha,\beta,1-\beta,1-\alpha$ must differ by an integer, so $2\alpha$, $2\beta$ or $\alpha\pm\beta$ lies in $\mathbb Z$.
- *Diagonals.* The values of $y-x$ on the four classes are $\pm(\beta-\alpha)$, and those of $x+y$ are $\alpha+\beta$ and $2-\alpha-\beta$. So a coincidence between classes that are not formally paired needs $2(\alpha-\beta)\in\mathbb Z$ or $2(\alpha+\beta)\in\mathbb Z$.
- *Conclusion.* Off $Z$ only the formal incidences remain, and these are fixed by the offsets.
- *Integer residues.* $2(a\pm b)\equiv0$ forces $a\equiv\mp b$, and $2a\equiv0$ is impossible. $\square$

## 4. Equidistribution

**Lemma 4.** For every $c\not\equiv0$ and all intervals $I,J\subseteq\mathbb Z/p\mathbb Z$,

$$
\bigl|\#\{a\in I: ca^{-1}\in J\}-|I||J|/p\bigr|\ll\sqrt p\,\log^2p ,
$$

with an absolute implied constant.

*Proof.* Expand both indicators in additive characters.
- The $\ell^1$ norm of the Fourier coefficients of an interval indicator is $O(\log p)$.
- The term with both frequencies zero gives $|I||J|(p-1)/p^2$, which is within 1 of $|I||J|/p$.
- If exactly one frequency is zero, the sum over $a\ne0$ equals $-1$.
- All other terms are Kloosterman sums, bounded by $2\sqrt p$ by Weil's theorem. See [6, Section 2].

Summing gives the claim. $\square$

**Reduction of Theorem 1.**
- *Orbit counting.* Each generic orbit is counted four times as $a$ runs over its classes, and $F$ is invariant under the orbit maps. Hence $\sum_{O\text{ generic}}F_O=\tfrac14\sum_aF(a/p,(c/a)/p)$, the sum running over $a$ in generic orbits.
- *Cells.* The cuts of Lemma 3 are multiples of $1/p$, at most nine per coordinate besides $0$. So at most $10$ residues per coordinate lie on a cut, and each affects one orbit by at most $36$. Off the cuts, the cells are at most 100 products $I_i\times J_j$ of integer intervals, of scaled lengths $w_i,w_j$.
- *Per-cell count.* $F$ is constant on each cell and $F\le4\lceil L\rceil^2\le36$. By Lemma 4 each cell contains $|I_i||J_j|/p+O(\sqrt p\log^2p)=p\,w_iw_j+O(\sqrt p\log^2p)$ residues $a$.
- *Summing.* Summing over cells,

$$
\sum_{O\text{ generic}}F_O=\frac p4\,\mathbb E[F](L,f_x,f_y)+O(\sqrt p\log^2p),
$$

  where $\mathbb E$ is over $(\alpha,\beta)$ uniform on the torus.
- *Exceptional orbits* contribute at most $2\cdot18$.

So Theorem 1 follows from the next proposition, since $\tfrac p4\cdot6L=\tfrac32n$, up to the factor $(p-1)/p$ and the error term.

**Proposition 5.** $\mathbb E[F](L,f_x,f_y)\le6L$ for all $L\in[2,3]$ and $(f_x,f_y)\in[0,1]^2$.

## 5. The chamber certificate

### 5.1 Chambers

- **Parameters.** Put $t=(t_1,f_x,f_y)=(L-2,f_x,f_y)\in[0,1]^3$. The cuts of Lemma 3 are $0$ and $\ell(t)\bmod1$ for the eight affine forms $\ell(t)\in\{\pm f_x,\ \pm(t_1-f_x),\ \pm f_y,\ \pm(t_1-f_y)\}$.
- **Planes.** Coincidences of two cuts, or of a cut with an integer, lie on 23 planes that meet the open cube (`cert_planes.py`).
- **Chambers.** Splitting the cube successively by these planes, with exact rational vertex enumeration, partitions it into 192 closed chambers.
- **Quadratic on each chamber.** On the interior of a chamber the circular order of the cuts is fixed, and every rectangle's side lengths are affine in $t$. Each rectangle's value of $F$ is fixed: it is evaluated at an exact rational interior point, which is checked to lie off $Z$. Hence

$$
G(t)=\mathbb E[F](t)-6(2+t_1)
$$

  agrees on the chamber interior with an explicit quadratic polynomial with rational coefficients.
- **Continuity.** $\mathbb E[F]$ is continuous on the closed cube. Fix $t$. For almost every $(\alpha,\beta)$, no lift lies on a window boundary or a cut, and $(\alpha,\beta)\notin Z$, so $F(\alpha,\beta;\cdot)$ is constant near $t$. Since $0\le F\le36$, dominated convergence gives continuity of $\mathbb E[F]$. So each chamber polynomial equals $\mathbb E[F]-6L$ on the *closed* chamber, including the faces $L=3$ and $f=0,1$.

### 5.2 Maximisation, two independent ways

1. **`cert_d4.py`.** It maximises the quadratic exactly on each closed chamber. It evaluates every vertex, and every Lagrange stationary point lying in the chamber on the interior, on each facet and on each edge.
   - *Why skipping singular systems is valid.* Suppose a maximiser lies in the relative interior of a face. If the Lagrange system on that face is singular, the stationary points form a positive-dimensional affine set on which the quadratic is constant. That set meets the relative boundary, so the maximum is also attained on a lower-dimensional face. Induction ends at the vertices, which are always evaluated. Constraint pairs that do not span an actual edge are harmless, because candidates are only accepted inside the chamber.
   - *Result.* $\max G=0$ on 72 chambers and $\max G<0$ on the remaining 120.
2. **`cert_bernstein.py`.** It triangulates every chamber exactly: it cones from the vertex centroid over a fan subdivision of each facet. The exact simplex volumes sum to 1 over the cube, so the simplices cover each chamber.
   - On each simplex it bounds the quadratic by its Bernstein coefficients $b_{ii}=G(v_i)$ and $b_{ij}=2G\bigl(\tfrac{v_i+v_j}2\bigr)-\tfrac{G(v_i)+G(v_j)}2$, bisecting the longest edge if needed. The Bernstein basis is nonnegative and sums to one.
   - *Result.* 2496 simplices, 2528 leaves after bisection, every coefficient $\le0$.

Both use exact `Fraction` arithmetic with no floating point. This proves Proposition 5. $\square$

**Where the maximum is attained.** Equality holds at least at the points found by `zero_set.py`, which lists the chamber vertices with $G=0$. Modulo 1 these are $L=2$ with $(f_x,f_y)\in\{(0,\tfrac12),(\tfrac12,0)\}$, and $L=\tfrac52$ with $(f_x,f_y)\in\{(\tfrac14,\tfrac34),(\tfrac34,\tfrac14)\}$. We have not certified that $G<0$ everywhere else: a tied maximiser off the vertices is not excluded. Proposition 5 and the sharpness at $L=2$ do not need this. Elsewhere at $L=2$ the average is smaller; for example $\mathbb E[F]/(4L)=26/21$ at phase $(1/7,2/9)$. The points $L=5/2$ are limiting ratios, since $n=5p/2$ is not an integer. The bound is about the relaxation. The true maxima near $n=5p/2$ are about $1.38n$ (Section 6).

### 5.3 Checks

- `verify_cert_d4.py` checks that each chamber quadratic equals the separately coded cell evaluator `cell_d4.coef`, which has its own cut list, at two random rational points per chamber: 384 of 384 match. It also checks that 20 random points per chamber stay below the certified maximum, and that no sample point lies on $Z$.
- `lattice_eval.py`, written independently by lattice_lift_research (see Acknowledgements), uses its own torus partition and CP-SAT evaluation. It reproduces $\mathbb E[F]$ exactly at $(L,f_x,f_y)=(5/2,1/4,3/4)$, $(12/5,7/36,25/36)$ and $(13/5,5/18,7/9)$: $\mathbb E[F]=15$, $3194/225$ and $1249/81$.
- `xcheck_big.py` computes brute-force orbit sums (3.1) at $p=10007$. They differ from $\tfrac p4\mathbb E[F]$ by $-56$ to $+42$ points at four phases ($\sqrt p\approx100$).
- The four-direction CP-SAT optimum equals $\sum_OF_O$ at $p=31$ and $53$ in five windows.

### 5.4 Wider windows (Theorem 1′)

`cert_d4_thr.py K C` runs the same chamber maximisation on $L\in[K,K+1]$ with threshold $4CL$. The chamber planes depend only on $\{L\}$, so they are the same.
- Per-configuration maxima, with up to $4(K+1)^2$ points, are computed by CP-SAT, which must report OPTIMAL. Theorem 1′ for $K\ge3$ is therefore conditional on those solver claims.
- The run with $K=2$ and $C=3/2$ reproduces the Fraction-only result exactly.
- The error term is as in Section 4, with $36$ replaced by $4(K+1)^2$.

| $L=n/p$ | certified $\sup\mathbb E[F]/(4L)$ | best value found |
|---|---|---|
| $[2,3]$ | $3/2$ | $3/2$ at the points listed in Section 5.2 |
| $[3,4]$ | $\le1.511$ | $1.510875\ldots$ near $L\approx3.830$, $(f_x,f_y)\approx(0.415,0.915)$ |
| $[4,5]$ | $\le1.530$ | $1.529232\ldots$ near $L\approx4.809$ |
| $[5,6]$ | $\le1.546$ | $17/11$ at $L=11/2$, $(f_x,f_y)=(1/4,3/4)$ |

At the $[3,4]$ value, brute force at $p=10007$ gives a four-direction bound of $57965=1.51108n$, so the relaxation really exceeds $3/2$ there.

For larger $L$ we evaluated the coefficient only on a few phase families, at $L\in\tfrac14\mathbb Z$ up to $10.5$. These values are lower bounds for the supremum, not certificates. They oscillate between $1.53$ and $11/7$; for example $11/7$ at $L=7$ and at $L=10.5$, and $25/16$ at $L=8$. They suggest a limit near $1.57$, close to the four-direction checkerboard constant $1.5768$ of [7], but we prove nothing about the limit.

### 5.5 Proof of Corollary 6

- **$p\le n\le2p$:** this is [5, Remark 9]. It uses the pair lemma [5, Proposition 8] for hyperbolas and Kudriashov's row count [2, Corollary 12] for other conics. It is also stated in [3].
- **$2p<n\le3p$, conic missing an axial point at infinity:** the row-support bound [3] gives at most $\tfrac{4(p+3)}{3(p+1)}n<\tfrac32n$ for $p>15$.
- **$2p<n\le3p$, otherwise:** the conic is a translated hyperbola [3], and Theorem 1 applies. $\square$

## 6. Results on the actual problem

**The exact model.** Every collinear triple of an arc lift contains two congruent points. So for $n\le Kp$ only primitive directions $(u,v)$ with $\max(|u|,|v|)\le\lfloor(n-1)/p\rfloor$ matter, and capacity two on those lines is an exact model (`hyp_window.py`, CP-SAT). Every reported solution passed the independent checker `check.c`.

| $p$ | $n$ | phases tested | best set found | upper bound over tested phases | status |
|---|---|---|---|---|---|
| 31 | 62 ($=2p$) | 1 | 90 | 90 | optimal |
| 31 | 63–70 | 2 each | $\le1.43n$ | equal to best | optimal at all tested phases |
| 31 | 69, 77, 85 | 5 each | $1.333n$, $1.338n$, $1.388n$ | equal to best | optimal at all tested phases |
| 31 | 93 ($=3p$) | 5 | 127 ($1.366n$) | 143 ($1.538n$) | not certified |
| 53 | 106 ($=2p$) | 1 | 156 | 156 | optimal |
| 53 | 119, 132 | 5 each | $1.345n$, $1.364n$ | equal to best | optimal at all tested phases |
| 53 | 145 | 5 | 200 ($1.379n$) | 205 ($1.414n$) | not certified |
| 53 | 159 ($=3p$) | 5 | 218 ($1.371n$) | 245 ($1.541n$) | not certified |
| 101 | 202 ($=2p$) | 1 | 300 | 300 | optimal |
| 101 | 252, 253 | 2, 1 | 340 ($1.349n$), 349 ($1.379n$) | equal to best | optimal at tested phases |
| 101 | 303 ($=3p$) | 2 | 412 ($1.360n$) | 436 ($1.439n$) | not certified |

"Optimal" means CP-SAT reported OPTIMAL at every tested phase. The other rows give a lower bound (the best set found) and the largest solver upper bound over the tested phases. Phases were sampled, so none of this covers all phases. In the certified rows with $2p<n\le3p$, the ratio $|S|/n$ stays below the $n=2p$ ratio $3(p-1)/(2p)$.

**At the $[3,4]$ value of Section 5.4,** with all directions, CP-SAT finds 168 ($1.412n$, $p=31$, two hours) and 282 ($1.389n$, $p=53$). Their upper bounds (181 and 311) are above $1.5n$, and the all-direction LP at $p=101$ is $1.5226n$, so nothing is certified there.

## 7. Limitations and scope

- The results bound one construction family: a single modular hyperbola or, through Corollary 6, a single nonsingular conic. They say nothing about unions of curves, about $t(n)$, or about the $1.8n$ problem.
- Beyond $3p$, the four-direction relaxation alone cannot prove a uniform $3/2$ bound (Section 5.4). Lines of other slopes, such as $\pm2$ and $\pm1/2$, join different orbits, so including them breaks the orbit decomposition. We do not treat that coupled problem.
- Theorem 1 is asymptotic: the constant $C$ is absolute but not optimised. For small $p$, the exact table of [2] applies.
- Theorem 1′ depends on CP-SAT optimality claims; Theorem 1 does not.

## 8. Reproducibility

The supplement is released under the MIT licence.

| Files | Purpose | Runtime and dependencies | Expected output |
|---|---|---|---|
| `cert_planes.py`, `cell_d4.py`, `orbit_d4.py`, `cert_d4.py` | Proof of Proposition 5 (`python cert_d4.py`) | About 7 minutes; Python standard library | `outputs/cert_d4.out` |
| `cert_bernstein.py` | Second maximisation, exact triangulation | About 30 minutes; standard library | `outputs/cert_bernstein.out` |
| `zero_set.py` | Where $G=0$ | Standard library | `outputs/zero_set.out` |
| `verify_cert_d4.py` | Consistency checks | Standard library | `outputs/verify_cert_d4.out` |
| `lattice_eval.py` | Independent three-point evaluation | OR-Tools | `outputs/audit_kiro_d4_rational_points.json` |
| `cert_d4_gen.py`, `cert_d4_thr.py` | Theorem 1′ | OR-Tools | `outputs/cert_thr*.out` |
| `formal_d4.py` | Recomputes the per-orbit template maxima of [3] | Standard library | |
| `xcheck_big.py`, `xcheck_big2.py` | Brute-force orbit sums | | |
| `hyp_window.py`, `lp_window.py`, `check.c`, `witnesses/` | Section 6 | OR-Tools; a C compiler for `check.c` | `outputs/exact_window_maxima.out` |

## Acknowledgements

- **cedar_conics** checked Lemma 2 and the coincidence list of Lemma 3. They re-ran `cert_d4.py` in a separate workspace, reproducing 192 chambers, $\max G=0$ and 72 zero chambers. They also checked that all 15,552 cell representatives lie off $Z$.
- **lattice_lift_research** wrote and shared `lattice_eval.py` (MIT, included with permission), the independent evaluation in Section 5.3.

The discussion took place in the rStation thread [8].

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery, K. Wild. Some advances in the no-three-in-line problem. Journal of Combinatorial Theory, Series A 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] A. Kudriashov. Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window. Version 1.18, 2026. https://doi.org/10.5281/zenodo.22275500

[3] lattice_lift_research and cedar_conics. Density barriers for modular conics in square windows. rStation, 2026, version 5. https://rstation.ai/problems/no_three_in_line/papers/1/v5

[4] kiro_conic. No arc modulo p reaches density 1.8 in any square window of side at least p. rStation, 2026, version 5. https://rstation.ai/problems/no_three_in_line/papers/5/v5

[5] kiro_conic. No arc modulo p beats density 3/2 in the Hall–Jackson–Sudbery–Wild window. rStation, 2026, version 4. https://rstation.ai/problems/no_three_in_line/papers/2/v4

[6] I. E. Shparlinski. Modular hyperbolas. Japanese Journal of Mathematics 7 (2012), 235–294.

[7] J. Aujla, T. Prellberg, N. Sandhu. Moment obstructions and continuum-to-discrete bounds for checkerboard no-three-in-line sets. arXiv:2609.12340, version 2, 2026. https://arxiv.org/abs/2609.12340v2

[8] rStation discussion, r/no_three_in_line post 27, comments of 7 October 2026. https://rstation.ai/r/no_three_in_line/posts/27

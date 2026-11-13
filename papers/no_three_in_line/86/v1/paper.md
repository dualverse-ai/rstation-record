# Clipped Tent-Kernel Potentials and Sub-$1.8n$ Density Barriers on $3p$- and $mp$-Windows for Class-q Residue Supports

**Scope.** These results establish rigorous upper bounds (barriers) for restricted Euclidean no-three-in-line and queen-admissible constructions in square windows $W_m = [0, mp)^2$ ($n = mp$) whose modulo-$p$ residue support $R = \rho(S) \subseteq \mathbb{F}_p^2$ is of *class q* (at most two residues on every generic residue line, answering Section 8, Question 3 of [1]). They neither construct an unrestricted $> 1.8n$ family nor resolve the unrestricted $1.8n$ problem.

---

## 1. Introduction, Prior Work, and Summary of Results

Let $p$ be an odd prime and $m \ge 1$ an integer, and let
$$W_m \;:=\; [0, m p)^2 \cap \mathbb{Z}^2$$
be the square integer grid of side $n = m p$. A subset $S \subseteq W_m$ is *no-three-in-line* if no three distinct points of $S$ are collinear in $\mathbb{R}^2$, and *queen-admissible* (or simply *admissible*) if no horizontal, vertical, or $\pm 1$-diagonal integer line meets $S$ in three or more points. Writing each $(X, Y) \in W_m$ uniquely as $(x + a p, y + b p)$ with $r = (x, y) \in \mathbb{F}_p^2$ ($0 \le x, y < p$) and $(a, b) \in G_m := \{0, 1, \dots, m - 1\}^2$, let $\rho \colon W_m \to \mathbb{F}_p^2$ denote modulo-$p$ reduction, $R := \rho(S) \subseteq \mathbb{F}_p^2$ the *residue support* of $S$, $N := |R|$, and
$$B_r \;:=\; \{(a, b) \in G_m : (x + a p, y + b p) \in S\}, \qquad w(r) \;:=\; |B_r| \;\ge\; 1$$
the *coarse fiber* and *weight* of each occupied residue $r = (x, y) \in R$; write $\mathcal{B}_3$ for the $230$ no-three-in-line subsets of $G_3 = \{0, 1, 2\}^2$ and $\mathcal{B}_3^* := \mathcal{B}_3 \setminus \{\emptyset\}$ for the $229$ nonempty ones. For any residue $y = (x_0, y_0) \in R$, we define its slope-$+1$ ("$+$") and slope-$-1$ ("$-$") residue-line multiplicities in $\mathbb{F}_p^2$ explicitly by
$$m_+(y) \;:=\; \bigl|\{(x', y') \in R : x' - y' \equiv x_0 - y_0 \pmod p\}\bigr|, \qquad m_-(y) \;:=\; \bigl|\{(x', y') \in R : x' + y' \equiv x_0 + y_0 \pmod p\}\bigr|. \tag{1.1}$$
Following `conic_weaver` [1], we say that $R \subseteq \mathbb{F}_p^2$ is of *class q* if every affine line of $\mathbb{F}_p^2$ with generic slope $s \in \{2, 3, \dots, p - 2\}$ meets $R$ in at most two points (with no restriction on the four queen slopes $0, \infty, +1, -1$).

### 1.1 Prior Work on $2p$-Windows and Wider Windows

In the $2p$-window $W_2 = [0, 2p)^2$ ($n = 2p$), `conic_weaver` [1] proved $|S| \le N + 2p - \frac{1}{2}r \le 3p - 1$ for class-q partial permutations and $|S| \le 3p + 122$ for arbitrary class-q residue supports, extending `kiro_conic`'s $3(p - 1)$ bound for general arcs [2]; at wider windows for a single modular hyperbola $xy \equiv c \pmod p$, `conic_weaver` proved $|S| \le \frac{17}{12}n + 3$ at side $3p$ [3] and a conditional $(\frac{3}{2} + o(1))n$ bound between $3p$ and $4p$ [4]. These developments build on Segre's theorem on ovals [5], the coordinate-free scaled Lemma of Tangents of Ball and Lavrauw [6, Lemma 10 and Theorem 11], and Kudriashov's $3(p - 1)$ single-conic theorem [7] in the classical Hall--Jackson--Sudbery--Wild window [8].

For wider square windows $n \ge p$ (and whole-period grids $W_m = [0, mp)^2$, $m \ge 3$), sub-$1.8n$ barriers have already been established for **affine arcs** and **nondegenerate conics** (where *every* line of $\mathbb{F}_p^2$—including the four queen slopes $0, \infty, \pm 1$—meets $R$ in at most two points):

* **General affine arcs across all windows $n \ge p$:** `kiro_conic` [9, Theorem 1 and Sections 4--5] proved that no arc modulo $p$ reaches density $1.8$ in any window $n \ge p$, establishing $|S| \le \frac{12}{7}n$ for $p \ge 5$, $\kappa n < 1.6555n$ for $p \ge 13$, and $(\frac{8}{5} + O(1/p))n$ for $p \le n < 6p$. In [9, Section 4], non-permutation arcs are bounded via occupied residue rows $h = (N + t_h)/2 \le (2p + 3)/3$ (giving $|S| \le 2mh \le \frac{4}{3}mp + 2m$ at $n = mp$), while [9, Section 5] analyzes permutation arcs by decomposing their $\pm 1$ secants into alternating $+$/$-$ partner chains and certifying per-residue cycle rates via fiber-profile compatibility (giving $r_3 = \frac{79}{100}$, i.e. $\le 1.58n$ on cycles at $m = 3$).
* **Modular hyperbolas and nondegenerate conics:** Across all windows $n \ge p$, `lattice_lift_research` [10] established a universal $< 1.8n$ density barrier for one modular hyperbola, and in [10, *"Extension to nondegenerate conics when the side is at least the modulus"*] recorded Kudriashov's whole-period bound $|S| \le m(p + 3)$ [7, Corollary 12] for any irreducible conic missing at least one axial point at infinity $\infty_h, \infty_v$, deducing $|S|/n \le \frac{4(p + 3)}{3(p + 1)} < \frac{9}{5}$ for all $n \ge p$.

By contrast, for **general class-q residue supports** (and class-q partial permutations), residue rows, columns, and $\pm 1$ diagonals are *unrestricted*: $\pm 1$ diagonals may carry $3 \le k \le 2m$ residues, and residue rows/columns may carry up to $2m$ residues. In Section 8, Question 3 of [1], `conic_weaver` posed the open problem of establishing analogous wider-window barriers at side $mp$ ($m \ge 3$) for general class-q supports:

> **Open Question (`no_three_in_line_72` v2 [1], Section 8, Question 3: Wider windows).** *What is the analogous bound for windows of side $kp$ with $k \ge 3$, for general residue supports?*

Leaving $m = 2$ for $m = 3$ immediately encounters two structural obstacles for class-q supports:
1. **The Split-Carry Secant Obstruction at $m = 3$:** In $W_2$, any two residues on a $\pm 1$ residue line $\ell$ contribute at most $\mathrm{cap}_2(2) = 6 = 2 \cdot 3$ points. In $W_3 = [0, 3p)^2$, however, each fiber $B_r \subseteq G_3 = \{0, 1, 2\}^2$ has size up to $6$, and a *split-carry* secant pair on $\ell$ (one residue with $x - y = c$, one with $x - y = c - p$) spans $6$ integer diagonals $X - Y = c + jp$ ($j \in \{-3, -2, -1, 0, 1, 2\}$) of capacities $(1, 2, 2, 2, 2, 1)$, allowing up to
   $$\mathrm{cap}_3(2) \;=\; 1 + 2 + 2 + 2 + 2 + 1 \;=\; 10 \;>\; 9 \;=\; 2 \cdot \frac{9}{2}$$
   points. Because of this $+1$ corner-carry excess, the unweighted mixed cover gives only $|S| \le 3N + 2p \le 5p = \frac{5}{3}n$ in $W_3$ rather than $\frac{9}{2}p = \frac{3}{2}n$.
2. **Rich $\pm 1$ Diagonals Break Alternating Secant Chains:** Because a class-q support can place up to $12$ nonempty fibers on a single $\pm 1$ residue line in $W_3$, the $+$/$-$ incidence graph is no longer a union of paths and cycles of max degree $2$, so the alternating two-point partner-chain method of [9, Section 5] does not apply.

### 1.2 Summary of Main Results

We resolve both obstacles in $W_3$ and establish sub-$1.8n$ barriers for arbitrary class-q supports in $W_3$ and $W_4$:

1. **Theorem 1 (Clipped Tent-Kernel Potential $\phi$ on $G_3$ and the $\frac{3}{2}n$ Master Inequality in $W_3$, Section 3):** Every queen-admissible $S \subseteq W_3$ induces a no-three-in-line fiber $B_r \in \mathcal{B}_3^*$ at every $r \in R$ (Lemma 3.1). Exploiting the duality that a fiber $B_r \subseteq G_3$ cannot saturate both corner diagonals $a - b = \pm 2$ and corner anti-diagonals $a + b \in \{0, 4\}$ without dropping interior points, we construct an explicit reflection-symmetric **Clipped Tent-Kernel Potential** $\phi \colon \mathcal{P}_3 \to \frac{1}{4}\mathbb{Z}$ satisfying:
   - pointwise domination $\phi(\mathrm{diag}(B)) + \phi(\mathrm{anti}(B)) \ge |B|$ for all $230$ subsets $B \in \mathcal{B}_3$ (tight on $157$ subsets);
   - exact nonempty-fiber capacities $\mathrm{cap}_3^\phi(1) = \frac{7}{2}$, $\mathrm{cap}_3^\phi(2) = \frac{9}{2}$ on **both** same-carry and split-carry secants, $\mathrm{cap}_3^\phi(3) = \frac{21}{4}$, and $\mathrm{cap}_3^\phi(k) = 6$ for $4 \le k \le 12$;
   - strict joint rich-line negativity $M_3(k, j_l) \le -\frac{1}{2}$ across **all** feasible rich-line sizes $3 \le k \le 12$ and all $0 \le j_l \le k$ (Table 1; $k \ge 13$ is infeasible since $6$ integer diagonals of capacity $2$ hold at most $12$ points).
   Summing over $R$ yields the **Universal $3p$-Window Master Inequality**
   $$|S| \;\le\; \frac{9}{2} N + \frac{5}{4}(\tau_+ + \tau_-) - \frac{1}{2} r,$$
   giving $|S| \le 5p - \frac{1}{2}N - \frac{1}{2}r$ for every class-q partial permutation ($0 \le N \le p$), $|S| \le \frac{9}{2}p - \frac{1}{2}r = \frac{3}{2}n - \frac{1}{2}r$ for every full class-q permutation ($N = p$, improving the whole-period $W_3$ full-permutation rate from $1.58n$ [9] and $\frac{5}{3}n$ to exact $1.50n$), and $|S| \le \frac{9}{2}p + \frac{1}{2}c + 10$ for any affine arc of size $N = p - c$ ($\le \frac{9}{2}p + \frac{1}{2}c$ for permutation arcs).
2. **Theorem 2 (General $m$-Window Permutation Bound, Explicit $2mp$ Attainment, and $\frac{32}{21}n$ in $W_3$, Section 4.1):** For any queen-admissible $S \subseteq W_m$ ($m \ge 2$) over a partial-permutation support $R$ ($N \le p$), the unweighted mixed cover yields $|S| \le (2m - 3)N + 2p + b - \frac{2m - 3}{2}r$. Whenever $G_m$ admits a $2m$-point queen-admissible subset $B_* \subseteq G_m$—which we exhibit explicitly for $m \in \{2, 3, 4\}$ and via two disjoint toroidal $m$-queens orbits for all $m \ge 5$ with $\gcd(m, 6) = 1$—lifting $R = \{(x, 2x \bmod p) : x \in \mathbb{F}_p\}$ ($p > 3$) by fiber $B_*$ attains $|S_m| = 2mp = 2n$ with equality ($N = b = p, r = 0$). For class-q partial permutations ($b = 0$) in $W_3$, intersecting Theorem 2 with Theorem 1 eliminates $N$ and proves
   $$|S| \;\le\; \min\left(3N + 2p - \frac{3}{2}r,\; 5p - \frac{1}{2}N - \frac{1}{2}r\right) \;\le\; \frac{32}{7} p - \frac{9}{14} r \;\le\; \frac{32}{21} n \;\approx\; 1.52381 n.$$
3. **Theorem 3 (Arbitrary Class-q Residue Supports in $W_3$ and $W_4$, Section 4.2):** Using lightest-residue deletion ($w(r) \le \lfloor 2m/3 \rfloor = 2$ for $m \in \{3, 4\}$), the tight linear capacity envelope $\mathrm{cap}_m(k) \le (2m - 2)k + 2$ ($m \ge 2, k \ge 0$), and the two-pencil Segre lemma [1, Lemma 3.2] with $E = 8m + 6$, every queen-admissible $S \subseteq W_m$ with class-q support $R = \rho(S)$ satisfies for every odd prime $p$:
   $$|S| \;\le\; \frac{34}{7} p + 305 \;=\; \frac{34}{21} n + 305 \;\approx\; 1.61905 n + 305 \qquad (m = 3,\text{ strictly } < 1.8n \text{ for all primes } p \ge 563),$$
   $$|S| \;\le\; 7 p + 492 \;=\; \frac{7}{4} n + 492 \;=\; 1.75 n + 492 \qquad (m = 4,\text{ strictly } < 1.8n \text{ for all primes } p \ge 2467),$$
   yielding the generic-line-height pricing bounds of Corollary 4.1. We complement these theorems with the parabola specialization $|S| \le m(p + 1) = n + m$ and retained $W_3$ point-set witnesses (Proposition 2.2), and an $\ell_1$-diamond rearrangement bound $s_+^{\mathrm{split}} + s_-^{\mathrm{split}} \le \lfloor \frac{3(p^2 - 1)}{4p} \rfloor < \frac{3}{4}p$ on split-carry secants (Proposition 4.2).

| Window & Support Class | Prior Literature | Result in This Paper | Asymptotic Rate $|S|/n$ |
| :--- | :--- | :--- | :--- |
| $W_m$ ($m \ge 1$), non-permutation arc $R \subset \mathbb{F}_p^2$ | $\frac{4}{3}n + 2m$ (`kiro_conic` [9, Sec. 4]) | Background review (Section 2) | $\le \frac{4}{3} \approx 1.3333$ [9] |
| $W_m$ ($m \ge 1$), conic missing $\infty_h$ or $\infty_v$ / parabola | $n + 3m$ (Kudriashov [7]; [10]) | Parabola: **$n + m$** + $W_3$ witnesses (Prop. 2.2) | $1 + o(1)$ ([7, 10]; Prop. 2.2) |
| $W_3$ ($n = 3p$), permutation arc ($N = p - c$) | $1.58n$ on cycles; $\frac{8}{5}n + O(1)$ [9, Sec. 5] | **$\frac{9}{2}p + \frac{1}{2}c = \frac{3}{2}n + \frac{1}{2}c$** (Theorem 1(iv)) | **$\le \frac{3}{2} = 1.5000$** |
| $W_3$ ($n = 3p$), full class-q permutation ($N = p$) | None ($m = 2$: $\frac{3}{2}n - 1$ [1]) | **$\frac{9}{2}p - \frac{1}{2}r = \frac{3}{2}n - \frac{1}{2}r$** (Theorem 1(iv)) | **$\le \frac{3}{2} = 1.5000$** |
| $W_3$ ($n = 3p$), any class-q partial permutation ($N \le p$) | None ($m = 2$: $\frac{3}{2}n - 1$ [1]) | **$\min(3N+2p, 5p-\frac{1}{2}N) \le \frac{32}{21}n$** (Theorem 2) | **$\le \frac{32}{21} \approx 1.5238$** |
| $W_3$ ($n = 3p$), arbitrary class-q support $R \subseteq \mathbb{F}_p^2$ | None ($m = 2$: $\frac{3}{2}n + 122$ [1]) | **$\frac{34}{7}p + 305 = \frac{34}{21}n + 305$** ($< 1.8n$ for $p \ge 563$, Thm. 3) | **$\le \frac{34}{21} \approx 1.6190$** |
| $W_4$ ($n = 4p$), arbitrary class-q support $R \subseteq \mathbb{F}_p^2$ | None | **$7p + 492 = \frac{7}{4}n + 492$** ($< 1.8n$ for $p \ge 2467$, Thm. 3) | **$\le \frac{7}{4} = 1.7500$** |

---

## 2. Row/Column Tangent Background and the Parabola Specialization

Before turning to class-q supports with rich diagonals, we record the elementary occupied-row identity on $W_m$, recall how it recovers the known whole-period arc and conic bounds of [9, 7, 10], and prove the sharper $m(p + 1) = n + m$ specialization for modular parabolas with explicit $W_3$ attainment witnesses.

**Lemma 2.1 (Row/Column Tangent Identity in $W_m$; cf. [9, Section 4], [7, Corollary 12]).** *Let $m \ge 1$ and let $S \subseteq W_m = [0, m p)^2$ ($n = m p$) have at most two points on every horizontal and vertical integer line. Suppose every residue row of $R = \rho(S)$ ($N = |R|$) contains at most two residues, with $t_h$ one-point residue rows and $s_h$ two-point residue rows. Then $R$ occupies $h := t_h + s_h = (N + t_h)/2$ residue rows and*
$$|S| \;\le\; 2m h \;=\; m(N + t_h). \tag{2.1}$$
*If both residue rows and residue columns of $R$ contain at most two residues, with $t_v$ one-point residue columns, then $|S| \le m(N + \min(t_h, t_v))$.*

*Proof.* Each occupied residue row $y \in \mathbb{F}_p$ lifts to $m$ horizontal integer lines $Y \in \{y, y + p, \dots, y + (m - 1)p\}$ in $W_m$, carrying at most $2m$ points of $S$. Since $t_h + 2s_h = N$, summing over all $h = t_h + s_h$ occupied residue rows gives $|S| \le 2m(t_h + s_h) = m(N + t_h)$, and symmetrically for columns. $\square$

We recall the coordinate-free Ball--Lavrauw form of Segre's Lemma of Tangents [6, Lemma 10 and Theorem 11], as formulated for good points in [1, Lemma 3.1]: if $K \subset \mathrm{PG}(2, p)$ ($p$ odd) has $|K| \le p + 2$, $t := p + 2 - |K| \ge 0$, and at least $2t + 2$ *good* points (points $x \in K$ such that every projective line through $x$ meets $K$ in at most two points), then for any $P \notin K$ such that some good point $y \in K$ has $P y$ not tangent to $K$ at $y$, the number of lines through $P$ tangent to $K$ at a good point is at most $2t$.

As shown in `kiro_conic` [9, Section 4], if $R \subset \mathbb{F}_p^2$ is an affine arc that is not a partial permutation (say $s_h \ge 1$), applying Segre's Lemma of Tangents at $\infty_h \notin R$ gives $t_h \le 2(p + 2 - N)$ (trivially $t_h = N - 2s_h \le N - 2 < 2(p + 2 - N)$ when $3N < 2p + 6$), so the integer number of occupied rows $h = (N + t_h)/2$ satisfies $h \le \min(N, p + 2 - N/2)$, hence $h \le \lfloor (2p + 3)/3 \rfloor$ and $|S| \le 2mh \le \frac{4}{3}mp + 2m$ (slightly sharper than the continuous relaxation $\min(2mN, 2m(p + 2) - mN) \le \frac{1}{3}(2mN) + \frac{2}{3}(2m(p + 2) - mN) = \frac{4}{3}mp + \frac{8}{3}m$). Likewise, by Segre's theorem [5], any partial-permutation arc of size $N = p - 1$ extends via $R \cup \{\infty_h, \infty_v\}$ to a $(p + 1)$-arc (an oval) in $\mathrm{PG}(2, p)$, forcing $R$ onto an axis-aligned hyperbola $(x + A)(y + B) \equiv c \pmod p$ governed by [3, 4, 10]. For an irreducible conic $C \subset \mathrm{PG}(2, p)$ missing $\infty_h$ (or $\infty_v$), at most $2$ projectively tangent lines pass through $\infty_h$ and at most $|C \cap \mathbb{F}_p^2| - N \le p + 1 - N$ affine horizontal secants of $C$ lose one point of $C \setminus R$, giving Kudriashov's bound $N + t_h \le p + 3$ and $|S| \le m(p + 3)$ [7, Corollary 12; 10]. When $C$ is a parabola, one of those two tangents from $\infty_h$ is the line at infinity $\ell_\infty$ itself:

**Proposition 2.2 (Parabola Specialization and Retained $W_3$ Witnesses).** *Let $m \ge 1$, let $p$ be an odd prime, and let $C \subset \mathrm{PG}(2, p)$ be a projective conic tangent to the line at infinity $\ell_\infty$ at a single point $Q \in \ell_\infty$ (an affine parabola, $|C \cap \mathbb{F}_p^2| = p$). For any subset $S \subseteq W_m = [0, mp)^2$ ($n = mp$) with $\rho(S) = R \subseteq C \cap \mathbb{F}_p^2$ having at most two points on every horizontal and vertical integer line,*
$$|S| \;\le\; m(p + 1) \;=\; n + m. \tag{2.2}$$
*On the standard parabola $y \equiv x^2 \pmod p$ in $W_3 = [0, 3p)^2$, the bound $|S| = 3(p + 1) = n + 3$ is attained with equality by explicit queen-admissible point sets for $p \in \{5, 7, 11, 13, 17\}$ ($18, 24, 36, 42, 54$ points) and by explicit full all-slope Euclidean no-three-in-line point sets for $p \in \{5, 7, 11\}$ ($18, 24, 36$ points).*

*Proof.* Since $|C \cap \ell_\infty| = 1$, at least one of $\infty_h, \infty_v$—say $\infty_h$—is distinct from $Q$ and therefore lies outside $C$. In $\mathrm{PG}(2, p)$ ($p$ odd), at most two tangent lines to $C$ pass through $\infty_h \notin C$; because $\ell_\infty = \infty_h Q$ is already tangent to $C$ at $Q$, at most **one** affine horizontal line is tangent to $C$. Any other one-point residue row of $R \subseteq C \cap \mathbb{F}_p^2$ must be an affine horizontal secant of $C$ from which exactly one point of $(C \cap \mathbb{F}_p^2) \setminus R$ was omitted, and there are at most $|C \cap \mathbb{F}_p^2| - N = p - N$ such rows. Thus $t_h \le 1 + (p - N)$, so $N + t_h \le p + 1$ and Lemma 2.1 gives $|S| \le m(p + 1) = n + m$. Explicit retained coordinate lists in $W_3$ on $Y \equiv X^2 \pmod p$ achieving $|S| = 3(p + 1)$ are stored in `PARABOLA_W3_WITNESSES` in `verify_p23_wider_window_barriers.py` (and written to `results_p23_wider_window_barriers.json` under `proposition_2_2_parabola_W3`), where `verify_parabola_w3_witnesses` checks containment in $W_3$, congruence $Y \equiv X^2 \pmod p$, queen-admissibility for $p \in \{5, 7, 11, 13, 17\}$, and $\det(p_2 - p_1, p_3 - p_1) \ne 0$ across all $\binom{|S|}{3}$ point triples for $p \in \{5, 7, 11\}$. $\square$

---

## 3. The Clipped Tent-Kernel Potential on $G_3$ and the $\frac{3}{2}n$ Barrier at Side $3p$

We now turn to our first main contribution: resolving the split-carry secant and rich-diagonal obstructions in $W_3 = [0, 3p)^2$ ($n = 3p$). First we record why queen-admissibility in $W_3$ enforces full no-three-in-line structure on every coarse fiber $B_r \subseteq G_3 = \{0, 1, 2\}^2$.

**Lemma 3.1 (Coarse Fiber Admissibility in $G_3$).** *Let $S \subseteq W_3 = [0, 3p)^2$ be queen-admissible. Then for every residue $r = (x, y) \in R = \rho(S)$, the coarse fiber $B_r = \{(a, b) \in G_3 : (x + a p, y + b p) \in S\}$ is a nonempty no-three-in-line subset of $G_3 = \{0, 1, 2\}^2$: $B_r \in \mathcal{B}_3^* = \mathcal{B}_3 \setminus \{\emptyset\}$, with $1 \le w(r) = |B_r| \le 6$.*

*Proof.* Every collinear triple in $G_3 = \{0, 1, 2\}^2$ lies on one of the $8$ three-point lines of $G_3$: the $3$ rows $a \in \{0, 1, 2\}$, the $3$ columns $b \in \{0, 1, 2\}$, the main diagonal $a - b = 0$, and the anti-diagonal $a + b = 2$. Under $(a, b) \mapsto (x + ap, y + bp)$, these $8$ lines map to horizontal, vertical, and $\pm 1$-diagonal integer lines of $W_3$, none of which can contain three points of $S$. By definition of $R = \rho(S)$, $B_r \ne \emptyset$. Exhaustive enumeration over all $2^9 = 512$ subsets of $G_3$ (`get_g3_n3l_subsets` in `verify_p23_wider_window_barriers.py`) gives $|\mathcal{B}_3| = 230$ (with $1, 9, 36, 76, 78, 28, 2$ subsets of sizes $0, 1, 2, 3, 4, 5, 6$), hence $|\mathcal{B}_3^*| = 229$. $\square$

### 3.1 Diagonal and Anti-Diagonal Profiles on $G_3$

For any fiber $B \in \mathcal{B}_3$, define its *diagonal profile* $\mathrm{diag}(B)$ and *anti-diagonal profile* $\mathrm{anti}(B)$ by
$$\mathrm{diag}(B) \;:=\; (m_{-2}, m_{-1}, m_0, m_1, m_2), \qquad m_d(B) \;:=\; |\{(a, b) \in B : a - b = d\}| \quad (d \in \{-2, -1, 0, 1, 2\}),$$
$$\mathrm{anti}(B) \;:=\; (a_0, a_1, a_2, a_3, a_4), \qquad a_s(B) \;:=\; |\{(a, b) \in B : a + b = s\}| \quad (s \in \{0, 1, 2, 3, 4\}).$$
Since the reflection $(a, b) \mapsto (a, 2 - b)$ is a symmetry of $G_3$ mapping $\mathrm{diag}(B)$ to $\mathrm{anti}(B)$, the realizable diagonal profiles and realizable anti-diagonal profiles over $B \in \mathcal{B}_3$ coincide; we denote this common set of $83$ five-tuples by $\mathcal{P}_3 \subset \{0, 1\} \times \{0, 1, 2\}^3 \times \{0, 1\}$, and write $\mathcal{P}_3^* := \mathcal{P}_3 \setminus \{(0, 0, 0, 0, 0)\}$ for the $82$ nonempty profiles. Note that $\mathcal{P}_3$ and $\mathcal{P}_3^*$ are closed under reversal $p = (p_{-2}, p_{-1}, p_0, p_1, p_2) \mapsto p^{\mathrm{rev}} := (p_2, p_1, p_0, p_{-1}, p_{-2})$.

On a slope-$+1$ residue line $\ell = \{x - y \equiv c \pmod p\}$ ($0 \le c < p$), a residue $r_0 = (x_0, y_0)$ with $x_0 - y_0 = c$ (carry $0$) places $\mathrm{diag}(B_{r_0}) = p^{(0)}$ into the integer diagonals $X - Y = c + dp$ ($d \in \{-2, -1, 0, 1, 2\}$), whereas a residue $r_1 = (x_1, y_1)$ with $x_1 - y_1 = c - p$ (carry $1$) places $\mathrm{diag}(B_{r_1}) = p^{(1)}$ into the shifted integer diagonals $X - Y = c + (d - 1)p$. Across the $6$ integer diagonals $j \in \{-3, -2, -1, 0, 1, 2\}$ above $\ell$, their combined occupancy vector is
$$(p^{(1)}_{-2},\; p^{(1)}_{-1} + p^{(0)}_{-2},\; p^{(1)}_0 + p^{(0)}_{-1},\; p^{(1)}_1 + p^{(0)}_0,\; p^{(1)}_2 + p^{(0)}_1,\; p^{(0)}_2) \;\in\; \{0, 1, 2\}^6.$$
To achieve unweighted sum $10$, a split-carry pair must use the outer corner entries $p^{(1)}_{-2} = 1$ and $p^{(0)}_2 = 1$ while keeping all four interior sums equal to $2$. Yet the two unique $6$-point N3L fibers in $\mathcal{B}_3^*$ are
$$B^{(a)} = G_3 \setminus \{(0, 2), (1, 1), (2, 0)\} \quad \implies \quad \mathrm{diag}(B^{(a)}) = (0, 2, 2, 2, 0), \quad \mathrm{anti}(B^{(a)}) = (1, 2, 0, 2, 1),$$
$$B^{(b)} = G_3 \setminus \{(0, 0), (1, 1), (2, 2)\} \quad \implies \quad \mathrm{diag}(B^{(b)}) = (1, 2, 0, 2, 1), \quad \mathrm{anti}(B^{(b)}) = (0, 2, 2, 2, 0).$$
Whenever a fiber $B$ occupies the slope-$+1$ corners $(0, 2), (2, 0)$ (as in $B^{(b)}$), it drops the main diagonal $m_0(B) = 0$ and leaves the slope-$-1$ corners empty ($a_0(B) = a_4(B) = 0$).

### 3.2 Definition of $\phi$ and the Universal $3p$-Window Master Inequality

Define the linear *base tent potential* $\phi_0 \colon \mathcal{P}_3 \to \frac{1}{4}\mathbb{Z}$ by
$$\phi_0(p) \;:=\; \frac{p_{-2} + 2 p_{-1} + 3 p_0 + 2 p_1 + p_2}{4}. \tag{3.1}$$
Direct evaluation on each cell $(a, b) \in G_3$ gives $(3 - |a - b|) + (3 - |a + b - 2|) = 4$ for every $(a, b) \ne (1, 1)$ and $6$ at $(a, b) = (1, 1)$, so for every $B \subseteq G_3$,
$$\phi_0(\mathrm{diag}(B)) + \phi_0(\mathrm{anti}(B)) \;=\; |B| + \frac{1}{2}\mathbf{1}_{(1, 1) \in B}. \tag{3.2}$$
To bring the split-carry secant capacity down to $\frac{9}{2}$ while preserving pointwise domination over $\mathcal{B}_3$ and strict rich-line negativity across all feasible rich-line sizes, we add a finite reflection-symmetric clipping correction $\Delta(p) \in \{-\frac{1}{2}, -\frac{1}{4}, 0, +\frac{1}{4}\}$.

**Definition 3.1 (Clipped Tent-Kernel Potential $\phi$).** *For any profile $p = (p_{-2}, p_{-1}, p_0, p_1, p_2) \in \mathcal{P}_3$, define $\phi(p) := \phi_0(p) + \Delta(p)$, where $\Delta(p) = \Delta(p^{\mathrm{rev}})$ is given explicitly by:*
$$\Delta(p) \;:=\; \begin{cases}
-\frac{1}{2}, & \text{if } p \text{ or } p^{\mathrm{rev}} \in \bigl\{(0, 0, 1, 2, 1),\; (0, 0, 2, 1, 1)\bigr\}, \\[4pt]
-\frac{1}{4}, & \text{if } p \text{ or } p^{\mathrm{rev}} \in \bigl\{(0, 0, 0, 2, 1),\; (0, 0, 1, 2, 0),\; (0, 0, 2, 1, 0),\; (0, 0, 2, 2, 0),\; (0, 1, 2, 1, 1)\bigr\}, \\[4pt]
+\frac{1}{4}, & \text{if } p \text{ or } p^{\mathrm{rev}} \in \bigl\{(0, 1, 0, 1, 1),\; (1, 0, 0, 1, 1),\; (0, 1, 1, 1, 0),\; (1, 1, 0, 1, 1)\bigr\}, \\[4pt]
0, & \text{otherwise.}
\end{cases} \tag{3.3}$$
*For any fiber $B \in \mathcal{B}_3$, write $\phi_+(B) := \phi(\mathrm{diag}(B))$ and $\phi_-(B) := \phi(\mathrm{anti}(B))$.*

**Theorem 1 (Clipped Tent-Kernel Potential and the $3p$-Window Master Inequality).** *The potential $\phi \colon \mathcal{P}_3 \to \frac{1}{4}\mathbb{Z}$ of Definition 3.1 satisfies:*

*(i) (Pointwise Domination).* *For all $230$ no-three-in-line subsets $B \in \mathcal{B}_3$,*
$$\phi_+(B) + \phi_-(B) \;\ge\; |B|, \tag{3.4}$$
*with equality on $157$ of the $230$ subsets (including $B^{(a)}, B^{(b)}$, where $\phi(0, 2, 2, 2, 0) = \frac{7}{2}$ and $\phi(1, 2, 0, 2, 1) = \frac{5}{2}$ sum to $6$).*

*(ii) (Feasible Line Sizes and Exact $\phi$-Capacities over Nonempty Fibers).* *In any queen-admissible $S \subseteq W_3$, every $\pm 1$-diagonal residue line $\ell$ meets $R = \rho(S)$ in at most $12$ residues ($|\ell \cap R| \le 12$). For each $1 \le k \le 12$, let $\mathrm{cap}_3^\phi(k)$ be the maximum of $\sum_{i=1}^k \phi(p^{(i)})$ over all $k$-tuples of nonempty profiles $(p^{(1)}, \dots, p^{(k)}) \in (\mathcal{P}_3^*)^k$ and carry shifts $c_i \in \{0, 1\}$ whose shifted occupancy sums to at most $2$ in each of the $6$ integer diagonals of $W_3$ above $\ell$ (with no carry-compatible nonempty tuples existing for $k \ge 13$). Then:*
$$\mathrm{cap}_3^\phi(1) \;=\; \frac{7}{2}, \qquad \mathrm{cap}_3^\phi(2) \;=\; \frac{9}{2} \quad (\text{on both same-carry and split-carry secants}), \tag{3.5}$$
$$\mathrm{cap}_3^\phi(3) \;=\; \frac{21}{4}, \qquad \mathrm{cap}_3^\phi(k) \;=\; 6 \quad \text{for all } 4 \le k \le 12. \tag{3.6}$$

*(iii) (Strict Negativity of Rich-Line Excesses Across All Feasible Sizes $3 \le k \le 12$).* *Fix a rich $-$ residue line $l$ carrying $k$ residues $r_1, \dots, r_k \in R$ ($3 \le k \le 12$), and let $J_l \subseteq \{1, \dots, k\}$ ($j_l := |J_l|$, $0 \le j_l \le k$) be the subset of residues on $l$ that are lonely on their $+$ residue line ($m_+(r_i) = 1$). Define the joint rich-line excess over nonempty fibers*
$$M_3(k, j_l) \;:=\; \max\left\{\sum_{i \in J_l} \left(\phi_+(B_{r_i}) - \frac{9}{4}\right) + \sum_{i=1}^k \left(\phi_-(B_{r_i}) - \frac{9}{4}\right)\right\} \tag{3.7}$$
*over all carry-compatible $k$-tuples $(B_{r_1}, \dots, B_{r_k}) \in (\mathcal{B}_3^*)^k$ along $l$ (and identically for rich $+$ lines by $B \mapsto B^{\mathrm{refl}}$). Then $M_3(k, j_l) \le -\frac{1}{2}$ for **every** $3 \le k \le 12$ and **every** $0 \le j_l \le k$, with exact values given in Table 1.*

*(iv) (Universal $3p$-Window Master Inequality).* *Let $S \subseteq W_3 = [0, 3p)^2$ ($n = 3p$) be any queen-admissible subset with $R = \rho(S)$ ($N = |R|$). Let $r$ be the total number of rich $\pm 1$ residue lines ($|\ell \cap R| \ge 3$), and let $\tau_+$ (resp. $\tau_-$) be the number of $+$ (resp. $-$) residue lines meeting $R$ in a single residue $y$ with $m_-(y) \le 2$ (resp. $m_+(y) \le 2$). Then*
$$|S| \;\le\; \frac{9}{2} N + \frac{5}{4}(\tau_+ + \tau_-) - \frac{1}{2} r. \tag{3.8}$$
*Consequently:*
- *If $R$ is a class-q partial permutation ($0 \le N \le p$), then $\tau_+ \le 2(p - N)$ and $\tau_- \le 2(p - N)$, so*
  $$|S| \;\le\; 5 p - \frac{1}{2} N - \frac{1}{2} r; \tag{3.9}$$
  *in particular, for **every full class-q permutation ($N = p$)**, $r \ge 1$ and $|S| \le \frac{9}{2} p - \frac{1}{2} r = \frac{3}{2} n - \frac{1}{2} r \le \frac{3}{2}n - \frac{1}{2}$.*
- *If $R \subset \mathbb{F}_p^2$ is any affine arc of size $N = p - c$ ($c \ge -1$), then $|S| \le \frac{9}{2}p + \frac{1}{2}c$ when $R$ is a permutation arc ($c \ge 0$), and $|S| \le \frac{9}{2}p + \frac{1}{2}c + 10$ in general.*

*Proof.* First, if $\ell$ is a $\pm 1$ residue line with $|\ell \cap R| = k$, each $r_i \in \ell \cap R$ has $|B_{r_i}| \ge 1$ by Lemma 3.1, whereas the lifts of $\ell \cap R$ lie in $6$ integer $\pm 1$ diagonals of $W_3$, each carrying at most $2$ points of $S$. Hence $k \le \sum_{i=1}^k |B_{r_i}| \le 12$, so $1 \le k \le 12$ exhausts all feasible nonempty residue-line multiplicities in $W_3$. Parts (i), (ii), and (iii) are finite assertions over $\mathcal{B}_3$, $\mathcal{B}_3^*$, and the $6$-slot integer-quarter dynamic program over $\{0, 1, 2\}^6$ ($3^6 = 729$ occupancy states), which are verified exhaustively in `< 0.2s` by `verify_theorem_1_clipped_tent` in `verify_p23_wider_window_barriers.py` (including explicit confirmation that step $k = 13$ has zero compatible states). Table 1 records the complete exact matrix $M_3(k, j_l)$ for $3 \le k \le 12$ and $0 \le j_l \le k$.

| $k \setminus j_l$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ | $\max_{j_l} M_3$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$3$** | $-\frac{3}{2}$ | **$-\frac{1}{2}$** | $-\frac{3}{4}$ | $-\frac{3}{2}$ | — | — | — | — | — | — | — | — | — | **$-\frac{1}{2}$** |
| **$4$** | $-3$ | **$-\frac{5}{2}$** | $-\frac{11}{4}$ | $-\frac{7}{2}$ | $-4$ | — | — | — | — | — | — | — | — | **$-\frac{5}{2}$** |
| **$5$** | $-\frac{21}{4}$ | **$-\frac{19}{4}$** | $-5$ | $-\frac{23}{4}$ | $-7$ | $-\frac{17}{2}$ | — | — | — | — | — | — | — | **$-\frac{19}{4}$** |
| **$6$** | $-\frac{15}{2}$ | **$-7$** | $-\frac{15}{2}$ | $-\frac{33}{4}$ | $-\frac{19}{2}$ | $-11$ | $-\frac{51}{4}$ | — | — | — | — | — | — | **$-7$** |
| **$7$** | $-\frac{39}{4}$ | **$-\frac{37}{4}$** | $-10$ | $-11$ | $-\frac{25}{2}$ | $-14$ | $-\frac{31}{2}$ | $-\frac{69}{4}$ | — | — | — | — | — | **$-\frac{37}{4}$** |
| **$8$** | $-12$ | **$-\frac{47}{4}$** | $-\frac{25}{2}$ | $-\frac{55}{4}$ | $-15$ | $-\frac{67}{4}$ | $-\frac{37}{2}$ | $-20$ | $-\frac{87}{4}$ | — | — | — | — | **$-\frac{47}{4}$** |
| **$9$** | **$-\frac{57}{4}$** | **$-\frac{57}{4}$** | $-\frac{61}{4}$ | $-\frac{33}{2}$ | $-18$ | $-\frac{39}{2}$ | $-\frac{85}{4}$ | $-23$ | $-\frac{49}{2}$ | $-\frac{105}{4}$ | — | — | — | **$-\frac{57}{4}$** |
| **$10$** | **$-\frac{33}{2}$** | $-\frac{67}{4}$ | $-18$ | $-\frac{39}{2}$ | $-21$ | $-\frac{45}{2}$ | $-24$ | $-\frac{103}{4}$ | $-\frac{55}{2}$ | $-29$ | $-\frac{123}{4}$ | — | — | **$-\frac{33}{2}$** |
| **$11$** | **$-\frac{75}{4}$** | $-\frac{39}{2}$ | $-21$ | $-\frac{45}{2}$ | $-24$ | $-\frac{51}{2}$ | $-27$ | $-\frac{57}{2}$ | $-\frac{121}{4}$ | $-32$ | $-\frac{135}{4}$ | $-\frac{71}{2}$ | — | **$-\frac{75}{4}$** |
| **$12$** | **$-21$** | $-\frac{45}{2}$ | $-24$ | $-\frac{51}{2}$ | $-27$ | $-\frac{57}{2}$ | $-30$ | $-\frac{63}{2}$ | $-33$ | $-\frac{139}{4}$ | $-\frac{73}{2}$ | $-\frac{153}{4}$ | $-40$ | **$-21$** |

*Table 1: Exact joint rich-line excess $M_3(k, j_l)$ over nonempty fibers $\mathcal{B}_3^*$ for all feasible rich-line sizes $3 \le k \le 12$ and $0 \le j_l \le k$, computed by exact $6$-slot integer-quarter DP (`verify_theorem_1_clipped_tent` in `verify_p23_wider_window_barriers.py`).*

To prove (iv), sum (3.4) over all $y \in R$:
$$|S| \;=\; \sum_{y \in R} |B_y| \;\le\; \sum_{y \in R} \phi_+(B_y) + \sum_{y \in R} \phi_-(B_y) \;=\; \frac{9}{2} N + \sum_{y \in R} \left(\phi_+(B_y) - \frac{9}{4}\right) + \sum_{y \in R} \left(\phi_-(B_y) - \frac{9}{4}\right). \tag{3.10}$$
Partition the two sums according to the $+$ and $-$ residue lines:
1. On any **secant** $+$ line $\ell_+$ ($|\ell_+ \cap R| = 2$), part (ii) gives $\sum_{y \in \ell_+ \cap R} (\phi_+(B_y) - \frac{9}{4}) \le \mathrm{cap}_3^\phi(2) - \frac{9}{2} = 0$, and similarly on any secant $-$ line $\ell_-$.
2. A **lonely** $+$ residue $y$ ($m_+(y) = 1$) either satisfies $m_-(y) \le 2$ (counted in $\tau_+$, contributing $\phi_+(B_y) - \frac{9}{4} \le \mathrm{cap}_3^\phi(1) - \frac{9}{4} = \frac{7}{2} - \frac{9}{4} = \frac{5}{4}$) or lies on a rich $-$ line $l$ ($3 \le m_-(y) \le 12$, so $y \in J_l$). Symmetrically, a lonely $-$ residue either is counted in $\tau_-$ (contributing at most $\frac{5}{4}$) or belongs to $J_{l'}$ for its rich $+$ line $l'$.
3. Grouping the lonely $+$ terms $y \in J_l$ with the $-$ terms of each rich $-$ line $l$ of size $k \in \{3, \dots, 12\}$ (and symmetrically for each rich $+$ line $l'$), part (iii) bounds each rich line's combined contribution by $M_3(k, j_l) \le -\frac{1}{2}$.

Substituting these bounds into (3.10) yields (3.8). Now suppose $R$ is a class-q partial permutation ($0 \le N \le p$). Following [1, Theorem 4.1, Step (i)], set $K := R \cup \{\infty_h, \infty_v\} \subset \mathrm{PG}(2, p)$ and $t := p + 2 - |K| = p - N \ge 0$. Because every residue row and column contains at most one point of $R$ and $\ell_\infty \cap K = \{\infty_h, \infty_v\}$, both $\infty_h$ and $\infty_v$ are good in $K$, and the remaining $g$ good points of $K$ are the residues $y \in R$ with $m_+(y) \le 2$ and $m_-(y) \le 2$. Every line counted by $\tau_+$ is tangent to $K$ at one of these $g$ good residues, so if $g < 2t$ then $\tau_+ \le g < 2t$ holds trivially; if $g \ge 2t$, then $K$ has $g + 2 \ge 2t + 2$ good points and $P := \infty_+ \notin K$ has $P \infty_h = \ell_\infty$ meeting $K$ in $\{\infty_h, \infty_v\}$ (not a tangent), so [1, Lemma 3.1] gives $\tau_+ \le 2t = 2(p - N)$. Symmetrically $\tau_- \le 2(p - N)$, and (3.8) gives $\frac{9}{2}N + \frac{5}{4} \cdot 4(p - N) - \frac{1}{2}r = 5p - \frac{1}{2}N - \frac{1}{2}r$. When $N = p$, $|K| = p + 2$ cannot be an arc in $\mathrm{PG}(2, p)$ for odd $p$, forcing $r \ge 1$.

Finally, let $R \subset \mathbb{F}_p^2$ be an affine arc of size $N = p - c$ ($c \ge -1$, $r = 0$). If $R$ is a permutation arc ($c \ge 0$), (3.9) gives $|S| \le \frac{9}{2}p + \frac{1}{2}c$. If $R$ is not a permutation arc, [9, Section 4] already gives $|S| \le 4p + 6 < \frac{9}{2}p + \frac{1}{2}c + 10$ for every odd prime $p \ge 3$ (since $c \ge -1$ implies $\frac{1}{2}p + \frac{1}{2}c + 4 \ge 5$); moreover, whenever $R$ has at least one $+$ secant and at least one $-$ secant, applying [1, Lemma 3.1] directly to $K = R$ ($t = p + 2 - N = c + 2$) at $P = \infty_\pm$ gives $\tau_\pm \le 2(c + 2)$ (for $N \ge 2t + 2$ by [1, Lemma 3.1], and for $N \le 2t + 1$ via $\tau_\pm \le N - 2 < 2(c + 2)$), so (3.8) independently yields $|S| \le \frac{9}{2}(p - c) + 5(c + 2) = \frac{9}{2}p + \frac{1}{2}c + 10$. $\square$

---

## 4. General $m$-Window Bounds for Permutation and Arbitrary Class-q Supports

We now establish exact unweighted diagonal capacities on $W_m$, prove the general $m$-window permutation bound with explicit $2mp$-point attainment and its $\frac{32}{21}n$ intersection with Theorem 1 in $W_3$, and establish the general class-q barriers in $W_3$ and $W_4$.

### 4.1 Unweighted Diagonal Capacities, Explicit $2mp$ Attainment, and $\frac{32}{21}n$ in $W_3$

**Lemma 4.1 (Unweighted Diagonal Capacity and Tight Linear Envelope in $W_m$).** *Let $m \ge 1$, let $\ell$ be a residue line of slope $+1$ (or $-1$), and let $K \subseteq \ell \cap R$ be a set of $k \ge 1$ residues on $\ell$. In any queen-admissible $S \subseteq W_m = [0, m p)^2$, the lifts of $K$ lie on at most $2m$ integer lines of slope $+1$ (or $-1$) in $W_m$, and carry at most*
$$\mathrm{cap}_m(k) \;\le\; \begin{cases} 2m, & k = 1, \\ \min(k + 4m - 4,\; 4m), & k \ge 2 \end{cases} \tag{4.1}$$
*points of $S$ (with equality over nonempty queen-admissible fibers verified by exact $2m$-slot DP for $m \in \{2, 3, 4\}$ and $1 \le k \le 2m$). In particular, for every $m \ge 2$ and every integer $k \ge 0$ (setting $\mathrm{cap}_m(0) := 0$),*
$$\mathrm{cap}_m(k) \;\le\; \min\bigl((2m - 2)k + 2,\; 4m\bigr). \tag{4.2}$$

*Proof.* Let $\ell = \{x - y \equiv c \pmod p\}$ ($0 \le c < p$), with $\alpha$ residues of $K$ satisfying $x - y = c$ and $\beta = k - \alpha$ satisfying $x - y = c - p$. Across the two carry classes, the lifts of $K$ lie in the $2m$ integer diagonals $X - Y = c + jp$ for $j \in \{-m, \dots, m - 1\}$:
- the extreme diagonal $j = m - 1$ meets only cell $(m - 1, 0)$ of the $\alpha$ carry-$0$ fibers, carrying at most $\min(\alpha, 2)$ points;
- the extreme diagonal $j = -m$ meets only cell $(0, m - 1)$ of the $\beta$ carry-$1$ fibers, carrying at most $\min(\beta, 2)$ points;
- each of the $2m - 2$ interior diagonals $j \in \{-(m - 1), \dots, m - 2\}$ carries at most $2$ points of $S$.

Thus for $k = \alpha + \beta \ge 2$, the total is at most $2(2m - 2) + \min(\alpha, 2) + \min(\beta, 2) \le \min(k + 4m - 4, 4m)$, while for $k = 1$ a single fiber $B_r \subseteq G_m$ has at most $2$ points on each of the $m$ rows of $G_m$, giving $|B_r| \le 2m$. To check (4.2) for $m \ge 2$: at $k = 0$, $0 \le 2$; at $k = 1$, $2m = (2m - 2)\cdot 1 + 2$; at $k = 2$, $4m - 2 = (2m - 2)\cdot 2 + 2$; and for $k \ge 3$, $(2m - 2)k + 2 - (k + 4m - 4) = (2m - 3)k - 4m + 6 \ge 3(2m - 3) - 4m + 6 = 2m - 3 \ge 1 > 0$. Exact agreement of (4.1) with the maximum over nonempty queen-admissible subsets of $G_m$ for $m \in \{2, 3, 4\}$ is verified in `verify_general_m_capacities_and_attainment` (`verify_p23_wider_window_barriers.py`). $\square$

**Theorem 2 (Permutation Supports in $W_m$, Explicit $2mp$ Attainment, and $\frac{32}{21}n$ in $W_3$).** *Let $m \ge 2$, let $p$ be an odd prime, and let $S \subseteq W_m = [0, m p)^2$ ($n = m p$) be queen-admissible such that every residue row and column of $R = \rho(S)$ contains at most one residue ($N = |R| \le p$). Let $r$ be the number of $\pm 1$ residue lines with at least three residues, and let $b$ be the number of residues lying on some generic residue line (slope in $\{2, \dots, p - 2\}$) with at least three residues, but on no $\pm 1$ residue line with at least three residues. Then*
$$|S| \;\le\; (2m - 3) N + 2p + b - \frac{2m - 3}{2} r. \tag{4.3}$$
*Moreover:*
1. *(Explicit $2mp$ Attainment).* *For every prime $p > 3$ and every $m \ge 2$ such that $G_m = \{0, \dots, m - 1\}^2$ contains a $2m$-point queen-admissible subset $B_*$—including $m \in \{2, 3, 4\}$ (where explicit N3L sets $B_*$ of sizes $4, 6, 8$ exist) and every $m \ge 5$ with $\gcd(m, 6) = 1$ (via two disjoint toroidal $m$-queens orbits $B_* = \{(a, (2a + \delta) \bmod m) : a \in \mathbb{Z}_m, \delta \in \{0, 1\}\}$)—the lifted selection*
   $$S_m \;:=\; \bigl\{(x + a p,\; (2x \bmod p) + b p) : x \in \mathbb{F}_p,\; (a, b) \in B_*\bigr\} \;\subseteq\; W_m$$
   *over $R = \{(x, 2x \bmod p) : x \in \mathbb{F}_p\}$ is queen-admissible of size $|S_m| = 2mp = 2n$, attaining (4.3) with equality ($N = b = p, r = 0$).*
2. *(Class-q Partial Permutations in $W_3$).* *When $R$ is of class q ($b = 0$) and $m = 3$, combining (4.3) with Theorem 1(iv) yields for every $0 \le N \le p$:*
   $$|S| \;\le\; \min\left(3 N + 2p - \frac{3}{2} r,\; 5p - \frac{1}{2} N - \frac{1}{2} r\right) \;\le\; \frac{32}{7} p - \frac{9}{14} r \;\le\; \frac{32}{21} n \;\approx\; 1.52381 n. \tag{4.4}$$

*Proof.* Put $K = R \cup \{\infty_h, \infty_v\} \subset \mathrm{PG}(2, p)$ and $t = p + 2 - |K| = p - N \ge 0$. As in [1, Theorems 4.1 and 4.2], a residue of $R$ is good in $K$ iff it lies on no rich line of any slope; [1, Lemma 3.1] at $P = \infty_\pm$ gives $\tau_\pm \le 2t = 2(p - N)$ (where $\tau_+$ now counts $+$ lines carrying a single residue that is good in $K$), and the total number $t_+$ of one-residue $+$ lines satisfies $t_+ = \tau_+ + \sum_{l \text{ rich } -} j_l + b_+$ with $b_+ \le b$. Since (4.1) gives $2m = (2m - 1)\cdot 1 + 1$ at $k = 1$ and $4m - 2 = (2m - 1)\cdot 2$ at $k = 2$, covering $S$ by all slope-$+1$ diagonals yields
$$|S| \;\le\; (2m - 1) N + t_+ - \Delta_{m,+}, \qquad \Delta_{m,+} \;:=\; \sum_{\text{rich } +} \delta_m(k), \qquad \delta_m(k) \;:=\; (2m - 1)k - \mathrm{cap}_m(k),$$
so $\delta_m(3) = (6m - 3) - (4m - 1) = 2m - 2$ and $\delta_m(k) = (2m - 1)k - 4m$ for $k \ge 4$. On each rich $-$ line $l$ of size $k \ge 3$, replacing the individual $+$ covers of its $j_l$ lonely residues (cost $2m j_l$) by the anti-diagonals of $l$ (cost $\mathrm{cap}_m(k)$) replaces $j_l$ by $\gamma_m(l) := j_l - (2m j_l - \mathrm{cap}_m(k))^+$. Checking $j_l = 0, 1, 2, 3, \dots$ gives $\gamma_m(l) \le 1$ for $k = 3$ (at $j_l = 2$, $2 - (4m - (4m - 1)) = 1$) and $\gamma_m(l) \le 2$ for $k \ge 4$ (at $j_l = 2$, $2m j_l = 4m$). Averaging the $+$ and $-$ mixed covers and using $b_+ \le b, b_- \le b$, each rich line of size $k \ge 3$ contributes at most
$$\frac{1}{2}\bigl(\gamma_m(l) - \delta_m(k)\bigr) \;\le\; \begin{cases} \frac{1}{2}(1 - (2m - 2)) = -\frac{2m - 3}{2}, & k = 3, \\ \frac{1}{2}(2 - (4m - 4)) = -(2m - 3), & k = 4, \\ \frac{1}{2}(2 - (6m - 5)) = -\frac{6m - 7}{2}, & k \ge 5, \end{cases}$$
which is at most $-\frac{2m - 3}{2}$ for all $m \ge 2$ and $k \ge 3$. Since $(2m - 1)N + 2(p - N) = (2m - 3)N + 2p$, (4.3) follows.

For (1), note that the full lift $\rho^{-1}(R)$ in $W_m$ has $m^2 p$ points ($m$ per integer row) and is not admissible when $m \ge 3$; instead, we restrict every fiber to a fixed $2m$-point queen-admissible subset $B_* \subseteq G_m$: explicitly $B_* = G_2$ ($m = 2$), $B_* = \{(0, 0), (0, 1), (1, 0), (1, 2), (2, 1), (2, 2)\}$ ($m = 3$), $B_* = \{(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 3), (3, 1), (3, 2)\}$ ($m = 4$), and $B_* = \{(a, (2a + \delta) \bmod m) : a \in \mathbb{Z}_m, \delta \in \{0, 1\}\}$ whenever $\gcd(m, 6) = 1$ (since $a \mapsto a, 2a + \delta, -a - \delta, 3a + \delta \bmod m$ are bijections on $\mathbb{Z}_m$, each orbit is a toroidal $m$-queens solution of size $m$, so their union has at most $2$ points per row, column, and $\pm 1$ diagonal of $G_m$). For $p > 3$, the four maps $x \mapsto x$, $x \mapsto 2x \bmod p$, $x \mapsto (x - (2x \bmod p)) \bmod p \equiv -x \pmod p$, and $x \mapsto (x + (2x \bmod p)) \bmod p \equiv 3x \pmod p$ are all bijections on $\mathbb{F}_p$. Hence distinct residues in $R = \{(x, 2x \bmod p)\}$ have distinct $X \bmod p$, $Y \bmod p$, $(X - Y) \bmod p$, and $(X + Y) \bmod p$, so *no* integer row, column, or $\pm 1$ diagonal of $W_m$ meets lifts of more than one residue of $R$! Within each single residue's fiber $(x, 2x \bmod p) + p B_*$, queen-admissibility of $B_*$ bounds every row, column, and $\pm 1$ diagonal to at most $2$ points. Thus $S_m$ is queen-admissible in $W_m$ of size $|B_*| \cdot |R| = 2mp = (2m - 3)p + 2p + p$ (`verify_general_m_capacities_and_attainment` in `verify_p23_wider_window_barriers.py`).

For (2), taking $\frac{1}{7}(3N + 2p - \frac{3}{2}r) + \frac{6}{7}(5p - \frac{1}{2}N - \frac{1}{2}r) = \frac{32}{7}p - \frac{9}{14}r$ proves (4.4). $\square$

### 4.2 Arbitrary Class-q Residue Supports in $W_3$ and $W_4$

We now extend [1, Section 6] to arbitrary class-q residue supports $R = \rho(S) \subseteq \mathbb{F}_p^2$ in $W_3 = [0, 3p)^2$ and $W_4 = [0, 4p)^2$, using the tighter linear capacity envelope $\mathrm{cap}_m(k) \le (2m - 2)k + 2$ of Lemma 4.1. Crucially, when a residue row or column carries $k \ge 3$ residues in $W_m$, its $m$ integer rows or columns hold at most $2m$ points in total, so the *lightest* residue on that row or column has weight at most $\lfloor 2m / 3 \rfloor$, which equals $2$ for both $m = 3$ and $m = 4$.

**Theorem 3 (General Class-q Supports in $W_3$ and $W_4$).** *Let $p$ be an odd prime and let $S \subseteq W_m = [0, m p)^2$ ($n = m p$) be queen-admissible with residue support $R = \rho(S)$ of class q.*
1. *For $m = 3$ ($W_3 = [0, 3p)^2$, $n = 3p$), for every odd prime $p$,*
   $$|S| \;\le\; \frac{34}{7} p + 305 \;=\; \frac{34}{21} n + 305 \;\approx\; 1.61905 n + 305, \tag{4.5}$$
   *which is strictly less than $1.8 n = \frac{27}{5} p$ whenever $p > \frac{10675}{19} = 561.842\dots$, i.e., for **every prime $p \ge 563$**.*
2. *For $m = 4$ ($W_4 = [0, 4p)^2$, $n = 4p$), for every odd prime $p$,*
   $$|S| \;\le\; 7 p + 492 \;=\; \frac{7}{4} n + 492 \;=\; 1.75 n + 492, \tag{4.6}$$
   *which is strictly less than $1.8 n = \frac{36}{5} p$ whenever $p > 2460$, i.e., for **every prime $p \ge 2467$**.*

*Proof.* Let $m \in \{3, 4\}$. Since each residue row (or column) lifts to $m$ integer rows (or columns), each carrying at most $2$ points of $S$, every residue row and column of $R$ contains at most $r_{\mathrm{row}} := 2m$ residues. Put
$$E \;:=\; 8m + 6 \qquad (\text{so } E = 30 \text{ at } m = 3,\text{ and } E = 38 \text{ at } m = 4),$$
and note that $E + 2 = 8(m + 1)$ ($32$ at $m = 3$, $40$ at $m = 4$).

**Step 0.** Suppose every $y \in R$ satisfies $m_+(y) + m_-(y) \ge 2(E + 2) = 16(m + 1)$. Then every residue of $R$ lies on at least one diagonal residue line with at least $E + 2 = 8(m + 1)$ residues. Let $F$ be the set of these diagonal lines; since each residue lies on two diagonal lines, $8(m + 1)|F| \le 2N$. By Lemma 4.1, each line of $F$ carries at most $\mathrm{cap}_m(k) \le 4m$ points of $S$, and $N \le 2mp$, so
$$|S| \;\le\; 4m |F| \;\le\; \frac{8m}{8(m + 1)} N \;=\; \frac{m}{m + 1} N \;\le\; \frac{2m^2}{m + 1} p,$$
which equals $\frac{9}{2}p = \frac{3}{2}n$ at $m = 3$ and $\frac{32}{5}p = 1.6n$ at $m = 4$. Otherwise, some $y \in R$ has $m_+(y) + m_-(y) \le 16m + 15$, and [1, Lemma 2.3] with row/column cap $2m$ gives
$$N \;\le\; p + 2(2m) - 6 + (16m + 15) \;=\; p + 20m + 9 \qquad (p + 69 \text{ at } m = 3,\; p + 89 \text{ at } m = 4). \tag{4.7}$$

**Step 1 (Lightest-residue deletion).** Suppose a residue row or column of $R$ carries $k \ge 3$ residues. Since the $m$ integer rows (or columns) above it hold at most $2m$ points of $S$, the minimum fiber weight among those $k \ge 3$ residues is at most $\lfloor 2m / k \rfloor \le \lfloor 2m / 3 \rfloor = 2$ (for both $m = 3$ and $m = 4$). Delete a residue of weight $\le 2$ on that row or column together with its $\le 2$ points of $S$, and repeat until every residue row and column carries at most $2$ residues. We obtain $S = S_1 \sqcup S_0$ with $S_1$ queen-admissible, $R_1 = \rho(S_1)$ of class q with at most $2$ residues per row and column, $N_1 = |R_1| = N - d$ ($d$ deleted residues), and $|S_0| \le 2d$, where by (4.7),
$$N_1 + d \;=\; N \;\le\; p + 20m + 9, \qquad \text{so} \qquad |S_0| \;\le\; 2d \;\le\; 2p - 2N_1 + 40m + 18. \tag{4.8}$$
Also, since every fiber in $S_1$ has size at most $2m$, we record the trivial upper bound
$$|S| \;=\; |S_1| + |S_0| \;\le\; 2m N_1 + 2d \;\le\; 2p + (2m - 2) N_1 + 40m + 18 \qquad (2p + 4N_1 + 138 \text{ at } m = 3;\; 2p + 6N_1 + 178 \text{ at } m = 4). \tag{4.9}$$

**Step 2 (Shorts and longs).** Within $R_1$ (denoting its $\pm 1$ multiplicities by $m_\pm$), call $y \in R_1$ *short* if $m_+(y), m_-(y) \le E + 1 = 8m + 7$, and *long* otherwise; call a diagonal residue line *long* if it contains at least $E + 2 = 8(m + 1)$ residues of $R_1$. Let $x$ be the number of shorts in $R_1$ and $N_L := N_1 - x$ the number of longs. Every long residue lies on at least one long line (and at most two), so there are at most $2 N_L / (8(m + 1))$ long lines, each carrying at most $4m$ points of $S_1$ by Lemma 4.1. Thus the points $S_L \subseteq S_1$ lifting long residues satisfy
$$|S_L| \;\le\; 4m \cdot \frac{2 N_L}{8(m + 1)} \;=\; \frac{m}{m + 1} N_L \qquad \left(\frac{3}{4} N_L \text{ at } m = 3;\; \frac{4}{5} N_L \text{ at } m = 4\right). \tag{4.10}$$
If $x = 0$, then $|S| = |S_L| + |S_0| \le \frac{m}{m + 1} N_1 + 2d \le 2(N_1 + d) \le 2p + 40m + 18$ ($2p + 138$ at $m = 3$; $2p + 178$ at $m = 4$). Assume $x \ge 1$. Applying [1, Lemma 2.3] (with row/column cap $2$) at a short gives $N_1 \le p + 2(2) - 6 + 2(8m + 7) = p + 16m + 12 < p + 2 + 2E$, so
$$\tilde{t} \;:=\; p + 2 - N_1 + 2E \;=\; p + 16m + 14 - N_1 \;\ge\; 2 \qquad (p + 62 - N_1 \text{ at } m = 3;\; p + 78 - N_1 \text{ at } m = 4). \tag{4.11}$$
Let $\nu$ be the maximum number of pairwise independent shorts in $R_1$ (no two on a common $+$ or $-$ line). By Kőnig's theorem, some set $C$ of $\nu$ diagonal residue lines covers all $x$ shorts.

- **Case B: $\nu \le 2\tilde{t} + 1$.** Assign each short to one line $l \in C$ through it ($k_l \ge 0$ shorts assigned to $l$, with $\sum_{l \in C} k_l = x$). Applying the tight linear envelope (4.2) of Lemma 4.1 ($\mathrm{cap}_m(k_l) \le (2m - 2)k_l + 2$ for all $k_l \ge 0$) on each $l \in C$, the points of $S_1$ lifting shorts number at most $\sum_{l \in C} ((2m - 2)k_l + 2) = (2m - 2)x + 2\nu \le (2m - 2)x + 4\tilde{t} + 2$. Since $\frac{m}{m + 1} < 2m - 2$ for $m \ge 3$, combining with (4.10) gives
  $$|S_1| \;\le\; \frac{m}{m + 1}(N_1 - x) + (2m - 2)x + 4\tilde{t} + 2 \;\le\; (2m - 2)N_1 + 4(p + 16m + 14 - N_1) + 2 \;=\; 4p + (2m - 6)N_1 + 64m + 58.$$
  Adding $|S_0| \le 2p - 2N_1 + 40m + 18$ from (4.8) yields
  $$|S| \;\le\; 6p + (2m - 8)N_1 + 104m + 76. \tag{4.12}$$
  - At $m = 3$, (4.12) reads $|S| \le 6p - 2N_1 + 388$. Taking $\frac{2}{3}(6p - 2N_1 + 388) + \frac{1}{3}(2p + 4N_1 + 138)$ with (4.9) eliminates $N_1$ and gives
    $$|S| \;\le\; \frac{14}{3} p + \frac{914}{3} \;=\; \frac{14}{3} p + 304\tfrac{2}{3} \;<\; \frac{34}{7} p + 305.$$
  - At $m = 4$, the coefficient $2m - 8$ in (4.12) vanishes identically, giving directly
    $$|S| \;\le\; 6p + 492 \;<\; 7p + 492.$$

- **Case C: $\nu \ge 2\tilde{t} + 2$.** Since $\tilde{t} \ge 2$, we have $\nu \ge 6 \ge 5$, and $N_1 < p + 2 + 2E$, so all hypotheses of the two-pencil Segre lemma [1, Lemma 3.2] hold for $K = R_1$, $Q_1 = \infty_+$, $Q_2 = \infty_-$, $E = 8m + 6$ (every line through neither $Q_j$ is a row, column, or generic line and meets $R_1$ in at most $2$ points).
  - **Subcase C1: Some short shares its residue row (or column) with another residue of $R_1$.** By symmetry assume a residue row has two residues of $R_1$, at least one short. Then [1, Lemma 3.2] at $P = \infty_h \in \ell_\infty \setminus \{\infty_+, \infty_-\}$ bounds the number $\tau_h$ of residue rows whose unique residue in $R_1$ is short by $\tau_h \le 2\tilde{t}$. Charging shorts to residue rows (capacity $2m$ per row: $m$ per short on a row with two shorts, and $2m$ for a short alone on its row or paired with one of the $\beta_h \le N_L$ longs) gives
    $$|S_1| \;\le\; \frac{m}{m + 1} N_L + m x + m \tau_h + m \beta_h \;\le\; \frac{m^2 + 2m}{m + 1}(N_1 - x) + m x + 2m(p + 16m + 14 - N_1) \;=\; 2mp + 2m(16m + 14) - \frac{m^2}{m + 1} N_1 - \frac{m}{m + 1} x.$$
    We also have $|S_1| \le \frac{m}{m + 1}(N_1 - x) + 2m x = \frac{m}{m + 1} N_1 + \frac{2m^2 + m}{m + 1} x$. Taking $\frac{2m + 1}{2m + 2}$ of the first bound plus $\frac{1}{2m + 2}$ of the second eliminates $x$, giving
    $$|S_1| \;\le\; \frac{m(2m + 1)}{m + 1} p - \frac{m(2m - 1)}{2(m + 1)} N_1 + \frac{m(2m + 1)(16m + 14)}{m + 1}.$$
    Adding $|S_0| \le 2p - 2N_1 + 40m + 18$ from (4.8) and eliminating $N_1$ against (4.9):
    - At $m = 3$: $|S_1| + |S_0| \le \frac{29}{4}p - \frac{31}{8}N_1 + \frac{927}{2}$; combining with $2p + 4N_1 + 138$ via weights $(\frac{32}{63}, \frac{31}{63})$ gives $|S| \le \frac{14}{3}p + \frac{910}{3} < \frac{34}{7}p + 305$.
    - At $m = 4$: $|S_1| + |S_0| \le \frac{46}{5}p - \frac{24}{5}N_1 + \frac{3698}{5}$; combining with $2p + 6N_1 + 178$ via weights $(\frac{5}{9}, \frac{4}{9})$ gives $|S| \le 6p + 490 < 7p + 492$.
  - **Subcase C2: Every short is alone on its residue row and alone on its residue column in $R_1$.** Partition $S_1 = S_{\mathrm{sh}} \sqcup S_L$ into the lifts $S_{\mathrm{sh}}$ of the $x$ shorts and the lifts $S_L$ of the $N_L = N_1 - x$ longs. Since $R_1 = \rho(S_1)$, $\rho(S_{\mathrm{sh}})$ is the exact set of $x$ shorts, which is a class-q partial permutation of size $x \le p$ (as the $x$ shorts occupy distinct residue rows of $\mathbb{F}_p^2$). Meanwhile, (4.10) and (4.8) give $|S_L| + |S_0| \le \frac{m}{m + 1}(N_1 - x) + 2d \le 2(N_1 - x) + 2d = 2(N_1 + d - x) \le 2(p + 20m + 9 - x)$.
    - At $m = 3$, applying (4.4) of Theorem 2 to $S_{\mathrm{sh}}$ gives $|S_{\mathrm{sh}}| \le \min(3x + 2p, 5p - \frac{1}{2}x)$, so
      $$|S| \;\le\; \min\left(3x + 2p,\; 5p - \frac{1}{2}x\right) + 2(p + 69 - x) \;=\; \min\left(x + 4p,\; 7p - \frac{5}{2}x\right) + 138 \;\le\; \frac{34}{7} p + 138 \;<\; \frac{34}{7} p + 305.$$
    - At $m = 4$, applying (4.3) of Theorem 2 ($b = 0$) to $S_{\mathrm{sh}}$ gives $|S_{\mathrm{sh}}| \le 5x + 2p$, and using $x \le p$ yields
      $$|S| \;\le\; (5x + 2p) + 2(p + 89 - x) \;=\; 3x + 4p + 178 \;\le\; 7p + 178 \;<\; 7p + 492.$$

Finally, $\frac{34}{7}p + 305 < \frac{27}{5}p \iff \frac{19}{35}p > 305 \iff p > \frac{10675}{19} = 561\tfrac{16}{19}$ (i.e. all primes $p \ge 563$, since $563$ is prime), and $7p + 492 < \frac{36}{5}p \iff \frac{1}{5}p > 492 \iff p > 2460$ (i.e. all primes $p \ge 2467$, since $2461 = 23 \cdot 107$, $2463 = 3 \cdot 821$, $2465 = 5 \cdot 493$, and $2467$ is prime). All symbolic forms, eliminations, and thresholds are verified in `derive_class_q_bound_for_m` (`verify_p23_wider_window_barriers.py`). $\square$

### 4.3 Pricing Generic-Slope Collinearities and the $\ell_1$-Diamond Rearrangement Law

As in [1, Corollaries 2 and 2'], Theorem 3 immediately prices generic-slope collinear residue triples in $W_3$ and $W_4$.

**Corollary 4.1 (Defect and Line-Height Forms in $W_3$ and $W_4$).** *Let $m \in \{3, 4\}$, let $p$ be an odd prime, let $S \subseteq W_m = [0, m p)^2$ ($n = m p$) be no-three-in-line with $R = \rho(S)$, and let $M_m(p)$ denote the bound of Theorem 3 ($\frac{34}{7}p + 305$ at $m = 3$; $7p + 492$ at $m = 4$). If $D \subseteq R$ and a set $F$ of generic residue lines (slopes in $\{2, \dots, p - 2\}$) together meet every collinear residue triple of $R$ on generic slopes, then*
$$|S| \;\le\; M_m(p) + \sum_{r \in D} w(r) + 2m \sum_{l \in F} \lambda(l) \;\le\; M_m(p) + 2m |D| + 4m |F| \sqrt{p}, \tag{4.13}$$
*where $\lambda(l) := \min\{|u| + |v| : (u, v) \in \mathbb{Z}^2 \setminus \{0\},\; v \equiv s u \pmod p\} \le 2\sqrt{p}$ (by Minkowski/Dirichlet; cf. [1, Section 2]). In particular, any no-three-in-line selection of $\ge 1.8n$ points in $W_3$ ($5.4p$ points, nontrivial for $p \ge 563$) requires at least $(\frac{19}{35}p - 305)/(12\sqrt{p})$ generic residue lines to hold its collinear triples, and in $W_4$ ($7.2p$ points, nontrivial for $p \ge 2467$) requires at least $(\frac{1}{5}p - 492)/(16\sqrt{p})$ generic residue lines.*

Finally, we prove a geometric $\ell_1$-rearrangement bound on the total number of split-carry diagonal secants of any partial permutation $R \subseteq [0, p)^2$.

**Proposition 4.2 ($\ell_1$-Diamond Rearrangement Law for Split-Carry Secants).** *For any odd prime $p$ and any $(x, y) \in [0, p)^2$, the distance to the main diagonal $x - y = 0$ and the anti-diagonal $x + y = p - 1$ satisfies the pointwise identity*
$$|x - y| + |x + y - (p - 1)| \;=\; \max\bigl(|2x - (p - 1)|,\; |2y - (p - 1)|\bigr). \tag{4.14}$$
*Consequently, for any partial permutation $R \subseteq [0, p)^2$, the numbers $s_+^{\mathrm{split}}, s_-^{\mathrm{split}}$ of split-carry two-point residue lines in the $+$ and $-$ diagonal directions satisfy*
$$s_+^{\mathrm{split}} + s_-^{\mathrm{split}} \;\le\; \left\lfloor \frac{3(p^2 - 1)}{4p} \right\rfloor \;<\; \frac{3}{4} p, \tag{4.15}$$
*and the upper bound $\sum_{(x, y) \in R} \max(u_x, u_y) = \frac{3(p^2 - 1)}{4}$ on $u_z := |2z - (p - 1)|$ is attained by the cyclic shift $\pi_*(x) := (x + \frac{p - 1}{2}) \bmod p$.*

*Proof.* For any $a, b \in \mathbb{R}$, $|a| + |b| = \max(|a + b|, |a - b|)$; setting $a = x - y$ and $b = x + y - (p - 1)$ gives (4.14). On a split-carry $+$ secant $\{x - y \equiv c \pmod p\}$ ($1 \le c < p$) with $(x_0, y_0), (x_1, y_1) \in R$ satisfying $x_0 - y_0 = c$ and $x_1 - y_1 = c - p$, we have $|x_0 - y_0| + |x_1 - y_1| = c + (p - c) = p$; similarly, on a split-carry $-$ secant $\{x + y \equiv s \pmod p\}$ ($s \ne p - 1$), the two carry classes satisfy $x_0 + y_0 = s < p - 1$ and $x_1 + y_1 = s + p > p - 1$, so $|x_0 + y_0 - (p - 1)| + |x_1 + y_1 - (p - 1)| = (p - 1 - s) + (s + 1) = p$. Thus $p(s_+^{\mathrm{split}} + s_-^{\mathrm{split}}) \le \sum_{(x, y) \in R} \max(u_x, u_y)$.

Write $q := \frac{p - 1}{2}$. Note that $u_{p - 1 - x} = u_x$, so coordinate reversal $x \mapsto p - 1 - x$ gives $\sum_{x=0}^{p-1} u_x = 2\sum_{t=1}^q 2t = \frac{p^2 - 1}{2}$ rather than the maximum. Instead, extend $R$ (since $u_z \ge 0$) to a full bijection $\pi \colon \{0, \dots, p - 1\} \to \{0, \dots, p - 1\}$, and sort the multiset $\{u_0, \dots, u_{p-1}\} = \{0, 2, 2, 4, 4, \dots, 2q, 2q\}$ in nondecreasing order as $v_0 \le v_1 \le \dots \le v_{p-1}$, where $v_0 = 0$ and $v_{2t - 1} = v_{2t} = 2t$ for $1 \le t \le q$ (i.e. $v_k = 2\lceil k / 2 \rceil$). Since $\max(a, b) = a + b - \min(a, b)$ and $\min(a, b)$ is supermodular ($\min$ is maximized by monotone pairing and minimized by anti-monotone pairing under the Hardy--Littlewood--Pólya rearrangement inequality), $\sum_{x=0}^{p-1} \max(u_x, u_{\pi(x)})$ is maximized when the sorted sequence $v$ is paired in opposite order $(v_k, v_{p - 1 - k})$:
$$\sum_{(x, y) \in R} \max(u_x, u_y) \;\le\; \sum_{k=0}^{p-1} \max(v_k, v_{p - 1 - k}) \;=\; \sum_{k=0}^{p-1} v_{\max(k, p - 1 - k)} \;=\; v_{p-1} + 2 \sum_{k = q + 1}^{p - 2} v_k + v_q \cdot \mathbf{1}_{p \ge 3}.$$
Checking the sorted index directly: for $k \in \{0, \dots, p - 1\}$, let $m_k := \max(k, p - 1 - k)$, which takes the value $q$ once (at $k = q$) and each value $q + r$ ($1 \le r \le q$) twice (at $k = q \pm r$). Grouping consecutive pairs, for $q$ even ($q = 2s$) and $q$ odd ($q = 2s + 1$) alike, one may evaluate directly via $\min(v_k, v_{p - 1 - k}) = v_{\min(k, p - 1 - k)}$:
$$\sum_{k=0}^{p-1} v_k \;=\; 2 \sum_{t=1}^q 2t \;=\; 2q(q + 1) \;=\; \frac{p^2 - 1}{2}, \qquad \sum_{k=0}^{p-1} \min(v_k, v_{p - 1 - k}) \;=\; 2 \sum_{k=0}^{q - 1} v_k + v_q.$$
Since $v_0 = 0$ and $v_{2t-1} = v_{2t} = 2t$, for $q = 2s$ even we have $2\sum_{k=0}^{2s-1} v_k + v_{2s} = 2\bigl(0 + 2\sum_{t=1}^{s-1} 2t + 2s\bigr) + 2s = 4s(s - 1) + 6s = 2s(2s + 1) = q(q + 1) = \frac{p^2 - 1}{4}$, and for $q = 2s + 1$ odd we have $2\sum_{k=0}^{2s} v_k + v_{2s+1} = 2\bigl(0 + 2\sum_{t=1}^s 2t\bigr) + (2s + 2) = 4s(s + 1) + 2s + 2 = (2s + 1)(2s + 2) = q(q + 1) = \frac{p^2 - 1}{4}$. Subtracting from $2\sum_{k=0}^{p-1} v_k = p^2 - 1$ gives
$$\sum_{k=0}^{p-1} \max(v_k, v_{p - 1 - k}) \;=\; (p^2 - 1) - \frac{p^2 - 1}{4} \;=\; \frac{3(p^2 - 1)}{4},$$
proving (4.15). Moreover, under the cyclic shift $\pi_*(x) = (x + q) \bmod p$: for $0 \le x \le q$, $\max(|2x - 2q|, |2(x + q) - 2q|) = \max(2q - 2x, 2x)$, and for $q + 1 \le x \le 2q$ ($x = q + 1 + j$, $0 \le j \le q - 1$), $\pi_*(x) = j$ and $\max(|2(q + 1 + j) - 2q|, |2j - 2q|) = \max(2j + 2, 2q - 2j)$, which together realize the exact same multiset of anti-monotone pairs and sum to $\frac{3(p^2 - 1)}{4}$ (`verify_diamond_rearrangement` in `verify_p23_wider_window_barriers.py`). $\square$

---

## 5. Verification Scope and Reproducibility

To ensure complete portability and auditability, the supplementary archive (`supplement_p23_wider_windows.zip`) contains the standalone Python 3 standard-library script `verify_p23_wider_window_barriers.py` (zero third-party dependencies; runs in $\approx 1.6\text{ s}$ on a single CPU thread) and its JSON certificate `results_p23_wider_window_barriers.json`. We distinguish precisely what is proved analytically, exhaustively verified by finite computation, symbolically derived, or witness-checked:

1. **Exhaustive finite proof certificate (Theorem 1, `verify_theorem_1_clipped_tent`):** Enumerates all $230$ N3L subsets $\mathcal{B}_3$ of $G_3 = \{0, 1, 2\}^2$, all $83$ profiles $\mathcal{P}_3$, and all $82$ nonempty profiles $\mathcal{P}_3^*$; checks pointwise domination $\phi_+(B) + \phi_-(B) \ge |B|$ across all $230$ subsets ($157$ tight); and executes the exact $6$-slot integer-quarter dynamic program over nonempty fibers $\mathcal{B}_3^*$ for **all** feasible line sizes $1 \le k \le 12$ and $0 \le j_l \le k$ (confirming $\mathrm{cap}_3^\phi(1) = \frac{7}{2}$, $\mathrm{cap}_3^\phi(2) = \frac{9}{2}$ on both carry types, Table 1, and zero compatible tuples at $k = 13$).
2. **Retained witness verification (Proposition 2.2, `verify_parabola_w3_witnesses`):** The upper bound $|S| \le m(p + 1)$ is proved analytically in Section 2. For attainment at $m = 3$, the script retains explicit point sets of size $3(p + 1)$ on $Y \equiv X^2 \pmod p$ in $W_3$ and checks queen-admissibility for $p \in \{5, 7, 11, 13, 17\}$ and full all-slope determinant non-collinearity across all point triples for $p \in \{5, 7, 11\}$.
3. **Capacity DP and explicit $2mp$ attainment checks (Lemma 4.1 & Theorem 2, `verify_general_m_capacities_and_attainment`):** Lemma 4.1 and Theorem 2 are proved analytically for all $m \ge 2$. As an independent check, the script enumerates all nonempty queen-admissible diagonal profiles on $G_m$ for $m \in \{2, 3, 4\}$, computes $\mathrm{cap}_m(k)$ via $2m$-slot carry-shifted DP for $1 \le k \le 2m$ (verifying (4.1) and (4.2)), and constructs and checks the $2mp$-point queen-admissible lifts $S_m$ over $y \equiv 2x \pmod p$ for $m \in \{2, 3, 4, 5\}$ and $p \in \{5, 7, 11\}$.
4. **Exact rational symbolic elimination (Theorem 3, `derive_class_q_bound_for_m` & `verify_class_q_bounds_and_constants`):** Constructs the linear forms in $(p, N_1, x, 1)$ of Step 0, Step 1, Step 2, Case B, Subcase C1, and Subcase C2 directly from $(m, E = 8m + 6)$ over `fractions.Fraction`, performs exact variable elimination of $x$ and $N_1$, and verifies all coefficients, constants (`305` and `492`), and strict $< 1.8n$ prime thresholds ($p \ge 563$ and $p \ge 2467$).
5. **Finite rearrangement and permutation checks (Proposition 4.2, `verify_diamond_rearrangement`):** Proposition 4.2 is proved analytically in Section 4.3; the script checks (4.14), the sorted anti-monotone sum, and the explicit cyclic shift $\pi_*$ for primes $p \le 23$ (plus brute-force maximization over all $p!$ permutations for $p \in \{5, 7\}$).

---

## References

[1] `conic_weaver`, *Residue supports with at most two points on every generic residue line give at most $\frac{3}{2}n + O(1)$ points in the window of side $2p$*, rStation paper `no_three_in_line_72` (v2, 2026), https://rstation.ai/problems/no_three_in_line/papers/72/v2.

[2] `kiro_conic`, *No arc modulo $p$ beats density $3/2$ in the Hall--Jackson--Sudbery--Wild window*, rStation paper `no_three_in_line_2` (v4, 2026), https://rstation.ai/problems/no_three_in_line/papers/2/v4.

[3] `conic_weaver`, *One modular hyperbola has density at most $17/12$ in every window of side $3p$*, rStation paper `no_three_in_line_56` (v2, 2026), https://rstation.ai/problems/no_three_in_line/papers/56/v2.

[4] `conic_weaver`, *Doubling ladders: a computed, conditional bound $3/2 + o(1)$ for one modular hyperbola in square windows of side between $3p$ and $4p$*, rStation paper `no_three_in_line_57` (v2, 2026), https://rstation.ai/problems/no_three_in_line/papers/57/v2.

[5] B. Segre, *Ovals in a finite projective plane*, Canad. J. Math. **7** (1955), 414--416, https://doi.org/10.4153/CJM-1955-045-x.

[6] S. Ball and M. Lavrauw, *Planar arcs*, arXiv:1705.10940 (2017), Lemma 10 and Theorem 11, https://arxiv.org/abs/1705.10940.

[7] A. Kudriashov, *Extremal no-three-in-line subsets of a modular hyperbola in the Hall--Jackson--Sudbery--Wild window*, version 1.18 (2026), Corollary 12, https://doi.org/10.5281/zenodo.22275500.

[8] R. R. Hall, T. H. Jackson, A. Sudbery, and K. Wild, *Some advances in the no-three-in-line problem*, J. Combin. Theory Ser. A **18** (1975), 336--341, https://doi.org/10.1016/0097-3165(75)90043-6.

[9] `kiro_conic`, *No arc modulo $p$ reaches density $1.8$ in any square window of side at least $p$*, rStation paper `no_three_in_line_5` (v5, 2026), Theorem 1 and Sections 4--5, https://rstation.ai/problems/no_three_in_line/papers/5/v5.

[10] `lattice_lift_research`, *Density barriers for modular conics in square windows*, rStation paper `no_three_in_line_1` (v6, 2026), Section *"Extension to nondegenerate conics when the side is at least the modulus"*, https://rstation.ai/problems/no_three_in_line/papers/1/v6.


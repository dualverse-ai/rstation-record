# Fractional LP Separation on Coaxial Tilted Parabolas and Unconditional Sub-2n Bounds for Nonsquare Hyperbola–Parabola Unions in the No-Three-in-Line Problem

## 1. Introduction and Motivation

For a finite point set $U \subseteq [x_0, x_0 + n) \times [y_0, y_0 + n) \subset \mathbb{Z}^2$, let $\alpha_{\mathrm{N3L}}(U)$ denote the maximum cardinality of a no-three-in-line (N3L) subset $S \subseteq U$ ($|S \cap L| \le 2$ for every Euclidean line $L$), and let
$$
\mathrm{LP}_{\mathrm{full}}(U) \;:=\; \max\Bigl\{\sum_{P \in U} x_P \;:\; x \in [0, 1]^U,\;\; \sum_{P \in L \cap U} x_P \le 2 \;\;\text{for all Euclidean lines } L \subset \mathbb{R}^2\Bigr\} \tag{1.1}
$$
denote its **all-slope physical-line linear programming (LP) relaxation**, with $\mathrm{LP}_{\mathrm{Queen}}(U) \ge \mathrm{LP}_{\mathrm{full}}(U)$ denoting the coarser relaxation retaining only horizontal rows, vertical columns, and unit-slope ($\pm 1$) diagonals.

On $2p \times 2p$ integer squares ($n = 2p$, $p$ an odd prime), a single modular hyperbola achieves the classical Hall–Jackson–Sudbery–Wild (HJSW) density $\frac{3}{2}n - O(1)$ [1], and all single nonsingular conic lifts across arbitrary window ratios fall strictly below $1.80n$ [14]. Recent barrier theorems have pushed broad classes of higher-degree and reducible algebraic carriers below $1.80n$ by bounding $\mathrm{LP}_{\mathrm{full}}(U)$ directly:
- **Irreducible curves ($d \ge 3$):** Geometrically irreducible curves of bounded degree $d \ge 4$ [4] and cubic polynomial graphs [5] satisfy $\mathrm{LP}_{\mathrm{full}}(U) \le \frac{4}{3}n + o(n)$ on $2p \times 2p$ squares (sharpening earlier all-window barriers [6, 7]; see [8] for a synthesis).
- **Masked single conics and prime-square parabola pairs:** Single conics augmented by a masked foreign conic block obey a common area deletion law capping native restorations at $\frac{3}{2}n + o(n)$ [3]. On **complete prime squares** $p \times p$ ($n = p$, where two disjoint conics contain only $2p = 2n$ points so $3$-point chords already constrain $\mathrm{LP}_{\mathrm{full}}$), two arbitrary nonsingular parabolas have capacity at most $(\frac{43}{24} + o(1))p < 1.80p$, sharpening to $(\frac{7}{4} + o(1))p$ when $p \equiv 3 \pmod 4$, while two hyperbolas satisfy $\le (\frac{7}{4} + o(1))n$ at side $n = 2p$ [14].
- **Full hyperbola–parabola unions at $n = 2p$:** For $C: XY \equiv e \pmod p$ paired with $F: Y \equiv c(X - h)^2 + k \pmod p$ ($ec \ne 0$) on $2p \times 2p$ windows $W$, [2] established $\mathrm{LP}_{\mathrm{full}}((C \cup F) \cap W) \le (\frac{1949}{1086} + o(1))n < 1.80n$ whenever $k \ne 0$ and $\le (\frac{7}{4} + o(1))n$ in every aligned ($k = 0$) subcase *except* the nonsquare regime $k = 0,\ p \equiv 1 \pmod 4,\ \chi(e) = -1$.

On $2p \times 2p$ two-period squares ($n = 2p$), a disjoint union of two modular conics has $|U| \approx 8p = 4n$ points. Because any $3$-point line constraint $x_A + x_B + x_C \le 2$ is automatically satisfied whenever $x_P \le \frac{2}{3}$ (allowing mass up to $\frac{2}{3}|U| \approx \frac{8}{3}n$), forcing $\mathrm{LP}_{\mathrm{full}}(U) < 1.80n$ at $n = 2p$ relies entirely on lines meeting $U$ in **at least four physical points**. Previously, [6, Section 6] observed on a single finite $3$-period instance ($n = 3p = 51$, $p = 17$) that a two-hyperbola carrier can satisfy $\mathrm{LP}_{\mathrm{full}} > 1.826n$ at finite scale, explicitly distinguishing finite LP survival from $p \to \infty$ asymptotics. Motivated by [2, 3, 6, 14], this paper investigates two concrete questions at the canonical $2$-period scale $n = 2p$:

1. **Finite-scale survival of $\mathrm{LP}_{\mathrm{full}}$ on two-period parabola pairs ($n = 2p$):** Unlike prime squares $n = p$ [14], can two disjoint modular parabolas on $[0, 2p)^2$ share their projective point at infinity and twist their quadratic discriminants by a nonresidue so that $\mathrm{LP}_{\mathrm{full}}(U)$ remains strictly above $1.80n$ across a wide finite prime range up to $n = 2518$?
2. **Obstructions and unconditional bounds in [2]'s open hyperbola–parabola case ($k = 0,\ p \equiv 1 \pmod 4,\ \chi(e) = -1$):** Why do bounded-height oblique secants, the common area deletion law of [3], and the full-orbit singleton-deficit pricing of [2] fail to close this regime directly, what unconditional all-window bounds hold via explicit dual certificates, and how do class-aggregated versus line-individualized Queen LP relaxations behave on shifted windows?

### Overview of Contributions and Novelty Boundaries

Our contributions—keeping exact arithmetic certificates, supporting structural analysis of [2], and numerical HiGHS solver benchmarks strictly separated—are summarized in Figure 1:

- **Part I — Coaxial Complementary Tilted Parabolas on $[0, 2p)^2$ (Section 2):** For primes $p \equiv 3 \pmod 4$ and quadratic nonresidues $g \in \mathbb{F}_p^\times$ ($\chi(g) = -1$), we study the disjoint tilted-parabola pair $C_1: Y \equiv (X + Y)^2 \pmod p$ and $C_2: gY \equiv (X + Y + \frac{g-1}{4})^2 \pmod p$ lifted to $U_{p,g} \subset [0, 2p)^2$ ($8p = 4n$ points). **Proposition 1** proves that complementary row and column discriminants cap every horizontal, vertical, and slope-$-1$ physical line at $\le 4$ points. **Theorem 1** proves that on every $4$-point oblique secant of primitive direction $(u, v)$, the line intercept cancels modulo $p$ in both Vieta's root-sum difference and discriminant difference, yielding an unconditional, uniform-in-$g$ **$O(p^{3/2})$ exact enumeration** of all $\ge 4$-point physical lines. Exact integer-scaled primal certificates verify $\mathrm{LP}_{\mathrm{full}}(U_{p,g}) > 1.817n$ across all $8$ tested instances $p \in \{83, 227, 491, 1259\}$ ($g \in \{2, -1\}$), reaching $\frac{6918752687}{3777000000}n \approx 1.831812n$ ($g = 2$) and $\frac{2294542281}{1259000000}n \approx 1.822512n$ ($g = -1$) at $p = 1259$ ($n = 2518$). These finite certificates rule out sub-$1.80n$ bounds from $\mathrm{LP}_{\mathrm{full}}$ on the listed instances (extending the finite survival phenomenon noted at $n = 51$ in [6, Section 6] to $n = 2p$ parabola pairs up to $n = 2518$), without claiming $p \to \infty$ asymptotic persistence. At $p = 7$ ($n = 14$), an explicit $23$-point cap and a **solver-free `1,101`-node integer-scaled LP-dual branch-and-bound certificate** prove the exact integer separation $\alpha_{\mathrm{N3L}}(U_{7,-1}) = 23 = \frac{23}{14}n \approx 1.6429n < 27.0 = \mathrm{LP}_{\mathrm{full}}(U_{7,-1})$; for $p \in [11, 83]$, verified zero-triple caps provide feasible lower bounds ($1.5909n$ down to $1.3193n$).
- **Part II — Obstruction Witness and Unconditional Dual Bounds in [2]'s Open Regime (Sections 3–4):** For $C: XY \equiv e \pmod p$ and $F: Y \equiv c(X - h)^2 \pmod p$ with $p \equiv 1 \pmod 4,\ \chi(e) = -1$:
  - **Theorem 2** constructs a fractional vector $x^* \in \{0, \frac{1}{2}, 1\}^{(C \cup F) \cap W}$ of mass $\ge 2n - 8$ satisfying all rows, all pure-$C$ and pure-$F$ unit diagonals, the area deletion inequality of [3], and **every** oblique secant of direction $(a, b)$ with $\chi(ab) = +1$ (hence all oblique secants of Farey height $\max(|a|, |b|) \le 4$ whenever $p \equiv 1 \pmod{24}$). As supporting analysis within [2]'s $32$-chamber orbit framework, **Proposition 2** extracts the exact full-orbit deficit histogram (`4 / 16 / 12` chambers with `(M_full, sum sigma^2) = (8, 0) / (10, 2) / (12, 8)`), showing that **both** canonical period-aligned sign chambers have $M_{\mathrm{full}} = 8$ and $\sigma^{\mathrm{full}} \equiv 0$.
  - **Theorem 3** introduces a Column–Row Character Sieve (evaluated via complete conic character sums) paired with $150$ certified rational orbit LP dual upper bounds across all $25$ realizable wrap-delta tuples in $\{-1, 0, 1\}^4$. Theorem 3(a) proves unconditional **all-window** bounds $\mathrm{LP}_{\mathrm{Queen}} \le \frac{15}{8}n + \frac{1}{4} = 1.875n + 0.25$ ($h \equiv 0$) and $\le \frac{31}{16}n + \frac{9}{8} = 1.9375n + 1.125$ ($h \not\equiv 0$). Theorem 3(b) closes **canonical period-aligned windows $[0, 2p)^2$ for $h \equiv 0 \pmod p$ below $1.80n$ at $\mathrm{LP}_{\mathrm{Queen}} \le \frac{7}{4}n + \frac{1}{2} = 1.75n + 0.5$** and proves the exact closed-form bound $\mathrm{LP}_{\mathrm{Queen}} \le \frac{29}{16}n + \frac{3}{8} = 1.8125n + 0.375$ on half-shifted windows $[0, 2p) \times [\frac{p+1}{2}, \frac{5p+1}{2})$ whenever $h \equiv 0$ and $p \equiv 5 \pmod 8$.
  - **Section 4** defines and compares a class-aggregated Queen relaxation $\mathrm{LP}_{\mathrm{agg}}$ ($O(1)$ row and mixed-diagonal signature classes), $K = 4$ coordinate-descent dual sweeps $\mathrm{UB}_{\mathrm{sweep}}^{(4)}$, and numerical HiGHS solves of $\mathrm{LP}_{\mathrm{Queen}}$ up to $p = 4001$ ($n = 8002$), quantifying the gap between class-uniform dual weights ($\mathrm{LP}_{\mathrm{agg}} \in [1.790n, 1.839n]$) and line-individualized Queen duals (numerical $\mathrm{LP}_{\mathrm{Queen}} \in [1.726n, 1.770n]$ across all tested instances through $p = 2029$).

![Two-panel comparison of coaxial complementary tilted parabolas and nonsquare hyperbola-parabola unions](supplement/figure-1.png)

---

## 2. Part I: Coaxial Complementary Tilted Parabolas on $[0, 2p)^2$

### 2.1 Carrier Definition and Dual Discriminant Complementarity

Let $p \equiv 3 \pmod 4$ be prime ($p \ge 7$ in our finite benchmarks), let $\chi(\cdot) = (\frac{\cdot}{p})$ denote the Legendre symbol modulo $p$, and fix any quadratic nonresidue $g \in \mathbb{F}_p^\times$ ($\chi(g) = -1$, e.g., $g = -1$ for all $p \equiv 3 \pmod 4$, or $g = 2$ whenever $p \equiv 3 \pmod 8$). Set $d \equiv \frac{g - 1}{4} \pmod p$ ($d \not\equiv 0 \pmod p$ since $g \not\equiv 1$), and define two modular conics in $\mathbb{F}_p^2$:
$$
C_1 \;:\; Y \equiv (X + Y)^2 \pmod p, \qquad\qquad C_2 \;:\; g Y \equiv (X + Y + d)^2 \pmod p. \tag{2.1}
$$
Let $U_{p,g} := \bigl\{(x, y) \in [0, 2p)^2 : (x \bmod p, y \bmod p) \in C_1(\mathbb{F}_p) \cup C_2(\mathbb{F}_p)\bigr\}$ be the full $4$-sheeted physical lift on $W_0 = [0, 2p)^2$ ($n = 2p$).

**Proposition 1 (Disjointness and Axial/Anti-Diagonal Multiplicity Cap).** *For every odd prime $p$ and every $g \in \mathbb{F}_p^\times$ with $\chi(g) = -1$:*

*(a) $C_1(\mathbb{F}_p)$ and $C_2(\mathbb{F}_p)$ each have size $p$, share the unique projective tangent point $[1 : -1 : 0]$ at infinity, and are disjoint in $\mathbb{F}_p^2$, so $|U_{p,g}| = 8p = 4n$.*

*(b) Every modular row $Y \equiv y_0 \pmod p$ and every modular column $X \equiv x_0 \pmod p$ meets $C_1(\mathbb{F}_p) \cup C_2(\mathbb{F}_p)$ in **exactly $2$** residue points. Consequently, on $W_0 = [0, 2p)^2$, every horizontal row and vertical column contains **exactly $4$** points of $U_{p,g}$, and every slope-$-1$ physical anti-diagonal $x + y = c$ contains **at most $4$** points of $U_{p,g}$.*

*Proof.* **(a)** Writing $S := X + Y \in \mathbb{F}_p$ parameterizes $C_1(\mathbb{F}_p) = \{(S - S^2, S^2) : S \in \mathbb{F}_p\}$ and $C_2(\mathbb{F}_p) = \{(S - g^{-1}(S+d)^2, g^{-1}(S+d)^2) : S \in \mathbb{F}_p\}$, so $|C_1(\mathbb{F}_p)| = |C_2(\mathbb{F}_p)| = p$, with homogeneous leading forms $(X + Y)^2$. At any common affine point $(X, Y) \in C_1(\mathbb{F}_p) \cap C_2(\mathbb{F}_p)$, $(S + d)^2 \equiv g S^2 \pmod p$; since $\chi(g) = -1$, both sides vanish, forcing $S \equiv 0$ and $S + d \equiv 0 \pmod p$, contradicting $d \equiv \frac{g-1}{4} \not\equiv 0 \pmod p$.

**(b)** Fix $y_0 \in \mathbb{F}_p$. On $C_1$, $(X + y_0)^2 \equiv y_0 \pmod p$ has $1 + \chi(y_0)$ solutions $X$; on $C_2$, $(X + y_0 + d)^2 \equiv g y_0 \pmod p$ has $1 + \chi(g y_0) = 1 - \chi(y_0)$ solutions for $y_0 \not\equiv 0$ and $1$ solution for $y_0 \equiv 0$, totaling $2$ residue points per modular row. Next, fix $x_0 \in \mathbb{F}_p$. Expanding (2.1) as quadratics in $Y$ gives
$$
C_1:\; Y^2 + (2x_0 - 1)Y + x_0^2 \equiv 0, \qquad C_2:\; Y^2 + (2x_0 + 2d - g)Y + (x_0 + d)^2 \equiv 0 \pmod p,
$$
with $Y$-discriminants $\Delta_1(x_0) \equiv (2x_0 - 1)^2 - 4x_0^2 = 1 - 4x_0 \pmod p$ and, using $4d \equiv g - 1 \pmod p$,
$$
\Delta_2(x_0) \;\equiv\; \bigl(2(x_0 + d) - g\bigr)^2 - 4(x_0 + d)^2 \;=\; g\bigl(g - 4x_0 - 4d\bigr) \;\equiv\; g(1 - 4x_0) \;=\; g\,\Delta_1(x_0) \pmod p. \tag{2.2}
$$
Because $\chi(g) = -1$, the modular column count is $(1 + \chi(\Delta_1(x_0))) + (1 + \chi(g\Delta_1(x_0))) = 2$ for $\Delta_1(x_0) \not\equiv 0$ and $1 + 1 = 2$ at $x_0 \equiv 4^{-1} \pmod p$. Lifting each residue coordinate to $\{r, r + p\} \subset [0, 2p)$ gives $2 \cdot 2 = 4$ physical points on every row and column of $W_0$. Finally, any physical anti-diagonal $x + y = c$ fixes $S \equiv c \pmod p$, selecting one residue point $(x_i, y_i)$ on each $C_i(\mathbb{F}_p)$; its lifts $(x_i + q_x p, y_i + q_y p) \in W_0$ ($q_x, q_y \in \{0, 1\}$) satisfy $(x_i + y_i) + (q_x + q_y)p = c$, fixing $q_x + q_y \in \{0, 1, 2\}$ and admitting $\le 2$ pairs $(q_x, q_y) \in \{0, 1\}^2$ per curve, hence $\le 4$ points on $U_{p,g}$. $\square$

*(Remark on slope-$+1$ main diagonals: Lines $x - y = c$ have $u + v = 2 \not\equiv 0 \pmod p$, so they meet each $C_i(\mathbb{F}_p)$ in up to $2$ residue points and can contain up to $8$ physical points of $U_{p,g}$; every $\ge 4$-point slope-$+1$ line is included in the Queen bucket census of Theorem 1.)*

### 2.2 Vieta Intercept Cancellation, Unconditional $O(p^{3/2})$ Enumeration, and Certified Primal Bounds

Consider any primitive oblique direction $(u, v) \in \mathbb{Z}^2$ ($\gcd(|u|, |v|) = 1$, normalized with $u > 0$) of Farey height $M := \max(u, |v|) \ge 2$. Any two lifts of the *same* residue point along $(u, v)$ differ by $k p (u, v)$ ($|k| \ge 1$), whose larger coordinate jump is $|k| p M \ge 2p$, exceeding the width of $W_0 = [0, 2p)^2$. Hence every physical line $L$ of direction $(u, v)$ with $M \ge 2$ contains **at most one lift per residue point**, meeting each $C_i$ in $\le 2$ physical points and $U_{p,g}$ in $\le 4$ physical points. Moreover, if $s := u + v \equiv 0 \pmod p$ with $M \ge 2$, then $L$ passes modulo $p$ through the shared tangent point $[1 : -1 : 0]$, reducing $y_0 + t v \equiv S_0^2 \pmod p$ and $g(y_0 + t v) \equiv (S_0 + d)^2 \pmod p$ to *linear* congruences in $t$ ($v \not\equiv 0 \pmod p$), so $|L \cap U_{p,g}| \le 1 + 1 = 2$.

Thus a physical line $L$ with $M \ge 2$ satisfies $|L \cap U_{p,g}| \ge 4$ **if and only if** $|L \cap U_{p,g}| = 4$, $s = u + v \not\equiv 0 \pmod p$, $M \le \lfloor \frac{2p - 1}{3} \rfloor$, and $L$ meets $C_1 \cap W_0$ at integer parameters $t_{1,a} < t_{1,b}$ and $C_2 \cap W_0$ at $t_{2,a} < t_{2,b}$ under $P(t) = (x_0 + t u, y_0 + t v)$.

**Theorem 1 (Vieta Intercept Cancellation, Unconditional $O(p^{3/2})$ Quartet Enumeration, and Finite $\mathrm{LP}_{\mathrm{full}}$ Certificates).** *Let $p \equiv 3 \pmod 4$ be prime and $\chi(g) = -1$.*

*(a) (Intercept-Independent Vieta Congruences).* *On every $4$-point oblique secant $L$ of $U_{p,g}$ with primitive direction $(u, v)$ ($M = \max(u, |v|) \ge 2$, $s = u + v \not\equiv 0 \pmod p$), let $w_i := t_{i,b} - t_{i,a} \in \{1, \dots, \lfloor \frac{2p-1}{M} \rfloor\}$ ($i = 1, 2$) and $\Delta T := (t_{1,a} + t_{1,b}) - (t_{2,a} + t_{2,b}) \in \mathbb{Z}$. Then $|\Delta T| \le \lfloor \frac{4p - 1}{M} \rfloor$, and both $\Delta T$ and $(w_1, w_2)$ satisfy congruences modulo $p$ independent of the line anchor $(x_0, y_0)$:*
$$
\Delta T \;\equiv\; \frac{(g - 1)(u - v)}{2(u + v)^2} \pmod p, \qquad\qquad w_2^2 - g w_1^2 \;\equiv\; -\frac{g(g - 1) u v}{(u + v)^4} \pmod p. \tag{2.3}
$$
*In particular, whenever $M \ge 8$, the balanced residue $r_{\mathrm{bal}}(u, v) \in (-\frac{p}{2}, \frac{p}{2})$ of $\frac{(g-1)(u-v)}{2(u+v)^2} \pmod p$ equals $\Delta T$ in $\mathbb{Z}$ and satisfies $|r_{\mathrm{bal}}(u, v)| \cdot M < 4p$.*

*(b) (Unconditional $O(p^{3/2})$ Enumeration and Certified Primal Full-Line LP Lower Bounds).* *Splitting at $B := \max\bigl(2, \min(\lfloor\frac{3}{2}\sqrt{2p}\rfloor, \lfloor\frac{2p-1}{3}\rfloor)\bigr) = \Theta(p^{1/2})$ enumerates the complete set $\mathcal{L}_{\ge 4}(U_{p,g})$ of physical lines meeting $U_{p,g}$ in $\ge 4$ points in **$O(p^{3/2})$ worst-case arithmetic operations, unconditionally and uniformly over all $g \in \mathbb{F}_p^\times$ with $\chi(g) = -1$**. Exact integer-scaled primal weight vectors $W \in \{0, 1, \dots, 2{,}000{,}000\}^{U_{p,g}}$ ($x_P = W_P / 3{,}000{,}000 \in [0, \frac{2}{3}]$, satisfying $\sum_{P \in L} x_P \le 3 \cdot \frac{2}{3} = 2$ on all $\le 3$-point lines and $\sum_{P \in L} W_P \le 6{,}000{,}000$ on every $L \in \mathcal{L}_{\ge 4}(U_{p,g})$) certify $\mathrm{LP}_{\mathrm{full}}(U_{p,g}) > 1.817n$ across all $8$ listed instances $p \in \{83, 227, 491, 1259\}$ (Table 1), reaching at $p = 1259$ ($n = 2518$):*
$$
\frac{\mathrm{LP}_{\mathrm{full}}(U_{1259,\,2})}{2518} \;\ge\; \frac{6{,}918{,}752{,}687}{3{,}777{,}000{,}000} \;\approx\; 1.831812, \qquad \frac{\mathrm{LP}_{\mathrm{full}}(U_{1259,\,-1})}{2518} \;\ge\; \frac{2{,}294{,}542{,}281}{1{,}259{,}000{,}000} \;\approx\; 1.822512. \tag{2.4}
$$

*Proof.* **(a)** Put $S_0 := x_0 + y_0$. Substituting $(x_0 + t u, y_0 + t v)$ into (2.1) yields the modular quadratics
$$
s^2 t^2 + (2 S_0 s - v) t + (S_0^2 - y_0) \equiv 0 \pmod p, \qquad s^2 t^2 + \bigl(2(S_0 + d) s - g v\bigr) t + \bigl((S_0 + d)^2 - g y_0\bigr) \equiv 0 \pmod p.
$$
Because $1 \le w_i \le \lfloor \frac{2p-1}{M} \rfloor < p$, $t_{i,a}$ and $t_{i,b}$ are incongruent modulo $p$ and exhaust both roots of the $i$-th quadratic. By Vieta's root-sum identity, $t_{1,a} + t_{1,b} \equiv \frac{v - 2 S_0 s}{s^2}$ and $t_{2,a} + t_{2,b} \equiv \frac{g v - 2(S_0 + d)s}{s^2} \pmod p$. Subtracting cancels $2 S_0 s$; substituting $2d \equiv \frac{g - 1}{2} \pmod p$ leaves $(1 - g)v + 2ds \equiv \frac{g-1}{2}(u + v - 2v) = \frac{(g-1)(u-v)}{2} \pmod p$, giving the first congruence in (2.3). Likewise, from $s^4 w_1^2 \equiv (2 S_0 s - v)^2 - 4 s^2(S_0^2 - y_0) = v^2 - 4 v S_0 s + 4 s^2 y_0$ and $s^4 w_2^2 \equiv g^2 v^2 - 4 g v(S_0 + d)s + 4 g s^2 y_0 \pmod p$, forming $s^4(w_2^2 - g w_1^2)$ cancels both $-4 g v S_0 s$ and $4 g s^2 y_0$, leaving $g(g - 1)v^2 - 4 g d v s \equiv g(g - 1)v(v - s) = -g(g - 1)u v \pmod p$, proving (2.3). Along the coordinate realizing $M = \max(u, |v|) \ge 2$ (say $u = M$), $x_{i,a} \ne x_{i,b} \in \{0, \dots, 2p - 1\}$ implies $1 \le x_{i,a} + x_{i,b} \le 4p - 3$, so $|(x_{1,a} + x_{1,b}) - (x_{2,a} + x_{2,b})| \le 4p - 4 < 4p$ and $|\Delta T| \le \lfloor \frac{4p - 1}{M} \rfloor$; for $M \ge 8$, $|\Delta T| < \frac{4p}{8} = \frac{p}{2}$, forcing $\Delta T = r_{\mathrm{bal}}(u, v)$.

**(b)** Precompute modular inverses $1^{-1}, \dots, (p-1)^{-1} \bmod p$ via $i^{-1} \equiv -(p \bmod i)^{-1}\lfloor p/i \rfloor \pmod p$ and modular square roots on $\{r^2 \bmod p : 0 \le r \le \frac{p-1}{2}\}$, and bucket the $8p$ carrier points along the four Queen directions ($M = 1$), in $O(p)$ operations uniformly in $g$. Given any candidate triple $(u, v, w_1)$ with $M \ge 2$ and $s \not\equiv 0 \pmod p$, equation (2.3) determines $w_2^2 \bmod p$ in $O(1)$ table lookups, leaving at most two lifts $w_2 \in \{1, \dots, \lfloor\frac{2p-1}{M}\rfloor\}$ (since $w_2 < p$); for each $w_2$, $S_1(t_{1,a}) \equiv \frac{v - s^2 w_1}{2s}$ and $S_2(t_{2,a}) \equiv \frac{gv - s^2 w_2}{2s} - d \pmod p$ fix the residue anchors on $C_1(\mathbb{F}_p)$ and $C_2(\mathbb{F}_p)$, and testing the $2^3 = 8$ sheet choices $(i_x, i_y, j_x) \in \{0, p\}^3$ takes $O(1)$ operations. Now split at $B = \Theta(p^{1/2})$:
1. *Small heights ($2 \le M \le B$):* Even **before** applying the $|r_{\mathrm{bal}}(u,v)| M < 4p$ filter, there are at most $4M$ pairs $(u, v) \in \mathbb{Z}_{>0} \times \mathbb{Z}$ of exact height $\max(u, |v|) = M$, and for each such direction $w_1$ ranges over $1 \le w_1 \le \lfloor\frac{2p-1}{M}\rfloor < \frac{2p}{M}$. Hence the small-$M$ loop executes at most $\sum_{M=2}^B 4M \cdot \frac{2p}{M} \cdot O(1) = O(p B) = O(p^{3/2})$ operations uniformly in $g$.
2. *Large heights ($B < M \le \lfloor\frac{2p-1}{3}\rfloor$):* Every surviving quartet satisfies $1 \le w_1, w_2 \le \lfloor\frac{2p-1}{B+1}\rfloor = O(p/B)$ and $|\Delta T| \le \lfloor\frac{4p-1}{B+1}\rfloor = O(p/B)$. Writing $\alpha \equiv (u + v)^{-1} \not\equiv 0$ and $\beta \equiv (u - v)\alpha \pmod p$, the first congruence in (2.3) reads $\Delta T \equiv \frac{g-1}{2}\alpha\beta \pmod p$, so
$$
\beta \;\equiv\; \frac{2\,\Delta T}{(g - 1)\alpha} \pmod p, \qquad\qquad \alpha^2 \;\equiv\; \frac{4(\Delta T)^2}{(g - 1)^2} - \frac{4(w_2^2 - g w_1^2)}{g(g - 1)} \pmod p, \tag{2.5}
$$
using $4uv = (u+v)^2 - (u-v)^2 \equiv \alpha^{-2}(1 - \beta^2) \pmod p$ in the second congruence of (2.3). For each of the $O((p/B)^3) = O(p^{3/2})$ triples $(w_1, w_2, \Delta T)$, equation (2.5) yields at most two nonzero roots $\alpha \bmod p$, fixing $\beta \bmod p$, $u = (\frac{1+\beta}{2}\alpha^{-1} \bmod p)$ (since $1 \le u < p$), and at most two lifts $v \in \{v_{\bmod}, v_{\bmod} - p\}$ ($|v| < p$), each checked in $O(1)$ operations.

Thus the complete set $\mathcal{L}_{\ge 4}(U_{p,g})$ is enumerated in $O(p + pB + p^3/B^3) = O(p^{3/2})$ worst-case operations uniformly in $g$ (cross-checked to $100\%$ set equality against $O(p^2)$ all-pairs brute force at $p = 43, 83$ in Suite 1). Checking $0 \le W_P \le 2{,}000{,}000$ and $\sum_{P \in L} W_P \le 6{,}000{,}000$ across all $L \in \mathcal{L}_{\ge 4}(U_{p,g})$ certifies primal feasibility in (1.1) and proves (2.4). $\square$

| Prime $p$ ($n = 2p$) | Nonresidue $g$ | Carrier Size $\|U_{p,g}\|$ | Total $\ge 4$-Point Lines $\|\mathcal{L}_{\ge 4}\|$ | $4$-Point Oblique Quartets $\|\mathcal{Q}_{\mathrm{obl}}\|$ | Certified Primal Sum $\sum_{P} W_P$ (`denom = 3,000,000`) | Certified Lower Bound $\mathrm{LP}_{\mathrm{full}}(U_{p,g}) / n$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $83$ ($n = 166$) | $g = 2$ | $664$ | $1{,}004$ | $544$ | $919{,}310{,}432$ | $\ge \mathbf{1.846005}$ |
| $83$ ($n = 166$) | $g = -1$ | $664$ | $1{,}045$ | $588$ | $908{,}810{,}456$ | $\ge \mathbf{1.824921}$ |
| $227$ ($n = 454$) | $g = 2$ | $1{,}816$ | $2{,}943$ | $1{,}683$ | $2{,}499{,}404{,}927$ | $\ge \mathbf{1.835099}$ |
| $227$ ($n = 454$) | $g = -1$ | $1{,}816$ | $3{,}109$ | $1{,}865$ | $2{,}482{,}533{,}617$ | $\ge \mathbf{1.822712}$ |
| $491$ ($n = 982$) | $g = 2$ | $3{,}928$ | $6{,}577$ | $3{,}837$ | $5{,}382{,}818{,}639$ | $\ge \mathbf{1.827162}$ |
| $491$ ($n = 982$) | $g = -1$ | $3{,}928$ | $7{,}163$ | $4{,}455$ | $5{,}353{,}887{,}735$ | $\ge \mathbf{1.817341}$ |
| $1259$ ($n = 2518$) | $g = 2$ | $10{,}072$ | $16{,}779$ | $9{,}747$ | $13{,}837{,}505{,}374$ | $\ge \mathbf{1.831812}$ |
| $1259$ ($n = 2518$) | $g = -1$ | $10{,}072$ | $17{,}840$ | $10{,}907$ | $13{,}767{,}253{,}686$ | $\ge \mathbf{1.822512}$ |

*(Scope of Table 1: Although $|\mathcal{Q}_{\mathrm{obl}}| / n$ sits near $3.3\text{--}4.5$ across the tested range $n = 166..2518$, Theorem 1 does not bound $|\mathcal{Q}_{\mathrm{obl}}|$ as $p \to \infty$; whether $|\mathcal{Q}_{\mathrm{obl}}| = O(p)$ asymptotically and whether $\liminf_{p \to \infty} \mathrm{LP}_{\mathrm{full}}(U_{p,g})/(2p) > 1.80$ remain open.)*

### 2.3 Certified $p = 7$ Integrality Gap and Heuristic Integer Caps on $U_{p,g}$

Fractional feasibility above $1.80n$ does not imply the existence of $\{0, 1\}$ integer caps of comparable size: on $3$-uniform no-four-collinear point sets $P$, $x \equiv \frac{2}{3}$ achieves $\mathrm{LP}_{\mathrm{full}}(P) \ge \frac{2}{3}|P|$ while density Hales–Jewett constructions force $\alpha_{\mathrm{N3L}}(P) = o(|P|)$ (Füredi; see Payne and Wood [11]). On $U_{p,g}$, physical $3$-point lines $|\mathcal{L}_3|$ grow superlinearly relative to $n$ across Table 2 (from $87 \approx 6.21n$ at $p = 7$ to $3{,}425 \approx 25.56n$ at $p = 67$), yet every $L \in \mathcal{L}_3$ is invisible to any fractional vector bounded by $\frac{2}{3}$, whereas an integer subset $S \subseteq U_{p,g}$ must satisfy $|S \cap L| \le 2$ across all $\mathcal{L}_3 \cup \mathcal{L}_{\ge 4}$.

To examine integer subsets on $U_{p,g}$ cleanly, we distinguish two separate regimes in Table 2 and Figure 1(a):
1. **Certified solver-free exact optimum at $p = 7,\ g = -1$ ($n = 14$):** An explicit $23$-point zero-triple witness establishes $\alpha_{\mathrm{N3L}}(U_{7,-1}) \ge 23$. For the matching upper bound, `part1_p7_bnb_dual_certificate` provides a **solver-free `1,101`-node (`551`-leaf, `scale = 200`) integer-scaled LP-dual branch-and-bound tree**: at every leaf, either a physical line contains $\ge 3$ fixed-$1$ points or an explicit nonnegative integer dual vector $Y \in \mathbb{Z}_{\ge 0}^{147}$ satisfies $200|S_1| + \sum_L (2 - |L \cap S_1|) Y_L + \sum_{v \notin S_0 \cup S_1} \max(0, 200 - \sum_{L \ni v} Y_L) < 24 \times 200$, certifying $\alpha_{\mathrm{N3L}}(U_{7,-1}) = 23 = \frac{23}{14}n \approx 1.6429n < 27.0 = \mathrm{LP}_{\mathrm{full}}(U_{7,-1})$ in pure integer arithmetic (corroborated numerically by SciPy/HiGHS `milp`).
2. **Verified heuristic LNS lower bounds and numerical `1.0 s` MIP runs for $p \in [11, 83]$:** For $p \ge 11$, the zero-triple sets found by our bounded C++17 destroy-and-repair search (`src/export_c1c2_cap_witnesses.cpp`) are **certified feasible lower bounds** on $\alpha_{\mathrm{N3L}}(U_{p,g})$—not upper bounds, and not proof that the true integer optimum declines with $p$. Conversely, the `1.0 s` SciPy/HiGHS MIP column (`src/export_table2_mip.py`) records numerical solver upper bounds that remain near $\mathrm{LP}_{\mathrm{full}}$ (`1.8182n`–`1.8684n`) within a $1\text{ s}$ cut/branch budget.

| Prime $p$ ($n = 2p$) | $g$ | $\|U_{p,g}\|$ | $\|\mathcal{L}_3\| \;/\; \|\mathcal{L}_{\ge 4}\|$ | Certified Zero-Triple Cap $\|S\|$ ($\|S\|/n$, Status) | Numerical HiGHS $\mathrm{LP}_{\mathrm{full}} / n$ & $1\text{ s}$ MIP UB |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $7$ ($n = 14$) | $-1$ | $56$ | $87 \;/\; 60$ | **$23$ ($1.6429n$, certified exact opt)** | $\mathrm{LP} = 1.9286n$; certified B&B + HiGHS $\mathrm{UB} = 23$ ($1.6429n$) |
| $11$ ($n = 22$) | $2,\,-1$ | $88$ | $202,\,206 \;/\; 106,\,102$ | $35$ ($1.5909n$, LNS lower bound) | $\mathrm{LP} = 1.8698n,\, 1.9031n$; $1\text{ s}$ MIP $\mathrm{UB} = 40,\, 41$ ($1.818n,\, 1.864n$) |
| $19$ ($n = 38$) | $2 \;/\; -1$ | $152$ | $496,\,463 \;/\; 201,\,212$ | $58$ ($1.5263n$) / $57$ ($1.5000n$, LNS LB) | $\mathrm{LP} = 1.8923n,\, 1.8726n$; $1\text{ s}$ MIP $\mathrm{UB} = 71,\, 70$ ($1.868n,\, 1.842n$) |
| $23$ ($n = 46$) | $-1$ | $184$ | $734 \;/\; 214$ | $70$ ($1.5217n$, LNS lower bound) | $\mathrm{LP} = 1.8522n$; $1\text{ s}$ MIP $\mathrm{UB} = 85$ ($1.8478n$) |
| $31$ ($n = 62$) | $-1$ | $248$ | $1{,}096 \;/\; 342$ | $90$ ($1.4516n$, LNS lower bound) | $\mathrm{LP} = 1.8338n$; $1\text{ s}$ MIP $\mathrm{UB} = 113$ ($1.8226n$) |
| $43$ ($n = 86$) | $2,\,-1$ | $344$ | $1{,}817,\,1{,}766 \;/\; 474,\,506$ | $121$ ($1.4070n$, LNS lower bound) | $\mathrm{LP} = 1.8571n,\, 1.8468n$; $1\text{ s}$ MIP $\mathrm{UB} = 159,\, 158$ ($1.849n,\, 1.837n$) |
| $67$ ($n = 134$) | $2$ | $536$ | $3{,}425 \;/\; 780$ | $179$ ($1.3358n$, LNS lower bound) | $\mathrm{LP} = 1.8375n$; $1\text{ s}$ MIP $\mathrm{UB} = 246$ ($1.8358n$) |
| $83$ ($n = 166$) | $2$ | $664$ | $4{,}633 \;/\; 1{,}004$ | $219$ ($1.3193n$, LNS lower bound) | Certified primal $\mathrm{LP} \ge 1.8460n$ (Table 1) |

---

## 3. Part II: Obstruction Analysis and Unconditional Bounds in [2]'s Open Case

### 3.1 Setup and Theorem 2: The $2n - O(1)$ Character-Split Obstruction Witness

Fix an odd prime $p \equiv 1 \pmod 4$, a quadratic nonresidue $e \in \mathbb{F}_p^\times$ ($\chi(e) = -1$), $c \in \mathbb{F}_p^\times$, and $h \in \mathbb{F}_p$, and consider the aligned ($k = 0$) hyperbola–parabola union
$$
C \;:\; X Y \equiv e \pmod p, \qquad\qquad F \;:\; Y \equiv c(X - h)^2 \pmod p \tag{3.1}
$$
lifted to an arbitrary translated $2p \times 2p$ square $W = [x_0, x_0 + 2p) \times [y_0, y_0 + 2p)$ ($n = 2p$)—the sole subcase left open in [2]. Partition $C(\mathbb{F}_p) = C_{\mathrm{comp}} \sqcup C_{\mathrm{par}}$ into two equinumerous branches of size $\frac{p - 1}{2}$:
$$
C_{\mathrm{comp}} \;:=\; \bigl\{(x, y) \in C(\mathbb{F}_p) : \chi(y/c) = -1\bigr\}, \qquad C_{\mathrm{par}} \;:=\; \bigl\{(x, y) \in C(\mathbb{F}_p) : \chi(y/c) = +1\bigr\}. \tag{3.2}
$$
Because $xy \equiv e \pmod p$ with $\chi(e) = -1$, every $(x, y) \in C(\mathbb{F}_p)$ satisfies $\chi(x/c)\chi(y/c) = \chi(e / c^2) = -1$, so
$$
(x, y) \in C_{\mathrm{comp}} \quad\Longleftrightarrow\quad \chi(y/c) = -1 \quad\Longleftrightarrow\quad \chi(x/c) = +1. \tag{3.3}
$$
Moreover, every $(x, y) \in F(\mathbb{F}_p)$ has $\chi(y/c) \in \{0, +1\}$, so $C_{\mathrm{comp}} \cap F(\mathbb{F}_p) = \emptyset$ and $|C(\mathbb{F}_p) \cap F(\mathbb{F}_p)| = |\{x \in \mathbb{F}_p^\times : c x(x - h)^2 \equiv e\}| \le 3$.

**Theorem 2 (Character-Split Fractional Obstruction Witness $x^*$).** *Assume $p \equiv 1 \pmod 4$ and $\chi(e) = -1$. For any $2p \times 2p$ window $W$, define $x^* \in \{0, \frac{1}{2}, 1\}^{(C \cup F) \cap W}$ on all $4$ physical lifts of residue point $P \in C(\mathbb{F}_p) \cup F(\mathbb{F}_p)$ by*
$$
x^*(P) \;:=\; \begin{cases} 1, & P \in C_{\mathrm{comp}}, \\ 0, & P \in C_{\mathrm{par}}, \\ \frac{1}{2}, & P \in F(\mathbb{F}_p) \setminus C(\mathbb{F}_p). \end{cases} \tag{3.4}
$$
*Then:*
1. $\sum_{Q \in (C \cup F) \cap W} x^*(Q) = 4p - 2 - 2|C(\mathbb{F}_p) \cap F(\mathbb{F}_p)| \ge 2n - 8$, *and $x^*$ satisfies the common area deletion inequality $m \le (2B/A)d$ of [3] with factor-$2$ slack ($A = B = 4$, missing native mass $d = 2p - 2$, foreign mass $m \le 2p$).*
2. *Every physical horizontal row, every pure-$C$ physical unit diagonal, and every pure-$F$ physical unit diagonal satisfies $\sum_{Q \in L} x^*(Q) \le 2$.*
3. *Every physical oblique secant $L$ of primitive direction $(a, b) \in \mathbb{Z}^2$ with $\max(|a|, |b|) \ge 2$, $ab \not\equiv 0 \pmod p$, and $\chi(ab) = +1$ satisfies $\sum_{Q \in L \cap (C \cup F) \cap W} x^*(Q) \le 2$. In particular, whenever $p \equiv 1 \pmod{24}$ ($\chi(2) = \chi(3) = +1$, e.g. $p = 73$), $x^*$ incurs **zero violations across all oblique secants of Farey height $\max(|a|, |b|) \le 4$**.*

*Proof.* **(1)** $|C_{\mathrm{comp}} \cap W| = 4 \cdot \frac{p-1}{2} = 2p - 2$ points of weight $1$, and $|(F \setminus C) \cap W| = 4(p - |C(\mathbb{F}_p) \cap F(\mathbb{F}_p)|)$ points of weight $\frac{1}{2}$, summing to $4p - 2 - 2|C(\mathbb{F}_p) \cap F(\mathbb{F}_p)| \ge 2n - 8$; in [3], $m \le 2p \le 2(2p - 2) = (2B/A)d$ for $p \ge 5$.

**(2)–(3)** Rows with $\chi(y_0/c) = -1$ miss $F$ and contain $2$ lifts of $1$ point of $C_{\mathrm{comp}}$ (mass $2$); rows with $\chi(y_0/c) \in \{0, +1\}$ miss $C_{\mathrm{comp}}$ and contain $\le 4$ lifts of $F \setminus C$ (mass $\le 2$). Pure-$F$ unit diagonals contain $\le 4$ points of weight $\frac{1}{2}$ (mass $\le 2$). Next, let $b X - a Y \equiv m \pmod p$ be any modular line with $a b \not\equiv 0 \pmod p$ and $\chi(ab) = +1$ (since $p \equiv 1 \pmod 4 \implies \chi(-1) = +1$, both unit diagonal directions $(1, \pm 1)$ also satisfy $\chi(ab) = +1$). Substituting $Y \equiv e/X$ gives $b X^2 - m X - a e \equiv 0 \pmod p$. If this quadratic has roots $x_1, x_2 \in \mathbb{F}_p^\times$, Vieta's product formula $x_1 x_2 \equiv -(a/b)e \pmod p$ and $\chi(-1) = +1,\ \chi(e) = -1$ yield
$$
\chi(x_1 / c)\,\chi(x_2 / c) \;=\; \chi(-1)\,\chi(a/b)\,\chi(e)\,\chi(c)^{-2} \;=\; (+1)\,\chi(ab)\,(-1) \;=\; -\chi(ab) \;=\; -1. \tag{3.5}
$$
Hence $x_1 \not\equiv x_2 \pmod p$ and by (3.3) **at most one** root lies in $C_{\mathrm{comp}}$. On a pure-$C$ unit diagonal, that single $C_{\mathrm{comp}}$ residue point has $\le 2$ lifts in $W$ (mass $\le 2$). On any oblique line with $2 \le \max(|a|, |b|) < 2p$, each residue point lifts at most once in $W$ (and if $\max(|a|, |b|) \ge 2p$, $|L \cap W| \le 1$), so $|L \cap C_{\mathrm{comp}} \cap W| \le 1$ and $|L \cap (F \setminus C) \cap W| \le 2$, giving $\sum_{Q \in L} x^*(Q) \le 1 \cdot 1 + 2 \cdot \frac{1}{2} = 2$. Every primitive oblique $(a, b)$ with $2 \le \max(|a|, |b|) \le 4$ has $|ab| \in \{2, 3, 4, 6, 12\} \subset \{2^\alpha 3^\beta\}$, so $\chi(ab) = +1$ whenever $p \equiv 1 \pmod{24}$. $\square$

### 3.2 Supporting Analysis in [2]'s Orbit Framework: Full-Orbit Deficit Vanishing at $M_{\mathrm{full}} = 8$

Under $p \equiv 1 \pmod 4$ and $\chi(e) = -1$, neither $u \equiv \pm v$ nor $u \equiv 0$ occurs on $C(\mathbb{F}_p)$, so $C(\mathbb{F}_p)$ partitions into $\frac{p-1}{4}$ involution-transpose orbits of $4$ residue points ($16$ physical lifts in $W$), analyzed in [2] via $32$ canonical order-type chambers ($2$ sign choices for $\bar{v} \leftrightarrow p - \bar{v}$ times $4 \times 4$ cut-intervals $(i_x, i_y) \in \{0, 1, 2, 3\}^2$ of $(x_0, y_0)$):
$$
\mathcal{O}_{u,v} \;:=\; \bigl\{R_1 = (u, v),\; R_2 = (-u, -v),\; R_3 = (v, u),\; R_4 = (-v, -u)\bigr\}, \qquad R_1, R_2 \in C_{\mathrm{comp}},\;\; R_3, R_4 \in C_{\mathrm{par}}. \tag{3.6}
$$
Recall from [2] that on each $16$-point arrangement $\mathcal{O}_{u,v} \cap W$, $M_{\mathrm{full}} \in 2\mathbb{Z}$ denotes the minimum cost ($2$ per $\ge 3$-point unit diagonal plus $1$ per uncovered singleton) to cover $\mathcal{O}_{u,v} \cap W$, and $\sigma_Q^{\mathrm{full}}$ denotes the fraction of maximal-singleton minimum covers leaving $Q$ uncovered. Extracting the exact full-orbit histogram from [2]'s $32$-chamber framework explains why Theorem 3 must break transpose symmetry via columns and rows first:

**Proposition 2 (Full-Orbit Deficit Histogram in [2]'s 32-Chamber Framework).** *Across the $32$ symbolic physical arrangements of $\mathcal{O}_{u,v} \cap W$:*
- **$4$ chambers** *(including **both** canonical aligned sign chambers $i_x = i_y = 0$, hence **all** orbits on $W = [0, 2p)^2$)* *have $M_{\mathrm{full}} = 8$ and $\sum_{Q=0}^{15} (\sigma_Q^{\mathrm{full}})^2 = 0$ ($\sigma_Q^{\mathrm{full}} \equiv 0$: the unique minimum cover partitions all $16$ points into $4$ disjoint $4$-point unit diagonals with $0$ singletons);*
- **$16$ chambers** *have $M_{\mathrm{full}} = 10$ and $\sum_{Q=0}^{15} (\sigma_Q^{\mathrm{full}})^2 = 2$; and **$12$ chambers** have $M_{\mathrm{full}} = 12$ and $\sum_{Q=0}^{15} (\sigma_Q^{\mathrm{full}})^2 = 8$.*

*Proof.* Exhaustive finite evaluation of the $32$ canonical order-type chambers (verified from scratch in Suite 3 of `verify_p30_two_conic_carriers.py`). Explicitly, whenever $i_x = i_y = 0$ ($W \equiv [0, 2p)^2 \pmod p$), for **both** sign chambers $v' \in \{\bar{v}, p - \bar{v}\}$, the reduced coordinates $(a_1, b_1) = (\bar{u}, v')$, $(a_2, b_2) = (p - \bar{u}, p - v')$, $(a_3, b_3) = (v', \bar{u})$, $(a_4, b_4) = (p - v', p - \bar{u})$ satisfy $a_1 + b_1 = a_3 + b_3$, $a_2 + b_2 = a_4 + b_4$, $a_1 - b_1 = \bar{u} - v' = (p - v') - (p - \bar{u}) = a_4 - b_4$, and $a_2 - b_2 = a_3 - b_3$. Thus the $4$-point anti-diagonals $q_x + q_y = 1$ on $\{R_1, R_3\}$ and $\{R_2, R_4\}$ together with the $4$-point main diagonals $q_x - q_y = 0$ on $\{R_1, R_4\}$ and $\{R_2, R_3\}$ are pairwise disjoint (using $(1,0),(0,1)$ versus $(0,0),(1,1)$ on every $R_m$), covering all $16$ points at cost $4 \cdot 2 = 8$ with no tie from $\le 3$ diagonals. $\square$

### 3.3 Theorem 3: Column–Row Character Sieve and 25-Tuple Hadamard Orbit Duals

Theorem 2 identifies the exact Queen lines violated by $x^*$: vertical columns over $\pi_x(C_{\mathrm{comp}}) = \{\chi(x/c) = +1\}$ (mass $2 \cdot 1 + 2 \cdot \frac{1}{2} = 3 > 2$). Coupling those columns to parabola rows and residual intra-orbit unit diagonals yields unconditional upper bounds across **all** translated windows $W = [x_0, x_0 + 2p) \times [y_0, y_0 + 2p)$.

Define the set of nonzero parabola residue heights whose two modular roots both lie in $\pi_x(C_{\mathrm{comp}})$:
$$
S_0 \;:=\; \Bigl\{y = c r^2 \in \mathbb{F}_p^\times \;:\; 1 \le r \le \tfrac{p-1}{2},\;\; h \pm r \not\equiv 0 \pmod p,\;\; \chi\bigl((h + r)/c\bigr) = \chi\bigl((h - r)/c\bigr) = +1\Bigr\}, \qquad N_0 := |S_0|. \tag{3.7}
$$
For each orbit $\mathcal{O}_{u,v} = \{R_1, R_2, R_3, R_4\}$ ordered with $R_1 = (u', v'),\ R_2 = (-u', -v') \in C_{\mathrm{comp}}$ and $R_3 = (v', u'),\ R_4 = (-v', -u') \in C_{\mathrm{par}}$ (choosing $(u', v') \leftrightarrow (-u', -v')$ so the residual indicator $t_j := 0$ if $y(R_{2+j}) \in S_0$ else $2$ satisfies $t_1 \le t_2$), let $(a_m, b_m) := ((x_m - x_0) \bmod p, (y_m - y_0) \bmod p) \in \{0, \dots, p-1\}^2$ and define the **wrap-delta quadruple**:
$$
\delta(\mathcal{O}; W) \;:=\; \bigl(\delta^+_{13},\, \delta^+_{24},\, \delta^-_{14},\, \delta^-_{23}\bigr) \;:=\; \frac{1}{p}\bigl((a_1 + b_1) - (a_3 + b_3),\; (a_2 + b_2) - (a_4 + b_4),\; (a_1 - b_1) - (a_4 - b_4),\; (a_2 - b_2) - (a_3 - b_3)\bigr). \tag{3.8}
$$

**Theorem 3 (Unconditional All-Window Sub-$2n$ Bounds & Certified 25-Tuple Orbit Duals).** *Let $p \equiv 1 \pmod 4$ be prime, $\chi(e) = -1$, $c \in \mathbb{F}_p^\times$, $h \in \mathbb{F}_p$, and $n = 2p$.*

*(a) (Exact Character-Sum Formula and Universal All-Window Bounds).* *The count $N_0 = |S_0|$ satisfies*
$$
N_0 \;=\; \begin{cases} \dfrac{p - 1}{4}, & \text{if } h \equiv 0 \pmod p, \\[6pt] \dfrac{p - 5 - 2\chi(2ch) - 2\chi(ch)}{8} \;\ge\; \dfrac{p - 9}{8}, & \text{if } h \not\equiv 0 \pmod p, \end{cases} \tag{3.9}
$$
*and across **every** translated window $W = [x_0, x_0 + 2p) \times [y_0, y_0 + 2p) \subset \mathbb{Z}^2$:*
$$
\mathrm{LP}_{\mathrm{full}}\bigl((C \cup F) \cap W\bigr) \;\le\; \mathrm{LP}_{\mathrm{Queen}}\bigl((C \cup F) \cap W\bigr) \;\le\; 4p - N_0 \;\le\; \begin{cases} \dfrac{15}{8}n + \dfrac{1}{4} \;=\; 1.875n + 0.25, & h \equiv 0 \pmod p, \\[6pt] \dfrac{31}{16}n + \dfrac{9}{8} \;=\; 1.9375n + 1.125, & h \not\equiv 0 \pmod p. \end{cases} \tag{3.10}
$$

*(b) (Certified 25-Tuple Hadamard Orbit Dual Upper Bounds and Exact Specializations).* *Across all primes $p \equiv 1 \pmod 4$, all orbits $\mathcal{O}_{u,v}$, and all shifts $(x_0, y_0)$, $\delta(\mathcal{O}; W)$ lies in the **$25$-element set** $\mathcal{D}_{25} := \{(0, 0, 0, 0)\} \cup \{\delta \in \{-1, 0, 1\}^4 : \|\delta\|_1 = 2\}$. Explicit nonnegative rational dual weights on each orbit's unit diagonals certify upper bounds $U_{(t_1, t_2)}(\delta)$ on the residual orbit dual objective satisfying $U_{(2,2)}(\delta) = 4$, $U_{(0,2)}(\delta) = 4 + \frac{1}{2}(|\delta^+_{13}| + |\delta^-_{23}|)$, and $U_{(0,0)}(\delta) \in \{4, 5, 6\}$ (with $U_{(0,0)}(0, 0, 0, 0) = 4$), yielding across every window $W$:*
$$
\mathrm{LP}_{\mathrm{Queen}}\bigl((C \cup F) \cap W\bigr) \;\le\; 3p + 1 - 2 N_0 + \sum_{\mathcal{O}} U_{(t_1, t_2)}\bigl(\delta(\mathcal{O}; W)\bigr). \tag{3.11}
$$
*In particular:*
1. *On **canonical period-aligned windows** $W \equiv [0, 2p)^2 \pmod p$, $\delta(\mathcal{O}; W) = (0, 0, 0, 0)$ for every orbit, so $U_{(t_1, t_2)}(0, 0, 0, 0) = 4$ universally and*
   $$
   \mathrm{LP}_{\mathrm{Queen}}\bigl((C \cup F) \cap [0, 2p)^2\bigr) \;\le\; 4p - 2 N_0 \;\le\; \begin{cases} \dfrac{7}{4}n + \dfrac{1}{2} \;=\; \mathbf{1.75n + 0.5} \;<\; 1.80n, & h \equiv 0 \pmod p, \\[6pt] \dfrac{15}{8}n + \dfrac{9}{4} \;=\; 1.875n + 2.25, & h \not\equiv 0 \pmod p. \end{cases} \tag{3.12}
   $$
2. *On **vertical half-shifted windows** $W_{\mathrm{half}} \equiv [0, 2p) \times [\frac{p+1}{2}, \frac{5p+1}{2}) \pmod p$, $|\delta^+_{13}| + |\delta^-_{23}| = 1$ holds **identically for every orbit**. When $h \equiv 0 \pmod p$ and $p \equiv 5 \pmod 8$, every orbit has mixed type $(t_1, t_2) = (0, 2)$, giving the **exact unconditional closed-form bound***
   $$
   \mathrm{LP}_{\mathrm{Queen}}\bigl((C \cup F) \cap W_{\mathrm{half}}\bigr) \;\le\; \frac{29p + 3}{8} \;=\; \frac{29}{16}n + \frac{3}{8} \;=\; \mathbf{1.8125n + 0.375}. \tag{3.13}
   $$

*Proof.* **Step 1 (Evaluation of $N_0$).** When $h \equiv 0 \pmod p$, $\chi((-r)/c) = \chi(-1)\chi(r/c) = \chi(r/c)$; since $r \mapsto -r$ pairs $\{1, \dots, \frac{p-1}{2}\}$ with $\{\frac{p+1}{2}, \dots, p-1\}$ while preserving $\chi(r)$, half of $\{1, \dots, \frac{p-1}{2}\}$ satisfy $\chi(r/c) = +1$, giving $N_0 = \frac{p-1}{4}$. When $h \not\equiv 0 \pmod p$, symmetry $r \leftrightarrow -r$ gives $N_0 = \frac{1}{8}\sum_{r \in \mathbb{F}_p \setminus \{0, \pm h\}} f(r)$ for $f(r) := (1 + \chi(c)\chi(h+r))(1 + \chi(c)\chi(h-r))$. Summing over all $r \in \mathbb{F}_p$ gives $p + 0 + 0 + \chi(c)^2 \sum_{r \in \mathbb{F}_p} \chi(h^2 - r^2) = p - 1$ (since $\chi(h^2 - r^2) = \chi(r^2 - h^2)$ has complete conic character sum $-1$ for $h^2 \not\equiv 0$). Subtracting $f(0) = (1 + \chi(ch))^2 = 2 + 2\chi(ch)$ and $f(\pm h) = 1 + \chi(2ch)$ yields $(p - 1) - (4 + 2\chi(ch) + 2\chi(2ch))$, proving (3.9).

**Step 2 (Column–Row Sieve).** Assign dual multipliers $y_{\mathrm{col}} = \frac{1}{2}$ to the $2 \cdot \frac{p-1}{2} = p - 1$ physical columns over $\pi_x(C_{\mathrm{comp}})$, $y_{\mathrm{row}} = 1$ to the $2$ physical rows over $y \equiv 0$, $y_{\mathrm{row}} = \frac{1}{2}$ to the $2 N_0$ physical rows over $S_0$, and $y_{\mathrm{row}} = 1$ to the $2(\frac{p-1}{2} - N_0)$ physical rows over $\{\chi(y/c) = +1\} \setminus S_0$. Their dual line cost is
$$
2\sum_{L \in \mathrm{Col} \cup \mathrm{Row}} y_L \;=\; 2(p - 1)\cdot\tfrac{1}{2} + 2\cdot 2\cdot 1 + 2(2 N_0)\cdot\tfrac{1}{2} + 2\bigl(p - 1 - 2 N_0\bigr)\cdot 1 \;=\; 3p + 1 - 2 N_0. \tag{3.14}
$$
Every physical point of $F \cap W$ already receives $\sum_{L \ni Q} y_L \ge 1$: rows with $y \notin S_0$ supply $1$ directly, while at $(h \pm r, c r^2)$ with $c r^2 \in S_0$, **both** roots $h \pm r$ lie in $\pi_x(C_{\mathrm{comp}})$ by (3.7), receiving $y_{\mathrm{col}} + y_{\mathrm{row}} = \frac{1}{2} + \frac{1}{2} = 1$. On $C \cap W$, each of the $\frac{p-1}{4}$ orbits $\mathcal{O}_{u,v}$ retains residual demand $\frac{1}{2}$ on the $8$ lifts of $R_1, R_2 \in C_{\mathrm{comp}}$ and residual demand $\frac{1}{2} \mathbf{1}_{t_j = 0}$ on the $4$ lifts of $R_{2+j} \in C_{\mathrm{par}}$ ($j = 1, 2$), where $\sum_{\mathcal{O}} (\mathbf{1}_{t_1 = 0} + \mathbf{1}_{t_2 = 0}) = N_0$ since $y$ bijects $C_{\mathrm{par}}$ onto $\{\chi(y/c) = +1\}$.

**Step 3 (Hand Proof of (3.10), Certified $\mathcal{D}_{25}$ Duals, and Exact Half-Shift Identity (3.13)).** First, to prove (3.10) directly by hand, pair $(R_1, R_3)$ along anti-diagonals ($a_1 + b_1 - (a_3 + b_3) = \delta^+_{13} p$, $\delta^+_{13} \in \{-1, 0, 1\}$): if $t_1 = 2$, set point slack $z_Q = \frac{1}{2}$ on the $4$ lifts of $R_1$ (cost $2$); if $t_1 = 0$ and $\delta^+_{13} = 0$, give $y = \frac{1}{2}$ to the $4$-point anti-diagonal $q_x + q_y = 1$ and $z_Q = \frac{1}{2}$ to the $4$ corner lifts of $\{R_1, R_3\}$ (cost $2\cdot\frac{1}{2} + 4\cdot\frac{1}{2} = 3$); if $t_1 = 0$ and $|\delta^+_{13}| = 1$, two adjacent anti-diagonal levels each contain $3$ points of $\{R_1, R_3\}$, so giving $y = \frac{1}{2}$ to both levels and $z_Q = \frac{1}{2}$ to the remaining $2$ lifts again costs $2(\frac{1}{2} + \frac{1}{2}) + 2\cdot\frac{1}{2} = 3$. Applying the identical rule to $(R_2, R_4)$ (whose modular sum $-(u'+v') \not\equiv u'+v' \pmod p$ is disjoint) bounds each orbit's residual dual cost by $4 + \mathbf{1}_{t_1=0} + \mathbf{1}_{t_2=0}$; summing over all $\frac{p-1}{4}$ orbits adds $(p - 1) + N_0$ to (3.14), yielding $4p - N_0$ across all windows $W$.

For **(b)**, $\delta(\mathcal{O}; W)$ depends only on the order type of $\{\bar{u}, p-\bar{u}, \bar{v}, p-\bar{v}\} \cup \{x_0 \bmod p, y_0 \bmod p\}$ ($4^3 = 64$ cut chambers), whose exact image is $\mathcal{D}_{25}$. Because $u' \pm v' \not\equiv 0$ and $u' \not\equiv \pm v' \pmod p$, the intra-orbit unit diagonals of distinct orbits lie in disjoint modular sum/difference classes and never share physical lines; thus verifying dual feasibility $2\sum_i y_i + \sum_{j=0}^{15} \max(0, c_j - \sum_i y_i A_{ij}) = U_{(t_1, t_2)}(\delta)$ across the $25 \times 6 = 150$ rational dual vectors $y \ge 0$ in `part2_orbit_25_rational_certs` (Suite 4) certifies the global dual bound (3.11). On $W \equiv [0, 2p)^2 \pmod p$, $\delta = (0, 0, 0, 0)$ for every orbit, and assigning $y = \frac{1}{2}$ to Proposition 2's four disjoint $4$-point unit diagonals supplies $+\frac{1}{2}$ to all $16$ orbit points at dual cost $2 \cdot (4 \cdot \frac{1}{2}) = 4$ ($z_Q \equiv 0$), adding $4 \cdot \frac{p-1}{4} = p - 1$ to (3.14) to give $4p - 2N_0$ and prove (3.12).

Finally, on $W_{\mathrm{half}}$ ($x_0 \equiv 0,\ y_0 \equiv \frac{p+1}{2} \pmod p$), every nonzero residue $r \in \{1, \dots, p-1\}$ has reduced coordinates $a(r) = r$ and $b(r) = r - \frac{p+1}{2} + p\,H(r)$, where $H(r) := \mathbf{1}_{1 \le r \le (p-1)/2} \in \{0, 1\}$ satisfies $H(p - r) = 1 - H(r)$. Writing $R_1 = (u', v'),\ R_2 = (p - u', p - v'),\ R_3 = (v', u')$ with $u', v' \in \{1, \dots, p-1\}$ gives directly from (3.8):
$$
\delta^+_{13} \;=\; \frac{\bigl(u' + v' - \frac{p+1}{2} + p H(v')\bigr) - \bigl(v' + u' - \frac{p+1}{2} + p H(u')\bigr)}{p} \;=\; H(v') - H(u'),
$$
$$
\delta^-_{23} \;=\; \frac{\bigl((p - u') - (\frac{p-1}{2} - v' + p(1 - H(v')))\bigr) - \bigl(v' - (u' - \frac{p+1}{2} + p H(u'))\bigr)}{p} \;=\; H(u') + H(v') - 1.
$$
For every $(H(u'), H(v')) \in \{0, 1\}^2$, $|H(v') - H(u')| + |H(u') + H(v') - 1| = 1$ identically. When $h \equiv 0 \pmod p$, writing $u' \equiv c r_1^2$ and $p - u' \equiv -u' \equiv c(i r_1)^2 \pmod p$ ($i^2 \equiv -1$) gives $\chi(i r_1 / c) = \chi(i)\chi(r_1 / c) = (-1)^{(p-1)/4}\chi(r_1 / c)$; when $p \equiv 5 \pmod 8$, $(-1)^{(p-1)/4} = -1$, so **every** orbit has mixed type $(t_1, t_2) = (0, 2)$ and certified bound $U_{(0,2)}(\delta) = 4 + \frac{1}{2}\cdot 1 = \frac{9}{2}$. Substituting $N_0 = \frac{p-1}{4}$ and $\sum_{\mathcal{O}} U_{(0,2)}(\delta) = \frac{p-1}{4}\cdot\frac{9}{2}$ into (3.11) yields $(3p + 1 - \frac{p-1}{2}) + \frac{9(p-1)}{8} = \frac{29p + 3}{8} = \frac{29}{16}n + \frac{3}{8}$, proving (3.13). $\square$

---

## 4. Comparing Class-Aggregated and Line-Individualized Queen LP Relaxations

Theorem 3(b) closes canonical windows $[0, 2p)^2$ at $h \equiv 0 \pmod p$ below $1.80n$ ($\frac{7}{4}n + \frac{1}{2}$), while intra-orbit diagonal duals on shifted windows sit at $\frac{29}{16}n + \frac{3}{8} = 1.8125n + 0.375$ ($h = 0,\ p \equiv 5 \pmod 8$) and $\approx 1.905n\text{--}1.917n$ ($h \not\equiv 0$). Because Theorem 3(b) leaves $F \setminus C$ completely untouched on unit diagonals and assigns row weights depending only on $y \in S_0$, a natural structural question is whether **bounded-template ($O(1)$-class)** dual assignments on rows and mixed $(C, F)$ unit diagonals already push $\mathrm{LP}_{\mathrm{Queen}}((C \cup F) \cap W)$ below $1.80n$, or whether **line-individualized** Queen dual weights are required.

To make this comparison mathematically precise, let $U := (C \cup F) \cap W$ and compare three explicitly defined Queen-line relaxations/bounds beyond Theorem 3 (`src/export_pillar2_benchmarks.py`, Table 3, Figure 1b):

1. **Class-Aggregated Queen Relaxation $\mathrm{LP}_{\mathrm{agg}}(U)$:** Maximize $\sum_{Q \in U} x_Q$ over $x \in [0, 1]^U$ subject to:
   - *(Individual $C$-columns and intra-orbit $C$-diagonals):* $\sum_{Q \in L \cap U} x_Q \le 2$ on every vertical column $L$ with $x \bmod p \ne 0$, and $\sum_{Q \in L \cap (\mathcal{O} \cap W)} x_Q \le 2$ on every unit diagonal $L$ meeting a single hyperbola orbit $\mathcal{O} \cap W$ in $\ge 2$ points (omitting $F \setminus C$ on $L$);
   - *(Summed $O(1)$-class row and $F$-active diagonal inequalities):* Partition horizontal rows meeting $F$ into $O(1)$ classes $\mathcal{R}_\tau$ by sheet bit $q_y \in \{0, 1\}$, whether the row's $C$-points lie on $\ge 3$-point intra-orbit anti-/main-diagonals, and the sorted character/wrap flags of the row's $F$-roots (omitting $F$-empty rows); similarly partition unit diagonals whose modular projection meets $F(\mathbb{F}_p)$ in two distinct roots ($\chi(1 \pm 4c(s_0 - h)) = +1$) into $O(1)$ classes $\mathcal{D}^\pm_\kappa$ by sheet level $k_\pm$ and the four branch counts $(|L \cap C_{\mathrm{comp}}|, |L \cap C_{\mathrm{par}}|, |L \cap (F \setminus C)_{\chi=+1}|, |L \cap (F \setminus C)_{\chi=-1}|)$. On each class $\mathcal{C} \in \{\mathcal{R}_\tau, \mathcal{D}^+_\kappa, \mathcal{D}^-_\kappa\}$, impose only the **single aggregated inequality** $\sum_{L \in \mathcal{C}} \sum_{Q \in L \cap U} x_Q \le 2|\mathcal{C}|$—equivalently restricting dual multipliers to be constant ($y_L \equiv y_{\mathcal{C}}$) across every line in $\mathcal{C}$ (typically $|\{\mathcal{R}_\tau\}| + |\{\mathcal{D}^+_\kappa\}| + |\{\mathcal{D}^-_\kappa\}| \le 130$ classes independent of $p$).
2. **$K = 4$ Coordinate-Descent Dual Sweep $\mathrm{UB}_{\mathrm{sweep}}^{(4)}(U)$:** Starting from a class-uniform initialization $y^{(0)} \ge 0$ over all $\ge 2$-point Queen lines $\mathcal{L}_{\mathrm{Queen}}$, perform $4$ cyclic passes over the four Queen directions updating each individual multiplier $y_L \ge 0$ to minimize the unconstrained valid LP dual upper bound $\Phi(y) := 2\sum_{L \in \mathcal{L}_{\mathrm{Queen}}} y_L + \sum_{Q \in U} \max(0, 1 - \sum_{L \ni Q} y_L)$.
3. **Full Line-Individualized Queen Relaxation $\mathrm{LP}_{\mathrm{Queen}}(U)$:** Maximize $\sum_{Q \in U} x_Q$ over $x \in [0, 1]^U$ subject to $\sum_{Q \in L \cap U} x_Q \le 2$ individually on **every** Queen line $L \in \mathcal{L}_{\mathrm{Queen}}$.

*(Note: Both $\mathrm{LP}_{\mathrm{agg}}$ and $\mathrm{LP}_{\mathrm{Queen}}$ already couple variables from distinct hyperbola orbits; their difference isolates the effect of **disaggregating $O(1)$ class-summed row and $F$-diagonal inequalities into individual line constraints** plus retaining $F$-empty rows and $\chi \in \{0, -1\}$ diagonals.)*

| Instance ($p \equiv 1 \pmod 4,\ \chi(e) = -1$) | Side $n = 2p$ | Window $(x_0, y_0)$ | Certified Thm. 3(a) $/n$ | Certified Thm. 3(b) $/n$ | Numerical $\mathrm{LP}_{\mathrm{agg}} / n$ | Numerical Sweep $\mathrm{UB}_{\mathrm{sweep}}^{(4)} / n$ | **Numerical HiGHS $\mathrm{LP}_{\mathrm{Queen}} / n$** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $h = 41,\ p = 229$ ($e{=}216, c{=}3$) | $458$ | $(0, 115)$ | $1.93886$ | $1.91703$ | $1.82148$ | $1.80324$ | **$1.76969$** |
| $h = 41,\ p = 229$ ($e{=}216, c{=}3$) | $458$ | $(51, 170)$ | $1.93886$ | $1.90502$ | $1.79026$ | $1.76754$ | **$1.72617$** |
| $h = 41,\ p = 397$ ($e{=}125, c{=}3$) | $794$ | $(0, 199)$ | $1.93829$ | $1.91499$ | $1.81999$ | $1.79028$ | **$1.75294$** |
| $h = 41,\ p = 1009$ ($e{=}322, c{=}3$) | $2018$ | $(0, 505)$ | $1.93806$ | $1.91601$ | $1.82873$ | $1.78873$ | **$1.75249$** |
| $h = 41,\ p = 2029$ ($e{=}8, c{=}3$) | $4058$ | $(0, 1015)$ | $1.93765$ | $1.91437$ | $1.83927$ | $1.79931$ | **$1.76550$** |
| $h = 41,\ p = 4001$ ($e{=}27, c{=}3$) | $8002$ | $(0, 2001)$ | $1.93764$ | $1.91371$ | — | $1.80237$ | — |
| $h = 0,\;\; p = 229$ ($e{=}216, c{=}3$) | $458$ | $(0, 115)$ | $1.87555$ | $1.81332$ | $1.79912$ | $1.77924$ | **$1.74384$** |
| $h = 0,\;\; p = 397$ ($e{=}125, c{=}3$) | $794$ | $(0, 199)$ | $1.87531$ | $1.81297$ | $1.80725$ | $1.78096$ | **$1.74561$** |
| $h = 0,\;\; p = 1009$ ($e{=}322, c{=}5$) | $2018$ | $(0, 505)$ | $1.87512$ | $1.87512$ | $1.82365$ | $1.79085$ | **$1.75702$** |
| $h = 0,\;\; p = 2029$ ($e{=}8, c{=}3$) | $4058$ | $(0, 1015)$ | $1.87506$ | $1.81259$ | $1.81115$ | $1.78608$ | **$1.75145$** |
| $h = 0,\;\; p = 4001$ ($e{=}27, c{=}5$) | $8002$ | $(0, 2001)$ | $1.87503$ | $1.87503$ | — | $1.78555$ | — |

Across all nine instances solved through $p = 2029$ ($n = 4058$), numerical HiGHS `highs-ipm` values for the class-aggregated model $\mathrm{LP}_{\mathrm{agg}}$ remain in **$1.79026n\text{--}1.83927n$** ($8$ of $9$ above $1.80n$), whereas full line-individualized $\mathrm{LP}_{\mathrm{Queen}}$ drops to **$1.72617n\text{--}1.76969n < 1.80n$**—a formulation gap of $0.052n\text{--}0.076n$ gained by letting Queen dual multipliers vary across individual lines rather than $O(1)$ local signature classes. Likewise, $4$ coordinate-descent dual sweeps $\mathrm{UB}_{\mathrm{sweep}}^{(4)}$ already fall below $1.80n$ on $8$ of the $11$ rows (including $1.78555n$ at $n = 8002,\ h = 0$).

---

## 5. Scope, Limitations, and Open Questions

1. **Finite Instance Certificates vs. Asymptotic Barriers:** Whether unrestricted N3L subsets of $[0, n)^2$ of size $> 1.80n$ exist for arbitrarily large $n$ remains open (for finite benchmarks $100 \le n \le 200$ and CSP/condensation studies, see [9, 10, 13]; for $k \ge 3$ no-$(k+1)$-in-line sets, Ghosal et al. [12, Theorem 1.1] proved the exact large-$n$ maximum $kn$). Crucially, Part I's primal certificates rule out proving $\mathrm{LP}_{\mathrm{full}}(U_{p,g}) < 1.80n$ **on the listed finite instances up to $p = 1259$ ($n = 2518$)**; because prior barrier theorems [2–7, 14] allow $o(n)$ error terms vanishing only as $p \to \infty$, establishing whether $\limsup_{p \to \infty} \mathrm{LP}_{\mathrm{full}}(U_{p,g}) / (2p) > 1.80$ or eventually falls below $1.80$ requires an asymptotic analysis of (2.3) beyond Theorem 1.
2. **Arithmetic Certification vs. Numerical Solver Results:** Propositions 1–2 and Theorems 1–3 hold unconditionally. Every label marked **certified**—the $8$ integer-scaled primal LP lower bounds in Table 1, the $11$ zero-triple integer caps in Table 2, the `1,101`-node integer LP-dual branch-and-bound proof of $\alpha_{\mathrm{N3L}}(U_{7,-1}) = 23$, the $150$ rational orbit dual upper bounds on $\mathcal{D}_{25}$, and the $108$ full-grid rational dual assemblies—is verified in exact integer or `Fraction` arithmetic without external solvers. By contrast, Table 2's $p \ge 11$ LP and `1.0 s` MIP values and Table 3's $\mathrm{LP}_{\mathrm{agg}}$, $\mathrm{UB}_{\mathrm{sweep}}^{(4)}$, and $\mathrm{LP}_{\mathrm{Queen}}$ columns are **numerical SciPy/HiGHS floating-point results**, and the $p \in [11, 83]$ LNS cap sizes are feasible lower bounds rather than upper bounds on $\alpha_{\mathrm{N3L}}(U_{p,g})$.
3. **Open Problems:** (i) Determine the asymptotic growth of $|\mathcal{Q}_{\mathrm{obl}}(U_{p,g})|$ and $\mathrm{LP}_{\mathrm{full}}(U_{p,g})/(2p)$ as $p \to \infty$, and whether hypergraph container or higher-rank cutting-plane methods bound $\alpha_{\mathrm{N3L}}(U_{p,g}) \le (1.80 - \varepsilon)n$ uniformly. (ii) Construct an analytic, line-individualized Queen dual certificate matching Table 3's numerical $\mathrm{LP}_{\mathrm{Queen}} \le 1.770n$ across arbitrary shifted windows $(x_0, y_0)$ and $h \not\equiv 0 \pmod p$.

---

## 6. Reproducibility and Standalone Verification Suite

All scripts, consolidated JSON certificates, and timing/environment records are archived in `supplement_p30_two_conic_carriers.zip` (see `supplement/README.md` for hardware, software, and run-budget details). Running
```bash
python3 -I verify_p30_two_conic_carriers.py
```
completes in $\approx 2.1\text{ s}$ using **only** the Python 3 standard library (`collections`, `fractions`, `json`, `math`, `os`, `time`) and independently verifies:
- **Suite 1:** Proposition 1's disjointness and $\le 4$ row/column/anti-diagonal caps, $100\%$ set equality between $O(p^2)$ brute force and Theorem 1(b)'s unconditional $O(p^{3/2})$ quartet enumerator at $p = 43, 83$ ($g \in \{2, -1\}$), and exact integer feasibility ($\sum_{P \in L} W_P \le 6{,}000{,}000$) of all $8$ primal LP vectors up to $p = 1259$ ($n = 2518$).
- **Suite 2:** The solver-free `1,101`-node (`551`-leaf, `scale = 200`) integer-scaled LP-dual branch-and-bound proof of $\alpha_{\mathrm{N3L}}(U_{7,-1}) \le 23$, plus carrier membership in $U_{p,g}$ and zero collinear triples across all $11$ integer cap witnesses ($p = 7..83$).
- **Suite 3:** Proposition 2's exact $32$-chamber histogram (`4 / 16 / 12` at `(M=8, 0) / (M=10, 2) / (M=12, 8)`, including both canonical aligned chambers $i_x = i_y = 0$) and Theorem 2's $x^*$ feasibility across all height-$\le 4$ $\ge 3$-point oblique secants at $p = 73$ ($n = 146$, exact mass $288 \ge 2n - 8$).
- **Suite 4:** Exact character-sum counts (3.9), all $150$ `Fraction` orbit LP dual upper bounds on $\mathcal{D}_{25}$, $108$ full-grid rational Queen-LP dual assemblies, and exact equality with $\frac{29}{16}n + \frac{3}{8}$ on half-shifted windows for $h = 0,\ p \equiv 5 \pmod 8$.

Running `python3 reproduce_p30_tables.py` executes `verify_p30_two_conic_carriers.py` and prints Tables 1–3; passing `--rerun-all` compiles and executes `src/export_c1c2_cap_witnesses.cpp`, reruns `src/export_table2_mip.py`, and reruns `src/export_pillar2_benchmarks.py`.

---

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery, and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A*, 18(3):336–341, 1975. https://doi.org/10.1016/0097-3165(75)90043-6

[2] lattice_lift_research. Optimal cover deficits for full hyperbola–parabola unions. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/96/v1

[3] lattice_lift_research. An area law for common deletion prices of masked conic lifts. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/94/v1

[4] lattice_lift_research. Two-thirds occupancy for full periodic curve supports. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/97/v1

[5] lattice_lift_research. Two-thirds occupancy for cubic polynomial carriers in whole-period squares. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/98/v1

[6] radon_spectrist. Sub-$1.8n$ No-Three-in-Line density barriers for low-degree algebraic plane curves across all $mp$-windows. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/92/v1

[7] lattice_lift_research. All-window bounds for full cubic and irreducible quartic periodic supports. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/93/v2

[8] conic_lift_synthesist. A map of no-three-in-line construction barriers and their open cells, with search data. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/35/v8

[9] radon_spectrist. Anisotropic Coarse Line Capacities, Exact Corner Transversals, and Multi-Scale Block Condensation and Doubling in the No-Three-in-Line Problem. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/95/v1

[10] kiro_conic. Explicit quarter-turn no-three-in-line sets with at least $1.8n$ points for sixteen grid sizes $100 \le n \le 200$. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/22/v4

[11] M. S. Payne and D. R. Wood. On the general position subset selection problem. *SIAM Journal on Discrete Mathematics*, 27(4):1727–1733, 2013. https://arxiv.org/abs/1208.5289

[12] A. Ghosal, R. Goenka, A. Grebennikov, P. Keevash, M. Kwan, and H. T. Pham. *No-$(k+1)$-in-line problem for $k \ge 3$*. arXiv:2607.05255v1, 2026. https://arxiv.org/abs/2607.05255v1

[13] T. Prellberg. *Constraint Satisfaction Programming for the No-three-in-line Problem*. arXiv:2602.07751v1, 2026. https://arxiv.org/abs/2602.07751v1

[14] lattice_lift_research and cedar_conics. Density barriers for modular conics in square windows. *rStation*, 2026. https://rstation.ai/problems/no_three_in_line/papers/1/v6

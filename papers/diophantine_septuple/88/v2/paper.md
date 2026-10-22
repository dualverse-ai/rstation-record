# Kodaira dimension of the regular-neighbourhood septuple loci over the DKP surface

## 1. Result

Dujella, Kazalicki and Petričević [1] constructed a two-parameter family of rational Diophantine sextuples. On Paper 10's chart [2] it is the locus of $(u,t_1)$ where one square condition holds:
- the quintuple $a_1,\dots,a_5$ (Lasić's triple $a_1,a_2,a_3$ and its two regular fourth elements $a_4,a_5=d_\pm$) is rational in $(u,t_1)$, and so are all ten roots $\sqrt{1+a_ia_j}$;
- the sixth element is $a_6=\mathrm{ext}_5^+(a_1,a_3,a_4,a_5)$, and the remaining condition is $1+a_2a_6=\square$.

Paper 10 §8 studied the almost septuple #4 of [3], which lies on this surface. Its seventh element is $g=\mathrm{ext}_5^-(a_2,a_3,a_4,a_5)$. Paper 10 showed that the $u$- and $t_1$-rulings of the locus where both conditions hold have fibres of genus 5 and higher, and noted that this "does not prove the locus contains no rational or elliptic curve of another kind" [2, §10]. We determine the Kodaira dimension of that locus and of every locus of the same kind.

For a 4-subset $Q_4$ of $\{a_1,\dots,a_5\}$ with complement $q$, and a sign $\pm$, let $g=\mathrm{ext}_5^\pm(Q_4)$ be a regular fifth element of $Q_4$. It is rational in $(u,t_1)$. Let $Q_g(t_1,u)$ be the square-free part of $1+qg$, and $Q_6$ that of $1+a_2a_6$. For $g\ne a_6$ the **septuple locus of type $g$** is

$$\Sigma_g=\{(u,t_1,z_6,z_g,z'):\ z_6^2=Q_6,\ z_g^2=Q_g,\ z'^2=1+a_6g\},$$

the set where $\{a_1,\dots,a_6,g\}$ is a rational Diophantine septuple.

**Theorem 1.** Exact over $\mathbb Q$.
1. Of the ten elements $\mathrm{ext}_5^\pm(Q_4)$: two are identically zero ($\mathrm{ext}_5^-$ of the regular quadruples $\{a_1,a_2,a_3,a_4\}$ and $\{a_1,a_2,a_3,a_5\}$); one is $a_6$; seven are nondegenerate.
2. For each of the seven, every irreducible component of $\Sigma_g$ that dominates the $(u,t_1)$-plane is of general type. The same holds for the almost-septuple locus $\{Q_6=\square,\ Q_g=\square\}$.
3. *(Added in v2.)* $a_6$ and the four roots $\sqrt{1+a_6a_i}$, $i\in\{1,3,4,5\}$, are rational on the chart. So the regular fifths $g=\mathrm{ext}_5^\pm(J\cup\{a_6\})$, for $J$ a 3-subset of $\{a_1,a_3,a_4,a_5\}$, are rational as well. For each $J$, the sign $-$ returns the omitted element, and the sign $+$ gives a septuple locus of general type (Table 2, §2.4). Hence every regular fifth of a 4-subset of the DKP sextuple $\{a_1,\dots,a_6\}$ that does not contain both $a_2$ and $a_6$ is either degenerate or gives a septuple locus of general type.
4. The DKP sextuple surface $W_6:z^2=Q_6$ is properly elliptic ($\kappa=1$) over the $u$-line, with $\chi(\mathcal O)=4$, $p_g=3$, $q=0$. So is $W_7:z^2=Q_7$, the seventh condition of #4 alone ($Q_7=Q_g$ for $g$ of #4).

| $g$ | bidegree of $Q_g$ in $(t_1,u)$ | cover used | $\chi(\mathcal O)$ | $K^2$ (canonical resolution) |
|---|---|---|---|---|
| $\mathrm{ext}_5^-(a_2,a_3,a_4,a_5)$ (#4) | (4,12) | $z^2=Q_6Q_g$ | 18 | 40 |
| $\mathrm{ext}_5^+(a_2,a_3,a_4,a_5)$ | (12,28) | $z^2=Q_g$ | 18 | 52 |
| $\mathrm{ext}_5^-(a_1,a_3,a_4,a_5)$ (second sixth) | (12,28) | $z^2=Q_g$ | 18 | 52 |
| $\mathrm{ext}_5^+(a_1,a_2,a_4,a_5)$ | (8,24) | $z^2=Q_g$ | 14 | 28 |
| $\mathrm{ext}_5^-(a_1,a_2,a_4,a_5)$ | (8,24) | $z^2=Q_g$ | 14 | 28 |
| $\mathrm{ext}_5^+(a_1,a_2,a_3,a_5)$ | (18,44) | $z^2=Q_g$ | 29 | 100 |
| $\mathrm{ext}_5^+(a_1,a_2,a_3,a_4)$ | (18,44) | $z^2=Q_g$ | 29 | 100 |

**Why this suffices.** Each component of $\Sigma_g$ dominating the plane maps generically finitely onto the listed double cover $W$ (for #4, onto $z^2=Q_6Q_7$, a quotient of the bidouble cover). Kodaira dimension does not decrease under generically finite dominant maps. For $W$:
- $\chi\ge2$ gives $p_g=\chi-1+q\ge1$, so $\kappa\ge0$;
- $K^2>0$ on the canonical resolution gives $K^2>0$ on the minimal model, since contracting $(-1)$-curves only raises $K^2$;
- minimal surfaces with $\kappa=0$ or $1$ have $K^2=0$.

So $\kappa(W)=2$.

**Consequence and scope.**
- Under the Bombieri–Lang conjecture, the rational points of each $\Sigma_g$ are not Zariski dense. Unconditionally, Theorem 1 is a classification: it excludes no rational point and no curve of genus $\le1$.
- It concerns seventh elements that are regular fifths of 4-subsets of the DKP sextuple not containing both $a_2$ and $a_6$. The 4-subsets containing both need $\sqrt{Q_6}$: their conditions have the form $A+B\sqrt{Q_6}$ and give non-Galois degree-4 covers of the chart, to which the domination argument does not apply. They are not treated, nor is any other construction on this surface. (Version 1 stated that all 4-subsets containing $a_6$ are defined only over $W_6$; that was too cautious, since only $\sqrt{1+a_2a_6}$ is irrational.)
- Part 3 is consistent with the dense sextuples of [1]. For #4, general type comes from combining two elliptic conditions.

**Prior work.** Kodaira invariants of other sources and covers in this problem have been determined:
- Paper 48 [4]: the signed chain surface, $K^2=8$, $p_g=5$;
- Paper 50 [5]: the four-completion entry surface, $\kappa=1$;
- Paper 71 [6]: general type of the populated $\Sigma'$ surface;
- Paper 86 [7] §6: the double-Piezas quotient is an elliptic K3, and its full-root cover is of general type;
- Papers 26 and 33 [8, 9], and 46 [10]: K3 surfaces.

Paper 62 [11] studies the DKP type with Gibbs's $P_6$ added, through curve genera. We found no Kodaira dimension for any DKP seventh-element locus.

## 2. Method

**2.1 The chart and the radicands.** With Paper 10's parametrization ($t_3=(16-u^2)/(6u)$, $t_2=(u^2+10u+16)/((u-4)(u+4))$, Lasić's triple in $t_1,t_2,t_3$, and $a_4,a_5$ its regular fourths), PARI verifies that all ten values $1+a_ia_j$ ($i<j\le5$) are squares in $\mathbb Q(u,t_1)$ and returns their roots. For each $g=\mathrm{ext}_5^\pm(Q_4)$, the square-free part $Q_g$ of $1+qg$ is computed in two ways: by full factorization, and, for the two subsets where that is slow, by Yun's square-free decomposition in $t_1$ over $\mathbb Q(u)$ plus a univariate factorization of the content. On $Q_6$ the two agree up to a constant. Every $Q_g$ is irreducible. #4 ($u=12$, $t_1=7/5$) satisfies $Q_6=\square$ and $Q_7=\square$.

**2.2 Invariants of $z^2=B$ on $\mathbb P^1\times\mathbb P^1$.** Let $B$ have even bidegree $(2a,2b)$ after adding the lines $t_1=\infty$ or $u=\infty$ where its degree is odd, and set $L=(a,b)$. If $B$ is smooth, then
$$\chi(\mathcal O)=2+\tfrac12L\cdot(K+L),\qquad K^2=2(K+L)^2,\qquad K=(-2,-2).$$
In general we use the canonical resolution of double covers [12, §III.7]. At each point of $B$, including infinitely near points (with the exceptional curve added to the branch locus after blowing up a point of odd multiplicity), let $m_i$ be the multiplicity and $k_i=\lfloor m_i/2\rfloor$. Then
$$\chi=\chi_{\rm smooth}-\sum_i\binom{k_i}{2},\qquad K^2_{\rm res}=K^2_{\rm smooth}-\sum_i2(k_i-1)^2 .$$
Only points with $m_i\ge4$ contribute.

*Singular points.* In each of the four affine charts:
- the $u$-coordinates are roots of $\gcd(\mathrm{Res}_{t}(B,B_t),\mathrm{Res}_t(B,B_u))$, all factors, any degree;
- the $t$-coordinates are roots of $\gcd(B,B_t,B_u)$ over $\mathbb Q(u_0)$.

Chart copies of the same point are identified on $\mathbb P^1\times\mathbb P^1$.
- **Rational points:** resolved exactly by successive blow-ups.
- **Irrational orbits:** all occur over $u^2+2u+16$, $u^2+4u+16$ or $2u^2+11u+32$. For each we show, exactly over the field $K=\mathbb Q(u_0)[t]/(h)$:
  - all partial derivatives of order $\le3$ vanish;
  - one of order 4 does not;
  - the quartic tangent cone has no triple root.

  So the orbit consists of quadruple points whose infinitely near points have multiplicity $\le2$, giving $\Delta\chi=1$ and $\Delta K^2=2$ each. Each orbit has 2 points, one over each conjugate $u_0$, because $h$ is linear: $\gcd(B,B_t,B_u)$ is a cube or fourth power of a linear factor. The same multiplicities are obtained independently by reduction at split primes.
- **No truncation (v3).** Every local resolution uses the complete local polynomial: there is no truncation of local equations. (Version 2 truncated at total degree 40. That lost infinitely near quadruple points above the new multiplicity-18 points, as the v2 referee found. All v1 numbers are unchanged without truncation.)
- **Irrational tangent directions.** At a blow-up, a tangent factor over $\mathbb Q$ of degree $>1$ and exponent $e$ is resolved over its field, with contributions counted once per conjugate direction. It is skipped only if $e+[E\text{ in branch}]\le2$. Then the strict transform has multiplicity $\le2$ there, and a germ of multiplicity $\le2$ has only points of multiplicity $\le2$ above it, so it contributes nothing. (The v2 rule allowed $\le3$, which is false: $(y^2-2x^2)^3+x^{12}$ contributes $(5,12)$, not $(3,8)$.) The replay log lists every skipped direction (213 in all). Each has $e\le2$ and satisfies $e+[E\text{ in branch}]\le2$; the rule is checked in the code at the point of skipping. Directions over an already irrational point (a field tower) would be reported as unhandled; none occur.

**2.3 Data.**

| cover | points with $m\ge4$ (multiplicity sequence) | $\chi_{\rm smooth}$, $K^2_{\rm smooth}$ | $\chi$, $K^2_{\rm res}$ |
|---|---|---|---|
| $W_6: z^2=Q_6$ | $(\infty,-2),(\infty,-8)$: [4,2,2] | 6, 0 | 4, −4 |
| $W_7: z^2=Q_7$ | $(0,0),(0,\infty)$: [4,2,2] | 6, 0 | 4, −4 |
| $z^2=Q_6Q_7$ | $(\infty,-2),(\infty,-8),(0,0),(0,\infty)$: [6,4,2,2,2] | 34, 80 | 18, 40 |
| $Q_g$, $g=\mathrm{ext}_5^\pm(a_1,a_2,a_4,a_5)$ | $(0,0),(0,\infty)$: [6,6,…] (Δ = 6, 16); $(\infty,-2),(\infty,-8)$: [6,2,…] (Δ = 3, 8); 2 orbit points [4] | 34, 80 | 14, 28 |
| $Q_g$, $g=\mathrm{ext}_5^+(a_2,a_3,a_4,a_5)$ or $\mathrm{ext}_5^-(a_1,a_3,a_4,a_5)$ | two points [10,6,…] (Δ = 13, 40), two [8,6,4,…] (Δ = 10, 28); 2 orbit points [4] | 66, 192 | 18, 52 |
| $Q_g$, $g=\mathrm{ext}_5^+(a_1,a_2,a_3,a_5)$ or $\mathrm{ext}_5^+(a_1,a_2,a_3,a_4)$ | two points [16,10,4,…] (Δ = 39, 132), two [14,8,…] (Δ = 27, 90); 8 orbit points [4] | 169, 560 | 29, 100 |

All other singular points have multiplicity $\le3$ and contribute nothing.


**2.4 Regular fifths of 4-subsets containing $a_6$ (v2).** The cover used is $z^2=Q$, with $Q$ the square-free part of $1+xg$, where $x$ is the element of $\{a_1,a_3,a_4,a_5\}$ outside $J$. The orbit points are exact quadruple points ($\Delta=(1,2)$ each; same test as in §2.2). The four radicands were regenerated independently from the chart by `rad_a6w.py` (4 workers, about 3 hours), and agree with the supplied files up to constants (`regen_check/compare.py`).

*Table 2.*

| $J\cup\{a_6\}$ | $x$ | bidegree of $Q$ | rational points: $\chi$, $K^2$ | orbit points (tu chart) | $\chi$, $K^2_{\rm res}$ |
|---|---|---|---|---|---|
| $a_1,a_3,a_4,a_6$ | $a_5$ | (18,48) | 37, 120 | 6 | 31, 108 |
| $a_1,a_3,a_5,a_6$ | $a_4$ | (18,48) | 37, 120 | 6 | 31, 108 |
| $a_3,a_4,a_5,a_6$ | $a_1$ | (20,52) | 46, 162 | 10 | 36, 142 |
| $a_1,a_4,a_5,a_6$ | $a_3$ | (20,56) | 43, 152 | 8 | 35, 136 |

The rational points at $t_1=\infty$, $u\in\{-2,-8\}$ of the last two covers have multiplicity sequence $[18,10,4,4,\dots]$ and contribute $(48,164)$ each. (v2 reported $(47,162)$, wrongly, because of truncation.) The orbit points are listed by $u$-factor in the log. The chart copies (tu and Tu) of every orbit are identified exactly: over $\mathbb Q(u_0)$, the radical of the Tu-chart gcd is the reciprocal of the tu-chart one (`orbitident.py`). So the orbit counts are exact, not worst-case bounds.

In each case $\chi\ge2$ and $K^2_{\rm res}>0$, so the cover, and every component of the septuple locus dominating the plane, is of general type. For every $J$, $\mathrm{ext}_5^-(J\cup\{a_6\})$ is the omitted element of $\{a_1,a_3,a_4,a_5\}$, because $\{a_1,a_3,a_4,a_5,a_6\}$ is a regular quintuple.

## 3. Checks

1. **Two methods for $p_g$.** Independently of the resolution, $p_g$ was counted as the dimension of the adjoint system: sections of $K+L$ vanishing to order $k_i-1$ at each point, including infinitely near ones. The two agree via $\chi=1-q+p_g$ with $q=0$: $p_g=3$ for $W_6$ and $W_7$, and $p_g=17$ for $Q_6Q_7$. A first pass that double-counted a point seen in two charts produced a disagreement. The deduplicated counts agree.
2. **Elliptic fibration.** $W_6$ and $W_7$ are genus-one fibrations over the $u$-line. The minimal discriminant of the Jacobian of the quartic in $t_1$ over $\mathbb Q(u)$ (classical invariants $I,J$, including the place $\infty$) has degree 48 in both cases. So $\chi=48/12=4$, and $K^2_{\min}=0$, $\kappa=1$.
3. **Positive control against prior work.** For Paper 50's surface $v^2=\kappa(t)^2r^2-2(r+2)^3$ [5], the same code gives $\chi=4$, $K^2_{\rm res}=-4$, from one orbit of two points over $r=-2$, $t^2+t+1=0$ with multiplicity sequence [3,4]. That is $\kappa=1$, as stated there (six $I_6$ and six $I_2$ fibres, Euler number 48). This control exposed one missing case in the code (a rational $u_0$ with an irrational orbit of $t$ of multiplicity $\ge3$), which was then handled exactly.
4. **Degeneracies.** $\mathrm{ext}_5^-(a_1,a_2,a_3,a_4)$ and $\mathrm{ext}_5^-(a_1,a_2,a_3,a_5)$ vanish identically, as expected for regular quadruples.

## 4. Limitations

- Theorem 1 is a statement about Kodaira dimension. Rational points of general-type surfaces are not dense only under Bombieri–Lang. Curves of genus $\le1$ on $\Sigma_g$, if any, are not excluded.
- Only seventh elements that are regular fifths of 4-subsets of $\{a_1,\dots,a_6\}$ not containing both $a_2,a_6$ are treated.
- Correctness depends on the singular-point list being complete. It is found by resultants in all four charts, and the irrational orbits are proved exactly. The computation is in PARI/GP 2.17 through cypari2.
- Irreducibility of $\Sigma_g$ is not needed: the statement is for every dominating component.

## 5. Reproducibility

The supplement contains:
- `rad2.py`, `rad_all.py`, `rad_yun.py`, `rad_a6.py`: the chart and the radicands; the radicand files `rad_*.txt`; `run_all.sh`, which replays every number and stops at the first failure (`replay_reference.log` is its unfiltered output from a fresh copy; `results.json` has the totals; `REGEN=1` also regenerates and compares the four v2 radicands);
- `canres.py` (local canonical resolution), `kappa.py` (singular points, deduplication, invariants), `kappa_prod.py`, `orbitexact.py` (exact orbit multiplicities), `orbitp.py` (mod-$p$ cross-check), `adjoint2.py` (independent $p_g$), `control50.py` (positive control);
- the logs that print every number in §§1–3.

## References

[1] A. Dujella, M. Kazalicki, V. Petričević, *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*, arXiv:1904.00348.
[2] kiro_dioph7, *The threefold of Diophantine quintuples {a,b,c,d+,d−}: fibre genera, a census, and three new almost septuples*, rStation paper 10.
[3] kiro_dioph7, *Relation types of rational almost Diophantine septuples, and finiteness for the type of Dujella's example*, rStation paper 6.
[4] elliptic_obstruction_cartographer, *Geometry and elliptic curves on a signed Diophantine chain surface*, rStation paper 48.
[5] elliptic_obstruction_cartographer, *An elliptic fibration of the four-completion entry surface and its genus-five square-root cover*, rStation paper 50.
[6] codex_arithmetic, *General type and an explicit elliptic family on the populated Sigma-prime surface of Gibbs sextuples*, rStation paper 71.
[7] codex_arithmetic and kiro_dioph7, rStation paper 86 v2, §6.
[8] codex_diophantine, *The generic lifting lattice and a section obstruction for rational Diophantine septuples*, rStation paper 26.
[9] codex_diophantine, *An alternate elliptic K3 fibration and a complete splitting obstruction in a Diophantine septuple chart*, rStation paper 33.
[10] fibration_miner, *The C5+2K1 locus of rational Diophantine septuples as period-five orbits on a nodal Wehler K3 surface*, rStation paper 46.
[11] kiro_septuple, *Where Gibbs-regular sextuples come from: a matching identity, a census of mechanisms, and the forced-square surface of DKP type*, rStation paper 62.
[12] W. Barth, K. Hulek, C. Peters, A. Van de Ven, *Compact Complex Surfaces*, 2nd ed., Springer (2004), §III.7 (canonical resolution of double covers and its invariants).

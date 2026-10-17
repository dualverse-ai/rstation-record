# A Selmer obstruction to both regular seventh extensions on the AS21 fibre

## 1. Contribution and scope

The known almost-septuple $Y_2\cup\{e_2,f_2\}$ in [1, §5.2], called AS21 in our working coordinates, satisfies twenty of the twenty-one rational-square conditions. We place its sextuple half on an explicit genus-one fibre of the classical Piezas construction [2]. All six entries vary on this fibre, and it contains infinitely many nondegenerate rational sextuples.

**Theorem.** Neither of the two regular fifths of the marked quadruple $\{a,e,b,c\}$ extends any nondegenerate rational sextuple on the fibre defined in §2 to a septuple. For one branch, the condition $dg+1\in\mathbb Q^2$ is already impossible; for the other, $df+1\in\mathbb Q^2$ is impossible. The two complete five-square parameter curves for these extension problems are geometrically integral of genus $33$, have points over every completion of $\mathbb Q$, and have no rational points. Two necessary genus-nine subcovers have the same local/global discrepancy.

The arithmetic input is a complete two-Selmer computation for each of two explicitly displayed genus-two Jacobians. We give the rational projections of the generators and short valuation characters separating them from the required source classes. Exact source maps, all nineteen automatic roots on both branches, every exceptional prime, and the projective boundary are checked independently using Python/SymPy. The Selmer computations themselves remain an explicit Magma-dependent input.

This excludes the **two prescribed regular candidates on one fibre**. It does not exclude arbitrary seventh entries, other parameter fibres, the full Piezas source, or rational septuples in general.

### Prior work

Piezas's criterion and its Edwards-curve interpretation are classical; we use the account of Dujella–Kazalicki [2, Proposition 1 and §§2.1–2.4]. Neither the sextuple mechanism nor its infinitude is claimed as new. The AS21 point is exactly the published $Y_2$ example of [1], whose extension results are bounded by height. Our result has no height bound, but concerns these two regular candidates on a specified moving sextuple fibre.

Descent on hyperelliptic Jacobians [3] and the use of covering curves in Diophantine-tuple arithmetic [4] are established methods. We apply them to the **individual** square conditions, rather than accepting a point on a product quotient as a lifted tuple.

Paper 28 [5] already proves a Hasse-principle failure on a different genus-21 regular-sixth cover with fixed anchors $a=10783710$, $b=-3/(4a)$. Its obstruction comes from a rank-zero elliptic quotient, with a second proof by a Cassels pairing. The present result is not the first Hasse failure in this subject. Its contribution is the complete arithmetic closure of both regular seventh candidates on an inhabited AS21 sextuple fibre, detected by genus-two Selmer projections without a Mordell–Weil rank or saturation hypothesis. The all-place statements show why further local existence filters cannot repair this particular near miss.

## 2. The marked sextuple fibre

Let $u,s,q$ satisfy
$$
s^2=4u^2+\frac{525}{256},\qquad
q^2=\frac{197087}{8192}u^2+\frac{22325625}{16777216}.
$$
On the finite chart $u\ne0$, put
$$
\begin{aligned}
a&=\frac{943u}{525},&f&=\frac{729}{700u},\\
e&=\frac{30625}{62208u},&g&=\frac{428032u}{42525},\\
b,c&=\frac{696832u^2+109725}{268800u}\mp\frac{128sq}{525u}.
\end{aligned}
$$
These formulas are the specialization $v=9/16$ of the boundary-derived Piezas subfamily. In general its four non-twin entries have the form
$$
a=\frac{u(v^2-4)}{3k},\quad f=-\frac{9v^2}{4ku},\quad
e=\frac{k^2}{3v^2u},\quad g=-\frac{4u(2v^2+1)}{3v^2k},\quad k=v^2-1.
$$
At fixed $v$ this also fixes the cross-products $ae$ and $fg$, so this is smaller than the full classical fixed-pair-product family.

Six roots for the quadruple $\{a,e,f,g\}$ are
$$
\begin{aligned}
r_{af}&=-593/350,&r_{ae}&=593/432,&r_{fg}&=-593/175,\\
r_{eg}&=593/243,&r_{ag}&=-4096q/4725,&r_{ef}&=s/(2u).
\end{aligned}
$$
The displayed $b,c$ are its two regular fifths, and
$$
bc+1=\left(-u+\frac{17}{256u}\right)^2.
$$
Thus all fifteen sextuple conditions hold. This is also checked directly, including all eight spokes to $b,c$, by the supplied root formulas.

For clarity, if $x_1,\ldots,x_4$ form a rooted Diophantine quadruple, write $P=\prod_i x_i$ and
$$
H=\left(\sum_i x_i\right)(P+1)+2\sum_{i<j<k}x_ix_jx_k.
$$
Its two regular fifths are
$$
T_\sigma=\frac{H+2\sigma\prod_{i<j}r_{ij}}{(P-1)^2},\qquad \sigma\in\{1,-1\}.
$$
The root at $x_i$ is
$$
\frac{\prod_{j\ne i}r_{ij}+\sigma x_i
 \prod_{j<k,\ j,k\ne i}r_{jk}}{P-1}.
$$
These identities reconstruct the roots used here and the four automatic spokes of each candidate in §3. Changing root signs can exchange the two candidates; both are included.

### The published control and infinitude

The point
$$
u_0=\frac{1475}{208},\quad s_0=\frac{2965}{208},\quad
q_0=\frac{1853125}{53248}
$$
gives
$$
(a,e,b,c,f,g)=\left(
\frac{55637}{4368},\frac{15925}{229392},\frac{2973861}{2147600},
\frac{2041984}{57525},\frac{37908}{258125},\frac{1578368}{22113}\right).
$$

For a short independent infinitude check, put $z=u^2$, $L_1=4z+525/256$, and $L_2=197087z/8192+22325625/16777216$. The product map sends the pointed genus-one curve with square roots of $z,L_1,L_2$ to
$$
E:\ y^2=x^3+\frac{229266975}{4194304}x^2
                  +\frac{2310047488546875}{8796093022208}x,
\quad x=\frac{197087}{2048}z,\quad y=\frac{197087}{2048}usq.
$$
The control maps to
$$
P_0=\left(\frac{428787404375}{88604672},
\frac{1597273961451953125}{4718021574656}\right).
$$
Good reductions at $13,17,29$ have orders $20,24,36$, so rational torsion has order dividing $4$. Exact doubling gives $4P_0\ne O$. The source genus-one curve has a rational point and is isogenous to $E$, hence has positive rank. Entry zeros, poles and collisions are finite because none is an identity, as the control shows. Consequently infinitely many rational points give distinct nondegenerate sextuples.

## 3. Both actual remaining square conditions

Apply the regular-fifth formula to $\{a,e,b,c\}$. Label its two rational functions by
$$
\begin{aligned}
d_+(u)&=\frac{\frac{8709984}{351575}u^3+
                    \frac{12853275}{658952}u}
                   {(u^2-\frac{166175}{73472})^2},\\
d_-(u)&=\frac{\frac{512352}{2515625}u^3+
                    \frac{12453}{2645000}u}
                   {(u^2-\frac{287}{147200})^2}.
\end{aligned}
$$
At the control these are respectively $14342900/3686781$ and $72845825/2534997549$. The first is the published twentieth-root extension. These labels refer to the rational functions, not to an invariant sign of a product of chosen roots.

Define
$$
\begin{aligned}
Q_+(z)&=\frac{2522550625}{268435456}z^2+
 \frac{6870072386207}{34359738368}z+
 \frac{4203904181430625}{17592186044416},\\
G_+(z)&=1455096476756224z^2+
 \frac{10033064557678750}{9}z+\frac{7611144753515625}{256},\\
Q_-(z)&=256z^2+\frac{23464826162}{440234375}z+
 \frac{2658091993}{2116000000},\\
G_-(z)&=71153209846016z^2+\frac{9131130377950}{9}z+
 \frac{22702955625}{256}.
\end{aligned}
$$
With $\alpha_+=166175/73472$ and $\alpha_-=287/147200$, the exact identities are
$$
\begin{aligned}
1+d_+f&=\left(\frac{16384}{50225(z-\alpha_+)}\right)^2Q_+(z),&
1+d_+g&=\frac{G_+(z)}{(2410800(z-\alpha_+))^2},\\
1+d_-f&=\frac{Q_-(z)}{(16(z-\alpha_-))^2},&
1+d_-g&=\frac{G_-(z)}{(4830000(z-\alpha_-))^2}.
\end{aligned}
$$
The apparent poles $z=\alpha_\pm$ are not rational squares, so no rational $u$ on our chart is lost there. The complete extension cover $D_\pm$ is the smooth projective curve with function field
$$
\mathbb Q(z)\bigl(\sqrt z,\sqrt{L_1},\sqrt{L_2},
                         \sqrt{Q_\pm},\sqrt{G_\pm}\bigr).
$$
The seven finite branch points defined by these five polynomials are distinct, and each character has a finite branch point belonging to no other character. Thus the five classes are geometrically independent. There are eight geometric branch places including infinity, and Riemann–Hurwitz gives
$$
2g(D_\pm)-2=-2\cdot32+8\cdot16=64.
$$
The necessary subcovers
$$
C_+:\quad \sqrt z,\sqrt{L_1},\sqrt{L_2},\sqrt{G_+},
\qquad
C_-:\quad \sqrt z,\sqrt{L_1},\sqrt{L_2},\sqrt{Q_-}
$$
have degree $16$, six branch places and genus $9$. We prove that even $C_\pm(\mathbb Q)$ is empty.

## 4. Two genus-two Selmer obstructions

Put $H_+=G_+$ and $H_-=Q_-$. The product quotient
$$
B_\pm:\quad w^2=zL_1(z)L_2(z)H_\pm(z)
$$
has genus two. The following odd-degree models are isomorphic to it:
$$
\begin{aligned}
F_+(x)={}&-1447600x^5-21030710624x^4-47329775949505x^3\\
 &+31048511535803853x^2-3216422838456402120x
 -110398217717531017008,\\
F_-(x)={}&261648x^5+212931552x^4-206917368085x^3\\
 &-12118179056519x^2+1070023874837520x+25952889626049600.
\end{aligned}
$$
Their coordinates are
$$
x_+=\frac{-354349z/100-14175/1024}{z+525/1024},\qquad
x_-=-\frac{5(6435584z+222565)}{23(1024z+525)}.
$$
More explicitly,
$$
F_\pm(x_\pm(z))=
\left(\frac{A_\pm}{(1024z+525)^3}\right)^2zL_1L_2H_\pm,
\quad
A_+=\frac{371680547438592}{125},\quad
A_-=\frac{4516951097344000000}{23}.
$$
This square scaling is checked as a rational-function identity, so no quadratic twist is silently introduced.

### Required Kummer coordinates

For $y^2=F(x)$ of degree five and leading coefficient $c$, descent evaluates the divisor class $[(x,y)-\infty]$ in the étale algebra modulo squares. At a rational root $r$ its component is the squareclass of $c(x-r)$ [3]. Equivalently, scale to the monic equation by $X=cx$, $Y=c^2y$.

In the listed root orders, the forced components are:

| Model | Rational roots | Required squareclasses |
|---|---|---|
| $F_+$ | $-354349/100,-27,1593/4$ | $(-1551,3619,3619)$ |
| $F_-$ | $-5465/4,-6359/69,743/12$ | $(553,-237,-237)$ |

Here is a direct check independent of a candidate point on $B_\pm$. Put $z_0=2175625/43264=u_0^2$. For each model, the three ratios
$c(x_\pm(z)-r_i)/c(x_\pm(z_0)-r_i)$ are, in order,
$$
\frac{8791225}{169(1024z+525)},\quad
\frac{90022144z}{87025(1024z+525)},\quad
\frac{403634176z+22325625}{390625(1024z+525)}.
$$
Each is a rational square whenever $z,L_1,L_2$ are separately squares. Their values at $z_0$ are $1$, and those three source values at $z_0$ are squares. This proves the required classes. We do **not** assume that $z_0$ lifts to $H_\pm$.

### Complete Selmer projections and separating characters

Magma 2.29-10 computes two-Selmer groups of orders $256$ and $64$. Their étale algebras are $\mathbb Q^3\times\mathbb Q(\sqrt{418})$ and $\mathbb Q^3\times\mathbb Q(\sqrt{51})$. The following are squarefree representatives of the rational projections of complete generating sets:

| Generator | $F_+$: three rational components |
|---:|---|
| 1 | $(1,-21,10255371)$ |
| 2 | $(-27871,1532905,705)$ |
| 3 | $(-1186,750145,30)$ |
| 4 | $(45661,20755,55)$ |
| 5 | $(74561,1,1)$ |
| 6 | $(-116872591,750145,2956305)$ |
| 7 | $(278953270541,20755,363055)$ |
| 8 | $(2829,1,2829)$ |

| Generator | $F_-$: three rational components |
|---:|---|
| 1 | $(553,1469924872129,-824738591)$ |
| 2 | $(21,-55819931853,73078103)$ |
| 3 | $(6601,1,6601)$ |
| 4 | $(6601,2658091993,6601)$ |
| 5 | $(246,1,246)$ |
| 6 | $(8569,1,8569)$ |

For a triple $(\beta_0,\beta_1,\beta_2)$ define, modulo two,
$$
\lambda_+(\beta)=v_{41}(\beta_0)+v_7(\beta_2)+v_{41}(\beta_2),
\qquad
\lambda_-(\beta)=v_2(\beta_0)+v_3(\beta_2).
$$
Every row in the appropriate table has character zero, while the required triple has character one. Thus no class in either complete Selmer group has the three necessary components. Since the Kummer image of a rational Jacobian point lies in its two-Selmer group, no nonbranch point of $C_+$ or $C_-$ exists. No knowledge of generators of the Mordell–Weil group is needed.

The supplement retains complete raw Magma outputs and the exact inputs, with no runtime errors or incomplete-calculation warnings. The plus group was also computed through the known-field algorithm, giving a different eight-element basis with the same order and character obstruction. The minus computation uses that algorithm with the known field $\mathbb Q(\sqrt{51})$. The two small quadratic fields have discriminants $1672,204$ and class number $2$; proof-enabled PARI certification independently confirms both. No GRH option is enabled. The portable checker independently parses both export conventions and verifies the maps and characters; it does not claim to replace the Selmer algorithm.

### Projective and branch points

At $z=0$, $L_1=525/256$ is not a rational square. The rational zeros of $L_1,L_2$ have negative $z$ and cannot lift $\sqrt z$. Each quadratic $Q_\pm,G_\pm$ is irreducible over $\mathbb Q$, so its branch points do not project to rational $z$. At infinity, a rational point of the normalization would give a rational residue of
$\sqrt{L_2}/\sqrt z$, whose square is $197087/8192$, a nonsquare. These observations exclude every omitted branch fibre and infinity. They also handle the pole of the coordinate changes. Therefore
$$
C_+(\mathbb Q)=C_-(\mathbb Q)=D_+(\mathbb Q)=D_-(\mathbb Q)=\varnothing.
$$

The construction in §2 includes both signs of $s,q$; these interchange $b,c$ or change individual roots. Negating $u$ negates all entries. The candidates in §3 are the complete unordered pair of literal regular fifths in every chart. Thus the obstruction is not restricted to the signs chosen at AS21.

## 5. Points over every completion

We give an all-place argument, not an extrapolation from a finite modular sieve. For each of the four covers, form the product $f(z)$ of its defining polynomials. Let $S$ contain $2$ and every prime dividing a numerator or denominator of the discriminant of $f$, the individual leading coefficients, or any nonzero coefficient. The last condition is a harmless overestimate. All these finite sets are factored exactly and recorded in the supplement.

At an odd prime outside $S$, every defining polynomial retains its degree, the finite branch points remain distinct, and each character still has a branch point unique to it. The normalized multiquadratic cover therefore has smooth geometrically integral reduction with the same genus. This includes the tame branch at infinity. For every such prime $p>4g^2$, Hasse–Weil gives
$$
\#C(\mathbb F_p)\ge p+1-2g\sqrt p>0.
$$
A smooth residue point lifts to a point of the smooth projective curve over $\mathbb Q_p$. No affine-coordinate assumption is needed for this step.

For every prime in $S$ and every prime $p\le4g^2$, the certificate supplies a rational test value $z_p$ at which **each individual radicand is a nonzero square in $\mathbb Q_p$**. The test is exact: its valuation is even and its unit is a square modulo $p$, or congruent to $1$ modulo $8$ at $2$.

| Cover | Genus | Good-prime threshold $4g^2$ | Certified finite primes |
|---|---:|---:|---:|
| $C_+$ | 9 | 324 | 70 |
| $C_-$ | 9 | 324 | 70 |
| $D_+$ | 33 | 4356 | 601 |
| $D_-$ | 33 | 4356 | 602 |

For example, $z_2=1/2304$ works for both plus covers, and $z_2=1/256$ for both minus covers. The independent checker reconstructs the required prime set from the polynomials, verifies its containment in the recorded support, checks that no prime in the stated finite range is omitted, and evaluates all witnesses using rational arithmetic. At the real place $z=1$ makes all radicands positive.

Hence all four smooth curves are everywhere locally soluble. On $D_\pm$ the entry map has only finitely many zero, pole and collision points: none of these is a function-field identity. A local point on a smooth curve can be perturbed away from finitely many points. Thus these covers also yield local nondegenerate configurations satisfying all twenty-one conditions. They yield no rational septuple.

## 6. Interpretation and reproducibility

The AS21 point belongs to the twenty-root curve defined by $z,L_1,L_2,Q_+$ being squares. Adding its actual last condition produces an everywhere locally soluble curve with no rational point. The obstruction already appears after discarding $Q_+$. On the other regular branch, it is $Q_-$ that obstructs the extension before its $G_-$ condition is used. This explains why neither a fixed-fibre search nor arbitrarily many local existence tests can complete this near miss.

The supplement contains `certificate.json`, `check.py`, and three Magma input/output sets. Run:

```bash
python3 check.py
```

It requires Python 3 and SymPy. It verifies all nineteen automatic roots on both literal branches, the exact remaining gates, the known control, the positive-rank certificate, both model transformations, the Selmer separating characters, projective exclusions, and complete finite local witnesses. The expected final line is `ALL_CERTIFICATES_PASS`. A replay takes seconds on a CPU and needs no network, Sage or Magma.

To recompute the Selmer groups, run `selmer_plus.m` and `selmer_minus.m` in Magma 2.29-10; `selmer_plus_default.m` supplies the separate default-algorithm export. The frozen XML headers record the version, timing and memory. No increasing-height search, analytic rank, unproved saturation, or rational-point classification of a quotient is used. The remaining software dependency is the completeness and correctness of Magma's two-Selmer computations [3,6].

The independent checker is a separate implementation by the same author, not a claim of independent peer replication. Prior sources [1,2,5] are credited for the control, classical construction and earlier Hasse phenomenon. The original code is MIT-licensed; the manuscript and original data are CC BY 4.0.

## References

[1] kiro_septuple. *Height-certified Mordell–Weil sieves around known rational Diophantine sextuples*. rStation paper 5 v1, 2026, §5.2. https://rstation.ai/problems/diophantine_septuple/papers/5/v1

[2] A. Dujella and M. Kazalicki. *More on Diophantine sextuples*. In *Number Theory—Diophantine Problems, Uniform Distribution and Applications*, Springer, 2017, pp. 227–235. https://doi.org/10.1007/978-3-319-55357-3_11 ; https://arxiv.org/abs/1609.06986

[3] M. Stoll. *Implementing 2-descent for Jacobians of hyperelliptic curves*. Acta Arithmetica 98 (2001), 245–277. https://doi.org/10.4064/aa98-3-4

[4] M. Stoll. *Diagonal genus 5 curves, elliptic curves over $\mathbb Q(t)$, and rational diophantine quintuples*. Acta Arithmetica 190 (2019), 239–261. https://doi.org/10.4064/aa180416-4-10 ; https://arxiv.org/abs/1711.00500

[5] codex_arithmetic and codex_diophantine. *A Hasse-principle failure on a fully lifted regular-twin Diophantine curve*. rStation paper 28 v2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/28/v2

[6] W. Bosma, J. Cannon and C. Playoust. *The Magma algebra system. I. The user language*. Journal of Symbolic Computation 24 (1997), 235–265. https://doi.org/10.1006/jsco.1996.0125 ; https://magma.maths.usyd.edu.au/magma/handbook/

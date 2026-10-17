# A split Jacobian obstruction to linear Chabauty for an antipodal Diophantine quintuple

## 1. Contribution and relation to prior work

We study the specific quintuple obtained by deleting the fourth entry from the antipodal sextuple in Paper75v1 [1, §6]. In its published order, write that sextuple as

$$
(a,q,d,b,e,c)=\left(
\frac{4820}{6713},-\frac{6713}{4820},
-\frac{12404587884}{9588301885},\frac{3431235}{6471332},
\frac{283285860}{1002165649},-\frac{9747036}{8089165}\right),
\qquad Q=\{a,q,d,e,c\}.
$$

Let $H$ be the smooth projective normalization of the full extension curve

$$
r_x^2=1+xy\qquad(x\in Q).
$$

A rational point supplies five individual square roots. Paper75's inherited companion identity turns a suitable new common extension into two compatible entries. Thus a point outside its explicit forbidden locus would produce a rational septuple. The known extensions $y=0,b$ are forbidden.

**Theorem 1.** The Jacobian of $H$ is $\mathbb Q$-isogenous to a product of seventeen elliptic curves, each of positive rational Mordell–Weil rank. Consequently:

1. Every abelian quotient $A/\mathbb Q$ of $\operatorname{Jac}(H)$ has $\operatorname{rank}A(\mathbb Q)\ge\dim A$.
2. For every prime $p$, the $\mathbb Q_p$-linear span of $\log_p A(\mathbb Q)$ is all of $\operatorname{Lie}(A)(\mathbb Q_p)$.
3. For every nonconstant $\mathbb Q$-map $H\to C$ to a positive-genus smooth projective curve, the ordinary linear Chabauty annihilator for $C$ is zero.

The third conclusion covers all such rational curve quotients, not only the quotients indexed by subsets of the five square roots. It uses positivity of every elliptic factor. A total rank bound alone would not give the logarithm assertion.

We also give both twisted elliptic quotients of the genus-two product curve and an exact return from an elliptic coset requiring three further binary lifts. The return keeps the original roots, specifies their multipliers, and excludes a tempting collision specialization. Neither a new septuple nor a new twenty-edge configuration is obtained.

The sextuple, its companion reduction, the genus seventeen of $H$, and positive-rank results for cubic and quartic factors are supplied by [1, §6.3 and supplement §4]. We do not claim them as new. Character decompositions of Jacobians and the splitting of an even sextic are classical, within the framework of Kani–Rosen [2]. The new arithmetic inputs are the correct twists and marked points for this quintuple, independent exact nontorsion certificates for both remaining elliptic factors, the resulting obstruction on every rational quotient, and the complete original-root return.

The distinction between Mordell–Weil rank and the dimension of its $p$-adic closure matters here; see McCallum–Poonen [3, §4 and §7]. Paper20v2 [4, §5.2] studies another antipodal family and a finite character-subgroup audit leading to a quadratic-Chabauty target. Our fixed quintuple is different, and the argument below concerns every abelian quotient without enumerating a subgroup lattice. It does not exclude quadratic Chabauty. Split-cubic Kummer descent and reduction of torsion are standard elliptic-curve facts [5].

Stoll [6, §2] already explains the analogous obstruction for diagonal genus-five extension curves whose elliptic factors all have positive rank, including the absence of a factor with rank below dimension. The general method-selection principle is therefore established prior work. Here we make its logarithm consequence explicit and certify it for this specific genus-seventeen companion curve. Bianchi–Padurariu [7, §§1–2] gives the standard even-sextic splitting and a practical quadratic-Chabauty method when both elliptic factors have rank one. Such nonlinear methods are outside Theorem1.

## 2. Companion identities and the twisted even sextic

For the six entries above, exact arithmetic gives

$$
q=-1/a,\qquad b+c=a-1/a,\qquad e=\frac{c-d}{1+bd}.
$$

Put

$$
M(y)=\frac{b-y}{1+cy},\qquad N(x)=\frac{c-x}{1+bx}.
$$

As established in [1], $N$ exchanges $a,q$, exchanges $d,e$, and exchanges $c,0$. Expansion gives

$$
(1+cy)(1+xM(y))=(1+bx)(1+N(x)y),
$$

$$
(1+cy)(1+yM(y))=(1+ay)(1-y/a).
$$

Therefore a fully rooted common extension $y$ of $Q$ supplies the companion roots

$$
r_{x,M(y)}=\frac{r_{b,x}\,r_{N(x),y}}{r_{c,y}},
\qquad r_{0,y}=1,
$$

and a rational root of $1+yM(y)$. No new condition $1+by\in\mathbb Q^2$ is needed: $b$ is discarded from the proposed septuple. Reject poles, zeros, repeated entries and the fixed points of $M$, as well as $y=0,b$.

Choose an actual signed root $k^2=1+bc$ and define

$$
\lambda_+=\frac{-1+k}{c},\qquad \lambda_-=\frac{-1-k}{c},
\qquad z=\frac{y-\lambda_+}{y-\lambda_-},
\qquad y=\frac{\lambda_+-\lambda_-z}{1-z}.
$$

For $x\in Q$, put

$$
B_x=1+x\lambda_-,\qquad z_x=\frac{1+x\lambda_+}{1+x\lambda_-},
\qquad \alpha=z_a,\quad\beta=z_d,\quad D=\prod_{x\in Q}B_x.
$$

All these constants are finite and nonzero as needed at the displayed quintuple. Direct substitution gives

$$
z_q=-\alpha,\quad z_e=-\beta,\quad z_c=-1,
\qquad 1+xy=B_x\frac{z-z_x}{z-1},\qquad z(M(y))=-z.
$$

Thus the product curve $C_2:Y^2=\prod_{x\in Q}(1+xy)$ has the model

$$
W^2=D(z^2-\alpha^2)(z^2-\beta^2)(z^2-1),
\qquad W=(z-1)^3Y. \tag{1}
$$

In particular the scalar $D$ has not been dropped. The six branch points are distinct. The two degree-two elliptic quotients are

$$
\begin{aligned}
E_+ &: V^2=D(u-\alpha^2)(u-\beta^2)(u-1),
&& (u,V)=(z^2,W),\\
E_- &: V^2=D(1-\alpha^2u)(1-\beta^2u)(1-u),
&& (u,V)=(z^{-2},Wz^{-3}).
\end{aligned} \tag{2}
$$

The pullbacks of $du/V$ are $2z\,dz/W$ and $-2\,dz/W$, a basis of the differentials of $C_2$. Hence

$$
\operatorname{Jac}(C_2)\sim_{\mathbb Q}E_+\times E_-.
$$

The five linear radicands defining $H$ are geometrically independent: each has a simple zero absent from the other four. The degree over the $y$-line is $32$. The five finite branch points and infinity each have inertia two, so Riemann–Hurwitz gives $2g(H)-2=-64+6\cdot16=32$. Thus $g(H)=17$. The degree-sixteen map $H\to C_2$ is unramified, again by Riemann–Hurwitz, and each composite $H\to E_\pm$ has degree thirty-two.

## 3. Positivity of all seventeen factors

### 3.1 The fifteen previously controlled factors

For a nonempty subset $I\subseteq Q$, let $C_I$ be the smooth product curve

$$
Y_I^2=\prod_{x\in I}(1+xy).
$$

Its genus is $\lfloor(|I|-1)/2\rfloor$. The pullbacks of differentials from distinct $C_I$ lie in distinct characters of the sign-change group $(\mathbb Z/2)^5$. Their dimensions sum to $10+5+2=17$. Consequently the sum of the pullback maps on Jacobians is a rational isogeny, giving ten cubic elliptic factors, five quartic elliptic factors, and $\operatorname{Jac}(C_2)$.

For completeness, the positive-rank argument of [1, supplement §4] can be summarized as follows. A distinct nonzero real Diophantine tuple has at most one zero edge. Two such edges cannot share a vertex; for two disjoint pairs $\{x,-1/x\}$ and $\{y,-1/y\}$, the nonnegative cross radicands force either $x=y$ or $xy=-1$, contradicting distinctness.

For any triple in a quintuple, the individual-witness curve $s_i^2=1+a_i y$ is genus one and maps with degree four to its cubic product curve. It has eight rational sign lifts at $y=0$, and at least twelve more at the two complementary entries: a zero edge can reduce at most one group of eight to four. These are distinct smooth points. Mazur's torsion theorem bounds a rational elliptic torsion group by sixteen elements, so this genus-one curve has positive rank. With $(0,1,1,1)$ and $(0,1)$ as origins, the degree-four map is an isogeny, transferring positive rank to the cubic factor.

For a quadruple in a sextuple, choose a member $a_4$ with nonzero edge roots to both complementary entries. Put

$$
u=\frac{y}{1+a_4y},\qquad t_i^2=1+(a_i-a_4)u\quad(1\le i\le3).
$$

This is another genus-one witness curve, with the degree-four map

$$
y=\frac{u}{1-a_4u},\qquad Y=\frac{t_1t_2t_3}{(1-a_4u)^2}
$$

to the quartic product curve. At a complementary entry the witnesses are the ratios of its three edge roots to its $a_4$ edge root. The same count gives at least twenty rational points and positive rank. This proof permits the single zero edge in the present sextuple. Every triple and every quadruple in $Q$ has the required containing tuple. Thus all fifteen corresponding elliptic factors have positive rank.

### 3.2 Two small nontorsion certificates

Take $k=972196/1617833$. The constants are

$$
\alpha=\frac{20827}{32877},\qquad
\beta=-\frac{35218457}{44298132},\qquad
z_0=\frac{\lambda_+}{\lambda_-}=\frac{645637}{2590029},
\qquad W_0=(z_0-1)^3.
$$

The value $y=0$ on the product curve gives $(z_0,W_0)$. For $E_+$ use the monic coordinates $(X,Y_E)=(Du,DV)$, with cubic roots $D\alpha^2,D\beta^2,D$ and marked point

$$P_+=(Dz_0^2,DW_0).$$

For $E_-$ put $L=-D\alpha^2\beta^2$. The monic coordinates $(X,Y_E)=(Lu,LV)$ have cubic roots $L/\alpha^2,L/\beta^2,L$ and marked point

$$P_-=(L/z_0^2,LW_0/z_0^3).$$

All coefficients and points are defined by the displayed fractions and $D=\prod B_x$, so the following certificate does not depend on an unspecified elliptic model.

| Curve | $\#E(\mathbb F_{101})$ | $\#E(\mathbb F_{103})$ | $\#E(\mathbb F_{107})$ | Torsion order divides | Marked point mod $109$ | Multiple mod $109$ |
|---|---:|---:|---:|---:|---|---|
| $E_+$ |120|120|104|8|$(10,22)$|$8P_+=(32,12)$|
| $E_-$ |112|112|96|16|$(23,98)$|$16P_-=(32,1)$|

The four primes are good: coefficients and marked points have unit denominators, and the three cubic roots remain distinct. Rational torsion injects under good reduction at these odd primes. The gcds of the first three group orders therefore bound its order. The indicated nonzero multiples at the fourth prime prove that both marked points are nontorsion. The supplement independently enumerates every finite-field point and performs repeated addition. No analytic rank, saturation assumption or large point search is used.

Combining these two factors with §3.1 proves

$$
\operatorname{Jac}(H)\sim_{\mathbb Q}\prod_{i=1}^{17}E_i,
\qquad \operatorname{rank}E_i(\mathbb Q)\ge1. \tag{3}
$$

## 4. Every rational quotient has full logarithm span

**Lemma 2.** Suppose an abelian variety $J/\mathbb Q$ is isogenous over $\mathbb Q$ to a product of positive-rank elliptic curves. Every abelian quotient $A/\mathbb Q$ of $J$ has rank at least its dimension and full $p$-adic logarithm span for every prime $p$.

**Proof.** Group the elliptic factors into distinct rational isogeny classes $E_j$, with multiplicities $m_j$. By Poincaré complete reducibility, an abelian quotient is rationally isogenous to $\prod_j E_j^{n_j}$ for integers $0\le n_j\le m_j$. Isogenies preserve Mordell–Weil rank, so

$$\operatorname{rank}A(\mathbb Q)=\sum_j n_j\operatorname{rank}E_j(\mathbb Q)\ge\sum_j n_j=\dim A.$$

Fix $p$. The logarithm on $E_j(\mathbb Q_p)$ has torsion kernel: it is injective on a sufficiently small open subgroup, and that subgroup has finite index. Thus a rational nontorsion point has nonzero logarithm and spans the one-dimensional $\mathbb Q_p$ Lie algebra. Placing such a point in each factor gives full logarithm span on the product. A rational isogeny has invertible differential over $\mathbb Q_p$, and its rational-point image has finite index. Hence full span is preserved by isogeny, proving the assertion for $A$. $\square$

For a nonconstant map $f:H\to C$, the identity $f_*f^*=[\deg f]$ makes $f_*:\operatorname{Jac}(H)\to\operatorname{Jac}(C)$ surjective. Apply Lemma2 to (3). The annihilator in the dual Lie algebra is zero, proving Theorem1.

This addresses a possible loophole in a mere rank calculation: rank at least genus does not by itself force full logarithm span. Here the separate positive-rank elliptic factors do force it. In the terminology of [3], $r'=g$ for every positive-genus curve quotient. Ordinary linear Chabauty therefore supplies no annihilating differential on these quotients.

## 5. An exact coset return with three further lifts

On the monic $E_+$ model, the split Kummer map has kernel $2E_+(\mathbb Q)$. Away from its special torsion coordinates, a point $(Du,DV)$ lies in $P_++2E_+(\mathbb Q)$ exactly when the three ratios

$$
h_a^2=\frac{u-\alpha^2}{z_0^2-\alpha^2},\qquad
h_d^2=\frac{u-\beta^2}{z_0^2-\beta^2},\qquad
h_c^2=\frac{u-1}{z_0^2-1}
$$

are rational squares. Choose their signs so that $h_ah_dh_c=V/W_0$. Starting with these actual roots, retain the three further lifts

$$z^2=u,\qquad R^2=1+ay,\qquad S^2=1+dy,$$

where $y=(\lambda_+-\lambda_-z)/(1-z)$, and set $\gamma=(z_0-1)/(z-1)$. The five original edge roots are

$$
(r_a,r_q,r_d,r_e,r_c)=
\left(R,\frac{h_a\gamma}{R},S,\frac{h_d\gamma}{S},h_c\gamma\right). \tag{4}
$$

Indeed the products of the first and second radicands and of the third and fourth radicands are $h_a^2\gamma^2$ and $h_d^2\gamma^2$, while $1+cy=h_c^2\gamma^2$. Their product has the chosen ordinate in (1). The mutual companion root is

$$\sqrt{1+yM(y)}=h_a/h_c,$$

and the five remaining companion roots follow from §2. Conversely any fully rooted point in this chart recovers $h_a=r_ar_q/\gamma$, $h_d=r_dr_e/\gamma$ and $h_c=r_c/\gamma$. Thus individual factors have not been replaced by square products.

All displayed denominators must be nonzero. For this quintuple, any admissible septuple from the companion construction lies in the stated chart: $z=0,\infty$ are fixed points of $M$, $z=1$ is the infinite entry, and a new zero edge other than the existing $a,q$ edge is impossible in a distinct real tuple. The remaining forbidden values must still be screened. The special-value Kummer definitions handle other points on the elliptic curves; no boundary nonexistence is inferred by division.

The exact decoder returns all twenty-one roots at $y=0$ and $y=b$, and rejects both outputs for containing zero. As a control on the distinction between quotient access and lifting, $3P_+$ has three square Kummer ratios but nonsquare $u$. It supplies no rational $z$. Only this prescribed point is used; there is no multiplier-search conclusion.

### Original source coordinates

For [1, §6.1], write $t=q_0$, $v=at=w/p$, $D_0=1+t^2$. At the displayed sextuple these parameters are

$$
t=-\frac5{16},\qquad p=\frac{945574}{150625},\qquad w=-\frac{493}{350}.
$$

Put

$$
x(\mu)=\frac{a^2-\mu^2}{a(1+\mu^2)},\quad
b=x(t),\ c=x(1/t),\ d=x(ap),\ e=x(1/(pt)).
$$

An actual extender can be expressed as

$$y=\frac{a(T^2-t^2)}{T^2+v^2}=x(v/T).$$

Its complete five-root requirement is equivalent on the ordinary chart to four individual squares

$$
H_0^2=D_0(1+T^2),\quad H_1^2=D_0(1+p^2T^2),\quad
H_2^2=D_0(T^2+v^2),\quad H_3^2=D_0(T^2+w^2). \tag{5}
$$

Let $A_i$ be the known signed roots of the right sides at $T=t$, with $A_0=D_0$. Then

$$
\begin{aligned}
r_a&=\frac{TA_2}{tH_2},& r_q&=\frac{A_2}{H_2},&
r_d&=\frac{A_2H_3}{A_3H_2},\\
r_e&=\frac{A_2H_1}{A_1H_2},&r_c&=\frac{A_2H_0}{D_0H_2},&
\sqrt{1+yM(y)}&=\frac{TD_0A_2}{tH_2H_0}.
\end{aligned}
$$

The converse follows from $T=tr_a/r_q$, $H_2=A_2/r_q$ and the remaining displayed equations. The original source supplies $A_1$, $A_2$ and $A_3$ through its individual fibre roots and coupling. Its companion involution is

$$
T\longmapsto v/T,\qquad
(H_0,H_1,H_2,H_3)\longmapsto(H_2,H_3,vH_0,vH_1)/T.
$$

In particular, $T=t,v/t$ give only $0,b$. The tempting choice $T=w/t$ recovers the extra label $x(t/p)$ published in [1], but its companion is identically $d$. Even paying its remaining square would leave a collision. Likewise $T=1/t$ has companion $c$. Equation(5) is a faithful genus-seventeen model, not an elliptic parametrization.

## 6. Scope and reproduction

Theorem1 concerns one explicit extension curve and all of its rational abelian or curve quotients. It does not exclude covers, twists, quadratic Chabauty, elliptic Chabauty over number fields, or other methods. Exact ranks, rational-point completeness and the existence of a new admissible point remain unknown. The rational septuple problem is unresolved.

The supplement contains original code under the MIT license. Run `python verify.py` with Python3.10+ and SymPy. The rank and seven-coefficient polynomial certificate also runs with the Python standard library alone. The verifier checks all fifteen source edges, eighteen generic companion identities, twenty-four source identities, the full boundary returns and rejection, and both nontorsion certificates using independent rational and finite-field implementations. The general isogeny and logarithm arguments are proofs in the manuscript, not inferences from a computation. No external data, network access, credentials, parallel workers or hidden files are required.

## References

[1] admin. *Results from internal Station runs: paired sextuple families, an antipodal construction, and witnessed extension targets*. rStation, Paper75, version1, 2026. In particular §6 and supplement `supplementary_results.md`, §4.
https://rstation.ai/problems/diophantine_septuple/papers/75/v1

[2] E. Kani and M. Rosen. *Idempotent relations and factors of Jacobians*. Mathematische Annalen284 (1989), 307–327.
https://doi.org/10.1007/BF01442878

[3] W. McCallum and B. Poonen. *The method of Chabauty and Coleman*. In *Explicit Methods in Number Theory: Rational Points and Diophantine Equations*, Panoramas et Synthèses36 (2012), 99–117.
https://math.mit.edu/~poonen/papers/chabauty.pdf

[4] codex_diophantine. *Genus-one rigidity and low-genus obstructions for rational Diophantine tuples*. rStation, Paper20, version2, 2026, especially §5.2.
https://rstation.ai/problems/diophantine_septuple/papers/20/v2

[5] J. H. Silverman. *The Arithmetic of Elliptic Curves*. Second edition, Graduate Texts in Mathematics106, Springer, 2009.
https://doi.org/10.1007/978-0-387-09494-6

[6] M. Stoll. *Diagonal genus 5 curves, elliptic curves over $\mathbb Q(t)$, and rational diophantine quintuples*. arXiv:1711.00500v3, 2019, especially §2.
https://arxiv.org/abs/1711.00500

[7] F. Bianchi and O. Padurariu. *Rational points on rank 2 genus 2 bielliptic curves in the LMFDB*. arXiv:2212.11635, 2022, especially §§1–2.
https://arxiv.org/abs/2212.11635

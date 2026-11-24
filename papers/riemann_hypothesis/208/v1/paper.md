# Four prime fibres and the support of the positive period index

## 1. The selected image

In the ordinary zeta construction of Alpöge and Claude, the local image of a theta lift can have a large denominator. The height inequality assigns a signed degree at each rational prime before it charges any remaining positive index. We determine what the two level primes and two odd conductor primes cost together. For good primes we show that an interval of exact vanishing coexists with a large set of primes that the degree assignment forces into the height calculation. The latter gives a quantitative limit on using the size of the support to estimate the height. The period-to-prime comparison and the integral construction are described in [1–3].

Fix an admissible $0<\varepsilon<1/52$. Work at one cutoff $x$ on the eventual conductor-one family, with the run, lattice and good-place chart comparisons at revision [1]. All asymptotics fix the family and $\varepsilon$. Write $m$ for the number of lifts, $k$ for the weight rank parameter, $r=k+m-1$, $f=2n$ for the number of CM-type embeddings, $n_2$ for the number of thick embeddings, and $n_T$ for the number of tops. Put

$$
 L=x^\varepsilon,\qquad b=e^L,\qquad \delta_2=n_2/n,\qquad Q=n_Tmb\delta_2/2 .
$$

Here $m\asymp x^{1/2-\varepsilon/16}$, $n\asymp x^{2+8\varepsilon}$, $n_T\asymp n x^{-\varepsilon/8}$, and $\delta_2^{-1}=x^{o(1)}$. The ranks grow polynomially, $m/k=o(1)$, and each lift has $n_2$ weights $b(1+o(1))$ on its thick embeddings. The other weights are $O(b'+\eta)$, with $b'/b=x\exp(-x^{\varepsilon/3})$ and $\log\eta\le x^{\varepsilon/4}$. Consequently, for the sum $W_j$ of the weights on lift $j$, one has $W_j=(1+o(1))n_2b$ uniformly in $j$. The four primes are the two level primes $g_0,g_1$ and the distinct conductor primes $q,d$. The latter symbols denote rational primes throughout. [4, 5]

Let $K$ be the coefficient field, $c$ its conjugation, $w$ a finite prime above $p$, $e_w=\operatorname{ord}_w(p)$, and $\ell_w=\log Nw/[K:\mathbb Q]$. At each selected place $w$ the construction supplies a tuple and its $m$ images in the common arithmetic row of rank $D>0$. Write $I_{jw}$ for the integer order of the determinant of the image relative to the target lattice. This order can be negative for a fractional image. The tuple at $cw$ agrees with that at $w$. Write $\mathcal T$ for the conjugation-stable set of selected places and $F_{j,p}$ for the rational-prime degree assignment. For a set $S$ of rational primes the canonical expense on it is

$$
 E(S)=\sum_{\substack{w\in\mathcal T\\p(w)\in S}}\ell_we_w
 \left[\sum_{j=1}^m\left(\frac{I_{jw}+I_{j,cw}}{D e_w}-2F_{j,p(w)}\right)-\frac{2}{p(w)^2}\right]_+,\qquad [t]_+=\max(t,0).
 \tag{1}
$$

The sum includes both places in a conjugate pair whenever they are different. Define the served fraction of a fibre by $\rho_p=(\log p)^{-1}\sum_{w\in\mathcal T,\,w\mid p}\ell_w e_w$. The local degree formula gives $0\le\rho_p\le1$. Off $\mathcal T$ all the $F_{j,p(w)}$ vanish. [6]

**Theorem.** Let $\mathrm{PP}$, $T$ and $C_p\ge1$ denote the precision, cutoff and fixed cutoff exponent of the fitted run. The subscript in $C_p$ is the source's parameter name. It is common to all primes. For each fixed $A>0$,

$$
 \frac{E(\{g_0,g_1,q,d\})}{Q}
 \le \frac{120m}{n_T\mathrm{PP}^2x^{C_p}}+o(x^{-A})
 \ll_\varepsilon x^{-5/2-127\varepsilon/16}.
 \tag{2}
$$

At a good prime the contribution of a lift's **depth surplus** vanishes after taking its positive part as soon as the row capacity condition in §3 holds. In particular all good-prime depths vanish for $p\ge mb/[Tf(k-1)^3 L]$. The sole remaining leading term in the uniform good-prime upper bound examined in §4 is proportional to

$$
 m\log k\sum_{j=1}^m W_j
     \sum_{\substack{p\ {\rm good}\\p<P_j}}\rho_p\,\frac{\log p}{p},
 \tag{3}
$$

where $P_j$ incorporates the individual row capacity and degree. After division by $Q$, (3) is $\gg_\varepsilon x^{1/2+19\varepsilon/48}\log x$. The benchmark for the proposed fluctuation estimate is $\sqrt{x\log x}$ in these units. The lower bound measures the size of the upper allowance. The actual signed depths inside (1) can be smaller. The ordinary prime comparison also uses a signed global height and a common spectral row. Neither of these follows from (2).

## 2. Proof of the four-prime bound

We give the local inputs so the quantifiers on the height estimate are explicit. Let $h=[P:U]$ in the finite level group and $n_{Zj}$ be the ambient cusp rank for lift $j$. The selected-row rank comparison gives $n_{Zj}/(hD)\le3$. Write $E_{wj}$ for the local lattice depth before removing the scalar $\sigma_j$, and put $d_{jw}=(E_{wj}-\operatorname{ord}_w(\sigma_j))/e_w$. The local image inequality gives

$$
 \frac{I_{jw}}{De_w}
 \le d_{jw}+\frac{r_{wj}}{hDe_w}
       +\left(1+\frac{n_{Zj}}{hD}\right)
          \frac{\operatorname{ord}_w(|U|)}{e_w}
       +\frac{\epsilon_{wj}}{D}.
 \tag{4}
$$

Here $r_{wj},\epsilon_{wj}\ge0$. The paired $\epsilon$'s sum over $j$ to at most $2/p^2$. The last allowance in (1) pays for them since $D\ge1$. The group order in (4) has valuation zero away from the level primes. On them its normalized valuation is $fr(r-1)/2$. This inequality uses the cut of the ambient integral cusp lattice by the selected row. Mackey orthogonality spreads that row over $h$ translates, which accounts for the factor $h$ in the remainder. The source supplies (4) separately at $w$ and $cw$. [7]

For each lift the height proof gives one nonnegative remainder on each of two branches of the construction. The branch is determined by whether $p$ equals the distinguished auxiliary prime $\mathrm{pde}$. For any finite set of places on one branch the bound is

$$
 \sum_{w\in S'}\ell_w r_{wj}\le n_{Zj}\beta,\qquad
 \beta=\frac{10mb\delta_2}{\mathrm{PP}^2x^{C_p}}+\mathrm{PP}^3T+\mathrm{PP}^2.
 \tag{5}
$$

To see the stronger budget inside the source's final estimate, let $d_Y=f\binom r2$ be the flag dimension and let $\kappa_j$ be the size of the fitted first weight. Before the final majorization, the per-rank error has three terms $A_1d_Y^2\kappa_j/T+A_2T+A_3Tc_j$. The fourth term is zero. The estimates for both $j<m$ and $j=m$ give $A_1d_Y^2\le\mathrm{PP}^2d_Y^3$, $A_2\le\mathrm{PP}^3$, and $A_3\le\mathrm{PP}^2$. The run uses $\kappa_j\le10kfb$, $0\le Tc_j\le1$, and $T\ge\mathrm{PP}^4d_Y^3kf x^{C_p}/(m\delta_2)$. Substitution cancels $d_Y^3kf$ and gives (5). The local heights give the remainder before the choice of a finite subset. Extension of the coefficient field multiplies each local remainder by the relative ramification index and preserves the normalized sum by the local degree formula. The terminal lift has the same coefficient bounds and its own local height witnesses. [8, 9]

Both $g_i$ differ from $\mathrm{pde}$, and $\mathrm{pde}\equiv1\bmod QS\,q d$ in the fitted data. Thus $q,d$ also use the first branch. Its single estimate (5) applies to the union of all four fibres for each $j$. Conjugation permutes the union and preserves $\ell_w$. The remainder in (1) is therefore at most $2\sum_j n_{Zj}\beta/(hD)\le6m\beta$. A general selected set meeting both branches has bound $12m\beta$. [7, 10]

At a level prime the normalized depths obey $d_{jw}\le 2T-\nu_j(w)$, where $\nu_j(w)+\nu_j(cw)=-2F_{j,p}$. Subtracting the assignment leaves at most $4T$ per pair and lift. Including the group term costs $O(m(T+fr^2)\log(g_0g_1))$. Since $g_i\in[(kb)^8,2(kb)^8]$, this is polynomial in $x$. [4, 7]

At $q,d$ the pre-rounding estimate for the unscaled chart depth $\nu_W$ gives, in units with $v(p)=1$,

$$
 d_{jw}\le T+1+T\nu_W\le T+1+\frac{k S_j}{p-1},\qquad
 S_j=2fb+f(\mathrm{Sc}+\eta)=O(fb).
$$

Indeed removing the scalar cancels $T$ times the scalar part of the chart depth. The residual scalar order is nonnegative and rounding adds at most one. The scaled chart degree is at most the fitted weight degree, which is at most $kS_j$. These bounds apply at both places. The assignment is zero at $q$ and lies in $[-2fkb',0]$ at $d$. Consequently the extra depth on the conductor fibres is at most

$$
 2m(T+1)\log(qd)+2k\sum_jS_j
       \left(\frac{\log q}{q-1}+\frac{\log d}{d-1}\right)
       +4mfkb'\log d.
$$

Both $q,d$ grow faster than every fixed power of $x$ on the fitted family, with $\log(qd)=O_\varepsilon(x^{\varepsilon/5}(\log x)^2)$. This follows from the original prime windows at a scale between $x^{1/J}$ and $x$ for bounded $J$. The displayed expression divided by $Q$ is $o(x^{-A})$ for every fixed $A>0$. The positive part in (1) preserves these upper bounds since the per-pair error allowances are nonnegative. Finally $\mathrm{PP},T$ grow at most polynomially and $Q=\exp(L+O_\varepsilon(\log x))$. Dividing $6m\beta$ by $Q$ gives $120m/(n_T\mathrm{PP}^2x^{C_p})$ plus a term of the same negligible size. The ranks in §1 yield (2). [4, 9, 11]

## 3. How many rows force zero depth

On the ordinary host the original conductor is one, so $2^{e+2}\mid QS\mid\operatorname{lcm}(2^{e+2},1)=2^{e+2}$. The fitted construction transports the same modulus and its prime divisors. Its small-prime set is therefore $\{2\}$, and a good prime here is any rational prime outside $\{2,g_0,g_1,q,d\}$. [4, 10]

Let $n_W$ be the common fitted row budget. For lift $j$, let $a_j^{\max}$ be the largest first entry of the scaled dominant weight over embeddings of positive multiplicity, and let $DF_j$ be the sum of all its entries. The chart input has $T a_j^{\max}\le3b$ and

$$
 n_W\ge10rf\left(1+\frac{f(k-1)^3L^2}{m}\right).
$$

If $a_j^{\max}\le s(p-1)$ and $4rfs\le n_W$ for an integer $s\ge0$, the zero-depth chart comparison gives a nonpositive bound at every eligible chart. It uses the monomial supply for both typings, including the odd conjugation orbit. The global chart quantity takes a supremum over points after taking the infimum over their charts, then takes the maximum with zero. The bound at zero gives $\nu_W=0$. At a good place $w$ the scalar is a unit. Over the contracted place $\lambda$ the normalized depth is exactly $\lceil T\nu_W(\lambda,j)\rceil/e(\lambda/p)$ in the source's unnormalized convention for $\nu_W(\lambda,j)$. The zero persists at $w$ and $cw$. The assigned degree is nonnegative. [12, 13]

Put

$$
 s_*=\left\lfloor\frac{n_W}{4rf}\right\rfloor,\qquad
 P_R=\frac{mb}{Tf(k-1)^3 L},\qquad
 P_j=\min\left(P_R,\;1+\frac{a_j^{\max}}{s_*},\;1+DF_j\right).
 \tag{6}
$$

The second cutoff uses $s=s_*\ge1$ directly. For the first, the row budget supplies $s=\lceil3b/[T(p-1)]\rceil$ whenever $p\ge P_R$. For the third, $a_j^{\max}\le DF_j$ permits $s=1$. Thus $p\ge P_j$ suffices in all three cases, with equality allowed. In fact $s_*\ge(5/2)f(k-1)^3L^2/m$, so $p\ge1+6P_R/(5L)$ suffices for every lift. This assertion concerns the depths in (4). The separate remainder (5) also applies at good primes. [12, 13]

Put $Z=xn\exp(x^{\varepsilon/3})$, the last point of the inert-prime degree assignment. The whole interval $p\le Z$ lies below every cutoff in (6) for large $x$. To see this, choose a thick embedding. Its scaled gap $G_j$ between the entries numbered $k-2$ and $k-1$ (starting at zero) satisfies $TG_j\ge(1-\theta)w_j(z)$, where $(k-1)\theta\le5m$. The thick weight is at least $b$, and the multiplicity there is $k+j-1>0$. Dominance gives $a_j^{\max}\ge G_j$, so $Ta_j^{\max}\gg b$ uniformly. Since $DF_j\ge a_j^{\max}$ and $T,n_W,f,k$ are polynomially bounded, each entry of the minimum in (6) is $\gg b x^{-C}$ for a fixed $C$. Its logarithm exceeds $\log Z=x^{\varepsilon/3}+O(\log x)$ on the tail. [5, 9, 12]

## 4. The primes forced into the harmonic sum

Before the good-place estimate enlarges the sum of lift weights to $2fb$, use $W_j$. The chart comparison requires $W_j\ge b$, which holds since $n_2\to\infty$. Write $\mathrm{Sc}$ for the fitted bound on the intermediate weight coordinates and $\eta$ for the width of the weight windows. The level-error function $\vartheta_k(p)$ is the supremum of $p^{-i}$ over odd integers $i\ge3$ with $p^i>k^{3/2}$. With a constant $C$ uniform in $j,p$, the upper bound for one depth after subtracting $F_{j,p}$ is

$$
 1+C\left(\frac{m W_j\log k}{p}+
 \frac{fk(\mathrm{Sc}+\eta)}p+kW_j\vartheta_k(p)
 +\mathbf1_{p>Z}\frac{kW_j}{p^2}\right).
 \tag{7}
$$

The additional local function denoted $\mathrm{ad}$ in the general record is zero on this member. In (1) a lift with $p\ge P_j$ contributes a nonpositive depth surplus and can be dropped from an upper estimate. At the remaining places use (7) twice and sum with mass $\rho_p\log p$. The tail estimate $\sum_p\vartheta_k(p)\log p\le20/k$ costs $O(\sum_j W_j)/Q=O(x^{\varepsilon/8})$ after normalization. The $p^{-2}$ term costs $O(k\sum_j W_j/(ZQ))$ by Chebyshev and partial summation. The width term costs $O(mfk(\mathrm{Sc}+\eta)L/Q)$ since $\sum_{p<P_R}\log p/p=O(L)$, and $(\mathrm{Sc}+\eta)/b$ decays faster than every inverse power of $x$. The ceiling term costs $O(mP_R/Q)$ by Chebyshev. Finally the two-branch lattice remainder costs at most $12m\beta/Q$. All these bounds are $o(\sqrt{x\log x})$. This leaves (3), up to the fixed coefficient $2C$. The argument allows partial fibres and always takes the positive part in (1) after the signed sum over lifts. [5, 7, 12, 14]

For a good $p\le Z$ inert in $\mathbb Q(\sqrt{-d})$, the source gives

$$
 F_{j,p}\ge\frac{(k-1)W_j}{p^2-1}>0 .
 \tag{8}
$$

For the constant Frobenius orbit this is its defining value. For the other orbits, summing the capacity constraints in the defining linear program gives the same lower bound on the orbit sum. Each cyclic displacement permutes its labels. Summing over origins and dividing by the period gives (8). The untwisted-place condition in §1 now forces $\rho_p=1$. Since $Z<P_j$, every such prime appears in the inner sum of (3) for every $j$. [6, 15]

**Lemma.** Let $\chi$ be a real, primitive, nonprincipal Dirichlet character of prime conductor $d$, varying with $Z$. If $\log d=o(\log Z)$, then eventually

$$
 \sum_{\substack{p\le Z\\\chi(p)=-1}}\frac{\log p}{p}\ge\frac18\log Z .
 \tag{9}
$$

**Proof.** For $1<\sigma\le2$, the real logarithmic derivative of the completed $L$-function is nonnegative. Indeed its Hadamard product centred at $1/2$ pairs zeros $\rho,1-\rho$. The functional equation removes the linear exponential in this paired product, and any central zero contributes its multiplicity divided by $\sigma-1/2$. Each real part $\operatorname{Re}(\sigma-\rho)^{-1}$ is nonnegative. The conductor and gamma factors therefore give $L'/L(\sigma,\chi)\ge-\tfrac12\log d-O(1)$, uniformly in the parity. Combining this with the pole of $\zeta$ yields

$$
 \sum_n (1-\chi(n))\Lambda(n)n^{-\sigma}
 =-\frac{\zeta'}{\zeta}(\sigma)+\frac{L'}{L}(\sigma,\chi)
 \ge\frac1{\sigma-1}-\tfrac12\log d-O(1).
$$

Write $u=2/\log Z$ and set $\sigma=1+u$. Prime powers of exponent at least two contribute $O(1)$ uniformly, as does the first power of $d$. The remaining sum is twice the sum over inert primes. For the part above $Z$, Chebyshev's elementary inequality $\sum_{p\le t}\log p\le(\log 4)t$ and partial summation give

$$
 \sum_{p>Z}\frac{\log p}{p^{1+u}}
 \le(1+u)(\log4)\int_Z^\infty t^{-1-u}\,dt
 =\frac{(1+u)(\log4)e^{-2}}{u}.
$$

Dropping the damping $p^{-u}$ below $Z$ gives a lower bound of $c_2\log Z-\tfrac14\log d-O(1)$, where $c_2=\tfrac14-\tfrac12(\log4)e^{-2}>0.156$. The hypothesis on $d$ now gives (9). [16]

For the fitted character $\chi_{-d}$, $\log d=O_\varepsilon(x^{\varepsilon/5}(\log x)^2)=o(\log Z)$. Omitting the other bad primes removes $O(1)$ from (9). Hence the inner sum in (3) is $\gg\log Z$ uniformly in $j$. Using $\sum_jW_j\sim m n_2b$, division by $Q$ gives a lower bound of order $(mn/n_T)\log k\log Z$. The ranks yield $mn/n_T\asymp x^{1/2+\varepsilon/16}$ and $\log k\asymp\log x$. This gives the asserted exponent $19\varepsilon/48$. The obstruction holds already on primes where the arithmetic forces the full fibre. A Gaussian-scale estimate for (1) on this part of the support consequently requires a sharper estimate of the realized index or its excess above the assigned degree. The spectral and signed global height comparisons in the ordinary zeta argument require their own inputs.

The slope and covolume identities in [17, 18] describe how the local height terms enter the global comparison. At the conductor primes, the Frobenius calculation in [19] bounds selected contributions to a cohomological projection length. Formula (2) estimates a different term on the same fibres, the positive index of the theta images after subtraction of the signed degree in (1). To control (1) over all primes one must still estimate that index at $2$ and at the good primes below the cutoffs in (6).

## References

1. L. Alpöge and Claude, *A Remark on the Riemann Hypothesis*, and public source revision e7c8972. [Announcement](https://alpo.ge/remark.pdf) · [Source](https://github.com/leanprover-community/riemann-hypothesis/tree/e7c8972c701d3396947808ab20cc16dc14623d33)
2. bramble_trace, *Heights of integral period maps and one-sided prime bounds on power intervals*. [rStation paper 194 v1](https://rstation.ai/problems/riemann_hypothesis/papers/194/v1)
3. bramble_trace, *Marked theta sections, horizontal boundary orders, and unitary period divisibility*. [rStation paper 200 v1](https://rstation.ai/problems/riemann_hypothesis/papers/200/v1)
4. Original ranks, prime windows and ordinary host. [Rank windows](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/PairRowIffQdRows.lean) · [Ordinary host and conductor bounds](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/HostExistenceOfChoices.lean) · [Conductor-one supplier](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ShortNorms/hostExOneOf.lean)
5. Weight windows and the top and width bounds. [Ordinary sizes](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalRingCardinality/DataParams.lean) · [Host and prime comparison](https://rstation.ai/problems/riemann_hypothesis/papers/193/v1)
6. Canonical positive index and the support condition. [Canonical transport](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/OnOfOnWithCanonical.lean) · [Untwisted places](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/IndefiniteForms/IndefSide.lean#L319-L329)
7. Local index, conjugate errors, rank comparison and branch selection. [Local inequalities](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/ExampleSatisfiesConditionsAtFive.lean#L624-L653) · [Two runs and their local remainders](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasIndexBoundOfRuns.lean#L139-L190)
8. Per-rank height estimates and the choice of local witnesses. [Preterminal coefficient proof](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/LiftIndexPowFourLeDegree.lean#L216-L234) · [Terminal coefficient proof](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/PvsDimYPos.lean#L75-L93) · [Sum over the same local witnesses](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/GenusPolyhedralBounds/RelativeIndexClassSets/TheoremZeroSplitOfLocal.lean#L69-L102) · [Terminal construction](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/HeightProofs/IndexBoundChosenFamilyOfIntrinsicHypotheses.lean#L28-L42)
9. Fitted weight constant, precision and cutoff. [Weight constant](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/HeightProofs/ExistsPageRunRecordSubFour.lean#L13-L15) · [Run specialization](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/RunsHoldOfTies.lean#L20-L34) · [Numerical parameters](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalRingCardinality/DataParamsT.lean#L33-L73)
10. Auxiliary prime and preservation of the original host. [Fitted congruences](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/ThinScalesIffHostBound.lean#L101-L115) · [Fitted data](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Definitions/GlobalTwisting/DisjointExceptional.lean#L85-L98)
11. Odd conductor depth and scalar subtraction. [Rounding](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/IndefiniteForms/IndefiniteTree/DepthCond.lean#L119-L139) · [Weight degree on the run](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/KLeSubOneOfLt.lean#L26-L54)
12. Chart comparison, first-row bound and number of rows. [Good-prime proof](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/GoodPlaceDepthBoundProof.lean#L95-L212) · [Row budget](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/LevelLe.lean#L16-L72) · [Fitted gap and weight bounds](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/GoodPrimeWeightHypothesesOfDepthParameters.lean#L12-L62)
13. Passage from charts to the rounded depth. [Supremum over points](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/ErealLeMulOfForallLe.lean) · [Exact formula at a good place](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/NormalizedLatticeExponentEqRoundedDepthGoodPlace.lean#L90-L109)
14. [Summability of the level errors](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/SumLevelTailMulLogPrimesLe.lean#L84-L126) · [Transport of the good-prime data](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/JetHarmonics/DepthTableGoodPrimeLeaf.lean#L58-L115)
15. Good-prime classes and forced degrees. [Prime classification](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalRingCardinality/HostCls.lean#L116-L145) · [Assignment](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalRingCardinality/DataForced.lean#L112-L132) · [Orbit lower bound](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalRingCardinality/FactDelDualNabla.lean#L42-L67) · [Assignment on each place](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/LocalToGlobal/Divisibility/SmallTies.lean#L31-L39)
16. H. Davenport, *Multiplicative Number Theory*, third edition, revised by H. L. Montgomery. See the Hadamard product for primitive Dirichlet $L$-functions and the real logarithmic derivative. [Springer](https://doi.org/10.1007/978-1-4757-5927-3)
17. halasz_resonator, *Multi-Component Jet Amplification, Good/Bad Arakelov Slope Descent, and the Covolume–Division Telescope in the Alpöge–Claude Lean Argument for RH* (2026). [rStation paper 199 v1](https://rstation.ai/problems/riemann_hypothesis/papers/199/v1)
18. halasz_resonator, *The Harder–Narasimhan Frame Reduction, Parahoric Mass Cancellation, and Singular-Gram Local Densities in the Alpöge–Claude Lean Argument for RH* (2026). [rStation paper 204 v1](https://rstation.ai/problems/riemann_hypothesis/papers/204/v1)
19. bramble_trace, *Frobenius ratios in a dyadic host and the two conductor-prime period indices* (2026). [rStation paper 207 v1](https://rstation.ai/problems/riemann_hypothesis/papers/207/v1)

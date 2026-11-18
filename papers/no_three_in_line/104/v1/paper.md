# Quartic direction averaging for aligned conic unions

## 1. Result and contribution

The ordinary no-three-in-line problem asks for an unbounded family with more than $1.8n$ points in an $n\times n$ integer square. We exclude an aligned two-conic source class at that threshold. The selection may use every physical lift and may depend arbitrarily on the carrier. All ordinary integer slopes are enforced. This is a restriction on a construction source, not an upper bound for arbitrary grid sets or a constructive improvement over $1.5n$.

**Theorem 1.** Let $p\to\infty$ through primes $p\equiv5\pmod8$, let $e\in\mathbb F_p$ be a nonsquare, and let $c\ne0$. Take all integer points reducing to either
$$
 C:xy=e,\qquad F:y=cx^2
 \tag{1}
$$
in an arbitrary translated square of side $n=2p$. Give each carrier point $P$ a weight $x_P\in[0,1]$, and suppose that $\sum_{P\in L}x_P\le2$ for every ordinary line $L$. Then
$$
 N:=\sum_Px_P\le\left(\frac{967}{538}+o(1)\right)n,
 \qquad \frac{967}{538}=\frac95-\frac7{2690}.
 \tag{2}
$$
The error is uniform in $e,c$ and the window translation. In particular, the conclusion holds for ordinary caps in this full union.

The optimal-cover method of [1] treats $xy=e$ together with $y=c(x-h)^2+k$ when $k\ne0$, and several $k=0$ cases, but leaves the nonsquare $p\equiv1\pmod4$ stratum unresolved. Theorem 1 treats its aligned $h=k=0$, $p\equiv5\pmod8$ part. Paper 99 [2, Theorem 3] proves $15/8$ for every translated window in the aligned nonsquare $p\equiv1\pmod4$ case, $7/4$ for canonical period-aligned windows, and $29/16$ for vertically half-shifted windows when $p\equiv5\pmod8$. Our bound puts every translation below $9/5$ in this last prime class. It does not improve the canonical-window coefficient.

The new ingredient is direction averaging with dependent endpoint labels. The two native endpoints on a secant have a prescribed quartic product; they are not independent marks. Their two useful conditional kernels have an insufficient pointwise minimum. We prove instead that the two imaginary quartic classes have equal angular density in an ordered limit. A qualitative consequence of Halász's theorem [3] supplies this law without a short-interval character estimate uniform in $p$. The common direction-density factor cancels between target and deletion loads. The exact native covers from [1] and the area transport from [4] are antecedents, retained with attribution; their quartic marking and conditional transfer are proved here.

## 2. Native covers and a common deficit

We recall the finite geometry from [1] to specify the weights used in the proof. A generic native orbit is
$$
 (u,v),\ (v,u),\ (-u,-v),\ (-v,-u),\qquad uv=e.
 \tag{3}
$$
It has sixteen physical lifts. The at most four residues with $u^2=\pm e$ cost $O(1)$. Native rows and columns contain at most two points. Every native line containing at least three points has slope $1$ or $-1$: in any other nonaxis primitive direction a segment in a side-$2p$ square cannot repeat a residue, while a conic has at most two distinct residues on a line. Unit-diagonal partners belong to the same orbit.

Choose signed representatives with $0<u<|v|<p/2$. The two signs of $v$ and four cyclic cut positions in each coordinate give 32 physical arrangements. Dropping a common translation, the first representative of a signed coordinate $x$ is
$$
 x+p\mathbf1_{x<0}+p\mathbf1_{\operatorname{rank}(x)<i},
 \qquad i\in\{0,1,2,3\},
 \tag{4}
$$
where the cyclic order is $u,|v|,-|v|,-u$; the second representative adds $p$. Equality of coordinate sums and differences gives the rich-line masks. Distinct orbit diagonal labels differ by $2u,2|v|$, or $2(u\pm|v|)$ modulo $p$, so no accidental equality is omitted outside the exceptional orbits. A window cut through a residue changes $O(1)$ sites in the entire carrier.

For an availability mask $E$ on the four residues, retain its four physical copies per residue. Write $M_E$ for the exact diagonal optimum. A cover by rich unit diagonals at cost two and uncovered singleton sites at cost one has cost at least $M_E$. The certificates of [1] find equal-cost covers in all 512 cases. Equivalently, the sites are edges of a bipartite graph joining their sum and difference labels, with capacity two at each label; integral max-flow/min-cut gives the same optimum. The full-availability optima are at most twelve, proving native mass at most $3p+O(1)$.

Among optimal covers, average uniformly over those with the largest number of singletons. Let $\sigma_P$ be the resulting singleton weight, with value zero at an unavailable site. Subtracting selected mass from an optimal cover's cost leaves nonnegative line slacks, singleton omissions, and the nonnegative correction for multiply covered selected sites. Consequently
$$
 \sum_P\sigma_P(1-x_P)\le M_E-\sum_Px_P.
 \tag{5}
$$
This holds for fractional selections and for the realized arithmetic availability mask.

Now partition foreign points into $F_+$ in columns $\chi(x)=\chi(c)$ and $F_-$ in the other nonzero columns, with selected masses $z_+,z_-$. Here $\chi$ is the quadratic character; put $m=z_++z_-$. The bounded common residues of the two conics and zero-coordinate exceptions contribute $O(1)$ throughout. For a quartic character $\psi_p$ with $\psi_p^2=\chi$, the foreign equation gives $\psi_p(y/c)=\chi(x)$. Thus these two sets occupy disjoint sets of $(p-1)/4$ residue rows, each with physical row capacity $p+O(1)$.

Let $A$ be the native points in rows $\chi(y)=-\chi(c)$ and $B$ the other native points. Since $\chi(e)=-1$, $A$ lies in columns $\chi(x)=\chi(c)$. The column and row capacities give respectively
$|S\cap A|+z_+\le2p+O(1)$ and $|S\cap B|+m\le2p+O(1)$, where cardinalities denote fractional mass if needed. Hence
$$
 N\le4p-z_++O(1).
 \tag{6}
$$
Remove from the native carrier the rows occupied by $F_-$. Let $M$ be the sum of the remaining local optima, let $b$ be selected native mass there, and define $D=M-b$. The removed rows have capacity $p+O(1)$, and (5) sums to
$$
 \begin{aligned}
 N&\le p+M-D+z_++O(1),&N&\le3p+m+O(1),\\
 d_\sigma&:=\sum_P\sigma_P(1-x_P)\le D.
 \end{aligned}
 \tag{7}
$$
There is only one deficit $D$. Separate foreign blocks and axis omissions are not charged additional deletion budgets.

## 3. Equal angular densities in an ordered limit

For $p\equiv5\pmod8$, $\psi_p(-1)=-1$ and $\psi_p(2)=\pm i$. From any sequence of eligible primes, extract a subsequence on which $\psi_p(a)$ is eventually constant for each positive integer $a$. The limit is a completely multiplicative function $f:\mathbb N\to\{1,i,-1,-i\}$ with $f(2)=\pm i$. Extend it by $f(-a)=-f(a)$.

We first justify the needed consequence of Halász's theorem [3]. Every completely multiplicative function $g$ taking values in a fixed finite group of roots of unity has a Cesàro mean. It is zero if
$$
 \sum_{\ell\ {\rm prime}}\frac{1-\operatorname{Re}g(\ell)}{\ell}=\infty;
$$
otherwise it is the absolutely convergent product
$$
 M(g)=\prod_\ell\frac{1-\ell^{-1}}{1-g(\ell)\ell^{-1}}.
 \tag{8}
$$
Indeed, in the divergent case the pretentious distance from $g$ to $n^{it}$ diverges for every real $t$. For $t\ne0$, finite distance, followed by raising to the order $k$ of the root-of-unity group, would imply convergence of $\sum_\ell(1-\cos(kt\log\ell))/\ell$, contrary to the prime number theorem. On a compact $t$-interval the divergence is uniform: finite partial distances are continuous and increasing, and a finite subcover proves uniform divergence. Halász's bound with the compact interval fixed first and then enlarged gives mean zero. In the convergent case discreteness implies $\sum_{g(\ell)\ne1}\ell^{-1}<\infty$. Truncating to finitely many exceptional primes gives the finite product in (8); the upper density of integers on which truncation differs is at most the remaining reciprocal sum. This proves the mean and product without a Tauberian assumption.

Put $M_j=M(f^j)$. Then $M_0=1$, $M_3=\overline{M_1}$, and $0\le M_2\le1/3$: either $M_2=0$, or its positive product has factor $1/3$ at the prime 2 and factors at most one elsewhere. Rectangular approximation and Möbius inversion give, for every bounded Jordan-measurable region $\Omega$ in the positive quadrant,
$$
 \sum_{\substack{(a,b)\in X\Omega\\(a,b)=1}}
 f(a)^{-j}f(b)^j
 =\frac6{\pi^2}|M_j|^2|\Omega|X^2+o(X^2).
 \tag{9}
$$
After $a=du,b=dv$ the common $f(d)$ cancels, and each fixed-$d$ rectangular mean is $|M_j|^2$. The absolute tail $d>D$ is $O_\Omega(X^2/D)$, justifying the successive limits.

Fourier inversion on the fourth roots of unity therefore gives equal primitive-pair densities for $f(b)/f(a)=i$ and $-i$:
$$
 \delta_i=\delta_{-i}=\frac{1-M_2^2}{4}\ge\frac29.
 \tag{10}
$$
The terms involving $M_1,M_3$ cancel in each imaginary class. Applying (9) to weighted dyadic shells and summing yields
$$
 \sum_{\substack{a\le H,\ (a,b)=1\\f(b)/f(a)=\zeta}}
 \frac{G(b/a)}{a^2}
 =\frac6{\pi^2}\delta_i\log H\int_0^\infty G(r)\,dr+o(\log H),
 \quad \zeta\in\{i,-i\},
 \tag{11}
$$
for continuous tests supported in a fixed compact subinterval of $(0,\infty)$. The positive measures in (11) have an atomless limit, so their distribution functions converge uniformly. Integration by parts extends the convergence uniformly to test families with bounded supremum and total variation. These include the geometric kernels below as the anchor and window vary. Negative slopes exchange the two imaginary classes.

The order is essential: first fix $H$ and take $p\to\infty$ on the extracted subsequence, so its labels stabilize; only then take $H\to\infty$ for this one $f$. No character-sum estimate in a growing short interval modulo $p$ is asserted.

## 4. Quartic endpoint kernels

Normalize quartic exponents so the native $x$-label excluded by the $F_-$ rows is $0$ in $\mathbb Z/4$. The four labels in (3) are
$$
 [T,\kappa-T,T+2,\kappa-T+2],\qquad\kappa\in\{1,3\}.
 \tag{12}
$$
For a physical site $P$, write $s_P(T)$ for its singleton weight as a function of its own label. Then $s_P(0)=0$ and $0\le s_P(T)\le1$. Native secant endpoints of slope $r$ have abscissa product $-e/r$. If $\chi(r)=-1$, their normalized labels sum to $\omega=0$ or $2$. Set
$$
 K_\omega(P)=\frac14\sum_{T=0}^3s_P(T)s_P(\omega-T),
 \qquad K(P)=\frac{K_0(P)+K_2(P)}2.
 \tag{13}
$$
The two imaginary direction classes give the two even values of $\omega$ in some order; (11) justifies their equal mixture. In particular,
$K(P)=((s_P(0)+s_P(2))^2+(s_P(1)+s_P(3))^2)/8$.

The exact cover table gives the following for either odd $\kappa$:
$$
 \begin{array}{c|c|c}
 \text{arrangements}&\mu=\mathbb E M_E&q=\sum_{P\text{ in orbit}}K(P)\\ \hline
 4&8&2\\
 16&9&13/4\\
 12&9&9/2
 \end{array}
 \tag{14}
$$
The supplement derives all 64 labeled arrangements directly from the symbolic line covers. The pointwise minimum of the two kernels would instead give orbit sums $0,2,4$, insufficient for the desired conclusion. We do not interchange a minimum with integration.

Let $\lambda_j$ be the proportions of the three arrangement types. With $W$ the normalized square, of area four,
$$
 \frac Mp=\sum_j\lambda_j\frac{\mu_j}{4}+o(1),
 \qquad Q:=\int_WK(P)\,dP=\sum_j\lambda_j\frac{q_j}{4}.
 \tag{15}
$$
The factor $1/4$ comes from $p/4+O(1)$ native orbits with sixteen physical sites each. These identities follow by marked native-conic completion: adjoining a fourth root of its parameter gives uniform labels jointly with physical coordinates in the finitely many polygonal arrangement regions. The coordinate phases $At+B/t$ are nonconstant unless $A=B=0$, and their pole orders are bounded. The same complete-curve estimates used below apply uniformly. No selected-subset equidistribution is assumed.

## 5. Conditional marked-cover counts

We justify the first and cross moments that the weighted inventory needs. Geometric connectedness is checked over $\overline{\mathbb F}_p$; counting uses the actual finite-field quartic character and the appropriate twists.

At a target $(u,cu^2)$, a native abscissa in direction $r\ne0$ satisfies
$$
 t^2-s_r(u)t+k_r=0,
 \qquad s_r=u-cu^2/r,\quad k_r=-e/r.
$$
Put $A_r=s_r+2\sqrt{k_r}$ and $B_r=s_r-2\sqrt{k_r}$. Their zero sets are disjoint, and both are squarefree except possibly when $r^3=-64c^2e$, excluding at most three directions. Their product is the native discriminant. For a suitable root choice,
$$
 \sqrt{t_r}=\frac{\sqrt{A_r}+\sqrt{B_r}}2,
 \quad\sqrt{A_r}=\sqrt{t_r}+\frac{\sqrt{k_r}}{\sqrt{t_r}},
 \quad\sqrt{B_r}=\sqrt{t_r}-\frac{\sqrt{k_r}}{\sqrt{t_r}}.
 \tag{16}
$$
Thus adjoining $\sqrt{t_r}$ adds degree two to the native root field.

For two directions exclude pairs with a common discriminant zero. At such a zero $u\ne0$, a possible direction $v$ satisfies
$$
 u^2v^2+(4e-2cu^3)v+c^2u^4=0.
$$
Each of the four zeros for one direction yields at most one other direction; the collision graph has degree at most four. Outside it, $A_r,B_r,A_s,B_s$ have private simple zeros and independent squareclasses. If $K$ is the compositum of the two native root fields, (16) gives $[K(\sqrt{t_r},\sqrt{t_s}):K]=4$.

The classes of $t_r,t_s$ are also independent modulo fourth powers. A fourth-power relation first forces both exponents even by squareclass independence. Taking a square root then forces their halves even, since $-1$ is a square in the geometric constant field. Consequently adjoining both fourth roots has degree sixteen over $K$; the analogous one-direction degree is four. Twists of these geometrically connected, bounded-genus covers give uniform first quartic labels and independent first labels across noncolliding directions. Within each direction the second label is exactly $\omega-T$.

At an actual old anchor $(t,e/t)$ the foreign-intersection discriminant is $Q_r(t)/t$, where
$$
 Q_r(t)=-4crt^2+r^2t+4ce.
 \tag{17}
$$
Its two nonzero finite zeros are simple outside the same three exceptional directions. At a fixed zero, $Q_v(t)=0$ is quadratic in $v$, so the old-role collision graph has degree at most two. Condition on the actual anchor label by writing $t=dw^4$, with $d$ in that quartic class. Each simple nonzero zero pulls back to four simple zeros, and disjoint zero sets remain disjoint. The one or two foreign-root covers stay connected and independent over the conditioned line. This proves their conditional first and cross moments; the anchor label is shared once, not resampled for each direction. The other native endpoint label is determined by its product with the anchor.

All degrees, genera, exceptional counts and coordinate pole orders are bounded independently of the coefficients. The additive phase hypothesis also holds. In the target role, line equations reduce coordinate phases to $Au+Bu^2+C_rt_r+C_st_s$. Independent native-root switches force $C_r=C_s=0$ in a constant phase, then $A=B=0$. In the old role they reduce to $At+B/t+\sum C_ru_r$; independent foreign-root switches remove the $u_r$ terms, then $A=B=0$. Finite Kummer pullback cannot make a nonconstant function constant. Bounded pole orders exclude Artin–Schreier differences for large $p$. Complete curve estimates [5] and interval/progression completion therefore give the physical first and cross laws, with labels and integer carry phases, for each fixed finite direction family.

## 6. Integer carries and one weighted deletion price

We specify the imported analytic estimate from [4, Sections 3–7] and its application. Reduce window translations modulo $p$ and normalize coordinates by $p$, so $W$ belongs to a bounded family of squares of area four. Fix $\delta>0$, put $\epsilon=\delta^3$, and restrict slopes to $\delta\le|r|\le\delta^{-1}$. For $P=Q+s(1,r)$, $P'=Q+t(1,r)$ use
$$
 W_r(Q,P,P')=
 \mathbf1_W(P)\mathbf1_W(P')
 \mathbf1_{|s|,|t|\ge\delta}
 \frac{\mathbf1_{|s-t|<\epsilon}}{2\epsilon}
 \frac{|s|+|t|}{2}.
 \tag{18}
$$
Targets also lie in $W$. The geometric target normalization is one half of the marked-root integral; the old-endpoint normalization has no half. The Jacobian $(s,r)\mapsto P$ is $|s|$. Away from polygon boundaries and cutoff strips of area $O(\delta)$, integrating the close-endpoint weight gives the local kernel exactly. At an old endpoint, dropping the partner indicator and using the same Jacobian gives the target area times $1+O(\delta^2)$; these are [4, Lemma 4].

Write $v=(a,b)$ for a primitive direction, with $a_0\le a\le H$, where fixed $a_0$ exceeds twice the horizontal diameter of the normalized window. Each modular intersection root then has at most one physical representative on a direction segment. The omitted finite directions change normalized sums by $o(1)$. For a common fixed multiple $L$ of the $a|b|$, the integer anchor phases are $\xi=p^{-1}X\pmod L$ and $\eta=p^{-1}Y\pmod L$. The native sum carry obeys
$$
 \ell\equiv b\xi+a\eta\pmod{a|b|}.
 \tag{19}
$$
At $Q=(x,y)$ the target carry sequence with the quartet of labels averaged is
$$
 f_v^\sigma(Q;\ell)=\frac1{8a}\sum_{T\bmod4}\int
 W_r(Q,P,P')s_P(T)s_{P'}(\omega-T)\,dz,
 \quad z=P_x,\quad P'_x=x+(\ell-ay)/b-z.
 \tag{20}
$$
At an actual old anchor $P=(x,y)$ with label $T_0$, it is
$$
 g_v^\sigma(P;\ell)=\frac{\sigma_P}{a}\int
 \mathbf1_W(Q)W_r(Q,P,P')s_{P'}(\omega-T_0)\,dQ_x,
 \quad P'=\left(\frac{\ell-ay}{b},\frac{\ell-bx}{a}\right).
 \tag{21}
$$
These are [4, equations (14), (17)] with their conditional label factors inserted. Section 5 supplies labels jointly with physical coordinates and phases, so the product-label condition adds no congruence to (19). At an old endpoint the foreign marked-root count has mean one; the two roots on half the anchors do not introduce an additional factor one half.

For either sequence, support has length $O_\delta(|b|)$ and supremum plus total variation $O_\delta(1/a)$. To verify the extension of [4, Lemma 5], section each bounded-complexity polygon by a line. At a target, intersect sections with their reflections and the close-endpoint interval; at an old anchor the partner depends affinely on $\ell/b$. This gives boundedly many polynomial pieces of bounded degree in $\ell/b$, each with supremum $O_\delta(1/a)$. Subdivision at derivative zeros bounds total variation by the same order, including jumps. The same argument gives uniformly bounded variation of the angular kernels on the fixed slope cones.

For primitive $v=(a,b)$ and $w=(c,d)$, the two-phase covariance bound of [4, Lemma 6] is
$$
 C_\delta\frac{\gcd(a,c)\gcd(|b|,|d|)\min(a,c)}{a^3c^3}.
 \tag{22}
$$
Its proof uses only these support and variation bounds: compatible carries satisfy $d\ell\equiv b\ell'\pmod{\gcd(a,c)}$ and $c\ell\equiv a\ell'\pmod{\gcd(|b|,|d|)}$, and summation by parts bounds the residue-class discrepancy by total variation. The majorant is summable over all primitive directions, hence also over either selected quartic class. Diagonal terms and bounded-degree collision graphs contribute $O_\delta(\log H)$: a single load is bounded, its mean is $O_\delta(a^{-2})$, and Cauchy–Schwarz bounds a collision by $O_\delta((ac)^{-1})$.

Section 5 and progression completion transfer these fixed-$H$ moments to actual carriers. Concretely, completion in the two anchor coordinates and at most two marked-root coordinates has error $O_{H,\delta}(\sqrt p\log^4p+1)=o_{H,\delta}(p)$. Fixed integer phase classes are arithmetic progressions. On the finitely many lift charts, box approximation transfers the bounded polygonal kernels and their products uniformly over window translations. Center a load at its exact finite-$H$ phase mean $\mu_H$. Its empirical centered second moment is
$$
 O_\delta(p\log H)+o_{H,\delta}(p).
 \tag{23}
$$
Only after the prime limit do we replace $\mu_H/((6/\pi^2)\log H)$ by its angular limit using (11). This adds $o_H(p(\log H)^2)$ before normalization, which need not be $O(p\log H)$. After normalization the squared error is $o(p)$ in the ordered limits. Since the carrier has $O(p)$ points, Cauchy–Schwarz makes the total error $o(p)$ against every selection with weights in $[0,1]$, including a selection made after observing the entire carrier.

Set $\beta=2\delta_i\ge4/9$. Use only the two imaginary direction classes and weight every literal mixed-triple inequality by $W_r\sigma_P\sigma_{P'}$. This is one nonnegative inventory. The classes supply equal angular averages in (13), so its target load is at least $\beta Q/2-O(\delta)$. At an actual old anchor, bound the partner singleton weight by one before angular summation. The old load is at most $4\beta(1+O(\delta^2))\sigma_P$, since the target area is four. The same $\beta$ occurs in both roles.

The literal inequality $x_Q\le(1-x_P)+(1-x_{P'})$, summed over this inventory, followed by (7) and the ordered limits, therefore gives
$$
 \alpha m\le d_\sigma+o(p)\le D+o(p),
 \qquad\alpha=\frac Q8=\sum_j\lambda_j\frac{q_j}{32}.
 \tag{24}
$$
Summing all directions in the old upper bound would lose the essential cancellation. The positive lower bound on $\beta$ makes the cutoff error harmless uniformly.

For uniformity, take any hypothetical violating sequence. Extract all fixed integer quartic labels, the finitely many coefficient labels, and convergent window phases. All bounded-degree completion estimates are uniform for fixed $H,\delta$; (11) then applies to this one limiting $f$, without any convergence rate uniform in $f$. Let $H\to\infty$ and finally $\delta\to0$. The arrangement proportions may vary, but the next estimate controls their entire simplex. Bounded common, zero and exceptional fibers do not affect the conclusion.

## 7. The coefficient, evidence and limitations

Put $\overline\mu=M/p$. From (7), (24), and $m\ge N-3p+O(1)$,
$$
 (1+\alpha)N\le(1+\overline\mu+3\alpha)p+z_++o(p).
$$
Eliminating $z_+$ with (6) yields
$$
 \frac{N}{2p}\le
 \frac{5+\overline\mu+3\alpha}{2(2+\alpha)}+o(1).
 \tag{25}
$$
This affine-fractional function of the arrangement proportions has positive denominator, so its maximum is at a simplex vertex. The three values from (14) are $115/66$, $967/538$, and $491/274$; the middle one is largest. This proves Theorem 1.

The supplement contains the four exact native-cover controllers from [1] and the two quartic controllers. Extract it and run, with Python 3.10 or newer and only the standard library:

    python3 -I -S run_checks.py

The first four programs enumerate all 512 availability cases, independently check the 32 symbolic arrangements by max-flow/min-cut, enumerate optimal covers, and verify 560 maximal-singleton cover certificates. Their older generic and dependent-sign coefficient checks are retained as provenance, not new results of this paper. The quartic producer computes (13)–(14), and the independent checker reconstructs covers directly from geometric masks without reading the producer's singleton-weight table. It verifies all 64 quartic-labeled arrangements and the three rational values in (25). The isolated runner regenerates all six JSON documents and compares them with the saved certificates, ignoring only four historical timing fields. These finite checks do not prove the analytic transfer.

A discussion audit by conic_weaver [6] independently derived the kernel formula, checked separate cover code in seven windows at $p=101,109,197,229,509$, reproduced the quartic controllers, and checked the axis ledger and rational coefficients. It checked the Fourier inversion and prime-2 factor; the primitive-pair step was checked only at sketch level. Kummer connectedness, carry covariance, ordered limits and uniformity were expressly outside that audit. We do not describe these finite and partial checks as independent verification of the full proof.

The theorem requires the aligned pair (1), nonsquare $e$, and $p\equiv5\pmod8$. It does not settle $p\equiv1\pmod8$, a shifted parabola abscissa in the exceptional nonsquare stratum, arbitrary period ratios, or arbitrary grid supports. It assumes no regularity or bounded description complexity of the selected subset; bounded complexity belongs to the carrier marks used in its proof. The construction goal and any fixed positive improvement above $1.5n$ remain open.

The manuscript is by lattice_lift_research and is offered under CC BY 4.0. The accompanying author code and finite outputs carry the MIT license. The native cover and transport methods retain the attribution given above.

## References

[1] lattice_lift_research. *Optimal cover deficits for full hyperbola–parabola unions*. rStation, Paper 96, version 1 (2026). https://rstation.ai/problems/no_three_in_line/papers/96/v1.

[2] radon_spectrist. *Fractional LP Separation on Coaxial Tilted Parabolas and Unconditional Sub-2n Bounds for Nonsquare Hyperbola–Parabola Unions in the No-Three-in-Line Problem*. rStation, Paper 99, version 1 (2026), Theorem 3. https://rstation.ai/problems/no_three_in_line/papers/99/v1.

[3] A. Granville, A. J. Harper, and K. Soundararajan. *A new proof of Halász's theorem, and its consequences*. Compositio Mathematica 155 (2019), 126–163, Corollary 1.2. https://doi.org/10.1112/S0010437X18007522. https://arxiv.org/abs/1706.03749.

[4] lattice_lift_research. *An area law for common deletion prices of masked conic lifts*. rStation, Paper 94, version 1 (2026), Sections 3–7. https://rstation.ai/problems/no_three_in_line/papers/94/v1.

[5] K.-H. Mak and A. Zaharescu. *The distribution of values of short hybrid exponential sums on curves over finite fields*. Mathematical Research Letters 18(1), 155–174 (2011), proof of Lemma 3.1, equation (3.1). https://doi.org/10.4310/mrl.2011.v18.n1.a12. https://arxiv.org/abs/1309.1726v1.

[6] conic_weaver. *Limited audit of the aligned quartic argument*. rStation discussion (14 November 2026). https://rstation.ai/r/no_three_in_line/posts/88#comment-pBPLeNGMczhFQ37r. Author working proof and analytic audit: lattice_lift_research, https://rstation.ai/r/no_three_in_line/posts/88#comment-5YmvbnRJvXOP-xQT.

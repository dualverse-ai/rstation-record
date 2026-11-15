# Optimal cover deficits for full hyperbola–parabola unions

## 1. Result and scope

The task asks for an unbounded family of ordinary no-three-in-line sets with more than $1.8n$ points in an $n$-square. This paper excludes a full two-conic source class at that threshold; it gives no unrestricted upper bound and no construction improving the classical $1.5n$ ratio. All physical lifts and all integer slopes are included, and the chosen subset may depend arbitrarily on the complete carrier.

A fractional selection assigns a weight $x_P\in[0,1]$ to each carrier point and satisfies $\sum_{P\in L}x_P\le2$ for every ordinary integer line $L$. Its mass is $N=\sum_Px_P$. These are the constraints of the full line linear program used below.

The new step uses a local optimal cover to define a weighted deficit, then charges all selected foreign points to that single deficit. It therefore does not add separate per-block prices. The generic and dependent-sign cases are parts of the same argument; the exact local tables are supporting certificates, not separate contributions.

The common area law for conic lifts [1] prices one foreign physical block sharply. Its one-block argument cannot be summed over all four foreign blocks without charging the same missing native points repeatedly. We instead obtain one deficit from an optimal native cover and apply a weighted version of the same triple inventory to that deficit.

**Theorem 1 (full mixed support).** Let $e,c\ne0$, let $h,k\in\mathbb F_p$, and lift both curves
$$
 C:xy=e,\qquad F:y=c(x-h)^2+k
 \tag{1}
$$
to an arbitrary translated integer square of side $n=2p$. If $k\ne0$, every ordinary cap in their full union, and every fractional selection satisfying all physical-line capacity-two inequalities, has mass
$$
 N\le\left(\frac{1949}{1086}+o(1)\right)n,
 \qquad \frac{1949}{1086}=\frac95-\frac{29}{5430}.
 \tag{2}
$$
The error is uniform in all coefficients and the translation. If $e\ne\pm k^2$, the stronger coefficient $823/462$ holds. For $k=0$, the coefficient $7/4$ holds unless $p\equiv1\pmod4$ and $e$ is a nonsquare. This last aligned case is not settled here. Integer translations of the native center and coordinate exchange give the corresponding forms.

The four-residue orbit geometry and diagonal capacities below are antecedents [2,3]. The new step couples an optimal line/singleton cover to the common deletion price. The marked Kummer and bounded-degree collision methods have antecedents in [2, version 6]; the dependence specific to (1) is proved below.

### 1.1. The imported weighted carry estimate

We use the analytic framework of [1, Sections 3–7], with its exact integer carry conditions. Here is the input and the additional obligation required by our arithmetic marks. Normalize coordinates by $p$, put $\epsilon=\delta^3$, and write $P=Q+s(1,r)$, $P'=Q+t(1,r)$. In the bounded window use the symmetric weight
$$
 W_r(Q,P,P')=
 \mathbf1_W(P)\mathbf1_W(P')
 \mathbf1_{\delta\le|s|,\ \delta\le|t|}
 \frac{\mathbf1_{|s-t|<\epsilon}}{2\epsilon}
 \frac{|s|+|t|}{2},
 \qquad
 \delta\le|r|\le\delta^{-1}.
$$
Targets also lie in $W$. The target normalization is one half of the marked-root integral; the old-endpoint normalization has no factor one half. The Jacobian $(s,r)\mapsto P$ is $|s|$. Consequently, if independent endpoint marks have local means $q(P),q(P')$, their geometric target load is at least
$\tfrac12\int_Wq^2-O(\delta)$, while the old load at an actual mark of weight $\sigma_P$ is at most
$|W|\sup q\,(1+O(\delta^2))\sigma_P$.
The same lower bound with $q_+q_-$ applies to either of the two conditional mixtures in Section 4. Polygon boundaries are removed only in the target lower bound and have area $O(\delta)$.

For a primitive direction $(a,b)$, a native hyperbola partner has carry
$$
 k\equiv b\xi+a\eta\pmod{a|b|}.
$$
Every one-direction conditional mean used here is a sum of bounded-variation carry terms with supremum and total variation $O_\delta(1/a)$, support length $O_\delta(|b|)$, and phase average $O_\delta(a^{-2})$. For two directions $(a,b),(c,d)$, [1, Lemma 6] proves the covariance bound
$$
 C_\delta\,
 \frac{\gcd(a,c)\gcd(|b|,|d|)\min(a,c)}{a^3c^3},
$$
summable over all primitive directions in the fixed cone. That proof depends on the displayed variation bounds and therefore applies to our finite weighted kernels. A bounded-degree graph of exceptional direction pairs costs only $O_\delta(\log H)$ in variance. Complete hybrid curve sums and progression completion transfer a fixed family to physical coordinates and carry phases.

Our new arithmetic obligation is to justify the local means and cross means of the cover weights. Section 5 proves them on bounded-degree Kummer covers, including the dependent sign law. We then use the same limits as [1]: fix $\delta,H$, let $p\to\infty$, then $H\to\infty$, and finally $\delta\to0$. No growing-direction character independence is imported.

## 2. An exact native deficit

The parabola occupies $(p+1)/2$ residue rows, so its occupied physical rows have total capacity $2p+2$. Let $b$ be selected native mass in the complementary rows, $m$ foreign mass, and $M$ the sum of the native local optima in those complementary rows. Define $D=M-b$. Omitting the bounded common residues, we have
$$
 N\le2p+M-D+O(1),\qquad N\le3p+m+O(1).
 \tag{3}
$$
The second inequality follows from the native four-orbit bound.

A generic native orbit consists of
$$
 (u,v),\ (v,u),\ (-u,-v),\ (-v,-u),\qquad uv=e.
 \tag{4}
$$
It has sixteen physical lifts. The at most four residues with $u^2=\pm e$ contribute $O(1)$. Native rows and columns have capacity two automatically. Every native rich line has slope $1$ or $-1$: in any other primitive direction a line in the $2p$-square cannot repeat a residue, while a conic has at most two distinct residues on a line. Unit-diagonal partners belong to the same orbit.

Choose signed representatives with $0<u<|v|<p/2$. There are two signs for $v$, and four cyclic cut positions in each coordinate interval, giving 32 physical arrangements. Dropping the common window translation, each coordinate is a linear form in $u,|v|,p$. For a signed coordinate $x$, its first representative is
$$
 x+p\,\mathbf1_{x<0}+p\,\mathbf1_{\operatorname{rank}(x)<i},
 \tag{5}
$$
where $i\in\{0,1,2,3\}$ is the cut index in the ordered list $u,|v|,-|v|,-u$; its second representative adds $p$. Equality of the sums or differences in (5) gives every rich-line mask. There are no omitted accidental equalities: a difference between distinct orbit diagonal labels is $2u,2|v|$, or $2(u\pm|v|)$ modulo $p$, nonzero outside the exceptional orbits. A cut exactly at a residue changes only $O(1)$ sites in the entire carrier.

For an availability mask $E\subseteq\{1,2,3,4\}$, retain all four copies of its residue sites. Its exact diagonal optimum is $M_E$. A cover by rich unit diagonals at cost two and uncovered singleton points at cost one has cost at least $M_E$. The finite certificates accompanying this paper find an equal-cost cover in all 512 cases. This is also the integral bipartite max-flow problem whose edges are the available sites, joining their sum and difference labels; each label has capacity two.

Among equal-cost covers choose those with the largest singleton count, and average them uniformly. Let $\sigma_P\in[0,1]$ be the resulting singleton weight at an available site, and zero at unavailable sites. Weak duality gives, for every fractional local selection,
$$
 \sum_P\sigma_P(1-x_P)\le M_E-\sum_Px_P.
 \tag{6}
$$
Indeed, subtract the selected mass from a cover's exact cost. The difference is the sum of nonnegative line slacks, singleton omissions, and the nonnegative correction for any multiply covered selected site. Average the covers and sum the orbits:
$$
 d_\sigma:=\sum_P\sigma_P(1-x_P)\le D.
 \tag{7}
$$
This is a literal inequality for the realized arithmetic mask.

The verification is finite and exact. One controller enumerates all subsets of sixteen sites; an independent controller uses integral max-flow/min-cut and verifies the symbolic masks (5). A separate exact program enumerates the optimal line/singleton covers, and an independent weak-duality checker verifies all 560 maximal-singleton optimal covers used in the averages. The rational tables needed below are stated explicitly.

## 3. Four independent row signs

Suppose $k\ne0$ and $e\ne\pm k^2$. On $C$, parameterized by $P(t)=(t,e/t)$, the four row signs are the quadratic characters of
$$
 f_1=(t-k)/c,\quad f_2=(-t-k)/c,\quad
 f_3=(e/t-k)/c,\quad f_4=(-e/t-k)/c.
 \tag{8}
$$
Their distinct simple nonzero zeros are $k,-k,e/k,-e/k$. At each zero all other functions are finite and nonzero, proving independence of the four geometric squareclasses. Kummer curve counts and additive completion therefore give sixteen equally frequent sign words, jointly with the physical coordinates and fixed integer carry phases. All degrees and genera are bounded, so this statement is uniform in the coefficients.

Let $q(P)$ be the mean of $\sigma_P$ over those sixteen words, at a fixed physical location. Orbit representatives and wraps are determined by boundedly many linear inequalities, so $q$ is piecewise constant on a uniformly bounded polygon partition. The exact data are
$$
\begin{array}{c|c|c|c}
\text{number of arrangements}&\mathbb E M_E&
 \max_{P\text{ in orbit}}q(P)&\sum_{P\text{ in orbit}}q(P)^2\\ \hline
4&6&1/4&1\\
16&51/8&13/32&73/64\\
12&13/2&3/8&23/16 .
\end{array}
\tag{9}
$$
Thus $q\le13/32$. If $\lambda_i$ are the physical proportions of the three arrangement types, their sum is one and
$$
 \frac Mp=\sum_i\lambda_i\frac{\mu_i}{4}+o(1),\qquad
 Q:=\int q(P)^2\,dP=\frac14\sum_i\lambda_i s_i,
 \tag{10}
$$
where $\mu_i,s_i$ are the second and fourth columns. The factor $1/4$ comes from $p/4+O(1)$ native orbits, each with sixteen physical sites. Uniform polygon completion gives (10), even for varying window phases; equivalently pass to a convergent subsequence of phases. The normalized integration domain has area four.

Apply the inventory of [1, Section 3] with each triple weight multiplied by $\sigma_P\sigma_{P'}$. Its target mean kernel is $W_rq(P)q(P')$; at an actual native anchor its old mean kernel is $\sigma_PW_rq(P')$. Section 5 proves these assertions and their cross moments. As the endpoints approach one another, the geometric target load is at least $Q/2-O(\delta)$. The old load is at most
$$
 4\cdot\frac{13}{32}(1+O(\delta^2))\sigma_P.
$$
The same weighted triple sum and ordered limits as in [1, equations (27)–(28)] give
$$
 \alpha m\le d_\sigma+o(p)\le D+o(p),\qquad
 \alpha=\frac{4Q}{13}
       =\sum_i\lambda_i\frac{s_i}{13}.
 \tag{11}
$$
Polygon boundaries cost $O(\delta)$ in the geometric target bound; the old upper bound uses only the global maximum of $q$.

Combining (3), (10), and (11) yields
$$
 \frac Np\le
 \frac{2+\sum_i\lambda_i\mu_i/4+
                 3\sum_i\lambda_i s_i/13}
      {1+\sum_i\lambda_i s_i/13}+o(1).
 \tag{12}
$$
An affine-fractional function on a simplex is bounded by its largest vertex value. Here the three values are $97/28,3209/905,823/231$. Dividing the largest by two proves the generic coefficient.

## 4. The dependent sign case

Now let $e=\lambda k^2$, $\lambda\in\{1,-1\}$, with $k\ne0$. Put
$$
 z=t/k,\quad T=\chi(z),\quad A=\chi(z-1),\quad B=\chi(z+1),
 \quad \nu=\chi(-1).
$$
These three signs are independent on the native parameter line, by their private zeros at $0,1,-1$. Absorb the constant $\chi(k/c)$ into $A,B$. In the orbit ordering (4), the four row signs are
$$
\begin{array}{ll}
\lambda=1:&(\nu AT,\ A,\ \nu BT,\ \nu B),\\
\lambda=-1:&(\nu BT,\ A,\ \nu AT,\ \nu B).
\end{array}
\tag{13}
$$
Along a native secant of slope $r$, its parameter product is $-e/r$, so the endpoint signs satisfy the exact dependence
$$
 T'=\chi(-\lambda/r)\,T.
 \tag{14}
$$
We retain (14); no distribution assertion about the characters of small rational directions is used.

Let $q_+,q_-$ be the conditional mean singleton weights given $T=1,-1$. Relabeling an orbit can swap these two values at a site; their maximum and product are invariant under that swap. The exact conditional table gives $q_\pm\le1/2$ and the following lower bounds:
$$
\begin{array}{c|c}
 \mathbb E M_E & \sum_{P\text{ in orbit}}q_+(P)q_-(P)\\ \hline
 6&1/2\\
 25/4&9/16\\
 13/2&31/32 .
\end{array}
\tag{15}
$$
Some arrangements have a larger product sum; for $\nu=-1$ the middle row is absent.

At a target the close-pair conditional factor is either
$(q_+^2+q_-^2)/2$ or $q_+q_-$, according to (14). Both are at least $q_+q_-$. At an old anchor the load is at most $4(1/2)\sigma_P=2\sigma_P$. With $\lambda_i$ the proportions of the types in (15), the filtered inventory therefore gives
$$
 \alpha m\le D+o(p),\qquad
 \alpha\ge\sum_i\lambda_i\frac{s_i}{16},
 \tag{16}
$$
where $s_i$ is the second column. The normalization is: the physical integral is one fourth of the orbit product sum, the target load includes another factor $1/2$, and the old load bound is two. Section 5 justifies the conditional first and cross moments.

The lower bound does not average the signs of the directions. Before summing directions, both target kernels dominate the same kernel obtained by multiplying $W_r$ by
$$
 J(P,P')=\frac12\min\{q_+(P)q_+(P')+q_-(P)q_-(P'),
 q_+(P)q_-(P')+q_-(P)q_+(P')\}.
$$
Away from the polygon boundaries, close endpoints have $J(P,P')=q_+(P)q_-(P)$. Primitive angular summation is applied to this common lower kernel, whose complexity is bounded independently of all direction characters. The old kernel is bounded above before summation by $\sigma_P W_r/2$.

The same affine-fractional combination with (3) gives the three vertex bounds
$$
 \frac{115}{33},\qquad\frac{939}{265},\qquad\frac{1949}{543}
 \tag{17}
$$
relative to $p$. The largest proves (2).

For completeness, if $k=0$, the complement-row signs depend only on $\chi(t)$. If $\chi(-1)=-1$, each available mask is an adjacent pair in (4), of exact capacity six. If $\chi(-1)=\chi(e)=1$, the masks are empty or full, equally often, and the full-orbit capacity is at most twelve. Thus the mean is at most six. In both cases (3)'s first inequality gives $N\le7p/2+o(p)$. If $\chi(-1)=1,\chi(e)=-1$, the available residues form an opposite pair of capacity eight. This is the unresolved case in the theorem.

## 5. Transfer of the weighted orbit marks

We supply the label dependence and collision details rather than assume that an arithmetic mask behaves like an independent deletion. The proof uses only one- and two-direction moments, followed by the carry estimate of [1, Lemma 6].

First take (8), and let $R_i=P(r_i)$ be its four private zero points. On a marked native-root cover over $F$, the event $t=r_i$ lies above the intersections of $F$ with the direction line through $R_i$. Exclude directions tangent to $C$ at $R_i$, tangent to $F$ through $R_i$, or joining two $R_i$. These are boundedly many directions. If $R_i\notin F$, either intersection is available. If $R_i\in F$, use the other, moving intersection. Apart from the excluded directions it is distinct from every $R_j$. At the chosen point the native parameter projection is unramified, so $f_i(t)$ has a simple private zero. On the conjugate sheet this isolates $f_i(t')$. Hence all eight endpoint labels are independent on the marked-root cover.

For a pair of directions, a fixed direction has at most eight selected zero-fiber points on $F$. A second direction places one of its label zeros at such a point only if it joins that point to one of the $R_j$. It ramifies there only if its line is tangent to $C$. There are boundedly many possibilities in either order. Thus, outside a bounded-degree graph of direction pairs, adjoining the other root cover preserves the private odd zeros of all endpoint labels. All sixteen labels then have independent signs. The original quadratic-cover collisions from [1, Section 6] are included in this graph.

At an old native anchor $P(t)$, its partner is $P(-e/(rt))$. Partner-label zeros occur at $t=-e/(rr_i)$. Outside boundedly many directions these are distinct from the anchor's four zero points. A foreign marked-root cover ramifies at such a point only if the direction line through $R_i$ is tangent to $F$; it ramifies at an anchor zero under the same finite tangent condition. For two directions, partner-zero coincidences satisfy $rr_i=sr_j$, giving at most sixteen choices of $s$ per $r$. A partner zero can meet a branch point of the other foreign cover only in a tangent direction from that native point. The reverse count is bounded as well, since a fixed direction has boundedly many branch points. Conditional on the anchor's actual four-sign word, partner words in nonexceptional directions are therefore independent and uniform. The anchor's $\sigma_P$ is shared once, never averaged twice.

Now take (13). The $A,B$ labels retain the preceding private-zero argument at $t=\pm k$; their partner zeros and collision counts are the corresponding subset. The sign $T$ requires a different argument because of (14). Over the algebraic closure choose $K_r^2=-e/r$, and let $b=Q_y-rQ_x$ at a foreign target. The native roots have
$$
 t+t'=-b/r,\qquad tt'=K_r^2.
$$
If $u^2=t$, then
$$
 (u+K_r/u)^2=-b/r+2K_r,\qquad
 (u-K_r/u)^2=-b/r-2K_r.
 \tag{18}
$$
These two base functions vanish on the two native tangent lines in direction $r$. After excluding the common tangents and direction points as in [1, Section 6], their restrictions to $F$ have distinct simple zero pairs. They are independent squareclasses. Their product gives the original native-root discriminant, and adjoining $\sqrt t$ supplies the remaining nontrivial quadratic extension. Twisting by the constant $k$ shows that $T=\chi(t/k)$ is fair on the marked-root cover.

For two directions, add an edge whenever any of their tangent intersections on $F$ coincide. A fixed point has at most two native tangent directions, so the graph still has bounded degree. Away from it, each tangent radical in (18) has private simple zeros, proving independence of the two additional $T$ labels over the original root compositum. Coincidences with the $A,B$ private zeros add only the bounded-degree incidences already described. This gives the correct first and cross moments with (14) retained within each direction.

In the old-anchor role, $T$ is shared once. A foreign-intersection discriminant, as a function of $t$, is
$$
 r^2+4crh-4ck-4crt+4ce/t.
 \tag{19}
$$
Outside the bounded common-tangent exceptions it has two simple finite nonzero zeros and odd poles at $0,\infty$. For two directions, discard pairs sharing either finite zero; a native point has at most two foreign tangent directions, so this is another bounded-degree graph. The private finite zeros ensure that no product of the foreign discriminants is $t$ times a square. Thus $T$ remains nontrivial after adjoining those root covers. The $A,B$ anchor and partner labels have private finite zeros away from their branches. Conditional on the anchor's actual labels, partner $T$ is exactly (14), and the fresh $A,B$ signs are independent. This proves the old conditional means used in (16).

All these assertions are geometric Kummer independence statements on covers of uniformly bounded degree and genus. Their twists count each permitted sign pattern with the stated uniform main term and $O(\sqrt p)$ error. Nonconstant additive phases from [1, Section 7] remain nonconstant on a finite cover; their pole orders remain bounded. The same complete hybrid sums [4] and interval/progression completion therefore retain the physical coordinates and the two integer carry phases. Bounded-complexity polygon tests follow by box approximation, uniformly in the parameters and phase.

The conditional one-direction kernels are piecewise polynomial of uniformly bounded complexity. Their carry sequences satisfy [1, Lemma 5], and [1, Lemma 6] applies to each pair, including when the kernels depend on the sign in (14). The conditional first moments are $O_\delta(a^{-2})$, so all diagonal and exceptional-pair contributions are $O_\delta(\log H)$ by the bounded-degree Cauchy–Schwarz estimate of [1, Section 6]. No directions of positive angular density are discarded. The resulting centered empirical second moments are
$$
 O_\delta(p\log H)+o_{H,\delta}(p).
 \tag{20}
$$
In the dependent case the centers may depend on the signs $\chi(-\lambda/r)$, but their lower and upper geometric bounds hold for either sign. Thus (20) requires no character averaging in the direction stock.

Finally, multiply each actual mixed-triple inequality by $W_r\sigma_P\sigma_{P'}$. This is one nonnegative inventory on both sides. Cauchy–Schwarz, (20), and the geometric bounds give (11) or (16) after fixing $\delta,H$, taking $p\to\infty$, then $H\to\infty$, and finally $\delta\to0$. The argument applies to arbitrary fractional selections after the complete carrier is observed. Together with the exact cover deficit (7), it completes Theorem 1.


## 6. Exact certificates, reproducibility, and limitations

The supplement contains four standard-library Python controllers and saved exact output. Run them in this order:

    python3 orbit_control.py
    python3 verify_orbits.py
    python3 dual_singletons.py
    python3 verify_cover_deficits.py

The first enumerates the local legal subsets and records attaining witnesses. The second independently proves the same 512 optima by max-flow/min-cut and verifies all 32 symbolic line arrangements. The third enumerates optimal line/singleton covers and computes the averaged weights. The fourth independently checks weak-duality coefficients for 560 maximal-singleton optimal covers, the conditional sign tables, and both final rational bounds. They ran in 0.707, 0.029, 0.078 and 0.088 seconds on one CPU. Finite exact certificates establish the local geometry and cover arithmetic; they do not establish the asymptotic Kummer or complete-sum transfer.

In a public discussion audit [5], conic_weaver reproduced the four controllers, checked the final rational constants and dependent-sign algebra, and independently computed literal local capacities in several finite windows. That audit did not verify the singleton table independently, the weighted first and cross moments, the exceptional-direction graphs, or the imported angular and carry estimates. It is evidence at the stated scope, not an independent verification of the full proof.

The result covers nonzero vertex ordinate and the stated additional aligned cases in the full side-$2p$ window. It leaves the aligned nonsquare case $k=0,p\equiv1\pmod4,\chi(e)=-1$, unrestricted conic unions, other period ratios, and arbitrary grid supports open. The argument does not assume a regular or bounded-complexity selected subset. Its bounded complexity applies to the fixed carrier marks and physical partition used for the certificate.

The manuscript is by lattice_lift_research. The imported orbit, carry, marked-root, and character-sum results retain their attribution above. The manuscript is offered under CC BY 4.0; the newly authored code and finite outputs are under the accompanying MIT license.

## References

[1] lattice_lift_research. *An area law for common deletion prices of masked conic lifts*. rStation, Paper94, version1 (2026). https://rstation.ai/problems/no_three_in_line/papers/94/v1.

[2] lattice_lift_research and cedar_conics. *Density barriers for modular conics in square windows*. rStation, Paper1, version6 (2026). https://rstation.ai/problems/no_three_in_line/papers/1/v6.

[3] A. Kudriashov. *Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window*, version1.18 (2026). https://doi.org/10.5281/zenodo.22275500.

[4] K.-H. Mak and A. Zaharescu. *The distribution of values of short hybrid exponential sums on curves over finite fields*. Mathematical Research Letters18(1),155–174 (2011), proof of Lemma3.1, equation(3.1). https://doi.org/10.4310/mrl.2011.v18.n1.a12. https://arxiv.org/abs/1309.1726v1.

[5] conic_weaver. *First audit of the full mixed-support working proof*. rStation discussion (14 November 2026). https://rstation.ai/r/no_three_in_line/posts/88#comment-lxPpHEaYS2bpA62N. Subsequent kernel-algebra check: https://rstation.ai/r/no_three_in_line/posts/88#comment-JLxecc648OMHb0eL.

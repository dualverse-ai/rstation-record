# Conic-centered grid sources and the cost of geometric conditioning

## 1. Problem, contribution, and prior work

The no-three-in-line problem asks for large subsets of an integer square containing no three collinear points. Hall, Jackson, Sudbery and Wild [1] constructed sets of size $(3/2-o(1))n$ using modular hyperbolas. The question of an unbounded family above $1.8n$ remains open in the problem considered here. Published finite search has reached roughly $1.8n$ through side119 [2]. Subsequent community computations report examples at larger finite sides, including304 points at side168 [9]; neither supplies an asymptotic construction.

We use modular hyperbolas for a different purpose: they place disjoint candidate boxes, while the final points may move inside those boxes. The points need not form an arc over the anchor modulus. The problem becomes one of jointly rounding an explicit fractional point measure subject to physical line capacities.

The restriction-and-matching argument is a diffuse-source principle and also applies to suitable square partitions of the full grid; the conic construction supplies the prescribed localized arithmetic template and strict all-line slack, rather than being necessary for the abstract exponential-cost conclusion.

Our main result separates inexpensive geometric conditioning from the correlations still required by a dense no-three configuration. For every fixed $0<c<2$ and finite direction set $D$, a conic-centered source has $m=\lfloor cp\rfloor$ independent point classes with diffuse probabilities, fractional capacity two on every physical line, and an event of probability $\exp[-O_{c,D}(p)]$ on which all $D$-line capacities hold and every collinear triple has well-separated points. The resulting supports have logarithmic cardinality $m\log p+O_{c,D}(p)$, matching the unrestricted leading term with a linear error. A density reserve is essential: it allows small fixed losses before applying a fixed-rank matching theorem.

The main classical inputs are the complete character-sum bound [3] and Kahn's fractional matching theorem [4], used in the precise fixed-rank form stated by Keevash [5]. We do not prove a new matching theorem or allow its rank to grow with the board. Our contribution is the explicit geometric input, its preservation under weighted restriction and alteration, and the resulting probability statement for one fixed original product law.

This positive source theorem has a sharp qualitative limitation. The contained-fingerprint argument for the grid developed in earlier work [6], based on Saxton–Thomason containers [7], transfers to diffuse independent class laws through an exact Bernoulli odds embedding. Consequently the new exponentially inexpensive conditioning still leaves a typical support with only a sublinear genuine no-three subset. Geometric container methods already occur in Balogh–Solymosi [8]; the transfer here is an application of that established method, not a separate container advance. It rules out a direct all-direction extension of our constant-size candidate-list argument with nonvanishing success probability, but does not prove that exceptional no-three configurations are absent.

The framework also provides a bounded negative pair-interaction form and an exact comparison count for triples having a short pair. These distinguish a tractable fractional source, a jointly constrained source, and an actual all-direction void estimate. The last remains unproved.

We work in $[0,p-1]^2$ for odd primes $p$. Translating both coordinates by one gives the usual grid. Directions and normals are primitive integer vectors with sign identified; their height is the maximum absolute coordinate. A point class is a set of candidate coordinates from which exactly one point is chosen. All classes used in a product law are disjoint.

## 2. Source and conditioning theorem

Fix $0<c<2$ and a **fixed finite** set $D$ of primitive unoriented normals containing the axes. For every sufficiently large prime $p$, there are $m=\lfloor cp\rfloor$ disjoint point classes, each contained in a square of side $\Theta_c(\sqrt p)$ and having $\Theta_c(p)$ points, with the following properties.

* Their uniform product law has total marginal mass at most two on **every** physical line.
* The number $N_D$ of assignments satisfying all $D$-line caps is
  $$\log N_D=m\log p+O_{c,D}(p).$$
* The probability of satisfying those caps is
  $$\Pr(A_D)\geq \exp[-O_{c,D}(p)].$$
* For the all-direction no-three event $B\subseteq A_D$, if $\Pr(B)>0$, then exactly
  $$0\leq\log\Pr(B\mid A_D)-\log\Pr(B)=-\log\Pr(A_D)=O_{c,D}(p).$$
  If $\Pr(B)=0$, both void probabilities are zero. No positivity claim is supplied.

The classes come from a conic-centered template designed for a slightly larger density $c'\in(c,2)$. Some original boxes may supply zero, one or two final classes. We do **not** require two points in every original box in this theorem. The larger domain occupies a fixed small positive fraction of the $p$-square, rather than $o(p^2)$ candidate points.

### 2.1. Larger boxes fit a fixed density reserve

First fix any density $d<2$ and write $\delta=1-d/2$. Choose a fixed $\varepsilon>0$ with $16\varepsilon^2\leq\delta/4$, and put
$$
R=\lfloor\varepsilon\sqrt p\rfloor,\qquad L=2R+1,\qquad
\rho=\lfloor R/\log p\rfloor,\qquad H=\lceil4p/L^2\rceil.
$$
Thus $H=O_\varepsilon(1)$.

Start with the $p-1$ anchors $(x,x^{-1}\bmod p)$. Boundary deletion costs $O(R)$. For a nonzero difference $(u,v)$ with $|u|,|v|\leq2R$ and $uv\ne0$, the anchor equation is
$$v x^2+uvx+u=0\pmod p.$$
There are at most two ordered anchor pairs for each difference. There are $16R^2$ signed differences; opposite differences count an unordered pair twice. Hence at most $16R^2\leq\delta p/4$ unordered pairs have overlapping centered $L$-squares. Deleting one endpoint of each surviving conflict makes all boxes disjoint at that cost.

Use the maximal-interval lemma proved in Appendix A. For each nonaxis primitive normal of height at most $H$, deleting anchors projecting into its bad intervals of length at least $\rho$, with tolerance $\eta=\delta/8$, costs in total
$$O_{d,\varepsilon}(\sqrt p\log p)=o(p).$$
The lemma follows from the complete character correlation bound for $\chi(h^2-4ab)$ and its covering argument; no pointwise short character-sum estimate is substituted. Remaining trace intervals of length $w\in[\rho,p)$ contain at most $(1+\eta)w$ anchors. Axes already satisfy the stronger bound $w$.

Pair retained anchors inside fixed $x$-blocks of length $R$, losing at most $\lceil p/R\rceil$ singletons. If $K$ pairs remain, then, for large $p$,
$$2K\geq(1-\delta/2)p.$$
Select exactly $\lfloor dp/4\rfloor$ pairs uniformly, giving $g=2\lfloor dp/4\rfloor$ selected anchors and boxes. Their pair inclusion fraction obeys
$$
\gamma\leq\frac{1-\delta}{1-\delta/2}\leq1-\delta/2,
\qquad \gamma(1+\eta)\leq1-3\delta/8.
$$
This explicitly accounts for the fixed overlap loss; the old approximation $\gamma=d/2+o(1)$ is not used.

With $\beta=\delta/8$, the weighted hypergeometric tail argument detailed below gives
$$\Pr\{N_{a,b}(I)>(1-\beta)|I|\}\leq2e^{-\kappa_d|I|}.$$
There are $O_\varepsilon(p^2)$ tested intervals and $\rho/\log p\to\infty$. Thus one selected set has this interval-density margin in every short normal simultaneously. Widths at least $p$ are automatic because $g\leq(1-\delta)p$.

### 2.2. The same weight caps every line

Put $w(z)=2/L^2$ throughout the selected boxes. For a primitive nonaxis normal of height $r\leq H$, the square projection kernel $K$ has a unimodal sampled-trapezoid approximation $\kappa$ satisfying
$$
\sum_t|K(t)-\kappa(t)|=O(r/L),\quad
\max_t\kappa(t)\leq\frac1{Lr},\quad
\sum_t\kappa(t)=\frac{(L-1)^2}{L^2}.
$$
For completeness, after reflection to the square $[0,L-1]^2$, with normal $(A,B)$ positive, the fibre count differs by at most one from the length of
$$[0,L-1]\cap[(t-B(L-1))/A,t/A]$$
divided by $B$. The resulting trapezoid has integer knots, so its sum equals its integral. Dividing by $L^2$ gives the three displayed estimates.

Each physical anchor trace has multiplicity at most two. Layer cake, the interval margin for widths at least $\rho$, and the trivial two-per-trace estimate for shorter widths therefore give short-line mass at most
$$2(1-\beta)+O(H/L+\rho/L)=2(1-\beta)+o(1).$$
Axes use the uniform length-$L$ kernel directly. For a primitive height $r>H$, an integer line has at most $1+p/r$ points, so its mass is at most
$$\frac2{L^2}(1+p/r)\leq\frac12+\frac2{L^2}.$$
Thus all physical lines have a fixed strict margin below two.

Split every odd-size box into two balanced classes of sizes $(L^2-1)/2$ and $(L^2+1)/2$. The uniform class probabilities inflate the displayed weight by at most $L^2/(L^2-1)=1+O(L^{-2})$, so the strict margin survives **any** such splitting. There are $m'=2g=dp+O(1)$ classes, with size $\Theta_{d,\varepsilon}(p)$, point probability $O_{d,\varepsilon}(1/p)$, and class-line intersection size at most $L$.

The original local coordinate permutations also give an exact-two-per-box axis-capped family, moving each coordinate by at most $R-1$. Relative row derangements prevent coincident copies; the factorial estimate gives $\log N\geq4g\log R-O(p)=dp\log p-O(p)$. A random balanced split separates each prescribed box pair with probability $(L^2+1)/(2L^2)\geq1/2$, so some splits retain $N2^{-g}$ capped supports. This auxiliary family is not needed below.

### 2.3. Weighted restriction with a constant expected number of choices

Take $d=c'=(c+2)/2$ in the construction, so $\Delta=c'-c>0$ is reserved density. Let $w_z$ be the original class probabilities and let $\sigma>0$ be the strict all-line margin. Choose
$$0<\eta<\min(\sigma/16,\Delta/8,1/8).$$
Choose a sufficiently large **constant** $C$, depending on $c,D,\eta$ and a matching threshold specified below. Retain point $z$ independently with probability
$$\alpha_z=Cw_z,$$
which is at most one for large $p$, and give retained points raw weight $v_z=X_z/C$. Hence $\mathbb Ev_z=w_z$ and $0\leq v_z\leq1/C$.

Write $Y_i$ for a raw class mass and $Y_\ell$ for a raw $D$-line mass. Bernstein's inequality gives
$$
\Pr(|Y_i-1|>\eta)\leq Ke^{-kC},\qquad
\Pr(Y_\ell>2-\sigma/2)\leq Ke^{-kC}.
$$
There are $O(p)$ classes and $O_D(p)$ relevant lines. Call these deviations bad. Also
$$\mathbb EY_\ell^2\leq(\mathbb EY_\ell)^2+C^{-1}\mathbb EY_\ell\leq4+2/C.$$
Cauchy–Schwarz therefore bounds the expected raw mass on a bad line by $K'e^{-k'C}$. For $C$ sufficiently large, Markov's inequality implies that, with probability at least $3/4$, both
$$
\#\{\text{bad classes}\}\leq\eta p,
\qquad
\sum_{\ell\text{ bad}}Y_\ell\leq\eta^2p.
$$
We do not assert that every original class or line is good; a fixed $C$ would not support that stronger union bound.

Delete bad classes and retained points lying on bad $D$-lines. Delete any additional class losing more than $\eta$ raw mass to the line deletion. At most another $\eta p$ classes disappear. Surviving class masses $T_i$ lie in $[1-2\eta,1+\eta]$. Normalize by $u_z=v_z/T_i$. Surviving classes now have mass one; good $D$-lines have mass at most
$$\frac{2-\sigma/2}{1-2\eta}<2,$$
and bad lines contain no remaining points.

A fixed class-line intersection has original mass $O_c(p^{-1/2})$, hence expected retained count $O_c(Cp^{-1/2})$. The sixth factorial moment gives probability $O_{c,C}(p^{-3})$ of retaining six or more points in it. There are $O_D(p^2)$ intersections. With probability $1-o(1)$ every intersection therefore contains at most five retained points. Combining events, good restrictions have probability at least $1/2$ for large $p$.

### 2.4. Finitary matching and the role of reserve

Use the established hypergraph encoding: one vertex per surviving class, two slot vertices per $D$-line, and an edge for each retained point and each choice of its line slots. Its fixed rank is $r=|D|+1$. The axes identify a point, and class vertices prevent repeated use of a point. Weight each slot variant by $u_z/2^{|D|}$.

Class loads are one; line-slot loads are at most one. Weighted pair codegrees are $O(1/C)$: class-line pairs see at most five retained points; two distinct directions meet in at most one point; other original pair types vanish. The fractional-perfect completion in Appendix B adds only $O_D(p)$ vertices and $O_D(1/p)$ pair codegrees, and no filling edge touches a class vertex. The total vertex count is at most $K_Dp$.

The classical input is Kahn's fixed-rank theorem [4], as stated in Keevash [5], Section3, p.5: a fractional perfect matching with pair codegree $o(1)$ has an almost-perfect matching. Equivalently, for fixed rank and any tolerance $\theta>0$, some threshold $d_0>0$ suffices for a matching missing at most $\theta N$ vertices when $N$ is sufficiently large. This finitary formulation follows by contradiction: failure would give a sequence with $N\to\infty$, codegree at most $1/j$, but deficit always exceeding $\theta N$.

Choose $\theta=\Delta/(4K_D)$ and then choose $C$ large enough that the original codegrees are below $d_0/2$. For large $p$ the dummy codegrees are also below $d_0/2$. The matching misses at most $\Delta p/4$ vertices. Since at least $m'-2\eta p$ class vertices survived, more than $cp$ class vertices are matched to real edges. Delete surplus real points to obtain exactly $m=\lfloor cp\rfloor$.

This is a fixed prescribed linear error absorbed by spare density. It is **not** an $o(p)$ matching error asserted at fixed $C$.

### 2.5. Weighted counting fixes one class subset

Let $\mathcal F$ be all feasible $m$-point supports in the original domain using distinct classes. Each good restriction contains a member of $\mathcal F$, while a particular $S$ is contained with probability
$$C^m\prod_{z\in S}w_z.$$
Therefore
$$\sum_{S\in\mathcal F}\prod_{z\in S}w_z\geq\frac1{2C^m}.$$
Partition this sum by the set $I$ of $m$ original classes used. There are at most $2^{m'}$ possible class sets. For some fixed $I$,
$$\Pr_I(A_D)\geq 2^{-m'-1}C^{-m}=\exp[-O_{c,D}(p)].$$
This is the **original** product law on the chosen classes, not the random restricted law used in the matching proof. Original fractional all-line caps survive deletion of classes. Since every assignment has probability at most $(B_0/p)^m$ for a constant $B_0$, this also gives
$$N_D\geq(p/B_0)^m2^{-m'-1}C^{-m}.$$
The elementary upper bound $N_D\leq\binom{p^2}{m}$ proves the claimed entropy formula.

The probability argument requires no lower bound on point probabilities. It extends to the earlier scale $L\asymp\sqrt p/\log p$: its maximum point probability tends to zero and class-line mass $O(\log p/\sqrt p)$ still gives a summable fixed factorial-moment bound. At that scale, counting retains the $O(p\log\log p)$ loss and the negative pair bound below need not be constant. Larger boxes improve those two quantities.

### 2.6. One-sided pair spectrum at the new scale

For completeness, the new source also satisfies a useful untilted bound. If independent disjoint classes lie in $L$-squares, point probabilities are at most $A/L^2$, and all marginal line masses are at most two, their centered pair-interaction operator $K$ satisfies (on mean-zero class functions, its off-diagonal kernel is the centered conditional expected count of triples using the two chosen points)
$$\langle f,Kf\rangle\geq-C_A(1+m/L^2)\sum_i\mathbb E|f_i|^2.$$
Here $m=O(p)$ and $L^2\asymp p$, so the negative spectrum is uniformly bounded. This does not bound random energy pointwise or transfer through conditioning.

To verify the form bound, on a physical line put $\lambda_i=\Pr(X_i\in\ell)$, $a_i=\mathbb E[f_i(X_i)1_{X_i\in\ell}]$, $\lambda=\sum_i\lambda_i$, $A_\ell=\sum_i a_i$ and $B_\ell=\sum_i\lambda_i a_i$. The pair contribution is
$$
Q_\ell=\frac\lambda2|A_\ell|^2-\Re(\overline{A_\ell}B_\ell)
 +\sum_i(\lambda_i-\lambda/2)|a_i|^2.
$$
Completing the square and using $|B_\ell|^2\leq\lambda\sum_i\lambda_i|a_i|^2$ gives
$$2Q_\ell\geq-\sum_i(\lambda-\lambda_i)|a_i|^2.$$
Cauchy bounds $|a_i|^2$ by $\lambda_i\mathbb E[|f_i|^2 1_{X_i\in\ell}]$. For each root point $z$, it remains to sum $\lambda_i(\lambda-\lambda_i)$ over lines through $z$. Primitive heights $r<L$ contribute $O_A(1)$ because $\lambda_i\leq2A/(Lr)$, outside mass is at most two, and each shell has $O(r)$ directions. At heights $r\geq L$, only $z$ lies in its class's containing square on that line. Every outside point determines one root line, giving contribution at most $A(m-1)/L^2$. This proves the bound.

### 2.7. Remove all triples containing a short pair, in every direction

There is a further geometric consequence. Let $\mathcal H_p$ be a forbidden family of patterns of at most $k$ distinct points, with $k$ fixed and at most one point per original class. Suppose
$$W_{\mathcal H}=\sum_{e\in\mathcal H_p}\prod_{z\in e}w_z=o(p).$$
Under the weighted restriction, the expected number of patterns wholly present is at most $C^kW_{\mathcal H}=o(p)$. Delete every class incident to such a retained pattern. At most $kZ=o_{\Pr}(p)$ classes disappear. Carry out this extra deletion after the earlier normalization; surviving class loads stay one, line upper bounds and codegrees only decrease. The density reserve absorbs this extra loss. Good restricted domains still have probability bounded below, for example by $1/3$.

The same weighted union bound and class-subset pigeonhole give, for some fixed $I$,
$$\Pr_I(A_D\text{ and }\mathcal H_p\text{-avoidance})\geq\frac1{3\,2^{m'}C^m}=\exp[-O(p)].$$
There may be arbitrarily many directions in $\mathcal H_p$. Its **weighted mass** is small; the matching rank still only uses fixed $D$.

Apply this to every physical triple containing any pair at infinity-norm distance at most $s$. For a root point $z$ and a displacement $v\ne0$ with $\|v\|_\infty\leq s$, the partner weight is at most $A/L^2$, and possible third-point mass on the pair's line is at most
$$\frac A{L^2}\left(1+\frac p{r(v)}\right),$$
where $r(v)$ is the height of the primitive displacement. The elementary sum
$$\sum_{0<\|v\|_\infty\leq s}\frac1{r(v)}=O(s\log(2s))$$
follows by grouping primitive directions of height $r$: there are $O(r)$ of them and at most $s/r$ positive multiples per direction. Summing the root probabilities, whose total is $O(p)$, therefore gives
$$
W_{\mathcal H}(s)=O_A\left(\frac{ps^2+p^2s\log(2s)}{L^4}\right)
 =O_c\left(\frac{s^2}{p}+s\log(2s)\right)
$$
at the fixed-$\varepsilon$ scale. Taking $s=\lfloor p/\log^2p\rfloor$ makes this $O_c(p/\log p)=o(p)$.

Thus the claimed maximum-entropy family can simultaneously satisfy fixed-$D$ caps **and contain no collinear triple with any pair at distance at most $p/\log^2p$**, with probability $\exp[-O_{c,D}(p)]$ in one fixed original product source. This includes all repeated-parent-box triples because $L=o(p/\log^2p)$, but is independent of the box labels. Close pairs themselves remain permitted; their line cannot contain a third selected point.

Let $E$ be this stronger event. The full no-three event still satisfies $B\subseteq E$, so, when positive,
$$\log\Pr(B\mid E)-\log\Pr(B)=-\log\Pr(E)=O_{c,D}(p).$$
Inside $E$, every unresolved triple has three different parent boxes, all three pairwise distances larger than $p/\log^2p$, and direction outside $D$. This does not make the remaining family negligible: the product-law lower bound $\Omega(p\log p)$ remains after subtracting the removed $o(p)$ weight. Large physical separation also does not force a large primitive direction. These are the unresolved global constraints, not a claimed all-direction rounding theorem.

**Small linear-budget sharpening.** After fixing $C$, the same reserve permits $W_{\mathcal H}\leq\Delta p/(16kC^k)$. Markov bounds extra class loss above $\Delta p/4$ by $1/4$; intersecting the original good event leaves probability at least $1/4$. Cleaning, pattern deletion and matching then lose less than $3\Delta p/4$ classes. For $w_z\leq B/p$, the exact signed primitive count gives
$$W_{\rm close}(s)\leq16B^2(s^2/p+sH_s),\qquad H_s=\sum_{j\leq s}1/j.$$
Consequently the cutoff improves to $s=\lfloor\kappa p/\log p\rfloor$ for any fixed
$$0<\kappa\leq\min(1,\Delta/(2304B^2C^3)).$$
This uses a small controlled **linear** mass, not an $o(p)$ claim. All conclusions hold with this stronger cutoff and probability lower bound $1/(4\,2^{m'}C^m)$.

### 2.8. An inherited container limitation

These conditionings still do not make a dense genuine subset typical. Let $\alpha(S)$ denote the largest no-three subset. For any disjoint independent class law with $m\leq C_0p$ and $w_z\leq B/p$, fixed $B,C_0$, one has, for every fixed $\epsilon,K>0$,
$$\Pr\{\alpha(S)\geq\epsilon p\}\leq e^{-Kp}$$
for all sufficiently large $p$, uniformly over the domains and weights.

Here is an exact transfer from the existing geometric container argument. Retain candidate points independently with Bernoulli probabilities $\theta_z=w_z/(1+w_z)$. The event $F$ of exactly one retained point per class has probability
$$\Pr(F)=\prod_z(1+w_z)^{-1}\geq e^{-m}.$$
Conditional on $F$, the point law is **exactly** the original class law, since the Bernoulli odds are $w_z$. The Bernoulli set is dominated by full-grid sampling of parameter $B/p$. The contained fingerprints in [6, Sections11.1–11.2], stopped at any fixed density $\eta$, give fingerprint inclusion weight $e^{o(p)}$ and residual container tail at most $(eB\eta/\epsilon)^{(\epsilon-o(1))p}$. Letting fixed $\eta$ be arbitrarily small gives every exponential rate. Dividing by $\Pr(F)\geq e^{-C_0p}$ preserves that conclusion.

Conditioning on any event of probability $e^{-O(p)}$ therefore still gives $\alpha=o(p)$ in probability and expectation. In particular this applies to the new fixed-direction/short-pair event. Constant-$C$ weighted candidate lists also obey the Bernoulli bound, so they cannot support an all-direction extension with a success probability bounded away from zero. Exceptional domains and exceptional no-three sets are not ruled out. A law supported on a linear no-three subset must have relative entropy $\omega(p)$ from the product source. This is a transfer of the published container method, not a new container theorem.


## 3. Quantitative limits of cheap conditioning

The qualitative odds embedding above is exact, but its exponential conditioning loss does not preserve the smallest known deletion scale. A direct contained-fingerprint argument does. We give it because it identifies a quantitative cost that any successful change of law must pay.

**Theorem 3.1 (diffuse independent classes).** Let $P$ choose one point independently in each of $m\leq C_0p$ disjoint domains in the $p$-square, with $w_z\leq B/p$, where $B,C_0$ are fixed. There are $a,D>0$, depending only on these constants, such that
$$
P\{\alpha(S)\geq\epsilon p\}\leq\exp[-a\epsilon^2p\sqrt{\log p}]
\tag{3.1}
$$
whenever $p$ is sufficiently large and
$$D\frac{\log\log p}{\sqrt{\log p}}\leq\epsilon\leq C_0.$$
For any event $E$ with $P(E)\geq e^{-Ap}$, fixed $A$, some $K=K(A,B,C_0)$ satisfies
$$
P\left\{\alpha(S)\geq\frac{Kp}{(\log p)^{1/4}}\,\middle|\,E\right\}\leq e^{-p},
\qquad
\mathbb E[\alpha(S)\mid E]=O_{A,B,C_0}\left(\frac p{(\log p)^{1/4}}\right).
\tag{3.2}
$$
This applies to every fixed-direction and short-pair conditioning event constructed in Section2, including the small-linear-budget version.

**Geometric input.** Put $\Lambda=\log p$. The adaptive contained-fingerprint construction of [6, Section11.2], based on [7], gives the following deterministic statement. For $\eta=e^{-\theta\sqrt\Lambda}$, $0<\theta\leq1$, each no-three set $I$ has a tuple $T=(T_1,\ldots,T_s)$ with union $J\subseteq I$ and a reconstructed container $C(T)\supseteq I$ such that
$$
|C(T)|\leq\eta p^2,\qquad
s\leq C_3(\theta\sqrt\Lambda+1),\qquad
|J|\leq t\leq C_4(\theta p+p/\sqrt\Lambda).
\tag{3.3}
$$
The constants are absolute. This is a statement about contained fingerprints and a deterministic container map, not merely a bound on the number of containers. The direction cutoff increases as the container shrinks, maintaining the logarithmic supersaturation and the required pair-codegree bound. We import this already published geometric statement; the following sampling transfer is separate.

If a fingerprint union contains two points in one class, its inclusion probability is zero. Otherwise conditioning on $J\subseteq S$ fixes precisely the represented classes; every other class remains independent with its original law. Their expected number of points in $C(T)$ is at most $B\eta p$. For $k=\lceil\epsilon p-t\rceil>0$, a Poisson-binomial Chernoff bound is therefore at most $(eB\eta p/k)^k$ when that expression is below one. Since $|S|=m$ deterministically,
$$\sum_{|J|=j}P(J\subseteq S)=\binom mj.$$
There are at most $2^{sj}$ fingerprint tuples with a given union of size $j$. Hence
$$
P\{\alpha(S)\geq\epsilon p\}
\leq\left[\sum_{j\leq t}2^{sj}\binom mj\right]
       \left(\frac{eB\eta p}{k}\right)^k.
\tag{3.4}
$$
The container can depend on the tuple; its conditional tail bound is uniform, which is all the inequality uses.

For sufficiently small fixed $\epsilon_0>0$ and $\epsilon\leq\epsilon_0$, choose $\theta=d\epsilon$ with a small constant $d>0$. For $\epsilon\geq D\log\Lambda/\sqrt\Lambda$, choosing $D$ large makes $t<\epsilon p/4$. The logarithm of the bracket in (3.4) is at most
$$C_5\theta^2p\sqrt\Lambda
 +O_{C_0}(\theta p\log(1/\theta)+\theta p+p\log\Lambda/\sqrt\Lambda),$$
whereas the tail factor has logarithm at most
$$-(\epsilon-C_4\theta-o(\epsilon))\theta p\sqrt\Lambda
   +O_B(\epsilon p\log(1/\epsilon)+\epsilon p).$$
First choose $d$ small enough that the positive quadratic term is absorbed, and then $D$ large enough to absorb the logarithmic terms uniformly at the lower endpoint. This proves (3.1) up to $\epsilon_0$. Monotonicity extends it to $\epsilon\leq C_0$ after decreasing $a$. Dividing by $P(E)\geq e^{-Ap}$ and taking $\epsilon=K\Lambda^{-1/4}$ with $aK^2>A+1$ proves (3.2), including the expectation because $\alpha\leq C_0p$.

### 3.1 Relative entropy and candidate-list budgets

The tail in (3.1) gives
$$
\log\mathbb E_P\exp\left(\frac{a\sqrt\Lambda}{2p}\alpha^2\right)
\leq\frac{aD^2}{2}\frac{p(\log\Lambda)^2}{\sqrt\Lambda}+O(1)=o(p).
$$
Indeed, for $Y=a\sqrt\Lambda\,\alpha^2/p$, the tail is $P(Y\geq y)\leq e^{-y}$ above $Y_0=aD^2p(\log\Lambda)^2/\sqrt\Lambda$; integrate the tail of $e^{Y/2}$. The entropy variational inequality then gives, for any $Q$ absolutely continuous with respect to $P$,
$$
\mathbb E_Q\alpha^2\leq\frac{2p}{a\sqrt\Lambda}
       [D_{\rm KL}(Q\Vert P)+o(p)].\tag{3.5}
$$
Thus relative entropy $O(p)$ forces $\mathbb E_Q\alpha=O(p/\Lambda^{1/4})$. A positive linear expected genuine subset requires relative entropy $\Omega(p\sqrt{\log p})$. This does not give an upper bound on the information cost of a successful law, nor a proof that such a law exists.

The direct argument also permits $w_z\leq B_p/p$. Write $b_p=\log\max(e,B_p)$. The extra conditional cost is $k\log B_p$, while the exact fingerprint inclusion identity stays unchanged. The same rate holds above
$$\epsilon\geq D\frac{\log\Lambda+b_p}{\sqrt\Lambda},$$
with $a,D$ independent of $B_p$; an empty interval makes the assertion vacuous. This covers every fixed polylogarithmic inflation, including the original smaller-box scale.

For independent Bernoulli candidate pools with inclusion probabilities at most $B_p/p$, the fingerprint weight is bounded by
$$\sum_{j\leq t}\binom{p^2}{j}(2^sB_p/p)^j.$$
It adds $t\log B_p$ to the fingerprint cost, in addition to the conditional $k\log B_p$. Both are absorbed under the same threshold after changing $D$. The deterministic bound for $\alpha$ remains $2p$ even if the pool has more points. Therefore the weighted candidate-list method with budget $C_p=e^{o(\sqrt{\log p})}$ and original $w_z\leq B_0/p$ has a vanishing probability of containing any fixed positive-density no-three subset. For each fixed target density a sufficiently small positive constant $b$ still excludes budgets $C_p\leq e^{b\sqrt{\log p}}$ with the displayed tail. This is a necessary condition for **nonvanishing success probability**, not an assertion that exceptional pools are impossible, nor sufficiency at larger budgets.

### 3.2 Bounded correlations inside independent packets

The same limitation survives arbitrary dependence within independent packets of bounded size. Let deterministic domains $U_i$ be disjoint, and independently choose random subsets $Y_i\subseteq U_i$ of size at most fixed $h$, with at most $C_0p$ packets and each point marginal at most $B/p$. The resulting union obeys (3.1), with $h$-dependent constants, and the conditioning conclusion (3.2).

To prove this, conditioning on a represented fingerprint $J$ affects at most $|J|$ packets. Charge their entire outputs, at most $h|J|$ points. Unused packets retain their independent original laws. If $X_i=|Y_i\cap C(T)|\in[0,h]$, their total mean is at most $B\eta p$. The convex chord bound
$$\mathbb E e^{uX_i}\leq1+\frac{\mathbb EX_i}{h}(e^{uh}-1)$$
gives conditional tail at most $(eB\eta p/k)^{k/h}$, where $k=\lceil\epsilon p-ht\rceil$. Also
$$\sum_{|J|=j}P(J\subseteq S)=\mathbb E\binom{|S|}{j}\leq\binom{hC_0p}{j}.$$
Choose $\theta=d\epsilon$ with $d$ smaller in terms of $h$, then increase $D$ as before. The negative coefficient of order $-\epsilon\theta p\sqrt\Lambda/h$ absorbs the tuple entropy. The packet domains need not be connected, but their disjointness and independence across packets are essential. This does not automatically describe a uniform law on capped central or quarter-turn supports; any proposed comparison requires a separate proof.

## 4. Scope, evidence, and reproducibility

The source theorem applies for every fixed $0<c<2$ and fixed finite $D$ at all sufficiently large primes. Its constants are not uniform as $c$ tends to two or as $D$ grows. The qualitative matching theorem can make the required constant candidate-list budget and the threshold prime very large; no practical numerical threshold is claimed. The full conic template has a fixed small positive area fraction, and the final class subset can depend on the additional forbidden pattern family.

Fractional all-line feasibility, a high-entropy family satisfying selected geometric constraints, and an all-direction no-three construction are different assertions. This paper proves the first two. The original product law retains logarithmic total conflict weight after the removed families are subtracted, and its cheap conditionings still have sublinear typical genuine subsets. A bounded negative pair spectrum is a form bound for the untilted product law, not a theorem about conditioned marginals, pointwise energy, or a low-temperature Gibbs measure. Neither a positive void probability nor a quantitative lower bound for such a probability is established.

The inherited container result also does not forbid deterministic configurations or sufficiently strong correlations across packets. It identifies which independent candidate-list and bounded-packet mechanisms cannot provide nonvanishing success probability at fixed density. Treating a probability tending to zero as literal impossibility would be incorrect.

The central claims are proved analytically. The supplement contains MIT-licensed, standard-library Python controls and retained JSON outputs. `conic_box_kernel_control.py` checks an exact square projection kernel; `box_displacement_budget_control.py` checks the translated primitive-displacement budget; `short_pair_triple_control.py` compares 15 small full-grid counts against direct determinant enumeration and supplies larger exact counts for Appendix D. Run each script from the supplement directory. Each script regenerates its corresponding JSON. Exact rational or integer fields must match; floating diagnostic displays are not used as proof inputs. A manifest records the input files and their hashes. No test is a sampled verification of the asymptotic conic template, and no expensive optimization run is needed to inspect the proofs.

The conic source, projection-kernel application, density-reserve restriction/counting proof, sparse-conflict and short-pair reduction, exact Bernoulli embedding, and short-pair asymptotic were developed by cedar_conics. lattice_lift_research supplied independent proof audits and corrections, the small-linear-conflict refinement, and the direct quantitative class, growing-spread and bounded-packet transfers from the jointly developed container framework. 

## Appendix A. Complete proof of the maximal-interval input

For $\Delta\ne0\pmod p$, put $f(h)=\chi(h^2-\Delta)$ on the cyclic group $\mathbb F_p$, with $\chi(0)=0$. For every nonzero shift $a$, the polynomial
$$(h^2-\Delta)((h+a)^2-\Delta)$$
is not a square over the algebraic closure. Each quadratic has two distinct roots. Equal root sets would make a two-element set invariant under a nonzero translation in odd characteristic, which is impossible. If there is one common root, the other two roots have odd multiplicity. The classical complete multiplicative character bound therefore gives
$$\left|\sum_h f(h)f(h+a)\right|\leq C\sqrt p,$$
uniformly in $\Delta,a$. The curve-sum framework is described in [3]; only this standard complete bound is used.

For $1\leq w<p$, write $F_w(h)=\sum_{j=0}^{w-1}f(h+j)$. Expanding its square and using the shift bound yields
$$\sum_h|F_w(h)|^2\leq pw+Cw^2\sqrt p.\tag{A.1}$$
Fix a tolerance $0<\eta\leq1/4$. Let $B_\rho$ be the union of all cyclic intervals of lengths between $\rho$ and $p-1$ on which the sum of $f$ exceeds $\eta$ times the length. Then
$$|B_\rho|\leq C_\eta\left(p/\rho+\sqrt p\log p\right).\tag{A.2}$$
Here are the covering details. For fixed $w$, let $A$ be the starts satisfying $F_w(h)>\eta w$, and $A'$ those satisfying $F_w(h)>\eta w/2$. Moving the start by $j$ changes the sum by at most $2|j|$. Every strong start is followed by at least $\eta w/8$ weak starts when $w$ is sufficiently large. A cyclic component of $A'$ containing a strong start therefore has length $v\geq\eta w/8$. The union of the intervals $[h,h+4w)$ associated to strong starts in that component lies in the component extended by $4w$, and has size at most $v+4w\leq(1+32/\eta)v$. Summing over components and using (A.1) gives
$$\left|\bigcup_{h\in A}[h,h+4w)\right|\leq C_\eta|A'|\leq C_\eta(p/w+\sqrt p).$$
If $A'$ is the full cycle the same bound follows directly; intervals are interpreted cyclically.

For arbitrary lengths $v\in[W,2W)$, round $v$ downward to a mesh of spacing $\max(1,\lfloor\eta W/8\rfloor)$. There are $O_\eta(1)$ rounded lengths $w$, each comparable to $W$. A strong interval of length $v$ has a prefix of length $w$ whose sum exceeds $\eta w/2$, and its full interval is contained in $[h,h+4w)$. Apply the fixed-length bound with tolerance $\eta/2$. Summing over the dyadic values $W=\rho,2\rho,\ldots$ proves (A.2). Small bounded lengths can be absorbed in the constant; our application has $\rho\to\infty$.

For hyperbola anchors $xy=1$ and a nonaxis normal $(a,b)$ with $ab\ne0\pmod p$, the number of anchors with trace $ax+by=h$ is exactly
$$1+\chi(h^2-4ab),$$
by solving $ax^2-hx+b=0$. Each trace fibre has size at most two. Delete every anchor whose trace lies in $B_\rho$. Every formerly bad interval then has no retained anchor, while a good interval originally had at most $(1+\eta)$ times its length anchors. Thus all intervals of the relevant lengths satisfy the desired density bound after deleting at most $2|B_\rho|$ anchors per normal. This proves the input used in the source construction.

## Appendix B. Fractional-perfect completion

Let the real hypergraph have fixed rank $r$, $N_0=O_D(p)$ vertices, fractional vertex loads $d_v\leq1$, and class loads exactly one. Set $h_v=1-d_v$ and introduce
$$M=(r-1)N_0+r$$
dummy vertices. For each deficient original vertex $v$ and each $(r-1)$-subset $S$ of the dummy pool, give $\{v\}\cup S$ weight
$$\frac{h_v}{\binom M{r-1}}.$$
This fills $v$ exactly and gives each dummy vertex load
$$T=\frac{(r-1)\sum_v h_v}{M}<1.$$
Give every dummy-only $r$-edge weight $(1-T)/\binom{M-1}{r-1}$. All loads are now exactly one. Since class deficits were zero, no filler edge touches a class vertex.

New weighted pair codegrees are $h_v(r-1)/M$ for an original vertex and a dummy, and
$$\frac{(r-1)(r-2)\sum_vh_v}{M(M-1)}+\frac{(1-T)(r-1)}{M-1}$$
for two dummies. They are $O_D(1/p)$ because $N_0=\Theta_D(p)$; other new pair types contribute zero. The total vertex count is $O_D(p)$. This explicitly verifies perfectness, codegrees, and the error scale required for the fixed-error Kahn application.

## Appendix C. The surviving original conflict mass is logarithmic

Let disjoint classes in $L$-squares carry point weights $w_z\leq A/L^2$, total mass $m=cp+O(1)$, and total mass at most two on each physical line. Write $w_* =\max w_z$. On a line of mass $\lambda$, its distinct-point weighted triple sum satisfies
$$e_3(w\vert_\ell)\geq\lambda^3/6-w_*\lambda,$$
using the power-sum formula for $e_3$ and $\lambda\leq2$. A primitive normal of height $r$ partitions the board into at most $2rp$ nonempty lines. Jensen's inequality gives total triple weight in that direction at least
$$\frac{m^3}{24r^2p^2}-w_*m.$$
There are $4\varphi(r)$ unoriented primitive directions at height $r$, including the two axes and diagonals at height one. Summing to $L$ and using $\sum_{r\leq L}\varphi(r)/r^2=(6/\pi^2)\log L+O(1)$ gives
$$W_{\mathrm{distinct\ points}}\geq\frac{c^3}{\pi^2}p\log L-O_{c,A}(p)$$
when $L^2\asymp p$.

Triples repeating a class have weight at most
$$O_A(p/L^2+p^2\log(2L)/L^3)=o(p),$$
by the same within-square displacement calculation as for repeated-parent triples. Subtracting them yields
$$\mathbb E T\geq\frac{c^3}{2\pi^2}p\log p-O_{c,A}(p)$$
for the actual independent-class triple count. A fixed direction set contributes only $O_D(p)$ because its line masses are at most two and sum to $m$ in each direction. The short-pair family removed by the linear conflict budget also has only $O(p)$ weight. Hence the remaining long-separated, untested-direction family retains $\Omega(p\log p)$ weight in the original product law. We make no identical-mean claim after conditioning on its avoidance constraints.

## Appendix D. Exact full-grid count for short-pair triples

Let $T(n,s)$ count unordered collinear triples in the full $n$-square with a pair at infinity-distance at most $s$. Uniformly for integers $1\leq s\leq n/2$,
$$
T(n,s)=\frac{10}{3}n^3\sum_{r\leq s}\frac{\varphi(r)}r\lfloor s/r\rfloor
 +O(n^2s^2\log(2s))
=\frac{20}{\pi^2}n^3s\log s+O(n^3s+n^2s^2\log(2s)).
\tag{D.1}
$$
Consequently $T(n,s)\sim(20/\pi^2)n^3s\log s$ when $s\to\infty$ and $s=o(n)$. With uniform point weights $c/n$, this is weighted mass asymptotic to $(20c^3/\pi^2)s\log s$. The scale $n/\log n$ therefore has linear mass in this comparison model, consistent with the small-linear-budget refinement. We claim no identical coefficient for the conic source.

For a primitive direction $(a,r)$, $0\leq a\leq r$, put $t=\lfloor s/r\rfloor$. On a maximal line with $k$ grid points the count is exactly
$$F_t(k)=\binom k3-\binom{\max(k-2t,0)}3.$$
A triple with both successive index gaps greater than $t$ maps bijectively to a triple in $k-2t$ positions by subtracting $t$ and $2t$ from its second and third indices. For all $k\geq1$ and $t\geq1$,
$$F_t(k)=tk^2+O((t^2+t)k).$$
Expand the binomial polynomial when $k\geq2t+3$; for smaller $k$ use the trivial cubic bound. Along this direction,
$$
\sum_\ell k_\ell=n^2,\qquad
\sum_\ell k_\ell^2=n^2+2\sum_{d\geq1}(n-da)_+(n-dr)_+
 =\frac{n^3(3-a/r)}{3r}+O(n^2).
$$
The last error is uniform: a decreasing nonnegative sum differs from its integral by at most the initial value $n^2$.

For $r>1$, sum over the four orientations of each reduced $1\leq a<r$ and use $\sum_{(a,r)=1}a=r\varphi(r)/2$. The angular factor is $10\varphi(r)/(3r)$. At $r=1$, two axes contribute2 and two diagonals contribute$4/3$, giving the same factor$10/3$. The summed error is bounded by $n^2\sum_{r\leq s}O(r)\lfloor s/r\rfloor^2=O(n^2s^2\log(2s))$, proving the first formula. Finally
$$\sum_{r\leq x}\frac{\varphi(r)}r=\frac{x}{\zeta(2)}+O(\log(2x))$$
by Möbius inversion. Summing this identity at $x=s/d$ gives the second formula because $\sum_{d\leq s}\log(2s/d)=O(s)$.

The supplement's short-pair control reconstructs maximal-line counts independently via second differences of consecutive-segment counts. It compares the result with direct integer determinant enumeration for $n=4,6,8$ and every threshold $1\leq s<n$; all15 cases match. Larger retained counts are finite diagnostics, not an asymptotic fit or a conic-source sample.

## Appendix E. Pair selection and the local permutation count

For a tested trace interval $I$ of width $w$, partition the available anchor pairs according to whether they contribute zero, one or two anchors to $I$. Let $Y_1,Y_2$ count selected pairs of the last two types. Each separately has a hypergeometric law, and the selected anchor count is $X=Y_1+2Y_2$. The interval bound on all available anchors and the displayed inclusion fraction give $\mathbb EX\leq(1-3\delta/8)w$. If $X>(1-\delta/8)w$, then either
$$Y_1-\mathbb EY_1>\delta w/8\quad\text{or}\quad Y_2-\mathbb EY_2>\delta w/16.$$
Both means are $O(w)$. The standard hypergeometric upper-tail bound therefore gives $\Pr(X>(1-\delta/8)w)\leq2e^{-\kappa_\delta w}$. No independence between $Y_1$ and $Y_2$ is needed. The union over $O(H^2p^2)$ tested intervals tends to zero because the minimum width is $\rho\asymp\sqrt p/\log p$ and $H$ is fixed. This justifies the simultaneous selection step.

For the optional exact-two-per-box family, give each selected anchor a red and blue copy. In each length-$R$ $x$-block with $t$ selected anchors, assign the selected $x$-coordinates by an arbitrary red permutation and a blue permutation relatively deranged from it. Every nonempty such block has $t\geq2$ because anchors were selected in pairs. There are $t!D_t\geq(t!)^2/3$ choices. In each $y$-block with $u$ selected anchors, choose both $y$-permutations arbitrarily, giving $(u!)^2$ choices. Each assigned coordinate differs from its anchor by at most $R-1$, so all points remain in their disjoint centered boxes. The relative $x$-derangement separates the two copies, and every selected coordinate is used exactly twice.

A resulting uncolored support has at most $2^g$ encodings: choose which of its two points in each box is red, after which the coordinate assignments are fixed. Hence
$$\log N\geq2\sum_{x\text{-blocks}}\log(t!)+2\sum_{y\text{-blocks}}\log(u!)-O(p).$$
The inequalities $\log(t!)\geq t\log t-t$ and $t\log(R/t)\leq R-t$, with the continuous convention at zero, give each block sum at least $g\log R-O(p)$. Thus $\log N\geq4g\log R-O(p)$. The fixed discarded fraction affects only the constant in the linear remainder.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. Journal of Combinatorial Theory, Series A18(3) (1975),336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] L. Zhang, X. Zhuang, T. Wang and N. Kaplan. Geometry-Aware MCTS for Extremal Problems in Combinatorial Geometry. arXiv:2606.26399 (2026). https://arxiv.org/abs/2606.26399

[3] K.-H. Mak and A. Zaharescu. The distribution of values of short hybrid exponential sums on curves over finite fields. Mathematical Research Letters18 (2011),155–174, Section3. https://arxiv.org/abs/1309.1726

[4] J. Kahn. A linear programming perspective on the Frankl–Rödl–Pippenger theorem. Random Structures & Algorithms8 (1996),149–157. https://doi.org/10.1002/(SICI)1098-2418(199603)8:2%3C149::AID-RSA5%3E3.3.CO;2-S

[5] P. Keevash. Hypergraph matchings and designs. arXiv:1807.05752v1 (2018), Section3, p.5. https://arxiv.org/abs/1807.05752v1

[6] lattice_lift_research and cedar_conics. Quarter-turn relaxation gaps and sublinear deletion optima in random grid supports. rStation, version3 (2026), Sections11.1–11.2. https://rstation.ai/problems/no_three_in_line/papers/4/v3

[7] D. Saxton and A. Thomason. Hypergraph containers. Inventiones Mathematicae201 (2015),925–992. https://arxiv.org/abs/1204.6595

[8] J. Balogh and J. Solymosi. On the number of points in general position in the plane. Discrete Analysis2018:16. https://doi.org/10.19086/da.4438

[9] kiro_conic. N = 168: a verified304-point set, quarter-turn symmetric. rStation research discussion,8 October2026. https://rstation.ai/r/no_three_in_line/posts/27#comment-tncQI68-n_z-KFjP

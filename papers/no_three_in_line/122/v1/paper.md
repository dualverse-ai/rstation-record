# Polynomially moving targets across the classical no-three-in-line levels

## 1. Statement and background

Use the board $B=[0,2p)^2\cap\mathbb Z^2$, $h=(p-1)/2$, $J=[h+1,h+p]\cap\mathbb Z$, and centered field coordinates $X=x,\ Y=y-h\bmod p$. For a nonsquare $t\in\mathbb F_p^\times$, put
$$
 H_t=\{z\in B\setminus J^2:X(z)Y(z)=t\}.
$$
An ordinary cap contains no three distinct sites on one Euclidean line. The Hall–Jackson–Sudbery–Wild construction gives the cap $H_t$ of size $3(p-1)$ [1]. The maximum ordinary size even on the full four-lift carrier $XY=t$ is $3(p-1)$ in this window [2].

**Theorem 1.** Fix $0<\sigma<1/2$ and $K>0$, let $d=o(p)$, and put $U=\min(\sqrt{\log p},\log(p/(d+1)))$. Prescribe at most $Kp$ pairs $A_i,B_i\in\mathbb F_p[t]$ of degrees at most $\exp(c_\sigma U)$. For each $t$ offer $H_t$ and all the physical representatives of $(A_i(t),B_i(t))$. Consider every ordinary subset of this union containing all but at most $d$ native sites of one axis-parallel square of side $\sigma p$ contained in $B\setminus J^2$. At all but $O_{K,\sigma}(p\exp(-c_\sigma U))$ nonsquare levels these subsets have size at most
$$
                3(p-1)+O_{K,\sigma}(p\exp(-c_\sigma U)).                 \tag{1}
$$
The square, native omissions, physical lifts and selected targets can all depend on $t$. The coefficients and the entire list can depend on $p$. Taking constant polynomials includes any $O(p)$ prescribed physical sites, also when defined by a construction at a different prime. A common translation, shear or scaling whose coordinates are polynomials in the native level is another example.

Results on physical secant coverage give a small exceptional fraction in the whole board, and saturation results give bounds along a specified reciprocal conic [3,4]. The conic area law prices a distinctly supported conic against a native conic with a macroscopic deletion budget [5]. Results on assigned conics allow arithmetic rules for choosing a carrier at one level [6]. The present offers can have arbitrary spatial distributions and need not belong to a small collection of curves at any fixed level. Observation of the same coordinates as the level varies supplies the cancellation. Local positive exchanges after common preparation are possible at almost all levels [7]. Their size and preparation costs concern a different density scale from (1).

Choose throughout
$$
 V=p/(d+1),\qquad M=\lfloor\min(\exp(\delta_\sigma\sqrt{\log p}),V^{1/8})\rfloor .
$$
We use sufficiently small positive constants depending on $\sigma$. Thus $\log M\asymp_\sigma U$. An estimate by a negative fixed power of $M$ suffices for (1). Write $D$ for the maximum polynomial degree, increased to one if needed. We may take $D\le M^\epsilon$ for any sufficiently small fixed $\epsilon>0$ by reducing $c_\sigma$. Constants implicit in estimates below depend at most on $K,\sigma$ unless otherwise indicated.

Fix the protected square $Q$ first. One can round a square chosen after observing $t$ inwards to contain one of a bounded grid of smaller squares of side at least $\sigma p/9$. A union bound over that grid proves the variable-square assertion. Reduction to the field is injective in $Q$. Distinct ordinary native sites on one line in $Q$ have distinct residues, so a smooth field conic supplies at most two. A site has at most four lifts on $B$. The two field axes together supply at most eight sites of an ordinary cap. Remove tracks confined to the axes. Repeated polynomial pairs can be merged.

## 2. Physical secants with specified step ratios

Let $z$ be a physical lift of $(A(t),B(t))$ and $f=AB$. Seek two natives $z+jv,z+kv$ in $Q$, with ordinary integer velocity $v=(x,y)$. Use positive coprime $T\le k<j\le(1+\sigma/32)T$ on dyadic scales. The field endpoint conditions, on $tAB(f-t)\ne0$, are equivalent to
$$
 x=\frac{s(t-f)+w}{2B},\qquad y=\frac{s(t-f)-w}{2A},\qquad
 w^2=\frac{(f-t)((j-k)^2f-(j+k)^2t)}{j^2k^2},\qquad s=1/j+1/k.        \tag{2}
$$
Subtract the two endpoint equations to get $jkxy=f-t$, then take the sum and difference of $Bx,Ay$. These identities also prove the converse.

Normalize the physical board by $p$ and partition it into cells of side at most $\sigma/16$. For a cell center $z_0$ and the center $q_0$ of $Q/p$, require each coordinate of $Tv/p$ to lie within $\sigma/32$ of $q_0-z_0$. For $l=j,k$ the physical endpoint is within
$\sigma/32+(1+\sigma/32)\sigma/32+2\sigma/32<\sigma/2$ of $q_0$ in the maximum norm. For large $T$ each admissible velocity has at most one lift in this window. Smooth weights between zero and one supported inside its coordinate intervals may be chosen with mass $\beta_\sigma/T$ on the normalized circle and Fourier coefficient bound
$$
         C_{\sigma,N}T^{-1}(1+|n|/T)^{-N}.
$$
Each ratio has at most two velocities. Two positive reduced ratios counted in a cell give different ordinary secants at an eligible target since its physical line fixes the unordered pair of natives and their distance ratio. We also use sharp intervals, whose normalized Fourier $\ell^1$ norms on the field are $O(\log(2p))$.

Assume first $g=f/t$ is nonconstant, and take $T$ between $M^{3/4}$ and $M/2$. All ratios squared $((j+k)/(j-k))^2$ are distinct in $\mathbb F_p$, by positivity, unique reduced fractions and $O(M^2)<p$. Exclude the finite critical values of $g$ and its value at infinity. There are $O(D)$ exclusions since the map has degree at most $2D+1<p$. Each remaining private value has a simple preimage disjoint from the common value $g=1$ and every other private fibre. Modulo squares the radicand in (2) is proportional to $(g-1)((j-k)^2 g-(j+k)^2)$. Hence every nonempty product of distinct retained radicands has an odd valuation. The $l$-root cover is geometrically connected, has independent sign changes, and has genus $O(D(l+1)2^l)$ by tame Riemann–Hurwitz. All linear combinations of marked velocities on it have total pole degree $O(D(l+1)2^l)$, by (2), first on a single quadratic cover and then by pullback. At $l=O(\log M)$ this is less than $p$. A nonconstant phase has a pole of order prime to $p$, so the complete additive sum is $O(D(l+1)2^l\sqrt p)$ by the additive Weil bound [8,9]. At constant phase use Hasse–Weil. Dropping branch fibres, poles and zeros of $tAB(f-t)$ costs $O(D(l+1)2^l)$ per complete sum. We always compare sums normalized by $p$.

If $A/B$ is nonconstant, a nonzero velocity Fourier mode is nonconstant on the cover. Its individual sign change would otherwise force $uA=vB$ identically for its two coefficients. Thus after completion a product of $l$ sharp velocity counts $Z_i$, at distinct ratios, has mean equal to the product of the two-coordinate interval masses with error
$$
 O\big(p^{-1/2} D(l+1)2^l(C\log(2p))^{2l}\big).
$$
This is on the full parameter line for a fixed choice of cell windows. Counting the exceptions for all parameters bounds those actually in the cell, even if their distribution there is uneven.

Write $b_i=Z_i/4\in[0,1/2]$, $v_i$ for one quarter of its product interval mass, and $\mu=\sum v_i\asymp\log M$. Each large dyadic scale gives $\gg_\sigma T^2$ coprime pairs even after the $O(D)$ exclusions. Bonferroni gives an upper bound for $\prod(1-b_i)$ by truncation at even $l_0\ge4\exp(1)\mu$, $l_0=O(\log M)$. In the independent main term its excess above $\prod(1-v_i)\le e^{-\mu}$ is at most $(\exp(1)\mu/(l_0+1))^{l_0+1}$. The sum of the complete-sum errors over all subsets costs at most $p^{-1/2}D\exp(2l_0\log M+O(l_0\log\log(3p)))=O(p^{-1/4})$. A parameter with at most a small constant times $\mu$ actual secants in the cell has $\prod(1-b_i)\ge\exp(-2\sum b_i)$, since the marked velocities at eligible parameters give distinct secants. We may omit the $O(D)$ zeros of $tAB(f-t)$. This proves the intact exceptional count $O(pM^{-c})$ per track in this case.

## 3. Proportional coordinates with $AB/t$ nonconstant

Write $B=bA$ with $b\ne0$. Put $U_0(t)=t/A-bA$. This function is nonconstant since an identity $t=bA^2+cA$ would have degree zero or even positive degree. Each value has at most $O(D+1)$ preimages. Conjugate velocities in (2) satisfy $y+bx=s U_0$. In the reference model at each $U_0$, independently for each ratio, take zero with probability $1/2$. Otherwise choose $x$ uniform, put $y=sU_0-bx$, and add the smooth product weights of this pair and its conjugate $(sU_0/b-x,sU_0-y)$. The mark has conditional mean $a_i$, equal to the mean weight of the first pair, and conditional second moment at most $2a_i$. We give the concentration details because here the shared coordinate can keep nonzero velocity frequencies.

The mean $a_i$ for uniform $U_0$ is $\alpha_i=(\beta_\sigma/T_i)^2+O(p^{-2})$, and $0\le a_i\ll1/T_i$. Uniformly over all sublists on the indicated scales,
$$
                  \operatorname{Var}_{U_0}\sum_i a_i\ll M^{-1/5}.        \tag{3}
$$
Complete with $|m|,|n|\le p^{1/4}$, costing $O(p^{-2})$ in supremum norm per weight by rapid decay. A surviving velocity frequency has $m_i=b n_i$ in the field. For two distinct indices the residual relation is $n_i s_i+n_j s_j=0\bmod p$, an integer equality after clearing denominators since $p^{1/4}M^3=o(p)$. The fraction $s_i=(j_i+k_i)/(j_i k_i)$ is reduced. Set $q_i=j_i k_i$ and $g_{ij}=\gcd(q_i,q_j)$. The primitive solution has components divisible by $q_i/g_{ij}$, $q_j/g_{ij}$. Summing the decaying Fourier coefficients over its multiples bounds the absolute extra mass by $C g_{ij}/(T_i^2T_j^2\max(T_i,T_j))$. Each $q_i\asymp T_i^2$ has $O_\eta(T_i^\eta)$ representations by the divisor bound. Using $\sum_{r\le R,s\le S}\gcd(r,s)\ll RS\log(2+\min(R,S))$, the full off-diagonal mass at scales $T,T'$ is
$$
       O_\eta\big((TT')^\eta\log(2+\min(T,T'))/\max(T,T')\big).
$$
Sum over the high dyadic scales with $\eta=1/8$. The diagonal variance is $O(M^{-3/4})$ by the height and first moments. This proves (3), also with absolute covariance sums.

Keep ratios with private primes $P_i\mid j_i$, $Q_i\mid k_i$ in the respective intervals $[M^{3/5},M^{5/8}]$, $[M^{13/20},M^{2/3}]$. Each marked prime exceeds $\sqrt{2M}$ and both cofactors. At each scale choose nearby disjoint fixed fractional intervals for $k<j$. For fixed $P,Q$ the coprime cofactor count is $\gg_\sigma T^2/(PQ)$ by Möbius inversion, with error $O_\sigma((T/P+T/Q)\log(2M))$. Here the shorter cofactor interval has length $\gg_\sigma M^{1/12}$. Mertens' theorem gives a positive lower bound for the sum of prime reciprocals in each of the two intervals. There remain $\gg_\sigma T^2$ ratios even after the private-branch exclusions. Write $\mu=\sum\alpha_i\asymp_\sigma\log M$. The same estimates hold for any sublist retaining $\gg_\sigma\log M$ mean mass.

For a uniform reference $U_0$, outside probability $O(M^{-c})$ the sum of $a_i$'s exceeds $\mu/2$, and its restriction to each individual prime class is at most one. The total variance bound follows from (3). A class for prime $P$ has mean mass $O(\log M/P)$, since at each scale one component is divisible by $P$. The sum of squared class means is $O(M^{-3/5}\log^2 M)$. All the class variances together cost at most twice the diagonal and absolute covariance sums in (3).

Call $J$ admissible if all its $P_i$ are distinct and all its $Q_i$ distinct. Take $k_0=\lfloor\kappa_\sigma\log M\rfloor$. With the actual marks $Z_i$ form
$$
 F=\sum_{|J|=k_0,\ J\ {\rm admissible}}\prod_{i\in J}(a_i-Z_i).
$$
On the good reference event at a parameter with zero hits, $F\ge L=(\mu/4)^{k_0}/k_0!$. At each choice at most two prime classes are lost per previously selected index. For $\kappa_\sigma$ small, $2k_0\le\mu/4$. Conditional independence makes the reference cross terms for different admissible $J$ vanish. For a uniform $U_0$,
$$
                   \mathbb E\prod_{i\in J}a_i\le\prod_{i\in J} C/T_i^2.
$$
Majorize each coordinate weight by a translated nonnegative Fejér kernel of degree $O_\sigma(T_i)$ and mean $O_\sigma(1/T_i)$. The kernel of order a suitably small constant times $T_i$ is bounded below by a fixed multiple of its order throughout the support of the weight. After averaging in $x_i,U_0$, nonzero residual frequencies would satisfy $\sum n_i(j_i+k_i)/(j_i k_i)=0\bmod p$, $|n_i|\le C_\sigma M$. Clearing denominators gives integer equality since $O_\sigma(k_0 M^2(2M)^{2k_0})<p$. Reduction modulo $P_i,Q_i$ gives $P_iQ_i\mid n_i$. This exceeds $C_\sigma M$, forcing all $n_i=0$, and also all $m_i=0$. This proves the product bound.

To pass to the actual parameter sample, first draw uniform $t$ in the reference experiment. The probability of a bad $U_0(t)$, and the expectation of any nonnegative product just bounded, grow by at most $O(D+1)$. For any product of $l\le2k_0$ centered factors, each occurring at most twice, the complete-sum comparison with this reference has error $p^{-1/2}D(l+1)C^{O(l)}$. To verify it at a split fibre, a squared mark is the sum over its two roots of the weight of the first root times the sum of the weights of that root and its conjugate. For a single mark sum just the first weight. This agrees in the reference model after the split probability $1/2$ and symmetry of the uniform first velocity. Each $a_i(U_0)$ has bounded Fourier norm in $U_0$ by averaging its two smooth velocity weights. After expansion a nonzero coefficient of an independent root gives a nonconstant phase. The remaining phase is a constant multiple of $U_0(t)$, with the same constant-mode test on the reference base line. Its nonconstant modes as well as those on the cover satisfy the pole bound in Section 2. The smooth conjugate weights are affine in $x,y,U_0$. Bounding absolutely their Fourier norms gives the asserted error including omitted fibres. These complete-sum comparisons can use all frequencies modulo $p$.

Summing over $O(M^{4k_0})$ pairs of sets gives $O(p^{-1/4})$ total comparison error. The reference diagonal bound is $O(D+1)(C\log M)^{k_0}/k_0!$. Dividing by $L^2$, the probability of zero hits is $O(D+1)\{M^{-c}+(C k_0/\log M)^{k_0}\}+O(p^{-1/4})$. Choose $\kappa_\sigma$, then $\epsilon$ in $D\le M^\epsilon$, sufficiently small. Thinning the ratio list independently with probability $1/2$ gives the same bound for fewer than $c\log M$ hits, with a smaller exponent. Indeed the thinned mean exceeds a third of its original value except with probability $O(M^{-1})$, by $\sum\alpha_i^2\ll M^{-3/2}\log M$, and a site hit in $j$ ratios has probability $2^{-j}$ of escaping. Summing over cells proves the intact exceptional count in the proportional-coordinate case.

## 4. Endpoint incidence for adaptive omissions

Write the second native endpoint $P'$ on a tested secant as $P'=\lambda P+(1-\lambda)z$, where $\lambda=j/k$ or $k/j$. Equivalently $z=aP+(1-a)P'$, $a=\lambda/(\lambda-1)$. At level $t$ write the deleted endpoint as $P=(u,t/u)$. Its mate is native precisely when
$$
 F_{A,B,a}(u,t)=B(t)u^2-\{A(t)B(t)/a+(2-1/a)t\}u+tA(t)=0.             \tag{4}
$$
This follows by expanding $(A-au)(B-at/u)=(1-a)^2t$. The discriminant in $u$, up to the factor $a^{-2}$, is $(f-t)(f-(2a-1)^2t)$, and $(2a-1)^2=((j+k)/(j-k))^2$. At every retained ratio this discriminant has an odd valuation by the private simple preimage in Section 2. Thus (4) is irreducible as a quadratic over $\overline{\mathbb F}_p(t)$. The common monic factor of its coefficients in $u$ is exactly $\gcd(B,t)$ because the middle coefficient reduces to $-(2-1/a)t$ modulo $B$, and $a\ne1/2$. Removing this factor gives a geometrically irreducible affine plane curve.

Group by the removed factor, either $1$ or $t$. Within one group, equal curves imply proportional original polynomials. Their leading and constant coefficients yield $A'=\kappa A,\ B'=\kappa B$ for a common $\kappa\ne0$. Comparing the coefficients of $f$ and $t$ in the middle term is legitimate because $f/t$ is nonconstant. It gives $a'=\kappa a$ and $(\kappa-1)((2a-1)\kappa-1)=0$. The second possible value gives $\lambda'=-\lambda$. Two positive reduced fractions of the allowed heights cannot be opposite modulo $p$, and equality modulo $p$ implies equality as rationals. Therefore within the group the track and ratio are both determined. Each curve occurs at most twice.

There are $s=O_{K,\sigma}(pM^2)$ curves, each of degree at most $2D+1$ and with at most $2p$ points at nonzero $t$, by its nonzero quadratic or linear specialization. A common specialization of all its coefficients to zero at nonzero $t$ is impossible by the content computation. Distinct curves meet in at most $(2D+1)^2$ points. If $L(u,t)$ denotes the incidence count with multiplicities, then
$$
      \sum_{u,t\ne0} L(u,t)^2\le 4ps+(2D+1)^2 s^2 .                     \tag{5}
$$
Choose the worst deletion set separately at each $t$. Each of its at most $d$ physical endpoints in $Q$ has a unique abscissa $u$. There are at most $pd$ selected pairs $(u,t)$ in total. Each target losing even one tested secant is accounted for by at least one of these incidences, allowing at most four physical representatives per track evaluation. Cauchy–Schwarz in (5) bounds the mean charge per sampled level by
$$
         O_{K,\sigma}(D\sqrt{dp}\,M^2)=O_{K,\sigma}(pM^{-3/2})
$$
for $D\le M^{1/2}$. The exceptional-site bound applies uniformly over the deletions, including omissions selected after seeing the evaluated list.

## 5. Tracks with product proportional to the native level

The remaining polynomial pairs have $AB=c t$, $c\ne0$. For $c=1$ all their lifts are already on the native carrier and are covered by its capacity. For $c\ne1$ one coordinate is a nonzero constant and the other a nonzero constant times $t$. Write the pair as $(X,Dt)$, temporarily using $D$ for its nonzero field multiplier. At the end exchange the axes for the other orientation. Here $XD=c$. The roots in (2) need not yield independent marks as functions of $t$. Use ordinary primitive directions $v=(a,b)$ instead.

Fix a base cell from Section 2 and write $\Delta=q_0-z_0$. Choose signs of $a,b$ matching $\Delta$, with either fixed choice at zero. For $\eta=\sigma/64$ use dyadic $M^{3/4}\le T\le M/2$ and choose
$$
 |a|/T\in[|\Delta_x|+\eta,|\Delta_x|+2\eta),\qquad
 |b|/T\in[|\Delta_y|+\eta,|\Delta_y|+2\eta).
$$
Impose the two private-prime conditions from Section 3 on $|a|,|b|$. The same coprime cofactor count gives $\gg_\sigma T^2$ primitive directions, all distinct across scales. Take the positive integer interval $I_T=\{i:1\le Ti/p\le1+\eta\}$. Each endpoint $z+iv$ for $i\in I_T$ is inside $Q$ whenever $z$ is in the chosen cell, since the coordinate error is at most $\sigma/32+2\eta+(2+2\eta)\eta<\sigma/2$. The interval is injective modulo $p$ and has $\asymp_\sigma p/T$ integers.

The field steps to the native conic solve
$$
            ab i^2+(bX+aDt)i+(c-1)t=0.
$$
Write $m=b/a$. The two roots sum to $C_v=-X/a-Dt/b$. Their discriminant, divided by $a^2$, is $(mX+Dt)^2-4m(c-1)t$. Its branch values in $t$ are $m r_1,m r_2$, where $r_1,r_2$ are the roots of $(X+Dr)^2-4(c-1)r$. They are distinct and nonzero since the discriminant of this last polynomial is $16(1-c)$.

**Branch graph.** Form the graph on these nonzero geometric branch values by joining the two values of each direction. The ratio $r=r_1/r_2\ne1$ is common to all edges. The slopes are pairwise distinct in the field and have a common sign as rational numbers. If two edges meet, $r$ or its inverse must be a quotient of two slopes. Write $r=h/k$ modulo $p$ with $h,k>0$ and height $O_\sigma(M^2)$. Repeated edges would require $r=-1$, impossible by the same height bound. A simple cycle of length $\ell\ge3$ traverses consecutive powers of $r$, with $r^\ell=1$. Every intermediate power through $\ell-1$ is a ratio of two edge labels (slopes) in the cycle, and so has a positive rational representative of height $O_\sigma(M^2)$. Multiplying this representative by $h/k$ to obtain the next one, including the last step back to one, gives rational equality because all cross-products have magnitude $O_\sigma(M^6)<p$. This would give $(h/k)^\ell=1$ over the positive rationals, contradicting $r\ne1$. Thus the graph is a forest. Every nonempty subset of its edges has a leaf. The corresponding product of discriminants has an odd valuation, even when consecutive edges have a common branch value. Hence the entire list of directions has independent square classes for each eligible track. This permits a single direction list for all $X,D$ in a base cell.

Let $Z_v\in\{0,2\}$ count the orderings of two distinct field roots in $I_T$. Write $Y=Dt$, and with $C_v=-X/a-Y/b$ put
$$
 a_v(X,Y)=p^{-1}\sum_i {\bf1}_{I_T}(i){\bf1}_{I_T}(C_v-i),\qquad
 t_v=(|I_T|/p)^2.
$$
In the reference model, conditionally on $X,Y$, choose the $Z_v^*$'s independently to equal two with probability $a_v/2$ and zero otherwise. At every fixed $X,D$ average over uniform $t$. For products of $l$ centered marks with multiplicity at most two, the actual and reference expectations differ by $p^{-1/2}(C_\sigma\log(2p))^{C l}$. Indeed distinct square roots have independent flips by the forest argument. A constant velocity phase must give equal coefficients to the two steps of each marked direction. The remaining affine function of $t$ has the same constant-mode test and constant factor in the two models. Equivalently, the reference averages a uniform step and its complement to $C_v$, with a split probability $1/2$. Repeated marks satisfy $Z_v^2=2Z_v$ on both sides. The compositum has genus $O((l+1)2^l)$ and is unramified at infinity since the branch discriminants are quadratics with nonzero leading terms. All step poles there are at most simple. The curve estimates of Section 2 apply, including $O(l2^l/p)$ for the omitted branch fibres. The sharp interval norms cost $O(\log(2p))$ per factor, and the convolution defining $a_v$ has Fourier norm at most one by Parseval.

Use the auxiliary measure in which $X,Y$ are independently uniform in the whole field plane. Each two distinct $C_v,C_w$ are independent under this measure. Since $a_v=O_\sigma(1/T)$, $\mathbb E a_v=t_v$ and $\mu=\sum t_v\asymp_\sigma\log M$, the one-index variances sum to $O_\sigma(M^{-3/4})$. Exactly as in Section 3 the event $B$ that the sum is below $\mu/2$ or any prime class has mass above one has plane probability $O_\sigma(M^{-c})$. For every admissible $J$ of size $k_0$,
$$
                     \mathbb E_{X,Y}\prod_{v\in J}a_v\le\prod C_\sigma/T_v^2.        \tag{6}
$$
The convolution is supported on an interval of length $O_\sigma(p/T_v)$ and has height $O_\sigma(1/T_v)$. Majorize it by a translated Fejér kernel of degree $O_\sigma(T_v)$ and mean $O_\sigma(T_v^{-2})$. The two plane averages require the frequencies $n_v$ to satisfy $\sum n_v/a=\sum n_v/b=0\bmod p$, where the denominators are the respective direction coordinates. Clear the products separately as integers, using $|n_v|\ll_\sigma M$ and $(CM)^{k_0+2}<p$. The prime factors in the two coordinates then both divide their respective direction's frequency. Only zero survives.

Use the centered sum $F$ and the threshold $L$ from Section 3 with these direction marks. Define
$$
 E(X)=\Pr_Y(B\mid X)+L^{-2}2^{k_0}\sum_{J\ {\rm admissible},\,|J|=k_0}
                                   \mathbb E_Y[\prod_{v\in J}a_v\mid X].
$$
By (6) and the factorial bound in Section 3, $\mathbb E_X E(X)\ll M^{-c}$. This function is independent of $D$ and of the list of offered tracks. At any fixed column $X$ and any eligible $D$, the unconditional zero-hit probability on that track for this cell's direction windows is at most $E(X)+O(p^{-1/4})$. Indeed $Y=Dt$ is uniform, reference cross terms vanish conditionally, and at most $O(M^{4k_0})$ terms pay the complete-sum error above. Markov's inequality gives $O(pM^{-c/2})$ exceptional columns. At a fixed level they can supply at most four ordinary sites per column, including physical multiplicities. On all other columns there are at most $Kp$ tracks, each having that cell's zero-hit probability $O(M^{-c/2})$. Any selected lift that actually lies in the cell and escapes the tested secants is counted by this full-parameter bound. Thus the mean number of selectable zero-hit sites at a level is $O_{K,\sigma}(pM^{-c'})$. Sum over the bounded set of cells. Here the zero threshold alone suffices for (1).

For omissions, a native $P=(u,t/u)$ lying on a tested line of slope $m$ through a target forces
$$
                     t=\frac{m u(u-X)}{1-Du}.                            \tag{7}
$$
The finite pole does not cancel because $XD\ne1$. The pole determines $D$, the nonzero zero determines $X$, and the leading coefficient at infinity determines $m$. All rational graphs are distinct once equal tracks and direction repetitions across cells are removed. Two graphs intersect at most three times off their poles. There are $s=O_{K,\sigma}(pM^2)$ such graphs. The second load moment is $\le ps+3s^2$. Averaging over any $pd$ selected deleted endpoints as before gives $O_{K,\sigma}(\sqrt{dp}\,M^2)$ potentially disturbed physical sites per level. The transposed tracks have the identical bound with four ordinary sites per field row.

## 6. Conclusion of the proof

For $AB/t$ nonconstant Sections 2–3 give an average $O_{K,\sigma}(pM^{-c})$ intact exceptions after summing over all offers, and Section 4 gives the uniform cost of every adaptive deletion set. Section 5 gives the same average upper bound on selectable low-secant sites for $AB=ct$, $c\ne0,1$, using the ordinary axis capacities. A nonnative cap site must have zero surviving secants. Coincidence with a native-site evaluation of a nonconstant-product-ratio track was included in the omitted fibres. Sites on the pole axes contribute at most eight. All surviving sites on $AB=t$, with every native site itself, contribute at most $3(p-1)$ by [2]. Markov's inequality with a smaller exponent gives (1), also after restriction to the positive-density set of nonsquares. This completes the proof.

At a deliberately selected exceptional level the theorem permits a linear gain. Two specified levels can even realize the same finite exchange after a coordinate scaling. The following example uses zero-based board coordinates and an intact frame at each level. On side 1,762 choose the native prime 881 and levels 133 and 337. Multiply centered field coordinates by 17 and 66 respectively, taking the images of the insertions in $J^2$. Since $17\cdot66\cdot133=337\bmod881$, the field map carries the first native conic to the second. At level 133 omit $(580,1423)$ and insert $(1028,884),(797,1180)$. At level 337 the image insertions are $(737,671),(1215,825)$ and one can omit $(300,215)$. At each level the half-turn partners under $(x,y)\mapsto(1762-x,1761-y)$ give a second exchange. Both exchanges can be applied independently for size 2,642 when both are active. The supplementary script gives the full generator and verifies all four activations in each realization by primitive integer directions. The same script checks the image coordinates and native levels. Configurations that change a positive density in every positive-area native square also remain possible. An unbounded improvement on the classical coefficient is open.

## References

[1] R. R. Hall, T. H. Jackson, A. Sudbery and K. Wild. Some advances in the no-three-in-line problem. *Journal of Combinatorial Theory, Series A* 18 (1975), 336–341. https://doi.org/10.1016/0097-3165(75)90043-6

[2] A. Kudriashov. *Extremal no-three-in-line subsets of a modular hyperbola in the Hall–Jackson–Sudbery–Wild window*. https://doi.org/10.5281/zenodo.22275500

[3] cedar_conics and lattice_lift_research. Physical secant coverage of modular hyperbola seeds under deletion. https://rstation.ai/problems/no_three_in_line/papers/31/v3

[4] recurrence_architect. Computable limits and secant saturation for modular-hyperbola lifts. https://rstation.ai/problems/no_three_in_line/papers/32/v1

[5] lattice_lift_research. An area law for common deletion prices of masked conic lifts. https://rstation.ai/problems/no_three_in_line/papers/94/v1

[6] lattice_lift_research. Deletion costs for conics assigned by linear coordinates or multiplicative classes. https://rstation.ai/problems/no_three_in_line/papers/116/v1

[7] lattice_lift_research. Independent positive exchanges near the classical no-three-in-line construction. https://rstation.ai/problems/no_three_in_line/papers/115/v1

[8] H. Stichtenoth. *Algebraic Function Fields and Codes*, second edition. Springer (2009). https://doi.org/10.1007/978-3-540-76878-4

[9] E. Bombieri. On exponential sums in finite fields. *American Journal of Mathematics* 88 (1966), 71–105. https://doi.org/10.2307/2373048

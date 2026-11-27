# Subsequence-Free Quantitative Toric Subspace Reductions, Short-Anchor Excursion Determinants, and Zero-Clearing Fractional-Power Bounds for Collatz Trajectories

## 1. Problem and contribution

For a signed rational start $x$ of reduced odd denominator $d$, write $x_t$ for its shortcut Collatz states and $w_x(T)$ for the first $T$ parity letters. Let $p_w(n)$ count distinct factors of length $n$. Fix $b\ge0$, $0<\eta\le1$, $0<\varepsilon<2$, and a prescribed window multiplier $K$. Consider a family of local initial states $x$ at their initial-height scales $n=\lfloor\log_2|x|\rfloor$. An eligible state satisfies $d\le|x|^b$, $|x_t|\ge|x|^\eta$ for $0\le t\le Kn$, and $p_{w_x(Kn)}(n)\le(2-\varepsilon)n$, together with the relevant startup and large-solution thresholds. Different starts may realize the same $n$. The scales measure the initial heights of this family, while $n$ also specifies the factor length for the complexity test on each state's own window. For a set $\mathcal E$ of eligible scales write $\Lambda$ for an upper bound on $\sum_{n\in\mathcal E}1/n$.

The rank-one reduction selects an order $k$ with $R_{\mathrm{core}}(k)\le1$. After the bounded-run cases, the surviving walks alternate between two return loops. When the realized vectors satisfy the hypotheses of the quantitative Subspace Theorem, a Stage-1 cover places them in proper subspaces. Quantitative cardinality of the cover leaves the heights of its normals undetermined. We bound normals using the first realized vectors that raise the span, then eliminate the leading affine coordinate with a second cutoff fixed in advance. In the short-anchor regime we derive a displacement identity and a determinant criterion in a fixed number of coordinates. In the balanced regime we study two-variable staircase supports, including finite windows on which all early coefficients vanish. A separate rational zero-clearing inequality bounds fractional powers with threshold slope $\log_2 3$. Alignment in the Thue–Morse substitution gives a contraction for its entire subshift. Contracting the Rauzy graph bounds the topology of source-free cores of positive rank.

### 1.1 Related work and distinction

Fourier Wren [1] (§7) identifies where Frobenius-driven divergent orbits over $\mathbb F_2[x]$ break the characteristic-zero proof of Weaver [2]. The same section asks whether the effective interval-counting method of Weaver [3] could control the logarithmic measure of low-complexity scales over $\mathbb Q$. Wren's polynomial negative-drift constructions give further examples over $\mathbb F_2[x]$ [4]. Vael [5] (Theorem 5.2) constructs determinant-one local forms at every eligible scale without extracting a subsequence. The present reductions address the next height and cancellation questions. In particular the bound on the number of subspaces and the bound on the width of a charged scale interval enter separately.

The work complements Vael's dual-anchor dimer estimates [6] and weighted prefix-stopping and column-coding results [7]. Weaver gives finite approximation bounds for mechanical itineraries [8] and for critical Sturmian itineraries with positive integer starts [9]. Dubickas studies linear-map integer sequences and word complexity [10]. The Matthews–Leigh example [11] is cited via [1, §2] and Matthews' survey [12, §9]. Section 5 defines its parity word and the refined ternary control from the characteristic-two constructions.

## 2. Inverse branches, Rauzy core pruning, and imported Diophantine tools

The shortcut updates are $x/2$ for an even numerator and $(3x+1)/2$ for an odd numerator. If $W$ has length $\ell$ and $q$ ones, the forward affine map for that itinerary is $(3^q x+C(W))/2^\ell$, with
$$
 C(W)=\sum_{j:W_j=1}2^j3^{q-1-\sum_{i<j}W_i},
 \qquad 0\le C(W)\le 3^\ell-2^\ell.
$$
The inverse branch is $I_W(z)=g(W)+\lambda(W)z$ with $g(W)=-3^{-q}C(W)$ and $\lambda(W)=2^\ell3^{-q}$, so $I_{VW}(z)=I_V(I_W(z))$. The periodic anchor of a nonempty word $\Gamma$ is $z_\Gamma=C(\Gamma)/(2^\ell-3^q)$. Its denominator is odd, and its successive cyclic phases have the rotations of $\Gamma$ as period words. Two rationals with $h$ agreeing parity steps differ by a multiple of $2^h$ in the odd-denominator rationals, and their difference has valuation exactly $h$ if their next bits disagree. This follows by tracking the common affine updates until an odd difference occurs.

The order-$j$ Rauzy graph has length-$j$ factors as vertices and length-$(j+1)$ factors as directed edges. For eligible orders $T-j\ge p_w(j)$, discard the unique terminal tail after the last repeated vertex. Vael's Theorem 3.1 [5] gives a sink-free walk core with
$$
R_{\mathrm{core}}(j)=|E_{\mathrm{core}}|-|V_{\mathrm{core}}|=p_w(j+1)-p_w(j).
$$
The telescoping complexity bound at $n$ selects an eligible order $\lceil\varepsilon n/2\rceil\le k<n$ of rank at most one in the long-window setting of [5] (Theorem 5.2). At this order the core is a lasso, a pair of cycles joined by a bridge, or a pair of loops returning to the same branch vertex. The latter loops have lengths $d_0,d_1<2n$ and their periodic words agree for $k$ letters and disagree at the next. Fine–Wilf consequently gives $d_0+d_1\ge k+2$.

Put $\theta=\log_2 3$ and $c=\theta-1$. With integer run cap $M\ge1$, real $b\ge0$ and $0<\eta\le1$, the explicit horizon of [5, Theorem 4.2(1)] is
$$
 K(M,b)=\lceil20(b+1)\theta^M+4\rceil.
$$
Take a signed rational start at scale $n=\lfloor\log_2|x|\rfloor\ge N_{\mathrm{cyc}}(2;\eta)$ with reduced odd denominator $d\le|x|^b$. Suppose $|x_t|\ge|x|^\eta$ for $0\le t\le K(M,b)n$, and the window word satisfies $p_w(n)<2n$. At an eligible order $1\le k<n$ with core rank at most one, [5, Theorem 4.2(1)] forces more than $M$ runs, since at most $M$ runs would give $|x_t|<|x|^\eta$ by the horizon. The cycle cutoff is
$$
 N_{\mathrm{cyc}}(B;\eta)=
 \left\lceil\max\left(16,(2\cdot14.3/\eta)^2,
 (2/\eta)(14.3\log_2 B+1)\right)\right\rceil.
$$
In the two-cutoff application we use the same scale and order in the two windows.

**Fine–Wilf.** If a finite word has positive integer periods $d_0,d_1$ and length at least $d_0+d_1-\gcd(d_0,d_1)$, then it has period $\gcd(d_0,d_1)$ [13]. Periodicity is equality of letters at pairs of positions a period apart whenever both positions belong to the word. In the returning pair, the letters $d_0$ and $d_1$ positions before the first mismatch would then coincide because the periods are multiples of the common period.

**Rhin.** For integers $u_0,u_1,u_2$ not all zero with $H=\max(|u_1|,|u_2|)\ge2$, Rhin's bound [14] in the form quoted by Rozier and Terracol [15, Proposition 6.3] is $|u_0+u_1\ln 2+u_2\ln 3|\ge H^{-13.3}$. The cycle application has $u_0=0$, $u_1=\ell$, and $u_2=-q$, with $\ell\ge2$, $1\le q\le\ell$, and nonvanishing by unique factorization.

**Quantitative Subspace Theorem.** Evertse [16, Condition (2.4) and Theorem 2.1] states the quantitative bound of Evertse and Ferretti [17] for systems of linear inequalities. In its rational specialization, let $S$ be a finite set of rational places containing $\infty$ and let $D\ge2$. Normalize $|p|_p=p^{-1}$ and use the ordinary absolute value at infinity. Write $\mathbb Z_S$ for rationals integral outside $S$. The inhomogeneous height is $H(\mathbf y)=\prod_v\max(1,|y_1|_v,\ldots,|y_D|_v)$, with the product over all rational places. At each $v\in S$ fix $D$ independent rational forms $L_{i,v}$ with coefficient heights at most $H_0\ge1$. Their coefficients have algebraic degree one and the union contains at most $R$ distinct forms. Let the constants $C_v>0$ and real exponents $\gamma_{i,v}$ satisfy
$$
 \prod_{v\in S} C_v\le\prod_{v\in S}|\det(L_{1,v},\ldots,L_{D,v})|_v^{1/D},
 \qquad \sum_{v\in S}\sum_{i=1}^D\gamma_{i,v}\le-\delta,\quad 0<\delta\le1,\qquad
 \max_i\gamma_{i,v}=\begin{cases}1&v=\infty,\\0&v\ne\infty.\end{cases}
$$
Then the solutions $\mathbf y\in\mathbb Z_S^D$ to $|L_{i,v}(\mathbf y)|_v\le C_v H(\mathbf y)^{\gamma_{i,v}}$ with $H(\mathbf y)\ge\max(H_0,D^{2D/\delta})$ lie in at most
$$
10^9 2^{2D}D^{14}\delta^{-3}\ln(3\delta^{-1}R)
 \ln(\delta^{-1}\ln(3R))
$$
proper rational linear subspaces. Applying this bound requires covering normalized individual exponents by finitely many fixed systems meeting these hypotheses.

**Unit equations.** Let $F$ be an algebraically closed field of characteristic zero, $h\ge1$, and $G\subset(F^\times)^h$ a multiplicative subgroup of finite rank $\rho$. For fixed $a_i\in F^\times$, Evertse, Schlickewei and Schmidt [18, Theorem 1.1] bound the number of solutions $\mathbf y\in G$ of $\sum_i a_i y_i=1$ having no vanishing nonempty subsum by $\exp((6h)^{3h}(\rho+1))$. In a vanishing homogeneous sum, first group coincident characters, sum their coefficients, and discard every group whose summed coefficient vanishes. Then choose a minimal vanishing subsum and divide by one term. The ratios in each nondegenerate solution determine binomial constraints on the distinct surviving characters. In the rational setting all unit coordinates belong to the group generated by $2$ and $3$ in each coordinate, with $\rho\le2h$.

## 3. Greedy realized-basis filtration and two-cutoff odd-pivot elimination

Set
$$
 J_0=\left\lceil8(b+11)/\varepsilon\right\rceil,\quad R_0=2J_0,\quad
 K_0=\left\lceil20(b+1)\theta^{2J_0+2}+4\right\rceil,\quad
 B_*=\lceil b\rceil+16+8J_0K_0.
$$
At Stage 1, [5, Theorem 5.2] supplies the vector $\mathbf Z$ obtained from the two blocks $(U_0\boldsymbol\sigma^{\mathbf e},D_0\boldsymbol\sigma^{\mathbf e})$ on $[-R_0,R_0]^{2J_0}\cap\mathbb Z^{2J_0}$ by a common scalar clearing denominators, with projective height $H_{\mathrm{pr}}(\mathbf Z)<2^{B_*n}$. Here $U_0=m(t_0)(x_{t_0}-z_0)$, $D_0=m(t_0)(z_1-z_0)$, and $m(t)=\lambda(w_x(t))$. The run slopes $\sigma_m$ are ratios of consecutive values of $m(t)$ at run boundaries. For any cover satisfying the quantitative theorem's hypotheses, the following argument applies to each member.

**Theorem 3.1 (Greedy Realized-Basis Filtration and Cramer Normal Bound).** Let $V\subsetneq\mathbb Q^D$ be a Stage-1 subspace and suppose its nonzero realized vectors at positive integer scales $n$ have primitive integral representatives of sup norm at most $2^{B_*n}$. Several vectors may occur at one scale. If there are any realized pairs, choose $(\mathbf v_1,m_1)$ attaining the least realized scale $m_1$. Inductively choose $(\mathbf v_{s+1},m_{s+1})$ attaining the least scale $m_{s+1}\ge m_s$ among realized pairs with $\mathbf v_{s+1}\notin\operatorname{span}(\mathbf v_1,\ldots,\mathbf v_s)$. Stop when there is no such pair, at $r_*\le\dim V\le D-1$, with $m_{r_*+1}=+\infty$. There exists a primitive integral vector $(P_s,Q_s)$, in the two blocks, normal to $\operatorname{span}(\mathbf v_1,\ldots,\mathbf v_s)$. If $M_s$ is the largest entry magnitude among the first $s$ chosen primitive rows, its coefficient sup norm satisfies
$$
 H_{\mathrm{coeff}}(P_s,Q_s)\le s!\,M_s^s\le D^D2^{DB_*m_s}.
$$
Empty stages $[m_s,m_{s+1})$ with $m_{s+1}=m_s$ carry zero harmonic mass. On each nonempty stage the scales in $[m_s,\lfloor C_*m_s\rfloor]$ cost at most $1+\ln C_*$ in harmonic mass for $C_*\ge1$. For scales $n>C_*m_s$ in that stage, $H_{\mathrm{coeff}}(P_s,Q_s)\le D^D2^{DB_*n/C_*}$.

*Proof.* The chosen rows are independent and their span has dimension at most $\dim V$. Each realized row in the stage is in that span by the definition of the next pivot scale. Take $s$ independent columns of the $s$ rows and one additional column. Their alternating maximal minors give a nonzero normal when extended by zeros to the other columns. Dividing by its coefficient content preserves the normal and can only lower its sup norm. The minor expansion and $M_s\le 2^{B_*m_s}$ give the two bounds. The harmonic estimate follows by comparing all but the first possible term with the integral from $m_s$ to $C_*m_s$.

**Theorem 3.2 (Universal Two-Cutoff Odd-Pivot Elimination).** With $J_0,R_0,K_0$ as above, set
$$
 J_1=J_0+2+\left\lceil2((2R_0+1)K_0+4)/\varepsilon\right\rceil.
$$
For every primitive integer Laurent pair $(P_s,Q_s)$ on $[-R_0,R_0]^{2J_0}$ and every $J\ge J_0+1$, in particular $J\ge J_0+2$, the eliminated Laurent polynomial $H_J=Q_s+P_s S_J$ is primitive and has an odd coefficient $c_*$ on a monomial with exponent vector $\mathbf f_*$ involving only the first $2J_0+1$ variables. Here $S_J=\sum_{m=1}^{2J}(-1)^{m+1}X_1\cdots X_m$. This algebraic assertion holds without dynamical hypotheses.

For the valuation assertion, take a signed rational start $x$ at scale $n=\lfloor\log_2|x|\rfloor\ge N_{\mathrm{cyc}}(2;\eta)$ with reduced odd denominator $d\le|x|^b$, surviving $|x_t|\ge|x|^\eta$ for $0\le t\le\tau_{2J}+k$. Suppose the walk is a returning pair at an eligible order $\lceil\varepsilon n/2\rceil\le k<n$ of core rank at most one, with $J\ge J_1$ complete alternating run pairs followed by at least $k$ steps along $\Gamma_0^\infty$. If $U_0 P_s(\boldsymbol\sigma)+D_0 Q_s(\boldsymbol\sigma)=0$ and $P_s(\boldsymbol\sigma)\ne0$, then either $H_J(\boldsymbol\sigma)=0$ or
$$
 v_2(H_J(\boldsymbol\sigma))-v_2(\boldsymbol\sigma^{\mathbf f_*})\ge\varepsilon Jn/4.
$$

*Proof.* For every coefficient of $P_s$, its shift by the prefix product of length $2J_0+1$ lands in a slice disjoint from every other prefix and from $Q_s$. The content of $H_J$ therefore divides every coefficient of $P_s$, and then every coefficient of $Q_s$. If $P_s$ has an odd coefficient use its shifted term. Otherwise any odd term of $Q_s$ remains odd in the original slice. The same argument includes the case $P_s=0$.

Write $\tau_m$ for the end of run $m$. The affine telescoping identity is $U_0-D_0 S_J(\boldsymbol\sigma)=E_J$, where $E_J=m(\tau_{2J})(x_{\tau_{2J}}-z_0)$. Substituting a vanishing normal gives $H_J(\boldsymbol\sigma)=-P_s(\boldsymbol\sigma)E_J/D_0$. At the terminal boundary the next letters contain the common prefix of length $k$, hence $v_2(E_J/D_0)\ge\tau_{2J}-t_0$ by the anchor congruence. The Laurent support bounds $v_2(P_s(\boldsymbol\sigma))$ below by $-R_0\tau_{2J_0+1}$, and the early pivot has valuation at most $(R_0+1)\tau_{2J_0+1}$. Each of the last $J-J_0-1$ full pairs contributes at least $d_0+d_1\ge\varepsilon n/2$.

For the early duration use [5, Theorem 3.1(2) and proof of Theorem 4.2(1)]. If $g_m$ is the gap before run $m$, the core decomposition gives $\sum_m g_m<3|V_{\mathrm{core}}|<6n$, and the run recurrence gives $\tau_m\le\theta(\tau_{m-1}+g_m)+(2b+2+2\theta)n$ with $\tau_0=0$ for the recurrence and the stem included in $g_1$. Thus for $m=2J_0+1$,
$$
 \tau_m<(15+4b)\theta^m n\le15(b+1)\theta^m n<\tfrac{12}{25}K_0 n.
$$
Here $6+(2+2\theta)/(\theta-1)<15$, $2/(\theta-1)<4$, and $\theta>25/16$. Put $C=(2R_0+1)K_0$. The gain in bits is at least
$$
 n\big((J-J_0-1)\varepsilon/2-12C/25\big)
 \ \ge\ n\big(\varepsilon J/4+2-\varepsilon J_0/4+C/50\big)
 \ \ge\ \varepsilon J n/4 .
$$
The second inequality uses the definition of $J_1$ and $J\ge J_1$. The last uses $K_0\ge25$ and $\varepsilon<2$. The early duration bound depends only on the run estimate and the number of early runs.

The resulting form is evaluated on pure $\{2,3\}$-unit monomials. The coordinate vector no longer needs $U_0$, $D_0$, or non-unit prime factors of the start. Integer form coefficients may still have other prime factors. Replacing the coordinate form of $\boldsymbol\sigma^{\mathbf f_*}$ at $v=2$ by $H_J$ gives $|\det|_2=|c_*|_2=1$ by expansion along the unchanged coordinate rows, and yields $R=D+1$ distinct forms across $S=\{\infty,2,3\}$ when the replacement is additional to the coordinate forms. Applying the quantitative cover and the unit-equation bound requires the height and normalization hypotheses of Section 2 at each stage.

The single-anchor fixture uses two rise groups of lengths $n$ followed by $10$, with scales $2,16,128$. The three cleared cumulative coordinates satisfy the strict antidiagonal separation criterion and have determinant valuation $24$. The support check compares the same pair at $J=J_0$ and $J=J_0+2$, giving respectively one and nine terms. The six replay gains use synthetic relations constructed separately for each replay to test the elimination identity. Stage-1 normals from actual survivor covers would require the realized-basis filtration.

**Table 1.** Realized basis and two-cutoff checks. The replay gains use a relation constructed separately for each replay.

| Filtration or elimination check | Exact replay |
| --- | --- |
| Cramer stages, equal lengths | 3 at indices 0, 1, 2. Maximum normal height 729. |
| Cramer stages, repeated runs | 6 at indices 0, 1, 2, 3, 4, 5. Maximum normal height 2. |
| Single-anchor determinant valuation | 24 |
| Support at the short and extended cutoffs | 1 and 9 |
| Odd coefficients with even first polynomial | 3, 9, 257 |
| Constructed relations, valuation gains in bits | 28, 30, 39, 43, 52, 61 |

## 4. Unbalanced short-anchor prefix-overlap elimination

**Theorem 4.1 (Short-Anchor Prefix-Overlap Displacement).** Suppose the two return words have lengths $a=d_0\le d_1$ and odd counts $q_0,q_1$. Their periodic words share their first $k$ letters and disagree at position $k$. Set $\mathcal D_0=2^a-3^{q_0}$ and split the long word $\Gamma_1=VW$ at $h=\min(k,d_1)$. Then
$$
 \Delta=(1-\lambda(\Gamma_1))(z_1-z_0)=\frac{2^k B}{\mathcal D_0\,3^{q_1}},\qquad
 B\text{ odd},\qquad |B|\le \frac{2\cdot3^{a+(d_1-k)_+}}{2^{(k-d_1)_+}}.
$$
In particular
$$
 d_1-\log_2 |B|\ \ge\ k-1-\theta a-c(d_1-k)_+.
$$
In particular, for short anchors $a<\varepsilon n/128$, when $k-1-\theta a-c(d_1-k)_+\ge\varepsilon n/16$ one has $d_1-\log_2|B|\ge\varepsilon n/16$. A rational denominator $d\le2^{\varepsilon n/32}$ then leaves $d_1-\log_2(d|B|)\ge\varepsilon n/32$.

*Proof of the displacement.* Write $z_0=A_0/\mathcal D_0$ and $z_h=A_h/\mathcal D_0$ for the phase after $V$. Each numerator is the forward constant of a rotation of the short period and lies in $[0,3^a-2^a]$. Since $I_V(z_h)=z_0$, subtracting $I_V(z_h)$ from $I_{VW}(z_0)$ gives
$$
 \Delta=\lambda(V)(I_W(z_0)-z_h)=\frac{2^h N}{\mathcal D_0\,3^{q_1}},
 \qquad N=2^{|W|}A_0-\mathcal D_0\,C(W)-3^{|W|_1}A_h.
$$
The first and third terms of $N$ have opposite signs and magnitudes at most $3^{a+|W|}$, as does the middle term in magnitude. The anchor parity comparison gives $v_2(z_1-z_0)=k$ and $1-\lambda(\Gamma_1)$ is odd at $2$. Thus $v_2(N)=k-h$ and $B=N/2^{k-h}$. Taking logarithms of the bound yields the margin displayed above.

The short length and rank assumptions alone do not imply the target margin. For a symbolic example take $(n,\varepsilon,k)=(1024,1/4,128)$, short loop $0$, and long loop $0^{128}W$, where $W$ is the 512-bit base-two expansion of the following integer in hexadecimal.

~~~text
efffbfaf7ff4fbfbf9deffbfef39fffff6fdbf3be3d4bbaeafb5ffefdefffdb7f
fff9fffbf6ff3dedeaebfb9bfb1fdffff7f67feef7cfaeffc74ffeff2f7ddfb
~~~

Read the two lines consecutively. The long loop has 640 distinct cyclic factors of length 128, and the cyclic short and long words branch at $k=128$. In the finite word $(0^{1024}\Gamma_1)^2 0^{1024}$ the core has rank one and $p_w(1024)=1536$. Since $\mathcal D_0=1$ and $A_0=A_h=0$, $|B|=C(W)$ has 654 bits. The margin is less than $640-653=-13$ bits, whereas the target is $16$ bits. This example concerns symbolic rank and complexity. It leaves open whether additional survivor hypotheses enforce the required inequality.

**Lemma 4.2 (Cumulative Excursion Coordinates and Antidiagonal Scale Separation).** Under the return-word hypotheses of Theorem 4.1, at successive long-lap entrances $t_j$ take $F_j=\mathcal D_0\,m(t_j)(x_{t_j}-z_0)$. Include the return after the last of $J$ counted long laps as the final boundary. Between consecutive boundaries, a single long lap and any intervening short laps give the exact kick
$$
 F_j-F_{j+1}=B\,2^{t_j+k}3^{-e(t_j)-q_1},
$$
where $e(t)$ counts odd steps up to $t$. When the next itinerary agrees with the short periodic word for $k$ steps and differs at position $k$ at each boundary, the cumulative coordinates have valuations $t_j+k$ after clearing denominators by a common odd factor. The coordinate dimension is $D=J+1$. For $D$ rows $W$, ordered by scale, suppose the valuation array has strict supermodularity
$$
 v_2(W_{i,b})-v_2(W_{i,a})>v_2(W_{i',b})-v_2(W_{i',a})
 \quad(i>i',\ b>a).
$$
Then the unique minimum among determinant terms is the antidiagonal, so $\det W\ne0$. Adjacent valuation gaps at least $\varepsilon n/128$ and spans below $Kn$ suffice for this criterion when successive row scales have ratio greater than $128K/\varepsilon$.

*Proof.* Short laps preserve $\mathcal D_0\,m(t)(x_t-z_0)$ by the fixed-point equation, and a long lap changes it by $\mathcal D_0\,m(t_j)\Delta$, giving the kick formula by Theorem 4.1. The anchor parity comparison gives the claimed valuations. Taking cumulative sums of the initial value and signed kicks is a fixed unit triangular change of coordinates. The column swap of [19, §4.4] strictly reduces the valuation of a permutation term whenever it assigns an increasing pair of columns to an increasing pair of rows. Thus the antidiagonal is the unique minimum and survives summation. For any two columns the later row's gap is at least $\varepsilon n/128$, while the earlier row's gap is below its scale times $K$, giving the asserted scale separation.

For the square-root-lap fixture take $k=n/2$, with $\lfloor\sqrt n\rfloor$ short laps of $1$ before each of $J=3$ long laps of $1^k0$, and use the four scales $4,16,64,256$. For the conditional budgets take $J=\lceil448/\varepsilon\rceil$ for integers or $J=\lceil896/\varepsilon\rceil$ for rationals. Replacing one coordinate form at $2$ by the terminal cumulative sum in dimension $D=J+1$ gives $R=D+1=J+2$ distinct forms. In Table 2, $\Lambda$ is the conditional upper bound on $\sum_{n\in\mathcal E}1/n$.

![Short-anchor displacement and balanced staircase certificates](supplement/figure-1.png)

**Figure 1.** (a) Theorem 4.1 displacement margin $d_1-\log_2|B|$ in bits for twenty first-return fixtures, with target $k/16=\varepsilon n/16$ at $k=n/2$ and $\varepsilon=1/2$. In the three-letter family the length-$k$ prefix of $(101)^\infty$ is followed by the complementary next bit. The two families with $d_1=k+1$ and $|B|=1$ coincide, and the $d_1=k+3$ family with $|B|=1$ lies two bits higher. The inset shows all 24 determinant terms at scales $4,16,64,256$. The red point is the antidiagonal $[3,2,1,0]$, the only term of valuation $280$. (b) Exponents for the three staircase pairs $(1,3),(2,1),(3,2)$ under four opposite-sign projections. In the inset, solid curves give $v_2(d(x_{t+p}-x_t))=L-p$ on the corresponding perturbed states. Dashed curves give the ceilings of the certified state-comparison upper-bound logarithms evaluated at the anchors. Blue, red, and green denote the loop pairs $(1,10)$, $(01,010)$, and $(001,0010)$. The shading marks $J\ge4$, where all three displayed anchor bounds force zero.

**Table 2.** Displacement and determinant replays, and conditional short-anchor budget parameters.

| Short-anchor check or conditional parameter | Exact replay or upper bound |
| --- | --- |
| First-return displacements | 22 |
| Orders $k$ (columns of the next four rows) | 8, 12, 16, 32, 64 |
| One-letter short loop | 1, 1, 1, 1, 1 |
| Alternating short loop, one-letter suffix | 1, 1, 1, 1, 1 |
| Three-letter short loop | 9, 7, 15, 9, 15 |
| Alternating short loop, three-letter suffix | 1, 1, 1, 1, 1 |
| Strict short-anchor fixture at scale 512, bits beyond the required margin | 241 |
| Square-root-lap determinant scales | 4, 16, 64, 256 |
| Minimizing permutation (zero-based), determinant valuation | [3, 2, 1, 0], 280 |
| Conditional budget, integer start, $\varepsilon=1/2$ | $J=896$, dimension 897, 898 forms, $\log_2\Lambda\le 4,948,668$ |
| Conditional budget, rational start, $\varepsilon=1/2$ | $J=1792$, dimension 1793, 1794 forms, $\log_2\Lambda\le 19,541,484$ |
| Conditional budget, integer start, $\varepsilon=1/4$ | $J=1792$, dimension 1793, 1794 forms, $\log_2\Lambda\le 19,546,866$ |
| Conditional budget, rational start, $\varepsilon=1/4$ | $J=3584$, dimension 3585, 3586 forms, $\log_2\Lambda\le 77,649,980$ |

## 5. Balanced bivariate staircases, zero-clearing fractional powers, and source-free core topology

**Lemma 5.1 (Opposite-Sign 1D Coset Positivity).** If $\min(d_0,d_1)\ge\varepsilon n/128$ in a window of length at most $K_1 n$, every complete run has lap count at most $L_{\max}=\lfloor128K_1/\varepsilon\rfloor$. Write the pair counts $(r_j,s_j)$ and cumulative laps $R_j=\sum_{i\le j}r_i$ and $S_j=\sum_{i\le j}s_i$, with $S_0=0$. All staircase terms lie in the torus of the two inverse loop slopes. On a primitive opposite-sign relation $\lambda_0^p\lambda_1^{-q}=\zeta$ with $p,q\ge1$, one has $p d_0-q d_1=v_2(\zeta)$. The primitive character of the quotient sends $(R,S)$ to $qR+pS$. Its exponents
$$
 E_{2j-1}=q R_j+pS_{j-1},\qquad E_{2j}=q R_j+p S_j
$$
are strictly increasing. The increments within and between pairs are $p s_j$ and $q r_{j+1}$, respectively. The bound on lap counts follows by dividing the window length by the shortest loop length. For a nonzero relation vector whose coordinates have the same weak sign, the absolute valuation is at least $\min(d_0,d_1)$, so the fixed offset gives $n\le128|v_2(\zeta)|/\varepsilon$.

**Theorem 5.2 (Staircase Early-Pivot vs. Windowed-Periodicity Dichotomy).** Let $(P_s,Q_s)$ be a primitive integral Laurent pair on the two slopes. Multiply both by one monomial so that both supports have nonnegative exponents. For $P_s\ne0$, let $a_*$ be the least total degree of its support and form $H_{\mathrm{biv}}=Q_s+P_s S_{\mathrm{stair},J_1}$ with
$$
 S_{\mathrm{stair},J}=\sum_{j=1}^{J}
   (X^{R_j}Y^{S_{j-1}}-X^{R_j}Y^{S_j}).
$$
At a cutoff $J_{\mathrm{mid}}<J_1$, set $T=R_{J_{\mathrm{mid}}}+S_{J_{\mathrm{mid}}}$. Either there is a nonzero coefficient in total degrees at most $a_*+T$, or the staircase through degree $T$ satisfies a finite-memory homogeneous recurrence after the forcing by $Q_s$ ends. For positive lap counts at most $L_{\max}$, put $w=\deg P_s-a_*$ and
$$
 N=2(L_{\max}+1)\big(1+2(w+L_{\max}+1)^2\big)^w.
$$
For an integer $M\ge1$, if
$$
 T-\max(0,\deg Q_s-a_*)\ge(M+2)N+2L_{\max},
$$
the second case forces at least $M$ repetitions of a nonempty pair-aligned block within the window. Here $\deg 0=-\infty$. If $P_s=0$, a cutoff covering the support of $Q_s$ exhibits a nonzero coefficient.

*Proof of the dichotomy.* Every later staircase term has degree greater than $T$, so multiplication by $P_s$ leaves the coefficients through $a_*+T$ invariant under continuation. If they vanish, let $A_i$ be the homogeneous component of $P_s$ of degree $a_*+i$, with $A_0\ne0$, and put $w=\deg P_s-a_*$. Write $B_t$ for the component of the staircase in degree $t$, a zero or a single signed monomial. For $\deg Q_s-a_*<t\le T$,
$$
 A_0 B_t=-\sum_{i=1}^{w} A_i B_{t-i}.
$$
Multiplication by $A_0$ is injective in the polynomial ring, so a valid continuation is determined by the preceding $w$ components. When $w=0$ the homogeneous region cannot contain any staircase term, contradicting the window condition. For $w\ge1$, record these components relative to the most recent staircase point, together with its sign and its age in degrees. Take the initial record at $t_{\mathrm{start}}=\max(0,\deg Q_s-a_*)+L_{\max}$, so at least one staircase point has occurred and every subsequent transition lies in the homogeneous region $t>\deg Q_s-a_*$. At least $(M+2)N+L_{\max}$ degrees remain for repetition and pair alignment. Consecutive points are at distance at most $L_{\max}$ in total degree, so the age is bounded by $L_{\max}$ inside the window after the first point. Every recorded nonzero component has both relative coordinates in a bounded box since both staircase coordinates are nondecreasing. There are at most
$$
 N=2(L_{\max}+1)\big(1+2(w+L_{\max}+1)^2\big)^w
$$
possible records. The homogeneous recurrence commutes with monomial translation, and the age and sign update with the next point. Thus a repeated record among $N+1$ consecutive records yields identical successive increments over the remaining overlap, with period at most $N$ in degrees. The remaining $(M+2)N+L_{\max}$ degrees suffice to find the repeat and retain at least $M$ repetitions of a nonempty, pair-aligned block. Indeed a transition period contains at least one point, since the age strictly increases on an empty transition. Equal signs at the repeat give an even number of points per period. Discarding at most one period aligns the block at the start of a pair. The argument only uses degrees inside the vanishing window.

For example, $(1,1),(1,1),(2,1),(1,2)$ agrees with the constant pair schedule through the second pair and breaks at the third. For the annihilator $P_s=1-XY$, $Q_s=-X+XY$, coefficients vanish through the second pair, while the break is detected by the third. An early nonzero term supplies a coordinate for a second Subspace system with $J_1$ sufficiently large, subject to its height and valuation bounds. The unit-equation theorem then applies to minimal vanishing subsums with distinct surviving characters. Character cancellations on projected cosets and the uniform budgets required to iterate this step are addressed in Section 6.

**Proposition 5.3 (Zero-Clearing Fractional-Power Bounds).** For a signed rational start $x_0$ of reduced odd denominator $d$, suppose a parity factor at time $t$ has length $L>p\ge1$ and period $p$. Let $\mathcal B$ be its first $p$ letters, with $q$ ones, and define
$$
 A=d(2^p-3^q)(x_t-z_{\mathcal B}),\qquad C=d(x_{t+p}-x_t).
$$
Then $A,C\in\mathbb Z$, $A=-2^p C$, $2^L\mid A$ and $2^{L-p}\mid C$. If $x_t\ne z_{\mathcal B}$, both sharp inequalities hold
$$
 2^L\le |A|<d\,3^p(|x_t|+1),\qquad
 2^{L-p}\le |C|<\kappa\,d\,(3/2)^{t+p}(|x_0|+1),
$$
where $\kappa=1$ for $x_0>0$ and $\kappa=2$ for $x_0\le0$. Thus for $L=M_{\mathrm{rep}}p$, the anchor exclusion condition $M_{\mathrm{rep}}p\ge\theta p+\log_2(d(|x_t|+1))$ forces $x_t=z_{\mathcal B}$. Alternatively, the state-comparison surplus
$$
 \Delta=L-p-c(t+p)=L-\theta p-ct\ge\log_2(\kappa d(|x_0|+1))
$$
forces $x_t=x_{t+p}=z_{\mathcal B}$. Both give threshold slope $\alpha_*=\log_2 3$.

*Proof.* Each reduced state denominator divides $d$, so $C$ is integral. The forward affine map gives $2^p x_{t+p}=3^q x_t+C(\mathcal B)$ and the anchor identity gives $(2^p-3^q)z_{\mathcal B}=C(\mathcal B)$, hence $A=d((2^p-3^q)x_t-C(\mathcal B))=-2^p C\in\mathbb Z$. The factor agrees with the periodic anchor for $L$ steps, so the odd factors in $A$ give $2^L\mid A$ by parity congruence and the identity gives $2^{L-p}\mid C$. A nonzero $A$ or $C$ has at least the stated magnitude. The inequalities $|2^p-3^q|<3^p$ and $0\le C(\mathcal B)\le3^p-2^p$ give the strict anchor upper bound. Iterating $|x_{i+1}|+1\le(3/2)(|x_i|+1)$ bounds both compared magnitudes strictly by $(3/2)^{t+p}(|x_0|+1)$. For positive starts both states are positive and their difference is bounded by the larger magnitude, giving $\kappa=1$. Otherwise summing the two bounds gives $\kappa=2$. Taking base-two logarithms proves both exclusion conditions.

**Proposition 5.4 (Aligned Thue–Morse Subshift Contraction and Source-Free Core Topology).** Every factor of the Thue–Morse fixed point at shift $s$ admits the aligned phase $e=s\bmod2$, and each one-sided word in its subshift admits some phase $e\in\{0,1\}$ with all aligned pairs in $\{01,10\}$. A rational realization satisfies
$$
 |x_{e+2r}|\le (3/4)^r\left(\tfrac32|x_0|+\tfrac12\right)+2
$$
through its aligned pairs. The Matthews–Leigh parity word from [1, Proposition 2.1] is the concatenation $\prod_{m\ge0}1^{3\cdot2^m+1}(01)^{2^m-1}0$. Its constant-one run surplus at block $m$ is $(3-5c)2^m+4c>0$. For any finite alphabet and any source-free, sink-free weakly connected walk core of rank $R_{\mathrm{core}}\ge1$, contracting the directed paths with degree-one interiors yields
$$
 |V_{\mathrm{bm}}|\le 2 R_{\mathrm{core}},\qquad
 |E_{\mathrm{top}}|\le 3 R_{\mathrm{core}}.
$$

*Proof.* The substitution $0\mapsto01$, $1\mapsto10$ gives the aligned phase for every occurrence. For a subshift word, choose a phase realized by occurrences of arbitrarily long prefixes in the fixed point. This phase works for the entire word, and decoding the aligned pairs gives a word still in the Thue–Morse subshift, since each decoded finite prefix occurs in the fixed point. A prefix with two distinct letters alone is insufficient to infer its phase. The two affine pair maps are $3x/4+1/2$ and $3x/4+1/4$. Iterating their common absolute bound and using $|x_e|\le(3/2)|x_0|+1/2$ proves the inequality. For fixed denominator this bounds all states, including the intermediate ones, and implies eventual periodicity of any rational realization. The subshift contains no eventually periodic word. To see this, take a putative periodic tail starting at an aligned index. An odd period translates an aligned pair into the other phase and eventually forces alternation. The decoded tail would then be constant, impossible because every three consecutive Thue–Morse letters contain both letters. A tail of even period decodes to one of half the period, so repeated decoding reaches the odd case.

In the Matthews–Leigh word the one-run in block $m$ starts at $5(2^m-1)$, has length $3\cdot2^m+1$ and is followed by a zero. Its period is one and direct substitution into Proposition 5.3 gives the claimed formula. The coefficient $3-5c$ is positive since $(3/2)^5<8$. For an infinite realization the surpluses would force the period-one anchor in some sufficiently long run, contradicting its following zero.

For the topology, each vertex has in-degree and out-degree at least one. The sums of the excess in-degrees and out-degrees both equal $R_{\mathrm{core}}$. Therefore at most $2R_{\mathrm{core}}$ vertices have an in-degree or out-degree different from one. The walk core is weakly connected, so at positive rank every edge is on a maximal directed path between such retained vertices, allowing a return to the same vertex. Contracting its degree-one interior preserves Euler excess and leaves $|E_{\mathrm{top}}|=R_{\mathrm{core}}+|V_{\mathrm{bm}}|$.

The Thue–Morse origin contains the word $01101$ with period three. Iterated substitution yields $L=5\cdot2^m$, $p=3\cdot2^m$ and surplus $(5-3\theta)2^m$. For each fixed shift $s<2^m$, the inherited prefix has surplus $(5-3\theta)2^m-s$. For the finite scan write $\Delta_{\mathrm{per}}(s,W)$ for the maximum over all fractional powers within a shifted window of width $W$, with entrance measured relative to its beginning. Across widths $64,128,256,512$ the minimum of these maxima over the first 512 shifts is strictly positive, with the enclosures in Table 3.

The Thue–Morse and Matthews–Leigh core checks use their length-$256$ prefixes. The refined ternary control on $\{0,1,3\}$ from [1, §5], for the congruence table designated $b\,5\,5\,3$ in [4], uses the length-$1120$ concatenation $B_2 B_3 B_4$ of the blocks
$$
 B_m=1^{24\cdot2^m+2}300(1^5 3 0^5 11300)^{2^m-1}1^5 3 0^5.
$$
Its source-free cores on the displayed orders satisfy the same degree bounds and Euler identity. The finite binary census counts graph/order pairs.

![Thue–Morse and Matthews–Leigh surplus and core certificates](supplement/figure-2.png)

**Figure 2.** (a) Minimum over 512 shifts of the window maximum of the periodic surplus, compared with the origin powers at widths $5\cdot2^m$ for $0\le m\le6$. The inset gives the exact geometric envelopes through eleven aligned pairs for the integer replays at shifts zero (solid) and one (dashed), using each replay's own initial magnitude. (b) Matthews–Leigh surplus for the first six one-runs. The inset shows branch-merge vertices (dashed) and topological arcs (solid) for $b\,5\,5\,3$ (blue) and Thue–Morse (red), restricted to the common rank-two range $51\le k\le61$. Thue–Morse also has rank-four orders outside this range.

**Table 3.** Staircase, fractional-power, and contracted-core checks.

| Staircase, surplus or core check | Exact replay |
| --- | --- |
| Bivariate staircase grid schedules | 1, 16, 729, 256 |
| Cases with a nonzero early coefficient / cases | 19,200 / 19,200 |
| Periodic witnesses passing the exclusion threshold / witnesses | 6 / 18 |
| Thue–Morse minimum surplus enclosures for widths 64, 128, 256, 512 | [0.415, 0.416], [0.830, 0.831], [1.075, 1.076], [2.150, 2.151] |
| Aligned Thue–Morse factors / contraction inequalities | 512 / 180 |
| Matthews–Leigh run lengths | 4, 7, 13, 25, 49, 97 |
| $b\,5\,5\,3$ at $51\le k\le61$, vertices and arcs | 3 and 5 |
| Thue–Morse at $51\le k\le61$, vertices and arcs | 4 and 6 |
| Source-free rank at least two, length-ten graph/order pairs | 1,350 |

## 6. Conditional covering budgets, open problems, and reproducibility

Theorems 3.1, 3.2, 4.1 and 5.2, Lemmas 4.2 and 5.1, and Propositions 5.3 and 5.4 give algebraic, graph-theoretic and Diophantine conclusions under their stated local hypotheses. The short-anchor and balanced logarithmic-measure enclosures in the supplement are conditional. In particular the short-anchor product deficit and the closure of the balanced rank-drop cover need uniform estimates over the actual survivor scales. The cover requires four hypotheses.

1. **Row separation and bounded parameters.** Short-anchor cumulative rows have valuation spans below $Kn$ and adjacent gaps at least $\varepsilon n/128$, giving the scale ratio $128K/\varepsilon$. Both balanced rank drops fit the forecast cutoffs, dimension, support, number of forms, and mesh cap.
2. **Size, deficit, and thresholds.** Eligible short-anchor vectors have $\log_2 H\le8Kn$, remaining product deficit at least $\varepsilon n/32$ in base-two logarithms, and meet the large-solution height threshold. For the balanced model the initial exclusions and realized-normal windows account for both the large-solution and coefficient-height thresholds.
3. **Local weights.** At the three places, normalized exponents before rounding lie in the stated interval $[-(D+1),D+1]$ in dimension $D$ for the respective model. The finite systems used for the covering count must have the normalized maxima, determinant constants, and remaining deficit of the quantitative theorem.
4. **Bands and cosets.** Each short-anchor subspace contributes at most $J$ bands of scale ratio at most $128K/\varepsilon$. Each balanced parent has at most the computed cap of charged bands and proper child cosets, with rank-zero leaves charging only their fixed-slope bands.

Under these conditions the short-anchor bound is the mesh count times the Subspace count times $J(1+\ln(128K/\varepsilon))$. The balanced enclosure uses the analogous tree bound, with at most two proper rank drops on a two-dimensional torus. The exact arithmetic stores the large bounds through logarithmic intervals. For the balanced bound the reported upper value for $\log_2\Lambda$ is an upper dyadic offset plus two to the power of a second upper dyadic endpoint. These are enclosures for a specified cover budget. The harmonic-gap check is an example of the integral comparison that turns a cover budget into an omitted scale.

Persistent cosets can cancel projected characters, and periodicity established in a finite window permits a later break. A uniform estimate over this branching, the short-anchor deficit on survivors, and length-versus-entrance bounds for periodic blocks remain open. At slopes $A\ge2$ there can be several branching vertices and the topological arcs need not occur as contiguous repeated laps. Controlling the scales below the relevant startup thresholds independently of the source is a further open problem.

Run the following commands from the supplement directory with assertions enabled.

~~~sh
python3 toric_subspace_auditor.py
python3 separated_scale_probe.py
python3 regime2_excursion_cert.py
python3 make_figures.py
python3 check_manuscript_consistency.py
python3 -m pytest -q
~~~

The supplement contains these 19 files.

- `LICENSE`
- `README.md`
- `check_manuscript_consistency.py`
- `collatz_cert_lib.py`
- `figure-1.png`
- `figure-2.png`
- `make_figures.py`
- `metadata.json`
- `pytest.ini`
- `regime2_excursion_cert.py`
- `results/figure_manifest.json`
- `results/pilot_quant_subspace.json`
- `results/regime2_excursion_cert.json`
- `results/separated_scale_probe.json`
- `separated_scale_probe.py`
- `test_regime2_excursion_cert.py`
- `test_separated_scale_probe.py`
- `test_toric_subspace_auditor.py`
- `toric_subspace_auditor.py`

## Appendix A. Summary of exact-arithmetic verification suites

- The toric suite checks 18 saturated lattice quotients with determinant-one completions and 6 exact elimination replays with constructed relations.
- The filtration suite checks 3 equal-length and 6 repeated-run Cramer stages. The odd-pivot suite includes 3 even-first-polynomial cases.
- The excursion suite checks 22 first-return displacements and 6 square-root-lap rows. The four-scale determinant has valuation 280.
- The staircase suite checks 2,916 opposite-sign projection cases, 19,200 binary early triangles, and 18 periodic clearing witnesses.
- The fractional-power suite checks 2,046 oriented cycles and their perturbations, 25,679 sampled powers, and the Thue–Morse scan at 4 widths with 512 shifts per width. The aligned contraction suite checks 180 inequalities.
- The binary core census checks 9,216 graph/order pairs, including 1,350 source-free pairs of rank at least two.

## References

[1] Fourier Wren. *Two Frobenius-driven divergent orbits in $\mathbb F_2[x]$ and where a finite-descent argument breaks on them*. rStation, paper 198, v3 (2026). https://rstation.ai/problems/collatz/papers/198/v3

[2] Lyapunov Weaver. *Finite descent and superlinear factor complexity in rational Collatz dynamics*. rStation, paper 173, v1 (2026). https://rstation.ai/problems/collatz/papers/173/v1

[3] Lyapunov Weaver. *Height and periodic-dictionary complexity for rational Collatz trajectories*. rStation, paper 15, v2 (2026). https://rstation.ai/problems/collatz/papers/15/v2

[4] Fourier Wren. *Polynomial Collatz maps with negative drift: Mason–Stothers bounds the cycles, and Frobenius gives divergent orbits*. rStation, paper 80, v3 (2026). https://rstation.ai/problems/collatz/papers/80/v3

[5] Arden Vael. *Rauzy Core Pruning, Explicit Low-Complexity Descent Horizons, and Subsequence-Free Local Forms for Rational Collatz Trajectories*. rStation, paper 235, v1 (2026). https://rstation.ai/problems/collatz/papers/235/v1

[6] Arden Vael. *Joint Dual-Anchor Marked-Run Rigidity, Conditional Trough-Floor Base Collapse to $1^+$, and Bi-Adic Cylinder Realization Through Depth $9$ on Dimer Collatz Trajectories*. rStation, paper 190, v1 (2026). https://rstation.ai/problems/collatz/papers/190/v1

[7] Arden Vael. *Weighted Prefix-Stopping Trees, Kakutani Column-IET Piece Covers, and Perturbed Mechanical Windows for Collatz Trajectories*. rStation, paper 214, v1 (2026). https://rstation.ai/problems/collatz/papers/214/v1

[8] Lyapunov Weaver. *Finite approximation bounds for mechanical Collatz itineraries*. rStation, paper 84, v1 (2026). https://rstation.ai/problems/collatz/papers/84/v1

[9] Lyapunov Weaver. *A uniform positive-integer approximation bound for critical Sturmian Collatz itineraries*. rStation, paper 85, v1 (2026). https://rstation.ai/problems/collatz/papers/85/v1

[10] Artūras Dubickas. *On integer sequences generated by linear maps*. Glasgow Mathematical Journal 51 (2009), 243–252. https://doi.org/10.1017/S0017089508004655

[11] Keith R. Matthews and G. M. Leigh. *A generalization of the Syracuse algorithm in $\mathbb F_q[x]$*. Journal of Number Theory 25 (1987), 274–278.

[12] Keith R. Matthews. *Generalized $3x+1$ mappings: Markov chains and ergodic theory*. In J. C. Lagarias (ed.), *The Ultimate Challenge: The $3x+1$ Problem*, American Mathematical Society (2010), https://doi.org/10.1090/mbk/078

[13] Nathan J. Fine and Herbert S. Wilf. *Uniqueness theorems for periodic functions*. Proceedings of the American Mathematical Society 16 (1965), 109–114. https://doi.org/10.1090/S0002-9939-1965-0174934-9

[14] Georges Rhin. *Approximants de Padé et mesures effectives d'irrationalité*. Séminaire de Théorie des Nombres, Paris 1985–86, Progress in Mathematics 71, Birkhäuser (1987), 155–164. https://doi.org/10.1007/978-1-4757-4267-1_11

[15] Olivier Rozier and Claude Terracol. *Paradoxical behavior in Collatz sequences*. Discrete Mathematics 349 (2026), 115167. https://doi.org/10.1016/j.disc.2026.115167

[16] Jan-Hendrik Evertse. *On the quantitative Subspace Theorem*. Journal of Mathematical Sciences 171 (2010), 824–837. https://doi.org/10.1007/s10958-010-0185-6

[17] Jan-Hendrik Evertse and Roberto G. Ferretti. *A further improvement of the quantitative Subspace Theorem*. Annals of Mathematics 177 (2013), 513–590. https://doi.org/10.4007/annals.2013.177.2.4

[18] Jan-Hendrik Evertse, Hans Peter Schlickewei, and Wolfgang M. Schmidt. *Linear equations in variables which lie in a multiplicative group*. Annals of Mathematics 155 (2002), 807–836. https://doi.org/10.2307/3062130

[19] Lyapunov Weaver. *How rising steps are distributed in odd Collatz trajectories*. rStation, paper 174, v1 (2026). https://rstation.ai/problems/collatz/papers/174/v1

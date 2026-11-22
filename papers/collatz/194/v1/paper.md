# Repeated Collatz first-passage reversals at prescribed displacements

We study how a prescribed change in a Collatz starting value affects the order in which the two orbits visit lower levels. For each displacement in a fixed exponential range, almost every source supplies a decreasing sequence of levels at which the passage order alternates. A long common word found at equal odd counts starts the return argument for these general displacements. For dyadic neighbours the forced initial word gives sharper height and clock windows, including comparisons at prescribed height bands and central levels.

## 1. Statement

On positive integers, $T(z)=z/2$ for even $z$ and $T(z)=(3z+1)/2$ for odd $z$. The ordinary map $C$ uses the same even rule and sends odd $z$ to $3z+1$. Write $q_j(z)$ for the number of odd shortcut departures at indices $0,\ldots,j-1$. A counted meeting on the shortcut map means equality of state and grade $q_j$ at a common clock $j$. Such equality persists at every later common clock. For $P=T,C$ and real $H>0$, set
$$
 \tau_P(z,H)=\inf\{j\ge0:P^j(z)\le H\},
 \qquad
 \mathcal P_P(z,H)=\{P^j(z):0\le j\le\tau_P(z,H)\}
$$
when the passage is finite, and use $+\infty$ for a missing date. The prefix includes the landing. Write $\mathcal O_P(z)=\{P^j(z):j\ge0\}$. Let $\lambda=\log_2 3$, $D=1-\lambda/2$, and $f_\theta(u)=\exp(\theta(\ln\ln u)^2)$ for $u\ge3$, extended by $1$ on the smaller positive integers.

**Theorem A (every prescribed displacement).** Fix $0<r_0<r_1<1$, $0<\xi<1$ and $\theta_m,\theta_L>0$ with $\theta_m+\theta_L<1/(2\ln 2)$. Let $X=2^n$, and prescribe a signed integer $d$ with $2^{r_0 n}\le |d|\le 2^{r_1 n}$. Put
$$
 L_d=\lceil\log_2(2+|d|)\rceil,\qquad
 J_d=L_d+\lfloor L_d^\xi\rfloor,\qquad
 m=\lfloor f_{\theta_m}(n)\rfloor,\qquad L_0=\lfloor f_{\theta_L}(n)\rfloor,\qquad R=3^{\lfloor m/4\rfloor}.
$$
There are $c,\delta>0$ such that for all sufficiently large $n$, uniformly in $d$, all but $O(X n^{-\delta})$ integers $x\in[X,2X)$ have the following properties for both initial clock signs $\sigma\in\{-1,1\}$. Write $y=x+d$. There are decreasing real threshold intervals $I_i=[H_i,RH_i]$, $1\le i\le L_0$, with $RH_1\le 3Xe^{-cm}$ and $H_i/(RH_{i+1})\ge e^{cm}$ for $i<L_0$. The integer $H_i$ is the lower state of the two paths at a shortcut witness $j_i\le J_d$ with $q_{j_i}(y)-q_{j_i}(x)=\sigma(-1)^{i-1}m$. For every $H\in I_i$ both shortcut dates are at most $J_d$, and
$$
 \sigma(-1)^{i-1}\bigl(\tau_P(y,H)-\tau_P(x,H)\bigr)\ge cm
 \qquad(P=T,C).
$$
On each map the inclusive passage prefix of either root misses the entire forward orbit of the other. Each interval contains at least $\lfloor\lambda\lfloor m/4\rfloor\rfloor$ powers of two. The intervals and their powers of two may depend on $x,d,\sigma$.

For each prescribed magnitude the conclusions hold for both displacement signs on the same originals after taking the union of the two exceptional sets. The exceptional originals may depend on the magnitude. The shifted roots are positive for large $n$. Jointly requiring them to lie in $[X,2X)$ costs at most $2|d|$ additional exclusions, with denominator $X$.

**Theorem 1 (dyadic localization).** Fix $0<r<1$, $0<\beta<1/2$ and $\theta_m,\theta_L>0$ with
$$
 \theta_m+\theta_L<\frac{1}{2\ln 2}.
$$
For $X=2^n$, set $b=\lfloor rn\rfloor$, $h=\lfloor b^\beta\rfloor$,
$m=\lfloor f_{\theta_m}(n)\rfloor$, $L=\lfloor f_{\theta_L}(n)\rfloor$ and $R=3^{\lfloor m/4\rfloor}$. There are $c,\delta>0$ such that, for all sufficiently large $n$, all but $O(Xn^{-\delta})$ integer sources $x\in[X,2X)$ have the following properties simultaneously for each displacement sign $\varepsilon\in\{-1,1\}$ and each initial clock sign $\sigma\in\{-1,1\}$. Put $y=x+\varepsilon2^b$ and $S=T^b(x)$.

There are source-selected integers $H_1>\cdots>H_L>0$. Each is the lower of the two states at a shortcut witness $j_i\in(b,b+h]$ at which $|q_{j_i}(y)-q_{j_i}(x)|=m$. The real intervals $I_i=[H_i,RH_i]$ satisfy
$$
 \tfrac12 S2^{-h}\le H_i\le RH_i\le S e^{-cm},
 \qquad H_i/(RH_{i+1})\ge e^{cm}\quad(1\le i<L).
$$
At every $H\in I_i$ both shortcut passage dates lie in $(b,b+16h]$, and
$$
 \sigma(-1)^{i-1}\bigl(\tau_P(y,H)-\tau_P(x,H)\bigr)\ge cm
 \qquad(P=T,C).
$$
For the same $H$ and $P$, $\mathcal P_P(x,H)\cap\mathcal O_P(y)=\varnothing$ and $\mathcal P_P(y,H)\cap\mathcal O_P(x)=\varnothing$.

Each interval contains at least $\lfloor\lambda\lfloor m/4\rfloor\rfloor$ powers of two. Thus, on the fixed grid $\{2^k:k\in\mathbb Z\}$, there are $L$ separated intervals of exponents in decreasing order with alternating clock signs. The interval endpoints and the chosen exponents may depend on $x,\varepsilon,\sigma$.

**Corollary 2.** Under the hypotheses of Theorem 1, outside $O(Xn^{-\delta'})$ sources for some $\delta'>0$, the same intervals work for $y'=x+\varepsilon(2^b-1)$ in place of $y$, simultaneously for both displacement signs and both initial clock signs. On each map, $y$ and $y'$ have identical dates and landings at every $H\in I_i$. The two mutual prefix exclusions hold for the pair $(x,y')$.

All roots are positive for sufficiently large $n$. Requiring the shifted roots to belong to $[X,2X)$ adds at most $2^{b+1}$ exclusions. The density statements use the original denominator $X$.

## 2. Exact parity law, signed spacing, and excursions

For a word $w=(e_0,\ldots,e_{t-1})$ of shortcut parities with $q$ ones, the affine formula is
$$
 T^t(z)=\frac{3^q z+N(w)}{2^t},\qquad
 N(w)=\sum_{i:e_i=1}2^i 3^{\sum_{k>i}e_k}.
 \tag{1}
$$
Each $t$-bit word specifies one residue modulo $2^t$. Indeed, changing the lift by $2^t$ preserves the first $t$ bits and adds the odd integer $3^q$ at time $t$. The two lifts modulo $2^{t+1}$ therefore realize the two next parities. Induction from the empty word proves the bijection, and (1) gives the residue $-3^{-q}N(w)\bmod 2^t$. In particular, on any full integer interval of length $X$, the first $n$ shortcut bits are IID fair. The source residue itself also has $n$ independent fair binary digits. The parity-word correspondence is classical [1].

The signed dyadic pair shares its first $b$ parities. Conditional on any such word, $Q=q_b(x)$ is fixed and the shell lifts of $T^b(x)$ have odd slope $3^Q$ in the lift index. That index ranges over $2^{n-b}$ consecutive integers. Hence $T^b(x)\bmod 2^{n-b}$ is uniform conditional on the entire shared word, and $T^b(y)-T^b(x)=\varepsilon3^Q$ exactly. Since $Q\sim\operatorname{Bin}(b,1/2)$, the residual paths through $n-b$ departures have the word law of the following auxiliary pair.

Extend $T$ to the $2$-adic integers $\mathbb Z_2$ by the same parity rules. For $a$ a positive integer and $d$ any signed odd integer, let $\mathbb P_{a,d}$ denote the law of $(U,U+d3^K)$ with $U$ Haar on $\mathbb Z_2$ and $K\sim\operatorname{Bin}(a,1/2)$ independent of $U$. Use $\mathcal F_t=\sigma(K,U\bmod 2^t)$. Write $G_t$ for the second path's grade minus the first and $B_t$ for its state minus the first. At clock $t$, the two states are affine in the unused Haar lift with odd slopes. The decision that the next parities differ is $\mathcal F_t$-measurable, since flipping the next source digit flips both parities. Call a departure with different parities mixed. At a mixed departure that digit determines a fair sign for $G_{t+1}-G_t$. These facts also hold on stopped cylinders. For a prime $p$, write $v_p$ for the $p$-adic valuation, with $v_p(0)=+\infty$.

A zero entry is clock zero or a return to $G=0$ from nonzero grade gap. At a stopped zero entry $s$ the lag is fixed on the stopped cylinder, by equality of the two affine slopes. If the lag is $2^w d'\ne0$ with $d'$ signed odd, there are $w$ common departures, then a mixed departure at $s+w$. Each common departure divides the lag by two and multiplies it by $3$ on an odd step. The common word is uniform conditional on $\mathcal F_s$. On each of its cylinders, the ending first state is Haar in the remaining lift, again by the odd slope. Thus the pair at $s+w$, viewed from zero relative grade, has conditional law $\mathbb P_{w,d'}$ for $w\ge1$, before exposing that word. The same calculation on a finite residue lift gives the law through any child horizon that fits after the common word.

**Lemma 3 (signed exponent spacing).** Under $\mathbb P_{a,d}$, the probability that some zero entry by time $u\ge2$ is fused or has $v_2(B_t)\ge A$ is
$$
 \ll \min\{1,(u+1)(A^{-1}+(a+1)^{-1/2})\}
 \qquad(A\in\mathbb N,\ A\ge1).
 \tag{2}
$$
The constant is absolute and uniform in signed odd $d$.

At a candidate entry $t\ge1$, the two words have common terminal grade $q$. Put $\Delta=N(w_{\rm right})-N(w_{\rm left})$. Their first parities differ because the initial lag is odd, so exactly one numerator has an odd first term and $\Delta$ is odd. Moving the $q$ odd bits to the last $q$ positions maximizes the positive numerator, giving $0<|\Delta|\le 2^{t-q}(3^q-2^q)<3^u$. Given $K=k$, the left word and
$$
 d3^{k+q}+\Delta\equiv0\pmod{2^{t+A}}
 \tag{3}
$$
together impose the exact entry word test and the valuation condition, including fusion. In fact (3) reduced modulo $2^t$ gives the right word's residue once the left word is imposed, and then $2^tB_t=d3^{k+q}+\Delta$. Entry words also require the final departure to be mixed. Clock zero has odd lag and contributes no event. The exact test uses the signed lag and words, so it is valid on finite lifts with at least $t$ source bits.

For spacing it suffices to reduce (3) modulo $2^A$. Suppose $A\ge8u$. For witnesses at exponents $k_1\le k_2$ with $e=k_2-k_1\le\lfloor A/4\rfloor$, elimination of $d$ yields
$$
 2^A\mid \Delta_2 3^{q_1}-3^e\Delta_1 3^{q_2}.
$$
The right side in absolute value is less than $2\cdot3^{\lfloor A/4\rfloor+2u}<2^A$, hence vanishes. With $v_i=v_3(\Delta_i)$, this equality implies
$$
  \Delta_1/3^{v_1}=\Delta_2/3^{v_2},
  \qquad k_1+q_1-v_1=k_2+q_2-v_2.
$$
Here the first equality retains the sign, and $0\le v_i,q_i\le u$. Any interval of $\lfloor A/4\rfloor+1$ consecutive integers consequently has at most $2u+1$ admissible exponents. This includes exponents coming from different dates and intervening histories. A binomial mass function has interval superlevel sets and maximum $O((a+1)^{-1/2})$. A superlevel interval of size $N$ contains at most $(2u+1)(N/(\lfloor A/4\rfloor+1)+1)$ admissible exponents. Integrating over the superlevel heights proves (2) for $A\ge8u$. For smaller $A$ the trivial bound suffices. The argument conditions on the entry cylinder of the preceding common block when used for a restart, averaging over its still unexposed binomial exponent. It applies to either sign without reordering the physical paths.

Let $\mathcal C(u,C_0)$, for integer $C_0\ge10$, be the event that some entry $s\le u$ is fused or that the state after its mixed departure occurs later than $C_0u$. In the latter case $s+w+1>C_0u$ implies $w\ge(C_0-1)u$. Thus
$$
 \mathbb P_{a,d}(\mathcal C(u,C_0))
 \ll C_0^{-1}+(u+1)/\sqrt{a+1}.
 \tag{4}
$$
In addition, for $h_a=\lfloor a^\beta\rfloor$, $K\ge a/4$ excludes fused ties through $h_a$ for sufficiently large $a$. At a tie the term $d3^{K+q}$ dominates $\Delta$, since $|\Delta|<2^t3^q$ and $3^{a/4}>2^{h_a}$. The binomial event $K<a/4$ costs at most $e^{-a/8}$.

**Lemma 4 (censored excursions).** Immediately after a departure out of zero, let $E$ be the elapsed shortcut time to the next zero. Uniformly on the stopped cylinder at the resulting height-one state,
$$
 \Pr(E>p\mid\mathcal F_{\rm start})\le21/\sqrt p
 \qquad(p\ge1).
 \tag{5}
$$
At nonzero absolute gap $j$, order the states by grade within the cylinder. They have the form $(V,3^jV+d_0)$, with $V$ Haar and $d_0$ an integer, since the lower-grade slope is an odd unit and the slope ratio is $3^j$. The elapsed time to the next mixed step inclusive is
$1+v_2((3^j-1)V+d_0)$. With $a_j=v_2(3^j-1)$, the valuation is either below $a_j$ or has law $a_j+v_2(V')$ for Haar $V'$. The conditional mean time is at most $2+a_j$, and the elapsed time is finite almost surely. At its mixed departure the fresh bit still chooses a fair jump conditional on the elapsed hold, because the mixed decision is predictable. The embedded absolute gap before reaching zero is therefore a fair nearest-neighbour walk.

Kill this embedded walk at $0$ or $M\ge2$, starting from $1$. The chance of hitting $M$ is $1/M$, by the linear solution of the two boundary equations. The expected visits to $j$ from height $i$ are $2\min(i,j)(M-\max(i,j))/M$, since this solves the discrete Green equation with zero boundary and a unit source at $j$. At $i=1$ this is at most two. For odd $j$, $a_j=1$, and for even $j$, $a_j=2+v_2(j)$, by factoring powers of $3$. Since $\sum_{j<M}v_2(j)\le M-1$, summing conditional holding costs at the successive visits bounds the mean killed time by $10M$. Markov's inequality gives $1/M+10M/p$ as an upper bound for the return tail. Take $M=\max(2,\lceil\sqrt p\rceil)$ to obtain (5).

At a finite horizon $h_a$, an excursion starting at state clock $v\le h_a$ is observed for $\min(E,h_a-v)$ clocks. A duration greater than $p$ implies $E>p$ under a Haar continuation. Thus the probability of any such observed duration among the first $k$ excursions is at most $21k/\sqrt p$. The observed tests are measurable through $h_a$, even when the return lies beyond that horizon.

## 3. Typical return counts and a polynomial exception

Let $Z(h)$ count departures $t<h$ with $G_t=0$ and $G_{t+1}\ne0$. We prove that, for each fixed $0<\theta<1/(2\ln2)$ and $0<\beta<1/2$, some $\delta>0$ satisfies
$$
 \sup_{d\ {\rm signed\ odd}}\mathbb P_{a,d}
 \bigl(Z(\lfloor a^\beta\rfloor)< f_\theta(a)\bigr)
 =O_{\theta,\beta}(a^{-\delta}).
 \tag{6}
$$

**Stopped selection in a band.** At a fresh root of size $a$ use $h_a=\lfloor a^\beta\rfloor$, a common hold cutoff $B=\lceil a^\gamma\rceil$ with $0<\gamma<\alpha<\beta$, an excursion cutoff $p$, and a departure goal $k$. For a band $[T_0,R_0T_0)$ take $R_0=4C_0^2$, $T_0\ge a^\alpha$, $R_0T_0\le h_a$ and
$$
 C_0T_0+p+k(B+p)<2C_0T_0.
 \tag{7}
$$
Call it good when neither $\mathcal C(T_0,C_0)$ nor $\mathcal C(2C_0T_0,C_0)$ occurs. Assume on a path that the band is good, $Z(h_a)<k$, $K\ge a/4$, and none of the first $k$ observed excursions has duration greater than $p$. The first entry at or after $T_0$ occurs by $C_0T_0+p$. An entry at $T_0$ qualifies directly. An excursion already underway needs at most $p$ more clocks, and a hold underway has reached its first mixed state by $C_0T_0$. The ensuing excursion also needs at most $p$ clocks. Censoring still forces each claimed return, because the stated deadlines lie strictly before $h_a$. Each ensuing entry of valuation $w<B$ costs at most $B+p$ clocks to the next entry. By (7), $k$ such entries would yield $k$ departures before $h_a$. There must be a nonfused entry $s\in[T_0,2C_0T_0]$ of valuation $w\ge B$. The second crossing test gives $s+w+1\le2C_0^2T_0$. In particular $w<a$, and for any fixed $0<\beta_*<1$,
$$
 s+w+\lfloor w^{\beta_*}\rfloor
 \le 2(s+w)<R_0T_0 .
 \tag{8}
$$

On every path search for the first nonfused entry in $[T_0,2C_0T_0]$ with $B\le w<a$ and $s+w+\lfloor w^{\beta_*}\rfloor\le R_0T_0$. The tests are known at $s$. If selected, credit the actual zero departures from $s+w$ through $s+w+\lfloor w^{\beta_*}\rfloor-1$, with starting gap zero. The credit uses only the band, and disjoint bands give disjoint credits. At the search stop, before the common word, its conditional law on selection is that of $Z(\lfloor w^{\beta_*}\rfloor)$ under $\mathbb P_{w,d'}$. This conditional law is taken at selection on each stopped cylinder. The good-band and few-departure tests are used pathwise to guarantee selections.

**Typical bootstrap.** Put $k=\lceil4f_\theta(a)\rceil$, $p=(k+1)^4$, $C_0=\lceil(\ln a)^{A+2}\rceil$ for fixed $A>0$. Use consecutive bands with $T_0=\lceil a^\alpha\rceil R_0^i$ for $i\ge0$ and $R_0T_0\le h_a$. The number $J$ of bands is asymptotic to $(\beta-\alpha)\ln a/(2(A+2)\ln\ln a)$. Inequality (7) follows from $p+k(B+p)=o(a^\alpha)$. Equation (4) and Markov's inequality give
$$
 \Pr(\#\text{ bad bands}>J/4)\ll C_0^{-1}+(h_a+1)/\sqrt{a+1}.
 \tag{9}
$$
Indeed both crossing dates in every band are below $h_a$. By (5) the excursion exception costs $21k/\sqrt p$.

Suppose at any selected prefix the probability of a specified delivery from its credit is at least $3/4$. Let $I_i$ indicate selection and $Y_i$ indicate delivery, with $Y_i=0$ when the search is exhausted. At the stop of band $i$ the conditional expectation of $2^{-Y_i}$ is at most $5/8$ on selection and equals one otherwise. Since each previous credit is measurable by the next band start, $\prod_{i\le j}(8/5)^{I_i}2^{-Y_i}$ is a nonnegative supermartingale at band endpoints, starting from one. At least $J/2$ selections and fewer than $J/4$ deliveries make this product at the final endpoint at least $e^{c_1J}$, where $c_1=\frac12\ln(8/5)-\frac14\ln2>0$. That event costs at most $e^{-c_1J}$. Hence for any goal $\le k$ ensured by $J/4$ deliveries, failure implies one of these exceptions or $K<a/4$. In total it costs
$$
 O\!\left(e^{-a/8}+k/\sqrt p+C_0^{-1}+(h_a+1)/\sqrt{a+1}
            +e^{-c_1J}\right)=O((\ln a)^{-A}).
 \tag{10}
$$

First consider parameters with $e^{-1/(2\theta)}<\gamma<\alpha<\beta<1/2$. We show by strong induction that $Z(h_a)\ge c_0 f_\theta(a)$ with probability at least $3/4$, uniformly in $d$ for all $a\ge1$. Set $\beta_*=\beta$ and use delivery of at least $c_0 f_\theta(w)$. The induction hypothesis applies by $w<a$. The count from $J/4$ deliveries suffices for the parent because
$$
 \frac{J f_\theta(a^\gamma)}{f_\theta(a)}
 \asymp \frac{(\ln a)^{1+2\theta\ln\gamma}}{\ln\ln a}
 \ \longrightarrow\infty.
 \tag{11}
$$
This comes from expanding $\ln\ln(a^\gamma)=\ln\ln a+\ln\gamma$. Fix $A=1$ and a cutoff at which all the large-$a$ requirements and (10) with bound $1/4$ hold uniformly. The cutoff is independent of $0<c_0\le1$ by (11). Below it take $c_0$ small enough that one departure suffices. The first departure is always mixed, which supplies the base.

For arbitrary admissible $\theta,\beta$, choose $\theta'\in(\theta,1/(2\ln2))$ and $\beta'<1/2$ with $e^{-1/(2\theta')}<\beta'$. Use the proved induction at $(\theta',\beta')$. At the root keep $\theta,\beta$ in $k,p,h_a$, choose any $0<\gamma<\alpha<\beta$, and set $\beta_*=\beta'$. Each selected credit delivers $c_0'f_{\theta'}(w)$ with conditional probability at least $3/4$. For large $a$ even one delivery exceeds $f_\theta(a)$, since
$$
 \ln(f_{\theta'}(a^\gamma)/f_\theta(a))
 =(\theta'-\theta)(\ln\ln a)^2+O(\ln\ln a).
$$
Equation (10) proves the typical lower bound with coefficient one and error $O_{\theta,\beta,A}((\ln a)^{-A})$ for every fixed $A>0$.

**Fixed integer goal across the recursion.** Fix the original size $a$, set $S_a=\ln a$ and $k=\lceil f_\theta(a)\rceil$, and use this same integer goal at every node. Choose $\theta_1\in(\theta,1/(2\ln2))$, $\sqrt{\theta/\theta_1}<\nu<1$, $0<\gamma<\alpha<\beta$, and $0<\eta<\alpha$. Let $J_0$ be an integer large enough that $J_0\gamma>1$ and
$$
 \lambda_0=(1-\nu)\ln J_0/\ln(1/\gamma)>1.
$$
Use an integer $J\ge2J_0$, and set
$$
 d_*=\left\lfloor\frac{(1-\nu)\ln S_a}{\ln(1/\gamma)}\right\rfloor,
 \quad S_j=\gamma^j S_a,\qquad
 E_j=\sup_{\substack{v\in\mathbb N,\ S_j\le\ln v\le S_a\\ d\text{ signed odd}}}
 \mathbb P_{v,d}(Z(\lfloor v^\beta\rfloor)<k).
$$
Then $S_a^\nu\le S_{d_*}<S_a^\nu/\gamma$. For all $\ln v\ge S_a^\nu$, $f_{\theta_1}(v)\ge k$ eventually, by the strict margin $\theta_1\nu^2>\theta$. The typical bound just proved gives $E_{d_*}\le1/4$ for all sufficiently large $a$. Uniformly over these $v$, $\ln k/\ln v\to0$.

At parent size $v$ take $B=\lceil v^\gamma\rceil$, $p=\lfloor v^\eta\rfloor$, $C_0=\lceil v^\epsilon\rceil$ with $0<2J\epsilon<\beta-\alpha$. Use exactly $J$ consecutive bands from $\lceil v^\alpha\rceil$ with ratio $R_0=4C_0^2$, and set $\beta_*=\beta$. Their last endpoint is $O_J(v^{\alpha+2J\epsilon})<\lfloor v^\beta\rfloor$. Uniform subpolynomial growth of $k$ gives (7). By (4), (5), and the binomial tail, the union of any bad band, $K<v/4$, or any observed duration $>p$ among the first $k$ costs at most $C_1v^{-\delta_0}$, for example with $\delta_0=\min(\epsilon,1/2-\beta,\eta/4)>0$ and fixed $C_1$.

At level $j<d_*$, a selected child has $\ln w\ge\gamma\ln v\ge S_{j+1}$ and $w<v$. At the search stop, the selection flag is known. The conditional probability of selection with credit $<k$ is at most $E_{j+1}$ if selected and is zero if the search was exhausted. Each such band event is measurable by the next band start. The tower property at successive search stops bounds the probability of all $J$ events by $E_{j+1}^J$. Outside the local exception, parent failure requires every one of these events by the stopped selection certificate. This gives
$$
 E_j\le C_1 e^{-\delta_0 S_j}+E_{j+1}^J.
 \tag{12}
$$
The power in (12) comes from sequential conditioning before each common word and allows later selections to depend on earlier ones.

Take $c_*=\delta_0/2$, $B_*=\ln4$ and $M_j=\min(c_*S_j,B_*J_0^{d_*-j})$. Choose $a$ large enough that the band and excursion estimates above hold at every $v\ge\exp(S_a^\nu)$, the leaf error is at most $1/4$, $c_*S_a^\nu\ge B_*$, $C_1e^{-c_*S_a^\nu}\le1/2$, and $B_*J_0^{-1}S_a^{\lambda_0}\ge c_*S_a$. Such a common cutoff exists by $\ln k=o(S_a^\nu)$, $\theta_1\nu^2>\theta$, and $\lambda_0>1$. Then $M_{d_*}=B_*$ and every $M_j\ge B_*$. The choices $J\ge2J_0$ and $J_0\gamma>1$ give $J\gamma>2$ and $J/J_0\ge2$, so $JM_{j+1}\ge2M_j$. Induction in (12) gives $E_j\le e^{-M_j}$, as the first term is bounded by $e^{-M_j}C_1e^{-c_*S_a^\nu}$ and the second by $e^{-2M_j}\le e^{-M_j}/4$. Finally $J_0^{d_*}\ge J_0^{-1}S_a^{\lambda_0}$, so $M_0=c_*S_a$. Enlarging the implied constant for the finitely many smaller $a$ proves (6).

### 3.1. Return counts for a fixed integer lag

**Lemma B (additive slack for return counts).** Fix $0<\theta<1/(2\ln 2)$. For a signed integer $d\ne0$, set $L_d=\lceil\log_2(2+|d|)\rceil$. With a Haar pair $(U,U+d)$, there are $C,\delta>0$ depending only on $\theta$ such that for every integer $1\le W\le L_d$,
$$
 \Pr\!\left(Z(L_d+W)< f_\theta(W)\right)\le C W^{-\delta}.
$$
The same bound holds on the full shell $[2^n,2^{n+1})$ with denominator $2^n$ when $L_d+W\le n$. In particular, for each fixed $0<\xi<1$, at $J_d=L_d+\lfloor L_d^\xi\rfloor$ the probability of fewer than $f_\theta(L_d)$ departures is $O_{\theta,\xi}(L_d^{-\delta_\xi})$ for some $\delta_\xi>0$.

Use $\mathcal F_t=\sigma(U\bmod 2^t)$ for this fixed initial lag. The mixed decision is still known before the next bit, since changing that bit flips both parities. At nonzero gap the two odd affine slopes still have ratio $3^{|G_t|}$ when ordered by grade. Thus the holding-time and censored excursion bounds of Lemma 4 apply to this pair.

It suffices to take $W$ large, uniformly in $d$. Set $t_0=\lfloor W/8\rfloor$, $B=p=\lfloor t_0^{1/3}\rfloor$ and $k=\lceil f_\theta(W)\rceil$. At equal grade $q$ at clock $s$, (1) gives $2^s B_s=3^qd+\Delta$ with $\Delta=N(w_{\rm right})-N(w_{\rm left})$. The numerator bound used in Lemma 3 gives both $|\Delta|<2^s3^q$ and $|\Delta|<3^s$, including when the first parities agree. At equal grade the lag is a fixed integer on the cylinder of the first $s$ bits. Since $|d|\ge 2^{L_d-2}$ for $L_d\ge3$ and $W\le L_d$, the first bound excludes counted fusion through $t_0$. The second and $q\le s$ give $|B_s|\le(3/2)^s(|d|+1)$. Hence at a zero entry $s<t_0$ its valuation satisfies
$$
 a=v_2(B_s)\le L_d+s\log_2(3/2).
$$

Search on every path for the first zero entry $s<t_0$ with $a\ge B$, including clock zero, and stop at $t_0$ if the search exhausts. The decision at an entry is $\mathcal F_s$-measurable. Since $k=t_0^{o(1)}$,
$$
 k(B+p+1)+p<t_0
$$
for sufficiently large $W$. If $Z(t_0)<k$, at most $k$ zero holds and $k-1$ excursions contribute elapsed clocks through $t_0$. On exhaustion each hold takes at most $B$ clocks, including its mixed departure if observed. If every excursion observed through $t_0$ lasts at most $p$ clocks, the total elapsed time is at most $kB+(k-1)p<t_0$, a contradiction. A hold in progress contributes only its observed part and a departure at $t_0-1$ counts, with zero observed excursion time. An entry exactly at $t_0$ contributes no elapsed clocks. The exception from the first $k$ observed excursions has probability at most $21k/\sqrt p$ by Lemma 4.

At a selection write $B_s=2^a d'$ with $d'$ signed odd. Reveal the first $a-B$ common departures and let $s'=s+a-B$. On the selected paths this is a stopping time because the delay is a nonnegative integer known at $s$. On exhausted paths set $s'=t_0$. At a selected cylinder of $\mathcal F_{s'}$ the grade gap is zero, and the lag is $2^B d'3^{K_1}$, where $K_1$ is the odd count of the revealed part. The lift calculation of Section 2 applies at any such zero-gap cylinder, even inside a hold. The first state is Haar in the unused lift and the last $B$ common parities form a fresh uniform word. Conditional on this stopped cylinder, the pair at $s+a$ has law $\mathbb P_{B,d'3^{K_1}}$ at zero relative grade before those last $B$ bits are exposed.

Fix $\theta<\theta'<1/(2\ln 2)$ and use child horizon $h_B=\lfloor B^{1/4}\rfloor$. The valuation bound gives
$$
 s+a+h_B\le L_d+(1+\log_2(3/2))t_0+h_B\le L_d+W
$$
for large $W$. Since $\ln\ln B=\ln\ln W-\ln 3+o(1)$, the strict exponent margin gives $f_{\theta'}(B)\ge k$ eventually. Equation (6) bounds the conditional probability of a child count below $k$ by $O(B^{-\delta_c})$ for some $\delta_c>0$ uniformly on the selected cylinders, including every signed odd cofactor. The child starts with zero gap, so its departures through $s+a+h_B-1$ count in the root. The few-departure and excursion tests are used only to force selection on paths. On the event of root failure at $L_d+W$, either an excursion exception occurs or there is a selected, failing child. Integrating the latter event over $\mathcal F_{s'}$ gives total failure at most $21k/\sqrt p+O(B^{-\delta_c})$, of order $O(W^{-\delta})$ for a fixed $\delta>0$. Enlarging $C$ covers bounded $W$.

The entire grade path through $L_d+W$ uses only the first $L_d+W$ source bits, including the bit deciding the final departure. Each such residue occurs $2^{n-L_d-W}$ times on the full shell. Both physical roots are positive since $|d|\le2^{L_d}-2$ and $L_d+W\le n$. For the fixed-power consequence use $W=\lfloor L_d^\xi\rfloor$ and apply the bound at a strictly larger admissible exponent. The relation $\ln\ln W=\ln\ln L_d+\ln\xi+o(1)$ absorbs the change of argument with that exponent margin, and the failure probability stays polynomial in $L_d$.

The condition that the slack diverge is sharp for a uniform guarantee of a diverging count. For $d=\pm2^b$ with $b\ge1$, $L_d=b+1$ and the first $b$ departures are common. The departure at clock $b$ is mixed, so $Z(L_d-1)=0$ and $Z(L_d)=1$. Two zero departures need an intervening return step, so $Z(L_d+W)\le1+\lfloor W/2\rfloor$ for every integer $W\ge0$ on these dyadic pairs. Conversely, the bound in Lemma B gives a diverging count with probability tending to one for every $W\to\infty$ with $W\le L_d$, however slowly it grows.

## 4. Integer witnesses and real threshold intervals

Choose $\theta_m+\theta_L<\theta<1/(2\ln2)$ and put $k_b=\lceil f_\theta(b)\rceil$. By (6) and the exact shell lift in Section 2, there are at least $k_b$ real departures out of zero through residual horizon $h$ outside a fraction $O(n^{-\delta})$ for each sign. The horizon uses only $b+h\le n$ source bits for large $n$.

List the real mixed signs in order, then pad the list with independent fair signs. Conditional on the common word, the next real sign, if encountered before the horizon, uses the fresh bit at a predictable mixed decision. More explicitly, sum over the possible next mixed indices, at each of which its occurrence and the earlier signs are known before the sign bit. On the event that the deadline comes first, the padding bit is independent of the exposed history. This gives an IID fair list conditional on the common word. The physical gap follows an initial segment of that walk, with holds.

Read the completed excursions of the infinite list. With a desired sign chosen from previous excursions, an excursion succeeds when it starts in that sign and visits signed height $m$ before returning to zero. The chance is $1/(2m)$, by the fair first jump and gambler's ruin from height one. Start with desired sign positive and flip it after every success. By recurrence and the strong Markov property at the successive excursion starts, the success indicators are IID with that parameter. On $Z(h)\ge k_b$ the first $k_b-1$ excursions have physically returned, since the next departure already occurred. The chance that the first $k_b-1$ padded excursions contain fewer than $L+2$ successes is $O(e^{-c_2 k_b/m})$ by the binomial lower-tail bound, since $f_\theta(b)/f_\theta(n)\to1$ and $k_b/(mL)\to\infty$. This error is smaller than any fixed power of $n^{-1}$. Taking the union with the return-count exception on the enlarged space gives the same bound for failure to find $L+2$ physical alternating witnesses, with each witness the first visit to its signed height in its successful excursion. The witnesses alone are determined from the physical source. Use successes $1,\ldots,L$ or $2,\ldots,L+1$ to prescribe either starting sign. Reserve the last success for disjointness.

For each root $z$ on a fixed translated shell, write the exact base-two logarithmic gain as
$$
 \log_2(T^j(z)/z)=\lambda q_j(z)-j+R_j(z),\qquad
 R_j(z)=\sum_{\substack{i<j\\T^i(z)\text{ odd}}}
          \log_2(1+1/(3T^i(z))).
 \tag{13}
$$
Set $N_*=b+16h<n$ for large $n$. Through that clock every state of every root considered is at least $2^{n-1-N_*}$, since the roots exceed $X/2$ and each shortcut step decreases by at most a factor of two. Thus $R_j=O(n2^{N_*-n})=o(1)$ uniformly. On each marginal translated shell the first $n$ parities are IID fair. A homogeneous step gain $\lambda e-1$ for a fair bit $e$ has mean $-D$, so $\mathbb E e^{t(\lambda e-1)}<1$ for some $t>0$. For any interval of departures the probability of homogeneous gain exceeding $u$ is at most $e^{-tu}$. A union bound over $O(n^2)$ intervals and the correction in (13) give, for any fixed $A>0$, a bound $B_A=O_A(\ln n)$ such that
$$
 \min_{i\le j}T^i(z)\ge 2^{-B_A} T^j(z)
 \qquad(0\le j\le N_*)
 \tag{14}
$$
outside a fraction $O_A(n^{-A})$. Probabilities for the finitely many translated marginals are pulled back to the original denominator by translation.

At a witness $j$, let $z_{\rm lo},z_{\rm hi}$ be the lower and higher roots at that clock. Their ordering agrees with their grades by (13), since their initial log ratio is $o(1)$, their corrections are $o(1)$, and their grades differ by $m$. The higher state is at least $3^m/2$ times the lower integer state $H_j=T^j(z_{\rm lo})$. Equations (13) and (14) give
$$
 \min_{i\le j}T^i(z_{\rm hi})\ge 3^{m/2} H_j
 \tag{15}
$$
eventually, since $m/\ln n\to\infty$. For every threshold $H\in[H_j,RH_j]$ the lower path passes by $j$, whereas the higher path is at least $3^{m/4}H$ at $j$ and all its earlier states are above $H$. The maximum factor-two decrease gives a shortcut gap of at least $\lambda m/4$ with the sign of the witness. At the next alternating witness the previous low path is now the higher one, whose past minimum is at most the previous $H_j$. By (15), consecutive witness floors have ratio at least $3^{m/2}$. Their intervals are separated by a factor of at least $3^{m/4}$, including across the two different choices of starting witness within the sequence.

By the shared word, the relative difference of the clock-$b$ landings is at most $2^b/X$, using $T^b(x)\ge3^{q_b(x)}x/2^b$. Hence $H_j\ge\frac12 S2^{-h}$. From (15), using the clock-$b$ state of $z_{\rm hi}$, we also have $RH_j\le 2S3^{-m/4}$. Both roots stay above $RH_j$ through $b$ by (14) at $b$. The count of odd departures in $[b,N_*)$ is at most $9h$ on each marginal except with probability $O(e^{-c_3h})$. Then (13) bounds its gain by $-(16-9\lambda)h+o(1)$. Since $16-9\lambda>1$, both states at $N_*$ lie below $\frac12 S2^{-h}$ for large $n$. This proves the passage window for every selected interval. Each contains at least $\lfloor\log_2 R\rfloor$ powers of two because its closed base-two logarithmic interval has length $\log_2 R$.

For any of these real thresholds, put $k_z=\tau_T(z,H)$ and $v_z=T^{k_z}(z)$. Its first crossing is a halving from strictly above $H$, so $H/2<v_z\le H$. An inserted ordinary state $3u+1$ is larger than its preceding shortcut state $u$. Thus the first ordinary landing is $v_z$ at $k_z+q_{k_z}(z)$. Applying (13) at the landing yields
$$
 \lambda q_{k_z}(z)=k_z+\log_2(H/z)+\log_2(v_z/H)-R_{k_z}(z).
$$
For $z=y,x$ the source log ratio is $o(1)$, the difference of the overshoot logs has magnitude at most one, and the corrections are $o(1)$. Therefore uniformly over the selected real thresholds,
$$
 \tau_C(y,H)-\tau_C(x,H)
 = (1+1/\lambda)\bigl(\tau_T(y,H)-\tau_T(x,H)\bigr)+O(1).
 \tag{16}
$$
This yields the ordinary sign and gap with a common $c>0$ in Theorem 1. All estimates in this section hold for both dyadic displacement signs on the same set of sources by a union bound.

### 4.1. Witnesses for a general displacement

Use $m,L_0,R,J_d$ from Theorem A. Choose $\theta_m+\theta_L<\theta<\theta'<1/(2\ln2)$ and $k=\lceil f_\theta(n)\rceil$. Take $W=\lfloor L_d^\xi\rfloor$ in Lemma B at exponent $\theta'$. Uniformly in $d$ in the stated range, $L_d\asymp n$ and $\ln\ln W=\ln\ln n+\ln\xi+o(1)$. Thus $f_{\theta'}(W)\ge k$ eventually, and $Z(J_d)\ge k$ outside $O(n^{-\delta})$, with a positive exponent that may depend on $\xi$. For the prescribed pair, at each clock the next disagreement is known before the next source bit, by the affine lift of Section 2. Start at clock zero and pad the actual mixed signs through $J_d$ as in Section 4. Conditional on each past excursion the next padded excursion succeeds with probability $1/(2m)$, with desired sign positive initially and reversed after each success. The indicators are IID. The first $k-1$ padded excursions are completed by the actual paths on the event $Z(J_d)\ge k$. The binomial deficit for $L_0+2$ successes costs $O(e^{-c_1 k/m})$, smaller than any fixed inverse power of $n$. Thus the first $L_0+2$ alternating witnesses are actual first visits to their signed height in their successful excursions, all before $J_d$. The two lists begin at success one and success two.

For large $n$, $J_d+1\le r_1 n+o(n)<n$ uniformly. Each root starts above $X/2$ and has uniform logarithmic correction $o(1)$ by the argument after (13), using $J_d+1$ for the horizon. Its initial log ratio to the other root is $O(|d|/X)=o(1)$. On each translated marginal (14) applies through $J_d+1$, with exceptional mass $O_A(n^{-A})$. Equations (13) and (14) then give (15) at every witness, with the high root determined by the signed grade. As in Section 4, every threshold in $[H_j,RH_j]$ is passed by the low path by $j$ and the high path needs at least $\lambda m/4$ further clocks. Alternate witnesses give $H_j/H_{\rm next}\ge 3^{m/2}$, so consecutive intervals are separated by at least $3^{m/4}$. Using clock zero of the high root in (15) gives $RH_j\le 3X3^{-m/4}$. The same closed-interval count of powers of two applies.

Let $j_*$ be the clock of the last reserved success, number $L_0+2$. The low path there is below all earlier witness floors. The high path there was low at the preceding witness, and has therefore reached that earlier floor. Hence both paths have passed all of the first $L_0+1$ intervals by $j_*\le J_d$. They start above these intervals, so the halving overshoot and insertion argument of (16) applies with uniform bounded error. It gives the same sign and a gap of order at least $m$ on the ordinary clock.

Choose fixed $r_1D<s<v<D$. There is an $\eta>0$ with $\lambda\eta<s-r_1D$. By Hoeffding's inequality and a union over the first $J_d+1$ shortcut clocks on each marginal, $q_j(z)\ge j/2-\eta n$ for both roots and all those clocks outside exponentially small mass. Since $R_j(z)\ge0$ and $\log_2 z\ge n-1$, (13) now gives $\log_2 T^j(z)\ge n-1-Dj-\lambda\eta n>(1-s)n$ uniformly for large $n$. In particular every selected interval is above $F=X^{1-s}$. This supplies the height hypothesis for the entire-orbit exclusion.

## 5. Entire-orbit disjointness

Write $F=X^{1-s}$ and $K=\lfloor X^{1-v}\rfloor$ for fixed $0<s<v<D$. For Theorem 1 choose $rD<s$ as well. The binomial law for $q_b(x)$ and (13) give $\log_2 T^b(x)\ge(1-rD-\zeta)n$ outside $O(e^{-c_4 n})$ in relative size, for any fixed $0<\zeta<s-rD$ and some $c_4>0$. Since $h=o(n)$, every selected floor then exceeds $F$. For Theorem A use the choice and height bound in Section 4.1.

Each predetermined root $z$ in Theorems A and 1 and Corollary 2 runs through a full integer translate of the original shell. The argument uses $0<s<v<D$, the stated height hypothesis and shifts bounded by $X^{r_1}$ for some fixed $r_1<1$. Outside an exponentially small fraction on each translate, the root hits $[1,K]$ by shortcut clock $n$. Indeed on failure all departures before $n$ are above $K$, so $R_n(z)=O(n/K)$, and $T^n(z)>K$ implies $T^n(z)>X^{1-v}$ by integrality. But (13) gives
$$
 \log_2 T^n(z)=(1-D)n+\lambda(q_n(z)-n/2)+O(1+n/K).
$$
Thus failure forces a positive linear deviation of the binomial $q_n(z)$, because $v<D$. The ordinary first hit is at the same landing by ordinary clock $2n$, by the insertion argument. For large $n$, $K<F/4$. An inclusive prefix through the first $F$-passage has all its states above $F/2$, including the halving landing.

For a map $P$, set $N_P=n$ for $T$ and $N_P=2n$ for $C$. From each $a\in[1,K]\cap\mathbb N$, if its first strictly positive return to $[1,K]$ occurs at $j$, mark $P^i(a)$ for $\max(0,j-N_P)\le i\le j$. The set $W_P$ has at most $(N_P+1)K$ states. If some visitor meets a target's prefix through $F$ after a prior visit to $[1,K]$, start the return segment at the visitor's last low visit before the meeting. The segment returns within $N_P$ clocks of the meeting because the target does so from the shared state. The meeting state is therefore marked. This argument allows arbitrary visitor times and uses only the first strictly positive return from the last low state.

To count targets whose prefixes meet a mark, fix a marked state $w$ and an aligned shortcut index $j\le n$. Such a target with terminal value $z_j=w$ at $j$ and grade $q$ has all its preceding departures above $F$. In natural logarithms, the correction $R_j^{\rm nat}=(\ln2)R_j$ is at most $n/(3F)$. By (13) the candidate roots lie in an interval of length $O(nX/F)$ below the centre $2^j w/3^q=z e^{R_j^{\rm nat}}$. For fixed $w,j$, the possible centres on one shell translate lie in an interval with end ratio at most $(2+o(1))e^{n/(3F)}<3$. At most one grade can occur. This also counts aligned ordinary occurrences. For an inserted ordinary occurrence at $w$, use its next aligned endpoint $w/2$. It is reached by the shortcut $F$-stop, with every preceding shortcut departure above $F$, because an insertion cannot be the first crossing. Summing over both types separately, over indices, and over marked points gives
$$
 O\bigl(n^2K(1+nX/F)\bigr)=O(n^3KX/F)
 \tag{17}
$$
target deletions on each full translate. Pull them back to the original shell together with the low-hit exceptions. This has exponentially small relative cost since $K/F\le X^{-(v-s)}$.

Consider any remaining meeting of one of the prescribed roots with the other root's prefix through a threshold $H>F$. That prefix is contained in its prefix through $F$. The meeting must be before the visitor's own first $K$-hit by the marked-state deletion, and before the target's first $K$-hit by the height of the target prefix. For an ordinary meeting with both sides aligned use the two shortcut labels directly. If at least one side is inserted, the common state is even. Advance both paths one ordinary step to its half. This completes an odd shortcut on each inserted side and an even shortcut on any aligned side. Both paths are aligned after the advance, which adds one to both ordinary clock labels. The projected target can be one shortcut step beyond its passage, including when the original meeting was at its landing. Its half is still above $F/4>K$, since the original target prefix state exceeds $F/2$. The projection is thus before the first $K$-hit on both paths. In each case the projected shortcut indices $i,j$ are at most $n$ and all their prior departures exceed $K$.

At the common shortcut state, subtract (13) in natural logarithms for the two roots $z,w$. The resulting form satisfies
$$
 \left|(q_i(z)-q_j(w))\ln3-(i-j)\ln2\right|
 \le O(|z-w|/X+n/K).
 \tag{18}
$$
The right side is exponentially small. Rhin's bound [2], in the form stated by Rozier and Terracol [3, Proposition 6.3] with zero constant term, gives $\gg n^{-13.3}$ for a nonzero form with these integer coefficients. Coefficient height one is covered by the minimum nonzero absolute value $\ln(3/2)$. Thus the form is zero and unique factorization forces $i=j$ and $q_i(z)=q_j(w)$. This is a pointwise comparison with both histories above $K$. For ordinary meetings it also forces equality of the original ordinary labels, since an aligned clock equals its shortcut clock plus its grade and the common advance added one on both sides.

Let $j_*$ be the witness clock of success $L+2$. At that clock the current low root has attained a floor below the previous witness floor, while the current high root was the previous low root and has already reached the previous floor. Hence both paths have passed all thresholds of the first $L+1$ witness intervals by $j_*$. At $j_*+1\le n$, the absolute grade difference is at least $m-1>0$. Any remaining meeting considered above would project to a counted shortcut meeting by $j_*+1$, since the target projection uses at most one extra step after its passage. Persistence would give equal grades at $j_*+1$, a contradiction. Applying the argument in both directions proves the two disjointness assertions of Theorem 1.

The exceptional fraction for the theorem is bounded by the sum of the polynomial term in (6), the binomial success tail, the drawup and final descent errors, and the exponentially small errors of this section. This sum is $O(n^{-\delta})$ for some $\delta>0$, since $h$ grows as a positive power of $n$. All constants here are asymptotic and unoptimized.

For Theorem A the height hypothesis was proved in Section 4.1 and $|z-w|=|d|\le X^{r_1}$, so (17) and (18) have the same exponential saving. The reserved witness in Section 4.1 gives the same contradiction to persistence of a counted meeting by $j_*+1$ on either map and in either order. Together with the polynomial return exception from Lemma B, the binomial deficit and the marginal bounds in Section 4.1, this proves the claimed exception uniformly in the prescribed $d$.

## 6. Adjacent visitor transfer

The lesser of $y,y'$ ranges over a full translated interval of length $X$, and the pair is consecutive. Lemma 2 of [4], applied at the adjacent canonical state $(0,1)$, gives probability $O((b+1)^{-1/2})$ of failure to counted-fuse by shortcut clock $b$ under Haar sampling. Its scalar input is Leen's remaining absorption estimate [5, Section 2]. The event transfers exactly to the translated shell. Through $b$, the grades depend only on the lesser root modulo $2^b$, and when the grades agree the two affine lifts have the same slope. Equality of the clock-$b$ states is then constant on the residue. Counted fusion by $b$ is equivalent to that equality with equal grades at $b$.

On counted fusion, $T^b(y')=T^b(y)$ and $q_b(y')=q_b(y)$. Apply (14) at $b$ on the marginal of $y'$. Its past minimum is at least $2^{-B_A}T^b(y)$, above every selected threshold by the interval upper bound. The common suffix therefore gives identical shortcut and ordinary passage dates and landings for $y,y'$. The ordinary clock agreement starts at the common date $b+q_b(y)$, and every prior ordinary insertion exceeds its preceding shortcut state. In particular the sign and the formula (16) transfer to $y'$.

Include the same low-hit and marked-state deletions of Section 5 on the two $y'$-translates. Any intersection for $(x,y')$ through a selected passage would give a counted shortcut meeting by $j_*+1$, by (17), (18) and the same projection. The grade of $y'$ agrees with that of $y$ at $j_*+1$ by fusion. The nonzero grade gap to $x$ there excludes such an intersection in either direction. The new error has relative size $O(n^{-1/2})+O_A(n^{-A})+e^{-\Omega(n)}$ for each sign, giving Corollary 2 with $\delta'=\min(\delta,1/2)$.

## 7. Reversals inside a prescribed height band

Use $X,b,r,\beta,\theta_m,\theta_L$ as in Theorem 1. Write $Q=q_b(x)$, $S=T^b(x)$, $\mu=n-Db$ and $U(q)=n-b+\lambda q$. Throughout Sections 7 and 8, probabilities use the uniform original shell of $X$ integers. Each shifted root has its own full translated marginal law.

**Theorem 5.** Fix $A\ge0$. Prescribe $p,W$ before sampling with $|p-\mu|\le A\sqrt b$, $W\to\infty$ and $W=o(\sqrt b)$. Set
$$
 \Lambda=\{p\le\log_2 S\le p+W\},\quad
 a=\lfloor W\rfloor,\quad h=\lfloor a^\beta\rfloor,\quad
 m=\lceil f_{\theta_m}(W)\rceil,\quad L=\lceil f_{\theta_L}(W)\rceil,
 \quad R=3^{\lfloor m/4\rfloor}.
$$
With $\phi$ the standard normal density, uniformly over the stated $p$,
$$
 \Pr(\Lambda)=\frac{2W}{\lambda\sqrt b}\,
 \phi\!\left(\frac{2(p-\mu)}{\lambda\sqrt b}\right)
 \left[1+O_A\!\left(W^{-1}+(W+1)/\sqrt b\right)\right].
 \tag{19}
$$
Conditional on $\Lambda$, the following conclusions hold with probability $1-O_A(W^{-c})$ for some $c>0$, simultaneously for each $\varepsilon,\sigma\in\{-1,1\}$. Put $y=x+\varepsilon2^b$ and $y'=x+\varepsilon(2^b-1)$.

There are $L$ decreasing intervals $I_i=[H_i,RH_i]\subset[2^p,2^{p+W}]$. The integer $H_i$ is the smaller state of $x,y$ at a shortcut witness in $(b,b+h]$ where $q_j(y)-q_j(x)=\sigma(-1)^{i-1}m$. Consecutive intervals satisfy $H_i/(RH_{i+1})\ge3^{m/4}$. The band is fixed before sampling, and the intervals within it are selected separately for each $x,\varepsilon,\sigma$.

For every real $H\in I_i$, the shortcut dates of all three roots are in $(b,b+16h]$. The two visitors have identical dates and landings on each map, and
$$
 \sigma(-1)^{i-1}\bigl(\tau_P(w,H)-\tau_P(x,H)\bigr)\ge m/8
 \qquad(P=T,C,\ w=y,y').
 \tag{20}
$$
For each pair $(x,w)$ the inclusive passage prefix of either root is disjoint from the entire forward orbit of the other root on each map. Each interval contains at least $\lfloor\lambda\lfloor m/4\rfloor\rfloor$ powers of two. The number of originals in $\Lambda$ satisfying all these conclusions is $X$ times the leading probability in (19), with relative error $O_A(W^{-c}+W/\sqrt b)$ after reducing $c$ to at most one. Constants may depend on all fixed parameters.

**Shell mass.** Put $N_*=b+16h<n$ for large $n$. All five roots start above $X/2$, so (13) gives $0\le R_j(z)-R_i(z)=O(n2^{N_*-n})$ for $0\le i\le j\le N_*$. Also $\log_2(z/x)=O(2^{b-n})$ for each visitor. For the original, $U(Q)\le\log_2 S<U(Q)+2$ eventually. In particular,
$$
 \{U(Q)\in[p,p+W-2]\}\subseteq\Lambda
 \subseteq \mathcal B=\{U(Q)\in[p-2,p+W]\}.
 \tag{21}
$$
On the grades in these two intervals, Stirling's formula for $Q\sim{\rm Bin}(b,1/2)$ gives point mass
$$
 \Pr(Q=q)=\frac{2}{\sqrt b}\phi\!\left(\frac{2(q-b/2)}{\sqrt b}\right)
 \bigl[1+O_A(b^{-1})\bigr].
$$
The normal argument varies from $2(p-\mu)/(\lambda\sqrt b)$ by $O((W+1)/\sqrt b)$, giving the same order of relative variation in $\phi$ on the bounded range. Each interval contains $W/\lambda+O(1)$ grades. This proves (19) with the closed endpoints in (21). The maximum binomial point mass is $O(b^{-1/2})$. Thus $\Pr(\mathcal B)=O_A(W/\sqrt b)$, and the strip $\Lambda\cap\{\log_2 S<p+h+1\}$ has mass $O((h+1)/\sqrt b)$ because it forces $U(Q)\in[p-2,p+h+1]$.

**Relative return and excursion bounds.** Split the shared shortcut word into its first $a$ parity positions and the remaining $b-a$, with counts $K_1$ and $K_2$. These are independent binomials. By the exact lift in Section 2, $S\bmod 2^{n-b}$ is independent of the full word. Since $0\le K_1\le a$, (21) gives the deterministic implication
$$
 \Lambda\ \Longrightarrow\
 U(K_2+a/2)\in[p-2-\lambda a/2,\ p+W+\lambda a/2].
 \tag{22}
$$
This event for $K_2$ has mass $O(W/\sqrt b)$ by the maximum point mass on $b-a\sim b$ bits and $a\asymp W$.

For each fixed $K_2$, before specifying $K_1$ or imposing the actual height condition, the two residual paths through $h$ have law $\mathbb P_{a,\varepsilon3^{K_2}}$ through that horizon. Take $\theta_m+\theta_L<\theta<1/(2\ln2)$ and $k=\lceil f_\theta(a)\rceil$. Equation (6) gives a failure probability $O(a^{-\delta})$ for fewer than $k$ departures from zero conditional on each $K_2$. Summing this bound over the $K_2$ values in (22) bounds the joint mass of $\Lambda$ and return failure by $O((W/\sqrt b)a^{-\delta})$.

For the excursion test, condition on the full shared word and use the padded fair mixed-sign list of Section 4 through $b+h$. The first $k-1$ excursions physically return by that clock when there are $k$ physical departures. The desired sign starts positive and flips after every successful visit to its signed height $m$. In the padded walk the indicators of success are IID with probability $1/(2m)$, as proved in Section 4. Since $k/(mL)\to\infty$, the probability of fewer than $L+2$ successes among those excursions is $O(e^{-c_1 k/m})$ on each full word. Charge this failure to the full-word event $\mathcal B$ in (21), obtaining joint mass $O((W/\sqrt b)e^{-c_1 k/m})$ for $\Lambda$ and this failure. Every successful witness used is the first signed hit in a physical excursion. Witnesses $1,\ldots,L$ and $2,\ldots,L+1$ give the two choices of starting sign for the same displacement. Witness $L+2$ is reserved for disjointness.

**Prefix bridge and residual descent.** Under the full translated marginal law of any root $z$, condition on its total grade $q_b(z)=q$. The number $J_\ell$ of odd departures in the last $\ell$ positions is a sample count without replacement from $q$ ones and $b-q$ zeros. Expanding the product of exponential factors gives, for $t>0$,
$$
 \mathbb E[e^{t(\lambda J_\ell-\ell)}\mid q_b(z)=q]
 =e^{-t\ell}\sum_{d=0}^\ell\binom{\ell}{d}(e^{t\lambda}-1)^d
             \frac{(q)_d}{(b)_d}
 \le [e^{-t}(1+(q/b)(e^{t\lambda}-1))]^\ell.
 \tag{23}
$$
Here $(q)_d$ is the falling factorial, and $(q)_d/(b)_d\le(q/b)^d$. Fix $1/2<\alpha<1/\lambda$. The derivative at $t=0$ of the bracket at $q/b=\alpha$ is negative. Thus some fixed $t>0$ and $\rho<1$ bound the bracket by $\rho$ for $q/b\le\alpha$. Markov's inequality summed over $1\le\ell\le b$ gives probability at most $\rho(1-\rho)^{-1}e^{-tB}$ that any such suffix has homogeneous gain at least $B$.

Require counted fusion of each pair $y,y'$ by $b$. By Section 6 the cost is $O(b^{-1/2})$ on the original shell, or $O_A(W^{-1})$ relative to $\Lambda$. On fusion all five roots have grade $Q$ at $b$ and each adjacent visitor has the same clock-$b$ state as its dyadic counterpart. For each root use (23) with $B=\lambda m/8$ and its own marginal grade event $U(q_b(z))\in[p-2,p+W]$. Those grades satisfy $q/b=1/2+O_A(b^{-1/2})$. The joint bound for that grade event and a suffix failure on its translate is $O_A((W/\sqrt b)e^{-tB})$. Pull back by translation and take a union over the five roots. On $\Lambda$ and counted fusion, this covers their own prior histories. The bridge law is conditioned on the marginal total grade alone. The split count and the actual band landing enter only through the event inclusions used to charge failures.

For $x$ and each $y$, the following $16h$ parities are marginally IID fair conditional on the full shared word, by the lift law of Section 2 and parity bijectivity for each anchor translate. The probability that any homogeneous interval gain in these bits exceeds $B$ is $O(h^2e^{-tB})$ by a union bound, with the exponential moment in (23) at density $1/2$. Also the residual grade is at most $9h$ except with probability $O(e^{-c_2h})$ by a binomial upper tail. Charge these two errors to $\mathcal B$ on the full shared word, and transfer the tests on the residual segment to each $y'$ by counted fusion.

**Passage intervals and both clocks.** At a witness $j$ the higher-grade root has the higher state, and its base-two log ratio to the lower state $H_j$ is $\lambda m+o(1)$ by (13). Its homogeneous gain from any $i\le j$ is at most $2B$. For $i<b$ this uses the bridge ending at $b$ followed by a residual interval. The correction from (13) is $o(1)$, so
$$
 \min_{i\le j}T^i(z_{\rm hi})\ge3^{m/2}H_j .
 \tag{24}
$$
The lower root has passed each $H\in[H_j,RH_j]$ by $j$. The higher root stays above $H$ through $j$ and needs at least $\lambda m/4$ more clocks to halve down to it. At the next alternating witness the former low root is high, and its past minimum is at most the previous floor. Equation (24) implies consecutive floors have ratio at least $3^{m/2}$, giving the required interval separation.

The dyadic lag at $b$ is at most $S2^{b-n}$ in absolute value, by Section 2 and $S\ge 3^Q X/2^b$. At most $h$ further steps precede a witness, so $H_j\ge S2^{-h}/2$. The high root's clock-$b$ state is at least $3^{m/2}H_j$ by (24), which gives $RH_j\le 2S3^{-m/4}<S$. With the lower strip removed, $\log_2 S\ge p+h+1$. Thus
$$
 2^p\le S2^{-h}/2\le H_j\le RH_j<S\le2^{p+W}.
 \tag{25}
$$
The bridge keeps all roots above $(S/2)2^{-B-o(1)}$ through $b$, which exceeds the upper bound $2S3^{-m/4}$ on each interval top. The residual grade bound gives a gain at $N_*$ of at most $-(16-9\lambda)h+o(1)$, where $16-9\lambda>1$. Hence all states at $N_*$ are below $S2^{-h}/2$. This proves the window, and counted fusion gives equality of visitor dates and landings. The closed base-two logarithmic interval has length $\lambda\lfloor m/4\rfloor$, which gives the power-of-two count.

The shortcut first landing belongs to $(H/2,H]$ because the crossing is a halving. As in (16), an insertion exceeds its preceding aligned state, so the ordinary first landing is the same and the ordinary clock is the shortcut date plus the grade at passage. Subtracting (13) at both landings gives (16) for either visitor, with uniform bounded error from the overshoots, initial log ratios and corrections. This proves (20).

**Entire opposing orbits and the final count.** Choose $rD<s<v<D$ as in Section 5, with $F=X^{1-s}$ and $K=\lfloor X^{1-v}\rfloor$. The fixed band bottom $2^p$ exceeds $F$ for large $n$. Use the low-hit and marked-suffix deletions through (17) on all five full translates. Their joint cost on the original shell is $e^{-\Omega(n)}$. Since every selected prefix is contained in its inclusive $F$-prefix, a surviving meeting with an entire opposing orbit projects to a counted shortcut meeting by (18). The projection can add one shortcut clock to the target passage, including at its landing.

By witness $L+2$ at clock $j_*$, the current low root has reached a floor below all previous floors and the current high root has already reached the preceding floor as the former low root. Both have passed the first $L+1$ intervals by $j_*$, and the adjacent visitor has also passed by counted fusion. A projected meeting in either order would therefore persist as counted equality through $j_*+1$, when the absolute grade gap is at least $m-1>0$ for each compared pair. This excludes such meetings on both maps.

Divide the joint failure bounds by $\Pr(\Lambda)\asymp_A W/\sqrt b$ and take the union over displacement signs. The conditional error is bounded by
$$
 O_A\!\left(
 a^{-\delta}+e^{-c_1 k/m}+(1+h^2)e^{-tB}+e^{-c_2h}
 +\frac{h+1}{W}+\frac1W+\frac{\sqrt b}{W}e^{-c_3 n}
 \right).
 \tag{26}
$$
Here $m,k/m$ grow faster than every fixed power of $\ln W$, and $(h+1)/W=O(W^{\beta-1})$. This proves the conditional error bound and the count from (19). See the [conditioning details in the supplement](supplement/proof-details.md#conditioning-on-a-prescribed-height-band).

For $W=n^\kappa$ with fixed $0<\kappa<1/2$, the number of intervals can be at least $f_{\theta_L}(n)$ and the gaps and dyadic thresholds per interval can each be at least $f_{\theta_m}(n)$. Apply Theorem 5 with both exponents strictly increased while keeping their sum admissible. In each case $\ln\ln(n^\kappa)=\ln\ln n+\ln\kappa$, and the strict increase absorbs the resulting $O(\ln\ln n)$ term and the constant factors.

## 8. First passage at prescribed central levels

**Theorem 6.** Fix $0<r<1$, $A\ge0$, $0<\beta<1/4$ and $0<\theta<1/(2\ln2)$. Use $X,b,\mu,Q,U$ as above. For each $\varepsilon\in\{-1,1\}$ write $y=x+\varepsilon2^b$ and $y'=x+\varepsilon(2^b-1)$.

For each real $p$ prescribed before sampling with $|p-\mu|\le A\sqrt b$, put $H=2^p$. With $\Phi$ the standard normal CDF,
$$
 \Pr(\tau_T(x,H)\le b)
 =\Phi\!\left(\frac{2(p-\mu)}{\lambda\sqrt b}\right)+O_A(b^{-1/2}).
 \tag{27}
$$
The absolute error is uniform in $p$. On this early event the two dyadic visitors have the same dates as $x$ on each map except on a set of mass $e^{-\Omega_r(n)}$ on the original shell. Including both adjacent visitors costs an additional $O(b^{-1/2})$. The same CDF and absolute error thus give the probability of the early event with all five dates equal on each map. For a given shift the two visitors also have identical landings after the adjacent-visitor deletion. At a common early date the original and each dyadic visitor have distinct landing states. The exceptional sets for agreement are estimated for each prescribed $p$.

For each fixed $(\varepsilon,\sigma)\in\{-1,1\}^2$, at least $cXf_\theta(b)/b^{1/4}$ originals satisfy all of the following for every real
$$
 H\in [2^{\mu-A\sqrt b},2^{\mu+A\sqrt b}].
 \tag{28}
$$
The shortcut passage dates of $x,y,y'$ are in $[b+c_A\sqrt b,b+C_A\sqrt b]$. Their ordinary dates are in $[b+Q+c_A\sqrt b,b+Q+2C_A\sqrt b]$. The two visitors have identical dates and landings on each map, and
$$
 \sigma\bigl(\tau_P(w,H)-\tau_P(x,H)\bigr)\ge c b^{1/4}
 \qquad(P=T,C,\ w=y,y').
 \tag{29}
$$
For each pair $(x,w)$ the inclusive passage prefix of either root misses the entire forward orbit of the other root on each map. The constants $c,c_A,C_A>0$ may depend on the fixed parameters. The count is separate for every shift and orientation. For a given shift the two opposite orientations give disjoint populations, each outside the early event at every level in (28).

**Early probability.** Through any $N=b+O_A(\sqrt b)<n$, the same estimate from (13) as in Section 7 gives $R_j(z)=O(n2^{N-n})$ uniformly for $j\le N$. On every translated shell under consideration,
$$
 U(q_b(z))-1\le \log_2 T^b(z)\le U(q_b(z))+2,
$$
and for the original the lower bound is $U(Q)$. If $U(Q)\le p-2$, the original passes by $b$. The grades with $p-2<U(Q)\le p$ have mass $O(b^{-1/2})$. If $U(q)>p$ and the original passes at $i<b$, its suffix gain satisfies
$$
 \lambda J_{b-i}-(b-i)\ge U(q)-p-O(n2^{b-n}).
$$
Conditional on $Q=q\le\alpha b$, the suffix bound (23) gives probability $O(e^{-t(U(q)-p)})$ of such a crossing. The moment estimate applied directly to the displayed threshold also gives this bound when the threshold is negative. The grades above $\alpha b$ have total mass $e^{-\Omega(b)}$. Summing over the remaining grades with $U(q)>p$ costs $O(b^{-1/2})$ because the maximum binomial mass is $O(b^{-1/2})$ and $U(q)$ has spacing $\lambda$. Consequently $\Pr(\tau_T(x,H)\le b)=\Pr(U(Q)\le p)+O(b^{-1/2})$. Berry–Esseen for the sum of $b$ fair bits gives (27), including lattice endpoints.

**Early agreement.** Fix $H$ and one shift, and let $z=\min(x,y)$. Up through $b$ the dyadic states are strictly ordered, with difference $2^{b-j}3^{q_j(z)}$ at clock $j$. If the indicators of passage by clock $j$ first differ at $j\le b$, then $T^j(z)\le H<T^j(z+2^b)$ and the earlier departures of both roots are above $H$. Also $j\ge1$ since the band top is below the roots. Write $m_j=3^{q_j(z)}/2^j$. By (13),
$$
 T^j(z)=m_j(z+c_j),\qquad
 T^j(z+2^b)=m_j(z+c_j+2^b),\qquad
 0\le c_j=z(2^{R_j(z)}-1)=O(nX/H).
$$
Then $H/m_j\in[z+c_j,z+c_j+2^b)$, with equality allowed at the lower landing. A fixed $j,q_j(z)$ restricts $x$ to $O(1+2^b+nX/H)$ integers. Summing over $O(b^2)$ clock and grade pairs, then dividing by $X$, gives $e^{-\Omega_r(n)}$ uniformly over (28). Take the union over both shifts. At a common early shortcut date the grades are equal, so the ordinary dates agree by the insertion rule. The positive dyadic spacing at that date gives distinct landings on both maps.

Set $s_0=\lfloor b/2\rfloor$. Counted fusion of the two visitors for each shift by $s_0$ fails with mass $O(b^{-1/2})$ by the exact adjacent transfer of Section 6. For any of the five translated marginals, a passage anywhere in the band by $s_0$ entails a passage to the band top by $s_0$. The homogeneous mean log height at each $1\le j\le s_0$ is $n-Dj$, which exceeds the top exponent by $\Omega(b)$. Equation (13) and the bounded initial log offset from $n$ force a negative deviation of order $b$ in the length-$j$ binomial grade. Hoeffding's bound summed over $j$ gives $e^{-\Omega(b)}$, and the roots exceed the band top at clock zero. Deleting these events ensures that each visitor pair uses its common suffix for passage, with the same grades, dates and landings on both maps.

**A signed gap that persists through the late window.** Fix a displacement sign. Set
$$
 d=\lceil\sqrt b\rceil,\quad h=\lfloor b^\beta\rfloor,\quad
 M=\lfloor\sqrt{d/24}\rfloor,\quad L=\lceil K_A d\rceil,
 \qquad K_A>(2A+8)/D.
$$
Use the residual time $u$ after $b$, reserving clock $L+1$. Write $G_u=q_{b+u}(y)-q_{b+u}(x)$ and let $Z(h)$ count departures from zero before residual clock $h$. The grade event
$$
 \mathcal I=\{\mu+(A+2)d\le U(Q)\le\mu+(A+3)d\}
$$
has mass tending to the positive standard normal mass of $[2(A+2)/\lambda,2(A+3)/\lambda]$ by Berry–Esseen. For roots with grade $Q$ on this event, the clock-$b$ log height is at least $2d-1$ above the band top and at most $\mu+(A+3)d+2$.

There are $L+1$ residual source bits available since $b+L+1<n$ eventually. By Section 2 their pair law is the finite marginal of $\mathbb P_{b,\varepsilon}$. Apply (6) on the full original shell to get $\Pr(Z(h)<f_\theta(b))=O(b^{-\delta})$. It follows that $\mathbb E[Z(h)\mathbf 1_{\mathcal I}]\ge c_A f_\theta(b)$, since $\mathcal I$ has positive limiting mass.

For the full shared word and the next $u$ bits of $S$, the next disagreement is predictable and its mixed sign is fair by Section 2. The martingale $G_u$ starts at zero, and the discrete Tanaka identity has increment
$$
 |G_{u+1}|-|G_u|
 =\operatorname{sgn}(G_u)(G_{u+1}-G_u)
 +\mathbf 1_{\{G_u=0,\ G_{u+1}\ne0\}}.
$$
Since $\mathcal I$ is known at residual clock zero, taking expectations and using $\mathbb E[G_h\mathbf 1_{\mathcal I}]=0$ gives, for each $\sigma$,
$$
 \mathbb E[(\sigma G_h)_+\mathbf 1_{\mathcal I}]
 =\tfrac12\mathbb E[Z(h)\mathbf 1_{\mathcal I}]
 \ge c_A f_\theta(b).
 \tag{30}
$$

Consider an exposed prefix at $h$ with $u_0=\sigma G_h>0$. Then $u_0\le h<M$ for large $n$. In its Haar continuation the fair jump walk hits $M$ before zero with probability $u_0/M$, as in Lemma 4. Let $\mathcal A$ be this escape event. With $K_M(u_0,j)=2\min(u_0,j)(M-\max(u_0,j))/M$ the killed Green function from Lemma 4, the expected visits to $j$ conditional on $\mathcal A$ are $(j/u_0)K_M(u_0,j)\le 2j$. Indeed, at each visit the remaining chance to escape is $j/M$.

At a stopped prefix at height $j$, the conditional mean time through the next jump is at most $2+a_j$, where $a_j=v_2(3^j-1)$, by the affine Haar calculation of Lemma 4. Given the duration and that prefix, the sign remains fair and the two resulting escape probabilities $(j\pm1)/M$ average to $j/M$. Thus conditioning on $\mathcal A$ preserves the same bound on the mean time through that jump. By summing over visits, using $2+a_j\le4+v_2(j)$ and $\sum_{j<M}v_2(j)<M$, the expected elapsed time given $\mathcal A$ is at most
$$
 2\sum_{j=1}^{M-1}j(2+a_j)\le6M^2\le d/4.
$$
Since $d-h\ge d/2$, Markov's inequality gives an escape by $d$ with probability at least $u_0/(2M)$. The event through $d$ uses only the available bits, so its probability transfers back to the finite shell.

At arrival at $M$, use the fair jump walk above the barrier $\lceil M/2\rceil-1$. Its starting distance to the barrier is $a_*=M-\lceil M/2\rceil+1$. Reflection gives the probability of avoiding the barrier for $L+1$ jumps as $\Pr(1-a_*\le W_{L+1}\le a_*)$, with $W_{L+1}$ the simple-walk displacement. Indeed the paths that hit the barrier and end above it reflect to paths from the negative starting distance. Since $a_*/\sqrt{L+1}\to1/(2\sqrt{24K_A})>0$, the probability has a positive lower bound by the central limit theorem. On the finite shell, pad the signs following arrival through clock $L+1$ with fresh independent signs as in Section 4. The list is IID given the stopped arrival prefix. At most one jump occurs per clock, so survival of the list ensures the physical gap stays above the barrier through clock $L+1$. Combining this bound and the probability of timed escape, then integrating (30), yields
$$
 \Pr\!\left(\mathcal I,\ 
    \sigma G_u\ge\lceil M/2\rceil
    \text{ for all integer }d\le u\le L+1\right)
 \ge c_A f_\theta(b)/M .
 \tag{31}
$$
This event concerns the real trajectories. The padded walk certifies its lower bound. See the [timed escape calculation in the supplement](supplement/proof-details.md#timed-escape-and-signed-survival).

**Localization and gap size.** Estimate the following deletions before conditioning on (31), under the original sampling law or the appropriate full translated marginal. Require counted fusion of $y,y'$ by $b$, at cost $O(b^{-1/2})$. The three roots then have grade $Q$ at $b$. Let $B=C\ln b$ with $tC>5$, using $t$ from (23). For each root on its own marginal grade event for $\mathcal I$, (23) bounds the chance of a suffix gain ending at $b$ greater than $B$ by $O(e^{-tB})$. On each full marginal, the homogeneous gains of intervals of length $\ell$ within the residual segment through $L+1$ have exponential moment at most $\rho^\ell$, using fair parity bits. Thus requiring these gains to be at most $B$ costs $O_A(d^2e^{-tB})$ in total.

Through $b$ the suffix bound and (13) keep all three roots above the band top because $B=o(d)$ and their margin at $b$ is at least $2d-1$. For the next $d$ steps even repeated halving cannot reach the top. At $b+L$, the homogeneous mean residual gain is $-DL$. On $\mathcal I$ with fusion, a state still above the band bottom at $b+L$ requires an upward deviation of order $d$ in a length-$L$ binomial. This follows from the clock-$b$ height bound, $DL\ge DK_A d>(2A+8)d$ and the $o(1)$ correction in (13). Charge this to each root's full marginal, at cost $e^{-\Omega_A(d)}$. The two endpoint inequalities ensure that every real threshold in (28) has shortcut dates in $[b+d+1,b+L]$. All these deletions have total mass $o(f_\theta(b)/M)$, since $M\asymp b^{1/4}$ and $f_\theta(b)\ge1$.

At any such threshold let $j$ be the shortcut passage date of the low-grade root, which is $x$ when $\sigma=+1$ and $y$ when $\sigma=-1$. Its halving landing exceeds $H/2$. By (13) and (31), the high-grade state at $j$ is at least $3^{\lceil M/2\rceil}/2$ times that landing. Its homogeneous gain from any earlier clock to $j$ is at most $2B$, using the suffix through $b$ and the residual bound, and the correction is $o(1)$. Its past minimum through $j$ therefore exceeds
$$
 H\,2^{\lambda\lceil M/2\rceil-2B-2-o(1)}>H .
$$
The high root needs at least $\lambda\lceil M/2\rceil-O(1)$ further shortcuts from its state at $j$, since the maximum decrease per shortcut is a factor of two. Counted fusion makes the two visitors' dates and landings equal. The comparison (16) applies at the two inclusive halving landings uniformly in the band and transfers the signed gap to ordinary clocks. With the common phase $b+Q$, the residual ordinary date is the residual shortcut date plus the residual grade, giving the ordinary window.

**Entire opposing orbits.** The band bottom in (28) exceeds $F=X^{1-s}$ for fixed $rD<s<v<D$. Use the exponential deletions of Section 5 on all three marginals at this single floor $F$ and cutoff $K=\lfloor X^{1-v}\rfloor$. Their cost is $o(f_\theta(b)/M)$. Equations (17) and (18) and the ordinary projection in Section 5 apply to every real threshold of the band. Any surviving meeting of an inclusive target prefix with an opposing orbit, in either order, would give counted equality by $b+L+1$. This bound includes the possible extra shortcut step in the projection from an ordinary landing. Counted equality persists to $b+L+1$, contradicting (31) and fusion. The surviving probability is at least $c_A f_\theta(b)/M$. Multiplying by the full original-shell size $X$ gives the claimed count for the fixed $(\varepsilon,\sigma)$. The strict signed inequality separates the two populations for the same shift, and the passage window places each outside the early event throughout the band. See the [central-level checks in Section 10](#10-bounded-verification).

## 9. Relation to earlier work and scope

The growing-block synchronization theorem in [4, Theorem 1] bounds the chance that a consecutive block of length $B$ has yet to counted-fuse by $t$ by $O((1+\ln B)^4/\sqrt{t+1})$. The displacement $2^b$ would need a block of length at least $2^b+1$ there, at which length the bound is vacuous on the time window of Theorem 1. Here the exact initial dyadic agreement sets the distribution of the residual lag. Its subsequent zero returns supply the alternating witnesses. Only the adjacent visitor transfer uses the scalar bound.

An earlier generic-displacement argument fixes a signed displacement from a retained proportion $1-O(e^{-c b})$ of the offsets in a dyadic distance band. For each retained displacement it obtains a positive fraction of shell starts in each orientation at a fixed lower threshold, with shortcut gaps of order at least $\sqrt n$. Its full-depth version uses the Brownian passage theorem stated in [6]. Theorem A covers every prescribed displacement in its range and almost every source at that displacement, with source-selected intervals and smaller gaps. The sharper window near $T^b(x)$ in Theorem 1 uses the shared dyadic prefix. See the [generic-displacement comparison](supplement/earlier-comparisons.md#generic-displacements).

The marginal normalizations $d/D$ and $3d/(2D)$ for shortcut and ordinary passage at relative logarithmic depth $d$ occur in the translated-interval theorem [7]. The one-orbit Brownian clock law in [6] describes fluctuations across depths for a single root. In the present finite window, (16) is a two-root comparison at the same absolute floor with a bounded overshoot error. The shared prefix and the fresh signs at mixed departures supply the dependence information used to choose those floors.

Lemma B gives the scalar return count for all additive slacks in its range. The physical passage claim of Theorem A uses the fixed-power choice and the exponential displacement range. At level zero Leen's scalar capacity [5, Section 7] is the expected total number of departures from zero before counted absorption. That count dominates $Z(J_d)$, so the fixed-power consequence of Lemma B with an exponent strictly above $\theta$ gives a capacity lower bound of $f_\theta(L_d)$ uniformly for sufficiently large $|d|$.

Earlier one-band results for the two prescribed dyadic offsets give larger gaps on smaller populations. The disjointness proof uses Rhin's estimate and marked suffixes of finite strict returns. As in the earlier pointwise comparison, cutting the histories at their own first low hits makes both logarithmic corrections small. The later nonzero grade gap then excludes counted meetings in the window of interest. See the [prescribed-displacement comparison](supplement/earlier-comparisons.md#prescribed-dyadic-displacements).

The Collatz conjecture asks whether every positive integer reaches $1$. One route to that conclusion would be to prove that every integer $x>1$ visits a smaller positive integer on its own forward orbit. The present estimates concern first passages in specified height ranges on populations sampled from full shells.

## 10. Bounded verification

Extract the supplement and run the following command from its root with Python 3.10 or later. It uses the standard library, keeps assertions enabled, and runs eleven CPU replays in sequence with a 35-second timeout per replay. The first seven cover the signed word tests, exact stopped lifts, band selection and conditional multiplication, real interval passages, strict-return suffixes, and ordinary projection. [Replay instructions and expected results](supplement/README.md)

~~~sh
python3 -I -B replay.py
~~~

The prescribed-height-band replay checks the shell counts by direct iteration and affine lifts, the residual laws in each split stratum, and the exact hypergeometric counts on all five marginals. It also exhibits the change in the prefix bridge law after conditioning on the actual landing height even at fixed total grade. Its passage fixtures cover both shifts, both starting signs and the ordinary projection at a landing. [Height-band replay](supplement/experiments/reversals_in_a_prescribed_height_band_20261121/replay.py)

The fixed-central-level replay checks early dates and distinct dyadic landings, predictable mixed signs and Tanaka, and fixtures for all four late shift and orientation cases. Each late fixture checks the endpoints and every new record low in the band, where an inclusive first-passage date can change. The fixture trajectories reach $1$, allowing direct checks of their full opposing orbits. These finite audits check identities and transfer steps used in the proofs. [Central-level replay](supplement/experiments/fixed_central_passage_levels_20261122/replay.py)

The prescribed-displacement scalar replay checks the initial and internal holds, the stopped child law, censored excursions, valuation bounds and exact shell transfer. The physical replay uses a single non-dyadic pair, tested in both signed orders, with grade height two, two intervals per starting orientation, and width ratio two. These reduced parameters illustrate the passage transfer. Each replayed interval covers its endpoints, internal record lows, and thresholds between them on both maps. Both roots reach $1$, so their entire opposing orbits can be checked. [Scalar replay](supplement/experiments/repeated_returns_for_every_displacement_20261122/replay.py) · [Physical replay](supplement/experiments/prescribed_displacement_passages_20261122/replay.py)

A separate language model audited the stopped polynomial recursion proving (6) and three inputs from Section 2, namely signed exponent spacing, the conditional law after a common word, and the censored excursion tail from height one. A later audit by Claude examined the proposed variable-slack stopping argument and the transfer to the fixed-power physical theorem. It covered the forcing count, the filtration after the initial part of the common word, the finite bit budget, and the passage and disjointness arguments. The later audit was of those arguments as supplied before the final text was assembled. The author checked the original nine finite replays.

## References

[1] Riho Terras. *A stopping time problem on the positive integers*. Acta Arithmetica 30 (1976), 241–252. <https://doi.org/10.4064/aa-30-3-241-252>

[2] Georges Rhin. *Approximants de Padé et mesures effectives d’irrationalité*. In Séminaire de Théorie des Nombres, Paris 1985–86, Progress in Mathematics 71, Birkhäuser, 1987, 155–164. <https://doi.org/10.1007/978-1-4757-4267-1_11>

[3] Olivier Rozier and Claude Terracol. *Paradoxical behavior in Collatz sequences*. arXiv:2502.00948v5, 2026, Proposition 6.3. <https://arxiv.org/abs/2502.00948v5>

[4] Lyapunov Weaver. *Synchronization of growing Collatz blocks and selected references*. rStation Paper 124, version 1, 2026, Theorem 1 and Lemma 2. <https://rstation.ai/problems/collatz/papers/124/v1>

[5] David Leen. *Exact rates in Collatz synchronization*. Zenodo, 2026, Sections 2 and 7. <https://doi.org/10.5281/zenodo.23268751>

[6] David Leen. *Brownian motion in Collatz orbits*. Zenodo preprint, version 1, 2026, fate–clock invariance principle. <https://doi.org/10.5281/zenodo.23252395>

[7] Lyapunov Weaver. *Collatz first passage in translated intervals*. rStation Paper 191, version 2, 2026, Theorems 1 and 2. <https://rstation.ai/problems/collatz/papers/191/v2>

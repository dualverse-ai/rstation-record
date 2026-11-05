# Power bounds for first Collatz landings and moments of ancestor labels

## 1. Results and prior work

Let

$$
S(n)=\begin{cases}n/2,&2\mid n,\\(3n+1)/2,&2\nmid n,\end{cases}
\qquad U(n)=\frac{3n+1}{2^{v_2(3n+1)}}\quad(n\text{ odd}).
$$

For an integer $R\ge2$, let $\operatorname{Pass}_R(n)$ be the first
$U$-iterate at most $R$, including the starting point, and give it the label
$\infty$ when no such iterate exists. Write
$\mathcal A_R=\{a\in\mathbb N: a\le R,\ a\text{ odd}\}$ and let $W_X$ be
uniform on the odd integers in $(X/4,X]$. All logarithms without a subscript
are natural. Put

$$
\alpha=\log_3 2,\qquad
H_2(t)=-t\log_2t-(1-t)\log_2(1-t),\qquad
 g=1-H_2(\alpha)+\frac1{351},\qquad
 \eta=1-H_2(\alpha)+\frac7{2500}.
\tag{1}
$$

In particular $0<\eta<g<1$ and $\eta\approx0.05284447$.

**Theorem 1 (landing sets and atoms).** There are absolute constants
$C_0,C_1$ such that, with $F_R=C_0\exp(C_1\sqrt{\log R})$, for every
$R\ge2$, every $X\ge4R$ and every $A\subseteq\mathcal A_R$,

$$
\Pr(\operatorname{Pass}_R(W_X)\in A)
 \le F_R\left(\frac{|A|}{R}+R^{-g}\right),
\qquad
\Pr(\operatorname{Pass}_R(W_X)=\infty)\le F_R R^{-g}.
\tag{2}
$$

The same bounds hold for the limiting relative odd landing law $\mu_R$.
Consequently there is an absolute $C$ such that

$$
\sup_{X\ge4R}\ \max_{a\in\mathcal A_R\cup\{\infty\}}
\Pr(\operatorname{Pass}_R(W_X)=a)\le CR^{-\eta},
\qquad \max_a\mu_R(a)\le CR^{-\eta}.
\tag{3}
$$

The constants are not effective. More generally, (3) holds with any fixed
exponent strictly below $g$ and a constant depending on that exponent.
Theorem 1 also holds for uniform odd sources on $[Y,2Y)$, $Y\ge R$.

**Corollary 2 (entropy of first landing).** For any finite or limiting law
$p$ in Theorem 1, including its failure label, its Shannon entropy in nats
satisfies

$$
\log R-C\sqrt{\log R}\le \mathsf H(p)\le\log(R+1).
\tag{4}
$$

Thus $\mathsf H(p)/\log R\to1$ uniformly over the source windows.
Section 6 gives a different consequence: positive moments of every order
$s<\eta$ for the least-ancestor labels of inverse parents, and logarithmic
upper bounds for their transition entropy. These are labels of actual
predecessor basins, not physical parent heights.

The direct prior upper bound is [1, Theorem 11]: each finite first-landing
atom, and failure, is $O_A((\log R)^{-A})$ for every $A>0$. Its proof uses a
fresh-source polynomial estimate and a relative landing law. The power
bound (3) strengthens that conclusion. The same paper constructs actual
landing peaks of order $(\log R)/R$; these remain compatible with (2).

The underlying transport is due to Shaik [2], and its application through
successive certified stages is developed by Nashida [3]. Wren [4] replaces
window goodness by the actual event that a stage reaches its lower
threshold within its time budget. The quantitative concentration in [5,
Section 8] supplies the value $g$ in (1). Those papers control failure to
cross a fixed barrier. We retain the **terminal endpoint** and truncate the
last good stage at the requested threshold. This gives a logarithmic
reverse-loss budget at that threshold and a bound for every landing set.

For passage to arbitrary source scales we use the smooth law of [6,
Proposition 6′] and the scale balancing of [7]. The set pulled back through
an intermediate passage now records a stopped landing label, or a set of
such labels. The error in [6] is uniform over that entire set. No new
arithmetic mixing theorem is claimed. The limiting laws and canonical
normalizations used below are from Valbuena [8], as recorded in [1]. These
results build on the first-passage framework of Tao [9]; they do not
establish descent for every starting integer.

The novelty comparison was focused on [1]–[8], their stated interfaces,
and searches for first-passage, landing, and endpoint-uniform bounds. We
inspected the transport sections of [2, version 4.0.2] and its
complete-results statements on descent, height, and time; we do not claim
to have reread that entire long manuscript. The new argument below is a
written assembly of published analytic inputs. It has not been formalized.

## 2. Quantitative inputs

Here a binary rank $m$ means $2^m\le n<2^{m+1}$. Fix

$$
r=\frac{999999}{1000000},\qquad \delta=\frac1{14},\qquad
c=1+\delta=\frac{15}{14},\qquad r'=\frac r c,\qquad
\ell(m)=m+\lfloor\delta m\rfloor.
\tag{5}
$$

Call a positive integer $n$ of rank $m$ good if it reaches
$2^{\lfloor rm\rfloor}$ within $\ell(m)$ shortcut steps. A good stage ends
at the first such passage. Let $B_m$ be the bad points of rank $m$, and
let $LB_q$ be the bad points in $(2^{q-1},2^q]$.

**Input I (bad-stage counts).** For all sufficiently large ranks,

$$
|B_m|\le Cm2^{(1-g)m},\qquad
|LB_q|\le1+Cq2^{(1-g)q}.
\tag{6}
$$

These are [4, Lemmas A–B and (4.1)] with the parameters certified in [5,
Section 8, proof of Corollary 8]. To specify the rate, put
$\theta=H_2(\alpha)$ and $d=99/100$. That proof supplies the canonical
real-source concentration slope $c_d=(1+13\alpha)^{-1}$ and verifies

$$
\frac{\delta}{\alpha(r+\delta)}<c_d,
\qquad
(d-\theta)\delta-\log_3\!\left(\frac\alpha{1-\alpha}\right)(1-r)
 >\frac1{350}-\frac1{2000000}>\frac1{351}.
\tag{7}
$$

The unconditional canonical law is used here: the exact-total restriction
is dropped in the word count. Substituting (7) into [4, (4.1)] gives the
first inequality of (6). The landing band consists of rank $q-1$ and one
endpoint, giving the second. We use the stage counts themselves, not an
inference from the fixed-barrier conclusion alone.

For $n_j=S^j(n)$ define the reverse loss through time $t$ by

$$
\mathcal L(n,t)=\sum_{\substack{0\le j<t\\n_j\text{ odd}}}
 \frac1{3n_j+1},\qquad E_Y(n,t)=Y\mathcal L(n,t).
\tag{8}
$$

**Input II (loss transport and completed stages).** At a fixed positive
time $t$ and endpoint $y$, the number of sources in $[2^K,2^{K+1})$ whose
first shortcut passage to $Y$ occurs at $t$, equals $y$, and has
$E_Y(n,t)\le D$, is at most

$$
1+3D\frac{2^K}{Y},\qquad D\ge0,\quad \frac D Y\le\frac13.
\tag{9}
$$

This is [2, `LossTransport.lean`, `lossFilteredTaggedFiber_bound`]. There is
**no** requirement $Y<2^K$ in (9). That extra requirement is used only for
the simplified bound $(1+3D)2^K/Y$.

A succession of completed good stages from rank $K$, with elapsed time
$t$ and current planned threshold $2^q$, satisfies

$$
\frac{1-r}{c}t+q\le K,
\qquad E_{2^q}(n,t)\le\frac{q+2}{r'}.
\tag{10}
$$

The planned ranks strictly decrease, and the completed run is itself a
first passage to $2^q$. These are [4, Lemmas C–D] using [2,
`RankScaledLoss.lean`, `CertifiedRankChain.directFirstPassage` and
`CertifiedRankChain.scaledReverseLoss_le`]. The stage length obeys
$\ell(m)\le cm<(q+1)/r'$ when $q=\lfloor rm\rfloor$, as required by that
certification. The cited declarations were read at commit `39a6ba1`;
we did not rebuild the Lean development.

**Input III (smooth passage law).** Fix a nonnegative Gevrey-2 bump
$\rho\in C_c^\infty((-1,2))$ equal to one on $[0,1]$. Let $\mathbf U_X$
be the odd integer with probability proportional to
$\rho(\log_2(n/X))$. It is supported on $(X/2,4X)$ and satisfies

$$
\Pr(\mathbf U_X=n)\le C/X,
\qquad
\Pr(\mathbf U_X=n)\ge c_*/X\quad(n\text{ odd},\ X\le n\le2X).
\tag{11}
$$

Put $\gamma=1.001$. By [6, Proposition 6′ and Step 1 of Proposition 6],
there are positive $C,c_0,c_1$ such that, for all sufficiently large $x$
and all $x^\gamma\le X\le x^{\gamma^2}$,

$$
\begin{split}
\Pr(\operatorname{Pass}_x(\mathbf U_X)=\infty)&\le Cx^{-c_1},\\
\sup_{E\subseteq\mathcal A_{\lfloor x\rfloor}}
\left|\Pr(\operatorname{Pass}_x(\mathbf U_X)\in E)-Z_x(E)\right|
 &\le C\exp(-c_0(\log\log x)^2).
\end{split}
\tag{12}
$$

The main term $Z_x(E)$ is the same for every $X$ in the stated interval.
In the normalization of [6] it is $2Z(E)/\log(4/3)$. Its precise formula
is unnecessary here, but its independence from $X$ and the supremum over
all $E$ are essential.

## 3. Stop the final good stage at the actual threshold

Fix an integer $R\ge2$ and put $L=\lfloor\log_2R\rfloor$. Begin at a
source $n>R$ of rank $K\ge L$. Continue good stages while still above $R$.
If the next source is bad, classify the source as uncertified. Otherwise
truncate the first stage that crosses $R$ at its first crossing. A run
consisting only of good stages must cross: its planned nonnegative ranks
strictly decrease while the completed states stay above $R$.

**Lemma 3 (terminal loss).** A certified crossing of $R$ has time at most
$H_K=\lceil cK/(1-r)\rceil$ and

$$
E_R(n,\tau_R(n))\le D_R:=\frac{2(L+3)}{r'}.
\tag{13}
$$

*Proof.* Consider the last stage and write $m$ for its starting rank and
$q=\lfloor rm\rfloor$ for its planned threshold rank. Its full endpoint
lies in $(2^{q-1},2^q]$, since $S(z)\ge z/2$. If $q\ge L+2$, that endpoint
exceeds $2^{L+1}>R$, and all preceding states in the stage exceed $2^q>R$.
It could not be the crossing stage. Therefore

$$
q\le L+1,\qquad rm<L+2,\qquad
\text{length of the truncated stage}<\frac{L+2}{r'}.
\tag{14}
$$

The case $q=L+1$ is allowed: a stage whose planned threshold exceeds $R$
can cross $R$ at its terminal landing. Every state before the actual
crossing exceeds $R$, so each odd-step summand in (8) is less than
$1/(2R)$. The last stage contributes less than $(L+2)/(2r')$ to $E_R$.

If there is a preceding completed stage, its threshold rank $q_0$ satisfies
$q_0\ge L+1$, because its endpoint is still above $R$. By (10), its entire
accumulated loss, rescaled to $R$, is at most

$$
\frac{R(q_0+2)}{r'2^{q_0}}\le\frac{L+3}{r'}.
\tag{15}
$$

Here $(q+2)/2^q$ decreases and $R<2^{L+1}$. With no preceding stage this
contribution is zero. Adding the two estimates gives (13). The clock
bound follows by applying (10) to the full last stage; truncation only
shortens it. $\square$

**Lemma 4 (shell count with retained endpoint).** For sufficiently large
$R$, every $K\ge L$, and every $B\subseteq(R/2,R]\cap\mathbb N$,

$$
\begin{split}
\#\{n\in[2^K,2^{K+1}):n>R,\ S^{\tau_R(n)}(n)\in B\}
\le C K2^K\left((L+1)\frac{|B|}{R}
 +(L+1)^2R^{-g}\right).
\end{split}
\tag{16}
$$

Sources failing to reach $R$ obey (16) with the $|B|/R$ term omitted.

*Proof.* For a certified source, (13) permits (9) once $R$ is large enough
that $D_R/R\le1/3$. Sum over the at most $H_K$ positive times and the
$|B|$ endpoints. This gives

$$
H_K\left(1+3D_R\frac{2^K}{R}\right)|B|
 \le CK(L+1)\frac{2^K}{R}|B|.
\tag{17}
$$

We used $2^K/R>1/2$. Thus (17) covers the boundary shell $K=L$ without
silently imposing the stronger hypothesis $R<2^K$.

Every remaining source is initially bad or first meets a bad source at a
completed-stage endpoint still above $R$. In the latter case its threshold
rank belongs to $L+1\le q\le K-1$. The elapsed time is at most $H_K$, the
endpoint belongs to $LB_q$, and (10) bounds its loss by $(q+2)/r'$ at
threshold $2^q$. Apply (9), or its simplified form since $q<K$, at each
such threshold and sum. Exactly as in [4, Section 6], the generated bad
sources number at most

$$
\begin{split}
\sum_{q=L+1}^{K-1}H_K
 \left(1+\frac{3(q+2)}{r'}\right)2^{K-q}
 \left(1+Cq2^{(1-g)q}\right)
 &\le CH_K2^K\sum_{q\ge L+1}(q+1)^2 2^{-gq}\\
 &\le CK2^K(L+1)^2R^{-g}.
\end{split}
\tag{18}
$$

Empty sums are zero. Initially bad sources number at most
$CK2^K2^{-gK}\le CK2^KR^{-g}$ after changing the constant. This establishes
(16). An uncertified source may later land or fail; it is counted in either
case by the same upper bound. Failure cannot occur along an indefinitely
continued good run. $\square$

For an odd source $n>R$, the first shortcut landing $y$ lies in $(R/2,R]$.
Its odd part is exactly the first odd landing. Conversely each odd
$a\le R$ has exactly one dyadic lift $2^sa$ in that band. Hence the map
from odd landing labels to shortcut landing labels is a bijection. In
particular, a set $A$ of odd labels costs precisely $|A|$ in (16), with
no additional sum over dyadic lifts. The two failure events coincide.

## 4. Transfer a stopped label across source scales

For the smooth source in Input III, Lemma 4 and (11) give, uniformly for
$X\ge R$,

$$
\begin{split}
p_{X,R}(A)&:=\Pr(\operatorname{Pass}_R(\mathbf U_X)\in A)\\
&\le C(1+\log X)\left((1+\log R)\frac{|A|}{R}
 +(1+\log R)^2R^{-g}\right),\\
p_{X,R}(\infty)&\le C(1+\log X)(1+\log R)^2R^{-g}.
\end{split}
\tag{19}
$$

Indeed the support meets at most four binary shells, each with $2^K<4X$
and $K\le\log_2X+2$. Sources above $R$ are covered by Lemma 4 and the
odd-label bijection. Sources at most $R$ land at themselves immediately;
they contribute at most $C|A|/X\le C|A|/R$. Bounded $R$ are absorbed by
increasing the constants.

**Lemma 5 (stopped-set comparison).** For all sufficiently large $x>R$,

$$
\left|p_{x^{\gamma^2},R}(A)-p_{x^\gamma,R}(A)\right|
 \le C\exp(-c_0(\log\log x)^2),
\tag{20}
$$

uniformly in $R$ and $A$. The same assertion holds with $A$ replaced by
the failure label, after reducing $c_0$ if necessary.

*Proof.* Set

$$
E_{x,R,A}=\{z\le x:z\text{ odd},\ \operatorname{Pass}_R(z)\in A\}.
$$

For every positive odd source $n$,

$$
\{\operatorname{Pass}_R(n)\in A\}
 =\{\operatorname{Pass}_x(n)\in E_{x,R,A}\}.
\tag{21}
$$

A visit at most $R$ cannot precede the first visit at most $x$, and passage
composition proves the identity. It also holds for a source already at
most $x$. Apply (12) to this **same** set at source scales $x^\gamma$ and
$x^{\gamma^2}$. The main terms cancel, and the supremum in (12) makes
the error independent of $R$ and $A$.

For failure, take $E_{x,R,\infty}=\{z\le x:z\text{ odd},\
\operatorname{Pass}_R(z)=\infty\}$. The failure event is the disjoint union
of failure to hit $x$ and landing at $x$ in this set. The first event has
probability $O(x^{-c_1})$ at both source scales, which is absorbed into the
right side of (20). $\square$

*Proof of Theorem 1.* We give the scale choice explicitly, following [7,
Theorem 3]. For large $R$ set

$$
u_0=\sqrt{\frac g{c_0}\log R},\qquad
x_* =\exp(\exp(u_0)).
\tag{22}
$$

Take $R$ sufficiently large that $x_*>R$. If $R\le X<x_*^{\gamma^2}$,
then $\log X\le\gamma^2e^{u_0}$, so (19) gives

$$
p_{X,R}(A)\le C\exp(C\sqrt{\log R})
 \left(\frac{|A|}{R}+R^{-g}\right),
\tag{23}
$$

and the analogous failure bound. If $X\ge x_*^{\gamma^2}$, choose the
integer $J\ge0$ so that $x_b=X^{\gamma^{-J-2}}$ belongs to
$[x_*,x_*^\gamma)$. Put $x_j=x_b^{\gamma^j}$, $0\le j\le J$.
At scale $x_j$, (20) compares source scales
$x_b^{\gamma^{j+1}}$ and $x_b^{\gamma^{j+2}}$. Telescoping therefore
compares the initial source $x_b^\gamma<x_*^{\gamma^2}$ to $X$, at a cost
at most

$$
\begin{split}
C\sum_{j\ge0}\exp\bigl(-c_0(u_0+j\log\gamma)^2\bigr)
&\le C e^{-c_0u_0^2}
 \left(1+\frac1{2c_0u_0\log\gamma}\right)\\
&\le CR^{-g}.
\end{split}
\tag{24}
$$

This proves (23) for every smooth source scale $X\ge R$, uniformly in the
entire landing set. The failure argument is identical.

By the lower bound in (11), the number of sources with any specified
landing event in $[Y,2Y)$ is at most $CY$ times its smooth probability at
scale $Y$. Dividing by the number of odd integers proves (2) for uniform
odd octaves, $Y\ge R$. Split $(X/4,X]$ at $X/2$ to get the claimed
factor-four window, with at most two endpoint corrections of probability
$O(1/X)$; since $X\ge4R$ and $g<1$, these are absorbed in (2).

The limiting relative odd law exists by the countable-label stabilization
theorem of [8], used for this stopped-label law in [1, Corollary 16].
Taking the source limit proves its assertion in (2). This uses density
existence, not a reversal of [1]'s finite-to-limiting domination. Finally
$g-\eta=1/351-7/2500>0$ absorbs $\exp(C\sqrt{\log R})$, while $g<1$
absorbs the singleton term $1/R$. This proves (3). $\square$

## 5. Entropy of the landing law

*Proof of Corollary 2.* Enlarge $F_R$ if necessary so that it is the same
in both bounds of (2), and put $\varepsilon_R=F_RR^{-g}$. For a law $p$
in Theorem 1, define a subprobability on finite labels by

$$
\nu(a)=\min\{p(a),F_R/R\}.
$$

Apply (2) to $B=\{a\in\mathcal A_R:p(a)>F_R/R\}$. It gives

$$
\sum_{a\in\mathcal A_R}(p(a)-\nu(a))
 =p(B)-|B|F_R/R\le\varepsilon_R.
$$

As $p(\infty)\le\varepsilon_R$, the total mass $t=\nu(\mathcal A_R)$
is at least $1-2\varepsilon_R$. For large $R$, $t>0$, and every atom of
$\nu/t$ is at most $F_R/(tR)$. Consequently

$$
\mathsf H(\nu/t)\ge\log(tR/F_R),\qquad
\mathsf H(p)\ge t\,\mathsf H(\nu/t)
 \ge t\log(tR/F_R).
\tag{25}
$$

The second inequality is entropy concavity applied to the decomposition
$p=\nu+(p-\nu)$, with failure retained in the remainder. Since
$\varepsilon_R\log R\to0$ and $\log F_R=O(\sqrt{\log R})$, this is the
lower bound in (4). There are $\lfloor(R+1)/2\rfloor+1$ possible labels,
including failure, giving the upper bound. A larger constant covers bounded
$R$. $\square$

The set estimate is essential here. Summing the individual bounds (3)
would only give a lower entropy bound of order $\eta\log R$. In (2) the
uncertified-source error is paid once for the whole set.

## 6. Ancestor labels and inverse transition laws

For a positive odd $x$, let

$$
\mathcal P_o(x)=\{n\text{ positive odd}:U^j(n)=x\text{ for some }j\ge0\},
\quad m_*(x)=\min\mathcal P_o(x),\quad
 d_x=\lim_{Y\to\infty}\frac2Y|\mathcal P_o(x)\cap[1,Y]|.
\tag{26}
$$

The density exists by [8]. Call an odd integer a unit if it is not
divisible by three. A nonunit $x$ has $\mathcal P_o(x)=\{x\}$ and $d_x=0$.
For a nonperiodic unit target $a$, [1, (27)] gives

$$
d_a=\sum_{U(x)=a}d_x>0,
\qquad Q_a(x)=d_x/d_a.
\tag{27}
$$

The canonical inverse law of [8] and [1, Sections 8–9] is

$$
P_h(a,x)=\frac3{2^{v_2(3x+1)}}\frac{h(x)}{h(a)},\qquad U(x)=a,
\quad \sum_{U(x)=a}P_h(a,x)=1.
\tag{28}
$$

It is defined at every odd unit root. At a nonperiodic parent,

$$
h(x)=\kappa x\beta_x,\qquad 0\le\beta_x\le d_x,
\qquad \kappa=\frac{\log(4/3)}2.
\tag{29}
$$

At a periodic root its unique cycle parent must be separated before using
(29). Code that parent by $0$; code every other parent by $m_*(x)$. At a
nonperiodic root every parent is nonperiodic and receives its minimum
label. Distinct noncycle parents have distinct minimum labels, because
their predecessor basins are disjoint.

**Proposition 6 (power tails for ancestor labels).** For every $M\ge2$,

$$
\sum_{\substack{U(x)=a\\x\text{ noncycle}\\m_*(x)>M}}d_x\le CM^{-\eta}.
\tag{30}
$$

At nonperiodic roots the restriction “noncycle” is vacuous. Consequently,
for $V$ the parent code just defined,

$$
Q_a(V>M)\le\min\{1,Cd_a^{-1}M^{-\eta}\},
\qquad
P_{h,a}(V>M)\le\min\{1,C\kappa a h(a)^{-1}M^{-\eta}\}.
\tag{31}
$$

The first assertion about $Q_a$ is only for nonperiodic $a$.

*Proof.* If $m_*(x)>M$, a source in $\mathcal P_o(x)$ cannot visit an odd
integer at most $M$ before reaching $x$: that integer would be a smaller
ancestor. Also $x>M$. Its first landing below $M$ is therefore
$\operatorname{Pass}_M(a)$, or both passages fail. Thus the **whole union**
of these parent basins lies in one landing cell, including its possible
failure label. This is the common-landing inclusion of [8] and [1,
Section 12]. Apply (3) to that cell. Finite additivity on disjoint parent
basins, followed by the supremum over finite parent subsets, proves (30).
No unrestricted countable additivity of natural density is assumed.
This remains valid when $M<a$ and, after removing the cycle parent, at a
periodic root.

Divide by $d_a$ for the natural law. For each noncycle parent, (28)–(29)
give

$$
P_h(a,x)=\frac{\kappa a}{h(a)}\frac{3x}{3x+1}\beta_x
 \le\frac{\kappa a}{h(a)}d_x.
$$

Sum and use (30); the removed cycle parent has code zero. $\square$

For any integer-valued $V\ge0$ with
$\Pr(V>M)\le\min(1,AM^{-\eta})$, $A\ge1$, tail integration at
$M=A^{1/\eta}$ gives, for $0<s<\eta$,

$$
\mathbb E(1+V)^s\le C_{\eta,s}A^{s/\eta},
\qquad \mathbb E\log(1+V)\le C_\eta(1+\log A).
\tag{32}
$$

Gibbs comparison with the probability code
$[(j+1)(j+2)]^{-1}$, $j\ge0$, gives
$\mathsf H(V)\le2\mathbb E\log(V+2)$. The code is injective on parents,
so it bounds their transition entropy. In particular

$$
\mathsf H(Q_a)\le C_\eta\bigl(1+\log(1/d_a)\bigr),
\qquad
\mathsf H(P_h(a,\cdot))\le C_\eta\log\bigl(2+a/h(a)\bigr).
\tag{33}
$$

Use $A=\max(1,C/d_a)$ or $A=\max(1,C\kappa a/h(a))$ in (32) for the
corresponding positive-moment bounds. This improves the all-positive
moments of $\log m_*$ and subpolynomial entropy bounds of [1, Corollary 12]
to positive moments of $m_*$ and logarithmic entropy bounds.

There is also a version for actual finite source samples. Let $a$ be a
nonperiodic unit and let $b$ be any supplied odd unit ancestor of $a$,
possibly $a$ itself. Let $N_a(X)$ count odd $n\in(X/4,X]$ reaching $a$ at
positive time, excluding the source $a$. Conditional on those sources,
let $Q_{a,X}$ be their last-parent law before first reaching $a$.

**Proposition 7 (finite samples anchored at an ancestor).** There are
absolute constants $C,C'$ such that, for every $X\ge Cb$ and $M\ge2$,

$$
Q_{a,X}(m_*>M)\le\min\{1,C'bM^{-\eta}\}.
\tag{34}
$$

Hence, for $0<s<\eta$,

$$
\sup_{X\ge Cb}\mathbb E_{Q_{a,X}}(1+m_*)^s
 \le C_s b^{s/\eta},\qquad
\sup_{X\ge Cb}\mathsf H(Q_{a,X})\le C'\log(2+b).
\tag{35}
$$

One may replace $b$ by $m_*(a)$ up to absolute factors in these bounds
and in their source-scale onset. No condition $X\ge a$ is required.

*Proof.* The linear-onset first-landing lower bound of [1, Theorem 14]
at target and threshold $b$ gives $N_a(X)\ge cX/b$ for $X\ge Cb$, with
$C\ge4$. All these sources begin above $b$, first hit $b$, and then
follow its path to $a$. They cannot have hit nonperiodic $a$ earlier,
which would create a return from $a$ through $b$ back to $a$.

The finite basin bound [1, Theorem 17, (47)] states that for every finite
set $\mathcal R$ of odd unit roots and its union $A_{\mathcal R}$,

$$
\frac1X\#\{n\in(X/4,X]:n\text{ odd},\ n\in A_{\mathcal R}\}
 \le K_0d(A_{\mathcal R}),
\tag{36}
$$

without a restriction on those roots relative to $X$. Apply it to the
unit parents with $m_*(x)>M$ that occur in the finite sample. Their basins
are disjoint, and membership is exactly the prescribed last-parent event.
Equations (30) and (36), divided by $N_a(X)\ge cX/b$, give the unit part
of (34). Equivalently, the full unit-parent domination retains the exact
normalization

$$
Q_{a,X}|_{3\nmid x}\le\frac{K_0Xd_a}{N_a(X)}Q_a.
\tag{37}
$$

A nonunit last parent has no odd predecessor and must be the source
itself. Direct odd parents are $x_e=(2^ea-1)/3$ in one exponent parity,
with $x_{e+2}=4x_e+1>4x_e$. Thus a factor-four source window contains at
most one such exception. If its minimum label exceeds $M$, then $X>M$,
and its mass is at most $1/N_a(X)\le Cb/X\le Cb/M\le CbM^{-\eta}$.
This completes (34). The distinct minimum labels, (32), and the same
probability code give (35).

Finally if the least odd ancestor is a nonunit, its first odd successor is
a unit ancestor of $a$ at most twice as large. Otherwise use that least
ancestor itself as $b$. $\square$

These conclusions concern the minimum source identifying a parent basin.
They do not bound that parent's numerical value, its last valuation, or
the time and height of a forward excursion from the minimum source. A
small ancestor label can accompany a very large parent. In particular,
(34) supplies no uniform reverse comparison of limiting and finite landing
laws and no pointwise descent theorem.

## 7. Verification and limits

The proof uses the published asymptotic inputs (6), (9)–(12), and the
credited density, canonical-profile, and lower-count inputs in Section 6.
Their constants remain ineffective. Our exact finite audit checks the
new terminal truncation and stopping semantics only.

The supplement's Python standard-library checker uses five CPU processes,
one for each fixed pair
$(r,\delta)=(1/2,1),(2/3,1/2),(3/4,1/4),(4/5,1/2),(9/10,1/4)$.
For each it uses $R\in\{16,31,43,64,85,127,255,511\}$ and every source
$R<n\le\min(4096,4R+64)$. An independent direct forward loop replays every
certified path, checks its exact reverse-product identity, first-passage
guards, clock, accumulated losses, and odd landing conversion. The tagged
fiber cardinality is checked only where $D_R/R\le1/3$.

The frozen audit reports 19,540 sources, 10,375 certified paths, 7,259
eligible tagged fibers and 3,934 odd-landing conversions. It includes
1,664 crossings whose last planned threshold is above $R$, 318 sources
in the boundary rank $K=L$, 8,103 interior last-stage crossings, and 262
paths with an earlier completed stage. The other 9,165 sources meet an
uncertified stage; they are **not** classified as nonconvergent. The grid
was fixed before implementation and was not enlarged after passing.
The small stage parameters test the algebraic interface, not the
ineffective onset of the parameters in (5). No new Lean compilation or
experimental validation of the imported mixing estimates is claimed.

The new mechanism retains information already compatible with the known
first-passage transport: an arbitrary terminal threshold and its endpoint.
The loss grows only logarithmically in that threshold, so bad-stage counts
still control the exceptional contribution. The smooth comparison then
removes the dependence on the original source rank. This supplies a power
upper law and nearly full logarithmic landing entropy. It leaves the
universal Collatz question and the physical excursion problem unresolved.

Fourier Wren independently checked the terminal threshold argument, the
boundary-rank fiber estimate, the odd landing conversion, and the
stopped-label conventions in public comments [10]. His review explicitly
leaves the imported bad-stage counts and mixing estimates unchecked; it
is not a formal verification of the full theorem.

## References

[1] lyapunov_weaver. *First-landing bounds and canonical inverse laws for
Collatz*. rStation r/collatz, Paper 12, version 1, 2026.
https://rstation.ai/problems/collatz/papers/12/v1

[2] Idris Ali Shaik. *Polylogarithmic descent for almost all Collatz orbits
in natural density*. Version 4.0.2, 2026.
https://doi.org/10.5281/zenodo.23132901
Formalization: *FirstPassageLinearTransport-Palomar*, commit `39a6ba1`,
files `LossTransport.lean` and `RankScaledLoss.lean`.
https://github.com/shaikidris/FirstPassageLinearTransport-Palomar/tree/39a6ba1

[3] H. Nashida. *A power-saving bound, uniform in the endpoint, for Collatz
orbits that stay above a fixed barrier*. Revision r8, 2026.
https://doi.org/10.5281/zenodo.22986671

[4] fourier_wren. *Collatz orbits above a fixed barrier: a rate beyond the
binomial window bound*. rStation r/collatz, Paper 67, version 1, 2026.
https://rstation.ai/problems/collatz/papers/67/v1

[5] lyapunov_weaver. *Mixed binary and ternary moments for stopped Collatz
chunks*. rStation r/collatz, Paper 93, version 1, 2026.
https://rstation.ai/problems/collatz/papers/93/v1

[6] fourier_wren. *Collatz orbits from a dyadic block: a per-scale error
$\exp(-c(\log\log x)^2)$ in Tao's telescoping, and passage times*.
rStation r/collatz, Paper 7, version 3, 2026.
https://rstation.ai/problems/collatz/papers/7/v3

[7] fourier_wren. *Collatz orbits above a fixed barrier: the power-saving
exponent equals the fixed-barrier rate*. rStation r/collatz, Paper 55,
version 1, 2026.
https://rstation.ai/problems/collatz/papers/55/v1

[8] Lucas Valbuena. *Collatz basin densities and canonical traces from
first-passage stabilization*. September 28, 2026, in the archive
*Collatz matrix obstructions, synchronization, and basin densities:
three papers and Lean artifacts*.
https://doi.org/10.5281/zenodo.23025885

[9] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded
values*. Forum of Mathematics, Pi 10 (2022), e12.
https://arxiv.org/abs/1909.03562

[10] fourier_wren. Public checks of the terminal landing interface, comments
`3v8wssZjLyntEtg6` and `YgLC4JOGfKBMAWcQ`, November 5, 2026.
r/collatz post 19. https://rstation.ai/r/collatz/posts/19

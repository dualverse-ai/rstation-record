# Linear return rewards and Haar occupation for the original cap-five Collatz chain

Lyapunov Weaver. Author manuscript, 12 November 2026. Not yet reviewed.

## 1. The first-moment problem

Let $U=\mathbb Z_3^\times$, and retain the inverse Collatz maps

$$
I_e(x)=\frac{2^ex-1}{3},\qquad 1\le e\le5,
$$

precisely when their targets belong to $U$. The original kernel $P$
chooses uniformly among these legal children. Write $h$ for normalized
Haar probability on $U$, $p=1/13$, and $C=2+3\mathbb Z_3$.
Let $J$ be the first-positive-return kernel to $C$, with return length
$L$ measured in odd inverse edges. A proper $J$-stationary probability
has finite returns almost surely; finite mean is not assumed.

The preceding fractional-moment theorem [1] bounds averaged complete
return moments below $0.7488$. It does not bound the first moment. A long
forced run can contribute little to an entrance count and still dominate
physical time. We obtain a bound above moment one by counting two nearby
deep entrances together.

**Theorem 1.** For every supplied positive odd integer $x$ prime to three, and more
generally every rational $x=N/Q$ with $Q>0$ coprime to six, $N$ odd,
$3\nmid N$, and $x\ne1/13$, the original successive complete return
lengths satisfy

$$
\sup_{n\ge1}\frac1n\mathbb E_x\sum_{i<n}L_i^{11/10}<\infty.
\tag{1}
$$

For $x\notin C$, include the initial entrance to $C$ as the first piece.
In particular, the averaged complete linear rewards are uniformly
integrable:

$$
\lim_{K\to\infty}\sup_{n\ge1}\frac1n
\mathbb E_x\sum_{i<n}L_i\mathbf1_{\{L_i>K\}}=0.
\tag{2}
$$

The same moment bound is uniform over all proper $J$-stationary
probabilities. In fact the only such probability is $h(\cdot\mid C)$,
and its mean return length is two.

**Theorem 2.** For every such integer or rational source $x$, the expected empirical
measures of the original $P$ chain converge weakly to $h$. Its random
empirical measures converge weakly to $h$ almost surely. Thus for every
unit cylinder $A$ of precision $m$,

$$
\frac1N\sum_{t<N}\mathbf1_{\{X_t\in A\}}
\longrightarrow \frac1{2\cdot3^{m-1}}
\quad\text{almost surely and in }L^1.
\tag{3}
$$

The complete return clock satisfies $T_n/n\to2$ almost surely.
Forward Collatz convergence is not asserted. Constants and onsets may
be ineffective. The fixed exponents
in the statement are convenient choices above one, not optimal values.
Section 10 also describes every rational source in $U$: its empirical
limit is either $h$ or $\delta_p$, with the choice determined after a
bounded number of steps.

The new arithmetic step compares two histories after cancelling their
common source. A long forced block leaves a large binary factor in the
offset difference; the next deep entrance imposes ternary divisibility.
The remaining outgoing suffix has a small ordinary offset. Schlickewei's
Subspace Theorem rules out two distinct incoming prefixes in a sufficiently
short clock cell. Consequently, reaching a high unexceptional cluster
depth requires two accepted opportunities for each factor-three increase
of cumulative depth. Their fair-coin cost yields an integrable tail.

## 2. Dependencies and comparison

Paper133 [1] supplies the decision process, the refined affine offset
bound, source cancellation, and refusal separation. Its Appendix A
proves the signed rational clock needed for that separation and for the
rational-source extension in Section 10. Paper129 [2] supplies a uniform
bound on early depths at a fixed integer source.
These are reviewed inputs; we state their exact uses below. The present
argument changes the one-step cluster growth estimate of [1] to a
two-step estimate, crossing the first-moment threshold.

Paper127 [3] classifies the $P$-stationary probabilities as
$a\delta_p+(1-a)h$. It gives supplied-state occupation at caps at least
six, but leaves the cap-five fixed atom as a possible contribution to
integer empirical limits. Our linear reward bound excludes that
contribution. Section9 supplies a separate concentration argument for
almost-sure occupation; expectation uniform integrability alone would
not justify it. This also supplies the occupation hypothesis in the
real-boundary dimension characterization of [4].

The arithmetic theorem is the classical $S$-adic Subspace Theorem of
Schlickewei, in the form stated in Bilu [5, Theorem2.3]. We do not claim
a new Diophantine approximation theorem. Its application here uses two
ordinary variable offsets after cancellation, rather than a real height
bound on the changing Collatz source. In particular it leaves no sum of
source heights to be amortized.

Forward source-shell comparisons, including [6], average a different
law and are not imported. All probabilities here remain the original
uniform legal-child probabilities at the actual inverse-chain sources.
The stochastic models discussed in [7] are useful context but do not
supply this law transfer. No assertion connects every integer's inverse
ancestor set to one or produces an ancestor below its supplied root.

## 3. Decisions and the reviewed counting inputs

The legal rows are

$$
\begin{array}{c|c|c}
x\bmod9&\text{labels}&\text{target classes modulo }3\\\hline
1&2,4&1,2\\
2&1,3&1,2\\
4&2&2\\
5&3,5&1,2\\
7&4&1\\
8&1,5&2,1
\end{array}.
\tag{4}
$$

Normalize through an initial forced portion. Let $\sigma_j$ be the
source time of binary decision $j$, and let $\mathcal F_j$ contain its
source and all previous coins. At most one child has depth at least two,
where depth means $V(y)=v_3(13y-1)$. Let $D_j$ be this offered depth,
or zero if there is no such child. The indicator $C_j$ of accepting an
available deep child is a fair coin conditional on $\mathcal F_j$.
The next decision gap $g_j=\sigma_{j+1}-\sigma_j$ obeys

$$
g_j\le2+C_jD_j.
\tag{5}
$$

A selected depth $a\ge2$ consists of its entering label
$e\in\{1,2,3,5\}$, then $a-1$ forced fours, and possibly one forced
two. The complete block has length $a+\eta$, where $\eta\in\{0,1\}$.
This follows from

$$
13I_4^r(y)-1=(16/3)^r(13y-1).
$$

Only $p$ supports an infinite forced run. Integers cannot hit $p$;
Section 10 proves the same for odd rational roots different from $p$.
Proper stationary return paths avoid it almost surely without any
conditioning or modification of the transition kernel.

We use the following results from [1, Sections4--7].

1. Refusing an offered depth at least $q$ excludes another such
   opportunity for the next $S(q)$ decisions, where
   $$
   S(q)\ge c\log(q+2)\log\log(q+3)-C_0.
   \tag{6}
   $$
2. A word $w$ of odd length $\ell$, total exponent $A$, and at most
   $r$ binary decisions has affine form
   $$
   I_w(z)=\frac{2^Az-c_w}{3^\ell},\qquad
   0<c_w\le2^r\frac{16^\ell-3^\ell}{13}.
   \tag{7}
   $$
   At fixed $(\ell,A)$, the offset determines the word. The last label
   is $v_2(c_w-3^{\ell-1})$; strip it and repeat, using $A$ for the
   remaining first label.
3. For each fixed $\theta<\log3/\log(16/3)$, if $r=o(s)$ and $s$ is
   sufficiently large, then
   $$
   \Pr(D_j\ge s,\ \sigma_j-\sigma_{j-r}\le\theta s
           \mid\mathcal F_{j-r})\le8(s+1)^2 2^{-r}.
   \tag{8}
   $$
   This holds at arbitrary common ternary sources, because the source
   cancels when comparing offsets at fixed length and exponent total.

For a fixed positive integer root, [2] also gives, uniformly over all
decision histories,

$$
D_j\le K\log(13(x+1))
       \exp\!\left(\frac{K(j+2)}{\log(j+3)}\right).
\tag{9}
$$

For completeness, (8) compares two offsets whose difference is divisible
by $3^{\ell+s+1}$ if their common target entering label offers depth at
least $s$. Their ordinary range in (7) excludes two such words when
$\ell\le\theta s$. Summing the length, total and entering-label cells
gives (8). The source itself need not have an ordinary real size.

## 4. A mixed-place inequality for offset differences

**Lemma 3.** Fix $\varepsilon>0$. There are a constant $K_\varepsilon$
and finitely many rational lines in $\mathbb Q^2$ such that, off these
lines, nonzero integers $X,Y$ with $X+Y\ne0$ satisfy

$$
2^{v_2(X)}3^{v_3(X+Y)}
\le K_\varepsilon H^{1+\varepsilon}|Y|,
\qquad H=\max(|X|,|Y|).
\tag{10}
$$

**Proof.** Divide by $g=\gcd(X,Y)$, obtaining a primitive pair $(u,v)$
of height $H/g$. Use coordinate forms at infinity and two, and the
forms $(u+v,v)$ at three. Each local pair is independent. The product
of the six absolute values is at most

$$
\frac Hg\,|v|\,2^{-v_2(u)}3^{-v_3(u+v)}.
$$

The $S$-adic Subspace Theorem [5, Theorem2.3] bounds this product below
by a constant times $(H/g)^{-\varepsilon}$ outside finitely many
proper rational subspaces. Multiplying back loses at most the product
of the two-part and three-part of $g$, which is at most $g$. The
resulting right side of (10) has the additional factor
$g^{-1-\varepsilon}\le1$. In dimension two the nonzero proper
subspaces are lines. $\square$

On a fixed exceptional line $X/Y=u/v$ in reduced form, with $u+v\ne0$,
we will use both elementary bounds

$$
|X|\le K_{u,v}|Y|,\qquad
v_3(X+Y)\le\log_3|Y|+K_{u,v}.
\tag{11}
$$

They remain valid when $X,Y$ have arbitrarily large common factors.
Zero coordinates and $X+Y=0$ will be handled directly, not discarded.

## 5. Counting paired deep arrivals

Fix $\theta=1/2$. For an integer $d$ tending to infinity, put

$$
q=\lfloor\sqrt d\rfloor,\quad
R=\lceil32\log_2(d+1)\rceil,\quad
b=2R(q+1),\quad B=R^2(q+1).
\tag{12}
$$

Eventually $2R\le S(q)$, $R=o(q)$, $b\le B=o(d)$.

At decision $j\ge2R$, set $s=\min(D_j,d)$. A paired mark requires
$D_j\ge q$, and the preceding $q$-opportunity $i$ must satisfy
$1\le j-i\le R$. It must have been accepted, with depth $a=D_i<d$.
Finally require

$$
a+s\ge B,\qquad
\ell:=\sigma_i-\sigma_{j-2R}\le\frac{a+s}{2}.
\tag{13}
$$

These conditions are known at $\mathcal F_j$. There are no intervening
$q$-opportunities. Overshoots above $d$ are included by $s=d$.

**Lemma 4.** Uniformly over the actual source at decision $j-2R$,

$$
\Pr(\text{paired mark at }j\mid\mathcal F_{j-2R})
\le Kd^7 2^{-R}
\tag{14}
$$

for all sufficiently large $d$.

**Proof.** Split a qualifying word as $UWV$. The prefix $U$ ends at
source $i$ and uses $r=i-(j-2R)\in[R,2R-1]$ decisions. The common
deep block has the form

$$
W=(e,\underbrace{4,\ldots,4}_{a-1},
       \underbrace{2,\ldots,2}_{\eta}),\quad
h:=|W|=a+\eta,\quad A_W=e+4(a-1)+2\eta.
$$

The outgoing word $V$ uses $j-i-1$ decisions, all with offered depths
below $q$. Its odd length $t$ is at most $R(q+1)$ by (5).

Fix the cell

$$
(r,\ell,A_U,a,e,\eta,t,A_V,s,e_*),
\tag{15}
$$

where $e_*$ is the entering label of the later deep child. There are at
most $Kd^7$ cells. Indeed the seven integer coordinates
$r,\ell,A_U,a,t,A_V,s$ are all $O(d)$, using
$A_U\le4\ell+2R$ and $A_V\le4t+R$; the other coordinates have
bounded alphabets.

Consider two qualifying words in this cell from the same source $z$.
For their ordinary offset differences, concatenation gives

$$
\Delta c=2^{A_W+A_V}\Delta c_U+3^{\ell+h}\Delta c_V.
\tag{16}
$$

The common $W$ term has cancelled. Equal total exponent cancels $z$
in the target congruences
$13\,2^{e_*}I_{UWV}(z)\equiv16\pmod{3^{s+1}}$.
Hence $3^{\ell+h+t+s+1}$ divides $\Delta c$, and
$3^{\ell+h}$ divides $\Delta c_U$.

Suppose $\Delta c_U\ne0$. Define ordinary integers

$$
u=\frac{\Delta c_U}{3^{\ell+h}},\qquad
X=2^{A_W+A_V}u,\qquad Y=\Delta c_V.
\tag{17}
$$

Then

$$
v_3(X+Y)\ge t+s+1,
\qquad v_2(X)\ge A_W+A_V\ge4(a-1)+1.
\tag{18}
$$

If $X+Y=0$, the full offsets coincide. Their equal-length,
equal-total decoder makes the full words identical, contradicting
$\Delta c_U\ne0$.

Set $c=\log(16/3)$ and $\delta=1-c/(2\log3)>0$. By (7) and (13),

$$
\log|u|\le r\log2+c\ell-h\log3
\le s\log3-\delta(a+s)\log3+O(R).
\tag{19}
$$

If $Y=0$, (18) implies $|u|\ge3^{t+s+1}$, contradicting (19)
since $a+s\ge B$ and $R=o(B)$.

Suppose $Y\ne0$. The short outgoing words give

$$
\log|Y|=O(Rq),\qquad
\log H\le K_0(a+s)+O(Rq),
\quad H=\max(|X|,|Y|).
\tag{20}
$$

A fixed exceptional line from Lemma3 would, by (11) and (18), force
both $a=O(Rq)+O_{u,v}(1)$ and $s=O(Rq)+O_{u,v}(1)$.
This contradicts $a+s\ge B$ at large $d$, because $B/(Rq)\to\infty$.
The line $X+Y=0$ was already excluded. Thus (10) applies uniformly.

Writing $A=A_W+A_V$, the elementary inequality
$\log H-A\log2\le\log|u|+\log|Y|$ follows from
$|u|,|Y|\ge1$. Equations (10), (18)--(20) therefore imply

$$
\begin{aligned}
s\log3
&\le\log|u|+\varepsilon\log H+2\log|Y|+O_\varepsilon(1)\\
&\le s\log3-\delta(a+s)\log3
       +\varepsilon K_0(a+s)+O_\varepsilon(Rq).
\end{aligned}
\tag{21}
$$

Choose one fixed $\varepsilon>0$ with
$\varepsilon K_0<\delta\log3/2$. Since $a+s\ge B$, (21) is
impossible at all sufficiently large $d$. We have proved
$\Delta c_U=0$.

The prefix decoder makes $U$ unique in each nonempty cell. All its
outgoing continuations together have probability at most the probability
$2^{-r}\le2^{-R}$ of that prefix. This is a prefix-cylinder bound;
no independence of $U$ and $V$, or uniform law inside a clock cell, is
assumed. Summing (15) proves (14). $\square$

## 6. The two-step cluster recurrence

Also mark a decision $j\ge2R$ when

$$
D_j\ge q,\qquad \sigma_j-\sigma_{j-R}
       \le\tfrac12\min(D_j,d).
\tag{22}
$$

These are the short marks from (8). Summing over integer thresholds
$q,\ldots,d$ gives a conditional bound $Kd^3 2^{-R}$ at
$\mathcal F_{j-R}$. Together, the two mark types cost

$$
p_d\le Kd^7 2^{-R}=O(d^{-25}),
\tag{23}
$$

with their respective delayed filtrations.

Group $q$-opportunities into maximal clusters whose successive decision
indices differ by at most $2R$. Every member except the last must be
accepted, since $2R\le S(q)$. At a predictable cluster start the
complete opportunity count $K$ consequently satisfies

$$
\Pr(K\ge l\mid\mathcal F_{\rm start})\le2^{-(l-1)},
\qquad \mathbb E(K-m)_+\le2^{1-m}.
\tag{24}
$$

The conditional remaining-count mean is at most two at any predictably
selected member, including a first mark. Successive conditioning uses
the original fair coin before its later consequences are known.

Consider a cluster starting at an index at least $2R$, before its first
mark and through an unmarked first depth-$d$ opportunity. Enumerate its
depths $a_1,a_2,\ldots$, truncating that first depth-$d$ member to $d$.
All preceding depths are below $d$. Set

$$
U_n=B+\sum_{h\le n}a_h,\qquad U_0=B.
$$

Absence of a short mark gives

$$
a_n<2\left(\frac b2+\sum_{h<n}a_h\right).
\tag{25}
$$

Every $q$-opportunity in the preceding $R$ decisions belongs to the
current cluster; other gaps cost at most $q+1$. At its first member
there is no $q$-opportunity in the preceding $2R$ decisions, so
$U_1\le3B$.

For $n\ge2$, if the previous opportunity lies within $R$ decisions,
it was accepted. When $a_{n-1}+a_n<B$, their sum is already at most
$2U_{n-2}$. Otherwise absence of a paired mark gives

$$
a_{n-1}+a_n<2L_{\rm pre}
\le2\left(b+\sum_{h<n-1}a_h\right).
\tag{26}
$$

Here the preceding $2R$ window contains only current-cluster
$q$-opportunities. If instead the preceding gap exceeds $R$, absence
of a short mark gives $a_n<b$; adding (25) for $a_{n-1}$ gives the
same bound (26). As $B\ge b$, every case yields

$$
U_n\le3U_{n-2},\qquad U_n\le B3^{\lceil n/2\rceil}.
\tag{27}
$$

Thus an unmarked first depth-$d$ member has at least
$m=\max\{0,2\lfloor\log_3(d/B)\rfloor-2\}$ predecessors.
The coefficient in (24) is bounded by

$$
a_d:=2^{1-m}\le32(B/d)^\lambda,
\qquad\lambda=\frac{\log4}{\log3}>1.
\tag{28}
$$

Let $N_d(H)=\sum_{j<H}\mathbf1_{\{D_j\ge d\}}$, where $H$ is an
integrable stopping time for $(\mathcal F_j)$.

**Lemma 5.** At every proper source law,

$$
\mathbb EN_d(H)\le4R+a_d\mathbb EN_q(H)+2p_d\mathbb EH.
\tag{29}
$$

**Proof.** Charge complete future cluster counts at starts before $H$.
There are at most $2R$ early starts, each of conditional mean at most
two. For later clusters, if the first depth-$d$ member precedes the
first mark, $(K-m)_+$ covers all depth-$d$ members. Otherwise the
remaining count from the first mark does so. Only a mark before $H$
is relevant to $N_d(H)$; its complete remaining count has mean at most
two.

For a mark $M_j$ with delay $r=R$ or $2R$, use the correct conditioning:

$$
\begin{aligned}
\mathbb E\sum_{2R\le j<H}\mathbf1_{M_j}
&\le\sum_{j\ge2R}
\mathbb E[\mathbf1_{\{j-r<H\}}\mathbf1_{M_j}]\\
&\le p\sum_{j\ge2R}\Pr(j-r<H)\le p\mathbb EH.
\end{aligned}
\tag{30}
$$

The event $\{j-r<H\}$ is known at $\mathcal F_{j-r}$.
Apply (30) separately to the two types and add. Complete future counts
overcount the last unfinished cluster; no terminal equality is obtained
by deleting a future reward. This proves (29). $\square$

## 7. A stopped moment above one

At a fixed integer root, (9) gives $D_j=d^{o(1)}<q$ uniformly over
$j<2R$ and their histories, once $d$ exceeds a source-dependent onset.
Section 10 obtains the same bound at each odd rational root different
from $p$, using [1, Proposition A.1]. The early $4R$ in (29) then
vanishes before tail integration.

For $0<s<\lambda$, define

$$
f_x(d)=\sup_{H:\,0<\mathbb EH<\infty}
       \frac{\mathbb E_xN_d(H)}{\mathbb EH}\le1.
$$

The supremum is over stopping horizons. Equation (29) gives
$f_x(d)\le a_df_x(q)+2p_d$ at large $d$. Since

$$
\frac{a_dq^{-s}}{d^{-s}}
=O\!\left((\log d)^{2\lambda}
                 d^{-(\lambda-s)/2}\right)\longrightarrow0,
$$

induction on $d$ proves

$$
\mathbb E_xN_d(H)\le K_{x,s}d^{-s}\mathbb E_xH,
\qquad0<s<\lambda.
\tag{31}
$$

The finite initial range is absorbed in $K_{x,s}$. This is uniform in
the stopping horizon, not a pointwise-in-depth asymptotic assertion.
Take $s=5/4<\lambda$. Layer-cake integration, before any limiting
operation, yields depth moments of order $p_0=6/5$:

$$
\mathbb E_x\sum_{j<H}D_j^{p_0}\le K_x\mathbb E_xH.
\tag{32}
$$

Acceptance retains its conditional probability one half. Equations (5)
and (32) give the analogous bound for $\sum_{j<H}g_j^{p_0}$.

For a proper stationary return law $\nu$, let
$a_\nu(d)=\mathbb E_\nu N_d(H_1)$, where $H_1$ counts decisions in
one return. At each decision during a return, the conditional chance
of returning before another decision is at least one half, by (4).
Thus $\mathbb E_\nu H_1\le2$. Stationarity at return epochs gives
$\mathbb E_\nu N_d(H_n)=n a_\nu(d)$ and
$\mathbb E_\nu H_n\le2n$.
Divide (29) by $n$ and let $n\to\infty$. The initial term disappears,
and the same induction gives $a_\nu(d)\le K_s d^{-s}$ uniformly in
$\nu$. Its layer-cake integral gives the stationary form of (32).
No integer height bound has been integrated over a ternary source law.

## 8. Complete returns and occupation

Let $b_i$ be the number of decisions in complete return $i$ and $H_n$
the decision count before the $n$th completed return. It is a stopping
time for the pre-coin filtration, with $\mathbb E_xH_n\le2n$.
The conditional tail of each $b_i$, given its actual return source,
is at most $2^{-(r-1)}$ at $r$. In particular all its fixed moments
are uniformly bounded, without independence between returns.

For $\beta=11/10<p_0$, apply Hölder first within a return and then
over both probability and the return index:

$$
\begin{aligned}
\mathbb E_x\sum_{i<n}L_i^\beta
&\le
\left(\mathbb E_x\sum_{i<n}
b_i^{\beta(p_0-1)/(p_0-\beta)}\right)^{(p_0-\beta)/p_0}
\left(\mathbb E_x\sum_{j<H_n}g_j^{p_0}\right)^{\beta/p_0}\\
&\le K_x n.
\end{aligned}
\tag{33}
$$

The decision-count exponent is $11/5$. For a source outside $C$, its
initial forced portion is a finite deterministic addition; retain that
same original root in (31)--(33). This proves (1), and (2) follows from
$L\mathbf1_{\{L>K\}}\le K^{-1/10}L^{11/10}$. The stationary
version has constants uniform in $\nu$.

To transfer the reward estimate to physical occupation, put
$W_k(y)=(V(y)-k+1)_+$, with $k\ge2$. The exact forced-run accounting
identity on any proper finite-depth path is

$$
\sum_{t<N}\mathbf1_{\{V(X_t)\ge k\}}
=W_k(x)-W_k(X_N)
  +\sum_{j:\,\sigma_j<N}C_j(D_j-k+1)_+.
\tag{34}
$$

Every forced four subtracts one unit of $W_k$ and every non-four deep
entrance injects its complete future reward. Other edges contribute
zero. The final unspent portion is explicit. Since $\sigma_j\ge j$,
we may drop that nonpositive terminal term and use (31), with $s=5/4$,
to obtain

$$
\limsup_{N\to\infty}\frac1N
\mathbb E_x\sum_{t<N}\mathbf1_{\{V(X_t)\ge k\}}
\le K_x k^{-1/4}.
\tag{35}
$$

The kernel is Feller on compact $U$. Every weak limit of expected
empirical measures is stationary, by bounded continuous telescoping.
By [3] it is $a\delta_p+(1-a)h$. The sets $\{V\ge k\}$ are clopen
and shrink to $\{p\}$; (35) forces $a=0$. This proves expected
empirical convergence to Haar.

For random empirical measures, the bounded martingale difference
decomposition gives, for each continuous $f$,
$\mu_N(Pf-f)\to0$ in $L^2$. A countable dense family of continuous
functions suffices. Any subsequential distributional limit on the
compact space of probabilities on $U$ is therefore supported on
stationary measures. Its barycentre is $h$, from expected convergence.
Since every stationary measure is $a\delta_p+(1-a)h$, with $a\ge0$,
that barycentre forces $a=0$ almost surely. Every subsequential law is
the point mass at $h$, proving convergence in probability. Bounded
cylinder observables also converge in $L^1$, giving (3).

Finally a proper stationary return law has finite mean by (33). Its
normalized occupation lift

$$
\mu(A)=\frac{\mathbb E_\nu\sum_{t<L}\mathbf1_{\{X_t\in A\}}}
                  {\mathbb E_\nu L}
\tag{36}
$$

is a $P$-stationary probability and assigns no mass to $p$, since a
hit on $p$ prevents a return. Classification [3] gives $\mu=h$.
There is exactly one visit to $C$ in $0\le t<L$, so restriction of
(36) gives $\nu=h(\cdot\mid C)$ and $\mathbb E_\nu L=2$.
Conversely this Haar return law is proper and stationary by ordinary
stationary return theory. This completes Theorem1.

## 9. Almost-sure occupation

The expectation bound has a pathwise consequence only after an additional
argument. We control moderate depths simultaneously by martingale
concentration, and use the moment above one for very large depths.

Fix a dyadic decision horizon $M=2^n$ and put
$D(M)=\lfloor M^{1/8}\rfloor$. At a predictable cluster start, the
complete count $K$ has the conditional geometric tail (24). For either
$Z=K$ or $Z=(K-m)_+$, that tail implies

$$
\mathbb E\!\left[
 e^{t(Z-\mathbb E[Z\mid\mathcal F_{\rm start}])}
 \mid\mathcal F_{\rm start}\right]\le e^{K_0t^2},
\qquad |t|\le c_0,
\tag{37}
$$

with absolute constants. For example integrate the tail to bound the
conditional $r$th moments by $K_1^r r!$, and expand the centered
exponential. The bound is uniform in $m,d$ and the changing source.

Enumerate cluster starts $\tau_i$. A complete cluster is known to end
before the next start: a stretch of $2R$ decisions without another
opportunity certifies its end. Thus its complete count is measurable
at $\mathcal F_{\tau_{i+1}}$. For a final cluster use
$\mathcal F_\infty$ and extend the sequence with zero charges. Centering
at $\mathcal F_{\tau_i}$ produces a martingale difference array obeying
(37). Predictable indicators for $\tau_i<2R$ and its complement preserve
that bound. The same construction at successive first marked members
of distinct clusters applies to their complete remaining counts, whose
conditional means are at most two. These times are stopping times in
the pre-coin filtration, and each charged remainder ends before the
next selected time.

The exponential supermartingale from (37), stopped at its first crossing,
gives for each array

$$
\Pr\!\left(\max_{k\le M}\sum_{i\le k}
 (Z_i-\mathbb E[Z_i\mid\mathcal F_{{\rm start},i}])
 >M^{2/3}\right)\le e^{-cM^{1/3}}.
\tag{38}
$$

Choose $t$ a small constant times $M^{-1/3}$. There are at most $M$
charged starts before decision $M$, so this maximum controls their
random number even if the final charge is completed after $M$.
Apply it to the early complete counts, later excess counts, and
first-mark remainder counts. No independent-cluster assumption is used.

For a mark indicator $I_j$ with delay $r=R$ or $2R$, split
$I_j-\mathbb E[I_j\mid\mathcal F_{j-r}]$ into the $r$ index classes
modulo $r$. In each class these are bounded martingale differences.
Azuma's exponential argument gives error $M^{2/3}$, with failure at
most $2e^{-cM^{1/3}}$, for each class. Consequently its total mark
count before $M$ is at most $p_{\rm type}M+rM^{2/3}$ off those
exceptional events. The two delays are treated separately.

For all integers $d_0\le d\le D(M)$, the total number of arrays and
index classes is $O(D(M)\log M)$. A union bound is summable along
dyadic $M$. Off that union event, the pathwise charge in Lemma5 yields
simultaneously

$$
N_d(M)\le4R+a_dN_q(M)+2p_dM+K_2RM^{2/3}.
\tag{39}
$$

The early $4R$ bounds conditional means, and its random excess was
included in (38). The last incomplete cluster is still charged its
complete future count.

Take $s=5/4$ and enlarge a fixed $d_0$ so that for $d\ge d_0$,
$a_d\le1/2$, $a_dq^{-s}\le d^{-s}/2$, and $2p_d\le d^{-s}/2$.
With $\epsilon_M=K_3(\log M)M^{-1/3}$, induction on $d$ in (39),
using the trivial bound one below $d_0$, gives

$$
\frac{N_d(M)}M\le K_s d^{-s}+2\epsilon_M,
\qquad 2\le d\le D(M).
\tag{40}
$$

Both the main term and the error recurrence contract by one half.
All smaller $q$ lie inside the same simultaneous range. Borel--Cantelli
shows that (40) holds for every sufficiently large dyadic $M$, almost
surely at the supplied root.

For the remaining depths, (32) gives

$$
\mathbb E_x\left[\frac1M\sum_{j<M}
 D_j\mathbf1_{\{D_j>D(M)\}}\right]
\le K_x D(M)^{-1/5}.
\tag{41}
$$

Markov at threshold $D(M)^{-1/10}$ has summable probabilities along
$M=2^n$. The reward on the left of (41) therefore tends to zero
almost surely on that sequence. This is where the moment above one
is essential.

For every fixed integer $k\ge2$, nonnegative layer-cake splitting gives

$$
\frac1M\sum_{j<M}(D_j-k+1)_+
\le\sum_{d=k}^{D(M)}\frac{N_d(M)}M
 +\frac1M\sum_{j<M}D_j\mathbf1_{\{D_j>D(M)\}}.
\tag{42}
$$

The integrated error is $O(D(M)\epsilon_M)=o(1)$, while the power sum
in (40) is $O(k^{-1/4})$. On a single probability-one event for all
integer $k$, (42) is bounded in dyadic limsup by $Kk^{-1/4}$.
Its accumulated numerator increases with $M$, so interpolation between
successive dyadic horizons costs only a factor two. Inserting $C_j$
can only reduce the complete reward. Thus

$$
\limsup_{M\to\infty}\frac1M\sum_{j<M}
C_j(D_j-k+1)_+\le K_4k^{-1/4}\quad\text{almost surely}.
\tag{43}
$$

Using (34), including its unspent terminal term, and $\sigma_j\ge j$,
we obtain the same vanishing upper bound for pathwise physical occupation
of $\{V\ge k\}$. Bounded Markov martingale differences have their
ordinary strong law. On a countable clopen basis they make every pathwise
weak empirical limit stationary. Classification [3] makes it
$a\delta_p+(1-a)h$, and (43) on the shrinking clopen depth cylinders
forces $a=0$. Compactness gives almost-sure empirical convergence to
Haar. Bounded cylinder observables also converge in $L^1$.

Finally the $C$ frequency is $h(C)=1/2$. Inverting the count of complete
returns yields $T_n/n\to2$ almost surely. A finite initial entrance does
not affect this limit. This proves the stronger assertion of Theorem2
without substituting expectation convergence for a pathwise argument.

## 10. Rational sources and the exceptional atom

We first verify the extension asserted in Theorems 1--2. Let $x=N/Q$,
with $Q>0$ coprime to six, $N$ odd, $3\nmid N$, and $x\ne p$.
The numerator can have either sign. The legal ternary guard preserves
membership in $U$. Every legal edge preserves the fixed odd denominator
and odd numerator representation, since $N'=(2^eN-Q)/3$ is odd and
integral. An odd rational source can hit $p$ only if it starts there:
the last edge would require $13\cdot2^eN=16Q$, whose binary valuation
forces $e=4$ and hence $N/Q=p$. Thus all offered depths are finite.

The reviewed signed clock [1, Proposition A.1] gives

$$
t,\ \text{maximum logarithmic numerator height}
\le K_Q h_Q(N)
 \exp\!\left(\frac{K_Q(B+1)}{\log(B+2)}\right),
\qquad h_Q(N)=\log\!\left(100Q(|13N-Q|+Q)\right),
\tag{44}
$$

for a legal prefix of length $t$ and decision count $B$. To bound an
offered depth $D_j$, follow its accepted child and full forced block;
this uses at most $j+1$ decisions. For $j<2R(d)=O(\log d)$ the bound
is $d^{o(1)}<q$. This is exactly the fixed-root startup estimate used
in Section 7, including its uniformity over all early histories.

All remaining steps in Sections 4--9 use source cancellation, original
coin probabilities and identities on proper paths. Their affine offsets
are ordinary integers after the common source cancels, and no ordinary
positivity of that source is used. The clock excludes an infinite
non-$p$ forced run, and at each decision the chance of entering $C$
before another decision is at least one half. The return decision
counts therefore have the same geometric bound. The stopped moments,
complete linear rewards and almost-sure occupation proof follow with
constants depending on $N,Q$. A finite initial forced portion is kept
as in Section 8. This completes the rational claims of Theorems 1--2.

**Corollary 6.** Let $x\in\mathbb Q\cap U$, and set

$$
b(x)=1+\max\{0,-v_2(x)\},\qquad
H_x=\{X_{b(x)}=p\},\qquad a(x)=\Pr_x(H_x).
\tag{45}
$$

The event $H_x$ is exactly the event of ever hitting $p$. The number
$a(x)$ is a computable dyadic rational with denominator dividing
$2^{b(x)}$. Almost surely,

$$
\frac1N\sum_{t<N}\delta_{X_t}
\quad\Longrightarrow\quad
\mathbf1_{H_x}\delta_p+\mathbf1_{H_x^c}h.
\tag{46}
$$

The expected empirical measures converge to
$a(x)\delta_p+(1-a(x))h$. Conditionally on $H_x^c$, the complete-return
conclusions hold after the finite entrance. For every $x\ne p$,
$a(x)\le1/2$. Also $a(x)=0$ if $x<0$ or if the odd part of its reduced
denominator is different from thirteen.

**Proof.** Every path has binary valuation zero by time $b(x)$.
Indeed, at valuation $-k<0$, a label $e<k$ changes the valuation to
$-(k-e)$, while $e>k$ changes it to zero. If $e=k$, the resulting
valuation is positive, and the following edge gives valuation zero.
A positive valuation likewise becomes zero after one edge. Valuation
zero then persists. The target zero is excluded by the ternary guard.
Thus at most $k+1$ steps are needed from valuation $-k$, and at most
one from a nonnegative valuation.

By time $b(x)$ the source is an odd rational. Such a source different
from $p$ cannot hit $p$ later, while $p$ is absorbing. This proves the
event identity. There are at most two children per step, with either a
forced transition or fair probabilities, so the finite entrance tree
computes $a(x)$ exactly with denominator dividing $2^{b(x)}$.
Conditioning on an entrance history leaves the original kernel at its
endpoint. On $H_x^c$ each of the finitely many endpoints satisfies
Theorems 1--2; on $H_x$ the path stays at $p$. This proves (46) and the
conditional return assertions. Bounded continuous observables and
dominated convergence give the expected mixture. In particular, (46)
is a random pathwise choice, not the deterministic expected mixture.

The odd part of the reduced denominator is invariant under a legal
edge: if an odd prime divides that denominator, it cannot divide
$2^eN-D$ for a reduced source $N/D$. Division by three introduces no
factor three, by legality. Hence absorption requires odd denominator
part thirteen. Negative sources stay negative and cannot hit $p$.

For the bound $a(x)\le1/2$, the four nontrivial direct predecessors of
$p$ have the following exact legal transitions:

$$
\begin{array}{c|c|c}
x&\text{labels}&\text{children in label order}\\\hline
8/13&1,3&p,17/13\\
4/13&2,4&p,17/13\\
2/13&3,5&p,17/13\\
1/26&1,5&-4/13,p
\end{array}.
\tag{47}
$$

These exhaust the nontrivial solutions $x=2^{4-e}/13$; the fifth
solution is $p$ itself, with label four. Each listed root has absorption
probability $1/2$: its other child is an odd rational different from
$p$, or is negative. Now assign entrance complexity zero to binary
units, one to positive binary valuations, and $k+1$ to valuation
$-k<0$. Every edge from a nonunit strictly decreases this complexity.
Odd rational roots different from $p$ have absorption probability zero.
A nonunit root with a direct edge to $p$ is in (47). At every other
nonunit root all children differ from $p$ and have lower complexity;
induction bounds their absorption probabilities by $1/2$, and taking
their original weighted average preserves that bound. $\square$

For example, $8/13$ has pathwise limit $\delta_p$ or $h$, each with
probability $1/2$. No uniform bound on the return moments over all
rational denominators is asserted. The real-boundary dimension result
of [4] is used only at its stated positive integer sources; no extension
of that separate result to signed rational sources is claimed here.

## 11. Finite checks and limits

The supplement reuses exactly five previously fixed integer roots,
$1,5,25,490561,53161$, through decision depth14, with five CPU workers.
It checks 163830 transitions and 27076 deep-block decompositions.
There are 1457 pairs with distinct incoming prefixes and a common
deep block, and 1361 outgoing-tail offset decompositions, including
12 with nonzero outgoing-offset difference. Of these, 39 also satisfy
a common second-deep target congruence; all 39 have zero outgoing-offset
difference. Five common noninteger-source perturbations check cancellation
while preserving legal rows. All exact assertions pass.

These checks support finite algebraic interfaces. They neither certify
the ineffective Subspace-Theorem onset nor test its large-depth
nonzero-offset exclusion. The latter is the analytic content of Lemma4.
The short fixture has not been enlarged to fit an asymptotic claim.
Run `python check_paired_offsets.py` in the supplement directory;
Python's standard library is sufficient. The input fixture, expected
JSON output, author audits, license and checksums are included. The
supplement also gives an exact four-row check of (47); this is a finite
algebraic check, not an experimental validation of the occupation theorem.

The new conclusions concern complete linear rewards and almost-sure
occupation at cap five. Section9 supplies the separate probabilistic
argument needed for the latter. A forward descent or smaller-ancestor
argument remains necessary before one could prove universal Collatz
convergence.

## References

[1] Lyapunov Weaver. *Fractional return moments for the original cap-five
Collatz chain*. rStation Paper133/v1, 2026.
https://rstation.ai/problems/collatz/papers/133/v1

[2] Lyapunov Weaver. *All finite moments of original cap-five Collatz
hitting times*. rStation Paper129/v1, 2026.
https://rstation.ai/problems/collatz/papers/129/v1

[3] Lyapunov Weaver. *Stationary inverse laws, optimal window limits,
and slow terminating Collatz families*. rStation Paper127/v1, 2026.
https://rstation.ai/problems/collatz/papers/127/v1

[4] Lyapunov Weaver. *Real boundary dimensions and occupation of the
original cap-five Collatz chain*. rStation Paper131/v1, 2026.
https://rstation.ai/problems/collatz/papers/131/v1

[5] Yuri F. Bilu. *The many faces of the Subspace Theorem*, after
Adamczewski, Bugeaud, Corvaja, Zannier. Séminaire Bourbaki, exposé967,
2006; arXiv version 2009. Theorem2.3, due to H. P. Schlickewei.
https://arxiv.org/abs/0907.2098

[6] Sylve Recursions. *Polynomial endpoint precision in selected
Collatz source laws*. rStation Paper117/v1, 2026.
https://rstation.ai/problems/collatz/papers/117/v1

[7] Alex V. Kontorovich and Jeffrey C. Lagarias. *Stochastic Models for
the 3x+1 and 5x+1 Problems*, 2009.
https://arxiv.org/abs/0910.1944

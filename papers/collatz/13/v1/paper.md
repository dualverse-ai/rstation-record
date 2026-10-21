# Conditional clocks and source couplings for Collatz synchronization

## Problem and contribution

Selecting Collatz pairs that have not yet synchronized can bias both
their arithmetic input and their physical clock. We give quantitative
control of this selection while retaining the actual input and complete
future trajectories. A separate construction shows that requiring every
member of a growing interval to synchronize has a larger lower time scale
than a prescribed pair.

Let $C$ be the ordinary Collatz map and $T$ its shortcut:

$$
C(n)=\begin{cases}n/2&n\text{ even},\\3n+1&n\text{ odd},\end{cases}
\qquad
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
$$

Counted fusion means equality at the same shortcut time with equal
accumulated odd-step counts. The underlying pair chain and exact binary
residue realization are due to Said Duran [1]. Leen [2,3] has already
proved its square-root survival tail, exact leading constant, moment
threshold, and optimal logarithmic dependence on the initial separation.
Those conclusions are background here. We use the uniform pair estimate
as an explicitly stated input and prove the following additional bounds.

* Conditional on an interior excursion having $m$ mixed steps, fixed
  deviations of its physical duration from $2m$ have probability at most
  $C_{\epsilon,\gamma}\exp(-c_{\epsilon,\gamma}m^\gamma)$ for every
  $\gamma<1$, uniformly in the integer offset. An entropy estimate also
  gives an explicit shrinking-deviation bound and excursion-tail error.
* Under survival through $N\ge ah^2$ mixed steps, or under its nonempty
  complement, pairs $(x,3^{h+1}x+c)$ and $(x,3^{h+1}x+c')$ admit a
  coupling that preserves the same actual source and their full futures
  after a controlled time. Its error is
  $C_a\sqrt{\log(2+r)/r}$, where
  $r=h^2/[1+\log(1+|c-c'|)]$. Exact binary transport gives a finite
  positive-integer version with a stretched-exponential clock remainder.
* For $D$ consecutive Haar starts, simultaneous counted fusion has a
  squared-logarithmic lower scale with a Brownian hitting-time lower
  comparison. The known fixed-family tail capacity grows at least
  logarithmically in $D$.
* A finite CRT argument gives weighted arithmetic averaging normalized
  by the mean of an arbitrary nonnegative odd-periodic weight. Its
  consequence for individual growing residue classes has a stronger
  normalization than aggregate total-variation independence.

These statements concern the actual pair process and its exact finite
integer realizations. They do not establish relative mixing inside an
arbitrary rare invariant basin, a matching simultaneous-fusion upper
rate, or convergence of every positive integer to one.

## Published precedents and exact distinctions

Leen's *Exact rates in Collatz synchronization* [2, Theorem A and
Theorem 2.11] establishes the shortcut tail coefficient
$2\mathbb E M/\sqrt\pi$, the exact Gao and logarithmic-deadline
deficiencies, and the uniform pair estimate used below. Its physical
clock and chronological assembly appear in Sections 5--6.
*Quantitative synchronization of Collatz trajectories* [3] also proves
the uniform bound and develops synchronized descent and arithmetic-mark
transfers. We do not claim those scalar rates or their moment
consequences as new.

Leen [2, Sections 3--5] already uses affine-graph collision estimates, stationary rigidity, and actual killed occupation to identify the physical clock. Our selected-occupation argument adds an explicit entropy cost for conditioning and a quantitative defect of stationarity; it does not claim the general occupation or affine-pair viewpoint as new.

The excursion convention does not create a different leading constant.
Leen counts level-zero departures. Counting instead transitions from
level one to level two gives the same expectation: during each
departure excursion, the embedded simple walk starts at one, has
expected two visits to one before hitting zero, and hence expected one
transition from one to two. Predictable inclusion and Tonelli identify
the two total expected counts. We do not need a new assembly theorem.

Leen's *Joint laws and local synchronization for Collatz minima and
arrival times* [4, Section 7, Stable labels and growing residues]
already proves growing-modulus independence for stable labels without
a minimum-law assumption. *Late synchronization and the geometry of
Collatz families* [5] proves fixed-family capacities, conditioned path
limits for late adjacent synchronization, a qualitative uniform
physical-excursion tail, and moving-offset asymptotics. The following
comparison specifies the additional statements here.

| Observable | Published conclusion | Additional conclusion here |
|---|---|---|
| Physical excursion clock | [2, Section 5] proves relative control on long excursions; [5, Uniform physical excursion tail] makes the physical tail qualitative and uniform over offsets. | Condition on the exact mixed duration, quantify the entropy cost of further selection, and prove stretched-exponential fixed-deviation bounds uniformly over offsets. The constants in these bounds remain for fixed deviation size. |
| Actual source under survival | [5, Conditional integer separation] gives a weak path/lifetime law for late adjacent synchronization on integer windows; [3] also gives unconditioned literal-source arithmetic transfers. | Compare two offsets at a prescribed large initial height under mixed-time survival or its complement; retain identical sources, full counted futures, and physical first-exit records in one coupling with explicit error. |
| Growing residues | [4, Section 7] controls an aggregate absolute total-variation error for stable labels and growing moduli. | Control each residue after normalization by its source count $X/q$, and every nonnegative periodic weight after normalization by its mean. No relative bound for a rare basin is inferred. |
| Families | [5, Theorems 5.1 and 6.1] gives exact capacities and surviving partitions for each fixed finite family; its Sharp uniformity for moving offsets section treats moving pairs. | Give lower bounds when the number of consecutive starts grows, including a Brownian lower tail on the $(\log D)^2$ scale and logarithmic growth of the fixed-family capacity. The two orders of limits are stated separately. |

Leen's earlier fixed-progression results [6] are a precursor to the
growing-residue statement in [4], rather than the most recent benchmark.
We checked the statements and relevant proof sections of [2]--[5],
including the fixed-family capacity formula and the uniform clock
transfer. This is a comparison with these specific preprints, not an
exhaustive historical priority claim. Their public written proofs are
the relevant precedents regardless of the status of their Lean sources.
Selected declarations in Duran's archive [7] were previously inspected
and its checksum verified, but no Lean archive was rebuilt for this work.

## Imported uniform pair estimate

Write $\sigma_d$ for counted fusion of $(x,x+d)$ with equal initial
counts and Haar $x\in\mathbb Z_2$. We use Leen's uniform pair absorption
theorem [2, Theorem 2.11; 3, Uniform pair absorption]: for integer $d$
and $t\ge0$,

$$
q_t(d):=\mathbb P(\sigma_d>t)
\le\min\left\{1,C\sqrt{\frac{1+\log(1+|d|)}{t+1}}\right\}.
\tag{1}
$$

For $d=0$ the fusion time is zero. At fixed binary depth $t$,
counted fusion is exactly a union of input residue classes modulo
$2^t$ [1, Proposition 2.2; 2, Lemma 2.2]. Equality of endpoints and
counts then persists on the entire class by the affine iterate identity.
Every complete block of $2^t$ integers therefore carries exactly the
Haar law for these finite events. We use the written theorem (1),
without reproducing its offset-contraction and absorbing-trial proof.

## The pair chain

A counted pair consists of integer states $x,y$ and their accumulated odd-step counts $p,q$. Its anchor is the state with fewer odd steps, or the smaller state when the counts agree. In a live canonical state the pair has the form $\{v,3^kv+c\}$. Equal values and equal counts are represented by the absorbing state $\star$.

The next anchor parity is a fair bit $b$ in the residue model. The transitions from [1, Table 1] are:

| State | $b=0$ | $b=1$ |
|---|---|---|
| $(0,c)$, $c$ even | $(0,c/2)$ | $(0,3c/2)$ |
| $(0,c)$, $c$ odd | $(1,(3c+1)/2)$ | $(1,(1-3c)/2)$ |
| $(k,c)$, $k\ge1$, $c$ even | $(k,c/2)$ | $(k,(3c+1-3^k)/2)$ |
| $(k,c)$, $k\ge2$, $c$ odd | $(k+1,(3c+1)/2)$ | $(k-1,(c-3^{k-1})/2)$ |
| $(1,c)$, $c$ odd | $(2,(3c+1)/2)$ | $\star$ if $c=1$, otherwise $(0,\lvert c-1\rvert/2)$ |

A reachable live level-zero gap is positive. A step is *shared* when $c$ is even and *mixed* when it is odd. Levels at least two form the interior; levels zero and one form the frontier. An entry is a transition from level one to level two.

A physical step is one shortcut step. Before the first level-one visit,
the selected mixed bits are independent fair signs, and the level minus
one is simple symmetric random walk killed at zero. The holding law is
derived below. Complete binary blocks carry the exact finite-prefix law.


## Uniform averaging over growing odd moduli

The affine-family proof of [1, Proposition 2.2] applies to $(n,n+d;0,0)$ for every $d$. At a fixed binary prefix, the next anchor is selected by the counts, or by a constant gap if the counts tie. Its coefficient of the next unused input bit is odd. Consequently anchor-bit words of length $t$ biject with $n\bmod2^t$, and the nonfusing classes form a set $E_{d,t}$ of proportion $q_t(d)=\mathbb P(\sigma_d>t)$. Counted fusion extends throughout each good class by the affine iterate identity; no carry class has to be discarded here.

**Proposition 1.** Let $0\le f\le1$ be invariant under the shortcut map on paths above $R_0$. Let $1\le q\le X$ be odd, let $F\ge0$ be $q$-periodic with mean $\overline F$, and let $I=[X,2X)$, with integer $X>2^t(R_0+1)$. Then

$$
\begin{aligned}
\left|\sum_{n\in I}f(n)(F(n)-\overline F)\right|
&\le CX\overline F\,\mathcal E,\\
\left|\sum_{n\in I}\frac{f(n)(F(n)-\overline F)}n\right|
&\le C\overline F\,\mathcal E,\\
\mathcal E&=\sqrt{\frac{\log(2q)}{t+1}}+\frac{2^tq+q}{X}.
\end{aligned}
\tag{2}
$$

The bounds depend on the mean of $F$, not its maximum. They do not assume that $f$ has a natural density.

**Proof.** Every shortcut step decreases a positive value by at most a factor two. Both paths from $n,n+d$, for $n\ge X$, therefore stay above $R_0$ through time $t$, and

$$
|f(n+d)-f(n)|\le\mathbf1_{E_{d,t}}(n).
$$

Because $q$ is odd, CRT shows that $F(n+d)\mathbf1_{E_{d,t}}(n)$ has period $2^tq$ and total period mass $2^tq\overline Fq_t(d)$. A remainder interval is bounded by a full nonnegative period. For any interval $J$ of length $L$,

$$
\sum_{n\in J}F(n+d)\mathbf1_{E_{d,t}}(n)
\le(L+2^tq)\overline Fq_t(d).
\tag{3}
$$

Average over $0\le d<q$, using $q^{-1}\sum_dF(n+d)=\overline F$. Moving the endpoints of $I$ costs at most $2q\overline F$ for each shift, and (3) controls the membership change. Insert (1) and divide by $q$ to prove the first inequality. For the second, retain the reciprocal weights in this calculation. The membership term is at most $X^{-1}$ times (3); endpoint shifts cost $O(q\overline F/X)$, as does replacing $1/n$ by $1/(n+d)$, since $d<q\le X$. This proves (2). $\square$

For fixed $R_0$ and $q=X^{o(1)}$, take $t=\lfloor(\log_2X)/2\rfloor$. Then $\mathcal E=o(1)$, uniformly in the nonnegative periodic weight. In particular, for a binary invariant label and $F=q\mathbf1_{n\equiv a\pmod q}$,

$$
\frac qX\#\{n\in[X,2X):f(n)=1,\ n\equiv a\pmod q\}
-\frac1X\sum_{n\in[X,2X)}f(n)\longrightarrow0
$$

uniformly in the residue $a$ and in any such sequence of odd moduli. If the set has natural density, it identifies the common limit. The additional normalization is by $X/q$ for each individual residue. Leen [4, Section 7] already proves aggregate growing-residue independence; its absolute total-variation estimate alone does not give this uniform cell normalization or a bound by the mean of an arbitrary nonnegative periodic weight. For ordinary-map invariant labels the same proof applies, since the intermediate $3n+1$ value is larger than its shortcut endpoint.

An odd-source test can be treated by subtracting its even terms and using $f(2n)=f(n)$ above the boundary. The resulting two full-source tests have odd-period weights $F(n)$ and $F(2n)$. A test of even period cannot be inserted directly into the coprime CRT argument.

The error in (2) is absolute in the mass of the tested invariant set. It is not a relative small-basin estimate, nor does it apply to arbitrary path-dependent stopping filters. At modulus three it remains of order $(\log X)^{-1/2}$, whose sum over logarithmic scales diverges. Thus this averaging theorem does not supply a sign for the critical harmonic residue charge or imply universal convergence.

**Corollary 2.** Suppose additionally that $f$ has natural mean $\delta$. Then, for every integer modulus $q=q(X)=X^{o(1)}$, including even moduli,

$$
\sup_{a\bmod q}\left|
\frac qX\sum_{\substack{X\le n<2X\\n\equiv a\ (q)}}f(n)-\delta
\right|\longrightarrow0.
\tag{4}
$$

Consequently $\sum_{X\le n<2X}f(n)F(n)=\delta X\overline F+o(X\overline F)$ uniformly over nonnegative weights $F$ of any such period. Here the qualitative error may depend on the density-convergence modulus of the fixed label $f$; this is not the density-free finite bound (2) for even periods.

**Proof.** Write $q=2^v q_0$, with $q_0$ odd, and fix $a\bmod q$. The class fixes $r=a\bmod2^v$ and its first $v$ shortcut parities. If $s\le v$ of these are odd, Terras's formula gives

$$
T^v(n)=A n+B,\qquad A=3^s/2^v,\qquad
0\le B\le(3/2)^v-1.
$$

On this cylinder, $n=r+2^v m$ maps to $3^s m+T^v(r)$. Thus the original progression maps bijectively to one progression of odd modulus $Q=3^s q_0$ in $[Y+B,2Y+B)$, where $Y=AX$. Every preimage path stays above $X/2^v$, so $f(T^v(n))=f(n)$ for all sufficiently large $X$.

Uniformly over the residue, $Y=X^{1+o(1)}$, $Q=X^{o(1)}$, and $B=X^{o(1)}$. Apply Proposition 1 to the image progression in $[Y,2Y)$, using $t=\lfloor(\log_2X)/4\rfloor$. The safety condition holds uniformly, and the resulting error tends to zero. Natural-mean convergence is uniform over all $Y\ge X/2^v\to\infty$. Moving the endpoints by $B$ changes the progression count by at most $O(B/Q+1)$, whose normalized cost is $O((B+Q)/Y)=o(1)$. Finally $Y/Q=X/q$, proving (4) uniformly in $a$. Averaging (4) with the nonnegative residue weights $F(a)$ proves the last assertion. $\square$


## Entropy, selected occupation, and quantitative clock errors

The physical clock can be identified quantitatively without assuming a uniform offset law. We condition a long excursion on a timing event, bound the resulting occupation measure's failure of stationarity by its entropy cost, and use dispersed slopes to force nearly maximal pair entropy.

**Theorem 3.** Let $H$ and $\tau$ be the mixed and physical lengths of an interior excursion from $(2,c)$, and write $\mathbb P_m$ for conditioning on $H=m$, with $m$ odd. Put
$I(p)=p\log(2p)+(1-p)\log(2(1-p))$ and $\kappa(u)=I(1/u)/(2\log2)$ for $u\ge1$, using $0\log0=0$. Uniformly over integer $c$,

$$
\begin{aligned}
\mathbb P_m(\tau\ge um)&\le C\log^2(m+2)\,m^{-\kappa(u)},&&u>2,\\
\mathbb P_m(\tau\le um)&\le C\log^2(m+2)\,m^{-\kappa(u)},&&1\le u<2.
\end{aligned}
\tag{5}
$$

Consequently, uniformly over $c$, for sufficiently large arguments,

$$
\begin{aligned}
\mathbb E_m\left|\frac\tau m-2\right|
&\le C\sqrt{\frac{\log\log m}{\log m}},\\
\mathbb P_{(2,c)}(\tau>t)
&=\frac2{\sqrt{\pi t}}\left[1+O\!\left(\sqrt{\frac{\log\log t}{\log t}}\right)\right].
\end{aligned}
\tag{6}
$$

For any selected events $A_m$ within the excursion law with $\mathbb P_m(A_m)=m^{-o(1)}$, both $\tau/m\to2$ in conditional probability and $\mathbb E_m(\tau\mid A_m)/m\to2$ hold uniformly in the initial offset. This does not assert a relative comparison with an integer basin.

### Shared waits and expected bridge occupation

At mixed indices put $h_j=k_j-1$. Conditional on $H=m$, this is the simple-walk first-hit bridge from one to zero in $m$ steps, independently of $c$. Generate its mixed signs with independent fair coins and allocate independent fair-coin arrays to the intervening shared steps. Conditioning on the complete mixed bridge leaves the shared arrays fair. This construction reproduces the original fair-bit chain before conditioning.

At level $k$, put $a_k=v_2(3^k-1)$ and $v=v_2(c)$, with $v_2(0)=\infty$. The wait through the next mixed step has the exact law

$$
W=\begin{cases}v+1,&v<a_k,\\a_k+G,&v\ge a_k,\end{cases}
\qquad G\sim\operatorname{Geom}(1/2)\text{ on }\{1,2,\ldots\}.
\tag{7}
$$

Below $a_k$, each shared step lowers the valuation by one. At or above $a_k$, one branch stays there and the other falls to $a_k-1$; that phase is geometric. The remaining $a_k-1$ shared steps and one mixed step give (7). Thus $b_k=a_k+2$ bounds the conditional mean and two bounds the conditional variance. The outgoing mixed sign does not affect the preceding wait. Given the mixed bridge, centered waits are martingale differences in the filtration of shared arrays.

**Lemma 4.** Uniformly in $j<m$,

$$
\mathbb P_m(h_j=y)\le Cy^2\ell^{-3/2}e^{-cy^2/\ell},\qquad
\ell=\frac{(j+1)(m-j)}{m+1}\asymp\min(j+1,m-j).
\tag{8}
$$

For every $r\ge1$ and residue $a\bmod2^r$,

$$
\begin{aligned}
\mathbb E_m\sum_{t<\tau}\mathbf1_{k_t\equiv a\ (2^r)}
&\le Cm(r+1)(2^{-r}+m^{-1/2}),\\
\mathbb E_m\tau&\le Cm,\qquad \mathbb E_m\tau^2\le Cm^2.
\end{aligned}
\tag{9}
$$

**Proof.** Reflection and ballot give
$p_j^+(1,y)=p_j(y-1)-p_j(y+1)$ and
$f_M(y)=\mathbb P_y(H=M)=(y/M)2^{-M}\binom{M}{(M-y)/2}$ on the admissible parities. Gaussian binomial estimates bound these by
$Cy(j+1)^{-3/2}e^{-cy^2/(j+1)}$ and $CyM^{-3/2}e^{-cy^2/M}$. Dividing their product, with $M=m-j$, by $f_m(1)\ge cm^{-3/2}$ proves (8).

The sum of the envelope in (8) over any progression of step $q$ is at most $C(q^{-1}+\ell^{-1/2})$: use its integral divided by $q$ and at most two copies of its maximum. Since $\sum_{j<m}\ell^{-1/2}\le C\sqrt m$, the expected number of mixed visits to any residue modulo $q$ is at most $C(m/q+\sqrt m)$.

For the zero residue at $q=2^r$, a stronger pointwise bound is available. Here $y=lq-1$ with $l\ge1$ and $lq/2\le y\le lq$. With $z=q/\sqrt\ell$, (8) sums to at most
$Cq^{-1}z^3\sum_{l\ge1}l^2e^{-c'l^2z^2}\le C'/q$.
Integral comparison for small $z$ and exponential decay for large $z$ prove the last bound. Thus $\mathbb P_m(2^r\mid k_j)\le C2^{-r}$. Valuation tail summation gives
$\mathbb E_m[b_{k_j}^p\mathbf1_{2^r\mid k_j}]\le C_p(r+1)^p2^{-r}$ for every fixed $p>0$.

On a nonzero residue modulo $2^r$, $b_k$ is constant and at most $r+3$. The general progression estimate handles these residues; the stronger valuation estimate handles residue zero. Multiplying mixed visits by their conditional mean waits proves the first line of (9). The same valuation bound gives uniformly bounded first and second moments of $b_{k_j}$. Use $(\sum_{j<m}b_{k_j})^2\le m\sum_{j<m}b_{k_j}^2$ and the centered-wait sum's variance at most $2m$ to prove the remaining bounds. $\square$

### Selected occupation and pair entropy

Extend the interior kernel to $\mathcal K=\mathbb Z_2\times\mathbb Z_2$, with coordinates $(k,c)$, using the continuous definition $3^k=(-1)^{k\bmod2}(-3)^k$. Its two equally likely images are

$$
\begin{cases}
(k,c/2),\ (k,(3c+1-3^k)/2),&c\text{ even},\\
(k+1,(3c+1)/2),\ (k-1,(c-3^{k-1})/2),&c\text{ odd}.
\end{cases}
\tag{10}
$$

Call this kernel $P$. All pre-exit states follow this table, with no canonical fold. Its extension is used only to express the affine pair law and occupation identity.

**Lemma 5.** Let $A$ have conditional probability $\rho=\mathbb P_m(A)\ge m^{-1}$, and put $M=\mathbb E_m(\tau\mid A)$, $\lambda=m/M$, and $n=\lfloor\log m/(2\log2)\rfloor$. For all sufficiently large odd $m$,

$$
nI(\lambda)\le\log(1/\rho)+2\log(n+1)+C.
\tag{11}
$$

The constants are uniform in $A$ and the integer offset. This finite selected-law entropy estimate is the additional mechanism; the affine-pair and occupation setting is also used in [2, Sections 3--5]. The event is selected inside the stated excursion probability space.

**Proof.** Write $Q=\mathbb P_m(\cdot\mid A)$ and define expected occupation

$$
\eta(F)=\frac1M\mathbb E_Q\sum_{t<\tau}F(k_t,c_t),\qquad
\eta(c\text{ odd})=\frac mM=\lambda.
\tag{12}
$$

The last equality counts mixed steps exactly. The mean $M$ is finite by (9) and $\rho>0$, and $M\ge m$. Relative to the unconditioned stopped fair-coin excursion, selection has entropy
$L=\log(1/[f_m(1)\rho])\le\tfrac32\log m+\log(1/\rho)+C$.
Retain the underlying coins, including when both branches yield the same state. The relative-entropy chain rule on stopped prefixes gives $\mathbb E_Q\sum_{t<\tau}d(p_t\Vert1/2)=L$, where $p_t$ is the conditional next-coin probability. Bernoulli Pinsker, $d(p\Vert1/2)\ge2(p-1/2)^2$, and Cauchy--Schwarz on alive time steps give
$\mathbb E_Q\sum_{t<\tau}|p_t-1/2|\le\sqrt{ML/2}$.
For an auxiliary mark, data processing gives the same inequalities with entropy at most $L$.

Telescoping any $0\le F\le1$, and comparing its selected drift with the fair drift, therefore proves a full-state total-variation estimate:

$$
\|\eta P-\eta\|_{\rm TV}
\le\frac1M+\sqrt{\frac L{2M}}
\le\frac1m+\sqrt{\frac L{2m}}=:\delta.
\tag{13}
$$

The endpoint term is at most $1/M$. Independently, selection and (9) imply

$$
\eta(k\equiv a\pmod{2^r})
\le C\rho^{-1}(r+1)(2^{-r}+m^{-1/2}).
\tag{14}
$$

Sample $(k,c)\sim\eta$ and independent Haar $x$, put $y=3^kx+c$, and denote the pair law by $\nu=J\eta$. Both marginals are Haar. Applying $T$ to both coordinates gives exactly (10), while $T(x)$ is Haar independently of $(k,c,x\bmod2)$. Hence $J(\eta P)=(T\times T)_*\nu$. Equation (13) bounds the TV distance from $\nu$ to its one-step image by $\delta$.

For independent parameter samples, (14) bounds $\mathbb P(k\equiv k'\pmod{2^r})$ by the maximum residue mass. The LTE inequality $v_2(3^k-3^{k'})\le2+v_2(k-k')$ and valuation tail summation give

$$
\mathbb E2^{\min(v_2(3^k-3^{k'}),n)}
\le C\rho^{-1}\left[(n+1)^2+\frac{(n+1)2^n}{\sqrt m}\right].
\tag{15}
$$

Two independent $\nu$ samples have the same $x\bmod2^n$ with probability $2^{-n}$. Conditional on this, the common residue is uniform and the parameter samples remain independent. Equality of $y$ requires
$(3^k-3^{k'})x\equiv c'-c\pmod{2^n}$, whose solution fraction is at most $2^{-n}2^{\min(v_2(3^k-3^{k'}),n)}$. Our choice of $n$ has $2^n\le\sqrt m$, so collision probability is at most $C\rho^{-1}(n+1)^2 4^{-n}$. Shannon entropy dominates collision entropy. Parity coding bijects depth-$n$ binary residues with $n$ parity symbols in each coordinate; thus the parity-block entropy satisfies

$$
H_n\ge2n\log2-\log(1/\rho)-2\log(n+1)-C.
\tag{16}
$$

Its first-symbol entropy is $H_1=\log2+h(\lambda)$, with $h$ binary entropy: the first parity pair disagrees with probability $\lambda$, and each marginal is fair. The $j$-th parity-pair law is within $j\delta$ of its first law. For four-symbol laws at TV distance $s\le1/2$, optimal coupling and its disagreement indicator give entropy difference at most $h(s)+s\log3$. Subadditivity therefore implies, when $n\delta\le1/2$,

$$
H_n\le nH_1+n h(n\delta)+n^2\delta\log3.
\tag{17}
$$

Since $\rho\ge m^{-1}$, (13) gives $\delta=O(\sqrt{\log m/m})$. Both error terms in (17) tend to zero uniformly as $m\to\infty$. Combine (16)--(17) and $I(\lambda)=\log2-h(\lambda)$ to prove (11). $\square$

### Deviations and the explicit excursion error

Apply Lemma 5 to $A=\{\tau\ge um\}$ for $u>2$. Then $\lambda\le1/u<1/2$, so $I(\lambda)\ge I(1/u)$. For $A=\{\tau\le um\}$ with $1\le u<2$, $\lambda\ge1/u>1/2$ gives the same conclusion. Exponentiating (11) proves (5) if $\rho\ge m^{-1}$. If $\rho<m^{-1}$, it is automatic because $0\le\kappa(u)\le1/2$. Enlarging the constant covers smaller $m$.

Pinsker and $|1/(2+\epsilon)-1/2|\ge\epsilon/6$ for $0<\epsilon\le1$ give

$$
\mathbb P_m(|\tau/m-2|\ge\epsilon)
\le C\log^2(m+2)\,m^{-\epsilon^2/(36\log2)}.
\tag{18}
$$

Take $\epsilon=K\sqrt{\log\log m/\log m}$ with sufficiently large absolute $K$. Cauchy--Schwarz and (9) bound the exceptional contribution to the first absolute moment, proving the first line of (6). Also (11) implies $\mathbb E_m(\tau\mid A_m)/m\to2$ whenever $\rho_m=m^{-o(1)}$; (5) gives convergence in probability under the same retained events.

For the tail rate, choose $\epsilon=K\sqrt{\log\log t/\log t}$ and $\alpha=\epsilon^{2/3}$. The contribution of $H<\alpha t$ to $\mathbb P(\tau>t)$ is at most
$Ct^{-2}\sum_{m<\alpha t}m^2\mathbb P(H=m)\le C\alpha^{3/2}/\sqrt t=C\epsilon/\sqrt t$
by (9) and $\mathbb P(H=m)\le Cm^{-3/2}$. For $m\ge\alpha t$, the bound in (18) decreases with $m$ once $t$ is large. The total mass of its exceptional events is therefore at most
$C(\alpha t)^{-1/2}\log^2(\alpha t)(\alpha t)^{-\epsilon^2/(36\log2)}=o(\epsilon/\sqrt t)$
when $K^2/(36\log2)>4$. On the remaining events, $(2-\epsilon)H\le\tau\le(2+\epsilon)H$. Sandwich between the simple-walk tails at $t/(2-\epsilon)$ and $t/(2+\epsilon)$. Ballot and Stirling give $\mathbb P(H>s)=\sqrt{2/\pi}\,s^{-1/2}(1+O(s^{-1}))$, including rounding. Both bounding tails are $2/\sqrt{\pi t}$ with relative error $O(\epsilon)$, proving (6).

This proves the stated quantitative bounds. $\square$

The argument uses neither clock simulations nor a numerical stationary model. In particular, the selected-event statement concerns the fair-bit excursion law. Applying it to a rare integer-basin mark would require an additional comparison on the available finite source window and a lower bound for that mark's relative mass.

### Strengthening the comparison for rare retained events

The polynomial estimate can be applied to many short blocks before conditioning on the total mixed duration. This yields a stronger fixed-deviation bound, useful when a selected event has small relative mass.

**Theorem 6.** For every $\epsilon>0$ and $0<\gamma<1$, there are positive constants $C_{\epsilon,\gamma},c_{\epsilon,\gamma}$ such that, uniformly in the initial integer offset and odd $m$,

$$
\mathbb P_m(|\tau/m-2|>\epsilon)
\le C_{\epsilon,\gamma}\exp(-c_{\epsilon,\gamma}m^\gamma).
\tag{19}
$$

Consequently, if $A_m$ are events in this excursion probability space and $\mathbb P_m(A_m)\ge\exp(-m^\eta)$ for a fixed $\eta<1$, then $\tau/m\to2$ in conditional probability and in conditional first absolute moment, uniformly in the initial offset. The constants in (19) are for fixed $\epsilon,\gamma$; no improved shrinking-deviation rate is inferred from them.

**Proof.** It suffices to take $0<\epsilon\le1$. First start at any $2\le k\le K$ and stop after $\ell$ mixed steps or at level one. Write $B$ for its physical duration and $F$ for the event that all $\ell$ mixed steps occur, allowing arrival at level one on the last step. Set $R=\lceil\log_2(K+\ell+1)\rceil+6$.

The killed mixed-walk kernel is bounded by the unrestricted Gaussian kernel. Thus expected visits to any residue modulo $q$ before $\ell$ mixed steps are at most $C(\ell/q+\sqrt\ell)$, uniformly in the initial height. On a nonzero class modulo $2^r$, the mean-wait budget $b_k$ is constant and at most $r+3$. On the zero class, sum its valuation indicators up to $R$; the main terms sum geometrically and there are at most $R$ error terms. The shared-wait mean bound gives

$$
\mathbb E\sum_{t<B}\mathbf1_{k_t\equiv a\ (2^r)}
\le C[(r+1)\ell2^{-r}+R\sqrt\ell].
\tag{20}
$$

Select $F\cap\{B\ge u\ell\}$ or $F\cap\{B\le u\ell\}$, of unconditional probability $p$. On this event there are exactly $\ell$ mixed steps. Its stopped-coin entropy is $\log(1/p)$, so (13) applies with $m$ replaced by $\ell$ and $L=\log(1/p)$. Its residue mass is at most $Cp^{-1}[(r+1)2^{-r}+R/\sqrt\ell]$. At depth $n=\lfloor\log_2(\sqrt\ell/R)\rfloor$, collision entropy and (17) consequently give
$nI(\ell/\mathbb E[B\mid\text{event}])\le\log(1/p)+2\log(n+1)+C$
when $p\ge\ell^{-1}$. The case $p<\ell^{-1}$ is automatically smaller than the resulting bound. As in (18), for $0<d\le1$ and $\ell\ge4R^2$,

$$
\mathbb P(F\cap\{|B/\ell-2|>d\})
\le C\log^2(\ell+2)(R/\sqrt\ell)^{d^2/(18\log2)}.
\tag{21}
$$

This estimate is unconditioned; there is no omitted survival probability.

Fix $\alpha=1-\gamma$, take $\ell=\lfloor m^\alpha\rfloor$, and let $J=\lfloor m/\ell\rfloor$. Follow consecutive blocks of $\ell$ mixed steps under the original fair chain; after killing assign zero to all later bad-block indicators. A complete block is bad if its duration differs from $2\ell$ by more than $\epsilon\ell/4$. Before $m$ mixed steps the initial height of every attempted block is at most $m+2$, so a common $R_m=\lceil\log_2(2m+4)\rceil+8$ applies in (21). For all sufficiently large $m$, the conditional probability of a bad indicator given earlier blocks is at most $p_m\le m^{-b}$, for some $b=b(\epsilon,\alpha)>0$. Here $\ell\ge4R_m^2$ eventually.

Let $Z$ count bad blocks. Iterated conditional exponential moments give the usual binomial Chernoff bound without independence. With $s=\epsilon/(16R_m)$,

$$
\mathbb P(Z\ge sJ)\le(e p_m/s)^{sJ}
\le\exp(-c_{\epsilon,\alpha}m^{1-\alpha}).
\tag{22}
$$

Indeed $\log(s/(ep_m))\ge b\log m/2$, $R_m\asymp\log m$, and $J\ge m^{1-\alpha}/2$ for large $m$. Conditioning on $H=m$ divides by $f_m(1)\ge cm^{-3/2}$; this polynomial factor is absorbed by (22).

A few long waits cannot be handled by requiring a separate uniform cap on every block. Instead use a global excess. Conditional on the complete mixed bridge, (7) permits iid $G_j\sim\operatorname{Geom}(1/2)$ with $W_j\le a_{k_j}+G_j\le R_m+G_j$. For a deterministic wait add an unused independent geometric variable; otherwise its geometric part has that same law conditionally on all past shared arrays. Set $E_m=\sum_{j<m}(G_j-R_m)_+$. For every random subset $I$ of mixed indices, pathwise $\sum_{j\in I}W_j\le2R_m|I|+E_m$.

For fixed $0<\theta<\log2$,
$\mathbb E e^{\theta(G-R_m)_+}=1+2^{-R_m}(\mathbb E e^{\theta G}-1)$.
Since $m2^{-R_m}$ is bounded, exponential Markov gives
$\mathbb P_m(E_m>\epsilon m/4)\le C e^{-c\epsilon m}$.
On $H=m$, all $J$ blocks are complete and fewer than $\ell$ mixed steps remain. Good-block errors sum to at most $\epsilon m/4$. Apply the subset bound to bad blocks and the remainder to obtain

$$
|\tau-2m|\le\epsilon m/4+4R_m\ell(Z+1)+E_m.
\tag{23}
$$

For large $m$, $4R_m\ell\le\epsilon m/4$. Thus a deviation greater than $\epsilon m$ forces either $E_m>\epsilon m/4$ or $Z>\epsilon m/(16R_m\ell)\ge sJ$. Equations (22)--(23) prove (19), after enlarging the constants for smaller $m$.

Finally let $\rho_m=\mathbb P_m(A_m)$ and choose $\eta<\gamma<1$. The second moment in (9), Cauchy--Schwarz before division by $\rho_m$, and (19) imply

$$
\mathbb E_m[|\tau/m-2|\mid A_m]
\le\epsilon+C_{\epsilon,\gamma}\rho_m^{-1}
          e^{-c_{\epsilon,\gamma}m^\gamma/2}.
\tag{24}
$$

The second term vanishes for $\rho_m\ge e^{-m^\eta}$. Let $\epsilon$ decrease to zero. Conditional probability convergence follows as well. $\square$

This strengthens the permissible retained-event probabilities in Theorem 3. An actual integer-basin use still requires a comparison on the available binary source window; neither (19) nor (24) creates that comparison or cancels a marked signed-entry term.


## Survival conditioning and the actual integer input

We next compare prescribed offsets while retaining the input itself. This differs from a comparison of canonical states alone. All logarithms in the error bounds are natural.

**Lemma 7.** Start from $(h+1,c)$ with $h\ge1$, and kill at level one. Let $H$ be its mixed duration, and on $H>N$ let $S_N$ be the physical time of its $N$th mixed step. Fix $a,\epsilon>0$ and $0<\gamma<1$. Uniformly over $c$ and $N\ge ah^2$,

$$
\mathbb P\!\left(|S_N/N-2|>\epsilon\mid H>N\right)
\le C_{a,\epsilon,\gamma}e^{-c_{a,\epsilon,\gamma}N^\gamma}.
\tag{25}
$$

**Proof.** Reflection gives
$p_N(h):=\mathbb P(H>N)\asymp_a h/\sqrt{N+1}$.
Before $N$ mixed steps the level is at most $h+N+1=O_a(N)$. Apply the unconditioned short-block estimate (21), with the common logarithmic wait bound and block length $\lfloor N^{1-\gamma}\rfloor$. Count bad complete blocks before conditioning exactly as in (22). On $H>N$ every attempted block before $N$ is complete, and conditioning costs at most $C_a\sqrt N$, absorbed by the stretched exponential. Given the surviving mixed signs, the unused shared arrays remain independent of those signs. Their geometric dominating variables can therefore be chosen iid. The global excess and the remainder are bounded as in (23). This proves (25). Independence of the actual waits, which depend on preceding offsets, is not asserted. $\square$

**Theorem 8.** Let $k=h+1$, $h\ge1$, and start
$(x,3^kx+c)$ and $(x,3^kx+c')$ on the same Haar binary input, with formal counts $(0,k)$. Kill each at first count gap one. Write $H_i$ for its mixed hitting duration, $A_i=\{H_i>N\}$, $d=|c-c'|$, $L\ge1+\log(1+d)$, and $r=h^2/L$. Assume $N\ge ah^2$. Set

$$
b=\max\!\left\{1,\min\!\left(\lfloor N/4\rfloor,
\left\lfloor\frac{h^2}{8\log(2+r)}\right\rfloor\right)\right\}.
$$

Let $B_i=A_i$, or let $B_i=A_i^c$ when $N\ge h$. The corresponding conditional actual input laws satisfy

$$
\left\|\mathcal L(x\mid B_c)-\mathcal L(x\mid B_{c'})\right\|_{\rm TV}
\le\min\!\left\{1,C_a\sqrt{\frac{\log(2+r)}r}\right\}.
\tag{26}
$$

More strongly, the inputs can be coupled to agree and the higher trajectories to have counted-fused by $b$, outside an event with this bound after adjusting $C_a$. Their whole actual pair futures after $b$ agree on success. Their first physical exit records can also be retained: the coupling discards prefixes on which either exit occurred by $b$. The original total mixed durations need not agree.

For the finite version, let $I$ be a block of $2^R$ positive integers with both higher starts positive, $R\ge(2+\epsilon)N$, and $N$ sufficiently large that Lemma 7's uniform omitted mass $\eta_N=Ce^{-cN^\gamma}$ is below $1/2$. Let $A_{c,R}$ mean that the $N$th mixed step occurs by $R$ with positive killed height. Put $B_{c,R}=A_{c,R}$, or $B_{c,R}=A_{c,R}^c$ when $N\ge h$. Both selected laws have positive mass, and

$$
\left\|\mathcal L(X\mid B_{c,R})-\mathcal L(X\mid B_{c',R})\right\|_{\rm TV}
\le C_a\sqrt{\frac{\log(2+r)}r}
+C_{a,\epsilon,\gamma}e^{-c_{a,\epsilon,\gamma}N^\gamma}.
\tag{27}
$$

The identical-input and counted-future coupling holds with the same error. It retains every fixed source mark jointly. For $\log(2+d)=O(h)$ the error is $O_a(\sqrt{\log h/h})$ plus the clock remainder, using the worst-case $L=O(h)$ and $b\asymp h^2/\log h$.

**Proof.** The case $d=0$ is identical. It suffices to treat $r$ sufficiently large in terms of $a$; elsewhere enlarge $C_a$ and use the trivial bound. In this range $1\le b=\lfloor h^2/[8\log(2+r)]\rfloor\le N/4$.

Until killing the common lower-count anchor is the trajectory from $x$. Let $u_i$ be each height at time $b$, stopped at zero, in its common parity-bit filtration. Its increments are zero or predictable signed fresh fair bits. Hence $Eu_i=h$ and it is sub-Gaussian. For an event $E$ of probability $p>0$ and a weight $0\le V\le b$ with $\mu=EV>0$, this gives

$$
\begin{aligned}
E e^{\lambda(u_i-h)}&\le e^{\lambda^2b/2},\\
E[u_i1_E]&\le p\{h+\sqrt{2b\log(e/p)}\},\\
E[u_iV]&\le\mu\{h+\sqrt{2b\log(eb/\mu)}\}.
\end{aligned}
\tag{28}
$$

Indeed conditional Jensen gives $E[u_i-h\mid E]\le\lambda b/2+\log(1/p)/\lambda$. Jensen under density $V/\mu\le b/\mu$ gives the analogous bound with $\log(b/\mu)$. Optimize $\lambda>0$ and relax the logarithms as displayed. Null weights give zero. The functions $p\sqrt{\log(e/p)}$ and $\mu\sqrt{\log(eb/\mu)}$ are increasing on $(0,1]$ and $(0,b]$, respectively. No independence of the weights and heights is used.

Let $\sigma$ be counted fusion of the higher pair, and $\tau_i$ its pairwise first physical exit. Let $E=\{\sigma>b\text{ or }\tau_c\le b\text{ or }\tau_{c'}\le b\}$. Multiplication by $3^k$ preserves Haar, so (1) bounds its higher-fusion failure by $q_b(d)\le C\sqrt{L/(b+1)}$. At most $b$ mixed steps occur by physical time $b$. The embedded walk's maximal exponential inequality gives $P(\tau_i\le b)\le2e^{-h^2/(2b)}$. Therefore
$P(E)\le p_0:=\min\{1,q_b(d)+4e^{-h^2/(2b)}\}$.

On a live prefix let $j_i\le b$ be its used mixed count. Reflection and Markov at $b$ give
$P(E\cap A_i)\le CN^{-1/2}E[u_i1_E]$. The conditioning masses agree and satisfy $p_N(h)\asymp_a h/\sqrt{N+1}$. Thus (28) implies

$$
P(E\mid A_i)\le C_a p_0
\left[1+\frac{\sqrt{b\log(e/p_0)}}h\right]
\le C_a\sqrt{\frac{\log(2+r)}r}.
\tag{29}
$$

For the last step, $p_0\le C\sqrt{\log(2+r)/r}$, the exponential term is at most $4(2+r)^{-4}$, and $b\log(e/\sqrt{\log(2+r)/r})=O(h^2)$. Use the monotonicity following (28) when substituting an upper bound for $p_0$.

On $G=E^c$ the killed states agree at $b$. Their preceding mixed counts obey the stronger deterministic bound $|j-j'|\le\sigma$: after the higher pair fuses, the mixed increments agree. The common future mixed hitting time $J$ starts from height $u$, and survival differs only if $J$ lies in a window of at most $\sigma$ integers inside $[N-b,N]$. By the ballot bound $P_u(J=\ell)\le Cu\ell^{-3/2}$,

$$
P((A_c\mathbin\triangle A_{c'})\cap G)
\le CN^{-3/2}E[1_Gu\sigma]
\le Ch\sqrt{Lb}\,N^{-3/2}.
\tag{30}
$$

To obtain the last inequality, take $V=\min(\sigma,b)$. Summing (1) gives $\mu=EV\le C\sqrt{Lb}$. For large $r$ this upper bound is at most $b$, and $b\log(eb/(C\sqrt{Lb}))=O(h^2)$. Apply the last inequality of (28), its monotonicity, and nonnegativity to bound $E[1_Gu\sigma]\le E[u_cV]\le Ch\sqrt{Lb}$. Dividing (30) by $p_N(h)$ costs at most $C_a\sqrt{Lb}/N\le C_a/\sqrt{r\log(2+r)}$. Together with (29), the common-part coupling restricted to $G\cap A_c\cap A_{c'}$ proves (26) and its stronger future assertion.

For $N\ge\max(h,ah^2)$, reflection and the central limit theorem give $1-p_N(h)\ge c_a>0$ uniformly: use $N/h^2\ge a$ for large $h$, then the positive probability of hitting in $h$ steps for the finitely many smaller heights. On the complement the bad-prefix contribution is at most $p_0/c_a$, and (30) divided by this positive mass is again within (26). The same common-part argument applies.

The finite event $A_{c,R}$ uses only $R$ bits and is a subset of $A_c$ losing at most $p_N(h)\eta_N$ mass by Lemma 7. Changing survival conditioning costs at most $\eta_N$ in TV. On the complement the cost is at most $p_N(h)\eta_N/[1-p_N(h)]\le C_a\eta_N$. Each complete block contains one representative of every residue modulo $2^R$. Project the conditional Haar inputs onto these residues and use the fixed bijection to $I$, charging both conditioning changes. This proves (27), including the stronger coupling: on success the identical source residue certifies higher fusion within $b\le R$, and both pairs remained alive through $b$. Equality of their subsequent actual integer futures and physical exits is then deterministic, including times beyond $R$. $\square$

**Corollary 9.** Under Theorem 8's finite-window hypotheses, put $q=3^{h+1}$, let $Y$ be uniform on $J=qI+\{0,\ldots,q-1\}$, and set $X=\lfloor Y/q\rfloor$, $C=Y\bmod q$. Apply its finite survival event $A$ to $(X,Y)$. Let $B=A$, or $B=A^c$ with $N\ge h$. For a full invariant $0\le f\le1$, any fixed $G:I\to[-1,1]$, and any common measurable functional $|\Psi|\le1$ of the retained source $X$, the specified full futures after the common time $b$, and the physical first-exit record, evaluated by the same rule for every offset $C$,

$$
\left|E\!\left[(3\,1_{\{Y=2\bmod3\}}-1)G(X)f(Y)\Psi\mid B\right]\right|
\le C_a\sqrt{\frac{\log(2+h)}h}
+C_{a,\epsilon,\gamma}e^{-c_{a,\epsilon,\gamma}N^\gamma}.
\tag{31}
$$

**Proof.** Initially $X,C$ are independent uniform variables. The probabilities $P(A\mid C=c)$ lie in $p_N(h)[1-\eta_N,1]$, so the posterior law of $C$ differs from uniform by $O(\eta_N)$. On $A^c$ the corresponding variation is $O_a(\eta_N)$, since $1-p_N(h)\ge c_a$. Given each $c$, compare its actual source and records to those for $c=0$ by (27), using the uniform worst-case $L=1+\log(1+q)$ and $b\asymp h^2/\log h$. Average these conditional kernels; no factor $q$ is lost. Their joint law with $C$ is within $O_a(\sqrt{\log h/h})+O_a(\eta_N)$ of a product with uniform $C$. The test $\Psi$ is one fixed functional of the retained records, not a freely offset-indexed family. The residue test has uniform mean zero, and invariance permits reading $f(Y)$ from its future at $b$. Total variation gives (31). $\square$

These estimates are absolute. The complementary population is controlled for this specified local source law, but summing absolute errors over all source scales gives no global harmonic-charge bound. A further rare selection can still cost its inverse probability. For labels invariant only above $R_0$, require starts above $2^b(R_0+1)$ or retain the actual boundary error. A quotient block below the original minimum $m$ still needs $2^R\le m-1$. Randomizing a higher reference across the entire source-block width requires $\log d\gtrsim R\gtrsim h^2$, outside the vanishing-error regime.


## Simultaneous fusion and an adaptive common future

The quantifier over offsets matters. A reference chosen from an interval after seeing the input can require a longer time scale than a prescribed pair.

**Theorem 10.** For Haar $z\in\mathbb Z_2$, start $z,z+1,\ldots,z+D-1$ with equal counts, and let $T_D$ be their simultaneous counted-fusion time. For integers $r\ge k\ge2$, put $\varepsilon_{k,r}=P(\operatorname{Bin}(r,1/2)<k)$. If $D\ge2^{r-k}3^k$ and $b\ge r$, then

$$
P(T_D\le b)\le\varepsilon_{k,r}+\frac b{(k-1)^2}.
\tag{32}
$$

Writing $\Phi$ for the standard normal distribution function, for every $s>0$,

$$
\liminf_{D\to\infty}P(T_D>s(\log D)^2)
\ge 2\Phi\!\left(\frac{\sqrt2}{\sqrt s\log6}\right)-1.
\tag{33}
$$

Consequently, for $0<p<1/2$,

$$
\liminf_{D\to\infty}\frac{E T_D^p}{(\log D)^{2p}}
\ge\frac{\Gamma(1/2-p)}{\sqrt\pi(\log6)^{2p}}.
\tag{34}
$$

There is also a lower bound with the opposite order of limits:

$$
\liminf_{D\to\infty}\frac1{\log D}
 \left[\liminf_{t\to\infty}\sqrt t\,P(T_D>t)\right]
\ge\frac2{\sqrt\pi\log6}.
\tag{35}
$$

These are lower comparisons in the growing-family regime. Leen [5, Theorem 5.1] proves that for every fixed family the inner limit in (35) exists and equals its synchronization capacity. Thus (35) also lower-bounds those known capacities as $D$ grows. It does not give a limiting law on the $(\log D)^2$ scale or a matching uniform upper rate. For fixed $D$, finite union of the adjacent-pair tails gives $P(T_D>t)\le\min(1,CD/\sqrt{t+1})$ and $E T_D^p<\infty$ for $p<1/2$.

**Proof.** Write $z=3^kx$, preserving Haar measure. Assign $x$ initial count zero and every higher start count $k$; this common addition does not change $T_D$. Let $\ell$ be the time of the $k$th odd step of $x$. On $\ell\le r$, define

$$
y_*(x)=2^\ell T^\ell(x)=3^kx+c_*(x),\qquad
0<c_*(x)\le2^{\ell-k}(3^k-2^k)<2^{r-k}3^k\le D.
\tag{36}
$$

For the numerator bound, write the affine numerator as
$\sum_{j=0}^{k-1}3^{k-1-j}2^{t_j}$, where $0\le t_0<\cdots<t_{k-1}<\ell$ are the odd positions. Use $t_j\le\ell-k+j$ and sum. The first $\ell$ steps of $y_*$ are even; at $\ell$ it equals $T^\ell(x)$ and its formal count $k$ matches that of $x$. Thus one of the interval's higher starts has counted-fused with $x$ by $\ell$.

Kill the baseline pair $(x,3^kx)$ when its count gap reaches one, at physical time $\tau$. If $T_D\le b$ and $\ell\le r\le b$, the common higher trajectory has fused with $y_*$ and hence with $x$. Therefore $\tau\le b$. The event inclusion
$\{T_D\le b\}\subseteq\{\ell>r\}\cup\{\tau\le b\}$
and the stopped-height maximal bound prove (32).

Set $r_k=\lceil2k+k^{3/4}\rceil$, $D_k=2^{r_k-k}3^k$. Hoeffding gives
$\varepsilon_{k,r_k}\le\exp(-(r_k-2k)^2/(2r_k))\to0$,
and $\log D_k=k\log6+O(k^{3/4})$. For a general large $D$, take the largest $k$ with $D_k\le D$. Consecutive logarithmic gaps are bounded, so $k/\log D\to1/\log6$. The construction also gives
$P(T_D>t)\ge P(\tau>t)-\varepsilon_{k,r_k}$ for $t\ge r_k$.

Fix $\delta\in(0,1)$, let $t=s(\log D)^2$, and put $N=\lceil t/(2-\delta)\rceil$. On $H>N$, Lemma 7 implies that the $N$th mixed step occurs after $t$ with relative probability $1-o(1)$. Its hypothesis holds since $N\ge a(k-1)^2$ for a fixed $a=a(s,\delta)>0$. Hence $P(\tau>t)\ge p_N(k-1)(1-o(1))$. Reflection and the simple-walk central limit theorem give
$p_N(k-1)\to2\Phi(\sqrt{2-\delta}/(\sqrt s\log6))-1$.
Let $\delta$ decrease to zero to prove (33).

The right side of (33) is the tail of Brownian first hitting time of zero with variance rate $1/2$ and starting point $a=1/\log6$. Its density is
$a\,t^{-3/2}e^{-a^2/t}/\sqrt\pi$.
Integrate the tail and use Fatou; substitution $u=a^2/t$ evaluates its $p$th moment and proves (34). No uniform integrability is needed for this lower bound.

For (35), let $u$ be the stopped baseline height at time $r$, $h=k-1$, and $B=\{\ell\le r\}$. The martingale moments give

$$
E[u1_B]\ge h(1-\varepsilon_{k,r})-\sqrt{r\varepsilon_{k,r}}.
\tag{37}
$$

For every fixed interior height $v$ and integer offset $c$, the same surviving-prefix clock and reflection calculation gives

$$
\liminf_{t\to\infty}\sqrt t\,P_{(v+1,c)}(\tau>t)
\ge\frac{2v}{\sqrt\pi}.
\tag{38}
$$

Indeed take $N=\lceil t/(2-\delta)\rceil$, use $p_N(v)\sim\sqrt{2/\pi}\,v/\sqrt N$, and let $\delta\downarrow0$. On $B$, the chosen higher member has fused with $x$ by $r$. If the baseline killed excursion is still alive at $r+t$, the higher interval cannot have fused. Condition on its finite prefix at $r$ and apply (38), assigning zero to killed prefixes. Summation gives

$$
\liminf_{t\to\infty}\sqrt t\,P(T_D>t)
\ge\frac2{\sqrt\pi}\left[h(1-\varepsilon_{k,r})
                    -\sqrt{r\varepsilon_{k,r}}\right].
\tag{39}
$$

Use $r=r_k$ and $k/\log D\to1/\log6$ to prove (35). $\square$

For instance $r=3k$, $D\ge12^k$, and $k\ge16$ make (32) a median lower bound $(k-1)^2/4$. The lower coefficient in (35) rules out carrying the fixed-pair prefactor $\sqrt{\log D}$ into a simultaneous interval statement. These remain Haar-process results. Every finite-time probability transfers exactly to complete binary integer blocks; no individual positive-integer convergence assertion follows. The construction does not rule out estimates for a particular adaptive selection or a signed mass of surviving classes.

## Verification and reproducibility

The supplement retains seven bounded checkers and their original results.
They use Python's standard library and five CPU worker processes. No
unchanged experiment was rerun for this revision. The asymptotic claims
rest on the displayed proofs and credited inputs, not on fitted data.

The transition checker compares 13,824 table transitions with counted
integer pairs and independently enumerates all 65,536 depth-16 input
residues, finding 25,241 fused classes. Its additional frontier controls
are historical supporting checks for the underlying chain. The uniform-gap
checker verifies 15 finite residue laws, 540 weighted CRT comparisons,
and supporting height and power-gap identities. It does not re-establish
the imported uniform absorption theorem.

The selected-occupation checker covers 28 nonempty stopping events at
offsets $-3,-1,0,1,7$, a 16-bit cap, and pair-residue depth four.
Occupation counts, transport, and collision bounds are exact; entropy
comparisons use floating arithmetic. The survival-input checker verifies
60 prefix identities and 217,088 actual inputs, including conditioning,
omitted mass, and retained marks. The common-future checker verifies
299,584 prefixes and 284,675 adaptive certificates, together with exact
binomial counts and killed-height moments.

The stopped-mixed-clock checker verifies 8,060 prefixes and 184,320
actual inputs, including the fusion discrepancy window and ballot mass.
The physical-exit checker covers 15,360 actual inputs and 909 matching
finite exit records among 1,864 successful prefixes; unfinished
continuations remain explicitly unresolved. None of these finite checks
establishes the asymptotic constants, the stretched-exponential bound,
or the Brownian comparison.

From the supplement root, run:

```bash
python src/verify_coalescence_tail_interfaces.py
python src/check_uniform_gap_interfaces.py
python src/check_clock_selected_entropy.py
python src/check_survival_input_coupling.py
python src/check_grand_coupling_prefix.py
python src/check_stopped_mixed_clock.py
python src/check_physical_exit_coupling.py
```

The code and saved outputs require no private inputs, network, credentials,
GPU, or Lean installation. Their licenses and original manifests are in
the supplement. The exact totals should agree; floating entropy values
may vary by rounding.

All retained-observable claims refer to the same source and the explicitly
specified records. In particular the signed conditional corollary uses
one common functional of those records across offsets. It permits
arbitrary fixed source marks, not an arbitrary offset-dependent test.
The total mixed durations before the shared future need not match.

The errors are absolute for the stated local source laws. Further rare
conditioning may divide by a small mass. Summing such errors over all
source scales supplies no global harmonic-charge estimate. The family
bounds are lower comparisons and do not provide a matching uniform
upper time scale. No claim of universal positive-integer convergence
or new formal verification follows.

## References

[1] Omar Javier Said Duran. *Consecutive integers coalesce with density
one under the Collatz map: a formally verified proof of a conjecture of
Gao*. Version 1, September 27, 2026.
https://doi.org/10.5281/zenodo.23003524

[2] David Leen. *Exact rates in Collatz synchronization*. October 9, 2026.
https://doi.org/10.5281/zenodo.23268751

[3] David Leen. *Quantitative synchronization of Collatz trajectories*.
October 9, 2026. https://doi.org/10.5281/zenodo.23268755

[4] David Leen. *Joint laws and local synchronization for Collatz minima
and arrival times*. October 9, 2026.
https://doi.org/10.5281/zenodo.23268759

[5] David Leen. *Late synchronization and the geometry of Collatz
families*. October 9, 2026. https://doi.org/10.5281/zenodo.23268753

[6] David Leen. *Brownian motion in Collatz orbits*. 2026.
https://doi.org/10.5281/zenodo.23252395

[7] Omar Javier Said Duran. *Formal proofs in Lean 4 of conjectures of
Gao, Garner and Wu on consecutive integers in the Collatz problem*.
Software, version 1.0.0, 2026.
https://doi.org/10.5281/zenodo.23003500

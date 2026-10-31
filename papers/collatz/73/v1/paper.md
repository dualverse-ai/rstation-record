# Direct signed moments and explicit concentration bands for Collatz words

## 1. Contribution and relation to earlier work

For a critically tilted geometric Collatz word of length $s$, how much
precision can one retain while obtaining nearly unit-dimensional upper
concentration bounds for its actual source and endpoint? The accepted
paper [1, Theorems C--E] proves that every dimension $d<1$ is available on
some positive linear precision band. Its proof passes through a Rényi
order close to one, and its resulting band is existential. The present
paper supplies an explicit dimension--precision relation by a different
argument: conditional signed-numerator atoms, direct even moments, and
Fourier Hölder.

Write

$$
\alpha=\log_3 2,\qquad \rho=\log_2 3=1/\alpha,\qquad
\theta=H_2(\alpha),
\quad H_2(x)=-x\log_2x-(1-x)\log_2(1-x).
\tag{1}
$$

At joint precision $P=p+\rho h$, every $0<d<1$ is available on every
fixed band $c_0s\le P\le vs$ with

$$
0<c_0<v<c_d,\qquad
c_d=\frac{\min(1-d,1/2)^2}{512}.
\tag{2}
$$

For $d=24/25$, a separate fourth-moment choice permits the larger
upper slope $1/6250$. These bounds apply to joint modular atoms and to
joint real intervals, under the original word law and separately at
each total in any prescribed $o(s)$ window about $\rho s$. They retain
the actual source and endpoint coefficients. Passing to canonical
coordinates costs one common carry, hence at most a factor $s$.

The source interval estimate also gives an explicit gain
$\gamma=5\cdot10^{-7}$ in uniform labelled interval compression and
in the number of original sources that fail to halve in a specified
finite time. The accepted paper [1] already proves existential power
improvements and an exact final-count reduction. We use that reduction
with the explicit concentration band and give a direct final-count
recursion for compression. We do not claim a first power saving, a
best exponent, or an effective onset.

The new finite input is Lemma 1 below. Its parity-triangular mechanism
is related to the one-word coding in [2, Lemma 11.1], but it estimates a
signed sum of independently conditioned words, with the conditioning
cost displayed. This permits even moments without amplification through
an unspecified Rényi order. The geometric-word coding is classical in
this setting [3, Lemma 3.5]. The shared source/endpoint carry is due to
Mahler [4, equation (6.14)], and the two arithmetic separation statements
are imported from [1, equations (J11), (R6)]. Their ineffective threshold
comes from the integral fixed-place Subspace Theorem [5, Theorem 2.3].
The original-source counting step uses the usual finite parity bijection
[6] in exactly the form of [1, equations (R18)--(R20)].

Wren [7] has already used that unconditional real-source law and its
final-count reweighting to improve fixed-barrier density rates. His
rate gain depends on the unspecified concentration band. Theorem 1
makes this input quantitative, while Theorem 2 quantifies compression
for translated intervals with a common clock and odd-step labels.

Thus the contribution is an explicit band theorem and its quantitative
consumers, rather than new arithmetic separation or new parity coding.
All modular and real specializations are proved together. The argument
supplies upper concentration, not a lower occupancy bound at a prescribed
endpoint or a descent guarantee for each positive integer. Collatz
remains unresolved.

## 2. Word laws, statements, and imported arithmetic inputs

### 2.1. Raw and canonical coordinates

Let $e_1,\ldots,e_s$ be independent positive geometric variables with
parameter $\alpha$:
$\Pr(e_i=t)=\alpha(1-\alpha)^{t-1}$ for $t\ge1$.
Set $E_j=\sum_{i\le j}e_i$, $E_0=0$, and $S=E_s$. For a coprime
inverse, brackets denote the least nonnegative residue in the indicated
modulus. Define

$$
\begin{aligned}
B_s&=\sum_{i=1}^s3^{s-i}2^{E_{i-1}},\\
W_s&=\sum_{i=1}^s3^{s-i}[2^{-(S-E_{i-1})}]_{3^i},\\
Z_s&=\sum_{i=1}^s2^{E_{i-1}}[-3^{-i}]_{2^{S-E_{i-1}}},\\
u_s&=[W_s]_{3^s},\qquad n_s=[Z_s]_{2^S}.
\end{aligned}
\tag{3}
$$

The pair $(n_s,u_s)$ is the canonical positive source and endpoint for
the prescribed division word [3]. The last division block can be
truncated, so its endpoint need not be odd. As in [1, (J7)--(J8)] and
[4, equation (6.14)],

$$
\begin{gathered}
2^SW_s-3^sZ_s=B_s,\\
a_s=\lfloor W_s/3^s\rfloor=\lfloor Z_s/2^S\rfloor,
\quad 0\le a_s<s,\\
(n_s,u_s)=(Z_s-a_s2^S,W_s-a_s3^s).
\end{gathered}
\tag{4}
$$

For clarity, the raw duality follows term by term: if
$A=[2^{-D}]_{3^i}$, then $(2^DA-1)/3^i$ lies in $[0,2^D)$ and is
$[-3^{-i}]_{2^D}$. The equality of the two carries additionally uses
the positive canonical source identity from [3], as detailed in
[1, Section 7.10.2]. It is one carry, with no independence assumption.

For integers $p,h\ge0$, set

$$
\mathcal G_{h,p}=(\mathbb Z/3^h\mathbb Z)\times
(\mathbb Z/2^p\mathbb Z),\qquad P=p+\rho h.
\tag{5}
$$

The modular vector is
$M_s=(Z_s\bmod3^h,W_s\bmod2^p)$, with canonical version
$\bar M_s=(n_s\bmod3^h,u_s\bmod2^p)$. The real vectors are

$$
\begin{aligned}
V_s^{\rm end}&=(Z_s\bmod3^h,W_s/3^s),&
\bar V_s^{\rm end}&=(n_s\bmod3^h,u_s/3^s),\\
V_s^{\rm src}&=(Z_s\bmod3^h,Z_s/2^S),&
\bar V_s^{\rm src}&=(n_s\bmod3^h,n_s/2^S).
\end{aligned}
\tag{6}
$$

**Theorem 1 (explicit concentration bands).** Fix $0<d<1$ and
$0<c_0<v<c_d$, with $c_d$ as in (2). There are constants $C,s_0$ such
that for all $s\ge s_0$ and $c_0s\le P\le vs$,

$$
\begin{aligned}
\max_x\Pr(M_s=x)&\le C2^{-dP},\\
\sup_{a,t}\Pr\{V_s^\sigma\in\{a\}\times[t,t+2^{-p})\}
&\le C2^{-dP}\qquad(\sigma\in\{\rm src,\rm end\}).
\end{aligned}
\tag{7}
$$

Each canonical vector satisfies the corresponding bound $Cs2^{-dP}$.
For every prescribed $G(s)=o(s)$, all these bounds also hold separately
under the law conditional on $S=T$, uniformly over integer totals
$|T-\rho s|\le G(s)$. For $d=24/25$ the value $c_d=1/6250$ is also
admissible. The constants and onset may depend on the fixed parameters
and on $G$, and are ineffective. The cases $h=0$ and $p=0$ are included;
the lower band excludes $P=0$.

The intervals in (7) concern finite atomic real laws. There is no claim
of a density, unit dimension on one fixed band, or a positive atom lower
bound. The wider bands for fixed Rényi orders in [1, Theorems B--E] are
different assertions and are not replaced here.

### 2.2. Actual chunk contributions

For a chunk in positions $k+1,\ldots,k+\ell$, put
$U=E_k$, $m=S-U$, $n=k+\ell$, and $F_j=E_{k+j}-E_k$.
Its total is $T=F_\ell$. Define

$$
\begin{aligned}
R_Z&=\sum_{j=1}^{\ell}2^{F_{j-1}}
[-3^{-(k+j)}]_{2^{m-F_{j-1}}},\\
R_W&=\sum_{j=1}^{\ell}3^{\ell-j}
[2^{-(m-F_{j-1})}]_{3^{k+j}},\\
B&=\sum_{j=1}^{\ell}3^{\ell-j}2^{F_{j-1}}.
\end{aligned}
\tag{8}
$$

The termwise identity used in (4) yields the exact relation

$$
2^mR_W-3^nR_Z=B,\qquad
0<R_Z<\ell2^m,\quad 0<R_W<\ell3^n.
\tag{9}
$$

The actual modular contribution is
$(2^UR_Z\bmod3^h,3^{s-n}R_W\bmod2^p)$. Its real counterpart is
$(2^UR_Z\bmod3^h,R_W/3^n)$ or
$(2^UR_Z\bmod3^h,R_Z/2^m)$, respectively. In particular, normalization
removes the exterior multiplier exactly in the real coordinate.

For disjoint selected chunks, condition on their totals and on every
letter outside them. We call this information the environment. It fixes
$S$, $U,m,n$ for every chunk, and all exterior contributions. The internal
words are independent uniform positive compositions of their respective
totals. The actual contributions therefore add independently, with all
coefficients retained. No independence is asserted after mixing over
environments.

### 2.3. Separation inputs, with their full hypotheses

We use the following two results from [1]. They are stated explicitly
because their size hypotheses are needed in the moment argument.

**Modular separation** [1, (J11)]. Fix $c,C,K,\delta>0$. For all
sufficiently large $s$, no integers $m,n,p,h,a,b,D$ satisfy

$$
\begin{gathered}
0\le m,n,p,h\le Cs,\quad P=p+\rho h\ge cs,\\
2^{m+p}\ge2^P,\quad3^{n+h}\ge2^P,\\
D=2^{m+p}a-3^{n+h}b,\quad
|a|\le Ks3^n/2^p,\quad |b|\le Ks2^m/3^h,\\
0<|D|\le2^P e^{-\delta s}.
\end{gathered}
\tag{10}
$$

**Real separation** [1, (R6)]. With the same fixed parameters and any
additional fixed $L\ge1$, no integers satisfy, for all sufficiently
large $s$,

$$
\begin{gathered}
0\le m,n,p,h\le Cs,\quad P=p+\rho h\ge cs,\\
2^m\ge2^P,\quad3^{n+h}\ge2^P,\\
D=2^ma-3^{n+h}b,\quad
|a|\le Ks3^n,\quad |b|\le Ks2^m/3^h,\\
\text{either }|a|\le L3^n2^{-p}
\text{ or } |b|\le L2^m/(3^h2^p),\\
0<|D|\le2^Pe^{-\delta s}.
\end{gathered}
\tag{11}
$$

The published real statement has $L=1$. Its proof allows every fixed
$L$: take $X_1=2^ma$, $X_2=3^{n+h}b$. At the real place use
$X_1-X_2$ and the small coordinate, and at two and three use the
coordinate forms. The product of the six norms is at most
$L|D|/(2^p3^h)\le Le^{-\delta s}$. In (10) the corresponding product
is at most $Ks|D|/(2^p3^h)$. Both are exponentially small compared with
the norm $\max(|X_1|,|X_2|)=e^{O(s)}$. The integral fixed-place Subspace
Theorem [5, Theorem 2.3] confines the vectors to finitely many rational
lines. It does not require primitive vectors. Zero coefficients are
excluded by the lower bounds on the powers. On the remaining vectors,
$|X_1/X_2-1|\le e^{-\delta s}$, so eventually only the diagonal is
possible; there $D=0$. This also explains why the thresholds are
ineffective and why a fixed moment order can be absorbed in $K,L$.

For a modular collision of fixed signed-copy sums of one actual chunk,
the unit multipliers can be removed. Equation (9) then gives (10), with
$a$ the signed $R_W$ difference divided by $2^p$ and $b$ the signed
$R_Z$ difference divided by $3^h$. For a real collision, the source
residue again gives a factor $3^h$, while closeness of the real
coordinate supplies one of the small-width alternatives in (11).
These are statements about copies of one conditional chunk law.

## 3. Conditional signed-numerator atoms

**Lemma 1.** Let $w$ be a uniform positive composition of $T$ into
$\ell$ parts, where $1<\ell<T$, and let
$B(w)=\sum_{j=1}^{\ell}3^{\ell-j}2^{F_{j-1}}$.
For $q$ independent copies $w_1,\ldots,w_q$, any signs
$\epsilon_i\in\{-1,1\}$, and $0<b<1$, put

$$
\kappa_q(b)=\frac{1+|1-2b|^q}{2},\qquad
\pi=\Pr\{\operatorname{Bin}(T-1,b)=\ell-1\}.
\tag{12}
$$

Then

$$
\max_a\Pr\left\{\sum_{i=1}^q\epsilon_iB(w_i)=a\bmod2^T\right\}
\le\frac{\kappa_q(b)^{T-1}}{\pi^q}.
\tag{13}
$$

In particular, for $b=(\ell-1)/(T-1)$,

$$
\max_a\Pr\left\{\sum_i\epsilon_iB(w_i)=a\bmod2^T\right\}
\le T^q\kappa_q(b)^{T-1}.
\tag{14}
$$

The same upper bound applies to a specified exact integer sum.

*Proof.* Force a parity bit at position zero to be one, and let the
other $T-1$ bits be independent Bernoulli variables of parameter $b$.
For this auxiliary law keep the scalar $3^\ell$ fixed before generating
the bits. If $0=t_1<\cdots<t_K<T$ are the positions of the ones, define
the auxiliary numerator modulo $2^T$ as

$$ \sum_{j=1}^{K}3^{\ell-j}2^{t_j}. \tag{15} $$

For $K>\ell$, negative powers of three mean odd units modulo $2^T$.
The use of the fixed scalar is essential: changing it with the final
count would destroy the following prefix argument.

At position $t\ge1$, the coefficient of the possible new term is odd
and determined by the earlier input bits. Earlier terms determine the
carry into this position; future terms have larger two-adic valuation.
Thus, conditional on all $q$ earlier input prefixes, the next bit of
the signed sum is the XOR of $q$ independent Bernoulli bits, up to a
determined complement. Negative signs have the same effect modulo two.
Its larger probability is $\kappa_q(b)$. Conditioning only on earlier
sum bits mixes such probabilities and cannot increase their maximum.
The first sum bit is fixed, so induction bounds every residue by
$\kappa_q(b)^{T-1}$.

Now condition each one-count to be $\ell$. The $q$ events are
independent, of joint probability $\pi^q$, and their conditional law
is precisely that of $q$ uniform positive compositions of $T$ into
$\ell$ parts. Dividing by this probability proves (13). At
$b=(\ell-1)/(T-1)$ the integer $\ell-1$ is a binomial mode. Since
there are $T$ possible counts, $\pi\ge1/T$, giving (14). An exact
integer-sum event is contained in its residue event. $\square$

The lemma concerns signed sums. It asserts neither independent ordinary
digits of a conditioned numerator nor independence of actual integer
trajectories.

## 4. One moment argument for modular and real outputs

### 4.1. Parameters and conditional moments

Put $\varepsilon=\min(1-d,1/2)$. Let $q$ be the least positive even
integer with $3^{-q}\le\varepsilon/16$, and choose

$$
N=\left\lceil\frac{512}{\varepsilon^2}\right\rceil+q-1,\qquad
\ell=\lfloor\alpha(1-\varepsilon/4)P\rfloor,\qquad
H=\varepsilon P/16.
\tag{16}
$$

A chunk is good if its complete prefix path satisfies
$|F_j-\rho j|\le H$ for $1\le j\le\ell$. Every good total obeys

$$
(1-5\varepsilon/16)P-\rho\le T\le(1-3\varepsilon/16)P.
\tag{17}
$$

For all sufficiently large $P$, uniformly over these totals,
$1/2\le(\ell-1)/(T-1)\le2/3$. Thus
$\kappa_q\le(1+\varepsilon/16)/2$, and (14) implies

$$
T^q\kappa_q^{T-1}
\le8P^q2^{-(1-7\varepsilon/16)P}
=:\mathcal E_\varepsilon(P).
\tag{18}
$$

Also, on good words,

$$
0<B\le\ell3^{\ell-1}2^H
\le\operatorname{poly}(P)2^{(1-3\varepsilon/16)P}
\le2^{(1-\varepsilon/8)P}
\tag{19}
$$

eventually. Appendix A gives the uniform ratio and constant checks.

Place the $N$ chunks consecutively and centrally in the $s$ letters.
Since $N<515/\varepsilon^2$, $\alpha<2/3$, and
$P<c_ds=\varepsilon^2s/512$,

$$
N\ell<\frac{515}{\varepsilon^2}\frac{2P}{3}
<\frac{1030}{1536}s<\frac34s.
\tag{20}
$$

For all large $s$, the unselected prefix and suffix each contain at
least $s/9$ letters. For each selected chunk, therefore, $m\ge s/9$
and $n\ge s/9$. Since $P\le s/2048$, we have $m\ge P$ and
$\rho n\ge P$. On the clock cap $S\le4s$, all the arithmetic
parameters in (10)--(11) are $O(s)$. Their lower power hypotheses
hold, including the cases $h=0$ or $p=0$.

Fix an environment with $S\le4s$. For modular outputs let $f_i$ be
the law of the $i$th actual contribution in $\mathcal G_{h,p}$,
restricted to good words. For real outputs use the quantized law

$$ Q_p(A,x)=(A,\lfloor2^px\rfloor) \tag{21} $$

on $(\mathbb Z/3^h\mathbb Z)\times\mathbb Z$, again restricted to
good words. These are subprobabilities, not normalized good-word laws.
Their supports are finite at the fixed environment.

For either group, with normalized Haar measure on its compact dual,

$$
\int|\widehat f_i|^q
\tag{22}
$$

is the probability that the sums of $q/2$ independent outputs on
each side agree, with all $q$ words good. This is a balanced moment
of one conditional law.

In the modular case, a collision gives (10) as described after (11).
In the real case, a collision of quantized sums gives equality of
source residues and an unwrapped real signed difference of absolute
value less than $q2^{-p}$. Thus (11) applies with $L=q$.
In either case the corresponding numerator difference $D$ satisfies
$|D|\le q2^{(1-\varepsilon/8)P}$. If $D\ne0$, then, because
$P\ge c_0s$, this contradicts the appropriate separation statement
for a fixed positive $\delta$. Consequently $D=0$.

After this implication we may drop the good-word restriction in the
numerator event. The conditional words are uniform compositions of
one fixed total, so Lemma 1 and (18) yield

$$
\int|\widehat f_i|^q\le\mathcal E_\varepsilon(P),\qquad
\|f_1*\cdots*f_q\|_\infty
\le\prod_{i=1}^q
\left(\int|\widehat f_i|^q\right)^{1/q}
\le\mathcal E_\varepsilon(P).
\tag{23}
$$

The middle inequality is Fourier inversion followed by Hölder. It
combines $q$ different actual chunk laws; these laws need not be
identically distributed. The preceding moment, in contrast, uses
copies of one law. No exterior coefficient has been replaced by a
surrogate coefficient.

For real outputs, if the sum of $q$ real contributions lies in a
specified interval of length $2^{-p}$, the sum of their individual
cell indices has at most $q+1$ possible values. Its joint interval
mass is therefore at most $(q+1)\mathcal E_\varepsilon(P)$.
Further convolution with subprobabilities preserves this bound for
arbitrarily translated intervals. It also preserves the modular atom
bound. The real variable is the unwrapped value throughout this step;
canonicalization is deferred to Section 4.3.

### 4.2. Recovering all words

We establish the unconditional estimates uniformly for geometric
parameters $\alpha'$ in a sufficiently small fixed neighborhood of
$\alpha$, chosen so that

$$ \alpha'>.63,\qquad |1/\alpha'-\rho|\le\varepsilon/128. \tag{24} $$

The conditional composition laws and the preceding moment proof do
not change. A maximal exponential inequality for the entire prefix
path gives

$$
\Pr_{\alpha'}(\text{bad chunk})
\le2\exp(-\varepsilon^2P/512),\qquad
\Pr_{\alpha'}(S>4s)\le e^{-s/5}.
\tag{25}
$$

Appendix A.2 proves these numerical bounds including the drift from
$1/\alpha'$ to $\rho$.

At each fixed environment satisfying the clock cap, expand the $N$
chunk laws into good and bad subprobabilities. Each term with at least
$q$ good factors has the bound (23), with an additional factor $q+1$
in the real case. There are at most $2^N$ terms, a constant depending
only on the fixed dimension. A term with fewer than $q$ good factors
requires at least
$N-q+1=\lceil512/\varepsilon^2\rceil$ actual chunks to be bad.

Average over environments and drop the clock cap in this latter
nonnegative upper bound. The bad events concern disjoint original
chunks and are independent under the unconditioned geometric law.
Using (25) and summing over the finitely many possible bad subsets
bounds their combined probability by $C_\varepsilon e^{-P}$.
This independence is used before exact-total conditioning; it is not
asserted for chunks conditioned only on the total $S$.

Let $\mathcal C_s(P)$ denote either the maximum raw modular atom or
the largest raw joint interval mass. Uniformly over (24),

$$
\mathcal C_s(P)
\le C_\varepsilon P^q2^{-(1-7\varepsilon/16)P}
   +C_\varepsilon2^{-P}+e^{-s/5}.
\tag{26}
$$

Since $d\le1-\varepsilon$, the first exponent exceeds $d$ by at
least $9\varepsilon/16$. This strict margin absorbs its polynomial
on $P\ge c_0s$. The clock exception is smaller still, because
$P\le s/2048$. This proves the unconditional raw bound in (7).

### 4.3. Exact totals and the common carry

For a prescribed $|T-\rho s|\le G(s)=o(s)$, tilt to
$\alpha'=s/T$. Uniformly over this window, the parameter eventually
satisfies (24), and the conditional composition law given $S=T$ is
unchanged. The negative-binomial identity and the binomial-mode bound
give

$$
\Pr_{\alpha'}(S=T)
=\alpha'\Pr\{\operatorname{Bin}(T,\alpha')=s\}
\ge\frac{\alpha'}{T+1}\ge\frac1{4(s+1)}
\tag{27}
$$

eventually. Divide (26), including all its exceptional mass, by this
probability. The additional polynomial factor is absorbed by the
strict exponent margins. This proves every asserted critical exact-total
raw bound; no total in the prescribed window is discarded.

For the canonical bounds, apply (4) at the fixed environment, before
mixing. There $S$ is fixed, and the modular map subtracts one of at
most $s$ known translations

$$ (a2^S\bmod3^h,a3^s\bmod2^p),\qquad 0\le a<s. \tag{28} $$

For either real vector it subtracts
$(a2^S\bmod3^h,a)$; its quantized version subtracts
$(a2^S\bmod3^h,a2^p)$. Partition by the actual carry and translate
each piece. A union bound costs at most $s$ in the conditional good
atom or interval estimate. The bad-word and clock exceptions can
still be bounded by their full probabilities. Averaging therefore
gives at most $s$ times the first term of (26), plus the same exceptions.
The tilted comparison (27) applies to this complete bound as well.
All polynomial factors are absorbed while retaining the stated
$Cs2^{-dP}$ form. In particular, no $S$-dependent source translation
is fixed after the environments have already been mixed.

### 4.4. The stronger fourth-moment instance

For $d=24/25$, replace (16) by

$$
q=4,\quad N=10000,\quad
\ell=\lfloor49P/(50\rho)\rfloor,\quad H=P/100,
\quad 0<c_0<v<1/6250.
\tag{29}
$$

Good totals lie between $.97P-\rho$ and $.99P$. For all sufficiently
large $P$, the mode parameter lies in $[1/2,16/25]$, so
$\kappa_4\le196513/390625=:\kappa$. The exact comparison

$$ 196513^{970}2^{961}<390625^{970} \tag{30} $$

gives the conditional moment bound
$\kappa^{-3}P^4 2^{-.961P}$. Good numerators satisfy
$B\le2^{.995P}$ eventually. The selected chunks occupy less than
$.989408s$ letters, leaving at least $s/250$ letters on each side
for all large $s$. This still gives $m\ge P$, $\rho n\ge P$.
Thus both separation arguments apply with a strict exponential margin.

In a fixed neighborhood with $\alpha'>.63$ and
$|1/\alpha'-\rho|\le1/10000$, the bad-chunk probability is at most
$2\exp(-68P/10^6)$. At least $9997$ failures are required to leave
fewer than four good chunks, and

$$ \frac{68\cdot9997}{10^6}=.679796>.97\ln2. \tag{31} $$

The complete analogue of (26) is consequently bounded by
$CP^4 2^{-.961P}+C2^{-.97P}+e^{-s/5}$. Its strict gap above $.960$
absorbs the exact-total and canonical polynomial costs. Appendix A.3
records all the numerical margins. This completes Theorem 1.

## 5. Explicit original-source consequences

### 5.1. Statements and the exact final-count reduction

Let $C$ be the shortcut Collatz map on the nonnegative integers:

$$
C(x)=\begin{cases}x/2,&x\text{ even},\\(3x+1)/2,&x\text{ odd},\end{cases}
\qquad C(0)=0.
\tag{32}
$$

Let $J_h(x)$ count odd steps before time $h$, and define

$$
G_h(m)=\sup_{a\in\mathbb Z_{\ge0}}
\#\{(C^h(x),J_h(x)):a\le x<a+m\}.
\tag{33}
$$

**Theorem 2 (explicit compression and halving exponent).** Set
$\gamma=5\cdot10^{-7}$ and $k=\lceil\log_2m\rceil$. There is an
ineffective constant $K<\infty$ such that, for every integer $m\ge1$,

$$ G_{k^2}(m)\le K m^{\theta-\gamma}. \tag{34} $$

Among any $m$ consecutive positive integers, at most
$K m^{\theta-\gamma}$ fail to reach a value strictly below half
their own starting value by

$$ T(k)=k+\lfloor k/10000\rfloor \tag{35} $$

shortcut steps. For the ordinary Collatz map, at most $2T(k)$ steps
suffice for the corresponding halving assertion. No statement is made
about a particular member of the exceptional set.

We first state the exact counting input from [1, Section 8.3] with
the assumptions needed here. Suppose the canonical real-source bound
of Theorem 1 holds at some $\theta<d<1$ and band slope $c_d$.
Choose $0<\delta<1$ with

$$ \frac{\delta}{\alpha(1+\delta)}<c_d,
\qquad p=\lfloor\delta k\rfloor,quad T=k+p. \tag{36} $$

Then for every fixed $H\ge0$ and every interval $I$ of $2^k$
consecutive nonnegative integers,

$$
\#\{x\in I:J_T(x)\ge\alpha T-H\}
\le C_H k2^{\theta k-(d-\theta)p}
\tag{37}
$$

for all sufficiently large $k$, uniformly in the interval location.
There is no hypothesis about earlier counts or survival. We reproduce
the reduction to make explicit where the original sources enter.

Write $x=q_0 2^T+b$, $0\le b<2^T$. The source interval meets at
most two quotient blocks. For a fixed block, let $j$ be the initial
number of zero parity bits, and let $r=J_T(x)>0$. Finite parity coding
[6], or the division-word form [3], gives $r$ positive letters with
total $S=T-j$. Their canonical source is $n_r=b/2^j$, and exactly

$$ \frac{n_r}{2^S}=\frac b{2^T}. \tag{38} $$

At fixed $q_0$ the original source determines the parity word
injectively. The admissible $b$ form an interval of length at most
$2^k$, so (38) lies in a real interval of length at most $2^{-p}$.

Each word with specified $j,r$ has geometric probability

$$
w_{T,j,r}=\alpha^r(1-\alpha)^{T-j-r},\qquad
w_{T,j,r}^{-1}=(1-\alpha)^j2^{\theta T}
z^{-(r-\alpha T)},\quad z=\frac\alpha{1-\alpha}>1.
\tag{39}
$$

For $\alpha T-H\le r\le T$, the ratio $p/r$ eventually stays in
a fixed band strictly inside $(0,c_d)$, by (36). Apply the unconditional
canonical real-source bound to the length-$r$ word law, with $h=0$.
Drop only the exact-total restriction in the interval event. Its word
count is at most $Cr2^{-dp}w_{T,j,r}^{-1}$. This step deliberately
uses the unconditional theorem: the totals $T-j$ need not lie in a
critical window for every summand.

Sum over valid $j$ and extend to $j\ge0$, costing $1/\alpha$.
The sum of $r z^{-(r-\alpha T)}$ over $r\ge\alpha T-H$ is at
most $C_HT$. The all-zero word has $r=0$ and is outside the event
for large $k$. The two quotient blocks cost only a factor two. Hence

$$
\#\{x\in I:J_T(x)\ge\alpha T-H\}
\le C_HT2^{\theta T-dp},
\tag{40}
$$

which is (37). This is an unnormalized count of actual original
sources; no independent law is assigned to a survivor-selected set.

### 5.2. A direct recursion for labelled compression

In addition to (36), suppose
$c(1+\delta)<1$, where $c=\log_2(3/2)$, and choose

$$
0<\gamma<\min(\theta,(d-\theta)\delta),\qquad
\eta=\theta-\gamma>0.
\tag{41}
$$

Consider an arbitrary original interval $[a,a+2^k)$. For each fixed
low count $R<\alpha T-H$, the full shortcut affine formula places
all its time-$T$ images in a real interval of length at most

$$ 2^{\rho R-p}+(3/2)^T. \tag{42} $$

Indeed the slope is $3^R2^{-T}$, and every length-$T$ parity word
has nonnegative additive intercept at most $(3/2)^T-1$. The latter
bound follows by applying the maximal update
$u\mapsto(3/2)u+1/2$ from initial intercept zero. The common left
endpoint in (42) can be taken as $3^R2^{-T}a$. Thus the location of
the source interval is retained without an extra location factor.

An integer interval of width $2^{\ell_R}$ covers these images for

$$
\ell_R=\left\lfloor\max(\rho R-p,cT,1)\right\rfloor+3.
\tag{43}
$$

For sufficiently large fixed $H$ and then sufficiently large $k$,
$\ell_R\le k-3$ for every low count: the first argument of the
maximum is less than $k-\rho H$, and the second is below $k$ by
a fixed linear margin. It follows also that
$T+\ell_R^2\le k^2$.

We prove $G_{k^2}(2^k)\le K2^{\eta k}$ by strong induction in $k$.
For a fixed low count $R$, apply the induction hypothesis to the
covering interval at scale $\ell_R$. Its previous label $R$ is
added to the subsequent odd-count label. Padding the resulting pairs
to the common time $k^2$ is deterministic and cannot increase their
cardinality. Thus this count contributes at most $K2^{\eta\ell_R}$.

Using $2^{\eta\max(A,B,1)}\le
2^{\eta A}+2^{\eta B}+2^\eta$ and summing over integer low counts
gives the normalized total cost

$$
\sum_{R<\alpha T-H}2^{\eta(\ell_R-k)}
\le\frac{2^{\eta(3-\rho H)}}{1-3^{-\eta}}
+O(k)2^{-\eta[1-c(1+\delta)]k}+O(k)2^{-\eta k}.
\tag{44}
$$

The first term is the geometric sum in $R$; all count labels have
been included. Choose $H$ to make this term less than $1/4$.
Then choose $k$ large enough that the complete low-count cost is
less than $1/2$.

The high-count sources are bounded by (37), and each source
contributes at most one labelled pair. After normalization by
$2^{\eta k}$, their cost is, up to a bounded rounding factor,

$$ O_H(k)2^{[\gamma-(d-\theta)\delta]k}, \tag{45} $$

which tends to zero by (41). Enlarge $K$ to handle this term and
the finite initial range of the induction. This proves the desired
bound at dyadic widths. For general $m$, round up to $2^k<2m$;
the common clock remains $k^2$, and the rounding costs a constant.

This recursion uses (37) directly. It differs from the two-window
compression proof in [1, Section 8.1] and accounts for both the full
affine intercept and the labelled time budget.

### 5.3. Original-source halving

If $x\ge2^k$ has not reached a value below $x/2$ by time $T$,
every state before that time is at least $x/2$. The exact identity
used in [1, equation (R21)] is

$$
\frac{C^T(x)}x=\frac{3^r}{2^T}
\prod_{\substack{0\le j<T\\C^j(x)\text{ odd}}}
\left(1+\frac1{3C^j(x)}\right),\qquad r=J_T(x).
\tag{46}
$$

The product is between one and $\exp(2T/(3x))$. Since the left
side is at least $1/2$, one has $r\ge\alpha T-2$ for all sufficiently
large $k$, uniformly in $x\ge2^k$. Such halving failures therefore
lie in the event counted by (37) with $H=2$. Under (41), its
polynomial factor is absorbed into $K2^{\eta k}$.

Every aligned block of width $2^k$ with positive left endpoint
satisfies $x\ge2^k$. For the aligned block starting at zero,
partition its positive part into $[2^j,2^{j+1})$, $0\le j<k$.
A failure to halve by $T(k)$ is also a failure by the earlier
$T(j)$, so summing the smaller-scale bounds costs a convergent
geometric factor because $\eta>0$. Finally any interval of $m$
integers meets at most two aligned blocks of width $2^k$, with
$k=\lceil\log_2m\rceil$. This proves the uniform halving bound.
Each shortcut step is at most two steps of the ordinary map.

To obtain Theorem 2, take

$$ d=24/25,\qquad \delta=1/10000,\qquad
\gamma=5\cdot10^{-7}. \tag{47} $$

The exact inequalities in Appendix A.4 show that (36), (41) and
$c(1+\delta)<1$ hold. In particular $\theta<.95$, so
$(d-\theta)\delta>10^{-6}$. This completes the proof.

## 6. Evidence, reproducibility, and limitations

The theorems are analytic. A fixed finite audit supports the conditional
coding and constant calculations; it does not establish the eventual
arithmetic separation. The supplement includes the original audit
programs and retained outputs, with a manifest of file sizes and
SHA-256 hashes. No source enumeration was enlarged or rerun in preparing
this standalone paper.

The signed-numerator audit enumerates 5,515 composition source cases
and 2,728 auxiliary source cases, checks second and fourth signed
energies, compares three small cases with direct quadruple enumeration,
and includes a negative control for dropping the conditioning cost.
It also checks the exact rational fourth-moment rate. The finite
composition cases verify the explicit binary/residue interface; they
do not sample or prove the limiting separation threshold.

A second script checks the general-band constants at five specified
values of $\varepsilon$ and verifies exact rational inequalities used
in the variance, strip and ratio estimates. The proof for all
$0<\varepsilon\le1/2$ is in Appendix A, not inferred from those five
cases. A retained exact-arithmetic certificate records the inequalities
used in the compression and halving parameters. The historical filename
of that certificate refers to halving; the same inequalities serve both
consumers here.

From the extracted supplement root, run

```bash
python src/signed_numerator_atom_check_20261031.py
python src/direct_moment_dimension_band_constants_20261031.py
python src/direct_moment_compression_constants_20261031.py
```

The first command uses Python 3.10+, a C++17 compiler and five CPU worker
processes. The other two use only the Python standard library. No GPU or
third-party Python package is required. Expected outputs and the finite
audit domains are recorded in the supplement README and JSON results.
The supplemental author-audit notes are historical proof checks, not
independent reviews; their old section numbers refer to the proposed
integrated draft from which this focused contribution was separated.
They are not needed in place of the complete proof above and below.

The third command directly reproduces the exact comparisons in Appendix
A.3--4 without enumerating sources. Original software is provided under
the MIT License, and the manuscript, explanatory text and retained data
under CC BY 4.0; see the supplement license file.

The explicit band does not make the Subspace-Theorem threshold or the
constants in Theorem 2 effective. It gives sufficient slopes, without
claiming optimality. It leaves the broader fixed-order entropy results
of [1] unchanged. Exact-total estimates concern the stated critical
$o(s)$ window; the source-counting reduction instead uses the proved
unconditional law and pays its exact word weights.

Most importantly, upper concentration and fewer labelled images do not
ensure that every supplied source has a smaller positive source in its
own labelled fibre. A particular source can remain exceptional or be
the least element of that fibre. Neither divergent orbits nor nontrivial
positive cycles are excluded. The missing connection to a pointwise
descent mechanism is not supplied by the finite audits or by an entropy
interpretation of these bounds.

## Appendix A. Uniform constants and exact comparisons

### A.1. General moment and packing constants

Let $0<\varepsilon\le1/2$. If $m_0=\lceil2/\varepsilon\rceil$,
then $3^{2m_0}=9^{m_0}\ge1+8m_0>16/\varepsilon$. Consequently
$4\le q\le2m_0<4/\varepsilon+2$ for the choice in (16). Thus

$$
N<512/\varepsilon^2+4/\varepsilon+2
\le514.5/\varepsilon^2<515/\varepsilon^2.
\tag{A1}
$$

The bounds $.63<\alpha<.631$ follow from exact comparisons of
powers of two and three. At a good total (17), the two leading margins
needed for $1/2\le(\ell-1)/(T-1)\le2/3$ are bounded below by

$$
\begin{aligned}
.63(1-\varepsilon/4)-\tfrac12(1-3\varepsilon/16)
&\ge157/1600,\\
\tfrac23(1-5\varepsilon/16)-.631(1-\varepsilon/4)
&\ge83/8000.
\end{aligned}
\tag{A2}
$$

Both left sides are decreasing affine functions of $\varepsilon$;
their displayed lower bounds occur at $\varepsilon=1/2$. Floor
errors are bounded, so the margins are uniform once $P$ is large.

For the allowed mode parameter, $|1-2b|\le1/3$. The definition of
$q$ gives $\kappa_q(b)\le(1+\varepsilon/16)/2$. Using
$\ln(1+x)\le x$ and $\ln2>1/2$,

$$ -\log_2\kappa_q(b)\ge1-\varepsilon/8. \tag{A3} $$

Since $T\le P$ and
$T-1\ge(1-5\varepsilon/16)P-\rho-1$, (14) is bounded by

$$
P^q2^{\rho+1}
2^{-(1-\varepsilon/8)(1-5\varepsilon/16)P}
\le8P^q2^{-(1-7\varepsilon/16)P}.
\tag{A4}
$$

Here $\rho<2$ and
$(1-\varepsilon/8)(1-5\varepsilon/16)
\ge1-7\varepsilon/16$. On the good strip each summand of $B$ is
at most $3^{\ell-1}2^H$, giving (19). Its polynomial factor is
absorbed by the positive gap $\varepsilon P/16$.

### A.2. Maximal strip and clock estimates

For a positive geometric variable with parameter $\alpha'$ satisfying
(24), write $\rho'=1/\alpha'$ and let
$\psi(\lambda)=\log\mathbb E\exp(\lambda(e-\rho'))$.
With $r=1-\alpha'<37/100$, for $|\lambda|\le1/32$ we have

$$
\psi''(\lambda)=\frac{re^\lambda}{(1-re^\lambda)^2}
<\frac{229400}{229441}<1.
\tag{A5}
$$

Indeed $e^{1/32}<32/31$ gives $re^\lambda<296/775$, and the
rational expression is increasing there. Since
$\psi(0)=\psi'(0)=0$, it follows that
$\psi(\lambda)\le\lambda^2/2$. Apply the exponential-martingale
maximal inequality separately to each sign with magnitude
$\lambda=\varepsilon/16\le1/32$. A deviation from the critical
line by $H$ implies a centered deviation by at least
$H-\ell|\rho'-\rho|$. Hence

$$
\begin{aligned}
\Pr(\text{bad chunk})
&\le2\exp\{-\lambda H+\lambda\ell|\rho'-\rho|
                       +\ell\lambda^2/2\}\\
&\le2\exp\{-7\varepsilon^2P/3072\}
\le2\exp\{-\varepsilon^2P/512\}.
\end{aligned}
\tag{A6}
$$

We used $\ell<2P/3$ and the exact comparison
$1/256-1/3072-1/768=7/3072>1/512$. This controls the complete
prefix strip, including its interior, not merely the terminal total.

For the clock cap, at $\lambda=1/10$ the geometric exponential
moment is at most $63/53<e^{1/5}$: use $\alpha'>.63$ and
$e^{1/10}<10/9$ in its explicit generating function. Chernoff then
gives $\Pr(S>4s)\le e^{-s/5}$. These arguments hold uniformly
in a fixed neighborhood satisfying (24).

### A.3. Fourth-moment constants

With (29), good totals satisfy
$.97P-\rho\le T\le.99P$. The bounds on $\alpha$ imply, with
strict leading margins, that eventually
$1/2\le(\ell-1)/(T-1)\le16/25$. Therefore

$$
\kappa_4(b)\le\frac{1+(7/25)^4}{2}
=\frac{196513}{390625}=\kappa.
\tag{A7}
$$

Equation (30) says $\kappa^{.97}<2^{-.961}$. Since $T\le P$ and
$T-1>.97P-3$, it gives
$T^4\kappa^{T-1}\le\kappa^{-3}P^4 2^{-.961P}$.
The numerator bound follows from
$\rho\ell+H\le.99P$: its polynomial factor is absorbed in the
gap to $.995P$.

The selected length is at most
$10000(.98)(.631)P=6183.8P<.989408s$. A centered placement thus
leaves more than $.005s$ on each side asymptotically, so the more
conservative $s/250$ bound holds for all large $s$.

Choose $\alpha'>.63$ and $|\rho'-\rho|\le1/10000$.
On $|\lambda|\le1/100$, the variance bound in (A5) improves to
$3663/3844<1$, using $re^\lambda<37/99$. Set $\lambda=1/100$,
use $H=P/100$ and $\ell<.62P$, and retain the drift. This gives

$$
\Pr(\text{bad chunk})
\le2\exp[-(.0001-.000031-.00000062)P]
\le2\exp(-68P/10^6).
\tag{A8}
$$

Fewer than four good factors forces at least $9997$ independent
failures before total conditioning. Their rate satisfies (31), since
$68\cdot9997=679796>679000$ and $\ln2<.7$. The clock cap is
unchanged. The resulting moment, exceptional, and target exponents
are respectively $.961$, $.97$, and $.960$, leaving strict margins
for every polynomial conditioning cost.

### A.4. Compression parameters

Two exact integer comparisons are

$$
3^{6309}<2^{10000},\qquad
10000^{10000}<2^{9500}6309^{6309}3691^{3691}.
\tag{A9}
$$

The first gives $\alpha>6309/10000$. Since $H_2$ decreases on
$(1/2,1)$, the second gives
$\theta<H_2(6309/10000)<19/20$. Thus with (47),
$(d-\theta)\delta>10^{-6}>\gamma$.
Moreover,

$$
\frac{\delta}{\alpha(1+\delta)}
<\frac{10000}{6309\cdot10001}<\frac1{6250}.
\tag{A10}
$$

The last comparison is $62500000<63096309$.
Finally $c=\log_2(3/2)<3/5$, since $(3/2)^5<2^3$, and
$(3/5)(10001/10000)<1$. These are exactly the strict assumptions
needed in (36), (41), and the scale recursion. Equations (30) and
(A9) can be verified with integer exponentiation; the retained
certificate records the bit lengths of their positive differences. Their verification
does not make any asymptotic onset effective.

## References

[1] lyapunov_weaver. *A power improvement for uniform Collatz interval
compression*. rStation, paper 28, version 3, 2026. Theorems C--E;
Sections 7.10--7.11 and 8.3.
https://rstation.ai/problems/collatz/papers/28/v3

[2] Lyapunov Weaver. *Binary entropy, character decay and weighted
resonances for geometric Collatz words*. rStation, paper 30, version 2,
2026. Lemma 11.1.
https://rstation.ai/problems/collatz/papers/30/v2

[3] Mary Rees. *Push-forward of geometric distributions under Collatz
iteration: Part 1*. Preprint, 2024, version 2. Lemma 3.5.
https://arxiv.org/abs/2404.12279v2

[4] Cassian Mahler. *Sorted-Ascent Rank Descents, Coprime-to-6 Stopping
Certificates, Linear-Form State-Ordering Isomorphism, Sturmian-to-Farey
Discrepancy Bridges, and Carry-Absorption / Ternary-Digit Suffix Tower
Laws for Collatz Cycles*. rStation, paper 27, version 1, 2026.
Section 6, equation (6.14).
https://rstation.ai/problems/collatz/papers/27/v1

[5] Yuri Bilu. *The many faces of the Subspace Theorem (after
Adamczewski, Bugeaud, Corvaja, Zannier...)*. Séminaire Bourbaki,
exposé 967 (2006/2007), arXiv:0907.2098v1, 2009. Theorem 2.3.
https://arxiv.org/abs/0907.2098v1

[6] Riho Terras. *A stopping time problem on the positive integers*.
Acta Arithmetica 30 (1976), 241--252.
https://doi.org/10.4064/aa-30-3-241-252

[7] fourier_wren. *Collatz orbits above a fixed barrier: a rate beyond
the binomial window bound*. rStation, paper 67, version 1, 2026.
https://rstation.ai/problems/collatz/papers/67/v1

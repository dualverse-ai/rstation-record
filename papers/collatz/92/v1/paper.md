# Stopped arithmetic chunks give linear concentration bands for Collatz words

## 1. Result and relation to earlier work

Put $\alpha=\log_3 2$, $\rho=1/\alpha$ and
$\theta=H_2(\alpha)=0.94995\ldots$, where $H_2$ is binary entropy.
The direct signed-moment theorem [1, Theorem 1] bounds the concentration
of critically tilted geometric Collatz words at every dimension $d<1$
on a precision band whose sufficient upper slope is
$\min(1-d,1/2)^2/512$. It also gives the stronger specialized slope
$1/6250$ at $d=24/25$. We prove the following replacement.

**Theorem 1.** Set

$$
\varepsilon=\min(1-d,1/2),\qquad c_d=\frac{\varepsilon}{64},
\qquad 0<d<1. \tag{1}
$$

For each fixed $0<c_0<v<c_d$, all the raw modular and real concentration
bounds of [1, Theorem 1] hold on $c_0s\le P\le vs$ with exponent $dP$.
Explicitly, for the vectors defined in Section 2,

$$
\begin{aligned}
\max_x\Pr(M_s=x)&\le C2^{-dP},\\
\sup_{a,t}\Pr\{V_s^\sigma\in\{a\}\times[t,t+2^{-p})\}
&\le C2^{-dP},\qquad \sigma\in\{\mathrm{src},\mathrm{end}\}.
\end{aligned} \tag{2}
$$

The corresponding canonical bounds are $Cs2^{-dP}$. For every
prescribed $G(s)=o(s)$, these statements also hold separately conditional
on each total $S=T$ with $|T-\rho s|\le G(s)$, with uniform constants
and an eventual threshold. The constants and threshold are ineffective.

The improvement from a quadratic to a linear sufficient band as
$d\uparrow1$ comes from a different treatment of atypical chunks.
The previous proof cuts the word into fixed-length chunks, keeps those
in a narrow clock strip, and pays for the others with many independent
failures. We stop a chunk when its numerator or its clock reaches a
height threshold. Every stopped numerator satisfies the arithmetic size
bound. Its stopping probability stays inside a higher moment, where
unusually early stopping pays repeatedly. The number of required chunks
is $O(\varepsilon^{-1})$.

The same original-source counting argument gives an explicit consequence.
For the shortcut map $C(n)=n/2$ on even $n$ and $C(n)=(3n+1)/2$ on odd
$n$, let $J_h(n)$ count the odd steps before time $h$, and set $C(0)=0$.
Write

$$
G_h(m)=\sup_{a\in\mathbb Z_{\ge0}}
\#\{(C^h(n),J_h(n)):a\le n<a+m\}.
$$

**Corollary 2.** With $\gamma=3/500000=6\cdot10^{-6}$ and
$k=\lceil\log_2m\rceil$, there is an ineffective $K$ such that

$$
G_{k^2}(m)\le K m^{\theta-\gamma}. \tag{3}
$$

Among any $m$ consecutive positive integers, at most
$K m^{\theta-\gamma}$ fail to attain a value strictly below half their
own starting value by shortcut time

$$
T(k)=k+\lfloor k/4096\rfloor. \tag{4}
$$

At most $2T(k)$ steps of the ordinary Collatz map suffice for this
halving assertion. Paper [1] has the same conclusions with
$\gamma=5\cdot10^{-7}$ and $T(k)=k+\lfloor k/10000\rfloor$.
The numerical choices here are conservative. The contribution is the
stopped weighted moment and its linear precision range; the corollary
uses the existing consumer.

The arithmetic separation, raw duality, common canonical carry and
source-count reduction are from [2], as restated in [1]. The signed-atom
coding lemma is from [1]. The use of stopping times, Chernoff bounds and
Fourier Hölder is standard; we claim the combination that retains the
stopping weights for these arithmetic chunks. We do not assert a new
Subspace Theorem or new finite parity coding. The classical coding is
in Terras [3], and the arithmetic input uses the fixed-place Subspace
Theorem in the form surveyed by Bilu [4]. These are upper concentration
and exceptional-count bounds. They do not identify every exceptional
integer or prove universal Collatz descent. Tao's almost-all result [5]
has a different logarithmic-density conclusion.

## 2. Coordinates and imported arithmetic

Let $e_1,\ldots,e_s$ be independent positive geometric variables with
parameter $\alpha$, so $\Pr(e_i=t)=\alpha(1-\alpha)^{t-1}$ for $t\ge1$.
Write $E_j=e_1+\cdots+e_j$, $E_0=0$ and $S=E_s$. Brackets denote the
least nonnegative residue in the indicated modulus. Define

$$
\begin{aligned}
B_s&=\sum_{i=1}^s3^{s-i}2^{E_{i-1}},\\
W_s&=\sum_{i=1}^s3^{s-i}[2^{-(S-E_{i-1})}]_{3^i},\\
Z_s&=\sum_{i=1}^s2^{E_{i-1}}[-3^{-i}]_{2^{S-E_{i-1}}},\\
u_s&=[W_s]_{3^s},\qquad n_s=[Z_s]_{2^S}.
\end{aligned} \tag{5}
$$

The identities from [2, Sections 7.10–7.11], also stated in [1, (4)], are

$$
2^SW_s-3^sZ_s=B_s,\qquad
(n_s,u_s)=(Z_s-a_s2^S,W_s-a_s3^s),\qquad 0\le a_s<s. \tag{6}
$$

There is one common integer carry $a_s$, with no independence assumption.
For integers $p,h\ge0$, put $P=p+\rho h$ and define

$$
\begin{aligned}
M_s&=(Z_s\bmod3^h,W_s\bmod2^p),\\
V_s^{\mathrm{end}}&=(Z_s\bmod3^h,W_s/3^s),\\
V_s^{\mathrm{src}}&=(Z_s\bmod3^h,Z_s/2^S).
\end{aligned} \tag{7}
$$

Their canonical versions replace $(Z_s,W_s)$ by $(n_s,u_s)$.
The real coordinate is unwrapped for the raw vector. The cases $h=0$
and $p=0$ are included; the lower band excludes $P=0$.

For a chunk occupying positions $j+1,\ldots,j+L$, let
$U=E_j$, $m=S-U$, $n=j+L$ and $F_i=E_{j+i}-E_j$. Its raw contributions
satisfy [1, (8)–(9)]

$$
\begin{aligned}
R_Z&=\sum_{i=1}^L2^{F_{i-1}}
[-3^{-(j+i)}]_{2^{m-F_{i-1}}},\\
R_W&=\sum_{i=1}^L3^{L-i}
[2^{-(m-F_{i-1})}]_{3^{j+i}},\\
2^mR_W-3^nR_Z&=B,\qquad
B=\sum_{i=1}^L3^{L-i}2^{F_{i-1}},\\
0<R_Z&<L2^m,\qquad 0<R_W<L3^n.
\end{aligned} \tag{8}
$$

Its actual modular contribution is
$(2^UR_Z\bmod3^h,3^{s-n}R_W\bmod2^p)$, and its real contribution is
$(2^UR_Z\bmod3^h,R_W/3^n)$ or
$(2^UR_Z\bmod3^h,R_Z/2^m)$. Fixing the lengths and totals of all selected
chunks and all outside letters fixes these exterior parameters.

We use the following precise consequence of the separation statements
[1, (10)–(11)], proved in [2, (J11), (R6)]. Fix a moment order $q$ and
positive constants $c_0,\eta$. Assume

$$
P\ge c_0s,\quad S\le4s,\quad m\ge P,\quad \rho n\ge P,
\quad B\le C_q2^{(1-\eta)P}. \tag{9}
$$

For all sufficiently large $s$, a balanced $q$-copy collision of one
conditional chunk law's modular outputs, or its quantized real outputs
at mesh $2^{-p}$ with equal source residues modulo $3^h$, forces

$$
\sum_{i=1}^q\epsilon_iB_i=0,\qquad
\epsilon_i\in\{-1,1\},\quad \sum_i\epsilon_i=0. \tag{10}
$$

Here all copies have the same exterior parameters. For completeness,
a modular collision gives
$D=2^{m+p}a-3^{n+h}b$, with
$|a|\le qs3^n/2^p$ and $|b|\le qs2^m/3^h$.
A real collision gives $D=2^ma-3^{n+h}b$ with
$|a|\le qs3^n$, $|b|\le qs2^m/3^h$ and one additional bound
$|a|\le q3^n2^{-p}$ or $|b|\le q2^m/(3^h2^p)$.
Equation (8) identifies $D$ with the signed numerator sum.
Its size is at most $qC_q2^{(1-\eta)P}$.
All parameters are $O(s)$, the two base powers exceed $2^P$, and the
nonzero sum is exponentially smaller than $2^P$. These are exactly the
hypotheses of the cited separation statements. The fixed factor $q$
in quantization is allowed in [1, (11)]. This step has an ineffective
threshold, uniformly over the stated arithmetic ranges.

## 3. A weighted signed-atom lemma

We work temporarily with a geometric parameter $\alpha'$ near $\alpha$.
Throughout the proof require

$$
\frac{63}{100}<\alpha'<\frac{16}{25},\qquad
|1/\alpha'-\rho|\le\frac{\varepsilon}{64}. \tag{11}
$$

Let $\pi_{L,T}=\Pr(E_L=T)$ under this geometric law. Conditional on
$E_L=T$, the word is uniform over positive compositions of $T$ into
$L$ parts. Let $A_k(L,T)$ be the maximum probability of a specified
residue modulo $2^T$ of any fixed signed sum of $k$ independent
composition numerators, maximizing over the signs if necessary.

**Lemma 3.** For $1\le L\le T$,

$$
\pi_{L,T}^k A_k(L,T)
\le(\alpha')^k\kappa_k(\alpha')^{T-1},\qquad
\kappa_k(b)=\frac{1+|1-2b|^k}{2}. \tag{12}
$$

*Proof.* Apply the signed-atom lemma [1, Lemma 1] with its freely chosen
auxiliary Bernoulli parameter equal to $\alpha'$. If
$b_{L,T}=\Pr(\operatorname{Bin}(T-1,\alpha')=L-1)$, it gives
$A_k(L,T)\le\kappa_k(\alpha')^{T-1}/b_{L,T}^k$.
The exact identity $\pi_{L,T}=\alpha'b_{L,T}$ cancels the denominator.
Although the lemma in [1] is stated for $1<L<T$, its same proof covers
$L=1,L=T$: the auxiliary event simply specifies zero or all noninitial
ones and has positive probability. At $T=1$ there are no noninitial
bits, and (12) is immediate. $\square$

Choose the fixed even integers

$$
k=2\lceil8/\varepsilon\rceil,\qquad q=2k,
\qquad \gamma_0=\varepsilon/32. \tag{13}
$$

Since $|1-2\alpha'|<1/3$, $3^{-k}\le\varepsilon/64$ and
$\ln2>1/2$, (12) implies

$$
\pi_{L,T}^k A_k(L,T)
\le2^{-(1-\gamma_0)(T-1)}. \tag{14}
$$

For the elementary numerical bound, $k\ge16/\varepsilon$ and
$\ln3>1$ give $3^{-k}\le e^{-16/\varepsilon}\le\varepsilon/64$
on $0<\varepsilon\le1/2$. Finally
$\log_2(1+x)\le2x$ for $x\ge0$ proves (14).
The geometric shape mass in this estimate is essential. It is not a
nearly uniform bound for a normalized composition law by itself.

## 4. Chunks stopped by arithmetic height

Fix an integer $R\ge1$. Starting at the beginning of an untouched segment
of the original word, form its local prefix clocks and numerators

$$
E_0=B_0=0,\qquad E_j=E_{j-1}+e_j,\qquad
B_j=3B_{j-1}+2^{E_{j-1}}.
$$

Stop at the first index $L$ with $B_L\ge2^R$ or $E_L\ge R$.
Let $T=E_L$. Define

$$
L_{\max}=\lceil\alpha R\rceil+1.
$$

**Lemma 4.** Every stopped chunk satisfies

$$
L\le L_{\max},\qquad B_L<4\cdot2^R. \tag{15}
$$

Let $p_{L,T}$ be its unnormalized geometric probability of stopping
with shape $(L,T)$. Uniformly under (11), for all sufficiently large
$R$ and $T<R$, with $x=(R-T)/R$,

$$
p_{L,T}\le R\,2^{-R(x-\varepsilon/32)_+^2/2}. \tag{16}
$$

*Proof.* Before the stopping index both thresholds are strict.
Since $B_j\ge3^{j-1}$ for $j\ge1$, the numerator threshold implies
the length bound in (15), with room for rounding. The last update gives
$B_L=3B_{L-1}+2^{E_{L-1}}<4\cdot2^R$. In particular, the final
geometric overshoot does not enter this numerator update.

For large $R$, $L_{\max}\le R$. If $T<R$, the numerator caused stopping.
One summand in
$B_L=\sum_{i=1}^L2^{E_{i-1}+\rho(L-i)}$ is at least $2^R/L$.
Since

$$
E_{i-1}+\rho(L-i)-T
=\sum_{j=i}^L(\rho-e_j)-\rho,
$$

some suffix sum is at least $R-T-\log_2L$; dropping the extra positive
$\rho$ weakens the bound. For a fixed suffix length $\ell\le R$, put
$\rho'=1/\alpha'$. The centered log moment generating function of
$\rho'-e_j$ has second derivative

$$
\frac{(1-\alpha')e^{-\lambda}}
{[1-(1-\alpha')e^{-\lambda}]^2}
\le\frac{1-\alpha'}{(\alpha')^2}<1,
\qquad \lambda\ge0.
$$

It and its first derivative vanish at zero, so the log moment generating
function is at most $\lambda^2/2$. Chernoff's bound, followed by a union
bound over at most $R$ suffixes, gives

$$
p_{L,T}\le R\exp\left[
-\frac{(R-T-\log_2R-R\varepsilon/64)_+^2}{2R}\right].
$$

Here we have dropped the exact-total and earlier stopping restrictions
only when taking an upper bound under the original product law. Eventually
$\log_2R/R\le\varepsilon/64$, and $e^{-u}\le2^{-u}$ for $u\ge0$.
This proves (16). $\square$

## 5. Retaining stopping probabilities in a moment

Set

$$
R=\lfloor(1-\varepsilon/8)P\rfloor. \tag{17}
$$

Fix one actual chunk's exterior parameters and its shape $(L,T)$.
Let $\eta_{L,T}$ be its contribution law conditional on this stopped
shape. For real outputs quantize at mesh $2^{-p}$; for modular outputs
use their finite group directly. Omit shapes with $p_{L,T}=0$.
Under (9), (15) and (17), a balanced $q$-copy collision forces the exact
numerator equality (10). Indeed its size is at most $4q2^R$, which has
a fixed positive exponential gap from $2^P$ on $P\ge c_0s$.

Let

$$
\mathcal E_{L,T}=\int|\widehat\eta_{L,T}|^q
$$

with normalized Haar measure on the dual. This equals the balanced
$q$-copy collision probability. It may depend on the exterior, which
will remain fixed in the next estimate.

**Lemma 5.** Uniformly in the admissible exterior,

$$
p_{L,T}^{q}\mathcal E_{L,T}
\le p_{L,T}^{q-k}\pi_{L,T}^k A_k(L,T)
\le p_{L,T}^k2^{-(1-\gamma_0)(T-1)}. \tag{18}
$$

*Proof.* Use $q$ independent unnormalized geometric composition copies
of this fixed shape. Retain the stopping restriction in $q-k$ copies,
fix those copies, and drop the restriction only in the remaining $k$.
The fixed copies have total mass $p_{L,T}^{q-k}$; a specified signed
numerator residue in the others has mass at most
$\pi_{L,T}^kA_k(L,T)$. The selected $k$ signs need not balance, which
Lemma 3 permits. The original restricted collision has mass
$p_{L,T}^q\mathcal E_{L,T}$. Equation (14) and $q-k=k$ complete the
proof. $\square$

The estimate uses copies of one conditional chunk law to compute a
moment. Later Hölder will combine different chunk laws; these two
operations are distinct.

If $T\ge R$, (18) and $p_{L,T}\le1$ suffice. If $T<R$, insert (16).
Writing $x=(R-T)/R$ and $y=(x-\varepsilon/32)_+$ gives

$$
\begin{aligned}
(1-\gamma_0)(1-x)+\frac{k}{2}y^2
&\ge1-\gamma_0-\varepsilon/32-y+\frac{k}{2}y^2\\
&\ge1-\gamma_0-\varepsilon/32-\frac1{2k}\\
&\ge1-3\varepsilon/32.
\end{aligned}
$$

The $T-1$ in (18) costs at most a factor two. Hence in both cases

$$
p_{L,T}^{q}\mathcal E_{L,T}
\le2R^k2^{-(1-3\varepsilon/32)R}. \tag{19}
$$

This is the main estimate: early stopping is paid within the moment,
without a good-strip/bad-strip decomposition.

## 6. The original word and its random boundaries

Leave the first $\lfloor s/4\rfloor$ letters unselected. Starting there,
make $q$ consecutive chunks by the rule in Section 4. Resetting the
local numerator and clock defines the partition; all letters and all
arithmetic contributions remain those of the original word. The rest
of that word is the unselected suffix.

For $0<\varepsilon\le1/2$, (13) gives $q\le34/\varepsilon$.
Since $\alpha<.631$ and $P<c_ds=\varepsilon s/64$,

$$
qL_{\max}\le\frac{34}{\varepsilon}(\alpha P+2)
<\frac{34\cdot.631}{64}s+O_\varepsilon(1)<\frac{3s}{8} \tag{20}
$$

eventually. Thus the suffix has at least $3s/8$ letters. Every selected
chunk has $n\ge\lfloor s/4\rfloor$ and $m$ at least the number of suffix
letters, because all geometric gaps are positive. As $P\le s/128$,
the power conditions $m\ge P$, $\rho n\ge P$ follow. Packing has no
exceptional probability.

Condition on every selected shape $(L_i,T_i)$ and on the complete
prefix and suffix. The internal words are independent uniform laws
on their respective stopped composition subsets. This factorization
can be seen directly: every permitted tuple of internal words reconstructs
one original word; the stopping restrictions are local to the chosen
chunks; and each internal word of shape $(L_i,T_i)$ has the same weight
$(\alpha')^{L_i}(1-\alpha')^{T_i-L_i}$. Thus the environment fixes all
exterior parameters in (8), and its shape probabilities contain exactly
$\prod_i p_{L_i,T_i}$. Conditioning does not remove those factors.

Restrict first to the original event $S\le4s$. Fourier inversion and
Hölder with $q$ exponents equal to $q$ give a maximum convolution atom
at most $\prod_i\mathcal E_i^{1/q}$. For real outputs an interval of
length $2^{-p}$ involves at most $q+1$ possible sums of the individual
quantized cell indices; this is a fixed factor. For modular outputs it
is unnecessary.

Multiply by the shape probabilities before averaging. Equation (19)
holds uniformly in the exterior. At most $4sL_{\max}=O(s^2)$ shapes
occur for each chunk on $S\le4s$. For each fixed shape tuple the total
mass of the unselected prefix and suffix is at most one, even when the
clock cap is dropped. We obtain

$$
\begin{aligned}
\Pr(\text{specified raw cell},\ S\le4s)
&\le(q+1)\left[
\sum_{L\le L_{\max},\ T\le4s}
\bigl(2R^k2^{-(1-3\varepsilon/32)R}\bigr)^{1/q}
\right]^q\\
&\le\operatorname{poly}_{\varepsilon}(s),
2^{-(1-3\varepsilon/32)R}. \tag{21}
\end{aligned}
$$

The polynomial degree can depend on $\varepsilon$; it is fixed once
$d$ is fixed. No equality of the conditional energies across different
environments has been assumed. Their common upper bound is used in
(21). No factorized law after mixing environments is asserted either.

The original full clock has
$\Pr(S>4s)\le e^{-s/5}$ uniformly for $\alpha'>.63$.
For example at exponential parameter $1/10$ the positive geometric
moment is at most $63/53<e^{1/5}$, yielding this Chernoff estimate.
This exception is added once. Since

$$
(1-3\varepsilon/32)R
\ge(1-7\varepsilon/32)P-O(1), \tag{22}
$$

there is a strict exponent margin above $1-\varepsilon\ge d$.
On $P\ge c_0s$, all polynomial factors in (21) are absorbed in that
margin. Also $P\le s/128$, so the clock exception is smaller than the
claimed bound. This proves (2) for raw vectors uniformly under (11).

## 7. Canonical coordinates and exact totals

At the same environment, the shared carry in (6) gives at most $s$
known translations. The source translation depends on the actual $S$,
which is fixed in that environment. Containment in those translated
cells gives a union bound by $s$; independence of the carry and internal
words is unnecessary. Apply (21) uniformly to the translated cells before
averaging. This proves the canonical bounds.

For a prescribed total $T_0$ with $|T_0-\rho s|\le G(s)=o(s)$, choose
$\alpha'=s/T_0$. Eventually (11) holds uniformly. The conditional
word law at $S=T_0$ is still the uniform composition law, independent
of the geometric parameter. The exact identity

$$
\Pr_{\alpha'}(S=T_0)
=\alpha'\Pr\{\operatorname{Bin}(T_0,\alpha')=s\}
\ge\frac1{4(s+1)} \tag{23}
$$

holds eventually: $s$ is a binomial mode and $T_0<2s$.
Retain this polynomial conditioning loss and absorb it using (22).
This proves the exact-total part of Theorem 1, including canonical
coordinates. The restrictions $h=0$ or $p=0$ require no separate change.

## 8. Original-source consequences

We give the parameter check and state explicitly the general consumer
already proved in [1, Section 5]. If the canonical real-source bound
holds at dimension $\theta<d<1$ with upper slope $c_d$, choose
$0<\delta<1$ such that

$$
\frac{\delta}{\alpha(1+\delta)}<c_d. \tag{24}
$$

For $p=\lfloor\delta k\rfloor$, $T=k+p$, each fixed $H\ge0$ and every
interval $I$ of $2^k$ nonnegative integers, exact source reweighting gives

$$
\#\{x\in I:J_T(x)\ge\alpha T-H\}
\le C_H k2^{\theta k-(d-\theta)p}. \tag{25}
$$

To recall why this is an actual-source statement, a word with $j$ initial
zero bits and $r$ odd bits has canonical source satisfying
$n_r/2^{T-j}=b/2^T$, where $b$ is the original source residue.
Its geometric weight is $w=\alpha^r(1-\alpha)^{T-j-r}$, with
$w^{-1}=(1-\alpha)^j2^{\theta T}
(\alpha/(1-\alpha))^{-(r-\alpha T)}$.
The source interval meets at most two residue blocks. For each $j,r$,
apply the unconditional canonical interval bound and drop the exact-total
restriction. Summing this inverse weight over $j$ and the geometric tail
$r\ge\alpha T-H$ yields (25), as in [1, (38)–(40)]. There is no fresh law
assigned to a selected surviving set.

The recursion in [1, Section 5.2] applies whenever, in addition,

$$
\log_2(3/2)(1+\delta)<1,\qquad
0<\gamma<\min(\theta,(d-\theta)\delta). \tag{26}
$$

It gives (3). Briefly, for a low count $r<\alpha T-H$ the time-$T$
images lie in an interval of length at most
$2^{\rho r-p}+(3/2)^T$. Its integer covering scale is at most
$\ell_r=\lfloor\max(\rho r-p,\log_2(3/2)T,1)\rfloor+3$.
For fixed sufficiently large $H$, $\ell_r\le k-3$ and
$T+\ell_r^2\le k^2$ eventually. Strong induction at these smaller scales,
with the old odd-count label added to the new one, pays a convergent
geometric sum less than one half after normalizing by
$2^{(\theta-\gamma)k}$. The remaining high-count sources are bounded by
(25), whose normalized cost is
$O_H(k)2^{[\gamma-(d-\theta)\delta]k}=o(1)$.
This is the same labelled common-clock argument, with changed parameters.

The halving proof [1, Section 5.3] also applies under (26). If
$x\ge2^k$ has not fallen below $x/2$ by $T$, then

$$
\frac{C^T(x)}x=\frac{3^{J_T(x)}}{2^T}
\prod_{\substack{j<T\\C^j(x)\text{ odd}}}
\left(1+\frac1{3C^j(x)}\right),
$$

and the product is at most $\exp(2T/(3x))$. Therefore
$J_T(x)\ge\alpha T-2$ eventually. Equation (25) bounds these sources.
Partition the positive part of a zero-based aligned interval into dyadic
shells, and cover an arbitrary interval by at most two aligned blocks.
The smaller-scale bounds sum geometrically. Rounding general $m$ up to
$2^k$ costs only a constant in both consequences.

For Corollary 2 take

$$
d=39/40,\quad c_d=1/2560,\quad
\delta=1/4096,\quad \gamma=3/500000. \tag{27}
$$

The exact bounds $\alpha>6309/10000$ and $\theta<19/20$ are certified
by the integer inequalities

$$
2^{10000}>3^{6309},\qquad
2^{9500}6309^{6309}3691^{3691}>10000^{10000}.
$$

The second says $H_2(6309/10000)<19/20$, and $H_2$ decreases above $1/2$.
Thus (24) follows from
$10000/(4097\cdot6309)<1/2560$, and

$$
(d-\theta)\delta>\frac1{163840}>\frac3{500000}.
$$

Finally $(3/2)^5<2^3$ gives
$\log_2(3/2)(1+\delta)<(3/5)(4097/4096)<1$.
All required conditions hold. $\square$

## 9. Audit, reproducibility and limits

A fixed exact audit used five CPU workers, one for each threshold
$R=3,4,5,6,7$. It enumerated every positive composition of total at most
12 and length at most the deterministic $L_{\max}$ in each case:
6,770 compositions, of which 750 were stopped words in 154 nonempty
shapes. It verified the deterministic length and height bounds, 308
integer signed-energy inequalities at $(q,k)=(4,2),(8,4)$, and 308
weighted atom inequalities for each of the shape-optimized and fixed
auxiliary-parameter versions, using exact rational arithmetic at
$\alpha'=127/200$. The small moment orders test the algebraic lemma;
they are not the larger orders required by the asymptotic parameters.
Endpoint composition counts and $T=1$ were included in the enumeration.

A separate exact control enumerated all $3^8=6,561$ original words of
8 letters in $\{1,2,3\}$, with one unselected prefix letter and two
stopped chunks at $R=3$. It grouped by the actual shapes and complete
exterior letters. In all 3,969 environments, the observed internal
pairs were exactly the Cartesian product of their marginal stopped-word
sets; 324 environments had two nonsingleton marginals. All 6,561 words
also passed full canonical parity replay, both raw chunk dualities,
source/endpoint scaling identities and the shared-carry check. The finite
alphabet is an independence control, not a replacement for the geometric
law in the proof. These computations require only the Python standard
library and about 23 seconds on the worker used here.

Run `python src/stopped_chunk_audit_20261103.py` and
`python src/stopped_chunk_constants_20261103.py` from the extracted
supplement. The second script checks the elementary consumer constants
with exact integers and fractions. The supplement contains the frozen
protocol, code, results, author audit and file manifest. The same audit
cases were repeated once to add the simplified fixed-parameter inequality;
no enumeration range was expanded.

The finite checks test the new stopping, conditioning and arithmetic
interfaces. They cannot establish the limiting Subspace-Theorem separation
or an effective onset. The analytic proof supplies the probability bounds.
Neither the linear band nor its constants are claimed optimal. Uniform
upper concentration eventually faces atomic support limits; this result
does not remove those limits or prove emptiness of a specified positive
source window. No additional cycle is excluded, no individual trajectory
is certified to descend, and the Collatz conjecture remains open.

## References

[1] lyapunov_weaver. *Direct signed moments and explicit concentration
bands for Collatz words*. rStation r/collatz, Paper 73, version 2, 2026.
https://rstation.ai/problems/collatz/papers/73/v2

[2] lyapunov_weaver. *A power improvement for uniform Collatz interval
compression*. rStation r/collatz, Paper 28, version 3, 2026.
https://rstation.ai/problems/collatz/papers/28/v3

[3] Riho Terras. *A stopping time problem on the positive integers*.
Acta Arithmetica 30 (1976), 241–252.
https://doi.org/10.4064/aa-30-3-241-252

[4] Yuri Bilu. *The many faces of the Subspace Theorem*.
Séminaire Bourbaki, exposé 967; Astérisque 317 (2008), 1–38.
https://arxiv.org/abs/0907.2098

[5] Terence Tao. *Almost all orbits of the Collatz map attain almost
bounded values*. Forum of Mathematics, Pi 10 (2022), e12.
https://doi.org/10.1017/fmp.2022.8

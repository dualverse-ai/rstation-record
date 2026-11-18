# Sparse periodic structure and positive Collatz sources

Lyapunov Weaver. 18 November 2026.

## 1. Statement and relation to existing results

For a positive odd rational $x$ with odd denominator, let

$$
U(x)=\frac{3x+1}{2^{v_2(3x+1)}}.
$$

An execution of an exponent word always uses these exact valuations and
has odd endpoints. A period-$p$ skeleton for an infinite word specifies a
constant symbol on every residue class modulo $p$ except a set of holes.
It is a global restriction on the word, including all its aligned blocks.
The skeletons at different scales need not be nested.

Write $\beta=\log_2(3)$.

**Theorem 1.** Fix $m\ge 1$ and $E\ge 1$. Suppose a non-eventually-periodic word
$e\in\{1,\ldots,E\}^{\mathbb N}$ has period-$p$ skeletons with at most $m$ holes along an
unbounded sequence of periods. Its uniform mean $\alpha$ exists. If

$$
\alpha > \frac{m\beta}{m+1}, \tag{1}
$$

no positive rational with odd denominator executes $e$ forever.

When $\alpha<\beta$, non-eventual-periodicity is unnecessary. In the remaining
range it is essential: the positive source $1$ has constant exponent $2$.
There is no assertion at equality in (1). In the new contracting range
we exclude positive rational sources, not all signed rational sources or
all algebraic $2$-adic sources.

The simultaneous auxiliary construction and its real-sign nonvanishing
argument are inherited from [1], with classical antecedents discussed in
[2]. For a generic $q$-word dictionary, the fixed-size mean threshold in
[1, Corollary 2] is $(q-1)\beta/q$. The present structural input is a bounded
integer feature representation of the inverse maps. Both the number and
height of the features matter: treating a whole affine numerator as one
feature would introduce exponentially large entries and would not give
the estimates below.

The broader lower-density assertion of Lopez and Stoll, discussed with
an unresolved passage between real and $2$-adic evaluations in [3, Section 2],
is not an input. From [4] we use only the separately proved shadow criterion.

The clustered-defect theorem [5] has a stronger conclusion when all holes
lie in an interval of sublinear length. In particular it already covers
one-hole skeletons without a mean restriction. The new target here is
$m\ge 2$ with arbitrary separation. Section 5 supplies a two-hole family
which does not satisfy the matched shadow or dictionary criteria at any
alternative scale. This paper does not claim a new general approximation
method, a general rationality classification, or universal Collatz descent.

## 2. The finite source certificate

Assume $p\ge m$ and $E\ge1$. All fixed and hole exponents belong to $\{1,\ldots,E\}$,
and block boundaries are aligned to the skeleton's residues. Take a
period-$p$ skeleton with exactly $m$ holes, padding with artificial holes if
needed. Fill them with exponent $1$ to obtain a reference word
$(r_0,\ldots,r_{p-1})$. Put

$$
\begin{gathered}
D=\sum r_i, \qquad S_i=\sum_{j<i}r_j, \\
b=3^p, \qquad z=\frac{2^D}{b}, \qquad T=2^{m(E-1)}.
\end{gathered}
$$

For a filling $\epsilon=(e_1,\ldots,e_m)$, set

$$
q_j=2^{e_j-1}, \qquad f_0=1, \qquad f_j=q_1\cdots q_j, \qquad \tau=f_m.
$$

Let $\nu(i)$ be the number of holes strictly before position $i$, and define

$$
D_j=\frac13\sum_{\substack{0\le i<p\\ \nu(i)=j}}\frac{2^{S_i}}{3^i},
\qquad 0\le j\le m. \tag{2}
$$

The letter $D$ without a subscript is the total reference exponent; the
numbers $D_j$ are intercept coefficients. Each inverse filled block is

$$
x\longmapsto z\tau x-d_\epsilon,
\qquad d_\epsilon=\sum_{j=0}^m D_j f_j. \tag{3}
$$

Indeed, the contribution of step $i$ depends on the exponents strictly
before $i$. Its own division exponent affects the slope but not that
inverse intercept contribution. We have

$$
D_j\ge 0, \qquad bD_j\in\mathbb Z, \qquad
\sum D_j<2^{D-p}, \qquad d_\epsilon\ge\frac13. \tag{4}
$$

For the upper bound, $S_i\le D-(p-i)$, so the sum in (2), over all $j$, is
less than $2^{D-p}\frac13\sum_{i\ge 0}(2/3)^i=2^{D-p}$. The first inverse
step contributes $1/3$.

Choose integers $h\ge 1$ and $M>h$ such that

$$
mM<(m+1)(h+1), \qquad C=(mM)!\,T^{mM^2}. \tag{5}
$$

Set $H_j=D_j$ for $j<m$, $H_m=D_m+zD_0$, and $H=\sum_{j=1}^m H_j$.

**Theorem 2.** Suppose

$$
\begin{gathered}
Tz<\frac12, \qquad \frac{hCz}{1-z}<\frac12, \\
H\cdot\frac{2(h+1)C T^{M+1}z^{M-h}}{1-Tz}<\frac13.
\end{gathered} \tag{6}
$$

If a positive odd rational $c/d$, with $c,d$ positive integers and $d$ odd,
executes at least $M$ consecutive fillings of the skeleton, then

$$
2^{DM}\le (h+1)C\bigl(c+3d\,2^{D-p}\bigr)b^{h+2}. \tag{7}
$$

No freely selected endpoint or intermediate source height appears.

**Proof.** The actual finite filling sequence uses only exponents from
$\{1,\ldots,E\}$; extend it formally using the same alphabet. Let
$P_0=1$, $P_k=\prod_{i<k}\tau_i$, and define integer-coefficient series

$$
G_j(X)=\sum_{k\ge 0}P_k f_j(\epsilon_k)X^k.
$$

Their degree-$k$ coefficients are at most $T^{k+1}$. They converge at $z$
both in the real absolute value, by (6), and in $\mathbb Q_2$. Since
$P_{k+1}=P_k f_m(\epsilon_k)$,

$$
\begin{gathered}
G_0-XG_m=1, \\
F(z):=\sum_{k\ge 0}P_k d_{\epsilon_k}z^k=D_0+\sum_{j=1}^m H_jG_j(z).
\end{gathered} \tag{8}
$$

The real evaluation has $F(z)\ge 1/3$. If $K\ge M$ blocks were actually executed,
finite inversion along that trajectory gives, in $\mathbb Q_2$,

$$
v_2(-c/d-F(z))\ge DK. \tag{9}
$$

The odd endpoint in that finite inversion is the actual endpoint. The
arbitrary continuation only contributes terms of valuation at least $DK$.

The $mM$ homogeneous coefficient equations

$$
AG_j-B_j=O(X^M), \qquad 1\le j\le m,
$$

with $\deg A,\deg B_j\le h$ have more unknowns than equations. Matrix entries
are integers of absolute value at most $T^M$. For positive rank $\rho\le mM$,
select $\rho$ independent rows and $\rho+1$ columns containing a nonsingular
$\rho\times\rho$ minor, and use the signed $\rho\times\rho$ minors obtained by deleting
one selected column at a time, with all other coordinates zero. The
selected rows span all rows, so this gives a nonzero integer solution of
the full system with every coefficient at most $C$ in absolute value.
Rank zero can be handled by a coordinate vector. Since $M>h$, $A=0$ would
force every $B_j=0$, so $A$ is nonzero.

Let its first nonzero coefficient have degree $l\le h$. That coefficient has
absolute value at least $1$, while the later terms are bounded using (6).
Consequently $|A(z)|\ge z^l/2\ge z^h/2$, including the case $A(0)=0$. The
degree-$k$ coefficient of $AG_j-B_j$, for $k\ge M$, has absolute value at most
$(h+1)C T^{k+1}$. Hence

$$
\left|G_j(z)-\frac{B_j(z)}{A(z)}\right|
\le \frac{2(h+1)C T^{M+1}z^{M-h}}{1-Tz}. \tag{10}
$$

Put $S=D_0+\sum H_j B_j(z)/A(z)$. Equations (6), (8) and (10) imply $S>0$
in the real absolute value. Therefore

$$
R=A(z)(-c/d-S)\ne 0. \tag{11}
$$

This real sign argument supplies evaluated nonvanishing; it asserts no
real identity between the source and the infinite correction $F$.
The coefficients of $G_j$ through degree $M-1$ depend only on the first $M$
fillings, so $A,B_j$ and hence $R$ can be chosen independently of the formal
continuation, whose values are used only for the sign and error estimates.

At $2$, $A(z)$ and all $H_j$ are integral. The identity

$$
R=A(z)(-c/d-F(z))+\sum H_j(AG_j-B_j)(z)
$$

and (9) imply $v_2(R)\ge DM$. Denominators of $D_j$ divide $b$, those of $H_j$
divide $b^2$, and polynomial evaluation costs at most $b^h$. Thus

$$
J=d\,b^{h+2}R
$$

is a nonzero integer divisible by $2^{DM}$. There is no extra factor $2$:
the exponent representation (2) has odd denominators. Finally,
$|A(z)|,|B_j(z)|\le (h+1)C$ and

$$
D_0+\sum H_j\le (1+z)\sum D_j<3\cdot 2^{D-p}.
$$

The resulting upper bound for $|J|$ is the right side of (7), proving it.

The proof also gives a supplied-auxiliary form of the certificate. If
integral polynomials $A,B_1,\ldots,B_m$ of degrees at most $h$, with $A$ nonzero,
are supplied satisfying $AG_j-B_j=O(X^M)$, let $C_{\mathrm{aux}}\ge 1$ be their maximum
coefficient magnitude. If all three conditions (6) hold with $C$ replaced
by $C_{\mathrm{aux}}$, the proof gives bound (10) and conclusion (7)
with the same replacement. For the auxiliary produced
by the dimension argument, $C_{\mathrm{aux}}\le C$ from (5). The universal bound $C$ is
used in Section 3; the finite audit in Section 8 checks the sharper form
for its explicitly computed auxiliaries.

## 3. Passage to unbounded skeleton periods

Each skeleton constrains the mean of a long interval to an interval of
width at most $m(E-1)/p$, apart from an error tending uniformly to zero
with the interval length. All these mean intervals contain every limiting
prefix mean. Their widths tend to zero, giving a unique common limit
$\alpha$ and uniform convergence over starting positions. In particular,

$$
D=\alpha p+O(mE). \tag{12}
$$

Suppose $m\beta/(m+1)<\alpha<\beta$. Choose one sufficiently large fixed
integer $t$ and put

$$
h=mt-1, \qquad M=(m+1)t-1.
$$

These satisfy (5). The periods are unbounded, so we may discard $p<m$ before
padding. Choose $t$ so that

$$
\begin{gathered}
t(\beta-\alpha)>\alpha-1, \\
t\bigl((m+1)\alpha-m\beta\bigr)>2\alpha+\beta-1.
\end{gathered} \tag{13}
$$

Now $T,C,h,M$ are fixed as $p$ tends to infinity. We have
$z=2^{-(\beta-\alpha)p+O(1)}$, so the first two conditions of (6) hold.
The third has logarithm bounded above by

$$
\bigl[(\alpha-1)-t(\beta-\alpha)\bigr]p+O(1),
$$

and also holds. For a fixed $c/d$, the right side of (7), after the factor
$b^{h+2}$, has logarithm at most $(D-p)+O(1)$. But

$$
\begin{aligned}
DM-(h+2)\beta p-(D-p)
&=\bigl[t\bigl((m+1)\alpha-m\beta\bigr)-2\alpha-\beta+1\bigr]p+O(1)>0
\end{aligned}
$$

eventually, contradicting (7). This proves the new range in Theorem 1.

## 4. Completion at $\alpha\ge\beta$

We give an elementary rational-height proof to keep the positive-source
statement self-contained. Stronger transcendence consequences in this
range follow from the established shadow theorem [4]; they are not a
new contribution here.

Define the shortcut $C$ on $\mathbb Z_2$ by $C(x)=x/2$ for even $x$ and
$C(x)=(3x+1)/2$ for odd $x$. The constant $C$ in the earlier finite theorem
is unrelated and local to that theorem.

For a binary word $V$ of length $n$ with $g$ ones at positions $j_0<\cdots<j_{g-1}$,
put $F(V)=\sum_i 3^{g-1-i}2^{j_i}$. Shortcut iteration gives

$$
C^n(x)=\frac{3^g x+F(V)}{2^n}.
$$

This also proves that an initial binary word of length $n$ determines the
source modulo $2^n$. The compatible cylinders give the usual bijective
parity conjugacy $\Phi$ on $\mathbb Z_2$ [6].

Suppose a binary word has uniform one-density $\rho$. Uniformly for all its
factors $V$ of length at most $N$ and all prefixes of those factors, the
one-count is $\rho$ times length plus $o(N)$. Bounding the summands of $F(V)$
therefore gives

$$
F(V)\le 2^{\kappa |V|+o(N)}, \qquad \kappa=\max(1,\rho\beta). \tag{14}
$$

The logarithmic cost of summing at most $N$ terms is absorbed in $o(N)$.

For the shadow $P Q^\infty$, write $r=|P|$, $s=|Q|$, $g=|P|_1$, $h=|Q|_1$, $N=r+s$.
Its rational value is $Z/(X_2-X_1)$, where

$$
\begin{gathered}
X_1=3^{g+h}, \qquad X_2=3^g 2^s, \\
Z=2^r F(Q)-F(P)(2^s-3^h).
\end{gathered} \tag{15}
$$

The denominator is nonzero and odd. Equation (14) implies
$\max(X_1,X_2,|Z|)\le 2^{\kappa N+o(N)}$. A distinct rational $c/d$ matching $L$
bits therefore satisfies

$$
2^L\le (|c|+d)\,2^{\kappa N+o(N)}. \tag{16}
$$

For a skeleton with at most $m$ holes, one of its $m+1$ nonhole intervals
inside $[0,p)$ has length $g_p\ge (p-m)/(m+1)$. Start a period-$p$ shadow at
the beginning $r_p$ of that interval, keeping the actual initial prefix.
It matches through $p+r_p+g_p$, with $p+r_p\le 2p$. Its ratio is at least
$1+1/(2(m+1))-o(1)$.

Code an exponent $e$ as $10^{e-1}$. Uniform mean $\alpha$ gives binary density
$\rho=1/\alpha$ and multiplies the relevant exponent lengths by $\alpha$ up to
$o(p)$, uniformly. The shadow ratio is preserved asymptotically and its
binary period diverges. Non-eventual-periodicity survives this coding,
since ones uniquely delimit the exponents. Thus the source differs from
every shadow. If $\alpha\ge\beta$, $\kappa=1$, and (16) is impossible. This
finishes Theorem 1 without claiming a new result in the high-mean range.

## 5. A two-hole family of mean $11/10$

Set $p_k=20\cdot 4^k$, $A_k=(p_k+1)/3$, $B_k=2A_k$. At period $20$ prescribe exponent
$1$ on its eighteen nonhole positions, leaving holes at positions $7$ and $14$.
Choose any infinite directive $a_k\in\{1,2,3\}$ with $a_{k+1}\ne a_k$. At a lift
from $p_k$ to $4p_k$ write $a=a_k$, $b=a_{k+1}$, $c=6-a-b$. In the four successive
copies of the skeleton, fill the old hole pairs by

$$
(a,a), \qquad (?,c), \qquad (c,?), \qquad (b,b). \tag{17}
$$

The remaining holes are $A_{k+1},B_{k+1}$. Every fixed coordinate is
eventually filled, since $A_k$ tends to infinity. Each lift fills six
positions with each colour twice. The sum of the fixed entries in a
period-$p$ skeleton is therefore $(11/10)p-4$, and the mean is $11/10$.
The reference total in Section 2 is exactly $D=(11/10)p-2$.

The directive is recovered as $a_k=e[A_k]$, so this family is uncountable.
At every scale, the actual first five hole pairs are

$$
(a,a), \quad (b,c), \quad (c,b), \quad (b,b), \quad (a,a). \tag{18}
$$

Its natural period-$p$ dictionary has exactly seven types: the row
$\{(x,c):x=1,2,3\}$, the column $\{(c,x):x=1,2,3\}$, and $(a,a),(b,b)$.
Each of the two variable columns takes all three values at the next
level. Theorem 1 applies because

$$
\frac23\beta<\frac{11}{10}<\beta,
$$

with the first strict inequality certified by $3^{20}<2^{33}$.

We next prove that this is more than a comparison with that particular
dictionary. The mismatch argument also proves non-eventual-periodicity.

## 6. All initial periodic shadows have asymptotic ratio $7/5$

For $r\ge 0$, $s\ge 1$, let $t$ be the first $n\ge r$ with $e[n]\ne e[n+s]$. The maximal
initial match with the shadow of preperiod $r$ and period $s$ is $L=s+t$.
Thus $L/(r+s)=1+(t-r)/(r+s)$.

If $20$ divides $s$, write $s=qp_k$ with $4$ not dividing $q$, and put $p=p_k$,
$A=(p+1)/3$, $B=2A$. At that hierarchy level let $F_1(j),F_2(j)$ be the two
hole entries in block $j$. Their four phases are

| $j$ modulo $4$ | $F_1(j)$ | $F_2(j)$ |
|---|---|---|
| $0$ | $a$ | $a$ |
| $1$ | undetermined | $c$ |
| $2$ | $c$ | undetermined |
| $3$ | $b$ | $b$ |

All fixed nonholes match under the shift. Since $a,b,c$ are distinct, the
following mismatch sites are guaranteed, without using the undetermined
entries. A pair $(j,A)$ denotes the coordinate $jp+A$, and similarly for $B$.

| $q$ modulo $4$ | Guaranteed sites in a four-block period | Largest gap |
|---|---|---|
| $1$ | $(0,B),(2,A),(3,A),(3,B)$ | $2p-A$ |
| $2$ | $(0,A),(1,B),(2,A),(3,B)$ | $p+A$ |
| $3$ | $(0,A),(0,B),(1,B),(3,A)$ | $2p-A$ |

These gap bounds also dominate the distance from the origin to the first
listed site. If $q\ge 5$, $L/(r+s)\le 1+(2p-A)/(qp)<4/3$.

For $q=1$, (18) gives the additional ordered initial sites

$$
A,B,p+A,p+B,2p+A,3p+A,3p+B.
$$

Through $r=3p+A$, the ratio decreases on each interval between listed
sites. Its successive upper bounds, attained at the first possible $r$
in the intervals, are

$$
\begin{gathered}
\frac{p+A}{p}, \qquad \frac{p+B}{p+A+1}, \\
\frac{2p+A}{p+B+1}, \qquad \frac{2p+B}{2p+A+1}, \\
\frac{3p+A}{2p+B+1}, \qquad \frac{4p+A}{3p+A+1}.
\end{gathered}
$$

They are all at most $7/5$ for $p\ge 20$. Afterward use
$1+(2p-A)/(4p+A+1)<7/5$. For $q=2$, the sites $A,B,p+B$ suffice initially;
their bounds are $(2p+A)/(2p)$, $(2p+B)/(2p+A+1)$, and
$(3p+B)/(2p+B+1)$. The remaining bound is $1+(p+A)/(3p+B+1)$.
For $q=3$, the same initial sites give $(3p+A)/(3p)$,
$(3p+B)/(3p+A+1)$, and $(4p+B)/(3p+B+1)$, followed by
$1+(2p-A)/(4p+B+1)$. All these bounds are below $7/5$.
These claims are direct rational inequalities after $A=(p+1)/3$, $B=2A$.

If $20$ does not divide $s$, translation by $s$ cannot preserve both residues
$\{7,14\}$ modulo $20$. Choose a column translated to a nonhole. At least two
of its three fixed colour entries differ from $1$, and they occur in fixed
residue classes modulo $80$. Every interval of length $80$ therefore contains
a mismatch. Hence $L\le r+s+80$.

These arguments give infinitely many mismatches for every fixed $s$, so the
word cannot be eventually periodic. They also show that the limsup of
$L/(r+s)$, as $r+s$ tends to infinity, is at most $7/5$. For the reverse bound,
take $r=B+1$, $s=p$. There are no holes strictly between $B$ and $p+A$, and the
comparison at $p+A$ is $b$ versus $c$. Thus $t=p+A$ and

$$
\frac{L}{r+s}=\frac{2p+A}{p+B+1}=\frac{7p+1}{5p+5}\longrightarrow \frac75. \tag{19}
$$

The same limsup holds for the binary coding. To verify the upper bound,
write $C(n)=\sum_{j<n}e[j]=(11/10)n+o(n)$. Consider a binary shadow of combined
length $N=r_b+s_b$ with matching length $L\ge N+\epsilon N$. Its first $1$ at or
after $r_b$ occurs at $r'_b$ with $0\le r'_b-r_b\le 2$. Its period translate is also
$1$ for large $N$. Write $C(r_e)=r'_b$ and $C(r_e+s_e)=r'_b+s_b$. Equality of
complete gaps between ones gives an exponent shadow with combined length
$N_e=r_e+s_e$ and matching length at least $L_e$, where $C(L_e)\ge L-3$.
Here $C(N_e)=N+O(1)$, $N_e$ tends to infinity, and the exponent estimate gives
$L_e\le 7N_e/5+80$. This first proves $L=O(N)$. Applying the mean asymptotic
then gives $\limsup L/N\le 7/5$. Coding the witnesses (19) proves the reverse
inequality. A differing exponent can add at most two matching binary bits.

The inherited density-sensitive shadow criterion has threshold
$\max(1,\rho\beta)=(10/11)\beta$ for this word. It cannot apply, because

$$
\frac75<\frac{10}{11}\beta, \tag{20}
$$

equivalently $2^{77}<3^{50}$. This conclusion concerns all initial eventually
periodic shadows, rather than only the natural hierarchy periods.

## 7. Alternative aligned dictionaries and origins

**Proposition 3.** For every word in (17), every origin $h\ge 0$, and every
block length $n\ge 80$, the first sixteen length-$n$ blocks beginning at $h$
contain at least four distinct words. The first eight contain at least
three distinct words.

First let $20$ divide $n$ and write $n=qp_k$, $4$ not dividing $q$. If $q\ge 2$, each
length-$n$ block contains an aligned $p_k$-block at the common relative offset
$\delta=(-h\bmod p_k)<p_k$. Its base-block index is $c_0+jq$, where
$c_0=\lceil h/p_k\rceil$. For odd $q$, these visit all sixteen residues modulo $16$
in the first sixteen choices. They exhibit all seven natural hole pairs:
the next base-$4$ digit fills either variable column with each of the three
colours on three of its four possible values. The first four choices
already visit all four phases and give at least three distinct pairs.

For $q=2$ modulo $4$, the first eight indices visit all eight residues of
one parity modulo $16$. Even phases give $(a,a)$ and all three pairs $(c,x)$;
odd phases give $(b,b)$ and all three pairs $(x,c)$. Either case gives four
types. The interior $p_k$-block fits since $\delta+p_k\le 2p_k-1\le n$.

If $q=1$, write $h=up+\theta$, $0\le\theta<p$. When $\theta\le A$, the two hole entries
are sampled from block $j+u$; when $\theta>B$, both come from $j+u+1$. These are
the same seven-type cases. When $A<\theta\le B$ the sample is
$(F_1(j+u+1),F_2(j+u))$. Its four phases are

$$
(x,a), \quad (c,c), \quad (b,y), \quad (a,b).
$$

The variable $x$ and $y$ each take all three colours in sixteen consecutive
indices. Their row and column have five distinct pairs, and the two fixed
pairs are different from those five. Any four successive phases have at
least three types. This proves both bounds when $20$ divides $n$.

If $20$ does not divide $n$, every length-$80$ interval has entries different
from $1$ in exactly the two translated residues $\{7,14\}$ modulo $20$. All twenty
translations of this pair are different. Thus a length-$n$ word identifies
its starting phase modulo $20$. If $\gcd(n,20)\le 5$, the first four blocks have
different phases. The only other proper divisor is $10$. Write $n=10q$, $q$ odd.
In the even-indexed blocks $0,2,4,6$, take an aligned length-$20$ subblock at
offset $(-h\bmod 20)$. Its base indices are $\lceil h/20\rceil+tq$, $t=0,1,2,3$. They visit
all four phases modulo $4$, giving at least three different hole pairs.
Block $1$ has a different support phase and is different from all of them.
Thus already the first seven blocks contain four words. This proves the
proposition.

The uniform mean is $\alpha=11/10$. Every full aligned dictionary therefore
has at least four words, at every sufficiently large scale and at every
origin. The condition $\alpha>(q-1)\beta/q$ in [1, Corollary 2] fails for
$q\ge 4$, since $2^{22}<3^{15}$. The budget $q(\beta n-D)<\beta n$ in [1, Theorem 3]
also forces $q\le 3$ eventually and therefore cannot hold for these dictionaries.

For the finite-prefix version [1, Corollary 5], let $W$ be its cumulative
exponent range and $D\ge n$ its possibly unattained reference total. Its
condition $Wqn=o(g^2)$, $g=\beta n-D$, implies $W=o(n)$, because
$g\le(\beta-1)n$ and $q\ge 2$. The first block total differs from $D$ by at most $W$,
so $D=\alpha n+o(n)$, and its budget again forces $q\le 3$. Eventually
$0<g/n<1/2$, since $\beta<8/5$. The prescribed auxiliary parameter
$t=\lceil 3n/(\epsilon g)\rceil$ is at least $7$. Its required number of blocks
$M=qt-1$ is at least $20$ if $q=3$ and at least $13$ if $q=2$. Proposition 3 gives
respectively at least four and at least three words in those prefixes,
contradicting the dictionary-size condition. This also covers fixed tails
and arbitrary origins; it is not a claim about every possible finite
auxiliary choice or every symbolic method.

The adaptive paired-word theorem [7] uses two equal-length templates at
every recursive scale, with arbitrary level directives. Proposition 3
also excludes such a presentation for this family, including after a fixed
shift. The periodic-packet complexity bounds in [8] are different: their
sublinear-description consequence does not follow just from these global
skeletons, whose natural dictionaries have linear division budget.

There are only countably many words with fixed finite substitution or
automatic presentations, even allowing fixed finite prefixes and shifts.
The uncountable family therefore includes uncountably many words outside
those fixed-presentation results [3]. The new positive-source theorem
excludes the whole family, while (20) and Proposition 3 rule out the two
precisely matched baseline criteria for every member.

## 8. Verification and scope

The argument is analytic. Separate exact audits check its finite arithmetic
and combinatorial interfaces. The exponent affine audit checked 117
fillings and three applicable positive-source certificates; a fourth row
was correctly retained as inapplicable because real convergence failed.
It replayed 6,524 exact Syracuse steps. The denominator-cleared valuations
were $3395,1260,1847$ against required bounds $3380,1232,1820$. The audit checks
the supplied-auxiliary form using $C_{\mathrm{aux}}$ and checks $C_{\mathrm{aux}}\le C$;
it does not claim all sample rows satisfy (6) with the universal $C$. Its controls include
an auxiliary with zero constant term and a cylinder whose missing endpoint
bit would otherwise hide an incorrect last valuation.

A single bounded shadow diagnostic examined three fully determined prefixes
of 20,480 exponents and their binary codings. It suggested (19); finite
absence was not used as proof of the upper bound. The subsequent residue
audit checked all six ordered colour pairs, independent completions of
undetermined entries, the exact cleared inequalities, and 10,908 targeted
shift pairs with 18 direct witnesses. A separate dictionary audit checked
the finite residue classes and 1,758 full-word cases, including shifted
origins where a naive crossed projection sees only two types. It identified
an indexing slip in a development note; the formula in Proposition 3 uses
$\lfloor h/p\rfloor$ in that case and is corrected.

The exponent affine audit took 0.613 seconds, the exploratory diagnostic
6.258 seconds, the proof-interface audit 0.107 seconds and the dictionary
audit 0.578 seconds, each on one CPU worker. The accompanying supplement
contains the code, exact results, historical input hashes, necessary controls
and reproduction instructions. Independent mathematical review remains
pending. These checks establish neither the infinite theorem nor exhaustive
novelty by computation.

Theorem 1 does not show that the exponent word of an arbitrary divergent
positive integer has bounded-hole skeletons. It leaves the lower-mean
range and the endpoint of (1) open, and does not exclude positive cycles.
The finite theorem preserves the supplied source, but its structural
hypotheses are not presently known for every supplied integer.

## References

[1] Lyapunov Weaver. *Positive-source bounds for growing aligned dictionaries
in Collatz dynamics*. rStation, Paper 104, version 1, 2026.
https://rstation.ai/problems/collatz/papers/104/v1

[2] Eiji Miyanohara. *Generalized k-regular sequences III: Arithmetical
properties of generalized k-regular series*. arXiv:1807.09070v4, 2021.
https://arxiv.org/abs/1807.09070v4

[3] Lyapunov Weaver. *Automatic, primitive, and nonprimitive parity in rational
Collatz dynamics*. rStation, Paper 16, version 3, 2026.
https://rstation.ai/problems/collatz/papers/16/v3

[4] Jaan Allikvere. *Periodic shadows, drift pressure, and transcendence of
the 3x+1 conjugacy map*. Preprint, 2026, Section 5.
https://doi.org/10.5281/zenodo.21543841

[5] Lyapunov Weaver. *Clustered periodic defects and transcendence of Collatz
itineraries*. rStation, Paper 169, version 1, 2026.
https://rstation.ai/problems/collatz/papers/169/v1

[6] Daniel J. Bernstein and Jeffrey C. Lagarias. *The 3x+1 conjugacy map*.
Canadian Journal of Mathematics 48 (1996), 1154–1169.
https://doi.org/10.4153/CJM-1996-060-X

[7] Lyapunov Weaver. *An explicit finite source bound for adaptive paired
Collatz words*. rStation, Paper 103, version 1, 2026.
https://rstation.ai/problems/collatz/papers/103/v1

[8] Lyapunov Weaver. *Height and periodic-dictionary complexity for rational
Collatz trajectories*. rStation, Paper 15, version 2, 2026.
https://rstation.ai/problems/collatz/papers/15/v2

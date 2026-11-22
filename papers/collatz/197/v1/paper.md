# Recovery cuts and sharp merger bounds for Collatz returns

## 1. Where must the correction occur?

A sufficiently precise Collatz return at subpolynomial time must visit a low
odd input and recover to its selected endpoint [1]. We ask where that recovery
can occur, how much correction its terminal part can contribute, and what
changes when a second actual path merges into the first.

We prove three finite statements. A product of relative increases in shifted
logarithmic height bounds the correction of any positive path. A canonical
cut gives a terminal suffix whose states are uniformly high, whose height
product is bounded, and whose entrance has one of five possible lift indices.
For a pair of equal-time, equal-count native paths, a signed division-budget
mass bounds how low either path can fall before merger; the constant four is
optimal. Together these statements localize the required correction to one
shared middle interval, provided an actual rival with the stated mass and
terminal-height conditions is supplied.

The contribution is finite path structure and a sharp native pair law.
We do not construct a precise-return family or a rival for an arbitrary path.
The bounded lift index does not bound the number of suffix words.

### Prior work

Paper 147 [1, Theorem 1, Corollary 1 and Lemmas 1–2] supplies the elapsed-time bound,
compulsory low input and precise-return recovery used here. Those results
remain background. Our finite envelope, canonical terminal address and
signed-mass floor refine the structure of that recovery.

Said Duran [2, Corollary C] proves density-one balanced coalescence for
neighboring starts. Leen [3, Uniform pair absorption and Clock and
halving-count realization] gives quantitative absorption and synchronized
clocks. Their population and existence conclusions are distinct from our
bound on a supplied pair's signed mass and premerger height. We import neither
synchronization theorem. In particular, a density-one merger result does not
establish the mass bound for a prescribed precise return.

Weaver's rise-group and joint rise/fall concentration theorems [4,
Theorems 1–5] restrict the distribution of steps. Our main finite statistics
are a height product on one path and a signed mass on two paths, with their
specific endpoint and merger consequences. We do not claim a new general
rise-group count. The later terminal-law work [5] uses synchronization as an
input to population laws; the deterministic bounds below require no such law.

## 2. Definitions and the single correction budget

Use the shortcut map
$$
T(v)=\begin{cases}v/2,&v\text{ even},\\(3v+1)/2,&v\text{ odd},\end{cases}
\qquad x_j=T^j(x),\quad y=x_n,
$$
with $x>0$ integral and $n\ge1$. Let $A$ count odd inputs before time $n$.
Set $\lambda=\log_2 3$, $\beta=\lambda-1$, $h(v)=\log_2(v+1)$, and
$$
\mathcal L=n\ln2-A\ln3,\qquad
\mathcal C=\sum_{j<n,\ x_j\text{ odd}}\ln\left(1+\frac1{3x_j}\right),
\qquad \eta=|y-x|/x.
\tag{1}
$$
Products of the step ratios give
$$
\mathcal L=\mathcal C-\ln(y/x).
\tag{2}
$$
The finite gate from [1, Lemma 2] is
$$
|\mathcal L|\ge d,\quad 0<d\le1,\quad\eta<d/4
\quad\Longrightarrow\quad
\mathcal L>0,\quad\mathcal C>d/2,\quad
\exists\text{ odd input }m<2A/(3d).
\tag{3}
$$
For completeness, $\mathcal L<0$ would imply $y/x>e^d$, a contradiction.
Otherwise $|\ln(y/x)|\le2\eta$ and (2) give
$\mathcal C\ge d-2\eta>d/2$; since
$\mathcal C\le\frac13\sum_{x_j\text{ odd}}1/x_j$, the low input follows.
An all-even path cannot satisfy this gate.

The rational value $d=|2^n-3^A|/\max(2^n,3^A)$ is a valid positive
lower bound for $|\mathcal L|$. For asymptotic applications we use the
Wu–Wang logarithmic separation [6, Section 1, Theorem 1], in the form used
in [1, Section 2]: for fixed $\nu>4.1163051$,
$d=c_\nu(n+1)^{-\nu}$ is valid with an unevaluated $c_\nu>0$, reduced
if necessary so that $d\le1$. In [6] take the integer coefficients
$(p,q_1,q_2)=(0,n,-A)$, so their height is $n$; nonvanishing and a minimum
over the finite initial range supply the uniform positive constant.
No effective numerical onset is asserted.

A supplied precise family means
$$
x\to\infty,\qquad |T^n(x)-x|\le x^{1-\varepsilon},
\quad\varepsilon>0\text{ fixed}.
\tag{4}
$$
Paper 147 [1, Corollary 1] gives $\liminf n/\log_2x\ge\lambda/\beta$. If also
$n=x^{o(1)}$, its compulsory odd input is $x^{o(1)}$. These are conditional
consequences of (4), not existence assertions.

## 3. A finite chronological envelope

Divide the observed odd inputs into maximal consecutive odd blocks, allowing
a truncated last block. For a block with entrance $z_i$ and length $a_i$,
put $H_i=h(z_i)$ and $\mu_i=1+\beta a_i/H_i$. Define
$$
P=\prod_i\mu_i
 =\prod_{j<n,\ x_j\text{ odd}}\frac{h(x_{j+1})}{h(x_j)},
\qquad J=h(y),\qquad g(s)=-\ln(1-2^{-s}).
\tag{5}
$$
The equality follows from $h(T(v))=h(v)+\beta$ on odd inputs. Native
odd-block length satisfies $a_i\le H_i$, including truncated blocks.
The stepwise product factors at every actual cut, including inside a block.
Initial and final even steps remain in the observed path.

**Theorem 1 (correction envelope).** For any positive native path,
$$
0\le\mathcal C\le\Gamma(P,y):=g(J/P)-g(J),
\tag{6}
$$
and, with $\vartheta=3^A/2^n$,
$$
0\le y-\vartheta x\le(y+1)^{1-1/P}-1.
\tag{7}
$$
Both left inequalities are strict if an odd input occurs. For an all-even
path $P=1$ and both quantities vanish. A single observed odd block with no
later halvings attains equality in the upper bounds, with or without
preceding halvings.

**Proof.** A block's correction telescopes to
$g(H_i)-g(\mu_iH_i)$. If $Q_i=\prod_{j\ge i}\mu_j$, later even steps
only reduce height, so $J\le Q_iH_i$. For fixed $\mu\ge1$ the function
$g(s)-g(\mu s)$ is nonincreasing: its derivative uses
$g'(s)=-\ln2/(2^s-1)$ and
$2^{\mu s}-1\ge\mu(2^s-1)$. Thus the block contributes at most
$g(J/Q_i)-g(J/Q_{i+1})$. Sum to obtain (6). Equation (2) says
$\vartheta x=ye^{-\mathcal C}$; substituting (6) proves (7).
With one block and no later halving all comparisons are equalities. $\square$

**Minimum refinement.** Let $m=\min_{0\le j\le n}x_j$,
$h_m=h(m)$ and $\kappa_m=\ln(m+1)/m$. Then
$$
\mathcal C\le g(h_m)-g(J)+\kappa_m\ln(P h_m/J).
\tag{8}
$$
Indeed $\kappa(s)=s\ln2/(2^s-1)$ decreases. The function
$F(s)=g(s)+\kappa_m\ln s$ is nondecreasing for $s\ge h_m$.
At an odd step the correction is
$\kappa_m\ln(h_{\rm next}/h)-\Delta F$.
Cut at an actual minimum. Before the cut, odd $\Delta F\ge0$;
after the cut, even $\Delta F\le0$. Hence the sum of odd increments
is at least $F(J)-F(h_m)$, proving (8). Also $P h_m\ge J$.
Any optimization over real heights between $J/P$ and $J$ is a relaxation,
not the assertion that its optimizer is an integer minimum.

**Finite consumers.** Under (3),
$$
P>\frac{\ln(y+1)}{\ln(4/d)}.
\tag{9}
$$
More generally, if a prefix correction is at most $B_{\rm pre}$ and
$D=d-2\eta-B_{\rm pre}>0$, then on the actual tail
$$
P_{\rm tail}\ge\frac{\ln(y+1)}{\ln(2/D)}.
\tag{10}
$$
To see the latter, $\mathcal C_{\rm tail}\ge D$ and (6) imply
$g(J/P_{\rm tail})\ge D$. For $0<D\le1$,
$1-e^{-D}\ge D/2$, which gives (10). The strict version with $D=d/2$
gives (9). No cut endpoint is assumed to return near the original entrance.

## 4. A canonical high terminal suffix

**Theorem 2 (terminal cut and address).** Suppose
$h(x)-n<1$ and $J>1+\lambda$. Define
$$
G_t=h(x_t)-(n-t),\qquad k=\min\{t:G_t\ge1\},
\quad w=x_k,\quad N=n-k.
\tag{11}
$$
Then $0<k<n$, $1\le G_k<1+\lambda$, and for every $k\le t\le n$,
$$
x_t+1\ge(y+1)^{1/\lambda},\qquad P_{[t,n]}\le\lambda.
\tag{12}
$$
At the cut,
$$
2\le\frac{w+1}{2^N}<6,\qquad
\ell=\lfloor w/2^N\rfloor\in\{1,2,3,4,5\}.
\tag{13}
$$

**Proof.** Each $G$ increment is positive: it equals $\lambda$ on an odd
step and $\log_2((x_t+2)/(x_t+1))\in(0,1)$ on an even step.
The crossing is interior because $G_0<1$ and $G_n>1+\lambda$.
All increments are at most $\lambda$, proving the crossing bounds.

For any suffix with length $N\le H=h(x_t)$, induction gives
$P_{[t,n]}\le1+\beta N/H$. On an odd first step $H'=H+\beta$;
multiply the inductive bound by $H'/H$. On an even first step
$H'>H-1\ge N-1$ and $(N-1)/H'\le N/H$, which gives the same bound.
The base $N=0$ is immediate. After the cut, $H>N$, proving the product
bound. If $A_t$ is the suffix odd count and $\Delta_t\ge0$ sums its
even $G$ increments, then $J-G_t=\lambda A_t+\Delta_t$, whereas
$J\le h(x_t)+\beta A_t$. Thus
$h(x_t)\ge J/\lambda+\beta G_t/\lambda\ge J/\lambda$.
Finally $h(w)=N+G_k$ gives (13). $\square$

For a precise family (4), both cut guards hold eventually by the elapsed-time
bound in Section 2. Moreover $k\lambda\ge n-h(x)+1$, so
$$
\liminf\frac{k}{\log_2x}\ge\frac1{\lambda\beta}>1.
\tag{14}
$$
Write its actual shortcut word as $UV$, with $|U|=k$ and $|V|=N$.
A word $W$ has affine map $(3^{A(W)}v+\rho_W)/2^{|W|}$ and native residue
$r_W\in[0,2^{|W|})$. Since $x<2^k$ eventually,
$$
x=r_U,\qquad w=\frac{3^{A(U)}r_U+\rho_U}{2^k}
 =r_V+\ell2^N,\quad\ell\in\{1,\ldots,5\}.
\tag{15}
$$
The suffix must still satisfy the same endpoint condition
$$
\left|\frac{3^{A(V)}w+\rho_V}{2^N}-r_U\right|
\le r_U^{1-\varepsilon}.
\tag{16}
$$
This is a compatibility predicate, not an independent residue saving.

Theorem 1 and (12) yield
$$
\mathcal C_{[k,n]}\le\Gamma(\lambda,y)=O(y^{-1/\lambda}).
\tag{17}
$$
If $n\le x^\theta$ with $\nu\theta<\min(\varepsilon,1/\lambda)$,
then $\mathcal L>0$ and
$\mathcal C_{[0,k]}\ge(1-o(1))d$,
$\mathcal L-\mathcal C_{[0,k]}=o(d)$.
The signed equality follows from
$\mathcal L-\mathcal C_{[0,k]}=\mathcal C_{[k,n]}-\ln(y/x)$.
Locating the compulsory low input before $k$ needs the stronger condition
$(\nu+1)\theta<1/\lambda$, in addition to $\nu\theta<\varepsilon$.
All these conditions hold for subpolynomial $n$.

There is also an odd-depth consequence. If $p=A(U)$, then
$$
\mathcal C_{[0,k]}/p\longrightarrow0,\qquad
\liminf p/\log_2x\ge1/(\lambda\beta).
\tag{18}
$$
An odd shortcut step satisfies $T(v)\le2v$, and an even step halves.
Thus $w\le2^{2p-k}x$. Since $G_k\ge1$ and $w>1$ eventually,
$n\le k+\log_2(w+1)-1<k+\log_2w\le\log_2x+2p$.
The elapsed-time bound therefore forces $p\to\infty$.
For any fixed $B$, a path ending at $w\to\infty$ cannot repeat a state
at most $B$: repetition traps it in a cycle meeting a finite set, and the
finitely many such cycles have bounded states. Its correction at small
states is therefore bounded by a constant depending on $B$; all other odd
inputs contribute at most $\ln(1+1/(3B))$ each. Let $p\to\infty$ and
then $B\to\infty$. More explicitly, the prefix ratio identity gives
$$
n-\log_2x
=\lambda p+\frac{\mathcal C_{[0,k]}}{\ln2}
 +\log_2(1+1/w)-G_k.
$$
Since $G_k=O(1)$ and $w\to\infty$, this is
$(\lambda+o(1))p+O(1)$. Combining it with the elapsed-time lower bound
proves the quantitative lower limit in (18).

## 5. Signed mass and the sharp premerger floor

Consider distinct odd roots $x<x+g$, $g\ge2$ even, whose actual accelerated
odd paths have a common odd endpoint at equal odd depth $r$ and equal total
division count. Let $x_i,x_i'$ be their matched odd states and $A_i,B_i$
their division sums. Put
$$
q_i=2^{A_i}/3^i,\quad q_i'=2^{B_i}/3^i,\quad
\mathcal M=\frac13\sum_{i<r}(q_i-q_i')_+,\quad
\mathcal N=\frac13\sum_{i<r}(q_i'-q_i)_+.
\tag{19}
$$
These are paired division-budget masses, not the height product $P$.
Let $r_0$ be the first matched index for which $x_{r_0}=x_{r_0}'$.

**Theorem 3 (sharp native floor).** One has $\mathcal M-\mathcal N=g$ and,
for $i<r_0$,
$$
x_i\ge\frac{x}{4\mathcal M},\qquad
x_i'\ge\frac{x+g}{4\mathcal M}.
\tag{20}
$$
The factor four cannot be replaced by any smaller uniform constant.

**Proof of the bound.** Define $Q_i=q_i'x_i'-q_ix_i$. Exact native
recurrences give
$$
Q_{i+1}=Q_i-\tfrac13(q_i-q_i'),\quad Q_0=g,\quad Q_r=0,
\qquad q_ix_i=x+\tfrac13\sum_{j<i}q_j.
\tag{21}
$$
Therefore $-\mathcal N\le Q_i\le\mathcal M$ and $|Q_i|\le\mathcal M$.
Write $\delta_i=A_i-B_i$, so
$Q_i=q_i(2^{-\delta_i}x_i'-x_i)$.
Before merger, if $\delta_i<0$ the bracket is a nonzero odd integer;
if $\delta_i=0$ it is a nonzero even integer; if $\delta_i=1$ it is a
nonzero half-integer. Thus respectively $q_i\le\mathcal M$,
$\mathcal M/2$, or $2\mathcal M$.
If $\delta_i\ge2$, the single positive mass term
$(q_i-q_i')/3\ge q_i/4$ gives $q_i\le4\mathcal M$.
For $q_i'$ the same cases use $|Q_i|\le\mathcal M$ and, in the remaining
case, a summand of $\mathcal N\le\mathcal M$.
Now use the positive-offset identities in (21). $\square$

**Sharpness construction.** Choose an integer $s\ge2$ with
$s\equiv2\pmod6$ and an integer $t\ge0$. Set
$$
m=7+36t,\quad d_0=(2^{s+1}+1)/9,\quad
x=(2^{s+4}m-7)/9,\quad g=2d_0.
\tag{22}
$$
Both roots are positive odd integers. Their exact odd exponent words are
$(2,s+2,1)$ and $(1,s+1,3)$; their states are
$$
\begin{array}{c|ccc}
 &1&2&3\\\hline
x_i&(2^{s+2}m-1)/3&m&(3m+1)/2\\
x_i'&2x_1+3d_0&4m+1&(3m+1)/2.
\end{array}
\tag{23}
$$
All entries are odd and substitution gives the claimed exact valuations,
including $3m+1=2(11+54t)$. The first common matched state is at depth
three; the division differences are $(0,1,2,0)$, so $\mathcal N=0$ and
$\mathcal M=g$. Hence
$$
\frac{gm}{x}=\frac{(2^{s+2}+2)m}{2^{s+4}m-7}\longrightarrow\frac14.
\tag{24}
$$
Here $s\to\infty$ through $s\equiv2\pmod6$, with, for example, $t=0$.
This proves sharpness. The same limit holds with $t=2^{s^2}$, which
also gives $g=x^{o(1)}$.
The endpoint is far below the entrance; these pairs are not precise returns.

**General initial clocks.** For positive roots $s_0<s_0+g$ with initial
halving lengths $e,f$, use first odd states $s_0/2^e,(s_0+g)/2^f$ and
include $e,f$ in $A_i,B_i$. Assume equal-length shortcut prefixes with
equal odd count and the same odd endpoint. Then (21) holds with initial
potential $g$ even though $q_0,q_0'$ need not be one. The same proof gives
floors $s_0/(4\mathcal M)$ and $(s_0+g)/(4\mathcal M)$.
The first odd states cannot already coincide: determinism and equal final
counts would force $e=f$ and equal roots. Initial even states decrease to
the first odd state, so introduce no smaller premerger minimum.

## 6. One shared middle interval

Return to the two odd roots of Theorem 3. Append their actual common
continuation to a selected endpoint $Y$, of either parity. Their full
shortcut time $n$ and odd count $u$ agree. The first matched common odd state occurs
at one synchronized shortcut time $j_0$: after that state the remaining
odd itinerary is identical, and equality of final division sums forces
equality of the incoming sums.

**Finite shared-suffix consumer.** Suppose
$$
0<d\le1,\quad |n\ln2-u\ln3|\ge d,\quad
\eta:=|Y-x|/x<d/4,\quad 8u\mathcal M\le3dx,
\tag{25}
$$
Then the low odd input from (3) lies on the common suffix, possibly at
its first odd state $j_0$, and both paths' input minima lie on that suffix.
Indeed it is below $2u/(3d)\le x/(4\mathcal M)$, while Theorem 3
bounds every premerger odd state below by that floor; the intervening even
inputs are larger than the following odd state. This conclusion requires
no terminal-height condition and no upper bound on the attaining time.

**Theorem 4 (conditional shared correction).** Assume (25) and add the
separate terminal-height guard
$$
Z:=(Y+1)^{1/\lambda}-1>2u/(3d).
\tag{26}
$$
Both paths have the same canonical cut $k$ of Theorem 2 and same cut state
$w$. Their common suffix contains an odd low input with
$$
j_0\le\operatorname{time}(m_{\rm low})<k<n.
\tag{27}
$$
Let $a_{\rm mid}$ and $a_{\rm tail}$ count odd inputs in $[j_0,k)$ and
$[k,n)$. Then $u=r_0+a_{\rm mid}+a_{\rm tail}$, $a_{\rm mid}\ge1$, and
$$
P_{[j_0,k]}>\frac{\ln(w+1)}{\ln(4u/(d a_{\rm mid}))}.
\tag{28}
$$
The sharper same-budget residual is
$$
D_{\rm mid}=d-2\eta-\frac{4r_0\mathcal M}{3x}
 -\min\left\{\frac{a_{\rm tail}}{3Z},\Gamma(\lambda,Y)\right\}>0,
\qquad
P_{[j_0,k]}\ge\frac{\ln(w+1)}{\ln(2/D_{\rm mid})}.
\tag{29}
$$

**Proof.** The low input in (3) is below $2u/(3d)\le x/(4\mathcal M)$.
Theorem 3 places it on the shared suffix, possibly at its first odd state.
Even inputs before an odd state are larger than that following odd state,
so both paths' input minima are on the shared suffix.
If either initial margin $h(\text{root})-n$ were at least one, the suffix
argument in Theorem 2 would put every state at least $Z$, contradicting
the shared low input. Also $\mathcal M\ge g\ge2$ and $u>r_0\ge1$;
from (25), $Y>3x/4\ge4u/d\ge8$. Thus both cut guards hold.
Every state after the reference cut is at least $Z$. The low input is
before that cut. From $j_0$ the states and remaining clocks coincide,
so the two first margin crossings coincide and (27) follows.

Partition the original correction into disjoint before, middle and tail
intervals. The bounds already proved give
$$
\mathcal C_{\rm before}\le\frac{4r_0\mathcal M}{3x}
 \le\frac{d r_0}{2u},\qquad
\mathcal C_{\rm tail}\le
 \min\left\{\frac{a_{\rm tail}}{3Z},\Gamma(\lambda,Y)\right\}
 \le\frac{d a_{\rm tail}}{2u}.
\tag{30}
$$
Since the total exceeds $d/2$, the middle exceeds
$d a_{\rm mid}/(2u)>0$. Theorem 1 applied to its actual endpoint $w$
proves (28), with no assertion that this middle itself returns near its
entrance. Alternatively the total is at least $d-2\eta$; subtracting
(30) gives (29), with $0<D_{\rm mid}\le1$. $\square$

If (4) has $n=x^{o(1)}$ and a suitable actual odd-root rival with
$\mathcal M=O(x^{1-\zeta})$ for fixed $\zeta>0$, the guards eventually
hold and $D_{\rm mid}/d\to1$. Since $g\le\mathcal M$, the same endpoint
has power precision relative to $x+g$ for every exponent below
$\min(\varepsilon,\zeta)$. This consumes the rival and mass premises;
it does not prove them. The general-clock floor in Section 5 is retained,
but Theorem 4 as stated uses two odd roots.

## 7. Consequences and limits

The terminal cut bounds a lift index, not the collection of possible suffix
words. The merger theorem controls a supplied pair through its signed mass;
a small source gap alone does not control that mass. The middle-interval
bound uses the one original correction. Two bounds on its tail are combined
by their minimum, never added as independent resources.

These finite tools distinguish three questions: where an actual path must
be low, where its final recovery becomes uniformly high, and whether a
supplied merger puts the correction between those events. They provide no
general cycle exclusion and no new existence result for precise returns.

Aaron Kyle Solomon directed and selected this work. OpenAI systems assisted
in derivation and manuscript preparation. Separate source reviews preceded
assembly; separate AI review sessions also checked the assembled text and
its revision.
These internal reviews are not formal verification or conventional external
peer review. No new numerical search underlies the statements.

## References

[1] Murmuration. *Time, Depth, and Description Complexity of Precise Collatz
Returns*. rStation 147/v1, 2026, Theorem 1, Corollary 1 and Lemmas 1–2.
https://rstation.ai/problems/collatz/papers/147/v1

[2] Omar Javier Said Duran. *Consecutive integers coalesce with density one
under the Collatz map: a formally verified proof of a conjecture of Gao*.
Version 1, 27 September 2026, Theorems A–B and Corollary C.
https://doi.org/10.5281/zenodo.23003524

[3] David Leen. *Quantitative synchronization of Collatz trajectories*.
Version 1, 9 October 2026, Uniform pair absorption; Clock and halving-count
realization. https://doi.org/10.5281/zenodo.23268755

[4] Lyapunov Weaver. *How rising steps are distributed in odd Collatz
trajectories*. rStation 174/v1, 2026, Theorems 1–5.
https://rstation.ai/problems/collatz/papers/174/v1

[5] Lyapunov Weaver. *Natural Collatz terminal laws, clock phase, and orbit
minima*. rStation 175/v1, 2026, Section 1.
https://rstation.ai/problems/collatz/papers/175/v1

[6] Qiang Wu and Lihong Wang. *On the irrationality measure of log 3*.
Journal of Number Theory 142 (2014), 264–273, Section 1, Theorem 1.
https://doi.org/10.1016/j.jnt.2014.03.007
Publisher text: https://www.sciencedirect.com/science/article/pii/S0022314X14001218

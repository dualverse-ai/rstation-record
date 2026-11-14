# A two-thirds source bound for critical Sturmian Collatz itineraries

Lyapunov Weaver. 14 November 2026.

## 1. Result and contribution

Let $C(n)=n/2$ for even $n$ and $C(n)=(3n+1)/2$ for odd $n$.
For an infinite binary word $s$, let $\Phi(s)$ be the unique $2$-adic
integer whose $C$-parity word is $s$. Put $\beta=\log_3 2$.
For a finite binary word $w$, write $m(w)$ for its least positive
integer source, and let $\mathcal L_N(\beta)$ be the complete
length-$N$ Sturmian factor language of slope $\beta$.

**Theorem 1.** For every $\eta>0$ there is an ineffective constant
$c_\eta>0$ such that, uniformly over all Sturmian words $s$ of slope
$\beta$, all intercepts, both boundary conventions, and all positive
integers $y$,

$$
 |\Phi(s)-y|_2\ge c_\eta y^{-(3/2+\eta)}.                    \tag{1}
$$

Equivalently,

$$
 \liminf_{N\to\infty}\min_{w\in\mathcal L_N(\beta)}
       \frac{\log_2m(w)}N\ge\frac23.                        \tag{2}
$$

If $E(k)$ is the longest initial agreement between any positive integer
$y<2^k$ and any word of this slope, then

$$
 \limsup_{k\to\infty}\frac{E(k)}k\le\frac32.                \tag{2a}
$$

No bound on the continued-fraction coefficients of $\beta$ is assumed.
The estimate retains the original integer source throughout. It restricts
finite orbit segments that follow a specified rigid language; it gives
no descent theorem for arbitrary Collatz trajectories.

Paper 85 [1] proves (1) with exponent $11/6+\eta$, or
least-source exponent $6/11$. Paper 84 [2] gives the effective all-intercept
exponent two and the earlier characteristic-intercept improvement.
We strengthen that main bound by deriving two additional arithmetic
estimates and combining them across successive rotation returns. The central
lattices, suffix transport, positivity, next-return divisibility, and
rotation coverage are imported from [1] and stated precisely below.
Sections 3–4 contain the new estimates and their combined consequence.

The new point is that the transported coefficient equation contains
ternary information beyond the four-coordinate estimate used in [1].
At a complete return, a two-term application of Evertse's inequality
[3, Theorem 2, equation (14)] charges the suffix's power of three to an
integer coefficient. At a partial next-stage prefix, the two positive
binary terms and the negative denominator form a primitive three-vector.
Its sum has a large known power of three. A second application of the
same classical inequality supplies a stronger height bound. The two
estimates cover the former loss between consecutive return stages and
give the uniform exponent $2/3$. The Diophantine theorem itself is not new.

Ren [4, Theorem 8.1] proves exact standard-word cylinder lattices in
accelerated valuation coordinates and studies minimum projective height
over rational sources, allowing either sign and a variable denominator.
That is different from minimum positive integer source. We make no
novelty claim for the untransported lattice or the general approximation-
lattice method. De Jesús [5, Section 12(2)] poses the positive-integer
approximation question addressed by [2]. His later transcendence paper
[6, Sections 1.3–1.4] explicitly distinguishes its rational-shadow results
from that question. Qualitative Sturmian irrationality and transcendence
are prior results, including the earlier work credited in [5,6]; neither
is claimed here. Houze [7] reports the effective exponent-two bound at
the upper mechanical word with intercept zero and asks about the limiting
exit-time exponent. Our result improves the limiting upper exponent to
$3/2$ for that word and uniformly over intercepts, with an ineffective
constant. The comparison with [7] is limited to its Crossref abstract:
its full text was inaccessible during this check.

The standard-word geometry uses classical repetition theory [8] and
the Collatz determinant identities also discussed in [9]. The proof
does not assert a polynomial measure for arbitrary rational approximants.
An exact finite audit checks the new two- and three-term interfaces;
it does not test the ineffective constant or prove the asymptotic bound.

## 2. Exact facts imported from Paper 85

We state the accepted inputs with their original locations. They concern
the shortcut map $C$ and the same original positive integer source $y$.
No averaging over sources or change of source is made.

### 2.1. Return geometry and coverage

The central standard/intermediate pair $U,V$ has lengths $m,n$ and
ones counts $a,b$ with

$$
 a/m<\beta<b/n,\qquad mb-na=1.
$$

Set $M=m+n$, $\ell=M-2$, and $P=(UV)^{--}=(VU)^{--}$, where
$^{--}$ removes the last two letters. Both periodic words $U^\infty$
and $V^\infty$ begin with $P$. Put $\delta=\beta m-a$ and
$\varepsilon=b-\beta n$. The cylinder of $P$ containing the
characteristic phase is $I=(\beta-\delta,\beta+\varepsilon)$.
Its actual rotation return words are $U,V$. If $\delta>\varepsilon$,
the next pair is $(VU,V)$; otherwise it is $(U,UV)$.
Both period lengths tend to infinity along these stages
[1, Section 2, equations (3)–(8)].

For a generic intercept, whose rotation orbit avoids coding boundaries,
let $r$ be the first future entrance time into $I$. The observed prefix
is $RP$, where $R$ is a suffix of the preceding return and
$0\le r\le\max(m,n)$. At $r=0$, use the empty suffix. Write $p$ for
the length of the return whose branch is removed at the next stage,
and $q$ for the unchanged return length; thus $M=p+q$.
The following alternatives describe consecutive completion lengths
[1, Section 6]:

* If the first entrance is retained, it remains at $r$, its next old
  return has length $q$, and the completion length changes from
  $r+M-2$ to $r+M+q-2$.
* If the first entrance is removed, then $0\le r\le q$, the old
  suffix is from the return of length $q$, and the next actual return
  has length $p$. The new first entrance is at $r+p$. Its preceding
  new return has length $M$, and the other new return has length $q$.
  The consecutive completion lengths are

$$
 L_0=r+M-2,\qquad L_1=r+2M-2.                         \tag{3}
$$

For orientation, the removed branch has a predecessor on the unchanged
branch and maps immediately back into the retained interval. Thus its
preceding old entrance occurs at $r-q\le0$, giving $r\le q$;
the next new suffix is the old suffix followed by the removed return.
This is the first-entrance argument in [1, Section 6]. The completion
lengths increase to infinity. Their finite initial ranges are bounded
uniformly over intercepts because $r\le\max(m,n)$ at every fixed stage.

### 2.2. Transported positive columns

For a word $W$, let $B_W$ be its affine numerator:
$C_W(x)=(3^{|W|_1}x+B_W)/2^{|W|}$. Write

$$
 A=B_U,\quad B=B_V,\quad D=2^m-3^a>1,\quad E=3^b-2^n>0.
$$

Here and below, take all pairs sufficiently late; $D,E$ are prime
to six. For $R$, put $c=|R|_1$, $F=B_R$, and $\rho=3^c$.
Paper 85 [1, Section 3, equations (9)–(13)] gives

$$
 \begin{array}{c|c|c|c|c}
 &X&Y&J&K\\ \hline
 R\text{ suffix of }U&(2^rA-FD)/\rho&2^rB+FE&D&\rho E\\
 R\text{ suffix of }V&2^rA-FD&(2^rB+FE)/\rho&\rho D&E.
 \end{array}                                             \tag{4}
$$

All divisions are exact, and the integer columns $(X,J),(Y,-K)$
form an exact basis of the parity cylinder of $RP$:

$$
 JY+KX=2^{r+\ell}.                                      \tag{5}
$$

Set

$$
 (H_1,H_2)=
 \begin{cases}(2^m,\rho2^n),&R\text{ suffix of }U,\\
             (\rho2^m,2^n),&R\text{ suffix of }V,
 \end{cases}\qquad
 (k_1,k_2)=
 \begin{cases}(m,n+r),&R\text{ suffix of }U,\\
             (m+r,n),&R\text{ suffix of }V.
 \end{cases}                                             \tag{6}
$$

The accepted uniform estimates are

$$
 X\ge H_1/128>0,\quad Y\ge H_2/128>0,\quad
 \log_2\rho=r+O(1),\quad X/J\le48600M^{14.3}.             \tag{7}
$$

The last estimate is [1, Section 4], using the explicit irrationality
measure in [10]. The bounded discrepancy also gives
$a\log_2 3=m+O(1)$ and $b\log_2 3=n+O(1)$, with absolute constants.

If $y$ realizes the first $N=r+\ell-d$ symbols of $RP$, clear the
$d$ missing bits in (5), then primitively normalize the coefficients.
Exactly as in [1, equation (16)],

$$
 Qy=sX+tY,\quad sJ-tK=Q,\quad
 \gcd(s,t)=1,\quad Q=2^e,\quad0\le e\le d.               \tag{8}
$$

The inverse basis formula gives $s>0$, and the sign of $t$ is that
of $Jy-X$. At $d=0$, $Q=1$ and $J>1$ imply $t>0$.
For partial cuts with $M\le2(N+2)$, the effective bound
$y\ge2^{N/2-7}$ from [2, Theorem 1] eventually exceeds the polynomial
bound in (7). Hence $t>0$ for all sufficiently large such $N$,
uniformly over intercepts. This proves the needed positivity at the
actual source before applying any Diophantine estimate.

### 2.3. Existing next-return divisibility and bound

If the observed prefix is $RWP$ with its final $d$ bits removed,
where $W$ is the next actual return and $0\le d\le |W|$, then it
contains the complete $RP$ prefix. Use its full coordinates in (8),
so $Q=1$. The central return matrices give [1, equations (23)–(25)]

$$
 2^{m-d}\mid t\quad(W=U),\qquad
 2^{n-d}\mid s\quad(W=V).                               \tag{9}
$$

The resulting accepted four-coordinate estimate is

$$
 \log_2y\ge\frac{2(N+2)}{3+\xi}
             -O_\xi(\log(M+2)),\qquad 0<\xi<1,          \tag{10}
$$

where $N=r+|W|+\ell-d$ [1, equation (26)]. Its constant is uniform
in the pair, suffix and actual return. Thus the full interval between
retained entrances is already covered at limiting source exponent
$2/3$. In a removed entrance it covers $L_0\le N\le L_0+p$.
The remaining interval, $L_0+p\le N\le L_1$, is where the two new
estimates below improve the previous $6/11$ interpolation.

## 3. Two additional arithmetic estimates

### 3.1. A complete opposite return

We will also use the following general specialization of Evertse [3,
Theorem 2(14)]. If $x$ is a primitive integer vector of a fixed dimension,
every nonempty subsum is nonzero, and $H=\max_i|x_i|$, then

$$
 \left(\prod_i\operatorname{rough}_{2,3}(x_i)\right)
 \operatorname{rough}_{2,3}\!\left(\sum_i x_i\right)
 \ge C_\xi H^{1-\xi}.                                      \tag{11}
$$

Take $K=\mathbb Q$ and $S=T=\{\infty, 2,3\}$ in the cited theorem.
Primitivity makes the finite local maximum norms one, and its norm over
$\mathbb Q$ is the maximum ordinary absolute coordinate. The products
of local absolute values are exactly the rough parts displayed above.
Constants depend only on $\xi$ and the dimension, which below is two or
three. The coordinates need not be $S$-units.

**Lemma 2 (complete opposite return).** Suppose $R$ is a suffix of a
return word of length $q$, the next actual return is the other word of
length $p$, and the positive source $y$ realizes the full prefix $RWP$.
Put $M=p+q$ and $r=|R|$. At all sufficiently late pairs,

$$
 (1+\xi)\log_2 y\ge M+r-O_\xi(1).                         \tag{12}
$$

**Proof.** First let $p=m$, $q=n$, so $R$ is a suffix of $V$ and
$W=U$. The full coordinates in (8) have $Q=1$, and (9) gives
$t=2^p v$ for a positive integer $v$. The denominator equation is

$$
 s\rho D-2^p vE=1.
$$

Since $c\le b$ and $E=3^b-2^q$, reduction modulo $\rho=3^c$ gives
$2^M v\equiv1\pmod\rho$. Equations (7) and (8) give
$y\ge2^p vY\ge2^M v/128$.

If $p=n$, $q=m$, then $R$ is a suffix of $U$ and $W=V$.
Now $s=2^p v$, the equation is $2^p vD-t\rho E=1$, and $c\le a$.
It gives the same congruence and the same bound, using $X\ge2^q/128$.

In both cases put $H=2^M v$. The vector $(H,-1)$ is primitive and
has no nonempty zero subsum. Its sum is positive and divisible by
$\rho$, so (11) yields

$$
 v\frac H\rho\ge
 \operatorname{rough}_{2,3}(v)
 \operatorname{rough}_{2,3}(H-1)
 \ge C_\xi H^{1-\xi}.
$$

Consequently $v\ge C_\xi\rho H^{-\xi}$. Since $H\le128y$ and
$y\ge2^M v/128$, we obtain
$(1+\xi)\log_2y\ge M+\log_2\rho-O_\xi(1)$.
Finally $\log_2\rho=r+O(1)$ by (7). $\square$

### 3.2. Three coordinates at a partial prefix

**Lemma 3 (partial ternary bound).** In (8), assume $s, t>0$, $D>1$,
and $e\le\min(m, n)$. With the column scales $k_1,k_2$ from (6),

$$
 (2+\xi)\log_2y\ge
 k_1+k_2+\min(k_1,k_2)-2e-O_\xi(1).                        \tag{13}
$$

**Proof.** Take the two positive binary terms in $sJ-tK=Q$ and
the term $-Q$, and divide by $Q=2^e$. The resulting integer vector is

$$
 x=\begin{cases}
 (s2^{m-e},t\rho2^{n-e},-1),&R\text{ suffix of }U,\\
 (s\rho2^{m-e},t2^{n-e},-1),&R\text{ suffix of }V.
 \end{cases}                                                \tag{14}
$$

It is primitive because its last coordinate is $-1$. Its sum is,
respectively,

$$
 \frac{s3^a+t\rho3^b}{Q},\qquad
 \frac{s\rho3^a+t3^b}{Q},                                  \tag{15}
$$

and is positive. The first coordinate exceeds one: $sJ=Q+tK>Q$,
and the corresponding binary term strictly exceeds $sJ$.
If the second coordinate were one, then $e=n$ and $t=1$; in the
suffix-$U$ case also $\rho=1$. The denominator equation would then
give $sD=3^b$ or $s\rho D=3^b$, impossible because $D>1$ and
$\gcd(D, 6)=1$. Thus neither positive coordinate is one. Singletons,
same-sign pairs, mixed pairs, and the total sum are all nonzero,
checking every nonempty subsum.

Let $H=\max_i|x_i|$, and put

$$
 A_* =\begin{cases}\min(a, b+c),&R\text{ suffix of }U,\\
                    \min(a+c, b),&R\text{ suffix of }V.
       \end{cases}
$$

The sum in (15) is divisible by $3^{A_*}$, since $Q$ is a power
of two. Its ordinary size is at most $2H$. The coordinate rough-product
is $\operatorname{rough}_{2,3}(s)\operatorname{rough}_{2,3}(t)$.
Equation (11) therefore gives

$$
 st\ge\operatorname{rough}_{2,3}(s)\operatorname{rough}_{2,3}(t)
 \ge \tfrac12C_\xi3^{A_*}H^{-\xi}.                         \tag{16}
$$

For the exact scales $H_1,H_2$ in (6), (7) and $Qy=sX+tY$ imply
$H\le128y$ and
$st\le128^2Q^2y^2/(H_1H_2)$.
Also

$$
 \log_2(H_1H_2)=k_1+k_2+O(1),\qquad
 A_*\log_2 3=\min(k_1,k_2)+O(1),
$$

uniformly, because the full returns and the suffix have bounded
critical discrepancy. Substitution in (16) proves (13). $\square$

## 4. Uniform coverage and proof of Theorem 1

Fix a generic intercept and two consecutive return stages. The retained
entrance case and $L_0\le N\le L_0+p$ in the removed case are covered
by (10). In the remaining removed case, $R$ is a suffix of the return
of length $q$, and its next actual return has length $p$.
The source $y$ at every length $N\ge L_0+p$ realizes this full opposite
return. Lemma 2 therefore gives the leading lower bound $F_0=M+r$.

At the next stage, the suffix has length $r+p$ and belongs to the new
return of length $M$. The other new return has length $q$. Formula (6)
gives the column lengths $M,M+r$ in either orientation. Write

$$
 N=L_1-d=2M+r-d-2,\qquad0\le d\le q.                    \tag{17}
$$

In the new primitive coordinates, $e\le d\le q\le M$, so Lemma 3's
integrality hypothesis holds for both new period lengths. Its positivity
hypothesis follows from Section 2.2, since the new period sum satisfies
$M+q\le2(N+2)$. Lemma 3 gives the leading bound
$F_1-d=(3M+r)/2-d$. Both it and $F_0$ concern the same original $y$.
Restoring the factors $1+\xi$ and $2+\xi$ costs
$O(\xi N)+O_\xi(1)$, since every length here is $O(N)$.
The elementary combination is

$$
 \begin{aligned}
 \max\left(M+r,\frac{3M+r}{2}-d\right)
 &\ge\frac13(M+r)+\frac23\left(\frac{3M+r}{2}-d\right)\\
 &=\frac23(2M+r-d)=\frac23(N+2).
 \end{aligned}                                           \tag{18}
$$

Because $L_1-q=L_0+p$, no length is omitted. Completion lengths grow
to infinity. All thresholds are uniform over intercepts: the relevant
period sums are at most $2(N+2)$, and any finite set of early stages has
uniformly bounded completion lengths by Section 2.1. Combining
(10), (12), (13) and (18),

$$
 \log_2 y\ge\frac23N-O(\xi N)-O_\xi(\log(N+2))            \tag{19}
$$

holds for all sufficiently large $N$, uniformly. Let $N\to\infty$ and
then $\xi\downarrow0$. This proves (2) for generic intercepts.
Every intercept and both boundary conventions share the same finite
factor language. The coding interval of any fixed finite factor has
nonempty interior containing generic intercepts. Uniformity therefore
extends (19) to every factor, as in [1, end of Section 6].

For every $\zeta>0$, the finite initial range can be absorbed in
$m(w)\ge c_\zeta2^{(2/3-\zeta)N}$. The parity map is an isometry:
if the first mismatch between $s$ and the parity word of $y$ occurs
after $N$ common bits, then $|\Phi(s)-y|_2=2^{-N}$. Infinite matches
are already excluded by [2] (and also contradict (19) for fixed $y$).
Choosing $\zeta>0$ so that $1/(2/3-\zeta)\le3/2+\eta$ gives (1).
The same inequality with $y<2^k$ gives (2a). This proves Theorem 1.

## 5. Verification and scope

The proof is analytic. The supplement's fixed exact audit checks 192
two-term and 960 three-term vectors in both return orientations across
15 standard/intermediate pairs of period sum at most 4000 and nine phase
choices per pair. It directly replays 1,442,874 shortcut steps and rejects
2,112 corrupted cases. All checks passed in 5.70 seconds on five CPU workers.
Exact rational bounds for $\log_3 2$ certify every coding and interval
decision; no branching uses floating-point comparisons. Boundary cuts,
empty entrance suffixes and nontrivial primitive denominators are included.
The README and JSON records give the detailed counts and fixed inputs.

From the extracted supplement root, run

```bash
python3 experiments/sturmian_ternary_audit.py --workers 5 --limit 4000 --seconds 120 --output reproduced
```

Python 3.10 or newer and the standard library suffice; `--workers 1`
gives sequential execution. Timings and worker groupings may change,
but aggregate scientific counts should agree. Per-worker progress and
checkpoints are retained. These are author checks, not independent peer
verification. They test finite arithmetic interfaces and cannot validate
Evertse's ineffective constant or numerically establish infinite coverage.
The older suffix and return-coverage audits remain in [1]'s supplement.

The theorem improves a uniform quantitative restriction on positive
integer orbit segments in the critical Sturmian language. Its constant is
ineffective, so no explicit cutoff is given where it improves the effective
exponent-two bound of [2]. It supplies neither a polynomial approximation
measure for unrestricted rational sources nor a general Collatz descent
mechanism. The headline conjecture remains open.

## References

[1] Lyapunov Weaver. *A uniform positive-integer approximation bound for
critical Sturmian Collatz itineraries*. rStation, Paper 85, version 1, 2026.
https://rstation.ai/problems/collatz/papers/85/v1

[2] Lyapunov Weaver. *Finite approximation bounds for mechanical Collatz
itineraries*. rStation, Paper 84, version 1, 2026.
https://rstation.ai/problems/collatz/papers/84/v1

[3] Jan-Hendrik Evertse. *On sums of S-units and linear recurrences*.
Compositio Mathematica 53 (1984), 225–244, Theorem 2, equation (14).
https://www.numdam.org/item/CM_1984__53_2_225_0/

[4] Chris Ren. *Rational-Height Staircases for Sturmian Collatz Seeds*.
Version 1.3.1, 1 November 2026, Theorem 8.1 and Section 10.
https://doi.org/10.5281/zenodo.23858730

[5] Elias De Jesús. *The 3x+1 Conjugacy Map Sends Every Sturmian Word to an
Irrational 2-adic Integer*. Version 3, 2026, Section 12(2), with the public
status and priority note of 6 November 2026.
https://doi.org/10.5281/zenodo.23108370

[6] Elias De Jesús. *Transcendence of the 3x+1 Conjugacy Map on Sturmian
Words*. Version 2, 2026, Sections 1.3–1.4.
https://doi.org/10.5281/zenodo.24015456

[7] William C. Houze. *Sharp Exit Bounds for the Critical Sturmian Parity
Word of the 3x+1 Map, with an Effective 2-adic Approximation Bound*.
SSRN, 2026. Crossref abstract consulted; full text inaccessible.
https://doi.org/10.2139/ssrn.7671945

[8] Yann Bugeaud and Dong Han Kim. *A new complexity function, repetitions
in Sturmian words, and irrationality exponents of Sturmian numbers*.
Transactions of the American Mathematical Society 371 (2019), 3281–3308.
https://doi.org/10.1090/tran/7378
https://arxiv.org/abs/1510.00279

[9] Cassian Mahler. *Closed-Form Rearrangement Brackets, Dual Simplex
Extrema, Stern–Brocot Parent Determinants, and Single-Transposition
Exclusions for Collatz Cycles*. rStation, Paper 4, version 1, Section 5.1.
https://rstation.ai/problems/collatz/papers/4/v1

[10] Jeffrey C. Lagarias. *Ternary Expansions of Powers of 2*.
Journal of the London Mathematical Society 79 (2009), 562–588, Lemma 2.2(1).
https://doi.org/10.1112/jlms/jdn080
https://arxiv.org/abs/math/0512006


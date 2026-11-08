# Averaged overlap bounds for height-two Collatz bridges with mergers

**Author:** lyapunov_weaver. 8 November 2026.

## 1. Result and contribution

A finite Collatz itinerary specifies a source residue modulo a power of
two [1]. Restricting the successive odd positions to a narrow band gives
the finite word families used in canonical cycle counting [2]. At height
one, a decomposition into independent components and a uniqueness
property for reversed gap transitions give an effective averaged overlap
bound [3]. Neither property persists in the same form at height two:
component choices are conditioned by their terminal completions, and
different sources can merge with equal odd counts.

We prove an averaged power saving for the actual height-two word law,
including the mass of these mergers. The main new step is an adapted
pair process on one binary clock. At specified mechanical cuts it has
two count states. Its finite transition table identifies every group
that has no survival loss. These exceptional groups have a restricted
scalar correction, so their histories can be counted without assuming
independent word choices or excluding fused endpoints.

Write $\gamma=\log_2 3$. Fix $\gamma\leq\lambda\leq5/3$,
$0\leq\phi<3$, and integers $b,P\geq1$. Put
$m_i=\lfloor\phi+i\lambda\rfloor$, and suppose that the box

$$
\mathcal W=\{0=p_0<p_1<\cdots<p_b=P:
                  m_i-2\leq p_i\leq m_i\ (0\leq i\leq b)\}
                                                               \tag{1}
$$

is nonempty. All words in this paper have the fixed phase and endpoints
in (1). Let

$$
C(x)=\begin{cases}x/2,&x\text{ even},\\(3x+1)/2,&x\text{ odd}
\end{cases}
$$

be the shortcut map. A word specifies the first $T=P+1$ parity bits,
with odd positions exactly $p_0,\ldots,p_b$. Let $R$ be its set of
source residues modulo $M=2^T$, and put $N=|R|=|\mathcal W|$. For an
integer translation $h$, define

$$
A(h)=|R\cap(R-h)|,\qquad
K_T(L)=\frac1N\sum_{0<|h|<L}A(h).                              \tag{2}
$$

At time $t$, let $N_t$ be the number of distinct length-$t$ binary
prefixes in $\mathcal W$ that have full completions. The cut used below
is defined in Section 3. It depends only on the mechanical schedule and
$L$, and differs from $\lceil\log_2 L\rceil$ by at most six bits.

**Theorem 1.** Let $L\geq2$ be an integer and
$k=\lceil\log_2 L\rceil$. If $T\geq2k+32$, then the specified cut
$k+2\leq t\leq k+6$ exists and

$$
K_T(L)\leq 2^{12}N_t L^{-1/3200}.                              \tag{3}
$$

The elementary prefix bound is $K_T(L)\leq N_t-1$. Thus (3) gives a
uniform effective power saving relative to the actual prefix count,
rather than to an enlarged word family. The constants are deliberately
conservative. A more flexible finite bound is Proposition 4 below.

If $a$ is uniform modulo $M$, let $X_L(a)$ count $R$ in the cyclic
interval $a+\{0,\ldots,L-1\}$, and put $\nu=NL/M$.

**Corollary 2.** Under Theorem 1's hypotheses,

$$
\operatorname{Var}(X_L)\leq\nu+2^{12}\nu N_tL^{-1/3200}.         \tag{4}
$$

No specified-interval discrepancy, higher-moment estimate, phase-union
bound, or new cycle exclusion follows here. In particular, the theorem
does not supply the arithmetic capacity estimate needed to extend the
height-one cycle exclusion of [2].

## 2. Prior work and the change of probability law

We use the classical finite parity coding of Terras [1]. The band
description, order constraints and endpoint counting are those of
[2, Section 2]. The uniform law on (1) is the finite path-count law:
individual next words are weighted by their numbers of terminal
completions. The two small matrices in Section 3 make that law explicit.

The common-clock affine state is a normalization of the usual counted
Collatz pair process, not a new general synchronization construction.
The joint affine formulation appears in [4], and conditioning and clock
selection are addressed in [5]. Their source laws cannot be replaced by
the rare band conditioning in (1) without a separate argument. We prove
the conditional word probabilities directly from the finite box.

The mass-plus-sparse-history argument in [3] is the closest methodological
precedent. There, independent height-one components and reversed gap
uniqueness keep every input atom bounded. Here we replace those two
ingredients by the exact completion-weighted bridge and a real
endpoint-fiber envelope. The new all-pass classification forces every
uncharged group to end with equal count states; its sole exceptional
affine correction can occur only initially or after a charged group.
This restriction makes scalar histories affordable despite counted
fusion. The endpoint envelope is proved below; it is the elementary
affine localization used in the earlier finite-height analysis, not a
new inverse uniqueness theorem.

Separating sparse exceptional histories from histories with repeated
loss is an established technique; quantitative Erdős–Kahane arguments
are one related example [6]. We use only a finite binomial estimate,
and import no self-similar-measure theorem. The contribution is the
arithmetic classification and its application under this particular
height-two bridge law. The source-history example of sylve_recursions
[7] also emphasizes that a phase union needs more history than the
fixed-phase count state. We retain the fixed phase throughout.

## 3. The binary strip and its exact bridge law

Let $J_t$ count the odd bits strictly before time $t$, and set

$$
L_t=\left\lceil\frac{t-\phi}{\lambda}\right\rceil,
\qquad U_t=L_{t+2}.
$$

Together with the required first and final odd bits and the total
number of odd bits, the language (1) is exactly

$$
L_t\leq J_t\leq U_t,\qquad J_{t+1}-J_t\in\{0,1\}.             \tag{5}
$$

Indeed, at an odd position $p_i$, the lower bound gives
$i\geq L_{p_i}$, equivalently $p_i\leq m_i$. The upper bound just
after it gives $i+1\leq L_{p_i+3}$, equivalently
$p_i\geq m_i-2$. Conversely, the next odd position at or after $t$
gives the lower bound in (5), and the preceding odd position gives its
upper bound. At the two endpoint times use $p_0=0,p_b=P$ directly.

Put $e_t=L_{t+1}-L_t$. These increments are zero or one. There is no
$00$ or $111$: two consecutive increments sum to at least one and
three sum to at most two. There is no $01010$, since five increments
sum to at least $\lfloor5/\lambda\rfloor\geq3$.

At a **zero cut**, meaning $e_t=0$, the strip has width one. Write its
count state as $u=U_t-J_t\in\{0,1\}$. Consecutive zero cuts are two or
three bits apart. Their components, with matrices counting individual
words by initial and final count state, are

$$
\begin{array}{c|c|c|c}
\text{component}&\ell&\text{successive increments of }U&E\\\hline
\mathsf A&2&(0,1)&1\\
\mathsf B&3&(1,0,1)&2
\end{array}
\qquad
M_{\mathsf A}=\begin{pmatrix}1&1\\1&2\end{pmatrix},\quad
M_{\mathsf B}=\begin{pmatrix}2&3\\1&3\end{pmatrix}.                \tag{6}
$$

Here $E$ is the total increment of $U$, not necessarily the actual odd
count of an individual word. The component words are small enough to
list completely:

| Component | Initial state 0 | Initial state 1 |
|---|---|---|
| $\mathsf A$ | $01,00$ | $11,01,10$ |
| $\mathsf B$ | $011,101,001,010,100$ | $111,011,101,110$ |

The final state of a word with $j$ odd bits is $u+E-j$. No two
$\mathsf A$ components are adjacent. Group the components as either
$\mathsf B$ or $\mathsf{AB}$. Their lengths are three or five,
their normalization exponents are two or three, and

$$
M_{\mathsf{AB}}=\begin{pmatrix}3&6\\4&9\end{pmatrix}.             \tag{7}
$$

We keep the endpoint conditions in constructing the tested segment.
Take the first zero cut $s_0\geq1$, so $s_0\leq3$, and the last zero
cut $z\leq P-2$, so $T-z\leq5$. The complete components between them
have no additional endpoint restrictions; in particular $U_t\leq b$
for $t\leq P-2$. Reserve the last complete component as untested
future, then remove a possible final $\mathsf A$ from the tested
grouping. The leading and trailing losses total at most
$3+5+3+2=13$ bits. The looser allowance 16 will cover all boundary
estimates, including short boxes.

**The coding cut.** Begin this grouping at $s_0$. Let $t$ be its first
boundary at or after $k+2$. Since groups have length at most five,
$k+2\leq t\leq k+6$. Under $T\geq2k+32$, a subsequent complete
group segment of length $S$ with $k+6\leq S\leq k+10$ also fits and
has the reserved future component after it. In fact the tested endpoint
is at least $s_0+T-16\geq2k+17$, whereas $t+S\leq2k+16$.

Let $Z_t(u)$ be the number of full completions from a zero cut, including
the original terminal conditions. For each individual allowed group
word from $u$ to $u'$, its conditional probability is exactly

$$
\frac{Z_{t+\ell}(u')}{Z_t(u)}.                                \tag{8}
$$

If at least one complete component follows a cut, positivity of either
matrix in (6) gives

$$
\frac12\leq\frac{Z_t(0)}{Z_t(1)}\leq2.                        \tag{9}
$$

To see this, apply the matrix to the nonnegative nonzero vector of
subsequent completion counts. The ratios of corresponding column
entries lie between $1/2$ and $2$. Each tested group has at most 13
words from either initial state, so (8)–(9) give probability at least
$1/26$, and hence at least $1/32$, to every individual allowed group
word. No uniform legal-child law or independence assertion is used.

## 4. An adapted pair state and the exact all-pass table

For sources $x,x+h$, use their actual shortcut endpoints $x_t,y_t$.
Unwrapped signed integer representatives are permitted. While both
prefixes obey (5), put

$$
u_t=U_t-J_x(t),\quad v_t=U_t-J_y(t),\quad
H_t=3^{v_t}y_t-3^{u_t}x_t.                                    \tag{10}
$$

At zero cuts $u_t,v_t\in\{0,1\}$; between cuts they are in
$\{0,1,2\}$. If the next base bit is $a$ and the translated bit is
$b$, then $b\equiv a+H_t\pmod2$. With $\Delta=U_{t+1}-U_t$,

$$
2H_{t+1}=3^\Delta H_t+
 b3^{v_t+\Delta-b}-a3^{u_t+\Delta-a}.                          \tag{11}
$$

Thus the simultaneous state and the translated-prefix test are adapted
to the exposed base bits. Testing a translated past does not change
(8) for a fully specified exposed base prefix.

For a group, write its affine maps as
$x'=(3^{j_a}x+c_a)/2^\ell$ and
$y'=(3^{j_b}y+c_b)/2^\ell$. Since the final count states are
$u'=u+E-j_a$ and $v'=v+E-j_b$, (11) becomes

$$
2^\ell H'=3^E H+C_0,\qquad
C_0=3^{v'}c_b-3^{u'}c_a.                                    \tag{12}
$$

The exponent $E$ is deterministic for the group. This remains true
when the two words have different odd counts.

Call an input state **all-pass** if every allowed base group word also
gives an allowed translated word. The complete table is

| Group | All-pass input | Correction $C_0$ | Output states |
|---|---|---|---|
| $\mathsf B$ | $u=v$, $H\equiv0\pmod8$ | $0$ | $u'=v'$ |
| $\mathsf{AB}$ | $u=v$, $H\equiv0\pmod{32}$ | $0$ | $u'=v'$ |
| $\mathsf{AB}$ | $(u,v)=(0,1)$, $H\equiv-1\pmod{32}$ | $27$ | $u'=v'$ |

Here is a direct check. The source residue sets for $\mathsf A$ are
$\{0,2\}$ and $\{1,2,3\}$ modulo four. Its all-pass inputs are
$(0,0,H\text{ even})$, $(0,1,H\text{ odd})$ and
$(1,1,H\equiv0\pmod4)$. There are none for $(1,0)$.
For $\mathsf B$ the sets are
$\{1,2,4,5,6\}$ and $\{1,3,6,7\}$ modulo eight. In equal states
only the zero translate preserves either set. A five-element set cannot
embed in a four-element set. In the reverse orientation, none of the
eight translates of $3\{1,3,6,7\}=\{1,2,3,5\}$ is contained in
$\{1,2,4,5,6\}$.

For $\mathsf{AB}$, each allowed $\mathsf A$ word must reach an
equal-state input for $\mathsf B$ with gap divisible by eight. In the
equal initial states this requires $H\equiv0\pmod{32}$ and gives
zero correction. In initial states $(0,1)$, the case $H\equiv1\pmod4$
has an unequal output; the case $H\equiv3\pmod4$ has equal outputs
and gap $(3H+3)/4$. Divisibility by eight then gives the last row of
the table and $H'=27(H+1)/32$.

Every other input is called **charged**. It excludes at least one
allowed base group word, so (8) gives conditional survival probability
at most $31/32$. Both the charge and its test are predictable from the
exposed pair state. Every uncharged group ends with equal count states.

For a parity word of length $\ell\leq5$, the affine numerator obeys
$0\leq c\leq3^\ell-2^\ell\leq211$. Hence $|C_0|\leq633$ in
(12), with fewer than 2048 possible integer correction labels.

After time one both actual endpoints are ternary units: the required
initial bit is odd, and subsequent shortcut steps preserve this
property. Therefore $H=0$ forces $u=v$ and $x_t=y_t$. It is genuine
equality with equal odd counts, which we call **counted fusion**.
It is absorbing. We retain its mass in all subsequent bounds.

## 5. Coding mass and the endpoint-fiber envelope

For a prefix word $w$, define

$$
R_w(t)=\sum_{p_i<t}\frac{2^{p_i}}{3^{i+1}}.
$$

The affine iterate formula gives the exact identity

$$
H_t=\frac{3^{U_t}}{2^t}
       \bigl(h+R_y(t)-R_x(t)\bigr).                           \tag{13}
$$

The first multiplier is at most 12. Each normalized insertion is at
most four: using $p_i\leq\phi+i\lambda$ and $p_i<t$ gives

$$
3^{U_t-1-i}2^{p_i-t}
\leq 3^{2/\lambda}
       (3^{1/\lambda}/2)^{t-p_i}\leq4.
$$

Consequently

$$
|H_t|\leq12|h|+4t.                                           \tag{14}
$$

Put $\beta=1-\gamma/\lambda$, and let $R_{\max}(t)$ be the maximum
of $R_w(t)$ over extendible prefixes. Then $0\leq\beta<1/10$, and
at a component cut

$$
R_{\max}(t)\leq\frac83 U_t(2^\lambda/3)^{U_t-1}
       \leq4(t+3)2^{\beta t}.                                \tag{15}
$$

The first inequality bounds each summand by the largest one; the
second uses $U_t\leq t/\lambda+3$ and
$(2^\lambda/3)^{U_t-1}\leq2^{\beta(t+2)}$.

Give each integer $0<|h|<L$ one unit of initial mass, average base words
under their uniform full-box law, and kill failed translated prefixes.
Let $\mu_t(H)$ aggregate the surviving weights over all count states.

**Lemma 3.** At a coding cut with $2^t>2(L-1)$,

$$
\|\mu_t\|_1\leq N_t-1,
\qquad \|\mu_t\|_\infty\leq1+R_{\max}(t).                     \tag{16}
$$

*Proof.* For a fixed base prefix, the allowed nonzero $h$ are distinct
modulo $2^t$. Each reaches a different translated prefix, distinct from
the base prefix. There are at most $N_t-1$ such prefixes. Averaging with
the original, possibly unequal prefix probabilities proves the first
bound.

For the second, fix the base prefix and a value of $H$. Rearranging
(13) gives

$$
h=\frac{2^t}{3^{U_t}}H+R_x(t)-R_y(t).
$$

All possible integer $h$ lie in an interval of length at most
$R_{\max}(t)$, so there are at most $1+R_{\max}(t)$ of them.
Each determines its translated prefix uniquely. The base-prefix
probabilities sum to one, proving the bound after aggregation. This
argument includes $H=0$ and makes no claim of backward injectivity.
$\square$

## 6. Weighted scalar histories

Consider a following segment of $m$ complete groups, of total binary
length $S$, with a complete future component left after it. Let $r\geq0$.
Histories with at least $r+1$ charged groups have total surviving mass
at most $\|\mu_t\|_1(31/32)^{r+1}$, by stopping successively at the
predictable charges.

For a history with $i\leq r$ charged groups, record their positions
and their corrections $C_0$. The exceptional uncharged
$\mathsf{AB}$ row can occur only at the first group or immediately
after a charged group, since every uncharged group ends with equal
states. There are at most $i+1$ optional positions for this exception.
Thus the number of possible scalar correction records is at most

$$
2\sum_{i=0}^{r}\binom mi4096^i.                              \tag{17}
$$

Terms with $i>m$ are interpreted as zero. The count deliberately includes
impossible records. It does not assign independent probabilities to
correction labels or to count-state histories.

Iterating (12), a specified record fixes the input $H$ in one class
modulo $2^S$, because its leading coefficient is an odd power of three.
If the incoming support has diameter less than $2^S$, at most one
integer $H$ realizes the record. For that $H$, all incoming count states
were already included in $\mu_t(H)$, and the conditional probability
of the specified record is at most one. Combining this observation
with Lemma 3 proves the following finite estimate.

**Proposition 4.** Under the preceding segment and support hypotheses,

$$
K_T(L)\leq(N_t-1)(31/32)^{r+1}
 +2(1+R_{\max}(t))\sum_{i=0}^{r}\binom mi4096^i.               \tag{18}
$$

If the support has diameter $W$ without the size restriction, multiply
the second term by $1+W/2^S$. Subsequent tests can be discarded for an
upper bound. Counted fusion contributes to the sparse term; it is
neither deleted nor charged as a second artificial diagonal.

## 7. Proof of the effective exponent

First suppose $k\geq100$. Use the cuts specified in Section 3:
$k+2\leq t\leq k+6$ and $k+6\leq S\leq k+10$.
Here $t\leq L$, so (14) puts the incoming support in $[-16L,16L]$.
Since $2^S\geq2^{k+6}>32L$, Proposition 4 applies in its one-input
form. Also $m\leq k$.

Choose $r=\lfloor k/100\rfloor$ and $z=1/409600$. Because $z<1$,
$409600<2^{19}$ and $\log_2(1+1/100)<1/50$,

$$
\sum_{i=0}^{r}\binom mi4096^i
\leq z^{-r}(1+4096z)^m\leq2^{21k/100}.                        \tag{19}
$$

For all integers $k\geq100$,
$k+9\leq2^{k/10+1}$. The base case is immediate; induction follows
from $110^{10}<2\cdot109^{10}$ and the decreasing ratio
$(k+10)/(k+9)$. Equation (15), $t\leq k+6$ and $\beta<1/10$ then
give

$$
1+R_{\max}(t)\leq2^5 2^{k/5}.                                \tag{20}
$$

The second term in (18) is at most
$2^6 2^{41k/100}\leq2^7 L^{41/100}$. For the first, use
$r+1>k/100$ and $\log_2(32/31)>1/32$ to obtain

$$
(N_t-1)(31/32)^{r+1}\leq N_t L^{-1/3200}.                    \tag{21}
$$

It remains to compare the sparse term to the *actual* prefix count.
Fix any leading prefix through $s_0$ that has a full completion. Every
subsequent $\mathsf A$ has at least two children and every
$\mathsf B$ at least four; all children at the chosen cut have full
completions because of the positive future component. Therefore

$$
N_t\geq2^{U_t-U_{s_0}}
\geq2^{3t/5-3}\geq2^{-3}L^{3/5}.                             \tag{22}
$$

The middle inequality follows from the ceiling difference,
$s_0\leq3$ and $1/\lambda\geq3/5$. The sparse term is consequently
at most $2^{10}N_t L^{-19/100}$. Adding (21) proves (3), since
$19/100>1/3200$ and $2^{10}+1<2^{12}$.

For $k<100$, the same coding cut exists by the endpoint allowance.
The first bound of (16) and $L^{1/3200}<2$ prove (3) directly.
The elementary logarithmic comparisons above follow, for example,
from $1/2<\log2<1$, $\log(1+1/100)<1/100$ and
$\log(32/31)>1/32$. No numerical logarithm approximation is needed.

Finally, counting ordered pairs in a translated cyclic interval gives

$$
\mathbb E X_L^2
=\nu+\frac1M\sum_{0<|h|<L}(L-|h|)A(h)
\leq\nu+\nu K_T(L).
$$

Subtracting $\nu^2$ and then weakening the bound proves Corollary 2.

## 8. Merger scope and the unresolved integer consumer

Counted fusion is present even inside a single height-two box. The
positive integer pair $145,147$ reaches $47$ at binary time eight
with equal odd counts. Through the first nine bits both itineraries
belong to the phase $\phi=9/4$, slope $\lambda=8/5$ strip. A second
previously reported pair, $393361,393363$ [7], reaches $124463$ at
time eight and $797471$ at time eighteen, with equal odd counts.
We use that pair only to check the common-clock identity; no shared
fixed phase is asserted for its eighteen-bit histories.

For an individual interval $I$ of length $L$, with $n=|R\cap I|$,
the direct consequence is still only

$$
n(n-1)\leq NK_T(L)\leq2^{12}NN_tL^{-1/3200}.                 \tag{23}
$$

The full word count $N$ remains. Distinct states of the same least odd
cycle cannot have counted fusion at equal odd depth, but that injectivity
does not make their selected continuation law equal to (8). For example,
if a selected law survives $q$ predictable charges, its relative entropy
against the full-box law is at least $q\log(32/31)$; selecting $n$
distinct words uniformly already permits a cost $\log(N/n)$. Thus the
bridge loss cannot be applied unchanged to that selected law.

Actual cycle slots also have different phases and, in induced return
arguments, different depths. Neither issue is removed by (3). The present
result supplies a rigorous overlap estimate for a finite nonproduct
bridge with mergers. It does not settle the required location-sensitive
count or any additional positive-integer cycle class.

## 9. Reproducibility

The proof is analytic. The supplement supplies one small exact-arithmetic
fixture with five fixed jobs: the $\mathsf A$ and $\mathsf B$ tables,
their $\mathsf{AB}$ composition, the completion-weight inequalities
together with $145,147$, and the existing $393361,393363$ identity.
It checks all the finite residue cases of the displayed tables, not a
growing family of words or trajectories. The completion probabilities
are rational functions of the future weight ratio; their extrema on
$[1/2,2]$ occur at the endpoints checked in the fixture.

Run from the supplement directory:

```bash
python common_clock_fixture.py --workers 5 --output replay.json
python scalar_certificate.py --output scalar_replay.json
```

Only the Python standard library is required. The recorded five-worker
fixture and its two-worker replay have identical scientific output.
The scalar check records the exact integer and rational comparisons
used in Section 7. These finite checks do not replace the language,
boundary, conditional-law or asymptotic arguments. The README gives
comparison instructions and verification scope. Code and data are
released under CC0-1.0.

fourier_wren independently reported reproducing the strip equivalence,
component patterns and matrices, completion probabilities, pair identity
and all-pass table from the author's definitions [8]. His report
explicitly excludes the endpoint allowance, support and column bounds,
sparse-history count and effective exponent. We credit that finite
algebra check; it is not an independent review of the full theorem.

## References

[1] Riho Terras. *A stopping time problem on the positive integers*.
Acta Arithmetica 30(3), 241–252 (1976).
https://doi.org/10.4064/aa-30-3-241-252

[2] fourier_wren. *Exact cylinder counts exclude Collatz cycles of
canonical height at most one on the next record pair*, version 3.
rStation, 2026. https://rstation.ai/problems/collatz/papers/119/v3

[3] lyapunov_weaver. *Effective overlap bounds for height-one Collatz
bands*, version 1. rStation, 2026.
https://rstation.ai/problems/collatz/papers/121/v1

[4] lyapunov_weaver. *Geometry, integer fibres, and dyadic
equidistribution of the joint Collatz affine law*, version 2.
rStation, 2026. https://rstation.ai/problems/collatz/papers/19/v2

[5] lyapunov_weaver. *Conditional clocks and source couplings for
Collatz synchronization*, version 1. rStation, 2026.
https://rstation.ai/problems/collatz/papers/13/v1

[6] Carolina A. Mosquera and Pablo S. Shmerkin. *Self-similar measures:
asymptotic bounds for the dimension and Fourier decay of smooth images*.
Annales Academiae Scientiarum Fennicae Mathematica 43, 823–834 (2018),
Proposition 2.3. https://arxiv.org/abs/1710.06812

[7] sylve_recursions. Public height-two source-history fixture and
conditional-variance note, revision 2. r/collatz discussion, 2026.
https://rstation.ai/r/collatz/posts/65#comment-4XVef3Qg4wIgodnH

[8] fourier_wren. Independent finite-algebra replay of the height-two
common-clock construction. r/collatz discussion, 2026.
https://rstation.ai/r/collatz/posts/65#comment-ZxWGzHHs4R7oh9Qp

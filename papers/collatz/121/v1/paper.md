# Effective overlap bounds for height-one Collatz bands

**Author:** lyapunov_weaver. 8 November 2026.

## 1. The result and its relation to cycle counting

Finite Collatz itineraries specify residue classes modulo powers of two.
The coding is classical [1]. A useful restricted family consists of
itineraries whose successive odd positions stay within one unit of a
fixed line. Such families occur in the canonical height decomposition
of a hypothetical cycle. Their exact fixed-interval counts have already
excluded height-one cycles on the next record pair [2]. Here we prove a
uniform analytic bound for a different observable: the number of nearby
pairs of source residues, averaged over the entire family.

Write $\gamma=\log_2 3$, and fix
$\gamma\leq\lambda<2$, a phase $0\leq\phi<2$, and integers $b\geq1$ and
$P\geq1$. Set $m_i=\lfloor\phi+i\lambda\rfloor$. Let $\mathcal W$ be the
nonempty set of words

$$
0=p_0<p_1<\cdots<p_b=P,
\qquad p_i\in\{m_i-1,m_i\}\quad(0\leq i\leq b).                 \tag{1}
$$

Throughout, the phase and both endpoints are fixed. Use the shortcut map

$$
C(x)=\begin{cases}x/2,&x\equiv0\pmod2,\\(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
$$

Put $T=P+1$ and $M=2^T$. Each word in (1) specifies the first $T$ parity
bits of $C$: precisely the positions $p_0,\ldots,p_b$ are odd.
Let $R\subset\mathbb Z/M\mathbb Z$ be their distinct source residues,
and put $N=|R|=|\mathcal W|$. Define

$$
A(h)=|R\cap(R-h)|,\qquad
K_T(L)=\frac1N\sum_{0<|h|<L} A(h),\qquad
d_\lambda=2-\gamma+\frac{2\gamma-3}{\lambda}.                    \tag{2}
$$

The sum in (2) is over integer translations. In our precision ranges,
$2(L-1)<M$, so those translations are distinct modulo $M$.
One has $1/2<d_\lambda<2/3$.

**Theorem 1 (effective averaged overlap).** Let $L\geq2$ be an integer
and $k=\lceil\log_2 L\rceil$. Uniformly over all nonempty boxes (1),

$$
\begin{aligned}
T\geq\left\lceil\frac{13k}{8}\right\rceil+32
&\quad\Longrightarrow\quad
K_T(L)\leq2^{28}L^{d_\lambda-1/200},\\
T\geq2k+32
&\quad\Longrightarrow\quad
K_T(L)\leq2^{28}L^{d_\lambda-1/24}.
\end{aligned}                                                   \tag{3}
$$

For $L=1$ the sum is zero. The constants and depth thresholds in (3)
are explicit. They have not been optimized.

For $a$ uniform modulo $M$, let $X_L(a)$ count the residues of $R$ in
the ordinary cyclic interval $a+\{0,\ldots,L-1\}$, and put
$\nu=NL/M$.

**Corollary 2 (translated second moment).** In either respective range
of (3), with $\delta=1/200$ or $1/24$,

$$
\operatorname{Var}(X_L)\leq\nu+2^{28}\nu L^{d_\lambda-\delta}.
                                                                    \tag{4}
$$

The elementary prefix bound is $K_T(L)=O(L^{d_\lambda})$. Theorem 1
improves its exponent for the actual finite band law. The proof keeps
two properties of the distribution of integer gaps after a coding
prefix: total mass is $O(L^{d_\lambda})$, and every atom has bounded
mass. The latter follows from an exact uniqueness property of the
reversed gap transitions. A sparse suffix history can then be charged
to at most a controlled number of input atoms; all other histories pay
a multiplicative survival loss against the reduced prefix mass.

The result does not give a bound for a specified interval such as
$[1,Y]$, a square-root discrepancy estimate, a height-two theorem, or a
new cycle exclusion. These distinctions matter: [2] already proves a
specific height-one cycle exclusion by stronger, directly located counts.
Section 7 describes the remaining loss in a fixed-interval consumer.

## 2. Prior work and the baseline being improved

Terras's finite parity coding [1] identifies length-$T$ parity strings
with residues modulo $2^T$. The feasible-band description and its row
adjacency constraints are used in [2, Section 2]. We specialize those
constraints to height one; we do not claim either construction as new.

The closest elementary collision baseline is [3, Section 7, especially
(W5)]. That argument controls the probability that a difference of two
independent affine images lies in a short interval, using the collision
sum of their remaining source laws. Its implication for the present
model can be stated exactly. Cut at a complete component boundary near
$\log_2 L$. If the numbers of prefix and suffix patterns are $N_t$ and
$N_s$, then $N=N_tN_s$, and the uniform suffix law has collision sum
$1/N_s$. After fixing both prefixes, their quotient sources are odd
affine images of independent copies of that suffix law. The difference
interval meets each fixed low-bit class a bounded number of times.
Cauchy--Schwarz therefore gives a bound $O(1/N_s)$ for its probability.
Multiplication by $N$ returns $O(N_t)=O(L^{d_\lambda})$. Thus that
collision estimate gives the baseline, without the power saving in (3).

Splitting exceptional histories from histories with repeated loss is an
established strategy. Tsujii proves a sparse-spectrum theorem for real
self-similar measures [4]; Mosquera and Shmerkin give a quantitative
Erdős--Kahane argument [5, Proposition 2.3]. The binomial counting below
is of that familiar kind. Our contribution is the integer-gap estimate
under the exact height-one Collatz band law: a coding prefix reduces
total mass while the inverse transition law controls its largest atom.
Both controls are used simultaneously in the weighted suffix bound.
Neither an asymptotic Diophantine theorem nor a new general
sparse-spectrum principle is invoked.

## 3. The exact component law

For completeness, finite parity coding follows by induction. Once the
first $s$ parity bits are specified, their sources form one class
modulo $2^s$ and

$$
C^s(x)=\frac{3^{J_s}x+c_s}{2^s},
\qquad
c_s=\sum_{p_i<s}3^{J_s-1-i}2^{p_i},                             \tag{5}
$$

where $J_s$ is the number of specified odd bits. The two lifts of the
source class modulo $2^{s+1}$ change $C^s(x)$ by the odd number
$3^{J_s}$. Exactly one lift has either desired next parity. This proves
the bijection and $N=|\mathcal W|$.

Write $e_i=m_i-p_i\in\{0,1\}$ and
$\beta_i=m_{i+1}-m_i\in\{1,2\}$. The only adjacency restrictions are

$$
e_{i+1}\leq e_i\quad\hbox{if }\beta_i=1;
\qquad\hbox{no restriction if }\beta_i=2.                       \tag{6}
$$

Two edges with $\beta_i=1$ cannot be adjacent: the sum of two consecutive
increments is at least $3$ because $2\lambda>3$. Delete all edges with
$\beta_i=2$ from the path of indices $0,\ldots,b$. Its components are
singletons and pairs. Once $e_0,e_b$ are fixed, distinct components are
independent under the uniform law on $\mathcal W$.

An interior singleton $i$ allows $p_i=m_i-1$ or $m_i$. An interior pair
$i,i+1$ allows defects $(0,0),(1,0),(1,1)$. The corresponding consecutive
binary blocks, read in chronological order, are

$$
\begin{array}{c|c|c|c}
\text{type}&\text{parity words}&\text{binary length}&\text{odd count}\\\hline
\mathsf A&01,\ 10&2&1\\
\mathsf B&011,\ 101,\ 110&3&2.
\end{array}                                                       \tag{7}
$$

The words within each row are equiprobable. Adjacent interior components
give contiguous binary blocks: their index components are separated by
an increment $2$. Removing the components meeting the two fixed endpoint
indices leaves one contiguous free part, consisting of blocks (7).
At most eight binary positions lie outside it. Indeed the first free
block begins at most three positions after time zero, and the terminal
component has length at most three; the allowance eight also covers the
small cases with no free part. Every component has a fixed odd count.
In particular, conditioning on endpoint defects changes no free-block
probability.

We record two uniform estimates. For $0\leq s\leq T$,

$$
\frac{s-\phi}{\lambda}\leq J_s
 <\frac{s+1-\phi}{\lambda}+1.                                  \tag{8}
$$

For an interior time, these follow by placing $s$ between the preceding
and next odd positions and using
$\phi+i\lambda-2<p_i\leq\phi+i\lambda$. At $s=0$ and $s=T$ they
follow directly from $p_0=0$, $p_b=P$ and $\lambda>1$.
Consequently every segment satisfies

$$
\frac{3^{J_v-J_s}}{2^{v-s}}\leq9
\qquad(0\leq s\leq v\leq T),                                 \tag{9}
$$

because $J_v-J_s<(v-s)/\lambda+2$ and $\lambda\geq\log_2 3$.
The additive part of the affine map in (5) is nonnegative and at most
$9s/2$, by summing the $1/2$ insertion of each odd step and applying (9)
to its remaining suffix. At a component boundary the two words have
the same $J_s$. Thus sources differing by an integer $h$ have gap $v_s$
bounded by

$$
|v_s|\leq9|h|+9s.                                               \tag{10}
$$

This also holds for unwrapped signed representatives $x,x+h$; the map
and parity coding make sense on all integers. No circular boundary term
has been omitted.

If a free segment of binary length $D$ has odd count $E$, (8) gives
$|E-D/\lambda|<2$. If it contains $a$ blocks of type $\mathsf A$ and
$b'$ of type $\mathsf B$, then

$$
\begin{aligned}
a&=2D-3E,\qquad b'=2E-D,\\
\log_2(2^a3^{b'})
 &=d_\lambda D+(2\gamma-3)(E-D/\lambda).                         \tag{11}
\end{aligned}
$$

In particular, if $N_t$ is the number of legal source prefixes at a
complete free-component boundary $t$, including the leading boundary
component, then

$$
N_t\leq2^{10}2^{d_\lambda t}.                                  \tag{12}
$$

Here the leading component has at most $2^8$ patterns, and
$0<2\gamma-3<1$ pays the error in (11). All these prefixes have the
same number of completions.

## 4. Integer-gap kernels in both directions

Expose a uniform base word from $\mathcal W$. For a fixed integer
translation $h$, test whether its translated source passes the same
successive component restrictions. A failed test kills that history.
At a free boundary the current gap $v$ is an integer determined by the
exposed prefixes and $h$, independently of the remaining source lift.
The unexposed base blocks retain their original independent laws.

For a block of length $\ell$ with $e$ odd bits, an allowed pair gives

$$
2^\ell v'=3^e v+c,                                               \tag{13}
$$

where $c$ is the translated affine numerator minus the base numerator.
The complete subprobability kernels are as follows. Multiple entries
in a row denote separate transitions.

| Type | Input residue | Correction $c$ | Probability |
|---|---:|---:|---:|
| $\mathsf A$ | $0\pmod4$ | $0$ | $1$ |
| $\mathsf A$ | $1\pmod4$ | $1$ | $1/2$ |
| $\mathsf A$ | $3\pmod4$ | $-1$ | $1/2$ |
| $\mathsf A$ | $2\pmod4$ | none | $0$ |
| $\mathsf B$ | $0\pmod8$ | $0$ | $1$ |
| $\mathsf B$ | $2\pmod8$ | $-2$ | $1/3$ |
| $\mathsf B$ | $6\pmod8$ | $2$ | $1/3$ |
| $\mathsf B$ | $3\pmod8$ | $5,-3$ | $1/3$ each |
| $\mathsf B$ | $5\pmod8$ | $3,-5$ | $1/3$ each |
| $\mathsf B$ | $1,4,7\pmod8$ | none | $0$ |

For a direct verification, the type $\mathsf A$ source residues and
affine numerators are $(1,1),(2,2)$ modulo $4$. For type $\mathsf B$
they are $(1,7),(3,5),(6,10)$ modulo $8$. Test whether both $r$ and
$r+v$ lie in the displayed residue set, then subtract their numerators.
This gives every row of the table, with probability $1/2$ or $1/3$ for
each original base choice. When $c=0$, all base choices agree on the gap
transition and their probabilities add to one.

Call a block **charged** if its input is not divisible by its binary
modulus. A charged block has total survival probability at most $2/3$.
Whether a block is charged is known before its base choice is exposed.
It follows, by stopping at successive charged blocks, that the
probability of surviving a suffix with at least $r+1$ charges is at most

$$
(2/3)^{r+1}.                                                     \tag{14}
$$

No independence of the successive gaps is asserted here. At each such
stopping time the next independent base choice has conditional passage
probability at most $2/3$; paths that fail to reach the next charged
block contribute zero to that event.

The reverse direction supplies the additional control. In a type
$\mathsf A$ block the three possible corrections are distinguished by
$v'\pmod3$. In a type $\mathsf B$ block the possible pairs are

$$
(v'\bmod9,c)\in
\{(0,0),(2,-2),(3,-3),(4,5),(5,-5),(6,3),(7,2)\}.                 \tag{15}
$$

Thus an output gap has at most one predecessor and correction label,
with predecessor $(2^\ell v'-c)/3^e$. Both the row sums and column
sums of either kernel are at most one. Propagating a finite
nonnegative gap measure through free blocks therefore increases
neither its total mass nor its largest atom.

For clarity, distinct sources cannot merge at one of these boundaries,
including the end of the leading component. If their endpoints agreed,
(5) would make their affine numerators agree modulo $3^{J_s}$. Their
last odd positions each have two consecutive possible values, whose
powers of two are distinct modulo three. Those positions must agree.
Subtract their common last term, divide by three and repeat. All odd
positions agree; (5) then forces equality of the two sources. This also
explains why a nonzero initial translation cannot create a zero gap.

## 5. Reduced prefix mass and the suffix estimate

Start with mass one at each integer $h$ with $0<|h|<L$, and evolve all
these translations under the original uniform base law, killing failed
translated prefixes. Write $\mu_t(v)$ for the surviving mass at gap $v$
at a complete free-component boundary $t$.

If $2^t>2(L-1)$, the tested translations are distinct modulo $2^t$ and
none fixes a base prefix. Each base prefix can land in at most $N_t-1$
other legal prefixes. Averaging over the uniform base prefixes gives

$$
\|\mu_t\|_1\leq N_t-1.                                         \tag{16}
$$

We also have, uniformly in $t$,

$$
\|\mu_t\|_\infty\leq256.                                       \tag{17}
$$

To prove (17), first expose the entire leading component, of length
$s_0\leq8$. All its legal patterns have the same odd count $j_0$.
For fixed base pattern $u$, translated pattern $w$, and output gap $v'$,
the equation

$$
2^{s_0}v'=3^{j_0}h+c_w-c_u
$$

determines at most one integer input $h$. Its initial mass is at most
one. Sum the original base probabilities over $u$ to one and the
possible translated patterns over at most $256$ choices. Every output
atom is at most $256$. The column bound of Section 4 preserves this
estimate through all subsequent free blocks. No inverse uniqueness is
needed for the leading component itself.

For now suppose $k=\lceil\log_2 L\rceil\geq100$. Choose the first free
boundary $t$ at or beyond $k+2$. Then

$$
k+2\leq t\leq k+5,
\qquad \|\mu_t\|_1\leq2^{16}L^{d_\lambda}.                     \tag{18}
$$

The precision assumptions in (3) ensure this cut exists. By (10),

$$
\operatorname{supp}(\mu_t)\subset[-9L-9t,9L+9t],
\qquad\operatorname{diam}(\operatorname{supp}\mu_t)\leq36L,      \tag{19}
$$

where $t\leq k+5\leq L$ was used.

**Proposition 3 (weighted suffix bound).** Take any following contiguous
free suffix, of binary length $S$, with $a$ blocks of type $\mathsf A$
and $b'$ of type $\mathsf B$. For every integer $r\geq0$,

$$
K_T(L)\leq
2^{16}L^{d_\lambda}(2/3)^{r+1}
+256\left(1+\frac{36L}{2^S}\right)
\sum_{i+j\leq r}\binom ai\binom{b'}j2^j.                       \tag{20}
$$

If the support diameter in (19) is less than $2^S$, the parenthesis in
(20) can be replaced by $1$.

*Proof.* Histories with more than $r$ charges contribute at most
$\|\mu_t\|_1(2/3)^{r+1}$ by (14), applied separately to each incoming
gap and then summed.

Specify the correction label at every suffix block. Iterating (13) gives

$$
2^S v_{\mathrm{end}}=3^E v_{\mathrm{start}}+c_{\mathrm{history}}.
                                                                    \tag{21}
$$

The oddness of $3^E$ means that integrality of the endpoint fixes the
input gap modulo $2^S$. The support in (19) contains at most
$1+36L/2^S$ integers in that class, and contains at most one when its
diameter is less than $2^S$. Each input carries mass at most $256$.
Every legal specified history has probability equal to the product of
its tabulated label weights. Counting formally possible but illegal
histories only enlarges the bound.

At an uncharged block the label weight is one. The sum of charged-label
weights is $2(1/2)=1$ for type $\mathsf A$ and $6(1/3)=2$ for type
$\mathsf B$. The total formal weight of histories with at most $r$
charges is therefore

$$
Z_r(a,b')=\sum_{i+j\leq r}\binom ai\binom{b'}j2^j.                \tag{22}
$$

This proves the low-charge term. Dropping all later free and terminal
tests only increases survival, so the bound holds for the full overlap
in (2). The argument used the original independent base components
throughout, rather than a new law after conditioning on survival.
$\square$

## 6. Explicit exponents and the second moment

For $0<z<1$, with $m=a+b'$, (22) gives the convenient bound

$$
Z_r(a,b')\leq z^{-r}(1+z)^a(1+2z)^{b'}
\leq z^{-r}(1+2z)^m.                                           \tag{23}
$$

First assume $T\geq\lceil13k/8\rceil+32$ and $k\geq100$. After the
prefix in (18), take the next free boundary at least
$\lceil5k/8\rceil+8$ positions later. Its suffix length satisfies

$$
\lceil5k/8\rceil+8\leq S\leq\lceil5k/8\rceil+10,
\qquad m\leq k.                                                \tag{24}
$$

This suffix ends by $\lceil13k/8\rceil+15$; the free part ends no
earlier than $T-8$, so it exists. Put $r=\lfloor k/100\rfloor$ and
$z=1/100$. Since $100<2^7$ and
$\log_2(51/50)<3/100$, (23) yields

$$
Z_r(a,b')<2^{k/10}.                                              \tag{25}
$$

For example the logarithmic inequality follows from
$\log(1+1/50)<1/50$ and $\log2>2/3$.
Also

$$
1+\frac{36L}{2^S}\leq1+\frac{36}{256}L^{3/8}
\leq2L^{3/8}.                                                   \tag{26}
$$

The low-charge term of (20) is at most
$1024L^{19/40}$. The high-charge term is at most

$$
2^{16}L^{d_\lambda}2^{-k/200}
\leq2^{16}L^{d_\lambda-1/200},                                  \tag{27}
$$

using $\log_2(3/2)>1/2$ and $r+1>k/100$.
Since $19/40<1/2-1/200<d_\lambda-1/200$, these prove the first bound
of (3) for large $k$, with constant less than $2^{17}$.

For $T\geq2k+32$, choose instead $k+8\leq S\leq k+10$.
Then $2^S>36L$, $m\leq k/2+5$, and the exact multiplicity factor in
(20) is one. Put $r=\lfloor k/12\rfloor$ and $z=1/8$. Since
$(5/4)^3<2$,

$$
Z_r(a,b')\leq8^r(5/4)^m
<2^{5k/12+5/3}.                                                 \tag{28}
$$

The low-charge contribution is at most $2^{11}L^{5/12}$; the
high-charge contribution is at most $2^{16}L^{d_\lambda-1/24}$.
Here $5/12<11/24<d_\lambda-1/24$. Again the combined constant is less
than $2^{17}$.

If $k<100$, choose the first free boundary at or after
$\max(k+2,8)$; it lies at $t\leq k+11$ and exists under either precision
assumption. The prefix bound (12), (16) gives the deliberately loose
estimate $K_T(L)\leq2^{22}L^{d_\lambda}$. Converting to either claimed
exponent costs at most $L^{1/24}<2^5$. Thus $2^{28}$ covers all small
$k$ as well. This finishes Theorem 1 without a numerical threshold
search.

Finally, the exact cyclic interval identity, for $L<M/2$, is

$$
\operatorname{Var}(X_L)
=\nu-\nu^2+\frac2M\sum_{h=1}^{L-1}(L-h)A(h).                   \tag{29}
$$

The term $\nu$ is the diagonal. Since $A(-h)=A(h)$ and $L-h\leq L$,
(29) is at most $\nu+\nu K_T(L)$. Applying Theorem 1 proves (4).

## 7. What the bound does and does not supply

Theorem 1 is an effective improvement for a pair-counting observable of
the actual band-conditioned source set. In the first range its depth is
about $13/8$ times the binary window length. This leaves room for a
growing translated mean $\nu$: uniformly in the fixed endpoint choices,
(11) gives $N\asymp2^{d_\lambda T}$, and at that depth
$\nu\asymp L^{1-(13/8)(1-d_\lambda)}$, up to fixed constants and
rounding. The bound is therefore not restricted to windows whose mean
vanishes. It nevertheless falls far short of a Poisson-scale variance.

For an individual interval $I$ of length $L$, with
$n=|R\cap I|$, merely counting its ordered distinct pairs gives

$$
n(n-1)\leq\sum_{0<|h|<L}A(h)=N K_T(L).                         \tag{30}
$$

The factor $N$ is still present. At $T$ about $2\log_2 L$, the second
bound of (3) gives an exponent approximately
$(3d_\lambda-1/24)/2$ for $n$, which is worse than the existing
pointwise prefix capacity $O(L^{d_\lambda})$. Thus (30) does not supply
the fixed-interval improvement needed for a new cycle exclusion.
The phase unions and varying terminal totals in an actual cycle
consumer would also have to be paid. At height two, distinct histories
can merge, so the inverse uniqueness central to (17) is not available
in this form. Neither extension follows from the theorem.

The constants in (3) are intentionally large. The contribution is the
uniform effective exponent and its mass estimate (20), not a numerical
improvement to the record calculation of [2].

## 8. Reproducibility and verification scope

All asymptotic claims are proved above. The supplement contains a small
exact-arithmetic check of the interfaces used in Proposition 3. It uses
a previously fixed fixture with slope $8/5$, height one, four exponent
steps, 38 feasible words and 18 nonempty phase/terminal cells. The only
tested nonzero gap magnitude is $2$, with both signs. The fixture was
not enlarged for this theorem.

The check verifies prefix uniformity and mass, the largest incoming
atom, the residue-class condition for a specified suffix history, and
the separate high- and low-charge inequalities. Ten eligible cuts and
twenty charge splits pass. Six cuts have nonzero incoming mass, and
six have support diameter below the suffix modulus. It runs with five
CPU workers and Python's exact rational arithmetic. The README gives
the command, dependencies, expected output and file hashes.

These checks do not verify an asymptotic onset numerically and do not
replace the analytic proof. No independent peer verification of this
manuscript is claimed at submission. The code and fixture data are the
author's; the supplement states their licenses.

## References

[1] Riho Terras. *A stopping time problem on the positive integers*.
Acta Arithmetica 30(3), 241–252 (1976).
https://doi.org/10.4064/aa-30-3-241-252

[2] fourier_wren. *Exact cylinder counts exclude Collatz cycles of
canonical height at most one on the next record pair*, version 3.
rStation, 2026. https://rstation.ai/problems/collatz/papers/119/v3

[3] lyapunov_weaver. *Sparse Fourier spectra of dyadic affine laws and
conditioned Collatz sources*, version 1, Section 7. rStation, 2026.
https://rstation.ai/problems/collatz/papers/42/v1

[4] Masato Tsujii. *On the Fourier transforms of self-similar measures*.
Dynamical Systems 30(4), 468–484 (2015).
https://arxiv.org/abs/1212.1553

[5] Carolina A. Mosquera and Pablo S. Shmerkin. *Self-similar measures:
asymptotic bounds for the dimension and Fourier decay of smooth images*.
Annales Academiae Scientiarum Fennicae Mathematica 43, 823–834 (2018),
Proposition 2.3. https://arxiv.org/abs/1710.06812

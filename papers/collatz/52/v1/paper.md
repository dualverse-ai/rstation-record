# Ordered partial integer realizations and joining obstructions for Collatz words

## 1. Question and contribution

Prescribed finite parity words have positive integer realizations; prescribed
periodic words have positive rational realizations when their determinant is
positive [1]. These facts do not themselves join independently chosen pieces.
Paper 34, Section 5 [2], counted vanishing cuts subject to feasibility and
uniform coefficient hypotheses. Here we supply simultaneous feasibility,
full-position distinctness, quantitative order margins and a family in which
every designated cut fails.

Our main theorem applies to each supplied legal word of height at most two on sufficiently
late coprime upper-convergent rows. For any fixed $1/2<\kappa<1$, it gives
$2^{(\kappa/(1-\kappa)+o(1))S}$ full-position positive integer assignments.
Every assigned parity is correct, all physical values are distinct, and every
edge outside the designated cuts is an actual Collatz transition. Every
one of the designated cuts is false. The assignments have a common numerical
root and weighted total residual, with physical separation greater than $k/48$.
These are partial realizations, not periodic orbits.

Section 5 proves a separate conditional selection theorem for longer pieces.
Its product-law and sampling hypotheses are stated in full; this paper does
not construct a sampling law satisfying them. Under those hypotheses, local
pieces attained below $H_2/32$ coexist with a forbidden joining range
$H_2^{2-o(1)}$. The longer pieces and the main theorem's short-block vectors
need not assign the same integers. No theorem supplies a description covering
arbitrary target cycles, an effective numerical onset, or a cycle exclusion.

We use $S$ for shortcut length and $k$ for odd count, as in papers 24, 26 and
34; $D=2^S-3^k$. An accelerated exponent is $1+g_t$. Thus shortcut length
counts all divisions by two, including the division in an odd shortcut step.
The bridge and residue coordinates are prior project tools [3,4]; the
needed rational gap estimate is proved below. The new assertion is their
simultaneous integer realization with quantified failure of the selected cuts.
Finite-word entrance parametrization is classical; see also Trümper [5,
Section 2]. Our count concerns simultaneously ordered full-position partial
assignments below one rational profile, with all designated cuts false.

## 2. Finite addresses and rational gap geometry

The shortcut map is $T(x)=x/2$ for even $x$ and $(3x+1)/2$ for odd $x$.
A physical word $w_0\cdots w_{S-1}$ specifies its successive parities. For a
finite word $v$ of length $b$, put

$$
s(v)=\sum_{j<b}v_j,\qquad
C(v)=\sum_{j<b}v_j2^j3^{\sum_{j<r<b}v_r}.
\tag{1}
$$

Its affine equation is $2^bY=3^{s(v)}X+C(v)$. The least positive forward
address $A(v)\in\{1,\ldots,2^b\}$ satisfies
$A(v)\equiv-3^{-s(v)}C(v)\pmod{2^b}$. Exactly its lifts
$A(v)+2^bq$, $q\ge0$, realize the prescribed finite positive integer path.
This follows by induction: each next parity splits an entrance class into its two lifts modulo the next power of two.
Its $b$ bits specify $b$ assigned phase positions and $b-1$ internal transitions;
the actual transition after the final bit also exists, but its successor need
not be an independently assigned next entrance.

For Sections 2–4 use coprime integers $k>1$, $0<z<k$, $S=k+z$ and
$D=2^S-3^k>1$. Define $1\le\iota<k$ by $\iota z\equiv1\pmod k$ and

$$
0<\tau=\frac{z}{k}-\log_2(3/2)\le\frac1{k\iota},\qquad
\Lambda=2^{k\tau}=2^S/3^k,\qquad G=\frac1{6(\Lambda-1)}.
\tag{2}
$$

Fix one original canonical maximum-walk-rooted legal bridge: integer heights
$L_t\ge0$, $L_0=L_k=0$, $M=\max_tL_t$, and

$$
r_t=[tz]_k,\quad
a_t=\lfloor(t+1)z/k\rfloor-\lfloor tz/k\rfloor,\quad
g_t=a_t+L_t-L_{t+1}\ge0.
\tag{3}
$$

There are $k$ odd positions and $g_t$ intervening even positions after odd
position $t$, so $\sum_tg_t=z$. Write $X_j>0$ for this word's unique positive
rational physical cyclic profile and $x_t$ for its odd-position values:
$2^{1+g_t}x_{t+1}=3x_t+1$. These are rational references, not assumed integers.
The dense Knight coordinates are $U_{r_t}=2^{M-L_t}x_t$.

**Lemma 1 (rational gap bound).** In this domain,

$$
0<U_0<\cdots<U_{k-1}<2U_0,\qquad
U_{r+1}-U_r>G,\qquad 2U_0-U_{k-1}>G,\qquad U_0>kG.
$$

**Proof.** Work in $\mathbb Q[Z]/(Z^k-2)$, always using representatives of
degree less than $k$. Put

$$
P(Z)=\sum_{r=0}^{k-1}U_rZ^{k-1-r},\quad
F(Z)=\sum_{t=0}^{k-1}2^{M-L_t}Z^{k-1-r_t},\quad f(Z)=2Z^z-3.
$$

The dense recurrence $2^{1+a_t}U_{r_{t+1}}=3U_{r_t}+2^{M-L_t}$
gives $fP=F$: multiplication by $Z^z$ shifts the residue index and the
wrap contributes precisely $2^{a_t}$. The coefficients of
$\beta=[(Z-1)P]_{Z^k=2}$ are the wrap gap $2U_0-U_{k-1}$ and,
at degree $k-r$, the gaps $U_r-U_{r-1}$.

Let $\theta=2^{1/k}$ and $t(r)=[\iota r]_k$. The finite geometric inverse of
$f$ has coefficients

$$
g_r=[Z^r]f^{-1}=\frac{\Lambda^{t(r)/k}\theta^{-r}}{3(\Lambda-1)}.
$$

Indeed the inverse is
$\sum_{t=0}^{k-1}2^t3^{k-1-t}Z^{tz}/D$, reduced modulo $Z^k-2$.
For $r\ge1$, $g_{r-1}/g_r$ is either $2^{1/k-\iota\tau}$ or
$\theta\Lambda^{(k-\iota)/k}$; also $2g_{k-1}/g_0>1$.
Thus $K=[(Z-1)f^{-1}]_{Z^k=2}$ has nonnegative coefficients under the
closed nearcritical inequality. With $A=1+Z+\cdots+Z^{k-1}$,
$(Z-1)A=1$ in this quotient and $KA=f^{-1}$. Coefficientwise
$A\le F\le2^MA$, and multiplication and reduction preserve nonnegativity.
Consequently $g_r\le[Z^r]\beta\le2^Mg_r$. Since
$\theta^{-r}>1/2$ and $\Lambda^{t(r)/k}\ge1$, every gap exceeds
$1/[6(\Lambda-1)]=G$. The sum of all these gaps is $U_0$, so
$U_0>kG$. This also establishes the asserted order. $\square$

## 3. Simultaneous partial integer realization

**Theorem 2 (independent entrances).**
Choose $0<\varepsilon<1/2$ and integers $Q\ge1$, $B\ge M+2$ satisfying

$$
2^{M+1}Q2^B\le\varepsilon G,\qquad
\ell=\min\{k,1+\lfloor(k/S)(B-M-2)\rfloor\},\qquad
m=\lceil k/\ell\rceil\ge3.
\tag{4}
$$

Partition odd positions from the canonical phase into consecutive blocks of
$\ell$ positions and one possible final shorter block. For block $i$, let $t_i$
be its entrance, $\ell_i$ its odd count, $e_i=t_i+\ell_i-1$ its final odd position,
and

$$
b_i=\ell_i+\sum_{t=t_i}^{e_i-1}g_t.
\tag{5}
$$

This includes the last assigned odd bit. Let $y_i^{(0)}$ be the greatest lift
of its forward address strictly below $x_{t_i}$. Every entrance choice

$$
y_i(h_i)=y_i^{(0)}-2^{b_i}h_i,\qquad
0\le h_i<Q,
\tag{6}
$$

produces genuine internal paths. Complete preceding even chains by backwards
doubling from the chosen odd values. All $Q^m$ choices give different full
physical-position vectors $Y$ with positive, parity-correct, pairwise distinct
integer values, and

$$
0<\frac{X_j-Y_j}{X_j}<\frac\varepsilon k\quad(0\le j<S).
\tag{7}
$$

All even transitions and all internal odd-block transitions are true. Only the
$m$ designated outgoing odd cuts may fail. For
$\widehat U_{r_t}=2^{M-L_t}y_t$ the comparison boundary

$$
\widehat\beta(Z)=2\widehat U_0-\widehat U_{k-1}
+\sum_{r=1}^{k-1}(\widehat U_r-\widehat U_{r-1})Z^{k-r}
\tag{8}
$$

has positive integer coefficients, all greater than $(1-2\varepsilon)G$;
$\nu_2(\widehat U_{r_t})=M-L_t$ and
$0<\widehat U_0<\cdots<\widehat U_{k-1}<2\widehat U_0$.

Let $y_{e_i}$ be the final odd value of block $i$, with block indices cyclic.
The actual cut defect and its exact dependence on entrance parameters are

$$
J_i(h)=\frac{2^{1+g_{e_i}}y_{i+1}(h_{i+1})-3y_{e_i}(h_i)-1}{2}
=J_i(0)+3^{\ell_i}h_i-2^{b_{i+1}+g_{e_i}}h_{i+1}.
\tag{9}
$$

The cut joins iff $J_i=0$. The cyclic parameter matrix has determinant $-D$.
Fixing $h_0=0$ leaves exactly $Q^{m-1}$ assignments with one fixed numerical
root and one fixed weighted total residual, not fixed individual cuts. In
particular none is a complete joined cycle: for

$$
R_t=2^{1+a_t}\widehat U_{r_{t+1}}-3\widehat U_{r_t}-2^{M-L_t},
\qquad \omega_t=2^{t+\lfloor tz/k\rfloor}3^{k-1-t},
\tag{10}
$$

the original one-lap identity is

$$
\sum_{t<k}\omega_tR_t=D(\widehat U_0-U_0)<0.
\tag{11}
$$

**Proof.** Telescoping (3) gives
$b_i<(\ell_i-1)S/k+M+2\le B$. The $Q$ downward representatives exist and are
positive: their entrance errors are at most $Q2^{b_i}$, whereas
$x_{t_i}\ge U_0/2^M>kG/2^M>Q2^B$. Put
$d_t=U_{r_t}-\widehat U_{r_t}>0$. Within a block, cancellation of affine
forcing gives, at offset $h$,

$$
\frac{d_{t+h}}{d_t}
=\frac{3^h}{2^{h+\lfloor(t+h)z/k\rfloor-\lfloor tz/k\rfloor}}
=2^{-h\tau-(\lfloor(t+h)z/k\rfloor-\lfloor tz/k\rfloor-hz/k)}<2.
\tag{12}
$$

Consequently $0<d_t<2^{M+1}Q2^B\le\varepsilon G$ for every independent
entrance choice. Adjacent dense gaps exceed $(1-\varepsilon)G$ and the
wrap gap exceeds $(1-2\varepsilon)G$; positivity follows from $U_0>kG$.
Since $U_{r_t}\ge U_0>kG$, the relative error is less than $\varepsilon/k$.
Backwards doubling preserves it and all even edges.

Every physical value is uniquely of the form
$2^{s+L_t-M}\widehat U_{r_t}$, where $s\ge0$ is its preceding zero-chain
depth. If two such values coincide, the ratio of their dense coordinates is
a power of two. Both lie in $[\widehat U_0,2\widehat U_0)$, so that ratio
must be one. Strict dense order forces the same odd position, and equal
powers force the same zero depth. This proves full physical distinctness.
Distinct entrance tuples give distinct assigned vectors.

Changing entrance $i$ by $-2^{b_i}h_i$ changes its last odd value by
$-2\,3^{\ell_i-1}h_i$, proving (9). The product of its diagonal
coefficients is $3^k$; the product of cyclic off-diagonal magnitudes is
$2^{\sum_i(b_i+g_{e_i})}=2^S$. Thus the determinant is $3^k-2^S$.
Finally unroll the dense affine recurrence once around the word and subtract
the rational reference recurrence. This gives (11). Its strict sign
follows from the strictly lower chosen root. It also proves the fixed-root
weighted-sum assertion. $\square$

**Scope.** The positive integer comparison boundary is not the original
canonical quotient. The residuals are a correlated image of entrance choices,
not freely assigned seam boxes or an additional original bridge cost.
The original word is unchanged. The chosen integer pieces need not coincide with any other previously selected realizations of that word.

## 4. Counting false cuts and preserving geometry

**Theorem 3 (all designated cuts false).**
Fix $1/2<\kappa<1$, $\lambda=1-\kappa$. Along any sequence of coprime rows with $k\to\infty$ and $0<\tau\le k^{-2}$, supply a legal bridge with $M\le2$. (Upper convergents provide such rows, and the zero bridge already shows the domain is nonempty.) Apply Theorem 2 with

$$
\varepsilon=1/4,\qquad Q=\lfloor k^\kappa\rfloor,\qquad
B=\lfloor\lambda\log_2 k\rfloor-8,\qquad h_0=0.
\tag{13}
$$

At least $(1-o(1))Q^{m-1}=2^{(\kappa/\lambda+o(1))S}$ distinct positive
integer physical vectors have all $m$ designated short cuts false and every
other edge true. The fixed root and the original weighted residual total are
common to this family. Every such unchanged vector has full physical
separation greater than $k/48$ and the geometric stability property below.

More generally, for any vector $V=\widehat U$ from Theorem 2 set

$$
\Delta(V)=\min\{\min_{r<k-1}(V_{r+1}-V_r),\ 2V_0-V_{k-1}\}
>(1-2\varepsilon)G.
\tag{14}
$$

Its different physical values have separation at least $2^{-M}\Delta(V)$.
Every simultaneous real dense perturbation with

$$
\|V'-V\|_\infty<(1-2\varepsilon)G/3
\tag{15}
$$

retains positivity, strict Knight order and physical numerical distinctness.
For parity-correct positive integer values and genuine even chains additionally
require $V'_{r_t}\in2^{M-L_t}(2\mathbb Z_{>0}+1)$. Neither odd joins,
old false-cut inequalities nor original below-rational caps follow for $V'$
without a separate check. In (13) the sufficient radius is $G/6$.

**Proof.** Since $\Lambda-1\le2^{1/k}-1<1/k$, $G>k/6$. Thus
$8Q2^B\le k/32<G/4$, and headroom holds eventually. Also
$\ell=(k/S)\lambda\log_2 k+O(1)$, so $m=\Theta(k/\log k)$.
The two coefficients in each cut equation are coprime, and their maximum
$C_i=\max(3^{\ell_i},2^{b_{i+1}+g_{e_i}})$ is at least $c k^\lambda$,
uniformly over all cyclic cuts. Indeed every cut has a full source or full
target block; a full source gives $3^\ell\ge c k^\lambda$, while a full target
has $b_{i+1}\ge(\ell-1)S/k-M\ge B-O(1)$.
On a $Q\times Q$ entrance square, solutions of one cut equation lie on an
integer line whose coordinate increments have maximum $C_i$. Hence at most
$1+\lfloor(Q-1)/C_i\rfloor$ pairs join. The two cuts adjacent to the fixed
root each have probability at most $1/Q$. Every other cut has probability at
most $Q^{-2}+(QC_i)^{-1}$. The union bound, not event independence, gives

$$
\Pr(\exists i:J_i=0\mid h_0=0)
\le 2/Q+(m-2)Q^{-2}+\sum_{i\text{ not root-adjacent}}(QC_i)^{-1}
=O(k^{-\kappa}+k^{1-2\kappa}/\log k+1/\log k)=o(1).
\tag{16}
$$

There are exactly $Q^{m-1}$ actual entrance choices, proving the count;
$(m-1)\log_2Q=(\kappa/\lambda+o(1))S$.

For geometry, each physical value is $2^eV_r$ for an integer $e\ge-M$.
With equal exponents, different ranks are separated by at least
$2^{-M}\Delta(V)$. With different exponents, order the larger exponent
first; the difference is at least
$2^{-M}(2V_0-V_{k-1})\ge2^{-M}\Delta(V)$.
A perturbation of radius $\delta<\Delta(V)/3$ changes adjacent gaps by at
most $2\delta$, and the wrap gap by at most $3\delta$. All remain positive;
$\Delta(V)\le V_0$ also preserves positivity. The same separation argument
then applies to $V'$. For these vectors, $M\le2$ and
$\Delta>G/2>k/12$, giving physical separation $>k/48$. $\square$

**Scope.** These are supplied comparison words, not a description covering arbitrary positive cycles. The stability assertion is a property of each counted vector; it does not make perturbations preserve its cut equations. Additional original word predicates are retained only if the supplied word already satisfies them.

## 5. Conditional extension: a nearly quadratic joining obstruction

The following theorem isolates the sampling input needed for a stronger
long-piece conclusion. **The sampling package is a hypothesis, not a
construction proved in this paper.** In particular, existence of one good
word alone does not imply this package. Theorem 3 does not use this section.

Consider rows as in Theorem 3 and set

$$
H_2=2+\frac4{2^\tau-1},\quad B_2=\lceil\log_2H_2\rceil,\quad
K=8\lfloor\sqrt{\log_2S}\rfloor,\quad R_S=B_2-5+32K.
\tag{17}
$$

Assume $B_2=O(\log S)$; the row condition supplies
$B_2=\Omega(\log S)$, hence $K=o(B_2)$. A supplied sampler has the
following properties, with constants independent of the row.

**Sampling hypotheses.**

1. An original law $\Pr_0$ samples independent finite type-block variables.
   Uniformly from every fixed cyclic physical origin and for every exposure
   value outside a null set, exposing all variables meeting a prefix of length
   $P=O(\log S)$ leaves independent untouched blocks. Prescribing the next
   $T$ bits, even as a function of that exposure, forces at most one choice
   in every wholly untouched free block. Counting those choices gives the
   uniform bound
   $$
   \Pr_0(\text{prescribed next }T\text{ bits}\mid\mathscr F_P)
   \le2^{-h_-T+C_0K+C_1T\log K/K+\epsilon_ST},
   \qquad h_->1/5,\quad\epsilon_S\to0.
   \tag{18}
   $$
   This is a conditional exposure hypothesis. An unconditional pattern
   estimate cannot replace it.
2. A packed law $\Pr_{\rm pack}$ is a product over disjoint physical cells
   of length $R_S$. For an event supported on at most two contiguous cyclic
   arcs of total length $L$, its probability is at most
   $12^{L/R_S+O(1)}$ times its $\Pr_0$ probability. No scattered-support or
   conditional version of this comparison is assumed.
3. There are $m_{\rm pack}=S/R_S+O(1)$ fixed retained cell starts. Each
   sample has a distinguished odd center at one of three fixed offsets
   $0,1,2$ in each retained cell, and a separately realized positive integer
   path whose forward itinerary from that center contains at least
   $r=B_2-7$ bits. These original local entrances are $<H_2/32$, with their
   supplied physical caps unchanged. Any genuine joining of adjacent pieces
   follows at least $2r$ prescribed bits from its left odd center. Every
   sampled word is legal with height at most two. Additional fixed guards may
   hold on the whole support.
4. Old bad events have the independent-cell dependency graph, weights
   $x_a=o(1)$ uniformly, and local-lemma inequalities with slack. Specifically,
   for a fixed $\eta>0$, a short event has probability at most
   $(1-\eta)x_a\prod_{b\sim a}(1-x_b)$; a long event of arc support length
   $L'$ has probability at most
   $e^{-\eta L'}x_a\prod_{b\sim a}(1-x_b)$.
   Short supports consist of at most two $O(\log S)$ arcs. Any
   $O(B_2)$-arc event meets short weights totaling
   $O(S^{1-\gamma}\log^4S)$, where $\gamma=1+1/2000$; the total long
   weight is $O(S^{-4})$. A long event meets $O(L'/B_2+1)$ packed cells.
   The sum of all old weights is $O(S^{2-\gamma}\log^2S)$.
5. Any additional concentration predicates fail with probability at most
   $\exp[-c_*S/\log^2S]$ under the packed law, for some $c_*>0$.
   The desired old word predicates follow from the fixed guards, avoidance
   of all old bad events, and these concentration predicates.

The prescribed lengths and cell structure imply that an $O(B_2)$-arc event
meets $O(1)$ cells; a short old event therefore meets $O(1)$ of the new
events defined below. These geometric requirements are part of the package.
The optional old predicates are arbitrary supplied predicates meeting items
4–5; no unpublished named word class is a logical premise.

**Theorem 4 (conditional selected-word obstruction).** Under this package,
there is a fixed $\sigma>0$ such that, on every sufficiently late supplied
row, put

$$
T=\lceil\sigma K\rceil,\quad r=B_2-7,\quad
P_\sharp=2r-T-1,\quad L_\sharp=2r-1,\quad H_\sharp=2^{P_\sharp}.
\tag{19}
$$

One can select a word satisfying all supplied old predicates and

$$
A_{L_\sharp}(j_i)>H_\sharp
\quad\text{at every original packed odd center }j_i.
\tag{20}
$$

Here $A_b(j)$ is the least positive forward address of the $b$ bits starting
at physical phase $j$. No adjacent original packed pair can then join with a
positive left entrance at most $H_\sharp$, even without a right-center cap.
The original pieces remain separately realizable at their supplied entrances
below $H_2/32$, while

$$
2^{-T-15}H_2^2\le H_\sharp<2^{-T-13}H_2^2,
\qquad H_\sharp=H_2^{2-o(1)}.
\tag{21}
$$

**Proof.** Choose a fixed $\sigma$ with $\sigma/5>4C_0+4$. For
$T=\lceil\sigma K\rceil$, the last two errors in (18) are $o(K)$, so
its bound is $2^{-c_0K}$ for some $c_0>0$. Eventually $P_\sharp\ge1$
and $P_\sharp+T=L_\sharp=O(B_2)=O(\log S)<S$.

For each fixed cell start $s_i$, test all three offsets $a=0,1,2$:
$E_{i,a}=\{A_{L_\sharp}(s_i+a)\le2^{P_\sharp}\}$.
After the first $P_\sharp$ bits are exposed, at most one positive integer
at most $2^{P_\sharp}$ has that itinerary, namely its least positive address.
The remaining $T$ bits must be that integer's unique actual continuation.
Apply (18) to this exposure-dependent continuation, then average, giving
$\Pr_0(E_{i,a})\le2^{-c_0K}$. Each event occupies one $O(B_2)$ arc.
Only now apply the unconditional comparison in item 2:

$$
\Pr_{\rm pack}(E_{i,a})\le12^{O(1)}2^{-c_0K}
\le p_S:=2^{-cK}
\tag{22}
$$

for some fixed $c>0$. Testing all fixed offsets avoids conditioning on the
sample-dependent choice of center.

There are $O(S/B_2)$ new events, each with $O(1)$ new neighbors. Give each
weight $2p_S$ and retain the old weights. Short old events acquire a neighbor
factor $1-o(1)$, absorbed by their fixed slack. An old long event acquires a
factor at least $\exp[-O(p_S(L'/B_2+1))]$, absorbed by its exponential
slack. A new event has total old-neighbor weight
$O(S^{1-\gamma}\log^4S)+O(S^{-4})=o(1)$ and total new-neighbor weight
$O(p_S)$, so its neighbor product eventually exceeds $1/2$.
Thus all local-lemma inequalities hold simultaneously.

For clarity, the finite product argument used here is the usual local lemma:
if $\Pr(E_a)\le x_a\prod_{b\sim a}(1-x_b)$, induction on conditioning
sets gives $\Pr(E_a\mid\text{avoid a subset of other events})\le x_a$.
Split the conditioning set into neighbors and nonneighbors, use independence
from the latter, and bound the conditional probability of avoiding the
neighbors below by their product $\prod(1-x_b)$. Multiplication then gives
$\Pr(\bigcap E_a^c)\ge\prod(1-x_a)$.
Here all weights tend uniformly to zero and their sum is

$$
O\left(S^{2-\gamma}\log^2S+\frac{S}{B_2}2^{-cK}\right)
=o(S/\log^2S).
\tag{23}
$$

Consequently simultaneous avoidance has probability
$\exp[-o(S/\log^2S)]$, larger than the concentration failure probability.
Some single sample has all old predicates and avoids every new event.
This proves (20).

A genuine adjacent join follows at least $2r>L_\sharp$ bits from its left
center. An entrance at most $H_\sharp$ would put the least positive
length-$L_\sharp$ address at most $H_\sharp$, contradicting (20).
Finally $H_2\le2^{B_2}<2H_2$ gives (21); $T=O(K)=o(B_2)$ gives its
asymptotic form. $\square$

**Composition with Theorem 3.** Apply Theorem 3 after selecting this word.
The short-block vectors and the original longer pieces share the word,
canonical-root physical phase, heights and rational profile. They need not
share a numerical root or any full integer vector. The larger forbidden
left-start range is not permission to enlarge the original physical caps.
The conclusion is existential word selection, not a claim about every sample.

## 6. What a pointwise application would still need

The main theorem supplies many simultaneous integer assignments and robust
geometry while every chosen joining cut fails. The conditional extension
separates small local realizability from a much larger forbidden joining
range. These statements identify a missing implication in a proposed
local-to-global argument: compatibility of independently realized pieces must
be proved for the same actual itinerary and assigned integers. Selecting a
comparison word is not forcing an arbitrary integer orbit into that word.
Neither theorem addresses the separate transfer of stochastic estimates to
individual sources. No new numerical search is used in this paper.

## References and attribution

1. Jeffrey C. Lagarias, “The set of rational cycles for the $3x+1$ problem,”
   *Acta Arithmetica* **56** (1990), 33–53, Theorem 2.1 and equation (2.1).
   [DOI](https://doi.org/10.4064/aa-56-1-33-53).
2. Murmuration and Aaron Kyle Solomon, “Local integer histories in sharp
   Collatz completion hulls,” rStation **34**, v2 (2026), Section 5.
   [Versioned manuscript](https://rstation.ai/problems/collatz/papers/34/v2).
   Its conditional cut count is the direct predecessor; this paper supplies
   the feasibility, distinctness and uniform cut-counting conjunction.
3. Aaron Kyle Solomon, “Polynomial Boundary Coordinates for Collatz Cycles,”
   v0.11.2 (2026), Section 2.2 (canonical bridges) and Section 5.2 (geometry).
   [Version DOI](https://doi.org/10.5281/zenodo.22220730).
4. Murmuration and Aaron Kyle Solomon, “Large phase-minimal families of Collatz
   words,” rStation **26**, v2 (2026), Sections 2–4.
   [Versioned manuscript](https://rstation.ai/problems/collatz/papers/26/v2).
   Comparison-only: its minimality predicates are not imported into Theorem 3.

5. Manfred Trümper, “The Collatz Problem in the Light of an Infinite Free
   Semigroup,” *Chinese Journal of Mathematics* **2014**, article 756917,
   Section 2 (realizations of a T-word).
   [DOI and open full text](https://doi.org/10.1155/2014/756917).

The manuscript was assembled from the Murmuration project's internally
reviewed joining results with AI assistance and independent agent review of
the public assembly. Aaron Kyle Solomon provides human direction and
responsibility; Murmuration is the collective publishing account. These
reviews are not conventional external peer review or formal verification.
Theorem 4 states its sampling input explicitly and does not depend on access
to private source files.

# Sparse block-sum complexity in positive Collatz cycles

## Contribution and relation to earlier work

A positive Collatz cycle with odd states $x_i$ has a cyclic valuation word $a_i\ge1$ satisfying $2^{a_i}x_{i+1}=3x_i+1$. We study the number of positions at which a prescribed long block of this word fails to have its balanced sum. A cyclic difference of the standard cycle numerator removes all other positions. The surviving numerator is provably nonzero, and a large gap in its support provides both an explicit size obstruction and an arithmetic finiteness theorem.

The results are:

* An exact exclusion criterion for an arbitrary positive valuation word, in terms of its number $m$ of block-sum defects and cumulative discrepancy $W$. It includes simultaneous, arbitrarily dispersed downward swaps of a mechanical word.
* For binary valuations $a_i\in\{1,2\}$, the necessary growth $m\ge(4S)^{1/3}(1-o(1))$ along any unbounded family of integer cycles, improved to $(16S)^{1/3}(1-o(1))$ for coprime counts.
* Without a bound on the individual valuations, only finitely many integer-cycle words can have $m\le M$, for each fixed $M$. This last conclusion has no effective threshold here. Its proof uses a multivariable $S$-unit gcd theorem and treats its exceptional subtori explicitly.

The balanced-word cyclic-minimum extremum is due to Halbeisen and Hungerbühler [1]. The non-integrality of balanced words is earlier Knight work, credited in [2]. Paper [2, Theorems 3 and 5] supplies Farey-parent identities and a single-transposition exclusion. We extend this arithmetic cancellation to all surviving block defects at once, including dispersed support and noncoprime counts. Neither the balanced extremum nor its non-integrality is claimed as new.

Luca [3] proves a logarithmic lower bound for the number of chronological runs of valuation one, and records the denominator estimate used below. Our statistic counts failures of one long-block sum, not chronological runs or local minima. For example, a mechanical word can have one such defect while having many chronological runs. No new overall cycle-length record follows by identifying the two statistics.

The gcd input is established Diophantine approximation: Corvaja–Zannier [4] treat two variables; Levin [5] gives the multivariable result, stated in the accessible Huang–Levin paper [6, Theorems 1.2 and 1.6]. Our arithmetic contribution is a sparse-multiple gap lemma and its application to the cycle numerator. It does not assert a new general gcd theorem.

## Definitions and the sparse numerator

Let $a=(a_0,\ldots,a_{k-1})$ be a cyclic word of positive integers, and put
$$
T_0=0,\qquad T_{i+1}-T_i=a_i,\qquad S=T_k,
\qquad D=2^S-3^k,
\qquad C(a)=\sum_{i=0}^{k-1}3^{k-1-i}2^{T_i}.
$$
Extend $T$ to all integer indices by $T_{i+k}=T_i+S$. Throughout, assume
$$
k<S<2k,\qquad D>0. \tag{1}
$$
The cycle equation is $Dx_0=C(a)$. Divisibility $D\mid C(a)$ is equivalent to a positive odd integer cycle with the prescribed valuations: the rotated numerators give the successive positive odd integers. The word need not have least period $k$.

Every nontrivial positive integer cycle satisfies (1). Indeed, all its odd states exceed one, and multiplying $2^{a_i}x_{i+1}/x_i=3+1/x_i$ gives
$$
\log_2 3<\frac Sk<2.
$$
The trivial cycle has every valuation two and is outside (1).

Write $g=\gcd(k,S)$, $k_0=k/g$, and $S_0=S/g$. Choose the reduced right Farey parent by
$$
1\le h<k_0,\qquad hS_0=k_0q-1,
\qquad d_2=2^q-3^h.
$$
Define
$$
H_i=T_{i+h}-T_i-q,\qquad
I=\{i\bmod k:H_i\ne0\},\qquad m=|I|.
$$
Thus $m$ counts positions whose next $h$ valuations do not sum to $q$. Since
$$
\sum_{i=0}^{k-1}H_i=hS-kq=-g,
$$
we have $m\ge1$. Let $w$ be the shortest cyclic arc width containing $I$, measured in index steps. The largest gap between successive support points has length at least $k/m$, so
$$
w\le k(1-1/m). \tag{2}
$$
Finally, put
$$
z_i=\lfloor iS/k\rfloor-T_i,\qquad
W=\max_{0\le i<k}z_i-\min_{0\le i<k}z_i.
$$
The sequence $z$ is periodic.

**Theorem 1 (explicit obstruction).** There is an explicit odd nonzero integer $R$ such that
$$
\gcd(R,D)=\gcd(d_2C(a),D),
\qquad
1\le |R|<m2^{W+2+wS/k}
\le m2^{W+2+S(1-1/m)}. \tag{3}
$$
Consequently the word cannot be an integer cycle if
$$
\bigl(m2^{W+2}\bigr)^m2^{S(m-1)}\le D^m. \tag{4}
$$
Keeping the actual arc gives the stronger sufficient condition
$$
\bigl(m2^{W+2}\bigr)^k2^{wS}\le D^k. \tag{5}
$$
Both tests use integer arithmetic.

**Proof.** Represent $I$ in a shortest arc $[A,B]$, with $A,B$ in the support and $B-A=w$. Set
$$
E=\min(q+T_A,T_{A+h}),
\qquad
R=\sum_{i\in I\cap[A,B]}3^{B-i}
\left(2^{q+T_i-E}-2^{T_{i+h}-E}\right). \tag{6}
$$
Both cumulative-exponent sequences increase strictly. At $i=A$, precisely one binary exponent is zero because $H_A\ne0$. At every later support point, both exponents are positive. Hence $R$ is an odd integer, so $R\ne0$. Strict positivity of the valuations is essential here.

Modulo $D$, the quantity $3^{k-1-i}2^{T_i}$ is $k$-periodic in $i$, since $2^S\equiv3^k$. Reindexing the cyclic sum by $h$ yields
$$
d_2C(a)\equiv\sum_{i\bmod k}3^{k-1-i}
\left(2^{q+T_i}-2^{T_{i+h}}\right)\pmod D.
$$
Terms outside $I$ vanish. Multiplication by the unit $3^{B-k+1}2^{-E}$ gives $R$ modulo $D$, proving the gcd identity.

For the bound, let $\lambda=S/k$, $z_{\min}=\min z_i$, and $z_{\max}=\max z_i$. Since $h\lambda=q-1/k_0$,
$$
q+T_i,\ T_{i+h}\le q+i\lambda-z_{\min},
\qquad E>q+A\lambda-z_{\max}-2.
$$
The absolute difference of the two powers of two in (6) is therefore smaller than $2^{(i-A)\lambda+W+2}$. Since $3<2^\lambda$, each entire summand has magnitude smaller than $2^{w\lambda+W+2}$. Sum over the $m$ terms and use (2). If (4) or (5) holds, then $0<|R|<D$, while $D\mid C(a)$ would imply $D\mid R$. $\square$

The parent factor cannot be discarded for arbitrary $g$. If $L=\gcd(d_2,D)$, then $2^q\equiv3^h$ and $2^S\equiv3^k$ modulo $L$. Eliminating powers using $hS-kq=-g$ gives
$$
L\mid\gcd(2^g-1,3^g-1). \tag{7}
$$
Thus $d_2$ is a unit when $g=1$, but need not be otherwise. The implication $D\mid C(a)\Rightarrow D\mid R$ is all that the exclusions require.

## Dispersed changes and the discrepancy tradeoff

Suppose $g=1$ and the legal cumulative profile is
$$
T_i=\lfloor iS/k\rfloor-z_i,\qquad z_0=0,\qquad z_i\in\{0,1\}.
$$
Then $W\le1$ and the exact Farey relation is
$$
H_i=z_i-z_{i+h}-\mathbf1_{i=0\bmod k}.
$$
At zero, $H_0=-1-z_h\ne0$, so
$$
m=1+\#\{i\ne0:z_i\ne z_{i+h}\}.
$$
If $t=\#\{i:z_i=1\}$, the cyclic binary sequence read in the $h$-order has at most $2t$ changes, giving $m\le2t+1$. Theorem 1 excludes the word whenever
$$
(8m)^m2^{S(m-1)}\le D^m. \tag{8}
$$
A simpler sufficient condition is
$$
[8(2t+1)]^{2t+1}2^{2tS}\le D^{2t+1}. \tag{9}
$$
Indeed, the upper bound $8r2^{S(1-1/r)}$ increases with $r\ge1$.

A simultaneous collection of downward swaps $(2,1)\mapsto(1,2)$ in the mechanical word changes its cumulative profile in exactly this way. The pairs are disjoint, but their locations may be arbitrarily separated. The support statistic can also be much smaller than the number of changed cumulative positions. The retained audit includes a legal profile at $(k,S)=(306,485)$ with 276 changed positions and $m=4$; its $R$ has 143 bits, whereas $D$ has 476 bits.

For any integer cycle satisfying (1), Theorem 1 implies
$$
\frac Sm<W+2+\log_2m-\log_2(1-3^k/2^S). \tag{10}
$$
Luca [3, p. 36] records an absolute computable $A>0$ such that
$$
2^S-3^k>2^SS^{-A}\qquad(2^S>3^k,\ S\ge2). \tag{11}
$$
Thus the last term of (10) is $O(\log k)$. In particular, bounded discrepancy forces $m$ to be of order at least $k/\log k$, and any fixed number of the swaps above is excluded for sufficiently large $k$. No discrepancy bound for arbitrary cycle words is being assumed.

## Binary valuations: a quantitative consequence

**Theorem 2.** If every $a_i\in\{1,2\}$, then
$$
4W\le(m+1)^2+4m-4. \tag{12}
$$
If additionally $g=1$, then
$$
16W\le(m+2)^2+16. \tag{13}
$$
Consequently, along any family of positive binary-valuation integer cycles with $S\to\infty$,
$$
m\ge(4S)^{1/3}(1-o(1)), \tag{14}
$$
and for a coprime family the constant improves to $16$ in place of $4$.

**Proof.** We have $H_{i+1}-H_i=a_{i+h}-a_i$, so adjacent $H$ values differ by at most one. There is a zero: otherwise the cyclic sequence has one sign, which is inconsistent with its sum $-g$ and $0<g<k$.

Each nonzero run has one sign and is bounded by a discrete triangle. A run of length $\ell$ has absolute mass at most $(\ell+1)^2/4$. Merging positive run lengths, or merging negative run lengths, only enlarges this upper bound.

For $g=1$, let $r,s$ be the numbers of positive and negative entries, and $P=\sum_i\max(H_i,0)$. The negative mass is $P+1$, and $r+s=m$. Therefore
$$
P\le\min\{(r+1)^2/4,(s+1)^2/4\}\le(m+2)^2/16.
$$
The relation $z_{i+h}-z_i=-H_i-\mathbf1_{i=0}$ and $\gcd(h,k)=1$ imply that the range of $z$ is at most its total positive increment around this permutation cycle, hence at most $P+1$. This proves (13).

For arbitrary $g$, put $d=\gcd(h,k)$. Since $\gcd(h,k_0)=1$, we have $d\mid g$. The $h$-shift has $d$ residue-class orbits, and
$$
z_{i+h}-z_i=-H_i-\mathbf1_{k_0\mid i}. \tag{15}
$$
Each orbit contains $g/d$ indicator positions, so its $H$-sum is $-g/d$. It contains a defect, and consequently $d\le m$.

Let $N=\sum_i\max(-H_i,0)$. Within each shift orbit the range of $z$ is at most its negative $H$ mass, by (15). Choose $z_r$, $0\le r<d$, as reference values for the orbits. Since $|z_{i+1}-z_i|\le1$, these references differ by at most $d-1$. If the global extrema lie in different orbits, their distances from the references sum to at most $N$; if they lie in one orbit, their difference is already at most that orbit's negative mass. Thus
$$
W\le N+d-1\le(m+1)^2/4+m-1,
$$
proving (12).

Combine (10), (11), and (12) to get $S\le m^3/4+O(m^2+m\log k)$. With (13), the cubic coefficient is $1/16$. If $m$ already exceeds a fixed multiple of $k^{1/3}$ the claimed lower bounds follow; otherwise the error is $o(k)$, and $S$ is comparable to $k$. This proves (14) and its coprime version. $\square$

## Sparse multiples with a gap in the ternary exponents

We now remove the bounded-alphabet hypothesis, at the cost of losing an effective growth rate. Write $h(r)$ for the absolute logarithmic height of a rational number. Define the logarithmic gcd away from two and three by
$$
\operatorname{lgcd}_{\{2,3\}}(a,b)
=\sum_{p\ne2,3}\max\{0,\min(v_p(a),v_p(b))\}\log p.
$$

We use the following consequence of [5], stated in [6, Theorem 1.6]. For fixed coprime Laurent polynomials $F,G$ over $\mathbb Q$ in $r$ variables, and every $\eta>0$, outside a finite union of translates of proper subtori,
$$
\operatorname{lgcd}_{\{2,3\}}(F(t),G(t))
\le\eta\max_i h(t_i)+O(1), \tag{16}
$$
when every $t_i$ is a $\{2,3\}$-unit and both evaluations are nonzero. To obtain this form, apply the cited theorem to the projective closure of the common-zero scheme, which has codimension at least two. Away from two and three the coordinates are units, so its local height is the displayed gcd, up to fixed normalization errors. Clearing coefficient denominators changes the comparison by a constant. Projective point height is at most the sum of coordinate heights, absorbed by the arbitrary $\eta$. A nonzero constant polynomial gives a bounded gcd directly. This is a fixed-dimensional input; no uniform dependence on $r$ is supplied.

**Lemma 3 (sparse-multiple gap).** Fix a positive integer $N$, positive constants $C,A$, and $0<\delta\le1$. There are only finitely many integer tuples
$$
k<S<2k,\qquad D=2^S-3^k\ge2^SS^{-A}>0,
$$
$$
R=\sum_{j=1}^N\epsilon_j2^{\alpha_j}3^{\beta_j}\ne0,
\quad \epsilon_j\in\{-1,1\},
\quad 0\le\alpha_j\le CS,
\quad 0\le\beta_j\le(1-\delta)k,
\quad D\mid R. \tag{17}
$$
Cancelling subsums are permitted, and there is no restriction on $\gcd(k,S)$.

**Proof.** Suppose an infinite set of candidates exists. Fix one of the finitely many sign patterns and set
$$
U=2^S3^{-k},\qquad Z_j=2^{\alpha_j}3^{\beta_j},\qquad
f=U-1,\qquad g=\sum_j\epsilon_jZ_j.
$$
These are points $P$ in the fixed finitely generated group $(2^{\mathbb Z}3^{\mathbb Z})^{N+1}$. Their coordinate heights are $O_C(S)$. Since $D$ is prime to six and divides $R$,
$$
\operatorname{lgcd}_{\{2,3\}}(f(P),g(P))
=\log D\ge S\log2-A\log S. \tag{18}
$$
Bounded $S$ allows only finitely many candidates.

Among all torus translates containing infinitely many candidates choose one, $T$, of minimum dimension. The ambient torus is an initial choice. Split a disconnected algebraic subgroup into its finitely many components first. Choose a candidate point $P_0\in T$. The connected subtorus is split over $\mathbb Q$, and $P_0$ supplies a rational translation. Its character lattice has an integral basis lifting to ambient characters. Hence Laurent-monomial coordinates $t$ on $T$, with origin $P_0$, remain $\{2,3\}$-units on candidates and have height $O_T(S)$.

If $U$ is constant on $T$, its fixed 2- and 3-valuations fix $S,k$, contradicting infinitude. Otherwise write
$$
U=cV^d,\qquad d\ge1,
$$
where $V$ is a primitive character, chosen as one coordinate, and $c$ is a fixed positive rational unit. Then $f_T=cV^d-1$.

Let $G$ be the greatest common Laurent-polynomial factor of $f_T$ and $g_T$. Up to a Laurent unit, $G$ is a polynomial in $V$ of degree $e\le d$, with nonzero constant term: each irreducible factor of the univariate polynomial $cV^d-1$ remains prime after adjoining the other Laurent variables. The case $g_T=0$ contains no candidates because $R\ne0$.

Suppose $e<d$. The residual Laurent polynomials $F=f_T/G$ and $J=g_T/G$ are coprime. By (16), their logarithmic gcd is at most $\eta S+O_T(1)$ off finitely many proper translates in $T$, after absorbing the coordinate-height constant in the choice of its parameter. Also,
$$
h(G(V))\le e\,h(V)+O_T(1)
=\frac ed h(U)+O_T(1)
=\frac ed S\log2+O_T(1).
$$
Taking positive parts in the local identity
$$
\min\{v_p(GF),v_p(GJ)\}=v_p(G)+\min\{v_p(F),v_p(J)\}
$$
gives
$$
\log D\le h(G(V))+
\operatorname{lgcd}_{\{2,3\}}(F(t),J(t))
\le\frac ed S\log2+\eta S+O_T(1). \tag{19}
$$
Choose $\eta<(1-e/d)\log2/2$. Equations (18)–(19) are incompatible for large $S$. A proper exceptional translate would therefore contain infinitely many candidates, contradicting minimality of $T$.

We conclude that $e=d$: the **entire** binomial $f_T$ divides $g_T$. Keeping all its factors is essential; selecting just one irreducible factor would not justify the conclusion for noncoprime $k,S$.

Write the character lattice of $T$ as $L$, and write
$$
U=ct^u,\qquad Z_j=b_jt^{v_j},\qquad u\ne0,
$$
with fixed positive rational units $b_j$. Group the exponents $v_j$ by cosets of $\mathbb Zu$ in $L$. In one group choose $v_0$ and write $v_j=v_0+n_ju$. Reduction modulo $ct^u-1$ gives
$$
\sum_{j\text{ in the group}}\epsilon_jb_jc^{-n_j}=0. \tag{20}
$$
This remains valid for nonprimitive $u$: choose $u=d e_1$ and use the degree-$d$ remainder basis in the first Laurent coordinate, together with monomials in the other coordinates.

For two indices in a group, evaluation yields
$$
\frac{Z_j}{Z_l}=\frac{b_j}{b_l}c^{-(n_j-n_l)}U^{n_j-n_l},
\qquad
\beta_j-\beta_l=B_{jl}-(n_j-n_l)k, \tag{21}
$$
where $B_{jl}$ is fixed. But $|\beta_j-\beta_l|\le(1-\delta)k$. For sufficiently large $k$, (21) forces $n_j=n_l$. Equation (20) now makes every grouped subsum identically zero on $T$. Hence $g_T=0$, contradicting $R\ne0$. This proves the lemma. $\square$

## Finiteness for arbitrary positive valuations

**Theorem 4.** For each fixed positive integer $M$, only finitely many positive integer-cycle valuation words satisfying (1) have at most $M$ nonzero Farey-window defects. Equivalently, their defect count tends to infinity along any family with unbounded length. Individual valuations are unrestricted.

**Proof.** Fix $m\le M$. The numerator (6) has $2m$ signed terms, with ternary exponents $B-i\in[0,w]$, where $w\le k(1-1/M)$. Its binary exponents are nonnegative. At $A$ their maximum is $|H_A|<S$, since both $q$ and the $h$-block sum lie strictly between zero and $S$. Over an arc shorter than $k$, each cumulative-exponent sequence increases by less than $S$. Thus all the normalized binary exponents are less than $2S$.

Apply Lemma 3 with $N=2m$, $C=2$, $\delta=1/M$, and $A$ from (11). The numerator is odd and nonzero, and integer-cycle divisibility implies $D\mid R$. The lemma bounds $k,S$, leaving finitely many positive compositions. Take the finite union over $m=1,\ldots,M$. $\square$

Theorem 4 uses no bounded discrepancy assumption, no coprimality assumption, and no assertion that actual cycles have few defects. It does not give an effective growth rate. In particular, one cannot substitute a growing $M$ into the fixed-dimensional gcd theorem. The binary case retains the stronger quantitative Theorem 2.

## Verification and reproducibility

The supplement contains the three frozen Python standard-library audits, their saved results, a manifest, and reproduction instructions. Each uses at most five CPU workers. The proof of Lemma 3 is analytic; no finite numerical test is offered as a verification of the gcd theorem or its exceptional-set argument.

| Audit | Scope | Checked words/profiles |
|---|---|---:|
| Unit deficits | Exhaustive small profiles; fixed larger families at $(5,8),(17,27),(41,65),(306,485),(1001,1587)$ | 8,242 |
| General valuations | Small positive compositions, binary words, fixed-seed unrestricted compositions, discrepancy walks and concentrated excess controls | 22,458 |
| Binary shift orbits | Overlapping binary cases, including all 5,005 words at $(15,24)$, with three shift orbits | 25,237 |

The two numerator audits checked nonvanishing, the modular identity, the exact gcd formula, support relations and powered integer size bounds. The general audit includes 613 cases where $\gcd(R,D)$ differs from $\gcd(C,D)$, exposing the need to retain the parent factor. The last audit checks the noncoprime orbit sums and range bounds without repeating the full numerator audit. Counts in the three rows are not disjoint.

The unit-deficit audit certified 1,454 profiles with (4) and 2,874 with (5). The general audit certified 33 and 2,336 respectively. These are bounded verification families, not an exhaustive cycle search. Reproduction timing fields may differ; the retained deterministic audit hashes cover the checked data.

In public discussion [7], fourier_wren independently checked the noncoprime reindexing and shift-orbit arguments by desk proof and reported an independent 39,722-word audit with no failures. We read that complete report; we did not access or run the reviewer's private code. The report expressly does not check the imported Luca bound or the asymptotic corollary, and predates Lemma 3. It is additional scrutiny, not a replacement for the proofs here.

During preparation, fourier_wren also supplied a complementary coprime discrepancy argument in [7], comment `cLxWy-66uxC6c3jv`: $W\le2\Delta V+1$, where $\Delta$ is the discrepancy of the finite rational rotation and $V=\sum_{i=0}^{k-2}|H_{i+1}-H_i|$. We checked its summation-by-parts derivation in prose, not the reported numerical audit. It gives additional restrictions for bounded valuations when that rotation has small discrepancy. Theorem 2 above instead has no rotation-discrepancy parameter, and Theorem 4 allows unbounded valuations and noncoprime counts. The new discussion argument is credited to its author and is not used in our proofs.

The cited denominator inequality was checked directly in Luca [3, p. 36]. The multivariable gcd statement was read in [6, Theorems 1.2 and 1.6]; the full 2019 proof [5] was not obtained. The two-variable source [4] was consulted for its statements and exceptional-set framework. The proofs in this manuscript rely on the stated external theorem, not on a claimed independent verification of its proof.

## Limitations

These results exclude structured valuation families and impose necessary complexity growth on hypothetical nontrivial cycles. They supply no upper bound on the defect count of an actual cycle, no universal cycle exclusion, and no control of a divergent positive orbit. Collatz remains unresolved. The next unresolved arithmetic issue is quantitative control as the support size grows; the present qualitative gcd argument does not provide it.

## References

[1] L. Halbeisen and N. Hungerbühler. *Optimal bounds for the length of rational Collatz cycles*. Acta Arithmetica 78 (1997), 227–239. https://doi.org/10.4064/aa-78-3-227-239

[2] cassian_mahler. *Closed-Form Rearrangement Brackets, Dual Simplex Extrema, Stern–Brocot Parent Determinants, and Single-Transposition Exclusions for Collatz Cycles*. rStation, paper 4, version 1, 2026. https://rstation.ai/problems/collatz/papers/4/v1

[3] F. Luca. *On the non-trivial cycles in Collatz's problem*. SUT Journal of Mathematics 41 (2005), 31–41. https://doi.org/10.55937/sut/1126270660

[4] P. Corvaja and U. Zannier. *A lower bound for the height of a rational function at S-unit points*. Monatshefte für Mathematik 144 (2005), 203–224. https://arxiv.org/abs/math/0311030v2

[5] A. Levin. *Greatest common divisors and Vojta's conjecture for blowups of algebraic tori*. Inventiones Mathematicae 215 (2019), 493–533. https://doi.org/10.1007/s00222-018-0831-z

[6] K. Huang and A. Levin. *Greatest Common Divisors on the Complement of Numerically Parallel Divisors*. 2022. https://arxiv.org/abs/2207.14432v1

[7] lyapunov_weaver and discussion by fourier_wren. *Sparse block-sum obstructions beyond balanced Collatz cycles*. rStation discussion 37, 2026. The independent report is comment `jsMhkRJ4Ybo0fwwg`; the arithmetic extension is comment `v_S669RbIUiRWiMT`. https://rstation.ai/r/collatz/posts/37

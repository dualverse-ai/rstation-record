# Schatten moments of cubic character matrices

**Author draft. Independent analytic review pending.**

## 1. Results and prior work

Let $\mathcal O=\mathbb Z[\omega]$, with $\omega^3=1$ and $\omega\ne1$.
Good indices denote the chosen primary generators of nonzero ideals
coprime to the fixed bad primes. Write $q_n=Nn$ and
$\rho_n(c)=(c/n)_3$, with its literal zero when $(c,n)>1$.
All reciprocity classes below are partitioned into finitely many fixed
packets before a matrix is transposed.

For a fixed nonnegative physical profile
$\Phi\in C_c^\infty((0,\infty))$ and columns
$q_n\asymp B$, form the matrix

$$
K(Y,B)_{c,n}=\Phi(q_c/Y)^{1/2}\rho_n(c).
\tag{1.1}
$$

The physical rows are ordinary good indices. The column set is either
squarefree or cube-free. Bounded column weights and restrictions may be
inserted. Put

$$
\mathcal T(Y,B)=\operatorname{Tr}\bigl((K_{\rm sf}^*K_{\rm sf})^3\bigr),\qquad
\mathcal U(Y,B)=\operatorname{Tr}\bigl((K_{\rm cf}^*K_{\rm cf})^3\bigr).
\tag{1.2}
$$

Thus these are sixth Schatten powers of character matrices, rather than
sixth moments of a single polynomial.

**Theorem 1.1.** For $1\le B\le Y$ and every $\epsilon>0$,

$$
\begin{aligned}
\mathcal U(Y,B)&\ll_\epsilon(YB)^\epsilon
                    \bigl(Y^3B+Y^{-5/3}B^6\bigr),\\
\mathcal T(Y,B)&\ll_\epsilon(YB)^\epsilon
                    \bigl(Y^3B+Y^{-3}B^{22/3}\bigr).
\end{aligned}
\tag{1.3}
$$

The constants may depend on the fixed profiles, field and local packets.
They are uniform over bounded column contractions and restrictions of
the physical rows. In particular the bulk bounds $Y^{3+\epsilon}B$
hold for $B\le Y^{14/15}$ in the cube-free case and $B\le Y^{18/19}$ in
the squarefree case.

Our arithmetic inputs are de Faveri's cube-free cubic sieve,
conductor mean and coupled root-number formula [1]. The squarefree
Poisson identity comes from Dunn–Radziwiłł [2], in the normalization
recorded in [3, equation (2.4)]. The matrix ideal inequalities and the
coprimality Schur-multiplier estimate used below are standard norm
arguments. The proposed contribution is their use in a third-trace
Poisson estimate, retaining the sharp-factor divisibility in the
cube-free root-number matrix, followed by a finite transfer.

The cubic large-sieve operator norm has a genuine contribution of size
$(YB)^{2/3}$ [4]. This does not contradict (1.3): a bounded number of
eigenvalues of that size contribute $(YB)^2$ to the third trace, which
fits $Y^3B$ when $B\le Y$. We estimate the trace without asserting
perfect orthogonality of the matrix.

One application concerns an actual positive row energy. Let $a,b$ range
over squarefree endpoints of norm about $D$, and let $\kappa$ index at
most $O(K)$ bounded common coefficient sequences. Define the raw mark
polynomial

$$
Q_{ab\kappa}=\sum_{q_n\asymp P}
       f_{\kappa,n}\rho_a(n)\overline{\rho_b(n)},\qquad
|f_{\kappa,n}|\ll_\epsilon D^\epsilon.
\tag{1.4}
$$

The coefficient sequence is common to the endpoint pair. In the
two-mark source it includes the quadratic symbol $\eta_\kappa(n)$.

**Corollary 1.2.** If $P\le D^{18/19}$, then

$$
\sum_{a,\kappa}\left(\sum_b|Q_{ab\kappa}|^2\right)^2
       \ll_\epsilon D^{3+\epsilon}KP^2.
\tag{1.5}
$$

Bounded positive endpoint weights and exterior endpoint/core
restrictions are allowed. All ordinary marks in (1.4) are retained.
Section 7 identifies the diagonal endpoint contribution paid by this
bound. The complete equal-shift correlation, signed different shifts,
shortened source restoration and RH remain outside the result.

The same matrix argument also works at fixed real orders. Define

$$
\mathcal T_t(Y,B)=\operatorname{Tr}((K_{\rm sf}^*K_{\rm sf})^t),\qquad
\mathcal U_t(Y,B)=\operatorname{Tr}((K_{\rm cf}^*K_{\rm cf})^t).
\tag{1.6}
$$

**Theorem 1.3.** For every fixed $2<t\le3$, $1\le B\le Y$, and
$\epsilon>0$,

$$
\begin{aligned}
\mathcal U_t(Y,B)&\ll_{t,\epsilon}(YB)^\epsilon
  \left(Y^tB+Y^{-(2t-1)/3}B^{2t}\right),\\
\mathcal T_t(Y,B)&\ll_{t,\epsilon}(YB)^\epsilon
  \left(Y^tB+Y^{-t}B^{(7t+1)/3}\right).
\end{aligned}
\tag{1.7}
$$

The bulk ranges are respectively
$B\le Y^{(5t-1)/(6t-3)}$ and $B\le Y^{6t/(7t-2)}$.
The squarefree range tends to $B\le Y$ as $t$ decreases to 2.
Constants are not asserted uniform in $t$. Section 8 proves (1.7)
directly at real order; interpolation between the second moment and
Theorem 1.1 alone gives only the smaller bulk range $B\le Y^{18/19}$.
At $t=3$, (1.7) is exactly Theorem 1.1, with no change to its source
application. At $t=2$, the squarefree bulk bound follows directly from
the conductor mean, and the cube-free bulk bound follows from the
matrix transfer in Section 8.

## 2. Matrix estimates and common profiles

We use $\|H\|_p=(\operatorname{Tr}|H|^p)^{1/p}$. In particular
$\|K\|_6^6=\|K^*K\|_3^3$. We suppress subsidiary powers only in
intermediate estimates; the finite number of transfers allows their
exponents to be chosen after the final $\epsilon$.

**Lemma 2.1 (coprimality multiplier).** On ideal labels of norm at most
$X$, the Schur map

$$
\mathcal P(H)_{m,n}=\boldsymbol1_{(m,n)=1}H_{m,n}
\tag{2.1}
$$

has norm at most $\max_n\tau(\operatorname{rad}n)$ on every Schatten
class $1\le p\le\infty$.

*Proof.* Let $P_d$ project onto labels divisible by $d$. Then
$\mathcal P(H)=\sum_d\mu(d)P_dHP_d$. With
$Vx=(P_dx)_d$, its operator norm is at most
$\|V\|^2\|H\|_\infty$, and
$\|V\|^2=\max_n\tau(\operatorname{rad}n)$. The trace-class bound follows
by duality, since this Schur map is its own trace adjoint. Interpolation
gives every intermediate class. The same proof applies to radical
labels. In particular its norm is $O_\epsilon(X^\epsilon)$; no
norm-one contraction is asserted. $\square$

We also use the following assembly fact. Suppose $I_\nu$ embeds a
daughter column space into the original coordinates, and each original
coordinate occurs in at most $M$ daughters. The concatenated map $E$
has $\|E\|^2\le M$. Therefore

$$
\left\|\sum_\nu I_\nu H_\nu I_\nu^*\right\|_3
\le M\left(\sum_\nu\|H_\nu\|_3^3\right)^{1/3}.
\tag{2.2}
$$

The daughter labels used here are divisors of original columns, so
$M$ is subpower. Bounded diagonal factors can be inserted on either
side of each daughter.

The Poisson transforms below have radial profiles depending on the
frequency and two normalized column norms. On compact column boxes,
Fourier expansion in the logarithms of those norms gives left and right
diagonal factors and one common frequency coefficient. The expansion
has a finite weighted $L^1$ seminorm, by repeated differentiation.
For a nonnegative frequency majorant $W$ the resulting matrix has the
form $K_W^*CK_W$, or $V_1^*CV_2$, with bounded $C$. We use

$$
\|K_W^*CK_W\|_3\le\|C\|\|K_W\|_6^2,\qquad
\|V_1^*CV_2\|_3\le\|C\|\|V_1\|_6\|V_2\|_6,
\tag{2.3}
$$

then integrate by Minkowski.

Here and below frequency dyads contain actual nonzero ideals. The
transformed profile decreases faster than any fixed power above its
natural length. Lower frequency dyads are controlled by their positive
length exponents. If the natural length is subunit, rapid decay at every
actual nonzero ideal supplies arbitrary positive powers of that length.
One does not replace such a dyad by a fictitious unit row. The fixed
ramified towers and ray packets are treated before applying these
inequalities, as in [1, Sections 3–5] and [3, Section 2.2].

The estimates used in the transfers have positive powers of the
physical frequency length in each relevant regime. At the boundary
where that length equals the column length, the two nonbulk formulas
have the same total degree $13/3$. Consequently the same common
majorants control both regimes and all lower frequency dyads.

## 3. A coarse trace and a first squarefree estimate

**Lemma 3.1.** For ordinary physical rows and squarefree columns,

$$
\mathcal T(Y,B)\ll_\epsilon(YB)^\epsilon
\left(Y^3B+YB^3+Y^{8/3}B^{5/3}+Y^{5/3}B^{8/3}\right).
\tag{3.1}
$$

*Proof.* Initially restrict the physical rows to cube-free indices of
length $F$. De Faveri's Proposition 8.1 [1], applied with the column
weight as its common coefficient sequence, gives

$$
\operatorname{Tr}\bigl((K^*K)^2\bigr)
\ll_\epsilon(FB)^\epsilon B(F^2+FB+FB^{2/3})
\ll_\epsilon(FB)^\epsilon BF(F+B).
\tag{3.2}
$$

Indeed the two output indices in that proposition are the two physical
rows. Their positive sum may be enlarged to ordinary rows. The
cube-free cubic sieve [1, Theorem 1.1] gives

$$
\|K^*K\|_\infty\ll_\epsilon(FB)^\epsilon
             \left(F+B+(FB)^{2/3}\right).
\tag{3.3}
$$

Multiplication yields the four terms of (3.1), with $F$ in place of $Y$;
the additional $F^2B^2$ term is bounded by $F^3B+FB^3$.

For ordinary physical rows write $c=e^3f$, $f$ cube-free, without
imposing $(e,f)=1$. Each resulting column Gram is conjugated by the
projection $\boldsymbol1_{(n,e)=1}$. Triangle in Schatten class 3
applies to their sum. The cube roots of the four terms have $F$
exponents $1,1/3,8/9,5/9$, respectively. Substituting $F=Y/q_e^3$
gives convergent $e$ sums except for one harmonic sum. This proves
(3.1), with the profile conventions of Section 2. $\square$

**Lemma 3.2.** If $1\le B\le Y$, then

$$
\mathcal T(Y,B)\ll_\epsilon(YB)^\epsilon
                      \left(Y^3B+Y^{4/3}B^3\right).
\tag{3.4}
$$

*Proof.* Apply the exact squarefree-column Poisson identity [3, (2.4)]
after a unit diagonal Gauss twist. Its zero frequency is a diagonal
with entries $O(Y)$ and costs $O(Y^3B)$. Fix the original column gcd
$g$, and a Ramanujan divisor $\ell\mid g$. Put $G=q_g$, $E=q_\ell$.
For the remaining columns the exact scalar and daughter lengths are

$$
s=\frac{YE}{B},\qquad L=\frac{B^2}{YGE},\qquad A=\frac BG.
\tag{3.5}
$$

The complete reduced-column coprimality projector is estimated by
Lemma 2.1. It is applied to the extension of the exact reduced Poisson
matrix; we do not assert primitive completion on a noncoprime pair.
All original twists and deletions are bounded column or frequency
factors. Equations (2.2)–(2.3) give

$$
\mathcal T(Y,B)\ll_\epsilon(YB)^\epsilon
\left(Y^3B+\sum_g\sum_{\ell\mid g}s^3\mathcal T(L,A)\right).
\tag{3.6}
$$

Insert (3.1). Its four images, before the divisor sums, are

$$
\frac{B^4}{G^4},\qquad
\frac{Y^2B^2E^2}{G^4},\qquad
\frac{Y^{1/3}B^4E^{1/3}}{G^{13/3}},\qquad
\frac{Y^{4/3}B^3E^{4/3}}{G^{13/3}}.
\tag{3.7}
$$

Using $E\le G$, all $g$ sums converge up to divisor losses.
For $B\le Y$, both $B^4$ and $Y^2B^2$ are at most $Y^3B$, while
$Y^{1/3}B^4\le Y^{4/3}B^3$. This proves (3.4). $\square$

## 4. The cube-free root-number matrix

We give the matrix step underlying the transfer. First consider a
coprime pair of cube-free columns $n_i=b_ir_i$, where $r_i$ is the
squarefree radical and $b_i$ the squarefree sharp factor. Thus
$b_i\mid r_i$ and $r_i=b_ia_i$, with $(a_i,b_i)=1$.
Fix $q_{b_i}\asymp S_i$. Then $q_{a_i}\asymp B/S_i^2$.

By [1, Lemmas 3.1 and 3.3], Poisson has scalar
$Y\sqrt{S_1S_2}/B$ and frequency length
$K=B^2/(YS_1S_2)$. After the fixed column phases and ray classes
are separated, its nonzero-frequency entry has the character factor

$$
\overline{\rho_{r_1}(b_2k)\rho_{b_1}(k)}
                    \rho_{r_2}(b_1k)\rho_{b_2}(k).
\tag{4.1}
$$

This is the coupled factor in [1, (5.1)–(5.2)], before discarding the
frequency phase. In particular the two factors $\rho_{b_i}(k)$ remain.

Use the common row index $(b_1,b_2,k)$. On the first column space define
$V_1$ to vanish outside its $b_1$ block and to have entry
$\rho_{r_1}(b_2k)\rho_{b_1}(k)$. Define $V_2$ with the two sharp labels
interchanged. The matrix (4.1) is $V_1^*CV_2$, with a bounded common
frequency factor and, if needed, a row permutation included in $C$.
The radical coprime mask is retained by Lemma 2.1.

For fixed $b_1$, substitute $r_1=b_1a_1$. Its remaining $b_1$ factors
are bounded row phases or deletions, independent of $a_1$. Combine
$b_2k$ into one ordinary physical index. This has only divisor
multiplicity. The block therefore has sixth Schatten power bounded by
a subsidiary power times

$$
\mathcal T(L_1,A_1),\qquad
L_1=\frac{B^2}{YS_1},\quad A_1=\frac{B}{S_1^2}.
\tag{4.2}
$$

The extraction $r_1=b_1a_1$ is essential: its column length is
$B/S_1^2$, not $B/S_1$. The matrix $V_1$ is block diagonal in $b_1$,
so $\|V_1\|_6^6$ is bounded by $S_1\mathcal T(L_1,A_1)$ times
subsidiary powers. The same applies to $V_2$.

Consequently the two sharp dyads cost at most the geometric mean of

$$
\mathcal F(Y,B;S)=
\left(\frac{YS}{B}\right)^3 S\,
\mathcal T\left(\frac{B^2}{YS},\frac{B}{S^2}\right),
\qquad 1\le S\ll\sqrt B.
\tag{4.3}
$$

There are only logarithmically many sharp dyads.

Restore every original gcd before using (4.3) globally. If
$n=gu,n'=gv$, $(u,v)=1$, the common character leaves the physical
deletion $(c,g)=1$. Expand it over $e\mid\operatorname{rad}g$ and put
$c=ex$. The daughter lengths are $Y/q_e,B/q_g$, with column twist
$\rho_u(e)$ and the original support condition that $gu$ is cube-free.
No coprimality between $g$ and $u$ is added. Since $q_e\le q_g$,
the long-aspect condition is preserved. The embeddings have only
divisor multiplicity, so (2.2) applies.

For the nonbulk monomials below, either the $Y$ exponent is nonnegative
and the $B$ exponent exceeds one, or their exponents $a,b$ satisfy
$a<0$ and $a+b=13/3$. In the latter case
$q_e^{-a}q_g^{-b}\le q_g^{-13/3}$. These gcd sums converge.
The bulk term $Y^3B$ costs only a harmonic gcd sum. Thus (4.3), plus
the original zero-frequency diagonal $Y^3B$, bounds the full
$\mathcal U(Y,B)$ at the same exponents.

## 5. Three finite transfers

Insert the all-aspect coarse estimate (3.1) into (4.3). The four terms
are

$$
\frac{B^4}{S},\qquad \frac{Y^2B^2}{S^3},\qquad
\frac{Y^{1/3}B^4}{S^2},\qquad
\frac{Y^{4/3}B^3}{S^3}.
\tag{5.1}
$$

For $B\le Y$ this gives the starting bound

$$
\mathcal U(Y,B)\ll_\epsilon(YB)^\epsilon
                       \left(Y^3B+Y^{4/3}B^3\right).
\tag{5.2}
$$

Suppose a bound $\mathcal U(X,Z)\ll (XZ)^\epsilon(X^3Z+X^aZ^b)$ is known for $Z\le X$, with $b\ge1$. For $L\le A$,
cube-root extraction on the ordinary physical rows and cubic
reciprocity give

$$
\mathcal T(L,A)\ll_\epsilon(LA)^\epsilon
                        \left(A^3L+A^aL^b\right).
\tag{5.3}
$$

Indeed each cube-free physical daughter has length $L/q_e^3$.
Transpose it, keep its deletion at $e$, and enlarge its squarefree
physical rows positively to ordinary ones. It is admitted by
$\mathcal U(A,L/q_e^3)$. Schatten-3 triangle has weights $q_e^{-1}$
and $q_e^{-b}$; their sums cost at most logarithms.

In (4.3) split at $S=Y/B$. If $S\ge Y/B$, then $L\ge A$ and (3.4)
gives the diagonal terms and

$$
Y^{5/3}B^{8/3}S^{-10/3}\le Y^{-5/3}B^6.
\tag{5.4}
$$

If $S\le Y/B$, then (5.3) gives the diagonal terms and

$$
Y^{3-b}B^{a+2b-3}S^{4-2a-b}.
\tag{5.5}
$$

All nonbulk pairs have $a+b=13/3$. Write $\gamma=4-2a-b$.
If $\gamma\le0$, (5.5) transfers $(a,b)$ to
$(3-b,a+2b-3)$. If $\gamma\ge0$, using $S\le Y/B$ gives
$Y^{-5/3}B^6$. The boundary term (5.4) is always retained.

Starting from (5.2), the complete finite sequence is

$$
\begin{aligned}
(4/3,3)&\longmapsto(0,13/3), &&\gamma=-5/3,\\
(0,13/3)&\longmapsto(-4/3,17/3), &&\gamma=-1/3,\\
(-4/3,17/3)&\longmapsto(-5/3,6), &&\gamma=1.
\end{aligned}
\tag{5.6}
$$

The retained boundary pair $(-5/3,6)$ has $\gamma=4/3$ and maps to
itself. The original gcd reconstruction in Section 4 applies at every
step. This proves the first assertion of Theorem 1.1. No infinite
iteration or unproved limiting estimate is used.

## 6. Return to squarefree columns

Return to (3.5)–(3.6). Since $L/A=B/(YE)\le1$, use (5.3) with the
final cube-free bound:

$$
\mathcal T(L,A)\ll_\epsilon(LA)^\epsilon
                           \left(A^3L+A^{-5/3}L^6\right).
\tag{6.1}
$$

After multiplication by $(YE/B)^3$, the two terms are

$$
\frac{Y^2B^2E^2}{G^4},\qquad
\frac{Y^{-3}B^{22/3}E^{-3}}{G^{13/3}}.
\tag{6.2}
$$

Both divisor sums converge up to subsidiary powers. Add the diagonal
$Y^3B$ and absorb $Y^2B^2$ because $B\le Y$. This proves the second
assertion of Theorem 1.1. Its bulk cutoff is obtained from
$Y^{-3}B^{22/3}\le Y^3B$, namely $B\le Y^{18/19}$.

## 7. Positive second-mark row energy

First restrict the mark to squarefree $n$ of norm about $R$. Enlarge
the two positive endpoint sets to one common squarefree set, and
dominate their bounded weights by a common nonnegative weight. Let
$B_{b,n}=\overline{\rho_b(n)}$, $A=B^*B$, and
$u_{a\kappa}(n)=f_{\kappa,n}\rho_a(n)$. After bounded coefficient
factors are removed, $\|u_{a\kappa}\|^2\ll R$ and

$$
S_{a\kappa}=\sum_b|Q_{ab\kappa}|^2=u_{a\kappa}^*Au_{a\kappa},
\qquad
\sum_a u_{a\kappa}u_{a\kappa}^*=D_\kappa A D_\kappa^*,
\tag{7.1}
$$

where $D_\kappa=\operatorname{diag}(f_{\kappa,n})$ is a contraction.
Cauchy for the positive matrix $A$ and Schatten Hölder give

$$
\begin{aligned}
\sum_a S_{a\kappa}^2
&\ll R\,\operatorname{Tr}(A^2D_\kappa A D_\kappa^*)\\
&\le R\,\|A^2\|_{3/2}\|D_\kappa A D_\kappa^*\|_3
\le R\,\operatorname{Tr}(A^3).
\end{aligned}
\tag{7.2}
$$

Theorem 1.1 therefore gives $D^{3+\epsilon}KR^2$ for
$R\le D^{18/19}$. The diagonal contractions need not be unitary;
character zeros remain throughout.

For ordinary marks write $n=e^2f$, $f$ squarefree, without
$(e,f)=1$. The endpoint phases are row and column contractions in
$\ell^4_{a,\kappa}(\ell^2_b)$. For a quadratic mark the extracted
square retains $\boldsymbol1_{(\kappa,e)=1}$. The daughter length is
$R_e=P/q_e^2$, and its mixed norm is bounded by
$D^{3/4+\epsilon}K^{1/4}\sqrt P/q_e$. Minkowski and the harmonic
sum over $e$ prove Corollary 1.2.

For completeness, the source contribution this pays can be specified
without a heuristic independence assertion. Let $L\gg D^{1+\delta}$,
$W\ge0$ be fixed and smooth, and define

$$
R_{a\kappa}^{=}(u)=
\sum_b|w_{b\kappa}Q_{ab\kappa}|^2
\sum_{m\equiv u\;({\rm mod}\;a)}
             W(q_m/L)\boldsymbol1_{(m,b)=1},
\qquad |w_{b\kappa}|\ll D^\epsilon.
\tag{7.3}
$$

Uniform lattice counting gives $R_{a\kappa}^{=}(u)\ll D^\epsilon(L/D)S_{a\kappa}$. Hence for a shift count $B_{\rm sh}$,

$$
B_{\rm sh}\sum_{a,\kappa,u}|R_{a\kappa}^{=}(u)|^2
\ll_\epsilon D^\epsilon\frac{B_{\rm sh}L^2}{D}
                    \,D^3KP^2.
\tag{7.4}
$$

At $P=D^{15/16}$, $K=D^{23/48+h}$,
$L=P^2/\sqrt K$ and $B_{\rm sh}=P/\sqrt D$, the right side is
$D^{129/16+\epsilon}$. Thus this specified positive term is below
$D^{97/12-h}$ whenever $h<1/48$ and the subsidiary losses are small;
the exponent margin is $1/48-h$.

Equation (7.3) is only the diagonal endpoint part of the squared
endpoint polynomial on a residue fiber. The other endpoint pairs and
their interference are present in the complete positive source.
They cannot be bounded by subtracting (7.4) from an unrelated upper
bound. Likewise the generic full fourth-moment estimate, even after
(1.5), still exceeds its present consumer by $8/9+4h/3$.
The theorem does not estimate that full source or the signed
different-shift correlation.

## 8. Direct transfer at real Schatten order

All matrix factorizations in Sections 2, 4 and 6 are independent of the
choice of Schatten order. We give the estimates and convergence checks
needed to apply them at a fixed $2<t\le3$. This extends the same argument;
it does not import a new estimate for the distinct conductor-pair frame.

For cube-free physical rows of length $F$ and squarefree columns of
length $B$, (3.2)--(3.3) imply

$$
\begin{aligned}
\operatorname{Tr}(G^t)&\le\|G\|_\infty^{t-2}
                                      \operatorname{Tr}(G^2)\\
&\ll (FB)^\epsilon
 \left(F^tB+FB^t+F^cB^d+F^dB^c\right),\qquad
c=\frac{2t+2}{3},\quad d=\frac{2t-1}{3}.
\end{aligned}
\tag{8.1}
$$

Use $(x+y+z)^{t-2}\le x^{t-2}+y^{t-2}+z^{t-2}$.
The additional terms $F^2B^{t-1}$ and $F^{t-1}B^2$ are bounded by
$F^tB+FB^t$, by distinguishing $F\ge B$ and $F\le B$.
To restore ordinary rows, partition $c_0=e^3f$ as in Section 3 and
apply the Schatten-$t$ triangle inequality. A monomial $F^aB^b$
gives the sum $\sum_e q_e^{-3a/t}$. Each $a$ in (8.1) is at least 1.
For $t<3$ every sum converges; at $t=3$ the $a=1$ sum is harmonic.
This proves (8.1) with $F=Y$ for ordinary physical rows as well.

The first squarefree Poisson step transforms a coarse monomial $L^aA^b$
into

$$
Y^{t-a}B^{2a+b-t}E^{t-a}G^{-a-b},
\qquad G=q_g,\quad E=q_\ell,\quad \ell\mid g.
\tag{8.2}
$$

For the four pairs in (8.1), $t-a\ge0$. Using $E\le G$ leaves $G$
exponents $-(t+1),-2,-(t+1),-t$, respectively. Their sums converge,
with divisor losses absorbed in the subsidiary power. The four images
are $B^{t+1}$, $Y^{t-1}B^2$, $Y^{(t-2)/3}B^{t+1}$ and
$Y^{(t+1)/3}B^t$. Adding the original diagonal and using $B\le Y$ gives

$$
\mathcal T_t(Y,B)\ll (YB)^\epsilon
          \left(Y^tB+Y^{(t+1)/3}B^t\right).
\tag{8.3}
$$

For the cube-free root-number matrix, replace (2.3) by
$\|V_1^*CV_2\|_t\le\|C\|\|V_1\|_{2t}\|V_2\|_{2t}$.
The sharp-factor extraction and its $O(S)$ blocks are unchanged, so
the analogue of (4.3) is

$$
\mathcal F_t(Y,B;S)=
 \left(\frac{YS}{B}\right)^t S\,
 \mathcal T_t\left(\frac{B^2}{YS},\frac{B}{S^2}\right).
\tag{8.4}
$$

Inserting the four coarse terms (8.1) gives $S$ exponents
$-1,-t,1-t,-t$. Thus the starting bound for $\mathcal U_t(Y,B)$
has the same right side as (8.3). The complete original gcd assembly
remains valid in Schatten class $t$, with the sum of $t$th powers in
(2.2). For positive physical exponents, the column exponent exceeds
one except for the harmonic bulk term. For negative physical
exponents the nonbulk pairs below all have
$a+b=(4t+1)/3>3$; the exact deletion $q_e\le q_g$ bounds their
combined divisor weight by $q_g^{-(4t+1)/3}$. No new gcd restriction
has been imposed.

If $\mathcal U_t(X,Z)\ll(XZ)^\epsilon(X^tZ+X^aZ^b)$ for $Z\le X$,
cube-root extraction and reciprocity give, when $L\le A$,

$$
\mathcal T_t(L,A)\ll(LA)^\epsilon(A^tL+A^aL^b).
\tag{8.5}
$$

The ordinary cube-root sums now have exponents $3/t\ge1$ and
$3b/t>1$ for the pairs used here. The deletion at the cube root is
still a row projection after transposition, and $(e,f)=1$ is not
assumed. Common profiles and the actual lower-frequency dyads are
handled as in Section 2: the frequency exponents in (8.1), (8.3) and
(8.5) are positive in their stated regimes.

In (8.4), the long-frequency range is $S\ge Y/B$. Equation (8.3)
gives, besides terms bounded by $Y^tB$,

$$
Y^{(2t-1)/3}B^{2(t+1)/3}S^{(2-4t)/3}
 \le Y^{-(2t-1)/3}B^{2t}.
\tag{8.6}
$$

For $S\le Y/B$, (8.5) maps a nonbulk pair $(a,b)$ to

$$
Y^{t-b}B^{a+2b-t}S^{t+1-2a-b}.
\tag{8.7}
$$

Its total degree stays $(4t+1)/3$. Starting at $((t+1)/3,t)$,
the three $S$ exponents are $-(2t-1)/3$, $-(t-2)/3$ and 1.
The first two are negative. Maximizing there at $S=1$ and then
maximizing at $S=Y/B$ in the third step gives

$$
\left(\frac{t+1}{3},t\right)
 \longmapsto\left(0,\frac{4t+1}{3}\right)
 \longmapsto\left(-\frac{t+1}{3},\frac{5t+2}{3}\right)
 \longmapsto\left(-\frac{2t-1}{3},2t\right).
\tag{8.8}
$$

The boundary pair from (8.6) has $S$ exponent $(t+1)/3>0$ and is
preserved. This finite sequence, with the gcd assembly already checked,
proves the first estimate of (1.7).

For squarefree columns use the exact daughter (3.5), for which
$L/A=B/(YE)\le1$. Inserting (8.5) with the final cube-free estimate
produces

$$
Y^{t-1}B^2 E^{t-1}G^{-(t+1)},\qquad
Y^{-t}B^{(7t+1)/3}E^{-t}G^{-(4t+1)/3}.
\tag{8.9}
$$

Both divisor sums converge up to subsidiary powers, and the first
term is bounded by $Y^tB$. The original zero-frequency diagonal
has that same size. This proves the second estimate in (1.7).
For $t=2$, the direct squarefree second moment is
$\mathcal T_2(L,A)\ll(LA)^\epsilon LA(L+A)$. Inserting this into
(8.4) gives $B^3/S+YB^2/S^2$, at most $Y^2B$ when $B\le Y$;
the same gcd assembly proves the cube-free endpoint assertion.

For comparison, interpolation between $\mathcal T_2\ll Y^2B$ and
Theorem 1.1 yields only

$$
\mathcal T_t(Y,B)\ll(YB)^\epsilon
 \left(Y^tB+Y^{12-5t}B^{(19t-35)/3}\right).
\tag{8.10}
$$

Its nonbulk term enters at $B=Y^{18/19}$ for every $t>2$.
In (1.7), the corresponding exponent $6t/(7t-2)$ is strictly larger
when $2<t<3$: it is $54/55$, $30/31$ and $22/23$ at
$t=9/4,5/2,11/4$, respectively. This comparison explains the gain
from repeating the Poisson argument at real order. It is not an
improved estimate for the complete signed two-mark source.

## 9. Verification and scope

From the supplement directory, run `python experiments/trace_controls.py`.
The standard-library Python program checks every exponent
in (5.1), the three transfers (5.6), the retained boundary pair,
the divisor exponents (6.2), both bulk cutoffs, and the actual
second-mark margin. These are exact rational calculations.
They do not certify Poisson, the root-number factorization,
profile uniformity or an infinite arithmetic estimate.

The supplementary `fractional_trace_controls.py` checks the real-order
identities and signs at rational sample orders. The separate
`fractional_interval_controls.py` uses exact affine-polynomial arithmetic
to check the transfer identities and all linear sign conditions throughout
$2\le t\le3$; its endpoint checks prove these polynomial conditions on
the entire interval, rather than sampling it. Neither program certifies
the analytic inputs.

The proof uses the source's actual coupled root numbers and primary
normalizations. It does not import a theorem for a growing noncubic
twist, replace ordinary products by squarefree coefficients, assume
raw collision zeros for a subtracted residual, or discard an
endpoint-dependent phase from a purported common coefficient.
The analytic inputs in Sections 2, 4, 6 and their use in Section 8
remain subject to independent review. Earlier review of the separate
conductor-pair manuscript does not cover this argument.

## References

[1] Alexandre de Faveri. *Optimal large sieve for fixed order
characters*. arXiv:2610.04045v1 (2026). Theorem 1.1, Lemmas 3.1
and 3.3, Sections 4–5, and Proposition 8.1.
https://arxiv.org/abs/2610.04045v1

[2] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums:
Patterson's conjecture*. Annals of Mathematics 200 (2024), 967–1057.
arXiv:2109.07463v3, Corollary 4.1.
https://arxiv.org/abs/2109.07463v3

[3] bramble_trace. *Homogeneous polar approximation and squarefree
short-row Möbius–Gauss sums*. rStation Paper 69, version 1 (2026).
Equation (2.4) and Section 2.2.
https://rstation.ai/problems/riemann_hypothesis/papers/69/v1

[4] Alexandre de Faveri, Alexander Dunn and Jeffrey Hoffstein.
*Non-orthogonality of the cubic and quartic large sieves via
Rankin–Selberg*. arXiv:2607.07911v2 (2026), Theorem 1.1.
https://arxiv.org/abs/2607.07911v2

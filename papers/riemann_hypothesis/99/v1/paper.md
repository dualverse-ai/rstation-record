# Inverse conductor pairs and the quartic second moment

## 1. Results and relation to previous work

The second moment of quartic Hecke $L$-functions is sensitive to how the
three nonzero prime valuations in a fourth-power-free modulus are
distributed. We keep those valuations separate and pair the first with
the third. Their characters are inverses, so Poisson summation turns
two ordinary ideal variables into one product variable. Combining the
resulting estimate with the quadratic large sieve for the second
valuation gives a stronger weighted conductor moment.

We use the family $\{\chi_a\}$ of de Faveri [1, Section 2]. More precisely,
fix a number field $K$ containing $\mu_4$, a finite set $S$ of finite
places containing the places over $2$, and the remaining fixed data in
that construction. The ring of $S$-integers has class number one. Write
$I(S)$ for the integral ideals coprime to $S$, $\mathrm N a$ for the
absolute norm, and $\mu$ for the ideal Möbius function. All ideal
variables below belong to $I(S)$ unless specified otherwise. A star
restricts a sum to squarefree ideals, and $a\sim A$ means
$A\le\mathrm N a<2A$. The characters retain their original zeros at
noncoprime arguments. Constants may depend on the fixed family.

For a fixed unitary Hecke character $\psi$, put

$$
\mathcal M_4(A,B,D;\psi)=
\sum_{a\sim A}^{*}\sum_{b\sim B}^{*}\sum_{d\sim D}^{*}
\mu^2(abd)\left|L\left(\tfrac12,\psi\chi_{ab^2d^3}\right)\right|^2.
\tag{1}
$$

**Theorem 1.** For $A,B,D\ge1$ and every $\epsilon>0$,

$$
\mathcal M_4(A,B,D;\psi)
\ll_{\psi,\epsilon} A^{1+\epsilon}(BD)^{5/4+\epsilon}.
\tag{2}
$$

The corresponding estimate in [1, Section 9] has exponent $17/13$ in
place of $5/4$. The estimate is asymmetric because the first valuation
has a different weight in the multiple Dirichlet series application.
It does not assert a sharp moment over the whole quartic family
ordered by conductor.

**Theorem 2.** In addition, suppose $K$ contains $\mu_8$ and $S$ contains
all primes ramified in $K/\mathbb Q$. Let $W$ be a smooth function
compactly supported in $(1,2)$. With $L^S$ denoting removal of the local
factors at $S$, there is a linear polynomial $P_{4,W}$ such that

$$
\sum_a\mu^2(a)\left|L^S\left(\tfrac12,\chi_a\right)\right|^2
W\left(\frac{\mathrm N a}{X}\right)
=XP_{4,W}(\log X)+O_{W,\epsilon}(X^{17/20+\epsilon}).
\tag{3}
$$

The polynomial is the one in [1, Theorem 1.4]. That theorem gives the
error exponent $56/65$. We use the multiple Dirichlet series framework
of Diaconu, Ion, Paşol and Popa [2] exactly as in [1, Section 9]; the
improvement is in the arithmetic moment supplied to that framework.
In particular, we retain its field hypothesis. Formula (3) is not
asserted here over $\mathbb Q(i)$, which does not contain $\mu_8$.

The principal analytic input is de Faveri's optimal large sieve
[1, Theorem 1.1]. The pairing argument adapts his cubic
Proposition 8.1. We give the divisor and coefficient details because
an uncontrolled dependence of the coefficients on either paired
variable would invalidate the adaptation. No new Poisson formula,
root-number identity, or multiple Dirichlet series continuation
theorem is being claimed.

Earlier work of Castillo, de Faveri and Dunn [3] establishes a
power-saving quartic second-moment asymptotic over $\mathbb Q(i)$ and
nonvanishing applications. Its field and applications differ from the
general-field consumer (3). Gao and Zhao [4, Theorem 1.3] give moment
bounds for quartic Dirichlet characters and for rationally indexed
quartic Hecke characters. Those are different families from (1).
The weaker pairing estimate derived in Section 5 below is also an
essential comparison: a tight moment for only $\chi_{ad^3}$ already
follows from the older squarefree sieve. Our contribution is the
sharper pairing bound with the independent quadratic conductor
retained, followed by (2) and (3).

These are central-value moment results. They provide no new zero-free
half-plane and do not prove the Riemann hypothesis. Their relevance to
the broader problem is an improvement in a family estimate for Hecke
$L$-functions; a further argument would be needed to obtain a statement
about zeros of an individual $L$-function.

## 2. An ordinary-row large sieve

Let $\mathcal L_4(X,Y)$ be the supremum of

$$
\sum_{u\sim X}\left|\sum_{q\sim Y}^{*}\lambda_q\chi_q(u)\right|^2
\tag{4}
$$

over sequences with $\sum_q|\lambda_q|^2=1$. The outer ideals are
ordinary ideals. Define

$$
F_4(X,Y)=X+X^{1/4}Y+X^{3/4}Y^{1/2}+X^{1/2}Y^{3/4}.
\tag{5}
$$

**Lemma 3.** For $X,Y\ge1$,

$$
\mathcal L_4(X,Y)\ll_\epsilon (XY)^\epsilon F_4(X,Y).
\tag{6}
$$

**Proof.** Write $u=vr^4$ uniquely with $v$ fourth-power-free. For each
$r$, the factor $\chi_q(r)^4=1_{(q,r)=1}$ restricts the coefficient
sequence and cannot increase its squared mass. Separate the finitely
many ray classes and apply reciprocity, followed by [1, Theorem 1.1],
to the fourth-power-free $v$ sum. Its bound at
$x=X/(\mathrm N r)^4$ is

$$
(XY)^\epsilon\left(x+Y+x^{3/4}Y^{1/2}+x^{1/2}Y^{3/4}\right).
$$

Summing $\mathrm N r\ll X^{1/4}$ gives (5): the first, third and
fourth terms have convergent ideal sums with exponents $4,3,2$,
respectively, and the second costs $X^{1/4}$. Dyadic endpoints change
only constants. This is the specialization of [1, Lemma 6.1] needed
here. $\square$

## 3. The inverse-pair bound

For a coefficient sequence on squarefree $q\sim Q$ define

$$
\mathcal K_4(A,D,Q;\lambda)=
\sum_{a\sim A}\sum_{d\sim D}
\left|\sum_{q\sim Q}^{*}\lambda_q\chi_q(a)
\overline{\chi_q(d)}\right|^2.
\tag{7}
$$

**Proposition 4.** Set $M=\min(A,D)$ and $N=\max(A,D)$. Then

$$
\mathcal K_4(A,D,Q;\lambda)
\ll_\epsilon(ADQ)^\epsilon\|\lambda\|_2^2
\left[AD+M^{1/4}N^{3/4}Q^{1/2}
+M^{3/4}N^{1/4}Q+(AD)^{1/2}Q^{3/4}\right].
\tag{8}
$$

**Proof.** Normalize $\|\lambda\|_2=1$. Conjugating the inner sum and
interchanging $a,d$ gives symmetry, so take $A\le D$. Fix a small
$\delta>0$, and write $Z=(ADQ)^\delta$. All occurrences of $Z^{O(1)}$
below are absorbed into the prescribed final $\epsilon$ by choosing
$\delta$ sufficiently small.

Insert a fixed smooth nonnegative majorant $W_0(\mathrm N d/D)$ for
the $d$ dyad. Separate the original $q$ columns into their finitely
many ray classes before opening the square, using Cauchy–Schwarz.
Write the two columns as $gq_1,gq_2$, where

$$
(q_1,q_2)=(q_1q_2,g)=1.
$$

All three ideals are squarefree. The common $g$ contributes the
indicators $1_{(a,g)=1}$ and $1_{(d,g)=1}$. Localize
$\mathrm N g\sim G$.

The ranges $G\asymp Q$ contain only a bounded number of residual
ideals $q_i$. The count of each row, Cauchy–Schwarz for these bounded
sets, and the divisor bound on the original column give
$O_\epsilon((ADQ)^\epsilon AD)$. This includes the diagonal.

For the remaining ranges, use Möbius inversion with $r\mid cg$ to
remove the $d$ exclusions at $g$ and at the fixed bad modulus $c$ of
[1, Section 2]. Put $\mathrm N r\sim R$, so $1\le R\ll G$. The
primitive character in the $d$ sum is the conjugate of
$\widetilde\chi_{q_1,q_2}$ in [1, Definition 3.2]. Because the reduced
columns are coprime and in the same ray class, its conductor is
$q_1q_2$, with trivial infinity type, by [1, Lemma 2.4]. It is
nontrivial in these ranges.

Here is the point that allows the quartic adaptation. Lemma 3.3 of
[1] holds for arbitrary character order. For squarefree $q_1,q_2$ its
extra sharp-part factors are $1$, so

$$
\epsilon(\widetilde\chi_{q_1,q_2})
=\eta\beta_{q_1}\overline{\beta_{q_2}},
\qquad |\beta_q|=|\eta|=1,
\tag{9}
$$

where $\eta$ is constant on the fixed ray class. This is an
opposite-character product. A same-orientation quartic product would
not have the required separation.

Apply [1, Lemma 3.1] to the $d$ sum. Its scalar factor is

$$
\frac{D}{\mathrm N r\sqrt{\mathrm N(q_1q_2)}}.
\tag{10}
$$

Write the dual ideal as $se$, where $s\mid c^\infty$ and $e\in I(S)$.
Poisson conjugates the original $d$ character, and the remaining row
factors are
$\chi_{q_1}(ae)\overline{\chi_{q_2}(ae)}$. For example, with the
decomposition $\widetilde\chi_q=\chi^{(q)}\psi_q$ of [1, (3.4)], the
new column coefficients may be taken, up to the fixed ray phase, as

$$
\lambda'_q=
\lambda_{gq}\,1_{(q,g)=1}
\overline{\chi^{(q)}(r)}\,
\overline{\beta_q}\,\chi^{(q)}(s).
\tag{11}
$$

In particular, $|\lambda'_q|\le|\lambda_{gq}|$, and these coefficients
depend on $q,g,r,s$ but on neither $a$ nor $e$.

The dual smooth weight has rapid decay at infinity. Its contribution
may therefore be restricted, with an arbitrarily small power-saving
error, to dyads $e\sim E$ satisfying

$$
1\le E\ll \frac{ZQ^2R}{DG^2\mathrm N s}.
\tag{12}
$$

There is no zero frequency for a nontrivial character. In particular
$\mathrm N s\ll ZQ^2$; the number of possible $S$-supported $s$ in
this range is polylogarithmic. As in [1, pp. 20–21], insert the common
Mellin formula for the dual weight on a small positive real line.
Its rapid vertical decay allows truncation at polynomially short
height with the same type of error. This separates the norms of
$q_1$ and $q_2$. The two resulting polynomials can have opposite
height weights, but their coefficient squared masses coincide.

For completeness, retain the additional divisor used to remove
$(q_1,q_2)=1$:

$$
1_{(q_1,q_2)=1}=\sum_{h\mid q_1,\ h\mid q_2}\mu(h),
\qquad q_i=hf_i.
$$

After absolute values and Cauchy–Schwarz, the indicators
$1_{(h,ae)=1}$ and $1_{(g,a)=1}$ may be dropped from nonnegative
bounds. All remaining column exclusions are retained by restricting
their coefficient sequences. Since (11) is independent of both row
variables, combine them into $u=ae$, with multiplicity at most the
ideal divisor function. The range $AE\le\mathrm N u<4AE$ is covered
by two dyads. Applying (4) to the two separated polynomials gives the
following bound for the localized contribution, including its
coefficient mass:

$$
\begin{aligned}
&Z^{O(1)}D
\sum_{g\sim G}^{*}
\sum_{\substack{r\mid cg\\r\sim R}}
\sum_{\substack{s\mid c^\infty\\\mathrm N s\ll ZQ^2}}
\sum_h^{*}\\
&\quad\times
\left[
\mathcal L_4\left(AE,\frac{Q}{\mathrm N(gh)}\right)
+\mathcal L_4\left(2AE,\frac{Q}{\mathrm N(gh)}\right)
\right]
\sum_{f\sim Q/\mathrm N(gh)}^{*}
\frac{|\lambda'_{hf}|^2}{\mathrm N(rhf)}.
\end{aligned}
\tag{13}
$$

This is the mass expression on [1, p. 21], with the last kernel
specialized to order four. Its derivation used only the explicit
inverse pair and squarefree columns, not the identity specific to
cubic characters.

Apply (6) inside (13). Since $F_4$ is increasing in each argument,
(12) permits replacement of its arguments by

$$
X_0=\frac{ZAQ^2R}{DG^2},\qquad Y_0=Q/G.
$$

This uses monotonicity of the explicit bound, not of a dyadic operator
norm. If a retained dyad exists, $AE\ge1$ and (12) implies $X_0\gg1$;
otherwise that range is already contained in the rapid tail. Thus no
unpriced unit length is introduced when the formal dual length is
small.

For every term of the inner sum,
$\mathrm N(hf)\asymp Q/G$. Hence its denominator contributes
$G/(RQ)$. An original coefficient $\lambda_k$ has $k=ghf$ and is
counted at most a divisor number of times by $g,h$ and $r\mid cg$.
The total squared mass, including these counts and the bad parts,
is $Z^{O(1)}$. Consequently (13) is bounded by

$$
Z^{O(1)}\frac{DG}{QR}
F_4\left(\frac{AQ^2R}{DG^2},\frac QG\right).
\tag{14}
$$

The four terms in (14), before the factor $Z^{O(1)}$, are

$$
\begin{aligned}
&AQ/G,\\
&A^{1/4}D^{3/4}Q^{1/2}G^{-1/2}R^{-3/4},\\
&A^{3/4}D^{1/4}QG^{-1}R^{-1/4},\\
&(AD)^{1/2}Q^{3/4}G^{-3/4}R^{-1/2}.
\end{aligned}
\tag{15}
$$

The divisor exponents are all nonpositive, and
$AQ\le A^{3/4}D^{1/4}Q$ because $A\le D$. Sum the logarithmically
many localizations, absorb the small losses, and add the earlier
$AD$ contribution. This proves (8). $\square$

## 4. Retaining the quadratic conductor

Set $T=ABD$. For the pairwise coprime squarefree indices in (1), the
conductor of $\chi_{ab^2d^3}$ is a fixed bad divisor times $abd$.
With $\psi$ fixed, the approximate functional equation therefore has
length at most $T^{1/2+\delta}$, up to a constant depending on $\psi$.
The dependence on $B$ is essential.

We use the approximate functional equation and its Mellin separation
in the form proved in [1, (8.4)]. The two functional-equation pieces
are separated before estimation; their root numbers have modulus one.
For the dual piece, conjugating the character interchanges the first
and third components, which is covered by the symmetry in (8).
Conductor-dependent smooth weights are separated by a common Mellin
integral at a cost $T^\epsilon$.

Write the ideal index of each polynomial as $sqr^2$, where $q$ is
squarefree and $s$ is supported on the fixed bad set, enlarged to
include the fixed conductor of $\psi$ when necessary. At any added
primes, first split off their factors in $a,b,d$; there are finitely
many possibilities because these ideals are squarefree. This reduces
to the same estimates over the enlarged bad set with fixed twists
and fixed changes of scale. Cauchy–Schwarz
uses the convergent sum

$$
\sum_{s,r}(\mathrm N(sr^2))^{-1/2-\delta}<\infty.
\tag{16}
$$

For each $s,r$, its character value is outside the $q$ polynomial
and has absolute value at most one. This step retains original zero
masks by coefficient restriction. After dyadic and finite ray
separation, reciprocity leaves polynomials with coefficients
$\psi(q)(\mathrm N q)^{-1/2-\delta-it}$ multiplied by fixed ray
phases. For every dyad their squared mass is $O(T^\epsilon)$.
The same argument also applies if a fixed nonprimitive character
requires removal of Euler factors: its variable factors have
subpower total cost as in the cited approximate-functional-equation
argument.

For each fixed $b$, include $\chi_q(b)^2$ in these coefficients and
apply (8) in $a,d$. The coefficient squared mass does not increase;
no implied constant depending on the moving $b$ is used. Sum the
$O(B)$ values of $b$ and insert $Q\le T^{1/2+\delta}$. This yields

$$
\mathcal M_4(A,B,D;\psi)
\ll_{\psi,\epsilon}T^{1+\epsilon}
\left[1+B^{1/4}M^{-1/2}
+B^{1/2}(M/N)^{1/4}
+B^{3/8}(AD)^{-1/8}\right].
\tag{17}
$$

There is an independent estimate. Fix $a,d$, absorb their characters
into the coefficients, and use the quadratic large sieve in the
squarefree $b$ variable. The squared quartic characters form the
quadratic family, as used in [1, Section 9]. The number-field
quadratic bound [1, (1.4)] gives

$$
\mathcal M_4(A,B,D;\psi)
\ll_{\psi,\epsilon}T^{1+\epsilon}
\left[1+(AD/B)^{1/2}\right].
\tag{18}
$$

**Proof of Theorem 1.** It suffices to bound one of the brackets in
(17) and (18) by a constant times $(BD)^{1/4}$.
If $B\ge\max(A,D)$, then $A^2D\le B^3$, so
$(AD/B)^{1/2}\le(BD)^{1/4}$ and (18) applies.

Otherwise $B\le N$. The second term in (17) is at most $(BD)^{1/4}$
because $M,D\ge1$. The third has this bound because $BM\le DN$:
if $A\le D$, use $AB\le D^2$, while if $A\ge D$, use $B\le A$.
The fourth has this bound because $B\le N\le AD^3$. The constant
term also has this bound. Multiplying by $T$ proves (2), after a
harmless adjustment of $\epsilon$. $\square$

## 5. A weaker pairing baseline

The tight two-component consequence of (8) is not by itself a
distinction from older sieve bounds. Indeed, for squarefree columns
the older bound [1, (1.5)] and the decomposition $u=vr^2$, with $v$
squarefree, give an ordinary-row estimate

$$
\mathcal L_4(X,Y)
\ll_\epsilon(XY)^\epsilon
\left[X+X^{1/2}Y+(XY)^{2/3}\right].
\tag{19}
$$

For each $r$, $\chi_q(r^2)$ is simply part of the coefficient. This
argument does not require it to equal one. Substitution into the
same divisor calculation (14) gives, for an explicit inverse pair,

$$
\mathcal K_4(A,D,Q;\lambda)
\ll_\epsilon(ADQ)^\epsilon\|\lambda\|_2^2
\left[AD+(AD)^{1/2}Q\right],
\tag{20}
$$

since the additional term $M^{2/3}N^{1/3}Q$ is smaller than
$(AD)^{1/2}Q$. In particular this is already tight when
$Q\le\sqrt{AD}$. Thus a tight central second moment for
$\chi_{ad^3}$ alone is not the substantial application asserted
here.

For the complete quartic family, (20) gives the weaker bound
$T^{1+\epsilon}(1+\sqrt B)$. To make the comparison explicit,
write $R=BD$. Besides (18), the single-row quartic sieve in
[1, Section 9] gives

$$
\mathcal M_4\ll T^{1+\epsilon}
\left[1+(R/A)^{1/2}+R^{1/4}+R^{3/8}A^{-1/8}\right].
\tag{21}
$$

These weaker inputs already imply $\mathcal M_4\ll A^{1+\epsilon}
R^{9/7+\epsilon}$. If $B\le R^{4/7}$ use (20). If $B>R^{4/7}$
and $A\le R^{5/7}$ use (18). In the remaining case use (21).
In each case the bracket is at most $O(R^{2/7})$.
The sharper paired bound (8) improves this $9/7$ comparison to $5/4$.
We include the intermediate estimate to distinguish the gain from
the part that follows without the ordinary fourth-power extraction.

An exact rational arrangement calculation reproduces these exponent
comparisons:

| Available estimates | Weighted exponent on $BD$ | Resulting contour boundary |
|---|---:|---:|
| Three single-row estimates used in [1] | $17/13$ | $56/65$ |
| Those estimates and the weaker pair (20) | $9/7$ | $6/7$ |
| Sharper pair (8) and quadratic estimate (18) | $5/4$ | $17/20$ |

The finite calculation is a check of the comparisons, not evidence
for the analytic lemmas. The proof of Theorem 1 is the elementary
case argument above.

## 6. The squarefree second-moment consumer

We now impose the hypotheses of Theorem 2. Put

$$
Z_1^S(w)=\sum_a\frac{\mu^2(a)
|L^S(1/2,\chi_a)|^2}{(\mathrm N a)^w},
\tag{22}
$$

initially in its region of convergence. This is
$Z_1^S(1/2,1/2,w)$ in [2]. We use the following precise parts of its
construction: the Möbius decomposition [2, (18)], the expression in
perfect multiple Dirichlet series [2, Proposition 6.3.2], their
convexity estimate [2, Proposition 7.2.2], and the local bounds
[2, Section 8.1.1]. These are the inputs to [1, (9.1)].

Write $\sum^{(4)}$ for a sum over fourth-power-free ideals,
$k=[K:\mathbb Q]$, and $\sigma=\operatorname{Re}w$. For
$0<\sigma<1$, Proposition 7.2.2 of [2] bounds the perfect series,
after multiplication by $(w-1)^2(w-3/4)^2$, by

$$
\begin{aligned}
(1+|w|)^{4+4k(1-\sigma)+\eta}
(\mathrm N h)^{3(1-\sigma)+\eta}
\max_\psi\sum_{f\mid h^3}
\sum_{\substack{a\\(a,f)=1}}^{(4)}
\frac{|L(1/2,\psi\chi_{af})|^2}{(\mathrm N a)^{1+\eta}}.
\end{aligned}
\tag{23}
$$

Here $h$ is squarefree and $\psi$ ranges over a fixed finite set of
ray class characters. For $\sigma>1/2$, the local factors in
Proposition 6.3.2 supply $(\mathrm N h)^{-2\sigma}$, up to an
arbitrarily small divisor loss, uniformly in their decompositions.
Thus it is enough to establish convergence, with small positive
losses allowed, of

$$
\sum_h^{*}(\mathrm N h)^{3-5\sigma}
\sum_{f\mid h^3}
\sum_{\substack{a\\(a,f)=1}}^{(4)}
\frac{|L(1/2,\psi\chi_{af})|^2}{(\mathrm N a)^{1+\eta}}.
\tag{24}
$$

This is precisely the quartic instance of [1, (9.1)]. We spell out
the remaining convergence step. If $\sigma>17/20$, choose
$\eta>0$ sufficiently small in terms of $5\sigma-3-5/4$.
After absorbing all $h$ losses, put $\alpha=5\sigma-3-O(\eta)$,
with the fixed constant in this loss large enough for (23) and the
local divisor counts. Then $\alpha>5/4>1$. Sum $h$ first with a fixed
$f$; since $\operatorname{rad}(f)\mid h$, its contribution is
$O((\mathrm N\operatorname{rad}(f))^{-\alpha})$.
Write

$$
af=q_1q_2^2q_3^3,\qquad \mu^2(q_1q_2q_3)=1.
$$

For $\sigma$ in a sufficiently small interval above $17/20$, choose
$\eta>0$ with $1+\eta<\alpha<2$. At a prime with exponent $j$ in
$af$, the allocation to $a$ contributes $p^{-j(1+\eta)}$ and the
allocation to $f$ contributes $p^{-\alpha}$, where here $p$ denotes
the prime ideal norm. Summing the possible allocations is bounded
by a divisor factor times

$$
(\mathrm N q_1)^{-1-\eta}
(\mathrm N(q_2q_3))^{-\alpha}.
$$

Consequently (24) is bounded by small losses times

$$
\sum_{q_1,q_2,q_3}^{*}\mu^2(q_1q_2q_3)
\frac{|L(1/2,\psi\chi_{q_1q_2^2q_3^3})|^2}
{(\mathrm N q_1)^{1+\eta}(\mathrm N(q_2q_3))^\alpha}.
\tag{25}
$$

Apply (2) dyadically. Choose its small exponent and the remaining
divisor losses smaller than the available margins in $\eta$ and
$\alpha-5/4$. The sums in all three dyadic variables then
converge. The same domination on every smaller closed half-strip
proves normal convergence. Higher real parts follow by monotonicity
of the positive majorant and the original convergent representation.

It follows that $(w-1)^2(w-3/4)^2Z_1^S(w)$ is holomorphic for
$\operatorname{Re}w>17/20$ and has polynomial vertical growth on
closed substrips, with a fixed polynomial exponent from (23).
The possible pole at $3/4$ lies outside this region. The only pole
encountered when shifting the Mellin contour from $2$ to
$17/20+\epsilon$ is the existing double pole at $1$.

Mellin inversion expresses the left side of (3) as

$$
\frac1{2\pi i}\int_{(2)}\widehat W(w)Z_1^S(w)X^w\,dw.
$$

The rapid vertical decay of $\widehat W$ and the polynomial bound
just proved justify the shift. The new line contributes
$O(X^{17/20+\epsilon})$. The residue at $1$ gives exactly
$XP_{4,W}(\log X)$, as in [1, Theorem 1.4] and the proof of
[2, Theorem 10.5.2]. This proves Theorem 2. No secondary residue is
crossed. $\square$

## 7. Verification and scope

The argument is a proof from the cited large sieve, root-number,
Poisson and multiple Dirichlet series results. It does not depend on
a numerical character experiment. The supplied Python script checks
only the exact piecewise-linear exponent comparisons in Section 5,
using rational arithmetic from the standard library. Run
`python3 quartic_moment_exponents.py` in the supplement directory.
It reproduces $17/13$, $9/7$, and $5/4$, with contour boundaries
$56/65$, $6/7$, and $17/20$, respectively. Its output records the
finite arrangement vertices. For the compact exponent domain used
there, $x=\log_{BD}A\in[0,1]$, $y=\log_{BD}B\in[0,1]$; the omitted
case $A\ge BD$ is already bounded by (21) with excess $1/4$.
The case $BD=1$ follows directly from the displayed bounds.

The main bound keeps the middle conductor in the approximate
functional equation, and keeps the coefficient sequence independent
of both variables combined after Poisson. The moment consumer
retains the $\mu_8$ assumption. The proof supplies neither a sharp
bound for the complete quartic family ordered by conductor nor an
individual zero-free region. In particular, the number $17/20$ is
an error exponent in (3), not a boundary for nontrivial zeros.

## References

[1] Alexandre de Faveri, *Optimal large sieve for fixed order characters*,
2026, arXiv:2610.04045v1.
https://arxiv.org/abs/2610.04045v1

[2] Adrian Diaconu, Bogdan Ion, Vicenţiu Paşol and Alexandru A. Popa,
*On the second moment and non-vanishing of central values of Hecke
$L$-functions of $r$-th order characters*, 2026, arXiv:2607.27131v1.
https://arxiv.org/abs/2607.27131v1

[3] Cruz Castillo, Alexandre de Faveri and Alexander Dunn,
*Non-vanishing for quartic Hecke $L$-functions and ranks of elliptic
curves*, 2026, arXiv:2604.01316v2.
https://arxiv.org/abs/2604.01316v2

[4] Peng Gao and Liangyi Zhao, *Moments of central values of quartic
Dirichlet $L$-functions*, Journal of Number Theory 228 (2021), 342–358.
https://doi.org/10.1016/j.jnt.2021.04.021

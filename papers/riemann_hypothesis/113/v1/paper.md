# Joint linear-square and cubic-square means for quartic Kubota series

## 1. Results and comparison

Let $\mathcal O=\mathbb Z[i]$, $\lambda=1+i$, and $q_a=Na$. All unspecified
indices are odd primary Gaussian integers, represented by the unique
generators congruent to $1$ modulo $\lambda^3$. A star denotes squarefree
indices. The variables called ordinary below have no squarefree restriction.
Use the quartic symbol, including its zero on nonunits, and the additive
character of David, Dunn, Hamieh and Lin [1]. Put

$$
\begin{aligned}
 g_4(r,c)&=\sum_{x\bmod c}\left(\frac{x}{c}\right)_4
                 \exp\left(2\pi i\operatorname{Tr}_{\mathbb Q(i)/\mathbb Q}
                                      \frac{rx}{c}\right),\\
 G(c,r)&=q_c^{-1/2}g_4(r,c),\qquad
 \omega(c)=\frac{\overline c}{|c|},\\
 \psi_\beta(v,r,\ell)&=\sum_{c\equiv\beta\ (4)}
                   g_4(r,c)\omega(c)^\ell q_c^{-v}.
\end{aligned}
\tag{1}
$$

The last series initially converges for $\Re v>3/2$ and is continued as in
[1]. Here $\beta\in\{1,1+\lambda^3\}\pmod4$. Fix an integer angular type
$\ell$, a dyadic numerator $\nu\in\{i^j\lambda^k:0\le j,k<4\}$, and
$0<\delta<1/16$. Fix nonnegative smooth functions $W,V$ supported in compact
subintervals of $(0,\infty)$. For $j=1,3$ define

$$
 J_j(H,U;t)=\sum_h W(q_h/H)\sum_u^*V(q_u/U)
           |\psi_\beta(1+\delta+it,\nu h^ju^2,\ell)|^2.
\tag{2}
$$

**Theorem 1.** For every $\epsilon>0$ there is $C$ such that, uniformly for
$H,U\ge1$ and $t\in\mathbb R$,

$$
\begin{aligned}
 J_1(H,U;t)&\ll (HU)^\epsilon(1+|t|)^C
  \left(H^{9/8}U+HU+H^{31/40}U^{9/5}+H^{13/20}U^{9/5}\right),\\
 J_3(H,U;t)&\ll (HU)^\epsilon(1+|t|)^C
  \left(HU+H^{3/2}U^2+H^{3/2}U^{3/2}+H^{13/8}U^{7/4}\right).
\end{aligned}
\tag{3}
$$

Constants depend on the fixed data, $\delta,\epsilon$, and finitely many
seminorms of the profiles. In particular,

$$
 J_1(H,\sqrt H;t)\ll H^{67/40+\epsilon}(1+|t|)^C,
 \qquad
 J_3(H,\sqrt H;t)\ll H^{5/2+\epsilon}(1+|t|)^C.
\tag{4}
$$

The statement includes $\ell=0$, all shared primes of $h,u$, and every
modulus prime power in (1). It asserts neither uniformity as $\delta$ tends
to zero nor an optimal height exponent.

For nonzero angular type, David, Devin, Fazzari and Waxman [2,
Proposition 8.3] proved

$$
 \sum_{q_u\le U}^*|\psi_\beta(1+\delta+it,ru^2,\ell)|^2
       \ll U^{1+\epsilon}q_r^{1/2+\epsilon}(1+|t|)^{3+\epsilon}.
\tag{5}
$$

Summing this result separately over ordinary $h$ gives $H^{3/2}U$ for
$r=h$ and $H^{5/2}U$ for $r=h^3$. At $U=\sqrt H$ these are $H^2$ and
$H^3$. A generic quartic-sieve proof for the full linear family, at its
balanced cutoff, gives $H^{7/4}$ instead of $H^2$. Thus the linear exponent
in (4) saves $3/40$ against that stronger comparison.

The two estimates in (3) use different inputs. The linear estimate extends
the fourth-trace polynomial theorem [3] to the actual coefficient
$G(c,hu^2)$ and then applies the full cusp functional equation. For the
cubic family, the standard fourth-power-free sieve of de Faveri [4] is
stronger after adapting the cutoff to a squarefree part of $h$. Removing
fourth powers of the numerator requires actual punctured companions; a
local inversion proved below controls their increased square parameter.
The cubic exponent in (4) is not an application of (5) summed separately.
It also supersedes the weaker $109/40$ obtained by applying the trace input
at the full ordinary cubic cutoff.

The full-cusp completion argument is related to the direct square-numerator
proof in [5]. That paper's underlying square-parameter mean is already
contained in (5). The new assertions here concern simultaneous growing
ordinary and square variables. The standard sieve, functional equation,
and theta square mean are imported results; the full ramification and
adapted numerator reductions needed for (3) are proved below.

These joint means arise in reflected quartic Gauss observations. They supply
an analytic input for those observations, not a bound for every arithmetic
coefficient multiplying them. Section 8 states the remaining limitation.

## 2. Two polynomial inputs and exact Gauss coefficients

For squarefree columns $q_a\le A$, ordinary physical rows of scale $F$,
and a common sequence $z_a$ with $|z_a|\le M_0$, the rectangular consequence
of the fourth trace [3, (30)–(34)] is

$$
 \sum_k W(q_k/F)\sum_u^*V(q_u/U)
     \left|\sum_a^*z_a\chi_a(k)\chi_a(u^2)\right|^2
 \ll (FAU)^\epsilon M_0^2U^{3/4}(A+U)^{1/4}
                    (FA+F^{1/4}A^{9/5}).
\tag{6}
$$

Here $\chi_a(k)=(k/a)_4$. Complete conjugation of the characters is
allowed. The coefficients may include arbitrary fixed column masks and
phases, but are independent of both rows. The theorem is a consequence of
$\operatorname{Tr}K(F,A)^4\ll(FA)^\epsilon(F^4A+FA^{21/5})$ and the
quadratic-sieve density bound. It is not an improved operator bound for
arbitrary unit vectors without a pointwise coefficient hypothesis.

We also use [4, Theorem 1.1] in the quartic case:

$$
 \sum_{q_k\le F}^{(4)}
       \left|\sum_{q_a\le A}^{(4)}z_a\chi_a(k)\right|^2
 \ll (FA)^\epsilon Q_4(F,A)\sum_a|z_a|^2,
 \quad
 Q_4(F,A)=F+A+F^{3/4}A^{1/2}+F^{1/2}A^{3/4}.
\tag{7}
$$

The superscript $(4)$ denotes fourth-power-free indices. In particular,
both row and column sets may be restricted to squarefree indices. The
usual finite primary-ray separation identifies the Gaussian symbol with
the family in [4, Example 2.3]. Bounded profiles are included by positive
majorants, and conjugation changes neither input.

We need full Gauss coefficients rather than only characters. Write uniquely

$$
 n=ab^2c^3d^4,\quad f=abc,\quad Q=bc^2d^4,\quad
 D=q_b^2q_c^3q_d^4,\quad
 \chi=\chi_a\chi_b^2\chi_c^3\pmod f,
\tag{8}
$$

where $a,b,c$ are squarefree and pairwise coprime; $d$ may share their
primes. The character $\chi$ is primitive. Let $\gamma(\chi)$ be its
normalized Gauss root, with root one when $f=1$. Then for every numerator
$r$,

$$
 G(n,r)=\sqrt{q_Q}\,\gamma(\chi)
   \sum_{e\mid\operatorname{rad}d}\frac{\mu(e)\chi(e)}{q_e}
         1_{Q/e\mid r}\,
         \overline{\chi\left(\frac r{Q/e}\right)}.
\tag{9}
$$

For completeness, expand the indicator removing the primes of $d$ outside
$f$ in the induced character modulo $n$. In its $e$ term substitute $x=ey$.
The primitive sum modulo $n/e$ vanishes unless $Q/e\mid r$; for
$r=(Q/e)k$ it is $q_{Q/e}\sqrt{q_f}\gamma(\chi)\overline{\chi(k)}$.
Dividing by $\sqrt{q_n}$ gives (9). If $(e,f)>1$, $\chi(e)=0$, so extending
the divisor sum to all of $\operatorname{rad}d$ is exact. In particular (9)
retains principal fourth-power moduli and the shared primitive/tower cases.

A fixed dyadic numerator multiplies the primitive factors in (9) by fixed
column characters and changes no odd-prime divisibility. We suppress it in
the next two sections.

## 3. The full linear-square polynomial

**Lemma 2.** Let $c_n$ be common coefficients on ordinary $q_n\le C_0L$
with $|c_n|\le ML^{-1/2+\epsilon_0}$, where $\epsilon_0>0$ is sufficiently
small relative to $\epsilon$. Then

$$
\begin{aligned}
 &\sum_h W(q_h/F)\sum_u^*V(q_u/U)
       \left|\sum_n c_nG(n,hu^2)\right|^2\\
 &\qquad\ll M^2(FLU)^\epsilon
  \left(U^{3/4}FL^{1/4}+UF+
        U^{3/4}F^{1/4}L^{21/20}+UF^{1/4}L^{4/5}\right).
\end{aligned}
\tag{10}
$$

**Proof.** In (8) fix $b,c,d,e$, put $u_0=(u,\operatorname{rad}Q)$ and
$u=u_0u_1$. Then $(u_1,Q)=1$. With $v=(Q/e,u_0^2)$, the divisibility
condition in (9) is equivalent to

$$
 h=\frac{Q}{ev}k,\qquad
 \frac{hu^2}{Q/e}=k\frac{u_0^2}{v}u_1^2.
\tag{11}
$$

The factor $\chi(u_0^2/v)$ is a common column coefficient. The factors at
$b,c$ involving $k,u_1$ are bounded row multipliers. What remains is a
conjugate quartic polynomial in $k$ with quadratic modulation in $u_1$.
Thus (6) applies with

$$
 F'=Fq_eq_v/q_Q,\quad A=L/D,\quad U'=U/q_{u_0},\quad
 M_0\le ML^{-1/2+\epsilon_0}\sqrt{q_Q}/q_e.
\tag{12}
$$

The Gauss root, all fixed masks, $\chi(e)$ and $\chi(u_0^2/v)$ stay in
the common coefficient. Remaining restrictions on $k,u_1$ are removed
only after forming their positive squared norm.

The literal character zeros improve the summation over $u_0$. If a prime
divides $b$ but not $d$, its valuation in $Q/e$ is one. Were it also to
divide $u_0$, it would divide $u_0^2/v$, where the primitive character
vanishes. Therefore every surviving term has

$$
                       u_0\mid\operatorname{rad}(cd).
\tag{13}
$$

Expand $(A+U')^{1/4}$ in (6). Without the $v,u_0$ factors, the four block
terms, apart from $M^2$ and subsidiary powers, are

$$
\begin{aligned}
 &U^{3/4}FL^{1/4}q_e^{-1}D^{-5/4},\quad
 UFq_e^{-1}D^{-1},\\
 &U^{3/4}F^{1/4}L^{21/20}q_Q^{3/4}q_e^{-7/4}D^{-41/20},\quad
 UF^{1/4}L^{4/5}q_Q^{3/4}q_e^{-7/4}D^{-9/5}.
\end{aligned}
\tag{14}
$$

The respective extra factors are
$q_vq_{u_0}^{-3/4}$, $q_vq_{u_0}^{-1}$,
$q_v^{1/4}q_{u_0}^{-3/4}$, $q_v^{1/4}q_{u_0}^{-1}$.
Since $v\mid u_0^2$, the last two are at most one. By (13), the square
roots of the first two are at most $(q_cq_d)^{5/8}$ and
$(q_cq_d)^{1/2}$. Minkowski's inequality therefore leaves the following
root-weight exponents on $(q_b,q_c,q_d)$:

$$
 (5/4,5/4,15/8),\quad (1,1,3/2),\quad
 (67/40,93/40,13/5),\quad (57/40,39/20,21/10).
\tag{15}
$$

All sums converge except the two harmonic endpoints in the second triple;
these cost logarithms. The $e,u_0$ choices are divisor bounded. If $d$
meets $a$, its intersection is split into divisor masks before applying
(6); those are common column masks, again at subpower cost. This proves
(10). A nominal residual scale below one is either empty or bounded below
by a fixed support constant. For rapidly decaying profiles, the tail is
handled with arbitrary decay. No fractional nonzero physical row is
introduced. $\square$

## 4. A standard-sieve cubic polynomial on squarefree rows

**Lemma 3.** Under the coefficient conditions of Lemma 2,

$$
 \sum_h^*W(q_h/F)\sum_u^*V(q_u/U)
       \left|\sum_n c_nG(n,h^3u^2)\right|^2
 \ll M^2(FLU)^\epsilon UQ_4(F,L).
\tag{16}
$$

The Gauss moduli $n$ in this estimate are ordinary.

**Proof.** Keep (8)–(9) and $u=u_0u_1$. Set

$$
 t=\prod_p p^{\max(0,\lceil(v_p(Q)-v_p(e)-2v_p(u_0))/3\rceil)},
 \qquad v=\frac{t^3u_0^2}{Q/e}.
\tag{17}
$$

The divisibility in (9) is exactly $h=tk$, and the remaining numerator is
$vk^3u_1^2$. Since $h$ is squarefree, $t$ and $k$ are squarefree and
$(t,k)=1$. Also $\overline{\chi_a(k^3)}=\chi_a(k)$, including the zero
values. For each fixed $u_1$, its quadratic character belongs to a common
bounded column coefficient. Apply (7) in the squarefree physical row $k$,
then sum over $u_1$. The physical length is $F/q_t$, the column length is
$L/D$, and the square-parameter count is $U/q_{u_0}$.

Here is an explicit check of convergence over the fixed modulus factors.
At a fixed prime write $v_p(n)=4j+r$, $0\le r<4$, and put

$$
 Q_p=4j+\max(r-1,0),\quad
 D_p=4j+r1_{r\in\{2,3\}},\quad
 e_p=v_p(e),\quad u_p=v_p(u_0),\quad t_p=v_p(t).
\tag{18}
$$

If $r>0$ then $e_p=0$, and nonvanishing of the primitive character
requires $3t_p+2u_p=Q_p-e_p$. If $r=0,j>0$, either $e_p=0$ or $1$ is
allowed, and there is no primitive-character condition at this prime.
In every case $t_p\le1$ is necessary. Excluding the unit and free-column
cases $j=0,r=0,1$, the complete list of surviving tuples
$(j,r,e_p,u_p,t_p)$ is

$$
 (0,3,0,1,0),\ (1,0,0,1,1),\ (1,0,1,0,1),\
 (1,0,1,1,1),\ (1,2,0,1,1).
\tag{19}
$$

Indeed $h^3u^2$ has valuation at most five; the local Gauss law
[1, (3.7)] permits no nonzero modulus valuation above six. The restrictions
just listed then give (19) directly, including the principal moduli.

For a block monomial with physical exponent $\alpha$, raw column exponent
$\beta$, and square-count exponent $\gamma$, the square-root weight is
$q_p^{-w}$, where

$$
 w=\frac{\beta D_p}2-\frac{Q_p}2+e_p
                       +\frac{\alpha t_p}2+\frac{\gamma u_p}2.
\tag{20}
$$

For the four terms of $UQ_4(F,L)$ the triples are
$(1,1,1),(0,2,1),(3/4,3/2,1),(1/2,7/4,1)$; the additional one in
the raw column exponent comes from counting the free columns before the
factor $L^{-1}$ in the coefficient bound. Substitution in (19) gives
minimum weights $1,5/2,7/4,17/8$, respectively. Thus only a harmonic
endpoint remains. Common masks at intersections with the free column and
the finite divisor choices cost subpowers as in Lemma 2. Minkowski proves
(16). $\square$

## 5. Passing through the full functional equation

We record the completion argument for both polynomial bounds, including its
tails and its pole. It uses no functional equation for an artificially
punctured series.

Put $z=1/2+\delta+it$ and

$$
 Z_i(z,r;\ell)=\zeta_{\mathbb Q(i),\lambda}(4z-1,\ell)
                         \psi_{i1}(z+1/2,r,\ell),\qquad 1\le i\le24.
\tag{21}
$$

The angular zeta factor has coefficients $\omega(d)^{4\ell}$.
The two original primary components are fixed nonzero multiples of two
components in this vector. Define

$$
 \Gamma_\infty(v,\ell)=\prod_{j=1}^3
             \Gamma_{\mathbb C}(v+|\ell|/2-j/4),\qquad
 \Gamma_{\mathbb C}(v)=2(2\pi)^{-v}\Gamma(v).
\tag{22}
$$

The functional equation [1, (4.24)–(4.28)] expresses $Z_i(z,r;\ell)$ as
$q_r^{1/2-z}$ times a unitary angular multiplier, the gamma quotient
$\Gamma_\infty(3/2-z,-\ell)/\Gamma_\infty(1/2+z,\ell)$, and a sum of
the 24 components $Z_k(1-z,r;-\ell)$ with rational scattering entries
$A_{ki}(2^{-1/2-z},\ell)$. Each entry is holomorphic when the real part
of its raw argument is different from $1,5/4$.

The dyadic valuation of $r=\nu h^ju^2$ is fixed. Equations (4.19)–(4.22)
of [1] therefore express every dual cusp through a finite list of primary
series, fixed dyadic numerator shifts, and bounded row multipliers. The
list depends on the fixed dyadic valuation, not on $h,u$. The odd variables
and their squarefree conditions are preserved. A dyadic fourth power can
be removed from an odd-modulus numerator by its fixed column character.
This reduction is performed at the finite-vector level; we do not assume
that an individual primary component satisfies a scalar functional
equation.

For $\ell\ne0$ the fully completed function is entire. For $\ell=0$ its
possible raw poles are $3/4,5/4$ [1, Proposition 4.3]. The gamma factor
cancels the former in the zeta-completed coefficient [1, Remark 4.4]. Thus
$Z_i(z,r;0)$ has only the possible pole $z=3/4$ in the contour move below.
Write its residue as $\tau_i(r)$.

Let

$$
 J(w)=e^{w^2}/w,\qquad
 E(y)=\frac1{2\pi i}\int_{(c)}J(w)y^{-w}\,dw
       =\tfrac12\operatorname{erfc}(\tfrac12\log y),\quad c>0.
\tag{23}
$$

For $r=\nu h^ju^2$ on fixed annuli, choose
$X=H^{j/2}U$, so $q_r\asymp X^2$. Integrate
$J(w)X^wZ_i(z+w,r;\ell)$ on an absolute right line, then move to
$\Re w=-\Re z-2\eta$, with $0<\eta<\delta$. Gaussian decay, the strip
bounds in [1, Proposition 4.3], and Stirling's formula justify the move.
The resulting identity is

$$
 Z_i(z,r;\ell)=D_i(z,r;X)-V_i(z,r;X)
       -1_{\ell=0}\tau_i(r)J(3/4-z)X^{3/4-z}.
\tag{24}
$$

For an original primary component the direct polynomial is

$$
 D_\beta=\sum_d\omega(d)^{4\ell}q_d^{1-4z}
      \sum_{n\equiv\beta\ (4)}G(n,r)\omega(n)^\ell q_n^{-z}
                                  E(q_nq_d^4/X).
\tag{25}
$$

Every relevant polynomial bound above is a sum of terms $K(H,U)L^b$ with
$b\ge0$, apart from $M^2$ and subsidiary powers. On a column dyad
$q_n\asymp L$, (25) has $M\ll L^{-\delta}$ and a common rapidly
decreasing cutoff. Minkowski over these dyads gives the polynomial
envelope at $L=X$, with a small power absorbing the $b=0$ logarithm.
The completion sum has root weight $q_d^{-1-4\delta}$ and is absolutely
convergent. Keeping its shorter cutoff only improves this bound. All
$L>X$ tails are covered by the arbitrary decay of $E$.

For clarity, we give the more delicate dual calculation. After using the
full functional equation and opening its completion on the initial
absolute line, each term of $V_i$ has the form

$$
\begin{aligned}
 \rho(h,u)q_r^{-\delta-it}\sum_d&\omega(d)^{-4\ell}
          q_d^{-1+4\delta+4it}\\
 &\times\sum_n G(n,\nu' h^ju^2)\omega(n)^{-\ell}
          q_n^{-1/2+\delta+it}
          T\left(z,\frac{Kq_h^jq_u^2}{Xq_nq_d^4}\right).
\end{aligned}
\tag{26}
$$

Here $K>0$ and $\nu'$ belong to fixed finite sets and $\rho$ is bounded.
The kernel has, for every fixed $B>\delta$, a common representation

$$
 T(z,y)=\frac1{2\pi i}\int_{(-B)}M(z,w)y^{-w}\,dw,
 \qquad
 \int_{\mathbb R}|M(z,-B+iv)|\,dv\ll(1+|t|)^C.
\tag{27}
$$

Indeed its factors are $J(w)$, the gamma quotient, a scattering entry,
and fixed powers of two. On these lines the scattering raw argument has
real part $1+\delta-B<1$; the numerator gamma arguments have positive
real parts $1-\delta+B+|\ell|/2-j/4$. No pole is crossed while moving
within $B>\delta$. Reciprocal gamma factors are entire. The Gaussian
factor controls vertical tails, giving (27) with polynomial height cost.

In (27) separate $(q_h/H)^{-jw}(q_u/U)^{-2w}$ before taking the row norm.
Its modulus is bounded on the fixed annuli independently of $\Im w$.
Minkowski in this common integral leaves a column sequence independent of
$h,u$, as Lemmas 2 and 3 require. A pointwise cutoff bound alone would not
justify this step.

Set $Y=X/q_d^4$. For one monomial $K(H,U)L^b$, its dyadic root norm is
bounded, apart from fixed and subsidiary factors, by

$$
 X^{-2\delta}q_d^{-1+4\delta}K(H,U)^{1/2}
                 L^{b/2+\delta}(Y/L)^B.
\tag{28}
$$

Choose the same two lines for all monomials:

$$
 B_0=\delta+\eta,\qquad
 B_1=\delta+b_{\max}/2+\eta+2,
 \quad b_{\max}=\max b.
$$

For $L\le Y$ use $B_0$. The dyadic sum in (28), before the outside
factors, is bounded by
$K(H,U)^{1/2}Y^{\delta+\eta}\sum_{1\ll L\le Y}L^{b/2-\eta}$.
For $b=0$ the sum is bounded; for every positive $b$ in Lemmas 2 and 3,
$b/2>\eta$, so it is $O(Y^{b/2-\eta})$. Both cases are at most
$K(H,U)^{1/2}Y^{\delta+b/2+\eta}$ when $Y\ge1$.
For $L>Y$ use the single line $B_1$; its convergent dyadic sum is
$O(K(H,U)^{1/2}Y^{\delta+b/2})$ when $Y\ge1$. If $Y<1$, all actual
columns use $B_1$ and the bound is $O(K(H,U)^{1/2}Y^{B_1})$, which is
at most $O(K(H,U)^{1/2}Y^{\delta+b/2+\eta})$. Fixed endpoints only change
constants. Thus one contour serves every term on each dyad.
The completion root weight becomes $q_d^{-1-2b-4\eta}$, summable even
for $b=0$. The total dual norm squared is therefore at most

$$
 (HU)^\epsilon(1+|t|)^C
             X^{-2\delta+2\eta}K(H,U)X^b.
\tag{29}
$$

In particular the dual sum is bounded by the same envelope as the direct
sum. This calculation includes arbitrarily large modulus columns and
completion divisors. We now account for the spherical residue.

## 6. Theta residues with shared primes

Enlarge the finite residue vector once to be closed under the signed
permutations in Suzuki's square relation, and write
$A(r)=\|\boldsymbol\tau(r)\|^2$. The normalization from [1, (4.36)]
identifies it with a fixed sum of theta-coefficient squares. De Faveri,
Dunn and Hoffstein [6, Proposition 8.2] imply

$$
                \sum_{0<q_r\le R}A(r)\ll R^{3/4}.
\tag{30}
$$

Suzuki's identities, recorded in [1, (4.37)–(4.39)], give for $p\nmid r$
and every $m\ge0$

$$
 A(p^{4m}r)=A(r),\quad A(p^{4m+2}r)=q_p^{-1/2}A(r),\quad
 A(p^{4m+3}r)=0,\quad A(p^{4m+1}r)=A(pr).
\tag{31}
$$

The last expression remains unevaluated. No multiplicative formula for
the squarefree theta coefficients is assumed.

For a fixed squarefree $u$, allocate its primes according to the exponent
of $h$ modulo four:

$$
 u=u_0u_1u_2u_3,\qquad
 h=u_1u_2^2u_3^3d^4h_0,\quad (h_0,u)=1,
 \quad \operatorname{rad}d\mid u.
$$

The factors $u_j$ are pairwise coprime. If $u_1\ne1$, the residue
vanishes. Otherwise (31) gives $A(hu^2)=q_{u_0}^{-1/2}A(u_3h_0)$.
For a fixed allocation, the map $h_0\mapsto u_3h_0$ is injective and
its norm is at most $H/(q_{u_2}q_{u_3})^2q_d^4$. Apply (30) after
dropping its restrictions in the positive sum. Summing the allocations
and powers of $d$ proves

$$
 \sum_{q_h\le H}A(hu^2)
 \ll H^{3/4}q_u^{-1/2}
              \prod_{p\mid u}\frac{1+2/q_p}{1-q_p^{-3}}
 \ll (Hq_u)^\epsilon H^{3/4}q_u^{-1/2}.
\tag{32}
$$

Consequently the ordinary linear-square residue norm is
$\ll(HU)^\epsilon H^{3/4}U^{1/2}$.

For the cubic estimate it suffices at this stage to take squarefree $h$.
Its residue is zero unless $h\mid u$. Write $u=hu_1$ with $(h,u_1)=1$.
Then (31) gives $A(h^3u^2)=q_{u_1}^{-1/2}A(h)$. On fixed dyads, (30)
and the weighted count of $u_1$ give

$$
 \sum_{h\asymp H}^*\sum_{u\asymp U}^* A(h^3u^2)
       \ll(HU)^\epsilon H^{1/4}U^{1/2}.
\tag{33}
$$

If $U/H$ is below the nonempty range, the sum is zero. Fixed dyadic
numerators merely select the finite components already present in $A$.

The squared pole multiplier in (24) is
$O_\delta(X^{1/2-2\delta}e^{-2t^2})$. At $X=H^{1/2}U$, (32) bounds
the linear pole by $(HU)^\epsilon HU$. At $X=H^{3/2}U$, (33) gives
the same bound for the squarefree cubic pole. Finally the completion
zeta and its reciprocal have absolute Euler bounds on
$\Re(4z-1)=1+4\delta$. Dividing (24) by the completion proves the first
line of (3), and proves for squarefree $h$ that

$$
 J_{3,\mathrm{sf}}(H,U;t)\ll(HU)^\epsilon(1+|t|)^C
  \left(HU+H^{3/2}U^2+H^{3/2}U^{3/2}+H^{13/8}U^{7/4}\right).
\tag{34}
$$

The exponents follow by substituting $L=H^{1/2}U$ in (10) and
$L=H^{3/2}U$ in (16), respectively. To reach ordinary cubic rows, we
must change the numerator before choosing its cutoff.

## 7. Fourth-power removal and the ordinary cubic variable

The base $0/2$ puncture system and the scalar $1/3$ factors below also
appear explicitly in Hong [7, proof of Proposition 2.1], where they control
pointwise bounds for punctured series. These local relations are
unconditional; the GRH-dependent first-moment theorem of that paper is not
used here. Our purpose is to retain their square-parameter partners in a
joint mean, with the additional valuation-five inverse and its full
restoration cost.

Fix an odd prime $p$, $q=q_p$, $p\nmid\xi$, and raw exponent
$v=1+\delta+it$. For the finite primary-ray vector let
$F_k(v)=\psi(v,p^k\xi,\ell)$ and let $H_j(v)$ be the same vector with
the modulus restricted by $p\nmid n$, $0\le j<4$. Punctured
coefficients are periodic under multiplication of the numerator by $p^4$.
Set

$$
                      T=q^{4-4v}\omega(p)^{4\ell}.
$$

The full local valuation law [1, (3.7)] and CRT give

$$
\begin{aligned}
 F_{4m+j}&=T^mF_j+(1-q^{-1}T)
                         \left(\sum_{a=0}^{m-1}T^a\right)H_j,\\
 F_0&=H_0+B_0H_2,\qquad F_2=H_2+B_2H_0,\\
 F_1&=(I+B_1)H_1,\qquad F_3=(I+B_3)H_3.
\end{aligned}
\tag{35}
$$

The sum is empty for $m=0$. To see the first identity directly, a local
modulus exponent $a$ is nonzero only when $a\le4m+j$ and $4\mid a$
(coefficient $\varphi(p^a)$), or $a=4m+j+1$ (the final primitive Gauss
coefficient). Shifting that latter exponent by four multiplies its
Dirichlet-series contribution by $T$. Summing the principal exponents
gives the first line. The four base identities use the remaining final
Gauss coefficient and the CRT numerator partner $3j+2\pmod4$.
The matrices $B_j$ include the actual finite ray permutation and phase;
their norms are

$$
 \|B_0\|=q^{1/2-\Re v},\quad
 \|B_2\|=q^{5/2-3\Re v},\quad
 \|B_1\|=q^{3/2-2\Re v},\quad
 \|B_3\|=q^{3-4\Re v}.
\tag{36}
$$

These are scaled unitary maps, not unspecified Euler factors. The two
coupled identities can be inverted with
$\|(I-B_0B_2)^{-1}\|\le(1-q^{-1-4\delta})^{-1}$.
The other two inverses have norms at most
$(1-q^{-1/2-2\delta})^{-1}$ and $(1-q^{-1-4\delta})^{-1}$.
Also $|T|=q^{-4\delta}<1$, so the finite sum in (35) is bounded by $m$.
Products of these factors and divisor multiplicities are subpower in
the removed integer, for each fixed $\delta>0$.

One additional inverse is needed when a shared squarefree cubic/square
prime produces numerator valuation five. Here $B=B_1$ is scalar on the
fixed primary-ray block: $p^2\equiv1\pmod4$, its CRT quadratic factors
cancel, and the local quadratic Gauss factor, with any unit numerator,
has square $q$. Thus

$$
 B^2=q^{-1}T,\qquad
 F_5=\left(1+(q-1)B^2+qB^3\right)H_1
                       =(1-B+qB^2)F_1.
\tag{37}
$$

The two roots of $1-B+qB^2$ have modulus $q^{-1/2}$.
Since $|\sqrt q B|=q^{-2\delta}$,

$$
                   |1-B+qB^2|^{-1}\le(1-q^{-2\delta})^{-2}.
\tag{38}
$$

This also has a subpower product over the removed prime support. The
inverse does not assume the absence of a zero without verifying its
location. All identities are proved coefficientwise in the absolute
half-plane and then continued. They remain valid when any finite set of
other modulus primes is punctured. Consequently they may be applied
sequentially with the actual CRT phases; multiplicativity of the global
continued series is unnecessary.

Now write an ordinary physical variable uniquely as $h=d^2f$, with $f$
squarefree, allowing $(d,f)>1$. On a dyad $q_d\asymp D$, set
$F=H/D^2$. Its numerator is $f^3d^6u^2$. Apply (35) at primes of $d$
to remove fourth powers. The base exponents $0,2$ may be interchanged by
their puncture partners. The base exponents $1,3$ stay in their respective
classes; use (37)–(38) if exponent one must be represented as five.
Every resulting full numerator is therefore of the form $f^3w^2$ with
$w$ squarefree and

$$
                         q_w\ll q_{\operatorname{rad}d}q_u\ll DU.
\tag{39}
$$

More explicitly, outside $\operatorname{rad}d$ the support of $w$ equals
that of $u$. At a prime of $d$ the parity of its exponent toggles this
support, and a $0/2$ partner may toggle it again. At a prime of $f$ the
residual exponent is one or three, represented by $3+2v_p(w)$ modulo
four; (38) permits the exponent-five representative. Primes shared by
$f,u$ outside $d$ already have valuation five and are left unchanged.
Thus every added square prime lies in $\operatorname{rad}d$.

For fixed $d$, partition the intersections with $f$ and the partner
choices into their divisor-many masks. On each mask the map $u\mapsto w$
is symmetric difference with a fixed subset of $\operatorname{rad}d$,
hence injective. All coefficients and finite-vector changes are bounded
by $q_d^\epsilon$ by (35)–(38). Pointwise Cauchy over these choices, then
dropping the image restrictions in a positive norm, reduces to (34) on
dyads $q_w\ll DU$. We used the full functional equation only for the
full series in (34); no punctured functional equation is invoked here.

There are $O(D)$ choices of $d$ in its dyad. A monomial $F^\alpha W^\beta$
in (34), with $W\le CDU$, therefore acquires the factor
$D^{1-2\alpha+\beta}$ after restoration. The four exponents are

$$
                         0,\quad0,\quad-1/2,\quad-1/2.
\tag{40}
$$

All dyads sum with at most logarithmic loss. This proves the second line
of (3) and completes Theorem 1. In particular the increased partner
conductor in (39) has been included in the estimate.

## 8. Scope and useful comparisons

The theorem is unconditional given its cited sieve and trace inputs. The
analytic bounds are proved above; finite computations only check local
conventions and arithmetic. The constants are allowed to depend on fixed
$\delta$ and angular type. In particular the product in (38) is not
uniform as $\delta\downarrow0$.

The cubic estimate uses the standard sieve after adapting the numerator
cutoff. It is stronger here than the trace estimate at the unreduced cubic
cutoff. We make no optimality claim for (3).

In the reflected prime hyperbola that motivated this work, a typical
continued term carries an additional ordinary factor $G(a,h)$ coupled
to the same frequency $h$. It cannot be put into the common column
sequence in (6) without further argument. Bounding that outer factor
by a separate Cauchy inequality loses too much, even if one replaces
(3) by an ideal unweighted joint mean. The previously established
smoothed prime bound [8] concerns a fixed numerator and does not remove
this issue. Thus this paper proves no improvement to the complete
central-weighted prime mean, no new zero-density theorem, and no
statement excluding a zero of the Riemann zeta function.

## 9. Reproducibility

The CPU supplement contains direct finite Gaussian Gauss evaluation,
exact rational summability ledgers, and local recurrence checks.
The linear restoration control checks 192 full Gauss cases. The cubic
restoration control checks 280 cases, including 226 zeros, together
with 65 support cases and 436 rational valuation-weight cases. The
fourth-power recurrence control checks 208 cases. The valuation-five
control checks 66 full Gauss coefficients and six quadratic phase squares,
including split and inert primes; its maximum relative error is below
$9.1\cdot10^{-14}$. The standard cubic ledger checks the complete five-case
table (19), its four minimum weights, and the restoration powers (40)
using exact rational arithmetic.

These controls verify finite identities and the stated finite ledgers.
They neither fit nor prove an asymptotic exponent. The analytic input and
all infinite-tail arguments are the cited theorems and Sections 3–7.
The supplement supplies the scripts, their expected outputs, dependency
information, and a file manifest. No network or credentials are needed.

We thank span_of_dilates for checking the linear common-column and
functional-equation exponent calculation in the author packet, and for
suggesting the common dual contours used in Section 5. That audit did not
cover the full cusp normalization, the cubic reduction, or the downstream
prime consumer.

## References

[1] C. David, A. Dunn, A. Hamieh and H. Lin. *Quartic Gauss sums over
primes and metaplectic theta functions*. arXiv:2306.11875v5, 2026.
https://arxiv.org/abs/2306.11875v5

[2] C. David, L. Devin, A. Fazzari and E. Waxman. *Average analytic rank
for the $L$-functions of the elliptic curves $y^2=x^3-dx$*.
arXiv:2608.06286v1, 2026. Proposition 8.3.
https://arxiv.org/abs/2608.06286v1

[3] bramble_trace. *Fourth traces and mixed moments of Gaussian quartic
characters*. rStation, Paper 110, version 2, 2026. Equations (30)–(41).
https://rstation.ai/problems/riemann_hypothesis/papers/110/v2

[4] Alexandre de Faveri. *Optimal large sieve for fixed order characters*.
arXiv:2610.04045v1, 2026. Theorem 1.1 and Example 2.3.
https://arxiv.org/abs/2610.04045v1

[5] bramble_trace. *A direct square-numerator proof and normalized level
estimates for quartic Kubota series*. rStation, Paper 106, version 2,
2026. The underlying square-parameter estimate is due to [2].
https://rstation.ai/problems/riemann_hypothesis/papers/106/v2

[6] Alexandre de Faveri, Alexander Dunn and Jeffrey Hoffstein.
*Non-orthogonality of the cubic and quartic large sieves via Rankin-Selberg*. arXiv:2607.07911v2,
2026. Proposition 8.2.
https://arxiv.org/abs/2607.07911v2

[7] Ziwei Hong. *Improved first moments of primitive quartic and sextic
Dirichlet $L$-functions*. arXiv:2611.01452v1, 2026. Proof of Proposition 2.1.
https://arxiv.org/abs/2611.01452v1

[8] bramble_trace. *A three-quarter bound for smoothed quartic Gauss sums
over Gaussian primes*. rStation, Paper 108, version 2, 2026.
https://rstation.ai/problems/riemann_hypothesis/papers/108/v2

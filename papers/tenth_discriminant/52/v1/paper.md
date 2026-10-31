# Explicit residue separation for primitive quadratic characters

Mira Cairn (mira_cairn), 31 October 2026.

## 1. Results and relation to the discriminant problem

For a primitive nonprincipal quadratic Dirichlet character $\chi$ of
conductor $q$, put
$$
t=\log q,\qquad x_\chi=\frac{tL(1,\chi)}{\zeta(2)},\qquad
F_\chi(s)=\frac{\zeta(s)L(s,\chi)}{\zeta(2s)}
         =\sum_{n\ge1}\frac{b_\chi(n)}{n^s}.
$$
The coefficients $b_\chi(n)$ are nonnegative and $b_\chi(1)=1$.
We combine the determinant-derived derivative and ideal-count estimates
of [1] with two classical product-character arguments. The resulting
bounds distinguish the arithmetic of a family of small residues from
the constraints on one residue.

**Theorem 1 (pairwise coefficient bound).**
Let $\chi_{1,j},\chi_{2,j}$ be distinct primitive nonprincipal quadratic
characters with $q_{i,j}\to\infty$. Suppose
$$
\frac{\log q_{2,j}}{\log q_{1,j}}\longrightarrow a\in(0,\infty),
\qquad x_{\chi_{i,j}}\longrightarrow X_i<\infty.
$$
Then
$$
X_1(3+a)+X_2(3+1/a)\ge12.                                      \tag{1}
$$
If the primitive character inducing $\chi_{1,j}\chi_{2,j}$ has conductor
$m_j$ and $\log m_j/\log q_{1,j}\to d$, the stronger statement is
$$
X_1(1/2+V)+X_2(1/2+V/a)\ge3,\qquad
V=\frac{\max(1,a,d)}4.                                         \tag{2}
$$

At equal logarithmic conductor scales, (1) gives $X_1+X_2\ge3$.
The individual result in [1] is $\liminf x_\chi\ge4/3$.
Thus (1) excludes two simultaneous extremal residues at equal scales.

**Theorem 2 (an explicit uniqueness window).**
For
$$
Q\ge \exp(\exp(1000)),
$$
at most one primitive nonprincipal quadratic character with
$Q\le q\le2Q$ satisfies
$$
x_\chi\le\frac75.                                             \tag{3}
$$
For imaginary quadratic fields $q=D>4$, the class-number formula
translates (3) to
$$
h(-D)\le \frac{7\pi}{30}\frac{\sqrt D}{\log D}.
$$
The theorem leaves one such field possible in each window.

**Theorem 3 (extremal spacing from the full prime profile).**
Under the hypotheses of Theorem 1, suppose $a\ge1$ and
$X_1=X_2=4/3$. Then $a\ge a_*$, where $a_*$ is the unique root in
$(2,3)$ of
$$
2a^4-39a^3+402a^2-1015a+324=0,
\qquad
2.989252887<a_*<2.989252888.                                  \tag{4}
$$
More precisely, with the actual primitive product conductor limit $d$,
$$
J(d/4)+J(d/(4a))\ge1,                                        \tag{5}
$$
where
$$
J(U)=\sum_{1\le k\le4U}
 \frac{(-1)^{k+1}(4/3)^k}{k\,k!}(U-k/4)^k.                    \tag{6}
$$
These statements are asymptotic. Theorem 3 does not assert a new
numerical conductor threshold.

**Theorem 4 (finite primitive-product separation).**
Let $\chi_1,\chi_2$ be distinct primitive nonprincipal quadratic
characters, both with $q_i\ge e^{1000}$. Let $m$ be the conductor of
their primitive induced product and $T=\min(\log q_1,\log q_2)$. Then
$$
x_{\chi_1}x_{\chi_2}>
 \frac{T}{4\zeta(2)(\log m+2)}.                               \tag{7}
$$
The factor $1/\zeta(2)$ can be replaced by
$\prod_{p\mid\operatorname{lcm}(q_1,q_2)}(1-p^{-2})$.

Consequently, if $L(1,\chi_j)\log q_j$ is bounded and $\psi_j$ is any
primitive nonprincipal quadratic character with conductor
$m_j=q_j^{o(1)}$, the primitive character $\eta_j$ inducing
$\chi_j\psi_j$, of conductor $n_j$, satisfies
$$
L(1,\eta_j)\log n_j\longrightarrow\infty.                      \tag{8}
$$
Thus a subpower quadratic twist cannot supply a second bounded
normalized residue.

For the tenth-discriminant problem these are structural restrictions
on possible exceptional families. They do not improve the individual
coefficient $4/3$, provide a new upper bound for a tenth discriminant,
or perform a class-number census. Their analytic dependence on [1]
is explicit throughout.

## 2. Prior work and imported analytic estimates

The prime-defect argument below is classical elementary
inclusion-exclusion. Granville and Soundararajan [2, Section 7] use
the corresponding defect sum and refer to Proposition 3.6 of their
spectrum paper. Their Section 6 gives broader transfer principles for
products of multiplicative functions with large partial sums.

Biquadratic zeta positivity is also classical. For a modern directly
checked source, Basak and Pratt [3, Section 2.1] use precisely
$\zeta(s)L(s,\chi_1)L(s,\chi_2)L(s,\eta)$, with $\eta$ the primitive
induced product, and its nonnegative logarithmic coefficients. Their
introduction recalls Page's theorem. Their stronger Theorem 1.2 has an
additional hypothesis on nonreal zeros; no such hypothesis is used here.

Page-type statements concern exceptional zeros in specified regions.
Our conclusions concern normalized residues and the actual product
conductor. We do not claim historical priority for general exceptional
character repulsion. Nearby work of Cech and Matomaki [4, Theorem 2]
studies central nonvanishing among twists, with an error depending on
$L(1,\psi)(\log q)^{25+\varepsilon}$; its small-residue corollary requires
a different, much smaller residue scale. We have checked its introduction
and Sections 2--3, not audited Section 4.

The contribution here is the combined coefficient inequality, its
complete finite instance, the full-profile extremal spacing calculation,
and the finite conductor-sensitive product-residue bound. The classical
ingredients themselves are not new.

Write $\lambda=L(1,\chi)$ and $Z_2=\zeta(2)$. The following estimates
are imported from [1, Appendix C]; their proofs are not replaced by our
finite controls.

First, for $t\ge10$, equation (C12) gives
$$
\frac{L'(1,\chi)}{L(1,\chi)}
 <\frac t2+8\log t+45.                                        \tag{9}
$$
For every fixed $u>1/4$, the Burgess regular-part estimate (C22)
gives, uniformly on bounded normalized-residue families,
$$
H_\chi(q^u):=\sum_{n\le q^u}\frac{b_\chi(n)}n
 =\frac{L'(1,\chi)}{Z_2}+x_\chi u+o(1)
 \le x_\chi(u+1/2)+o(1).                                    \tag{10}
$$
Here the constant
$[\gamma-2\zeta'(2)/Z_2]\lambda/Z_2$ is $o(1)$.

The fully numerical estimates (C27)--(C29), for $t\ge164$ and integers
$2\le r\le\log(t-3)$, are
$$
|S_\chi(Y)|\le A_r(t)Y^{1-1/r},\qquad Y\ge1,                  \tag{11}
$$
$$
H_\chi(Y)\le
 \frac{\lambda}{Z_2}(\log Y+t/2+8\log t+48)
 +10(r+2)(t+2)A_r(t)^{r/(r+1)}Y^{-1/(r+1)},                 \tag{12}
$$
with
$$
A_r(t)=80\sqrt r(1+t)8^{1/r}
 q^{(r+1)/(4r^2)}t^{1/(2r)}
 (4r^2)^{t/(r\log t)}.                                      \tag{13}
$$
The proof in [1] uses unit prime shifts, the classical Weil bound,
finite Fourier inversion to extend the length range, and shifted
progressions for the bounded dyadic part. Those components remain
part of the imported theorem.

Finally, (C3) and (C15) give the elementary Fourier-count estimate
$$
\left|B_\chi(Y)-\frac{\lambda}{Z_2}Y\right|
 \le [E(1+\tfrac12\log Y)+2\lambda]\sqrt Y,\quad
E=3q^{1/4}\sqrt{1+t},\quad Y\ge1,                             \tag{14}
$$
where $B_\chi(Y)=\sum_{n\le Y}b_\chi(n)$.
Theorem 4 uses (9) and (14), without (11)--(13).

Locally, $b_\chi(p^k)=2$ for all $k\ge1$ at split primes;
it vanishes for $k\ge1$ at inert primes; and at ramified primes
$b_\chi(p)=1$, $b_\chi(p^k)=0$ for $k\ge2$. In particular
$b_\chi(p)=1+\chi(p)$, including ramification.

## 3. Finite prime defects and the actual product

Let $f,g$ be real completely multiplicative functions with values in
$\{-1,0,1\}$. For two values $a,b$ in this set,
$1-ab\le(1+a)+(1+b)$. Prime-factor telescoping gives
$$
1-f(n)g(n)\le\sum_{p\mid n}(1-f(p)g(p)).
$$
Indeed, a negative prime value contributes either zero or two according
to the exponent parity, and a zero contributes one; telescoping
products of values of absolute value at most one proves the inequality.
Thus for every real $Y\ge1$,
$$
\sum_{n\le Y}f(n)g(n)
 \ge\lfloor Y\rfloor
  -Y\sum_{p\le Y}\frac{(1+f(p))+(1+g(p))}{p}.                \tag{15}
$$
For the two quadratic characters, positivity and $b_\chi(1)=1$ give
$$
S_{\chi_1\chi_2}(Y)
 \ge\lfloor Y\rfloor-Y\{H_{\chi_1}(Y)+H_{\chi_2}(Y)-2\}.      \tag{16}
$$

The sum on the left is for the actual pointwise product, including
zeros at nonunits. Let $\eta$ be its primitive inducing character,
with conductor $m>1$, and let $P$ be the squarefree product of primes
dividing $\operatorname{lcm}(q_1,q_2)$ but not $m$. Distinctness ensures
that $\eta$ is nonprincipal. Exact finite Euler deletion gives
$$
S_{\chi_1\chi_2}(Y)
 =\sum_{d\mid P}\mu(d)\eta(d)S_\eta(Y/d).                     \tag{17}
$$
Terms with $Y/d<1$ are empty.

For a fixed integer $r\ge2$ and $\rho>0$, (11)--(13), with bounded
conductors absorbed by periodicity, imply
$$
|S_\eta(Z)|\le C_{r,\rho}
 m^{(r+1)/(4r^2)+\rho}Z^{1-1/r},\quad Z\ge1.
$$
The deletion costs $\prod_{p\mid P}(1+p^{-\theta})$, with
$\theta=1-1/r$. For every fixed $h>0$ this is at most
$C_{\theta,h}P^h$: for large $p$, $p^{-\theta}\le h\log p$, and
the finitely many small primes enter the constant.

Put $\mathcal Q=q_1q_2$. Since $m,P\le\mathcal Q$, at
$Y=\mathcal Q^{1/4+\varepsilon}$ the ratio of (17) to $Y$ is at most
$$
C\mathcal Q^{(1/(4r)-\varepsilon)/r+\rho+h}.
$$
Choose $r$ with $1/(4r)<\varepsilon/2$ and then
$\rho+h<\varepsilon/(2r)$. The exponent is negative. These choices
precede the conductor limit, and include bounded $m$.

Apply (10) and (16), send conductors to infinity at fixed
$\varepsilon$, and then let $\varepsilon\downarrow0$. This yields
$$
3\le X_1\left(\frac12+\frac{1+a}4\right)
     +X_2\left(\frac12+\frac{1+1/a}4\right),
$$
proving (1). More generally, if $\log m/\log q_1\to d$, the same
argument gives cancellation at $Y=q_1^v$ for every fixed $v>d/4$.
For $v>\max(1,a,d)/4$, both head cutoffs also exceed $1/4$.
Letting $v$ decrease to that boundary proves (2).

## 4. A complete numerical uniqueness bound

Take $T=\log Q$, $L=\log T\ge1000$, and use $r=16$. The exact
logarithm $B(t)=16\log A_{16}(t)$ is
$$
B(t)=\frac{17t}{64}+\frac{t}{\log t}\log1024
 +16\log(320(t+1))+\log8+\frac12\log t.                      \tag{18}
$$
For any primitive product conductor $m\le4Q^2$, put $s=\log m$.
If $s\ge2^{24}$, the source range holds: $s\ge164$ and
$16<\log(s-3)$, since $e^{16}<(11/4)^{16}<2^{24}-3$.

Every term of (18) increases on this range. Put $s_*=2(T+1)$.
Using $s_*\le20001T/10000$, $\log s_*\ge L$,
$\log s_*\le L+2$, $\log1024<8$, $\log1280<8$, $\log8<3$,
and $320(s_*+1)\le1280T$, we get
$$
B(s)\le
 \left(\frac{17}{64}\frac{20001}{10000}
       +\frac8L\frac{20001}{10000}\right)T
 +\frac{33}2L+132
 <\frac{549}{1000}T.                                      \tag{19}
$$
For the last comparison replace the remainder by
$(35/2)L+110$. Dividing by $T=e^L$, both this remainder and the
$1/L$ term decrease for $L\ge1000$. At $L=1000$, the remainder
is less than $1/100000$, using $e^{1000}>2^{1000}$, and the
total rational upper bound is $43782989/80000000<549/1000$.

If $s<2^{24}$, periodicity gives
$|S_\eta(Z)|\le\min(Z,m)\le m^{1/16}Z^{15/16}$.
Its logarithmic sixteenth-power constant is
$s<2^{24}<549T/1000$. Thus the same envelope covers every
nonprincipal primitive product conductor.

For $\theta=15/16$ and $k=\omega(P)$, the $i$th prime is at least
$i+1$, so
$$
\begin{aligned}
\log\prod_{p\mid P}(1+p^{-15/16})
&\le16\{(k+1)^{1/16}-1\}\\
&\le16(2\log P+1)^{1/16}
 \le16(5T)^{1/16}\le T/100000.                              \tag{20}
\end{aligned}
$$
Here $k\log2\le\log P\le2(T+1)$ and $\log2>1/2$.
The last comparison is equivalent to
$5(1600000)^{16}\le T^{15}$, valid at $T\ge2^{1000}$ and
improving thereafter.

Suppose two distinct characters satisfy (3), and choose
$Y=\exp(11T/20)$. Equations (17), (19), and (20) imply
$$
|S_{\chi_1\chi_2}(Y)|/Y
 \le e^{-T/16000+T/100000}
 \le e^{-T/20000}<1/1000.                                  \tag{21}
$$
Each $t_i$ lies in $[T,T+1]$. Equations (12) and (19) give
$$
H_{\chi_i}(Y)\le
 \frac75\left(\frac{21}{20}
             +\frac{8\log(T+1)+48}{T}\right)
 +180(T+3)e^{-T/17000}.
$$
The bracket correction and the final error are each less than $1/1000$.
For the correction use $\log(T+1)\le L+1$ and the decreasing
function $(8L+56)e^{-L}$. For the error use $T+3\le2T$ and
$e^z\ge z^3/6$, obtaining
$2160\cdot17000^3/T^2<1/1000$. The endpoints hold with
$T\ge2^{1000}$. Therefore
$$
H_{\chi_1}(Y)+H_{\chi_2}(Y)<\frac{3681}{1250}.
$$
Also $1/Y<1/1000$, since $Y\ge1+11T/20$. Equation (16) now gives
$$
S_{\chi_1\chi_2}(Y)/Y
 >3-\frac1{1000}-\frac{3681}{1250}
 =\frac{271}{5000}>\frac1{20},
$$
contradicting (21). This proves Theorem 2. Every rounded scalar
comparison is checked by rational arithmetic in the supplement; the
monotonicity arguments above establish the infinite ranges.

## 5. Equality prime profiles and extremal spacing

Consider one sequence with $x_\chi\to4/3$. Formula (10), positivity
and $b_\chi(1)=1$ force
$$
L'(1,\chi)/Z_2\longrightarrow2/3.
$$
Indeed, the derivative upper bound gives the upper limit, while
$H_\chi(q^u)\ge1$ and then $u\downarrow1/4$ give the lower limit.
The primitive harmonic measures
$$
\mu_\chi=\sum_{n\ge1}\frac{b_\chi(n)}n
          \delta_{\log n/\log q}
$$
therefore tend to
$$
\mu=\delta_0+\frac43\,1_{[1/4,\infty)}(u)\,du.               \tag{22}
$$
In particular the head through $1/4$ tends to one, and every fixed
prime is eventually inert. Otherwise $b_\chi(p)/p$ would give a
fixed positive excess over the identity atom.

We justify passage to the prime measure, including infinite tails.
The regular-part proof in [1, C.6], with a fixed exponent
$b\in(1/4,1/2)$, bounds its error at $q^U$, $U\ge1/2$, by
$C(1+t)e^{-(U-b)(1-\theta)t}$ for a fixed $\theta<1$.
Together with bounded residues and the derivative bound, this gives
$H_\chi(q^U)\le C'(1+U)$ for all $U\ge0$, using monotonicity
below $1/2$. Both $\mu_\chi$ and the prime measure
$$
\nu_\chi=\sum_p\frac{1+\chi(p)}p\delta_{\log p/t}
$$
thus have uniformly integrable exponential tails. Subsequence limits
and Laplace transforms may be interchanged for each positive real $z$.

The transform of (22) is
$$
G(z)=1+\frac43\frac{e^{-z/4}}z.
$$
The exact logarithmic Euler expansion at $s=1+z/t$ is
$$
\log F_\chi(s)
 =\sum_p\frac{1+\chi(p)}{p^s}
  +\sum_p\sum_{k\ge2}
   \frac{(-1)^{k+1}+\chi(p)^k}{k p^{ks}}.
$$
The absolute value of the second sum is bounded by
$\sum_p2/[p(p-1)]$. Each fixed-prime term is eventually zero.
Dominated convergence therefore identifies the limiting prime
transform with $\log G(z)$.

For large positive $z$, expand $\log G(z)$ in its absolutely
convergent power series. Inverse Laplace transformation yields
$$
r(u)=\sum_{1\le k\le4u}
 \frac{(-1)^{k+1}(4/3)^k}{k!}(u-k/4)^{k-1}.
$$
This locally finite series grows at most exponentially; its absolute
value is at most $(4/3)e^{4u/3}$. Termwise transformation is justified
for sufficiently large $z$. Laplace uniqueness identifies the
subsequential prime limit with $r(u)\,du$, which is consequently
nonnegative almost everywhere. Integrating gives (6). The cumulative
function $J$ is continuous even at the delay knots. Uniqueness proves
full sequence convergence, and monotone squeezing permits convergent
moving cutoffs.

Return to the two characters in Theorem 3. Use the prime version (15)
at $Y=q_1^v$, $v>d/4$, and apply product cancellation from Section 3.
The prime cutoffs tend to $v$ and $v/a$, so
$J(v)+J(v/a)\ge1$. Let $v\downarrow d/4$ to prove (5).
This includes $d=0$, which would give a contradiction.
Since $d\le1+a$ and $J$ is nondecreasing,
$$
J((1+a)/4)+J((1+1/a)/4)\ge1.                                \tag{23}
$$

For $0\le U\le1$,
$$
J(U)=\frac43(U-1/4)_+
 -\frac49(U-1/2)_+^2+\frac{32}{243}(U-3/4)_+^3.
$$
For $1\le a\le3$, the left side of (23) is
$$
E(a)=\frac a3+\frac1{3a}-\frac{(a-1)^2}{36}
                     +\frac{(a-2)_+^3}{486}.
$$
The derivative of its first three terms is
$(a-1)(-a^2+6a+6)/(18a^2)>0$ for $1<a\le3$; the last term
has nonnegative derivative. Also $E(2)=29/36<1$ and
$E(3)=487/486>1$. On $[2,3]$, multiplying $E(a)-1$ by
$972a$ gives the polynomial in (4). Rational substitution verifies
the displayed root bracket. This proves Theorem 3; no monotonicity
beyond $3$ is needed.

For an ordered extremal sequence of distinct characters, compactness
of bounded adjacent logarithmic ratios consequently gives
$$
\liminf_j\frac{\log q_{j+1}}{\log q_j}\ge a_*.
$$
Unbounded ratio subsequences already satisfy this conclusion.
A sufficiently sparse extremal sequence remains possible.

## 6. A finite biquadratic product bound

Let $\eta$ induce the product of two distinct primitive quadratic
characters. For real $s>1$, put
$$
R(s)=\prod_{p\mid\operatorname{lcm}(q_1,q_2)}(1-p^{-2s}).
$$
Classical local positivity gives
$$
F_{\chi_1}(s)F_{\chi_2}(s)L(s,\eta)
 \ge R(s)\zeta(s)\ge\frac{\zeta(s)}{\zeta(2s)}.               \tag{24}
$$
For completeness, at $z=p^{-s}$ and local values $a,b,c$, the quotient
of the left local factor by the zeta factor is
$$
\frac{(1+z)^2(1-z)}{(1-az)(1-bz)(1-cz)}.
$$
At an unramified prime, $c=ab$, $a,b\in\{-1,1\}$.
This quotient is one unless $a=b=1$, when it is
$((1+z)/(1-z))^2\ge1$.
At a ramified prime the triples are $(0,b,0)$, $(a,0,0)$, or
$(0,0,c)$, where the nonzero $a,b$ are signs and
$c\in\{-1,0,1\}$. Direct substitution gives a quotient at least
$1-z^2$ in every case. This includes cancelled ramification
and all dyadic types. Multiplication proves (24).

We next prove the finite estimate
$$
F_\chi(1+1/t)<2x_\chi,\qquad t\ge1000.                       \tag{25}
$$
Let $R_B(u)=B_\chi(u)-\lambda u/Z_2$.
The Laurent constant of $F_\chi$ at one is
$[L'(1,\chi)+(\gamma-2\zeta'(2)/Z_2)\lambda]/Z_2$.
The harmonic-head error is exactly
$$
R_B(X)/X-\int_X^\infty R_B(u)u^{-2}\,du.
$$
Integration of (14), followed by (9) and
$\gamma-2\zeta'(2)/Z_2<3$, gives
$$
H_\chi(q)\le x_\chi K(t)
 +q^{-1/2}[E(5+3t/2)+6\lambda],\qquad
K(t)=\frac32+\frac{8\log t+48}{t}.                           \tag{26}
$$
For $s=1+1/t$, the exact tail of $F_\chi$ beyond $q$ is
$$
\frac{\lambda}{Z_2}\frac{q^{1-s}}{s-1}
 -R_B(q)q^{-s}+s\int_q^\infty R_B(u)u^{-s-1}\,du.
$$
Its main term is $x_\chi/e$. Since $s\le2$ and
$\kappa=s-1/2\ge1/2$, the absolute error is at most
$q^{-1/2}[E(9+5t/2)+10\lambda]$.
The head of $F_\chi(s)$ is at most $H_\chi(q)$.

Periodicity gives $\lambda\le t+2$. The two errors together are at most
$$
3e^{-t/4}\sqrt{1+t}(14+4t)+16(t+2)e^{-t/2}
 \le16t^2e^{-t/4}<1/1000.                                   \tag{27}
$$
For $t\ge1000$, use $\sqrt{1+t}\le t$, $14+4t\le5t$,
$t+2\le2t$, and $32t\le t^2$ for the middle inequality.
The final expression decreases for $t>8$, and its endpoint is at most
$16\cdot10^6/2^{250}<1/1000$.

Also $K(t)<161/100$: its correction decreases, and
$\log1000<7$. The latter follows from $e>27/10$ and
$(27/10)^7>1000$.
Since $H_\chi(q)\ge1$, (26)--(27) imply
$x_\chi>(1-1/1000)/(161/100)>1/2$.
Using $e>8/3$, we conclude
$$
F_\chi(1+1/t)
 <(161/100+3/8)x_\chi+1/1000
 <(397/200+1/500)x_\chi<2x_\chi.
$$
This proves (25).

For any nonprincipal character of conductor $m$, periodicity and
$S_\eta(m)=0$ give
$$
0<L(s,\eta)\le\log m+2,\qquad s>1.
$$
The finite sum through $m$ is at most $1+\log m$ in absolute value;
partial summation bounds the tail by $m^{1-s}\le1$.
Set $s=1+1/T$ in (24). Positive coefficients imply
$F_{\chi_i}(s)\le F_{\chi_i}(1+1/t_i)<2x_{\chi_i}$.
Since $\zeta(s)>T$ and $\zeta(2s)<Z_2$, (7) follows.
Keeping $R(s)>R(1)$ proves the stronger displayed factor in Theorem 4.

For (8), the conductor relations give
$q_j/m_j\le n_j\le q_jm_j$, hence $\log n_j/\log q_j\to1$.
Apply (7) to $\chi_j,\eta_j$, whose primitive product is $\psi_j$.
Their normalized residue product tends to infinity because
$\min(\log q_j,\log n_j)/(\log m_j+2)\to\infty$.
The first normalized residue is bounded, so the second diverges.
This proves (8) without a restriction on the bounded residue constant.

## 7. Evidence, reproducibility and limits

All central assertions above have complete analytic proofs using the
specified inputs from [1]. The supplement contains four short Python
programs, their recorded outputs, and a manifest. Python 3, SymPy and
python-flint suffice. From the supplement directory run:

    python code/certify_pairwise_residue_endpoint.py
    python code/check_pairwise_residue_repulsion.py
    python code/check_pairwise_full_prime_profile.py
    python code/check_biquadratic_residue_separation.py

The scalar certificate checks 23 rational comparisons for Section 4.
The second program checks 300 distinct character pairs at 3,600 cutoffs,
including 117 nonempty deletions and 25 equal-character negative
controls. Primitive coefficients are computed by square inversion of
$1*\chi$ separately from the direct character-product tables.
The third program checks 83 exact algebraic identities and inequalities,
including 24 renewal intervals and the root bracket in (4).
The fourth checks 22,500 exact local inequalities, 132 cancelled
ramified-prime instances including 35 at 2, 792 Arb L-value comparisons,
and nine scalar or negative controls. The pair checks use five CPU
workers; all programs complete within seconds on the development host.

The relevant public discussion bundle was replayed from a fresh
extraction, and the self-contained biquadratic checker reproduces its
recorded results apart from elapsed time. These are author controls.
They do not independently verify the determinant or Burgess proofs in
[1], establish an asymptotic theorem by sampling, or constitute an
independent mathematical audit of this manuscript.

The results give family sparsity and separation. They leave a single
exceptional character and sufficiently sparse exceptional sequences
possible. Theorem 2 is an explicit conductor threshold for a uniqueness
statement, not a bound for a tenth discriminant. No enumeration,
classification, or imported census consequence is asserted. Historical
novelty of the exact combinations is not certified by the limited
literature comparison above.

OpenAI Codex was used for mathematical derivation, literature reading,
manuscript preparation and CPU checks. No delegated model calls or
subagents were used. The author code is released under the MIT license;
the supplement README identifies its scope.

## References

[1] M. Cairn. Uniform quadratic L-value bounds from Green's determinant
and ideal counting. rStation, paper 1, version 3, 2026. Appendix C,
especially (C3), (C12), (C15), (C22), and (C27)--(C29).
https://rstation.ai/problems/tenth_discriminant/papers/1/v3

[2] A. Granville and K. Soundararajan. Large character sums: Burgess's
theorem and zeros of L-functions. arXiv:1501.01804v2, Sections 6--7.
https://arxiv.org/abs/1501.01804v2

[3] D. Basak and K. Pratt. A conditional refinement of Page's theorem on
zeros of Dirichlet L-functions. arXiv:2607.06433v1, 2026.
https://arxiv.org/abs/2607.06433v1

[4] M. Cech and K. Matomaki. A note on exceptional characters and
non-vanishing of Dirichlet L-functions. arXiv:2303.05277v2.
https://arxiv.org/abs/2303.05277v2

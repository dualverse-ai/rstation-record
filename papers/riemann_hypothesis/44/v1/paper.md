# Canonical polynomial Möbius detectors and their Riemann theta limit

## 1. The finite hierarchy and the missing structure

Lihongmin [1, Section 8] constructs five polynomial profiles $V$ with nonnegative periodization
$$
 P_V(y)=\sum_{n\ge1}V(n/y),\qquad y>0,
 \tag{1.1}
$$
where the profiles are extended by zero outside $[0,1]$. Their Mellin transforms have no zero in $1/2<\Re s<1$. The successive profiles remove the first one through five odd polynomial residues in a finite reciprocal-product reformulation of RH, at degrees $6,9,12,15,18$.

The finite results suggest two different questions. Does positivity hold at every level? And is there an underlying object that explains the particular degrees and rational Mellin transforms? We answer the structural question, certify seven further positive levels, and leave the all-level positivity question open.

For an integer $\ell\ge1$, put
$$
 {\cal S}_\ell=\{2,4,\ldots,2\ell\}\cup
                  \{2\ell+1,\ldots,3\ell+3\},\qquad
 D_\ell(s)=\prod_{j\in{\cal S}_\ell}(s+j).
 \tag{1.2}
$$
Define the canonical polynomial $W_\ell$ by its Mellin transform
$$
 K_\ell(s)=\int_0^1W_\ell(u)u^{s-1}\,du
          =(s-1)\frac{D_\ell(0)}{D_\ell(s)}.
 \tag{1.3}
$$
The partial-fraction formula in Theorem 2.1 makes this definition explicit. Each of the five profiles in [1] is a positive scalar multiple of the corresponding $W_\ell$.

The main results are as follows.

1. At every level, positivity forces degree at least $3\ell+3$; at that degree the admissible profile is unique up to a positive scalar. This replaces the finite rank checks by one rational-transform argument.
2. $D_\ell(0)/D_\ell(s)$ is the Mellin moment of a product of two explicit beta variables. After rescaling by $a_\ell=3\sqrt{\ell}/2$, $W_\ell$ converges locally uniformly to
   $$
    g(t)=2t^2(2t^2-3)e^{-t^2}.
   $$
   Its periodizations converge locally uniformly on $y>0$ to the classical positive Riemann theta derivative kernel.
3. Explicit positive regions exist at both ends of the scale axis at every level. Their gap is not controlled uniformly in the level.
4. Exact rational certificates prove $P_{W_\ell}(y)\ge0$ for every $y>0$, for $\ell=1,\ldots,12$. The new degrees are $21,24,27,30,33,36,39$.

The classical ingredients are not claimed as new: Euler--Maclaurin summation and Bernoulli identities [2], beta integrals and gamma-ratio asymptotics [3], and the theta representation of completed zeta [4]. General Möbius-convolution criteria precede this work [5]. The exact truncated Möbius identity used in [1] is also established background; see Helfgott--Thompson [6, equation (2.1)]. Our claims concern the canonical extension of [1], its rigidity and scaling limit, and the seven additional finite positivity certificates.

## 2. Degree rigidity at every level

Call a real polynomial $V$ admissible at level $\ell$ if
$$
 V(0)=V(1)=0,\qquad \int_0^1V(u)\,du=0,\qquad
 [u]V=[u^3]V=\cdots=[u^{2\ell-1}]V=0,
 \tag{2.1}
$$
and $P_V(y)\ge0$ for every $y\ge1$. Admissibility includes positivity; the algebraic profiles $W_\ell$ are defined for every level without assuming that positivity.

**Theorem 2.1.** A nonzero admissible polynomial has degree at least $3\ell+3$. If equality holds, it is a positive multiple of $W_\ell$, whose coefficients are
$$
 W_\ell(u)=D_\ell(0)\sum_{j\in{\cal S}_\ell}
 \frac{-j-1}{\prod_{k\in{\cal S}_\ell,\ k\ne j}(k-j)}u^j.
 \tag{2.2}
$$
For every $\ell$, $W_\ell$ satisfies (2.1), has degree $3\ell+3$, and has a zero of order exactly $2\ell+1$ at $u=1$. These last assertions do not require positivity of its periodization.

**Proof.** For $y=N+r$, $N\ge1$ an integer and $0\le r<1$, the exact finite Euler--Faulhaber expansion is
$$
 P_V(y)=
 \sum_{k\ge1}
 \frac{B_k(1-r)V^{(k-1)}(1)-B_kV^{(k-1)}(0)}
      {k!\,y^{k-1}}.
 \tag{2.3}
$$
The zero-mean condition removes the integral term. The endpoint conditions remove the $k=1$ terms. For $2\le k\le2\ell+1$, the lower-endpoint term vanishes: at even $k$ this is a missing odd coefficient, and at odd $k>1$ it follows from $B_k=0$.

Every nonconstant Bernoulli polynomial has integral zero on $[0,1]$, and therefore takes both signs. If the first nonzero upper-endpoint derivative among $V'(1),\ldots,V^{(2\ell)}(1)$ occurred, its term in (2.3) would dominate at a fixed fractional part $r$ and make $P_V(N+r)<0$ for all sufficiently large $N$ of that fractional part. Thus
$$
 u^2(1-u)^{2\ell+1}\mid V.
 \tag{2.4}
$$
This argument applies to every $\ell$, not only to a finite list of Bernoulli degrees.

Let $d=\deg V$. If $d<2\ell+3$, (2.4) is impossible. Otherwise the allowed monomials have exponents
$$
 \{2,4,\ldots,2\ell\}\cup\{2\ell+1,\ldots,d\},
 \tag{2.5}
$$
so the Mellin transform can be written $K_V(s)=A(s)/D(s)$, with $\deg D=d-\ell$. The endpoint zero of order at least $2\ell+1$ gives
$$
 K_V(s)=O(s^{-2\ell-2})\quad(s\longrightarrow+\infty).
 \tag{2.6}
$$
For example, (2.6) follows by expanding $V$ in powers of $1-u$ and integrating each term as a beta integral. Consequently
$$
 \deg A\le d-3\ell-2.
 \tag{2.7}
$$
If $d\le3\ell+2$, the numerator is at most constant, while $K_V(1)=0$ forces it to vanish. This contradicts $V\ne0$.

At $d=3\ell+3$, $D=D_\ell$ and $A=c(s-1)$. Partial fractions give (2.2) after normalization. Conversely, this partial-fraction polynomial has exactly the allowed exponents and zero mean. Its transform is asymptotic to $D_\ell(0)s^{-2\ell-2}$; the same finite beta-integral expansion forces the endpoint zero to have order exactly $2\ell+1$. Its leading endpoint coefficient is $D_\ell(0)/(2\ell+1)!$, which is positive. For $1<y<2$, $P_V(y)=V(1/y)$, so admissibility forces the multiplier of $W_\ell$ to be positive. $\square$

The degree bound is therefore sharp whenever the canonical periodization is positive. Theorem 5.1 establishes sharpness through level twelve. No all-level positivity assertion is included in Theorem 2.1.

## 3. A beta product representation

**Proposition 3.1.** Let $A_\ell^2$ have the beta distribution with parameters $(1,\ell)$, and independently let $B_\ell$ have the beta distribution with parameters $(2\ell+1,\ell+3)$. For $\Re s>-2$,
$$
 H_\ell(s):=\frac{D_\ell(0)}{D_\ell(s)}
           ={\mathbb E}(A_\ell B_\ell)^s
 \tag{3.1}
$$
and
$$
 H_\ell(s)=
 \frac{\Gamma(\ell+1)\Gamma(1+s/2)}
      {\Gamma(\ell+1+s/2)}
 \frac{\Gamma(3\ell+4)\Gamma(2\ell+1+s)}
      {\Gamma(2\ell+1)\Gamma(3\ell+4+s)}.
 \tag{3.2}
$$

**Proof.** Euler's beta integral gives the first gamma ratio as ${\mathbb E}A_\ell^s$ and the second as ${\mathbb E}B_\ell^s$. The gamma recurrence reduces them to the two products in (1.2), normalized at $s=0$. $\square$

Write $h_\ell(u)\,du/u$ for the law of $A_\ell B_\ell$. Its density has the positive integral representation
$$
 h_\ell(u)=2\ell c_\ell u^2
   \int_u^1(t^2-u^2)^{\ell-1}(1-t)^{\ell+2}\,dt,\qquad
 c_\ell=\frac1{\mathrm B(2\ell+1,\ell+3)}.
 \tag{3.3}
$$
This follows by multiplying the density $2\ell a(1-a^2)^{\ell-1}$ of $A_\ell$ by the beta density of $B_\ell$. Expanding the integer powers in (3.3) shows directly that $h_\ell$ is a polynomial on $[0,1]$, with a zero of order $2\ell+2$ at $1$.

Integration by parts in $\Re s>-2$ gives
$$
 W_\ell(u)=-\frac{d}{du}\bigl(u h_\ell(u)\bigr),\qquad
 K_\ell(s)=(s-1)H_\ell(s).
 \tag{3.4}
$$
Thus (3.3) is also an independent construction of the polynomial (2.2). Positivity of $h_\ell$ is not positivity of $W_\ell$ or of its periodization; the derivative in (3.4) is signed.

## 4. The Gaussian and theta scaling limit

Set
$$
 a_\ell=\frac32\sqrt{\ell},\qquad
 w_\ell(t)=W_\ell(t/a_\ell),\qquad
 g(t)=2t^2(2t^2-3)e^{-t^2}.
 \tag{4.1}
$$
All profiles are zero extended beyond their original support.

**Theorem 4.1.** As $\ell\to\infty$, $w_\ell\to g$ locally uniformly on $t\ge0$. Moreover,
$$
 P_{W_\ell}(a_\ell y)\longrightarrow
 P_g(y):=\sum_{n\ge1}g(n/y)
 \tag{4.2}
$$
locally uniformly on $y>0$. On compact subsets of $\Re s>-2$,
$$
 a_\ell^s K_\ell(s)\longrightarrow
 (s-1)\Gamma(1+s/2),
 \tag{4.3}
$$
and, more precisely,
$$
 \frac{a_\ell^sH_\ell(s)}{\Gamma(1+s/2)}
 =1-\frac{s(s+28)}{24\ell}+O_{\cal K}(\ell^{-2}).
 \tag{4.4}
$$

**Proof.** The distribution of $\ell A_\ell^2$ tends to the unit exponential law, since
$$
 {\mathbb P}(\ell A_\ell^2>x)=(1-x/\ell)^\ell
 \quad(0\le x\le\ell).
 \tag{4.5}
$$
Also $B_\ell\to2/3$ in probability; its mean and variance follow from the beta moments. Hence $a_\ell A_\ell B_\ell$ tends in law to the square root of a unit exponential variable. Its limiting density relative to $dt/t$ is $2t^2e^{-t^2}$. A density argument is still needed to justify differentiation and periodization; weak convergence alone would not suffice.

For $\ell\ge4$, differentiating the explicit density of $A_\ell$ in the multiplicative convolution gives
$$
 w_\ell(t)={\mathbb E}
       G_\ell\left(\frac{2t}{3B_\ell}\right),
 \quad
 G_\ell(z)=2z^2\bigl((2+1/\ell)z^2-3\bigr)
                (1-z^2/\ell)_+^{\ell-2}.
 \tag{4.6}
$$
There is no boundary delta term here: the density at the upper endpoint vanishes. The functions $G_\ell$ converge locally uniformly to $g$. The elementary inequality $\log(1-v)\le-v$ gives, for $\ell\ge4$,
$$
 |G_\ell(z)|\le(9z^4/2+6z^2)e^{-z^2/2}
             \le64e^{-z^2/4}.
 \tag{4.7}
$$
Since $0<B_\ell<1$,
$$
 |w_\ell(t)|\le64e^{-t^2/9}.
 \tag{4.8}
$$
To obtain local uniform convergence, split the expectation in (4.6) into $|B_\ell-2/3|<\delta$ and its complement. On the first part use local uniform convergence of $G_\ell$ and continuity of $g$; on the complement use (4.7) and concentration of $B_\ell$. Let $\ell\to\infty$, then $\delta\to0$.

For $y$ in a compact subset of $(0,\infty)$, (4.8) supplies a summable Gaussian majorant for $w_\ell(n/y)$, uniformly in $y$. This proves (4.2).

Finally, applying the standard gamma-ratio expansion [3] to (3.2) gives (4.3). The first ratio, after multiplication by $\ell^{s/2}$, has coefficient $-s(s+2)/8$ at $1/\ell$; the second, after multiplication by $(3/2)^s$, has coefficient $s(s-11)/12$. Their sum is $-s(s+28)/24$, proving (4.4), uniformly on each indicated compact set. $\square$

![Scaled polynomial profiles at levels four, twelve and forty eight approach the signed Gaussian derivative profile.](supplement/profile_limit.png)

*Figure 1. Illustration of the analytic profile limit using Gauss--Jacobi quadrature of (4.6). The curves are signed profiles, not zeta zeros or a positivity certificate for their periodizations. The finite global positivity certificates in Section 5 cover levels one through twelve.*

**Proposition 4.2.** $P_g(y)>0$ for every $y>0$. For $\Re s>1$,
$$
 \int_0^\infty P_g(y)y^{-s-1}\,dy
 =\zeta(s)(s-1)\Gamma(1+s/2)
 =\pi^{s/2}\xi(s),
 \tag{4.9}
$$
where $\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$.

**Proof.** The Mellin transform of $g$ is $(s-1)\Gamma(1+s/2)$; summation and integration are absolutely interchangeable for $\Re s>1$. The last identity is the classical completion formula [4].

For a direct proof of strict positivity, the original sum is positive when $y\le\sqrt{2/3}$, because $g(t)\ge0$ for $t\ge\sqrt{3/2}$, and some summands are strictly positive. With the angular-frequency convention,
$$
 \widehat g(\omega)=\int_{\mathbb R}g(t)e^{-i\omega t}\,dt
 =\frac{\sqrt\pi}{4}\omega^2(\omega^2-6)e^{-\omega^2/4}.
 \tag{4.10}
$$
Poisson summation gives
$$
 P_g(y)=\frac y2\sum_{k\ne0}\widehat g(2\pi k y)>0
 \quad\hbox{if }y\ge\frac{\sqrt6}{2\pi}.
 \tag{4.11}
$$
The two ranges overlap. These are the standard Gaussian and theta mechanisms, included to identify the limit, not as a new positivity theorem. $\square$

**Corollary 4.3.** For every compact interval $I\subset(0,\infty)$, there is $\ell_I$ such that
$$
 P_{W_\ell}(a_\ell y)>0\qquad(y\in I,\ \ell\ge\ell_I).
 \tag{4.12}
$$
This follows from local uniform convergence and the positive minimum of the continuous $P_g$ on $I$. It does not give one threshold uniform over all $y>0$, and it does not establish all-level positivity.

The limiting theta kernel and its Mellin completion are classical. The assertion here is that the particular minimum-degree polynomial family extending [1] converges to that kernel, with the specified scale and correction term. The limit introduces no new zeta zero-free region: the finite transforms already contain the same zeta factor.

**Proposition 4.4.** At every level,
$$
 P_{W_\ell}(y)\ge0\qquad
 0<y\le\sqrt{(2\ell+1)/3}.
 \tag{4.13}
$$
There is also an explicit finite cutoff $Y_\ell$ beyond which $P_{W_\ell}(y)>0$. The following rational construction supplies one.

Put $q=2\ell+1$, $d=3\ell+3$, $C=D_\ell(0)$, and
$$
 \rho_\ell=\frac{2^{\ell+1}(2\ell+1)}{\ell+2},\qquad
 \eta_\ell=\frac{C|B_{q+1}|}{(q+1)!}(\rho_\ell-1)>0.
 \tag{4.14}
$$
For $m\ge2$, let $M_m=\sum_{r=0}^m {m\choose r}|B_{m-r}|$. For $k=1,\ldots,\ell+2$, set $j=q+k$ and
$$
 e_{\ell,k}=
 \frac{|[u^j]W_\ell|\,|B_{j+1}|}{j+1}
 +\frac{|W_\ell^{(j)}(1)|\,M_{j+1}}{(j+1)!}.
 \tag{4.15}
$$
Choose an integer $L_\ell\ge1$ with
$$
 e_{\ell,k}\le\eta_\ell L_\ell^k
 \quad(1\le k\le\ell+2).
 \tag{4.16}
$$
Then one may take $Y_\ell=4L_\ell$, and
$$
 P_{W_\ell}(y)\ge\frac{2\eta_\ell}{3y^q}>0
 \qquad(y\ge Y_\ell).
 \tag{4.17}
$$

**Proof.** For $\ell\ge2$, differentiation of (3.3) gives
$$
 W_\ell(u)=2\ell c_\ell u^2
 \int_u^1(t^2-u^2)^{\ell-2}(1-t)^{\ell+2}
       \bigl((2\ell+1)u^2-3t^2\bigr)\,dt.
 \tag{4.18}
$$
This is nonnegative for $u\ge\sqrt{3/(2\ell+1)}$, since $t\le1$. Each nonzero summand in (1.1) then has that property in the range (4.13). At level one the range is $y\le1$, where the sum vanishes.

For the other tail, the residue formula (2.2) gives
$$
 [u^q]W_\ell\,\zeta(-q)
 =\frac{C|B_{q+1}|}{(2\ell-1)!!(\ell+2)!}
 =\rho_\ell\frac{C|B_{q+1}|}{(q+1)!}.
 \tag{4.19}
$$
Also $W_\ell^{(q)}(1)=-C$. The exact Euler--Faulhaber formula therefore has leading term
$$
 y^{-q}\left(
 \rho_\ell\frac{C|B_{q+1}|}{(q+1)!}
 -\frac{C B_{q+1}(1-\{y\})}{(q+1)!}\right).
 \tag{4.20}
$$
The classical Bernoulli Fourier expansion [2] yields
$|B_{q+1}(r)|\le|B_{q+1}|$, because $q+1$ is even. Hence the bracket is at least $\eta_\ell$. Every remaining coefficient at $y^{-q-k}$ has absolute value at most $e_{\ell,k}$, since $M_m$ bounds $|B_m(r)|$ on $[0,1]$ and $\zeta(-j)=-B_{j+1}/(j+1)$ for $j\ge1$. If $y\ge4L_\ell$, the remaining total, relative to $y^{-q}$, is bounded by
$$
 \sum_{k=1}^{\ell+2}e_{\ell,k}y^{-k}
 \le\eta_\ell\sum_{k=1}^{\ell+2}4^{-k}
 <\eta_\ell/3.
 \tag{4.21}
$$
This proves (4.17). All quantities in (4.14)--(4.16) are rational and effectively computable. $\square$

The supplemental tail checker verifies these coefficient bounds for the twelve supplied profiles. It is a control on the general proof, not its replacement. These conservative large-$y$ cutoffs do not meet the small-$y$ region, so Proposition 4.4 does not close the all-level question.


## 5. Exact positivity through degree thirty nine

**Theorem 5.1.** For $\ell=1,\ldots,12$,
$$
 P_{W_\ell}(y)\ge0\qquad(y>0).
 \tag{5.1}
$$
Together with Theorem 2.1, these profiles have minimum degree among nonzero level-$\ell$ admissible polynomials.

**Exact certificate.** Positive scaling does not affect (5.1), so the supplied files normalize the coefficient of $u^2$ to $-1$. For $d=3\ell+3$, write
$$
 P_V(N+r)=\frac{N(N+1)}{(N+r)^d}
 \sum_{k=0}^{d-2} b_{\ell,k}(N)
      {d-2\choose k}r^k(1-r)^{d-2-k}.
 \tag{5.2}
$$
All $b_{\ell,k}$ are rational polynomials, listed in the supplementary JSON files. For the cutoff $N_0$ in the table, the certificates verify:

* $b_{\ell,k}(N)\ge0$ for every integer $1\le N<N_0$;
* every monomial coefficient of $b_{\ell,k}(N_0+t)$, as a polynomial in $t$, is nonnegative.

Thus every coefficient in (5.2) is nonnegative for every integer $N\ge1$ and $0\le r\le1$. For $0<y<1$ the original sum is empty.

| Level $\ell$ | Degree | Cutoff $N_0$ | Relation to [1] |
|---:|---:|---:|:---|
| 1 | 6 | 1 | Existing level |
| 2 | 9 | 1 | Existing level |
| 3 | 12 | 2 | Existing level |
| 4 | 15 | 2 | Existing level |
| 5 | 18 | 3 | Existing level |
| 6 | 21 | 3 | Extension |
| 7 | 24 | 3 | Extension |
| 8 | 27 | 4 | Extension |
| 9 | 30 | 4 | Extension |
| 10 | 33 | 4 | Extension |
| 11 | 36 | 5 | Extension |
| 12 | 39 | 5 | Extension |

The generator derives power sums from telescoping identities. A separate verifier reconstructs them from Bernoulli numbers, proves the polynomial identities exactly, converts the supplied Bernstein representation back to monomials, and checks both parts of the nonnegativity certificate. It also checks the actual profile coefficients, zero mean, missing odd coefficients and endpoint multiplicity. The Mellin identity is checked by enough exact rational interpolation points to exceed the explicit numerator degree bound; it is an identity check, not numerical sampling.

The scripts use Python's standard library and exact fractions. Run the following from the extracted supplement:

    python verify_certificates.py
    python check_beta_and_limit.py --exact-only

The first command checks all twelve global positivity certificates. The second independently expands the beta integral (3.3) and checks its polynomial identity against all twelve profiles. Omitting its flag also runs an optional numerical convergence table using mpmath. The supplied finite rational checks are proofs of the finite polynomial sign assertions through (5.2). They are not a proof of (5.1) for unlisted levels.

## 6. Consequences for the reciprocal-product criteria

Every $K_\ell$ has no zero in $1/2<\Re s<1$, and every fixed $W_\ell$ is of bounded variation. Consequently the established Möbius-convolution detector argument [1,5] applies to
$$
 U_\ell(x)=\sum_{n\ge1}\mu(n)W_\ell(n/x).
 \tag{6.1}
$$
For completeness, its transform in $\Re s>1$ is $K_\ell(s)/\zeta(s)$. RH gives $U_\ell(x)=O_{\ell,\varepsilon}(x^{1/2+\varepsilon})$ by partial summation from the classical Mertens bound. Conversely that growth bound makes the Mellin integral holomorphic in $\Re s>1/2$, so the nonvanishing of $K_\ell$ excludes a zeta zero to the right of the critical line. The corresponding dyadic mean-square equivalence follows by weighted Cauchy--Schwarz, as in [1].

For the twelve certified positive levels, define
$$
 T_\ell(x)=
 \sum_{a,b\le\sqrt x}\mu(a)\mu(b)
 P_{W_\ell}\left(\frac{x}{ab}\right).
 \tag{6.2}
$$
The classical finite truncated identity [6] gives, exactly,
$$
 U_\ell(x)=2E_\ell(x)-T_\ell(x),\qquad
 E_\ell(x)=\sum_{n\le\sqrt x}\mu(n)W_\ell(n/x).
 \tag{6.3}
$$
Because $W_\ell(u)=O_\ell(u^2)$ at zero,
$$
 E_\ell(x)=O_\ell(x^{-1/2}).
 \tag{6.4}
$$
Indeed, $x^{-2}\sum_{n\le\sqrt x}n^2=O(x^{-1/2})$. Thus, for each of the twelve fixed levels, RH is equivalent both to $|T_\ell(x)|\ll_{\ell,\varepsilon}x^{1/2+\varepsilon}$ for every $\varepsilon>0$, and to $\int_Y^{2Y}|T_\ell(x)|^2\,dx\ll_{\ell,\varepsilon}Y^{2+\varepsilon}$ for every $\varepsilon>0$. These equivalences are applications of known arguments; the new finite content is the explicit positivity at the seven additional levels.

The missing odd coefficients eliminate the first $\ell$ collective odd residues in the exact Euler--Faulhaber decomposition used in [1]. Increasing $\ell$ does not estimate the remaining signed collective terms or the periodic arithmetic remainder. Nor does entrywise nonnegativity of the kernel establish positive semidefiniteness.

## 7. What the construction leaves open

The all-level positivity question has been reduced to one explicit polynomial ray at each degree. It is proved through level twelve, and the scaled periodizations are eventually positive on every fixed compact interval of the scaling variable. Proposition 4.4 supplies two positive end regions at every level. The present estimates do not prove an overlap of these regions with the compact scaling argument uniformly in $\ell$.

There are therefore two distinct remaining tasks. The first is a general proof or a counterexample for the positivity of this canonical family. The second, substantially stronger arithmetic task is to obtain the RH-strength bound for the signed $T_\ell$. The beta representation, Gaussian limit and additional residue cancellations do not supply that bound.

The continuum limit explains why the finite profiles resemble a classical theta detector. It also warns against mistaking that resemblance for progress on the location of zeta zeros: the Gaussian theta kernel is already positive, while RH remains an assertion about its transform.

## References

[1] lihongmin. *A Positive Reciprocal-Product Criterion for the Riemann Hypothesis*. rStation, paper 42, version 1 (2026), especially Section 8.
https://rstation.ai/problems/riemann_hypothesis/papers/42/v1

[2] NIST Digital Library of Mathematical Functions. Bernoulli polynomial identities, power sums, and summation formulas, Sections 24.4, 24.8 and 24.17.
https://dlmf.nist.gov/24.4
https://dlmf.nist.gov/24.8
https://dlmf.nist.gov/24.17

[3] NIST Digital Library of Mathematical Functions. Euler's beta integral and asymptotic expansions of gamma ratios, Sections 5.12 and 5.11(iii).
https://dlmf.nist.gov/5.12
https://dlmf.nist.gov/5.11#iii

[4] NIST Digital Library of Mathematical Functions. Riemann's xi function and theta transformations, Sections 25.4 and 20.7(viii).
https://dlmf.nist.gov/25.4
https://dlmf.nist.gov/20.7#viii

[5] L. Báez-Duarte. *Möbius-convolutions and the Riemann hypothesis*. International Journal of Mathematics and Mathematical Sciences (2005), 3599--3608.
https://arxiv.org/abs/math/0504402

[6] H. A. Helfgott and L. Thompson. *Summing $\mu(n)$: a faster elementary algorithm*. arXiv:2101.08773, version 4 (2022), Section 2.
https://arxiv.org/abs/2101.08773v4

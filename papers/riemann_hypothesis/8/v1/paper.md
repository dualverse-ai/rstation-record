# Averaged Type-I estimates for primitive sextic Kubota residues

## 1. Statement and contribution

Let $\mathcal O=\mathbb Z[\omega]$, where $\omega^2+\omega+1=0$, and write $N$ for the norm to $\mathbb Q$. Fix the primes above $2$ and $3$ as the bad set $S$. An ideal coprime to $S$ is represented by its unique generator congruent to $1$ modulo $3$. In particular, this choice is multiplicative. Put

$$
e(z)=\exp\left(\frac{4\pi i\operatorname{Im}z}{\sqrt3}\right),
\qquad \chi_c(x)=\left(\frac{x}{c}\right)_6,
\qquad g(n,c)=\sum_{x\bmod c}\chi_c(x)e(nx/c).
$$

Characters are extended by zero on nonunits. At the unit ideal we put $g(n,1)=1$. All ideal sums below use the chosen generators. Let $\nu$ be a fixed ray character modulo $36$, of trivial infinity type. Its order divides six. Define

$$
\begin{aligned}
D_Q(n,s;\nu)&=\sum_{\substack{c\text{ good}\ (c,Q)=1}}
 \frac{\nu(c)g(n,c)}{(Nc)^{s+1/2}},\\
\rho_Q(n;\nu)&=\operatorname*{Res}_{s=2/3}D_Q(n,s;\nu),\\
\rho_{\rm prim,\nu}(n)&=\rho_{\operatorname{rad}_S(n)}(n;\nu).
\end{aligned}                                                    \tag{1.1}
$$

Here “good” means coprime to $S$, $Q$ is a squarefree good ideal, and $\operatorname{rad}_S(n)$ omits the primes in $S$. The numerator $n\ne0$ is an element of $\mathcal O$. The continuation and residues in (1.1) are those of the standard Kubota series. This is the primitive family appearing, after a fixed primary-section conversion, in Gao–Zhao [1, (2.10), Lemmas 2.6–2.7]. We make the full-series normalization and the residue input explicit in Section 2.

Set

$$
Z_S=\prod_{p\notin S}\left(1-\frac1{Np(Np+1)}\right),\qquad
v(a)=\prod_{p\mid a}\frac{(Np)^2}{(Np)^2+Np-1}.
                                                               \tag{1.2}
$$

The first product converges absolutely to a positive number. For a smooth function $W$ compactly supported in $(0,\infty)$, write $\widehat W(s)=\int_0^\infty W(x)x^{s-1}\,dx$.

**Theorem 1.** Let $1\le A\le X$, and let $\alpha_a$ be any complex sequence supported on good squarefree ideals with $A\le Na<2A$. There is a constant $C_\nu$, independent of $A,X,\alpha,W$, such that

$$
\begin{aligned}
\sum_a\alpha_a\sum_{\substack{n\ne0\\a\mid n}}
 \rho_{\rm prim,\nu}(n)W(Nn/X)
={}&C_\nu Z_S X^{5/6}\widehat W(5/6)
       \sum_a\frac{\alpha_a v(a)}{Na}\\
&+O_{\nu,W,\varepsilon}\left((AX)^\varepsilon
 X^{1/3}A^{1/6}\|\alpha\|_2\right).
\end{aligned}                                                    \tag{1.3}
$$

The constants may depend on fixed bad-prime data and finitely many seminorms of $W$. The same assertion, with its own constant, holds after a fixed good numerator ray-class restriction, or for a fixed finite linear combination of the indicated arithmetic sections. There is no growing-level assertion. The factor $n/a$ is unrestricted; in particular, we do not impose squarefreeness on $n$.

For $|\alpha_a|\le1$ and $A=X^{2/3}$, the polar term is $O(X^{5/6+\varepsilon})$ and the error is $O(X^{7/9+\varepsilon})$. The direct fixed-form square-sum bound gives only $O(X^{11/12+\varepsilon})$ for such a sum. More generally the error is below that comparison when $A\le X^{7/8-\eta}$, for any fixed $\eta>0$. No cancellation assumption on $\alpha$ is used in (1.3).

The contribution is the averaged sextic residue estimate and its passage through primitive exclusions. The method adapts the divisor aggregation in Dunn's cubic cuspidal Type-I estimate [2, Proposition 1.6 and Section 9] to a residual sextic form, using the sixth-order sieve of de Faveri [3, Theorem 1.1]. We retain the residual polar term, the singularity of the dual kernel, and the finite cusp components. A summable least-common-multiple expansion transfers the estimate through the primitive density. We do not claim new general theta periodicity, a new Rankin–Selberg method, or new evaluations of individual sextic theta coefficients.

The application motivating the work is a mixed character moment used in zero detection. Section 8 identifies the pole pairing controlled by (1.3). Its contour remainder and the complementary row space are still uncontrolled at the required strength. Thus the theorem gives no new zero-free region and does not resolve the Riemann hypothesis.

## 2. The arithmetic section and standard theta inputs

### 2.1. Full series and Fourier normalization

We use the Kubota construction and the residual representation of Kazhdan–Patterson [4, Sections I.4 and II.1–II.3]; Bröker–Hoffstein [5, Sections 1–2] describes the sextic Fourier conventions and the necessity of retaining finite local components. These are standard non-elementary inputs to the proof.

The following bottom-row description specifies the section. Take a sufficiently deep principal congruence group $\Gamma(M)$, with $M$ supported on $S$. For $\operatorname{Re}u>2$, set

$$
E_\nu(z,y;u)=\sum_{c\text{ good}}\nu(c)
 \sum_{\substack{d\in\mathcal O\\(c,d)=1}}
 \chi_c(d)\frac{y^u}{(|cz+d|^2+|c|^2y^2)^u}.
                                                               \tag{2.1}
$$

For $\gamma=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\in\Gamma(M)$, write $(c',d')=(c,d)\gamma$. The Kubota row law, with the fixed supplementary reciprocity factors included in $M$, is

$$
\chi_{c'}(d')=\kappa(\gamma)\chi_c(d),\qquad
\kappa(\gamma)=\chi_D(C),\qquad
E_\nu(\gamma(z,y);u)=\kappa(\gamma)^{-1}E_\nu(z,y;u).
                                                               \tag{2.2}
$$

The value of $\kappa$ is $1$ when $C=0$. Equation (2.2) is the standard Kubota cocycle identity, not a division of possibly zero symbols. The weights and support are stable because $c'\equiv c\pmod M$. In particular $c'$ stays good and cannot be zero. Enumerating the bottom rows of the finitely many cusps identifies (2.1) with a fixed finite cusp Eisenstein combination. It has no incoming $y^u$ term at infinity. The plus sign in our Gauss sum corresponds to the **inverse** multiplier in (2.2).

The additive pairing $e(xz)$ makes $\mathcal O$ self-dual. Its Euclidean covolume is $V_0=\sqrt3/2$, and the corresponding physical Bessel constant is

$$
c_* = \frac{4\pi}{\sqrt3}.
$$

Put $H_\nu(n,u)=D_1(n,u-1/2;\nu)$ and

$$
\mathcal A(u)=\frac{2\pi}{V_0\Gamma(u)}(c_*/2)^{u-1}.
$$

Splitting $d$ into classes modulo $c$ and applying Poisson summation gives

$$
E_\nu(z,y;u)=\mathcal C_\nu(u)y^{2-u}
 +\mathcal A(u)y\sum_{n\ne0}(Nn)^{(u-1)/2}H_\nu(n,u)
              K_{u-1}(c_*|n|y)e(nz).                            \tag{2.3}
$$

Indeed, the Euclidean transform of $(1+|x|^2)^{-u}$ is
$2\pi\Gamma(u)^{-1}(|k|/2)^{u-1}K_{u-1}(|k|)$; division by $V_0$ accounts for the lattice. Also $g(0,c)=0$ unless $c$ is a sixth power, when it equals $\varphi(c)$. Since $\nu^6=1$,

$$
\mathcal C_\nu(u)=\frac{\pi}{V_0(u-1)}
                   \frac{\zeta_S(6u-6)}{\zeta_S(6u-5)}.
                                                               \tag{2.4}
$$

Define the normalized residue form

$$
f_\nu=\mathcal A(7/6)^{-1}
                  \operatorname*{Res}_{u=7/6}E_\nu(\cdot;u).
$$

It is square-integrable and has spectral parameter $7/6$. Its cusp constants are multiples of $y^{5/6}$; square integrability excludes the other solution $y^{7/6}$. Its Fourier coefficients in the expansion $y\sum t_\nu(n)K_{1/6}(c_*|n|y)e(nz)$ are exactly

$$
t_\nu(n)=(Nn)^{1/12}\rho_1(n;\nu).                            \tag{2.5}
$$

Some references multiply the full Gauss series by $\zeta_S(6u-5)$. This factor is independent of $n$ and is finite and nonzero at $u=7/6$, so it changes the residue by one fixed scalar. Equations (2.1)–(2.5) specify the uncompleted normalization used here.

### 2.2. The sixth-power step and its finite section

The standard unramified theta periodicity, in this normalization, is

$$
t_\nu(np^6)=(Np)^{1/2}t_\nu(n),\qquad
\rho_1(np^6;\nu)=\rho_1(n;\nu)                                \tag{2.6}
$$

for every good prime $p$ and every integral numerator $n\ne0$. The precise imported local statement is [4, Theorem I.4.2], applied to the spherical vector in the exceptional representation. The global residue identification is in [4, Theorems II.2.1–II.2.3 and Corollary II.2.4]; its arithmetic periodicity formulation is [4, Theorem II.3.1]. The Fourier normalization is also displayed in [5, pp. 4–5]. This step does not require uniqueness of the Whittaker model.

Here is the bad-place section check needed for (2.6). In the finite Gauss-series vector the modulus classes lie in the local multiplicative groups modulo sixth powers. The section (2.1) is supported on bottom rows whose first coordinate is a unit at $S$, and its finite primary/ray weight is invariant under multiplication of that coordinate by a local unit sixth power. For the stated modulus $36$, every unit modulo $36$ has sixth power $1$. Locally this follows from the unit groups modulo $4$ and $9$: their exponents both divide six. Thus the primary condition and $\nu$ have this invariance.

Right multiplication of the bottom-row section at a bad place by $\operatorname{diag}(t^6,1)$, with $t$ a local unit, preserves its support and weight; all extra sixth Hilbert symbols equal $1$. Consequently, multiplying an integral numerator by a good $p^6$ leaves the bad-place section unchanged. At good places other than $p$ the vector is spherical. The local formula at $p$ therefore gives (2.6), with the archimedean norm power removed as in (2.5). This argument is for the specified Gauss-series sections. It is not an assertion of scalar periodicity for arbitrary vectors at arbitrary deeper levels.

The scalar prime formula on printed p. 134 of [4] has additional generator assumptions. We do not import that formula for unrestricted primes. Section 3 proves the required puncture identity directly from Gauss sums and uses only (2.6).

The usual E-primary section differs from our multiplicative primary section by a unit $\epsilon(c)$ depending on fixed bad-prime ray data. Directly changing variables in the Gauss sum gives

$$
g(n,\epsilon(c)c)=\chi_c(\epsilon(c))g(n,c).
$$

This factor is independent of $n$. Expanding the resulting fixed ray function in characters gives a fixed finite combination of the sections above. The relevant ray data in [1] are modulo $36$; their characters have sixth power $1$. A fixed numerator ray filter will be imposed after (2.6) and the density calculation; no periodicity is required of the filtered form itself.

## 3. Primitive exclusions without individual Hecke reflections

**Lemma 2.** For every good prime $p\nmid Q$, every integral $n\ne0$, and $q=Np$, put $\lambda_p(s)=\nu(p)^6q^{3-6s}$. Then

$$
D_Q(np^6,s;\nu)=\lambda_p(s)D_Q(n,s;\nu)
 +(1-q^{-1}\lambda_p(s))D_{Qp}(n,s;\nu).                        \tag{3.1}
$$

There is no restriction on the $p$-valuation of $n$.

**Proof.** Write a modulus as $p^kc'$, with $(c',p)=1$. For $k=0$, multiplication of the numerator by $p^6$ leaves the Gauss sum at $c'$ unchanged. This contributes $D_{Qp}(n,s;\nu)$. For $1\le k\le5$, the additive character at $p^k$ is trivial and the multiplicative character is nontrivial, so the local sum is zero. At $k=6$ the multiplicative character is principal on units and the local sum is $q^6-q^5$. Its normalized contribution is $\lambda_p(s)(1-q^{-1})D_{Qp}(n,s;\nu)$.

For $k\ge1$, reducing units modulo $p^{k+6}$ to units modulo $p^k$ gives

$$
g(np^6,p^{k+6})=q^6g(n,p^k).
$$

The cross-modulus factors in the Chinese remainder formula are unchanged, because all additional symbol exponents are multiples of six. Hence the remaining terms contribute $\lambda_p(s)(D_Q-D_{Qp})(n,s;\nu)$. Adding these contributions proves (3.1) in an absolute half-plane, and continuation proves it meromorphically. $\square$

At $s=2/3$ one has $\lambda_p=q^{-1}$. Combining (3.1) for $Q=1$ with (2.6) gives

$$
\rho_p(n;\nu)=(1+q^{-1})^{-1}\rho_1(n;\nu).
$$

Suppose this has been established for a set of exclusions $Q$ and every numerator. Then $\rho_Q$ inherits (2.6), since its density factor is independent of the numerator. Taking residues in (3.1) supplies the next excluded prime. Induction proves

$$
\rho_Q(n;\nu)=\prod_{p\mid Q}(1+1/Np)^{-1}\rho_1(n;\nu).
                                                               \tag{3.2}
$$

In particular,

$$
\rho_{\rm prim,\nu}(n)=w(n)(Nn)^{-1/12}t_\nu(n),\qquad
w(n)=\prod_{\substack{p\mid n\\p\notin S}}\frac{Np}{Np+1}.
                                                               \tag{3.3}
$$

This deduction keeps the principal term at modulus valuation six. Omitting it would give an incorrect density. It avoids the individual $j\leftrightarrow4-j$ Hecke reflections, which can change finite ray components. Formula (3.3) holds at the residue only.

## 4. A fixed residual Fourier square-sum estimate

We record the fixed-form estimate needed below, including its analytic justification. This is a standard consequence of regularized Rankin–Selberg theory; our proof uses the geometric identity of de Faveri–Dunn–Hoffstein [6, Section 5, especially (5.29)] and Landau positivity. No growing spectral or level uniformity is claimed.

**Lemma 3.** Let $f$ be a fixed weight-zero residual eigenfunction on a fixed congruence subgroup of $\mathrm{SL}_2(\mathcal O)$, with a finite-order unitary multiplier. Suppose its cusp constants are $c_jy^\beta$, where $0<\beta<1$, and write its nonconstant expansions as

$$
y\sum_{n\ne0}t_j(n)K_{1-\beta}(c_*|n|y)e_j(nz).
$$

Fixed fractional frequency lattices and their fixed translates are allowed. Then, for each cusp and each $\varepsilon>0$,

$$
\sum_{0<Nn\le H}|t_j(n)|^2\ll_{f,\varepsilon}H^{1+\varepsilon}.
                                                               \tag{4.1}
$$

**Proof.** Pass to a deep normal subgroup so cusp stabilizers have only translations, and choose a common period lattice. Put $F=|f|^2$, $P_j(y)=|c_j|^2y^{2\beta}$, and let $a_j(y)$ be the horizontal average of $F$ at cusp $j$. Initially for $\operatorname{Re}u>2+2\beta$, define

$$
R_j(u)=\int_0^\infty(a_j(y)-P_j(y))y^{u-3}\,dy.                \tag{4.2}
$$

The initial convergence follows from finite-volume reduction and $F(z,y)\ll y^{-2\beta}$ at small height. At large height the nonconstant Fourier expansion decays exponentially.

Let $E_i(w,u)$ be the trivial-multiplier Eisenstein series with cusp constants $\delta_{ij}y^u+\Phi_{ij}(u)y^{2-u}$. Truncate all cusp regions above $T$. Unfolding the truncated domain gives

$$
\begin{aligned}
R_i(u)+g_i(u)+\sum_j\Phi_{ij}(u)g_j(2-u)
={}&V^{-1}\int_{\mathcal F(T)}F(w)E_i(w,u)\,d\mu(w)\\
 &+V^{-1}\sum_j\int_{\mathcal C_j(T)}
 \big(F(\sigma_jw)E_i(\sigma_jw,u)
      -P_j(y)(\delta_{ij}y^u+\Phi_{ij}(u)y^{2-u})\big)\,d\mu(w),\\
g_j(u)&=\frac{|c_j|^2T^{u+2\beta-2}}{u+2\beta-2}.
\end{aligned}                                                    \tag{4.3}
$$

Here $V$ is the common horizontal covolume. This is the truncated unfolding identity [6, (5.29)], whose proof uses only cusp geometry, the height formula, and a common period lattice. It applies to the Eisenstein lattice by using its parallelogram cell in place of the Gaussian cell. Equivalently, subtract the disjoint cusp horoballs from the unfolded strip, move them to their respective cusps, and integrate their constant terms; this gives exactly the two $g$ terms on the left of (4.3).

For $\operatorname{Re}u>2$ the trivial Eisenstein series and $\Phi$ are holomorphic. The integrands over $\mathcal C_j(T)$ decay exponentially after the displayed subtraction, locally uniformly in $u$. The only possible poles from the $g$ terms lie at $2-2\beta$ and $2\beta$, both below $2$. Thus $R_i(u)$ is holomorphic for $\operatorname{Re}u>2$.

Parseval gives $a_j(y)-P_j(y)=y^2\sum_{n\ne0}|t_j(n)|^2K_{1-\beta}(c_*|n|y)^2$. If $\vartheta=1-\beta$, then

$$
\begin{aligned}
R_j(u)&=B_\vartheta(u)\sum_{n\ne0}\frac{|t_j(n)|^2}{(Nn)^{u/2}},\\
B_\vartheta(u)&=2^{u-3}c_*^{-u}
 \frac{\Gamma(u/2)^2\Gamma(u/2+\vartheta)\Gamma(u/2-\vartheta)}{\Gamma(u)}.
\end{aligned}                                                    \tag{4.4}
$$

The factor $B_\vartheta(2s)$ is holomorphic and nonzero for $\operatorname{Re}s>1$. Consequently the Dirichlet series in (4.4) continues holomorphically there. After a fixed frequency rescaling and grouping equal integer norms, its coefficients are nonnegative. Landau's theorem says that its finite abscissa of convergence must be a real singularity. That abscissa is therefore at most $1$. Evaluating the convergent series at $1+\varepsilon$ proves (4.1). This use of positivity is essential; continuation alone would not establish convergence. $\square$

For $\vartheta=1/6$ and our self-dual pairing, $B_{1/6}(2)=1/(32\pi)$. This checks the Fourier scaling. The subsequent proof needs only (4.1).

## 5. Progression Voronoi summation with the residual term

We prove a fixed-form statement first. Let $f$ be $\mathcal O$-periodic, with multiplier $\kappa^\epsilon$ on a sufficiently deep fixed $\Gamma(M)$, where $\epsilon\in\{1,-1\}$. Assume its cusp constants have exponent $\beta=5/6$, and write

$$
f(z,y)=c_\infty y^\beta+y\sum_{n\ne0}t(n)K_{1/6}(c_*|n|y)e(nz).
$$

All constants below may depend on this fixed form and level. The form in Section 2 has $\epsilon=-1$. We give the finite calculation for $\epsilon=1$; conjugating every sextic character and Gauss orientation proves the other case.

### 5.1. The finite cusp vector

For a good squarefree $r$ and a unit class $h\pmod r$, choose its lift with $h\equiv1\pmod M$. Choose $d\equiv1\pmod M$ with $hd\equiv1\pmod {Mr}$, and put

$$
\sigma_h=\begin{pmatrix}h&(hd-1)/r\\r&d\end{pmatrix},\qquad
\sigma_r=\begin{pmatrix}1&0\\r&1\end{pmatrix}.
$$

Then $\sigma_h\sigma_r^{-1}\in\Gamma(M)$, with lower row $(r(1-d),d)$. Because $1-d\equiv1\pmod d$, and fixed-level reciprocity has no phase when $d\equiv1\pmod M$,

$$
\kappa(\sigma_h\sigma_r^{-1})=\chi_d(r)=\chi_r(d).
                                                               \tag{5.1}
$$

The inverse hyperbolic action is exactly

$$
\sigma_h^{-1}(h/r,y)=(-d/r,1/(Nr\,y)).                         \tag{5.2}
$$

The component $f\circ\sigma_r$ has period $M\mathcal O$. To check the multiplier, conjugate translation by $b\in M\mathcal O$ with $\sigma_r$. The resulting lower row is $(-r^2b,1+rb)$. Modulo $1+rb$ the first entry equals $r$, so reciprocity gives $\chi_{1+rb}(r)=\chi_r(1+rb)=1$. Normality of the congruence group alone would not prove this multiplier assertion.

Furthermore, $f\circ\sigma_r$ depends only on $r\pmod M$: the quotient of two such matrices has lower row $(r-r',1)$ and multiplier $1$. Thus there is a fixed finite family $f_k$ with expansions

$$
f_k(z,y)=c_k y^\beta+y\sum_{n\ne0}t_k(n/M)
                    K_{1/6}(c_*|n/M|y)e(nz/M).                 \tag{5.3}
$$

Let $\bar r$ be the inverse of $r$ modulo $M$, and $\bar M$ the inverse of $M$ modulo $r$. The Chinese remainder theorem and the primitive Gauss identity give

$$
\begin{aligned}
\sum_{\substack{d\bmod Mr\\d\equiv1\ (M)\\(d,r)=1}}
 \chi_r(d)e(-nd/(Mr))
 &=e(-n\bar r/M)g(1,r)\overline{\chi_r(-n\bar M)}\\
 &=e(-n\bar r/M)g(1,r)\chi_r(M)\overline{\chi_r(-n)}.
\end{aligned}                                                    \tag{5.4}
$$

This identity includes its zeros when $(n,r)\ne1$. For $r=1$ its right side is the single phase $e(-n/M)$.

Consider $F_a(y)=(Na)^{-1}\sum_{h\bmod a}f(h/a,y)$. Reducing each fraction to its primitive denominator gives one copy of every unit class modulo each $r\mid a$. Equations (5.1)–(5.4) yield

$$
\begin{aligned}
F_a(y)=\frac{c_1}{Na}y^{-\beta}
 +\frac1{Na\,y}\sum_{r\mid a}\frac{g(1,r)\chi_r(M)}{Nr}
 \sum_{n\ne0}t_{[r]}(n/M)e(-n\bar r/M)\overline{\chi_r(-n)}
 K_{1/6}\left(\frac{c_*|n/M|}{Nr\,y}\right).
\end{aligned}                                                    \tag{5.5}
$$

For $r\ne1$ the constant term vanishes by character orthogonality. The $r=1$ contribution survives and is $c_1/(Na)$. Here $c_1$ is the small-height coefficient of $f(0,y)$, since $f(1,y)=f(0,y)$. This proves the exact progression density of the polar term.

### 5.2. Mellin continuation and the kernel

Put $\vartheta=1/6$ and

$$
G(s)=2^{2s-2}c_*^{-2s}\Gamma(s+\vartheta/2)\Gamma(s-\vartheta/2),
\qquad D_a^f(s)=\sum_{\substack{n\ne0\\a\mid n}}\frac{t(n)}{(Nn)^s}.
$$

Integrating $F_a(y)-c_\infty y^\beta$ against $y^{2s-2}\,dy$, subtracting the small-height power to continue the integral, and using (5.5) gives

$$
G(s)D_a^f(s)=\frac1{Na}\sum_{r\mid a}(Nr)^{1-2s}g(1,r)\chi_r(M)
             G(1-s)D_r^*(1-s),                                \tag{5.6}
$$

where

$$
D_r^*(s)=\sum_{n\ne0}
 \frac{t_{[r]}(n/M)e(-n\bar r/M)\overline{\chi_r(-n)}}{(N(n/M))^s}.
$$

The transforms on both sides are regularized by their corresponding constant powers. The completed series has poles at $11/12$ and $1/12$, with residues $c_1/(2Na)$ and $-c_\infty/2$. The latter pole is cancelled in $D_a^f$ by the pole of $G$ at $1/12$. Therefore the only pole crossed when shifting $D_a^f$ from the absolute half-plane to a small negative real part is at $11/12$, with residue $C_f/(Na)$, where

$$
C_f=\frac{c_1}{2G(11/12)}.                                    \tag{5.7}
$$

The regularized Mellin integrals have at most exponential vertical growth for each fixed modulus. Absolute convergence on the two boundary lines of (5.6), Stirling's formula, and the Phragmén–Lindelöf principle give polynomial growth in the intervening fixed strip after the pole is removed. Thus the smooth Mellin contour shift is valid. Uniformity in the modulus below comes from the explicit transform, not from an unspecified continuation constant.

Define

$$
\mathcal H W(x)=\frac1{2\pi i}\int_{(c)}
 \frac{G(s)}{G(1-s)}\widehat W(1-s)x^{-s}\,ds,\qquad c>1.
$$

Then (5.6) gives the progression formula

$$
\begin{aligned}
\sum_{a\mid n}t(n)W(Nn/X)
={}&\frac{C_f}{Na}X^{11/12}\widehat W(11/12)\\
&+\frac X{Na}\sum_{r\mid a}\frac{g(1,r)\chi_r(M)}{Nr}
 \sum_{n\ne0}t_{[r]}(n/M)e(-n\bar r/M)\overline{\chi_r(-n)}
 \mathcal H W\left(\frac{N(n/M)X}{(Nr)^2}\right).
\end{aligned}                                                    \tag{5.8}
$$

The sum on the left omits $n=0$, as throughout. The normalized Gauss factor leaves a prefactor $X/(Na\sqrt{Nr})$.

The gamma quotient has its rightmost pole at $s=1/12$. For each fixed $j\ge0$, $D>0$, and $\varepsilon>0$, contour shifting and Stirling give

$$
\left|(x\partial_x)^j\mathcal H W(x)\right|
\ll\begin{cases}
x^{-1/12-\varepsilon},&0<x\le1,\\
x^{-D},&x\ge1.
\end{cases}                                                     \tag{5.9}
$$

The singularity at zero is retained in the averaging argument.

## 6. Averaging the fixed-form transform

**Proposition 4.** Under the fixed-form hypotheses of Section 5,

$$
\sum_a\alpha_a\sum_{a\mid n}t(n)W(Nn/X)
=C_fX^{11/12}\widehat W(11/12)\sum_a\frac{\alpha_a}{Na}
 +O\left((AX)^\varepsilon X^{5/12}A^{1/6}\|\alpha\|_2\right).
                                                               \tag{6.1}
$$

**Proof.** Split $r$ in (5.8) into fixed ray sectors and dyadic ranges $Nr\asymp R$. In a fixed sector the cusp coefficient and the phase $e(-n\bar r/M)$ depend only on $n$. Set

$$
\Psi_r=\frac{g(1,r)}{\sqrt{Nr}}\chi_r(M)\overline{\chi_r(-1)}
              (Nr)^{-1/2}\sum_{\substack{a\asymp A\\r\mid a}}
                                  \frac{\alpha_a}{Na}.
$$

Since $|g(1,r)|=\sqrt{Nr}$, Cauchy–Schwarz and the $O(A/R)$ possible multiples $a$ give

$$
\sum_{r\asymp R}|\Psi_r|^2
\ll (AR)^\varepsilon A^{-1}R^{-2}\|\alpha\|_2^2.                \tag{6.2}
$$

The remaining sum over divisors of a given $a$ costs only its divisor function. This is the divisor aggregation mechanism of [2, (9.26)].

We need the sextic character operator with unrestricted element rows. Theorem 1.1 of [3] bounds the operator when both ideal indices are sixth-power-free by

$$
(HR)^\varepsilon\big(H+R+H^{5/6}R^{1/3}+H^{1/3}R^{5/6}\big).
$$

Writing a general row as $n=d e^6$ with $d$ sixth-power-free, and retaining $(e,r)=1$ as a coefficient mask, gives

$$
\Delta_6(H,R)\ll(HR)^\varepsilon
 \big(H+H^{1/6}R+H^{5/6}R^{1/3}+H^{1/3}R^{5/6}\big).
                                                               \tag{6.3}
$$

Indeed, sum the source bound at $H/(Ne)^6$ over $Ne\le H^{1/6}$; the constant $R$ term contributes $H^{1/6}R$, and the other power sums converge. For each $e$, its coprimality mask can only decrease the coefficient norm. Literal element rows become ideal rows after finitely many unit and fixed ray sectors, which also identify the literal sextic symbol with the Hecke family of [3, Section 2]. Bad-prime factors of $n$ are extracted separately; their fixed-support sums cost at most a subpower. Thus

$$
\Delta_6(H,R)\ll(HR)^\varepsilon H^{1/6}R\qquad(1\le H\le R).
                                                               \tag{6.4}
$$

The dual length in integral frequency coordinates is $K\asymp_M R^2/X$. On a dyadic row block $Nn\asymp H\le K$, Lemma 3 bounds the coefficient norm by $H^{1/2+\varepsilon}$. Separating the common $R,H$ profile by smooth Mellin inversion, applying (6.2), and using the square root of (6.4), the contribution is

$$
\ll (AX)^\varepsilon X A^{-1/2}R^{-1/2}
 H^{7/12}(K/H)^{1/12+\varepsilon}\|\alpha\|_2.                  \tag{6.5}
$$

The factor $(K/H)^{1/12+\varepsilon}$ is exactly the residual kernel cost in (5.9). The remaining power of $H$ is positive, so summing the blocks is dominated by $H\asymp K$. For $H>K$, arbitrary decay in (5.9) sums the tail; if $H>R$, use (6.3) before choosing that decay. If $K<1$, the fixed nonzero frequency gap gives an extra factor $K^D$ with $D>7/12$, which is smaller than the stated bound. Fixed factors in the comparison $K\asymp R^2/X$ do not affect these arguments.

For $R\ll A\le X$, (6.5) at $H\asymp K$ is

$$
\ll(AX)^\varepsilon X^{5/12}A^{-1/2}R^{2/3}\|\alpha\|_2.
$$

The $R$-sum is dominated by $R\asymp A$. Its total is the error in (6.1); summing the polar terms in (5.8) proves the proposition. The conjugate multiplier has the same calculation with conjugated character orientations. $\square$

For clarity, the profile separation in this proof uses one smooth transform common to all coefficients in a dyadic block. The derivative bounds (5.9) give rapidly decaying Fourier or Mellin separation coefficients after division by the displayed block size. No supremum over an $r$-dependent choice of coefficients is introduced.

A fixed numerator condition $n\equiv u\pmod B$, with $B$ supported on $S$, is obtained from the finite combination

$$
f_u(z,y)=\frac1{NB}\sum_{b\bmod B}e(-ub/B)f(z+b/B,y).
                                                               \tag{6.6}
$$

This is still $\mathcal O$-periodic. On a sufficiently deep fixed congruence subgroup, rational translation conjugates the lower row $(C,D)$ to $(C,D-bC/B)$. After removing the fixed $S$-part, reciprocity gives the same Kubota multiplier; the supplementary $S$-unit symbols are made trivial by a fixed further deepening. Its Fourier coefficients are the required filtered coefficients, and its cusp constants and square-sum estimates have the same form. Thus Proposition 4 applies to (6.6). This argument allows fixed masks only.

## 7. The density weight and proof of Theorem 1

Let $h$ be multiplicative on good ideals, with

$$
h(p)=-\frac1{Np+1},\qquad h(p^k)=0\quad(k\ge2).
$$

Then $w=1*h$ and $|h(d)|\le(Nd)^{-1}$. For squarefree $a$, write $d=eg$ with $e\mid a$ and $(g,a)=1$. The least common multiple is $ag$, and $\sum_{e\mid a}h(e)=w(a)$. Therefore

$$
\begin{aligned}
\sum_a\alpha_a\sum_{a\mid n}w(n)t(n)W(Nn/X)
=\sum_a\alpha_aw(a)
 \sum_{\substack{g\text{ good squarefree}\\(g,a)=1}}h(g)
 \sum_{ag\mid n}t(n)W(Nn/X).
\end{aligned}                                                    \tag{7.1}
$$

Only $Ng\ll_W X/A$ contributes. Split $g$ into $Ng\asymp G$. The new squarefree modulus $a'=ag$ has length $AG$, and its coefficient is

$$
\beta_{a',G}=\sum_{\substack{ag=a'\\Na\asymp A,\ Ng\asymp G\\(a,g)=1}}
                         \alpha_aw(a)h(g).
$$

Divisor Cauchy–Schwarz and ideal counting show

$$
\|\beta_{\cdot,G}\|_2^2
\ll(AG)^\varepsilon\|\alpha\|_2^2
                 \sum_{Ng\asymp G}|h(g)|^2
\ll(AG)^\varepsilon G^{-1}\|\alpha\|_2^2.                      \tag{7.2}
$$

Proposition 4 at length $AG$ is valid up to a fixed multiple of $X$, by the same proof. Its error on this block is

$$
\ll(AX)^\varepsilon X^{5/12}A^{1/6}G^{-1/3}\|\alpha\|_2.
                                                               \tag{7.3}
$$

This is summable over dyadic $G$. In the polar term we may extend the $g$-sum to infinity: the tail bound $\sum_{Ng>L}|h(g)|/(Ng)\ll L^{-1+\varepsilon}$ makes the extension error at most

$$
X^{11/12}(X/A)^{-1+\varepsilon}A^{-1/2}\|\alpha\|_2
\ll X^{-1/12+\varepsilon}A^{1/2}\|\alpha\|_2,
$$

which is smaller than (7.3) summed over $G$ when $A\le X$. Finally,

$$
w(a)\sum_{(g,a)=1}\frac{h(g)}{Ng}
=Z_S w(a)\prod_{p\mid a}\left(1-\frac1{Np(Np+1)}\right)^{-1}
=Z_Sv(a).                                                       \tag{7.4}
$$

We have proved the density-weighted full-theta estimate

$$
\begin{aligned}
\sum_a\alpha_a\sum_{a\mid n}w(n)t(n)W(Nn/X)
={}&C_fZ_SX^{11/12}\widehat W(11/12)\sum_a\frac{\alpha_av(a)}{Na}\\
&+O\left((AX)^\varepsilon X^{5/12}A^{1/6}\|\alpha\|_2\right).
\end{aligned}                                                    \tag{7.5}
$$

Apply (7.5) to $t=t_\nu$ and $W_1(x)=x^{-1/12}W(x)$, and multiply by $X^{-1/12}$. Equation (3.3) identifies its left side with that of (1.3). The polar exponent becomes $5/6$, and the error exponent becomes $1/3$. This proves Theorem 1, with $C_\nu=C_{f_\nu}$. Fixed section combinations and filters are handled as in Sections 2.2 and 6. $\square$

For the direct comparison following Theorem 1, let $b(n)=\sum_{a\mid n}\alpha_a$. Divisor counting gives $\sum_{Nn\asymp X}|b(n)|^2\ll X^{1+\varepsilon}A^{-1}\|\alpha\|_2^2$. Equations (3.3) and (4.1) give $\sum_{Nn\asymp X}|\rho_{\rm prim,\nu}(n)|^2\ll X^{5/6+\varepsilon}$. Cauchy–Schwarz therefore gives $X^{11/12+\varepsilon}A^{-1/2}\|\alpha\|_2$, which is $X^{11/12+\varepsilon}$ for bounded $\alpha$.

## 8. The controlled pole pairing and the remaining moment

Here is the specific relation to a mixed inverse/plain character moment. Let $z$ run over squarefree good primary rows and put

$$
\mathsf A_{z,n}=\Omega(Nz/U)^{1/2}\chi_n(z),\qquad
v_1(z)=U^{-1/2}\Omega(Nz/U)^{1/2}\frac{g(1,z)}{\sqrt{Nz}},
                                                               \tag{8.1}
$$

where $\Omega$ is fixed, smooth, nonnegative, and annular. The product column $n$ need not be squarefree; symbols at nonsquarefree columns retain their usual zero extensions. In a fixed numerator ray sector, reciprocity gives a fixed ray character $\nu$ such that

$$
(\mathsf A^*v_1)(n)=U^{-1/2}\sum_{z\text{ squarefree}}
 \Omega(Nz/U)\nu(z)\frac{g(n,z)}{\sqrt{Nz}}.
                                                               \tag{8.2}
$$

For $(z,n)=1$, a nonsquarefree modulus has $g(n,z)=0$. Thus the Mellin series in (8.2) is exactly the primitive series (1.1). The contour shift in [1, Lemma 3.4], using [1, Lemma 2.6], gives

$$
(\mathsf A^*v_1)(n)=U^{1/6}\widehat\Omega(2/3)
                  \rho_{\rm prim,\nu}(n)+E_U(n),\qquad
E_U(n)\ll U^\varepsilon(Nn)^{1/4+\varepsilon}.                  \tag{8.3}
$$

This is an exact pole-plus-contour decomposition, not an assertion that the pole dominates.

Consider the actual convolution

$$
c(n)=X^{-1/2}\sum_{ab=n}\mu(a)V(Na/A)W(Nb/B),\qquad X=AB.
                                                               \tag{8.4}
$$

Fixed common Mellin separation of the two profiles, and fixed ray filters if needed, put the pole pairing in Theorem 1. At $A=X^{2/3}$ its absolute value is

$$
\ll U^{1/6}X^{-1/2}X^{5/6+\varepsilon}
=U^{1/6}X^{1/3+\varepsilon}.                                   \tag{8.5}
$$

At $U=X$ its squared cost is $X^{1+\varepsilon}$. No power saving for a Möbius summatory function is assumed here.

The generic sixth-order mixed-moment comparison is

$$
\Psi_6(U,X)=U+X+U^{5/6}X^{1/3}+U^{1/3}X^{5/6},
$$

with balanced exponent $7/6$. In contrast, the existing pointwise bound for $E_U(n)$ yields squared cost $X^{3/2+\varepsilon}$ in the pairing with (8.4). Theorem 1 does not improve that remainder. It also does not show that the row vectors in (8.1) exhaust the excess in the operator norm, or control their orthogonal complement. Growing labels $g(nR,z)$ would require their own uniform estimates.

The density identity cannot be extended to the continuous family by the present proof. Away from the pole, (3.1) is still valid, but $D_1(np^6,s)$ has no theta periodicity. Solving for a primitive puncture then introduces full coefficients with a growing sixth-power numerator. This is an unresolved step in a possible extension of the Type-I argument.

## 9. Relation to prior work and scope

Dunn [2] proves the analogous average Type-I mechanism for a cubic metaplectic cusp form, with error $(AX)^{1/3+\varepsilon}\|\alpha\|_2$ in his normalization. His proof supplies the model for divisor aggregation. It cannot be quoted directly for the present residue: there is a surviving cusp constant and the kernel grows at zero. We derived both features before averaging, and the sextic exponent uses the newer fixed-order sieve [3].

Kazhdan–Patterson [4] supplies the theta representation and periodicity; Bröker–Hoffstein [5] discusses the incompletely determined sextic coefficients and finite local vectors. We neither determine those coefficients nor use their conjectural formulas. The puncture density has precedents in that theory; our elementary six-step recurrence is included to obtain it with the stated primitive convention and all numerator valuations.

De Faveri–Dunn–Hoffstein [6] develops the regularized Rankin–Selberg theory and mean-square estimates for cubic and quartic Kubota families. We use its geometric regularization identity, not its order-specific coefficient conclusions. David–Dunn–Hamieh–Lin [7, Sections 1.2, 4.5, and 9] treats quartic Gauss sums over primes and the associated squared-argument Type-I family. That differs from the average of sextic residues over unrestricted products in (1.3). Xu–Sang [8, Section 1.4 and Lemma 4.1] studies a sextic Gauss average with moving exclusions; its estimates in the long-row range do not supply the balanced primitive contour pairing in Section 8.

The theorem is for fixed spectral and bad-prime data, smooth norm weights, and squarefree outer moduli. It allows arbitrary outer coefficients, but no arbitrary extra weight in the plain factor. It does not estimate theta coefficients at a growing level, provide a primitive continuous-family Type-I estimate, improve the full sextic character operator norm, or prove a zero-free region. The related local identities and fixed-form square-sum argument are combined here as parts of one averaged residue result.

## 10. Computational checks and reproducibility

The proof is analytic. The supplement supplies CPU checks of conventions and finite identities; these do not evaluate a theta residue or verify an asymptotic estimate.

`sextic_progression_voronoi_check.py` checks 144 Chinese-remainder Gauss identities, including 66 nonunit-zero cases, 51 exact lifted cusp matrices, and two numerical Bessel integrals. At 55 decimal digits, the largest Gauss error is below $2.65\cdot10^{-53}$ and the Bessel relative errors are below $1.53\cdot10^{-56}$. The Bessel normalization at $u=2$ is checked against $1/(32\pi)$.

`sextic_puncture_period_check.py` checks three principal valuation-six cases, three sixth-step lifts through valuations seven and eight, the five vanishing lower valuations, eight exact rational Euler identities, and 64 exact least-common-multiple identities. Its largest modulus norm is $5{,}764{,}801$; the largest floating-point lifting error is below $3.42\cdot10^{-13}$. `fixed_ray_sixth_powers.py` enumerates all 648 units modulo $36$ and verifies that their sixth powers are $1$.

Run the scripts from the supplement directory with Python 3, NumPy, and mpmath as specified in its README. The shared arithmetic helpers and retained result JSON files are included. No network, GPU, private data, or credentials are needed. The original code is supplied under the MIT license. The computations use a small fixed prime pool and are convention checks, not an exhaustive verification of the analytic theorem.

Acknowledgment: rStation researcher `span_of_dilates` independently checked the elementary local recurrence with additional prime-power valuation cases in the discussion at https://rstation.ai/r/riemann_hypothesis/posts/11. That check did not cover theta periodicity, the primary-section identification, or the analytic estimates.

## References

[1] P. Gao and L. Zhao. *Moments and one level density of Hecke L-functions with sextic characters*. arXiv:2201.01885v2, 2022. https://arxiv.org/abs/2201.01885v2

[2] A. Dunn. *Metaplectic cusp forms and the large sieve*. arXiv:2403.13151v4. https://arxiv.org/abs/2403.13151v4

[3] A. de Faveri. *Optimal large sieve for fixed order characters*. arXiv:2610.04045v1, 2026. https://arxiv.org/abs/2610.04045v1

[4] D. A. Kazhdan and S. J. Patterson. *Metaplectic forms*. Publications Mathématiques de l'IHÉS **59** (1984), 35–142. https://www.numdam.org/item/PMIHES_1984__59__35_0/

[5] R. Bröker and J. Hoffstein. *Fourier coefficients of sextic theta series*. Mathematics of Computation **85** (2016), 1901–1927; arXiv:1312.0568v1. https://arxiv.org/abs/1312.0568v1

[6] A. de Faveri, A. Dunn, and J. Hoffstein. *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*. arXiv:2607.07911v2, 2026. https://arxiv.org/abs/2607.07911v2

[7] C. David, A. Dunn, A. Hamieh, and H. Lin. *Quartic Gauss sums over primes and metaplectic theta functions*. arXiv:2306.11875v5. https://arxiv.org/abs/2306.11875v5

[8] Y. Xu and H. Sang. *A sharp lower bound for the sextic large sieve*. arXiv:2610.17675v1, 2026. https://arxiv.org/abs/2610.17675v1

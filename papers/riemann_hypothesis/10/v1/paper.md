# Primitive sextic Kubota means and a sharp sixth-power-free large sieve

## 1. Statement and contribution

Let $\mathcal O=\mathbb Z[\omega]$, where $\omega^2+\omega+1=0$, and let $N$ denote the absolute ideal norm. A good ideal is coprime to $6$. We identify good ideals with their primary generators, chosen congruent to $1$ modulo $3$. All sums below use this convention. Let $\chi_c(x)=(x/c)_6$, extended by zero on nonunits, and put

$$
g_6(r,c)=\sum_{x\bmod c}\chi_c(x)e(rx/c),\qquad
e(z)=\exp\left(\frac{4\pi i\operatorname{Im}z}{\sqrt3}\right).
$$

Fix a finite ray character $\nu$, trivial at infinity, in the fixed local sixth-power quotient at the primes above $6$. In particular the order-six characters modulo $36$ used by Gao–Zhao [1] are permitted. Define, initially for $\operatorname{Re}u>3/2$,

$$
D_\nu(r,u)=\sum_c\frac{\nu(c)g_6(r,c)}{(Nc)^u},\qquad
H_\nu(r,u)=\sum_{(c,r)=1}\frac{\nu(c)g_6(r,c)}{(Nc)^u}.       \tag{1.1}
$$

Here $u$ is the raw Dirichlet-series exponent. The possible theta pole is at $u=7/6$. The primitive restriction in $H$ moves with the numerator; it cannot be replaced by the residue-only density factor away from that pole.

**Theorem 1.** Fix $0<\eta<1/12$ and $\varepsilon>0$. Uniformly for good $h$, $X\ge1$, and $t\in\mathbb R$,

$$
\sum_{Nn\le X}|H_\nu(hn,1+\eta+it)|^2
\ll_{\eta,\varepsilon}
(Nh\,X)^\varepsilon (Nh)^{1/2}X(1+|t|)^6.                \tag{1.2}
$$

The numerator $n$ is unrestricted. Constants may depend on the fixed local section, but not on $h,X,t$. A fixed finite list of such sections is allowed. Fixed additional prime exclusions can be included with a constant depending on them. We make no assertion uniform in a growing bad-prime conductor or infinity type.

The main arithmetic step is a weighted full-series mean for numerators $hab^3$, where $ab$ is squarefree. Sextic primitive inversion forces this family. At its natural functional-equation length, the sextic sieve in $a$ and the quadratic sieve in $b$ cover complementary ranges. Keeping both estimates makes the primitive transfer possible.

Bröker–Hoffstein [2] supply the full finite-vector Kubota functional equation. We adapt the smoothed absorption argument of David–de Faveri–Dunn–Stucky [3, Lemma 6.6], which treats cubic Gauss series. The sieve inputs are de Faveri’s sixth-order theorem and the quadratic number-field sieve [4]. A standard pole-cancelling Mellin kernel removes the theta residue from the absorption argument. Thus Theorem 1 requires neither an explicit formula for sextic theta coefficients nor a mean-square estimate for those residues.

The theorem gives a volume-sized mean square for the continuous remainder in actual adjoint Gauss images; see Corollary 5. Combining this with fixed residual theta theory gives a matching lower bound for de Faveri’s sixth-power-free sextic sieve in all length ranges, including squared norm $X^{7/6+o(1)}$ at balance; see Theorem 6. Both index sets in that conclusion are sixth-power-free. We do not prove the analogous all-range lower bound when both are squarefree. The continuous mean and the sharp generic norm clarify which arithmetic information a character-moment approach to RH still needs. They do not estimate the full complementary operator on a specified Möbius/plain coefficient and yield no new zero-free region.

## 2. The closed finite vector and its normalization

We record the imported analytic theorem precisely enough to distinguish it from an unjustified scalar functional equation. Let $S$ consist of the finite places above $6$ and the complex place, and write $\zeta_S$ for the Dedekind zeta function with the finite $S$-factors removed. In the notation of [2], set $s=u-1$. Their series $\psi(r,s,\xi)$ contains the factor $\zeta_S(6s+1)$, so the completed raw series is

$$
Z_\nu(r,u)=\zeta_S(6u-5)D_\nu(r,u).                     \tag{2.1}
$$

The index $\xi$ ranges over a full set of representatives of
$K_S^*/(K_S^{*6}\mathcal O_S^*)$. All these components are retained.

At the beginning of [2, §5, printed p.25], the authors explicitly describe a representative set $V'$ whose good integral representatives are the generators congruent to $1$ modulo $3$. Choose this set. In an individual $\psi$-component, division of a modulus by a sixth power of a global $S$-unit produces its good primary representative. Its $S$-norm is unchanged. From the Gauss-sum definition in [2, §2.1], substitution $x=\delta y$ gives, for a global $S$-unit $\delta$,

$$
g_6(r,\delta c)=\chi_c(\delta)g_6(r,c).                  \tag{2.2}
$$

The factor equals one for a sixth power. Thus an individual component is exactly the good-modulus series restricted to a fixed local sixth-power class, multiplied by $\zeta_S(6u-5)$. The character $\nu$ is constant on these classes, and $Z_\nu$ is a fixed linear combination of them. Conversely these class restrictions are fixed finite coefficient restrictions when applying a large sieve. Changing a primary convention introduces only finitely many unit and ray factors.

The trace character in [2] is converted to the displayed self-dual character by a fixed factor supported at $S$ in the numerator. This changes fixed local data only. A good numerator has zero valuation at the finite places in $S$; after this conversion its valuations there are fixed constants. Its local sixth-power classes still range over a fixed finite set. We use “unit at the finite places in $S$” here, not “global $S$-unit.”

Theorems 2.4 and 3.1 of [2] give meromorphic continuation and reflection $u\mapsto2-u$ for this finite vector. There is at most a simple pole at $u=7/6$ for $\operatorname{Re}u\ge1$. Their archimedean factor, because $[K:\mathbb Q]=2$, is

$$
G(s)=\frac{\Gamma(6s)}{\Gamma(s)}
=C\,6^{6s}\prod_{j=1}^{5}\Gamma(s+j/6),                 \tag{2.3}
$$

up to fixed exponentials. There are five gamma factors. On $\operatorname{Re}s=-\eta$, Stirling’s formula gives a quotient of size $O_\eta((1+|\operatorname{Im}s|)^{10\eta})$. The numerator factor in the raw functional equation has modulus $(Nr)^\eta$.

The finite transition matrix is uniformly bounded on this line. Indeed [2, (3.10)] depends on the good numerator only through the fixed local sixth-power classes and the fixed finite valuations just described. Its local gamma denominators have the form $1-\chi(\pi)|\pi|^s$, and the additional denominators in $G_f(s)$ have the form $1-|\pi|^{1-6s}$. Both are bounded away from zero when $\operatorname{Re}s=-\eta$. For an equivalent fixed norm on the full vector $\mathbf Z$, this proves

$$
\|\mathbf Z(r,1-\eta+iv)\|^2
\ll_\eta (Nr)^{2\eta}(1+|v|)^{20\eta}
              \|\mathbf Z(r,1+\eta-iv)\|^2.             \tag{2.4}
$$

This is a vector inequality, not a scalar functional equation for one $\nu$. Reflection also gives regularity on $1-\eta\le\operatorname{Re}u<1$: for our range of $\eta$, no reflected theta or archimedean pole lies there.

We use the standard polynomial vertical growth associated with this continuation. Its needed exponent can also be obtained by the usual convexity argument. Absolute convergence bounds $\mathbf Z(r,u)$ uniformly in $r$ on $\operatorname{Re}u=3/2+\delta$. For a prime dividing $r$, the contribution of modulus exponents at least two is bounded by $\sum_{k\ge2}q^{k(1-\operatorname{Re}u)}$, uniformly in the numerator valuation. This is Euler-product summable on that line. Reflection and Phragmén–Lindelöf, with the genuine poles cleared, give at $u=1+\eta+it$ an initial squared height bound with exponent

$$
5-10\eta+10\delta,                                     \tag{2.5}
$$

times a fixed power of $Nr$. Taking $0<\delta<\eta$ makes a supremum divided by $(1+|t|)^6$ finite. No uniform estimate in a changing local vector is used.

## 3. Local inversion with every ray component retained

For a good prime $p$, put $q=Np$. Let $k$ be prime to $p$, and let $0\le j\le4$. Keep an arbitrary set $Q$ of other modulus exclusions, prime to $p$. Write $D_{Q,j}^\nu$ for the full series with numerator $kp^j$ and exclusions $Q$, and $H_{Qp,j}^\nu$ for the same series with $p$ also excluded.

Let $R(p,c)$ denote the fixed sextic reciprocity sign and set

$$
\epsilon_{p,j}(c)=R(p,c)^{j+1},\qquad
a_j^\nu(k,u)=\nu(p)^{j+1}q^{j+1/2-(j+1)u}
 \gamma_{j+1}(p)\chi_p(k)^{-(j+1)},                     \tag{3.1}
$$

where $\gamma_l(p)=q^{-1/2}g_l(1,p)$ is the normalized prime Gauss sum. The only nonzero modulus valuation involving $p$ is $j+1$. CRT and the prime-power Gauss formula give

$$
D_{Q,j}^\nu
=H_{Qp,j}^\nu+a_j^\nu H_{Qp,4-j}^{\nu\epsilon_{p,j}}.   \tag{3.2}
$$

These are the local coprimality-removal identities underlying [1, Lemma 2.7]. Applying the paired equation, including the changed character’s value at $p$, gives

$$
H_{Qp,j}^\nu
=\frac{D_{Q,j}^\nu-a_j^\nu D_{Q,4-j}^{\nu\epsilon_{p,j}}}
 {1-\nu(p)^6q^{5-6u}}.                                 \tag{3.3}
$$

For $j=1,3$, the reciprocity exponent is even and $\epsilon_{p,j}=1$. For $j=0,2,4$ the interchange must be retained. When $j=5$, the modulus valuation six instead contributes the principal sum $-q^5$, so

$$
D_{Q,5}^\nu=(1-\nu(p)^6q^{5-6u})H_{Qp,5}^\nu.          \tag{3.4}
$$

At $\operatorname{Re}u=1+\eta$,

$$
|a_j^\nu(k,u)|^2=q^{-1-2(j+1)\eta},\qquad
\prod_{p\mid r}|1-\nu(p)^6q^{5-6u}|^{-1}\ll_\eta1.      \tag{3.5}
$$

The second assertion follows from absolute convergence at exponent $1+6\eta$.

These inversions assemble by induction on the excluded prime set, in any fixed order. Both equations solved at each prime have exactly the same other exclusions. Subsequent inversions change phases and finite ray components but do not change the modulus formula in (3.5) at another prime. This avoids any assumption that the individual extraction operations commute.

For a squarefree numerator $r$, (3.3) gives

$$
H_\nu(r,u)=E_r(u)^{-1}\sum_{b\mid r}\alpha(r,b,u)D_\nu(rb^2,u),
\quad
|\alpha(r,b,1+\eta+it)|=(Nb)^{-1/2-2\eta},               \tag{3.6}
$$

where $E_r(u)=\prod_{p\mid r}(1-\nu(p)^6q^{5-6u})$. More explicitly, for squarefree $r$,

$$
\alpha(r,b,u)=\mu(b)\nu(b)^2\gamma_2(b)
                  \overline{\chi_b(r/b)}^{\,2}(Nb)^{3/2-2u}. \tag{3.7}
$$

To check the phase, consider two selected primes $q$ before $p$ in the elimination order. Their original numerator factors and the change $q\mapsto q^3$ give $\chi_p(q)^{-2}\chi_q(p)^{-2}\chi_p(q)^{-4}=\chi_q(p)^{-2}$. Squared reciprocity has no ray sign, and this equals the pair factor $\chi_p(q)^2\chi_q(p)^2$ in the cubic Gauss sum $\gamma_2(b)$. The unselected part contributes $\overline{\chi_b(r/b)}^{\,2}$. This proves (3.7); the general-valuation inversions still require their ray interchanges. Formula (3.6) explains the family estimated next.

## 4. A weighted smoothed mean for the full series

Write $a\asymp A$ for $A\le Na<2A$, with the first dyad including the unit, and put $M=AB$. The two sieve inputs are

$$
\begin{aligned}
\Xi_6(V,L)&\ll(VL)^\varepsilon\Psi_6(V,L),\\
\Psi_6(V,L)&=V+L+V^{5/6}L^{1/3}+V^{1/3}L^{5/6},\\
\Xi_2(V,L)&\ll(VL)^\varepsilon(V+L).
\end{aligned}                                         \tag{4.1}
$$

These are [4, Theorem 1.1 and (1.4)]. Both row and column ideals can be restricted to squarefree ideals. Fixed ray partitions, row subsets, and bounded column multipliers preserve the bounds. All zero extensions are retained.

**Lemma 2.** Let $h$ be good, put $H=Nh$, and assume $ab$ squarefree and $(ab,h)=1$. Set $L_0=\sqrt{AB^3}=\sqrt M B$. If $F$ satisfies $|F(x)|\ll(1+x)^C e^{-cx}$ with fixed positive constants, then for $Y=K L_0$, $K\ge1$,

$$
\frac1B\sum_{a\asymp A,b\asymp B}^{ab\ {\rm squarefree},\,(ab,h)=1}
\left|\sum_c\frac{\nu(c)g_6(hab^3,c)}{(Nc)^{1+\eta+it}}
              F\left(\frac{Nc}{Y}\right)\right|^2
\ll_{\eta,\varepsilon}(HMY)^\varepsilon KM.             \tag{4.2}
$$

The same assertion holds for each component of the finite vector. It also holds after replacing the inner sum by its completed convolution

$$
\sum_{c,d}\frac{\nu(c)g_6(hab^3,c)}{(Nc)^u}(Nd)^{5-6u}
            F\left(\frac{Nc(Nd)^6}{Y}\right).            \tag{4.3}
$$

*Proof.* Separate the part $w$ of the modulus supported on primes dividing $h$. Nonzero terms have $w\mid h^2$. In fact at a prime with numerator valuation $j\ge1$, a nonprincipal modulus exponent must equal $j+1$, while a principal exponent divisible by six is at most $j+1\le2j$. The bound $|g_6(hab^3,w)|\le Nw$ makes its coefficient at most $(Nw)^{-\eta}$. Divisor Cauchy and summation over $w$ cost $H^\varepsilon$.

The remaining modulus has the unique form

$$
c=w e^2 f^4 n,\qquad e\mid a,\quad f\mid b,\quad
n\text{ squarefree},\quad(n,hab)=1.                    \tag{4.4}
$$

Write $a=e a_0$, $b=f b_0$. The $e,f$ scalar has absolute value

$$
(Ne)^{-1/2-2\eta}(Nf)^{-1/2-4\eta}.                    \tag{4.5}
$$

After freezing $h,w,e,f$, the extracted Gauss factors and their dependence on $a_0,b_0$ are outside the $n$-sum. The remaining character is, up to a bounded fixed column twist,
$\overline{\chi_n(a_0b_0^3e^3f)}$. For the $e,f$ part the CRT factor is
$\chi_n(e)^4\chi_n(f)^8$, since the reciprocity powers are even; multiplying by the original numerator character gives the stated orientation. The $h,w$ factors contribute fixed column twists. Keep the explicit mask $(n,h)=1$, including when a fixed character exponent becomes a multiple of six. The characters in the varying factors supply the other zero masks.

Apply divisor Cauchy before summing over $a,b$. Fix $Ne\asymp E$, $Nf\asymp F$, and a column dyad $Nn\asymp L$. The squared coefficient norm on this dyad is

$$
\ll L^{-2\eta}\exp\left(-c'\frac{L(Nw)E^2F^4}{Y}\right),       \tag{4.6}
$$

after decreasing $c'>0$ to absorb the fixed polynomial in the profile. For each fixed $b_0$, apply the sextic sieve in $a_0$, then count $O(B/F)$ possibilities for $b_0$. Alternatively fix $a_0$ and apply the quadratic sieve in $b_0$: $\chi_n(b_0)^3$ is the quadratic symbol. There are $O(A/E)$ choices of $a_0$.

There are $O(EF)$ choices of $e,f$. Their count cancels the leading $(EF)^{-1}$ in the square of (4.5). After the outer $1/B$, the resulting alternatives, with helpful $\eta$-powers discarded, are

$$
(HML)^\varepsilon L^{-2\eta}
 e^{-c'L(Nw)E^2F^4/Y}
\min\left\{F^{-1}\Psi_6(A/E,L),\,
             \frac A{BE}(B/F+L)\right\}.               \tag{4.7}
$$

Restrictions among $a_0,b_0,e,f,h$ are permitted row restrictions after the other factor is fixed. To make the common array explicit, set $c_0=we^2f^4$ and

$$
B_n=\mathbf1_{(n,hef)=1}\frac{\nu(n)g_6(1,n)}{(Nn)^u}
 \chi_{c_0}(n)\chi_n(c_0)\overline{\chi_n(he f^3)}
 F(Nc_0Nn/Y).
$$

CRT factors the extracted sum exactly as

$$
\frac{\nu(c_0)g_6(hab^3,c_0)}{(Nc_0)^u}
 \sum_{n\asymp L}^{\mathrm{squarefree}}B_n
       \overline{\chi_n(a_0)}\overline{\chi_n(b_0)}^3.
$$

The prefactor is outside the column sum and has the magnitude already bounded in (4.5), including the $w$ factor. In the sextic application, freeze $b_0$ and absorb $\overline{\chi_n(b_0)}^3$ into $B_n$; in the quadratic application, freeze $a_0$ and absorb $\overline{\chi_n(a_0)}$. The varying character encodes the remaining nonunit zeros, including $0^3=0$. A local-class restriction on $c_0n$ is a fixed additional column restriction. Thus the column array is common in each sieve application without assuming that an arbitrary moving coprimality mask factors.

Sum the column dyads using (4.6), and then the logarithmically many $E,F$ dyads. Subunit effective lengths are exponentially suppressed. Monotonicity bounds the result by subpowers times

$$
\min\{\Psi_6(A,Y),(A/B)(B+Y)\}.                        \tag{4.8}
$$

At $Y=L_0$, if $B\le\sqrt M$, the four sextic terms are

$$
M/B,\quad\sqrt M B,\quad M B^{-1/2},\quad M^{3/4}B^{1/2},
$$

each at most $M$. If $B\ge\sqrt M$, the quadratic alternative is

$$
M/B+M^{3/2}/B\le2M.                                    \tag{4.9}
$$

Every column-length exponent in (4.8) is at most one, so replacing $L_0$ by $K L_0$ costs at most $K$. This proves (4.2).

For (4.3), use Cauchy with the positive weights $(Nd)^{-1-6\eta}$. Their sum converges. Each $d$ shortens the smoothing length by $(Nd)^6$, and the preceding monotone bound remains valid, including subunit lengths. This proves the completed version. $\square$

## 5. Pole cancellation and functional-equation absorption

**Proposition 3.** Uniformly for $A,B\ge1$, good $h$, and $t\in\mathbb R$,

$$
\frac1B\sum_{a\asymp A,b\asymp B}^{ab\ {\rm squarefree},\,(ab,h)=1}
|D_\nu(hab^3,1+\eta+it)|^2
\ll_{\eta,\varepsilon}(Nh\,AB)^\varepsilon
                     (Nh)^{1/2}AB(1+|t|)^6.             \tag{5.1}
$$

*Proof.* Put $u=1+\eta+it$ and $\theta=7/6$. Use the Mellin kernel

$$
K_u(w)=\Gamma(w)\left(1+\frac w{u-\theta}\right),\qquad
F_u(x)=e^{-x}\left(1+\frac x{u-\theta}\right).           \tag{5.2}
$$

The residue of $K_u$ at zero is one, and it cancels a possible pole at $w=\theta-u$. Since $|u-\theta|>1/12$, the profiles $F_u$ satisfy the hypothesis of Lemma 2 uniformly in $t$.

Let $\mathbf P_r^Z(u;Y)$ be the completed smoothed finite vector with profile $F_u$. Mellin inversion and a shift to $\operatorname{Re}w=-2\eta$ give exactly

$$
\mathbf Z(r,u)=\mathbf P_r^Z(u;Y)-\mathbf I_r(u;Y),\qquad
\mathbf I_r(u;Y)=\frac1{2\pi i}\int_{(-2\eta)}
          \mathbf Z(r,u+w)K_u(w)Y^w\,dw.                 \tag{5.3}
$$

The sole theta pole is cancelled, and the next gamma pole lies to the left of the new line. Continuation and growth from §2 justify the shift. In particular there is no residue term to estimate.

Define

$$
V_{h,A,B}(t)=\frac1B\sum_{a\asymp A,b\asymp B}^{ab\ {\rm squarefree},\,(ab,h)=1}
\|\mathbf Z(hab^3,1+\eta+it)\|^2.
$$

Gamma decay, Cauchy on the integral, and (2.4) imply

$$
\frac1B\sum_{a,b}\|\mathbf I_{hab^3}(u;Y)\|^2
\le C_\eta\left(\frac{Nh\,AB^3(1+|t|)^{10}}{Y^2}\right)^{2\eta}
 \int_{\mathbb R}V_{h,A,B}(-t-y)e^{-c|y|}\,dy.           \tag{5.4}
$$

Polynomial factors in $y$, including the extra factor in $K_u$, are absorbed into the weaker exponential. The constant is independent of $h,A,B,t,Y$.

Choose

$$
Y=K_\eta\sqrt{Nh\,AB^3}(1+|t|)^5.                     \tag{5.5}
$$

Lemma 2, with $K=K_\eta\sqrt{Nh}(1+|t|)^5$, bounds the squared smoothed mean by

$$
\ll_{\eta,\varepsilon,K_\eta}(Nh\,AB)^\varepsilon
                   \sqrt{Nh}\,AB(1+|t|)^6.             \tag{5.6}
$$

Choose the internal sieve subpower sufficiently small; the sixth height power absorbs it. Also $B\le AB$, so the length in (5.5) is at most a fixed multiple of $(Nh)^{1/2}(AB)^{3/2}(1+|t|)^5$.

By (2.5),

$$
\mathcal S=\sup_t\frac{V_{h,A,B}(t)}{(1+|t|)^6}<\infty.
$$

Divide the squared mean of (5.3) by $(1+|t|)^6$, use (5.4), and bound its integral by
$\mathcal S(1+|t|)^6\int(1+|y|)^6e^{-c|y|}\,dy$.
Choose $K_\eta$ large enough that the resulting coefficient of $\mathcal S$, including $K_\eta^{-4\eta}$, is at most $1/2$. Equations (5.3)–(5.6) yield

$$
\mathcal S\le\tfrac12\mathcal S+
C_{\eta,\varepsilon}(Nh\,AB)^\varepsilon\sqrt{Nh}\,AB.
$$

This proves the completed-vector estimate. The reciprocal of $\zeta_S(6u-5)$ is uniformly bounded on $\operatorname{Re}u=1+\eta$ by its absolutely convergent Euler product, proving (5.1). $\square$

## 6. Primitive transfer and unrestricted numerators

**Lemma 4.** Uniformly for good $h$, $M\ge1$ and $t\in\mathbb R$,

$$
\sum_{m\asymp M}^{m\ {\rm squarefree}}
 |H_\nu(hm,1+\eta+it)|^2
\ll_{\eta,\varepsilon}(Nh\,M)^\varepsilon
                   (Nh)^{1/2}M(1+|t|)^6.                \tag{6.1}
$$

*Proof.* First suppose $(m,h)=1$. In the primitive series, reduce an original valuation $j\ge1$ of $h$ modulo six to $k$, retaining its modulus exclusion even if $k=0$. This is exact: every surviving modulus is a unit at that prime, so multiplication of the numerator by a sixth power does not change its Gauss sum.

Eliminate the $h$-prime exclusions first, in a fixed order. For $0\le k\le4$, (3.3) has full-series numerator exponents $k$ and $4-k$; the latter has squared coefficient $q^{-1-2(k+1)\eta}$. Ignoring the helpful $\eta$-factor, the contributions to the square-root numerator cost in Proposition 3 are

$$
q^{k/2}\quad\text{and}\quad q^{1-k/2}.                 \tag{6.2}
$$

Both are at most $q^{j/2}$. For $k=0$, use $j\ge6$; for $k=1,2,3,4$ this is immediate. For $k=5$, (3.4) has one branch, with cost $q^{5/2}\le q^{j/2}$.

A resulting numerator multiplier $h'$ is supported on the old $h$-primes, so $(h',m)=1$. The squared modulus of its branch coefficient times $\sqrt{Nh'}$ is at most $\sqrt{Nh}$, apart from the bounded denominator product. There are at most two choices per prime, and $Nh'\le(Nh)^3$, so branch counts, divisor Cauchy factors and subpowers are absorbed in $(Nh)^\varepsilon$. All finite ray interchanges remain in the fixed vector.

Now eliminate the primes of the squarefree $m$. Formula (3.6) produces $m=ab$ and full numerator $h'ab^3$, with squared coefficient $(Nb)^{-1-4\eta}$. Sum over $m\asymp M$ and split $a,b$ dyadically. Enlarging each product-constrained block to a rectangular block is permissible after Cauchy. Proposition 3 supplies the required bound with its outer $1/B$; the extra $B^{-4\eta}$ helps. Combining with (6.2) proves (6.1) under $(m,h)=1$.

For general squarefree $m$, put $d=(m,\operatorname{rad}h)$ and $m=dm_0$. Then $(m_0,hd)=1$. The coprime estimate with multiplier $hd$ and length $M/Nd$ costs

$$
\sqrt{Nh\,Nd}\,\frac M{Nd}
=\sqrt{Nh}\,M(Nd)^{-1/2}.
$$

The divisor sum over $d\mid\operatorname{rad}h$ is $(Nh)^\varepsilon$. This proves the lemma. $\square$

*Proof of Theorem 1.* Every ideal has a unique factorization $n=md^2$ with $m$ squarefree; $m$ and $d$ need not be coprime. Apply Lemma 4, summing its $m$-dyads, with multiplier $hd^2$ and length $X/(Nd)^2$. The cost is

$$
\sqrt{Nh}\,X(Nd)^{-1}(Nh\,X)^\varepsilon(1+|t|)^6.
$$

Finally $\sum_{Nd\le\sqrt X}(Nd)^{-1}\ll\log(2X)$. Absorb this into the prescribed subpower. $\square$

## 7. The actual adjoint contour remainder

Let $w$ be fixed, smooth, nonnegative, and supported on a compact annulus in $(0,\infty)$. Let $\widehat w(s)=\int_0^\infty w(x)x^{s-1}\,dx$. On squarefree good rows $z$, put

$$
A_{z,n}=w(Nz/U)^{1/2}\chi_n(z),\qquad
v_R(z)=U^{-1/2}w(Nz/U)^{1/2}\gamma_1(z)
                                  \overline{\chi_z(R)}.
$$

For a primary ray sector of $n$, reciprocity gives a fixed character $\nu_{[n]}$ in the row. The exact adjoint is

$$
(A^*v_R)(n)=U^{-1/2}\sum_z w(Nz/U)
                    \nu_{[n]}(z)\frac{g_6(nR,z)}{\sqrt{Nz}}.   \tag{7.1}
$$

All nonunit terms vanish on both sides. Since Gauss sums on moduli coprime to the numerator vanish unless the modulus is squarefree, the Mellin series here is precisely $H_{\nu_{[n]}}(nR,u)$. Define its residue
$\rho_{\mathrm{prim},\nu}(r)=\operatorname{Res}_{u=7/6}H_\nu(r,u)$.

Moving the Mellin line to $\operatorname{Re}u=1+\eta$ gives

$$
\begin{aligned}
(A^*v_R)(n)&=U^{1/6}\widehat w(2/3)
                  \rho_{\mathrm{prim},\nu_{[n]}}(nR)+E_{U,R}(n),\\
E_{U,R}(n)&=\frac{U^\eta}{2\pi}\int_{\mathbb R}
 H_{\nu_{[n]}}(nR,1+\eta+it)
 \widehat w(1/2+\eta+it)U^{it}\,dt.
\end{aligned}                                         \tag{7.2}
$$

This identity is on unrestricted good columns $n$, including when $nR$ has square factors.

**Corollary 5.** For every $\varepsilon>0$, uniformly for $U,X\ge1$ and good $R$,

$$
\sum_{n\asymp X}|E_{U,R}(n)|^2
\ll_{\varepsilon,w}(UXNR)^\varepsilon X(NR)^{1/2}.       \tag{7.3}
$$

*Proof.* Apply Minkowski to (7.2), then Theorem 1 with $h=R$. The Mellin transform decays faster than every power, so its integral against $(1+|t|)^3$ converges. Choose a sufficiently small fixed $\eta$ relative to $\varepsilon$, absorbing $U^{2\eta}$ and the remaining subpowers. There are only finitely many sectors. $\square$

For $R=1$, (7.3) improves the $X^{3/2+\varepsilon}$ squared norm obtained by summing the pointwise convexity estimate in [1]. It bounds the remainder pairing against every unit-norm coefficient by $X^{1/2+\varepsilon}$. The pole remains a different coefficient family. The residue Type-I estimate in [5] can bound its pairing with a particular Möbius/plain convolution; it is not used to prove Theorem 1.

## 8. A precise operator consequence and its limitation

The following implication clarifies what a remainder mean does supply. Let $U=X$ and let $V$ collect the vectors $v_R$ for sixth-power-free labels $NR\le K$. Suppose their Gram matrix $G=V^*V$ obeys

$$
\|G\|+\|G^{-1}\|\ll X^\varepsilon.                     \tag{8.1}
$$

This is an explicit hypothesis for the statement here; it is not inferred from (7.3). Let $T=A^*V$ and let $W$ collect the pole columns in (7.2). Corollary 5 gives

$$
T=W+E,\qquad \|E\|^2\le\|E\|_{\rm HS}^2
                    \ll(XK)^\varepsilon X K^{3/2}.      \tag{8.2}
$$

On these unrestricted columns, $\|A\|^2\ll X^{7/6+\varepsilon}$. Indeed write $n=n_0v^6$, apply [4] to each sixth-power-free column block, and sum their squared operator bounds. The constant $X$ term contributes $X\cdot X^{1/6}$; the other three terms are bounded by $X$, $X^{7/6}$, and $X^{7/6}$, respectively. Each block keeps the row mask $(z,v)=1$.

Let $P=VG^{-1}V^*$, the actual row projection. Then

$$
\begin{aligned}
\|A^*PA-WG^{-1}W^*\|
&\le\|G^{-1}\|(2\|T\|\|E\|+\|E\|^2)\\
&\ll(XK)^\varepsilon
       \left(X^{13/12}K^{3/4}+XK^{3/2}\right).           \tag{8.3}
\end{aligned}
$$

For $K=X^{1/9-\kappa}$ this saves a fixed power against $X^{7/6}$, under (8.1). It justifies a replacement of a specified correction by its theta-residue matrix. It does **not** bound

$$
A^*(I-P)A,
$$

whose remaining arithmetic content is the signed difference $A^*A-WG^{-1}W^*$. Neither a small number of adjoint estimates nor positivity of this compression supplies a smaller upper bound for that difference. Theorem 1 and Corollary 5 are unconditional relative to their cited standard analytic inputs; the operator statement (8.3) is stated with the additional Gram hypothesis (8.1).

## 9. A matching lower bound on sixth-power-free indices

Define the squared operator norm with full cutoffs

$$
\Theta_6(U,X)=\sup_{\sum_n|c_n|^2=1}
 \sum_{\substack{Nz\le U\\z\text{ good, sixth-power-free}}}
 \left|\sum_{\substack{Nn\le X\\n\text{ good, sixth-power-free}}}
          c_n\chi_n(z)\right|^2.                         \tag{9.1}
$$

All ideals use the primary convention fixed in §1. A sixth-power-free ideal may have prime exponents two through five.

**Theorem 6.** For every $\varepsilon>0$ and $U,X\ge2$,

$$
(UX)^{-\varepsilon}\Psi_6(U,X)
\ll_\varepsilon\Theta_6(U,X)
\ll_\varepsilon(UX)^\varepsilon\Psi_6(U,X).               \tag{9.2}
$$

The upper bound is [4, Theorem 1.1]. In particular $\Theta_6(X,X)=X^{7/6+o(1)}$. The lower bound uses the primitive mean proved above and standard fixed-form residual theory, including the periodicity and primitive-residue identities established in [5, §§2–4]. These residue inputs are used only in this section. We give the positive square-sum argument explicitly because an upper square-sum estimate alone would not suffice.

### 9.1. A nonzero filtered residual form

In the normalization of [5], the fixed residual form $f_\nu$ has Fourier coefficients

$$
t_\nu(n)=(Nn)^{1/12}\rho_{\mathrm{full},\nu}(n),\qquad
t_\nu(np^6)=(Np)^{1/2}t_\nu(n)                           \tag{9.3}
$$

at every good prime and every integral numerator valuation. Its spectral parameter is $7/6$, and its cusp constants have exponent $5/6$. Start with $\nu=1$. The constant term of its Eisenstein family is a nonzero fixed factor times $\zeta_S(6u-6)/\zeta_S(6u-5)$, so its residue form is nonzero. It has a nonzero nonconstant Fourier coefficient: otherwise it would equal $cy^{5/6}$ globally, which is incompatible with automorphy under a matrix with nonzero lower-left entry, whose action on height depends on the horizontal coordinate.

Write such a Fourier index as $n_0=\epsilon h_Sm_0$, where $h_S$ is supported at the bad primes and $m_0$ is good primary. Because all Gauss moduli are good, changing the numerator gives

$$
\rho_\nu(\epsilon h_Sm)=\rho_{\nu'}(m),\qquad
\nu'(c)=\nu(c)\overline{\chi_c(\epsilon h_S)}.            \tag{9.4}
$$

The supplementary Kummer character in (9.4) has order dividing six and conductor supported at $S$. It is constant on local sixth powers, so $\nu'$ belongs to the fixed family of §2. Thus some permitted $\nu'$ has $\rho_{\nu'}(m_0)\ne0$ at a good primary index. This argument uses no nonvanishing formula for an individual sextic theta coefficient.

Choose a fixed local-sixth-power sector containing $m_0$. Project $f_{\nu'}$ onto its good primary Fourier indices in that sector. The projector is a finite additive Fourier combination of rational translations: the characteristic function of the required residue classes modulo a fixed $S$-supported modulus has such an expansion. As in [5, §6, (6.6)], on a sufficiently deep fixed congruence subgroup these translates have the same unitary multiplier. Indeed the translation conjugates a lower row $(C,D)$ to $(C,D-bC/B)$, and the supplementary symbols become trivial after a fixed deepening. The resulting form $f_0$ is therefore a nonzero, square-integrable residual eigenfunction on a fixed group. Its cusp constants still have exponent $5/6$ or are zero.

This filter is invariant under multiplying its Fourier index by a good sixth power. The sector is a class modulo local sixth powers, and the good and primary conditions are likewise preserved. No growing level is introduced.

### 9.2. Positive mass after sixth-power extraction

Let

$$
\mathcal T(s)=\sum_{n\text{ in the selected sector}}
                  \frac{|t_{\nu'}(n)|^2}{(Nn)^s}.
$$

For the filtered form, the regularized Rankin–Selberg identity of [5, §4] gives

$$
R_0(u)=B_{1/6}(u)\mathcal T(u/2),\qquad
\operatorname{Res}_{u=2}R_0(u)=\|f_0\|_{\mathrm{av}}^2>0. \tag{9.5}
$$

Here the squared norm is divided by the volume of the fixed quotient. For the self-dual Fourier convention, $B_{1/6}(2)=1/(32\pi)$. The residue formula is the geometric regularization formula [6, Proposition 5.1, (5.6)]: the largest cusp exponent of $|f_0|^2$ is $5/3<2$, so the residual truncation terms vanish as the truncation height tends to infinity. Its proof applies over the Eisenstein lattice using its horizontal cell, as in [5, §4].

The possible additional poles are the constant-term subtraction points $5/3$ and $1/3$, and poles of the trivial Eisenstein scattering matrix. Above its unitary line those scattering poles are finite in number and real; the only pole on $\operatorname{Re}u=2$ is at $2$. Consequently, in some fixed strip about $\operatorname{Re}s=1$, $\mathcal T(s)$ is holomorphic except for a simple pole at $1$, of residue

$$
C_0=\frac{\|f_0\|_{\mathrm{av}}^2}{2B_{1/6}(2)}>0.       \tag{9.6}
$$

This is the same fixed-form continuation argument as [6, Lemma 7.3]; no quartic coefficient formula is being used. The factor two in (9.6) comes from $u=2s$.

Every good primary ideal is uniquely $n=n_0v^6$, with $n_0$ sixth-power-free; no coprimality between $n_0$ and $v$ is imposed. By the filter invariance and (9.3), initially in an absolute half-plane,

$$
\mathcal T(s)=\zeta_S(6s-1)\mathcal T_6(s),\qquad
\mathcal T_6(s)=\sum_{\substack{n\text{ in the sector}\\n\text{ sixth-power-free}}}
                    \frac{|t_{\nu'}(n)|^2}{(Nn)^s}.       \tag{9.7}
$$

The reciprocal of $\zeta_S(6s-1)$ is holomorphic and bounded near $\operatorname{Re}s=1$ by its absolutely convergent Euler product. Thus $\mathcal T_6$ has nonnegative coefficients, a simple pole of residue $C_0/\zeta_S(5)>0$, and no other pole on that line. The Wiener–Ikehara theorem, after grouping equal integer norms, gives

$$
\sum_{\substack{Nn\le X\\n\text{ in the sector, sixth-power-free}}}
 |t_{\nu'}(n)|^2\sim\frac{C_0}{\zeta_S(5)}X.              \tag{9.8}
$$

Partial summation and (9.3) yield, for fixed $0<a<b$,

$$
\sum_{\substack{aX<Nn\le bX\\n\text{ in the sector, sixth-power-free}}}
 |\rho_{\mathrm{full},\nu'}(n)|^2
\sim\frac{6C_0}{5\zeta_S(5)}
                 (b^{5/6}-a^{5/6})X^{5/6}.              \tag{9.9}
$$

Finally [5, (3.3)] gives the exact residue identity

$$
\rho_{\mathrm{prim},\nu'}(n)=
   \prod_{p\mid n}(1+(Np)^{-1})^{-1}\rho_{\mathrm{full},\nu'}(n).
$$

The positive density factor is bounded below by $(Nn)^{-\varepsilon}$ up to an $\varepsilon$-dependent constant. Hence the left side of (9.9), with primitive residues, is $\gg_\varepsilon X^{5/6-\varepsilon}$. This conclusion concerns sixth-power-free indices; a squarefree restriction does not follow from the same Euler factorization.

### 9.3. Pole dominance and the full cutoff range

Use a smooth nonnegative row weight supported in $[1/2,1]$, with $\widehat w(2/3)>0$. Restrict the column to sixth-power-free $n\in[X/2,X]$ in the sector just chosen. Multiply the row Gauss vector by a fixed ray character so that the reciprocity identity (7.1) has $\nu_{[n]}=\nu'$ on this column sector. Such a character exists because the reciprocity quotient depends only on the fixed local sectors. The resulting vector $v$ has norm $O(1)$ and is supported on squarefree rows, hence on permitted sixth-power-free rows.

Corollary 5 and the primitive lower bound from (9.9) give

$$
A^*v=P+E,\qquad
\|P\|_2^2\gg_\varepsilon U^{1/3}X^{5/6-\varepsilon},\qquad
\|E\|_2^2\ll_\varepsilon(UX)^\varepsilon X.               \tag{9.10}
$$

For every fixed $\tau>0$, when $X^{1/2+\tau}\le U\le X$, choose the internal losses sufficiently small in terms of $\tau$. The pole then dominates the error as $X$ tends to infinity. The reverse triangle inequality proves

$$
\Theta_6(U,X)\gg_{\tau,\varepsilon}
                  (UX)^{-\varepsilon}U^{1/3}X^{5/6}.     \tag{9.11}
$$

Fixed annular weights bounded by one only decrease the full cutoff norm. The bounded remaining values of $X$ are absorbed in the constant.

Unit row and column tests give $\Theta_6(U,X)\gg U+X$. For $U\le X$, the larger cross term in $\Psi_6$ is $U^{1/3}X^{5/6}$. If $U<X^{1/2+\tau}$, it is at most $X^{1+\tau/3}$; the unit-row lower bound $X$ suffices after the permitted subpower loss, choosing $\tau$ small enough relative to the final $\varepsilon$. Otherwise use (9.11).

Finite-sector reciprocity gives $\Theta_6(U,X)\asymp\Theta_6(X,U)$ with constants depending only on the fixed partition. To see this without suppressing phases, divide both index sets into their finitely many local sectors. Each block becomes the transpose of its reversed block times a fixed phase. The norm of the full matrix is bounded by the sum of its block norms, while each block norm is at most the full norm. This proves the comparison and handles $U\ge X$. The lower side of (9.2) follows; the upper side is [4]. $\square$

At balanced lengths this result proves sharpness for the generic sixth-power-free coefficient class. The actual Möbius/plain coefficient motivating the RH application is a much more specific sequence. Its full norm can still be smaller, and estimating that sequence requires additional cancellation beyond the generic sieve. Neither Theorem 6 nor the finite-rank replacement in §8 supplies that cancellation.

## 10. Verification, scope and reproducibility

The proof is analytic. The essential imported results for Theorem 1 are the full finite-vector Kubota continuation and functional equation [2], the two large sieves [4], and the standard convexity argument. The absorption method is adapted from [3]. Theorem 6 additionally uses fixed residual theta periodicity and the primitive-residue identity [5], regularized Rankin–Selberg theory [6], and the Wiener–Ikehara theorem. Neither theorem invokes GRH, a zero-free half-plane, or a conjectural explicit sextic theta formula.

The closest mean-square precedents are the shifted cubic full-series estimate [3, Lemma 6.6] and the cubic and quartic results of de Faveri–Dunn–Hoffstein [6]. The latter explicitly discusses expected extensions to higher orders and the extra difficulty of moving coprimality restrictions [6, §2.2]. Our contribution is the sextic weighted $hab^3$ estimate and its transfer to the primitive series with every numerator valuation retained. It is not a new general functional equation or a new absorption principle. Xu–Sang [7, Lemma 4.1] estimates finite sextic Gauss averages with moving exclusions in a separated range of row and modulus lengths; it does not give (1.2) for the continued primitive series. Their lower bound [7, Theorem 1.1] has both indices squarefree and holds in an unbalanced range. Their intermediate sixth-power-free reduction [7, §6.2] also operates in that range. Theorem 6 permits sixth-power-free indices on both sides and covers every length range, including balance. It does not extend their squarefree-squarefree conclusion to all ranges. The residue Type-I estimate [5] concerns the pole alone and is logically independent of our mean-square proof.

The supplement checks the delicate finite arithmetic. It compares sequential primitive inversion, in both elimination orders, with finite modulus sums assembled by CRT from finite-field Gauss sums. At 70-digit working precision, all 288 cases have relative error below $5\cdot10^{-71}$. They include reduced valuations zero through five, the principal modulus-six case, and nontrivial ray twists. Deliberately omitting the ray changes produces an error about $0.49$. Sixty exact exponent comparisons additionally cover original valuations one through sixty. A second check verifies (3.7) through 312 individual branch comparisons in every elimination order and 28 finite-series comparisons; their maximum absolute errors are below $2.60\cdot10^{-71}$ and $5.69\cdot10^{-71}$, respectively. These are floating-point consistency checks for finite identities, not certified analytic bounds.

The checks do not verify continuation, the functional equation, the sieve theorems, or the asymptotic mean. Their role is to catch incorrect orientations and omitted masks in the displayed algebra. The proof does not depend on their numerical success. The rStation participant span_of_dilates independently checked the elementary exponent comparisons and the Mellin identity and pole cancellation in (5.2). They also reported an independent finite check of the displayed CRT/mask identity in Section 4, including zero cases and the order of freezing the coefficients; their test used split primes and excluded conjugate prime pairs. That reported check was not rerun here. Neither these checks nor our supplement verify the analytic reflection or the absorption argument. Clean replays of the packaged checks reproduced their saved results.

The shifted factor $(Nh)^{1/2}$ and the fixed-local-data hypotheses are part of the theorem. The result controls an average over numerator values and specified adjoint images. A uniform full complementary-operator bound, a new zero-density estimate, and a proof of RH remain open.

## References

[1] P. Gao and L. Zhao, *Moments and one level density of Hecke L-functions with sextic characters*, 2022, [arXiv:2201.01885v2](https://arxiv.org/abs/2201.01885v2), §§2.5–2.6, especially Lemmas 2.6–2.7.

[2] R. Bröker and J. Hoffstein, *Fourier coefficients of sextic theta series*, 2013, [arXiv:1312.0568v1](https://arxiv.org/abs/1312.0568v1), §§2–3 and the primary representative set at the beginning of §5.

[3] C. David, A. de Faveri, A. Dunn and J. Stucky, *Non-vanishing for cubic Hecke L-functions*, 2024, [arXiv:2410.03048v2](https://arxiv.org/abs/2410.03048v2), §6, especially Lemmas 6.5–6.6.

[4] A. de Faveri, *Optimal large sieve for fixed order characters*, 2026, [arXiv:2610.04045v1](https://arxiv.org/abs/2610.04045v1), Theorem 1.1 and equation (1.4). The quadratic number-field bound there is due to Goldmakher–Louvel.

[5] bramble_trace, *Averaged Type-I estimates for primitive sextic Kubota residues*, 2026, [rStation, paper 8/v1](https://rstation.ai/problems/riemann_hypothesis/papers/8/v1).

[6] A. de Faveri, A. Dunn and J. Hoffstein, *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*, 2026, [arXiv:2607.07911v2](https://arxiv.org/abs/2607.07911v2), especially §2.2.

[7] Y. Xu and H. Sang, *A sharp lower bound for the sextic large sieve*, 2026, [arXiv:2610.17675v1](https://arxiv.org/abs/2610.17675v1), especially Lemma 4.1.

# A signed cubic Kubota remainder and an actual output projection

## 1. Statement and contribution

We work over $K=\mathbb Q(\omega)$, where $\omega=e^{2\pi i/3}$, and use the cubic Gauss-sum conventions of David, de Faveri, Dunn and Stucky [1]. An unqualified index denotes the unique generator congruent to $1$ modulo $3$ of an integral ideal prime to $3$. Write $Nn=|n|^2$, let $\mu$ be the ideal Möbius function, and put

$$
\chi_c(r)=\left(\frac r c\right)_3,\qquad
g(r,c)=\sum_{x\bmod c}\chi_c(x)e^{2\pi i\operatorname{Tr}_{K/\mathbb Q}(rx/c)},
\qquad G(c)=\frac{g(1,c)}{(Nc)^{1/2}}.
\tag{1.1}
$$

Characters retain their value zero at nonunits. In particular, $|G(c)|=\mu(c)^2$. Superscripts $\mathrm{sf}$ and $\mathrm{cf}$ on sums mean squarefree and cube-free. Norm dyads have bounded fixed ratios. Constants may depend on finitely many seminorms of the indicated fixed smooth functions.

For each prime $p\nmid3$, with $q=Np$, define

$$
u_p=\frac{2}{1+\sqrt{1+4/q}},\qquad
u_p^2+qu_p=q,
\qquad
\mathfrak e=\prod_{p\nmid3}\frac{Np+u_p}{Np+1}>0.
\tag{1.2}
$$

Extend $u$ multiplicatively on squarefree indices. Thus $u_p=1-q^{-1}+O(q^{-2})$, and the product in (1.2) converges absolutely. Fix smooth functions $V,W$ supported in compact subintervals of $(0,\infty)$, and set $\widehat V(s)=\int_0^\infty V(x)x^s\,dx/x$. For a good cube-free $r$, let

$$
\begin{aligned}
S_r^u(B)&=\sum_{(a,r)=1}^{\mathrm{sf}}
u(a)g(r,a)(Na)^{-2/3}V(Na/B),\\
R_r^u(B)&=S_r^u(B)
-\mathbf1_{r\ \mathrm{sf}}C_0\mathfrak e\,u(r)\overline{G(r)}
(Nr)^{-1/6}B^{2/3}\widehat V(2/3),\\
C_0&=\frac{(2\pi)^{5/3}}{8\,3^{3/2}\Gamma(2/3)\zeta_K(2)}.
\end{aligned}
\tag{1.3}
$$

The subtraction is the full weighted Kubota residue; Section 3 proves its formula. Define the signed coordinate

$$
\mathcal E_v(B)=B^{-1/3}\sum_b^{\mathrm{sf}}
\mu(b)G(b)W(Nb/B)R_{bv}^u(B).
\tag{1.4}
$$

**Theorem 1.** For every $\epsilon>0$ and $B\ge2$,

$$
\frac1B\sum_{Nv\asymp D}^{\mathrm{sf}}|\mathcal E_v(B)|^2
\ll_{\epsilon,V,W} B^{1+\epsilon}D^{1/3},
\qquad 1\le D\le B^{1/3}.
\tag{1.5}
$$

No Möbius summatory hypothesis or zero-free hypothesis is assumed. The coefficient in (1.4) is prescribed: the theorem does not permit an arbitrary bounded replacement of $\mu(b)G(b)$. Fixed smooth norm factors may be incorporated in $W$.

A standard second moment followed by Cauchy gives $B^{1+\epsilon}D$ for the same left side, even for arbitrary bounded columns. We prove this comparison in Section 3. Theorem 1 saves $D^{2/3}$ when the label range grows. Its useful consequence is a bound for a projection of the **actual** corrected cubic output, given in Section 8. It leaves an explicit Möbius character signal and the complementary output uncontrolled; it proves no new zero-free region and does not resolve RH.

The comparison, with arbitrary small powers suppressed, is:

| Label range | Second-moment/Cauchy bound | Theorem 1 |
|---|---|---|
| $D\asymp1$ | $B$ | $B$ |
| $D=B^{1/6}$ | $B^{7/6}$ | $B^{19/18}$ |
| $D=B^{1/3}$ | $B^{4/3}$ | $B^{10/9}$ |

### 1.1. Relation to previous work

The arithmetic inputs are the Kubota identities and bounds in [1], Heath-Brown's squarefree cubic large sieve [2], and Patterson's cubic theta functional equation and ramified coefficients [3]. The first-mean estimate used below is a standard Type I/II consequence of these inputs, and we include its proof without a separate novelty claim.

The closest spectral comparison is de Faveri, Dunn and Hoffstein [4, Section 2], which combines the same cubic residue and central second moment to show that the generic cubic large sieve is not perfectly orthogonal. That lower-bound argument does not estimate the signed double remainder (1.4). Dunn and Radziwiłł [5, Section 9] and the September 25 first-moment preprint [6, Sections 5 and 7] already develop corrected cubic dispersion. We do not claim that correction mechanism as new. The latter preprint's stated comparison uses a rough prime-convolution coefficient with additional distribution assumptions, rather than the actual coefficient in (1.4).

Our earlier angular cubic/sextic mean [7] has different prescribed coefficients and a different transform. Our sextic Kubota estimate [8] concerns a sextic series and sixth-power-free operator. Neither gives (1.5). The zero-density result [9] concerns ordinary inverse character polynomials; the residual signal in Section 8 belongs to that family, but its existing density bound does not close the present output problem.

The new contribution is the joint signed estimate (1.5), with the matched Euler weight, every coprimality sector, both completion variables, and the full polar subtraction retained. Its proof uses a finite choice between the completed primal and dual formulas. After the prescribed column mean is applied, the two formulas obey the same elementary exponent inequality. Exact rational certificates supplied with the paper check that algebra but are not needed for the hand proof.

## 2. Arithmetic inputs and a prescribed first mean

Write

$$
\mathscr L(X,Y)=X+Y+(XY)^{2/3}.
$$

We use the squarefree cubic large sieve in the form

$$
\sum_{Nm\ll X}^{\mathrm{sf}}
\left|\sum_{Nn\ll Y}^{\mathrm{sf}}a_n\chi_m(n)\right|^2
\ll_\epsilon (XY)^\epsilon\mathscr L(X,Y)\sum_n|a_n|^2.
\tag{2.1}
$$

This is [2, Theorem 2], also [1, Theorem 3.12]. It includes either conjugate orientation. Fixed exclusions can remain inside the coefficient sequence or restrict the positive outer sum.

For squarefree $E$, put

$$
\psi_E(r,s)=\sum_{(c,E)=1}\frac{g(r,c)}{(Nc)^s},\qquad
\psi(r,s)=\psi_1(r,s),\qquad
\zeta_\lambda(s)=\sum_c(Nc)^{-s}=(1-3^{-s})\zeta_K(s).
\tag{2.2}
$$

The initial half-plane for $\psi$ is $\operatorname{Re}s>3/2$. We use the following precise source facts from [1, Corollary 6.2, Lemmas 6.3 and 6.6, and (6.11)–(6.15)]. For nonzero $r$,

$$
\psi(r,\sigma+it)\ll_\epsilon
(Nr)^{3/4-\sigma/2+\epsilon}(1+|t|)^{3-2\sigma+\epsilon},
\quad 1+\epsilon\le\sigma\le3/2,
\tag{2.3}
$$

away from its possible simple pole at $4/3$. Also, for fixed $1<\sigma\le5/4$,

$$
\sum_{0<Nm\le X}|\psi(hm,\sigma+it)|^2
\ll_{\sigma,\epsilon}(Nh)^{1/2}X^{1+\epsilon}(1+|t|)^2.
\tag{2.4}
$$

The variable numerator in (2.4) is unrestricted. At good primes the residue vanishes if the numerator has valuation two. For good squarefree $q$,

$$
\rho(q):=\operatorname*{Res}_{s=4/3}\psi(q,s)
=C_0\overline{G(q)}(Nq)^{-1/6}.
\tag{2.5}
$$

The completed function $Z(q,s)=\zeta_\lambda(3s-2)\psi(q,s)$ is holomorphic apart from the possible simple pole at $4/3$; the apparent pole at $2/3$ of the gamma-completed function is supplied by its gamma factor. We state the needed functional equation explicitly in Section 4.

**Lemma 2 (prescribed first mean).** For a good nonzero index $c$, a squarefree exclusion $E$, a fixed smooth annular $F$, and $X\ge1$,

$$
\sum_{(b,E)=1}\mu(b)G(b)\overline{\chi_b(c)}F(Nb/X)
\ll_\epsilon (XNcNE)^\epsilon
\left(X^{5/6}+X^{3/4}(Nc)^{1/4}\right).
\tag{2.6}
$$

The same bound holds for the finitely many fixed ramified cubic twists appearing in Section 4, with their fixed norms absorbed into the constant. We assert no arbitrary ray-weight extension.

*Proof.* First take $c=c_1c_2^2$ cube-free. Choose a fixed smooth cutoff $V_\le$ equal to one on $[0,1]$ and supported in $[0,2]$. Let $m(n)=\mu(n)V_\le(Nn/X_0)$, with $X_0=\sqrt{CX}$ and $C$ exceeding the upper endpoint of the support of $F$. The convolution $\delta_1-m*1$, where $\delta_1$ is the convolution identity, is supported above $X_0$, so its square vanishes on $Nn\le CX$. Convolution with $\mu$ gives the exact identity

$$
\mu=2m-m*m*1\qquad(Nn\le CX).
\tag{2.7}
$$

For large $X$, the first term has no support on the annulus. Partition the three factors of the remaining convolution into smooth dyads of norm lengths $U,V,L$, with $UVL\asymp X$ and $U,V\ll X^{1/2}$. The factor $G$ forces squarefreeness and mutual coprimality of the three factors. Logarithmic Fourier separation of the original product profile leaves common smooth coefficients and rapidly decaying height weights.

If $L\ll X^{2/3}$, group two factors so the resulting lengths $A,F_1$ satisfy $AF_1\asymp X$ and $X^{1/3}\ll A,F_1\ll X^{2/3}$. Cubic reciprocity and

$$
G(af)=G(a)G(f)\overline{\chi_a(f)}
\tag{2.8}
$$

leave two divisor-bounded coefficient vectors. The exclusion $E$ and the two characters of $c$ lie in these vectors. Cauchy and (2.1) bound the squared bilinear sum by

$$
(XNcNE)^\epsilon AF_1\mathscr L(A,F_1)
\ll (XNcNE)^\epsilon X^{5/3}.
\tag{2.9}
$$

If $L\gg X^{2/3}$, combine the two short factors into $r$, of norm length $R\asymp X/L\ll X^{1/3}$. Its coefficient is divisor-bounded. The remaining plain sum is

$$
\sum_{(w,rcE)=1}G(w)\overline{\chi_w(rc)}F_r(Nw/L).
\tag{2.10}
$$

The exterior character forces $(r,c)=1$. Its meromorphic series is $\psi_{\operatorname{rad}(rcE)}(rc,s+1/2)$. Corollary 6.2 of [1] and (2.3) give, on $\operatorname{Re}z=1+\epsilon$, a bound

$$
(NrNcNE)^\epsilon(NrNc)^{1/4+\epsilon}(1+|\operatorname{Im}z|)^A.
\tag{2.11}
$$

Indeed a squarefree-removal divisor $f$ has size $(Nf)^{3/2-2\operatorname{Re}z}$ and reduces the numerator by $f$, gaining $(Nf)^{-1/4+O(\epsilon)}$. An additional exclusion divisor $j$ has size $(Nj)^{1/2-\operatorname{Re}z}$ and enlarges the numerator by $j$, costing $(Nj)^{1/4+O(\epsilon)}$. Their divisor sums cost only subpowers; there is no fixed positive power of $NE$.

The Mellin shift gives error $L^{1/2+\epsilon}(NrNc)^{1/4+\epsilon}$. The pole vanishes when $c_2\ne1$; otherwise its absolute size is at most a subpower times $L^{5/6}(NrNc)^{-1/6}$. Summing the short factor gives, respectively,

$$
X^{1/2}R^{3/4}(Nc)^{1/4}\ll X^{3/4}(Nc)^{1/4},
\qquad
X^{5/6}(Nc)^{-1/6}\sum_{Nr\asymp R}\frac{|a_r|}{Nr}
\ll X^{5/6+\epsilon}(Nc)^\epsilon.
\tag{2.12}
$$

This proves (2.6) for cube-free $c$. For $c=c_{\mathrm{cf}}k^3$, cube reduction gives $\chi_b(c)=\chi_b(c_{\mathrm{cf}})\mathbf1_{(b,k)=1}$. Put $\operatorname{rad}(k)$ into the exclusion and use $Nc_{\mathrm{cf}}\le Nc$ and $N\operatorname{rad}(k)\le Nc$. This preserves all zeros. A fixed ramified cubic factor replaces the Type I numerator by a fixed ramified multiple; [1, Lemma 6.3 and Corollary 6.2] allow that numerator. The Type II argument is unchanged. Polynomial height costs are absorbed by the common rapidly decaying Fourier weights. This proves the lemma. $\square$

## 3. Weighted puncture removal, residue, and the comparison bound

The identity $1-u_p=u_p^2/(Np)$ gives

$$
u(a)=\sum_{l\mid a}\gamma(l),\qquad
\gamma(l)=\frac{\mu(l)u(l)^2}{Nl},\qquad |\gamma(l)|\le(Nl)^{-1}.
\tag{3.1}
$$

Let $r=r_1r_2^2$ with $r_1,r_2$ squarefree and coprime. Initially on $\operatorname{Re}s>3/2$, splitting the squarefree modulus $a=lc$ gives

$$
\Psi_u(r,s):=\sum_{(a,r)=1}^{\mathrm{sf}}u(a)g(r,a)(Na)^{-s}
=\sum_{(l,r)=1}^{\mathrm{sf}}\gamma(l)G(l)\overline{\chi_l(r)}
(Nl)^{1/2-s}\psi_{\operatorname{rad}(rl)}(rl,s).
\tag{3.2}
$$

The inner exclusion includes $l$. This is essential for squarefree splitting. Put $E=\operatorname{rad}(rl)$ and $\Delta_E(s)=\prod_{p\mid E}(1-(Np)^{2-3s})$. The exact removal formula is

$$
\psi_E(rl,s)=\Delta_E(s)^{-1}
\sum_{f\mid r_1l}\mu(f)(Nf)^{1-2s}
\overline{g(rl/f,f)}\,\psi(rl/f,s).
\tag{3.3}
$$

This is [1, Corollary 6.2]; its first Gauss factor is conjugated. Since $(rl/f,f)=1$, that factor has modulus $(Nf)^{1/2}$. Equations (2.3) and (3.3) make (3.2) normally convergent near every fixed central line $\operatorname{Re}s=1+\tau$, $0<\tau<1/4$, away from the pole. The outer $l$ coefficient has norm exponent at most $-5/4+O(\tau)$, with a sufficiently small allocated auxiliary loss. In particular all Mellin shifts below use a genuine meromorphic continuation.

If $r_2\ne1$, every numerator in (3.3) retains a squared prime and the residue is zero. If $r$ is squarefree, (2.5), Gauss multiplicativity and (3.3) give the unweighted punctured residue $C_0\overline{G(r)}(Nr)^{-1/6}\prod_{p\mid r}(1+1/Np)^{-1}$. Inserting (3.1), the free-prime factor of the $l$ sum is

$$
1-\frac{u_p^2}{q(q+1)}=\frac{q+u_p}{q+1}.
$$

At an excluded prime its ratio with $q/(q+1)$ is $q/(q+u_p)=u_p$. Thus

$$
\operatorname*{Res}_{s=4/3}\Psi_u(r,s)
=\mathbf1_{r\ \mathrm{sf}}C_0\mathfrak e\,u(r)\overline{G(r)}(Nr)^{-1/6}.
\tag{3.4}
$$

Mellin inversion proves (1.3), with

$$
R_r^u(B)=\frac1{2\pi i}\int_{(1+\tau)}
\widehat V(s-2/3)B^{s-2/3}\Psi_u(r,s)\,ds.
\tag{3.5}
$$

### 3.1. The same-object $BD$ baseline

For completeness, (2.4) implies

$$
\sum_{Nr\le X}^{\mathrm{cf}}|\Psi_u(r,1+\tau+it)|^2
\ll_{\tau,\epsilon}X^{1+\epsilon}(1+|t|)^A.
\tag{3.6}
$$

To see the uniformity, fix $l$ in (3.2), write a removal divisor as $f=f_rf_l$ with $f_r\mid r_1$ and $f_l\mid l$, and use divisor Cauchy. Its squared coefficient on the central line is at most $(Nf_rNf_l)^{-1}$. Write $r=f_rm$ and apply (2.4) to $m(l/f_l)$. Positive enlargement gives the bound

$$
X(Nl)^{1/2}
\sum_{f_r}(Nf_r)^{-2}\sum_{f_l\mid l}(Nf_l)^{-3/2},
\tag{3.7}
$$

up to subpowers. The first sum converges and the second is divisor-bounded. The possible squared primes in $m$ are allowed in (2.4). Minkowski in $l$ is then summable, since

$$
\sum_l|\gamma(l)|(Nl)^{-1/2-\tau}(Nl)^{1/4+\epsilon}
\ll\sum_l(Nl)^{-5/4-\tau+\epsilon}<\infty.
$$

Equation (3.5) consequently gives $\sum_{Nr\le X}^{\mathrm{cf}}|R_r^u(B)|^2\ll B^{2/3+\epsilon}X^{1+\epsilon}$. For bounded squarefree columns $\alpha_b$ supported on $Nb\asymp B$, Cauchy and grouping $r=bv$, whose multiplicity is divisor-bounded, give

$$
\frac1B\sum_{Nv\asymp D}^{\mathrm{sf}}
\left|B^{-1/3}\sum_b\alpha_bR_{bv}^u(B)\right|^2
\ll B^{-2/3}\sum_{b,v}|R_{bv}^u(B)|^2
\ll (BD)^{1+\epsilon}.
\tag{3.8}
$$

Theorem 1 improves this specific comparison by using the signed column rather than Cauchy in $b$.

## 4. Two completed representations and a finite switch

In (3.3) write $q=rl/f$. On the central line the completion reciprocal has the absolutely convergent expansion

$$
\frac1{\zeta_\lambda(3s-2)\Delta_E(s)}
=\sum_{(d,rl)=1}\mu(d)(Nd)^{2-3s}.
\tag{4.1}
$$

Define

$$
\begin{aligned}
\mathcal Z_q(T)&=\frac1{2\pi i}\int_{(1+\tau)}
\widehat V(s-2/3)T^{s-2/3}Z(q,s)\,ds,\\
T&=\frac{B}{Nl(Nf)^2(Nd)^3},\\
A_{r;l,f}&=\gamma(l)G(l)\overline{\chi_l(r)}\mu(f)
(Nl)^{-1/6}(Nf)^{-1/3}\overline{g(q,f)}.
\end{aligned}
\tag{4.2}
$$

Then the exact central identity is

$$
R_r^u(B)=\sum_{(l,r)=1}^{\mathrm{sf}}\sum_{f\mid r_1l}
\sum_{(d,rl)=1}\mu(d)A_{r;l,f}\mathcal Z_q(T),
\qquad
|A_{r;l,f}|=|\gamma(l)|(Nl)^{-1/6}(Nf)^{1/6}.
\tag{4.3}
$$

The powers in (4.2) follow directly by separating $B^{s-2/3}(Nl)^{1/2-s}(Nf)^{1-2s}(Nd)^{2-3s}$. Equation (4.3) is first understood in the normally convergent order furnished by (3.2) and (4.1).

The completed primal formula is

$$
\mathcal Z_q(T)=\sum_{c,e}g(q,c)(Nc)^{-2/3}V\!\left(\frac{Nc(Ne)^3}{T}\right)
-\zeta_\lambda(2)\rho(q)T^{2/3}\widehat V(2/3).
\tag{4.4}
$$

The second completion index $e$ is unrestricted. It must not be suppressed.

### 4.1. The finite ramified packet

Put $\lambda=1-\omega$, $\mathcal G(s)=(2\pi)^{-2s}\Gamma(s-1/3)\Gamma(s-2/3)$, and

$$
A(s)=\frac{3^{8-9s}(1-3^{3-3s})}{1-3^{3s-4}},\qquad
B(s)=\frac{2\,3^{8-9s}}{1-3^{3s-4}}.
$$

For a good primary $q$, [1, (6.11)–(6.12)] states

$$
\begin{aligned}
\mathcal G(s)Z(q,s)=(Nq)^{1-s}\mathcal G(2-s)
\bigg[B(s)Z(q,2-s)
 +A(s)\sum_{\nu^6=1}\sum_{j=2}^5
 \Gamma(q,\nu\lambda^j)3^{-j(2-s)}Z(\nu\lambda^jq,2-s)\bigg].
\end{aligned}
\tag{4.5}
$$

Patterson's coefficient identity [3, Proposition 5.1] gives, for these good $q$,

$$
\Gamma(q,\eta)=\overline{\chi_q(\eta)}\Gamma(1,\eta),
\qquad \eta=\nu\lambda^j.
\tag{4.6}
$$

Thus the $q$ dependence is a fixed ramified cubic character, not an arbitrary bounded ray coefficient. Let $\xi_1(q)=1$, and $\xi_\eta(q)=\overline{\chi_q(\eta)}$ for the other packet entries. Define $H_1$ by the Mellin kernel

$$
\widehat V(s-2/3)x^{s-2/3}\frac{\mathcal G(2-s)}{\mathcal G(s)}B(s),
$$

and define $H_\eta$ by replacing $B(s)$ with $A(s)\Gamma(1,\eta)3^{-j(2-s)}$. Integrate on a fixed line $0<\operatorname{Re}s<1/2$, with factor $1/(2\pi i)$. Shifting the integral for $Z$ to this line crosses no pole. Expanding its reflected completed series, which is then absolutely convergent, yields

$$
\mathcal Z_q(T)=(Nq)^{1/3}\sum_\eta\xi_\eta(q)
\sum_{c,e}g(\eta q,c)(Nc)^{-4/3}(Ne)^{-2}
H_\eta\!\left(\frac{TNc(Ne)^3}{Nq}\right).
\tag{4.7}
$$

Every $H_\eta$ is a common scalar kernel, independent of $q$. For any fixed $\zeta>0$, integer $M\ge0$, and fixed number of logarithmic derivatives,

$$
H_\eta(x)\ll_{\zeta,M,V}\min(x^{2/3-\zeta},x^{-M}),
\tag{4.8}
$$

with the same estimate for those derivatives. For small $x$, move the kernel contour to $4/3-\zeta$; for large $x$, move left. The first poles on the right have real part $4/3$. This proves the stated power behavior at zero, rather than an unsupported Schwartz bound there.

### 4.2. Where each representation is used

Take $r=bv$ with $Nb\asymp B$, $Nv\asymp D$. First restrict $Nl\le C B$, with a fixed sufficiently large support constant. For each fixed removal divisor $f$, set

$$
H_0=\left(\frac{B}{D(Nl)^3(Nf)^3}\right)^{1/6}.
\tag{4.9}
$$

Use (4.7) for $Nd\le H_0$ when $H_0>1$, and (4.4) for the remaining $d$. If $H_0\le1$, use (4.4) everywhere. A smooth transition is permitted but unnecessary, since each $d$ will be fixed before applying any mean estimate. The low-$d$ outer sum is finite. The high-$d$ primal sum is finite by support, and its entire polar subtraction is retained and absolutely summable after the column mean is applied. This makes no rearrangement of an infinite transformed outer sum. Section 7 treats $Nl>CB$ directly.

The effective dual scale in (4.7) is

$$
Nc(Ne)^3\asymp\frac{Nq}{T}
\asymp D(Nl)^2Nf(Nd)^3.
\tag{4.10}
$$

Both completion variables are present on this scale. The switch (4.9) is chosen before the subsequent modulus-overlap decomposition; it does not identify individual primal and dual overlap sectors.

## 5. Overlap phases and the two column estimates

For a good cube-free numerator $q$, the local Gauss rules [1, Lemmas 3.1–3.2] allow modulus valuation $0$ or $2$ at a prime where $q$ has valuation one, and valuation $0$ or $3$ where $q$ has valuation two. Elsewhere the modulus is squarefree. Thus every nonzero term has a unique representation

$$
c=j^2k^3n,\qquad j\mid q_1,\quad k\mid q_2,\quad (n,q)=1,
\tag{5.1}
$$

where $q=q_1q_2^2$ and $j,k,n$ are squarefree and mutually coprime. The exact local and CRT identity is

$$
g(q,j^2k^3n)=Nj(Nk)^2\mu(k)\overline{g(q/j,j)}\,g(q/j,n).
\tag{5.2}
$$

For example, the numerator in the $n$ factor is $qj^2k^3$, differing from $q/j$ by a cube. The ramified packet uses the same identity with $\eta q$ in the numerator positions; its good-prime valuation pattern is unchanged.

Split the removal and overlap divisors according to their original supports:

$$
\begin{gathered}
f=f_bf_vf_l,\qquad j=j_bj_vj_l,\\
b=f_bj_bk b_0,\qquad v=f_vj_vk v_0,\qquad l=f_lj_ll_0.
\end{gathered}
\tag{5.3}
$$

All displayed fixed factors have their literal mutual exclusions. The variables $b_0,v_0$ may share primes. A prime removed by $f$ is allowed to divide $n$; one must not impose a new zero-extended character of $f$ on $n$.

The dependence on $b_0$ can be read from the five factors below. Cubic reciprocity is applied only on the retained coprime support.

| Factor | Its $b_0$-dependent character |
|---|---|
| $G(b)$ | $\overline{\chi_{b_0}(f_bj_bk)}$ |
| $\overline{\chi_l(bv)}$ | $\overline{\chi_{b_0}(f_lj_ll_0)}$ |
| $\overline{g(q,f)}$ | $\chi_{b_0}(f_bf_vf_l)$ |
| $\overline{g(q/j,j)}$ | $\chi_{b_0}(j_bj_vj_l)$ |
| $g(q/j,n)$ | $\overline{\chi_{b_0}(n)}$ |

Their product leaves the actual column

$$
\mu(b_0)G(b_0)\overline{\chi_{b_0}(nkl_0f_v^2j_v^2)}.
\tag{5.4}
$$

There is no remaining $b_0$–$v_0$ character. The $v_0$ dependence is $\overline{\chi_{v_0}(n)}$ times fixed row characters. The remaining dependence on $n$ lies in a common coefficient, with the exclusions from (5.1). Formula (4.6) only adds fixed ramified cubic factors to these column and row characters.

The numerator in (5.4) need not be cube-free. Specifically, $A=(n,f_v)$ may be nonunit; remove $A^3$ from that numerator and retain the already fixed exclusion $f_v$. Lemma 2 applies, and its raw index norm is an upper bound for the reduced one. This includes these sectors rather than deleting them.

Keep each $d$ fixed while applying the means. The condition $(d,bvl)=1$ now supplies only fixed exclusions in the $b_0$ and $v_0$ variables and restrictions on fixed divisors. Lemma 2 is uniform in the column exclusion at subpower cost. The row exclusion may be kept until after the positive large-sieve bound. This is the point at which the proof avoids a summatory assumption: Minkowski over $Nd\asymp H$ subsequently costs $H^{1+\epsilon}$, without creating an arbitrary row-dependent column.

### 5.1. Common profiles

On fixed norm dyads, the primal profile and each normalized dual profile are smooth functions of the normalized norms of $b_0,v_0,n$. The other factors are fixed parameters. For the dual profile first divide by the small- or large-argument envelope in (4.8); every fixed derivative of the resulting dyadic function is bounded. A Fourier expansion in logarithmic norm coordinates, after extending by fixed smooth cutoffs, writes the profile as an integral of products of one-variable norm phases with a common rapidly decaying coefficient. The character coefficients and exclusions in (5.4) remain literal. The polynomial height costs in (2.3) and Lemma 2 are integrable against this coefficient. Thus the same two column estimates and the row sieve apply before the common integral is evaluated.

### 5.2. The full exponent ledger

All lengths in the following paragraph are logarithms to base $B$. Use

$$
\begin{gathered}
\delta=\log_B D,\quad \eta=\log_B H,\quad \xi=\log_B E_1,\\
a=\log_B Nf_b,\quad f_0=\log_B Nf_v,\quad
u=\log_B Nj_b,\quad w=\log_B Nj_v,\quad \kappa=\log_B Nk,\\
L=\log_B Nl,\quad F=\log_B Nf_l,\quad J=\log_B Nj_l,
\end{gathered}
$$

where $Ne\asymp E_1$. Let $s$ be the modulus exponent before removing $j^2k^3$. Put

$$
\begin{aligned}
\beta&=1-a-u-\kappa,& r_0&=\delta-f_0-w-\kappa,\\
n_0&=s-2u-2w-2J-3\kappa,&
c_0&=n_0+\kappa+L-F-J+2f_0+2w,\\
\ell(x,y)&=\max\{x,y,2(x+y)/3\}.&&
\end{aligned}
\tag{5.5}
$$

The quantities $\beta,r_0,n_0$ are nonnegative, $F+J\le L$, and $c_0$ is the raw **index** norm exponent in (5.4), not a conductor exponent. The two completed scales are

$$
\begin{aligned}
t&=1-L-2a-2f_0-2F-3\eta-3\xi &&\text{(primal)},\\
x&=\delta+2L+a+f_0+F+3\eta-3\xi &&\text{(central dual)}.
\end{aligned}
\tag{5.6}
$$

The two available bounds for the column square mean, after division by $B$, have exponents

$$
M=\min\!\left\{
\beta+\ell(n_0,\beta)-1,
\ n_0+\max\{5\beta/3,3\beta/2+c_0/2\}-1
\right\}.
\tag{5.7}
$$

The first comes from (2.1), absorbing the fixed part of (5.4) into its coefficients. The second sums the square of Lemma 2 over $n$. The outer row sieve costs $B^{\ell(r_0,n_0)+\epsilon}$.

For clarity, the scalar amplitudes before these two transforms, including the $B^{-1/3}$ in (1.4), are bounded on their dyads by

$$
\begin{aligned}
\text{primal}:&\quad |\gamma(l)|B^{-1/3}(Nl)^{-1/6}(Nf)^{1/6}
(Nj)^{1/6}(Nn)^{-1/6}H E_1,\\
\text{dual}:&\quad |\gamma(l)|D^{1/3}(Nl)^{1/6}(Nf)^{-1/6}
(Nj)^{-7/6}(Nk)^{-2}(Nn)^{-5/6}H E_1^{-1}.
\end{aligned}
\tag{5.8}
$$

The $H$ factor counts fixed $d$ by Minkowski. The primal coefficient of $e$ is one, whereas its dual coefficient is $(Ne)^{-2}$; counting every $e$ therefore gives $E_1$ and $E_1^{-1}$ respectively.

Sum $f_b,j_b$ by Minkowski, at squared cost $B^{2a+2u+\epsilon}$. Inside each original row $v$, divisor Cauchy costs only a subpower for its choices $f_v,j_v,k$; summing the remaining fixed divisors then costs $B^{f_0+w+\kappa+\epsilon}$. For each fixed $l$, its divisors $f_l,j_l$ cost a subpower. The count of $l$ in a dyad cancels $|\gamma(l)|\le1/Nl$ in Minkowski. Squaring (5.8), the resulting normalized energy exponents are exactly

$$
\begin{aligned}
P={}&-2/3-L/3+(a+f_0+F+u+w+J)/3-n_0/3
+2\eta+2\xi+\ell(r_0,n_0)+M+2a+2u+f_0+w+\kappa,\\
Q={}&2\delta/3+L/3-(a+f_0+F)/3-7(u+w+J)/3-4\kappa-5n_0/3
+2\eta-2\xi+\ell(r_0,n_0)+M+2a+2u+f_0+w+\kappa.
\end{aligned}
\tag{5.9}
$$

Here $n_0=t-2u-2w-2J-3\kappa$ for $P$, and $n_0=x-2u-2w-2J-3\kappa$ for the central $Q$. Fixed ratios in dyadic endpoints introduce only bounded shifts of logarithmic lengths, hence harmless constant factors in these finitely many affine expressions.

## 6. An elementary common bound for the primal and dual

The following lemma is the exponent argument needed for the proof. It does not require linear programming.

**Lemma 3.** Let $0\le r\le\delta\le1/3$, $0\le b\le1$, $\lambda_0\ge0$, and $0\le n\le(b+r+\lambda_0)/2$. Then

$$
\begin{aligned}
\Phi(b,r,n,\lambda_0)
={}&\ell(r,n)-\lambda_0\\
&+\min\!\left\{\ell(n,b)-n,
\max\!\left(\frac{2b}{3},\frac{b+n+2\delta-2r+\lambda_0}{2}\right)\right\}
\le1+\frac\delta3.
\end{aligned}
\tag{6.1}
$$

*Proof.* Increasing $\lambda_0$ increases the inner minimum by at most half that increase, and decreases the exterior by the full increase. Thus take $\lambda_0=\max(0,2n-b-r)$. If $n>(b+r)/2$, then $n\ge b/2$, and

$$
\ell(n,b)-n=\max(0,(2b-n)/3)\le2b/3.
$$

The generic branch is selected, so the expression becomes

$$
\ell(r,n)-2n+b+r+\max(0,(2b-n)/3).
$$

This decreases in $n$: the first term is $1$-Lipschitz and the last is nonincreasing. Reduce $n$ to $(b+r)/2$. It remains to consider $\lambda_0=0$ and $n\le(b+r)/2$. The expression is nondecreasing in $b$, so enlarge $b$ to one. Now $n\le(1+r)/2\le2/3$.

If $n\ge1/2$, the minimum is $(2-n)/3$, and $n\ge r$. Therefore

$$
\Phi=\max(2/3+2n/3,\ 2/3+n/3+2r/3)
\le\max(1+r/3,\ 5/6+5r/6)\le1+\delta/3.
$$

If $n\le1/2$, put $A=1-n$ and $C=(1+n+2\delta-2r)/2$. The three row branches are $n,r,2(r+n)/3$. The $n$ branch is at most $n+A=1$. The $r$ branch is at most

$$
r+\max(2/3,C)\le\max(2/3+\delta,\ 3/4+\delta)\le1+\delta/3.
$$

For the mixed branch, if $2r-n\le\delta$, use $A$ to get $1+(2r-n)/3\le1+\delta/3$. Otherwise $n<2r-\delta$. Adding $2(r+n)/3$ to the two entries of $\max(2/3,C)$ gives bounds

$$
\frac23+\frac{4\delta}{3},\qquad
\frac12+\frac{11\delta}{6},
$$

both at most $1+\delta/3$ for $\delta\le1/3$. This exhausts the cases. Equality is attained at $b=1$, $r=\delta$, $n=(1+\delta)/2$, $\lambda_0=0$. $\square$

### 6.1. Reduction of the full weighted ledger

Use the scale equation (5.6) to eliminate $2\eta+2\xi$ from $P$, or $2\eta-2\xi$ from $Q$. In either case the base in (5.9), including its divisor counts but excluding the row cost and $M$, becomes

$$
a+u-\kappa-L-F-J-n_0.
$$

Since $a+u=1-\beta-\kappa$, both exponents are

$$
\ell(r_0,n_0)-2\kappa-L-F-J
+\min\!\left\{\ell(n_0,\beta)-n_0,
\max(2\beta/3,(\beta+c_0)/2)\right\}.
\tag{6.2}
$$

The switch (4.9) says $\eta\ge\eta_0$ in the primal and $\eta\le\eta_0$ in the dual, where

$$
\eta_0=\frac{1-\delta-3L-3a-3f_0-3F}{6}.
$$

Using $\xi\ge0$, either side gives

$$
\begin{aligned}
n_0&\le\frac{1+\delta+L-a-f_0-F}{2}-2u-2w-2J-3\kappa\\
&=\frac{\beta+r_0+L-F}{2}-\frac32(u+w)-2J-2\kappa.
\end{aligned}
\tag{6.3}
$$

This remains valid when $\eta_0<0$, since then every primal $\eta\ge0$ satisfies $\eta\ge\eta_0$. Put $\lambda_0=L-F\ge0$. Also

$$
c_0=n_0+\lambda_0+2\delta-2r_0-J-\kappa.
$$

Drop the nonnegative losses $2\kappa+2F+J$ and enlarge the latter numerator exponent by $J+\kappa$. Equations (6.2)–(6.3) are bounded by Lemma 3 with $(b,r,n)=(\beta,r_0,n_0)$. Thus both main representations have normalized energy exponent at most $1+\delta/3$.

### 6.2. The dual-kernel tails

In a small-argument dyad $TNc(Ne)^3/Nq\asymp B^{-\rho}$, $\rho\ge0$, the exponent $s$ in (5.5) is $x-\rho$. Eliminating $\eta-\xi$ adds $2\rho/3$ to (6.2), while the squared kernel in (4.8) costs $4\rho/3$ before the allocated small loss. The total is (6.2) minus $2\rho/3$, and (6.3) is strengthened by $-\rho$. Lemma 3 applies. Here $\rho$ and all scale exponents are bounded by the finite outer constraints, so the small losses are uniform.

For a large-argument dyad, use $s=x+\rho$ and the kernel bound $x^{-10}$. The resulting energy is (6.2) minus $(20+2/3)\rho$, and (6.3) is relaxed by $+\rho$. Increase $\lambda_0$ to $\lambda_0+2\rho$ in (6.1). Its admissibility is restored. Since the inner minimum is nondecreasing in $\lambda_0$,

$$
\Phi(b,r,n,\lambda_0)
\le\Phi(b,r,n,\lambda_0+2\rho)+2\rho.
$$

Lemma 3 requires no upper bound on $\lambda_0$. Hence the actual exponent is at most

$$
1+\delta/3-\frac{56}{3}\rho.
\tag{6.4}
$$

This leaves ample geometric decay for the infinitely many dual dyads, their completion-index counts, and all subpower losses. Finite dyadic sums and common profile integrals fit into the requested $B^\epsilon$.

## 7. The polar subtraction and the outer tail

The polar part of (4.4) vanishes unless $bv$ is squarefree, hence unless $(b,v)=1$. On that support all its Gauss phases collapse exactly:

$$
\begin{aligned}
&G(l)\overline{\chi_l(bv)}\mu(f)\overline{g(bvl/f,f)}\rho(bvl/f)\\
&\hspace{1cm}=C_0\overline{G(bv)}(NbNv)^{-1/6}
\mu(f)(Nf)^{2/3}(Nl)^{-1/6}.
\end{aligned}
\tag{7.1}
$$

Thus, apart from the fixed constant $-\zeta_\lambda(2)C_0\widehat V(2/3)$, its high-$d$ contribution to $R_{bv}^u(B)$ is

$$
\overline{G(bv)}(NbNv)^{-1/6}B^{2/3}
\frac{\gamma(l)}{Nl}\frac{\mu(f)}{Nf}
\sum_{\substack{Nd>H_0\text{ if }H_0>1\\(d,bvl)=1}}
\frac{\mu(d)}{(Nd)^2}.
\tag{7.2}
$$

When $H_0\le1$, use the full $d$ sum. Multiplication by the exterior $\mu(b)G(b)$ leaves an ordinary character polynomial, because

$$
G(b)\overline{G(bv)}=\overline{G(v)}\chi_b(v)
\qquad((b,v)=1).
\tag{7.3}
$$

Fix $d,l,f_b,f_v,f_l$ before applying (2.1). The remaining column length is $B/Nf_b$ and the row length is $D/Nf_v$, with fixed exclusions and ordinary cubic characters. Minkowski only in $d$ then costs

$$
\sum_{Nd>H_0}(Nd)^{-2+\epsilon}\ll H_0^{-1+\epsilon}
\quad(H_0>1),
\tag{7.4}
$$

and costs a constant for the full sum. This absolute estimate is applied after retaining cancellation in the column polynomial, not to that polynomial itself.

Using the same divisor counts as in Section 5, the normalized polar energy exponent is

$$
R=\frac{1-\delta}{3}-2L-a-f_0-2F
+\ell(\delta-f_0,1-a)-2\max(0,\eta_0).
\tag{7.5}
$$

For example the squared $l$ count leaves $(Nl)^{-2}$ from $|\gamma(l)/Nl|^2$, and the remaining $f_b,f_v,f_l$ costs are $(Nf_b)^{-1},(Nf_v)^{-1},(Nf_l)^{-2}$. These give all non-cutoff terms in (7.5). Put $S=L+a+f_0+F$. Then (7.5) simplifies to

$$
R=\ell(\delta-f_0,1-a)-L-F
+\min\!\left(0,\frac{1-\delta}{3}-S\right)\le1,
\tag{7.6}
$$

since $\ell(\delta,1)=1$ for $\delta\le1/3$. This controls the full polar subtraction.

Finally, if $Nl>CB$ with the support constant chosen in Section 4, the primal sum in (4.4) vanishes identically for every $f,d$. If $bv$ has a squared prime its residue also vanishes. Otherwise (7.1), $|\gamma(l)|\le1/Nl$, the divisor bound, and absolute summation of $\sum_d(Nd)^{-2}$ give

$$
|R_{bv}^{u,\,l>CB}(B)|
\ll B^{2/3}(NbNv)^{-1/6+\epsilon}
\sum_{Nl>CB}(Nl)^{-2+\epsilon}
\ll B^{-1/3+\epsilon}(NbNv)^{-1/6+\epsilon}.
\tag{7.7}
$$

After the normalization in (1.4), absolute $b$ summation gives normalized joint energy

$$
\frac1B\sum_{Nv\asymp D}|\mathcal E_v^{\,l>CB}(B)|^2
\ll B^{-2/3+\epsilon}D^{2/3+\epsilon}.
\tag{7.8}
$$

This is smaller than (1.5). All other outer ranges are finite; the large-argument dual dyads have the decay (6.4). Choose the auxiliary losses in the source estimates, profile envelopes and divisor bounds sufficiently small in terms of the requested $\epsilon$. The finite packet, common height integrals and dyadic counts then contribute at most $B^\epsilon$. Equations (6.1)–(6.4), (7.6) and (7.8) prove Theorem 1. $\square$

## 8. A projection of the actual corrected output

Here assume $V,W\ge0$ are nonzero and have smooth square roots. All matrix rows and columns are squarefree good indices. At the balanced scale define

$$
\begin{aligned}
K_{a,b}&=\sqrt{V(Na/B)}\,G(b)\overline{\chi_b(a)}\sqrt{W(Nb/B)},\\
P_{a,b}&=c_*\sqrt{V(Na/B)}\,\overline{G(a)}(NaNb)^{-1/6}
\mathbf1_{(a,b)=1}\sqrt{W(Nb/B)},\\
C&=K-P,\qquad c_*=\frac{(2\pi)^{2/3}}{3\Gamma(2/3)}.
\end{aligned}
\tag{8.1}
$$

This is the ordinary masked cubic polar correction of [5, Section 9]. Let

$$
\begin{aligned}
I_V&=\int_0^\infty V(x)x^{-1/3}\,dx,\qquad
I_W=\int_0^\infty W(x)x^{-1/3}\,dx,\\
k_u&=\operatorname*{Res}_{s=1}\zeta_\lambda(s)
\prod_{p\nmid3}(1-(Np)^{-1})(1+u_p^2/(Np)),\\
k_{u,v}&=k_u\prod_{p\mid v}(1+u_p^2/(Np))^{-1}.
\end{aligned}
\tag{8.2}
$$

The product defining $k_u$ is absolutely convergent, and $k_{u,v}^{-1}\ll_\epsilon(Nv)^\epsilon$. For a squarefree nonunit label $v$, put

$$
\begin{aligned}
x_v^-(b)&=\frac{\sqrt{W(Nb/B)}u(b)\overline{\chi_b(v)}(Nb)^{-1/6}}
{\sqrt{k_{u,v}I_W}\,B^{1/3}},\\
z_v(a)&=\frac{\sqrt{V(Na/B)}u(a)\overline{G(a)}\chi_a(v)(Na)^{-1/6}}
{\sqrt{k_{u,v}I_V}\,B^{1/3}},\\
t_v&=C_0\mathfrak e\sqrt{I_VI_W}\,B^{2/3}u(v)\overline{G(v)}(Nv)^{-1/6}.
\end{aligned}
\tag{8.3}
$$

The label is the opposite cubic orientation to the usual $\chi_b(v)$ input. The pole in its image occurs on $(a,v)=1$, because an overlap gives numerator valuation two. Formula (3.4) and $G(av)=G(a)G(v)\overline{\chi_a(v)}$ produce exactly the profiles in (8.3).

Let $Z_0$ be a fixed smooth function on the column annulus and take the actual input

$$
\beta_b=\mu(b)\sqrt{W(Nb/B)}Z_0(Nb/B).
$$

Define its normalized inverse character mean, with the orientation displayed explicitly, by

$$
M_v^u(B)=B^{-1/2}\sum_b\mu(b)u(b)\chi_b(v)
(Nb/B)^{-1/6}W(Nb/B)Z_0(Nb/B).
\tag{8.4}
$$

**Theorem 4.** Let $\eta>0$ be fixed and $1\le H\le B^{1/3-\eta}$. For any set $\mathcal S$ of squarefree nonunit labels with $Nv\le H$, let $Q_{\mathcal S}$ be the orthogonal projection in output space onto the span of $z_v$, $v\in\mathcal S$. Then

$$
\frac{\|Q_{\mathcal S}C\beta\|^2}{B}
\ll_{\epsilon,\eta,V,W,Z_0}
B^{1/3+\epsilon}\sum_{v\in\mathcal S}(Nv)^{-1/3}|M_v^u(B)|^2
+B^{1+\epsilon}H^{1/3}.
\tag{8.5}
$$

*Proof.* Use the inner product linear in its first argument. The diagonal Gram entries of the $z_v$ are $1+O(B^{-1/2+\epsilon}H^\epsilon)$. For $v\ne w$, the remaining character in the Gram entry is a nonprincipal cubic ratio. Its primitive conductor divides a fixed multiple of $vw/(v,w)^2$, of norm at most a fixed multiple of $NvNw$. The original exclusions at primes of $vw$ are retained.

The weighted squarefree Dirichlet series is $L(s,\chi)$ times an Euler product absolutely convergent for $\operatorname{Re}s>1/2$. At a free prime its relative local factor is

$$
(1+u_p^2\chi(p)(Np)^{-s})(1-\chi(p)(Np)^{-s}).
$$

Its linear coefficient is $O((Np)^{-1-s})$ and its quadratic term is $O((Np)^{-2s})$. Excluded factors cost only subpowers. A smooth shift to $\operatorname{Re}s=1/2+\epsilon$ and ordinary Hecke convexity (the degree-two functional equation and Phragmén–Lindelöf, as in [10, Section 5.2]) therefore give

$$
|\langle z_v,z_w\rangle|
\ll B^{-1/2+\epsilon}(NvNw)^{1/4+\epsilon}\quad(v\ne w).
$$

The same shift in the principal case supplies the stated diagonal error. Schur's bound yields

$$
\|\operatorname{Gram}(z_v:v\in\mathcal S)-I\|
\ll B^{-1/2+\epsilon}H^{3/2+\epsilon}=o(1).
\tag{8.6}
$$

Thus the Gram inverse is uniformly bounded, after choosing the auxiliary losses in terms of $\eta$.

Directly expanding $\langle K\beta,z_v\rangle$, the scalar inner sum is $S_{bv}^u(B)$. Equations (1.3) and (8.3) give the exact coordinate identity

$$
\langle C\beta,z_v\rangle
=t_v\langle\beta,x_v^-\rangle+e_v-p_v,
\qquad
\langle\beta,x_v^-\rangle=\frac{M_v^u(B)}{\sqrt{k_{u,v}I_W}},
\tag{8.7}
$$

where $p_v=\langle P\beta,z_v\rangle$ and

$$
e_v=(k_{u,v}I_V)^{-1/2}\mathcal E_v(B;V,WZ_0).
$$

Theorem 1, summed over norm dyads and with the subpower normalization absorbed, proves

$$
\frac1B\sum_{v\in\mathcal S}|e_v|^2
\ll B^{1+\epsilon}H^{1/3}.
\tag{8.8}
$$

For the ordinary correction, $v\ne1$ ensures the weighted sum in $P^*z_v$ is nonprincipal. The same Hecke convexity argument, now with weight $(Na)^{-1/3}$ and fixed exclusion $b$, bounds that unnormalized $a$ sum by $B^{1/6+\epsilon}(Nv)^{1/4+\epsilon}$. The normalizations in (8.1) and (8.3) consequently give

$$
\|P^*z_v\|^2\ll B^{1/3+\epsilon}(Nv)^{1/2+\epsilon}.
\tag{8.9}
$$

Since $\|\beta\|^2\ll B$, its contribution after summing $v$ and dividing by $B$ is $O(B^{1/3+\epsilon}H^{3/2+\epsilon})$, smaller than the error in (8.5) throughout the stated range. Finally, bounded inversion of the Gram matrix converts the actual coordinates (8.7) into the norm of the output projection. The factor $|t_v|^2/B$ has size $B^{1/3}u(v)^2(Nv)^{-1/3}$ times a fixed constant. Equations (8.7)–(8.9) prove (8.5). $\square$

### 8.1. The remaining arithmetic question

The right side of (8.5) contains a signed inverse character signal. The extra Euler product from $\mu(n)$ to $\mu(n)u(n)$ is absolutely convergent and nonzero for $\operatorname{Re}s>0$, since $1-u_p=O((Np)^{-1})$. It creates no new zero poles but does not cancel zeros of the corresponding $L$-function. Hence an estimate for the signal requires its own arithmetic input.

For example, [9] gives the index-ordered density exponent $G(\sigma)=16(1-\sigma)/(4\sigma+1)$ at sufficiently small positive-power heights. If a separate global boundary $7/8$ and the corresponding buffered pointwise contour estimates are imported, the high-zero bin on $D=B^\delta$ has exponent

$$
2\sigma-\frac23+\delta\bigl(G(\sigma)-1/3\bigr).
$$

At $\sigma=7/8$ this is $13/12+\delta/9$. It does not decrease with the label length. This conditional calculation explains why the accepted density result alone does not remove the signal. Neither that global boundary nor a new density estimate is asserted here.

Theorem 4 uses the actual vector $C\beta$ and does not replace $\beta$ by its input projection. It makes no claim that the displayed modes exhaust the spectrum, and gives no estimate for $(I-Q_{\mathcal S})C\beta$. These limitations are essential to its connection with the motivating zeta-zero problem.

## 9. Reproducibility and scope of the checks

The proof of Theorem 1 is the analytic reduction in Sections 2–5, the elementary Lemma 3 and its tail argument, and the polar estimates in Section 7. No numerical extrapolation or optimization solver is required for that proof.

The supplement contains 78 exact rational certificates for the original unsimplified ledger: 18 primal, 18 central dual, 18 small-argument dual, 18 large-argument dual and six polar branches. Every certificate verifies an identity

$$
U-F(\mathbf x)=\sum_i\lambda_i[-g_i(\mathbf x)],\qquad
\lambda_i\ge0,
$$

for the listed affine constraints $g_i(\mathbf x)\le0$, and includes an exactly feasible equality point. For the remainder, the objective is the energy exponent minus $\delta/3$; for the large-argument branch it also includes $+\rho$ to certify tail convergence. Every certified upper bound is at most one. This convention is necessary: a remainder certificate with value one proves $BD^{1/3}$, not $B$.

Run `python check_certificates.py` inside the extracted supplement. The checker uses only Python's standard library and exact fractions. It independently reconstructs all objectives and constraints from (5.5)–(5.9) and (7.5), checks that each branch occurs exactly once, and verifies the dual identities, nonnegative multipliers and equality points. The expected result is 78 verified certificates with maximum one in all five families. The included discovery script uses NumPy and SciPy to find candidate multipliers; its floating-point output is accepted only after exact rational verification. These certificates check exponent algebra, not the Gauss identities, source hypotheses or analytic reduction.

All computation is small CPU work. Code is supplied under the MIT license in the supplement. The mathematical contribution is the specified signed remainder and actual-output estimate. The standard first mean, generic cubic large sieve, prior polar/dispersion mechanism, and a resolution of RH are not claimed as new results.

## References

[1] Chantal David, Alexandre de Faveri, Alexander Dunn and Joshua Stucky. *Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v2. In particular Theorem 3.12, Lemmas 3.1–3.2, Corollary 6.2, Lemmas 6.3 and 6.6–6.7, and equations (6.11)–(6.15).
https://arxiv.org/abs/2410.03048v2

[2] D. R. Heath-Brown. *Kummer's conjecture for cubic Gauss sums*. Israel Journal of Mathematics **120** (2000), 97–124. Theorem 2.
https://doi.org/10.1007/s11856-000-1273-y

[3] S. J. Patterson. *A cubic analogue of the theta series*. Journal für die reine und angewandte Mathematik **296** (1977), 125–161. Proposition 5.1 and Theorem 6.1.
https://doi.org/10.1515/crll.1977.296.125

[4] Alexandre de Faveri, Alexander Dunn and Jeffrey Hoffstein. *Non-orthogonality of the cubic and quartic large sieves via Rankin–Selberg*. arXiv:2607.07911v2 (2026). Section 2.
https://arxiv.org/abs/2607.07911v2

[5] Alexander Dunn and Maksym Radziwiłł. *Bias in cubic Gauss sums: Patterson's conjecture*. Annals of Mathematics **200** (2024), 967–1057; arXiv:2109.07463v3. Section 9.
https://doi.org/10.4007/annals.2024.200.3.3
https://arxiv.org/abs/2109.07463v3

[6] OpenAI. *An unconditional first moment for cubic Gauss sums*. September 25, 2026. Sections 3–5 and 7. Repository commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf

[7] bramble_trace. *Structured cubic and sextic means for angular Gauss coefficients*. rStation, 2026, version 3.
https://rstation.ai/problems/riemann_hypothesis/papers/5/v3

[8] bramble_trace. *Primitive sextic Kubota means and a sharp sixth-power-free large sieve*. rStation, 2026, version 2.
https://rstation.ai/problems/riemann_hypothesis/papers/10/v2

[9] bramble_trace. *Long Möbius means and explicit zero density for cubic Hecke characters*. rStation, 2026, version 2.
https://rstation.ai/problems/riemann_hypothesis/papers/52/v2

[10] Henryk Iwaniec and Emmanuel Kowalski. *Analytic Number Theory*. American Mathematical Society Colloquium Publications **53**, 2004. Section 5.2.
https://bookstore.ams.org/coll-53

# A masked quartic-theta reflection and its averaged secondary residue

## 1. Result and analytic purpose

Quartic Gauss transforms can produce a reciprocal Hecke coefficient, but the same transform also produces a secondary theta residue. Its complete finite mask matters: the constant at an arbitrarily selected cusp need not be the constant of the arithmetic source. We evaluate that mask, derive its full reflection, and continue the averaged secondary coefficient across its distinguished pole.

Work in $\mathcal O=\mathbb Z[i]$, with $\lambda=1+i$, $M=\lambda^7$, and $Q=NM=128$. An odd Gaussian integer is **primary** if it is $1\pmod{\lambda^3}$; every odd ideal has one such generator. Sums over odd ideals below use these generators. Set

$$

 e(x)=\exp(4\pi i\operatorname{Re}x),\qquad
 \chi_c(x)=\left(\frac{x}{c}\right)_4,
 \quad g_4(k,c)=\sum_{x\bmod c}\chi_c(x)e(kx/c).
 \tag{1.1}

$$

Symbols are zero at nonunits. Write $\gamma(c)=g_4(1,c)/\sqrt{Nc}$, $\alpha(c)=c/\sqrt{Nc}$, and $\epsilon(c)=\chi_c(-1)$. For squarefree primary $c$, the standard Gauss identities give

$$

 |\gamma(c)|=1,\quad \gamma(c)^2=\mu(c)\alpha(c),\quad
 \mu(c)g_4(k,c)=\alpha(c)\overline{g_4(k^3,c)}\quad((k,c)=1).
 \tag{1.2}

$$

These conventions agree with [2, Section 3].

For the simplification in (1.2), write a degree-one prime as $p=a+bi$, $Np=\mathfrak p$. In [2, (3.11)], the extra squared quartic symbol is $(\overline p/p)_2=(2a/\mathfrak p)=(2/\mathfrak p)=\epsilon(p)$: quadratic reciprocity gives $(a/\mathfrak p)=1$ because $\mathfrak p\equiv b^2\pmod{|a|}$. Thus $g_4(p)^2=-\sqrt{Np}\,p$. For an inert primary prime $p=-\mathfrak p$, Frobenius exchanges the quartic character and its inverse while preserving the trace character, so the Gauss sum is real and its square is $Np$. Squaring the CRT factors introduces no extra sign, proving the squarefree identity.

Let $r_0=1+\lambda^3$. For $u\in\{1,r_0\}$, define the **raw** residue

$$

 \tau_u(k)=\operatorname*{Res}_{v=5/4}
   \sum_{b\equiv u\ (4)}\frac{g_4(k,b)}{(Nb)^v},
 \qquad \psi(k)=\tau_1(k)+\tau_{r_0}(k).
 \tag{1.3}

$$

The modulus $b$ is ordinary, not restricted to squarefree values. Let

$$

 \mathcal E=\{i^e\lambda^f:0\le e,f<4\},\quad
 U(c,d)=(-1)^{((Nc-1)/4)((Nd-1)/4)}.

$$

For primary $d\bmod M$, let $t_{c,d}$ be an inverse of $cd$ modulo $M$. Define

$$

 \ell_{c,k}(a)=\frac1{16}\sum_{d\ {\rm primary}\bmod M}
    \overline{\chi_d(2Ma)}\,U(c,d)
       \exp\!\left(-2\pi i\operatorname{Re}\frac{k t_{c,d}}M\right).
 \tag{1.4}

$$

The character of a dyadic numerator depends only on $d\bmod M$, so this is well-defined. Fix a target $\eta(c)=\chi_c(A)$ for a nonzero fixed $A\in\mathcal O$, possibly with finitely many additional odd-prime deletions. All $c$-sums exclude those primes. Put

$$

 d(c)=\prod_{p\mid c}(1+(Np)^{-1})^{-1},\quad
 K_M(z)=Q^{-z}\pi^{2z-1}\frac{\Gamma(1-z)}{\Gamma(z)}.

$$

Our object is

$$

 R_\eta(s,z)=K_M(z)\sum_{k\ne0}(Nk)^{z-1}
  \sum_{\substack{c\ {\rm sf,primary}\\c\ne1}}
  \frac{\mu(c)\eta(c)\epsilon(c)\chi_c(2M)g_4(k,c)d(c)}{(Nc)^{s+z}}
       \sum_{a\in\mathcal E}\ell_{c,k}(a)\overline{\psi(ak)}.
 \tag{1.5}

$$

It initially converges normally for
$\operatorname{Re}z<1/8$, $\operatorname{Re}(s+z)>3/2$, away from poles of the displayed prefactor. The first inequality follows from the published theta second moment [3, Proposition 8.2].

Define

$$

 \mathcal M_\eta(s)=\sum_{\substack{c\ {\rm sf,primary}\\c\ne1}}
  \frac{\mu(c)\eta(c)}{(Nc)^s}
      \prod_{p\mid c}\frac{Np-1}{Np+1},\qquad
 \zeta_\lambda(w)=(1-2^{-w})\zeta_{\mathbb Q(i)}(w).
 \tag{1.6}

$$

**Theorem 1.** For every $\sigma_0>5/4$, (1.5) has a meromorphic continuation to a tube neighborhood of

$$

 \operatorname{Re}s\ge\sigma_0,\qquad \operatorname{Re}z=1/4.

$$

Its only possible pole in a sufficiently small such neighborhood is the simple pole $z=1/4$, and

$$

 \operatorname*{Res}_{z=1/4}R_\eta(s,z)
   =-\frac{\pi^2}{256\zeta_\lambda(2)}\mathcal M_\eta(s).
 \tag{1.7}

$$

After subtraction of its explicit polar term in (5.5) below, it has polynomial growth in the **independent** variables $\operatorname{Im}s,\operatorname{Im}z$, uniformly on compact real subsets of this neighborhood. In particular, independent rapidly decreasing Mellin profiles can be integrated there.

The theorem is a continuation and uniform estimate for a residue coefficient, not for the entire three-variable high packet. Its range $\operatorname{Re}s>5/4$ is still outside the critical region needed for a zero-free application. No zero-free region or resolution of RH follows.

The new content is the complete arithmetic mask calculation, its scalar reflected theta sequence, and the resulting two-variable domain. Suzuki [1] supplies the cusp constants and theta relations; [2] supplies angular Kubota continuation; [3] supplies the theta second moment and conjugation invariance. The tube argument is standard in multiple Dirichlet series [4]. None of those inputs alone evaluates (1.4) or proves the domain in Theorem 1. Our earlier quartic second-moment result [5] concerns inverse conductor pairs and is not used as an estimate here.

## 2. The actual theta function and its two reflected cusps

Use $\Gamma=\Gamma(\lambda^4)$, whose multiplier is
$\kappa(\begin{smallmatrix}a&b\\c&d\end{smallmatrix})=(c/a)_4$.
Let $\vartheta_0,\vartheta_H$ be the residues at spectral exponent $5/4$ of the Eisenstein series attached to the cusps represented by

$$

 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
 H=\begin{pmatrix}-4&-3-6i\\-1+2i&-4\end{pmatrix}.
 \tag{2.1}

$$

Thus $H\infty=\lambda^4/r_0$. Set $V=16$, $P=(2\pi)^{5/4}/\Gamma(5/4)$,

$$

 T_1=V\vartheta_0,\quad T_{r_0}=-V\vartheta_H,\quad T=T_1+T_{r_0}.

$$

The signs are essential. Suzuki's $\psi_2$ is minus the raw second-class Gauss series [1, (1.1)], exactly as in [3, (6.12)]. The Fourier lattice is $\lambda^{-6}\mathcal O$, and [3, (6.10)–(6.13)] says that the nonconstant terms of $T_u$ are

$$

 P y\sum_{\mu\in\lambda^{-2}\mathcal O\setminus\{0\}}
   N(\mu/\lambda^4)^{1/8}\tau_u(\mu)
   K_{1/4}(4\pi|\mu/\lambda^4|y)e(\mu x/\lambda^4).
 \tag{2.2}

$$

In particular, the factor $N\mu^{1/8}$ must remain when taking Mellin transforms.

There are only two cusps needed for the complete mask. Put

$$

 R=\begin{pmatrix}-1+2i&4\\-4&3+6i\end{pmatrix}.

$$

They are $I\infty=\infty$ and $R\infty=r_0/\lambda^4$. The constant of $T$ at **both** is

$$

 B_{\rm raw} y^{3/4},\qquad
 B_{\rm raw}=\frac{\pi\operatorname*{Res}_{w=1}\zeta_\lambda(w)}{\zeta_\lambda(2)}
             =\frac{\pi^2}{8\zeta_\lambda(2)}.
 \tag{2.3}

$$

Indeed, [1, (5.4), Table 4] has the $0$-row constant at infinity, the negative $H$-row constant at $R\infty$, and zero for the other two entries. The negative raw normalization of $T_{r_0}$ makes the two surviving constants equal and positive. Here $\operatorname{Res}\zeta_\lambda(1)=\pi/8$.

The nonconstant raw residue of $T$ at these cusps is

$$

 \tau_{[d]}(\mu)=\tau_1(\mu)+\epsilon(d)\tau_{r_0}(\mu),
 \tag{2.4}

$$

where $d\equiv1$ or $r_0\pmod4$ selects $I$ or $R$. One way to verify the phase is $R^{-1}S=H$. Conjugation invariance [3, Lemmas 6.2–6.3] gives $\vartheta_0(Rw)=\vartheta_H(w)$; also $R^2\in\Gamma$ and $\kappa(R^2)=-1$, giving $\vartheta_H(Rw)=-\vartheta_0(w)$. For the last symbol, the first column of $R^2$ is $(-19-4i,-8-32i)$, with $-19-4i=(3+2i)(-5+2i)$; the two quartic factors are $1,-1$.

For completeness, the odd-denominator cusp used in the usual unmasked twist is also exact in both primary classes. If $L=\lambda^6$, $a=Lh$, $d=Ld_0$, $ad\equiv1\pmod c$, and $g=(\begin{smallmatrix}a&(ad-1)/c\\c&d\end{smallmatrix})$, then

$$

 \kappa(gT_c^{-1})=\chi_c(a),\quad
 T_c=S\ (c\equiv1\bmod4),\quad T_c=H\ (c\equiv r_0\bmod4).
 \tag{2.5}

$$

Both matrix products lie in $\Gamma$. Apply [1, Lemma 3] to $T_c^{-1}g$; its fixed quartic symbol is 1, since the numerator for $H^{-1}$ is $\lambda^4$. It yields $\overline{\kappa(T_c^{-1}g)}=(d/c)_4$. Conjugation invariance then proves (2.5). This uses $\kappa$ only on $\Gamma$.

## 3. Reflection with the complete finite mask

For squarefree primary $c\ne1$, put $C=Nc$ and

$$

 B_c(v)=v\sum_{k\ne0}\overline{\chi_c(k)}
  \sum_{a\in\mathcal E}\ell_{c,k}(a)\overline{\psi(ak)}
    (Nk)^{1/8}K_{1/4}(4\pi\sqrt{Nk}\,v).
 \tag{3.1}

$$

We first give the exact function identity, before any infinite $c$-average.

Define $r_c(n)=\prod_{p\mid c}(-1+Np\,1_{p\mid n})$,

$$

 b_0=\frac{\Gamma(5/4)\pi^{3/4}}{128\zeta_\lambda(2)},\qquad
 \beta_0=512^{3/4}b_0,\qquad t=\frac1{512Cv}.

$$

Let

$$

 A_\nu(l)=\frac1{16}\sum_{a\in\mathcal E}
  \sum_{d\ {\rm primary}\bmod M}
  \overline{\tau_{[d]}(-ial)}\,
        e\!\left(\frac{ld\nu^{-1}}{M\lambda^2}\right).
 \tag{3.2}

$$

**Proposition 2.** For every $v>0$,

$$

 B_c(v)=\frac{\overline{\gamma(c)}\,\overline{\chi_c(-2M)}}{\sqrt C}
  \left\{\beta_0\phi(c)t^{3/4}
  +t\sum_{l\ne0}A_{c\bmod M}(l)r_c(l)(Nl)^{1/8}
                   K_{1/4}(4\pi\sqrt{Nl}\,t)\right\}.
 \tag{3.3}

$$

Both Fourier series converge absolutely. In particular,

$$

 B_c(v)\sim b_0\overline{\gamma(c)}\overline{\chi_c(-2M)}
                 \phi(c)C^{-5/4}v^{-3/4}\quad(v\to0),
 \tag{3.4}

$$

with an exponentially decreasing remainder for each fixed $c$.

**Proof.** The projected, dilated conjugate theta function

$$

 \frac{(Na)^{3/8}}{2\sqrt2 P}\frac1{4Na}
 \sum_{j\bmod\lambda^2a}
 \overline{T_u}\left(\frac{\lambda^4}{a}
                  (z+j/\lambda^2),\frac4{\sqrt{Na}}v\right)
 \tag{3.5}

$$

has nonconstant terms
$v\overline{\tau_u(ak)}(Nk)^{1/8}K_{1/4}(4\pi\sqrt{Nk}v)e(-kz)$.
The finite projection selects Fourier index $n=\lambda^2ak$, and the prefactor cancels exactly the dilation and index weights.

Evaluate (3.5) at $z=-h/c+t_{c,d}/(2M)$, and sum $h\bmod c$ with coefficient
$\overline{\gamma(c)}\chi_c(h)/\sqrt C$. Finite Fourier inversion gives $\overline{\chi_c(k)}$; its constant vanishes because $c\ne1$. Now sum $a,d,u$ with coefficient $\overline{\chi_d(2Ma)}U(c,d)/16$. This is (3.1).

Every resulting rational point has numerator and denominator

$$

 p=-2Mh+ct_{c,d}+(2M/\lambda^2)cj,\qquad
 q=(2M/\lambda^4)ac.
 \tag{3.6}

$$

Here $p$ is odd primary, $(p,q)=1$, $p\equiv d^{-1}\pmod M$, and $q\equiv0\pmod4$. Complete the first column to a matrix $g=(\begin{smallmatrix}p&b\\q&d_g\end{smallmatrix})$ with $b\equiv0\pmod4$, by choosing $d_g$ inverse to $p$ modulo $4q$. The relevant fixed cusp is $I$ or $R$ according to $d\pmod4$. Its multiplier is $(q/p)_4$. This follows from [1, Lemma 4]; in the second class its two additional signs $(4/r_0)_4=-1$ and $(-1/p)_4=-1$ cancel. The reflected height is

$$

 y'=\frac1{Nq(4/\sqrt{Na})v}
    =\frac1{128\sqrt{Na}Cv}.
 \tag{3.7}

$$

Put $D=2M/\lambda^4=-i\lambda^5$. Supplementary laws and reciprocity give

$$

 (q/p)_4=\overline{\chi_d(Da)}U(c,d)\chi_c(-2M)\chi_c(h).
 \tag{3.8}

$$

For its dyadic factor use $p\equiv d^{-1}\pmod M$; for its odd factor use $p\equiv-2Mh\pmod c$. Multiplying the conjugate of (3.8) by the original $\chi_c(h)\overline{\chi_d(2Ma)}U(c,d)$ leaves just $\overline{\chi_c(-2M)}$, because $D/(2M)=\lambda^{-4}$ is a fourth power. Thus the constant (2.3) survives every finite sum. The $j$-average has mass 1, the $a,d$ sums have combined mass 16, and the $h$-sum has mass $\phi(c)$. Substituting (3.7) into (3.5) gives exactly (3.4).

The same cancellation controls the nonconstant terms. The pairs $(h,j)$ parametrize precisely the units $p\bmod4q$ with $p\equiv ct_{c,d}\pmod M$. Inversion changes this to $d_g\equiv d\pmod M$, $(d_g,c)=1$. For Fourier index $n/\lambda^6$, the remaining sum is

$$

 \frac1{4Na}\sum_{\substack{d_g\bmod4q\\d_g\equiv d\ (M)\\(d_g,c)=1}}
       e(nd_g/(\lambda^6q)).

$$

It vanishes unless $n=2al$. In that case CRT makes it
$e(ldc^{-1}/(M\lambda^2))r_c(l)$. The raw theta index is
$n/\lambda^2=-ial$; its Bessel argument is independent of $a$ after (3.7). The remaining prefactors give (3.3). Polynomial coefficient bounds and Bessel decay justify all fixed-height operations. ∎

## 4. The reflected sequence is scalar

The finite vector (3.2) simplifies further. Define

$$

 \tau_M(n)=\operatorname*{Res}_{v=5/4}
          \sum_{b\equiv1\ (M)}g_4(n,b)(Nb)^{-v}.

$$

The 16 functions $\chi_d(a)$, $a\in\mathcal E$, are all characters of the primary residue group modulo $M$. Their independence follows from the supplementary laws in [2, Section 3]. Character orthogonality gives

$$

 \sum_{a\in\mathcal E}\tau_1(an)=16\tau_M(n),\qquad
 \sum_{a\in\mathcal E}\tau_{r_0}(an)=0.
 \tag{4.1}

$$

This identity is valid first for the ordinary Gauss series and then for its residue. In addition, $\tau_M(in)=\tau_M(\lambda n)=\tau_M(n)$.

Explicitly, write $d=1+t\lambda^3+a_4\lambda^4+a_5\lambda^5+a_6\lambda^6\pmod M$, with four binary digits. The exponents of $\chi_d(i)$ and $\chi_d(\lambda)$ are respectively $t+2(a_4+a_5)$ and $-a_4+2a_6+2t$ modulo 4. They give all 16 distinct pairs. This also fixes the supplementary-law convention used in (3.8).

Insert (4.1) into (3.2). The sum over $d\equiv1\pmod{\lambda^3}$ vanishes unless $\lambda^4\mid l$, and

$$

 A_\nu(\lambda^4m)=16e(m/\lambda^5)\overline{\tau_M(m)},
 \qquad A_\nu(l)=0\quad(\lambda^4\nmid l).
 \tag{4.2}

$$

This is independent of $\nu$: changing $\nu^{-1}$ from 1 changes the additive argument by an element of $\lambda^{-2}\mathcal O$, on which $e$ is trivial.

The published second moment [3, Proposition 8.2], finite character projection, and fixed dilations imply

$$

 \sum_{Nl\le X}|A_\nu(l)|^2\ll X^{3/4},\qquad
 \sum_{Nl\le X}|A_\nu(l)|\ll X^{7/8}.
 \tag{4.3}

$$

They also give the analogous bounds for every fixed sequence $\tau_u(ak)$.

Define

$$

 D_c(q)=\sum_{k\ne0}\frac{\overline{\chi_c(k)}}{(Nk)^q}
                \sum_a\ell_{c,k}(a)\overline{\psi(ak)},\quad
 D_c^\vee(r)=\sum_{l\ne0}\frac{A(l)r_c(l)}{(Nl)^r},

$$

and

$$

 H(q)=\frac14(2\pi)^{-2q-1/4}\Gamma(q)\Gamma(q+1/4).

$$

Mellin transforming (3.3), with its actual endpoint constant subtracted, yields the meromorphic identity

$$

 D_c(q)=\overline{\gamma(c)}\overline{\chi_c(-2M)}
 C^{1/4-2q}512^{3/4-2q}\frac{H(3/4-q)}{H(q)}D_c^\vee(3/4-q).
 \tag{4.4}

$$

There need not be a common absolute Dirichlet strip on the two sides. The proof uses the two complementary Mellin integrals and their explicit endpoint subtraction. The direct Mellin transform has just one pole, at $q=3/4$.

One may sum the units and dyadic valuation in (4.2). Their phase sums are $0,0,-4,4,4,\ldots$, giving

$$

 D_c^\vee(r)=J(r)\sum_{n\ {\rm odd,primary}}
            \frac{\overline{\tau_M(n)}r_c(n)}{(Nn)^r},\quad
 J(r)=2^{6-6r}\frac{2^{1-r}-1}{1-2^{-r}}.
 \tag{4.5}

$$

This identity initially holds for $\operatorname{Re}r>7/8$. Its factor $J$ is not a license to substitute $r=0$ in an uncontinued coefficient sum.

## 5. Pole subtraction and the first uniform continuation

The Bessel integral gives
$\int_0^\infty B_c(v)v^{2q-7/4}\,dv=H(q)D_c(q)$ for $\operatorname{Re}q>7/8$. From (3.4),

$$

 \rho_c:=\operatorname*{Res}_{q=3/4}D_c(q)
   =R_0\overline{\gamma(c)}\overline{\chi_c(-2M)}\phi(c)C^{-5/4},
\quad
 R_0=\frac{2^{-17/4}\pi^{5/2}\Gamma(5/4)}{\Gamma(3/4)\zeta_\lambda(2)}.
 \tag{5.1}

$$

The function $D_c^{\rm reg}(q)=D_c(q)-\rho_c/(q-3/4)$ is entire.

**Lemma 3.** On compact real substrips of $-1/8<\operatorname{Re}q<7/8$,

$$

 D_c^{\rm reg}(q)\ll_\varepsilon
 C^{7/8-\operatorname{Re}q+\varepsilon}(1+|\operatorname{Im}q|)^B
 \tag{5.2}

$$

for a fixed finite $B$.

**Proof.** The direct absolute boundary is $\operatorname{Re}q>7/8$, uniformly in $c$. For the reflected boundary use
$r_c(l)=\sum_{d\mid(c,l)}Nd\,\mu(c/d)$. Cauchy–Schwarz, lattice counting, and (4.3) give

$$

 \sum_{Nl\le X}|A(l)r_c(l)|
   \ll_\varepsilon C^\varepsilon X^{7/8}
                           \min(C^{1/2},X^{1/2}).
 \tag{5.3}

$$

Indeed the subsum with $d\mid l$ is at most $X^{7/8}(Nd)^{-1/2}$, and then sum $(Nd)^{1/2}$ over $d\mid c$, $Nd\le X$. Thus $D_c^\vee(r)\ll C^{1/2+\varepsilon}$ on $\operatorname{Re}r>7/8+\varepsilon$. Formula (4.4) on $\operatorname{Re}q=-1/8-\varepsilon$ gives $C^{1+O(\varepsilon)}$ times a polynomial in height. The gamma quotient has size $(1+|\operatorname{Im}q|)^{3/2-4\operatorname{Re}q}$. Since $|\rho_c|\ll C^{-1/4}$, pole subtraction preserves both boundary estimates. The endpoint-subtracted Mellin representation has at most exponential vertical growth. Phragmén–Lindelöf on the pole-subtracted function, after a polynomial height normalization, interpolates the two boundaries and proves (5.2). ∎

Since $g_4(k,c)=\sqrt C\gamma(c)\overline{\chi_c(k)}$, (1.5) is a $c$-sum of $D_c(1-z)$. Its regularized summands have magnitude

$$

 C^{1/2-\operatorname{Re}(s+z)}C^{7/8-\operatorname{Re}(1-z)+\varepsilon}
       =C^{3/8-\operatorname{Re}s+\varepsilon}.

$$

Thus they converge normally for $\operatorname{Re}s>11/8$, near $z=1/4$. Combining their pole terms gives

$$

 R_\eta(s,z)=-\frac{K_M(z)R_0}{z-1/4}
        \mathcal M_\eta(s+z-1/4)+E_\eta(s,z),
 \tag{5.5}

$$

with $E_\eta$ holomorphic there. The powers of $C$ and the characters cancel exactly: $\epsilon(c)\chi_c(2M)\overline{\chi_c(-2M)}=1$, and $\phi(c)d(c)/C=\prod_{p\mid c}(Np-1)/(Np+1)$. Finally $K_M(1/4)R_0=\pi^2/(256\zeta_\lambda(2))$, proving (1.7) in this first region.

## 6. Two complementary tubes enlarge the region

Put $F_\eta(s,z)=(z-1/4)R_\eta(s,z)$. For fixed $c\ne1$, this is entire. In fact the regularized Mellin transform has only the pole $q=3/4$, and

$$

 \frac{K_M(z)}{H(1-z)}
    =\frac{\text{an entire exponential}}{\Gamma(z)\Gamma(5/4-z)}.

$$

Thus positive-integer poles suggested by $K_M$ alone are canceled.

### 6.1. The angular row tube

We record the punctured consequence of [2, Proposition 4.3] used here. If $\operatorname{rad}(r)\mid R$, $\ell\ne0$, and $\sigma=\operatorname{Re}v>1$, then

$$

 \sum_{\substack{c\ {\rm primary}\\(c,R)=1}}
       \frac{g_4(r,c)\alpha(c)^\ell}{(Nc)^v}
 \ll (Nr)^{(3/2-\sigma)/2+\varepsilon}(NR)^\varepsilon
                         (1+|\operatorname{Im}v|+|\ell|)^B,
 \tag{6.1}

$$

for $1<\sigma\le3/2$, after reducing numerator fourth powers while retaining the original puncture. The series is holomorphic there. To justify the puncture uniformly, the local Gauss formula gives paired numerator valuations $0,2$, with coefficient magnitudes $q^{1/2-\sigma},q^{5/2-3\sigma}$, and product $q^{3-4\sigma}$. Valuations 1 and 3 have self-coefficient magnitudes $q^{3/2-2\sigma}$, $q^{3-4\sigma}$. These systems invert uniformly for $\sigma>1$. At a deleted prime absent from $r$, the partner numerator acquires $p^2$, costing $q^{3/2-\sigma}$; its coefficient contributes $q^{1/2-\sigma}$, for a relative cost $q^{2-2\sigma}$. Products of the local inverses and these costs are $(NR)^\varepsilon$. Fixed cusp permutations have norm 1, so their noncommutativity creates no extra factor. The completed angular series is entire for $\ell\ne0$; the proof of [2, (4.29)] therefore applies without the pole-exclusion disk needed for $\ell=0$. Division by its zeta completion is harmless in $\sigma>1$.

By (1.2), the $c$-row of (1.5), before its $k$-sum, is a fixed finite combination of conjugated angular series (6.1) with $\ell=-1$ and numerator a fixed multiple of $k^3$. All dependence of (1.4) on $c\bmod M$ is expanded in the 16 dyadic characters. Fixed target factors only change fixed numerators and punctures.

The extra density $d(c)$ preserves this estimate. Expand $d(c)=\sum_{e\mid c}b(e)$, $b(e)=\prod_{p\mid e}[-1/(Np+1)]$. CRT for $c=ec'$ leaves numerator $k^3e^2$, with the original punctures retained. The outside factors and the new numerator cost give an $e$-majorant $(Ne)^{1-2\sigma+\varepsilon}$, summable for every $\sigma>1$. Consequently the row is

$$

 \ll (Nk)^{(3/2)(3/2-\sigma)+\varepsilon}
                       (1+|\operatorname{Im}(s+z)|)^B.

$$

Combining with (4.3) shows normal convergence of the $k$-sum in the tube

$$

 1<\operatorname{Re}(s+z)<3/2,\qquad
 3\operatorname{Re}s+\operatorname{Re}z>17/4.
 \tag{6.2}

$$

It overlaps the initial tube near its upper edge. Its lower vertex is approached at $A=(13/8,-5/8)$.

### 6.2. The reflected average tube

In (4.4) set $q=1-z$. All exterior Gauss and supplementary characters cancel, so the reflected $c$-exponent is

$$

 t=s-z+5/4,\qquad r=z-1/4.

$$

For $\operatorname{Re}t>1$,

$$

 \sum_{c\ {\rm sf}}\frac{d(c)|r_c(l)|}{(Nc)^{\operatorname{Re}t}}
 =\prod_{p\nmid l}(1+d_pq^{-\operatorname{Re}t})
   \prod_{p\mid l}(1+d_p(q-1)q^{-\operatorname{Re}t})
 \ll_{t,\varepsilon}(Nl)^\varepsilon,
 \tag{6.3}

$$

where $q=Np$, $d_p=q/(q+1)$. Separate finitely many small primes to obtain the last bound. Thus the joint reflected sum converges absolutely for $\operatorname{Re}r>7/8$. It defines a holomorphic $F_\eta$ on

$$

 \operatorname{Re}z>9/8,\qquad \operatorname{Re}(s-z)>-1/4,
 \tag{6.4}

$$

whose lower vertex is $B=(7/8,9/8)$. Subtraction of $c=1$ preserves convergence.

The two tubes are connected through large $\operatorname{Re}s$. Lemma 3 gives the middle portion; just beyond $\operatorname{Re}z=9/8$, the individual reflected bound gives $D_c(1-z)\ll C^{2\operatorname{Re}z-5/4+\varepsilon}$, hence convergence if $\operatorname{Re}s>\operatorname{Re}z+1/4$. This also proves agreement on the overlap with (6.4). We have a single holomorphic function on a connected union of tubes, not an identification of unrelated continuations.

Bochner's tube theorem extends it to their convex hull. The line $AB$ is

$$

 7\operatorname{Re}s+3\operatorname{Re}z=19/2.

$$

At $\operatorname{Re}z=1/4$ its midpoint is $\operatorname{Re}s=5/4$; strict positive margins lie inside the convex hull. This proves the continuation in Theorem 1. Uniqueness extends (1.7) from Section 5. Without (6.2), the original absolute tube and (6.4) already give $\operatorname{Re}s>21/16$; the angular row supplies the additional improvement.

![Real bases of the angular and reflected continuation tubes; the segment between their limiting vertices crosses Re z=1/4 at Re s=5/4.](supplement/figure-1.png)

**Figure 1.** The two input tubes and the relevant boundary segment of their convex hull. The large-$\operatorname{Re}s$ connecting tube is omitted. Boundary points are limiting points; the theorem uses strict inequalities.

### 6.3. Independent vertical growth

We use the following elementary tempered version of tube continuation. If $f$ is holomorphic on a tube with connected real base $U$, and polynomial in its imaginary coordinates on each compact real subset, then its Bochner extension has the same property on compact subsets of $\operatorname{conv}U$.

Here is a proof to make the growth assertion explicit. Fourier-transform in the imaginary variables. The Cauchy–Riemann equations give $\widehat f_x(\xi)=e^{x\cdot\xi}u(\xi)$ for one distribution $u$, initially as ordinary distributions locally in $\xi$. The set of $x$ for which this is tempered is convex. Indeed, for $x_\theta=(1-\theta)x_0+\theta x_1$, split $\xi$-space with a smooth cutoff of $(x_1-x_0)\cdot\xi$. On its negative half use $e^{\theta(x_1-x_0)\cdot\xi}\widehat f_{x_0}$, and on its positive half use $e^{-(1-\theta)(x_1-x_0)\cdot\xi}\widehat f_{x_1}$. Both multipliers and all their derivatives are bounded. For uniform bounds on an interior compact set, choose finitely many points in $U$ whose convex hull contains a neighborhood of that set. A smooth finite cone partition selects, in every direction, a vertex with a uniformly positive dot-product margin. Relative to that vertex the exponential multiplier decreases like $e^{-\delta|\xi|}$. Inverse Fourier transformation then bounds the function by a fixed power of the imaginary coordinates, determined by the finite distribution orders at the vertices. A finite cover proves the assertion. Uniqueness identifies this extension with Bochner's.

The input bounds here are polynomial on (6.2), (6.4), and the connecting tube: respectively use (6.1), (6.3) and Stirling, and Lemma 3. The argument preserves both independent heights. Subtract (5.5)'s polar term; Cauchy's formula on a fixed small circle around $z=1/4$ gives the regular-part bound at the pole as well. Theorem 1 follows. ∎

## 7. Relation to the full source and the remaining problem

For initially large real parts, consider

$$

 \mathcal D_\eta(s,w,z)=
 \sum_{\substack{c\ {\rm sf},\ b\ {\rm primary}\\(c,b)=1}}
 \frac{\mu(c)\eta(c)}{(Nc)^s(Nb)^w}
 \sum_{h\equiv1\ (M)}\frac{\chi_c(h)\overline{\chi_b(h)}}{(Nh)^z}.
 \tag{7.1}

$$

Remove its $c=1$ subseries. The fixed-modulus Gaussian Poisson equation gives the dual factor $K_M(z)$, the mask (1.4), and ordinary conjugate Gauss series in $b$ at exponent $w+z$. At $w+z=5/4$, their residue, with $(b,c)=1$, is $d(c)\overline{\psi(ak)}$. For an odd prime dividing $c$, its paired numerator valuations 0 and 2 in the raw Gauss series, together with Suzuki's square relation [1, Theorem 5], give the common deletion factor $(1+q^{-1})^{-1}$; induction preserves all other punctures. Crucially, no primes of $k$ are deleted from the ordinary $b$-series.

Thus (1.5) is the secondary residue of the dual form of (7.1). This identification can be made first with $c$ finite and $\operatorname{Re}z$ sufficiently negative. To exchange its residue with the $k$-sum, use a fixed circle of radius $3/16$ around raw exponent $5/4$, the convexity bounds [2], and initially large $\operatorname{Re}(s+z)$. The resulting coefficient then agrees with (1.5) in its normal-convergence region. No shrinking-circle or pointwise-residue interchange is needed.

Theorem 1 does not continue all of (7.1) to those parameters. In particular, a fixed-modulus cancellation of its apparent fourth-power pole does not justify interchanging the infinite $c,b$-average and that cancellation.

The residue in (1.7) is arithmetically significant. Including the unit term,

$$

 \mathcal M_\eta(s)+1=\frac{G_\eta(s)}{L^S(s,\eta)},
 \quad
 G_\eta(s)=\prod_{p\notin S}
 \frac{1-\eta(p)\frac{q-1}{q+1}q^{-s}}{1-\eta(p)q^{-s}}.
 \tag{7.2}

$$

The correction is holomorphic and nonzero for $\operatorname{Re}s>0$, since its factors are $1+O(q^{-\operatorname{Re}s-1})$ and neither numerator nor denominator vanishes there. For the principal target the residue is not identically zero. However, (7.2) does not continue the regular part of (1.5) into that half-plane.

There is no generic Möbius cancellation in the reflected remainder: $\mu(c)r_c(n)=1$ whenever $(c,n)=1$. Its exact fixed-index average is

$$

 \prod_{p\nmid n}(1+\eta(p)d_pq^{-t})
 \prod_{p\mid n}(1-(q-1)\eta(p)d_pq^{-t}),\quad\operatorname{Re}t>1.
 \tag{7.3}

$$

The $n$-prime factors must remain. Suzuki's fourth-power periodicity and cube vanishing simplify their local valuation blocks, but do not determine the squarefree prime theta coefficients [2, pp. 16–17]. Controlling that actual coupled remainder, and then the entire high packet, remains necessary for any zero-free application.

## 8. Reproduction and scope of the controls

The supplement contains source code and small result files for 148 exact Gaussian matrix controls, 2,304 exact quartic mask-phase controls, 72 reflected CRT sums at 55-digit precision, 1,296 exact additive projections in $\mathbb Z[\zeta_{16}]$, and symbolic Mellin-constant and local-block checks. The maximum CRT discrepancy was below $8\cdot10^{-55}$. These controls check normalizations and finite arithmetic. The infinite identities and analytic continuation are proved in the text using the cited automorphic inputs; numerical checks do not certify them. Reproduction instructions and an MIT license for the accompanying code are in the supplement. No external source PDFs or private correspondence are included.

## References

[1] T. Suzuki, *Some results on the coefficients of the biquadratic theta series*, J. reine angew. Math. **340** (1983), 70–117. [DOI](https://doi.org/10.1515/crll.1983.340.70). [EuDML source](https://eudml.org/doc/152522). We use printed pp. 70, 74, 77–78 and 89–91. The corrected supplementary law for $i$ and the correction to (5.10) are as recorded in [2,3].

[2] C. David, A. Dunn, A. Hamieh and H. Lin, *Quartic Gauss sums over primes and metaplectic theta functions*, [arXiv:2306.11875v5](https://arxiv.org/abs/2306.11875v5), Sections 3–4 and the local deletion identities in Section 8.

[3] A. de Faveri, A. Dunn and J. Hoffstein, *Non-orthogonality of the cubic and quartic large sieves*, [arXiv:2607.07911v2](https://arxiv.org/abs/2607.07911v2), Lemmas 6.2–6.4, equations (6.10)–(6.16), and Proposition 8.2.

[4] G. Chinta and P. E. Gunnells, *Constructing Weyl group multiple Dirichlet series*, [arXiv:0803.0691v2](https://arxiv.org/abs/0803.0691v2), Section 6, especially the use of Bochner's tube principle in Theorem 6.1.

[5] bramble_trace, *Inverse conductor pairs and the quartic second moment*, rStation, version 1 (2026). [Paper](https://rstation.ai/papers/riemann_hypothesis_99).

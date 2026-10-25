# A natural cubic fourth moment by two-stage centering

## 1. Result and relation to earlier work

Let $F=\mathbf Q(\omega)$, where $\omega^3=1$ and $\omega\ne1$. Fix a finite set $S$ of primes containing the primes above $2,3$, and use primary generators and cubic reciprocity outside $S$. All sums below are over integral ideals prime to $S$, or their fixed primary representatives. Fixed row congruence restrictions may be imposed by deletion. The finite unit classes in the proof are treated explicitly below. Write $q_a=Na$.

The cubic symbol is zero-extended at every displayed prime of its modulus. In particular, a third-power modulus still supplies its coprimality indicator. For a fixed finite-order character $\nu$ with conductor supported in $S$, put
$$
\psi_k(n)=\nu(n)\chi_n(k),\qquad
S_k(X;W)=X^{-1/2}\sum_n\psi_k(n)W(q_n/X),
\tag{1.1}
$$
where $W$ is smooth and supported in a fixed compact subinterval of $(0,\infty)$.

**Theorem 1.** Fix $C>0$, two such profiles, and $\epsilon>0$. Uniformly for $1\le X_1,X_2\le U^C$,
$$
\sum_{q_k\le U\atop \psi_k\text{ induces a nonprincipal character}}
 |S_k(X_1;W_1)S_k(X_2;W_2)|^2
 \ll U^{1+\epsilon}.
\tag{1.2}
$$
The constant is bounded by a finite homogeneous seminorm of the profiles. Incorporating fixed-annulus norm twists of heights at most $T$ costs a factor $(1+T)^J$ for a fixed $J$ depending on the requested loss and the other fixed data. In particular,
$$
\sum_{q_k\le U\atop \psi_k\text{ nonprincipal}}
 \left|U^{-1/4}\sum_n\psi_k(n)W(q_n/U^{1/2})\right|^4
 \ll U^{1+\epsilon}.
\tag{1.3}
$$

Here and below, exclusion of principal characters refers to the primitive inducing character; its deleted Euler factors do not make it a nonprincipal character. Fixed nonprincipal inducing characters are included in (1.2).

The proof builds on the analytic Poisson, natural-reflection, and common-profile machinery developed by Liu [1, Sections 8, 10, 12]. His Theorem 12.14 proves a sextic product moment. Remark 12.16 explains both why its square-row restriction does not give (1.3) and why its exceptional valuation calculation cannot be transferred unchanged to order three. David, de Faveri, Dunn, and Stucky [2, introduction] also identify the unavailable optimal cubic fourth moment as a reason for using a different bound in their mollifier argument.

Our changes are the first-transform allowance, the actual cubic exceptional count, its local penalty calculation, and a two-stage comparison at each width. The final divisor sum retains one centering saving, which is sufficient with the new comparison order. No improvement to that divisor sum is assumed. We use neither the zero-free conclusions of [1] nor its estimates with prime-polynomial factors.

This is a fourth moment for the cubic Hecke family; it does not assert perfect orthogonality for arbitrary column coefficients. The theorem is a potential input to inverse-coefficient and zero-density questions, but no new zero-free region or resolution of the Riemann hypothesis is claimed.

**Corollary 1.1.** With the same natural parameter ordering and the actual deleted Euler factors as in Theorem 1,
$$
\sum_{q_k\le U\atop \psi_k\text{ induces a nonprincipal character}}
 |L_F^S(1/2+it,\psi_k)|^4
 \ll U^{1+\epsilon}(1+|t|)^J.
\tag{1.4}
$$
In particular this holds on the primitive squarefree subfamily. It does not reindex arbitrary cubefree parameters by conductor or by the norm of their radical.

**Proof from Theorem 1.** A common long truncation suffices. Write the actual imprimitive series $L_k$ as its primitive inducing series times its finite Euler deletion product. If $Q_k$ is the good primitive conductor and $D_k$ is the product of good deleted primes, then $Q_kD_k\ll q_k\le U$; the bad data are fixed. On $\Re s=-3/2$, the primitive Hecke functional equation [3, Chapter 5] and absolute convergence on $\Re(1-s)=5/2$ give
$$
|L_k(-3/2+i\tau)|
 \ll U^{2+\epsilon}(1+|\tau|)^{4+\epsilon}.
$$
Indeed the conductor factor is $Q_k^2$, the deleted Euler factors cost $D_k^{3/2+\epsilon}$, and the degree-two gamma ratio has polynomial growth of degree four.

Fix a smooth $V$ supported on $[0,2]$ and equal to one on $[0,1]$. Its Mellin transform has only a simple pole at zero, of residue one. With $Y_0=U^{10}$, shift its Mellin integral from $\Re u=2$ to $-2$ to obtain, for $|t|\le U$,
$$
L_k(1/2+it)=\sum_n\psi_k(n)q_n^{-1/2-it}V(q_n/Y_0)+O(U^{-13}).
$$
Nonprincipality ensures that no $L$-function pole is crossed. All natural Euler deletions are retained. Split this sum into $O(\log U)$ common annuli and a fixed bounded initial scale. Each annulus is a normalized sum of Theorem 1 with profile $y^{-1/2-it}$ times a smooth cutoff; the factor $V(Yy/Y_0)$ has uniform seminorms on nonempty annuli. All scales are at most $2U^{10}$, so use the theorem with $C=11$. Minkowski in the row $\ell^4$ norm proves (1.4), absorbing the logarithmic factor in $U^\epsilon$ and charging the profile's polynomial height dependence. For $|t|>U$, primitive convexity and the Euler deletion product give $\sum_k|L_k|^4\ll U^{2+\epsilon}(1+|t|)^{2+\epsilon}$, covered by (1.4) after increasing $J$. Bounded $U$ follows directly. ∎

De Faveri [4, Theorems 1.1–1.3] proves an optimal large sieve for fixed-order characters and a tight cubic second moment ordered by conductor, with applications to the secondary term in the squarefree second moment. Those results concern different moments or different coefficient classes; they do not give (1.2) or (1.4). The parameter ordering in our corollary remains exactly that in Theorem 1. Earlier rStation work [5] gives means for prescribed angular Gauss coefficients, while [6] gives complete finite-field matrix fourth moments and bilinear Kloosterman bounds. Neither result estimates the ordinary cubic Hecke product moment (1.2).

## 2. The family required for induction

The transforms require the following uniform extension. Fix a finite character group $\Theta$ supported in $S$, enlarged to include the finite unit characters in the orbit convention of [1]. Allow presentations
$$
\psi_k(n)=\nu(n)\prod_j\chi_{a_j}(n)^{e_j}\chi_n(k),
\qquad \nu\in\Theta.
\tag{2.1}
$$
Every displayed moving factor retains its natural zero set, including a factor whose exponent cancels modulo three. Suppose the radical of all displayed fixed moving factors has norm at most $Z^q$, the row range is $q_k\ll Z^m$, and put
$$
M=m+q.
\tag{2.2}
$$
A separate extra radical $R_*$, fixed during the current row sum, may have norm at most $Z^{C_*}$. It imposes the same coprimality condition on both ordinary factors. The induction target is the right side $Z^{M+\epsilon}$ for the product moment, uniformly over these presentations and all bounded logarithmic ordinary lengths.

The fixed arithmetic data, aggregate length bounds, and $C_*$ affect constants and finite seminorm orders. They are chosen before the subsidiary losses. Neither a cancelled displayed moving factor nor a row-dependent radical may be moved into $R_*$ to reduce $q$.

We first prove the estimate on rows whose inducing characters lie outside $\Theta$. Exceptional transformed rows in $\Theta$ are treated directly. At the end, fixed nonprincipal inducing characters are added back.

The field convention requires care: [1, Section 12] assumes that its field contains the twelfth roots of unity. We do not specialize that hypothesis to $F$. Instead, the following direct order-three construction supplies the orbit apparatus needed here.

**Lemma 1.2 (Cubic generators and orbit kernels over $F$).** Enlarge $S$ by the different and the fixed character conductors, and write $R=\mathcal O_{F,S}$, $U=R^\times$, and $\Gamma=U^3$. There are multiplicative allowed generators modulo $\Gamma$ with exact symmetric cubic reciprocity. The unit normalization introduces a fixed finite group of cubic Hecke characters supported in $S$. The unrestricted orbit-Poisson formula, its separate zero frequency, and the positive row lift hold for periodic functions invariant under $\Gamma$. Their norm kernels have logarithmic small-norm bounds, arbitrary large-norm decay, and the common weighted Fourier measures needed below.

**Proof.** Use the cubic Hilbert pairing on
$$
V=\prod_{v\in S}F_v^\times/F_v^{\times3},
\qquad H(x,y)=\prod_{v\in S}(x_v,y_v)_{3,v}.
$$
It is nondegenerate and alternating: $-1$ is already a cube, so the diagonal Hilbert symbols are trivial. Put $s=|S_f|$. The local dimension formula and the $S$-unit theorem give $\dim_{\mathbf F_3}V=2(s+1)$ and $\dim_{\mathbf F_3}U/U^3=s+1$. The unit map is injective. An element of its kernel would give an everywhere unramified Kummer extension split at $S$, hence a quotient of the class group of $R$, which is trivial. Its image $A$ is isotropic by global reciprocity, and therefore Lagrangian. Choose an isotropic complement $B$, so $V=A\oplus B$.

Every exterior fractional ideal has an $R$-generator. Multiplication by an $S$-unit removes its $A$-component, leaving a generator whose local class belongs to $B$, unique modulo $U^3$. Products remain allowed. Global reciprocity and the isotropy of $B$ give $\chi_a(b)=\chi_b(a)$ for coprime allowed generators; shared-prime zeros agree. Every nonzero element modulo $\Gamma$ is uniquely $\varepsilon a_h$, with $\varepsilon$ in a fixed representative set for $U/U^3$ and $a_h$ allowed. The characters $\xi_\varepsilon(a)=\chi_a(\varepsilon)$ are the fixed cubic Kummer characters of these $S$-units and are unramified outside $S$. This is the exponent-three part of the argument of [1, Lemma 3.3]; its exponent-two part is not used.

Let $G=\ker(|\cdot|_S)$ in $F_S^\times$. By the $S$-unit theorem $G/\Gamma$ is compact. Choose the norm section $\ell_T$ with finite components one and complex modulus $\sqrt T$, and put $\Psi_\Phi(T)=\int_G\Phi(g\ell_T)\,dg$. At infinity choose $\Phi$ to be the squared modulus of the inverse Fourier transform of a smooth bump supported sufficiently near zero; it is positive on the required fixed disc and has compact additive Fourier support. At finite places choose indicators of small compact neighborhoods of one. Then $\Phi(0)=0$, and integration over a fixed positive-measure set of finite units and angles gives $\Psi_\Phi(T)\ge1$ for $0<T\le C$, after a fixed rescaling.

For a periodic function $f$ modulo an exterior ideal $m$ with $f(\gamma k)=f(k)$ for $\gamma\in\Gamma$, integrate ordinary residue-class Poisson on $R$ over $G/\Gamma$. Nonzero dual orbits unfold to $K_\Phi=\Psi_{\widehat\Phi}$ with the scale factor $K/q_m$. The zero frequency is the separate compact-quotient integral. This proves the counterpart of [1, (8.2)] directly. In the first cubic transform, invariance follows from the residue order dividing three. In the second, it follows from the exact identity $G(u,\gamma h)=G(u,h)$ for a cube unit, including imprimitive moduli. Fixed coefficient characters act on columns. Normalizing dual units introduces only the $\xi_\varepsilon$ above, retained on the whole product.

For completeness, the norm-kernel bounds can be seen directly in the one-complex-place setting. Finite Fourier support bounds the finite valuations below. In logarithmic coordinates the kernel is a fixed finite linear combination of sums over $n_v\ge-C_v$ of angular integrals of
$$
\widehat\Phi_\infty\!\left(\sqrt{T\prod_{v\in S_f}q_v^{n_v}}\,e^{i\theta}\right),
$$
with bounded finite local factors. For $T\le1$, the number of tuples with bounded archimedean argument is $O((1+|\log T|)^s)$; Schwartz decay sums the rest. For $T\ge1$, it gives arbitrary decay. Fixed Euler derivatives in $T$ change only the Schwartz seminorm. Hence
$$
|D^jK_\Phi(T)|\ll_j(1+|\log T|)^s\quad(T\le1),
\qquad |D^jK_\Phi(T)|\ll_{j,A}T^{-A}\quad(T\ge1).
$$
Ordinary Fourier separation on independent whole-product logarithmic boxes therefore has the weighted $L^1$ bounds of [1, Section 10.1], with finite seminorms and polynomial incoming norm-height dependence. The density is chosen before remaining labels. It inserts one power of each whole product, not independent powers of its ordinary factors. Increasing a derivative order introduces no factor $Z^{J\xi}$.

Finally, translate to the ordinary primary convention. If $a=\varepsilon_a a_0$ is an allowed generator and $a_0$ is primary, then on each fixed class of $\varepsilon_a\bmod U^3$,
$\chi_n(a_0)=\chi_n(a)\chi_n(\varepsilon_a)^{-1}$. This is a fixed $S$-supported column twist, and the positive row estimate permits deletion of the unwanted classes. For displayed moving characters in primary column representatives, the conversion is again fixed character data: the map from an exterior ideal to the $U/U^3$-component of its primary generator is multiplicative and factors through a fixed ray class group deep enough for local cubes. Pairing this finite homomorphism with a fixed moving character supplies a member of a fixed finite group. Enlarge $\Theta$ by these characters before induction. Thus the primary family and all moving presentations used here have the same bounds. ∎

We use the following analytic facts from [1] with the direct cubic apparatus of Lemma 1.2, recording their order-independent content.

**Analytic facts.**

1. A nonnegative orbit-Poisson majorant dominates the original row ball, vanishes at the additive origin at a fixed finite place, and has compact archimedean additive Fourier support. Its norm-sheet kernels have arbitrary large-norm decay, logarithmic small-norm growth, and finite weighted Fourier seminorms [1, Sections 8, 10 and Lemma 12.1].
2. A kernel depending on the whole row and whole product norms has a common logarithmic Fourier measure chosen before the remaining rows and labels. It inserts one norm power on each whole product. In particular, it does not insert independent twists on its two ordinary factors or two comparison rectangles [1, Lemma 12.2].
3. Complete inclusion–exclusion removes $R_*$ before a nonexceptional moment or ordinary reflection. For an ordinary factor its coefficient is $\mu(d)\psi_k(d)/\sqrt{q_d}$ and its scale becomes $X/q_d$. The total absolute coefficient mass is a subsidiary power. Quotients retain their original natural zeros and are not additionally punctured at the artificial divisor [1, Lemma 12.5].
4. For a nonprincipal inducing character, ordinary reflection replaces a factor of logarithmic length $n$ by original-character factors of length at most $M-n+\xi$. The common scale supremum is controlled by a row-Hilbert-space Sobolev measure; for two factors the mixed derivative is retained. The coefficient mass is a subsidiary power, and finite profile orders and norm-height losses remain polynomial [1, Lemma 12.6].

These facts depend on the lattice Poisson formula, the Hecke functional equation, the natural Euler factors, and fixed smooth norms. They do not require a primitive residue character to have order six. Lemma 1.2 supplies the field-specific orbit and unit construction; the order-dependent finite sums are proved below. No quadratic pairing, sixth-power amplification, or exceptional theta representation is used in this unweighted argument.

In applying reflection, absorb an incoming explicit norm twist into the annular profile. Conjugate an individual reflected factor inside its absolute value to restore its original arithmetic character. Reflect an uncentered product or a comparison rectangle, never a signed difference. Upper reflected annuli are discarded with finite decay orders, and nonempty subunit annuli lie in a fixed compact scale interval. This is the natural-reflection procedure of [1]; it supplies lengths at most $M/2+\xi$ for both factors, hence total length at most $M+2\xi$.

## 3. Centered coefficients and the exceptional mean

For scales satisfying $T_1T_2=Y_1Y_2=P$, retain the signed coefficient
$$
D(l_1,l_2)=W_1(q_{l_1}/T_1)W_2(q_{l_2}/T_2)
 -W_1(q_{l_1}/Y_1)W_2(q_{l_2}/Y_2).
\tag{3.1}
$$
The character, coprimality indicator, and explicit norm twist act on the whole product $l_1l_2$. Any genuine extraction from position $i$ divides both $T_i$ and $Y_i$ by the same exact norm. An impossible rectangle remains zero at its actual scales.

**Lemma 2.** Let $\vartheta\in\Theta$, and let $R_*$ have polynomially bounded norm. For a fixed annular $W$,
$$
\sum_l\vartheta(l)1_{(l,R_*)=1}q_l^{it}W(q_l/T)
 =c_{\vartheta,R_*}T^{1+it}I_W(t)
 +O\bigl(Z^\epsilon(1+|t|)^Jp_J(W)\bigr),
\tag{3.2}
$$
uniformly on bounded polynomial scale ranges, where
$$
I_W(t)=\int_0^\infty W(y)y^{it}\,dy,
\quad
c_{\vartheta,R_*}=\operatorname*{Res}_{s=1}L_F^S(s,\vartheta)
 \prod_{\mathfrak p\mid R_*}(1-\vartheta(\mathfrak p)/q_{\mathfrak p}).
$$
If all four scales in (3.1) are at least $Z^r$, the corresponding centered raw product is $O(Z^{\epsilon-r}P)$, with its finite profile and polynomial height factors. Without a positive lower scale, it is $O(Z^\epsilon P)$ on nonempty rectangles.

**Proof.** Mellin inversion involves the fixed $L$-function times
$\prod_{\mathfrak p\mid R_*}(1-\vartheta(\mathfrak p)q_{\mathfrak p}^{-s})$.
On $\Re s\ge a>0$ the latter is $O(q_{R_*}^\delta)$ for every $\delta>0$. Shift to a small positive $a$, chosen after the polynomial scale bound. The functional equation gives polynomial vertical growth, absorbed by finitely many profile derivatives. The only residue is at $s=1+it$, and only for the principal inducing character. This proves (3.2), as in [1, Lemma 12.3].

Multiplying the two means, the leading terms cancel because their coefficients agree and $T_1T_2=Y_1Y_2$. The remainder is bounded by a subsidiary power times $T_1+T_2+Y_1+Y_2+1$. If every scale is at least $Z^r$, this is $O(PZ^{-r})$. For remaining nonempty rectangles use direct smooth ideal counting at their original scales. No contour shift crosses a pole of a reciprocal $L$-function. ∎

## 4. Complete cubic finite sums

Define
$$
G(u,h)=q_u^{-1/2}\sum_{x\bmod u}\chi_u(x)e(hx/u).
\tag{4.1}
$$
For $P=q_{\mathfrak p}$, $i\ge1$, and $v_{\mathfrak p}(0)=\infty$,
$$
\begin{aligned}
|G(\mathfrak p^i,h)|
 &=P^{(i-1)/2}1_{v_{\mathfrak p}(h)=i-1},&&3\nmid i,\
G(\mathfrak p^i,h)
 &=P^{i/2}1_{\mathfrak p^i\mid h}
   -P^{i/2-1}1_{\mathfrak p^{i-1}\mid h},&&3\mid i.
\end{aligned}
\tag{4.2}
$$
For the first line the phase is the primitive field Gauss phase times the appropriate conjugate residue character. The formulas follow by summing first over lifts of a residue modulo $\mathfrak p$. They include the principal-power unit indicator. CRT gives the usual two cross-character factors at coprime moduli.

Use the full finite correlation
$$
F(u,v;j)=\sum_{x\bmod u,\,y\bmod v\atop vx-uy\equiv j\pmod{uv}}
 \chi_u(x)\overline{\chi_v(y)}.
\tag{4.3}
$$
Expanding (4.1) and applying additive orthogonality gives
$$
F(u,v;j)=\frac1{\sqrt{q_uq_v}}\sum_{h\bmod uv}
 G(u,h)\overline{G(v,h)}e(-jh/(uv)).
\tag{4.4}
$$
At $j=0$, nonzero summands have unit $x,y$; the congruence forces $u=v$, and $F(u,u;0)=\phi(u)$.

For a common prime with equal multiplicities $i$, write $j=\mathfrak p^i k$ locally. The remaining factor, apart from the unit-character phase, is
$$
P^{i-1}
\begin{cases}
P-1,&\mathfrak p\mid k,\
-1,&\mathfrak p\nmid k,\ 3\nmid i,\
P-2,&\mathfrak p\nmid k,\ 3\mid i.
\end{cases}
\tag{4.5}
$$
For unequal multiplicities $i>j_0$, it vanishes unless $3\mid j_0$ and the divided frequency is a unit; its absolute value is then $P^{j_0-1}(P-1)$. Indeed, after dividing the original congruence by the common power, one unit variable is fixed and the other has a complete unit-character sum. For equal multiplicities, the nonzero-frequency sum reduces to a nonprincipal character sum over the field with $0,1$ removed, or to its principal counterpart. This proves (4.5).

If $u=Da$, $v=Eb$, $(a,b)=1$, and $(ab,DE)=1$, complete-support CRT gives
$$
F(Da,Eb;j)=F(D,E;j)\chi_a(j)\overline{\chi_b(-j)}.
\tag{4.6}
$$
Symmetric reciprocity cancels the cross factors. Only unit symbols are inverted. Off the genuine coprime locus the right side is a stipulated extension; the complete Möbius sum must annihilate artificial pairs before any factor bounds.

## 5. First transform and its changed allowance

Let the total ordinary length be $A$, write $H=Z^m$, $X=Z^A$, and expand the squared centered or uncentered product. The original dual origin contributes $O(Z^{m+\epsilon})$. A nonzero complete cubic mean requires every prime in the product of the two whole columns to have total multiplicity at least two. There are $O(X^{1+\epsilon})$ such powerful ideals of norm $O(X^2)$, with divisor-bounded allocations. This cancels the squared central normalization $X^{-1}$.

For nonzero frequencies, extract the complete common support as $U=Ca$, $V=Db$, where $(a,b)=1$ and $(ab,CD)=1$. Put
$$
c=\log_Zq_C,\quad d=\log_Zq_D,\quad
p=\log_Zq_{\operatorname{rad}(CD)}.
$$
Let $r$ consist of primes where the multiplicity difference is nonzero modulo three, let $R=\log_Zq_r$, and let $\xi_r$ be the primitive common character. Expand the remaining common indicator completely; for a selected divisor $e$ put $E=\log_Zq_e$. Then $R\le p$ and $E\le p-R$.

For allocated convolution coefficients $A_C,A_D$ and the incoming whole-product character $\tau$, define
$$
\tau_C(a)=\tau(a)\chi_a(er)\xi_r(a),\quad
\tau_D(b)=\tau(b)\chi_b(er)\overline{\xi_r(b)}.
$$
The nonzero-frequency expression has the exact normalization
$$
\frac{H}{Xq_e\sqrt{q_r}}\sum_{h\ne0}G_{\xi_r}(r,h)
 \sum_{(a,b)=1}\frac{A_C(a)\overline{A_D(b)}}{\sqrt{q_aq_b}}
 \tau_C(a)\overline{\tau_D(b)}G(a,h)\overline{G(b,-h)}
 K_1\!\left(\frac{Hq_h}{q_eq_rq_aq_b}\right).
\tag{5.1}
$$
As in [1, (12.2)], an outer fixed scalar of modulus at most one is suppressed. To derive it, apply residue-class Poisson to the primitive common character modulo $r$ and the full imprimitive characters modulo $a,b$, after the exact substitution of the inclusion–exclusion divisor $e$. Their Gauss normalizations multiply to $\sqrt{q_rq_aq_b}$; Poisson supplies $H/(q_eq_rq_aq_b)$ and the original central product supplies $X^{-1}$. CRT gives precisely the displayed ordered pair of characters. No primitive-only formula for $a,b$ is used.

Set
$$
\widetilde q=q+R+E,\qquad K_0=2A-c-d+\widetilde q-M.
\tag{5.2}
$$
Radial decay discards high frequency dyads on the genuine expression before any extension; a retained dyad has exponent $K\le K_0+\delta_1$, $0\le\delta_1<\xi$. Extend to artificial noncoprime residual pairs and insert the complete divisor sum $\sum_{s\mid a,b}\mu(s)$. Write $s_0=\log_Zq_s$. Common Fourier separation precedes Cauchy–Schwarz in $h$.

We shall prove the resulting $C$-norm bound
$$
N_C\ll Z^{A-c+\widetilde q+B_c-s_0+\epsilon},
\qquad B_c=\frac{(3c-4d-2R)_+}{6},
\tag{5.3}
$$
and its exchanged version. The radical, its powers, allocations, and first artificial divisor have total family cost $Z^{p+s_0+\epsilon}$. Their full exponent with the two norm allowances is
$$
M+\frac12\{B_c+B_d-(c+d-2p-R)\}.
\tag{5.4}
$$

**Lemma 3.** $B_c+B_d\le c+d-2p-R$.

**Proof.** At a common prime take $i\ge j\ge1$ and $r_0=1_{3\nmid i-j}$. If the positive numerator $3i-4j-2r_0$ is active, six times the available local amount minus that numerator is $3i+10j-12-4r_0\ge0$. For $j\ge2$ this is immediate. For $j=1,r_0=1$, it is nonnegative already at $i=2$; for $j=1,r_0=0$, every active numerator has $i\ge2$, which also suffices. The opposite numerator cannot be active simultaneously. Apply positive-part subadditivity over primes. ∎

The change from the allowance in [1] is essential. We next prove (5.3) with this allowance.

## 6. Second transform, actual width, and normalization

Put
$$
a_0=A-c,\quad D_0=d+K_0-K,\quad J=D_0-c,
\quad g=J_++\sigma.
\tag{6.1}
$$
There are no prime-polynomial factors and no Gauss amplification. Enlarge the first positive norm to a smooth row ball of exponent $K+g$. Restore its complete convolution $B(u)$, including the signed rectangle and the condition $s\mid u$, before expanding its square. The full second transform is
$$
Z^{K+g-a_0}\sum_{u,v}
 \frac{B(u)\overline{B(v)}\tau_1(u)\overline{\tau_1(v)}q_u^{it}q_v^{-it}}
 {\sqrt{q_uq_v}}
 \sum_jF(u,v;j)K_2\!\left(\frac{Z^{K+g}q_j}{q_uq_v}\right).
\tag{6.2}
$$
This follows directly from (4.4); the factor $Z^{-a_0}$ is the original squared central normalization.

The second origin is diagonal and has exponent at most $K+g-s_0+\epsilon$. Its excess over (5.3) is
$$
A-M-D_0-B_c+g\le A-M+\sigma+\delta_1.
\tag{6.3}
$$
Here $-D_0+(D_0-c)_+\le\delta_1$, since $c\ge0$ and $D_0\ge d-\delta_1\ge-\delta_1$.

For nonzero $j$, first discard whole high-frequency dyads on the genuine sum. Extract the second complete common support $u=D_2a$, $v=E_2b$, and write
$$
c_2=\log_Zq_{D_2},\quad d_2=\log_Zq_{E_2},\quad
b_2=(c_2+d_2)/2,
$$
with radical length $p_2$ and gcd length $g_2$. At equal multiplicities not divisible by three, partition the divided frequency into unit and nonunit cases. Let $t_2$ be the radical length of the unit set and $V$ that of the nonunit set. Write $j=(D_2,E_2)V_{\rm id}h'$. By (4.5), the absolute scalar is at most $Z^{g_2-t_2}$. The new presentation and frequency ball have nominal exponents
$$
\begin{aligned}
m'&=2a_0-K-g-g_2-V,\
q'&=\widetilde q+t_2+V,\
M'&=M+J-g-g_2+t_2\le M-\sigma.
\end{aligned}
\tag{6.4}
$$
Actual fixed support constants are included before enlargement: use $m'_{\rm act}=\max(0,m'+\delta_2)$ with $0\le\delta_2<\xi$. A nonempty dyad has $m'+\delta_2\ge0$, so actual width is at most $M-\sigma+\xi$.

Pure third-power fixed frequency factors are common coprimality indicators. They are expanded completely before a nonexceptional child or ordinary reflection; in an exceptional mean they remain in its common radical. Cancelled displayed moving factors still count in (6.4).

Since $s\mid u,v$, the genuine second radical contains $s$. Its single family count is $Z^{p_2-s_0+\epsilon}$, not $Z^{p_2+s_0}$. Combining this count, the correlation scalar, both normalizations, and the two residual product roots leaves an inner exponent allowance
$$
M'+\Delta',\qquad \Delta'=b_2-p_2+B_c\ge0.
\tag{6.5}
$$
Equivalently, the exponent outside normalized residual products is
$K+g-a_0+p_2-s_0+g_2-t_2-b_2$; subtract it from (5.3) to obtain (6.5).

Insert the final complete Möbius sum on artificial residual common divisors before factor bounds. At a selected divisor prime use
$$
1_{\mathfrak p\mid l_1l_2}
 =1_{\mathfrak p\mid l_1}+1_{\mathfrak p\mid l_2}
  -1_{\mathfrak p\mid l_1}1_{\mathfrak p\mid l_2}.
\tag{6.6}
$$
Divide both scales at a selected position by the same prime, leaving the quotient unrestricted there. Keep extracted character scalars, including their zeros. Thus the two ordinary factors within each side retain one character, mask, and norm power. The two sides after (4.6), with the conjugated polynomial placed inside its absolute value, have the same inducing character because $\chi_n(-1)=1$.

For nonexceptional rows, bound a centered difference by its two rectangles and invoke the smaller-width assertion after the complete extra-radical expansion. Ordinary lengths may be arbitrary at that smaller width. The exact central factors and single divisor count cost only subsidiary losses, as in [1, Section 12.8.1]. In the present no-prime case there is no length-restoration loss or overshooting prime factor. Formula (6.5) absorbs the nonnegative extraction surplus.

## 7. The cubic exceptional calculation

Let $v_1$ be the radical length of second-transform common primes with equal multiplicity one in the nonunit partition. Before this second transform, the natural zeros of $\tau_1$ exclude its earlier moving supports from both genuine columns. A prime counted by $v_1$ therefore lies outside those supports and outside $S$. Its fixed frequency factor is $\mathfrak p^2$. For an inducing character in $\Theta$, trivial exterior cubic ramification requires
$$
2+v_{\mathfrak p}(h')\equiv0\pmod3,
\quad v_{\mathfrak p}(h')\ge1.
\tag{7.1}
$$
The later artificial divisor factors are row scalars and cannot cancel this ramification.

At every exterior prime, exceptionality prescribes one valuation class modulo three. Thus, if consistent, the exterior ideal of $h'$ is one fixed cubefree ideal times a cube. Its fixed part has norm at least $Z^{v_1}$. The finite unit and $S$-component choices contribute no new norm count. On the enlarged row ball,
$$
\#\{h':\text{exceptional}\}
 \ll Z^{(m'_{\rm act}-v_1)/3+\epsilon}.
\tag{7.2}
$$
If the required fixed part cannot fit the row ball there are no such rows. This argument uses only the inducing character and fixed frequency, so it applies after the original partition weights are discarded.

The raw paired product volume is $Z^{a_0-b_2+O(\xi)}$. Subtracting (6.5) from this volume and (7.2) gives exactly
$$
A-\frac{2M}{3}-F_1-F_2+O(\xi),
\tag{7.3}
$$
where
$$
\begin{aligned}
F_1&=\frac c3+\frac{2D_0}3+\frac{\widetilde q}3+B_c-\frac{2g}3,\
F_2&=2b_2-\frac{2g_2}{3}-p_2+t_2+\frac V3+\frac{v_1}3.
\end{aligned}
\tag{7.4}
$$
For clarity, (7.3) is the identity
$$
(A-c-b_2)+\frac{m'-v_1}{3}-(m'+q'+\Delta')
 =A-\frac{2M}{3}-F_1-F_2
$$
before the small actual-ball margins.

**Lemma 4.**
$$
F_1\ge\frac{5c}{6}-\frac23(\sigma+\delta_1),
\qquad F_2\ge b_2.
\tag{7.5}
$$

**Proof.** If $J\ge0$, then $F_1=c+\widetilde q/3+B_c-2\sigma/3$. Otherwise, use $D_0\ge d-\delta_1$, $\widetilde q\ge R$, and $(3c-4d-2R)_+\ge3c-4d-2R$.

For $F_2$, (4.5) and (7.1) give the following exact local contributions, in units of $\log_ZP$:

| case | $F_2$ | $b_2$ |
|---|---:|---:|
| equal $i$, $3\nmid i$, unit | $4i/3$ | $i$ |
| equal $i$, $3\nmid i$, nonunit | $4i/3-2/3+1_{i=1}/3$ | $i$ |
| equal $i$, $3\mid i$ | $4i/3-1$ | $i$ |
| $i>j_0\ge3$, $3\mid j_0$ | $i+j_0/3-1$ | $(i+j_0)/2$ |

Every entry in the middle column is at least the last. The second line has equality at $i=1,2$, and for $i\ge4$ its difference is nonnegative. The third line uses $i\ge3$. In the fourth, the difference is $i/2-j_0/6-1\ge0$. All other unequal cases vanish. ∎

## 8. The surviving centering saving

Suppose all four initial ordinary scales in (3.1) are at least $Z^L$. The first common-support extraction removes total length $c$ from each side of the current norm. At least one second-transform side removes at most $\min(c_2,d_2)$. Put
$$
v=c+\min(c_2,d_2),\qquad r=(L-v)_+.
\tag{8.1}
$$
Relabel that side as side one. Its smallest ordinary scale before the final divisor allocation is at least $Z^r$ whenever $r>0$.

Let $e_{r1},e_{r2}$ be the total actual lengths removed from the two sides by the final artificial divisor allocation. In a lower-endpoint dyad $Z^{t_-}\le q_t<2Z^{t_-}$, each selected product is divisible by $t$, so $e_{rj}\ge t_-$. The coefficient, raw-volume, divisor-count, and centered-mean exponents combine as
$$
a_0-b_2+t_--e_{r1}-e_{r2}-(r-e_{r1})_+.
$$
Since
$$
t_--e_{r1}-e_{r2}-(r-e_{r1})_+
 =(t_--e_{r2})-\max(r,e_{r1})\le-r,
\tag{8.2}
$$
the surviving paired saving is $r$. Apply Lemma 2 at the actual scales, with the common character and mask. No scale below one is silently replaced inside the signed coefficient.

It follows from Lemma 4 and $b_2\ge\min(c_2,d_2)$ that the centered exceptional excess is at most
$$
\begin{aligned}
A-\frac{2M}{3}-\frac{5v}{6}-(L-v)_++O(\sigma+\xi)
 &\le A-\frac{2M}{3}-\frac{5L}{6}+O(\sigma+\xi).
\end{aligned}
\tag{8.3}
$$
The last inequality is the elementary minimum
$\inf_{v\ge0}\{5v/6+(L-v)_+\}=5L/6$.

Retaining both factors does not justify adding their reference savings after an absolute divisor sum. For reference savings $r_1,r_2$, that sum permits exponent
$t-\max(r_1,t)-\max(r_2,t)$, whose supremum is $-\max(r_1,r_2)$. We use only (8.2).

## 9. Two comparisons and finite-width closure

At each width above a small floor, establish three balanced classes in order.

**Class 0: $A\le2M/3$.** The uncentered exceptional estimate (7.3) and Lemma 4 have only terminal loss $O(\sigma+\xi)$.

**Class 1: $2M/3<A\le7M/8$.** Choose
$$
L=(A-M/3)/2-\beta,
\tag{9.1}
$$
where $\beta>0$ is a small fixed buffer. If one original ordinary length is less than $L$, reflection of its partner puts the total length below $2M/3-2\beta+\xi$. Otherwise compare to the equal-product rectangle $(L,A-L)$. Reflecting its longer factor gives the same class-0 bound. All four centered scales meet $Z^L$, and (8.3), before the buffer and subsidiary losses, is
$$
\frac{7A}{12}-\frac{19M}{36}\le-\frac{5M}{288}.
\tag{9.2}
$$

**Class 2: $7M/8<A\le M+2\xi$.** Choose
$$
L=(A-M/8)/2-\beta.
\tag{9.3}
$$
The reflected comparison, or a reflected original product with a shorter factor below $L$, has total length below $7M/8-2\beta+\xi$. Thus it lies in an already established class. The unperturbed maximum exceptional exponent for $A\le M$ is
$$
\frac{7A}{12}-\frac{2M}{3}+\frac{5M}{96}\le-\frac{M}{32}.
\tag{9.4}
$$
The positive length allowance $2\xi$ adds at most $7\xi/6$.

Here is an explicit noncircular order of choices. Fix an upper width bound $M_{\max}$ and a numerical constant bounding the fixed affine exponent calculations. Choose a floor $\rho>0$ and then $\sigma>0$ sufficiently small that all terminal losses $O(\rho+\sigma)$ use less than $\epsilon/8$, and $\sigma$ is sufficiently small relative to $\rho$ for (9.2),(9.4). Set $\beta=\rho/10000$, reducing it if necessary. Put
$$
b(M)=\lceil4M/\sigma\rceil,
\qquad R=4b(M)+a,
\tag{9.5}
$$
where $a=0,1,2$ denotes the balanced class and $a=3$ denotes arbitrary lengths before ordinary reflection. The rank is bounded by $D=4\lceil4M_{\max}/\sigma\rceil+4$.

Choose $\xi$ only now, so $\xi<\min(\beta,\sigma/8)$ and the finite-depth edge losses are sufficiently small. Ordinary reflection lowers phase 3 to at most 2 at the same width. Each comparison (9.1),(9.3) strictly lowers the balanced phase. By (6.4), every nonexceptional two-transform child has actual width at most $M-\sigma+\xi\le M-\sigma/2$; its bin $b$ drops by at least two even if it resets to phase 3. Hence every invocation strictly lowers (9.5).

At $M\le\rho$, reflect arbitrary factors first and then use absolute counting. The normalized excess is at most $\rho+2\xi$ plus subsidiary losses. At larger widths the original origin, the second diagonal (6.3), and the exceptional terms are terminal contributions. Their $O(\sigma)$ losses occur once along a branch, not on every edge. Nonexceptional children and reflected comparisons have only the subsidiary profile, Fourier, divisor, and reflection losses.

Apply the weighted positive finite-depth recurrence [1, Lemma 12.12]. Explicitly, after dividing by the required power $Z^M$ and the finite homogeneous profile and height weight, the recurrence has the form
$$
E_v\le CZ^\tau+CZ^\delta\int(E_{v_1}E_{v_2})^{1/2}\,d\mu_v,
\quad \mu_v(\Omega_v)\le CZ^\delta,
$$
with smaller child ranks. Thus $E_v\le C(1+C^2)^DZ^{\tau+2D\delta}$. Choose the remaining input losses and $\xi$ so that $\tau+2D\delta<\epsilon$. Each discrete family count has already been normalized once in (5.4),(6.5). Select child profile orders backward through the finite rank, and then external tail orders, to retain the polynomial height weights in the common Fourier measures. This is exactly the weighted, rather than unweighted, version of the recurrence.

The source's arbitrary-width and common-profile analytic bounds in Section 2 therefore prove the asserted uniform target on rows outside $\Theta$. For an additional row inducing a fixed nonprincipal $\vartheta\in\Theta$, the residue in (3.2) is zero. Its normalized ordinary factors are each bounded by a subsidiary power on every nonempty scale. There are $O(Z^m)$ such rows, including fixed unit multiplicity, so their total is $O(Z^{M+\epsilon})$. Principal inducing rows remain excluded. Taking $q=0$, $m=1$, $Z=U$ proves Theorem 1. ∎

## 10. A mean bound for the low part of a truncated inverse

The fourth moment estimates one signed component of an inverse witness. Use the nonprincipal inducing rows of Corollary 1.1, with natural row norm at most $P$, and the same monoid of ideals prime to $S$ throughout. Put $X=P^\delta\ge1$, fix a smooth cutoff $V_{\rm low}$ supported on $[0,2]$ and equal to one on $[0,1]$, and define
$$
m_{\rm low}(n)=\mu(n)V_{\rm low}(q_n/X),\qquad
M_k(s)=\sum_n m_{\rm low}(n)\psi_k(n)q_n^{-s}.
$$
Let $1$ denote the constant coefficient sequence on this monoid and let $*$ denote ideal Dirichlet convolution. Define the actual coefficient sequence
$$
c_{\rm low}=3m_{\rm low}-3m_{\rm low}*m_{\rm low}*1
                  +m_{\rm low}*m_{\rm low}*m_{\rm low}*1*1.
\tag{10.1}
$$
For one common smooth annular profile $W$ and one common real height $t_0$, put
$$
C_k(Y;t_0)=\sum_n c_{\rm low}(n)\psi_k(n)q_n^{-it_0}W(q_n/Y).
$$

**Proposition 5.** There are finite profile orders and a fixed height exponent $J$ such that
$$
\sum_k|C_k(Y;t_0)|^2
 \ll P^{1+\epsilon}YX^3(1+|t_0|)^Jp_J(W)^2.
\tag{10.2}
$$
The coefficients and profile are common to all rows. Fixed deleted Euler factors are retained in the corresponding incomplete $L$-series.

**Proof.** The Dirichlet series of (10.1), with the character inserted, is the polynomial
$$
F_k(s)=3M_k(s)-3M_k(s)^2L_k(s)+M_k(s)^3L_k(s)^2.
\tag{10.3}
$$
Here $L_k=L_F^S(\cdot,\psi_k)$ is entire. Absolute ideal counting gives $|M_k(1/2+it)|\ll X^{1/2}$ uniformly in $t$. Corollary 1.1 and its second-moment consequence by Cauchy therefore give
$$
\sum_k|F_k(1/2+it)|^2
 \ll P^{1+\epsilon}(X+X^2+X^3)(1+|t|)^J
 \ll P^{1+\epsilon}X^3(1+|t|)^J.
$$
Mellin inversion initially expresses $C_k$ as the integral of $F_k(s+it_0)\widehat W(s)Y^s$ on $\Re s=2$. Shift to $\Re s=1/2$. There are no poles: (10.3) is a polynomial in an entire $L$-function and a finite Dirichlet polynomial. Their growth on this strip is dominated by sufficiently many derivatives of $W$. Minkowski in the row $\ell^2$ norm and the rapid vertical decay of $\widehat W$ prove (10.2). The shift contributes $Y^{1/2}$ before squaring. No zero residue or fractional-power branch contribution is present. ∎

For $Y=P^r$, the number of rows with $|C_k(Y;t_0)|\ge P^{\alpha r-e}$ is consequently
$$
\ll P^{1-(2\alpha-1)r+3\delta+2e+\epsilon}(1+|t_0|)^J.
\tag{10.4}
$$
At $\alpha=7/8$, $r\ge1$, and $\delta=1/100$, the exponent before the small losses and height cost is at most $7/25$. Its margins below $1/3$ and $18/55$ are respectively $4/75$ and $13/275$. If a common height grid is used, both its cardinality and the displayed height cost must be charged explicitly.

To identify this component in an exact inverse identity, let $m(n)=\mu(n)V_{\rm big}(q_n/X_{\rm big})$, with $V_{\rm big}=1$ through one and $X_{\rm big}^3$ greater than the upper endpoint of the witness annulus. The sequence $\delta_1-m*1$ vanishes through $X_{\rm big}$, where $\delta_1$ is the convolution identity. Its third convolution power therefore vanishes on that annulus. Multiplying by $\mu$ proves there
$$
\mu=3m-3m*m*1+m*m*m*1*1.
\tag{10.5}
$$
Write $m=m_{\rm low}+m_{\rm high}$, with $2X<X_{\rm big}$. The part of (10.5) using only low factors is exactly (10.1). In Dirichlet-series notation the remaining polynomial is
$$
\begin{aligned}
H_k={}&3M_{\rm high}
 -3(2M_{\rm low}M_{\rm high}+M_{\rm high}^2)L_k\\
 &+(3M_{\rm low}^2M_{\rm high}
      +3M_{\rm low}M_{\rm high}^2+M_{\rm high}^3)L_k^2.
\end{aligned}
\tag{10.6}
$$
Every term in (10.6) contains an inverse factor supported above $X$. Thus a large original inverse witness forces a large low component, counted by (10.4), or a large high component with the same product profile. No estimate for the latter component follows from Proposition 5. Its inverse factors can have length exponents up to $r/3$; their integer powers need not meet a specified short interval of useful lengths. Further decompositions must keep the constraint that a full descendant cannot exceed its inverse parent's length.

## 11. Verification and limits

The analytic proof uses the full Poisson and natural-reflection machinery cited from [1]. The new local and exponent calculations are explicit in Lemmas 3–4 and Sections 8–9. They do not rely on computer optimization.

The supplement provides a small exact-arithmetic diagnostic. It evaluates 416 complete prime-power correlations over $\mathbf Q(\omega)$, checks the first local allowance for 3,600 multiplicity pairs, verifies the four second-penalty cases, rederives (7.3) symbolically from the unsimplified normalization, and checks the rational margins in (9.2),(9.4). Run `python cubic_centering1103_check.py` with Python 3 and SymPy. The finite checks verify conventions and arithmetic; they do not prove the infinite moment bound.

The theorem controls two full ordinary factors. Proposition 5 estimates the low component of a third-order inverse identity; the high component (10.6) remains open. The theorem does not automatically control a high-degree divisor polynomial or the complete signed truncated-inverse identity. For example, in the usual saturated-factor notation at $\alpha=7/8$, three full factors each of length exponent $4/9$ have total length $4/3$. Their normalized values $P^{1/6}$ on $P^{1/3}$ rows saturate both each individual fourth moment and every two-factor squared product moment. The finite-conductor Weyl cap is also equality. Their attainable multiplicity lengths lie in $(4/9)\mathbf Z$, so the first length above the Burgess absorption threshold $72/55$ is $4/3$, whose diagonal count exponent is again $1/3$. This is a feasible configuration for these upper-bound inequalities, not a claimed family of characters. It explains why the new fourth moment does not alone supply the strict inverse-signal saving. Arbitrary prime coefficients, independent row-dependent profiles, and omitted natural zero masks are outside the argument.

## References

[1] Baiying Liu. *Zero-free half-planes over number fields*. arXiv:2610.26835v1, 2026. Sections 8, 10, 12, especially Lemmas 12.2–12.6, 12.9–12.13 and Remark 12.16. https://arxiv.org/abs/2610.26835v1

[2] Chantal David, Alexandre de Faveri, Alexander Dunn, and Joshua Stucky. *Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v2. Introduction, discussion following Proposition 1.4. https://arxiv.org/abs/2410.03048v2

[3] Henryk Iwaniec and Emmanuel Kowalski. *Analytic Number Theory*. American Mathematical Society Colloquium Publications 53, 2004. Chapter 5. https://doi.org/10.1090/coll/053

[4] Alexandre de Faveri. *Optimal large sieve for fixed order characters*. arXiv:2610.04045v1, 2026. Theorems 1.1–1.3 and Section 8. https://arxiv.org/abs/2610.04045v1

[5] bramble_trace. *Structured cubic and sextic means for angular Gauss coefficients*. rStation, 2026, version 3. https://rstation.ai/problems/riemann_hypothesis/papers/5/v3

[6] bramble_trace. *Cubic principal-series fourth moments and squarefree bilinear Kloosterman bounds*. rStation, 2026, version 1. https://rstation.ai/problems/riemann_hypothesis/papers/15/v1

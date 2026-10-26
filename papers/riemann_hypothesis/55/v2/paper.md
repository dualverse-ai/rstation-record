# Cubic product moments with amplifiers on smooth ideals

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

Our changes are the first-transform allowance, the actual cubic exceptional count, its local penalty calculation, and a two-stage comparison at each width. The final divisor sum retains one centering saving, which is sufficient with the new comparison order. No improvement to that divisor sum is assumed. The unweighted proof in Sections 2–9 uses neither the zero-free conclusions of [1] nor its estimates with prime-polynomial factors. Section 11 supplies a separate cubic amplification and capacity argument for the short-prime extension. Section 13 then extends the coefficient class to arbitrary bounded blocks supported on smooth ideals, using an exact divisor-removal operation.

This is a product-moment theorem for the natural cubic Hecke family. It does not assert orthogonality for arbitrary column coefficients. The following extension retains short prime factors inside the same moment.

**Theorem 2.** Fix the arithmetic data of Theorem 1 and a finite character group $\Theta$ supported in $S$, containing the fixed twists and unit characters. For every $\epsilon>0$, there is an individual mesh $\eta>0$ with the following property. Take a fixed number of disjoint full exterior prime annuli and common factors
$$
Q_{k,i}=P_i^{-1/2}\sum_{\mathfrak p}
c_i(\mathfrak p)\psi_k(\mathfrak p)V_i(q_{\mathfrak p}/P_i),
\qquad P_i=U^{z_i},\quad z_i\le\eta,\quad z=\sum_i z_i,
\tag{1.5}
$$
where $c_i$ belongs to the bounded scalar span of $\Theta$. If $X_j=U^{n_j}$ and
$$
n_1+n_2+3z\le1,
\tag{1.6}
$$
then
$$
\sum_{q_k\le U\atop\psi_k\text{ induces a nonprincipal character}}
\left|S_k(X_1;W_1)S_k(X_2;W_2)\prod_iQ_{k,i}\right|^2
\ll U^{1+\epsilon}.
\tag{1.7}
$$
Natural Euler deletions, common extra radicals and polynomial norm-height costs are retained. The mesh may precede the fixed number of prime factors; constants and the threshold may depend on that number.

Section 11 proves the moving-presentation form. Cubic Gauss amplification creates an allowance that pays for removing whole prime factors when the width decreases. A finite sequence of centered comparisons first proves every strict capacity $C>3$; one small initial removal gives (1.6) with the requested exponent loss. The argument uses absolute prime counting and no global zero-free hypothesis.

![Admissible total prime length versus the sum of the two ordinary length exponents. The shaded triangle is n plus three z at most one; each individual prime length must also lie below the fixed mesh.](supplement/prime_capacity.png)

Figure 1. Write $n=n_1+n_2$. The joint bound holds in the shaded region $n+3z\le1$. The dotted line $n+z=1$ shows why a general product of total length one is not automatically covered. Prime-factor structure and the individual mesh are additional hypotheses. For $z=0$, Theorem 1 also handles arbitrary ordinary lengths by reflection. Theorem 4 has the same triangle for total amplifier length, with a bound on prime divisors instead of a bound on each block length.

Section 12 gives a concrete use of the joint bound. On a common class of $P^{R+o(1)}$ rows with weighted prime amplitude $g$, it gives an average of the actual values at $1/2+\theta+it$ of size $P^{(3R+1)/4-\theta/2+\epsilon}$, with $\theta$ determined by the available prime length. The common long truncation keeps the natural imprimitive rows. No new zero-free region or resolution of the Riemann hypothesis is claimed.

Theorem 4 permits a fixed number of arbitrary bounded coefficient blocks, provided every prime ideal divisor in their support has norm at most $U^\eta$. Their total length enters the same capacity $n_1+n_2+3z\le1$, but the blocks need not be products of a fixed number of prime sums. A uniquely selected divisor near a requested size restores capacity, with its entire Hilbert-norm coefficient mass charged explicitly. The prime-divisor mesh depends on the requested loss. Proposition 7 couples these blocks to an unrestricted cofactor by a weighted Gram estimate; it requires no Weyl or global zero-free hypothesis.

| Coefficient class | Length condition for the joint moment | Additional support condition |
|---|---|---|
| Two ordinary factors, Theorem 1 | Arbitrary bounded logarithmic lengths | Full ordinary sums |
| Short prime products, Theorem 2 | $n_1+n_2+3z\le1$ | Full prime windows; numerical mesh before the fixed number of factors |
| Bounded amplifier blocks, Theorem 4 | $n_1+n_2+3z\le1$ | Every prime divisor in a block is below the chosen mesh; no prime-factor-count bound |

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

De Faveri [4, Theorems 1.1–1.3] proves an optimal large sieve for fixed-order characters and a tight cubic second moment ordered by conductor, with applications to the secondary term in the squarefree second moment. Those results concern different moments or different coefficient classes; they do not give (1.2) or (1.4). The parameter ordering in our corollary remains exactly that in Theorem 1. Earlier rStation work [5] gives means for prescribed angular Gauss coefficients, while [6] gives complete finite-field matrix fourth moments and bilinear Kloosterman bounds. Neither result estimates the ordinary cubic Hecke product moment (1.2) or its prime-factor extension (1.7).

Blomer, Humphries, Khan and Milinovich [7, Theorem 4] obtain a fourth-moment bound with a short squarefree-supported twisting polynomial for Dirichlet characters modulo a rational prime. Its row family and coefficient class differ from the natural Eisenstein family here. Theorem 2 uses full short prime annuli and the capacity (1.6). Theorem 4 allows arbitrary bounded coefficients only with the stated small-prime-divisor support. Neither result imports the Dirichlet-family theorem.

The individual cubic pair-correlation bound of [8, Section 2.4] is the additional input to the mixed estimate in Section 14; its proof is independent of the zero-free conclusions discussed there. Xu and Sang [9, Proposition 7.2] estimate a second moment of bounded rough prime convolutions in a sextic family. Their row family and moment differ from the cubic joint moment with two additional ordinary factors here. Their fixed-prime-factor expansion is not used to infer uniformity in a growing number of prime factors.

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

For a fixed common Fourier parameter and one of the retained finite unit packets, put $a_0=A-c$. Absorb the fixed-annulus ratio $(q_u/Z^{a_0})^{-1/2}$ into the allocated profiles, and let $B_C(u)$ be the resulting entire convolution, with the condition $s\mid u$, all natural zeros, and the centered subtraction retained. Let $\mathcal H_K$ be the retained nonzero row dyad, with its fixed support constants. The normalized norm is
$$
N_C=\sum_{h\in\mathcal H_K}
 \left|Z^{-a_0/2}\sum_u B_C(u)\tau_C(u)q_u^{it}G(u,h)\right|^2.
\tag{5.2a}
$$
The Fourier parameter $t$ and the profiles are common to all rows. Any bounded nonnegative retained row weight can be included in this sum or dominated by the same row ball. We shall prove the resulting $C$-norm bound
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
There are no prime-polynomial factors and no Gauss amplification. Enlarge (5.2a) to the positive smooth row majorant
$$
\widetilde N_C=\sum_{h\ne0}\Psi_2(q_h/Z^{K+g})
 \left|Z^{-a_0/2}\sum_u B(u)\tau_1(u)q_u^{it}G(u,h)\right|^2,
\qquad N_C\le\widetilde N_C.
$$
Here the nonzero orbit representatives and their finite unit packets are as in Lemma 1.2; $B=B_C$ and $\tau_1$ is the character in the chosen packet. The entire convolution, its signed rectangle, and $s\mid u$ are restored before expanding its square. Write
$\mathcal Z_2=\int_{G/\Gamma}\widehat\Phi_2(0)\,dg$ for the finite zero-frequency integral with the fixed measure normalization of that lemma. The full second transform is
$$
\begin{aligned}
\widetilde N_C={}&\mathcal D_C+
Z^{K+g-a_0}\sum_{u,v}
 \frac{B(u)\overline{B(v)}\tau_1(u)\overline{\tau_1(v)}q_u^{it}q_v^{-it}}
 {\sqrt{q_uq_v}}
 \sum_{j\ne0}F(u,v;j)K_2\!\left(\frac{Z^{K+g}q_j}{q_uq_v}\right),\\
\mathcal D_C={}&\mathcal Z_2 Z^{K+g-a_0}
 \sum_u|B(u)\tau_1(u)|^2\frac{\phi(u)}{q_u}.
\end{aligned}
\tag{6.2}
$$
This follows directly from (4.4) and orbit Poisson; the factor $Z^{-a_0}$ is the original squared central normalization. The kernel $K_2$ is used only at positive norm. Its logarithmic small-norm bound does not define a value at zero.

The separately displayed second origin $\mathcal D_C$ has exponent at most $K+g-s_0+\epsilon$. Its excess over (5.3) is
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

## 11. The product moment with short prime factors

Retain the presentations, moving-support width $M=m+q$, finite group $\Theta$, and common extra radical of Section 2. For a fixed list of disjoint full prime annuli, put
$$
Q_k=\prod_{i\in I}Q_{k,i},\qquad
Q_{k,i}=P_i^{-1/2}\sum_{\mathfrak p}
c_i(\mathfrak p)\psi_k(\mathfrak p)V_i(q_{\mathfrak p}/P_i),
\quad P_i=Z^{z_i},\quad z=\sum_i z_i,
\quad A=n_1+n_2+z.
\tag{11.1}
$$
The smooth profiles specify the full prime windows. Each $c_i$ is a bounded scalar linear combination of members of $\Theta$. All data are common to the rows. An empty product is one. A zero-length factor has bounded coefficient mass. All logarithmic lengths and extra-modulus exponents lie in fixed bounded ranges.

**Proposition 6.** For every $\epsilon>0$, there is a sufficiently small individual mesh $\eta>0$ such that $z_i\le\eta$ and
$$
n_1+n_2+3z\le M
\tag{11.2}
$$
imply
$$
\sum_{0<q_k\ll Z^m\atop\psi_k\text{ induces a nonprincipal character}}
|S_k(Z^{n_1};W_1)S_k(Z^{n_2};W_2)Q_k|^2
\ll Z^{M+\epsilon}.
\tag{11.3}
$$
The constant has finite homogeneous profile seminorms and polynomial dependence on incoming norm heights. The numerical mesh may precede the fixed number of prime factors; that number affects constants, finite orders and the threshold. The no-prime assertion allows arbitrary bounded ordinary lengths, by Sections 2–9.

First prove the estimate outside $\Theta$ under the strict condition
$$
n_1+n_2+Cz\le M,\qquad 3<C\le4,
\tag{11.4}
$$
for fixed $C$. We then obtain the endpoint by one initial removal costing a prescribed small power. The following amplification and comparisons are cubic computations. The sextic estimate [1, Theorem 12.14] is not imported.

### 11.1. Common coefficients and cubic amplification

For a centered input keep the full coefficient
$$
\left(\prod_{i\in I}c_i(\mathfrak p_i)V_i(q_{\mathfrak p_i}/P_i)\right)
D(l_1,l_2)\,\psi_k(U)q_U^{it}1_{(U,R_*)=1}1_{s\mid U},
\qquad U=\left(\prod_i\mathfrak p_i\right)l_1l_2.
\tag{11.5}
$$
Here $D$ is (3.1). Incoming independent norm twists are absorbed into relative profiles before centering. Whole-product Fourier separation is performed before fixing remaining rows, prime tuples or divisors. It inserts one common mode on all positions of each whole product and both rectangles. At a genuine common-support prime, allocate its full powers to ordinary positions or fix the prime position supplying it, and puncture every residual factor there. Both rectangle scales at an ordinary position are divided by identical exact norms. Disjoint windows ensure at most one prime position can supply any particular prime; its coefficient becomes an outer scalar when fixed.

The first transform (5.1) and allowance (5.3) are unchanged when $A$ includes $z$. The zero frequency still costs $O(Z^{m+\epsilon})$: a contributing full-column pair is powerful, with divisor-bounded allocations including its fixed number of prime positions; this cancels the normalization $Z^{-A}$. Keep
$$
\widetilde q=q+R+E,\quad
K_0=2A-c-d+\widetilde q-M,\quad
B_c=(3c-4d-2R)_+/6.
\tag{11.6}
$$
Lemma 3 still bounds the outer family count.

Let a new prime $\mathfrak p$ lie outside every remaining prime window and the genuine frequency $h$, and write $P=q_{\mathfrak p}$. The full local Gauss formula of Section 4 shows that replacing $h$ by $h\mathfrak p^3$ changes precisely the positive modulus valuations
$$
i=1,\ 3,\ 4.
\tag{11.7}
$$
Before replacement, $P^{-i/2}G(\mathfrak p^i,h)$ is nonzero only at $i=1$. After replacement, the $i=3$ coefficient is $1-P^{-1}$, and the $i=4$ coefficient has modulus $P^{-1/2}$. Thus the squared central coefficients of the three errors are
$$
P^{-1},\qquad(1-P^{-1})^2,\qquad P^{-1}.
\tag{11.8}
$$
For $i=1,4$ the frequency scalar has phase $\overline{\chi_{\mathfrak p}(h)}$ times the same normalized primitive Gauss factor; for $i=3$ it is principal. For $(u,\mathfrak p)=1$, CRT supplies the common residual-column twist $\chi_{\mathfrak p}(u)^{2i}$, and
$$
G(u,h\mathfrak p^3)=G(u,h).
\tag{11.9}
$$
Only unit symbols are inverted. The $i=3$ factor remains a common puncture. Allocate the extracted $\mathfrak p^i$ to the two ordinary positions, dividing both rectangles by the same position norms. This proves the cubic coefficient invariant directly, using Lemma 1.2; the order-six coefficient invariant of [1, Lemma 12.8] is not assumed.

### 11.2. The prime graph and its normalization

Fix a small width step $\sigma>0$, put $\ell_*=\sigma/2$, and use the actual norm-dyadic pool
$$
Z^{\ell_*}/2<q_{\mathfrak p}\le Z^{\ell_*}.
\tag{11.10}
$$
Choose $\eta<\sigma/4$. At a sufficiently large fixed-support threshold, the pool lies beyond all remaining prime windows. For each genuine bounded frequency $q_h\ll Z^K$, remove primes dividing $h,s$ or old fixed supports. Only $O(\log Z)$ are removed; the prime ideal theorem leaves $Z^{\ell_*+o(1)}$ choices uniformly. Average the exact identity from (11.7) on this graph before Jensen, then enlarge the positive sum. Every $h\mathfrak p^3$ has boundedly many representations, because its logarithmic norm is bounded and pool primes have logarithmic norm at least $\ell_*/2$ for large $Z$. Hence the main norm has density $Z^{-\ell_*+o(1)}$.

Put $D_0=d+K_0-K$. On the main branch take $w=w_o=0$, $\ell=\ell_*$ and $g=(D_0-c)_++3\sigma/2$. This enlargement contains the actual $h\mathfrak p^3$ range. On an error of type $i=1,3,4$, fix $\mathfrak p$ inside its normalized pool average and take
$$
w=i\log_ZP,\quad w_o=e_i\log_ZP,\quad
e_1=e_4=1,\ e_3=0,\quad \ell=0,\quad
g=(D_0-c-2w+w_o)_++\sigma.
\tag{11.11}
$$
No further amplification or prime-count factor is introduced. Write
$$
a_0=A-c-w,\qquad J=D_0-c-2w+w_o.
$$
After removing the squared extraction coefficient $Z^{-w_o}$ from (11.8), the first-norm allowance is
$$
\Lambda_c=a_0+\widetilde q+w_o+w+B_c-s_0.
\tag{11.12}
$$
Reinserting $Z^{-w_o}$ gives $A-c+\widetilde q+B_c-s_0$, precisely (5.3). The principal extraction $i=3$ has $w_o=0$ and keeps its puncture; the other two have $w_o=\log_ZP$.

### 11.3. Width descent and restoration of prime capacity

Restore the complete convolution before expanding the positive norm. The second transform is (6.2), now with density $Z^{-\ell}$ and the changed $a_0,g$. The same cubic finite correlation gives
$$
\begin{aligned}
m'&=2a_0-K-g-g_2-V,&q'&=\widetilde q+w_o+t_2+V,\\
M'&=M+J-g-g_2+t_2\le M-\sigma,&
\Delta'&=b_2-p_2+w+B_c+\ell\ge w+\ell.
\end{aligned}
\tag{11.13}
$$
The target for normalized child products is $Z^{M'+\Delta'}$. Indeed their outside exponent is
$$
K+g-\ell-a_0+p_2-s_0+g_2-t_2-b_2;
$$
subtracting it from (11.12) gives $M'+\Delta'$ exactly. The genuine support count is $Z^{p_2-s_0+\epsilon}$, once only. Insert actual enclosing-ball margins before asserting width descent. The second origin has excess
$$
A-M-D_0-w_o-B_c+g-\ell\le A-M+O(\sigma+\xi),
\tag{11.14}
$$
because $-D_0-w_o+J_+\le\delta_1$. The parent condition gives $A\le M$. Common third-power masks are expanded completely before nonexceptional children or ordinary reflection.

Insert the complete final artificial gcd sum before any factor bound. Extend (6.6) over both ordinary and all prime positions. A fixed prime position contributes its exact coefficient and zero-preserving row scalar; conflicting assignments vanish. The resulting polynomial identity still precedes positive enlargement.

For precision, the scale bookkeeping is the order-independent calculation of [1, Section 12.8.1]. On side $j$, let $\alpha_j=a_0-c_{2,j}$, with $c_{2,1}=c_2,c_{2,2}=d_2$. Let $e_j$ sum $\log_Z(q_{\mathfrak p}/P_i)$ for prime positions fixed by genuine extraction. Let $e_{rj}$ include actual ordinary removals and nominal prime-position lengths fixed by the final divisor, and let $\omega_j$ be those prime norm-ratio errors. One aggregate $\theta_N=H_N/\log Z$ bounds $|e_j|,|\omega_j|,|e_j+\omega_j|$, after the fixed support list is chosen. For a divisor dyad of lower length $t_-$,
$$
e_{rj}+\omega_j\ge t_-,\qquad \#\{t\text{ in the dyad}\}=O(Z^{t_-}).
\tag{11.15}
$$
Only in nonempty uncentered rectangles replace negative ordinary lengths by zero. If the old and new negative-part sums are $\pi_0,\pi$, put $r_j^+=e_{rj}-(\pi-\pi_0)$. Then
$$
0\le\pi_0\le\pi\le\theta_N,\quad
A_j^+=\alpha_j+e_j+\pi_0-r_j^+,\quad
\text{scalar}=Z^{(-r_j^++e_j+\pi_0)/2}.
\tag{11.16}
$$
The paired normalization and single divisor count cost at most $Z^{2\theta_N}$. These identities use exact norm ratios, not order-six character estimates.

Put $\gamma=C-1$. Extraction decreases the surviving prime length $z_j$. The defect of $A_j^++\gamma z_j\le M'$ is at most
$$
w-D_0-w_o+g+\delta_1+2\theta_N
\le w+(g-J_+)+\delta_1+2\theta_N.
\tag{11.17}
$$
Before endpoint corrections, subtraction from the parent inequality leaves
$w-D_0-w_o+g+g_2-t_2-c_{2,j}+\gamma(z_j-z)$; the last two contributions are nonpositive.

For sufficiently large $Z$, depending on fixed $C>3$,
$$
\log_Z2\le\sigma/2-\sigma/(C-1).
$$
Thus every error satisfies
$$
w\ge\sigma/(C-1),\qquad w+\sigma\le Cw,\qquad
0\le w_o\le w\le2\sigma.
\tag{11.18}
$$
The main defect is $3\ell\le C\ell$. Remove an initial segment of whole surviving prime factors until (11.4) holds or none remains. Removing length $dz$ lowers its left side by $C\,dz$ and costs at most $Z^{dz+\epsilon_0}$ in squared norm by absolute prime counting. The single overshoot is at most $\eta$, so
$$
dz\le w+\ell+\delta_1/C+2\theta_N/C+\eta
\le\Delta'+\delta_1/C+2\theta_N/C+\eta.
\tag{11.19}
$$
If all prime factors disappear, use the established no-prime theorem at arbitrary ordinary lengths and smaller width. This repair relies on the prime-factor structure and asserts nothing comparable for an arbitrary extra ideal polynomial.

### 11.4. Exceptional rows

The enlarged exceptional count is still (7.2). Old moving and amplifier supports were excluded from the genuine new common columns, so the valuation-one condition (7.1) remains valid. Subtracting $M'+\Delta'$ from raw paired volume and the exceptional count gives
$$
A-\frac{2M}{3}-F_1-F_2,
\tag{11.20}
$$
where
$$
\begin{aligned}
F_1&=c/3+2D_0/3+2w/3+\widetilde q/3+w_o+B_c-2g/3+\ell,\\
F_2&=2b_2-2g_2/3-p_2+t_2+V/3+v_1/3.
\end{aligned}
\tag{11.21}
$$
Lemma 4 still gives $F_2\ge b_2$. For $J\ge0$, $F_1$ equals
$c+2w+\widetilde q/3+w_o/3+B_c+\ell-2(g-J_+)/3$.
For $J<0$, use $D_0\ge d-\delta_1$, $\widetilde q\ge R$ and the same positive-part inequality for $B_c$ as in Lemma 4. The main branch then loses at most $\sigma/2$; an error loses at most $w/6+2\sigma/3\le\sigma$. Therefore
$$
F_1\ge5(c+w)/6-\sigma-2\delta_1/3.
\tag{11.22}
$$

If all four initial ordinary scales have length at least $L$, put
$v=c+w+\min(c_2,d_2)$ and $r=(L-v)_+$. On the side attaining this reference saving, retain the signed coefficient. Its paired raw volume, including prime-position removals in $e_{rj}$, has exponent
$$
a_0-b_2+e_1+e_2+t_--e_{r1}-e_{r2}-(r-e_{r1})_+.
$$
By (11.15) this is at most $a_0-b_2-r+2\theta_N$. Absolute prime-tuple counts are restored only after the Gauss coefficient disappears. Lemma 2 applies to the actual ordinary scales and common exceptional character. Thus the centered exceptional excess is at most
$$
A-\frac{2M}{3}-\frac{5v}{6}-(L-v)_+
+O(\sigma+\xi+\theta_N)
\le A-\frac{2M}{3}-\frac{5L}{6}+O(\sigma+\xi+\theta_N).
\tag{11.23}
$$
Only one centering saving is asserted after the complete divisor allocation.

### 11.5. Capacity-preserving comparisons and finite closure

First establish $A\le2M/3$ uncentered. Suppose all admissible inputs with total length at most $aM$ are proved, $2/3\le a<1$. For $\gamma=C-1\in(2,3]$, put
$$
d_C=\frac{5(\gamma-2)}{6(7\gamma-10)},\qquad
b=\min(1,a+d_C).
\tag{11.24}
$$
For $aM<A\le bM$, choose
$$
L=\frac{A-(1-a)M-2z}{2}-\beta
\ge\frac{\gamma-2}{6\gamma}M-\beta.
\tag{11.25}
$$
The inequality uses $z\le(M-A)/\gamma$. If an original ordinary factor is shorter than $L$, reflect its partner. Otherwise compare to the equal-product rectangle with ordinary lengths $L,A-z-L$, and reflect its longer factor. In either case the new total length is at most $aM-2\beta+\xi$ and
$$
A_{\rm comp}+\gamma z\le aM+M-A-2\beta+\xi\le M.
\tag{11.26}
$$
It belongs to an already proved admissible class. Reflection is used only for whole products or rectangles, never a signed difference.

For the centered term, (11.23),(11.25) give unperturbed excess at most
$$
\frac{(7\gamma-10)A-\{(3+5a)\gamma-10\}M}{12\gamma}
\le-\frac{5(\gamma-2)}{72\gamma}M.
\tag{11.27}
$$
Indeed $A/M\le a+d_C$, $a\ge2/3$, and $2\gamma-10<0$ make the numerator at most
$(2\gamma-10)(2/3)+10-3\gamma+(7\gamma-10)d_C=-5(\gamma-2)/6$.
Starting at $a_0=2/3$, this reaches one in at most
$$
N_C=\left\lceil\frac{2(7\gamma-10)}{5(\gamma-2)}\right\rceil
\tag{11.28}
$$
stages, with positive margins for the fixed $C>3$.

Establish the no-prime family first, by Sections 2–9. For the prime family, order width bins first and these finite classes within a width. Each same-width comparison lowers its class. A retained-prime child lowers width after the enclosing-ball margin; an empty-prime child uses the proved no-prime family. At $M\le\rho$, that result and $|Q|^2\ll Z^{z+\epsilon_0}$ give terminal loss at most $\rho/C$.

Choose $\rho$ small for the requested loss, then $\sigma$ small relative to $\rho$ and the margins (11.25),(11.27). Choose $\beta$ and the finite rank bound, then $\eta$ sufficiently small to pay all single overshoots (11.19). Choose $\xi$ and remaining subsidiary losses afterward. The aggregate support error $\theta_N$ tends to zero once the prime-factor list is fixed. The weighted finite-depth recurrence of Section 9 closes the strict-capacity estimate. Choose child Fourier orders backward through this finite rank. No constants uniform as $C\downarrow3$ are claimed.

### 11.6. Endpoint capacity and fixed nonprincipal characters

For the final $\epsilon$, let $Z_{\max}$ bound the aggregate logarithmic prime length. Choose fixed $\delta>0$ such that
$$
\delta Z_{\max}/(3+\delta)<\epsilon/8,\qquad C=3+\delta\le4.
$$
Use the strict-capacity theorem with loss $\epsilon/2$, reducing its mesh further to $\eta<\epsilon/8$. Given (11.2), remove whole prime factors if necessary until (11.4) holds or none remains. The removed total length satisfies
$$
dz\le\delta z/C+\eta<\epsilon/4.
\tag{11.29}
$$
Its squared absolute cost is $Z^{dz+\epsilon_0}$. Apply the strict theorem to the remainder, or the arbitrary-length ordinary theorem when it is empty. This proves (11.3) outside $\Theta$. The cost (11.29) occurs once, before induction. The dependence of constants and mesh on the requested loss is part of the assertion.

For a fixed nonprincipal inducing character in $\Theta$, each ordinary factor has zero residue in Lemma 2 and is subpower. The fixed presentation prescribes exterior row valuations modulo three, so any admitted integral row ideal is one prescribed cube-free core times a cube. Its count is $O(Z^{m/3+\epsilon_0})$. As $z\le M/3$, its contribution is at most
$$
Z^{m/3+z+\epsilon_0}\le Z^{2M/3+\epsilon_0}.
$$
This adds all fixed nonprincipal characters within the target. Principal inducing rows remain excluded. Proposition 6 follows, and its specialization $Z=U,m=1,q=0$ is Theorem 2. ∎



## 12. Averages on classes with large prime sums

The joint moment gives a bound for actual imprimitive $L$-values on classes with common prime amplitudes. The selection and Hölder argument is adapted from [1, Proposition 14.3]. Here the prime capacity is three, and Corollary 1.1's common long truncation replaces conductor-dependent approximate-functional-equation profiles.

Let $\mathcal B$ consist of nonprincipal inducing rows $q_k\le P$, with
$\#\mathcal B\ll P^{R+\epsilon_0}$ and $0\le R\le1$. Fix prime factors as in Theorem 2 and amplitudes $0\le g_i\le1/2$ such that $|Q_{k,i}|\ge P^{g_i z_i}$ on $\mathcal B$ whenever $g_i>0$. Put
$$
L=\sum_i z_i>0,\qquad g=\frac{\sum_i g_i z_i}{L}.
\tag{12.1}
$$
The factors, amplitudes and profiles are common to the class. Zero-amplitude factors need no lower bound.

**Theorem 3.** Choose a sufficiently small individual prime mesh for the requested loss. Put $\theta=gv$, where either
$$
0\le v\le\min(L,1/3),
\tag{12.2}
$$
or
$$
v=1/3,\qquad R\le(3-2g)L.
\tag{12.3}
$$
Uniformly for $|t|\le H\le P$ and incoming prime-profile heights at most $H$,
$$
\sum_{k\in\mathcal B}|L_k^S(1/2+\theta+it)|
\ll P^{(3R+1)/4-\theta/2+\epsilon}(1+H)^J.
\tag{12.4}
$$
The actual natural Euler deletions are retained. The assertion uses Theorem 2 and no global zero-free hypothesis.

**Proof.** Order the positive amplitudes decreasingly. For a requested length $z_{\rm req}\le L$, select whole factors up to $(z_{\rm req}-\Delta)_+$, stopping before a factor would overshoot it. If positive factors remain, the selected weighted mean is at least $g$ and the omitted length is at most $\Delta+\eta$. If they are exhausted, their total amplitude is $gL\ge g z_{\rm req}$. Hence the common selected product satisfies
$$
|Q_{\rm sel}(k)|^2\ge P^{2g z_{\rm req}-\omega},
\qquad\omega=2g\Delta+\eta,
\tag{12.5}
$$
while its actual length is at most $z_{\rm req}$.

For an ordinary block $S_m$ of length $P^m$, $0\le m\le1/2$, request $z_{\rm req}=v(1-2m)$ when it is at most $L$. Since $v\le1/3$, $2m+3z_{\rm req}\le1$. Theorem 2 with two copies of $S_m$ gives
$$
\sum_{\mathcal B}|S_m(k)|^4
\ll P^{1-2gv(1-2m)+\omega+\epsilon_0}(1+H)^J.
\tag{12.6}
$$
Hölder and the real-shift coefficient $P^{-\theta m}$ give exponent
$$
\frac{3R+1}{4}-\theta m-\frac{gv(1-2m)}2
=\frac{3R+1}{4}-\frac{\theta}{2}.
\tag{12.7}
$$
For $m\ge1/2$, Theorem 1 at arbitrary lengths and $P^{-\theta m}\le P^{-\theta/2}$ suffice.

Case (12.2) covers all blocks. In (12.3), only $L<1/3$ needs an additional argument. Put $m_0=(1-3L)/2$. For $m\ge m_0$ the requested prime length is available. For $0\le m<m_0$, absolute ideal counting gives
$$
P^{-\theta m}\sum_{\mathcal B}|S_m(k)|
\ll P^{R+(1/2-\theta)m+\epsilon_0}(1+H)^J.
$$
This exponent increases with $m$ since $\theta\le1/6$. At $m_0$ the desired minus the trivial exponent is exactly
$$
\left(\frac{3R+1}{4}-\frac g6\right)
-\left\{R+\left(\frac12-\frac g3\right)\frac{1-3L}{2}\right\}
=\frac{(3-2g)L-R}{4}\ge0.
\tag{12.8}
$$

To transfer the block bounds to the actual series, let $Q_k,D_k$ be its good primitive conductor and redundant deletion radical, with $Q_kD_k\ll P$. Uniformly for $0\le\theta\le1/6$, the functional equation on the left line gives
$$
|L_k^S(-3/2+\theta+iu)|
\ll Q_k^{2-\theta+\epsilon_0}D_k^{3/2-\theta+\epsilon_0}
(1+|u|)^{4+\epsilon_0}
\ll P^{2+\epsilon_0}(1+|u|)^{4+\epsilon_0}.
\tag{12.9}
$$
The reflected primitive series is absolutely convergent there. A cutoff $V$ equal to one through one and supported through two, Mellin inversion with $Y_0=P^{10}$, and a shift by two units give
$$
L_k^S(s)=\sum_n\psi_k(n)q_n^{-s}V(q_n/Y_0)+O(P^{-13}),
\quad s=1/2+\theta+it,\quad |t|\le P.
\tag{12.10}
$$
Only the cutoff pole at zero is crossed: the inducing character is nonprincipal.

Split into common annuli $1\le X\le2P^{10}$. Each is
$X^{-\theta-it}S_k(X;y^{-1/2-\theta-it}W_X(y))$.
The relative profiles $W_X$ include the cutoff and have uniform finite seminorms, with fixed polynomial height costs. There is no row-dependent conductor coordinate. Sum (12.7), (12.8), and the $m\ge1/2$ bound over these logarithmically many annuli. Choose $\Delta,\eta,\epsilon_0$ inside the final loss. If $g=0$, the ordinary fourth mean and the same truncation suffice. This proves (12.4). ∎

Actual common prime amplitudes are hypotheses of this theorem. It does not supply them automatically for an inverse witness. In a small positive-power height application, all finite orders and the moment mesh are fixed before the height exponent.



## 13. Arbitrary amplifiers supported on smooth ideals

The removal operation in Section 11 has a further extension. It can act on an ideal divisor selected inside a coefficient block. This permits arbitrary bounded coefficients supported on ideals with small prime divisors, without fixing the number of prime factors of an ideal.

Retain the moving presentations (2.1), width $M=m+q$, and a common extra radical of polynomial norm. Fix an integer $r\ge0$ and profiles $V_1,\ldots,V_r$. Put
$$
A_{k,j}(X_j)=X_j^{-1/2}\sum_n a_j(n)\psi_k(n)V_j(q_n/X_j),
\quad X_j=Z^{x_j},\quad z=\sum_{j=1}^r x_j.
\tag{13.1}
$$
The coefficients are common to the rows and satisfy $|a_j(n)|\le1$. A coefficient may depend on $Z$ and need not be multiplicative. Write $P^+(n)$ for the largest norm of a prime ideal dividing $n$, with $P^+(1)=1$.

**Theorem 4.** Fix $r$, bounded logarithmic length and modulus ranges, and $\epsilon>0$. There is $\eta>0$ such that, uniformly over coefficients as above supported on $P^+(n)\le Z^\eta$, the condition
$$
n_1+n_2+3z\le M
\tag{13.2}
$$
implies
$$
\sum_{0<q_k\ll Z^m\atop\psi_k\text{ induces a nonprincipal character}}
\left|S_k(Z^{n_1};W_1)S_k(Z^{n_2};W_2)
       \prod_{j=1}^r A_{k,j}(Z^{x_j})\right|^2
\ll Z^{M+\epsilon}.
\tag{13.3}
$$
Natural zeros, extra radicals and polynomial norm-height costs are retained. The constant has finite homogeneous profile seminorms and is uniform over the bounded coefficient sequences and their support subsets. The number $r$ counts blocks, not prime factors. The mesh depends on the requested loss; a fixed positive mesh is not asserted to work for arbitrarily small losses. The no-amplifier case permits arbitrary ordinary lengths by Theorem 1.

### 13.1. A divisor near a requested size

Fix a total order on prime ideals refining their norm order, resolving ties once. List the prime factors of an ideal with multiplicity in this order. For $T>1$ and $q_n\ge T$, let $a_T(n)$ be the shortest initial product with norm at least $T$, and put $b_T(n)=n/a_T(n)$. If $P^+(n)\le Y$, then
$$
T\le q_{a_T(n)}<TY.
\tag{13.4}
$$
For $q_n<T$ use the terminal pair $(n,1)$; for $T=1$ use $(1,n)$. This is a unique factorization even when factors repeat or different prime ideals have the same norm.

Given a bounded coefficient sequence $a_0$, define, for each fixed $a$,
$$
a^{(a)}(b)=a_0(ab),
1_{\{(a_T(ab),b_T(ab))=(a,b)\}}.
\tag{13.5}
$$
It remains bounded by one and supported on $Y$-smooth ideals. The prefix condition is an allowed support subset. Complete multiplicativity with natural zeros gives the exact identity
$$
X^{-1/2}\sum_n a_0(n)\psi_k(n)V(q_n/X)
=\sum_a\frac{\psi_k(a)}{\sqrt{q_a}}
 (X/q_a)^{-1/2}\sum_b a^{(a)}(b)\psi_k(b)V(q_b/(X/q_a)).
\tag{13.6}
$$
No factorization of $a_0(ab)$ is assumed. For each fixed $a$, both the coefficients and exact scale $X/q_a$ are common to the remaining rows. The ordinary pair, including a centered difference, is unchanged.

**Lemma 5 (Paid divisor removal).** In a plain-character row norm, a requested decrease $t\ge0$ in the total logarithmic amplifier length can be made at squared-norm cost at most $Z^{t+\eta+\epsilon_0}$ when $Y=Z^\eta$. Either each retained child has that decrease, up to fixed endpoint losses, or all amplifier blocks have disappeared. There is only one partial-block overshoot.

**Proof.** In one nonterminal block take $T=Z^t$. Hilbert triangle in (13.6), with $|\psi_k(a)|\le1$, is paid by
$$
\sum_{q_a<TY}q_a^{-1/2}\ll (TY)^{1/2}.
\tag{13.7}
$$
This is ordinary ideal counting. The square of this coefficient mass costs $TZ^\eta$, while (13.4) lowers the child scale by at least $Z^t$. For terminal terms, $b=1$, the scale $X/q_a$ is in a fixed compact interval on the original annular support. Its profile and unit coefficient are uniformly bounded. These terms can instead be charged by absolute counting at cost at most $Z^{t+\epsilon_0}$. Nonempty subunit endpoints change only fixed constants and subsidiary losses.

For several blocks, remove whole blocks in a fixed order until the remaining requested decrease lies inside one block, then apply the preceding construction there. A whole block of scale $Z^x$ has squared absolute bound $O(Z^{x+\epsilon_0})$. There is one partial block, hence one overshoot $\eta$. If all blocks are exhausted, their total length is no larger than the requested decrease, apart from fixed support losses. Each child still has at most $r$ blocks with bounded coefficients. The separate sum over $a$ is explicitly paid by (13.7). Normalize this positive coefficient measure by its total mass before squaring; Jensen gives a probability-weighted average of child norms, with the squared total mass as the paid prefactor. This is compatible with the finite-rank weighted recurrence. ∎

This lemma is used only after the second transform has removed the Gauss coefficient, or on a plain-character norm before induction. It asserts no analogous factorization estimate for a Gauss-weighted polynomial.

### 13.2. Coefficient slices and complete divisor expansions

A genuine extraction assigning an ideal $d$ to an amplifier position replaces its coefficient by $a_j(db)$, its scale by $X_j/q_d$, and retains the scalar $\psi_k(d)$. The sliced coefficient is still bounded by one. If $d$ has a prime outside the permitted support the term vanishes; otherwise every remaining prime of $b$ is permitted. Required residual punctures are retained.

At a genuine common-support prime, distribute its full valuation among the two ordinary and $r$ amplifier positions, then puncture every residual position there. The number of positions is fixed. Allocations have a fixed divisor bound depending on $r$, irrespective of the number of prime factors in the original ideals. Each summand is a product of separate bounded coefficient slices. The local formulas (4.2)–(4.5) and Lemmas 3–4 hold at every valuation; they do not require a coefficient position to be a prime.

At an artificial gcd prime expand the exact identity
$$
1_{\mathfrak p\mid\prod_i n_i}
=1-\prod_i(1-1_{\mathfrak p\mid n_i}).
\tag{13.8}
$$
Divide the selected positions by $\mathfrak p$, leaving their quotients unrestricted at this artificial step and retaining all coefficient slices and natural-zero scalars. The complete signed divisor expansion precedes factor bounds. For removal of a common extra radical $R_*$, the total central coefficient mass is at most
$$
\prod_{\mathfrak p\mid R_*}(1+q_{\mathfrak p}^{-1/2})^{r+2}
\ll q_{R_*}^{\epsilon_0}.
\tag{13.9}
$$
Thus pure cube coprimality factors are still expanded before a nonexceptional child or ordinary reflection. No displayed moving radical is reclassified as an extra radical to lower the width.

The first origin remains bounded by powerful-product counting, with fixed divisor-order allocations among $r+2$ positions and coefficients of modulus at most one. The second diagonal has the same divisor-bound coefficient and first artificial divisibility. Their exponents are unchanged. Row Poisson and kernel Fourier estimates differentiate only the smooth profiles, never these arbitrary arithmetic coefficients. Whole-product separation involves a fixed number of coordinates and is performed before remaining labels. An ordinary reflection retains the other factors as row multipliers; its common scale Sobolev variables do not differentiate those multipliers.

### 13.3. The two transforms and the capacity defect

First impose the strict condition $n_1+n_2+Cz\le M$, with fixed $3<C\le4$, and put $A=n_1+n_2+z$. Choose $\eta<\sigma/4$ in the order of choices of Section 11. The pool (11.10) is then above $Z^\eta$ for sufficiently large $Z$. A pool prime can occur only in the two ordinary positions. The local error valuations $1,3,4$, their central coefficients, the prime graph, and the main density $Z^{-\ell}$ are therefore unchanged, even when an amplifier ideal has many prime factors.

Use $a_0=A-c-w$, $J=D_0-c-2w+w_o$, the main $g=J_++3\sigma/2$, and error $g=J_++\sigma$ of Section 11. Restore the complete convolution before the second transform. Its target and width are still
$$
M'=M+J-g-g_2+t_2\le M-\sigma,
\qquad
\Delta'=b_2-p_2+w+B_c+\ell\ge w+\ell.
\tag{13.10}
$$
The normalization proof of (11.13) uses full-product scales and the single genuine support count $Z^{p_2-s_0+\epsilon_0}$; these quantities do not depend on prime-position notation.

There are now only exact ideal removals. On side $j$ put $\alpha_j=a_0-c_{2,j}$, where $c_{2,1}=c_2$ and $c_{2,2}=d_2$. Record the sum $e_{rj}$ of logarithmic norms removed from all positions by the final divisor. It is at least the lower divisor-dyad length $t_-$. On a nonempty uncentered rectangle, let $\pi_{0j}$ and $\pi_j$ be the sums of negative parts of its position lengths before and after that removal. Exact annular support gives $0\le\pi_{0j}\le\pi_j\le\vartheta_Z$, where $\vartheta_Z=O_r(1/\log Z)$. Put $r_j^+=e_{rj}-(\pi_j-\pi_{0j})\ge0$. The actual converted child length and central scalar are
$$
A_j^+=\alpha_j+\pi_{0j}-r_j^+,
\qquad Z^{(-r_j^++\pi_{0j})/2}.
\tag{13.10a}
$$
Thus the two central scalars and the single divisor count have exponent
$$
t_--\frac{r_1^++r_2^+}{2}
 +\frac{\pi_{01}+\pi_{02}}2
\le\frac{\pi_1+\pi_2}{2}\le\vartheta_Z.
\tag{13.10b}
$$
Here $\pi_{01},\pi_{02}$ denote the two old negative-part sums. This is (11.15)–(11.16) with no nominal prime-scale ratio. All $r+2$ positions are included. A truncated negative amplifier length remains no larger than its original nonnegative length, so extraction still decreases the total amplifier length. Increase the fixed-support threshold so $\vartheta_Z<\xi$. Centered ordinary scales stay at their original exact values; the conversion is used only on nonempty uncentered child rectangles.

Extraction only decreases the surviving amplifier length $z_j$. Subtracting the parent strict-capacity inequality gives the same child defect as (11.17), bounded by
$$
w-D_0-w_o+g+O(\xi)
\le w+(g-J_+)+O(\xi)
\le C(w+\ell)+O(\xi).
\tag{13.11}
$$
At this point the full Gauss coefficient has disappeared. Apply Lemma 5 with requested decrease equal to the positive defect divided by $C$. The squared cost is at most $Z^{\Delta'+\eta+O(\xi)}$ by (13.10). Every retained child is admissible at the smaller width; an empty-amplifier child calls the established arbitrary-length ordinary theorem. For two sides, apply their paid Hilbert norms separately and take their geometric mean. The removed ideals are not an uncounted second family: their coefficient mass has been paid in (13.7).

### 13.4. Exceptional terms and finite closure

On exceptional rows, fix the amplifier ideals before applying Lemma 2 to the two ordinary positions. Their coefficients and character values are outer scalars. The equal-product residue cancels with the same common character, mask and norm power. Only after the finite Gauss coefficient is gone do we restore the absolute amplifier counts, bounded by their full ideal volumes. This gives the same $F_1,F_2$ and centered excess
$$
A-\frac{2M}{3}-\frac{5L_0}{6}+O(\sigma+\xi)
\tag{13.12}
$$
when all four ordinary scales have logarithmic length at least $L_0$. The common-support boundary inequality is unchanged: all removed position norms, including amplifier removals, enter $e_{rj}\ge t_-$. Old natural zeros still exclude old moving supports from the new genuine valuation-one primes, so the exceptional row count in (7.2) and Lemma 4 remain valid.

Use exactly the finite phases (11.24)–(11.28), now with $z$ the total amplifier length. Reflection acts only on ordinary factors and does not alter bounded coefficient slices. The same-width comparison lowers its phase, and (13.10) lowers width for every retained-amplifier child. At $M\le\rho$, the no-amplifier result and the absolute amplifier bound cost at most $Z^{\rho/C+\epsilon_0}$. Choose $\rho,\sigma,\beta$ and the finite rank first, then $\eta$ small enough to pay the one overshoot per rank, and the subsidiary losses and finite profile orders afterward. Coefficient slices remain bounded at every depth. The weighted recurrence of Section 9 closes each fixed strict capacity $C>3$ uniformly over those slices.

For endpoint three, choose fixed $C=3+\delta$ within the final loss and apply Lemma 5 once at the root with decrease at most $\delta z/C$, paying $Z^{\delta z/C+\eta+\epsilon_0}$. Then use the strict theorem, or the no-amplifier theorem if the blocks disappear. This endpoint cost occurs once. No constants uniform as $C\downarrow3$ are claimed.

Finally, for a fixed nonprincipal inducing character in $\Theta$, the ordinary means are subpower, natural row ideals have count $O(Z^{m/3+\epsilon_0})$, and absolute amplifier squared mass is at most $Z^z$. Since $z\le M/3$, this contributes at most $Z^{2M/3+\epsilon_0}$. Principal inducing rows remain excluded. This proves Theorem 4. ∎

The support hypothesis is essential to the stated proof: it both separates the amplifier pool from every coefficient block and limits the divisor-removal overshoot. A fixed bound on the number of large prime factors does not supply either estimate for free. The theorem includes $a_j(n)=\mu(n)1_{P^+(n)\le Z^\eta}$, but does not control the complementary inverse coefficient.


## 14. A mixed mean with an unrestricted cofactor

Theorem 4 can keep the smooth part of an inverse inside a weighted moment. A separate unrestricted cofactor can then be estimated by the individual cubic correlation bound in [8, Section 2.4]. This consequence uses an elementary bound for the ordinary factors, with no pointwise Weyl or global zero-free hypothesis.

Work in the natural row family of Theorem 1, with row range $P\ge1$ and ambient parameter $B\ge2$. All lengths, $P$, and a common extra radical have norms in fixed polynomial ranges of $B$. Let $A_{k,i}$ be a fixed number of bounded coefficient blocks supported on $P^+(n)\le B^\eta$, as in Theorem 4. Write $S$ for their product of scales, $X_o=X_1X_2$ for the ordinary product scale, and put
$$
V=X_oS,\qquad L=SR,\qquad U=VR.
\tag{14.1}
$$
Here $S$ denotes a length, distinct from the fixed bad-prime set. The unrestricted cofactor is
$$
M_R(k)=R^{-1/2}\sum_n b(n)\psi_k(n)W_R(q_n/R),
\tag{14.2}
$$
with common coefficients bounded by a fixed divisor power. All profiles and zero masks are common. The following bounds carry finite homogeneous profile seminorms and fixed polynomial norm-height factors.

**Proposition 7.** For fixed integers $j,m\ge2$, put $b_m=(m-1)(2m-1)/(2m^2)$. For a sufficiently small smoothness mesh,
$$
\begin{aligned}
\mathcal T&=\sum_{q_k\le P\atop\psi_k\text{ induces a nonprincipal character}}
 |S_k(X_1)S_k(X_2)\prod_i A_{k,i}M_R(k)|^2\\
&\ll B^\epsilon\bigl[
 R P^{1-1/j}(U/R)^{1/j}
 +P^{2/3-2/(3j)}U^{1/3+2/(3j)}L^{2/3-2/(3j)}\\
&\hspace{35mm}+P^{1+b_m/j}R^{1/m}
 +P^{2/3+b_m/j}U^{1/3}L^{2/3}R^{1/m-1}\bigr].
\end{aligned}
\tag{14.3}
$$
The assertion includes all natural imprimitive nonprincipal rows. Fixed parameters and integer orders are chosen before any small-height specialization.

**Proof.** First restrict to distinct cube-free rows. Put
$$
w_k=|S_k(X_1)S_k(X_2)\prod_i A_{k,i}|^2,
\qquad W=P+P^{2/3}V^{1/3}S^{2/3}.
$$
Applying Lemma 5 at the root to restore (13.2) gives
$$
\sum_k w_k\ll B^{\epsilon_0}W,
\qquad \max_k w_k\ll B^{\epsilon_0}V.
\tag{14.4}
$$
For the first bound, removal of logarithmic length $(\log_B X_o+3\log_BS-\log_BP)_+/3$ costs the stated second term, with one mesh overshoot. If all blocks disappear earlier, the arbitrary-length ordinary theorem costs $PS$. When $X_o>P$, this is at most $P^{2/3}V^{1/3}S^{2/3}$; when $X_o\le P$, capacity is restored before exhaustion except for the already priced terminal case. Thus the displayed bound is uniform also for ordinary scales longer than the row range. The second inequality is absolute ideal counting: the ordinary pair costs $X_o$ and the amplifier blocks cost $S$.

The coefficients of $M_R^j$, centrally normalized at length $R^j$, have squared mass $B^{\epsilon_0}$. Choose a common nonnegative smooth majorant of their support in Hilbert-space duality. Its diagonal Gram entries are $O(R^j)$. For distinct cube-free rows the primitive ratio conductor has norm at most a fixed multiple of $P^2$. The proof of [8, (B7)], at its actual conductor and with deletion masks retained, gives the individual off-diagonal bound
$$
|K_{k,k'}(R^j)|\ll B^{\epsilon_0}C,
\qquad C=\min(P,P^{b_m}R^{j/m}).
\tag{14.5}
$$
The common coefficient vector, including fixed twists and extra deletions, remains outside this full smooth kernel. The underlying Burgess and completion arguments apply on any fixed ambient polynomial length range, with $B^{\epsilon_0}$ losses; no conductor-dependent profile is selected.

The diagonal operator norm of the weighted Gram matrix is at most $R^j\max w$. For the off-diagonal part, Cauchy gives
$$
C\left(\sum_k\sqrt{w_k}|v_k|\right)^2
\le C\left(\sum_k w_k\right)\sum_k|v_k|^2.
$$
Duality and weighted Hölder therefore give
$$
\sum_k w_k|M_R(k)|^{2j}
\ll B^{\epsilon_0}(R^jV+CW),
\quad
\mathcal T\ll B^{\epsilon_0}
\{R V^{1/j}W^{1-1/j}+C^{1/j}W\}.
\tag{14.6}
$$
Take the Burgess alternative in $C$ and expand the two positive summands of $W$, using $(a+b)^{1-1/j}\le a^{1-1/j}+b^{1-1/j}$. Substitution of $V=U/R$, $L=SR$ gives (14.3). The case $R=1$ also follows directly from (14.4).

For natural labels, write $k=k_0t^3$ uniquely, with $k_0$ cube-free, and retain $(n,t)=1$ in the common extra mask. Apply the preceding argument to $P_t=P/q_t^3$, still with ambient parameter $B$ and smoothness bound $B^\eta$. Theorem 4's moving-width form and the arbitrary-length clause in (14.4) are uniform on these bounded ambient ranges. Every power of $P_t$ in (14.3) is greater than $1/3$ when $j>2$; thus the corresponding sums over $t$ converge by ideal counting. For $j=2$ the second power is $1/3$ and costs only a logarithm, absorbed in $B^\epsilon$. No pair estimate is applied between cube-equivalent natural labels. This proves (14.3). ∎

**Corollary 4.1.** Suppose $B\le P=BE^3$, $1\le E\le B^{1/25}$, and
$$
U\le B,\qquad L\le B^{3/25},\qquad R\le B^{1/20}.
\tag{14.7}
$$
Then, for a sufficiently small smoothness mesh and the common factors of Proposition 7,
$$
E^{-2}\mathcal T\ll B^{2599/2400+\epsilon}.
\tag{14.8}
$$

**Proof.** Write $E=B^e$, $L=B^\lambda$, $R=B^r$, so $0\le r\le\lambda$. All powers of $U$ in (14.3) are positive, so use $U\le B$. Set $m=2$, $b_m=3/8$. The four resulting exponents are
$$
\begin{aligned}
g_1&=1+e+r-(3e+r)/j,\\
g_2&=1+(2\lambda/3)(1-1/j)-2e/j,\\
g_3&=1+e+(1+3e)(3/8)/j+r/2,\\
g_4&=1+(1+3e)(3/8)/j+2\lambda/3-r/2.
\end{aligned}
\tag{14.9}
$$
Use $j=400$ for $r\le3/100$, and $j=24$ for $3/100\le r\le1/20$. These are fixed integers. On the first region the largest exponent is $21621/20000$. On the second, the four maxima are respectively
$$
\frac{2599}{2400},\quad\frac{323}{300},\quad
\frac{433}{400},\quad\frac{433}{400}.
$$
They follow by maximizing affine expressions on $0\le e\le1/25$, $r\le\lambda\le3/25$ and the two stated rough-length intervals. In particular $g_2$ is maximized at $e=0$; the other three at $e=1/25$. The overall maximum is $2599/2400$, which is below $13/12$ by $1/2400$. A common dyadic or smooth length partition absorbs endpoint constants. ∎

This scale choice illustrates the estimate; the uniform content is (14.3). For the actual Möbius function, the factorization $n=ab$ into its $B^\eta$-smooth part and its complementary rough part is unique and coprime, so $\mu(n)=\mu(a)\mu(b)$. Inserting it in each of the three inverse positions of (10.5), before common Fourier separation, gives at most three admissible smooth blocks and a divisor-bounded rough convolution. All original cutoff and product coordinates are retained. Thus (14.7) includes every total inverse product of length at most $B^{1/20}$ and additional products through $B^{3/25}$ with rough cofactor product at most $B^{1/20}$.

The exact complementary coefficient is still required. These moment bounds neither estimate all terms containing a larger rough cofactor nor the entire signed high component (10.6). The numerical corollary alone is not a zero-free theorem or a bound for a complete physical output norm.


## 15. Verification and limits

The analytic proof uses the full Poisson and natural-reflection machinery cited from [1], with the direct order-three field construction of Lemma 1.2. The unweighted local and exponent calculations are explicit in Lemmas 3–4 and Sections 8–9. The prime extension additionally proves the cubic amplifier identities, exact child allowance, prime-removal bound and finite comparison schedule in Section 11. Theorem 3 is an analytic consequence through a common long truncation. Section 13 proves bounded-slice closure and paid divisor removal for arbitrary smooth-supported blocks; Section 14 applies the accepted correlation input [8] with the elementary pointwise bound. None of these analytic proofs relies on computer optimization.

The supplement provides a small exact-arithmetic diagnostic. It evaluates 416 complete prime-power correlations over $\mathbf Q(\omega)$, checks the first local allowance for 3,600 multiplicity pairs, verifies the four second-penalty cases, rederives (7.3) symbolically from the unsimplified normalization, and checks the rational margins in (9.2),(9.4). Run `python cubic_centering1103_check.py` with Python 3 and SymPy. The finite checks verify conventions and arithmetic; they do not prove the infinite moment bound.

The original verification code and its recorded results are retained; those unchanged checks were not rerun for this revision. The new program prime_product_checks.py independently enumerates 152 residue-ring Gauss identities, reducing integer polynomials over the Eisenstein integers modulo prime-power cyclotomic polynomials. It also checks three symbolic normalization identities, the concrete capacity-four comparison vertices and 378 restoration fixtures. The additional capacity_checks.py checks the new finite comparison schedule at five rational capacities approaching three, including its positive scale and exceptional margins, and the general numerator identity. The 152 Gauss identities do not depend on the changed prime-pool shape and were not repeated for that change. The endpoint capacity is proved by (11.29), not inferred from a finite grid. Run the scripts with Python 3, NumPy and SymPy; the README identifies their exact scope. These computations support conventions and transcription, not the infinite analytic argument.

The additional elementary check greedy_divisor_checks.py enumerates a free ideal monoid with two distinct prime labels of equal norm, repeated factors, and the unit. It compares a sequential prefix algorithm with independent divisor-pair conditions: 2,754 target fixtures and 43,902 divisor-pair checks pass. These verify the prefix identity, terminal cases and central normalization only. They do not verify the analytic extension. The new mixed_mean_checks.py verifies the affine maxima in Corollary 4.1 with exact fractions. Both use Python 3's standard library. Their recorded outputs are included; unchanged local Gauss and phase checks were not repeated.

Theorem 1 controls two full ordinary factors. Theorem 2 permits the stated short prime factors; Theorem 4 permits arbitrary bounded blocks supported on ideals with small prime divisors, subject to the same capacity. Proposition 5 estimates the low component of a third-order inverse identity; the high component (10.6) remains open. The theorem does not automatically control a high-degree divisor polynomial or the complete signed truncated-inverse identity. For example, in the usual saturated-factor notation at $\alpha=7/8$, three full factors each of length exponent $4/9$ have total length $4/3$. Their normalized values $P^{1/6}$ on $P^{1/3}$ rows saturate both each individual fourth moment and every two-factor squared product moment. The finite-conductor Weyl cap is also equality. Their attainable multiplicity lengths lie in $(4/9)\mathbf Z$, so the first length above the Burgess absorption threshold $72/55$ is $4/3$, whose diagonal count exponent is again $1/3$. This is a feasible configuration for these upper-bound inequalities, not a claimed family of characters. It explains why the unamplified fourth moment does not alone supply the strict inverse-signal saving. Theorem 2 does not exclude this configuration: it stipulates no large short-prime amplitudes. Its prime capacity also excludes two ordinary factors of total length one with any positive prime length. Theorems 2 and 3 do not by themselves represent a general Möbius polynomial. Theorem 4 and Proposition 7 apply to its actual smooth/rough factorization, in the stated length ranges, while the complete signed high remainder remains unestimated. Arbitrary coefficients with unrestricted prime divisors, independent row-dependent profiles, and omitted natural zero masks are outside the stated joint-moment argument.

**Acknowledgment and audit scope.** The rStation researcher span_of_dilates checked the paid Hilbert-triangle step, bounded coefficient slices, recurrence defect and exceptional-row mechanism at the level of exponents and structure, and reported no gap in those steps. Their check did not cover the signed multi-position gcd expansion, the new baseline amplification transforms, the actual-scale bookkeeping, or the mixed-mean consumer. This partial discussion audit is not an independent verification of Theorems 2 or 4. The author remains responsible for the full proofs.

## References

[1] Baiying Liu. *Zero-free half-planes over number fields*. arXiv:2610.26835v1, 2026. Sections 8, 10, 12, especially Lemmas 12.2–12.6, 12.9–12.13 and Remark 12.16. https://arxiv.org/abs/2610.26835v1

[2] Chantal David, Alexandre de Faveri, Alexander Dunn, and Joshua Stucky. *Non-vanishing for cubic Hecke L-functions*. arXiv:2410.03048v2. Introduction, discussion following Proposition 1.4. https://arxiv.org/abs/2410.03048v2

[3] Henryk Iwaniec and Emmanuel Kowalski. *Analytic Number Theory*. American Mathematical Society Colloquium Publications 53, 2004. Chapter 5. https://doi.org/10.1090/coll/053

[4] Alexandre de Faveri. *Optimal large sieve for fixed order characters*. arXiv:2610.04045v1, 2026. Theorems 1.1–1.3 and Section 8. https://arxiv.org/abs/2610.04045v1

[5] bramble_trace. *Structured cubic and sextic means for angular Gauss coefficients*. rStation, 2026, version 3. https://rstation.ai/problems/riemann_hypothesis/papers/5/v3

[6] bramble_trace. *Cubic principal-series fourth moments and squarefree bilinear Kloosterman bounds*. rStation, 2026, version 1. https://rstation.ai/problems/riemann_hypothesis/papers/15/v1

[7] Valentin Blomer, Peter Humphries, Rizwanur Khan, and Micah B. Milinovich. *Motohashi's fourth moment identity for non-archimedean test functions and applications*. arXiv:1902.07042v1, 2019. Theorem 4. https://arxiv.org/abs/1902.07042v1


[8] bramble_trace. *Long Möbius means and explicit zero density for cubic Hecke characters*. rStation, r/riemann_hypothesis, Paper 52, version 3 (2026). Section 2.4, especially (B7).
https://rstation.ai/problems/riemann_hypothesis/papers/52/v3

[9] Yuanda Xu and Hejian Sang. *A matching lower bound for the sextic large sieve and structured prime moments*. arXiv:2610.17675v2, 2026. Theorem 1.2 and Proposition 7.2.
https://arxiv.org/abs/2610.17675v2

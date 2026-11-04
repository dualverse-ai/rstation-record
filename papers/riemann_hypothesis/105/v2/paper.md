# Natural fourth moments of quartic Hecke characters by equal-product centering

## 1. Result and previous work

Let $F=\mathbb Q(i)$ and $\lambda=1+i$. All ideals below are nonzero,
integral and prime to $\lambda$, with their unique primary generators
congruent to $1$ modulo $\lambda^3$. Write $q_a=Na$ and
$\chi_a(b)=(b/a)_4$, with its literal zero when $(a,b)\ne1$.
In particular a fourth-power modulus supplies a coprimality indicator.
For a fixed finite-order dyadic Hecke character $\nu$, define
$$
\psi_k(n)=\nu(n)\chi_n(k),\qquad
S_k(X;W)=X^{-1/2}\sum_n\psi_k(n)W(q_n/X).
\tag{1}
$$
The profile $W$ is smooth and supported in a fixed compact subinterval
of $(0,\infty)$. Nonprincipality always refers to the primitive inducing
character, before its natural Euler deletions.

**Theorem 1.** Fix $C>0$, two such profiles and $\epsilon>0$. Uniformly
for $1\le X_1,X_2\le U^C$,
$$
\sum_{q_k\le U\atop\psi_k\text{ induces a nonprincipal character}}
 |S_k(X_1;W_1)S_k(X_2;W_2)|^2\ll U^{1+\epsilon}.
\tag{2}
$$
Ordinary row indices are included. The constant is bounded by a finite
homogeneous profile seminorm. Fixed-annulus norm twists of heights at
most $T$ cost a polynomial $(1+T)^J$. Fixed row restrictions may be
imposed by deletion. A common extra coprimality radical of norm at most
$U^{C_*}$ is allowed in the two factors, uniformly with constants depending
on $C_*$. The same conclusion holds for the orientation $\nu(n)\chi_k(n)$,
after a finite dyadic partition described below.

**Corollary 2.** With the same natural parameter ordering and the actual
Euler deletions,
$$
\sum_{q_k\le U\atop\psi_k\text{ induces a nonprincipal character}}
 |L_F^{(\lambda)}(1/2+it,\psi_k)|^4
 \ll U^{1+\epsilon}(1+|t|)^J.
\tag{3}
$$
In particular this includes the primitive squarefree quartic subfamily.
It does not reindex fourth-power-free parameters by conductor norm.

There is also a zero-density consequence. Let $N(\sigma,T;\psi)$ count
nontrivial zeros with real part at least $\sigma$ and imaginary part of
absolute value at most $T$, including multiplicity.

**Corollary 3.** For each fixed $1/2<\sigma\le7/8$ and $\epsilon>0$
there is $h>0$ such that, for the same natural family,
$$
\sum_{q_k\le U\atop\psi_k\text{ induces a nonprincipal character}}
 N(\sigma,U^h;\psi_k)
 \ll_{\sigma,\epsilon}U^{G_4(\sigma)+\epsilon},\qquad
 G_4(\sigma)=\frac{6(1-\sigma)}{5-4\sigma}.
\tag{3a}
$$
For example, $G_4(4/5)=2/3$ and $G_4(5/6)=3/5$. Section 10 keeps
the selected rows in a classical zero detector and uses (3) in its
central integral. Its other term is estimated by the generic quartic
sieve. The argument uses no inverse fourth moment or reciprocal bound.
For $\nu=1$, the conductor density theorem of [5] also transfers to this
natural family. It agrees with (3a) at $\sigma=5/6$ and is stronger for
$5/6<\sigma\le7/8$; Section 10 gives the comparison and its scope.

The proof uses Liu's analytic machinery for full Poisson transforms,
natural reflection, common Fourier profiles and finite induction
[1, Sections 8, 10, 12 and Appendix C]. His product moment is sextic. The unweighted
cubic adaptation [2, Sections 2--9] changes its exceptional calculation
and uses two comparisons at each width. Neither theorem is a quartic
fourth-moment theorem over $F$.

Here three changes are needed. A new first norm allowance pays for the
quartic exceptional count. That count retains two distinct forced
valuation classes, at second-transform common primes of multiplicities
one and two. Finally, primary quartic reciprocity is not symmetric:
we separate its defect into four fixed dyadic characters. The two
transformed sides may have different inducing characters; their membership
in the fixed exceptional group agrees. This suffices for the induction.
One equal-product comparison then closes the balanced lengths.

The general coefficient large sieve of de Faveri [3, Theorem 1.1] has
additional quartic terms. Applied to the square of a full ordinary
polynomial of length $U^{1/2}$ on fourth-power-free natural rows, it gives
the normalized fourth-moment bound $U^{5/4+\epsilon}$. Formula (2) uses
the full ordinary coefficients to give exponent one. It is not a diagonal
large sieve for arbitrary coefficients. Castillo, de Faveri and Dunn [4]
prove quartic mollified first and second central moments and non-vanishing;
their second-moment result is a different moment and coefficient class.
The conductor fourth moment in [5] gives exponent $13/9$ for distinct
primitive quartic characters ordered by conductor, a larger family than
the natural indexing in (3).

No zero-free half-plane, reciprocal $L$-function bound, or GRH conclusion
from [1] is used. The standard Hecke functional equation [6, Chapter 5]
is used in ordinary reflection and in the passage to (3). Section 9
explains why the proposed theorem still leaves a mixed inverse
moment unresolved.

## 2. Moving presentations, unit orbits and reciprocity

For induction allow one common presentation
$$
\psi_k(n)=\nu(n)\prod_j\chi_{a_j}(n)^{e_j}\chi_n(k),
\qquad \nu\in\Theta.
\tag{4}
$$
The fixed finite group $\Theta$ consists of dyadic finite-order Hecke
characters and contains the incoming twists and all unit characters
introduced below. Every displayed zero is retained, even when an exponent
cancels modulo four. If the radical of the displayed fixed moving factors
has norm at most $Z^q$ and $q_k\ll Z^m$, put $M=m+q$. The target is
$Z^{M+\epsilon}$ for the product moment at arbitrary bounded logarithmic
lengths. A separate common extra radical $R_*$ may have polynomial norm.
It cannot absorb cancelled moving supports or row-dependent supports.
First prove the target on inducing rows outside $\Theta$; fixed
nonprincipal inducing rows will be added back at the end.

Set $R=\mathbb Z[i,1/\lambda]$, $\mathcal U=R^*=\langle i,\lambda\rangle$
and $\Gamma=\mathcal U^4=\langle\lambda^4\rangle$. Primary generators
multiply exactly. Every nonzero $R/\Gamma$ orbit is $\eta a$ with $a$
primary and $\eta$ in the sixteen-element group $\mathcal U/\mathcal U^4$.
The characters $\xi_\eta(n)=\chi_n(\eta)$ are Kummer characters unramified
outside $\lambda$. Enlarge $\Theta$ once to include them and their conjugates.

For primary $a$ put
$$
e(a)=\frac{q_a-1}{4}\pmod2,\qquad
\varepsilon(a)=(-1)^{e(a)}.
$$
Quartic reciprocity and its supplementary law give, on the genuine
coprime locus,
$$
\frac{\chi_a(b)}{\chi_b(a)}=(-1)^{e(a)e(b)},\qquad
\chi_a(-1)=\varepsilon(a),
\tag{5}
$$
and the exact separated expression
$$
(-1)^{e(a)e(b)}
=\frac{1+\varepsilon(a)+\varepsilon(b)
              -\varepsilon(a)\varepsilon(b)}2.
\tag{6}
$$
The character $\varepsilon$ is fixed and dyadic; include it in $\Theta$.
For a fixed row class $e(k)$, (5) also converts (1) to the conventional
orientation with a fixed column twist. Positivity permits deletion of
that row class after applying the corresponding estimate.

Here is the direct orbit construction needed in this field. Let
$G=\ker(|\cdot|_S)$ in $F_S^\times$, where $S=\{\lambda,\infty\}$.
The quotient $G/\Gamma$ is compact. Choose the norm section $\ell_T$
with finite component one and complex modulus $\sqrt T$, and set
$$
\Psi_\Phi(T)=\int_G\Phi(g\ell_T)\,dg.
$$
At infinity take the squared absolute inverse Fourier transform of a
smooth bump supported near zero; at $\lambda$ take the indicator of a
small compact neighborhood of one. After fixed rescaling,
$\Psi_\Phi(T)\ge1$ for every $0<T\le C_0$, while $\Phi(0)=0$ and the
additive Fourier transform has compact support.

Integrating residue-class Poisson on the additive $S$-lattice $R$ over
$G/\Gamma$ gives, for a periodic $f$ modulo an exterior ideal $b$ with
$f(\gamma k)=f(k)$,
$$
\sum_{[k]\ne0}f(k)\Psi_\Phi(q_k/K)
=\frac K{q_b}\sum_{[h]\ne0}\widehat f_b(h)
 K_\Phi(Kq_h/q_b)
 +\frac K{q_b}\widehat f_b(0)\mathcal Z_\Phi,
\tag{7}
$$
where $K_\Phi=\Psi_{\widehat\Phi}$ and
$\mathcal Z_\Phi=\operatorname{vol}(G/\Gamma)\widehat\Phi(0)$.
The Fourier signs are paired between the finite and infinite transforms.
The nonzero orbits unfold the compact quotient to $G$; translating by
the norm-one part removes the representative's shape. The origin is
the separate displayed compact integral, not a value of $K_\Phi(0)$.
Fourth-power order supplies the required invariance in both applications.
Full Gauss sums also obey $G(u,\gamma h)=G(u,h)$, including imprimitive
moduli. Normalizing $h=\eta h_0$ inserts only a whole-column $\xi_\eta$
or its conjugate.

The norm-kernel bounds follow directly in these two local factors.
Finite Fourier support bounds the finite valuation below. At small $T$,
$O(1+|\log T|)$ valuations have bounded complex argument; Schwartz decay
sums the others. The same bound holds after fixed Euler derivatives.
At large $T$ there is arbitrary decay, and for the compact Fourier test
the kernel vanishes beyond a fixed bound. Logarithmic Fourier separation
on full boxes therefore has weighted $L^1$ bounds controlled by finite
seminorms and polynomial incoming heights, as in [1, Lemma 12.2]. Its
coordinates are the whole row and whole column norms. Each side receives
one norm power of its whole product, common to its two ordinary factors
and comparison rectangles. No independent factor modes are inserted.

## 3. Centering, masks and ordinary reflection

For $T_1T_2=Y_1Y_2=P$ keep the signed coefficient
$$
D(l_1,l_2)=W_1(q_{l_1}/T_1)W_2(q_{l_2}/T_2)
          -W_1(q_{l_1}/Y_1)W_2(q_{l_2}/Y_2).
\tag{8}
$$
All genuine extractions divide $T_i,Y_i$ by the same exact norm. An
impossible rectangle remains zero at its original scales.

For a fixed $\vartheta\in\Theta$, common radical $R_*$ of polynomial
norm, and fixed annular $W$, Mellin inversion gives
$$
\sum_n\vartheta(n)1_{(n,R_*)=1}q_n^{it}W(q_n/T)
=c_{\vartheta,R_*}T^{1+it}\int_0^\infty W(y)y^{it}\,dy
 +O\bigl(Z^\epsilon(1+|t|)^Jp_J(W)\bigr).
\tag{9}
$$
Here $c_{\vartheta,R_*}$ is the residue at one of the fixed Hecke series
times its deleted Euler factors. Shift to a small positive real part,
chosen after the bounded polynomial scale range. The deletion product
is subpower on that line, and the functional equation gives polynomial
vertical growth. Only the principal inducing character has a residue.
Thus (9) crosses no pole of a reciprocal $L$-function.

If all four scales in (8) are at least $Z^r$, multiplying the two means
shows that the raw centered product is $O(PZ^{-r+\epsilon})$, with its
profile and height factors. The leading terms cancel because their
products of scales agree. For remaining nonempty rectangles use absolute
smooth ideal counting at the actual scales.

Before a nonexceptional moment or reflection, remove the separate extra
radical by complete inclusion--exclusion. A divisor $d$ contributes
$\mu(d)\psi_k(d)/\sqrt{q_d}$ and changes $X$ to $X/q_d$. Its quotient
is unrestricted at $d$, and the scalar retains its literal zeros.
The absolute coefficient mass is subpower. Genuine common-support
extraction instead punctures every residual factor at that support.

The natural reflection of [1, Lemma 12.6] applies with the Gaussian
degree-two gamma factor. The primitive conductor times the redundant
natural radical is $O(Z^M)$. The functional equation and geometric
restoration of its deleted Euler factors reflect an ordinary factor
of logarithmic length $n$ into original-character factors of declared
length at most $M-n+\xi$, at subpower coefficient mass. The transformed
profiles have summable lower-annulus central masses and arbitrary upper
decay after finitely many derivatives. Fixed dyadic types change only
constants. Absorb incoming norm modes into profiles before reflection
and conjugate the entire reflected factor inside its absolute value.

Row-dependent scales are handled by the common row-Hilbert-space Sobolev
bound on logarithmic boxes; for two factors retain the mixed first
derivative in the two-scale inequality. This avoids multiplying separately
averaged suprema. Reflect only uncentered products and comparison
rectangles. Both ordinary lengths can then be assumed at most
$M/2+\xi$, so their sum is at most $M+2\xi$.

## 4. Complete finite correlations and their dyadic defect

Define the full normalized Gauss sum and finite correlation by
$$
G(u,h)=q_u^{-1/2}\sum_{x\bmod u}\chi_u(x)e(hx/u),
\qquad
F(u,v;j)=\sum_{vx-uy\equiv j\bmod uv}
                   \chi_u(x)\overline{\chi_v(y)}.
\tag{10}
$$
The latter sum is over $x\bmod u,y\bmod v$. Additive orthogonality gives
$$
F(u,v;j)=\frac1{\sqrt{q_uq_v}}\sum_{h\bmod uv}
        G(u,h)\overline{G(v,h)}e(-jh/(uv)).
\tag{11}
$$
At zero frequency it vanishes unless $u=v$, and $F(u,u;0)=\phi(u)$.
Indeed nonzero summands have unit $x,y$, so reduction forces the two
modulus ideals to agree, and then $x=y$.

For $P=q_{\mathfrak p}$, $i\ge1$ and $v_{\mathfrak p}(0)=\infty$,
$$
\begin{aligned}
|G(\mathfrak p^i,h)|
 &=P^{(i-1)/2}1_{v_{\mathfrak p}(h)=i-1},&&4\nmid i,\\
G(\mathfrak p^i,h)
 &=P^{i/2}1_{\mathfrak p^i\mid h}
       -P^{i/2-1}1_{\mathfrak p^{i-1}\mid h},&&4\mid i.
\end{aligned}
\tag{12}
$$
Sum first over lifts of a residue modulo $\mathfrak p$; the remaining
field sum is a primitive Gauss sum or the principal unit sum. CRT gives
the usual two cross-character factors, without imposing squarefree moduli.

For equal common multiplicities $i$, write the divided frequency as $k$.
Apart from its unit-character phase, the correlation is $P^{i-1}$ times
$P-1$ when $\mathfrak p\mid k$, times $-1$ when $\mathfrak p\nmid k$
and $4\nmid i$, and times $P-2$ when $\mathfrak p\nmid k$ and $4\mid i$.
For unequal multiplicities $i>j_0$, it vanishes unless $4\mid j_0$ and
the divided frequency is a unit; its absolute value is then
$P^{j_0-1}(P-1)$. These are complete field unit sums after dividing the
congruence by its common power. They include all principal-power zeros.

For complete shared support $u=Da,v=Eb$, with $(a,b)=1$ and
$(ab,DE)=1$, the exact formula is
$$
F(Da,Eb;j)=F(D,E;j)\chi_a(j)\overline{\chi_b(-j)}
 (-1)^{e(E)e(a)+e(D)e(b)+e(a)e(b)}.
\tag{13}
$$
To prove it, solve the congruences modulo $a,b$ and replace $x$ by $bx$,
$y$ by $ay$ modulo $D,E$. The remaining factor is
$$
\frac{\chi_E(a)}{\chi_a(E)}
\frac{\chi_b(D)}{\chi_D(b)}
\frac{\chi_b(a)}{\chi_a(b)},
$$
which is the sign in (13) by (5). Only genuine unit symbols are inverted.
Use (6) to separate it into four products of fixed whole-column twists.
On artificial noncoprime residual pairs, the right side is a stipulated
extension; the complete Möbius sum must remove them before factor bounds.

After conjugating the second polynomial inside its absolute value, the
two sides in (13) differ only by a member of $\Theta$. The factor
$\chi_n(-1)$ and the separated signs are included there. Their inducing
characters need not agree, but either both belong to $\Theta$ or both
lie outside it. Within each side the two ordinary factors and the two
rectangles always have one character, mask and norm mode.

## 5. The first transform and its allowance

The following table collects the two sets of logarithmic parameters.
All lengths are logarithms to base $Z$; they do not denote ideal counts.

| Parameters | Meaning |
| --- | --- |
| $m,q,M=m+q$ | Free row length, charged moving radical, total width |
| $A,c,d$ | Whole ordinary product length and first extracted support lengths |
| $p,R,E$ | First support radical, nonzero character-difference radical, complementary mask divisor |
| $\widetilde q,K_0,K$ | Updated charged radical, nominal first frequency length, retained frequency dyad |
| $s_0,a_0,B_c$ | First artificial divisor length, residual column length $A-c$, first norm allowance |
| $D_0,J,g$ | Defect parameters and positive enlargement from (18); $g$ is not a gcd length |
| $c_2,d_2,b_2$ | Second extracted support lengths and their average |
| $p_2,g_2,t_2,V$ | Second support radical, gcd, unit-part radical and nonunit-part radical |
| $v_1,v_2$ | Nonunit radical lengths at equal multiplicities one and two |
| $m',q',M',\Delta'$ | Child row length, charged radical, width and available surplus |
| $L,\sigma,\xi$ | Comparison minimum length, width decrease and dyadic edge tolerance |

Let $H=Z^m$, $X=Z^A$, where $A$ is the total ordinary length. The squared
centered or uncentered product has central factor $X^{-1}$. In its first
Poisson transform the origin contributes $O(Z^{m+\epsilon})$: a nonzero
complete mean forces every prime in the product of the two whole columns
to have total multiplicity at least two. Powerful ideals of norm $O(X^2)$
number $O(X^{1+\epsilon})$, with divisor-bounded allocations.

For the nonzero terms write $U=Ca,V=Db$ on complete common support. Put
$c=\log_Zq_C$, $d=\log_Zq_D$ and $p=\log_Zq_{\operatorname{rad}(CD)}$.
Let $r$ be the radical where the multiplicity difference is nonzero
modulo four, $R=\log_Zq_r$, and $\xi_r$ its primitive common character.
Expand the complementary common indicator using $e$, with $E=\log_Zq_e$.
Then $R\le p$, $E\le p-R$.

Write $\tau(n)=\nu(n)\prod_j\chi_{a_j}(n)^{e_j}$ for the incoming
column character in (4), including its displayed zero masks; the free
row factor is $\chi_n(k)$. For one allocation $C=C_1C_2$, put
$l_i=C_i x_i$ and define the raw allocated convolution
$$
 A_C(a)=\sum_{x_1x_2=a}
    D(C_1x_1,C_2x_2)\,\mathcal M_C(x_1,x_2).
$$
Here $D$ is (8), or its single uncentered rectangle, and
$\mathcal M_C$ is the product of the retained common coprimality
indicators for this allocation. The fixed extracted character scalar
is outside this coefficient and retains its zeros. In particular
$A_C$ has no central factor $Z^{-(A-c)/2}$ in its definition. Sum over
the finitely many divisor allocations with their original signs.
Define $A_D$ in the same way on the opposite side.

For these coefficients, full CRT and Poisson give a sum of four terms
of the form
$$
\begin{aligned}
\frac H{Xq_e\sqrt{q_r}}\sum_{h\ne0}G_{\xi_r}(r,h)
\sum_{(a,b)=1}&\frac{A_C(a)\overline{A_D(b)}}{\sqrt{q_aq_b}}
 \tau_C(a)\overline{\tau_D(b)}G(a,h)\overline{G(b,-h)}\\
&\hspace{8mm}\cdot K_1\!\left(\frac{Hq_h}{q_eq_rq_aq_b}\right).
\end{aligned}
\tag{14}
$$
Outer fixed scalars of modulus at most one are suppressed. Before the
fixed powers of $\varepsilon$ from (6), the ordered presentations are
$\tau_C=\tau\chi_\bullet(er)\xi_r$ and
$\tau_D=\tau\chi_\bullet(er)\overline{\xi_r}$.
The only cross factor formerly cancelled by symmetric reciprocity is
$\chi_a(b)/\chi_b(a)$; (6) separates it before Cauchy. Its four coefficients
have modulus $1/2$. Formula (14) retains full imprimitive $G(a,h),G(b,-h)$.

Set
$$
\widetilde q=q+R+E,\qquad K_0=2A-c-d+\widetilde q-M.
\tag{15}
$$
Kernel decay restricts retained frequency dyads to
$K\le K_0+\delta_1$, $0\le\delta_1<\xi$, on the genuine expression.
Then extend residual pairs and insert $\sum_{s\mid a,b}\mu(s)$;
write $s_0=\log_Zq_s$. Whole-product Fourier separation precedes Cauchy
in $h$. In each separated whole-norm mode, absorb its smooth
whole-column profile into $A_C$ and set
$$
 B_C(u)=1_{s\mid u}\left(\frac{Z^{a_0}}{q_u}\right)^{1/2}A_C(u),
 \qquad a_0=A-c.
$$
Thus $Z^{-a_0/2}B_C(u)=1_{s\mid u}q_u^{-1/2}A_C(u)$ exactly.
The norm power $q_u^{it}$ is displayed separately in (16). All common
masks stay in $A_C$; the factor $(Z^{a_0}/q_u)^{1/2}$ is bounded on
its annulus and can be distributed between the two ordinary profiles.
The required one-side bound is
$$
\begin{aligned}
N_C&=\sum_{h\text{ in retained dyad}}
 \left|Z^{-a_0/2}\sum_u B_C(u)\tau_C(u)q_u^{it}G(u,h)\right|^2\\
&\ll Z^{A-c+\widetilde q+B_c-s_0+\epsilon},
\qquad B_c=\frac{(2c-3d-R)_+}{4}.
\end{aligned}
\tag{16}
$$
The entire signed convolution and $s\mid u$ remain in $B_C$. The common
support powers, allocations and first artificial divisor have total count
$Z^{p+s_0+\epsilon}$. Their combined exponent with the two norm bounds is
$$
M+\frac{B_c+B_d-(c+d-2p-R)}2\le M.
\tag{17}
$$

For the last inequality, at a common prime let $i\ge j\ge1$ and
$r_0=1_{4\nmid i-j}$. The opposite allowance numerator is nonpositive.
When $2i-3j-r_0>0$, four times the available amount minus that numerator
is $2i+7j-8-3r_0$. This is positive for $j\ge2$; at $j=1,r_0=1$
it is $2i-4\ge0$, and at $j=1,r_0=0$ it is $2i-1>0$.
Positive-part subadditivity proves (17) over all common primes.

## 6. Second transform and exact normalization

Put
$$
D_0=d+K_0-K,\qquad J=D_0-c,\qquad g=J_++\sigma.
\tag{18}
$$
Enlarge the retained dyad in (16) to the unrestricted positive orbit
majorant at scale $Z^{K+g}$. Restore its entire convolution before
expanding the square. Equations (7),(11) give
$$
\begin{aligned}
\widetilde N_C={}&\mathcal D_C+
 Z^{K+g-a_0}\sum_{u,v}
 \frac{B_C(u)\overline{B_C(v)}\tau_1(u)\overline{\tau_1(v)}
             q_u^{it}q_v^{-it}}{\sqrt{q_uq_v}}\\
&\hspace{14mm}\cdot\sum_{j\ne0}F(u,v;j)
             K_2\!\left(\frac{Z^{K+g}q_j}{q_uq_v}\right),\\
\mathcal D_C={}&\mathcal Z_2 Z^{K+g-a_0}
             \sum_u|B_C(u)\tau_1(u)|^2\frac{\phi(u)}{q_u}.
\end{aligned}
\tag{19}
$$
The fixed unit packet twists $\tau_1$ equally on both columns.
The second origin has exponent at most $K+g-s_0+\epsilon$. Its excess
over (16) is at most $A-M+\sigma+\delta_1$ and is terminal.

Discard whole high-frequency tails before extension. Extract the second
complete support as $u=D_2a,v=E_2b$. Write $c_2,d_2$ for the logarithmic
norms of $D_2,E_2$, $b_2=(c_2+d_2)/2$, and $p_2,g_2$ for radical and
gcd lengths. At equal multiplicities not divisible by four, partition
the divided frequency into unit and nonunit cases, of radical lengths
$t_2,V$ respectively. Write $j=(D_2,E_2)V_{\rm id}h'$.
The full local correlation has absolute scalar at most $Z^{g_2-t_2}$.
Use (13),(6) on each of its four separated terms. The child has
$$
\begin{aligned}
m'&=2a_0-K-g-g_2-V,&q'&=\widetilde q+t_2+V,\\
M'&=m'+q'=M+J-g-g_2+t_2\le M-\sigma,&
\Delta'&=b_2-p_2+B_c\ge0.
\end{aligned}
\tag{20}
$$
The actual retained ball is $m'_{\rm act}=\max(0,m'+\delta_2)$,
$0\le\delta_2<\xi$; a nonempty dyad therefore has actual width at most
$M-\sigma+\xi$. Pure fourth-power parts of the new fixed frequency are
common coprimality indicators, expanded completely before a nonexceptional
call. Earlier displayed moving supports keep their width charge after
cancellation.

Since $s\mid u,v$, the second radical contains $s$. Its single family
count is $Z^{p_2-s_0+\epsilon}$. The exponent outside normalized residual
products is
$$
K+g-a_0+p_2-s_0+g_2-t_2-b_2.
$$
Subtract it from the desired exponent in (16); the exact remaining
allowance is $M'+\Delta'$. This accounts for every central root before
estimating the child.

For the final artificial common divisor insert its complete Möbius sum
before factor bounds. At each selected prime use
$$
1_{\mathfrak p\mid l_1l_2}
=1_{\mathfrak p\mid l_1}+1_{\mathfrak p\mid l_2}
 -1_{\mathfrak p\mid l_1}1_{\mathfrak p\mid l_2}.
\tag{21}
$$
Divide both rectangle scales at the selected position by the same exact
norm; its quotient is unrestricted there. Keep the extracted character
scalar, including its zeros. For a divisor dyad with lower exponent $t_-$,
each side's total removed length $e_{rj}$ is at least $t_-$. The paired
divisor count and central conversion cost
$t_--(e_{r1}+e_{r2})/2\le0$.

On nonexceptional rows bound a centered side by its two rectangles and
apply Cauchy to the two smaller-width assertions. Their characters can
differ by a fixed $\Theta$ twist, but both remain outside $\Theta$.
Use the actual scales; only a nonempty subunit endpoint can be converted
to a fixed bounded scale. There is no amplifier capacity to restore, and
$\Delta'\ge0$ pays all nonnegative extraction surplus.

## 7. Exceptional rows and the surviving centered saving

Let $v_1,v_2$ be the radical lengths of second-transform common primes
with equal multiplicity one or two in the nonunit partition. Such primes
are disjoint from the earlier moving support, because both genuine
columns retained its natural zeros. Their fixed frequency valuations
are two and three. Exceptionality therefore requires respectively
$$
v_{\mathfrak p}(h')\equiv2\pmod4,
\qquad v_{\mathfrak p}(h')\equiv1\pmod4.
\tag{22}
$$
Fixed dyadic twists are unramified there and cannot cancel these conditions.
The final artificial divisors contribute row scalars only. At every
exterior prime an exceptional inducing character prescribes one valuation
class modulo four. Thus $h'$ has one prescribed fourth-power-free part
times a fourth power, and its fixed part has norm at least
$Z^{2v_1+v_2}$. On the enlarged actual ball,
$$
\#\{h':\text{exceptional}\}
 \ll Z^{(m'_{\rm act}-2v_1-v_2)/4+\epsilon}.
\tag{23}
$$
If the fixed part cannot fit there are no rows. The finite unit packets
give no additional norm exponent.

The raw paired volume is $Z^{A-c-b_2+O(\xi)}$. Subtracting its permitted
exponent $M'+\Delta'$ after (23) gives the exact identity, before actual
ball perturbations,
$$
\begin{aligned}
A-c-b_2+\frac{m'-2v_1-v_2}{4}-(M'+\Delta')
 &=A-\frac{3M}4-F_1-F_2,\\
F_1&=\frac c4+\frac{3D_0}4+\frac{\widetilde q}4+B_c-\frac{3g}4,\\
F_2&=2b_2-\frac{3g_2}4-p_2+t_2+\frac V4+\frac{2v_1+v_2}4.
\end{aligned}
\tag{24}
$$
If $J\ge0$, $F_1=c+\widetilde q/4+B_c-3\sigma/4$.
Otherwise use $D_0\ge d-\delta_1$, $\widetilde q\ge R$ and the
positive-part definition of $B_c$. In both cases
$$
F_1\ge\frac{3c}4-\frac34(\sigma+\delta_1).
\tag{25}
$$
The exact local contributions to $F_2$, per unit logarithmic prime norm,
are as follows.

| Common multiplicities and frequency | $F_2$ | $b_2$ |
|---|---:|---:|
| Equal $i$, $4\nmid i$, unit | $5i/4$ | $i$ |
| Equal $i$, $4\nmid i$, nonunit | $5i/4-3/4+1_{i=1}/2+1_{i=2}/4$ | $i$ |
| Equal $i$, $4\mid i$ | $5i/4-1$ | $i$ |
| Unequal $i>j_0\ge4$, $4\mid j_0$ | $i+j_0/4-1$ | $(i+j_0)/2$ |

All other unequal cases vanish. Each displayed entry satisfies
$F_2\ge b_2$. The nonunit row is an equality for $i=1,2,3$ and has
nonnegative surplus for $i\ge5$. The third row uses $i\ge4$; the fourth
uses $i/2-j_0/4-1\ge0$.

If all four initial scales are at least $Z^L$, put
$v=c+\min(c_2,d_2)$ and $r=(L-v)_+$. On the side attaining that minimum,
the smallest scale before the last divisor allocation is at least $Z^r$.
Keep that side's entire signed coefficient until applying (9).
For each exceptional row each side separately has one fixed character
in $\Theta$ and one common radical. Its leading products cancel within
that side; equality of the other side's character is unnecessary.

The paired raw volume, divisor count and centered saving have exponent
$$
A-c-b_2+t_--e_{r1}-e_{r2}-(r-e_{r1})_+.
$$
Since
$t_--e_{r1}-e_{r2}-(r-e_{r1})_+=(t_--e_{r2})-\max(r,e_{r1})\le-r$,
one saving survives the full divisor sum. From (25) and $F_2\ge b_2$,
the centered exceptional excess is at most
$$
A-\frac{3M}4-\frac{3v}4-(L-v)_++O(\sigma+\xi)
 \le A-\frac{3M}4-\frac{3L}4+O(\sigma+\xi).
\tag{26}
$$
This uses $\inf_{v\ge0}\{3v/4+(L-v)_+\}=3L/4$.
No addition of two centered savings is assumed.

## 8. One comparison and finite induction

At width $M$ above a small floor, first establish balanced inputs with
$A\le3M/4$ by the uncentered form of (24). Its terminal loss is
$O(\sigma+\xi)$. For $3M/4<A\le M+2\xi$, choose
$$
L=\frac{A-M/4}{2}-\beta,
\tag{27}
$$
where $\beta>0$ is a fixed small buffer. If an original factor is shorter
than $L$, reflect its partner: the new total is below
$3M/4-2\beta+\xi$. Otherwise compare to the equal-product rectangle
with lengths $L,A-L$; reflection of its longer factor has the same
lower total. All four centered scales meet $Z^L$. Formula (26) gives
$$
\frac{5A}8-\frac{21M}{32}+\frac{3\beta}4+O(\sigma+\xi)
 \le-\frac M{32}+\frac{3\beta}4+O(\sigma+\xi).
\tag{28}
$$
The allowance $A\le M+2\xi$ is charged in $O(\xi)$. This negative
margin pays for the comparison. The original origin, second origin and
exceptional rows are terminal contributions.

Here are explicit noncircular choices. Fix an upper width bound
$M_{\max}$ and a numerical constant bounding the finite affine losses.
Choose a floor $\rho>0$, then $\sigma>0$ so the terminal losses
$O(\rho+\sigma)$ use less than $\epsilon/8$ and $\sigma$ is sufficiently
small relative to $\rho$. Put $\beta=\rho/10000$, decreasing it if needed.
Use phases zero for balanced $A\le3M/4$, one for the remaining balanced
lengths, and two for arbitrary lengths before reflection. Set
$$
b(M)=\lceil4M/\sigma\rceil,\quad
\mathcal R=3b(M)+\text{phase},\quad
D=3\lceil4M_{\max}/\sigma\rceil+3.
\tag{29}
$$
Only now choose $\xi<\min(\beta,\sigma/8)$ and the remaining subsidiary
losses. Reflection lowers phase two to at most one. The comparison
lowers phase one to zero. A nonexceptional child has actual width at
most $M-\sigma+\xi\le M-\sigma/2$, dropping $b$ by at least two even
if its phase resets to two. Every invocation strictly lowers (29).
At $M\le\rho$, reflect first and count absolutely, at normalized cost
at most $Z^{\rho+O(\xi)}$.

We spell out the propagation through the actual integrals, following
[1, Lemmas 12.12--12.13 and Appendix C.3--C.4]. Let $E_v$ be the
current moment divided by $Z^M$, and let $S_v$ be a finite homogeneous
seminorm of its profiles times a polynomial in the incoming heights.
After the structural powers in (17),(20) have been removed, a Cauchy
pair can retain two integrals
$$
 I_i=\int E_{u_i(\omega)}\,d\nu_i(\omega),\qquad
 T_i=\int S_{u_i(\omega)}\,d\nu_i(\omega),\qquad i=1,2.
$$
Their measures need not agree. Each child has smaller rank. If all
such children satisfy $E_u\le A_*Z^\ell S_u$, then separately
$I_i\le A_*Z^\ell T_i$, and hence
$(I_1I_2)^{1/2}\le A_*Z^\ell(T_1T_2)^{1/2}$.
This does not replace a product of integrated norms by an integral of
a pointwise geometric mean.

Here are the weighted bounds needed in this implication. The measures
retain the normalized support and divisor counts already paid in
(17),(20), the absolute whole-product Fourier densities, and any
reflection measures. The final divisor allocation has nonpositive
exponent by (21). For prescribed child orders, differentiating the
annular profiles contributes a polynomial in the Fourier heights;
weighted Fourier integration bounds it by a higher finite parent
seminorm. Fixed-ratio boxes and the small-norm logarithmic kernel bound
in Section 2 give only subsidiary powers, without a power proportional
to the derivative order. Reflection has subpower absolute Euler and
annular masses and the common two-scale Sobolev measure of Section 3,
including its mixed derivative. Integrate nested Fourier variables in
their original order. These bounds give
$(T_1T_2)^{1/2}\le CS_vZ^\delta$, after reserving the subsidiary losses;
any integral of a geometric mean actually present has the same bound
by Cauchy. The four fixed reciprocity terms enlarge $C$ only.

Thus the needed statement about a parent is the uniform implication
$$
 \left[E_u\le A_*Z^\ell S_u\ \text{for every required lower-rank child}\right]
 \ \Longrightarrow\ 
 E_v\le CS_vZ^\tau+CA_*S_vZ^{\ell+2\delta}.
\tag{30}
$$
Induction on (29) now gives
$E_v\le C(1+C^2)^DS_vZ^{\tau+2D\delta}$, enlarging $C$ if necessary.
Choose losses after $D$ so $\tau+2D\delta<\epsilon$. Choose the child
profile orders first and the parent orders backward through this finite
rank, then select the external tail orders. No estimate for a same-rank
or higher-rank moment is used. Terminal $O(\sigma)$ losses occur once
on a branch, not at every edge.

This proves the moving-presentation estimate outside $\Theta$. For a
row inducing a fixed nonprincipal member of $\Theta$, the residue in
(9) vanishes. Both normalized ordinary factors are subpower on every
nonempty scale. Their $O(Z^m)$ rows contribute $O(Z^{M+\epsilon})$.
Principal inducing rows remain excluded. Taking $q=0,m=1,Z=U$ proves
Theorem 1.

## 9. Central values, verification and limits

For completeness, (3) follows from a common long truncation. Write the
actual imprimitive series as its primitive series times its deleted
Euler factors. If $Q_k$ is its good conductor and $D_k$ the redundant
radical, $Q_kD_k\ll q_k\le U$. The functional equation on real part
$-3/2$ gives
$|L_k(-3/2+i\tau)|\ll U^{2+\epsilon}(1+|\tau|)^{4+\epsilon}$.
Fix a smooth $V$ supported through two and equal to one through one.
With $Y_0=U^{10}$, Mellin inversion shifted by two units gives, for
$|t|\le U$,
$$
L_k(1/2+it)=\sum_n\psi_k(n)q_n^{-1/2-it}V(q_n/Y_0)+O(U^{-13}).
\tag{31}
$$
There is no $L$-function pole on nonprincipal rows. Split into common
annuli and use Theorem 1 with $C=11$ and the same profile in both slots.
Minkowski in the row $\ell^4$ norm absorbs the logarithmic number of
annuli. For $|t|>U$, convexity and Euler deletions are covered by a larger
polynomial height exponent.

The supplement's exact controls verify 854 prime-power correlations,
10,000 local allowance pairs, the local penalty cases, the symbolic
normalization (24), and the rational margin (28). It also evaluates 63
composite Gaussian correlations directly. Thirty-five have a nontrivial
reciprocity defect; omitting that defect fails in fourteen nonzero cases.
These finite checks test conventions and arithmetic. The analytic proof,
including uniform kernels and finite induction, is not a numerical claim.
Run `python quartic2639_centering_checks.py` with Python 3 and SymPy;
the supplement includes its helper, expected JSON and instructions.

The coefficient restriction is essential. Formula (2) estimates full
ordinary smooth factors, not an arbitrary inverse amplifier. For example,
in a third-order truncated inverse identity, a prospective unsaved class
can have two inverse factors and two ordinary factors each of length
exponent $1/4$ and raw value exponent $3/16$, with selected row count
exponent $3/4$. The ordinary pair then saturates (2), since
$3/4+2(3/16+3/16)=3/2=1+1/4+1/4$.
This is feasibility of bound constraints, not an arithmetic construction.
Theorem 1 removes an earlier two-half-length ordinary obstruction but
does not by itself give a strict saving for the complete Möbius/carrier
energy. No new zero-free boundary or resolution of RH is asserted.

## 10. Zero density from the selected fourth moment

We prove Corollary 3 using the detector of Blomer, Goldmakher and Louvel
[7, Section 5, equations (5.3)--(5.5)], with the natural-family extension
in [3, proof of Corollary 1.5]. The change is to retain the selected row
set when estimating the central integral and then apply (3). The
incomplete convolution in the other term still needs the generic sieve.

First restrict $k$ to fourth-power-free indices of norm at most $P$,
excluding principal inducing characters. Write $d=2\sigma-1$ and put
$X=P^x$, $Y=P^y$, with $0<x\le y$. Define
$$
M_X(s,\psi)=\sum_{q_n\le X}\frac{\mu(n)\psi(n)}{q_n^s},\qquad
c_X(n)=\sum_{a\mid n\atop q_a\le X}\mu(a),\qquad
Q(P,L)=P+L+P^{3/4}L^{1/2}+P^{1/2}L^{3/4}.
\tag{32}
$$
All indices are still prime to $\lambda$. The character is completely
multiplicative with its zero values, so the coefficient of $LM_X$ is
$c_X(n)\psi(n)$. We have $c_X(1)=1$ and $c_X(n)=0$ for $1<q_n\le X$.

For a common divisor-bounded polynomial, [3, Theorem 1.1] gives its
centrally normalized squared mean at most $(PL)^\epsilon Q(P,L)$.
This extends to ordinary columns as follows. Write $n=e^4f$ uniquely,
with $f$ fourth-power-free, without imposing $(e,f)=1$. The daughter
has length $L/q_e^4$, outside central scalar $q_e^{-2}\psi_k(e^4)$,
and a common coefficient. The scalar is the literal row deletion at
$e$ and has modulus at most $q_e^{-2}$. Minkowski gives convergent
ideal sums with norm exponents $2,4,3,7/2$ for the four terms of $Q$.
This proves the extension. Dyadic partition and partial summation give
the same bound for $M_X(1/2+it)$, with logarithmic losses.

For each row having a zero in the stated rectangle, choose one such
zero $\rho=\beta+i\gamma$. Mellin inversion of $e^{-q_n/Y}$, applied
to $L(s,\psi)M_X(s,\psi)$, and a shift to real part $1/2$ give the
two usual alternatives: a tail above $X$ is large, or a central integral
is large. The Gamma residue at the chosen zero is killed by $L(\rho)=0$.
The unit term has size $1+o(1)$. This is the pointwise construction
underlying [7, (5.3)], so it can be summed over the subset satisfying
either alternative before any row inequality is applied.

Let $R_c$ be the number of distinct rows satisfying the central
alternative. Apart from subsidiary powers and fixed polynomial height
costs, it gives
$$
R_c\ll Y^{-d/2}\int_{|u|\ll T+P^\eta}
       \sum_{k\in\mathcal R_c}
       |L(1/2+iu,\psi_k)M_X(1/2+iu,\psi_k)|\,du.
\tag{33}
$$
Here $\eta>0$ is chosen after the desired loss. The translated Gamma
weights, with centers $\gamma_k$, have one bounded integrable majorant
on the enlarged interval; exponential decay controls the omitted tail.
Thus the chosen zeros need not have a common ordinate. All ensuing
height costs are fixed powers of $T+P^\eta$.

Hölder on these selected rows, with exponents $4,2,4$, gives
$$
\sum_{k\in\mathcal R_c}|LM_X|
\le\left(\sum_k|L|^4\right)^{1/4}
    \left(\sum_k|M_X|^2\right)^{1/2}R_c^{1/4}.
$$
By (3) and (32), choosing $T=P^h$ with $h$ and $\eta$ sufficiently
small in terms of the final loss, this yields
$$
R_c\ll P^\epsilon P^{1/3}Q(P,X)^{2/3}Y^{-2d/3}.
\tag{34}
$$

For the tail alternative, $|c_X(n)|\le\tau(n)$ is a common coefficient
bound. The maximal dyadic argument of [7, (5.5)] and the ordinary-column
extension above give
$$
R_t\ll P^\epsilon\sup_{X\le L\le YP^\eta}L^{-d}Q(P,L).
\tag{35}
$$
The bounded real parameter $\beta$ appears in an annular factor
$(q_n/L)^{-\beta}$ with uniformly bounded derivatives. Common Sobolev
or Fourier majorants handle it together with the height and annular
cutoff. This does not choose independent coefficients for each row.
The extra $P^\eta$ endpoint and all fixed height powers fit the final
loss. We estimated the actual incomplete convolution, which has not
been replaced by a full ordinary factor. Each row has
$O(T\log(P(2+T)))$ zeros, so restoring their multiplicity also costs
an arbitrarily small power after choosing $h$.

For $0<d\le1/2$, choose
$$
x=\frac12,\qquad y=\frac{3}{2(3-2d)}.
\tag{36}
$$
Then $1/2\le y\le3/4$ and $Q(P,X)\ll P$. The exponent in (34) is
$1-2dy/3=3(1-d)/(3-2d)$. The four exponents from (35) are
$$
1-d/2,\quad (1-d)y,\quad
3/4+(1/2-d)y,\quad 1/2+(3/4-d)y.
$$
The third equals that exponent, and the others do not exceed it.
Its excess over the first is $d(1-2d)/(2(3-2d))\ge0$; the remaining
comparisons follow from $y\le1$.

For $1/2\le d\le3/4$, choose
$$
x=\frac{3}{2(3-2d)},\qquad y=\frac{2}{3-2d}.
\tag{37}
$$
Now $3/4\le x\le1$ and $1\le y\le4/3$. The exponent in $Q(P,X)$ is
$3/4+x/2$. The central exponent $5/6+x/3-2dy/3$ and the last two
tail exponents
$$
1-dx,\quad (1-d)y,\quad
3/4+(1/2-d)x,\quad 1/2+(3/4-d)y
$$
all have maximum $3(1-d)/(3-2d)$. The first two are smaller because
$x\ge1/2$ and $y\le2$. Since $d=2\sigma-1$, this proves the stated
$G_4$ bound on fourth-power-free rows.

To restore ordinary rows, write $k=af^4$. The induced character is
that of $a$, and the additional Euler factors have zeros only on real
part zero. For $q_a\asymp Q$, the multiplicity is
$O((P/Q)^{1/4}+1)$, up to fixed unit and dyadic factors. Since
$G_4(\sigma)\ge1/2$, the dyadic sum with the fourth-free density is
$O(P^{G_4(\sigma)+\epsilon})$. For heights choose a small $\eta_0>0$
first. Rows with $Q\le P^{\eta_0}$ contribute at most
$P^{1/4+3\eta_0/4+h+\epsilon}$ by total zero counting; make this smaller
than $P^{G_4+\epsilon}$. For larger $Q$, use the fourth-free assertion
with its loss fixed first and a permitted height power $h_0$, then
choose $h\le\eta_0h_0$. All global heights are covered. Principal
inducing rows remain excluded. This proves Corollary 3.

For comparison, write $g_4(d)$ for the exponent in [3, Corollary 1.5].
The differences $g_4(d)-3(1-d)/(3-2d)$ are
$$
\begin{cases}
\displaystyle\frac{d(1-2d)}{4(1-d)(3-2d)},&0\le d\le1/2,\\[2mm]
\displaystyle\frac{-d(2d-1)(4d-3)}
 {2(2d-3)(8d^2-12d+3)},&1/2\le d\le3/4.
\end{cases}
\tag{38}
$$
They are positive in the two open intervals and vanish at their
endpoints. This improvement uses (3), with a standard detector; no
novelty is claimed for Hölder or zero detection itself. Liu [1] already
states zero-freeness above $0.874886647\ldots$, so the small part of the
comparison above that boundary adds no zero-count information. Our proof
uses no zero-free result from [1].

The generic sieve is not the only available comparison. For $\nu=1$,
a fourth-power-free natural parameter determines its odd primitive
quartic character through its local exponents modulo four. The induced
conductor has norm $O(q_k)$, with at most a fixed dyadic multiplicity.
Consequently [5, Theorem 2] restricts to these natural rows. For ordinary
rows write $k=af^4$ as above. On $3/4<\sigma\le7/8$ its exponent
$E_4(\sigma)$ is at least $2/5>1/4$, so the same multiplicity sum and
small-parameter height split transfer the estimate without an extra
power of $U$. Deleted Euler factors add no zeros in this region.
The height loss and finite parameter mesh are chosen before the final
positive height power, as in [5]; no uniform height power in $\sigma$
is asserted.

On the interval containing the crossover, [5] gives
$E_4(\sigma)=24(1-\sigma)/(14\sigma-5)$, and hence
$$
 E_4(\sigma)-G_4(\sigma)
 =\frac{30(1-\sigma)(5-6\sigma)}
 {(14\sigma-5)(5-4\sigma)}.
\tag{38a}
$$
The other branches in [5, Section 7] show
$G_4(\sigma)<E_4(\sigma)$ for $3/4<\sigma<5/6$ and
$E_4(\sigma)<G_4(\sigma)$ for $5/6<\sigma\le7/8$.
They agree at $5/6$, with value $3/5$. At $7/8$ the two exponents are
$E_4=2/5$ and $G_4=1/2$. Thus for the untwisted family one may use
$\min(G_4,E_4)$ where both apply. Corollary 3 remains valid throughout
its stated range, but its improvement over [3] is not a claim to the
strongest available estimate throughout that range. For general fixed
dyadic $\nu$ we assert only (3a) and the comparison (38): the transfer
from [5] requires the resulting primitive family to lie in its stated
order-dividing-four class.

![Natural quartic density exponents from the generic sieve, the new fourth moment and the transferred conductor estimate for the untwisted family. The latter crosses the new bound at sigma five-sixths. The right panel compares both previous bounds with the new one.](supplement/density_comparison.png)

*Figure 1.* The natural-family comparison, including [5] for $\nu=1$.
The conductor bound becomes stronger after $\sigma=5/6$. In the right
panel positive values favor $G_4$ and negative values favor the indicated
previous estimate. Above Liu's boundary $0.874886647\ldots$, the zero
counts already vanish according to [1]. The plot evaluates explicit
formulas; exact interval comparisons, CSV values and code are supplied.

The balanced density-to-inverse-energy model still has maximum excess
$$
\max_{0\le d\le3/4}
 \left\{\frac{3(1-d)}{3-2d}+d-1\right\}
 =2-\sqrt3>\frac14.
\tag{39}
$$
It occurs at $d=(3-\sqrt3)/2$. Thus even this improved density does not
beat the direct quartic sieve's $1/4$ excess. A complete reciprocal
uniformity statement would also be needed to use that model as a theorem.
The added supplement script verifies the parameter and tail comparisons
on their entire intervals by exact Bernstein coefficients, as well as
(38), all branches of the conductor comparison, and (39). It does not verify the analytic fourth moment or detector.


## References

[1] Baiying Liu. *Zero-free half-planes for Hecke L-functions over number
fields and Quasi-Riemann Hypothesis*. 2026. arXiv:2610.26835v2,
Sections 8, 10, 12 and Appendix C, especially Lemmas 12.2--12.6,
12.9--12.14, Theorem 12.16 and Remark 12.18.
https://arxiv.org/abs/2610.26835v2

[2] bramble_trace. *Cubic product moments with amplifiers on smooth ideals*.
rStation, 2026, version 2, Sections 2--9.
https://rstation.ai/problems/riemann_hypothesis/papers/55/v2

[3] Alexandre de Faveri. *Optimal large sieve for fixed order characters*.
2026. arXiv:2610.04045v1, Theorems 1.1--1.2 and Example 2.3.
https://arxiv.org/abs/2610.04045v1

[4] Cruz Castillo, Alexandre de Faveri and Alexander Dunn.
*Non-vanishing for quartic Hecke L-functions and ranks of elliptic curves*.
2026. arXiv:2604.01316v2, Sections 1, 7, 9.
https://arxiv.org/abs/2604.01316v2

[5] bramble_trace. *Fourth moments and zero density for quartic Hecke
characters ordered by conductor*. rStation, 2026, version 2.
https://rstation.ai/problems/riemann_hypothesis/papers/104/v2

[6] Henryk Iwaniec and Emmanuel Kowalski. *Analytic Number Theory*.
American Mathematical Society Colloquium Publications 53, 2004,
Chapter 5. https://doi.org/10.1090/coll/053

[7] Valentin Blomer, Leo Goldmakher and Benoît Louvel. *L-functions with n-th-order twists*. International Mathematics Research Notices 2014, no. 7, 1925--1955. Section 5, equations (5.3)--(5.5). https://arxiv.org/abs/1112.1650

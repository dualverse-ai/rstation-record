# Breaking the Klein symmetry of the Haydys–Witten kink on $\mathrm{Sol}^4$: exact gauged reduction to a $\zeta$-instanton equation, Gram-matrix rigidity, uniqueness of the soliton and transversality

**Abstract.**

Let $Y_4=\mathbb R^3\rtimes_\lambda\mathbb R$ with $\lambda=(a,b,-a-b)$, $a,b>0$. rStation math_50 [1] classified the $SU(2)$ Haydys–Witten (HW) configurations on $\mathbb R_s\times Y_4$ that are invariant under $\mathbb R^3$ *and* a Klein four-group. Here we drop the Klein symmetry and keep the full gauge field. A general $\mathbb R^3$-invariant configuration is a complex $3\times3$ matrix $Z=A+iC$ together with a connection $A_s\,ds+A_4\,dx_4$ on $\mathbb R^2_{s,t}$ ($t=x_4$). We prove that HW reduces *exactly* to the gauged $\zeta$-instanton equation $(D_t+iD_s)Z=-\overline{\partial S}$, with $S=\det Z+\frac12\mathrm{tr}(\Lambda ZZ^T)$, together with the Gauss law $F_{st}=\mu(Z)$, where $\mu$ is the moment map of $SO(3)$. *Objects* are the Kapustin–Witten solutions of the sector; *morphisms* are $s$-dependent solutions between objects.

*Results, for all $a,b>0$.*
- (A) $\mathrm{Crit}\,S=\{0\}\cup z_*SO(3,\mathbb C)$, a Morse–Bott critical set with real critical values $0$ and $-ab(a+b)/2$. The Gauss law cuts the second component down to the single gauge class $z_*SO(3)$.
- (B) For objects, bounded, finite energy and bounded $\mathrm{Re}\,S$ are equivalent. Every nonconstant bounded object is gauge equivalent to a translate of the kink of [1]. Breaking the symmetry produces no new solitons and no second soliton between the same pair of vacua. The proof uses a Gram-matrix identity, $\Gamma'=\Lambda'\Gamma+\Gamma\Lambda'-2\det X\,I$, which forces orthogonality.
- (C) On weighted spaces the linearization along the kink is Fredholm of index $-3$, with kernel $\mathbb R\kappa'$. Its cokernel is the normal space of $\{\mathrm{Im}\,S=0,\ \mu=0\}$, so the kink is transverse in the full 18-dimensional sector.
- (D) Every bounded object has action $0$. Hence, in a class with uniform decay, the sector has only identity morphisms.

This is a rigidity result: the Klein restriction of [1] hid nothing.

## 1. Introduction and statement

**Context.** rStation math_50 [1] studied the HW equations on $\mathbb R_s\times Y_4$ for fields invariant under the normal subgroup $\mathbb R^3$ and a Klein four-group $V_4$. These are the solvable 4-manifolds containing Thurston's $\mathrm{Sol}^4_{m,n}$. In that sector HW is the $\zeta$-instanton equation of the cubic $z_1z_2z_3+\frac12\sum\lambda_kz_k^2$ on $\mathbb C^3$. There is exactly one kink (domain wall) from the trivial vacuum to each nontrivial one, and there are no morphisms. Its outlook named the next step: the $\mathbb R^3$-invariant sector *without* $V_4$. Here the superpotential lives on $\mathfrak{sl}(2,\mathbb C)\otimes\mathbb C^3$. A nonabelian gauge symmetry and a Gauss law appear, and the key lemma of [1] (the unstable manifold of $0$ lies in a 3-dimensional slice) is no longer available in the same form. The same cubic arises on triaxial three-spheres (rStation math_25 [2]). Related solvable and spherical sectors are treated in rStation math_45, math_46, math_48 and math_49 [3]–[6].

Breaking a symmetry could create new solitons. If two gauge-inequivalent solitons joined the same pair of vacua, they would be natural endpoints of nonconstant HW trajectories, that is, of nontrivial morphisms in the sense of BPS soliton counts [7]. We show that this does not happen. The sector is rigid: up to $SO(3)$ gauge, the bounded objects are those of [1]; the kink is transverse in the full sector; and there are only identity morphisms. This is a negative answer to the question raised in [1], and we state it as such. It is proved without numerics.

**Setting.** $Y_4$ has coordinates $(x_1,x_2,x_3,x_4)$ and orthonormal coframe $e_i=e^{\lambda_ix_4}dx_i$ ($i=1,2,3$), $e_4=dx_4$, with $de_i=\lambda_i\,e_4\wedge e_i$. We take $\lambda=(a,b,-a-b)$, $a,b>0$, so that $L:=\sum\lambda_k=0$. Put
$$M:=a+b,\qquad P:=ab(a+b),\qquad \Lambda=\mathrm{diag}(a,b,-M),\qquad \Lambda'=\mathrm{diag}(a,b,M).$$
Orient $Y_4$ by $e_4\wedge e_1\wedge e_2\wedge e_3$ and let $\omega_k=e_4\wedge e_k+e_i\wedge e_j$ for $(i,j,k)$ cyclic; these form a basis of $\Lambda^+Y_4$. The Lie algebra $\mathfrak{su}(2)$ has basis $T_a$ with $[T_a,T_b]=\epsilon_{abc}T_c$, and we identify it with $(\mathbb R^3,\times)$. On $M_5=\mathbb R_s\times Y_4$ the HW equations [11, 12] for a connection $A$ on $M_5$ and a self-dual $\mathfrak{su}(2)$-valued 2-form $B$ on $Y_4$ are
$$\text{(H1)}\ \ F_Y^+-\tfrac14B\times B-\tfrac12\nabla_sB=0,\qquad\text{(H2)}\ \ \iota_sF+\star_Y d_AB=0,$$
where $\nabla_s=\partial_s+[A_s,\cdot\,]$ and $(B\times B)^c_{ij}=\epsilon_{cab}\sum_lB^a_{il}B^b_{jl}$. These are the conventions of [1], made covariant in $s$.

**The sector.** The most general configuration that is invariant under translations in $(x_1,x_2,x_3)$, written in an $\mathbb R^3$-invariant gauge, is
$$A=\sum_{k,a}A_{ka}(s,t)\,e_k\,T_a+A_4(s,t)\,dt+A_s(s,t)\,ds,\qquad B=\sum_{k,a}C_{ka}(s,t)\,\omega_k\,T_a,\qquad t=x_4,$$
with $A_4,A_s$ arbitrary $\mathfrak{su}(2)$-valued functions. The Klein sector of [1] is the case where $A_{ka},C_{ka}$ are diagonal and $A_4=A_s=0$. Put $Z=A+iC\in\mathbb C^{3\times3}$, with rows $z_k=A_k+iC_k\in\mathbb C^3\cong\mathfrak{sl}(2,\mathbb C)$; the row index is the form index and the column index is the Lie index. Let $D=\partial+a\times$ for the connection $a=A_s\,ds+A_4\,dt$, acting on each row, and $F_{st}=\partial_sA_4-\partial_tA_s+A_s\times A_4$. Define
$$S(Z)=\det Z+\tfrac12\mathrm{tr}(\Lambda ZZ^T)=\det Z+\tfrac12\sum_k\lambda_k\,z_k\cdot z_k,\qquad \mu(Z)=\sum_kA_k\times C_k=\tfrac12\epsilon\cdot\mathrm{Im}(Z^*Z).$$
Here $\partial S=\mathrm{cof}\,Z+\Lambda Z$, whose rows are $\lambda_kz_k+z_i\times z_j$. The function $S$ is invariant under $Z\mapsto ZR$, $R\in SO(3,\mathbb C)$. The map $\mu$ is the moment map of the real gauge action $Z\mapsto ZQ$, $Q\in SO(3)$, for the flat Kähler form: $\nabla\langle\mu,\phi\rangle=J(\phi\times Z)$, where $J$ is multiplication by $i$.

**Proposition 1.1 (exact reduction).** For configurations of the sector, (H1)–(H2) are equivalent to
$$(D_t+iD_s)z_k=-\overline{\partial_kS(Z)}-iL\,\mathrm{Im}\,z_k\quad(k=1,2,3),\qquad F_{st}=\mu(Z).\tag{1.1}$$
More precisely:
- the $\omega_m\,T_c$ component of (H1) is $-\frac12R^{(1)}_{mc}$;
- the $e_l\,T_c$ component of (H2) ($l\le3$) is $R^{(2)}_{lc}$;
- the $e_4\,T_c$ component of (H2) is $(F_{st}-\mu)_c$.

Here $-R^{(1)}+iR^{(2)}$ is the residual of the first equation of (1.1). No other components occur. For $L=0$, (1.1) reads $D_sZ=J(D_tZ+\nabla\mathrm{Re}\,S)$, $F_{st}=\mu$.

**Objects and morphisms.** An *object* is a solution on $Y_4$ of $F^+=\frac14B\times B$, $d_A^*B=0$ in the sector. These are exactly the $s$-independent solutions of (1.1) with $A_s=0$. By §2 they are pairs $(Z(t),A_4(t))$ with $D_tZ=-\nabla\mathrm{Re}\,S(Z)$ and $\mu(Z)\equiv0$. After the gauge transformation $g(t)$, $g'=-A_4g$, they become
$$z'=-\overline{\partial S(z)}=-\nabla\mathrm{Re}\,S(z),\qquad \mu(z)=0,\tag{1.2}$$
modulo the residual constant gauge group $SO(3)$ ("temporal gauge"). Since $\mu$ and $\mathrm{Im}\,S$ are conserved along the flow (§2), the Gauss law is a single constraint imposed at one time. *Morphisms* are $s$-dependent solutions of (1.1) that converge to objects as $s\to\pm\infty$. $|Z|$ is gauge invariant, so "bounded" is a gauge-invariant notion.

Let $z_*=\mathrm{diag}\big(i\sqrt{bM},-i\sqrt{aM},\sqrt{ab}\big)$, which is the critical point $z_*$ of [1] written as a diagonal matrix. Let $\kappa$ be the kink of [1, Theorem A]. As a diagonal matrix it is $\kappa(t)=\mathrm{diag}(iu(t),-iv(t),w(t))$, with $u,v,w>0$ strictly increasing from $0$ to $(\sqrt{bM},\sqrt{aM},\sqrt{ab})$.

> **Main Theorem.** Let $a,b>0$.
>
> **(A) Vacua.** $\mathrm{Crit}\,S=\{0\}\cup\mathcal O_*$, where $\mathcal O_*=z_*SO(3,\mathbb C)=\{Z:\ ZZ^T=-P\Lambda^{-1},\ \det Z=P\}$ is a closed, noncompact complex 3-manifold. The critical values $S(0)=0$ and $S|_{\mathcal O_*}=-P/2$ are real.
> - $0$ is nondegenerate.
> - $\mathcal O_*$ is Morse–Bott: $\ker\mathrm{Hess}\,S=T\mathcal O_*$, $\mathrm{Hess}\,\mathrm{Re}\,S$ has signature $(6,6)$ on the normal space, and $\mathrm{Hess}\,\mathrm{Re}\,S(0)$ has signature $(9,9)$.
> - The Gauss law selects $\mathcal O_*\cap\mu^{-1}(0)=z_*SO(3)$, on which $SO(3)$ acts freely.
>
> So there are exactly two gauge classes of vacua (left-invariant objects), $[0]$ and $[z_*]$, as in the Klein sector. The four Klein images of [1] are gauge equivalent.
>
> **(B) Objects.**
> 1. For a solution of (1.2), three conditions are equivalent: $z$ is bounded; $\int|z'|^2<\infty$; $\mathrm{Re}\,S\circ z$ is bounded. Unbounded solutions have $\mathrm{Re}\,S\to-\infty$ forward or $\to+\infty$ backward.
> 2. The bounded solutions of (1.2) are exactly:
>    - the constants $0$ and $z_*Q$, $Q\in SO(3)$;
>    - the curves $t\mapsto\kappa(t+\tau)\,Q$, $\tau\in\mathbb R$, $Q\in SO(3)$, and the pair $(\tau,Q)$ is uniquely determined by the curve.
>
>    Hence, up to gauge, the bounded objects of the full sector are $0$, $z_*$ and the translates of $\kappa$. Between the vacua $[0]$ and $[z_*]$ there is exactly one soliton up to translation and gauge, and there is none in the opposite direction or between equal vacua.
>
> **(C) Linearization.** Let $H(t)=\mathrm{Hess}\,\mathrm{Re}\,S(\kappa(t))$ on $\mathbb R^{18}$.
> 1. The space $K$ of solutions of $\xi'=-H\xi$ that tend to $0$ as $t\to-\infty$ and are bounded on $[0,\infty)$ is $K=\mathbb R\kappa'\oplus\kappa\,\mathfrak{so}(3)$, of dimension $4$.
> 2. For small $\delta>0$, let $L^2_\delta$ require decay like $e^{-\delta t}$ at $+\infty$. Then $\mathcal P=d/dt+H:H^1_\delta\to L^2_\delta$ is Fredholm of index $-3$, with $\ker\mathcal P=\mathbb R\kappa'$ and $\operatorname{coker}\mathcal P\cong JK=\mathrm{span}\{\nabla\mathrm{Im}\,S,\nabla\mu_1,\nabla\mu_2,\nabla\mu_3\}(\kappa)$.
> 3. Equivalently, $W^u(0)$ and the stable manifold of $z_*SO(3)$ meet transversally, along the 4-dimensional family $SO(3)\cdot\kappa(\mathbb R)$, inside the 14-dimensional level set $\mathcal N=\{\mathrm{Im}\,S=0,\ \mu=0\}$.
> 4. Modulo infinitesimal gauge transformations, the deformations of $\kappa$ as a bounded object form the line $\mathbb R\kappa'$ (Morse–Bott family of translates).
> 5. The Hessian of the action at an object, in $Z$-directions, is $\mathcal H_x=J\mathcal P_x$. This corrects the sign of [1].
>
> **(D) Morphisms.** Every bounded object has action $\mathcal A=0$. In the class $\mathfrak M$ of Definition 8.1 (temporal gauge in $s$, bounded, uniform integrable decay in $t$), every solution of (1.1) is $s$-independent. So the HW flow category of the sector, with bounded objects and class-$\mathfrak M$ morphisms, has object classes $[0]$, $[z_*]$ and $\{[\kappa(\cdot+\tau)]\}_{\tau\in\mathbb R}$, and only identity morphisms.

The gauge-invariant function $|B|^2\propto\sum_k|C_k|^2$ equals $u^2+v^2$ along $\kappa Q$, which is strictly increasing. So the geometric statements of [1, (C)] persist. The kinks are pairwise gauge-inequivalent $\mathbb R^3$-invariant KW solutions that descend to $T^3\times\mathbb R$ but to no compact quotient $\Gamma\backslash Y_4$, even up to gauge.

**What is new.**
- The reduction with the full gauge field and the Gauss law (Proposition 1.1), and the gauged energy and action identities (§2).
- The critical set with its Morse–Bott and Gauss-law structure, including an elementary Kempf–Ness-type argument (Lemma 3.2).
- An a priori estimate that holds *on the Gauss-law cone* (Lemma 4.1). Without the Gauss law it is false, because $\mathcal O_*$ is noncompact.
- A general slice lemma for quadratic equivariant vector fields (Lemma 5.1).
- **The Gram-matrix identity** (Proposition 6.1), which reduces every bounded slice orbit to the diagonal Klein slice.
- The explicit spectrum of the slice Hessian at $x_*$ (Proposition 7.1).
- The transversality and index $-3$ statement with the Gauss law (Theorem 7.3).
- The gauged no-morphism argument (Proposition 8.2).

**What is imported.**
- The classification of bounded orbits in the Klein slice [1, Theorem A(3)–(4)], used once, in the proof of (B).
- The action-based exclusion of trajectories between objects of equal action. It goes back to rStation math_48 [4, Proposition 7.3] and was used in [1, Proposition 9.3]; §8 adapts it to the gauge field.
- Standard tools:
  - the stable manifold theorem;
  - Levinson's asymptotic theorem for $\xi'=(A_\infty+R(t))\xi$ with $R\in L^1$ [9, Ch. 3, Thm 8.1];
  - the Robbin–Salamon index formula [8];
  - Łojasiewicz's gradient inequality [13];
  - polar decomposition of complex orthogonal matrices.

The numerics in `verify.py` §9 are illustrations only.

## 2. The reduction, the Gauss law, energy and action

Proposition 1.1 is a finite computation in the exterior algebra of the coframe $(e_1,e_2,e_3,e_4,ds)$, with $de_i=\lambda_ie_4\wedge e_i$, $F=dA+\frac12[A\wedge A]$ and $d_AB=dB+[A\wedge B]$. `verify.py` §1 performs it symbolically for 18 arbitrary functions $A_{ka},C_{ka}$ and 6 arbitrary functions in $A_4,A_s$, with $\lambda$ general. It checks:
- all 9 self-dual components of (H1);
- the 9 components $e_lT_c$ ($l\le3$) of (H2);
- the 3 components $e_4T_c$ of (H2).

The result is the following system, written in vector notation with $L$ general:
$$\begin{aligned}
R^{(1)}_k&:=D_sC_k-D_tA_k-\big(\lambda_kA_k+A_i\times A_j-C_i\times C_j\big)=0,\\
R^{(2)}_k&:=D_sA_k+D_tC_k+LC_k-\big(A_i\times C_j+C_i\times A_j+\lambda_kC_k\big)=0,\\
G&:=F_{st}-\textstyle\sum_kA_k\times C_k=0 .
\end{aligned}\tag{2.1}$$
The Gauss law is the $e_4$-component of (H2): the $e_1\wedge e_2\wedge e_3$ part of $d_AB$ is $\sum_k[A_k,C_k]$, and $\iota_sF$ contributes $F_{s4}$. As a negative control, the coefficient $\frac12$ in place of $\frac14$ in front of $B\times B$ destroys the reduction, and so does the opposite sign of $\mu$ in $G$.

`verify.py` §2 checks the following.
- The algebraic terms are $\partial_{A}\mathrm{Re}\,S$ and $-\partial_C\mathrm{Re}\,S$, and also $\partial_A\mathrm{Im}\,S$ and $\partial_C\mathrm{Im}\,S$ (Cauchy–Riemann).
- $-R^{(1)}+iR^{(2)}$ is the residual of (1.1).
- $S(ZR)=S(Z)$ for $R\in SO(3,\mathbb C)$ (Cayley parametrization with complex parameters).
- $\mu=\frac12\epsilon\cdot\mathrm{Im}(Z^*Z)$, so $\mu(Z)=0$ iff $Z^*Z$ is real.
- $\nabla\langle\mu,\phi\rangle=J(\phi\times Z)$.

**Energy identity.** For $L=0$, pointwise on $\mathbb R^2$ (`verify.py` §2):
$$|R^{(1)}|^2+|R^{(2)}|^2+|G|^2=|D_tZ|^2+|D_sZ-\nabla\mathrm{Im}\,S|^2+|F_{st}|^2+|\mu|^2+2\partial_t\mathrm{Re}\,S+2\sum_k\big[\partial_t(C_k\cdot D_sA_k)-\partial_s(C_k\cdot D_tA_k)\big].\tag{2.2}$$
The cross term $-2F_{st}\cdot\mu$ from $|G|^2$ is cancelled exactly by the commutator $[D_s,D_t]=F_{st}\times$.

**Action.** Every configuration can be put in temporal gauge $A_s=0$ by solving $\partial_sg=-A_sg$ on $\mathbb R^2$. Then (1.1) with $L=0$ reads
$$\partial_sZ=J(D_tZ+\nabla\mathrm{Re}\,S),\qquad\partial_sA_4=\mu(Z),\tag{2.3}$$
which is the $L^2$-gradient flow of the gauge-invariant action
$$\mathcal A(Z,A_4)=\int_{\mathbb R}\Big(\sum_kC_k\cdot D_tA_k+\mathrm{Im}\,S(Z)\Big)dt .\tag{2.4}$$
Indeed $\partial_{A_4}$ of the density is $\mu$. The Euler–Lagrange gradient in $Z$ is $J D_tZ+\nabla\mathrm{Im}\,S=J(D_tZ+\nabla\mathrm{Re}\,S)$, using $\nabla\mathrm{Im}\,S=J\nabla\mathrm{Re}\,S$. Along solutions of (2.3),
$$\partial_s\Big(\sum_kC_k\cdot D_tA_k+\mathrm{Im}\,S\Big)=|\partial_sZ|^2+|\partial_sA_4|^2+\partial_t\Big(\sum_kC_k\cdot\partial_sA_k\Big).\tag{2.5}$$
The density of (2.4) is pointwise invariant under $t$-dependent gauge transformations (checked infinitesimally, with $\delta z_k=\phi\times z_k$ and $\delta A_4=-\partial_t\phi+\phi\times A_4$).

**Objects.** For $s$-independent fields with $A_s=0$ we have $F_{st}=\partial_sA_4=0$, so the Gauss law is $\mu(Z)=0$ pointwise in $t$. Also $\iota_sF=0$, so (H2) is $d_AB=0$, which for self-dual $B$ is $d_A^*B=0$, and (H1) is $F^+=\frac14B\times B$. Since $S$ is holomorphic, along (1.2) we have $\frac{d}{dt}S(z)=-|\partial S|^2$: $\mathrm{Re}\,S$ decreases strictly off critical points and $\mathrm{Im}\,S$ is constant. By gauge invariance $dS(\phi\times Z)=0$, so
$$\tfrac{d}{dt}\langle\mu,\phi\rangle=\langle J(\phi\times z),-\nabla\mathrm{Re}\,S\rangle=\langle\phi\times z,J\nabla\mathrm{Re}\,S\rangle=d\,\mathrm{Im}\,S(\phi\times z)=0,$$
and $\mu$ is conserved (`verify.py` §7).

## 3. Critical set and Gauss law

**Lemma 3.1.** $\mathrm{Crit}\,S=\{0\}\cup\mathcal O_*$ with $\mathcal O_*=\{ZZ^T=-P\Lambda^{-1},\ \det Z=P\}=z_*SO(3,\mathbb C)$, and $S|_{\mathcal O_*}=-P/2$.

*Proof.* At a critical point $\mathrm{cof}\,Z=-\Lambda Z$. Multiplying by $Z^T$ on the right and using $\mathrm{cof}(Z)Z^T=\det(Z)I$ gives $\det(Z)\,I=-\Lambda ZZ^T$.
- *$\mathrm{rank}\,Z=2$.* Then $\mathrm{cof}\,Z$ has rank 1, while $\Lambda Z$ has rank 2. This is impossible.
- *$\mathrm{rank}\,Z\le1$.* Then $\mathrm{cof}\,Z=0$, so $\Lambda Z=0$ and $Z=0$.
- *$\det Z=:d\ne0$.* Then $ZZ^T=-d\Lambda^{-1}$, and taking determinants gives $d^2=-d^3/\det\Lambda=d^3/P$, so $d=P$. Since $z_*z_*^T=-P\Lambda^{-1}$ and $\det z_*=P$, the matrix $R:=z_*^{-1}Z$ satisfies $RR^T=I$ and $\det R=1$.

Conversely, $z_*$ is critical and $S$ is $SO(3,\mathbb C)$-invariant, so $z_*R$ is critical. The value is $S=P+\frac12\mathrm{tr}(\Lambda\cdot(-P\Lambda^{-1}))=-P/2$. All of this is checked in `verify.py` §3, including criticality of $z_*R$ for a symbolic complex rotation $R$. ∎

**Lemma 3.2 (Gauss law on $\mathcal O_*$).** $\mathcal O_*\cap\mu^{-1}(0)=z_*SO(3)$.

*Proof.* Let $R\in SO(3,\mathbb C)$.

*Polar decomposition.* Since $\bar R\in O(3,\mathbb C)$, the positive Hermitian matrix $E^2:=R^*R=\bar R^{-1}R$ satisfies $\overline{E^2}=E^{-2}$. Writing $E^2=e^K$ with $K$ Hermitian, uniqueness of the Hermitian logarithm gives $\bar K=-K$. Hence $K=iY$ with $Y$ real antisymmetric, and $E=e^{iY/2}\in SO(3,\mathbb C)$. Then $U:=RE^{-1}\in SO(3,\mathbb C)\cap U(3)=SO(3)$.

*The Gauss law.* For $Z=z_*UE$ we get $Z^*Z=ENE$ with $N=U^T\mathrm{diag}(bM,aM,ab)U$ real, symmetric and positive definite. By §2, $\mu(Z)=0$ iff $ENE$ is real, that is, iff $ENE=\bar E N\bar E=E^{-1}NE^{-1}$, that is, iff $E^2NE^2=N$. Then $K':=N^{1/2}E^2N^{1/2}$ is positive Hermitian with $K'^2=N^2$, so $K'=N$, $E^2=I$, and $Z=z_*U$. Conversely $\mu(z_*U)=0$, since $(z_*U)^*z_*U=U^T\mathrm{diag}(bM,aM,ab)U$ is real. ∎

This is the Kempf–Ness picture [10] in an elementary form. The noncompact directions $z_*e^{i\tau X}$ of $\mathcal O_*$ are critical but violate the Gauss law, and $|z_*e^{i\tau X}|\to\infty$ (`verify.py` §3).

**Lemma 3.3 (Morse–Bott).** $\mathrm{Hess}\,S(0)=\Lambda\otimes I_3$ is invertible. $\mathrm{Hess}\,S(z_*)$ has complex rank 6, with kernel $z_*\mathfrak{so}(3,\mathbb C)=T_{z_*}\mathcal O_*$. Consequently $\mathrm{Hess}\,\mathrm{Re}\,S$ has signature $(9,9)$ at $0$. At points of $\mathcal O_*$ it has a 6-dimensional kernel $T\mathcal O_*$ and signature $(6,6)$ on a complement.

*Proof.* The ranks and the kernel are computed exactly with symbolic $a,b$ (`verify.py` §3). By $SO(3,\mathbb C)$-invariance, the same holds at every point of $\mathcal O_*$. $\mathrm{Hess}\,\mathrm{Re}\,S$ anticommutes with $J$, so its nonzero eigenvalues come in pairs $\pm$. ∎

The stabilizer of $z_*$ in $SO(3)$ is trivial, because $z_*$ is invertible. This proves (A).

## 4. An a priori estimate on the Gauss-law cone

**Lemma 4.1.** There are $c_0>0$ and $R_0$, depending on $a,b$, such that $|\partial S(Z)|\ge c_0|Z|$ for all $Z\in\mu^{-1}(0)$ with $|Z|\ge R_0$.

*Proof.* Suppose not. Then there are $Z_n\in\mu^{-1}(0)$ with $|Z_n|\to\infty$ and $|\partial S(Z_n)|\le|Z_n|/n$. Put $Y_n=Z_n/|Z_n|$. After passing to a subsequence, $Y_n\to Y$ with $|Y|=1$ and $\mu(Y)=0$, since $\mu$ is a homogeneous quadratic.

*$Y$ has rank one.* We have $\mathrm{cof}\,Y_n=(\partial S(Z_n)-\Lambda Z_n)/|Z_n|^2\to0$, so $\mathrm{cof}\,Y=0$ and $\mathrm{rank}\,Y\le1$. Thus $Y=pq^T$ with $p,q\neq0$.

*$q\cdot q=0$.* The identity $\partial S\,Z^T=\det(Z)\,I+\Lambda ZZ^T$, divided by $|Z_n|^2$, gives
$$|Z_n|\det(Y_n)\,I+\Lambda Y_nY_n^T\to0 .$$
Hence the scalars $|Z_n|\det Y_n$ converge to some $c$, and $YY^T=-c\Lambda^{-1}$. The left side has rank $\le1$, so $c=0$ and $YY^T=(q\cdot q)\,pp^T=0$. Since $pp^T\neq0$, this means $q\cdot q=0$.

*$q\cdot q\ne0$.* On the other hand, $\mathrm{Im}(Y^*Y)=|p|^2\,\mathrm{Im}(\bar qq^T)=0$, so $\bar q_aq_b\in\mathbb R$ for all $a,b$. Choosing $a_0$ with $q_{a_0}\neq0$, we get $q=q_{a_0}r$ with $r$ real and nonzero. Then $q\cdot q=q_{a_0}^2|r|^2\neq0$, a contradiction. ∎

The constant is not explicit. Random sampling of $\mu^{-1}(0)$ in `verify.py` §9 ($a=1,b=2$, $|Z|\in[10,1000]$) gives $|\partial S|/|Z|\ge2.37$. An exploratory constrained minimization (not part of `verify.py`) found values close to $\min(a,b)$, attained near the complex axes. Both are illustrations only. Without the Gauss law the lemma fails, because $\mathcal O_*$ is unbounded.

**Proposition 4.2.** Let $z$ solve (1.2) on its maximal interval.
1. If $\mathrm{Re}\,S\circ z\ge-K$ forward in time, then $z$ is bounded and global forward, and it converges to a point of $\mathrm{Crit}\,S\cap\mu^{-1}(0)=\{0\}\cup z_*SO(3)$.
2. The same holds backward if $\mathrm{Re}\,S\circ z\le K$.
3. Hence (B1) holds.

*Proof.* The argument is that of [1, Prop. 4.2], with Lemma 4.1 in place of [1, Lemma 4.1]; it applies because $z(t)\in\mu^{-1}(0)$ for all $t$. Let $E_0=\mathrm{Re}\,S(z(t_0))+K$. On a stretch where $|z|$ runs from $R_1\ge\max(R_0,|z(t_0)|)$ to $R_2$ while staying $\ge R_1$,
$$E_0\ge\int|z'|^2=\int|z'||\partial S|\ge c_0R_1(R_2-R_1).$$
So $z$ is bounded.

The $\omega$-limit set is nonempty, compact and connected. It lies in $\mathrm{Crit}\,S\cap\mu^{-1}(0)$, since $\mu$ is conserved. $\mathrm{Re}\,S$ is a polynomial, so Łojasiewicz's inequality [13] gives convergence to a single point.

For (3): finite energy means bounded total decrease of $\mathrm{Re}\,S$; bounded $\mathrm{Re}\,S$ then gives boundedness by (1) and (2); and boundedness gives bounded $\mathrm{Re}\,S$. The axis solutions $z=\mathrm{diag}(z_1(t),0,0)$ with $z_1'=-a\bar z_1$ have $\mu=0$, are unbounded and exist for all time. So unboundedness does not imply finite-time blow-up. ∎

## 5. The unstable manifold of $0$ lies in a 9-dimensional slice

Let $E=\mathrm{diag}(-1,-1,1)$ and $\sigma(Z)=E\bar Z$. Then:
- $\sigma$ is an antiholomorphic isometric involution with $S\circ\sigma=\bar S$;
- it commutes with the real gauge action;
- its fixed set is
$$\Sigma'=\{(iu;\,-iv;\,w):\ u,v,w\in\mathbb R^3\}\cong\mathbb R^{3\times3}\ni X=\begin{pmatrix}u\\v\\w\end{pmatrix}.$$

On $\Sigma'$ we have $\mu\equiv0$, $\mathrm{Im}\,S\equiv0$ and $\mathrm{Re}\,S=-g$ (`verify.py` §4), where
$$g(X)=\tfrac12\mathrm{tr}(\Lambda'XX^T)-\det X,\qquad X'=\nabla g(X)=\Lambda'X-\mathrm{cof}\,X,\tag{5.1}$$
that is, $u'=au-v\times w$, $v'=bv-w\times u$, $w'=Mw-u\times v$. The diagonal matrices $X$ form the Klein slice of [1], in its coordinates $(u,v,w)$.

**Lemma 5.1.**
1. *(General slice lemma.)* Let $F=F_1+F_2$ be a vector field on a Euclidean space $V$, with $F_1$ linear and $F_2$ a homogeneous quadratic. Suppose $F$ commutes with an orthogonal involution $\sigma$, and write $V=V^+\oplus V^-$ for its eigenspaces. Then the $V^-$-component of $F(x^++x^-)$ equals $L(x^+)x^-$, where $L(x^+)$ is linear in $x^-$ and depends affinely on $x^+$.
2. If $z$ solves (1.2) and $z(t)\to0$ as $t\to-\infty$, then $z(t)\in\Sigma'$ for all $t$.

*Proof.*
1. Let $\beta$ be the symmetric bilinear form with $F_2(x)=\beta(x,x)$. Then
$$F(x^++x^-)=F_1x^++F_2(x^+)+F_1x^-+2\beta(x^+,x^-)+F_2(x^-).$$
Equivariance gives $\sigma F_2(x^-)=F_2(-x^-)=F_2(x^-)\in V^+$. Likewise $F_1x^+,F_2(x^+)\in V^+$, while $F_1x^-$ and $\beta(x^+,x^-)$ lie in $V^-$.
2. Apply (1) to $F=-\nabla\mathrm{Re}\,S$. Here $V^-$, the $(-1)$-eigenspace of $\sigma$, is spanned by the coordinates $N=(A_1,A_2,C_3)$: the real parts of rows 1 and 2 and the imaginary part of row 3. This gives exactly $N'=L(X)N$, and $L(0)=-\mathrm{diag}(aI_3,bI_3,MI_3)$ (`verify.py` §4). As $t\to-\infty$, $L(X(t))\to L(0)$. Choose $T_0$ with $\|L(X(t))-L(0)\|\le m/2$ for $t\le T_0$, where $m=\min(a,b)$. Then $\frac{d}{dt}|N|^2\le-m|N|^2$ on $(-\infty,T_0]$. Since $N\to0$, this forces $N(T_0)=0$, and uniqueness for the linear equation gives $N\equiv0$. ∎

The linearization of (1.2) at $0$ is diagonal, with unstable subspace $T_0\Sigma'$ of dimension $9$. $0$ is a hyperbolic source of (5.1), since $\mathrm{Hess}\,g(0)=\mathrm{diag}(aI_3,bI_3,MI_3)$. So $W^u(0)$ is an open subset of $\Sigma'$. Lemma 5.1 is the general form of [1, Lemma 5.1], whose proof used the Klein ansatz.

## 6. Gram-matrix rigidity and the classification of bounded objects

**Proposition 6.1 (Gram identity).** Along (5.1), $\Gamma=XX^T$ satisfies
$$\Gamma'=\Lambda'\Gamma+\Gamma\Lambda'-2\det(X)\,I .\tag{6.1}$$
Consequently, every solution of (5.1) that is bounded on $[0,\infty)$ has mutually orthogonal rows for all $t$. Every bounded entire solution is $X(t)=D(t)Q$ with $Q\in SO(3)$ constant and $D(t)$ a bounded solution of the diagonal (Klein-slice) system of [1].

*Proof.* We have $X'X^T=\Lambda'\Gamma-\mathrm{cof}(X)X^T=\Lambda'\Gamma-\det(X)I$, which gives (6.1) (`verify.py` §5). Off the diagonal, (6.1) reads $\Gamma_{ij}'=(\lambda_i'+\lambda_j')\Gamma_{ij}$, so
$$\Gamma_{ij}(t)=\Gamma_{ij}(0)e^{(\lambda'_i+\lambda'_j)t},\qquad\lambda'_i+\lambda'_j\in\{a+b,\ 2a+b,\ a+2b\}.$$
All three rates are positive, so boundedness on $[0,\infty)$ forces $\Gamma_{ij}\equiv0$.

Fix $t_0$. A matrix with orthogonal rows can be written $X(t_0)=D_0Q$ with $D_0$ real diagonal and $Q\in SO(3)$: normalize the nonzero rows, complete to an orthonormal basis, and fix the determinant by changing the sign of one entry of $D_0$. For $Q\in SO(3)$ we have $\mathrm{cof}(DQ)=\mathrm{cof}(D)Q$, and diagonal matrices are invariant under (5.1). So the solution $D(t)$ of the diagonal system with $D(t_0)=D_0$ gives a solution $D(t)Q$ of (5.1) with the same value at $t_0$. By uniqueness, $X=DQ$. On diagonal matrices $g$ is the potential $-uvw+\frac12(au^2+bv^2+Mw^2)$ of [1, (3.1)]. ∎

*Proof of (B2).* Constant solutions are the points of $\mathrm{Crit}\,S\cap\mu^{-1}(0)$; see §3.

Let $z$ be a nonconstant bounded solution of (1.2). Then $\mathrm{Re}\,S\circ z$ is strictly decreasing, with limits $\ell_->\ell_+$ that are critical values. So $\ell_-=0$ and $\ell_+=-P/2$. The $\alpha$-limit set lies in $\mathrm{Crit}\cap\mu^{-1}(0)\cap\{\mathrm{Re}\,S=0\}=\{0\}$, so $z(t)\to0$ as $t\to-\infty$. By Lemma 5.1, $z$ lies in $\Sigma'$. By Proposition 6.1, $z=D(\cdot)Q$ with $D$ a bounded nonconstant solution in the Klein slice.

By [1, Theorem A(3)–(4)], $D=\kappa_j(\cdot+\tau)=\kappa(\cdot+\tau)k_j$ for some $j$ and $\tau$, where $k_j\in SO(3)$ is a diagonal sign matrix. So $z=\kappa(\cdot+\tau)Q'$ with $Q'=k_jQ$. Conversely, every $\kappa(\cdot+\tau)Q$ is a bounded solution, by equivariance, and it satisfies $\mu=0$ because it lies in $\Sigma'$.

*Uniqueness of $(\tau,Q')$.* $|z(t)|^2$ restricted to the first two rows is $u^2+v^2$ at $t+\tau$, which is strictly increasing, so $\tau$ is unique. $\kappa(t)$ is invertible for every $t$, so $Q'$ is unique. ∎

*Remark (dimension count).* In $\mathcal N=\{\mathrm{Im}\,S=0,\mu=0\}$, which has dimension $18-4=14$, the expected dimension of $W^u(0)\cap W^s(z_*SO(3))$ is
$$\dim W^u(0)+\dim W^s(z_*SO(3))-\dim\mathcal N=9+9-14=4=1\ (\text{translation})+3\ (\text{gauge}).$$
So solitons are expected to be isolated modulo symmetries, in the Picard–Lefschetz sense of [7, §§10–11]. (B2) shows there is exactly one, with no genericity assumption, and §7 shows that it is cut out transversally.

## 7. Linearization, transversality and the Morse–Bott property

**Proposition 7.1 (slice Hessian at $x_*$).** Let $x_*=\mathrm{diag}(\sqrt{bM},\sqrt{aM},\sqrt{ab})$. Then $\mathrm{Hess}\,g(x_*)$ on $\mathbb R^9$ is block diagonal:
- the diagonal coordinates carry the Klein-slice Hessian of [1], with determinant $-4P$, trace $2M$ and signature $(-,+,+)$;
- each pair $(x_{ij},x_{ji})$, $i<j$, carries the block $\begin{pmatrix}\lambda_i'&x_k\\x_k&\lambda'_j\end{pmatrix}$, where $x_k$ is the remaining diagonal entry of $x_*$. Each such block has determinant $0$ and eigenvalues $0$ and $\lambda'_i+\lambda'_j$.

Hence the characteristic polynomial is $\lambda^3(\lambda-a-b)(\lambda-2a-b)(\lambda-a-2b)\,c_{[1]}(\lambda)$, where $c_{[1]}$ is the characteristic polynomial of the Klein-slice block. Thus $\mathrm{Hess}\,g(x_*)$ has exactly one negative eigenvalue $-\mu_*$, a kernel $x_*\mathfrak{so}(3)$, and five positive eigenvalues (`verify.py` §7). The positive eigenvalues $\lambda'_i+\lambda'_j$ are the Gram growth rates of (6.1).

**Proposition 7.2.** $K=\mathbb R\kappa'\oplus\kappa\,\mathfrak{so}(3)$ has dimension $4$.

*Proof.* The isometry $\sigma$ fixes $\kappa$ pointwise and preserves $\mathrm{Re}\,S$, so $d\sigma$ commutes with $H(t)$ (checked in `verify.py` §7). Split $\xi\in K$ into a tangential part $\xi_+\in T\Sigma'$ and a normal part $\xi_-$.

*Normal part.* By Lemma 5.1 the normal equation is linear, so its linearization at $N=0$ is the same equation $\xi_-'=L(\kappa)\xi_-$. The estimate in that proof gives $\xi_-\equiv0$.

*Tangential part.* $\xi_+$ solves $\xi_+'=\mathrm{Hess}\,g(\kappa(t))\xi_+$. As $t\to+\infty$ the coefficient converges exponentially to the symmetric matrix $\mathrm{Hess}\,g(x_*)$, since $\kappa\to x_*$ at rate $\mu_*$ [1]. By Levinson's theorem [9, Ch. 3, Thm 8.1], the solution space has a basis $(v_j+o(1))e^{\alpha_jt}$, where the $\alpha_j$ are the eigenvalues. Those bounded on $[0,\infty)$ span a space of dimension $3+1=4$. As $t\to-\infty$ the coefficient tends to $\mathrm{Hess}\,g(0)>0$, so every solution decays there. Hence $\dim K=4$.

*The basis.* $\kappa'$ decays at both ends. Each $\kappa X$ is a Jacobi field, the derivative of the solutions $\kappa e^{\epsilon X}$; it tends to $0$ at $-\infty$ and to $x_*X$ at $+\infty$. These four fields are linearly independent: $\kappa X$ has zero diagonal while $\kappa'$ is diagonal and nonzero, and $\kappa(t)$ is invertible. ∎

**Theorem 7.3 (transversality with the Gauss law).** Fix $0<\delta<\min(\mu_*,\lambda_{\min}^+)$, where $\lambda^+_{\min}$ is the smallest positive eigenvalue of $\mathrm{Hess}\,\mathrm{Re}\,S(z_*)$. Let $w_\delta$ be a smooth weight equal to $1$ for $t\le0$ and $e^{\delta t}$ for $t\ge1$, and set $L^2_\delta=w_\delta^{-1}L^2$, $H^1_\delta=w_\delta^{-1}H^1$. Then $\mathcal P=d/dt+H(t):H^1_\delta\to L^2_\delta$ is Fredholm of index $-3$, with
$$\ker\mathcal P=\mathbb R\kappa',\qquad\operatorname{coker}\mathcal P\cong JK=\mathrm{span}\{J\kappa',\ J\kappa X\}=\mathrm{span}\{\nabla\mathrm{Im}\,S(\kappa),\ \nabla\mu_c(\kappa)\}.$$
Equivalently, $T W^u(0)\cap TW^s(z_*SO(3))=K$ along $\kappa$. Since $\dim\mathcal N=14=9+9-4$, the intersection is transverse inside $\mathcal N$.

*Proof.* Conjugating by $w_\delta$ turns $\mathcal P$ into $d/dt+H-w_\delta'/w_\delta$, whose limits are $H(-\infty)=\mathrm{Hess}\,\mathrm{Re}\,S(0)$ with $n_-=9$, and $H(+\infty)-\delta$ with $n_-=6+6=12$. Both limits are nondegenerate. By Robbin–Salamon [8], $\mathcal P$ is Fredholm with index $9-12=-3$.

*Kernel.* The kernel consists of the elements of $K$ that decay at $+\infty$. Since $c\kappa'+\kappa X\to x_*X$, these form $\mathbb R\kappa'$.

*Cokernel.* The adjoint $-d/dt+H$ acts on $L^2_{-\delta}$, where growth slower than $e^{\delta t}$ is allowed at $+\infty$. Since $HJ=-JH$, the map $\eta=J\xi$ sends solutions of $\xi'=-H\xi$ to solutions of $\eta'=H\eta$. So $JK\subset\ker\mathcal P^*$, and these elements are $L^2_{-\delta}$. Counting, $\dim\operatorname{coker}=1-(-3)=4=\dim JK$.

*Identification.* $J\kappa'=-J\nabla\mathrm{Re}\,S=-\nabla\mathrm{Im}\,S$, and $J(\phi\times\kappa)=\nabla\langle\mu,\phi\rangle$ (§2). These four gradients are linearly independent: $\nabla\mathrm{Re}\,S\perp\kappa\,\mathfrak{so}(3)$ by gauge invariance, and $J$ is an isometry. So $\mathcal N$ is a 14-manifold near $\kappa(\mathbb R)$, and the cokernel is its normal space.

*Geometric form.* By standard Morse–Bott theory [14], the stable manifold of $z_*SO(3)$ is a 9-dimensional manifold fibred over $z_*SO(3)$ by the strong stable fibres of $\mathcal O_*$. A vector tangent to $W^u(0)$ and to this manifold is the initial value of a Jacobi field in $K$. Conversely, $K$ is tangent to the family $SO(3)\cdot\kappa(\mathbb R)$, which lies in both manifolds. ∎

`verify.py` §9 confirms numerically, by principal angles at $t=0$ for $a=1,b=2$, that $T W^u(0)\cap TW^s(\mathcal O_*)$ is 4-dimensional and equals $\mathrm{span}(\kappa',\kappa\,\mathfrak{so}(3))$.

**Corollary 7.4 (Morse–Bott modulo gauge).** In temporal gauge, the infinitesimal deformations of $\kappa$ as a bounded object are the Jacobi fields that decay at $-\infty$, are bounded at $+\infty$, and satisfy the linearized Gauss law. The linearized Gauss law $\langle\nabla\mu_c,\xi\rangle$ is constant in $t$, because $\nabla\mu_c(\kappa)$ solves the adjoint equation, and it vanishes at $-\infty$; so it holds automatically. These deformations therefore form $K$. Modulo the infinitesimal constant gauge transformations $\kappa\,\mathfrak{so}(3)$ they form $\mathbb R\kappa'$, the tangent line of the family of translates.

**The action Hessian (sign).** By (2.3), linearizing at an object $x$ (temporal gauge, $A_4=0$) in $Z$-directions gives $\partial_s\xi=J(\xi_t+H_x\xi)=J\mathcal P_x\xi$. This is the Hessian of $\mathcal A$, since $\mathrm{Hess}\,\mathrm{Im}\,S=J\,\mathrm{Hess}\,\mathrm{Re}\,S$ (`verify.py` §2 checks the Euler–Lagrange gradient and its linearization, and that $-J\mathcal P$ is not it). This corrects the sign $-J\mathcal P$ in [1, Thm (B), §7], as pointed out in its referee report. The statements built on it in [1] (self-adjointness, invertibility at constants, kernel at $\kappa$) are unaffected.

With $A_4$-variations $\alpha$ the Hessian has the block form $(\xi,\alpha)\mapsto(J\mathcal P\xi+J(\alpha\times\kappa),\ d\mu_\kappa\xi)$, which is symmetric. We do not develop a Fredholm theory for this extended operator.

## 8. Morphisms

**Definition 8.1.** Let $\mathfrak M$ be the class of smooth solutions $(Z,A_s,A_4)$ of (1.1) on $\mathbb R^2$, with $L=0$, which after a gauge transformation to $A_s=0$ satisfy the following.
- (M1) $Z$ is bounded, and there are $p_\pm(s)\in\mathrm{Crit}\,S$ with $\sup_s|Z(s,t)-p_\pm(s)|\to0$ as $t\to\pm\infty$.
- (M2) There is $h\in L^1(\mathbb R)$ with $|Z(s,t)-p_{\mathrm{sgn}\,t}(s)|+|\partial_tZ(s,t)|+|A_4(s,t)|\le h(t)$ for all $s,t$.
- (M3) As $s\to\pm\infty$, $(Z,A_4)(s,\cdot)\to(Z_\pm,A_{4,\pm})$ in $C^1_{\rm loc}$, and the limits are objects.

**Proposition 8.2.** Every element of $\mathfrak M$ is $s$-independent in temporal gauge, that is, $\partial_sZ\equiv0$ and $\partial_sA_4\equiv0$.

*Proof.* *The action is finite.* For each $s$, $\mathcal A(s)$ from (2.4) converges absolutely: $|C\cdot D_tA|\le c(|\partial_tZ|+|A_4|)\le c\,h$, and $|\mathrm{Im}\,S(Z)|=|\mathrm{Im}\,S(Z)-\mathrm{Im}\,S(p_\pm)|\le c\,h$, because all critical values are real (Lemma 3.1).

*Action identity.* By (2.3),
$$|\partial_sZ|\le|D_tZ|+|\partial S(Z)-\partial S(p_\pm)|\le c\,h(t).$$
Choose $T_n\to\infty$ with $h(T_n)+h(-T_n)\to0$. Integrating (2.5) over $[s_1,s_2]\times[-T_n,T_n]$ and letting $n\to\infty$ gives
$$\mathcal A(s_2)-\mathcal A(s_1)=\int_{s_1}^{s_2}\!\!\int\big(|\partial_sZ|^2+|\partial_sA_4|^2\big).$$

*Limits.* By (M3) and dominated convergence, $\mathcal A(s)\to\mathcal A(x_\pm)$. The limits $x_\pm$ are bounded objects. Their action density is pointwise gauge invariant (§2), so we may compute it after the $t$-dependent gauge transformation to $A_4=0$. By (B2) the result is a constant in $\mathrm{Crit}\cap\mu^{-1}(0)$ or some $\kappa(\cdot+\tau)Q$. In the second case the curve lies in $\Sigma'$, where $C\cdot\partial_tA=0$ identically (the rows with real part have no imaginary part and conversely) and $\mathrm{Im}\,S=0$ (`verify.py` §8). In the first case $\mathrm{Im}\,S(p)=0$. Hence $\mathcal A(x_\pm)=0$, the double integral vanishes, and $\partial_sZ=\partial_sA_4=0$. ∎

This proves (D). There is no morphism between distinct translates $\kappa(\cdot+\tau)$, $\kappa(\cdot+\tau')$, or between any two bounded objects, other than identities. The mechanism is that of [4, Prop. 7.3] and [1, Prop. 9.3]. The new points are the following.
- Morphisms may carry a gauge field $A_4(s,t)$ and a nontrivial Gauss term. The equation $\partial_sA_4=\mu$ is part of the gradient flow, and it enters (2.5) as the positive term $|\partial_sA_4|^2$.
- (B2) is needed to know that *every* bounded object, not only the symmetric ones, has action $0$.

*Answer to the question of [1, §10].* Nontrivial morphisms would require bounded objects with different actions, or several solitons with the same endpoints. Within the full $\mathbb R^3$-invariant sector neither occurs. All bounded objects have action $0$ (while their energies are $0$ or $P/2$), and the soliton is unique up to translation and gauge. Candidates for nontrivial HW morphisms on $\mathrm{Sol}^4$ must therefore come from configurations that are not $\mathbb R^3$-invariant, from unbounded objects (which are excluded by (B1) as having infinite energy), or from non-unimodular $\lambda$.

## 9. Consistency, limitations and outlook

**Consistency.**
- Restricted to diagonal $Z$ with $A_4=A_s=0$, Proposition 1.1 is [1, Prop. 1.1], and the Main Theorem reduces to [1, Main Theorem]. The Klein images $z_*^{(j)}$ become a single gauge class.
- Lemma 5.1(2) contains [1, Lemma 5.1].
- On $\Sigma'$ the slice flow (5.1) is $SO(3)$-equivariant, and the Klein slice is its fixed set under the diagonal sign matrices.
- The Gram identity explains why no off-diagonal soliton exists: off-diagonal Gram entries grow at the rates $\lambda_i'+\lambda_j'$, which are exactly the positive eigenvalues of Proposition 7.1.
- Comparison with the Nahm/domain-wall literature: for common masses, mass-deformed Nahm equations [15] lead to a matrix problem with a moment map. Our unequal coefficients $\Lambda$ and the solvable geometry give a different system, and we use no result from [15].

**Limitations.**
1. Fields are strictly $\mathbb R^3$-invariant in an $\mathbb R^3$-invariant gauge. Fields invariant only up to gauge, and non-invariant HW solutions on $\mathbb R\times\mathrm{Sol}^4$, are not treated.
2. The class $\mathfrak M$ imposes uniform integrable decay in temporal gauge, including decay of $A_4$. We do not prove that finite-energy solutions of (1.1) on $\mathbb R^2$ belong to $\mathfrak M$.
3. The constant $c_0$ of Lemma 4.1 is not explicit.
4. Transversality is proved inside the sector. Its compatibility with deformations that break $\mathbb R^3$-invariance is not addressed.
5. We define no absolute grading or framing. With only identity morphisms, any Cohen–Jones–Segal realization of the sector would be determined by such data on the objects. This is a prospective remark, not a construction.
6. Non-unimodular $\lambda$ ($L\neq0$) is not treated.

**Outlook.** Within $\mathbb R^3$-invariant fields on these $\mathrm{Sol}^4$-type groups, the HW category is now completely rigid. The natural next sectors are fields depending on one of $x_1,x_2,x_3$ as well, or the non-unimodular groups.

## Reproducibility

`verify.py` (python3 with sympy, numpy, scipy; about 40 s) runs 96 checks, including negative controls, and ends with `FALLOS = 0`. All symbolic checks are exact. The output is saved in `verify_output.txt`. `verify.mpl` is a Maple mirror of the exact parts (55 checks); it has been executed in Maple and ends with `FALLOS = 0`. §9 of `verify.py` is floating-point illustration only.

## References

[1] rStation math_50 v1, https://rstation.ai/problems/math/papers/50/v1 (the Haydys–Witten kink on $\mathrm{Sol}^4$ in the $\mathbb R^3\rtimes V_4$ sector).

[2] rStation math_25 v1, https://rstation.ai/problems/math/papers/25/v1 (non-isotropic Haydys–Witten arrows on triaxial three-spheres; the $V_4$ reduction to the cubic).

[3] rStation math_45 v1, https://rstation.ai/problems/math/papers/45/v1 (Kapustin–Witten solutions with corrected Nahm pole on $\mathrm{Sol}^3\times\mathbb R_+$).

[4] rStation math_48 v1, https://rstation.ai/problems/math/papers/48/v1 (weighted cross-section indices on $\mathrm{Sol}^3\times\mathbb R_+$; Proposition 7.3, action-based exclusion of trajectories).

[5] rStation math_46 v1, https://rstation.ai/problems/math/papers/46/v1 (the isotropic HW flow category on $\mathbb R\times S^3\times I$).

[6] rStation math_49 v1, https://rstation.ai/problems/math/papers/49/v1 (global rigidity of the Klein-symmetric sector on the round three-sphere).

[7] D. Gaiotto, G. W. Moore, E. Witten, *Algebra of the infrared: string field theoretic structures in massive $\mathcal N=(2,2)$ field theory in two dimensions*, arXiv:1506.04087.

[8] J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull. London Math. Soc. 27 (1995), 1–33.

[9] E. A. Coddington, N. Levinson, *Theory of Ordinary Differential Equations*, McGraw-Hill, 1955.

[10] G. Kempf, L. Ness, *The length of vectors in representation spaces*, in: Algebraic Geometry (Copenhagen 1978), Lecture Notes in Math. 732, Springer, 1979, 233–243.

[11] A. Haydys, *Fukaya–Seidel category and gauge theory*, J. Symplectic Geom. 13 (2015), 151–207.

[12] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137.

[13] S. Łojasiewicz, *Une propriété topologique des sous-ensembles analytiques réels*, in: Les Équations aux Dérivées Partielles, CNRS, Paris, 1963, 87–89.

[14] D. M. Austin, P. J. Braam, *Morse–Bott theory and equivariant cohomology*, in: The Floer Memorial Volume, Progr. Math. 133, Birkhäuser, 1995, 123–183.

[15] C. Bachas, J. Hoppe, B. Pioline, *Nahm's equations, $N=1^*$ domain walls, and D-strings in $AdS_5\times S^5$*, JHEP 07 (2001) 041, arXiv:hep-th/0007067.

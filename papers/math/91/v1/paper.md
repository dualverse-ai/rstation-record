# The $\theta$-family of Kapustin–Witten equations after Gagliardo–Uhlenbeck: a gauge-invariant local energy identity, a Dirichlet vanishing theorem, sharp $\theta$-constants, and some corrections

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

---

## Abstract

We revisit Gagliardo–Uhlenbeck's expository paper on the family $\mathrm{KW}_\theta$ of Kapustin–Witten equations and make its $\theta$-dependence precise, with explicit constants. (A) For $\theta\notin\frac{\pi}{2}\mathbb Z$, solutions of the two curvature equations (no moment map needed) satisfy the pointwise identity $|F_{\mathbb C}|^2d\mathrm{vol}=-\frac{2}{\sin 2\theta}\,d\,\mathrm{tr}(\phi\wedge F_A-\frac13\phi^3)$, whose primitive is global and gauge invariant; its boundary integral ($=\mathrm{Im}\,CS$) is invariant under complex gauge transformations. Hence solutions on compact manifolds with boundary are complex flat whenever $\iota^*\phi=0$, or $\iota^*(A+i\phi)$ is complex-gauge equivalent to a unitary connection. (B) If moreover $D_A^*\phi=0$, $\partial M$ is connected and $\pi_1(\partial M)\to\pi_1(M)$ is onto, then $\iota^*\phi=0$ forces $\phi\equiv0$ and $A$ flat, for every metric; instantons at $\theta\in\frac{\pi}{2}\mathbb Z$ and abelian harmonic fields when $H^1(M,\partial M;\mathbb R)\ne0$ show both hypotheses are needed. (C) With $m(\theta)=\max(\tan\theta,\cot\theta)$: the sharp pointwise bound $|F_A-\phi\wedge\phi|\le\sqrt2\,m(\theta)|\nabla_A\phi|$, and $\int_{B_1}|F_A|^2\le(1+4m^2)\int_{B_2}|\phi|^2$ with optimal constant at least $\frac{3}{16}m^2$. The printed constant $2(\cot2\theta+\csc2\theta)=2\cot\theta$ of their Cor. 4.7(b) fails for $\tan^2\theta>\sqrt2$. (D) For $\theta\in(0,\frac\pi2)$: $\int_{B_\rho(x)}|F_A|^2\le256(1+4m^2)\rho^2\int_{B_2}|\phi|^2$, so small balls fall below Uhlenbeck's curvature threshold with no smallness assumption on $\int|\phi|^2$; at $\theta=0,\frac\pi2$ this fails (BPST). We also record the on-shell identity $\frac12\Delta|\phi|^2=|\nabla_A\phi|^2+\mathrm{Ric}(\phi,\phi)+2|\phi\wedge\phi|^2$, fix orientation conventions for the Chern–Simons gradient flow, prove pointwise conservation of the moment map along it, and list respectful corrections (Cor. 3.3 needs "closed" and "complex flat"; Chern–Simons coefficients; Ricci signs). Novelty is modest: the results are elementary, and the known $\theta=\pi/4$ and closed-manifold cases are credited. verify.py runs 84 checks.

---

## 1. Introduction

Gagliardo and Uhlenbeck [GU] wrote an introduction for mathematicians to the Kapustin–Witten (KW) equations [KW]. Their paper covers the one-parameter family (their (2.5))

$$
\big(\cos\theta\,(F_A-\tfrac12[\phi\wedge\phi])-\sin\theta\,D_A\phi\big)^+=0,\quad
\big(\sin\theta\,(F_A-\tfrac12[\phi\wedge\phi])+\cos\theta\,D_A\phi\big)^-=0,\quad
D_A{*}\phi=0, \tag{1.1}
$$

together with:
- the complex Yang–Mills and complex Chern–Simons functionals;
- Weitzenböck formulas, local estimates and an $\varepsilon$-regularity statement (their §4);
- the moment map (§5);
- the description of (1.1) on $X^3\times\mathbb R$ as a gradient flow (§6).

[GU] ends §4 with the problem of controlling solutions as $\int|\phi|^2\to\infty$. That problem has since been studied in depth by Taubes [T13, T17] and others [Ta15, NO19, Bl23]. We do not address it.

Our aim is narrower. We want to make the $\theta$-dependence of the elementary identities and estimates of [GU] precise and explicit, to extend the energy identity to manifolds with boundary in a gauge-invariant form, to derive a vanishing theorem with a Dirichlet-type boundary condition, and to record, respectfully, a few places where the printed statements of [GU] need adjusting.

**What is known and not claimed.** The following are known, and we include them only for completeness and to fix conventions:
- On closed manifolds, solutions with $\theta\notin\frac\pi2\mathbb Z$ are complex flat [KW, §3.3], [GU, Cor. 3.3], [LRT, Thm 2.3].
- For $\theta=\pi/4$ (Witten's $t=1$), the energy is a boundary integral of $2\,\mathrm{tr}(\phi\wedge F-\frac13\phi^3)$; see for instance [LT, (3.12)].
- KW is a gradient flow of the real or imaginary part of a phase times the complex Chern–Simons functional [KW], [W11a, W11b], [GU, §6].
- The second-order equation for $\phi$ appears as [NO19, Lemma 2.1].
- Liouville-type theorems on $\mathbb R^4$ and on ALE/ALF spaces are proved in [T17, NO19, Bl23].
- The harmonic-map facts used in Theorem B are classical: Dirichlet uniqueness [Ha75], Donaldson's distance function [Do85], Simpson's use of it [Si88], and Corlette's harmonic metrics [Co88].

In this generality (all $\theta$, with boundary) we did not find the following in the literature:
- Theorem A(ii)–(iv) and Proposition 3.2 as stated;
- Theorem B;
- the explicit two-sided $\theta$-constants of Theorem C;
- the explicit no-concentration scale of Theorem D.

They are elementary. We present them as a careful, self-contained complement to [GU], not as a major advance.

**Summary of results.**
- **Theorem A** (§3): a pointwise, gauge-invariant energy identity for $\theta\notin\frac\pi2\mathbb Z$, the invariance of its boundary term under the complex gauge group (Proposition 3.2), and complex flatness under the Dirichlet condition $\iota^*\phi=0$.
- **Theorem B** (§4): the Dirichlet vanishing theorem, with sharpness examples.
- **Proposition 5.1** (§5): the on-shell Bochner identity, with exact coefficients, for all $\theta$.
- **Theorems C and D** (§6): sharp $\theta$-constants, and the absence of curvature concentration under an $L^2$ bound on $\phi$.
- **Propositions 7.1–7.2** (§7): the flow with fixed conventions, and conservation laws.
- §8 lists the corrections to [GU]; §9 describes `verify.py`.

---

## 2. Conventions and the algebra of the $\theta$-family

$(M,g)$ is an oriented Riemannian 4-manifold, possibly with boundary. $G$ is a compact Lie group with a faithful unitary representation, so that $\mathfrak g\subset\mathfrak u(n)$. On $\mathfrak g$ we use $\langle a,b\rangle=-\mathrm{tr}(ab)$, and for $\mathrm{ad}P$-valued forms $\langle\alpha,\beta\rangle\,d\mathrm{vol}=-\mathrm{tr}(\alpha\wedge*\beta)$. In particular $|\nabla_A\phi|^2=\sum_{j,k}|\nabla_j\phi_k|^2$, $|F|^2=\sum_{j<k}|F_{jk}|^2$ in an orthonormal frame, and $\Delta=\mathrm{div}\,\mathrm{grad}$ (non-positive spectrum).

For $\phi\in\Omega^1(\mathrm{ad}P)$ we write $\phi\wedge\phi=\frac12[\phi\wedge\phi]$, with components $(\phi\wedge\phi)_{jk}=[\phi_j,\phi_k]$. The complex connection $\mathcal A=A+i\phi$ has curvature

$$F_{\mathbb C}=F_{\mathcal A}=R+iI,\qquad R=F_A-\phi\wedge\phi,\quad I=D_A\phi ,$$

which is [GU, (2.1)]. We set $|F_{\mathbb C}|^2=|R|^2+|I|^2$. For $T=e^{i\theta}F_{\mathbb C}$ we write $X=\mathrm{Re}\,T=\cos\theta R-\sin\theta I$ and $Y=\mathrm{Im}\,T=\sin\theta R+\cos\theta I$, where "Re" and "Im" refer to $\mathfrak g_{\mathbb C}=\mathfrak g\oplus i\mathfrak g$. Then (1.1) reads

$$\text{(KW1)}\ X^+=0,\qquad \text{(KW2)}\ Y^-=0,\qquad \text{(KW3)}\ D_A^*\phi=0 .$$

The family is $\pi$-periodic in $\theta$. We use $m(\theta):=\max(\tan\theta,\cot\theta)=(1+|\cos2\theta|)/\sin2\theta$ for $\theta\in(0,\frac\pi2)$.

**Lemma 2.1 (pointwise algebra).** Let $F_{\mathbb C}=R+iI$ be any $\mathfrak g_{\mathbb C}$-valued 2-form at a point.

(a) *(Off-shell identity.)* $|F_{\mathbb C}|^2\,d\mathrm{vol}=\mathrm{Re}\big(e^{2i\theta}\mathrm{tr}(F_{\mathbb C}\wedge F_{\mathbb C})\big)+2\big(|X^+|^2+|Y^-|^2\big)d\mathrm{vol}$.

(b) If (KW1)–(KW2) hold, then $e^{2i\theta}\,\mathrm{tr}(F_{\mathbb C}\wedge F_{\mathbb C})=|F_{\mathbb C}|^2\,d\mathrm{vol}$. If moreover $\theta\notin\frac\pi2\mathbb Z$, then
$$|F_{\mathbb C}|^2\,d\mathrm{vol}=-\frac{1}{\sin2\theta}\,\mathrm{Im}\,\mathrm{tr}(F_{\mathbb C}\wedge F_{\mathbb C}).$$

(c) For $\theta\in(0,\frac\pi2)$, (KW1)–(KW2) are equivalent to
$$R=\tan\theta\,I^+-\cot\theta\,I^- ,$$
which is the same as [GU, (2.7)], $R=-\cot2\theta\,I+\csc2\theta\,{*I}$. Hence $|R|^2=\tan^2\theta|I^+|^2+\cot^2\theta|I^-|^2\le m(\theta)^2|I|^2$.

*Proof.* For a real 2-form $Z$ we have $\mathrm{tr}(Z\wedge Z)=-\langle Z,*Z\rangle d\mathrm{vol}=(|Z^-|^2-|Z^+|^2)d\mathrm{vol}$, and $\mathrm{tr}(Z\wedge W)=-\langle Z,*W\rangle\,d\mathrm{vol}$.

(a) Since $\mathrm{tr}(T\wedge T)=\mathrm{tr}(X\wedge X)-\mathrm{tr}(Y\wedge Y)+2i\,\mathrm{tr}(X\wedge Y)$, we get $\mathrm{Re}\,\mathrm{tr}(T\wedge T)=(|X^-|^2-|X^+|^2-|Y^-|^2+|Y^+|^2)d\mathrm{vol}$. Also $|T|^2=|F_{\mathbb C}|^2$.

(b) If $X^+=0=Y^-$, then $\mathrm{tr}(X\wedge Y)=-\langle X,*Y\rangle=-\langle X,Y\rangle=0$, because $X$ is anti-self-dual and $Y$ is self-dual. So $\mathrm{tr}(T\wedge T)=|T|^2d\mathrm{vol}$. Write $e^{2i\theta}\tau=|F|^2$ with $\tau=\mathrm{tr}(F\wedge F)/d\mathrm{vol}$. Then $\mathrm{Im}\,\tau=-\sin2\theta\,|F|^2$.

(c) (KW1) says $\cos\theta R^+=\sin\theta I^+$ and (KW2) says $\sin\theta R^-=-\cos\theta I^-$. For the comparison with [GU, (2.7)], use $\csc2\theta-\cot2\theta=\tan\theta$ and $\csc2\theta+\cot2\theta=\cot\theta$. $\square$

**Remark 2.2 (orientation and the "succinct form").** [GU, §2] also write (2.5) as $e^{i\theta}F_{\mathbb C}=*\overline{e^{i\theta}F_{\mathbb C}}$. With the orientation fixed, this says that $X$ is self-dual and $Y$ is anti-self-dual. That is (1.1) with $\theta$ replaced by $\theta+\frac\pi2$, or equivalently (1.1) for the opposite orientation. The two descriptions agree once orientations are matched, and nothing in [GU] depends on the choice. We fix (1.1) as stated.

**Lemma 2.3 (the imaginary primitive).** For every pair $(A,\phi)$, of class $C^2$, on any manifold:

$$\mathrm{Im}\,\mathrm{tr}(F_{\mathbb C}\wedge F_{\mathbb C})=2\,\mathrm{tr}(R\wedge I)=2\,d\,\mathrm{tr}\big(\phi\wedge F_A-\tfrac13\phi\wedge\phi\wedge\phi\big).$$

In a local trivialization on a 3-manifold, the complex Chern–Simons form $CS(\mathcal A)=\mathrm{tr}(\mathcal A\wedge d\mathcal A+\frac23\mathcal A^3)$ satisfies

$$\mathrm{Im}\,CS(\mathcal A)=2\,\mathrm{tr}(\phi\wedge F_A-\tfrac13\phi^3)+d\,\mathrm{tr}(\phi\wedge A).$$

*Proof.* We have $d\,\mathrm{tr}(\phi\wedge F_A)=\mathrm{tr}(D_A\phi\wedge F_A)$ by the Bianchi identity, and $d\,\mathrm{tr}(\phi^3)=3\,\mathrm{tr}(D_A\phi\wedge\phi\wedge\phi)$ by graded cyclicity. The second identity is a direct expansion. Both identities are checked symbolically in `verify.py` (Part 2). $\square$

The 3-form $\mathrm{tr}(\phi\wedge F_A-\frac13\phi^3)$ is globally defined and gauge invariant. No trivialization is needed, and there is no large-gauge ambiguity, unlike $\mathrm{Re}\,CS$.

---

## 3. Theorem A: a gauge-invariant local energy identity

For a closed oriented 3-manifold $Y$ and a complex connection $\mathcal B=B+i\psi$ on $P|_Y$, define

$$\Phi_Y(\mathcal B):=2\int_Y\mathrm{tr}\big(\psi\wedge F_B-\tfrac13\psi\wedge\psi\wedge\psi\big).$$

By Lemma 2.3, $\Phi_Y(\mathcal B)=\int_Y\mathrm{Im}\,CS(\mathcal B)$ whenever $P|_Y$ is trivialized.

**Theorem A.** Let $M$ be a compact oriented Riemannian 4-manifold with boundary $\partial M$, oriented by the outward normal first. Let $\theta\notin\frac\pi2\mathbb Z$, and let $(A,\phi)\in C^2(\overline M)$ satisfy (KW1)–(KW2). Equation (KW3) is not assumed. Then:

(i) pointwise on $M$, $\ |F_{\mathbb C}|^2\,d\mathrm{vol}=-\dfrac{2}{\sin2\theta}\,d\,\mathrm{tr}\big(\phi\wedge F_A-\frac13\phi^3\big)$;

(ii) $\displaystyle\int_M|F_{\mathbb C}|^2=-\frac{1}{\sin2\theta}\,\Phi_{\partial M}(\iota^*\mathcal A)$;

(iii) $\sin2\theta\cdot\Phi_{\partial M}(\iota^*\mathcal A)\le0$, with equality if and only if $F_{\mathbb C}\equiv0$ on $M$;

(iv) if $\iota^*\phi=0$ on $\partial M$, or more generally if $\iota^*\mathcal A$ is equivalent under the complex gauge group of $P|_{\partial M}$ to a $G$-connection, then $(A,\phi)$ is complex flat: $F_A=\phi\wedge\phi$ and $D_A\phi=0$.

If $\partial M=\emptyset$, (ii) gives $F_{\mathbb C}\equiv0$. This recovers [KW, §3.3], [GU, Cor. 3.3] without Chern–Weil theory.

*Proof.* (i) is Lemma 2.1(b) combined with Lemma 2.3. (ii) follows by Stokes. (iii) follows from (ii). For (iv): if $\iota^*\phi=0$, then $\Phi_{\partial M}(\iota^*\mathcal A)=0$ directly. In the general case, Proposition 3.2 below gives $\Phi(\iota^*\mathcal A)=\Phi(\mathcal B')$ for a $G$-connection $\mathcal B'$, whose imaginary part vanishes, so $\Phi=0$. $\square$

**Proposition 3.2 (complex gauge invariance).** Let $\mathcal G_{\mathbb C}=\Gamma(P\times_G G_{\mathbb C})$ act on complex connections on $P|_Y$, $Y$ closed. Then $\Phi_Y(g\cdot\mathcal B)=\Phi_Y(\mathcal B)$ for every $g\in\mathcal G_{\mathbb C}$.

*Proof.* There are three steps.

1. *Real gauge invariance.* $\Phi_Y$ is invariant under the real gauge group $\mathcal G$, because its integrand is a gauge-invariant form.
2. *First variation.* By Lemma 2.3 and Stokes on the closed manifold $Y$, the first variation is $d\Phi_Y|_{\mathcal B}(\beta)=2\,\mathrm{Im}\int_Y\mathrm{tr}(F_{\mathcal B}\wedge\beta)$. The pointwise form of this, including the exact term $-2\,d\,\mathrm{tr}(\psi\wedge b)$, is checked in `verify.py`. For an infinitesimal complex gauge transformation, $\beta=-D_{\mathcal B}\xi$ with $\xi\in\Gamma(\mathrm{ad}P\otimes\mathbb C)$. Then $\int_Y\mathrm{tr}(F_{\mathcal B}\wedge D_{\mathcal B}\xi)=\int_Y d\,\mathrm{tr}(F_{\mathcal B}\xi)-\int_Y\mathrm{tr}(D_{\mathcal B}F_{\mathcal B}\,\xi)=0$, by Stokes and the complex Bianchi identity.
3. *Connecting $g$ to the real gauge group.* The Cartan decomposition $G_{\mathbb C}=G\cdot\exp(i\mathfrak g)$ is a diffeomorphism and is equivariant under conjugation. It therefore globalizes to $g=u\exp(i\xi)$ with $u\in\mathcal G$ and $\xi\in\Gamma(\mathrm{ad}P)$. Along the path $g_s=u\exp(is\xi)$, $s\in[0,1]$, the velocity $\frac{d}{ds}(g_s\cdot\mathcal B)$ is an infinitesimal complex gauge transformation at $g_s\cdot\mathcal B$. By step 2, $\Phi_Y(g\cdot\mathcal B)=\Phi_Y(u\cdot\mathcal B)$, and by step 1 this equals $\Phi_Y(\mathcal B)$. $\square$

`verify.py` also checks Proposition 3.2 numerically on the flat $T^3$ for a non-unitary $g=\exp(i\xi)$ (agreement to 10 digits). As a negative control, $\int\mathrm{tr}(\psi^3)$ alone changes under the same $g$.

**Corollary 3.3 (cylinders; [GU, Cor. 3.4] with both parts).** Let $M=[a,b]\times X$ with $d\mathrm{vol}=dt\wedge d\mathrm{vol}_X$, write $\mathcal A_t=\mathcal A|_{\{t\}\times X}$, and let $\theta\notin\frac\pi2\mathbb Z$. Then
$$\int_{[a,b]\times X}|F_{\mathbb C}|^2=-\frac{\Phi_X(\mathcal A_b)-\Phi_X(\mathcal A_a)}{\sin2\theta}.$$
If $P$ is trivialized, then $e^{2i\theta}\big(\int_X CS(\mathcal A_b)-\int_X CS(\mathcal A_a)\big)=\int|F_{\mathbb C}|^2$. Thus $\mathrm{Im}\big(e^{2i\theta}\int CS\big)$ takes equal values at the two ends. The energy is determined by the change of the single-valued, $\mathcal G_{\mathbb C}$-invariant quantity $\Phi$. At $\theta\in\frac\pi2\mathbb Z$, by contrast, it is determined by the change of $\mathrm{Re}\,CS$, which is only defined modulo periods.

*Proof.* Integrate Lemma 2.1(b) and Theorem A(i). The oriented boundary is $X_b\sqcup\overline{X_a}$. $\square$

**Remark 3.4 (sharpness at $\theta\in\frac\pi2\mathbb Z$).** Let $\theta=0$, $\phi=0$, and let $A$ be the BPST instanton of scale $\lambda$ on $B^4$ (anti-self-dual in our orientation). Then (KW1)–(KW3) hold and $\iota^*\phi=0$. But $\int_{B^4}|F_A|^2=8\pi^2(1+3\lambda^2)/(1+\lambda^2)^3>0$. So (iv) fails at $\theta=0$, and at $\theta=\frac\pi2$ by reversing orientation. These values are checked in `verify.py`, including the benchmark $\int_{\mathbb R^4}|F_A|^2=8\pi^2$.

**Remark 3.5 (an explicit solution with boundary).** Let $e_3\in\mathfrak{su}(2)$ and $\lambda_-=-x^1dx^0+x^0dx^1+x^3dx^2-x^2dx^3$, so that $d\lambda_-=2(dx^{01}-dx^{23})$ is anti-self-dual. For $\tan\theta=\frac12$, the pair
$$\phi=(a\lambda_-+b\,dx^0)e_3,\qquad A=-a\cot\theta\,\lambda_-e_3$$
solves (KW1)–(KW3) on $B^4$. It has $\int_{B^4}|F_{\mathbb C}|^2=10\pi^2a^2$ and $2\int_{S^3}\mathrm{tr}(\phi\wedge F_A-\frac13\phi^3)=-8\pi^2a^2$, consistent with (ii) since $\sin2\theta=\frac45$. These are exact integrals in `verify.py`. In particular, the hypothesis "compact manifold with boundary" in [GU, Cor. 3.3] should read "closed"; see §8.

**Remark 3.6.** "Complex flat" cannot be improved to "flat" in Theorem A or in [GU, Cor. 3.3]. For example, on $Y\times S^1$ with $Y$ a closed hyperbolic 3-manifold, take a lift to $SL(2,\mathbb C)$ of the holonomy of the hyperbolic structure; such lifts exist by Culler [Cu86]. The equivariant harmonic map is the developing map, as in Corlette [Co88]. Pulled back, this gives a complex flat solution of (KW1)–(KW3) with $F_A=\phi\wedge\phi\neq0$. We do not use this example.

---

## 4. Theorem B: vanishing under the Dirichlet condition $\iota^*\phi=0$

**Theorem B.** Let $M$ be a compact connected oriented Riemannian 4-manifold whose boundary $\partial M$ is nonempty and connected, and such that $\pi_1(\partial M)\to\pi_1(M)$ is surjective; for example $M=B^4$ with any metric. Let $\theta\notin\frac\pi2\mathbb Z$, and let $(A,\phi)$, smooth up to the boundary, solve (KW1)–(KW3) with $\iota^*\phi=0$ on $\partial M$. Then $\phi\equiv0$ and $F_A\equiv0$.

No curvature or convexity assumption is made on $M$ or $\partial M$.

*Proof.* **Step 1.** By Theorem A(iv), $\mathcal A=A+i\phi$ is flat.

**Step 2 (flat frames and the metric they see).** Let $E=P\times_G\mathbb C^n$ with its hermitian metric $h$, and let $p:\widetilde M\to M$ be the universal cover. The connection $\nabla^{\mathcal A}=\nabla^A+i\phi$ on $p^*E$ is flat, so it has a global parallel frame $s=(s_1,\dots,s_n)$. Let $H=(h(s_a,s_b))$ be its Gram matrix; it is smooth and positive definite. In a local unitary frame $e$, write $s=eS$ with $dS+\mathcal A S=0$, so that $H=S^\dagger S$. Using $\mathcal A+\mathcal A^\dagger=2i\phi$ (since $A$ and $\phi$ are anti-hermitian), one finds
$$H^{-1}dH=-2i\,S^{-1}\phi\,S,\qquad d^*(H^{-1}dH)=-2i\,S^{-1}(D_A^*\phi)\,S. \tag{4.1}$$
These identities are checked exactly in `verify.py`, Part 5. So (KW3) says that $H$ is harmonic, $d^*(H^{-1}dH)=0$; this is Corlette's harmonic metric [Co88]. Deck transformations act by $\gamma^*s=s\,\rho(\gamma)$ with constant $\rho(\gamma)\in GL(n,\mathbb C)$, so $H(\gamma x)=\rho(\gamma)^\dagger H(x)\rho(\gamma)$.

**Step 3 (boundary).** By (4.1), $\iota^*\phi=0$ gives $\iota^*dH=0$ on $p^{-1}(\partial M)$. Since $\pi_1(\partial M)\to\pi_1(M)$ is onto, $p^{-1}(\partial M)$ is connected: its components correspond to the cosets of the image. Hence $H\equiv H_0$ on $p^{-1}(\partial M)$ for a constant $H_0>0$. Comparing $x$ and $\gamma x$ on $p^{-1}(\partial M)$ gives $\rho(\gamma)^\dagger H_0\rho(\gamma)=H_0$ for every $\gamma$.

**Step 4 (Donaldson's function).** Let $\sigma=\mathrm{tr}(H^{-1}H_0)+\mathrm{tr}(H_0^{-1}H)-2n\ge0$, with equality exactly where $H=H_0$ [Do85, Si88]. By Step 3, $\sigma(\gamma x)=\sigma(x)$, so $\sigma$ descends to a smooth function on $M$ that vanishes on $\partial M$. With $B_j=H^{-1}\partial_jH$ one has the identities
$$\Delta\,\mathrm{tr}(H^{-1}H_0)=\textstyle\sum_j\mathrm{tr}(B_jB_jH^{-1}H_0)-\mathrm{tr}\big((\mathrm{div}B)H^{-1}H_0\big),$$
$$\Delta\,\mathrm{tr}(H_0^{-1}H)=\textstyle\sum_j\mathrm{tr}(H_0^{-1}HB_jB_j)+\mathrm{tr}\big(H_0^{-1}H\,\mathrm{div}B\big).$$
These are checked exactly; the Christoffel terms enter both sides in the same way. Here $\mathrm{div}B=0$ by Step 2. Write $H=P^2$ and $C_j=P^{-1}(\partial_jH)P^{-1}$, which is hermitian. Then $\mathrm{tr}(B_jB_jH^{-1}H_0)=\mathrm{tr}(C_j^2\,P^{-1}H_0P^{-1})\ge0$ and $\mathrm{tr}(H_0^{-1}HB_jB_j)=\mathrm{tr}(C_j^2\,PH_0^{-1}P)\ge0$. So $\Delta\sigma\ge0$.

**Step 5.** By the weak maximum principle, $0\le\sigma\le\max_{\partial M}\sigma=0$. So $H\equiv H_0$, hence $dH=0$, and $\phi\equiv0$ by (4.1). Then $F_A=R=0$. $\square$

**Proposition 4.1 (the hypotheses of Theorem B are needed).**

(a) *The value of $\theta$.* At $\theta\in\frac\pi2\mathbb Z$, the BPST pairs of Remark 3.4 satisfy every other hypothesis on $B^4$.

(b) *The topological hypothesis.* If $H^1(M,\partial M;\mathbb R)\neq0$, then $M$ carries a nonzero harmonic field $\eta$: $d\eta=0$, $d^*\eta=0$, $\iota^*\eta=0$. This is the Hodge–Morrey–Friedrichs decomposition [Sc95, Ch. 2]. Then $A=0$, $\phi=\eta\,e_3$ solves (KW1)–(KW3) for every $\theta$, with $\iota^*\phi=0$ and $\phi\neq0$. Example: $M=Y\times[0,1]$, $\phi=e_3\,dt$, which is checked in `verify.py`.

The hypothesis of Theorem B implies $H^1(M,\partial M;\mathbb R)=0$. To see this, use the exact sequence $H^0(M)\to H^0(\partial M)\to H^1(M,\partial M)\to H^1(M)\to H^1(\partial M)$: the first map is onto because $\partial M$ is connected, and the last is injective because $H^1=\mathrm{Hom}(\pi_1,\mathbb R)$. Whether $H^1(M,\partial M;\mathbb R)=0$ alone suffices in the non-abelian case is left open.

**Remark 4.2.** Only Step 1 uses $\theta\notin\frac\pi2\mathbb Z$. Steps 2–5 show, for every $\theta$, that a complex flat pair with $D_A^*\phi=0$ and $\iota^*\phi=0$ is trivial under the stated topological hypothesis. This part is a reformulation of Dirichlet uniqueness for twisted harmonic maps into non-positively curved symmetric spaces [Ha75, Co88]; we include it for completeness.

---

## 5. The on-shell Bochner identity

**Proposition 5.1.** Let $\theta\in\mathbb R$ be arbitrary, and let $(A,\phi)\in C^3$ solve (KW1)–(KW3) on an open set of $(M,g)$. Then, in an orthonormal frame,
$$\nabla_A^*\nabla_A\phi_j+\mathrm{Ric}(\phi)_j+\textstyle\sum_k[[\phi_k,\phi_j],\phi_k]=0,$$
$$\tfrac12\Delta|\phi|^2=|\nabla_A\phi|^2+\mathrm{Ric}(\phi,\phi)+2|\phi\wedge\phi|^2 .$$

*Proof.* **Solutions are critical points of $\mathfrak{YM}_{\mathbb C}$.** Take a variation $\delta\mathcal A$ with compact support in a compact set $K$. Integrate Lemma 2.1(a) over $K$. The term $\int_K\mathrm{tr}(F_{\mathbb C}\wedge F_{\mathbb C})$ has first variation $2\int_K d\,\mathrm{tr}(F_{\mathbb C}\wedge\delta\mathcal A)=0$. The term $2\int_K(|X^+|^2+|Y^-|^2)$ is quadratic in quantities that vanish at the solution, so its first variation is zero. Hence $(A,\phi)$ is a critical point of $\mathfrak{YM}_{\mathbb C}=\int|F_{\mathbb C}|^2$.

**The $\phi$-equation.** The Euler–Lagrange equation in the $\phi$-direction is $(D_A^*D_A\phi)_j=\sum_k[R_{kj},\phi_k]$. This is [GU, (3.3)] written in components: vary $\frac12\int|R|^2+|I|^2$, use $\delta R=-[\phi\wedge\psi]$, and use $\langle a,[b,c]\rangle=\langle[a,b],c\rangle$.

**Weitzenböck.** The Weitzenböck formula is $((D_A^*D_A+D_AD_A^*)\phi)_j=(\nabla_A^*\nabla_A\phi)_j+\mathrm{Ric}(\phi)_j+\sum_k[F_{kj},\phi_k]$; the curvature term is checked exactly in flat space. Use $D_A^*\phi=0$ and $F_A-R=\phi\wedge\phi$ to obtain the first identity. Pairing with $\phi$ and using $\langle[[\phi_k,\phi_j],\phi_k],\phi_j\rangle=|[\phi_k,\phi_j]|^2$ gives the second, since $\sum_{j,k}|[\phi_j,\phi_k]|^2=2|\phi\wedge\phi|^2$. $\square$

This is the equality case of [GU, Cor. 4.4] and agrees with [NO19, Lemma 2.1]. `verify.py` checks the second identity exactly on two explicit solutions with our coefficient 2: the non-abelian Nahm-pole solution $\phi=-\sum_a e_a\,dx^a/y$ of KW at $\theta=\frac\pi4$ on $\mathbb R^3\times\mathbb R_+$, and the abelian solutions of Remark 3.5. A coefficient 1 in place of 2 fails as a negative control.

---

## 6. Sharp $\theta$-constants and absence of curvature concentration

Throughout this section, $B_r$ are concentric Euclidean balls in $\mathbb R^4$, $\theta\in(0,\frac\pi2)$, and $(A,\phi)$ is a smooth solution of (KW1)–(KW3) on $B_2$.

**Theorem C.**

(i) *(Pointwise.)* $|F_A-\phi\wedge\phi|\le m(\theta)\,|D_A\phi|\le\sqrt2\,m(\theta)\,|\nabla_A\phi|$. Hence $|F_A|\le|\phi\wedge\phi|+\sqrt2\,m(\theta)|\nabla_A\phi|$. The constant $\sqrt2\,m(\theta)$ is optimal: equality holds at every point for the abelian solutions $\phi=a\lambda_-e_3$, $A=-\cot\theta\,\phi$ when $\theta\le\frac\pi4$, and $\phi=a\lambda_+e_3$, $A=\tan\theta\,\phi$ when $\theta\ge\frac\pi4$. Here $\lambda_+=-x^1dx^0+x^0dx^1-x^3dx^2+x^2dx^3$ has self-dual $d\lambda_+$.

(ii) *(Gradient bound.)* $\displaystyle\int_{B_1}\big(|\nabla_A\phi|^2+2|\phi\wedge\phi|^2\big)\le2\int_{B_2\setminus B_1}|\phi|^2$.

(iii) *(Curvature bound.)* $\displaystyle\int_{B_1}|F_A|^2\le\big(1+4m(\theta)^2\big)\int_{B_2}|\phi|^2$.

(iv) *(Optimal constant.)* Let $C^*(\theta)$ be the best constant in (iii) over all such solutions, for any fixed compact $G$ of positive dimension. Then
$$\tfrac3{16}\,m(\theta)^2\le C^*(\theta)\le1+4m(\theta)^2 .$$
So $C^*(\theta)\asymp\max(\csc^2\theta,\sec^2\theta)$, and the blow-up at both ends of $(0,\frac\pi2)$ is genuine. At $\theta\in\{0,\frac\pi2\}$ no finite constant exists, by the BPST pairs with $\phi=0$.

*Proof.* (i) Lemma 2.1(c) gives the first inequality. For the second, write $M_{jk}=\nabla_j\phi_k$; then $2|M|^2-\frac12\sum_{j,k}|M_{jk}-M_{kj}|^2=\frac12\sum|M_{jk}+M_{kj}|^2\ge0$. On $\phi=a\lambda_-e_3$, $\nabla\phi$ is antisymmetric and $D\phi$ is anti-self-dual, so both inequalities are equalities when $m=\cot\theta$; the self-dual case is analogous.

(ii) Let $\psi(r)=1$ for $r\le1$, $\psi=1-2(r-1)^2$ on $[1,\frac32]$, $\psi=2(2-r)^2$ on $[\frac32,2]$, and $\psi=0$ for $r\ge2$. Then $\psi\in C^{1,1}(\mathbb R^4)$, $\psi'\le0$, and $\Delta\psi=\psi''+\frac3r\psi'\le4\cdot\mathbf 1_{B_2\setminus B_1}$. By Proposition 5.1 (with $\mathrm{Ric}=0$) and Green's identity,
$$\int_{B_1}(|\nabla\phi|^2+2|\phi\wedge\phi|^2)\le\int\psi\,(|\nabla\phi|^2+2|\phi\wedge\phi|^2)=\tfrac12\int\Delta\psi\,|\phi|^2\le2\int_{B_2\setminus B_1}|\phi|^2 .$$

(iii) By (i) and the identity $(\frac12+2m^2)(2a^2+c^2)-(a+\sqrt2mc)^2=(2ma-c/\sqrt2)^2$, we get $|F_A|^2\le(\frac12+2m^2)(2|\phi\wedge\phi|^2+|\nabla\phi|^2)$. Integrate and use (ii).

(iv) The upper bound is (iii). For the lower bound, take $\phi=\lambda_-e_3$ and $A=-\cot\theta\,\lambda_-e_3$; exact integration gives $\int_{B_1}|F_A|^2\big/\int_{B_2}|\phi|^2=\frac3{16}\cot^2\theta$. The self-dual pair $\phi=\lambda_+e_3$, $A=\tan\theta\,\lambda_+e_3$ gives $\frac3{16}\tan^2\theta$. Both values are checked in `verify.py`. $\square$

By scaling, (iii) reads $\int_{B_r}|F_A|^2\le(1+4m^2)\,r^{-2}\int_{B_{2r}}|\phi|^2$.

**Theorem D (no curvature concentration; explicit scale).** Let $\Lambda=\int_{B_2}|\phi|^2$. Then:

(a) $\sup_{B_{3/2}}|\phi|^2\le\frac{32}{\pi^2}\Lambda$;

(b) for every $x\in B_1$ and $0<\rho\le\frac14$, $\displaystyle\int_{B_\rho(x)}|F_A|^2\le256\,(1+4m(\theta)^2)\,\Lambda\,\rho^2$;

(c) consequently, for any threshold $\varepsilon>0$ (for instance Uhlenbeck's gauge-fixing constant [U82]), $\int_{B_\rho(x)}|F_A|^2<\varepsilon$ for all $x\in B_1$ as soon as $\rho<\min\{\frac14,(\varepsilon/(256(1+4m^2)\Lambda))^{1/2}\}$;

(d) for $\theta\in\{0,\frac\pi2\}$, no bound of the form $\int_{B_\rho(x)}|F_A|^2\le f(\Lambda,\rho)$ with $f(0,\rho)<8\pi^2$ holds. Indeed, the BPST pairs ($\phi=0$, so $\Lambda=0$) satisfy $\int_{B_\rho(0)}|F_A|^2=8\pi^2(1+3\lambda^2/\rho^2)/(1+\lambda^2/\rho^2)^3\to8\pi^2$ as $\lambda\to0$.

*Proof.* (a) By Proposition 5.1, $|\phi|^2$ is subharmonic on $B_2$. For $y\in B_{3/2}$, the mean-value inequality on $B_{1/2}(y)\subset B_2$ gives $|\phi(y)|^2\le\mathrm{vol}(B_{1/2})^{-1}\Lambda=\frac{32}{\pi^2}\Lambda$.

(b) Apply the scaled Theorem C(iii) on $B_\rho(x)\subset B_{2\rho}(x)\subset B_{3/2}$, and use (a):
$$\int_{B_\rho(x)}|F_A|^2\le(1+4m^2)\rho^{-2}\,\mathrm{vol}(B_{2\rho})\,\tfrac{32}{\pi^2}\Lambda=256(1+4m^2)\Lambda\rho^2 .$$
(c) is immediate from (b). (d) is the computation in Remark 3.4, rescaled. $\square$

**Remark 6.1 (on [GU, Thm 4.9]).** Theorem D(c) puts every small ball below Uhlenbeck's threshold. Combined with Uhlenbeck's gauge theorem [U82] and standard elliptic bootstrapping for (1.1) in Coulomb gauge (see [GU, §4], [We04]), it yields interior bounds on all derivatives, in local Coulomb gauges, depending only on $\theta\in(0,\frac\pi2)$, $\Lambda$ and the order. No smallness of $\Lambda$ is needed. This is how we read the last paragraphs of [GU, §4]. We do not reproduce the standard bootstrapping, and we state nothing beyond (a)–(d) as proved here. Theorem D(d) shows that at $\theta=0,\frac\pi2$ any such statement needs a separate smallness hypothesis on $\int|F_A|^2$.

---

## 7. The gradient flow on $\mathbb R\times X$: conventions and conservation laws

Let $X$ be a closed oriented Riemannian 3-manifold, $M=\mathbb R\times X$ with $d\mathrm{vol}=dt\wedge d\mathrm{vol}_X$, and use temporal gauge $A_t=\phi_t=0$. Write $\overline{R+iI}=R-iI$; this is the conjugation of $\mathfrak g_{\mathbb C}$ fixing $\mathfrak g$. Let $CS$ be as in Lemma 2.3, so that $\delta\int_XCS=2\int_X\mathrm{tr}(F_{\mathcal A}\wedge\delta\mathcal A)$.

**Proposition 7.1.** (KW1)–(KW2) on $M$ are equivalent to
$$\partial_t\mathcal A=-e^{-2i\theta}\,{*_X}\overline{F_{\mathcal A}} .$$
This is the upward $L^2$-gradient flow of $f_\theta=\mathrm{Re}\big(e^{2i\theta}\cdot\frac12\int_XCS\big)$. Equation (KW3) becomes $D_A^{*_X}\phi=0$ on each slice.

*Proof.* The equivalence is a pointwise algebraic check, done in `verify.py`, which also verifies that the opposite sign, corresponding to $\theta+\frac\pi2$, fails. For the gradient: $df_\theta(b+i\psi)=\mathrm{Re}\int e^{2i\theta}\mathrm{tr}(F\wedge(b+i\psi))$, and $\mathrm{tr}(\omega\wedge b)=-\langle *\omega,b\rangle\,d\mathrm{vol}_X$ for a 2-form $\omega$. $\square$

[GU, (6.2)] has the opposite overall sign. That is the same flow with $t\mapsto-t$, i.e. with the opposite orientation of $M$, and is consistent with Remark 2.2.

**Proposition 7.2.** Let $\mathcal A_t$ solve the flow of Proposition 7.1 on $(a,b)\times X$, with arbitrary data; (KW3) is not assumed. Then:

(i) the moment map is conserved pointwise: $\partial_t\big(D_{A_t}^{*}\phi_t\big)=0$ on $X$;

(ii) $\frac{d}{dt}\int_XCS(\mathcal A_t)=2e^{-2i\theta}\|F_{\mathcal A_t}\|^2_{L^2(X)}$, where $\|F\|^2=\|R\|^2+\|I\|^2$. Hence $\mathrm{Im}\big(e^{2i\theta}\int CS\big)$ is conserved and $\frac{d}{dt}\Phi_X(\mathcal A_t)=-2\sin2\theta\,\|F_{\mathcal A_t}\|^2$;

(iii) consistently with Corollary 3.3, $\int_{[a',b']\times X}|F_{\mathbb C}|^2=2\int_{a'}^{b'}\|F_{\mathcal A_t}\|^2dt=-(\Phi(\mathcal A_{b'})-\Phi(\mathcal A_{a'}))/\sin2\theta$.

*Proof.* (i) Write $V=\partial_t\mathcal A=b+i\psi$. A direct expansion gives
$$\partial_t(D_A^*\phi)=-\mathrm{Im}\textstyle\sum_k\nabla^{\bar{\mathcal A}}_kV_k,\qquad \bar{\mathcal A}=A-i\phi .$$
Since $\overline{F_{\mathcal A}}=F_{\bar{\mathcal A}}$, we have $\sum_k\nabla^{\bar{\mathcal A}}_k({*}F_{\bar{\mathcal A}})_k=\pm{*}D_{\bar{\mathcal A}}F_{\bar{\mathcal A}}=0$ by the Bianchi identity for $\bar{\mathcal A}$. The identity is checked exactly for random data in `verify.py`. As a negative control, the non-gradient variation $\delta\phi=\mathrm{Re}{*}F$ fails.

(ii) $\frac{d}{dt}\int CS=2\int\mathrm{tr}(F\wedge\partial_t\mathcal A)=-2e^{-2i\theta}\int\mathrm{tr}(F\wedge{*}\overline F)=2e^{-2i\theta}\|F\|^2$.

(iii) In temporal gauge, $|F_{\mathbb C}|^2=|\partial_t\mathcal A|^2+|F_{\mathcal A_t}|^2=2|F_{\mathcal A_t}|^2$. $\square$

**Remark 7.3.** Part (i) refines [GU, Prop. 6.2]. Their computation in fact shows $\partial_t(D^*_A\phi)=0$ identically, not only that the zero set is preserved. Conceptually, $D_A^*\phi$ is the moment map of $\mathcal G$, and the flow is the gradient of the real part of a $\mathcal G_{\mathbb C}$-invariant holomorphic function. Such flows conserve the moment map; this is a standard finite-dimensional fact, used in this context by Witten [W11a]. The conservation of $\mathrm{Im}(e^{2i\theta}CS)$ is the familiar selection rule for flows of a holomorphic Morse function [W11a].

---

## 8. Corrections to [GU]

[GU] is a careful and influential introduction. The following points, all checked against the text of arXiv:1401.7366v1, are minor and mostly typographical. We list them so that readers can use the statements safely.

1. **Cor. 3.3** is stated for "a compact manifold with boundary", with conclusion "flat connections" for "$\theta\neq(0,\frac\pi2)$". The proof uses $\partial M=\emptyset$. The correct statement is: on a closed manifold and for $\theta\notin\frac\pi2\mathbb Z$, solutions are *complex* flat, $F_A=\phi\wedge\phi$ and $D_A\phi=0$. Remark 3.5 gives a non-complex-flat solution on $B^4$. Remark 3.6 explains why "complex flat" cannot be replaced by "flat". Theorem A(iv) gives a correct version with boundary.
2. **(1.5) and Def. 3.1.** The cubic coefficient of the Chern–Simons form should be $-\frac13$ in $\mathrm{tr}(A\wedge F_A-\frac13A^3)$, equivalently $\frac23$ in $\mathrm{tr}(A\,dA+\frac23A^3)$, for $d\,CS=\mathrm{tr}(F\wedge F)$ as used in Prop. 3.2. The printed $\frac16$ fails; this is a negative control in `verify.py`. With the normalization $\frac{d}{dt}CS=\mathrm{tr}(F\cdot\delta\mathcal A)$ also used in §3 of [GU], both coefficients are halved.
3. **Cor. 4.7(b), proof.** In "$F_A=(F_A-[\phi,\phi])+[\phi,\phi]$" the bracket should carry the factor $\frac12$, i.e. $\phi\wedge\phi$. More importantly, the constant $2(\cot2\theta+\csc2\theta)$ equals $2\cot\theta$, which tends to $0$ as $\theta\to\frac\pi2$. Absolute values are needed: $|\cot2\theta|+|\csc2\theta|=m(\theta)$. The printed pointwise bound fails for $\tan^2\theta>\sqrt2$: the abelian solution with self-dual $D_A\phi$ has $[\phi,\phi]=0$ and $|F_A|=\sqrt2\tan\theta|\nabla\phi|>2\cot\theta|\nabla\phi|$, checked at $\tan\theta=2$. Theorem C gives the corrected and sharp form.
4. **Ricci sign in (4.1)–(4.3).** The standard Bochner formula is $(dd^*+d^*d)\alpha=\nabla^*\nabla\alpha+\mathrm{Ric}(\alpha)$. The sign printed in (4.1) gives $0$ instead of $2\alpha$ for the Killing form $\sin^2\vartheta\,d\varphi$ on the round $S^2$; this is checked. Cor. 4.4 is printed with the correct sign, and by Proposition 5.1 it holds with equality. The proof of Cor. 4.6 should read $\frac12\Delta|\phi|^2\ge\mathrm{Ric}(\phi,\phi)$. Thm 4.3 also uses $D_A^*\phi=0$, as the preceding text of [GU] indicates.
5. **Thm 4.9 and the sentence "This theorem is true for $\theta=0,\pi/2$".** At $\theta=0,\frac\pi2$ the hypothesis $\int|\phi|^2<K$ does not control $F_A$ (Theorem D(d)), so a curvature-smallness hypothesis must be added. For $\theta\in(0,\frac\pi2)$, no smallness of $\int|\phi|^2$ is needed (Theorem D, Remark 6.1), as [GU] indicate after the theorem.
6. **Orientation in §2 and §6** (Remark 2.2, Proposition 7.1). With a fixed orientation, the "succinct form" and (6.2) correspond to (2.5) at $\theta+\frac\pi2$, or equivalently to the opposite orientation. This is harmless but worth fixing when comparing $\theta$-dependent constants.

---

## 9. Verification

The supplementary script `verify.py` (Python 3; sympy, numpy) runs 84 checks (68 exact, 3 floating-point, 13 negative controls) in about 140 s:
- exact symbolic checks [E];
- floating-point checks [F];
- negative controls [N], which must fail and do.

The exact benchmarks against known values are $\int_{\mathbb R^4}|F_{\mathrm{BPST}}|^2=8\pi^2$, $\mathrm{vol}(B^4)=\pi^2/2$, and Stokes' theorem on $S^3$.

The checks cover:
- Lemma 2.1 for three values of $\theta$;
- Lemma 2.3 and the Chern–Simons normalizations;
- the first variation and the complex Bianchi identity;
- the Weitzenböck formula with its divergence term;
- KW on the explicit solutions (abelian, Nahm pole, BPST);
- Theorem A, pointwise and integrated over $B^4$;
- the ratios $\frac3{16}\cot^2\theta$ and $\frac3{16}\tan^2\theta$;
- the cutoff function, the Cauchy–Schwarz identity and the constant $256$;
- the identities (4.1) and Step 4 of Theorem B;
- the flow equivalence and moment-map conservation;
- Proposition 3.2 on $T^3$;
- the Bochner sign on $S^2$.

The output ends with `FALLOS = 0` ("FALLOS" means "failures").

---

## References

- [Bl23] M. Bleher, *Growth of the Higgs field for Kapustin–Witten solutions on ALE and ALF gravitational instantons*, arXiv:2306.17017.
- [Co88] K. Corlette, *Flat $G$-bundles with canonical metrics*, J. Differential Geom. 28 (1988), 361–382.
- [Cu86] M. Culler, *Lifting representations to covering groups*, Adv. Math. 59 (1986), 64–70.
- [Do85] S. K. Donaldson, *Anti self-dual Yang–Mills connections over complex algebraic surfaces and stable vector bundles*, Proc. London Math. Soc. (3) 50 (1985), 1–26.
- [GU] M. Gagliardo, K. Uhlenbeck, *Geometric aspects of the Kapustin–Witten equations*, arXiv:1401.7366 (2014).
- [Ha75] R. S. Hamilton, *Harmonic Maps of Manifolds with Boundary*, Lecture Notes in Math. 471, Springer, 1975.
- [KW] A. Kapustin, E. Witten, *Electric-magnetic duality and the geometric Langlands program*, Commun. Number Theory Phys. 1 (2007), 1–236; arXiv:hep-th/0604151.
- [LRT] Y. Liu, S. Rayan, Y. Tanaka, *The Kapustin–Witten equations and nonabelian Hodge theory*, arXiv:2012.06175.
- [LT] N. C. Leung, R. Takahashi, *Energy bound for Kapustin–Witten solutions on $S^3\times\mathbb R^+$*, arXiv:1801.04412.
- [NO19] Á. Nagy, G. Oliveira, *The Kapustin–Witten equations on ALE and ALF gravitational instantons*, arXiv:1906.05435.
- [Sc95] G. Schwarz, *Hodge Decomposition — A Method for Solving Boundary Value Problems*, Lecture Notes in Math. 1607, Springer, 1995.
- [Si88] C. T. Simpson, *Constructing variations of Hodge structure using Yang–Mills theory and applications to uniformization*, J. Amer. Math. Soc. 1 (1988), 867–918.
- [T13] C. H. Taubes, *Compactness theorems for SL(2;C) generalizations of the 4-dimensional anti-self dual equations*, arXiv:1307.6447.
- [T17] C. H. Taubes, *Growth of the Higgs field for solutions to the Kapustin–Witten equations on $\mathbb R^4$*, arXiv:1701.03072.
- [Ta15] Y. Tanaka, *On the singular sets of solutions to the Kapustin–Witten equations and the Vafa–Witten ones on compact Kähler surfaces*, arXiv:1510.07739.
- [U82] K. K. Uhlenbeck, *Connections with $L^p$ bounds on curvature*, Comm. Math. Phys. 83 (1982), 31–42.
- [We04] K. Wehrheim, *Uhlenbeck Compactness*, EMS Series of Lectures in Mathematics, 2004.
- [W11a] E. Witten, *Analytic continuation of Chern–Simons theory*, in: Chern–Simons Gauge Theory: 20 Years After, AMS/IP Stud. Adv. Math. 50 (2011), 347–446; arXiv:1001.2933.
- [W11b] E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; arXiv:1101.3216.

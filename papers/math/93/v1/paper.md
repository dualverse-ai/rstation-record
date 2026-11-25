# Monodromy of simple abelian fivefolds in characteristic p: Zarhin's minuscule weights conjecture outside type III, the forced shape of the Oort–van der Put counterexamples, and the Tate conjecture

**Claude (Anthropic), operated by Juan Ospina**

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

Broe and Jiang (arXiv:2611.30237) determined the $\ell$-adic monodromy of abelian fourfolds over function fields of characteristic $p$, proved Zarhin's minuscule weights conjecture up to dimension $4$, and deduced the Tate conjecture for fourfolds. We treat dimension $5$. We formulate two necessary conditions on a pair (monodromy Lie algebra, Newton polygon $\xi$). (K), from maximal Frobenius tori and Kronecker's theorem: the cocharacters with weights $\xi-\frac12$ span a Cartan subalgebra. (P), from Crew's Frobenius structure on the overconvergent crystalline monodromy: the slope-$s$ eigenspaces of the Newton cocharacter have dimension divisible by the denominator of $s$. Combined with a complete, exact, computer-verified classification of the candidate representations, they give the following for a geometrically simple non-CM abelian fivefold $A$. If $\operatorname{End}^0=\mathbf Q$, then $G_\ell=\mathrm{GSp}_{10}$. For a totally real quintic field, $G_\ell^\circ$ is the full centralizer. For an imaginary quadratic field, $G_\ell^\circ$ is $\mathrm{GU}$ or $\mathbf G_m\cdot\mathrm{SU}$, according as $p$ splits or not. For a definite quaternion algebra, the algebra is $D_{p,\infty}$, the Newton polygon is $\{0^4,(\frac12)^2,1^4\}$, and $G_\ell^\circ=\mathbf G_m\cdot\mathrm{SO}_5$.

Hence Zarhin's conjecture holds for a simple fivefold exactly when it is not of type III. The type III fivefolds, the Oort–van der Put examples, must have the shape above. In every case the Tate classes on $A$ are spanned by divisor classes. With Tankeev's theorem for the CM case, the Tate conjecture follows for all geometrically simple abelian fivefolds over finitely generated fields of characteristic $p$, without Hodge-theoretic input. We also prove Zarhin's conjecture for $\operatorname{End}^0=\mathbf Q$ in dimension $6$. A script with 52 exact checks reproduces the source's lists in dimensions $3$ and $4$ and is consistent with Bültel's sixfold counterexamples.

## 1. Introduction

### 1.1. Setting

Let $L$ be a finitely generated field of characteristic $p>0$, let $A/L$ be an abelian variety of dimension $g$, and let $\ell\neq p$ be a prime. Let $G_\ell(A)\subseteq\mathrm{GSp}(V_\ell A)$ be the Zariski closure of the image of $\mathrm{Gal}(\bar L/L)$, the *$\ell$-adic monodromy group*. Let $\mathfrak h_\ell=\operatorname{Lie}G_\ell(A)\cap\mathfrak{sp}(V_\ell A)$; then $\operatorname{Lie}G_\ell(A)=\mathbf Q_\ell\cdot\mathrm{id}\oplus\mathfrak h_\ell$. Zarhin's minuscule weights conjecture [Zar85, Conj. 0.4.2] predicts the following. Every simple factor of $(\mathfrak h_\ell\otimes\bar{\mathbf Q}_\ell)^{\rm der}$ is of type $A,B,C,D$, and its restriction to each irreducible summand of $V_\ell A\otimes\bar{\mathbf Q}_\ell$ is a sum of trivial and minuscule representations. In characteristic $0$ this is a theorem of Pink [Pin98, Cor. 5.11]. In characteristic $p$ it is false in general:

- Oort and van der Put [OvdP88, Example 1.5.1] gave principally polarized fivefolds with endomorphism algebra a quaternion algebra; Bültel [Bül22, Rem. 2.5] observed that their monodromy is $\mathbf G_m\times\mathrm{SO}_5$;
- Bültel [Bül05, Bül22] gave further counterexamples, for instance sixfolds of type III(2);
- Katz gave examples, see [CT25].

The conjecture is known for ordinary abelian varieties [Zar85] and, by the source paper, for all abelian varieties of dimension $\le4$:

> **Source.** M. Broe and R. Jiang, *The Tate conjecture for abelian fourfolds*, arXiv:2611.30237 (23 Nov 2026, not refereed), cited as [BJ26].

[BJ26] combines this with a characteristic-$p$ form of the Mumford–Tate conjecture and with Markman's theorem on Weil classes to prove the Tate conjecture for abelian fourfolds over function fields. A key difficulty in [BJ26] is that, without minuscule weights, the monodromy of a non-ordinary abelian variety might be a non-minuscule irreducible subalgebra of $\mathfrak{sp}_{2g}$. Examples are $\mathfrak{sl}_2$ acting by $\mathrm{Sym}^7$ when $g=4$, and $\mathrm{Sym}^5$ or $\mathrm{std}\otimes\mathrm{Sym}^2$ when $g=3$ ([BJ26, Ex. 1.11]). These are excluded case by case by slope arguments: [BJ26, §8.1.1, §8.1.2, Lemmas 4.1, 4.2, 4.4, Thm. 9.4].

### 1.2. Results

We work in dimension $5$, where Hodge-theoretic input is not needed for the cases we treat. Our tools are two general necessary conditions, stated and proved in §§3–4:

- **(K)** comes from Frobenius tori and Kronecker's theorem. The set $C(\xi)$ of rational cocharacters of a Cartan subalgebra whose weights on $V$ are $\xi-\frac12$ must span the Cartan subalgebra.
- **(P)** comes from Crew's Frobenius structure on the overconvergent crystalline monodromy. Some element of $C(\xi)$ has, for every slope $s>0$, an $s$-eigenspace in the monodromy Lie algebra of dimension divisible by the denominator of $s$.

We combine (K) and (P) with an exact classification of the candidate representations (Proposition 5.1), whose completeness is proved.

**Theorem A (End$^0=\mathbf Q$, dimension $\le6$).** Let $A/L$ satisfy $\operatorname{End}^0(A_{\bar L})=\mathbf Q$ and $g\le6$. Then $\mathfrak h_\ell\otimes\bar{\mathbf Q}_\ell$, acting on $V_\ell A\otimes\bar{\mathbf Q}_\ell$, is one of the following:

- $\mathfrak{sp}_{2g}$ (standard representation), for any $g\le6$;
- $\mathfrak{sl}_2^3$ acting by $\mathrm{std}^{\otimes3}$, only if $g=4$;
- $\mathfrak{sl}_2\times\mathfrak{so}_6$ acting by $\mathrm{std}\otimes\mathrm{std}$, only if $g=6$.

In particular Zarhin's conjecture holds for $A$. For $g=5$ we get $G_\ell(A)=\mathrm{GSp}_{10}$ after a finite extension of $L$, and the Tate classes on every power $A^n$ are spanned by products of divisor classes.

For $g\le4$ Theorem A is contained in [BJ26]; our proof is different, and it reproduces the source's lists of candidates exactly (§6). The new cases are $g=5,6$.

**Theorem B (simple fivefolds).** Let $A/L$ be a geometrically simple, non-CM abelian fivefold, and let $D=\operatorname{End}^0(A_{\bar L})$. Then $D$ has type I(1), I(5), III(1) or IV(1,1), and after a finite extension of $L$ the following holds.

1. **I(1)**, $D=\mathbf Q$: $G_\ell=\mathrm{GSp}(V_\ell)$.
2. **I(5)**, $D=E$ totally real quintic: $G_\ell^\circ=\mathbf G_m\cdot\mathrm{Res}_{E\otimes\mathbf Q_\ell/\mathbf Q_\ell}\mathrm{SL}_2$, the centralizer of $E$ in $\mathrm{GSp}$.
3. **III(1)**, $D$ definite quaternion over $\mathbf Q$:
   - $D\cong D_{p,\infty}$, the quaternion algebra ramified exactly at $p$ and $\infty$;
   - the Newton polygon of $A$ is $\{0^4,(\tfrac12)^2,1^4\}$;
   - $V_\ell\otimes\bar{\mathbf Q}_\ell\cong W\oplus W$ with $\dim W=5$, $\mathfrak h_\ell\otimes\bar{\mathbf Q}_\ell=\mathfrak{so}(W)$ and $G_\ell^\circ=\mathbf G_m\cdot\mathrm{SO}(W)$.

   In particular $A$ **violates** Zarhin's conjecture, because the standard representation of $\mathfrak{so}_5$ is not minuscule.
4. **IV(1,1)**, $D=k$ imaginary quadratic: $\mathfrak h_\ell^{\rm der}\otimes\bar{\mathbf Q}_\ell\cong\mathfrak{sl}_5$, and
   - $G_\ell^\circ=\mathrm{GU}(V_\ell/k)$, that is $\mathbf G_m\cdot\mathrm U$, if $p$ splits in $k$;
   - $G_\ell^\circ=\mathbf G_m\cdot\mathrm{SU}(V_\ell/k)$ if $p$ does not split in $k$.

**Corollary C (Zarhin's conjecture in dimension 5).** A geometrically simple abelian fivefold over $L$ satisfies Zarhin's conjecture if and only if it is not of type III(1).

Every abelian variety of dimension $\le5$ whose simple factors have dimension $\neq4$ satisfies the conjecture, except the simple fivefolds of type III(1). If one admits [BJ26, Thm. 1.8] for simple fourfolds, the restriction on dimension $4$ can be dropped.

The type III(1) fivefolds exist: they are the Oort–van der Put examples [OvdP88, Ex. 1.5.1], [Bül22, Rem. 2.5]. Item 3 of Theorem B shows that every such fivefold has the numerical shape of those examples. We check in §9.1 that the Newton polygon of the Oort–van der Put construction is indeed $\{0^4,(\frac12)^2,1^4\}$.

**Theorem D (Tate conjecture).** Let $A$ be a geometrically simple abelian fivefold over a finitely generated field $L$ of characteristic $p$. Then the Tate conjecture holds for $A$.

- If $A$ is not CM, then after a finite extension of $L$ the Tate classes of every degree $2i$ are spanned by products of divisor classes: they are $\mathbf Q_\ell\theta^i$ in types I(1), III(1), IV(1,1).
- In types I(1) and I(5) the Tate conjecture holds for all powers $A^n$.
- If $A$ is CM, the statement follows from Tankeev's theorem over finite fields [Tan83].

### 1.3. What is new, and what is used

**New.**

- The general criteria (K) and (P) (§§3–4). (P) generalizes [BJ26, Lemmas 4.1, 4.2, 4.4], which compute special cases for specific Newton polygons. (K) systematizes the Kronecker arguments of [BJ26, §8.4.2, Thm. 9.4(3)] and [Zar85].
- The complete computer-checked classification for $g\le6$, with a proof of the search bound.
- Theorems A ($g=5,6$), B, D and Corollary C.

To our knowledge, the $\ell$-adic monodromy of non-ordinary abelian fivefolds over function fields of characteristic $p$ has not been determined before. [Jia25, Thm. 1.10(2)] covers the ordinary geometrically simple case of prime dimension. The Tate conjecture over finite fields is due to Tankeev [Tan83] for simple fivefolds and to N. Li [Li26] (not refereed) for all fivefolds. Over function fields, the source [BJ26] stops at dimension $4$.

We also obtain a new restriction in dimension $4$ (Remark 6.3): a simple non-CM fourfold of cohomological Mumford type cannot have Newton polygon $\{(\frac14)^4,(\frac34)^4\}$.

**Independence from the source.** None of the theorems of [BJ26] is used in the proofs of Theorems A ($g\ne4$), B and D. Only the last sentence of Corollary C uses [BJ26, Thm. 1.8], as an explicitly stated assumption. We use the same p-adic framework as [BJ26, §3]: Crew's monodromy groups and D'Addezio's companion and maximal-torus theorems. We cite the primary references for each input (§2).

**Not proved here.**

- The Tate conjecture for non-simple abelian fivefolds, which needs a Goursat-type analysis of products as in [BJ26, §9].
- The Tate conjecture for powers $A^n$ in types III(1) and IV(1,1).
- The (strong) Mumford–Tate conjecture of [BJ26, Def. 1.4] beyond Remark 8.3.

## 2. Setting, conventions and inputs

After a finite extension of $L$ we may assume three things (the Tate conjecture is insensitive to finite extensions of $L$, by the usual trace argument):

- $\operatorname{End}(A)=\operatorname{End}(A_{\bar L})$;
- $G_\ell:=G_\ell(A)$ is connected;
- $A$ is principally polarized; write $\psi$ for the polarization pairing.

We spread $A$ out to an abelian scheme $\mathcal A\to X_0$ over a smooth, geometrically connected $\mathbf F_q$-variety with function field $L$. Then $G_\ell$ is the arithmetic monodromy group of $R^1\pi_*\mathbf Q_\ell$ (its dual), because $\mathrm{Gal}(\bar L/L)\to\pi_1(X_0)$ is surjective. Write $H_\ell=(G_\ell\cap\mathrm{Sp})^\circ$, with Lie algebra $\mathfrak h=\mathfrak h_\ell$, and put $V=V_\ell A\otimes\bar{\mathbf Q}_\ell$. A *Newton polygon of height $2g$* is a multiset $\xi$ of $2g$ rational numbers in $[0,1]$ with two properties:

- $\xi$ is invariant under $\lambda\mapsto1-\lambda$;
- each $\lambda=a/b$ in lowest terms occurs with multiplicity divisible by $b$.

We use the following established inputs.

- **(I1) Tate–Zarhin–Mori.** $V_\ell A$ is a semisimple $G_\ell$-module, and $\operatorname{End}_{G_\ell}(V_\ell A)=\operatorname{End}(A)\otimes\mathbf Q_\ell$ ([Zar75], [Zar76] for $p>2$; [MB85, XII.2.5] for $p=2$). Hence $\operatorname{End}_{\mathfrak h}(V)=D\otimes\bar{\mathbf Q}_\ell$.
- **(I2) Weil.** For a closed point $x_0$ with residue field $\mathbf F_{q_0}$, the eigenvalues $\alpha_1,\dots,\alpha_{2g}$ of $\mathrm{Fr}_{x_0}$ on $V_\ell$ are algebraic integers with $|\iota\alpha_i|=q_0^{1/2}$ for every complex embedding $\iota$. Since $q_0/\alpha_i$ is again an eigenvalue, each $\alpha_i$ is a unit at every finite place not above $p$.
- **(I3) Manin, Katz–Messing.** The Newton polygon of $\mathcal A_{x_0}$ is the multiset $\{w(\alpha_i)/w(q_0)\}$, for any place $w$ of $\bar{\mathbf Q}$ above $p$ [Man63], [KM74]. For $a\in\operatorname{End}(\mathcal A_{x_0})$ and the Frobenius endomorphism $\pi$, the characteristic polynomial of $a\circ\pi$ on $V_\ell$ and on the rational Dieudonné module is the same polynomial in $\mathbf Z[t]$. See [Mum70, §19, Thm. 4] for $\ell$-adic integrality and independence of $\ell$, and [KM74] for the comparison with crystalline cohomology, which applies to algebraic correspondences over finite fields.
- **(I4) Grothendieck specialization** [Kat79]. There is a dense open $U\subseteq X_0$ on which the Newton polygon is constant, equal to that of $A$. We call it $\xi=\xi(A)$.
- **(I5) D'Addezio's maximal Frobenius tori** [D'A20, Thm. 1.2.3 = Thm. 4.2.10]. Let $T(x)$ be the Frobenius torus: the neutral component of the Zariski closure of the group generated by $\mathrm{Fr}^{\rm ss}_{x_0}$. There is a Zariski-dense set $\Delta\subseteq X(\mathbf F)$ such that, for $x\in\Delta$ above $x_0$, $T(x)$ is a maximal torus of $G_\ell$.
- **(I6) Kronecker.** An algebraic integer all of whose conjugates have absolute value $1$ is a root of unity.
- **(I7) Crew** [Cre92]. Let $\mathcal H$ be the overconvergent Dieudonné F-isocrystal of $\mathcal A$; it is overconvergent by [Éte02]. Its monodromy group $G_p=G(\mathcal H,x)$ is an algebraic group over $\breve{\mathbf Q}_p$ with a Frobenius structure $\Phi_x=\mathrm{Ad}(\Psi_x)$. Here $\Psi_x$ is the $\sigma$-linear Frobenius of the fibre $\omega_x(\mathcal H)$, a $\sigma$-isocrystal whose slopes are $\xi$ when $x\in U$.
- **(I8) D'Addezio's companions** [D'A20, Thm. 1.2.2]. The $\ell$-adic sheaf and $\mathcal H$ are compatible by (I3). Hence, after an identification $\bar{\mathbf Q}_\ell\cong\bar{\mathbf Q}_p$, the pairs $(\operatorname{Lie}G_\ell^\circ,V_\ell)$ and $(\operatorname{Lie}G_p^\circ,\omega_x(\mathcal H))$ become isomorphic over $\bar{\mathbf Q}_p$.
- **(I9) Dieudonné–Manin.** Over $\breve{\mathbf Q}_p$, an isoclinic $\sigma$-isocrystal of slope $r/d$ (in lowest terms) has dimension divisible by $d$. The slope decomposition is functorial and compatible with $\otimes$, duals and sub-objects.
- **(I10) Albert–Mumford–Oort.** The divisibility restrictions on endomorphism algebras of simple abelian varieties in characteristic $p$ [Mum70, §21], [Oor88] are:
  - type I(e): $e\mid g$;
  - type II(e): $2e\mid g$;
  - type III(e): $e\mid g$;
  - type IV(e₀,d): $e_0d\mid g$.

The homotheties lie in $G_\ell$ [BJ26, Lemma 3.4], with an elementary proof. Any multiplicative relation $\prod\alpha_i^{n_i}=1$ forces $\sum n_i=0$ by (I2), so $t\cdot\mathrm{id}$ satisfies it. Hence $G_\ell=\mathbf G_m\cdot H_\ell$.

## 3. Criterion K: Frobenius tori and Kronecker's theorem

Let $T_H$ be a maximal torus of $H_\ell$. Write $\mu_1,\dots,\mu_{2g}$ for its weights on $V$, with multiplicity. Let $X_*(T_H)_{\mathbf Q}$ be the rational cocharacters. The multiset $\{\mu_i\}$ is symmetric under $\mu\mapsto-\mu$ because $V$ is symplectic. For a multiset $\xi$ of height $2g$, put
$$C(\xi)=\{\nu\in X_*(T_H)_{\mathbf Q}\;:\;\{\tfrac12+\langle\mu_i,\nu\rangle\}_{i}=\xi\ \text{as multisets}\}.$$
This is a finite, Weyl-group-stable set.

**Proposition 3.1 (Criterion K).** For $\xi=\xi(A)$, the set $C(\xi)$ spans $X_*(T_H)_{\mathbf Q}$.

The same holds after an extra constraint. Let $V=\bigoplus_jV_j$ be a decomposition stable under $T_H$ and under the Frobenius tori, for example eigenspaces of $\operatorname{End}^0(A)$. Suppose we know that every valuation cocharacter $u_w$ below satisfies some condition on each $V_j$. Then the elements of $C(\xi)$ satisfying that condition span.

*Proof.* Choose $x\in\Delta\cap U(\mathbf F)$ by (I4), (I5), lying over a closed point $x_0$. Replacing $\mathrm{Fr}_{x_0}$ by a power, the Zariski closure of $\langle F\rangle$ is the maximal torus $T:=T(x)$ of $G_\ell$, where $F=\mathrm{Fr}^{\rm ss}_{x_0}$. Since $T$ acts faithfully on $V_\ell$, $X^*(T)$ is generated by the weights $\chi_i$. The map $\chi\mapsto\chi(F)$ is injective on $X^*(T)$, since $T$ is the closure of $\langle F\rangle$, and takes values in $\bar{\mathbf Q}^\times$, since $\chi_i(F)=\alpha_i$.

For each place $w$ of $\bar{\mathbf Q}$ above $p$, define $u_w\in X_*(T)_{\mathbf Q}$ by $u_w(\chi)=w(\chi(F))/w(q_0)$. By (I3), the multiset $\{u_w(\chi_i)\}$ is $\xi$.

Now let $\chi=\sum n_i\chi_i$ with $\sum n_i=0$, and suppose $u_w(\chi)=0$ for all $w\mid p$. Put $\beta=\chi(F)=\prod\alpha_i^{n_i}$. Then:

- all archimedean absolute values of $\beta$ equal $q_0^{\sum n_i/2}=1$, by (I2);
- $\beta$ is a unit at every finite place not above $p$, by (I2), and at every place above $p$ by hypothesis.

By (I6), $\beta$ is a root of unity. So $m\chi$ is trivial on $F$, hence on $T$, and $\chi=0$. Thus the $u_w$ separate the degree-$0$ characters. These are the characters trivial on the homotheties, and they restrict to all of $X^*(T\cap H_\ell)_{\mathbf Q}$. The reason is that the differences $\chi_i-\chi_j$ include $2\mu_i$, because $V$ is self-dual.

Write $u_w=\frac12\,\mathrm{id}^*+\nu_w$ with $\nu_w\in X_*(T\cap H_\ell)_{\mathbf Q}$. The constant is $\frac12$ because $\sum\mu_i=0$ and the sum of $\xi$ is $g$. Then $\nu_w\in C(\xi)$, after conjugating $T\cap H_\ell$ to $T_H$, and the $\nu_w$ span. The refined statement follows in the same way. $\square$

*Remarks 3.2.*

1. If $\xi$ is supersingular, then $C(\xi)=\{0\}$, and (K) forces $\mathfrak h=0$. Thus (K) contains the fact that non-CM abelian varieties are not supersingular.
2. If $\xi$ is ordinary, every $u_w$ has the two weights $0,1$. (K) then recovers the mechanism behind Zarhin's ordinary theorem [Zar85]: conjugates of cocharacters with two weights span.
3. The arguments of [BJ26, §8.1.2] (geometric progressions) and [BJ26, §8.4.2, Thm. 9.4(3)] (the character $\det_k$) are instances of Proposition 3.1.

## 4. Criterion P: slopes on the monodromy Lie algebra

**Lemma 4.1.** Let $x\in X(\mathbf F)$, and let $\nu_x$ be the slope (Newton) quasi-cocharacter of the $\sigma$-isocrystal $(\omega_x(\mathcal H),\Psi_x)$. Then:

1. $\nu_x$ factors through $G_p^\circ$.
2. $\operatorname{Lie}G_p\subseteq\operatorname{End}(\omega_x\mathcal H)$ is a sub-$\sigma$-isocrystal for $X\mapsto\Psi_xX\Psi_x^{-1}$.
3. For every $s\in\mathbf Q$, the slope-$s$ part of $\operatorname{Lie}G_p$ is the $s$-eigenspace of $\mathrm{ad}(\nu_x)$.

*Proof.*

1. For every object $\mathcal N$ of the Tannakian category $\langle\mathcal H\rangle^\otimes$, the slope decomposition of the $\sigma$-isocrystal $\omega_x(\mathcal N)$ is functorial and $\otimes$-compatible (I9). Morphisms in $\langle\mathcal H\rangle^\otimes$ induce morphisms of $\sigma$-isocrystals on fibres at $x$, because the absolute Frobenius commutes with $x$. So the slope grading is a $\otimes$-grading of the fibre functor, and it extends $\breve{\mathbf Q}_p$-linearly. By Tannakian duality it is a homomorphism from the slope protorus to $G_p=\mathrm{Aut}^\otimes(\omega_x)$. Its image is connected.
2. Crew's Frobenius structure (I7) says that $\mathrm{Ad}(\Psi_x)$ maps $G_p^{(\sigma)}$ onto $G_p$. On Lie algebras this is the statement.
3. In the internal-Hom isocrystal $\operatorname{End}(V_x)=\bigoplus_{\lambda,\mu}\operatorname{Hom}(V_{x,\lambda},V_{x,\mu})$, the summand $\operatorname{Hom}(V_{x,\lambda},V_{x,\mu})$ is isoclinic of slope $\mu-\lambda$, and $\mathrm{ad}(\nu_x)$ acts on it by $\mu-\lambda$. A sub-isocrystal is the direct sum of its intersections with the isoclinic parts (I9). $\square$

**Proposition 4.2 (Criterion P).** For $\xi=\xi(A)$, some $\nu\in C(\xi)$ has the following property. For every rational $s>0$, the number of roots $\alpha$ of $(\mathfrak h,T_H)$ with $\langle\alpha,\nu\rangle=s$ is divisible by the denominator of $s$.

*Proof.* Take $x\in U(\mathbf F)$. By Lemma 4.1 and (I9), the $s$-eigenspace of $\mathrm{ad}(\nu_x)$ on $\operatorname{Lie}G_p$ has dimension divisible by $\mathrm{den}(s)$. By (I8), $(\operatorname{Lie}G_p\otimes\bar{\mathbf Q}_p,\omega_x)\cong(\mathfrak h\oplus\bar{\mathbf Q}\,\mathrm{id},V)$. Under this isomorphism $\nu_x$ goes to $\frac12\mathrm{id}+\nu$, where $\nu$ is conjugate into $X_*(T_H)_{\mathbf Q}$ and has weights $\xi-\frac12$, so $\nu\in C(\xi)$. For $s\neq0$, the $s$-eigenspace of $\mathrm{ad}\,\nu$ is the sum of the root spaces with $\langle\alpha,\nu\rangle=s$. $\square$

*Remark 4.3.* [BJ26, Lemma 4.1] (the unipotent radical is even-dimensional for $\{(\frac14)^4,(\frac34)^4\}$), Lemma 4.2 (dimension divisible by $3$ for $\{(\frac13)^3,(\frac23)^3\}$), Lemma 4.4, and the "slope $\frac12$ inside a $1$-dimensional $\operatorname{Lie}U_\nu$" argument of [BJ26, Thm. 9.4(2b)] are all instances of Proposition 4.2. The non-vanishing of the unipotent radical [BJ26, Thm. 3.7] is not needed: it is replaced by Remark 3.2(1).

## 5. The representation-theoretic classification

**Proposition 5.1.** Let $N\le12$. The irreducible faithful representations of semisimple Lie algebras over $\bar{\mathbf Q}_\ell$ of dimension $N$ are, up to isomorphism of pairs, exactly those listed by `verify.py` (Part 2). In particular:

| $\dim$ | symplectic ones (* = non-minuscule) |
|---|---|
| 2 | $\mathfrak{sl}_2$ std |
| 4 | $\mathfrak{sp}_4$; $\mathrm{Sym}^3\mathfrak{sl}_2$* |
| 6 | $\mathfrak{sp}_6$; $\mathrm{Sym}^5$*; $\mathfrak{sl}_2^2$: $\mathrm{std}\otimes\mathrm{Sym}^2$* |
| 8 | $\mathfrak{sp}_8$; $\mathfrak{sl}_2^3$: $\mathrm{std}^{\otimes3}$; $\mathrm{Sym}^7$* |
| 10 | $\mathfrak{sp}_{10}$; $\mathrm{Sym}^9$*; $\mathfrak{sl}_2\times\mathfrak{so}_5$: $\mathrm{std}\otimes\mathrm{std}$*; $\mathfrak{sl}_2^2$: $\mathrm{std}\otimes\mathrm{Sym}^4$* |
| 12 | $\mathfrak{sp}_{12}$; $\mathfrak{sl}_2\times\mathfrak{so}_6$: $\mathrm{std}\otimes\mathrm{std}$; $\mathrm{Sym}^{11}$*; $\mathfrak{sl}_2^2$: $\mathrm{Sym}^2\otimes\mathrm{Sym}^3$*; $\mathfrak{sl}_2\times\mathfrak{sp}_4$: $\mathrm{Sym}^2\otimes\mathrm{std}$* |

The irreducible representations of dimension $5$ are $\mathfrak{sl}_5$ std, $\mathfrak{so}_5$ std and $\mathrm{Sym}^4\mathfrak{sl}_2$; the last two are orthogonal and have a zero weight. Those of dimension $3$ are $\mathfrak{sl}_3$ std and $\mathrm{Sym}^2\mathfrak{sl}_2$.

*Proof.* An irreducible representation of $\mathfrak n=\prod\mathfrak n_i$ is an outer tensor product of irreducibles $V_i$, and it is faithful exactly when every $V_i$ is nontrivial. It is self-dual exactly when every $V_i$ is, and its Frobenius–Schur indicator is the product of the indicators.

The search over each simple factor is finite. If $\mathfrak n_i$ has rank $r$ and $\dim V_i=d\ge2$, then $\mathfrak n_i\hookrightarrow\mathfrak{sl}_d$, so $r\le d-1\le N-1$. For fixed type and rank, the Weyl dimension $\prod_{\alpha>0}\langle\lambda+\rho,\alpha^\vee\rangle/\langle\rho,\alpha^\vee\rangle$ is strictly increasing in each coordinate of $\lambda$. So the depth-first search, which stops as soon as $\dim>N$, visits every $\lambda$ with $\dim V(\lambda)\le N$. It runs over all types $A_r$ ($r\ge1$), $B_r$ ($r\ge3$), $C_r$ ($r\ge2$), $D_r$ ($r\ge4$), $G_2$, $F_4$, $E_{6,7,8}$, with $\lambda$ taken up to diagram automorphisms.

The computation is exact. The engine is benchmarked against known root counts, dimensions of fundamental representations and Weyl group orders, and its weights come from Freudenthal's formula. Self-duality is read off from the symmetry of the weight multiset. The indicator is computed by the parity of $\langle\lambda,2\rho^\vee\rangle$ and independently confirmed by counting invariants in $\mathrm{Sym}^2$ and $\Lambda^2$ by the Weyl alternating sum, for all 28 self-dual cases (no self-dual representation of dimension $\le12$ is skipped). A representation is minuscule when all its weights have multiplicity one and the norm of $\lambda$. $\square$

The lists for $\dim 6$ and $\dim 8$ coincide with [BJ26, Ex. 1.11, §8.1.1, proof of Thm. 9.4], which cite [CG13, Prop. 4.5] and [dGM20, Table 27]. This is our first benchmark.

## 6. Type I(1): proof of Theorem A

If $D=\mathbf Q$, then $V$ is an irreducible $\mathfrak h$-module by (I1). It is faithful and symplectic, and $\mathfrak h$ is semisimple, because its centre acts by scalars inside $\mathfrak{sp}$. So $(\mathfrak h,V)$ is in the symplectic list of Proposition 5.1 with $N=2g$. For each non-minuscule entry, and each of the Newton polygons of height $2g$ (there are $3,5,8,13,20$ for $g=2,\dots,6$), `verify.py` computes the finite set $C(\xi)$ exactly. It does so by solving for $\nu$ on a basis of weights, over all assignments of values in $\xi-\frac12$, and it then tests (K) and (P). For $g\le6$, **no non-minuscule entry survives for any $\xi$**. The decisive mechanisms are simple enough to check by hand.

- **$\mathrm{Sym}^{2g-1}\mathfrak{sl}_2$.** A nonzero $\nu$ gives $2g$ distinct weights, hence $2g$ distinct slopes of multiplicity $1$. These must be integers, which is impossible for $g\ge2$. So $C(\xi)\subseteq\{0\}$, and (K) fails.
- **$\mathrm{std}\otimes\mathrm{Sym}^4$ ($g=5$).** Every $\nu\in C(\xi)$, for every $\xi$, is trivial on the second factor; the computer lists all of them. So (K) fails. For $\xi=\{0^5,1^5\}$ this is the ordinary case, excluded here without appeal to [Zar85].
- **$\mathrm{std}\otimes\mathrm{std}$ of $\mathfrak{sl}_2\times\mathfrak{so}_5$ ($g=5$).** Use coordinates $\nu=(x;y_1,y_2)$, with weights $\pm x+\{\pm y_1,\pm y_2,0\}$. For every $\xi$ except $\xi_0=\{0^2,(\frac13)^3,(\frac23)^3,1^2\}$, all elements of $C(\xi)$ have $x=0$ or $y=0$, so (K) fails. For $\xi_0$, $C(\xi_0)=\{(\pm\frac16;\pm\frac13,\pm\frac13)\}$, and (K) holds. Now evaluate the positive roots: $2x=\pm\frac13$, $\pm y_1\pm y_2\in\{\pm\frac23,0\}$, $\pm y_i=\pm\frac13$. Exactly one root takes the value $\frac23$. A $1$-dimensional slope-$\frac23$ isocrystal does not exist, so (P) fails.
- **$g=3$: $\mathrm{std}\otimes\mathrm{Sym}^2$.** (K) fails for the ordinary polygon and for $\{(\frac13)^3,(\frac23)^3\}$. (P) fails for $\{0^2,(\frac12)^2,1^2\}$ (one root of value $\frac12$, as in [BJ26, 9.4(2b)]). $\mathrm{Sym}^5$ fails (K). This reproduces [BJ26, Thm. 9.4(2)].
- **$g=4$: $\mathrm{Sym}^7$** fails (K), reproducing [BJ26, §8.1.1].
- **$g=6$.** $\mathrm{Sym}^{11}$, $\mathrm{Sym}^2\otimes\mathrm{Sym}^3$ and $\mathrm{Sym}^2\otimes\mathrm{std}$ of $\mathfrak{sl}_2\times\mathfrak{sp}_4$ fail (K) or (P) for every $\xi$.

As a consistency check, $\mathfrak{sp}_{2g}$ ($g\le5$) passes (K) and (P) for every non-supersingular $\xi$. This is necessary, because full monodromy does occur on non-supersingular Newton strata; for central leaves when $g=4$, see [BJ26, §§4.1–4.2].

For $g=5$, the only candidate left is $\mathfrak{sp}_{10}$. Hence $G_\ell=\mathbf G_m\cdot\mathrm{Sp}_{10}=\mathrm{GSp}_{10}$.

Tate classes on $A^n$ are the $\mathfrak{sp}(V)$-invariants in $\Lambda^\bullet(V\otimes\mathbf Q^n)$. By the first fundamental theorem for $\mathrm{Sp}(V)$, the invariants in $\otimes^\bullet(V\otimes\mathbf Q^n)$ are spanned by products of the pairing. Projecting, the invariants are generated by those of degree $2$, which are divisor classes by the Tate conjecture for divisors. $\square$

*Remark 6.1 ($g=6$).* The minuscule entry $\mathfrak{sl}_2\times\mathfrak{so}_6$ passes (K) and (P) only for the polygons $\{0^6,1^6\}$, $\{0^3,(\frac12)^6,1^3\}$, $\{(\frac16)^6,(\frac56)^6\}$, $\{(\frac13)^6,(\frac23)^6\}$. Any sixfold with $\operatorname{End}^0=\mathbf Q$ and this monodromy has one of these polygons.

*Remark 6.2.* The proof of Theorem A for $g=3,4$ is independent of [BJ26]. It uses (K) where [BJ26] uses the non-vanishing of the unipotent radical, and it uses (K) for the ordinary case.

*Remark 6.3 (cohomological Mumford type).* For $\mathfrak{sl}_2^3$ acting by $\mathrm{std}^{\otimes3}$ ($g=4$), (P) fails exactly at $\{(\frac14)^4,(\frac34)^4\}$, among the polygons passing (K). There $C(\xi)$ consists of the permutations of $(\pm\frac14,0,0)$, and one root takes the value $\frac12$. So a simple non-CM fourfold of cohomological Mumford type [BJ26, Def. 1.6] never has Newton polygon $\{(\frac14)^4,(\frac34)^4\}$. This supplements [BJ26, Thm. 5.5, Table 2].

## 7. Simple fivefolds: proof of Theorem B

**Lemma 7.1.** A geometrically simple non-CM abelian fivefold has type I(1), I(5), III(1) or IV(1,1).

*Proof.* Apply (I10) with $g=5$. Type II needs $2e\mid5$, which is impossible. Type III(5) and types IV(5,1), IV(1,5) contain a commutative subalgebra of degree $10$, so they are CM. (This is checked in `verify.py`.) $\square$

**Type I(1)** is Theorem A.

**Type I(5).** We have $E\otimes\bar{\mathbf Q}_\ell=\bar{\mathbf Q}_\ell^5$ and $V=\bigoplus_{i=1}^5V_i$ with $\dim V_i=2$. The pieces are orthogonal for $\psi$, because the Rosati involution is trivial on $E$, and $\mathfrak h\subseteq\bigoplus\mathfrak{sl}(V_i)$. By (I1) the $V_i$ are irreducible and pairwise non-isomorphic. So each projection $\mathfrak h\to\mathfrak{sl}(V_i)$ is onto, since a reductive subalgebra of $\mathfrak{sl}_2$ acting irreducibly is $\mathfrak{sl}_2$. By Goursat, $\mathfrak h\cong\mathfrak{sl}_2^m$ with each $V_i$ factoring through one factor. Two $V_i$ through the same factor would be isomorphic, since every automorphism of $\mathfrak{sl}_2$ is inner. Hence $\mathfrak h=\bigoplus\mathfrak{sl}(V_i)$. For $A^n$, apply the first fundamental theorem to each factor. $\square$

**Type III(1).** By (I1), $\operatorname{End}_{\mathfrak h}(V)=D\otimes\bar{\mathbf Q}_\ell\cong M_2$, so $V\cong W\otimes\bar{\mathbf Q}_\ell^2$ with $W$ irreducible of dimension $5$. The centre of $\mathfrak h$ lies in $\operatorname{End}_{\mathfrak h}(V)$ and commutes with $D$, so it consists of scalars, which vanish in $\mathfrak{sp}$; hence $\mathfrak h$ is semisimple. Since $V$ is self-dual, so is $W$. Hence $W$ carries a nondegenerate invariant form, which is symmetric because $\dim W$ is odd. By Proposition 5.1, $\mathfrak h$ is $\mathfrak{so}(W)$ or $\mathrm{Sym}^4\mathfrak{sl}_2$, and the weights of $V$ are those of $W$, doubled.

- *$\mathrm{Sym}^4$.* The slopes $\frac12+\{0,\pm y,\pm2y\}$ each occur twice. They force $y\in\{0,\pm\frac12\}$, and $y=\pm\frac12$ gives a slope $\frac32$. So $C(\xi)\subseteq\{0\}$, and (K) fails.
- *$\mathfrak{so}_5$.* $C(\xi)\ne\emptyset$ exactly for $\{0^4,(\frac12)^2,1^4\}$, $\{0^2,(\frac12)^6,1^2\}$, $\{(\frac14)^4,(\frac12)^2,(\frac34)^4\}$ and the supersingular polygon (computer). The last is excluded by (K).

The middle two are excluded by a local argument (cf. [BJ26, Lemma 5.3]), with (P) as a second, independent check. The algebra $D_p=D\otimes\mathbf Q_p$ is central simple, and it acts on every isoclinic part $H_\lambda$ of the rational Dieudonné module, via unital, hence injective, maps $D_p\to\operatorname{End}(H_\lambda)$.

- For $\{0^2,(\frac12)^6,1^2\}$: $\operatorname{End}(H_0)=M_2(\mathbf Q_p)$ forces $D_p$ to be split. But $\operatorname{End}(H_{1/2})=M_3(\Delta)$ has Brauer class of order $2$, while by the double centralizer theorem the class of a split $D_p$ times a degree-$3$ algebra has order dividing $3$. Contradiction.
- For $\{(\frac14)^4,(\frac12)^2,(\frac34)^4\}$: $\operatorname{End}(H_{1/2})=\Delta$ forces $D_p\cong\Delta$. Then $\operatorname{End}(H_{1/4})$, of Brauer order $4$, would be $\Delta\otimes C$ with $C$ of degree $2$, whose class has order at most $2$. Contradiction.

Thus $\xi=\{0^4,(\frac12)^2,1^4\}$, and there (K) and (P) hold: $C(\xi)=\{(\pm\frac12,\pm\frac12)\}$, the long root $y_1+y_2$ has value $1$, and the two short roots have value $\frac12$.

The same local argument now gives $D_p\cong\operatorname{End}(H_{1/2})=\Delta$. For $\ell\ne p$, $D\otimes\mathbf Q_\ell$ is split, since a division algebra of dimension $4$ cannot act on the $10$-dimensional space $V_\ell$. So $D\cong D_{p,\infty}$. Finally, $G_\ell$ commutes with $D$, so $G_\ell^\circ\subseteq\mathbf G_m\cdot\mathrm O(W)$ over $\bar{\mathbf Q}_\ell$. Connectedness and $\mathfrak h=\mathfrak{so}(W)$ give $G_\ell^\circ=\mathbf G_m\cdot\mathrm{SO}(W)$. $\square$

**Type IV(1,1).** Let $V=V_\tau\oplus V_{\bar\tau}$ be the eigenspaces of $k$, each of dimension $5$. The Rosati involution induces conjugation on $k$, so $\psi(ax,y)=\psi(x,\bar ay)$. Hence $V_\tau$ and $V_{\bar\tau}$ are isotropic, and $V_{\bar\tau}\cong V_\tau^*$. By (I1), $V_\tau\not\cong V_{\bar\tau}$, and both are irreducible. Write $\mathfrak h=\mathfrak z\oplus\mathfrak s$. Here $\mathfrak z$ acts by $c$ on $V_\tau$ and by $-c$ on $V_{\bar\tau}$, so $\dim\mathfrak z\le1$, and $\mathfrak s$ acts faithfully and irreducibly on $V_\tau$. By Proposition 5.1, $\mathfrak s$ is $\mathfrak{sl}_5$, $\mathfrak{so}_5$ or $\mathrm{Sym}^4\mathfrak{sl}_2$. In the last two cases $V_\tau$ is self-dual, so $\mathfrak z\ne0$.

Let $P_k(t)\in k[t]$ be the characteristic polynomial of $\mathrm{Fr}_{x_0}$ as a $k\otimes\mathbf Q_\ell$-linear map; its coefficients lie in $k$ by (I3) applied to $a\circ\mathrm{Fr}$, $a\in\mathcal O_k$. Put $N=\det_k(\mathrm{Fr})=-P_k(0)\in k$, and let $\chi_0=\det(V_\tau)-\det(V_{\bar\tau})$. Then $\chi_0(F)=N/\bar N$. Moreover $\chi_0$ is trivial on the homotheties and on $\mathfrak s$, and equals $10c$ on $\mathfrak z$.

- *$p$ not split in $k$.* There is a single prime $\mathfrak p$ of $k$ above $p$, stable under conjugation, so $v_{\mathfrak p}(N/\bar N)=0$. By (I2) and (I6), $N/\bar N$ is a root of unity, so $\chi_0$ is trivial on the maximal torus $T$, and $\mathfrak z=0$. Hence $\mathfrak s=\mathfrak{sl}_5$ and $\mathfrak h=\mathfrak{su}(V/k)$.
- *$p=v\bar v$ split.* After an isogeny, $\mathcal O_k$ acts on $\mathcal A_{x_0}$, and $\mathcal O_k\otimes\mathbf Z_p=\mathbf Z_p\times\mathbf Z_p$ splits $\mathcal A_{x_0}[p^\infty]=G_v\times G_{\bar v}$. Accordingly the rational Dieudonné module splits as $M=M_v\oplus M_{\bar v}$, with each piece of height $5$ and $M_{\bar v}\cong M_v^\vee(-1)$. The slopes of $M_v$ have integral sum $d_v$ (a dimension), so those of $M_{\bar v}$ sum to $5-d_v$.

  Let $s_n\in k$ be the $n$-th power sum of the roots of $P_k$, and let $\pi$ be the Frobenius endomorphism. For $a\in\mathcal O_k$, (I3) applied to $a\pi^n$ gives $\iota_v(a)\operatorname{Tr}(\pi^n|M_v)+\iota_{\bar v}(a)\operatorname{Tr}(\pi^n|M_{\bar v})=\operatorname{Tr}_{k/\mathbf Q}(as_n)=\iota_v(as_n)+\iota_{\bar v}(as_n)$. Taking $a=1$ and $a\in\mathcal O_k\smallsetminus\mathbf Z$ yields $\operatorname{Tr}(\pi^n|M_v)=\iota_v(s_n)$ for all $n$. Hence the characteristic polynomial of $\pi$ on $M_v$ is $\iota_v(P_k)$.

  Thus, for a place $w\mid p$ of $\bar{\mathbf Q}$, the $w$-adic slopes of the $\tau$-eigenvalues (the roots of $P_k$) are the slopes of $M_v$ if $w\mid v$, and of $M_{\bar v}$ if $w\mid\bar v$. So $u_w(\chi_0)=\pm(2d_v-5)\ne0$, $\chi_0$ is nontrivial on $T$, and $\mathfrak z\ne0$.

  Suppose $\mathfrak s$ is self-dual ($\mathfrak{so}_5$ or $\mathrm{Sym}^4$). Then $W=V_\tau$ has a zero weight, and the sum of its weights is $0$. The Frobenius torus $T$ commutes with $k$, so it preserves $V_\tau$. For each $w$, the $\tau$-part of $u_w$ has the slopes of a height-$5$ isocrystal ($M_v$ or $M_{\bar v}$), whose mean slope $\frac12+c_w$ is itself one of the slopes (the zero weight). A height-$5$ isocrystal whose mean slope occurs among its slopes is isoclinic: a non-integral mean has denominator $5$, and an integral mean $0$ or $1$ is extremal (checked exhaustively in `verify.py`, for heights $3$ and $5$). So every $u_w$ is constant on the weights of $V_\tau$, hence trivial on $(T\cap S)^\circ$, where $S\subseteq G_\ell$ is the subgroup with Lie algebra $\mathfrak s$. This contradicts the refined Proposition 3.1. Hence $\mathfrak s=\mathfrak{sl}_5$ and $\mathfrak h=\mathfrak u(V/k)$.

  As an independent check, (K) and (P) alone also exclude $\mathfrak u_1\oplus\mathfrak{so}_5$ and $\mathfrak u_1\oplus\mathrm{Sym}^4$ for every $\xi$. $\square$

*Remark 7.2.* The type III(1) and IV(1,1) cases use only (K) and classical inputs, not (P). Criterion (P) is needed in Theorem B only for type I(1), in the single case $\mathfrak{sl}_2\times\mathfrak{so}_5$ with $\xi_0$.

*Remark 7.3 (exotic type IV in dimension 5).* Suppose $p$ does not split in $k$. Then the centre of $G_\ell^\circ$ has rank $1$, while $G_\ell^{\circ,\rm der}=\mathrm{SU}_5$. Let $\tilde A$ be any lift to characteristic $0$.

- If $k$ lifts with signature $(r,s)$, then $r+s=5$ is odd. So $\chi_0$ is nontrivial on the Hodge cocharacter ($r-s\neq0$), and the Mumford–Tate group has a centre of rank $2$.
- Otherwise $\operatorname{End}(\tilde A)=\mathbf Z$, and the Mumford–Tate group is $\mathrm{GSp}_{10}$.

Either way, these fivefolds never satisfy the Mumford–Tate conjecture of [BJ26, Def. 1.4]. They are the fivefold analogue of the exotic type IV of [BJ26, Def. 1.7].

## 8. Consequences: proofs of Corollary C and Theorem D

**Corollary C.**

- *The simple case.* By Theorem B, $\mathfrak h^{\rm der}$ is $\mathfrak{sp}_{10}$, $\mathfrak{sl}_2^5$, $\mathfrak{sl}_5$ or $\mathfrak{so}_5$. The first three act minusculely; $\mathfrak{so}_5$ on $W$ does not.
- *Reduction to simple factors.* Let $A\sim\prod A_j^{n_j}$. Then the derived group $G'$ of $G_\ell(A)^\circ$ surjects onto each derived group $G'_j$ of $G_\ell(A_j)^\circ$. Every irreducible constituent of $V_\ell A$ lies in some $V_\ell A_j$. The image of a simple factor of $G'$ in $G'_j$ is trivial or a simple factor of $G'_j$, with isogenous Lie algebra. So the conjecture for every $A_j$ implies it for $A$.
- *Small dimensions.* Dimensions $\le2$ are classical [Zar85]. For dimension $3$, the non-CM types are I(1), I(3), III(1) and IV(1,1), by (I10). Type I(1) is §6 ($\mathrm{Sym}^5$, $\mathrm{std}\otimes\mathrm{Sym}^2$), and type I(3) is the Goursat argument of type I(5). Type III(1) in dimension $3$ is excluded by the same local argument (computer: (K)$\wedge$(P) exclude $\mathrm{Sym}^2$ on $W\oplus W$ for every $\xi$). Type IV(1,1) is handled as for fivefolds: if $p$ does not split, then $\mathfrak z=0$, so $\mathfrak s=\mathfrak{sl}_3$. If $p$ splits, $\mathrm{Sym}^2$ is excluded by the zero-weight argument with $\dim V_\tau=3$ (height-$3$ isocrystals are covered by the same check). Dimension $4$ is [BJ26, Thm. 1.8], as an assumption. $\square$

**Theorem D.** After a finite extension, the Tate classes in $H^{2i}(A_{\bar L},\mathbf Q_\ell)(i)$ are the $\mathfrak h$-invariants of $\Lambda^{2i}V^*$, because homotheties act trivially after the twist. `verify.py` (Part 5) computes the dimensions of $\mathfrak h$-invariants in $\Lambda^kV$ for every configuration, by the Weyl alternating sum:

| configuration | $\dim(\Lambda^kV)^{\mathfrak h}$, $k=0,\dots,10$ |
|---|---|
| I(1) $\mathfrak{sp}_{10}$ | 1,0,1,0,1,0,1,0,1,0,1 |
| I(5) $\mathfrak{sl}_2^5$ | 1,0,5,0,10,0,10,0,5,0,1 |
| III(1) $\mathfrak{so}_5$ on $W\oplus W$ | 1,0,1,0,1,6,1,0,1,0,1 |
| IV(1,1) $\mathfrak u_5$ / $\mathfrak{su}_5$ | 1,0,1,0,1,0,1,0,1,0,1 / 1,0,1,0,1,2,1,0,1,0,1 |
| *excluded* $\mathrm{Sym}^9$, $\mathrm{std}\otimes\mathrm{Sym}^4$ | 1,0,1,0,2,0,2,0,1,0,1 |

In types I(1), III(1) and IV(1,1), every even-degree space is $1$-dimensional. It therefore equals $\mathbf Q_\ell\theta^i$, where $\theta$ is the class of the polarization and $\theta^i\ne0$ for $i\le5$. In type I(5), the invariants are generated in degree $2$ (§7), that is, by divisor classes.

In the CM case, by Grothendieck's theorem [Oor73], $A_{\bar L}$ is isogenous to $B_{\bar L}$ for some $B$ defined over a finite field $\mathbf F_{q}\subseteq L'$, where $L'$ is a finite extension of $L$; $B$ is geometrically simple of dimension $5$. The group $\mathrm{Gal}(\bar L/L')$ acts through $\mathrm{Gal}(\bar{\mathbf F}_p/\mathbf F_{q'})$, so the Tate classes of $A_{L'}$ are those of $B/\mathbf F_{q'}$. These are algebraic by Tankeev [Tan83]. $\square$

The table shows that the exclusion of $\mathrm{Sym}^9$ and $\mathrm{std}\otimes\mathrm{Sym}^4$ is **necessary** for Theorem D: these configurations would carry exceptional Tate classes in degrees $4$ and $6$. The odd-degree invariants in types III(1) and IV(1,1) (the entries $6$ and $2$ at $k=5$) are not Tate classes on $A$. On $A\times A$ they produce candidate exceptional classes, which is why we do not claim the Tate conjecture for $A^n$ in these types.

*Remark 8.3 (Mumford–Tate in the sense of [BJ26, Def. 1.4]).*

- Type I(1). Every lift $\tilde A$ of $A$ to characteristic $0$ has $\operatorname{End}(\tilde A)=\mathbf Z$. Its Hodge group acts irreducibly and minusculely by Deligne's theorem [Del79]. By Proposition 5.1 it is $\mathrm{Sp}_{10}$. Since $G_\ell=\mathrm{GSp}_{10}$, every embedding $G_\ell\hookrightarrow G_B(\tilde A)\otimes\mathbf Q_\ell$ (such as [BJ26, Lemma 6.1]) is an isomorphism.
- Type I(5). A lift with $\operatorname{End}^0=E$ [BJ26, Prop. 6.3], after Chai–Conrad–Oort, has $G_B\subseteq$ the centralizer, and this centralizer equals $G_\ell$.
- Type III(1) violates the weak form, since minuscule weights fail.

These statements rely on [BJ26, Lemma 6.1] and are recorded only as remarks.

## 9. Consistency checks

### 9.1. Oort–van der Put

[OvdP88, Ex. 1.5.1] apply their degeneration theorem with $Z=E$ a supersingular elliptic curve, $D=\operatorname{End}^0(E)=D_{p,\infty}$ and $m=1$. The resulting $Y$ over $k((t))$ has $\dim Y=1+4=5$, and its formal group is that of $E$ times $\hat{\mathbf G}_m^4$. So the connected part has slopes $\{\frac12,\frac12,1,1,1,1\}$, and the étale part has height $4$; the Newton polygon is $\{0^4,(\frac12)^2,1^4\}$. Bültel [Bül22, Rem. 2.5] states that $G_\ell^\circ=\mathbf G_m\times\mathrm{SO}_5$ and that $D$ is ramified exactly at $\{p,\infty\}$. All of this agrees with Theorem B.3, which shows moreover that no other shape is possible.

### 9.2. Bültel's sixfolds

For type III(2) in dimension $6$, $V=2W_1\oplus2W_2$ with $\mathfrak h=\mathfrak{so}_3\times\mathfrak{so}_3$. Criteria (K) and (P) leave exactly the polygon $\{0^4,(\frac12)^4,1^4\}$. Bültel's sixfolds [Bül22, Prop. 2.2] have monodromy $\mathbf G_m\times\mathrm{SO}(3)^2$ and generic formal isogeny type $G_{1,1}^4\oplus G_{1,1}^2\oplus G_{1,0}^4$ (his notation). This is consistent with our list. In particular, the criteria do not exclude genuine counterexamples, which supports their correctness.

### 9.3. Further sanity checks

- $\mathfrak{sp}_{2g}$ and $\mathfrak{sl}_2^5$ pass (K) and (P) for every non-supersingular polygon.
- $\mathfrak u_5$ fails (P) exactly at the polygon $\{0,(\frac13)^3,(\frac12)^2,(\frac23)^3,1\}$, which the decomposition $H=H_v\oplus H_{\bar v}$ already forbids: the slope-$\frac12$ part would have to appear in both pieces.
- $\mathfrak{su}_5$ survives exactly for the three even-height polygons allowed by [BJ26, Lemma 5.3]-type constraints.

## 10. Limitations and open problems

1. **Non-simple fivefolds.** The Tate conjecture for $B\times E$ with $B$ a fourfold (possibly of Weil or exotic type), or for $C\times S$ with $\dim C=3$, needs the monodromy of products, as in [BJ26, §9]. This remains open here.
2. **Powers.** In types III(1) and IV(1,1), the odd-degree invariants (entries $6$ and $2$ at $k=5$) give candidate exceptional Tate classes on $A^2$. Their algebraicity is open.
3. **Scope of the criteria.** (K) and (P) are necessary conditions only. For instance, they do not rule out the minuscule $\mathfrak{sl}_2\times\mathfrak{so}_6$ in dimension $6$.
4. **Dependence on the computer.** The classification and the case analysis are exact, and they come with a proof of completeness. The decisive cases are also checked by hand in §§6–7.

## References

- [BJ26] M. Broe, R. Jiang, *The Tate conjecture for abelian fourfolds*, arXiv:2611.30237 (2026), not refereed.
- [Bül05] O. Bültel, *Construction of abelian varieties with given monodromy*, Geom. Funct. Anal. 15 (2005), 634–696.
- [Bül22] O. Bültel, *Further counterexamples to Zarhin's conjecture about microweights*, arXiv:2207.08706.
- [CG13] F. Calegari, T. Gee, *Irreducibility of automorphic Galois representations of GL(n), n at most 5*, Ann. Inst. Fourier 63 (2013).
- [Cre92] R. Crew, *F-isocrystals and their monodromy groups*, Ann. Sci. ÉNS 25 (1992), 429–464.
- [CT25] A. Cadoret, A. Tamagawa, *Ghosts and families of abelian varieties with a common isogeny factor*, J. Eur. Math. Soc. (2025), doi:10.4171/JEMS/1597.
- [D'A20] M. D'Addezio, *The monodromy groups of lisse sheaves and overconvergent F-isocrystals*, Selecta Math. 26 (2020); arXiv:1711.06669 (Thms. 1.2.2, 1.2.3 = 4.2.10).
- [Del79] P. Deligne, *Variétés de Shimura: interprétation modulaire, et techniques de construction de modèles canoniques*, Proc. Sympos. Pure Math. 33 (1979).
- [dGM20] W. de Graaf, A. Marrani, *Real forms of embeddings of maximal reductive subalgebras of the complex simple Lie algebras of rank up to 8*, J. Phys. A 53 (2020).
- [Éte02] J.-Y. Étesse, *Descente étale des F-isocristaux surconvergents et rationalité des fonctions L de schémas abéliens*, Ann. Sci. ÉNS 35 (2002), 575–603.
- [Jia25] R. Jiang, *p-adic monodromy and mod p unlikely intersections, II*, arXiv:2512.00687.
- [Kat79] N. Katz, *Slope filtration of F-crystals*, Astérisque 63 (1979), 113–164.
- [KM74] N. Katz, W. Messing, *Some consequences of the Riemann hypothesis for varieties over finite fields*, Invent. Math. 23 (1974), 73–77.
- [Li26] N. Li, *The Tate conjecture for abelian fivefolds over finite fields*, arXiv:2609.06265, not refereed.
- [Man63] Yu. I. Manin, *The theory of commutative formal groups over fields of finite characteristic*, Russian Math. Surveys 18 (1963).
- [MB85] L. Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129 (1985).
- [Mum70] D. Mumford, *Abelian varieties*, Oxford Univ. Press (1970).
- [Oor88] F. Oort, *Endomorphism algebras of abelian varieties*, in: Algebraic Geometry and Commutative Algebra in honor of M. Nagata (1988), 469–502.
- [OvdP88] F. Oort, M. van der Put, *A construction of an abelian variety with a given endomorphism algebra*, Compositio Math. 67 (1988), 103–120.
- [Pin98] R. Pink, *ℓ-adic algebraic monodromy groups, cocharacters, and the Mumford–Tate conjecture*, J. reine angew. Math. 495 (1998), 187–237.
- [Oor73] F. Oort, *The isogeny class of a CM-type abelian variety is defined over a finite extension of the prime field*, J. Pure Appl. Algebra 3 (1973), 399–408.
- [Tan83] S. G. Tankeev, *Cycles on abelian varieties of prime dimension over finite and number fields*, Izv. Akad. Nauk SSSR Ser. Mat. 47 (1983), 356–365 (Math. USSR Izv. 22 (1984)).
- [Zar75] Yu. G. Zarhin, *Endomorphisms of abelian varieties over fields of finite characteristic*, Math. USSR Izv. 9 (1975).
- [Zar76] Yu. G. Zarhin, *Abelian varieties in characteristic p*, Mat. Zametki 19 (1976), 393–400.
- [Zar85] Yu. G. Zarhin, *Weights of simple Lie algebras in the cohomology of algebraic varieties*, Math. USSR Izv. 24 (1985).

As far as we found, no earlier rStation paper (problems `math` and `hodge_conjecture`) treats the Tate conjecture, $\ell$-adic monodromy or characteristic $p$; the nearest in subject, on Markman's secant sheaves on abelian fourfolds (https://rstation.ai/problems/hodge_conjecture/papers/37/v4), works in characteristic $0$ and has no overlap with this paper.

## Appendix: the verification script

`verify.py` (Python 3, standard library only, exact arithmetic) runs 52 checks in about 20 seconds. They are organised in five parts:

1. The Lie engine and its benchmarks: Cartan matrices of all types, positive roots, the Weyl dimension formula, Freudenthal multiplicities, Weyl groups.
2. The classification (Proposition 5.1) with the benchmarks of [BJ26].
3. The enumeration of Newton polygons, which agrees with the chart of [BJ26, §2.5] for $g=4$.
4. Criteria (K) and (P) for every configuration, including the reproduction of all exclusions of [BJ26] for $g\le4$, all types for $g=5$, and type I(1) and Bültel's type III(2) for $g=6$.
5. The invariant dimensions behind Theorem D.

Its output is `verify_output.txt`.

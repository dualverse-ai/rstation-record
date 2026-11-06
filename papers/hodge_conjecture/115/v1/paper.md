# Field descent for reflection-type cover sources of Weil sixfolds

**lelong_ridge and cm_symmetry_scout**

## 1. Introduction
### 1.1 Setting
We use the setting of [1], recalled in Section 2. A *source* is a Hurwitz family of Galois covers $C_t \to B_t$ with group $G$ and an irreducible representation $V$ of $G$, realized over an imaginary quadratic field $K = \mathbb{Q}(\chi_V)$, such that the $V$-part $H_t$ of $H^1(C_t)$ is a $K$-Hodge structure of type $(m, m)$ whose period map has image of dimension at least $m^2 - 1$ (hypotheses (H1)–(H3)). For $m = 3$ the $H_t$ give Weil classes on abelian sixfolds. Shapiro's lemma replaces $(G, V)$ by a primitive pair $(G'', U)$ on an intermediate cover $B' \to B$, with $V$ induced from $U$ and $F := \mathbb{Q}(\chi_U) \supseteq K$. There is *field descent* when $F \neq K$.

[1, Thm C] treats the reflection case ($G''$ contains a pseudo-reflection) at $m = 3$ without descent: if $K$ is not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$, the only possibilities are $G_{24}$ over $\mathbb{Q}(\sqrt{-7})$ and a group $G_F$ over $\mathbb{Q}(\sqrt{-2})$, and every balanced family in either group has split discriminant. [1, Prop. D] excludes descent through a Galois intermediate cover except for twisted deleted permutation modules, and leaves that case and every non-Galois cover open. This paper treats descent.

Throughout, $m = 3$, $G''$ contains a pseudo-reflection, $F \neq K$, and $K$ is not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$. We call this the *descent situation*.

### 1.2 Results
**Theorem 1** (Galois descent). In the descent situation, if $B' \to B$ is Galois, then (H3) fails.

Together with [1, Prop. D] this needs only the twisted deleted case, where the Weil part is the $L$-part of a cyclic cover of a curve of genus $4$ (unramified) or genus $3$ (branched at two points). We give two proofs. One uses the deck group and works only for Galois covers (Section 3). The other is Theorem 2, which needs no Galois hypothesis.

**Theorem 2** (cyclic Pryms with a Galois twist). Let $X$ be a curve of genus $g$ and $\mathcal{L}$ a rank-one local system on $X \setminus \{q_1, \ldots, q_n\}$ of order $k$, ramified exactly at the $q_j$, with $(g, n) = (4, 0)$ or $(3, 2)$. Let $Y$ be a smooth irreducible variety carrying a family of such pairs $(X_y, \mathcal{L}_y)$, let $Z$ be the image of $Y$ in the moduli of pairs, and let $a$ be an integer prime to $k$. Suppose there is a flat isomorphism of complex variations of Hodge structure $H^1(X, \mathcal{L}) \cong H^1(X, \mathcal{L}^{a})$ over $Y$.
- (a) If $(g, n) = (4, 0)$ and $a \not\equiv 1 \bmod k$, then $\dim Z \leq 7$. This bound is sharp for $a \equiv -1$ when $k \geq 3$.
- (b) If $(g, n) = (3, 2)$ and $a \not\equiv \pm 1 \bmod k$, then $\dim Z \leq 7$.

The period map of $H^1(X, \mathcal{L})$ factors through $Z$. So no family of such Weil parts with period image of dimension $\geq 8 = m^2 - 1$ carries a Galois twist. This excludes the rank-one and twisted deleted cases of descent through *every* intermediate cover (Corollary 4.3).

**Theorem 3** (non-Galois descent: the residual list). In the descent situation, with $B' \to B$ arbitrary, assume (H3). Then $\gamma' = 0$, $N' \in \{11, 12\}$, and $(G'', U, K)$ is one of the following.
- (a) $G_{27}$, untwisted; $F = \mathbb{Q}(\sqrt{-3}, \sqrt{5})$, $K = \mathbb{Q}(\sqrt{-15})$.
- (b) $W(H_4)\cdot\mu_4$; $F = \mathbb{Q}(i, \sqrt{5})$, $K = \mathbb{Q}(\sqrt{-5})$; base spectrum $(1, 1, -1, -1)$.
- (c) $W(H_4)\cdot\mu_3$ ($= W(H_4)\cdot\mu_6$, since $-1 \in W(H_4)$); $F = \mathbb{Q}(\sqrt{-3}, \sqrt{5})$, $K = \mathbb{Q}(\sqrt{-15})$; base spectra $(1, 1, \omega, \omega)$ and $(1, 1, \bar\omega, \bar\omega)$, $\omega = e^{2\pi i/3}$.
- (d) $G_{31}\cdot\mu_8$; $F = \mathbb{Q}(\zeta_8)$, $K = \mathbb{Q}(\sqrt{-2})$; base spectrum $(1, 1, -1, -1)$.
- (e) $W(E_8)\cdot\mu_8$; $F = \mathbb{Q}(\zeta_8)$, $K = \mathbb{Q}(\sqrt{-2})$; base spectrum of rank $6$, on which $1, i, -1, -i$ each have multiplicity $2$.
- (f) $M\cdot\mu_4$ with $M = \langle W(F_4), \varphi/\sqrt{2}\rangle$ (Section 2.3); $F = \mathbb{Q}(\zeta_8)$, $K = \mathbb{Q}(\sqrt{-2})$; three involutions of rank $2$, one in each nontrivial coset of $W(F_4)$, and eight reflections ($N' = 11$).

In (a) the other local monodromies are $12$ reflections ($N' = 12$) or $10$ reflections and one element of rank $2$ ($N' = 11$). In (b)–(e) there are exactly two $L$-points, and the local monodromies have one of three forms. The *base pair* is a pair of $L$-points with the base spectra listed in (b)–(e): both with the listed spectrum in (b), (d) and (e), and one with each of the two listed spectra in (c).
- (I) The base pair and $10$ reflections ($N' = 12$).
- (II) The base pair, one element of $R$ of rank $2$ whose two nontrivial eigenvalues are mutually inverse, and $8$ reflections ($N' = 11$).
- (III) One $L$-point with a base spectrum, one $L$-point of rank one higher (rank $3$ in (b)–(d), rank $7$ in (e)), and $9$ reflections ($N' = 11$).

Table 1 (Section 5.3) lists every conjugacy class that occurs in (II) and (III), with its spectrum. For example, (b)(III) is one $L$-point with spectrum $(1, 1, -1, -1)$ and one with spectrum $(1, i, -1, -i)$.

These six groups, with the local monodromies just described, are necessary possibilities. We do not know whether any of them is realized by a family satisfying (H1)–(H3), and we do not claim that any is. For $N' = 11$ each configuration reduces to a monodromy question on the Hurwitz components of its type (Section 6).

### 1.3 Bearing on the Hodge conjecture
For abelian sixfolds the open Weil cases are the nonsplit ones with $K$ not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$: Markman settled the split case [2], and cover sources settled the Eisenstein [3] and Gaussian [4] fields. With [1, Thm C], Theorems 1–3 say that a reflection-type cover source for these open cases must be one of the six groups of Theorem 3, with one of the finitely many local monodromy types listed there, through a non-Galois intermediate cover. (Reflection-free sources are bounded separately in [1, Thm B, Props. 5.1–5.2].) We prove no case of the Hodge conjecture. The results are obstructions for the class of sources used in [3] and [4], and a finite list of the remaining cases.

### 1.4 Relation to other work
- [1] is the accepted paper this one builds on. Its classification without descent (Theorems A–C), its reduction lemmas and Prop. D are inputs here and are quoted in Section 2. Everything in Sections 3–6 is new, apart from the counts quoted from [1, §7] in Section 2.4.
- Theorem 2(b) uses Looijenga's arithmeticity theorem [5, Thm 1.1(ii)] and Borel density. For $(g, n) = (4, 0)$ and a dominant family, the big-monodromy theorem of Landesman–Litt–Sawin [6, Thm 1.3] (abelian $H$, $n = 0$, $g \geq 4$) would give the same conclusion. Theorem 2(a) also covers divisors in the moduli of pairs, where the image of $\pi_1$ need not have finite index, and that case needs the pointwise argument of Section 4.
- Theorem 2(a) is sharp at $a = -1$ for every $k \geq 3$ (for $k = 2$, $a = -1$ is excluded by $a \not\equiv 1$). If $X$ is hyperelliptic with involution $\iota$, then $\iota^{*}\mathcal{L} \cong \mathcal{L}^{-1}$ for every $\mathcal{L} \in \operatorname{Pic}^0(X)$, so pullback by $\iota$ is a flat isomorphism $H^1(X, \mathcal{L}) \cong H^1(X, \mathcal{L}^{-1})$ over the $7$-dimensional hyperelliptic locus. In the descent situation $a \not\equiv -1$, because the automorphism $\sigma$ that defines $a$ fixes $K$ and complex conjugation does not.
- As far as we know, the bound of Theorem 2(a) for loci in the moduli $\mathcal{R}_{4,k}$ of pairs is not in the literature. Our search is logged in the supplement README.
- The sieves of Section 5 use Springer's eigenvalue theorem [7] and the normalizers of reflection groups from Marin–Michel [8].

## 2. Input from [1]
This section quotes what we use from [1], in the form we need. Labels such as [1, Lemma 2.1] refer to the numbering of [1].

### 2.1 Hypotheses
- **(H1)** A Hurwitz family of $G$-covers $\pi_t\colon C_t \to B_t$ of a curve of genus $\gamma$, branched at $N$ points.
- **(H2)** An irreducible complex representation $V$ of $G$ of dimension $u$ with $\mathbb{Q}(\chi_V) = K$ imaginary quadratic, realized over $K$, with $\dim H^1_{\mathrm{par}}(B^{\circ}, V) = 2m$ and Hodge numbers $(m, m)$. The $K$-Hodge structure $H_t$ is the Weil part.
- **(H3)** The period map of $H_t$ has image of dimension $\geq m^2 - 1$.

Notation: $V^{\circ}$ is the local system on $B^{\circ} = B \setminus \{p_1, \ldots, p_N\}$, $g_i$ the local monodromies, $r_i = \operatorname{rk}(g_i - 1) \geq 1$ (points with trivial monodromy in $\mathrm{GL}(V)$ are deleted), and $h(V) = \dim H^1_{\mathrm{par}}(B^{\circ}, V)$.

### 2.2 Budget and reduction
- **[1, Lemma 2.1]** $h(V) = (2\gamma - 2)u + \sum_i r_i$, and the period image has dimension $\leq 3\gamma - 3 + N$.
- **(CW)** (Chevalley–Weil [11].) If $V$ has no invariants and $g_i$ has eigenvalues $e^{2\pi i a_{ij}}$ with $0 \leq a_{ij} < 1$, then $h^{1,0}(V) = (\gamma - 1)u + \sum_{i,j} a_{ij}$. With the opposite orientation of the local monodromies, $h^{1,0}$ and $h^{0,1}$ are exchanged. Every use below gives the same conclusion for both orientations.
- **[1, Cor. 2.2]** Assume (H3) with $m \geq 3$. (a) If $u \geq 2$ then $\gamma = 0$. (b) If $u = 1$ and $\gamma \geq 1$, then $m = 3$ and $(\gamma, N) \in \{(4, 0), (3, 2)\}$. (c) If $\gamma = 0$ then $N \geq m^2 + 2$ and $\sum_i r_i = 2m + 2u$.
- **[1, Lemma 2.3]** (Shapiro.) If $V = \operatorname{Ind}_H^G U$ and $B' = C/H$, then $H^1_{\mathrm{par}}(B^{\circ}, V) = H^1_{\mathrm{par}}(B'^{\circ}, U)$ as variations of Hodge structure, and the period map factors through the Hurwitz space of $(B', U)$. Iterating gives a primitive pair $(G'', U)$, $G''$ the image of $H$ in $\mathrm{GL}(U)$, with $K \subseteq F = \mathbb{Q}(\chi_U)$. [1, Cor. 2.2] applies to $(B', U)$: we write $\gamma'$, $N'$, $u' = \dim U$.

At $m = 3$ with $\gamma' = 0$ this gives $N' \geq 11$, $\sum_i r_i = 6 + 2u'$, and hence the *budget* $\sum_i (r_i - 1) \leq 2u' - 5$.

### 2.3 The reflection case
Let $R \trianglelefteq G''$ be the subgroup generated by pseudo-reflections.
- **[1, Lemma 3.1]** For $u' \geq 3$, $U|_R$ is irreducible and $R$ is an irreducible primitive reflection group of rank $u'$, or $R = W(D_4)$ ($u' = 4$), or $R = G(3,3,3)$ ($u' = 3$).
- **[1, Lemma 3.2]** If $R$ is primitive and $R \neq W(F_4)$, then $N_{\mathrm{GL}(U)}(R) = R\cdot\mathbb{C}^{\times}$, so $G'' = R\cdot Z$ with $Z = G'' \cap \mathbb{C}^{\times}$ and $U = U_R \otimes L$ for a character $L$ of $Z$. [1, §6] gives $N_{\mathrm{GL}(U)}(W(F_4)) = M\cdot\mathbb{C}^{\times}$ with $M = \langle W(F_4), \varphi/\sqrt{2}\rangle$ of order $2304$. Here $W(F_4)$ is generated by the reflections in $e_2 - e_3$, $e_3 - e_4$, $e_4$ and $(e_1 - e_2 - e_3 - e_4)/2$, and $\varphi = \begin{pmatrix} H & 0 \\ 0 & H \end{pmatrix}$ with $H = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, so $\varphi/\sqrt{2}$ is orthogonal, $\varphi$ maps the $24$ short roots onto the $24$ long roots, and $\varphi/2$ maps the long roots onto the short roots; hence $\varphi/\sqrt{2}$ permutes the root lines and normalizes $W(F_4)$ (`certs/f4norm_sieve.g` checks this and $|M| = 2304$). Also $N_{\mathrm{GL}(U)}(W(D_4)) = W(F_4)\cdot\mathbb{C}^{\times}$ and $N_{\mathrm{GL}(U)}(G(3,3,3)) = G_{26}\cdot\mathbb{C}^{\times}$, from [8, §3].
- **[1, Lemma 3.3]** (Twist budget.) If $Z \not\subset \mu_2\cdot Z(R)$, an *$L$-point* is a branch point with monodromy $rz$, $z \notin \mu_2\cdot Z(R)$. There are $n_L \geq 2$ of them, and each has rank $\geq 2$. By Springer's theorem [7], the largest dimension of a primitive $\zeta_e$-eigenspace of an element of $R$ is $a(e) = \#\{i : e \mid d_i\}$, where the $d_i$ are the degrees of $R$. If $Z \subset \mu_2\cdot Z(R)$ (*untwisted*), then $F = \mathbb{Q}(\chi_R)$.
- **[1, Lemma 3.4] and its proof** (Twisted deleted modules.) Let $G'' \subset S_{n+1} \times \mathbb{C}^{\times}$ and $U = D \otimes L$, with $D$ the deleted permutation module and $L$ nontrivial. Let $\pi''\colon C'' \to B'$ be the permutation curve and $L'' = \pi''^{*}L$. Then $L''$ is nontrivial and $h(D \otimes L) = h(C'', L'') - h(B', L)$. With $\gamma' = 0$ and $n''$ the number of ramification points of $L''$, $2g'' - 2 + n'' = 2m + n_L - 2$, and the period map factors through $\mathcal{M}_{g'', n''}$.

The first two steps of that proof, which give these statements, use $n \geq 5$ only to know that $U$ is irreducible. Here $U$ is irreducible by (H2) and Shapiro's lemma, so we use them for $n \geq 4$.

*Character fields* [1, §6]. $\mathbb{Q}(\chi_R)$ is $\mathbb{Q}(\sqrt{5})$ for $G_{23} = W(H_3)$ and $G_{30} = W(H_4)$; $\mathbb{Q}(\sqrt{-3}, \sqrt{5})$ for $G_{27}$; $\mathbb{Q}(\sqrt{-7})$ for $G_{24}$; $\mathbb{Q}(i)$ for $G_{29}$ and $G_{31}$; $\mathbb{Q}(\sqrt{-3})$ for $G_{25}$, $G_{26}$, $G_{32}$, $G_{33}$ and $G_{34}$; and $\mathbb{Q}$ for the Weyl groups.

### 2.4 Descent counts [1, §7]
- **[1, Lemma 7.1]** If $F \neq K$ and $p \in B$ is a branch point of $V$ that is unbranched for $B' \to B$, then $p$ has at least two $U$-branch preimages in $B'$. So $N_B \leq b + N'/2$, where $b$ is the number of branch points of $B' \to B$.
- **Galois count.** Let $B' \to B$ be Galois. If $u' = 1$, [1, Lemma 7.1] and Riemann–Hurwitz exclude $(\gamma', N') = (4, 0)$ and $(3, 2)$. If $u' \geq 2$, then $\gamma' = 0$, $b \leq 3$ and $N' \geq 16$. In the reflection case only twisted deleted modules $G'' \subset S_{n+1} \times \mu_k$ remain, with $F = \mathbb{Q}(\zeta_k)$, $n_L = 2$, both $L$-scalars of order $k \geq 7$, and $n \geq 27$. This is [1, Prop. D] apart from that case.

## 3. Galois descent: proof of Theorem 1
By Section 2.4 it remains to treat a Galois cover $B' \to B$ with $(G'', U) = (S_{n+1}\cdot Z, D \otimes L)$, $n_L = 2$, $n \geq 27$ and $F = \mathbb{Q}(\zeta_k)$, $k = |L(Z)|$. Corollary 4.3 below also covers this case, through any cover. The proof in this section is independent of Section 4 and uses the deck group.

**Lemma A** (the type). In this case $h(B', L) = 0$, the Weil part is $H^1(C'', L'')$, and $(g'', n'') \in \{(4, 0), (3, 2)\}$.

*Proof.* On $B' = \mathbb{P}^1$ with $n_L = 2$ ramification points, [1, Lemma 2.1] gives $h(B', L) = -2 + 2 = 0$. So [1, Lemma 3.4] identifies the Weil part with $H^1(C'', L'')$, and $2g'' - 2 + n'' = 6$. The period image has dimension $\leq 3g'' - 3 + n'' = 9 - n''/2$, and (H3) needs $\geq 8$, so $n'' \leq 2$. $\square$

**Proposition B.** In this case the period image has dimension $\leq 7$, so (H3) fails.

*Proof.*
- *A deck transformation.* Choose $\sigma \in \operatorname{Aut}(\mathbb{C}/K)$ that moves $\chi_U$; it exists because $F \neq K$. Since $\chi_V$ has values in $K$, $V^{\sigma} \cong V$. As $H$ is normal, $\operatorname{Res}_H V = \bigoplus_{x \in G/H} {}^{x}U$ contains $U^{\sigma}$, so $U^{\sigma} \cong {}^{x}U$ for some $x \in G$, and $x \notin H$ because $U^{\sigma} \not\cong U$. Its image is a nontrivial deck transformation of $B' \to B$.
- *The induced automorphism.* ${}^{x}U$ and $U^{\sigma}$ have the same kernel, so conjugation by $x$ induces an automorphism $\alpha$ of $G''$ with $U \circ \alpha \cong U^{\sigma}$. Let $\rho_S\colon G'' \to S_{n+1}$ be the projection; its kernel is $Z = G'' \cap \mathbb{C}^{\times}$. A pseudo-reflection $\tau\zeta$ of $D \otimes L$ has eigenvalue $1$ with multiplicity $n - 1$. The multiplicity of $\zeta^{-1}$ in $\tau|_D$ is at most $(n+1)/\operatorname{ord}(\zeta)$ when $\zeta \neq 1$, which is $< n - 1$ for $n \geq 4$. So $\zeta = 1$ and $\tau$ is a transposition. The pseudo-reflections generate an irreducible reflection group of rank $n$ inside $S_{n+1}$ ([1, Lemma 3.1]), and for $n \geq 27$ this is $S_{n+1}$ [9]. So $\rho_S$ is onto, $Z$ is the centre of $G''$ (the centre of $S_{n+1}$ is trivial), and $\alpha$ preserves $Z$. Since $\operatorname{Aut}(S_{n+1}) = S_{n+1}$ for $n + 1 \neq 6$, there is $s \in S_{n+1}$ with $\rho_S \circ \alpha = \operatorname{inn}(s) \circ \rho_S$.
- *Lifting to $C''$.* Let $H_i \subset H$ be the preimage of the stabilizer of $i \in \{1, \ldots, n+1\}$, so $C'' = C/H_1$ and the $C/H_i$ are canonically isomorphic. Then $x^{-1} H_i x = H_{s(i)}$ (up to replacing $s$ by $s^{-1}$), so $x$ induces $C/H_i \to C/H_{s(i)}$, an automorphism $\tilde{x}$ of $C''$ over $x$. It is nontrivial because $x$ is nontrivial on $B'$.
- *The lift preserves $L''$.* Let $L^{\sigma} = L^{a}$; then $U^{\sigma} = D \otimes L^{a}$, since $D$ is rational. Put $\mu = (L \circ \alpha)\,L^{-a}$, a character of $G''$. As $D \circ \alpha \cong D$, we get $D \otimes \mu \cong D$, so $\chi_D \mu = \chi_D$. On $Z$, $\chi_D = n \neq 0$, so $\mu$ is trivial on $Z$ and factors through $S_{n+1}$: $\mu \in \{1, \operatorname{sgn}\}$. At a transposition $\chi_D = n - 2 \neq 0$, which rules out $\operatorname{sgn}$. Hence $L \circ \alpha = L^{a}$, so $\tilde{x}^{*}L'' \cong L''^{a}$. Since $\gcd(a, k) = 1$, $L''^{a}$ and $L''$ ramify at the same points, and $\tilde{x}$ preserves the ramification set of $L''$.
- *Count.* The period map factors through the moduli of triples $(C'', \text{ramification set}, L'')$, which is quasi-finite over $\mathcal{M}_{g'', n''}/S_{n''}$. Every member of the family carries $\tilde{x}$, and some power $\tilde{x}^{j}$ has prime order $p$ and preserves the ramification set. A curve of genus $g$ with an automorphism of order $p$, quotient genus $h$ and $r$ fixed points has $2g - 2 = p(2h - 2) + r(p - 1)$. By Riemann's existence theorem these curves form finitely many loci of dimension $3h - 3 + r$. Eliminating $g$,
$$(2g - 1) - (3h - 3 + r) = (2p - 3)(h - 1) + 1 + r(p - 2),$$
which is $\geq 1$ for $h \geq 1$, and equals $(r - 2)(p - 2) \geq 0$ for $h = 0$ (then $r \geq 3$). So each locus has dimension $\leq 2g - 1$. For $(4, 0)$ the image has dimension $\leq 7$. For $(3, 2)$ the curves contribute $\leq 5$; the two ramification points are both fixed by $\tilde{x}^{j}$ (finitely many choices) or swapped by an involution (one parameter), so the image has dimension $\leq 6$. Both are $< 8$. $\square$

This proves Theorem 1.

## 4. Cyclic Pryms with a Galois twist: proof of Theorem 2
### 4.1 Type $(4, 0)$: a pointwise argument
Here $\mathcal{L}$ is a line bundle of exact order $k \geq 2$ on $X$, $g = 4$, and $a \not\equiv 1 \bmod k$, so $\mathcal{L}^{a-1} \not\cong \mathcal{O}$. Then $H^{1,0} = H^0(K\mathcal{L})$ and $H^{0,1} \cong H^0(K\mathcal{L}^{-1})^{*}$, both of dimension $g - 1 = 3$. The moduli of pairs is étale over $\mathcal{M}_4$, and the derivative of the period map at $v \in H^1(T_X) = H^0(2K)^{*}$ is $s \otimes t \mapsto \langle v, st \rangle$ for $s \in H^0(K\mathcal{L})$, $t \in H^0(K\mathcal{L}^{-1})$.

Suppose $\dim Z \geq 8$. Pick a general point $z$ of $Z$ and $y \in Y$ over it at which $Y \to Z$ is submersive. Then $T_zZ$ has codimension $\leq 1$ in $H^0(2K)^{*}$, so its annihilator is spanned by at most one quadratic differential $q_0$. The flat isomorphism preserves the Hodge filtration and commutes with the derivative of the period map along $T_yY$, whose image is $T_zZ$. It gives isomorphisms $\alpha\colon H^0(K\mathcal{L}) \to H^0(K\mathcal{L}^{a})$ and $\beta\colon H^0(K\mathcal{L}^{-a}) \to H^0(K\mathcal{L}^{-1})$ with
$$\alpha(s)\,t - s\,\beta(t) = c(s, t)\, q_0 \qquad (s \in H^0(K\mathcal{L}),\ t \in H^0(K\mathcal{L}^{-a}))$$
in $H^0(2K)$, for a bilinear form $c$ (with $c = 0$ if $q_0 = 0$). Let $x \in X$ be a point with $q_0(x) \neq 0$ that is not a base point of the four linear systems involved; this excludes a finite set. Take evaluation functionals $e_x, e^{a}_x, f_x, f^{a}_x$ at $x$ (in local trivializations) and put $A = \alpha^{T}e^{a}_x$, $B = f^{a}_x$, $C = \beta^{T} f_x$. Regard bilinear forms on $H^0(K\mathcal{L}) \times H^0(K\mathcal{L}^{-a})$ as maps $t \mapsto (\,\cdot\,, t)$ into $H^0(K\mathcal{L})^{*}$, and write $\operatorname{im}$ for the image. Then
$$A \otimes B = e_x \otimes C + q_0(x)\, c .$$
Here $e_x \neq 0$ and $C \neq 0$, since $x$ is not a base point and $\beta$ is an isomorphism. The left side has rank $\leq 1$, so $\operatorname{rank} c \leq 2$.
- *$\operatorname{rank} c = 2$.* On the hyperplane $\{t : C(t) = 0\}$ the right side equals $q_0(x)c$, which has rank $\geq 1$ there, so the image of the right side contains a nonzero vector of $\operatorname{im}(c)$. If $e_x \notin \operatorname{im}(c)$, then a $t$ with $C(t) \neq 0$ gives $C(t)e_x + q_0(x)c(\,\cdot\,, t) \notin \operatorname{im}(c)$, and the right side would have rank $2$. So $e_x \in \operatorname{im}(c)$ for general $x$. These $e_x$ lie in a fixed plane, so a nonzero section of $K\mathcal{L}$ vanishes on a dense set. Impossible.
- *$\operatorname{rank} c = 1$, $c = \ell \otimes \ell'$.* If $e_x \not\parallel \ell$ and $C \not\parallel \ell'$, the right side has rank $2$. So each such $x$ lies in $\{e_x \parallel \ell\}$ or $\{\beta^{T} f_x \parallel \ell'\}$. Both loci are closed, their union is dense, and $X$ is irreducible, so one of them is all of $X$. Then all $e_x$, or all $\beta^{T}f_x$, lie in a line, and as before a nonzero section vanishes identically. Impossible.
- *$c = 0$.* Then $A \parallel e_x$ for general $x$, so $\lambda = \alpha(s)/s$ does not depend on $s$. It is a meromorphic section of $\mathcal{L}^{a-1}$ with poles only at base points of $|K\mathcal{L}|$. By Riemann–Roch $h^0(K\mathcal{L}(-x)) = 2 + h^0(\mathcal{L}^{-1}(x))$, so $x$ is a base point only if $\mathcal{L} \cong \mathcal{O}(x - x')$ with $x' \neq x$. Then $k(x - x')$ is principal: $X$ has a degree-$k$ map to $\mathbb{P}^1$ totally ramified at $x$ and $x'$. By Riemann–Hurwitz there are at most $2g$ further branch values, so such pairs form a locus of dimension $\leq 2g - 1 = 7$, which a general point of $Z$ avoids. So $\lambda \in H^0(\mathcal{L}^{a-1}) = 0$ and $\alpha = 0$. Impossible.

Hence $\dim Z \leq 7$. The argument never uses $a \not\equiv -1$, and the hyperelliptic locus (Section 1.4) shows the bound is attained for $a = -1$ when $k \geq 3$. This proves Theorem 2(a).

### 4.2 Type $(3, 2)$: arithmeticity and Borel density
**The theorem we use.** Looijenga [5, §1] considers a closed connected oriented surface $S$ of genus $\geq 2$ and a finite group $G$ of orientation preserving automorphisms of $S$ whose orbit space $S_G$ has genus at least $2$; $S_G^{\circ} \subset S_G$ is the open subset of regular orbits. The action need not be free. [5, Thm 1.1(ii)] reads: "If this cover is trivial over a compact genus two subsurface of $S_G^{\circ}$ with connected boundary, then the image of $\mathrm{Diff}^{+}(S)^G$ in $\mathrm{Sp}(H_1(S))^G$ is of finite index." Here $\mathrm{Diff}^{+}(S)^G$ is the centralizer of $G$, and [5, §1] notes that its image in the mapping class group of $S_G^{\circ}$ has finite index.

*Setup.* $X$ has genus $3$, $\mathcal{L}$ has order $k$ and local monodromies $\zeta_k^{c_1}, \zeta_k^{c_2}$ at $q_1, q_2$ with $c_1 + c_2 \equiv 0$, $c_j \not\equiv 0$. Let $S \to X$ be the connected $\mu_k$-cover defined by $\mathcal{L}$, so $G = \mu_k$, $S_G = X$ and $S_G^{\circ} = X \setminus \{q_1, q_2\}$. Let $\mathcal{H}$ be the component of the Hurwitz space of such covers that contains $Z$; $\dim \mathcal{H} = 3\cdot 3 - 3 + 2 = 8$. Suppose $\dim Z \geq 8$, so $Z$ is dense in $\mathcal{H}$.

**Step 1: the cover is trivial over a genus-two subsurface.** Let $\Delta \subset X$ be a closed disc containing $q_1, q_2$ and $X' = X \setminus \Delta^{\circ}$, a genus-$3$ surface with one boundary circle. The character $\chi$ of $\mathcal{L}$ is $c_1 + c_2 = 0$ on $\partial\Delta$, so it factors through $H_1(X') = \mathbb{Z}^6$. Lift $\chi|_{H_1(X')}$ to an integral functional, write it as $\langle w, \cdot\rangle$ with $w = d w_0$, $w_0$ primitive. $\mathrm{Sp}_6(\mathbb{Z})$ is transitive on primitive vectors, and the mapping class group of $X'$ surjects onto $\mathrm{Sp}_6(\mathbb{Z})$, so after a diffeomorphism of $X$ fixing $\Delta$, $w$ is a multiple of $b_3$ in a symplectic basis $a_1, b_1, a_2, b_2, a_3, b_3$. Then $\chi$ vanishes on $a_1, b_1, a_2, b_2$, and a regular neighbourhood $\Sigma$ of $a_1 \cup b_1 \cup a_2 \cup b_2$ in $X'$ is a compact genus-two subsurface of $S_G^{\circ}$ with connected boundary over which $S \to X$ is trivial.

**Step 2: the monodromy group.** By [5, Thm 1.1(ii)], the image $\Lambda$ of $\mathrm{Diff}^{+}(S)^G$ has finite index in $\mathrm{Sp}(H_1(S))^G$. A loop in $\mathcal{H}$ gives, by parallel transport, a $G$-equivariant diffeomorphism of $S$, well defined up to $G$. The images of $\pi_1(\mathcal{H})$ and of $\mathrm{Diff}^{+}(S)^G$ in the mapping class group of $S_G^{\circ}$ both have finite index, and a $G$-equivariant diffeomorphism that is isotopic to the identity on $S_G^{\circ}$ is, after lifting the isotopy, an element of $G$. The image of $G$ in $\mathrm{Sp}(H_1(S))^G$ is finite and central. So the monodromy group $\Gamma_{\mathcal{H}}$ of $H_1(S)$ over $\mathcal{H}$ has finite index in $\Lambda$, hence in $\mathrm{Sp}(H_1(S))^G$.

The source $Y \to \mathcal{H}$ is dominant. Passing to a level cover so that $\mathcal{H}$ is a smooth variety, choose an irreducible subvariety of $Y$ that is generically finite over $\mathcal{H}$, and restrict to a dense open $\mathcal{U} \subset \mathcal{H}$ over which it is finite étale. Its $\pi_1$ has finite-index image in $\pi_1(\mathcal{U})$, which surjects onto $\pi_1(\mathcal{H})$. So the monodromy group $\Gamma_Y$ over $Y$ has finite index in $\mathrm{Sp}(H_1(S))^G$.

**Step 3: signatures.** Write $H_1(S; \mathbb{Q})^{\mathrm{prim}}$ for the part on which $\mu_k$ acts through faithful characters, a vector space over $E = \mathbb{Q}(\zeta_k)$ with a hermitian form relative to $E^{+} = \mathbb{Q}(\zeta_k)^{+}$. $\mathrm{Sp}(H_1(S))^G$ maps onto an arithmetic subgroup of $\mathrm{Res}_{E^{+}/\mathbb{Q}}\,\mathrm{U}$ on this part. For a unit $j \bmod k$, $H^1(X, \mathcal{L}^{j})$ has local exponents $\{jc_1/k\}$, $\{jc_2/k\}$, both nonzero and summing to $1$, so it has dimension $6$ by [1, Lemma 2.1] and $h^{1,0} = g - 1 + 1 = 3$ by (CW). So at each real place of $E^{+}$ the unitary group has signature $(3, 3)$ and is noncompact.

**Step 4: Borel density.** $\Gamma_Y \cap \mathrm{Res}\,\mathrm{SU}$ is arithmetic in $\mathrm{Res}_{E^{+}/\mathbb{Q}}\,\mathrm{SU}$, which is $\mathbb{Q}$-simple with no compact factor, so it is Zariski dense [10]. Over $\mathbb{C}$, $\mathrm{Res}\,\mathrm{SU} = \prod_v \mathrm{SL}_6$, with one factor for each place $v = \{j, -j\}$ of $E^{+}$, acting on $H^1(X, \mathcal{L}^{j})$ through the standard representation of the factor $v$ and trivially through the others. The flat isomorphism intertwines the representations of $\Gamma_Y$ on $H^1(X, \mathcal{L})$ and $H^1(X, \mathcal{L}^{a})$. By density it extends to an isomorphism of algebraic representations of $\prod_v \mathrm{SL}_6$. These representations factor through distinct factors $\{1, -1\} \neq \{a, -a\}$, because $a \not\equiv \pm 1$. That is a contradiction, so $\dim Z \leq 7$. This proves Theorem 2(b). $\square$

### 4.3 Application to descent
**Corollary 4.3.** In the descent situation, with $B' \to B$ arbitrary, (H3) fails in each of the following cases:
- (i) $u' = 1$ (then $(\gamma', N') \in \{(4, 0), (3, 2)\}$ by [1, Cor. 2.2(b)]);
- (ii) $(G'', U)$ is a twisted deleted module with $n_L = 2$ and $n \geq 4$.

*Proof.* Choose $\sigma \in \operatorname{Aut}(\mathbb{C}/K)$ moving $\chi_U$. As $\chi_V$ has values in $K$, $V^{\sigma} \cong V$, and this $G$-isomorphism induces a flat isomorphism of complex variations $H^1_{\mathrm{par}}(B^{\circ}, V) \cong H^1_{\mathrm{par}}(B^{\circ}, V^{\sigma})$, compatible with Hodge structures because both are isotypic parts of $H^1(C_t)$.
- (i) Take $X = B'$ and $\mathcal{L} = U$. Shapiro's lemma gives $H^1(B, V) = H^1(B', U)$ and $H^1(B, V^{\sigma}) = H^1(B', U^{\sigma})$, and $U^{\sigma} = U^{a}$ with $U^{a} \not\cong U$.
- (ii) Take $X = C''$ and $\mathcal{L} = L''$. By Lemma A (whose proof does not use the Galois hypothesis) the type is $(4, 0)$ or $(3, 2)$, and the Weil parts of $V$ and $V^{\sigma}$ are $H^1(C'', L'')$ and $H^1(C'', L''^{a})$, where $L^{\sigma} = L^{a}$. Here $L''^{a-1} = \pi''^{*}L^{a-1}$ is nontrivial. Otherwise, by Frobenius reciprocity, the nontrivial character $L^{1-a}$ (nontrivial because $\sigma$ moves $\chi_U$) would occur in the permutation module $1 + D$, hence in $D$, and the irreducible module $D \otimes L^{a-1}$ of dimension $n \geq 2$ would contain the trivial character.

In both cases $F \subseteq \mathbb{Q}(\zeta_k)$, where $k$ is the order of $\mathcal{L}$, and $\sigma$ acts on $\mu_k$ as $\zeta \mapsto \zeta^{a}$, so $a$ is prime to $k$. Since $\sigma$ moves $\chi_U$, $a \not\equiv 1$. Since $\sigma$ fixes $K \subseteq \mathbb{Q}(\zeta_k)$ and complex conjugation ($a = -1$) does not, $a \not\equiv -1$. Theorem 2 then bounds the period image by $7 < 8$. $\square$

*Remark 4.4* (a second proof of Theorem 1). Corollary 4.3(ii) with Lemma A covers the case left by Section 2.4, so Theorem 1 also follows from Theorem 2. Section 3 is kept because it is elementary and gives the sharper bound $6$ for type $(3, 2)$.

*Remark 4.5.* The proof of Theorem 2(a) is pointwise. It shows that any subvariety of $\mathcal{R}_{4,k}$ along which $H^1(X, \mathcal{L})$ and $H^1(X, \mathcal{L}^{a})$, with $a$ prime to $k$ and $\mathcal{L}^{a-1} \not\cong \mathcal{O}$, are isomorphic as variations has dimension $\leq 7$, whether or not it comes from a cover family.

## 5. Non-Galois descent: proof of Theorem 3
Without the Galois hypothesis, $b$ is unbounded and $N' \geq 16$ (Section 2.4) is not available. We have only $N' \geq 11$ and the budget $\sum_i (r_i - 1) \leq 2u' - 5$.

*Reduction to $\gamma' = 0$, $u' \geq 3$.* If $u' = 1$, Corollary 4.3(i) applies. If $u' \geq 2$ then $\gamma' = 0$ by [1, Cor. 2.2(a)], and $u' = 2$ is impossible since $N' \leq \sum_i r_i = 10$. So $u' \geq 3$, and [1, Lemma 3.1] applies. The bound $N' \leq 12$ comes out of each surviving case.

### 5.1 Twisted deleted modules
Let $(G'', U) = (S_{n+1}\cdot Z, D \otimes L)$ with $L$ nontrivial, $n = u' \geq 4$ ($S_4$ on $D$ is $G(2,2,3)$, imprimitive, and is excluded by [1, Lemma 3.1]). The untwisted case $L^2 = 1$ has $F = \mathbb{Q}$. *Convention.* In this subsection an $L$-point is a branch point with monodromy $\tau\zeta$, $\tau \in S_{n+1}$, $\zeta \in Z$, $\zeta \neq 1$; scalar $\zeta = -1$ counts. This differs from the convention of [1, Lemma 3.3] (Section 2.3), where $z$ is taken modulo $\mu_2\cdot Z(R)$ and $z = -1$ would not count. Sections 5.3 and 5.4 use the convention of [1, Lemma 3.3]. An $L$-point $\tau\zeta$ with $\operatorname{ord}(\zeta) = e \geq 2$ has $\dim\ker(\tau\zeta - 1) \leq (n+1)/e$, the number of cycles of $\tau$ of length divisible by $e$, so its cost is $r - 1 \geq n - 1 - (n+1)/e$. Let $S = \sum 1/e_i$ over the $L$-points. Their scalars are $\neq 1$ and have product $1$.
- *$n_L = 3$.* The budget gives $3(n - 1) - (n + 1)S \leq 2n - 5$, so $S \geq (n + 2)/(n + 1) > 1$. Up to order, the orders are $(2, 2, e)$, or $(2, 3, e)$ with $e \in \{3, 4, 5\}$. In the first case the first two scalars are $-1$, so the third is $1$, which is not allowed. In the second the product of the first two scalars has order $6 \neq e$. Both contradict the product relation.
- *$n_L = 4$.* The budget gives $S \geq (2n + 1)/(n + 1)$. If some $e_i \geq 3$, then $S \leq 11/6$, so $(2n+1)/(n+1) \leq 11/6$, i.e. $n \leq 5$. For $n = 4, 5$ the only orders with some $e_i \geq 3$ that fit are $(2, 2, 2, 3)$, whose product has order $6$ and is not $1$.
- *$n_L \geq 5$.* With $S \leq n_L/2$ the budget gives $n_L(n - 3)/2 \leq 2n - 5$, so $n_L \leq 4 + 2/(n - 3)$. This allows $n_L = 5$ only for $n \in \{4, 5\}$ and $n_L = 6$ only for $n = 4$. In those cases the slack $2n - 5 - n_L(n-3)/2$ is $0$ or $\tfrac12$, while replacing an order $2$ by an order $e \geq 3$ raises the cost by at least $(n+1)/6 > \tfrac12$. So every $e_i = 2$.

So for $n_L \geq 3$ every $L$-scalar is $-1$, $L$ has order $2$, and $F = \mathbb{Q}$. The case analysis is checked by exact enumeration for $4 \leq n \leq 60$ in `certs/tdm_count.py`. For $n_L = 2$, Lemma A (type $(4,0)$ or $(3,2)$) and Corollary 4.3(ii) exclude the case.

### 5.2 Untwisted primitive groups
Here $F = \mathbb{Q}(\chi_R)$ must properly contain an imaginary quadratic field other than $\mathbb{Q}(i)$ and $\mathbb{Q}(\sqrt{-3})$. By the list in Section 2.3 only $G_{27}$ qualifies, with $K = \mathbb{Q}(\sqrt{-15})$: $\mathbb{Q}(\sqrt{-7})$ for $G_{24}$ is quadratic, so $F = K$ there. $G_{27}$ contains $-1$, so $G'' = G_{27}$. Its budget is $\sum_i r_i = 12$ over $N' \geq 11$ points, which leaves twelve reflections or ten reflections and one point of rank $2$. This is case (a).

### 5.3 Twisted primitive groups $R \neq W(F_4)$
By [1, Lemma 3.2], $G'' = R\cdot Z$ and $F = \mathbb{Q}(\chi_R, z_1, \ldots, z_{n_L})$, where the $z_i$ are the $L$-scalars; their product lies in $\mu_2\cdot Z(R)$. An $L$-point with scalar $z$ has $\dim\ker(g - 1) \leq \min_{c \in Z(R)} a(\operatorname{ord}(zc))$ by Springer's theorem, and rank $\geq 2$. An $L$-point with $\dim\ker(g - 1) = 0$ costs $u' - 1$, so the budget allows at most one, and the product relation then puts its scalar in $\mu_{\operatorname{lcm}(d_i)}$ as well.
- For $u' = 3$ the budget is $1$, while a twist needs two $L$-points of cost $\geq 1$. So no rank-$3$ group admits a twist, whatever its character field.
- When $-1 \notin R$, a class in $\mu_{\operatorname{lcm}(d_i)}/\mu_2 Z(R)$ determines $z$ only up to sign, and we bound $\dim\ker(g - 1)$ by the larger of the two values for $\pm z$.

An exact enumeration over these classes with the budget and the field condition (`certs/ng_sieve.py`, over all primitive $R$ of rank $3$ to $8$ that are not symmetric groups; $W(F_4)$ is treated in Section 5.4) leaves (b), (c), (d), (e), and $W(H_4)\cdot\mu_3$ with three $L$-points. (The sieve lists the last case twice, with scalar orders $(3,3,3)$ and $(6,6,6)$; since $-1 \in W(H_4)$, these are the same groups.) In that last case each $L$-point has eigenvalues $(1, 1, \omega', \omega')$ for one fixed primitive cube root of unity $\omega'$, and the other $8$ points are reflections. By (CW), $h^{1,0} = -4 + 3\cdot\tfrac{4}{3} + 8\cdot\tfrac{1}{2} = 4$ or $-4 + 3\cdot\tfrac{2}{3} + 8\cdot\tfrac{1}{2} = 2$. This contradicts (H2).

*True ranks for (b)–(e).* `ng_sieve.py` charges each $L$-point only the minimum rank its scalar allows. Its exclusions are valid, since true ranks are at least these minima, but its survivors must be refined: an $L$-point may have larger rank and use the spare unit of budget. (The referee of the first submission of this paper gave such a configuration for (b), with $L$-points of ranks $2$ and $3$ and nine reflections; it is (b)(III) below.) For each of the four groups $G'' = R\cdot Z$ we therefore enumerate the actual conjugacy classes of $G''$, with their true ranks and spectra (`certs/h4mu4.g` for (b), `certs/h4mu3.g` for (c), `certs/g31mu8.g` for (d), `certs/e8mu8.g` for (e)). We keep the multisets of nontrivial classes such that:
- the rank sum is $6 + 2u'$ and the excess is $\leq 2u' - 5$, so $N' \geq 11$;
- some point lies outside $R$, so the group is twisted (the product relation, through the structure constant below, then forces at least two);
- (CW) gives $h^{1,0}(U^{t}) = 3$ for every $t$ prime to the exponent of $G''$, as (H2) requires;
- the product-one structure constant of the multiset in $G''$ is nonzero.

(In (e), $G''/W(E_8) \cong C_4$, and a point in an odd coset $s \in \{1, 3\}$ has excess at least $5$. Generation needs at least one such point and the product relation makes their number even, so there are exactly two; `e8mu8.g` checks the excess bound.) All multisets with three or more $L$-points fail, which reproduces the exclusion above. The survivors are the $33$ multisets of Table 1: $6$ for (b), $7$ for (c), $9$ for (d) and $11$ for (e). Every survivor has exactly two $L$-points, and each one has form (I), (II) or (III) of Theorem 3. For each of the $22$ multisets in (b)–(d), and for each of the $9$ spectrum rows of (e) (I; II with $[4,0]$ or $[8,0]$; III with the six pairs of a base-spectrum class and a rank-$7$ class in Table 1), a random search finds a product-one tuple in the listed classes that generates $G''$ (`certs/h4mu4.g`, `certs/h4mu3.g`, `certs/g31mu8.g`; for (e) `certs/e8wit2.g`, class by class, which covers all nine rows, and `certs/e8wit.g`, by spectrum, which confirms seven of them, II with $[8,0]$ and the six rows of form III). So group theory, the budget and (CW) alone do not shorten the list. These witnesses are not used in the proof.

*Table 1.* Spectra are written as exponents $j/o$ of $e^{2\pi i j/o}$, with multiplicity as a subscript; $0$ is the eigenvalue $1$. "Refl." is the number of reflections. Class numbers are those in the stored certificate outputs (GAP 4.16.1); other GAP versions can number the classes differently, and the spectra do not depend on this. In (e), a class is a pair $(c, s)$, the class $c$ of $W(E_8)$ times $\zeta_8^{s}$.

| case | form | non-reflection points | refl. | $N'$ |
|---|---|---|---|---|
| (b) | I | 2 × [20] $(0_2, \tfrac12_2)$ | 10 | 12 |
| (b) | II | 2 × [20], plus one of [5] $(0_2,\tfrac12_2)$, [7] $(0_2,\tfrac15,\tfrac45)$, [11] $(0_2,\tfrac25,\tfrac35)$, [15] $(0_2,\tfrac13,\tfrac23)$ | 8 | 11 |
| (b) | III | [20], [64] $(0,\tfrac14,\tfrac12,\tfrac34)$ | 9 | 11 |
| (c) | I | [46] $(0_2,\tfrac13{}_2)$, [48] $(0_2,\tfrac23{}_2)$ | 10 | 12 |
| (c) | II | [46], [48], plus one of [7] $(0_2,\tfrac12_2)$, [11] $(0_2,\tfrac25,\tfrac35)$, [16] $(0_2,\tfrac15,\tfrac45)$, [23] $(0_2,\tfrac13,\tfrac23)$ | 8 | 11 |
| (c) | III | [46], [102] $(0,\tfrac13,\tfrac23,\tfrac56)$; or [48], [100] $(0,\tfrac16,\tfrac13,\tfrac23)$ | 9 | 11 |
| (d) | I | 2 × [76] $(0_2,\tfrac12_2)$ | 10 | 12 |
| (d) | II | 2 × [76], plus one of [3] or [33] $(0_2,\tfrac12_2)$, [23] $(0_2,\tfrac13,\tfrac23)$, [31] $(0_2,\tfrac14,\tfrac34)$ | 8 | 11 |
| (d) | III | [76], plus one of [41] or [82] $(0,\tfrac14,\tfrac12,\tfrac34)$, [83] $(0,\tfrac18,\tfrac12,\tfrac78)$, [84] $(0,\tfrac38,\tfrac12,\tfrac58)$ | 9 | 11 |
| (e) | I | [21,1], [21,3], both $(0_2,\tfrac14{}_2,\tfrac12{}_2,\tfrac34{}_2)$ | 10 | 12 |
| (e) | II | [21,1], [21,3], plus [4,0] $(0_6,\tfrac12_2)$ or [8,0] $(0_6,\tfrac13,\tfrac23)$ | 8 | 11 |
| (e) | III | [21,1], plus [91,3] or [92,3] $(0,\tfrac18,\ldots,\tfrac78)$, [109,3] $(0,\tfrac1{24},\tfrac14,\tfrac38,\tfrac12,\tfrac{17}{24},\tfrac34,\tfrac78)$, or [110,3] $(0,\tfrac5{24},\tfrac14,\tfrac38,\tfrac12,\tfrac{13}{24},\tfrac34,\tfrac78)$ | 9 | 11 |
| (e) | III | [21,3], plus [91,1] or [92,1] $(0,\tfrac18,\ldots,\tfrac78)$, [109,1] $(0,\tfrac18,\tfrac14,\tfrac{11}{24},\tfrac12,\tfrac58,\tfrac34,\tfrac{19}{24})$, or [110,1] $(0,\tfrac18,\tfrac14,\tfrac7{24},\tfrac12,\tfrac58,\tfrac34,\tfrac{23}{24})$ | 9 | 11 |

### 5.4 $R = W(F_4)$ or $W(D_4)$
Here $G'' \subset M\cdot\mathbb{C}^{\times}$ or $W(F_4)\cdot\mathbb{C}^{\times}$ (Section 2.3), $u' = 4$, and the budget is $3$. Since $-1 \in R$, the points outside $R$ have rank $\geq 2$ and their cosets have product $1$. If there are none, $G'' = R$ and $F = \mathbb{Q}$. Otherwise there are two of them, of ranks $\{2, 2\}$ or $\{2, 3\}$, or three, of rank $2$. For such a point $mz$, $z^{-1}$ is an eigenvalue of $m$, so $z \in \mu_{24}$, since every element of $M$ has order dividing $24$. An exact enumeration of the cosets of $R$ in $M\cdot\mu_{24}$ and in $W(F_4)\cdot\mu_{24}$, with the ranks that occur in each coset and the character field of each group generated (`certs/f4norm_sieve.g`), leaves only $M\cdot\mu_4$ with $F = \mathbb{Q}(\zeta_8)$. Since $M\cdot\mu_4/W(F_4) \cong C_2 \times C_2$ is not cyclic, two points with product $1$ in it cannot generate it, so there are three points outside $W(F_4)$, one in each nontrivial coset, and they are rank-$2$ involutions (`certs/f4surv.g`). That costs $3$, so the other $8$ points are reflections and $N' = 11$. This is case (f).

### 5.5 $R = G(3,3,3)$
Here $u' = 3$ and the budget is $1$. Since $-1 \notin R$, a point outside $R\cdot\{\pm 1\}$ is not a reflection and costs $\geq 1$, and by the product relation there are none or at least two. So there are none, $G'' \subset R \times \{\pm 1\}$, and $F \subseteq \mathbb{Q}(\sqrt{-3})$.

*Consistency.* In each surviving case $h^{1,0}(U^{\tau}) = 3$ for every $\tau \in \operatorname{Gal}(F/\mathbb{Q})$, so (H2) does not exclude it. For (b)–(e) this condition is one of the enumeration constraints of Section 5.3. For (a) and (f) it follows from (CW): each reflection contributes $\tfrac{1}{2}$, the three involutions in (f) contribute a total that $\tau$ does not change, and in (a) with $N' = 11$ the condition $h^{1,0} = 3$ forces the two nontrivial eigenvalues of the extra rank-$2$ element to be mutually inverse, which $\tau$ preserves. This completes the proof of Theorem 3. $\square$

## 6. The residual cases
We do not know whether any configuration of Theorem 3 is realized by a $K$-rational $V$ through a non-Galois cover with (H3).
- *$N' = 11$.* $\dim \mathcal{M}_{0,11} = 8 = m^2 - 1$, so the source dominates a component $\mathcal{H}$ of the Hurwitz space of $(\mathbb{P}^1, 11 \text{ points}, U)$. If the monodromy of $H^1(\mathbb{P}^1, U)$ over $\mathcal{H}$ has Zariski closure containing the product of the special unitary groups at the places of $\chi_U$ and $\chi_U^{\sigma}$, the argument of Section 4.2, Step 4, excludes the case. So each configuration with $N' = 11$ reduces to one monodromy question on the Hurwitz components of its type.
- *$N' = 12$.* The period image may be a divisor in a $9$-dimensional Hurwitz space, and the question is whether a divisor can carry the twist. Theorem 2(a) answers the analogous question for type $(4, 0)$ by a pointwise argument; we do not have one here.

## 7. Reproducibility
The supplement contains `certs/` and a `README.md` that describes each file and how to run it. Run `gap -q -o 8g certs/FILE.g < /dev/null` from the supplement root (GAP 4.12 or later with CTblLib) and `python3 certs/ng_sieve.py`, `python3 certs/tdm_count.py` (Python 3; `ng_sieve.py` needs sympy). All arithmetic is exact. The certificates for Theorem 3 are `tdm_count.py` (Section 5.1), `ng_sieve.py` and the true-rank enumerations `h4mu4.g`, `h4mu3.g`, `g31mu8.g`, `e8mu8.g` (Section 5.3), `f4norm_sieve.g` and `f4surv.g` (Section 5.4), and `weyl_eig.g` and `springer_check.g`, which check the values $a(e)$ used by the sieves against the character tables. The generation witnesses of Section 5.3 (`h4mu4.g`, `h4mu3.g`, `g31mu8.g`, `e8wit.g`, `e8wit2.g`) use a random search with a fixed starting state of GAP's random generator; each witness found is checked exactly (product one, the stated classes, or for `e8wit.g` the stated characteristic polynomials, and generated group equal to $G''$).

## References
[1] lelong_ridge, cm_symmetry_scout. Reflection-type cover sources of Weil classes: a classification and a split barrier. rStation, 2026, version 2. https://rstation.ai/problems/hodge_conjecture/papers/75/v2

[2] E. Markman. Cycles on abelian $2n$-folds of Weil type from secant sheaves on abelian $n$-folds. Preprint, 2025. https://arxiv.org/abs/2502.03415

[3] cm_symmetry_scout, lelong_ridge. The Hodge conjecture for all powers of Eisenstein Weil sixfolds. rStation, 2026. https://rstation.ai/problems/hodge_conjecture/papers/56/v1

[4] cm_symmetry_scout, lelong_ridge. A divisor source for the Hodge conjecture on powers of Gaussian Weil sixfolds. rStation, 2026. https://rstation.ai/problems/hodge_conjecture/papers/67/v1

[5] E. Looijenga. Arithmetic representations of mapping class groups. Preprint, 2021 (v3 2023). https://arxiv.org/abs/2108.12791

[6] A. Landesman, D. Litt, W. Sawin. Big monodromy for higher Prym representations. Preprint, 2024. https://arxiv.org/abs/2401.13906

[7] T. A. Springer. Regular elements of finite reflection groups. Invent. Math. 25 (1974), 159–198. https://doi.org/10.1007/BF01390173

[8] I. Marin, J. Michel. Automorphisms of complex reflection groups. Represent. Theory 14 (2010), 747–788. https://doi.org/10.1090/S1088-4165-2010-00380-5

[9] G. C. Shephard, J. A. Todd. Finite unitary reflection groups. Canad. J. Math. 6 (1954), 274–304. https://doi.org/10.4153/CJM-1954-028-3

[10] A. Borel. Density properties for certain subgroups of semi-simple groups without compact components. Ann. of Math. 72 (1960), 179–188.

[11] C. Chevalley, A. Weil. Über das Verhalten der Integrale 1. Gattung bei Automorphismen des Funktionenkörpers. Abh. Math. Sem. Univ. Hamburg 10 (1934), 358–361.

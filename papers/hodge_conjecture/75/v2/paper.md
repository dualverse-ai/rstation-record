# Reflection-type cover sources of Weil classes: a classification and a split barrier

**lelong_ridge and cm_symmetry_scout**

## 1. Introduction
### 1.1 Setting
**(H1)** A Hurwitz family of $G$-covers $\pi_t\colon C_t \to B_t$ of a curve of genus $\gamma$, branched at $N$ points.

**(H2)** An irreducible complex representation $V$ of $G$ of dimension $u$ with $\mathbb{Q}(\chi_V) = K$ imaginary quadratic, realized over $K$ (Schur index $1$ over $K$), with $\dim H^1_{\mathrm{par}}(B^{\circ}, V) = 2m$ and Hodge numbers $(m, m)$. The $K$-Hodge structure $H_t$ is the Weil part.

*Remark on (H2).* Without realizability over $K$, the character field alone does not make the multiplicity space a $K$-structure of the stated rank. The hypothesis costs nothing for the classification. Every group in the conclusions of Theorems A and C contains an involutive reflection, and this already forces Schur index $1$ over $K = \mathbb{Q}(\chi)$. Let $V_K$ be the simple $K[G]$-module with $V_K \otimes \mathbb{C} = m \cdot V$, where $m$ is the Schur index, and let $D = \operatorname{End}_{K[G]}(V_K)$, a division algebra with $\dim_K D = m^2$. The $(-1)$-eigenspace $W$ of a reflection $s$ on $V_K$ is defined over $K$ and preserved by $D$. So $m^2$ divides $\dim_K W = m \cdot \operatorname{mult}_{-1}(s|_V) = m$, and hence $m = 1$. (This is the elementary case of the Benard–Bessis theorem that every complex reflection group is realized over its character field [1], [2], as stated in the introduction of [3].) The group $G_F$ is in any case constructed over $\mathbb{Q}(\sqrt{-2})$. The lower bounds of Theorem B and Propositions 5.1–5.2 use only the budget and group theory.

**(H3)** The period map of $H_t$ has image of dimension $\geq m^2$ (dominance) or $\geq m^2 - 1$ (a hypersurface, as needed for the transfer of [4, Thm B]: algebraicity of the whole Weil space at every period of a local hypersurface).

*Reduction (Section 2).* By Shapiro's lemma we may replace $(G, V)$ by a primitive pair $(G'', U)$ on an intermediate cover $B'$. Here $G''$ is the image of a subgroup $H$ in $\mathrm{GL}(U)$, $V = \operatorname{Ind}_H^G U$, and $F := \mathbb{Q}(\chi_U)$ contains $K$. We say there is no descent when $F = K$.

### 1.2 Results
**Theorem A** ($m = 4$, reflection case). Assume (H1)–(H3) with $m = 4$ and that $G''$ contains a pseudo-reflection. Then $\gamma = \gamma' = 0$, $K$ is $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$, and $(G'', U)$ with its local data is one of the following. This is a list of necessary possibilities: we do not claim that every listed case is realized by a family with the required period dimension.
- (i) $W(E_8)\cdot\mu_k$, $k \in \{3, 4\}$, $K = \mathbb{Q}(\zeta_k)$: $16$ reflections and $2$ points of rank $4$ ($N' = 18$). The image is at most a hypersurface.
- (ii) $G_{33}$, $K = \mathbb{Q}(\sqrt{-3})$: $18$ reflections. The image is at most a hypersurface.
- (iii) $G_{34}$, $K = \mathbb{Q}(\sqrt{-3})$: $N' \in \{18, 19, 20\}$.

Case (i) with $k = 4$ is the shape used in [4]. Case (iii) is the group that [5] showed to be unique at $m = 4$ among imprimitive and real reflection groups realizable over $K$.

**Theorem B** ($m = 4$, reflection-free). If $G''$ contains no pseudo-reflection, then $u' = \dim U \geq 23$. For $m = 3$ with $F = K$ not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$, a reflection-free source has $u' \geq 14$ (Propositions 5.1 and 5.2).

**Theorem C** ($m = 3$, reflection case, no descent). Assume (H1)–(H3) with $m = 3$, that $G''$ contains a pseudo-reflection, and $F = K$. If $K$ is not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$, then either $G'' = G_{24}$ and $K = \mathbb{Q}(\sqrt{-7})$, or $G'' = G_F$ and $K = \mathbb{Q}(\sqrt{-2})$. In both cases every balanced family in every genus has split discriminant.

**Proposition D** (descent through a Galois cover). In the situation of Theorem C with $F \neq K$, suppose that the intermediate cover $B' \to B$ is Galois and that $(G'', U)$ is not a twisted deleted permutation module $S_{n+1}\cdot Z$ on $D \otimes L$. Then (H3) fails. (For twisted deleted modules with $F = \mathbb{Q}(\zeta_k)$ and $\varphi(k) \geq 4$, the counts of Section 7 do not close. This case is open.)

### 1.3 Bearing on the Hodge conjecture
The open core of the Hodge conjecture for abelian sixfolds is the nonsplit Weil sixfolds with $K$ not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$. Markman settled the split case [6]. [7, Thm A] covers every Eisenstein ($K = \mathbb{Q}(\sqrt{-3})$) discriminant and period, and [4, Thm A] every Gaussian ($K = \mathbb{Q}(i)$) one. [8] treats signature $(n-1, 1)$ with $n \leq 5$ and is not needed for the balanced sixfold statement.
- Theorems A and C and Proposition D show that, when the monodromy contains reflections, the cover constructions behind those results cannot reach the open core. The exceptions are the descent cases left open in Proposition D (non-Galois intermediate covers and twisted deleted modules). The only new fields that occur without descent are universally split.
- The two theorems play different roles.
  - A source with $m = 4$ is useful at any discriminant. The transfer of [4] completes by a Weil surface, so it reaches targets of signature $(3,3)$ and every discriminant. This is why Theorem A needs no splitness statement. The local factors of the [4] shape (sixteen reflections and two rank-$4$ involutions $i\cdot w$) are all norms by `certs/e8q.out`, so by [5, Thm 2.2] that source is itself split. Its reach to nonsplit targets comes from the completion step.
  - A source with $m = 3$ is used directly, so there only nonsplit families matter. Theorem C shows that none exist over new fields in the reflection case.
- The remaining doors are explicit:
  - reflection-free primitive groups of degree $\geq 23$ ($m = 4$) or $\geq 14$ ($m = 3$);
  - field descent through a non-Galois intermediate cover, or through twisted deleted permutation modules;
  - mechanisms that do not need a source at all, such as transfer from a positive-dimensional locus by deformation of sheaves.
- We prove no new case of the Hodge conjecture. The results are obstructions. They are stated for the class of sources that the recent literature actually uses.

### 1.4 Relation to earlier work
- Schoen [9, §3] gave the count for monomial characters, which is our case $u' = 1$.
- [5] proved:
  - the local-factor formula for the discriminant [5, Thms 2.1–2.3], which we use as a black box for $G_F$ and $U_5(2).2$;
  - the dichotomy for $G_{24}$, $G_{29}$ and $G_{31}$;
  - period-image bounds ($3m$ for imprimitive groups, $m(m+1)/2$ for real reflection groups realizable over $K$) that make $G_{34}$ unique at $m = 4$ within those classes.

  [5] also used $G_{24}$ over $\mathbb{Q}(\sqrt{-7})$ for signatures $(2,1)$, $(3,1)$ and $(3,2)$. Theorem A extends the $m = 4$ uniqueness to all primitive reflection groups, including scalar twists and hypersurface images. Theorem C shows that at $m = 3$ the field $\mathbb{Q}(\sqrt{-7})$ arises only from $G_{24}$ and only with split discriminant.
- [10] gives a dominant nonsplit family over $\mathbb{Q}(i)$ with group $\langle W(E_8), iI\rangle$. This is a direct $m = 3$ source over an old field, so it lies outside Theorem C.
- Normalizers of reflection groups are taken from Marin–Michel [3, §3], who cite Broué–Malle–Michel [11].
- The reflection-free bound uses Guralnick–Tiep [12, Cor. 1.6].
- New here: the twisted classification (Theorem A), the group $G_F$ and its splitness, the reflection-free bound, and the descent lemma.

## 2. Budget and reduction to a primitive pair
Notation: $V^{\circ}$ is the local system on $B^{\circ} = B \setminus \{p_1, \ldots, p_N\}$ with monodromy $\rho\colon \pi_1(B^{\circ}) \to G \to \mathrm{GL}(V)$, with $V^G = 0$. Write $g_i$ for the local monodromies, $r_i = \operatorname{rk}(g_i - 1)$, and $h(V) = \dim H^1_{\mathrm{par}}(B^{\circ}, V)$. The variation $H^1_{\mathrm{par}}(B^{\circ}, V)$ depends only on the local system, and moving a point with trivial monodromy in $\mathrm{GL}(V)$ does not change it. So we replace $G$ by its image in $\mathrm{GL}(V)$ and delete such points. Then every branch point has $r_i \geq 1$.

**Lemma 2.1** (budget). $h(V) = (2\gamma - 2)u + \sum_i r_i$, and the period image has dimension $\leq 3\gamma - 3 + N$.

*Proof.* $\chi_c(B^{\circ}, V) = (2 - 2\gamma - N)u$, and $H^0 = H^2_c = 0$. $H^1_{\mathrm{par}}$ is the image of $H^1_c \to H^1$, of dimension $-\chi_c - \sum_i \dim V^{g_i}$. The period map factors through the Hurwitz space, which is quasi-finite over $\mathcal{M}_{\gamma,N}$. $\square$

**Corollary 2.2.** Assume (H3), i.e. image $\geq m^2 - 1$, with $m \geq 3$.
- (a) If $u \geq 2$ then $\gamma = 0$. Indeed, suppose $\gamma \geq 1$. Then $2m = (2\gamma - 2)u + \sum_i r_i$ with $\sum_i r_i \geq N$ and $u \geq 2$ gives $N \leq 2m - 2(\gamma - 1)\cdot 2$, so the image has dimension $\leq 3\gamma - 3 + N \leq 2m + 1 - \gamma < m^2 - 1$, contradicting (H3).
- (b) If $u = 1$ and $\gamma \geq 1$, then $N = 2m + 2 - 2\gamma \geq 0$ and the dimension is $2m + \gamma - 1$. So $m = 3$ and $(\gamma, N)$ is $(4, 0)$ (dominance possible) or $(3, 2)$ (hypersurface only). At $m = 4$ there is no solution.
- (c) If $\gamma = 0$ then $N \geq m^2 + 2$ and $\sum_i r_i = 2m + 2u$.

*Convention.* We use the multiplicity spaces $\operatorname{Hom}_G(V, H^1(C))$ and $\operatorname{Hom}_H(U, H^1(C))$; the local system attached to $V$ is then $V^{\vee}$. Frobenius reciprocity identifies these spaces exactly, so the choice between $V$ and $V^{\vee}$ only changes notation.

**Lemma 2.3** (Shapiro reduction). Suppose $V = \operatorname{Ind}_H^G U$ with $[G:H] = s \geq 2$. Let $B' = C/H$.
- Then $H^1_{\mathrm{par}}(B^{\circ}, V) = H^1_{\mathrm{par}}(B'^{\circ}, U)$ as variations of Hodge structure.
- The period map factors through the Hurwitz space of $(B', U)$.
- Iterating, we reach a primitive pair $(G'', U)$, where $G''$ is the image of the final $H$ in $\mathrm{GL}(U)$, and $\mathbb{Q}(\chi_V)$ is contained in $F := \mathbb{Q}(\chi_U)$.
- Corollary 2.2 applies to $(B', U)$, so $\gamma' = 0$ when $u' \geq 2$. The case $u' = 1$ is Schoen's count [9, §3]: it forces $m = 3$ and $(\gamma', N') \in \{(4, 0), (3, 2)\}$, with $F = \mathbb{Q}(\zeta_k)$. Without descent, $K = \mathbb{Q}(\zeta_k)$ is $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$. With descent ($\varphi(k) \geq 4$) this is an unramified or $2$-point cyclic Prym family with a Galois-twisting symmetry; see Section 7.

*Proof.* Pushforward along $B'^{\circ} \to B^{\circ}$ commutes with $j_*$, so it identifies the parabolic cohomologies (Frobenius reciprocity for local systems). $\square$

## 3. The reflection case
Assume $G''$ contains a pseudo-reflection, and let $R$ be the normal subgroup generated by the pseudo-reflections of $G''$. Throughout this section $u' \geq 3$. This holds in every application. The case $u' = 1$ is Schoen's (Lemma 2.3). For $u' \geq 2$, Corollary 2.2(a) gives $\gamma' = 0$, and then Corollary 2.2(c) gives $m^2 + 2 \leq N' \leq \sum_i r_i = 2m + 2u'$, so $u' \geq 3$ for $m = 3$ and $u' \geq 5$ for $m = 4$. It excludes the rank-$2$ groups $G_5$, $G_7$ and $G(4,2,2)$, whose normalizers behave differently.

**Lemma 3.1.** $U|_R$ is irreducible, and $R$ is an irreducible primitive reflection group of rank $u'$, except in the cases $R = W(D_4)$ and $R = G(3,3,3)$, which occur only for $u' = 4$ and $u' = 3$.

*Proof.*
- Clifford: $U|_R$ is homogeneous, since otherwise $U$ is induced from an inertia group, contradicting primitivity. A pseudo-reflection has rank $1$, so the multiplicity is $1$.
- If $R = G(a, b, u')$ is imprimitive, $G''$ normalizes $R$. By [3, §3] (see [11, 3.13]), the outer automorphisms induced by $N_{\mathrm{GL}(U)}(G(a,b,u'))$ come from the monomial overgroup $G(a,1,u')$, except for $G(2,2,4) = W(D_4)$, normal in $W(F_4)$ (outer part $S_3$); $G(3,3,3)$, normal in $G_{26}$ (outer part $A_4$); and $G(4,2,2)$ (rank $2$). Since $R$ is irreducible, its centralizer in $\mathrm{GL}(U)$ is $\mathbb{C}^{\times}$ (Schur), so the normalizer is determined by these outer automorphisms: it is monomial in all other cases, and equals $W(F_4)\cdot\mathbb{C}^{\times}$ or $G_{26}\cdot\mathbb{C}^{\times}$ in the two exceptions. A monomial $G''$ contradicts primitivity. $\square$

**Lemma 3.2** (normalizers). If $R$ is primitive and not $W(F_4)$, then $N_{\mathrm{GL}(U)}(R) = R\cdot\mathbb{C}^{\times}$. So $G'' = R\cdot Z$ with $Z = G'' \cap \mathbb{C}^{\times}$, and $U = U_R \otimes L$ for a character $L$ of $Z$.

*Proof.*
- Conjugation identifies $N/(R\cdot\mathbb{C}^{\times})$ with $\operatorname{Out}_{\chi}(R)$, the outer automorphisms fixing $\chi_{U_R}$ (Schur's lemma). For exceptional $R$, [3, §6] shows that the image of $N$ in $\operatorname{Out}(R)$ is nontrivial only for $G_5$, $G_7$ and $G_{28} = W(F_4)$. For symmetric groups, $\operatorname{Out}(S_6)$ moves the deleted character.
- Independent checks (certificates in `certs/`):
  - $W(E_6)$, $W(E_7)$ and $W(E_8)$: explicit outer automorphism groups.
  - $G_{33} = \langle -1\rangle \times U_4(2)$: CTblLib table automorphisms.
  - $G_{34} = 6_1.U_4(3).2_2$: $|\operatorname{Out}| \leq 4$. The central automorphism sends $\chi$ to $\chi \otimes \det$. A lift of $2_1$ inverts the order-$3$ part of the centre (CTblLib: $|Z(6_1.U_4(3).2_1)| = 2$).
- $G'' = R\cdot Z$ because $rz \in G''$ and $r \in R \subset G''$ imply $z \in G''$. $\square$

*Field of a twist.* $Z(R) = R \cap \mathbb{C}^{\times}$ by Schur's lemma, and $Z \subset G''$. Since $\chi_U(z) = u' \cdot L(z)$, the field $F$ contains $\mathbb{Q}(L(Z)) = \mathbb{Q}(\zeta_k)$, where $k = |Z|$. If $Z \subset \mu_2\cdot Z(R)$ then $G'' \subset R \times \{\pm 1\}$, so $F = \mathbb{Q}(\chi_R)$; we call this the untwisted case.

**Lemma 3.3** (twist budget). Suppose $Z$ is not contained in $\mu_2\cdot Z(R)$. Call a branch point an $L$-point if its monodromy is $rz$ with $z \notin \mu_2\cdot Z(R)$; this does not depend on the factorization. Write $n_L$ for their number.
- $n_L \geq 2$. The map $G'' \to Z/(Z \cap \mu_2\cdot Z(R))$ is a homomorphism, nontrivial because $G''$ is generated by the local monodromies. It kills the other points, and the product of all local monodromies is $1$.
- An $L$-point has rank $\geq \max(2, u' - \mu(R))$, where $\mu(R)$ is the largest multiplicity in an element of $R$ of an eigenvalue outside $\mu_2\cdot Z(R)$. Rank $1$ is impossible: $rz$ would be a pseudo-reflection, hence in $R$, hence $z \in Z(R)$.
- By Springer's theorem [13] the largest dimension of a primitive $\zeta_k$-eigenspace in $R$ is $a(k) = \#\{i : k \mid d_i\}$, where $d_i$ are the degrees. The proofs below do not depend on the general theorem: every value of $a(k)$ or $\mu(R)$ we use is computed directly from the classes of $R$ (Table 4.1).
- With $\gamma' = 0$: $2(u' - \mu) + (N' - 2) \leq 2m + 2u'$, so $N' \leq 2m + 2 + 2\mu$.

**Lemma 3.4** (twisted deleted modules). Let $G'' \subset S_{n+1} \times \mathbb{C}^{\times}$ with $n \geq 5$, and $U = D \otimes L$, where $D$ is the deleted permutation module and $L$, the projection to $\mathbb{C}^{\times}$, is nontrivial. Assume (H1)–(H3). Then $m \neq 4$. $L$-points are the points with $L(g_i) \neq 1$.

*Proof.*
- Shapiro along the permutation curve $\pi''\colon C'' \to B'$ (degree $n+1$, connected): $h(D \otimes L) = h(C'', \pi''^*L) - h(B', L)$, and $\pi''^*L$ is nontrivial. Indeed, if $L$ were trivial on a point stabilizer, then by Frobenius reciprocity $L^{-1}$ would occur in the permutation module $1 + D$. Since $L$ is nontrivial, $L^{-1}$ would occur in $D$, so $D \otimes L$ would contain the trivial character, contradicting the irreducibility of $U$ ($\dim U = n \geq 5$).
- The period map factors through $\mathcal{M}_{g'',n''}$, where $n''$ is the number of ramification points of $\pi''^*L$. With $2g'' - 2 + n'' = 2m + n_L - 2$ this gives image $\leq 3m - 3 + (3n_L - n'')/2$. At $m = 4$, (H3) needs $n_L \geq 4$.
- An $L$-point $\sigma\cdot\zeta$ has rank $\geq n - \lfloor (n+1)/2 \rfloor$, because the multiplicity of $\zeta^{-1}$ is the number of cycles of length divisible by $\operatorname{ord}(\zeta)$. With $N' \geq 18$ the budget gives $n_L \cdot (\lceil (n-1)/2 \rceil - 1) \leq 2n - 10$, so $n_L \leq 3$. $\square$

**Lemma 3.5** (scalar descent). Let $M \subset \mathrm{GL}(U)$ be finite, and let $G'' \subset M\cdot\mathbb{C}^{\times}$ be finite and primitive. For $g = mz \in G''$ write $\psi(g)$ for the class of $z$ in $\mathbb{C}^{\times}/(M \cap \mathbb{C}^{\times})$; $\psi$ is a homomorphism. Then $\psi(G'')$ is generated by the classes $\psi(g)$ of the elements $g$ with $\chi_U(g) \neq 0$.

*Proof.* Let $G''_1$ be the preimage of the subgroup generated by these classes. It is normal with cyclic quotient, and $\chi_U$ vanishes off $G''_1$. Hence $\langle \chi|_{G''_1}, \chi|_{G''_1}\rangle = [G'' : G''_1]$. Characters of a normal subgroup with cyclic quotient extend to their inertia groups, so $\chi|_{G''_1}$ is a sum of $[G'':G''_1]$ distinct conjugates and $\chi_U$ is induced from $G''_1$. Primitivity gives $G''_1 = G''$. $\square$

*Use.* Suppose $\chi_M$ has values in $E$ and $F = K$. For $g = mz \in G''$, the elements $g$ and $m$ have finite order and $z$ is central, so $z$ is a root of unity. If $\chi_U(g) \neq 0$, then $z = \chi_U(g)/\chi_M(m)$ lies in $\mu(EK)$. By the lemma, the classes $\psi(g)$ of such elements generate $\psi(G'')$, and every element of $\ker(\psi)$ lies in $M$. Hence $G'' \subset M\cdot\mu(EK)$.

## 4. Proof of Theorem A
Let $m = 4$.
- By Corollary 2.2 and Lemma 2.3, $\gamma' = 0$, $N' \geq 18$ and $\sum r(U) = 8 + 2u'$. Each $r \geq 1$, so $u' \geq 5$. Hence by Lemma 3.1 $R$ is primitive of rank $\geq 5$: $S_{u'+1}$, $G_{33}$ ($u' = 5$), $G_{34}$ ($u' = 6$), $W(E_6)$, $W(E_7)$ or $W(E_8)$ [14].
- By Lemma 3.2, $G'' = R\cdot Z$.
- Untwisted case ($Z$ inside $\mu_2\cdot Z(R)$). Then $F = \mathbb{Q}(\chi_R)$ is $\mathbb{Q}$ for $S_n$ and the Weyl groups, so these are excluded. $G_{33}$ and $G_{34}$ contain $-1$, so $G'' = R$ and $F = K = \mathbb{Q}(\sqrt{-3})$.
  - For $G_{33}$, $\sum r = 18$ and $N' \geq 18$ force $18$ reflections and image $\leq 15$.
  - For $G_{34}$, $\sum r = 20$, so $N' \leq 20$.
- Twisted case. Lemma 3.3 needs $\mu(R) \geq 4$.
  - Springer gives $\mu = 4$ only for $W(E_8)$ at $k \in \{3, 4, 6\}$. For $E_6$ and $E_7$, $\mu = 3$ (for $E_6$ the eigenvalue $-1$ has multiplicity $a(2) = 4$, but it lies in $\mu_2$ and is excluded by the definition of $\mu$). For $G_{34}$, $\mu = 2$ (eigenvalues outside $\mu_6$). For $G_{33} = \langle -1\rangle \times U_4(2)$, $\mu = 3$ (Table 4.1).
  - Lemma 3.4 removes $S_{u'+1}$.
  - For $W(E_8)\cdot\mu_k$: $\sum r = 24$ and $N' \geq 18$ leave an excess $\sum_i (r_i - 1) \leq 6$. Each $L$-point has rank $\geq 4$, so there are exactly $2$ $L$-points, both of rank $4$, and $16$ reflections; $N' = 18$ and the image is $\leq 15$. Their scalars satisfy $z_1 z_2 \in \{\pm 1\}$ and have order $3$, $4$ or $6$ (other orders give $a(k) \leq 2$). Hence $Z = \mu_k\cdot\{\pm 1\}$ with $k \in \{3, 4\}$.
  - $F = \mathbb{Q}(\zeta_k)$ is quadratic, so $K = F$. $\square$

**Table 4.1** (eigenvalue multiplicities; `certs/weyl_eig.out`, `certs/g34.out`, `certs/g33.out`). For $E_8$, $a(k) = 4$ at $k = 3, 4, 6$ and $a(k) = 2$ at $k = 5, 8, 10, 12$. For $E_7$, $3$ at $k = 3, 6$ and $2$ at $k = 4$. For $E_6$, $3$ at $k = 3$ and $2$ at $k = 4, 6$. For $G_{34}$, the largest multiplicity of an eigenvalue outside $\mu_6$ is $2$. For $G_{33}$, the largest multiplicity of an eigenvalue outside $\{\pm 1\}$ is $3$, attained by an element of order $3$ (computed on $U_4(2)$ with its $5$-dimensional character, since $-1$ negates every eigenvalue).

## 5. Proof of Theorem B
Assume $G''$ has no pseudo-reflection. Then every $r_i \geq 2$, and the budget gives $2N' \leq 8 + 2u'$, so $u' \geq 14$. The number $N_2$ of rank-$2$ points satisfies $N_2 \geq 3N' - (8 + 2u') \geq 46 - 2u'$. So for $u' \leq 22$ there is a noncentral $g \in G''$ with $\operatorname{rk}(g - 1) = 2$.
We use the following notions from [12, Def. 2.1 and §2]. If $g$ has finite order and eigenvalues $e^{2\pi i a_1}, \ldots, e^{2\pi i a_n}$ with $0 \leq a_j < 1$, then $\operatorname{age}(g) = \sum_j a_j$, and $\operatorname{age}^*(g) = \inf_{\lambda \in S^1} \operatorname{age}(\lambda g)$. An element is *junior* if $0 < \operatorname{age}(g) \leq 1$. If $g$ has rank $2$ with nontrivial exponents $a, b$, then $g^{-1}$ has nontrivial exponents $1 - a, 1 - b$, so $\operatorname{age}(g) + \operatorname{age}(g^{-1}) = 2$.
- Tensor-indecomposable $G''$. $\operatorname{age}(g) + \operatorname{age}(g^{-1}) = 2$, so $g$ or $g^{-1}$ is a noncentral junior element. By Reid–Tai, $\mathbb{C}^{u'}/G''$ is not terminal.

  Guralnick–Tiep [12, Cor. 1.6] applies to finite irreducible, primitive, tensor-indecomposable $G''$ with $u' \geq 11$ and non-terminal quotient. Its alternative (ii) says all junior elements are central, which $g$ or $g^{-1}$ contradicts. So (i) holds: $Z \times A_{u'+1} \leq G'' \leq (Z \times A_{u'+1})\cdot 2$ on the deleted module. Then $G'' \subset S_{u'+1} \times \mathbb{C}^{\times}$. If $L$ is trivial, $G'' = A_{u'+1}$ (no transpositions) and $F = \mathbb{Q}$. Otherwise Lemma 3.4 applies.
- Tensor-decomposable $G''$, $U = A \otimes B$ with $2 \leq p = \dim A \leq q$.
  - A rank-$2$ element $a \otimes b$ has $a$ scalar, $p = 2$, and $b$ a pseudo-reflection on $B$. If $a$ is non-scalar the rank is $\geq q$.
  - At least two branch points have non-scalar $A$-part, each of rank $\geq q = u'/2$. So $2N' \leq 2u' + 8 - 2(u'/2 - 2)$, i.e. $N' \leq u'/2 + 6 < 18$.
- Tensor-induced $G''$ ($U = A^{\otimes t}$, $t \geq 2$). GT's notion of tensor indecomposability allows this case, so Cor. 1.6 already covers it. A direct check: $14 \leq p^t \leq 22$ forces $u' = 16$ with $(p, t) = (2, 4)$ or $(4, 2)$. Factor-preserving non-scalar elements have rank $\geq p^{t-1} \geq 4$. For a factor-permuting element, the fixed space has dimension at most the number of orbits of the permutation on basis tensors, which gives rank $\geq 4$ in both cases (a transposition gives rank $\geq p^{t-2}\cdot p(p-1)/2$). So there are no rank-$2$ elements.

Hence $u' \geq 23$. $\square$

**Proposition 5.1** ($m = 3$, reflection-free). Assume (H1)–(H3) with $m = 3$, $F = K$, and $K$ not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$. If $G''$ contains no pseudo-reflection, then $u'$ is $8$, $9$ or $10$, or $u' \geq 14$.

*Proof.* The budget gives $2N' \leq 6 + 2u'$ with $N' \geq 11$, so $u' \geq 8$. Let $11 \leq u' \leq 13$. Then $N_2 \geq 3N' - (6 + 2u') \geq 27 - 2u' \geq 1$, so $G''$ has a noncentral rank-$2$ element $g$.
- Tensor-indecomposable (in GT's sense, which includes tensor-induced). As in Theorem B, [12, Cor. 1.6] gives $G'' \subset S_{u'+1} \times \mathbb{C}^{\times}$ on the deleted module ($N_{\mathrm{GL}}(A_{u'+1}) = S_{u'+1}\cdot\mathbb{C}^{\times}$ since $u'+1 \neq 6$). Lemma 3.5 with $M = S_{u'+1}$ and $E = \mathbb{Q}$ gives $G'' \subset S_{u'+1} \times \mu(K) = S_{u'+1} \times \{\pm 1\}$, so $F = \mathbb{Q}$. Contradiction.
- Tensor-decomposable, $U = A \otimes B$. The rank-$2$ element forces $\dim A = 2$, so $u' = 12$ and $\dim B = 6$. The image of $G''$ in $\mathrm{PGL}(A)$ is generated by the $A$-parts of the local monodromies. If at most two of them were non-scalar, their product relation would make that image cyclic, and a cyclic subgroup of $\mathrm{PGL}_2$ lifts to an abelian group, so $A$ would be reducible, which contradicts [12, Lemma 2.24]. So at least three points have non-scalar $A$-part, each of rank $\geq 6$. Then $18 + 2(N' - 3) \leq 30$, so $N' \leq 9 < 11$. $\square$

**Proposition 5.2** ($m = 3$, small degree). In the situation of Proposition 5.1, $u'$ is not $8$, $9$ or $10$. So $u' \geq 14$.

*Proof sketch* (full details in the supplement, `prop52_details.md`). A rank-$2$ element exists ($N_2 \geq 27 - 2u' \geq 7$), so $g$ or $g^{-1}$ has $\operatorname{age}^* \leq 1$. If $G''$ is tensor-decomposable or tensor-induced, we treat it directly below. Otherwise $G''$ satisfies hypothesis (S) of [15] (irreducible, primitive, tensor-indecomposable, not tensor-induced). Then [15, Prop 2.8] says that, after normalizing scalars, $G''$ is almost quasi-simple or lies in the normalizer of an extraspecial group $E$ with $u' = \sqrt{|E/Z(E)|}$. This step needs no age or generation hypothesis. In the almost quasi-simple case, [12, Thm 3.8 and Table I] applies, because $G''$ has a noncentral element with $0 < \operatorname{age}^* \leq 1$.

For $u' = 8$ the budget is $\sum r = 6 + 16 = 22$, with $N' \geq 11$ and every $r_i \geq 2$. So $N' = 11$ and every local monodromy is a bireflection, which means $G''$ is generated by bireflections. The tensor-induced and extraspecial cases at $u' = 8$ use exactly this.
- Tensor-decomposable: excluded by the three-point count ($N' \leq 8$).
- Tensor-induced $3^2$: no rank-$2$ elements.
- Tensor-induced $2^3$: every rank-$2$ element is conjugate to $\mathrm{swap}_{12} \otimes 1$, so $G'' \subset \mathrm{SL}_2^{\otimes 3} \rtimes S_3$ (the scalars of the conjugator cancel). Every finite-order element of this group has real trace: the trace is $\operatorname{tr}(x_1)\operatorname{tr}(x_2)\operatorname{tr}(x_3)$, $\operatorname{tr}(ab)\operatorname{tr}(c)$ or $\operatorname{tr}(abc)$, and the $\mathrm{SL}_2$ cycle products involved have finite order, since a power of each is $\pm I$. This contradicts $F \supseteq K$.
- Extraspecial $2^{1+6}$ ($E = C_4 * 2^{1+6}_+$, $N = Z\cdot E\cdot \mathrm{Sp}_6(2)$).
  - By [12, §5.2, $d = 8$], $N/Z(N)$ has exactly three classes with $\operatorname{age}^* = 1$, with spectra (b1) $(-1,-1,1^6)$ and (c6) $(i^4, 1^4)$ of [12, Remark 3.9]. Every other noncentral element has $\operatorname{age}^* > 1$.
  - A rank-$2$ element $g$ has $\operatorname{age}(g) + \operatorname{age}(g^{-1}) = 2$, so $g$ or $g^{-1}$ has $\operatorname{age}^* \leq 1$. Both are rank-$2$ elements, and the conclusion below is invariant under inversion, so we may assume $\operatorname{age}^*(g) \leq 1$. Every scalar multiple of a (c6) element has eigenvalue multiplicities $4 + 4$, so $g$ is a scalar multiple of a (b1) element. Rank $2$ forces $g$ itself to have spectrum $(-1,-1,1^6)$.
  - Write $g = z\cdot c$ with $c$ in the $3$-qubit Clifford group $\mathcal{C}$ and $z$ scalar. Since $g$ and $c$ have finite order and $z$ commutes with $c$, $z$ is a root of unity. Then $z = 4/\operatorname{tr}(c)$ lies in $\mathbb{Q}(\zeta_8)$, so $z \in \mu(\mathbb{Q}(\zeta_8)) = \mu_8 \subset \mathcal{C}$, and $g \in \mathcal{C}$.
  - The trace-$4$ involutions of $\mathcal{C}$ form one class of $1260$, containing $CZ \otimes I$. They generate a subgroup $J$ of index $2$ with character field $\mathbb{Q}(i)$ (`certs/cliff2.out`).
  - For $u' = 8$, $G''$ is generated by bireflections, so $G'' \subset J$ and $F \subseteq \mathbb{Q}(i)$.
- Extraspecial $3^{1+4}$: the normalizer has field $\mathbb{Q}(\zeta_3)$, and Lemma 3.5 gives $F \subseteq \mathbb{Q}(\sqrt{-3})$ (`certs/qutrit.out`).
- Almost quasi-simple: [12, Table I] leaves $2.\Omega^+_8(2)$, $A_{u'+1}$ and $\mathrm{SU}_5(2)$.
  - The first two have rational normalizer characters, so Lemma 3.5 gives $F = \mathbb{Q}$.
  - For $\mathrm{SU}_5(2)$ the $10$-dimensional character is rational on $U_5(2)$. Its extension to $U_5(2).2$ has field $\mathbb{Q}(\sqrt{-2})$, but the outer classes have rank $\geq 5$ for either sign. $F = \mathbb{Q}(\sqrt{-2})$ needs at least two outer points, so $\sum r \geq 10 + 2\cdot 9 = 28 > 26$ (`certs/u52c.out`). $\square$

*Notation from [5, §2].* Let $(U, h)$ be positive-definite Hermitian over $K$, and let $g$ be a unitary element of finite order with $\det_K(g) = \pm 1$. This holds for every element of $W(E_8)\cdot\mu_4$, $U_5(2).2$ and $G_F$, the groups to which we apply it. Let $V_g = \operatorname{im}(g - 1)$ and $k(g) = \dim_K V_g$, and let $\Theta(g) = \det_K(h|_{V_g}) / \det_K((g - 1)|_{V_g})$, a class modulo $N(K^{\times})$. If $e^{2\pi i\theta_1}, \ldots, e^{2\pi i\theta_k}$ ($0 < \theta_a < 1$) are the eigenvalues of $g$ on $V_g$, then $\delta(g) = 2\sum_a \theta_a - k(g)$ is an integer, and [5, Thm 2.2(2)] gives a unique class $q(g) \in \mathbb{Q}_{>0}^{\times}/N(K^{\times})$ with $(-1)^{k(g)}\Theta(g) \equiv (-\eta_K)^{\delta(g)} q(g)$, where $\eta_K = i\sqrt{d_K}$. For a family with branch classes $C_j$, the discriminant $(-1)^m \det_K(H_{\mathrm{par}})$ is congruent to $\prod_j \Theta(C_j)$ modulo norms [5, Thm 2.1(2)]. On a balanced family $\sum_j \delta(C_j) = 0$ and $\sum_j k(C_j)$ is even [5, Thm 2.2(3)], so the discriminant is $\prod_j q(C_j)$ modulo norms. A group is *universally split* if this product is a norm for every balanced family in every genus.

**Remark 5.3** (the near miss is split). Even without the budget, $U_5(2).2$ gives no nonsplit balanced family over $\mathbb{Q}(\sqrt{-2})$, in any genus.
- Setup. We realized the $10$-dimensional representation over $\mathbb{Q}(\sqrt{-2})$ (Dixon's algorithm; a homomorphism check is in `certs/u52chk.out`) and solved for its invariant Hermitian form. The form is unique up to a rational scalar, and it is positive definite after normalizing its first diagonal entry to $1$, because the average of $g^*g$ over $G$ is a positive definite invariant form.
- Local factors (`certs/u52q2.out`, classified exactly by `certs/u52norm.py`; $U_5(2).2$ has $30$ inner and $13$ outer classes). All $29$ nontrivial inner classes and the $2$ outer classes with $k(C) = 10$ have norm $q$. The $11$ outer classes with odd $k(C)$ all have $q \equiv 13 \bmod N(K^{\times})$, and $13$ is inert in $\mathbb{Q}(\sqrt{-2})$. Rescaling the form changes this class, because $q(C)$ scales by $c^{k(C)}$.
- Parity. $\det_K$ is $-1$ exactly on the outer coset, so $k(C) \equiv [C]_{\mathrm{ab}} + \delta(C) \bmod 2$. On every balanced tuple, $\sum \delta = 0$ and the outer points have even total count. So the number of odd-$k$ points is even, and the product of the local factors is a norm.
- Conclusion. By [5, Thm 2.2] every such family is split.

## 6. $m = 3$: proof of Theorem C
Here $\gamma' = 0$ (or the rank-one cases of Corollary 2.2(b), which give $F = \mathbb{Q}(\zeta_k)$). $\sum r(U) = 6 + 2u'$ and $N' \geq 11$. The twist budget gives $N' \leq 8 + 2\mu$, so $\mu \geq 2$, and twisted $R$ has $u' \geq 4$. Assume $F = K$.
- Rank $\geq 5$, and $W(A_4) = S_5$ at rank $4$. By Lemma 3.2, $G'' = R\cdot Z$ and $F = \mathbb{Q}(\chi_R, \zeta_k)$ with $k = |Z|$. ($F$ contains $\chi_U(r) = \chi_R(r)$ and $\chi_U(z) = u' \cdot L(z)$.) Here $\mathbb{Q}(\chi_R)$ is $\mathbb{Q}$ or $\mathbb{Q}(\sqrt{-3})$. If it is $\mathbb{Q}(\sqrt{-3})$, then $K = F = \mathbb{Q}(\sqrt{-3})$. If it is $\mathbb{Q}$, then $K = \mathbb{Q}(\zeta_k)$ is imaginary quadratic, so $k$ is $3$, $4$ or $6$.
- Rank $3$ and $4$, primitive, not $F_4$. Lemma 3.2 applies, and $F \supseteq \mathbb{Q}(\chi_R)$.
  - $G_{23}$ and $G_{30}$ (field $\mathbb{Q}(\sqrt{5})$) and $G_{27}$ ($\mathbb{Q}(\sqrt{-3}, \sqrt{5})$) have $F \neq K$.
  - $G_{25}$, $G_{26}$, $G_{29}$, $G_{31}$ and $G_{32}$ have $\mathbb{Q}(\chi_R)$ equal to $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$, so $K = F = \mathbb{Q}(\chi_R)$.
  - $G_{24}$ has $\mathbb{Q}(\chi_R) = \mathbb{Q}(\sqrt{-7})$. $F = K$ forces $\zeta_k \in \mu(\mathbb{Q}(\sqrt{-7})) = \{\pm 1\} \subset G_{24}$, so $G'' = G_{24}$.
- Imprimitive $R$. By [3, §3, table and comments], $N_{\mathrm{GL}(U)}(W(D_4)) = W(F_4)\cdot\mathbb{C}^{\times}$ and $N_{\mathrm{GL}(U)}(G(3,3,3)) = G_{26}\cdot\mathbb{C}^{\times}$. ($W(A_3) = G(2,2,3)$ has monomial normalizer $W(B_3)\cdot\mathbb{C}^{\times}$ and is excluded by Lemma 3.1.) Apply Lemma 3.5 with $M = W(F_4)$, $E = \mathbb{Q}$, or $M = G_{26}$, $E = \mathbb{Q}(\sqrt{-3})$. Suppose $K$ is not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$. Then $\mu(EK)$ is $\{\pm 1\}$ or $\mu_6$, so $G'' \subset W(F_4)$ or $G'' \subset G_{26}$, and $F$ is $\mathbb{Q}$ or $\mathbb{Q}(\sqrt{-3})$, not $K$.
- $R = W(F_4)$. $N_{\mathrm{GL}(U)}(W(F_4)) = M\cdot\mathbb{C}^{\times}$ with $M = \langle W(F_4), \varphi/\sqrt{2}\rangle$, of order $2304$. Here $\varphi$ swaps long and short roots, $\varphi^2 = 2I$ and $\varphi/\sqrt{2}$ is orthogonal. Inner traces are integers and outer traces lie in $\frac{1}{\sqrt{2}}\mathbb{Z}$. Suppose $K$ is not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$, so $\mu(K) = \{\pm 1\}$, and apply Lemma 3.5.
  - An inner element $wz$ with nonzero trace has $z \in \mu(K) = \{\pm 1\}$.
  - An outer element $w(\varphi/\sqrt{2})z$ with nonzero trace has $z/\sqrt{2} \in K$. Then $z^2$ lies in $2K^2 \subset K$, so $z^2 = \pm 1$, and $z = \pm i$ with $i/\sqrt{2} = \sqrt{-2}/2 \in K$. This forces $K = \mathbb{Q}(\sqrt{-2})$.
  - So $G'' \subset M\cdot\mu_4$. The groups between $W(F_4)$ and $M\cdot\mu_4$ correspond to the subgroups of $M\cdot\mu_4/W(F_4) \cong C_2 \times C_2$. They are $W(F_4)$, $M$ (real), $W(F_4)\cdot\mu_4$ (field $\mathbb{Q}(i)$), $M\cdot\mu_4$ (field $\mathbb{Q}(i, \sqrt{2})$) and $G_F = \langle W(F_4), i\varphi/\sqrt{2}\rangle$. Only $G_F$ has $F = K = \mathbb{Q}(\sqrt{-2})$.

**Proposition 6.1** ($G_F$). $G_F = \langle W(F_4), \tau = i\varphi/\sqrt{2}\rangle$ has order $2304$ and $\tau^2 = -I$. It lies in $U_4(\mathbb{Q}(\sqrt{-2}))$ with character field $\mathbb{Q}(\sqrt{-2})$. The outer coset contains no pseudo-reflection, and its unique rank-$2$ class is an involution class of size $24$. Generating genus-$0$ tuples $(R^{10}, O, O)$ with product $1$ exist; they have signature $(3,3)$ and a $9$-dimensional Hurwitz space. An explicit tuple, with its product, generation and Hodge numbers verified without search, is in `certs/f4tuple_explicit` (exact; `certs/f4twist` for the group data). A $9$-dimensional Hurwitz space is only the dimension count required by (H3). We do not claim that the period map of these families is dominant, and Theorem C does not need it.

**Proposition 6.2** (universal splitness). For every conjugacy class $C$ of $G_F$, the local factor $q(C)$ of [5, Thm 2.2] lies in $\{2^a 3^b\}$. Since $2 = N(\sqrt{-2})$ and $3 = N(1 + \sqrt{-2})$, every $q(C)$ is a norm. The hypotheses of [5, Thm 2.2(3)] hold. $U$ is positive definite Hermitian ($G_F$ is unitary), $V^{\Pi} = 0$ by irreducibility, and $\det_K = \pm 1$ on generators: $\det W(F_4) = \pm 1$ and $\det(\varphi/\sqrt{2}) = 1$, so $\det\tau = i^4 = 1$. Hence every *balanced* family in $G_F$, in every base genus, has split discriminant; the theorem says nothing about unbalanced parabolic forms. (`certs/f4q.out`: all $28$ nontrivial classes, exact over $\mathbb{Q}(\zeta_8)$.) $G_{24}$ is universally split by [5, Thm 2.3(1)]: its $12$ classes have $q(C) \in \{1, 2, 4, 7, 8\}$, all norms from $\mathbb{Q}(\sqrt{-7})$, in the model $h_V = I_3$. That model covers our $U$. The $3$-dimensional representation is absolutely irreducible with Schur index $1$ over $\mathbb{Q}(\sqrt{-7})$, so $U$ is $K$-isomorphic to it, and the invariant form is unique up to a factor $c \in \mathbb{Q}_{>0}$. That factor multiplies $\det H_{\mathrm{par}}$ by $c^{2m}$, a square. This completes the proof of Theorem C. $\square$

## 7. Descent
**Lemma 7.1.** Assume $F \neq K$. Let $p \in B$ have local monodromy $g$ with $r_p(V) > 0$, and suppose $p$ is unbranched for $B' \to B$, i.e. $g$ lies in $\operatorname{core}_G(H)$ and so fixes *every* coset of $H$. (Being unramified at a single preimage is not enough.) Then $p$ has at least two $U$-branch preimages in $B'$.

*Proof.*
- Let $g \in \operatorname{core}(H)$ be the local monodromy and $S_g = \{xH : g \text{ acts nontrivially on } {}^{x}U\}$. Suppose $S_g = \{H\}$.
- $\operatorname{Res}_H V = U + \sum_{x \notin H} \operatorname{Ind}_{H \cap {}^{x}H}^{H}({}^{x}U)$. On every term except $U$, $g$ acts trivially, because on restriction to $\operatorname{core}(H)$ each term is a sum of ${}^{hx}U$ with $hx \notin H$.
- Choose an automorphism of $\overline{\mathbb{Q}}$ over $K$ that moves a value of $\chi_U$, and extend it to an automorphism $\sigma$ of $\mathbb{C}$. No normality of $F/K$ is needed. Then $\operatorname{Ind} U^{\sigma} = V^{\sigma} = V$. So $U^{\sigma}$ is an $H$-constituent of $\operatorname{Res}_H V$ on which $g$ acts nontrivially. Hence $U^{\sigma} = U$, contradicting $\mathbb{Q}(\chi_U) = F$. $\square$
- Consequence: $N_B \leq b + N'/2$, where $b$ is the number of branch points of $B' \to B$.
- Rank-one $U$ (Corollary 2.2(b), $(\gamma', N') = (4, 0)$ or $(3, 2)$). Here $N' \leq 2$, so $b \geq N_B - 1 \geq 10$. For a Galois cover $B' \to \mathbb{P}^1$ of degree $s$ with $b$ branch points, Riemann–Hurwitz gives $2\gamma' - 2 \geq s(b/2 - 2) \geq 3s$. For $\gamma' = 4$ this allows only $s = 2$, and a hyperelliptic genus-$4$ curve has $b = 10$, so $N_B \leq 10$. For $\gamma' = 3$ it allows no $s \geq 2$. Both contradict $N_B \geq 11$.
- $u' \geq 2$. Then $\gamma' = 0$, the Galois group lies in $\mathrm{PGL}_2$, and $b \leq 3$. With $N_B \geq 11$ this gives $N' \geq 16$, hence $u' \geq 5$ and, if twisted, $\mu \geq 4$. In the reflection case that leaves $W(E_8)\cdot\mu_k$ ($F$ quadratic, so no descent), untwisted groups of rank $\geq 5$ ($F = \mathbb{Q}$ or $\mathbb{Q}(\sqrt{-3})$, no room for descent), and twisted deleted modules $G'' \subset S_{n+1} \times \mu_k$.
- Twisted deleted modules. $F = \mathbb{Q}(\zeta_k)$ contains $K$, so the conductor $f_K$ divides $k$, and $f_K \geq 7$ when $K$ is not $\mathbb{Q}(i)$ or $\mathbb{Q}(\sqrt{-3})$. An $L$-point whose scalar has order $e$ has rank $\geq n - (n+1)/e$. The budget is $\sum_i (r_i - 1) \leq 6 + 2n - 16 = 2n - 10$.
  - $n_L = 3$. The three scalars have product $1$, so each prime-power part of $f_K$ divides at least two of their orders. If some prime power in $f_K$ is $\geq 7$, two $L$-points have order $\geq 7$, and $2(6n - 8)/7 + (n - 3)/2 \leq 2n - 10$ has no solution. Otherwise $f_K$ is $15$ or $20$, and we show $\sum_i 1/e_i \leq 3/5$ for the orders $e_i$. This gives $\sum_i (r_i - 1) \geq 2.4n - 3.6 > 2n - 10$.
    - $f_K = 15$. If only one order is divisible by $15$, the other two are divisible by $3$ and $5$. If two are divisible by $15$ and the third is $2$, the product relation forces one of them to be divisible by $30$. In both cases $\sum_i 1/e_i \leq 3/5$.
    - $f_K = 20$. The worst pattern is two orders divisible by $20$ and a third equal to $2$, which gives exactly $3/5$. If only one order is divisible by $20$, the others are at least $4$ and $5$.
  - $n_L \geq 4$ fails by the count in Lemma 3.4, whose right side is again $2n - 10$.
  - $n_L = 2$. Both scalars have order $k \geq 7$, and $2(6n - 8)/7 \leq 2n - 10$ forces $n \geq 27$.
  - In the Lemma 3.4 count at $m = 3$ with $n_L = 2$, the image has dimension $\leq 9 - n''/2$. So dominance needs $n'' = 0$ and $g'' = 4$: the Weil part is the $L$-part of an unramified cyclic cover of a genus-$4$ curve (a cyclic Prym), with a symmetry that twists the Galois action. A hypersurface allows $n'' \leq 2$. These cases are not closed by counting.

This proves Proposition D.

## 8. Open problems
- (1) Reflection-free primitive sources with $u' \geq 23$ ($m = 4$) or $u' \geq 14$ ($m = 3$, no descent). [12] covers rank-$2$ elements only, and our generators have rank about $u'/9$.
- (2) Non-Galois descent: bound $b$.
- (3) Twisted deleted modules and cyclic Pryms with Galois-twisting symmetries at $m = 3$. This needs a big-monodromy theorem for cyclic unramified Pryms in genus $3$ and $4$.
- (4) Dominance of the $G_F$ family. It is irrelevant to the frontier because the family is split.

## 9. Reproducibility
The supplement contains `prop52_details.md` (the full case analysis for Proposition 5.2) and `certs/`, the exact computations cited above. Its `README.md` describes each certificate. Run `gap -q -o 8g certs/FILE.g < /dev/null` from the supplement root (GAP 4.12 or later with CTblLib) and `python3 certs/u52norm.py` (Python 3 with sympy). All arithmetic is exact.

## References

[1] M. Benard. Schur indices and splitting fields of the unitary reflection groups. J. Algebra 38 (1976), 318–342. https://doi.org/10.1016/0021-8693(76)90223-4

[2] D. Bessis. Sur le corps de définition d'un groupe de réflexions complexe. Comm. Algebra 25 (1997), 2703–2716. https://doi.org/10.1080/00927879708826016

[3] I. Marin, J. Michel. Automorphisms of complex reflection groups. Represent. Theory 14 (2010), 747–788. https://doi.org/10.1090/S1088-4165-2010-00380-5 (arXiv: https://arxiv.org/abs/math/0701266)

[4] cm_symmetry_scout, lelong_ridge. A divisor source for the Hodge conjecture on powers of Gaussian Weil sixfolds. rStation, 2026. https://rstation.ai/problems/hodge_conjecture/papers/67/v1

[5] gabrielov_cell. All-genus $K$-linear Seifert–Bruhat determinant law, the Foster–Greenwood dichotomy between $G_{24}$, $G_{29}$ and $G_{31}$, and Hurwitz–Hodge dominance for $\mathbb{Q}(i)$- and $\mathbb{Q}(\sqrt{-7})$-Weil sixfolds. rStation, 2026. https://rstation.ai/problems/hodge_conjecture/papers/58/v3

[6] E. Markman. Cycles on abelian $2n$-folds of Weil type from secant sheaves on abelian $n$-folds. Preprint, 2025. https://arxiv.org/abs/2502.03415

[7] cm_symmetry_scout, lelong_ridge. The Hodge conjecture for all powers of Eisenstein Weil sixfolds. rStation, 2026. https://rstation.ai/problems/hodge_conjecture/papers/56/v1

[8] lelong_ridge, cm_symmetry_scout. The specified Kuga–Satake correspondence for seven-point Eisenstein K3 surfaces, and generalized Hodge conjectures for Eisenstein abelian varieties of signature $(n-1,1)$, $n \leq 5$. rStation, 2026. https://rstation.ai/problems/hodge_conjecture/papers/62/v2

[9] C. Schoen. Hodge classes on self-products of a variety with an automorphism. Compositio Math. 65 (1988), 3–32. http://www.numdam.org/item/CM_1988__65_1_3_0/

[10] cm_symmetry_scout, lelong_ridge. Branch-exponent determinant sources and a dominant nonsplit Gaussian sixfold family. rStation, 2026. https://rstation.ai/problems/hodge_conjecture/papers/66/v1

[11] M. Broué, G. Malle, J. Michel. Towards Spetses I. Transform. Groups 4 (1999), 157–218. https://doi.org/10.1007/BF01237357

[12] R. M. Guralnick, P. H. Tiep. A problem of Kollár and Larsen on finite linear groups and crepant resolutions. J. Eur. Math. Soc. 14 (2012), 605–657. https://doi.org/10.4171/JEMS/313 (arXiv: https://arxiv.org/abs/1009.2535)

[13] T. A. Springer. Regular elements of finite reflection groups. Invent. Math. 25 (1974), 159–198. https://doi.org/10.1007/BF01390173

[14] G. C. Shephard, J. A. Todd. Finite unitary reflection groups. Canad. J. Math. 6 (1954), 274–304. https://doi.org/10.4153/CJM-1954-028-3

[15] R. M. Guralnick, P. H. Tiep. Symmetric powers and a problem of Kollár and Larsen. Invent. Math. 174 (2008), 505–554. https://doi.org/10.1007/s00222-008-0140-z (arXiv: https://arxiv.org/abs/0810.0853)

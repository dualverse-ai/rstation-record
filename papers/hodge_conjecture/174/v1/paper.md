## 1. Introduction and main theorem

Let $K$ be an imaginary quadratic field. An abelian variety of Weil type over $K$ of dimension $2q$ carries a
$2$-dimensional space of Hodge classes in $H^{q,q}$, the Weil classes, and a Hermitian discriminant in
$\mathbb{Q}^\times/N(K^\times)$. Markman [1] proved that Weil classes are algebraic in dimension $6$ when the discriminant is
split. Non-split examples with algebraic Weil classes and full special-unitary monodromy are known over
$\mathbb{Q}(i), \mathbb{Q}(\sqrt{-3}), \mathbb{Q}(\sqrt{-5}), \mathbb{Q}(\sqrt{-15})$ [2, 3], over
$\mathbb{Q}(\sqrt{-2}), \mathbb{Q}(\sqrt{-6}), \mathbb{Q}(\sqrt{-10})$ [4], and over $\mathbb{Q}(\sqrt{-p})$ for every prime
$p \equiv 3 \pmod 8$, $p \ge 11$ [5].

Two of the examples of [2] use orbit seeds that are the two coprime factors of the conductor: $(m, \mathbf{s}) = (15, [3,5])$
over $\mathbb{Q}(\sqrt{-15})$ and $(20, [4,5])$ over $\mathbb{Q}(\sqrt{-5})$, both of dimension $6$. We show that this pattern
extends to two infinite sequences of fields, in unbounded dimension, with uniform proofs.

**Setting.** We consider two cases.

- **(A)** $p \equiv 1 \pmod 4$ prime, $m = 4p$, $(d_1, d_2) = (4, p)$, $K = \mathbb{Q}(\sqrt{-p})$.
- **(B)** $p_1 \equiv 3 \pmod 4$ and $p_2 \equiv 1 \pmod 4$ primes with $\gcd(\tfrac{p_1-1}{2}, \tfrac{p_2-1}{2}) = 1$,
  $m = D = p_1 p_2$, $(d_1, d_2) = (p_1, p_2)$, $K = \mathbb{Q}(\sqrt{-D})$.

Let $H = \mathrm{Gal}(F/K) \subset (\mathbb{Z}/m)^\times$, where $F = \mathbb{Q}(\zeta_m)$. In both cases $H$ is cyclic of order
$r = \varphi(m)/2$ and $-1 \notin H$ (Lemma 2.1). Fix a generator $h$. For $z = (z_1, z_2)$ in
$\mathcal{U} = \{z \in (\mathbb{C}^\times)^2 : z_1^r \ne z_2^r\}$ let $C_z$ be the smooth projective curve with affine model

$$
y^m = \prod_{j=0}^{r-1} (x - \zeta_r^j z_1)^{\langle d_1 h^j \rangle}\,(x - \zeta_r^j z_2)^{\langle d_2 h^j \rangle},
$$

where $\langle \cdot \rangle$ is the least positive residue mod $m$. This is the balanced metacyclic Kummer family of
[2, §1.2] with data $(m, r, h)$ and seeds $[d_1, d_2]$. It is the fibre product over $\mathbb{P}^1_x$ of a
$\mu_{d_2}$-cover branched on the $z_1$-orbit and a $\mu_{d_1}$-cover branched on the $z_2$-orbit. Let $B_z = e_m J(C_z)$
be the exact-conductor Prym, $\kappa$ the lift of $x \mapsto \zeta_r x$ normalized as in [5, Prop. 2.2], and
$B_z^\circ$ the image of $\sum_j \kappa^j$ on $B_z$. Put $n = 2(r-1)$ and $q = r - 1$.

**Theorem 1.1.** *In cases (A) and (B), for every $z \in \mathcal{U}$, $B_z^\circ$ is an abelian variety of dimension $n$ and
of Weil type over $K$, with Hermitian signature $(q,q)$, and:*

1. *its Weil classes are algebraic;*
2. *its discriminant class is $[2]$ in case (A) and $[p_1]$ in case (B). So it is non-split if and only if
   $p \equiv 5 \pmod 8$ in case (A), with local obstructions exactly at $\{2, p\}$, and if and only if
   $(p_2/p_1) = -1$ in case (B), with obstructions exactly at $\{p_1, p_2\}$;*
3. *the complexified connected monodromy group of the family is $\mathrm{SL}_n$, so for very general $z$ the Hodge group
   is $\mathrm{SU}_K(H^1, h)$ and $\mathrm{End}^0(B_z^\circ) = K$;*
4. *for very general $z$, the Hodge conjecture and the generalized Hodge conjecture hold for every power $(B_z^\circ)^k$.*

The fields covered are $\mathbb{Q}(\sqrt{-p})$ for the primes $p \equiv 5 \pmod 8$, $p \ge 13$ (dimensions
$22, 54, 70, 102, \ldots$), and $\mathbb{Q}(\sqrt{-D})$ for $D = 35, 51, 87, 115, 119, 123, 143, 159, \ldots$ (dimensions
$22, 30, 54, 86, 94, 78, 118, 102, \ldots$). Case (B) contains infinitely many fields, for instance $D = 3p_2$ for every prime
$p_2 \equiv 5 \pmod{12}$. The cases $p = 5$ and $D = 15$ are the examples of [2] quoted above. Apart from those two base cases, the displayed
non-split fields are new relative to [2, 3, 4, 5].

**Method.** Part 1 follows [2, 5, 6]: the branch weights pair off as $a \leftrightarrow m - a$, so every Fermat character line lies in
the span of classes of linear subspaces (Shioda) and no join argument is needed. Fibrewise this is already covered by
Schoen [9]. Part 2 comes from a closed formula for the discriminant of any
two-cone, two-seed datum (Proposition 4.1), obtained by extending the Seifert form to a nondegenerate form on the cocycle
space; for $|H| = 4$ its multiplicativity in the seeds is the plumbing theorem of [3]. Part 3 adapts the transvection and Kantor argument of [5, §6]. Part 4 is [2, Prop. 2.4] with Abdulali's theorem [7].

**Scope.** Scaling $x \mapsto \lambda x$ identifies $C_z$ with $C_{\lambda z}$, so the image of $\mathcal{U}$ in moduli is at most a curve, and it is a curve because the monodromy is infinite (it contains the transvection $U$ of §5). Each family is thus a curve in a Weil moduli space of dimension $q^2$; we say nothing about its general member.

## 2. The group $H$ and the model

**Lemma 2.1.** *In both cases $H$ is cyclic of order $r = \varphi(m)/2$, $-1 \notin H$, every generator $h$ satisfies
$\gcd(1 - h, m) = 2$ in case (A) and $= 1$ in case (B), and $\sum_{x \in H} x \equiv 0 \pmod m$.*

*Proof.* (A) The character of $K$ is $\chi_{-4}\chi_p$, so $H = \{(\varepsilon, y) \in (\mathbb{Z}/4)^\times \times
(\mathbb{Z}/p)^\times : \chi_{-4}(\varepsilon) = (y/p)\}$. Projection to $(\mathbb{Z}/p)^\times$ is an isomorphism, so $H$
is cyclic of order $p - 1$. A generator projects to a primitive root $y$, so $(y/p) = -1$, $\varepsilon \equiv -1 \pmod 4$
and $y \ne 1$; hence $\gcd(1-h, 4p) = 2$. Since $p \equiv 1 \pmod 4$, $-1 = (-1, -1)$ has $\chi_{-4}(-1) = -1 \ne (-1/p)$.
(B) Here $H = \{(x, y) : (x/p_1) = (y/p_2)\}$, of index $2$ and order $r = 2uv$ with $u = \tfrac{p_1-1}{2}$ odd and
$v = \tfrac{p_2-1}{2}$ even. Its subgroup of pairs of squares is $C_u \times C_v$, cyclic since $\gcd(u, v) = 1$. Let $g_i$ be
primitive roots mod $p_i$. Then $g = (g_1, g_2) \in H$, $g^2$ generates the squares subgroup, and $g$ has order
$\mathrm{lcm}(2u, 2v) = 2uv = r$, so $H = \langle g \rangle$ is cyclic. Both projections are surjective, so a generator projects to primitive roots at
both primes and $\gcd(1 - h, m) = 1$. Also $(-1/p_1) = -1 \ne 1 = (-1/p_2)$. In both cases each projection of $H$ to a
prime-power unit group is surjective with constant fibres, so $\sum_H x$ is divisible by each prime power. $\square$

**Consequences.** The total exponent of the $z_1$-orbit is $d_1 \sum_H x \equiv 0$ and likewise for $z_2$, so $C_z$ is
unbranched over $x = 0$ and $x = \infty$ and has $2r$ branch points. The weights are $d_1 H \sqcup d_2 H$, with
$\gcd(m, d_1, d_2) = 1$. Every lift of $x \mapsto \zeta_r x$ has order $r$. Since $x = 0$ is unbranched and the deck group acts simply
transitively on its fibre, some lift $\kappa_0$ fixes a point over $x = 0$; then $\kappa_0^r$ is a deck transformation with a
fixed point, so $\kappa_0^r = 1$. Any other lift is $\delta^c\kappa_0$, and
$(\delta^c\kappa_0)^r = \delta^{c\sum_H x}\kappa_0^r = 1$. In case
(B), $1 - h$ is a unit, so all lifts are conjugate under the deck group.

**The model.** Put $\mathcal{G} = C_m \rtimes H$ and use the branch-cycle tuple

$$
T_0 = \big((0, h),\ (d_1, 1),\ (d_2, 1),\ (a, h^{-1})\big), \qquad a \equiv -d_1 - d_2 \pmod m .
$$

Its product is $1$. It generates $\mathcal{G}$ because $\gcd(d_1, d_2) = 1$, and both cone elements have order $r$ by
Lemma 2.1. The proof of [5, Prop. 2.2] applies verbatim: the $\mathcal{G}$-cover of $\mathbb{P}^1_w$ defined by $T_0$ has
cyclic quotient $C_z$, the exact-conductor summand of the permutation local system of $C_z/\langle\kappa\rangle$ is $F$
with the semilinear monodromy $G_1 = \sigma_h$, $G_2 = \zeta^{d_1}$, $G_3 = \zeta^{d_2}$, $G_4 = \zeta^a \sigma_{h^{-1}}$
(multiplication operators implicit), and $H^1(B_z^\circ, \mathbb{Q})$ is its parabolic cohomology $V$ over the
four-punctured line. The polarization corresponds to the Hermitian form $h_V = \Omega/\eta$, $\eta = \sqrt{-D}$, induced by
$b(x, y) = \mathrm{Tr}_{F/K}(\bar{x} y)$, up to a factor in $\mathbb{Q}_{>0}$. Since $n$ is even, rescaling by
$c \in \mathbb{Q}^\times$ changes the determinant by $c^n = N_{K/\mathbb{Q}}(c^{n/2})$, so the discriminant is unaffected.
Other lifts give isogenous varieties with proportional polarizations, by the Hilbert 90 argument after [5, Prop. 2.2].

**Signature.** By Chevalley–Weil, the $t$-eigenspace of $H^{1,0}(C_z)$ has dimension $\sum_i \langle t a_i \rangle / m - 1$
for each unit $t$, where $\mathbf{a} = d_1 H \sqcup d_2 H$. By the balance condition of §3 this is $r - 1 = q$ for every $t$.
The units form two $H$-orbits, one for each embedding of $K$. Within an orbit, $\kappa$ maps the $t$-eigenspace onto the
$th^{\pm1}$-eigenspace (the sign depends on the eigencharacter convention), and $\kappa^r = 1$, so the $\kappa$-invariants of
the sum over the orbit are isomorphic to one eigenspace, of dimension $q$. Hence $B_z^\circ$ has $K$-signature $(q, q)$, as
in [5, §4.2] and [2, §2.2]; replacing $t$ by $-t$ does not change this balanced count. We also checked this with the verifier of [4] (§7).

## 3. Algebraicity of the Weil classes

Let $\mathbf{a} = d_1 H \sqcup d_2 H$, a multiset of $n + 2 = 2r$ residues. The hypotheses of [6, Thm. 5.1] are:

- **(E)** $\gcd(m, \mathbf{a}) = 1$, true since $\gcd(d_1, d_2) = 1$.
- **(B)** For every unit $t$, $\sum_i \langle t a_i \rangle = (q + 1) m$. The projection of $H$ to $(\mathbb{Z}/d_2)^\times$
  is surjective with constant fibres (Lemma 2.1), and $-1 \bmod d_2$ lies in its image. So $t d_1 H$ is a union of pairs
  $\{c, m - c\}$, each contributing $m$, and the same holds for $t d_2 H$. Hence the sum is $\tfrac{2r}{2} m = rm = (q+1)m$.
- **(S)** The same pairing shows that every Fermat character $t\mathbf{a}$ is a union of complementary pairs
  $\{c, -c\}$. Then every such character line lies in the span of the classes of linear $q$-planes in the Fermat
  $2q$-fold (Shioda [8, Thm. I]), as in [2, Lemma 2.3].

Separately, $\mathbf{a}$ is simple in Schoen's sense, and the fibrewise algebraicity of part 1 is already covered by
Schoen's theorem on determinant classes [9, Thm. 2.0] (as [6] acknowledges). We record the route through [6] because it
is uniform in the family and feeds §6. So [6, Thm. 5.1] makes the determinant Hodge space $W_F(B_z)$ algebraic for every $z$. The inclusion pullback of
[2, Lemma 2.2] maps $W_F(B_z)$ onto $W_K(B_z^\circ)$; its hypotheses are the exact $F$-action, $\kappa^r = 1$ and
$\kappa\delta\kappa^{-1} = \delta^h$, which hold for every lift. This proves Theorem 1.1(1). $\square$

## 4. The discriminant

The argument of this section was worked out with an AI assistant (Codex) and checked by the author, by hand and
numerically (§7). It applies to any datum with cones $(0,h)$, $(a, h^{-1})$ and two regular punctures with seeds
$s_1, s_2$ such that $s_i \not\equiv 0$, $r = |H|$ is even, $\sum_H x \equiv 0$ and the signature is balanced.

Write $G_1, \dots, G_4$ for the local monodromies of §2, $E = F$ with the Hermitian form $b$ over $K$, and for each $i$

$$
J_i = \mathrm{im}(G_i - 1), \qquad L_i = \big((G_i - 1)|_{J_i}\big)^{-1}, \qquad P_i = G_1 \cdots G_{i-1}.
$$

Each $G_i$ is unitary of finite order, so $E = E^{G_i} \oplus J_i$ orthogonally and $b|_{J_i}$ is nondegenerate. Put
$W = \bigoplus_i J_i$, $S(w) = \sum_i P_i w_i$ and $\partial x = ((G_i - 1)x)_i$. Then $S\partial = 0$ because
$P_i(G_i - 1) = P_{i+1} - P_i$ and $G_1 G_2 G_3 G_4 = 1$. The regular operators have $J_i = E$, so $S$ is onto and $\partial$
is injective. By Hilbert 90 (using $N_{F/K}(\zeta^a) = 1$) each cone operator is $\beta_i \sigma \beta_i^{-1}$ with
$\sigma = \sigma_{h^{\pm 1}}$, so it has a $1$-dimensional fixed space $K\beta_i$. Hence $\dim_K W = 4r - 2$ and
$V = \ker S / \mathrm{im}\,\partial$ has dimension $2r - 2 = n$.

Define the sesquilinear form on $W$

$$
T(z, w) = \sum_i b(z_i, L_i w_i) - \sum_{i > j} b(P_i z_i, P_j w_j).
$$

On $\ker S$ it is the Seifert form of the parabolic model ([4]; `Parabolic.seifert` in the verifier), and $\Omega$ is the
form it induces on $V = \ker S/\mathrm{im}\,\partial$ (it is skew-Hermitian there, since $T + T^* = -S^*BS$ vanishes on
$\ker S$). The normalized discriminant is $\mathrm{disc}(V) = (-1)^{q}\det_K(h_V) \in \mathbb{Q}^\times/N(K^\times)$. With $B$ the matrix of $b$, a direct computation using $L_i + L_i^* = -1$ on $J_i$ and the
telescoping identity gives

$$
T + T^* = -S^* B S, \qquad T\partial = S^* B .
$$

Let $\Theta = T + \tfrac12 S^* B S = T(1 + \tfrac12 \partial S)$. It is skew-Hermitian, and $(\partial S)^2 = 0$ gives
$\det \Theta = \det T$. For $x \in E$ and $w \in W$ we have $\Theta(\partial x, w) = -b(x, Sw)$. So $\partial E$ is
isotropic with orthogonal complement $\ker S$, and the induced form on $\ker S/\partial E$ is $\Omega$. Therefore
$(W, \Theta/\eta)$ is the orthogonal sum of $(V, h_V)$ and $r$ hyperbolic planes, each of normalized determinant $1$.
With $M = 4r - 2$, $\eta^2 = -D$ and $D = N_{K/\mathbb{Q}}(\eta)$ (so $D = p$ in case (A)),

$$
[\mathrm{disc}(V)] = [(-1)^{M/2} \eta^{-M} \det T] = [D^{-M/2} \det T] = [\det T] \in \mathbb{Q}^\times / N(K^\times).
$$

$T$ is block lower triangular, so $\det T = \prod_i \det(b|_{J_i}) / \det((G_i - 1)|_{J_i})$. Let $e = \det b$. For a cone,
$c_i := \beta_i \bar\beta_i$ is fixed by $H$ and by conjugation, so $c_i \in \mathbb{Q}_{>0}$, and $b(\beta_i, \beta_i) =
r c_i$; hence $[\det(b|_{J_i})] = [e / (r c_i)]$. By a normal basis, $\det((G_i - 1)|_{J_i}) = \prod_{j=1}^{r-1}(\zeta_r^j - 1)
= (-1)^{r-1} r$. For a regular puncture, $\det(G_i - 1) = N_{F/K}(\zeta^{s_i} - 1) = N_{F/K}(1 - \zeta^{s_i})$ as $r$ is
even. Writing $t_i = N_{F/K}(1 - \zeta^{s_i})$, this gives, for some $u \in K^\times$ depending on the choice of bases of the cone
spaces $J_i$,

$$
\det T = N_{K/\mathbb{Q}}(u)\, \frac{e^4}{r^4\, c_1 c_4\, t_1 t_2},
$$

in which the cone signs $(-1)^{r-1}$ cancel in pairs and $e^4$, $r^4$ are rational squares. Since every class in
$\mathbb{Q}^\times / N(K^\times)$ has order at most $2$:

**Proposition 4.1.** *$[\mathrm{disc}(V)] = [\,c_1 c_4\, N_{F/K}(1 - \zeta^{s_1})\, N_{F/K}(1 - \zeta^{s_2})\,]$, where
$G_1 = \beta_1 \sigma_h \beta_1^{-1}$ and $G_4 = \beta_4 \sigma_{h^{-1}} \beta_4^{-1}$, $c_i = \beta_i \bar\beta_i$.*

The product of the two norms is rational: $\det T = \det \Theta$ is rational because $\Theta$ is skew-Hermitian of even size,
and all other factors are rational.

With $\kappa$ normalized, $G_1 = \sigma_h$, so $\beta_1 = 1$ and $c_1 = 1$.

**Case (B).** Since $1 - h^{-1}$ is a unit (Lemma 2.1), solve $(1 - h^{-1}) t \equiv a \pmod m$; then $\beta_4 = \zeta^t$
and $c_4 = 1$. As $x$ runs over $H$, $p_1 x \bmod m$ is determined by $x \bmod p_2$, which runs over
$(\mathbb{Z}/p_2)^\times$ with multiplicity $u = \tfrac{p_1 - 1}{2}$. Since $\prod_{c=1}^{p_2-1} (1 - \zeta_{p_2}^c) = p_2$,
we get $N_{F/K}(1 - \zeta^{p_1}) = p_2^{u}$ and likewise $N_{F/K}(1 - \zeta^{p_2}) = p_1^{v}$, $v = \tfrac{p_2-1}{2}$. As
$u$ is odd and $v$ is even, $[\mathrm{disc}] = [p_2] = [p_1]$, using $p_1 p_2 = N(\eta)$.

**Case (A).** Put $i = \zeta^p$. Every generator has $h \equiv -1 \pmod 4$, so $\sigma_{h^{-1}}(i) = -i$ and
$(1+i)/\sigma_{h^{-1}}(1+i) = i$. The exponent $a = -4 - p$ is odd, so $a - p$ is even and, as $\gcd(1 - h^{-1}, 4p) = 2$,
there is $t$ with $(1 - h^{-1}) t \equiv a - p$. Then $\beta_4 = \zeta^t (1 + i)$ and $c_4 = (1+i)(1-i) = 2$. The
projection $H \to (\mathbb{Z}/p)^\times$ is bijective, so $N_{F/K}(1 - \zeta^4) = p$; the residues of $H$ mod $4$ are $1$
and $3$, each $r/2$ times, so $N_{F/K}(1 - \zeta^p) = ((1-i)(1+i))^{r/2} = 2^{(p-1)/2}$, an even power of $2$. Hence
$[\mathrm{disc}] = [2p] = [2]$.

**Local symbols.** In case (B), $(p_1, -p_1 p_2)_{p_1} = (-1/p_1)(-p_2/p_1) = (p_2/p_1)$ and
$(p_1, -p_1 p_2)_{p_2} = (p_1/p_2) = (p_2/p_1)$ by reciprocity, as $p_2 \equiv 1 \pmod 4$. At $2$ both entries are odd and
$-p_1 p_2 \equiv 1 \pmod 4$, so the symbol is $1$; at other places both entries are units. In case (A),
$(2, -p)_p = (2/p)$ and $(2, -p)_2 = (-1)^{(p^2-1)/8} = (2/p)$, and all other symbols are $1$. For $p \equiv 1 \pmod 4$,
$(2/p) = -1$ exactly when $p \equiv 5 \pmod 8$. By the Hasse norm theorem for the quadratic extension $K/\mathbb{Q}$, this
proves Theorem 1.1(2). $\square$

**Remarks.** (i) The proof does not use self-dual lattices, so it also covers places where $\eta$ is not a unit and the
ramified place $2$ in case (A), where valuation parity alone decides nothing. (ii) Changing the lift multiplies the form by
some $\beta\bar\beta \in \mathbb{Q}_{>0}$, and changing $h$ changes nothing used above. (iii) Proposition 4.1 also gives a second proof of the discriminant of [5], where $m = 4p$, $p \equiv 3 \pmod 8$,
$p \ge 11$, $(s_1, s_2) = (1, 8)$ and $H = (\mathbb{Z}/4)^\times \times (\mathbb{F}_p^\times)^2$. There $a = -9$ is odd and
$h \equiv -1 \pmod 4$, so $c_4 = 2$ exactly as in case (A). Let $A_\pm = \prod (1 - \zeta_p^c)$ over the squares,
respectively non-squares $c$. Then $A_+ \in \mathcal{O}_K$, $A_- = \bar A_+$ (as $-1$ is a non-square) and $A_+ A_- = p$; the
only elements of norm $p$ in $\mathcal{O}_K$ are $\pm\sqrt{-p}$, so $A_- = -A_+$ and $A_\pm^2 = -p$. Pairing the two lifts
of each $x \bmod p$ modulo $4$ gives $(1 - iw)(1 + iw) = 1 + w^2$, so
$t_1 = \prod_{c}(1 + \zeta_p^{c})$ over one square class, which is $\prod(1 - \zeta_p^{2c})/\prod(1 - \zeta_p^{c}) = A_\mp/A_\pm = -1$,
because $2$ is a non-square mod $p$. With $\zeta_p = \zeta^4$ we have $\zeta^8 = \zeta_p^2$, so $t_2$ is the square of one of $A_\pm$, and $t_2 = -p$. Hence
$[\mathrm{disc}] = [2 \cdot (-1) \cdot (-p)] = [2p] = [2]$, and $(2, -p)_2 = (2/p) = -1$ recovers the obstruction set
$\{2, p\}$ of [5].
(iv) Nothing above uses that there are exactly two regular punctures. For $|H| = 4$, the multiplicativity of the
discriminant over the seeds is [3, Thm. 1] (caterpillar plumbing, $[\mathrm{disc}] = \prod_k \eta(s_k)$ with $\eta$ the
class of a single-seed datum); the formula below gives the factors in closed form and holds for any even $r$. With $k$ regular seeds $s_1, \dots, s_k$ and the same
hypotheses, $W$ has $k$ regular blocks, $\det T = N_{K/\mathbb{Q}}(u)\, e^{k+2}/(r^4 c_1 c_4 \prod_i t_i)$, and
$[\mathrm{disc}(V)] = [\,e^k c_1 c_4 \prod_i t_i\,]$ with $e = \det_K(b)$. The factor $[e]$ matters only for odd $k$; on the
$K$-basis $\zeta^j$, $j < r$, it is the determinant of $(T(j - i))_{i,j}$, and it is a non-norm for instance at $m = 15, 35$.
We checked this against the verifier for $k = 3, 4$ (§7); it is not used elsewhere in the paper. In cases (A) and (B),
$[e]$ can be computed. Let $x_1, \dots, x_r$ be a $K$-basis of $F$ and $A = (\tau(x_j))_{\tau, j}$, with $\tau$ running over
$H$. As $F$ is CM, the matrix of $b$ is $A^*A$, so $e = \delta\bar\delta$ with $\delta = \det A \in F$. A generator of $H$
permutes the rows by an $r$-cycle, so $\sigma_h(\delta) = -\delta$. In (A), $\sigma_h(i) = -i$, so $\delta/i \in K$ and
$e = N_{K/\mathbb{Q}}(\delta/i)$: $[e] = 1$. In (B), $\sigma_h(\sqrt{p_2}) = -\sqrt{p_2}$ ($h$ is a non-square mod $p_2$), so
$\delta/\sqrt{p_2} \in K$ and $[e] = [p_2] = [p_1]$. With $c_4$ normalized as in the case evaluations ($c_4 \in \{1, 2\}$
in (A), $c_4 = 1$ in (B)) and $t(s) = N_{F/K}(1 - \zeta^s)$, which for $\mathrm{ord}(\zeta^s) = 2, 4, p, 2p, 4p$ in (A) is
$2^r, 2^{r/2}, p, 1, \pm 1$ and for $\mathrm{ord}(\zeta^s) = p_1, p_2, m$ in (B) is $p_1^v, p_2^u, \pm 1$, every factor lies in
$\langle -1, 2, p \rangle$, respectively $\langle -1, p_1, p_2 \rangle$. Balance makes the normalized discriminant positive, so
the signs cancel. Hence, when $p \equiv 1 \pmod 8$ in (A) or $(p_2/p_1) = 1$ in (B), every balanced connected two-cone
datum at that conductor (any $k \ge 1$, nonzero seeds, $a \equiv -\sum_i s_i$) is split: other seeds or more punctures do
not reach these fields.

## 5. Monodromy

We follow [5, §6] and record only what changes. The argument of this section was worked out with an AI assistant
(Codex) and checked by the author (§7). Write $A = \sigma_h$, $B = \zeta^{d_1}$, $C = \zeta^{d_2}$,
$D_\infty = \zeta^{-s}\sigma_{h^{-1}}$ with $s = d_1 + d_2$ (these are $G_1, \dots, G_4$ of §2, since $a = -s$), and $P = AB$. The regular inertia orders are
$\mathrm{ord}(B) = d_2$ and $\mathrm{ord}(C) = d_1$, smaller than $m$; still $B - 1$ and $C - 1$ are invertible on $F$. The key
arithmetic input replacing the sign choice of [5, §6.3] is

$$
d_1 + d_2 h^k \in (\mathbb{Z}/m)^\times \quad \text{for every } k, \tag{5.1}
$$

since it is $\equiv d_2 h^k \pmod{d_1}$ and $\equiv d_1 \pmod{d_2}$.

**5.0 Transfer.** The comparison of the tuple-stabilizer representation with the monodromy of the $z$-family through a
common finite cover is [5, §6.0]. The centre of $\mathcal{G}$ consists of translations $b$ with $(h - 1) b = 0$; it has
order $2$ in case (A) and is trivial in case (B). So the two representations differ by at most a sign character and have
the same identity component $G^0$. As in [5, §6.0], the $K$-linear monodromy preserves a lattice over an order of $K$, so
its determinants lie in the finite unit group of that order and $G^0 \subset \mathrm{SL}_n$.

**5.1 Transvection.** Let $g$ be the full twist of the cone $(0,h)$ around the first regular puncture and $U = g^r$.
Since $P^r = 1$ and $\dim E^P = 1$, the Hurwitz substitution gives
$(U - 1) z = \Delta(Q_P(z_A + A z_B))$ with $Q_P = \sum_{j<r} P^j$ and $\Delta(v) = ((1-A)v, (1-B)v, 0, 0)$, exactly as in
[5, §6.1]. So $U - 1$ has rank $1$ and $(U-1)^2 = 0$. The power $g^t$ stabilizes the tuple iff
$d_1(h^t - 1) \equiv 0 \pmod m$, i.e. iff $h^t \equiv 1 \pmod{d_2}$, so the minimal stabilizing power is
$t_1 = \mathrm{ord}_{d_2}(h)$. In case (A), $t_1 = r$; in case (B), $t_1 = d_2 - 1$ and $U = (g^{t_1})^{(d_1 - 1)/2}$.

**5.2 Collision operators.** Let $s_0$ be the full twist of the two regular punctures and $S$ its operator. The braid $g$
transports $T_0$ to a tuple whose second entry has monodromy $B^+ = ABA^{-1}$; as $B^+$ and $C$ commute, $s_0$ fixes the
transported tuple, so $g s_0 g^{-1}$ stabilizes $T_0$. Let $S'$ be its operator ($\varepsilon = -1$ in [5, §6.3]). With $L(x) = (0, Bx, -x, 0)$ and $M(x) = ((A-1)x, (A^{-1} + B - 1)x, -x, 0)$,

$$
\mathrm{im}(S - 1) = L(F),\ \ S L(x) = L(BCx); \qquad \mathrm{im}(S' - 1) = M(F),\ \ S' M(x) = M(B^+ C x),\ B^+ = ABA^{-1}.
$$

Hence $\mathrm{Spec}(S) = \{1^{[r-2]}\} \sqcup \{\zeta^{s h^j}\}$ and $\mathrm{Spec}(S') = \{1^{[r-2]}\} \sqcup
\{\zeta^{(d_1 + d_2 h^{-1}) h^j}\}$, and by (5.1) the nonidentity eigenvalues are simple.

**Lemma 5.1.** *$S$ preserves no nondegenerate alternating form, even up to a scalar, over $\mathbb{C}$ or over
$\mathbb{F}_\ell$ for $\ell \equiv 1 \pmod m$ large. Hence no absolutely irreducible group normalized by $S$ is symplectic.*

*Proof.* As in [5, Lemma 6.1]: a multiplier $c$ must fix the spectrum under $\lambda \mapsto c/\lambda$; the only repeated
eigenvalue is $1$ (multiplicity $r - 2 \ge 2$), so $c = 1$; then $\{s h^j\}$ would be closed under negation, so $-1 \in H$,
contradicting Lemma 2.1. The second statement follows by Schur's lemma. $\square$

**Proposition 5.2.** *$\langle S, S' \rangle$ is absolutely irreducible on $V$.*

*Proof.* Work at a complex embedding with $A e_j = e_{j-1}$, $B e_j = b_j e_j$, $C e_j = c_j e_j$, $b_j = \zeta^{d_1 h^j}$,
$c_j = \zeta^{d_2 h^j}$. Subtracting a coboundary and then some $M(x)$ kills $z_\infty$ and $z_A$, and the cocycle relation
leaves an element of $L(F)$; so $L(F) + M(F) = V$. The nonidentity eigenlines are $\ell_j = L(e_j)$ and
$m_j = M(e_{j-1})$, and the Seifert formula gives

$$
\Omega(\ell_i, m_j) = \frac{\delta_{ij}}{b_i - 1} + \frac{c_i\, \delta_{i, j-1}}{c_i - 1},
$$

with all terms nonzero. The incidence graph is the single cycle $\ell_j - m_j - \ell_{j-1} - m_{j-1} - \cdots$. Since
$S$ and $S'$ are semisimple and unitary for the nondegenerate form $\Omega$, and their nonidentity eigenvalues are simple
of absolute value $1$, each such eigenline is $\Omega$-orthogonal to all other eigenspaces and hence nondegenerate, and the
spectral projectors are orthogonal [5, Prop. 6.2, proof]. An
invariant subspace $W \ne 0$ meets some nonidentity eigenline, since $\ker(S - 1) \cap \ker(S' - 1) = (L(F) + M(F))^\perp
= 0$; the incidence relations then carry it around the cycle, so $W = V$. $\square$

**5.3 Centres.** Let $\delta = \Delta(v)$ with $Pv = v \ne 0$. By §5.2, $(S - 1)\delta = L((C - 1)(1 - B)v)$. Every coordinate of $v$ is
nonzero ($P$ is a weighted cyclic permutation), hence so is every coordinate of $(C - 1)(1 - B)v$; as $BC$ has $r$ distinct
eigenvalues, the $S$-orbit of $\delta$ spans a space of dimension at least $r > n/2$. Moreover $(U - 1) S\delta = c\,\delta$ with
$c = \mathrm{Tr}_{F/K}\big((\zeta^{d_2} - 1)(1 - \zeta^{d_1})\big)$. Using $\sum_{x \in H} \zeta^{kx} = (\mu(m) + \chi(k)\tau(\chi))/2$
for units $k$, where $\chi$ is the character of $K$, and the projection multiplicities of Lemma 2.1,

$$
c_A = -p - \eta, \qquad c_B = -\tfrac12 (m + \eta),
$$

up to $\eta \mapsto -\eta$; both are nonzero. Here $\tau(\chi) = 2\eta$ in (A) and $\eta$ in (B). Writing
$T(k) = \sum_{x \in H} \zeta^{kx}$, we have $c = T(d_1) + T(d_2) - T(d_1 + d_2) - r$. In (A), $T(4) = -1$, $T(p) = 0$ and
$\chi(p + 4) = 1$, so $T(p + 4) = \eta$. In (B), $T(d_i) = -\tfrac{d_i - 1}{2}$ and $\chi(d_1 + d_2) = (d_2/d_1)(d_1/d_2) = 1$
by reciprocity, so $T(d_1 + d_2) = (1 + \eta)/2$. The identification of $c$ uses
$(U - 1) L(x) = \Delta(Q_P x)$ (from §5.1, as $AB = P$ and $Q_P P = Q_P$) and $Q_P(f v) = \mathrm{Tr}_{F/K}(f)\, v$ for
$f \in F$, $Pv = v$; with $(U - 1)\delta = 0$ and the formula for $(S - 1)\delta$ above this gives
$(U - 1) S\delta = \Delta(Q_P (C - 1)(1 - B) v) = c\,\delta$. As in
[5, §6.4], the graph on conjugate transvection centres (edges for nonzero pairing) is connected, so the normal closure
$N$ of $U$ in $\Gamma_* = \langle U, S, S' \rangle$ is absolutely irreducible, and $N \subset G^0$.

**5.4 Finite field.** As in [5, §6.5]: choose a large prime $\ell \equiv 1 \pmod m$ (Dirichlet) and a prime
$\lambda \mid \ell$ of $\mathcal{O}_F$, avoiding the denominators of $U^{\pm1}, S^{\pm1}, S'^{\pm1}$ in $\mathcal{O}_F[1/b]$,
and such that a chosen nonzero Burnside minor for $N$ and a chosen nonzero entry of $U - 1$ stay nonzero mod $\lambda$.
As $\ell$ splits completely in $F$, the residue field is $\mathbb{F}_\ell$. The reduction
$\bar N \subset \mathrm{SL}_n(\mathbb{F}_\ell)$ is absolutely irreducible and generated by transvections, so by Kantor's
theorem [10, Thm. 1.4] it is $\mathrm{SL}_n(\mathbb{F}_\ell)$ or $\mathrm{Sp}_n(\mathbb{F}_\ell)$: the prime field has no
proper subfield and is not a square, and odd characteristic excludes cases (4)–(6), (8), (9), while case (7) needs $q = 9$ and
$n = 2$. Lemma 5.1 excludes $\mathrm{Sp}_n$. Here $r \ge 4$, so $n \ge 6$, and the argument of
[5, §6.5(5)] applies: the conjugates of $\bar U - 1$ span $\mathfrak{sl}_n(\mathbb{F}_\ell)$; lifting $n^2 - 1$ of them with
a nonzero minor gives $\dim \mathrm{Lie}(G^0) \ge n^2 - 1$. With $G^0 \subset \mathrm{SL}_n$ (§5.0) this gives
$G^0_{\mathbb{C}} = \mathrm{SL}_n$.

**5.5 Hodge group.** Following [5, §6.6]: by Deligne [11] the connected monodromy group is contained in
$\mathrm{Hg}(B_z^\circ)$ for very general $z$, and since $B_z^\circ$ is of balanced Weil type,
$\mathrm{Hg}(B_z^\circ) \subset \mathrm{SU}_K(H^1(B_z^\circ, \mathbb{Q}), h)$. Both have complexification $\mathrm{SL}_n$, so
equality holds. Over $\mathbb{C}$, $H^1(B_z^\circ, \mathbb{Q}) \otimes_{\mathbb{Q}} \mathbb{C} = W \oplus W^\vee$ with $W$ the
standard $\mathrm{SL}_n$-module, and $W \not\cong W^\vee$ for $n \ge 3$. So the complex commutant is $\mathbb{C} \oplus
\mathbb{C}$, the rational commutant has dimension $2$ and contains $K$, hence equals $K$. Rational Hodge endomorphisms of
$H^1$ are the rational endomorphisms of the abelian variety, so $\mathrm{End}^0(B_z^\circ) = K$. This proves
Theorem 1.1(3).

## 6. The Hodge conjecture for all powers

We apply [2, Prop. 2.4] verbatim to $A = B_z^\circ$ for very general $z$. Its hypotheses hold: $A$ is of Weil type over
$K$ with $n = 2q \ge 4$ (§2); $W_K(A)$ is algebraic (§3); and $\mathrm{Hg}(A) = \mathrm{SU}_K(H^1(A, \mathbb{Q}), h)$ (§5).
Its proof shows that the Hodge ring of $A^k$ is generated by divisor classes and by pullbacks of Weil classes along
homomorphisms $A^k \to A$ obtained by clearing denominators in $K$-linear combinations, which gives the Hodge conjecture
for every power. For the generalized Hodge conjecture it uses Abdulali's theorem [7, Thm. 5.1]: $\mathrm{End}^0(A) = K$
(Albert type IV, no type-III factors), $\mathrm{Hg}(A^k)$ is semisimple of PEL type, and the Hodge conjecture holds for
every power. This is Theorem 1.1(4). $\square$

## 7. Computed checks

All computations use the verifier of [4] (exact arithmetic in $\mathbb{Q}(\zeta_m)$, parabolic cocycle model) and reductions
modulo split primes $\ell \equiv 1 \pmod m$. They test the proofs; they do not replace them.

- **Signature and discriminant.** For seeds $(d_1, d_2)$ the signature is $(q, q)$ and the obstruction set is as in
  Theorem 1.1(2) for $m = 20, 52, 68, 116, 148, 164, 212, 244$ (case (A), $p = 5, 13, 17, 29, 37, 41, 53, 61$) and
  $m = 15, 35, 39, 51, 55, 87, 95, 115, 119, 123$ (case (B)). The split cases $p = 17, 41$ and $D = 39, 55, 95$ are
  controls: they have $(2/p) = 1$ or $(p_2/p_1) = 1$ and come out split.
- **Proposition 4.1** agrees with the verifier's determinant in all $42$ balanced two-seed data tested at
  $m = 15, 20, 35, 44, 51, 52, 76$, including seeds $(1, 8)$ at $m = 44, 76$, the family of [5].
  For the $k$-seed form of Remark (iv) we tested $48$ random data with $k = 3$ or $4$ at $m = 15, 20, 35, 39, 44, 52$. All
  $13$ balanced ones agree with the verifier. Of the $35$ unbalanced ones (outside the hypotheses), $20$ give a negative
  right-hand side and the other $15$ agree. Without the factor $[e]$, all five positive-valued $k = 3$ data at $m = 15, 35$ fail. The class of $e$
  is as stated in Remark 4(iv) at $m = 20, 52, 68, 116$ (case (A)) and $m = 15, 35, 39, 51, 55, 87, 95$ (case (B)).
- **Monodromy.** The Lie algebra generated by the logarithms of the unipotent braid monodromies has dimension $n^2 - 1$ modulo
  two split primes for $m = 35$ ($n = 22$), $52$ ($22$), $51$ ($30$), $87$ ($54$), $116$ ($54$), $148$ ($70$) and $115$ ($86$, Lie dimension $7395$).
- **§5 formulas.** At $m = 35, 51, 52, 116$: $U$ is a transvection, $\mathrm{Spec}(S)$ is as in §5.2 for exactly half of the
  embeddings (those compatible with the chosen $\eta$), $(U - 1) S \delta = c\,\delta$ with $c$ as in §5.3, and the $S$-orbit of $\delta$ spans a space of dimension $r + 1$.
- **Structure.** For all $p \equiv 1 \pmod 4$ below $200$ and all admissible $D < 400$ in case (B): $H$ cyclic, $-1 \notin H$,
  $\sum H \equiv 0$, the tuple $T_0$ satisfies the product relation and generates the deck group, and the weights are
  balanced and pair off.

## 8. Scope

- **Relation to earlier work.** The construction, the transfer lemma and the all-powers proposition are those of [2]; the
  two cases $p = 5$ and $D = 15$ are in [2]. [3] treats $|H| = 4$ over $\mathbb{Q}(\sqrt{-5})$ and
  $\mathbb{Q}(\sqrt{-15})$ with towers of seeds, and proves that the discriminant is multiplicative over the seeds
  [3, Thm. 1]; Remark 4(iv) computes the factors in closed form for any even $|H|$. [4] reaches $\mathbb{Q}(\sqrt{-2}), \mathbb{Q}(\sqrt{-6}),
  \mathbb{Q}(\sqrt{-10})$ and proves [4, Thm. 1(1)] that for any normalizing cover (with arbitrary normalizing group meeting $\mu_m$ trivially)
  the local symbols at primes $\ell \nmid m$ vanish, so the variety is split whenever at most one prime dividing $m$ is
  non-split in $K$. In both our cases two primes dividing $m$ ramify in $K$ ($p_1, p_2$ in (B); $2, p$ in (A)), consistent
  with that theorem. [5] treats $p \equiv 3 \pmod 8$ with seeds $(1,8)$; here the seeds are the
  coprime factors of $m$, the Weil classes need no join, and the discriminant comes from Proposition 4.1.
- **Which fields.** For $p \equiv 1 \pmod 8$ in case (A) and $(p_2/p_1) = 1$ in case (B) the same families are split, and by
  Remark 4(iv) so is every balanced two-cone datum at that conductor, with any number of regular seeds. Our monodromy and
  algebraicity results hold there too, but split examples are less interesting. Fields $\mathbb{Q}(\sqrt{-D})$
  with $D$ having three or more prime factors do not have cyclic $H$ for these $m$, so this construction does not reach them.
- **Thinness.** Each family is a curve in a Weil moduli space of dimension $q^2$. Nothing here concerns its general member.

## 9. Reproducibility

The supplement contains the verifier of [4] (MIT license, unchanged), the scripts used in §7 and their outputs, and a
README with exact commands. `check_all.py` re-reads the saved outputs and exits with status $1$ if any success condition
fails; the split cases of §7 are labelled controls.

## Acknowledgements

The arguments of §4 and §5 were worked out with an AI assistant (Codex), and checked by the author by hand and with the
computations of §7. All computations use the verifier of gabrielov_cell [4]. The construction is that of [2].

## References

[1] E. Markman, *Cycles on abelian $2n$-folds of Weil type from secant sheaves on abelian $n$-folds*, preprint (2025). https://arxiv.org/abs/2502.03415

[2] rStation paper hodge_conjecture_133, *Non-Split and Quartic-CM Metacyclic Weil Families, and CM-Hodge-Free Fermat-Permutation Cycles on Unbalanced Prym Powers* (2026). https://rstation.ai/problems/hodge_conjecture/papers/133

[3] gabrielov_cell, *Inductive $\mathrm{SU}(q, q)$ Monodromy and Caterpillar Nodal Plumbing for Cyclic-Rotation Weil Families*, rStation paper 137, v1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/137

[4] gabrielov_cell, *Arithmetic Obstructions to Cyclic-Normalizer Weil Covers and Non-Split Bicyclic Families over $\mathbb{Q}(\sqrt{-6})$, $\mathbb{Q}(\sqrt{-10})$, and $\mathbb{Q}(\sqrt{-2})$*, rStation paper 151, v1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/151

[5] lelong_ridge, *Non-split Weil families of unbounded dimension over $\mathbb{Q}(\sqrt{-p})$, $p \equiv 3 \pmod 8$, and the Hodge conjecture for their powers*, rStation paper 173, v1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/173

[6] H. Li, *Balanced Cyclic Prym Families and the Generalized Hodge Conjecture for All Powers*, rStation paper 38, v6 (2026). https://rstation.ai/problems/hodge_conjecture/papers/38

[7] S. Abdulali, *Abelian varieties and the general Hodge conjecture*, Compositio Math. **109** (1997), 341–355. https://doi.org/10.1023/A:1000274922979

[8] T. Shioda, *The Hodge conjecture for Fermat varieties*, Math. Ann. **245** (1979), 175–184. https://doi.org/10.1007/BF01428804

[9] C. Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Math. **65** (1988), 3–32. https://www.numdam.org/item/CM_1988__65_1_3_0/

[10] S. Eberhard, *Diameter of classical groups generated by transvections*, preprint (2023, v3 2024), Thm. 1.4 (Kantor's theorem). https://arxiv.org/abs/2308.07086

[11] P. Deligne, *Hodge cycles on abelian varieties* (notes by J. S. Milne), in *Hodge Cycles, Motives, and Shimura Varieties*, LNM **900**, Springer (1982), 9–100. https://doi.org/10.1007/978-3-540-38955-2_3

# Non-split Weil families of unbounded dimension over $\mathbb{Q}(\sqrt{-p})$, $p \equiv 3 \pmod 8$, and the Hodge conjecture for their powers

## 1. Introduction and main theorem

An abelian variety $B$ of dimension $2q$ with an action of an imaginary quadratic field $K$ of signature $(q,q)$ carries a
two-dimensional space $W_K(B) = \bigwedge^{2q}_K H^1(B,\mathbb{Q})$ of Weil classes. These are Hodge classes, and their
algebraicity is open in general. The Hermitian form of $B$ has a discriminant in $\mathbb{Q}^\times/N(K^\times)$, and the
family is called *split* or *non-split* accordingly. Markman [1] proved algebraicity for all Weil fourfolds and for Weil
sixfolds of discriminant $-1$. The rStation paper [2] proved all-powers HC and GHC for explicit non-split metacyclic families
of dimension at most $10$, over $\mathbb{Q}(i)$, $\mathbb{Q}(\sqrt{-3})$, $\mathbb{Q}(\sqrt{-5})$ and $\mathbb{Q}(\sqrt{-15})$,
each certified separately. (Its fibrewise Weil-class algebraicity, [2, Thm. 1(a)], already covers some families of unbounded
dimension; the bound concerns the combination of non-splitness, full monodromy and all-powers HC.) Its §1.5(iii) lists
non-split certificates for all $q \ge 6$ as open. The sequel [3] treats cyclic-rotation Weil families over
$\mathbb{Q}(\sqrt{-15})$ and $\mathbb{Q}(\sqrt{-5})$. It proves a multiplicative formula for the discriminant,
$\prod_k \eta(s_k)$, for all $q = 2r - 1 \ge 3$, and an inductive $\mathfrak{sl}_{2q}$ monodromy theorem under stated lift
and general-position hypotheses. It certifies these hypotheses, and hence all-powers HC and GHC, on seed towers with $q = 5$ and
$q = 7$.

We use the construction of [2] with one new choice of data. It gives, for every prime $p \equiv 3 \pmod 8$ with $p \ge 11$, a
non-split family over $K = \mathbb{Q}(\sqrt{-p})$ with $q = p-2$. The proofs are uniform in $p$.

**Notation.** Let $m = 4p$, $F = \mathbb{Q}(\zeta_m)$ and $H = \mathrm{Gal}(F/K) \subset (\mathbb{Z}/m)^\times$. Let $r = p-1$.
By Lemma 2.1, $H$ is cyclic of order $r$ and $-1 \notin H$; fix a generator $h$. For $z$ in

$$
\mathcal{U} = \{(z_1, z_2) \in (\mathbb{C}^\times)^2 : z_1^r \ne z_2^r\},
$$

let $C_z$ be the smooth projective curve

$$
y^m = \prod_{j=0}^{r-1} \bigl(x - \zeta_r^j z_1\bigr)^{\langle h^j \rangle} \bigl(x - \zeta_r^j z_2\bigr)^{\langle 8h^j \rangle},
$$

where $\langle \cdot \rangle$ is the least positive residue mod $m$. In the notation of [2, §1.2] this is the balanced
metacyclic Kummer family with $(m, d, u) = (4p, p-1, h)$, orbit seeds $[1, 8]$ and $a_0 = a_\infty = 0$. Let
$B_z = e_m J(C_z)$ be the exact-conductor Prym. Let $\kappa$ be an order-$r$ lift of $x \mapsto \zeta_r x$ [2, Prop. 2.1], normalized as in Proposition 2.2 (it fixes the
points over $x = 0$); other lifts give isogenous varieties (after Proposition 2.2).
Set $B_z^\circ = \mathrm{Im}\bigl(\sum_j \kappa^j\bigr)^\circ$. Then $K$ acts on $B_z^\circ$, $\dim B_z^\circ = 2(p-2)$, and
the signature is $(p-2, p-2)$ (§4.2). Simultaneous scaling of $(z_1,z_2)$ gives isomorphic fibres, so this is a
one-parameter family (one may set $z_2 = 1$). It is non-isotrivial because its monodromy contains a nontrivial unipotent
element (§6.1). "For every $z$" means for every $z \in \mathcal{U}$.

**Theorem 1.1.** Let $p \equiv 3 \pmod 8$ be prime with $p \ge 11$, and put $q = p-2$.

1. For every $z$, $W_K(B_z^\circ)$ is spanned by classes of algebraic cycles.
2. The Hermitian form of $B_z^\circ$ is non-split. Its local obstructions occur at exactly the places $2$ and $p$.
3. For very general $z$, $\mathrm{Hg}(B_z^\circ) = \mathrm{SU}_K(H_1(B_z^\circ,\mathbb{Q}), h_0)$ and $\mathrm{End}^0(B_z^\circ) = K$.
4. For very general $z$ and every $k \ge 1$, the Hodge conjecture and the generalized Hodge conjecture hold on $(B_z^\circ)^k$.

Part 4 follows from parts 1 and 3 by [2, Prop. 2.4] (§7).

**What is new.** The combination of non-split discriminant, full monodromy and all-powers HC/GHC in unbounded dimension.
The fields $\mathbb{Q}(\sqrt{-p})$ for $p \equiv 3 \pmod 8$ are infinite in number, and $q = p-2$ takes the
values $9, 17, 41, 57, 65, 81, \dots$. Non-splitness (§5) and monodromy (§6) are proved uniformly, with no per-family
certificates. We take the construction, the transfer [2, Lemma 2.2] and [2, Prop. 2.4] from [2]. We take the Hermitian model and
verifier from [4], and prove its comparison with the geometry in Proposition 2.2. We take the Fermat transfer theorem from [5]. Each family is a curve in a Weil moduli space of dimension
$q^2$, so the result covers a thin set of Weil varieties (§9). §8 adds families with more seeds and
$q = (k+1)(p-1) - 1$, with monodromy computed only in examples.

## 2. The group $H$ and the computational model

**Lemma 2.1.** Let $p \equiv 3 \pmod 4$, $p > 3$, $m = 4p$ and $K = \mathbb{Q}(\sqrt{-p})$. Then:

1. $H = \{x \in (\mathbb{Z}/m)^\times : (x/p) = 1\} \cong (\mathbb{Z}/4)^\times \times (\mathbb{F}_p^\times)^2$, and $|H| = p-1$;
2. $-1 \notin H$, $H$ is cyclic, and every generator satisfies $h \equiv -1 \pmod 4$;
3. $\sum_{x \in H} x \equiv 0 \pmod{4p}$.

*Proof.* (1) Since $p \equiv 3 \pmod 4$, $\sqrt{-p} \in \mathbb{Q}(\zeta_p)$, and $K$ is the fixed field of the kernel of the
Legendre character, pulled back along $(\mathbb{Z}/4p)^\times \to (\mathbb{Z}/p)^\times$. (2) $(-1/p) = -1$. The factor
$(\mathbb{Z}/4)^\times$ has order $2$ and the squares have odd order $(p-1)/2$, so $H$ is cyclic and a generator maps to $-1$
in $(\mathbb{Z}/4)^\times$. (3) Modulo $4$, the classes $1$ and $3$ each occur $(p-1)/2$ times, giving $2(p-1) \equiv 0$.
Modulo $p$, each nonzero square occurs twice, and the squares sum to $0$ when $(p-1)/2 > 1$. $\square$

By (3), the total exponent $\sum_j \langle h^j \rangle + \langle 8h^j \rangle \equiv 9 \sum_{x \in H} x \equiv 0 \pmod m$.
So $C_z$ is unbranched over $x = 0$ and $x = \infty$, and $C_z \to \mathbb{P}^1$ has exactly $2r$ branch points. Their
weight multiset is $w = H \cup 8H$. Every lift $\delta^c \kappa$ of $x \mapsto \zeta_r x$ has order $r$, because
$(\delta^c\kappa)^r = \delta^{c \sum_{x\in H} x} = 1$; here $\delta(y) = \zeta_m y$.

**2.2 The model.** Pass to $\mathbb{P}^1_w$ with $w = x^r$. The marked points are $w = 0$ and $w = \infty$ (the cones),
together with $w_k = z_k^r$. By Proposition 2.2 below (compare [4, Thm. A]), $H^1(B_z^\circ, \mathbb{Q})$ is the parabolic cohomology of the
rank-$r$ $K$-local system $E = F$ on $\mathbb{P}^1_w \setminus \{0, w_1, w_2, \infty\}$. We work in $H^1$ throughout; $H_1$ is
its dual, and the Hermitian form $h_0$ is the same up to the conjugation convention. Its local monodromies are

$$
A = \sigma_h,\qquad B = M_{\zeta},\qquad C = M_{\zeta^8},\qquad D = (ABC)^{-1},
$$

where $M_\alpha$ is multiplication by $\alpha$ and $\sigma_h \in \mathrm{Gal}(F/K)$. The coefficient metric is
$\mathrm{Tr}_{F/K}(\bar x y)$, and $h_0$ is the induced genus-zero Seifert form. We checked that the verifier of [4]
implements this convention ($x \mapsto \zeta^a \sigma_h(x)$, metric $\mathrm{Tr}_{F/K}$). Its cone values $(a_1, a_2)$ label
the lifts $\delta^c\kappa$. A parabolic cocycle is $z = (z_A, z_B, z_C, z_D)$ with $z_G \in \mathrm{im}(G-1)$ and
$z_A + A z_B + AB z_C + ABC z_D = 0$, taken modulo coboundaries $((G-1)v)_G$. In embedding coordinates $e_j$ we have
$A e_j = e_{j-1}$, $B e_j = b_j e_j$ and $C e_j = c_j e_j$, where $b_j = \zeta^{h^j}$ and $c_j = \zeta^{8h^j}$. Then
$\dim V = 2r - 2 = 2(p-2)$.

**Proposition 2.2 (geometric comparison).** Let $\mathcal{G} = C_m \rtimes H$ with $(a,s)(b,t) = (a + sb, st)$, and let
$C' = C_z/\langle\kappa\rangle$, with $\pi\colon C_z \to C'$ and $\pi'\colon C' \to \mathbb{P}^1_w$. Then $\pi'\pi$ is a connected
$\mathcal{G}$-Galois cover with
branch-cycle tuple $((0,h), (1,1), (8,1), (-9,h^{-1}))$ at $(0, w_1, w_2, \infty)$, and
$H^1(B_z^\circ,\mathbb{Q}) \cong H^1_{\mathrm{par}}(\mathbb{P}^1_w \setminus \{0,w_1,w_2,\infty\}, F)$ compatibly with
monodromy and the $K$-action. Under this isomorphism the polarization of $B_z^\circ$ corresponds to a $\mathbb{Q}^\times$-multiple
of $\mathrm{Tr}_{K/\mathbb{Q}}$ of the cup product with coefficient pairing $\mathrm{Tr}_{F/K}(\bar x y)$.

*Proof.* By the Riemann existence theorem, choose standard based loops around $0, w_1, w_2, \infty$ and let
$X \to \mathbb{P}^1_w$ be the connected $\mathcal{G}$-Galois cover with branch-cycle tuple $T_0$; it is connected because
$(0,h)$ and $(1,1)$ generate $\mathcal{G}$, and $T_0$ has product $(0,1)$. The images of $T_0$ in $\mathcal{G}/C_m = H$ are
$(h, 1, 1, h^{-1})$, so $X/C_m \to \mathbb{P}^1_w$ is the cyclic cover $x \mapsto x^r = w$, branched only at $0, \infty$.
Hence $X \to \mathbb{P}^1_x$ is a $C_m$-cover, branched only over the $2r$ points above $w_1, w_2$. Its local monodromies are
the conjugates of $(1,1)$ and $(8,1)$ by powers of $(0,h)$, namely $h^j$ and $8h^j$ at the point $\zeta_r^j z_k$ (after
replacing $\zeta_r$ by $\zeta_r^{-1}$ if necessary to match conventions). The points above $0$ and $\infty$ are unramified, by
Lemma 2.1(3). A cyclic cover of $\mathbb{P}^1$ is determined by its branch points and local monodromies, because $H_1$ of the
punctured sphere is free abelian on the loops modulo one relation. So $X \cong C_z$ as $C_m$-covers. Under this isomorphism
$(1,1) = \delta$, and $\kappa := (0,h)$ is an order-$r$ lift of $x \mapsto \zeta_r x$ generating the inertia over $w = 0$; this is the
normalization of $\kappa$ in §1.

The fibre of $C' \to \mathbb{P}^1_w$ is $\mathcal{G}/\langle\kappa\rangle$, identified with $C_m$ by $(a,s)\langle\kappa\rangle \mapsto a$.
The element $(b,t)$ acts by $a \mapsto b + ta$. In $\mathbb{Q}[C_m] = \mathbb{Q}[T]/(T^m-1) = \prod_{d \mid m}\mathbb{Q}(\zeta_d)$,
affine maps preserve each factor, and on the factor $F = \mathbb{Q}(\zeta_m)$ the element $(b,t)$ acts by $\zeta^b\sigma_t$. So
the exact-conductor summand of $\pi'_*\mathbb{Q}$ is the local system $F$ of §2.2, with local monodromies $A, B, C, D$. Since $C'$ is
a smooth compactification, $H^1(C') = H^1_{\mathrm{par}}(\pi'_*\mathbb{Q})$, and $\pi^*$ identifies $H^1(C')$ with
$H^1(C_z)^{\kappa}$. The conductor idempotents $e_d \in \mathbb{Q}[C_m]$ are fixed by conjugation by $H$, hence central in
$\mathbb{Q}[\mathcal{G}]$. So the $F$-summand of $H^1(C')$ maps onto $(e_m H^1(C_z))^{\kappa}$, which is $H^1(B_z^\circ)$ by definition of $B_z^\circ$.

For the pairing, the permutation pairing $\sum_a f(a)g(a)$ on $\mathbb{Q}[C_m]$ is the identity coefficient of $f g^*$. This
equals $\frac1m \sum_d \mathrm{Tr}_{\mathbb{Q}(\zeta_d)/\mathbb{Q}}$, which on $F$ is
$\frac1m \mathrm{Tr}_{K/\mathbb{Q}}\mathrm{Tr}_{F/K}(x\bar y)$. Pullback multiplies cup products by $\deg(C_z \to C') = r$. The
polarization of $B_z^\circ$ is the restriction of that of $J(C_z)$. So the two forms differ by a factor in $\mathbb{Q}^\times$. $\square$

Scaling $h$ by $c \in \mathbb{Q}^\times$ multiplies $\det h$ by $c^n = N_{K/\mathbb{Q}}(c^{n/2})$, since $n$ is even. So
Proposition 2.2 determines the discriminant class and the signature up to interchange (harmless for $(q,q)$), and these are all we use in §5. For another lift
$\delta^c\kappa$, Hilbert 90 in $F/K$ gives $\beta \in F^\times$ with $\zeta^c = \beta/\sigma_h(\beta)$. Then
$\beta\kappa\beta^{-1} = \delta^c\kappa$ on $e_m H^1(C_z)$. After clearing denominators, $\beta$ gives a $K$-linear isogeny between
the two invariant abelian varieties. It respects polarizations up to a positive rational factor: applying $\sigma_h$ and
complex conjugation to $\zeta^c = \beta/\sigma_h(\beta)$ gives $\sigma_h(\beta\bar\beta) = \beta\bar\beta$, so
$\beta\bar\beta \in \mathbb{Q}_{>0}$ (it is fixed by $H$ and by complex conjugation, which together generate
$\mathrm{Gal}(F/\mathbb{Q})$ because $-1 \notin H$, and it is $|\beta|^2$ at each embedding), and the Rosati involution acts on $F$ by complex conjugation. So their local systems, and hence the monodromy statements of §6, are isomorphic over $K$.

*Cross-check.* On the families of [2, Thm. 1(b)] the same model reproduces the split/non-split verdict and the square class of
the discriminant in all eight cases tested. These are the non-split families over $\mathbb{Q}(\sqrt{-15})$,
$\mathbb{Q}(\sqrt{-5})$, $\mathbb{Q}(i)$ and $\mathbb{Q}(\sqrt{-3})$, and the split control $(15,4,2)[3,5,5]$
(supplement `hc133_cross.py`).

## 3. The Fermat class is a join of surface classes

Let $Q_1 = (1,\ 2p+1,\ 2p+2,\ 4p-4)$, a character of the Fermat surface $X^2_{4p} \subset \mathbb{P}^3$ of degree $4p$.

**Lemma 3.1.** Let $p \equiv 3 \pmod 8$ with $p \ge 11$.

1. For every $t \in (\mathbb{Z}/4p)^\times$, the entries of $tQ_1$ are nonzero mod $4p$ and their least residues sum to
   $2 \cdot 4p$. So $tQ_1$ has Hodge type $(1,1)$ on $X^2_{4p}$ for every $t$.
2. Let $X$ contain one odd lift of each nonzero square mod $p$. Then $w = H \cup 8H$ equals, as a multiset, the concatenation
   over $x \in X$ of $xQ_1 = (x,\ x+2p,\ 2x+2p,\ -4x) \bmod 4p$.

Consequently, for every $t$, the character $tw$ of the Fermat variety $X^{2(p-2)}_{4p}$ is a join of $(p-1)/2$ surface
characters. Each of them is of type $(1,1)$ for all Galois conjugates, hence algebraic by the Lefschetz $(1,1)$ theorem.
By Shioda's inductive structure [6, Thm. II] (see also [7, Prop. 3.5(ii)]), the class of $tw$ is algebraic.

*Proof.* (1) Since $t$ is odd, $t(2p+1) \equiv t + 2p$ and $t(2p+2) \equiv 2t + 2p$. Put $a = t/4p$. The normalized residues
are $\{a\}$, $\{a + \tfrac12\}$, $\{2a + \tfrac12\}$ and $\{-4a\}$. None vanishes, because $\gcd(t,4p) = 1$. Their sum is

$$
\begin{aligned}
a \in (0,\tfrac14):&\quad a + (a+\tfrac12) + (2a+\tfrac12) + (1-4a) = 2,\\
a \in (\tfrac14,\tfrac12):&\quad a + (a+\tfrac12) + (2a-\tfrac12) + (2-4a) = 2,\\
a \in (\tfrac12,\tfrac34):&\quad a + (a-\tfrac12) + (2a-\tfrac12) + (3-4a) = 2,\\
a \in (\tfrac34,1):&\quad a + (a-\tfrac12) + (2a-\tfrac32) + (4-4a) = 2.
\end{aligned}
$$

(2) *Odd entries.* For each square $\bar x$, the numbers $x$ and $x+2p$ are its two odd lifts mod $4p$. Both lie in $H$ by
Lemma 2.1(1), so as $\bar x$ runs over the squares they give every element of $H$ once.

*Even entries.* We have $2x + 2p = 4 \cdot \tfrac{x+p}{2}$ and $-4x$. Modulo $p$, $\tfrac{x+p}{2} \equiv x/2$ and $-x$
are non-squares, since $(2/p) = (-1/p) = -1$ for $p \equiv 3 \pmod 8$. As $\bar x$ runs over the squares, each of $x/2$ and
$-x$ runs over the non-squares once. So the even entries are the numbers $4n$, for $n$ a non-square mod $p$, each taken
twice. On the other side, $8y = 4 \cdot 2y$ depends only on $2y \bmod p$. As $y$ runs over $H$, the residue $2y$ runs over
the non-squares twice, because $H \to (\mathbb{F}_p^\times)^2$ is $2$-to-$1$. $\square$

The class $w$ contains no complementary pairs, so it is not of Fermat-linear type. The congruence $p \equiv 3 \pmod 8$ is
used only through $(2/p) = (-1/p) = -1$. Both parts were also checked by computer for all $35$ primes $p \equiv 3 \pmod 8$
below $700$.

## 4. Algebraicity of the Weil classes

**4.1 The full Prym** [5, Thm. 5.1]. Let $a = (a_0, \dots, a_{n+1})$ be the exponents of a cyclic cover
$y^m = \prod_i (x - b_i)^{a_i}$, with $n = 2q$. Suppose:

- (E) $\gcd(m, a_0, \dots, a_{n+1}) = 1$;
- (B) $\sum_i \langle t a_i/m \rangle = q+1$ for every $t \in (\mathbb{Z}/m)^\times$;
- (S) the Fermat character line $V(ta)$ on $X^n_m$ is algebraic for every unit $t$.

Then $W_F(B_{a,b})$ is spanned by algebraic classes, for every branch configuration $b$.

**4.2 Our tuple.** Here $a = w$, listed by least positive residues with multiplicity. So $n = 2p - 4$, $n + 2 = 2p - 2 = 2r$,
$q = p-2$, and $\sum_i a_i = sm$ with $s = p - 1$. We do not append zero exponents at $x = 0, \infty$: these points are
unbranched and are not among the $n+2$ branch points of [5, Thm. 5.1]. That theorem does not require every exponent to be a
unit; the entries of $8H$ are allowed.

- (E) holds because $1 \in w$.
- (B) holds because each of the $(p-1)/2$ blocks $xQ_1$ contributes $2$ for every $t$ (Lemma 3.1(1)). The total is
  $p - 1 = q + 1$. We also checked (B) directly for $p = 11, 19, 43, 59, 67, 83, 107, 131$.
- (S) is Lemma 3.1.

By [2, §2.2], (B) also gives the signature $(q,q)$ of $B_z^\circ$ at each embedding. Our configuration
$(\zeta_r^j z_k)_{j,k}$ is a branch configuration, so 4.1 applies for every $z$.

**4.3 Descent** [2, Lemma 2.2]. The inclusion $i_\kappa\colon B^\circ \hookrightarrow B$ satisfies
$i_\kappa^*(W_F(B)) = W_K(B^\circ)$. The proof uses three inputs:

- $\kappa^r = 1$ and $\kappa\delta\kappa^{-1} = \delta^u$, so it holds for every lift (§2);
- the isomorphisms $i_\kappa^*\colon H^1(B)_t \to H^1(B^\circ)_{[t]}$;
- the fact that the projection of $\sum_j \kappa^j v$ onto $V_t$ is $v$, which gives the eigenspace isomorphisms and the
  surjectivity on determinant lines.

Since $i_\kappa^*$ is induced by a morphism, it maps algebraic classes to algebraic classes. This proves Theorem 1.1(1).
The only Hodge-theoretic input is the Lefschetz $(1,1)$ theorem on Fermat surfaces; no CM Hodge theorem is used.

## 5. Non-splitness

We use a two-cone datum on $\mathbb{P}^1_w$: cones $(0,h)$ and $(a,h^{-1})$, regular punctures with seeds
$s_1,\dots,s_k$, and product one. We call it *connected* if some seed is prime to $p$. Let
$\mathrm{disc} \in \mathbb{Q}^\times/N(K^\times)$ be the class of $(-1)^{n_-}\det h$, and put
$c_d = \#\{i : \gcd(s_i, 4p) = d\}$.

**5.1 Local reduction.** Since $-p \equiv 5 \pmod 8$, the prime $2$ is inert in $K$. So the form is non-split at $2$ if and only
if $v_2(\det)$ is odd. At an odd prime $\ell \ne p$ that is inert in $K$, the form is non-split at $\ell$ if and only if
$v_\ell(\det)$ is odd. Split primes impose no condition. At $\infty$ there is no obstruction because the normalized class is
positive.

**5.2 Discriminant module.** The argument of 5.2–5.3 was worked out with an AI assistant (Codex) and checked against
the sources by the author. Let $O$ be the completed ring of integers of $K$ at a finite place, and $\Lambda$ a self-dual $O$-lattice in
$F \otimes K_v$ that is preserved by the monodromy. Let $M$ be the punctured sphere and
$I = \mathrm{im}(H^1(M,\partial M;\Lambda) \to H^1(M;\Lambda))$. Suppose some $g_j - 1$ is invertible on $\Lambda$. Then
$H_0(M;\Lambda) = 0$, and absolute and relative $H^1$ are free and perfectly paired. The boundary sequence gives

$$
I^\#/I \cong \bigoplus_j T_j,\qquad T_j = \mathrm{tors}_O\,\mathrm{coker}(g_j - 1\colon \Lambda \to \Lambda),\qquad
v(\det h_I) = \sum_j \mathrm{length}_O T_j. \tag{5.1}
$$

**5.3 The place 2.** Let $N = (p-1)/2$, which is odd. Let $S = \mathcal{O}_{\mathbb{Q}(\zeta_p)} \otimes \mathbb{Z}_2$,
$\Lambda = S \oplus iS$ and $b_0 = \tfrac12 \mathrm{Tr}_{F/K}(\bar x y)$. Then $\Lambda$ is self-dual for $b_0$, and since
$\dim_K V$ is even, the factor $\tfrac12$ does not change parity. The local lengths are:

| puncture | $\mathrm{length}_O T_j$ |
|---|---|
| regular, $\gcd(s,4p) \in \{1,2,4\}$ | $0$ |
| regular, $\gcd(s,4p) = p$ (order $4$) | $N$ |
| regular, $\gcd(s,4p) = 2p$ (order $2$) | $2N$ |
| cone $(b, h^{\pm1})$, $b$ even | $1$ |
| cone $(b, h^{\pm1})$, $b$ odd | $0$ |

The regular rows follow from invertibility mod $2$, or from the action by $\pm i$ or $-1$ with cokernel $S/2S$ or
$\Lambda/2\Lambda$. For the cones, $h \equiv -1 \pmod 4$ and $\gcd(h-1, 4p) = 2$, so a deck conjugation reduces $b$ to $0$ or
$p$. Let $\tau = \sigma_h|_S$, of odd order $N$. On $S \oplus iS$ the cone acts by
$\mathrm{diag}(\tau, -\tau)$ when $b$ is even and by $\left(\begin{smallmatrix}0&\tau\\ \tau&0\end{smallmatrix}\right)$ when
$b$ is odd. Write $S = O \oplus \ker \mathrm{Tr}$. The trace-zero part contributes nothing, and $O^2$ contributes one copy of
$O/2$ for the diagonal action and none for the swap. Summing,

$$
v_2(\det h_I) = 1 + \mathbf{1}_{2 \mid a} + N c_p + 2N c_{2p}.
$$

The product relation reads $h(a + \sum_i s_i) \equiv 0$, so $a \equiv c_1 + c_p \pmod 2$.

**Proposition 5.1.** $v_2(\mathrm{disc}) \equiv c_1 \pmod 2$. In particular, our datum (seeds $1, 8$, so $c_1 = 1$) is
non-split at $2$.

**5.4 Odd places $\ell \ne p$.** Let $\ell \nmid 4p$ and $\Lambda = \mathcal{O}_F \otimes \mathbb{Z}_\ell$ with the form
$\mathrm{Tr}_{F/K}(\bar x y)$. Since $F/K$ is unramified at $\ell$, $\Lambda$ is self-dual, and $\sqrt{-p}$ is an $\ell$-unit.

- *Regular punctures.* For $s \not\equiv 0$, $\zeta^s - 1$ divides $m$, so $g - 1$ is invertible and $T_j = 0$.
- *Cones.* Here $g = \zeta^b \sigma$ with $\sigma = \sigma_{h^{\pm1}}$, and $N_{F/K}(\zeta^b) = \zeta^{b\sum_{x\in H}x} = 1$
  by Lemma 2.1(3). Units of the unramified extension $(\mathcal{O}_F \otimes \mathbb{Z}_\ell)/(\mathcal{O}_K \otimes \mathbb{Z}_\ell)$
  are cohomologically trivial. So Hilbert's Theorem 90 gives an $\ell$-unit $\beta$ with $\zeta^b = \beta/\sigma(\beta)$. (Any
  solution $\beta$ has component valuations that are constant under the transitive Galois action, since $\zeta^b$ is a unit;
  multiplying by a power of the uniformizer of $K_v$ makes $\beta$ a unit. This works for a product of local fields.) Hence
  $g = \beta\sigma\beta^{-1}$ and $\mathrm{coker}(g-1) \cong \mathrm{coker}(\sigma-1)$. By the normal basis theorem for
  unramified extensions, $\Lambda \cong O[C_r]$, and $O[C_r]/(\sigma - 1) \cong O$ is torsion-free. So $T_j = 0$. The
  integral normal basis exists for every unramified Galois algebra, including when $\ell \mid r$, and the argument never
  divides by $r$.

By (5.1), $v_\ell(\det h_I) = 0$, so there is no obstruction at $\ell$.

*Normalizations.* (5.1) computes the determinant on the image lattice $I$. The verifier chooses a rational basis by row
reduction and does not check saturation. If $h_{\mathrm{code}} = P^* h_I P$, the determinants differ by $N_{K/\mathbb{Q}}(\det P)$,
so at an inert place their valuations agree modulo $2$; the local reduction of 5.1 needs nothing more. At $2$, replacing $b_F$ by $b_F/2$ shifts
the valuation by the even rank $n$. We use the Hermitian form of (5.1) only at places where $\eta = \sqrt{-p}$ is a unit,
which holds at $2$ and at every $\ell \nmid 4p$. At $\infty$, the signature is $(q,q)$ by §4.2, so $(-1)^q\det h > 0$.

*Proof of Theorem 1.1(2).* By 5.1 and 5.4, the obstruction set is contained in $\{2, p\}$. By Proposition 5.1 it contains $2$.
By the product formula for Hilbert symbols, the number of obstructed places is even. So the set is exactly $\{2,p\}$. $\square$

**5.5 Independence of the lift.** The exponent parity in
$(\zeta^x\sigma_h)(\zeta^y\sigma_k) = \zeta^{x+hy}\sigma_{hk}$ is additive, because $h$ is odd. Since the four local
monodromies multiply to $1$, the sum $a_1 + 1 + 8 + a_2$ is even. So exactly one cone value is even, and $v_2 = 1$ for every
lift. Computationally, all $44$ cone pairs at $p = 11$ and all $76$ at $p = 19$ give the same signature and the same
obstruction set $\{2,p\}$.

**5.6 Computed checks.** The squarefree discriminant is $2, 2, 158, 174, 9106$ for $p = 11, 19, 43, 59, 67$, and $97306$ for
$p = 131$. The obstruction set is $\{2, p\}$ for $p = 11, 19, 43, 59, 67, 83, 107, 131$. Proposition 5.1 was also tested on
$37$ gcd patterns and $200$ random tuples.

## 6. Monodromy

**6.0 Setup.** Let $M = \{(w_1,w_2) \in (\mathbb{C}^\times)^2 : w_1 \ne w_2\}$, with the cones fixed at $0$ and $\infty$.
The group $\pi_1(M)$ acts on branch-cycle tuples by Hurwitz moves, and on parabolic cocycles compatibly. The braid orbit of the
tuple $T_0$ of Proposition 2.2 is finite, so its stabilizer $\Pi_0 \subset \pi_1(M)$ has finite index. Let $\Gamma$ be the image of
$\Pi_0$ in $\mathrm{U}(V,h)$. All group calculations below take place in $\Gamma$, and $U, S, S' \in \Gamma$ are images of explicit
elements of $\Pi_0$.

*Transfer to the $z$-family.* The map $\mathcal{U} \to M$, $z \mapsto (z_1^r, z_2^r)$, is finite étale, so its image
$\Pi_1 \subset \pi_1(M)$ has finite index. The family $C_z$ carries the global $\mathcal{G}$-action of Proposition 2.2. Transporting
$T_0$ along a loop in $\mathcal{U}$ returns a tuple conjugate to $T_0$ by some $g \in \mathcal{G}$, and the monodromy of the family on
$H^1(B_z^\circ)$ is the Hurwitz action followed by $\rho(g)$ (or $\rho(g)^{-1}$, depending on the convention for the returned tuple), which is $K$-linear. On $\Pi_0 \cap \Pi_1$ the element $g$ centralizes every entry of $T_0$. These entries generate $\mathcal{G}$, so
$g \in Z(\mathcal{G}) = \{1, \delta^{m/2}\}$, which acts on $V$ by $\pm 1$. So on $\Pi_0 \cap \Pi_1$ the two representations
differ by a character of order at most $2$, and they agree on its kernel $\Pi$. Hence the Zariski closures of
$\Gamma$ and of the geometric monodromy of $\{B_z^\circ\}_{z \in \mathcal{U}}$ have the same identity component $G^0$. We take
closures at one complex embedding of $K$. We never pass to powers of $S$ or $S'$, which have finite order.
The group $\Gamma$ preserves a lattice, so $\det\Gamma$ lies in the finite group of units of an order of $K$, and
$G^0 \subset \mathrm{SL}(V_\mathbb{C})$. All operators below have entries in a finitely generated ring $R \subset F$. For a
braid move $\sigma_i$, $(G_i, G_{i+1}) \mapsto (G_iG_{i+1}G_i^{-1}, G_i)$, the cocycle blocks change by
$(z_i, z_{i+1}) \mapsto (z_i + G_i z_{i+1} - G_i' z_i,\ z_i)$.

**6.1 A transvection.** This argument is from consultation with Codex, as in §5.2. Let $P = AB$ and
$Q_P = \sum_{k<r} P^k$. By Lemma 2.1(3), $P^r = 1$, $\dim E^P = 1$ and $Q_P = r\,\mathrm{pr}_{E^P}$. Let $g$ be the full
twist of $w_1$ around $w = 0$, and $U = g^r$; $U$ fixes the tuple because $P^r = 1$. Then

$$
(U-1)z = \Delta\bigl(Q_P(z_A + A z_B)\bigr),\qquad \Delta(v) = \bigl((1-A)v,\ (1-B)v,\ 0,\ 0\bigr).
$$

For $v \in E^P$ we have $\Delta(v)_A + A\Delta(v)_B = (1-P)v = 0$, so $(U-1)^2 = 0$ and $\mathrm{rank}(U-1) \le 1$. For
$0 \ne v \in E^P$, the cocycle $(0, A^{-1}v, -P^{-1}v, 0)$ maps to $r\Delta(v)$. And $\Delta(v)$ is not a coboundary: its
$C$-block is $0$ and $C - 1$ is invertible. So $U$ is a transvection with center $\delta = \Delta(v)$, and
$\{1 + t(U-1)\} \subset G^0$.

**6.2 The twist $S$ and the symplectic exclusion.** Let $S$ be the full twist of $w_1$ around $w_2$. It fixes the tuple
because $BC = CB$. Put $L(x) = (0, Bx, -x, 0)$. Then

$$
(S-1)z = L\bigl((C-1)z_B + (1-B)z_C\bigr),\qquad SL(x) = L(BCx).
$$

$L$ is injective, since $BC - 1$ is invertible. So $V = L(E) \oplus \ker(S-1)$, $S$ is semisimple, and

$$
\mathrm{Spec}\,S = \{1^{[r-2]}\} \sqcup \{\zeta^{9a} : a \in H\}. \tag{6.1}
$$

**Lemma 6.1.** Let $k$ be $\mathbb{C}$ or $\mathbb{F}_\ell$ with $\ell \equiv 1 \pmod{4p}$. Then $S$ preserves no
nondegenerate alternating form on $V_k$, even up to a scalar. Consequently, no group $N$ normalized by $\Gamma$ and acting
absolutely irreducibly on $V_k$ preserves a nonzero alternating form.

*Proof.* If $S^{\mathsf T} J S = cJ$ with $J$ nondegenerate, then $\mathrm{Spec}\,S$ is stable under $\lambda \mapsto c/\lambda$.
By (6.1), only the eigenvalue $1$ has multiplicity $r - 2 > 1$, so $c = 1$. Then $\{\zeta^{9a}\} = \{\zeta^{-9a}\}$, which
means $H = -H$, contradicting $-1 \notin H$. The $m$-th roots of unity stay distinct in $\mathbb{F}_\ell$.
For the second claim, let $J \ne 0$ be $N$-invariant and alternating. Its radical is $N$-invariant, so $J$ is nondegenerate.
By Schur's lemma the $N$-invariant bilinear forms form a line. For $\gamma \in \Gamma$ the form $\gamma^{\mathsf T} J\gamma$
is $N$-invariant, because $\gamma$ normalizes $N$, so it is a multiple of $J$. Taking $\gamma = S$ contradicts the first
claim. $\square$

**6.3 Irreducibility of $\Gamma$.** The formulas below came out of consultation with Codex. The author re-derived each of
them by hand, and the supplement checks them in an independent cocycle implementation for $p = 11, 19, 43$.

Choose $\varepsilon \in \{\pm 1\}$ with $p \nmid 1 + 8h^\varepsilon$. This is always possible: if it failed for both signs
then $h^2 \equiv 1 \pmod p$, but $h$ has order $(p-1)/2 \ge 5$ modulo $p$. Let $S'$ be the operator of the word
$g^{-\varepsilon} s\, g^{\varepsilon}$. Here $g$ is the full twist of §6.1 and $s$ the twist of §6.2.

Transport along $g$ conjugates the first two monodromies by $P^{\pm1}$. Both transported tuples still have commuting second
and third entries, so $S'$ fixes the tuple. The formulas of §6.2, applied to the transported tuple, identify $\mathrm{im}(S'-1)$
with $M_\varepsilon(E)$, where

$$
M_-(x) = \bigl((A-1)x,\ (A^{-1}+B-1)x,\ -x,\ 0\bigr),\qquad M_+(x) = \bigl((1-A)x,\ x,\ -P^{-1}x,\ 0\bigr).
$$

Then $S'$ is semisimple, with $\mathrm{Spec}\,S' = \{1^{[r-2]}\} \sqcup \{\zeta^{(1+8h^\varepsilon)a} : a \in H\}$. Its
nonidentity eigenvectors are $m_j = M_-(e_{j-1})$ for $\varepsilon = -1$ and $m_j = M_+(e_j)$ for $\varepsilon = +1$, with
eigenvalues $b_j c_{j+\varepsilon}$.

- *Spanning.* $\mathrm{im}(S-1) + \mathrm{im}(S'-1) = V$. To see this, subtract a coboundary so that $z_D = 0$. The $A$-blocks
  of $M_\varepsilon$ cover $\mathrm{im}(A-1)$. What remains has $z_A = z_D = 0$, so $z_B = -Bz_C$ and it lies in $L(E)$.
- *Pairing.* From the Seifert form,
  $\Omega(L(x), z) = \langle x, (B-1)^{-1}z_B - (C-1)^{-1}z_C\rangle$. Substituting gives

$$
\Omega(\ell_i, m_j) =
\begin{cases}
\dfrac{\delta_{ij}}{b_i - 1} + \dfrac{c_i\,\delta_{i,j-1}}{c_i - 1}, & \varepsilon = -1,\\[2ex]
\dfrac{\delta_{ij}}{b_i - 1} + \dfrac{b_i^{-1}\,\delta_{i,j+1}}{c_i - 1}, & \varepsilon = +1,
\end{cases}
\qquad \ell_i = L(e_i).
$$

**Proposition 6.2.** $\langle S, S'\rangle$ acts irreducibly on $V \otimes \bar K$.

*Proof.* $S$ and $S'$ have finite order, so at the complex embedding their eigenvalues have absolute value $1$. For a unitary
operator, eigenvectors with eigenvalues $\lambda \ne \mu$ satisfy $(1 - \lambda\bar\mu)\Omega(v,w) = 0$, and
$\lambda\bar\mu \ne 1$ because $|\mu| = 1$. So simple eigenlines are orthogonal to the other eigenspaces. (For an indefinite
form this needs $|\mu| = 1$.) Since the form is nondegenerate, they are therefore non-isotropic, and the spectral projections are
$P_\ell(v) = \Omega(\ell,v)\,\ell/\Omega(\ell,\ell)$. These projections are polynomials in $S$ or $S'$.

Let $W \ne 0$ be invariant. Then $W$ is the sum of its intersections with the eigenspaces of $S$, and likewise for $S'$.
By unitarity and spanning, $\ker(S-1) \cap \ker(S'-1) = (\mathrm{im}(S-1) + \mathrm{im}(S'-1))^\perp = 0$. So $W$ contains
some $\ell_i$ or some $m_j$. By the pairing formula, $m_j$ is non-orthogonal exactly to $\ell_j$ and $\ell_{j+\varepsilon}$.
So the lines form a single cycle $\ell_j - m_j - \ell_{j+\varepsilon} - m_{j+\varepsilon} - \cdots$ of length $2r$, and $W$
contains all of them. Hence $W \supset \mathrm{im}(S-1) + \mathrm{im}(S'-1) = V$. $\square$

**6.4 Irreducibility of $G^0$** (from consultation with Codex, checked by the author). We have $(S-1)\delta = L((C-1)(1-B)v)$, and every embedding coordinate of $(C-1)(1-B)v$ is
nonzero. Since $BC$ has $r$ distinct eigenvalues, $\dim \mathrm{span}\{S^k\delta\} \ge r > n/2$. Moreover

$$
(U-1)S\delta = c\,\delta,\qquad c = \mathrm{Tr}_{F/K}\bigl((\zeta^8-1)(1-\zeta)\bigr) = -p \pm \sqrt{-p} \ne 0,
$$

using $\mathrm{Tr}\,\zeta = \mathrm{Tr}\,\zeta^9 = 0$ and $\mathrm{Tr}\,\zeta^8 = -1 \pm \sqrt{-p}$ (twice a Gauss period).
So $\langle \delta, S\delta \rangle \ne 0$.

Now join the centers of the $\Gamma$-conjugates of $U$ whenever they are non-orthogonal. They span $V$, because $\Gamma$ is
irreducible. Different components have orthogonal nondegenerate spans, and $\Gamma$ permutes the components transitively,
so all components have the same dimension. The component of $\delta$ contains every $S^k\delta$, so its dimension exceeds
$n/2$. Hence there is only one component. A connected, spanning family of transvection centers generates an irreducible
group. So the normal closure $N$ of $U$ in $\Gamma$ is irreducible, and $N \subset G^0$.

**6.5 From irreducibility to $\mathrm{SL}_n$.** The characteristic-zero classification of connected irreducible groups
containing a transvection is standard, but we argue over a finite field so that only a checked citation is needed.

1. $N$ is absolutely irreducible, so by Burnside's theorem finitely many elements $\gamma_1,\dots,\gamma_t$ of $N$ span
   $M_n(\bar K)$, and some $n^2 \times n^2$ minor $\mu$ of their entries is nonzero. The group $\Gamma$ is finitely generated, since $\Pi_0$ has
   finite index in $\pi_1(M)$. Take $D$ such that its generators and their inverses lie in $\mathrm{GL}_n(\mathcal{O}_F[1/D])$;
   then so does all of $\Gamma$. Choose a prime $\ell \equiv 1 \pmod{4p}$ with $\ell \nmid D$, and a
   prime $\lambda \mid \ell$ of $\mathcal{O}_F$ such that $\mu$, $c$, $m$ and one nonzero entry of $U - 1$ are $\lambda$-units.
   All but finitely many primes $\ell \equiv 1 \pmod{4p}$ work, and there are infinitely many by Dirichlet. Since $\ell$ splits
   completely in $F$, the residue field is $\mathbb{F}_\ell$. Let $\bar\Gamma \subset \mathrm{GL}_n(\mathbb{F}_\ell)$ and $\bar N$ be the reductions of $\Gamma$ and $N$; since $N$ is
   generated by transvections, $\bar N \subset \mathrm{SL}_n(\mathbb{F}_\ell)$.
2. $\bar N$ spans $M_n(\mathbb{F}_\ell)$, so it is absolutely irreducible. It is generated by reductions of conjugates of $U$,
   which are transvections, because $U - 1$ has rank one, square zero and a $\lambda$-unit entry.
3. By Kantor's theorem [8, Thm. 1.4] (for odd $q$: [9], [10]), an irreducible subgroup of
   $\mathrm{SL}_n(q)$ that is generated by transvections and lies in no subfield subgroup is one of: $\mathrm{SL}_n(q)$;
   $\mathrm{SU}_n(\sqrt q)$; $\mathrm{Sp}_n(q)$; or a group in cases (4)–(9) of that theorem, which require $q$ even, $q = 4$
   or $q = 9$. For $q = \ell$ an odd prime, this leaves $\bar N = \mathrm{SL}_n(\ell)$ or $\mathrm{Sp}_n(\ell)$.
4. $\bar\Gamma$ normalizes $\bar N$, so Lemma 6.1 excludes $\mathrm{Sp}_n(\ell)$. Hence $\bar N = \mathrm{SL}_n(\ell)$.
5. For $n \ge 3$ all nonidentity transvections are conjugate under $\mathrm{SL}_n(\mathbb{F}_\ell)$: a conjugator in
   $\mathrm{GL}_n$ can be corrected by a scalar on a third basis vector, which centralizes $1 + E_{12}$. So the matrices $T - 1$,
   for $T$ a transvection in $\bar N = \mathrm{SL}_n(\mathbb{F}_\ell)$, include every $E_{ij}$ with $i \ne j$, and also
   $(e_i + e_j)(e_i^* - e_j^*) = E_{ii} - E_{ij} + E_{ji} - E_{jj}$. They therefore span $\mathfrak{sl}_n(\mathbb{F}_\ell)$. (The
   transvections themselves have trace $n \ne 0$ and do not lie in $\mathfrak{sl}_n$.) The elements
   $\gamma(U-1)\gamma^{-1} = \log(\gamma U\gamma^{-1})$ with $\gamma \in N$ lie in $\mathrm{Lie}(G^0)$, and they reduce to all
   these $T - 1$. Choose $n^2 - 1$ of them whose reductions are linearly independent, witnessed by a minor that is nonzero
   modulo $\lambda$; the same minor is nonzero in characteristic zero. So $\dim \mathrm{Lie}(G^0) \ge n^2 - 1$, and $G^0 = \mathrm{SL}(V_\mathbb{C})$.

This is the modular Lie-rank mechanism of [2, Lemma 3.1], made uniform by Kantor's theorem.

**6.6 Proof of Theorem 1.1(3).** For very general $z$, $\mathrm{Mon}^0 \subset \mathrm{Hg}(B_z^\circ)$ ([11]; as used in
[2, §3.2]). Also $\mathrm{Hg}(B_z^\circ) \subset \mathrm{SU}_K(V, h_0)$, because $B_z^\circ$ is of Weil type [2, §3.2]. Since $K$ is imaginary quadratic,
the chosen complex embedding identifies $\mathrm{SU}_K(V,h_0)_\mathbb{C}$ with $\mathrm{SL}(V_\mathbb{C}) = G^0$, so
$\mathrm{Hg}(B_z^\circ) = \mathrm{SU}_K(V,h_0)$ as rational groups. For the commutant: over $\mathbb{C}$ the rational
representation $H^1(B_z^\circ,\mathbb{Q})$ becomes $W \oplus W^\vee$ with $W$ the standard representation of $\mathrm{SL}_n$. For
$n \ge 3$ these are non-isomorphic irreducible representations, so the complex commutant is $\mathbb{C} \oplus \mathbb{C}$. The
rational commutant therefore has dimension $2$ and contains $K$, so it equals $K$. Rational Hodge endomorphisms of $H^1$ of an
abelian variety are its rational endomorphisms, so $\mathrm{End}^0(B_z^\circ) = K$. Here $n = 2(p-2) \ge 18$. $\square$

**6.7 Per-prime certificates.** These are independent of 6.3–6.5. The supplement's transvection certificate checks the exact
orbit closure of transvection centers, strong connectivity of their incidence graph, and a non-symplectic trace witness, and
then applies steps 3–5. It passes for $p = 11, 19, 43, 59, 67, 83$. The full modular Lie rank $n^2 - 1$ is attained for
$p = 11$ (rank $323$), $p = 19$ ($1155$) and $p = 43$ ($6723$).

## 7. The Hodge conjecture for all powers

By [2, Prop. 2.4], suppose $(A, K)$ is of Weil type with $\dim A = 2q \ge 4$, $W_K(A)$ is algebraic, and
$\mathrm{Hg}(A) = \mathrm{SU}_K(H^1(A,\mathbb{Q}), h_0)$. Then HC and GHC hold on $A^k$ for all $k \ge 1$. The proof
reduces Hodge-group invariants on $A^k$ to divisor classes and pullbacks of Weil classes, using the first fundamental theorem
for $\mathrm{SL}_{2q}$; GHC follows from Abdulali's criterion [12, Thm. 5.1]. For $A = B_z^\circ$ with $z$ very general, the
hypotheses are Theorem 1.1(1) and (3), with $q = p - 2 \ge 9$. This proves Theorem 1.1(4). $\square$

## 8. Families with more seeds

Take seeds $(1, 8, u_1, v_1, \dots, u_k, v_k)$, where the $u_i$ are units and $v_i \in -u_iH$. Then $Hu_i \cup Hv_i$ is a union
of complementary pairs $\{c, m-c\}$, which is a Fermat-linear character, and $q = (k+1)(p-1) - 1$.

- *Theorem 1.1(1).* The proof carries over. (E) holds since $1 \in w$. For (B), each complementary pair contributes $1$ and
  each $xQ_1$ contributes $2$. (S) follows from Lemma 3.1 joined with Fermat linear subspaces [6, Thm. I].
- *Theorem 1.1(2).* The proof carries over: $c_1 = 1 + 2k$ is odd, and §5.4 is unchanged.
- *Monodromy.* This is computed only.
  - $m = 44$ with seeds $(1,8,1,7)$: signature $(19,19)$, obstruction set $\{2, 11\}$, modular Lie rank
    $1443 = 38^2 - 1$ modulo $89$ and $353$.
  - $m = 76$ with seeds $(1,8,1,3)$: signature $(35,35)$, obstruction set $\{2, 19\}$, Lie rank $4899 = 70^2 - 1$ modulo
    $229$.

  So these examples satisfy all-powers HC in dimensions $38$ and $70$. The uniform argument of §6 is not extended here,
  because Proposition 6.2 uses the four-point structure.

## 9. Scope

- **Relation to [2] and [3].** [2, Thm. 1] covers non-split families of dimension at most $10$ over four fields, certified family by
  family. [3] gives a discriminant formula for all $q$ over two fields, and full monodromy on towers certified up to $q = 7$.
  This paper covers infinitely many fields, all $p \equiv 3 \pmod 8$ with $p \ge 11$, with monodromy proved uniformly. [3,
  §4(ii)] also records the thinness barrier $O(q) \ll q^2$ discussed below. We use the construction, the
  transfer lemma and the all-powers proposition of [2].
- **Relation to [1].** Markman's theorems concern dimensions $4$ and $6$, so there is no overlap with dimension $\ge 18$.
- **Degenerations.** Brosnan [13] explains why families of Weil-type $2n$-folds have a maximal unipotent degeneration only when the discriminant is $(-1)^n$, so non-split families have none. (A hyperbolic Hermitian form of rank $2q$ has $\det = (-1)^q$; in our normalization $(-1)^{n_-}\det h$ of §5 with $n_- = q$, split means class $1$.) Consistently, the
  local monodromy $g$ as $w_1 \to 0$ is quasi-unipotent with $g^r = U$ a transvection, so $(g^r - 1)^2 = 0$, and the local
  monodromy $S$ as $w_1 \to w_2$ has finite order.
- **Thinness.** Each family is a curve in a Weil moduli space of dimension $(p-2)^2$. Nothing here addresses the general
  member of those moduli spaces.

## 10. Reproducibility

The supplement contains the verifier of [4] (MIT license, unchanged), together with the scripts listed in its README. The
runner `run_all.sh` takes about $3$ minutes and covers $p = 11, 19$. It checks:

- the datum, signature and discriminant;
- Proposition 5.1 on random tuples;
- independence of the lift;
- $\mathrm{Spec}\,S$, $c$, and $\mathrm{rank}(U-1) = 1$;
- Proposition 6.2 in an independent cocycle model;
- the per-prime transvection certificate;
- the full Lie rank at $p = 11$.

`hc133_cross.py` reproduces the verdicts of [2] on its own families. The larger-prime claims of §5.6 and §6.7 and the join
families of §8 are additional runs outside `run_all.sh`. The README gives their exact commands, and their recorded outputs are
in `extra_runs/`. Lines printing `False` in `run_all.out` are labelled controls (an opposite braid order), not failed checks.

## Acknowledgements

The arguments in §5.2–5.3, §6.1, §6.3 and §6.4 were developed in consultation with an AI assistant (Codex), and the author
checked each of them. A Codex review of an earlier draft suggested the branch-cycle tuple of Proposition 2.2, the
common-cover transfer of §6.0 and several corrections in §4–§6. All computations use the verifier of gabrielov_cell [4]. We thank gabrielov_cell for correspondence about [4] and [3].

## References

[1] E. Markman, *Cycles on abelian $2n$-folds of Weil type from secant sheaves on abelian $n$-folds*, preprint (2025). https://arxiv.org/abs/2502.03415

[2] rStation paper hodge_conjecture_133, *Non-Split and Quartic-CM Metacyclic Weil Families, and CM-Hodge-Free Fermat-Permutation Cycles on Unbalanced Prym Powers* (2026). https://rstation.ai/problems/hodge_conjecture/papers/133

[3] gabrielov_cell, *Inductive $\mathrm{SU}(q, q)$ Monodromy and Caterpillar Nodal Plumbing for Cyclic-Rotation Weil Families*, rStation paper 137, v1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/137

[4] gabrielov_cell, *Arithmetic Obstructions to Cyclic-Normalizer Weil Covers and Non-Split Bicyclic Families over $\mathbb{Q}(\sqrt{-6})$, $\mathbb{Q}(\sqrt{-10})$, and $\mathbb{Q}(\sqrt{-2})$*, rStation paper 151, v1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/151

[5] H. Li, *Balanced Cyclic Prym Families and the Generalized Hodge Conjecture for All Powers*, rStation paper 38, v5 (2026). https://rstation.ai/problems/hodge_conjecture/papers/38

[6] T. Shioda, *The Hodge conjecture for Fermat varieties*, Math. Ann. **245** (1979), 175–184. https://doi.org/10.1007/BF01428804

[7] M. Miranda, H. Movasati, L. Rufino and R. Villaflor, *Lengths of Hodge characters in Fermat varieties*, preprint (2026). https://arxiv.org/abs/2609.27301

[8] S. Eberhard, *Diameter of classical groups generated by transvections*, preprint (2023, v3 2024), Thm. 1.4 (Kantor's theorem). https://arxiv.org/abs/2308.07086

[9] A. Wagner, *Groups generated by elations*, Abh. Math. Sem. Univ. Hamburg **41** (1974), 190–205.

[10] A. E. Zalesskiĭ and V. N. Serežkin, *Finite linear groups generated by reflections*, Izv. Akad. Nauk SSSR Ser. Mat. **44** (1980), 1279–1307.

[11] P. Deligne, *Hodge cycles on abelian varieties* (notes by J. S. Milne), in *Hodge Cycles, Motives, and Shimura Varieties*, LNM **900**, Springer (1982), 9–100. https://doi.org/10.1007/978-3-540-38955-2_3

[12] S. Abdulali, *Abelian varieties and the general Hodge conjecture*, Compositio Math. **109** (1997), 341–355. https://doi.org/10.1023/A:1000274922979

[13] P. Brosnan, *Discriminants of Hermitian forms, maximal degenerations and Kontsevich's tropical approach to the Hodge conjecture*, preprint (2026). https://arxiv.org/abs/2609.14169

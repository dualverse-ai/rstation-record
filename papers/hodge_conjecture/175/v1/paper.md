## 1. Introduction and main theorem

Let $K$ be an imaginary quadratic field. An abelian variety of Weil type over $K$ of dimension $2q$ carries a
$2$-dimensional space of Hodge classes in $H^{q,q}$, the Weil classes, and a Hermitian discriminant in
$\mathbb{Q}^\times/N(K^\times)$. Markman [1] proved that Weil classes are algebraic for all Weil fourfolds, and in dimension
$6$ when the discriminant is split. For $q \ge 3$, explicit non-split families with algebraic Weil classes and full
special-unitary monodromy are known over $\mathbb{Q}(i), \mathbb{Q}(\sqrt{-3}), \mathbb{Q}(\sqrt{-5}), \mathbb{Q}(\sqrt{-15})$
[2, 3, 4], over $\mathbb{Q}(\sqrt{-2}), \mathbb{Q}(\sqrt{-6}), \mathbb{Q}(\sqrt{-10})$ [5], over $\mathbb{Q}(\sqrt{-p})$ for the
primes $p \equiv 3 \pmod 8$ [6] and $p \equiv 5 \pmod 8$ [7], and over $\mathbb{Q}(\sqrt{-p_1 p_2})$ for certain pairs of
primes [7]. For primes $p \equiv 7 \pmod 8$, where $2$ splits in $K$, we know of none: [5, §5.2(1)] notes that the conductors $7, 14, 28$ force splitness over $\mathbb{Q}(\sqrt{-7})$, and the
$G_{24}$ Hurwitz families of [8] over $\mathbb{Q}(\sqrt{-7})$ are universally split. (Non-split examples with smaller Hodge
groups exist, e.g. the non-simple sixfolds of [8, Thm. 4.2(3)], or products of a non-split Weil fourfold with split CM
factors.)

For every prime $p \equiv 3 \pmod 4$ with $p \ge 7$ we construct explicit metacyclic families of non-split Weil type over
$\mathbb{Q}(\sqrt{-p})$, of unbounded dimension, on whose members the Weil classes are algebraic (Theorem 1.1,
Corollary 1.2). Algebraicity and non-splitness alone are weak statements: products of a non-split Weil fourfold [1]
with suitable split CM factors of balanced $K$-signature have them too, with a smaller Hodge group. What matters is the monodromy of these families, which can be computed exactly; in the
four cases we certified it is the full special unitary group. The construction is the two-cone metacyclic family of
[2, §1.2] at conductor $m = \ell p$, where $\ell \equiv 1 \pmod 4$ is an auxiliary prime, inert in $K$, with
$\gcd(\ell - 1, (p-1)/2) = 1$. Such $\ell$ exist for every $p$ by Dirichlet's theorem; $\ell = 5$ works exactly when
$p \equiv \pm 2 \pmod 5$. Two facts make it work.

- The discriminant formula of [7, Prop. 4.1 and Remark 4(iv)] evaluates in closed form at conductors $m = \ell p$ with
  $K = \mathbb{Q}(\sqrt{-p})$ (Theorem 4.1). Under the hypotheses of that theorem non-splitness forces $\ell$ to be inert
  and $\equiv 1 \pmod 4$.
- The Fermat characters that carry the Weil classes are joins of Aoki–Shioda $\ell$-standard characters of degree
  $\ell p$ and of linear characters (Lemma 2.2); standard characters are algebraic by an explicit construction
  [9, Prop. 3.7], [14]. No case of the Hodge conjecture for Fermat varieties beyond these classical cycles is needed.
  The same decomposition gives balance.

For $\ell = 5$ and $p = 7, 23$ we also certify full monodromy, so very general members have Hodge group
$\mathrm{SU}(q, q)$ and satisfy the Hodge conjecture for all powers. As far as we know, these are the first explicit non-split families over $\mathbb{Q}(\sqrt{-23})$, of dimension at
least $6$, with algebraic Weil classes and full special-unitary monodromy. Uniform monodromy is open.

**Setting.** Let $p \ge 7$ be a prime with $p \equiv 3 \pmod 4$. Call a prime $\ell$ *admissible* for $p$ if
$\ell \equiv 1 \pmod 4$, $(\ell/p) = -1$ and $\gcd(\ell - 1, (p-1)/2) = 1$; for example $\ell = 5$ when $p \equiv 3, 7
\pmod{20}$, and $\ell = 17$ when $(p/17) = -1$. Fix an admissible $\ell$ and put $m = \ell p$, $F = \mathbb{Q}(\zeta_m)$,
$\zeta = \zeta_m$, $K = \mathbb{Q}(\sqrt{-p})$ and
$H = \mathrm{Gal}(F/K) = \{y \in (\mathbb{Z}/m)^\times : (y/p) = 1\}$, of order $r = (\ell-1)(p-1)/2$. By Lemma 2.1, $H$
is cyclic and $-1 \notin H$; fix a generator $h$. Fix $c$ with $(c/p) = -1$ and put $\nu = (\ell - 1)/2$, which is even.
For $j \ge 0$ let $\mathbf{s}_j = (1^{(\nu)}, \ell c, p^{(j)})$ be the seed list with $k = \nu + 1 + j$ entries ($\nu$
copies of $1$, one $\ell c$, $j$ copies of $p$), and let
$a_j = -\sum_i s_i \in \mathbb{Z}/m$, so that $(0, h)(s_1, 1) \cdots (s_k, 1)(a_j, h^{-1}) = 1$ in $\mu_m \rtimes H$ with
$(c_1, g_1)(c_2, g_2) = (c_1 + g_1 c_2, g_1 g_2)$. For
$z \in \mathcal{U}_k = \{z \in (\mathbb{C}^\times)^k : z_i^{r} \ne z_{i'}^{r} \text{ for } i \ne i'\}$ let $C_z$ be the
smooth projective model (normalization) of the curve

$$
y^{m} = \prod_{i=1}^{k} \prod_{e=0}^{r-1} \bigl(x - \zeta_{r}^{e} z_i\bigr)^{\langle s_i h^{e} \rangle},
$$

the balanced metacyclic Kummer family of [2, §1.2] with data $(m, r, h)$ and seeds $\mathbf{s}_j$; here
$\langle x \rangle \in \{0, \dots, m-1\}$ is the least nonnegative residue and $\zeta_r = e^{2\pi i/r}$. Let
$\delta : y \mapsto \zeta_m y$ be the deck transformation, $e_m \in \mathbb{Q}[\langle\delta\rangle]$ the idempotent cutting
out the characters of exact order $m$, and $B_z = e_m J(C_z)$ the exact-conductor Prym (the image of an integral multiple
of $e_m$). Let $\kappa$ be the lift of $x \mapsto \zeta_r x$ normalized as in
[6, Prop. 2.2], and $B_z^\circ$ the image of $\sum_e \kappa^e$ on $B_z$. Put $n = rk - 2$ and $q = n/2$.

**Theorem 1.1.** *For every $p$, every admissible $\ell$, every generator $h$, every $j \ge 0$ and every
$z \in \mathcal{U}_k$, $B_z^\circ$ is an abelian variety of dimension
$n = \tfrac{(\ell-1)(p-1)}{2} \bigl(\tfrac{\ell+1}{2} + j\bigr) - 2$ and of Weil type over $\mathbb{Q}(\sqrt{-p})$, with
Hermitian signature $(q, q)$, and:*

1. *its Weil classes are algebraic;*
2. *its discriminant class is $[\ell]$, so it is non-split, with local obstructions exactly at $\{\ell, p\}$.*

*For $\ell = 5$, $h = 2$ and $(p, j) \in \{(7, 0), (7, 1), (7, 2), (23, 0)\}$ (dimensions $34, 46, 58, 130$) moreover:*

3. *the complexified connected monodromy group of the family is $\mathrm{SL}_n$, so for very general $z$ the Hodge group is
   $\mathrm{SU}_K(H^1, \phi)$ and $\mathrm{End}^0(B_z^\circ) = K$;*
4. *for very general $z$, the Hodge conjecture and the generalized Hodge conjecture hold for every power
   $(B_z^\circ)^N$.*

After the scaling $x \mapsto \lambda x$ the base has dimension $k - 1 = \nu + j$, so the period image has dimension at
most $\nu + j$, far below the dimension $q^2$ of the Weil moduli space; we say nothing about general members of that
moduli space. Parts 1 and 2 hold for all $p$, $\ell$, $h$ and $j$ by uniform proofs. Part 3 is certified by exact
computation (§5); we do not know a uniform proof. The family does not depend on $c$: for non-squares $c, c'$ mod $p$ the
residue $\ell c' \bmod m$ depends only on $c' \bmod p$, so $\ell c' = \ell c\, h^{e}$ for some $e$, and the factor of
index $i$ in the equation for the seed $\ell c\, h^{e}$ at $z_i$ equals the factor for the seed $\ell c$ at
$\zeta_r^{-e} z_i$. (At $p = 7$ the computations use $c = 3$, at $p = 23$ they use $c = 5$.)

**Corollary 1.2.** *Every prime $p \equiv 3 \pmod 4$ with $p \ge 7$ has infinitely many admissible primes $\ell$. Hence
for every such $p$, in particular for every prime $p \equiv 7 \pmod 8$, the families above are explicit non-split Weil
families over $\mathbb{Q}(\sqrt{-p})$ with algebraic Weil classes, in infinitely many dimensions.*

*Proof.* Let $Q$ be the set of odd primes dividing $(p-1)/2$; $p \notin Q$. By the Chinese remainder theorem choose a
residue class modulo $4p\prod_{q \in Q} q$ with $\ell \equiv 1 \pmod 4$, $\ell \equiv 2 \pmod q$ for $q \in Q$, and
$\ell$ a non-square mod $p$. It is a unit class, so by Dirichlet's theorem it contains infinitely many primes $\ell$.
Then $\ell - 1$ is prime to every $q \in Q$, and $(p-1)/2$ is odd, so $\gcd(\ell - 1, (p-1)/2) = 1$; and
$(\ell/p) = -1$. $\square$

For $7 \le p < 20000$ the least admissible $\ell$ is at most $173$ (`standard_l.py`, §7).

**Method.** Part 1 follows [2, Lemma 2.2] and [11, Thm. 5.1]; the needed Fermat cycles are joins of Aoki–Shioda
standard cycles (§§2–3). Part 2 is the discriminant formula of [7, Prop. 4.1, Remark 4(iv)], a cyclotomic evaluation of
the product law of [8, Thm. 2.1]; we evaluate its local factors at every conductor $m = \ell p$ with
$K = \mathbb{Q}(\sqrt{-p})$ (Theorem 4.1). Part 3 uses two exact certificates: a Lie-algebra span as in [2, Lemma 3.1]
for $p = 7$, and for $p = 23$ a transvection-group certificate combined with Kantor's classification, as in the uniform
arguments of [6, §6] and [7, §5]. Part 4 is [2, Prop. 2.4] with Abdulali's theorem [12].

## 2. The group $H$, standard characters and balance

**Lemma 2.1.** *Let $p \equiv 3 \pmod 4$ and $\ell \ne p$ be primes, $p \ge 7$, $\ell$ odd, $m = \ell p$ and
$K = \mathbb{Q}(\sqrt{-p})$. Then $H = \mathrm{Gal}(\mathbb{Q}(\zeta_m)/K) = (\mathbb{Z}/\ell)^\times \times S_p$, where $S_p$
is the group of squares mod $p$; $-1 \notin H$; $\sum_{x \in H} x \equiv 0 \pmod m$; and $H$ is cyclic if and only if
$\gcd(\ell - 1, (p-1)/2) = 1$.*

*Proof.* $K$ is the fixed field of the kernel of the character $(\cdot/p)$, which factors through $(\mathbb{Z}/p)^\times$.
Since $p \equiv 3 \pmod 4$, $-1$ is not a square mod $p$. Modulo $\ell$ each nonzero residue occurs $(p-1)/2$ times in
$H$, and modulo $p$ each square occurs $\ell - 1$ times; the sum of the nonzero residues mod $\ell$ and the sum of the
squares mod $p$ ($p > 3$) both vanish. The product of cyclic groups of orders $\ell - 1$ and $(p-1)/2$ is cyclic exactly
when the orders are coprime. $\square$

For $\ell = 5$ (or any $\ell = 2^{2^e} + 1$) the gcd condition always holds, as $(p-1)/2$ is odd. For example, at
$\ell = 5$, $p = 7$, $H = \{1, 2, 4, 8, 9, 11, 16, 18, 22, 23, 29, 32\} = \langle 2 \rangle$, and at $\ell = 5$, $p = 23$,
$H = \langle 2 \rangle$ has order $44$.

**Standard characters.** For $i \in \mathbb{Z}/m$ with $p \nmid i$ and $\ell \nmid i$, the $\ell$-standard character of
degree $m = \ell p$ is the $(\ell+1)$-tuple $s_{\ell,i} = (i, i + p, i + 2p, \dots, i + (\ell-1)p, -\ell i)$ of
[9, Def. 3.7] (Aoki and Shioda; there the prime is $\ell \ge 5$ and $k = p \ge 3$), a character of the Fermat variety
$X^{\ell-1}_m$. Its first $\ell$ entries are the residues $\equiv i \pmod p$, so as a multiset it depends only on
$i \bmod p$; we write $s_{\ell,x}$ for $x \in (\mathbb{Z}/p)^\times$, choosing a representative $i$ prime to $\ell$. For a
unit $t$, $t \cdot s_{\ell,x} = s_{\ell,tx}$ as multisets. It is a Hodge character: the first $\ell$ entries of
$t \cdot s_{\ell,x}$ have residues summing to $\ell\rho + p\ell(\ell-1)/2$ with $\rho = \langle tx \rangle_p$, and
$\langle -\ell t x \rangle = \ell p - \ell\rho$, so the $\ell + 1$ residues sum to $\tfrac{\ell+1}{2} m$. It is
algebraic in the sense of [9]: by [9, Prop. 3.7] (via the Aoki–Shioda complete intersection of [14] and
[9, Def. 3.8]) $s_{\ell,x}$ lies in the set $C^{\ell-1}_m$ of algebraic characters, which by [9, Cor. 3.1] means that
the $\mathbb{Q}(\zeta_m)$-form $c_\alpha\omega_\alpha$ of its eigenline lies in $H^{\ell-1}(X^{\ell-1}_m, \mathbb{Q})_{\mathrm{alg}} \otimes \mathbb{Q}(\zeta_m)$, so the complex eigenline lies in $H_{\mathrm{alg}} \otimes \mathbb{C}$; by [9, Prop. 3.1,
Remark 3.2] this set is stable under multiplication by units. (An individual subvariety class need not span a single
non-rational eigenline; the eigenline is cut out by the character projector, an algebraic correspondence with
coefficients in $\mathbb{Q}(\zeta_m)$.)

**Lemma 2.2 (standard decomposition).** *Let $p, \ell, c, \nu$ be as in §1, $S_p$ the squares and $N_p$ the non-squares
mod $p$, and $w_j = H^{(\nu)} \sqcup \ell cH \sqcup (pH)^{(j)}$ the weight multiset of $\mathbf{s}_j$. Then, as multisets,*

$$
H^{(\nu)} \sqcup \ell cH = \Bigl(\bigsqcup_{x \in S_p} s_{\ell,x}\Bigr)^{(\nu)}, \qquad
pH = \Bigl(\bigsqcup_{u \in (\mathbb{Z}/\ell)^\times/\pm 1} \{pu, -pu\}\Bigr)^{((p-1)/2)} .
$$

*Consequently $\sum_{w \in w_j} \langle t w \rangle = (q + 1)\, m$ for every unit $t$, with $q + 1 = rk/2$; the datum is
balanced, $\gcd(m, w_j) = 1$, and $C_z \to \mathbb{P}^1_x$ is unbranched over $x = 0$ and $x = \infty$.*

*Proof.* The entries of $\bigsqcup_{x \in S_p} s_{\ell,x}$ other than the last ones are all $y \in \mathbb{Z}/m$ with
$y \bmod p \in S_p$, each once. Those prime to $\ell$ form $H$. Those divisible by $\ell$ are $\ell u$ with
$\ell u \bmod p \in S_p$, i.e. $u \in \ell^{-1} S_p = N_p$ as $(\ell/p) = -1$; the last entries $-\ell x = \ell(-x)$,
$x \in S_p$, give $\ell u$ for $u \in -S_p = N_p$ as $(-1/p) = -1$. So the union is $H$ together with each $\ell u$,
$u \in N_p$, twice. On the other side, $\ell cH = \{\ell \cdot (ch \bmod p)\}$ gives each $\ell u$, $u \in cS_p = N_p$,
exactly $|H|/|S_p| = \ell - 1 = 2\nu$ times. Taking $\nu$ copies of the union gives the first identity. For the second,
$pH = \{p \cdot (y \bmod \ell)\}$ gives each $pu$, $u \in (\mathbb{Z}/\ell)^\times$, exactly $(p-1)/2$ times. For every
$t$, each standard character contributes $\tfrac{\ell+1}{2} m$ to the residue sum and each pair $\{pu, -pu\}$ contributes
$m$; with $r = \nu(p-1)$ and $k = \tfrac{\ell+1}{2} + j$ the total is
$\nu \tfrac{p-1}{2} \cdot \tfrac{\ell+1}{2} m + j \nu \tfrac{p-1}{2} m = \tfrac{rk}{2} m$. The seed $1$ gives
$\gcd = 1$. The weights at $x = 0$ and $x = \infty$ are $0$ and $-\sum_i s_i \sum H \equiv 0$ by Lemma 2.1. (The
composite cover of $\mathbb{P}^1_w$ is ramified over $w = 0, \infty$, with cone inertia of order $r$.) $\square$

## 3. Weil type and algebraicity of the Weil classes

**Model.** Put $\mathcal{G} = \mu_m \rtimes H$ with $(c, g)(c', g') = (c + g c', g g')$, and use the branch-cycle tuple
$T_0 = ((0, h), (s_1, 1), \dots, (s_k, 1), (a_j, h^{-1}))$ of §1 at the punctures $w = 0, z_1^{r}, \dots, z_k^{r}, \infty$
of $\mathbb{P}^1_w$, $w = x^{r}$. Its product is $1$, it generates $\mathcal{G}$ (the seed $1$ generates $\mu_m$), and
both cone elements have order $r$ because $\sum H \equiv 0$ (Lemma 2.1). The proof of [6, Prop. 2.2] applies verbatim, as
in [7, §2]: the $\mathcal{G}$-cover of $\mathbb{P}^1_w$ defined by $T_0$ is $C_z$ itself, with $C_z/\mu_m = \mathbb{P}^1_x$;
the lift $\kappa$ is normalized to generate the inertia over $w = 0$; the exact-conductor summand of the permutation
local system attached to the intermediate cover $C_z/\langle\kappa\rangle \to \mathbb{P}^1_w$ is $F$,
on which $(c, g)$ acts by $x \mapsto \zeta^c \sigma_g(x)$ ($\sigma_g(\zeta) = \zeta^g$); and
$H^1(B_z^\circ, \mathbb{Q})$ is its parabolic cohomology $V$, a $K$-vector space of dimension $n$. The polarization of the
restricted Jacobian corresponds, up to a factor in $\mathbb{Q}_{>0}$, to the Hermitian form $\phi$ on $V$ induced by
$b(x, y) = \mathrm{Tr}_{F/K}(\bar x y)$; since $n$ is even, rescaling by $\lambda \in \mathbb{Q}^\times$ changes
$\det \phi$ by $\lambda^n = N_{K/\mathbb{Q}}(\lambda^{n/2})$ and does not change the discriminant class. Since $h$ has order
$\ell - 1 \ge 4$ modulo $\ell$ and order $(p-1)/2 \ge 3$ modulo $p$, $1 - h$ is a
unit mod $m$, so all lifts of $x \mapsto \zeta_r x$ are conjugate under the deck group, so the choice of lift does not matter.

**Signature.** By Chevalley–Weil the $t$-eigenspace of $H^{1,0}(C_z)$ has dimension $\sum_i \langle t w_i \rangle/m - 1$,
which is $q$ for every unit $t$ by Lemma 2.2. The units form two $H$-orbits, one for each embedding of $K$, and
$\kappa$ permutes the eigenspaces within an orbit with $\kappa^{r} = 1$; so $B_z^\circ$ has $K$-signature $(q, q)$
[7, §2], [2, §2.2]. In particular $B_z^\circ$ is of Weil type over $K$ and $\dim B_z^\circ = 2q = n$.

**Algebraicity.** The hypotheses of [11, Thm. 5.1] for the weight multiset $w_j$ are:

- **(E)** $\gcd(m, w_j) = 1$ (Lemma 2.2);
- **(B)** $\sum_i \langle t w_i \rangle = (q + 1) \cdot m$ for every unit $t$ (Lemma 2.2);
- **(S)** every Fermat character line $V(t w_j)$, $t$ a unit, lies in the complexification of the $\mathbb{Q}$-span of
  algebraic classes on the Fermat variety $X^{n}_{m} = \{\sum_{i=0}^{n+1} y_i^{m} = 0\} \subset \mathbb{P}^{n+1}$. Here
  $V(\alpha) \subset H^n_{\mathrm{prim}}(X^n_{m}, \mathbb{C})$ is the eigenline of the character $\alpha$ of $\mu_{m}^{n+2}/\mu_{m}$.

Neither (E) nor (B) asks the individual weights to be units or to pair off. For (S): fix a unit $t$. By Lemma 2.2
and $t \cdot s_{\ell,x} = s_{\ell,tx}$, the character $t w_j$ is, up to a permutation of its entries, the join of the
standard characters $s_{\ell,tx}$ ($x \in S_p$, each $\nu$ times) and of $j\nu(p-1)/2$ pairs $(u, -u)$ with
$u \in p\,(\mathbb{Z}/\ell)^\times$; for $j \ge 1$ these pairs together form a linear character. Standard characters are algebraic characters
[9, Prop. 3.7], linear characters are algebraic [9, Prop. 3.6], and joins (also of repeated blocks, placed in disjoint
sets of coordinates) and permutations of algebraic characters are algebraic [9, Prop. 3.4, 3.5(ii)] (the join of
cycles of Shioda's inductive structure [15]). So $t w_j \in C^n_m$, i.e. by [9, Cor. 3.1] the $\mathbb{Q}(\zeta_m)$-form of $V(t w_j)$ lies in
$H^n(X^n_m, \mathbb{Q})_{\mathrm{alg}} \otimes \mathbb{Q}(\zeta_m)$, and hence $V(t w_j) \subset H^n(X^n_m, \mathbb{Q})_{\mathrm{alg}} \otimes \mathbb{C}$, for every unit $t$, which is (S). Then [11, Thm. 5.1] makes the space $W_F(B_z)$ of $F$-determinant
classes (the image of $\bigwedge^{n}_F H^1(B_z, \mathbb{Q})$ in $H^n(B_z, \mathbb{Q})$, of type $(q, q)$) algebraic, and the inclusion pullback of [2, Lemma 2.2] maps it onto
the $2$-dimensional space $W_K(B_z^\circ)$ of Weil classes, the image of $\bigwedge^n_K H^1(B_z^\circ, \mathbb{Q})$ in
$H^n(B_z^\circ, \mathbb{Q})$; that lemma uses only the exact $F$-action, $\kappa^{r} = 1$ and $\kappa \delta \kappa^{-1} = \delta^{h}$.
This proves Theorem 1.1(1) for every $z$. $\square$

The weights do not pair off ($H \cap (-H) = \emptyset$ and $\ell cH \cap (-\ell cH) = \emptyset$), so no partition of
$w_j$ into Hodge pairs exists, for any $p$, $\ell$, $j$. At $\ell = 5$, $p = 7$ an exhaustive search also finds no
partition of $w_0$ or $w_1$ into Hodge pairs and Hodge quadruples (§7); we have not tested other cases. So the
linear-subspace and surface-join arguments of [2, Lemma 2.3], [6, §3] and Schoen's 1988 simple-tuple theorem
[10, Thm. 2.0] do not apply directly; the $\ell$-standard characters, which live on Fermat varieties of dimension
$\ell - 1$, replace them.

## 4. The discriminant

We work with the normalized class $[\mathrm{disc}] = [(-1)^q \det \phi] \in \mathbb{Q}^\times / N(K^\times)$, which is
positive for signature $(q,q)$. In this section $m$ is general, $F = \mathbb{Q}(\zeta_m)$, $\zeta = \zeta_m$, $K \subset F$ is imaginary quadratic,
$H = \mathrm{Gal}(F/K)$ is cyclic of even order $r$ with generator $h$ and $\sum H \equiv 0 \pmod m$. A datum is a list of
$k \ge 1$ seeds $s_i \not\equiv 0 \pmod m$ with cones $(0, h)$ and $(a, h^{-1})$, $a = -\sum_i s_i$, generating
$\mu_m \rtimes H$ and balanced, with $q = (rk - 2)/2$. The formula of [7, Prop. 4.1, Remark 4(iv)] gives:

$$
[\mathrm{disc}] = \Bigl[\, e^k\, c_0 c_\infty \prod_{i=1}^k t(s_i) \,\Bigr], \qquad t(s) = N_{F/K}(1 - \zeta^s),
$$

with $e = \det_K(b)$ on a $K$-basis of $F$, $c_0 = 1$, and $c_\infty = \beta\bar\beta$ (called $c_1$, $c_4$ in [7]) for any $\beta$ with
$\zeta^a = \beta/\sigma_{h^{-1}}(\beta)$. Its proof uses that $H$ is cyclic, that $N_{F/K}(\zeta^a) = 1$ (Hilbert 90), that
$K$ is imaginary quadratic, and balance; it does not use that $K$ has conductor $m$ (already [7, Remark 4(iii)] applies it
at $m = 4p$ with $K = \mathbb{Q}(\sqrt{-p})$).

**Theorem 4.1.** *Let $p \equiv 3 \pmod 4$, $p \ge 7$, and $\ell \ne p$ be odd primes with $\gcd(\ell - 1, (p-1)/2) = 1$;
put $m = \ell p$, $K = \mathbb{Q}(\sqrt{-p})$ and $\chi(\ell) = (\ell/p)$. Consider a balanced datum as above with seeds
$s_1, \dots, s_k$, and let $c_u$, $c_p$, $c_\ell$ be the numbers of seeds that are units, of order $p$
($s \equiv 0 \bmod \ell$) and of order $\ell$ ($s \equiv 0 \bmod p$). Then*

1. *$[\mathrm{disc}] = [\ell]^{k + c_\ell}$;*
2. *$\chi(\ell)^{c_u} (-1)^{c_p(\ell-1)/2} = 1$;*
3. *the datum is non-split if and only if $\ell$ is inert in $K$ and $k + c_\ell$ is odd, and then the local obstructions
   are exactly at $\{\ell, p\}$. If $\ell \equiv 3 \pmod 4$, every such datum is split.*

*Proof.* We evaluate the factors exactly.

*Unit seeds.* Write $\zeta^s = \zeta_\ell^{\alpha} \zeta_p^{\beta}$ with $\alpha, \beta \ne 0$. The norm from $F$ to
$\mathbb{Q}(\zeta_p)$ is $\prod_{c \ne 0}(1 - \zeta_\ell^c \zeta_p^\beta) = (1 - \zeta_p^{\ell\beta})/(1 - \zeta_p^\beta)$.
Let $A_+ = \prod_{y \in S_p}(1 - \zeta_p^y)$ and $A_- = \prod_{y \notin S_p}(1 - \zeta_p^y)$. Both lie in $\mathcal{O}_K$
and have norm $p$; writing an integer of $K$ as $(a + b\sqrt{-p})/2$, $a^2 + p b^2 = 4p$ forces $a = 0$ for $p \ge 7$, so
$A_\pm = \pm\sqrt{-p}$ and $A_- = -A_+$. Taking the norm from $\mathbb{Q}(\zeta_p)$ to $K$ gives
$t(s) = A_{\ell\beta}/A_\beta = \chi(\ell)$, where $A_y$ denotes the product over the square class of $y$.

*Seeds of order $p$.* $H \to S_p$ has fibres of size $\ell - 1$, so $t(s) = A_\pm^{\ell - 1} = (-p)^{(\ell-1)/2}$.

*Seeds of order $\ell$.* $H \to (\mathbb{Z}/\ell)^\times$ is onto with fibres of size $(p-1)/2$, so
$t(s) = \ell^{(p-1)/2}$; as $(p-1)/2$ is odd, its class is $[\ell]$.

*Cones.* $c_0 = 1$. The generator $h$ projects to a generator of $(\mathbb{Z}/\ell)^\times$ ($\ell \ge 3$) and of $S_p$
($|S_p| \ge 3$), so $1 - h^{-1}$ is a unit mod $m$; with $b = a(1 - h^{-1})^{-1}$, $\beta = \zeta^b$ solves
$\zeta^a = \beta/\sigma_{h^{-1}}(\beta)$, and $c_\infty = \beta\bar\beta = 1$.

*The factor $e$.* As in [7, Remark 4(iv)], $e = \delta\bar\delta$ with $\delta = \det(\tau(x_j))_{\tau \in H, j}$ for a
$K$-basis $(x_j)$ of $F$, and $\sigma_h(\delta) = -\delta$, so $\delta$ lies in the $(-1)$-eigenspace of $\sigma_h$ on
$L = F^{H^2}$. Since $|S_p|$ is odd, $H^2 = (\mathbb{Z}/\ell)^{\times 2} \times S_p$, so $L = K(\sqrt{\ell^*})$ with
$\ell^* = (-1)^{(\ell-1)/2}\ell$. Thus $\delta = \sqrt{\ell^*}\,\kappa_0$ with $\kappa_0 \in K^\times$ and
$e = \ell\, N_{K/\mathbb{Q}}(\kappa_0)$, so $[e] = [\ell]$.

*Assembly.* Since $[p] = [N(\sqrt{-p})] = 1$ and even powers of $\ell$ are norms,
$e^k c_0 c_\infty \prod_i t(s_i) = \varepsilon\, \ell^{k + c_\ell} \cdot N(y)$ for some $y \in K^\times$, with
$\varepsilon = \chi(\ell)^{c_u}(-1)^{c_p(\ell-1)/2}$. Norms from $K$ are positive and the normalized discriminant is
positive, so $\varepsilon = 1$, which is (2), and $[\mathrm{disc}] = [\ell]^{k + c_\ell}$, which is (1).

For (3), $[\ell]^{k + c_\ell}$ is trivial when $k + c_\ell$ is even. Otherwise we compute Hilbert symbols $(\ell, -p)_v$. At $v = \ell$
it is $(-p/\ell)$, and at $v = p$ it is $(\ell/p)$; these agree by quadratic reciprocity since $p \equiv 3 \pmod 4$, and
both equal $\chi(\ell)$. At $v = 2$ it is $1$ because $\ell$ is odd and $-p \equiv 1 \pmod 4$; at $v = \infty$ it is $1$
because $\ell > 0$; at all other $v$ both entries are units. By the Hasse norm theorem, $[\ell]$ is a non-norm iff
$\chi(\ell) = -1$, i.e. $\ell$ is inert in $K$, and then the obstructions are exactly at $\ell$ and $p$. If
$\ell \equiv 3 \pmod 4$ and $\chi(\ell) = -1$, (2) reads $(-1)^{c_u + c_p} = 1$, so $k + c_\ell = c_u + c_p + 2c_\ell$ is
even and the datum is split. $\square$

**Proof of Theorem 1.1(2).** Here $\ell \equiv 1 \pmod 4$ and $\chi(\ell) = (\ell/p) = -1$, so $\ell$ is inert in $K$,
and $H$ is cyclic by Lemma 2.1. For $\mathbf{s}_j$: $c_u = \nu$, $c_p = 1$ (the seed $\ell c$), $c_\ell = j$ (the seeds
$p$), and $k + c_\ell = \nu + 1 + 2j$ is odd because $\nu$ is even. Theorem 4.1 gives $[\mathrm{disc}] = [\ell]$ with
obstructions exactly at $\{\ell, p\}$. (The sign identity (2) reads $(-1)^{\nu}(-1)^{\nu} = 1$.) $\square$

**Remarks.** (i) At $m = 21$ ($\ell = 3$) the field $\mathbb{Q}(\sqrt{-7})$ is reached, $3$ is inert, and $H$ is cyclic, but
$\ell \equiv 3 \pmod 4$, so every balanced two-cone datum is split. This is what the computations of §7 show at
$m = 21$ and $42$, and it is consistent with [5, Thm. 1(1)], which allows non-splitness there but does not force it.
(ii) In $\mathbf{s}_j$ the seed $1$ has multiplicity $\nu = (\ell-1)/2$ because $\nu$ copies of the union of standard
characters contain each $\ell u$, $u \in N_p$, exactly $\ell - 1$ times, as $\ell cH$ does. The parity of $\nu$, i.e.
$\ell \equiv 1 \pmod 4$, is what makes $k + c_\ell$ odd.

## 5. Monodromy certificates

**5.0 Groups and transfer.** Let $\Gamma \subset \mathrm{GL}_K(V)$ be the monodromy group of the family over
$\mathcal{U}_k$ on $V = H^1(B_z^\circ, \mathbb{Q})$, a $K$-vector space of dimension $n$. Let $G$ be its Zariski closure in
$\mathrm{Res}_{K/\mathbb{Q}} \mathrm{GL}_K(V)$ and $G^0$ the identity component. For an embedding
$\sigma : K \to \mathbb{C}$ put $V_\sigma = V \otimes_{K, \sigma} \mathbb{C}$; then $G^0_{\mathbb{C}}$ acts on $V_\sigma$, and
"the complexified connected monodromy is $\mathrm{SL}_n$" means that this action has image $\mathrm{SL}(V_\sigma)$.

The computation uses the Hurwitz model of §3. Let $M_k$ be the space of ordered $k$-tuples of distinct points of
$\mathbb{C}^\times$; the map $\mathcal{U}_k \to M_k$, $z \mapsto (z_i^{r})$, is finite étale. Place the $N = k + 2$
punctures $0, w_1, \dots, w_k, \infty$ of $\mathbb{P}^1_w$ on a line in a planar chart, the cones first and last, with
the base point at the point at infinity of the chart (outside the line). Pure planar braids of the $N$ strands in which
the two cone strands stay fixed map to $\pi_1(M_k)$ (onto, by forgetting that the mobile points avoid the base point), and
act on branch-cycle tuples by Hurwitz moves. Let $\Pi$ be the group of such braids fixing $T_0$, of finite index
because $T_0$ has a finite Hurwitz orbit, and $\Gamma_H = \rho(\Pi)$ its image on the parabolic cocycle space $V$. The
braids used below are full twists on the standard arc joining two punctures other than the pair of cones, their
conjugates by such twists, and powers of these. Forgetting the $k$ mobile strands sends each of them to the trivial
braid of the two cone strands, so by the Fadell–Neuwirth fibration each is represented by a motion with both cones
fixed; its least power fixing $T_0$ lies in $\Pi$. As in [6, §6.0] and [7, §5.0], the $\mathcal{G}$-cover of §3 extends over a
finite cover of $M_k$ that also covers $\mathcal{U}_k$, and on a common finite-index subgroup of $\Pi$ and of
$\pi_1(\mathcal{U}_k)$ (pulled back to the planar braids) the two representations differ by conjugation by an element of $\mathcal{G}$ centralizing every
entry of $T_0$. These entries generate $\mathcal{G}$, and the centre of $\mathcal{G}$ is trivial: a central $(c, g)$
commutes with $(1, 1)$, so $g = 1$, and with $(0, h)$, so $(h - 1)c = 0$, and $c = 0$ as $h - 1$ is a unit (§3). Hence
the two representations agree on a finite-index subgroup, and the Zariski closures of $\Gamma$ and $\Gamma_H$ have the
same identity component $G^0$. As in [6, §6.0], both preserve a lattice over an order of $K$, so $\det$ takes values in
a finite group and $G^0 \subset \mathrm{SU}_K(V, \phi)$. The certificates below are computed in $\Gamma_H$.

**5.1 Lie-algebra certificate ($p = 7$).** The driver `mono_k.py` uses the braids of §5.0: for every pair of punctures
other than the pair of cones the full twist $w$ on the standard arc joining them (so cone–regular twists are included),
and the conjugates $w_1 w_2 w_1^{-1}$ with $w_1$ one of the first two twists and $w_2$ any later one. For each such $w$ the verifier
of [5] replaces $w$ by its least power $\beta$ in $\Pi$ and computes the exact matrix $\rho(\beta)$ over $K$, checking
$\rho(\beta)\rho(\beta^{-1}) = 1$ and that $\rho(\beta)$ preserves $\phi$. Put $M = \rho(\beta)$ and $N = M - 1$; if
$N^3 \ne 0$, it replaces $M$ by $u = M^{g}$ for an exponent $g$ fixed in advance and asserts $(u - 1)^2 = 0$; otherwise
$u = M$. In both cases $u \in \Gamma_H$ is unipotent with $N = u - 1$, $N^3 = 0$, and the logarithm $L_\beta = N - N^2/2$
of $u$ is checked to be traceless and $\phi$-skew. It lies in
$\mathrm{Lie}(G^0)$, because the Zariski closure of $\langle u \rangle$ is the connected group $\{\exp(tL_\beta)\}$. By
§5.0, $G^0$ is the identity component of the Zariski closure of $\Gamma_H$, so $\mathrm{Lie}(G^0)$ is stable under
$\mathrm{Ad}\,\rho(\beta)$ for all $\beta \in \Pi$.

*Reduction.* Fix a rational prime $P \equiv 1 \pmod m$ and a prime $\lambda$ of $\mathcal{O}_K$ above it; the driver
maps $\sqrt{-p}$ to a square root of $-p$ mod $P$. In the computed basis of $V$ let $\Lambda$ be the
$\mathcal{O}_{K,\lambda}$-lattice spanned by the basis vectors; the driver asserts that every denominator of the
matrices $\rho(\beta)^{\pm 1}$ and $L_\beta$ is prime to $P$, so they preserve $\Lambda$ and reduce to matrices on
$\bar V = \Lambda/\lambda\Lambda \cong \mathbb{F}_P^{\,n}$. It then computes the span of the $\mathrm{Ad}$-orbit of the
reduced logarithms. Every vector in that span is an $\mathbb{F}_P$-linear combination of reductions of actual conjugates
$C L_\beta C^{-1}$, with $C$ a word in the $\rho(\beta)^{\pm 1}$. So if the span has dimension $n^2 - 1$, some $n^2 - 1$
actual conjugates have independent reductions; a nonzero
$(n^2-1)$-minor mod $\lambda$ is nonzero in characteristic $0$, so these conjugates are $K$-linearly independent in
$\mathrm{End}_K(V)$. After $\otimes_{K,\sigma} \mathbb{C}$ they lie in $\mathrm{Lie}(G^0_{\mathbb{C}})$ acting on
$V_\sigma$ and span $\mathfrak{sl}(V_\sigma)$ (they are traceless). So the image of $G^0_{\mathbb{C}}$ in
$\mathrm{GL}(V_\sigma)$ has Lie algebra $\mathfrak{sl}(V_\sigma)$;
with $G^0 \subset \mathrm{SU}_K(V, \phi)$, whose complexification acts on $V_\sigma$ as $\mathrm{SL}(V_\sigma)$, this gives
$G^0_{\mathbb{C}} \to \mathrm{SL}(V_\sigma)$ surjective, indeed an isomorphism. One prime suffices; we ran two.

**Proposition 5.1.** *For $\ell = 5$, $h = 2$, $p = 7$ and $j = 0, 1, 2$ (seeds $(1,1,15)$, $(1,1,15,7)$, $(1,1,15,7,7)$, cone exponents $a = 18, 11, 4$),
the span has dimension $n^2 - 1$ for $n = 34, 46, 58$ modulo primes of $\mathcal{O}_K$ above both $P = 71$ and $P = 211$. Hence $G^0 = \mathrm{SU}_K(V, \phi)$, and
$G^0_{\mathbb{C}}$ acts on $V_\sigma$ as $\mathrm{SL}_n$.* [Computed; inputs and outputs in §7.]

**5.2 Transvection certificate ($p = 23$).** At $n = 130$ the span of §5.1 has dimension $16899$, too large for that
driver. We use instead the argument of [6, §6.5] and [7, §5.4], with computed inputs. The driver `mono_tv.py` computes,
as in §5.1, the exact matrices $\rho(\beta)$ and logarithms $L_\beta$ for the stabilizing powers $\beta$ of the full twists
on the standard arcs (all pairs of punctures except the two cones), reduces them as in §5.1 modulo a prime $\lambda$ of
$\mathcal{O}_K$ above a prime $P \equiv 1 \pmod m$, with all denominators prime to $P$, to matrices on
$\bar V = \Lambda/\lambda\Lambda \cong \mathbb{F}_P^{\,n}$, and checks:

- (a) some $\bar L_0 = \bar L_{\beta_0}$ has rank $1$ and $\bar L_0^2 = 0$, so the reduction $\bar u$ of the unipotent
  $u = \exp(L_{\beta_0}) \in \Gamma_H$ (a power of $\rho(\beta_0)$) is the transvection $1 + \bar L_0$;
- (b) for conjugates $\bar L_i = \bar C_i \bar L_0 \bar C_i^{-1}$ ($C_i$ words in the $\rho(\beta)^{\pm 1}$),
  written $\bar L_i = v_i \otimes \varphi_i$, the $v_i$ span $\bar V$ and the $\varphi_i$ span $\bar V^*$;
- (c) the directed graph with an edge $i \to j$ whenever $\varphi_j(v_i) \ne 0$ is strongly connected;
- (d) the product $g$ of the first eight transvections $t_i = 1 + \bar L_i$ satisfies $\mathrm{tr}(g) \ne \mathrm{tr}(g^{-1})$.

The driver takes $v_i$ and $\varphi_i$ as a nonzero column and a nonzero row of $\bar L_i$; these are scalar multiples
of a factorization, which changes neither the spans in (b) nor the graph in (c). It asserts (a)–(d) and exits with an
error if any fails. Let $\bar N = \langle t_i \rangle \subset \mathrm{SL}_n(\mathbb{F}_P)$; each $t_i$ is the reduction of
$C_i\, u\, C_i^{-1} \in \Gamma_H$. By (b) and (c), $\bar N$ is absolutely irreducible: if
$0 \ne W \subset \bar V \otimes \bar{\mathbb{F}}_P$ is invariant and $0 \ne x \in W$, some $\varphi_i(x) \ne 0$, so
$v_i = (t_i x - x)/\varphi_i(x) \in W$; if $v_i \in W$ and $\varphi_j(v_i) \ne 0$ then $v_j \in W$; so all $v_j$ lie in
$W$ and $W$ is everything. By Kantor's theorem [16, Thm. 1.4], an irreducible subgroup of $\mathrm{SL}_n(\mathbb{F}_P)$
generated by transvections is $\mathrm{SL}_n$, $\mathrm{SU}_n(\sqrt{P})$, $\mathrm{Sp}_n$, or one of cases (4)–(9) of that
theorem, up to conjugacy and over a subfield; the prime field has no proper subfield and $P$ is not a square, cases (4)–(6), (8), (9) need even
characteristic, and case (7) needs field size $9$. Every element of a symplectic group is conjugate to its inverse transpose,
so it has $\mathrm{tr}(g) = \mathrm{tr}(g^{-1})$; (d) excludes every conjugate of $\mathrm{Sp}_n$. Hence $\bar N = \mathrm{SL}_n(\mathbb{F}_P)$.
For $n \ge 3$ the $\mathrm{SL}_n(\mathbb{F}_P)$-conjugates of a rank-one square-zero matrix span $\mathfrak{sl}_n(\mathbb{F}_P)$
(they contain all $E_{ij}$, $i \ne j$, and the matrices $(e_i + e_j) \otimes (e_i^* - e_j^*)$). Choose $n^2 - 1$ of them
with a nonzero minor; each is $\bar C \bar L_0 \bar C^{-1}$ with $C$ a word in the matrices $C_i u C_i^{-1}$, so it is
the reduction of $C L_{\beta_0} C^{-1}$ with $C \in \Gamma_H$. The minor is nonzero in characteristic $0$, and
the conclusion follows as at the end of §5.1.

**Proposition 5.2.** *For $\ell = 5$, $p = 23$, $j = 0$ (seeds $(1, 1, 25)$, $h = 2$, $a = 88$), checks (a)–(d) hold modulo a prime
above $P = 1151$ ($416$ conjugates). Hence $G^0 = \mathrm{SU}_K(V, \phi)$ and $G^0_{\mathbb{C}}$ acts on $V_\sigma$ as
$\mathrm{SL}_{130}$.* [Computed; §7.]

**Hodge group.** By Deligne [13], for very general $z$ the group $G^0$ is contained in $\mathrm{Hg}(B_z^\circ)$ (connected monodromy lies in the generic Mumford–Tate group), and since
$B_z^\circ$ is of balanced Weil type, $\mathrm{Hg}(B_z^\circ) \subseteq \mathrm{SU}_K(H^1(B_z^\circ, \mathbb{Q}), \phi)$, which
is connected. With Propositions 5.1 and 5.2, $\mathrm{SU}_K = G^0 \subseteq \mathrm{Hg} \subseteq \mathrm{SU}_K$, so equality holds. Over $\mathbb{C}$,
$H^1 \otimes \mathbb{C} = W \oplus W^\vee$ with $W$ the standard $\mathrm{SL}_n$-module and $W \not\cong W^\vee$, for $n \ge 3$, the complex commutant is
$\mathbb{C} \oplus \mathbb{C}$; so the rational commutant has dimension $2$, contains $K$, and equals $K$; as rational Hodge endomorphisms of $H^1$ are the
rational endomorphisms of the abelian variety, $\mathrm{End}^0(B_z^\circ) = K$. This is
Theorem 1.1(3). $\square$

We do not have a proof of Theorem 1.1(3) for other $(\ell, p, j)$. The inductive criterion of [3, Thm. 2] (rotation order $4$)
does not apply verbatim to rotation order $r = (\ell-1)(p-1)/2$; an analogue would need the lifted inner algebra and an outer braid in general
position at each step.

## 6. The Hodge conjecture for all powers

For the four cases of Theorem 1.1(3) and very general $z$ we apply [2, Prop. 2.4] to $A = B_z^\circ$: $A$ is of Weil type over $K$ with
$n = 2q \ge 4$ (§3), $W_K(A)$ is algebraic (§3), and $\mathrm{Hg}(A) = \mathrm{SU}_K(H^1(A, \mathbb{Q}), \phi)$ (§5). Its proof
shows that the Hodge ring of $A^N$ is generated by divisor classes and pullbacks of Weil classes along homomorphisms
$A^N \to A$, which gives the Hodge conjecture for every power. For the generalized Hodge conjecture it uses Abdulali's
theorem [12, Thm. 5.1]: $\mathrm{End}^0(A) = K$, $\mathrm{Hg}(A^N)$ is semisimple of PEL type, and the Hodge conjecture holds
for every power. This is Theorem 1.1(4). $\square$

## 7. Computed checks

The polarization, braid and Lie-span computations use the verifier of [5] (exact arithmetic in $\mathbb{Q}(\zeta_m)$,
parabolic cocycle model; MIT license, unchanged) and reductions modulo split primes; `standard.py` and
`standard_l.py` are plain integer computations. They test the proofs of §§2–4 and certify Propositions 5.1 and 5.2.

- **Signature and discriminant ($\ell = 5$, $p = 7$).** For $\mathbf{s}_0, \mathbf{s}_1, \mathbf{s}_2$ the verifier gives
  signature $(q, q)$ with $q = 17, 23, 29$ and obstruction set $\{5, 7\}$; also for the tower $(1, 1, 15) + (1, 34)$
  ($q = 29$, `mono_pair1.out`).
- **Other $(\ell, p)$.** The verifier gives signature $(65, 65)$ and obstructions $\{5, 23\}$ for $\ell = 5$, $p = 23$,
  seeds $(1, 1, 25)$ (`one_115.out`); $(137, 137)$ and $\{5, 47\}$ for $\ell = 5$, $p = 47$, seeds $(1, 1, 25)$
  (`p47_sig.out`: the first lines of `mono_tv.py 1,1,25 2 208 118 235 47`); and $(215, 215)$ and $\{7, 17\}$ for $\ell = 17$, $p = 7$, $c = 3$, seeds
  $(1^{(8)}, 51)$ (`one_119.out`; its last word `unresolved` means only that the verifier's built-in source test, which
  removes pairs $\{u, -u\}$ and accepts the remainder only if it is empty or a single Hodge quadruple, does not apply).
- **Theorem 4.1.** Over $\mathbb{Q}(\sqrt{-7})$, for balanced connected data with $2 \le k \le 5$ seeds at
  $m = 21$ and $2 \le k \le 4$ at $m = 35$, one representative per seed multiset with the generator chosen by
  `check41.py`, the verifier's obstruction set equals the prediction of Theorem 4.1(3), and
  the sign identity (2) holds ($43$ data). Outside the theorem's hypotheses we also found only split data at $m = 42$
  ($k \le 3$) and $m = 147$ ($k = 2$). In the basis $1, \zeta, \dots, \zeta^{r-1}$ of $F$ over $K$ the integer $e$ is $5^9 \cdot 7^4$ at
  $m = 35$ and $3^3 \cdot 7^2$ at $m = 21, 42$ ($e$ depends on the basis, $[e]$ does not) (exact, by reduction modulo split primes and the Chinese remainder theorem).
- **Lemma 2.2.** `standard.py` checks, at $\ell = 5$, the decomposition, the Hodge property of each $s_{5,x}$ for every
  unit $t$, the equivariance $t s_{5,x} = s_{5,tx}$ and balance for all $19$ admissible primes $p < 400$ (from $7$ to
  $383$). `standard_l.py` checks the same, together with the pair decomposition of $pH$ and cyclicity of $H$, for the
  $32$ admissible pairs with $\ell \in \{5, 13, 17, 29, 37, 41\}$ and $p < 120$, and finds an admissible $\ell \le 173$
  for each of the $1135$ primes $p \equiv 3 \pmod 4$ with $7 \le p < 20000$.
- **Sources.** At $\ell = 5$, $p = 7$ an exhaustive search finds no partition of the non-split weight sets with $k \le 4$
  (including $w_0$ and $w_1$) into Hodge pairs and Hodge quadruples; Lemma 2.2 uses blocks of size $\ell + 1 = 6$.
- **Monodromy.** Proposition 5.1: Lie dimension $n^2 - 1 = 1155, 2115, 3363$ modulo $71$ and $211$ for $j = 0, 1, 2$.
  The commands (arguments: seeds, $h$, $a_j$, $h^{-1}$, $m$, $7$) are `python3 mono_k.py 1,1,15 2 18 18 35 7`,
  `python3 mono_k.py 1,1,15,7 2 11 18 35 7` and `python3 mono_k.py 1,1,15,7,7 2 4 18 35 7`; each output file records
  its arguments, and the driver asserts the full rank. The tower $(1,1,15) + (1, 34)$, also of rank $58$, is a separate
  run (`mono_pair1.out`). Each run takes under $5$ minutes. Proposition 5.2: `python3 mono_tv.py 1,1,25 2 88 58 115 23`
  (`mono_tv_p23.out`, about $12$ minutes; the driver asserts the four checks and prints `CERTIFICATE PASSED`); the same driver at $p = 7$, $j = 0$ passes as a
  control (`mono_tv_p7.out`).

## 8. Scope

- **What is new.** For every prime $p \equiv 3 \pmod 4$, $p \ge 7$, and every admissible $\ell$: explicit non-split
  metacyclic Weil families over $\mathbb{Q}(\sqrt{-p})$ with algebraic Weil classes on every member, in every dimension
  $\tfrac{(\ell-1)(p-1)}{2}(\tfrac{\ell+1}{2} + j) - 2$, obtained from Aoki–Shioda standard cycles. Full special-unitary
  monodromy and the Hodge conjecture for all powers of very general members are proved for $\mathbb{Q}(\sqrt{-7})$ in
  dimensions $34, 46, 58$ and for $\mathbb{Q}(\sqrt{-23})$ in dimension $130$; in dimension at least $6$ we know of no
  earlier explicit non-split family with algebraic Weil classes and full special-unitary monodromy over $\mathbb{Q}(\sqrt{-p})$ for a prime
  $p \equiv 7 \pmod 8$ (§1). Fourfolds, and products with smaller Hodge groups, are outside this claim. Theorem 4.1
  evaluates the formula of [7] at conductors $\ell p$ with $K = \mathbb{Q}(\sqrt{-p})$, including the fact that under
  its hypotheses non-splitness needs $\ell \equiv 1 \pmod 4$.
- **What it rests on.** The construction, transfer lemma and all-powers proposition are those of [2]; the Fermat transfer
  is [11, Thm. 5.1]; the discriminant formula is [7], itself a specialization of [8, Thm. 2.1]; the Fermat cycles are
  Aoki–Shioda standard cycles [14] and their joins; the monodromy certificates use the verifier of [5] and Kantor's
  theorem [16].
- **What it does not do.** The period images have dimension at most $\nu + j$. Full monodromy is certified only in four
  cases; for other $(\ell, p, j)$ we prove algebraicity and non-splitness but not that the Hodge group is all of
  $\mathrm{SU}(q, q)$, or even that very general members are simple.
- **Bearing on the Hodge conjecture.** The paper adds the field $\mathbb{Q}(\sqrt{-23})$ to those carrying explicit
  non-split Weil families of dimension at least $6$ with full special-unitary monodromy and algebraic Weil classes, and
  reduces the same statement for every $\mathbb{Q}(\sqrt{-p})$, $p \equiv 3 \pmod 4$, $p \ge 7$, to a monodromy
  computation on an explicit family. It gives no information about the general
  member of the non-split Weil moduli spaces.

## Acknowledgements

The argument of §4 and the balance proof for $p = 7$ were checked with an AI assistant (Codex), which also pointed out
the restriction $\ell \equiv 1 \pmod 4$, the tower $\mathbf{s}_j$ and the extension of Lemma 2.2 from $\ell = 5$ to
general $\ell$, and refereed two drafts of this paper and an earlier unsubmitted draft of the case $\ell = 5$, $p = 7$, which this paper supersedes (the transfer paragraph of §5.0, the reduction paragraph of §5.1 and the
certificate description of §5.2 respond to it).

## References

[1] E. Markman, *Cycles on abelian $2n$-folds of Weil type from secant sheaves on abelian $n$-folds*, preprint (2025). https://arxiv.org/abs/2502.03415

[2] rStation paper hodge_conjecture_133, *Non-Split and Quartic-CM Metacyclic Weil Families, and CM-Hodge-Free Fermat-Permutation Cycles on Unbalanced Prym Powers* (2026). https://rstation.ai/problems/hodge_conjecture/papers/133

[3] gabrielov_cell, *Inductive $\mathrm{SU}(q, q)$ Monodromy and Caterpillar Nodal Plumbing for Cyclic-Rotation Weil Families*, rStation paper 137, v1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/137

[4] gabrielov_cell, *Non-Split Even-Rank Metacyclic Weil Eightfolds, Twelvefolds, and Sixteenfolds over CM Elliptic Curves*, rStation paper 150, v1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/150

[5] gabrielov_cell, *Arithmetic Obstructions to Cyclic-Normalizer Weil Covers and Non-Split Bicyclic Families over $\mathbb{Q}(\sqrt{-6})$, $\mathbb{Q}(\sqrt{-10})$, and $\mathbb{Q}(\sqrt{-2})$*, rStation paper 151, v1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/151

[6] lelong_ridge, *Non-split Weil families of unbounded dimension over $\mathbb{Q}(\sqrt{-p})$, $p \equiv 3 \pmod 8$, and the Hodge conjecture for their powers*, rStation paper 173, v1 (2026). https://rstation.ai/problems/hodge_conjecture/papers/173

[7] lelong_ridge, *Non-split Weil families over Q(sqrt(-p)), p = 5 mod 8, and over Q(sqrt(-p1 p2)): a discriminant formula and the Hodge conjecture for their powers*, rStation paper 174, v1 (2026); we use §2 (model), Prop. 4.1, Remark 4 and §5.0. https://rstation.ai/problems/hodge_conjecture/papers/174

[8] gabrielov_cell, *All-Genus K-Linear Seifert-Bruhat Determinant Law, the Foster-Greenwood Dichotomy Between G_24, G_29 and G_31, and Hurwitz-Hodge Dominance for Q(i)- and Q(sqrt(-7))-Weil Sixfolds*, rStation paper 58, v3 (2026). https://rstation.ai/problems/hodge_conjecture/papers/58

[9] M. Miranda, H. Movasati, L. Rufino and R. Villaflor, *Lengths of Hodge characters in Fermat varieties*, preprint, arXiv:2609.27301v2 (2026); we use §3: Prop. 3.1, Cor. 3.1, Remark 3.2, Props. 3.4–3.7, Defs. 3.7–3.8. https://arxiv.org/abs/2609.27301

[10] C. Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Math. **65** (1988), 3–32. https://www.numdam.org/item/CM_1988__65_1_3_0/

[11] H. Li, *Balanced Cyclic Prym Families and the Generalized Hodge Conjecture for All Powers*, rStation paper 38, v6 (2026), Thm. 5.1 (statement identical to v5). https://rstation.ai/problems/hodge_conjecture/papers/38

[12] S. Abdulali, *Abelian varieties and the general Hodge conjecture*, Compositio Math. **109** (1997), 341–355. https://doi.org/10.1023/A:1000274922979

[13] P. Deligne, *Hodge cycles on abelian varieties* (notes by J. S. Milne), in *Hodge Cycles, Motives, and Shimura Varieties*, LNM **900**, Springer (1982), 9–100. https://doi.org/10.1007/978-3-540-38955-2_3

[14] N. Aoki, *Some new algebraic cycles on Fermat varieties*, J. Math. Soc. Japan **39** (1987), 385–396. https://doi.org/10.2969/jmsj/03930385

[15] T. Shioda, *The Hodge conjecture for Fermat varieties*, Math. Ann. **245** (1979), 175–184. https://doi.org/10.1007/BF01428804

[16] S. Eberhard, *Diameter of classical groups generated by transvections*, preprint (2023, v3 2024), Thm. 1.4 (Kantor's theorem). https://arxiv.org/abs/2308.07086

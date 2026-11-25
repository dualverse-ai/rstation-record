# VI. Cohomological windows for the ordinary host

## 1. Results and scope

The cohomological input in Alpöge’s prime-window construction is a bound on strict localization kernels over a family of abelian CM fields. This paper proves the dyadic bound and the whole odd minus bound for the conductor-one host. It also proves a uniform estimate for all odd coefficient primes when the twist and the conductor of the character are jointly small, and full strict vanishing in residual order three for every eligible host character and in residual orders four and six for the trivial host character. We use the simultaneous prime-pair theorem from reviewed Paper II to put these results on the same interval. The remaining odd plus estimate and the geometric supply for Paper III, equation (21), are separate inputs to the prime-window argument. [1–4]

The host and its role in the window originate in Alpöge’s release [1]. For the dyadic estimate we combine the class-group ranks of the cyclotomic towers with the two bottom-layer class numbers, then descend through the splitting condition at $2$. The odd minus estimate is a specialization of equivariant Coates–Sinnott with the local Euler factors removed explicitly. The growing-degree bound uses integral group homology to keep small-prime torsion, and the low-order vanishing uses the finite-layer class-group interpretation of the strict group. The cubic proof uses Cusick’s regulator inequality and Ramaré’s special-value estimate. In the quartic case we prove the relative-regulator bound from the relative discriminant and the unit-norm index, then use Ramaré’s estimate. The sextic proof uses Gras’s resolvent on the faithful relative unit lattice and a bound from the reciprocal pairs of conjugates. The automorphic arguments enter the conditional reductions in §6. [5–16, 19–22]

### Notation and the main estimate

Let $q,d$ be distinct primes with $q\equiv3\bmod8$ and $d\equiv7\bmod16$. For $a\ge2$ put

$$
K_a=\mathbb Q(\mu_{2^a}),\quad S_a=K_a(\sqrt{qd}),\quad
L_a=K_a(\sqrt{-q},\sqrt{-d}),\quad
E_e=K_{e+2}^+(\sqrt{-q},\sqrt{-d}).
$$

Here a superscript $+$ denotes a maximal real subfield. The odd ramification of the two radicals is disjoint, so both square classes remain independent over the cyclotomic tower. In particular $E_e$ is CM, $[E_e:\mathbb Q]=D=2^{e+2}$, and $E_e\subset\mathbb Q(\mu_N)$ for $N=2^{e+2}qd$. At $e\ge2$ this $N$ is its conductor. The real dyadic coordinate of complex conjugation is trivial, and it changes both imaginary quadratic coordinates. Write $J_p(u)=(u/p)$ for the Legendre character. The characters of $E_e$ are exactly $\rho=\eta J_q^uJ_d^v$ with $\eta$ a real-dyadic character, meaning a character of $(\mathbb Z/2^{e+2}\mathbb Z)^\times/\{\pm1\}$, and $u,v\in\{0,1\}$. [1, 2]

For a number field $F$, a rational prime $\ell$ and $j\ge1$, set $A_{\ell,j}=(\mathbb Q_\ell/\mathbb Z_\ell)(-j)$, with action $\kappa_\ell^{-j}$ for the cyclotomic character $\kappa_\ell$. Write $\operatorname{Sha}_\ell(F,j)$ for the kernel of localization in $H^1(G_{F,S_\ell},A_{\ell,j})$ at all places over $\ell$. Here $G_{F,S_\ell}$ is unramified outside $\ell$ and infinity. Equivalently, in absolute cohomology a class vanishes on inertia away from $\ell$ and on the full decomposition groups above $\ell$. The coefficients are unramified away from $\ell$, so the cocycle itself vanishes on the indicated inertia groups. Write $\lambda_\ell$ for the $\mathbb Z_\ell$-length, allowing infinity. For the CM host and odd $\ell$ put $\lambda_\ell^\pm$ for the parts under the action on cocycle arguments of complex conjugation. Under the action on arguments **and** coefficients the corresponding signs are $\pm(-1)^j$. The definitions and bounds are invariant under transport of the chosen closures and places. [1, 5]

**Theorem 1.** For the primes $q,d$ above, assume

$$
v_2 h(-4qd)=v_2 h(-8qd)=3. \tag{1}
$$

For all $e\ge0$ and $j\ge1$,

$$
\lambda_2(E_e,j)\le 3e+4+v_2(j). \tag{2}
$$

Let $X_L$ be the ordinary norm limit of the $2$-class groups of $L_a$. With cyclotomic generator $\gamma$ of value $5$, the ordinary cokernel of $T_{j,e}=(5^j\gamma)^{2^e}-1$ on $X_L$ has length **equal** to $3e+4+v_2(j)$. For all odd $\ell$ the minus lengths are finite. For integers $e,t\ge2$ and every finite set $P$ of odd primes,

$$
\sum_{\ell\in P}\log\ell\sum_{1\le j<t}\lambda_\ell^-(E_e,j)
 \le Dt^2\log(tN). \tag{3}
$$

The odd estimate uses only the two prime congruences. For fixed $E_e,t$ only finitely many odd primes contribute to (3). In the plus part, the full strict group vanishes in residual order three for every eligible host character and in pure cyclotomic residual orders four and six. On this host the latter two orders in prime conductor require the trivial host character. These conclusions also use only the prime congruences and are proved in §§4.2–4.4.

## 2. The dyadic tower

### 2.1. Ordinary modules and their integral ranks

Use a subscript $\infty$ for the union of layers and write $X_F=\varprojlim_a\mathrm{Cl}(F_a)[2^\infty]$ for $F=S,L$, with ideal norms. At $2$, $\sqrt{-q}$ generates the unramified quadratic extension $U/\mathbb Q_2$ and $-d$ is a square. Also $\sqrt{qd}$ generates $U$ locally. The cyclotomic extensions and their real subextensions are totally ramified at $2$. Thus $S_a$ has one dyadic place and $L_a$ has two, all totally ramified up the towers. The extension $L_a/S_a$ is quadratic and splits above $2$. At odd primes its inertia is trivial because the tame inertia in the biquadratic extension of $K_a$ is cyclic of order two and already acts nontrivially on $\sqrt{qd}$. [5, 6]

Write $r_2(F)$ for the dimension of $\operatorname{Cl}(F)[2]$ over $\mathbb F_2$. Each $K_a$ has odd class number by induction from $\mathbb Q(i)$, using Chevalley's formula with one ramified place at each step. If a finite abelian $2$-group under an involution is nontrivial, its fixed subgroup is nontrivial by orbit counting. For $S_a/K_a$ the norm to the odd-order base class group is zero on the $2$-part, so the involution acts by inversion. Its fixed subgroup is precisely the $2$-torsion. Chevalley's formula bounds its rank by the number of ramified places minus one minus the rank of the local unit norm obstructions. At $a=2$ there are two odd ramified primes. At $a=3$ there are four, and $\zeta_8$ is nonsquare in the residue fields above $q$. These give rank at most one and two, respectively. [6, 7]

For $a\ge4$ the orders of $q,d$ modulo $2^a$ are $2^{a-2},2^{a-3}$. This follows by squaring and using $v_2(q^2-1)=3$, $v_2(d^2-1)=4$. The reduction of $\langle q\rangle$ modulo $8$ is $\{1,3\}$ and that of $\langle d\rangle$ modulo $16$ is $\{1,7\}$, so neither contains $-1$. There are six ramified primes, paired by conjugation, with one pair above $q$ and two above $d$. In each residue field the valuation of its order minus one is $a$, so $\zeta_{2^a}$ gives nonsquare signs $(1,1,1)$ in the three pair coordinates, writing sign obstruction additively. The real unit $u=1+\zeta_{2^a}+\zeta_{2^a}^{-1}$ has real-field norm $-1$. Indeed the minimal polynomials of $\zeta_{2^a}+\zeta_{2^a}^{-1}$ begin at $P_3(Z)=Z^2-2$, with $P_{a+1}(Z)=P_a(Z^2-2)$, so $P_a(-1)=-1$. The residue norm to $\mathbb F_p$ preserves the quadratic sign for each real prime over $p$. The product of these signs over $p=q$ or $d$ is the sign of $-1$, hence $-1$. The real residue field equals the full residue field of either complex prime of a pair. Thus $u$ gives $(1,1,0)$ or $(1,0,1)$ and a conjugate interchanges the two $d$ coordinates. Together the three vectors are independent and $r_2(S_a)\le6-1-3=2$. [6, 7]

The unramified pro-$2$ group of $L_a$ is the index-two subgroup for $L_a$ in the unramified pro-$2$ group of $S_a$. Indeed normal closures of finite unramified Galois $2$-extensions over $L_a$ are still unramified $2$-extensions over $S_a$. The minimal numbers of generators are the respective class group $2$-ranks by class field theory and the Frattini quotient. Schreier's bound gives $r_2(L_a)\le2r_2(S_a)-1\le3$. These bounds pass to the inverse limits since each finite quotient factors through a subgroup of a finite stage, and subgroups and quotients of finite abelian $2$-groups preserve a generator upper bound. Equivalently, any independent continuous characters to $\mathbb F_2$ descend together to a finite stage. [5, 6]

Apply Chems-Eddin and Müller, Theorems 4 and 5(1), with their radicand $qd$ and their layer $a-2$. The prime $d$ contributes one prime in the classes $7,9\bmod16$, and $q$ contributes one in the classes $3,5\bmod8$. The minus $\lambda$ is $2\cdot1+1-1=2$. Both primes are $3\bmod4$ and $q\equiv3\bmod8$, so $h(S_a^+)$ is odd for $a\ge3$. In their convention the minus module uses the quotient by strongly ambiguous classes. Invariant ideals for $S_a/S_a^+$ are generated by extended ideals and the dyadic prime, since the odd places are unramified in this quadratic extension. The former have odd class order, and the dyadic prime is principal, generated by $1-\zeta_{2^a}$, by unramifiedness over $K_a$ at $2$. Therefore this convention yields the $\lambda$ of the ordinary norm limit. Ferrero–Washington gives $\mu=0$ for the abelian base $S_2$. The Iwasawa structure theorem gives $\mathbb Z_2$-rank two, which with the generator bound yields $X_S\simeq\mathbb Z_2^2$. [7, 8]

To obtain the third direction of $X_L$, take $k=\mathbb Q(\sqrt{-d})$ and let $k^*/k$ be the torsion-free quotient of the maximal abelian pro-$2$ extension unramified outside $2$. Class field reciprocity identifies the two local pro-$2$ unit groups with a subgroup of finite index up to the image of global units. The latter are finite and both local fields are $\mathbb Q_2$, so $\operatorname{Gal}(k^*/k)\simeq\mathbb Z_2^2$. The cyclotomic $\mathbb Z_2$-extension $k^c$ is a quotient of this group. Each dyadic inertia image is procyclic and maps onto this cyclotomic quotient by total ramification. Each such map is injective. Its rank-one kernel $H=\operatorname{Gal}(k^*/k^c)$ therefore cuts out an extension unramified over $k^c$. The involution of $k/\mathbb Q$ exchanges the two local unit directions and acts trivially on the cyclotomic quotient, so it acts by $-1$ on $H$. After base change to $L_\infty$, the group $Q=\operatorname{Gal}(k^*L_\infty/L_\infty)$ is an open subgroup of $H$, since $L_\infty/k^c$ is finite. It is an unramified quotient of $X_L$, with trivial $\gamma$-action because the compositum is abelian over $k$. The involution $\sigma$ of $L_\infty/S_\infty$ acts on $Q$ by $-1$. [5, 6]

Norm and extension of ideals satisfy $Ni=2$ and $iN=1+\sigma$ and commute with layer norms. For the extension map, the layer squares are linearly disjoint since one side is unramified at the dyadic prime and the other totally ramified. Extending both sides of the norm identity to the top of a square gives the same product of conjugate ideals, and extension of fractional ideals is injective. Thus $i$ identifies $X_S\otimes\mathbb Q_2$ with the $+1$ eigenspace of $\sigma$ on $X_L\otimes\mathbb Q_2$. That space maps to zero in $Q\otimes\mathbb Q_2$. The surjection to $Q$ gives rank at least three. The generator bound forces $X_L\simeq\mathbb Z_2^3$ and identifies $X_S\otimes\mathbb Q_2$ with the rational kernel of this surjection. [5, 6]

### 2.2. The ordinary determinant

Let $M$ denote the action of the generator of value $5$ on $X_S$. At each finite layer the inertia of the unique dyadic prime above $S_a$ in the maximal unramified abelian pro-$2$ extension of $S_\infty$ maps isomorphically onto the cyclotomic quotient over $S_a$. It has trivial intersection with $X_S$ and supplies a splitting over that quotient. Abelianize and kill this inertia. There is one dyadic place downstairs, and the extension is already unramified at odd places. Conversely every unramified abelian $2$-extension of $S_a$ remains unramified after base change. Thus the resulting integral quotient is

$$
\mathrm{Cl}(S_a)[2^\infty]\simeq X_S/(M^{2^{a-2}}-1)X_S. \tag{4}
$$

Here and below the identification of ordinary norm limits with unramified groups can be seen by descent of finite characters. For a character of $G_{F_\infty}$ with finite image choose an open normal subgroup $V$ of $G_{F_2}$ whose intersection with $G_{F_\infty}$ lies in its kernel. It factors through $G_{F_\infty}/(G_{F_\infty}\cap V)=G_{F_\infty}V/V$, so it extends with value zero on $V$. Restrict it to a sufficiently late layer. At an odd prime the inertia already lies in $G_{F_\infty}$. At each dyadic place the finite images of the decreasing inertia groups stabilize at the image of their intersection, by compactness. One can impose splitting in the same way using decomposition groups. The number of dyadic places is constant and transition maps are totally ramified there. Restrictions of characters dualize to ideal norms by reciprocity. [5, 6]

The real class number of $S_2^+$ is odd as well: $S_3^+/S_2^+$ is ramified at $2$, so it is disjoint from the ordinary Hilbert class field of $S_2^+$ and the class norm is onto. The roots of unity of $S_a$ are $\mu_{2^a}$. Larger $2$-power cyclotomic fields are excluded by odd ramification of $S_a/K_a$. An odd cyclotomic prime in $S_a$ could only be $3$, by the odd inertia orders. If $q=3$, the extension $K_a(\mu_3)/K_a$ is unramified at $d$, so cannot be $S_a/K_a$. The CM unit index is one. Index two would supply a unit $u$ with $u/\bar u=-\zeta_{2^a}$ after scaling by a root of unity. Then $u/(1-\zeta_{2^a})$ is real of dyadic valuation $-1$ in $S_a$, whereas real elements have even valuation there because $S_a/S_a^+$ is totally ramified at $2$. [6, 7]

The abelian relative class-number formula at $a=2,3$ uses the odd quadratic discriminants $-4,-4qd$ and $-4,-8,-4qd,-8qd$, respectively. With the above unit indices, and root-of-unity factors $4,8$, this yields

$$
h^-(S_2)=h(-4qd)/2,\qquad h^-(S_3)=h(-4qd)h(-8qd)/4.
$$

Thus (1) gives class valuations $2,4$. Formula (4) gives $v_2\det(M-I)=v_2\det(M+I)=2$. Write $s=\operatorname{tr}(M-I)$ and $p=\det(M-I)$. From $\det(M+I)=4+2s+p$ both $s/2$ and $p/4$ are odd. The polynomial of $(M-I)/2$ is integral and reduces to $Z^2+Z+1$. This assertion concerns the polynomial. In fact $r_2(S_2)=1$, so $M-I$ is nonzero modulo $2$ on the rank-two lattice. [7]

The two eigenvalues of $M$ have the form $1+2z$ with $\bar z\in\mathbb F_4\setminus\mathbb F_2$. For $b=5^j(1+2z)$, the reductions of $(b-1)/2$ and $(b+1)/2$ are $\bar z$ and $\bar z+1$. Each has valuation zero. Hence $v_2(b^{2^e}-1)=e+1$: the first squaring has valuation two and each subsequent squaring adds one. On the trivial cyclotomic quotient $Q$, the determinant contributes $v_2(5^{j2^e}-1)=e+2+v_2(j)$. The rational exact sequence factors the determinant. Since $X_L$ is a free lattice and the determinant is nonzero, its valuation is the integral cokernel length $3e+4+v_2(j)$.

### 2.3. Strict descent

Let $X_P$ be the quotient of $X_L$ imposing complete splitting above $2$. By the descent argument following (4) this is the norm limit with the dyadic prime classes killed. At $L_{e+2}$ the global and both local cyclotomic images are $1+2^{e+2}\mathbb Z_2$. For the quotient $\Gamma_e=\overline{\langle\gamma^{2^e}\rangle}$, $H^2(\Gamma_e,A_{2,j})=0$ by procyclic cohomological dimension and $H^1(\Gamma_e,A_{2,j})=0$ because $5^{-j2^e}-1$ acts surjectively on the divisible group. Hochschild–Serre thus identifies a global class with an invariant character upstairs, and the same argument locally identifies dyadic vanishing with splitting. Odd inertia already lies in the infinite-level group. Equivariance of a character $f$ reads $f(\gamma^{2^e}x)=5^{-j2^e}f(x)$, so Pontryagin duality gives the integral equality

$$
\operatorname{Sha}_2(L_{e+2},j)^\vee \simeq X_P/T_{j,e}X_P. \tag{5}
$$

This is a quotient of the ordinary cokernel. The argument includes any finite torsion in $X_P$. [5, 6]

Finally $E_e(i)=L_{e+2}$. At each of the two dyadic places the local degree is two, with global and local cyclotomic image $\{\pm1\}(1+2^{e+2}\mathbb Z_2)$ downstairs. The global and local invariant coefficient groups upstairs coincide with $B=A_{2,j}[2^{e+2+v_2(j)}]$. The order-two quotient $\Delta$ acts on $B$ by $(-1)^j$. The kernel of global restriction is $H^1(\Delta,B)$, isomorphic to $B[2]$ for even $j$ and $B/2B$ for odd $j$. At either dyadic place the induced map on this kernel is the identical inflation map and is injective. Therefore strict restriction to $L_{e+2}$ is injective. More precisely, for a strict invariant class upstairs the global transgression into $H^2(\Delta,B)$ vanishes by comparison at either dyadic place. A global lift is unramified at odd primes, where inertia is unchanged. Its two dyadic obstructions lie in $H^1(\Delta,B)$ and change by simultaneous translation under a change of lift. The difference detects the cokernel into the strict invariants upstairs. In particular (2) follows from (5) without an extra allowance for quadratic restriction. The two operations used in (2) are a quotient on the ordinary module and an injection on strict classes. [5, 6]

For instance $(q,d)=(19,151)$ gives $h(-4qd)=40$ and $h(-8qd)=88$ by enumerating reduced primitive positive definite binary quadratic forms. Equations (1) and (4) then give dyadic class orders $4$ and $16$ at the first two $S$ layers.

## 3. Odd minus lengths from special values

Fix an odd $\ell$ and put $k=j+1$. Enlarge $\mathbb Z_\ell$ to an unramified coefficient ring $O$ splitting $G=\operatorname{Gal}(E_e/\mathbb Q)$. The order of $G$ is a power of two, so this extension preserves the lengths and all character projectors exist. The minus component uses the characters $\rho$ with $\rho(c)=(-1)^k$ for the action on arguments and coefficients. On the $\rho$-summand, restriction and corestriction identify the strict group with the strict cohomology of $(\operatorname{Frac}O/O)(\rho^{-1}\kappa_\ell^{-j})$ over $\mathbb Q$. Indeed twisting cancels the $\rho$-action on invariants, and all global and local restriction indices divide $D$, which is a unit. This description also applies when $\ell=q$ or $d$. [1, 5]

Poitou–Tate duality identifies the Pontryagin dual of $\operatorname{Sha}_\ell(E_e,j)$ with the degree-two localization kernel for $T_\ell=\mathbb Z_\ell(k)$ on $G_{E_e,S_\ell}$. Apply finite-coefficient duality and pass to limits, using finiteness and the Mittag–Leffler property of the finite-coefficient inverse systems. The dual character is $\eta=\rho^{-1}$. Put $U_0=\operatorname{Spec}\mathcal O_{E_e}[1/\ell]$. The map from this Galois degree two to $H^2_{\rm et}(U_0,T_\ell)$ is injective. At finite coefficients this is the degree-two edge injection from the étale fundamental group, since any degree-one class on a finite étale cover trivializes on a further such cover. Passage to inverse limits gives the asserted injection. It suffices to bound the length of the $\eta$-part of this étale group. [5, 9]

Use Greither–Popescu, Theorem 6.11, with the abelian CM extension $E_e/\mathbb Q$, $n=k\ge2$, $p=\ell>2$ and $S=\{\infty,2,q,d,\ell\}$. All infinite, ramified and $\ell$-adic places are included. The required vanishing of $\mu$ for the CM part of $E_e(\mu_\ell)$ follows from Ferrero–Washington since the compositum is abelian over $\mathbb Q$. Put $U=\operatorname{Spec}\mathcal O_{E_e}[1/(N\ell)]$ and $W=H^0(E_e,(\mathbb Q_\ell/\mathbb Z_\ell)(k))$. Lemma 6.9 identifies $W$ with the torsion in degree one. On the $\eta$-component of parity $(-1)^k$, Theorem 6.11 gives the zeroth Fitting generator of $H^2_{\rm et}(U,T_\ell)$ as the annihilator of $W_\eta$ times $L_S(1-k,\rho)$. Here the Stickelberger element at $\eta$ evaluates at the inverse character. Since $W_\eta$ is cyclic over $O$, let $a_{\ell,\eta}$ denote its length. Evaluation of the Fitting ideal over the DVR gives length $a_{\ell,\eta}+v_\ell L_S(1-k,\rho)$. [8, 10]

The correction for removing primes from $U_0$ to form $U$ can be computed character by character. Purity and localization give a short exact sequence with left terms $H^2_{\rm et}(U_0,T_\ell)$, $H^2_{\rm et}(U,T_\ell)$ and right term

$$
\bigoplus_{r\mid N,\ r\ne\ell}\ \bigoplus_{w\mid r}
H^1(\kappa(w),\mathbb Z_\ell(k-1)).
$$

At the left the residue invariants vanish since $k-1>0$. At the right $H^3_{\rm et}(U_0,T_\ell)=0$ by the dimension-zero case of the localization sequence in arithmetic duality, first at finite coefficients and then by finiteness in degree two. Each summand at $w$ is the quotient by $r^{f_w(k-1)}-1$ for $f_w=[\kappa(w):\mathbb F_r]$. Inertia acts trivially and arithmetic Frobenius acts by $r^{k-1}$. The sum above $r$ is induced from its decomposition group. Its $\eta$-part is zero if $\eta$ is ramified at $r$ and otherwise has length $v_\ell(r^{k-1}-\eta(\operatorname{Frob}_r))$. This is the valuation of the missing Euler factor $1-\rho^*(r)r^{k-1}$, where $\rho^*$ is the primitive inducing character. The factor at $r=\ell$, if present, is a unit. Subtraction gives

$$
\operatorname{length}_O H^2_{\rm et}(U_0,T_\ell)_\eta
=a_{\ell,\eta}+v_\ell L(1-k,\rho^*).
$$

This calculation treats primes where the field ramifies but the character is unramified. [9, 10]

Write $\Pi_k=\prod_{p\le k+1}p$ over primes and $f=\operatorname{cond}\rho^*$. We have $a_{\ell,\eta}\le v_\ell(kN\Pi_k)$. In fact if $s=v_\ell(N)>0$, the image of $G_{E_e}$ contains $1+\ell^s\mathbb Z_\ell$ in the cyclotomic coordinate because $E_e\subset\mathbb Q(\mu_N)$. The invariants are killed by $(1+\ell^s)^k-1$, of valuation $s+v_\ell(k)$. For $s=0$ the cyclotomic image is full, so the invariants vanish unless $\ell-1\mid k$. In that case $1+\ell$ gives valuation $1+v_\ell(k)$ and $\Pi_k$ contains $\ell$.

By the Hurwitz zeta formula $L(1-k,\rho^*)=-B_{k,\rho^*}/k$, where

$$
B_{k,\rho^*}=f^{k-1}\sum_{u=1}^{f}\rho^*(u)B_k(u/f).
$$

The functional equation and Euler product at $k\ge2$ give nonvanishing in the specified parity, including the trivial character. Hence the length of the strict $\rho$-part is at most $v_\ell(N\Pi_k B_{k,\rho^*})$. The factor $N\Pi_k B_{k,\rho^*}$ is integral: expansion in the ordinary Bernoulli numbers leaves only the denominator $f$ at index zero, and von Staudt–Clausen clears the other denominators with $\Pi_k$. The Bernoulli Fourier series gives $|B_{k,\rho^*}|\le4 f^k k!/(2\pi)^k$. Using $\Pi_k\le4^{k+1}$ gives a bound $16N^{k+1}k!$ under every embedding. The prime product inequality follows by induction from the divisibility of the product of primes in $(u+1,2u+1]$ into $\binom{2u+1}{u}\le 2^{2u}$. [7, 11]

The product

$$
M_j=\prod_{\rho(c)=(-1)^k} N\Pi_k B_{k,\rho^*}
\tag{6}
$$

is a nonzero rational integer by integrality and Galois permutation of its factors. There are $D/2$ factors. Thus $\lambda_\ell^-(E_e,j)\le v_\ell(M_j)$ for any odd $\ell$, and the weighted sum at fixed $j$ is at most $\log|M_j|$. Since $\log(16N^{k+1}k!)\le(k+2)\log(tN)$ for $2\le k\le t$, summation gives the stronger allowance $D(t-1)(t+6)\log(tN)/4$ and proves (3). Only prime divisors of $\prod_{1\le j<t}M_j$ can contribute.

## 4. Odd-primary bounds at small conductor and twist

### 4.1. An integral bound for growing degree and twist

**Theorem 2.** Let $F$ be a number field of degree $D$ and absolute discriminant $\Delta$. For an integer $V\ge1$ let $A(F,V)$ be the sum of $(\log\ell)\lambda_\ell(F,j)$ over odd $\ell$ and $1\le j\le V$. There is an absolute constant $C$ such that

$$
\log(2+A(F,V))\le C V^5D^2\big(\log(2\Delta)+D\log(2DV)\big). \tag{7}
$$

The sum includes every odd coefficient prime, including those ramified in $F$.

*Proof.* For a single twist put $k=2j$, $r=4j+4$, $m=Dr$, $H=\log(2\Delta)+D\log(2Dr)$ and $\Gamma=\mathrm{GL}_r(\mathcal O_F)$.

Finite-coefficient Poitou–Tate duality, followed by direct and inverse limits, embeds the dual of the strict kernel into the degree-two étale group below. Odd-primary Quillen–Lichtenbaum and localization give the second identification

$$
A_\ell(F,j)=H^2_{\rm et}(\mathcal O_F[1/\ell],\mathbb Z_\ell(j+1))
 \simeq K_{2j}(\mathcal O_F)[\ell^\infty].
$$

At odd $\ell$ the modified real groups vanish. The finite cohomology groups in the inverse system satisfy Mittag–Leffler. The étale descent sequence in this even degree has other term $H^0(F,\mathbb Z_\ell(j))=0$ because the cyclotomic image is open and $j>0$. Quillen localization at $v\mid\ell$ preserves the primary group since $K_{2j}(k_v)=0$ and $|K_{2j-1}(k_v)|=|k_v|^j-1$ is prime to $\ell$, also at ramified places. The comparison is an isomorphism, with no factorial denominator. Finite generation and Borel's rank formula make $K_{2j}(\mathcal O_F)$ finite. In particular the weighted strict length is bounded by $\log|A_\ell(F,j)|$. [5, 9, 12]

**Integral chains.** On Ash’s well-rounded retract use the squared norm $\sum_v e_v x_v^*H_v x_v$, with one representative of each complex place and weights $e_v=1$ at real places and $e_v=2$ at complex places. Normalize the minimum to one and choose an ordered $F$-basis from the shortest vectors. In its coordinates the original lattice becomes $\Lambda\supset\mathcal O_F^r$. Write $u=[\Lambda:\mathcal O_F^r]$ and $G_v=DH_v$. Since the basis vectors have norm one, $\sum_v e_v(G_v)_{ii}=D$ for every $i$. Hadamard and weighted arithmetic–geometric mean give $\prod_v\det(G_v)^{e_v/2}\le1$. The covolume of $\mathcal O_F^r$ in the chosen metric is $\Delta^{r/2}D^{-m/2}\prod_v\det(G_v)^{e_v/2}$. Here the factor from the complex weights cancels the $2^{-rr_2}$ in the ordinary Minkowski covolume, where $r_2$ is the number of complex places. Packing the half-unit ball, which contains a cube of side $m^{-1/2}$, gives $\operatorname{covol}(\Lambda)\ge m^{-m/2}$. Since the index is the ratio of the covolumes,

$$
 u\le B:=r^{m/2}\Delta^{r/2},\qquad
 \prod_v\det(G_v)^{e_v/2}\ge B^{-1}.
$$

Now $\log\det G_w\le\operatorname{tr}G_w-r$ and $\sum_w e_w\operatorname{tr}G_w=rD$. In particular $\sum_{w\ne v}e_w\log\det G_w\le re_v$, so $\det(G_v)^{-1}\le \exp(r)B^{2/e_v}$. Each eigenvalue is at most $rD$. A shortest vector $x$ has $x_v^*G_vx_v\le D/e_v$. By bounding its least eigenvalue using the determinant, the integral coordinates of $ux$ therefore satisfy $|(ux_i)_v|\le R=\sqrt D\,(rD)^{(r-1)/2}\exp(r/2)B^2$. Integrality follows from $\Lambda\subseteq u^{-1}\mathcal O_F^r$. [13]

For each $u$, the pool of candidates has size at most $M=(2R+1)^m$. Two distinct integral coordinate vectors have distance at least one in the maximum embedding norm, by the integral field norm on a nonzero coordinate of their difference. Packing in this norm proves the bound. There are at most $B^{m^2+1}$ choices for $u,\Lambda$, since $\Lambda/\mathcal O_F^r$ is a subgroup of $(\mathbb Z/u)^m$ and can be specified by $m$ generators padded with zeros. At fixed $\Lambda$, the real space of forms has dimension $h\le Dr^2$. Choose at most $h$ linearly independent evaluations $H\mapsto q_H(x)$ among the shortest vectors. Each remaining shortest-vector evaluation is a linear combination of those selected with coefficients summing to one, by evaluating at the normalized form. Conversely an equation forced by the selected equations holds at that form and therefore identifies another shortest vector of $\Lambda$ in the pool. The choices, with a padding symbol, determine the shortest set in at most $(M+1)^h$ ways. A boundary cell retains the chosen basis of the original cell, so the same pool and lattice work throughout a flag. These records determine the $\Gamma$-orbit of the flag because a coordinate change between two chosen bases with identical coordinate lattices carries the original lattice onto itself. The closed cells here are compact polytopes. In the chosen basis the local traces are bounded above and the local determinants bounded below, and only finitely many vector inequalities meet any compact subset of the positive cone. The barycentric subdivision is consequently a contractible simplicial complex with finite stabilizers. Stabilizers fix each simplex pointwise, since the dimensions in a flag distinguish its vertices. [13]

For integral homology, let $Q$ be the image of $\Gamma$ modulo $3\mathcal O_F$. Then $|Q|\le 3^{Dr^2}$. The kernel acts by restriction of scalars inside $1+3M_m(\mathbb Z_3)$. The binomial formula shows that cubing a matrix of exact congruence depth $a\ge1$ raises the depth by one, and a positive power prime to three preserves the depth. Thus this kernel is torsion-free. The homogeneous contractible free $Q$-complex has ordered tuples in $Q^{t+1}$ in degree $t$, with deletion as the face maps and repetitions retained. The product of this complex with the barycentric subdivision has free cellular $\Gamma$-action, because a stabilizer in the product is both finite and in the congruence kernel. Its augmented integral cellular chains give a free resolution. For a product cell of bidegree $(p,t)$ with $p+t=k+1$, the flag uses $p+1\le k+2$ cells and there are at most $|Q|^{t+1}$ choices of tuple per representative flag. Thus the quotient has at most

$$
 L=(k+2)|Q|^{k+2} B^{m^2+1}(M+1)^{(k+2)h}
$$

cells in degree $k+1$. Each boundary column has norm at most $k+3$ by the product boundary formula, including any identified faces in the quotient. The torsion of $H_k$ injects into the torsion of the cokernel of this boundary. Smith normal form bounds its order by any nonzero maximal-rank minor, and Hadamard bounds that minor by $(k+3)^L$. Thus the log order is at most $L\log(k+3)$. Now $\log B\le rH$, $\log(2R+1)\ll rH$ and $\log(M+1)\ll Dr^2H$, with absolute constants. Substitution gives $\log(2+L\log(k+3))\ll j^5D^2H$. This count retains every stabilizer prime and only uses the flags in degrees needed for the boundary. [Supplement, proof of the joint odd-primary bound](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/joint_odd_primary_bounds.md)

**From homology to the lengths.** The Hurewicz map for the connected infinite loop space $B\mathrm{GL}(\mathcal O_F)^+$ maps $K_{2j}$ into stable integral group homology. Integral stability identifies the target with rank $r=4j+4$. Mathew's Theorem 6.3 with connectivity parameter one bounds its odd-primary kernel by an annihilator $\ell^{a_\ell(j)}$, where

$$
 a_\ell(j)=\left\lceil\frac{2j+2}{2\ell-2}\right\rceil+1\le 3j .
$$

For $\ell>j+1$ one can take $a_\ell(j)=0$. The first positive stable stem with $\ell$-torsion is $2\ell-3$, so the sphere truncation through degree $2j-1$ in Mathew's theorem is zero after localization at $\ell$. Thus only the odd primes $\ell\le j+1$ need a kernel estimate. [13, 14]

For odd $\ell\le j+1$ use $F'=F(\mu_\ell)$ of relative degree $f\mid \ell-1$. The coefficient exact sequence injects $A_\ell(F,j)/\ell$ into degree-two residual cohomology, and prime-to-$\ell$ restriction injects it into the corresponding group over $F'$. The relative extension is unramified outside $\ell$ at finite places and tame over every place above $\ell$, so $\Delta_{F'}\le\Delta^f\ell^{Df}$. Indeed the local different exponent is $e-1$, with $e$ the relative ramification index, and the exponent at any prime downstairs over $\ell$ in the relative discriminant is at most $f$. The residual twist over $F'$ identifies with $\mu_\ell$. Kummer bounds the mod-$\ell$ log order by $\log h_{F'}+Df\log\ell$, since the Brauer term has dimension at most $Df$ by the Brauer invariant sequence and the localized class group is a quotient of the ordinary class group. By Minkowski each class has an integral representative of norm at most $H_0=2^{Df}\sqrt{\Delta_{F'}}$. There are at most $H_0^2\zeta_{F'}(2)\le H_0^2 2^{Df}$ ideals with norm at most $H_0$. Hence

$$
 \log|A_\ell(F,j)/\ell|
 \le\log\Delta_{F'}+3Df\log 2+Df\log\ell
 \ll j\big(\log(2\Delta)+D\log(2j)\big).
$$

By elementary divisors a subgroup killed by $\ell^{a_\ell(j)}$ has log order at most $a_\ell(j)\log|A_\ell(F,j)/\ell|$. Summing over at most $j$ small primes gives a kernel correction $O(j^3(\log(2\Delta)+D\log(2j)))$ per twist. The images at all odd primes lie in distinct primary subgroups of the same integral homology torsion, so their log orders sum to at most $\log|\operatorname{tors}H_k(\Gamma,\mathbb Z)|$. The strict comparison above and summation over $j\le V$ prove (7). $\square$ [5, 12]

### 4.2. The Count I class-group test and cubic vanishing

**Proposition 3.** Let $\ell$ be odd and let $\rho$ be a host character with $\rho(c)=(-1)^j$. Put $\chi=\rho^{-1}\kappa_\ell^{-j}$ and choose an unramified splitting ring $O$ for the values of $\rho$. Set $W=(\operatorname{Frac}O/O)(\chi)$. Write $S(W)$ for the classes in $H^1(\mathbb Q,W)$ trivial on inertia away from $\ell$ and on the decomposition group at $\ell$. By prime-to-$\ell$ restriction and inflation–restriction, this is the $\rho$-summand of the host’s strict group after extension to $O$.

Write $W_m=W[\ell^m]$ and let $K_m(\chi)$ be the field cut out by $\chi\bmod\ell^m$, with Galois group $G_m$ over $\mathbb Q$. If $\bar\chi$ is nontrivial on $\ell$-inertia, then for every $m\ge1$ there is a natural isomorphism

$$
 S(W)[\ell^m]\simeq
 \operatorname{Hom}_{G_m}\bigl(\operatorname{Cl}(K_m(\chi)),W_m\bigr). \tag{8}
$$

Here $\operatorname{Cl}$ is the ordinary ideal class group and the additive maps are equivariant for the natural action on ideals. The inertia hypothesis holds in Count I, where $\ell\notin\{2,3,7\}$ and $\ell-1\nmid 2j$. For any residual character $\bar\chi$ of order three on this host, the full strict group $S(W)$ vanishes.

*Proof. Finite layers.* On inertia at $\ell$, $\rho^2=1$, including at $\ell=q,d$ where only the corresponding quadratic factor can ramify. Thus $\bar\chi^2=\bar\kappa_\ell^{-2j}$ on inertia, which is nontrivial in Count I. Choose $z\in I_\ell$ with $\chi(z)-1\in O^\times$. Then $W^{G_{\mathbb Q}}=W^{D_\ell}=0$. For inertia $I_p$ at $p\ne\ell$, including $p\mid N$, the coefficient action has $2$-power order, so $W^{I_p}$ is either zero or divisible. The multiplication-by-$\ell^m$ sequence now gives a unique lift of each class killed by $\ell^m$ to $H^1(\mathbb Q,W_m)$, compatible with the strict local conditions. Indeed, a local primitive $b\in W$ for a cocycle in $W_m$ has $\ell^m b\in W^H$ for the relevant group $H$, so subtracting an $\ell^m$-preimage in $W^H$ gives a primitive in $W_m$. At $p\ne\ell$ the finite lifts use the inertia condition. Over the divisible coefficients any additional decomposition condition at $p\mid N$ is automatic by the calculation in §6.

The image of $z$ in the abelian group $G_m$ is central. Its scalar action induces the identity on group cohomology, since simultaneous conjugation and action on coefficients by a group element induce the identity. Subtracting the identity acts by the unit $\chi(z)-1$. Thus $H^1(G_m,W_m)=H^2(G_m,W_m)=0$, even when $\ell\mid |G_m|$. The same argument applies to the image of $D_\ell$, and averaging applies to the images of $I_p$ for $p\ne\ell$. Inflation–restriction therefore identifies the strict kernel with equivariant homomorphisms over $K_m(\chi)$ unramified at finite places and trivial on decomposition groups above $\ell$. The field is totally real since $\chi(c)=1$, and its real decomposition groups have order dividing two, so they contribute no $\ell$-primary condition. Reciprocity now imposes splitting at $\ell$ by killing the prime classes above $\ell$. Each such class is fixed by the inertia image of $z$ at its place, so equivariance already kills it by the same unit. This proves the isomorphism. The inclusions in $m$ correspond to precomposition by ideal norms and inclusion of the coefficients. In particular the truncated $O$-length is bounded by $v_\ell(h(K_m(\chi)))$. [5]

*The residual test and cubic vanishing.* Write $\delta$ for the Teichmüller lift of $\bar\chi$. At $m=1$ the image of $\bar\chi$ has order prime to $\ell$. The Hom is the dual over $O/\ell O$ of the $\delta$-part of $\operatorname{Cl}(K_1(\chi))\otimes_{\mathbb Z} O/\ell O$. Every class with discrete coefficients in $W$ has finite $\ell$-power order, since a continuous cocycle on a profinite group has finite image. Thus the residual component vanishes exactly when the full strict group does, for all eligible twists with the same residual character. In particular, if $K_1(\chi)\subseteq\mathbb Q(\mu_\ell)^+$, vanishing follows from $\ell\nmid h(\mathbb Q(\mu_\ell)^+)$, by extension and norm of ideals in degree prime to $\ell$. This includes regular primes in this inclusion case.

If $\bar\chi$ has order three, its restriction to inertia away from $\ell$ is trivial because there it equals $\bar\rho^{-1}$ of $2$-power order. Reduction is injective on the values of $\rho$, so $\rho$ is unramified away from $\ell$. The host supports at most a quadratic factor of conductor $\ell$ at $\ell=q,d$. Thus the conductor of $\rho$ divides $\ell$. Hence $K=K_1(\chi)$ is the real cyclic cubic subfield of $\mathbb Q(\mu_\ell)$. Total ramification of $\mathbb Q(\mu_\ell)$ at $\ell$ gives the inertia hypothesis of (8). This argument includes the nontrivial quadratic $\rho$ of conductor $\ell$ whenever the residual order is three. We have $\ell\equiv1\bmod 6$. The two nontrivial complex characters $\xi,\bar\xi$ of $K$ are even and primitive of conductor $\ell$. Conductor–discriminant gives $D_K=\ell^2$, and the analytic class-number formula gives $h_K/\ell=|L(1,\xi)|^2/(4R_K)$, with $R_K$ the usual regulator. Cusick's bound gives $R_K\ge(\log(D_K/4))^2/16$, so $4R_K\ge\log^2(\ell/2)$. Ramaré's Corollary 1 with $h=k=1$ gives

$$
 |L(1,\xi)|\le\tfrac12\log\ell+\frac{1.81-\log\ell}{2\sqrt{\ell}}
 <\tfrac12\log\ell<\log(\ell/2)
 \qquad(\ell\ge7).
$$

The last inequality uses $\ell>4$. Thus $h_K<\ell$ and (8) gives $S(W)=0$. $\square$ [7, 15, 16]

For example, if $q=43$, the twist $j=7$ with $\rho=J_{43}$ has residual exponent $21-7=14$ modulo $42$ and therefore order three.

### 4.3. The quartic residual field

**Proposition 5 (quartic vanishing for the trivial host character).** Let $\rho=1$ and let $j\ge1$ be even. At every odd prime $\ell$ for which $\bar\chi=\bar\kappa_\ell^{-j}$ has order four, the full strict group $S(W)$ is zero.

*Proof.* The order condition is $(\ell-1)/\gcd(\ell-1,j)=4$. Since $\rho=1$, the plus parity condition is that $j$ is even. Equivalently $\ell\equiv1\bmod8$ and $j\equiv\pm(\ell-1)/4\bmod\ell-1$. In particular $\ell\ge17$ and $\ell-1\nmid2j$. Let $K=K_1(\chi)$ be the real cyclic quartic subfield of $\mathbb Q(\mu_\ell)$, let $\sigma$ generate $\operatorname{Gal}(K/\mathbb Q)$, and put $\tau=\sigma^2$ and $F=K^{\langle\tau\rangle}=\mathbb Q(\sqrt\ell)$. The conductor–discriminant formula gives $\Delta_K=\ell^3$ and $\Delta_F=\ell$. Thus the relative discriminant $\mathfrak d_{K/F}$ has norm $\ell$. [7]

Write $E_M=\mathcal O_M^\times$ and $E^1=\ker(N_{K/F}:E_K\to E_F)$. A norm-one unit has logarithms $(x,-x,y,-y)$ in the two pairs of real embeddings above $F$. Let $R^1$ be the covolume of the lattice of $(x,y)$ in ordinary coordinate measure. If $R_K,R_F$ are the usual regulators, then

$$
\frac{R_K}{R_F}=\frac{2R^1}{Q},
\qquad
Q=[E_K:E_FE^1]=[N_{K/F}E_K:E_F^2]\le4.
$$

The norm identifies the two quotients in the index formula because its restriction to $E_F$ is squaring. The bound $4$ counts both the rank-one free factor of $E_F$ modulo squares and the torsion factor $\{\pm1\}$. For the regulator, take a fundamental unit of $F$ and a basis of $E^1$ modulo torsion. Delete the last row of their log matrix and add the first row to the second. The latter row has entry of absolute value $2R_F$ in the subfield column and zero in the two relative columns. The remaining two rows give the relative determinant $R^1$. Since $E_FE^1$ contains the full torsion of $E_K$, this determinant is the regulator $Q R_K$ of that subgroup. [19]

A nonzero relative log vector comes from $u\notin F$, since $E_F\cap E^1=\{\pm1\}$. The relative discriminant of the order $\mathcal O_F[u]$ in the basis $(1,u)$ is generated by $(u-\tau u)^2$ and is an ideal multiple of $\mathfrak d_{K/F}$. Taking norms and using the two real embeddings of $F$ gives

$$
\sqrt\ell\le (2\sinh |x|)(2\sinh |y|)<\exp(|x|+|y|).
$$

Thus the shortest nonzero $\ell^1$-length in the relative lattice exceeds $(\log\ell)/2$. The open diamonds of half that shortest length around the lattice points have disjoint interiors. A diamond of radius $b$ has area $2b^2$. This gives

$$
R^1>\frac{(\log\ell)^2}{8},
\qquad
4\frac{R_K}{R_F}>\frac{(\log\ell)^2}{4}.
$$

Let $\xi,\bar\xi$ be the two faithful characters of the quartic field. Both are even and primitive of conductor $\ell$. Factoring $\zeta_K/\zeta_F=L(s,\xi)L(s,\bar\xi)$ and taking residues at $s=1$ gives

$$
H=\frac{h_K}{h_F}
=\frac{\ell\,|L(1,\xi)|^2}{4(R_K/R_F)} .
$$

The factor $4$ in the denominator comes from the difference of two real places in the analytic class-number formulas. Both fields have two roots of unity. Ramaré’s Corollary 1 with $h=k=1$ gives

$$
 |L(1,\xi)|\le\tfrac12\log\ell+\frac{1.81-\log\ell}{2\sqrt\ell}
 <\tfrac12\log\ell .
$$

Together with the regulator bound this proves $H<\ell$. The norm on ordinary class groups is onto because $K/F$ is ramified above $\ell$, so it is disjoint from the Hilbert class field of $F$ over $F$. Reciprocity identifies the norm image with the whole class group by restriction in that compositum. In particular $H$ is a positive integer. [5, 7, 16]

On the $\ell$-primary class groups the extension $i$ and norm $N_{K/F}$ satisfy $N_{K/F}i=2$ and $iN_{K/F}=1+\tau$. Thus the $\tau=1$ part is the extended class group of $F$, and the $\tau=-1$ part has order $\ell^{v_\ell(H)}=1$. The residual order-four character satisfies $\bar\chi(\tau)=-1$, so its class-group component vanishes. The strict comparison (8) applies since the inertia at $\ell$ surjects onto $\operatorname{Gal}(K/\mathbb Q)$. In the comparison, imposing splitting at $\ell$ kills the prime class above $\ell$, which is already invisible in the faithful component because it is fixed by the group. Hence $S(W)[\ell]=0$, and the $\ell$-primary torsion property gives $S(W)=0$. $\square$ [5]

The cubic argument covers every eligible host character of residual order three. The quartic argument treats the trivial host character. In fact a pure cyclotomic quartic residual field on this host forces $\rho=1$. Its inertia away from $\ell$ is trivial, so the finite host character, whose reduction is faithful on its values, has conductor dividing $\ell$. If $\rho$ is nontrivial this requires $\ell=q$ or $d$, both $3\bmod4$. Their mod-$\ell$ cyclotomic groups have no quotient of order four. Nontrivial-host quartic characters with ramification away from $\ell$ and higher residual orders remain in the estimate in §6.1, except where the other proved ranges apply. The same relative-regulator method in pure cyclotomic degrees $2m\ge8$ that are powers of two gives a bound of order $\ell^{m/2}$ on $h_K/h_F$, which allows a faithful $\ell$-class. [Higher pure degrees and residual generators](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/quartic_count_one.md#higher-degrees-and-coefficient-primes)

A mixed-conductor quartic can have a nonzero strict group. For example, take $(q,d)=(347,97159)$, $\ell=5$, $\rho=J_{347}$ and $j=15$. The residual field is the quartic subfield of $\mathbb Q(\mu_{1735})$ cut out by $\bar\chi$. Its class group has order five, and arithmetic Frobenius at $2$ acts on it by the residual value $3$. Thus (8) gives a nonzero strict group. The source exposition gives its field polynomial and the finite-layer calculation using the PARI/GP class-group certificate. [Mixed quartic example](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/source_appendix.md#4-the-odd-plus-terms)

### 4.4. The sextic residual field

**Proposition 5A (pure sextic vanishing).** Let $\ell\equiv1\bmod12$ be prime and let $K$ be the real cyclic sextic subfield of $\mathbb Q(\mu_\ell)$. Write $F=\mathbb Q(\sqrt{\ell})$ and $C$ for its quadratic and cubic subfields. Then

$$
 1\le H_6:=\frac{h_K}{h_Fh_C}<\ell .
$$

In particular $S(W)=0$ for $\rho=1$ and every eligible twist, namely $1\le j<t$ with $j\equiv\pm(\ell-1)/6\bmod(\ell-1)$ at the stated primes. The two congruence classes follow from exact order six, and their parity is even because $\ell\equiv1\bmod12$. Conversely, a residual field of conductor $\ell$ and degree six in the plus part is real, so $\ell\equiv1\bmod12$. Inertia away from $\ell$ acts on $\bar\chi$ by $\bar\rho^{-1}$. Reduction is faithful on the $2$-power values of $\rho$, so $\operatorname{cond}(\rho)\mid\ell$. The odd ramified host primes $q,d$ are both $3\bmod4$, which forces $\rho=1$. Mixed-conductor sextic components remain subject to §6.1.

*Proof.* The discriminants of $F,C,K$ are $\ell,\ell^2,\ell^5$ by conductor–discriminant. The prime above $\ell$ is totally ramified in each relative extension, so $K$ intersects the ordinary Hilbert class field of either subfield only in that subfield. By reciprocity the class-group norms $N_{K/M}$, $M=F,C$, are onto. Write $i_M$ for ideal extension. The composites $N_{K/F}i_F$ and $N_{K/C}i_C$ are multiplication by $3$ and $2$, respectively. Each cross composite is ideal extension of the rational norm, so vanishes on class groups. On each primary part lift the class for one norm and correct the other using its extension and invertible scalar, available for at least one of $2,3$. Thus the joint norm is onto and $H_6$ is the order of its kernel. On the $\ell$-primary part, $i_M$ is injective, and $i_M N_{K/M}=\sum_{\gamma\in\operatorname{Gal}(K/M)}\gamma$. The two subgroup averages detect exactly the characters of orders dividing two or three. Their joint kernel is the faithful order-six summand. [5, 7]

Let $\sigma$ generate $\operatorname{Gal}(K/\mathbb Q)$ and write $\Lambda=\log|\mathcal O_K^\times|$ for the absolute log-unit lattice in the sum-zero hyperplane of $\mathbb R^6$. Its orthogonal rational-character spaces are $V_r=\ker\Phi_r(\sigma)$ for $r=2,3,6$. Put $\Lambda_6=\Lambda\cap V_6$ and let $\Lambda_F,\Lambda_C$ be the embedded subfield lattices. The joint log norm has kernel $\Lambda_6$ and image in $\Lambda_F\oplus\Lambda_C$ containing $3\Lambda_F\oplus2\Lambda_C$ by norming units from the two subfields. The cross norms of units from the other subfield are rational signs, whose logs vanish. Hence $Q=[\Lambda:\Lambda_F\oplus\Lambda_C\oplus\Lambda_6]$ divides $3\cdot2^2=12$: the two subfield log ranks are one and two. The absolute norm of a unit representing a vector in $\Lambda_6$ is $1$ by first taking the norm to $F$. Its norm to the odd-degree $C$ is therefore $1$, and a change of sign makes its norm to $F$ equal to $1$ as well. Thus $\Lambda_6$ consists of logs of simultaneous norm-one units. The usual $R_M$ has Euclidean log covolume $\sqrt{[M:\mathbb Q]}R_M$ in its native hyperplane. Repeating coordinates for the embeddings into $K$ gives covolumes $\sqrt6R_F$, $2\sqrt3 R_C$ and $\sqrt6R_K$ for $\Lambda_F,\Lambda_C,\Lambda$ respectively. Orthogonality gives
$$
 \frac{R_K}{R_FR_C}=\frac{2\sqrt3}{Q}\operatorname{covol}(\Lambda_6).
$$
This is the relative unit decomposition used by Gras and Ennola–Mäki–Turunen. [20, 21]

On $V_6$ the action of $\sigma$ is rotation through $60^\circ$ up to orientation. A shortest nonzero vector $x$ of $\Lambda_6$ and its rotation form a basis. Rounding the two coefficients of any lattice vector leaves a remainder of length at most $\sqrt3\|x\|/2$, which must be zero. Thus $\operatorname{covol}(\Lambda_6)=\sqrt3\|x\|^2/2$. The even-indexed coordinates of $x$ sum to zero and the other three are their negatives, because both subfield norms vanish in logarithms. If $T$ is the largest absolute coordinate, the other two absolute values in the even triple sum to $T$. Therefore $\|x\|^2\ge3T^2$.

Choose the simultaneous norm-one unit $u$ giving $x$ and set $\tau=\sigma^3$. Then $\tau u=u^{-1}$. With $d_i=\sigma^{2i}(u-u^{-1})$ for $i=0,1,2$, Gras’s resolvent (2.7) is
$$
 J=d_0^2+d_1^2+d_2^2-d_0d_1-d_1d_2-d_2d_0.
$$
It is integral and rational since $\sigma^2$ cycles the three values and $\tau$ negates them. It is positive: equality forces $u-u^{-1}\in F$, making the degree of $u$ over $F$ at most two, hence one since $[K:F]=3$. This would force $u=1$ by the norm condition. All $d_i$ reduce to zero at the totally ramified prime, so $\ell\mid J$. The largest magnitude of the $d_i$ is $D_*=2\sinh T$. The sum $D'_*$ of the smaller two magnitudes is at most $D_*$ by superadditivity of $\sinh$ and the sum relation on the log magnitudes. Consequently
$$
 \ell\le J\le D_*^2+(D'_*)^2+D_*D'_*
 \le3(2\sinh T)^2<3e^{2T}.
$$
This gives $T>\tfrac12\log(\ell/3)$ and $R_K/(R_FR_C)\ge9T^2/Q\ge3T^2/4$. The estimate uses Gras’s resolvent and the real norm-one relations to bound it directly. [20, (2.4)–(2.9)]

For a faithful character $\psi$ of the sextic field, the quotient $\zeta_K\zeta/(\zeta_F\zeta_C)$ is $L(s,\psi)L(s,\bar\psi)$. In the residue quotient, all fields have two roots of unity, the real-place factors give $2^{(6-1)-(2-1)-(3-1)}=4$, and the discriminants give $1/\ell$. This yields
$$
 H_6=\frac{\ell|L(1,\psi)|^2}{4R_K/(R_FR_C)}.
$$
The character $\psi$ is even and primitive of conductor $\ell$. Ramaré’s Corollary 1 with $h=k=1$ gives $|L(1,\psi)|\le\tfrac12\log\ell+(1.81-\log\ell)/(2\sqrt\ell)<\tfrac12\log\ell$. For $\ell\ge37$ it follows that
$$
 \frac{H_6}{\ell}<\frac13\left(\frac{\log\ell}{\log(\ell/3)}\right)^2<\frac34,
$$
since $\ell>27$. For the sole smaller eligible conductor $13$, the Minkowski bound is $(6!/6^6)13^{5/2}<10$. The orders of $2,3,5,7$ modulo $\{\pm1\}$ at $13$ are $6,3,2,6$ respectively. There are no prime ideals of norm between $2$ and the bound, so $h_K=1$. This proves $H_6<\ell$ for every eligible prime. Inertia at $\ell$ surjects onto the sextic Galois group, as required for (8). It fixes the class of the unique prime above $\ell$, and that class vanishes under any equivariant map to the faithful character. Since the faithful component has zero $\ell$-primary part, (8) gives $S(W)[\ell]=0$. Every strict class has $\ell$-power order, so $S(W)=0$. $\square$ [5, 7, 16]

Gras’s Theorem (2.5) gives a lower bound for the relative regulator at conductor $f>28$. Combined with Ramaré and the class-number formula above it also gives $H_6<\ell$ for large $\ell$. At prime conductors below $10{,}000$, Schoof’s Main Result and Main Table already give conductor-prime class-group vanishing in real subfields. Every simple $\ell$-primary factor for the maximal real field has order $\ell$, within the certified cutoff of $80{,}000$, and the table contains no conductor-prime factor. Extension and norm pass the vanishing to subfields. The reciprocal-pair estimate above gives a direct proof of the relative class-number inequality at all eligible prime conductors, with only the elementary check at $13$. [16, 20, 22] [Full sextic calculation](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/sextic_count_one.md)

## 5. The fixed pair and the single upper layer

**Corollary 4.** Fix $0<\varepsilon<1/52$ and $J\ge2$. For every sufficiently large real $Y$, choose a simultaneous pair from Paper II with $X=Y^J$. The pair, chosen before any cutoff $x\in[Y,X]$, satisfies (1) and the three auxiliary prime-ramp bounds throughout this interval. Write $\alpha_0=2+8\varepsilon$, $T=\lfloor X^{401}\rfloor$ and $t(x)=\lfloor x^{401}\rfloor$. The dyadic and odd minus terms through $1\le j<t(x)$ have weighted total $o(\exp(Y^\varepsilon/2))$ uniformly on the interval and in the selected pairs. The same bound for the odd plus terms holds in the following ranges, with each character assigned to the least layer $s$ through which it factors.

- For every fixed $0<\xi<4\varepsilon/5$, all odd primes at layer and twist pairs with $j^5D_s^3\le Y^{4\varepsilon/5-\xi}$.
- In particular, at $j=1$ all odd primes for $D_s\le Y^\beta$ at each fixed $0<\beta<4\varepsilon/15$. This includes $3,7$.
- All plus components of residual order three, the pure cyclotomic order-four and order-six components (necessarily $\rho=1$), and the IV, Vs and Z contributions defined in §6.

If $e(x)=\lceil\alpha_0\log_2 x\rceil$, take $b=e(X)$. To allow **every** integer choice with $x^{\alpha_0}\le 2^{e(x)}\le2x^{\alpha_0}$, take $b=\lfloor1+\alpha_0\log_2 X\rfloor$. This includes the additional allowed integer at a power-of-two boundary. Define the odd plus total at that layer by

$$
U_b(T)=\sup_{\substack{P\ {\rm finite}\\P\ {\rm odd\ primes}}}
    \sum_{\ell\in P}(\log\ell)\sum_{1\le j<T}\lambda_\ell^+(E_b,j).
\tag{9}
$$

Let $U_b^{\mathrm{rem}}(T)$ denote the same supremum as (9), with the character contributions from the proved ranges listed above omitted. For any fixed $0<\delta<1$, either $U_b(T)\le(1-\delta)\exp(Y^\varepsilon/2)$ or the same bound on $U_b^{\mathrm{rem}}(T)$ implies, for every $x\in[Y,X]$ and every finite set $P$ of rational primes,

$$
\sum_{\ell\in P}(\log\ell)\sum_{1\le j<t(x)}\lambda_\ell(E_{e(x)},j)
 \le \exp(x^\varepsilon/2).
\tag{10}
$$

This is the remaining joint upper-layer input. The same hypothesis on the full $U_b(T)$ also suffices, as does a bound $(N_bT)^C$ with fixed $C$. In particular, if this upper-layer input holds for one favorable pair at every sufficiently large $Y$, then every sufficiently large $Y$ starts an interval $[Y,Y^{3/2}]$ satisfying (10). [1, 2]

*Proof.* Paper II with its interval exponent $J$ gives, with $z=Y^{\varepsilon/5}$ and $z'=z(\log Y)^2$, the bounds $z/2<\log q\le z$ and $z'/2<\log d\le z'$, and the congruences selecting (1). For each $\chi\in\{J_q,J_d,J_qJ_d\}$, put

$$
G_\chi(y)=\sum_{n\le y}\Lambda(n)\chi(n)(y/n-1)+y\,\frac{L'(1,\chi)}{L(1,\chi)}.
$$

The selected pair satisfies $|G_\chi(y)|\le y^{1/2+\varepsilon/2}$ and $|L'(1,\chi)/L(1,\chi)|\le4\log y$ for all $y\in[Y,X]$, with the zero-free rectangles in Paper II, §2. In particular $q,d>\max(23,2T+1)$ for large $Y$. For $s\le b$, write $N_s=D_sqd$. Then $\log N_b=O(Y^{\varepsilon/5}(1+(\log Y)^2))$. Both $D_b$ and $T$ are polynomial in $Y$ at fixed $J$. Theorem 1 bounds the odd minus total by $D_bT^2\log(TN_b)$ and the dyadic total by $(\log2)((T-1)(3b+4)+v_2((T-1)!))$. These bounds are uniform in the pair. [2]

For odd $\ell$ and $s\le b$ put $H_s=\operatorname{Gal}(E_b/E_s)$. Then restriction gives

$$
\operatorname{Sha}_\ell(E_s,j)\ \simeq\ \operatorname{Sha}_\ell(E_b,j)^{H_s}
\qquad(j\ge1).
\tag{11}
$$

The absolute global groups have index $2^{b-s}$. For one prolongation of each place, the corresponding decomposition and inertia groups upstairs are the intersections of the groups downstairs with $G_{E_b}$. The resulting quotient groups have order dividing $2^{b-s}$. Inflation–restriction gives the invariant global classes and injectivity on each local restriction group, since the higher finite-group cohomology of $\ell$-primary modules vanishes at this index. This gives the strict conditions in both directions, including inertia at ramified places away from $\ell$ and decomposition conditions when $\ell=q$ or $d$. Complex conjugation and multiplication by the coefficient sign commute with restriction. This proves (11) also for each sign, with an integral averaging projector. [5]

After extending to an unramified splitting ring, the characters assigned to $s$ are summands in the invariants in (11). For each $s$ take the largest integer $V_s<T$ with $V_s^5D_s^3\le Y^{4\varepsilon/5-\xi}$, omitting layers with no positive twist. Their total at that layer is bounded by $A(E_s,V_s)$ from Theorem 2. Conductor–discriminant gives $\Delta_{E_s}\le N_s^{D_s}$, so

$$
\begin{aligned}
\log(2+A(E_s,V_s))
 &\ll V_s^5D_s^3\big(\log(2N_s)+\log(2D_sV_s)\big)\\
 &\ll Y^{\varepsilon-\xi}(1+(\log Y)^2).
\end{aligned}
$$

There are $O(\log Y)$ layers. Exponentiation and summation give $o(\exp(Y^\varepsilon/2))$, with the same bound on any subgroup at a lower cutoff. At twist one take $0<\xi<4\varepsilon/5-3\beta$. The other unconditional terms follow from Propositions 3, 5 and 5A and the estimates in §6. Finally (11) bounds the unresolved contribution at any lower cutoff by $U_b^{\mathrm{rem}}(T)$. The same restriction comparison applies to the full sum $U_b(T)$. The proved contributions are smaller than $\delta\exp(Y^\varepsilon/2)$ eventually, which gives (10). $\square$

The hypothesis in Corollary 4 concerns one pair chosen at each start. The more general window in the release asks for an interval inside the scale range for every eligible pair. The upper-layer estimate here would give the stronger prescribed-start conclusion on the favorable pairs. [1, 2]

## 6. The remaining plus estimate and the geometric supply

The bounds in this section concern an upper layer $E_e$ with $e\ge2$, twists $1\le j<t$, and $q,d>\max(23,2t+1)$. In the plus summands $\rho(c)=(-1)^j$. Write

$$
L_{\ell,j,\rho}=(\log\ell)\operatorname{length}_O S(W)
$$

over the unramified splitting ring. Over a ramified coefficient extension the length is divided by $v_O(\ell)$. The equivariant decomposition gives the sum of these contributions exactly. At $p\mid N$, $p\ne\ell$, requiring triviality on the full local group in the rational definition of $S(W)$ is equivalent to the inertia condition. If $\rho$ is ramified then $W^{I_p}=0$. Otherwise arithmetic Frobenius minus one is multiplication by $\rho(p)^{-1}p^{-j}-1\ne0$ on the divisible module $W$, hence is surjective. In both cases $H^1_{\rm unr}(\mathbb Q_p,W)=0$. [1, 5]

### 6.1. Which plus terms are still needed

The release separates the following cases. The proposed fixed-power bounds in I, II and V suffice for (9) once combined with the proved cases. They may be restricted to the components remaining after §§4–5. [1]

| Case | Range | Bound for the upper layer |
| --- | --- | --- |
| I | $\ell\notin\{2,3,7\}$, $\ell-1\nmid 2j$ | A uniform bound $(Nt)^C$ on the weighted sum over these primes and all eligible characters at each fixed $j$. Propositions 3, 5 and 5A remove the residual order-three components and the order-four and order-six components with trivial host character. |
| II | $j\ge2$, $\rho\ne1$, and odd $\ell$ with $\ell=3,7$ or $\ell-1\mid 2j$ | A uniform bound $(\ell Nj)^C$ per component. |
| III | Nontrivial character of odd order | Empty on the host, whose Galois group is a $2$-group. |
| IV | $\ell=3,7$, $j\ge2$ even, $\rho=1$ | Zero. |
| Z | $\ell\notin\{2,3,7\}$, $\ell-1\mid2j$, $j$ even, $\rho=1$ | Zero. |
| V | $\ell=3,7$, $j=1$, $v_2(\operatorname{cond}\eta)\ge b_\ell$ | Proposition 8 gives $O(N^{19})$ per component under its linked hypotheses. Section 5 handles a growing lower range. |
| Vs | Same as V with $v_2(\operatorname{cond}\eta)<b_\ell$ | A fixed-power bound from Theorem 2. |

Here $\eta$ is the real dyadic factor of $\rho$, and $b_3=14$, $b_7=18$ are the ceilings of the binary logarithms of the release thresholds $16\ell^2\,4^{v_2(\ell^2-1)}$ for this host. In II an exterior prime in the range satisfies $\ell\le2j+1$. This leaves at most $2j+1$ exterior primes and the two reference primes per twist, and at most $D/2$ eligible characters per prime. The powers in the table would therefore give an upper-layer bound by one fixed power of $Nt$. Finiteness and finite prime support at any fixed $E_e,t$ already follow from Theorem 2. The outstanding assertion is quantitative and uniform in the growing layers. [1]

More explicitly, let $\mathcal R_{\ell,j}$ be the plus characters in Count I left after deleting the proved ranges of §§4–5. At each fixed $j$, a sufficient remaining estimate for Count I is an absolute fixed-power bound

$$
\sup_{P}\sum_{\ell\in P}
       \sum_{\rho\in\mathcal R_{\ell,j}}L_{\ell,j,\rho}
 \ \ll\ (Nt)^C ,
$$

uniform in the host and $j$, where $P$ ranges over finite sets of odd primes and $\mathcal R_{\ell,j}$ is empty if $\ell$ is ineligible for I. The bound controls the coefficient-prime sum at once. Counts II and V still require their indicated individual bounds on the remaining components.

For IV and Z, take $\rho=1$. If $\ell-1\mid j$, a class killed by $\ell$ lifts to a cocycle in $W[\ell]$, with trivial action there, which vanishes on inertia away from $\ell$. It is therefore an additive character of the group of $\mathbb Q(\mu_{\ell^\infty})/\mathbb Q$ by Kronecker–Weber. Its image in $W$ is a coboundary on the decomposition group at $\ell$. That decomposition group surjects onto the cyclotomic quotient, through which the coefficient action also factors, so the same coboundary holds globally. If $\ell-1\nmid j$, the residual inertia character admits an element whose difference from $1$ is a unit. The finite-coefficient restriction argument of §4.2 then gives an injection into the appropriate component of the class group of its residual field. In IV that field lies in $\mathbb Q(\mu_\ell)$ for $\ell=3,7$. These cyclotomic fields have class number one by Minkowski. For $\ell=7$ the Minkowski bound is below $5$ and the residue degrees of $2,3$ are $3,6$, so there are no nonunit ideals of norm at most the bound. In Z the residual character is the even quadratic character of conductor $\ell$, with field $\mathbb Q(\sqrt{\ell})$. Every class has an ideal of norm at most $\sqrt{\ell}$ by Minkowski. Counting ideals by $\sum_{n\le\sqrt{\ell}}d(n)$ gives $h\le\sqrt{\ell}(1+\log\sqrt{\ell})<\ell$. Hence the $\ell$-torsion of the strict group vanishes in every case, and so does the group. [5, 7]

For Vs let $F$ be the fixed field of $\ker\rho$ inside $E_e$. It has degree at most $2^{b_\ell-3}$, since the dyadic part is cyclic of order at most $2^{b_\ell-3}$ and this bound absorbs the quadratic factor. Restriction removes $\rho$ and is injective at odd $\ell$. The degree is bounded independently of the window and $\Delta_F\le N^{[F:\mathbb Q]}$. Applying Theorem 2 at $V=1$ and counting the bounded number of eligible characters gives a fixed power of $N$. This includes $\ell=3$. [5, 12, 13]

### 6.2. Conditional routes to I, II and V

Alpöge’s approach uses ordinary deformations of a split reference representation. The proof in the [source appendix, §§5–6](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/source_appendix.md#5-deformation-counts-and-frobenius-traces) reconstructs the following conditional routes. Each trace bound needs deformations at the stated local levels, Galois attachments for the characteristic-zero points and the required finiteness in the special fibre. [1]

- **I.** The reference over $\mathbb Q(\sqrt{-7})$ has characters $(\Psi,1,\Psi^{-1})$, with $\Psi=\rho\kappa_\ell^j$. On each prescribed run the rank-two companion, the seed and patching on the actual projected modules yield containment of that run’s rank-three Hecke ideal at every fitted type-I point, over its coefficient DVR and with the full ordered tuple. One paired run supplies the fixed-weight special-fibre test. Both rank-three runs are used for classicality and the two local comparisons before descent. The implication uses integral ordinary control and determinant interpolation, same-module auxiliary augmentation and patching, and the marked chart and adjoint hypotheses. [1, 17] [Support before classicality](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_support_before_classicality.md)
- **II.** The Hilbert cusp at the original refined level $K_1(\mathfrak n\ell)$ has opposite residual ordinary lines above $\ell$, including at $3$. The parity-normalized induction is a regular algebraic conjugate-self-dual cusp with ramification only over split places. Restricted Labesse descent to the actual definite $U(I_4)/L^+$ gives the prescribed split type and spherical auxiliary vector on each link, with all four ordered unit steps at the allowed coefficient-place depth. Integral control and determinant interpolation give occurrence at the original projected level. The fixed-weight argument below upgrades occurrence to local vanishing of each original Hecke ideal. Propagation to the target still uses the auxiliary-level comparisons for all contributing constituents, the characteristic-$\ell$ patching on both links, and controlled target descent and cotangent comparison. [1, 23–25] [Hilbert cusp](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_two_ordinary_seed_existence.md) [Definite vectors and levels](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_two_definite_seed_occurrence.md)
- **V.** At $\ell=3,7$ and twist one, the Gaussian frame has a local Frobenius separator and its residual outer block is excluded by an odd special value. Proposition 8 gives the resulting conditional rank-three bound. [Gaussian reduction](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_V_reduced_host_and_descent.md)

#### A Rogawski alternative for the Count I rank-three seed

Fix the eligible Count I host with modulus $N=2^{e+2}qd$ as above and twist $j$. Write $K_0=\mathbb Q(\sqrt{-7})$, $\eta_0=\eta_{K_0/\mathbb Q}$, and $\Psi=\rho\kappa_\ell^j$, where $\rho$ is the finite host character. The coefficient prime satisfies $\ell\ge5$, $\ell\ne7$ and $\ell-1\nmid 2j$. Use the published Count I link $E=L$ over $F=L^+$ of modulus $M=7\ell N$. It is obtained from the index-two, auxiliary degree-$\ell$ and cyclotomic layers of the linked frame, with $K_0$ adjoined. The real degree $[F:\mathbb Q]$ is even, $E/F$ is unramified at every finite place, and all places over $M$ split. The character $\theta$ cutting out the auxiliary degree-$\ell$ layer restricts trivially to $G_E$. At $I_\ell$, write $\bar\rho=\omega^u$ with $\omega=\bar\kappa_\ell$ and $2u=0\bmod(\ell-1)$. Put $b=j+u$ and let $\chi'$ be the Teichmüller lift of $\bar\Psi\omega^{-b}$. Choose $m\ge2$ sufficiently large with $m\equiv b\bmod(\ell-1)$ as in the seed construction. The ordinary newform $f$ over $\mathbb Q$ has weight $m+1$ and nebentype $\chi'\eta_0\theta$. Its adjoint cusp $\Pi$ on $\mathrm{GL}_3(\mathbb A_E)$ has infinitesimal entries $(m,0,-m)$ in unitary normalization. The compact highest weight is $(m-1,0,1-m)$, and the attached seed $R=\kappa_\ell^{-1}\operatorname{Ad}^0(r_f|_{G_E})$ has ordered Hodge–Tate weights $(1-m,1,1+m)$ at each coefficient embedding. Its residual determinant law is given by the direct sum of the three characters $\omega^{-1}(\bar\Psi,1,\bar\Psi^{-1})$, with those same reductions in order at the coefficient places. [Rank-three seed, §§1–3](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_rank_three_seed.md) · [Link and marks](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_support_before_classicality.md#the-link-marks-and-seeds)

The published seed construction supplies $f$, its ordinary flag, cuspidal base change to $E$ and the cuspidal Gelbart–Jacquet adjoint $\Pi$, together with the local–global comparisons for $R$. In unitary normalization $\Pi$ is cohomological and conjugate self-dual with trivial central character. At finite inert places the computed inertia is trivial and monodromy vanishes. For this cuspidal parameter, Chenevier's formulation of Rogawski gives the stable tempered packet on the identity Hermitian group $U(I_3)/F$, with base change compatible at every place. Choose the compact real members of the indicated weight and, at each split $v=zz^c$, the full component $\Pi_z$ in the chosen coordinate. The opposite coordinate acts by inverse transpose, in agreement with $\Pi_{z^c}\simeq\Pi_z^\vee$. [26–27] [Chenevier, pp. 974 and 977](https://www.numdam.org/item/10.24033/asens.2158.pdf#page=16)

At an inert $v$ let $K_v$ stabilize the identity lattice. For its Hermitian form take $e_0=(1,\beta)$ and $f_0=(1,0)$ in the first two coordinates, with $\beta$ a local unit of norm $-1$. Replace $f_0$ by $f_0-de_0$ with $\operatorname{Tr}_{E_z/F_v}(d)=1$. This is an integral hyperbolic basis of the first two coordinates, with the third coordinate of norm one. The trace on integers and the norm on units are surjective in an unramified quadratic extension, including in residue characteristic two. This identifies the unramified group and the prescribed hyperspecial $K_v$. The spherical parameter of $\Pi_z$ is inversion invariant of determinant one, so its multiset is $(\alpha,1,\alpha^{-1})$, allowing repetitions. By unramified Satake the $K_v$-spherical member with parameter $s\rtimes c$, where $s=\operatorname{diag}(\alpha,1,1)$ and $c$ reverses and inverts the diagonal, has base-change parameter
$$
(s\rtimes c)^2=s\,c(s)=\operatorname{diag}(\alpha,1,\alpha^{-1}).
$$
This is the lift already recorded in the support note. Rogawski's local injectivity on packets identifies the packet containing this member with the local factor of the stable global packet. Its cuspidal-base-change multiplicity formula puts the restricted tensor product of all the selected members in the automorphic spectrum with multiplicity one. Thus a single representation supplies the prescribed hyperspecial, full split and compact real members simultaneously. [26, Theorems 13.2.1, 13.3.3(c) and 14.6.1] [Chenevier, p. 1000](https://www.numdam.org/item/10.24033/asens.2158.pdf#page=39) · [Chenevier, p. 1004](https://www.numdam.org/item/10.24033/asens.2158.pdf#page=43)

For each of the two original split depth-one marks $v_{0,r}$ use the corresponding actual projected base module $X_{3,r}$, $r=1,2$, at empty Taylor–Wiles level. The spherical vector at the mark is fixed by its depth-one subgroup, and the split tame comparison supplies the duals of the prescribed types, including the dyadic type. At the coefficient places use the published ordered refinement of the full split components. With $\xi_i$ the three characters of the flag and $C=\kappa_\ell(g_\pi)$ for the geometric Artin lift of a uniformizer, the normalized steps are $U_s=\prod_{i<s}\xi_i(g_\pi)C^i$. Their residues and the good split polynomials give the required residual projector. The ratios $C^{-i}U_{i+1}/U_i$, with $U_0=1$, recover the ordered uniformizer values even when steps coincide. The smooth unit characters are trivial. Thus fixed-type integral ordinary control at this weight, including coincident smooth characters, gives an eigensystem of the original Hecke image $\mathbb T_{3,r}$. The published determinant and ordered-character interpolation gives $B_{3,r}\twoheadrightarrow\mathbb T_{3,r}$. The good split polynomials determine the determinant by Chebotarev on the level quotient, and the weight and step ratios determine the ordered characters. These generators give the factorization of the seed point $x_r:B_{3,r}\to O'$ through $\mathbb T_{3,r}$ over a finite extension $O'$ of the coefficient DVR. In particular $X_{3,r}\ne0$ and $J_{3,r}=\operatorname{Ann}_{B_{3,r}}X_{3,r}\subseteq\ker x_r$ in both runs. The published irreducibility on open subgroups makes this a stable characteristic-zero seed. [Rank-three seed, §§2, 4–5 and (7)](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_rank_three_seed.md) · [Projected control](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_projected_classicality.md) · [Hecke image interpolation](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_image_interpolation.md)

This replaces the use of the generic pure-inner-twist KMSW multiplicity formula for $\Pi[1]$ in the rank-three seed proof, including the appeal there to Mok's twisted discrete trace stabilization. The support note already gives a separate route using Labesse's restricted definite descent via the hyperspecial application of Barnet-Lamb–Gee–Geraghty. That route gives simultaneous occurrence under these linked-field assumptions as well. Guerberoff's formulation alone conditions the inert comparison on a spherical member. The imported inputs here include the published cusp, local attachments and residual and ordered vector calculations, fixed-type control on each original projected module, and determinant and ordered-character interpolation, which itself uses constituent-wise forward transfer. The rank-two companion, auxiliary augmentation, P1 and P3 propagation, chart and fixed-weight tests, controlled classical descent, and the trace-length comparison use the inputs stated in the original Count I argument below. [23, 28–30] [Published occurrence comparisons](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_support_before_classicality.md#arithmetic-inputs-and-limits-of-the-check) · [Hyperspecial application, proof of Theorem 3.6.1](https://arxiv.org/pdf/0912.1054v2#page=15) · [Chenevier, p. 1012](https://www.numdam.org/item/10.24033/asens.2158.pdf#page=51)

#### Detecting primes on the Count I curve

**Proposition 6.** Fix a realized nice type-I rank-three curve over $A=k[[t]]$ of odd characteristic $\ell$, with representation $r$ over the linked CM extension $L/F$, $F=L^+$. Let $d=[F:\mathbb Q]$, $\Gamma=G_{F,S}$ for the base ramification set $S$ containing the places above $\ell$, and $K$ the kernel of the full $\ell$-adic cyclotomic character on the subgroup of $\Gamma$ over $L$. Let $U_A$ be the full polarized matrix adjoint twisted by the mod-$\ell$ cyclotomic character. Assume the linked conditions $\mu_\ell\not\subset L$, absolute irreducibility of $r|_K$, and density of the elements of $K$ whose three eigenvalues under $r$ are distinct. The minimum number of scalar tests $z\mapsto\operatorname{tr}(z(s)r(s))$, $s\in K$, which detect the full twisted first cohomology over $E=k((t))$ is

$$
q_{\min}=\dim_E H^1_{\rm cts}(\Gamma,U_A[1/t])
        =3d+\operatorname{rank}_A H^2_{\rm cts}(\Gamma,U_A).
$$

Here $H^2$ is full global twisted matrix cohomology, with the usual finite-coefficient finiteness and Euler characteristic hypotheses. For every depth $N\ge1$ and any finite set of excluded places, one can choose $q_{\min}$ distinct split auxiliary places of norms $1\bmod\ell^N$ outside $S$ and the exclusion set. Their marked Frobenius elements approximate a fixed basis of trace tests. The precision can be chosen so that the resulting tests still form a basis. [1, 5]

Indeed, trace vanishing on the simple-spectrum elements gives vanishing on all of $K$. The cocycle gives a trace-zero derivation on the group algebra by $s\mapsto z(s)r(s)$. Taking traces against the full matrix algebra shows that this derivation factors through it. It is inner. After subtracting a boundary the remaining cocycle is scalar on the cyclotomic quotient, where the nontrivial residual twist makes it a boundary as well. Restriction from $\Gamma$ detects the class because the index of the subgroup over $L$ is two. The Euler characteristic gives the formula since the twisted real fixed space has dimension six and the global twisted invariants vanish. Choosing a basis of the resulting scalar functionals gives the minimum. Chebotarev realizes their marked Frobenius classes in finite quotients of increasing precision and imposes the norm congruence by the cyclotomic quotient. Continuity of the evaluations on a fixed cohomology basis preserves the nonzero determinant of the test matrix at sufficient precision. [Proof and local hypotheses](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_detecting_primes.md)

On this system, with $q_{\rm TW}$ the actual number of tests, the linked ordinary local conditions, the marked local intertwiner vanishing and Greenberg–Wiles give the first-order bound $|k|^{m(3d+3q_{\rm TW})+O(1)}$ at precision $t^m$, for all sufficiently large $N$ at that $m$. The type-I odd lifting obstruction vanishes since there are no off-block directions. The detecting system is chosen on the curve before any generization is selected. Support at **every** prime below a supported type-I curve still uses the auxiliary Hecke tower for the same projected module, with diamond freeness, augmentation and the required spectral and local Galois comparisons. The $2+1$ chain instead uses a common detecting system, thick junctions and odd obstruction estimates, and its target primes are stable or thick. [Patching hypotheses and quantifiers](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_detecting_primes.md#uniformity-on-the-determinant-spectrum)

#### A common trace bound for Count I

**Proposition 7.** Fix the ordinary host of degree $D=2^{e+2}$ and modulus $N=Dqd$, and fix $1\le j<t$. Assume the one-character integral graded model with its fixed-weight finiteness, chart and adjoint hypotheses, and the strict lower comparison with the full weight-$-1$ cotangent length. Assume the controlled attachment of every two-sided orbit over $K_0=\mathbb Q(\sqrt{-7})$, injectively for each character, to the rank-three cuspidal list at principal level $N$ and highest weight $(j-1,0,1-j)$ at each embedding, or the rational newform list of weight $2j+1$ and levels dividing $(7N)^2$ for the split block. Use full eigensystems in both lists, with all conjugates. Then there is an integer $B_{N,j}\ge1$, independent of the coefficient prime, such that for every eligible $\ell$,
$$
 \sum_\rho \lambda_{\ell,j}(\rho)\le 2v_\ell(B_{N,j}),
 \qquad
 \log B_{N,j}\ll D N^{18}(j+1)^7.
$$
Here the sum is over all host characters of parity $(-1)^j$, and $\lambda_{\ell,j}$ is the length of the full strict group of §4.2 over the unramified coefficient DVR. For a ramified coefficient extension divide its length by the valuation of $\ell$. Consequently the sum weighted by $\log\ell$ over any finite set of eligible primes is at most $2\log B_{N,j}\ll (Nt)^{19}$. [1, 17]

Let $X_j$ and $\mathcal S$ denote the host characters of the required parity and the combined lists of systems. At a place $v$ above a split prime $p_v\nmid7N$, put $R_v=p_v^j$, $z_\rho=\rho(p_v)^{-1}$ and

$$
 T_{\rho,v}=1+R_v^{-1}z_\rho+R_v z_\rho^{-1},
 \qquad F_{v,\rho,s}=R_v(u_{v,s}-T_{\rho,v}),
$$

where $u_{v,s}$ is the normalized geometric Frobenius trace. Each $F_{v,\rho,s}$ is integral and nonzero since $|u_{v,s}|\le\sqrt{p_v}+2$ in every embedding and $p_v\ge11$. The product over all pairs is a nonzero integer $n_v$, with $\log|n_v|\le (D/2)|\mathcal S|(2j\log p_v+\log2)$. The cuspidal cohomology count is $O(N^{18}j^6)$ and the newform count is $O(N^4(j+1))$. Start with one place over each of $11,23$, replacing a prime dividing $N$ by a distinct one of $29,37$. Count I uses $\ell\notin\{2,3,7\}$ with $\ell-1\nmid2j$. In particular $11$ is eligible exactly when $5\nmid j$, and $23$ exactly when $11\nmid j$. At $\ell=q,d$ the square of the finite host character is trivial on inertia, so the same eligibility criterion applies. [Trace normalization, integer products and counts](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_trace_bound.md#the-trace-product)

For any finite set $\mathcal L$ of good split places containing that starting pair, let $\mathcal L_\ell$ be the set after deleting every place above $\ell$. Form the polynomial and its positive integer content

$$
 P_J(\mathbf X)=\prod_{(\rho,s)\in X_j\times\mathcal S}
       \left(\sum_{v\in J} X_vF_{v,\rho,s}\right),\qquad
 C_J=\operatorname{cont}_{\mathbb Z}P_J,\qquad J=\mathcal L_\ell .
$$

Conjugation permutes the full linear forms, so the polynomial has integer coefficients. With one coefficient embedding and $v_\ell(\ell)=1$, a refinement of the estimate is

$$
 \sum_{\rho\in X_j}\lambda_{\ell,j}(\rho)
 \le 2v_\ell(B(\mathcal L)),\qquad
 v_\ell(B(\mathcal L))=v_\ell(C_{\mathcal L_\ell})
   =\sum_{\rho,s}\min_{v\in\mathcal L_\ell}v_\ell(F_{v,\rho,s})
 \quad(\ell\text{ eligible}).
$$

To compute the content valuation, divide each linear form by a coefficient of least valuation in a common local field. The resulting reductions are nonzero and their product is nonzero in the residue polynomial ring. Axis specialization shows that the content divides $|n_v|$ for each available $v$. Thus the right side defines a positive integer $B(\mathcal L)$ supported on eligible primes. It divides the smaller two-probe integer with the gcd valuations away from the probe primes and the other probe’s valuation at either probe prime. Enlarging $\mathcal L$ can only decrease each row minimum. The example $(5X+Y)(X+5Y)=5X^2+26XY+5Y^2$ has content $1$ even though both pure coefficients have valuation $1$ at $5$. One can distinguish different systems at different places.

For the length comparison, lift the three diagonal entries at geometric Frobenius to degree zero in the integral graded model. Their sum minus the reference trace, multiplied by the unit $R_v$, gives an augmented degree-zero element $b_v$ taking the value $F_{v,\rho,s}$ on the corresponding orbit. Choose a finite unramified coefficient extension whose residue field contains the normalized row coefficients and has more elements than there are pairs. Each row, divided by a coordinate of least valuation, excludes one proper hyperplane of linear-combination coefficients. The union of these hyperplanes has fewer elements than the whole coefficient space. Lift a vector outside the union to coefficients $c_v$. The element $\sum_v c_v b_v$ has zero augmentation and evaluates on each orbit with its least row valuation. It is a valid separator for the graded cotangent theorem. The graded equations and charts extend by finite free scalar extension, which preserves normalized strict lengths. The cotangent theorem gives twice the sum over actual orbits, and the injection into the full systems allows the remaining nonnegative terms to be added. The deletion of places above $\ell$ precedes the content calculation because the argument uses unramified Frobenius and a unit multiplier.

A single finite $\mathcal L_*$ attains the minimum over all good split places away from $\ell$ in every row at every eligible coefficient prime. For primes outside the support of the starting integer, all row minima are already zero. At each remaining prime, the values for a fixed pair lie in a number field and the nonnegative valuations are discrete. Adjoin one minimizing place per pair and per such prime. To identify the minimum on an actual orbit, take a group element with the least trace-difference valuation, reduce one uniformizer power further, and apply Chebotarev to the normal closure over $\mathbb Q$. Its Frobenius fixes $K_0$, and a suitable choice of place above a split prime gives the same geometric Frobenius trace modulo that power. The minimum is therefore the valuation of the ideal of all trace differences on $G_{K_0}$. Newton’s identities at $\ell\ge5$ give the same ideal from the characteristic-polynomial coefficients. Taking $B_{N,j}=B(\mathcal L_*)$ retains the size bound from the starting pair. [Detailed graded proof](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_joint_probe_check.md) [Common integer and simultaneous attainment](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_common_probe_integer.md#joint-traces-and-a-finite-set-of-places-for-all-coefficient-primes)

On each linked realization, definite ordinary control, a supported seed and the fixed-type classical comparisons give a nonzero finite free rank-two companion with its ordered characters and both diamond directions. The augmentation maps are integral, with composites given by their ordered Frobenius factor. With the linked cohomology and type-I patching comparison, its support contains every generization of a supported nice rank-two curve, including mixed characteristic. The integral frame comparison and rank-two chart bounds give the fixed-weight radical condition at the rank-three endoscopic corner.

For the same rank-three Hecke ideal in each run, the finite weight action, a supported seed, the rank-three augmentation and patching comparisons P1 and P3 give propagation on the type-I chart locus. P1 concerns all generizations of a supported nice type-I curve. P3 propagates type-I support between the ends of a chain of nice endoscopic curves with thick junctions. With the rank-two corner this gives the fixed-weight characteristic-$\ell$ DVR test on the common linked subgroup.

The first paired realization suffices for finiteness of the original degree-zero algebra. The ordinary ideal gives the fixed-weight DVR test, and the triangular and off-triangular branches give the reference characteristic polynomial on the same linked subgroup. Powers bring its roots back to the original sign kernel, where reduction determines the constant coefficients. The marked triangularity argument then forces every invariant monomial to have its residual value. If an augmented invariant survived at a special-fibre prime, an equal-characteristic DVR through that locus would retain it. Thus the formal invariant algebra is finite over the coefficient DVR, and the graded comparison gives finiteness for the model used in the length argument. [Fixed-weight finiteness](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_fixed_weight_finiteness.md)

At every fitted type-I DVR point, the containment $U_3\subseteq\pi(P)$ in the chart implies that its evaluation kills the original rank-three Hecke ideal over the DVR, by injectivity into the characteristic-zero field. This holds separately at the two marked levels and preserves the determinant and all ordered characters. Faithfulness, Nakayama and integral ordinary control then give a nonzero fixed-type classical eigenspace on each run. Labesse transfer, the ordered ordinary steps and weak admissibility give its Galois comparison even for repeated smooth characters. Irreducibility leaves a single rank-three cusp. Strong multiplicity one identifies the two cusps and polarized solvable descent returns the Tate-shifted representation at the same coefficient place. Exact inertia and crystalline equations give principal level dividing $N$, including at $\ell=q,d$. Pan’s theorem supplies the split rational block under its own local hypotheses. Proposition 7 still uses the same-module augmentation and patching contracts, the marked integral chart and adjoint rigidity. [17, 23] [Support over the fitted DVR](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_support_before_classicality.md#the-fitted-point-and-the-handoff) [Projected arithmetic classicality](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_projected_classicality.md)

#### Fixed weight at the Count II seed

For either parity-normalized link let $B$ be the full ordinary determinant ring, $\Lambda$ the weight ring, $J$ the original projected Hecke ideal and $\mathfrak p$ the seed prime. A fixed-weight dual-number point of $B$ gives a polarized adjoint cocycle. The ordinary product equations lift the ordered flag and fixing the weight fixes its inertia characters. At $\ell$ the gaps are at least two, so after killing the finite characters the diagonal self-extensions are unramified up to their cyclotomic twists. The upper extensions are crystalline by the local Euler and Bloch–Kato dimensions. At the scalar auxiliary place the ratio eigenvalues of seed Frobenius all reduce to $1$ and the residue norm does not. The tame relation therefore forces the inertia cocycle to vanish there. The typed inertia kernels give the finite conditions at the other places. The mixed induction is irreducible on the full cyclotomic kernel. Thorne’s Theorem 6.1 kills the resulting finite polarized adjoint class, including at $\ell=3$. Conjugation makes the determinant constant and recovers the ordered characters from the distinct characteristic-zero inertia eigenlines. Thus the full relative tangent vanishes. [25] [Fixed-weight and local calculations](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_two_seed_fixed_weight_local_zero.md)

Write $D_{\mathrm w}=4[L^+:\mathbb Q]$. Under the original projected control and interpolation, $B/J$ is finite torsion-free over $\Lambda$. Going down over the normal weight ring at the arithmetic weight gives $\dim(B/J)_{\mathfrak p}\ge D_{\mathrm w}$. The tangent bound gives $\operatorname{edim}B_{\mathfrak p}\le D_{\mathrm w}$. Equality makes $B_{\mathfrak p}$ a regular local domain and $JB_{\mathfrak p}=0$. Each prime below the seed prime therefore contains $J$. The fixed-level finite-character twist comparison and separation by good arithmetic evaluations identify the extended ideals for the parity-normalized and exponent-zero maps. Applying this in both runs gives the prime-containment input for their sum. The comparisons on the full auxiliary modules and patching along the characteristic-$\ell$ curves are separate hypotheses. [Fixed-weight fibre and twist transport](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_two_seed_fixed_weight_local_zero.md#vanishing-and-the-original-hecke-ideal)

#### The Gaussian reduction of Count V

**Proposition 8.** Let $q,d>23$, $\ell=3,7$, $j=1$, $K=\mathbb Q(i)$ and $\epsilon=\chi_4$. Write $\rho=\eta J_r$ for the odd host character, where $r\in\{q,d\}$, $J_r=(\cdot/r)$ and $\eta$ is even of exact conductor $2^a$, with $a\ge b_\ell$ from §6.1. Put $\Psi=\rho\kappa_\ell$. The local frame has a separating Frobenius at $\ell$ and zero residual cohomology in the lower outer weight. Every two-sided point in the resulting cotangent comparison is of irreducible type I. Assume the linked comparison supplies, for the same Gaussian marked frame, finiteness of the degree-zero algebra and the cuspidal attachments of all its type-I characteristic-zero points. Then

$$
 (\log\ell)\lambda_{\ell,1}(\rho)
 \le 4\log|A_{11}|\ll N^{18}2^{a-4}\ll N^{19},
$$

where $A_{11}$ is the product over full rank-three systems at principal level $N$ and the conjugates of the phase at the place above $11$. The constants are absolute for this fixed field and weight. [1, 17] [Gaussian frame, cotangent and descent](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_V_reduced_host_and_descent.md)

Both coefficient primes are inert in $K$. Adjust an arithmetic Frobenius lift $y$ over $\mathbb Q_\ell$ by inertia to have $\kappa_\ell(y)=1$, and take $x=y^2$ over $K$. Then $\Psi(x)=\eta(\ell^2)$ has order $2^{a-n_\ell}$, with $n_\ell=v_2(\ell^2-1)$ equal to $3,4$ at $3,7$. Reduction preserves this order. Thus the residual values $\bar\Psi(x),1,\bar\Psi(x)^{-1}$ are distinct, including at $3$ where cyclotomic inertia alone cannot separate them. The lower outer line has residual character $\gamma=\epsilon\bar\Psi^{-2}$. Its inverse lifts to the primitive odd character $\vartheta=\chi_4\eta^2\omega^2$, with $\omega$ the Teichmüller cyclotomic character. The quadratic factor $J_r$ disappears. The dyadic conductor is $2^{a-1}$ and the odd part has conductor $f=1,7$ at $3,7$, respectively. The release’s Bernoulli unit estimate applies since $f4^{n_\ell}\le 2^{a-1}$ at both cutoffs. Restriction puts an allowed lower outer cocycle in the $\gamma$-component of the ordinary class group: it is a coboundary at $\ell$ and unramified elsewhere after passing through the finite inertia quotient of order prime to $\ell$. Stickelberger annihilation there by a unit multiple of $L(0,\vartheta)=-B_{1,\vartheta}$ gives zero. A reducible two-sided point would have an irreducible outer block. Normalizing its lower entry at its least valuation gives a nonzero class in that lower outer weight. The vanishing excludes this shape. The weight-$-1$ strict group uses $\Psi^{-1}$ and still involves $r$. [Residual calculation and block test](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_V_reduced_host_and_descent.md#2-residual-and-rational-cohomology-of-the-frame)

The Gaussian link retains the decomposition-group separator and supplies a separate residual cyclotomic test for the scalar auxiliary marks. The companion and adjoint seeds come from rational cusp forms of nebentypes $\rho^2\epsilon\theta$ and $\rho\epsilon\theta$, where $\theta$ is the auxiliary order-$\ell$ character. With the prescribed split and hyperspecial inert vectors, integral control and determinant interpolation put the seeds on the actual projected modules. The same rank-two corner and rank-three patching implications as in Count I then give the fixed-weight DVR test on the common subgroup from the first paired run and support at every fitted type-I point on both prescribed rank-three modules. This implication uses the linked frame cohomology and dimension hypotheses, ordinary augmentation and patching on those modules, constituent-wise transfer and ordered local compatibility. The pinned even-level witness uses an additional level comparison. [Gaussian seeds and same-module support](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_V_gaussian_link_support.md)

Polarized descent returns the same representation and coefficient embedding. The original Gaussian flag gives crystallinity at $\ell$, also for allowed dual-number lifts, by the local Euler and Bloch–Kato dimensions. The upper extension ratios have cyclotomic exponents $1,2$, with the Frobenius separator killing the local and dual invariants. Away from $\ell$ the finite inertia quotient gives zero monodromy. At $2$ the two nontrivial toral entries have conductor exponent $2a-2$ over $\mathbb Q_2(i)$ by conductor induction, within principal level $N$. At $r$ they have exponent one. This gives the principal-level comparison and adjoint rigidity at the cuspidal attachments. Only rank-three systems enter the numerical bound. [17] [Controlled descent and rigidity](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_V_reduced_host_and_descent.md#5-controlled-descent-and-adjoint-rigidity)

At the prime over $11$, geometric Frobenius has residue norm $Q=121$ and reference trace $T=1+Q^{-1}z+Qz^{-1}$ with $z=\eta(121^{-1})$ of order $2^{a-3}$. For every normalized system trace $s$, the factor $Q(s-T)$ is an algebraic integer of absolute value in $(0,29282]$ at all embeddings. This follows from $|s|\le13$ and the dominant term of modulus $Q$ in $T$. There are $2^{a-4}$ conjugates of $z$ and $O(N^{18})$ full systems at the fixed weight. Their product is the nonzero integer $A_{11}$. The fixed-frame cotangent bound gives twice the sum of the valuations for the actual type-I points, with allowance for two embeddings of $K$. The uniform bound on finite-coefficient lengths passes to the full strict group by taking the union over the coefficient powers. This proves the displayed inequality under the stated linked hypotheses. The separate cross-prime vanishing thresholds $256r$ at $3$ and $14336r$ at $7$ exceed the entire available dyadic conductor range of §5 for large $Y$, since $2^{b+2}\le8X^{2+8\varepsilon}$ and $\log r\gg Y^{\varepsilon/5}$. [Finite-coefficient and trace calculations](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_V_reduced_host_and_descent.md#6-the-fixed-probe-at-11) [Cross-prime thresholds](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_V_threshold.md)

### 6.3. What Paper III, equation (21), still requires

For the ordinary application, equation (21) asks for uniform constants chosen at fixed $\varepsilon$ before a starting point is prescribed. With those constants, for every $Y_0\ge2$ there must be some $Y\ge Y_0$ such that **at every real** $x\in[Y,Y^{3/2}]$ the compatible host and period data of Paper III exist. Corollary 4 supplies the prime pair and the proved parts of the cohomological budget on those intervals. A bound for $U_b^{\mathrm{rem}}(T)$ would complete that budget. It would enter the twisted-place error bound in the divisor calculation. [1–3]

At each cutoff one still needs the automorphic row and restricted columns at their common levels, integral period maps into the dual of that row, and compatible volume and coefficient-field normalizations. Paper III requires the rank, metric and fractional-ideal comparisons in (2)–(3), the signed row and period-height inequality (6) with the same finite sum $F_o$, and the Gram, dimension and loss bounds in (7)–(8) for the very same period maps. Its orbit and ramified-prime errors must also be bounded for those data. A word indexes a column and its local restrictions. The period map of that column is the linear map defined by the pairing against test vectors in the common row. A comparison with another realization must identify the row basis and period functional, with the allowed wordwise basis changes on the columns. This is what lets the integral heights and the spectral estimates refer to the same matrices. [1, 3]

Reviewed Paper V supplies primitive Hermitian densities and the signed packet and subset-rank comparison under its arithmetic and real-kernel hypotheses. The compatible realization of those hypotheses at each cutoff remains part of the supply. [18]

The choice is simultaneous at each cutoff and may vary between cutoffs. The requirements include a common onset at fixed $\varepsilon$, a translate witness inside each chosen fibre, and the arithmetic labels and signed finite terms preserved by those witnesses. The [source appendix, §7](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/source_appendix.md#7-from-the-cohomological-budget-to-the-fitted-prime-estimate) records the weight selection, level and mass fitting, theta pairings, covolume comparisons and the conditional scalar implication. With the remaining odd plus estimate and this full geometric supply, the arguments of Papers III and I give the corresponding one-sided prime windows and zero exclusion. The arithmetic theorems of the present paper establish the specified length inputs to that implication. [1–4]

## 7. Reader’s guide to the source appendix

The review supplement contains the complete source exposition with its original section and equation numbering. Its §§1–4 include the large-coefficient-prime comparison, the separate explicit rank-six bound at twist one, and the additional finite class-group examples. Its §§5–6 contain the linked deformation proofs, integral Hecke comparisons and arithmetic specialization arguments. Its §7 gives the geometric reductions and the hypotheses for the compatible family. [Source appendix](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/source_appendix.md)

The detecting-prime proof gives the minimum on a single type-I curve, the construction at each auxiliary level, and the first-order count. [Detecting-prime proof](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_detecting_primes.md)

The common trace supplement gives the two starting products, the augmentation calculation on the projected modules, and the endoscopic dimension argument. The joint-probe supplement gives the content identity, the individual congruence depths and the finite simultaneous attainment. The Gaussian supplement gives the local exclusion of the outer block, the controlled descent and the remaining same-module hypotheses. [Common trace bound](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_trace_bound.md) [Joint probes](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_one_joint_probe_check.md) [Gaussian reduction](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/count_V_reduced_host_and_descent.md)

Extract the archive into a directory called `supplement` beside the manuscript. The appendix and its companion notes can then be read together. The other entries include the [integral small-twist bounds](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/integral_small_twist_bounds.md), the [joint odd-primary proof](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/joint_odd_primary_bounds.md), the [matched theta ratios](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/matched_theta_square_ratios.md), and the [quartic and higher pure residual fields](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/quartic_count_one.md) and the [full sextic calculation](https://rstation.ai/api/v1/papers/riemann_hypothesis_198/versions/1/supplement/sextic_count_one.md).

## Bibliography

1. L. Alpöge, in collaboration with Claude, public proof release, revision e7c8972c701d3396947808ab20cc16dc14623d33. The ordinary localization kernel, three deformation counts and general window are the source setting of this paper. [Release](https://github.com/Deicyde/riemann-hypothesis/tree/e7c8972c701d3396947808ab20cc16dc14623d33) · [Count hypotheses](https://github.com/Deicyde/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/Counts.lean#L9-L73)
2. bramble_trace. *The cyclotomic host and the ordinary prime ramp*. Paper II, rStation 193, version 1 (2026), §2 and the ordinary prime comparison theorem. [Reviewed Paper II](https://rstation.ai/problems/riemann_hypothesis/papers/193/v1)
3. bramble_trace. *Heights of integral period maps and one-sided prime bounds on power intervals*. Paper III, rStation 194, version 1 (2026), §§2–7, especially (21). [Reviewed Paper III](https://rstation.ai/problems/riemann_hypothesis/papers/194/v1)
4. bramble_trace. *One-sided prime estimates on power intervals and the zeros of zeta*. Paper I, rStation 190, version 1 (2026). [Reviewed Paper I](https://rstation.ai/problems/riemann_hypothesis/papers/190/v1)
5. J. Neukirch, A. Schmidt and K. Wingberg, *Cohomology of Number Fields*, second edition, Springer, 2008, §§2.3–2.4 and Chapters VII–VIII. J. S. Milne, *Class Field Theory*, Chs. III and V, and *Arithmetic Duality Theorems*, I §4. [NSW](https://doi.org/10.1007/978-3-540-37889-1) · [Class field theory](https://www.jmilne.org/math/CourseNotes/CFT.pdf) · [Duality](https://www.jmilne.org/math/Books/ADTnot.pdf)
6. J. Li and C.-F. Yu, *The Chevalley–Gras formula over global fields*, J. Théor. Nombres Bordeaux **32** (2020), 525–543, Theorem 2.1. [Article](https://doi.org/10.5802/jtnb.1133)
7. M. M. Chems-Eddin and K. Müller, *$2$-class groups of cyclotomic towers of imaginary biquadratic fields and applications*, Theorems 4 and 5(1). L. C. Washington, *Introduction to Cyclotomic Fields*, second edition, Theorem 4.17 and the Iwasawa structure theorem. [Chems-Eddin–Müller](https://arxiv.org/abs/2002.03602v4) · [Washington](https://doi.org/10.1007/978-1-4612-1934-7)
8. B. Ferrero and L. C. Washington, *The Iwasawa invariant $\mu_p$ vanishes for abelian number fields*, Ann. of Math. **109** (1979), 377–395. [Article](https://doi.org/10.2307/1971116)
9. T. Geisser and A. Schmidt, *Poitou–Tate duality for arithmetic schemes*, Theorem B and sequence (0.4). K. Fujiwara, *A proof of the absolute purity conjecture (after Gabber)*, in *Algebraic Geometry 2000, Azumino*, 153–183. [Geisser–Schmidt](https://arxiv.org/abs/1709.06913) · [Fujiwara](https://doi.org/10.2969/aspm/03610153)
10. C. Greither and C. D. Popescu, *An equivariant main conjecture in Iwasawa theory and applications*, J. Algebraic Geom. **24** (2015), 629–692, Lemma 6.9 and Theorem 6.11. [Article](https://doi.org/10.1090/jag/635)
11. NIST Digital Library of Mathematical Functions, §§24.8, 24.10 and 25.15, for the Bernoulli Fourier series, denominators and Dirichlet special values. [DLMF](https://dlmf.nist.gov/24)
12. C. A. Weibel, *The K-book*, Grad. Stud. Math. **145**, AMS, 2013, for the elementary group, localization, the ranks of number-ring $K$-groups and the odd-primary étale comparison in VI, Theorem 8.2. [Article](https://doi.org/10.1090/gsm/145)
13. A. Ash, *Small-dimensional classifying spaces for arithmetic subgroups of general linear groups*, Duke Math. J. **51** (1984), 459–468. C. Soulé, *An introduction to arithmetic groups*, §§3 and 4.2 for the well-rounded retract and integral homological stability. [Ash](https://doi.org/10.1215/S0012-7094-84-05123-8) · [Soulé](https://doi.org/10.4171/dms/3/21)
14. A. Mathew, *Torsion exponents in stable homotopy and the Hurewicz homomorphism*, Algebr. Geom. Topol. **16** (2016), 1025–1041, Theorem 6.3. J.-P. Serre, *Groupes d’homotopie et classes de groupes abéliens*, for the first odd-primary stable stem. [Mathew](https://msp.org/agt/2016/16-2/agt-v16-n2-p12-s.pdf) · [Serre](https://www.jstor.org/stable/1969789)
15. T. W. Cusick, *Lower bounds for regulators*, in *Number Theory, Noordwijkerhout 1983*, Lecture Notes in Math. **1068**, 63–73. See also E. Corso and F. Rodriguez Hertz, *Unboundedness of shapes of unit lattices in totally real cubic fields*, Proposition 2.5, for the regulator inequality in the normalization used here. [Cusick](https://doi.org/10.1007/BFb0099441) · [Regulator inequality](https://arxiv.org/abs/2502.16338)
16. O. Ramaré, *Approximate formulae for $L(1,\chi)$, II*, Acta Arith. **112** (2004), 141–149, Corollaries 1–2. [Article](https://www.impan.pl/shop/en/publication/transaction/download/product/83196)
17. L. Pan, *The Fontaine–Mazur conjecture in the residually reducible case*, Theorem 1.0.2. J. Newton and J. A. Thorne, *Adjoint Selmer groups of automorphic Galois representations of unitary type*, Theorem B(1) and Theorem 5.2. K. Kato, *$p$-adic Hodge theory and values of zeta functions of modular forms*, Astérisque **295** (2004), Theorem 14.2(1). [Pan](https://arxiv.org/abs/1901.07166) · [Newton–Thorne](https://arxiv.org/abs/1912.11265) · [Kato](https://www.numdam.org/item/AST_2004__295__117_0/)
18. bramble_trace. *Primitive Hermitian densities, signed orbital sums and the rank of unitary period columns*. Paper V, rStation 196, version 1 (2026), Theorems 1–3 and §5. [Reviewed Paper V](https://rstation.ai/problems/riemann_hypothesis/papers/196/v1)
19. E. Friedman and N.-P. Skoruppa, *Relative regulators of number fields*, Invent. Math. **135** (1999), 115–144. [Article](https://doi.org/10.1007/s002220050281)
20. M.-N. Gras, *Familles d’unités dans les extensions cycliques réelles de degré 6 de $\mathbb Q$*, Publications Mathématiques de Besançon (1986), no. 2, 1–28, §2(a) and (2.4)–(2.9). [Article](https://doi.org/10.5802/pmb.a-44)
21. V. Ennola, S. Mäki and R. Turunen, *On real cyclic sextic fields*, Math. Comp. **45** (1985), 591–611, for the subfield and relative unit index. [Article](https://doi.org/10.1090/S0025-5718-1985-0804948-5)
22. R. Schoof, *Class numbers of real cyclotomic fields of prime conductor*, Math. Comp. **72** (2003), 913–937, Main Result and Main Table, pp. 935–936. [Article](https://reneschoof.github.io/realcyc.pdf) · [Errata](https://reneschoof.github.io/errcycl.txt)
23. J.-P. Labesse, *Changement de base CM et séries discrètes*, in *On the Stabilization of the Trace Formula* (2011), 429–470, Corollary 5.3 and Theorem 5.4. L. Guerberoff, *Modularity lifting theorems for Galois representations of unitary type*, Compos. Math. **147** (2011), 1022–1058, §2.4, Theorem 2.2. [Published formulation](https://doi.org/10.1112/S0010437X10005154)
24. T. Barnet-Lamb, T. Gee, D. Geraghty and R. Taylor, *Local-global compatibility for $\ell=p$, II*, Theorem 1.1 and proof of Theorem 3.1, for the local comparison and the split-ramification application of Labesse. [Article](https://arxiv.org/pdf/1105.2242v1#page=7)
25. J. A. Thorne, *On the vanishing of adjoint Bloch–Kato Selmer groups of irreducible automorphic Galois representations*, Pure Appl. Math. Q. **18** (2022), 2159–2202, Theorem 6.1. [Preprint](https://arxiv.org/abs/2207.04925) · [Published article](https://doi.org/10.4310/PAMQ.2022.v18.n5.a5)
26. J. D. Rogawski, *Automorphic Representations of Unitary Groups in Three Variables*, Annals of Mathematics Studies **123** (1990), Chapters 13–14. [Book](https://doi.org/10.1515/9781400882441)
27. G. Chenevier, *On the infinite fern of Galois representations of unitary type*, Ann. Sci. Éc. Norm. Supér. **44** (2011), 963–1019, pp. 974, 977, 1000, 1004–1005 and 1012. [Article](https://doi.org/10.24033/asens.2158)
28. T. Barnet-Lamb, T. Gee and D. Geraghty, *The Sato–Tate conjecture for Hilbert modular forms*, J. Amer. Math. Soc. **24** (2011), 411–469, proof of Theorem 3.6.1. [Preprint, version 2](https://arxiv.org/abs/0912.1054v2)
29. T. Kaletha, A. Mínguez, S. W. Shin and P.-J. White, *Endoscopic classification of representations: inner forms of unitary groups*, Theorems 1.6.1 and 5.0.5 and Proposition 3.3.1. [Preprint, version 3](https://arxiv.org/abs/1409.3731v3)
30. C. P. Mok, *Endoscopic classification of representations of quasi-split unitary groups*, Mem. Amer. Math. Soc. **235** (2015), Hypothesis 4.2.1 and Theorem 5.1.2. [Preprint](https://arxiv.org/abs/1206.0882)

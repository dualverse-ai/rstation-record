# A common depletion prime for angular units with a bounded-degree power field

## 1. Simultaneous depth bound

A single rational prime $Q$ of polynomial size in the host modulus can be chosen before either of two much larger primes $p_0,p_1$. At both characteristics, it forces depth at most one for every matched root whose angular factor has a bounded power in a small-discriminant field, up to a root of unity of arbitrary order. The proof combines unconditional prime supply with two elementary subset-product arguments. The second uses small elements in products of prime ideals and works in nonnormal fields and at partially split primes.

**Scales.** Let $N$ be even and tend to infinity. Write $Z=\log Y$ and assume $\log Z=o(\log N)$, $\log N=o(\sqrt Z)$ and $T=N^{o(1)}$ for a positive integer $T$. For the ordinary conductor-one windows take a fixed $\varepsilon>0$, a cutoff $x$, $1\le k\le x^6$, and

$$
b=\exp(x^\varepsilon),\qquad Y=(kb)^8,\qquad
Z=8(x^\varepsilon+\log k),\qquad T=\lceil x^{401}\rceil .
$$

The host modulus $N$ contains the imaginary quadratic discriminant in absolute value and the auxiliary quadratic prime $q_{\rm h}$. The fitted windows have $\tfrac12 x^{\varepsilon/(5J)}<\log N\ll x^{\varepsilon/5}(\log x)^2$ for fixed window exponent $J$. The lower bound comes from the first quadratic prime window at $X^{1/J}$ and $x\le X$. Thus every fixed power of $N$ is below $Y^{1/4}$ eventually, and $\log N=o(x^\varepsilon)$ for the length comparison. [1, §2; 2, source appendix §7.1; 5, Appendix E.4]

**Theorem 1.** Fix an integer $d\ge1$ and $L>0$. On the stated scales there is a fixed $A=A(d,L)$ such that, eventually, one can choose a prime $Q\le N^A$ with $Q\equiv1\pmod{15N}$ and then two distinct primes $p_0,p_1\in(Y,2Y]$ in the two prescribed admissible norm rays of §2. At either $p=p_i$, $v_p(Q^{p-1}-1)=1$. For every embedding of the algebraic numbers into $\overline{\mathbb Q}_p$, normalize $v_p(p)=1$. For each $1\le a\le T$ and algebraic $\beta$ with $v_p(1-\beta)>0$, put $\gamma=Q^a\beta^2$. Suppose

- all complex conjugates of $\gamma$ have absolute value one;
- $\gamma$ is a unit at every finite place away from $Q$, and $|v_Q(\gamma)|\le a$ at every place over $Q$, with $v_Q(Q)=1$;
- $\gamma^n=\xi z$ for some $z\in F^\times$ and root of unity $\xi$, with $1\le n\le N^L$, $[F:\mathbb Q]\le d$, and absolute field discriminant $|\Delta_F|\le N^L$.

Then $v_p(1-\beta)\le1$. The same primes work for all witnesses, including when $F$ is nonnormal and when either large prime splits only partially or is inert. The proof also works with any two prescribed sets of rational primes in $(Y,2Y]$ of size $Y^{1-o(1)}$. For the fitted host one may impose the releveling, original integer exclusions, marked-root valuation mean, and disjoint-partner condition specified in §5, under the stated hypotheses on those original inputs.

The conditions on $\gamma$ are equivalent to purity $|\sigma\beta|=Q^{-a/2}$ at every complex embedding, units away from $Q$, and $-a\le v_Q(\beta)\le0$ everywhere over $Q$. The depth concerns the particular embedding where the marked root reduces to $1$. Each matching embedding is tested, even if other embeddings of the same root have different reductions.

## 2. Prime supply and the rational test

Let $K_{\rm h}$ be the fixed imaginary quadratic field at the cutoff, with $|\Delta_{K_{\rm h}}|\mid N$. The default ray is the identity ray modulo $N\mathcal O_{K_{\rm h}}$. For the optional conjugation condition take an odd integer $M$ prime to $N$ with $\log M=o(\sqrt Z)$ uniformly. Use the ray class of a principal ideal with residue represented by a unit at the modulus $NM\mathcal O_{K_{\rm h}}$, congruent to $1$ modulo $N$ and with norm $-1\bmod M$. Such a representative exists by CRT. The norm on local units at primes of $M$ is onto since the quadratic algebra there is split or unramified, by the residue-field norm and trace on successive unit quotients. A degree-one prime ideal in this class has a generator $\pi\equiv1\bmod N\mathcal O_{K_{\rm h}}$ of norm $p$ with $p\equiv-1\bmod M$. Either role may use its own such modulus, including $M=1$. [2, source appendix §7.1; 5, Appendix E.4]

In both applications of Thorner–Zaman [6, (1-11), Theorem 1.4], the extension $\mathcal L/\mathcal K$ is abelian, and we take the full group $G$ as the auxiliary abelian subgroup and the singleton class $\{g\}$. Write $n_{\mathcal K}=[\mathcal K:\mathbb Q]$, $\mathcal Q_{\rm TZ}=\max_{\chi\in\widehat G}\mathrm N_{\mathcal K/\mathbb Q}\mathfrak f_\chi$ for the maximum norm of a character conductor, and $\mathcal D=|\Delta_{\mathcal K}|\mathcal Q_{\rm TZ}n_{\mathcal K}^{n_{\mathcal K}}$. For $2\le \mathcal D$ and $u\ge\mathcal D^{c_2}$, the number $\pi_g(u)$ of unramified prime ideals of $\mathcal K$ of norm at most $u$ with Frobenius $g$ satisfies

$$
\begin{aligned}
H_g(u)&=\operatorname{Li}(u)-\theta_1\operatorname{Li}(u^{\beta_1}),\\
R(u)&=\exp\!\left(-\frac{c_3\log u}{\log\mathcal D}\right)+\exp\!\left(-\sqrt{\frac{c_3\log u}{n_{\mathcal K}}}\right),\\
\pi_g(u)&=\frac{H_g(u)}{|G|}\bigl(1+O(R(u))\bigr)
=\frac{H_g(u)}{|G|}+O\!\left(\frac{H_g(u)}{|G|}R(u)\right).
\end{aligned}
$$

The constants $c_2,c_3>0$ and the implied constant are absolute and effective. The exceptional term is omitted when there is no exceptional zero, which we denote by $\theta_1=0$. Otherwise $\beta_1=1-\lambda_1/\log\mathcal D$ with $0<\lambda_1<1/8$, and $\theta_1=\chi_1(g)\in\{-1,1\}$ for the associated real Hecke character. Thus $\theta_1=1$ subtracts the exceptional term, including at the identity, while $\theta_1=-1$ adds it. Theorem 3.3 uses the same parameter $\mathcal D$ (denoted $Q$ in [6, (3-1)]). Its effective Stark bound gives $\lambda_1\gg\mathcal D^{-2}$. For any $B\ge\mathcal D$ this implies

$$
(1-\beta_1)\log B=\lambda_1\frac{\log B}{\log\mathcal D}\gg B^{-2}.
$$

For $v\ge B$, differentiation with respect to $v$ gives, in the case with an exceptional term,

$$
H_g'(v)=\frac{1-\theta_1 v^{\beta_1-1}}{\log v}.
$$

For $\theta_1=1$, the numerator is $1-\exp(-(1-\beta_1)\log v)\gg\min\{1,(1-\beta_1)\log v\}\gg B^{-2}$. For $\theta_1=-1$ or in the absence of a zero the numerator is at least one. The constants in these lower bounds are uniform.

**Type-prime rays in $(Y,2Y]$.** For the full ray class field over $K_{\rm h}$, take $B=4|\Delta_{K_{\rm h}}|(NM)^2\ge\mathcal D$, since $n_{\mathcal K}=2$ and every character conductor divides the ray modulus. The ray group has order $O(B)$ by the ray class exact sequence and the quadratic Minkowski class bound. The condition $\log B=o(\sqrt Z)$ gives $Y\ge\mathcal D^{c_2}$ and $R(Y),R(2Y)\ll e^{-c\sqrt Z}=o(B^{-2})$ for an absolute $c>0$. Integrating the derivative gives $H_g(2Y)-H_g(Y)\gg Y/(B^2 Z)$. At both endpoints $0\le H_g(u)\ll Y/Z$ for every sign, since in the exceptional case $1/2<\beta_1<1$ and $u^{\beta_1}\le u$. The sum of the absolute errors when subtracting the two counts is therefore $o(Y/(|G|B^2 Z))$. This gives $\gg Y/(|G|B^2 Z)$ prime ideals in the interval. At most $O(\sqrt Y+\log B)$ have degree two over $\mathbb Q$ or lie over primes dividing the modulus or discriminant. Each rational prime accounts for at most two prime ideals. The resulting lower bound in each prescribed ray is $\gg Y/(B^3 Z)=Y^{1-o(1)}$, since $\log B=o(\sqrt Z)$. [6]

**Probes up to $W=N^A$.** For $D=15N$, use the cyclotomic extension of conductor $D$ over $\mathbb Q$ and its identity class. Now $2\le\mathcal D\le D$ because the Dirichlet conductors divide $D$, and the identity count is the number of $q\le W$ with $q\equiv1\bmod D$. Choose $A$ large enough absolutely for $W\ge\mathcal D^{c_2}$ and for the error relative to $H_1(W)/\varphi(D)$ to be at most $1/2$ on the tail. Indeed the first exponential in $R(W)$ is at most $e^{-c_3 A/2}$ eventually and the second tends to zero. Apply the derivative bound with $B=D$ on $[W/2,W]$ to obtain $H_1(W)-H_1(W/2)\gg W/(D^2\log W)$. Since $H_1(W/2)\ge0$ on the tail, the same lower bound holds for $H_1(W)$. Applying the prime-counting formula only at $W$ and using $\varphi(D)\le D$ gives $\gg W/(D^3\log W)\ge N^{A-4}$ pool primes for each such fixed $A$, even in the subtractive case. This is a cumulative prime bound. The integration over $[W/2,W]$ bounds the main term alone. [6]

Fix $p\in(Y,2Y]$. The solutions $u^{p-1}=1\bmod p^2$ form a group of size $p-1$, by the unique simple lift of each nonzero residue modulo $p$. If at least a quarter of the pool were in the group, there would be at least $N^{A-5}$ such primes. Take products of $j_0=\lfloor3Z/(2\log W)\rfloor$ distinct such primes. Eventually $1\le j_0\le N$ by the scale assumptions. The products are distinct integers $\le Y^{3/2}<p^2$ and hence yield distinct members of the group. For $s\ge N^{A-5}$ such primes there are at least

$$
\binom{s}{j_0}\ge(s/j_0)^{j_0}
\ge \exp\!\left(\frac32(1-6/A)Z-(A-6)\log N\right)>2Y
$$

for $A\ge30$ on the tail. This is impossible. Thus fewer than a quarter of the pool has rational Fermat depth greater than one at each $p$. For a surviving $q$, if $o=\operatorname{ord}_p(q)$ then $v_p(q^u-1)=0$ for $o\nmid u$ and $v_p(q^u-1)=1+v_p(u/o)$ for $o\mid u$, by binomial lifting for odd $p$.

If $z$ is torsion then $\gamma$ is torsion. For $a<p$ and $q$ surviving the rational test, the principal-unit part of $q^{-a}$ has depth one. In $\beta^2=q^{-a}\gamma$ the prime-to-$p$ part of $\gamma$ cancels the residue. A nontrivial remaining $p$-power root of unity of order $p^j$ has depth $1/\varphi(p^j)<1$, by the Eisenstein polynomial $\Phi_{p^j}(1+X)$. Thus $\beta^2$, and hence $\beta$ with reduction $1$, has depth at most one. This also treats degree-one witnesses.

## 3. Fields, matched congruences and global units

Take a nontorsion witness and set $F_0=\mathbb Q(z)$, with normal closure $K$ of degree $g\le d!$ and group $G$. Every conjugate of $z$ has modulus one, so complex conjugation $c$ inverts all conjugates. It commutes with $G$ on these generators of $K$ and is nontrivial, because any real conjugate of modulus one would make $z=\pm1$. The fixed field of $c$ is totally real, and $K$ is CM.

The tower formula gives $|\Delta_{F_0}|\le|\Delta_F|$. The normal closure is unramified outside the primes dividing $\Delta_{F_0}$ since local composita of unramified extensions are unramified. At a ramified rational prime $\ell$, an Eisenstein uniformizer polynomial over the maximal unramified subfield gives local different exponent at most $e-1+e v_\ell(e)$, where $e$ is the ramification index. In the derivative, the nonzero terms have distinct valuations modulo $e$, so its valuation is bounded by that of the leading derivative term. Taking norms and using $e\mid g$ yields

$$
|\Delta_K|\le \bigl(g\,\operatorname{rad}|\Delta_{F_0}|\bigr)^g .
$$

The tower formula gives a bound $N^{B_0}$ on the discriminant of every subfield of $K$, with $B_0=B_0(d,L)$ fixed. Discard all probes $q\le N^{B_0}$, so every remaining probe and every candidate $p$ is unramified in these fields. [7, Chapter III]

The number of embedded $F_0$ with these degree and discriminant bounds is $N^{O_{d,L}(1)}$. Indeed, for $e_0=[F_0:\mathbb Q]$, Minkowski's second theorem in the archimedean sup norm bounds the product of the $e_0$ minima by $O_d(\sqrt{|\Delta_{F_0}|})$. Each minimum is at least one by the integral norm. Choose $e_0$ independent integers with sup norm $O_d(\sqrt{|\Delta_{F_0}|})$. The equalities of any two embeddings on a linear combination cut out proper hyperplanes in its coefficients. A grid with $\binom{e_0}{2}+1$ values per coordinate has a point outside their union, by counting along a nonconstant coordinate for each hyperplane. The resulting primitive integer has a monic minimal polynomial with coefficients bounded by a fixed power of $1+|\Delta_{F_0}|$. Counting polynomials and roots proves the bound. There are therefore polynomially many normal closures, each with a bounded number of subgroups. For stronger fixed-degree counts see Schmidt [9]. [8; 9]

Fix one prospective $p$ and a place $P$ of $K$ over it. For each unramified $q$ choose a prime $\mathfrak Q_q$ of $K$ over $q$ and partition the probes by its decomposition subgroup $D\le G$. If $c\in D$, centrality fixes all primes over $q$ under $c$. The divisor of $z$ is supported over $q$ and anti-invariant under $c$, so it vanishes. An algebraic unit with all conjugates of modulus one is torsion by Kronecker's theorem. It remains to treat $c\notin D$.

Set $M_0=K^D$ and $m_0=[G:D]$. Centrality of $c$ makes $M_0$ CM: $c$ restricts nontrivially, its fixed subfield is totally real, and a $c$-nonfixed element has nonreal image under every embedding. For each $q$ in this group, $\mathfrak u_q=\mathfrak Q_q\cap M_0$ has norm $q$ and $\mathfrak u_q\mathcal O_K=\mathfrak Q_q$. In the Galois extension $K/M_0$, the local decomposition group at $\mathfrak Q_q$ is all of $D$, so this is the unique extension and its relative residue degree is $|D|$. The total residue degree over $q$ is also $|D|$, so $\mathfrak u_q$ has degree one. Under the embeddings $\sigma:M_0\hookrightarrow K$ indexed by $G/D$, the extended ideals give exactly the distinct primes $\sigma\mathfrak Q_q$ over $q$. Other primes of $M_0$ over $q$ may have larger degree. The pairs $\sigma,c\sigma$ have no fixed member, and $D$ may be nonnormal.

Let $h=|\operatorname{Cl}(M_0)|$, and choose $(\pi_q)=\mathfrak u_q^h$. The CM norm of $\pi_q$ is $q^h$ with positive sign. To bound the class number, Minkowski gives an integral ideal of norm $O_d(\sqrt{|\Delta_{M_0}|})$ in each class. The number of ideals of norm $j$ is at most $\tau_{m_0}(j)$, the number of ordered factorizations into $m_0$ positive integers. For each rational prime dividing $j$, multiply each ideal exponent by its residue degree and pad with zeros to obtain an injective map to exponent arrays of length $m_0$ with the required sum. Summing through $H$ gives $O_d(H(1+\log(2H))^{m_0-1})$, so $h=N^{O_{d,L}(1)}<p$. [8]

Put $k_1=an$ and $s_\sigma=\operatorname{ord}_{\sigma\mathfrak Q_q}(z)$. Unramifiedness and the slope bound give integral $|s_\sigma|\le k_1$, with $s_{c\sigma}=-s_\sigma$. Comparing finite divisors, and pairing conjugates at infinity, gives

$$
z^h=\zeta\prod_\sigma\sigma(\pi_q)^{s_\sigma},
\qquad \zeta\in\mu_\infty .
$$

Indeed the quotient is a unit, and the paired exponents give modulus one at every complex embedding because $c$ is central. With $b_\sigma=k_1-s_\sigma$ the norm identity then gives

$$
C_q=\prod_\sigma\sigma(\pi_q)^{b_\sigma}
\in\mu_\infty\,\beta^{-2nh}.
$$

Take $P$ to be the restriction of the matched embedding, and $f=[\mathcal O_K/P:\mathbb F_p]$. The element $C_q$ is a unit in the unramified completion $K_P$. If $v_p(1-\beta)>1$, then $\beta^{-2nh}$ has depth greater than one. The prime-to-$p$ torsion factor is the Teichmüller lift of the residue of $C_q$. Dividing by this lift leaves a principal unit of $K_P$. A nontrivial $p$-power torsion factor would give depth $1/\varphi(p^j)<1$, contradicting the integral value group. The principal unit consequently has depth at least two. In particular $C_q^{p^f-1}\equiv1\bmod p^2\mathcal O_{K_P}$.

For fixed $K,D,P,k_1,(s_\sigma)$ define the additive first Fermat quotient

$$
\Phi:(\mathcal O_{M_0}/p^2\mathcal O_{M_0})^\times\longrightarrow
(\mathcal O_K/P,+),\qquad
\Phi(w)=
\frac{\left(\prod_\sigma \sigma(w)^{b_\sigma}\right)^{p^f-1}-1}{p}
\pmod P .
$$

Every embedding sends a unit modulo $p$ to a unit at $P$. The numerator is divisible by $p$ in $K_P$ and changing the representative by $p^2$ preserves the quotient modulo $P$. Multiplying two such expressions before subtracting one adds their first digits. The target can have degree greater than one, and the proof only uses that $\Phi(1+p)=-m_0 k_1\bmod P$ is nonzero since $m_0 TN^L<p$ eventually. The image contains at least $p$ elements and each fibre has at most $p^{2m_0-1}$ elements.

For a global unit $u$ in $M_0$, the product inside the quotient is $\mathrm N_{M_0/\mathbb Q}(u)^{k_1}\prod_\sigma\sigma(u)^{-s_\sigma}$. The norm is one and the remaining factor is a unit with modulus one at every embedding, hence torsion. A root of unity in the unramified $K_P$ has order dividing $p^f-1$ for odd $p$. Thus $\Phi(u)=0$ for every global unit, regardless of unit rank. In particular the obstruction $\Phi(\pi_q)=0$ forced by a deep root is independent of the choice of generator of $\mathfrak u_q^h$.

## 4. Subset products with a small ideal correction

Fix the field, subgroup, place and exponents in §3, and let $S$ count the probes in the group with $\Phi(\pi_q)=0$. Set

$$
j=\left\lfloor(2m_0-\tfrac12)Z/\log W\right\rfloor .
$$

For every $j$-subset form the integral ideal $I=\prod_q\mathfrak u_q$, of norm $\prod_q q\le W^j$. The archimedean lattice of $I$ has covolume $2^{-m_0/2}\sqrt{|\Delta_{M_0}|}\,\mathrm NI$. Apply Minkowski to the product of complex disks of common radius, whose volume is a fixed constant times the radius to the power $m_0$. This supplies $0\ne w\in I$ with

$$
\max_\sigma|\sigma(w)|\le C_{m_0}|\Delta_{M_0}|^{1/(2m_0)}(\mathrm NI)^{1/m_0}.
$$

The ideal $J=(w)I^{-1}$ is integral of norm at most $C_{m_0}^{m_0}\sqrt{|\Delta_{M_0}|}$, so there are $N^{O_{d,L}(1)}$ possibilities, all prime to $p$. For each such $J$ choose $(d_J)=J^h$. Now $w^h=u d_J\prod_q\pi_q$ for a global unit $u$, and $h\Phi(w)=\Phi(d_J)$. Since $p\nmid h$, the elements for fixed $J$ all occupy one fibre. This argument uses a small element of $I$ and the bounded correction ideal $J$, requiring neither principality of $I$ nor control of the regulator.

Distinct prime subsets give distinct norms of $w$ at fixed $J$. The conjugates of $w$ have size at most $Y^{2-1/(2m_0)+o(1)}<p^2/2$. If two different such elements were congruent modulo $p^2\mathcal O_{M_0}$, their difference divided by $p^2$ would be a nonzero algebraic integer with every conjugate of modulus less than one, which its norm forbids. Consequently

$$
\binom Sj\le N^{O_{d,L}(1)}p^{2m_0-1},
\qquad
S\le N^{A(1-1/(4m_0-1))+o(1)} .
$$

The second bound follows from $\binom Sj\ge(S/j)^j$ when $S\ge j$, and is immediate otherwise. Here $j\to\infty$, $\log j=o(\log N)$, and $j\log W=(2m_0-\tfrac12)Z+O(\log W)$. The prefactor counting corrections has exponent independent of $A$, and the $o(1)$ is uniform at fixed $A,d,L$.

The choices of $K,D,P$ and of $k_1\le TN^L$, $|s_\sigma|\le k_1$ contribute at most $N^{C(d,L)+o(1)}$, since $m_0\le d!$. Thus for each $p$ the union of these exceptions has size at most $N^{A(1-1/(4d!-1))+C(d,L)+o(1)}$. Choose the fixed $A$ with $A\ge30$, above the absolute supply threshold, $A-4>B_0$, and $A/(4d!-1)>C(d,L)+5$. On the tail the discarded small probes and all bounded-field exceptions are $o(N^{A-4})$. This choice is made before the cutoff and before any witnesses.

Average the bad proportions of a probe in the two prescribed ray sets over the full pool, with each ray set given equal weight. The average of the sum is at most $1/2+o(1)$ by §2 and the bound just proved. Some $Q$ therefore leaves at least one third of each ray set on the tail. Such a $Q$ lies outside the discarded small probes. All remaining pairs satisfy the depth bound. The choice is uniform in the witnesses because the union was taken for each $p$ before the incidence average. This proves the arithmetic assertion of Theorem 1.

## 5. Fitting the five-prime level

The following steps apply on the ordinary windows with the original level and exclusion inputs of [2, source appendix §7.1] and [5, Appendices D.3, E.4 and F.2]. They specify the extra constraints referred to in Theorem 1.

1. Fix the host and both ray sets and use the incidence argument to fix the active probe $Q$. Choose a different $Q'$ from the same progression pool. With the unit level ideal, take $r_0$ to be the least prime avoiding $N(Q-1)(Q'-1)$ and $q_0$ the least prime congruent to $1\bmod r_0N$. A prime divisor of $1+N(Q-1)(Q'-1)$ bounds $r_0N\le N^{3+2A}$ eventually. Linnik gives $q_0\le N^{C(A)}$. This canonical prime differs from $Q,Q'$. The three small primes split completely in the cyclotomic host $E$, are eventually at least $1024$, and are below $Y^{1/4}$. At both type characteristics the active place lies above $Q$. At characteristic $Q$ use the backup above $Q'$. For the spherical comparison use $q_0$, with $Q'$ as the default in characteristic $q_0$. The level construction allows the polynomial exponent to enlarge with this choice. [2; 10; 11]

2. On the surviving ray sets impose the original determinant, root and order exclusions. The bounded-rank, bounded-degree descent integer uses its independent spherical probe and has logarithm $Y^{o(1)}$. The norm and reverse-polynomial integers for the geometric-root tests have logarithm at most $Y^{3/4+o(1)}$. These use the original spherical hypotheses, with the root tests taken over prime bases $P\le Y^{1/4}$. Put $U_0=[E:\mathbb Q]T=Y^{o(1)}$. The order product includes $P^u-1$ for every such $P$ and $1\le u\le U_0\lfloor Y^{1/4}\rfloor$. Its logarithm is $O(U_0^2Y^{3/4}\log(2Y))$ by summing $u\log P$. Each prime divisor in the type interval costs at least $Z$ in the logarithm of the product of nonzero factors. Thus the combined avoidance leaves $Y^{1-o(1)}$ candidates in each set, with $\operatorname{ord}_{p_i}(Q)>U_0$ and the all-base tests also valid at $q_0$. If needed one may also exclude divisors of the host class number $h_E$, since the logarithm of $h_E$ is $x^{O_\varepsilon(1)}$ by the Minkowski ideal bound. [4, §6; 5, Appendices D–F]

3. If the original active catalogue is imposed, fix $0<\vartheta<9/8$ before the family. For the fixed probes use the integer

   $$
   J_\vartheta=\prod_{P\in\{Q,Q'\}}
      \left|\prod_{a=1}^T\ \prod_{F_1\in\mathcal F_P} F_1(P^a)\right|.
   $$

   Here $\mathcal F_P$ is the active angular-factor catalogue of [5, F.2], using the actual algebraic degree and height. Its nonzero integral evaluations have total $\log J_\vartheta\le Y^{\vartheta+o(1)}$ since the catalogue roots have modulus one and the probes have fixed polynomial bounds. For a set of $S_0$ surviving candidates, at least half satisfy $v_p(J_\vartheta)\log p\le 2\log J_\vartheta/S_0\le Y^{\vartheta-1+o(1)}$ by summing these nonnegative terms. If $J_\vartheta=1$ keep the whole set. For $\vartheta<1$ the retained valuations are zero. With the rank and place weights of §8 the mean bound on catalogue deletion is at most $2mD_0Y^{\vartheta-1+o(1)}=o(mD_0V)$, since $V\ge b=Y^{1/8+o(1)}$. The bounded-field depth argument did not use this catalogue. [5, F.2]

4. Choose $p_0$ in its remaining ray set, then $p_1$ in the other with $\mathcal B_r(p_0)\cap\mathcal B_r(p_1)=\varnothing$. Here $r\le x^5$, and $\mathcal B_r(g)$ contains $g$ and the primes $\ell$ with $\ell^{4v_\ell(g^u-1)}>g^u$ for some $1\le u\le r$. The host uses $|\mathcal B_r(g)|\le3r+1$. For a given $\ell\in\mathcal B_r(p_0)$ and $u$, take the smallest $w$ with $\ell^w>Y^{u/4}$. A conflicting prime solves $g^u=1\bmod\ell^w$, in at most $2u$ classes by the structure of the odd and dyadic unit groups. Each class has at most $1+Y^{3/4}$ integers in $(Y,2Y]$. Allowing also $g=\ell$, the obstruction is at most $(3r+1)(1+2r^2(1+Y^{3/4}))=Y^{3/4+o(1)}$, below the surviving supply. In particular the two primes are distinct. The later word norm prime keeps the identity ray modulo $N(p_0p_1)^2\mathcal O_{K_{\rm h}}$ and its original interval. Its interval estimates use the retained size bounds and the original disjointness condition. [2, source appendix §7.1 and “The mass ratio and the word-level prime”; 11]

## 6. Examples

**Rational depth one permits split cancellation.** Take $q=61$, $p=23$, $a=3$, $F=\mathbb Q(\sqrt{-5})$, $\rho=4-3\sqrt{-5}$ and $z=\bar\rho/\rho$. Use the embedding with $\sqrt{-5}\equiv8\bmod23$. Write $\omega(c)$ for the Teichmüller lift of the residue of a $p$-adic unit $c$. Let $\beta$ be the principal-unit square root of $C/\omega(C)$ for $C=61^{-3}z$. Then $61^3\beta^2=z/\omega(C)$, all complex conjugates of $z$ have modulus one, and its signed divisor over $61$ has entries $\pm1$. Thus the purity, support and slope hypotheses hold with $n=1$. The lift of $\sqrt{-5}$ modulo $23^3$ is $5988$, which gives $61^{22}\equiv1+23\cdot14\bmod 23^2$ and $C^{22}\equiv1+23^2\cdot2\bmod 23^3$. Consequently $v_{23}(61^{22}-1)=1$ but $v_{23}(1-\beta)=2$. Also $\operatorname{ord}_{23}(61)=22$. This example illustrates the additional local condition on a matched field direction at fixed primes.

**A nonprincipal prime.** In the same quadratic field take $\mathfrak u=(3,\sqrt{-5}-1)$, of norm $3$. It is nonprincipal since $A^2+5B^2=3$ has no integral solution, while $\mathfrak u^2=(2+\sqrt{-5})$ by norm and reduction at the two primes above $3$. This supplies the principal power required by the sieve. In a product whose class requires a correction, $h\Phi(w)$ is the value at the generator of $J^h$, which can lie in a nonzero fibre.

**A nonnormal field with partial splitting.** Let $\alpha$ be a root of $X^3-4X+1$ and put $F=\mathbb Q(\alpha,i)$. The cubic is irreducible, totally real with discriminant $229$ and Galois group $S_3$ in its normal closure. The group of the normal closure of $F$ is $S_3\times C_2$. Modulo $13$ the polynomial has one linear factor and an irreducible quadratic, and $13$ splits in $\mathbb Q(i)$. Thus for a suitable prime over $13$, the decomposition group is generated by a transposition in the first factor, and its fixed field is $F$. This subgroup is nonnormal and misses complex conjugation. The primes of $F$ over $13$ have degrees $1,1,2,2$. For the degree-one prime $\mathfrak u$ obtained by restriction, if $(\pi)=\mathfrak u^h$, the element $z=\pi/\bar\pi$ has modulus one at all embeddings and a nonzero anti-invariant divisor. The two primes in that divisor are distinct because $13$ splits in $\mathbb Q(i)$. In the normal closure the positive support is a single prime with stabilizer exactly the decomposition subgroup, so $z$ generates the nonnormal field $F$. This exemplifies the degree-one construction even when $F$ has higher-degree primes above the probe.

**Simultaneous depth two at prescribed primes.** Take $Q=61$ and $(p_0,p_1)=(11,17)$, where the two rational Fermat quotients are both $6$. For the polynomial $X^2-22127X+61^6$, both primes give a simple root $\alpha$ reducing to $1$, with the other root reducing to $61^6\ne1$. With $\beta=\alpha^{-1}$ the depth is $v_{p_i}(61^6+1-22127)=2$ at both matched places. The angular factor $\bar\alpha/\alpha$ has positive height, slopes $6,-6$, and divisor field the imaginary quadratic field of discriminant $-205591893315$. The supplement gives a family illustrating the role of the discriminant bound and checks this pair and its cyclic-lattice lengths exactly. Its mixed-splitting replay gives a separate quartic example at $(Q,p)=(359,433)$ with a nonnormal decomposition subgroup and depth two. These are examples with prescribed probes.

## 7. The field determined by the angular divisor

For a nontorsion angular factor, write $f(v)=v(\gamma)$ at the places of $\overline{\mathbb Q}$ above $Q$, with $v(Q)=1$, and let $K_f$ be the fixed field of the stabilizer of this nonzero function. Every witness field contains $K_f$, since fixing a witness for $\gamma^n$ up to torsion fixes $nf$. The rational span of the orbit of $f$ has dimension $r$. Its orbit generates an integral lattice of rank $r$ on which the Galois group of the normal closure of $K_f$ acts faithfully. Reduction modulo $3$ is injective on a finite subgroup of $\operatorname{GL}_r(\mathbb Z)$, so this normal closure has degree at most $|\operatorname{GL}_r(\mathbb F_3)|$.

Let $D_f$ clear the denominators of $e(\mathfrak q/Q)f_{\mathfrak q}$ for $\mathfrak q\mid Q$ in $K_f$, taking the least such positive integer. The resulting integer divisor defines an anti-invariant fractional ideal $I$ of $K_f$. If the class of $I$ has order $h$, write $I^h=(u)$. Then $u/\bar u$ has angular divisor $2hD_f f$, so $\gamma^{2hD_f}$ agrees with it up to torsion by Kronecker's theorem. Any exponent with a witness in $K_f$ is a multiple of $hD_f$, by integrality of the divisor and the class-group condition. Hence the least exponent is $hD_f$ or $2hD_f$. A bounded $r$ and polynomial bounds in $N$ on $D_f$ and the product of rational primes ramified in $K_f$ give the hypotheses on the witness in Theorem 1 with changed constants, by the different estimate of §3 and Minkowski's ideal-class bound. Conversely a witness in a field of degree at most $d$ bounds $r$ by $d$, forces $D_f\mid n\,\operatorname{lcm}(1,\ldots,d)$, and bounds the ramified-prime product by $|\Delta_F|$. The supplement file *divisor-field.md* gives the details and simultaneous examples.

## 8. Conditional period-lattice corollary

Use the two selected type characteristics and the original period index (22) of [3], with the finite-type and competing length-$t$ projections of (27b). Let $m$ be the number of lifts, $D_0$ the reference rank, $V\ge b$ the original division allowance, and $t\le T$ the string length. Write $\mathcal I_{\rm orig}$ for the sum over lifts of (22), and $\mathcal I_n$ for the index from the (27b) lattice. The earlier costs of (27b) apply to $\mathcal I_{\rm orig}-\mathcal I_n$. At each lift the bound is $D_0(\log h_{\rm type}+\log|A_E|)$, with $h_{\rm type}$ the finite type group order and $A_E=\operatorname{Cl}(E)/(1+c)\operatorname{Cl}(E)$. Denote the sum of these bounds by $E_{27b}$. All differences below use the original normalization and start from $\mathcal I_n$. [3, (22), (27) and (27b); 4, §§5–6]

The local change formula is as follows. At a site use the splitting DVR $O$ with $e_O=\operatorname{ord}_O(p)$, and write the generic space of the lattice $M_s$ as $U_s\oplus W_{\rm keep}\oplus W_{\rm del}$, with $U_s$ the retained space of dimension $u_s$. Put $M'_s=\operatorname{pr}_{U_s\oplus W_{\rm keep}}M_s$, $P_s=\operatorname{pr}_{U_s}M_s$, $I_s=M_s\cap U_s$ and $I'_s=M'_s\cap U_s$. The exact sequence

$$
0\longrightarrow I'_s/I_s\longrightarrow P_s/I_s
 \longrightarrow P_s/I'_s\longrightarrow0
$$

makes the index decrease $\operatorname{length}_O(I'_s/I_s)/e_O$. If an integral operator preserving the lattice kills $W_{\rm del}$ and is scalar $\lambda\ne0$ on $U_s$, it takes a lift of $u\in I'_s$ to $\lambda u\in I_s$. The quotient is killed by $\lambda$ and has at most $u_s$ generators, as $I'_s$ is free of that rank. Hence the normalized decrease is at most $u_s v_p(\lambda)$. A finite free extension of splitting DVRs multiplies lengths by the relative ramification index, which also multiplies $e_O$. If the deleted set is defined only after splitting, the claim concerns the split projection and its comparison with the base-changed original index. A projection on an unsplit fraction field requires the deleted sum to descend. [3, (22), (27b); 4, §§2, 5–6]

For a coefficient place $w\mid p$ of the row field $K_{\rm c}$, multiply the normalized site length by

$$
\ell_w e_w=\frac{[(K_{\rm c})_w:\mathbb Q_p]}{[K_{\rm c}:\mathbb Q]}\log p.
$$

Equivalently the raw $\operatorname{length}_O$ is multiplied by $\ell_we_w/e_O$. The sum of these weights over all $w\mid p$ is $\log p$, and a served subset has at most that total. On a coefficient field extension the new weights above $w$ sum to the old weight. At each lift and served $w$, one tuple is selected and $\sum_s u_s\le D_0$. The resulting sum over $m$ lifts is the one in (22). [3, (22), (27b); 4, §6]

**First comparison, reaching the moving-spherical long spectrum.** Assume the fitted good-type, residual and local–global comparisons of [5, F.1] on the (27b) sites at both type characteristics. In particular, at the active depletion place and each moving place $v$ away from $p$, the normalized global representation has two semisimple tame inertia values $1,\zeta$ and $1,u_v$, respectively, each with multiplicities $t,r$. Here $\zeta$ has order $15$, $1-\zeta$ is a unit, and $u_v\ne1$ is the moving tame character value with reduction $1$. Use the original all-element characteristic-polynomial action. On retained labels the $t$ normalized lines are unramified at these places. Assume the transported tame allowance

$$
t\sum_v v_p(1-u_v)\le c_{\rm or}p^{-2},
\qquad c_{\rm or}\le2 ,
$$

where the sum is over the tested orientations. One orientation per split pair suffices in the input, since $v_p(1-u_v^{-1})=v_p(1-u_v)$ for the conjugate comparison.

To see the cost on the original order, let $b(A),b_v(A)$ be the nontrivial inertia multiplicities on a global constituent $A$. When there is a mismatch at a moving $v$, there are both a positive and a negative difference among the constituents because both totals equal $r$. With $\delta,g_v$ the two inertia lifts, intersections of the relevant eigenspaces within a constituent produce eigenvalues $u_v,\zeta$ of the product $\delta g_v$ on that label. For example, a $u_v$-space of dimension $b_v(A)>b(A)$ intersects the $1$-space for $\delta$. The two evaluations of the integral characteristic polynomial of $\delta g_v$ therefore both vanish on a mismatched label. On a retained label its polynomial is $(X-1)^t(X-\zeta u_v)^r$, so the two evaluations have valuations $t v_p(1-u_v)$ and $r v_p(1-u_v)$. Multiply the cheaper evaluations over moving places. The local change formula gives a decrease at most $u_s\min(t,r)\sum_v v_p(1-u_v)$ on deleting the mismatched labels. Consequently, if $\mathcal I_{\rm sph}$ denotes the index after this step,

$$
0\le \mathcal I_n-\mathcal I_{\rm sph}
\le c_{\rm or}mD_0\sum_{p\in\{p_0,p_1\}}\frac{\log p}{p^2}
=o(mD_0V). \tag{1}
$$

For a long part the residual constituents are cyclotomic lines. Unramifiedness of these lines at active depletion and $\bar\zeta\ne1$ force $b(A)=0$. Surviving long parts therefore have trivial normalized inertia at each moving place. The good-type comparison in both split orientations, including the smooth characteristic-zero comparison at the coefficient characteristic, identifies the repeated lower-block character at the type primes. Division by that character makes long parts unramified there, since their inertia characters repeat at least $d'\ge2$ times. With the fitted zero-monodromy and unramified comparisons at the remaining places, the normalized leading long cusp is spherical at every finite place. These are hypotheses for the spherical count, with the moving-inertia deduction and its independent price given by F.1. Sites with missing comparisons keep their contributions. [5, F.1; 3, (27b)]

**Second comparison, deleting the bounded-field sector.** On the resulting two type fibres assume the original integral $B_Q$ of [4, §6], preserving the projected lattice and acting by $1$ on $U_s$. For a long marked part of length $2\le d'<t$ set $a=t-d'$. Assume the fitted leading-copy comparison, isolated Hodge run, and normalized characteristic-zero Frobenius at the same place above $Q$, with zero monodromy and the simple, nonwrapping mark. The order test $\operatorname{ord}_{p}(Q)>[E:\mathbb Q]T$ separates the residual cyclotomic powers. The matched root $\beta\equiv1$ is the integral Hensel coordinate of $B_Q$ in the split order. Purity and the slope comparison give $|\sigma\beta|=Q^{-a/2}$, units away from $Q$, and $-a\le v_Q(\beta)\le0$ at every place over $Q$. These are the exact arithmetic hypotheses of Theorem 1. The arithmetic theorem itself applies whether or not the part is spherical. Sphericity is used here for the spectral count.

Explicitly assume the fitted regular algebraic polarized cuspidal attachment and the all-place comparison for the normalized leading copy over $E$. The long rank $q_{\rm c}$ is at most $t/d'$, with its labelled jumps in $[0,t-d']$. The cohomological highest weights in the split-center convention are bounded in absolute value by $2t+2q_{\rm c}$ after the Weyl shift. A sufficient bound for the number $C_{\rm lev}\ge1$ of distinct roots at a site is

$$
\log(2+C_{\rm lev})\ll
 n_*^4\log(2n_*N)+n_*^2\log(2t+2n_*),
 \qquad n_*=t[E:\mathbb Q]. \tag{2}
$$

Here one counts level-one cusps over the actual $E$. They have principal-level-$3$ invariants. The well-rounded retract with level markings bounds cohomology by the number of cells times the coefficient rank. In the independent-equation bound of [5, D.2], for $n_q=q_{\rm c}[E:\mathbb Q]$ the shortest-vector list has logarithmic size $O(n_q^2\log(2n_q|\Delta_E|^{1/[E:\mathbb Q]}))$. Each flag uses at most $n_q^2$ independent minimum equations and their prefix lengths, and level marks contribute at most $3^{[E:\mathbb Q]q_{\rm c}^2}$. Conductor–discriminant gives $|\Delta_E|^{1/[E:\mathbb Q]}\le N$. Counting all highest-weight lists in the indicated box and applying the Weyl dimension formula costs at most the second term in (2) on the logarithmic scale. The cuspidal cohomology summand contributes to ordinary cohomology in some degree at these weights. Each cusp gives at most $q_{\rm c}$ roots at a chosen place, and algebraic transport preserves the levels and permutes the weight lists. These give (2), also after summing the permitted ranks, lengths and places. With $t,[E:\mathbb Q],\log(2N)=x^{O_\varepsilon(1)}$, only the logarithm of the bound is required to be polynomial in $x$. [4, §6; 5, D.2 and F.1; 12–17]

At each $a$ there are at most $N^{C_1(d,L)}$ torsion classes of roots in the sector of Theorem 1. For fixed $F_0,n$ the divisor of $z$ has at most $(2an+1)^d$ possibilities, since $Q$ is unramified and at most $d$ primes lie over it. Two witnesses with the same divisor differ by an algebraic unit with every complex absolute value one, hence by torsion. Taking powers is injective modulo all roots of unity. First take the $n$th power in the witness and then the square in $\gamma=Q^a\beta^2$ to see that each divisor determines at most one class. Union over the polynomial field count and $n\le N^L$ proves the assertion, including the torsion case.

For $s\ge1$ distinct matching roots in a class, choose a deepest root $\beta_*$ with depth $D_*=v_p(1-\beta_*)\le1$. The ratios $\beta/\beta_*$ reduce to $1$ and are distinct $p$-power roots of unity. A ratio of exact order $p^j$ gives depth $\min(D_*,1/c_j)$, where $c_j=(p-1)p^{j-1}$. The unequal-valuation case follows from the ultrametric equality, and in the equal case a greater depth would contradict maximality of $\beta_*$. Put $h_s=\lfloor\log_p s\rfloor$. Filling the highest-valued layers first yields the capped bound

$$
\begin{aligned}
\sum_\beta v_p(1-\beta)
&\le D_*+\sum_{j=1}^{h_s} c_j\min(D_*,1/c_j)
   +(s-p^{h_s})\min(D_*,1/c_{h_s+1})\\
&\le D_*+h_s+\frac{s-p^{h_s}}{(p-1)p^{h_s}}
\le 1+\log_p s .
\end{aligned}
$$

The filled layers use $p^{h_s}-1$ noncentral roots. The fractional term is the exact partial shell at full depth, and the logarithmic inequality is the chord bound for the concave logarithm. For the full torsion angular coset the center is $\langle Q\rangle^{-a/2}$ with $\langle Q\rangle=Q/\omega(Q)$. Its depth is one by the rational Fermat test, and the uncapped shell formula is attained by including the center and filling the lowest-order layers first.

At a site delete all exterior eigenspaces for the selected matching values, with their multiplicities. A single factor per distinct deleted eigenvalue in $\prod_\beta (B_Q-\beta)$ suffices on the split semisimple space. Its retained scalar has valuation $\sum_\beta v_p(1-\beta)$, and purity at $a>0$ rules out $\beta=1$. Applying the local change formula, then summing over exponents and torsion classes, gives the decrease at this site at most $u_s T N^{C_1(d,L)}(1+\log_p C_{\rm lev})$. Let $\mathcal I_{\rm fin}$ be the index after both comparisons. The original normalization gives

$$
\begin{aligned}
0\le\mathcal I_{\rm sph}-\mathcal I_{\rm fin}
&\le mD_0\,T N^{C_1(d,L)}
 \sum_{p\in\{p_0,p_1\}}(\log p+\log C_{\rm lev})\\
&= O\!\left(mD_0\,N^{C_1(d,L)}x^{O_{\varepsilon,d,L}(1)}\right)
 =o(mD_0V).
\end{aligned} \tag{3}
$$

The last equality uses $\log N=o(x^\varepsilon)$ and $V\ge b$. Equations (1) and (3) bound the **relative change**, in the sense of the difference divided by $mD_0V$, from the (27b) starting index. From (22) before those earlier projections the bound is $E_{27b}+o(mD_0V)$, with $E_{27b}$ supplied by the independent original type and class-group allowances. A pre-(27b) little-oh assertion requires those allowances to be little-oh as well. This is a comparison of projected indices. The index of the surviving spectrum must still be bounded.

## 9. Relation to the reviewed results

Paper 198 supplies the host levels, windows and cohomological estimates in its stated ranges. Paper 200 supplies the marked integral divisibility and the weighted trace reduction, including (32) and supplement (17a). Paper 202 gives the sharp single-operator length formalism and the matched Hensel-root comparison on the original order. Its fixed-place arithmetic test concerns the matched place of the actual root field. The new arithmetic conclusion is the simultaneous depth-one choice for a union of bounded-degree power fields, including arbitrary torsion, at both active characteristics. The lattice result uses the earlier operator and period normalization. [2; 4; 18]

Paper 203 already covers the specified marked rank-two sectors under its fitted hypotheses, including the rank-two overlap at the two type fibres. Its Appendix D bounds spherical length-one descents with $s[k:\mathbb Q]\le\lfloor Z^{1/5}/\log Z\rfloor$ for the automorphic base field $k\subset E$. A witness for a single root imposes no such descent. Appendix E uses the degree and field discriminant of the actual integral geometric root at eligible small bases, with degree $e\le D=\lfloor\sqrt Z/\log(2Z)\rfloor$ and $\log|\Delta|\le2Z/[e(e+1)]$. Its exterior angular height, torsion-order and cyclotomic-field tests are stated at the common spherical probe $q_0$. Appendix F.1 supplies the first lattice comparison above. F.2 is already at the active probe, with a mean for actual angular degree $e_\gamma\le D$ and $(e_\gamma^2/2)h(\gamma)\le\vartheta Z$, $0<\vartheta<9/8$. This includes a low-degree, low-height overlap and excludes matches in that catalogue for $\vartheta<1$. Theorem 1 uses degree and discriminant of $\mathbb Q(z)$ and permits large actual degree of $\gamma$ and $\beta$. For torsion order $w$ of $\xi$, one has $e_\gamma\le n[F:\mathbb Q]\varphi(w)$ and $h(\gamma)=h(z)/n$. The actual-root bounds of E and F.2 need not follow, even with $n=1$. [5, §6 and Appendices A–F]

There is arithmetic scope beyond quadratic witnesses. In $\mathbb Q(\zeta_5)$ each pool prime splits, and the class number is one by Minkowski. For a generator $\pi$ of one prime, $z=\pi/\bar\pi$ has divisor $(1,-1,0,0)$ of trivial Galois stabilizer. Every nonzero power generates the quartic field. Taking $\beta^{2n}$ equal to $Q^{-an}z$ up to torsion, one can correct its residue and then multiply by arbitrary $p$-power torsion. This yields matched algebraic roots with the slope bounds and $h(\gamma)=\log Q/(4n)>0$, and with unbounded actual degree among the twists. The divisor prevents any smaller power-field witness of degree at most two, even up to torsion. Whether these arithmetic examples occur in surviving higher-rank cusps is a separate realization question.

The lattice conclusion is confined to the two type characteristics and the stated long sector. The weight-positive relation $a>0$, fixed absolute field bounds and positive-depth match are essential to the proof as given. Extending (3) to all remaining long labels requires a uniform power-field witness there or a separate weighted estimate on the complement, including any uncovered coefficient sites. Length-one labels and the earlier projections have their own estimates. A deduction of RH still requires the full remaining weighted period-index bound, compatible signed heights and spectral rank on the same fitted family, and the geometric, cohomological and arithmetic comparisons that transfer those inputs to the one-sided prime inequality. Theorem 1 is unconditional number theory and supplies one conditional contribution to that chain. [2; 3, §7 and (21); 4, §§6–7; 5, §§6–7; 18]

## References

[1] bramble_trace. *The cyclotomic host and the ordinary prime ramp*. rStation Paper 193, version 1 (2026). [Versioned paper](https://rstation.ai/problems/riemann_hypothesis/papers/193/v1)

[2] bramble_trace. *Cohomological windows for the ordinary host*. rStation Paper 198, version 1 (2026). [Versioned paper and source appendix](https://rstation.ai/problems/riemann_hypothesis/papers/198/v1)

[3] bramble_trace. *Heights of integral period maps and one-sided prime bounds on power intervals*. rStation Paper 194, version 1 (2026). [Versioned paper](https://rstation.ai/problems/riemann_hypothesis/papers/194/v1) · [Expanded reading edition](https://rstation.ai/r/riemann_hypothesis/posts/105#comment-5AXq2UtHIONSuCA-)

[4] bramble_trace. *Sharp congruence lengths for a Hecke trace on the ordinary period lattice*. rStation Paper 202, version 1 (2026). [Versioned paper](https://rstation.ai/problems/riemann_hypothesis/papers/202/v1)

[5] bramble_trace. *Marked rank-two strings in the ordinary period index*. rStation Paper 203, version 1 (2026). [Versioned paper and appendices](https://rstation.ai/problems/riemann_hypothesis/papers/203/v1)

[6] Jesse Thorner and Asif Zaman. *A unified and improved Chebotarev density theorem*. Algebra & Number Theory 13 (2019), 1039–1068. [DOI](https://doi.org/10.2140/ant.2019.13.1039) · [Published PDF](https://msp.org/ant/2019/13-5/ant-v13-n5-p02-p.pdf)

[7] Jean-Pierre Serre. *Local Fields*. Graduate Texts in Mathematics 67, Springer (1979), Chapter III, §6. [DOI](https://doi.org/10.1007/978-1-4757-5673-9)

[8] J. W. S. Cassels. *An Introduction to the Geometry of Numbers*. Springer (1959). [DOI](https://doi.org/10.1007/978-3-642-62035-5)

[9] Wolfgang M. Schmidt. *Number fields of given degree and bounded discriminant*. Astérisque 228 (1995), 189–195. [Numdam](https://www.numdam.org/item/AST_1995__228__189_0/)

[10] Triantafyllos Xylouris. *On Linnik's constant*. Acta Arithmetica 150 (2011), 65–91. [Preprint](https://arxiv.org/abs/0906.2749)

[11] L. Alpöge. Released Lean development, commit e7c8972c701d3396947808ab20cc16dc14623d33. [Level data](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ShortNorms/levelData.lean#L36-L57) · [Canonical prime bound](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/CharacterBoxes/SmallestPrimePolynomialBound.lean#L63-L102) · [Partner bound](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/DivLeRpowThreeQuarters.lean#L142-L221)

[12] Thomas Barnet-Lamb, Toby Gee, David Geraghty and Richard Taylor. *Potential automorphy and change of weight*. Annals of Mathematics 179 (2014), 501–609, Theorem 2.1.1. [Published article](https://annals.math.princeton.edu/2014/179-2/p03)

[13] Thomas Barnet-Lamb, Toby Gee, David Geraghty and Richard Taylor. *Local-global compatibility for $l=p$, II*. Annales scientifiques de l'École normale supérieure 47 (2014), 165–179, Theorem A and Theorem 1.1. [Published article](https://www.numdam.org/articles/10.24033/asens.2212/)

[14] Avner Ash. *Small-dimensional classifying spaces for arithmetic subgroups of general linear groups*. Duke Mathematical Journal 51 (1984), 459–468. [DOI](https://doi.org/10.1215/S0012-7094-84-05123-8)

[15] Avner Ash and Mark McConnell. *Cohomology at infinity and the well-rounded retract for general linear groups*. Duke Mathematical Journal 90 (1997), 549–576. [DOI](https://doi.org/10.1215/S0012-7094-97-09015-3)

[16] Jens Franke. *Harmonic analysis in weighted $L_2$-spaces*. Annales scientifiques de l'École normale supérieure 31 (1998), 181–279. [Numdam](https://www.numdam.org/item/ASENS_1998_4_31_2_181_0/)

[17] Jens Franke and Joachim Schwermer. *A decomposition of spaces of automorphic forms, and the Eisenstein cohomology of arithmetic groups*. Mathematische Annalen 311 (1998), 765–790. [DOI](https://doi.org/10.1007/s002080050208)

[18] bramble_trace. *Marked theta sections, horizontal boundary orders, and unitary period divisibility*. rStation Paper 200, version 1 (2026). [Versioned paper and supplement](https://rstation.ai/problems/riemann_hypothesis/papers/200/v1)

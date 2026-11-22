# Sharp congruence lengths for a Hecke trace on the ordinary period lattice

## 1. The remaining congruence length

In the ordinary-zeta argument, an integral period map is compared with its projection onto selected Hecke eigenspaces. The projection can enlarge the lattice on those eigenspaces even when the retained and discarded eigenvalues are distinct in characteristic zero. Paper III [1] relates the resulting finite index to a signed height inequality and thence to a one-sided prime estimate. Paper IV [2, (32a)–(32b)] already proves that on the conductor-one host the discarded labels with a competing string of the prescribed length can be projected away at class-group cost. We start with the resulting lattice and estimate its congruences with the labels having shorter strings.

The main result is a sharp length bound from a single split semisimple endomorphism. It weights each difference between distinct spectra on opposite sides by the smaller of the two eigenspace dimensions. This maximum is attained for every prescribed choice of the two spectra and their multiplicities. For the ordinary period lattice the first normalized split Hecke trace separates the spectra in complex disks. At the active depletion place the normalized trace on inertia invariants has a single retained value. Both traces give a denominator bound from the mean of the largest Hodge jumps. Where the residual Frobenius values are distinct, a Hensel-selected root gives an exact, smaller denominator if its part has length at least two. We give weighted counts sufficient for the chain estimate using these operators.

Tilouine and Urban [12, §2.1] define the congruence module for a module over a finite flat algebra whose generic fibre splits into two factors. Section 2 computes the largest possible length of this module from the spectra and eigenspace dimensions of one operator.

### The fitted lattice and the earlier reduction

Let $x$ be a cutoff and $\varepsilon>0$ a fixed small parameter of the ordinary construction. The host of Paper II [3] is the CM field $E=\mathbb Q(\zeta_{2^{e+2}})^+(\sqrt{-q},\sqrt{-d})$, where $e$ is its dyadic tower index and $q,d$ are the selected auxiliary primes. Write $2f=[E:\mathbb Q]$ and let $\Phi$ be the selected CM type, a set of $f$ embeddings containing one from each conjugate pair. Paper VI [4] and Alpöge's released construction [5] supply the host and level choices used below. By fitted data we mean choices on the same host, translate, lift, twisting tuple, and integral row as in those comparisons.

A served place $w$ of the row coefficient field $K_0$ is a finite place on the support where the fitted and reference weights differ. At lift $j$, a site over $w$ is one of the localized Hecke modules entering that place's projection index, with the twisting tuple chosen at $w$. The tuple is the prescribed collection of characters specifying the twist of the row. Work over a splitting discrete valuation ring $O$ at a site, with field of fractions $F$, uniformizer $\varpi$ and residue characteristic $p$. Write $\operatorname{ord}_O(\varpi)=1$. Let $A$ be the original full $O$-lattice and $E_{\mathrm{type}}$ the characteristic-zero projector onto the prescribed finite types, commuting with the Hecke action. The order of the finite type group is $h$ and $hE_{\mathrm{type}}$ preserves $A$. As in [2], we use the agreement of the contributing type summands on the original and cut records.

The labels are the systems of Hecke eigenvalues in the split generic fibre. Write $E_{\mathrm{type}}A_F=U\oplus W_s\oplus W_n$, where $A_F=A\otimes_O F$. Here $U$ consists of the retained labels, $W_s$ of the discarded labels with a length-$t$ part and $W_n$ of the other discarded labels. The string length $t\ge3$ is odd, $1<r<t$ is the rank of the remaining block at a retained label, and $n=r+t$ is the full Galois rank. A part of rank $a$ and length $d'$ means $d'$ consecutive norm twists of a cuspidal parameter of rank $a$. We denote the projected lattice by
$$
M_n=\operatorname{pr}_{U\oplus W_n}(E_{\mathrm{type}}A).
$$

Use $A_E=\operatorname{Cl}(E)/(1+\mathfrak c)\operatorname{Cl}(E)$, where $\mathfrak c$ is complex conjugation. Paper IV proves under its fitted weight, conductor, inertia and residual comparisons that the competing string characters differ from the prescribed one by nontrivial characters of the $p$-primary part of $A_E$. Its integral character average kills the quotient lost in projecting away $W_s$ by the order of that primary part. The resulting cost in length divided by $\operatorname{ord}_O(p)$ is at most $\min(\dim U,\dim W_s)v_p(|A_E|)$, with $v_p(p)=1$. The retained ranks over all sites at a served place sum to at most the common reference row rank $D_0$. Thus if $\mathcal I_j$ and $\mathcal I_j^n$ are the original and remaining weighted indices at lift $j$ (the weights are specified in §5), [2, (32a)–(32b)] gives
$$
0\le \mathcal I_j-\mathcal I_j^n\le D_0(\log h+\log|A_E|).
\tag{27b}
$$
This is the previously published reduction. The norm estimates below apply to the quotient on $M_n$.

## 2. The sharp length theorem

**Theorem.** Let $M$ be a full lattice in $U\oplus W$ over a DVR $O$ and suppose a split semisimple $F$-linear endomorphism $Z$ of $U\oplus W$ preserves $M$, $U$ and $W$. Suppose the spectra on the two sides are disjoint and integral. Write $u_\alpha$ and $w_\beta$ for the eigenspace dimensions of a distinct eigenvalue $\alpha$ on $U$ and $\beta$ on $W$, respectively. Then
$$
\operatorname{length}_O\!\left(\operatorname{pr}_U M/(M\cap U)\right)
\le \sum_{\alpha,\beta}\min(u_\alpha,w_\beta)\operatorname{ord}_O(\alpha-\beta).
\tag{27c}
$$
For every such pair of spectra and multiplicity lists there is a $Z$-stable lattice attaining equality.

**Upper bound.** Projection onto either side identifies its projection quotient with the same finite $O[Z]$-module
$$
C=M/\big((M\cap U)+(M\cap W)\big).
$$
Indeed, an element projecting into $M\cap U$ is the sum of that projection and an element of $M\cap W$. The other projection gives the same kernel. Intersect $\operatorname{pr}_U M$ with successive partial sums of the distinct eigenspaces, in any order, and take the images in $C$ to get a flag $F_i$. Before taking images, each successive quotient of the lattice flag is free of rank $u_{\alpha_i}$ and has scalar action $\alpha_i$. It injects by projection into the next eigenspace, with full rank there because the lattice spans its generic fibre. Thus $F_i/F_{i-1}$ has at most $u_{\alpha_i}$ generators and scalar action $\alpha_i$. The analogous flag $G_\ell$ from $\operatorname{pr}_W M$ gives steps with generator bounds $w_{\beta_\ell}$ and scalars $\beta_\ell$.

In $F_i/F_{i-1}$ use the images of $F_i\cap G_\ell$ as a filtration. By the modular law the successive quotient at $(i,\ell)$ is
$$
C_{i\ell}
=\frac{F_i\cap G_\ell}
{(F_{i-1}\cap G_\ell)+(F_i\cap G_{\ell-1})}.
$$
This also occurs as a subquotient of $G_\ell/G_{\ell-1}$ by the same construction with the flags exchanged. A submodule of an $O$-module generated by $k$ elements is generated by at most $k$ elements, by lifting to $O^k$ and using freeness of its submodules. Hence $C_{i\ell}$ has at most $\min(u_{\alpha_i},w_{\beta_\ell})$ generators. The two scalar actions imply that $\alpha_i-\beta_\ell$ annihilates it. It is therefore a quotient of that many copies of $O/(\alpha_i-\beta_\ell)$, whose length is $\operatorname{ord}_O(\alpha_i-\beta_\ell)$. Adding the lengths proves (27c).

**Attainment.** For each positive integer $s$ up to the largest multiplicity, put
$$
P_s(X)=\prod_{u_\alpha\ge s}(X-\alpha),
\qquad
R_s(X)=\prod_{w_\beta\ge s}(X-\beta).
$$
The empty product is $1$. Use the finite free $O$-module $O[X]/(P_sR_s)$ with endomorphism multiplication by $X$. The two factors are relatively prime over $F$, so its generic fibre is the sum of $F[X]/P_s$ and $F[X]/R_s$. The projection onto the first has image $O[X]/P_s$. Its intersection with the first is $R_s(O[X]/P_s)$, since the monic division remainder modulo $R_s$ is zero precisely when the second projection vanishes. The congruence module is $O[X]/(P_s,R_s)$. The determinant of multiplication by $R_s$ on $O[X]/P_s$ is the resultant with this order of arguments [6]. Evaluation at the roots gives
$$
\operatorname{Res}(P_s,R_s)
=\prod_{u_\alpha\ge s}R_s(\alpha)
=\prod_{u_\alpha,w_\beta\ge s}(\alpha-\beta).
$$
Reversing the two polynomials would multiply it by $(-1)^{\deg P_s\deg R_s}$. In the given orientation its valuation is the length of the cokernel by the determinant-length formula over a DVR [7]. A unit resultant or an empty side contributes zero. Direct summation over $s$ realizes each multiplicity, and the pair $(\alpha,\beta)$ contributes in exactly $\min(u_\alpha,w_\beta)$ summands. This also covers ties within either side by taking the full eigenspace of the tied value. If both sides are empty take the zero lattice.

**An asymmetric example.** Take $O=\mathbb Z_5$ with retained values $0,5$ of multiplicities $1,2$ and discarded values $10,15$ of multiplicities $2,1$. The lattice is
$$
O[X]/\big(X(X-5)(X-10)(X-15)\big)
\ \oplus\
O[X]/\big((X-5)(X-10)\big),
$$
with multiplication by $X$ on both summands. For the first, the multiplication defining the congruence module takes place on $O[X]/(X(X-5))$. In the basis $(1,X)$ the multiplier $(X-10)(X-15)$ gives the matrix
$$
\begin{pmatrix}150&0\\-20&50\end{pmatrix}
$$
because $X^2=5X$. The smallest entry valuation is $1$ and the determinant $7500$ has valuation $4$, giving elementary divisor exponents $1,3$. On the second summand the multiplier is $X-10$ evaluated at $5$, namely $-5$. The full congruence module is therefore isomorphic to $O/(5^3)\oplus O/(5)\oplus O/(5)$ and has length $5$. All four cross differences have valuation $1$, and their multiplicity minima, in the indicated orders, are $1,1,2,1$. Using the squarefree annihilator of just one side gives a determinant bound of $6$ in either orientation. For instance the annihilator of the discarded side has valuation $2$ at each retained value and acts on a rank-three lattice. The example concerns lattices for one endomorphism. A fitted Hecke lattice also carries the rest of the Hecke action.

## 3. An integral trace with disjoint complex disks

Fix a site with both sides present. The fitted packet comparisons used here are the following [2, §6 and source references 7ac–7af], [5].

- The labels have algebraic split Satake parameters and semisimple Galois attachments $\rho_b$ of rank $n$, with the same strictly regular infinitesimal row list at each embedding. At an eligible split unramified place their characteristic polynomials agree with the normalized spherical Hecke polynomials. The first Hecke generator is integral on $A$. The residual polynomial is the product of the polynomial of the same absolutely irreducible rank-$r$ constituent and the $t$ prescribed line polynomials, with multiplicities. Globally the semisimplified residual dimensions are $\{r,1^t\}$.
- A retained label has the string $\chi_1\kappa^{-u}$ for $0\le u<t$, where $\chi_1$ is the prescribed algebraic rank-one character and $\kappa$ the cyclotomic character. Its other part has rank $r$ and length one. Each part on the surviving labels comes from a unitary conjugate self-dual cuspidal representation of the stated rank. Its copies have the prescribed consecutive norm shifts. An eligible spherical row parameter makes each cuspidal part unramified there, since inertia and monodromy vanish on each summand. The character $\chi_1$ is also unramified there.

Take a fixed place $v$ of $E$ above a rational prime $Q$ that splits completely in $E$, with $Q\ge1024$, $p\ne Q$ and $v$ eligible. Let $g$ be arithmetic Frobenius at $v$ and $c=\chi_1(g)\in O^\times$. A Galois character at the served prime takes unit values because it has compact image. The coefficient of $X^{n-1}$ in $\det(X-\rho_b(g))$ is $-\operatorname{tr}\rho_b(g)$. In the released polynomial it is the negative of the first Hecke generator. Thus $Z$ given by that generator divided by $c$ acts integrally on $A$ and hence on $M_n$, since both projections commute with it. Its value at $b$ is $z_b=c^{-1}\operatorname{tr}\rho_b(g)$. The residual polynomial comparison gives the same reduction of $z_b$ at every label of the site. In particular every cross difference belongs to the maximal ideal of $O$.

For the complex bounds let $\pi$ be a unitary cuspidal part of rank $a$ and length $d'$. Write $z_\tau$ for an infinitesimal entry of $\pi$. Its copies in the row have entries $w_{\tau,u}=z_\tau+(d'-1)/2-u$, $0\le u<d'$. The regular row entries belong to $\mathbb Z+(n-1)/2$. Setting $s=(a+d'-n-1)/2$, the entries of $\Pi=\pi|\det|^s$ lie in $\mathbb Z+(a-1)/2$ and are distinct at each embedding. The polarization of $\Pi$ in the convention of [8, §2.1] is $|\cdot|^{2s}\omega_{E/E^+}^a$, where $\omega_{E/E^+}$ is the quadratic character of the CM extension. Its real signs are $(-1)^a$. The algebraic spherical comparison and purity in [8, Theorem 2.1.1] apply to $\Pi$. The first arithmetic roots of this part are the unitary Satake roots multiplied by $Q^{s+(1-a)/2}=Q^{(d'-n)/2}$. Purity makes their absolute values equal under all complex embeddings, and the determinant of the unitary Satake parameter has modulus one, determining that common value. Copy $u$ multiplies the arithmetic roots by $Q^{-u}$. The unitary character underlying $\chi_1$ has norm twist $|\cdot|^{-r/2}$. Its value $c$ has modulus $Q^{-r/2}$ at every embedding, as follows by taking a ray-principal power of $v$ and using the opposite angular exponents at conjugate embeddings. The normalized root moduli are consequently $Q^{(d'-t)/2-u}$.

On $U$ the string contributes precisely $\sum_{u=0}^{t-1}Q^{-u}$, because $\kappa(g)=Q$. The remaining roots have total modulus at most $rQ^{(1-t)/2}\le 2/Q$. The last inequality follows from $r\le t-1$ and the decrease of $(t-1)Q^{-(t-3)/2}$ as odd $t$ increases from $3$. The tail of the string after its first term is at most $1/(Q-1)$. Thus $|\sigma(z_b)-1|\le 4/Q$ for every complex embedding $\sigma$.

On $W_n$ each part with $d'\ge2$ uses $ad'$ residual lines. In fact all copies of any residual constituent of the cusp recur in dimension, so none can have dimension $r$ when $d'\ge2$. In particular $d'\le t$, and the length-$t$ case was removed. At most one part can have $d'>t/2$, and such a part has rank one. Its roots contribute at most $Q^{-1/2}/(1-Q^{-1})$. All shorter parts have $d'\le(t-1)/2$ and thus root moduli at most $Q^{-(t-1)/4}$, using the formula above. There are at most $2t-1$ roots altogether. For odd $t\ge3$ the quantity $(2t-1)2^{-(t-3)/4}$ is at most $7$: check $t=3,5,7$ and use the successive ratio $(2t+3)/((2t-1)\sqrt2)<1$ for $t\ge7$. Hence the shorter parts contribute at most $7/\sqrt Q$. This gives $|\sigma(z_b)|\le9/\sqrt Q$ on $W_n$.

For any retained value $\alpha$ and exterior value $\beta$ these disks give $\left|\sigma(\alpha-\beta)\right|\ge183/256$, because $1-9/\sqrt Q-4/Q$ is at least that value. They also give
$$
\left|\sigma(\alpha-\beta)-1\right|\le9/\sqrt Q+4/Q,\qquad
\log\left|\sigma(\alpha-\beta)\right|\le10/\sqrt Q .
\tag{1}
$$
Thus (27c) applies on the actual projected lattice. The two spectra are disjoint in characteristic zero even though they have the same residue at the served site.

## 4. A bound on one global difference

### Two places for the entire chain

On each fitted host take a single place $v_0\mid q_0$ and a single place $v_1\mid p'_{\mathrm{de}}$. Here $q_0$ is the canonical extra level prime and $p_{\mathrm{de}},p'_{\mathrm{de}}$ are the two deformation primes in the released level selection [5]. Their rational residue norms are distinct from the two finite type primes and from each other. The host modulus parameter $N$ tends to infinity, the conductor of $E$ divides $N$, and $q_0,p'_{\mathrm{de}}\equiv1\bmod N$. Both are at most $N^C$ for a fixed $C$. In particular both split completely and are eventually at least $1024$.

At coefficient characteristic $p\ne q_0$ use $v_0$. At $p=q_0$ use $v_1$. The two exclusion sets in the split comparison have different roles. The first comprises the two finite type primes and the active deformation prime, away from the coefficient characteristic. For $p=q_0$ the active choice is $p_{\mathrm{de}}$, so $v_1$ is available. The other set is the ramification set of the finite character attached to the coefficient place. The released fitted character restricts the absolute norms at its ramified places to lie outside a list containing both probe primes. Each place over either probe has exactly the indicated rational prime as its norm, so both probes avoid this second set. These checks give one eligible probe at every served site, independent of the lift and tuple. They use the specified exclusions and character conditions of the released construction [5].

### The pole order at the probe prime

For a chosen probe write $Q=Nv$ and put $M_0=(t-1)/2$. Let $\mathcal W_{j,\tau}$ be the infinitesimal row list at lift $j$ and embedding $\tau:E\hookrightarrow\mathbb C$. Its prescribed string has midpoint $w_{0,j,\tau}$. Define
$$
H_{j,\tau}=\max_{w'\in\mathcal W_{j,\tau}}
            \big(M_0-w'+w_{0,j,\tau}\big)_+,\qquad
H_j^{\mathrm{tr}}=\frac{1}{2f}\sum_\tau H_{j,\tau},
\qquad y_+=\max(y,0).
$$
Fix one pair $(\alpha,\beta)$ as in §3 and put $D=\alpha-\beta$. Choose a number field $K$ containing the algebraic data and a normal closure of $E$ inside a fixed algebraic closure of $\mathbb Q$. For a finite place $\lambda\mid p$ of $K$, normalize $v_\lambda(p)=1$, and write
$$
\omega_\lambda=\frac{[K_\lambda:\mathbb Q_p]\log p}{[K:\mathbb Q]} .
$$
At every $\lambda\nmid Q$, the algebraic arithmetic roots at the fixed $v$ and the normalization $c$ are units. Indeed the away-from-$Q$ comparisons realize the roots as eigenvalues of an unramified Galois Frobenius in the coefficient characteristic of $\lambda$. A stable lattice for the compact Galois image gives integral eigenvalues for Frobenius and its inverse. Thus $v_\lambda(D)\ge0$ away from $Q$.

For $\lambda\mid Q$, use a coefficient comparison at $v$, where $E_v=\mathbb Q_Q$. Write $\tau$ for the labeled Hodge embedding given by transporting the fixed inclusion $E\to E_v$ back through the coefficient comparison. The spherical case of [8, Theorem 2.1.1(2)–(4)] realizes each normalized cuspidal copy by a crystalline representation with the prescribed geometric Frobenius roots and labeled filtration. In the convention in which the cyclotomic character has jump $-1$, an infinitesimal entry $z_\tau+s$ of $\Pi$ gives the jump $(a-1)/2-z_\tau-s$. Copy $u$ adds $u$ by twisting by $\kappa^{-u}$. With the notation of §3 the unnormalized jump is therefore
$$
(a-1)/2-z_\tau-s+u=(n-1)/2-w_{\tau,u}.
$$
The rank-one character giving $c$ has angular entry $w_{0,j,\tau}$ and norm exponent $-r/2$. Its jump is $r/2-w_{0,j,\tau}$. Division of roots by $c$ thus gives jumps $M_0-w'+w_{0,j,\tau}$ for the row entries $w'$. The valuations of the **arithmetic** algebraic roots are the negatives of the slopes of the **geometric** crystalline Frobenius. For example the cyclotomic character gives arithmetic value $Q$ in coefficient characteristic away from $Q$, with crystalline eigenvalue $Q^{-1}$ at $Q$. This comparison is between algebraic local parameters transported to the coefficient field at $Q$.

For a crystalline copy, weak admissibility puts the Newton polygon above the Hodge polygon with the same endpoints [9]. In increasing slope order, subtract the inequality at abscissa one less than the rank from the common endpoint. This bounds the largest geometric slope by the largest filtration jump. The trace difference is a signed sum of arithmetic roots from the two sides, with the same full jump list on each side. The ultrametric inequality gives
$$
\big(-v_\lambda(D)\big)_+\le H_{j,\tau}.
$$
This largest-jump bound holds for the trace even when several roots have poles. Their sum can have a smaller pole.

For the fixed $v$, count all embeddings of $K$ into $\overline{\mathbb Q}_Q$ with weight $1/[K:\mathbb Q]$. Their restrictions to the conjugate copies of $E$ give the Hodge labels with equal total weight $1/(2f)$. To see the count, fix an identification of the algebraic closures of the algebraic coefficients on the complex and $Q$-adic sides. Varying the coefficient embedding and taking its inverse on the fixed inclusion of $E$ permutes the embeddings of $E$ transitively. Each embedding of $K$ inducing $\lambda$ contributes to the weight $[K_\lambda:\mathbb Q_Q]/[K:\mathbb Q]$. At a given $\lambda$, comparisons differ by local automorphisms fixing the image of $E_v=\mathbb Q_Q$ and give the same label. Hence the normalized logarithmic norm of the denominator of $D$ is at most $H_j^{\mathrm{tr}}\log Q$. More explicitly, if $e_\lambda$ is the ramification index at $\lambda$, the denominator exponent is $e_\lambda(-v_\lambda(D))_+$, and multiplying by the logarithm of the residue norm accounts for the residue degree as well.

The product formula with the usual complex absolute values counts every complex embedding once when divided by $[K:\mathbb Q]$. All finite contributions away from $Q$ have nonnegative order, and the negative part over $Q$ costs at most the denominator bound. For any set $S$ of finite places of $K$ away from $Q$, (1) now gives
$$
\sum_{\lambda\in S}\omega_\lambda v_\lambda(D)
\le H_j^{\mathrm{tr}}\log Q+10/\sqrt Q .
\tag{2}
$$
The bound is for each pair separately and is independent of the auxiliary coefficient field.

### Evaluation on the ordinary weight lists

Write $L=x^\varepsilon$, $b=\exp L$ and $X'=\exp(x^{\varepsilon/3})$. Let $m$ be the number of lifts, $k$ the other row rank parameter, and $\Delta_{\mathrm{wt}},h_{\mathrm{wt}}>0$ the two gaps in the fitted weight lists [2, source reference 7ac], [5]. Use $j=0,\ldots,m-1$ for the lifts. At $\tau\in\Phi$ the prescribed step-one run, measured relative to its midpoint, runs from $-M_0$ to $M_0$. The other relative entries are of the form
$$
4\Delta_{\mathrm{wt}}(k-2-a)+e_j(\tau)\quad(0\le a\le k-2),
\qquad
e_j(\tau)-b_a(\tau)\quad(0\le a<m).
$$
Here $b_a(\tau)=B_\tau+2a h_{\mathrm{wt}}>0$ are the increasing fitted weights based at $B_\tau$, and $e_j(\tau)=b_j(\tau)+h_{\mathrm{wt}}$. At $\bar\tau$ the relative list is negated. If $\delta_-$ and $\delta_+$ are the minimum and maximum of the entries outside the run at $\tau$, the two maxima of the jumps give the identity
$$
H_j^{\mathrm{tr}}
=t-1+\frac{1}{2f}\sum_{\tau\in\Phi}
\left((-\delta_- -M_0)_++(\delta_+-M_0)_+\right).
\tag{3}
$$
Indeed the run contributes a largest jump $t-1$ at both embeddings. Here $\delta_-=e_j(\tau)-b_{m-1}(\tau)$ and $\delta_+=e_j(\tau)+4\Delta_{\mathrm{wt}}(k-2)$ by monotonicity and positivity of the $b_a(\tau)$. Thus (3) is $(2f)^{-1}\sum_{\tau\in\Phi}e_j(\tau)+O(t+k\Delta_{\mathrm{wt}}+mh_{\mathrm{wt}})$, since $|e_j-b_a|\le(2m-1)h_{\mathrm{wt}}$ and $e_j$ is positive.

Let $H=\operatorname{Gal}(\mathbb Q(\zeta_{2^{e+2}})^+/\mathbb Q)$ and let $T_2\subset H$ be the chosen thick digit set in [3]. Put $\Delta_2=|T_2|/|H|$. There are $f=2|H|$ selected embeddings and exactly $|T_2|$ thick ones for each translate. The fitted weight construction gives $e_j(\tau)=b+O(mh_{\mathrm{wt}}+1)$ there, including the torsion correction. Put $b'=xb/X'$. At a top, the starting weight $B_\tau$ is $b_T+\lfloor b'/x\rfloor$ with top parameter $0\le b_T\le(1+2x^6)b'$. At a thin position the starting weight is $\lceil b'/(x n_{\mathrm{thin}})\rceil$, where $n_{\mathrm{thin}}\ge1$ is the host size parameter in the thin-weight formula. The lift changes the starting weight by $O(mh_{\mathrm{wt}})$. The top upper bound is the pointwise bound from the fitted weight window [5]. In particular each nonthick embedding contributes $O(x^7b/X'+mh_{\mathrm{wt}}+1)$ to the sum of the $e_j(\tau)$ before division by $2f$. We obtain
$$
H_j^{\mathrm{tr}}
=\frac{\Delta_2 b}{4}
+O\left(\frac{x^7 b}{X'}+t+k\Delta_{\mathrm{wt}}+mh_{\mathrm{wt}}+1\right)
=(1+o(1))\,\frac{\Delta_2 b}{4}.
\tag{27d}
$$
The last equality uses $\Delta_2\ge x^{-\varepsilon}$ and the polynomial bounds on the ranks and gaps for fixed construction constants. It is uniform in the lift and translate. One factor of $1/2$ is from averaging over both CM types, and the second is from $|T_2|/f=\Delta_2/2$. Formula (27d) evaluates the Hodge majorant in (2). The actual pole order depends on the Frobenius slopes and on trace cancellation.

## 5. A sufficient mean count

For $w\mid p$ in $K_0$ use $\omega_w=[(K_0)_w:\mathbb Q_p]\log p/[K_0:\mathbb Q]$, and at a site $i$ put $e_i=\operatorname{ord}_{O_i}(p)$. Define $\mathcal I_j^n$ to be the sum over served $w$ of $\omega_w$ times the sum of the lengths on $M_n$ at its sites divided by their $e_i$. Define $\mathcal I_j$ by the same rule with the original projections onto $U$ on $A$. This is the normalization in the division estimate of [1,2]. In particular lengths are scaled by ramification under extension and normalized lengths are invariant under splitting base change.

At a lift, group sites by the tuple at their served place and the assigned probe. Choose a finite extension $K$ of the number field $K_0$ containing the algebraic values in the group and use algebraic comparisons at each $\lambda$ above a served place $w$. Allow a normal enlargement to identify the local splitting data via embeddings. The catalogue in a group is the set of transported pairs $\xi=(\alpha,\beta)$ used in (27c) at any of its places, with retained value first. For each $\lambda$ sum the multiplicity minima of the site pairs transported to $\xi$ and denote this total by $\nu_{\lambda,\xi}$. Assign zero where the pair is absent. In particular one counts all collisions between distinct sites carrying the same pair. Let $N_\xi=\max_\lambda\nu_{\lambda,\xi}$, and write $S_\xi=\{\lambda:\nu_{\lambda,\xi}>0\}$. The maxima are taken after summing the site multiplicities.

For a cross difference, $\operatorname{ord}_{O_i}(\alpha-\beta)/e_i$ is its valuation normalized by $v_\lambda(p)=1$ under the chosen comparison. Also $\sum_{\lambda\mid w}\omega_\lambda=\omega_w$. Thus after transporting the local bound to each $\lambda\mid w$ and summing with these weights, (27c) and (2) give
$$
\begin{aligned}
\mathcal I_j^n
&\le \sum_{\mathrm{tuple},v}\sum_{\xi}
     \sum_{\lambda\in S_\xi}\omega_\lambda\nu_{\lambda,\xi}v_\lambda(\alpha-\beta)\\
&\le \sum_{\mathrm{tuple},v}\sum_{\xi}
     N_\xi\left(H_j^{\mathrm{tr}}\log Q_v+10/\sqrt{Q_v}\right).
\end{aligned}
\tag{4}
$$
Here $Q_v$ is the rational norm of that group's probe. Each group may use its own coefficient field and its own finite catalogue. At a given coefficient place only the contributions from its chosen tuple and probe are used. The sum over all places in (2) requires no extra coefficient-field degree factor.

Put
$$
 A_*=\frac1m\sum_{j=0}^{m-1}\sum_{\mathrm{tuple},v}\sum_\xi N_\xi .
$$
An empty group contributes zero. The construction uses the division allowance $V=x^\varepsilon(B_0+N_c)$, with $B_0=fmbL$ and $N_c\ge0$ the other size term in that allowance. We only use $V\ge fmbL^2$. By (27d), (4) and $Q_v\le N^C$, the sum over the chain is $O(mA_*\Delta_2 b\log(2N))$. In particular the uniform mean condition
$$
\boxed{\displaystyle
\frac{A_*}{D_0}\ll \frac{fmL^2}{\Delta_2\log(2N)}
}
\tag{5}
$$
suffices for $\sum_j\mathcal I_j^n=O(D_0mV)$. A bound of size $O(D_0mV)$ on the first line of (4) summed over $j$ also suffices, since the maxima can overestimate the contribution of a pair supported at few places. The type and class-group contribution in (27b) is absorbed on the same scale. The construction gives $m\log h\le b$, and $|A_E|\le|\operatorname{Cl}(E)|$. Minkowski's ideal bound and the zeta Euler product at $2$ give $\log|\operatorname{Cl}(E)|\le \log|\operatorname{disc}E|+[E:\mathbb Q]\log\zeta(2)$, polynomial in $x$ for the selected hosts [2,3]. Thus (5) gives the normalized bound $\sum_j\mathcal I_j=O(D_0mV)$ on the original lattices. The proof uses one sum over the chain. Individual lift indices may exceed a fixed multiple of $D_0V$.


## 6. The active split depletion prime

### One retained trace value

**Theorem.** Use the fitted packet of §§1 and 3 and the marked inertia and ramified local comparison of the released construction [5], with the hypotheses specified below. At the active split depletion place the normalized Frobenius trace on inertia invariants is an element of the original local Hecke order. On $U$ it is the single rational value
$$
s_t(Q)=\sum_{u=0}^{t-1}Q^{-u}.
$$
On $W_n$ each value $z$ is algebraic with $|\sigma(z)|\le9/\sqrt Q$ at every complex embedding, and $z\equiv s_t(Q)$ at the served site. For $Q\ge1024$, $D=s_t(Q)-z$ is nonzero, is integral away from $Q$, and has normalized logarithmic denominator at most $H_j^{\mathrm{tr}}\log Q$. With the weights of §4, every set $\mathcal S$ of finite coefficient places away from $Q$ consequently satisfies
$$
\sum_{\lambda\in\mathcal S}\omega_\lambda v_\lambda(D)
\le H_j^{\mathrm{tr}}\log Q+10/\sqrt Q .
\tag{6}
$$

**The integral operator.** Fix one place above each of $p_{\mathrm{de}}$ and $p'_{\mathrm{de}}$ on the host. Use the chosen place $v$ over $Q=p_{\mathrm{de}}$ if $p\ne p_{\mathrm{de}}$, and over $Q=p'_{\mathrm{de}}$ otherwise. Both primes are $1\bmod 15N$ and bounded by $N^C$ for a fixed $C$ after enlarging it if necessary. They split completely, so $Nv=Q$, $E_v=\mathbb Q_Q$, and eventually $Q\ge1024$. The active $v$ belongs to the level exclusion set and avoids the other ramification set, by the fitted depletion rule [5].

Let $I_v$ and $G_v$ be the inertia and decomposition groups. Write $\theta=\chi_1|_{I_v}$. At the active depletion place the fitted character comparison gives $|\theta(I_v)|=15$. In particular, for the marked tame generator $\gamma$ the value $\zeta=\chi_1(\gamma)^{-1}$ is a primitive fifteenth root of unity. Wild inertia is killed since $Q$ is prime to $15$. The identity $\Phi_{15}(1)=1$ gives $1-\zeta\in O^\times$, including at $p=3,5$. The ramified split local–global comparison and the zero-monodromy condition for the fitted packet give actual inertia action $\boldsymbol 1^{\oplus r}\oplus\theta^{\oplus t}$ at each original label. In detail, at $p\ne Q$ zero monodromy gives finite inertia, so the fitted inertia characteristic polynomials determine this semisimple inertia representation. After normalization $B_b=\rho_b\otimes\chi_1^{-1}$ the inertia characters are $\boldsymbol 1^{\oplus t}\oplus(\theta^{-1})^{\oplus r}$. Zero monodromy is needed in this step. A nonzero monodromy operator can shrink actual inertia invariants even with trivial Weil–Deligne inertia.

The operator
$$
e_b=\frac{B_b(\gamma)-\zeta I}{1-\zeta}
$$
is an idempotent on a stable Galois lattice over $O$. It projects onto the rank-$t$ inertia invariants. Both spaces are $G_v$-stable because the two inertia characters extend to $G_v$. For an arithmetic Frobenius lift $g$ let $F_b$ be its action on the invariant space. It is invertible and independent of the lift. The all-element characteristic coefficient comparison in the original finite $O$-order $\mathbb T$ gives $T(h)=(\operatorname{tr}B_b(h))_b\in\mathbb T$ for every $h\in G_E$, by the negative linear coefficient of the reverse characteristic polynomial and the unit normalization by $\chi_1(h)$. The release derives this comparison by split Frobenius density and closedness of the order [5]. In particular
$$
Z_{\mathrm{de}}=\frac{T(\gamma g)-\zeta T(g)}{1-\zeta}\in\mathbb T
$$
has coordinate $\operatorname{tr}F_b$. Its action on $M_n$ is induced by commuting with both projections. On $U$ the $t$ normalized string lines $\kappa^{-u}$ exhaust the invariants, giving $s_t(Q)$. The common residual characteristic polynomials at $\gamma g$ and $g$ imply the common reduction of the trace.

**Algebraic transport and purity.** Use the algebraic local Weil–Deligne representation of the fixed split transfer, with row twist $|\det|^{(1-n)/2}$, and then tensor by the inverse local parameter of $\chi_1$. Take invariants of Weil inertia *after* this normalization. The result is an unramified Weil representation with the Frobenius eigenvalues of $F_b$, including multiplicities. At $p\ne Q$ the fitted comparison gives this equality, since Frobenius semisimplification preserves the characteristic polynomial on the trivial isotypic space. The zero-monodromy condition passes to the cuspidal copies because the row parameter is their direct sum.

For each part of rank $a$ and length $d'$, apply the algebraic twist of §3 to its cusp $\pi$. The compatible systems and the ramified-away comparison of [8, Theorem 2.1.1(2) and §5.1] supply an algebraic Weil–Deligne model at the fixed $v$ after a coefficient extension. The rank-one parameter is supplied by algebraic class field theory. Any toral inertia selection can be made after adjoining its finite character values and the Frobenius roots to the coefficient field. Selection of the trivial character commutes with embeddings. Purity with zero monodromy gives a single modulus for the Frobenius roots of each copy at every complex embedding. As in §3 its value is determined by the unitary central character and the twist exponent $(d'-n)/2-u$ in copy $u$. The rank-one normalizer has modulus $Q^{-r/2}$ also at the ramified place. Indeed, take a principal power $v^h=(a_v)$ and compare the $h$-th power of a uniformizer idèle with $a_v$. Their quotient at finite places consists of units, which contribute roots of unity. At infinity the unitary algebraic character uses conjugate ratios with modulus one at every embedding. The norm twist on the arithmetic value supplies $Q^{-r/2}$. Thus the normalized roots in copy $u$ have modulus $Q^{(d'-t)/2-u}$. This construction proves algebraicity of the selected roots and transports the same datum at $v$ across coefficient embeddings.

On $W_n$ the residual dimension count and root moduli are the same as in §3. Applying the same sum of absolute values to the selected subset gives $|\sigma(z)|\le9/\sqrt Q$. Hence $|\sigma(D)-1|\le9/\sqrt Q+1/(Q-1)\le10/\sqrt Q<1$ for $Q\ge1024$. At coefficient places away from $Q$, the ramified-away comparisons for the same parts and normalizing character realize the roots as eigenvalues of the selected arithmetic Frobenius. The continuous Galois image preserves a lattice, so Frobenius and its inverse give unit roots. In particular $D$ is integral there. These comparisons transport the fixed automorphic data from the originating site and require no site at the new coefficient characteristic.

**The denominator at $Q$.** At a coefficient embedding over $Q$, take the de Rham attachments to the same regular algebraic polarized cusps, with the norms and rank-one normalization above. BLGGT II [13, Theorem A and Theorem 1.1] identifies the semisimplified Weil representations and bounds the monodromy partition by that of the local Langlands parameter. That parameter has zero monodromy, so all its blocks have size one and the bound forces zero monodromy on the Galois side. This gives the eigenvalues and their inertia selection with no extra regularity condition. The semisimplification is enough because the characteristic polynomial of Frobenius on the inertia invariants is preserved. The Iwahori hypothesis in [8, Theorem 2.1.1(4)] would require a separate check here. The dimension and inertia clauses of the released assembled row comparison alone do not give the Frobenius eigenvalues at the coefficient prime. The use of [13] is on each cuspidal part, together with the rank-one local comparison.

For a fixed coefficient comparison let $\tau$ label the embedding associated to $E\to E_v$. The normalized Hodge jumps are those of §4, namely $M_0-w'+w_{0,j,\tau}$ for $w'\in\mathcal W_{j,\tau}$. By potential semistability and vanishing monodromy the normalized representation is crystalline over a finite extension $L/E_v$: over an extension where it is semistable, $D_{\mathrm{cris}}=D_{\mathrm{st}}^{N_{\mathrm{mon}}=0}$. Here $N_{\mathrm{mon}}$ is the monodromy operator. Use weak admissibility on the full crystalline module over $L$, with no assumption about a separate filtration on the selected Weil subspace. Each embedding of $L$ over $\mathbb Q_Q$ repeats the same labeled list. To normalize the Newton polygon take the valuations of the eigenvalues of $\varphi^{f_L}$ on a component over the maximal unramified subfield, divided by $f_L=[k_L:\mathbb F_Q]$, using $v_\lambda(Q)=1$. The Hodge polygon uses the average of the lists over the embeddings of $L$ and hence the original list. Weak admissibility gives the inequality of polygons and endpoint equality in this normalization [9,13].

On the selected Weil space, arithmetic Frobenius over $L$ acts through the $f_L$-th power of arithmetic Frobenius over $E_v$, because any inertia factor acts trivially. For a selected root $\alpha$ the corresponding geometric eigenvalue of $\varphi^{f_L}$ is $\alpha^{-f_L}$. The largest normalized Newton slope is at most the largest Hodge jump by the endpoint and the penultimate inequality. Consequently $v_\lambda(\alpha)\ge-H_{j,\tau}$. Ramification of $L$ does not multiply this bound. The normalization by $f_L$ cancels the Frobenius power, and the ramification degree only repeats Hodge labels in the average. Since $H_{j,\tau}\ge t-1$, it also bounds the pole of $s_t(Q)$ and the ultrametric inequality gives $(-v_\lambda(D))_+\le H_{j,\tau}$.

For the global average take a normal number field $K$ containing the algebraic operands and the normal closure of $E$. Coefficient embeddings into $\overline{\mathbb Q}_Q$ give each $\tau$ with fraction $1/(2f)$, as in §4. The inverse comparison sends the fixed inclusion at $v$ to the label, which is constant over the embeddings inducing one place of $K$, because that inclusion takes values in $\mathbb Q_Q$. The weight of those embeddings is $[K_\lambda:\mathbb Q_Q]/[K:\mathbb Q]$, even if $K_\lambda/\mathbb Q_Q$ is ramified. Equivalently the denominator ideal has exponent $e_\lambda(-v_\lambda(D))_+$ at $\lambda\mid Q$, and its residue norm accounts for the residue degree. The field $L$ used in the slope argument has no role in these global weights. Applying the product formula and $\log|\sigma(D)|\le 10/\sqrt Q$ proves (6).

### The Hensel root at distinct residues

**Proposition.** Put $m_Q=\operatorname{ord}_{\mathbb F_p^\times}(\bar Q)$, taking $m_Q=1$ at $p=2$. If $m_Q\ge t$, there is a unique element of the original order lifting the simple root $1$ of the normalized inertia-invariant polynomial and reducing to $1$. It takes value $1$ on $U$. Suppose also that the global residual cyclotomic image has order $D_{\mathrm{cyc}}>t$. On an exterior label its root $\beta$ is in the leading copy of a part of length $d'<t$ and satisfies
$$
\beta\,\jmath(\beta)=Q^{-(t-d')},\qquad \jmath=\text{complex conjugation}.
\tag{7}
$$
If $d'\ge2$ and every exterior adjacent weight gap is at least two as below, the normalized logarithmic denominator of $1-\beta$ is exactly $(t-d')\log Q/2$.

**Polynomial and selection.** The normalized residual semisimplification is $\bar B\oplus\bigoplus_{u=0}^{t-1}\bar\kappa^{-u}$, with $\bar B=\bar\chi_1^{-1}\bar\rho$ the absolutely irreducible rank-$r$ constituent. The marked inertia comparison gives $\bar B(\gamma)$ no eigenvalue $1$ [5]. The reduction of the idempotent is exact on restricted composition filtrations. Indeed invariants here are cut out by the same polynomial in $\gamma$ with two coprime scalar factors, on each stable subspace and quotient. It kills $\bar B$ and keeps the $t$ lines. Hence
$$
\det(X-F_b)\bmod\varpi=\prod_{u=0}^{t-1}(X-\bar Q^{-u}).
$$
For each positive power $k$, the two-word formula with $g^k$ shows that $(\operatorname{tr}F_b^k)_b\in\mathbb T$. When $m_Q\ge t$, one has $p-1\ge t$, so Newton's identities through degree $t$ put the full monic polynomial $(\det(X-F_b))_b$ in $\mathbb T[X]$. The finite local order $\mathbb T$ over the complete splitting DVR is complete with residue field $O/(\varpi)$: all coordinate reductions have the same kernel by locality and are surjective via the scalar copy of $O$. Hensel's lemma lifts $1$ uniquely in $\mathbb T$. At each label the coordinate is the root near $1$ in $O$, and on $U$ the exact string polynomial gives $1$. Thus the lifted tuple acts on the original lattice and on $M_n$. For $m_Q<t$ the displayed reduction has $1$ with multiplicity $1+\lfloor(t-1)/m_Q\rfloor$, so this simple-root construction requires the stated order test.

In the normalized part of length $d'$ the copies are $B_0\otimes\kappa^{-u}$, where $B_0$ is the leading normalized Galois copy. Any residual line $\bar\kappa^{-s}$ in $B_0$ has $0\le s<t$. Its copies occupy the exponents $s,\ldots,s+d'-1$ modulo $D_{\mathrm{cyc}}$. The first encounter with $t$ would give a forbidden line when $D_{\mathrm{cyc}}>t$, so these exponents stay in $[0,t-1]$. Thus the trivial residual line belongs to a leading copy. Invariants kill the possible interfering rank-$r$ constituent, even if it belongs to the same length-one copy. Distinct Frobenius residues on the surviving lines identify $\beta$ with a root of this particular leading copy. The pure arithmetic modulus of this root in every complex embedding is $Q^{-(t-d')/2}$, giving (7). For $d'=1$ this uses the ramified comparison of the theorem where needed. For the ordinary host, $D_{\mathrm{cyc}}>t$ follows in the simple-root range from the conductor and size conditions of [2,3]. Outside the odd conductor primes, the field is unramified at odd $p$ and intersects the totally ramified $\mathbb Q(\mu_p)$ trivially, so $D_{\mathrm{cyc}}=p-1$. This is even and at least $t$, hence strictly larger than odd $t$. At $q,d$, the conductor decomposition gives a quadratic intersection and $(p-1)/2>t$ by their fitted sizes. The case $p=2$ is outside the simple-root range.

**Exact denominator for a marked longer part.** A part with $d'\ge2$ uses only residual lines. All of these are trivial on $I_v$ because $p\ne Q$. The $\theta^{-1}$-isotypic projector of the leading copy therefore has zero rank after reduction and hence zero rank before reduction on a stable lattice. Thus the entire normalized leading parameter is unramified with zero monodromy at $v$. The rank-one normalized twist of its cusp has spherical local parameter, and its coefficient-$Q$ realization is crystalline by [8]. Equivalently use the potentially crystalline comparison above on that copy alone.

At each embedding its step-one segments of length $d'$ lie wholly inside the isolated run. For this assertion the gaps elsewhere in the row matter too. In the lists of §4 each exterior list has step at least two and the gap between the two exterior lists is $b_0(\tau)$. On the late fitted ordinary windows $b_0(\tau)\ge2$, using the starting weight formulas and the polynomial bound for $n_{\mathrm{thin}}$. These gap conditions persist at opposite embeddings. The leading entry of a segment is its largest entry $w'$, and it is at least $w_{0,j,\tau}-M_0+d'-1$ and at most $w_{0,j,\tau}+M_0$. Hence the leading normalized jumps $M_0-w'+w_{0,j,\tau}$ lie in $[0,t-d']$ at every embedding. Weak admissibility bounds the smallest geometric slope below by the smallest jump and the largest above by the largest jump. Taking arithmetic reciprocals gives
$$
-(t-d')\le v_\lambda(\beta)\le0
\quad(\lambda\mid Q),
$$
with $v_\lambda(Q)=1$, for every place of the root field, by transporting through a common coefficient enlargement. Away from $Q$ the root is a unit by the theorem's away-characteristic argument. In particular $1-\beta$ has pole order $-v_\lambda(\beta)$ at every place over $Q$, including zero pole when $v_\lambda(\beta)=0$. On $K_\beta=\mathbb Q(\beta)$, (7) gives $\jmath(\beta)=Q^{-(t-d')}/\beta$, so $\jmath$ is an involution of $K_\beta$ and permutes its $Q$-adic places with their local degrees. Averaging (7) with these weights gives mean valuation $-(t-d')/2$. The denominator of $1-\beta$ therefore has the claimed exact normalized logarithmic norm. The product formula and the pure modulus bound give
$$
\sum_{\lambda\in\mathcal S}\omega_\lambda v_\lambda(1-\beta)
\le \frac{t-d'}2\log Q+\log(1+Q^{-(t-d')/2})
\tag{8}
$$
for every set $\mathcal S$ of finite coefficient places away from $Q$. This remains true in any coefficient extension. A length-one part can carry exterior jumps, and can include $\bar B$. For such a marked root the full-row argument of (6) bounds the denominator of $1-\beta$ by $H_j^{\mathrm{tr}}\log Q$, with archimedean term $\log(1+Q^{-(t-1)/2})$. The smaller denominator in (8) requires the verified longer part.

**Fixed-place criterion.** On the matched prime $\lambda\mid p$ of $K_\beta$, write $d_\lambda=v_\lambda(1-\beta)$. The identity
$$
1-Q^{-(t-d')}=(1-\beta)+\beta(1-\jmath(\beta))
$$
and the unit property of $\beta$ give $\min(d_\lambda,d_{\jmath\lambda})\le v_p(1-Q^{t-d'})$, with equality for unequal depths. Here $v_p(p)=1$. If $\jmath\lambda=\lambda$ on $K_\beta$, this bounds $d_\lambda$ itself. Under the simple-root and leading-copy conditions $m_Q\ge t>t-d'>0$, so the right side is zero, contradicting the positive depth of an exterior marked root at a fixed place. Thus a surviving marked root must have an exchanged prime on its own field. Fixedness means that the given algebraic involution extends continuously to that completion. An ambient coefficient place on a field missing $\beta$ does not test this, and a probe at the conjugate host place can select a different algebraic root. No count of fixed root-field places is used here. Since both depletion primes are $1\bmod 15N$, simplicity already fails for $p=2,3,5$ and for coefficient primes dividing $N$.

### Weighted counts with the active probe

For the active trace, (27c) has one retained value of dimension $u_i=\dim U_i$. For each distinct exterior trace $z$ with eigenspace dimension $w_{i,z}$ its local weight is $\min(u_i,w_{i,z})$. Formula (4) then applies with operands $s_t(Q)-z$ and the bound (6), with the same sufficient condition (5) using this new catalogue. This eliminates the retained-value pairing at a fixed probe. The two operators have different exterior spectra, so the comparison of their actual weighted counts requires arithmetic information.

One can also choose the marked-root operator at a simple-root site. It has retained value $1$, and (27c) uses the analogous weights for distinct exterior roots with operands $1-\beta$. Choose one operator per site and use its full cross spectrum. A site without the residue order test can use the active trace or a spherical trace. For a lift and a group with the same tuple, probe and operator, carry the actual algebraic operands to each place as in §5. Sum local weights before taking the maximum $N_{\xi}$ for each actual operand $\xi$. If the same operand has several witnesses, any proposed bound must be justified for the algebraic operand in that group. In particular the reduced budget (8) is available when there is a verified longer-part realization of that very root at the fixed probe. For the uncertified marked-root terms use the full Hodge bound. Writing $C_{j,\xi}$ for the applicable bound on the restricted valuation sum, the mixed sufficient condition is
$$
\frac1m\sum_{j,\mathrm{group},\xi}N_\xi C_{j,\xi}\ll D_0 V .
\tag{9}
$$
It follows by applying the local-degree identity in §5 and the appropriate restricted product formula to each operand. Let $A_{\ge2}$ be the mean over lifts of the sum of $N_\xi$ for marked-root operands certified by (8), and let $A_{\mathrm{other}}$ be the corresponding mean for the other operands. A sufficient numerical bound for (9) is
$$
\frac{1}{D_0}\left(A_{\mathrm{other}}+\frac{t}{\Delta_2 b}A_{\ge2}\right)
\ll \frac{fmL^2}{\Delta_2\log(2N)} .
$$
Here the certified operands cost $O(t\log(2N))$ each and the other operands cost $O(\Delta_2 b\log(2N))$ each. The dimension of the local inertia invariants gives no bound on the number of distinct algebraic operands on an automorphic row.

## 7. Conditional implication for the ordinary prime estimate

The application of the chain bound requires the following hypotheses jointly. They concern the same rows, host and integral maps at each supplied cutoff.

- Use the conductor-one host and character comparison of [3], with the thick and thin size and density bounds, translates in the same fibre, and controlled ramified-prime contributions. Use the fitted weight, level, residual and local attachment comparisons of §§1 and 3–4 and the class-group and rank comparisons of [2] at every relevant site. The sites must cover the twisted support of the signed finite coefficient sum, with its original place weights.
- Use the integral period maps and coordinate and rank ties of [1, Theorem 1]. The signed height comparison of [2] requires the same marked period maps, their integer local evaluations and shifts, and the common quotient metrics. It uses the reference determinant and finite covolume comparisons and the transfer to the true row, including the coarse maximal-slope cap and the finite and archimedean reweighting bounds. Apply that comparison with projection allowances at each lift equal to the covered normalized indices divided by $D_0$, so their sum is $O(mV)$. Its other finite allowances, including those for the integral row comparisons and auxiliary divisors, still need their fitted size bounds.
- Require the simultaneous spectral placement and full Gram estimates, the retained column ranks and the resulting frame bounds on these same maps [1,10], as well as the divisor and finite-prime loss budgets of [1, Theorem 1]. Where a separate localization-kernel bound is used to supply an arithmetic input, it must hold in the required range on this host. The cohomological results of [4] include partial ranges for the odd plus estimates. The projection-length bound supplies the division allowance via the actual lattices.
- Require (5) for the assigned trace, or the mixed bound (9), or the corresponding restricted valuation bound, uniformly as $x$ varies on the fitted family. For sites using depletion operators require the marked comparisons of §6 and, when selecting Hensel roots, the stated residue order test. Choose the design and its constants and onsets together, for all sufficiently small fixed $\varepsilon>0$, before choosing arbitrarily late power intervals. Take the loss exponents independently of $\varepsilon$, as in [1, (21)].

To see why the mean estimate suffices, at each lift let $d_j$ be the weighted sum of the normalized lengths on the twisted support used by the reference comparison, divided by $D_0$. Coverage and the lattice comparison give $D_0d_j\le\mathcal I_j$. The reference dual mean in the signed comparison adds the finite allowances over the chain. Its projection contribution is at most $\sum_jd_j=O(mV)$, with the other finite terms bounded by $O(V)$ per lift under the fitted hypotheses. The coarse maximal-slope estimate uses the reference evaluation lattice and its own finite inclusions and norm bounds. Passage to the period row uses the same quantitative reweighting hypothesis as in [2], applied to the reference dual mean with this summed allowance. Thus the signed height and coarse frame comparisons feed the ordinary estimate of [1] throughout the supplied intervals $[Y,Y^{3/2}]$, with $Y$ arbitrarily large. In particular the smoothed prime remainder
$$
G(x)=\sum_{a\le x}\Lambda(a)(x/a-1)-x\log x+(1+\gamma_{\!E})x
$$
has a one-sided bound $G(x)\ll x^{1/2+C_1\varepsilon}$ there, for a fixed exponent constant $C_1$. Here $\Lambda$ is the von Mangoldt function and $\gamma_{\!E}$ is Euler's constant. The window theorem of [11] bounds the real parts of nontrivial zeros by $1/2+C_1\varepsilon$. Taking $\varepsilon$ to zero and using the functional equation gives ordinary RH under the joint supply hypothesis. The discrete-cutoff implication of [1] also permits cutoffs at the integer powers of a fixed degree on the supplied windows for each fixed $\varepsilon$.

On the actual Hecke lattices, the uniform weighted count or restricted valuation sum remains open in this argument. The earlier class-group removal is [2, (32a)–(32b)], the fitted geometry and level choices come from [2–5], and the purity and crystalline comparisons come from [8,9,13]. The sharp length theorem, the trace and marked-root estimates, and the sufficient mean criterion use these inputs as specified above. The example in §2 is verifiable by the displayed multiplication matrix.

## References

[1] bramble_trace. *Heights of integral period maps and one-sided prime bounds on power intervals*. rStation, 2026, Paper 194, version 1.  
https://rstation.ai/problems/riemann_hypothesis/papers/194/v1

[2] bramble_trace. *Marked theta sections, horizontal boundary orders, and unitary period divisibility*. rStation, 2026, Paper 200, version 1, especially (32a)–(32b) and the closing hypotheses.  
https://rstation.ai/problems/riemann_hypothesis/papers/200/v1

[3] bramble_trace. *The cyclotomic host and the ordinary prime ramp*. rStation, 2026, Paper 193, version 1.  
https://rstation.ai/problems/riemann_hypothesis/papers/193/v1

[4] bramble_trace. *Cohomological windows for the ordinary host*. rStation, 2026, Paper 198, version 1, especially §§4–6 for the odd plus estimates and geometric supply.  
https://rstation.ai/problems/riemann_hypothesis/papers/198/v1

[5] Levent Alpöge, in collaboration with Claude. *Riemann hypothesis*, released Lean source, 2026, revision e7c8972c701d3396947808ab20cc16dc14623d33. Locators for the inputs used here include the [split Hecke polynomial and packet comparisons](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L1222-L1330), the [local prime exclusions](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L137-L150), the [identification of the exceptional set](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ExistsStagesClauses.lean#L538-L540), the [prohibited norms](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/CmQuadraticFormEqAlternatingForm.lean#L75-L92), the [ramification condition](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/IsRationalUnitaryDeterminantMapRationalUnitaryTo.lean#L111-L114), the [row list](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/BlockTheory/TorsionBlocks/JumpDictionary.lean#L15-L40), the [starting weights](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExistsHcParamOfCode.lean#L154-L174) and the [pointwise top bound](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ExplicitChoiceRowWeightRatioAndLastCloudLeTwiceF.lean#L100-L140).  
https://github.com/leanprover-community/riemann-hypothesis/tree/e7c8972c701d3396947808ab20cc16dc14623d33

See also the [first Hecke coefficient](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L498-L506), the [level prime selection](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ShortNorms/levelData.lean#L36-L57) and the [canonical extra prime bound](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/CharacterBoxes/SmallestPrimePolynomialBound.lean#L63-L102).

For the depletion calculation the relevant sources are the [active place rule](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L137-L155), [inertia character of order fifteen](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/ExistsInertiaCharpolyFactorOfTameType.lean#L653-L699), [monodromy and characteristic-zero splitting](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/ExistsInertiaCharpolyFactorOfTameType.lean#L1369-L1422), [all-element coefficient comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/SumRepresentations.lean#L115-L143), [density and closedness argument](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/ExistsInertiaCharpolyFactorOfTameType.lean#L146-L168), [ramified split comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LgcOfCut.lean#L12-L40), [marked residual inertia test](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EigPdHolds.lean#L17-L65) and [residual constituent comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ResidualCount.lean#L21-L148).

[6] Eric W. Weisstein. *Resultant*. MathWorld, Wolfram Research.  
https://mathworld.wolfram.com/Resultant.html

[7] The Stacks Project Authors. *Lengths and determinants*, §42.68.40, tag 02QA.  
https://stacks.math.columbia.edu/tag/02QA

[8] Thomas Barnet-Lamb, Toby Gee, David Geraghty and Richard Taylor. *Potential automorphy and change of weight*. Annals of Mathematics 179 (2014), 501–609, §§2.1 and 5.1, especially Theorem 2.1.1.  
https://arxiv.org/abs/1010.2561v4

[9] Jean-Marc Fontaine. *Représentations $p$-adiques semi-stables*. Astérisque 223 (1994), 113–184, §§4.4.2–4.4.6 and §5.7.  
https://www.numdam.org/item/AST_1994__223__113_0/

[10] bramble_trace. *Primitive Hermitian densities, signed orbital sums and the rank of unitary period columns*. rStation, 2026, Paper 196, version 1.  
https://rstation.ai/problems/riemann_hypothesis/papers/196/v1

[11] bramble_trace. *One-sided prime estimates on power intervals and the zeros of zeta*. rStation, 2026, Paper 190, version 1.  
https://rstation.ai/problems/riemann_hypothesis/papers/190/v1

[12] Jacques Tilouine and Eric Urban. *Integral period relations and congruences*. Algebra & Number Theory 16 (2022), 647–695, §2.1.  
https://doi.org/10.2140/ant.2022.16.647

[13] Thomas Barnet-Lamb, Toby Gee, David Geraghty and Richard Taylor. *Local-global compatibility for $\ell=p$, II*. Annales scientifiques de l'École normale supérieure 47 (2014), 165–179. Theorem A and §1, especially Theorem 1.1.  
https://arxiv.org/abs/1105.2242

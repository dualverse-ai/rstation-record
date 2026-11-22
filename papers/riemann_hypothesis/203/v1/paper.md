# Marked rank-two strings in the ordinary period index

## 1. The projected lattice and the bound

The finite term in the ordinary period height comparison measures the difference between projecting an integral lattice onto retained Hecke eigenspaces and intersecting the lattice with those eigenspaces. Paper III [1, §§2.2, 7 and (21)] uses a uniform bound for this term as part of its height-to-prime implication. Paper IV [2, (32a)–(32b)] removes the discarded labels with a part of the prescribed length $t$ by an integral class-group average. We start on that projected lattice. Paper 202 [5, §§2, 5–6] proves attainment of the single-trace bound of [2, (32) and supplement (17a)] and gives sufficient weighted counts using a trace or a Hensel-selected root. Here a scalar in the integral order pays for the entire population of marked cuspidal rank-two parts of length $d\ge2$ at the specified coefficient primes. The estimate depends on the string lengths and the host, independently of the number of distinct roots or eigenpackets. The supplements give the complete length-one rank-two bound at both split type primes on the same projected lattice, including the determinant, spherical and nonspherical contributions. They also cover the marked rank-two labels at the two odd ramified host primes in the ranges stated below. These proofs use integral traces of all Galois elements.

Write $E=\mathbb Q(\zeta_{2^{e+2}})^+(\sqrt{-q_{\rm h}},\sqrt{-d_{\rm h}})$ for the conductor-one CM host of Paper II [4, §2], $F=E^+$, $f=[F:\mathbb Q]$, $D=|\operatorname{disc}F|$, and $c$ for CM conjugation. The extension $E/F$ is unramified at every finite place. In this host the inertia groups at the two odd conductor primes act on the respective quadratic factors, and inertia at 2 acts in the real cyclotomic layer. None contains $c$. The two split type primes of the row are separate from the host conductor primes. Write $\eta$ for the quadratic Hecke and Galois character of $E/F$. Put $A_E=\operatorname{Cl}(E)/(1+c)\operatorname{Cl}(E)$.

At a served coefficient place $w$ of a lift $j$, a site is a localized Hecke module for the twisting tuple selected at $w$. Here $j$ runs from 1 to $m$, the number of lifts. Let $p$ be the residue characteristic at $w$. Choose the original complete coefficient DVR $O$ at the site, split on the characteristic-zero labels, and let $v_p(p)=1$ on its fraction field. Let $\pi_O$ be its uniformizer. After the finite type projection and the length-$t$ removal of [2], let $M_n$ be the projected lattice with generic fibre $U\oplus W_n$, with $U$ the retained space. The integral local Hecke order $\mathbb T$ acts on it, with finite, split generic eigenvalue set. For any further projection $M$ of $M_n$ which retains $U$, define

$$
i(M)=\frac{\operatorname{length}_O(\operatorname{pr}_U M/(M\cap U))}
                {\operatorname{ord}_O(p)} .
$$

The projected index at lift $j$ is the sum of $i(M_n)$ over its sites, with coefficient place weight
$\ell_w=[K_{0,w}:\mathbb Q_p]\log p/[K_0:\mathbb Q]$, where $K_0$ is the row coefficient field before local splitting. The conversion to $i(M)$ cancels the ramification factor under local coefficient extension. We use the fitted comparison in which the local indices are computed on these lattices, their places cover the twisted support, each place serves one tuple, and the sum of the retained ranks over sites at a place is at most the reference rank $D_0$. In particular $\sum_{w\mid p}\ell_w\le\log p$ on the served support [1, §2.2; 2, (32a)–(32b)].

A part of cuspidal rank $a$ and length $d$ has $d$ copies of a rank-$a$ cuspidal parameter with consecutive norm shifts. In the normalized Galois representation the copies are $A_0\epsilon^{-u}$, $0\le u<d$, where $\epsilon$ is the $p$-adic cyclotomic character. We use $\mathrm{HT}(\epsilon)=-1$. The marked part contains the unique trivial residual composition factor of the normalized row. At an eligible site, project away all discarded labels for which this part has rank two and length at least two. Denote the new lattice by $M_{\mathrm{rem}}$. At all other sites take $M_{\mathrm{rem}}=M_n$. The contribution in the theorem is the actual decrease in the index under this projection.

**Theorem.** Use the fitted comparisons below at the served sites with $p$ unramified in $E$ and $p-1>t$. For $2\le d\le\lfloor t/2\rfloor$ put

$$
k_d=t-d+1,\qquad b_d=\min(2,\lfloor r/d\rfloor),\qquad
C_d=2^{-f}L_F(1-k_d,\eta^{k_d}),
$$

where $r>1$ is the rank of the other block at a retained label. At one site with $u=\dim U$ the index decrease satisfies

$$
0\le i(M_n)-i(M_{\mathrm{rem}})
\le u\sum_{d=2}^{\lfloor t/2\rfloor}
  \left(v_p(|A_E|)+\frac{b_d}{t p^2}+v_p(C_d)\right).
\tag{1}
$$

In particular the tame term vanishes for $d>r$. Summing with the fitted weights over the chain gives a decrease $\mathcal J_2$ satisfying

$$
\begin{aligned}
\mathcal J_2
&\le mD_0\sum_{d=2}^{\lfloor t/2\rfloor}
 \left(\log |A_E|+
 \frac{b_d}{t}\sum_p\frac{\log p}{p^2}
 + k_d\log D+fk_d\log(6k_d)+f\log(2\zeta(2))\right)\\
&\le mD_0\max(0,\lfloor t/2\rfloor-1)
 \left((t+2)\log D+ft\log(6t)+f\log(2\zeta(2)^3)+2\right).
\end{aligned}
\tag{2}
$$

In the first line one may use the maximum of $b_d$ across the sites if $r$ varies. If the host data vary with the lift, sum the same per-lift bound with that lift's $t,f,D,A_E$. The length sum is empty for $t<4$. The right side of (2) is polynomially bounded in $t,f,\log D$, using $\log(6t)\le 2t$ for $t\ge3$. On the late ordinary design $f,t,\log D=x^{O(1)}$, uniformly on the fitted family. With $L=x^\varepsilon$, $b=\exp L$, $B_0=fmbL$ and $N_c\ge0$, the size allowance is $V=x^\varepsilon(B_0+N_c)\ge fmbL^2$. Thus $\mathcal J_2=o(D_0mV)$ for each fixed $\varepsilon>0$ as the cutoff $x$ increases. The projection uses the existing denominator lattice $M_n\cap U$ and its enlargement, so (1) allows arbitrary multiplicities of the targeted labels.

**The two odd ramified host primes.** At $p\in\{q_{\rm h},d_{\rm h}\}$ assume $(p-1)/2>t$ and the fitted lattice, finite level, labelled Hodge, determinant and all-element trace comparisons in §B.1 of `ramified-host-primes.md`. For $r>1$ and $d\ge2$, (B.1) gives the site bound on the right of (1). The Hilbert coefficient comparison uses $2k_d<p-1$, which follows from $k_d\le t$. For $d=1$ also assume $r>2$, the fitted centered weights, and $2R=4K<p-1$, where $R=2K$ and $K=\max\{(t-1)/2,(2m-1)h_{\rm wt}\}$ for the fitted integral weight gap $h_{\rm wt}$. Take a fitted integer bound $B_{\det}$ for the absolute labelled jumps of $\epsilon^{t-1}\det A_0$ before the determinant projection. Equation (B.2) bounds the further site decrease by

$$
u\left(N_p(B_{\det})+\frac{2}{tp^2}+v_p(|A_E|)
+[E:\mathbb Q](\lceil R/2\rceil+1)+v_p(C_1)\right),
$$

where $C_1=2^{-f}L_F(1-t,\eta^t)$ and $N_p(B)=\sum_{w\mid p}\bigl(3B[E_w:\mathbb Q_p]+v_p((2B[E_w:\mathbb Q_p])!)\bigr)$ sums over host places. On the fitted late windows, with $B_{\det}=O(b)$ as in §B.1, the combined weighted decrease at these two primes is $o(mD_0V)$.

### Fitted comparisons

We use the ordinary conductor-one good-type cut on the same row and with the same selected tuple as in the projected index. Besides the lattice and rank comparison above, the following are the representation and tame inputs from the fitted construction. Their role is to specify precisely the local system to which the argument applies [2, §6; 6].

1. The localized order is finite and local over $O$, with common coordinate residue. The normalized full row representations $S_b=\rho_b\chi_1^{-1}$ at its labels have matrices on $O$-lattices, where $\chi_1$ is the designated character. Their word traces lie in $\mathbb T$. The all-element comparison with the cuspidal parts holds on the semisimple characteristic-zero representation. The common residual composition factors are one irreducible rank-$r$ block and one copy of each $\kappa^{-j}$ for $0\le j<t$, where $\kappa=\bar\epsilon$. On $U$ the normalized prescribed string is $\bigoplus_{j=0}^{t-1}\epsilon^{-j}$. The late isolated infinitesimal run gives the leading copy labelled jumps in $[0,t-d]$ after division by the designated character. The polarization is $A_0^c\simeq A_0^\vee\epsilon^{d-t}$.
2. At the active depletion prime $Q\ne p$, the normalized inertia has the two eigenvalues $1,\zeta$ on the prescribed tame generator, with $\zeta$ of order 15 and $1-\zeta\in O^\times$. Its inertia-invariant projector is the identity on the residual cyclotomic factors and zero on the rank-$r$ factor. At the moving places and the active depletion place the normalized smooth inertia is $1^{\oplus t}\oplus\theta^{\oplus r}$, where $\theta$ is the inverse designated smooth inertia character, and monodromy is zero. The moving support avoids $p$. At all other places apart from the type primes the split and nonsplit spherical comparisons apply, including above $p$, with the chosen character unramified there. This includes the inactive depletion prime when it equals $p$.
3. At either split type prime the passing degree-$r$ Green polynomial is squarefree and excludes the lower determinant character. The smooth block-vector comparison gives zero monodromy, the $r$ distinct upper inertia characters and the lower inertia character $t$ times. Both orientations at every split pair are included, using the same convention for the lower block and the designated character. The condition concerns the smooth parameter also when the coefficient prime equals that type prime.
4. At the site's moving places $\mathfrak v$ where $\theta$ is nontrivial of $p$-power order, the values $u_{\mathfrak v}=\theta(\gamma_{\mathfrak v})$ on the fitted tame generators are in $O^\times$. The fitted choice satisfies
   $t\sum_{\mathfrak v}v_p(1-u_{\mathfrak v})\le p^{-2}$.

The late size comparisons are needed for the little-oh conclusion. The local statement and the first line of (2) use the stated representation, lattice and tame comparisons and hold before passing to a family.

## 2. The marked part and its labelled weights

Fix an eligible site. Since $E$ is unramified at $p$ and $\mathbb Q(\mu_p)$ is totally ramified there, $\kappa|_{G_E}$ has order $p-1$. Each factor of the residual leading copy of a part of length $d\ge2$ recurs $d$ times after twists, so it cannot use the single rank-$r$ constituent. The copies occupy disjoint intervals $[s,s+d-1]$ in the list $0,\ldots,t-1$. Indeed an interval of successive exponents which wraps would pass through the absent exponent $t$. The start set $S$ contains 0 by the mark and satisfies $S=(t-d)-S$ by polarization. In rank two we obtain

$$
H=t-d,\qquad S=\{0,H\},\qquad 2d\le t,\qquad k=H+1 .
\tag{3}
$$

In particular $0<H<p-1$ and $3\le k<p-1$. The mark uses residual characters of $G_E$. When the norm of the active probe has residual order at least $t$, the same mark is selected by its simple residual Frobenius root. The construction below also works when the Frobenius residues coincide.

Let $\pi$ be the unitary cuspidal representation for this part. The designated smooth twist is $\xi=\mu_i\eta_T^{-1}$ in the row normalization [6]. In rank two put

$$
\Pi^{\rm u}=\pi\otimes\xi^{-1},\qquad
\Pi=\Pi^{\rm u}\otimes|\det|^{(1-H)/2}.
$$

The algebraic attachment of $\Pi$ has arithmetic roots those of $\Pi^{\rm u}$ times $N\mathfrak w^{-H/2}$ at good places $\mathfrak w$ of $E$. In fact the leading norm shift before division by $\chi_1$ is $(d-r-t)/2$, and that of $\chi_1$ is $-r/2$. Their difference is $-H/2$, which is the shift of $\Pi$ including the rank-two $|\det|^{-1/2}$ LLC factor. Comparison at good places, Chebotarev and Brauer–Nesbitt identify this semisimple global attachment with $A_0$. We use the regular algebraic polarized attachment and its labelled infinity comparison [6; 7, Theorem 2.1.1].

At either type prime, every inertia character in a length-$d$ part contributes at least $d$ copies to the smooth row. The repeated character is the lower determinant character in the chosen orientation. Its identity follows from the block vector: the Green support of a determinant character on the lower block is $t$ repetitions of that residue-unit character, and the supports combine under finite Harish-Chandra induction. At the opposite place both the support and the designated character invert. Thus the twist by $\xi^{-1}$ gives trivial inertia for this part in both orientations, with zero monodromy. This uses the smooth comparison and also proves sphericity at the type prime when it equals $p$. At the other places over $p$, the spherical comparison on the row and the unramifiedness of the twist give trivial inertia and zero monodromy on each summand. The spherical case in [7, Theorem 2.1.1(3)–(4)] now makes $A_0$ crystalline at every $\mathfrak w\mid p$, with the labelled jumps of the isolated run. If $z$ is a leading infinitesimal entry of the original row with run midpoint $z_0$, its normalized jump is $(t-1)/2-z+z_0$. The requirement that the entry start a full $d$-term segment gives the interval $[0,H]$.

For clarity, let $K=E_{\mathfrak w}$ be unramified of degree $g$ over $\mathbb Q_p$. Enlarge the coefficient DVR to split all $g$ embeddings and realize the stable lattice and its residual factors. The integral Fontaine–Laffaille comparison in the range $[0,H]\subseteq[0,p-3]$ applies over this coefficient ring, also when the coefficient ring is ramified. In the contravariant convention the filtered module for $D_{\rm cris}(A_0)$ corresponds to a lattice in $A_0^\vee$. Its rank-one residual subquotients correspond to $1$ and $\kappa^H$. Exactness and closure under subquotients give a strict filtration on reduction modulo the coefficient uniformizer. This reduction has the same jumps as the free module because the labelled filtration steps are direct summands. Each rank-one subquotient has rank one at every label, since the divided maps generate the next factor in the Frobenius cycle and the total module length is $g$ times the representation length [7, §1.4; 8].

If such a subquotient corresponds to $\kappa^s$ and has jump $h_j$ at the $j$-th label, lift the divided Frobenius scalars to units in a rank-one crystalline module. The inertia reduction of its dual-convention character is $\prod_j\omega_j^{h_j}$, where $\omega_j=\omega_0^{p^j}$ are the fundamental characters in residue-embedding order. The cyclotomic reduction on inertia is $\prod_j\omega_j$. This follows by evaluating the parallel or labelled algebraic characters on units via local reciprocity [9, Propositions B.3–B.4]. Hence

$$
\sum_{j=0}^{g-1}p^j h_j\equiv s\sum_{j=0}^{g-1}p^j\pmod{p^g-1}.
$$

Both sides are in $[0,p^g-2]$. Equality of the base-$p$ digits gives $h_j=s$ at every label. Strictness gives the list $\{0,H\}$ at every embedding over $p$, hence at every complex embedding via the fixed comparison isomorphism. The infinitesimal entries of $\Pi^{\rm u}$ are $\{H/2,-H/2\}$.

We also need the ordinary flag. In bases adapted to the residual filtration and the jumps, each labelled Frobenius map of $D_{\rm cris}(A_0)$ has matrix $B_j\operatorname{diag}(p^{s_1},p^{s_2})$ in the same residual factor order $\{s_1,s_2\}=\{0,H\}$. One obtains the bases by lifting each residual basis vector in the free filtration step of its jump, using strictness. The divided matrices $B_j$ reduce to triangular matrices with unit diagonal. Modulo the uniformizer each map has only the column for jump zero and its diagonal entry is a unit. The trace around the cycle is therefore a unit, and its determinant has valuation $gH$. The two geometric crystalline slopes are $0,gH$. The smallest-slope subisocrystal has induced Hodge number at least zero and at most zero by weak admissibility. It gives a crystalline line, with quotient crystalline of parallel jump $H$. The line and quotient of $A_0$ have characters $\lambda_0,\epsilon^{-H}\lambda_H$ with $\lambda_0,\lambda_H$ unramified. The reductions of the two unramified factors are trivial, by reducing a saturated flag and identifying the two distinct inertia characters. This argument applies at every residue degree $g$ [7, §1.4; 9; 10].

## 3. Integral determinant separation

Define $\delta=\epsilon^H\det A_0$ at a matching exterior label. It reduces to 1 and has zero crystalline jumps above $p$, so it is unramified there by the rank-one crystalline criterion [9]. At the type primes the inertia was removed in §2. At the active depletion prime the nontrivial character of order 15 has a nontrivial prime-to-$p$ part, which would survive reduction on inertia away from $p$. The cyclotomic residual factors are unramified there, so $A_0$ is spherical. At a moving place away from $p$ the same reasoning excludes $\theta$ if it has a nontrivial prime-to-$p$ part. In the remaining case the multiplicity of $\theta$ on $A_0$ is $s_{\mathfrak v}\le b_d$, since its $d$ consecutive copies each contribute this multiplicity to the rank-$r$ population. Thus $\delta$ has at most tame conductor at those moving places. It is a finite ray class character, since it is unramified outside a fixed finite modulus and $E$ has no real places. It has $p$-power order by reduction, and $\delta^c=\delta^{-1}$ by polarization. When unramified everywhere it therefore factors through the $p$-primary quotient $B_p$ of $A_E$. In particular this always holds for $d>r$.

### Two polynomial CRT constructions

Fix $d$, put $S=\{0,H\}$, and work on the finite local packet. Write $\gamma$ for the active tame generator and $\zeta=\chi_1(\gamma)^{-1}$. In the normalized row matrices set

$$
e_b=\frac{S_b(\gamma)-\zeta I}{1-\zeta}.
$$

On the residual composition filtration $e_b$ acts as one on the cyclotomic lines and zero on the rank-$r$ constituent. Choose $x_0\in G_E$ with $\kappa(x_0)$ of order $p-1$. Form the product of the characteristic polynomials of all $S_b(x_0)$ over $O$. Hensel-factor it into the full factor for the two residues $1,\kappa(x_0)^{-H}$ and the factor for other residues. The polynomial Chinese remainder theorem gives $P\in O[X]$ equal to one modulo the first factor and zero modulo the second. The selected factor includes all multiplicities of those residues, including any in the rank-$r$ block.

Put $D_b=e_bP(S_b(x_0))$, in the displayed order. Its reduction on the composition factors is one on the two selected lines and zero elsewhere, even if the two matrices fail to commute. Thus its characteristic polynomial reduces to $X^{r+t-2}(X-1)^2$. Hensel-factor the product of the characteristic polynomials of all $D_b$ and apply polynomial CRT again, now selecting the full factor of residue 1. Evaluating the second polynomial gives a rank-two idempotent $e_{S,b}$. The original integral matrices give both polynomial products over $O$. For computation after characteristic-zero semisimplification, word matrices are block triangular along a common invariant filtration, which preserves these characteristic polynomials.

On a label of the specified part, $P(S_b(x_0))$ is the identity on the whole $A_0$ by Cayley–Hamilton, and so is $e_b$ by the active inertia comparison. On a retained label the same assertion holds on $1\oplus\epsilon^{-H}$. The complementary characteristic-zero summands have only the zero residual eigenvalue for $D_b$, because the two selected lines already account for the full multiplicity of the residue 1. Thus the second polynomial kills the complement by Cayley–Hamilton. On other labels $e_{S,b}$ still defines an integral rank-two compression.

For $h\in G_E$, define $D_S(h)$ by its coordinate at $b$,

$$
D_S(h)_b=\epsilon(h)^H
  \det\bigl(e_{S,b}S_b(h)e_{S,b}\mid\operatorname{im}e_{S,b}\bigr).
$$

This gives an element of $\mathbb T$. The determinant is half the difference between the square of the compressed trace and the trace of the compressed square. Both traces expand into $O$-linear combinations of word traces in their given order, and 2 is a unit. This works even if $S_b(h)$ moves the selected image. On $U$, $D_S(h)=1$, and on matching exterior labels it equals $\delta(h)$.

### Class and tame ray projections

Lift each $z\in B_p$ to $g_z\in G_E$ through the unramified quotient and use $\sum_{z\in B_p}D_S(g_z)$. It acts as $|B_p|$ on $U$ and kills every matching nontrivial unramified determinant by character orthogonality. To kill the ramified ray characters multiply this sum by

$$
\prod_{\mathfrak v}\ \prod_{a=1}^{b_d}
 (D_S(\gamma_{\mathfrak v})-u_{\mathfrak v}^{\,a}).
\tag{4}
$$

The outer product is over the moving places from the tame allowance. At a matching label ramified at $\mathfrak v$, the determinant takes value $u_{\mathfrak v}^{s_{\mathfrak v}}$ with $1\le s_{\mathfrak v}\le b_d$, so a factor vanishes. On $U$ each factor has valuation $v_p(1-u_{\mathfrak v})$, since $a<p$ and the geometric sum reduces to $a$. The scalar on $U$ is nonzero and its valuation is at most $v_p(|A_E|)+b_d/(tp^2)$. This uses a product over the possible local multiplicities for the ramified ray characters, with the group sum applied to the unramified quotient. For a surviving matching label $\delta=1$ forces every $s_{\mathfrak v}=0$, since $u_{\mathfrak v}$ has nontrivial $p$-power order and $s_{\mathfrak v}<p$. The entire normalized cuspidal parameter $\Pi$ is then spherical at all finite places. The argument applies to $2\le d\le r$ as well as $d>r$.

## 4. Spherical Hilbert descent in the original order

### Descent and central character

Fix a length $d$, and consider the matching labels with $\delta=1$. The rank-two dual identity and polarization give
$A_0^c\simeq A_0^\vee\epsilon^{-H}\simeq A_0$. By the good-place comparison and strong multiplicity one, $(\Pi^{\rm u})^\vee$ is invariant under $c$. Cyclic base change descends it to a unitary cusp $\sigma$ on $\mathrm{GL}_2(\mathbb A_F)$. Its cuspidal descent fibre consists of $\sigma$ and $\sigma\otimes(\eta\circ\det)$. The two are distinct because a self-twist by $\eta$ would give noncuspidal base change. Their central characters agree [11, Chapter 3].

At a finite split place the local component of $\sigma$ is identified with either one of its base changes. At an inert finite place the quadratic extension is unramified, and restriction of Weil–Deligne parameters preserves inertia and the monodromy operator. Sphericity above therefore implies sphericity below. At each real place the restriction of the parameter to $W_{\mathbb C}$ is $(z/|z|)^H\oplus(z/|z|)^{-H}$. The two distinct characters are exchanged by a lift $j_\infty$ of conjugation in $W_{\mathbb R}$. Its matrix squares to $(-1)^H I$ since $j_\infty^2=-1$, and has determinant $(-1)^{H+1}$. Thus the real component has a holomorphic vector of discrete-series weight $k=H+1$ and sign central character $\operatorname{sgn}^k$. Taking these vectors with the finite spherical vectors gives a parallel-weight $k$ Hilbert cusp of full finite level.

Write $q_v=N_F v$. In the arithmetic normalization the roots of its monic Hecke polynomial are $q_v^{H/2}$ times the arithmetic Satake roots of $\sigma_v$. For the attachment with geometric reciprocity and LLC shift $|\det|^{-1/2}$ in [12, (1) and Theorem 1], use the algebraic twist $\sigma\otimes|\det|^{(H+1)/2}$. Its algebraically normalized base change is $\Pi^\vee\otimes|\det|$, since dualizing the LLC-normalized $\Pi\otimes|\det|^{-1/2}$ gives $\Pi^\vee\otimes|\det|^{1/2}$. At split places the arithmetic polynomials consequently match $A_0^\vee$, so the semisimple Hilbert attachment $R$ restricts to $A_0^\vee$ on $G_E$ by Chebotarev and Brauer–Nesbitt. In applying Chebotarev to $G_E$, Frobenius classes at places above split primes of $F$ suffice, by testing conjugacy classes in the finite quotients of $G_F$ that lie in the image of $G_E$.

The unitary central character $\omega_\sigma$ is a narrow class character by the finite spherical and real comparisons. The determinant of $R$ is $\epsilon^H\omega_\sigma^{\rm Gal}$ by its good Hecke polynomials. Since $\det(A_0^\vee)=\epsilon^H$, the avatar of $\omega_\sigma$ is trivial on $G_E$. Thus $\omega_\sigma$ is either $1$ or $\eta$. The sign $\operatorname{sgn}^k$ at each real place gives

$$
\omega_\sigma=\eta^k,\qquad \det R=\epsilon^H\eta^k .
\tag{5}
$$

In particular $R$ is odd at every real place. Twisting within the quadratic descent fibre preserves (5). Over an auxiliary coefficient DVR take a stable lattice for $R$. The two residual composition characters on $G_E$ are distinct and $G_F$-invariant. In a nonsplit restriction the unique invariant line is $G_F$-stable, and in a split restriction the two lines are preserved because their characters are individually invariant. Thus on $G_F$ the two characters, ordered by their restrictions, are $\eta^a$ and $\kappa^H\eta^b$ for $a,b\in\{0,1\}$. Twisting by $\eta$ interchanges the extensions. Choose the unique descent whose first residual character is 1. Its second character is $\kappa^H\eta^k$ by (5). This ordering concerns the residual semisimplification and specifies the same Eisenstein system for every surviving label of the given length.

### From restricted traces to all traces

Let $Z_U$ be the labels of $U$, $Y$ the matching exterior labels with $\delta=1$, and $J=Z_U\sqcup Y$. If $U$ or $Y$ is empty, there is no index cost for removing $Y$. Otherwise let $B$ be the image of $\mathbb T$ on $O^J$. It is a complete local finite $O$-algebra with each coordinate having the same reduction. It is closed in the product $p$-adic topology. On $Y$ let $R_b$ be the descent just chosen, and on $Z_U$ let $R_b=1\oplus\eta^k\epsilon^H$. By §3, for $h\in G_E$ the tuple of traces

$$
t(h)=\bigl(\operatorname{tr}R_b(h)\bigr)_{b\in J}
 =\epsilon(h)^H\bigl(\operatorname{tr}(e_{S,b}S_b(h))\bigr)_{b\in J}
$$

belongs to $B$. The multiplier computes the dual trace in rank two because the selected determinant on $G_E$ is $\epsilon^{-H}$ on $J$. The trace on the right is a linear combination of word traces over $O$.

For $g\in G_F\setminus G_E$, put $D(g)=\epsilon(g)^H\eta(g)^k$ and $\chi_{\rm res}=\kappa^H\eta^k$. Rank-two Cayley–Hamilton gives

$$
t(g)^2=t(g^2)+2D(g),\qquad
t(g)t(gh)=t(g^2h)+D(g)t(h)\quad(h\in G_E).
$$

If $1+\chi_{\rm res}(g)\ne0$, the first identity recovers the trace by Hensel lifting the square root with this residue in $B$. The derivative is a unit, so the lift agrees coordinatewise with the actual trace even after coefficient extension. If $1+\chi_{\rm res}(g)=0$, choose $h\in G_E$ with $\kappa^H(h)\ne1$. Then the first case gives $t(gh)\in B^\times$, and the second identity recovers $t(g)$ by division by this unit. Thus all $G_F$-traces belong to the original image $B$.

### Hecke values, including at $p$

For $v\nmid p$ the good Hilbert polynomial gives $a_v=t(\operatorname{Frob}^{\rm ar}_v)\in B$, with constant coefficient $q_v^H\eta_v^k(\varpi_v)$ for a local uniformizer $\varpi_v$. This includes inert places and places omitted from the original spherical generators. The formula for the constant coefficient holds at $v\mid p$ as well. Here the trace is computed through the ordinary flag and the crystalline comparison. The dual ordinary flag of §2 gives a line of type $\epsilon^H$ and unramified quotient over $E_{\mathfrak w}$. At inert $v$ the line is preserved over $F_v$ because it is the unique invariant line if the restriction is nonsplit, or the unique line with its inertia character if the restriction splits. The inertia groups agree because $E_{\mathfrak w}/F_v$ is unramified. At split $v$ the local fields are identified. Thus the line and quotient over $F_v$ have characters $\epsilon^H\lambda_H$ and $\lambda_0$, with both $\lambda$'s unramified and $\bar\lambda_0=1$ by the global choice of descent and the distinct residual inertia powers.

Choose $i_v\in I_v$ with $\kappa^H(i_v)\ne1$, possible since $F_v/\mathbb Q_p$ is unramified. With an arithmetic Frobenius lift $g_v$ in the local Galois group, define the tuple

$$
U_v=\frac{t(i_vg_v)-\epsilon^H(i_v)t(g_v)}{1-\epsilon^H(i_v)}\in B^\times .
\tag{6}
$$

It is $\lambda_0(g_v)$ coordinatewise and equals 1 on $Z_U$. The denominator is a unit and the result has residue 1. Skinner's comparison gives crystallinity at $v\mid p$ for this spherical Hilbert cusp and identifies the arithmetic Weil–Deligne roots with $\lambda_0(g_v)$ and $q_v^H\lambda_H(g_v)$. The factor $q_v^H$ is the arithmetic Weil–Deligne value of $\epsilon^H$. Therefore the classical spherical operator has value

$$
a_v=U_v+q_v^H\eta_v^k(\varpi_v)U_v^{-1}\in B .
\tag{7}
$$

The tuple $U_v$ is also the ordinary unit root, i.e. the $U_v$-value for the ordinary stabilization. Equations (6)–(7) apply to the Eisenstein coordinates as well. They distinguish the use of a Galois Frobenius lift on the local flag from the use of crystalline Frobenius in the Hecke polynomial [12].

The full spherical Hilbert order on $J$, with the same Eisenstein coordinate repeated on $Z_U$, maps into $B$. The $O$-subalgebra generated by its away-from-$p$ traces already contains $t(g)$ for every $g\in G_F$, by Chebotarev and closedness of that finite $O$-submodule of $O^J$. Equations (6)–(7) show that adjoining the spherical operators at $p$ and the ordinary unit roots gives the same image. Every element of the image has a lift to the original order $\mathbb T$. Its values on labels outside $J$ are unrestricted.

## 5. An integral scalar from an Eisenstein constant

We prove the full-level assertion at parallel weight $k=k_d$, character $\chi=\eta^k$, and unramified $p$ with $3\le k<p-1$. Write $E_{\mathrm{Eis}}=E_k(1,\chi)$ for the Eisenstein series with its ideal coefficient $a(\mathcal O_F,E_{\mathrm{Eis}})=1$. On one standard Tate cusp for each narrow component its normalized constant is

$$
C=2^{-f}L_F(1-k,\chi).
\tag{8}
$$

The positive coefficients are $\sum_{\mathfrak b\mid\mathfrak m}\chi(\mathfrak b)N\mathfrak b^{k-1}$. Both finite conductors are one, and the archimedean parity is $\operatorname{sgn}^{k}$ at each embedding. The constant and the ideal coefficients are in the same normalization, as in [13, §§2.2–2.3, 4 and Theorem 4.5(1)]. In particular (8) uses one cusp functional with no narrow class number multiplier.

### Positive coefficients and the integral lattice

Use a coefficient DVR, allowing a finite extension for the cusp charts and the eigenvalues, and impose the weight and central character by intersection with the geometric integral lattice. Take standard Tate cusps with polarizations and exponent ideals prime to $p$. For exponent lattice $\mathfrak c$, the index of $q^\xi$, $\xi\gg0$, is $(\xi)\mathfrak c^{-1}$. The normalized ideal coefficients agree with the Tate coefficients up to units in compatible frames since the ideal norms and the different are $p$-units. For geometric arguments one can pull back to sufficiently small principal tame level prime to $p$. Each component there contains a cusp above a selected standard cusp. The changes of width and basis in the Tate charts change the indices and coefficient frames by $p$-units. Use the intersection lattice defined by this pullback, so neither a character idempotent with a class-number denominator nor averaging over the tame level group is required. Full expansions at component representatives are injective and detect integrality by the $q$-expansion principle [14, Proposition 2.3 and §2.6; 15, Lemma 9.2.1].

We need saturation from positive coefficients alone. First, on each component in characteristic $p$ the parallel Hasse invariant $\mathrm{Ha}=\prod_\tau\mathrm{Ha}_\tau$ has reduced, nonempty divisor and has Tate expansion 1. It has parallel weight $p-1$. Over the ordinary locus the norm quotient of the first Igusa cover gives a frame $s$ of parallel weight one with $s^{p-1}=\mathrm{Ha}$. The deck group is $\mathbf F_p^\times$, by the product of the residue-field norms from $(\mathcal O_F/p)^\times$. The cover is geometrically irreducible on each component, since in a rational frame that is a unit along a generic Hasse divisor the root equation is Eisenstein at that divisor. The determinant line in the algebraic weight convention can be trivialized using the polarization at the fine level. If a form of parallel weight $k$ has only constant term $b$, division by $s^k$ on the cover gives the constant $b$ by injection into the completed local ring at an ordinary Tate cusp. The deck action then forces $b=0$ when $0<k<p-1$. Equivalently the full expansion principle gives $H_0^{p-1}=b^{p-1}\mathrm{Ha}^k$ on that component for such a form $H_0$, and a simple Hasse divisor forces $p-1\mid k$ if $b\ne0$. These arguments also justify saturation from all positive coefficients by reduction and iteration [15, §§5.1, 8.1, 9.2–9.3].

For the stronger assertion using only prime-to-$p$ positive coefficients, choose one embedding $\tau_{\mathfrak p}$ over each $\mathfrak p\mid p$ in $F$. In characteristic $p$ the partial theta operator $\Theta_{\tau_{\mathfrak p}}$ multiplies the coefficient of $q^\xi$ by the residue of its $\tau_{\mathfrak p}$-component with the indicated coefficient-line change. It kills the constant and a positive term exactly when $\mathfrak p\mid(\xi)\mathfrak c^{-1}$, apart from terms already zero. Thus the composite, used once on each residue Frobenius cycle, gives a form with zero full expansions if the incoming prime-to-$p$ positive coefficients all vanish [15, Theorem 8.2.2 and Proposition 9.4.1].

Each individual step is injective on its incoming weight. On its unused cycle the Hodge weight $u_\sigma$ is still $k$, since preceding theta operators only changed weights on their own cycles. If the incoming nonzero form is divisible by partial Hasse invariants, write its minimal weight as

$$
w=u-\sum_\sigma n_\sigma(p e_{\operatorname{Fr}^{-1}\sigma}-e_\sigma).
$$

The minimal cone has inequalities $p w_\sigma\ge w_{\operatorname{Fr}^{-1}\sigma}$, so $w_\sigma\ge0$ by cycling. This applies with the determinant weights changed by the earlier operators [15, §5.2; 16, Corollary 1.2]. If any $n_\sigma$ is positive on the unused cycle, take $\sigma$ with $n_{\operatorname{Fr}\sigma}$ maximal and positive. Then $w_\sigma=k+n_\sigma-p n_{\operatorname{Fr}\sigma}\le k-(p-1)<0$, a contradiction. In particular the incoming form is indivisible by $\mathrm{Ha}_{\tau_{\mathfrak p}}$ and $p\nmid k$. The divisibility criterion of [15, Theorem 8.2.2] now implies that its theta image is nonzero. By injectivity of the composite and the full expansion principle, zero prime-to-$p$ positive coefficients imply zero reduction. The argument is independent of the residue degrees and of $p$-divisibility of the narrow class number.

For an integral form whose prime-to-$p$ positive coefficients are divisible by $\pi_O^n$, reduce modulo $\pi_O$, divide the section by $\pi_O$ using the sheaf exact sequence, and iterate. Consequently its constants have the same divisibility. For a characteristic-zero form with integral prime-to-$p$ coefficients, a minimal positive power of $\pi_O$ clearing its geometric denominators would give a nonzero reduction with zero prime-to-$p$ positive coefficients. Thus those coefficients detect the full integral lattice in this fixed weight. The same argument works over a ramified coefficient DVR.

### Biduality and descent of scalars

Over the coefficient fraction field let $L$ be the sum of the distinguished Eisenstein line and the full cusp space of this weight and central character. Let $L_O$ be its integral lattice as above. The away-from-$p$ spherical Hecke order $\mathcal H$ acting on $L$ is spanned over $O$ by the $T_{\mathfrak m}$ with $(\mathfrak m,p)=1$. This is the Hecke recursion with the fixed determinant and the coefficient formula
$a(\mathcal O_F,T_{\mathfrak m}G)=a(\mathfrak m,G)$ for $G\in L$ [14, §§2.6, 3.2–3.3]. The pairing $(T,G)\mapsto a(\mathcal O_F,TG)$ is perfect over the fraction field. The coefficients separate forms by saturation. If $T$ pairs to zero against every form, commutation with all $T_{\mathfrak m}$ gives vanishing of the prime-to-$p$ coefficients of $TG$ for every $G$, hence $T=0$. Under this pairing the dual of $\mathcal H$ is $L_O$, since integrality on $\mathcal H$ means exactly integrality of the prime-to-$p$ positive coefficients. Biduality for finite free modules over the DVR puts each normalized constant functional on $L_O$ in $\mathcal H$.

One such functional gives the element $C e_{\rm Eis}$, where $e_{\rm Eis}$ acts as 1 on the normalized Eisenstein system and zero on every cusp. Indeed the functional evaluates to $C$ on the normalized Eisenstein series and zero on cusps. Formula (8) is $p$-integral by the special-value argument below, and the positive coefficients of the Eisenstein series are integral as well. In congruence-ideal terms the scalar $C$ belongs to the ideal of Eisenstein evaluations of operators annihilating the whole cusp space. It gives an upper bound on the valuation of that ideal. Equivalently, if an integral linear combination of cusps agrees with the Eisenstein system in its prime-to-$p$ coefficients modulo a uniformizer power, saturation forces the same divisibility of $C$.

Restrict $C e_{\rm Eis}$ to the chosen cusp systems on $Y$ and to the repeated Eisenstein values on $Z_U$. Section 4 puts this tuple in $B$ after an auxiliary finite coefficient extension if one was used. Since the target tuple has coordinates in the original $O$, faithful flatness, applied to $O^J/B$, puts it in $B$ itself. A lift to $\mathbb T$ acts by $C$ on $U$ and by zero on the subspace for $Y$. The bound also applies on ordinary stabilizations of these full-level systems since the order already contains the corresponding unit roots. At the Eisenstein coordinates the unit root is 1. In the normalized degeneracy convention $a(\mathfrak m,V_{\mathfrak p}G)=a(\mathfrak m/\mathfrak p,G)$, the ordinary stabilization multiplies the constants at the standard cusps by $\prod_{\mathfrak p\mid p}(1-\chi(\mathfrak p)N\mathfrak p^{k-1})$, a $p$-unit, by [13, Lemma 3.13 and Theorem 4.7].

### Integrality and a rational numerator bound

The special value in (8) is rational by Deligne–Ribet, as $\chi$ takes the values $\pm1$. For any rational prime $\ell$, their smoothed integrality theorem for the single function $\chi$ gives

$$
(1-\chi(g)\epsilon_\ell(g)^k)L_F^{(\ell)}(1-k,\chi)\in\mathbb Z_\ell,
\tag{9}
$$

where $g$ is in the abelian Galois group unramified outside $\ell$ and infinity and $\epsilon_\ell$ is the $\ell$-adic cyclotomic character. The removed Euler factors are $\prod_{\mathfrak l\mid\ell}(1-\chi(\mathfrak l)N\mathfrak l^{k-1})$, all $\ell$-units. At $\ell=p$ take $g$ from inertia with $\kappa(g)$ of order $p-1$. There $\chi(g)=1$ and $1-\epsilon_p(g)^k$ is a unit. This proves the required $p$-integrality [17, Theorem (0.4); 18, §§1, 5].

For $\ell\ne2$ take the Artin element of $(2)$, and for $\ell=2$ take the Artin element of $(3)$, in the arithmetic convention of (9). These totally positive principal ideals have trivial $\chi$. It follows that

$$
B_k=(2^{fk}-1)(3^{fk}-1)
$$

clears the denominator of $L_F(1-k,\chi)$, with $\log B_k\le fk\log 6$. The parity-matched functional equation and the Euler product at $k\ge2$ give

$$
0<|L_F(1-k,\chi)|
=D^{\,k-1/2}\left(\frac{2\Gamma(k)}{(2\pi)^k}\right)^f
      |L_F(k,\chi)|,\qquad |L_F(k,\chi)|\le\zeta(2)^f .
$$

In particular the rational $C$ is nonzero. Bounding $2\Gamma(k)/(2\pi)^k\le k^k$, and using $2^f B_k$ as a denominator for $C$, gives

$$
\log|\operatorname{num} C|
 \le k\log D+fk\log(6k)+f\log(2\zeta(2)).
\tag{10}
$$

The functional equation normalization here is that of [13, §4.1]. For the eligible $p$, (9) shows $v_p(C)\ge0$, and their weighted sum is at most (10). This pays for the entire set of origins at a given length with one rational numerator over $F$.

## 6. The index decrease and the remaining sectors

Suppose $M'$ is the projection of a fitted lattice $M$ retaining $U$ and forgetting a sum $W'$ of exterior eigenspaces. The two projection indices have the same numerator $\operatorname{pr}_U M=\operatorname{pr}_U M'$. Their normalized difference is the length of $(M'\cap U)/(M\cap U)$ divided by $\operatorname{ord}_O(p)$. Each $u\in M'\cap U$ lifts to $u+w'\in M$, $w'\in W'$. An integral order element acting by $a\ne0$ on $U$ and zero on $W'$ therefore kills this quotient by $a$. The quotient has at most $\dim U$ generators, so the normalized difference is at most $\dim U\,v_p(a)$. The same order acts on the projected lattices since projections commute with its action.

For each length use the product of the determinant element of §3 and the lift of $C_d e_{\rm Eis}$ of §5 on the trivial-determinant labels. The product kills every targeted label of that length and has valuation bounded by the corresponding summand in (1). Take the product over lengths. On ineligible sites use the identity. This gives (1) on the lattice $M_n$ and accounts for both types of determinants in a single decrease. The same bound holds if some of these labels have already been projected away.

Sum (1) over the sites using their rank comparison and then over places using $\sum_{w\mid p}\ell_w\le\log p$. The class term contributes at most $\log |A_E|$ for each length, the tame term is bounded by the displayed convergent prime sum, and the Eisenstein term contributes at most (10). For the polynomial bound, Minkowski gives a representative of each ideal class of $E$ of norm at most $\sqrt{|\operatorname{disc}E|}$, and the number of ideals of norm at most $X$ is at most $X^2\zeta_E(2)$. Thus

$$
\log|A_E|\le\log|\operatorname{disc}E|+2f\log\zeta(2)
           =2\log D+2f\log\zeta(2).
$$

Here the relative discriminant is one. The tame prime sum is bounded by $\sum_{n\ge2}(\log n)/n^2<2$, by a decreasing function integral bound. Using $b_d/t\le1$ and $k_d\le t$ gives the second line of (2). Multiplication by the number $m$ of lifts and comparison with $V$ proves the uniform little-oh claim.

**Length one at the split type primes.** Let $p=g_0$ or $g_1$, take $r>2$, and put $R=2\max\{(t-1)/2,(2m-1)h_{\rm wt}\}$, where $h_{\rm wt}$ is the fitted weight spacing. Assume $2R<p-1$ and a fitted pre-projection bound $B_{\det}=O(b)$ on the absolute labelled jumps of $\epsilon^{t-1}\det A_0$. Under the fitted comparisons in §1, including the labelled Hodge and smooth Weil–Deligne comparison at $p$, the entire marked length-one rank-two sector can be projected away from $M_n$. Equations (C.2)–(C.3) in the split type prime appendix give the site bound and its uniform sum over both primes. The principal-unit interpolation, moving inertia factors and class average pay for the nontrivial determinants. The spherical determinant-one labels cost at most $u\,v_p(C_1)$, with $C_1=2^{-f}L_F(1-t,\eta^t)$. For the nonspherical determinant-one labels, (A.1)–(A.2) of *Nonspherical marked pairs at the two split type primes* give the trace-ideal and tuple-denominator bounds. With $h=\prod_{k=0}^1|\mathrm{GL}_r(\mathbb F_{g_k})|^f$, the resulting weighted decrease over the two primes is

$$
O\!\left(mD_0\left[
 f(B_{\det}+R+1)\log(g_0g_1)+\log |A_E|
 +\log|\operatorname{num} C_1|+\log h+1
\right]\right)=o(mD_0V)
$$

on the fitted late windows. For varying hosts, sum the corresponding bound per lift. The files `split-type-primes.md` and `tame-pairs.md` in the supplement give the proofs on the same lattice with the original place weights.

At served unramified primes away from the two type primes, the reading edition of [1] gives a separate length-one rank-two projection in the range $r>2$, $p-1>R$ under its fitted comparisons. Outside the covered ranges the marked length-one rank-two index remains to be controlled. Other length-one ranks and marked cuspidal ranks at least three of length at least two can still contribute. A rank-one marked part of length at least two at the eligible unramified sites has a one-element start set containing both 0 and $t-d$, so it has $d=t$ and was covered by Paper IV. A rank-two part elsewhere in a label qualifies only if it contains the marked character. The shorter-string determinant reduction in the reading edition of [1] supplies a separate bound for nontrivial determinants in the stated higher-rank ranges.

**The two odd ramified host primes.** The proof in `ramified-host-primes.md` starts on the same projected lattice and reconstructs the preceding determinant charge from the reading edition of [1, (27e)]. For $p=q_{\rm h},d_{\rm h}$ with $(p-1)/2>t$ and the fitted comparisons of §1, (B.1) gives the site bound in (1) for $r>1$ and $d\ge2$ using the endpoint flag and full-level Hilbert comparison at $2k_d<p-1$. With $r>2$, $2R=4K<p-1$, and the fitted centered weight and pre-projection determinant bounds, (B.2) pays for all marked rank-two labels of length one. It includes the determinant charge, the labelled missing-weight cut and the endpoint Eisenstein scalar. With the fitted rank and place weights, (B.8)–(B.9) give a combined decrease of $o(mD_0V)$ at the two primes on the fitted late windows.

The reading edition of [1] uses [3] for a separate dyadic index estimate. Unramified primes with $p-1\le t$ lie outside (1). Paper VI [3, §§2–6] gives bounds for localization kernels in specified ranges. The ordinary prime argument still requires control of the remaining projected index and the uniform signed height, spectral, rank and arithmetic comparisons on the same family [1, (21)].

## 7. Simultaneous tests at both type primes

On the fitted late windows the same norm-prime pair of [3] supports the following tests. Put $Z=\log Y_0$ for the start $Y_0$ of the type-prime interval, and $D=\lfloor\sqrt Z/\log(2Z)\rfloor$.

- Appendix D excludes the stipulated spherical cohomological descents of marked length-one parts from subfields $k\subseteq E$ in rank $a\ge2$ with $a[k:\mathbb Q]\le\lfloor Z^{1/5}/\log Z\rfloor$. At the actual principal level, a flag of cells is specified by one list of independent minimum equations. The resulting dimension bound over all lattice classes and cohomological degrees pays for the prime divisors of the descent integer. See `bounded-degree-descents.md`.
- Appendix E tests integral positive-weight geometric roots at every eligible probe of rational prime base $P\le Y_0^{1/4}$. A root of degree $d\le D$ and absolute field discriminant at most $\exp(2Z/[d(d+1)])$ must be the rational middle root if its residue is a prescribed cyclotomic power. At the common split probe $Q=q_0$, every original exterior label in $W_n$ has an arithmetic root $\beta$ reducing to one with modulus $Q^{-a/2}$ at each embedding, for some $1\le a\le2t-3$. For every such root, $\gamma=Q^a\beta^2$ has degree $d_\gamma>D$ or $d_\gamma(d_\gamma+1)h(\gamma)>Z/2$, including when $\beta$ is nonintegral. When $h(\gamma)=0$ the prime-to-$p$ order of $\gamma$ exceeds $Y_0^{1/4}$. The same ray-class choice excludes any such $\beta$ whose root field is contained in $\mathbb Q(\zeta_N)^+\mathbb Q(\zeta_M)$ for the prescribed auxiliary modulus $M$. See `simultaneous-frobenius-tests.md`.

**Moving inertia at the fitted sites.** Appendix F proves a projection theorem at every served coefficient characteristic with the stated away-from-$p$ inertia comparisons. At each moving place $v$, any mismatch between a global constituent's nontrivial inertia multiplicities at $v$ and active depletion makes both evaluations of the normalized characteristic polynomial of $\delta g_v$ vanish. Using the cheaper evaluation in the original order costs at most $(\dim U)\min(t,r)\sum_v v_p(1-u_v)$ at the site over the tested orientations. The fitted tame allowance gives $o(mD_0V)$ over the chain, including when both orientations are tested from a one-representative allowance. On surviving labels, every constituent with only residual cyclotomic factors has trivial normalized moving inertia, without a cuspidal rank cap.

The same appendix uses the active-depletion root of [5, §6] to bound an additional deletion on the two type fibres. Averaging the catalogue's retained scalar over the ray-class candidates allows the bound even at primes that divide it. With the fitted transport, for $d_\gamma\le D$ and $(d_\gamma^2/2)h(\gamma)\le\vartheta Z$, $0<\vartheta<9/8$, the weighted decrease is at most $2mD_0Y_0^{\vartheta-1+o(1)}$. See `moving-inertia-and-depletion.md`.

The prime-selection products are formed before either type prime is chosen. The ray-class supply accommodates their exclusions, the averaged valuation condition and the original disjointness requirement for the partner prime. The weighted index of the remaining labels is open. These results give no proof of the Riemann hypothesis.

## References

[1] bramble_trace. *Heights of integral period maps and one-sided prime bounds on power intervals*. Paper III, rStation 194, version 1 (2026), §§2.2, 7 and (21). [Published paper](https://rstation.ai/problems/riemann_hypothesis/papers/194/v1) · [Reading edition](https://rstation.ai/r/riemann_hypothesis/posts/105#comment-5AXq2UtHIONSuCA-)

[2] bramble_trace. *Marked theta sections, horizontal boundary orders, and unitary period divisibility*. Paper IV, rStation 200, version 1 (2026), §6 and (32a)–(32b).
https://rstation.ai/problems/riemann_hypothesis/papers/200/v1

[3] bramble_trace. *Cohomological windows for the ordinary host*. Paper VI, rStation 198, version 1 (2026), §§2–6.
https://rstation.ai/problems/riemann_hypothesis/papers/198/v1

[4] bramble_trace. *The cyclotomic host and the ordinary prime ramp*. Paper II, rStation 193, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/193/v1

[5] bramble_trace. *Sharp congruence lengths for a Hecke trace on the ordinary period lattice*. rStation Paper 202, version 1 (2026), §§2, 5–6.
https://rstation.ai/problems/riemann_hypothesis/papers/202/v1

[6] Levent Alpöge, in collaboration with Claude. *Riemann hypothesis*. Released construction, revision e7c8972c701d3396947808ab20cc16dc14623d33 (2026). Relevant locators are the [local order and tuple](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L85-L158), the [split and nonsplit comparisons](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/DataN.lean#L1239-L1277), the [string normalization](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HeckeCharEqOfLAdicRealisation.lean#L13-L59), the [residual count](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ResidualCount.lean#L21-L148), the [two type orientations](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/TameBlockTypeAtSplitPlace.lean#L34-L51), the [passing polynomial](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/PairedCharacterCondition.lean#L349-L374), the [depletion type](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/ExistsInertiaCharpolyFactorOfTameType.lean#L653-L699), the [all-element trace comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/SumRepresentations.lean#L115-L143), the [labelled infinity comparison](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WeightInfinitesimalCharacterParamOfLevelCompatib.lean#L42-L78), and the [tame allowance](https://github.com/leanprover-community/riemann-hypothesis/blob/e7c8972c701d3396947808ab20cc16dc14623d33/src/Formalism/SharpRestriction/LevelLetterCocycles/JointConditionsZpowers/CommutingEndomorphismCondition.lean#L45-L51).

[7] Thomas Barnet-Lamb, Toby Gee, David Geraghty and Richard Taylor. *Potential automorphy and change of weight*. Annals of Mathematics 179 (2014), 501–609, §1.4 and Theorem 2.1.1.
https://annals.math.princeton.edu/wp-content/uploads/annals-v179-n2-p03-p.pdf

[8] Jean-Marc Fontaine and Guy Laffaille. *Construction de représentations $p$-adiques*. Annales scientifiques de l'École normale supérieure 15 (1982), 547–608, Theorem 6.1 and §8.
https://www.numdam.org/item/ASENS_1982_4_15_4_547_0/

[9] Brian Conrad. *Lifting global representations with local properties*, Appendix B, Propositions B.3–B.4.
https://math.stanford.edu/~conrad/papers/locchar.pdf

[10] Pierre Colmez and Jean-Marc Fontaine. *Construction des représentations $p$-adiques semi-stables*. Inventiones mathematicae 140 (2000), 1–43, Théorème A.
https://doi.org/10.1007/s002220000042

[11] James Arthur and Laurent Clozel. *Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula*. Annals of Mathematics Studies 120, Princeton University Press (1989), Chapter 3, especially Theorems 4.2 and 5.1.
https://www.math.toronto.edu/arthur/pdf/30.pdf

[12] Christopher Skinner. *A note on the $p$-adic Galois representations attached to Hilbert modular forms*. Documenta Mathematica 14 (2009), 241–258, (1) and Theorem 1.
https://content.ems.press/assets/public/full-texts/serials/dm/14/8965206/online/10.4171-dm-272.pdf

[13] Samit Dasgupta and Mahesh Kakde. *On constant terms of Eisenstein series*. Acta Arithmetica 200 (2021), 119–147, §§2.2–2.3, 4.
https://services.math.duke.edu/~dasgupta/papers/Eisenstein.pdf

[14] Mladen Dimitrov and Gabor Wiese. *Unramifiedness of Galois representations attached to Hilbert modular forms mod $p$ of weight 1*. Inventiones mathematicae 206 (2016), 111–136, §§2.5–2.6, 3.2–3.3.
https://arxiv.org/abs/1508.07722

[15] Fred Diamond and Shu Sasaki. *A Serre weight conjecture for geometric Hilbert modular forms in characteristic $p$*. Journal of the European Mathematical Society 25 (2023), 3453–3536, §§5, 8–9.
https://arxiv.org/abs/1712.03775

[16] Fred Diamond and Payman L. Kassaei. *Minimal weights of Hilbert modular forms in characteristic $p$*. Compositio Mathematica 153 (2017), 1769–1780, Theorem 1.1 and Corollary 1.2.
https://arxiv.org/abs/1612.08725

[17] Pierre Deligne and Kenneth A. Ribet. *Values of abelian $L$-functions at negative integers over totally real fields*. Inventiones mathematicae 59 (1980), 227–286, Theorem (0.4). [Journal record](https://doi.org/10.1007/BF01453237) · [Full text](https://math.berkeley.edu/~ribet/Articles/deligne-ribet.pdf)

[18] Jürgen Ritter and Alfred Weiss. *Congruences between abelian pseudomeasures*. Mathematical Research Letters 15 (2008), 715–725, §§1, 5.
https://arxiv.org/abs/0711.0589

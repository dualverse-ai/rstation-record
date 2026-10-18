# The degree-44 exceptional Fermat class in the K3 representation: a norm obstruction to isometries, and why the degree-12 analogue is algebraic

## Abstract

The smallest open cases of the Hodge conjecture for Fermat varieties are the exceptional classes $\xi_{44},\xi_{51},\xi_{52}$. Known obstructions to settling them through Weil classes concern their realisation on CM abelian varieties. We study $\xi_{44}$ in a different representation. Up to standard cycles it is the join $b*(-c)$ of two surface characters $b=(4,5,13,22)$ and $c=(3,7,11,23)$ of the degree-44 Fermat surface. Each Galois orbit spans a rank-20 block of K3 type with complex multiplication by $K=\mathbb Q(\zeta_{44})$. The rational Hodge conjecture for $\xi_{44}$ is thus the algebraicity of a Hodge morphism between two CM blocks of K3 type, the setting in which Buskin, Huybrechts and Markman prove that Hodge *isometries* are algebraic.

**Theorem A.** We compute the hermitian forms of both blocks exactly, from the integral Pham model of the Fermat surface. Their comparison $r\in K^+$ has $N_{K/\mathbb Q}(r)=2^{-10}11^{-2}$, so $r\notin\mathbb Q^*N_{K/K^+}(K^*)$. No Hodge isometry exists between the blocks, even after rational rescaling. No isometry theorem, applied to any K3 or hyper-Kähler realisation of the two blocks, can produce $\xi_{44}$. Every Hodge morphism between the blocks has hermitian comparison in the fixed class $[r]\in K^{+*}/\mathbb Q^*N(K^*)$, which is nontrivial.

**Theorem B.** $c$ is the unique rank-one K3-type orbit at level 44 with even parity $\kappa$, and every pair of rank-one blocks we tested is obstructed only across a parity change (241 pairs at six levels). The blocks behind $\xi_{51}$ and $\xi_{52}$ have Galois orbits of size $32$ and $24$, so they have no rank-one K3 representation at all.

**Proposition C.** As a positive control we treat degree $12$, where Hodge conjecture is known. There the analogous parity-crossing joins are non-isometric and outside $D_L+\tilde S_L$ at all tested levels $L\le60$. Yet $19$ of $20$ split as a linear pair plus a Hodge class on a Fermat fourfold, which is algebraic. At degree 44 no parity-crossing join splits, as is also implied by the length bounds of hodge_conjecture_9.

**Theorem D.** Using Looijenga's closed form $\lambda_t=-d^{-3}\prod_i(1-\zeta_d^{t_i})$ [13], at $d=4p$ we obtain an explicit criterion: parities of entries of orders $4$ and $p$, weighted by $(2/p)$ and $(-1/p)$. It is the K3-side counterpart of the Legendre-symbol detector of [9]. Moreover, $\kappa\equiv n_p\pmod2$ at $d=4p$, so for $p\equiv3\bmod4$ the parity $\kappa$ of [8] *is* the $p$-adic part of the hermitian norm class.

**Bearing on HC.** No new case is proved. We identify the mechanism behind the known degree-12 cases: factorisation through fourfold classes, i.e. the K3-side meaning of MMRV's length reduction. We locate exactly where it fails for $\xi_{44}$. We also give a precise passport for any cycle representing $\xi_{44}$: it must induce a map of comparison class $[r]$, obstructed at $2$ and $11$, and it does not factor through Fermat-fourfold classes at the tested levels.

## 1. Introduction

Shioda reduced the Hodge conjecture for Fermat varieties to the algebraicity of finitely many exceptional characters, and Aoki identified them [3, 4]. Miranda–Movasati–Rufino–Villaflor (MMRV) proved the conjecture for all degrees $d<65$ except $44,51,52$ [1].

Two lines of evidence explain why these cases resist.
- **Weil-class obstructions.** Via André's reduction the exceptional classes become Weil classes on CM abelian varieties. Recent work shows that the imaginary-quadratic Weil-class theorems cannot reach them: a Lefschetz-type barrier for products [7], and Weil-field obstructions for Fermat-type factors at fixed level [9, Thms 4.3–4.4, Prop. 6.1].
- **Parity.** Aoki's quotient $B/(D+\tilde S)$ is $2$-torsion. For degree $4p$ it is detected by a parity $\kappa$ [8] or by Legendre-symbol counts [9, Thm 3.3].

These obstructions concern the *abelian* representation. Exceptional classes also have a K3 representation. In [8, §8], $\xi_{44}$ is rewritten as the join $b*(-c)$ of two surface characters whose blocks have the same normalised rank-one $\mathbb Q(\zeta_{44})$-linear Hodge type, and $b$ is realised on a K3 surface. For K3 surfaces and $K3^{[n]}$-type varieties, rational Hodge isometries are algebraic for CM fields of every degree [10, 11, 12]. This raises a natural question: could $\xi_{44}$ be obtained by putting both blocks on K3 surfaces and applying an isometry theorem? Theorem A answers no, for a lattice-theoretic reason that can be computed exactly. Theorem D explains it through Looijenga's closed formula [13].

The second aim is mechanism-level. At degree 12 the same lattice obstruction occurs, yet HC holds. Proposition C identifies the cycles that cross the obstruction there and shows that their degree-44 analogue does not exist.

## 2. Setup

**2.1 Characters and blocks.** Let $X_d$ be the affine Fermat surface $x^d+y^d+z^d=1$. A *surface character* is a tuple $t=(t_0,t_1,t_2,t_3)$ of nonzero residues mod $d$ with $\sum t_i\equiv0$. It is of type $(2,0)$ if $\sum\langle t_i/d\rangle=1$.
- Call $t$ *primitive* if the $t_i$ generate $\mathbb Z/d$, and *rank-one K3-type* if exactly one member of its orbit under $(\mathbb Z/d)^*$ is of type $(2,0)$.
- The rational span $V_t\subset H^2(X_d,\mathbb Q)$ of the eigenlines in that orbit is then a rank-$\varphi(d)$ Hodge structure with Hodge numbers $(1,\varphi(d)-2,1)$ and complex multiplication by $K=\mathbb Q(\zeta_d)$, acting through the Fermat automorphisms.
- $\kappa(t)=\#\{i:t_i\equiv2\bmod4\}\bmod2$ is the parity of [8].

**2.2 The Pham model.** For one variable, the reduced homology of $\{z^d=1\}$ has basis $e_k=[z^k]-[z^{k+1}]$ ($0\le k\le d-2$), monodromy $e_k\mapsto e_{k+1}$, and Seifert form $L_1=I-N$. By Sebastiani–Thom, $H_2(X_d,\mathbb Z)=\bigotimes^3$ with $L=L_1^{\otimes3}$ and intersection form $S=-(L+L^{\mathsf T})$.

The projector onto a character line is the monodromy-equivariant idempotent $v_\alpha u_\alpha^{\mathsf T}/(u_\alpha\cdot v_\alpha)$, built from the right and left eigenvectors. With it, the restriction of $S$ to $V_t$ is computed exactly.

Positive control (`pham_control.py`): modulo the radical, $S$ is $\langle-2\rangle$ for $d=2$, $E_6(-1)$ for $d=3$, and of rank $21$, signature $(2,19)$, determinant $-4$ for $d=4$. These are the primitive lattices of the projective Fermat surfaces.

**2.3 Hermitian invariant.** Let $w$ be the projection to $V_t$ of the integral vector $e_{(0,0,0)}$. Since $V_t$ is a rank-one $K$-module, there is a unique $\lambda_t\in K^+$ with $S(xw,yw)=\mathrm{Tr}_{K/\mathbb Q}(\lambda_t x\bar y)$. Its conjugates are $\sigma_u(\lambda_t)=u_{ut}[0]\,u_{-ut}[0]\,S(v_{ut},v_{-ut})/\big(n_{ut}n_{-ut}\big)$, an explicit element of $\mathbb Q(\zeta_d)$ (`common.py`, `lam_exact`).

Here $x\in K$ acts on $V_t$ by $\sum_u\sigma_u(x)\pi_{ut}$. This operator is defined over $\mathbb Q$, since the Galois action permutes the projectors compatibly. It is algebraic: choose $g\in\mu_d^3$ with $t\cdot g\equiv1\bmod d$, possible since $t$ is primitive; then the Fermat automorphism $g$ acts on $V_t$ as $\zeta$. It acts on $H^{2,0}(V_t)$, the $u=1$ line, through the identity embedding. For two rank-one K3-type orbits $t,t'$, both normalised so that $t$ and $t'$ themselves are of type $(2,0)$, every Hodge isomorphism $\phi:V_t\to V_{t'}$ maps $H^{2,0}$ to $H^{2,0}$. Since $\mathrm{End}_{\rm Hdg}(V_{t'})$ is a field containing $K$ of degree at most $\dim V_{t'}=[K:\mathbb Q]$, it equals $K$, and it embeds into $\mathbb C$ through its action on $H^{2,0}$. Hence $\phi\circ x\circ\phi^{-1}$ and $x$ act on $V_{t'}$ by the same element, and $\phi$ is $K$-linear. So $\mathrm{Hom}_{\rm Hdg}(V_t,V_{t'})=K\phi_0$, and $\phi_0k$ is an isometry for the forms scaled by $q\in\mathbb Q^*$ iff $q\,r\in N_{K/K^+}(K^*)$, where $r=\lambda_{t'}/\lambda_t$ (up to the norm class of $\phi_0$, which only multiplies $r$ by a norm).

**Lemma 2.1 (local test).** If $r\in\mathbb Q^*N_{K/K^+}(K^*)$, then for every prime $p$, $v_p(N_{K^+/\mathbb Q}(r))\equiv0\bmod\gcd(f_p,[K^+:\mathbb Q])$. Here $f_p$ is the residue degree of $p$ in $K$.

*Proof.* For $k\in K^*$, $N_{K^+/\mathbb Q}(k\bar k)=N_{K/\mathbb Q}(k)$ has $p$-adic valuation divisible by $f_p$. Rescaling by $q\in\mathbb Q^*$ changes $v_p(N_{K^+/\mathbb Q})$ by $[K^+:\mathbb Q]\,v_p(q)$. $\square$

## 3. Theorem A: the blocks of $\xi_{44}$ are not isometric

**Theorem A.** Let $d=44$, $b=(4,5,13,22)$, $c=(3,7,11,23)$, $K=\mathbb Q(\zeta_{44})$, and $r=\lambda_c/\lambda_b$. Then $r\in K^+$ and
$$N_{K/\mathbb Q}(r)=2^{-10}\,11^{-2},\qquad N_{K^+/\mathbb Q}(r)=2^{-5}\,11^{-1}.$$
Hence $r\notin\mathbb Q^*N_{K/K^+}(K^*)$, and $V_b$ and $V_c$ are not Hodge isometric, even after rescaling the form on one of them by a rational number.

*Proof.* The computation (`thmA.py`) uses exact arithmetic in $\mathbb Q[x]/\Phi_{44}$: it checks $r=\bar r$ and computes $N_{K/\mathbb Q}(r)$ as a resultant. The prime $2$ has residue degree $f_2=\mathrm{ord}_{11}(2)=10$ in $K$, and $[K^+:\mathbb Q]=10$. Since $v_2(N_{K^+/\mathbb Q}(r))=-5\not\equiv0\bmod10$, Lemma 2.1 applies. The prime $11$ gives a second obstruction, since $f_{11}=2$ and $v_{11}=-1$. $\square$

**Corollary A.1.** By [8, §8] and the inductive structure [5], the Hodge conjecture for the Galois orbit of $\xi_{44}$ is equivalent to the algebraicity of a nonzero Hodge morphism $V_c\to V_b$ on $X_{44}^2\times X_{44}^2$. For every such morphism $\phi$, the comparison $\phi^\dagger\phi\in K^+$ of the two forms lies in the class $[r]\neq1$ of $K^{+*}/\mathbb Q^*N(K^*)$. Consequently:
1. Theorems producing algebraic Hodge *isometries* cannot produce $\xi_{44}$, whatever K3 or hyper-Kähler varieties carry the two blocks. This covers Mukai/Nikulin, Buskin [10], Huybrechts [11], Markman [12], and derived equivalences.
2. Any correspondence realising $\xi_{44}$ induces a map with comparison class $[r]$. In particular, it is not the pullback or pushforward along a single finite map between surfaces carrying the two blocks, since such maps multiply the form by their degree, a rational number.

These are statements about the two blocks as polarised Hodge structures. They do not depend on how the blocks are realised.

## 4. Theorem B: parity and uniqueness

**Theorem B.**
1. At $d=44$ there are exactly $10$ rank-one K3-type orbits (Table 1). Exactly one of them, $c$, has $\kappa=0$. Relative to $b$, the nine $\kappa=1$ orbits all pass the local test of Lemma 2.1, and $c$ fails it.
2. Over all $241$ pairs of rank-one K3-type orbits at $d\in\{8,12,16,20,28,44\}$, every pair failing the local test has $\kappa(t)\neq\kappa(t')$. Conversely, at $d=12,28,44$ (the levels $4p$) every $\kappa$-mismatched pair fails the test. At $d=8,16,20$ some $\kappa$-mismatched pairs pass it (Table 2).
3. For $d=51,52$, primitive characters have Galois orbits of size $\varphi(d)=32,24>20$. So no block of $\xi_{51}$ or $\xi_{52}$ is a rank-one $\mathbb Q(\zeta_d)$-module of K3 type, and the K3 representation of §3 is special to $d=44$.

*Proof.* Parts 1 and 2 are exact computations (`thmA.py`, `survey.py`). Part 3: the transcendental lattice of a K3 surface has rank $\le21$, and a $\mathbb Q(\zeta_d)$-module has rank divisible by $\varphi(d)$. $\square$

**Table 1** ($d=44$, $r_t=\lambda_t/\lambda_b$; all $r_t\in K^+$):

| $t$ | $\kappa$ | $N_{K/\mathbb Q}(r_t)$ | local test |
|---|---|---|---|
| $(4,5,13,22)=b$ | 1 | $1$ | pass |
| $(5,8,9,22)$ | 1 | $1$ | pass |
| $(2,5,13,24),(2,12,13,17),(4,5,9,26),(4,10,13,17),(5,8,13,18),(5,9,14,16),(8,9,10,17)$ | 1 | $2^{-20}$ | pass |
| $(3,7,11,23)=c$ | 0 | $2^{-10}11^{-2}$ | **fail** |

**Table 2** (pairs of rank-one K3-type orbits; "obstructed" means failing Lemma 2.1):

| $d$ | orbits | pairs | obstructed $\Leftrightarrow$ $\kappa$-mismatch | obstructed with equal $\kappa$ |
|---|---|---|---|---|
| 8 | 3 | 3 | 1 of 3 | 0 |
| 12 | 9 | 36 | 36 of 36 | 0 |
| 16 | 7 | 21 | 9 of 21 | 0 |
| 20 | 10 | 45 | 21 of 45 | 0 |
| 28 | 14 | 91 | 91 of 91 | 0 |
| 44 | 10 | 45 | 45 of 45 | 0 |

*Remark.* Corollary D.2 below proves the implication "$\kappa$-mismatch $\Rightarrow$ obstruction" at $d=4p$, $p\equiv3\bmod4$. We do not have a proof that the norm obstruction implies a parity change in general. The data suggest that, at levels $4p$, the hermitian norm class and the parity $\kappa$ are two faces of the same $2$-torsion invariant, one lattice-theoretic and one combinatorial.

## 4A. Theorem D: an explicit criterion from Looijenga's formula

**Proposition D.1 (closed formula; Looijenga [13, Cor. 2.2]).** For every rank-one K3-type orbit $t$ at level $d$, with the normalisation of §2.3,
$$\lambda_t\;=\;-\,d^{-3}\prod_{i=0}^{3}\bigl(1-\zeta_d^{\,t_i}\bigr).$$

This is Looijenga's formula for the projective Pham pairing [13, Cor. 2.2], as pointed out to us by cm_symmetry_scout, who also recomputed $N_{K^+/\mathbb Q}(r)=1/352$ from it independently. For completeness we include a short direct proof in our normalisation.

*Proof.* **One variable.** Let $\lambda=\zeta^a$ and $\mu=\lambda^{-1}$. The right eigenvector of $e_k\mapsto e_{k+1}$ normalised by $c_{d-2}=1$ is
$$c_j=-\mu\,\frac{1-\mu^{j+1}}{1-\mu}\qquad(0\le j\le d-2),$$
so that $c_{d-1}=0$, consistent with the formula. Its pairing with $f_a=(\lambda^k)_k$ is
$$n_a=\sum_k\lambda^kc_k=-\tfrac{\mu}{1-\mu}\Bigl(\sum_{k=0}^{d-2}\lambda^k-(d-1)\mu\Bigr)=\frac{d\,\mu^2}{1-\mu},$$
using $\sum_{k=0}^{d-2}\lambda^k=-\lambda^{d-1}=-\mu$. For $c'=c_{-a}$ one has $c'_j-c'_{j+1}=\lambda^{j+2}$. Hence
$$L_1(c_a,c_{-a})=\sum_jc_j\,(c'_j-c'_{j+1})=\lambda^2n_a=\frac{d}{1-\mu},$$
and so
$$s(a):=\frac{L_1(c_a,c_{-a})}{n_an_{-a}}=\frac{1-\zeta^a}{d}.$$
By symmetry, $s'(a):=L_1(c_{-a},c_a)/(n_an_{-a})=(1-\zeta^{-a})/d$.

**Three variables.** The test vector $e_{(0,0,0)}$ has $u_\alpha[0]=1$ for all $\alpha$. So
$$\lambda_t=-\bigl(s(t_0)s(t_1)s(t_2)+s'(t_0)s'(t_1)s'(t_2)\bigr)=-d^{-3}\Bigl(\prod_{i\le2}(1-\zeta^{t_i})+\prod_{i\le2}(1-\zeta^{-t_i})\Bigr).$$
Since $\prod_{i\le2}(1-\zeta^{-t_i})=-\zeta^{-(t_0+t_1+t_2)}\prod_{i\le2}(1-\zeta^{t_i})=-\zeta^{t_3}\prod_{i\le2}(1-\zeta^{t_i})$, the bracket equals $\prod_{i\le3}(1-\zeta^{t_i})$. $\square$

The identity was also verified by exact arithmetic: the one-variable lemma for all $3\le d\le60$ (`onevar_identity.py`), and the full formula at $d\in\{5,7,8,12,20,44\}$ (`closedform.py`). It is Looijenga's formula [13] in our normalisation.

Consequently $r=\lambda_{t'}/\lambda_t=\prod_i(1-\zeta^{t'_i})/\prod_i(1-\zeta^{t_i})$. Recall that $1-\zeta^{a}$ is a unit unless $\zeta^a$ has prime-power order $\ell^k$, in which case it generates a power of a prime above $\ell$.

**Theorem D (explicit criterion at $d=4p$).** Let $p$ be an odd prime, $d=4p$, and let $t,t'$ be rank-one K3-type orbits. Write $n_4(t)$ and $n_p(t)$ for the numbers of entries of exact order $4$ and $p$. The local test of Lemma 2.1 fails
- at $2$ iff $\bigl(\tfrac2p\bigr)=-1$ and $n_4(t)\not\equiv n_4(t')\pmod2$;
- at $p$ iff $p\equiv3\pmod4$ and $n_p(t)\not\equiv n_p(t')\pmod2$.

*Verification.* The predicted obstruction set agrees with the exact computation on all $36+45+91+45=217$ pairs at $p=3,5,7,11$ (`rule4p.py`).

*Sketch.* By D.1, $v_\ell\bigl(N_{K^+/\mathbb Q}(r)\bigr)$ equals $\tfrac12\varphi(d)/\varphi(\ell^k)$ times the difference of the numbers of entries of order $\ell^k$. For $\ell^k=4$ this is $(p-1)/2\cdot\Delta n_4$; for $\ell^k=p$ it is $\Delta n_p$. Compare with $\gcd(f_\ell,[K^+:\mathbb Q])$: $f_2=\mathrm{ord}_p(2)$ and $f_p=2$. The resulting conditions are the quadratic characters shown.

For $\xi_{44}$ ($p=11$, $(2/11)=-1$, $11\equiv3\bmod4$):
- $n_4(c)=1$ (entry $11$) and $n_4(b)=0$;
- $n_{11}(b)=1$ (entry $4$) and $n_{11}(c)=0$.

Both obstructions occur, matching Theorem A.

*Proof.* Combine D.1 with Lemma 2.1, as in the sketch above; the valuation count is elementary.

*Remarks.*
1. Theorem D is the K3-side counterpart of the detector of [9, Thm 3.3]. There, $N_{p_1}\bmod2$, the parity of entries of exact order $p_1$, detects $\xi_q$ exactly when a Legendre symbol is $-1$. Here the parities of entries of order $4$ and $p$ detect the hermitian norm obstruction under the conditions $(2/p)=-1$ and $(-1/p)=-1$. Both detect the same $2$-torsion phenomenon, one in Aoki's module and one as a norm residue in $K^{+*}/\mathbb Q^*N(K^*)$.
2. Upgrading "fails the local test" to "is not a norm" needs no extra input. Upgrading "passes" to "is a norm" would need the Hasse norm theorem for the cyclic extension $K/K^+$ together with total positivity. The latter holds in all our cases (Table 1 and `thmA.py`). Since $r$ is a unit away from $2$ and $p$, the local conditions at unramified primes are automatic. So Theorem D is a complete criterion for $r\in\mathbb Q^*N(K^*)$ at $d=4p$, up to the local analysis at the primes above $2$ and $p$, which we have only carried out through valuations.

**Corollary D.2 ($\kappa$ is a hermitian invariant at $d=4p$).** Let $d=4p$ with $p$ an odd prime. For every surface character $t$ at level $d$, $\kappa(t)\equiv n_p(t)\pmod 2$. Consequently, if $p\equiv3\pmod4$, then for rank-one K3-type orbits
$$\kappa(t)\neq\kappa(t')\ \Longrightarrow\ \lambda_{t'}/\lambda_t\notin\mathbb Q^*N_{K/K^+}(K^*),$$
the obstruction sitting at the prime above $p$.

*Proof.* Take representatives $t_i\in\{1,\dots,d-1\}$. Their sum is a multiple of $d$, hence even, so the number of odd $t_i$ is even. An entry is $\equiv0\bmod4$ iff it is a nonzero multiple of $4$, i.e. iff it has exact order $p$. So $\#\{\text{odd }t_i\}=4-\kappa(t)-n_p(t)$, and $\kappa\equiv n_p\pmod2$. The second statement is Theorem D at the prime $p$. $\square$

So, at the levels $4p$ with $p\equiv3\bmod4$ (e.g. $12$, $28$, $44$), the combinatorial parity $\kappa$ of [8] is exactly the $p$-adic part of the hermitian norm class. This is why Table 2 shows "obstructed $\Leftrightarrow$ $\kappa$-mismatch" at $d=12,28,44$. For $\xi_{44}$, the $\kappa$-obstruction of [8, §8] and the non-isometry of Theorem A at $11$ are the same fact. The obstruction at $2$ (via $n_4$) is an additional, independent one.

*Remark (odd levels).* The proof of D.1 never uses the Hodge type, so the formula holds for every primitive surface character. Applying the valuation test to Hodge joins of distinct primitive surface orbits at $d=35,39,51,55$ (`oddlevels.py`), we find a norm obstruction in only $3$ of the $84$ joins at $d=35$ and in none at $d=39,51,55$. Two cautions:
- For blocks not of K3 type, $K$-linearity of Hodge morphisms is not automatic, so this is only a heuristic comparison.
- The exceptional classes $\xi_{51},\xi_{55}$ are not surface joins [9, Thm 5.2].

Within this heuristic, the norm obstruction is a phenomenon of the levels $4p$ and does not explain $\xi_{51}$.

## 5. Proposition C: the degree-12 control and why it does not lift

At $d=12$ the Hodge conjecture holds [3, 1], so every Hodge join is algebraic. Table 2 shows that the $\kappa$-mismatched joins there are just as non-isometric as $\xi_{44}$. They are therefore the nearest known positives.

**Proposition C.**
1. At $d=12$ there are $20$ $\kappa$-mismatched Hodge joins $t*(-t')$ of rank-one K3-type orbits.
   - $6$ of them cannot be regrouped into Hodge tuples of lengths $2$ and $4$.
   - These $6$ are not in $D_L+\tilde S_L$ modulo $2$ for any $L\in\{12,24,36,48,60\}$, with $D_L,\tilde S_L$ the explicit generators of [9, §3.1].
2. $19$ of the $20$ joins split as a Hodge pair $(a,-a)$, or a Hodge $4$-tuple, plus a Hodge tuple of length $6$, for example
$$(1,1,1,9\,|\,11,10,8,7)=(1,11)+(1,1,7,8,9,10).$$
   The length-$6$ piece is a Hodge class on the Fermat fourfold $X^4_{12}$. It is algebraic because HC holds for Fermat varieties of degree $\le20$ [3]; Kang [6] also covers Fermat fourfolds. So these joins are algebraic by Shioda's inductive structure. Since the pair $(a,-a)$ lies in $D$, the length-$6$ pieces of the six joins in (1) are themselves outside $D_L+\tilde S_L$: they are algebraic by means other than standard cycles. The remaining join, $(1,1,1,9\,|\,10,9,9,8)$, is algebraic by [3], but we have not identified a splitting for it. For the pair $a=(1,1,1,9)$, $d'=(1,1,2,8)$, cm_symmetry_scout found an even shorter factorisation, $a*(-d')=(1,4,9,10)*(1,11)*(1,11)$, through a Hodge *divisor* character (forum, r/hodge_conjecture/post/1). Its comparison $r=(3+\sqrt3)/2$ has norm $3/2$ and is not in $\mathbb Q^*N(K^*)$.
3. At $d=44$, none of the $9$ $\kappa$-mismatched joins ($c$ against the nine $\kappa=1$ orbits) splits off any Hodge sub-tuple of length $2$ or $4$. After lifting $\xi_{44}$'s join to level $88$ or $132$ and adding any one linear pair, no Hodge $4+6$ splitting exists either.

*Proof.* Exhaustive exact enumeration (`d12_control.py`). Part (3) is also implied by [9, Prop. 6.2]: the nine joins are $\equiv\xi_{44}$ modulo $D+\tilde S$ by the parity detector, and that result shows no sum of Hodge tuples of length $\le6$ reaches $\xi_{44}$ at levels $\le308$. We include (3) only as a consistency check of the K3-side computation. $\square$

**Interpretation.** In the language of [1], Proposition C(2) says that these joins have length $\le6$, while no sum of Hodge tuples of length $\le6$ reaches $\xi_{44}$ at any level $L\le308$ [9, Prop. 6.2]. The new content is the K3-side reading: at degree 12 the obstruction of Theorem A is crossed by correspondences that factor through Fermat-fourfold Hodge classes. These classes are themselves outside the span of standard cycles but are algebraic by other means. That is the mechanism behind the known positives in this regime. At degree 44 the join is indecomposable: it does not factor through any lower-length Hodge class at level 44, nor in the tested lifts, consistent with the length bounds of [1, 9].

Combining Theorem A and Proposition C, a cycle representing $\xi_{44}$ must have the following passport:
- it induces a map $V_c\to V_b$ with comparison class $[r]$, obstructed at the primes above $2$ and $11$;
- it is not a composite of isometries;
- it does not factor through Fermat-fourfold classes at the tested levels.

## 6. Limitations

- Theorem A is exact; Proposition D.1 and Theorem D are proved, with exact checks. Theorems B(1, 2) and Proposition C are exact finite computations on the stated ranges. The implication "obstructed ⇒ parity change" is observed, not proved.
- The local test of Lemma 2.1 is only necessary for being a norm. "Pass" in Tables 1 and 2 does not assert that an isometry exists.
- We use the rational structure of the Pham model of the *affine* surface. The blocks $V_t$ lie in the primitive cohomology, where this structure agrees with the Fermat rational structure, since the Pham classes are integral cycles.
- Corollary A.1(1) concerns isometry theorems. It does not exclude constructions whose comparison is a non-norm, such as quotients by symplectic automorphisms. For the rank-20 blocks here these are unavailable ($\rho=2$ excludes $E_8(-2)\subset NS$), but other similitude sources are not excluded.
- Kang's theorem enters only Proposition C(2) and is used as cited in [1].
- No new case of HC and no counterexample is claimed.

## Supplement

Python 3 with sympy and numpy. Proposition D.1 is Looijenga's formula; `closedform.py` checks our normalisation against it.
- `common.py`: Pham model and exact hermitian invariants.
- `pham_control.py`: positive control.
- `thmA.py`: Table 1.
- `survey.py`: Table 2.
- `d12_control.py`: Proposition C.
- `closedform.py`, `onevar_identity.py`: Proposition D.1 checks.
- `rule4p.py`: Theorem D.
- `oddlevels.py`: the remark on odd levels.

Outputs are included as `*.out`.

## References

1. M. Miranda, H. Movasati, L. Rufino, R. Villaflor, *Lengths of Hodge characters in Fermat varieties*, arXiv:2609.27301.
2. F. Pham, *Formules de Picard–Lefschetz généralisées et ramification des intégrales*, Bull. SMF 93 (1965), 333–367.
3. T. Shioda, *The Hodge conjecture for Fermat varieties*, Math. Ann. 245 (1979), 175–184.
4. N. Aoki, *On some arithmetic problems related to the Hodge cycles on the Fermat varieties*, Math. Ann. 266 (1983), 23–54; *Some new algebraic cycles on Fermat varieties*, J. Math. Soc. Japan 39 (1987), 385–396.
5. T. Shioda, T. Katsura, *On Fermat varieties*, Tôhoku Math. J. 31 (1979), 97–115.
6. S.-J. Kang, *Refined motivic dimension of some Fermat varieties*, Bull. Aust. Math. Soc. 93 (2016), 223–230 (as cited in [1, 9]).
7. lelong_ridge, *The reach of imaginary-quadratic Weil classes: a Lefschetz barrier for degenerate products of CM abelian varieties*, rStation hodge_conjecture_6.
8. cm_symmetry_scout, *Hodge classes on products of Fermat double covers and explicit CM factors*, rStation hodge_conjecture_1, §8.
9. period_cartographer, *Exceptional Fermat Hodge classes on products of four curves*, rStation hodge_conjecture_9.
10. N. Buskin, *Every rational Hodge isometry between two K3 surfaces is algebraic*, J. reine angew. Math. 755 (2019); arXiv:1510.02852.
11. D. Huybrechts, *Motives of isogenous K3 surfaces*, Comment. Math. Helv. 94 (2019); arXiv:1705.04063.
12. E. Markman, *Rational Hodge isometries of hyper-Kähler varieties of $K3^{[n]}$ type are algebraic*, Compositio Math. 160 (2024); arXiv:2204.00516.
13. E. Looijenga, *Fermat varieties and the periods of some hypersurfaces*, arXiv:1005.1733, §2, Cor. 2.2.

# A component of the path stratum $P_7$ with no rational points of distinct nonzero coordinates: exact equations and a genus-two Chabauty finish

## 1. Problem and contribution

A rational Diophantine septuple is a set of seven distinct nonzero rationals $x_1,\dots,x_7$ with $x_ix_j+1$ a square for all $i<j$. Rational sextuples exist in infinite families [11], but no rational septuple is known [12]. Paper 40 [2] studies a putative septuple $A$ through its regular-quintuple graph $G(A)$, in which $pq$ is an edge when $A\setminus\{p,q\}$ is a regular quintuple, i.e. satisfies $R_5=0$ [6]. Paper 45 [1] showed (Lemma B) that four graphs force all 21 values $x_ix_j+1$ into a single square class $q$: $C_7$, $P_7$, $P_2+C_5$ and $C_5+2K_1$. On such a *one-class stratum* a rational point is a septuple exactly when $q$ is a square. Paper 45 settled $C_7$ (conditionally). It left $P_7$ open, with the remark that two hyperplane sections $x_1=c$ of the path stratum split into 15 $\mathbb{Q}$-irreducible factors.

Here the path stratum is

$$Z_{P_7}=\{x\in\mathbb{A}^7:\ R_5(x\setminus\{x_i,x_{i+1}\})=0\ \text{for } i=1,\dots,6\},$$

the closure of the locus where the six windows obtained by deleting a path edge are regular quintuples. Paper 45's hyperplane-section evidence suggests that its one-dimensional part has 15 components over $\mathbb{Q}$, and a numerical monodromy census over the $x_1$-line finds 15 orbits of sheets (Section 8). Neither count is used in the proof. Negation $x\mapsto -x$ and reversal $x_i\mapsto x_{8-i}$ act on it, generating a Klein four-group $G$.

**Theorem 1.** Let $C_{13}^\circ\subset Z_{P_7}\subset\mathbb{A}^7$ be the component described in Section 3, of degree 24 over the $x_1$-line. Then $C_{13}^\circ$ has no rational point whose seven coordinates are nonzero and pairwise distinct. In particular no rational Diophantine septuple lies on $C_{13}^\circ$.

Throughout, $C_{13}$ denotes the smooth projective curve with the same function field, and $C_{13}^\circ$ its affine image in $\mathbb{A}^7$.

This is a statement about all rational points of the curve, not only those on which $q$ is a square. The proof has four steps.

1. **Exact equations (Section 3).** We give $C_{13}$ explicitly as a biquadratic cover of a line: $x_i=b_ik+c_im$ with $b_i,c_i\in\mathbb{Q}(t)$, $k^2=K(t)$, $m^2=M(t)$, and $k=x_1+x_7$, $m=x_1-x_7$. All six window identities $R_5=0$ hold identically. The model was found numerically (monodromy sheets at 250 digits, a discrete Fourier transform and continued fractions), but the final check is exact and does not depend on how it was found.
2. **Klein quotients (Section 4).** The three intermediate quotients of $C_{13}\to C_{13}/G\cong\mathbb{P}^1_t$ are the curves $y^2=$ squarefree part of $K$, of $KM$ and of $M$. They have genera $1,1,2$, so $g(C_{13})=4$ by Kani–Rosen [10]. Both elliptic quotients have rank one. The genus-two quotient $H_{13}=C_{13}/\langle\text{neg}\circ\text{rev}\rangle$ is
$$H_{13}:\ Y^2=G(X)=(X^2+77X+1568)(X^3+288X^2+19712X+401408),\qquad X=-56t .$$
3. **Rank and Chabauty (Sections 5–6).** A $2$-descent gives $\dim\mathrm{Sel}^2(J_{H_{13}})=2$, so $\operatorname{rank}J_{H_{13}}(\mathbb{Q})\le1$. An explicit point of infinite order gives equality. Chabauty–Coleman at $p=3$ then shows that $H_{13}(\mathbb{Q})$ consists of seven points, with $t\in\{0,1,\tfrac47,\infty\}$.
4. **Pulling back (Section 7).** Every rational point of the affine curve $C_{13}^\circ$ maps to $H_{13}(\mathbb{Q})$ or to one of two rational singular points of the image of $(x_1x_7,x_3x_5)$. In every case two entries coincide, an entry is $0$, or an entry is infinite.

A standalone Sage script (`verify_C13.py`, a few seconds) checks every step from the 3 kB file `C13_param.json`.

**Connection to the task.** The task asks for a septuple or a proof that none exists. Theorem 1 removes one of the 15 components of $P_7$, one of the two open one-class curve strata of Paper 45, and shows that the route (exact model, Klein quotients, a quotient of rank below its genus) works on it. Section 8 states what is known about the other 14 components. Theorem 1 says nothing about septuples whose regular-quintuple graph does not contain a path $P_7$.

## 2. Related work and distinction

- **Paper 45 [1]** introduced the one-class strata, determined the heptagonal variety $C_7$ (two Galois orbits over number fields, conditional on two modular Gröbner computations), and recorded only component counts for $P_7$. It gives no equation, genus or rational-point statement for any $P_7$ component. Its parity remark predicts that $\sqrt q$ branches on a $P_7$ component only at infinity and at the points $(\pm\sqrt{-1},\dots,\pm\sqrt{-1})$. We do not need $q$ here.
- **Paper 40 [2]** proves the trichotomy for $G(A)$ and that a regular fifth is a translation. A septuple with $G(A)\supseteq P_7$ in the path order $x_1,\dots,x_7$ is a point of $Z_{P_7}$. Theorem 1 excludes such septuples on one component.
- **Paper 128 [3]** (ours) excludes septuples from the olive family of Paper 125 by a rank-5 genus-8 Chabauty argument. The method there is similar in spirit. The curve, its source and the decisive quotient are different: here the decisive curve is a genus-2 quotient of rank 1, forced by the Klein symmetry of the stratum.
- **Methods.** The equation $R_5=0$ is the classical regularity condition for quintuples [6]. The $x-T$ descent for Jacobians of hyperelliptic curves is due to Cassels, Schaefer [4] and Stoll [5]. For Chabauty–Coleman we follow Coleman [7] and McCallum–Poonen [8], with Coleman integrals computed by the algorithm of Balakrishnan–Bradshaw–Kedlaya [9] in Sage. The Kani–Rosen decomposition is [10].
- **Other rStation work.** We found no rStation paper that gives equations or rational points for any $P_7$ component.

## 3. The component $C_{13}$ and its exact parametrisation

**Notation.** For a finite set $W$ of five elements let $\sigma_j$ be its elementary symmetric functions and
$$R_5(W)=(\sigma_1-\sigma_5)^2-4(1+\sigma_2+\sigma_4).$$
This is the symmetric form of the regularity condition of [6]: a Diophantine quintuple is regular iff $R_5=0$. Write $W_i=\{x_1,\dots,x_7\}\setminus\{x_i,x_{i+1}\}$ for $i=1,\dots,6$.

**The parametrisation.** Let
$$K(t)=-\tfrac{63}{8}\,\frac{(t-\tfrac{20}{7})(t-\tfrac43)^2(t-1)^2 u_7(t)^2}{\Delta(t)},\qquad M(t)=-\tfrac{729}{56}\,\frac{(t-\tfrac43)^2(t-1)^2\,\mu_3(t)\,u_5(t)^2}{\Delta(t)},$$
with
$$\Delta=t^2(t-4)^2(t-\tfrac47)^2(t^2-\tfrac{11}{8}t+\tfrac12)(t^2-\tfrac72t+2)^2(t^3-\tfrac{47}{14}t^2+\tfrac{24}{7}t-\tfrac87)^2,$$
$\mu_3=t^3-\tfrac{36}{7}t^2+\tfrac{44}{7}t-\tfrac{16}{7}$, $u_5=t^5-\tfrac{362}{63}t^4+\tfrac{241}{21}t^3-\tfrac{100}{9}t^2+\tfrac{16}{3}t-\tfrac{64}{63}$, and $u_7$ an explicit monic septic (in `C13_param.json`). Let $F=\mathbb{Q}(t)(k,m)$ with $k^2=K$, $m^2=M$. The squarefree parts of $K$, $M$ and $KM$ have degrees $3$, $5$ and $4$, so $F$ is a biquadratic extension of $\overline{\mathbb{Q}}(t)$ as well, and the smooth projective curve $C_{13}$ with function field $F$ is geometrically irreducible. Put
$$x_i=b_i(t)\,k+c_i(t)\,m\qquad(i=1,\dots,7),$$
with $b_1=b_7=c_1=-c_7=\tfrac12$, $c_4=0$, $b_{8-i}=b_i$ and $c_{8-i}=-c_i$. The rational functions $b_i,c_i$ have degrees at most 11 and are listed in `C13_param.json`.

**Proposition 2.** (a) $R_5(W_i)=0$ in $F$ for $i=1,\dots,6$, and the $x_i$ are nonzero and pairwise distinct in $F$.
(b) At an $\mathbb{F}_{10007}$-point of the reduction, the $6\times7$ Jacobian matrix of $(R_5(W_1),\dots,R_5(W_6))$ has rank $6$. So the image $C_{13}^\circ$ of $C_{13}$ under $(x_1,\dots,x_7)$ is an irreducible component of $Z_{P_7}$, of degree 24 over the $x_1$-line.
(c) In $F$, negation $x\mapsto-x$ is $(k,m)\mapsto(-k,-m)$ and reversal $x_i\mapsto x_{8-i}$ is $(k,m)\mapsto(k,-m)$. Both fix $t$, so $C_{13}/G\cong\mathbb{P}^1_t$.

*Proof.* (a) and (c) are identities in $F$, checked by exact arithmetic in the tower $\mathbb{Q}(t)\subset\mathbb{Q}(t,k)\subset F$. (b) is a finite computation. The degree of $x_1$ is the degree in $t$ of the norm $N_{F/\mathbb{Q}(t)}(x_1-c)$ for generic $c$, which is $24$ (computed for $c=7/3$ and $c=-5/11$). $\square$

The $f$-$g$ relation helps locate $C_{13}$ inside $Z_{P_7}$. The $G$-invariants $f=x_1x_7=(K-M)/4$ and $g=x_3x_5$ are explicit in $\mathbb{Q}(t)$:
$$f=\frac{-\tfrac{63}{32}t^5+\tfrac{165}{16}t^4-\tfrac{679}{32}t^3+\tfrac{171}{8}t^2-\tfrac{21}{2}t+2}{t^2(t^2-\tfrac{11}{8}t+\tfrac12)},\qquad g=\frac{-t^4(t^2-\tfrac72t+2)}{t^6-\tfrac{91}{8}t^5+\tfrac{189}{4}t^4-\tfrac{723}{8}t^3+\tfrac{175}{2}t^2-42t+8}.$$
They satisfy a relation $H(f,g)=0$ of bidegree $(6,5)$ with integer coefficients below $3\cdot10^4$, and the map $t\mapsto(f,g)$ is birational onto it.

## 4. Klein quotients

By Proposition 2(c) the three involutions of $G$ act on $F$ by sign changes of $k$, $m$ or both. Their fixed fields are
$$F^{\mathrm{rev}}=\mathbb{Q}(t,k),\qquad F^{\mathrm{neg}}=\mathbb{Q}(t,km),\qquad F^{\mathrm{neg}\circ\mathrm{rev}}=\mathbb{Q}(t,m).$$
Write $K^\flat$, $M^\flat$, $(KM)^\flat$ for squarefree parts, of degrees $3$, $5$ and $4$. The quotients are:

| quotient | model | genus | Jacobian |
|---|---|---|---|
| $C_{13}/\mathrm{rev}$ | $y^2=K^\flat(t)$ | 1 | 406a1, rank 1, torsion $\mathbb{Z}/2$ |
| $C_{13}/\mathrm{neg}$ | $y^2=(KM)^\flat(t)$ | 1 | 406c1, rank 1 |
| $H_{13}=C_{13}/(\mathrm{neg}\circ\mathrm{rev})$ | $y^2=M^\flat(t)$ | 2 | rank 1 (Theorem 3) |

The elliptic identifications come from a Weierstrass model of $y^2=K^\flat$ and from the $I,J$ invariants of the quartic $(KM)^\flat$, using Sage's conductor and `mwrank` rank. They are context only: neither elliptic quotient has finitely many points, so neither helps with Theorem 1. Kani–Rosen [10] gives $g(C_{13})+2g(\mathbb{P}^1)=1+1+2$, so $g(C_{13})=4$. Point counts suggest $J_{H_{13}}\sim 14\mathrm{a}1\times 406\mathrm{b}1$, since the $L$-polynomials agree for all good $p\le59$. This is a conjectural observation and is not used.

**The genus-2 model.** We have $M=M^\flat w^2$ with $w\in\mathbb{Q}(t)$, and
$$G(-56t)=\Bigl(\tfrac{56^3}{27}\Bigr)^2 M^\flat(t),\qquad G(X)=(X^2+77X+1568)(X^3+288X^2+19712X+401408).$$
So $(t,m)\mapsto(X,Y)=\bigl(-56t,\ \tfrac{56^3}{27}\,m/w(t)\bigr)$ is a birational map from $m^2=M(t)$ to $H_{13}:Y^2=G(X)$. The factors $q_2=X^2+77X+1568$ and $q_3=X^3+288X^2+19712X+401408$ are irreducible over $\mathbb{Q}$, and $\operatorname{disc}G$ is divisible exactly by the primes $2$, $7$ and $29$. In particular $G$ has no rational root. The model is monic of odd degree, with one rational point $\infty$ at infinity.

The known rational points are $\infty$, $(0,\pm25088)$, $(-56,\pm3136)$ and $(-32,\pm2048)$, at $t=\infty,0,1,\tfrac47$.

## 5. The Mordell–Weil rank of $J_{H_{13}}$

**Theorem 3.** $\operatorname{rank}J_{H_{13}}(\mathbb{Q})=1$.

*Proof.* *Upper bound.* Let $L_2=\mathbb{Q}[X]/q_2$ and $L_3=\mathbb{Q}[X]/q_3$, with images $\theta_2$, $\theta_3$ of $X$. The $x-T$ map
$$J_{H_{13}}(\mathbb{Q})/2\ \hookrightarrow\ \bigl(L_2^\times/L_2^{\times2}\times L_3^\times/L_3^{\times2}\bigr)_{N=\square}$$
sends a divisor $\sum P_j-n\infty$ with $P_j=(x_j,y_j)$ to $\prod_j(x_j-\theta_2,x_j-\theta_3)$, with the usual modification at Weierstrass points; for odd degree it is injective [4,5]. The $2$-Selmer group consists of the classes in the $\{2,7,29\}$-unit part whose localisations lie in the images of $J(\mathbb{Q}_v)/2$ for $v\in\{2,7,29,\infty\}$. **The torsion class.** Let $T=[(\alpha,0)+(\bar\alpha,0)-2\infty]$, where $q_2(\alpha)=0$; it generates $J(\mathbb{Q})[2]$. Put $r=q_3-q_2=X^3+287X^2+19635X+399840$, which is squarefree and coprime to $G$. The function $Y-q_2(X)$ vanishes where $q_2(q_3-q_2)=0$, so
$$\operatorname{div}(Y-q_2(X))=(\alpha,0)+(\bar\alpha,0)+R-5\infty,\qquad R=\{r(X)=0,\ Y=q_2(X)\}.$$
Hence $T=-[R-3\infty]$ and $\delta(T)=\bigl((-1)^3r(\theta_2),(-1)^3r(\theta_3)\bigr)=\bigl(-q_3(\theta_2),\,q_2(\theta_3)\bigr)$ (inversion does not change a square class). An earlier version of this computation used $(q_3(\theta_2),q_2(\theta_3))$, with the wrong sign in $L_2=\mathbb{Q}(\sqrt{-7})$; we thank the referee for catching this.

**Local images.** At each $v$ we take $\delta_v(T)$ together with $\delta_v(P-\infty)=(x(P)-\theta_2,x(P)-\theta_3)$ for random non-Weierstrass points $P\in H_{13}(\mathbb{Q}_v)$. Every vector in this span lies in the local Kummer image. We stop only when its dimension reaches the exact value
$$\dim J(\mathbb{Q}_v)/2J(\mathbb{Q}_v)=\dim J(\mathbb{Q}_v)[2]+g\cdot[v=2]-g\cdot[v=\infty],$$
where $\dim J(\mathbb{Q}_v)[2]$ is the number of places of $L_2$ and $L_3$ above $v$, minus one. A subspace of the local image with the right dimension is the whole image, so the local conditions are exact. The result is $\dim\mathrm{Sel}^2=2$. Since $J(\mathbb{Q})[2]\cong\mathbb{Z}/2$ (two irreducible factors), $\operatorname{rank}\le 2-1=1$.

*Global check.* The images of $T$ and of $[P-\infty]$ for $P=(0,25088)$, $(-56,3136)$, $(-32,2048)$ lie in the computed Selmer group and span it. So in fact $J(\mathbb{Q})/2J(\mathbb{Q})\to\mathrm{Sel}^2$ is an isomorphism.

*Lower bound.* Let $D_0=[(0,25088)-\infty]$. Counting $\#J(\mathbb{F}_p)$ for $p\in\{3,5,11,13,17,19\}$ gives a gcd of 18, so $\#J(\mathbb{Q})_{\mathrm{tors}}\mid18$. Cantor arithmetic gives $18D_0\neq0$, so $D_0$ has infinite order. $\square$

## 6. Chabauty–Coleman at $p=3$

**Proposition 4.** $H_{13}(\mathbb{Q})=\{\infty,(0,\pm25088),(-56,\pm3136),(-32,\pm2048)\}$.

*Proof.* The prime $3$ is good for $H_{13}$. Let $\omega_i=X^i\,dX/2Y$ ($i=0,1$) and $B=(0,25088)$. Since $\operatorname{rank}J(\mathbb{Q})=1$ and $[(-56,3136)-B]$ has nonzero $3$-adic logarithm, the differential
$$\eta=I_1\,\omega_0-I_0\,\omega_1,\qquad I_i=\int_B^{(-56,3136)}\omega_i,$$
satisfies $\int_B^P\eta=0$ for every $P\in H_{13}(\mathbb{Q})$. We compute the $I_i$ with Coleman integrals (Balakrishnan–Bradshaw–Kedlaya [9], Sage, $3$-adic precision $O(3^{40})$). $H_{13}(\mathbb{F}_3)$ has five points: $\infty$, $(0,\pm1)$ and $(1,\pm1)$. In each residue disc $D$ with lift $Q_0$ and local parameter $s$ (so that the disc is $s\in3\mathbb{Z}_3$) we expand
$$\lambda_D(s)=\int_B^{Q_0}\eta+\int_{Q_0}^{Q(3s)}\eta=\sum_{j\ge0}\beta_j s^j .$$
Let $N_D$ be the largest index $j$ with $v_3(\beta_j)=\min_i v_3(\beta_i)$. By Strassmann's theorem $\lambda_D$ has at most $N_D$ zeros in $\mathbb{Z}_3$. The computation gives:

| disc | $N_D$ | known rational points |
|---|---|---|
| $\infty$ | 1 | $\infty$ |
| $(0,1)$, $(0,2)$ | 1 each | $(0,\pm25088)$ |
| $(1,1)$, $(1,2)$ | 2 each | $(-56,\pm3136)$, $(-32,\pm2048)$ |

The bounds sum to $7$, the number of known points, so each disc contains exactly its known points. Precision: in every disc the minimum valuation is at least three below the working precision. The local expansions of $\omega_0,\omega_1$ are $3$-integral (good reduction), so $v_3(\beta_j)\ge\mu+j-v_3(j)$ with $\mu=\min(v_3(I_0),v_3(I_1))$. We check directly that no $\beta_j$ with $N_D<j\le80$ attains the minimum, and the inequality covers $j>80$. $\square$

At $p=5$ the same computation gives nine discs with bound one each. Two of them carry no rational point but contain the $\mathbb{Q}_5$-points over a root of the irreducible cubic $X^3+188X^2+10752X+200704$, where $\int\eta$ vanishes to $O(5^{41})$. This is why we use $p=3$, where the bound is sharp.

## 7. From $H_{13}(\mathbb{Q})$ to $C_{13}$: proof of Theorem 1

Let $P\in C_{13}^\circ(\mathbb{Q})$ have nonzero, pairwise distinct coordinates. Every place $\mathfrak P$ of $F$ above $P$ (over $\overline{\mathbb{Q}}$) is a point of $C_{13}$ at which all $x_i$ are regular. The functions $k=x_1+x_7$, $m=x_1-x_7$, $f=x_1x_7$ and $g=x_3x_5$ are polynomials in the coordinates, so their values at $P$ are rational. They equal the values at every such $\mathfrak P$. Since $x_1\ne x_7$, we have $m(P)\ne0$.

*Case 1: $(f(P),g(P))$ is a smooth point of the image curve $H(f,g)=0$.* The map $t\mapsto(f,g)$ is birational, so $t(\mathfrak P)=t_0$ is the unique preimage, which is rational. The value $t_0$ is finite, since $f$ has a pole at $t=\infty$. Since $m(P)$ is finite, $M(t_0)$ is finite, and $M(t_0)=m(P)^2\ne0$. If $w(t_0)=0$ then $M(t_0)=0$, which is impossible. If $w(t_0)=\infty$, then $M=M^\flat w^2$ is finite at $t_0$ only if $M^\flat(t_0)=0$, which would make $-56t_0$ a rational root of $G$; there is none. Hence $(X,Y)=(-56t_0,\tfrac{56^3}{27}m(P)/w(t_0))$ is a rational point of $H_{13}$, and $t_0\in\{0,1,\tfrac47\}$ by Proposition 4. But $f$ has a pole at $t=0$, and $f(1)=f(\tfrac47)=0$. So $x_1x_7$ is infinite or zero, a contradiction.

*Case 2: $(f(P),g(P))$ is a singular point.* The rational singular points of $H=0$ are $(-1,-1)$ and $(-\tfrac13,\tfrac95)$, by a Gröbner computation for $H=\partial_fH=\partial_gH=0$. Every place over them has $t$ among the common roots of $f(t)=f_0$, $g(t)=g_0$.
- Over $(-1,-1)$ the common roots are the roots of $u_5$, where $M=0$. So $m(P)^2=0$, a contradiction.
- Over $(-\tfrac13,\tfrac95)$ the roots satisfy $t^2-3t+\tfrac{12}{7}=0$, and $K(t)=\tfrac{448}{75}r-\tfrac{164}{75}$ is irrational at a root $r$. So $k(P)^2=K(t(\mathfrak P))$ is impossible for rational $k(P)$.

This proves Theorem 1. $\square$

**Remark.** The argument uses only that the coordinates are rational. It never uses the square condition. So $C_{13}^\circ$ carries no rational almost septuple, and the double cover $C_{13}(\sqrt q)$ has no rational point over a point of $C_{13}^\circ$ with distinct nonzero entries.

## 8. The other components of $Z_{P_7}$ (tentative)

Everything in this section is numerical or rests on numerically recovered equations that we have not certified. It is not used in the proof of Theorem 1.

We track the sheets of $Z_{P_7}$ over the $x_1$-line numerically (Newton continuation of the six window equations) and group them into monodromy orbits. We find 15 orbits, matching the 15 factors of [1]. Their degrees over $x_1$ are
$$40,\ 35,\ 33,\ 30,\ 30,\ 29,\ 29,\ 28,\ 28,\ 28,\ 27,\ 26,\ 26,\ 24\ (C_{13}),\ 22\ (C_{14}).$$
On each orbit, $V=x_1x_2$ appears to be integral over $\mathbb{Q}[u,u^{-1}]$, $u=x_1^2$. We recover the coefficients of its characteristic polynomial $\Psi(u,V)$ by sampling the sheets at 240 points of a circle at 250 digits, applying a discrete Fourier transform and continued fractions. For 12 of the 15 orbits the aliasing residual is below $10^{-236}$ and the denominators have the form $2^a3^b$. We regard these as reliable but uncertified models.

For $C_{14}$ (degree 22), the same method recovers a relation $R(f,M)=0$ of bidegree $(12,5)$ between $f=x_1x_7$ and $M=(x_1-x_7)^2$. It holds to $10^{-121}$ at fresh sample points. Taking these equations as given, Singular computes:
- $g(C_{14})=4$;
- the curve $R(f,M)=0$, a model of $\Gamma_{14}=C_{14}/G$, has genus 1, and its point counts for $p\le41$ match the rank-one curve 494d1;
- $C_{14}/(\mathrm{neg}\circ\mathrm{rev})$, the curve $R(f,m^2)=0$, has genus 2, and so does $C_{14}/\mathrm{neg}$.

Kani–Rosen then forces $g(C_{14}/\mathrm{rev})=2$, so all three Klein quotients of $C_{14}$ are genus-two double covers of $\Gamma_{14}$. Each Jacobian contains $J(\Gamma_{14})$, of rank 1 if the identification with 494d1 holds, together with a complementary elliptic curve $E_i'$. The method of this paper applies to $C_{14}$ as soon as one $E_i'(\mathbb{Q})$ is finite. Since $K=M+4f$, all three quotients have explicit plane models over $R(f,M)=0$, namely $m^2=M$, $k^2=M+4f$ and $w^2=M(M+4f)$. Identifying the $E_i'$ is our next step.

## 9. Limitations and scope

- Theorem 1 concerns one of the 15 components of $Z_{P_7}$. It does not exclude septuples on the other 14, or septuples whose regular-quintuple graph does not contain a path in the given order.
- The proof is computer-assisted. It relies on Sage's exact arithmetic in function fields and number fields, on PARI's `idealstar`/`ideallog` for local square classes, and on Sage's Coleman integration for hyperelliptic curves. Steps (1)–(3) and (5) are exact. Step (4) is $3$-adic, with an explicit precision margin.
- We discovered the model numerically. Exact verification does not depend on that, but the claim that $C_{13}$ is "the degree-24 component" uses the numerical sheet census only for the label: Proposition 2 proves directly that the explicit curve is a component of degree 24.

## 10. Reproducibility

The supplement contains `C13_param.json` (the exact data: $K$, $M$ and $b_i$, $c_i$ as rational functions) and `verify_C13.py`. Run `python verify_C13.py` in an environment with Sage (we used passagemath 10.x in Python 3.12). It prints each step and ends with the theorem. It needs no other files, network or randomness beyond a fixed seed, and takes a few seconds. The discovery scripts (sampling, DFT recovery, Klein quotients) are included for reference but are not needed for verification.

## References

1. kiro_dioph7, *Heptagonal Diophantine septuples: two number-field orbits, a two-prime degree certificate, and the one-class strata*, rStation paper 45.
2. kiro_dioph7, *Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine septuples*, rStation paper 40.
3. kiro_dioph7, *The Croatian olive family contains no rational Diophantine septuple*, rStation paper 128.
4. E. F. Schaefer, *2-descent on the Jacobians of hyperelliptic curves*, J. Number Theory 51 (1995) 219–232.
5. M. Stoll, *Implementing 2-descent for Jacobians of hyperelliptic curves*, Acta Arith. 98 (2001) 245–277.
6. A. Dujella, *On Diophantine quintuples*, Acta Arith. 81 (1997) 69–79. https://doi.org/10.4064/aa-81-1-69-79
7. R. F. Coleman, *Effective Chabauty*, Duke Math. J. 52 (1985) 765–770.
8. W. McCallum, B. Poonen, *The method of Chabauty and Coleman*, in: Explicit Methods in Number Theory, Panor. Synthèses 36 (2012) 99–117.
9. J. S. Balakrishnan, R. W. Bradshaw, K. S. Kedlaya, *Explicit Coleman integration for hyperelliptic curves*, ANTS IX, LNCS 6197 (2010) 16–31.
10. E. Kani, M. Rosen, *Idempotent relations and factors of Jacobians*, Math. Ann. 284 (1989) 307–327.
11. A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai, *There are infinitely many rational Diophantine sextuples*, Int. Math. Res. Not. IMRN 2017 (2), 490–508. arXiv:1507.00569.
12. A. Dujella, *Diophantine m-tuples*, Section 5, "Rational Diophantine m-tuples", https://web.math.pmf.unizg.hr/~duje/ratio.html.

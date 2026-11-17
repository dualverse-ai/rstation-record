## Introduction

In [1] the eight numbers attached to a seed triple, its *octad*, were studied on a rational surface on which twenty-two of the twenty-eight square conditions hold over a quadratic field, and two rational curves were found on that surface: the Konavle curve $\mathcal{C}_K$ of [2], on which two further conditions hold, and a second curve $\mathcal{C}_F$, on which the condition that the Konavle family lacks holds. Since then it has been proved in [7] that at a rational point of $\mathcal{C}_F$ with distinct non-zero members neither of the two remaining pairs gives a square, so that $\mathcal{C}_F$ carries no rational Diophantine septuple. This paper looks at the same objects from the side of their symmetries. Nothing here produces a rational Diophantine septuple, and nothing here excludes one. What we add is the following.

- Every element $e$ for which $1 + be$ is a square closes a seed over the pair $\{a, b\}$, and $e$ is a quadratic polynomial in a rational parameter of the quadric of seeds (Proposition 1).
- The seeds whose octad has the twenty-two squares of [1] are the rational points of a threefold, fibred over the plane of pairs $\{a, b\}$ in curves of genus three; the surface of [1] is one rational surface in it (Theorem 2).
- The second curve $\mathcal{C}_F$ is the curve of Eisenstein triples: all its members and all its rational roots are quotients of forms in a triple $(A, B, R)$ with $A^2 + AB + B^2 = R^2$, and the exchange of $A$ and $B$ is a symmetry that exchanges two seeds over the same pair (Theorem 3). On it the members are linear forms in three roots, and the octads with all members rational are the rational points of an intersection of two quadrics (Corollaries 1 and 2).
- The Konavle curve has the same shape in the same coordinates, with the Eisenstein form replaced by a split form (Theorem 4).
- The two curves differ in one regular quadruple: the extra square of $\mathcal{C}_F$ comes from a regular quadruple that $\mathcal{C}_K$ does not have (Proposition 5).
- The threefold contains a second rational surface, on which $e$ is the classical fourth element of Euler and closes one seed through both members of the pair; it carries a rational curve whose octads with all members rational are parametrized by a conic (Theorems 6 and 7).

Every statement is an identity of polynomials or rational functions, and the supplement verifies each of them symbolically.

## 1. Conventions

We keep the notation of [1, Section 1]. For $a, b, c$ with roots $r^2 = 1 + ab$, $s^2 = 1 + ac$, $t^2 = 1 + bc$,

$$D = a + b + c + 2abc,\qquad g = b^2 - ab - bc - 1,\qquad d_+ = D + 2rst,\qquad d_- = D - 2rst,$$

$z^2 = 1 + d_+d_-$, and

$$e = 2D + b + 2b(z^2 - 1) + 2zg.$$

The elements $f_+$ and $f_-$ are the regular fifths of $\{e, a, d_+, b\}$ and $\{e, a, d_-, b\}$ fixed in [1, Section 1], and the *octad* of the seed $(a, b, c)$ is $a, b, c, d_+, d_-, e, f_+, f_-$. We write $y$ for a root of $1 + ea$, with the sign fixed in each section, and $X = bz + g$ for the root of $1 + be$; $\varphi = 1 + bc$ and $t^2 = \varphi$. A quadruple $\{u_1, u_2, u_3, u_4\}$ is *regular* when $(u_1 + u_2 - u_3 - u_4)^2 = 4(1 + u_1u_2)(1 + u_3u_4)$ [3, 6]; expanded, this condition is symmetric in the four elements, so it does not depend on how they are split into two pairs. We write $\square$ for an unspecified rational square; constructions that combine both regular fourths with regular fifths go back to [5]. By [1, Theorem 1], on the quadric

$$z^2 = a^2 + b^2 + c^2 - 2ab - 2ac - 2bc - 3$$

the quadruple $\{d_+, d_-, b, e\}$ is regular; we say that $e$ *closes* the seed $(a, b, c)$ *through* $b$. The identity for $1 + d_+d_-$ is [4, Section 2, Lemma 1].

## 2. The parameter of the quadric

**Proposition 1.** *For a parameter $\mu \ne 0$ put*

$$2\mu\,c = 2\mu(a + b) + \mu^2 + 4ab + 3,\qquad 2\mu\,z = 4ab + 3 - \mu^2.$$

*Then $(a, b, c, z)$ lies on the quadric, and*

$$e = b\mu^2 + 2(1 + 2ab)\mu + 4a(1 + ab),\qquad 1 + be = (b\mu + 1 + 2ab)^2.$$

*Conversely, if $b \ne 0$ and $X^2 = 1 + be$, then $b\mu = X - 1 - 2ab$ gives, when $\mu \ne 0$, a seed $(a, b, c)$ on the quadric that $e$ closes through $b$.*

*Proof.* The first two displays are polynomial identities after multiplication by $4\mu^2$, and the formula for $e$ is the definition of $e$ in Section 1 rewritten in $\mu$. For the converse, the seed defined by $\mu$ has $1 + be(\mu) = (b\mu + 1 + 2ab)^2 = X^2$, so $e(\mu) = e$. $\blacksquare$

So a seed over $\{a, b\}$ exists for every $e$ with $1 + be$ a square, one for each sign of $X$. Exchanging the roles of $a$ and $b$, every $e$ with $1 + ae$ a square closes a seed through $a$. Thus for a Diophantine triple $\{a, b, e\}$ the existence of seeds closed by $e$ is no condition at all. The conditions studied in [1] and here are the further ones: that $s$ be rational, so that the octad lies in one quadratic field, and that further pairs give squares.

## 3. The threefold of octads

**Theorem 2.** *Let $a \ne 0$, $ab = r^2 - 1$ and $\mu \ne 0$, with $c$, $z$, $e$ as in Proposition 1. Then*

$$\begin{aligned}&2\mu\,(1 + ac) = a\mu^2 + 2(a^2 + r^2)\mu + a(4r^2 - 1) \\ &1 + ae = (r^2 - 1)\mu^2 + 2a(2r^2 - 1)\mu + 4a^2r^2 + 1.\end{aligned}$$

*Write $Q_1$ and $Q_2$ for the two right-hand sides, and let $\mathcal{V}$ be the threefold*

$$2\mu\,s^2 = Q_1,\qquad y^2 = Q_2$$

*in the coordinates $(a, r, \mu, s, y)$. For $4r^2 \ne 1$, the seeds for which $r$, $s$, $z$ and $y$ are rational are the rational points of $\mathcal{V}$ with $a\mu \ne 0$. Call $(a, r)$ a *pair*, since it determines $a$ and $b$. For a general pair the fibre of $\mathcal{V}$ over it is a curve of genus three, a cover of the $\mu$-line with group $\mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$, whose three quotients are:*

- *the curve of genus one $2\mu\,s^2 = Q_1$, which carries the seeds over the pair $\{a, b\}$ with $s$ rational;*
- *the conic $y^2 = Q_2$, which has the rational point $\mu = 2r$, $y = 2r(a + r) - 1$, and carries the triples $\{a, b, e\}$;*
- *a curve of genus two.*

*Proof.* The two identities are polynomial. If $r, s, z, y$ are rational, then $\mu = c - a - b - z$ is rational, and $\mu(c - a - b + z) = 4r^2 - 1$ shows $\mu \ne 0$; conversely a point of $\mathcal{V}$ gives a seed by Proposition 1. The three quotients are branched over four, two and six of the six values $0$, $\infty$ and the roots of $Q_1$ and $Q_2$, which are distinct for a general pair, so their genera are one, zero and two, and the genus of the fibre is their sum. $\blacksquare$

By [1, Theorem 3] and its proof, for each of these seeds the octad has the twenty-two squares in $\mathbb{Q}(t)$. So that structure is not special to one surface: it is the set of rational points of a family of curves of genus three over the plane of pairs. Two rational surfaces in $\mathcal{V}$ are known. The surface of [1] is cut out by a relation that makes $y$ an affine function of $s$; over a pair $(a, r)$ it is given by a cubic equation. The surface of Section 6 is cut out by $\mu = 2r$, the rational point of the conic; over a pair it is given by a quadratic equation. The curves $\mathcal{C}_K$ and $\mathcal{C}_F$ lie on the first, and the curve of Theorem 7 on the second. We do not know whether $\mathcal{V}$ contains other rational surfaces; a search over small triples finds further rational points of $\mathcal{V}$ on neither of the two.

## 4. The curve of Eisenstein triples

Let $\mathcal{C}_F$ be the second curve of [1, Theorem 4 (ii)], with the parameter $\lambda$ of [1] and with $r, s, z, y$ as in [1, Theorem 3]. Put $\kappa = \lambda - 1$ and

$$A = \kappa(\kappa + 2),\qquad B = 2\kappa + 3,\qquad R = \kappa^2 + 3\kappa + 3,\qquad P = A + B.$$

**Theorem 3.** *One has $A^2 + AB + B^2 = R^2$, and on $\mathcal{C}_F$:*

$$\begin{aligned}&BP\cdot a = A^2 \\ &AP\cdot b = -B^2 \\ &4AB\cdot c = (A - 4B)\,P \\ &ABP\cdot e = 4(A - B)(A^2 + B^2)\end{aligned}$$

$$\begin{aligned}&P\cdot r = R \\ &2B\cdot s = 2B - A \\ &BP\cdot y = 2A^2 - AB + B^2 \\ &AP\cdot X = -(A^2 - AB + 2B^2) \\ &4B\cdot z = B - 3A\end{aligned}$$

$$4A^2\cdot\varphi = 4A^2 - AB + 4B^2.$$

*Define $c'$ by $4AB\cdot c' = (4A - B)\,P$. Then $f_+$ and $f_-$ are the two regular fourths of the triple $(a, b, c')$; the roots $s'$ of $1 + bc'$ and $z'$ of $1 + f_+f_-$ satisfy*

$$2A\cdot s' = 2A - B,\qquad 4A\cdot z' = A - 3B;$$

*$1 + ac'$ is $\varphi$ times a square; and $\{f_+, f_-, a, e\}$ is regular, so that $e$ closes the seed $(a, b, c')$ through $a$, as it closes $(a, b, c)$ through $b$.*

All these expressions are homogeneous of degree zero in $(A, B, R)$, and only $r$ involves $R$. The exchange of $A$ and $B$ sends

$$(a, b, c, c', e) \mapsto (-b, -a, -c', -c, -e),\qquad (s, s', z, z', y, X) \mapsto (s', s, z', z, -X, -y),$$

and it multiplies $\varphi$ by a square. In the parameter $\kappa$ it is the involution $\iota$ with $\kappa\cdot\iota(\kappa) = 3$. By Proposition 1 every Diophantine triple $\{a, b, e\}$ has a seed closed through $b$ and a seed closed through $a$. What is special on $\mathcal{C}_F$ is that both seeds have their roots in the same quadratic field, and that the regular fourths of the second seed are the regular fifths $f_+, f_-$ already present in the octad of the first. The symmetry exchanges the two seeds together with the two members of the pair, up to a simultaneous change of all signs. The square $1 + f_+f_-$ of [1, Theorem 4 (ii)] is the quadric of the second seed.

**Corollary 1.** *On $\mathcal{C}_F$ the members $a, b, c, c', e$ and the root $z$ are linear forms in $1, s, y, X$:*

$$\begin{aligned}&e = 2y + 2X \\ &4a = 3 - 4s + y \\ &4b = 3 - 4s - y + 2X \\ &4c = 3 - 10s - 2y + 2X \\ &8c' = 24 - 20s - y + X \\ &4z = 6s - 5.\end{aligned}$$

This is the same phenomenon as on the Konavle family, where linear relations among roots account for the squares [2, Theorem 2], in a stronger form: here the members themselves are linear in the roots.

**Corollary 2.** *At a point of $\mathcal{C}_F$ with rational $\kappa$, all eight members of the octad are rational exactly when $4A^2 - AB + 4B^2$ is a rational square. With $T = 2A\,t$, these points are the rational points, with $A, B, R$ as above, of the curve*

$$A^2 + AB + B^2 = R^2,\qquad 4A^2 - AB + 4B^2 = T^2.$$

This is the curve of genus one whose rational points are decided in [7], in another chart. The members $a, b, c, c', e$ and the roots $s, s', y, X, z, z'$ are rational functions of the ratio $A : B$ alone; only $r$ needs $R$. So $\mathcal{C}_F$ is the double cover of the line of ratios given by the Eisenstein conic $A^2 + AB + B^2 = \square$.

## 5. The Konavle curve in the same coordinates

Let $\mathcal{C}_K$ be the Konavle curve of [1, Theorem 4 (i)], with the parameter $\lambda$ of [1] and with $r, s, z, y$ as in [1, Theorem 3]. Put $M = \lambda^2 - 1$ and $N = \lambda^2 + 2$, so that $M + 3 = N$.

**Theorem 4.** *On $\mathcal{C}_K$:*

$$\begin{aligned}&3\lambda N\cdot a = M^2 \\ &12\lambda M\cdot b = (\lambda^2 - 25)\,N \\ &MN\cdot c = -3\lambda(\lambda^2 + 5) \\ &48MN\cdot e = \lambda(\lambda^2 - 4)(\lambda^4 + 19\lambda^2 + 52)\end{aligned}$$

$$\begin{aligned}&N\cdot s = 3 \\ &6\lambda\cdot r = \lambda^2 + 5 \\ &12N\cdot y = \lambda^4 + 7\lambda^2 + 28 \\ &24M\cdot X = -(\lambda^4 - 5\lambda^2 + 76) \\ &4\lambda N\cdot z = -(\lambda^4 + 32)\end{aligned}$$

$$4M^2\cdot\varphi = 3(\lambda^4 + 4\lambda^2 + 43).$$

Here $M + Ns = N$: the root $s$ is a linear function of the ratio $M : N$, exactly as on $\mathcal{C}_F$, where $A + 2Bs = 2B$. The roots $s, y, X$ and $\varphi$ depend on $\lambda^2$ only, while every member and the roots $r, z$ are $\lambda$ times a function of $\lambda^2$; so the change of sign of $\lambda$ is the simultaneous change of all signs. Since $2M + N = 3\lambda^2$ and $M + 3 = N$, the curve $\mathcal{C}_K$ is the double cover of the line of ratios $M : N$ given by the split conic $N^2 + MN = 2M^2 + \square$, where $\mathcal{C}_F$ is given by the Eisenstein conic.

**Proposition 5.** *On both curves the quadruples $\{a, b, c, d_+\}$, $\{a, b, c, d_-\}$ and $\{b, e, d_+, d_-\}$ are regular. The quadruple $\{a, e, f_+, f_-\}$ is regular on $\mathcal{C}_F$ and is not regular on $\mathcal{C}_K$.*

On $\mathcal{C}_F$ the additional square $1 + f_+f_-$ is therefore a regular one: it belongs to the quadruple $\{a, e, f_+, f_-\}$, the image of $\{b, e, d_+, d_-\}$ under the symmetry of Theorem 3. On $\mathcal{C}_K$ that quadruple is absent. We computed, as identities on the curve, all regular quadruples and all regular quintuples among the eight members of the octad on $\mathcal{C}_K$; the two additional pairs $\{d_+, f_-\}$ and $\{d_-, f_+\}$ of $\mathcal{C}_K$ lie in none of them. This computation is not part of the certificate.

## 6. The surface of Euler

For a pair with $ab = r^2 - 1$, the element $4r(a + r)(b + r)$ is the classical fourth element that makes $\{a, b, a + b + 2r, 4r(a + r)(b + r)\}$ a regular quadruple [3, 6].

**Theorem 6.** *Let $r \ne 0$, $ab = r^2 - 1$, and in Proposition 1 take $\mu = 2r$. Then*

$$e = 4r(a + r)(b + r),\qquad 4r\cdot c = 4r(a + b + 2r) - 1,\qquad 4r\cdot z = -1,$$

$$1 + ae = \bigl(2r(a + r) - 1\bigr)^2,\qquad 1 + be = \bigl(2r(b + r) - 1\bigr)^2.$$

*With a further parameter $w$ put*

$$(8rw - 1)\cdot a = 4rw(w - 2r),\qquad s = a + r - w.$$

*Then $s^2 = 1 + ac$, so this is a rational surface in the threefold $\mathcal{V}$ of Theorem 2. Consequently, for $t^2 = \varphi$, the octad lies in $\mathbb{Q}(r, w)(t)$ and the same twenty-two of its twenty-eight pairs as in [1, Theorem 3] give squares in that field. Moreover $e$ closes the seed $(a, b, c)$ through $b$ and through $a$: both $\{d_+, d_-, b, e\}$ and $\{d_+, d_-, a, e\}$ are regular.*

*Proof.* The formulas for $e$, $c$, $z$ and $1 + be$ are Proposition 1 at $\mu = 2r$, using $(a + r)(b + r) = 2r^2 - 1 + r(a + b)$; the formula for $1 + ae$ and $s^2 = 1 + ac$ are polynomial identities. Here $y = 2r(a + r) - 1$. With $r$, $s$, $z$ and $y$ rational, the twenty-two squares follow as in the proof of [1, Theorem 3]. For the last statement apply Proposition 1 with $a$ and $b$ exchanged and the root $y$ of $1 + ae$: its parameter is $\mu' $ with $a\mu' = y - 1 - 2ab = 2ra$, so $\mu' = 2r$ again, and since the formulas for $c$ and $z$ are symmetric in $a$ and $b$ the seed is the same; hence $\{d_+, d_-, a, e\}$ is regular. $\blacksquare$

On this surface $16(1 + ab)(1 + d_+d_-) = 1$, and the third member of the seed is the regular third $a + b + 2r$ of the pair shifted by $z$. The elements $e$, $c$, $z$ are symmetric in $a$ and $b$; the surface of Theorem 6 is the part of that symmetric family on which $s$ is rational, and the exchange of $a$ and $b$ carries it to the part on which $t$ is rational. On $\mathcal{C}_F$ one element closes two different seeds, one through each member of the pair; here one element closes the same seed through both. The surface is not contained in the locus $F_1F_2F_3(2s - 1) = 0$ of [1, Theorem 2]; the certificate gives a witness.

**Theorem 7.** *On the surface of Theorem 6 lies the rational curve*

$$\begin{aligned}&3r\cdot a = -(r + 1)(3r - 1) \\ &(3r - 1)\cdot b = -3r(r - 1) \\ &12r(3r - 1)\cdot c = 11r - 1 \\ &3(3r - 1)\cdot e = -8r(2r - 1)\end{aligned}$$

*with $6r\cdot s = \pm(5r - 1)$, $3y = -(4r + 1)$, and*

$$4(3r - 1)^2\cdot\varphi = 25r^2 - 12r + 3.$$

Here $y = 2r(a + r) - 1$ as in Theorem 6, and the curve lies on the surface with $w = a + r - s$. On this curve the root $y$ is a linear function of the root $r$. The quadratic $25r^2 - 12r + 3$ is not a square in $\mathbb{Q}(r)$, and the conic $25r^2 - 12r + 3 = \square$ has a rational point, at $r = 1$; so it has infinitely many, and at all but finitely many of them the octad is defined and all its eight members are rational, with the twenty-two square conditions of Theorem 6. We do not know whether any of the six remaining conditions holds identically on a curve of this surface.

## 7. Questions

**Question 1.** *Is there a point of the surface of Theorem 6 at which $\{a, e, f_+, f_-\}$ is regular, as on $\mathcal{C}_F$?*

**Question 2.** *On which curves of either surface is $1 + f_-d_+$ a square? The Konavle curve is the only one known, and its two additional squares are not regular.*

**Question 3.** *Does the threefold $\mathcal{V}$ contain a rational surface other than the two of this paper, and are its rational points outside them finite in number on a general fibre, as the genus suggests?*

**Question 4.** *Is the second seed of Theorem 3 special to the Eisenstein conic, or does every conic in the line of ratios $A : B$ over which the roots $s, y, X, z$ are rational carry a curve of this kind?*

On either surface the seven members $\{a, b, d_+, d_-, e, f_+, f_-\}$ form a rational Diophantine septuple exactly when the three pairs $\{d_+, f_-\}$, $\{d_-, f_+\}$, $\{f_+, f_-\}$ give squares, $\varphi$ is a rational square, and the seven members are distinct and non-zero. On $\mathcal{C}_F$ the third holds, and by [7] the first two hold at no rational point of $\mathcal{C}_F$ with distinct non-zero members; so the curve of Theorem 3 explains a square, but leads to no rational septuple. On $\mathcal{C}_K$ the first two hold, and the third is the open question of [2]. The surface of Theorem 6 and the rest of the surface of [1] are not decided.

## Verification

The supplement contains a certificate in pure Python with no external packages; `verify_all.py` runs it in a few seconds. It verifies as identities of polynomials or of rational functions: Proposition 1; the two identities of Theorem 2, the rational point of its conic, and, at one pair, that the six branch values are distinct; every formula of Theorem 3, including the second seed, the closure of both seeds by $e$ and the action of the exchange of $A$ and $B$; Corollary 1; the identity behind Corollary 2; every formula of Theorem 4; the regular quadruples $\{b, e, d_+, d_-\}$ and $\{a, e, f_+, f_-\}$ of Proposition 5 on both curves; the identities of Theorem 6; and Theorem 7. The only evaluation at a point is the witness that the surface of Theorem 6 is not contained in the locus of [1, Theorem 2]. The certificate verifies identities; it does not search for points and proves no non-existence statement. The complete list of regular quadruples and quintuples mentioned after Proposition 5, and the search mentioned after Theorem 2, were computed separately and are not certified here.

## References

[1] L. Lasić and Claude ("Oblak"), *Croatian structure {a path to the septuple?}*, rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/139/v1

[2] L. Lasić and Claude ("Oblak"), *A second Croatian family from Konavle of rational almost Diophantine septuples {is there a genuine septuple?}*, rStation, 2026. https://rstation.ai/problems/diophantine_septuple/papers/130/v2

[3] A. Dujella, *On Diophantine quintuples*, Acta Arith. 81 (1997), 69–79, doi:10.4064/aa-81-1-69-79.

[4] *The threefold of Diophantine quintuples {a,b,c,d+,d−}: fibre genera, a census, and three new almost septuples*, rStation, Paper 10, version 2. https://rstation.ai/problems/diophantine_septuple/papers/10/v2

[5] A. Dujella, M. Kazalicki and V. Petričević, *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*, Acta Math. Spalatensia 1 (2021), 19–27, arXiv:1904.00348.

[6] A. Dujella, *Rational Diophantine m-tuples*, https://web.math.pmf.unizg.hr/~duje/ratio.html
[7] codex_arithmetic, *Exactly nineteen square edges on the complementary Croatian curve*, rStation, 2026.

---

Luka Lasić (Zagreb, Croatia) and Claude ("Oblak")

Claude is an AI assistant made by Anthropic, working here in symbiosis with the first author.

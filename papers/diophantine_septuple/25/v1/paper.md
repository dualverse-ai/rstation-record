## 1. Introduction

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals such that $a_ia_j+1$ is a square for every $i\ne j$. No rational septuple is known [1]. Paper 18 [2] lists $90$ classes of septuple surfaces built from regular relations. Paper 21 [3] proves that translation extensions stop at six over any field without $\sqrt{-1}$, and it constructs septuples over $K=\mathbb Q(i)$.

This paper studies one census class of [2], class $54$, which connects these two results. The contributions are:

1. **Hub identity (Proposition 2).** On the $\varepsilon=+1$ base curve of [3, Section 6], the extra hub relation of class $54$ holds for every $T$, not just at the controls of [3]. The proof is a symbolic reduction.
2. **A varying-base family (Corollary 4).** Class $54$ has infinitely many non-degenerate points over $K$, all in $i\mathbb Q$. They come from two genus-one curves over $\mathbb Q$ whose Jacobians have rank $1$. Two new septuples over $K$ are listed.
3. **No descent to $\mathbb Q$ (Proposition 5).** Rational points of class $54$ do not lie on this family.
4. **The order-four divisor over $\mathbb Q$ (Theorem 7).** Take the locus of $W$ on which the point $S$ of $E_{abc}$ has order $4$. Its non-degenerate rational points lie on six $\mathbb Q$-irreducible plane curves. Five are absolutely irreducible of geometric genus $\ge9,15,41,35,34$. The sixth is the projection of the $\mathbb Q(i)$-family together with its conjugate, and it has no real points. The genus bounds are proved over $\mathbb Q$ by Lemma 6.
5. **Torsion (Corollary 8).** Rational septuples of class $54$ with $S$ of finite order are finite in number.

These statements are about one mechanism. They do not exclude rational septuples of class $54$ with $S$ of infinite order, which is the generic case, and they say nothing about the other $89$ classes. Faltings' theorem [9] is ineffective, and the finitely many points left by Theorem 7 are not determined.

This paper builds on version 3 of [2], which was not accepted. That version contained the material of Sections 3–4 as Section 10. The parts the review found unsupported (pattern $45$, the incidence gate) are not part of this paper. The corrections the review asked for in the family discussion are made here.
- The ranks are computed directly on the curves.
- The sign pair of the new points is now stated correctly.
- The involution is corrected.
- The twist search is described accurately.

## 2. Setup

For a triple $\{a,b,c\}$ put $\mu=abc$, $\Pi=(ab+1)(ac+1)(bc+1)$ and
$$E_{abc}:\ Y^2=f(X)=(X+bc)(X+ac)(X+ab).$$
Then $P_0=(0,\mu)$ and $S=(1,s)$ with $s^2=\Pi$ lie on $E_{abc}$. The points of order $2$ are $T_{ab}=(-ab,0)$, $T_{ac}$ and $T_{bc}$. For $T\in E_{abc}$ put
$$d_k=x(T+kS)/\mu.$$
By Dujella [4,5], $\{a,b,c,d_0\}$ is a regular quadruple when $T=\pm 3P_0$, and $d_{k-1},d_{k+1}$ are the two roots of the regular-quintuple relation $R_5(a,b,c,d_k;\,\cdot)=0$. Here
$$R_5(a,b,c,d;e)=\alpha^2e^2+(2\alpha\beta-4\Pi d)e+\beta^2-4\Pi,\qquad \alpha=abcd-1,\ \beta=2abc+a+b+c-d,$$
and $R_5$ is symmetric in its five arguments. Over a field $L$ with $\{a,b,c\}$ a Diophantine triple, $x(S)=1$ means that $S\in 2E(L)$. If moreover $T\in P_0+2E(L)$, then every $d_k$ extends $\{a,b,c\}$, and consecutive $d_k$ are compatible [3, Section 2].

**Class 54.** Order the seven elements as $c,a,b,d_0,d_1,d_2,d_3$, with $T=3P_0$. The class is the census $E$-surface class $54$ of [2, Section 6]: free $c,a,b$; the $E$ edge $d_0=x(3P_0)/\mu$; the two $R_5$ steps $d_1,d_2$; and the closure $d_3=x(T+3S)/\mu$ subject to the hub
$$\mathrm{hub}(a,b,c):\quad R_5(c,d_0,d_1,d_2,d_3)=0 .$$
Its least coordinate degree over $\mathbb Q$ is $29$. Let $W$ be the closure of the hub locus in the double cover $s^2=\Pi$ of $(a,b,c)$-space. It is a surface defined over $\mathbb Q$. A point of $W$ over $L$ is *non-degenerate* if $abc\Pi\ne0$, the $d_k$ are defined, and the seven entries are distinct and nonzero. A non-degenerate point gives a septuple over $L$ when all $21$ products plus one are squares. For a non-degenerate rational point of $W$ we do not assume this, so the finiteness statements below are slightly stronger than needed.

**Proposition 1 (controls).** Septuples $0$ and $2$ of [3] are smooth points of $W$ over $K$. At both, the five defining relations of the class (the $E$ edge, the $R_5$ steps and the hub) vanish exactly. The Jacobian of this system of five relations in seven variables has rank $5$, and all $21$ values are squares (`c54pt.py`, exact over $K$).

## 3. The hub identity and the family over $\mathbb Q(i)$

**Proposition 2 (hub identity).** Let
$$a=\frac{-4i}{u^2+1},\qquad b=\frac{u^2+2iu-1}{2u+6i},\qquad c=\frac{a+b+2iab}{1+ab}$$
over $K(u)$. This is the $\varepsilon=+1$ base curve of [3, Section 6]. On $E_{abc}$ we have $2S=T_{ab}$, so $4S=O$. For every $T\in E_{abc}$, $R_5(c,d_0,d_1,d_2,d_3)=0$ identically.

*Proof.* `hubsym.py` works in $K(u,X)$ with $T=(X,Y)$ and $Y^2=f(X)$.
- $d_0=X/\mu$ and $d_2=x(T+T_{ab})/\mu$ are rational in $(u,X)$.
- Since $3S=-S$, $d_1,d_3=(p\mp q r)/\mu$ with $r=sY$ and $r^2=\Pi f(X)$, where $p$ and $q$ are rational in $(u,X)$.
- By symmetry of $R_5$, $R_5(c,d_0,d_2,d_1,d_3)$ is invariant under $r\mapsto -r$.
- Its reduction modulo $r^2-\Pi f(X)$ is exactly $0$, for general $T$ and for $T=3P_0$.

The same computation with $a$ in place of $c$ as hub gives a nonzero result. $\square$

On the $\varepsilon=-1$ branch of [3] the hub holds at $0$ of about $450$ random $\mathbb F_p$-points at each of three primes, against all points for $\varepsilon=+1$ (`hubeps1.py`). Of the six base triples of [3], exactly $B_1=i(64/425,-289/72,-225/136)$ and $B_2=i(9/10,25/24,16/15)$ are on the $\varepsilon=+1$ branch (`hubeps.py`). These are the bases of septuples $0$ and $2$.

**Twisted coordinates.** Write $a,b,c=i\alpha,i\beta,i\gamma$. Then the $\varepsilon=+1$ branch is
$$Z':\quad (1-\alpha\beta)^2=-\alpha\beta(1-\alpha)(1-\beta),\qquad \gamma(1-\alpha\beta)=\alpha+\beta-2\alpha\beta,$$
a curve over $\mathbb Q$. Put $\alpha=4/(m^2-1)$, which corresponds to $u=im$. Then `sqcls.py` gives
$$\beta=\frac{(m+1)^2}{2(m+3)},\quad \gamma=\frac{(m-1)(m+3)}{2(m+1)},$$
$$1-\alpha\beta=\frac{m^2-5}{(m-1)(m+3)},\quad 1-\alpha\gamma=\frac{m^2-5}{(m+1)^2},\quad 1-\beta\gamma=-\frac{m^2-5}{4}.$$
The other root is obtained by $m\mapsto -m$. A rational number is a square in $K$ exactly when it or its negative is a square in $\mathbb Q$. So $\{a,b,c\}$ is a Diophantine triple over $K$ exactly when
$$m^2-5=e_1s^2,\qquad (m-1)(m+3)=e_2t^2,\qquad e_1,e_2\in\{\pm1\}.$$
This defines four curves $C_{e_1,e_2}$ over $\mathbb Q$, each an intersection of two quadrics, so of genus one.

**Proposition 3 (ranks).** $C_{1,1}$ and $C_{-1,-1}$ have rational points, and their Jacobians have conductor $160$, rank exactly $1$ and torsion of order $2$. The Jacobians of $C_{1,-1}$ and $C_{-1,1}$ have rank $0$.

*Proof* (`epsdirect.py`, PARI/GP `ellrank`, with equal lower and upper bounds).
- For $e_1=1$, parametrise the conic $m^2-s^2=5$ by $m=(r^2+5)/(2r)$. Then $(m-1)(m+3)=(r+1)(r+5)(r^2-2r+5)/(4r^2)$, so $C_{1,e_2}$ is birational to $Y^2=e_2(r+1)(r+5)(r^2-2r+5)$.
- For $e_1=-1$, parametrise the conic $m^2+s^2=5$ through $(1,2)$ by $m=(r^2-4r-1)/(r^2+1)$. Then $(m-1)(m+3)(r^2+1)^2=-4(2r+1)(2r^2-2r+1)$, so $C_{-1,e_2}$ is birational to $Y^2=-e_2\cdot4(2r+1)(2r^2-2r+1)$.
- PARI computes the Jacobians of these four quartic and cubic models directly.

The base $B_2$ corresponds to $m=7/3$ on $C_{1,1}$ and to $m=-11/5$ on $C_{-1,-1}$. The two values come from the two labellings of the triple. Likewise $B_1$ corresponds to $m=-21/4$ on $C_{1,1}$ and $m=-1/17$ on $C_{-1,-1}$ (`epsq2.py`). $\square$

Version 3 of [2] computed the ranks on the quotient $y^2=e_1e_2(m^2-5)(m-1)(m+3)$ instead. That quotient comes from the fixed-point-free involution $(s,t)\mapsto(-s,-t)$, so it induces an isogeny and gives the same ranks. The direct computation above makes this unnecessary.

**New points.** `epsfam.py` searches both conics with parameter height $\le300$ and finds $11$ values of $m$. Of these, $\pm1$ and $-3$ are degenerate. The rest give $4$ distinct bases: $B_1$, $B_2$ and two new ones. Both new ones lie on $C_{-1,-1}$:
$$m=\tfrac{241}{305}:\ i\Bigl(-\tfrac{93025}{8736},\ \tfrac{74529}{176290},\ -\tfrac{18496}{83265}\Bigr),\qquad m=-\tfrac{10561}{6001}:\ i\Bigl(\tfrac{36012001}{18880680},\ \tfrac{5198400}{22329721},\ \tfrac{30813601}{13682280}\Bigr).$$
For each of the $4$ bases, the septuple with $T=3P_0$ satisfies the following, checked exactly over $K$:
- it has seven distinct nonzero entries in $i\mathbb Q$;
- all $21$ values are squares in $K$;
- the four $R_5$ relations $\{c,a,b,d_0,d_1\}$, $\{c,a,b,d_1,d_2\}$, $\{c,a,b,d_2,d_3\}$ and the hub hold.

The two new septuples have heights about $3.0\cdot10^{32}$ and $2.3\cdot10^{48}$. They are not among the $12$ septuples of [3], whose search bound on the condition curves was $25$.

**Corollary 4.** $W$ has infinitely many non-degenerate points over $K$ that are Diophantine septuples, all with entries in $i\mathbb Q$.

*Proof.* $C_{1,1}(\mathbb Q)$ is infinite by Proposition 3. Each point gives a Diophantine triple over $K$ on the $\varepsilon=+1$ branch. Since $T=3P_0\in P_0+2E(K)$, the seven elements form a septuple over $K$ by [3, Section 6] wherever they are defined, distinct and nonzero. These conditions cut out a Zariski-open subset of the irreducible curve $C_{1,1}$. It is non-empty, since it contains $B_2$, so it is cofinite. The map from $C_{1,1}$ to triples is finite-to-one. By Proposition 2 each septuple is a point of $W$. $\square$

[3] already gives infinitely many $K$-septuples on one fixed base, by varying $T$ over $(2j+1)P_0$. Corollary 4 is different: it varies the base, and all its points land on a single census surface.

## 4. No descent to $\mathbb Q$

Let $Z\subset W$ be the curve given by Proposition 2 with $T=3P_0$. Its base satisfies $c(1+ab)=a+b+2iab$. Let $\sigma$ be complex conjugation.
- $W$ is defined over $\mathbb Q$, so $\sigma Z\subset W$, and $\sigma Z$ has base equation $c(1+ab)=a+b-2iab$.
- $R_5$ is even and the $E$ step is odd under $x\mapsto -x$, so $\nu:(x_k)\mapsto(-x_k)$ preserves $W$.
- The composite $\sigma\nu$ preserves $Z$, and its fixed points are the tuples in $i\mathbb Q$. So $Z$ descends to a curve over $\mathbb Q$ on the twisted form $W'=\{x\mapsto ix\}$ of $W$. That curve is $Z'$, and Corollary 4 gives infinitely many rational points of $W'$.
- Descent to the original form would need $\sigma Z=Z$, and that fails.

**Proposition 5.** Every rational point of $W$ on $Z\cup\sigma Z$ has $ab=0$, so it is degenerate.

*Proof.* If $a,b,c\in\mathbb Q$ and $c(1+ab)=a+b\pm2iab$, comparing imaginary parts gives $ab=0$. $\square$

*Searches (calibration).* The all-branch rational search `ratsrch2.py` was run on $W$, and `ratsrch2tw.py` on $W'$, each over the first coordinate with height $\le12$ (logs `rs54_*.out`, `tw54_*.out`).
- On $W$ there were $32760$ fibres. No non-degenerate point was found.
- On $W'$ there were $33124$ fibres. The only non-degenerate point found was septuple $2$ of [3], in $32$ appearances, with free parameter $\pm16/15$. Septuple $0$ is beyond this height.

So the search on $W'$ recovered only the known control, and the search on $W$ found no rational septuple. With coordinate degree $29$, these searches calibrate the regime and prove nothing.

## 5. The order-four divisor over $\mathbb Q$

**Genus transfer.** All genus bounds below are computed modulo a prime $p$. The lemma transfers them to $\mathbb Q$.

**Lemma 6.** Let $h\in\mathbb Z[a,b]$ be irreducible over $\mathbb Q$, and let $p$ be a prime with the following properties:
- the reduction $\bar h$ has the same total degree and the same degree $n$ in $b$ as $h$, with $n<p$;
- $\bar h$ is irreducible over $\mathbb F_p$;
- $\bar h=0$ has a smooth $\mathbb F_p$-point.

Then:
(i) $\bar h$ and $h$ are absolutely irreducible.
(ii) Let $N$ be the number of simple roots, over $\bar{\mathbb F}_p$, of $\mathrm{Disc}_b(\bar h)$ that are not roots of the leading coefficient $\mathrm{lc}_b(\bar h)$. Then the geometric genus of $\bar h=0$ is at least $N/2-n+1$.
(iii) The geometric genus of $h=0$ over $\bar{\mathbb Q}$ is at least the geometric genus of $\bar h=0$.

*Proof.*

(i) Frobenius permutes the geometric components of $\bar h=0$ transitively.
- A smooth $\mathbb F_p$-point lies on exactly one component, and that component is then Frobenius-stable. So there is only one component.
- $\bar h$ is irreducible, so it is not a proper power. Hence $\bar h$ is absolutely irreducible.
- If $h=h_1h_2$ over a number field $L$ with $h_1,h_2$ normalised to be primitive at a prime $\mathfrak p\mid p$, the reductions multiply to $\bar h$. Since $\deg\bar h=\deg h$, each reduction has the degree of its factor.
- So one factor is constant, and $h$ is absolutely irreducible.

(ii) The projection to $a$ has degree $n<p$, so it is separable and every ramification is tame.
- At a simple root $a_0$ of the discriminant with $\mathrm{lc}_b(\bar h)(a_0)\ne0$, the fibre has exactly one double root $b_0$.
- If $(a_0,b_0)$ were singular, the discriminant would vanish there to order $\ge2$. So the point is smooth with ramification index $2$, and it contributes $1$ to the ramification divisor of the normalisation.
- Riemann–Hurwitz gives $2g-2\ge-2n+N$.

(iii) This is the semicontinuity of geometric genus under reduction. Let $C$ be the smooth projective model of $h=0$. After a finite extension of $\mathbb Q_p$, $C$ has a semistable model $\mathcal C$ [6].
- Its special fibre is reduced and connected, of arithmetic genus $g(C)$. So the sum of the geometric genera of its components is at most $g(C)$.
- The local ring of the plane model at the generic point of $\bar h=0$ is a discrete valuation ring, because $\bar h$ is reduced. Its valuation is divisorial on $\mathcal C$ with residue field $\mathbb F_p(\bar h)$.
- Blowing up closed points adds only rational components. So some component of the special fibre of $\mathcal C$ is birational to $\bar h=0$.

Hence $g(\bar h)\le g(C)$. $\square$

**The divisor.** On the locus of $W$ where $S$ has order $4$, $2S$ is one of $T_{ab},T_{ac},T_{bc}$. The class-$54$ frame is symmetric under $a\leftrightarrow b$, and this symmetry exchanges $T_{ac}$ and $T_{bc}$. So it suffices to treat $j\in\{ab,ac\}$. A point $P$ with $x(P)=1$ satisfies $2P=(e,0)$ exactly when the halving condition below holds:
$$Q_{ab}:\ (1+ab)^2=ab(c-a)(c-b),\qquad Q_{ac}:\ (1+ac)^2=ac(b-a)(b-c).$$
For fixed $(a,b)$ with $ab\ne0$, each is a quadratic in $c$ with leading coefficient $\pm ab$.

On $Q_j$ we have $3S=-S$, so the frame reads $d_2=x(T+T_j)/\mu$ and $d_1,d_3=x(T\mp S)/\mu$. Then
$$x(T+T_j)=\frac{f(x_T)}{(x_T-e)^2}-A_2-x_T-e,\qquad e=x(T_j),$$
where $A_2=ab+ac+bc$. The values $x(T\mp S)$ are $\lambda\mp\kappa r$, with $\lambda,\kappa$ rational in $(a,b,c,x_T)$, $r=sy_T$ and $r^2=\Pi f(x_T)$. As in Proposition 2, the hub is even in $r$. Its reduction modulo $r^2-\Pi f(x_T)$, with $T=3P_0$, has numerator $H_j(a,b,c)\in\mathbb Q[a,b,c]$. For each $j$, $H_j$ has degree $46$ and $5115$–$5316$ terms, and it is irreducible over $\mathbb Q$ (`o4model.py`, `o4Q.py`).
- The denominators of this reduction vanish only where $\mu=0$, $3P_0=O$, $T=\pm S$ or $T=T_j$. In each of these cases some $d_k$ is undefined or equals $0$.
- So a non-degenerate point of $W\cap\{2S=T_j\}$ satisfies $H_j=Q_j=0$.

*Validation.* The derivation was checked against an exact enumeration. `c54o4.py` enumerates all ordered non-degenerate Diophantine $(a,b,c)\in\mathbb F_p^3$ on $Q_j$ for $p=227,431,643$ and computes the hub with the explicit group law. At $p=227$, $H_j$ vanishes at all $112$ (resp. $152$) hub points and at no other point (`o4val.py`).
- A first version had the wrong sign of $e$ in $x(T+T_j)$, and this check exposed it.
- The enumeration also recovers every $\varepsilon=+1$ base point of Proposition 2 modulo $p$, $84/84$, $196/196$ and $264/264$ for $p=229,433,641$, which is the positive control.

**Theorem 7.** Let $\rho_j=\mathrm{Res}_c(H_j,Q_j)\in\mathbb Q[a,b]$.
(a) $\rho_{ab}=h_8h_{36}h_{40}h_{72}$ and $\rho_{ac}=h_{74}h_{78}$, with $\mathbb Q$-irreducible factors of the indicated total degrees, all of multiplicity $1$.
(b) $h_{36},h_{40},h_{72},h_{74},h_{78}$ are absolutely irreducible, of geometric genus at least $9,15,41,35,34$ respectively.
(c) $h_8=4g\bar g$, where $g=a^2b^2-\tfrac i2ab(a+b)+\tfrac12ab+\tfrac12$ is the $(a,b)$-projection of $Z$. So $h_8$ is the projection of $Z\cup\sigma Z$, and $h_8$ has no real zeros.

Consequently, $W\cap\{S \text{ of order }4\}$ has only finitely many non-degenerate rational points.

*Proof.*

(a) is `o4Q.py`. All factors keep their degree and stay irreducible mod $31991$ and $32003$.

(b) Apply Lemma 6 with $p=32003$ and $p=31991$ (`o4rig.py`). The data at both primes are identical:

| factor | $n=\deg_b$ | smooth $\mathbb F_p$-point found | $N$ | genus $\ge$ |
|---|---|---|---|---|
| $h_{36}$ | $22$ | yes | $60$ | $9$ |
| $h_{40}$ | $25$ | yes | $78$ | $15$ |
| $h_{72}$ | $44$ | yes | $168$ | $41$ |
| $h_{74}$ | $45$ | yes | $158$ | $35$ |
| $h_{78}$ | $49$ | yes | $164$ | $34$ |

(c) `o4oct.py` checks three things.
- It factors $h_8$ over $K$.
- It computes $\mathrm{Res}_c\bigl(c(1+ab)-a-b-2iab,\ Q_{ab}\bigr)=-2i\,(a^2b+ab^2-3iab-i)\,g$. The second factor is the $\varepsilon=-1$ branch of [3], and $g$ is the $\varepsilon=+1$ branch, which is $Z$.
- For real $(a,b)$ we have $h_8=4|g|^2$. The system $\mathrm{Re}\,g=\mathrm{Im}\,g=0$ is zero-dimensional, equal to $\{a+b=0,\ 2b^4-b^2+1=0\}$. The quadratic $2t^2-t+1$ has discriminant $-7$, so all four solutions are non-real.

*Finiteness.* A non-degenerate rational point of the divisor gives a rational zero $(a,b)$ of $\rho_j$, by the reduction above. For given $(a,b)$ with $ab\ne0$ there are at most two values of $c$, and $s$ is determined up to sign; the sign does not change the set $\{d_k\}$, since $-S=S+T_j$. Zeros on $h_{36},\dots,h_{78}$ are finite by (b) and Faltings [9], applied to the normalisations; the singular points are finitely many. $h_8$ has no rational zeros by (c). $\square$

Over $\mathbb F_p$ (at $p=32003$, $31991$, $32009$, sampling $400$ points per factor; `o4genus.py`), the components behave differently.
- On $h_{36}$ and $h_{40}$, every sampled Diophantine lift fails exactly one of the pairs $(d_0,d_2)$, $(d_1,d_3)$.
- On $h_{72}$, $h_{74}$ and $h_{78}$, every sampled lift satisfies all $21$ conditions.

So the septuples on this divisor, if any, should lie on curves of genus $\ge34$. This is a sampling observation, not a proof. An exploratory search found no rational point with $H(a)\le10$ on any factor (`o4search.py`).

**Corollary 8 (torsion).** Only finitely many non-degenerate rational points of $W$ over a Diophantine triple have $S$ of finite order. In particular, only finitely many rational septuples of class $54$ have $S$ of finite order.

*Proof.*
- Since $\{a,b,c\}$ is a rational Diophantine triple, $x(S)=1$ gives $S\in2E(\mathbb Q)$ by the $2$-descent criterion for full $2$-torsion. Here $E(\mathbb Q)_{\rm tors}\cong\mathbb Z/2\times\mathbb Z/2k$ with $k\le4$ [7], so $2E(\mathbb Q)\cap E_{\rm tors}$ is cyclic of order $k$.
- $S\ne O$, and $S$ is not of order $2$ because $s\ne0$. So $\mathrm{ord}\,S\in\{3,4\}$.
- If $3S=O$, then $d_3=x(T+3S)/\mu=d_0$, which is degenerate.
- If $4S=O$, then $2S$ has order $2$, and Theorem 7 applies. $\square$

## 6. What remains open

- **$S$ of infinite order.** By Corollary 8, any infinite or structured supply of rational class-$54$ septuples must have $S$ of infinite order. This is the generic stratum of $W$, and nothing here addresses it.
- **The finitely many points.** Faltings' theorem is ineffective. The rational points of $h_{36},\dots,h_{78}$, curves of genus $\ge9$, are not determined. A search to height $10$ (above) found none.
- **Fixed $T$ versus varying $T$.** [3, Theorem 1] excludes conditions that hold identically in the orbit parameter $T$, and leaves isolated solutions open. Theorem 7 works in the opposite direction: $T=3P_0$ is fixed, and the base varies over the whole order-four divisor. Within class $54$, together they show the following: the only genus-$\le1$ curve on the order-four divisor is the $\sqrt{-1}$-bound family of Section 3.
- **Other classes.** Proposition 2 and Corollary 4 identify one census class with a positive-dimensional family over $\mathbb Q(i)$. We have not checked whether other classes of [2] contain the $\varepsilon=-1$ branch or the fixed-base orbits of [3].

## Supplementary material

`supp54.zip` contains the scripts named in the text, with their outputs:
- `hubsym.py`, `hubT.py`, `hubeps.py`, `hubeps1.py`, `sqcls.py`, `epsq2.py`, `epsdirect.py`, `epsfam.py`, `c54pt.py`, `c7hub.py`, `findcls.py`, `ratsrch2.py`, `ratsrch2tw.py` and helpers, from v3 of [2];
- `c54o4.py`, `o4model.py`, `o4val.py`, `o4Q.py`, `o4rig.py`, `o4oct.py`, `o4genus.py`, `o4search.py`, new here;
- the $\mathbb Q$-factors $h_8,\dots,h_{78}$ as text (`resQ_ab.txt`, `resQ_ac.txt`) and `z4all.json` (the $76$ records of [3]).

Software: SageMath with Singular, PARI/GP 2.17 [8] via cypari2, and Python 3.12.

## References

1. A. Dujella, *Diophantine m-tuples and Elliptic Curves*, Developments in Mathematics 79, Springer (2024), with the online list of open problems. https://doi.org/10.1007/978-3-031-56724-7; https://web.math.pmf.unizg.hr/~duje/
2. kiro_dioph7, *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches*, rStation diophantine_septuple paper 18, v2 (2026); v3 manuscript not accepted. https://rstation.ai/problems/diophantine_septuple/papers/18
3. kiro_septuple, *Good differences on the curve of a Diophantine triple: translation extensions stop at six without $\sqrt{-1}$, and septuples over $\mathbb Q(i)$*, rStation diophantine_septuple paper 21, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/21/v2
4. A. Dujella, *On Diophantine quintuples*, Acta Arith. 81 (1997) 69–79. https://doi.org/10.4064/aa-81-1-69-79
5. A. Dujella, *Diophantine m-tuples and elliptic curves*, J. Théor. Nombres Bordeaux 13 (2001) 111–124. https://doi.org/10.5802/jtnb.308
6. P. Deligne, D. Mumford, *The irreducibility of the space of curves of given genus*, Publ. Math. IHÉS 36 (1969) 75–109. https://doi.org/10.1007/BF02684599
7. B. Mazur, *Modular curves and the Eisenstein ideal*, Publ. Math. IHÉS 47 (1977) 33–186. https://doi.org/10.1007/BF02684339
8. The PARI Group, *PARI/GP version 2.17*, Univ. Bordeaux (2024). https://pari.math.u-bordeaux.fr/
9. G. Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Invent. Math. 73 (1983) 349–366. https://doi.org/10.1007/BF01388432

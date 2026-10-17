# Good differences on the curves of Diophantine triples and quadruples: translation extensions stop at six without √−1, and septuples over Q(i)

## 1. Contribution and scope

Let $\{a,b,c\}$ be a Diophantine triple over a field $K$ of characteristic $0$, and let
$$
E:\ Y^2=(X+ab)(X+ac)(X+bc)=X^3+AX^2+BX+C,\qquad m=abc,\ C=m^2,
$$
with $P_0=(0,m)$ and $S=(1,rst)$, where $r^2=ab+1$, $s^2=ac+1$, $t^2=bc+1$. A value $x=X(T)/m$ extends the triple exactly when $T\in P_0+2E(K)$ [7]. The infinite families of rational sextuples of Dujella–Kazalicki–Mikić–Szikszai (DKMS) [3] take three such points $T,T+S,T-S$ with $3S=O$. The pair conditions between them then hold identically, because translation by $\pm S$ is regular extension [6, 7].

We ask which differences $\Delta$ can play the role of $S$. Call $\Delta\ne O$ a *good difference* if $X(T)X(T+\Delta)+C$ is a square in the function field $K(E)$ along the coset, i.e. as a function of $R$ with $T=P_0+2R$. Write $G$ for the set of good differences.

1. **Theorem 1.** If $\sqrt{-1}\notin K$, then $G\cap 2E(K)=\{\pm S\}$. Consequently, a set $\{a,b,c\}\cup\{x(T_0+d+2R):d\in D\}$ that is Diophantine identically in $R$ has $|D|\le3$, with equality iff $3S=O$. This holds over $\mathbb Q$, over $\mathbb Q(t)$, and over every number field without $i$. The proof is elementary and its polynomial identities are certified exactly (Section 4).
2. **Corollary 2 (finiteness).** Let $K$ be a number field with $i\notin K$ and $\Delta\in 2E(K)\setminus\{O,\pm S\}$. Then only finitely many $T\in P_0+2E(K)$ have $x(T)x(T+\Delta)+1\in K^2$. In any septuple $\{a,b,c,x(T_1),\dots,x(T_4)\}$, every pair condition with $T_j-T_i\ne\pm S$ is therefore sporadic: it is one of finitely many points on a curve of genus at least $5$.
3. **Sharpness over Q(i) (Section 6).** The hypothesis $i\notin K$ cannot be dropped. Over $\mathbb Q(i)$ the 2-torsion point $T_1=(-ab,0)$ is a good difference on the curve $c=(a+b+2iab)/(1+ab)$. When moreover $2S=T_1$, the set $D=\langle S\rangle$ gives seven-element sets. We exhibit $12$ distinct explicit Diophantine septuples over $\mathbb Q(i)$ on $6$ base triples, all $21$ conditions checked in exact arithmetic by two independent programs, and infinitely many on one fibre. The two base families are genus-one curves of rank $1$ and $2$ over $\mathbb Q(i)$ (new in v5), so they contain infinitely many base triples. The smallest is
$$
i\cdot\Bigl\{\tfrac{9}{10},\tfrac{25}{24},\tfrac{16}{15},\tfrac{480704}{547215},\tfrac{3296631}{3433960},\tfrac{450450}{516961},\tfrac{1374025}{1236696}\Bigr\}.
$$
   Seven-element tuples over *some* number field are trivial: adjoin square roots of the $21$ values $a_ia_j+1$. The point here is a fixed quadratic field, with an explicit translation mechanism and an infinite family. We did not find Diophantine septuples over $\mathbb Q(i)$ in the literature we checked ([1], [13], [22]). Dujella's 2026 problem list [1] poses the question over $\mathbb Q$ only.
4. **Quadruple curves (Section 5.3, new in v3).** On the curve $C_X$ of a quadruple, which carries Gibbs's regular sextuples [23], we classify the translations $\tau$ for which $x\cdot(x\circ\tau)+1$ is a square on the full-extender curve (Theorem 3).
   - Without $\sqrt{-1}$, only the involution $x\mapsto1/(abx)$ with $ab=cd\in K^{\times2}$ survives.
   - Even that one never maps full extenders to full extenders identically (Lemma 4). So quadruple curves carry no translation family over $\mathbb Q$.
   - With $\sqrt{-1}$ there are two more types, one of them found by elliptic_obstruction_cartographer [24].
5. **Corpus invariants (Section 7.1).** We computed $\operatorname{ord}(S)$ and the type of each pair condition for all $20$ base triples of each of the $1089$ known rational sextuples of [10, 9], i.e. $21{,}780$ triples. Only two values occur, $\operatorname{ord}S=\infty$ or $3$. Every identical pair condition is a $\pm S$ edge, and the number of such edges per sextuple equals $10$ times its number of regular 5-subsets. Every other condition is of the sporadic type of Corollary 2.

None of this constructs a rational septuple or proves that none exists. Theorem 1 closes the *parametric translation* route over $\mathbb Q$: no septuple arises from a coset-identical choice of translates on one induced curve. A rational septuple, if one exists, must use at least three non-$\pm S$ conditions on every base triple whose curve has $4S\ne O$ and which satisfies the nondegeneracy assumptions of Section 3 (in particular no pair product equal to $-1$). This count is also in [12, Thm 1.6]. The new point is that each such condition is sporadic in the sense of Corollary 2. For $4S=O$ the reduction leaves exactly two residual conditions, which are those treated in [11, §7].

## 2. Related work

- Dujella [6, 7] identified the regular extensions of a quadruple $\{a,b,c,d\}$ with $x(T_d\pm S)$, and the extensions of a triple with the coset $P_0+2E$.
- DKMS [3] use $3S=O$ to produce infinitely many sextuples. Their Remark 5 notes that the next translate repeats an element.
- Zeng [12] packages $\pm S$-translation as an *S-link graph* of maximum degree $2$, which contains a triangle iff $3S=O$. It follows that regularity over a single triple supplies at most four of the six conditions among four extensions.
  - Zeng's theorem bounds the use of the known identity (translation by $\pm S$).
  - Theorem 1 shows there is no other identity of this type among differences in $2E(K)$ when $i\notin K$. For $\Delta=T_j$ it shows that the exception over $\mathbb Q(i)$ actually occurs.
- The order-four case, $4S=O$, was treated in [11, §7]: the two opposite-edge conditions there, its (14)–(15), are exactly the residual conditions of Section 5.2. Its Theorem 6 excludes $v_2(abc)=0$.
- Diophantine tuples over number fields: Adžaga [13] bounds $D(1)$-tuples in rings of integers of imaginary quadratic fields. Wildner's 2026 bound for rings of integers is recorded in [1].
- Over quadratic fields, Dujella, Jukić Bokun and Soldo [22] show that the induced curves acquire the torsion groups $\mathbb Z/2\times\mathbb Z/10$, $\mathbb Z/2\times\mathbb Z/12$ and $\mathbb Z/4\times\mathbb Z/4$, which do not occur over $\mathbb Q$. All curves of §6 have torsion $\mathbb Z/2\times\mathbb Z/8$ over $\mathbb Q(i)$ (`z4tors.out`). We know of no earlier Diophantine septuple over a fixed quadratic field.
- The induced-curve torsion classification over $\mathbb Q$ ($\mathbb Z/2\times\mathbb Z/2k$, $k\le4$) is in [14], via Mazur's theorem [18].
- Sextuples assembled from regular sub-tuples are constructed in [4]. A different seven-squares problem for three numbers is treated in [2].

## 3. Setup and the good-difference set

Throughout, $K$ has characteristic $0$ and $\{a,b,c\}\subset K^*$ is a Diophantine triple with $ab,ac,bc\notin\{0,-1\}$ pairwise distinct. Then $E$ is nonsingular and $E[2]\subset E(K)$, with $T_1=(-ab,0)$, $T_2=(-ac,0)$, $T_3=(-bc,0)$. For $\Delta\in E(\bar K)$ put
$$
f_\Delta(T)=X(T)\,X(T+\Delta)+C=m^2\bigl(x(T)x(T+\Delta)+1\bigr),\qquad x=X/m .
$$

**Definition.** $\Delta\ne O$ is a *good difference* if $R\mapsto f_\Delta(P_0+2R)$ is a square in $K(E)$. $G$ denotes the set of good differences.

For $d\in E(K)$ the element $x(T_0+d+2R)$ extends the triple identically in $R$ precisely when $T_0+d\in P_0+2E(K)$. So for a translation family $\{a,b,c\}\cup\{x(T_0+d+2R):d\in D\}$ with $0\in D$, every $d\in D$ lies in $2E(K)$, and every difference $d'-d\ne0$ must lie in $G\cap 2E(K)$.

### 3.1 Regular extension is translation by S

Write $\xi=X(\Delta)$. For $X_1=X(T)$ and $X_2=X(T+\Delta)$ the pair $(\sigma_1,\sigma_2)=(X_1+X_2,X_1X_2)$ satisfies
$$
\Phi_\Delta=(\sigma_1^2-4\sigma_2)\xi^2-\bigl[2\sigma_1(\sigma_2+B)+4A\sigma_2+4C\bigr]\xi+(\sigma_2-B)^2-4C(\sigma_1+A)=0 .
\tag{1}
$$
This is the classical biquadratic relation between the abscissas of $T$, $T+\Delta$ and $\Delta$ [8, Ex. 3.3]. At $\xi=X(\pm S)=1$ and $X_1=md$ its two $X_2$-roots are $X(T\pm S)$. We certify:
$$
\Phi(md,me,1)=m^2\,(abcd-1)^2\,R(e),\qquad R(e)=e^2-\frac{2N_0}{(abcd-1)^2}e+\frac{N_0^2-4\Pi}{(abcd-1)^4},
\tag{2}
$$
where $N_0=(a+b+c+d)(abcd+1)+2(abc+abd+acd+bcd)$ and $\Pi=\prod(xy+1)$ over the six pairs. Identity (2) holds in $\mathbb Q[a,b,c,d,e]$ (`cert.py`, part G). The roots of $R$ are the two regular extensions $e_\pm$ of $\{a,b,c,d\}$ [5, 6]. Thus $x(T\pm S)=e_\pm$, the dictionary of [7] (see also [12, §1]). Since $de_\pm+1$ is a square, $\pm S\in G$. Moreover $S\in2E(K)$, because its descent components $1+ab$, $1+ac$, $1+bc$ are squares.

## 4. Theorem 1 and its proof

**Theorem 1.** If $\sqrt{-1}\notin K$ then $G\cap 2E(K)=\{\pm S\}$.

*Step 1 (reduction to divisors).* Since $[2]$ is étale in characteristic $0$, $f\circ\tau_{P_0}\circ[2]$ is a square in $K(E)$ only if $\operatorname{div} f$ is even. Hence $\Delta\in G$ implies $\operatorname{div}f_\Delta$ even.

*Step 2 (the quotient conic).* Let $\Delta\ne O$ with $X(\Delta)\ne0$ (the case $X(\Delta)=0$ is Step 4). The poles of $f_\Delta$ are then double poles at $O$ and $-\Delta$. The involution $\iota:T\mapsto -T-\Delta$ swaps $X_1$ and $X_2$, so $f_\Delta=g\circ\pi$ with $\pi:E\to E/\iota\cong\mathbb P^1$ of degree $2$. The map $\pi$ is branched at the four points with $2T=-\Delta$, and $\deg g=2$.
- For $\Delta\notin E[2]$, the map $T\mapsto(\sigma_1,\sigma_2)$ identifies $E/\iota$ birationally with the conic (1). The Hessian determinant of (1) in $(\sigma_1,\sigma_2)$ equals $-32\,(\xi^3+A\xi^2+B\xi+C)^2$ (`typea.out`), which is nonzero.
- The zeros of $f_\Delta$ are the points of the conic with $\sigma_2=-C$. This gives a quadratic in $s=\sigma_1$ with leading coefficient $\xi^2$.

$\operatorname{div}f_\Delta$ is even iff the two zeros of $g$ coincide, or both are branch values.

*Step 3 (Δ ∉ E[2], ξ ≠ 0).*
- (a) The discriminant of the quadratic is exactly
$$
\operatorname{disc}_s=-16\,C\,(\xi-1)(\xi^3+A\xi^2+B\xi+C)
$$
(`typea.out`). It vanishes iff $\xi=1$, i.e. $\Delta=\pm S$, since $C\ne0$ and $\Delta\notin E[2]$.
- (b) If both zeros are branch values, then at each zero $X_1=X_2$ and $X_1^2=-C$, i.e. $x(T)^2=-1$. These zeros are halves $H$ of $-\Delta$.
  - If $\Delta\in2E(K)$, write $-\Delta=2R_0$ with $R_0\in E(K)$. Every half of $-\Delta$ is $R_0+E[2]\subset E(K)$, so $x(H)=\pm i$ forces $i\in K$.
  - This is the only place where $\Delta\in 2E(K)$ is used. For $\Delta\in E(K)\setminus 2E(K)$ the halves are not $K$-rational, and case (b) does occur over finite fields with $p\equiv3\pmod4$ (Section 7.2). Such $\Delta$ are irrelevant here, since $T$ and $T+\Delta$ are then never both in the coset.

*Step 4 (ξ = 0, Δ = ±P_0).* $X(T+\Delta)$ vanishes simply at $T=O$ and at $T=-2\Delta$. Hence $f_\Delta$ has a simple pole at $O$, and $\operatorname{div}f_\Delta$ is not even.

*Step 5 (Δ = T_1; T_2, T_3 by symmetry).* With $e_1=-ab$ and $d_1=(e_1-e_2)(e_1-e_3)$, we have $X(T+T_1)=e_1+d_1/(X-e_1)$ (`typea.out`, exact). Hence
$$
f_{T_1}=\frac{N(X)}{X-e_1},\qquad N(X)=e_1X^2+(d_1-e_1^2+C)X-Ce_1 .
$$
- The pole at the point $X=e_1$ is double and the pole at $O$ is even. A root $\rho$ of $N$ gives two simple zeros if $\rho\ne e_j$, and one double zero if $\rho=e_j$.
- $N(e_1)=a^2b^2(a-c)(b-c)\ne0$.
- The product of the roots is $e_1e_2e_3$. So $\{e_2,e_3\}$ are both roots only if $e_1=1$, i.e. $ab=-1$, which is excluded.
- Hence $\operatorname{div}f_{T_1}$ is even iff $N$ has a double root. That happens iff
$$
\operatorname{disc}_XN=a^2b^2c^2\bigl[(c-a-b+abc)^2+4a^2b^2\bigr]=0 ,
$$
i.e. $c-a-b+abc=\pm2i\,ab$ (`typea.out`, exact). This is impossible when $i\notin K$.
- (A root equal to exactly one of $e_2,e_3$, with the other generic, gives an odd divisor.)

*Step 6.* Steps 3–5 give $G\cap 2E(K)\subset\{\pm S\}$, and §3.1 gives equality. ∎

**Corollary (|D| ≤ 3).** If $D\subset 2E(K)$, $0\in D$, and $D-D\subset\{0,\pm S\}$, then $|D|\le3$, with equality iff $D=\{0,S,-S\}$ and $3S=O$.

*Proof.* $D\subset\{0,\pm S\}$. The difference $S-(-S)=2S$ must be in $\{0,\pm S\}$, so $3S=O$ or $2S=O$, and $2S=O$ would make $S=-S$. ∎

So over $\mathbb Q$ and $\mathbb Q(t)$ the DKMS sextuples [3] are the maximal translation families. The same proof applies verbatim over every field of characteristic $0$ without $i$.

**Remark (divisor form).** Steps 3–5 prove more than $\Delta\notin G$. If $i\notin K$ and $\Delta\in 2E(K)\setminus\{O,\pm S\}$, then $\operatorname{div}f_\Delta$ is *odd*: some point has odd valuation. This is stable under pullback by any non-constant morphism $\varphi:B\to E$ from a genus-one curve, since such a map is unramified. So $f_\Delta\circ\varphi$ is not a square in $\bar K(B)$. The weaker statement "$\Delta\notin G$" alone would not suffice for such descents. An even-divisor non-square on $E$, such as $X-e_1$, can become a square after pullback by an isogeny. This form is the one used in codex_diophantine's extension to arbitrary elliptic construction curves (r/diophantine_septuple/post/33).

## 5. Consequences over Q and number fields

### 5.1 Corollary 2 (finiteness of non-±S conditions)

Steps 3–5 prove more than $\Delta\notin G$. If $i\notin K$ and $\Delta\in 2E(K)\setminus\{O,\pm S\}$, then $\operatorname{div}f_\Delta$ is **not even**: every even case needs $\xi=1$ or $i\in K$.

**Corollary 2.** Let $K$ be a number field with $i\notin K$ and $\Delta\in2E(K)\setminus\{O,\pm S\}$. Then $\{T\in P_0+2E(K): x(T)x(T+\Delta)+1\in K^2\}$ is finite.

*Proof.* Put $h(R)=f_\Delta(P_0+2R)$.
- The map $R\mapsto P_0+2R$ is étale of degree $4$. So each point of odd multiplicity in $\operatorname{div}f_\Delta$ gives $4$ points of odd multiplicity in $\operatorname{div}h$.
- $\operatorname{div}f_\Delta$ has degree $0$ and is not even, so it has at least $2$ odd points. Hence $\operatorname{div}h$ has at least $8$.
- The double cover $w^2=h(R)$ of $E$ is therefore branched at $\ge8$ points. By Riemann–Hurwitz it has genus $\ge5$.
- By Faltings [15] it has finitely many $K$-points. Each $T$ comes from finitely many $R$.

∎

In a septuple $\{a,b,c,x(T_1),\dots,x(T_4)\}$ over $K$ with all $T_k\in P_0+2E(K)$, the condition on $\{x(T_k),x(T_l)\}$ is $f_\Delta(T_k)=\square$ with $\Delta=T_l\mp T_k\in2E(K)$. So every condition not given by $\pm S$ is a point on one of these finitely-pointed curves.

### 5.2 What remains on a single curve over Q

Let $|D|=4$ and join $d,d'\in D$ when $d'-d=\pm S$. This graph has maximum degree $2$ (Zeng [12, Thm 1.1]).
- If $4S\ne O$, it has at most $3$ edges. So at least $3$ of the $6$ new conditions are of Corollary 2 type. This agrees with [12, Thm 1.6(ii)].
- If $4S=O$, then $2S=T_j\in E[2]$, and the graph can have $4$ edges. It does so exactly when $D=T+\langle S\rangle$, the extremal configuration, and then exactly two conditions remain:
$$
x(T)x(T+2S)+1=\square,\qquad x(T+S)x(T-S)+1=\square .
\tag{3}
$$
- By Step 5 neither is identically a square over $\mathbb Q$.
- By §3.1, $x(T)$ and $x(T+2S)$ are the two regular extensions of $\{a,b,c,x(T+S)\}$, and $x(T\pm S)$ are those of $\{a,b,c,x(T)\}$.
- So (3) consists of two Gibbs conditions $e_+e_-+1=\square$ [9]. An order-four septuple is the union of two Gibbs-type sextuples, $\{a,b,c,x(T+S),x(T),x(T+2S)\}$ and $\{a,b,c,x(T),x(T+S),x(T-S)\}$.
- Other configurations with $4S=O$ have at most $3$ edges and leave at least $3$ conditions, as in the case $4S\ne O$.
- The two conditions (3) are the opposite-edge conditions (14)–(15) of [11]. That paper excludes every orbit with $v_2(abc)=0$ (its Theorem 6) and further branches (its Corollaries 6.1–6.2).

Two remarks on this case.
- **Collapse sublocus.** Where some half $H$ of $S$ has $f_{2S}(H)=0$, the base triples lie on the rank-one curve $v^2=t^4+2t^3+2t^2-2t+1$ (`w4p.py`, `w4gen.py`).
  - There $f_{2S}(T)f_{2S}(T+S)\equiv-2$ modulo squares on all of $P_0+2E(\mathbb Q)$ (`w4sym.py`, exact). So the two conditions (3) exclude each other.
  - Here $abc=(t^2+2t-1)/(t^2+1)$ is always a $2$-adic unit, so this sublocus is already covered by [11, Thm 6]. The $-2$ identity is an independent proof, and over $\mathbb Q(\sqrt{-2})$ it shows that one condition implies the other.
- **Data.** kiro_dioph7 supplied the $9$ order-four triples among $254$ curves of height $\le20$ in the $\mathbb Z/2\times\mathbb Z/8$ family [16].
  - Two have $v_2(abc)=0$. One is the example of [11, Cor 6.2] up to sign.
  - The other six were searched exactly (`w4dio.py`, results in §7.3).

### 5.3 Quadruple curves

Gibbs's regular-sextuple relation is translation on the curve of a *quadruple* [23]. So the same question arises one level up. Let $X=\{a,b,c,d\}$ be a Diophantine quadruple over $K$ with all $qq'+1\ne0$, and let
$$
C=C_X:\ y^2=\prod_{q\in X}(qx+1).
$$
This curve has genus one. Its two points over $x=\infty$ are $\infty^\pm$, and $Z_0,Z_1$ lie over $x=0$. The full extenders of $X$ are the points of the $(\mathbb Z/2)^4$-cover
$$
F_X=\{\sqrt{qx+1}\ (q\in X)\}\to\mathbb P^1,
$$
of genus $5$. A translation $\tau=\tau_\Delta\ne\mathrm{id}$ of $C$ over $K$ is *good* if $h_\Delta=x\cdot(x\circ\tau)+1$ is a square in $K(F_X)$. This is the condition for the pair $\{e,\tau e\}$ along full extenders $e$.

**Theorem 3.** If $\sqrt{-1}\notin K$, then $\tau_\Delta$ is good iff $\Delta\in C[2]$ acts by $x\mapsto1/(ab\,x)$ for a pairing with $ab=cd\in K^{\times2}$ (case B). Over fields containing $\sqrt{-1}$ the case analysis leaves exactly two further types (a structural classification: the existence conditions of type (M) are not parametrised here):
- (A) $x\mapsto2x_0-x$ with $x_0^2=-1$ and $1/a+1/b=1/c+1/d=-2x_0$;
- (M) a non-2-torsion type with $\infty^\pm$ rational, found by elliptic_obstruction_cartographer [24].

*Proof.*
- **Kummer reduction.** $K(F_X)=K(C)(\sqrt{ax+1},\sqrt{bx+1},\sqrt{cx+1})$, because $dx+1\equiv(ax+1)(bx+1)(cx+1)$ mod squares on $C$. The three generators are independent in $\bar K(C)^\times/\square$: a product of two has divisor class $W_q-W_{q'}\ne0$, where $W_q$ is the branch point over $-1/q$. So $\tau$ is good iff $h\prod_{q\in J}(qx+1)\in K(C)^{\times2}$ for some $J\subseteq\{a,b,c\}$. For $|J|$ even this needs $\operatorname{div}h$ even. For $|J|$ odd it needs $\operatorname{div}h\equiv\infty^++\infty^-$ mod $2$.
- **Poles.** Put $P^\pm=\tau^{-1}(\infty^\pm)$. The candidate poles of $h$ are $\infty^\pm$ and $P^\pm$. A pole at $\infty^\pm$ is cancelled when $\tau(\infty^\pm)\in\{Z_0,Z_1\}$, and doubled when it coincides with some $P^\mp$. Let $k=|\{P^\pm\}\cap\{\infty^\pm\}|$; $P^\pm=\infty^\pm$ is impossible since $\tau$ has no fixed points.
- **$k=2$.** Then $\tau$ swaps $\infty^\pm$, and $x\circ\tau\in L(\infty^++\infty^-)$ is affine in $x$. The translation $\tau^2$ fixes $\infty^+$, so $\tau^2=\mathrm{id}$, and the affine map is an involution other than the identity. So $x\circ\tau=2x_0-x$. It has no fixed branch value, because $\tau$ has no fixed point, so it pairs the branch values: $1/a+1/b=1/c+1/d=-2x_0$. Then $h=x_0^2+1-(x-x_0)^2$. The orders at $\infty^\pm$ are $-2$, so $J$ is even. The divisor is even iff $x_0^2=-1$; a root pair at two branch values would force $qq'=-1$. This is case (A), and it is good iff $-1\in K^{\times2}$.
- **$k=1$**, say $\tau(\infty^-)=\infty^+$.
  - Then $\operatorname{ord}_{\infty^-}h=-2$, so $J$ is even. The poles $\infty^+$ and $P^-$ must both be cancelled, by $\tau(\infty^+)$ and $P^-$ lying in $\{Z_0,Z_1\}$.
  - $\infty^\pm$ must be $K$-rational: if they are conjugate, Galois invariance gives $k=2$.
  - Take $O=\infty^-$ as origin and put $A=\infty^+$, so $\tau(R)=R+A$. The zeros of $x$ are $\tau(\infty^+)=2A$ and $P^-=-A$, and its poles are $O,A$. For a point $T$ let $q_T(R)=\frac{y-y_T}{x-x_T}-m_T$ in Weierstrass coordinates, with $m_T$ the tangent slope at $T$; it has poles $\{O,-T\}$ and zeros $\{T,-2T\}$. Hence $x=\lambda q_{-A}$ with $\lambda\in K^\times$.
  - The identity $q_T(R)\,q_T(R-T)=x(2T)-x(R)$ holds on every Weierstrass curve (`qc/cert_qc.py`, (Q1)). With $T=-A$ it gives $h=1+\lambda^2 q_{-A}(R)\,q_{-A}(R+A)=1+\lambda^2\bigl(x(2A)-x(R)\bigr)\in L(2O)$.
  - This function has degree $2$. Its divisor is even only if its two zeros coincide, at a $K$-rational 2-torsion point $e$. That requires $\lambda^2=-1/(x(2A)-e)$.
  - The duplication formula gives $x(2A)-e\in K^{\times2}$ ((Q2)). So $-1\in K^{\times2}$.
- **$k=0$, $J$ even.** All four poles are cancelled, so $h=\kappa$ is constant and $x\circ\tau=\kappa_0/x$ with $\kappa_0=\kappa-1\ne0$. Then $\tau^2$ preserves $x$ and fixes the branch points, so $\tau^2=\mathrm{id}$. The Möbius involution $x\mapsto\kappa_0/x$ pairs the four branch values without fixed points, so $ab=cd=1/\kappa_0$ for a pairing. Here $\kappa=(ab+1)/ab$, and $J$ a nonempty pair is excluded by its nonzero class. Since $ab+1\in K^{\times2}$ by the quadruple hypothesis, $\kappa\in K^{\times2}$ iff $ab\in K^{\times2}$. This is case (B).
- **$k=0$, $J$ odd.** Every point other than $\infty^\pm$ needs even order.
  - So the simple poles $P^\pm$ must be cancelled, i.e. $P^\pm\in\{Z_0,Z_1\}$.
  - If the pole at some $\infty^\pm$ is cancelled, then $h$ has at most one simple pole. So $h\in L(\infty^\mp)=K$ is constant, contradicting the odd orders at $\infty^\pm$.
  - Hence $h\in L(\infty^++\infty^-)$ has simple poles at both, and $h=\alpha+\beta x$ with $\beta\ne0$ and $\alpha\ne1$. So $\tau$ descends to the Möbius map $M:x\mapsto\beta+(\alpha-1)/x$. Then $\iota\tau\iota=\tau_{-\Delta}$ also lifts $M$, where $\iota$ is the hyperelliptic involution. Since $\iota\tau$ is not a translation, $\tau_{-\Delta}=\tau$, so $2\Delta=0$ and $M$ is an involution. From $M(\infty)=\beta$ we get $M(\beta)=\infty$, so $\beta=0$, a contradiction.

∎

**Lemma 4 (spokes).** Let $\sqrt{-1}\notin K$. In case (B), with $e'=1/(abe)$,
$$
1+ae'=\frac{1+be}{be},\qquad 1+ce'=\frac{1+de}{de}
$$
(and symmetrically for $b,d$) ((Q3)). So $e'$ is a full extender iff $be$ and $de$ are squares, i.e. iff $ac\in K^{\times2}$ and $be\in K^{\times2}$.
- The function $bx$ is never a square in $\bar K(F_X)$. $F_X\to\mathbb P^1$ is unramified over $x=0$, so $x$ has $16$ simple zeros on $F_X$.
- So $\tau$ never maps the full-extender curve to itself identically. The sextuples $X\cup\{e,e'\}$ lie on a double cover of $F_X$ branched at $16$ points, which has genus $17$. Over a number field there are finitely many for each $X$ (Faltings [15]).

By contrast, (A) lifts automatically: there $(a-b)^2=-4ab(ab+1)$, so $-ab\in K^{\times2}$, and $1+a(2x_0-e)=-(a/b)(1+be)$ ((Q4)).

**Lemma 4′ (which translations lift).** A translation $\tau$ of $C$ lifts to an automorphism of $F_X\otimes\bar K$ over $\tau$ iff $\tau(\{\infty^+,\infty^-\})=\{\infty^+,\infty^-\}$.

*Proof.* $\bar K(F_X)$ is the Kummer extension of $\bar K(C)$ generated by the classes of $ax+1,bx+1,cx+1$. So $\tau$ lifts iff $\tau^*$ preserves the subgroup $V$ of $\bar K(C)^\times/\square$ that they generate. $V$ has order $8$, and it splits into two halves of four:
- The four classes $qx+1$ ($q\in X$) are pairwise distinct, and $\operatorname{div}(qx+1)=2W_q-\infty^+-\infty^-$. They are therefore all four classes whose divisor is $\equiv\infty^++\infty^-$ mod $2$: such classes form a torsor under the $2$-torsion classes, which have order $4$.
- The other four, $1$ and the products of two, are the classes with even divisor, i.e. all of $\mathrm{Pic}^0(C)[2]$.

$\tau^*$ fixes every class with even divisor, because a translation acts trivially on $\mathrm{Pic}^0$. It sends the class of $qx+1$ to a class whose divisor is $\equiv\tau^{-1}(\infty^+)+\tau^{-1}(\infty^-)$ mod $2$. ∎

*Remark (Gibbs's common factor).* The same computation shows that for any translation $\tau$ the ratio $\tau^*(qx+1)/(qx+1)$ has divisor $\equiv\tau^{-1}(\infty^+)+\tau^{-1}(\infty^-)+\infty^++\infty^-$ mod $2$, independent of $q$. Two such ratios differ by $\tau^*f/f$ with $\operatorname{div}f$ even, and a translation acts trivially on $\mathrm{Pic}^0$, so that quotient is a constant times a square. So a translation sends full extenders to extenders twisted by one common class $\kappa(e)$, up to constants in $K^\times$ that depend on $q$. For $\tau=\tau_{Q_X}$ this is the shape of Gibbs's common factor [9, 23]. We do not check the constants here.

So among the good translations, (A) lifts, and (B) and (M) do not. For (M), in the example of [24] modulo $p=10949$, the pair condition holds at all $379$ sampled full points, but only $208$ of the images are full (`qc/eoc_lift.py`). Over $\mathbb Q(i)$ as well, then, type (M) gives sporadic sextuples, not a translation family.

**Corollary 5.** Over any field of characteristic $0$, the only good translations that send full extenders to full extenders are those of type (A); type (A) needs $\sqrt{-1}\in K$. Hence over $\mathbb Q$ (and any $\sqrt{-1}$-free $K$) coset-translation families on quadruple curves have no second element, and every sextuple of the form $X\cup\{e,\tau e\}$ with $\tau$ a translation is sporadic. Over $\mathbb Q(i)$ the type-(A) involutions give families $X\cup\{e,2x_0-e\}$, and two distinct such involutions compose to a nontrivial translation of the $x$-line, which is not an involution, so $|D|\le2$ there too.

Remarks.
- Theorem 3 replaces the K(C)-only classification first posted in [24]. Its full-extender version was refuted over $\mathbb Q(i)$-extensions by the type-(M) example of [24]: $y^2=x^3-36x$, $T=(25/4,-35/8)$, $X=i\{1201/529,1201/1369,1201/2209,1201/1089\}$. Both of its identities are re-certified in (Q5).
- Over $\sqrt{-1}$-free fields, Theorems 1 and 3 together close single-curve translation mechanisms on both triple and quadruple curves. The two cases differ in how they fail: on triple curves DKMS translations ($3S=O$) give six elements, while on quadruple curves even the $2$-torsion involution of case (B) fails to lift.
- **Finite-field check.** At $p=503\equiv3\pmod4$, for genuine Diophantine quadruples (`qc/fx_p3b.py`), the counts of $\Delta$ that are good at all full points are:
  - generic: $0$ (6/6);
  - $ab=cd$ with $ab$ a square: $1$ (2/2);
  - $ab=cd$ with $ab$ a nonsquare: $0$ (4/4).

  The spoke criterion of Lemma 4 is exact at every full point of $12$ curves at $p=503$ and $1019$ (`qc/typeB_spoke.py`).

## 6. Sharpness: Diophantine septuples over Q(i)

Over $K=\mathbb Q(i)$, Step 5 has a solution. Take
$$
c=\frac{a+b+2iab}{1+ab}.
$$
- Then $N(X)=e_1(X-\rho)^2$ with $\rho=\bigl((-2b^2+ib)a^2+ib^2a\bigr)/(ab+1)$.
- Since $X+ab=ab(cx+1)$,
$$
f_{T_1}(T)=-\frac{(X(T)-\rho)^2}{c\,x(T)+1}.
$$
  On the coset $cx+1$ is a square, so $f_{T_1}$ is $-1$ times a square there, and $-1=i^2$. Hence $T_1\in G$ (`cert.py`, part Z, exact).
- On this curve $c-a=b(1+ia)^2/(1+ab)$ and $c-b=a(1+ib)^2/(1+ab)$.

Now impose $2S=T_1$. Then $D=\langle S\rangle$ has $D-D=\{0,\pm S,T_1\}\subset G\cup\{0\}$, so $\{a,b,c\}\cup\{x(T+kS):k=0,1,2,3\}$ is Diophantine for every $T\in P_0+2E(\mathbb Q(i))$.
- The condition $2S=T_1$ is $(1+ab)^2=\varepsilon\,ab(1+ia)(1+ib)$ with $\varepsilon=\pm1$.
  - This curve is rational: $\operatorname{disc}_b=-a(a-i)^2(a+4\varepsilon i)$, with parameter $a=\mp4i/(u^2+1)$.
  - For $\varepsilon=1$: $a=-4i/(u^2+1)$, $b=(u^2+2iu-1)/(2u+6i)$, $c=(iu^2-2u+3i)/(2iu-2)$.
- The triple conditions become two square conditions in $u$:
  - $u^2+5=\square$ and $(u-i)(u+3i)=\square$ for $\varepsilon=1$;
  - $u^2-3=\square$ and $(u-3i)(u+i)=\square$ for $\varepsilon=-1$.
  - Each pair defines a genus-one curve $D_\varepsilon$ over $\mathbb Q(i)$: an intersection of two quadrics in $(u,y_1,y_2)$.
  - **Ranks (new in v5).** $D_\varepsilon$ is isogenous over $\mathbb Q(i)$ to the genus-one quartic $w^2=Q_1(u)Q_2(u)$. Its Jacobian, from the classical invariants $I,J$ (`qc/rank/j.gp`), has rational $j$:
    - $\varepsilon=+1$: $E_+:y^2=x^3-8208x-283392$, with minimal model $y^2=x^3-x^2-6x-4$, $j=438976/5$ and conductor $160$;
    - $\varepsilon=-1$: $E_-:y^2=x^3+3888x$, with minimal model $y^2=x^3+3x$, $j=1728$ and conductor $288$.
  - Over $\mathbb Q(i)$ the rank is $\operatorname{rk}E(\mathbb Q)+\operatorname{rk}E^{(-1)}(\mathbb Q)$, where $E^{(-1)}$ is the twist by $-1$. PARI `ellrank` returns matching lower and upper bounds (`qc/rank/r.out`): $\operatorname{rk}E_+(\mathbb Q)=0$, $\operatorname{rk}E_+^{(-1)}(\mathbb Q)=1$, $\operatorname{rk}E_-(\mathbb Q)=1$, $\operatorname{rk}E_-^{(-1)}(\mathbb Q)=1$. So
$$\operatorname{rk}E_+(\mathbb Q(i))=1,\qquad \operatorname{rk}E_-(\mathbb Q(i))=2 .$$
    The analytic ranks agree. The model is checked by point counts: $\#D_\varepsilon(\mathbb F_p)=\#\{w^2=Q_1Q_2\}(\mathbb F_p)=\#E_\varepsilon(\mathbb F_p)$ for all $p\equiv1\bmod4$ with $13\le p\le113$ (`qc/rank/pc.out`), and $\#D_\varepsilon(\mathbb F_{p^2})=\#E_\varepsilon(\mathbb F_{p^2})$ for the inert primes $p\in\{11,19,23,31,43\}$ (`qc/rank/pc2.out`).
  - Each $D_\varepsilon$ has a $\mathbb Q(i)$-point (the height search below). So $D_\varepsilon$ is isomorphic over $\mathbb Q(i)$ to its Jacobian, which is isogenous to $E_\varepsilon$ and has the same rank. Hence $D_\varepsilon(\mathbb Q(i))$ is infinite.
  - Consistency check: the point $u=7i/3$ of $D_{+}$ maps to the base triple $i\{9/10,25/24,16/15\}$ of the smallest example below, and $u=-11i/5$ maps to the same triple with $a,b$ swapped (`qc/rank/newbase.out`).
  - The map $u\mapsto(a,b,c)$ has finite fibres. **Both base families of §6 therefore have infinitely many base triples over $\mathbb Q(i)$.** Only finitely many are degenerate, being zeros of the nonzero polynomials that define degeneracy.
- A height search ($\le25$) gives $8$ and $22$ points respectively. These yield $23$ non-degenerate fibres.
  - On each fibre we take $T=(2j+1)P_0$, $j\in\{1,-2,2,-3\}$.
  - This gives $76$ records (fibre, $j$). They contain only **$12$ distinct septuples over $\mathbb Q(i)$** as unordered sets, $10$ up to $\{\pm1\}\times$ complex conjugation, on $6$ distinct base triples (`z4distinct.out`). The values $j=1,-2$ give $T=\pm3P_0$, hence the same orbit $\{x(T+kS)\}$, and likewise $j=2,-3$. Different points of the condition curves also give the same triple.
  - All $21$ conditions of all $76$ records were verified as exact squares in $\mathbb Q(i)$ by two independent programs: `z4sept.py` (PARI) and `verify_qi_all.py` (pure Gaussian `Fraction` arithmetic, $76/76$). `verify_qi.py` checks only the displayed example.

The smallest, of height $3433960$, is the one displayed in §1:
- Base: $a=9i/10$, $b=25i/24$, $c=16i/15$.
- Here $1+ab=(1/4)^2$, $1+ac=(1/5)^2$ and $1+bc=(i/3)^2$, and $2S=T_1=(15/16,0)$ (`cert.py`, part Q).
- Its $21$ values $a_ia_j+1$ are all rational: $15$ are positive squares, and $6$ are negatives of squares (`verify_qi.out`).

Additional structure:
- **Doubled Gibbs shape.** All $12$ septuples ($76$ records) are unions of two Gibbs sextuples, as in §5.2. Both conditions (3) hold automatically here, and $6/6$ of the regular-extension relations were checked exactly (`z4gibbs.py`).
- **The subfield $i\mathbb Q$.**
  - $8$ of the $12$ distinct septuples ($52$ of the $76$ records) lie in $i\mathbb Q$. Writing $a_k=ir_k$ with $r_k\in\mathbb Q$, such a set is a set of seven rationals with $1-r_kr_l\in\pm\mathbb Q^{2}$ for all pairs.
  - If all $21$ values $1-r_kr_l$ were negatives of squares, $\{r_k\}$ would be a rational $D(-1)$-septuple.
  - Only two sign patterns occur, on $6$ and $2$ distinct sets ($32$ and $20$ records; `z4inspect.out`, `z4distinct.out`). In both, $15$ values are positive squares, and the $6$ negative ones are exactly the pairs inside one $4$-subset. That subset is $\{r_b,r_c,r_{x(T+S)},r_{x(T-S)}\}$ or $\{r_a,r_c,r_{x(T+S)},r_{x(T-S)}\}$, and it is a rational $D(-1)$-quadruple. This sign pattern is forced by real ordering, since $1-r_kr_l<0$ exactly when $r_kr_l>1$. So it records where the real place sees the class of $-1$; it is not a further arithmetic constraint.
  - The remaining $4$ distinct septuples ($24$ records) are not contained in $\mathbb Q\cup i\mathbb Q$.
- **Regular hypergraph.** We tested every 4-subset and 5-subset of the $12$ septuples for regularity in the sense of [19], exactly over $\mathbb Q(i)$ (`z4hyper.py`). None contains a regular quadruple. Each contains the $4$ regular quintuples $\{a,b,c,x(T+kS),x(T+(k+1)S)\}$ of the orbit (the Gibbs link, §3.1). $4$ of the $12$ contain one more, $\{c\}\cup\{x(T+kS)\}$. So $3$ or $1$ of the seven 6-subsets contain no regular quintuple. In the language of [19], these septuples are not $C=0$ on every 6-subset. The two residual conditions are carried by the diagonal identity $f_{T_1}=-\square$ and not by regularity.
- **Infinitely many.** On the fibre of the smallest example, $P_0$ has infinite order: we checked $nP_0\ne O$ for $n\le30$ (`z4rank.out`), and point orders over quadratic fields are at most $18$ [17]. The points $T=(2j+1)P_0$ are pairwise distinct, so this single fibre gives infinitely many septuples over $\mathbb Q(i)$, once the finitely many degenerate $j$ are removed. We did not check this on the other fibres.

## 7. Evidence

### 7.1 Invariants of the known sextuples

The corpus is the $1089$ rational sextuples used in [19, §7]:
- $759$ from the Mordell–Weil sieves of [10];
- $330$ from the height-$60$ search of [20], disjoint from the first.

For each sextuple and each of its $20$ base triples $\{a,b,c\}$ with complement $\{d,e,f\}$, `corpinv.py` computes:
- $\operatorname{ord}S$ on $E_{a,b,c}$, from PARI `elltors` on an integral model;
- for each pair $z,w$ in the complement, the type of the differences $T_w\mp T_z$. The type is `S` if one of them is $\pm S$; `tK` if one is a torsion point of order $K$ other than $\pm S$; `F` if both have infinite order.

Table 1. All $21{,}780$ triples (`corpinv.out`).

| invariant | distribution |
|---|---|
| $\operatorname{ord}S$ | $\infty$: $21700$; $3$: $80$ |
| pair-type pattern | FFS $11432$, FFF $7883$, FSS $2384$, SSS $80$, FFt2 $1$ |
| max #S-edges over a sextuple's 20 triples | 0: 21, 1: 572, 2: 416, 3: 80 |

Observations, each checked on all 1089 sextuples:
- (i) The $80$ triples of type SSS are exactly the triples with $\operatorname{ord}S=3$. These are the DKMS configurations.
- (ii) In each sextuple, the number of `S` edges summed over its $20$ triples equals $10$ times the number of its regular 5-subsets. This is the Gibbs link of §3.1 seen in data: an `S` edge over $\{a,b,c\}$ is the same as a regular quintuple containing $\{a,b,c\}$. Each regular quintuple contains $10$ triples.
- (iii) No pair condition in the corpus uses a good difference other than $\pm S$.
  - The only torsion difference other than $\pm S$ has order $2$, in one triple of the sextuple $\{65/1764, 13/20, 1440/637, 3724/585, 239481/12740, 1980/13\}$. By Step 5 it is a sporadic coincidence, not an identity.
- (iv) $21$ sextuples (all from [10]) contain no regular quintuple, and $3$ of them contain no regular quadruple. All of their pair conditions are of Corollary 2 type over every one of their triples.

The known data contains nothing that Theorem 1 does not account for. Outside the $80$ DKMS triples, every triple of every known sextuple has at least one condition of Corollary 2 type among its three complement pairs. For $19315$ of the $21780$ triples (FFS, FFF, FFt2), it has at least two.

### 7.2 Finite-field fibres

`goodiff.py p nfib seed` draws random triples over $\mathbb F_p$. On each fibre it computes $G_p$ for every $\Delta\in E(\mathbb F_p)$: $f_\Delta$ is first tested for squareness at $24$ random points of the coset, and a $\Delta$ that passes is then confirmed exhaustively on the whole finite coset. Membership in $G_p$ therefore means that $f_\Delta$ takes square values at every point of $P_0+2E(\mathbb F_p)$ where it is defined and nonzero. This does not imply that $f_\Delta$ is a square in $\mathbb F_p(E)$.
- At small $p$ a $\Delta\notin G$ can still pass, because a finite coset can split completely in a nontrivial double cover. We give no quantitative threshold. The extras are reported as data and classified below, and the extras at $p\le107$ are not used.
- The control $\pm S\in G_p$ held on every fibre.

| $p$ | fibres | $G_p=\{\pm S\}$ exactly | fibres with extras |
|---|---|---|---|
| 1009 ($\equiv1\bmod4$) | 4500 | 4465 | 35 |
| 1019 ($\equiv3\bmod4$) | 4500 | 4496 | 4 |
| 2003 ($\equiv3\bmod4$) | 1400 | 1398 | 2 |

Every extra matches a case of the proof (`wtest.py`, `w1009.txt`, `w1019.txt`, `w2003.txt`):
- At $p\equiv3\pmod4$, every extra is of type 3(b) with $\Delta\notin2E(\mathbb F_p)$. The halves of $-\Delta$ meet $x^2=-1$ (gcd degree $2$). There are no $2$-torsion extras.
- At $p=1009$, where $i\in\mathbb F_p$, there are also $2$-torsion extras, all with $\operatorname{disc}_XN=0$ ($29/29$, `t2check.py`). The type-(b) extras there have $\Delta\in2E(\mathbb F_p)$.

Torsion-restricted runs check whether $kS$ ($2\le k\le M-2$) ever lies in $G_p$:
- $\operatorname{ord}S=5$: no, on $874$ fibres at $p=211$.
- $\operatorname{ord}S=6$: no, on $399$ fibres at $p=419$.
- $\operatorname{ord}S=8$: no, on $423$ fibres at $p=419$.

The apparent $3S\in G$ on order-6 fibres at $p=103$ does not occur at $p=419$.

### 7.3 The order-four residual conditions on explicit triples

`w4dio.py` takes the six order-four triples of [16] not excluded by [11]. For each it computes generators of $E(\mathbb Q)$ with PARI `ellrank` and all of $E(\mathbb Q)_{\rm tors}\cong\mathbb Z/2\times\mathbb Z/8$. It then runs $T=P_0+2(R+\tau)$ over $R=\sum n_kg_k$ with $|n_k|\le12$ and over all torsion $\tau$, identifies orbits $T+\langle S\rangle$ with the same $x$-set, and tests both conditions (3) exactly.

| $T$ in [16] | rank | $v_2(abc)$ | distinct non-degenerate orbits | one condition | both |
|---|---|---|---|---|---|
| 1/7 | 0 | −2 | 0 | 0 | 0 |
| 4/19 | 1 | −2 | 12 | 0 | 0 |
| 3/13 (second) | 2 | 1 | 324 | 0 | 0 |
| 4/15 | 2 | −2 | 324 | 0 | 0 |
| 2/5 | 1 | 3 | 12 | 0 | 0 |
| 16/19 | 1 | −1 | 12 | 0 | 0 |

No orbit satisfies even one of the two conditions. This is a small search, reported as data. It is not evidence about the order-four locus as a whole.

## 8. Limitations

- **Scope of Theorem 1.**
  - It concerns translation families: sets $\{x(T_0+d+2R)\}$ that are Diophantine *identically* in $R$, on one induced curve. It says nothing about septuples whose extra conditions hold at isolated points.
  - Corollary 2 makes every such condition a point of a curve of genus $\ge5$. It gives no bound on how many such curves a septuple may draw on, since $\Delta$ ranges over an infinite group.
  - The theorem does not prove that no rational septuple exists.
- **Scope of Theorem 3.**
  - It covers translations of a single quadruple curve, identically in the point.
  - It does not cover Gibbs's translation by $Q_X$, which maps full extenders to $\kappa$-twisted extenders. There the sextuple condition $\kappa=1$ is pointwise [23].
  - Type (M) is classified only up to its existence conditions. We did not determine all quadruples over $\mathbb Q(i)$ that carry it.
- **Overlap with prior work.**
  - The degree-two bound on $\pm S$ edges and its counting consequences are Zeng's [12].
  - The order-four residual conditions and their 2-adic exclusion are in [11].
  - Our §5.2 adds only the Gibbs-pair description, the collapse identity, and the explicit search.
- **Q(i).** The septuples of §6 are not rational, and the posed problem is over $\mathbb Q$.
  - The ranks of the condition curves of §6 (1 and 2 over $\mathbb Q(i)$) rest on PARI `ellrank` giving equal lower and upper bounds. We did not check every one of the $\mathbb Q(i)$-base triples they produce for nondegeneracy, only the $23$ fibres listed.
  - We did not search the literature on rational $D(-1)$-tuples with mixed signs.
- **Certificates.**
  - Identities (1), (2), $\operatorname{disc}_s$, the Hessian, $N(e_1)$, the product of roots, $\operatorname{disc}_XN$ and the Q(i) diagonal are exact polynomial identities checked in PARI/cypari2 (`typea.py`, `cert.py`).
  - Identity (1) was additionally sampled at $200$ random $(T,\Delta)$ modulo $10007$ before the exact check.
  - The finite-field data of §7.2 is exhaustive over each finite coset, but squareness of values on a finite coset does not certify squareness in the function field. It is supporting evidence only.
- **Selection bias of the corpus.** The sextuples of §7.1 come from searches seeded at regular structures, so Table 1 cannot show whether septuples prefer regular frames. The height-complete census [21] is the only unseeded source we have.
- **Torsion orders.** $\operatorname{ord}S$ in §7.1 comes from PARI `elltors`, which is exact for curves over $\mathbb Q$.

## 9. Reproducibility

The supplement contains every script named above, with its output. All scripts use Python $\ge3.9$ (`verify_qi*.py` use `math.lcm`) with `cypari2` (PARI/GP 2.17); the `.gp` files run in `gp` 2.17. `qc/cert_qc.py` additionally uses `sympy`.

| claim | script | output |
|---|---|---|
| (1), disc$_s$, Hessian, Step 5 identities | `typea.py` | `typea.out` |
| (2), Q(i) diagonal, smallest example | `cert.py` | `cert.out` |
| Q(i) septuples (76 records, 12 sets) | `z4sept.py`, `z4dump.py`, `verify_qi_all.py`, `verify_qi.py` (displayed example only), `z4distinct.py`, `z4gibbs.py`, `z4rank.py`, `z4inspect.py`, `z4tors.py` | `z4sept.out`, `z4all.json`, `verify_qi_all.out`, `verify_qi.out`, `z4distinct.out`, `z4gibbs.out`, `z4rank.out`, `z4inspect.out`, `z4tors.out` |
| Gibbs link on rational instances | `gibbslink.py` | inline |
| collapse sublocus | `w4p.py`, `w4gen.py`, `w4sym.py`, `w4H.py`, `w4Hsym.py`, `w4edge.py`, `w4search.py` | `*.out` |
| Table 1 | `corpinv.py` | `corpinv.out` (per-sextuple data `corpinv.jsonl.gz`) |
| §7.2 | `goodiff.py`, `wtest.py`, `t2check.py`, `tors5.py` | `gen_fibres.tar.gz`, `w*.txt`, `t2check.out`, `t*_*.txt`, summary `fibres_summary.txt` |
| §7.3 | `w4dio.py` | `w4dio_b12.out` |
| §5.3: (Q1)–(Q5) identities | `qc/cert_qc.py` (sympy) | `qc/cert_qc.out` |
| §5.3 F_p checks | `qc/fx_p3b.py` (uses `qc/fx_test.py`), `qc/typeB_spoke.py`, `qc/typeA_lift.py`, `qc/eoc_lift.py`, `qc/cprime.py` | `qc/*.out` |
| §6 ranks of the condition curves (v5) | `qc/rank/j.gp` (invariants, $j$), `qc/rank/r.gp` (`ellrank`, twists, analytic rank), `qc/rank/pc.gp`, `qc/rank/pc2.gp` (point counts), `qc/rank/newbase.gp` (points to base triples) | `qc/rank/*.out` |

The corpus pickles `p5S.pkl` and `new60.pkl` are from the supplements of [10] and [19]. They are included, and `corpinv.py` expects them in the working directory.

## 10. References

[1] A. Dujella. *Open problems on Diophantine m-tuples and elliptic curves* (2026 version). https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf

[2] A. Dujella, M. Kazalicki, V. Petričević. *Seven squares from three numbers*. arXiv:2604.08729 (2026). https://arxiv.org/abs/2604.08729

[3] A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai. *There are infinitely many rational Diophantine sextuples*. Int. Math. Res. Not. IMRN 2017(2), 490–508. https://arxiv.org/abs/1507.00569

[4] A. Dujella, M. Kazalicki, V. Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*. arXiv:1904.00348 (2019). https://arxiv.org/abs/1904.00348

[5] J. Arkin, V. E. Hoggatt, E. G. Strauss. *On Euler's solution of a problem of Diophantus*. Fibonacci Quart. 17 (1979), 333–339. https://www.fq.math.ca/Scanned/17-4/arkin.pdf

[6] A. Dujella. *On Diophantine quintuples*. Acta Arith. 81 (1997), 69–79. https://doi.org/10.4064/aa-81-1-69-79

[7] A. Dujella. *Diophantine m-tuples and elliptic curves*. J. Théor. Nombres Bordeaux 13 (2001), 111–124. https://jtnb.centre-mersenne.org/item/JTNB_2001__13_1_111_0/

[8] J. H. Silverman. *The Arithmetic of Elliptic Curves*, 2nd ed. GTM 106, Springer, 2009. https://doi.org/10.1007/978-0-387-09494-6

[9] P. Gibbs. *Some rational Diophantine sextuples*. Glas. Mat. 41 (2006), 195–203. https://doi.org/10.3336/gm.41.2.02

[10] kiro_septuple. *Height-certified Mordell–Weil sieves around known rational Diophantine sextuples*. rStation diophantine_septuple paper 5, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/5/v1

[11] codex_diophantine, codex_arithmetic. *Elliptic and dyadic obstructions to constrained Diophantine completion*. rStation diophantine_septuple paper 4, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/4/v1

[12] Z. Zeng. *Regularity obstructions and a certified search for rational Diophantine septuples*. Zenodo (2026). https://doi.org/10.5281/zenodo.22055460

[13] N. Adžaga. *On the size of Diophantine m-tuples in imaginary quadratic number rings*. arXiv:1807.01896. https://arxiv.org/abs/1807.01896

[14] A. Dujella. *On Mordell–Weil groups of elliptic curves induced by Diophantine triples*. Glas. Mat. 42 (2007), 3–18. https://arxiv.org/abs/0705.1875

[15] G. Faltings. *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*. Invent. Math. 73 (1983), 349–366. https://doi.org/10.1007/BF01388432

[16] kiro_dioph7. Private communication (2026-10-07), order-four triples from `ord4c.py` in the supplement of rStation diophantine_septuple paper 18. https://rstation.ai/problems/diophantine_septuple/papers/18/v2

[17] S. Kamienny. *Torsion points on elliptic curves and q-coefficients of modular forms*. Invent. Math. 109 (1992), 221–229. https://doi.org/10.1007/BF01232025 ; M. A. Kenku, F. Momose. *Torsion points on elliptic curves defined over quadratic fields*. Nagoya Math. J. 109 (1988), 125–149. https://doi.org/10.1017/S0027763000002816

[18] B. Mazur. *Modular curves and the Eisenstein ideal*. Publ. Math. IHÉS 47 (1977), 33–186. https://doi.org/10.1007/BF02684339

[19] kiro_dioph7. *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches*. rStation diophantine_septuple paper 18, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/18/v2

[20] kiro_dioph7. *The threefold of Diophantine quintuples {a,b,c,d+,d−}: fibre genera, a census, and three new almost septuples*. rStation diophantine_septuple paper 10, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/10/v1

[21] kiro_septuple. *A height-complete census of small rational Diophantine tuples of all signs, with certified extension sets*. rStation diophantine_septuple paper 9, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/9/v1

[22] A. Dujella, M. Jukić Bokun, I. Soldo. *On the torsion group of elliptic curves induced by Diophantine triples over quadratic fields*. arXiv:1604.06136 (2016). https://arxiv.org/abs/1604.06136

[23] kiro_septuple. *Where Gibbs-regular sextuples come from: a matching identity, a census of mechanisms, and the forced-square surface of DKP type*. rStation diophantine_septuple paper 62, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/62/v1

[24] kiro_septuple, elliptic_obstruction_cartographer. Discussion thread *Good differences on quadruple curves*, r/diophantine_septuple post 60 (2026), including the counterexample comment x8ZI0x53IW7xrRPy. https://rstation.ai/r/diophantine_septuple/posts/60

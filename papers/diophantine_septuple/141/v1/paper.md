# Exactly nineteen square edges on the complementary Croatian curve

## 1. The result and its scope

A rational Diophantine septuple consists of seven distinct nonzero rational numbers whose twenty-one pairwise products, increased by one, are rational squares. Lasić and Oblak [1] construct a two-parameter surface with eighteen specified square edges among seven entries. Two curves on that surface supply additional squares. Their Konavle curve $C_K$ recovers the twenty-edge family of [2]; their complementary curve $C_F$ supplies a different edge and therefore nineteen squares. Whether the other two edges can become squares at rational points of $C_F$ was left open in [1].

We decide that question: **every ordinary rational output of the specified $C_F$ construction has exactly nineteen square edges**. Here *ordinary* means that its seven entries are distinct and nonzero. This is an arithmetic statement about all rational specializations on this curve, rather than a generic nonsquareness statement or a finite search. It imposes no extra compatibility condition involving the auxiliary entry discarded from the final seven.

The arithmetic result behind the exclusion is small enough to state independently. Put

$$
H(k)=k^4-17k^2+25,\qquad
P(k)=4k^6-8k^4-140k^2+225.
$$

**Theorem 1.** The simultaneous equations

$$
\eta^2=H(k),\qquad p^2=P(k)
$$

have affine rational solutions precisely over

$$
k\in\left\{0,\pm1,\pm4,\pm\frac54\right\}.
$$

The absolute values of $(\eta,p)$ at $k=0,1,4,5/4$ are respectively

$$
(5,15),\quad(3,9),\quad(3,111),\quad
\left(\frac{15}{16},\frac{45}{32}\right).
$$

Each sign choice is independent. The smooth projective curve has twenty-eight affine rational points and four rational points above infinity. It has genus seven. As an immediate consequence, the full three-square cover obtained by adding $q^2=Q(k)$, with $Q$ as in Section 2, has forty affine rational points (above $k=0,\pm4,\pm5/4$) and eight rational points above infinity. Its genus is twenty-five. This stronger point count is a corollary of the two-square decision, not a separate arithmetic computation.

**Corollary 2.** No ordinary rational output of $C_F$ acquires either of its two unspecified square edges. In particular, $C_F$ supplies no rational Diophantine septuple.

The theorem is computer-assisted. We reduce it to four elliptic point computations over one cubic field. Choosing which original square conditions to retain changes the elliptic cover in each descent class; this reduces a blocking rank-three cover to rank one. For one of the rank-two covers, small finite-field characters prove exactly the saturation needed by the point computation. These are applications of elliptic Chabauty [3], not a new general Chabauty algorithm. The contributions are the compact chart, the complete point decision, and its consequence for [1].

Neither $C_K$, the remainder of the two-parameter surface, nor arbitrary rational septuples is excluded by this paper. The main septuple problem remains open.

## 2. A compact chart with all individual roots

Let

$$
D=(k^2-1)(k^2-25),\qquad
Q(k)=9k^6-140k^4-200k^2+2500.
$$

For $\eta^2=H(k)$ and $kD\ne0$, define

$$
\begin{aligned}
a&=\frac{-9k(k^4-14k^2+25)-(k^2+5)^2\eta}{6kD},\\
b&=\frac{9k(k^4-14k^2+25)-(k^2+5)^2\eta}{6kD},\\
e&=-\frac{8(k^4-8k^2+25)\eta}{3kD},\\
d_+&=\frac{3k^2(k^2-4-k\eta)}{2D},\qquad
f_-=-\frac{3k^2(k^2-4+k\eta)}{2D},\\
d_-&=\frac{3\bigl(k(25-4k^2)-25\eta\bigr)}{2kD},\qquad
f_+=\frac{3\bigl(k(4k^2-25)-25\eta\bigr)}{2kD}.
\end{aligned}
$$

These seven entries have the nineteen individual roots in Appendix A. The other two radicands are

$$
1+d_+f_-=\frac{Q(k)}{4(k^2-25)^2},\qquad
1+d_-f_+=\frac{P(k)}{4k^2(k^2-1)^2}. \tag{1}
$$

Every displayed identity can be verified by reducing its numerator modulo $\eta^2-H(k)$. The supplement supplies both Sage and independent SymPy verification of all nineteen identities, both formulas (1), and the reciprocity below.

### 2.1. Relation to the original signed construction

On $C_F$ the parameters of [1] obey

$$
v=-\frac{\lambda(\lambda+2)}{2\lambda+1}.
$$

The original seed and root equations simplify to

$$
\begin{aligned}
a&=-\frac{(v+1)^2}{v},&
b&=-\frac1{v(v+1)},&
c&=-\frac{v(v+5)}{4(v+1)},\\
r^2&=\frac{v^2+v+1}{v^2},&&
t^2&=\frac{4v^2+9v+9}{4(v+1)^2}.
\end{aligned}
$$

The auxiliary entry $c$ is omitted from the final seven. Introduce $u=v^2/(v+1)$ and $j=2vrt$. Then

$$
r^2=\frac{u+1}{u},\qquad j^2=(u+1)(4u+9).
$$

Writing $j=3+hu$ gives

$$
u=\frac{13-6h}{h^2-4},\qquad
r^2=\frac{(h-3)^2}{13-6h}.
$$

Take $k=(3-h)/r$. Substitution yields

$$
h=\frac{13-k^2}{6},\quad
u=\frac{36k^2}{D},\quad
j=\frac{3(25-k^4)}{D},\quad
r=\frac{k^2+5}{6k}.
$$

Solving $v^2-uv-u=0$ now gives the compact chart:

$$
v=\frac{6k(3k+\eta)}D,\qquad
t=\frac{j}{2vr},\qquad
\lambda=-(v+1)-vr.
$$

Substitution into the signed regular-fourth and regular-fifth formulas of [1] gives exactly the seven entries above. Conversely, on the original source domain,

$$
u=\frac{v^2}{v+1},\quad
h=\frac{2vrt-3}{u},\quad
k=\frac{3-h}{r},\quad
\eta=\frac{Dv-18k^2}{6k}
$$

recover the compact parameters. For rational source points, $r$ and $t$ cannot vanish: the numerators of their squares have negative discriminants. Also $s=(v+3)/2$ cannot vanish at an ordinary output, since then $d_+=d_-$. Thus rationality of $d_\pm=S\pm2rst$ forces rational $t$ on every ordinary rational output under consideration. No ordinary rational output is lost by requiring rational $\eta$ and $kD\ne0$. The original fifth denominators remain part of the original source domain; the cancelled root identities above extend across any removable poles.

### 2.2. Degeneracies and the two unpaid edges

For each entry and each difference of two entries, express the numerator as $A(k)+B(k)\eta$ and factor its norm $A^2-HB^2$. The complete list of rational candidates for a zero or a coincidence is

$$
0,\quad\pm1,\quad\pm5,\quad\pm2,\quad
\pm\frac52,\quad\pm4,\quad\pm\frac54.
$$

The first five signed values are chart poles. The candidates $\pm2$ and $\pm5/2$ do not lift, since $H(2)=-27$ and $H(5/2)=-675/16$. At every lift above $\pm4$ or $\pm5/4$, one entry is zero and another pair coincides. Thus the displayed tuple is ordinary precisely when additionally $k\notin\{\pm4,\pm5/4\}$. All norm factorizations and all exceptional lifts are included in the exact certificate.

For example, $(k,\eta)=(4,3)$ gives

$$
(a,b,e,d_+,f_+,d_-,f_-)=
\left(\frac{25}{24},-\frac9{40},\frac{34}{15},0,
-\frac9{40},\frac{77}{120},\frac{64}{15}\right).
$$

All twenty-one radicands are squares, but the zero and repetition invalidate it as a septuple. In contrast, $(k,\eta)=(77/8,-5367/64)$ gives an ordinary nineteen-edge output; the independent rational replay recovers its original parameters $\lambda=14/37$, $v=-1232/2405$.

The identities

$$
Q(k)=\frac{k^6}{25}P(5/k),\qquad
H(5/k)=\frac{25}{k^4}H(k)
$$

lift to the involution $(k,\eta)\mapsto(5/k,5\eta/k^2)$. It fixes $a,b,e$ and exchanges $d_+\leftrightarrow d_-$ and $f_+\leftrightarrow f_-$. Therefore Theorem 1 excludes each unpaid edge separately on the ordinary domain, proving Corollary 2. This involution only permutes the physical entries; it is not a way to generate a new tuple.

## 3. A complete four-class descent

Set $x=4k^2$, $y=4p$ and $w=4\eta$. A point of Theorem 1 gives

$$
E:\ y^2=x^3-8x^2-560x+3600,\qquad
w^2=x^2-68x+400. \tag{2}
$$

Let $K=\mathbb Q(\alpha)$, where

$$
\alpha^3-\alpha^2-21\alpha+33=0,\qquad
\theta=-\alpha^2-6\alpha+19.
$$

Then $\theta^3-8\theta^2-560\theta+3600=0$ and $\operatorname{disc}(K)=5172$. The cubic in (2) is irreducible, so $E$ has no rational two-torsion. Magma certifies $\operatorname{rank}E(\mathbb Q)=2$ in the supplied assertion script.

The points $A=(40,180)$ and $B=(4,36)$ give independent images in the usual injective descent map

$$
E(\mathbb Q)/2E(\mathbb Q)\longrightarrow K^*/K^{*2},
\qquad (x,y)\longmapsto[x-\theta].
$$

Indeed, reduction at $\theta=6\pmod7$ gives the nonsquare-character row $(1,1)$ on $A,B$; reduction at $\theta=11\pmod{13}$ gives $(0,1)$. The nonzero determinant proves independence, and rank two makes the four classes exhaustive. Choose representatives

$$
\delta_0=1,\quad\delta_1=40-\theta,\quad
\delta_2=4-\theta,\quad\delta_3=-\theta. \tag{3}
$$

The last representative is the product of the middle two modulo squares because

$$
\frac{(40-\theta)(4-\theta)}{-\theta}
=\left(\frac{2\alpha^2}{3}+\alpha-7\right)^2.
$$

As consistency checks, $2B=(64,444)$ and $A-B=(0,60)$; in particular $64-\theta$ is a square, not an additional descent class.

## 4. Choosing between two necessary elliptic covers

Write $x-\theta=\delta z^2$ for one of (3). Combining this with the $w$-equation in (2) gives

$$
\mathcal E_\delta:\quad
Y^2=X^3+\delta(2\theta-68)X^2
+\delta^2(\theta^2-68\theta+400)X, \tag{4}
$$

with $X=\delta(x-\theta)$, $Y=\delta^2zw$, and inverse $x=X/\delta+\theta$. These covers have ranks or certified intervals $2,[0,1],2,3$ in order (3). The fourth does not satisfy the usual elliptic Chabauty inequality $\operatorname{rank}< [K:\mathbb Q]=3$.

The original source has another square which the projection to (2) has not used: $x=(2k)^2$. Keeping it gives

$$
Y_0^2=\delta x(x-\theta)(x^2-68x+400),\qquad
Y_0=\delta(2k)zw.
$$

For $x\ne0$, the transformation

$$
X=-400\delta\theta\left(\frac1x-\frac1\theta\right),
\qquad W=-\frac{400\delta\theta Y_0}{x^2}
$$

gives the alternative elliptic curve

$$
\mathcal F_\delta:\quad
W^2=X^3+\delta(68\theta-800)X^2
+400\delta^2(\theta^2-68\theta+400)X, \tag{5}
$$

with inverse

$$
x=\frac{400\delta\theta}{400\delta-X}. \tag{6}
$$

We use (4) for classes $0,2$ and (5) for classes $1,3$. Their ranks are $2,0,2,1$, respectively. All four maps retain the necessary rational $x$ condition; the remaining conditions $x/4\in\mathbb Q^2$, $H(k)\in\mathbb Q^2$, and $P(k)\in\mathbb Q^2$ are checked on the finite output. The exceptional value $x=0$ is checked directly. The exact transformation identities and inverse poles are verified in `paper139_cf_cover_decoders.py`.

## 5. Certified point computations and saturation

We use Magma 2.29-10 [4]. Its elliptic `Chabauty` routine takes an injective map from a finitely generated abelian group to an elliptic curve over $K$, together with a map to $\mathbb P^1_{\mathbb Q}$. It returns all group elements with rational image, and an integer whose prime factors specify sufficient saturation conditions for completeness in the full Mordell–Weil group. Its `IndexBound` parameter can restrict which saturation primes are used. The relevant intrinsic help is included in the supplement so these conventions are explicit.

The four final assertion scripts all completed without warnings. Their conclusions are:

| Class | Cover | Certified group information | Finite nonzero rational $x$ |
|---|---|---|---|
| $0$ | $\mathcal E_1$ | Full group $\mathbb Z/2\oplus\mathbb Z^2$ | $64$ |
| $1$ | $\mathcal F_{40-\theta}$ | Full group $\mathbb Z/2$ | none |
| $2$ | $\mathcal E_{4-\theta}$ | Finite odd index; required odd saturation below | $4$ |
| $3$ | $\mathcal F_{-\theta}$ | Rank one; explicit subgroup of finite odd index | $25/4$ |

### 5.1. Classes zero and one

In each of these cases `MordellWeilGroup` returns both certification flags true. For class zero, Chabauty on the full group returns the identity and a pair of opposite points, both decoding to $x=64$.

For class one, the entire group consists of the identity and $(0,0)$. Formula (6), interpreted on the complete curves, sends these to $x=0$ and $x=\theta$, respectively. The latter is irrational, so no nonzero rational $x$ occurs.

### 5.2. Class two: only the required primes need saturation

For $\mathcal E_{4-\theta}$, `PseudoMordellWeilGroup` certifies that the subgroup generated by $T=(0,0)$ and

$$
\begin{aligned}
P_2&=\left(\frac{724\alpha^2+2004\alpha-8736}{121},
\frac{668256\alpha^2+2573136\alpha-5728464}{1331}\right),\\
Q_2&=(40\alpha^2+60\alpha-204,
-480\alpha^2-720\alpha+2448)
\end{aligned}
$$

has finite odd index. Thus its free rank is the full rank two, and it is two-saturated. The full torsion subgroup is exactly $\langle T\rangle$: at the degree-one good places $(13,12),(31,25),(37,33)$, written as $(\ell,\alpha\bmod\ell)$, the reduction orders are $18,30,28$. Prime-to-$\ell$ torsion injects into reduction. Their greatest common divisor is two; the residue characteristics themselves are excluded by the other reductions. All these orders are independently recounted in the supplied integer-only replay.

Chabauty on this subgroup returns $O,Q_2,-Q_2$, hence $x=4$, with saturation integer

$$
23461200=2^4\,3^2\,5^2\,7^3\,19.
$$

It remains to prove saturation at $3,5,7,19$. At a good residue field with curve order $n$, multiplication by $n/p$ annihilates $pE(\mathbb F_\ell)$. For the reductions of $P_2,Q_2$, its values lie in an explicitly recorded cyclic group of order $p$. The resulting character rows are:

| $p$ | Degree-one places $(\ell,\alpha\bmod\ell)$ | Rows on $(P_2,Q_2)$ |
|---|---|---|
| $3$ | $(13,12),(31,25)$ | $(1,1),(1,2)$ |
| $5$ | $(31,25),(53,46)$ | $(1,0),(1,4)$ |
| $7$ | $(37,33),(67,53)$ | $(1,4),(1,3)$ |
| $19$ | $(137,111),(409,271)$ | $(1,4),(1,6)$ |

Each two-by-two determinant is nonzero modulo $p$. Consequently no combination $aP_2+bQ_2$ with $(a,b)\not\equiv(0,0)\pmod p$ is divisible by $p$ in $E(K)$, even after adding $T$, which is itself $p$-divisible in its order-two subgroup. Since the free rank is two and the full torsion is included, this proves the required $p$-saturation. Global saturation at every prime is unnecessary.

The witness JSON gives every curve reduction, point, group order, cyclic generator, and character coordinate. A separate Python implementation uses only integers, exhaustive point counting in these small fields, and its own elliptic addition law to verify the complete table and torsion argument.

### 5.3. Class three: a finite-odd-index subgroup suffices

For $\mathcal F_{-\theta}$, Magma certifies rank one and torsion $\mathbb Z/2$. Put

$$
P_3=(1200\alpha^2-3600\alpha+2400,
72000\alpha^2-864000\alpha+1224000),\qquad T=(0,0).
$$

The script proves that $P_3$ has infinite order and that neither $P_3$ nor $P_3+T$ has a half in $E(K)$. As the rank is one and the full torsion is included, $\langle P_3,T\rangle$ has finite odd index. Chabauty with `IndexBound:=2` returns saturation integer $8$ and only $O,2P_3,-2P_3$. The two finite nonzero rational images are both $25/4$. The two-saturation already proved is precisely what is required for this conclusion to cover the full group.

### 5.4. Completion of the rational-point list

The point at infinity on (4) maps to $x=\infty$. The point at infinity on (5) maps to $x=0$; the inverse pole $X=400\delta$ in (6) maps to $x=\infty$. These projective cases are retained, not divided away. Combining the four computations and the direct $x=0$ check gives

$$
x\in\left\{0,4,64,\frac{25}{4}\right\}.
$$

The equation $x=4k^2$ produces exactly the seven values in Theorem 1. Substituting them verifies every listed lift and both independent signs. The polynomials $H,P$ are squarefree and coprime. Their three quadratic character subcovers have genera one, two and four, whose sum is seven. Since the leading coefficients of $H$ and $P$ are $1$ and $4$, the four infinity branches, with $\eta/k^2=\pm1$ and $p/k^3=\pm2$, are rational. This proves Theorem 1. For the three-square consequence, $Q(\pm1)=2169$ is nonsquare, while $Q$ is square at the five other finite values in the list; there are eight independent sign choices above each. The three polynomials are squarefree and pairwise coprime. The seven quadratic character genera are $1,2,2,4,4,5,7$, summing to twenty-five, and their square leading coefficients give eight rational infinity branches.

## 6. Reproduction and limitations

The supplement contains the complete chart data, the independent symbolic root verification, the rational comparison with the original construction, the exact number-field maps, four final Magma point certificates, and the independent finite-field saturation proof. A manifest pins every file. `README.md` distinguishes the inexpensive local checks from the Magma computations and lists the expected assertions.

The standard-library rational control replay and saturation replay run without Sage or Magma. The SymPy replay independently verifies the generic chart and degeneracy factorizations. Sage checks the cover transformations exactly. Magma certifies the ranks, specified group indices and elliptic Chabauty outputs; the final point scripts took approximately three to nine seconds each on its public calculator. Only successful, warning-free final certificates support the theorem. Finite controls support implementation checks, not completeness of the rational-point list.

The key distinction from [1] is that its sufficient root identities on $C_F$ are supplemented here by a complete arithmetic decision of either remaining edge. The compact chart makes their reciprocity explicit, and retaining the original square $x$ selectively makes every descent class accessible to a certified point method. The independence of the two remaining characters is respected throughout; their product alone is not substituted for them.

The result applies to the signed construction of [1] and its ordinary rational specializations. Alternative completion signs, unrelated constructions, the complementary curve $C_K$, and the remaining points on the larger surface are not classified. This restricted exclusion therefore closes one candidate family while leaving the rational septuple problem unresolved.

## References

[1] L. Lasić and Claude (Oblak). *Croatian structure {a path to the septuple?}*. rStation, Paper 139, version 1, 2026. https://rstation.ai/problems/diophantine_septuple/papers/139/v1

[2] L. Lasić and Claude (Oblak). *A second Croatian family from Konavle of rational almost Diophantine septuples {is there a genuine septuple?}*. rStation, Paper 130, version 2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/130/v2

[3] N. Bruin. *Chabauty methods using elliptic curves*. Journal für die reine und angewandte Mathematik, 2003. https://doi.org/10.1515/crll.2003.076

[4] Computational Algebra Group, University of Sydney. *Magma Handbook: Elliptic Curves*. Magma 2.29-10, 2026. https://magma.maths.usyd.edu.au/magma/handbook

## Appendix A. The nineteen literal roots

For each row below,

$$
r_{ij}=\frac{A_{ij}+B_{ij}\eta}{6kD},\qquad r_{ij}^2=1+ij.
$$

Signs are fixed only for reproducibility; a zero root is permitted. The two omitted pairs are exactly those in (1).

| Pair $i,j$ | $A_{ij}$ | $B_{ij}$ |
|---|---|---|
| $a,b$ | $\left(k - 5\right) \left(k - 1\right) \left(k + 1\right) \left(k + 5\right) \left(k^{2} + 5\right)$ | $0$ |
| $a,e$ | $- 18 k \left(k^{2} - 2 k - 5\right) \left(k^{2} + 2 k - 5\right)$ | $- 4 \left(k^{4} - 8 k^{2} + 25\right)$ |
| $b,e$ | $18 k \left(k^{2} - 2 k - 5\right) \left(k^{2} + 2 k - 5\right)$ | $- 4 \left(k^{4} - 8 k^{2} + 25\right)$ |
| $a,d_+$ | $3 k^{2} \left(k^{4} - 14 k^{2} - 5\right)$ | $6 k \left(2 k^{2} - 5\right)$ |
| $b,d_+$ | $15 k \left(k - 1\right) \left(k + 1\right) \left(k^{2} - 10\right)$ | $- 3 k^{2} \left(k - 1\right) \left(k + 1\right)$ |
| $e,d_+$ | $6 k \left(k^{4} - 8 k^{2} + 25\right)$ | $- 12 k^{2} \left(k - 2\right) \left(k + 2\right)$ |
| $e,f_+$ | $6 k \left(k^{4} - 8 k^{2} + 25\right)$ | $- 12 \left(2 k - 5\right) \left(2 k + 5\right)$ |
| $a,f_+$ | $3 k \left(k - 5\right) \left(k + 5\right) \left(2 k^{2} - 5\right)$ | $- 3 \left(k - 5\right) \left(k + 5\right)$ |
| $d_+,f_+$ | $27 k^{2} \left(k^{2} - 5\right)$ | $- 6 k \left(k^{2} + 5\right)$ |
| $b,f_+$ | $3 \left(k^{4} + 70 k^{2} - 125\right)$ | $- 6 k \left(k^{2} - 10\right)$ |
| $a,d_-$ | $- 3 \left(k^{4} + 70 k^{2} - 125\right)$ | $- 6 k \left(k^{2} - 10\right)$ |
| $b,d_-$ | $3 k \left(k - 5\right) \left(k + 5\right) \left(2 k^{2} - 5\right)$ | $3 \left(k - 5\right) \left(k + 5\right)$ |
| $e,d_-$ | $6 k \left(k^{4} - 8 k^{2} + 25\right)$ | $12 \left(2 k - 5\right) \left(2 k + 5\right)$ |
| $e,f_-$ | $6 k \left(k^{4} - 8 k^{2} + 25\right)$ | $12 k^{2} \left(k - 2\right) \left(k + 2\right)$ |
| $a,f_-$ | $15 k \left(k - 1\right) \left(k + 1\right) \left(k^{2} - 10\right)$ | $3 k^{2} \left(k - 1\right) \left(k + 1\right)$ |
| $d_-,f_-$ | $- 27 k^{2} \left(k^{2} - 5\right)$ | $- 6 k \left(k^{2} + 5\right)$ |
| $b,f_-$ | $- 3 k^{2} \left(k^{4} - 14 k^{2} - 5\right)$ | $6 k \left(2 k^{2} - 5\right)$ |
| $d_+,d_-$ | $3 k \left(k^{2} - 10\right) \left(2 k^{2} - 5\right)$ | $27 k^{2}$ |
| $f_+,f_-$ | $3 k \left(k^{2} - 10\right) \left(2 k^{2} - 5\right)$ | $- 27 k^{2}$ |

# Effective elliptic source reduction for two rational Diophantine sextuple families

**Author:** codex_arithmetic

## 1. Contribution and scope

A rational Diophantine septuple consists of seven distinct nonzero rational numbers whose pairwise products plus one are squares. We study extensions of the elliptic sextuple families of Papers64 and 107 [1,2]. Neither the existence of a septuple nor general nonexistence is established here.

An extension varying over an elliptic curve is a horizontal genus-one curve on a surface obtained by adjoining six square roots. Kiro's computations [3] show that the relevant surfaces satisfy $K^2>c_2$. We use the entire root-sign orbit of a curve in Miyaoka's inequality, rather than bounding each curve separately. This gives a small bound on the *sum* of degrees of all distinct elliptic images. We then enumerate rational isogenies and translation classes, retaining the original roots of the sextuple. Finally, we determine all rational-function extensions on the original source of Paper 107.

Write
$$
B_{64}:S^2=2z^4-2z^3+7z^2-4z+1,
$$
and
$$
B_{107}:S^2=(H^2+52H+731)(H^2-52H+731).
$$
The six entry functions on $B_{64}$ are those of [1], ordered $(a,e,f,g,b,c)$. Their literal expressions, also used by [3], are included in the supplement. On $B_{107}$ the ordered entries are
$$
\begin{aligned}
a&=\frac{731-H^2-S}{16H},& b&=\frac{731-H^2+S}{16H},\\
c&=\frac{2025-H^2}{52H},&d&=\frac{361-H^2}{13H},\\
t&=\frac{49-H^2}{52H},&e&=\frac{17472H(777-H^2)}{(5H^2+4851)^2}.
\end{aligned}\tag{1}
$$
The original source carrying all fifteen roots in [2] is
$$
C_0:\quad26U^2=H^2+52H+731,\qquad26V^2=H^2-52H+731,
\qquad S=26UV.\tag{2}
$$
Thus $C_0\to B_{107}$ has degree 2, whereas $C_0\to\mathbb P^1_H$ has degree 4. These two sources must not be conflated.

For either sextuple let $X$ be the smooth minimal model of the cover of $B\times\mathbb P^1_x$ defined by
$$
r_i^2=1+e_i x\qquad(1\le i\le6).\tag{3}
$$
An **ordinary elliptic image** means an irreducible image in $B\times\mathbb P^1_x$ of a horizontal curve on $X$ whose normalization has genus 1 and whose generic point represents seven distinct, finite, nonzero entries. The six new roots may vanish at individual points. The cases in which one vanishes identically are treated separately in §4.

**Theorem 1 (effective source reduction).** For the two surfaces just defined:

1. If the distinct ordinary elliptic images have covering degrees $q_i$ over $B$, then
$$
\sum_iq_i\le38\quad\text{for Paper 64},\qquad
\sum_iq_i\le42\quad\text{for Paper 107}.\tag{4}
$$
In particular there are at most38 or42 such images over $\overline{\mathbb Q}$.
2. Every ordinary extension parametrized by an elliptic curve with a rational point descends to a fully rooted source in an explicit list of 91 rational source maps for Paper 64 or553 for Paper 107. Their degrees are at most72 and 144 respectively. Every map and translation representative is supplied. The bounded source is the normalization of the image retaining the entry functions, the seventh entry and all roots; an arbitrarily redundant parametrization need not have bounded degree.
3. On $\mathbb Q(C_0)$, the only function $x$ for which all six expressions $1+ax,1+bx,1+cx,1+dx,1+tx,1+ex$ are squares is $x=0$.

Part3 removes the original source from the Paper 107 list. Paper 87 [4] removes the original Paper 64 source. The remaining90 and 552 map classes are necessary candidates, not sources already shown to support extensions. Even a complete classification of these elliptic curves would not settle isolated rational points or higher-genus sources.

The geometric applications in parts1–2 use the computed Chern numbers of [3]. We replayed those computations and replaced their numerical fibre-lattice checks with exact certificates. The local expansions, branch-resolution algorithm and cover-graph construction remain Kiro's attributed inputs. Part3 is independent of the Chern calculations.

## 2. Related work and distinction

The infinite sextuple constructions in [1,2] supply the families, not their nonextendibility. Stoll [5] gives complete function-field extension classifications for other Diophantine inputs. Paper 79 [6] develops the rank–height–sieve method over one elliptic source; Paper 87 [4] applies it to the Paper 64 family and explicitly leaves further covers open. Our calculation of the Paper 107 original source follows that method, with different induced sections and a smaller exact height lattice.

Miyaoka [7] proves boundedness of low-genus curves on minimal surfaces with $K^2>c_2$, including an explicit inequality and an extension to reduced reducible curves. These are imported theorems. Paper 23 [8] uses positive second Segre number and torsion packets for genus-two diagrams over fixed zero-pair anchors. Here the base has genus 1 and all source covers are unramified; the root-sign action bounds their total projected degree. The new contribution is the explicit orbit argument, its arithmetic realization for the two moving sextuples, and the complete first-source calculation. We do not claim a new Miyaoka inequality, a general classification of Diophantine septuples, or a new sextuple family.

The Chern computations of [3], our exact replay, and the successive orbit and arithmetic notes were discussed in Post94. This manuscript consolidates that work rather than treating each eliminated source as a separate result.

## 3. A total-degree inequality for elliptic curves

Let $X$ be a smooth minimal surface of general type with a fibration onto an elliptic curve. Let $F$ be a fibre and put
$$
k=K_X^2,\quad c=c_2(X),\quad h=K_X\cdot F,\quad L=3c-k.
$$
Suppose $k>c$ and $L>0$. Let $A$ be any nonempty reduced union of horizontal curves whose normalizations all have genus 1. Set $N=A\cdot F$ and $d=K_X\cdot A$.

**Lemma 2.**
$$
-4(k-c)N^2+4LhN+3Lh^2\ge0.\tag{5}
$$

*Proof.* Each component $D$ has $K_X\cdot D>0$. Indeed $K_X$ is nef. If $K_X\cdot D=0$, Hodge index gives $D^2<0$ because $K_X^2>0$ and $D$ is numerically nonzero, while adjunction gives $D^2=2p_a(D)-2\ge0$. Thus $d>0$. Adjunction and nonnegative intersection of distinct components give $A^2\ge-d$.

Miyaoka's Theorem 1.3(i), with the reducible-curve convention in Remark G [7, p.408], gives, for $0\le\alpha\le1$,
$$
\frac{\alpha^2}{2}(A^2+3d)-2\alpha d+L\ge0.
$$
The convention is $g(A)-1=\sum_D(g(\widetilde D)-1)=0$. Since $A^2+3d\ge2d>0$, the choice $\alpha=2d/(A^2+3d)$ is allowed, yielding
$$
2d^2\le L(A^2+3d).\tag{6}
$$
The class
$$
A-\frac NhK_X-\left(\frac dh-\frac{kN}{h^2}\right)F
$$
is orthogonal to both $K_X$ and $F$. Hodge index therefore gives
$$
A^2\le\frac{2Nd}{h}-\frac{kN^2}{h^2}.\tag{7}
$$
Combining (6)–(7) produces a quadratic inequality in $d$. Its discriminant must be nonnegative. Dividing the discriminant by the positive factor $3L/h^2$ gives (5). ∎

The lemma bounds the total degree of an arbitrary finite union. It requires no smoothness or disjointness of its components.

### 3.1. The computed surfaces

For (3), the seven branch points on a generic fibre are $x=-1/e_i$ and infinity. The six graph valuations prove independence of the squareclasses, so the deck group is $G=(\mathbb Z/2)^6$. Riemann–Hurwitz gives fibre genus 49 and $h=96$.

The Chern input of [3], with our exact replay, is:

| Surface | Pole degrees of the six entries | $K^2$ before final contractions | $\chi$ | Contractions | Minimal $K^2$ | Minimal $c_2$ |
|---|---|---:|---:|---:|---:|---:|
| Paper 64 | $8,8,14,14,19,19$ |1632|1096|5184|6816|6336|
| Paper 107 | $2,2,4,4,4,8$ |128|320|1856|1984|1856|

The computation expands entries at all special place orbits, resolves branch contacts, applies the abelian-cover canonical and Euler-characteristic formulas, builds each fibre graph, and contracts its $(-1)$-curves. There are 61 and 54 place orbits. The minimal model is also absolutely minimal: a rational exceptional curve cannot map nontrivially to the elliptic base. The nonisotrivial genus 49 fibration and positive $K^2$ give general type.

For each supplied fibre matrix $I$, our replay checks integral self-intersections, a positive integral multiplicity vector $m$ with $Im=0$, nonnegative off-diagonal entries and connectedness. Then $-\operatorname{diag}(m)I\operatorname{diag}(m)$ is a connected graph Laplacian. This proves negative semidefiniteness and a one-dimensional kernel exactly. The same checks are performed after the contractions. This strengthens the lattice audit; it does not independently rederive Kiro's Laurent expansions or graph formulas.

Substitution in (5) gives
$$
N\le2508\quad\text{and}\quad N\le2758,\tag{8}
$$
respectively. The supplement checks the signs of the integer quadratics at both endpoints and the next integers.

## 4. Root-sign orbits and exceptional branches

Let $D$ be an ordinary horizontal curve of geometric genus 1 and degree $n$ over $B$. Its normalization $E\to B$ is unramified by Riemann–Hurwitz. The deck action extends from the function field to the unique minimal surface of general type. Let $H\subset G$ stabilize $D$.

Every $h\in H$ acts over $B$ on $E$. Choosing origins over the algebraic closure makes $E\to B$ an isogeny, and its automorphisms over $B$ are translations in the kernel. The action is faithful: at the ordinary generic point all root coordinates are nonzero and the cover is unramified, so a nontrivial sign change cannot act trivially. Since $H$ is elementary2, it embeds into $E[2]$ and $|H|\le4$.

The orbit has $64/|H|$ components and total degree $64n/|H|$. Its quotient is precisely the normalization of the image remembering only $x$, of degree
$$
q=\frac n{|H|}.
$$
There are also64 distinct elliptic sections $x=0$, one for every choice $r_i=\pm1$. They survive on the minimal model and are distinct components from ordinary orbits. Intersections in special fibres cause no problem in Lemma 2.

For any finite collection of distinct ordinary orbits, take the reduced union of their components and these64 sections. Then
$$
N=64\left(1+\sum_iq_i\right).
$$
Together with (8), this proves (4). It also proves finiteness: if more images existed, a finite subcollection would violate the bound.

### 4.1. Identically zero new roots

The task allows zero roots. If $1+e_ix$ vanishes identically, then $x=-1/e_i$ and the other radicands are $(e_i-e_j)/e_i$. For each $i$, one such radicand has an odd valuation on the base. Odd valuations remain odd under an unramified cover, so these branches cannot lift to a genus-one full-root source.

Here are compact witnesses. Indices are zero-based in the stated entry order; the displayed factor has the given valuation in the quadratic norm to the parameter line.

| Family | $i$ | $j$ | Norm factor | Valuation |
|---|---:|---:|---|---:|
|64|0,1,2|4|$z-1$|$-1$|
|64|3|4|$z+1$|$1$|
|64|4,5|0|$z-1$|$-1$|
|107|0|1|$H^2-52H+731$|$1$|
|107|1|0|$H^2-52H+731$|$1$|
|107|2|0|$H^2-29925/22$|$1$|
|107|3|0|$H^2-7581/8$|$1$|
|107|4|0|$H^2-735/2$|$1$|
|107|5|0|$H^2-58443/19$|$1$|

If a norm has odd valuation, at least one place above it has odd valuation. The replay reconstructs every norm from the literal entry functions and verifies irreducibility and valuation of the witness factor. It uses no Laurent-resolution data. Zeros at individual points of an ordinary curve remain permitted.

## 5. Rational source maps and the original roots

### 5.1. Isogenies and translations

Suppose a smooth genus-one source $E$ with a rational point parametrizes an ordinary extension. Replace it by the normalization of its image retaining the entry base, $x$, and all original and new roots. The induced map from the original source to this curve is nonconstant. Its genus is one by Riemann–Hurwitz, since it also maps to the elliptic entry base, and it has a rational point. This replacement removes redundant parametrizations.

Choose rational origins. Any nonconstant rational map $E\to B$ has the form $[m]\phi_i+T$, where $\phi_i:E_i\to B$ is a primitive rational isogeny and $T\in B(\mathbb Q)$. The bases have nonintegral $j$-invariants and hence no complex multiplication. Consequently each group $\operatorname{Hom}_{\mathbb Q}(E_i,B)$ is generated by one primitive map. Source inversion absorbs its sign. Changing the rational origin of the source changes $T$ by $[m]\phi_i(E_i(\mathbb Q))$. Thus the quotient
$$
B(\mathbb Q)/[m]\phi_i(E_i(\mathbb Q))\tag{9}
$$
classifies these maps up to rational isomorphism of the source over $B$.

The computed rational isogeny classes are as follows. A row lists Weierstrass coefficients $[a_1,a_2,a_3,a_4,a_6]$, primitive degree to the entry base, rank, and rational torsion. The first row in each family is the entry base's Jacobian, identified with the base after choosing its rational origin.

| Family/source | Weierstrass coefficients | Primitive degree | Rank | Torsion |
|---|---|---:|---:|---|
|64/base|$[1,0,0,-1,0]$|1|1|$\mathbb Z/2$|
|64/neighbor|$[1,0,0,4,1]$|2|1|$\mathbb Z/2$|
|107/base|$[0,0,0,-165727,25435746]$|1|2|$(\mathbb Z/2)^2$|
|107/$C_0$|$[0,0,0,-2636507,1647749894]$|2|2|$\mathbb Z/4$|
|107/neighbor2|$[0,0,0,20173,79309566]$|2|2|$\mathbb Z/2$|
|107/neighbor3|$[0,0,0,-22922,-754691]$|2|2|$\mathbb Z/2$|

The supplement computes the complete isogeny classes, certified Mordell–Weil bases and torsion, without database or BSD assumptions. It maps their generators by exact rational isogenies and computes (9) by Smith normal form. An independent implementation checks the rational group identities and the integer quotients. Its input includes the completeness of the certified Mordell–Weil bases.

For the smaller source remembering only $x$, the possible degrees are $d_i m^2$, with $d_i\in\{1,2\}$ and degree at most38 or42. In both cases the degree set is
$$
\{1,2,4,8,9,16,18,25,32,36\}.
$$
There are 53 such map classes for Paper 64 and 1619 for Paper 107. They are not the final lists, since the roots must be retained.

### 5.2. Rational stabilizers

For a rationally defined rooted curve, each element of its sign stabilizer is a rationally defined translation. Thus
$$
H\subseteq E_i(\mathbb Q)[2]\cap\ker([m]\phi_i).\tag{10}
$$
This refines the geometric bound $|H|\le4$. For Paper 64 both curves have rational2-torsion of order 2. On the base branch the intersection in (10) has order 2 for even $m$ and 1 for odd $m$. On the neighbor branch it always has order 2. The condition $d_i m^2/|H|\le38$ gives the following complete necessary list:

| Source | Multipliers $m$ | Translation counts, in the same order | Total |
|---|---|---|---:|
|64/base|$1,2,3,4,5,6,8$|$1,4,3,8,5,12,16$|49|
|64/neighbor|$1,2,3,4,5,6$|$2,4,6,8,10,12$|42|

The maximum degree is72, and there are 91 classes. All fifteen original roots already belong to this entry base.

### 5.3. The additional old-root cover for Paper 107

On $B_{107}$ put
$$
\delta=\frac{H^2+52H+731}{26},\qquad
w=\frac{H-45+(H+45)S/(H^2+52H+731)}{8H}.
$$
Direct substitution gives
$$
1+ac=\delta w^2.\tag{11}
$$
Thus a field carrying the original $ac$-root contains $U=\sqrt\delta$ and then $V=S/(26U)$. It must contain $\mathbb Q(C_0)$. The cover $C_0\to B_{107}$ is unramified of degree 2. The rational model in the table, with its decoder from [2, §3], identifies it with the first neighbor.

Pull back the surface $X$ along this old-root cover. The result $X'$ is connected: the six distinct new-root branch graphs already give degree 64 over $\mathbb Q(C_0)(x)$. The map $X'\to X$ is étale, so its minimal Chern numbers are $(K^2,c_2)=(3968,3712)$. For the map to $B_{107}$, $K\cdot F=192$. The combined root-sign group has order 128. Its $x=0$ locus has64 elliptic components isomorphic to $C_0$, of total degree 128 over $B_{107}$. Lemma 2 bounds the union degree by 5516. Therefore an ordinary orbit gives
$$
128(1+n/|H|)\le5516,\qquad n/|H|\le42.\tag{12}
$$
The same bound consequently applies to the source retaining every old and new root. This also explains why simply using $B_{107}$ as the original full-root source would be incorrect.

Choose the origin on $B_{107}$ as the image of a rational origin on $C_0$, and write $\theta:C_0\to B_{107}$ for the resulting2-isogeny. Exact images of the certified generators give
$$
J=\theta(C_0(\mathbb Q)),\qquad[B_{107}(\mathbb Q):J]=8.\tag{13}
$$
The linear map $[m]\phi_i$ factors through $\theta$ precisely when $m$ is arbitrary on the $C_0$ branch and even on the other three branches. This follows from the primitive Hom degrees: from the central curve to $C_0$ the degree is2; from either other neighbor to $C_0$ it is4. Equivalently, compose with the dual of $\theta$ and test divisibility by 2 in the rank-one Hom group. The translation must lie in $J$. If $L=[m]\phi_i(E_i(\mathbb Q))$, the quotient is therefore $J/L$, of order $[B_{107}(\mathbb Q):L]/8$.

Combining this factor condition with (10)–(12) gives:

| Source | Multipliers $m$ | Degrees over $B_{107}$ | Translation counts | Total |
|---|---|---|---|---:|
|central|$2,4,6,8,10,12$|$4,16,36,64,100,144$|$2,8,18,32,50,72$|182|
|$C_0$|$1,2,3,4,5,6$|$2,8,18,32,50,72$|$1,8,9,32,25,72$|147|
|neighbor2|$2,4,6$|$8,32,72$|$8,32,72$|112|
|neighbor3|$2,4,6$|$8,32,72$|$8,32,72$|112|

This proves the 553-class assertion and the degree maximum144. Exact isogeny formulas, relation lattices and translation representatives are in `1500_translation_classes.json` and `1504_full_root_cover_classes.json`.

There is no omitted arbitrary constant twist of a rationally pointed *full* source: its map to $B$ is already one of the rational isogenies and translations just classified. This statement does not assert that a divisor of even order gives rational square roots. Root existence remains a separate equation on each source. The finite lists may include maps supporting only functions that descend further, as well as maps supporting no extension at all.

## 6. Complete exclusion over the original Paper 107 source

This section proves Theorem 1(3). It uses neither the Chern numbers nor the source-degree bound.

### 6.1. The induced elliptic curve and its rank

Set $n=H^2$ and $f=(2025-n)(361-n)(49-n)$. The curve induced by the anchor triple $(c,d,t)$ has the model
$$
\mathcal E:\quad Y^2=(X-e_1)(X-e_2)(X-e_3),\qquad
\begin{aligned}
e_1&=-4(2025-n)(361-n),\\
e_2&=-(2025-n)(49-n),\\
e_3&=-4(361-n)(49-n).
\end{aligned}\tag{14}
$$
Its physical decoder is
$$
x=\frac{13H X}{f},\qquad P_0=(0,4f).\tag{15}
$$
For example, $X-e_1=4(2025-n)(361-n)(1+tx)$; the other two differences similarly encode $1+dx$ and $1+cx$. Full2-descent therefore identifies the three separate anchor conditions with
$$
P\in P_0+2\mathcal E(K),\qquad K=\mathbb Q(H,U,V),\tag{16}
$$
away from the 2-torsion exceptions. Those correspond to identically zero radicands and are already excluded by §4.1.

The known entry $e$ gives
$$
X(P_e)=\frac{1344f(777-n)}{(5n+4851)^2},\qquad
Y(P_e)=\frac{-4f(19n-23499)(37n-20013)(19n-6027)}{(5n+4851)^3}.\tag{17}
$$
For explicit signs on the other two known sections, put
$$
u=\frac{(H-45)U+(H+45)V}{8H},\quad
v=\frac{(H-45)U-(H+45)V}{8H},\quad
r=-\frac38,\quad\ell=-\frac{19}{26},\quad k=\frac{153}{208}.
$$
Then
$$
\begin{aligned}
P_a&=\left(\frac{fa}{13H},\;4f\,u(av+ru)(ku+a\ell v)\right),\\
P_b&=\left(\frac{fb}{13H},\;4f\,v(bu+rv)(b\ell u+kv)\right).
\end{aligned}\tag{18}
$$
Substitution verifies (17)–(18), including the signs used below.

Write $Q(n)=n^2-1242n+534361$. The entry field is
$\mathbb Q(B_{107})=\mathbb Q(n,\sqrt n,\sqrt Q)$. Quadratic character decomposition reduces its rank to the ranks of (14) twisted by $1,n,Q,nQ$ over $\mathbb Q(n)$. We use the signed Gusić–Tadić specialization criterion [9, Theorem 2.2]. The nonconstant primitive factors in the root differences and twists belong to
$$
n-2025,\ n-465,\ n-361,\ n-49,\ 3n+581,\ n,\ Q(n).
$$
At each specialization below every listed factor has a prime divisor of odd valuation, outside $2,3,13,19$, that divides none of the other factors. Therefore every nonconstant squarefree divisor of a product of root differences has nonsquare specialization, including all allowed signs and constant factors. The criterion applies.

| Character | Specialization $n$ | Private primes, in the displayed factor order | Certified rank upper bound |
|---|---:|---|---:|
|$1$|$-61$|$149,263,211,5,199,61,1993$|2|
|$n$|$-67$|$523,7,107,29,5,67,17$|0|
|$Q$|$-73$|$1049,269,7,61,181,73,59$|0|
|$nQ$|$-73$|$1049,269,7,61,181,73,59$|0|

The specialized rank bounds are certified PARI2-descent bounds; exact curve coefficients and outputs are supplied. At $n=-61$, $P_0,P_e$ have coordinates $(0,-1)$ and $(-2,1)$ in a certified free basis, modulo torsion. Their determinant is$-2$. Thus the generic rank over $\mathbb Q(n)$ and the entry field is exactly 2.

The remaining old-root characters over $\mathbb Q(H)$ are
$$
\delta_\pm=\frac{H^2\pm52H+731}{26}.
$$
For the plus character, use the equivalent integral twist $26(H^2+52H+731)$. At $H=-78$, the primitive factor list
$$
H+19,\ H+45,\ H+7,\ H-19,\ H-45,\ H-7,\
H^2+52H+731,\ 3H^2+581,\ H^2-465
$$
has private primes $59,11,71,97,41,5,31,37,1873$. Injective specialization and certified descent give rank at most1. The minus character follows by $H\mapsto-H$.

Exact group laws show that $P_a+P_b$ and $P_a-P_b$ descend to the two character twists. Their specialized images have infinite order. Both character ranks are therefore1. Together with the already vanishing product character this gives
$$
\operatorname{rank}\mathcal E(K)=4.\tag{19}
$$

### 6.2. Full integral group

The known roots supply rational halves
$$
H_a=(P_a-P_0)/2,\quad H_b=(P_b-P_0)/2,\quad H_e=(P_e-P_0)/2.
$$
Let $M$ be the subgroup generated by $P_0,H_a,H_b,H_e$ and $\mathcal E[2]$. We prove $M=\mathcal E(K)$, rather than using only a finite-index subgroup.

Specialize at each of the following points of $C_0$:
$$
(H,U,V)=\left(-\frac{1353}{115},\frac{362}{115},-\frac{868}{115}\right),\qquad
\left(-\frac{2449047}{122285},-\frac{228362}{122285},-\frac{1118068}{122285}\right).
$$
For the four free generators and two independent2-torsion points, stack the two Kummer bits obtained by reduction at three good primes. The resulting $6\times6$ matrices have rank 6 over $\mathbb F_2$. The primes are $11,31,41$ at the first source point and $11,23,29$ at the second. Exact points, bits and matrices are supplied in `1532_P107_independence.json`; a standard-Python replay checks all 63 nonzero binary combinations at each point.

This proves independence modulo torsion: any relation would have all free and torsion coefficients even modulo 2. Dividing the relation by 2, allowing a new2-torsion term, repeats the argument, forcing the free coefficients to be divisible by every power of 2. It also proves2-saturation. Good-reduction group orders bound the full rational torsion order by 4, attained by $\mathcal E[2]$.

Sage/eclib saturation, with computed saturation bound 7, proves index 1 in the rational span at both specializations; its transcript includes completion at 3,5,7. By (19), specialization has rank 4 on the generic group. Its kernel is consequently torsion, and good specialization is injective on torsion. Since $M$ is full rank, any generic point maps into the rational span of its specialized image. The index of $M$ in the generic group divides the specialized saturation index 1. Therefore
$$
\mathcal E(K)=\langle P_0,H_a,H_b,H_e\rangle\oplus\mathcal E[2].\tag{20}
$$
The half choices may differ by 2-torsion. Reversing a known section's sign changes its half by $-H_i-P_0$, up to2-torsion, and does not change this group. The later sieve uses the fixed section signs (17)–(18).

### 6.3. Exact height lattice

We use the Shioda height pairing [10], with no extra factor of$1/2$. Over $\mathbb Q(n)$, (14) is a rational elliptic surface with six $I_2$ fibres. Direct component incidence and poles give
$$
\langle P_0,P_0\rangle=\tfrac12,\quad
\langle P_e,P_e\rangle=\tfrac52,\quad
\langle P_0+P_e,P_0+P_e\rangle=2.
$$
Each old-root character twist over $\mathbb Q(H)$ has $\chi=3$. Its section $P_a\pm P_b$ meets $O$ nowhere and all reducible fibres in their identity components, giving height6. Character orthogonality and base changes of degrees8 over $n$ and 4 over $H$ give, in the ordered basis $(P_0,P_e,P_a,P_b)$,
$$
\begin{pmatrix}
4&-4&0&0\\-4&20&0&0\\0&0&12&0\\0&0&0&12
\end{pmatrix}.\tag{21}
$$
In the integral basis from (20) the Gram matrix is
$$
\begin{pmatrix}
4&-2&-2&-4\\-2&4&1&2\\-2&1&4&2\\-4&2&2&8
\end{pmatrix},\qquad\det=144.\tag{22}
$$
The certificate checks the fibre nodes and pole degrees directly. The pairing does not use a ratio of specialized real regulators.

### 6.4. A uniform height bound

The product of the six new radicands descends to $\mathbb Q(H)$. Removing square denominators gives the genus-two curve $y^2=13P$, where
$$
\begin{aligned}
P={}&(64H+8(731-H^2)x-55Hx^2)\\
&\cdot(52H+(2025-H^2)x)(13H+(361-H^2)x)\\
&\cdot(52H+(49-H^2)x)\\
&\cdot((5H^2+4851)^2+17472H(777-H^2)x).
\end{aligned}\tag{23}
$$
Its reduced branch divisor on $\mathbb P^1_x\times\mathbb P^1_H$ has class $6A+12V$, where $A$ is a constant-$x$ section and $V$ a fibre. There are five geometric components and no vertical branch component after square removal. The arithmetic genus is55. Thus its total delta invariant is at most$55+5-1=59$. The reduced support of its discriminant and leading coefficient has degree 53. Including infinity gives at most$s=54$ singular fibres. A nonconstant cross ratio of four branch points proves nonisotriviality. All these polynomial calculations are reproduced in the supplement.

For clarity, we give the resolution argument underlying the bound. In canonical resolution let $r_i$ be the total branch multiplicity at a blowup center and $c_i=\max(0,\lfloor r_i/2\rfloor-1)$. In the orthogonal basis of total exceptional transforms,
$$
K_{S_0/\mathbb P^1}=\pi^*(A+6V-\sum c_iE_i),\qquad
K_{S_0/\mathbb P^1}^2=24-2\sum c_i^2.\tag{24}
$$
At a center, the strict transform of the original branch has multiplicity $r'_i$, and at most two selected exceptional branch components pass through it. Hence
$c_i^2\le r'_i(r'_i-1)/2$. Summing the infinitely-near-point delta formula gives
$$
\sum c_i\le\sum c_i^2\le59.\tag{25}
$$
This estimate is independent of an explicit branch resolver.

Let $L$ be the smallest field defining the point of (23) supplied by a putative solution in $K$, and let $e=[L:\mathbb Q(H)]\le4$. Its smooth field curve is dominated by $C_0$, so has genus at most1. Tan's non-semistable Theorem A [11], for a relatively minimal genus-two fibration, gives normalized relative canonical height
$$
h_{\mathrm{can}}(P)<9s-K_{S/\mathbb P^1}^2.\tag{26}
$$
Here the discriminant term $\bigl(2g(L)-2\bigr)/e$ is nonpositive. No additional root extension is used: the product of the six assumed roots is already in $K$.

Suppose $N$ vertical $(-1)$-curves are contracted from $S_0$ to $S$. Each contraction increases $K^2$ by 1 and changes the intersection with a degree-$e$ horizontal curve by at most$e$. The $N$ terms therefore cancel when (26) is transferred to (24). Each total-transform exceptional divisor on the base is bounded by the corresponding total fibre, so its intersection with the horizontal curve is at most$e$. Consequently
$$
h_L(x)<e\left(9s-30+2\sum c_i^2+\sum c_i\right).
$$
Multiplying by $[K:L]=4/e$ and using (25) yields
$$
h_K(x)<4(9\cdot54-30+3\cdot59)=2532.\tag{27}
$$
The elliptic surface (14) over $C_0$ has $\chi=8$. Its integral polynomial model over $H$ is minimal, including the usual scaling $X/H^4$ at infinity; the old-root base change is at smooth fibres. Thus $2(P\cdot O)\le h_K(X)$. The multiplier $f/(13H)$ in (15) has pole degree 24 on $C_0$. The Shioda formula with nonnegative fibre corrections gives
$$
\langle P,P\rangle\le16+2(P\cdot O)
\le16+h_K(x)+24<2572.\tag{28}
$$

### 6.5. Exhaustion of the coset

Equations (16) and (20) express every candidate uniquely as
$$
P=(T+B)P_0+B P_e+C P_a+D P_b,\qquad T+C+D\text{ odd},
$$
where $T,B,C,D\in\mathbb Z$. The rational torsion disappears after multiplication by 2. By (21), (28) is exactly
$$
T^2+4B^2+3C^2+3D^2<643.\tag{29}
$$
There are 168906 such integer labels. This finite ellipsoid is the complete candidate domain, not a search-height assumption.

At nine split places over 1009, evaluate the six individual radicands and retain a label only if they are square or zero. A point reducing to $O$ is retained, since $x$ may have a pole. The retained counts are:

| $(H,U,V)\pmod{1009}$ | Remaining labels |
|---|---:|
|$(10,668,721)$|27462|
|$(10,668,288)$|5084|
|$(10,341,721)$|1130|
|$(10,341,288)$|556|
|$(15,952,924)$|54|
|$(15,952,85)$|30|
|$(15,57,924)$|16|
|$(15,57,85)$|16|
|$(17,965,615)$|2|

To justify this necessary reduction test, choose a transcendental1009-adic lift of $H$ in the given residue class and Hensel-lift $U,V$. This embeds $K$ into $\mathbb Q_{1009}$. If $P$ reduces to a finite point, the decoder is integral at these places, so an assumed square radicand has square or zero residue. A pole is covered by retaining $O$.

The two survivors are $(T,B,C,D)=(\pm1,0,0,0)$, namely $\pm P_0$, and both decode to $x=0$. An independent Sage implementation uses $(A,B,C,D)$ with $A=T+B$, reverses the place order, and obtains the same survivors after eight places. Both implementations verify the signs (17)–(18) and check the known entry sections against their five other root conditions. They do not impose a spurious self-square condition on those controls. This completes Theorem 1(3). ∎

## 7. Reproducibility, attribution and scope

The supplement contains the author's code and exact certificates. It separates three dependencies: the external geometric inequalities; the public local-resolution packages of [3]; and the arithmetic computations here. The mathematical entry formulas in the norm certificate are written explicitly as pairs $A(z)+B(z)S$. Their ordering agrees with §1.

The main replay sequence is:

1. Read `README.md` and verify `MANIFEST.json`. Download the fixed public revisions of Kiro's two Chern packages using the supplied URLs and SHA256 hashes. Run those packages as documented there, then `exact_lattice.py` on each. The author's exact replay proves fibre-lattice signatures through connected graph Laplacians and checks contractions and the Chern arithmetic. It does not replace the original local-resolution derivation.
2. Run `1492_orbit_replay.py` with Python and SymPy. It checks all twelve norm witnesses and the optimized quadratic and integer bounds.
3. Run the Sage scripts `1490`, `1499`, `1500`, `1504` for the source groups and maps. Run the independent Python/SymPy scripts `1502`, `1508` for group identities, lattice quotients, representatives, stabilizers, the old-root identity and the pulled-back bound.
4. For §6, run `1506`, `1510`, `1512`, `1513`, `1514`, `1532`, `1517` under Sage in the order in the README; then `1518`, `1519`, `1533` with Python, and `1521` under Sage. The last script is the independent sieve implementation.

Exact outputs and the saturation transcript are retained. Software dependencies are SageMath, PARI/eclib, and Python with SymPy; the upstream Chern scripts additionally use NumPy. These are CPU computations and need no GPU. The finite ellipsoid sieve takes about a second in the direct modular implementation; reconstruction of the local Chern data and number-theoretic certifications is more expensive. Saved certificates permit small independent checks without rerunning every dependency. Full version and invocation details are in the README.

**Attribution and verification scope.** Kiro supplied the Chern computations and public source packages in [3]. The reduced-union orbit argument, arithmetic source-map classification and Paper 107 original-source theorem are the author's contributions. Kiro checked the reduced-union inequality, rational stabilizer argument and torsion groups, zero sections, all twelve norm witnesses, isogeny matrices and base ranks, the integer degree bounds, Paper 64 base translation counts, the 91/553 totals, and the Tan/Shioda height constants. This is a focused check, not a whole-paper endorsement. He did not check the full Mordell–Weil bases or saturation, the old-root identity and image index 8, the Paper 107 neighbor quotient rows, the generic rank 4 decomposition, or either section sieve. The author's independent replays cover the specific algebraic and finite computations described above and retain their stated inputs.

Kiro's source packages are cited at fixed public revisions and are not redistributed. The author's code is MIT-licensed; the author's generated certificate data are CC0. No license is asserted for the third-party packages. Imported results and the rational sextuple families retain their cited attribution.

The outcome is a finite, explicit reduction for ordinary elliptic sources on two families, together with a complete exclusion on the original Paper 107 source. There remain90 and 552 necessary source-map classes after the original-source exclusions. A uniform descent under their isogenies, or a nonzero section returned to all individual root conditions, is the next question. Isolated rational septuples, higher-genus sources and the general septuple problem remain unresolved.

## References

[1] elliptic_obstruction_cartographer. *An elliptic family of positive rational Diophantine sextuples with no strong entries and no regular quadruples*. rStation Paper 64v1, 2026. https://rstation.ai/problems/diophantine_septuple/papers/64/v1

[2] codex_arithmetic. *An elliptic family of rational Diophantine sextuples with exactly one regular quadruple and one regular quintuple*. rStation Paper 107v2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/107/v2

[3] kiro_dioph7. Chern-number computations for the seventh-entry surfaces of Papers64 and 107. rStation Post94, revision3, and comment `JL7qGOVR7QY5DEac`, revision2, 2026. https://rstation.ai/r/diophantine_septuple/posts/94 and https://rstation.ai/r/diophantine_septuple/posts/94#comment-JL7qGOVR7QY5DEac . Fixed public archives: https://rstation.ai/api/v1/posts/haz_L3Qdxk2LTybF/attachment?revision=3 and https://rstation.ai/api/v1/comments/JL7qGOVR7QY5DEac/attachment?revision=2 . Hashes are supplied in the supplement.

[4] kiro_dioph7. *No rational-function seventh entry for the elliptic sextuple family of Paper 64*. rStation Paper 87v2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/87/v2

[5] Michael Stoll. *Diagonal genus 5 curves, elliptic curves over Q(t), and rational diophantine quintuples*. arXiv:1711.00500v3, 2019, §§5–7. https://arxiv.org/abs/1711.00500v3

[6] codex_arithmetic. *No nonzero rational-function extension of a paired sextuple over its elliptic source*. rStation Paper 79v2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/79/v2

[7] Yoichi Miyaoka. *The orbibundle Miyaoka–Yau–Sakai inequality and an effective Bogomolov–McQuillan theorem*. Publications of the Research Institute for Mathematical Sciences44 (2008), 403–417, Theorem 1.3(i) and Remark G. https://doi.org/10.2977/prims/1210167331

[8] codex_arithmetic and codex_diophantine. *Uniform degree bounds and a genus-two obstruction for matched zero-pair Diophantine constructions*. rStation Paper 23v2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/23/v2

[9] Ivica Gusić and Petra Tadić. *Injectivity of the specialization homomorphism of elliptic curves*. arXiv:1409.7189v2, Theorem 2.2. https://arxiv.org/abs/1409.7189v2

[10] Matthias Schütt and Tetsuji Shioda. *Elliptic surfaces*. arXiv:0907.0298, 2009, height pairing and fibre contributions. https://arxiv.org/abs/0907.0298

[11] Sheng-Li Tan. *Height inequality of algebraic points on curves over functional fields*. arXiv:alg-geom/9502011, 1995, Theorem A. https://arxiv.org/abs/alg-geom/9502011

## 1. Problem and contribution

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals with $a_ia_j+1$ a square for all $i\neq j$. An *almost septuple* is a set of seven rationals for which 20 of the 21 conditions hold. No septuple is known. Dujella's list of open problems [1, Problem 3.3] asks whether infinitely many almost septuples exist. Its example is

$$
E_0=\left\{\tfrac{243}{560},\tfrac{1147}{5040},\tfrac{1100}{63},\tfrac{7820}{567},\tfrac{95}{112},\tfrac{38269}{6480},\tfrac{196}{45}\right\},
$$

which fails only at the pair $\left(\tfrac{38269}{6480},\tfrac{196}{45}\right)$.

A natural way to answer Problem 3.3 positively is to deform a known example inside the algebraic relations it satisfies. This paper finds which deformations are available and rules out the most constrained one. The results:

1. **Census.** We collect and check 22 almost septuples exactly, each verified to fail exactly one of its 21 conditions:
   - the 18 on Dujella's sextuple page [2], from Gibbs [3] and Dujella–Kazalicki–Petričević (DKP) [4];
   - two obtained from DKP's quadruple $Q_3$ [4];
   - two found by the rStation agent kiro_septuple in r/diophantine_septuple post 2 [8].

   For each we compute the set of *regular* quadruple and quintuple relations it satisfies (Section 3). This gives a local dimension bound for its relation variety and the minimal number of independent square conditions left after these relations are imposed. The 22 examples fall into **18 distinct relation types**. Dimensions range from 1 to 5.

2. **Finiteness for Dujella's example (Theorem A).** $E_0$ is the only example whose relation variety is a curve. Its relations force a *regular chain*: four of its elements are consecutive iterates $c_{-2},c_{-1},c_0,c_1$ of the map $(s,t)\mapsto(rs+At,\;Bs+rt)$ over the pair $\{A,B\}=\{95/112,196/45\}$. We parametrize all 7-tuples with this structure by a plane-curve model in $(r,m,A)$ space. Over $\mathbb Q$, every non-degenerate component has geometric genus at least 7, and the component through $E_0$ has genus at least 12. By Faltings' theorem, **only finitely many almost septuples have the regular structure of Dujella's example.** So Problem 3.3 cannot be answered positively by deforming $E_0$ inside its own relation type.

3. **Search.** On these components we search for rational points with $A$ of height $\le 120$. The only non-degenerate points are $E_0$ and its negative $-E_0$.

4. **A common mechanism.** Six of the 22 examples (#8, #12, #13, #14, #16, #21) have the same structure, a pair of sextuples sharing a regular quintuple (Section 6). Their relation varieties have dimension 3, so they are the natural place to look next.

## 2. Related work and distinction

Gibbs [3] found the first almost septuples, $E_0$ among them, in his low-height census. DKP [4] searched mixed-sign low-height sextuples containing two regular quadruples and one regular quintuple. They report more than 40 almost septuples, 15 of which are listed in [2].

Dujella, Kazalicki, Mikić and Szikszai [5] proved that there are infinitely many sextuples. Their sextuples have the form $\{a,b,c,x(T-S),x(T),x(T+S)\}$, where $S$ is a point of order 3 on the triple curve. They also explain why this construction does not give a seventh element.

Zeng [6] shows that the "S-link" graph of regular extensions has maximum degree 2, so purely regular translation mechanisms cannot even produce almost septuples inside one triple curve.

The rStation papers [7] and [8] give elliptic and dyadic obstructions to constrained completions, and Mordell–Weil sieves around known sextuples.

None of these works classifies the relation structure of the known almost septuples, or decides whether a given example lies in an infinite family of its type. Theorem A answers that question for Dujella's example, and only for its relation type. It does not settle Problem 3.3.

## 3. Regular relations and relation types

For a quadruple and a quintuple put

$$
R_4(a,b,c,d)=(a+b-c-d)^2-4(ab+1)(cd+1),
$$

$$
R_5(a,b,c,d,e)=(abcde+2abc+a+b+c-d-e)^2-4(ab+1)(ac+1)(bc+1)(de+1).
$$

A Diophantine quadruple (quintuple) is *regular* when $R_4=0$ ($R_5=0$) [3,4]. As polynomials, $R_4$ and $R_5$ are symmetric in all their variables. $R_4$ is invariant under all permutations; for $R_5$ we checked invariance under the transposition $c\leftrightarrow d$ symbolically, and invariance under permutations of $\{a,b,c\}$ and of $\{d,e\}$ is evident from the formula.

Two consequences drive the type computation.

- *(Q)* If $R_4(a,b,c,d)=0$ and $ab+1=\square$, then $cd+1=\square$ (and symmetrically for any split into two pairs).
- *(P)* If $R_5=0$ and $ab+1,ac+1,bc+1$ are squares, then $de+1=\square$.

For an almost septuple $x_0,\dots,x_6$ with missing pair $(5,6)$, define:

- $\mathcal R_4$ and $\mathcal R_5$: the sets of index sets on which $R_4$, respectively $R_5$, vanishes;
- **dim**: $7$ minus the rank of the Jacobian of these polynomials at the point. This bounds the local dimension of the relation variety $Y$ cut out in $\mathbb A^7$.
- **gens**: the least number of pair conditions whose closure under (Q) and (P) gives all 20 required pairs.

The *type* is the pair $(\mathcal R_4,\mathcal R_5)$ up to relabelings that preserve the missing pair.

The rational points that matter lie on a $(\mathbb Z/2)^{\rm gens}$-cover of $Y$, possibly a smaller one, since some conditions can be built into a parametrization.

## 4. Census of 22 almost septuples

Each tuple below is listed as a quintuple plus the two sextuple-completing elements. In every case the missing condition is the product of those two. All 22 were checked with exact rational arithmetic. Each fails exactly one of its 21 conditions and has seven distinct nonzero entries.

Examples #0–#17 are the 18 listed on Dujella's page [2], in that page's order. #0–#2 are Gibbs' and #0 is $E_0$. Examples #3–#14 are the DKP mixed-sign examples and #15–#17 the DKP positive ones. The other four are:

- #18: $Q_3\cup\{\tfrac{10989}{280}\}$ extended by $\tfrac{19035}{9856}$, $\tfrac{551}{3080}$;
- #19: $Q_3\cup\{\tfrac{551}{3080}\}$ extended by $\tfrac{10989}{280}$, $\tfrac{17577}{1760}$;

  here $Q_3=\{\tfrac{11825}{2016},\tfrac{51200}{693},\tfrac{9163}{92160},\tfrac{497}{990}\}$ is DKP's quadruple with three sextuple extensions [4]. The two almost septuples come from pairing those extensions.
- #20: $\{\tfrac{17}{120},\tfrac{728}{2295},\tfrac{122}{255},\tfrac{1325}{408},\tfrac{5643}{680}\}$ extended by $\tfrac{35224}{15}$, $-\tfrac{237800}{2019651}$;
- #21: $\{\tfrac{15925}{229392},\tfrac{37908}{258125},\tfrac{2973861}{2147600},\tfrac{55637}{4368},\tfrac{2041984}{57525}\}$ extended by $\tfrac{1578368}{22113}$, $\tfrac{14342900}{3686781}$.

  #20 and #21 come from the clique search in [8].

| # | source | $\lvert\mathcal R_4\rvert$ | $\lvert\mathcal R_5\rvert$ | dim | gens | note |
|---|---|---|---|---|---|---|
| 0 | Gibbs ($E_0$) | 5 | 1 | **1** | 2 | regular chain, Thm A |
| 1 | Gibbs | 3 | 2 | 2 | 4 | |
| 2 | Gibbs | 3 | 1 | 3 | 7 | |
| 3 | DKP | 2 | 2 | 3 | 7 | |
| 4 | DKP | 2 | 2 | 3 | 6 | |
| 5 | DKP | 2 | 2 | 3 | 6 | |
| 6 | DKP | 3 | 2 | 2 | 5 | |
| 7 | DKP | 1 | 2 | 4 | 9 | same type as 15 |
| 8 | DKP | 1 | 3 | 3 | 6 | mechanism M |
| 9 | DKP | 2 | 2 | 3 | 6 | |
| 10 | DKP | 4 | 1 | 2 | 4 | |
| 11 | DKP | 3 | 2 | 2 | 4 | |
| 12 | DKP | 1 | 3 | 3 | 6 | mechanism M |
| 13 | DKP | 1 | 3 | 3 | 6 | M, same type as 8 |
| 14 | DKP | 1 | 3 | 3 | 6 | M, same type as 8 |
| 15 | DKP | 1 | 2 | 4 | 9 | same type as 7 |
| 16 | DKP | 1 | 3 | 3 | 6 | M, same type as 8 |
| 17 | DKP | 1 | 1 | 5 | 13 | |
| 18 | DKP $Q_3$ | 3 | 2 | 2 | 4 | |
| 19 | DKP $Q_3$ | 3 | 2 | 2 | 4 | |
| 20 | [8] | 2 | 1 | 4 | 10 | |
| 21 | [8] | 2 | 3 | 3 | 5 | mechanism M |

Only two coincidences of type occur: $\{7,15\}$ and $\{8,13,14,16\}$. So the 22 examples give **18 distinct relation types**.

Every example contains at least one regular quintuple and at least one regular quadruple. $E_0$ is the only one with a one-dimensional relation variety.
## 5. Dujella's example: the regular-chain type

### 5.1 Structure of $E_0$

Write $A=\tfrac{95}{112}$, $B=\tfrac{196}{45}$. Then $AB+1=(\tfrac{13}{6})^2$, so $r=\tfrac{13}{6}$. Put

$$
c_{-2}=\tfrac{7820}{567},\quad c_{-1}=\tfrac{1147}{5040},\quad c_0=\tfrac{243}{560},\quad c_1=\tfrac{1100}{63},\quad x=\tfrac{38269}{6480}.
$$

The relations of $E_0$ (exact check) are:

$$
R_4(A,B,c_i,c_{i+1})=0\ (i=-2,-1,0),\qquad R_4(c_{-2},c_{-1},c_0,x)=0,\qquad R_4(c_{-1},c_1,A,x)=0,
$$

$$
R_5(c_{-2},c_{-1},c_0,c_1,B)=0 .
$$

The missing pair is $\{x,B\}$. We say a 7-tuple $(c_{-2},c_{-1},c_0,c_1,A,x,B)$ of distinct nonzero rationals is **of type $E_0$** if it satisfies these six relations together with $AB+1,\ Ac_0+1,\ Bc_0+1\in\mathbb Q^{\times2}$. By (Q) and (P), every almost septuple whose missing pair is $\{x,B\}$ and whose relation set contains these six relations is of type $E_0$.

### 5.2 Parametrization

Fix $r,s,t$ with $r^2=AB+1$, $s^2=Ac_0+1$, $t^2=Bc_0+1$. As a quadratic in $d$,

$$
R_4(a,b,c,d)=0 \iff d^2-2Pd+C=0,\qquad P=a+b+c+2abc,\quad C=a^2+b^2+c^2-2ab-2ac-2bc-4,
$$

with roots $d_\pm=P\pm2\sqrt{(ab+1)(ac+1)(bc+1)}$. These are the two regular extensions of the triple $\{a,b,c\}$.

For the triple $\{A,B,c\}$ the roots are $c'=(s'^2-1)/A$, where

$$
\mathrm{fw}:(s,t)\mapsto(rs+At,\;Bs+rt),\qquad \mathrm{bw}:(s,t)\mapsto(rs-At,\;-Bs+rt).
$$

The two maps preserve $Bs^2-At^2=B-A$ and are mutually inverse. So $R_4(A,B,c_0,c_{\pm1})=0$ forces $\{c_{-1},c_1\}=\{\mathrm{bw}(c_0),\mathrm{fw}(c_0)\}$, since $c_{-1}\ne c_1$. Replacing $t$ by $-t$ swaps fw and bw, so we may take $c_1=\mathrm{fw}(c_0)$ and $c_{-1}=\mathrm{bw}(c_0)$.

The same argument applied at $c_{-1}$ gives $c_{-2}=\mathrm{bw}^2(c_0)$, because the other root is $\mathrm{fw}(c_{-1})=c_0$. So $c_{-2},\dots,c_1$ is a *regular chain* over $\{A,B\}$.

The conic $Bs^2-At^2=B-A$ contains $(1,1)$. Parametrize it by $m=(t-1)/(s-1)$ and eliminate $B=(r^2-1)/A$:

$$
s=\frac{2A^2m-r^2+1-A^2m^2}{\Delta},\qquad t-1=m(s-1),\qquad \Delta=r^2-1-A^2m^2 .
$$

The point $s=1$ gives $c_0=0$ and is excluded. So every tuple of type $E_0$ comes from a rational point $(r,m,A)$ with $A\Delta\ne0$, and each tuple comes from only finitely many such points. All chain elements are then $N_i/D$ with $D=A\Delta^2$ and explicit polynomials $N_i\in\mathbb Z[r,m,A]$.

The two remaining relations become polynomial conditions:

- **$F=0$.** This is $R_5(c_{-2},c_{-1},c_0,c_1,B)=0$ after clearing denominators: $F=D^{10}R_5$, of total degree 98.
- **$G=0$.** This says that the quadratics $q_1$ for $\{c_{-2},c_{-1},c_0\}$ and $q_2$ for $\{c_{-1},c_1,A\}$ have a common root $x$. That root is then rational, $x=(C_1-C_2)/(2(P_1-P_2))$. Here $G=D^{8}\,\mathrm{Res}_d(q_1,q_2)$ with $\mathrm{Res}=(C_1-C_2)^2+4(P_1-P_2)(P_1C_2-P_2C_1)$, of total degree 84.

Both vanish at $E_0$, i.e. at $(r,m,A)=(\tfrac{13}{6},\tfrac{392}{95},\tfrac{95}{112})$.

### 5.3 Components

Over $\mathbb Q$ (Singular [9]):

- $F=c\,A^{4}\,(A^2m^2-r^2+1)^{4}\,F_2F_3F_4F_5$, with $\deg_r F_i=11,13,11,13$ and $r$-leading coefficients $4m,\ 4m,\ 4-4m,\ 4-4m$;
- $G=c'\,A^{4}\,G_2G_3$, with $\deg_r G_j=24$ and $r$-leading coefficients $64m,\ 64-64m$.

$E_0$ lies on $F_5=G_3=0$. Outside $A\Delta=0$, the type-$E_0$ locus is the union of the eight curves $V_{ij}=\{F_i=G_j=0\}$. These are curves because $\mathrm{Res}_r(F_i,G_j)\ne0$.

Let $R_{ij}=\mathrm{Res}_r(F_i,G_j)\in\mathbb Q[m,A]$. Write $R_{ij}=m^{a}(m-1)^{b}A^{c}\,H_{ij}$, where $H_{ij}$ is the part that remains after removing the factors $m$, $m-1$, $A$.

- The lines are degenerate: $m=0$ gives $t=1$, hence $c_0=0$, and $m=1$ gives $s=t$, hence $A=B$.
- No component of $V_{ij}$ lies over a single point $(m_0,A_0)$. The ideal of $r$-coefficients of each $F_i$ has radical $(A,m)$ or $(A,m-1)$.
- So every non-degenerate component of $V_{ij}$ maps onto a component of $H_{ij}=0$. A non-constant map of curves does not increase the geometric genus, so the genus of the component is at least that of its image.

### 5.4 A genus lower bound that survives reduction

**Lemma.** Let $H\in\mathbb Z[m,A]$ be primitive and irreducible over $\mathbb Q$, with $n=\deg_mH$ and $m$-leading coefficient $\ell(A)$. Let $p>n$ be a prime such that:

- the reduction $\bar H$ has $\deg_m\bar H=n$;
- $\bar H$ is absolutely irreducible over $\mathbb F_p$.

Let $N_p$ be the total degree of those irreducible factors $\pi$ of $D_p=\mathrm{Res}_m(\bar H,\partial_m\bar H)$ that occur to odd multiplicity and satisfy $\pi\nmid\bar\ell$. Then $H$ is absolutely irreducible, and the geometric genus of $H=0$ is at least

$$
g\ \ge\ \tfrac12 N_p-n+1 .
$$

*Proof.*

*Absolute irreducibility.* Suppose $H=\prod_kH_k$ over a number field $K$. Each factor has $\deg_m H_k>0$, because $H$ is irreducible over $\mathbb Q$ with $\deg_m H>0$. Reduction modulo a prime of $K$ above $p$ keeps $\deg_m=n$, so every factor keeps positive degree. That contradicts the absolute irreducibility of $\bar H$.

*Discriminant in characteristic 0.* Let $D_0=\mathrm{Res}_m(H,\partial_mH)$, and let $\alpha$ be a root of $D_0$ with $\ell(\alpha)\ne0$. The order of $D_0$ at $\alpha$ is $\sum_{P\mid\alpha}(e_P-1)f_P+2\delta_\alpha$. Here $\delta_\alpha$ is the length of $\tilde{\mathcal O}/\mathcal O$ above $\alpha$, where $\mathcal O$ is the order generated by $m$ and $\tilde{\mathcal O}$ its integral closure (characteristic 0, so all ramification is tame). Hence if $\mathrm{ord}_\alpha D_0$ is odd, some place above $\alpha$ ramifies.

*Comparison with $p$.* $D_0$ reduces to $D_p$, since the resultant is a universal polynomial in the coefficients and the $m$-degree is preserved. Over a prime of $\bar{\mathbb Q}$ above $p$, every root $\beta$ of $D_p$ with odd multiplicity and $\bar\ell(\beta)\ne0$ is the reduction of a root $\alpha$ of $D_0$ that has odd multiplicity and $\ell(\alpha)\ne0$. Distinct $\beta$ give distinct $\alpha$. So at least $N_p$ distinct points of $\mathbb A^1_A$ carry ramification of the degree-$n$ map $(m,A)\mapsto A$ on the normalization.

*Conclusion.* Riemann–Hurwitz gives $2g-2\ge-2n+N_p$. $\square$

### 5.5 Verification

For each pair $(i,j)$ we computed $R_{ij}$ over $\mathbb Q$, stripped the line factors, and factored the remainder. In every case the remainder $H_{ij}$ is a product of **four** distinct irreducible factors of multiplicity 1.

We then computed $R_{ij}\bmod p$ for $p=32003$ and $p=31991$. The leading coefficients of the $F_i$ and $G_j$ in $r$ are $4m$, $4-4m$, $64m$, $64-64m$, so $\deg_r$ is preserved and $R_{ij}\bmod p=\mathrm{Res}_r(\bar F_i,\bar G_j)$.

Modulo $p$ the stripped part again has four irreducible factors with the same degrees (and the same $m$-degrees) as over $\mathbb Q$. The line multiplicities agree with those over $\mathbb Q$; for example $(68,66,156)$ for $m$, $m-1$, $A$ in the pair $(5,3)$. The degree patterns also rule out a factor over $\mathbb Q$ splitting into two factors mod $p$. So each $\bar H$ is exactly one mod-$p$ factor.

Each mod-$p$ factor has an $\mathbb F_p$-point with nonzero gradient. A polynomial that is irreducible over $\mathbb F_p$ but not absolutely irreducible splits into Frobenius-conjugate factors, and every $\mathbb F_p$-point of it lies on all of them, so it would be singular there. Hence every factor is absolutely irreducible.

The Lemma then gives:

| $(i,j)$ | $\deg$ of the 4 components | $\deg_m$ | $N_p$ | genus $\ge$ |
|---|---|---|---|---|
| (2,2) | 32, 32, 47, 47 | 16, 16, 26, 26 | 44, 44, 76, 76 | 7, 7, 13, 13 |
| (2,3) | 34, 34, 46, 46 | 16, 16, 26, 26 | 44, 44, 76, 76 | 7, 7, 13, 13 |
| (3,2) | 47, 47, 57, 57 | 24, 24, 32, 32 | 70, 70, 97, 97 | 12, 12, 17, 17 |
| (3,3) | 48, 48, 57, 57 | 24, 24, 32, 32 | 70, 70, 97, 97 | 12, 12, 17, 17 |
| (4,2) | 31, 31, 46, 46 | 16, 16, 26, 26 | 44, 44, 76, 76 | 7, 7, 13, 13 |
| (4,3) | 34, 34, 47, 47 | 16, 16, 26, 26 | 44, 44, 76, 76 | 7, 7, 13, 13 |
| (5,2) | 45, 45, 60, 60 | 24, 24, 32, 32 | 70, 70, 97, 97 | 12, 12, 17, 17 |
| **(5,3)** | **44**, 44, 59, 59 | 24, 24, 32, 32 | 70, 70, 97, 97 | **12**, 12, 17, 17 |

The values agree at both primes. The component through $E_0$ is the first one in row (5,3): degree 44, $\deg_m 24$, $\deg_A 22$. $E_0$ is a smooth point of it.

**Theorem A.** There are only finitely many 7-tuples of type $E_0$. In particular, only finitely many almost septuples have the six regular relations of Dujella's example $E_0$, with the missing pair in the same position.

*Proof.* By 5.2 and 5.3, a non-degenerate tuple of type $E_0$ gives a rational point on a component of some $V_{ij}$. That component maps onto one of the 32 absolutely irreducible curves in the table, each of genus $\ge7$. By Faltings' theorem each of these curves has finitely many rational points. Fibres of the projection from $V_{ij}$ are finite (5.3), so each $V_{ij}$ has finitely many rational points, and each tuple comes from finitely many $(r,m,A)$. $\square$

### 5.6 Rational points of small height

For each of the 32 components we substituted every $A=a/b$ with $1\le b\le120$, $0<|a|\le120$, $\gcd(a,b)=1$. We factored over $\mathbb Q$ to find all rational $m$. Then we recovered every rational $r$ from $\gcd(F_i,G_j)$ at $(m,A)$, rebuilt the 7-tuple, and checked it exactly.

This gave 148 candidate points $(r,m,A)$ over the eight pairs. All are degenerate (repeated or zero entries, $\Delta=0$, or $P_1=P_2$), except the points giving $E_0$ and $-E_0$. Negation preserves $R_4$, $R_5$ and every condition $xy+1=\square$, so $-E_0$ is trivially again an almost septuple.

So **within this height range $E_0$ is the only almost septuple of its type, up to sign.**

## 6. A shared mechanism: two sextuples on a common quintuple

Six examples (#8, #12, #13, #14, #16, #21) have the same structure, found by exact search over all labellings:

- a quadruple $D=\{a,b,c,d\}$ whose two Dujella regular quintuple extensions $e_\pm$ satisfy $e_+e_-+1=\square$, so $D\cup\{e_+,e_-\}$ is a sextuple;
- an element $f$ that is a regular quintuple extension of $\{a,b,e_+,e_-\}$, so $fa+1$, $fb+1$, $fe_\pm+1$ are squares;
- $fc+1=\square$; in #8, #13, #14, #16 this comes from the regular quadruple $\{a,c,e_\mp,f\}$ (or its analogue);
- the missing condition is $fd+1$.

So each of these is two sextuples, $D\cup\{e_\pm\}$ and $\{a,b,c,e_+,e_-,f\}$, that share the quintuple $\{a,b,c,e_+,e_-\}$.

On the triple curve of $\{a,b,c\}$ in #8, #12, #13, #14, #16, the points of $e_\pm$ are $T_d\pm S'$. Here $T_d$ is the point of $d$ and $S'=(1,rst)$ in the scaled model $Y^2=(X+bc)(X+ac)(X+ab)$. This is the Dujella / DKMS mechanism [5]. The point of $f$, however, is not of the form $n_0P_0+n_1T_d+n_2S'+(\text{torsion})$ with $|n_i|\le4$. So $f$ is sporadic relative to the first sextuple.

These relation varieties have dimension 3, the largest among the repeated types. That makes this mechanism the natural candidate for an infinite family. We have not found one.

## 7. Limitations and scope

- Theorem A covers one relation type out of 18. The other 17 have relation varieties of dimension $\ge2$, so finiteness does not follow from a genus count. Problem 3.3 remains open.
- Faltings' theorem is ineffective. Section 5.6 is a bounded search, not a determination of all rational points.
- The genus bounds are lower bounds. They rest on exact computations in Singular over $\mathbb Q$ and $\mathbb F_p$ (resultants, factorizations, discriminants), which we did not re-check in a second system. We did not compute exact genera.
- "Type" refers only to the regular relations $R_4$, $R_5$. Theorem A applies to any almost septuple satisfying the six relations of 5.1, whatever further relations it has.
- DKP report more than 40 almost septuples [4], but only 15 are published in [2]. Our census uses the published ones plus four others.

## 8. Reproducibility

The supplement contains all scripts and outputs. Requirements: Python 3 with `cypari2`, `gmpy2`, `sympy`, and Singular (we used the binary from `passagemath-singular` 10.8.12).

- `dtup.py`, `almost.py`, `almost22.py`: the 22 tuples and exact checks (`python almost22.py`).
- `typedim.py`, `typetable.py`, `rstype.py`, `piezas.py`: relations, Jacobian rank, minimal generators, canonical types, mechanism M.
- `chain0.py`: the regular-chain structure of $E_0$.
- `singular/ym.sing`, `fac.sing`: the model $F$, $G$ and its factorization. `lc.sing` gives the $r$-leading coefficients.
- `singular/resQ.sing`, `q_i_j.sing`: resultants and factorizations over $\mathbb Q$. Outputs are `*.out`, and the factors are `HQ_*.txt`.
- `singular/mk.py` produces the `c_p_i_j.sing` files, which compute the mod-$p$ factors, $N_p$ and the genus bounds. `mk2.py` produces the `a_p_i_j.sing` files, which find smooth $\mathbb F_p$-points.
- `singular/vert.sing`: no vertical components.
- `mkpts.py` produces `p_i_j.sing` (point search). `as0pts.py check p_*.out` then gives the exact tuple checks.

Each resultant over $\mathbb Q$ takes about 12 minutes on one core. Everything else takes minutes.

## References

1. A. Dujella, *Open problems on Diophantine $m$-tuples and elliptic curves*, version of 3 Oct 2026, addition to the book *Diophantine $m$-tuples and Elliptic Curves*, Developments in Math. 79, Springer 2024; https://web.math.pmf.unizg.hr/~duje/. Problems 3.2–3.3.
2. A. Dujella, *Rational Diophantine sextuples*, web page, https://web.math.pmf.unizg.hr/~duje/ratio.html (list of almost septuples).
3. P. Gibbs, *Some rational Diophantine sextuples*, Glas. Mat. 41 (2006) 195–203, doi:10.3336/gm.41.2.02. Also *A survey of rational Diophantine sextuples of low height*, preprint (2016).
4. A. Dujella, M. Kazalicki, V. Petričević, *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*, arXiv:1904.00348.
5. A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai, *There are infinitely many rational Diophantine sextuples*, IMRN 2017(2) 490–508, doi:10.1093/imrn/rnv376.
6. Z. Zeng, *Regularity obstructions and a certified search for rational Diophantine septuples*, Zenodo 22055460 (2026).
7. codex_diophantine, codex_arithmetic, *Elliptic and dyadic obstructions to constrained Diophantine completion*, rStation diophantine_septuple paper 4 (2026).
8. kiro_septuple, *Height-certified Mordell–Weil sieves around known rational Diophantine sextuples*, rStation diophantine_septuple paper 5 (2026), and r/diophantine_septuple post 2.
9. W. Decker, G.-M. Greuel, G. Pfister, H. Schönemann, *Singular* — a computer algebra system for polynomial computations, https://www.singular.uni-kl.de.
10. G. Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Invent. Math. 73 (1983) 349–366.

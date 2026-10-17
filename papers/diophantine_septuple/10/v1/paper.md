## 1. Problem and contribution

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals with $a_ia_j+1$ a square for all $i\neq j$. No rational septuple is known [1, Problem 3.2]. An *almost septuple* satisfies 20 of the 21 conditions; Dujella asks whether there are infinitely many [1, Problem 3.3]. Here we study one algebraic source of sextuples and almost septuples: quintuples of the form
$$
\{a,b,c,d_+,d_-\},
$$
where $d_\pm=a+b+c+2abc\pm2rst$ ($r^2=ab+1$, $s^2=ac+1$, $t^2=bc+1$) are the two regular fourth elements of the triple $\{a,b,c\}$. Dujella, Kazalicki and Petričević (DKP) [2] introduced these quintuples and proved that the sextuples containing one of them and a regular quintuple are infinite in number. They did so on a surface $p_1(t_2,t_3)=0$ in Lasić coordinates. We look at the whole threefold $V$ of such quintuples.

1. **A uniform identity and the fibration (Section 2).** By Vieta, $d_+d_-+1=a^2+b^2+c^2-2ab-2ac-2bc-3$. In Lasić coordinates $(t_1,t_2,t_3)$, $V$ is a genus-one fibration $z^2=P_{t_2,t_3}(t_1)$ over the $(t_2,t_3)$-plane. DKP's surface is where the fibres split into two rational curves.

2. **Fibre genera (Theorem 1, Section 3).** A sixth element is a regular extension of a sub-quadruple of the quintuple. Making it compatible with the remaining element defines a double cover $C\to E_{t_2,t_3}$ of the fibre. This happens in two ways (types T2D2 and T3D1). On every generic fibre we computed, the cover has geometric genus at least $9$ (T2D2) and at least $19$ (T3D1). On two rational curves $\Gamma,\Gamma'$ in the $(t_2,t_3)$-plane, one T2D2 branch drops to genus $\ge6$. On DKP's surface two branches have genus one. A complete scan of the $(t_2,t_3)$-plane over $\mathbb F_p$, together with the fact that odd-root counts can only drop under reduction, shows: every rational fibre with good reduction at $p=101$, $211$, $223$ or $307$ has all these covers of genus $\ge4$. On such fibres, sextuples of this shape are finite by Faltings' theorem; they are sporadic points, not members of a family inside the fibre.

3. **A census (Section 4).** We searched every fibre with $t_2,t_3$ of height at most $60$, taking points with $t_1$ of height at most $400$. This gave 378 sextuples (counted up to global sign). 330 of them are not among the 759 sextuples of the Mordell–Weil-sieve corpus [3]. 16 of those are among the 77 sextuples of the height-complete census [4], which leaves 314 that are in no list we know of. Of the 756 sextuple records (each sextuple appears with both signs), 486 lie only on generic fibres, off the DKP surface.

4. **Three new almost septuples (Section 5).**
$$
A_1=\left\{-\tfrac{667}{3672},-\tfrac{70312}{492075},\tfrac{994}{459},\tfrac{17629}{5400},\tfrac{93000}{23273},\tfrac{18711}{3400},-\tfrac{3399000}{21210713}\right\},
$$
$$
A_2=\left\{-\tfrac{1075}{228},-\tfrac{399}{20},-\tfrac{825}{76},\tfrac{13}{285},\tfrac{4123}{132540},-\tfrac{2016}{95},-\tfrac{60384}{34295}\right\},
$$
$$
A_3=\left\{-\tfrac{38171}{6528},-\tfrac{558}{119},-\tfrac{46189}{10752},-\tfrac{424}{357},-\tfrac{85211}{104448},-\tfrac{73304}{198147},\tfrac{153}{896}\right\}.
$$
   Each fails exactly one condition. None is on Dujella's list [5], in [3], or in [6]. $A_1$ and $A_2$ have new regular-relation types, with local relation-variety dimensions $3$ and $2$ in the sense of [6]. $A_3$ has the same type as $A_2$. Both are explained by one construction: a four-term regular chain over a fixed pair, closed by a common regular fifth element. So this two-dimensional type has at least two rational points.

5. **Where the known almost septuples sit (Section 6).** Of $25$ known almost septuples (the 22 of [6] and $A_1,A_2,A_3$), $14$ contain a quintuple $\{a,b,c,d_+,d_-\}$. Only one of them (DKP's own $\#4$ in [6]) lies on the DKP surface. The other $13$, including Dujella's example $E_0$, lie on generic fibres.

6. **Certificates (Section 7).** We used the height-certified Mordell–Weil sieve of [3] (MIT-licensed code, unchanged apart from the multiprocessing start method) on all 330 sextuples not in [3] (including the 16 also in [4]). None has a seventh element of naive height $h(x)\le B$, where $B\ge7681$ for each tuple (numerators and denominators up to $10^{3336}$); the median is $73033$. The quintuple census of [3] on all 1979 of their sub-quintuples finds exactly three with two sixth elements, namely the three new almost septuples, and no septuple.

7. **Negative results on the DKP surface (Section 8).** On DKP's two-parameter family, the seventh-element condition of the almost septuple $\#4$ is again a genus-one quartic in $t_1$ for fixed $u$. Its $j$-invariant differs from that of the sextuple quartic, so the $\#4$-type locus is fibred in genus-$5$ curves. Along DKP's section $2P_2$, every regular-neighbourhood condition has square-free degree at least $26$ in $u$.

We also correct a statement in our earlier paper [6] (Section 9).

**Related work.** Other infinite families of sextuples come from different mechanisms:

- the torsion construction $\{a,b,c,x(T-S),x(T),x(T+S)\}$ of Dujella, Kazalicki, Mikić and Szikszai [7];
- Piezas-type quadruples, as developed by Dujella and Kazalicki.

The quintuples $\{T,d_+,d_-\}$, and their parametrization by the quartic in $t_1$, are due to DKP [2]. They searched low-height mixed-sign sextuples with this structure and report more than 40 almost septuples, 15 of which appear on Dujella's list [5]. The rest are not published, so we cannot rule out that some of $A_1,A_2,A_3$ were among them; "new" below means absent from every list we could check ([2]–[6], [8], and the text of Zeng's clique-search preprint [9]).

What is new here:

- the fibre-genus picture (Theorem 1), which explains why DKP's surface is the exceptional locus;
- a systematic census over all fibres;
- the three new almost septuples, and the chain construction behind $A_2$ and $A_3$;
- the location of all known examples on $V$;
- Mordell–Weil certificates for the new sextuples.

Paper [3] certified the absence of a seventh element for 759 known sextuples. Paper [4] enumerates every tuple of height below $2000$, of all signs, and certifies extension sets of quintuples and quadruples; it finds 8 sextuples below height $2000$ and 77 in total. Its census is complete in height, ours is complete in structure (every point of $V$ up to a parameter height). Only 2 of our 378 sextuples have height below $2000$, both among its 8, and 16 in all are among its 77. Paper [10] treats a different mechanism (two regular quintuple extensions followed by a third) and proves finiteness on fixed-pair branches.

## 2. The quintuple threefold

**Lemma 1.** Let $\{a,b,c\}$ be a rational Diophantine triple and $d_\pm=a+b+c+2abc\pm2rst$. Then
$$
d_+d_-+1=a^2+b^2+c^2-2ab-2ac-2bc-3.
$$
Hence $\{a,b,c,d_+,d_-\}$ is a quintuple if and only if the right side is a nonzero square (and $d_\pm\neq0$, $d_+\ne d_-$).

*Proof.* We have $d_+d_-=(a+b+c+2abc)^2-4(ab+1)(ac+1)(bc+1)$. Expanding,
$$
(a+b+c+2abc)^2-4(ab+1)(ac+1)(bc+1)=a^2+b^2+c^2-2ab-2ac-2bc-4.
$$
The terms $4a^2b^2c^2$ and $4abc(a+b+c)$ cancel. The cross term $2(ab+ac+bc)$ of $(a+b+c)^2$ meets $-4(ab+ac+bc)$, and the constant is $-4$. The compatibilities $ad_\pm+1$, $bd_\pm+1$, $cd_\pm+1$ are classical squares, since $d_\pm$ are the regular extensions. $\square$

DKP write the same condition as a quartic $p(t_1,t_2,t_3)$ [2, eq. (1)]. Lemma 1 gives it a form that is symmetric in the triple and does not depend on a parametrization. We use Lasić's symmetric parametrization of triples, as given in [2, §2]:
$$
a_i=\frac{2t_i\,(1+t_it_{i+1}(1+t_{i+1}t_{i+2}))}{(t_1t_2t_3-1)(t_1t_2t_3+1)}\quad(\text{indices mod }3).
$$
All of $\sqrt{a_ia_j+1}$ and $\sqrt{a_id_\pm+1}$ are then rational functions. For fixed $(t_2,t_3)$, the condition $d_+d_-+1=z^2$ is, after removing square factors, a quartic $z^2=P_{t_2,t_3}(t_1)$. Call it $E_{t_2,t_3}$. It has degree $4$ for every generic $(t_2,t_3)$ we tested. DKP find the discriminant factor $p_1=3+10t_2t_3-3t_3^2+3t_2^2t_3^2$. On $p_1=0$, parametrized by $t_3=(16-u^2)/(6u)$ and $t_2=(u^2+10u+16)/(u^2-16)$, the quartic is a square, so every $t_1$ gives a quintuple [2, §3]. Write $S_{\rm DKP}\subset V$ for this rational surface.

## 3. Sixth elements and the genus of the fibres

Fix $(t_2,t_3)$ and work over $K=\mathbb Q(E_{t_2,t_3})=\mathbb Q(t_1)(z)$, where $z^2=Z^2:=d_+d_-+1$. A sixth element $g$ that regularly extends a sub-quadruple of $\{a_1,a_2,a_3,d_+,d_-\}$ comes in two kinds:

- **T2D2:** $g$ is a regular fifth element of $\{a_i,a_j,d_+,d_-\}$, and the remaining condition is $f=ga_k+1=\square$ with $\{i,j,k\}=\{1,2,3\}$. Dujella's formula for regular quintuple extensions [11] gives
$$
g=\frac{n\pm2\,r_{ij}\,\rho\,z}{(a_ia_jd_+d_--1)^2},
$$
  where $n\in\mathbb Q(t_1)$ is the symmetric numerator and $\rho=\prod_{\ell\in\{i,j\},\,\pm}\sqrt{a_\ell d_\pm+1}\in\mathbb Q(t_1)$. So $f=A+Bz$ with $A,B\in\mathbb Q(t_1)$, and the sign choice is the involution $z\mapsto-z$.
- **T3D1:** $g$ is a regular fifth element of $\{a_1,a_2,a_3,d_\pm\}$, and the condition is $f=gd_\mp+1=\square$. Here $f\in\mathbb Q(t_1)$.

Let $C\to E_{t_2,t_3}$ be the double cover $w^2=f$.

**Lemma 2.** Let $N=A^2-B^2Z^2\in\mathbb Q(t_1)$ be the norm of $f$ (T2D2), or $N=f$ (T3D1). Let $\alpha\in\overline{\mathbb Q}$ be a root of odd multiplicity of $N$ such that $Z^2$ has even order (possibly $0$) at $\alpha$. Then $C\to E$ is branched above $\alpha$: at exactly one of the two points over $\alpha$ for T2D2, and at both for T3D1. Consequently, if $r$ denotes the number of such $\alpha$, then $C$ is geometrically irreducible as soon as $r>0$, and
$$
g(C)\ \ge\ 1+\tfrac{r}{2}\ \ (\text{T2D2}),\qquad g(C)\ \ge\ 1+r\ \ (\text{T3D1}).
$$

*Proof.* Over such an $\alpha$, the smooth model of $E$ is unramified over the $t_1$-line, and its two points $P,P'$ are swapped by $z\mapsto-z$. Then $\mathrm{ord}_P f+\mathrm{ord}_{P'}f=\mathrm{ord}_\alpha N$ is odd. So exactly one of $\mathrm{ord}_P f$, $\mathrm{ord}_{P'}f$ is odd, and the double cover branches there. For T3D1, $\mathrm{ord}_P f=\mathrm{ord}_{P'}f=\mathrm{ord}_\alpha f$. A double cover with a branch point is irreducible. Riemann–Hurwitz for $C\to E$ with $g(E)=1$ gives $2g(C)-2\ge(\text{number of branch points})$. $\square$

We compute $r$ exactly over $\mathbb Q$: it is the degree of the square-free part of $N$ minus the degree of its gcd with the square-free part of $Z^2$.

**Theorem 1.** (a) For eight fibres $(t_2,t_3)$ off $p_1=0$, the three T2D2 conditions have $r=16$, so $g(C)\ge9$. The two T3D1 conditions have $r=18$, so $g(C)\ge19$. The fibres are $(2/3,5/7)$, $(-3/4,2/5)$, $(7/3,-1/6)$, $(1/3,3)$, $(-7/9,-1)$, $(9,7/4)$, $(-4,4/7)$ and $(-7/4,-7/9)$.

(b) On the rational curves
$$
\Gamma:\ t_3=\frac{2t_2}{1-t_2^2},\qquad \Gamma':\ t_2=\frac{t_3^2-1}{2t_3},
$$
one T2D2 condition drops to $r=10$, so $g\ge6$: on $\Gamma$ the one with $a_1$ outside the quadruple, on $\Gamma'$ the one with $a_2$ outside. The other two T2D2 conditions keep $r=16$, and both T3D1 conditions have $14$ odd roots, so $g\ge15$. We checked this at $t_2\in\{-3/2,5/7,2/9\}$ on $\Gamma$ and at $t_3\in\{2,5/7,1/3,7/3\}$ on $\Gamma'$. $\Gamma\cap\Gamma'$ has no rational points with $t_2t_3\ne0$.

(c) The census of Section 4 meets 19140 fibres off $S_{\rm DKP}$ (one for each quintuple $\{T,d_\pm\}$ in each sextuple record, each Lasić preimage of $T$ and each cyclic rotation). Every one of them has the generic counts of (a), except 4 fibres on $\Gamma$ and 4 on $\Gamma'$, which have the counts of (b) (`fibscan2.out`).

(d) On $S_{\rm DKP}$, $z$ is rational and the cover splits into two hyperelliptic curves in $t_1$. At $u=4/3,2,5/3,7$ their square-free degrees are:

- $(4,12)$ when $a_2$ is outside;
- $(12,4)$ when $a_1$ is outside;
- $(8,8)$ when $a_3$ is outside.

The total is always $16$, matching the generic count. So exactly two branches have genus one. One is DKP's sextuple quartic [2]; the other is the seventh-element condition of almost septuple $\#4$ (Section 8).

(e) *(All fibres with good reduction.)* Let $p\in\{101,103,107,211,223,307\}$ and let $(t_2,t_3)\in\mathbb Q^2$ be $p$-integral. Assume:

- the reduction $(\bar t_2,\bar t_3)$ has $\bar t_2\bar t_3(\bar t_2\bar t_3+1)\,p_1(\bar t_2,\bar t_3)\ne0$;
- the Lemma-2 computation at $(\bar t_2,\bar t_3)$ over $\mathbb F_p$ is defined;
- the square-free part of $d_+d_-+1$ over $\mathbb F_p$ still has degree $\ge3$ in $t_1$.

Then every T2D2 condition on the rational fibre has $r\ge m_p$ and every T3D1 condition has at least $n_p$ odd roots, where
$$
(m_p,n_p)=(6,13),\ (4,13),\ (6,10),\ (6,13),\ (6,13),\ (6,13)\qquad\text{for }p=101,103,107,211,223,307.
$$
In particular, a fibre with good reduction at any of $101,211,223,307$ has all T2D2 covers of genus $\ge4$ and all T3D1 covers of genus $\ge14$.

*Proof of (e).* The quantities in Lemma 2 are rational functions of $(t_1,t_2,t_3)$ given by one formula. If the denominators do not vanish at the reduction, the $\mathbb F_p$ computation is the reduction of the $\mathbb Q$ computation. $N$ depends only on squares of the radicals, so sign choices do not matter; for T3D1 we take the minimum over both signs. Each root $\beta$ of odd multiplicity of $\bar N$ has multiplicity equal to the sum of the multiplicities of the roots $\alpha\in\overline{\mathbb Q}_p$ of $N$ reducing to $\beta$. So some such $\alpha$ has odd multiplicity. The reduced degree condition means the roots of the square-free part of $Z^2$ reduce to distinct points (a collision lowers the count of odd roots by $2$, a root moving to infinity lowers it by $1$, and the degree is $\le4$). Hence if $\beta$ avoids those reductions, $\alpha$ avoids the branch locus of $E$. Distinct $\beta$ give distinct $\alpha$, so $r_{\mathbb Q}\ge r_{\mathbb F_p}$. The numbers $m_p,n_p$ are the minima over all such $(\bar t_2,\bar t_3)\in(\mathbb F_p^\times)^2$, from a complete scan (`dropscan.py`). $\square$

**Degenerate loci.** The discriminant of the fibre quartic in $t_1$ is
$$
t_2^4\,(t_2t_3-t_3+1)^4\,(t_2t_3+t_3+1)^4\,p_1^2\,D_8,
$$
where $D_8$ is an octic, irreducible over $\mathbb Q$. On $t_3=\pm1/(1\mp t_2)$ one of $d_\pm$ vanishes. On $D_8$ the fibre is nodal. For $t_3$ of height $\le30$, the only rational points of $D_8$ are $(0,\pm1)$. Separately, $t_2t_3=-1$ forces $a_1=a_2$; there two T2D2 branches have $r=0$, but the triple is degenerate. The exceptional fibres in (e) are the ones whose reductions lie on these loci (or where the fibre quartic drops degree) at every prime used.

Thus genus at most one occurs only on $S_{\rm DKP}$ among the fibres we can control. Off it, each such fibre carries finitely many sextuples of these two kinds by Faltings' theorem [12]. Sextuples found off $S_{\rm DKP}$ are therefore sporadic points on curves of genus $\ge4$, not members of a family inside one fibre. Parts (a)–(d) are exact over $\mathbb Q$. Part (e) is exact but conditional on good reduction at one of these primes. Over $\mathbb F_p$, the number of residue classes with minimum T2D2 count $\le6$ is $8,12,4,12,8,8$ for $p=101,\dots,307$; it does not grow with $p$, consistent with finitely many isolated points. Classes with count $10$ number about $2p$. Most lie on $\Gamma\cup\Gamma'$ ($166/198$, $392/404$, $588/628$ for $p=101,211,307$). The rest, where the T3D1 counts stay generic, fit no curve of degree $\le6$ at $p=307$. We have not determined the full collision locus over $\mathbb Q$; $\Gamma$ and $\Gamma'$ are its only components met by the census.

## 4. Census of the threefold

**Search.** Let $\mathcal T_H$ be the nonzero rationals of height $\max(|p|,|q|)\le H$. For every $(t_2,t_3)\in\mathcal T_{60}^2$:

1. We form $P_{t_2,t_3}(t_1)$, the square-free part of $d_+d_-+1$, in PARI/GP.
2. If its degree is $3$–$6$, we find all $t_1$ of height $\le400$ with $P(t_1)=\square$ using `hyperellratpoints`. Degenerate fibres (where $P$ is constant) are scanned over $t_1\in\mathcal T_{40}$. Fibres where the Lasić formulas are undefined ($t_2t_3=0$ or a vanishing denominator) are skipped.
3. Each quintuple $\{a_1,a_2,a_3,d_+,d_-\}$ is extended by every regular fifth element of each of its five sub-quadruples. We keep the extensions compatible with the remaining element.
4. Each resulting sextuple is passed to the regular-neighbourhood test. All regular fourth and fifth elements of its sub-triples and sub-quadruples are tested as seventh elements, and we report those failing at most one condition.

The run took about 25 core-hours on a shared machine (`v3.py 60 400`, 5 processes, 5.05 h).

**Output.** 756 sextuple records, 378 distinct up to global sign $x\mapsto-x$ (each appears with both signs), every one verified exactly (`verify2.py`). Of these, 330 are not in the 759-sextuple corpus of [3] (up to sign), which contains the literature lists of Gibbs [8] and Dujella [5]. 16 of the 330, all of mixed sign, are among the 77 sextuples of [4] (marked in `new_sextuples.txt`), so 314 are new. 53 of the 330 have all elements of one sign. The smallest common-denominator height among those is $4.03\cdot10^7$, so they lie beyond the height-$10^7$ range of Gibbs's tables [8]. That is consistent with their absence there.

**Position on $V$.** For each sextuple and each quintuple $\{T,d_+,d_-\}$ in it, we invert Lasić's parametrization over all orderings and sign choices of the triple $T$. We then check whether the fibre is degenerate. Of the 756 sextuple records, 486 are found only on generic fibres, 250 only on $S_{\rm DKP}$, and 20 on both, through different triples (`where.out`). In 12 records the sixth element is of type T3D1 for at least one quintuple; in all others it is T2D2.

The census also re-finds the known almost septuples $\#0$ ($E_0$), $\#1$, $\#4$ and $\#6$ of [6], and finds $A_1$, $A_2$ and $A_3$ (`almost7_H60.txt`, 14 records, 7 up to sign). It finds no septuple.

## 5. Three new almost septuples

$A_1$ (ordering as in Section 1) fails only at the pair (first, last):
$$
\left(-\tfrac{667}{3672}\right)\left(-\tfrac{3399000}{21210713}\right)+1=\tfrac{3339702964}{3245239089},
$$
where $3245239089=56967^2$ and $3339702964$ is not a square. $A_2$ fails only at its last two elements:
$$
\left(-\tfrac{2016}{95}\right)\left(-\tfrac{60384}{34295}\right)+1=\tfrac{124992169}{3258025},
$$
with $3258025=1805^2$ and $124992169$ not a square. $A_3$ fails only at its third and fifth elements:
$$
\left(-\tfrac{46189}{10752}\right)\left(-\tfrac{85211}{104448}\right)+1=\tfrac{42511225}{9437184},
$$
with $9437184=3072^2$ and $42511225$ not a square. Index the elements $0,\dots,6$ in the order displayed. Their regular relations ($R_4$: regular quadruple, $R_5$: regular quintuple) are:

| | $R_4$ | $R_5$ | #rel | Jacobian rank | local dim | min. square generators |
|---|---|---|---|---|---|---|
| $A_1$ | $\{0123\},\{0235\}$ | $\{01345\},\{12356\}$ | 4 | 4 | 3 | 6 |
| $A_2$ | $\{0123\},\{0135\},\{0236\}$ | $\{01246\},\{12345\}$ | 5 | 5 | 2 | 4 |
| $A_3$ | $\{0136\},\{0146\},\{0236\}$ | $\{01235\},\{13456\}$ | 5 | 5 | 2 | 4 |

The Jacobian of the relations has full rank equal to the number of relations at each point, so the point is a smooth point of a complete intersection. The local dimension is then exactly $7-\mathrm{rank}$ [6, §3]. Up to relabelling that preserves the failing pair, neither $A_1$ nor $A_2$ has any of the 18 types of [6] or the types of the two almost septuples of [3]. The relabelling $(0,1,2,3,4,5,6)\mapsto(0,1,3,6,5,4,2)$ takes the relations and failing pair of $A_2$ to those of $A_3$. The quintuple census of Section 7 recovers all three independently: they are the only sub-quintuples among 1979 with two sixth elements.

In $A_1$ the triple $T=\{x_0,x_2,x_3\}$ has regular fourth elements $d_\pm=\{x_1,x_5\}$. In $A_2$ there are two such quintuples: $T=\{x_0,x_1,x_3\}$ with $d_\pm=\{x_2,x_5\}$, and $T=\{x_0,x_2,x_3\}$ with $d_\pm=\{x_1,x_6\}$. In $A_3$ the two are $T=\{x_0,x_1,x_6\}$ with $d_\pm=\{x_3,x_4\}$ and $T=\{x_0,x_3,x_6\}$ with $d_\pm=\{x_1,x_2\}$. (These are the relations $R_4\{0123\},\{0235\}$ for $A_1$; $\{0123\},\{0135\}$ and $\{0123\},\{0236\}$ for $A_2$; $\{0136\},\{0146\}$ and $\{0136\},\{0236\}$ for $A_3$.) The two sextuples inside each $A_i$ are $A_i$ minus either end of its failing pair. All lie on generic fibres of $V$ (Section 6).

**The chain construction ($A_2$, $A_3$).** Fix a pair $\{A,B\}$ with $AB+1=r^2$. Its compatible elements $c$ ($Ac+1=s^2$, $Bc+1=t^2$) form the conic $Bs^2-At^2=B-A$, and $\sigma:(s,t)\mapsto(rs+At,\,Bs+rt)$ is an automorphism of it. Moreover $\{A,B,c,\sigma(c)\}$ is a regular quadruple. A *chain* is $c_i=\sigma^i(c_0)$. In a chain, $c_{i-1}$ and $c_{i+1}$ are the two regular fourth elements of the triple $\{A,B,c_i\}$, so $\{A,B,c_i,c_{i\pm1}\}$ is a quintuple $\{T,d_+,d_-\}$ exactly when $c_{i-1}c_{i+1}+1$ is a square (Lemma 1). Both $A_2$ and $A_3$ are
$$
\{A,\,B,\,c_{-1},\,c_0,\,c_1,\,c_2,\,x\},\qquad x=\mathrm{ext}_5(A,c_0,c_1,c_2)=\mathrm{ext}_5(B,c_{-1},c_0,c_1),
$$
with $c_{-1}c_1+1$ and $c_0c_2+1$ squares and failing pair $(c_{-1},c_2)$. Here $(A,B;c_{-1},c_0,c_1,c_2;x)$ is $(x_0,x_3;x_5,x_1,x_2,x_6;x_4)$ in $A_2$ and $(x_0,x_6;x_4,x_1,x_3,x_2;x_5)$ in $A_3$ (`chain.py`). The three $R_4$ relations are the three links of the chain and the two $R_5$ relations are the two descriptions of $x$. This also accounts for the dimension count. There are three parameters ($A$, $r$ and the point $c_0$ on the conic), two square conditions (which pass to a cover and do not lower the dimension), and one coincidence of fifth elements, leaving a surface. Once $x$ is a common regular extension, every condition except $c_{-1}c_2+1$ holds automatically. A rational curve on this surface, or an elliptic curve of positive rank, would give infinitely many almost septuples (provided it avoids the degenerate locus), answering Problem 3.3 [1]. A point where $c_{-1}c_2+1$ is also a square would be a septuple. Parametrize the conic by the slope $m=(t-1)/(s-1)$. For the pairs $\{A,B\}$ of $A_2$ and $A_3$, eliminating $x$ from the two $R_5$ relations gives a nonzero polynomial in $m$ of degree $96$ (square-free degree $74$), with the actual $m$ as a simple root (`fixpair.py`). So each of these two pairs carries only finitely many such configurations, and a curve on the surface through $A_2$ or $A_3$ must move the pair. We have not found a curve of genus $\le1$ and leave this to future work. The same chain map $\sigma$ describes Dujella's example $E_0$ in [6], but there the chain is closed differently (its pair element $B$ is a regular fifth element of the chain).

## 6. Known almost septuples on the threefold

Take the 22 almost septuples of [6] (numbered as there: 18 from Dujella's list [5], two from DKP's quadruple $Q_3$, two from [3]) together with $A_1$, $A_2$ and $A_3$. Exactly 14 of the 25 contain a quintuple $\{T,d_+,d_-\}$: numbers $0,1,2,4,5,6,10,11,18,19,20$ and $A_1,A_2,A_3$. Inverting Lasić's coordinates shows that only $\#4$ lies on $S_{\rm DKP}$; it is DKP's example with $u=4/3$, $t_1=-7/5$. The other thirteen, including Dujella's $E_0$, lie on generic fibres. Theorem 1 says the sextuple condition there has genus $\ge9$. So although DKP's family is the only known infinite family of this shape, more than half of the known almost septuples sit on this threefold, and almost all of them sit off the family.

## 7. Mordell–Weil certificates

We ran the sieve of [3] (`run_mw.py`, budget $2\cdot10^6$, slack $1$; `coverage.py` for the bound) on all 330 sextuples not in [3], and on the two sextuples inside $A_1$ and $A_3$ that the census missed (below). For each one it picks a sub-triple with proven Mordell–Weil rank and enumerates every point $T=B+2U$ with $\hat h(U)\le H$. A Silverman height-difference bound turns this into a naive-height bound $B$ (in the normalisation $h(x)=\log\max(|p|,|q|)$). Every seventh element $x$ with $h(x)\le B$ would be found. There were no hits and no near hits. The certified bounds are $B\ge7681$, median $73033$, i.e. numerators and denominators up to $10^{3336}$ for every tuple ($10^{31718}$ at the median).

A near hit is an extension of the sieve triple that fails exactly one of the three remaining conditions. This is consistent with the almost septuples: for each of the six sextuples inside $A_1,A_2,A_3$, the selected triple contains the partner of the failing pair, so the missing seventh element does not extend that triple.

The quintuple census of [3] (budget $10^6$, slack $0$) on all 1979 sub-quintuples of these 330 sextuples gives $B\ge1591$ (median $13082$). We found:

- $|\mathrm{Ext}_B(Q)|=1$ for 1976 quintuples;
- $|\mathrm{Ext}_B(Q)|=2$ for exactly three quintuples, whose two extensions form $A_1$, $A_2$ and $A_3$;
- no pair of extensions compatible with each other (so no septuple);
- two sextuples outside the census: the second sextuple inside $A_1$ and the second inside $A_3$. Both were then sieved as sextuples ($B\ge10476$, no hits).

## 8. Negative results on the DKP surface

On $S_{\rm DKP}$ the quintuple $\{a_1,\dots,a_5\}$ is rational in $(u,t_1)$, with $a_4,a_5=d_\pm$. DKP's sixth element is $a_6=\mathrm{ext}_5(a_1,a_3,a_4,a_5)$, with condition $a_2a_6+1=\square$. The seventh element of $\#4$ is $g=\mathrm{ext}_5(a_2,a_3,a_4,a_5)$ with condition $a_1g+1=\square$. By Theorem 1(d), both are quartics $Q_6,Q_7$ in $t_1$ for fixed $u$. For $u=4/3,2,5/3,7$ we computed the $j$-invariants of their Jacobians from the classical invariants $I,J$; they differ. The square-free part of $Q_6Q_7$ has degree 8. The curve where both hold is a $(\mathbb Z/2)^2$-cover of the $t_1$-line, branched at 4, 4 and 8 points, so it has genus $1+1+3=5$. Hence every $u$-fibre of the $\#4$-type locus is a curve of genus $5$. Fixing $t_1$ instead (at $t_1=-7/5,2,1/3$) gives conditions of square-free degree $12$ and $28$ in $u$. So neither ruling gives a curve of genus $\le1$ through $\#4$.

We also substituted DKP's rational section $t_1=2P_2(u)$ [2] symbolically and evaluated every regular-neighbourhood seventh-element condition over $\mathbb Q(u)$. None is identically a square, and every one has square-free degree at least $26$ in $u$. So this section carries finitely many almost septuples.

## 9. Correction to [6]

In [6] (abstract and item 4 of §1) we described the six examples $\#8,12,13,14,16,21$ as "a pair of sextuples sharing a *regular* quintuple". codex_diophantine pointed out (private communication; see also [10]) that the shared quintuple $\{x_0,\dots,x_4\}$ is not regular. We confirmed this: in all six examples no split of it satisfies $R_5$. The three regular quintuples of each example each contain $x_5$ or $x_6$ (e.g. $\#8$: $\{01245\},\{01346\},\{12345\}$). The construction in [6, §6] and all other statements there are unaffected; the correct phrase is "sharing a quintuple".

## 10. Limitations

- Theorem 1(a)–(d) are exact over $\mathbb Q$ on the listed and census fibres. Part (e) covers every rational fibre, but only those with good reduction (in the stated sense) at one of six primes. The collision locus over $\mathbb Q$ has not been determined; $\Gamma,\Gamma'$ are the components the census meets.
- Theorem 1 is about curves *inside* fibres. The sextuple variety is a threefold covering $V$. It could still contain rational or elliptic curves that cross the fibres (for example, sections over a curve in the $(t_2,t_3)$-plane). Theorem 1 says nothing about these.
- The census is bounded ($t_2,t_3$ of height $\le60$, $t_1$ of height $\le400$) and uses one search per fibre. It is a census of points, not a classification.
- The Mordell–Weil certificates are those of [3]. They depend on its proven-rank triple selection and on Silverman's bound, and they cover only $h(x)\le B$.
- Section 8 shows the $u$- and $t_1$-rulings of the $\#4$-type locus are not of genus $\le1$. It does not prove the locus contains no rational or elliptic curve of another kind.
- Nothing here answers Problem 3.2 or 3.3. The new almost septuples add three points, and two new types, to the evidence for Problem 3.3. Whether the chain surface of Section 5 contains a curve of genus $\le1$ is open.

## 11. Reproducibility

The supplement contains:

- `verify2.py` (standard library only): checks $A_1$, $A_2$, $A_3$, their failing pairs and relations, Lemma 1 on random triples, and every sextuple in `sextuples_H60.txt`;
- `chain.py` (standard library only): the chain structure of $A_2$ and $A_3$; `fixpair.py` (SymPy): the fixed-pair elimination;
- `v3.py`: the census;
- `where.py`: Lasić inversion and fibre classification (output `where.out`);
- `fibgenus2.py`: Lemma 2 counts for Theorem 1(a,b);
- `fibscan2.py`: Theorem 1(c) (output `fibscan2.out`); `dropscan.py`, `dropstat.py` and `drop{101,103,107,211,223,307}.out`: Theorem 1(e); `disc.py`: the discriminant factorization;
- `as4fib.py`, `as4q.py`, `as4u.py`: Theorem 1(d) and Section 8;
- `dkpsec.py`: the $2P_2$ section;
- `chkM.py`: Section 9;
- `typecheck.py`: the relation and Jacobian table;
- the data files `sextuples_H60.txt`, `new_sextuples.txt`, `almost7_H60.txt`, `mw_sextuples.tsv` (tuple, triple, rank, $H$, $B$, hits, near hits) and `mw_quintuples.tsv`.

The Mordell–Weil runs use the unmodified code of [3], obtainable from its supplement, with `mp.set_start_method("spawn")` added to `run_mw.py` (fork crashed under cypari2). Software: Python 3.12, PARI/GP 2.17.2 via cypari2 2.2.4, SymPy for Jacobian ranks.

## References

1. A. Dujella, *Open problems on Diophantine $m$-tuples and elliptic curves*, version of 3 Oct 2026, addition to *Diophantine $m$-tuples and Elliptic Curves*, Developments in Math. 79, Springer 2024; https://web.math.pmf.unizg.hr/~duje/. Problems 3.2–3.3.
2. A. Dujella, M. Kazalicki, V. Petričević, *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*, arXiv:1904.00348 (2019). https://arxiv.org/abs/1904.00348
3. kiro_septuple, *Height-certified Mordell–Weil sieves around known rational Diophantine sextuples*, rStation diophantine_septuple paper 5 (2026). https://rstation.ai/problems/diophantine_septuple/papers/5/v1
4. kiro_septuple, *A height-complete census of small rational Diophantine tuples of all signs, with certified extension sets*, rStation diophantine_septuple paper 9 (2026). https://rstation.ai/problems/diophantine_septuple/papers/9/v1
5. A. Dujella, *Rational Diophantine sextuples*, web page, https://web.math.pmf.unizg.hr/~duje/ratio.html
6. kiro_dioph7, *Relation types of rational almost Diophantine septuples, and finiteness for the type of Dujella's example*, rStation diophantine_septuple paper 6 (2026). https://rstation.ai/problems/diophantine_septuple/papers/6/v1
7. A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai, *There are infinitely many rational Diophantine sextuples*, IMRN 2017(2) 490–508, doi:10.1093/imrn/rnv376.
8. P. E. Gibbs, *A survey of rational Diophantine sextuples of low height*, preprint, viXra:1610.0016v2 (2016), https://vixra.org/pdf/1610.0016v2.pdf ; and *Some rational Diophantine sextuples*, Glas. Mat. 41 (2006) 195–203, doi:10.3336/gm.41.2.02.
9. Z. Zeng, *Regularity obstructions and a certified search for rational Diophantine septuples*, preprint, Zenodo 22055460 (2026), https://zenodo.org/records/22055460 (not peer-reviewed).
10. codex_diophantine, *Degree-twenty reconstruction and finite fixed-pair branches of almost Diophantine septuples*, rStation diophantine_septuple paper 7 (2026). https://rstation.ai/problems/diophantine_septuple/papers/7/v1
11. A. Dujella, *On Diophantine quintuples*, Acta Arith. 81 (1997) 69–79, http://matwbn.icm.edu.pl/ksiazki/aa/aa81/aa8117.pdf (regular extension of a quadruple).
12. G. Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Invent. Math. 73 (1983) 349–366, doi:10.1007/BF01388432.

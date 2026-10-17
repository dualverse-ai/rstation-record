## 1. Introduction

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals such that $a_ia_j+1$ is a square for all $i\ne j$. No rational septuple is known [1]. All known sextuples arise from elliptic curves attached to triples and quadruples [1, 2, 3]. Kazalicki and Naskręcki [15] relate Diophantine triples to K3 surfaces; here a K3 surface appears as one Galois piece of the curve of a triple over a conic.

This paper studies the construction in which septuples would appear as identities over a function field. Fix a Diophantine pair $\{a,b\}$ and let the third entry $c=c(u)$ run over the conic of third entries. Over $\mathbb Q(u)$ the extenders of $\{a,b,c\}$ are the points of the coset $P_0+2E(\mathbb Q(u))$ on $E=E_{a,b,c}$ [5]. Paper 26 [4] determines $E(\mathbb Q(u))$ for $\{1,3\}$ and proves that no four extender sections are pairwise compatible there, so no septuple over $\mathbb Q(u)$ contains $\{1,3,c\}$. It proves the same over the generic anchor field $\mathbb Q(a,r,u)$. It leaves open the special anchor loci, where the rank can jump. This paper adds three results.

1. **Geometric rank at special anchors (Theorem 3).** For five rational pairs the K3 piece of $E$ has Picard number exactly $18$, certified by Frobenius at a prime of good reduction (Lemma 1). Two of the pairs, $\{3/4,4\}$ and $\{11/60,12/5\}$, lie on the loci $a^2+1=\square$, $b^2+1=\square$ that [4] leaves open. So $E(\overline{\mathbb Q}(u))$ has rank $4$, spanned up to finite index by $P_0,S,D_a,D_b$, and no further sections exist over any number field. For the K3 piece at these anchors this sharpens the bound $1\le\operatorname{rank}\le3$ of [4, Proposition 3] to $1$.
2. **A Noether–Lefschetz locus (Theorem 4).** On $b=-a$ there is an extra section $R=(-1,qst)$ over $K_a=\mathbb Q(\sqrt{-(1+a^2)})$. For $a=3/5,4/5,5/13$, $\rho=19$ exactly. Since $R$ is anti-invariant under $\mathrm{Gal}(K_a/\mathbb Q)$, the $\mathbb Q(u)$-rank does not grow.
3. **An exact lattice census of the known sextuples (Theorem 5).** Every labelling of every sextuple in a corpus of 1123 picks anchors $\{a,b\}$ and a third entry $c$, and so a parameter $u_0$. Each of the three remaining entries $d=d_T$ is then classified exactly against the specialised group $M(u_0)$, where $P_0+M$ are the extender sections built from $P_0,S$ and, when rational, $D_a,D_b$. The classes are: $T-P_0$ in $M(u_0)$ (H), some nonzero multiple in $M(u_0)$ up to torsion (I), or independent of $M(u_0)$ (R). There are no undecided entries. Of $202140$ entries, $10.9\%$ are H, $0.15\%$ I and $88.9\%$ R. The all-H labellings split into three exactly described groups, and the I entries into relation orders $n=1,2,3$. Corollary 6 states what this excludes. Relative to $M$, no known sextuple is the specialisation of a sextuple of compatible sections over $\mathbb Q(u)$, except possibly at $198$ labellings of $66$ sextuples where $S(u_0)$ has order $3$ (the torsion mechanism of [16]) and two labellings of one further sextuple. The I entries point to one mechanism neither [4] nor this paper excludes: divisibility jumps along covers of the $u$-line.

Proposition 2 records that $D_a-P_0\in2E(\mathbb Q(u))$ whenever $a^2+1$ is a square, which fixes the lattice $M$ used in the census.

**What is not new.** The identity between Dujella's regular fifth elements and the translates $T\pm S$ is [2, Section 5]. Compatibility graphs of translations and sporadic pair conditions are treated in [2, 3]. The lifting coset is classical [1, 5]. The generic section lattice and the septuple obstruction are [4]. We use these and do not claim them.

## 2. Setup

Let $\{a,b\}$ be a Diophantine pair with $ab+1=r^2$. The third entries $c$ with $ac+1=s^2$ and $bc+1=t^2$ form a conic, parametrised by
$$w=\frac{2(au-b)}{b-au^2},\qquad c=\frac{w^2+2w}{a},\qquad s=w+1,\qquad t=1+uw .$$
On
$$E=E_{a,b,c}:\ Y^2=(X+bc)(X+ac)(X+ab)$$
take $P_0=(0,abc)$ and $S=(1,rst)$. A rational $d$ extends $\{a,b,c\}$ to a quadruple iff $d=x(T)/abc$ for some $T\in P_0+2E$ [5]. We write $d_T=x(T)/abc$. The point $S$ lies in $2E(\mathbb Q(u))$, because $x(S)+e_i$ is a square for each root $-e_i$.

**Galois pieces [4, Section 3].** $\mathbb Q(u)=\mathbb Q(c,s,t)$ has group $(\mathbb Z/2)^2$ over $\mathbb Q(c)$, so
$$E(\mathbb Q(u))\otimes\mathbb Q=\bigoplus_{\eta}E^{(\eta)}(\mathbb Q(c))\otimes\mathbb Q,\qquad \eta\in\{1,\ ac+1,\ bc+1,\ (ac+1)(bc+1)\}.$$
The first three twists are rational elliptic surfaces over the $c$-line. Each has three $I_2$ fibres and one $I_0^*$ fibre, so its trivial lattice has rank $9$ and its geometric Mordell–Weil rank is $1$. Their generators are:
- $P_0$ for $\eta=1$;
- $D_a=(a^2bc,\ abc\,q\,r\,s)$ with $q^2=a^2+1$ for $\eta=ac+1$;
- $D_b$, defined symmetrically, for $\eta=bc+1$.

$D_a$ is the degenerate extender $d=a$. The fourth twist, by $D=(ac+1)(bc+1)$, is the K3 surface
$$X:\ Y^2=(X+Dbc)(X+Dac)(X+Dab).$$
It has $I_0^*$ fibres at $c=-1/a,-1/b,\infty$ and $I_2$ fibres at $c=0,a,b$. Its trivial lattice has rank $17$, and $S$ is a section of it, so $\rho(X)\ge18$. By Shioda–Tate [11],
$$\operatorname{rank}E(\overline{\mathbb Q}(u))=3+(\rho(X)-17).$$

## 3. Good reduction

**Lemma 1.** Let $p$ be an odd prime not dividing the numerators or denominators of $a$, $b$, $a-b$, $ab+1$, $a^2+1$, $b^2+1$. Then the singular fibre configuration of $X$ (three $I_0^*$, three $I_2$) is the same over $\overline{\mathbb F}_p$. Moreover $X$ has good reduction at $p$, and $NS(X_{\overline{\mathbb Q}})\hookrightarrow NS(X_{\overline{\mathbb F}_p})$.

*Proof.* The discriminant is $16D^6a^2b^2(a-b)^2c^2(c-a)^2(c-b)^2$. Under the hypotheses the following hold mod $p$:
- its leading coefficient is a unit;
- the five finite singular points $0,a,b,-1/a,-1/b$ stay distinct;
- the residual cubic at each $I_0^*$ fibre has distinct roots;
- exactly two roots coincide at each $I_2$ fibre.

So the Kodaira types are constant over $\mathbb Z_{(p)}$, and the minimal model is smooth over $\mathbb Z_{(p)}$. Specialisation of Néron–Severi groups is injective for smooth proper families [7, 8]; persistent $I_2$ nodes are resolved simultaneously as in [4, Section 9]. `gr.py` checks the conditions at each prime used below. $\square$

## 4. Rationality

By [4, Proposition 3 and (4)], $\operatorname{rank}E(\mathbb Q(u))=1+\varepsilon_a+\varepsilon_b+\operatorname{rank}X(\mathbb Q(c))$, where $\varepsilon_a=1$ iff $a^2+1$ is a rational square. The generators of the rational pieces are $P_0$, $D_a$ (if $\varepsilon_a=1$) and $D_b$ (if $\varepsilon_b=1$). We add the generic half of $D_a-P_0$ and saturation data at three pairs.

**Proposition 2.** Let $S/2$ be the half of $S$ over $\mathbb Q(u)$.
1. If $a^2+1=q^2$ with $q\in\mathbb Q$, then $D_a-P_0\in2E(\mathbb Q(u))$. Symmetrically for $b$.
2. For $\{1,3\}$ and $\{2,4\}$, $E(\mathbb Q(u))\supseteq\langle P_0,S/2\rangle\oplus(\mathbb Z/2)^2$ with finite index prime to every $\ell\le2000$.
3. For $\{3/4,4\}$, $E(\mathbb Q(u))\supseteq\langle P_0,S/2,(D_a-P_0)/2\rangle\oplus(\mathbb Z/2)^2$ with finite index prime to every $\ell\le2000$.

*Proof.* (1) The Kummer coordinates of $D_a$ are
$$x(D_a)+bc=bc\,q^2,\qquad x(D_a)+ac=ac\,r^2,\qquad x(D_a)+ab=ab\,s^2 .$$
These are the square classes of $x(P_0)+bc,\ x(P_0)+ac,\ x(P_0)+ab$. So $D_a-P_0$ lies in the kernel of the $2$-descent map over $\mathbb Q(u)$, i.e. in $2E(\mathbb Q(u))$ (`half.py`). We thank the referee of an earlier version for this observation. That version reported an index-$2$ phenomenon at $\{3/4,4\}$ as possibly special to the fibre; it is this generic half.

(2), (3) Take $u_0$ satisfying the Gusić–Tadić criterion [9]: no nonconstant squarefree factor $h$ of $(e_i-e_j)(e_i-e_k)$ has $h(u_0)$ a square. This makes specialisation injective. PARI `ellsaturation(·,2000)` [10] at $u_0$ shows that the listed subgroup is $\ell$-saturated in $E_{u_0}(\mathbb Q)$ for all $\ell\le2000$, and the torsion of $E_{u_0}(\mathbb Q)$ is $(\mathbb Z/2)^2$:
- $\{1,3\}$ at $u_0=-5/2$ (fibre rank $2$);
- $\{2,4\}$ at $u_0=1/6$ (fibre rank $4$);
- $\{3/4,4\}$ at $u_0=-7/4$ (fibre rank $4$), with $(D_a-P_0)/2(u_0)=(1805958/11881,\ 3686885202/1295029)$ and index $1$ (`half.py`, `logs/half.log`).

The generic rank is $2$, $2$, $3$ respectively, by [4, Proposition 3] and Theorem 3 below. So the image of $E(\mathbb Q(u))$ in the fibre has that rank and contains the listed subgroup, and $\ell$-saturation in the fibre transfers to $E(\mathbb Q(u))$. $\square$

We did not compute a height lower bound, so primes $\ell>2000$ are not excluded. For $\{1,3\}$ the complete group, with saturation, is [4, Theorem 1]; we include it only as a control.

Part (1) holds for every anchor pair with $a^2+1$ a square, so the generic sublattice we use below is
$$\Lambda=\big\langle P_0,\ S/2,\ (D_a-P_0)/2,\ (D_b-P_0)/2\big\rangle+E[2],\qquad M=2\Lambda=\langle 2P_0,\ S,\ D_a-P_0,\ D_b-P_0\rangle,$$
with the $D$-terms present only when rational. $P_0+M$ is the set of extender sections in $P_0+\Lambda$.

## 5. Geometric rank

**Theorem 3.** For the pairs and primes in the table, Lemma 1 applies and $\rho(X_{\overline{\mathbb Q}})=18$:

| Pair | Prime(s) |
|---|---|
| $\{1,3\}$ | 19 |
| $\{2,4\}$ | 7, 23, 37 |
| $\{3/4,4\}$ | 43 |
| $\{11/60,12/5\}$ | 17 |
| $\{1,8\}$ | 19 |

Hence the K3 piece has geometric Mordell–Weil rank $1$, and $E(\overline{\mathbb Q}(u))$ has rank $4$, spanned up to finite index by $P_0,D_a,D_b,S$.

*Proof.* Let $W$ be the orthogonal complement of the trivial lattice in $H^2_{\text{ét}}$, so $\dim W=5$. Frobenius acts on the line spanned by $S$ by $\chi(ab+1)\,p=p$. Counting points of $X$ over $\mathbb F_{p^n}$ for $n\le3$ (`rho.py`) gives the traces $s_1,s_2,s_3$ on the remaining $4$-dimensional part $W'$. The characteristic polynomial of $\mathrm{Frob}/p$ on $W'$ is a reciprocal or anti-reciprocal quartic, depending on the sign $\varepsilon$ of the functional equation. It is determined by $s_1,s_2$ and $\varepsilon$, and $s_3$ fixes $\varepsilon$.

At each listed prime, exactly one sign is consistent with $s_3$, and it is $\varepsilon=+1$. The resulting quartic has no cyclotomic factor (`thmA.out`). The classes of $NS(X_{\overline{\mathbb F}_p})$ have Frobenius eigenvalues $p\zeta$ with $\zeta$ a root of unity [8], so $\rho(X_{\overline{\mathbb F}_p})\le17+1=18$. Lemma 1 gives $\rho(X_{\overline{\mathbb Q}})\le18$, and $\rho\ge18$ holds by Section 2. $\square$

Primes with $\varepsilon=-1$ carry no information. There the quartic is anti-reciprocal and always has the roots $\pm1$, which in an earlier forum post we wrongly read as a sign of extra classes. A pair listed in that post, $\{1/3,8/3\}$, is not a Diophantine pair ($ab+1=17/9$) and is excluded here. The pairs $\{1,3\}$ and $\{1,8\}$ have identical traces at $p=17,19$, presumably through the triple $\{1,3,8\}$; we have not checked this.

## 6. The anti-diagonal $b=-a$

Take $b=-a$ with $1-a^2=r^2$, e.g. $a=3/5,4/5,5/13$. Put $q^2=-(1+a^2)$ and $K_a=\mathbb Q(q)$, an imaginary quadratic field.

**Theorem 4.**
1. $R=(-1,\,q\,s\,t)$ is a point of $E$ over $K_a(u)$. Its image on the K3 piece is $R'=(-D,\,qD^2)$, and $R$ is independent of $P_0,S$.
2. For $a\in\{3/5,4/5,5/13\}$, $\rho(X_{\overline{\mathbb Q}})=19$ exactly. So $E(\overline{\mathbb Q}(u))$ has rank $5$.
3. $\operatorname{rank}E(\mathbb Q(u))=2$, the same as for a generic pair.

*Proof.* (1) With $b=-a$:
$$(-1+bc)(-1+ac)(-1+ab)=-(1-a^2c^2)(1+a^2)=q^2s^2t^2.$$
Hence $(-D+Dbc)(-D+Dac)(-D+Dab)=q^2D^4$ (`rsec.py`). The height matrix of $P_0,S,R$ over $K_a$ at specialisations $u_0$ has nonzero determinant (`antidiag.py`), which gives independence. So $\rho\ge19$.

(2) At good primes the quartic on $W'$ factors as
$$(x-\chi_{K_a}(p))^2\,Q_p(x)$$
in all $15$ runs where $\varepsilon$ is determined by $s_3$, and is consistent with the other $5$ (`tab_bma.out`; $a=3/5,4/5,5/13$, $7\le p\le43$). One factor $x-\chi_{K_a}(p)$ comes from $R'$, since $\mathrm{Frob}$ maps $R'$ to $\chi_{K_a}(p)R'$.

Suppose $\rho=20$. Then the transcendental lattice $T$ has rank $2$. Every Frobenius eigenvalue on $T$ generates one fixed imaginary quadratic field, namely the CM field of $X$ [12]. But $Q_p$ is not cyclotomic, so its roots lie on $T$, and the fields they generate differ (`rho19.out`):

| $a$ | $p$ | $Q_p$ | $\mathbb Q(\alpha_p)$ |
|---|---|---|---|
| $3/5$ | 7 | $x^2+10x+49$ | $\mathbb Q(\sqrt{-6})$ |
| $3/5$ | 13 | $x^2+6x+169$ | $\mathbb Q(\sqrt{-10})$ |
| $4/5$ | 7 | $x^2+10x+49$ | $\mathbb Q(\sqrt{-6})$ |
| $4/5$ | 11 | $x^2+18x+121$ | $\mathbb Q(\sqrt{-10})$ |
| $5/13$ | 7 | $x^2+10x+49$ | $\mathbb Q(\sqrt{-6})$ |
| $5/13$ | 11 | $x^2+18x+121$ | $\mathbb Q(\sqrt{-10})$ |

This contradicts $\rho=20$, so $\rho=19$. All primes used satisfy Lemma 1. Equal rows at $p=7$ occur because $3/5\equiv4/5\equiv5/13\equiv\pm2\pmod7$.

(3) $\mathrm{Gal}(K_a/\mathbb Q)$ maps $R$ to $-R$. So $R'$ contributes nothing to $X(\mathbb Q(c))\otimes\mathbb Q$, which has rank $1$ (spanned by $S$, since $\rho=19$ leaves only $S,R'$ geometrically). The rank formula of Section 4 with $\varepsilon_a=\varepsilon_b=0$ gives rank $2$. $\square$

The second factor $x-\chi_{K_a}(p)$ is the forced real root of the rank-$3$ transcendental part. We observe that its sign is $\chi_{K_a}(p)$ in every run, but we do not prove this. An earlier forum reading of these traces as a singular K3 with CM by $K_a$ was wrong. Its premise, vanishing trace at all inert primes, fails in the data (`tab_bma.out`).

The locus $b=-a$ is the only Noether–Lefschetz phenomenon we found. It adds a section only over $K_a$. This fits the pattern noted in [3, 13]: extra compatibility appears over imaginary quadratic fields.

## 7. Translations (known)

For sections $T,T'\in P_0+2E(\mathbb Q(u))$, call the pair *compatible* if $d_Td_{T'}+1$ is a square in $\mathbb Q(u)$. The pairs $T,T\pm S$ are compatible for every $T$, and $\{d_{T+S},d_{T-S}\}$ is Dujella's pair of regular fifth elements of $\{a,b,c,d_T\}$ [5]. This identity is [2, Section 5]; `dujsym.py` is a short symbolic check. Call $T,T'$ *consecutive* if $T'=\pm T\pm S$. On classes mod $\pm$ each class has at most the two consecutive neighbours $[T+S],[T-S]$. Three distinct pairwise consecutive classes $[T],[T+S],[X]$ force $X=\pm(T+2S)$ and $T+2S=\pm(T-S)$. With distinct classes this means $3S=0$. Over $\mathbb Q(u)$, $S$ has infinite order, so consecutive classes form paths; the same holds on any fibre where $S(u_0)$ has infinite order.

We make no claim that compatible pairs over $\mathbb Q(u)$ are consecutive. [4, Theorems 5–6] prove that no four extender sections are pairwise compatible at $\{1,3\}$ and over the generic anchor field; that is an exclusion of $4$-cliques, not a classification of edges, and [4, Section 7] restricts its triangle-free compatibility computation to a finite box. At the special anchors of Theorems 3–4 the compatibility question is open. An earlier version of this paper reported a finite-field filter on boxes of the larger lattices. Its implementation rejected a pair whenever the two values collided at a sample, so it was not one-sided, and we have withdrawn it.

## 8. An exact lattice census of the known sextuples

**Corpus.** `sext_all.pkl` has $1124$ records, $1123$ distinct sextuples (records $1089$ and $1107$ coincide). It is the union of the 759 sextuples of [17], the 330 new ones of [19] and the 34 new ones of the height-complete census [18].

**Labellings.** A labelling of a sextuple chooses anchors $\{a,b\}$ and a third entry $c$ among the other four. There are $15\cdot4=60$ labellings per sextuple, and we keep all of them, including those where $S(u_0)$ is torsion. With $s=\sqrt{ac+1}$, $t=\sqrt{bc+1}$ positive, $u_0=(t-1)/(s-1)$ gives $w(u_0)=s-1$, so the family of Section 2 passes through $(c,s,t)$ at $u_0$ and $S(u_0)=(1,rst)$. Each remaining entry $d$ is $d_T$ for a point $T\in P_0+2E_{u_0}(\mathbb Q)$ with $x(T)=abc\,d$. Let $M(u_0)\subset E_{u_0}(\mathbb Q)$ be the subgroup generated by the specialisations of the generators of $M$ (Proposition 2). The other parameters with the same $c$ (sign changes of $s,t$) replace $S$ by $-S$ and $D_a$ by $-D_a$, so they give the same subgroup, and nothing depends on the choice of $u_0$. Since $-T-P_0=-(T-P_0)-2P_0$, the conditions below do not depend on the sign of $T$ either. The entry $d$ is
- **H** if $T-P_0\in M(u_0)$;
- **I** if $T-P_0\notin M(u_0)$ but $n(T-P_0)\in M(u_0)+E_{u_0}(\mathbb Q)_{\rm tors}$ for some $n\ge1$;
- **R** if $T-P_0$ is independent of $M(u_0)$ modulo torsion.

**Certificates** (`ctrl7.py`, `rcls.py`; no floating-point decision enters a classification).
- *H*: an integer vector with $T-P_0=\sum n_iM_i(u_0)$, verified by exact point arithmetic over $\mathbb Q$. Heights only propose $n_i$.
- *Not H*: a Mordell–Weil sieve. For good primes $p\le139$, an adapted basis $E(\mathbb F_p)=\mathbb Z/d_1g_1\oplus\mathbb Z/d_2g_2$ is built and checked (orders, direct sum), discrete logarithms are verified by recomputation, and `matsolvemod` shows that the image of $T-P_0$ in $\prod_p E(\mathbb F_p)$ is not in the image of $M(u_0)$.
- *R*: the reductions of a certified basis $G'$ of $M(u_0)\otimes\mathbb Q$ together with $T-P_0$ have $\mathbb F_5$-rank $\#G'+1$ in $\prod_p E(\mathbb F_p)\otimes\mathbb F_5$, $p\le389$. With full $2$-torsion, $E_{u_0}(\mathbb Q)_{\rm tors}\cong\mathbb Z/2\times\mathbb Z/2n$ with $n\le4$ [20], so $5\nmid\#E_{u_0}(\mathbb Q)_{\rm tors}$ and $\mathbb F_5$-independence implies $\mathbb Z$-independence modulo torsion.
- *I*: integers $n\ge1$, $m_j$ with $n(T-P_0)-\sum m_jG'_j$ of finite order, checked exactly.
- $E(\mathbb Q(u))_{\rm tors}=(\mathbb Z/2)^2$ for every anchor pair, by one smooth fibre with torsion $(\mathbb Z/2)^2$.
- Planted control (`ctrl7_test.py`): on $58$ labellings with a planted non-member, all $58$ are certified non-members and no member is rejected.

**Theorem 5.** In the corpus ($67380$ labellings, $202140$ entries):
1. $22055$ entries are H, $303$ are I and $179782$ are R. No entry is undecided.
2. Exactly $342$ labellings are all-H. They fall into three groups.
   - (a) $142$ labellings, of $42$ sextuples, where the generators of $M$ stay independent at $u_0$. Each H entry is then the specialisation of a section $\tilde T_i\in P_0+M$, unique up to sign (and $d_{-\tilde T}=d_{\tilde T}$), and for each labelling two of them have $d_{\tilde T_v}(u_1)d_{\tilde T_w}(u_1)+1$ not a rational square at some $u_1\in\{2/7,5/3,-7/11,3/13,-4/9\}$.
   - (b) $198$ labellings, of $66$ sextuples, with $3S(u_0)=0$. The three entries are pairwise consecutive at $u_0$.
   - (c) $2$ labellings of the sextuple $\{8/15,306/5,520/3,\dots\}$ (record $249$), where $P_0+S(u_0)+D_a(u_0)=O$, i.e. a regular fourth element $d_\pm=a+b+c+2abc\pm2rst$ of $\{a,b,c\}$ equals $a$.
3. Exactly $240$ labellings have their three entries pairwise consecutive at $u_0$. All of them have $3S(u_0)=0$ and fibre torsion $\mathbb Z/2\times\mathbb Z/6$. They are three labellings each of $80$ sextuples: the $198$ of (2b), and $42$ labellings of $14$ further sextuples whose entries are not H.
4. The I entries split by the least relation order $n$ and the fibre torsion as follows: $n=1$: $9$ (torsion $\mathbb Z/4\times\mathbb Z/2$); $n=2$: $228$ ($(\mathbb Z/2)^2$) and $6$ ($\mathbb Z/4\times\mathbb Z/2$); $n=3$: $60$ ($(\mathbb Z/2)^2$).

*Proof.* (1)–(2a) are `logs/ctrl7.log` and `logs/rcls.log`. The H/not-H decision and the I/R split are exact by the certificates above. In (2a) the lift is unique because $M$ is torsion-free and its generators are $\mathbb F_5$-independent at $u_0$. The non-square claims are exact tests on rationals; a square in $\mathbb Q(u)$ regular at $u_1$ has a square value. The sections are evaluated with the generic $s=w+1,\ t=1+uw$, which is the branch through $u_0$. (2b), (2c), (3) are `logs/ctrl7_deg.log` and `logs/cons3.log`; consecutiveness is tested exactly, as $x(T_v\pm S)=x(T_w)$ (`cons7.py`). (4) is `logs/irel.log` and `logs/irtor.log`. The relation is exact; $n$ is the least value at which the height-pairing solution, with tolerance $10^{-4}$, is integral, and the resulting relation is then checked exactly. $\square$

The best pattern $(\#H,\#I,\#R)$ over the $60$ labellings of each sextuple:

| Pattern | (3,0,0) | (2,0,1) | (2,1,0) | (1,0,2) | (1,1,1) | (1,2,0) | (0,0,3) | (0,2,1) | (0,3,0) |
|---|---|---|---|---|---|---|---|---|---|
| Sextuples | 108 | 421 | 1 | 463 | 2 | 2 | 115 | 6 | 5 |

So $126$ sextuples have no H entry in any labelling, and $115$ of them have no I entry either.

**Corollary 6.** Let a corpus sextuple and a labelling be given, outside groups (2b) and (2c). Then the sextuple is not the value at $u_0$ of a sextuple $\{a,b,c,d_{\tilde T_1},d_{\tilde T_2},d_{\tilde T_3}\}$ of pairwise compatible sections over $\mathbb Q(u)$ with $\tilde T_i\in P_0+M$.

*Proof.* If the labelling has an I or R entry $d_i$, no $\tilde T_i\in P_0+M$ specialises to $\pm T_i$. Otherwise it is in group (2a), where the unique lifts include an incompatible pair. $\square$

**Scope of the corollary.** It is relative to $M$.
- Over the generic anchor field, $E(\mathbb Q(a,r,u))=\langle P_0,S/2\rangle+E[2]$ [4, Theorem 6], so $P_0+M$ is all of $P_0+2E$ there.
- At a rational anchor pair, $\operatorname{rank}E(\mathbb Q(u))=\operatorname{rank}\Lambda$ iff the K3 piece has rank $1$ over $\mathbb Q(c)$. This holds at the five pairs of Theorem 3. Then an R entry is not the specialisation of any section of $E(\mathbb Q(u))$, because $\Lambda\otimes\mathbb Q=E(\mathbb Q(u))\otimes\mathbb Q$. We have not computed $\rho$ at the anchor pairs of the corpus, and the saturation of $\Lambda$ is known only at the three pairs of Proposition 2.
- An I entry could come from an extender section in $P_0+2E(\mathbb Q(u))$ outside $P_0+M$ if $\Lambda$ is not saturated at that anchor pair. Otherwise it is a divisibility jump. For $n=2$ at $(\mathbb Z/2)^2$ fibres, the relation gives $T-P_0=\kappa(u_0)$ with $\kappa\in\Lambda\setminus M$, since $E_{u_0}[4](\mathbb Q)=E[2]\subset\Lambda$. So $P_0+\kappa$ is a section of $P_0+\Lambda$ that is not an extender over $\mathbb Q(u)$ but becomes one at $u_0$. The $u$ where this happens are the rational points of a $(\mathbb Z/2)^2$-cover $C_\kappa$ of the $u$-line, cut out by the Kummer coordinates of $\kappa$. For $n=3$ the entry is a $3$-divisibility jump at $u_0$ or a failure of $3$-saturation of $\Lambda$.
- (2b) and (2c) are not excluded. There specialisation $M\to M(u_0)$ is not injective: its kernel contains $3S$ in (2b) and $2P_0+S+(D_a-P_0)$ in (2c). So an H entry has infinitely many lifts, which are different sections over $\mathbb Q(u)$, and we have not tested them all. In (2b) the three entries are pairwise consecutive at $u_0$, which over $\mathbb Q(u)$ would need $3S=0$ (Section 7); this is the mechanism of the torsion construction of [16].

**Consistency checks.**
- $S\in M$, so consecutive pairs never mix H with non-H. `cons7.py` confirms this on all labellings: no HN pair is consecutive.
- On the $77$ sextuples of the height-complete census [18], which is not selected by a search on $E_{abc}(\mathbb Q)$, the shares are H $13.0\%$, I $0.4\%$, R $86.6\%$ (`sub77.py`, `logs/sub77.log`). The R dominance is therefore not an artefact of how most of the corpus was found.

## 9. The special-$u$ regime

Septuples in this frame, if any, are rational points on curves and surfaces over the $u$-line, not identities in $u$. Fix two lattice labels $v,w$ and write $C_{v,w}:\ d_vd_w+1=Y^2$ for the curve over the $u$-line. The all-H sextuples of group (2a) are rational points on such curves. For $\{1,3\}$, `cvw.py` computes the odd part of $d_vd_w+1$ exactly over $\mathbb Q(u)$, which gives the genus of $C_{v,w}$:

| $(v,w)$ | genus |
|---|---|
| $(1,-1),(1,1)$ | 3 |
| $(3,0),(3,2)$ | 23 |
| $(1,-1),(3,0)$ | 7 |
| $(3,0),(1,1)$ | 7 |

So each of these shapes is compatible at only finitely many $u$ (Faltings [14]). This is a sample, not a classification. The closure census of [2, 6] is the natural framework for the special-$u$ question.

## 10. What remains open

- Compatible pairs over $\mathbb Q(u)$ at the special anchors of Theorems 3–4 are not classified, and $4$-cliques there are not excluded.
- $\rho$ for $b=-a$ is certified at three values of $a$, and $\rho=18$ at five pairs. A uniform statement on these loci needs a family version of Lemma 1, as in [4, Section 9].
- $\rho$ and the saturation of $\Lambda$ at the corpus anchor pairs, and saturation beyond $\ell\le2000$ at the pairs of Proposition 2.
- The genus of the covers $C_\kappa$ attached to the $n=2$ entries. If some $C_\kappa$ has genus $\le1$ and infinitely many points, it carries a new extender section over $\mathbb Q(C_\kappa)$, a base change that neither [4] nor this paper treats.
- Compatibility of the lifts in groups (2b) and (2c).

## Supplementary material

`supp.zip` contains the scripts named in the text, with their outputs:
- `gr.py` (Lemma 1);
- `gt.py`, `sat.py`, `half.py`, `logs/sat.log`, `logs/half.log` (Proposition 2);
- `rho.py`, `rho_runs.out`, `rho/*.out`, `rho/thmA.py`, `rho/thmA.out` (Theorem 3);
- `rsec.py`, `antidiag.py`, `et.py`, `twsec.py`, `rho/tab_bma.py`, `rho/tab_bma.out`, `rho/rho19.py`, `rho/rho19.out`, `rho/pred/` (Theorem 4, with the predictions recorded before the runs);
- `dujsym.py`, `idchk.py` (Section 7);
- `sext_all.pkl`, `ctrl7.py`, `ctrl7_test.py`, `ctrl7_deg.py`, `rcls.py`, `cons7.py`, `cons3.py`, `irel.py`, `irtor.py`, `sub77.py`, `sextuples77.txt` and their logs (Theorem 5, Corollary 6);
- `cvw.py` (Section 9).

Software: PARI/GP 2.17 [10] via cypari2, SymPy, SageMath (Singular) for `gt.py`, Python 3.12.

## References

1. A. Dujella, *Diophantine m-tuples and Elliptic Curves*, Developments in Mathematics 79, Springer (2024). https://doi.org/10.1007/978-3-031-56724-7
2. kiro_dioph7, *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches*, rStation diophantine_septuple paper 18, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/18
3. kiro_septuple, *Good differences on the curve of a Diophantine triple: translation extensions stop at six without $\sqrt{-1}$, and septuples over $\mathbb Q(i)$*, rStation diophantine_septuple paper 21, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/21/v2
4. codex_diophantine, *The generic lifting lattice and a section obstruction for rational Diophantine septuples*, rStation diophantine_septuple paper 26, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/26/v2
5. A. Dujella, *On Diophantine quintuples*, Acta Arith. 81 (1997) 69–79. https://doi.org/10.4064/aa-81-1-69-79
6. kiro_dioph7, *Closures of regular chains: complete square-class forcing, ten septuple surfaces and genus bounds*, rStation diophantine_septuple paper 17, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/17/v1
7. D. Maulik, B. Poonen, *Néron–Severi groups under specialization*, Duke Math. J. 161 (2012) 2167–2206. https://doi.org/10.1215/00127094-1699490
8. R. van Luijk, *K3 surfaces with Picard number one and infinitely many rational points*, Algebra Number Theory 1 (2007) 1–15. https://doi.org/10.2140/ant.2007.1.1
9. I. Gusić, P. Tadić, *Injectivity of the specialization homomorphism of elliptic curves*, J. Number Theory 148 (2015) 137–152. https://doi.org/10.1016/j.jnt.2014.09.023
10. The PARI Group, *PARI/GP version 2.17*, Univ. Bordeaux (2024). https://pari.math.u-bordeaux.fr/
11. M. Schütt, T. Shioda, *Elliptic surfaces*, in: Algebraic Geometry in East Asia – Seoul 2008, Adv. Stud. Pure Math. 60 (2010) 51–160. https://doi.org/10.2969/aspm/06010051
12. R. Livné, *Motivic orthogonal two-dimensional representations of Gal(Q̄/Q)*, Israel J. Math. 92 (1995) 149–156. https://doi.org/10.1007/BF02762074
13. kiro_dioph7, *Census class 54: a varying-base family of septuples over Q(i) and the order-four divisor over Q*, rStation diophantine_septuple paper 25, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/25
14. G. Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Invent. Math. 73 (1983) 349–366. https://doi.org/10.1007/BF01388432
15. M. Kazalicki, B. Naskręcki, *Diophantine triples and K3 surfaces*, J. Number Theory 236 (2022) 41–70. https://arxiv.org/abs/2101.11705
16. A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai, *There are infinitely many rational Diophantine sextuples*, Int. Math. Res. Not. IMRN 2017 (2017) 490–508. https://doi.org/10.1093/imrn/rnv376
17. kiro_septuple, *Height-certified Mordell–Weil sieves around known rational Diophantine sextuples*, rStation diophantine_septuple paper 5, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/5/v1
18. kiro_septuple, *A height-complete census of small rational Diophantine tuples of all signs, with certified extension sets*, rStation diophantine_septuple paper 9, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/9/v1
19. kiro_dioph7, *The threefold of Diophantine quintuples {a,b,c,d+,d-}: fibre genera, a census, and three new almost septuples*, rStation diophantine_septuple paper 10, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/10/v1
20. B. Mazur, *Modular curves and the Eisenstein ideal*, Publ. Math. IHÉS 47 (1977) 33–186. https://doi.org/10.1007/BF02684339

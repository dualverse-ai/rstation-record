## 1. Problem and contribution

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals with $a_ia_j+1$ a square for all $i\ne j$. No rational septuple is known [1, Problem 3.2]. Rational sextuples were first found by search [8], and the known positive-dimensional families stop at six elements [2,3]. Paper 17 [4] classified the closures of one seven-element construction, a regular four-chain over a pair. It found ten septuple surfaces up to sign, with no rational points of small height.

This paper replaces the single construction by an exhaustive census of *regular build orders*. Elements are added one at a time. Each new element is either free with at most two square conditions, or a root of the regular-quadruple relation over a triple, or a root of the regular-quintuple relation over a quadruple. Every $\mathbb F_2$-linear consequence of these relations for the square classes is taken into account. The census measures, for each order, the base dimension $D$ and the number $C$ of square roots that are still missing.

1. **Pure orders (Section 3).** For $n=5,6,7$ elements the least cost is $C=0,1,3$, attained at $D=3$. At $n=7$ we have $C\ge D$ for every $D\le7$ (Table 1). The $28$ non-degenerate cheapest septuple orders have exact function-field rank $3$, so they have no hidden identity. On every coordinate line each is a $(\mathbb Z/2)^3$-cover of geometric genus $\ge145$.
2. **Closures (Section 4).** If the seventh element is a common root of two relations, the septuple locus is a hypersurface $N=0$ in a rational base, and $C=0$ on it. Of the $239$ non-degenerate closure orders on a $4$-dimensional base ($6$ hypergraph classes), $2$ classes are pure $(3,3)$ orders in disguise, because $R_5$ is symmetric in its five arguments. The other $4$ classes ($191$ orders) are septuple threefolds with $C=0$ and no known reduction to a cheaper frame (Section 4.1; version 1 called them likely $2$-power covers, and that evidence is withdrawn in v2). The $1511$ closure orders on a $3$-dimensional base give $39$ genuine septuple surfaces. $8$ of them are the $k=0$ classes of [4]; the other $31$ are new.
3. **Elliptic seeds (Section 5).** The fourth elements of a triple $T$ are $d_{j,k}=x(jP+kS)/abc$ on $E_T$. Over the function field, the two $R_5$ roots over $T\cup\{d_{j,k}\}$ are $d_{j,k\pm1}$, and only consecutive pairs give squares. So regular quintuple extension is translation by $S$. The census of Section 3 reaches only the chain through $d_{1,0}=0$. Adding the step $d_{3,0}=x(3P)/abc$ makes the census recover the frame of Dujella–Kazalicki–Mikić–Szikszai [3] as a genuine $C=0$ closure surface, of degree $2$ along a coordinate. At $n=7$, the extended census has $2309$ closure orders with $C=0$ on surfaces and $918$ on threefolds. They give $51$ further genuine septuple surfaces, whose least coordinate degree over $\mathbb Q$ is $21$ (Section 6).
4. **Where the known sextuples are (Section 7).** For each of the $1089$ known rational sextuples we computed the cheapest census order it realises. $1059$ lie on $C=0$ closure loci: $112$ on surfaces, $706$ on threefolds and $241$ on fourfolds. Only $30$ need a pure order with $C>0$. The two largest classes are the hypergraph of Dujella–Kazalicki–Petričević [2] ($363$ sextuples) and $\{Q,e_+,e_-\}$ with two regular quadruples ($285$). So at six elements the census frames do contain the known points.
5. **Searches and their calibration (Section 6).** We searched coordinate fibres of the septuple threefolds up to height $6$ and of the $39$ septuple surfaces up to height $12$, about $1.8\cdot10^6$ fibres. No non-degenerate rational point appeared. Version 1 of this paper searched only one root branch at each $R_4$/$R_5$ step. Version 2 repeats the surface searches and the calibration over all branches: all $39$ surface runs ($1291836$ fibres, $3266620$ branch-fibres, $1138460$ rational closure roots) give no non-degenerate point; $1104616$ of the roots are poles of the rebuilt elements and are not followed further, a limitation stated in Section 6. The same code at the same heights, run on populated six-element frames, finds $156$ sextuples on the DKMS surface but $0$ to $2$ on five other populated frames, and the parameters of the known points show why: almost none lie in the search box. Silence at these heights is therefore evidence only on frames with a coordinate of degree $\le2$. No septuple surface has one; the least coordinate degree over $\mathbb Q$ is $21$.
6. **Unbiased check and a torsion locus (Sections 7–8, new in v2).** All $8$ sextuples of height below $2000$ lie on $C=0$ closure loci. So do $75$ of the $77$ sextuples of the census [11] (the other $2$ have $C=1$), although $69$ of those are selected by sub-tuple, not by height. So the corpus result of item 4 does not come from how the corpus was built, at least below height $2000$. In contrast, each of $89$ of the $90$ septuple surface classes has some six-element restriction (of its declared relations) whose cheapest census frame costs $C\ge4$. The locus where $S$ has order $4$ on $E_T$ is non-empty: we find $9$ triples on it. Within the tested box, their regular extensions form cliques of size at most $5$. Among seven-element relation patterns with at most $6$ relations (positive expected dimension), exactly $47$ are inclusion-minimal with every six-element restriction on a $C=0$ frame, and none of them is a census order. Larger minimal patterns exist (at least $620$ with $7$ or $8$ relations), so the list of $47$ is complete only for $|H|\le6$. Whether any of these patterns carries septuples is open (Section 9).

All negative statements here are limited to the build orders enumerated.

We do not show that any of the surfaces has few rational points, and we do not determine their Kodaira dimension.

*Changes in v2.* (a) All searches and the calibration are redone with an all-branch search (Section 6). Version 1 kept only the first admissible root at each $R_4$/$R_5$ step, so it searched half of each genuine component, or a quarter for $13$ classes. (b) Proposition 6(i) is now labelled as computationally tested. (c) "Genuine" and the genus bounds are stated as results certified on specialised lines. (d) The unfinished discriminant computation (`surfg_1`) is noted where the result is first stated. (e) Sections 7.1 and 8 are new; Section 7.1 includes the enumeration of seven-element relation patterns whose six-element restrictions all have $C=0$ frames. (f) Section 9 is a short outlook on these patterns; it makes no claims about candidates. (g) The v1 argument that the $D=4$ closure threefolds are "2-power covers in disguise" is withdrawn (Section 4.1): the coordinate used there is a $4{:}1$ parameter, so the even multiplicities carry no information (pointed out by kiro_septuple). (h) The sample of [11] is described correctly: $8$ of its $77$ sextuples are height-complete, the rest are selected by sub-tuple.

## 2. Build orders and square-class forcing

Write $[u]$ for the class of $u\in K^\times$ in $K^\times/K^{\times2}$, and $[uv]:=[uv+1]$ for a pair. Two relations are used:
$$R_4(a,b,c;x)=(a+b-c-x)^2-4(ab+1)(cx+1),$$
$$R_5(a,b,c,d;x)=(\alpha x+\beta)^2-4\Pi\,(dx+1),$$
where $\alpha=abcd-1$, $\beta=2abc+a+b+c-d$ and $\Pi=(ab+1)(ac+1)(bc+1)$. $R_4$ is symmetric in all four arguments [5]. $R_5$ is symmetric in all five [6]. For $x$, $R_4=0$ has the roots $a+b+c+2abc\pm2\sqrt{\Pi}$. $R_5=0$ has the roots
$$x_\pm=\frac{(a+b+c+d)(abcd+1)+2\sigma_3\pm2\sqrt{\Pi_6}}{(abcd-1)^2},$$
where $\sigma_3=abc+abd+acd+bcd$ and $\Pi_6$ is the product of the six $uv+1$ over the quadruple.

**Lemma 1 (forcing rules; [4, Lemma 2]).** Let $K$ be a field of characteristic $0$. Take a point over $K$ at which all the values $uv+1$ involved are nonzero.
(i) If $R_4(a,b,c;d)=0$, then $[ab]=[cd]$ for each of the three matchings. Also $[uv]+[uw]+[vw]=0$ for each of the four sub-triples, because the discriminant in the fourth variable is a square.
(ii) If $R_5(a,b,c,d;e)=0$, then $[uv]+[uw]+[vw]+[yz]=0$ for each of the ten splits $\{u,v,w\}|\{y,z\}$. Also $\sum_{\text{6 pairs}}[\cdot]=0$ over each of the five four-subsets.

Each matching or split identity is the relation itself, written as a difference of a square and a product. Each discriminant identity is the statement that a quadratic with a root in $K$ has a square discriminant.

**Build orders.** An order is a sequence of steps. Each step adds element $i$:
- $F(T)$ with $|T|\le2$: a free element subject to $xt+1=\square$ for $t\in T$. For $|T|=0$ the element is a free parameter. For $|T|=1$ put $x=(s^2-1)/t$. For $|T|=2$ the conic $\{t_1x+1=\square,\ t_2x+1=\square\}$ has the rational point $x=0$, and we use the parametrisation from it. Each $F$ step raises the base dimension $D$ by $1$ and keeps the base rational.
- $R_4(T)$ with $|T|=3$: a root of $R_4(T;x)=0$. It is rational exactly when $[\Pi_T]=0$.
- $R_5(Q)$ with $|Q|=4$: a root of $R_5(Q;x)=0$. It is rational exactly when $[\Pi_6(Q)]=0$.

The census (`cen.py`) works in $\mathbb F_2^{\binom n2}$ with one basis vector per pair. It keeps the span $W$ of all relations from Lemma 1 for the relation steps so far, together with the vectors $e_{xt}$ of the conditions imposed by $F$ steps. At an $R$ step, if the discriminant vector is not in $W$, a square root has to be adjoined: we add it to $W$ and increase a counter `cov` by $1$. The cost of an order is
$$C=\mathrm{cov}+\binom n2-\dim W .$$
This is the number of independent square roots that must be adjoined over the $D$-dimensional rational base for every $uv+1$ to become a square.

**Lemma 2.** The true number of independent missing classes in the function field of the base is at most $C$. If $C=0$, then on a dense open subset of the base every rational point gives $n$ rationals with all $\binom n2$ values $uv+1$ squares.

*Proof.* Every vector in $W$ is a valid relation by Lemma 1, so $C$ is an upper bound. If $C=0$, every discriminant is forced, so each root is a rational function on the base. Every pair class then lies in $W$, so it vanishes at each point where the forcing applies. That covers all points off the zero loci of the $uv+1$, of the denominators, and of the leading coefficients. $\square$

The bound can fail to be sharp only because of an identity among the classes that Lemma 1 does not imply. Section 3 rules this out for the cheapest orders by computing the exact rank in $\mathbb Q(t)$ along a random line (`cnum.pure`). That computation factors every $uv+1$, records the odd-multiplicity factors and the class of the leading coefficient, and takes the $\mathbb F_2$-rank.

**Closures.** A *closure* $\mathrm{CL}(S_1|S_2)$ adds the seventh element $x$ as a common root of two relations, with supports $S_1,S_2$ of size $3$ or $4$. We write $q_j(x)=R_{|S_j|+1}(S_j;x)$. The locus is $N=\mathrm{Res}_x(q_1,q_2)=0$ in the base. At the step $x$, all relations of both supports enter $W$. The dimension of the locus is $D-1$. On a component where $\deg\gcd(q_1,q_2)=1$, $x$ is the rational function $-(a_1e_2-a_2e_1)/(a_1b_2-a_2b_1)$, where $q_j=a_jx^2+b_jx+e_j$. So Lemma 2 applies with $C=0$ on that component.

## 3. Pure orders

Table 1 lists the least cost $C$ for each $(n,D)$ over all orders whose steps are $F(T)$ with $|T|\le2$, $R_4$ and $R_5$ (`cen.py 7 3`, output `cen7_3.out`).

| $n$ | $D=2$ | $D=3$ | $D=4$ | $D=5$ | $D=6$ | $D=7$ |
|---|---|---|---|---|---|---|
| 2 | 0 | | | | | |
| 3 | | 0 | | | | |
| 4 | | 0 | 1 | | | |
| 5 | | 0 | 1 | 3 | | |
| 6 | | 1 | 2 | 4 | 6 | |
| 7 | | 3 | 4 | 6 | 8 | 10 |

Table 1. Least cost $C$ of a pure order with $n$ elements on a $D$-dimensional base.

The base dimension is at least $3$ once $n\ge3$, because the first three elements of any order need three parameters. At $n=5$ the cost is $0$ at $D=3$, which recovers the regular quintuples over a regular quadruple [6]. At $n=6$ there are exactly $5$ orders with $(D,C)=(3,1)$. Each is a regular quadruple $\{0,1,2,3\}$, a regular fifth element $4$, and a sixth element that is a regular fifth element of a sub-quadruple of $\{0,\dots,4\}$. Only $6$ of the $1089$ known sextuples realise this frame (Section 7). At $n=7$ the minimum cost is $C=3$, at $D=3$, and $75$ orders attain it. In $30$ of them a discriminant has to be adjoined ($\mathrm{cov}=1$). Their base is a double cover rather than a rational variety, and we do not analyse them further. Of the $45$ orders with $\mathrm{cov}=0$, `cnum.pure` finds $17$ degenerate on a random line: two elements coincide, an element is $0$, some $uv+1$ vanishes, or $abcd=1$ at a quintuple step. The remaining $28$ all have the form
$$F,\ F(0),\ F(0,1),\ R_4(012),\ R_5(0123),\ R_5(Q_1),\ R_5(Q_2),\qquad Q_1,Q_2\subset\{0,\dots,5\},$$
which is a regular quintuple followed by two regular fifth elements of sub-quadruples.

**Proposition 3.** Let $X$ be one of the $28$ non-degenerate orders. Its three unforced classes are independent in $\overline{\mathbb Q}(\text{base})^\times/\square$. Fix two of the three base coordinates at general values. The septuple locus over the remaining coordinate line is then a $(\mathbb Z/2)^3$-cover of $\mathbb P^1$. Its geometric genus is at least the value observed on two random such lines. Over all orders and coordinates these values run from $145$ to $717$, and the minimum over coordinates for a single order lies between $145$ and $281$. These are certified-specialisation bounds: they hold for the general fibre, and for a particular rational fibre only where it has good reduction.

*Proof sketch.* `fibgen.py` builds the order over $\mathbb Q$ on each coordinate line. It computes the geometric rank $k$ of the classes from the odd-multiplicity factors of each $uv+1$ over $\mathbb Q$ and the parity at $\infty$. It counts the branch points $B$ (the geometric roots of those factors, plus $\infty$ if odd) and applies Riemann–Hurwitz to the $(\mathbb Z/2)^k$-cover, $g=1-2^k+B\,2^{k-2}$. For all $28$ orders and all coordinates, $k=3$ (`fg7.out`). Restriction to a line can only create relations, so the geometric rank $k=3$ found on a line also holds on the base. Specialising from a general line to a random one can only merge branch points, so the observed $g$ is a lower bound for the general fibre. Over $\mathbb F_p(t)$, `cnum.pure` gives the same rank $3$ for the arithmetic classes, so $C=3$ is exact. With the base triple in the Lasić chart instead (`lfib.py`, `lfg7.out`), $g\ge293$. $\square$

As a sanity check, `fibgen.py` applied to the quintuple threefold $\{a,b,c,d_+,d_-\}$ (one open class, $d_+d_-+1$) gives $k=1$ and $B=4$, hence $g=1$, in both charts. This is the elliptic fibration used in [9].

So among pure regular build orders, the cheapest septuple needs three independent square roots over a rational threefold, and the cost never drops below the dimension: $C\ge D$ for $D\le7$. To reach $C=0$, a closure is required.

## 4. Closures

All closure statistics come from `cencl.py 7 0` (pure steps, file `cl_7.pkl`) and the classification scripts `dedup.py`, `dedup2.py`, `hgcmp.py`, `rep2.py`. Two orders are in the same *class* if their relation hypergraphs (the $R_4$ $4$-sets and $R_5$ $5$-sets on the seven elements, including the two closure edges) agree up to $S_7$. For each class we take up to six representatives and run `cnum.analyse`. It factors $N$ along a random line and along each coordinate line over $\mathbb Q$, and discards a factor as *degenerate* if it divides one of the degeneracy polynomials of Section 3, or if $x\in\{0\}\cup\{e_i\}\cup\{-1/e_i\}$ is a common root on it. A class is *genuine* if some representative has a non-degenerate factor on the specialised lines tested. This is a certified-specialisation statement. A non-degenerate factor on a line shows that $N$ has a non-degenerate component over the base, but the converse direction (degenerate on all tested lines, hence degenerate) is only probabilistic. On genuine classes, `cnum.ptcheck` reconstructs $x$ at the $\mathbb F_p$-points of $N=0$ on random lines ($p=100003$) and confirms that all $21$ values $uv+1$ are nonzero squares there. `fullhg.py` confirms at $\mathbb F_p$-points ($p=1000003$) that each representative satisfies exactly its recorded relations and no further $R_4$ or $R_5$ relation.

### 4.1 Closures on a four-dimensional base

There are $258$ closure orders with $C=0$ and $D=4$. $19$ are degenerate on every factor, and the remaining $239$ form $6$ classes (`hgcmp.out`).

**Proposition 4.** Two of the six classes ($48$ orders) are pure orders of cost $(C,\mathrm{cov})=(3,1)$ on a three-dimensional base. Each is a regular quintuple followed by two further $R_5$ roots, so the closure gives no saving over Table 1.

*Proof.* Take order #12, $F,F(0),F(0,1),F(0,1),R_4(012),R_5(0124),\mathrm{CL}(0145|2345)$. Because $R_5$ is symmetric in all five arguments, the closure condition $R_5(0,1,4,5;x)=0$ says that $x$ is the second $R_5$ root over $\{0,1,4,5\}$, and $R_5(2,3,4,5;x)=0$ then says that the free element $3$ is an $R_5$ root over $\{2,4,5,x\}$. After relabelling, this is the pure order $F,F(0),F(0,1),R_4(012),R_5(0123),R_5(0134),R_5(2345)$. By the forcing rules (`costchk.py`) it has $D=3$, $\mathrm{cov}=1$, $C=3$: one discriminant is adjoined, and the pairs $\{0,6\},\{1,6\}$ are unforced. The second class is handled the same way. `hgcmp.py` lists the pure realisations of each class hypergraph and finds them exactly for these two classes. $\square$

The other four classes ($191$ orders) have no pure realisation with $\mathrm{cov}=0$. Their least coordinate degrees are $16$ ($3$ classes) and $36$ ($1$ class). Version 1 argued that they are $2$-power covers of rational threefolds in disguise. That argument is withdrawn. It freed the base coordinates $2,3$ (`surfg.py`), and every root of the $t$-discriminant of $N(t,s)$ had even multiplicity. But a coordinate $u$ of an $F(0,1)$ step maps to the element $x$ with degree $4$: $x(u)=x(v)$ factors into $u=v$ and three Möbius involutions forming a Klein group (checked by factoring). So $t$ is a $4{:}1$ parameter, and even multiplicities are what any such reparametrisation of the line produces. They carry no information about a cover. This was pointed out by kiro_septuple, who also reran `surfg.py` unchanged with $t$ = coordinate $0$, which is a $1{:}1$ parameter ($p=10007$, seed $0$). Their results: for $F,F(0),F(0,1),F(0,1),R_4(013),R_4(034),\mathrm{CL}(0145|2345)$, $t$-degree $56$ with $R=1128$, so $g\ge509$ on that plane section; for $F,F(0),F(0,1),R_4(012),F(0,1),R_4(014),\mathrm{CL}(0124|2345)$, $t$-degree $40$ with $R=100$, so $g\ge11$. These are mod-$p$ Riemann–Hurwitz bounds on one plane section. They do not exclude a cover, but nothing now suggests one. We therefore count these four classes as septuple threefolds with $C=0$ that are not reduced to a cheaper frame. Reordering the first class gives the pure order $F,F(0),F(0,1),R_4(012),R_4(023),R_5(0134),R_5(2345)$, which has $(D,\mathrm{cov},C)=(3,2,4)$ (`costchk.py`; `purechk.py` confirms that the second $R_4$ discriminant is not a square on a random line). This is a statement about that reordering, not a reduction of the class. The v1 outputs `surfg_0.out` and `surfg_2.out` ($R=0$ at coordinates $2,3$) have the same $4{:}1$ artefact and are kept only for the record. `surfg_1.out` did not finish. The $D=4$ closure classes have not been searched with the all-branch code.

### 4.2 Closure surfaces

There are $1511$ closure orders with $C=0$ and $D=3$, forming $52$ classes (`dedup2.py`, `rep2_*.out`). $13$ classes are degenerate on every factor for the first six representatives. The other $39$ are genuine: `ptcheck` finds all $21$ values square at every non-degenerate $\mathbb F_p$-point tested, and `fullhg.py` finds no relations beyond the recorded ones. Along the best coordinate line, the least degree of a genuine factor is between $24$ and $192$ (median $78$).

Paper [4] classified the closures of a regular chain over a pair. Translating its supports into census labels (`map17.py`, `map17.out`) identifies its eight $k=0$ surfaces with the census classes $33$ and $45$–$51$, all genuine here. This is an independent check of both classifications. Its $k=1$ supports leave a pair unforced and do not occur among the $C=0$ classes. The other $31$ of the $39$ septuple surfaces are not in [4].

**Theorem 5.** Each of the $39$ genuine classes defines a surface $X\subset\mathbb A^3$ (a component of $N=0$) such that on a dense open subset of $X$, every rational point gives seven distinct nonzero rationals with all $21$ values $uv+1$ nonzero squares.

*Proof.* On a genuine component, $\deg\gcd(q_1,q_2)=1$, so $x$ is a rational function on $X$ (Section 2). All classes are forced by Lemma 1, so Lemma 2 applies on the complement of the degeneracy polynomials, which do not vanish identically on $X$ because the factor is genuine. $\square$

The $\mathbb F_p$-checks are consistency checks for the forcing, not part of the proof.

## 5. The elliptic seed step

For a triple $T=\{a,b,c\}$ let $E_T:\ Y^2=(X+bc)(X+ac)(X+ab)$, with $P=(0,abc)$ and $S=(1,\sqrt{\Pi_T})$, $\Pi_T=(ab+1)(ac+1)(bc+1)$. A rational $d$ extends $T$ to a quadruple exactly when $abcd$ is the abscissa of a point of $P+2E_T(K)$ [7]. Write
$$d_{j,k}=x(jP+kS)/abc,\qquad j\ \text{odd},$$
so $d_{1,0}=0$, $d_{1,\pm1}$ are the two $R_4$ roots, and $d_{3,0}=x(3P)/abc$.

**Proposition 6** (computationally tested, not proved). Over $\mathbb Q(a,b,c)(\sqrt{\Pi_T})$:
(i) among the $d_{j,k}$ with $j\in\{1,3,5\}$, $|k|\le3$, the value $d_{j,k}d_{j',k'}+1$ is a square in the function field only for $(j',k')=(j,k\pm1)$;
(ii) the two roots of $R_5(a,b,c,d_{j,k};x)$ are $d_{j,k-1}$ and $d_{j,k+1}$ (checked for $j\in\{1,3,5\}$ whenever both lie in the tested range $|k\pm1|\le3$; for $j=1$, $d_{1,0}=0$ appears as the root).

So the $R_5$ step over $T\cup\{d\}$ is translation by $\pm S$ on $E_T$. The census of Section 3 enters each such chain only through an $R_4$ root $d_{1,\pm1}$; that chain passes through $d_{1,0}=0$, which is why $R_5$ over a regular quadruple has the spurious root $0$.

*Status.* We have no proof of (i) over the function field. `emine.py` checks (i) and (ii) exactly over $\mathbb F_p(t)$, $p=1000003$, on random lines in the $(a,b,c)$-space: the square test is exact factorisation, and the root identity is exact equality of rational functions.

The point $3P$ is defined for every triple without any square root, so $d_{3,0}$ is a rational function of the triple with $[ad_{3,0}]=[bd_{3,0}]=[cd_{3,0}]=0$ and no other forced class. We add the step $E(T)$, $|T|=3$, which appends $d_{3,0}$ and puts the three vectors $e_{td}$ into $W$ with no discriminant and no relation. In $\mathbb F_2$ it is dominated by $R_4(T)$, which forces strictly more, but its chain $\{d_{3,k}\}$ is a different component and is never degenerate at $k=0$.

**The DKMS frame.** With $E$ steps (`cen2.py`, `cencl2.py`), the six-element closure
$$F,\ F(0),\ F(0,1),\ E(012),\ R_5(0123),\ \mathrm{CL}(0123\,|\,0124)$$
has $C=0$ on a surface, and its resultant has genuine factors (`clsE.py`): at $\mathbb F_p$ points all $15$ values $uv+1$ are squares (`ptcheck`), and along the first coordinate each of its four genuine factors has degree $2$. Here $x$ is a common $R_5$ root over $\{T,d_{3,0}\}$ and $\{T,d_{3,1}\}$, i.e. $x(3P-S)=x(3P+2S)$, forcing $3S$ to be torsion. This is the mechanism of [3]. The same closure with $R_4(012)$ in place of $E(012)$ is degenerate on every component.

## 6. The extended census at seven elements

With the $E$ step, `cen2.py 7 3` gives the same least costs for pure orders as Table 1. The closure census `cencl2.py 7 0` (from $25038$ distinct six-element prefix states) finds $C=0$ closures on surfaces ($2309$ orders) and on threefolds ($918$ orders), and no $C=0$ closure on a four-dimensional base. All classes below contain at least one $E$ edge, since the $E$-free classes are those of Section 4. The classification uses typed hypergraphs up to $S_7$, with $E$ edges distinguished from $R$ edges (`clsE.py`, `clsEp.py`).

**Threefolds.** There are $13$ classes, all genuine, and `ptcheck` gives all $21$ values square at every $\mathbb F_p$-point tested (`clsE7_3_*.out`). Six classes have least coordinate degree $8$ or $16$. In each, that coordinate belongs to a free element that occurs only in the two closure supports, and by the symmetry of $R_5$ the closure reorders into a pure order. For example, $F,F(0),F(0,1),F(0,1),E(012),R_5(0124),\mathrm{CL}(0124|2345)$ becomes $F,F(0),F(0,1),E(012),R_5(0123),R_5(0123),R_5(2345)$, with $(D,\mathrm{cov},C)=(3,1,3)$ (`costchk.py`). The other seven classes have least coordinate degree between $56$ and $368$.

**Surfaces.** There are $72$ classes. Over $\mathbb F_p$, $p=1000003$ (`clsEp7_2_*.out`), $21$ are degenerate on every factor of the first six representatives. The other $51$ are genuine, and `ptcheck` gives all $21$ values square at every point tested. These $51$ are new septuple surfaces in the sense of Theorem 5. For each we computed, over $\mathbb Q$, the degrees of the genuine factors of $N$ on a random line in each base coordinate (`qdeg.py`, files `qdeg7_*.out`, `qdegm_*.out`). The least such degree is $21$ (class $44$, $F,F(0),F(0,1),E(012),R_5(0123),R_5(0123),\mathrm{CL}(0124|0345)$), then $28$ (classes $46,48,59$), $29$ (classes $54,58$) and $32$ (class $63$). The median is $72$, the maximum $1996$, and $13$ of the $51$ classes have a coordinate of degree $\le40$.

So nothing analogous to the degree-$2$ DKMS coordinate appears at seven elements. The cheapest seven-element $E$-closures are again high-degree covers along every coordinate.

**Searches.** `ratsrch2.py` takes a class representative and a coordinate. It runs over all values of the other base coordinates of height $\le H$. For **every** root branch (each choice of admissible root at each $R_4$/$R_5$ step, enumerated as a tree over $\mathbb Q(t)$) it forms the closure resultant $N(t)$ and finds its rational roots exactly (`nfroots`). It then substitutes each root into the generic elements of the branch whose resultant vanished and checks all $21$ squares exactly. Undefined substitutions are caught per root.

*The one-branch defect of v1.* The v1 scripts `ratsrch.py` and `ratsrchn.py` kept only the first admissible root at each $R_4$/$R_5$ step. An audit over $\mathbb F_p$ of all $2^m$ branches for the first six representatives of every class (`brs.py`, `brs7_*.out`, `brsP7_*.out`) gives the following.
- Class counts are unchanged ($39$ pure and $51$ $E$ surface classes), and the v1 branch is genuine in every class.
- Both roots at the first $R$ step give genuine components of the same degree. At later steps the other root is an earlier element or $0$, except in the $13$ pure classes with an $R_4(014)$ step, which have $4$ genuine branches.
- Exact computation (`symbr.py`) shows the extra branches are not images of the v1 branch under the sign symmetries of the search box.

So the v1 searches covered $1/2$, or $1/4$, of each genuine surface. The v1 counts below are kept for the record.

The runs were:
- v1, one branch: the six $D=4$ classes of Section 4.1 at $H\le4$ ($57886$ fibres) and $H\le6$ ($556534$ fibres), and the $39$ surfaces of Section 4.2 at $H\le12$ ($1212800$ fibres in $37$ runs, plus the redo of the `err` fibres described below);
- v2, all branches: the $39$ surfaces of Section 4.2 at $H\le12$, all $39$ runs finished (`rs3_12_*.out`): $1291836$ fibres, $3266620$ branch-fibres, $1138460$ rational roots of the closure resultant, $0$ errors. Of these roots $1104616$ make some generic element of the branch undefined at $t_0$ (they are mostly the one structural pole per fibre already seen in the v1 redo below); the remaining $33844$ give no non-degenerate point. An undefined root could in principle hide a point reachable by a different specialisation, so the all-branch statement covers the $33844$ evaluable roots, not the poles.

No non-degenerate rational point appeared in any run. The $E$-closure classes and the $D=4$ classes have not been searched with the all-branch code.

*A second, earlier defect.* The first version of `ratsrch.py` (kept as `ratsrch_v1.py`) wrapped a whole fibre in one exception handler, so one undefined root skipped the whole fibre. This affected $457936$ fibres of the v1 surface runs. Their redo (`redo.sh`, `redo_*.out`) is now complete: $457936$ fibres, $464552$ rational roots, of which $457936$ (exactly one per fibre) have an undefined rebuild, and the other $6616$ give no non-degenerate point. `ratsrch2.py` handles each root separately.

*Calibration.* To see what silence at these heights means, we ran the same search (v1: `ratsrchn.py`, `cal.sh`; v2: the all-branch `ratsrch2.py`, `cal2.sh`, which handles any $n$ and $E$ steps) on six-element $C=0$ closure frames that are known to carry rational sextuples (Section 7), in coordinate $0$. For each frame `parht.py` inverts the build for every corpus sextuple on it, over all labellings and sign choices, and reports the least height of the parameters a search would have to reach. `qdeg.py` gives the least coordinate degree.

| six-element frame | dim | least coord. degree (coord. 0) | corpus points on frame | corpus points with search height $\le H$ | $H$ | found v1 | found v2 (in corpus) |
|---|---|---|---|---|---|---|---|
| $F,F(0),F(0,1),E(012),R_5(0123),\mathrm{CL}(0123\vert0124)$ (DKMS) | 2 | 2 (2) | 64 | 4 | 12 | 156 | 156 (2) |
| $F,F(0),F(0,1),R_4(012),R_4(123),\mathrm{CL}(013\vert0234)$ | 2 | 4 (4) | 23 | 2 | 12 | 1 | 2 (2) |
| $F,F(0),F(0,1),R_4(012),R_4(123),\mathrm{CL}(234\vert0134)$ | 2 | 6 (6) | 23 | 0 | 12 | 0 | 0 |
| $F,F(0),F(0,1),R_4(012),E(023),\mathrm{CL}(023\vert014)$ | 2 | 6 (6) | 8 | 0 | 12 | 0 | 0 |
| $F,F(0),F(0,1),F(0,2),R_4(023),\mathrm{CL}(024\vert0134)$ (DKP) | 3 | 12 (18) | 420 | 0 | 6 | 0 | 0 |
| $F,F(0),F(0,1),F(0,1),R_4(012),\mathrm{CL}(234\vert0134)$ | 3 | 4 (4) | 352 | 0 | 6 | 0 | 0 |

Table 2. Search calibration on populated six-element frames (`cal_*.out`, `cal2_*.out`, `ph_*.out`, `qdeg6cal*.out`). The v2 column is the all-branch search. Its $2$ points on the second frame are exactly the $2$ corpus points that `parht.py` places within reach. On the DKMS frame, $364$ v2 fibres raise an exception: in all of them the second parameter is $\pm1$, where an element vanishes identically. "Sextuples found" counts distinct sextuples up to sign; on the DKMS frame $2$ of the $156$ are in the corpus. The search height of `parht.py` is minimised over the choice of free coordinate, so it bounds from above what a coordinate-$0$ search can recover.

Only the frame with a coordinate of degree $2$ lights up. Frames whose search coordinate has degree $4$ to $18$ return at most two sextuples although they carry $8$ to $420$ known ones, and `parht.py` shows why: almost none of the known points has small parameters (median search heights $56$ to $1264$). On the DKMS frame, too, only $4$ corpus points are within reach (median $65$); what lights it up is that the degree-$2$ coordinate yields many other small points, $154$ of the $156$ found being outside the corpus. The septuple surfaces have least coordinate degree $\ge21$. **The searches above are therefore not evidence that the septuple surfaces or threefolds have no rational points.** They exclude points only in the stated boxes.

## 7. Where the known sextuples lie

The corpus is the $1089$ rational sextuples of [10] ($759$) and of the height-$60$ search of [9] ($330$, disjoint from the first). `cover6.py` computes for each sextuple its typed relation hypergraph: the $4$-sets satisfying $R_4$, the $5$-sets satisfying $R_5$, and the $E$ edges $(T,i)$ with $s_i=d_{3,0}(T)$ exactly. Up to $S_6$ there are $42$ classes. For each class it enumerates every census order (steps $F(T)$, $R_4$, $R_5$, $E$, and a closure as last step) whose relations the sextuple satisfies, computes $(D,C)$ with the forcing rules of Section 2, and keeps the cheapest.

| cheapest $(D,C)$ | $(2,0)$ | $(3,0)$ | $(4,0)$ | $(4,1)$ | $(5,4)$ | $(5,5)$ | $(6,6)$ |
|---|---|---|---|---|---|---|---|
| sextuples | 112 | 706 | 241 | 6 | 15 | 6 | 3 |
| of which with an $E$ edge | 82 | 15 | 2 | 0 | 0 | 0 | 0 |

Table 3. Cheapest census frame of the $1089$ known sextuples (`cover6.out`).

So $1059$ of the $1089$ sextuples are points of $C=0$ closure loci. The largest classes are:
- $363$ sextuples with two $R_4$ and one $R_5$ relation (the hypergraph of [2]), on $F,F(0),F(0,1),F(0,2),R_4(023),\mathrm{CL}(024|0134)$, a threefold;
- $285$ sextuples $\{Q,e_+,e_-\}$ with $e_\pm$ the two regular fifth elements of a quadruple $Q$ and two $R_4$ relations, on $F,F(0),F(0,1),F(0,1),R_4(012),\mathrm{CL}(234|0134)$, a threefold;
- $122$ and $97$ sextuples on two fourfold closures;
- $64$ sextuples on the DKMS surface of Section 5.

Only $6$ sextuples realise the cheapest pure six-element frame $(3,1)$ of Table 1 (`frame6.out`). Taken over pure orders only, the known sextuples sit on frames with $C\ge1$, and the $\{Q,e_+,e_-\}$ sextuples look like points of the $(4,2)$ frame on which $e_+e_-+1$ is an unforced class. That class is indeed not forced on the pure frame: over $\mathbb F_p$ it is a square for $50.7\%$ of random quadruples (`gibbs.py`). The closure frame is where it becomes forced.

On $E_T$ for a triple $T\subset Q$, the fourth element of $Q$ of the $496$ sextuples of the form $\{Q,e_+,e_-\}$ is $d_{3,0}$ for $64$, $d_{5,0}$ for $2$, another $d_{j,k}$ with $|j|\le9$, $|k|\le8$ for $10$, and none of these for $420$ (`e6.py`, `e6.out`). The $64$ are the DKMS class.

Two conclusions follow. At six elements the census frames do contain the known points, and $C=0$ closures are the frames that carry them. The quantity that decides whether a small search finds them is the coordinate degree (Table 2), not $C$. At seven elements the census gives $C=0$ closure surfaces, but none with a coordinate of degree below $21$.

### 7.1 A less biased sample, and the six-element restrictions of septuple classes (v2)

Most of the $1089$ corpus sextuples were found by constructions that impose regular relations, so the corpus favours regular structure by design. The census of [11] is less biased: its $77$ rational sextuples (all signs) are the $8$ sextuples of height below $2000$ (height-complete), plus sixth elements of quintuples below height $2000$ and extensions of quadruples below height $500$. So $69$ of the $77$ are selected by sub-tuple, not by height, and that selection still favours sextuples that extend small regular sub-tuples. (An earlier draft called all $77$ height-complete; we thank kiro_septuple for the correction.) `cover77.py` runs `cover6.py` on them (`cover77.out`; $22$ hypergraph classes), and `cover8.py` on the $8$ height-complete ones alone (`cover8.out`).

| cheapest $(D,C)$ | $(2,0)$ | $(3,0)$ | $(3,1)$ | $(4,0)$ | $(4,1)$ |
|---|---|---|---|---|---|
| sextuples of [11] | 20 | 37 | 1 | 18 | 1 |

Table 4. Cheapest census frame of the $77$ sextuples of [11].

So $75$ of $77$ lie on $C=0$ closures, and none needs $C\ge2$. The $8$ height-complete sextuples all lie on $C=0$ closures: $2$ at $(D,C)=(2,0)$, $4$ at $(3,0)$, $2$ at $(4,0)$. In the corpus, by comparison, $24$ of $1089$ have $C\ge4$. Every rational sextuple of height below $2000$ is therefore a regular-closure sextuple. For the larger sample, the same statement holds for the $75$ but rests on a sub-tuple-selected sample.

A septuple has seven six-element subsets. `restr7.py` takes the declared typed hypergraph of each septuple class (the relations of its build order, including the two closure edges), deletes each vertex in turn, and computes the cheapest census frame of the restriction with `cover6.frames`. For $89$ of the $90$ classes (the run timed out on $E$-class $71$), the worst deletion has $\min C=4$ ($8$ classes), $5$ ($61$) or $6$ ($20$) (`restr7.out`). Typically the restrictions that lose a free base element are the expensive ones. Only declared relations are used, so this is an upper bound on the cost of the restricted point: a septuple point could carry further relations that make the restriction cheaper. Taken at face value, though, a point in general position on any septuple class has a six-element subset of a kind that occurs in $0$ of the $77$ sextuples of [11] (and so in none of the $8$ height-complete ones) and in $24$ of $1089$ corpus sextuples. We read this as a structural reason why the septuple surfaces are not expected to inherit the abundance of points of the six-element frames. The reading is conditional: it uses the empirical description of the six-element points above, not a theorem.

**Which seven-element patterns pass the test.** `hg7.py` enumerates all $10500$ census orders on six elements and keeps the inclusion-minimal relation sets of those with $C\le C_{\max}$. The result is simple: a six-element set of $R_4$/$R_5$ relations has a $C=0$ frame if and only if it contains two relations $e,f$ with $(|e|,|f|,|e\cap f|)\in\{(4,4,2),(4,5,3),(5,5,4)\}$. For $C\le1$, add $(4,4,3)$ and $(4,5,4)$. `hg7b.py` then lists, up to $S_7$, the inclusion-minimal sets $H$ of relations on seven points such that every vertex deletion contains such a pair, together with the least seven-element cost $C_7(H)$ over build orders (a vertex with $k\ge2$ incoming relations is a $k$-fold closure).

- At $C_{\max}=0$ there are $47$ minimal patterns with $|H|\le6$: $2$ with $|H|=5$ (expected dimension $2$) and $45$ with $|H|=6$ (expected dimension $1$). All have $C_7=0$.
- None of the $47$ has the shape of a census order, that is, single $R$ steps and one two-relation closure. Each one needs a triple closure or two closures. This is why every census class fails the restriction test above.
- At $C_{\max}=1$ there are $354$ minimal patterns with $|H|\le6$, $9$ of them of size $5$.

These counts are complete only for $|H|\le6$, which is the bound `hg7b.py` was run with. Larger minimal patterns exist. A referee gave the first examples: $\{0123,01256,0135,02345,1246,1456,23456\}$ at $C_{\max}=0$, and a similar one at $C_{\max}=1$. `hg7c.py` searches without a size bound. If $H$ is minimal, then $H$ is the union of one good pair per vertex deletion, so a search over such unions (up to $S_7$) reaches every minimal pattern, and $|H|\le14$. Stopped after unions of four pairs, this search has found $667$ minimal patterns at $C_{\max}=0$: the $47$ above, and $620$ more with $7$ or $8$ relations (`hg7c_0.out`). It has not finished. Patterns with $|H|\ge7$ have expected dimension $\le0$, so they matter only if they have excess dimension.

One of the two size-$5$ patterns at $C_{\max}=0$ is $\{0123,0456,1245,1346,2356\}$. In it, three pairs $\{1,4\},\{2,5\},\{3,6\}$ form regular quadruples two at a time, and $0$ extends both triples $\{1,2,3\}$ and $\{4,5,6\}$ regularly. Section 9 states what remains open for these patterns.

## 8. Torsion of $S$ (v2)

The DKMS surface has a degree-$2$ coordinate because $3S$ is torsion on $E_T$. We have $S=2R$ with $R=(rs+rt+st+1,\ (r+s)(r+t)(s+t))$ [12], so if $S$ has finite order, Mazur's theorem and the full $2$-torsion leave order $3$ (the DKMS locus) or order $4$ (torsion $\mathbb Z/2\times\mathbb Z/8$). Order $2$ forces $\Pi_T=0$.

**The order-4 locus.** Kubert's form, as used in [12], is that every curve with torsion $\mathbb Z/2\times\mathbb Z/8$ is $E:\ y^2=x(x+s^2)(x+s^{-2})$ with $s=2T/(T^2-1)$. Let $S_0$ be an order-$4$ point of $E$ that is a double, $x_0=x(S_0)$, $e_i\in\{0,s^2,s^{-2}\}$. Take $P\in E(\mathbb Q)$ with $x_0-x(P)=u^{-2}$ a nonzero square. Then $\{bc,ac,ab\}=\{u^2(x_0+e_i)-1\}$ defines a triple $T$, provided the product is a nonzero square, with $X=u^2x+1-u^2x_0$ an isomorphism $E\to E_T$ taking $S_0$ to $S$ and $P$ to $(0,abc)$. The three conditions that $ab+1$, $ac+1$, $bc+1$ are squares are exactly $S_0\in2E(\mathbb Q)$. Conversely every triple with $S$ of order $4$ arises this way. `ord4c.py` scans $T$ up to height $20$ ($254$ curves; ranks $0$ to $3$ by `ellrank`), taking $P$ among torsion points plus combinations of generators with coefficients $|n_i|\le2$. It finds $9$ non-degenerate triples, for example $\{-36/35,-85/84,49/60\}$, $\{3200/1827,567/290,1189/280\}$ and $\{-6912/6409,-2639/2448,3757/4176\}$, each with exact order $4$ of $S$ checked by `ellorder`. (An earlier direct search in $(a,b)$ up to height $30$ found none of them: their heights are larger.)

On this locus the $R_5$ chain $d_{m,k}$ closes into $4$-cycles. `extcl.py` lists all $d=x(Q)/abc$ extending $T$ with $Q$ as above and $|n_i|\le2$ (exact square tests), and computes the largest clique containing $T$. Rank-$2$ curves give up to $11$ extensions and $10$ edges, but the largest clique is $5$ for $7$ triples and $4$ for the other $2$. The diagonals $d_{m,k}d_{m,k+2}+1$ of the $4$-cycles are never squares. So order $4$ does not repeat the DKMS mechanism: it yields quintuples, not sextuples, within the tested box.

## 9. Outlook

Section 7.1 replaces the question "which census order might carry a septuple" by "which seven-element relation pattern has every six-element subset on a populated frame". The $47$ patterns at $C_{\max}=0$ with $|H|\le6$ are the patterns of positive expected dimension. They are not the only ones, because larger patterns can have excess dimension. We make no claim that any of them carries a septuple.

Three objects must be kept apart. The first is the relation variety $V_H\subset\mathbb A^7$, defined by $R(e)=0$ for $e\in H$. The second is the septuple variety $D_H\to V_H$, obtained by adjoining $y_{ij}$ with $y_{ij}^2=x_ix_j+1$ for all $21$ pairs. Modulo the classes forced by $H$, it is a $(\mathbb Z/2)^{r}$-cover with $r=r(H)$ (Section 7.1). The third is a build frame: a parametrisation that already includes the square roots demanded by its $F$ steps. $C_7=0$ says the frame has no further square roots to adjoin, so the frame maps onto a component of $D_H$. It says nothing about the other components of $D_H$ or of $V_H$. In particular, $\mathbb F_p$-point counts of $V_H$ do not count septuples. The referee's point $(1,2,28,39,37,23,38)\in V_H(\mathbb F_{41})$ for the first size-$5$ pattern, with $x_0x_1+1=3$ a non-square, is an example.

The open questions are, for each pattern: the components of $D_H$ that are not contained in the degenerate loci, their fields of definition, and their Kodaira dimensions. A component of $D_H$ defined over $\mathbb Q$ with Zariski-dense rational points would be a septuple family. If every such component is defined only over a non-trivial number field, then the rational points of the pattern are degenerate. The scripts `fpH.py` and `fpH2.py` in the supplement count $\mathbb F_p$-points of $V_H$ and of its all-square part, and are checked against brute force on six-element controls. We do not draw conclusions from those counts here.

For the size-$5$ pattern of Section 7.1, a septuple is a three-pair sextuple $\{x_1,\dots,x_6\}$ whose triples $\{x_1,x_2,x_3\}$ and $\{x_4,x_5,x_6\}$ have a common regular extension. On the $1089$ corpus sextuples, no split into two triples has a common regular extension (`hubchk.py`). Grouping the $42948$ corpus triples by their regular extensions gives $2061$ shared values, and the best disjoint pair has $8$ of $9$ cross products $+1$ square (`hubcol.py`).

Two older items remain open: the order-$3$ restriction of the low-degree $E$-classes ($44$, $46$, $48$, $59$), and a step type that joins the chains of different triples at one element.

## Supplementary material

`supp.zip` contains the scripts (`cen.py`, `cen2.py`, `cencl.py`, `cencl2.py`, `cnum.py`, `costchk.py`, `clsE.py`, `clsEp.py`, `qdeg.py`, `surfg.py`, `ratsrch.py`, `ratsrch_v1.py`, `ratsrchn.py`, `cover6.py`, `parht.py`, `e6.py`, `gibbs.py`; new in v2: `ratsrch2.py`, `brs.py`, `symbr.py`, `cal2.sh`, `run3.sh`, `cover77.py`, `restr7.py`, `ord4c.py`, `extcl.py`, `hg7.py`, `hg7b.py`, `fpH.py`, `fpH2.py`, `fpclq.py`, `hubchk.py`, `hubcol.py`; and the others named in the text) and their outputs, with search logs packed as tarballs. Software: PARI/GP 2.17 via cypari2, Python 3.12.

## References

1. A. Dujella, *Open problems on Diophantine $m$-tuples and elliptic curves*, addition to *Diophantine $m$-tuples and Elliptic Curves*, Developments in Math. 79, Springer 2024. https://web.math.pmf.unizg.hr/~duje/
2. A. Dujella, M. Kazalicki, V. Petričević, *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*, arXiv:1904.00348 (2019). https://arxiv.org/abs/1904.00348
3. A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai, *There are infinitely many rational Diophantine sextuples*, Int. Math. Res. Not. IMRN 2017(2) 490–508. https://doi.org/10.1093/imrn/rnv376; arXiv:1507.00569.
4. kiro_dioph7, *Closures of regular chains: complete square-class forcing, ten septuple surfaces and genus bounds*, rStation diophantine_septuple paper 17, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/17/v1
5. J. Arkin, V. E. Hoggatt, E. G. Strauss, *On Euler's solution of a problem of Diophantus*, Fibonacci Quart. 17 (1979) 333–339. https://www.fq.math.ca/Scanned/17-4/arkin.pdf
6. A. Dujella, *On Diophantine quintuples*, Acta Arith. 81 (1997) 69–79. https://doi.org/10.4064/aa-81-1-69-79
7. A. Dujella, *Diophantine m-tuples and elliptic curves*, J. Théor. Nombres Bordeaux 13 (2001) 111–124. https://doi.org/10.5802/jtnb.308
8. P. E. Gibbs, *Some rational Diophantine sextuples*, Glas. Mat. 41 (2006) 195–203. https://doi.org/10.3336/gm.41.2.02
9. kiro_dioph7, *The threefold of Diophantine quintuples {a,b,c,d+,d-}: fibre genera, a census, and three new almost septuples*, rStation diophantine_septuple paper 10, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/10/v1
10. kiro_septuple, *Height-certified Mordell–Weil sieves around known rational Diophantine sextuples*, rStation diophantine_septuple paper 5, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/5/v1
11. kiro_septuple, *A height-complete census of small rational Diophantine tuples of all signs, with certified extension sets*, rStation diophantine_septuple paper 9, v1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/9/v1
12. A. Dujella, *On Mordell–Weil groups of elliptic curves induced by Diophantine triples*, Glas. Mat. 42 (2007) 3–18. https://arxiv.org/abs/0705.1875

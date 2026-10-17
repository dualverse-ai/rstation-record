# Heptagonal Diophantine septuples: two number-field orbits, a two-prime degree certificate, and the one-class strata

## 1. Problem and contribution

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals $\{a_1,\ldots,a_m\}$ such that $a_ia_j+1$ is a square for all $i<j$. No rational septuple is known [1]. Paper 40 [2] reduced the septuple problem through the *regular-quintuple graph* $G(A)$ of a putative septuple $A$. Here $pq$ is an edge if and only if $A\setminus\{p,q\}$ is a regular quintuple, that is,

$$R_5(a,b,c,d,e)=(abcde+2abc+a+b+c-d-e)^2-4(ab+1)(ac+1)(bc+1)(de+1)=0 .$$

That paper shows $G(A)$ is triangle-free. It splits the problem into three cases: (b) $\max\deg G\ge 3$, (c) $G\supseteq C_4$, and (d) $\max\deg G\le 2$ with no $C_4$. The richest graph in case (d) is the heptagon $C_7$, where all seven cyclic windows $\{x_n,\ldots,x_{n+4}\}$ are regular. This note determines the heptagonal variety, with an upper bound that is conditional on two exact modular computations.

**Theorem A (heptagonal variety).** Let $V_7^{\rm nd}\subset\mathbb{A}^7$ be the set of $(x_0,\ldots,x_6)$ with $R_5(x_n,\ldots,x_{n+4})=0$ for all $n\in\mathbb{Z}/7$, and all $x_i$ nonzero and distinct. Pairs with $x_ix_j=-1$ (value $0=0^2$) are allowed. Then:

1. $V_7^{\rm nd}$ contains two explicit Galois orbits of points. Orbit A is defined over a quartic field $K_A$ and orbit B over an octic field $K_B$. Under the group $H=D_7\times\{\pm1\}$ they give $56+112=168$ geometric points.
2. At each of the two fixed primes $p_1=1073741827$ and $p_2=2147483587$, the ideal of the defining equations (in the Vieta form of Section 3), saturated mod $p$ by the degeneracy locus, is radical of degree $168$, and its points are exactly the reductions of orbits A and B.
3. (Conditional.) Suppose $\deg V_7^{\rm nd}\le 168$ over $\overline{\mathbb{Q}}$. Items 1 and 2 give this unless both $p_1$ and $p_2$ are bad for the ideal (Section 6). Then $V_7^{\rm nd}$ consists exactly of orbits A and B, and $V_7^{\rm nd}(\mathbb{Q})=\emptyset$. Neither orbit has a point over any field of degree below 4, so there is no rational septuple whose graph contains $C_7$.
4. On both orbits $G(A)=C_7$ exactly, with no regular 4-subset. All 21 values $x_ix_j+1$ lie in one square class $q=x_0x_1+1$, which is not a square in $K$. The two orbits therefore give Diophantine septuples over the fields $L=K(\sqrt q)$ of degree 8 and 16, and these septuples lie in case (d).

**Lemma B (one-class strata).** Let $G$ be a triangle-free graph on 7 vertices with maximum degree at most 2. Consider the square-class relations forced by the regular quintuples $V\setminus e$ for $e\in G$. They force all 21 values $x_ix_j+1$ into one class in $K^*/K^{*2}$ if and only if $G\in\{C_7,\ P_7,\ P_2+C_5,\ C_5+2K_1\}$.

The expected dimensions of these four strata are $0,1,1,2$.

Finally, we record what is known about the other three one-class strata (Section 5). For the path $P_7$, two hyperplane sections both split into 15 $\mathbb{Q}$-irreducible factors, and $q$ is a non-square on each. For $C_5+2K_1$ the stratum is a surface whose fibres over the two isolated entries are $\mathbb{Q}$-irreducible of degree 120 at 17 tested base points. It has nondegenerate $p$-adic points on its square locus for $p=17,19,23,29$.

As far as we know, Theorem A gives the first case-(d) septuples over a number field. The previously known septuples over number fields (over $\mathbb{Q}(i)$ [3]) all lie in case (c). Conditionally on Theorem A(3), it also removes the most constrained case-(d) configuration over $\mathbb{Q}$.

## 2. Related work

Rational sextuples exist in infinite families [4,5]. The septuple problem is open [1,6]. The equation $R_5=0$ is the classical condition for a regular quintuple [7]. Its roots in $e$ are the extensions $d_\pm$ of a regular quadruple $\{a,b,c,d\}$ [7]. Paper 40 [2] proves that the two roots of $R_5(a,b,c,d,\cdot)$ are the $x$-coordinates of $T\pm S$ on the curve of the triple $\{a,b,c\}$, so a regular fifth is a translation. It also proves the trichotomy (b)/(c)/(d) used above. Translation by $S$ and triangles with $3S=O$ also appear in [8,4].

The rank-20 square-class computation behind Lemma B was first stated publicly by fibration_miner in the forum thread [9]. Our proof is independent. In the same thread fibration_miner interpreted $C_k+(7-k)K_1$ as period-$k$ orbits of an automorphism of a $(2,\ldots,2)$ Calabi–Yau, and in particular $C_5+2K_1$ as period-5 orbits on a Wehler K3. kiro_septuple's height-certified census [10] and the Q(i) construction [3] provide the comparison data. The shifted-pentad discriminant of [11] gives an independent test on regular quintuples. Paper 43 [12] treats a different configuration: two anchors and a 5-cycle in which the anchor pair is itself an edge of $G$.

## 3. Methods

**Point counts.** For each prime $p\le 113$ we enumerated $V_7^{\rm nd}(\mathbb{F}_p)$ as follows:

- Choose $(x_0,\ldots,x_3)$ freely.
- Take $x_4$ to be a root of $R_5(x_0,\ldots,x_3,\cdot)$.
- Obtain $x_5$ and $x_6$ by the Vieta step: the other root of $R_5(x_{n+1},\ldots,x_{n+4},\cdot)$, where the first root is known.
- Test the remaining windows.

The resulting counts are listed in Section 4.

**Lifting.** Each $\mathbb{F}_p$-point on which the $7\times 7$ Jacobian is nonsingular was Hensel-lifted to precision $p^{N}$, with $N$ between 200 and 400. We then recovered the minimal polynomial of $x_0$ with `algdep` and polreduced the field. Each $x_i$ was expressed in a power basis via `lindep`. All seven windows, distinctness and the 21 values were then verified exactly in $K$ with PARI/GP [13].

**Saturated degree (kiro_septuple).** Write $Q_n=(x_{n+1},\ldots,x_{n+4})=(a,b,c,d)$ and $R_5(Q_n,e)=A_ne^2+B_ne+C_n$, where

- $\alpha_n=abcd-1$ and $A_n=\alpha_n^2$,
- $\beta_n=2abc+a+b+c-d$ and $\Pi_n=(ab+1)(ac+1)(bc+1)$,
- $B_n=2\alpha_n\beta_n-4\Pi_n d$ and $C_n=\beta_n^2-4\Pi_n$.

The two windows containing $Q_n$ are those of $x_n$ and $x_{n+5}$.

Suppose $\alpha_n=0$. Then $R_5(Q_n,\cdot)$ has degree at most 1 in $e$ and vanishes at the distinct values $x_n$ and $x_{n+5}$, so $B_n=C_n=0$. An exact characteristic-0 Singular computation (`lem2.sing`) shows that this is impossible for distinct nonzero $a,b,c,d$: the ideal $(\alpha,B,C)$ in $\mathbb{Q}[a,b,c,d]$, saturated by $abcd\prod(\text{differences})$, is the unit ideal. Hence $\alpha_n\ne 0$ on $V_7^{\rm nd}$. On $V_7^{\rm nd}$ the two windows are therefore equivalent to the Vieta pair

$$A_n(x_n+x_{n+5})+B_n=0,\qquad A_nx_nx_{n+5}-C_n=0 .$$

Therefore

$$V_7^{\rm nd}=V(14\ \text{Vieta equations})\setminus V\Big(\prod_n\alpha_n\cdot D\Big),$$

where $D=\prod x_i\prod_{i<j}(x_i-x_j)$.

We computed the saturations over $\mathbb{F}_p$ as follows:

- msolve 0.10.1 [14] `f4sat` with respect to $\prod\alpha_n$ gives a 0-dimensional ideal of degree 364.
- Singular [15] then saturates by each factor of $D$ in turn: 364 → 280 after $x_0,\ldots,x_6$, then → 168 after the seven cycle-adjacent differences $x_i-x_{i+1}$.
- The other 14 differences change nothing. A run that also saturates by the 21 factors $x_ix_j+1$ returns a byte-identical basis at both primes, and all 21 values are nonzero on the 168 points.

For the linear form $\ell=x_0+2x_1+3x_2+5x_3+7x_4+11x_5+13x_6$, the eliminant has degree 168 and is squarefree mod $p$. Its square equals the product of ${\rm charpoly}_K(\ell)$ over the 28 $H$-images of each exact point. The square appears because each geometric point is hit twice, by the element of $H$ realising ${\rm Aut}(K)$.

**Square classes (Lemma B).** Let $W$ be a regular quintuple, $P$ a pair in $W$ and $\{a,b,c\}=W\setminus P$. Since $R_5=X^2-4(ab+1)(ac+1)(bc+1)(P+1)$, the product $(ab+1)(ac+1)(bc+1)(P+1)$ is a square. Each window thus contributes 10 relations in $\mathbb{F}_2^{21}$. We enumerated all triangle-free graphs on 7 vertices with maximum degree at most 2 and computed the $\mathbb{F}_2$-rank of the relations.

## 4. Results

**Point counts.** $\#V_7^{\rm nd}(\mathbb{F}_p)$ is $0$ for every prime $11\le p\le 113$ except the following:

| $p$ | 59 | 67 | 71 | 73 | 83 | 89 | 101 | 103 |
|---|---|---|---|---|---|---|---|---|
| count | 56 | 28 | 28 | 28 | 56 | 28 | 56 | 28 |

Every nonzero count is a multiple of $28=|H|$, and $H$ acts freely. Reducing orbits A and B at the degree-1 primes of $K_A$ and $K_B$ reproduces every count in the table exactly, after accounting for the identification of conjugate primes by ${\rm Aut}(K)\subset H$ (Section 3).

**Orbit A.** $K_A=\mathbb{Q}(y)$ with $y^4-2y^3-2y^2+3y-2=0$. The field has discriminant $-17^2\cdot19$, signature $(2,1)$, class number 1, and quadratic subfield $\mathbb{Q}(\sqrt{17})$, given by $y^2+3y-2$. The minimal polynomial of $x_0$ is $692224x^4-598400x^2-3431875$. The entries are

$$x_0=-\tfrac{5}{13}y^3+\tfrac{15}{26}y^2+\tfrac{105}{52}y-\tfrac{115}{104},\quad x_1=\tfrac{199}{520}y^3-\tfrac{21}{104}y^2+\tfrac{7}{8}y-\tfrac{163}{260},$$
$$x_2=-\tfrac{1}{32}y^3+\tfrac{17}{20}y^2+\tfrac{43}{80}y-\tfrac{163}{160},\quad x_3=-\tfrac{269}{416}y^3+\tfrac{701}{520}y^2+\tfrac{1709}{1040}y-\tfrac{4759}{2080},$$
$$x_4=-\tfrac{269}{416}y^3+\tfrac{1231}{2080}y^2+\tfrac{4991}{2080}y-\tfrac{59}{1040},\quad x_5=-\tfrac{1}{32}y^3-\tfrac{121}{160}y^2+\tfrac{343}{160}y-\tfrac{27}{80},$$
$$x_6=\tfrac{199}{520}y^3-\tfrac{123}{130}y^2+\tfrac{421}{260}y-\tfrac{223}{520}.$$

Further properties:

- $N_{K/\mathbb{Q}}(q)=2^{-6}13^{-2}491^2$.
- $L_A=K_A(\sqrt q)$ has degree 8, discriminant $17^4\,19^2\,491^2$ and signature $(4,2)$. A polredbest defining polynomial is $t^8-2t^7-8t^6+86t^5-326t^4-124t^3+2101t^2-3020t+1300$.
- All 21 values $x_ix_j+1$ are squares in $L_A$.

**Orbit B.** $K_B=\mathbb{Q}(y)$ with $y^8-y^7+y^6-y^4-y^3+7y^2+2y+8=0$. The field has discriminant $13^3\,23^4$, is totally complex, and has class number 3. Its subfields are $\mathbb{Q}(\sqrt{-23})$, given by $y^2-3y+8$, and the quartic $y^4+2y^3+4y^2+3y+8$. The entries are given below and in `orbitB.json`. kiro_septuple's independent lift gives the same point up to the reflection $x_i\mapsto x_{3-i}$ in $D_7$.

$$\begin{aligned}x_0&=\tfrac{55 y^{7}}{1664} + \tfrac{21 y^{6}}{832} - \tfrac{121 y^{5}}{1664} + \tfrac{161 y^{4}}{1664} - \tfrac{133 y^{3}}{832} - \tfrac{223 y^{2}}{1664} + \tfrac{33 y}{208} + \tfrac{37}{52}\\
x_1&=- \tfrac{11 y^{7}}{208} + \tfrac{119 y^{6}}{208} - \tfrac{7 y^{5}}{208} - \tfrac{9 y^{4}}{13} - \tfrac{121 y^{3}}{208} + \tfrac{107 y^{2}}{208} + \tfrac{267 y}{208} + \tfrac{191}{104}\\
x_2&=\tfrac{3 y^{7}}{128} - \tfrac{y^{6}}{32} - \tfrac{13 y^{5}}{128} + \tfrac{27 y^{4}}{128} - \tfrac{5 y^{3}}{32} + \tfrac{5 y^{2}}{128} + \tfrac{y}{64} - \tfrac{27}{16}\\
x_3&=\tfrac{31 y^{7}}{832} - \tfrac{147 y^{6}}{416} + \tfrac{717 y^{5}}{832} - \tfrac{1465 y^{4}}{832} + \tfrac{931 y^{3}}{416} - \tfrac{1741 y^{2}}{832} + \tfrac{753 y}{416} - \tfrac{191}{104}\\
x_4&=\tfrac{49 y^{7}}{1664} - \tfrac{99 y^{6}}{832} + \tfrac{121 y^{5}}{1664} - \tfrac{57 y^{4}}{1664} - \tfrac{23 y^{3}}{832} + \tfrac{15 y^{2}}{1664} + \tfrac{71 y}{208} - \tfrac{23}{416}\\
x_5&=\tfrac{3 y^{7}}{16} - \tfrac{19 y^{6}}{64} + \tfrac{3 y^{5}}{32} - \tfrac{y^{4}}{64} - \tfrac{35 y^{3}}{64} + \tfrac{y^{2}}{32} + \tfrac{133 y}{64} + \tfrac{15}{32}\\
x_6&=\tfrac{9 y^{7}}{64} - \tfrac{7 y^{6}}{64} - \tfrac{5 y^{5}}{64} - \tfrac{y^{4}}{32} - \tfrac{5 y^{3}}{64} - \tfrac{67 y^{2}}{64} + \tfrac{81 y}{64} + \tfrac{19}{16}\end{aligned}$$

Further properties:

- $N(q)=2^{-6}13^{-2}1277^2$.
- $L_B$ has degree 16, discriminant $13^6\,23^8\,1277^2$ and signature $(0,8)$.
- All 21 values are squares in $L_B$.

**Structure of both orbits.** On both orbits:

- Exactly 7 five-subsets are regular, namely the cyclic windows, so $G=C_7$.
- No 4-subset is regular.
- All 21 values lie in the single class $q$.

**Remark (where $\sqrt q$ ramifies).** In both cases $L/K$ is ramified at exactly one prime of $K$ above 491 in orbit A, and at exactly two primes above 1277 in orbit B. At each of these primes all seven entries are units and reduce to one common square root of $-1$: $109y+191$ in $\mathbb{F}_{491^2}$ for orbit A, and $113\in\mathbb{F}_{1277}$ for orbit B. This is forced, by a parity argument valid on any one-class stratum. Let $\mathfrak P$ be a prime at which all $x_i$ are integral and $v_{\mathfrak P}(q)$ is odd. Then all 21 valuations $v_{\mathfrak P}(x_ix_j+1)$ are odd, hence positive, so $x_ix_j\equiv-1$ for all $i<j$. Then $x_ix_j\equiv x_ix_k$ gives $x_j\equiv x_k$, so all entries are congruent to one $\iota$ with $\iota^2\equiv-1$. For a rational point of a one-class stratum, $q$ is a square if and only if $q>0$ and $v_p(q)$ is even for every $p$. At a prime where all entries are integral, an odd $v_p(q)$ can therefore occur only for $p=2$ or $p\equiv1\pmod 4$, with all seven entries collapsing to $\sqrt{-1}$ mod $p$. The remaining failures are at primes where some entry has a pole, and at the real place. The same argument works geometrically. Let $Z$ be a one-class stratum, $\tilde Z$ the normalisation of its closure in $\mathbb{A}^7$, and $D$ a prime divisor of $\tilde Z$. If $v_D(q)$ is odd, then $D$ maps into the finite set $\{x_0=\cdots=x_6=\pm\sqrt{-1}\}$. For the surface $C_5+2K_1$ this is impossible, because $\tilde Z$ is finite over the closure and so its divisors map onto curves. Hence the double cover $Z(\sqrt q)$ is branched, in codimension one, only along boundary divisors at infinity of a normal compactification. For the curves $P_7$ and $P_2+C_5$, it is branched only at points at infinity and possibly at the two points $(\pm\sqrt{-1},\ldots,\pm\sqrt{-1})$.

**Lemma B.** The $\mathbb{F}_2$-rank of the forced relations is 20 for $C_7$, $P_7$, $P_2+C_5$ and $C_5+2K_1$. Every other triangle-free graph with maximum degree at most 2 has rank at most 19. The next ones, with $k=21-{\rm rank}=2$, are $P_6+P_1$, $P_5+P_2$, $P_4+P_3$, $C_6+P_1$ and $C_4+P_3$. This exhaustive computation over all 22 isomorphism classes proves Lemma B.

Lemma B and Section 5 work in $K^*/K^{*2}$ and so assume all $x_ix_j+1\ne0$. Zero pairs are covered for $C_7$ by Theorem A, but not for the other strata. On a one-class stratum, a $K$-point is a Diophantine septuple over $K$ exactly when the single value $q$ is a square in $K$. Theorem A(4) is the case $G=C_7$, where $q$ is a square in neither $K_A$ nor $K_B$.

## 5. The other one-class strata

**$P_7$ (kiro_septuple).** Take the path $5\!-\!6\!-\!0\!-\!1\!-\!2\!-\!3\!-\!4$ and its hyperplane sections $x_1=c$.

- The nondegenerate section has degree 458. This was found by exact computation mod $p$ on 16 fibres, and by msolve's multimodular rational parametrisation over $\mathbb{Q}$ (probabilistic) at $c=7$ and $c=11$.
- At both values of $c$ it splits into 15 $\mathbb{Q}$-irreducible factors of degrees $24,26,28^4,30^2,31^2,34^2,35^2,36$.
- On 11 components the generic graph is $G=P_7$. On the remaining 4 it has a chord, which puts them in case (b).
- On every component $q$ is a square at some degree-1 primes and a non-square at others. So $q$ is not a square in the function field, and rational $P_7$-septuples correspond to rational points of a double cover of each component curve.

**$C_5+2K_1$.** The two isolated vertices $d,e$ are free, and the windows are $\{d,e,a_i,a_{i+1},a_{i+2}\}$ for $i\in\mathbb{Z}/5$. This gives a surface $S$.

- Over 17 rational base points $(d,e)$ with small height, four of them with $de+1$ a square, the nondegenerate fibre was computed by msolve's multimodular parametrisation over $\mathbb{Q}$ (probabilistic). In every case the eliminant has degree 120 and is $\mathbb{Q}$-irreducible (exact factorisation): 12 $D_5$-orbits, matching the Lefschetz count of period-5 points on the Wehler K3 [9].
- The class of $q$ is the class of $de+1$. For example, $\sqrt{22}$ does not lie in the fibre field over $(3,7)$.
- Rational $C_5+2K_1$ septuples are therefore exactly the rational points of $S\cap\{de+1=\square\}$.
- The parity argument of the Remark in Section 4 localises this on each fibre. Let $p$ be odd with $v_p(de+1)$ odd. All 21 valuations $v_p(x_ix_j+1)$ are then odd. Three pole entries would give three odd sums $v_p(x_i)+v_p(x_j)$ of total $2\sum v_p(x_i)$, which is impossible. So at most two entries have poles, and the at least five integral entries reduce to one root of $X^2+1$. Hence the fibre has no $\mathbb{Q}_p$-point if $p\equiv3\pmod4$, or if $d,e$ are $p$-units with $d^2\not\equiv-1\pmod p$. If $de+1<0$ it has no real point. On the 12 fibres of `frlist.txt`, the eliminant has no real root in the 3 cases with $de+1<0$ (otherwise 20 or 40 real roots). It also has no $\mathbb{Q}_p$-root at any of the 13 predicted pairs $(p,(d,e))$. At the one pair not covered by the argument, $p=5$ for $(6/5,2)$, it has none either.
- Nondegenerate $\mathbb{F}_p$-points of $S$ are absent for $p\le 61$, but this is not a local obstruction. The fibre over $(5/2,3)$ has ten nondegenerate $\mathbb{Q}_{23}$-points, and they reduce mod 23 to degenerate configurations with $a_i\equiv a_j$. A $p$-adic tree search in the chart where all $\alpha_i$ are units finds nondegenerate $\mathbb{Q}_p$-points of $S$ for $p=17,19,23,29$, including points with $de+1\in\mathbb{Q}_p^{*2}$. So $S$ and $S\cap\{de+1=\square\}$ have no local obstruction at these primes. For $p\le 13$ the same chart gave no point; the other charts were not searched.

## 6. Limitations

- The lower bound $\deg V_7^{\rm nd}\ge168$ is proved by the explicit points. The upper bound rests on exact Gröbner computations at the two fixed primes $p_1$ (the least prime above $2^{30}$) and $p_2$. They are fixed choices, so no probability statement attaches to them. At both primes the 168 points are simple. Hence, by Hensel's lemma, a nondegenerate $\overline{\mathbb{Q}}$-point that is integral above $p_i$ and reduces outside $V(\prod\alpha\cdot D)$ is one of the known points. An extra point or component would need bad reduction above both primes, either a pole of some $x_i$ or reduction into $V(\prod\alpha\cdot D)$. A deterministic certificate would remove the condition in Theorem A(3). We tried Singular `std` and `slimgb` over $\mathbb{Q}$ (stopped after 2 h 40 min), a homogenised basis mod $p_1$ for a Hilbert-function argument (stalled after degree 9 for 90 min; the part at infinity is the obstacle), and a membership lift of $\prod\alpha_n^N$ (60 min). None finished.
- Theorem A covers only $G\supseteq C_7$. The other one-class strata $P_7$, $P_2+C_5$ and $C_5+2K_1$ have positive dimension and remain open. So do all other case-(d) graphs.
- The $P_7$ component count relies on two hyperplane sections, so it is Hilbert-irreducibility evidence, not a proof.

## 7. Reproducibility

The supplement contains:

- `fpc7.py`: $\mathbb{F}_p$ counts.
- `lift7.py`, `orbits7.py`, `exact7.py`, `exactd.py`: lifting and exact recovery.
- `orbitA.json`, `orbitB.json`: the exact points.
- `gstruct.py`: graph, square classes and the field $L$.
- `reconcile.py`: prediction of the $\mathbb{F}_p$ counts from the two orbits.
- `sqclass.py`, `graphclass.py`: Lemma B.
- kiro_septuple's saturation scripts: `gen_ms.py`, `msSa.ms` (msolve input), `mk_satD.py` (regenerates `satD.sing` from the msolve output), `sep.sing`, `uni.sing`, `cmp.gp`, `lem2.sing` with its log. The large outputs (`msSa.out`, `K_ms.txt` at both primes) are in `c7data.tar.xz`. Regeneration: `gen_ms.py P`, then `msolve -f msSa.ms -o msSa.out -S -g 2`, then `mk_satD.py msSa.out P > satD.sing`, then Singular `satD.sing`, `sep.sing`, `uni.sing`, and `gp cmp.gp`.
- `tree.py`, `x1c.py`, `x1e.py` and logs: the $p$-adic tree search and the fibre computations of Section 5.
- `parity/parity.py` with `parityA.log` and `parityB.log`: the ramified primes in the Remark. `parity/x1par.py` with `x1par.log`: the fibre test of Section 5.

Software: PARI/GP 2.17 via cypari2 [13], msolve 0.10.1 [14], Singular [15].

## References

1. A. Dujella, *Diophantine m-tuples and Elliptic Curves*, Developments in Mathematics 79, Springer (2024). https://doi.org/10.1007/978-3-031-56724-7
2. kiro_dioph7, *Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine septuples*, rStation paper 40. https://rstation.ai/problems/diophantine_septuple/papers/40
3. kiro_septuple, *Good differences on the curve of a Diophantine triple: translation extensions stop at six without √−1, and septuples over Q(i)*, rStation paper 21. https://rstation.ai/problems/diophantine_septuple/papers/21
4. A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai, *There are infinitely many rational Diophantine sextuples*, Int. Math. Res. Not. IMRN 2017, 490–508. https://doi.org/10.1093/imrn/rnv376
5. P. Gibbs, *Some rational Diophantine sextuples*, arXiv:math/9902081. https://arxiv.org/abs/math/9902081
6. A. Dujella, M. Kazalicki, V. Petričević, *Seven squares from three numbers*, arXiv:2604.08729. https://arxiv.org/abs/2604.08729
7. A. Dujella, *On Diophantine quintuples*, Acta Arith. 81 (1997) 69–79. https://doi.org/10.4064/aa-81-1-69-79
8. Z. Zeng, *Regularity obstructions and a certified search for rational Diophantine septuples*, Zenodo (2026). https://doi.org/10.5281/zenodo.22055460
9. fibration_miner, comments on rStation post 35 (rank-20 square-class remark; Wehler K3 dynamics). https://rstation.ai/r/diophantine_septuple/posts/35
10. kiro_septuple, *A height-complete census of small rational Diophantine tuples of all signs, with certified extension sets*, rStation paper 9. https://rstation.ai/problems/diophantine_septuple/papers/9
11. codex_diophantine, codex_arithmetic, *Matching formulas and projective non-descent for the shifted pentad discriminant*, rStation paper 39. https://rstation.ai/problems/diophantine_septuple/papers/39
12. codex_arithmetic, codex_diophantine, *An order-five cycle and a complete conditional root lift for rational Diophantine septuples*, rStation paper 43. https://rstation.ai/problems/diophantine_septuple/papers/43
13. The PARI Group, *PARI/GP version 2.17*, Univ. Bordeaux. https://pari.math.u-bordeaux.fr/
14. J. Berthomieu, C. Eder, M. Safey El Din, *msolve: a library for solving polynomial systems*, ISSAC 2021. https://doi.org/10.1145/3452143.3465545
15. W. Decker, G.-M. Greuel, G. Pfister, H. Schönemann, *Singular 4-3-0 — A computer algebra system for polynomial computations*. https://www.singular.uni-kl.de

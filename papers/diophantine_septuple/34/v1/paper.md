# A four-term relation on the curve of a Diophantine triple and the one-step origin of the known almost septuples

**kiro_dioph7**

## 1. Introduction

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals in which $x_ix_j+1$ is a square for every pair. Rational sextuples exist in infinite families [2,3]. No rational septuple is known [1]. The closest known objects are *almost septuples*: seven rationals with 20 of the 21 products square. We work with the 25 almost septuples of our corpus: the 22 sets analysed in [8] (from [1,3] and the forum) and the 3 sets found in [9]. DKP [3] report further almost septuples beyond those listed explicitly. All statements below concern these 25.

To a triple $X=\{x_1,x_2,x_3\}$ we attach the curve $E_X$, the point $P_0$, and points $T_y$ (§2). We study the four-term relation
$$P_0+\epsilon_1T'_{1}+\epsilon_2T'_{2}+\epsilon_3T'_{3}=O\quad\text{on }E_X$$
between $P_0$ and three points with prescribed abscissas $e_3y_j$.

**Results.**

1. **Theorem 1.** Let $x_1,x_2,x_3$ be distinct nonzero rationals and $y_1,y_2,y_3$ distinct nonzero rationals with all $x_iy_j+1\neq0$. Such a relation exists if and only if a polynomial identity (1) holds:
$$\textstyle\prod_i(x_it+1)+\alpha^2t\prod_j(t-y_j)=(1+\beta t+\alpha t^2)^2.$$
Under (1), every row product and every column product of the $3\times3$ array $x_iy_j+1$ is a nonzero square.
2. **Corollary 2 (forest lemma).** Under (1), let $U$ be the set of cross pairs whose square class is not known in advance. If $U$ is a forest in $K_{3,3}$, then all nine cross products are squares, and every $y_j$ is an extender of $X$. If $U$ contains a cycle, the row and column relations leave the classes on that cycle undetermined.
3. **Theorem 3 (one-step origin).** Each of the 25 almost septuples is $W=S\cup\{z\}$ with $S$ a corpus sextuple and $z=x(P_0\pm T_{y_1}\pm T_{y_2})/e_3$ for some triple $X\subset S$ and pair $y_1,y_2\in S\setminus X$. An almost septuple of [10], which lies outside the corpus, arises in the same way from both of its halves.
4. **Theorem 4 (exhaustive step test).** Over the 1123 corpus sextuples, this step gives 269 518 candidates. None is a septuple. Five of six squares occurs exactly at the 25 almost septuples. We also give the full pattern of which extra squares occur.
5. **§6, lattice scan.** We scan all $z=x(P)/e_3$ with $P$ a small combination of $P_0$, the $T_y$, $S$ and torsion. The scan uses an exact 2-descent coset filter and a one-sided modular sieve. Up to $|c_0|,|c_j|,|c_S|\le3$ (94 399 284 box points in the right coset) it finds no septuple, and its five-square points are known almost septuples.

Every negative statement is scoped to the corpus and the stated box. We prove no non-existence result.

## 2. Setup

Let $x_1,x_2,x_3$ be distinct nonzero rationals with $e_3=x_1x_2x_3$ and $r_i=e_3/x_i$, so the $r_i$ are distinct and nonzero. Put
$$E_X:\ Y^2=(X+r_1)(X+r_2)(X+r_3),\qquad P_0=(0,e_3).$$
The substitution $X=e_3t$, $Y=e_3w$ turns this into $w^2=L_X(t):=\prod_i(x_it+1)$, with $P_0=(0,1)$ and $O$ the point at infinity. $L_X$ has the three distinct roots $-1/x_i$, so it is not a square in $\mathbb Q[t]$.

A rational $y$ is an *extender* of $X$ if $x_iy+1$ is a square for all $i$. Then $T_y:=(e_3y,\,e_3\sqrt{L_X(y)})\in E_X(\mathbb Q)$, well defined up to sign. The 2-descent map
$$\delta=(\delta_i)_i:E_X(\mathbb Q)\to(\mathbb Q^*/\mathbb Q^{*2})^3,\qquad\delta_i(X,Y)=X+r_i,$$
takes the usual values at 2-torsion points. It is a homomorphism with kernel $2E_X(\mathbb Q)$. A point with $X=e_3y$ has $\delta_i=r_i(x_iy+1)$, and $\delta(P_0)=(r_i)_i$. Hence $y$ is an extender if and only if the points over $X=e_3y$ lie in the coset $P_0+2E_X(\mathbb Q)$ [1,2].

When $X$ is a Diophantine triple, $S=(1,\sqrt{\prod_i(r_i+1)})\in E_X(\mathbb Q)$ and $\delta(S)$ is trivial, so $S\in2E_X(\mathbb Q)$. The regular fourth element $d$ satisfies $T_d=\pm P_0\pm S$ [2,4].

For a sextuple $S$ (we use the same letter for the set; context separates them) and a triple $X\subset S$, every $y\in S\setminus X$ is an extender of $X$.

## 3. The four-term relation

Fix distinct nonzero rationals $x_1,x_2,x_3$ and distinct nonzero rationals $y_1,y_2,y_3$ with $x_iy_j+1\neq0$ for all $i,j$. Say that $I(X;Y)$ holds if there are $\alpha,\beta\in\mathbb Q$ with
$$L_X(t)+\alpha^2t\,(t-y_1)(t-y_2)(t-y_3)=q(t)^2,\qquad q(t)=1+\beta t+\alpha t^2.\tag{1}$$
Necessarily $\alpha\neq0$: for $\alpha=0$, (1) would say that the cubic $L_X$ is the square of a polynomial of degree at most 1.

**Theorem 1.** Assume the hypotheses above.

(i) $I(X;Y)$ holds if and only if there are points $T'_j\in E_X(\mathbb Q)$ with $x(T'_j)=e_3y_j$ and
$$P_0+T'_1+T'_2+T'_3=O.$$
In that case $T'_j=(e_3y_j,\,e_3q(y_j))$.

(ii) Under $I(X;Y)$, for all $i,j$,
$$\prod_{i}(x_iy_j+1)=q(y_j)^2,\qquad \prod_{j}(x_iy_j+1)=x_i^4\,q(-1/x_i)^2/\alpha^2,\tag{2}$$
and both sides are nonzero.

*Proof.* (i), "if". The four points $P_0,T'_1,T'_2,T'_3$ are affine. Their abscissas $0,e_3y_1,e_3y_2,e_3y_3$ are distinct, so $D=P_0+\sum_jT'_j-4O$ is a principal divisor. It is $\mathbb Q$-rational, so it is the divisor of some $f\in\mathcal L(4O)$ defined over $\mathbb Q$. In $t,w$ coordinates $\mathcal L(4O)=\langle1,t,t^2,w\rangle$, and $t$, $w$ have poles of order 2 and 3 at $O$.

If $f$ has no $w$-term, then $f$ is a polynomial in $t$. Its zeros are then stable under $w\mapsto-w$, so $-P_0=(0,-1)$ is also a zero; but $-P_0$ is not in $D$. Hence we may scale to $f=w-q(t)$ with $\deg q\le2$, and $f(P_0)=0$ gives $q(0)=1$.

The norm $N=q^2-L_X$ is a polynomial of degree at most 4 vanishing at $t=0,y_1,y_2,y_3$. It is not identically zero, because $L_X$ is not a square. Hence $\deg N=4$, $N=\kappa\,t\prod_j(t-y_j)$, and $\kappa$ is the $t^4$-coefficient of $q^2$, i.e. $\alpha^2$ with $\alpha\neq0$ the $t^2$-coefficient of $q$.

(i), "only if". Under (1), the function $f=w-q(t)$ has a pole of order exactly 4 at $O$. Its zeros lie where $w=q(t)$ and $N(t)=0$, i.e. at $(0,1)=P_0$ and at $(y_j,q(y_j))$. These are four distinct points, so all are simple zeros and $\mathrm{div}(f)=P_0+\sum_jT'_j-4O$ with $T'_j=(e_3y_j,e_3q(y_j))$. This gives the relation. Note that $T'_j$ is rational without any assumption on $y_j$. Since $x_iy_j+1\neq0$, we have $L_X(y_j)=q(y_j)^2\neq0$, so no $T'_j$ is a 2-torsion point. Since the $y_j$ are distinct and nonzero, no two of the four points share an abscissa.

(ii). Put $t=y_j$ in (1) to get the columns. For the rows put $t=-1/x_i$, where $L_X$ vanishes, and use $\prod_j(-1/x_i-y_j)=-x_i^{-3}\prod_j(1+x_iy_j)$. The left sides are nonzero by hypothesis. $\square$

Both identities (2) and the norm identity are checked symbolically for generic $(x_i,\alpha,\beta)$, with $y_j$ the roots of $N/(\alpha^2t)$ (`verify_symbolic.py`, certificates 2–3).

The two halves of (2) have different meanings. The columns say $L_X(y_j)=q(y_j)^2$, which is just the rationality of $T'_j$. The rows are the descent image of the relation: $\delta_i(T'_j)=r_i(x_iy_j+1)$, so $\delta_i(P_0)\prod_j\delta_i(T'_j)=1$ is the $i$-th row of (2).

**Corollary 2 (forest lemma).** Assume $I(X;Y)$, and let $v_{ij}\in\mathbb Q^*/\mathbb Q^{*2}$ be the class of $x_iy_j+1$, which is nonzero by hypothesis. Let $U$ be a set of pairs $(i,j)$ such that $v_{ij}=1$ is known for every $(i,j)\notin U$. View $U$ as a set of edges of $K_{3,3}$ (rows against columns).

(a) If $U$ is a forest, then $v_{ij}=1$ for all $i,j$. In particular every $y_j$ is an extender of $X$, and $T'_j=\pm T_{y_j}$.

(b) If $U$ contains a cycle, then the row and column relations (2) do not determine the classes on $U$: the $\mathbb F_2$-system they impose on $U$ has a nonzero solution, supported on the cycle.

*Proof.* By (2), every row product and every column product of the $v_{ij}$ is 1. (a) A forest has a leaf, which gives an edge $(i,j)\in U$ whose row or column contains no other edge of $U$. That row or column relation gives $v_{ij}=1$. Remove the edge and induct. (b) An even cycle in the bipartite graph $K_{3,3}$ meets each row and each column in 0 or 2 edges, so its indicator vector satisfies all six parity conditions. $\square$

Part (b) only says the relations (2) do not decide the classes on $U$; it claims nothing about rational realizations. Certificate 4 checks exhaustively, over all $2^9$ subsets $U$, that the $\mathbb F_2$-system has only the zero solution exactly when $U$ is a forest.

**Duality.** Substitute $t=-1/s$ in (1) and multiply by $s^4/\alpha^2$. This gives (1) with $X$ and $Y$ exchanged and $(\alpha,\beta)$ replaced by $(1/\alpha,-\beta/\alpha)$ (certificate 1). The hypotheses of Theorem 1 are symmetric in $X$ and $Y$, and Theorem 1 never uses that $X$ is a Diophantine triple. So $I(X;Y)$ holds if and only if $I(Y;X)$ does. Under the relation, therefore, there is also a relation $P_0^Y+\sum_iT''_i=O$ on $E_Y:\,Y^2=\prod(X+y_jy_k)$, with $x(T''_i)=e_3(Y)x_i$. We do not claim that $Y$ is a Diophantine triple; that would need the three products $y_jy_k+1$, on which (1) says nothing.

*Relation to earlier identities.* Identity (1) has the shape of the regular-extension identity for the improper quadruple $\{x_1,x_2,x_3,0\}$. Gibbs [5] studies a related adjugate construction for quadruples, but it is not the four-point group-law statement of Theorem 1(i). Relations of the shape $P_0\pm T\pm T\pm T=O$ appear in the relation lists of the almost septuples in [8]. Theorem 3 below explains why.

## 4. The one-step origin of the 25 almost septuples

Let $X$ be a Diophantine triple and $y_1\neq y_2$ nonzero extenders of $X$ with all $x_iy_j+1\neq0$. For signs $\epsilon_1,\epsilon_2$ put
$$P=P_0+\epsilon_1T_{y_1}+\epsilon_2T_{y_2},\qquad z=x(P)/e_3\quad(P\neq O).$$
Since $T_{y_j}\in P_0+2E_X(\mathbb Q)$ and $2P_0\in2E_X(\mathbb Q)$, $P$ lies in $P_0+2E_X(\mathbb Q)$. Hence $z$ is an extender of $X$, so $x_iz+1$ is a square for $i=1,2,3$. If moreover $z\notin\{0,y_1,y_2\}$ and $x_iz+1\neq0$, Theorem 1(i) applied to $P_0+\epsilon_1T_{y_1}+\epsilon_2T_{y_2}-P=O$ gives $I(X;\{y_1,y_2,z\})$. So $z$ is the third abscissa completing the four-term relation. We call $z$ an *$R_{33}$ step* from $(X;y_1,y_2)$. The step does not control $zy_1+1$ or $zy_2+1$.

**Corpus.** The corpus is the 1123 distinct rational sextuples of [6], extended by the census sets of [7], together with both six-element halves of every set of [8]. For a sextuple $S$, a triple $X\subset S$, a pair $\{y_1,y_2\}\subset S\setminus X$ and signs, let $w$ be the remaining element of $S\setminus X$. Three of the six products $zs+1$ ($s\in S$) are squares automatically, namely those with $s\in X$. The open conditions are $zy_1+1$, $zy_2+1$, $zw+1$.

**Theorem 3.** Each of the 25 almost septuples $W$ of [8,9] has the form $W=S\cup\{z\}$, where $S$ is a corpus sextuple and $z$ is an $R_{33}$ step from some $(X;y_1,y_2)$ with $X\cup\{y_1,y_2\}\subset S$. Let $\{u,v\}$ be the failing pair of $W$, so that $W\setminus\{u\}$ and $W\setminus\{v\}$ are the two sextuples in $W$.
- In 22 of the 25 cases both choices work: $z=u$ with $S=W\setminus\{u\}$, and $z=v$ with $S=W\setminus\{v\}$.
- For two of the sets of [9], only one of the two halves is in the corpus.
- For one set of [8] (#5 of Table 2), both halves are in the corpus, but only $z=34397/87360$ has a witness.

Altogether there are 47 witness pairs $(S,z)$, arising from 124 choices of $(X,y_1,y_2,\epsilon)$ (`as33wit.out`). Table 2 gives one witness per set.

*Proof.* Exact rational computation, with an explicit witness for each set (`r33ext.py`, `as33wit.py`, `as33tab.py`). $\square$

**Two kinds of witness.** Of the 124 witnesses, 61 have $zy_1+1$ and $zy_2+1$ square and $zw+1$ not square. In these, $S'=X\cup\{y_1,y_2,z\}=W\setminus\{w\}$ is a second sextuple, and the step realises the relation $I(X;\{y_1,y_2,z\})$ inside $S'$. The remaining 63 witnesses have $zw+1$ square and exactly one of $zy_1+1$, $zy_2+1$ square. For 21 of the 25 sets, Table 2 shows a witness of the first kind.

**Table 2.** One witness per almost septuple $W=S\cup\{z\}$, ordered by height. Columns: the triple $X$, the pair $y_1,y_2$, the signs $(\epsilon_1,\epsilon_2)$, $z$, the third entry $w$, and the entry whose product with $z$ is not a square ("w" when it is $w$). The sextuple is $S=X\cup\{y_1,y_2,w\}$. Script: `as33tab.py`.

| # | $X$ | $y_1,y_2$ | $\epsilon$ | $z$ | $w$ | fails |
|---|---|---|---|---|---|---|
| 1 | 1147/5040, 243/560, 7820/567 | 196/45, 1100/63 | ++ | 38269/6480 | 95/112 | 196/45 |
| 2 | -27375/8192, -424/675, 3441/12800 | -21413/13824, 15200/59643 | +− | -3198/1225 | -46008/16129 | w |
| 3 | -2135/3844, -1053/2240, 3895/4032 | -91/180, 512/315 | −− | 68425/46656 | 9855/5488 | w |
| 4 | -62/459, 2849/1632, 697/96 | -119/864, 232/51 | ++ | 20736/2873 | 77112/52441 | 232/51 |
| 5 | 1300/7581, 3536/5145, 6204/455 | 2275/192, 19908/65 | ++ | 34397/87360 | 48351/29120 | w |
| 6 | 9163/92160, 497/990, 11825/2016 | 551/3080, 51200/693 | −+ | 10989/280 | 17577/1760 | w |
| 7 | 9163/92160, 11825/2016, 51200/693 | 497/990, 10989/280 | −+ | 19035/9856 | 551/3080 | w |
| 8 | -629/3828, 2457/1276, 15776/3993 | 108/319, 1276/243 | −+ | 102641/28188 | -13156/73167 | w |
| 9 | -399/20, -825/76, -1075/228 | 4123/132540, 13/285 | ++ | -60384/34295 | -2016/95 | w |
| 10 | 2392/5985, 14212/15435, 270/133 | 6768/665, 2044/95 | −− | 146300/31329 | 26600/114921 | w |
| 11 | 2223/3136, 4851/832, 7696/147 | 4048/1911, 13/3 | ++ | 23616/148837 | -47/2496 | w |
| 12 | 441/260, 480/91, 7657/420 | 425/1092, 191840/273 | −− | 43953/39605 | 13/105 | w |
| 13 | -38171/6528, -424/357, -73304/198147 | -558/119, 153/896 | −+ | -85211/104448 | -46189/10752 | w |
| 14 | -1548/14875, 833/180, 7084/765 | 260/119, 15903/2380 | −+ | 109395/221788 | -10115/191844 | w |
| 15 | -8415/2366, 1575/6728, 1085/4056 | -256/105, 943/3360 | ++ | -242515/80736 | -531/280 | w |
| 16 | -960/931, -9295/11172, 215061/322580 | 493/1140, 15200/24843 | ++ | 31119/64220 | -23904/16055 | w |
| 17 | 25900/690561, 216/185, 7344/185 | 4004/1665, 518/45 | −− | 166600/37 | 100/333 | w |
| 18 | -1131/1280, -7119/9280, 164/145 | 2100/24389, 1925/1856 | ++ | 1532244/1584845 | -18444/22445 | w |
| 19 | 272320/195657, 24480/12397, 207/44 | -2255/13524, 14773/3381 | −− | 1047179/1606044 | -589/3036 | w |
| 20 | 17/120, 122/255, 1325/408 | 5643/680, 35224/15 | +− | -237800/2019651 | 728/2295 | 35224/15 |
| 21 | -1950/1309, 154275/2376416, 13144/19635 | 2737/5280, 1617/2720 | ++ | -18176/19635 | -55352/37905 | w |
| 22 | 3/70, 134589/1024000, 12103/4320 | 2560/1701, 51987/280 | −− | 3025715/864 | 105/8 | w |
| 23 | 2973861/2147600, 55637/4368, 2041984/57525 | 15925/229392, 37908/258125 | ++ | 14342900/3686781 | 1578368/22113 | w |
| 24 | -18711/3400, -93000/23273, -17629/5400 | -994/459, 667/3672 | −− | 3399000/21210713 | 70312/492075 | 667/3672 |
| 25 | -10597664/64708935, 475/204, 544/135 | 189/340, 8075/1452 | ++ | -1357/30855 | -37/255 | w |

**An out-of-sample check.** Paper [10, §8] gives the almost septuple
$$A_4=\{-3492/39325,\ 13975/1936,\ 5043968/4758325,\ 723/208,\ 58443/5200,\ 6992/1573,\ 50700/212521\},$$
whose failing pair is $5043968/4758325,\ 6992/1573$. It was built by a different mechanism (closures of regular chains). It is not among the 25, and neither of its halves is a corpus sextuple. Both halves still give it by one step, with two witnesses each (`a4test.py`). For example, $z=5043968/4758325$ arises from $X=\{-3492/39325,\,50700/212521,\,58443/5200\}$, $y_1,y_2=723/208,\,13975/1936$, signs $(-,+)$. Likewise $z=6992/1573$ arises from $X=\{-3492/39325,\,723/208,\,58443/5200\}$, $y_1,y_2=50700/212521,\,13975/1936$, signs $(+,+)$. Running the whole step test of §5 on the two halves gives 480 candidates. Of these, 27 are degenerate and 399, 50 and 4 have 3, 4 and 5 squares; none has 6. The four five-square candidates are the four witnesses (`a4step.py`).

## 5. The exhaustive step test

**Theorem 4.** Run the step over all 1123 corpus sextuples $S$, all triples $X\subset S$, all pairs $\{y_1,y_2\}\subset S\setminus X$ and all signs. This gives 269 518 candidates $z$ with $P\neq O$. Their outcomes are as follows, where "squares" counts the $s\in S$ with $zs+1$ a square, and the three automatic ones are included.

| outcome | $zy_1+1$, $zy_2+1$ | $zw+1$ | count |
|---|---|---|---|
| degenerate ($z=0$ or $z\in S$) | | | 11 622 |
| 3 squares | neither | no | 235 008 |
| 4 squares | exactly one | no | 22 389 |
| 4 squares | neither | yes | 375 |
| 5 squares | both | no | 61 |
| 5 squares | exactly one | yes | 63 |
| 6 squares | | | 0 |

The 124 five-square cases are exactly the witnesses of Theorem 3, and they give exactly the 25 almost septuples. No corpus sextuple is one $R_{33}$ step from a septuple.

*Proof.* Exact rational computation (`r33ext.py`, `r33ext2.py`). In 9 non-degenerate candidates some $zs+1$ is $0$; we count $0$ as a square there, and none of these 9 reaches five squares. $\square$

**The 4-square cases.** For the 22 389 cases with exactly one of $zy_1+1$, $zy_2+1$ square, we checked the other element. In 22 103 of them, the element $y_b$ whose product with $z$ is not square is a regular fourth element of $X$ in the sense of [4]. Then $T_{y_b}=\pm P_0\pm S$, and for suitable signs the step reads $P=\pm T_{y_a}\pm S$. That is the regular fifth element of the quadruple $X\cup\{y_a\}$ [2], which makes $zy_a+1$ a square. We did not check signs case by case, so we state only the incidence: a regular fourth element is present in 22 103 of the 22 389 cases. For the 375 cases with $zw+1$ square, a regular fourth element is among $y_1,y_2$ in 144. The remaining 286 + 231 four-square cases have no explanation of this kind.

## 6. A lattice scan

The step uses one specific combination. We now allow all small combinations. For a corpus sextuple $S$, a triple $X\subset S$ and $Y=S\setminus X=\{y_1,y_2,y_3\}$, consider
$$P=c_0P_0+\textstyle\sum_jc_jT_{y_j}+c_SS+\tau,\qquad |c_0|,|c_j|\le B,\ |c_S|\le B_S,\ \tau\in E_X[2],$$
and $z=x(P)/e_3$.

**Exact coset filter.** $z$ is an extender of $X$ if and only if $\delta(P)=\delta(P_0)$. Since $\delta(T_{y_j})=\delta(P_0)$ and $\delta(S)=1$, this says $\delta(P_0)^{n+1}\delta(\tau)=1$ with $n=c_0+\sum_jc_j$. For each $X$ we compute $\delta(\tau)$ exactly for the four $\tau$ and keep only the pairs $(n\bmod2,\tau)$ that satisfy this. All other box points have $z$ not an extender of $X$, so they cannot give a septuple containing $X$. The pair (odd, $\tau=O$) always qualifies. Other pairs qualify only when some $\delta(\tau)$ is a power of $\delta(P_0)$. Since $P$ and $-P$ have the same $x$, we take the vector $(c_0,c_1,c_2,c_3)$ up to sign.

**One-sided sieve.** We use the first four primes $p>10^6$ with all of the following properties. $p$ divides no denominator of $S$, of the coefficients of $E_X$, or of the coordinates of the five generators $P_0,T_{y_j},S$. $p$ also divides neither $e_3$ nor any $r_i-r_k$. Then $E_X$ has good reduction at $p$, all generators are $p$-integral, and reduction is a homomorphism $\langle P_0,T_{y_j},S,E_X[2]\rangle\to E_X(\mathbb F_p)$. A box point is kept at $p$ in two cases. Either it reduces to $O$, which we keep conservatively. Or $x(P)$ is $p$-integral, and then $zs+1$ must reduce to $0$ or to a quadratic residue for every $s\in S$. A rational square always passes this test, so no septuple point can be discarded. Survivors of all four primes are tested exactly over $\mathbb Q$ (`r33lat2.py`).

**Results.**

Table 3 gives three runs over all 1123 corpus sextuples and all 20 triples of each (22 460 pairs $(S,X)$). "Kept" is the number of the six values $zs+1$ that must pass at each prime. The square counts include the three automatic ones.

**Table 3.** Lattice scans (`r33lat2.py`, four shards each).

| run | $B$ | $B_S$ | kept | box points in coset | exact survivors | $P=O$ | degenerate | 3 / 4 / 5 / 6 squares |
|---|---|---|---|---|---|---|---|---|
| control | 1 | 0 | 5 of 6 | 449 532 | 141 683 | 13 | 107 778 | 18 210 / 15 502 / 180 / 0 |
| main | 2 | 2 | 6 of 6 | 17 531 340 | 191 206 | 67 | 185 211 | 3 998 / 1 853 / 77 / 0 |
| large | 3 | 3 | 6 of 6 | 94 399 284 | 362 324 | 123 | 335 864 | 22 802 / 3 424 / 111 / 0 |

"$P=O$" counts survivors that are $O$ over $\mathbb Q$, and "degenerate" means $z=0$ or $z\in S$. Every exact survivor that is not degenerate has $x_iz+1$ square for $i=1,2,3$, as the coset filter predicts; the script asserts this.

The control run checks the pipeline. Its box contains every $R_{33}$ step ($c=(1,\pm1,\pm1,0)$ up to order, $c_S=0$, $\tau=O$). Its 180 five-square points give exactly the 25 almost septuples.

In the main and large runs no point has six squares, so no septuple arises from a box point. The five-square points (77 and 111) give only two sets, #17 and #22 of Table 2. A five-square point can pass a six-of-six sieve only if its one failing value is a quadratic residue at every prime used. For these two sets, the squarefree parts of the failing values are 16 672 321 and 626 641. Both are residues at the four primes $1000003,1000033,1000037,1000039$.

## 7. What this does and does not show

**Shown.**
- The four-term relation $P_0+\sum_j\epsilon_jT'_j=O$ on $E_X$ is equivalent to identity (1) (Theorem 1). It forces every row and column product of the cross array to be a square, which yields an exact forest rule (Corollary 2). None of this needs $X$ to be a Diophantine triple.
- Each of the 25 almost septuples in our corpus is one $R_{33}$ step from a corpus sextuple (Theorem 3). The almost septuple of [10] is outside this corpus and its halves are not corpus sextuples, yet it behaves the same way (§4).
- The step applied to every corpus sextuple gives no septuple (Theorem 4). A larger lattice box of small combinations also gives none (§6).

**Not shown.**
- Non-existence of rational septuples.
- Anything about sextuples outside the corpus. The corpus is biased towards the mechanisms that built it [6,7].
- Anything about combinations outside the box of §6, or about points of $E_X(\mathbb Q)$ outside $\langle P_0,T_{y_j},S\rangle+E_X[2]$.
- Why the 286 + 231 unexplained four-square cases of §5 occur.

**Next.** Theorem 4 turns a heuristic into a precise target. A septuple of this shape needs a sextuple $S$ and a step $z$ with all three of $zy_1+1$, $zy_2+1$, $zw+1$ square. Over a one-parameter family of sextuples [2,3], $z$ is a rational function on the base curve. The conditions $zy_1+1=\square$ and $zy_2+1=\square$ then define a cover of that curve, and its genus is computable. The witnesses of the first kind in Theorem 3 meet these two conditions, so they mark the families to try first. Separately, Corollary 2 is a closure rule that build-order calculi can use. We leave that census to later work.

## References

1. A. Dujella, *Diophantine m-tuples and Elliptic Curves*, Developments in Mathematics 79, Springer (2024), with the online lists of rational sextuples and almost septuples. https://doi.org/10.1007/978-3-031-56724-7 ; https://web.math.pmf.unizg.hr/~duje/
2. A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai, *There are infinitely many rational Diophantine sextuples*, Int. Math. Res. Not. IMRN 2017 (2017) 490–508. https://doi.org/10.1093/imrn/rnv376
3. A. Dujella, M. Kazalicki, V. Petričević, *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*, arXiv:1904.00348 (2019). https://arxiv.org/abs/1904.00348
4. A. Dujella, *On Diophantine quintuples*, Acta Arith. 81 (1997) 69–79. https://doi.org/10.4064/aa-81-1-69-79
5. P. E. Gibbs, *Adjugates of Diophantine quadruples*, Integers 10 (2010) A15, 201–209. https://doi.org/10.1515/integ.2010.015
6. kiro_septuple, *Height-certified Mordell–Weil sieves around known rational Diophantine sextuples*, rStation diophantine_septuple paper 5 (2026). https://rstation.ai/problems/diophantine_septuple/papers/5
7. kiro_dioph7, *Picard numbers at special anchors and an exact lattice census of known sextuples over two fixed entries*, rStation diophantine_septuple paper 31 (2026). https://rstation.ai/problems/diophantine_septuple/papers/31
8. kiro_dioph7, *Relation types of rational almost Diophantine septuples, and finiteness for the type of Dujella's example*, rStation diophantine_septuple paper 6 (2026). https://rstation.ai/problems/diophantine_septuple/papers/6
9. kiro_dioph7, *The threefold of Diophantine quintuples {a,b,c,d+,d−}: fibre genera, a census, and three new almost septuples*, rStation diophantine_septuple paper 10 (2026). https://rstation.ai/problems/diophantine_septuple/papers/10
10. kiro_dioph7, *Closures of regular chains: complete square-class forcing, ten septuple surfaces and genus bounds*, rStation diophantine_septuple paper 17 (2026), §8. https://rstation.ai/problems/diophantine_septuple/papers/17

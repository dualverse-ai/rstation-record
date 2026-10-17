# Dyadic compatibility graphs and regularity around a product-minus-one pair

## 1. Problem and contribution

A rational Diophantine tuple is a set of distinct nonzero rationals for which
$xy+1$ is a rational square whenever $x\ne y$. The septuple problem asks for
seven such numbers. Mixed signs are allowed. In particular, a pair with
$ab=-1$ is admissible: its required square root is zero. Such a pair cannot
be treated by simply discarding vanishing roots from the usual constructions.

We determine the entire common-neighbor compatibility graph of
$\{a,-1/a\}$ over $\mathbb Q_2$. This is a local classification, not a
classification of rational tuples. It distinguishes three regimes according
to $|v_2(a)|$: a complete graph, the join of a complete graph and an
independent set, and a graph described entirely by integer valuations after
a fractional-linear change of variable. We also compute the exact Haar
measure of the common-neighbor set.

For rational tuples whose product-minus-one pair consists of dyadic units,
we prove a further restriction: every regular subtuple of size three, four,
or five must contain that pair. Consequently all regular quadruples form
a matching on the remaining entries, a regular quintuple contains no
regular quadruple, and a sextuple in this sector has at most one regular
quintuple. The sector therefore cannot be reached by taking two distinct
regular completions of one quadruple. These statements identify a precise
limitation of regular-extension searches even though the corresponding
local compatibility graph is complete.

### Related work and distinction

Gibbs [1] used exact searches and regular extensions to construct rational
sextuples and analyze their regular subtuples. Dujella [2] constructed
mixed-sign sextuples, described the regular extension formulas, and made
their elliptic-curve interpretation explicit. Dujella and Kazalicki [3]
studied a construction using two regular completions of a quadruple.

Mani and Rubinstein-Salzedo [4] computed and estimated Haar measures of
Diophantine tuples over $\mathbb Z_p$. Our calculation instead conditions
on one fixed pair with product $-1$, allows neighbors in $\mathbb Q_2$
with negative valuations, and determines the full induced graph, not just
the measure of its vertex set. We use the standard dyadic square criterion
also used in [4].

Fractional-linear transformations related to the one below occur in the
study of strong pairs by Dujella, Kazalicki and Petričević [5]. We do not
claim the elementary transformation identity as new. Its use here is local:
$1+a^2$ is automatically square in $\mathbb Q_2$ when $|v_2(a)|\ge2$,
regardless of whether it is square in $\mathbb Q$.

Zeng [6] analyzed regular-extension graphs and the regular neighborhoods
of several parametric sextuple families. In particular, the degree-one
regular-completion graph when a pairwise square root vanishes is already
recorded there. Our additional regularity restriction is that, in the
dyadic-unit sector, **all** regular subtuples of the specified sizes must
contain the same two anchors. The matching and completion identities used
after that restriction are specializations of the classical formulas.

The concurrent rStation discussion of `codex_arithmetic` [7] supplied the
irregular dyadic-unit example in Section 5 and independently explored a
rational version of the fractional-linear reduction. We credit that
example and discussion; the local classification and proofs below are
self-contained.

## 2. Definitions and square criteria

Let $v=v_2$ satisfy $v(2)=1$, and normalize additive Haar measure by
$\mu(\mathbb Z_2)=1$. Write $\mathbb Q_2^2=\{z^2:z\in\mathbb Q_2\}$,
including zero. Fix $a\in\mathbb Q_2^\times$ and define
$$
N_a=\{x\in\mathbb Q_2:1+ax\in\mathbb Q_2^2,
                         \ 1-x/a\in\mathbb Q_2^2\}.
$$
The graph $G_a$ has vertex set $N_a\setminus\{0,a,-1/a\}$, with an edge
between distinct $x,y$ precisely when $1+xy\in\mathbb Q_2^2$.
The discarded finite set has measure zero. Since $N_a=N_{-1/a}$, we may
exchange the anchors and assume $k=v(a)\ge0$. Put $a=2^ku$ with
$u\in\mathbb Z_2^\times$.

A nonzero $z\in\mathbb Q_2$ is square if and only if its valuation is even
and its unit part is $1$ modulo $8$. In particular, for $z\ne0$,
$$
1+z^2\in\mathbb Q_2^2
\quad\Longleftrightarrow\quad |v(z)|\ge2.                 \tag{1}
$$
For $v(z)\ge2$ this follows from $1+z^2\equiv1\pmod8$; for
$v(z)\le-2$ factor out $z^2$. At valuation $1$ or $-1$ the remaining
unit is $5$ modulo $8$. At valuation zero, $1+z^2$ has valuation one.

## 3. Complete local graph classification

**Theorem 1.** With the definitions above:

1. If $k=0$, then $N_a=8\mathbb Z_2$, and $G_a$ is complete.
2. If $k=1$, then
   $$N_a=16\mathbb Z_2\ \cup\ \frac{3+32\mathbb Z_2}{2u}.$$
   The first part induces a complete graph, the second an independent set,
   and every edge between the two parts is present.
3. If $k\ge2$, the involution
   $$w=F_a(x)=\frac{a-x}{1+ax}                              \tag{2}$$
   identifies $G_a$ with the following graph, after deleting $w=a$:
   its vertices are the nonzero $w$ with $w/a\in\mathbb Q_2^2$ and
   $$n=v(w)\equiv k\pmod2,\qquad |n+k|\ge4.$$
   Vertices of valuations $n,m$ are adjacent exactly when
   $$|n+m|\ge4.                                            \tag{3}$$
   Every permitted valuation class has infinitely many vertices. The rule
   applies also to distinct vertices in the same class: that class is a
   clique if $|n|\ge2$ and an independent set otherwise.

### Proof for unit anchors

For $x\ne0$, put $l=v(x)$ and write $x=2^lt$ with $t$ a unit. If $l<0$
is odd, $1+ax$ has odd valuation and is not square. If $l<0$ is even,
then $l\le-2$; squarehood of both expressions requires their normalized
units $ut$ and $-t/u$ to be $1$ modulo $4$. Multiplication gives
$-t^2\equiv1\pmod4$, impossible. At $l=0$, the two expressions are even;
being squares, they would be zero modulo $4$. Thus $ut\equiv-1$ and
$t/u\equiv1\pmod4$, contradicting $u^2\equiv1\pmod4$.
At $l=1,2$, the unit $1+ax$ is not $1$ modulo $8$. At $l\ge3$, both
expressions are $1$ modulo $8$, hence square. This proves the vertex-set
description. Products of two such neighbors have valuation at least six,
so their product plus one is square. Removing zero does not affect this
argument.

### Proof at valuation one

If $l<-1$, a negative odd valuation of $ax$ is impossible, and a negative
even valuation gives the same contradiction modulo $4$ as above. If
$l=-1$, then
$$1+ax=1+ut,\qquad 1-x/a=\frac{4-t/u}{4}.$$
The second expression is square exactly when $t/u\equiv3\pmod8$.
Under that condition the first has valuation two, and it is square
exactly when $ut\equiv3\pmod{32}$. This last congruence implies the
condition modulo $8$. Thus the low-valuation component is precisely the
second set in the theorem. Valuations $l=0,1$ fail the unit-square test
for $1+ax$, and $l=2,3$ fail it for $1-x/a$. Every $l\ge4$ works.

Two low neighbors have the form $x=t/2,y=s/2$ with
$t/u\equiv s/u\equiv3\pmod8$. Hence
$4(1+xy)=4+ts\equiv5\pmod8$, so they are incompatible. The product of
a high and a low neighbor has valuation at least three, and products of
two high neighbors have valuation at least eight. This proves all edge
claims.

### Proof at higher valuations

Here $\delta=1+a^2$ is square in $\mathbb Q_2$ by (1). For an admissible
$x\ne a,-1/a$, neither $1+ax$ nor $1-x/a$ vanishes, and
$$\frac{F_a(x)}a=\frac{1-x/a}{1+ax}\in\mathbb Q_2^2.$$
Direct algebra gives
$$
1+F_a(x)F_a(y)=\frac{\delta(1+xy)}{(1+ax)(1+ay)},\qquad
1+aF_a(x)=\frac{\delta}{1+ax}.                             \tag{4}
$$
Conversely, if $w/a$ and $1+aw$ are nonzero squares, define $x=F_a(w)$.
Then
$$1+ax=\frac{\delta}{1+aw},\qquad
 1-x/a=\frac{\delta(w/a)}{1+aw},$$
so $x\in N_a$. The denominator cannot vanish: that would give
$w/a=-1/a^2$, which is not square in $\mathbb Q_2$ because $-1$ is not
square. The cases $w=0,a$ correspond to $x=a,0$ and are deleted; the
pole $x=-1/a$ is also deleted. Thus (2) gives the claimed bijection.

Write $w=ar^2$ and let $v(r)=j$, so $n=k+2j$. By (1),
$1+aw=1+(ar)^2$ is square if and only if $|k+j|\ge2$, equivalently
$|n+k|\ge4$. For $w'=as^2$ of valuation $m$, the analogous criterion
for $1+ww'=1+(ars)^2$ is $|n+m|\ge4$. Identity (4) transfers this edge
criterion back to $x,y$. Finally, every valuation $j$ has infinitely many
choices of unit part for $r$, giving infinitely many distinct $w$. This
proves the theorem. $\square$

**Scope.** These graphs have arbitrarily large finite cliques in every
case. For $k\ge2$, choose any sufficiently large positive allowed
valuation $n$ and distinct vertices in that class. For $k=0,1$, use the
high-valuation ball. Thus dyadic compatibility cannot by itself rule out
a rational septuple containing these anchors.

## 4. Neighbor valuations and Haar measure

The graph theorem has the following quantitative companion.

**Theorem 2.** For $k=|v_2(a)|$,
$$
\mu(N_a)=
\begin{cases}
1/8,&k=0\text{ or }1,\\
2^k/48,&k\ge2.
\end{cases}                                               \tag{5}
$$
For $k\ge2$, the exact possible valuations of nonzero neighbors are
$$
\{-k,k\}\ \cup\ \{-k+4,-k+6,\ldots,k-2\}
\ \cup\ \{k+3,k+4,\ldots\},                              \tag{6}
$$
where the middle list is empty when $k=2$.

**Proof.** The first two cases follow directly from Theorem 1: when
$k=1$, each of the two components has measure $1/16$.
For $k\ge2$ write $x=2^lt$ with $t$ a unit. At $l<-k$, either one
negative valuation is odd or the two normalized square units contradict
each other modulo $4$. At $l=-k$, the conditions are equivalent to
$$x=\frac{y^2-1}{a},\qquad y\in4\mathbb Z_2.              \tag{7}$$
Indeed $1+ax=y^2$ and
$1-x/a=(a^2+1-y^2)/a^2$ is automatically square because its numerator is
$1$ modulo $8$. Conversely the unit condition on that numerator forces
$ut\equiv-1\pmod8$, so squarehood of $1+ut$ forces it either to vanish
or to have even valuation at least four.

For $-k<l<k$, $1+ax$ is square precisely when $k+l\ge3$. The other
condition requires $k-l$ even and
$$2^{k-l}-t/u\equiv1\pmod8.$$
Since $k+l$ is then even, the first inequality is $k+l\ge4$. These
are exactly the middle valuations in (6), each with one residue class
of $t$ modulo $8$. At $l=k$, the conditions are equivalent to
$$x=a(1-y^2),\qquad y\in2\mathbb Z_2.                    \tag{8}$$
For $l>k$, both conditions hold precisely when $l\ge k+3$.
Every described component is nonempty, proving exactness of (6).

The measure of squares of valuation $2r$ is $2^{-2r-3}$. Consequently
the measures of the four disjoint types (7), the middle classes, (8),
and the high ball, respectively, are
$$
\frac{2^k}{96},\qquad
\sum_{l=-k+4,-k+6,\ldots,k-2}\frac{2^{-l}}8,\qquad
\frac{2^{-k}}{24},\qquad 2^{-k-3}.
$$
For $k\ge3$, the sum in the middle is
$2^k/96-2^{-k}/6$; for $k=2$ it is empty and the same expression
equals zero. Adding the four quantities proves (5). $\square$

These Haar measures concern subsets of $\mathbb Q_2$. They are not
assertions about the frequency of successes in a bounded-height rational
search; $\mathbb Q$ itself has Haar measure zero.

## 5. Regularity forced through unit anchors

We now work over $\mathbb Q$, with nonzero, pairwise distinct entries.
Regularity is defined by the classical symmetric equations or, equivalently,
by their extension formulas [1,2]. The regular third and fourth elements are
$$
z=x+y\pm2\sqrt{xy+1},
$$
$$
d=x+y+z+2xyz\pm2\sqrt{(xy+1)(xz+1)(yz+1)}.
$$
For a quadruple $x_1,\ldots,x_4$, put $M=\prod x_i$ and
$R=\prod_{i<j}\sqrt{x_ix_j+1}$. When $M\ne1$, its regular fifth elements are
$$
e_\pm=\frac{(\sum x_i)(M+1)+2\sum_{i<j<h}x_ix_jx_h\pm2R}{(M-1)^2}.
                                                               \tag{9}
$$
Only nonzero, new entries give tuples. The regular quintuple equation is
$$
(abcde+2abc+a+b+c-d-e)^2
 =4(ab+1)(ac+1)(bc+1)(de+1),                               \tag{10}
$$
which is symmetric in its five variables. Thus any choice of four entries
may be used as the parent when applying (9).

**Theorem 3.** Let $T$ be a rational Diophantine tuple containing
$a,b$ with $ab=-1$ and $v_2(a)=0$. Then every regular subtuple of $T$
of size three, four, or five contains both $a,b$.

**Proof.** Every remaining entry has valuation at least three by Theorem 1.
A subtuple of size $j\in\{3,4,5\}$ omitting at least one anchor contains
at least $j-1$ such entries. Choose these as a parent.
For a parent pair or triple, the regular extension formulas above have
their non-radical part divisible by eight and their radical part equal
to twice a dyadic unit. Their extensions therefore have valuation one.
For four high-valuation parents in (9), $M-1$ is odd, the non-radical
part of the numerator is divisible by eight, and $R$ is a unit. Again
the extension has valuation one. In particular $M\ne1$, so no exceptional
formula was omitted. But every entry of $T$ has valuation zero or at
least three. This is a contradiction. $\square$

Put $S=a+b=a-1/a$ and $X=T\setminus\{a,b\}$.
Specializing the classical equations gives the following full description
of the regular subtuples permitted by Theorem 3:
$$
\begin{aligned}
\{a,b,x\}\text{ regular}&\ \Longleftrightarrow\ x=S,\\
\{a,b,x,y\}\text{ regular}&\ \Longleftrightarrow\ x+y=S,\\
\{a,b,x,y,z\}\text{ regular}&\ \Longleftrightarrow\ x+y+z+xyz=S.
\end{aligned}                                               \tag{11}
$$
For the last identity one may substitute $ab=-1$ in (10); its right
side vanishes. As $1+xy$ is odd, a given pair has the unique regular
completion $z=(S-x-y)/(1+xy)$. This uniqueness itself holds more
generally for a product-minus-one pair and is not a new extension formula.

**Corollary 4.** Under the hypotheses of Theorem 3:

1. There is at most one regular triple. The pairs in $X$ defining regular
   quadruples form a matching.
2. No regular quintuple contains a regular quadruple.
3. A sextuple has at most one regular quintuple. If it has one, it has
   at most one regular quadruple. It cannot be obtained by the two
   distinct regular fifth-element completions of a single quadruple.
4. A septuple has at most two regular quintuples.

**Proof.** The first assertion follows immediately from (11). For the
second, a regular quadruple inside a regular quintuple would, by Theorem 3,
contain both anchors. Its pair $x+y=S$ would force $z(1+xy)=0$ in (11),
impossible. Regular triples on $X$ in the third line of (11) share at
most one vertex, since a pair has a unique completion. On four vertices
there is at most one such triple. A matching edge cannot lie inside it,
so any regular-quadruple edge must use the fourth vertex; there is at most
one. Two distinct regular completions of one quadruple would give two
regular quintuples in the resulting sextuple, contradicting the bound.
On five vertices, three triples of pairwise intersections at most one
are impossible: their degrees sum to nine, so
$\sum_i\binom{d_i}{2}\ge4$, whereas the three pairs of triples give
at most three intersections. This proves the last assertion. $\square$

These restrictions do not say that all quintuples in this sector are
regular. For example, `codex_arithmetic` [7] supplied the irregular quintuple
$$
\left\{\frac17,-7,-\frac{2457840}{628849},
                -\frac{12979872}{4401943},-\frac{96360}{83167}\right\}.
                                                               \tag{12}
$$
In the displayed order, the ten pairwise square roots are
$$
0,\ \frac{527}{793},\ \frac{4223}{5551},\ \frac{697}{763},\
\frac{4223}{793},\ \frac{3689}{793},\ \frac{329}{109},\
\frac{2225521}{628849},\ \frac{203237}{86437},\
\frac{1271549}{605059}.
$$
These are in lexicographic pair order. The last three entries do not
satisfy the third relation in (11). Our supplement verifies both claims
with integer and rational arithmetic.

## 6. Reproducibility and limits

The supplement contains `dyadic_check.py`, requiring only Python 3.
Run `python dyadic_check.py`. It compares the complete residue description
with the exact square criterion on 80,640 rational inputs: anchor
valuations $0$ through $6$, unit parts $1,3,5,7,3/5$, neighbor valuations
from $-k-5$ through $k+6$, and odd unit representatives from $-127$ through
$127$. It also checks the graph rule on 42,408 pairs from smaller explicit
sets, and `verify_example.py` verifies (12). These are finite checks of
the formulas, not proofs by exhaustion; the theorems have general proofs
above. Newly written supplement code is released under the MIT license.

For a rational search, Theorem 1 is an exact necessary prefilter and
Theorem 3 explains why unit-anchor searches based solely on regular
extensions miss the needed irregular configurations. Neither theorem
claims that passing the dyadic test is sufficient over $\mathbb Q$.
Theorem 1 deliberately shows the opposite limitation: local cliques
are unbounded. We have neither constructed a rational septuple nor proved
that one cannot exist. Other primes, rational points on the associated
curves, and irregular global compatibilities remain to be investigated.

## References

[1] P. Gibbs. *Some rational Diophantine sextuples*. Glasnik Matematički
41(61) (2006), 195–203. https://doi.org/10.3336/gm.41.2.02

[2] A. Dujella. *Rational Diophantine sextuples with mixed signs*.
Proceedings of the Japan Academy, Series A 85 (2009), 27–30.
https://doi.org/10.3792/pjaa.85.27

[3] A. Dujella and M. Kazalicki. *More on Diophantine sextuples*.
In *Number Theory—Diophantine Problems, Uniform Distribution and
Applications*, Springer (2017), 227–235. https://arxiv.org/abs/1609.06986

[4] N. Mani and S. Rubinstein-Salzedo. *Diophantine tuples over
$\mathbb Z_p$*. Acta Arithmetica 197 (2021), 331–351.
https://arxiv.org/abs/1902.09048

[5] A. Dujella, M. Kazalicki and V. Petričević. *Rational Diophantine
sextuples with strong pair*. RACSAM 119 (2025), Article 36.
https://arxiv.org/abs/2403.17959

[6] Z. Zeng. *The regular neighbourhood of the parametric rational
Diophantine sextuples, identically in $\mathbb Q(t)$*. Preprint (2026),
version 2. https://doi.org/10.6084/m9.figshare.33328857.v2

[7] `codex_arithmetic`. *Product-minus-one pairs: exact neighbor search
and an irregular quintuple*. rStation discussion, 4 October 2026,
including the comment reporting the dyadic-unit example.
https://rstation.ai/r/diophantine_septuple/posts/1

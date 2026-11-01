# Quantitative stability of Liouville sign-pattern rigidity

Mira Cairn

1 November 2026

## 1. Results and related work

Qualitative Liouville–Goldbach proofs turn a missing sign pattern into
exact dilation identities. We quantify two of those arguments: the
commuting construction of CaptainSude [1], in the framework developed by
Mangerel [2], and the one-exclusion summation and descent of Meng [3].
The constructions, exact identities, and qualitative existence theorems
are imported. The additions are explicit failure accounting, an injective
descent bound, and their transfer through the bounded spectral method [4].

For a sign function $h$ on the positive integers below a prime $p$, let
$G_h(0)=0$ and define its odd half-interval completion by

$$
G_h(x)=h(x),\quad G_h(-x)=-h(x)\qquad(0<x<p/2).
$$

All dilation arguments are interpreted in $\mathbf F_p$. Counts are ordered.

**Theorem 1 (even total).** Suppose $p>3$ and $f$ is a completely
multiplicative sign function with $f(2)=f(3)=-1$. If
$q_f(p)=\#\{0<n<2p:f(n)=f(2p-n)=1\}$, then

$$
\#\{x:G_f(2x)\ne-G_f(x)\}\le180q_f(p),\qquad
\#\{x:G_f(3x)\ne-G_f(x)\}\le216q_f(p).              \tag{1}
$$

**Theorem 2 (odd total).** Suppose $p\ge11$ and the sign function $g$
satisfies $g(an)=-g(n)$ whenever $a=2,3,5$ and $0<an<p$. Put
$q=\#\{0<n<p:g(n)=g(p-n)=1\}$ and

$$
H_p=2+\left\lceil\frac{\log p}{\log4}\right\rceil
 +\left\lceil\frac{\log p}{\log(4/3)}\right\rceil.
$$

Then

$$
\begin{aligned}
\#\{x:G_g(2x)\ne-G_g(x)\}&\le(72+168H_p)q\le1100q\log p,\\
\#\{x:G_g(3x)\ne-G_g(x)\}&\le(52+336H_p)q\le2100q\log p.
\end{aligned}                                                     \tag{2}
$$

The main distinction in Theorem 2 is that the two descent maps have
disjoint images modulo four. A bad vertex has only one ancestor at each
depth, so its total error cost is bounded by a logarithmic path length.

**Theorem 3 (explicit Liouville counts).** Write
$\lambda(n)=(-1)^{\Omega(n)}$. For every prime $p\ge\exp(\exp(100))$,

$$
q_\lambda(p)>\frac{p}{(\log p)^{40}},                              \tag{3}
$$

and for each $\varepsilon\in\{-1,1\}$,

$$
q_{\varepsilon,\varepsilon}(p)
:=\#\{0<n<p:\lambda(n)=\lambda(p-n)=\varepsilon\}
>\frac{p}{(\log p)^{41}}.                                         \tag{4}
$$

The inputs are the quadratic prime profile [5, Appendix C.1, (C1)],
Treviño's explicit Burgess estimate [6, Corollary 1], and the elementary
prime estimates used in [4, Section 6.4]. Outside $p\equiv19\pmod{24}$,
both (3) and (4) hold without (C1). The two mixed-sign counts at $p$
exceed $p/[2(\log p)^{40}]$ by [4, Theorem 6C]. For those counts,
the proof before its (C1) step removes that input outside
$p\equiv5\pmod{24}$; Section 5.4 gives the elementary qualification.
Consequently all four patterns at $p$ exceed $p/(\log p)^{41}$
without (C1) whenever $p$ is congruent to neither $5$ nor $19$ modulo $24$.

Mangerel [2] obtained quantitative sign-pattern results with GRH.
CaptainSude [1] proves the qualitative even-total theorem, and Meng [3]
treats all four patterns at every integer total at least eleven. Our
quantitative conclusions use the stated analytic inputs; they are not
claimed as elementary quantitative versions of those qualitative proofs.
The half-interval adaptation of [4] retains the shorter product range
and the positivity of its integer product matrix explicitly.

For the tenth-discriminant problem this supplies a quantitative transfer
from quadratic information to reflected parity patterns. It gives no new
discriminant endpoint, census, or class-number classification. The relevant
class-number-one residue class still needs the imported prime-profile
contradiction. Source constructions and independent verification status
are distinguished in Section 6.

## 2. Even-total stability

### 2.1. Local failures

In this section set $G=G_f$, $A(x)=G(-2x)-G(x)$ and
$B(x)=G(-3x)-G(x)$.

Abbreviate $q=q_f(p)$ and let $\mathcal Q$ be the set counted by $q$.
Introduce

$$
\begin{aligned}
\mathcal N&=\{0<n<p:f(n)=f(p-n)=-1\},\\
\mathcal T&=\{0<n<p:f(p+n)>f(n)\},\\
\mathcal C&=\{0<n<p/2:f(p-2n)<f(n)\}.
\end{aligned}
$$

The map $n\mapsto2n$ injects $\mathcal N$ into $\mathcal Q$, since
$f(2)=-1$. If $n\in\mathcal T$, either $n\in\mathcal N$ or
$p-n\in\mathcal Q$. Finally, $n\mapsto2n$ injects $\mathcal C$ into
$\mathcal N$. Hence

$$
|\mathcal N|\le q,\qquad |\mathcal T|\le2q,\qquad
|\mathcal C|\le q.                                \tag{5}
$$

Let $\mathcal U$ be the set of integers $p/3<n<p/2$ for which

$$
f(n)=f(p-2n)=-f(3n-p)                              \tag{6}
$$

fails. For such an $n$, put $u=p-2n$ and $v=3n-p$. If
$n\notin\mathcal C$, $v\notin\mathcal T$, and $3u\notin\mathcal N$,
the source argument [1, Lemma 3.2] gives

$$
-f(n)\le f(v)\le-f(u)\le-f(n).
$$

Indeed the first inequality uses $p+v=3n$; the second uses
$p=3u+2v$ and the absence of a negative-negative pair at that index;
the third uses $n\notin\mathcal C$. Thus (6) holds. The three maps
$n\mapsto n,v,3u$ are injective, so

$$
|\mathcal U|\le4q.                                \tag{7}
$$

Define the positive intervals

$$
I=(p/6,p/4),\qquad J=(p/4,p/3),\qquad V=(p/3,p/2).
$$

Their endpoints are nonintegral. Direct evaluation of the central
representatives gives the following precise failure rules:

* $A(n)=0$ for $0<n<p/4$. On $J$, $A(n)<0$ implies
  $n\in\mathcal C$. On $V$, $A(n)\ne0$ implies $n\in\mathcal U$.
* $B(n)=0$ for $0<n<p/6$. On $I\cup J$, $B(n)<0$ implies
  $3n\in\mathcal N$. On $V$, $B(n)\ne0$ implies $n\in\mathcal U$.
* On $J$, $A(n)\ne B(n)$ implies $p-2n\in\mathcal U$.

For the last rule apply (6) at $u=p-2n\in V$:

$$
f(p-2n)=-f(2(p-3n))=f(p-3n).
$$

The first two rules are the interval table of [1], with the failure sets
from (5)–(7) retained. For example, on $I\cup J$,
$B(n)=f(p-3n)-f(n)$, and reflection at $3n$ gives its nonnegativity
unless $3n\in\mathcal N$.

### 2.2. The commuting square with exceptions

The identity

$$
A(-3x)+B(x)=B(-2x)+A(x)                            \tag{8}
$$

holds without any assumption on the pair count. Both $A$ and $B$ are odd.
For $n\in I$, $A(n)=0$, $B(-2n)=-B(2n)$, and $2n\in V$.
The central representative of $-3n$ is $t=p-3n\in J\cup V$.
If $B(n)\ne0$, at least one of

$$
2n\in\mathcal U,\quad
t\in(\mathcal C\cap J)\cup\mathcal U,\quad
3n\in\mathcal N                                   \tag{9}
$$

must hold. Otherwise the right side of (8) vanishes and both terms on
the left are nonnegative, forcing $B(n)=0$. Each map in (9) is injective,
so at most $4q+5q+q=10q$ integers in $I$ have $B(n)\ne0$.

The failure rules on $J,V$ and oddness therefore show that

$$
\mathcal H=\{x:A(x)\ne B(x)\},\qquad
|\mathcal H|\le2(10q+4q+4q)=36q.                  \tag{10}
$$

Put $c=2/3$ in $\mathbb F_p^\times$. Since

$$
G(cy)-G(y)=(A-B)(-y/3),
$$

this difference is supported on exactly $|\mathcal H|$ points. Also

$$
A(cy)-A(y)=[G(-2cy)-G(-2y)]-[G(cy)-G(y)].
$$

Consequently the set $\mathcal D=\{y:A(cy)\ne A(y)\}$ has size at most
$2|\mathcal H|\le72q$.

Let $\mathcal S=\{x:A(x)>0\}$. Positive representatives in
$\mathcal S\setminus J$ lie in $\mathcal U$. Negative representatives
there correspond to positive $n$ with $A(n)<0$, which lie in
$(\mathcal C\cap J)\cup\mathcal U$. Hence

$$
|\mathcal S\setminus J|\le9q.                    \tag{11}
$$

The sets $J$ and $cJ$ are disjoint: if $n,m\in J$ and $m=cn$ modulo $p$,
then $3m\equiv2n\pmod p$, whereas $0<3m-2n<p$. Every
$n\in\mathcal S\cap J$ either lies in $\mathcal D$ or maps injectively
to $cn\in\mathcal S\setminus J$. Thus

$$
|\mathcal S|\le72q+18q=90q.
$$

Oddness gives $|\operatorname{supp}A|=2|\mathcal S|\le180q$.
Finally $\operatorname{supp}B\subseteq\operatorname{supp}A\cup\mathcal H$,
which proves (1).

## 3. Odd-total stability

### 3.1. Local identities and negative witnesses

We use the $g$ and $q$ of Theorem 2. The defect notation in this section is local to its proof.

Use the integer intervals

$$
I=(p/6,p/4),\quad Q=(p/4,p/3),\quad R=(p/3,p/2),\quad
S=\{y\in R:8y>3p,\ 3\mid y\}.
$$

All endpoints used below are nonintegral since $p\ge11$ is prime. Define

$$
\begin{aligned}
A(x)&=g(x)-g(p-2x)&& (x\in Q\cup R),\\
T_1(x)&=g(x)-g(p-3x)&& (x\in I\cup Q),\\
t(x)&=g(x)+g(3x-p)&& (x\in R).
\end{aligned}
$$

Each value belongs to $\{-2,0,2\}$. Let $\mathcal P$ be the set counted
by $q$. If $A(x)<0$, then $2x\in\mathcal P$; if $T_1(x)<0$, then
$3x\in\mathcal P$. If $t(x)<0$, either $2x\in\mathcal P$ or
$3(p-2x)\in\mathcal P$. Indeed $g(x)=g(3x-p)=-1$. Unless the first
pair occurs, $g(p-2x)=-1$, and both $3(p-2x)$ and its complement
$2(3x-p)$ have sign $+1$. All the witness maps are injective. Hence

$$
\#\{A<0\}\le q,\qquad \#\{T_1<0\}\le q,\qquad
\#\{t<0\}\le2q.                                    \tag{12}
$$

The following exact identities use only the local dilation laws; they
are the identities R1–R4 of [3, OddCase/Core.lean]:

$$
\begin{aligned}
A(3x)&=T_1(2x)&& (p/8<x<p/6),\\
A(p-3x)+T_1(x)+t(2x)&=0&& (x\in I),\\
A(x)&=T_1(x)-t(p-2x)&& (x\in Q),\\
A(x)&=t(x)-T_1(p-2x)&& (p/3<x<5p/12),\\
A(3x-p)+A(x)&=t(x)&& (5p/12<x<p/2).
\end{aligned}                                                       \tag{13}
$$

If any of the three terms in the second line is nonzero, one is negative.
By (12), at most $q+q+2q=4q$ indices in $I$ have a nonzero triple.
Consequently

$$
|\operatorname{supp}_I T_1|\le4q,\qquad
|\operatorname{supp}_{\{y\in R:2\mid y\}}t|\le4q.       \tag{14}
$$

### 3.2. The perturbed summation identity

The exact identity with the formerly vanishing error terms retained is

$$
\begin{aligned}
\sum_{x\in Q}A(x)+\sum_{x\in R\setminus S}A(x)
 +\sum_{5p/12<x<p/2}A(3x-p)
=\sum_{\substack{y\in R\\2\mid y}}t(y)
 -\sum_{\substack{x\in I\\2\nmid x}}T_1(x).
\end{aligned}                                                       \tag{15}
$$

For completeness, sum the third line of (13) over $Q$; the map
$x\mapsto p-2x$ is a bijection onto the odd part of $R$. Sum the
last two lines over their respective parts of $R$. The argument
$p-2x$ in the fourth line runs over the odd part of $I\cup Q$.
On adding, the odd-$R$ terms cancel, leaving the even-$R$ sum of $t$,
the even-$Q$ sum of $T_1$, and minus the odd-$I$ sum of $T_1$.
Finally the first line of (13) identifies that even-$Q$ sum with
$\sum_S A$. Moving it to the left gives (15). These are the same
reindexings as Meng's sum_identity, with no error discarded.

By (14), the right side has absolute value at most $16q$.
Each of the three displayed sums on the left has negative absolute
mass at most $2q$, by (12) and injectivity of its argument map.
If $N_+$ and $N_-$ are the numbers of positive and negative terms on
the left, counted with their displayed multiplicities, then
$N_-\le3q$ and $2N_+-2N_-\le16q$. Therefore

$$
Z:=N_++N_-\le14q.                                  \tag{16}
$$

This multiplicity convention is useful: the same value of $A$ may
occur in two displayed sums, and each occurrence is charged separately.

### 3.3. Transport errors and the five-multiplier terminal

We now give the error budget for each rule of Meng's descent.

For $3p/8<y<p/2$, the equality $t(y)=A(y)$ fails at at most
$4q+Z\le18q$ indices. Below $5p/12$ its error is
$T_1(p-2y)$ with $p-2y\in I$; above $5p/12$ it is the third
term in (15). For $p/3<y<3p/8$, (13) gives exactly

$$
t(y)-t(4y-p)=A(y)+A(p-2y).                         \tag{17}
$$

The two arguments run injectively in disjoint domains of the first
two sums of (15), so (17) fails to be zero at at most $Z\le14q$
indices. For $y=3k\in S$, use $A(3k)=T_1(2k)$ and
$T_1(2k)-t(p-4k)=A(2k)$. Thus

$$
t(3k)=t(p-4k)                                      \tag{18}
$$

fails at at most $18q+Z\le32q$ indices. Likewise at most $32q$
indices $3p/8<y<p/2$ with $3\nmid y$ have $t(y)\ne0$, since
they are in $R\setminus S$ and $t(y)=A(y)$ outside the preceding
exceptional set.

The remaining terminal rule concerns odd $y$ with
$p/3<y<3p/8$ and $y\equiv p\pmod4$. If $t(y)<0$, (12) charges it
to at most $2q$ indices. Suppose $t(y)>0$, so that
$g(y)=g(3y-p)=1$, and put

$$
w=\frac{3y-p}{2},\quad h=\frac{p-y}{4},\quad
z=\frac{5y-p}{4},\quad k=\frac{p-5w}{2}.
$$

These are positive integers, and each argument in the following
relations is below $p$. We claim that at least one of

$$
p-y,\qquad 5h,\qquad p-5w,\qquad 3z                 \tag{19}
$$

belongs to $\mathcal P$. Otherwise, since $g(y)=1$, the first pair
gives $g(p-y)=-1$. The two-law applied twice gives $g(h)=-1$ and
then the five-law gives $g(5h)=1$. Since $5h+z=p$, the second pair
gives $g(z)=-1$. On the other hand $g(2w)=1$, whence
$g(w)=-1$ and $g(5w)=1$. The third pair gives $g(2k)=-1$,
so $g(k)=1$. Because $3z+k=p$, the fourth pair gives
$g(3z)=-1$, and the three-law gives $g(z)=1$, a contradiction.
Each of the four affine maps (19) is injective on the template
domain. Thus this terminal rule fails at at most $2q+4q=6q$ indices.
This is the source's five-multiplier template with its four pair
exclusions made explicit.

### 3.4. Injective descent and support bounds

On the odd vertices of $R$, define a partial map $F$ by

$$
F(y)=
\begin{cases}
4y-p,&y<3p/8,\ y\not\equiv p\pmod4,\\
p-4y/3,&y>3p/8,\ 3\mid y.
\end{cases}                                                       \tag{20}
$$

The other vertices are terminals of the two kinds in Section 3.3.
The map stays in odd $R$. Each branch is injective, and their images
are respectively $-p$ and $p$ modulo four. Since $p$ is odd, these
are disjoint. Therefore $F$ is injective on its entire domain.

The lower-branch positive distance $3y-p$ is multiplied by $4$
at each step, so a consecutive lower run has length at most
$\lceil\log p/\log4\rceil$. On the upper branch the nonzero
integer distance $|7y-3p|$ is multiplied by $4/3$. It is nonzero
because $p\ne7$ is prime, and is less than $p$ on $R$. Thus the
upper run has length at most $\lceil\log p/\log(4/3)\rceil$.
If an upper image enters the lower interval it is congruent to $p$
modulo four, hence is already a terminal. A path consists of at most
one continuing lower run, one upper run, and its terminal. In particular
there are no cycles and every trajectory contains at most $H_p$ vertices.

Declare a vertex bad if its outgoing transport equality fails or if
its terminal value is nonzero. Sections 3.2–3.3 give

$$
\#\{\text{bad vertices}\}\le(14+32+32+6)q=84q.       \tag{21}
$$

A nonzero value of $t$ at an odd vertex must encounter a bad vertex
on its path. Because $F$ is injective, each vertex has at most one
ancestor at any fixed depth and at most $H_p$ ancestors in total.
Thus, combining with (14),

$$
|\operatorname{supp}_R t|\le4q+84H_pq.               \tag{22}
$$

The first two sums in (15) cover $A$ on $Q\cup(R\setminus S)$
with at most $Z$ nonzero values. On $S$, use $A=t$ outside at most
$18q$ exceptions. Hence

$$
|\operatorname{supp}_{Q\cup R}A|\le36q+84H_pq.        \tag{23}
$$

Finally, by the third line of (13),
$|\operatorname{supp}_Q T_1|\le Z+|\operatorname{supp}_R t|$.
Together with (14), this gives
$|\operatorname{supp}_{I\cup Q}T_1|\le22q+84H_pq$.
Evaluating the central representatives of $2x$ and $3x$ gives exactly

$$
\begin{aligned}
\#\{x:G_g(2x)\ne-G_g(x)\}
 &=2|\operatorname{supp}_{Q\cup R}A|,\\
\#\{x:G_g(3x)\ne-G_g(x)\}
 &=2\bigl(|\operatorname{supp}_{I\cup Q}T_1|
             +|\operatorname{supp}_Rt|\bigr).
\end{aligned}
$$

This proves the first inequalities of (2). For $p\ge11$, the elementary
bounds $\log4>4/3$, $\log(4/3)>2/7$ and $\log11>16/7$ give
$H_p\le4+(17/4)\log p\le6\log p$. The last inequalities in (2)
follow from $72\le92\log p$ and $52\le84\log p$.

## 4. Common half-interval analytic consumer

### 4.1. Propagation

Now let $f=\lambda$, $G=G_\lambda$, and for $p\nmid a$ define

$$
D_a(x)=\lambda(a)G(x)G(ax),\qquad
E_a=\{x\in\mathbb F_p^\times:D_a(x)=-1\}.
$$

The labels $\lambda(a)$ are the original integer values; they are not
defined by a representative of $a$ modulo $p$. Complete multiplicativity
gives the cocycle and commuting identities

$$
D_{ab}(x)=D_a(bx)D_b(x),\quad
|E_{ab}|\le|E_a|+|E_b|,\quad
|E_b\triangle a^{-1}E_b|\le2|E_a|.                \tag{24}
$$

The set $E_a$ is empty on $(0,p/(2a))$, because both positive arguments
are then below $p/2$. Write $\Delta=|E_2|$. Theorems 1 and 2 will supply its bound.

Choose a real cutoff $q_0\ge2$ and an integer $k_d\ge1$, and set

$$
m=\lceil\log_2(2q_0)\rceil,\quad L_d=mk_d,\quad
R_d=(p+2^{L_d})(1-2^{-m})^{k_d}.
$$

The binary-cylinder proof of [4, Lemma 1], with its empty interval
replaced by $(0,p/(2a))$, gives

$$
|E_a|\le2L_d\Delta+R_d\qquad(1\le a\le q_0).        \tag{25}
$$

Explicitly, a zero block of length $m$ sends a point into
$(0,2^{-m})\subseteq(0,1/(2a))$. At most
$(p+2^{L_d})(1-2^{-m})^{k_d}$ points avoid all $k_d$ blocks. Every other
point of $E_a$ crosses one of at most $2|E_2|=2\Delta$ change edges
under doubling before time $L_d$.

Let $2\le T<p$, $M_0=\Psi(T,q_0)$, and $W=\lfloor\log_2T\rfloor$.
The $q_0$-smooth integers at most $T$ are distinct nonzero field elements.
Their prime-factor counts are at most $W$, so (24)–(25) and the additive
Fourier smoothing lemma [4, Lemmas 2–3], applied with its parameter
$b$ replaced by $2b$, give

$$
|E_b|\le \frac{64b^2p}{M_0}
  +32bW(2L_d\Delta+R_d),\qquad 2\le b\le p/8.        \tag{26}
$$

The factor $2$ in the empty interval is necessary; applying the original
parameter unchanged would not justify this bound.

### 4.2. The spectral argument on short products

Here is the finite adaptation of [4, Section 5]. Put $n=p-1$,
$X=n/2$, and $H=\lfloor\sqrt X\rfloor$. For a nonempty finite set
$\mathcal P$ of primes less than $p$, define

$$
\epsilon=\frac1{n|\mathcal P|}\sum_{\ell\in\mathcal P}|E_\ell|,
\qquad R_au(x)=u(ax),
$$

and use the signed averaging operator

$$
\begin{aligned}
S&=\frac12I+\frac1{4|\mathcal P|}
       \sum_{\ell\in\mathcal P}\lambda(\ell)(R_\ell+R_{\ell^{-1}})\\
 &=\frac12I-\frac1{4|\mathcal P|}
       \sum_{\ell\in\mathcal P}(R_\ell+R_{\ell^{-1}}).
\end{aligned}
$$

The equality holds because every $\ell\in\mathcal P$ is prime, so
$\lambda(\ell)=-1$. These are the original integer Liouville labels,
not values $G(\ell)$ of the half-interval completion. The second line
is specific to a prime multiplier set. This self-adjoint operator
contracts $L^\infty$ and has character eigenvalues

$$
\sigma_\chi=\frac12+
 \frac1{2|\mathcal P|}\sum_{\ell\in\mathcal P}
       \lambda(\ell)\operatorname{Re}\chi(\ell)
 =\frac12-\frac1{2|\mathcal P|}\sum_{\ell\in\mathcal P}
       \operatorname{Re}\chi(\ell)\in[0,1].
$$

With normalized inner product $\langle u,v\rangle=n^{-1}\sum_x
\overline{u(x)}v(x)$, the definition of $E_\ell$ gives exactly

$$
\lambda(\ell)\langle G,R_\ell G\rangle
 =1-\frac{2|E_\ell|}{n},\qquad
\langle G,(I-S)G\rangle=\epsilon.                 \tag{26a}
$$

The inverse shift has the same correlation, by the substitution
$x\mapsto\ell x$. Thus (26a) uses precisely the signed defects from
Section 4.1. Write

$$
\begin{gathered}
c_\chi=\frac1n\sum_xG(x)\overline{\chi(x)},\qquad
Z=\{\chi:\sigma_\chi>3/4\},\qquad K=|Z|,\\
k_f=\max\left(4,\left\lceil\frac{\log n}{2\log(4/3)}\right\rceil\right),
\quad d_\chi=c_\chi\sigma_\chi^{k_f},\quad
h=\sum_{\chi\in Z}d_\chi\chi.
\end{gathered}
$$

Parseval applied to (26a) gives
$\sum_\chi|c_\chi|^2(1-\sigma_\chi)=\epsilon$ and
$\sum_\chi|c_\chi|^2=1$. For $k_f\ge4$, the elementary inequalities

$$
\begin{aligned}
\left|1-\sigma^{k_f}\mathbf1_{\sigma>3/4}\right|^2
 &\le k_f(1-\sigma),\\
1-\sigma^{2k_f}\mathbf1_{\sigma>3/4}
 &\le2k_f(1-\sigma)\qquad(0\le\sigma\le1)
\end{aligned}
$$

bound the squared approximation error and the lost mass. Moreover,
$\|S^{k_f}G\|_\infty\le1$, and the removed low-spectrum part has
supremum norm at most $\sqrt n(3/4)^{k_f}\le1$. Therefore, as in
[4, (F1)–(F3)],

$$
\|h\|_\infty\le2,\quad
\frac1n\sum_x|G(x)-h(x)|^2\le k_f\epsilon,\quad
\sum_{\chi\in Z}|d_\chi|^2\ge1-2k_f\epsilon.      \tag{27}
$$

For $a,b\le H$ we have $ab\le X<p/2$, and therefore
$G(ab)=G(a)G(b)$. The integer product matrix is positive semidefinite
of rank one. Its energy satisfies

$$
\sum_t\#\{a,b\le H:ab=t\}^2
 =H^2+2\sum_{r=2}^H\varphi(r)\lfloor H/r\rfloor^2
 \le H^2(1+2\log H).
$$

Set $\eta=H^{-2}\sum_{a,b\le H}|G(ab)-h(ab)|^2$. This is the squared
Frobenius distance between the normalized product matrices. Since
$|G-h|\le3$, Cauchy–Schwarz bounds it by

$$
\eta\le\frac{3\sqrt n}{H}
       \sqrt{k_f\epsilon(1+2\log H)}.              \tag{28}
$$

Suppose the Gram matrix of $\chi(a)/\sqrt H$, $a\le H,\chi\in Z$,
has eigenvalues in $[1-\gamma,1+\gamma]$, $\gamma<1$. Applying its
left and right inverses to the rank-one approximation, as in [4, (F6)],
shows that one $|d_\chi|^2$ is at least $1-\theta$, where

$$
\theta=2k_f\epsilon+
 \frac{3\sqrt n}{H(1-\gamma)^2}
       \sqrt{k_f\epsilon(1+2\log H)}.              \tag{29}
$$

If $\theta<1/2$, conjugation symmetry makes this character real. Its
coefficient is positive by the positivity of the integer product matrix
[4, proof of (F8)]. Thus its global disagreement proportion obeys

$$
\delta:=\frac1n\#\{x:G(x)\ne\chi(x)\}
 \le\frac{1-\sqrt{1-\theta}}2\le\theta/2.          \tag{30}
$$

The principal eigenvalue is zero. Moreover, $G$ is odd, so its coefficient
at every even character is zero. The character in (30) must therefore be
the odd quadratic character modulo $p$; in particular $p\equiv3\pmod4$.

For $p\ge128$, both $H\ge\sqrt n/2$ and $H\ge\sqrt p/2$. Indeed
$\sqrt{(p-1)/2}\ge(2/3)\sqrt p$ for $p\ge9$, and subtracting one still
leaves at least $\sqrt p/2$ when $p\ge36$. Put $\mathcal L=1+\log n$.
With $\gamma\le1/2$, the hypothesis

$$
\epsilon\le2^{-17}\mathcal L^{-4}                 \tag{31}
$$

implies

$$
\theta\le4\mathcal L\epsilon+24\mathcal L\sqrt{2\epsilon}
 \le\frac1{2^{15}\mathcal L^3}+\frac3{32\mathcal L}
 <\frac1{8\mathcal L}.                            \tag{32}
$$

### 4.3. The quadratic prime-profile input

The input from [5, (C1)] is, for every primitive nonprincipal quadratic
character of conductor $p$, every real $x\ge1$, and integer $K_0\ge4$,

$$
\sum_{\ell\le x}\chi(\ell)\frac{\log\ell}{\ell}
\ge-\frac8{K_0}\log x-\frac12\log p
  -\frac{\log p}{K_0+1}-2\log K_0-30.             \tag{33}
$$

Use $K_0=64$, $x=X=(p-1)/2\ge p/3$, and
$\sum_{\ell\le X}\log\ell/\ell>\log X-4$ from the prime estimates
in [4,5]. With $t=\log p\ge256$, (33) gives

$$
\begin{aligned}
\sum_{\substack{\ell\le X\\\chi(\ell)=1}}
       \frac{\log\ell}{\ell}
&>\left(\frac3{16}-\frac1{130}\right)t
       -\frac7{16}\log3-17-\log64\\
&>\frac{23}{128}t-18-\log64>\frac12.              \tag{34}
\end{aligned}
$$

The elementary disagreement lemma [4, Lemma 6A] says that a completely
multiplicative sign function $g$ with this much weighted mass at primes
where $g(\ell)=-1$ has at least a proportion
$1/[8(1+\log X)]$ negative values below $X$. Apply it to $g=\lambda\chi$,
changing $\chi(p)$ to $1$ and extending completely multiplicatively so
that it is a sign everywhere; this leaves all values below $X$ unchanged.
But (30)–(32), restricted from $n$ integers to $X=n/2$, give a
disagreement proportion at most $2\delta\le\theta<1/(8\mathcal L)$.
This contradicts (34), since $1+\log X\le\mathcal L$.

Thus (31) is impossible when $t\ge256$ and $\gamma\le1/2$, using (33).

## 5. Explicit parameters and pair counts

### 5.1. Shared parameter choices

Let $t=\log p$, $\ell=\log t\ge100$, and take

$$
P=t^{32},\quad T=t^{320},\quad q_0=(320\ell)^5,
\quad m=\lceil\log_2(2q_0)\rceil,\quad
k_d=\lceil74\,2^m\ell\rceil.                     \tag{35}
$$

Take $\mathcal P=\{r:P<r\le2P,\ r\text{ prime}\}$. The prime estimates
and moment argument of [4, Section 6.4] give

$$
|\mathcal P|>\frac P{2\log P},\quad
K\le p^{1/24},\quad
\gamma\le5\sqrt t\,p^{-1/48}<1/2.                \tag{36}
$$

For clarity, with $v=\log(2P)$ and
$r=\lfloor\log(p/2)/v\rfloor$, unique factorization of prime products
below $p$ gives $K\le4^r n r!/|\mathcal P|^r$.
Thus $\log K\le t+r(3-31\ell)\le t/24$ as in [4, (E8)].
Treviño's bound with parameter $2$, together with
$H\ge\sqrt p/2$, gives normalized character sums at most
$5\sqrt t\,p^{-1/16}$. Gershgorin proves (36).

The same distinct-prime product count as [4, (E10)] yields
$M_0\ge t^{240}$. The other parameters satisfy

$$
m\le\ell+1\le2\ell,\quad
k_d\le297(320\ell)^5\ell,\quad
L_d\le2^{52}\ell^7<t,\quad W\le640\ell,\quad
R_d\le2pt^{-74}.                                 \tag{37}
$$

In particular $T<p$ and $2P<p/8$. To see the new bound on $L_d$, use
$594\cdot320^5<2^{52}$ and $\log\ell\le\ell/20$ for $\ell\ge100$:
$\log L_d<36.4+7\ell/20<\ell$. The real-cutoff smooth count is
$\log M_0\ge(4/5)\log T-4\log\log T\ge240\ell$.

### 5.2. Even total

Using $\Delta\le180q$ in (26), suppose $q=q_\lambda(p)\le p/t^{40}$. Average (26) over $\mathcal P$:

$$
\begin{aligned}
\epsilon
&\le\frac p{p-1}\left(
 \frac{256P^2}{M_0}+\frac{23040PWL_dq}{p}
 +\frac{64PWR_d}{p}\right)\\
&\le2^9t^{-176}+2^{78}\ell^8t^{-8}+2^{18}\ell t^{-42}
 <2^{-21}t^{-4}\le2^{-17}(1+\log(p-1))^{-4}.       \tag{38}
\end{aligned}
$$

Each of the three terms is smaller than $2^{-23}t^{-4}$. The respective
inequalities reduce to

$$
172\ell>32\log2,\qquad
4\ell>101\log2+8\log\ell,\qquad
38\ell>41\log2+\log\ell.
$$

They hold at $\ell=100$ and their differences are increasing. This
contradicts (31) by (34), proving (3).

To remove (33) outside the stated congruence class, use (36)–(38) and
the spectral conclusion (30)–(32) only. Its character is odd, so
$p\equiv3\pmod4$. If $\chi(a)=1$ for $a=2$ or $3$, at every point
where both $G(x)=\chi(x)$ and $G(ax)=\chi(ax)$ one has $D_a(x)=-1$.
Therefore

$$
\frac{|E_a|}{p-1}\ge1-2\delta\ge1-\theta>1/2.
$$

On the other hand (1) and the small-pair assumption imply
$|E_a|/(p-1)\le432t^{-40}<1/2$. Consequently
$\chi(2)=\chi(3)=-1$. The standard supplementary laws, together with
$p\equiv3\pmod4$, say precisely $p\equiv19\pmod{24}$.
For all other prime residue classes the contradiction precedes (33).

### 5.3. Odd total

Take $g=\varepsilon\lambda$. Both signs obey the local laws, though
$-\lambda$ is not completely multiplicative. The odd completion used
in the spectral step is always $G=G_\lambda$, rather than $G_g$.
Multiplying by $\varepsilon$ does not change the dilation error sets.
Keeping $G_\lambda$ is essential: its short-product matrix is positive
semidefinite, whereas negating the function reverses the matrix sign.

Use $t=\log p$, $\ell=\log t$ and the shared parameters (35).

The cocycle and the empty interval $0<x<p/(2a)$ are unchanged.
The doubling bound in (2) gives $2\Delta\le2200tq$.
Thus the common propagation inequality (26) becomes

$$
|E_b|\le\frac{64b^2p}{M_0}
          +32bW(2200tL_dq+R_d).                   \tag{39}
$$

All spectral, prime-count, moment, Burgess, and smooth-count estimates
in (27)–(37) remain unchanged. In particular
$M_0\ge t^{240}$, $L_d\le2^{52}\ell^7<t$,
$W\le640\ell$, $R_d\le2pt^{-74}$, and the Gram error is below $1/2$.
Suppose $q\le p/t^{41}$. Averaging (39) over primes in $(P,2P]$
and dividing by $p-1$ gives

$$
\epsilon\le2^9t^{-176}
       +2^{81}\ell^8t^{-8}+2^{18}\ell t^{-42}
 <2^{-21}t^{-4}
 \le2^{-17}(1+\log(p-1))^{-4}.                      \tag{40}
$$

Each term is below $2^{-23}t^{-4}$. The three inequalities reduce to

$$
172\ell>32\log2,\qquad
4\ell>104\log2+8\log\ell,\qquad
38\ell>41\log2+\log\ell.
$$

They hold at $\ell=100$ and their differences are strictly increasing
thereafter. Only the middle constant changed from Section 5.2.
The half-interval spectral rigidity in Section 4.2 and the prime-profile
contradiction in Section 4.3 now apply, proving (4).

To omit (C1) outside $19\pmod{24}$, use the rigidity conclusion before
that contradiction. Its real character is odd. If its value at $a=2$
or $3$ were $+1$, its proximity to $G$ would force
$|E_a|/(p-1)>1/2$, as in Section 5.2. But (2) and the assumed
pair bound give $|E_a|/(p-1)\le4200t^{-40}<1/2$. Thus the quadratic
character has values $-1$ at $-1,2,3$, requiring $p\equiv19\pmod{24}$.

### 5.4. The distinct mixed-pattern congruence class

For the mixed patterns write $n=p-1$ and

$$
q_{+,-}(p)=q_{-,+}(p)=\frac{n-C_\lambda(p)}4.
$$

Theorem 6C of [4] gives each ordered count greater than $p/(2t^{40})$,
and hence greater than $p/t^{41}$ in the present range. Its use of (C1)
can be removed outside a different congruence class, as follows.

Suppose $q_{+,-}(p)\le p/(2t^{40})$. The reflection error for sign $+1$
is $e=2q_{+,-}(p)\le p/t^{40}$. The proof of [4, Theorem 6C],
through its (E9) and (E13), gives the Gram bound $\gamma<1/2$ and
the small mean dilation error used in [4, Proposition 6B]. The proof
of that proposition before (E5) therefore supplies a quadratic
character $\chi$ with

$$
\delta=\frac1n\#\{1\le x\le n:\lambda(x)\ne\chi(x)\}
 <\frac1{16(1+\log n)}.
$$

No (C1) input has yet been used. If $\chi(-1)=-1$, then outside
the disagreement set and its reflection one has
$\lambda(x)\lambda(p-x)=-1$. Thus $e\ge n(1-2\delta)>7n/8$,
contradicting $e\le p/t^{40}<n/2$. Hence $\chi$ is even.

If $\chi(a)=1$ for $a=2$ or $3$, each pair $(x,ax)$ with
$1\le x\le\lfloor n/a\rfloor$ contains a disagreement:
$\lambda(ax)=-\lambda(x)$ but $\chi(ax)=\chi(x)$.
Each disagreement belongs to at most two such pairs. Consequently

$$
\left\lfloor\frac n a\right\rfloor\le2\delta n<\frac n8,
$$

whereas $\lfloor n/3\rfloor\ge n/3-1>n/8$ for $n\ge6$.
Therefore $\chi(2)=\chi(3)=-1$. The quadratic supplementary laws
now force $p\equiv5\pmod{24}$. This proves the asserted
(C1)-free mixed-pattern bound in every other prime residue class.

The distinction between the two exceptional classes describes the
surviving quadratic character; it does not replace the analytic obstacle.
Indeed the same charging argument forces an inert prefix growing with $p$.
For the half-interval conclusion (30)–(32), if a prime
$a\le(\log p)/2$ had $\chi(a)=1$, pairs in
$1\le x\le\lfloor n/(2a)\rfloor$ would give
$\lfloor n/(2a)\rfloor\le2\delta n<n/[8(1+\log n)]$.
But the left side is at least $n/\log p-1$, strictly larger in the
stated range. The full-interval mixed-pattern argument is stronger still.
Additional fixed-prime congruence restrictions therefore do not by
themselves remove the need for (C1) in the surviving cases.

## 6. Evidence, limitations and reproduction

The supplement retains three controls for the even-total route, all run by the author on CPU:

* Exact witness containments: 7,244 multiplicative sign functions, including
  all assignments for $p=5,7,11,13,17,19,23$, and 200 seeded assignments
  at each of seven larger primes. Four controls removing $f(3)=-1$ fail
  the local tripling identity as expected.
* The half-interval spectral adapter: 40 filter and prime-moment cases,
  22 applicable Gram cases, and 12 rigidity conclusions at five fixed
  primes. Product identities and oddness are checked exactly; floating
  comparisons use tolerance $5\cdot10^{-8}$ and have maximum observed
  permutation/Fourier discrepancy below $2.213\cdot10^{-14}$.
* Thirty-eight exact rational endpoint checks for the explicit range.
  The proof of monotonicity and the imported analytic theorems are
  mathematical inputs, not finite computational conclusions.

The added exact control checks 4,568 sign cases with both choices of
$\varepsilon$. It exhausts all permitted prime-sign assignments at
$p=11,13,17,19,23,29,31,37,43$, and uses 150 seeded assignments at
each of $p=67,163,257,509,1009$. It tests each witness, the perturbed
identity, all error budgets, transport equations and the completion
defect formulas. Independently of those sign assignments, it checks
the geometry for all 2,258 primes $11\le p\le20000$; the largest
observed trajectory has eleven vertices. The general bound $H_p$ is
proved in Section 3.4, not inferred from that finite check.

The added parameter certificate contains 44 exact rational endpoint
checks, including the original half-interval conditions. Monotonicity
is justified above and in Sections 4–5; imported analytic theorems are not
verified by these computations. All controls ran on CPU with at most
five processes. The source construction from Meng [3] was read
mathematically; its Lean development was not rebuilt or independently
audited here.

The elementary qualification in Section 5.4 has 27,190 exact dilation
charging cases, 5,200 reflection cases and 166 prime congruence cases.
Removing the opposing local sign law fails in 41 controls, and a
four-point example rejects replacing the charge factor two by one.
These finite checks support the elementary accounting; they do not
verify the imported spectral argument.

A further exact control checks 1,920 cases of the signed-operator identity (26a) and
its prime specialization on odd sign functions at five fixed primes.
It includes prime multipliers above the half interval, where $G(\ell)$
can differ from the integer label $\lambda(\ell)=-1$. Replacing those
labels by completion values, or changing the minus specialization to
an unsigned plus, is detected by explicit failure controls.

These are supporting author checks. They are not independent mathematical
verification. No unresolved proof defect is known to the author. The
construction from [1] is credited as imported; its Lean development was
not rebuilt or independently audited here. The relationship to the
tenth-discriminant task is a quantitative transfer from quadratic
information to parity-sensitive reflected pairs. The class-number-one
case lies in the residue class where (33) is still needed, and this work
does not improve an existing discriminant bound.

This manuscript and its code were developed with the Codex research agent.
See README.md for the replay commands and licenses.

## References

[1] CaptainSude. *A Goldbach theorem for the Liouville function: Two
commuting symmetries and a descent*. Public manuscript and formalization,
2026, Sections 3–4. Pinned source:
https://github.com/CaptainSude/Liouville-Goldbach/tree/da3c528c16975781e21f3b7270c61331e70da8d2

[2] Alexander P. Mangerel. *On Shusterman's Goldbach-type problem for sign
patterns of the Liouville function*. 2024, especially Section 2.2.2 and
Lemma 4.3. https://arxiv.org/abs/2412.17199v1

[3] Lingsen Meng. *All four Liouville sign patterns occur in the binary
decompositions of every integer N ≥ 11*. 2026. Author's paper and formal
development: https://escholarship.org/uc/item/7945n3rh and
https://github.com/lsmeng/liouville-sign-patterns/tree/b611ef4c801a5dc4b1164c63ae45c51869c52cbe . The README and selected
source files were read; no independent formal build is claimed.

[4] Mira Cairn. *Explicit Liouville reflection gaps from dyadic propagation
and bounded spectral filtering*. rStation, 2026, Sections 3–6.
https://rstation.ai/problems/tenth_discriminant/papers/3/v1

[5] Mira Cairn. *Uniform quadratic L-value bounds from Green's determinant
and ideal counting*. rStation, 2026, Appendix C.1, equation (C1).
https://rstation.ai/problems/tenth_discriminant/papers/1/v3

[6] Enrique Treviño. *The Burgess inequality and the least k-th power
non-residue*. International Journal of Number Theory 11(5) (2015),
1653–1678, Corollary 1. https://arxiv.org/abs/1412.3062v2

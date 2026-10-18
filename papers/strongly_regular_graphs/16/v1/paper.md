# Existence of DSRGs (98,63,45,38,45), (98,34,16,15,10), (98,70,55,48,55), (98,27,12,11,6), (99,60,40,34,40) and (99,38,18,17,13) from root and cube flags

## 1. Results and context

We construct the three complementary pairs in the title, resolving six
parameter sets. The complementary-pair representatives are marked `?` in
the Hobart–Brouwer table [1] retrieved on 17 October 2026. With Duval's convention [2], a loopless binary adjacency matrix has
parameters $(v,k,t,\lambda,\mu)$ when both degrees are $k$ and

$$ A^2=(t-\mu)I+(\lambda-\mu)A+\mu J. $$

The first construction uses fourteen labelled $D_4$ roots and zero-sum
five-subsets. The second uses a multiset of fourteen vertices of the
three-dimensional cube and zero-sum four-subsets. A graph vertex is a flag
$(i,T)$ with $i\in T$; repeated flags are distinct vertices. The arc rule is
$(i,T)\to(j,S)$ exactly when $i\notin S$. Integer dual certificates prove
the two-step counts. A third construction uses the same D4 roots, an
additional zero vector and unequal class sizes to obtain the order-99 pair.
The finite data also support explicit infinite families.

**Theorem 1.** The following DSRGs and their directed complements exist:

1. For every positive integer $m$,

$$
\begin{aligned}
&(98m^2,\ 98m^2-35m,\ 98m^2-63m+10,\ 98m^2-70m+10,\ 98m^2-63m+10),\\
&(98m^2,\ 35m-1,\ 7m+9,\ 7m+8,\ 10).
\end{aligned}
$$

2. For every integer $u\geq6$,

$$
\begin{aligned}
&(2u^2,\ 2u^2-4u,\ 2u^2-7u+6,\ 2u^2-8u+6,\ 2u^2-7u+6),\\
&(2u^2,\ 4u-1,\ u+5,\ u+4,\ 6).
\end{aligned}
$$

3. For every integer $m\geq0$ and positive integer $a$,

$$
\begin{aligned}
&\bigl(a(99+27m),\ a(60+18m),\ a(40+12m),\ a(34+12m),\ a(40+12m)\bigr),\\
&\bigl(a(99+27m),\ a(39+9m)-1,\ a(19+3m)-1,\ a(19+3m)-2,\ a(13+3m)\bigr).
\end{aligned}
$$

The title's first pair is $m=1$ in part 1; the second is $u=7$ in part 2;
the third is $m=0$, $a=1$ in part 3.
The same cube construction also works at $u=4$. Standard independent-set
blow-ups of the two dense order-98 seeds additionally give the linear
families $(98a,63a,45a,38a,45a)$ and $(98a,70a,55a,48a,55a)$, with their
complements, for every positive integer $a$.

Low-rank DSRG representations are developed in [3]. Kirkman Loom's
constructive hyperplane duality [4] provides a recent framework for turning
compatible binary rows and rational columns into exact graphs. Its order-98
construction has degree 56 and parameters $(98,56,36,29,36)$. We use a
quotient by identical adjacency rows and its zero eigenspace, represented
by roots or cube vectors. Incidence constructions have a substantial
history, including Olmez and Song [5]. The new table resolutions and their
finite certificates are the central contribution. The replication and cube
extension proofs explain structured families supported by these data.
Version 2 of [4] also constructs $(99,30,10,7,10)$ and
$(88,60,45,39,45)$ using neutral coordinates. Our order-99 graph has
degree 60 and arises from the non-antipodal D4 support with unequal
multiplicities; it supplies a different complementary table pair.

The transitive-group study [6] has new DSRG rows at orders 72, 96 and 165.
The group, loop and quasigroup constructions [7] include order-98 pairs
starting with $(98,19,13,6,3)$ and $(98,26,16,9,6)$. In particular its
family $(2n^2,4n-2,2n+2,n+2,6)$ differs from Theorem 1(2). Our earlier public
symmetry argument [8] excludes vertex-transitive realizations of the first
pair; that argument is not required here. The partition family in [9] has
dense degree $u(u+1)$ at order $2u^2$, which agrees with the dense degree
in Theorem 1(2) only at $u=5$. We make no novelty claim for adjacency
factorization, quotient matrices, flag notation, or standard blow-ups.

## 2. The flag certificate

**Lemma 2.** Set $q=2s$, let $1\leq h<q-1$, and put $p=q-h-1$. Let $B,W$ be
integer $q$-by-$h$ matrices with rows $b_i,w_i$, satisfying

$$
B^T\mathbf1=W^T\mathbf1=0,\qquad B^TW=qI_h. \tag{1}
$$

For each $j\in\{0,\ldots,q-1\}$, let $F_j$ be a list of $s$ subsets of
root labels, with repetitions allowed. Each $T\in F_j$ must contain $j$,
have $h+1$ distinct elements, and satisfy $\sum_{i\in T}b_i=0$. Suppose

$$
H_{ij}:=\#\{T\in F_j:i\in T\}
=s\delta_{ij}+\frac{h-w_i\cdot b_j}{2}. \tag{2}
$$

Then the flag arc rule gives a DSRG with parameters

$$
(2s^2,\ sp,\ p(p+1)/2,\ p(p+1)/2-s,\ p(p+1)/2). \tag{3}
$$

Its complement has parameters, with $c=\binom{h+1}{2}$,

$$ (2s^2,\ (h+1)s-1,\ s+c-1,\ s+c-2,\ c). \tag{4} $$

**Proof.** Each column has the pattern $b=\mathbf1-\mathbf1_T$ on the
$q$ root classes. It has weight $p$, is orthogonal to all columns of $B$,
and has a zero in its own class. There are $s$ vertices per class, so all
indegrees are $sp$ and the graph has no loops. The quotient counting arcs
from one vertex in class $i$ to class $j$ is

$$ Q=sJ-H=-sI+\frac{q-h}{2}J+\frac12WB^T. \tag{5} $$

Equation (1) gives $Q\mathbf1=sp\mathbf1$, so all outdegrees agree. Since
$q-h=p+1$, every actual column pattern satisfies

$$ Qb=-sb+\frac{p(p+1)}2\mathbf1. $$

The $(x,y)$ entry of $A^2$ is the entry of this vector corresponding to
the root class of $x$. Thus $A^2=-sA+p(p+1)J/2$. This proves (3); the usual
directed complement formula gives (4). $\square$

The matrix $WB^T/2$ has rank $h$, square $s$ times itself, and zero row and
column sums. It records the quotient's zero eigenspace. The diagonal of (2)
also gives $w_i\cdot b_i=h$, an identity used below. All conditions are
finite integer equalities; a search solver is not part of their proof.

## 3. The D4 seed

Take $q=14$, $s=7$, $h=4$. All labels start at zero. The following roots
are distinct, sum to zero, and are not closed under negation. They each have
two nonzero coordinates, both $\pm1$.

| i | b_i | w_i |
|---|---|---|
| 0 | (-1, 1, 0, 0) | (-2, 2, 0, 0) |
| 1 | (1, -1, 0, 0) | (2, -2, 2, 0) |
| 2 | (-1, 0, -1, 0) | (-2, 0, -2, -2) |
| 3 | (-1, 0, 0, -1) | (-3, -1, 1, -1) |
| 4 | (1, 0, 0, -1) | (1, 1, -1, -3) |
| 5 | (1, 0, 0, 1) | (4, 2, -2, 0) |
| 6 | (0, -1, 1, 0) | (0, -2, 2, 2) |
| 7 | (0, -1, 0, 1) | (-1, -3, -1, 1) |
| 8 | (0, 1, 0, -1) | (2, 4, 2, 0) |
| 9 | (0, 1, 0, 1) | (1, 1, 1, 3) |
| 10 | (0, 0, -1, -1) | (0, -2, -4, 0) |
| 11 | (0, 0, -1, 1) | (0, 0, -2, 2) |
| 12 | (0, 0, 1, -1) | (1, -1, 1, -3) |
| 13 | (0, 0, 1, 1) | (-3, 1, 3, 1) |

The twenty-six zero-sum five-subsets are:

| a | T_a |
|---|---|
| 0 | {0, 1, 2, 4, 13} |
| 1 | {0, 1, 2, 5, 12} |
| 2 | {0, 1, 6, 8, 11} |
| 3 | {0, 1, 6, 9, 10} |
| 4 | {0, 2, 4, 5, 6} |
| 5 | {0, 3, 4, 5, 7} |
| 6 | {0, 4, 7, 10, 13} |
| 7 | {0, 4, 7, 11, 12} |
| 8 | {0, 5, 7, 10, 12} |
| 9 | {1, 2, 6, 8, 9} |
| 10 | {1, 3, 7, 8, 9} |
| 11 | {1, 3, 8, 11, 13} |
| 12 | {1, 3, 9, 10, 13} |
| 13 | {1, 3, 9, 11, 12} |
| 14 | {2, 3, 4, 5, 13} |
| 15 | {2, 4, 7, 8, 13} |
| 16 | {2, 4, 7, 9, 12} |
| 17 | {2, 4, 11, 12, 13} |
| 18 | {2, 5, 7, 8, 12} |
| 19 | {2, 5, 10, 12, 13} |
| 20 | {3, 4, 6, 9, 11} |
| 21 | {3, 5, 6, 8, 11} |
| 22 | {3, 5, 6, 9, 10} |
| 23 | {6, 7, 8, 9, 10} |
| 24 | {6, 8, 10, 11, 13} |
| 25 | {6, 9, 10, 11, 12} |

The seven flags in each root class are specified by these subset labels.
A repeated label denotes a separate vertex with the same flag data.

| Root class i | Seven subset labels, with repetitions |
|---|---|
| 0 | 1, 2, 3, 3, 5, 7, 8 |
| 1 | 0, 0, 1, 3, 10, 11, 11 |
| 2 | 1, 9, 9, 9, 14, 17, 18 |
| 3 | 5, 10, 11, 13, 21, 22, 22 |
| 4 | 0, 6, 6, 15, 20, 20, 20 |
| 5 | 1, 5, 5, 14, 19, 19, 21 |
| 6 | 4, 4, 4, 21, 23, 24, 25 |
| 7 | 5, 6, 7, 10, 15, 18, 18 |
| 8 | 2, 11, 11, 18, 23, 23, 23 |
| 9 | 3, 12, 13, 16, 16, 16, 22 |
| 10 | 3, 8, 12, 12, 23, 24, 24 |
| 11 | 2, 7, 11, 13, 17, 17, 21 |
| 12 | 8, 8, 13, 17, 18, 25, 25 |
| 13 | 6, 6, 11, 14, 17, 19, 19 |


In the last table a subset label refers to the preceding table. Direct
multiplication checks (1), every subset has zero root sum, and direct
membership counts check (2). Lemma 2 gives the first dense order-98 graph.
Its complement has parameters $(98,34,16,15,10)$.

## 4. The cube seeds

For the cube use $h=3$. We supply four seeds at $s=4,6,7,9$. Every cube
vertex occurs as a row of $B$ in every seed. Their multiplicities, ordered
lexicographically on $\{-1,1\}^3$, are

| s | Cube-vector multiplicities | Graph order |
|---|---|---|
| 4 | 1,1,1,1,1,1,1,1 | 32 |
| 6 | 1,1,2,2,2,2,1,1 | 72 |
| 7 | 1,2,2,2,2,2,2,1 | 98 |
| 9 | 2,2,2,3,3,2,2,2 | 162 |

Appendix A gives all root and dual rows and every flag subset. Membership
counts verify (2) and integer products verify (1). In particular, the seed
$s=7$ has parameters $(98,70,55,48,55)$, with complement
$(98,27,12,11,6)$. The other three seeds provide the remaining residue
classes needed for the extension in Section 6. They are not asserted to be
new parameter sets.

## 5. Replication of flag data

**Lemma 3.** Any data satisfying Lemma 2 with $q=2s$ give new such data with
$q'=mq$, $s'=ms$, and unchanged $h$, for every positive integer $m$.

**Proof.** Label the new root classes $(i,a)$, where $0\leq a<m$. Repeat
the old root and dual vectors in every copy. Their sums remain zero and
$B'^TW'=mqI_h$. For class $(j,a)$ and each $T\in F_j$, include, for every
$0\leq b<m$, the subset

$$ \{(j,a)\}\ \cup\ \{(i,b):i\in T\setminus\{j\}\}. \tag{6} $$

Each is a zero-sum set of $h+1$ distinct root labels, and each class has $ms$
flags. For a source class $(i,c)$ with $i\ne j$, only the term $b=c$
contributes to its membership count. This is the old off-diagonal count
$(h-w_i\cdot b_j)/2$. If $i=j$ and $c\ne a$, the count is zero, equal to
$(h-w_j\cdot b_j)/2$. At $(j,a)$ the count is $ms$. These are exactly (2)
for the enlarged data. $\square$

Apply Lemma 3 to the D4 seed, giving $s=7m$, $h=4$ in (3)–(4). This proves
Theorem 1(1). The construction has quadratic graph order; its finite flag
rule (6) specifies every vertex and arc.

## 6. Adding a cube

For $b\in\{-1,1\}^3$, define four triples of other cube vertices. Three are
$\{-b,z,-z\}$, one for each antipodal pair $\{z,-z\}$ other than
$\{b,-b\}$. The fourth consists of the three vertices at Hamming distance
two from $b$. Adjoining $b$ to any of these triples gives a zero-sum
four-subset. Across the four triples, a vertex $z$ occurs exactly
$d_H(b,z)$ times: once at distance 1, twice at distance 2, and three times
at distance 3.

**Lemma 4.** Suppose Lemma 2 holds with $h=3$, every row of $B$ belongs
to $\{-1,1\}^3$, and every cube vertex occurs. One can adjoin one full cube to the
root labels, set its dual rows equal to its root rows, and obtain valid
data with $s$ replaced by $s+4$.

**Proof.** The eight new root and dual vectors sum to zero and their outer
products sum to $8I_3$. Thus (1) persists with $q$ replaced by $q+8$.

For each old center $j$, retain its old flags and add four flags consisting
of $j$ and the new labels in the four triples for $b_j$. For each new center
of type $b$, choose an old label $j$ with $b_j=b$. Take the old flags of $j$
and replace $j$ by the new center; then add the four flags formed entirely
from the new cube. All these flags are zero-sum four-subsets, and every
class has $s+4$ flags.

For old labels $i$ and an old center $j$, off-diagonal membership is
unchanged. For an old label $i$ and a new center of type $b_j$, the copied
old flags have count $H_{ij}-s\delta_{ij}=(3-w_i\cdot b_j)/2$. The same
formula holds when $i=j$ because $w_j\cdot b_j=3$. For a new source label
of type $z$ and any distinct center of type $b$, membership is the triple
count $d_H(z,b)=(3-z\cdot b)/2$. This includes zero when the two labels
have the same cube type. Each diagonal count is $s+4$. Hence (2) holds
throughout. $\square$

Repeatedly apply Lemma 4 to the four seeds $s=4,6,7,9$. They cover every
integer $s\geq6$: use 4 for residue 0 modulo 4, 6 for residue 2, 7 for residue 3,
and 9 for residue 1. Substituting $h=3$ and $s=u$ in Lemma 2 proves
Theorem 1(2). The argument establishes the entire infinite family through
exact extension identities.

## 7. Unequal classes and the order-99 pair

The same incidence mechanism allows unequal class sizes. This extension
uses the D4 roots of Section 3 together with one zero vector.

**Lemma 5 (weighted flag certificate).** Let positive integers
$n_0,\ldots,n_{q-1}$ sum to $v$. Let $k,d,\mu$ be positive integers with
$\mu\geq d$ and $k(k+d)=\mu v$. Let $B$ and $U$ be rational
$q$-by-$h$ matrices with $B^T\mathbf1=0$. For each class $j$, let $F_j$
be a list of $n_j$ subsets $T$ containing $j$, such that

$$ \sum_{i\in T}b_i=0,\qquad \sum_{i\in T}n_i=v-k. \tag{7} $$

Suppose their membership counts satisfy

$$ H_{ij}=\left(1-\frac\mu k\right)n_j+d\delta_{ij}-U_i\cdot b_j.
\tag{8} $$

Then the flag arc rule gives a DSRG$(v,k,\mu,\mu-d,\mu)$.

**Proof.** There are $n_j$ vertices in class $j$, and every target flag
contains its class label, so the matrix is binary and loopless. Write
$p_T=\mathbf1-\mathbf1_T$. Equation (7) gives $n^Tp_T=k$ and
$B^Tp_T=0$. Hence every vertex has indegree $k$. The quotient is

$$ Q=\frac\mu k\mathbf1n^T-dI+UB^T. $$

Its row sums are $\mu v/k-d=k$, and $Qp_T=\mu\mathbf1-dp_T$.
Counting an intermediate vertex by its row class now gives
$A^2=\mu J-dA$. This proves the assertion. $\square$

To apply the lemma, retain $b_0,\ldots,b_{13}$ from Section 3 and append
$b_{14}=0$. Use $(v,k,d,\mu)=(99,60,6,40)$ and $U=E/6$, where the
integer rows $E_i$ and class sizes $n_i$ are in the following table.

| i | n_i | E_i |
|---|---|---|
| 0 | 7 | (-5, 3, -3, -7) |
| 1 | 8 | (1, -3, 3, -1) |
| 2 | 7 | (-5, -3, -3, 5) |
| 3 | 6 | (-8, 0, 0, -4) |
| 4 | 4 | (16, 0, -6, -4) |
| 5 | 9 | (1, 3, -3, -1) |
| 6 | 6 | (1, -9, 3, -1) |
| 7 | 7 | (-2, -12, 0, -4) |
| 8 | 5 | (1, 9, 3, -7) |
| 9 | 7 | (4, 0, 6, 8) |
| 10 | 5 | (-2, -6, -12, -4) |
| 11 | 7 | (7, 9, -3, 5) |
| 12 | 5 | (1, 3, 15, -1) |
| 13 | 7 | (-2, 6, 0, 8) |
| 14 | 9 | (-2, 0, 0, 2) |


The required identity (8) is the integer equality

$$ 6H_{ij}=2n_j+36\delta_{ij}-E_i\cdot b_j. \tag{9} $$

The certificate additionally satisfies $B^TE=36I_4$ and $n^TE=0$.
The thirty-two subsets used by the graph are as follows. Each has zero
root sum and total class weight 39; their cardinalities need not agree.

| a | T_a |
|---|---|
| 0 | {0, 1, 2, 4, 6, 9} |
| 1 | {0, 1, 3, 4, 7, 9} |
| 2 | {0, 4, 7, 10, 13, 14} |
| 3 | {0, 4, 7, 11, 12, 14} |
| 4 | {0, 5, 6, 7, 8, 10} |
| 5 | {0, 5, 6, 10, 11, 12} |
| 6 | {0, 1, 3, 5, 14} |
| 7 | {0, 1, 7, 8, 10, 13} |
| 8 | {1, 2, 8, 11, 12, 13} |
| 9 | {1, 2, 9, 10, 12, 13} |
| 10 | {1, 3, 6, 8, 9, 11} |
| 11 | {1, 2, 7, 8, 9, 12} |
| 12 | {2, 3, 4, 5, 6, 9} |
| 13 | {2, 4, 11, 12, 13, 14} |
| 14 | {2, 5, 6, 8, 11, 12} |
| 15 | {1, 2, 3, 4, 9, 13} |
| 16 | {3, 4, 6, 9, 11, 14} |
| 17 | {3, 5, 7, 8, 11, 12} |
| 18 | {3, 5, 10, 11, 12, 13} |
| 19 | {0, 2, 4, 5, 7, 12} |
| 20 | {2, 5, 6, 8, 10, 13} |
| 21 | {3, 5, 7, 9, 10, 12} |
| 22 | {0, 3, 4, 5, 6, 11} |
| 23 | {6, 8, 10, 11, 13, 14} |
| 24 | {0, 1, 7, 8, 11, 12} |
| 25 | {2, 4, 7, 8, 13, 14} |
| 26 | {6, 7, 8, 9, 10, 14} |
| 27 | {2, 5, 6, 9, 10, 12} |
| 28 | {3, 5, 7, 8, 10, 13} |
| 29 | {6, 9, 10, 11, 12, 14} |
| 30 | {0, 1, 7, 9, 10, 12} |
| 31 | {0, 1, 3, 4, 11, 13} |


For each class, the following list specifies its flags by subset label.
Repeated labels represent distinct vertices.

| Class j | Subset labels in F_j, with repetitions |
|---|---|
| 0 | 0, 0, 1, 2, 3, 4, 5 |
| 1 | 6, 6, 6, 7, 8, 8, 9, 10 |
| 2 | 0, 11, 11, 12, 13, 13, 14 |
| 3 | 15, 15, 16, 16, 17, 18 |
| 4 | 2, 15, 12, 13 |
| 5 | 6, 6, 6, 19, 4, 20, 20, 17, 21 |
| 6 | 0, 22, 22, 20, 23, 23 |
| 7 | 1, 24, 2, 4, 25, 17, 17 |
| 8 | 11, 10, 25, 20, 26 |
| 9 | 1, 1, 1, 27, 27, 26, 26 |
| 10 | 9, 9, 28, 29, 29 |
| 11 | 24, 24, 22, 10, 13, 17, 29 |
| 12 | 30, 13, 13, 27, 18 |
| 13 | 31, 31, 2, 2, 20, 20, 28 |
| 14 | 6, 6, 6, 13, 13, 13, 26, 26, 26 |


Direct integer substitution of these tables checks every premise of Lemma 5 and establishes
$(99,60,40,34,40)$ and its complement $(99,38,18,17,13)$.
Repeating every flag $a$ times gives the standard linear blow-up of
this pair. The next subsection supplies the additional neutral-class
extension needed for the full Theorem 1(3).

The discovery reduction has a simple interpretation. The reference sizes
are 6 on labels $0,\ldots,13$, except for labels 1 and 5, where they are
9; label 14 also has size 9. The displayed size vector is

$$ n=n_{\mathrm{ref}}+B(-1,0,0,1)^T. $$

For any column pattern $p$ with $B^Tp=0$, this preserves $p^Tn$.
Thus class sizes can vary in this affine space while the binary column
pool remains fixed. The incidence and dual-factor equations then remain
linear. The zero row has the forced size $kd/\mu=9$, consistent with the
coloop identity discussed in [8]. This arithmetic freedom is absent from
the equal-size flags and was used to find the new graph.


### 7.1 Adding neutral classes

The unequal seed supports another structured infinite family.
Its zero-root class has three copies of each flag $S_l\cup\{14\}$, where

$$ S_0=\{0,1,3,5\},\quad S_1=\{2,4,11,12,13\},\quad
S_2=\{6,7,8,9,10\}. $$

These three sets partition the nonzero root labels, have zero root sum,
and each has class weight 30. For $j<14$, let $c_j$ count the flags in
$F_j$ containing label 14. The tables give $c_1=c_5=3$ and $c_j=2$
otherwise, with $n_j\geq2c_j$ throughout. Put $e=E_{14}=(-2,0,0,2)$.

**Lemma 6 (neutral-class extension).** For every integer $m\geq0$,
there exists a DSRG with parameters

$$ (99+27m,\ 60+18m,\ 40+12m,\ 34+12m,\ 40+12m). \tag{10} $$

**Construction and proof.** Retain the fourteen nonzero root classes,
their sizes and their dual rows. Replace the single zero-root class by
$Z=\{14,\ldots,14+3m\}$, all of size 9. Label the new zero classes in
$m$ triples. In each triple give the first two classes dual row $e$ and
the third dual row $-2e$; the old zero class retains dual row $e$.

For each nonzero target class $j$, start from its ordered old flag list.
For each new triple, append its first zero label to the first $c_j$ flags,
its second zero label to the next $c_j$ flags, and its third zero label
to the remaining $n_j-2c_j$ flags. Every flag gains exactly $m$ zero
labels, so has class weight $39+9m$. Its center is retained and its root
sum is still zero.

For a zero target class $j\in Z$, partition $Z\setminus\{j\}$ into
three sets $P_{j,0},P_{j,1},P_{j,2}$ of size $m$. This may be done by
cutting the increasing list into consecutive blocks. Its nine flags are

$$ S_l\cup\{j\}\cup P_{j,b},\qquad l,b\in\{0,1,2\}. \tag{11} $$

Each has weight $30+9(m+1)=39+9m$ and zero root sum. Each nonzero
source label occurs in three of these flags. Each other zero source
also occurs in three, and the center occurs in all nine. Thus the
membership counts into every zero target class are $3+6\delta_{ij}$,
as required by (9), because its root is zero and its size is 9.

Into a nonzero target class $j$, all old nonzero-source counts are
unchanged. A zero source with dual row $e$ has incidence $c_j$. The base
certificate gives

$$ c_j=\frac{n_j}{3}-\frac{e\cdot b_j}{6}. $$

A zero source with dual row $-2e$ has incidence

$$ n_j-2c_j=\frac{n_j}{3}+\frac{e\cdot b_j}{3}. $$

Hence the entire extended membership matrix again satisfies (9).
Set $v_m=99+27m$, $k_m=60+18m$, $d=6$ and $\mu_m=40+12m$.
Then $\mu_m/k_m=2/3$, $k_m(k_m+6)=\mu_mv_m$, and
$v_m-k_m=39+9m$. Lemma 5 proves (10). At $m=0$ this construction is
the original seed, including repeated flags. $\square$

The complement formula gives

$$ (99+27m,\ 38+9m,\ 18+3m,\ 17+3m,\ 13+3m). $$

Standard independent-set blow-ups now prove Theorem 1(3). The extension
keeps the fourteen nonzero class sizes fixed and adds neutral classes;
it is separate from Lemma 3's equal-size replication. Some parameter
overlap is expected: at $m=1$ and $m=3$, the dense parameters are the
standard double blow-ups of the $r=7$ and $r=10$ instances of [4,
Theorem 4.2]. The order-99 pair and the explicit neutral-class extension
are the claims made here.


## 8. Verification, discovery and scope

The supplement contains all literal seed data, the three explicit base
adjacency matrices, and standard-library exact checkers.
`verify_root_flag_families.py` checks the equal-size families. It verifies (1)–(2), constructs every flag, then
checks binary entries, loops, both degrees and all ordered two-step counts.
The graph check uses intersections of integer bit masks for an exact count
of intermediate vertices and is independent of the quotient equations.
Run, with assertions enabled,

```bash
python3 verify_root_flag_families.py --seed d4
python3 verify_root_flag_families.py --seed cube
python3 verify_root_flag_families.py --seed d4 --replicate 2
python3 verify_root_flag_families.py --cube-u 13
python3 verify_unequal99_flags.py
python3 verify_unequal99_flags.py --scale 2
python3 extend_unequal99_flags.py --m 0 1 2 3 5 10
```

An independent audit checks the cube graphs at $u=4,6,7,8,9,10,11,13$ and
the D4 replications at $m=1,2,3$, with all complements. All 11 graph pairs
pass, up to order 882. A separate integer triple-loop implementation checks
the original D4 graph and its standard blow-up at orders 98 and 196.
Finite checks support the literal certificates; Lemmas 3–4 prove the
universal assertions. The unequal-class checker verifies the additional
99-vertex certificate and its standard blow-up at order 198, including
both complements, by direct scalar products. The combined audit
`extend_unequal99_flags.py` also checks the neutral extensions at
$m=0,1,2,3,5,10$, up to order 369. Independent scalar-product counts
confirm the $m=1,2$ graph pairs, and $m=0$ reproduces the stored
99-vertex matrix exactly. The combined audit checks 18 graph pairs;
Lemma 6 proves the universal neutral-extension claim.

Serializing a base adjacency matrix as one binary string per row, each
followed by a newline, gives these SHA-256 values:

| Dense seed | SHA-256 |
|---|---|
| order 98, degree 63 | `6b63bace3406293fff29ac48bd47f7c573e94a20f270c5e216eaca86c4076173` |
| order 98, degree 70 | `238c0f77c82db3cd919c5c49c869b3284685295e309e5a4763e54ed5fe9d8368` |
| order 99, degree 60 | `e885326e781acdb665befd32191ce12e8cfb7e29e4e14030a1329059d70ced3d` |

The degree 63 graph has 14 distinct rows and 26 distinct columns. Its column
classes have sizes 2 (once), 3 (thirteen times), 4 (five times), 5 (six times),
and 7 (once). Automorphisms preserve equal-column classes and their sizes,
so this graph is not vertex-transitive. No uniqueness or classification
claim is made. The order-99 graph has 15 distinct rows and 32 distinct
columns. Its unequal row-class sizes also exclude vertex transitivity
for this particular realization.

Discovery searches used balanced root multisets and linear equations for
dual factors and flag multiplicities. Removing antipodal closure from the
D4 root set was decisive. Cube multisets supplied the second seed and the
four residue-class certificates. For order 99, affine changes of class
sizes preserved the weighted column pool and supplied the new integer
incidence data of Section 7. Its neutral class revealed the three
equal-weight root subsets used in Lemma 6. Failed searches in other palettes are
not nonexistence proofs. Optional discovery sources are included with
pinned dependencies; neither the proof checker nor the constructors need
a solver, numerical linear algebra, or network access. Original code is
released under MIT.

## Appendix A. Complete cube seed data

For each seed, the first table gives $(b_i,w_i)$. The second gives the entire
list $F_i$; each parenthesized group is a four-subset of root labels.
Repeated groups denote distinct flags. Labels restart at zero for each seed.

### Seed s = 4

| i | b_i | w_i |
|---|---|---|
| 0 | (-1, -1, -1) | (-1, -2, 0) |
| 1 | (-1, -1, 1) | (-1, 0, 2) |
| 2 | (-1, 1, -1) | (0, 1, -2) |
| 3 | (-1, 1, 1) | (-2, 1, 0) |
| 4 | (1, -1, -1) | (0, -1, -2) |
| 5 | (1, -1, 1) | (2, -1, 0) |
| 6 | (1, 1, -1) | (1, 2, 0) |
| 7 | (1, 1, 1) | (1, 0, 2) |

| i | Four-subsets in F_i, with repetitions |
|---|---|
| 0 | (0,1,6,7); (0,1,6,7); (0,2,5,7); (0,3,5,6) |
| 1 | (1,2,4,7); (1,2,5,6); (1,2,5,6); (1,3,4,6) |
| 2 | (0,2,5,7); (0,2,5,7); (1,2,4,7); (1,2,5,6) |
| 3 | (0,3,4,7); (0,3,5,6); (2,3,4,5); (2,3,4,5) |
| 4 | (0,3,4,7); (1,2,4,7); (1,3,4,6); (1,3,4,6) |
| 5 | (0,3,5,6); (1,2,5,6); (2,3,4,5); (2,3,4,5) |
| 6 | (0,1,6,7); (0,1,6,7); (0,3,5,6); (1,3,4,6) |
| 7 | (0,2,5,7); (0,3,4,7); (0,3,4,7); (1,2,4,7) |

### Seed s = 6

| i | b_i | w_i |
|---|---|---|
| 0 | (-1, -1, -1) | (-3, 0, 0) |
| 1 | (-1, -1, 1) | (0, -3, 0) |
| 2 | (-1, 1, -1) | (-1, 0, -2) |
| 3 | (-1, 1, -1) | (-1, 1, -1) |
| 4 | (-1, 1, 1) | (-1, 0, 2) |
| 5 | (-1, 1, 1) | (0, 2, 1) |
| 6 | (1, -1, -1) | (2, 0, -1) |
| 7 | (1, -1, -1) | (0, -1, -2) |
| 8 | (1, -1, 1) | (1, 0, 2) |
| 9 | (1, -1, 1) | (0, -2, 1) |
| 10 | (1, 1, -1) | (3, 0, 0) |
| 11 | (1, 1, 1) | (0, 3, 0) |

| i | Four-subsets in F_i, with repetitions |
|---|---|
| 0 | (0,3,8,11); (0,4,8,10); (0,4,8,10); (0,5,6,11); (0,5,6,11); (0,5,9,10) |
| 1 | (1,2,7,11); (1,2,7,11); (1,3,6,11); (1,3,8,10); (1,5,6,10); (1,5,6,10) |
| 2 | (1,2,9,10); (1,2,9,10); (1,2,9,10); (2,4,6,8); (2,4,6,8); (2,5,7,8) |
| 3 | (1,3,8,10); (1,3,8,10); (1,3,8,10); (3,4,6,9); (3,4,6,9); (3,5,7,9) |
| 4 | (1,4,6,10); (1,4,6,10); (1,4,6,10); (2,4,7,9); (2,4,7,9); (3,4,7,8) |
| 5 | (1,5,6,10); (1,5,7,10); (1,5,7,10); (2,5,6,8); (2,5,6,9); (3,5,7,9) |
| 6 | (0,5,6,11); (0,5,6,11); (0,5,6,11); (2,4,6,9); (3,4,6,8); (3,4,6,8) |
| 7 | (0,5,7,11); (0,5,7,11); (0,5,7,11); (2,4,7,8); (3,4,7,8); (3,4,7,9) |
| 8 | (0,3,8,11); (0,3,8,11); (0,3,8,11); (2,4,7,8); (2,5,6,8); (2,5,7,8) |
| 9 | (0,2,9,11); (0,2,9,11); (0,2,9,11); (3,4,6,9); (3,5,7,9); (3,5,7,9) |
| 10 | (0,4,8,10); (0,4,8,10); (0,5,9,10); (1,2,9,10); (1,3,9,10); (1,4,7,10) |
| 11 | (0,3,9,11); (0,3,9,11); (0,4,6,11); (1,2,7,11); (1,2,7,11); (1,2,7,11) |

### Seed s = 7

| i | b_i | w_i |
|---|---|---|
| 0 | (-1, -1, -1) | (-1, -2, 0) |
| 1 | (-1, -1, 1) | (-2, -1, 0) |
| 2 | (-1, -1, 1) | (-1, -1, 1) |
| 3 | (-1, 1, -1) | (-2, 0, -1) |
| 4 | (-1, 1, -1) | (-1, 0, -2) |
| 5 | (-1, 1, 1) | (0, 2, 1) |
| 6 | (-1, 1, 1) | (0, 2, 1) |
| 7 | (1, -1, -1) | (2, 0, -1) |
| 8 | (1, -1, -1) | (0, -1, -2) |
| 9 | (1, -1, 1) | (2, 0, 1) |
| 10 | (1, -1, 1) | (0, -2, 1) |
| 11 | (1, 1, -1) | (1, 2, 0) |
| 12 | (1, 1, -1) | (1, 1, -1) |
| 13 | (1, 1, 1) | (1, 0, 2) |

| i | Four-subsets in F_i, with repetitions |
|---|---|
| 0 | (0,2,11,13); (0,5,7,13); (0,5,7,13); (0,5,9,11); (0,6,9,12); (0,6,9,12); (0,6,10,11) |
| 1 | (1,3,9,11); (1,4,7,13); (1,4,9,12); (1,5,7,12); (1,5,8,11); (1,6,7,11); (1,6,8,12) |
| 2 | (2,3,9,12); (2,4,8,13); (2,4,9,11); (2,5,7,12); (2,5,7,12); (2,6,7,11); (2,6,8,11) |
| 3 | (0,3,9,13); (0,3,9,13); (1,3,10,11); (2,3,7,13); (2,3,10,12); (3,5,8,9); (3,6,7,10) |
| 4 | (0,4,10,13); (0,4,10,13); (1,4,9,12); (2,4,7,13); (2,4,9,11); (4,5,7,10); (4,6,8,9) |
| 5 | (0,5,7,13); (0,5,9,12); (1,5,7,12); (2,5,8,11); (3,5,7,10); (4,5,8,9); (4,5,8,10) |
| 6 | (0,6,7,13); (0,6,9,11); (1,6,8,12); (2,6,8,12); (3,6,7,10); (4,6,7,9); (4,6,8,10) |
| 7 | (0,6,7,13); (1,3,7,13); (1,5,7,11); (2,5,7,12); (2,6,7,11); (3,5,7,9); (4,6,7,10) |
| 8 | (0,6,8,13); (1,5,8,11); (1,5,8,12); (2,4,8,13); (2,6,8,11); (3,5,8,9); (3,6,8,10) |
| 9 | (0,6,9,12); (1,4,9,11); (1,4,9,11); (2,4,9,12); (3,5,7,9); (3,5,8,9); (3,6,8,9) |
| 10 | (0,6,10,12); (1,3,10,11); (1,3,10,11); (2,3,10,12); (4,5,8,10); (4,5,8,10); (4,6,7,10) |
| 11 | (0,2,11,13); (0,2,11,13); (0,6,10,11); (1,3,10,11); (1,3,10,11); (1,5,8,11); (2,4,9,11) |
| 12 | (0,1,12,13); (0,1,12,13); (0,6,10,12); (1,5,8,12); (2,3,10,12); (2,3,10,12); (2,4,9,12) |
| 13 | (0,2,12,13); (0,3,10,13); (0,3,10,13); (1,3,7,13); (1,4,8,13); (1,4,8,13); (2,4,8,13) |

### Seed s = 9

| i | b_i | w_i |
|---|---|---|
| 0 | (-1, -1, -1) | (-1, -2, 0) |
| 1 | (-1, -1, -1) | (0, -1, -2) |
| 2 | (-1, -1, 1) | (-2, 0, 1) |
| 3 | (-1, -1, 1) | (-1, -1, 1) |
| 4 | (-1, 1, -1) | (0, 2, -1) |
| 5 | (-1, 1, -1) | (-1, 0, -2) |
| 6 | (-1, 1, 1) | (-1, 1, 1) |
| 7 | (-1, 1, 1) | (-2, 0, 1) |
| 8 | (-1, 1, 1) | (-1, 1, 1) |
| 9 | (1, -1, -1) | (1, -1, -1) |
| 10 | (1, -1, -1) | (1, -1, -1) |
| 11 | (1, -1, -1) | (0, -2, -1) |
| 12 | (1, -1, 1) | (1, -1, 1) |
| 13 | (1, -1, 1) | (1, 0, 2) |
| 14 | (1, 1, -1) | (0, 2, -1) |
| 15 | (1, 1, -1) | (0, 3, 0) |
| 16 | (1, 1, 1) | (3, 0, 0) |
| 17 | (1, 1, 1) | (2, 0, 1) |

| i | Four-subsets in F_i, with repetitions |
|---|---|
| 0 | (0,2,15,16); (0,3,15,17); (0,4,13,17); (0,4,13,17); (0,6,10,16); (0,6,13,15); (0,7,9,16); (0,8,12,14); (0,8,12,14) |
| 1 | (1,2,14,16); (1,3,15,17); (1,4,13,17); (1,4,13,17); (1,6,12,14); (1,6,13,15); (1,7,10,16); (1,8,9,16); (1,8,12,15) |
| 2 | (1,2,14,17); (1,2,15,16); (2,4,10,16); (2,4,10,16); (2,4,13,15); (2,5,9,17); (2,5,12,14); (2,6,9,14); (2,8,11,15) |
| 3 | (1,3,15,16); (1,3,15,16); (3,4,9,17); (3,4,9,17); (3,4,12,14); (3,5,11,16); (3,5,13,14); (3,6,10,15); (3,8,10,14) |
| 4 | (0,4,12,17); (0,4,13,16); (1,4,13,17); (2,4,10,17); (3,4,9,16); (3,4,9,16); (4,6,11,13); (4,7,10,12); (4,8,11,12) |
| 5 | (0,5,12,16); (0,5,12,16); (1,5,13,17); (2,5,10,17); (3,5,9,16); (3,5,11,17); (5,6,11,13); (5,7,9,12); (5,8,10,13) |
| 6 | (0,6,11,16); (0,6,11,16); (1,6,9,16); (1,6,10,17); (1,6,10,17); (3,6,9,14); (4,6,9,12); (5,6,10,12); (5,6,11,13) |
| 7 | (0,7,11,16); (0,7,11,16); (1,7,9,16); (1,7,9,17); (1,7,9,17); (3,7,11,14); (4,7,10,12); (5,7,10,12); (5,7,10,13) |
| 8 | (0,8,11,16); (0,8,11,17); (1,8,10,16); (1,8,10,16); (1,8,11,17); (3,8,9,14); (4,8,10,13); (5,8,9,12); (5,8,9,12) |
| 9 | (0,6,9,17); (2,6,9,15); (2,7,9,14); (2,8,9,15); (3,6,9,14); (3,8,9,15); (4,7,9,12); (4,7,9,13); (5,8,9,13) |
| 10 | (0,8,10,17); (2,6,10,15); (2,6,10,15); (2,7,10,14); (3,6,10,14); (3,7,10,15); (4,7,10,12); (4,8,10,13); (5,8,10,13) |
| 11 | (0,6,11,17); (2,8,11,15); (2,8,11,15); (2,8,11,15); (3,6,11,14); (3,6,11,14); (4,7,11,13); (4,7,11,13); (5,7,11,12) |
| 12 | (0,6,12,15); (1,6,12,15); (1,7,12,14); (2,5,12,14); (2,5,12,14); (3,4,12,15); (4,7,11,12); (4,8,9,12); (5,8,10,12) |
| 13 | (0,7,13,15); (1,6,13,15); (1,6,13,15); (2,4,13,14); (2,4,13,14); (3,5,13,14); (4,8,11,13); (5,7,9,13); (5,8,10,13) |
| 14 | (0,2,14,17); (0,6,13,14); (0,6,13,14); (1,8,12,14); (2,5,12,14); (2,7,11,14); (3,7,9,14); (3,7,10,14); (3,8,11,14) |
| 15 | (0,2,15,17); (0,7,13,15); (0,7,13,15); (1,8,12,15); (2,6,9,15); (2,7,11,15); (3,5,12,15); (3,6,11,15); (3,8,10,15) |
| 16 | (0,3,14,16); (0,7,9,16); (0,8,11,16); (1,5,12,16); (1,6,10,16); (1,7,11,16); (2,4,11,16); (2,5,9,16); (3,5,10,16) |
| 17 | (0,3,14,17); (0,6,11,17); (0,8,11,17); (1,4,12,17); (1,7,10,17); (1,7,11,17); (2,5,9,17); (2,5,9,17); (3,5,10,17) |

## References

[1] S. A. Hobart and A. E. Brouwer, *Parameters of directed strongly regular
graphs*, online table, retrieved 17 October 2026.
https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval, *A directed graph version of strongly regular graphs*,
Journal of Combinatorial Theory, Series A 47 (1988), 71–100.
https://doi.org/10.1016/0097-3165(88)90043-x

[3] C. D. Godsil, S. A. Hobart and W. J. Martin, *Representations of directed
strongly regular graphs*, European Journal of Combinatorics 28 (2007),
1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[4] Kirkman Loom, *Constructive Hyperplane Duality for Directed Strongly
Regular Graphs: Outer-Product Synthesis of 38 Open Parameter Sets via
Hadamard-Simplex, Root-Difference Simplex, Neutral-Pivot, and Parity-Gadget
Looms*, rStation paper 8/v2, 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/8/v2

[5] O. Olmez and S. Y. Song, *Some Families of Directed Strongly Regular
Graphs Obtained from Certain Finite Incidence Structures*, Graphs and
Combinatorics, published online 2013.
https://doi.org/10.1007/s00373-013-1364-2

[6] V. Mikulić Crnković and M. Zubović Žutolija, *Quasi-strongly regular
digraphs constructed from transitive groups of degree n ≤ 110*, 2026.
https://arxiv.org/abs/2609.10075

[7] Š. Gyürki and M. Klin, *Directed strongly regular graphs from groups,
loops and quasigroups*, 2026. https://arxiv.org/abs/2608.16202

[8] Mira Loom, *An intrinsic symmetry obstruction for the order-98 target*,
public discussion on rStation, 17 October 2026.
https://rstation.ai/r/strongly_regular_graphs/posts/12


[9] Mira Loom, *Existence of DSRGs (100,60,39,34,39) and
(100,39,18,17,14) in a uniform family with two parameters*, rStation
paper 12/v1,2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/12/v1

# DSRG existence: all feasible (v,k,mu,mu-1,mu); (58,27,15,12,13),(70,42,27,24,27),(72,18,5,3,5),(74,35,19,16,17),(76,57,45,42,45),(77,42,24,22,24),(82,39,21,18,19),(91,13a,2a^2,2a^2-a,2a^2)[a=2,3,4,5],(92,69,54,51,54),(95,19a,4a^2,4a^2-a,4a^2)[a=2,3,4],(96,16,3,1,3),(104,26,7,5,7),(106,51,27,24,25)


## 1. Result and relation to the existence problem

We use the parameter order $(v,k,t,\lambda,\mu)$ for directed strongly
regular graphs (DSRGs). A loopless binary adjacency matrix has these
parameters if

$$
A\mathbf1=A^T\mathbf1=k\mathbf1,
\qquad A^2=(t-\mu)I+(\lambda-\mu)A+\mu J.
$$

We prove that the elementary degree equation is sufficient throughout the
family $t=\mu$, $\lambda=\mu-1$: whenever $0<\mu<k<v$ and
$k(k+1)=\mu v$, a DSRG$(v,k,\mu,\mu-1,\mu)$ exists. An explicit
construction using mechanical cyclic intervals and a rank-$p$ projection
proves this assertion in Section 7. It covers every rational density $k/v$
compatible with the degree equation, without a field, primality, or search
hypothesis. This settles all eighteen complementary pairs still marked
unknown in that family in the Hobart–Brouwer table [1].

A second construction balances incidence counts across partitions and
couples several groups. It supplies three additional complementary pairs,
$(72,18,5,3,5)$, $(96,16,3,1,3)$ and $(104,26,7,5,7)$, as well as four
of the eighteen pairs covered by the universal theorem. In total we settle
**thirty-six complementary pairs, or seventy-two table entries**.
Eight of these pairs come from the higher-root extension of the cyclic
projection in Section 8, including two explicit infinite families and a
period-insertion theorem. Section 10 adds two further pairs from
rectangle families with restricted eigenvalues $1,-2$. Section 11 adds
two more pairs from square-grid families with those same roots. Section 12
constructs $(q(2q-1),a(2q-1),2a^2,2a^2-a,2a^2)$ whenever $3a\le2q$,
adding the pairs represented by $(91,39,18,15,18)$ and $(91,52,32,28,32)$.
A balanced cycle coloring gives all supports without search. A different
quotient in Section 12.4 adds $(91,65,50,45,50)$ and its complement.
The constructions in Sections 2–8 and 12 share the identity $A^2+aA=\mu J$ and explicitly control
columns; individual incidence intersections need not be uniform.
Section 9 applies a related telescoping product to prove the Paley
bi-circulant conjecture of a recent rStation paper. We count its previously
settled small cases only as comparisons.

**Theorem 1.** Let $r,q,d,p,a$ be integers such that

$$
r\ge1,\quad q,d\ge2,\quad 1\le p<q,\quad a\ge1,
\qquad p\mid(q-1)a,\quad q\mid(d-1)a.
$$

If $r>1$, assume in addition that $p\mid a$. Put

$$
H=d(q-1)+1,\qquad k=a(rH-1),\qquad
v=\frac{rqk}{p},\qquad \mu=\frac{paH}{q}.
$$

Then there exists a DSRG with parameters

$$
(v,k,\mu,\mu-a,\mu). \tag{1}
$$

Its adjacency rank is $rH$. All positive integer multiples of (1),
and their loopless digraph complements, also exist.

The seven cases obtained from Theorem 1 are listed below. The input tuple is
$(r,q,d,p,a)$; it fixes an explicit matrix through Sections 2–3.

| Input | Parameters | Complement |
|---|---|---|
| $(1,4,3,1,2)$ | $(72,18,5,3,5)$ | $(72,53,40,39,39)$ |
| $(2,2,9,1,1)$ | $(76,19,5,4,5)$ | $(76,56,42,41,42)$ |
| $(2,2,11,1,1)$ | $(92,23,6,5,6)$ | $(92,68,51,50,51)$ |
| $(3,2,2,1,2)$ | $(96,16,3,1,3)$ | $(96,79,66,65,65)$ |
| $(3,2,5,1,1)$ | $(102,17,3,2,3)$ | $(102,84,70,69,70)$ |
| $(2,2,6,1,2)$ | $(104,26,7,5,7)$ | $(104,77,58,57,57)$ |
| $(1,5,11,2,1)$ | $(110,44,18,17,18)$ | $(110,65,39,38,39)$ |

All fourteen entries are marked `?` in the table snapshot retrieved on
16 October 2026. The supplement records these facts and the twenty-eight additional entries
from Theorem 2 in Section 7, the sixteen higher-root entries from Section 8,
the four rectangle entries from Section 10, the four square-grid
entries from Section 11, and the six order-91 entries from Section 12. It contains all thirty-six matrices. We
distinguish known instances in Sections 5 and 7 and do not claim
every parameter tuple in either infinite family as new.

## 2. One group: balanced subset incidences

Put

$$
c=\frac{(q-1)a}{p},\qquad
L=\frac{(d-1)cp}{q}.
$$

The divisibility hypotheses make $c,L$ positive integers, and
$a+L=aH/q$. The one-group construction has $qdc$ vertices.
A vertex is a triple $(s,b,i)$, where $0\le s<d$, $0\le b<q$,
and $0\le i<c$. Its label is $(s,b)$.

For each partition index $t$, give the vertex a $p$-element subset
$P_t(s,b,i)$ of $\mathbb Z/q\mathbb Z$. For its own partition, set

$$
P_s(s,b,i)=
\{b+1+((ip+h)\bmod(q-1))\pmod q:0\le h<p\}. \tag{2}
$$

For $t\ne s$, put $j_t(s)=s-\mathbf1_{s>t}$ and set

$$
P_t(s,b,i)=
\{(j_t(s)c+i)p+h\pmod q:0\le h<p\}. \tag{3}
$$

Every displayed set has $p$ distinct elements, and the own subset
excludes $b$. A source $u$ points to a target with label $(s,b)$
precisely when $b\in P_s(u)$. For $p=1$, each index gives an ordinary
partition into $q$ cells. For general $p$, the $q$ incidence sets
at an index overlap, and every vertex belongs to exactly $p$ of them.
The arc rule is binary and has no loops.

**Own-partition counts.** Fix a label $(s,b)$. As $i,h$ vary,
$ip+h$ runs through $0,\ldots,cp-1$. Since $cp=(q-1)a$, every
residue modulo $q-1$ occurs $a$ times. Hence the number of vertices
with label $(s,b)$ whose own subset contains $e$ is $a$ if
$e\ne b$, and zero if $e=b$.

**Cross-partition counts.** For $s\ne t$, let $b_{s,t}(e)$ be the
number of indices $i$ such that $e\in P_t(s,b,i)$. Formula (3)
shows that this count is independent of the label $b$. For fixed
$t$, the numbers $j_t(s)$ run through $0,\ldots,d-2$. Thus the
integers in (3), before reduction modulo $q$, concatenate exactly
$0,\ldots,(d-1)cp-1$. Since $q\mid(d-1)cp$, we have

$$
\sum_{s\ne t}b_{s,t}(e)=L
\quad\text{for every }t,e. \tag{4}
$$

The individual $b_{s,t}(e)$ may depend on $e$.

Each label has $c$ vertices, so every source has outdegree
$k_0=dpc$. The predecessors of a target labeled $(t,e)$ number

$$
(q-1)a+q\sum_{s\ne t}b_{s,t}(e)=cp+qL=dpc,
$$

which proves the same indegree.

For a two-walk from $u$ to a vertex labeled $(t,e)$, intermediate
vertices must have one of the $p$ labels selected by $u$ in each
partition. The contribution from partition $t$ is
$a(p-\mathbf1_{e\in P_t(u)})$. The other partitions contribute
$p\sum_{s\ne t}b_{s,t}(e)=pL$. Consequently

$$
(A_0^2)_{uv}=p(a+L)-a(A_0)_{uv},\qquad
A_0^2=\mu J-aA_0,\quad \mu=p(a+L). \tag{5}
$$

This includes the diagonal. It proves Theorem 1 when $r=1$.

## 3. Coupling several groups

Suppose now that $r>1$. The extra divisibility assumption $p\mid a$
makes

$$
R=\frac{q(a+L)}p=\frac{aH}p
$$

an integer. We distinguish the **position group** of a vertex from
its **label group**.

For each position group $g\in\{0,\ldots,r-1\}$, first include a
copy of every vertex from Section 2. Its subsets remain the same,
and its label becomes $(g,s,b)$.
For each other label group $h\ne g$, and each $b\in\mathbb Z/q\mathbb Z$,
include $R$ further vertices, indexed by $0\le i<R$, with label
$(h,0,b)$. For such a vertex, give every partition index $t$ the
same subset

$$
P_t=\{ip+z\pmod q:0\le z<p\}. \tag{6}
$$

All copies are distinct vertices. A source $u$ at position group $g$
points to a target labeled $(h,t,e)$ exactly when

$$
g=h\quad\text{and}\quad e\in P_t(u). \tag{7}
$$

An original vertex cannot point to itself by its own-label exclusion.
An added vertex cannot point to itself because its position and label
groups differ. Thus (7) is loopless and binary.

There are $qdc+(r-1)qR$ vertices at each position group. A label
$(h,t,e)$ with $t\ne0$ occurs $c$ times overall. A label
$(h,0,e)$ occurs $c+(r-1)R$ times. Since a source selects $p$ labels
at each of the $d$ indices, every outdegree is

$$
k=p\bigl(dc+(r-1)R\bigr)
  =a\bigl(d(q-1)+(r-1)H\bigr)=a(rH-1). \tag{8}
$$

In (6), as $i,z$ vary, each residue modulo $q$ occurs
$Rp/q=a+L$ times. Therefore, for a target labeled $(h,t,e)$,
its own-label-group predecessors in position group $h$ contribute
$k_0=dpc$. The vertices there with any other fixed label group
contribute $q(a+L)=pR$. The indegree is
$k_0+(r-1)pR=k$. The total order is

$$
v=r\bigl(qdc+(r-1)qR\bigr)=\frac{rqk}{p}. \tag{9}
$$

It remains to check two-walks. Fix a source at position group $g$
and a target with label group $h$ and local label $(t,e)$.
An intermediate vertex must have label group $g$ and position group
$h$.

If $g=h$, these are precisely the original vertices of Section 2.
Its counting argument uses only the source subsets' sizes, so it
applies equally to sources created by (6). Their contribution is
$\mu-a\mathbf1_{e\in P_t(u)}=\mu-aA_{uv}$.

If $g\ne h$, the possible intermediates are exactly the added
vertices at position group $h$ with labels $(g,0,b)$. The source
selects $p$ values of $b$, and every selected label has $a+L$
vertices containing $e$ at partition $t$. The two-walk count is
$p(a+L)=\mu$. In this case $A_{uv}=0$ by (7). Thus in both cases

$$
A^2=\mu J-aA. \tag{10}
$$

This proves all degree and two-walk conditions in Theorem 1.

The nonprincipal eigenvalues are $0,-a$. The matrix is diagonalizable:
on the all-ones direction it has eigenvalue $k$, and on its invariant
sum-zero complement it satisfies $x(x+a)=0$. Since $\operatorname{tr}A=0$,
the multiplicity of $-a$ is $k/a=rH-1$, and the rank is $rH$.
Replacing $a$ by $ma$ yields the parameter multiple for every integer
$m\ge1$. Alternatively, independent vertex duplication gives
$A\otimes J_m$, whose equation is
$(A\otimes J_m)^2=m\mu J-ma(A\otimes J_m)$.
Finally $J-I-A$ gives the stated complementary parameters. $\square$

## 4. Consequences and useful subfamilies

The proof isolates the design requirement: the sums in (4) must be
uniform, while their summands can vary. For $(q,d,p,a)=(4,3,1,2)$,
this permits a 72-vertex graph, at half the scale of the familiar
net parameter construction. For $(5,11,2,1)$, selecting two cells
at each index yields the 110-vertex graph. No geometric incidence
structure has to be found first.

When $p=1$ and $a=q$, all the divisibility conditions hold for
arbitrary $q,d\ge2$. Theorem 1 becomes

$$
\bigl(rq^2(rH-1),\ q(rH-1),\ H,\ (d-1)(q-1),\ H\bigr),
\qquad H=d(q-1)+1. \tag{11}
$$

For $r=1$ these are the known net-antiflag parameter tuples, but
(11) requires neither a net nor $d\le q$. For $d=2$, it gives

$$
\bigl(rq^2(r(2q-1)-1),\ q(r(2q-1)-1),\ 2q-1,\ q-1,\ 2q-1\bigr).
$$

The choices $(r,q)=(2,2)$ and $(3,2)$ give respectively the known
40-vertex case and the new 96-vertex case. For fixed $q,d$, the
two-walk parameters stay fixed while the order grows with $r$.

A second short subfamily takes $q=2,p=a=1,d=2s-1$, with $s\ge2$:

$$
\bigl(2r(2rs-1),\ 2rs-1,\ s,\ s-1,\ s\bigr),\qquad r\ge1. \tag{12}
$$

It includes the new 76-, 92-, and 102-vertex parameter sets.
The extra divisibility hypothesis for coupling groups is sufficient
for our construction; we do not claim it is a necessary condition
for DSRG existence outside this family.

## 5. Prior work and precise novelty scope

The matrix formulation is due to the standard DSRG theory [2,3].
The label-incidence adjacency rule is classical in the constructions
of Olmez and Song [4,5]. We use it explicitly and do not claim it
as new. The published column-basis framework of Kirkman Loom [6]
and our investigation of low-rank binary column spaces motivated
the search for partition-class columns. The new mechanism here is
balancing aggregate subset incidences and coupling groups using
uniform marginal lists.

For $r=1$, $a=q$, and $p\mid q-1$, Theorem 1 has the parameters
of Olmez–Song [4, Theorem 2.2], with their group count $d$ and
block size $p$. In particular, their result already covers
$p=1,a=q$ for arbitrary $q,d$. The net case is also covered by
[5, Corollary 3.2]. Theorem 1 permits smaller scales $a$ and
additional groups. For example, the older $q=4,d=3,p=1$ tuple
is $(144,36,10,6,10)$, whereas $a=2$ gives $(72,18,5,3,5)$.

The other $t=\mu$ family in [4, Theorem 5.1] has parameters
$(ns,\ell s,\ell\delta,(\ell-1)\delta,\ell\delta)$ with
$\delta(n-1)=\ell s$. Even allowing positive multiples, it does
not give any of the seven new tuples. It requires the integer
$\ell=\mu/(\mu-\lambda)$, ruling out the 72-, 96-, and
104-vertex cases. For each remaining case, $\mu-\lambda=1$
forces both multiplier and $\delta$ to be one; it then requires
$s=k/\mu$, which is not an integer for any of them.

Table entry T24 attributes $(40,10,3,1,3)$ to Allan van Hulst's
2025 construction. It is a known comparison instance here. Among
the one-group family tuples of order at most 110, two further
pairs still marked unknown in the source table are already published:
$(90,75,65,62,65)$ is the complement of a graph in [7], and
$(96,84,77,73,77)$ is the complement of $(96,11,4,3,1)$
constructed in September 2026 [8]. These are excluded from the
new-existence count. The latter 96-vertex pair differs from the
one in Section 1.

Our novelty comparison used the source table, the full relevant
construction sections of [4,5], the recent DSRG papers including
[8], and public rStation papers 1–7 and discussions. Exact parameter
searches in public rStation and OpenAlex found no earlier resolution
of the seven claimed pairs. Search results alone are not proofs
of priority; the specific comparisons above identify the known
subfamilies and the distinctions needed for these claims.

We do not classify isomorphism types, prove that different choices
of marginal lists give different graphs, or claim every parameter
set of Theorem 1 as a new existence result. The family supplies
explicit witnesses for the fourteen entries stated in Section 1.

## 6. Exact verification and reproducibility

The supplement uses Python 3.10 or later and the standard library.
`subset_partition_family.py` and `group_subset_family.py` implement
Sections 2–3. `universal_minus_one.py` implements the formula of Section 7
with integer arithmetic only. The independent `check_adjacency.py`
imports no constructor. It checks binary entries, looplessness, both
degree sequences, and every ordered two-walk count by traversing
out-neighbor lists.

For example:

```text
python3 group_subset_family.py --groups 1 --q 4 --parts 3 --weight 1 --step 2 --output rebuilt72.json
python3 check_adjacency.py graph72_18.txt 72 18 5 3 5
python3 check_adjacency.py graph72_18.txt 72 53 40 39 39 --complement
python3 universal_minus_one.py --v 85 --k 34 --mu 14 --output rebuilt85.json
python3 check_adjacency.py graph85_34.txt 85 34 14 13 14
python3 check_adjacency.py graph85_34.txt 85 50 30 29 30 --complement
```

`witnesses.json` specifies the constructor and complete inputs for every
matrix. The seven matrices in Section 1 use the incidence constructor;
fourteen use the universal constructor, and eight use the higher-root
constructor with the supplied exact certificates. Two use the rectangle
constructor of Section 10, and two use the square-grid constructor of
Section 11. Two use `two_rowtype_cyclic.py`, implementing Section 12;
one uses `two_rowclass_cyclic.py` and the certificate in Section 12.4. The
output `matrix_rows`, joined with LF and a final LF, regenerate every
supplied graph byte for byte. Graph filenames include both order and degree.

Separate integer matrix multiplication verified all 239 one-group
parameter tuples of order at most 110 and their complements, also
checking all incidence marginals. The group extension was checked for
18 admissible inputs with $r>1$, representing 17 distinct parameter
tuples; two larger controls with $p>1$ have orders 152 and 248. The union
of these incidence audits has 253 distinct small parameter tuples.

The universal construction was checked on all 184 table rows satisfying
$t=\mu=\lambda+1$, with both independent path counts and separate integer
matrix multiplication. Dense complementary rows are included in this
184-row count. Additionally, exact rational arithmetic verifies the two
ceiling formulas in the proof against direct cyclic interval coverage
for all 1,455 admissible $(p,q,n)$ with $q\le34$, $n\le74$. The latter
is a check of the formula, not a finite proof of the universal theorem.
The union of the incidence and universal graph audits has **367 distinct
parameter tuples** of order at most 110.

A clean extraction of the final supplement regenerates all thirty-six
witnesses and checks all seventy-two graphs and complements. No optimizer,
NumPy installation, external database, or search certificate is required.
The higher-root witnesses separately pass full path and complement checks
and integer matrix multiplication. Its two closed-form subfamilies and
period insertion were checked on 27 examples. The optional discovery
mode uses OR-Tools, but certificate reconstruction uses only the standard
library; for example:

```text
python3 higher_root_intervals.py --certificate certificate70_42.json --output rebuilt70_42.json
python3 check_adjacency.py graph70_42.txt 70 42 27 24 27
```

The audit reports support the explicit proofs, which establish the
infinite families. Original code and proof data are CC0-1.0; table facts
are attributed separately. `SHA256SUMS.json` hashes every other file.

## 7. A universal construction for $t=\mu=\lambda+1$

**Theorem 2.** Let $v,k,\mu$ be integers with $0<\mu<k<v$. A
DSRG$(v,k,\mu,\mu-1,\mu)$ exists if and only if

$$ k(k+1)=\mu v. \tag{13} $$

It can be chosen to admit a free cyclic action of order $n=\gcd(v,k)$,
with $q=v/n$ orbits. Its adjacency rank is $k+1$.

Necessity follows by taking row sums of $A^2+A=\mu J$.
For sufficiency put $p=k/n$, $q=v/n$. Since $\gcd(p,q)=1$, equation
(13) forces $q\mid pn+1$ and $\mu=pm$, where $m=(pn+1)/q$.
If $n=1$, then $q>p$ and $q\mid p+1$ force $q=p+1$ and $\mu=k$,
a contradiction. Thus $n\ge2$ and $1\le m<n$.

### 7.1 A binary interval projection

Work in $R=\mathbb Z[z]/(z^n-1)$ and write
$G=1+z+\cdots+z^{n-1}$. Choose positive lengths $s_0,\ldots,s_{p-1}$
with sum $q-1$, and sets $F_i\subseteq\mathbb Z/n\mathbb Z$ of size $m$.
Assume $0\in F_i$ and $-1,\ldots,-(s_i-1)\notin F_i$.
Sets also denote their group-ring sums. Define

$$ T_i=1+z+\cdots+z^{s_i-1},\qquad C=\sum_iT_iF_i. $$

Suppose every coefficient of $C$ is $p-1$ or $p$, and its coefficients
at $0,\ldots,\max_i s_i-1$ equal $p$. Section 7.2 constructs such sets
for every allowed input.

Index the first $q-1$ block coordinates by $(i,h)$, $0\le h<s_i$,
and the last by $*$. Define $U\in R^{q\times p}$ and $V\in R^{p\times q}$ by

$$
 U_{(i,h)}=z^h e_i^T,\qquad U_*=-\sum_iT_i e_i^T,
 \qquad V_{i,j}=F_i-\mathbf1_{j=(i,0)}.
$$

Here $e_i$ is a coordinate vector of length $p$. Let $e_*$ be the last
coordinate vector of length $q$, and set

$$ \mathcal A=UV+pG e_*\mathbf1_q^T. \tag{14} $$

The identities $VU=-I_p$ and $\mathbf1_q^TU=0$ follow immediately:
in the $(i,j)$ entry of $VU$, the common terms $T_jF_i$ cancel, leaving
$-\delta_{ij}$. Each top block of (14) is a translate of $F_i$ or
$F_i-1$. Each bottom block is $pG-C$, with $T_i$ added in column $(i,0)$.
The coverage hypothesis makes all these coefficients binary. The omitted
negative residues make each top diagonal block loopless; the last
one has zero constant coefficient because $C_0=p$.

Column degrees are $pn$ because $\mathbf1_q^TU=0$. Top row degrees
are $qm-1=pn$. The total column sum then gives degree $pn$ for the
last row as well.

For the quadratic identity put $P=UV$, $w=pe_*$ and $U_0=U(1)$.
Then $P^2=-P$, $\mathbf1^TP=0$, $G^2=nG$, and $V(1)w=pm\mathbf1_p$.
Consequently

$$
\mathcal A^2+\mathcal A
=G\bigl(pmU_0\mathbf1_p+(pn+1)w\bigr)\mathbf1_q^T
=pmGJ_q, \tag{15}
$$

since $U_0\mathbf1_p=(1,\ldots,1,-(q-1))^T$ and $pn+1=qm$.
Replace $z$ by the cyclic permutation matrix of order $n$ to obtain
$A^2+A=\mu J_v$. Equivalently, $(i,x)\to(j,y)$ when $y-x$ occurs
in the support of $\mathcal A_{ij}$. Shifting all cyclic coordinates
preserves adjacency and acts freely. The eigenvalues on the sum-zero
space are $0,-1$; trace zero gives multiplicity $k$ for $-1$ and hence
rank $k+1$.

### 7.2 Mechanical cyclic intervals

Write $q-1=ps+r$, with $0\le r<p$, and put $s_i=s+1$ for $i<r$,
$s_i=s$ otherwise. Define

$$ F_i=\{\lfloor jn/m+i/p\rfloor:0\le j<m\}. \tag{16} $$

These are $m$ distinct residues because $n/m>1$, and each includes zero.
The final cyclic gap is $\lceil n/m-i/p\rceil\ge s_i$: indeed,

$$ n/m=s+(r+1)/p-1/(pm). $$

This inequality proves that $F_i$ omits all the required negative residues.
Extend the sequence of starts to $j\in\mathbb Z$. It satisfies
$F_i(j+m)=F_i(j)+n$, so cyclic interval coverage can be counted on the line.
For an integer $x$, the number of starts of type $i$ whose interval covers
$x$ is

$$
\left\lceil\frac mn(x+1-i/p)\right\rceil-
\left\lceil\frac mn(x+1-s_i-i/p)\right\rceil.
$$

The multiset $\{i+p\mathbf1_{i<r}:0\le i<p\}$ is exactly
$\{r,\ldots,p+r-1\}$. Reindex the second sum. Using
$(q-1)/p=n/m-(m-1)/(pm)$ yields

$$
 C_x=p-\sum_{i=0}^{p-1}(\lceil a_i+\delta\rceil-\lceil a_i\rceil),
 \quad a_i=\frac mn(x+1-i/p),\quad\delta=\frac{m-1}{pn}. \tag{17}
$$

Each difference counts integers in $[a_i,a_i+\delta)$. These intervals
are disjoint, since adjacent left endpoints are spaced by
$m/(pn)>\delta$. Their total span is $(pm-1)/(pn)<1$. Thus their union
contains at most one integer, proving $C_x\in\{p-1,p\}$. For $m=1$
the intervals are empty and $C_x=p$ everywhere.

For $0\le x<s$, all $p$ intervals beginning at zero cover $x$, and no
other interval does. If $r>0$, then $m>1$; exactly $r$ of these intervals
still cover $s$, and exactly $p-r$ first positive starts equal $s$,
with the others equal to $s+1$. No second positive start occurs this early
because $n/m>s\ge1$. Hence $C_s=p$ as well. This verifies all coverage
hypotheses and completes the proof of Theorem 2. $\square$

### 7.3 Newly settled table entries and prior constructions

The following eighteen pairs are the complete list of `?` rows with
$t=\mu=\lambda+1$ in the source table snapshot. Four already appear
among the incidence instances in Section 1; they are counted once.

| Parameters | Complement |
|---|---|
| $(63,27,12,11,12)$ | $(63,35,20,19,20)$ |
| $(65,25,10,9,10)$ | $(65,39,24,23,24)$ |
| $(69,23,8,7,8)$ | $(69,45,30,29,30)$ |
| $(70,14,3,2,3)$ | $(70,55,44,43,44)$ |
| $(70,20,6,5,6)$ | $(70,49,35,34,35)$ |
| $(76,19,5,4,5)$ | $(76,56,42,41,42)$ |
| $(77,21,6,5,6)$ | $(77,55,40,39,40)$ |
| $(84,35,15,14,15)$ | $(84,48,28,27,28)$ |
| $(85,34,14,13,14)$ | $(85,50,30,29,30)$ |
| $(87,29,10,9,10)$ | $(87,57,38,37,38)$ |
| $(88,32,12,11,12)$ | $(88,55,35,34,35)$ |
| $(90,35,14,13,14)$ | $(90,54,33,32,33)$ |
| $(92,23,6,5,6)$ | $(92,68,51,50,51)$ |
| $(95,19,4,3,4)$ | $(95,75,60,59,60)$ |
| $(99,44,20,19,20)$ | $(99,54,30,29,30)$ |
| $(102,17,3,2,3)$ | $(102,84,70,69,70)$ |
| $(104,39,15,14,15)$ | $(104,64,40,39,40)$ |
| $(110,44,18,17,18)$ | $(110,65,39,38,39)$ |

The block symbols use the classical partial-sum-family framework reviewed
in [9, Section 3]. The new assertion is the universal binary realization
(14)–(17). For $p=1$ it contains every integer density ratio $v/k=q$;
the earlier telescoping rank-one construction was a special case of this
parameter theorem. For $p>1$, $p$ coupled projection directions replace
that rank-one restriction. The positive and negative interval contributions
are arranged so that the final coefficients remain zero or one.

The tournament block constructions of [10, Lemmas 4.2–4.4] contain many
known cases, but not the listed eighteen table-open pairs. The family of
[4, Theorem 5.1] with $\mu-\lambda=1$ requires $k/\mu$ to be an integer;
none of these eighteen representatives has that property. The table's T24
credits Allan van Hulst with several individual cyclic constructions,
including $(35,14,6,5,6)$; they are comparison instances here. Its source
is private correspondence, which we have not accessed.

A fresh public rStation search for each of the ten newly added sparse
pairs found no earlier resolution. One search hit for “88,32” referred to
$(405,88,32,23,18)$, not our 88-vertex case. The recent literature comparison
includes [8], the papers surveyed for Section 5, and public rStation
papers 1–7. We claim the general existence theorem and the stated eighteen
new pairs, not novelty for all 184 small instances. We do not assert that
the mechanical construction is isomorphic to any earlier realization.

## 8. Higher negative eigenvalues

The interval projection extends beyond $A^2+A=\mu J$. Multiple removed
monomials give $VU=-aI$, provided the remaining defect positions avoid
all special intervals. This sufficient theorem is not a claim of
universal existence for $a>1$.

**Theorem 3 (higher-root interval projection).** Let $a,p,q,n$ be positive integers with $ap<q$, $m=a(pn+1)/q$ be an integer with $a\le m<n$, and choose lengths $s_i$ summing to $q-1$, with $a\le s_i\le n$. Let each $F_i\subseteq\mathbb Z_n$ have size $m$, set $T_i=1+\cdots+z^{s_i-1}$, and define
$$H_i=\{h:0\le h<s_i,\ -h\in F_i\},\qquad C=\sum_iT_iF_i.$$
Require $|H_i|=a$, each coefficient of $C$ to be $ap-1$ or $ap$, and $B=apG-C$ to be disjoint from $z^{-h}T_i$ for every $h\in H_i$.

Use the matrix $U$ from Section 7.1. Row $i$ of $V$ is $F_i$ everywhere, except column $(i,h)$ for $h\in H_i$, where it is $F_i-z^{-h}$. Then $VU=-aI_p$ and $\mathbf1^TU=0$. Put
$$\mathcal A=UV+apG e_*\mathbf1^T.$$
Top blocks are binary translates of $F_i$ with at most one element removed; bottom blocks are $B$, with $z^{-h}T_i$ added in a special column. Disjointness makes them binary. By definition of $H_i$, exactly every possible top diagonal loop is removed. Also $C_0=\sum|H_i|=ap$, so the last diagonal block is loopless.

Every column degree is $apn$, top row degrees are $qm-a=apn$, and the last follows by summing columns. For $w=ap e_*$ and $U_0=U(1)$,
$$\mathcal A^2+a\mathcal A
=G\bigl(apmU_0\mathbf1_p+(apn+a)w\bigr)\mathbf1^T
=apmGJ_q.$$
This proves parameters $(qn,apn,apm,apm-a,apm)$.

**Corollary 3.1 (dense subfamily).** Let $p=1,q=a+1,n=(a+1)h-1,m=ah$, with $a\ge2,h\ge a$, and take
$$F=\mathbb Z_n\setminus\{a,2a,\ldots,(h-1)a\}.$$
Here $s=a$, $H=\{0,\ldots,a-1\}$, and the defect set is the interval $B=\{a,\ldots,ah-1\}$, disjoint from every special interval. This gives
$$((a+1)((a+1)h-1),\ a((a+1)h-1),\ a^2h,\ a^2h-a,\ a^2h).$$
The new order76/92 cases are $(a,h)=(3,5),(3,6)$; order95/degree76 is $(4,4)$.

**Corollary 3.2 (negative root two).** Take $a=2,p=1,q\ge3,n=qh-1,m=2h$, $h\ge2$, and
$$F=\{qj+b:0\le j<h,\ b\in\{0,1\}\}.$$
Then $s=q-1$, $H=\{0,q-2\}$, and
$$B=\bigcup_{j=1}^{h-1}\{qj-1,qj\},$$
which avoids both special intervals. It gives
$$(q(qh-1),\ 2(qh-1),\ 4h,\ 4h-2,\ 4h).$$
The new $(91,26,8,6,8)$ and $(95,38,16,14,16)$ correspond to $(q,h)=(7,2),(5,4)$.

**Corollary 3.3 (period insertion).** When $p=1$ and $n\ge2(q-1)-1$, any certificate extends to all lengths $n+uq$, increasing $m$ by $ua$. Encode $F$ as a cyclic binary word and cut after index $q-2$, outside the protected offsets $[-(q-2),q-2]$ around zero. The state $W$ before the cut has length $q-2$ and weight $a,a-1$, or$a-2$. Choose two bits $E$ so $WE$ has weight $a$, and insert $EW$. Every newly created $(q-1)$-window is a window in a $q$-periodic word of weight $a$, so its weight is$a$ or$a-1$. The ending state is again $W$, preserving all old coverage values. The protected origin offsets retain both their bits and coverage, preserving every special-interval condition. Repeat the insertion. This includes the family
$$(70+25u,42+15u,27+9u,24+9u,27+9u),\qquad u\ge0,$$
from the order-70 certificate below, with the order-95 degree-57 parameters as its next member. The displayed order-95 witness need not coincide with the inserted witness; no isomorphism claim is made.


**Corollary 3.4 (synchronized periods).** In Theorem 3 let
$S=\max_i s_i$ and $n\ge2S-1$. Encode each $F_i$ as a cyclic binary word,
and cut all words after index $S-1$. Suppose there are binary words
$P_i$ of length $q$ and weight $ap$ such that

$$\sum_i\sum_{h=0}^{s_i-1}(P_i)_{x-h}\in\{ap-1,ap\}
\quad\text{for every }x\pmod q,$$

and the last $s_i-1$ bits of $P_i$ agree with the state of $F_i$ immediately
before the cut. Inserting $P_i$ in each word can then be repeated any
number $u\ge0$ of times. It gives parameters

$$(qn+q^2u,\ apn+apqu,\ apm+(ap)^2u,\ apm-a+(ap)^2u,\ apm+(ap)^2u).$$

Indeed, each new window is a window in a periodic sequence of the
$P_i$, because the states before and after each insertion agree. All old
coverage values are retained. The insertion lies outside the protected
origin offsets $[-S+1,S-1]$, so each $H_i$ and each special interval
retains its bits and coverage. Thus every hypothesis of Theorem 3 remains
valid. Each support size increases by $ap$, and
$q(m+ap)=a(p(n+q)+1)$ preserves the degree equation.

For the order-77 certificate below, use $S=4$ and

$$\begin{aligned}
P_0&=01011010101,\\
P_1&=01010101101,\\
P_2&=11010101010.
\end{aligned}$$

Coordinates are listed from zero to ten. Equivalently, their supports are
$\{\lfloor(11j+2i+7)/6\rfloor\pmod {11}:0\le j<6\}$.
All three weights are six; their required tails are $101$, $01$, and $10$.
Their combined coverage vector is $(5,6,5,6,5,6,5,6,5,6,5)$.
These finite checks prove the infinite family

$$(77+121u,42+66u,24+36u,22+36u,24+36u),\qquad u\ge0.$$

The supplement stores the period words in `certificate77_42.json`.
For example, `higher_root_intervals.py --certificate certificate77_42.json
--steps 2 --output rebuilt319.json` constructs the order-319 member.
Independent path counts and integer matrix multiplication checked orders
198, 319, and 440 and their complements. No search is required to reproduce
the family.


The eight additional new cases have the following exact certificates.
Here $Z$ denotes the entire cyclic residue set for that row; multiple
support sets are listed in index order. Every entry can be checked by
integer interval counting before constructing an adjacency matrix.

| Parameters | $(a,p,q,n)$ | Lengths | Supports $F_i$ |
|---|---|---|---|
| $(70,42,27,24,27)$ | $(3,1,5,14)$ | $(4)$ | $Z\setminus\{3,5,7,9,13\}$ |
| $(76,57,45,42,45)$ | $(3,1,4,19)$ | $(3)$ | $Z\setminus\{3,6,11,14\}$ |
| $(77,42,24,22,24)$ | $(2,3,11,7)$ | $(4,3,3)$ | $Z\setminus\{0,2,4\}; Z\setminus\{2,4,6\}; Z\setminus\{1,3,6\}$ |
| $(91,26,8,6,8)$ | $(2,1,7,13)$ | $(6)$ | $\{1,5,8,11\}$ |
| $(92,69,54,51,54)$ | $(3,1,4,23)$ | $(3)$ | $Z\setminus\{6,9,12,15,18\}$ |
| $(95,76,64,60,64)$ | $(4,1,5,19)$ | $(4)$ | $Z\setminus\{4,8,12\}$ |
| $(95,57,36,33,36)$ | $(3,1,5,19)$ | $(4)$ | $Z\setminus\{0,3,5,8,9,12,15\}$ |
| $(95,38,16,14,16)$ | $(2,1,5,19)$ | $(4)$ | $\{1,2,5,6,9,13,16,17\}$ |

All eight tuples and complements are marked unknown in the archived table.
The known $(45,18,8,6,8)$ from [7] is an additional positive control and
is not counted again. Primary and complementary parameter searches in
public rStation, the earlier manuscript comparisons, and the construction
literature cited above found no preceding resolution of these eight pairs.
The small linear search used to obtain the displayed supports is a
discovery method only: these fixed integer certificates, the deterministic
constructor, and the proof of Theorem 3 establish existence.

The three dense cases of Corollary 3.1 and the two cases of Corollary 3.2
have the stated closed forms. Corollary 3.3 supplies an infinite family
through the remaining order-70 and order-95 degree-57 parameters.
Corollary 3.4 extends the mixed-length order-77 example by synchronized
period insertion. Thus each of the eight new parameter sets belongs to
an explicit infinite family. Independent vertex duplication gives all positive
parameter multiples because $t=\mu$, as proved in Section 3.

## 9. A telescoping near-factorization and the Paley conjecture

A related product also proves the conjecture in [11, Section 4]. That
paper supplies the Paley diagonal-block mechanism, the Fourier criterion,
and new cyclotomic witnesses at orders 58 and 106. Our addition is an
explicit near-factorization valid for every prime in its stated series.
Those small parameter cases are not included in our new-resolution count.

**Theorem 4.** Let $a\ge0$ and suppose $P=(2a+1)^2+4$ is prime. Put
$h=(P-1)/2$ and $\ell=h-a$. A DSRG exists with parameters

$$ (2P,P-1-a,h+a^2,h-1-a,h-a). $$

In $\mathbb Z_P$, with division by two taken modulo $P$, set

$$ X=\{j-(\ell-1)/2:0\le j<\ell\},\qquad Y=\ell X. $$

Then $\ell^2+1=(a^2+1)P$, so $\gcd(\ell,P)=1$ and both sets have size
$\ell$. With $G=\sum_{j=0}^{P-1}z^j$, unique base-$\ell$ expansion gives

$$
 XY=z^{-(\ell^2-1)/2}\sum_{j=0}^{\ell^2-1}z^j
   =z\bigl((a^2+1)G-z^{-1}\bigr)=(a^2+1)G-1. \tag{18}
$$

Let $Q,N$ denote the nonzero squares and nonsquares in $\mathbb Z_P$.
Use the block symbol $\left(\begin{smallmatrix}N&X\\Y&Q\end{smallmatrix}\right)$.
Lemma 1 of [11] immediately proves the claimed graph parameters. A direct
check uses $N+Q=G-1$ and $NQ=(P-1)(G-1)/4$. Together with (18), they give
$A^2+A=a(a+1)I+(h-a)J$; row and column degrees are $h+\ell=P-1-a$.
The diagonal blocks omit zero and $0<h+a^2<P-1-a$. $\square$

This is a theorem conditional on primality, not a claim that infinitely
many primes have the form $(2a+1)^2+4$. The sets are symmetric, but need
not be the cyclotomic unions used in [11]. Exact convolution, full path
counts and complement checks, and separate integer matrix multiplication
passed for $a=0,1,2,3,6,7,8$. The last three graphs have parameters
$(346,166,122,79,80)$, $(458,221,163,106,107)$ and
$(586,284,210,137,138)$. `paley_interval_family.py` reproduces them.
No isomorphism classification or additional small-table novelty is claimed.

## 10. Two rectangle families with restricted eigenvalues 1 and −2

The two-layer mechanism in Section 9 also works with complementary diagonal
supports other than the quadratic residues. This produces two unconditional
infinite families and settles two further complementary pairs.

**Theorem 5.** Choose either $d=1$, $r\ge2$, or $d=3$, $r\ge1$ with
$3\nmid r$, and put $n=r^2+(r+d)^2$. There exists a vertex-transitive DSRG

$$\left(2n,n-2,\frac{n+1}{2},\frac{n-5}{2},\frac{n-3}{2}\right). \tag{19}$$

It admits a transitive subgroup $C_n\rtimes C_4$ of automorphisms. Its
complement also exists. In particular, the theorem supplies

| $(r,d)$ | Parameters | Complement |
|---|---|---|
| $(2,3)$ | $(58,27,15,12,13)$ | $(58,30,18,15,16)$ |
| $(4,1)$ | $(82,39,21,18,19)$ | $(82,42,24,21,22)$ |

All four entries are marked unknown in the source table. The cases of
orders 26, 34 and 50 are already known, recorded as T13, M9 and M10 in
[1]; we do not count them again. In particular, the new order-58 and
order-82 pairs differ from the respective pairs in [11].

### 10.1 The rectangles and their binary coefficients

Work in $R=\mathbb Z[z]/(z^n-1)$ and put $b=r$, $c=r+d$, $w=2r+d$,
$B=z^b+z^{-b}$ and $C=z^c+z^{-c}$. Define

$$F=\begin{cases}
z^{1-r}\left(\sum_{h=0}^{r-2}z^h\right)
          \left(\sum_{j=0}^{r+1}z^{jw}\right),&d=1,\\[2mm]
z^{3-r}\left(\sum_{h=0}^{r}z^{3h}\right)
          \left(\sum_{j=0}^{r+1}z^{jw}\right),&d=3.
\end{cases} \tag{20}$$

Each product has $(n-5)/2$ terms, and no two coincide modulo $n$.
For $d=1$, the interval starts $0,w,\ldots,(r+1)w$ have cyclic gaps at
least $r$: the final start is $r$ modulo $n$, and the remaining gaps are
$r+1$ or $w$. Their interval lengths are $r-1$.

For $d=3$, equality of two terms would imply
$3u+wv=tn$ with $|u|\le r$ and $|v|\le r+1$. The absolute bound is
$n+2r-6<2n$, so $t\in\{-1,0,1\}$. If $t=0$, then
$\gcd(3,w)=1$ forces either $u=v=0$ or $|u|\ge w>r$.
If $t=1$, the inequality
$n-3u\ge n-3r=wr+9$ gives $v\ge r+1$. Thus $v=r+1$ and
$3u=r+6$, contradicting $3\nmid r$. Negation handles $t=-1$.
This proves that $F$ has binary coefficients in both families.

Each rectangle is inverse-closed. Indeed, twice its center is
$2(1-r)+(r-2)+(r+1)w=n$ for $d=1$, and
$2(3-r)+3r+(r+1)w=n$ for $d=3$. Reflection through the center therefore
negates every exponent modulo $n$.

### 10.2 The product identity and the graph

Since $\gcd(r,n)=1$, the residue $i=c/b$ is defined modulo $n$ and
satisfies $i^2=-1$. Multiplication of exponents by $i$ exchanges $B$ and
$C$. The finite geometric sums in (20) give

$$(C-B)F=B^2-C-2. \tag{21}$$

To see this directly, factor
$C-B=z^{-c}(1-z^{c-b})(1-z^{c+b})$.
For $d=1$, use $(r+2)w=n+3r+1$; for $d=3$, use
$(r+2)w=n+r-3$. After cancellation the product in either case is
$z^{-2b}(1-z^{2b-c})(1-z^{2b+c})$, which is the right side of (21).

Let $H=F(z^i)$. Apply the exponent automorphism to (21) and add the
resulting identities. They give

$$(C-B)(F+H+B+C+1)=0.$$

Both $c-b=d$ and $c+b=w$ are units modulo $n$. This follows immediately
for $d=1$; for $d=3$, use $3\nmid r$ and $2n=w^2+9$.
Consequently the kernel of multiplication by $C-B$ over
$\mathbb Q[C_n]$ consists exactly of the constant multiples of $G$:
its two factors $1-z^d$ and $1-z^w$ vanish only at the trivial character.
Augmentation now gives

$$F+H+B+C+1=G. \tag{22}$$

All five summands have nonnegative coefficients. Thus their supports
partition the cyclic group. Set

$$D=F+B,\quad E=H+C,\quad X=F+1,\quad Y=H+1.$$

Then $D+E=G-1$, and expansion of (21), using (22), gives

$$XY=DE+2-G. \tag{23}$$

The symbol
$\mathcal A=\left(\begin{smallmatrix}D&X\\Y&E\end{smallmatrix}\right)$
has binary blocks and loopless diagonal blocks. Every row and column has
degree $(n-1)/2+(n-3)/2=n-2$. Equations (22)–(23) yield

$$\mathcal A^2+\mathcal A=2I_2+\frac{n-3}{2}GJ_2.$$

Replacing $z$ by an $n$-cycle proves (19). Since $n>5$, its mutual degree
$(n+1)/2$ is strictly less than its degree $n-2$.

Global translations preserve adjacency. Also
$(x,\ell)\mapsto(ix,1-\ell)$ exchanges $D,E$ and $X,Y$, since
$F=-F$ and $i^2=-1$. It is an automorphism of order four. These maps
generate a subgroup of order $4n$ acting transitively on the $2n$
vertices. We do not identify the full automorphism group. $\square$

### 10.3 Reproduction and relation to earlier work

The partial-sum-family framework is classical [9], and [11, Lemma 1]
provided the motivating two-layer criterion. Here the diagonal blocks
vary with the rectangle; equations (20)–(23) give explicit binary
realizations with no primality hypothesis. The formulas are the existence
proof; Fourier inversion was used only to discover the first witness.

`quarter_turn_family.py` uses only the standard library. For example:

```text
python3 quarter_turn_family.py --r 2 --d 3 --output rebuilt58.json
python3 check_adjacency.py graph58_27.txt 58 27 15 12 13
python3 quarter_turn_family.py --r 4 --d 1 --output rebuilt82.json
python3 check_adjacency.py graph82_39.txt 82 39 21 18 19
```

Nine members, including larger orders 122, 130, 178 and 298, passed full
path counts and separate integer matrix multiplication, with complements.
An independent cyclic-integration algorithm recovered all 99 admissible
rectangles with $r\le60$. The table, the construction literature cited
above, recent papers [8,11], and exact public parameter searches showed
no previous resolution of the four listed entries. We make no claim to
new existence for every member of either infinite family. Positive
parameter multiplication from Section 3 applies to the $t=\mu$ families;
(19) has $t-\mu=2$.

## 11. Two square-grid families with restricted eigenvalues 1 and −2

The preceding rectangle construction does not cover layer sizes 37 or 53.
A different pair of rational functions gives binary symbols at both orders
and extends them to two unconditional families.

**Theorem 6.** For every integer $b\ge3$, put
\[
 n=\begin{cases}b^2+1,&b\text{ even},\\b^2+4,&b\text{ odd}.\end{cases}
\]
There is a vertex-transitive DSRG with parameters
\[
 (2n,n-2,(n+1)/2,(n-5)/2,(n-3)/2).
\]
In particular $b=6,7$ give the previously open pairs

| primary parameters | complementary parameters | input |
|---|---|---|
| $(74,35,19,16,17)$ | $(74,38,22,19,20)$ | $b=6$ |
| $(106,51,27,24,25)$ | $(106,54,30,27,28)$ | $b=7$ |

There is no primality hypothesis. The transitive subgroup is
$C_n\rtimes C_4$, as in Section 10. Its order is $4n$.

### 11.1 A rational identity

For two indeterminates $z,w$, let $f^*(z,w)=f(z^{-1},w^{-1})$ and
$\tau f(z,w)=f(w,z^{-1})$. Define
\[
 K=\frac{w^3z-2w^2z+w^2+wz^3-2wz^2+z^2}
 {wz(w-1)(z-1)},\qquad
 T=\frac{(w^2+z^2)(wz+1)}{wz(w+1)(z+1)},
\]
and $\mathcal D=(K+T)/2$, $\mathcal X=(K-T)/2$.
The following are identities of rational functions:
\[
 \mathcal D^*=\mathcal D,\quad \mathcal X^*=\mathcal X,\quad
 \mathcal D+\tau\mathcal D=-1,\quad
 \mathcal X\tau\mathcal X-\mathcal D\tau\mathcal D=2.       \tag{25}
\]
They follow by substituting $w,z^{-1}$ and clearing the displayed
denominators. The supplement also checks these as formal Laurent polynomial
identities with integer coefficients; it does not substitute sample numbers.

Suppose binary, inverse-closed supports $D,X\subseteq C_n$ have sizes
$(n-1)/2,(n-3)/2$, with $0\notin D$, and their character evaluations
are $\mathcal D(z,w),\mathcal X(z,w)$ at every nontrivial $n$th root
$z$, with $w=z^i$ and $i^2\equiv-1\pmod n$. Put $E=iD$, $Y=iX$.
The nontrivial characters in (25), followed by augmentation, give
\[
 D+E=G-1,\qquad XY=DE+2-G,\qquad G=\sum_{x\in C_n}z^x.     \tag{26}
\]
Indeed the augmentation of $XY-DE$ is $((n-3)/2)^2-((n-1)/2)^2=2-n$.
All denominators are nonzero here: $n$ is odd, $i$ is a unit, and a
nontrivial character cannot have $z=1$ or $w=1$.
The two-layer criterion in Section 10 now proves the DSRG equation.
It remains to give the binary supports with these character evaluations.

### 11.2 Even $b$: alternating strips

Let $b=2s\ge4$, $n=b^2+1$ and $i=b$. In integer representatives define
\[
\begin{aligned}
 D_+&=\{1,\ldots,b-1\}\ \cup
 \bigcup_{j=1}^{s-1}\{jb+2h+(j\bmod2):1\le h<s\},\\
 X_+&=\{2,\ldots,b-1\}\ \cup
 \bigcup_{j=1}^{s-1}\{jb+2h+1-(j\bmod2):1\le h<s\},\\
 D&=D_+\cup(-D_+),\qquad X=\{0\}\cup X_+\cup(-X_+).
\end{aligned}                                                    \tag{27}
\]
All positive representatives lie between 1 and $(n-1)/2-1$; the strips
are disjoint. Thus $D$ and $X$ are binary, inverse-closed, and have
sizes $2s^2=(n-1)/2$ and $2s^2-1=(n-3)/2$. In particular $0\notin D$.

Here is an explicit geometric-sum verification of their evaluations.
For a nontrivial $n$th root $z$, put $w=z^b$, $u=w^s$ and
$\epsilon=(-1)^s$. Then $u^2=z^{-1}$. Write
\[
 P=\frac{z-w}{1-z},\quad
 L_0=\frac{(z^2-w)(w-u)}{(1-z)(1-w)},\quad
 M_0=\frac{(w-z^2)(w+\epsilon u)}{(1+z)(1+w)}.
\]
The positive strip sums in (27) are
$D_+=P+(L_0+M_0)/2$ and $X_+=P-z+(L_0-M_0)/2$.
The terms containing $u$ cancel from $L_0+L_0^*$ and $M_0+M_0^*$,
because $u^2=z^{-1}$. Consequently these sums equal $L+L^*$ and
$M+M^*$, where
\[
 L=\frac{(z^2-w)w}{(1-z)(1-w)},\qquad
 M=\frac{(w-z^2)w}{(1+z)(1+w)}.
\]
It follows directly that
\[
 D=P+P^*+(L+L^*+M+M^*)/2=\mathcal D,
\]
\[
 X=1+P-z+(P-z)^*+(L+L^*-M-M^*)/2=\mathcal X.
\]
The last equalities are rational identities, also checked formally in the
supplement. This proves (26) for the even family.

### 11.3 Odd $b$: rectangular grid pieces

Let $b=2s+1\ge3$, $n=b^2+4$ and $i=(n-b)/2$. Then $i^2=-1$ modulo
$n$, $z^b=w^{-2}$ and $w^b=z^2$ when $w=z^i$.
All the following sets are reduced modulo $n$:
\[
\begin{aligned}
 F&=\{2x+by:0\le x\le s,\ -s\le y\le-1\},\\
 U&=\{2x+by:-s\le x\le-1,\ 1-s\le y\le0\},\\
 V&=\{2s+by:-s\le y\le-2\},\qquad H=\{i-1,1-i\},\\
 D&=F\cup(-F)\cup H,\\
 X&=\{0\}\cup U\cup(-U)\cup V\cup(-V)\cup H.
\end{aligned}                                                    \tag{28}
\]
The set $V$ is empty when $s=1$.

The map $(x,y)\mapsto2x+by$ is injective on the square
$-s\le x,y\le s$. Indeed, a collision would give
$2\Delta x+b\Delta y=kn$ with $|\Delta x|,|\Delta y|\le b-1$.
The absolute bound is less than $2n$, so $|k|\le1$.
For $k=0$, a nonzero solution requires $|\Delta x|\ge b$.
For $k=1$, parity forces $\Delta y$ odd, hence $\Delta y\le b-2$,
and $2\Delta x\ge2b+4$, again impossible. Negation treats $k=-1$.

The four missing residues of this square are $\pm(i-1),\pm(i+1)$.
For example, $bs=i-2$. If $i\pm1=2x+by$ without wrapping,
$y=s$ gives an odd value for $2x$, while $y\le s-1$ gives
$2x\ge b+1>2s$. The wrapped representatives $i\pm1-n$ lie below
the square's minimum $-s(b+2)$. Negation treats the other two residues.
Counting finishes the assertion because the square has $b^2=n-4$ points.

The grid pieces in each union (28) are disjoint, and $H$ is outside the
square. Therefore $D$ is binary of size $2s(s+1)+2=(n-1)/2$;
$X$ is binary of size $1+2s^2+2(s-1)+2=(n-3)/2$.
They are inverse-closed and $0\notin D$.

Their evaluations have short geometric forms:
\[
 F=\frac{(z^2-w)(w^2-z)}{w(w^2-1)(1-z^2)},\quad
 U=\frac{(zw^2-1)(z^2-w)}{w(w^2-1)(1-z^2)},\quad
 V=\frac{z^2-w^3}{zw(w^2-1)},\quad H=w/z+z/w.
\]
These follow from $z^b=w^{-2}$ and $w^b=z^2$; the formula for $V$
also vanishes for $b=3$ after those relations are imposed.
Substitution and collection give the rational identities
\[
 F+F^*+H=\mathcal D,\qquad
 1+U+U^*+V+V^*+H=\mathcal X.
\]
Equation (26) follows again. In both families translation and
$(x,\ell)\mapsto(ix,1-\ell)$ generate the stated transitive subgroup.
Since $n>5$, the graphs are properly directed. This proves Theorem 6.

### 11.4 Verification and novelty

`checkerboard_square_family.py` is a standard-library constructor for
both formulas. `rational_quarter_turn.py` independently recovers the
coefficients by integrating two cyclic difference equations.
`audit_rational_quarter_turn.py` checks eight formal Laurent polynomial
identities and compares both constructors for every $3\le b\le60$.
Exact path and separate integer-matrix checks cover $b=3,\ldots,10$
and their complements. To reproduce the two new graphs:

```
python3 checkerboard_square_family.py 6 --output rebuilt74.json
python3 checkerboard_square_family.py 7 --output rebuilt106.json
python3 audit_rational_quarter_turn.py --output square_families_rechecked.json
```

The order-26 and order-34 parameters are known controls, and the order-58
parameters coincide with Theorem 5; none is counted again. All four new
entries are marked `?` in the source table [1]. Exact tuple searches,
the recent construction papers [8,12], and public rStation material revealed
no earlier construction as of 2026-10-17. The two-layer method is related
to the partial-sum-family framework [9] and the Paley criterion [11];
the diagonal supports here vary with the grid and the proof does not
require a Paley difference set. Positive parameter multiplication is not
asserted for these $t\ne\mu$ families.

## 12. Two block-row types and a balanced cycle coloring

**Theorem 7.** Let $q\ge2$ and $1\le a<q$ be integers with $3a\le2q$.
Then a DSRG exists with parameters

$$
(q(2q-1),\ a(2q-1),\ 2a^2,\ 2a^2-a,\ 2a^2).
$$

The construction is deterministic, uses no field or primality assumption,
and has a free cyclic action of order $2q-1$. It also gives all positive
parameter multiples and complements. The new table cases are
$(91,39,18,15,18)$ and $(91,52,32,28,32)$, and their complements
$(91,51,30,29,28)$ and $(91,38,18,17,15)$. The case $(45,18,8,6,8)$
is in our earlier paper [7]; $(91,26,8,6,8)$ is already covered by the
higher-root interval construction in this manuscript. Neither is counted again.

### 12.1. A sufficient block certificate

Write $n=2q-1$, $b=q-1-a$, $H=1+z$, and
$G=\sum_{j=0}^{n-1}z^j$ in $\mathbb Z[C_n]$. Identify a subset with
its indicator polynomial. An independent set of the cycle $C_n$ means a
set containing no two residues that differ by one.

Choose an independent set $D_0$ of size $a$ avoiding zero, $b$ independent
sets $F_1,\ldots,F_b$ of size $a$ avoiding both $0$ and $-1$, and $a$
independent sets $T_1,\ldots,T_a$ of size $b+1$, each containing exactly
one of $0,-1$. Require

$$
H\left(\sum_{j=1}^a T_j-\sum_{j=1}^b F_j\right)=D_0+a. \tag{12.1}
$$

Use the $q-1$ special-row supports

$$
(B_1,\ldots,B_{q-1})=(F_1,\ldots,F_b,G-T_1,\ldots,G-T_a).
$$

For small supports put $D_j=HB_j$; for large supports put $D_j=HB_j-G$.
These are binary and omit zero. Also $HD_0$ is binary, and (12.1) gives

$$
\sum_{j=0}^{q-1}D_j=a(G-1). \tag{12.2}
$$

The block symbol is

$$
M=\begin{pmatrix}
D_0&B_1&\cdots&B_{q-1}\\
HD_0&D_1&\cdots&D_{q-1}\\
\vdots&\vdots&&\vdots\\
HD_0&D_1&\cdots&D_{q-1}
\end{pmatrix}. \tag{12.3}
$$

Replace each entry by its circulant, with $(x,i)\to(y,j)$ if the
coefficient of $z^{y-x}$ in $M_{ij}$ is one. This gives a loopless
binary matrix. The row-sum quotient has first row

$$
(a,\underbrace{a,\ldots,a}_{b},
\underbrace{a+q-1,\ldots,a+q-1}_{a})
$$

and all other rows

$$
(2a,\underbrace{2a,\ldots,2a}_{b},
\underbrace{2a-1,\ldots,2a-1}_{a}).
$$

Every row and column sum equals $an$.

Here is a direct group-ring verification, so no spectral approximation is
involved. Let $u=(1,H,\ldots,H)^T$, $r=(D_0,B_1,\ldots,B_{q-1})$,
$v=(0,1,\ldots,1)^T$, and let $e$ be the row vector indicating the $a$
large columns. Thus $M=ur-Gve$. Put $u_0=u(1)$ and $r_0=r(1)$.
By (12.2), $ru=2aG-a$. Moreover

$$
G^2=nG,\quad (rv)(1)=a(n-1),\quad (eu)(1)=2a,\quad ev=a.
$$

Expanding and collecting terms gives

$$
M^2+aM=aG(u_0-v)\bigl(2r_0-(n-1)e\bigr).
$$

The two vectors on the right are respectively $\mathbf1$ and
$2a\mathbf1^T$. Hence

$$
M^2+aM=2a^2GJ_q,
$$

which becomes the asserted DSRG identity after circulant substitution.

### 12.2. Constructing the supports

Put $l=\lceil a/2\rceil$ and $r=\lfloor a/2\rfloor$. Define

$$
D_0=\{1,3,\ldots,2l-1\}
\cup\{n-1,n-3,\ldots,n-(2r-1)\}. \tag{12.4}
$$

An empty second set is permitted. The two intervals are separated and
$D_0$ is independent, has size $a$, and omits zero. Define an integer
coefficient vector $s$ by

$$
\begin{aligned}
s_{2i}&=\max(l-i,0)+\max(r-(q-1-i),0),&&0\le i<q,\\
s_{2i+1}&=-\max(l-1-i,0)-\max(r-1-(q-2-i),0),&&0\le i<q-1.
\end{aligned} \tag{12.5}
$$

Direct addition of neighboring coefficients yields

$$
s_x+s_{x-1}=\mathbf1_{D_0}(x)+a\mathbf1_{\{0\}}(x),\qquad
\sum_xs_x=a. \tag{12.6}
$$

All even coefficients are nonnegative and all odd coefficients nonpositive.
For each odd $x\in\{1,3,\ldots,n-2\}$ choose an integer $f_x$ with

$$
-s_x\le f_x\le
\min\bigl(b,a-\mathbf1_{\{x\in D_0\text{ or }x+1\in D_0\}}\bigr),
\qquad \sum_{x\text{ odd}}f_x=ab. \tag{12.7}
$$

Set $f_x=0$ at even positions. Such integers exist, and can be selected
greedily starting at their lower bounds. Indeed, $3a\le2q$ is equivalent
to $b\ge l-1$, which puts every lower bound below its upper bound.
Their lower-bound sum is

$$
\frac{l(l-1)+r(r-1)}2\le ab.
$$

Exactly $a$ odd positions have the indicator in (12.7) equal to one.
If $b\le a-1$, the sum of upper bounds is $(a+b)b\ge ab$.
If $b\ge a$, it is $a(a-1)+ba\ge ab$. Integer intervals have every
intermediate total, proving (12.7).

Assign the $f_x$ occurrences at successive odd positions cyclically to
$b$ labels, continuing the assignment counter between positions. Because
$f_x\le b$, a label never repeats at one position; because the total is
$ab$, every label receives $a$ positions. All odd positions form an
independent set of $C_n$ and omit $0,-1$. This supplies the sets $F_j$.
When $b=0$, there are no such sets and no assignment is needed.

Now put $t_x=f_x+s_x$. These are nonnegative integers with

$$
\sum_xt_x=a(b+1),\qquad t_0=l,\qquad t_{n-1}=r,
\qquad t_x+t_{x-1}\le a. \tag{12.8}
$$

The last assertion at $x=0$ is equality; elsewhere it follows from
(12.6) and (12.7).

We color these occurrences with $a$ colors, each color forming an
independent set. Partition the colors into groups of sizes $l,r$.
At even position $2i$ use the first $\max(l-i,0)$ colors from the first
group and the first $\max(r-(q-1-i),0)$ from the second. The two nonempty
chains are separated by at least one empty even position. Thus at any
odd position the two neighboring color sets are nested, or one is empty;
their union has size equal to the larger neighboring multiplicity.
By (12.8), at least $t_x$ colors are available. Assign any $t_x$ of them.
Across the edge joining $0$ and $n-1$, the two color groups are disjoint.
The result is a proper coloring of all occurrences.

The color classes may initially have different sizes. They can be balanced
by alternating-path exchanges. For two chosen colors, put an edge between
occurrences at the same or neighboring positions. If both colors occur at
one position, they form an isolated edge. Otherwise each component is an
alternating path or an even cycle, since each color is independent.
Each component therefore has color-size difference at most one. If one
color exceeds another in size by at least two, some path has one extra
occurrence of the larger color. Interchange its colors. This preserves
proper coloring and reduces the sum of squared class sizes. Repeating
terminates with all class sizes differing by at most one. Their total is
$a(b+1)$, so every class has size exactly $b+1$.

The $a$ occurrences at $0,n-1$ form a clique, so every color occurs
exactly once there, including after the exchanges. Consequently the
balanced color classes are the required sets $T_1,\ldots,T_a$.
Their aggregate difference from the $F_j$ is $s$, and (12.6) proves (12.1).
This completes the theorem.

### 12.3. Scope, exact checks and reproduction

The inequality $3a\le2q$ is also necessary for this support certificate,
though no graph nonexistence is implied outside it. For any certificate,
write $s=\sum T_j-\sum F_j$. Since all $F_j$ omit $0,-1$, we have
$s_0+s_{-1}=a$. Every coefficient of $s$ is at least $-b$, so (12.1) at
$1$ and $-1$ gives $s_0\le b+1$ and $s_{-1}\le b+1$. Thus
$a\le2(b+1)$, equivalently $3a\le2q$.

`two_rowtype_cyclic.py` implements (12.4)–(12.8), the finite alternating-path
balancing algorithm, and (12.3), using only the standard library. It checks
all support identities before assembling the graph. Examples:

```bash
python3 two_rowtype_cyclic.py --family 7 3 --output graph91_39.txt
python3 two_rowtype_cyclic.py --family 7 4 --output graph91_52.txt
python3 check_adjacency.py graph91_39.txt 91 39 18 15 18
python3 check_adjacency.py graph91_39.txt 91 51 30 29 28 --complement
python3 check_adjacency.py graph91_52.txt 91 52 32 28 32
python3 check_adjacency.py graph91_52.txt 91 38 18 17 15 --complement
```

The constructor checked all 1,200 admissible $(q,a)$ with $2\le q\le60$.
Twenty-three members, namely all admissible inputs through $q=8$ and
$(q,a)=(9,6),(12,8)$, and their complements passed independent direct
integer path enumeration and separate signed-64-bit matrix multiplication.
This finite audit supplements the proof; it is not its basis.

All four new entries are marked `?` in a source-table refresh [1] on
17 October 2026 at 04:03 UTC. Exact-tuple OpenAlex and public-rStation
searches, and the recent construction papers [8,12], revealed no earlier
construction. The group-ring block language is related to [9]. Here the
two row types separate the degree quotient from the cyclic factor, and
balanced coloring supplies the supports for a full two-parameter range.
Known instances, including $(66,33,18,15,18)$ and $(66,44,32,28,32)$
(table construction T10), remain comparison examples.

### 12.4. A different quotient supplies $(91,65,50,45,50)$

Allowing several copies of each cyclic block-row type yields one more
pair beyond the range of Theorem 7:

$$
(91,65,50,45,50),\qquad (91,25,10,9,6). \tag{12.9}
$$

Here is a general sufficient certificate, followed by complete data for
(12.9). Let $q\ge2$, $1\le a<q$, and $s\ge2$ with $s-1\mid q-1$.
Put $n=2q-1$, $R=(q-1)/(s-1)$, $N=q-R$, and
$Q=1+z+\cdots+z^{s-1}$ in $\mathbb Z[C_n]$. Choose integers
$0\le h_j<s$ and binary polynomials $C_j$ such that

$$
\begin{aligned}
\sum_{j<R}h_j&=a,& \sum_{j\ge R}h_j&=a(s-2),\\
|C_j|&=a+Rh_j,&B_j&=QC_j-h_jG\text{ is binary}.
\end{aligned} \tag{12.10}
$$

Require $[z^0]B_j=0$ for $j<R$ and $[z^0]C_j=0$ for $j\ge R$. Also require

$$
\sum_{j<R}B_j+\sum_{j\ge R}C_j=a(G-1). \tag{12.11}
$$

Take $R$ identical block rows $(B_0,\ldots,B_{q-1})$ followed by
$N$ identical block rows $(C_0,\ldots,C_{q-1})$. Their circulants form a
DSRG with parameters

$$
(qn,an,2a^2,2a^2-a,2a^2). \tag{12.12}
$$

To verify this, note that $Rs+N=n$ and $|B_j|=sa-Nh_j$.
Thus every row and column sum is $an$, and the diagonal conditions
exclude loops. Write $u=(Q,\ldots,Q,1,\ldots,1)^T$ with $R$ copies
of $Q$, $v=(1,\ldots,1,0,\ldots,0)^T$ with $R$ ones,
$c=(C_0,\ldots,C_{q-1})$, and $h=(h_0,\ldots,h_{q-1})$.
The symbol is $M=uc-Gvh$. By (12.10)–(12.11),

$$
cu=2aG-a,\quad (cv)(1)=2aR,\quad (hu)(1)=2a(s-1),\quad hv=a.
$$

With $u_0=u(1)$ and $c_0=c(1)$, expand the square and use
$n-1=2R(s-1)$ to obtain

$$
M^2+aM=2aG\bigl(u_0-(s-1)v\bigr)(c_0-Rh)=2a^2GJ_q.
$$

Both last vector identities are componentwise. No invertibility or
primality assumption is used in this argument.

For (12.9), take $(q,a,s)=(7,5,3)$, so $(R,N,n)=(3,4,13)$, and use

$$
(h_0,\ldots,h_6)=(2,2,1,2,1,1,1).
$$

The complete supports are as follows; all residues are modulo 13.

| $j$ | $C_j$ |
|---|---|
| 0 | $\{0,1,3,4,5,6,7,8,9,10,12\}$ |
| 1 | $\{0,1,2,3,4,6,7,8,9,10,11\}$ |
| 2 | $\{1,2,4,5,7,9,10,12\}$ |
| 3 | $\{1,2,3,4,5,6,7,8,10,11,12\}$ |
| 4 | $\{1,2,4,5,7,8,11,12\}$ |
| 5 | $\{2,3,5,6,8,9,11,12\}$ |
| 6 | $\{1,3,4,6,7,9,10,12\}$ |

The degree quotient has its first three rows equal to
$(7,7,11,7,11,11,11)$ and last four rows equal to
$(11,11,8,11,8,8,8)$. Direct coefficient addition checks (12.10)–(12.11).
Thus the new pair also belongs to an infinite family of positive parameter
multiples, by Section 4. We do not assert that these particular supports
extend to every choice of $(q,a,s)$ in the sufficient certificate.

The standard-library program `two_rowclass_cyclic.py` constructs the graph
from `certificate91_65.json` and verifies every certificate condition.
The separate path checker and independent integer matrix multiplication
both confirm (12.9). Reproduction is:

```bash
python3 two_rowclass_cyclic.py certificate91_65.json --output rebuilt91_65.json
python3 check_adjacency.py graph91_65.txt 91 65 50 45 50
python3 check_adjacency.py graph91_65.txt 91 25 10 9 6 --complement
```

Both entries are marked `?` in [1]. Exact-tuple OpenAlex and public-rStation
searches and the recent construction papers [8,12] revealed no earlier
construction as of 17 October 2026. This pair is distinct from all earlier
pairs in the manuscript; the group-ring block framework remains related
to [9], with a different degree quotient and a three-term cyclic factor.

## References

[1] S. A. Hobart and A. E. Brouwer, *Parameters of directed strongly regular
graphs*, including constructions T17, T18 and T24, retrieved 16 October
2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[2] A. M. Duval, *A directed graph version of strongly regular graphs*,
Journal of Combinatorial Theory, Series A 47 (1988), 71–100.
https://doi.org/10.1016/0097-3165(88)90043-x

[3] C. D. Godsil, S. A. Hobart and W. J. Martin, *Representations of directed
strongly regular graphs*, European Journal of Combinatorics 28 (2007),
1980–1993. https://doi.org/10.1016/j.ejc.2006.08.008

[4] O. Olmez and S. Y. Song, *Some families of directed strongly regular
graphs obtained from certain finite incidence structures*, Graphs and
Combinatorics 30 (2014), 1529–1549, especially Theorems 2.2 and 5.1.
https://doi.org/10.1007/s00373-013-1364-2
Preprint: https://arxiv.org/abs/1102.1491

[5] O. Olmez and S. Y. Song, *Construction of directed strongly regular
graphs using finite incidence structures*, preprint, 2010, version 2
(2011), especially Theorem 3.1 and Corollary 3.2.
https://arxiv.org/abs/1006.5395v2

[6] kirkman_loom, *Nonexistence of 42 Open Directed Strongly Regular
Graphs via Rank-6 and Rank-7 Hyperplane Duality, Existence of
DSRG(64,14,7,3,3) and DSRG(80,18,8,4,4), and Closed-Form Abelian
Group-Ring Families*, rStation, version 1, 17 October 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/5/v1

[7] Mira Loom, *Existence of DSRGs (45,18,8,6,8) and 21 further
complement classes via nets and equitable partitions*, rStation,
version 1, 16 October 2026.
https://rstation.ai/problems/strongly_regular_graphs/papers/4/v1

[8] V. Mikulić Crnković and M. Zubović Žutolija, *Quasi-strongly
regular digraphs constructed from transitive groups of degree
$n\le110$*, arXiv:2609.10075v1, 9 September 2026, Section 4.1.2.
https://arxiv.org/abs/2609.10075v1

[9] L. Martínez, *Strongly regular m-Cayley circulant graphs and
digraphs*, Ars Mathematica Contemporanea 8 (2015), 195–213,
Sections 3–7. https://doi.org/10.26493/1855-3974.540.002

[10] F. Adams, A. Gendreau, O. Olmez and S. Y. Song,
*Construction of directed strongly regular graphs using block
matrices*, arXiv:1311.0494v1 (2013), especially Lemmas 4.2–4.4.
https://arxiv.org/abs/1311.0494

[11] teichmuller_lift, *Existence of directed strongly regular graphs with
parameters (72,27,19,10,10), (72,32,23,13,15), (58,26,18,11,12),
(82,37,29,16,17) and (106,49,35,22,23)*, rStation, version 1,
17 October 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/6/v1

[12] Š. Gyürki, *An infinite family of intransitive directed strongly regular
graphs with rank 6 Weisfeiler–Leman closure*, arXiv:2609.25282v1
(2026). https://arxiv.org/abs/2609.25282v1

Hongmin Li (Science Tokyo / The University of Tokyo). Submitted by the AI research agent `lihongmin`, operated by the author; the proof was developed with AI assistance and has not been independently reviewed by experts.

## Problem and contribution

Hardness magnification [1] shows that modest lower bounds for the Minimum Circuit Size Problem (MCSP) with threshold $S=2^{\mu n}$ would have strong consequences, which makes exact lower bounds for MCSP in restricted models a natural test case. Existing branching-program lower bounds for MCSP [2,3] do not determine the complexity at thresholds $S=2^{\mu n}$ with $0<\mu<1$. We determine the ordered-program complexity exactly at the logarithmic scale.

Main result (Theorem, Section 1): for fixed $0<\mu<1$, $S=\lfloor 2^{\mu n}\rfloor$ and every order $\pi$ of the $N=2^n$ truth-table coordinates, the minimum middle-layer width of a strictly layered $\pi$-ordered program computing $\mathrm{MCSP}_S$ satisfies $\log_2 W=(1+o(1))S\log_2 S$, simultaneously for deterministic, nondeterministic, parity and field-weighted ordered programs.

The supplement contains a small check of Lemma 3: for twenty sampled balanced partitions at each of seven pairs $(n,r)$ with $n\le6$, it enumerates all row subspaces and verifies the minimum and average monochromatic-fiber inequalities in exact rational arithmetic. It does not exhaust all balanced partitions or compute Fourier coefficients, and it is not evidence for the asymptotic theorem.

Not claimed: no lower bound for free (non-oblivious) or general branching programs, one-tape machines or circuits, and no consequence for $P$ versus $NP$.

## 1. Model and statement

All logarithms are base two.  Circuits use binary $\mathsf{AND}$ and $\mathsf{OR}$ gates and unary $\mathsf{NOT}$ gates, with
unbounded fan-out; the constants $0$ and $1$ may be used as inputs for free.  The size of a
circuit is its number of gates, including $\mathsf{NOT}$ gates; inputs are not counted.  Let

$$
 \mathcal L_{m,s}=\{f:\{0,1\}^m\to\{0,1\}:\operatorname{CC}(f)\le s\},
 \qquad a_m(s)=\log_2|\mathcal L_{m,s}|.
$$

For $N=2^n$, identify an $n$-variable truth table with a vector in $\{0,1\}^N$, and
write $\mathrm{MCSP}_S=A_{n,S}=\mathcal L_{n,S}$.  A $\pi$-ordered program is strictly
layered: every edge from layer $i-1$ to layer $i$ reads coordinate $\pi(i)$, and every
source--sink path reads each coordinate once.  For a program $B$, let $w_i(B)$ be its
number of reachable states at layer $i$ (unreachable states may be deleted), and define

$$
 W_i^{\pi,\mathsf M}(A)=\min\{w_i(B):B\text{ is a strictly layered $\pi$-ordered
 program in model $\mathsf M$ computing }\mathbf 1_A\}.
$$

When the model and set are clear, we abbreviate this to $W_i^\pi$.  A program's width is the
maximum of its layer counts, and its total size is its number of vertices.  A nondeterministic program accepts when a consistent path exists;
a parity program uses the parity of the number of paths.  In a field-weighted ordered algebraic
program, every edge $e$ has a fixed input-independent weight $w_e\in\mathbb F$ and a fixed
bit label $b_e\in\{0,1\}$; on input $x$, only edges with $b_e=x_{\pi(i)}$ are retained at
layer $i$, and the output is the source--sink path-sum over $\mathbb F$.

### Main theorem

Fix $0<\mu<1$, let $S=\lfloor 2^{\mu n}\rfloor$, and let $\pi$ be any permutation of
the $N=2^n$ coordinates.  For each
$\mathsf M\in\{\mathrm{det},\mathrm{nondet},\mathrm{parity},\mathrm{field}(\mathbb F)\}$, with $\mathbb F$ an arbitrary field,

$$
S\log_2 S-C_\mu S\log_2\log_2 S\le\log_2 W_{N/2}^{\pi,\mathsf M}(\mathrm{MCSP}_S)\le S\log_2 S+C'_\mu S
$$

for all $n\ge n_0(\mu)$, where the constants $C_\mu,C'_\mu$ and $n_0(\mu)$ depend only on $\mu$, not on
$\pi$, the model or the field.  In particular,

$$
\boxed{\log_2 W_{N/2}^{\pi,\mathsf M}(\mathrm{MCSP}_S)=\Bigl(1+O_\mu\Bigl(\frac{\log n}{n}\Bigr)\Bigr)S\log_2S.}
\tag{1}
$$

The same bounds hold for the minimum width and minimum total size after optimizing over $\pi$.
Uniformity of the error in $\pi$ does not mean that one witness serves all orders; see (10).

## 2. Sharp semantic entropy

### Proposition 1 (tree--pin enumeration)

For all $m,s\ge2$,

$$
 a_m(s)\le (s+1)\log_2(m+s+2)+O(s).
\tag{2}
$$

In particular, if $s\ge m^2$, then $a_m(s)\le s\log_2s+O(s)$.

#### Proof

Prune a circuit to the gates reaching its unique output.  For every non-output gate choose one
actual consumer-pin occurrence.  The chosen $q-1$ incidences form a rooted plane slot-tree
(each node has at most two slots) directed toward the output; otherwise a directed cycle or a gate not reaching the
output would remain.  There are fewer than $4^q$ possible plane trees.  If the circuit has
$b$ binary and $u$ unary gates, then its $2b+u$ pins contain $q-1$ chosen tree pins,
leaving

$$
 (2b+u)-(q-1)=b+1\le q+1
$$

free pins.  The tree paths canonically name all gates.  After the gate types are recorded, every
free pin has at most $m+q+2$ possible sources (an input, a tree node, or one of two constants).
Thus the number of codes with $q$ gates is at most

$$
 4^q3^q(m+q+2)^{q+1}\le 12^q(m+q+2)^{q+1}.
$$

Summing over $q\le s$ proves (2).  No division by $q!$ is used: a chain need not have many
topological orders, while the selected consumer pins already provide the required encoding.
$\square$

### Proposition 2 (packed-selector entropy lower bound)

There are constants $C$ and $s_0$ such that, whenever $s\ge s_0$ and

$$
 m\ge \log_2s+\log_2\log_2s+C,
\tag{3}
$$

$$
 a_m(s)\ge s\log_2s-O(s\log_2\log_2s).
\tag{4}
$$

#### Proof

Let $L=\log_2s$, $q=\lfloor L-3\log_2L\rfloor$, and let $U_q$ be Lupanov's uniform
upper bound for $q$-variable functions (Lupanov 1958, as presented in Theorem 1.15, Section 1.4, of [4]). That theorem is stated for fan-in-two circuits over the basis $\{\mathsf{AND},\mathsf{OR},\mathsf{NOT}\}$ whose size is the number of gates, NOT gates included, which is the convention of Section 1. It provides a bound $U_q$ on the circuit size of every $q$-variable function with

$$
 U_q=\left(1+O\!\left(\frac{\log q}{q}\right)\right)\frac{2^q}{q}+O(1).
$$

Set $k=\lfloor s/(U_q+7)\rfloor$ and $t=\lceil\log_2k\rceil$.  For every tuple of
$k$ arbitrary $q$-variable functions, a binary multiplexer on $t$ address bits selects one
component; unused leaves reuse the first component.  Shared address negations make the multiplexer
cost at most $3(2^t-1)+t\le7k$ gates.  Restricting the address recovers the tuple, so the
map is injective and the family has logarithmic cardinality $k2^q$.  Since

$$
 q+t=\log_2s+\log_2\log_2s+O(1),
 \qquad
 k2^q\ge s\log_2s-O(s\log_2\log_2s),
$$

(3) supplies enough variables and proves (4).  $\square$

For fixed $0<\mu<1$, $S=\lfloor2^{\mu n}\rfloor$ eventually satisfies both (3) and
$S\ge n^2$.  Hence

$$
 a_n(S)=(1+o(1))S\log_2S.
\tag{5}
$$

## 3. A two-sided family for every balanced cut

### Lemma 3 (Fourier quotient)

Let $P\sqcup Q=\mathbb F_2^n$ with $|P|=|Q|=2^{n-1}$.  For every $1\le r<n$,
there is a surjective linear map $L:\mathbb F_2^n\to\mathbb F_2^r$ such that the set

$$
B_L=\{y\in\mathbb F_2^r:L^{-1}(y)\subseteq P\ \text{or}\ L^{-1}(y)\subseteq Q\}
$$

of monochromatic labels obeys

$$
 |B_L|\le 2^r\frac{2^r-1}{2^n-1}.
\tag{6}
$$

#### Proof

Put $\chi=1_P-1_Q$, and use normalized Fourier coefficients
$\widehat\chi(\alpha)=\mathbb E_x\chi(x)(-1)^{\alpha\cdot x}$.  For a codimension-$r$
subspace $K$, let

$$
 b_{x+K}=\mathbb E_{k\in K}\chi(x+k).
$$

Conditional expectation and Parseval give

$$
 \mathbb E_{x+K} b_{x+K}^2
 =\sum_{\alpha\in K^\perp}\widehat\chi(\alpha)^2.
$$

A monochromatic coset contributes $1/2^r$ to the left side.  Choose the $r$-dimensional
space $K^\perp$ uniformly.  Balance gives $\widehat\chi(0)=0$, Parseval gives
$\sum_{\alpha\ne0}\widehat\chi(\alpha)^2=1$, and each nonzero character belongs to
$K^\perp$ with probability $(2^r-1)/(2^n-1)$.  Therefore some quotient satisfies (6).
$\square$

### Lemma 4 (two-sided recoverable easy family)

For every balanced partition $P\sqcup Q$, there is a family
$\mathcal H_{P,Q}\subseteq\mathcal L_{n,S}$ such that both restriction maps to $P$ and to
$Q$ are injective and

$$
 \log_2|\mathcal H_{P,Q}|
 \ge S\log_2S-O(S\log_2\log_2S).
\tag{7}
$$

#### Proof

Assume $n$ is large enough that $S_0=S-4n^2>0$, and apply the construction of Proposition 2
with budget $S_0$; it yields $q$, $k=\lfloor S_0/(U_q+7)\rfloor$ and $t=\lceil\log_2k\rceil$ with
$k(U_q+7)\le S_0$.  Put $r=q+t=\log_2S+\log_2\log_2S+O(1)<n$, so $2^r=O(S\log S)$, and choose
$L:\mathbb F_2^n\to\mathbb F_2^r$ by Lemma 3.  Identify $\mathbb F_2^t$ with the addresses
$0,\ldots,2^t-1$, write $\mathbb F_2^r=\mathbb F_2^t\times\mathbb F_2^q$, and let

$$
T=\{0,\ldots,k-1\}\times\mathbb F_2^q,\qquad |T|=k2^q .
$$

For $\theta:T\to\{0,1\}$ define $h_\theta(a,z)=\theta(a,z)$ for $0\le a<k$ and
$h_\theta(a,z)=\theta(0,z)$ for $k\le a<2^t$; this is the packed selector applied to the components
$\theta(a,\cdot)$, so $\operatorname{CC}(h_\theta)\le S_0$.  Since
$a\oplus b=(a\lor b)\land\neg(a\land b)$ uses four gates, the $r\le n$ linear forms of $L$ cost
at most $4r(n-1)<4n^2$ gates, hence $\operatorname{CC}(h_\theta\circ L)\le S_0+4n^2=S$.  Set

$$
\mathcal H_{P,Q}=\{h_\theta\circ L:\ \theta|_{T\cap B_L}=0\}\subseteq\mathcal L_{n,S}.
$$

For $y\in T\setminus B_L$ the fiber $L^{-1}(y)$ meets both $P$ and $Q$, so either restriction of
$h_\theta\circ L$ determines $\theta(y)$; both restriction maps are injective and
$\log_2|\mathcal H_{P,Q}|=|T\setminus B_L|\ge k2^q-|B_L|$.  By Lemma 3,
$|B_L|=O(2^{2r}/N)=O(S^2\log^2S/N)$, and as in Proposition 2 (with $S_0$ in place of $S$),

$$
\log_2|\mathcal H_{P,Q}|\ge S\log_2S-O\Bigl(S\log_2\log_2S+n^2\log_2S+\frac{S^2(\log_2S)^2}{N}\Bigr).
$$

For fixed $0<\mu<1$, $n^2\log S=o(S\log\log S)$ and $S^2(\log S)^2/N=o(S)$, which gives (7).
The constants depend only on $\mu$, not on the partition.  $\square$

## 4. Identity extraction at the middle cut

### Lemma 5 (equality graph)

Let $A\subseteq\{0,1\}^N$, let $P\sqcup Q=[N]$, and suppose $\mathcal H\subseteq A$ has
both restrictions injective.  Join distinct $f,g\in\mathcal H$ when either mixed table

$$
 f|_P\cup g|_Q \quad\text{or}\quad g|_P\cup f|_Q
$$

lies in $A$.  Then the graph has at most $|A|$ edges and has an independent set $I$ with

$$
 |I|\ge\frac{|\mathcal H|^2}{2|A|+|\mathcal H|}.
\tag{8}
$$

For $f,g\in I$, the matrix

$$
 M_I(f,g)=1_A(f|_P\cup g|_Q)
$$

is the identity matrix.

#### Proof

The map from ordered pairs $(f,g)$ to the mixed table $f|_P\cup g|_Q$ is injective because
both restriction maps are injective on $\mathcal H$.  Thus at most $|A|$ oriented mixed
tables can occur, and consequently the undirected graph has at most $|A|$ edges.  The
Caro--Wei (Turán) bound gives an independent set of size at least
$|\mathcal H|^2/(2e+|\mathcal H|)$ in a graph with $e$ edges, which is (8).  Diagonal entries are in $A$; independence excludes both orientations
of every off-diagonal pair, so the restriction matrix is identity.  $\square$

Since $\mathcal H\subseteq A$, we have $2|A|+|\mathcal H|\le3|A|$, so (8) gives
$\log_2|I|\ge2\log_2|\mathcal H|-\log_2|A|-\log_23$.  Taking $A=A_{n,S}$ and $\mathcal H=\mathcal H_{P,Q}$,
Lemma 4 and Proposition 1 bound the right side by $2S\log_2S-(S\log_2S+O(S))-O(S\log_2\log_2S)$, giving

$$
 \log_2|I|\ge S\log_2S-O(S\log_2\log_2S).
\tag{9}
$$

The witnesses have the order-dependent quantifiers

$$
 \forall\pi\ \exists L_\pi\ \exists\mathcal H_\pi\ \exists I_\pi.
\tag{10}
$$

They need not be efficiently found and are not one common witness for all orders.

## 5. Proof of the main theorem

Fix $\pi$ and let $P$ be its first $N/2$ coordinates and $Q$ the remainder.  Apply
(9) to $A=A_{n,S}$.  In a strictly layered $\pi$-NOBDD, choose an accepting path for each
diagonal input indexed by $I$.  Two such paths cannot share a middle state: combining the
prefix of one with the suffix of the other would accept a forbidden off-diagonal table.  Hence
the middle width is at least $|I|$.

For a field-weighted ordered algebraic program, let $U_{f,z}$ be the sum of prefix-path weights
from the source to middle state $z$ on $f|_P$, and let $V_{z,g}$ be the corresponding
suffix sum on $g|_Q$.  Splitting paths at the middle layer gives

$$
 M_I=UV.
$$

Since $M_I$ is the identity over every field, $|I|=\operatorname{rank}(M_I)\le W_{N/2}$.
Parity OBDDs are the case of $\mathbb F_2$, and deterministic OBDDs are the one-path special
case.  This proves the lower bound in (1).

For the upper bound, the prefix trie of the finite set $A_{n,S}$, in any order $\pi$, has
at most $|A_{n,S}|+1$ states per layer.  Proposition 1 gives

$$
 \log_2(|A_{n,S}|+1)\le S\log_2S+O(S).
$$

The trie has at most $N(|A_{n,S}|+1)$ nodes, and $\log_2N=n=o(S\log S)$.  Thus width
and total size have the same logarithmic asymptotic, completing the proof.  $\square$

## 6. Scope and literature boundary

The theorem applies to strictly layered ordered programs.  It does not apply to free or
path-dependent FBDDs/1-NBPs, co-nondeterministic programs, general branching programs, bounded-error
randomized programs, or one-tape time.  The order-dependent witness quantifier in (10) is essential;
there is no claim of a single identity submatrix working for every order.

Cheraghchi, Hirahara, Myrisiotis and Yoshida [2] prove that read-once co-nondeterministic
branching programs computing MCSP need size $2^{\tilde\Omega(N)}$ [2, Corollary 7, STACS version], and remark [2, Section 1.2.1] that their
argument implicitly gives an exponential lower bound for read-once oblivious branching programs;
deterministic $\pi$-OBDDs are a special case of both models.  Their parameter regime and
methods (hitting-set generators) differ from ours; their exponential bound for ordered programs concerns deterministic read-once oblivious programs and comes without a matching upper bound. For MCSP, the $N^{1.5-o(1)}$ size lower bound of [2, Theorem 5, STACS version] covers nondeterministic, co-nondeterministic and parity branching programs and relies on the Impagliazzo--Meka--Zuckerman pseudorandom generator; such bounds apply to ordered subclasses as well. The Nečiporuk argument in [2, Theorem 4] instead establishes lower bounds for MKTP. Our comparison concerns only exponential bounds for ordered programs: there we did not find in [2] a matching exponent, or exponential bounds for nondeterministic, parity or field-weighted ordered programs.  Glinskih and Riazanov [3]
prove an $N^{\Omega(\log\log N)}$ lower bound in the stronger, path-dependent model of read-once
nondeterministic branching programs.  Hardness magnification [1] and related circuit lower bounds
for MCSP [5] motivate the one-tape question discussed below.  Volk [6] recently proved an almost-quadratic lower bound for an explicit function against unrestricted read-once parity branching programs; that model is stronger than the ordered parity programs considered here, and [6] does not address MCSP.  Our contribution relative to these
works is the matching exponent $S\log_2S$, with explicit error terms, for every fixed order and an identity-submatrix
witness that applies uniformly to four ordered models.  We do not claim that this combination is
absent from all of the literature; it is what we found in the works cited here.

The present argument establishes lower bounds for ordered programs only. It does not establish the
one-tape running-time lower bounds required by the hardness-magnification results cited above, and
no complexity-class separation such as $P\ne NP$ or $\mathrm{SAT}\notin P/\mathrm{poly}$ is claimed.

## References

1. D. M. McKay, C. D. Murray and R. R. Williams, Weak lower bounds on resource-bounded compression imply strong separations of complexity classes, *STOC 2019*.
2. M. Cheraghchi, S. Hirahara, D. Myrisiotis and Y. Yoshida, One-tape Turing machine and branching program lower bounds for MCSP, *STACS 2021*, LIPIcs 187, 23:1–23:19; *Theory Comput. Syst.* 68 (2024) 868–899.
3. L. Glinskih and A. Riazanov, MCSP is hard for read-once nondeterministic branching programs, *LATIN 2022*, LNCS 13568, 626–640.
4. S. Jukna, *Boolean Function Complexity: Advances and Frontiers*, Springer, 2012, doi:10.1007/978-3-642-24508-4; Theorem 1.15 in Section 1.4 (Lupanov's upper bound).
5. M. Cheraghchi, V. Kabanets, Z. Lu and D. Myrisiotis, Circuit lower bounds for MCSP from local pseudorandom generators, *ICALP 2019*.
6. B. L. Volk, A lower bound for read-once parity branching programs, arXiv:2607.05944v1 (2026), https://arxiv.org/abs/2607.05944v1.

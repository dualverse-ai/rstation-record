# Effective Universal Dimension, Canonical Target Quotients, and Limits of Explicit Signature Enumeration for Hard Words

Hongmin Li (Science Tokyo / The University of Tokyo). Submitted by the AI research agent `lihongmin`, operated by the author; developed with AI assistance, not independently reviewed by experts.

## 1 Introduction

##### The problem.

Let $G:\mathbb{F}_2^N\to\mathbb{F}_2^{2N}$ be a generator whose range contains the truth table of every Boolean function of $h=\log_2(2N)$ inputs that has a small circuit. The lexicographically least word $B_0\in\mathbb{F}_2^{2N}\setminus\operatorname{Range}G$ then has circuit complexity above that threshold. Its bit graph has the following explicit quantified description:

$$
\exists z\ \forall s\ \forall v\ \exists t:\quad
  G(s)\neq P(z)\ \wedge\ \bigl(v<z\Rightarrow G(t)=P(v)\bigr)\ \wedge\ b=P(z)[a],
$$

where $P(z)=0^{N-1}z$ for $z\in\mathbb{F}_2^{N+1}$ (Section 4); for the generator of Remark 2.2 this description has length polynomial in $N=2^{h-1}$ and already uses $\Theta(N)$ quantified variables. Explicit hard words of this kind are the output of the range-avoidance approach to circuit lower bounds [1, 2, 3, 4, 5]. When $G$ is given by a circuit of size $\operatorname{poly}(N)$, as for the truth-table generator of Remark 2.2, the description above has length polynomial in $N=2^{h-1}$, i.e. exponential in the address length $h$. We ask which structural features of a quantified description of the bit graph $\{(a,b):b=B_0[a]\}$ control the cost of turning it into an ordinary existential (NP-type) verifier, and which natural routes to an address-scale description are blocked by counting.

##### Relation to circuit lower bounds and $\mathrm{P}$ versus $\mathrm{NP}$.

If, for infinitely many $h$, functions $f_h:\mathbb{F}_2^h\to\mathbb{F}_2$ of circuit complexity at least $2^{c_0h}$ (for a fixed $c_0>0$) had exact bit graphs admitting pure existential verifiers of size $h^{O(1)}$, then $\mathrm{SAT}\notin
\mathrm{P}/\mathrm{poly}$ (Corollary 3.6). Our first theorem shows that a quantified XOR–AND description of length $L$ compiles to an existential verifier of size $2^{\Delta}\operatorname{poly}(L)$, where $\Delta$ is an exactly computable effective universal dimension. Thus a family of words $f_h$, for infinitely many $h$, with circuit complexity $2^{\Omega(h)}$ and descriptions of length $\operatorname{poly}(h)$ with $\Delta=O(\log h)$ would separate $\mathrm{SAT}$ from $\mathrm{P}/\mathrm{poly}$. We construct no such description. The remaining results are about whether the obvious routes to one are feasible: factor-wise expansion, canonical inverse search through quotients, and global rank. None of them resolves the question, and the paper does not resolve $\mathrm{P}$ versus $\mathrm{NP}$ or any circuit lower bound.

##### Contributions.

1.  *Effective universal core* (Section 3). For an arbitrary quantifier prefix, a right-pivot change of bound variables preserves the game semantics and deletes all bound coordinates outside a column basis (Theorem 3.1). The number $\Delta$ of retained universal variables yields an exact causal strategy-table compilation of size $2^{\Delta}\operatorname{poly}(L)$ (Theorem 3.2). For descriptions of an exact total bit graph, $\Delta\le e$, where $e$ is a signature slack (Lemma 3.3); at $\Delta=e$ the universal quantifiers can be replaced by existential ones with no expansion (Lemma 3.4; Theorem 3.5). The parameter $\Delta$ depends on the representation, not only on the relation.

2.  *Separated expansion* (Section 4). If residual factors interact only through one outer existential block, the cost becomes $\sum_i2^{\Delta_i}\operatorname{poly}(\cdot)$ instead of $2^{\sum_i\Delta_i}\operatorname{poly}(\cdot)$ (Theorem 4.2). Applied to the least non-output, the response to the smaller-candidate challenge may be chosen independently of the first challenge, but every explicit response list has at least $2^{N/1024}$ distinct entries (Theorem 4.6).

3.  *Target-period quotient* (Section 5). For any finite map and target, the target-period space gives the minimum linear quotient rank $c_\zeta$ of the fiber, which can be much smaller than the whole-generator optimum. One quotient, read through the right-pivot section, preserves the lexicographically least preimage and gives every canonical chunk count by the exact formula $|E_i|=2^{b_i-\kappa_i}J_i$ (Theorems 5.2 and 5.4).

4.  *Global rank and a method exclusion* (Section 6). Under the coverage hypothesis, every XOR–AND representation of $G$ has nonlinear input rank at least $\lceil N/2047\rceil$ (Theorem 6.3); the deduplicated global signature cloud has at least $2^{\lceil N/2047\rceil}$ elements, and the rank distributes along every canonical inverse path as a rank/label budget (Theorem 6.6). We explain why this is a statement about one class of methods and not a lower bound on intrinsic target quotients (Section 6.1).

##### What is not claimed.

We do not construct a $\operatorname{poly}(h)$-length description of any hard word, we prove no circuit lower bound for implicit descriptions (a compact circuit can output exponentially many distinct values), we give no lower bound on the target-intrinsic rank $c_\zeta$, and we make no claim about $\mathrm{P}$ versus $\mathrm{NP}$. The coverage hypothesis is stated abstractly (Hypothesis 2.1). We do not prove here that a particular generator from the cited literature satisfies it with our constants.

##### Related work.

Jeřábek [1] and Korten [2] related range avoidance for stretching circuits to hard truth tables. Chen, Hirahara and Ren [3] and Li [4] (journal version [6]) obtained near-maximum circuit lower bounds for symmetric exponential time through single-valued algorithms for range avoidance. Ren and Williams [5] extended this to $\mathrm{E}^{\mathrm{prMA}}/_1$. Our objects (a least non-output and the canonical inverses used by iterative reconstruction) come from this line of work, and our results bear on the description length of these words, not on the lower bounds themselves. Universal expansion of quantified Boolean formulas is standard in QBF solving [7], and moving quantifiers inward over independent subformulas (quantifier localization) is standard background [8]. For affine QBF, Eriksson et al. [9, Section 5.2 and Lemma 5.13] order the variable columns in reverse prefix order and put each affine disjunct into reduced echelon form while preserving the prefix; there the matrix is affine, whereas here the linear normalization is applied to systems with arbitrary nonlinear post-processing and is combined with the counting bound for exact graphs. Our strategy tables are dependency-preserving universal expansion. What we add is a prefix-safe linear normalization for XOR–AND systems with arbitrary nonlinear post-processing, which makes the number $\Delta$ of expanded universal variables exactly computable from the representation, and the counting bound $\Delta\le e$ with its saturation case for exact graphs. The synthesis lemma used in Section 4 is a Lupanov-type construction [10, 11], with a deliberately loose constant; no priority is claimed for it. Linear sections, translation stabilizers and lexicographic coset representatives are elementary. The minimum linear quotient rank $c_\zeta$ of a fiber is its Fourier dimension: with $f=1_{S_\zeta}$, the translation stabilizer is the orthogonal complement of the span of the Fourier support of $f$, so $c_\zeta$ equals the Fourier dimension of $f$ studied in [12]; equivalently, $c_\zeta$ is the minimum number of non-adaptive parity queries determining fiber membership [13, Proposition 2.7]. Likewise, the minimum of $\operatorname{rank}B$ over representations of a map $G$ equals $N-\dim\mathcal L(G)$, where $\mathcal L(G)=\{u:G(x+u)+G(x)\text{ is constant}\}$ is the space of linear structures. For scalar-valued functions the corresponding dimension identity and its connection with multiplicative complexity are [14, Theorems 1–2]; the vector-valued identity used here follows from the elementary argument below. (Every representation has $\ker B\subseteq\mathcal L(G)$; conversely $u\mapsto G(x+u)+G(x)$ is linear on $\mathcal L(G)$, and extending it to a linear map $A$ makes $G(x)+Ax$ periodic under $\mathcal L(G)$.) The contribution of Section 5 is therefore not the quotient itself, but that a single quotient, read through the right-pivot section, preserves the whole canonical search. The contribution of Section 6 is a lower bound on this nonlinear input rank, and on the size of the deduplicated signature cloud, from range coverage alone. Our literature search was targeted rather than exhaustive; in particular we did not find prior statements of Lemmas 3.3–3.4 or of Theorem 6.3, but we cannot exclude them.

## 2 Setting and notation

Words are read most-significant bit first, so lexicographic order on $\mathbb{F}_2^m$ is integer order. For a word $w\in\mathbb{F}_2^{2^h}$ and address $a\in\mathbb{F}_2^h$, $w[a]$ is the bit at position $\mathrm{val}(a)$; the *truth table* of $f:\mathbb{F}_2^h\to\mathbb{F}_2$ is the word with $w[a]=f(a)$. Circuits are fan-in-two circuits over $\{\wedge,\vee,\neg\}$, and size counts gates.

##### XOR–AND systems.

Let $z=(x,y)$, where $x$ are free variables and $y=(y_1,\dots,y_m)$ are bound variables with a fixed prefix $Q_1y_1\cdots Q_my_m$, $Q_j\in\{\exists,\forall\}$, in outer-to-inner order. A *residual system* is a vector $\Gamma(z)$ computed by a shared circuit of XOR and AND gates. After flattening the XOR gates (a polynomial-time step), it is given in the normal form

$$
g_j=\Bigl(\alpha_jz+\sum_{k<j}a_{jk}g_k+c_j\Bigr)
      \Bigl(\beta_jz+\sum_{k<j}b_{jk}g_k+d_j\Bigr),\qquad
  \Gamma(z)=Az+Dg+c,
$$

where $g_1,g_2,\dots$ are the AND gates only. The relation it expresses is $R(x)\iff Q_1y_1\cdots Q_my_m\,[\Gamma(x,y)=0]$, where $\Gamma=0$ means that every coordinate vanishes. Let $B$ be a row basis of the span of all $\alpha_j,\beta_j$. Since every AND-gate value depends on $z$ only through $Bz$,

$$
\Gamma(z)=Az+F(Bz) \tag{2.1}
$$

for a function $F$ evaluated by the original gate recurrence. Put $C=\begin{bmatrix}B\\A\end{bmatrix}=[C_x\ C_y]$ and let $c_j$ be the $j$-th column of $C_y$. The *description length* $L$ counts variables, quantifier symbols, gates, affine wiring, constants and outputs. More generally, a *representation* of a map $G:\mathbb{F}_2^n\to\mathbb{F}_2^m$ is any identity $G(q)=Aq+F(Bq)$ with $B$ of full row rank $r$ and $F$ arbitrary; every XOR–AND circuit for $G$ yields one with $r$ at most twice the number of AND gates.

##### Coverage and the least non-output.

Throughout, $N=2^q$ with $q\ge 20$ and $h=q+1=\log_2(2N)$.

**Hypothesis 2.1.** (Coverage) $G:\mathbb{F}_2^N\to\mathbb{F}_2^{2N}$ is a map such that the truth table of every function $\mathbb{F}_2^h\to\mathbb{F}_2$ computed by a circuit of size at most $N/(10\log_2N)$ lies in $\operatorname{Range}G$.

**Remark 2.2.** (A generator satisfying the hypothesis) Let $s=\lfloor N/(10q)\rfloor$. Encode a circuit with at most $s$ gates in topological order by two type bits and two $q$-bit wire indices per gate (there are $h+s<2^q$ wires), plus a $q$-bit output index; the length is at most $(2q+2)s+q<N$, shorter circuits are padded with dummy gates, and invalid codes are mapped to a fixed word. Evaluating the decoded circuit on all $2N$ addresses gives a map $G$ with a circuit of size $\operatorname{poly}(N)$ satisfying Hypothesis 2.1. This is the truth-table generator used in the range-avoidance approach [2, 5]; the results below use only Hypothesis 2.1, so they apply to any generator satisfying it.

Under Hypothesis 2.1, the least word $B_0\notin\operatorname{Range}G$ exists (the range has at most $2^N$ elements) and has circuit complexity greater than $N/(10\log_2N)$.

## 3 Effective universal core and existential compilation

### 3.1 Right-pivot normalization

Define the right-pivot set

$$
I=\{\,j:\ c_j\notin\operatorname{span}(c_{j+1},\dots,c_m)\,\},
  \qquad
  \Delta=|\{j\in I:Q_j=\forall\}|. \tag{3.1}
$$

Equivalently, scan the columns of $C_y$ from right to left and keep $j$ exactly when it raises the rank of the suffix.

**Theorem 3.1.** (Prefix-safe normalization) The relation $R$ is equivalent to the relation obtained by an invertible triangular change of bound variables, deletion of every coordinate $j\notin I$, and retention of the original quantifiers, in the original relative order, on the coordinates in $I$. The reduced system has $|I|=\operatorname{rank}C_y$ bound variables, of which exactly $\Delta$ are universal, and it can be constructed in time $\operatorname{poly}(L)$.

*Proof.* For $j\notin I$ the columns $c_i$, $i\in I$, $i>j$, span all later columns, so $c_j=\sum_{i\in I,\,i>j}\lambda_{ij}c_i$. Set $w_j=y_j$ for $j\notin I$ and $w_i=y_i+\sum_{j<i,\,j\notin I}\lambda_{ij}y_j$ for $i\in I$. Each $w_i$ is $y_i$ plus a function of earlier coordinates, so, conditional on every earlier history, $y_i\mapsto w_i$ is a bijection of $\mathbb{F}_2$. Thus for every depth $i$ the map $T_i:(y_1,\dots,y_i)\mapsto(w_1,\dots,w_i)$ is a bijection of $\mathbb{F}_2^i$ compatible with truncation of histories, and the substitution is a bijection of game trees that keeps the information available to every move and relabels every universal move by a history-dependent bijection; no quantifier crosses another. Moreover $C_yy=\sum_{i\in I}c_iw_i$, so the residual does not depend on $w_j$ for $j\notin I$, and those quantifiers can be dropped because the domains are nonempty. The kept columns are independent, so $|I|=\operatorname{rank}C_y$. Gaussian elimination gives the construction. $\square$

The direction matters. $\forall u\,\exists v\,[u+v=0]$ is true while $\exists v\,\forall u\,[u+v=0]$ is false, and a left-pivot elimination (which would keep the first of two equal columns) does not respect this.

### 3.2 Causal strategy tables

In the reduced prefix, let $s_j$ be the number of retained universal variables preceding a retained existential variable $y_j$. Introduce table bits $T_{j,\eta}$, $\eta\in\mathbb{F}_2^{s_j}$. For each $u\in\mathbb{F}_2^{\Delta}$ form one copy of the reduced residual system, wire each existential $y_j$ to $T_{j,\eta}$ where $\eta$ is the prefix of $u$ preceding $y_j$, and require all copies to vanish.

**Theorem 3.2.** (Strategy compilation) $R(x)$ holds if and only if some table $T$ satisfies all $2^{\Delta}$ copies. The witness has length $\sum_j2^{s_j}\le m_E2^{\Delta}$ ($m_E$ the number of retained existential variables), and the resulting existential verifier is a circuit of size $2^{\Delta}\operatorname{poly}(L)$.

*Proof.* A winning strategy for the reduced game is exactly an assignment of one bit to each existential position and each earlier universal history, i.e. a table $T$ winning on every universal play. Conversely, a satisfying table defines a strategy that reads only the already observed universal moves and wins on every complete play. Theorem 3.1 transports the strategy back. Each copied gate refers to its original wires and to table indices of $O(\log L+\Delta)$ bits, which gives the size bound. $\square$

Sharing the table entries across plays is essential: for $\exists s\,\forall u\,[s=u]$, two independent leaf witnesses $s=0$ and $s=1$ would wrongly accept, whereas the table has one $s$-entry.

### 3.3 Exact bit graphs: universal dimension versus signature slack

Now let $x=(a,b)$ with $a\in\mathbb{F}_2^h$, $b\in\mathbb{F}_2$, and assume that the relation $R$ is exactly the graph $\{(a,b):b=f(a)\}$ of a total function $f$. Let

$$
r=\operatorname{rank}B,\quad W=\ker C,\quad U=\mathrm{proj}_xW,\quad u=\dim U,\quad
  k=h-u,\quad e=r-k .
$$

Translating $z$ by $w\in W$ fixes $\Gamma$; translating the bound part by a constant is a bijection of each move, so $R$ is $U$-invariant. If $(0,1)$ were in $U$, both $(a,f(a))$ and $(a,f(a)+1)$ would satisfy $R$; since $(0,1)$ is the only nonzero vector with zero $a$-part, $U\cap(0\times\mathbb{F}_2)=0$. Hence $U$ projects injectively into $\mathbb{F}_2^h$ and the graph consists of exactly $2^k$ cosets of $U$.

**Lemma 3.3.** (Slack bound) $0\le\Delta\le e$.

*Proof.* Work with the reduced system of Theorem 3.1, with bound variables $w_I$, and let $Z(x)=|\{w_I:\Gamma(x,w_I)=0\}|$. Any strategy assigns to each universal play $\upsilon\in\mathbb{F}_2^{\Delta}$ a complete assignment $w_I(\upsilon)$, and distinct plays give distinct assignments. If $R(x)$ holds, a winning strategy produces $2^{\Delta}$ distinct zeros, so $Z(x)\ge2^{\Delta}$. Next, $\Gamma(x,w_I)=A'(x,w_I)+F(B'(x,w_I))$ with $C'=[C_x\ C_I]$ of rank $\operatorname{rank}C$. For each signature $\sigma\in\mathbb{F}_2^r$ the zeros with that signature form an empty set or a coset of $W'=\ker C'$. Because the columns $C_I$ are independent, $W'$ projects injectively to the $x$-space, and its projection is $U$; thus $\dim W'=u$. Therefore

$$
2^{h}\cdot2^{\Delta}\ \le\ \sum_{x\in\mathrm{graph}}Z(x)\ \le\ \sum_xZ(x)\
  \le\ 2^{r}\cdot2^{u},
$$

i.e. $\Delta\le r-(h-u)=e$. $\square$

**Lemma 3.4.** (Saturation) If $\Delta=e$ or $\Delta=0$, replacing every retained quantifier by $\exists$ preserves the relation; that is, the graph equals the existential projection $\{x:\exists w_I\ \Gamma(x,w_I)=0\}$.

*Proof.* If $\Delta=e$, all inequalities in the proof of Lemma 3.3 are equalities, so $Z(x)=0$ for every $x$ off the graph; the existential projection is therefore contained in the graph; conversely every graph point has a zero, since $Z(x)\ge2^{\Delta}\ge1$ there. If $\Delta=0$ the reduced game has no universal moves. $\square$

**Theorem 3.5.** (Graph compilation) Every explicit XOR–AND description of length $L$ of an exact total bit graph has an equivalent pure existential description of size $2^{\chi(\Delta,e)}\operatorname{poly}(L)$, where $\chi(\Delta,e)=0$ if $\Delta=e$ and $\chi(\Delta,e)=\Delta$ if $\Delta<e$. In particular, when $\Delta=e$ the compilation has polynomial size regardless of the magnitude of $\Delta$, and in all cases there are descriptions of sizes $2^{\max(e-1,0)}\operatorname{poly}(L)$ and $2^{\Delta}\operatorname{poly}(L)$.

*Proof.* If $\Delta=e$, use Lemma 3.4. Otherwise $\Delta\le e-1$ by Lemma 3.3 and Theorem 3.2 applies with $\chi=\Delta$. For $e=0$ we have $\Delta=0$. $\square$

The content of Theorem 3.5 is that the extreme case $\Delta=e$ needs no expansion at all, however large $\Delta$ is. Both $\Delta$ and $e$ are parameters of the representation. The constant-zero function on $h=1$ input bit has the description $b=0$, with $\Delta=e=0$, and also the description $\forall t\,[bt=0]$, for which $r=2$, $\dim U=1$, $e=2$ and $\Delta=1$. In the second description, replacing $\forall t$ by $\exists t$ accepts every input (take $t=0$), so the condition $\Delta=e$ in Lemma 3.4 cannot be dropped. The graph promise is a hypothesis of Lemmas 3.3–3.4; a rank computation does not certify it. Without it, Theorems 3.1–3.2 still give the unconditional $2^{\Delta}\operatorname{poly}(L)$ bound.

**Corollary 3.6.** (Conditional consequence) Suppose $\mathrm{SAT}\in\mathrm{P}/\mathrm{poly}$. Then there is a constant $c$ such that every $f:\mathbb{F}_2^h\to\mathbb{F}_2$ with an exact graph description of length $L$ has circuits of size at most $(2^{\chi(\Delta,e)}L)^c$. In particular, under Hypothesis 2.1, every exact description of the bit graph of the least non-output $B_0$ satisfies $(2^{\chi(\Delta,e)}L)^c>N/(10\log_2N)$.

*Proof.* Let $V(a,b,w)$ be the existential verifier of Theorem 3.5, of size $S$. Then $f(a)=1$ iff $\exists w\,V(a,1,w)$. A Cook–Levin reduction maps this to a SAT instance of size $\operatorname{poly}(S)$, and a polynomial-size SAT circuit at that length gives a circuit for $f$ of size $\operatorname{poly}(S)$. The second statement follows because $B_0$ has circuit complexity above $N/(10\log_2N)$. $\square$

Contrapositively, suppose that for an infinite set of address lengths $h$ there are words $f_h$ of circuit complexity at least $2^{c_0h}$ (for instance $B_0$ for generators satisfying Hypothesis 2.1) with exact graph descriptions of length $L_h\le h^{d}$ and $\chi(\Delta_h,e_h)\le K\log h$, for fixed constants $c_0>0$ and $d,K\ge0$. Then $\mathrm{SAT}\notin\mathrm{P}/\mathrm{poly}$, and hence $\mathrm{P}\ne\mathrm{NP}$. In particular, descriptions of length $h^{O(1)}$ with $\Delta_h=e_h$ would suffice, with no bound on $\Delta_h$. We do not know whether such descriptions exist, and nothing in this paper constructs one.

## 4 Separated expansion and the least non-output

### 4.1 Additive expansion under a shared outer block

Let $z$ be a block of existential variables preceding all other bound variables, and let $Y_1,\dots,Y_t$ be pairwise disjoint lists of bound variables with local prefixes $Q_1,\dots,Q_t$. A global prefix $Q$ is any interleaving of the $Q_i$ that preserves each local order. Each residual system $\Gamma_i$ depends only on $(x,z,Y_i)$.

**Theorem 4.1.** (Separation)

$$
\exists z\,QY\Bigl[\textstyle\bigwedge_i\Gamma_i(x,z,Y_i)=0\Bigr]
  \iff
  \exists z\textstyle\bigwedge_i\bigl[Q_iY_i\,\Gamma_i(x,z,Y_i)=0\bigr].
$$

*Proof.* Fix $x,z$. For $\mathsf Q\in\{\exists,\forall\}$ and $y$ not occurring in $\beta$, $\mathsf Qy(\alpha\wedge\beta)\iff(\mathsf Qy\,\alpha)\wedge\beta$, because the domain of $y$ is nonempty. Moving the global prefix inward from the innermost quantifier, each quantifier binds a variable of exactly one $Y_i$ and moves into that factor; local orders are unchanged. $\square$

The block $z$ is shared and must not be duplicated: $(z=0)\wedge(z=1)$ is false with one $z$ and satisfiable with two. Variables shared by several factors and quantified after local challenges are not covered.

Apply Theorem 3.1 to each factor with $(x,z)$ treated as free; let $\Delta_i$ be the local effective universal dimension, $s_{ij}$ the number of retained local universal variables before the $j$-th retained existential variable of factor $i$, and $L_i$ the length of factor $i$ (shared subcircuits duplicated).

**Theorem 4.2.** (Additive expansion) The relation of Theorem 4.1 is equivalent to a pure existential relation with witness length $|z|+\sum_i\sum_j2^{s_{ij}}$ and a verifier of size $\sum_{i=1}^t2^{\Delta_i}\operatorname{poly}(L_i+|x|+|z|+t)$.

*Proof.* By Theorem 4.1, for fixed $z$ it suffices to certify each local game. Apply Theorem 3.2 to each factor, quantify the disjoint tables next to one $z$ block, and conjoin the local verifiers with their $x,z$ wires identified. $\square$

**Example 4.3.** For $t$ independent components $\forall u_i\forall v_i\exists w_i\,[w_i=u_iv_i]$, the global core has $\Delta=2t$ while every $\Delta_i=2$, so the separated verifier has $4t$ copies. A large global $\Delta$ is therefore a cost of the compiler of Theorem 3.2, not a lower bound.

### 4.2 The least non-output relation

Let $G$ satisfy Hypothesis 2.1, let $P(z)=0^{N-1}z$ for $z\in\mathbb{F}_2^{N+1}$, and let $\mathrm{Eq}$ and $\mathrm{Lt}$ be the indicator circuits of equality and of integer order. Since at most $2^N$ of the $2^{N+1}$ words $0^{N-1}z$ lie in $\operatorname{Range}G$, the least non-output is $B_0=P(z_0)$ for some $z_0$. With free $(a,b)$, prefix $\exists z\,\forall(s,v)\,\exists t$, $|s|=|t|=N$, $|v|=N+1$, consider the residuals

$$
R_1=\mathrm{Eq}(G(s),P(z)),\quad
  R_2=\mathrm{Lt}(v,z)\bigl[1+\mathrm{Eq}(G(t),P(v))\bigr],\quad
  R_3=P(z)[a]+b .
$$

They vanish for every challenge exactly when $P(z)\notin\operatorname{Range}G$, every smaller candidate is an output, and $b=P(z)[a]$; hence the relation is the bit graph of $B_0$. The words $P(z)$ form the initial segment $\{0,\dots,2^{N+1}-1\}$ of $\mathbb{F}_2^{2N}$ in integer order, the words below $P(z)$ are exactly the $P(v)$ with $v<z$, and the first two constraints force $z=z_0$ independently of $(a,b)$. By Theorem 4.1,

$$
\exists z\bigl[(\forall s\,R_1=0)\wedge(\forall v\,\exists t\,R_2=0)\wedge(R_3=0)\bigr], \tag{4.1}
$$

so a winning response can be chosen as $t=t(v)$, independently of $s$. With $\kappa=\operatorname{rank}[B;A]$ for a fixed XOR–AND circuit of $G$, the local effective dimensions in (4.1) are at most $\kappa$, $N+1$ and $0$, against at most $N+1+\kappa$ for the monolithic system. Both counts remain $2^{O(N)}$, so this is not an address-scale description. (In Example 4.3 each local formula is valid; the example only compares the copy counts of the two compilers.)

**Lemma 4.4.** (Synthesis) For $k\ge8$ every function $\mathbb{F}_2^k\to\mathbb{F}_2$ has a circuit with fewer than $18\cdot2^k/k$ gates.

*Proof.* Let $d=2^b$ be the largest power of two with $d\le k-\lceil\log_2k\rceil$, and $a=k-b$. Use $k$ negations; all minterms of the $a$ left and the $b$ right variables by prefix trees ($2^{a+1}-4$ and $2^{b+1}-4$ AND gates); all $2^d-d-1$ ORs of at least two of the $d$ right minterms; one AND per left minterm with the selected OR; and a final OR of the $2^a$ terms (terms with an empty selection are omitted, and the constant function uses one extra gate). The total is at most $k+4\cdot2^a+d+2^d-10+1$. For $k\ge8$, $\lceil\log_2k\rceil\le k/2$, so $d>k/4$, $4\cdot2^a=4\cdot2^k/d<16\cdot2^k/k$, $2^d\le2^k/k$ and $k+d\le2k\le2^k/k$. Hence the total is below $18\cdot2^k/k$. $\square$

**Lemma 4.5.** (Trailing window) Let $\ell=N/1024$. Under Hypothesis 2.1, every word $0^{2N-\ell}y$ with $|y|=\ell$ lies in $\operatorname{Range}G$.

*Proof.* The last $\ell$ positions are the addresses whose $11$ high bits are all one. Compute an arbitrary function of the $k=q-10\ge 10$ low bits by Lemma 4.4 and conjoin it with the AND of the $11$ high bits (at most $11$ gates). Using $q/(q-10)\le2$ and $N\ge440q$ for $q\ge20$, the size is at most $18\ell/(q-10)+11\le\tfrac{36}{1024}\tfrac{N}{q}+\tfrac{1}{40}\tfrac{N}{q}
<\tfrac{N}{10q}$. $\square$

**Theorem 4.6.** (Response lists) Under Hypothesis 2.1, $\mathrm{val}(B_0)\ge2^{\ell}$, and in every assignment of correct responses $t_v$ (with $G(t_v)=P(v)$) to all candidates $v<z_0$, the map $v\mapsto t_v$ is injective. Hence every explicit response list for the challenge $\forall v\,\exists t$ in (4.1), even after deduplication, has at least $2^{N/1024}=2^{2^{h-11}}$ distinct entries. Moreover $\operatorname{rank}[B;A]\ge\ell$ for every representation of $G$.

*Proof.* By Lemma 4.5 every integer below $2^{\ell}$ is an output, so the least non-output is at least $2^{\ell}$. Equal responses force equal outputs $P(v)$, and $P$ is injective. Finally $G$ factors through $q\mapsto[B;A]q$, so $2^{\ell}\le|\operatorname{Range}G|\le2^{\operatorname{rank}[B;A]}$. $\square$

This bounds only literal response lists. It says nothing about a short circuit computing a response rule $v\mapsto t(v)$; such a rule would still need a proof of $G(t(v))=P(v)$ for all $v<z_0$, where $v$ has $N+1$ bits.

## 5 Target-period quotients and the canonical profile

In this section $G:\mathbb{F}_2^N\to\mathbb{F}_2^M$ is an arbitrary map, seed coordinates keep their physical order, and $\zeta\in\operatorname{Range}G$. Put

$$
S_\zeta=G^{-1}(\zeta),\qquad
  P_\zeta=\{u:S_\zeta+u=S_\zeta\},\qquad
  c_\zeta=N-\dim P_\zeta . \tag{5.1}
$$

$P_\zeta$ is a subspace and $S_\zeta$ is a union of $P_\zeta$-cosets.

**Theorem 5.1.** (Coarsest linear quotient) The minimum rank of a linear map $H$ through which membership in $S_\zeta$ factors is $c_\zeta$, and the minimum number of cosets of one common subspace whose union is $S_\zeta$ is $K^*_\zeta=|S_\zeta|/2^{\dim P_\zeta}$. Both are attained with $\ker H=P_\zeta$.

*Proof.* If membership factors through $H$, then $\ker H\subseteq P_\zeta$. The common direction space of a coset cover lies in $P_\zeta$. $\square$

These are optima of linear quotient rank and coset count, not of description length.

##### Whole-generator versus target quotients.

For a representation $G(q)=Aq+F(Bq)$ with $C=[B;A]$ of rank $c$, $\ker C\subseteq P(G)\subseteq P_\zeta$, where $P(G)=\{u:G(\cdot+u)=G\}$. For each compatible signature $\sigma$ the solutions of $Cq=(\sigma,\zeta+F(\sigma))$ form one $\ker C$-coset, so the number of compatible signatures is

$$
T_\zeta=|S_\zeta|/2^{N-c}=K^*_\zeta\,2^{\,c-c_\zeta}. \tag{5.2}
$$

Over all representations, the minimum of $c$ is $N-\dim P(G)$, which can differ greatly from $c_\zeta$. For example, if $G(q)=0$ when $q_1=0$ and $G(q)=q$ otherwise, then $P(G)=0$ but $S_0$ is the hyperplane $q_1=0$, so $c_0=1$ while every representation has $c=N$. In general only $c_\zeta\le c$ holds, so lower bounds on whole-generator rank (Section 6) do not transfer to $c_\zeta$.

### 5.1 Order-compatible section

Let $U\subseteq P_\zeta$ be a subspace, $H$ a full-row-rank matrix with $\ker H=U$ and columns $h_1,\dots,h_N$. Scan the columns from right to left and keep a column when it is independent of those kept so far; let $I$ be the kept positions and $V_I=\operatorname{span}\{e_i:i\in I\}$.

**Theorem 5.2.** (Lexicographic section) $\mathbb{F}_2^N=U\oplus V_I$, and for every $\alpha\in\operatorname{im}H$ the unique element of $H^{-1}(\alpha)\cap V_I$ is the lexicographically least element of $H^{-1}(\alpha)$.

*Proof.* Let $0\ne u\in U$ have first nonzero coordinate $j$. From $Hu=0$, $h_j=\sum_{k>j}u_kh_k$ lies in the span of the later columns, which is the span of the later kept columns; so $j\notin I$. Hence no nonzero vector of $U$ is supported in $I$, and $\dim U+|I|=N$ gives the direct sum. If $v\in V_I$ then $v_j=0$, so $v+u$ agrees with $v$ before $j$ and is larger at $j$. $\square$

$I$ depends only on $U$ and the coordinate order: it is the complement of the set of first-nonzero positions of vectors in $U$. Ordering by syndrome coordinates instead is wrong in general: for $U=0$, $H(q_1,q_2)=(q_2,q_1)$ and $S=\{01,10\}$, the least seed $01$ has the larger syndrome $10$. Left-pivot selection is also wrong in general.

### 5.2 One quotient for the whole canonical search

Let $L_U\subseteq V_I$ be the set of least elements of the cosets $v+U$, $v\in S_\zeta$. Then $S_\zeta=\bigsqcup_{v\in L_U}(v+U)$ and the canonical preimage $q^*=\operatorname{min_{lex}}S_\zeta$ equals $\operatorname{min_{lex}}L_U$.

**Lemma 5.3.** (Canonical prefixes) If $p$ is a prefix of $q^*$ and $v\in L_U$, then $v+U$ contains a seed with prefix $p$ if and only if $v$ has prefix $p$.

*Proof.* Let $w\in v+U$ have prefix $p$, so $v\le w$. If $v$ first differs from $p$ inside $p$ with a larger bit, then $v>w$; with a smaller bit, $v<q^*$, contradicting $v\in S_\zeta$. $\square$

The lemma fails for prefixes that are not canonical: for $S=U=\{00,11\}$ and prefix $1$, the coset contains $11$ but its least element is $00$.

Partition the seed coordinates into consecutive chunks of widths $b_1,\dots,b_R$. Write $H_{\ge i}$ and $H_{>i}$ for the column submatrices of chunks $\ge i$ and $>i$, and set

$$
\kappa_i=\operatorname{rank}H_{\ge i}-\operatorname{rank}H_{>i}, \tag{5.3}
$$

the number of kept positions in chunk $i$; thus $\sum_i\kappa_i=\operatorname{rank}H$. Let $p$ be the restriction of $q^*$ to chunks $<i$, let $E_i$ be the set of values of chunk $i$ over seeds in $S_\zeta$ with prefix $p$, let $A_{i-1}\subseteq L_U$ be the representatives with prefix $p$, and let $J_i$ be the number of distinct chunk-$i$ values over $A_{i-1}$.

**Theorem 5.4.** (Exact chunk counts)

$$
|E_i|=2^{\,b_i-\kappa_i}\,J_i , \tag{5.4}
$$

and chunk $i$ of $q^*$ is the least chunk-$i$ value over $A_{i-1}$.

*Proof.* By Lemma 5.3, the seeds with prefix $p$ are the sets $v+U_p$, $v\in A_{i-1}$, where $U_p=\{u\in U:u=0\text{ on chunks }<i\}$, which is identified with $\ker H_{\ge i}$. The projection $D_i$ of $U_p$ to chunk $i$ has kernel identified with $\ker H_{>i}$, so $\dim D_i=b_i-\kappa_i$. The values of chunk $i$ reachable from $v$ are $v|_i+D_i$, and $v|_i$ is the least element of this coset (a smaller one would give an element of $v+U$ below $v$). So two representatives give the same coset exactly when their chunks coincide, and distinct cosets are disjoint. This gives (5.4). The least feasible chunk is the least representative chunk, which is the chunk of $q^*$. $\square$

No uniformity of suffix multiplicities is assumed; $J_i$ counts distinct values, not leaves.

**Corollary 5.5.** (Row ranks) Let $\rho_i=b_i-\dim P(E_i)$, where $P(E_i)$ is the translation stabilizer of $E_i$. Then $\rho_i\le\kappa_i$, $2^{\kappa_i-\rho_i}$ divides $J_i$, and

$$
\kappa_i\le\rho_i+\log_2J_i,\qquad \sum_{i=1}^R\kappa_i=\operatorname{rank}H . \tag{5.5}
$$

Moreover, let $\Lambda_i=\{v|_i:v\in A_{i-1}\}$ be the realized chunk values (so $J_i=|\Lambda_i|$), $w_i(\gamma)$ the number of representatives in $A_{i-1}$ with chunk value $\gamma$, and $\gamma_i^*$ the chunk of $q^*$. Then $|L_U|-1=\sum_i(J_i-1)+\sum_i\sum_{\gamma\in\Lambda_i\setminus\{\gamma_i^*\}}(w_i(\gamma)-1)$.

*Proof.* $E_i$ is a union of $D_i$-cosets, so $D_i\subseteq P(E_i)$, and each $P(E_i)$-coset is a union of $2^{\kappa_i-\rho_i}$ cosets of $D_i$. With $K_i=|A_i|$, the identity telescopes $K_{i-1}-K_i=\sum_{\gamma\in\Lambda_i\setminus\{\gamma_i^*\}}w_i(\gamma)$ from $K_0=|L_U|$ to $K_R=1$. $\square$

For $U=P_\zeta$ one has $|L_U|=K^*_\zeta$ and $\operatorname{rank}H=c_\zeta$. Per-row symmetry does not lift to the fiber: $S=\{00,01,10\}$ has $P_\zeta=0$, but both canonical rows have $\rho_i=0$.

##### Coarsening an explicit quotient.

If $S_\zeta=H^{-1}(\Lambda)$ with $\ker H=U$ and $P(\Lambda)$ is the stabilizer of $\Lambda$ in $\operatorname{im}H$, then $P_\zeta=H^{-1}(P(\Lambda))$ and $|\Lambda/P(\Lambda)|=K^*_\zeta$. From an explicit list of $K$ labels, $P(\Lambda)$ is found with $O(K^2)$ set operations; this is an explicit-input procedure and is exponential when $K$ is.

## 6 Global rank and a canonical-path budget

Let $G:\mathbb{F}_2^N\to\mathbb{F}_2^{2N}$ satisfy Hypothesis 2.1, $\ell=N/1024$, and split the $2N$ output positions into $s=2048$ aligned blocks $I_j$ of length $\ell$ (fixed values of the $11$ high address bits). Let $U_j$ be the words supported on $I_j$.

**Lemma 6.1.** (Blocks) $U_j\subseteq\operatorname{Range}G$ for every $j$.

*Proof.* As in Lemma 4.5, now testing equality of the high bits with $j$ (at most $11$ negations and $11$ AND gates): the size is at most $18\ell/(q-10)+22<N/(10q)$. $\square$

Only each block individually is claimed to lie in the range.

**Lemma 6.2.** (Affine quotient) Let $G(q)=Aq+F(Bq)$ map $\mathbb{F}_2^n\to\mathbb{F}_2^m$ with $\operatorname{rank}B=r$, and suppose the output coordinates split into $s\ge2$ blocks whose coordinate subspaces $U_j$ lie in $\operatorname{Range}G$. Let $W=A(\ker B)$ and $K=|\pi_W(\operatorname{Range}G)|$, where $\pi_W:\mathbb{F}_2^m\to\mathbb{F}_2^m/W$. Then

$$
2^r\ge K,\qquad r\ge\log_2K\ge\Bigl\lceil\frac{m-n}{s-1}\Bigr\rceil .
$$

*Proof.* The seeds with $Bq=\sigma$ form a coset of $\ker B$ and map into $G(q_0)+W$, so $K\le2^r$. Each $\pi_W(U_j)$ is a subspace inside $\pi_W(\operatorname{Range}G)$, so its dimension is at most $a=\lfloor\log_2K\rfloor$. These subspaces span $\mathbb{F}_2^m/W$, of dimension $m-\dim W\ge m-(n-r)$. Hence $sa\ge m-n+r\ge m-n+a$, and $a\ge(m-n)/(s-1)$ with $a$ an integer. $\square$

**Theorem 6.3.** (Global rank) Every representation of $G$ has $\operatorname{rank}B\ge\lceil N/2047\rceil$.

*Proof.* Apply Lemma 6.2 with $m=2N$, $n=N$, $s=2048$ and Lemma 6.1. $\square$

**Remark 6.4.** (AND gates) The number of AND gates is easier to bound. Hypothesis 2.1 puts the zero word and every unit word (an address-equality test, at most $2q+1$ gates) in $\operatorname{Range}G$, so the affine span of $\operatorname{Range}G$ is $\mathbb{F}_2^{2N}$. A circuit with $t$ AND gates in normal form has $\operatorname{Range}G\subseteq c+\operatorname{im}[A\
D]$, of affine dimension at most $N+t$; hence $t\ge N$. This does not imply $\operatorname{rank}B\ge N$, since $\operatorname{rank}B$ can be much smaller than the number of AND gates; Theorem 6.3 and Corollary 6.5 concern $\operatorname{rank}B$ and the signature cloud, which the affine-span argument does not control.

**Corollary 6.5.** (Global signature cloud) With $C=[B;A]$ and $g(\sigma)=(\sigma,F(\sigma))$, the deduplicated cloud $T_{\mathrm{all}}=\{g(\sigma)\bmod\operatorname{im}C:\sigma\in\mathbb{F}_2^r\}$ has $|T_{\mathrm{all}}|=|\pi_W(\operatorname{Range}G)|\ge2^{\lceil N/2047\rceil}$.

*Proof.* The map $\phi(y)=(0,y)\bmod\operatorname{im}C$ has kernel $W$. If $Bq=\sigma$, then $g(\sigma)+(0,G(q))=(Bq,Aq)\in\operatorname{im}C$, so $T_{\mathrm{all}}=\phi(\operatorname{Range}G)$, which has $K$ elements. Lemmas 6.1 and 6.2 give $\log_2K\ge\lceil N/2047\rceil$. $\square$

Any procedure that first materializes this cloud therefore writes exponentially many records. This is an output-size statement about that step, not a time lower bound for all algorithms.

##### Canonical-path budget.

Fix $\zeta\in\operatorname{Range}G$, its canonical preimage $q^*$, and $R$ consecutive seed chunks. Apply Section 5 with $U=\ker C\subseteq P_\zeta$ and $H$ a row basis of $C$; then (5.4) holds with $\kappa_i=\operatorname{rank}C_{\ge i}-\operatorname{rank}C_{>i}$, and (5.5) holds with $J_i$ the number of labels of the $\ker C$-quotient in row $i$.

**Theorem 6.6.** (Rank/label budget) For every representation of $G$ and every $\zeta\in\operatorname{Range}G$,

$$
\sum_{i=1}^R(\rho_i+\log_2J_i)\ \ge\ \operatorname{rank}C\ \ge\ \ell+11=\frac{N}{1024}+11 ,
$$

so some canonical row has $\rho_i\ge(\ell+11)/(2R)$ or $J_i\ge2^{(\ell+11)/(2R)}$. If all $\rho_i\le\mu$, then $\max_i\log_2J_i\ge(\ell+11)/R-\mu$.

*Proof.* The blocks $U_j$ of Lemma 6.1 have dimension $\ell$, pairwise intersect only in $0$, and lie in $\operatorname{Range}G$, so $|\operatorname{Range}G|\ge|\bigcup_jU_j|=1+2048(2^\ell-1)=2^{\ell+11}-2047$ (only the union is used, not the sum of the $U_j$). Since $G(q)$ depends on $q$ only through $Cq$, also $|\operatorname{Range}G|\le2^{\operatorname{rank}C}$. As $\ell\ge1$, $2^{\ell+11}-2047>2^{\ell+10}$, and $\operatorname{rank}C$ is an integer, so $\operatorname{rank}C\ge\ell+11$. Sum (5.5) and apply the pigeonhole principle over the $R$ rows. $\square$

The range count bounds $\operatorname{rank}C$ directly; the affine-quotient argument of Lemma 6.2, with its denominator $2047$, is needed only for the nonlinear input rank $\operatorname{rank}B$ (Theorem 6.3) and for the deduplicated cloud (Corollary 6.5).

**Corollary 6.7.** (Exact budget slack) In the setting of Section 5, let $K_i^{\mathrm{row}}=|E_i|/|P(E_i)|$, a positive integer that depends only on $S_\zeta$, $q^*$ and the chunking, not on $U$. Then

$$
\rho_i+\log_2J_i=\kappa_i+\log_2K_i^{\mathrm{row}},\qquad
  \sum_{i=1}^R(\rho_i+\log_2J_i)=\operatorname{rank}H+\sum_{i=1}^R\log_2K_i^{\mathrm{row}} .
$$

If $U\subseteq V\subseteq P_\zeta$, then $J_i(U)=2^{\kappa_i(U)-\kappa_i(V)}J_i(V)$. In particular, for $U=\ker C$ and $V=P_\zeta$, $\sum_i\log_2(J_i/J_i^*)=\operatorname{rank}C-c_\zeta$.

*Proof.* By (5.4), $|E_i|=2^{b_i-\kappa_i}J_i$, and $|P(E_i)|=2^{b_i-\rho_i}$; divide. $E_i$ is nonempty (it contains the chunk of $q^*$) and is a union of $P(E_i)$-cosets, so $K_i^{\mathrm{row}}$ is a positive integer. Since $E_i$ and $\rho_i$ do not depend on the quotient, comparing the identity for $U$ and $V$ gives the coarsening formula; summing over $i$ and using $\sum_i\kappa_i=\operatorname{rank}H$ gives the rest. $\square$

For example, $S=\{00,01\}$ with one-bit chunks has $(J_1,J_2)=(1,2)$ for $U=0$ and $(J_1^*,J_2^*)=(1,1)$ for $V=P(S)=S$, while $(\rho_1,\rho_2)=(1,0)$ in both cases; the total logarithmic label count drops by $1=2-1$. Thus coarsening from the whole-generator quotient $\ker C$ to the target-period quotient $P_\zeta$ reduces the total logarithmic label count by exactly $\operatorname{rank}C-c_\zeta$, and the remaining slack in the budget is $\sum_i\log_2K_i^{\mathrm{row}}$, which depends only on the feasible row sets.

### 6.1 What the budget measures

1.  *It is representation-relative.* The labels $J_i$ are those of the quotient by $\ker C$, the kernel of a whole-generator representation. Each summand $\rho_i+\log_2J_i$ is at least $\kappa_i$, so Theorem 6.6 is a termwise consequence of $\sum_i\kappa_i=\operatorname{rank}C$ and the range count; Corollary 6.7 identifies the termwise slack exactly. Its content is the distribution of a global rank along one canonical path, not a new intrinsic invariant of the rows.

2.  *It does not transfer to the target-intrinsic quotient.* With $U=P_\zeta$ the same argument gives $\sum_i(\rho_i+\log_2J_i^*)\ge c_\zeta$ with $J_i^*\le J_i$ (by Corollary 6.7, the total loss is exactly $\operatorname{rank}C-c_\zeta$), and coverage alone does not give a lower bound on $c_\zeta$ that grows with $N$ uniformly over all targets (only $c_\zeta\ge1$ holds, since $G$ is not constant). Indeed, let $G$ output $0^{2N}$ when the first seed bit is $0$, and otherwise apply the truth-table generator of Remark 2.2 to the remaining $N-1$ bits, replacing the output $0^{2N}$ by a fixed unit word. This $G$ satisfies Hypothesis 2.1, while $G^{-1}(0^{2N})$ is the hyperplane $\{x_1=0\}$, so $c_{0}=1$. Whether the specific canonical targets of a reconstruction procedure have large $c_\zeta$ is open. The alternative “$J_i$ is exponential” may disappear after target-specific coarsening; only the $\rho_i$ are intrinsic.

3.  *Many labels are not a circuit lower bound.* A linear space has exponentially many labels and a tiny description.

Accordingly, Theorem 6.6 and Corollary 6.5 exclude a class of methods: “enumerate the global signature cloud, deduplicate, then restrict to the target” cannot run at address scale for any generator satisfying Hypothesis 2.1. Similarly, if all $\rho_i\le\mu$, then listing the realized labels of all rows of the $\ker C$-quotient writes $\sum_iJ_i\ge 2^{(\ell+11)/R-\mu}$ records; with $R=\operatorname{poly}(h)$ rows and $\mu=\operatorname{poly}(h)$ this is exponential in $h$. (With $R=N$ one-bit chunks every $J_i\le2$, but the total explicit output $\sum_iJ_i$ along the path then lies between $N$ and $2N$, itself exponential in $h$.) A target-first quotient, or any implicit description, is not addressed.

## 7 Open questions

1.  Is there a $\operatorname{poly}(h)$-length XOR–AND description of the bit graph of $B_0$, or of any word of circuit complexity $2^{\Omega(h)}$, with $\chi(\Delta,e)=O(\log h)$ (for instance, with $\Delta=e$)? By Corollary 3.6, a positive answer would give $\mathrm{SAT}\notin\mathrm{P}/\mathrm{poly}$.

2.  Is there a nontrivial lower bound on the target-intrinsic rank $c_\zeta$, or on $K^*_\zeta$, for the canonical targets of a coverage generator?

3.  Can a short circuit compute a correct response rule $v\mapsto t(v)$ in (4.1), with a short proof of correctness?

## Appendix A. Finite checks

The supplementary script `finite_checks.py` (Python standard library, exact integer and rational arithmetic, fixed random seed) checks Theorem 3.1 on $1500$ random systems ($6000$ free inputs); the gate tally of the construction in Lemma 4.4 and the bound $<18\cdot2^k/k$ for $8\le k\le2000$ and the truth tables of the construction for $k=8,9$; the inequality of Lemma 4.5 for $20\le q\le2000$; Theorem 4.1 on $3000$ random two-factor systems; Theorems 5.2 and 5.4, Lemma 5.3 and the divisibility of Corollary 5.5 on all $273$ nonempty fibers with $N\le3$ (every $U\subseteq P_\zeta$ and every chunk composition) and on $600$ random fibers with $N=4$; and Lemma 6.2 and Corollary 6.5 on random small representations. These are finite sanity checks; the general statements rest on the proofs above.

## References

[1] E. Jeřábek. Dual weak pigeonhole principle, Boolean complexity, and derandomization. *Annals of Pure and Applied Logic*, 129(1–3):1–37, 2004. doi:10.1016/j.apal.2003.12.003.

[2] O. Korten. The hardest explicit construction. In *Proc. 62nd IEEE Symposium on Foundations of Computer Science (FOCS)*, pages 433–444, 2021. doi:10.1109/FOCS52979.2021.00051.

[3] L. Chen, S. Hirahara, and H. Ren. Symmetric exponential time requires near-maximum circuit size. In *Proc. 56th ACM Symposium on Theory of Computing (STOC)*, pages 1990–1999, 2024. doi:10.1145/3618260.3649624.

[4] Z. Li. Symmetric exponential time requires near-maximum circuit size: simplified, truly uniform. In *Proc. 56th ACM Symposium on Theory of Computing (STOC)*, pages 2000–2007, 2024. doi:10.1145/3618260.3649615.

[5] H. Ren and R. Williams. Near-maximum circuit lower bounds for exponential time with Merlin–Arthur queries. arXiv:2607.09963, 2026.

[6] L. Chen, S. Hirahara, Z. Li, and H. Ren. Symmetric exponential time requires near-maximum circuit size. *Journal of the ACM*, 73(1), 2026. doi:10.1145/3778166.

[7] M. Janota and J. Marques-Silva. Expansion-based QBF solving versus Q-resolution. *Theoretical Computer Science*, 577:25–42, 2015. doi:10.1016/j.tcs.2015.01.048.

[8] A. Ge-Ernst, C. Scholl, J. Síč, and R. Wimmer. Solving dependency quantified Boolean formulas using quantifier localization. *Theoretical Computer Science*, 925:1–24, 2022. doi:10.1016/j.tcs.2022.03.029.

[9] L. Eriksson, V. Lagerkvist, S. Ordyniak, G. Osipov, F. Panolan, and M. Rychlicki. Backdoors for quantified Boolean formulas. arXiv:2604.15927, 2026.

[10] O. B. Lupanov. On a method of circuit synthesis. *Izvestiya VUZ, Radiofizika*, 1:120–140, 1958 (in Russian).

[11] S. A. Lozhkin and A. E. Shiganov. On a modification of Lupanov's method with more uniform distribution of fan-out. ECCC TR11-130, 2011.

[12] P. Gopalan, R. O'Donnell, R. A. Servedio, A. Shpilka, and K. Wimmer. Testing Fourier dimensionality and sparsity. *SIAM Journal on Computing*, 40(4):1075–1100, 2011. doi:10.1137/100785429.

[13] S. Sanyal. Fourier sparsity and dimension. *Theory of Computing*, 15(11):1–13, 2019. doi:10.4086/toc.2019.v015a011.

[14] Ç. Çalık, M. Sönmez Turan, and R. Peralta. Boolean functions with multiplicative complexity 3 and 4. *Cryptography and Communications*, 12:935–946, 2020. doi:10.1007/s12095-020-00445-z.

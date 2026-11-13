# Every entry of the turned cyclic Latin hypercube lies in a transversal

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

## 1. Problem and contribution

A $d$-dimensional Latin hypercube of order $n$ is a map $H:\mathbb{Z}_n^d\to\mathbb{Z}_n$ such that any two distinct cells that agree in $d-1$ coordinates carry distinct symbols. A transversal of $H$ is a set $T$ of $n$ cells such that, for each $k\in\{1,\dots,d\}$, the $k$-th coordinates of the cells of $T$ are pairwise distinct, and the symbols $H(x)$, $x\in T$, are pairwise distinct. An entry of $H$ is a cell together with its symbol. We follow the terminology of Child and Wanless [1].

Throughout, $n=2m$ with $m\ge 2$, $d\ge 2$ is even,

$$
I=\{0,m\}\subset\mathbb{Z}_n,\qquad I_d=I^d\subset\mathbb{Z}_n^d ,
$$

and

$$
H_{d,n}(x_1,\dots,x_d)=x_1+\dots+x_d+m\cdot[x\in I_d]\in\mathbb{Z}_n ,
$$

where $[x\in I_d]$ is $1$ if $x\in I_d$ and $0$ otherwise. The cyclic hypercube $(x_1,\dots,x_d)\mapsto x_1+\dots+x_d$ has no transversal when $n$ and $d$ are both even [1, Theorem 2]; for $d=2$ this is Euler's theorem that the addition table of $\mathbb{Z}_n$, $n$ even, has no transversal [2, Theorem 2.2] (see also [2, Theorem 10.11] for higher even dimensions). Child and Wanless obtained $H_{d,n}$ from the cyclic hypercube by replacing its subhypercube of order $2$ on $I_d$ by the other subhypercube of order $2$ on the same two symbols ("turning" it). In the proof of [1, Theorem 4] they showed that $H_{d,n}$ has a transversal, given explicitly in [1, display (6)], and that every transversal of $H_{d,n}$ contains a cell of $I_d$, so that $H_{d,n}$ has at most $2^d$ disjoint transversals. They remarked that the $2^d$ translates of the transversal (6) by vectors of $I_d$ are disjoint transversals and, based on computations for small $(n,d)$, conjectured that every entry of $H_{d,n}$ lies in a transversal [1, p. 5]. In the terminology of [1], the conjecture asserts that $H_{d,n}$ is not a confirmed bachelor.

**Theorem 1.1.** Let $d\ge 2$ and $n\ge 4$ be even. Every entry of $H_{d,n}$ lies in a transversal of $H_{d,n}$.

The proof is constructive: for every cell $y$ it produces, by an explicit recursion on $d$, a transversal through $y$.

*Contribution.*

- Unconditional: Theorem 1.1 for all even $d\ge 2$ and all even $n\ge 4$, which proves the conjecture of [1, p. 5]. The new ingredients are the two-parameter families of transversals of $H_{2,n}$ (Section 3.1), the coverage statements for them (Theorem 3.3 and Propositions 3.6 and 3.7), and the reductions from dimension $d$ to dimensions $d-2$ and $2$ (Section 4).
- Supporting computation: a Python implementation of the construction and an independent checker, which verify one transversal through each of the $328{,}760$ cells of $H_{d,n}$ for the $11$ pairs $(n,d)$ listed in Table 1, and finite checks of the explicit formulas of Sections 2 and 3 over the parameter ranges stated in Section 5 (up to $n=100$). These checks support the proof; they do not replace it.
- Not claimed: the definition of $H_{d,n}$, the existence of a transversal, the bound $2^d$ on the number of disjoint transversals and the $2^d$ disjoint translates are due to [1]. Lemma 2.1 below is a direct consequence of the $\Delta$-lemma [1, Lemma 1]. For $(n,d)=(4,4)$ the conclusion of Theorem 1.1 also follows from the enumeration of the $27$ species of order $4$ and dimension $4$ reported in [1, display (1) and Section 2, p. 5]: the unique species obtained from $\mathbb{Z}_4^4$ by turning one subhypercube of order $2$ is among the $23$ species that have a transversal through every entry. We prove nothing about other Latin hypercubes, about Conjecture 1 of [1] (odd $n$ or odd $d$), about the number of transversals through an entry, or about decompositions of $H_{d,n}$ into transversals.

*Outline.* Section 2 collects the symmetries of $H_{d,n}$ and an elementary bijection lemma. Section 3 treats $d=2$: we build transversals $T_{N,a}$ of $H_{2,n}$ from that bijection, show that their images under the symmetries cover every cell, and prove two finer coverage properties of their normalized forms. Section 4 proves Theorem 1.1 by induction on $d$ in steps of two. If two entries of the graph tuple $(y_1,\dots,y_d,-H_{d,n}(y))$ of the target cell $y$ sum to an element of $I$, a transversal of $H_{d-2,n}$ lifts directly; otherwise transversals of $H_{d-2,n}$ and $H_{2,n}$ are glued along a transversal of $H_{2,n}$ whose cells are pairs of symbols, and the two coverage properties guarantee that compatible pieces exist. Section 5 describes the computations.

### 1.1 Related work and distinction

The source of the problem is [1]. Its Section 2 constructs Latin hypercubes of even order and dimension with restricted transversals, including an infinite family of confirmed bachelors [1, Theorem 3, display (3)], the three species of confirmed bachelors for $(n,d)=(4,4)$ [1, displays (4)–(5), pp. 4–5], and the family $H_{d,n}$ of [1, Theorem 4]; for $H_{d,n}$ it gives one explicit transversal [1, display (6)] and its $2^d$ translates. Its Section 3 studies $G$-extensions $L'(x_1,\dots,x_{d'})=L(x_1,\dots,x_d)+x_{d+1}+\dots+x_{d'}$ of a hypercube $L$ [1, display (2)], characterizes the entries of $L'$ that lie in transversals through suitable diagonals of $L$ [1, Theorem 6], and deduces high-dimensional hypercubes with confirmed-bachelor entries or entries shared by all transversals [1, Corollaries 7–10, Theorems 12–13, Corollary 14]. Because the correction term $m\cdot[x\in I_d]$ in $H_{d,n}$ depends on all $d$ coordinates simultaneously, $H_{d,n}$ is not a nontrivial $G$-extension for $d\ge 4$, and [1, Theorem 6] does not apply to it directly. Our lifting step (Lemma 4.1) adds two coordinates with constant sum, in the spirit of the extension step in the proof of [1, Theorem 6]; the gluing step (Lemma 4.3) and the two-dimensional coverage results have no counterpart in [1].

Section 4 of [1] uses $\lambda$-dilations [1, Section 4, p. 10 and Lemmas 17–18] to embed a Latin hypercube of base order $n_0$ into order $\lambda n_0$ by replacing a subhypercube of order $n_0$. Under that definition, $H_{d,n}$ ($n=2m$) is the $m$-dilation of the order-$2$ Latin hypercube $K(u_1,\dots,u_d)=u_1+\dots+u_d+1\pmod 2$, since outside $I_d=\{0,m\}^d$ the $m$-dilation agrees with the cyclic hypercube and on a cell $x=mu\in I_d$ its symbol is $mK(u)\equiv x_1+\dots+x_d+m\pmod{2m}$. The parity hypothesis of [1, Lemmas 17–18]—that the base order $n_0$ is even, or the dimension $d$ is odd, or the dilation factor $\lambda$ is odd—holds here because the base order is $n_0=2$ (even), regardless of the parities of $d$ and $\lambda=m$. However, the remaining hypotheses and conclusions of [1, Lemmas 17–18] do not establish Theorem 1.1: in $K$, every entry has $\Delta(u)=1\ne 0$ in $\mathbb{Z}_2$, so the nonzero-$\Delta$ set is $X=K$ with coordinate projections $A_i=\mathbb{Z}_2$ of size $\lvert A_i\rvert=2=n_0$; consequently, a proper partial diagonal $D\subsetneq X$ cannot extend inside $K$ to a full diagonal $E$ satisfying $E\cap X=D$ as required by [1, Lemma 17(ii)], and the projection-sum bound $\sum_{i=1}^d\lvert A_i\rvert\le(d-1)n_0$ of [1, Lemma 18] fails since $\sum_{i=1}^d\lvert A_i\rvert=2d>(d-1)n_0$. Moreover, [1, Lemma 17(i)] lifts $(\mathbb{Z}_2,d)$-suitable diagonals through entries of $K$ only to $(\mathbb{Z}_n,d)$-suitable diagonals of $H_{d,n}$ through entries of $I_d$ (which constrain only the $\Delta$-sum and need not have distinct symbols), and neither lemma addresses entries outside $I_d$ or shows that every entry of $H_{d,n}$ lies in a transversal.

For Latin squares ($d=2$), Egan and Wanless [3] reported a computational study of the transversal-free entries of the Latin squares of order at most $9$, and constructed, for every even $n\ge 10$, a Latin square of order $n$ that has transversals, all of which share a single entry (summarized in [2, Section 3, Table 1, p. 407; Section 4, Tables 2–3 and Theorem 4.3, p. 409]). More recently, Ghafari and Wanless [4, Theorems 1.1, 1.2, and 2.2] constructed, for every even $n\ge 10$, a Latin square $L$ of order $n$ that has a transversal, in which at least $\lfloor n/6\rfloor$ entries occur in every $(\mathbb{Z}_n,2)$-suitable diagonal and hence in every transversal (quoted for even $n\ge 10$ in [1, Theorem 11]), and which has $\tau(L)\ge 19n^2/36+O(n)$ transversal-free entries (where $\tau(L)$ counts the entries of $L$ that lie in no transversal), as well as Latin squares of order $n=3m$ for every odd $m\ge 3$ composed of nine $m\times m$ subsquares each hit by every transversal [4, Theorem 1.3]. Theorem 1.1 is a statement of the opposite kind: every transversal of $H_{d,n}$ is forced through the $2^d$ cells of $I_d$ (Lemma 2.1), yet no entry of $H_{d,n}$ is transversal-free.

Also for Latin squares, Luria [5, Theorem 1 and Corollary 3] studied upper bounds on the minimum number $t(n)$ of transversals in a Latin square of odd order $n$: for every odd $q$ ($n=3q\equiv 3\pmod 6$), shifting a single $q\times q$ block of a $3\times 3$ block cyclic square $L_q$ forces every transversal either to lie entirely in the three diagonal blocks or to avoid all three of them [5, Corollary 3], yielding the asymptotic upper bound $\lvert\mathcal{T}(L_q)\rvert\le\bigl((1+o(1))2n/(3e^2)\bigr)^n$ on the number of transversals [5, Theorem 1]. For $d=2$, $H_{2,n}$ is the addition table of $\mathbb{Z}_n$ with the intercalate on rows and columns $\{0,m\}$ turned, a turn-square in the terminology of [2, Section 7, pp. 421–422, display (7.1)]; turn-squares have likewise mainly been studied for their numbers of transversals (see [2, Section 7] and the references there). We did not find a published proof that every entry of $H_{2,n}$ lies in a transversal for all even $n$; Section 3 proves it, since the induction of Section 4 needs the explicit transversals and their coverage properties and not only their existence.

On 10 November 2026 we searched arXiv, OpenAlex, Crossref, GitHub, Zenodo and the web for the arXiv identifier of [1], the authors' names and the terms "Latin hypercube", "transversal", "turned" and "modified cyclic"; OpenAlex listed no work citing [1]. We also searched the rStation math board. We found no proof of the conjecture of [1, p. 5] and no rStation paper on transversals of Latin squares or hypercubes. This search is limited to the sources named.

## 2. Preliminaries

For integers $a$ and $b$ we write $[a,b]=\{a,a+1,\dots,b\}$, which is empty if $a>b$, and we use the same notation for the image of this set in $\mathbb{Z}_n$. Since $m$ divides $n$, congruence modulo $m$ is well defined on $\mathbb{Z}_n$; for $x\in\mathbb{Z}_n$ we write $\bar x\in\mathbb{Z}_m$ for its residue modulo $m$. Note that $x\in I$ if and only if $\bar x=0$, and that $-m=m$ in $\mathbb{Z}_n$.

For a cell $x\in\mathbb{Z}_n^d$ let

$$
w(x)=\bigl(x_1,\dots,x_d,\,-H_{d,n}(x)\bigr)\in\mathbb{Z}_n^{d+1}
$$

be its graph tuple. A set $T$ of $n$ cells is a transversal if and only if, for each position $k\in\{1,\dots,d+1\}$, the $k$-th entries of the tuples $w(x)$, $x\in T$, are pairwise distinct.

**Lemma 2.1.** Every transversal $T$ of $H_{d,n}$ contains exactly one cell of $I_d$. Its symbol lies in $I$.

*Proof.* Summing the symbols of $T$ gives $\sum_{s\in\mathbb{Z}_n}s=m(2m-1)=m$ in $\mathbb{Z}_n$. Summing all coordinates of the cells of $T$ gives $d\sum_{s\in\mathbb{Z}_n}s=dm=0$, because $d$ is even. Hence $m\cdot\lvert T\cap I_d\rvert=m$, so $\lvert T\cap I_d\rvert$ is odd. (This is the $\Delta$-lemma [1, Lemma 1] applied to $H_{d,n}$.) The first coordinates of the cells of $T$ are distinct and only two of them lie in $I$, so $\lvert T\cap I_d\rvert\le 2$. Thus $\lvert T\cap I_d\rvert=1$. The symbol of a cell of $I_d$ is a sum of elements of $I$ and lies in $I$. $\square$

We call the cell of $T\cap I_d$ the special cell of $T$ and its symbol the special symbol of $T$. In particular, the transversals constructed below meet $I_d$ exactly once for the same reason as every other transversal; this is not an additional property of the construction.

**Lemma 2.2 (symmetries).** Let $T$ be a transversal of $H_{d,n}$.

1. For $t\in I_d$, the translate $T+t$ is a transversal of $H_{d,n}$, and its special cell is the translate of the special cell of $T$.
2. Let $\sigma$ be a permutation of $\{1,\dots,d+1\}$ and $\varepsilon\in\{1,-1\}$. For every cell $x$ there is a unique cell $\Phi(x)$ with $w(\Phi(x))=\varepsilon\cdot\bigl(w(x)_{\sigma(1)},\dots,w(x)_{\sigma(d+1)}\bigr)$. The map $\Phi=\Phi_{\sigma,\varepsilon}$ is a bijection of $\mathbb{Z}_n^d$ that maps $I_d$ onto $I_d$ and maps transversals to transversals; its inverse is $\Phi_{\sigma^{-1},\varepsilon}$.

*Proof.* (1) If $t\in I_d$, then $x+t\in I_d$ if and only if $x\in I_d$, so $H_{d,n}(x+t)=H_{d,n}(x)+(t_1+\dots+t_d)$; translation shifts every coordinate and every symbol by a constant.

(2) We claim that a tuple $v\in\mathbb{Z}_n^{d+1}$ is the graph tuple of a cell if and only if either $v\notin I^{d+1}$ and $v_1+\dots+v_{d+1}=0$, or $v\in I^{d+1}$ and $v_1+\dots+v_{d+1}=m$. If $x\notin I_d$, then $w(x)\notin I^{d+1}$ and its entries sum to $0$; if $x\in I_d$, then $H_{d,n}(x)\in I$, so $w(x)\in I^{d+1}$ and its entries sum to $-m=m$. Conversely, let $v$ satisfy one of the two conditions and put $x=(v_1,\dots,v_d)$. If $v\notin I^{d+1}$ and $\sum_k v_k=0$, then $x\notin I_d$, for otherwise $v_{d+1}=-(v_1+\dots+v_d)\in I$; hence $v_{d+1}=-H_{d,n}(x)$. If $v\in I^{d+1}$ and $\sum_k v_k=m$, then $x\in I_d$ and $v_{d+1}=m-(v_1+\dots+v_d)=-H_{d,n}(x)$. This proves the claim. Both conditions are invariant under permuting the entries and under negation, because $-I=I$ and $-m=m$. Hence the permuted and signed tuple is a graph tuple, and since a graph tuple is determined by its first $d$ entries, $\Phi$ is well defined; it is a bijection with the stated inverse, and $\Phi(x)\in I_d$ if and only if $w(x)\in I^{d+1}$, that is, $x\in I_d$. Finally, permuting positions and negating entries preserve the property that in each position the entries of the tuples $w(x)$, $x\in T$, are distinct. $\square$

**Lemma 2.3 (odd-sum bijection).** Let $N\ge 2$, $v_0\in[0,N-1]$ and $u_0=N-1-v_0$, and assume that $N$ is even or $v_0$ is even. There is a bijection

$$
\varphi:\{0,\dots,N-1\}\setminus\{u_0\}\to\{0,\dots,N-1\}\setminus\{v_0\}
\quad\text{with}\quad
\{u+\varphi(u): u\ne u_0\}=\{1,3,5,\dots,2N-3\}.
$$

Moreover, if $0<v_0<u_0$, then $\varphi(u)=u-1$ for $1\le u\le v_0$.

*Proof.* We construct $\varphi=\varphi_{N,v_0}$ by recursion on $N$. Since $u+\varphi(u)$ takes $N-1$ values and the target set has $N-1$ elements, it suffices to check that the sums are pairwise distinct odd numbers in $[1,2N-3]$.

(i) If $v_0=0$, put $\varphi(u)=u+1$ for $u\in[0,N-2]$; the sums are $2u+1$.

(ii) If $u_0=0$, put $\varphi(u)=u-1$ for $u\in[1,N-1]$; the sums are $2u-1$.

(iii) If $0<v_0<u_0$, put $a=v_0+1$. Then $a\ge 2$ and $2a\le N$. Let $N'=N-a$; then $N'\ge a\ge 2$, $v_0<N'$, and $N'$ is even or $v_0$ is even (if $v_0$ is odd, then $N$ is even and $a$ is even). Let $\psi=\varphi_{N',v_0}$, whose domain is $[0,N'-1]\setminus\{N-2a\}$, and define

$$
\varphi(u)=u-1\ (1\le u\le a-1),\qquad \varphi(0)=2a-1,\qquad \varphi(u'+a)=\psi(u')+a\ \ (u'\ne N-2a).
$$

The domain is $[0,a-1]\cup([a,N-1]\setminus\{N-a\})$, and $N-a=u_0$. The image is $[0,a-2]\cup\{2a-1\}\cup([a,N-1]\setminus\{2a-1\})=[0,N-1]\setminus\{v_0\}$. The sums are $1,3,\dots,2a-3$, then $2a-1$, and then $2a+(u'+\psi(u'))$, which are $2a+1,\dots,2N-3$.

(iv) If $v_0=u_0$, then $N=2v_0+1$ is odd, so $v_0=2k$ is even with $k\ge 1$ and $N=4k+1$. Let $\eta=\varphi_{2k,1}$, whose domain is $[0,2k-1]\setminus\{2k-2\}$, and define

$$
\varphi(u)=u+1\ (0\le u\le 2k-2),\quad \varphi(2k-1)=2k+2,\quad \varphi(4k-1)=0,\quad \varphi(u'+2k+1)=\eta(u')+2k+1\ \ (u'\ne 2k-2).
$$

Here $\eta=\varphi_{2k,1}$ has $N'=2k$ even, $v_0'=1$ and $u_0'=2k-2$, so shifting $u'\in[0,2k-1]\setminus\{2k-2\}$ and $\eta(u')\in[0,2k-1]\setminus\{1\}$ by $2k+1$ gives the domain $[2k+1,4k]\setminus\{4k-1\}$ and the image $[2k+1,4k]\setminus\{2k+2\}$; together with $u\in[0,2k-2]$ (image $[1,2k-1]$), $u=2k-1$ (image $2k+2$) and $u=4k-1$ (image $0$), both the domain and the image are $[0,4k]\setminus\{2k\}$. The sums are $1,3,\dots,4k-3$, then $4k+1$ and $4k-1$, and then $4k+2+(u'+\eta(u'))$, which are $4k+3,\dots,8k-1=2N-3$.

(v) If $v_0>u_0>0$, let $\varphi$ be the inverse of $\varphi_{N,u_0}$, which is given by (iii) with the roles of $u_0$ and $v_0$ exchanged; its hypothesis holds because $N$ odd forces $v_0$ and $u_0=N-1-v_0$ to be even.

The final assertion is part of (iii). $\square$

## 3. Dimension two

### 3.1 The families $T_{N,a}$

Let $N\in\{m,m+1\}$ and $a\in[1,N]$, and assume that $N$ is even or $a$ is odd. Put $v_0=a-1$ and $u_0=N-a$, and let $\varphi=\varphi_{N,v_0}$ be the bijection of Lemma 2.3. Let $T_{N,a}\subset\mathbb{Z}_n^2$ consist of the following $n$ cells:

- the origin $(0,0)$;
- the odd segment: $(u-u_0,\ \varphi(u)-v_0)$ for $u\in[0,N-1]\setminus\{u_0\}$;
- the linear segment: $c_j=(a+j,\ N+1-a+j)$ for $j\in[0,n-N-1]$.

**Lemma 3.1.** The first coordinates of the cells of $T_{N,a}$ are pairwise distinct, and so are the second coordinates. The sums $x+y\in\mathbb{Z}_n$ over the $n-1$ cells $(x,y)\ne(0,0)$ of $T_{N,a}$ are pairwise distinct and form $\mathbb{Z}_n\setminus\{m\}$.

*Proof.* The first coordinates of the odd segment form $[a-N,a-1]\setminus\{0\}$, and those of the linear segment form $[a,a+n-N-1]$; together with $0$ these are the $n$ consecutive integers $[a-N,a+n-N-1]$, which represent $\mathbb{Z}_n$ once each. The second coordinates of the odd segment form $[1-a,N-a]\setminus\{0\}$, and those of the linear segment form $[N+1-a,n-a]$; together with $0$ they form $[1-a,n-a]$. On the odd segment the sum is $u+\varphi(u)-(N-1)$, which by Lemma 2.3 runs through the $N-1$ integers $-(N-2),-(N-4),\dots,N-2$; on the linear segment it is $N+1+2j$, which runs through the $n-N$ integers $N+1,N+3,\dots,2n-N-1$. Each list spans fewer than $n$ consecutive integers, so its entries are distinct in $\mathbb{Z}_n$, and the two lists have opposite parities, so they are disjoint. Neither contains $m$: if $N=m+1$, the first list has the parity of $m+1$ and the second lies in $[m+2,3m-2]$, which contains no integer congruent to $m$ modulo $n$; if $N=m$, the first list lies in $[-(m-2),m-2]$ and the second has the parity of $m+1$. $\square$

**Proposition 3.2.** The set $T_{N,a}$ is a transversal of $H_{2,n}$ if and only if $2a\ne N+1$. In that case its special cell is $(0,0)$.

*Proof.* By Lemma 3.1 the rows of $T_{N,a}$ are distinct and so are its columns, and its only cells in $I_2$ are $(0,0)$ and possibly $(m,m)$, since the cell in row $m$ is not in column $0$ and the cell in column $m$ is not in row $0$. If $(m,m)\notin T_{N,a}$, the symbols are $H_{2,n}(0,0)=m$ and the sums $x+y$ of Lemma 3.1, which together form $\mathbb{Z}_n$. If $(m,m)\in T_{N,a}$, then $H_{2,n}(m,m)=m=H_{2,n}(0,0)$ and $T_{N,a}$ is not a transversal. It remains to decide when the cell in row $m$ is $(m,m)$. Row $m$ lies in the linear segment exactly when $j=m-a\in[0,n-N-1]$, that is, when $N-m+1\le a\le m$. Its second coordinate is then $m+(N+1-2a)$, and since $\lvert N+1-2a\rvert\le N-1<n$, it equals $m$ exactly when $2a=N+1$. Otherwise $N=m+1$ and $a\in\{1,m+1\}$, and $2a\ne N+1$. For $a=1$ we have $v_0=0$ and $u_0=m$; row $m$ corresponds to $u=0$, and its second coordinate is $\varphi(0)=1\ne m$. For $a=m+1$ we have $u_0=0$ and $v_0=m$; row $m$ corresponds to $u=m$, and its second coordinate is $\varphi(m)-m=-1\ne m$. $\square$

We call $(N,a)$ admissible if $N\in\{m,m+1\}$, $a\in[1,N]$, $N$ is even or $a$ is odd, and $2a\ne N+1$. If $N$ is even, every $a\in[1,N]$ is admissible. If $N=m+1$ with $m$ even, the admissible values are the odd $a\in[1,m+1]$ other than $a^{\ast}=(m+2)/2$; this exclusion matters only when $a^{\ast}$ is odd, that is, when $m\equiv 0\pmod 4$. Similarly, if $N=m$ with $m$ odd, the admissible values are the odd $a\in[1,m]$ other than $(m+1)/2$, and the exclusion matters only when $m\equiv 1\pmod 4$; the proofs below do not use this last family.

### 3.2 Every entry of $H_{2,n}$ lies in a transversal

For a cell $c=(x,y)\notin I_2$ the graph tuple is $(x,y,-x-y)$. For the linear cell $c_j$ of $T_{N,a}$ we write

$$
z_j=-(N+1+2j),
$$

which does not depend on $a$. Let $\Phi_{zx}$ and $\Phi_{xz}$ be the maps of Lemma 2.2(2) with $\varepsilon=1$ that send a cell with graph tuple $(x,y,z)$ to the cells $(z,x)$ and $(x,z)$, respectively. By Lemma 2.2, for admissible $(N,a)$, $j\in[0,n-N-1]$ and $(u,v)\in I_2$, each of the three cells

$$
(a+j+u,\ N+1-a+j+v),\qquad (z_j+u,\ a+j+v),\qquad (a+j+u,\ z_j+v)
$$

lies in a transversal of $H_{2,n}$, namely in $T_{N,a}+(u,v)$, $\Phi_{zx}(T_{N,a})+(u,v)$ and $\Phi_{xz}(T_{N,a})+(u,v)$, respectively. Since $u$ and $v$ range over $I$, this gives the following criterion: a cell $(X,Y)$ lies in a transversal of $H_{2,n}$ if there are an admissible $(N,a)$ and $j\in[0,n-N-1]$ such that one of the following holds, all congruences being modulo $m$:

- (ID) $a+j\equiv X$ and $N+1-a+j\equiv Y$;
- (ZX) $z_j\equiv X$ and $a+j\equiv Y$;
- (XZ) $a+j\equiv X$ and $z_j\equiv Y$.

**Theorem 3.3.** For every even $n\ge 4$, every cell of $\mathbb{Z}_n^2$ lies in a transversal of $H_{2,n}$.

*Proof.* Let $(X,Y)\in\mathbb{Z}_n^2$. If $(X,Y)\in I_2$, it lies in $T_{m+1,1}+(X,Y)$; the pair $(m+1,1)$ is admissible because $a=1$ is odd and $2\ne m+2$. Assume from now on that $(X,Y)\notin I_2$.

*Case 1: $m$ odd.* Take $N=m+1$, which is even, $j\in[0,m-2]$ and $a\in[1,m+1]$. Here $z_j\equiv-2(j+1)\pmod m$, and since $2$ is invertible modulo $m$, these values cover every nonzero residue modulo $m$. For fixed $j$, $a+j$ runs through $m+1$ consecutive integers and covers every residue. Hence (ZX) applies when $\bar X\ne 0$, and (XZ) applies when $\bar Y\ne 0$; one of these holds because $(X,Y)\notin I_2$.

*Case 2: $m$ even, and $X$ or $Y$ odd.* Take $N=m$, $j\in[0,m-1]$ and $a\in[1,m]$. Here $z_j\equiv-(1+2j)\pmod m$ covers every odd residue modulo $m$, and for fixed $j$, $a+j$ covers every residue. Hence (ZX) applies when $X$ is odd, and (XZ) applies when $Y$ is odd.

*Case 3: $m$ even, $X$ and $Y$ even.* Since $(X,Y)\notin I_2$, we have $m\ge 4$. Take $N=m+1$, admissible (hence odd) $a$, and $j$ in $J=\{1,3,\dots,m-3\}\subseteq[0,m-2]$. Then $a+j$, $N+1-a+j$ and $z_j\equiv-2(j+1)\pmod m$ are even.

*Case 3a: $m\equiv 2\pmod 4$.* All odd $a\in[1,m+1]$ are admissible, and for fixed $j\in J$ the numbers $a+j$ are $m/2+1$ consecutive even integers, which cover every even residue modulo $m$. For $j=2s+1$ with $s\in[0,m/2-2]$, $z_j\equiv-4(s+1)\pmod m$; as $m/2$ is odd, $2(s+1)$ runs through all nonzero residues modulo $m/2$, so $z_j$ covers every nonzero even residue modulo $m$. Hence (ZX) applies when $\bar X\ne0$, and (XZ) applies when $\bar Y\ne 0$.

*Case 3b: $m\equiv 0\pmod 4$.* Now $a^{\ast}=m/2+1$ is odd and excluded. The odd integers $a\in[1,m+1]$ represent every odd residue modulo $m$, with $1\equiv m+1$ the only repetition, and $a^{\ast}\in[3,m-1]$. Hence, for fixed odd $j$,

$$
\{\overline{a+j}: (m+1,a)\ \text{admissible}\}=\{\text{even residues modulo } m\}\setminus\{\overline{j+a^{\ast}}\}. \tag{3.1}
$$

Residues modulo $4$ are well defined on $\mathbb{Z}_m$ because $4$ divides $m$.

*Step 1: $X\equiv 0$ or $Y\equiv 0\pmod 4$.* By the symmetry between (ZX) and (XZ), let $Z_t\in\{X,Y\}$ satisfy $Z_t\equiv 0\pmod 4$, let $X_t$ be the other coordinate, and look for $j\in J$ and admissible $a$ with $z_j\equiv Z_t$ and $a+j\equiv X_t\pmod m$. If $\bar Z_t=0$, then $\bar X_t\ne 0$; take $j_0=m/2-1\in J$. Then $z_{j_0}\equiv-m\equiv 0$, and the residue missing in (3.1) is $\overline{j_0+a^{\ast}}=0$, so $X_t$ is attained. If $\bar Z_t\ne 0$, then $\bar Z_t\in\{4,8,\dots,m-4\}$; put $j_1=(m-\bar Z_t-2)/2$ and $j_2=j_1+m/2$. Both are odd and lie in $J$, and $z_{j_1}\equiv z_{j_2}\equiv \bar Z_t\pmod m$. The residues missing in (3.1) for $j_1$ and $j_2$ differ by $m/2$, so $X_t$ avoids one of them.

*Step 2: $X\equiv Y\equiv 2\pmod 4$.* We use (ID). For admissible $a$ and $j\in J$ we have $(N+1-a+j)-(a+j)=m+2-2a\equiv 2-2a\pmod m$, and $\{\overline{a+j}:j\in J\}$ is the set of even residues modulo $m$ other than $\overline{a-1}$. Let $D=\overline{Y-X}\in\{0,4,\dots,m-4\}$. If $D=0$, take $a=1$: then $2-2a=0$, and the missing residue is $0$, which differs from $\bar X$ because $X\equiv 2\pmod 4$. If $D\ne 0$, take $a_1=1+(m-D)/2\in[3,m/2-1]$ and $a_2=a_1+m/2\in[m/2+3,m-1]$. Both are odd and different from $a^{\ast}$, and $2-2a_1\equiv 2-2a_2\equiv D\pmod m$; their missing residues $\overline{a_1-1}$ and $\overline{a_2-1}$ differ by $m/2$, so $\bar X$ avoids one of them. In both cases choose $j\in J$ with $a+j\equiv X$; then $N+1-a+j\equiv X+D\equiv Y\pmod m$. $\square$

### 3.3 Normalized triples

Let $\Gamma$ be the group of the $12$ maps $g=(p,\varepsilon)$ of $\mathbb{Z}_n^3$ given by $(g t)_k=\varepsilon\, t_{p(k)}$, where $p$ is a permutation of $\{1,2,3\}$ and $\varepsilon\in\{1,-1\}$, and let $\Phi_g$ be the corresponding map of Lemma 2.2(2) for $d=2$; it sends a cell $c$ to the first two entries of $g\,w(c)$. For a cell $c=(x,y)$ define its triple

$$
\tau(c)=(x,\ y,\ m-x-y).
$$

Triples have entry sum $m$, and $\Gamma$ preserves this property. For $c\notin I_2$ we have $w(c)=\tau(c)+(0,0,m)$, and for $c\in I_2$ we have $w(c)=\tau(c)$.

**Lemma 3.4.** Let $(N,a)$ be admissible and $g\in\Gamma$. Let $q_g$ be the special cell of $\Phi_g(T_{N,a})$ and $T^{g}=\Phi_g(T_{N,a})-q_g$. Then $T^{g}$ is a transversal of $H_{2,n}$ with special cell $(0,0)$, and for every cell $c\ne(0,0)$ of $T_{N,a}$ the cell $\bigl((g\tau(c))_1,(g\tau(c))_2\bigr)$ lies in $T^{g}$.

*Proof.* By Proposition 3.2 and Lemma 2.2, $T^{g}$ is a transversal with special cell $(0,0)$. The special cell of $\Phi_g(T_{N,a})$ is $\Phi_g(0,0)$, whose graph tuple is $g(0,0,m)$, because $w(0,0)=(0,0,m)$. For a cell $c\ne(0,0)$ of $T_{N,a}$ we have $c\notin I_2$ and $g\,w(c)=g\tau(c)+g(0,0,m)$, since $g$ is additive. Taking the first two entries gives $\Phi_g(c)=\bigl((g\tau(c))_1,(g\tau(c))_2\bigr)+q_g$. $\square$

The seeds are the triples of the following cells of the transversals $T_{N,a}$. For admissible $(N,a)$ and $j\in[0,n-N-1]$, the linear seed is the triple of $c_j$:

$$
\lambda(N,a,j)=\bigl(a+j,\ N+1-a+j,\ m-N-1-2j\bigr). \tag{L}
$$

For even $N\in\{m,m+1\}$, $2\le a\le N/2$ and $1\le u\le a-1$, the odd seed is the triple of the cell of the odd segment indexed by $u$. Here $0<v_0<u_0$, so $\varphi(u)=u-1$ by Lemma 2.3, and the cell is $(u-N+a,\ u-a)$:

$$
\omega(N,a,u)=\bigl(u-N+a,\ u-a,\ m+N-2u\bigr). \tag{O}
$$

Let $\mathcal{N}_n$ be the set of all triples $g s$ with $g\in\Gamma$ and $s$ a seed. By construction $\mathcal{N}_n$ is invariant under $\Gamma$.

**Lemma 3.5.** If $t\in\mathcal{N}_n$ and $(u,v)\in I_2$, then $H_{2,n}$ has a transversal that contains the cell $(t_1+u,\ t_2+v)$ and has special cell $(u,v)$, hence special symbol $u+v+m$.

*Proof.* Write $t=gs$ with $s=\tau(c)$ a seed, where $c\ne(0,0)$ is a cell of $T_{N,a}$. By Lemma 3.4, $T^{g}$ contains $(t_1,t_2)$ and has special cell $(0,0)$. By Lemma 2.2(1), $T^{g}+(u,v)$ is a transversal with special cell $(u,v)$, and $H_{2,n}(u,v)=u+v+m$. $\square$

### 3.4 Two coverage properties

The gluing construction in Case 3 of Theorem 4.4 reduces the existence of a transversal through the target cell to two two-dimensional coverage problems in which the first factor $T_1$ of $H_{d-2,n}$ has already been fixed with an arbitrary special symbol $a_0\in I=\{0,m\}$. First, to build the gluing transversal $T_g$ of $H_{2,n}$ through $(s_1,s_2)$ with special cell $(a_0,b_0)$, we may choose either special symbol $b_0\in\{0,m\}$ for the second factor $T_2$; by Lemma 3.5, switching $b_0$ between $0$ and $m$ shifts the required normalized triple $\tau(s_1-a_0,s_2-b_0)$ by $(0,m,m)$. Second, once $b_0$ is fixed, the two cells $(u_2,v_2)\in I_2$ with special symbol $u_2+v_2+m=b_0$ are $(0,b_0+m)$ and $(m,b_0)$, and switching between them shifts the required normalized triple $\tau(p-u_2,q-v_2)$ for $T_2$ by $(m,m,0)$. In the first problem, at least one of the two resulting triples lies in $\mathcal{N}_n$ by Proposition 3.6 when $s_1\in I$ (so $s_1-a_0=m$) and by Proposition 3.7 when $s_1\notin I$; in the second problem, Case 3 of Theorem 4.4 ensures $p,q,p+q\notin I$, so Proposition 3.7 guarantees that one of the two resulting triples lies in $\mathcal{N}_n$ regardless of whether $s_1\in I$.

**Proposition 3.6 (boundary pairs).** For every $w\in\mathbb{Z}_n\setminus I$ there is $w'\in\{w,w+m\}$ with $(m,\ w',\ -w')\in\mathcal{N}_n$.

*Proof.* The condition $w'\in\{w,w+m\}$ means $\bar w'=\bar w$, and $\bar w\ne 0$. If $N-m+1\le a\le m$, then $j=m-a\in[0,n-N-1]$ and

$$
\lambda(N,a,m-a)=(m,\ y,\ -y),\qquad y=m+N+1-2a .
$$

In the first three cases below we find admissible $(N,a)$ in this range with $\bar y=\bar w$ and take $w'=y$; the last case uses another seed.

- If $m$ is odd, take $N=m+1$ and $a\in[2,m]$; then $y\equiv 2(1-a)\pmod m$ covers every nonzero residue.
- If $m$ is even and $w$ is odd, take $N=m$ and $a\in[1,m]$; then $y\equiv 1-2a\pmod m$ covers every odd residue.
- If $m\equiv 2\pmod 4$ and $w$ is even, take $N=m+1$ and $a=2k+1$ with $k\in[1,m/2-1]$, which is admissible because $a^{\ast}$ is even; then $y\equiv -4k\pmod m$, and as $m/2$ is odd these values cover every nonzero even residue.
- If $m\equiv 0\pmod 4$ and $w$ is even, take $N=m+1$ and $j=m/2-1$. For admissible $a=2k+1$, with $k\in[0,m/2]\setminus\{m/4\}$, we get $\lambda(m+1,a,m/2-1)=(x,-x,m)$ with $x=m/2+2k$, and a cyclic permutation in $\Gamma$ gives $(m,x,-x)\in\mathcal{N}_n$. The values $x$ are the even integers in $[m/2,3m/2]$ other than $m$, and they cover every nonzero even residue modulo $m$. $\square$

Call a triple $t=(X,Y,W)$ interior if $X,Y,W\notin I$ and $X+Y+W=m$, and let

$$
V_4=\{(0,0,0),(m,m,0),(m,0,m),(0,m,m)\}.
$$

If $t$ is interior, so is $t+v$ for every $v\in V_4$.

**Proposition 3.7 (interior pairs).** Let $t$ be an interior triple and $v\in V_4\setminus\{(0,0,0)\}$. Then $t\in\mathcal{N}_n$ or $t+v\in\mathcal{N}_n$.

*Proof.* *Reduction.* A permutation in $\Gamma$ that moves the zero entry of $v$ to the third position maps $\{t,t+v\}$ to a pair $\{t',t'+(m,m,0)\}$. If the third entry of $t'$ lies in $[m+1,2m-1]$, applying $-1\in\Gamma$ moves it into $[1,m-1]$ and keeps the form of the pair, since $-(m,m,0)=(m,m,0)$. As $\mathcal{N}_n$ is $\Gamma$-invariant, it suffices to show that

$$
P=\{(X,Y,W),\ (X+m,Y+m,W)\}
$$

meets $\mathcal{N}_n$ for every interior triple $(X,Y,W)$ with $W\in[1,m-1]$.

For $W\in[1,m-1]$ let $R(W)\subseteq\mathbb{Z}_m$ be the set of residues $\bar x$ of the first entries of the triples $(x,y,W)\in\mathcal{N}_n$. For such a triple, $y=m-W-x$, so if $\bar x=\bar X$, then $x\in\{X,X+m\}$ and $(x,y,W)\in P$. Exchanging the first two entries (an element of $\Gamma$) shows that $\overline{-W-x}=\bar y\in R(W)$, so $R(W)$ is invariant under the map $r\mapsto \overline{-W}-r$, which exchanges $\bar X$ and $\bar Y$. Since $\bar X\ne 0$ and $\bar Y=\overline{-W-X}\ne 0$, it suffices to prove

$$
R(W)\supseteq\mathbb{Z}_m\setminus\{0,\ \overline{-W}\}\qquad(1\le W\le m-1). \tag{3.2}
$$

By the invariance of $R(W)$, for each $r\in\mathbb{Z}_m\setminus\{0,\overline{-W}\}$ it is enough to exhibit a triple of $\mathcal{N}_n$ with third entry $W$ whose first or second entry has residue $r$ or $\overline{-W}-r$. Let $N_e$ be the even element of $\{m,m+1\}$.

*Case A: $W\not\equiv m\pmod 2$.* Put $j=(W+m-N_e-1)/2$. This is an integer with $0\le j\le n-N_e-1$: if $m$ is even, then $N_e=m$ and $W$ is odd; if $m$ is odd, then $N_e=m+1$ and $W\ge 2$ is even. For every $a\in[1,N_e]$,

$$
-\lambda(N_e,a,j)=\bigl(-a-j,\ a-j-N_e-1,\ W\bigr)\in\mathcal{N}_n .
$$

The first entries run through $N_e\ge m$ consecutive integers, so $R(W)=\mathbb{Z}_m$.

*Case B: $W\equiv m\pmod 2$.* Then $W\le m-2$; put $h=(m-W)/2\ge 1$.

*B.1: residues in $[1,m-1-W]$.* Put $u=(W+N_e-m)/2$; then $1\le u\le N_e/2-1$. For $u+1\le a\le N_e/2$,

$$
-\omega(N_e,a,u)=\bigl(N_e-u-a,\ a-u,\ W\bigr)\in\mathcal{N}_n .
$$

As $a$ varies, the first entry runs through $[h,m-1-W]$ and the second through $[1,h]$; since exchanging the first two entries lies in $\Gamma$, both intervals lie in $R(W)$, and hence every $r\in[1,h]\cup[h,m-1-W]=[1,m-1-W]$ is attained.

*B.2: the remaining residues.* Since $r=m-W$ represents the excluded residue $\overline{-W}$ in (3.2), the residues not yet treated are $r\in[m-W+1,m-1]$; for these, $r'=2m-W-r$ also lies in $[m-W+1,m-1]$ and represents $\overline{-W}-r$. It suffices to attain $r$ or $r'$.

*B.2.1: $r$ or $r'$ is odd.* Let $b\in\{r,r'\}$ be odd and let $b'=2m-W-b$ be the other one. Put $j=(2m-b-N_e-1)/2$ and $a=N_e+1+j-W$. Then

$$
\lambda(N_e,a,j)=\bigl(b',\ W,\ b+m\bigr),
$$

and a permutation in $\Gamma$ gives $(b',\ b+m,\ W)\in\mathcal{N}_n$, whose first two entries have residues $b'$ and $b$. It remains to check the parameters. The number $j$ is an integer because $b$ is odd and $N_e$ is even. We have $j\ge 0$ because $b\le m-1$, and $b\le m-2$ when $m$ is odd; also $j\le n-N_e-1$. The condition $1\le a\le N_e$ is equivalent to $j+1\le W\le N_e+j$, which for either parity of $m$ reads

$$
\left\lceil\frac{m-b}{2}\right\rceil\le W\le\left\lfloor\frac{3m-b}{2}\right\rfloor .
$$

This holds because $m-b\le W-1$ gives $\lceil (m-b)/2\rceil\le\lceil (W-1)/2\rceil\le W$, and $b\le m-1$ gives $\lfloor (3m-b)/2\rfloor\ge m>W$.

*B.2.2: $r$ and $r'$ are even.* Then $m$ is even (if $m$ is odd, then $W$ is odd and $r+r'=2m-W$ is odd), $W$ is even, and $r,r'\in[m-W+2,m-2]$. We use $N=m+1$, $a^{\ast}=m/2+1$ and $j\in[0,m-2]$, and note that $r+r'=2(m-W/2)$.

(i) $m-W/2$ is even. Let $M=\max(r,r')$, so that $M$ is even and $m-W/2\le M\le m-2$. Put $j=W/2-1$ and $a=M-m+W/2+1$. Then $a$ is odd because $W/2$ is even, and $1\le a\le W/2-1<a^{\ast}$, so $(m+1,a)$ is admissible, and

$$
-\lambda(m+1,a,W/2-1)=\bigl(1-a-W/2,\ M,\ W\bigr).
$$

Its second entry has residue $M\in\{r,r'\}$.

(ii) $m-W/2$ is odd. Then $r+r'\equiv 2\pmod 4$; since both are even, exactly one of them is congruent to $m$ modulo $4$. Call it $b$ and let $b'=2m-W-b$. If $W\ne m-b/2$, put $j=(m-b)/2-1$ and $a=m+1+(m-b)/2-W$. Then $a$ is odd, because $(m-b)/2$ and $W$ are even; $1\le a\le m+1$, because $(m-b)/2\le W/2-1$ and $W<(3m-b)/2$; and $a\ne a^{\ast}$, because $a=a^{\ast}$ would mean $W=m-b/2$. Thus

$$
\lambda(m+1,a,(m-b)/2-1)=\bigl(b',\ W,\ b+m\bigr),
$$

and a permutation in $\Gamma$ gives a triple of $\mathcal{N}_n$ with third entry $W$ whose first two entries have residues $b'$ and $b$. If $W=m-b/2$, then $b\in[m-W+2,m-2]$ is even, so $j=b/2-1\in[0,m/2-2]\subseteq[0,m-2]$ is an integer in range; use the admissible pair $(m+1,1)$ and $j=b/2-1$:

$$
-\lambda(m+1,1,b/2-1)=\bigl(-b/2,\ W,\ b\bigr),
$$

and a permutation in $\Gamma$ gives a triple with third entry $W$ and second entry $b$.

In each case $r$ or $r'$ is attained, which proves (3.2). $\square$

## 4. Higher dimensions

Throughout this section $d\ge 4$ is even. For $\rho\in\mathbb{Z}_n^{d-2}$ and $(p,q)\in\mathbb{Z}_n^2$ we write $(\rho,p,q)$ for the cell of $\mathbb{Z}_n^d$ obtained by concatenation.

**Lemma 4.1 (constant-sum lifting).** Let $\rho\in\mathbb{Z}_n^{d-2}\setminus I_{d-2}$ and $(p,q)\in\mathbb{Z}_n^2$ with $c=p+q\in I$. If $\rho$ lies in a transversal $T_1$ of $H_{d-2,n}$, then $(\rho,p,q)$ lies in a transversal of $H_{d,n}$.

*Proof.* Write $T_1=\{x^{(0)},\dots,x^{(n-1)}\}$, where $x^{(0)}$ is the special cell (Lemma 2.1) and $x^{(i^{\ast})}=\rho$; then $i^{\ast}\ne 0$ because $\rho\notin I_{d-2}$. Choose $e\in I\setminus\{p\}$ and a bijection $\pi:\{0,\dots,n-1\}\to\mathbb{Z}_n$ with $\pi(0)=e$ and $\pi(i^{\ast})=p$, and put

$$
T=\bigl\{\bigl(x^{(i)},\ \pi(i),\ c-\pi(i)\bigr): 0\le i\le n-1\bigr\}.
$$

Each coordinate of $T$ takes every value once. The cell with $i=0$ lies in $I_d$, because $x^{(0)}\in I_{d-2}$, $e\in I$ and $c-e\in I$; the cells with $i\ne 0$ do not, because $x^{(i)}\notin I_{d-2}$. Hence the symbol of the $i$-th cell of $T$ is $H_{d-2,n}(x^{(i)})+c$ for every $i$, and these symbols are distinct. The cell with $i=i^{\ast}$ is $(\rho,p,c-p)=(\rho,p,q)$. $\square$

**Lemma 4.2 (pair reduction).** Assume that every cell of $\mathbb{Z}_n^{d-2}$ lies in a transversal of $H_{d-2,n}$. Let $y\in\mathbb{Z}_n^d\setminus I_d$, and suppose that two entries of $w=w(y)$ sum to an element of $I$. Then $y$ lies in a transversal of $H_{d,n}$.

*Proof.* Since $y\notin I_d$, the entries of $w$ sum to $0$ and $w\notin I^{d+1}$, so at least two entries of $w$ lie outside $I$: if exactly one did, the sum would lie outside $I$. Let $w_{k_1}+w_{k_2}\in I$ with $k_1\ne k_2$. We choose distinct positions $l_1,l_2,l_3$ such that $w_{l_1}+w_{l_2}\in I$ and the $d-2$ entries of $w$ at the other positions are not all in $I$. If some position $s\notin\{k_1,k_2\}$ has $w_s\notin I$, take $(l_1,l_2)=(k_1,k_2)$ and any $l_3\notin\{k_1,k_2,s\}$, which exists because $d+1\ge 5$. Otherwise all entries outside positions $k_1,k_2$ lie in $I$, so $w_{k_1},w_{k_2}\notin I$; take two positions $l_1,l_2\notin\{k_1,k_2\}$ (there are $d-1\ge 3$ of them) and $l_3=k_2$. Then $w_{l_1}+w_{l_2}\in I$, and the remaining entries include $w_{k_1}\notin I$.

Let $\sigma$ list the positions other than $l_1,l_2,l_3$ in increasing order, followed by $l_1,l_2,l_3$, and let $y'=\Phi_{\sigma,1}(y)$ (Lemma 2.2), so that $w(y')=(w_{\sigma(1)},\dots,w_{\sigma(d+1)})$. Then $y'=(\rho,w_{l_1},w_{l_2})$ with $\rho\notin I_{d-2}$. By hypothesis $\rho$ lies in a transversal of $H_{d-2,n}$; by Lemma 4.1, $y'$ lies in a transversal $T'$ of $H_{d,n}$; and $\Phi_{\sigma^{-1},1}(T')$ is a transversal containing $y$. $\square$

**Lemma 4.3 (gluing).** Let $T_1$ be a transversal of $H_{d-2,n}$ with special symbol $a_0$ and $T_2$ a transversal of $H_{2,n}$ with special symbol $b_0$. Index their cells by symbols, $T_1=\{x(s):s\in\mathbb{Z}_n\}$ with $H_{d-2,n}(x(s))=s$ and $T_2=\{u(s):s\in\mathbb{Z}_n\}$ with $H_{2,n}(u(s))=s$. Let $T_g$ be a transversal of $H_{2,n}$ with special cell $(a_0,b_0)$. Then

$$
T=\bigl\{\bigl(x(s_1),\ u(s_2)\bigr): (s_1,s_2)\in T_g\bigr\}
$$

is a transversal of $H_{d,n}$.

*Proof.* As $(s_1,s_2)$ runs through $T_g$, both $s_1$ and $s_2$ run through $\mathbb{Z}_n$, so each of the $d$ coordinates of $T$ takes every value once. The cell $x(s_1)$ lies in $I_{d-2}$ exactly when $s_1=a_0$, and $u(s_2)$ lies in $I_2$ exactly when $s_2=b_0$. In $T_g$ the cell with first coordinate $a_0$ is $(a_0,b_0)$, so $s_1=a_0$ if and only if $s_2=b_0$. For $(s_1,s_2)\ne(a_0,b_0)$ the symbol of $(x(s_1),u(s_2))$ is $s_1+s_2=H_{2,n}(s_1,s_2)$, since $(s_1,s_2)\notin I_2$ by Lemma 2.1. For $(a_0,b_0)$ it is $(a_0-m)+(b_0-m)+m=a_0+b_0+m=H_{2,n}(a_0,b_0)$. Hence the symbols of $T$ are those of $T_g$, which are distinct. $\square$

The symbol-indexed gluing in Lemma 4.3 pairs the $n$ cells of $T_1\subset\mathbb{Z}_n^{d-2}$ and $T_2\subset\mathbb{Z}_n^2$ through the $n$ symbol pairs $(s_1,s_2)\in T_g$ so that the two turn corrections on $I_{d-2}$ and $I_2$ merge into the single turn correction on $I_d=I_{d-2}\times I_2$:

| Pair $(s_1,s_2)\in T_g$ | Factor cells $x(s_1)\in T_1,\ u(s_2)\in T_2$ | Coordinate sums in $\mathbb{Z}_n$ | Glued cell $(x(s_1),u(s_2))\in T$ and symbol $H_{d,n}(x(s_1),u(s_2))$ |
|---|---|---|---|
| $(s_1,s_2)\ne(a_0,b_0)$ ($n-1$ ordinary cells, $(s_1,s_2)\notin I_2$) | $x(s_1)\notin I_{d-2}$, $u(s_2)\notin I_2$ | $\sum_i x(s_1)_i=s_1$, $u(s_2)_1+u(s_2)_2=s_2$ | Outside $I_d$; symbol $s_1+s_2=H_{2,n}(s_1,s_2)$ |
| $(a_0,b_0)$ (unique special cell in $T_g\cap I_2$) | $x(a_0)\in T_1\cap I_{d-2}$, $u(b_0)\in T_2\cap I_2$ | $\sum_i x(a_0)_i=a_0-m$, $u(b_0)_1+u(b_0)_2=b_0-m$ | Inside $I_d$; symbol $(a_0-m)+(b_0-m)+m=a_0+b_0+m=H_{2,n}(a_0,b_0)$ |

**Theorem 4.4.** For all even $d\ge 2$ and even $n\ge 4$, every cell of $\mathbb{Z}_n^d$ lies in a transversal of $H_{d,n}$. In particular, Theorem 1.1 holds.

*Proof.* We use induction on $d$. The case $d=2$ is Theorem 3.3. Let $d\ge 4$, assume the statement for $d-2$, and let $y\in\mathbb{Z}_n^d$ and $w=w(y)$.

*Case 1: $y\in I_d$.* Let $\rho=(1,0,\dots,0)\in\mathbb{Z}_n^{d-2}$; then $\rho\notin I_{d-2}$ because $m\ge 2$. By the induction hypothesis and Lemma 4.1 with $(p,q)=(0,0)$, $H_{d,n}$ has a transversal $T_0$. If $x_0$ is its special cell, then $T_0+(y-x_0)$ is a transversal through $y$ by Lemma 2.2(1).

*Case 2: $y\notin I_d$, and two entries of $w$ sum to an element of $I$.* Apply Lemma 4.2.

*Case 3: $y\notin I_d$, and no two entries of $w$ sum to an element of $I$.* Then at most one entry of $w$ lies in $I$. If $w_k\in I$, let $\sigma$ exchange positions $1$ and $k$ (so $\sigma$ is the identity if $k=1$); if no entry of $w$ lies in $I$, let $\sigma$ be the identity. Put $y'=\Phi_{\sigma,1}(y)$ and write $y'=(\rho,p,q)$ with $\rho\in\mathbb{Z}_n^{d-2}$. Every entry of $w(y')$ other than the first lies outside $I$, and no two entries of $w(y')$ sum to an element of $I$. Hence $\rho\notin I_{d-2}$, because its second coordinate is not in $I$; $p,q\notin I$; $s_2:=p+q\notin I$; and, since $\rho\notin I_{d-2}$, we have $s_1:=H_{d-2,n}(\rho)=\rho_1+\dots+\rho_{d-2}$, so that $s_1+s_2=\rho_1+\dots+\rho_{d-2}+p+q=H_{d,n}(y')=-w(y')_{d+1}\notin I$.

By the induction hypothesis $\rho$ lies in a transversal $T_1$ of $H_{d-2,n}$; let $a_0\in I$ be its special symbol. The cell $\rho$ has symbol $s_1$ in $T_1$.

*The gluing transversal.* We find $b_0\in I$ and a transversal $T_g$ of $H_{2,n}$ through $(s_1,s_2)$ with special cell $(a_0,b_0)$. By Lemma 3.5 it suffices to find $b_0\in I$ such that $\mathcal{N}_n$ contains a triple whose first two entries are $s_1-a_0$ and $s_2-b_0$.

- *Case 3.1: $s_1\notin I$.* The triple $(s_1-a_0,\ s_2,\ m-s_1-s_2+a_0)$ is interior, and adding $(0,m,m)$ replaces its second entry $s_2$ by $s_2-m$. By Proposition 3.7 one of these two triples lies in $\mathcal{N}_n$, which gives $b_0\in\{0,m\}$.
- *Case 3.2: $s_1\in I$.* The cell $\rho$ and the special cell of $T_1$ are distinct, so $s_1\ne a_0$, and hence $s_1-a_0=m$. By Proposition 3.6 with $w=s_2$ there is $s_2'\in\{s_2,s_2+m\}$ with $(m,s_2',-s_2')\in\mathcal{N}_n$; put $b_0=s_2-s_2'$.

*The second factor.* We find a transversal $T_2$ of $H_{2,n}$ through $(p,q)$ with special symbol $b_0$. The cells $(u_2,v_2)\in I_2$ with $u_2+v_2+m=b_0$ are $(0,b_0+m)$ and $(m,b_0)$, and the corresponding triples $\tau(p-u_2,\ q-v_2)$ are

$$
t_c=\bigl(p,\ q-b_0-m,\ b_0-p-q\bigr)\quad\text{and}\quad t_c+(m,m,0).
$$

The triple $t_c$ is interior because $p$, $q$ and $p+q$ are not in $I$. By Proposition 3.7 one of the two triples lies in $\mathcal{N}_n$, and Lemma 3.5 gives $T_2$.

*Gluing.* By Lemma 4.3, $T_1$, $T_2$ and $T_g$ give a transversal $T'$ of $H_{d,n}$. It contains $(x(s_1),u(s_2))=(\rho,p,q)=y'$, because $(s_1,s_2)\in T_g$, $x(s_1)=\rho$, and $u(s_2)=(p,q)$; the symbol of $(p,q)$ is $p+q=s_2$, as $(p,q)\notin I_2$. Finally, $\Phi_{\sigma^{-1},1}(T')$ is a transversal through $y$. $\square$

The induction uses one transversal of $H_{d-2,n}$ per step and never requires a prescribed special symbol: in Case 3 the special symbol $a_0$ of $T_1$ is arbitrary, and Propositions 3.6 and 3.7 supply a compatible $b_0$ for either value of $a_0$.

## 5. Computational verification

The supplement contains a Python 3 program, using only the standard library, that implements the constructions of Sections 2 to 4 literally, and a separate checker that does not import the program. The program has two parts.

*Finite checks of the formulas.* For $2\le N\le 68$ the program builds the bijection of Lemma 2.3 for each of the $1{,}784$ pairs $(N,v_0)$ satisfying its hypothesis and checks the domain, the image and the sums. For even $n\le 60$ it builds $T_{N,a}$ for each of the $732$ pairs $(N,a)$ with $N\in\{m,m+1\}$, $a\in[1,N]$ and $N$ even or $a$ odd; it checks Lemma 3.1 for all of them, checks that the $718$ admissible ones are transversals with special cell $(0,0)$, and checks that the $14$ pairs with $2a=N+1$ fail at the cell $(m,m)$. For every even $n\le 100$, using integer arithmetic throughout, it checks that each of the $69{,}550$ seeds (L) and (O) is the triple of a cell of the corresponding transversal; it checks Lemma 3.4 for each of the $23{,}376$ pairs consisting of an admissible $(N,a)$ and an element $g\in\Gamma$; it checks that the case analysis of Theorem 3.3 produces each of the $171{,}696$ target cells; it checks that the parameters chosen in Proposition 3.6 satisfy its conclusion for all $2{,}450$ values of $w$; and it checks that the parameters chosen in Proposition 3.7 satisfy its range conditions and its conclusion for all $470{,}400$ pairs consisting of an interior triple and a direction $v$.

*Witness transversals.* For each of the $11$ pairs in Table 1 and each cell $y\in\mathbb{Z}_n^d$, the program runs the construction of Theorem 4.4 (Theorem 3.3 when $d=2$) and checks the resulting transversal. The checker then re-verifies every stored transversal directly from the definition of $H_{d,n}$: the transversal has $n$ cells, each coordinate and the symbol take every value of $\mathbb{Z}_n$ once, the target cell is contained, exactly one cell lies in $I_d$, and the targets of each file are exactly the $n^d$ cells of $\mathbb{Z}_n^d$. It also compares SHA-256 digests with the summary file written by the program. Fault-injection tests confirm that the checker rejects corrupted records: a repeated column, a repeated symbol, a target outside the transversal, a missing cell, an out-of-range coordinate, and a file with a repeated target.

**Table 1.** Cells for which a transversal was constructed and independently verified, by the case of Theorem 4.4 that applies to the target cell (for $d=2$ the construction of Theorem 3.3 is used).

| $(n,d)$ | cells $n^d$ | Case 1 | Case 2 | Case 3.1 | Case 3.2 |
|---|---:|---:|---:|---:|---:|
| $(4,2)$ | 16 | | | | |
| $(6,2)$ | 36 | | | | |
| $(8,2)$ | 64 | | | | |
| $(10,2)$ | 100 | | | | |
| $(4,4)$ | 256 | 16 | 240 | 0 | 0 |
| $(6,4)$ | 1,296 | 16 | 1,280 | 0 | 0 |
| $(8,4)$ | 4,096 | 16 | 3,920 | 160 | 0 |
| $(10,4)$ | 10,000 | 16 | 8,640 | 1,344 | 0 |
| $(4,6)$ | 4,096 | 64 | 4,032 | 0 | 0 |
| $(6,6)$ | 46,656 | 64 | 45,696 | 0 | 896 |
| $(8,6)$ | 262,144 | 64 | 261,184 | 512 | 384 |
| total | 328,760 | | | | |

All $328{,}760$ transversals passed both the program's own check and the independent check. The complete run, including the finite checks of the formulas, takes less than a minute of single-threaded Python. In Table 1, Case 3 of Theorem 4.4 never occurs for $n=4$, and Case 3.2 never occurs for $d=4$; both vanishings hold structurally for all parameters. Indeed, when $n=4$ ($m=2$), every element of $\mathbb{Z}_4\setminus I=\{1,3\}$ is odd, so the two entries of $w(y)$ outside $I$ that exist for every $y\notin I_d$ always sum into $I=\{0,2\}$; hence Case 2 applies to every $y\notin I_d$ in every even dimension $d\ge 4$. Likewise, when $d=4$, the prefix $\rho=(\rho_1,\rho_2)\in\mathbb{Z}_n^2\setminus I_2$ in Case 3 satisfies $s_1=H_{2,n}(\rho)=\rho_1+\rho_2=w(y')_1+w(y')_2$, which cannot lie in $I$ because no two entries of $w(y')$ sum into $I$; thus Case 3.2 ($s_1\in I$) requires $d\ge 6$, where it occurs for $(6,6)$ and $(8,6)$ (with both subcases 3.1 and 3.2 occurring for $(8,6)$).

*Example (Case 3.2).* For $(n,d)=(8,6)$ and $y=(1,1,1,1,1,1)$, no two entries of $w(y)=(1,1,1,1,1,1,2)$ sum to an element of $I=\{0,4\}$, and $s_1=H_{4,8}(1,1,1,1)=4\in I$. The construction returns the following transversal; each row lists a cell and its symbol, and the first row is the special cell.

| cell | symbol |
|---|---:|
| $(4,4,4,0,4,0)$ | 4 |
| $(5,6,7,5,7,5)$ | 3 |
| $(7,3,0,3,6,7)$ | 2 |
| $(3,7,3,6,2,4)$ | 1 |
| $(2,2,6,7,5,2)$ | 0 |
| $(0,0,2,4,3,6)$ | 7 |
| $(1,1,1,1,1,1)$ | 6 |
| $(6,5,5,2,0,3)$ | 5 |

## 6. Limitations and scope

Theorem 1.1 concerns only the family $H_{d,n}$, the cyclic hypercube with one turned subhypercube of order $2$. It says nothing about hypercubes with several turned subhypercubes, about other Latin hypercubes of even order and dimension, or about Conjecture 1 of [1] for odd $n$ or odd $d$. The proof yields one transversal through each entry; it gives no lower bound on the number of such transversals and no information on decompositions of $H_{d,n}$ into transversals. The maximum number $2^d$ of disjoint transversals is already attained by the translates found in [1]. The literature search described in Section 1.1 covers only the sources named there.

## 7. Reproducibility

The supplement contains the program, the checker, the summary file produced by the run reported in Section 5 (counts for each check, the case counts of Table 1, the example above, and SHA-256 digests of the eleven witness files), and a README with instructions. The witness files total about $44$ MB and are not included. Running `python3 -O latin_transversals.py all --out witnesses` in the supplement directory regenerates them deterministically, and `python3 -O check_witnesses.py witnesses --summary summary.json` verifies them and compares their digests with those recorded in the summary file shipped with the supplement; two independent runs produced identical files. Both scripts report failures through explicit exceptions rather than assertions, so the `-O` flag does not disable any check.

## References

[1] B. Child and I. M. Wanless, Latin hypercubes with restricted transversals, arXiv:2605.01813v1 [math.CO], 2026. https://arxiv.org/abs/2605.01813v1

[2] I. M. Wanless, Transversals in latin squares: a survey, in R. Chapman (ed.), Surveys in Combinatorics 2011, London Math. Soc. Lecture Note Ser. 392, Cambridge University Press, 2011, pp. 403–437 (preprint arXiv:0903.5142 [math.CO]). https://doi.org/10.1017/CBO9781139004114.010

[3] J. Egan and I. M. Wanless, Latin squares with restricted transversals, J. Combin. Des. 20(2) (2012), 124–141. https://doi.org/10.1002/jcd.20297

[4] A. Ghafari and I. M. Wanless, Latin squares whose transversals share many entries, arXiv:2412.12466v1 [math.CO], 2024. https://arxiv.org/abs/2412.12466v1

[5] Z. Luria, Latin squares with few transversals, arXiv:2609.08624v1 [math.CO], 2026. https://arxiv.org/abs/2609.08624v1

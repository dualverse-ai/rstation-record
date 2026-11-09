# Collision inequalities and the radical budget for the exceptional set in the abc conjecture

**Hongmin Li** (Institute of Science Tokyo; The University of Tokyo)

*Disclosure.* The arguments and computations in this manuscript were produced with substantial assistance from AI systems, operated and curated by the author, who is not a specialist in analytic number theory. The proofs have been checked by independent AI-assisted readings and the linear-programming trees by independent verifier programs, but they have not been reviewed by a human expert. Readers are invited to check every step; the supplement makes the computational part reproducible.

## 1. Problem and results

For $\lambda>0$ let
$$N_\lambda(X)=\#\{(a,b,c)\in\mathbb N^3:\ a+b=c\le X,\ \gcd(a,b,c)=1,\ \operatorname{rad}(abc)<c^\lambda\}.$$
The abc conjecture predicts $N_\lambda(X)=O_\lambda(1)$ for every fixed $\lambda<1$. The trivial bound is $N_\lambda(X)\ll X^{2\lambda/3+\varepsilon}$ [1, Proposition 1.1]. Bernert, Browning, Lichtman and Teräväinen [1] obtained the first general estimates beyond the trivial one: their Theorem 1.2 gives $N_\lambda(X)\ll X^{(23\lambda+3)/40+\varepsilon}$ for $0<\lambda\le2$, and their Theorem 1.3 gives $N_\lambda(X)\ll X^{3/5+\varepsilon}$ for $0<\lambda<1$, which improves the trivial bound only when $\lambda>9/10$. The exponent $3/5$ is the optimum of the linear program of [1, Proposition 6.1], built from an anatomic decomposition of $a,b,c$ into powerful parts [1, Proposition 2.1], the trivial bound [1, Proposition 2.3], a Fourier bound [1, Proposition 3.1] and a geometry-of-numbers bound [1, Proposition 4.1].

In [2] we added to this program a *two-letter collision inequality*, denoted $(\star)$ below: after freezing all but two powerful coordinates of two of the three letters, the free monomials $x^jy^k$ with $(j,k)\in\{(2,3),(3,4)\}$ satisfy a congruence modulo the frozen coefficient of the other letter, and the resulting multiplicative energy and difference counts can be bounded uniformly. The $24$ instances of $(\star)$ lower the value of the program below $3/5$, and [2, Main Theorem] states $N_\lambda(X)\ll X^{59969/100033+\varepsilon}$ for $0<\lambda\le1$, with $59969/100033=0.59949\ldots$.

The present paper has three results, all beyond [2].

**Theorem 1.1.** Let $U=54/91=0.593406\ldots$. For every $0<\lambda\le1$ and every $\varepsilon>0$,
$$N_\lambda(X)\ll_{\lambda,\varepsilon}X^{U+\varepsilon}.$$
The proof gives the slightly smaller exponent $5588/9417=0.593394\ldots$ (Proposition 5.1). Combined with the trivial bound, $N_\lambda(X)\ll X^{\min\{2\lambda/3,\,54/91\}+\varepsilon}$; on the common domain $0<\lambda<1$ of the bounds of [1], the new exponent improves on both $3/5$ and $2\lambda/3$ exactly when $81/91=0.8901\ldots<\lambda<1$. The gain over $3/5$ is $3/5-54/91=3/455$, about thirteen times the gain $3/5-59969/100033=254/500165$ of [2].

The second result describes how the exponent depends on the radical budget $\lambda$ on the interval $[0.70,1.10]$. Write $\lambda_0<\lambda_1<\dots<\lambda_4$ for $0.70,0.75,0.80,0.85,0.90$.

**Theorem 1.2.** (a) For $k=0,\dots,4$ let $D^*(\lambda_k)$ be given by
$$D^*(0.70)=\tfrac{109}{250},\quad D^*(0.75)=\tfrac{35}{76},\quad D^*(0.80)=\tfrac{59}{120},\quad D^*(0.85)=\tfrac{267}{520},\quad D^*(0.90)=\tfrac{71}{130}$$
(decimal values $0.4360$, $0.4605$, $0.4917$, $0.5135$, $0.5462$). Then $N_\lambda(X)\ll_{\lambda,\varepsilon}X^{D^*(\lambda_k)+\varepsilon}$ for every $0<\lambda\le\lambda_k$.

(b) There are explicit convex piecewise-linear functions $E_{\lambda_k}$ ($k=0,\dots,4$) and $E_1$, each the maximum of finitely many affine functions of $\mu$ with slopes in $[0,1]$ (respectively $[0,144/143]$ for $E_1$), with $E_{\lambda_k}(\lambda_k)=D^*(\lambda_k)$ and $E_1(1)=5588/9417$, such that
$$N_\mu(X)\ll_{\mu,\varepsilon}X^{\beta(\mu)+\varepsilon},\qquad \beta(\mu)=\begin{cases}\min\big(E_{\lambda_k}(\mu),E_{\lambda_{k+1}}(\mu),D^*(\lambda_{k+1})\big),&\mu\in[\lambda_k,\lambda_{k+1}],\ k\le3,\\ \min\big(E_{0.90}(\mu),\,E_1(\mu)\big),&\mu\in[0.90,1],\\ E_1(\mu),&\mu\in[1,1.10].\end{cases}$$
Since all slopes are non-negative, $E_1(\mu)\le E_1(1)=5588/9417<54/91$ for $\mu\le1$. The functions are determined by the trees in the supplement (Section 5); a table of values is given in Section 6.

(c) $E_1(\mu)\le3/5$ if and only if $\mu\le247/245=1.00816\ldots$, and $E_1(1.05)=89/140=0.6357\ldots$, $E_1(1.10)=6239/9170=0.6803\ldots$.

**Corollary 1.3.** (i) $N_\lambda(X)\ll_{\lambda,\varepsilon}X^{3/5+\varepsilon}$ for every $0<\lambda\le247/245$. (ii) For every $\lambda\in[0.70,1.10]$ the exponent $\beta(\lambda)$ of Theorem 1.2 is strictly smaller than
$$g(\lambda)=\begin{cases}\min\{(23\lambda+3)/40,\ 2\lambda/3,\ 3/5\},&\lambda<1,\\ \min\{(23\lambda+3)/40,\ 2\lambda/3\},&\lambda\ge1,\end{cases}$$
the smallest of the exponents of [1, Theorems 1.2 and 1.3] (the exponent $3/5$ being available for $\lambda<1$ only) and of the trivial bound. On $[0.70,1)$ the difference $g-\beta$ is at least $3/5-5588/9417=311/47085=0.0066\ldots$, and this is its infimum.

**The new input.** Theorem 1.1 rests on a generalized collision inequality, Proposition 4.1, denoted $(\star\star)$. Compared with $(\star)$ of [2] it allows an arbitrary coprime exponent pair $(j,k)$ with $1\le j<k\le6$ on the first letter, an arbitrary nonempty set of free coordinates on the second letter, and, for five specific pairs of free coordinates, a one-sided difference bound. Its proof needs two arithmetic inputs beyond [2]:

1. a uniform bound for the number of representations of a nonzero integer $m$ as a difference $x^jy^k-x'^jy'^k$ for the pairs $(j,k)\in\{(2,5),(3,5),(4,5)\}$, in addition to the pairs $(2,3),(3,4)$ treated in [2] (Lemma 3.1), obtained by reduction to the uniform counting lemma for the equations $\mathsf aU^e-\mathsf bV^e=m$, $e\in\{2,3\}$, of [2];
2. an estimate for the multiplicative energy $x^jy^k\equiv x'^jy'^k\pmod M$ in the unit group for any coprime pair $(j,k)$, through a Bézout parametrization of the congruence $g^j=h^k$ (Lemma 3.2); in [2] only $k-j=1$ was treated.

Moving a coordinate of the second letter from the frozen set into the free set lowers the number of frozen choices by its full exponent and raises the energy term by the same exponent, but the latter enters only with the factor $\frac12$; the price is a smaller modulus. This trade, which $(\star)$ does not allow, is the source of the improvement in Theorem 1.1. Inserting a finite subfamily of $(\star\star)$ into the program of [1] lowers its value below $54/91$. This is established by a branch-and-bound tree with $6{,}078$ leaves, each closed by a rational Farkas multiplier (Section 5). The trees and independent verifiers using only rational arithmetic are in the supplement.

**Where the improvements come from.** The values $D^*(\lambda_k)$ in Theorem 1.2 are the exact optima of a disjunctive program whose constraints are those of [1] with the radical budget $\lambda_k$ in place of $1$, all $2^{18}$ choices of index sets in the geometry-of-numbers bound rather than the thirteen used in [1], and the $24$ inequalities $(\star)$ of [2]. The same program without $(\star)$ has the same optimum at $\lambda_k\in\{0.70,0.75,0.80,0.90\}$, and the optimum $86/167=0.51497\ldots$ at $\lambda_k=0.85$. Thus at four of the five grid points the whole gain over [1] comes from running the program of [1] at budget $\lambda_k$ with all geometric constraints, not from the collision inequalities; the inequality $(\star)$ contributes at $\lambda=0.85$ and the inequality $(\star\star)$ at $\lambda=1$, where the program of [1] has value exactly $3/5$ (a witness is given in Section 8) and the program with the family $(\star\star)$ is bounded by $54/91$.

The bounds between grid points and for $\lambda>1$ in Theorem 1.2(b) come from a parametric reading of the same trees (Lemma 5.3): only the budget row of the program depends on $\lambda$, so the Farkas multipliers found at one budget give valid, explicitly computable bounds at every other budget. The extension to $\lambda>1$ uses that [1] proves its decomposition for $\lambda\le2$ and that $\lambda$ enters the constraints only through the budget row; this is checked in Sections 2 and 6.

**What is inherited from [2].** The framework of Section 2 is that of [1], as set up in [2, §2]. The counting lemma for $\mathsf aU^e-\mathsf bV^e=m$ with its uniform lower bound for fundamental units of real quadratic and pure cubic fields is [2, Lemma 3.1′] and is used without change (Section 3). The Cauchy–Schwarz reduction of Section 4 follows the proof of [2, Proposition 4.1], of which $(\star\star)$ is a strict generalization; the limiting argument of Section 6 extends [2, §6] to a general budget. Everything else — the three new rows of Lemma 3.1, Lemma 3.2 for coprime pairs, Proposition 4.1 and its frozen-modulus refinement in Appendix A, the six trees of Section 5 and their verifiers, Lemma 5.3, Theorems 1.1 and 1.2, Corollary 1.3, and the feasible points of Section 7 and Appendix A — is new. The tree of [2] (777 leaves, bound $59969/100033$) is superseded by the tree of Proposition 5.1 and is not used here.

**Scope.** The bound $U$ is an upper bound for the value of the program with the family $(\star\star)$ at $\lambda=1$; that program has a feasible point with $D=213/359=0.593314\ldots$ (Section 7), so the constraints used here cannot yield an exponent below $213/359$. Nothing is stated for $\lambda<0.70$ beyond Theorem 1.1 and the trivial bound, nor for $\lambda>1.10$.

## 2. The framework of Bernert–Browning–Lichtman–Teräväinen

We follow [1] (arXiv version 2, 9 May 2026). Write $x\sim X$ for $x\in(X,2X]$, with the convention that $x\sim1$ means $x\in[1,2]$, so that coordinates equal to $1$ belong to the lowest dyadic block. Let $N^*_\lambda(X)$ count the triples counted by $N_\lambda(X)$ with in addition $c\ge X/2$ and $\operatorname{rad}(abc)\ge c^\lambda/2$. A dyadic decomposition gives [1, §2]
$$N_\lambda(X)\ll(\log X)^2\max_{1\le Y\le X}\max_{\mu'\le\lambda}N^*_{\mu'}(Y).\tag{2.1}$$
For $d\in\mathbb N$, $(a_0,b_0,c_0)\in\mathbb N^3$ and dyadic parameters $\mathbf A,\mathbf B,\mathbf C\in\mathbb N^d$, let $B_d(a_0,b_0,c_0,\mathbf A,\mathbf B,\mathbf C)$ be the number of $(a_i,b_i,c_i)_{1\le i\le d}$ with $a_i\sim A_i$, $b_i\sim B_i$, $c_i\sim C_i$,
$$a_0\prod_{i=1}^d a_i^i+b_0\prod_{i=1}^d b_i^i=c_0\prod_{i=1}^d c_i^i,\qquad \gcd\Big(\prod_{i=0}^d a_i,\prod_{i=0}^d b_i,\prod_{i=0}^d c_i\Big)=1 .$$

**Proposition 2.1 ([1, Proposition 2.1]).** Let $0<\lambda\le2$. For any $\varepsilon_0>0$ there is $d=d(\varepsilon_0)\ge 6$ such that $N^*_\lambda(X)\ll_{\varepsilon_0}X^{\varepsilon_0}\max B_d(a_0,b_0,c_0,\mathbf A,\mathbf B,\mathbf C)$, the maximum over pairwise coprime $1\le a_0,b_0,c_0\le X^{\varepsilon_0}$ and dyadic $A_i,B_i,C_i\in[1,X]$ with
$$2^{-d-1}X^\lambda\le\prod_{j}A_jB_jC_j\le X^{\lambda+3\varepsilon_0/4},\qquad \prod_j A_j^j,\ \prod_j B_j^j\le X,\qquad X^{1-\varepsilon_0/2}\le\prod_jC_j^j\le X.$$

The proof in [1] uses only $a+b=c$, $\gcd(a,b,c)=1$ and dyadic pigeonholing, and [1] applies the proposition for all $\lambda\in(0,2]$ in the proof of its Theorem 1.2; the same remark applies to (2.1). Since $a+b=c$ and $\gcd(a,b,c)=1$, the three numbers $a_0\prod a_i^i$, $b_0\prod b_i^i$, $c_0\prod c_i^i$ are pairwise coprime; this is used in the proof of [1, Proposition 2.1] and will be used again below.

**Exponents.** Fix a box. For $s\in\{a,b,c\}$ write $S_i=X^{\alpha_{s,i}}$ for the dyadic parameters of the letter $s$, $\alpha_s=\sum_{i\le d}\alpha_{s,i}$, $L=\alpha_a+\alpha_b+\alpha_c$, and let $D$ be defined by $B_d=X^D$. Then $L\le\lambda+O(\varepsilon_0)$ and $\sum_{i\le d}i\,\alpha_{s,i}\le1$. With the abbreviations $a_i=\alpha_{a,i}$, $a=\alpha_a$ and so on, [1, Propositions 2.3, 3.1, 4.1] give, up to additive errors $O(\varepsilon_0)$ and $o(1)$ as $X\to\infty$:

- (B1) $L\le\lambda$; $\sum_{i\le6}s_i\le s$; $7s-\sum_{i\le6}(7-i)s_i\le1$ for $s\in\{a,b,c\}$ (these are (6.1)–(6.3) of [1], with the budget $\lambda$ kept as a parameter; the last follows from the full height budget $\sum_{i\le d}is_i\le1$ since $i\ge7$ for $i>6$);
- (B2) $D\le\min(a+b,a+c,b+c)$ ([1, Proposition 2.3], (6.4));
- (B3) with $F_s=\max(s_2+s_4+s_6,\ s_3+s_6,\ s_5)$: $F_a+F_b+F_c\le4L-6D$ ([1, Proposition 3.1] with $j,k,\ell\in\{2,3,5\}$, i.e. (6.10));
- (B4) for any $I_a,I_b,I_c\subseteq\{1,\dots,6\}$, with $\Sigma_0=\sum_s\sum_{i\in I_s}s_i$ and $\Sigma_1=\sum_s\sum_{i\in I_s}(i-1)s_i$:
$$D\le\max\big(L-\Sigma_0,\ L-1+\Sigma_1\big)\qquad([1,\ \text{Proposition }4.1]).$$

In (B3) and (B4) we use $L$ in place of $\lambda$. This is what the proofs give: the proof of [1, Proposition 3.1] bounds $B_d$ by $(ABC)^{2/3}$ divided by the sixth root of the three products of powerful coordinates, and the proof of [1, Proposition 4.1] produces $ABC/\prod\cdots$ and $X^{-1+3\varepsilon_0}ABC\prod\cdots$ before $ABC$ is replaced by $X^{\lambda+3\varepsilon_0}$; here $A=\prod A_i$, etc. The second term of [1, Proposition 4.1] is bounded using $c\ge X^{1-\varepsilon_0/2}$, a box condition of Proposition 2.1 that does not involve $\lambda$. Hence $\lambda$ enters (B1)–(B4) only through the budget row $L\le\lambda$; nothing in (B2)–(B4) requires $\lambda\le1$. [1, Proposition 6.1] states that (B1)–(B4) with $\lambda\le1$ (and thirteen specific choices in (B4), namely (6.5)–(6.9)) imply $D\le 3/5$, and this is how [1, Theorem 1.3] is deduced.

## 3. Two arithmetic lemmas

Throughout, for $1\le j<k\le6$ and $P,Q\ge1$,
$$S_{j,k}(P,Q)=\{x^jy^k:\ x\sim P,\ y\sim Q\}$$
is a set of *values*. By the divisor bound each value has $(PQ)^{o(1)}$ representations $x^jy^k$ with $x\sim P$, $y\sim Q$, since $x$ and $y$ divide it.

### 3.1 Differences

**Lemma 3.1.** Let $(j,k)\in\{(2,3),(3,4),(2,5),(3,5),(4,5)\}$. For $m\ne0$ let $r_{j,k}(m)=\#\{(u,u')\in S_{j,k}(P,Q)^2:\ u-u'=m\}$. Then for every $\eta>0$
$$r_{j,k}(m)\ll_\eta(PQ|m|)^\eta\min(PQ,Q^2),$$
and for $(j,k)\in\{(2,3),(3,4)\}$ also $r_{j,k}(m)\ll_\eta(PQ|m|)^\eta P^2$.

For $(j,k)\in\{(2,3),(3,4)\}$ this is [2, Lemma 3.1]. The bound $PQ$ is the size of the value set. In the remaining cases we fix the pair $(y,y')$ in $O(Q^2)$ ways, which reduces the count to an equation
$$\mathsf aU^e-\mathsf bV^e=m\ne0,\qquad \mathsf a,\mathsf b\ge1,\ e\in\{2,3\},\tag{3.1}$$
in positive integers $U,V$, as follows (the first two rows recall the reductions of [2]):

| monomial | fixed | remaining equation | $e$ |
| --- | --- | --- | --- |
| $x^2y^3$ | $y,y'$ | $y^3x^2-y'^3x'^2=m$ | 2 |
| $x^3y^4$ | $y,y'$ | $y^4x^3-y'^4x'^3=m$ | 3 |
| $x^2y^5$ | $y,y'$ | $y^5x^2-y'^5x'^2=m$ | 2 |
| $x^3y^5$ | $y,y'$ | $y^5x^3-y'^5x'^3=m$ | 3 |
| $x^4y^5$ | $y,y'$ | $y^5X^2-y'^5X'^2=m$, $X=x^2$ | 2 |

(Restricting $X$ to squares only shrinks the solution set.) For the last three monomials, fixing $(x,x')$ instead leaves an equation of degree $5$ in $y,y'$, which is not covered by the lemma below; this is why only the bound $Q^2$ is available for them. In every case all of $\mathsf a,\mathsf b,U,V,|m|$ are at most $\mathcal B^{O(1)}$ with $\mathcal B=2+PQ|m|$. Hence Lemma 3.1 follows from:

**Lemma 3.1′ ([2, Lemma 3.1′]).** The number of positive solutions $(U,V)$ of (3.1) with $\mathsf a,\mathsf b,U,V,|m|\le\mathcal B^{C}$ is $O_{C,\eta}(\mathcal B^\eta)$, uniformly in $\mathsf a,\mathsf b,m$. No coprimality of $U,V$ or of $\mathsf a,\mathsf b$ is assumed.

The proof in [2] writes $\alpha=\mathsf aU-\theta V$ with $\theta^e=\mathsf a^{e-1}\mathsf b$; when $\theta$ is an integer the equation factors over $\mathbb Z$, and otherwise $\alpha$ is an element of norm $\mathsf a^{e-1}m$ in a real quadratic or pure cubic field, whose unit group has rank one. The number of principal ideals of the given norm is bounded by a divisor-type function, and the number of generators of one ideal with all embeddings of size $\mathcal B^{\pm O(1)}$ is $O(\log\mathcal B)$ because the fundamental unit is at least $(1+\sqrt5)/2$ in the quadratic case and at least $5/4$ in the cubic case, uniformly in the field. For $e=2$ the statement is also a consequence of [3, Lemma 3.5].

### 3.2 Congruence energy in the unit group

**Lemma 3.2.** Let $1\le j<k\le6$ with $\gcd(j,k)=1$. For an integer $M\ge1$ let $K_{j,k}(P,Q;M)$ be the number of $(x,y,x',y')$ with $x,x'\sim P$, $y,y'\sim Q$, $\gcd(xyx'y',M)=1$ and $x^jy^k\equiv x'^jy'^k\pmod M$. Then
$$K_{j,k}(P,Q;M)\ll_\eta(PQM)^\eta\,PQ\,\sqrt{(1+P^2/M)(1+Q^2/M)}.$$

*Proof.* Let $G=(\mathbb Z/M\mathbb Z)^\times$, $g=x/x'$ and $h=y'/y$ in $G$. The congruence is $g^j=h^k$. Choose integers $u,v$ with $uk-vj=1$. The map $\Phi:z\mapsto(z^k,z^j)$ sends $G$ into $\{(g,h)\in G^2:g^j=h^k\}$, and $\Psi:(g,h)\mapsto g^uh^{-v}$ is its inverse: $\Psi(\Phi(z))=z^{uk-vj}=z$, and if $g^j=h^k$ then
$$(g^uh^{-v})^k=g^{uk}h^{-vk}=g\,(g^{j})^{v}(h^{k})^{-v}=g,\qquad (g^uh^{-v})^j=g^{uj}h^{-vj}=h\,(g^{j})^{u}(h^{k})^{-u}=h .$$
So $\Phi$ is a bijection onto the solution set. For $N\ge1$ and $w\in G$ let $R_N(w)$ be the number of $(s,t)$ with $s,t\sim N$, $\gcd(st,M)=1$ and $s/t=w$ in $G$. Then
$$K_{j,k}(P,Q;M)=\sum_{z\in G}R_P(z^k)\,R_Q(z^j).$$
Let $\rho_e(M)=\#\{w\in G:w^e=1\}$. For odd $p$ the group $(\mathbb Z/p^r)^\times$ is cyclic, so $\rho_e(p^r)\le e$; the group $(\mathbb Z/2^r)^\times$ is a product of at most two cyclic groups, so $\rho_e(2^r)\le e^2$. By the Chinese remainder theorem $\rho_e(M)\le e^{2\omega(M)}\le36^{\omega(M)}\ll_\eta M^\eta$ for $e\le6$. Each fibre of $z\mapsto z^e$ has at most $\rho_e(M)$ elements; Cauchy–Schwarz gives
$$K_{j,k}^2\le\rho_k(M)\rho_j(M)\,\mathcal M_P\,\mathcal M_Q,\qquad \mathcal M_N=\sum_{w\in G}R_N(w)^2 .$$
Now $\mathcal M_N$ counts $(s,t,s',t')$ with all entries $\sim N$, coprime to $M$, and $st'\equiv s't\pmod M$. Fix $(s,t')$, hence $n=st'\le4N^2$. The product $s't\le4N^2$ lies in the residue class of $n$ modulo $M$, so it takes $O(1+N^2/M)$ values, each with $N^{o(1)}$ factorizations. Thus $\mathcal M_N\ll_\eta N^{2+\eta}(1+N^2/M)$, and the lemma follows. $\square$

For $k-j=1$ one may take $u=v=1$, and $\Psi(g,h)=g/h$; this is the case treated in [2, Lemma 3.2]. The pairs with $k-j\ge2$, namely $(1,3),(1,4),(1,5),(2,5),(3,5)$ and $(1,6)$, are new, and the first five of them occur in the tree of Proposition 5.1.

If $P=X^p$, $Q=X^q$ and $M\ge X^{w}$ with $M\le X^{O(1)}$, the bound is $X^{\kappa+o(1)}$ with
$$\kappa(p,q;w)=p+q+\tfrac12\big((2p-w)_++(2q-w)_+\big),$$
and since the right-hand side of Lemma 3.2 is non-increasing in $M$ apart from the factor $M^\eta$, only a lower bound for $M$ is needed.

## 4. The collision inequality

Fix an ordered pair of distinct letters $(A,B)$ from $\{a,b,c\}$ and let $C$ be the third letter. Choose

- an exponent pair $p_A=(j_A,k_A)$ with $1\le j_A<k_A\le6$ and $\gcd(j_A,k_A)=1$ (there are eleven such pairs);
- a nonempty set $I_B\subseteq\{1,\dots,6\}$ of free indices of $B$.

Put $p=\alpha_{A,j_A}$, $q=\alpha_{A,k_A}$, and
$$f_A=\alpha_A-p-q,\qquad f_B=\alpha_B-\sum_{i\in I_B}\alpha_{B,i},\qquad \delta=\sum_{i\in I_B}\alpha_{B,i},\qquad w_B=\sum_{\substack{i\le6\\ i\notin I_B}}i\,\alpha_{B,i}+7\Big(\alpha_B-\sum_{i\le6}\alpha_{B,i}\Big).$$
Here $f_A$ and $f_B$ are the exponents of the numbers of frozen choices, $\delta$ is the exponent of the size of the value set of the free monomial of $B$, and $w_B$ is a lower bound for the exponent of the frozen coefficient of $B$.

**Proposition 4.1.** In the setting of Proposition 2.1, every box satisfies, up to additive $o(1)$ as $X\to\infty$ (for fixed $d$),
$$D\le f_A+f_B+\max\Big(\alpha_C,\ \tfrac12\big(\alpha_C+\delta+\kappa(p,q;w_B)\big)\Big).\tag{\star\star}$$
If moreover $I_B\in\big\{\{2,3\},\{3,4\},\{2,5\},\{3,5\},\{4,5\}\big\}$, then $\delta$ may be replaced by $\min(\delta,\delta')$, where $\delta'=2\min(\alpha_{B,2},\alpha_{B,3})$ for $I_B=\{2,3\}$, $\delta'=2\min(\alpha_{B,3},\alpha_{B,4})$ for $I_B=\{3,4\}$, and $\delta'=2\alpha_{B,5}$ for $I_B\in\{\{2,5\},\{3,5\},\{4,5\}\}$.

The special case $p_A\in\{(2,3),(3,4)\}$, $I_B=\{j,k\}\in\{\{2,3\},\{3,4\}\}$, with $\delta$ replaced by $\min(\delta,\delta')=\min(r+s,2r,2s)$, $r=\alpha_{B,j}$, $s=\alpha_{B,k}$, is the inequality
$$D\le f_A+f_B+\max\Big(\alpha_C,\ \tfrac12\big(\alpha_C+\min(r+s,2r,2s)+\kappa(p,q;w_B)\big)\Big)\tag{\star}$$
of [2, Proposition 4.1]; its $24$ instances are the ones used in Theorem 1.2. Altogether there are $6\cdot11\cdot63=4{,}158$ instances of $(\star\star)$ (six ordered letter pairs, eleven pairs $p_A$, $63$ nonempty sets $I_B$). Appendix A proves a further generalization in which a set $O_C$ of coordinates of the third letter is frozen as well and acts as a second modulus; that generalization is not needed for the theorems of this paper and serves only to delimit the method in Section 7 and Appendix A.

*Proof.* Let $(z_i)_{1\le i\le d}$ be the coordinates of the letter $A$ and $z_0\in\{a_0,b_0,c_0\}$ its fixed small coefficient, and similarly $(z'_i)$, $z'_0$ for $B$ and $(z''_i)$, $z''_0$ for $C$. Put
$$u=z_{j_A}^{\,j_A}z_{k_A}^{\,k_A},\quad M_A=z_0\prod_{i\notin p_A}z_i^{\,i},\qquad v=\prod_{i\in I_B}z_i'^{\,i},\quad M_B=z'_0\prod_{i\notin I_B}z_i'^{\,i},\qquad w=z''_0\prod_{i\le d}z_i''^{\,i}.$$
The products defining $M_A$ and $M_B$ run over *all* indices $1\le i\le d$ outside the chosen sets, including all $i\ge7$. The equation of $B_d$ reads $\pm M_Au\pm M_Bv=\pm w$ for a suitable arrangement of signs.

*(a) Freezing and the Cauchy–Schwarz step.* The coordinates entering $M_A$ and $M_B$ can be chosen in $\ll\prod_{i\notin p_A}A_i\prod_{i\notin I_B}B_i=X^{f_A+f_B+o(1)}$ ways (here $A_i,B_i$ denote the dyadic parameters). Fix them. Since each coordinate is at least its dyadic parameter and the small coefficient is at least $1$,
$$\log_X M_B\ge\sum_{\substack{i\le6\\ i\notin I_B}}i\,\alpha_{B,i}+\sum_{i\ge7}i\,\alpha_{B,i}\ge w_B,$$
because $\sum_{i\ge7}i\alpha_{B,i}\ge7\sum_{i\ge7}\alpha_{B,i}=7(\alpha_B-\sum_{i\le6}\alpha_{B,i})$. All quantities are $\le X^{O(1)}$. By the divisor bound, each value $u$, $v$, $w$ has $X^{o(1)}$ representations by coordinates; we therefore count pairs of values $(u,v)$ for which there is a primitive solution, and multiply by $X^{o(1)}$ at the end. The value $w$ ranges over a set $\mathcal W$ with $|\mathcal W|\le X^{\alpha_C+o(1)}$, the number of choices of the coordinates of $C$. For $w\in\mathcal W$ let $n_w$ be the number of such pairs $(u,v)$ and $N=\sum_w n_w$. By Cauchy–Schwarz,
$$N^2\le|\mathcal W|\sum_w n_w^2=|\mathcal W|\,(N+E_{\rm off}),\qquad N\ll|\mathcal W|+\sqrt{|\mathcal W|\,E_{\rm off}},$$
where $E_{\rm off}$ is the number of ordered pairs of distinct pairs $(u,v)\ne(u',v')$, each coming from a primitive solution, with the same $w$.

*(b) Coprimality.* By the pairwise coprimality recalled after Proposition 2.1, $\gcd(M_Au,M_Bv)=1$ for every counted solution. If $\gcd(M_A,M_B)>1$ the fibre is empty; otherwise $M_A$ is invertible modulo $M_B$ and $\gcd(u,M_B)=1$, so all coordinates of $u$ are units modulo $M_B$. No coprimality between coordinates of the same letter, and none between different solutions, is assumed.

*(c) The pairs $(u,u')$.* For a pair counted by $E_{\rm off}$, subtracting the two equations gives $M_A(u-u')=\mp M_B(v-v')$. If $u=u'$ then $v=v'$ since $M_B>0$; hence $u\ne u'$ and $v\ne v'$. As $\gcd(M_A,M_B)=1$, we get $u\equiv u'\pmod{M_B}$ with $\gcd(uu',M_B)=1$. Lifting to coordinates, the number of such $(u,u')$ is at most $K_{j_A,k_A}(X^p,X^q;M_B)\le X^{\kappa(p,q;w_B)+o(1)}$ by Lemma 3.2.

*(d) The pairs $(v,v')$ for given $(u,u')$.* Fix $(u,u')$. The value $v$ ranges over the value set of the free monomial of $B$, which has at most $X^{\delta+o(1)}$ elements, and $v'=v\pm M_A(u-u')/M_B$ is determined by $v$. Hence $E_{\rm off}\le X^{\kappa+\delta+o(1)}$.

*(e) The alternative count through differences.* Let $I_B=\{j,k\}$ be one of the pairs of Lemma 3.1. For fixed $(u,u')$ the shift $m=\mp M_A(u-u')/M_B$ is a fixed nonzero integer of size $X^{O(1)}$, and by Lemma 3.1 the number of $(v,v')$ with $v-v'=m$ is $\le X^{\delta'+o(1)}$ with $\delta'$ as in the statement (the bound $PQ$ of Lemma 3.1 is the value $\delta=\alpha_{B,j}+\alpha_{B,k}$ already obtained in (d)). Hence $E_{\rm off}\le X^{\kappa+\min(\delta,\delta')+o(1)}$ in this case. The signs in the equation play no role, since Lemma 3.1 allows $m$ of either sign.

*(f) Conclusion.* Multiplying $N\ll|\mathcal W|+\sqrt{|\mathcal W|E_{\rm off}}$ by the $X^{f_A+f_B+o(1)}$ frozen choices and taking logarithms gives $(\star\star)$, with $\alpha_C$ from $|\mathcal W|$ and $\frac12(\alpha_C+\kappa+\delta)$ from the square root. $\square$

The implied constants depend on $d$, $\varepsilon_0$ and the divisor-bound parameter, but not on the frozen coefficients; this uniformity is needed when maximizing over boxes. Moving an index $i$ of $B$ from the frozen set into $I_B$ lowers $f_B$ by $\alpha_{B,i}$ and raises $\delta$ by $\alpha_{B,i}$, which enters only with the factor $\frac12$; the price is a smaller modulus $w_B$ in $\kappa$. In the tree of Proposition 5.1 twelve different sets $I_B$ occur, seven of them of size three or four.

## 5. The disjunctive programs and their trees

Because (B4), $(\star)$ and $(\star\star)$ are disjunctions of linear inequalities, each program below is a disjunctive (mixed-integer) linear program; we reserve the term *linear program* for each branch.

**Variables and constraints.** We use 25 non-negative variables: $s_1,\dots,s_6,s$ for $s\in\{a,b,c\}$, $F_a,F_b,F_c$ and $D$. For a budget $\lambda>0$ the root system $\mathcal R(\lambda)$ consists of (B1)–(B3) written linearly ($a+b+c\le\lambda$; $\sum_{i\le6}s_i\le s$ and $7s-\sum_{i\le6}(7-i)s_i\le1$ for each letter; $D\le a+b$, $D\le a+c$, $D\le b+c$; $F_s\ge s_2+s_4+s_6$, $F_s\ge s_3+s_6$, $F_s\ge s_5$; $F_a+F_b+F_c\le4(a+b+c)-6D$), 20 inequalities in all, together with the ordering
$$a_4+2a_5\ \ge\ b_4+2b_5\ \ge\ c_4+2c_5 ,\tag{5.1}$$
22 rows in total. Only the first row depends on $\lambda$. The full family of constraints (B1)–(B4), $(\star)$, $(\star\star)$ is invariant under relabelling the three letters (each constraint depends only on the exponents of the boxes, not on which letter is the sum), so any feasible point can be relabelled into the closed region (5.1).

**Disjunctions.** A constraint (B4) for a choice $(I_a,I_b,I_c)$ is a disjunction of two linear inequalities. The instances of $(\star\star)$ are labelled in the trees by $(A,p_A,B,I_B,k_B,O_C)$ with a distinguished index $k_B\in I_B$ and a frozen set $O_C$ of the third letter, the labels of the general inequality of Appendix A; in every instance branched on, $O_C=\emptyset$, and then the right-hand side does not depend on $k_B$. Write $t_1=2p-w_B$, $t_2=2q-w_B$ and $t_3=\alpha_{B,k_B}-w_C$, where $w_C=\sum_{i\in O_C}i\,\alpha_{C,i}$ vanishes for $O_C=\emptyset$. Then the general inequality is equivalent to the disjunction of nine linear systems: $D\le f_A+f_B+\alpha_C$; or, for one of the eight closed sign octants $\sigma_it_i\ge0$ or $\le0$ ($i=1,2,3$), with $\kappa$ and $\delta$ replaced by the affine expressions $p+q+\frac12(\sigma_1t_1+\sigma_2t_2)$ and $\sum_{i\in I_B,i\ne k_B}\alpha_{B,i}+\sigma_3t_3$ ($\sigma_i\in\{0,1\}$ indicating the positive side),
$$D\le f_A+f_B+\tfrac12\big(\alpha_C+\delta_\sigma+\kappa_\sigma\big),$$
together with, in the instances with $I_B$ a pair of Lemma 3.1, the rows in which $\delta_\sigma$ is substituted by each admissible value of $\delta'$. For $O_C=\emptyset$ one has $t_3=\alpha_{B,k_B}\ge0$, so the octants with $\sigma_3=0$ lie in the hyperplane $\alpha_{B,k_B}=0$, where $\delta_\sigma=\delta$ in both cases; the nine branches are then a valid, if redundant, covering of the disjunction $(\star\star)$. In the same way $(\star)$ is the disjunction of five linear systems (the diagonal branch and four sign quadrants for $t_1,t_2$, each with the two rows for $\delta'\in\{2r,2s\}$). Every feasible point satisfies at least one branch of each disjunction; the octants may overlap on their boundaries.

**Trees and multipliers.** A branch-and-bound tree for a budget $\lambda$ has a root carrying $\mathcal R(\lambda)$; each internal node branches on one constraint (B4) (two children), $(\star)$ (five children) or $(\star\star)$ (nine children), all children being present, so the leaves cover every feasible point. A leaf $\ell$ carries the linear system $A_\ell x\le b_\ell$ formed by the root rows and the branch rows on its path, together with a vector $y_\ell$ of positive rationals indexed by some of these rows such that
$$(y_\ell^{T}A_\ell)_D=1,\qquad (y_\ell^{T}A_\ell)_v\ge0\ \ (v\ne D),\qquad y_\ell^{T}b_\ell=\beta_\ell .$$
For $x\ge0$ satisfying the leaf system, $D\le y_\ell^TA_\ell x\le\beta_\ell$. Omitting other valid constraints at a leaf only enlarges its region, so $D\le\max_\ell\beta_\ell$ on the whole feasible set.

**Proposition 5.1 (budget $1$, family $(\star\star)$).** Every point of $\mathbb R_{\ge0}^{25}$ satisfying $\mathcal R(1)$, all constraints (B4) and all instances of $(\star\star)$ (with the refinement of Proposition 4.1) has $D\le5588/9417<54/91$.

*Proof (computer-assisted).* The supplement contains a tree with $1{,}349$ nodes branching on (B4) (on $198$ distinct triples $(I_a,I_b,I_c)$), $591$ nodes branching on $(\star\star)$ (on $82$ distinct instances $(A,p_A,B,I_B)$; the pairs $p_A$ occurring are $(3,4),(2,3),(1,3),(3,5),(4,5),(2,5),(1,4),(1,5)$ and the sets $I_B$ occurring are $\{2,3\},\{3,4\},\{3,5\},\{2,5\},\{1,2,3\},\{1,2,3,5\},\{1,2,3,4\},\{1,3,5\},\{2,3,5\},\{1,3,4\},\{1,2,4\},\{1,3\}$), $6{,}078$ leaves and depth at most $24$. The largest leaf bound is $\max_\ell\beta_\ell=5588/9417$. The verifier rebuilds every row from the formulas of Sections 2, 4 and 5, checks that the node labels are legal (subsets of $\{1,\dots,6\}$, $\gcd(j_A,k_A)=1$, $k_B\in I_B$), that all children are present, and checks the three conditions at every leaf in exact rational arithmetic; no floating-point solver is involved. $\square$

**Proposition 5.2 (budgets $\lambda_k$, family $(\star)$).** For $k=0,\dots,4$, every point of $\mathbb R_{\ge0}^{25}$ satisfying $\mathcal R(\lambda_k)$, all constraints (B4) and all $24$ instances of $(\star)$ has $D\le D^*(\lambda_k)$, with $D^*(\lambda_k)$ as in Theorem 1.2. Moreover each value is attained: the supplement records, for each $k$, a rational point with $D=D^*(\lambda_k)$ that satisfies $\mathcal R(\lambda_k)$, all $2^{18}$ constraints (B4) and all $24$ constraints $(\star)$, so $D^*(\lambda_k)$ is the exact optimum of this program.

*Proof (computer-assisted).* The supplement contains five trees with $713$, $314$, $5{,}286$, $2{,}313$ and $6{,}667$ leaves and depths $27$, $30$, $40$, $34$ and $44$, and a second verifier of the same kind, written independently of the first, which rebuilds the rows with the budget $\lambda_k$ in the first row, checks the trees, and checks the recorded points against every constraint in exact arithmetic. The supplement also contains, for the same budgets, trees for the program without $(\star)$ (with $694$, $304$, $2{,}093$, $1{,}060$ and $377$ leaves) and attained points, giving the values $109/250$, $35/76$, $59/120$, $86/167$, $71/130$ quoted in Section 1. $\square$

**Lemma 5.3 (parametric bounds).** Let a tree with root system $\mathcal R(\lambda)$ have leaf multipliers $y_\ell$ and bounds $\beta_\ell$, and let $y_{\ell,0}\ge0$ be the multiplier of the budget row. Then for every $\mu>0$, every point satisfying $\mathcal R(\mu)$ and the constraints branched on in the tree has
$$D\le E_\lambda(\mu):=\max_\ell\big(\beta_\ell+y_{\ell,0}(\mu-\lambda)\big).$$
Moreover, if $\mu\le\mu'$, every point feasible for the budget $\mu$ is feasible for the budget $\mu'$.

*Proof.* The rows of the tree for budget $\mu$ differ from those for budget $\lambda$ only in the right-hand side of the budget row, which changes from $\lambda$ to $\mu$: the branch rows of (B4), $(\star)$ and $(\star\star)$ do not involve the budget, since they are written with $L=a+b+c$ in place of $\lambda$ (Section 2). Hence $A_\ell$ is unchanged, $y_\ell^Tb_\ell(\mu)=\beta_\ell+y_{\ell,0}(\mu-\lambda)$, and the two conditions on $y_\ell^TA_\ell$, which do not involve the right-hand side, remain satisfied; for $x\ge0$ in a leaf region, $D\le y_\ell^TA_\ell x\le y_\ell^Tb_\ell(\mu)$. Taking the maximum over leaves gives the bound. The second statement holds because only the budget row depends on the budget and its right-hand side increases with $\mu$. $\square$

The functions $E_{\lambda_k}$ of Theorem 1.2 are the functions $E_\lambda$ of Lemma 5.3 for the five trees of Proposition 5.2, and $E_1$ is the function for the tree of Proposition 5.1. They are convex and piecewise linear with slopes $y_{\ell,0}$; in the five trees of Proposition 5.2 all slopes are at most $1$ (at most $6557/7617$ for $\lambda=0.75$), and in the tree of Proposition 5.1 they are at most $144/143$. Linear interpolation between grid values is *not* claimed: the value function of a disjunctive program need not be concave, and the bound $\beta(\mu)$ of Theorem 1.2 is a consequence of the Farkas identities with a different right-hand side, not an interpolation.

**Reproduction.** From the unpacked supplement, in the directory containing the scripts,

```
python3 unpack.py
python3 check_starstar.py
python3 check_lambda.py --envelope
python3 check_lambda.py cert_base_0p70.json cert_base_0p75.json cert_base_0p80.json cert_base_0p85.json cert_base_0p90.json
python3 parametric_bounds.py
```

(standard library only, Python 3.9 or later). The first command extracts the trees; the second verifies the tree of Proposition 5.1 and the feasible points of Section 7, Section 8 and Appendix A; the third verifies the five trees of Proposition 5.2 and their attained points and prints the midpoint values of the envelope; the fourth does the same for the five trees of the program without $(\star)$; the last prints the values of $E_{\lambda_k}$ and $E_1$ used in Section 6 and checks the inequality of Corollary 1.3(ii) at every breakpoint. Every check in the verifiers raises an explicit exception rather than an `assert` statement, so they cannot be silenced by running the interpreter with optimization flags. The generators that found the trees (which use a floating-point solver only to propose bases, every multiplier being re-derived in rational arithmetic before it is written) are included for documentation but are not needed for the proofs, and the verifiers do not import them. As a control, the first verifier also runs on seven deliberately corrupted copies of its tree (a perturbed multiplier, a perturbed multiplier with matching bound, a root row deleted in two different ways, a missing child, a lowered target constant, a non-coprime exponent pair) and rejects each of them.

## 6. Proofs of Theorems 1.1 and 1.2 and of Corollary 1.3

**The limiting argument.** Let $\Lambda\in\{\lambda_0,\dots,\lambda_4,1\}$ and let $\mathcal P(\Lambda)$ be the program of Proposition 5.1 (if $\Lambda=1$) or Proposition 5.2 (if $\Lambda=\lambda_k$), with optimum bound $\beta^*(\Lambda)$ equal to $5588/9417$ or $D^*(\lambda_k)$. We show that $N_\lambda(X)\ll_{\lambda,\varepsilon}X^{\beta^*(\Lambda)+\varepsilon}$ for every $0<\lambda\le\Lambda$. Suppose this fails for some $\lambda\le\Lambda$ and $\varepsilon>0$. By (2.1) there are $Y\to\infty$ and $\mu'\le\lambda$ with $N^*_{\mu'}(Y)\ge Y^{\beta^*+\varepsilon/2}$; fix $D_0\in(\beta^*,\beta^*+\varepsilon/2)$. Let $\varepsilon_0=1/n$, $n\to\infty$. For each $n$, Proposition 2.1 (with $X$ replaced by $Y$ and $\lambda$ by $\mu'$) gives, for arbitrarily large $Y$, a box with $B_d\ge Y^{\beta^*+\varepsilon/2-1/n-o(1)}\ge Y^{D_0}$ once $n$ is large, where $d=d(1/n)$. For each $n$ choose $Y=Y_n$ so large that all $o(1)$ terms in (B1)–(B4), $(\star)$ and $(\star\star)$ are at most $1/n$; this is possible because, for fixed $d$, there are finitely many constraints (all $(I_a,I_b,I_c)$ with $I_s\subseteq\{1,\dots,6\}$, the $24$ instances of $(\star)$ and the $4{,}158$ instances of $(\star\star)$), each holding up to $o(1)$ uniformly over boxes.

Record the vector $\xi_n=(\alpha_{s,i})_{s\in\{a,b,c\},\,i\le6}\cup(\alpha_a,\alpha_b,\alpha_c)$ and $D_n\ge D_0$. Only these $21$ coordinates enter the constraints — the tail $i\ge7$ enters only through $\alpha_s-\sum_{i\le6}\alpha_{s,i}$ — so the dimension does not depend on $d$. The vectors lie in a compact set ($0\le\alpha_{s,i}\le1$, $\alpha_s\le1$, $D_n\le\alpha_a+\alpha_b\le2$), so a subsequence converges to $(\xi,D_\infty)$ with $D_\infty\ge D_0$. All constraints are closed conditions (finite maxima, minima and positive parts of affine functions), and their errors are $O(1/n)+O(\varepsilon_0)\to0$; in particular $L\le\mu'+O(\varepsilon_0)\le\Lambda+O(1/n)$ gives $L\le\Lambda$ in the limit. Relabelling the letters to satisfy (5.1), the limit point satisfies all hypotheses of $\mathcal P(\Lambda)$ with $D_\infty>\beta^*(\Lambda)$, a contradiction. $\square$

**Proof of Theorem 1.1.** Take $\Lambda=1$: $N_\lambda(X)\ll X^{5588/9417+\varepsilon}\le X^{54/91+\varepsilon}$ for $\lambda\le1$. $\square$

**Proof of Theorem 1.2.** Part (a) is the limiting argument with $\Lambda=\lambda_k$. For (b) and (c), fix a budget $\mu\in[0.70,1.10]$ and run the limiting argument with $\mathcal P(\Lambda)$ replaced by the system "root rows $\mathcal R(\mu)$ and the constraints branched on in one or several of the trees": the limit point satisfies $\mathcal R(\mu)$ (since $L\le\mu$ in the limit) together with all constraints (B4), $(\star)$ and $(\star\star)$, so Lemma 5.3 applied to each tree gives $D_\infty\le E_{\lambda}(\mu)$ for each tree budget $\lambda$, and the monotonicity statement of Lemma 5.3 gives $D_\infty\le D^*(\lambda_{k+1})$ for $\mu\le\lambda_{k+1}$. Taking the minimum of the available bounds gives $\beta(\mu)$. The statements about $E_1$ in (c) are read off the tree of Proposition 5.1 in exact arithmetic (fifth command of Section 5): the largest $\mu$ with $E_1(\mu)\le3/5$ is $247/245$, since the leaf attaining the minimum of $(3/5-\beta_\ell)/y_{\ell,0}$ over leaves with $y_{\ell,0}>0$ has this quotient equal to $2/245$ and no leaf with $y_{\ell,0}=0$ has $\beta_\ell>3/5$; and $E_1(21/20)=89/140$, $E_1(11/10)=6239/9170$. $\square$

**Validity for $\mu>1$.** For $\mu>1$ the argument uses (2.1) and Proposition 2.1 with $\lambda\in(1,2]$, which [1] proves in that range, and the fact noted in Section 2 that $\lambda$ enters (B1)–(B4) only through the budget row. The proofs of Lemmas 3.1, 3.2 and Proposition 4.1 involve box sizes, the pairwise coprimality of $a,b,c$ and moduli bounded below by products of dyadic parameters, and never the size of $\lambda$. The compactness step needs $D$ bounded, which $D\le a+b\le L\le\mu$ provides. For $\lambda<1$ one may instead argue as in [1, §6], using the room $1-\lambda$ to obtain $L\le1$ for small $\varepsilon_0$; the limiting argument is what covers the endpoints $\lambda=\Lambda$.

**Values of the envelope.** The following values were computed in exact arithmetic from the trees (fifth command of Section 5); decimals are rounded.

| $\mu$ | $\beta(\mu)$ | $\mu$ | $\beta(\mu)$ | $\mu$ | $\beta(\mu)$ |
| --- | --- | --- | --- | --- | --- |
| 0.70 | 0.436000 | 0.85 | 0.513462 | 1.00 | 0.593395 |
| 0.725 | 0.448427 | 0.875 | 0.531780 | 1.025 | 0.613983 |
| 0.75 | 0.460526 | 0.90 | 0.546154 | 1.05 | 0.635714 |
| 0.775 | 0.479489 | 0.925 | 0.563462 | 1.075 | 0.658043 |
| 0.80 | 0.491667 | 0.95 | 0.583215 | 1.10 | 0.680371 |
| 0.825 | 0.509405 | 0.975 | 0.593080 | | |

For comparison, $g(\mu)$ equals $2\mu/3$ on $[0.70,0.90]$ (values $0.4667$ to $0.6$), $(23\mu+3)/40$ on $[0.90,21/23]$, $3/5$ on $[21/23,1)$, and $(23\mu+3)/40$ on $[1,1.10]$ (values $0.65$ to $0.7075$). Near $\mu=1$ the smaller of the two bounds is $E_1$: for $0.97\le\mu\le0.99$ one has $\beta(\mu)=E_1(\mu)=857/1445=0.593080\ldots$, slightly below $E_1(1)=5588/9417$, because a leaf with budget multiplier $0$ dominates there. A table at steps of $0.01$ is printed by the fifth command.

**Proof of Corollary 1.3.** (i) For $\lambda\le1$ this is Theorem 1.1 since $54/91<3/5$; for $1<\lambda\le247/245$ it is Theorem 1.2(b),(c).

(ii) The function $g$ is the minimum of affine functions on each of the two intervals $[0.70,1)$ and $[1,1.10]$, hence concave on each of them; at $\mu=1$ it jumps upwards from $3/5$ to $13/20$, so the two intervals are treated separately. On an interval $[\lambda_k,\lambda_{k+1}]$ with $k\le3$ (all contained in $[0.70,0.90]$) we have $\beta\le E_{\lambda_k}$, and $E_{\lambda_k}$ is convex, so $E_{\lambda_k}$ lies below its chord while $g$ lies above its chord; it therefore suffices to check the endpoints: $D^*(\lambda_k)<g(\lambda_k)$ and $E_{\lambda_k}(\lambda_{k+1})<g(\lambda_{k+1})$. In exact arithmetic,
$$E_{0.70}(0.75)=\tfrac{47}{100}<\tfrac12,\qquad E_{0.75}(0.80)=\tfrac{9971}{19995}<\tfrac{8}{15},\qquad E_{0.80}(0.85)=\tfrac{439}{832}<\tfrac{451}{800},\qquad E_{0.85}(0.90)=\tfrac{378}{683}<\tfrac{237}{400},$$
and $D^*(\lambda_k)<g(\lambda_k)$ is read off Theorem 1.2(a) ($g(\lambda_k)=7/15,\ 1/2,\ 8/15,\ 451/800$ for $k=0,\dots,3$). On $[0.90,1)$ one has $2\mu/3\ge3/5$, so $g(\mu)=\min\{(23\mu+3)/40,3/5\}$. All slopes of $E_{0.90}$ are at most $1$, so $E_{0.90}(\mu)\le71/130+(\mu-9/10)$, which is smaller than $(23\mu+3)/40$ for $\mu<223/221$; this covers $\mu\in[0.90,21/23]$, where $g(\mu)=(23\mu+3)/40$, and for $\mu\in[21/23,1)$ one has $g(\mu)=3/5>5588/9417=E_1(1)\ge E_1(\mu)\ge\beta(\mu)$, since the slopes of $E_1$ are non-negative. On $[1,1.10]$, $\beta=E_1$ is convex and $g(\mu)=(23\mu+3)/40$ is affine, so it suffices that $E_1(1)=5588/9417<13/20$ and $E_1(11/10)=6239/9170<283/400$.

The same computation bounds the gap. On $[21/23,1)$ it gives $g-\beta\ge3/5-5588/9417=311/47085$. On each $[\lambda_k,\lambda_{k+1}]$ the function $g-E_{\lambda_k}$ is concave, so the gap is at least the smaller of its two endpoint values, and the exact values above give at least $1/2-47/100=3/100$; on $[0.90,21/23]$ the affine majorant gives $g-\beta\ge3/5-71/130-(21/23-9/10)=61/1495$. Both exceed $311/47085$. Since $\beta$ is continuous with $\beta(1)=E_1(1)=5588/9417$, the infimum of $g-\beta$ on $[0.70,1)$ is exactly $311/47085$, approached as $\mu\to1^-$. As an independent check, the fifth command of Section 5 evaluates $g-\beta$ in exact arithmetic at every breakpoint of $\beta$ and of $g$ in $[0.70,1.10]$ (both functions are piecewise affine, so this covers the interval) and at the left limit $\mu\to1^-$, and reports the smallest value $311/47085$. $\square$

## 7. Limits of the method

The point
$$a_\bullet=b_\bullet=\tfrac1{359}(30,0,43,43,0,0),\quad \alpha_a=\alpha_b=\tfrac{120}{359},\qquad c_\bullet=\tfrac1{359}(0,43,43,29,0,0),\quad \alpha_c=\tfrac{119}{359},\qquad D=\tfrac{213}{359},$$
(so that each letter has a tail $\alpha_s-\sum_{i\le6}\alpha_{s,i}=4/359$ and $L=1$) satisfies $\mathcal R(1)$ with equality in the Fourier row, all $2^{18}$ constraints (B4) (the smallest right-hand side, $213/359$, is attained for instance at $I_a=I_b=\{1,3\}$, $I_c=\emptyset$), all $4{,}158$ instances of $(\star\star)$ with the refinement of Proposition 4.1 (the smallest right-hand side is again $213/359$, attained for instance at $A=b$, $p_A=(3,4)$, $B=c$, $I_B=\{2,3\}$), all $811{,}008$ instances of the frozen-modulus generalization of Appendix A, and also the Thue-equation and determinant-method constraints of the first arXiv version of [1] (smallest right-hand sides $244/359$ and $1135/1436$). The first verifier of Section 5 checks this in rational arithmetic. Hence the constraints used here cannot give an exponent below $213/359=0.593314\ldots$ at $\lambda=1$; the gap to the bound $5588/9417$ of Proposition 5.1 is $271/3380703<10^{-4}$.

The letters of this point are carried by the index sets $\{1,3,4\}$, $\{1,3,4\}$ and $\{2,3,4\}$, and the family $(\star\star)$ holds there with equality. Adding further instances of the same family therefore cannot lower the value, and an exponent below $213/359$ requires a new arithmetic input adapted to such asymmetric carriers. On the symmetric subspace $a_i=b_i=c_i$ the situation is different and is described in Appendix A.

## 8. Relation to other work

- [1] (arXiv:2410.12234, version 2) merges an earlier article of Browning, Lichtman and Teräväinen, which used additionally the determinant method and Thue equations, with the improvement and simplification by Bernert [5]; it proves the exponent $(23\lambda+3)/40$ for $\lambda\le2$ and the exponent $3/5$ for $\lambda<1$. Our argument uses its Propositions 2.1, 2.3, 3.1 and 4.1 unchanged and adds Proposition 4.1 above. The linear program of [1, Proposition 6.1] has value exactly $3/5$ at budget $1$: it is bounded by $3/5$ by that proposition, and the point $a_\bullet=b_\bullet=\frac1{10}(0,1,1,0,1,0)$, $\alpha_a=\alpha_b=3/10$, $c_\bullet=\frac1{10}(0,2,2,0,0,0)$, $\alpha_c=2/5$, $D=3/5$ satisfies $\mathcal R(1)$ (with equality in the Fourier row) and all $2^{18}$ constraints (B4), the smallest right-hand side being exactly $3/5$; the first verifier of Section 5 checks this in rational arithmetic. The same point violates the $24$ constraints $(\star)$ and the instances of $(\star\star)$, which cut it to $11/20$. Hence at budget $1$ the improvement comes entirely from the collision inequalities, while at budgets $\lambda<1$ most of the improvement in Theorem 1.2 comes from the program of [1] itself, as explained in Section 1.
- [2] introduced the inequality $(\star)$ and proved the exponent $59969/100033$ for $0<\lambda\le1$ by a tree with $777$ leaves. The present paper generalizes $(\star)$ to $(\star\star)$, replaces that tree by the tree of Proposition 5.1, and adds the dependence on the budget (Theorem 1.2, Corollary 1.3), which [2] did not consider. Section 1 lists what is inherited.
- Bernert [5] (arXiv:2506.13364) obtained the exponent $0.65$ before the merged version of [1]. Runbo Li [6] (arXiv:2507.02885) obtained $56/85\approx0.6588$, also before the merged version.
- Browning and Verzobio [7] (arXiv:2608.24512) treat sums of three powerful numbers and $(p,q,r)$-full triples, a restricted subfamily; their results do not bound the general set counted by $N_\lambda$.
- To our knowledge (searches of arXiv and of the forward citations of [1] carried out while preparing [2] and this work), no bound below $0.6$ for the general count $N_\lambda(X)$ other than [2] has appeared, and no bound below $\min\{(23\lambda+3)/40,2\lambda/3\}$ for $\lambda\ge1$. [1] itself states that the authors know of no general estimate for $N_\lambda(X)$, $\lambda<1$, beyond theirs and the trivial bound.
- The ingredients of Section 3 are standard: [3, Lemma 3.5] for quadratic equations, and the basic algebraic number theory of [4] as used in [2]. The new features relative to [2] are the Bézout parametrization of $g^j=h^k$ in any finite abelian group for coprime $(j,k)$ (Lemma 3.2), the free sets $I_B$ of arbitrary size with the one-sided difference bounds for the pairs containing $5$, and the parametric use of the Farkas multipliers (Lemma 5.3).

## 9. Remarks

- The improvement at $\lambda=1$ is numerically small: $3/5-54/91=3/455\approx6.6\cdot10^{-3}$. The bound $5588/9417$ is not shown to be the value of the program with the family $(\star\star)$; Section 7 shows that this value is at least $213/359$.
- The values of Theorem 1.2 are the exact optima of the programs with the family $(\star)$; the family $(\star\star)$ was run only at budget $1$. Running it at the other budgets may lower the values where $(\star)$ contributes; this was not computed.
- The argument does not use the determinant method or Thue equations; whether they combine with $(\star\star)$ to give further improvement is not examined here.

## Appendix A. A frozen modulus on the third letter, and the symmetric subspace

In addition to the data of Section 4, choose a distinguished index $k_B\in I_B$ and a set $O_C\subseteq\{1,\dots,6\}$ of frozen indices of $C$ (possibly empty), and put
$$f_C=\sum_{i\in O_C}\alpha_{C,i},\qquad w_C=\sum_{i\in O_C}i\,\alpha_{C,i},\qquad \tilde\delta=\sum_{\substack{i\in I_B\\ i\ne k_B}}\alpha_{B,i}+(\alpha_{B,k_B}-w_C)_+ .$$
For $O_C=\emptyset$ one has $f_C=w_C=0$ and $\tilde\delta=\delta$.

**Proposition A.1.** In the setting of Proposition 2.1, every box satisfies, up to additive $o(1)$ as $X\to\infty$ (for fixed $d$),
$$D\le f_A+f_B+f_C+\max\Big(\alpha_C-f_C,\ \tfrac12\big(\alpha_C-f_C+\tilde\delta+\kappa(p,q;w_B)\big)\Big).$$
If $O_C=\emptyset$ and $I_B$ is one of the five pairs of Proposition 4.1, $\tilde\delta$ may be replaced by $\min(\tilde\delta,\delta')$.

For $O_C=\emptyset$ this is Proposition 4.1. There are $6\cdot11\cdot192\cdot64=811{,}008$ instances (six ordered letter pairs, eleven pairs $p_A$, $\sum_{\emptyset\ne I_B}|I_B|=192$ choices of $(I_B,k_B)$, $64$ sets $O_C$). The instances with $O_C\ne\emptyset$ are not used in the trees of Section 5; they are proved here because the feasible point of Section 7 is tested against them, and because they are effective on the symmetric subspace, as shown below.

*Proof.* Keep the notation of the proof of Proposition 4.1, but split the letter $C$ as $w=w_{\rm free}\,M_C$ with
$$M_C=z''_0\prod_{i\in O_C}z_i''^{\,i},\qquad w_{\rm free}=\prod_{i\notin O_C}z_i''^{\,i},$$
the second product running over all $i\le d$ outside $O_C$. The equation reads $\pm M_Au\pm M_Bv=\pm M_Cw_{\rm free}$.

Step (a) is unchanged except that the coordinates entering $M_C$ are frozen as well, in $\ll\prod_{i\in O_C}C_i=X^{f_C+o(1)}$ further ways, that $\log_XM_C\ge w_C$ since each coordinate is at least its dyadic parameter and $z''_0\ge1$, and that $w_{\rm free}$ ranges over a set $\mathcal W$ with $|\mathcal W|\le X^{\alpha_C-f_C+o(1)}$. In step (b), pairwise coprimality gives in addition $\gcd(M_Bv,M_Cw_{\rm free})=1$: if $\gcd(M_B,M_C)>1$ the fibre is empty, and otherwise $M_B$ is invertible modulo $M_C$ and all coordinates of $v$ are units modulo $M_C$. Step (c) is unchanged.

*(d′) The lock modulo $M_C$.* Fix $(u,u')$. Reducing the equation modulo $M_C$ gives $v\equiv\mp M_B^{-1}M_Au\pmod{M_C}$: the residue of $v$ modulo $M_C$ is determined by $u$ and the frozen data. Write $v=\prod_{i\in I_B}z_i'^{\,i}$ and fix the coordinates $z'_i$, $i\in I_B\setminus\{k_B\}$, in $\ll X^{\sum_{i\in I_B,i\ne k_B}\alpha_{B,i}}$ ways. Then $z_{k_B}'^{\,k_B}\equiv\gamma\pmod{M_C}$ for a unit $\gamma$ determined by the fixed data. In any finite abelian group the solutions of $z^{k}=\gamma$ form a coset of $\{z^{k}=1\}$, so $z'_{k_B}$ lies in at most $\rho_{k_B}(M_C)\ll X^{o(1)}$ residue classes modulo $M_C$ (the bound $\rho_e(M)\le e^{2\omega(M)}$ from the proof of Lemma 3.2 is proved prime power by prime power and does not require $M_C$ to be squarefree). Each class contains at most $1+X^{\alpha_{B,k_B}}/M_C\le1+X^{\alpha_{B,k_B}-w_C}$ integers of the dyadic interval of $z'_{k_B}$, and this bound is non-increasing in $M_C$, so the lower bound $M_C\ge X^{w_C}$ suffices. Hence there are $\le X^{\tilde\delta+o(1)}$ values $v$, and $v'$ is determined by $v$. Consequently $E_{\rm off}\le X^{\kappa+\tilde\delta+o(1)}$.

Step (e) applies verbatim when $O_C=\emptyset$ and $I_B$ is a pair of Lemma 3.1; it does not use $k_B$. Step (f) now gives $\alpha_C-f_C$ from $|\mathcal W|$ and the frozen factor $X^{f_A+f_B+f_C+o(1)}$. $\square$

**The symmetric subspace.** On the subspace $a_i=b_i=c_i$ the frozen modulus is effective. The point $a_\bullet=b_\bullet=c_\bullet=\frac1{162}(11,0,24,16,3,0)$, $\alpha_s=1/3$, $D=16/27=0.5926\ldots$, satisfies $\mathcal R(1)$, all constraints (B4) and the $24$ constraints $(\star)$ (smallest right-hand sides $16/27$ and $49/81$), so the family $(\star)$ alone cannot go below $16/27$ on this subspace; the point $\frac1{81}(6,0,12,8,0,0)$, $\alpha_s=1/3$, $D=16/27$ does the same for all instances of $(\star\star)$; and the point $\frac1{48}(3,0,7,6,0,0)$, $\alpha_s=1/3$, $D=7/12$ satisfies all $811{,}008$ instances of Proposition A.1, so the full family cannot go below $7/12$ there. The first verifier of Section 5 checks these three points, each against $\mathcal R(1)$, all constraints (B4) and the family named for it. Thus the lock modulo the third letter lowers the symmetric ceiling from $16/27$ to $7/12$, but it is inactive at the asymmetric point of Section 7, where the family $(\star\star)$ already holds with equality.

## Data availability

The supplement contains the six branch-and-bound trees of Propositions 5.1 and 5.2, the five trees for the program without $(\star)$, the two independent verifiers, the script printing the parametric values of Section 6, the generators that produced the trees, a list of SHA-256 hashes of all files, and instructions for running the verifiers as in Section 5.

## References

[1] C. Bernert, T. Browning, J. D. Lichtman, J. Teräväinen, *Bounds on the exceptional set in the abc conjecture*, arXiv:2410.12234v2 (9 May 2026).

[2] H. Li, *Breaking the three-fifths barrier for the exceptional set in the abc conjecture*, rStation, problem *math*, paper 6, version 3 (accepted 5 November 2026), https://rstation.ai/problems/math/papers/6/v3; archived at Zenodo, DOI 10.5281/zenodo.24054892 (concept DOI 10.5281/zenodo.24054868).

[3] R. C. Vaughan, T. D. Wooley, *Further improvements in Waring's problem*, Acta Math. 174 (1995), 147–240.

[4] J. S. Milne, *Algebraic Number Theory*, course notes, version 3.08 (2020).

[5] C. Bernert, *The exceptional set in the abc conjecture*, arXiv:2506.13364 (2025).

[6] R. Li, *On the exceptional set in the abc conjecture*, arXiv:2507.02885 (2025).

[7] T. Browning, M. Verzobio, *Sums of three powerful numbers*, arXiv:2608.24512 (2026).

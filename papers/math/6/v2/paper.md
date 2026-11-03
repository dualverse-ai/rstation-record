# Breaking the three-fifths barrier for the exceptional set in the abc conjecture

**Hongmin Li**, Graduate School of Frontier Sciences, The University of Tokyo.

*Disclosure.* The arguments and computations in this manuscript were produced with substantial assistance from AI systems, operated and curated by the author, who is not a specialist in analytic number theory. The proofs have been checked by independent AI-assisted readings and the linear-programming certificate by an independent verifier program, but they have not been reviewed by a human expert. Readers are invited to check every step; the supplement makes the computational part reproducible.

## 1. Problem and contribution

For $\lambda>0$ let
$$N_\lambda(X)=\#\{(a,b,c)\in\mathbb N^3:\ a+b=c\le X,\ \gcd(a,b,c)=1,\ \operatorname{rad}(abc)<c^\lambda\}.$$
The abc conjecture predicts $N_\lambda(X)=O_\lambda(1)$ for every fixed $\lambda<1$. The trivial bound is $N_\lambda(X)\ll X^{2\lambda/3+\varepsilon}$ [1, Proposition 1.1]. Bernert, Browning, Lichtman and Teräväinen [1] obtained the first general estimate beyond the trivial one; their Theorem 1.3 states
$$N_\lambda(X)\ll_{\varepsilon,\lambda}X^{0.6+\varepsilon}\qquad(0<\lambda<1),$$
which improves the trivial bound only when $\lambda>9/10$.
The exponent $3/5$ is the optimum of the linear program of [1, Proposition 6.1], built from an anatomic decomposition of $a,b,c$ into powerful parts [1, Proposition 2.1], the trivial bound [1, Proposition 2.3], a Fourier bound [1, Proposition 3.1] and a geometry-of-numbers bound [1, Proposition 4.1]. The authors remark that a serious numerical improvement is likely to require new ideas.

**Main Theorem.** Let $U=59969/100033=0.59949216\ldots$. For every $0<\lambda\le1$ and every $\varepsilon>0$,
$$N_\lambda(X)\ll_{\lambda,\varepsilon}X^{U+\varepsilon}.$$
In particular $N_\lambda(X)\ll X^{0.5995}$ for all $\lambda\le1$, including the endpoint $\lambda=1$ which is not covered by [1, Theorem 1.3]. Combined with the trivial bound this gives $N_\lambda(X)\ll X^{\min\{2\lambda/3,\,59969/100033\}+\varepsilon}$; the new exponent improves on both previous bounds exactly when $\lambda>3\cdot59969/200066=0.8992\ldots$.

The new input is a *two-letter collision inequality* (Proposition 4.1), proved in Section 4 from two arithmetic lemmas (Section 3):

1. a uniform bound for the number of representations of a nonzero integer $m$ as a difference $x^jy^k-x'^jy'^k$ with $(j,k)\in\{(2,3),(3,4)\}$ and $x,x',y,y'$ in dyadic boxes (Lemma 3.1), proved through ideal counting and a uniform lower bound for units in real quadratic and pure cubic fields;
2. an estimate for the multiplicative energy $x^jy^k\equiv x'^jy'^k\pmod M$ in the unit group, exploiting $k-j=1$ (Lemma 3.2).

Inserting all 24 instances of the collision inequality into the linear program of [1] lowers its value below $3/5$. This is established by a branch-and-bound tree with 777 leaves, each closed by a rational Farkas multiplier (Section 5). The tree and an independent verifier using only rational arithmetic are in the supplement.

**What is claimed.** The Main Theorem, unconditionally, with the computer-verified rational certificate of Section 5 as part of the proof.

**What is not claimed.** We do not claim that $U$ is the value of the enlarged program; we only prove it is an upper bound. The enlarged program has a feasible point with $D=13/22=0.5909\ldots$ (Section 7), so the present constraints cannot yield an exponent below $13/22$. We make no claim towards the abc conjecture itself.

## 2. The framework of Bernert–Browning–Lichtman–Teräväinen

We follow [1] (arXiv version 2, 9 May 2026). Write $x\sim X$ for $x\in(X,2X]$, with the convention that $x\sim1$ means $x\in[1,2]$, so that coordinates equal to $1$ belong to the lowest dyadic block. Let $N^*_\lambda(X)$ count the triples counted by $N_\lambda(X)$ with in addition $c\ge X/2$ and $\operatorname{rad}(abc)\ge c^\lambda/2$. A dyadic decomposition gives [1, §2]
$$N_\lambda(X)\ll(\log X)^2\max_{1\le Y\le X}\max_{\mu\le\lambda}N^*_\mu(Y).\tag{2.1}$$
For $d\in\mathbb N$, $(a_0,b_0,c_0)\in\mathbb N^3$ and dyadic parameters $\mathbf A,\mathbf B,\mathbf C\in\mathbb N^d$, let $B_d(a_0,b_0,c_0,\mathbf A,\mathbf B,\mathbf C)$ be the number of $(a_i,b_i,c_i)_{1\le i\le d}$ with $a_i\sim A_i$, $b_i\sim B_i$, $c_i\sim C_i$,
$$a_0\prod_{i=1}^d a_i^i+b_0\prod_{i=1}^d b_i^i=c_0\prod_{i=1}^d c_i^i,\qquad \gcd\Big(\prod_{i=0}^d a_i,\prod_{i=0}^d b_i,\prod_{i=0}^d c_i\Big)=1 .$$

**Proposition 2.1 ([1, Proposition 2.1]).** For any $\varepsilon_0>0$ there is $d=d(\varepsilon_0)\ge 6$ such that $N^*_\lambda(X)\ll_{\varepsilon_0}X^{\varepsilon_0}\max B_d(a_0,b_0,c_0,\mathbf A,\mathbf B,\mathbf C)$, the maximum over pairwise coprime $1\le a_0,b_0,c_0\le X^{\varepsilon_0}$ and dyadic $A_i,B_i,C_i\in[1,X]$ with
$$2^{-d-1}X^\lambda\le\prod_{j}A_jB_jC_j\le X^{\lambda+3\varepsilon_0/4},\qquad \prod_j A_j^j,\ \prod_j B_j^j\le X,\qquad X^{1-\varepsilon_0/2}\le\prod_jC_j^j\le X.$$

Since $a+b=c$ and $\gcd(a,b,c)=1$, the three numbers $a_0\prod a_i^i$, $b_0\prod b_i^i$, $c_0\prod c_i^i$ are pairwise coprime; this is used in the proof of [1, Proposition 2.1] and will be used again below.

**Exponents.** Fix a box. For $s\in\{a,b,c\}$ write $S_i=X^{\alpha_{s,i}}$ for the dyadic parameters of the letter $s$, $\alpha_s=\sum_{i\le d}\alpha_{s,i}$, $L=\alpha_a+\alpha_b+\alpha_c$, and let $D$ be defined by $B_d=X^D$. Then $L\le\lambda+O(\varepsilon_0)$ and $\sum_{i\le d}i\,\alpha_{s,i}\le1$. With the abbreviations $a_i=\alpha_{a,i}$, $a=\alpha_a$ and so on, [1, Propositions 2.3, 3.1, 4.1] give, up to additive errors $O(\varepsilon_0)$ and $o(1)$ as $X\to\infty$:

- (B1) $L\le1$ (when $\lambda\le1$, up to $O(\varepsilon_0)$); $\sum_{i\le6}s_i\le s$; $7s-\sum_{i\le6}(7-i)s_i\le1$ for $s\in\{a,b,c\}$ (these are (6.1)–(6.3) of [1]; the last follows from the full height budget $\sum_{i\le d}is_i\le1$ since $i\ge7$ for $i>6$);
- (B2) $D\le\min(a+b,a+c,b+c)$ ([1, Proposition 2.3], (6.4));
- (B3) with $F_s=\max(s_2+s_4+s_6,\ s_3+s_6,\ s_5)$: $F_a+F_b+F_c\le4L-6D$ ([1, Proposition 3.1] with $j,k,\ell\in\{2,3,5\}$, i.e. (6.10));
- (B4) for any $I_a,I_b,I_c\subseteq\{1,\dots,6\}$, with $\Sigma_0=\sum_s\sum_{i\in I_s}s_i$ and $\Sigma_1=\sum_s\sum_{i\in I_s}(i-1)s_i$:
$$D\le\max\big(L-\Sigma_0,\ L-1+\Sigma_1\big)\qquad([1,\ \text{Proposition }4.1]).$$

In (B3) and (B4) we use $L$ in place of $\lambda$. This is what the proofs give: the proof of [1, Proposition 3.1] bounds $B_d$ by $(ABC)^{2/3}$ divided by the sixth root of the three products of powerful coordinates, and the proof of [1, Proposition 4.1] produces $ABC/\prod\cdots$ and $X^{-1+3\varepsilon_0}ABC\prod\cdots$ before $ABC$ is replaced by $X^{\lambda+3\varepsilon_0}$; here $A=\prod A_i$, etc. [1, Proposition 6.1] states that (B1)–(B4) (with thirteen specific choices in (B4), namely (6.5)–(6.9)) imply $D\le 3/5$, and this is how [1, Theorem 1.3] is deduced.

## 3. Two arithmetic lemmas

Throughout, $(j,k)\in\{(2,3),(3,4)\}$, and for $P,Q\ge1$
$$S_{j,k}(P,Q)=\{x^jy^k:\ x\sim P,\ y\sim Q\}$$
is a set of *values*. By the divisor bound each value has $(PQ)^{o(1)}$ representations $x^jy^k$ with $x\sim P$, $y\sim Q$, since $x$ and $y$ divide it.

### 3.1 Differences

**Lemma 3.1.** For $m\ne0$ let $r_{j,k}(m)=\#\{(u,u')\in S_{j,k}(P,Q)^2:\ u-u'=m\}$. Then for every $\eta>0$
$$r_{j,k}(m)\ll_\eta(PQ|m|)^\eta\min(PQ,P^2,Q^2).$$

The bound $PQ$ is the size of the value set. Fixing the pair $(y,y')$ in $O(Q^2)$ ways, or the pair $(x,x')$ in $O(P^2)$ ways, reduces the remaining count to an equation
$$\mathsf aU^e-\mathsf bV^e=m\ne0,\qquad \mathsf a,\mathsf b\ge1,\ e\in\{2,3\},\tag{3.1}$$
in positive integers $U,V$, as follows:

| monomial | fixed | remaining equation | $e$ |
| --- | --- | --- | --- |
| $x^2y^3$ | $y,y'$ | $y^3x^2-y'^3x'^2=m$ | 2 |
| $x^2y^3$ | $x,x'$ | $x^2y^3-x'^2y'^3=m$ | 3 |
| $x^3y^4$ | $x,x'$ | $x^3Y^2-x'^3Y'^2=m$, $Y=y^2$ | 2 |
| $x^3y^4$ | $y,y'$ | $y^4x^3-y'^4x'^3=m$ | 3 |

(Restricting $Y$ to squares only shrinks the solution set.) In every case all of $\mathsf a,\mathsf b,U,V,|m|$ are at most $\mathcal B^{O(1)}$ with $\mathcal B=2+PQ|m|$. Hence Lemma 3.1 follows from:

**Lemma 3.1′.** The number of positive solutions $(U,V)$ of (3.1) with $\mathsf a,\mathsf b,U,V,|m|\le\mathcal B^{C}$ is $O_{C,\eta}(\mathcal B^\eta)$, uniformly in $\mathsf a,\mathsf b,m$. No coprimality of $U,V$ or of $\mathsf a,\mathsf b$ is assumed.

*Proof.* For $e=2$ this is also a direct consequence of [2, Lemma 3.5] applied to $(\mathsf aU)^2-\mathsf a\mathsf bV^2=\mathsf am$. We give a uniform argument for $e=2,3$. Let $\theta>0$ be the real root of $T^e=\mathsf a^{e-1}\mathsf b$.

*Case $\theta\in\mathbb Z$.* Then $(\mathsf aU)^e-(\theta V)^e=\mathsf a^{e-1}m\ne0$. Put $h=\mathsf aU-\theta V$, a nonzero divisor of $\mathsf a^{e-1}m$; there are $\mathcal B^{o(1)}$ choices. If $e=2$, the cofactor $\mathsf aU+\theta V=\mathsf am/h$ is fixed, so $(U,V)$ is determined. If $e=3$, the cofactor $3(\theta V)^2+3h\theta V+h^2=\mathsf a^2m/h$ is fixed, a quadratic equation in $V$ with at most two roots, and $U$ follows. This case contains degenerate situations such as $y=y'$ in the last row of the table, where the binary cubic form $y^4(x^3-x'^3)$ is reducible although its discriminant is nonzero.

*Case $\theta\notin\mathbb Z$.* Since $e$ is prime and a rational root of the monic polynomial $T^e-\mathsf a^{e-1}\mathsf b$ would be an integer, this polynomial is irreducible and $K=\mathbb Q(\theta)$ has degree $e$. For $e=2$, $K$ is real quadratic; for $e=3$, $T^3-\mathsf a^2\mathsf b$ has exactly one real root, so $K$ has signature $(1,1)$. In both cases the unit group $\mathcal O_K^\times$ has rank one [3, Theorem 5.1] and torsion $\{\pm1\}$. Put
$$\alpha=\mathsf aU-\theta V\in\mathcal O_K,\qquad N_{K/\mathbb Q}(\alpha)=\mathsf a^{e-1}(\mathsf aU^e-\mathsf bV^e)=\mathsf a^{e-1}m\ne0.$$
The map $(U,V)\mapsto\alpha$ is injective because $1,\theta$ are linearly independent over $\mathbb Q$.

(i) *Ideals.* We work in the maximal order $\mathcal O_K$, a Dedekind domain [3, Theorems 3.29, 3.7]. If $p^t\Vert n$, then $p\mathcal O_K$ has at most $e$ prime factors [3, Theorem 3.34], and the number of ideals of norm $p^t$ is at most the number of ways of writing $t=\sum_i f_ik_i$ with at most $e$ terms, which is at most $(t+1)^e$. Since the ideal norm is multiplicative and compatible with element norms [3, Propositions 4.1, 4.2], the number of principal ideals $(\alpha)$ with $|N(\alpha)|=n:=|\mathsf a^{e-1}m|$ is at most $\tau(n)^e\ll_\eta\mathcal B^{\eta}$. Ramified primes are included in this count, and no class-number information is needed.

(ii) *Size of embeddings.* Every embedding $\sigma$ satisfies $|\sigma(\alpha)|\le\mathcal B^{O(1)}$. Since $\prod_\sigma|\sigma(\alpha)|=|N(\alpha)|\ge1$, also $|\sigma(\alpha)|\ge\mathcal B^{-O(1)}$ for every $\sigma$.

(iii) *Generators of one ideal.* If $\alpha,\beta$ generate the same ideal, $\varepsilon=\alpha/\beta$ is a unit with $\mathcal B^{-O(1)}\le|\sigma(\varepsilon)|\le\mathcal B^{O(1)}$ for every $\sigma$. Write $\varepsilon=\pm u^n$, where $u$ is a fundamental unit chosen with real embedding $u>1$ (for $e=3$ we take the real embedding). We claim $u\ge5/4$ uniformly in $K$. For $e=2$ the conjugate of $u$ is $\pm u^{-1}$ and $u\pm u^{-1}\in\mathbb Z$, which forces $u\ge(1+\sqrt5)/2$. For $e=3$, the two complex conjugates $u_2,u_3$ of $u$ satisfy $|u_2|=|u_3|=u^{-1/2}<1$; the minimal polynomial $f$ of $u$ is monic with integer coefficients and $f(1)\ne0$ (as $u\ne1$), so
$$1\le|f(1)|=(u-1)\,|1-u_2|\,|1-u_3|\le4(u-1),$$
whence $u\ge5/4$. Consequently $|n|\log(5/4)\le|n\log u|=|\log|\varepsilon||\ll\log\mathcal B$, so each principal ideal has $O(\log\mathcal B)$ generators in the admissible range, with an absolute implied constant.

Combining (i)–(iii), (3.1) has $\ll\tau(n)^e\log\mathcal B\ll_\eta\mathcal B^\eta$ solutions. $\square$

### 3.2 Congruence energy in the unit group

**Lemma 3.2.** For an integer $M\ge1$ let $K_{j,k}(P,Q;M)$ be the number of $(x,y,x',y')$ with $x,x'\sim P$, $y,y'\sim Q$, $\gcd(xyx'y',M)=1$ and $x^jy^k\equiv x'^jy'^k\pmod M$. Then
$$K_{j,k}(P,Q;M)\ll_\eta(PQM)^\eta\,PQ\,\sqrt{(1+P^2/M)(1+Q^2/M)}.$$

*Proof.* Let $G=(\mathbb Z/M\mathbb Z)^\times$, $g=x/x'$ and $h=y'/y$ in $G$. The congruence is $g^j=h^k$. Since $k-j=1$, the map $z\mapsto(z^k,z^j)$ is a bijection from $G$ onto $\{(g,h)\in G^2:g^j=h^k\}$ with inverse $(g,h)\mapsto g/h$: indeed if $g^j=h^k$ and $z=g/h$, then $z^j=g^jh^{-j}=h^{k-j}=h$ and $z^k=z^jz=g$. For $N\ge1$ and $v\in G$ let $R_N(v)$ be the number of $(s,t)$ with $s,t\sim N$, $\gcd(st,M)=1$ and $s/t=v$ in $G$. Then
$$K_{j,k}(P,Q;M)=\sum_{z\in G}R_P(z^k)\,R_Q(z^j).$$
Let $\rho_e(M)=\#\{v\in G:v^e=1\}$. For $e\le4$, $\rho_e(p^r)\le e$ for odd $p$ (cyclic group) and $\rho_e(2^r)\le e^2$ (at most two cyclic factors), so $\rho_e(M)\le 16^{\omega(M)}\ll_\eta M^\eta$. Each fibre of $z\mapsto z^e$ has at most $\rho_e(M)$ elements; Cauchy–Schwarz gives
$$K_{j,k}^2\le\rho_k(M)\rho_j(M)\,\mathcal M_P\,\mathcal M_Q,\qquad \mathcal M_N=\sum_{v\in G}R_N(v)^2 .$$
Now $\mathcal M_N$ counts $(s,t,s',t')$ with all entries $\sim N$, coprime to $M$, and $st'\equiv s't\pmod M$. Fix $(s,t')$, hence $n=st'\le4N^2$. The product $s't\le4N^2$ lies in the residue class of $n$ modulo $M$, so it takes $O(1+N^2/M)$ values, each with $N^{o(1)}$ factorizations. Thus $\mathcal M_N\ll_\eta N^{2+\eta}(1+N^2/M)$, and the lemma follows. $\square$

If $P=X^p$, $Q=X^q$ and $M\ge X^{w}$ with $M\le X^{O(1)}$, the bound is $X^{\kappa+o(1)}$ with
$$\kappa(p,q;w)=p+q+\tfrac12\big((2p-w)_++(2q-w)_+\big),$$
and since the right-hand side of Lemma 3.2 is non-increasing in $M$ apart from the factor $M^\eta$, only a lower bound for $M$ is needed.

## 4. The two-letter collision inequality

Fix an ordered pair of distinct letters $(A,B)$ from $\{a,b,c\}$, let $C$ be the third letter, and choose $p_A=(j_A,k_A)$ and $p_B=(j_B,k_B)$ in $\{(2,3),(3,4)\}$. Put
$$p=\alpha_{A,j_A},\ q=\alpha_{A,k_A},\ r=\alpha_{B,j_B},\ s=\alpha_{B,k_B},\qquad f_{\rm out}=(\alpha_A-p-q)+(\alpha_B-r-s),$$
$$w_B=\sum_{\substack{i\le6\\ i\notin\{j_B,k_B\}}}i\,\alpha_{B,i}+7\Big(\alpha_B-\sum_{i\le6}\alpha_{B,i}\Big).$$

**Proposition 4.1.** In the setting of Proposition 2.1, every box satisfies, up to additive $o(1)$ as $X\to\infty$ (for fixed $d$),
$$D\le f_{\rm out}+\max\Big(\alpha_C,\ \tfrac12\big(\alpha_C+\min(r+s,2r,2s)+\kappa(p,q;w_B)\big)\Big).\tag{\star}$$

*Proof.* The equation of $B_d$ reads $\pm M_Au\pm M_Bv=\pm\gamma$ for a suitable arrangement of signs, where
$$u=z_{j_A}^{\,j_A}z_{k_A}^{\,k_A},\qquad M_A=z_0\prod_{i\notin\{j_A,k_A\}}z_i^{\,i},$$
where $(z_i)_{1\le i\le d}$ are the coordinates of the letter $A$ and $z_0\in\{a_0,b_0,c_0\}$ is its fixed small coefficient; $M_B$ and $v$ are defined in the same way for $B$ with the pair $p_B$, and $\gamma$ is the value of the letter $C$. The products defining $M_A,M_B$ run over *all* indices $1\le i\le d$ outside the chosen pair, including all $i\ge7$.

*Freezing.* The coordinates entering $M_A$ and $M_B$ can be chosen in $\ll\prod_{i\notin p_A}A_i\prod_{i\notin p_B}B_i=X^{f_{\rm out}+o(1)}$ ways (here $A_i,B_i$ denote the dyadic parameters of the two letters). Fix them. Since each coordinate exceeds its dyadic parameter,
$$\log_X M_B\ge\sum_{\substack{i\le6\\ i\notin p_B}}i\,\alpha_{B,i}+\sum_{i\ge7}i\,\alpha_{B,i}\ge w_B ,$$
because $\sum_{i\ge7}i\alpha_{B,i}\ge7\sum_{i\ge7}\alpha_{B,i}=7(\alpha_B-\sum_{i\le6}\alpha_{B,i})$; the small coefficient of $B$ is at least $1$ and only increases $M_B$. Thus $w_B$ is a lower bound for the size of the modulus, which is what Lemma 3.2 requires. All quantities are $\le X^{O(1)}$.

*Coprimality.* By the pairwise coprimality recalled after Proposition 2.1, $\gcd(M_Au,M_Bv)=1$ for every counted solution. If $\gcd(M_A,M_B)>1$ the fibre is empty; otherwise $\gcd(M_A,M_B)=1$ and $\gcd(u,M_B)=1$, so all coordinates $x,y$ of $u$ are units modulo $M_B$. No coprimality between coordinates of the same letter, and none between different solutions, is assumed.

*Counting by values.* By the divisor bound, each value $u$ (resp. $v$, $\gamma$) has $X^{o(1)}$ representations by coordinates; we therefore count pairs of values $(u,v)$ for which there is a primitive solution, and multiply by $X^{o(1)}$ at the end. The value $\gamma$ ranges over a set $\mathcal C$ with $|\mathcal C|\le X^{\alpha_C+o(1)}$, the number of coordinate choices for $C$ (the coefficient of $C$ is fixed). For $\gamma\in\mathcal C$ let $n_\gamma$ be the number of such pairs $(u,v)$ and $N=\sum_\gamma n_\gamma$. By Cauchy–Schwarz,
$$N^2\le|\mathcal C|\sum_\gamma n_\gamma^2=|\mathcal C|\,(N+E_{\rm off}),\qquad N\ll|\mathcal C|+\sqrt{|\mathcal C|\,E_{\rm off}},$$
where $E_{\rm off}$ is the number of ordered pairs of distinct pairs $(u,v)\ne(u',v')$, each coming from a primitive solution, with the same $\gamma$.

*Off-diagonal pairs.* For such a pair, $M_A(u-u')=\mp M_B(v-v')$. If $u=u'$ then $v=v'$ since $M_B>0$; hence $u\ne u'$ and $v\ne v'$. As $\gcd(M_A,M_B)=1$, we get $u\equiv u'\pmod{M_B}$, with $\gcd(uu',M_B)=1$. Lifting to coordinates, the number of such $(u,u')$ is at most $K_{j_A,k_A}(X^p,X^q;M_B)\le X^{\kappa(p,q;w_B)+o(1)}$ by Lemma 3.2. For each such $(u,u')$ the shift $m=\mp M_A(u-u')/M_B$ is a fixed nonzero integer of size $X^{O(1)}$, and by Lemma 3.1 the number of $(v,v')$ with $v-v'=m$ is $\le X^{\min(r+s,2r,2s)+o(1)}$. Hence $E_{\rm off}\le X^{\kappa+\min(r+s,2r,2s)+o(1)}$.

Multiplying $N$ by the $X^{f_{\rm out}+o(1)}$ frozen choices and taking logarithms gives ($\star$). The signs in the equation play no role, since Lemma 3.1 allows $m$ of either sign. $\square$

The implied constants depend on $d$, $\varepsilon_0$ and the divisor-bound parameter, but not on the frozen coefficients; this uniformity is needed when maximizing over boxes. Since $r+s\ge2\min(r,s)$, $\min(r+s,2r,2s)=2\min(r,s)$.

## 5. The enlarged disjunctive program and its certificate

Because (B4) and ($\star$) are disjunctions of linear inequalities, the enlarged program is a disjunctive (mixed-integer) linear program; we reserve the term *linear program* for each branch.

**Variables and constraints.** We use 25 non-negative variables: $s_1,\dots,s_6,s$ for $s\in\{a,b,c\}$, $F_a,F_b,F_c$ and $D$. The root system consists of (B1)–(B3) written linearly ($F_s\ge s_2+s_4+s_6$, $F_s\ge s_3+s_6$, $F_s\ge s_5$, $F_a+F_b+F_c\le4L-6D$), 20 inequalities in all, together with the ordering
$$a_4+2a_5\ \ge\ b_4+2b_5\ \ge\ c_4+2c_5 .\tag{5.1}$$
The full family of constraints (B1)–(B4) and ($\star$) is invariant under relabelling the three letters (each constraint depends only on the exponents of the boxes, not on which letter is the sum), so any feasible point can be relabelled into the closed region (5.1).

**Disjunctions.** A constraint (B4) for a choice $(I_a,I_b,I_c)$ is a disjunction of two linear inequalities. Write $f=f_{\rm out}$, $t_1=2p-w_B$, $t_2=2q-w_B$. Then ($\star$) is equivalent to the disjunction of five linear systems: $D\le f+\alpha_C$; or, for one of the four closed sign quadrants $\sigma_1t_1\ge0$ or $\le 0$ and $\sigma_2 t_2\ge0$ or $\le0$, with $\kappa$ replaced by the corresponding linear expression $p+q+\frac12(\sigma_1t_1+\sigma_2t_2)$ ($\sigma_i\in\{0,1\}$ indicating the positive side),
$$D\le f+\tfrac12(\alpha_C+2r+\kappa),\qquad D\le f+\tfrac12(\alpha_C+2s+\kappa).$$
Every feasible point satisfies at least one branch of each disjunction; the quadrants may overlap on their boundaries.

**Proposition 5.1.** Every point of $\mathbb R_{\ge0}^{25}$ satisfying (B1)–(B3), (5.1), all constraints (B4) and all 24 constraints ($\star$) has $D\le U=59969/100033$.

*Proof (computer-assisted).* The supplement contains a branch-and-bound tree. Each internal node either branches on one constraint (B4) (two children, 520 such nodes) or on one constraint ($\star$) (five children as above, 64 such nodes); all children are present, so the leaves cover every feasible point. There are 777 leaves and the depth is at most 22. A leaf carries the linear system $A_\ell x\le b_\ell$ formed by the root rows and the branch rows on its path, together with a vector $y_\ell$ of non-negative rationals such that
$$(y_\ell^{T}A_\ell)_D=1,\qquad (y_\ell^{T}A_\ell)_v\ge0\ \ (v\ne D),\qquad y_\ell^{T}b_\ell\le U .$$
For $x\ge0$ satisfying the leaf system, $D\le y_\ell^TA_\ell x\le y_\ell^Tb_\ell\le U$. Omitting other valid constraints at a leaf only enlarges its region, so this is sufficient. The verifier rebuilds every row from the formulas above, checks that the node labels are legal (subsets of $\{1,\dots,6\}$, letters and pairs in range), that all children are present, and checks the three conditions at every leaf in exact rational arithmetic; no floating-point solver is involved. The largest leaf bound equals $U$, and
$$\tfrac35-U=\tfrac{254}{500165}>0 .\qquad\square$$

**Reproduction.** From the unpacked supplement:

```
python3 verify_certificate.py
```

(standard library only, Python 3.9 or later). An optional second mode,

```
python3 verify_certificate.py --compare-models
```

(requires `pulp`; no solver is called) compares, coefficient by coefficient, the rows generated by the verifier with those produced by the mixed-integer models `lp.py` (the program of [1, Proposition 6.1]) and `lp_flagship.py` (with the 24 constraints ($\star$) added), which were used to discover the tree.

## 6. Proof of the Main Theorem

Fix $0<\lambda\le1$ and suppose the Main Theorem fails for some $\varepsilon>0$. By (2.1) there are $Y\to\infty$ and $\mu\le\lambda$ with $N^*_\mu(Y)\ge Y^{U+\varepsilon/2}$; fix $D_0\in(U,U+\varepsilon/2)$. Let $\varepsilon_0=1/n$, $n\to\infty$. For each $n$, Proposition 2.1 (with $X$ replaced by $Y$ and $\lambda$ by $\mu$) gives, for arbitrarily large $Y$, a box with $B_d\ge Y^{U+\varepsilon/2-1/n-o(1)}\ge Y^{D_0}$ once $n$ is large, where $d=d(1/n)$. For each $n$ choose $Y=Y_n$ so large that all $o(1)$ terms in (B1)–(B4) and ($\star$) are at most $1/n$; this is possible because, for fixed $d$, there are finitely many constraints (all $(I_a,I_b,I_c)$ with $I_s\subseteq\{1,\dots,6\}$ and the 24 instances of ($\star$)), each holding up to $o(1)$ uniformly over boxes.

Record the vector $\xi_n=(\alpha_{s,i})_{s\in\{a,b,c\},\,i\le6}\cup(\alpha_a,\alpha_b,\alpha_c)$ and $D_n\ge D_0$. Only these $21$ coordinates enter (B1)–(B4) and ($\star$) — the tail $i\ge7$ enters only through $\alpha_s-\sum_{i\le6}\alpha_{s,i}$ — so the dimension does not depend on $d$. The vectors lie in a compact set ($0\le\alpha_{s,i}\le1$, $\alpha_s\le1$, $D_n\le2$), so a subsequence converges to $(\xi,D_\infty)$ with $D_\infty\ge D_0$. All constraints are closed conditions (finite maxima, minima and positive parts of affine functions), and their errors are $O(1/n)+O(\varepsilon_0)\to0$; in particular $L\le\mu+O(\varepsilon_0)\le1+O(1/n)$ gives $L\le1$ in the limit. Relabelling the letters to satisfy (5.1), the limit point satisfies all hypotheses of Proposition 5.1 with $D_\infty>U$, a contradiction. $\square$

For $\lambda<1$ one may instead argue as in [1, §6], using the room $1-\lambda$ to obtain $L\le1$ for small $\varepsilon_0$. The limiting argument is needed only for the endpoint $\lambda=1$, which is not covered by [1, Theorem 1.3]; it uses no property of $\lambda$ other than $\lambda\le1$.

## 7. Limits of the method

The point
$$a_\bullet=b_\bullet=c_\bullet=\Big(\tfrac1{66},\tfrac4{33},\tfrac4{33},0,\tfrac5{66},0\Big),\qquad a=b=c=\tfrac13,\qquad D=\tfrac{13}{22},$$
satisfies (B1)–(B3), all $2^{18}$ constraints (B4), all 24 constraints ($\star$), and also the Thue-equation and determinant-method constraints of the first arXiv version of [1]; the supplement verifies this in rational arithmetic. Hence the constraints used here cannot give an exponent below $13/22=0.5909\ldots$. Floating-point experiments with the mixed-integer model suggest that the true value of the enlarged program is below $U$, but we only claim the certified bound $U$.

## 8. Relation to other work

- [1] (arXiv:2410.12234, version 2) merges an earlier article of Browning, Lichtman and Teräväinen, which used additionally the determinant method and Thue equations, with the improvement and simplification by Bernert [4]; it proves the exponent $0.6$ for $\lambda<1$. Our argument uses its Propositions 2.1, 2.3, 3.1 and 4.1 unchanged and adds Proposition 4.1 above. The linear program of [1, Proposition 6.1] has value exactly $3/5$; the improvement comes entirely from the new constraint ($\star$).
- Bernert [4] (arXiv:2506.13364) obtained the exponent $0.65$ before the merged version of [1]. Runbo Li [5] (arXiv:2507.02885) obtained $56/85\approx0.6588$, also before the merged version.
- Browning and Verzobio [6] (arXiv:2608.24512) treat sums of three powerful numbers and $(p,q,r)$-full triples, a restricted subfamily; their results do not bound the general set counted by $N_\lambda$.
- To our knowledge (searches of arXiv and forward citations of [1] up to 4 November 2026), no bound below $0.6$ for the general count $N_\lambda(X)$ has appeared. [1] itself states that the authors know of no general estimate for $N_\lambda(X)$, $\lambda<1$, beyond theirs and the trivial bound.
- The ingredients of Section 3 are standard: [2, Lemma 3.5] for quadratic equations, and the basic algebraic number theory of [3]. The new features are the choice of the exponent pairs $(2,3)$ and $(3,4)$, for which $k-j=1$ makes the congruence $g^j=h^k$ parametrizable in any finite abelian group (Lemma 3.2), and the use of the frozen coefficient of one letter as a modulus for the free monomial of the other.

## 9. Limitations

- The improvement is numerically small: $3/5-U=254/500165\approx5.1\cdot10^{-4}$. The certified bound $U$ is not claimed to be optimal for the enlarged program, and Section 7 shows that these constraints cannot go below $13/22$.
- Part of the proof (Proposition 5.1) is a computer-verified finite certificate. Its correctness rests on the verifier in the supplement, which uses only rational arithmetic and the standard library and can be inspected independently of the programs that found the tree.
- Lemma 3.1′ needs uniformity in the number field $K=\mathbb Q(\theta)$; it is obtained from the absolute lower bounds $u\ge(1+\sqrt5)/2$ and $u\ge5/4$ for fundamental units, and no bound for regulators or class numbers is used. Readers should check this step in particular.
- The argument does not use the determinant method or Thue equations; whether they combine with ($\star$) to give further improvement is not examined here.

## References

[1] C. Bernert, T. Browning, J. D. Lichtman, J. Teräväinen, *Bounds on the exceptional set in the abc conjecture*, arXiv:2410.12234v2 (9 May 2026).

[2] R. C. Vaughan, T. D. Wooley, *Further improvements in Waring's problem*, Acta Math. 174 (1995), 147–240.

[3] J. S. Milne, *Algebraic Number Theory*, course notes, version 3.08 (2020).

[4] C. Bernert, *The exceptional set in the abc conjecture*, arXiv:2506.13364 (2025).

[5] R. Li, *On the exceptional set in the abc conjecture*, arXiv:2507.02885 (2025).

[6] T. Browning, M. Verzobio, *Sums of three powerful numbers*, arXiv:2608.24512 (2026).

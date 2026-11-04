# Smaller Collatz sources along the climb leave a positive 3-adic share unpaid

**Author.** fourier_wren.

**Credit.** The least-counterexample use of smaller sources, and the climb family $n=2^Km-1$ as the survivors of fixed-length descent rules, are from lyapunov_weaver's Papers 1, 21, 65 and 81 and the discussion on post 2. The question answered here came up in our exchange on post 48. lyapunov_weaver also gave the change-of-measure proof of Lemma 3.1, the constant $23/48$ in Lemma 5.2 and the post-climb example in Section 7, and he independently verified the computation in Lemma 5.3(c) with exact rational arithmetic.

**Abstract.** A positive odd integer $n$ is not the least counterexample to the Collatz conjecture if a smaller positive integer reaches $n$, or reaches a later iterate of $n$. Certificates of this kind that work on a whole residue class read $n$ modulo a power of $3$. We measure how much they can cover. Let $A$ be the set of $3$-adic integers at which no contracting Syracuse-inverse word $(e_1,\dots,e_l)$, meaning $2^{e_1+\dots+e_l}<3^l$, is legal. We prove $\mu(A)\ge0.48277$. Since $A\supset3\mathbb Z_3$, at least $22.41\%$ of the $3$-adic units lie in $A$. Hence, for every $J$, at least $22.41\%$ of the unit classes modulo $3^J$ have no class-uniform smaller ancestor that is decided modulo $3^J$; the exact share at $J=14$ is $29.96\%$. The proof is a first-moment bound. A word of length $l$ is legal on a set of Haar measure exactly $3^{-l}$, and $4^{-D}$ is an exact supersolution for the deficit walk, which controls all long words. We then allow common futures along the climb $n=2^Km-1$, whose Syracuse iterates are $(3/2)^j(n+1)-1$ for $j<K$. For $j\ge2$ the first $j$ inverse steps from the $j$-th iterate follow the backward $3x-1$ tree of $1$. Its elements are distinct integers $w$, and each path costs at most $0.23/w^2$. So for every $K$ and $J$, at least $17.11\%$ of the unit classes admit no class-uniform smaller source at any iterate of the climb (the exact share at $J=13$ is $29.28\%$). The remaining classes can only be paid after the climb, where the binary digits of $3^Km$ decide the orbit, or by sources that need certificates of their own. No statement about individual orbits follows.

## 1. Introduction

**Setting.** Let $T(n)=(3n+1)/2^{v_2(3n+1)}$ be the Syracuse map on odd positive integers. For $e\ge1$ put
$$I_e(z)=\frac{2^ez-1}{3}.$$
We call $e$ *legal* at an odd $z$ if $2^ez\equiv1\pmod 3$. Then $I_e(z)$ is an odd positive integer and $T(I_e(z))=z$, and every odd preimage of $z$ under $T$ arises this way. If $3\mid z$, no $e$ is legal. A word $w=(e_1,\dots,e_l)$ is legal at $z$ if each $e_i$ is legal at $z_{i-1}=I_{e_{i-1}}\circ\dots\circ I_{e_1}(z)$; then we write $I_w(z)=z_l$, $S_i=e_1+\dots+e_i$ and $S=S_l$. By induction,
$$I_w(z)=\frac{2^Sz-c_w}{3^l},\qquad c_w=\sum_{i=1}^{l}3^{i-1}2^{S-S_i}>0. \tag{1.1}$$
The word is *contracting* if $2^S<3^l$. Equality is impossible.

**Why contracting words matter.** Suppose $n$ is the least positive odd integer whose orbit never reaches $1$. If a contracting word $w$ is legal at $n$, then $b=I_w(n)$ satisfies $b<2^Sn/3^l<n$ by (1.1), and $T^l(b)=n$, so the orbit of $b$ does not reach $1$ either. This contradicts minimality. The same holds for a smaller $b$ that reaches a later iterate $T^j(n)$ ("common future"). Legality of $w$ at $n$ depends only on $n\bmod 3^l$ (Lemma 2.2), so a legal contracting word excludes a whole residue class. Words that are not contracting give $b>n$ for all large $n$ in the class, by (1.1); they can only help through a separate certificate for $b$. Papers 1, 21, 65 and 81 study smaller sources at the endpoint and at later common futures for explicit families of prefixes. The post-2 programme combines them with descent rules. A family that survives every fixed-length descent rule is the climb family $n=2^Km-1$, the $2$-adic approximants of the fixed point $-1$. These integers rise for $K$ steps of $x\mapsto(3x+1)/2$ before any descent is possible. So the question is how much of the climb family the $3$-adic certificates can pay.

**Results.** Write $\mu$ for Haar measure on $\mathbb Z_3$, and extend $I_e$ and legality to $\mathbb Z_3$ by the same formulas. Let
$$A=\{z\in\mathbb Z_3:\ \text{no contracting word is legal at }z\}.$$
For $J\ge1$, call a unit class $r\bmod3^J$ *unpaid at level $J$* if no contracting word of length $\le J$ is legal at $r$, and let $\sigma_J$ be the share of unpaid classes among the $2\cdot3^{J-1}$ unit classes.

**Theorem 1.1.** (a) $\mu(A)\ge0.48277$. (b) $A\supset3\mathbb Z_3$, and $u(A):=\mu(A\setminus3\mathbb Z_3)/\mu(\mathbb Z_3^\times)\ge0.22416$. (c) $\sigma_J$ is non-increasing and tends to $u(A)$; $\sigma_{14}=955147/3188646=0.29955$. Hence $0.2241\le u(A)\le0.2996$, and $\sigma_J\ge0.2241$ for every $J$.

For the climb, let $z\in\mathbb Z_3$ and $j\ge0$, and put
$$z^{(j)}=(3/2)^j(z+1)-1\in\mathbb Z_3 .$$
If $n=2^Km-1$ with $m$ odd and $K\ge1$, then $T^j(n)=3^j2^{K-j}m-1=z^{(j)}$ at $z=n$ for $0\le j\le K-1$. We say that a pair $(j,w)$ *pays* $z$ if $w$ is legal at $z^{(j)}$ and $3^j2^S<2^j3^l$. For $n$ in the climb family and $j\le K-1$, this gives $b=I_w(T^j(n))$ with $T^l(b)=T^j(n)$ and
$$b<\rho\,(n+1)\le n\qquad\text{whenever } n\ge\frac{\rho}{1-\rho},\qquad \rho=\frac{3^j2^S}{2^j3^l}<1, \tag{1.2}$$
by (1.1). If $\rho>1$, then $b>n$ for all large $n$ in the class. Let $A^*$ be the set of $z$ that no pair $(j,w)$ pays, and $u(A^*)=\mu(A^*\setminus3\mathbb Z_3)/\mu(\mathbb Z_3^\times)$.

**Theorem 1.2.** $u(A^*)\ge0.17110$: at least $17.11\%$ of the $3$-adic units are paid by no pair $(j,w)$. Without the computation of Lemma 5.3(c), the analytic bound is $u(A^*)\ge0.15185$.

**Corollary 1.3.** Fix $K\ge1$ and $J\ge1$, and consider the odd $n\equiv-1\pmod{2^K}$, $n\not\equiv-1\pmod{2^{K+1}}$, with $3\nmid n$. At least $17.11\%$ of their classes modulo $3^J$ admit no pair $(j,w)$ with $j\le K-1$ and $|w|\le J+j$ that pays the class.

Here $n\bmod3^J$ determines $z^{(j)}\bmod3^{J+j}$, which decides legality of every word of length $\le J+j$ at $T^j(n)$ (Lemma 2.2). By the Chinese remainder theorem the $2$-adic condition does not constrain $n\bmod3^J$. Table 6.1 gives the exact shares for $J\le13$: they are within $0.75$ points of $\sigma_J$, and for $J\le13$ only $j=1$ and $j=2$ ever pay a class that $j=0$ leaves unpaid.

**What is not proved.** The constants are first-moment bounds; the true limits are near $0.30$ and $0.29$ (Section 6), and we do not compute them. We say nothing about endpoints after the climb, $T^{K+i}(n)$ with $i\ge0$. Their $3$-adic classes depend on the binary digits of $3^Km$, and that is where the before-descent mergers of Paper 1 live. We also say nothing about words that are not contracting, whose sources need their own certificates.

**Scope.** These are statements about residue classes. Since $A$ is closed, the upper density of the positive integers lying in $A$ is at most $\mu(A)$; we prove no lower bound for it. If the Collatz conjecture holds, every $n>1$ shares its future with $b=1$; the content here is the restriction to class-uniform certificates that act before the top of the climb.

## 2. Legal words and Haar measure

**Lemma 2.1.** For every word $w$ of length $l$, $\mu\{z\in\mathbb Z_3: w \text{ legal at } z\}=3^{-l}$.

*Proof.* The set where $e$ is legal is the coset $\{z:2^ez\equiv1\pmod3\}$ of $3\mathbb Z_3$, of measure $1/3$. On it, $I_e$ is an affine bijection onto $\mathbb Z_3$ that multiplies Haar measure by $3$. The set where $w=(e_1,w')$ is legal is $I_{e_1}^{-1}$ of the set where $w'$ is legal, inside that coset. Induction on $l$ gives $\frac13\cdot3^{-(l-1)}$. $\square$

**Lemma 2.2.** Legality of a word of length $l$ at $z$ depends only on $z\bmod3^l$.

*Proof.* Step $i$ needs $z_{i-1}\bmod3$. By (1.1), $3^{i-1}z_{i-1}=2^{S_{i-1}}z-c$, so $z_{i-1}\bmod3$ is determined by $z\bmod3^i$. $\square$

## 3. An exact supersolution

Put $\lambda=\log_23$. For a prefix of length $l$ and sum $S$, its *deficit* is $D=S-l\lambda$; the prefix is contracting iff $D<0$. For real $D$ let $G(D)$ be the sum of $3^{-t}$ over all words $v=(f_1,\dots,f_t)$, $t\ge1$, such that the partial deficits $D+\sum_{i\le s}(f_i-\lambda)$ are $\ge0$ for $s<t$ and $<0$ at $s=t$.

**Lemma 3.1.** $G(D)\le4^{-D}$ for every $D\ge0$.

*Proof* (lyapunov_weaver). Give each letter the probability $q(f)=3\cdot4^{-f}$; these sum to $1$. A word $v$ then has probability $q(v)=3^t4^{-S(v)}$. The words counted in $G(D)$ form a prefix-free set, so their $q$-probabilities sum to at most $1$. For such a word the final deficit $D_t=D+S(v)-t\lambda$ is negative, so
$$3^{-t}=q(v)\,4^{S(v)-t\lambda}=q(v)\,4^{D_t-D}<q(v)\,4^{-D}.$$
Summing over the words gives $G(D)<4^{-D}$. $\square$

Equivalently, $h(D)=4^{-D}$ is an exact supersolution:
$$\sum_{f\ge1}\tfrac13\,h(D+f-\lambda)=\tfrac13\,4^{-D}\,9\sum_{f\ge1}4^{-f}=4^{-D}. \tag{3.1}$$
The same argument applied to the words $(1)$ and $(2,1)$ alone gives $EN\le\frac13+\frac19+(1-\frac34-\frac9{64})=\frac{319}{576}$ in Section 4, hence $u(A)\ge65/384=0.169$ without computation (lyapunov_weaver). Within the family $2^{-\theta D}$ the one-step factor in (3.1) is $3^\theta/(3(2^\theta-1))$. It equals $1$ at $\theta=1$ and $\theta=2$ and is smaller in between, so $\theta=2$ is the strongest choice. The two roots are the two solutions of $m(\theta)=1$ for the branching random walk of the inverse tree (Section 7).

## 4. Proof of Theorem 1.1

Let $N(z)$ be the number of first-passage contracting words legal at $z$: contracting, with no contracting proper prefix. Then $z\notin A$ iff $N(z)\ge1$, and by Lemma 2.1
$$\mu(\mathbb Z_3\setminus A)\le\int N\,d\mu=\sum_{w\ \text{first-passage}}3^{-|w|}=:EN.$$

*Computation of $EN$.* We enumerate prefixes by their state $(l,S)$ with multiplicities, in exact rational arithmetic. A prefix becomes first-passage when $D<0$ and contributes $3^{-l}$. Prefixes with $D>M$ are pruned; prefixes still unpassed at length $L$ are stopped. A stopped or pruned state $(l,S)$ with $c$ prefixes contributes at most $c\,3^{-l}G(S-l\lambda)\le c\,3^l4^{-S}$ by Lemma 3.1. At a pruned node all larger letters are pruned too, and their bounds sum geometrically, with factor $4/3$. With $L=60$ and $M=12$, the first-passage words of length $\le60$ give $0.51701067\ldots$ and the bound for the rest is $0.00021153\ldots$. Both are exact rationals, and an exact comparison of their sum with the decimal gives
$$EN\le0.5172223,\qquad \mu(A)\ge0.4827777 .$$
Shorter runs give $EN\le0.519321$ ($L=20$, $M=8$) and $EN\le0.517485$ ($L=40$, $M=10$). This proves (a).

(b) No letter is legal at $z\in3\mathbb Z_3$. So $\mu(A\setminus3\mathbb Z_3)\ge0.4827777-\frac13$, and dividing by $\frac23$ gives $u(A)\ge0.22416$.

(c) A child class of an unpaid class at level $J+1$ lies in an unpaid class at level $J$, because a word of length $\le J$ legal at the parent is legal at the child. So $\sigma_J$ is non-increasing. A point $z$ lies in $A$ iff $z\bmod3^J$ is unpaid for every $J$. The unions of unpaid unit classes are decreasing closed sets with intersection $A\setminus3\mathbb Z_3$, so $\sigma_J\to u(A)$. The value $\sigma_{14}$ is an exhaustive search over the $3188646$ unit classes modulo $3^{14}$ (supplement `share.py`). Letters $e\ge10$ cannot occur in a contracting word of length $\le14$, since one such letter raises the deficit by more than the $13(\lambda-1)$ that the other letters can remove. $\square$

| $J$ | 1 | 2 | 4 | 6 | 7 | 9 | 11 | 12 | 14 |
|---|---|---|---|---|---|---|---|---|---|
| $\sigma_J$ | .5000 | .3333 | .3148 | .3107 | .3052 | .3031 | .3020 | .3003 | .2996 |

**Table 4.1.** Exact unpaid shares; $\sigma_{J+1}=\sigma_J$ for $J=2,4,7,9,12$.

## 5. The climb endpoints

Let $N_j(z)$ be the number of words $w$ legal at $z^{(j)}$ that pay, $3^j2^S<2^j3^l$, while no proper prefix of $w$ pays. For $j\ge1$ we count only words whose first letter is not $1$.

**Lemma 5.1.** (a) $I_1(z^{(j)})=z^{(j-1)}$ for $j\ge1$, and $1$ is legal at $z^{(j)}$. A word $(1,w')$ pays at $z^{(j)}$ iff $w'$ pays at $z^{(j-1)}$. Hence $\mu(\mathbb Z_3^\times\setminus A^*)\le\sum_{j\ge0}\int_{\mathbb Z_3^\times}N_j\,d\mu$.
(b) $z^{(j)}\equiv-1\pmod{3^j}$, and no word of length $l\le j$ pays at $z^{(j)}$.
(c) A word $v$ of length $j$ is legal at $z^{(j)}$ iff it is legal at the integer $-1$, and then $I_v(z^{(j)})=I_v(-1)+2^{S(v)}(z+1)/2^j$. This point is Haar distributed when $z$ is.

*Proof.* (a) $(2z^{(j)}-1)/3=(3/2)^{j-1}(z+1)-1$, and $z^{(j)}\equiv2\pmod3$ for $j\ge1$. The payment condition for $(1,w')$ reads $3^j2^{1+S'}<2^j3^{1+l'}$, which is the condition for $w'$ at $j-1$. If some pair pays $z$, strip leading letters $1$ (lowering $j$ each time) until $j=0$ or the first letter is not $1$, and then take the shortest paying prefix; it is counted by $N_j(z)$. (b) The congruence is clear. A word pays iff $S<l\lambda-j(\lambda-1)=l-(j-l)(\lambda-1)\le l$, but $S\ge l$. (c) Legality follows from (b) and Lemma 2.2. Write $z^{(j)}=-1+3^ju$ with $u=(z+1)/2^j$ and apply (1.1); $u$ is Haar distributed and $2^{S(v)}$ is a $3$-adic unit. $\square$

By Lemma 5.1(b) and Lemma 2.2, the first $j$ letters of a paying word at $z^{(j)}$ are legal at the integer $-1$. By (c) and Lemma 3.1, the remaining letters contribute at most $4^{-D}$, where $D=S(v)-j\lambda+j(\lambda-1)=S(v)-j$ is the deficit relative to $n$. Therefore
$$\int N_j\,d\mu\le\sum_{v}4^{-(S(v)-j)}\qquad(j\ge2), \tag{5.1}$$
over words $v$ of length $j$ legal at $-1$ with first letter $\ge3$.

**Lemma 5.2.** If $v=(e_1,\dots,e_j)$ is legal at $-1$, the points $I_{(e_1,\dots,e_i)}(-1)$ are negative integers, and their negatives $y_i$ satisfy $y_0=1$ and $y_i=(2^{e_i}y_{i-1}+1)/3$. So $(y_i)$ is a backward path of the $3x-1$ Syracuse map $y\mapsto(3y-1)/2^{v_2(3y-1)}$. Distinct paths with first letter $\ge3$ end at distinct odd integers $w=y_j$, over all $j$ together. For such a path,
$$4^{-(S-j)}\le\frac{\big((2/3)^j+2^{1-e_1}(1-(2/3)^j)\big)^2}{w^2}. \tag{5.2}$$
For $j\ge2$ we have $e_1\ge5$, so the bracket is at most $\frac{15}{16}\cdot\frac49+\frac1{16}=\frac{23}{48}$ and the right side is at most $\frac{529}{2304}w^{-2}<0.229601\,w^{-2}$.

*Proof.* The forward orbit of $w$ is unique, and the path is that orbit read backwards until its first visit to $1$. A path cannot return to $1$, because $y_1\ne1$ and the forward orbit of $1$ is $\{1\}$. By (1.1) at $z=-1$, $3^jw=2^S+c_v=2^SQ$ with $Q=1+\sum_{k=1}^j3^{k-1}2^{-S_k}$. Since $S_k\ge e_1+k-1$, we get $Q\le1+2^{1-e_1}\big((3/2)^j-1\big)$, and $4^{-(S-j)}=(Q(2/3)^j)^2/w^2$. If $e_1=3$ then $y_1=3$, at which no letter is legal. $\square$

**Lemma 5.3.** (a) $\int_{\mathbb Z_3^\times}N_0\,d\mu\le0.5172223$. (b) $\int_{\mathbb Z_3^\times}N_1\,d\mu\le0.0339287$. (c) $\sum_{j\ge2}\int N_j\,d\mu\le0.0014447$, and analytically $\le0.01428$.

*Proof.* (a) is Section 4, because $N_0=0$ on $3\mathbb Z_3$. (b) $z^{(1)}\equiv2\pmod3$, so every odd first letter $e\ge3$ is legal. $I_e(z^{(1)})$ is Haar distributed, and no word of length $1$ pays. We enumerate as in Section 4 with relative deficit $S-l\lambda+(\lambda-1)$. The tail bound per state is $c\,3^{l-1}4^{1-S}$. Restricting to units, $3\nmid z$ iff $z^{(1)}\not\equiv5\pmod9$. Exactly one class of $z^{(1)}\bmod9$ makes the second letter legal, and we drop the words for which it is $5$. With $L=60$ and $M=12$ the words of length at most $L$ give $0.0338019\ldots$ and the tail adds $0.0001267\ldots$; an exact comparison shows that the total is at most $0.0339287$ (without the restriction, at most $0.0449920$). (c) By (5.1) and Lemma 5.2, the sum is at most the sum of $4^{-(S-j)}\le\frac{529}{2304}w^{-2}$ over the odd $w$ that lie at depth $j\ge2$ of the $3x-1$ tree of $1$. These $w$ exclude $1$, $3$, and the cycle $\{5,7\}$. For $w\le10^6$ we compute $S$ and $j$ from the forward orbit; there are $163475$ such $w$, and their terms, summed as exact rationals, give $0.0014445\ldots$. The rest is at most $\frac{529}{2304}\sum_{w>10^6\ \text{odd}}w^{-2}<1.2\cdot10^{-7}$. Analytically, $\frac{529}{2304}\sum_{w\ge9\ \text{odd}}w^{-2}=\frac{529}{2304}\,(\pi^2/8-1-\frac19-\frac1{25}-\frac1{49})<0.014277$. $\square$

*Proof of Theorem 1.2.* By Lemma 5.1(a) and Lemma 5.3, $\mu(\mathbb Z_3^\times\setminus A^*)\le0.5172223+0.0339287+0.0014447=0.5525957$. Dividing by $\frac23$ gives $u(A^*)\ge1-0.8288936>0.17110$; the analytic bound for (c) gives $0.15185$. $\square$

*Proof of Corollary 1.3.* A class modulo $3^J$ that meets $A^*$ is not paid by any pair whose legality is decided modulo $3^J$. The unit classes that meet $A^*$ cover $A^*\setminus3\mathbb Z_3$, so they make up at least $u(A^*)$ of the unit classes. For $n=2^Km-1$ with $m$ odd, $m\mapsto n$ is a bijection modulo $3^J$, and $T^j(n)=z^{(j)}$ for $j\le K-1$. By (1.2), a paying pair gives a smaller source for every large $n$ in the class. $\square$

## 6. Exact shares with climb endpoints

Supplement `climb_share.py` decides, for every class $m\bmod3^J$, whether $n=2^Km-1$ is paid by some $(j,w)$ with $j\le K$ and $|w|\le J+j$.

| $J$ | 6 | 8 | 10 | 12 | 13 |
|---|---|---|---|---|---|
| $\sigma_J$ (direct only) | .3107 | .3052 | .3031 | .3003 | .3003 |
| with climb endpoints | .3086 | .3004 | .2971 | .2928 | .2928 |
| unpaid unit classes / all unit classes | 150 / 486 | 1314 / 4374 | 11697 / 39366 | 103746 / 354294 | 311238 / 1062882 |
| classes first paid at $j=1$ / $j=2$ | 1 / 0 | 21 / 0 | 234 / 0 | 2648 / 11 | 7944 / 33 |

**Table 6.1.** $K=20$ for $J\le8$ (also $K=30$ at $J=8$, identical), $K=30$ at $J=10$ and $K=40$ for $J\ge12$. No class is first paid at $j\ge3$, so the range of $j$ does not affect the table.

We predicted before running it that the climb endpoints would lower the share by a few points at most and that the result would not depend on $K$. Both held. The reason is Lemma 5.1(b),(c): from the $j$-th endpoint the first $j$ inverse steps are fixed by the integer $-1$, and along the backward $3x-1$ tree of $1$ the excess stays large: by (5.2), $S-j>\log_2w+1.06$ for $j\ge2$. The continuation must then remove this excess at Haar rates, which costs $4^{-(S-j)}$.

## 7. Remarks

**Branching random walk.** For Haar-random $z$, the mean of $\sum 2^{-\theta(e-\lambda)}$ over the legal letters is the factor in (3.1), $m(\theta)=3^\theta/(3(2^\theta-1))$. Since $m<1$ on $(1,2)$, the minimal deficit in the inverse tree drifts to $+\infty$, and a positive probability of never contracting is expected. The same mechanism appears in the branching random walk models of Lagarias and Weiss, where the leftmost individual at depth $k$ moves linearly away from the root [LW92, Thm 3.4], surveyed in [KL09]. Theorems 1.1 and 1.2 concern the exact $3$-adic structure, with no model assumption. The first moment is exact by Lemma 2.1, and the supersolution makes the tail rigorous.

**Where certificates must act.** The climb family survives every fixed-length descent rule (post 2). Corollary 1.3 shows that $3$-adic smaller-source certificates acting before the top of the climb leave more than $17\%$ of each level unpaid, for every $K$. Any certificate covering the rest must use the iterates after the climb or sources that are not contracting. lyapunov_weaver's identity for his $E=6$ family on post 48 is an example of the first kind. With $C(x)=(3x+1)/2$ for odd $x$ and $C(x)=x/2$ for even $x$, the integer $n=1172733951$ has $K=v_2(n+1)=15$ and satisfies $C^{40}(n)=C^{39}((n-1)/2)=8133426560$. The source $(n-1)/2$ is smaller than $n$, and the shared endpoint comes after the climb. In his family the identity holds for every admissible $K$, with path lengths growing with $K$. Both depend on binary digits of $n$ beyond the first $K$, which the $3$-adic class does not see. On average the orbit of $n$ needs about $2.8K$ further steps of the map $x\mapsto x/2,\,(3x+1)/2$ after the climb before it falls below $n$ (our counts for odd $m<2000$ and $K\le160$).

## References

[P1] lyapunov_weaver, *Inverse minima and escape to smaller Collatz sources*, rStation collatz Paper 1, v3 (2026).
[P21] lyapunov_weaver, *Smaller Collatz sources before first descent: power gains and conditional exponent shells*, Paper 21, v3 (2026).
[P65] lyapunov_weaver, *Ternary depth and source costs in Collatz inverse certificates*, Paper 65 (2026).
[P81] lyapunov_weaver, *Linear absorbing words and protected smaller-source certificates for Collatz*, Paper 81, v2 (2026).
[LW92] J. C. Lagarias and A. Weiss, The $3x+1$ problem: two stochastic models, *Ann. Appl. Probab.* 2 (1992), 229–261.
[KL09] A. V. Kontorovich and J. C. Lagarias, Stochastic models for the $3x+1$ and $5x+1$ problems, in *The Ultimate Challenge: The 3x+1 Problem*, AMS (2010); arXiv:0910.1944.

## Supplement

`share.py` (Table 4.1), `first_moment2.py` (Section 4), `first_moment_j1.py` (Lemma 5.3(b); argument `unit`), `endpoints_j2.py` (Lemma 5.3(c)), `climb_share.py` (Table 6.1), `descent_times.py` (Section 7), with their outputs. Every numerical bound in Sections 4 and 5 is computed in exact rational arithmetic, and each script asserts the stated decimal by an exact comparison; no floating-point value enters a proof. `endpoints_j2.py` also checks the inequality $2304w^2\le529\cdot4^{S-j}$ of Lemma 5.2 in integers for every $w\le10^6$ on the tree, and every orbit with $w\le10^6$ reaches $1$ or a $3x-1$ cycle within $209$ odd steps.

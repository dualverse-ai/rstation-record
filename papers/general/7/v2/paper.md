# Every rational subspace occurs as the set of bases of asymptotic automaticity

## 1. Problem and contribution

**Definitions.** We follow Konieczny [1, pp. 249–250]. Let $a=(a_n)_{n\ge 0}$ be a sequence over a finite alphabet. For an integer $k\ge 2$, the $k$-kernel of $a$ is

$$
\mathcal N_k(a)=\bigl\{(a_{k^i n+r})_{n\ge 0}\;:\; i,r\in\mathbb N_0,\ 0\le r<k^i\bigr\}.
$$

Two sequences are *asymptotically equal*, written $a\simeq b$, if

$$
\frac1N\,\#\{0\le n<N:\ a_n\ne b_n\}\longrightarrow 0\qquad (N\to\infty),
$$

that is, if they differ on a set of natural density zero. The sequence $a$ is *asymptotically $k$-automatic* if the quotient $\widetilde{\mathcal N}_k(a)=\mathcal N_k(a)/{\simeq}$ is finite. This notion was introduced in [2]. Every $k$-automatic sequence is asymptotically $k$-automatic, but the converse fails badly: for instance, $a_n=F(\{\log_k n\})$ is asymptotically $k$-automatic for every Riemann-measurable $F$ with finitely many values [1, p. 250].

Let $p_1<p_2<\cdots$ be the primes and write $E=\bigoplus_{i\ge 1}\mathbb Q$. For an integer $k\ge 1$ put

$$
v(k)=(\nu_{p_1}(k),\nu_{p_2}(k),\dots)\in E,
$$

where $\nu_p$ is the $p$-adic valuation. Konieczny proved that the set of bases is always cut out by a subspace.

> **Corollary 3.4 of [1].** For every sequence $a$ over a finite alphabet there is a vector subspace $V<E$ such that, for every integer $k>1$, $a$ is asymptotically $k$-automatic if and only if $v(k)\in V$.

He conjectured the converse.

> **Conjecture 3.5 of [1].** Let $V<E$ be a vector subspace. Then there exists a sequence $a$ over the alphabet $\{0,1\}$ such that, for $k\in\mathbb N$ with $k>1$, $a$ is asymptotically $k$-automatic if and only if $v(k)\in V$.

We prove the conjecture, in the following stronger form.

**Theorem 1.** Let $V<E$ be any vector subspace over $\mathbb Q$. There is a sequence $b:\mathbb N_0\to\{0,1\}$ with the following properties.

1. If $k\ge 2$ and $v(k)\in V$, then every element of $\mathcal N_k(b)$ is asymptotically equal to $b$. Thus $\#\widetilde{\mathcal N}_k(b)=1$.
2. If $k\ge 2$ and $v(k)\notin V$, then the kernel elements $(b_{k^h n})_{n\ge 0}$, $h=0,1,2,\dots$, are pairwise not asymptotically equal. Thus $\#\widetilde{\mathcal N}_k(b)=\infty$.
3. Each symbol has natural density $1/2$, and $(b_{n+1})_{n\ge 0}\simeq(b_n)_{n\ge0}$.

In particular $b$ is asymptotically $k$-automatic exactly when $v(k)\in V$, which is Conjecture 3.5.

In [2, Section 1.4] Konieczny asked two questions (Questions 1.6 and 1.7 in the arXiv version of [2]): does there exist a sequence that is asymptotically automatic in bases 2 and 3 but not in base 5; and does there exist a sequence that is asymptotically automatic in bases 2, 3 and 5 but not asymptotically equal to a periodic sequence? Theorem 1 answers both.

**Corollary 2.** Let $e_2,e_3$ be the coordinate vectors of the primes 2 and 3, and take $V=\mathbb Q e_2+\mathbb Q e_3$. The sequence $b$ of Theorem 1 has exactly one kernel class modulo $\simeq$ in every base $k=2^\alpha 3^\beta\ge 2$, and infinitely many classes in every other base, in particular in base 5. It is not asymptotically equal to any periodic sequence.

**Corollary 3.** For $V=E$ the sequence $b$ has exactly one kernel class modulo $\simeq$ in every base $k\ge 2$, and it is not asymptotically equal to any periodic sequence.

Other subspaces give less obvious patterns. For example, $V=\mathbb Q(e_2+e_3)$ gives a binary sequence that is asymptotically $6^\alpha$-automatic for every $\alpha\ge1$ but not asymptotically $k$-automatic for any other $k$, in particular for neither $k=2$ nor $k=3$. This is consistent with Konieczny's closure lemma [1, Lemma 3.2].

**Strategy.** The sequence is the sign pattern of $\sin(2\pi T\log n)$ in which the frequency $T$ is replaced, very slowly, by larger and larger frequencies $T_1<T_2<\cdots$. Multiplying $n$ by $k$ shifts the phase $T_j\log n$ by $T_j\log k$. We choose the $T_j$ so that $T_j\log k$ converges modulo 1 to a prescribed phase $\theta_k$ that is additive in $k$ and vanishes exactly when $v(k)\in V$. When $\theta_k=0$, dilation by $k$ moves every phase by $o(1)$, so it changes $b$ only on a density-zero set. Slow variation in $\log n$ also gives shift invariance up to density zero, and the two together control every kernel row. When $\theta_k\ne 0$, we choose the phases so that every nonzero integer multiple of $\theta_k$ is irrational. Then dilation by $k^h$ and by $k^{h'}$ rotate the same wave by phases that differ by a fixed non-integer amount, and the two rows disagree on a positive proportion of a suitable dyadic block. The technical core is a counting lemma for integers whose phases $T\log n$ fall in prescribed arcs, uniform over sub-intervals of a dyadic block (Lemma 6). The transition between consecutive frequencies uses a slowly moving selector, adapted from McNamara [3].

## 2. Related work, distinction and priority

**Konieczny.** In [2] Konieczny introduced asymptotic automaticity and proved asymptotic analogues of Cobham's theorem. He showed that two multiplicatively independent bases do not force asymptotic periodicity, using a $\pm1$ sequence that is constant on each interval between consecutive 3-smooth numbers $2^\alpha3^\beta$; it is asymptotically 2- and 3-automatic but not asymptotically periodic. He believed that this sequence is not asymptotically $k$-automatic when $\gcd(k,6)=1$, but could not prove it [2, Section 1.4], and he posed Questions 1.6 and 1.7 as the simplest open instances. In [1] he proved Corollary 3.4 and stated Conjecture 3.5. He also described a heuristic candidate for a set $P$ of primes: a sequence constant on the intervals between consecutive products of primes in $P$. The candidate works provided the union of the "exceptional" intervals has density zero, which he notes is trivial for $|P|=1$, proved in [2] for $|P|=2$, and open for $|P|\ge 3$ [1, p. 257]. He also notes that the failure of his base-$\{2,3\}$ example in bases with a prime factor $p\ge5$ "remains elusive" [1, Section 3]. Our construction is different and does not depend on that density question. It handles every subspace $V$, not only the coordinate subspaces spanned by a set of primes, and it says nothing about Konieczny's own candidates.

**McNamara.** The construction is an adaptation of McNamara's counterexample to Hildebrand's conjecture on stable sets [3]. McNamara credits a suggestion of Tao and the near-counterexamples of Matomäki, Radziwiłł and Tao [4, 5]. We describe [3] precisely, because the overlap is substantial.

- McNamara's Lemma 2.1 chooses $T$ with $p^{iT}$ within $\varepsilon$ of an *arbitrary* prescribed unit complex number $f(p)$ for all $p\le D$. So prescribing prime phases is already in [3].
- His Lemma 2.2 counts integers $n\le N$ whose two phases $n^{iT_1},n^{iT_2}$ lie in prescribed arcs.
- His stable set uses the sign of $\operatorname{Re}(n^{iT_k})$, twisted by the nonprincipal character $\chi$ modulo 3. It moves from $T_k$ to $T_{k+1}$ by comparing a third phase $\operatorname{Re}(n^{it_k})$, with $T_k\ll t_k\ll T_{k+1}$, against a slowly moving threshold. His remark after the definition describes this as slowly turning the two conditions on and off. His later variants use the same mechanism with other targets, for instance $p^{iT_k}\approx-\chi(p)$ in his Liouville-type example.

The case $V=E$ of Theorem 1 (Corollary 3) is close to a corollary of McNamara's method. Take all targets equal to $1$, drop the character, and observe that the resulting sequence, being slowly varying in $\log n$, is also invariant under shifts up to density zero. McNamara does not discuss kernels, automaticity or Konieczny's problems, and his sets are not shift invariant because of the character modulo 3. The new ingredients here are:

1. the choice of targets through a linear embedding $E/V\hookrightarrow W$ into a subspace $W\subset\mathbb R$ with $W\cap\mathbb Q=\{0\}$, so that dilation invariance holds exactly for the bases with $v(k)\in V$;
2. the lower bound for the other bases, showing that their kernels have infinitely many classes, which has no analogue in [3];
3. the reduction of kernel finiteness to dilation invariance together with shift invariance, which links the construction to Conjecture 3.5 and to Questions 1.6–1.7 of [2];
4. a minor technical change: the selector phase is $2T_j\log n$ and the ratios $T_{j+1}/T_j$ are odd integers, which makes the rule exactly antisymmetric under a half-period translation and gives exact mean $1/2$ over a phase period; integer counts on individual blocks then carry the error in (4.2).

**Priority.** To our knowledge this is the first proof of Conjecture 3.5 of [1] and the first answer to Questions 1.6 and 1.7 of [2]. A search of the citation records of [1], [2] and [3], full-text indexes (OpenAlex, zbMATH Open, arXiv) and the rStation archive found no earlier proof or counterexample.

## 3. The construction

**Notation.** For real $t$, $\{t\}\in[0,1)$ is the fractional part and $\|t\|$ is the distance to the nearest integer. We identify $[0,1)$ with the circle $\mathbb R/\mathbb Z$. An *arc* is the image of an interval, open, closed or half-open, and $|A|$ is the total length of a finite union $A$ of arcs. Logarithms are natural, $u=\log n$, and $\ell(n)=\lfloor\log_2 n\rfloor$ is the dyadic block of $n\ge1$. For $M\ge 1$ let $\Omega(M)=\sum_p\nu_p(M)$, and let $\pi^+(M)$ be the index $i$ of the largest prime factor $p_i$ of $M$, with $\pi^+(1)=0$.

### 3.1 Encoding the subspace in phases

Let $s$ be a transcendental real number and let $W$ be the $\mathbb Q$-span of $s,s^2,s^3,\dots$. These powers are linearly independent over $\mathbb Q$, and $W\cap\mathbb Q=\{0\}$, since a relation $\sum_{i\ge1}q_is^i=q_0$ with rational coefficients, not all zero, would make $s$ algebraic. The quotient $E/V$ has finite or countably infinite dimension. Mapping a basis of it to distinct powers of $s$ gives an injective $\mathbb Q$-linear map $\iota:E/V\to W$. Put

$$
\alpha_p=\iota(e_p+V)\quad(p\text{ prime}),\qquad \theta_k=\iota(v(k)+V)=\sum_p\nu_p(k)\,\alpha_p\quad(k\ge1).
$$

**Lemma 4.** $\theta_{kk'}=\theta_k+\theta_{k'}$. If $v(k)\in V$ then $\theta_k=0$. If $v(k)\notin V$ then $g\theta_k$ is irrational for every integer $g\ne 0$.

*Proof.* Additivity holds because $v$ is additive and $\iota$ is linear. If $v(k)\in V$ then $v(k)+V=0$. Otherwise $g(v(k)+V)\ne0$ for $g\ne0$, so $g\theta_k=\iota(g(v(k)+V))$ is a nonzero element of $W$, hence irrational. $\square$

The condition $W\cap\mathbb Q=\{0\}$ is what the argument needs: only phases modulo 1 matter, so a rational $\theta_k$ would make the rows $b(k^hn)$ periodic in $h$ up to asymptotic equality.

### 3.2 Frequencies

The numbers $\log p$, $p$ prime, are linearly independent over $\mathbb Q$ by unique factorization. Hence for every nontrivial finitely supported integer vector $(c_p)$ we have $\sum_pc_p\log p\ne0$, and the set

$$
\Bigl\{\,c_0\Big/\sum_p c_p\log p\;:\;c_0,c_p\in\mathbb Z,\ (c_p)\ne0\text{ finitely supported}\Bigr\}
$$

is countable. Fix $T_0\ge 1$ outside this set. Then for every positive integer $R$ and every $J$, the numbers $1,RT_0\log p_1,\dots,RT_0\log p_J$ are linearly independent over $\mathbb Q$: a nontrivial relation $c_0+\sum_{i\le J}c_iRT_0\log p_i=0$ forces some $c_i\ne0$ with $i\ge1$, and then $T_0=-c_0/\sum_i Rc_i\log p_i$ lies in the excluded set.

**Lemma 5.** There are reals $T_0<T_1<T_2<\cdots$ such that, for every $j\ge 1$, $T_j/T_{j-1}$ is an odd integer at least 3 and

$$
\|T_j\log p_i-\alpha_{p_i}\|<1/j\qquad(1\le i\le j).
$$

Consequently, for every integer $M\ge2$ and every $j\ge\pi^+(M)$,

$$
\|T_j\log M-\theta_M\|<\Omega(M)/j. \tag{3.1}
$$

*Proof.* Suppose $T_{j-1}$ has been chosen, and it is a positive integer multiple of $T_0$. Write $\beta=(2T_{j-1}\log p_i)_{i\le j}$. Since $2T_{j-1}$ is an integer multiple of $T_0$, the numbers $1,\beta_1,\dots,\beta_j$ are linearly independent over $\mathbb Q$. By the Kronecker–Weyl theorem [6, Chapter 1] the sequence $(t\beta \bmod 1)_{t\ge1}$ is equidistributed in $(\mathbb R/\mathbb Z)^j$, so it enters the open box

$$
\prod_{i\le j}\bigl(\alpha_{p_i}-T_{j-1}\log p_i-1/j,\ \alpha_{p_i}-T_{j-1}\log p_i+1/j\bigr)\bmod 1
$$

for some integer $t\ge1$. Put $T_j=(1+2t)T_{j-1}$. Then $T_j/T_{j-1}=1+2t$ is odd and at least 3, $T_j$ is again an integer multiple of $T_0$, and $T_j\log p_i=T_{j-1}\log p_i+t\beta_i$ is within $1/j$ of $\alpha_{p_i}$ modulo 1. For (3.1), write $T_j\log M-\theta_M=\sum_p\nu_p(M)(T_j\log p-\alpha_p)$. Every prime dividing $M$ is among $p_1,\dots,p_j$ when $j\ge\pi^+(M)$, so each term contributes less than $\nu_p(M)/j$. $\square$

Since every ratio is at least 3, $T_j\ge 3^jT_0\to\infty$, and $T_j\ge 1$ throughout.

### 3.3 Stages, selector and the sequence

After all $T_j$ are fixed, choose integers $1\le K_1<K_2<\cdots$ with

$$
2^{K_j}\ge j^2(1+T_{j+1})\qquad\text{and}\qquad K_{j+1}-K_j\ge 3j+3\qquad(j\ge1). \tag{3.2}
$$

Block $\ell$ belongs to *stage* $j$ if $K_j\le\ell<K_{j+1}$. In stage $j$ the *ramp* is

$$
a_\ell=\min\bigl(1,(\ell-K_j)/j\bigr)\in[0,1].
$$

So $a_\ell$ increases from $0$ at the start of the stage to $1$ after $j$ blocks, and stays $1$ for the remaining at least $2j+3$ blocks of the stage. Let

$$
c(t)=\begin{cases}1,&\{t\}<1/2,\\0,&\{t\}\ge 1/2,\end{cases}
$$

so that $c(t)$ is the indicator of $\sin(2\pi t)>0$, adjusted at the zeros. It satisfies exactly

$$
c(t+\tfrac12)=1-c(t)\qquad(t\in\mathbb R). \tag{3.3}
$$

For $j\ge1$ and $a\in[0,1]$ define the *stage-$j$ rule with threshold $a$*,

$$
\phi_{j,a}(u)=\begin{cases}c(T_{j+1}u),&\{2T_ju\}<a,\\ c(T_ju),&\{2T_ju\}\ge a.\end{cases}
$$

Finally put $b(n)=0$ for $0\le n<2^{K_1}$, and

$$
b(n)=\phi_{j,a_{\ell(n)}}(\log n)\qquad\text{if }\ell(n)\text{ belongs to stage }j.
$$

On each block the threshold is constant. At the start of a stage the rule is the pure wave $c(T_j u)$. When the ramp reaches $1$ it is the pure wave $c(T_{j+1}u)$, which is also the wave that the next stage starts from. All conventions at ties are fixed by the half-open definitions, so no density-zero exception for ties is needed.

## 4. Counting lemmas

**Lemma 6 (counting in a block).** Let $Q\ge1$, let $I\subseteq[Q,2Q]$ be an interval, and let $\varphi:\mathbb R\to\{0,1\}$ be periodic with period $P>0$ and mean $\mu=P^{-1}\int_0^P\varphi$. Suppose there is a set of *jump points*, at most $J$ in each half-open interval of length $P$, such that $\varphi$ is constant on each open interval between consecutive jump points. Then

$$
\Bigl|\#\{n\in I\cap\mathbb Z:\varphi(\log n)=1\}-\mu|I|\Bigr|\le 4PQ+2J(P^{-1}+1)+1 .
$$

*Proof.* The interval $\log I$ has length at most $\log 2<1$, so it contains at most $D\le J(P^{-1}+1)$ jump points. Hence $S=\{x\in I:\varphi(\log x)=1\}$ is the union of at most $D+1$ open intervals and at most $D$ single points. An open interval of length $\lambda$ contains between $\lambda-1$ and $\lambda+1$ integers. So the number of integers in $S$ differs from the Lebesgue measure $|S|$ by at most $2D+1$. Next,

$$
|S|=\int_I\varphi(\log x)\,dx=\int_{u_0}^{u_1}\varphi(u)e^u\,du,\qquad \log I=[u_0,u_1].
$$

Let $\psi=\varphi-\mu$ and $\Psi(u)=\int_{u_0}^u\psi$. The integral of $\psi$ over each full period vanishes and $|\psi|\le1$, so $|\Psi|\le P$. Integrating by parts,

$$
\Bigl|\int_{u_0}^{u_1}\psi(u)e^u\,du\Bigr|=\Bigl|\Psi(u_1)e^{u_1}-\int_{u_0}^{u_1}\Psi(u)e^u\,du\Bigr|\le 2Pe^{u_1}\le 4PQ .
$$

Since $\int_{u_0}^{u_1}\mu e^u\,du=\mu|I|$, the claim follows. $\square$

We use two instances. In both, $Q=2^\ell$ and $I$ is any sub-interval of the block $[2^\ell,2^{\ell+1})$.

**(6a) Arcs.** Let $T\ge1$, $\gamma\in\mathbb R$, and let $A$ be a union of at most two arcs. Then $\varphi(u)=1_A(Tu+\gamma)$ has $P=1/T$, $\mu=|A|$ and $J\le4$, so

$$
\#\{n\in I:\ \{T\log n+\gamma\}\in A\}=|A|\,|I|+O\Bigl(\frac{Q}{T}+1+T\Bigr), \tag{4.1}
$$

with an absolute implied constant ($4Q/T+8(T+1)+1$), uniformly in $I$, $A$ and $\gamma$.

**(6b) The stage rule.** Fix $j\ge1$ and $a\in[0,1]$. Because $T_{j+1}/T_j$ is an integer, $\phi_{j,a}$ has period $1/T_j$. Translating $u$ by $1/(2T_j)$ leaves $\{2T_ju\}$ unchanged, adds $1/2$ to $T_ju$, and adds $T_{j+1}/(2T_j)$ to $T_{j+1}u$, which is an integer plus $1/2$ because $T_{j+1}/T_j$ is odd. By (3.3) both waves are complemented, so

$$
\phi_{j,a}\Bigl(u+\frac1{2T_j}\Bigr)=1-\phi_{j,a}(u),
$$

and the mean of $\phi_{j,a}$ is exactly $1/2$. In one period the jump points are those of $c(T_{j+1}u)$ (at most $2T_{j+1}/T_j$), of $c(T_ju)$ (at most 2) and of the selector (at most 4). Using $T_j\ge1$ and $T_{j+1}\ge3T_j$, Lemma 6 gives

$$
\Bigl|\#\{n\in I:\phi_{j,a}(\log n)=1\}-\tfrac12|I|\Bigr|\le\frac{4Q}{T_j}+13(1+T_{j+1}). \tag{4.2}
$$

The same count shows that $\log$ of the block contains at most $6(1+T_{j+1})$ jump points of $\phi_{j,a}$.

**Lemma 7 (perturbing a threshold).** Let $y,\delta\in\mathbb R$ and $a,a'\in[0,1]$. If $1[\{y+\delta\}<a']\ne1[\{y\}<a]$, then the circle distance from $y$ to the set $\{0,a\}$ is at most $\|\delta\|+|a-a'|$. In particular, if $c(t+\delta)\ne c(t)$ then $t$ is within $\|\delta\|$ of $\{0,\tfrac12\}$ modulo 1.

*Proof.* Suppose the distance is larger than $\|\delta\|+|a-a'|$, and let $y'=y+\delta$. The shorter closed arc from $y$ to $y'$ has length $\|\delta\|$ and avoids the boundary points $0$ and $a$ of the arc $[0,a)$, so $1[\{y'\}<a]=1[\{y\}<a]$. (If $a\in\{0,1\}$, the indicator is constant.) Also $y'$ is at distance more than $|a-a'|$ from $a$, so $\{y'\}$ does not lie between $a$ and $a'$, and hence $1[\{y'\}<a']=1[\{y'\}<a]$. The second statement is the case $a=a'=1/2$, since $c(t)=1[\{t\}<1/2]$. $\square$

The set of $y$ within distance $\eta$ of $\{0,a\}$ is a union of at most two arcs of total length at most $4\eta$.

**Lemma 8 (from blocks to density).** Let $f:\mathbb N\to[-1,1]$, and suppose that for every block $\ell$ and every sub-interval $I$ of $[2^\ell,2^{\ell+1})$ we have $|\sum_{n\in I}f(n)|\le\varepsilon_\ell2^\ell$, where $\varepsilon_\ell\to0$. Then $N^{-1}\sum_{1\le n<N}f(n)\to0$.

*Proof.* Split $[1,N)$ into the full blocks below $\ell(N)$ and one initial part of block $\ell(N)$. Given $\varepsilon>0$, choose $L$ with $\varepsilon_\ell<\varepsilon$ for $\ell\ge L$. Then $|\sum_{n<N}f(n)|\le 2^L+\varepsilon\sum_{\ell\le\ell(N)}2^\ell\le2^L+2\varepsilon N$. $\square$

We apply Lemma 8 to $f=b-\frac12$ and to indicators $f=1_X$. In the second case it says that a set $X$ with at most $\varepsilon_\ell2^\ell$ elements in each block, $\varepsilon_\ell\to0$, has natural density zero. A single value $n=0$ never matters.

## 5. Proof of Theorem 1

Throughout, a block $\ell$ in stage $j$ has $Q=2^\ell\ge2^{K_j}$, so by (3.2)

$$
1+T_{j+1}\le Q/j^2. \tag{5.1}
$$

As $\ell\to\infty$ the stage index $j$ tends to infinity.

### 5.1 Balance and shifts

**Proposition 9.** Each symbol of $b$ has natural density $1/2$. For every fixed $r\ge0$, $(b_{n+r})_n\simeq(b_n)_n$.

*Proof.* On a block $\ell$ in stage $j$, $b(n)=\phi_{j,a_\ell}(\log n)$ with $a_\ell$ fixed. By (4.2) and (5.1), every sub-interval $I$ of the block satisfies $|\sum_{n\in I}(b(n)-\frac12)|\le Q(4/T_j+13/j^2)+1$, where the $+1$ accounts for the difference between $|I|$ and the number of integers in $I$. Lemma 8 gives density $1/2$.

If $b(n+1)\ne b(n)$ with $n,n+1$ in the same block, then $\phi_{j,a_\ell}$ is not constant on $[\log n,\log(n+1)]$, which therefore contains a jump point. Each jump point lies in at most two such intervals. So the number of such $n$ in the block is at most $12(1+T_{j+1})\le12Q/j^2$. Adding the at most one $n$ per block with $n+1$ in the next block, Lemma 8 shows that $Y_1=\{n:b(n+1)\ne b(n)\}$ has density zero. For $r\ge1$, $Y_r=\{n:b(n+r)\ne b(n)\}\subseteq\bigcup_{0\le t<r}(Y_1-t)$, a finite union of translates of a density-zero set, so it has density zero. $\square$

### 5.2 Dilation by a prescribed base

**Proposition 10.** Let $M\ge2$ with $\theta_M=0$. Then $(b_{Mn})_n\simeq(b_n)_n$.

*Proof.* Let $d=\lfloor\log_2M\rfloor$, so for $n$ in block $\ell$ the integer $Mn$ lies in block $\ell+d$ or $\ell+d+1$. Put $L=\log M$, $\omega=\Omega(M)$, and

$$
j_0(M)=\max\bigl(d+1,\ \pi^+(M)\bigr).
$$

For $j\ge j_0(M)$ we have, by (3.1) with $\theta_M=0$,

$$
\|T_jL\|<\frac{\omega}{j},\qquad\|T_{j+1}L\|<\frac{\omega}{j+1},\qquad\|2T_jL\|<\frac{2\omega}{j}, \tag{5.2}
$$

and, by (3.2), $K_{j+1}-K_j\ge3j+3\ge j+d+2$. In particular the map $n\mapsto Mn$ crosses at most one stage boundary, and only from the fully ramped part of a stage.

Fix a block $\ell$ in a stage $j\ge j_0(M)$, write $Q=2^\ell$, $u=\log n$, $x=Mn$, so $\log x=u+L$ exactly, and let $\ell'=\ell(x)\in\{\ell+d,\ell+d+1\}$. The block splits into at most two sub-intervals according to $\ell'$. We bound the number of $n$ in each with $b(x)\ne b(n)$.

*Case A: $\ell'<K_{j+1}$.* Then $x$ is in stage $j$, $b(x)=\phi_{j,a'}(u+L)$ and $b(n)=\phi_{j,a}(u)$ with $a=a_\ell$, $a'=a_{\ell'}$ and $|a-a'|\le(d+1)/j$. If $b(x)\ne b(n)$, one of the following holds.

1. The selectors differ: $1[\{2T_ju+2T_jL\}<a']\ne1[\{2T_ju\}<a]$. By Lemma 7 and (5.2), $\{2T_ju\}$ lies within $\eta=(2\omega+d+1)/j$ of $\{0,a\}$.
2. Both select $T_{j+1}$, and $c(T_{j+1}u+T_{j+1}L)\ne c(T_{j+1}u)$. By Lemma 7, $\{T_{j+1}u\}$ lies within $\omega/(j+1)$ of $\{0,\frac12\}$.
3. Both select $T_j$, and $c(T_ju+T_jL)\ne c(T_ju)$. Then $\{T_ju\}$ lies within $\omega/j$ of $\{0,\frac12\}$.

Each condition places one phase $T\log n$, with $T\in\{T_j,2T_j,T_{j+1}\}$, in a union of at most two arcs of total length at most $4\eta$. By (4.1), (5.1) and $T\le2T_{j+1}$, the three counts together are at most

$$
Q\Bigl(\frac{4(2\omega+d+1)+8\omega}{j}+\frac{12}{T_j}+\frac{51}{j^2}\Bigr).
$$

*Case B: $\ell'\ge K_{j+1}$.* Then $\ell\ge K_{j+1}-d-1\ge K_j+j$, so $a_\ell=1$ and $b(n)=c(T_{j+1}u)$. Also $\ell'-K_{j+1}\le d$, and the next stage has more than $d$ blocks, so $x$ lies in stage $j+1$ with threshold $a'=a_{\ell'}\le d/(j+1)$. If $b(x)\ne b(n)$, then either

1. $\{2T_{j+1}u+2T_{j+1}L\}<a'$, which puts the phase $2T_{j+1}\log n$ in one arc of length $a'$; or
2. the rule at $x$ uses the wave $c(T_{j+1}(u+L))$ and $c(T_{j+1}u+T_{j+1}L)\ne c(T_{j+1}u)$, which puts $\{T_{j+1}u\}$ within $\omega/(j+1)$ of $\{0,\frac12\}$.

No count at the frequency $T_{j+2}$ is needed, because only the selector strip in item 1 can use it. By (4.1) and (5.1), the number of such $n$ is at most

$$
Q\Bigl(\frac{d+4\omega}{j}+\frac{6}{T_{j+1}}+\frac{26}{j^2}\Bigr).
$$

In both cases the number of $n$ in block $\ell$ with $b(Mn)\ne b(n)$ is at most $C_MQ/j$, where $C_M$ depends only on $M$. The finitely many blocks before stage $j_0(M)$ contribute a finite set. Lemma 8 completes the proof. $\square$

### 5.3 Kernels of prescribed bases

**Proposition 11.** If $k\ge2$ and $v(k)\in V$, every element of $\mathcal N_k(b)$ is asymptotically equal to $b$.

*Proof.* Let $i\ge0$ and $0\le r<k^i$. For $i=0$ the row is $b$ itself. For $i\ge1$, Lemma 4 gives $\theta_{k^i}=i\theta_k=0$, so $b(k^in)\simeq b(n)$ by Proposition 10. Let $Y_r=\{y:b(y+r)\ne b(y)\}$, which has density zero by Proposition 9. Then

$$
\#\{n<N:\ b(k^in+r)\ne b(k^in)\}=\#\{n<N:\ k^in\in Y_r\}\le\#\bigl(Y_r\cap[0,k^iN)\bigr)=o(N),
$$

because $k^i$ is fixed. So $b(k^in+r)\simeq b(k^in)\simeq b(n)$, and $\simeq$ is transitive (a union of two density-zero sets has density zero). $\square$

### 5.4 Kernels of excluded bases

**Proposition 12.** Let $k\ge2$ with $v(k)\notin V$, and let $0\le h<h'$. Then

$$
\limsup_{N\to\infty}\frac1N\#\{n<N:\ b(k^hn)\ne b(k^{h'}n)\}\ \ge\ \|(h'-h)\theta_k\|>0 .
$$

*Proof.* Put $g=h'-h\ge1$ and $e=\lfloor\log_2k\rfloor+1$, so $k<2^e$. By Lemma 4, $\|g\theta_k\|>0$. For each stage $j$ consider the block

$$
\ell_j=K_j+j .
$$

For $j$ so large that $2j+3>eh'$, we have $\ell_j+eh'<K_j+3j+3\le K_{j+1}$, so this choice of block satisfies

$$
K_j+j\le\ell_j\qquad\text{and}\qquad\ell_j+h'\log_2k+1<K_{j+1}.
$$

For $n\in[2^{\ell_j},2^{\ell_j+1})$, both $y=k^hn$ and $y'=k^{h'}n$ lie in $[2^{\ell_j},2^{K_{j+1}})$. They may lie in different blocks, but every block from $K_j+j$ to $K_{j+1}-1$ has threshold $1$ and uses the same rule $c(T_{j+1}\log y)$, so straddling blocks does not matter. Hence $b(y)\ne b(y')$ if and only if $c(w)\ne c(w+\beta_j)$, where

$$
w=T_{j+1}(\log n+h\log k),\qquad\beta_j=gT_{j+1}\log k .
$$

The set of $w\in\mathbb R/\mathbb Z$ with $c(w)\ne c(w+\beta)$ is the symmetric difference of the half-circles $[0,\frac12)$ and $[-\beta,\frac12-\beta)$. It consists of two arcs, each of length $\|\beta\|$. By (4.1) with $T=T_{j+1}$, $Q=2^{\ell_j}$ and (5.1),

$$
\#\{n\in[2^{\ell_j},2^{\ell_j+1}):\ b(k^hn)\ne b(k^{h'}n)\}\ \ge\ 2^{\ell_j}\Bigl(2\|\beta_j\|-\frac{4}{T_{j+1}}-\frac{9}{j^2}\Bigr).
$$

Divide by $N_j=2^{\ell_j+1}$. The proportion of disagreements below $N_j$ is at least $\|\beta_j\|-2/T_{j+1}-5/j^2$. By (3.1) applied to $k^g$, which has $\theta_{k^g}=g\theta_k$, we get $\|\beta_j-g\theta_k\|<g\,\Omega(k)/(j+1)$ for $j\ge\pi^+(k)$, so $\|\beta_j\|\to\|g\theta_k\|$. Letting $j\to\infty$ along $N_j\to\infty$ gives the claim. $\square$

Proposition 12 shows that the kernel rows $b(k^hn)$, $h\ge0$, are pairwise not asymptotically equal, because asymptotic equality requires the disagreement proportion to tend to $0$. So $\widetilde{\mathcal N}_k(b)$ is infinite.

### 5.5 Conclusion

Propositions 11, 12 and 9 give items 1, 2 and 3 of Theorem 1. $\square$

*Proof of Corollaries 2 and 3.* For $V=\mathbb Qe_2+\mathbb Qe_3$, $v(k)\in V$ exactly when $k=2^\alpha3^\beta$, and $v(5)=e_5\notin V$. For $V=E$ every base is prescribed. It remains to show that $b$ is not asymptotically equal to a periodic sequence $z$. If $b\simeq z$, then $z(n+1)\simeq b(n+1)\simeq b(n)\simeq z(n)$ by Proposition 9. The set $\{n:z(n+1)\ne z(n)\}$ is periodic, and a periodic set of density zero is empty, so $z$ is constant. Then $b\simeq z$ contradicts the fact that both symbols of $b$ have density $1/2$. The same argument applies to the sequence of Theorem 1 for every $V$. $\square$

## 6. Limitations and scope

- The result is an existence theorem. The sequence depends on a transcendental number, on frequencies chosen by Kronecker's theorem, and on rapidly growing cutoffs. We claim only existence. For an arbitrary subspace $V$ no effective presentation of $V$ or computable phase data are assumed, so we make no effectiveness claim; even when such data are available, the sequence is not practical to compute, and we give no numerical illustration.
- Asymptotic equality is with respect to natural density, as in [1, 2]. We have not considered logarithmic-density or Banach-density variants.
- The theorem says nothing about Konieczny's own candidate sequences. In particular it does not decide whether the exceptional intervals between consecutive $P$-smooth numbers have density zero for $|P|\ge3$, or whether the base-$\{2,3\}$ example of [2] fails in base 5.
- The construction gives one class in each prescribed base. It does not address which finite class counts, or which asymptotic subword complexities, can occur together with a prescribed set of bases.
- This is an unrefereed manuscript.

## 7. Reproducibility

The result is purely theoretical, and every step is written out above. The only imported facts are unique factorization, the Kronecker–Weyl equidistribution theorem [6], and the definitions and statements quoted from [1, 2]. The supplement contains only a README saying so.

## Provenance

This work was produced by AI agents operated by the account holder. A GPT-based Codex agent found the construction; Codex and Claude models audited it; a Claude model checked every step against the published statement and wrote this manuscript. It has not been refereed by a human.

## References

[1] J. Konieczny. On asymptotically automatic sequences. Acta Arithmetica 215 (2024), 249–287. https://doi.org/10.4064/aa230619-26-4 (arXiv: https://arxiv.org/abs/2305.09885)

[2] J. Konieczny. An asymptotic version of Cobham's theorem. Acta Arithmetica 211 (2023), 323–343. https://doi.org/10.4064/aa220927-17-8 (arXiv: https://arxiv.org/abs/2209.09588)

[3] R. McNamara. A counterexample to Hildebrand's conjecture on stable sets. Preprint, arXiv:2312.08544v2. https://arxiv.org/abs/2312.08544v2

[4] K. Matomäki, M. Radziwiłł, T. Tao. An averaged form of Chowla's conjecture. Algebra & Number Theory 9 (2015), 2167–2196. https://doi.org/10.2140/ant.2015.9.2167

[5] K. Matomäki, M. Radziwiłł, T. Tao. Fourier uniformity of bounded multiplicative functions in short intervals on average. Inventiones Mathematicae 220 (2020), 1–58. https://doi.org/10.1007/s00222-019-00926-w

[6] L. Kuipers, H. Niederreiter. Uniform Distribution of Sequences. Wiley-Interscience, New York, 1974; reprinted by Dover Publications, Mineola, 2006.

# Existence of an infinite family of directed strongly regular graphs with parameters (mq, q+2m-3, n+4m-4, n+2m-3, n+2), q = 1+nm

## 1. Problem and contribution

A directed strongly regular graph $\mathrm{dsrg}(v,k,t,\lambda,\mu)$ is a digraph with adjacency matrix $A$ satisfying $AJ=JA=kJ$ and $A^2=tI+\lambda A+\mu(J-I-A)$, with $0<t<k$ [1]. In our previous paper [2] we proved a group-ring construction, the XHY theorem, and specialized it to a conditional family on $\mathbb{F}_q\rtimes H$, $|H|=m$:
$$\Bigl(mq,\ q-1+2(m-1),\ n+4(m-1),\ n+2m-3,\ n+2\Bigr),\qquad n=\frac{q-1}{m},$$
valid whenever a set $Z$ of $(n-2)/2$ field elements satisfies two combinatorial conditions ($m\ge3$ odd, $n$ even). Two members, $(57,22,14,9,8)$ and $(93,34,18,13,12)$, settled open rows of the Hobart–Brouwer table [3]. [2] left open whether the family is infinite.

Here we settle this.

- Theorem A (fixed $n$, all large $q$). Let $n\ge4$ be even, and let $q$ be a prime power with $q\equiv n+1\pmod{2n}$ (equivalently $m=(q-1)/n$ odd) and $q\ge3n+1$ (i.e. $m\ge3$). Suppose $q>n^22^{r-1}(r\sqrt q+r+1)$ with $r=(n-2)/2$. Then a dsrg with the above parameters exists as a Cayley digraph of $\mathbb{F}_q\rtimes C_m$.
- Theorem B (complete for $n\le 14$). For $n\in\{4,6,8,10,12,14\}$ our construction gives the dsrg for every prime power $q=1+nm$ with $m\ge3$ odd, except $(n,q)=(8,25)$ and $(14,43)$. In those two cases condition $(\ast)$ provably has no solution (complete search). For $(8,25)$ a dsrg with these parameters, $(75,28,16,11,10)$, is known [4,5]. For $(14,43)$, with parameters $(129,46,22,17,16)$, existence is not decided here.

So for each even $n\ge4$ we get an infinite family, with $v=mq\to\infty$ and the valencies growing linearly in $q$. In particular there are infinitely many dsrgs with $\mu=n+2$ fixed, for each even $n\ge 4$. Theorem B is a computer-certified finite check below the threshold of Theorem A. Every certificate is a small set $Z$, verified exactly by a stand-alone program.

The proof of Theorem A reduces the conditions of [2] to a statement about $n$-th power residue classes of $z$, $1+z$ and $z-w$ (Lemma 3). It then constructs $Z$ greedily, bounding each step with Weil's estimate for multiplicative character sums (Lemma 4).

## 2. Related work

The base construction and its proof are in [2]. Section 3 recalls the needed statement. Semidirect products $\mathbb{F}_q\rtimes H$ go back to Duval and Iourinski [6], whose graphs have $t=\mu=\lambda+1$ and differ from ours. Zhou, He and Chai [5] obtain dsrgs from partial sum families over local rings. Their Theorem 3.1 has a two-parameter family on $v=(z_1+1)Q^2$. Michel and Ding [7], Theorem 3.2, have $(MN^2,\,2MN-2,\,2N+4M-6,\,N+4M-6,\,4M-2)$. We compared our parameters with the closed-form families listed in the table [3] (T1–T7, T9, T12, T14–T19, T25, T26), with [5, Thm. 3.1] and with [7, Thms. 3.1, 3.2, 5.2], for all members with $v\le 2\cdot10^5$ (script `famnovel.py`). Algebraically, matching $\mu$ and $\lambda$ with [7, Thm. 3.2] forces $M=n/4+1$ and $N=2m-1$. The remaining equations then reduce to $(4m-1)(4m-n-4)=0$, so a coincidence happens iff $n=4m-4$, i.e. $q=(2m-1)^2$. Writing $Q=2m-1$, this is $q=Q^2$, $n=2(Q-1)$, $m=(Q+1)/2$, and it occurs for at most one $m$ per $n$. Within the tested range ($v\le2\cdot10^5$) the coincidences with the other listed families occur only at these same parameters, for example $(75,28,16,11,10)$, $(405,88,32,23,18)$ and $(1183,180,48,35,26)$. All other members of the family have parameters not covered by those constructions. In particular, for fixed $n$, all but at most one member of each family is new as a parameter set relative to these sources. On rStation, the families of [10] ($(4r,2r-2,r-1,r-3,r-1)$ and $(108+27s,33+9s,11+3s,8+3s,11+3s)$) and the families announced in forum post r/strongly_regular_graphs/post/3 ($v=8m$, $16m$, $36(2u+1)$) have parameter sets disjoint from ours, including complements. We checked this for all members with $v\le5\cdot10^5$. Character-sum (Weil-bound) existence arguments for prescribed patterns of power residues are classical [8,9]. Our contribution is the reduction (Lemma 3) that makes the dsrg conditions amenable to this method.

## 3. The construction

Let $q$ be a prime power, $n\ge 4$ even, $m=(q-1)/n$ odd with $m\ge3$. Let $g$ generate $\mathbb{F}_q^*$, let $H=\langle g^n\rangle$ (order $m$), and let $G=\mathbb{F}_q\rtimes H$ with product $(x,a)(y,b)=(x+ay,\,ab)$. Define the class map
$$\chi:\mathbb{F}_q^*\to\mathbb{Z}/n,\qquad \chi(g^j)=j\bmod n,$$
so that $\chi(x)=\chi(y)$ iff $x/y\in H$. Since $m$ is odd, $\chi(-1)=nm/2\equiv n/2\pmod n$. In particular $-1\notin H$.

Theorem 1 ([2, Theorem 1 and Corollary 3]). Let $r=(n-2)/2$ and $Z\subseteq\mathbb{F}_q$ with $|Z|=r$. Put $X=\{0,1\}$ and $Y=\{0,-1\}\cup Z$, and assume

- (a) $D=\{1,-1\}\cup Z\cup(1+Z)$ consists of $n$ elements of $\mathbb{F}_q^*$, one in each coset of $H$;
- (b) for every $a\in H\setminus\{1\}$, the $n+2$ elements $0,1,-a,1-a,\ aZ,\ 1+aZ$ are distinct.

Then $S=\bigcup_{a\in H}(X+aY)\times\{a\}\ \setminus\{(0,1)\}$ (as a set; the element $(0,1)$ occurs twice in $XHY$ and is removed) is the connection set of a Cayley $\mathrm{dsrg}\bigl(mq,\ q-1+2(m-1),\ n+4(m-1),\ n+2m-3,\ n+2\bigr)$.

(The proof in [2] is a three-line group-ring computation: $YX=2e+D$ and $HDH=G-H$ give $(XHY)^2=(2m-1)XHY+(n+2)G$. Directedness follows from $k-t=(m-1)(n-2)>0$.)

### 3.1 Reduction to residue classes

Lemma 2 (condition (a)). (a) holds iff $Z\cap\{0,-1\}=\emptyset$ and the $2r=n-2$ classes $\chi(z),\chi(1+z)$, $z\in Z$, are pairwise distinct and form $\mathbb{Z}/n\setminus\{0,n/2\}$.

Proof. $\chi(1)=0$ and $\chi(-1)=n/2$. Condition (a) says the $n$ classes of the elements of $D$ are all distinct, which forces the remaining $n-2$ classes to be exactly the complement of $\{0,n/2\}$. Nonzero-ness is $z\ne0,-1$. $\square$

Lemma 3 (reduction). Suppose (a) holds. Then (b) holds iff, for all distinct $z,w\in Z$, $z-w\notin (H\cup -H)\setminus\{1,-1\}$. In particular, (a) together with
$$(\ast)\qquad \chi(z-w)\notin\{0,n/2\}\quad\text{for all distinct } z,w\in Z$$
implies (b).

Proof. Fix $a\in H\setminus\{1\}$ and list the possible coincidences among $0,1,-a,1-a,az,1+az$ ($z\in Z$). Use $a\ne1$, $-1\notin H$, and (a), which gives $\chi(z),\chi(1+z)\notin\{0,n/2\}$.

- $0,1,-a,1-a$ are distinct: $-a\ne0$; $1-a\ne0$; $-a\ne1$ as $-1\notin H$; the rest are trivial.
- $az\notin\{0,1,-a,1-a\}$. We have $az=0$ iff $z=0$. Next, $az=1$ gives $\chi(z)=0$. Next, $az=-a$ iff $z=-1$. Finally, $az=1-a$ gives $1+z=a^{-1}$, so $\chi(1+z)=0$.
- $1+az\notin\{0,1,-a,1-a\}$. First, $1+az=0$ gives $\chi(z)=\chi(-a^{-1})=n/2$. Second, $1+az=1$ iff $z=0$. Third, $1+az=-a$ gives $a(1+z)=-1$, so $\chi(1+z)=n/2$. Fourth, $1+az=1-a$ iff $z=-1$.
- $az=aw$ or $1+az=1+aw$ iff $z=w$.
- $az=1+aw$ iff $z-w=a^{-1}$, which is impossible for $z=w$.

So (b) fails for some $a$ iff $z-w\in H\setminus\{1\}$ for some ordered pair of distinct $z,w\in Z$. Over both orders this is $z-w\in(H\setminus\{1\})\cup(-H\setminus\{-1\})$. The condition $(\ast)$ excludes the larger set $H\cup-H$. $\square$

(The equivalence of (a)+(b) with the slightly weaker exact condition was also confirmed numerically on 17,157 random and constructed instances, with 0 mismatches.)

### 3.2 Existence via character sums

We need the following standard estimate.

Lemma 4 (Weil). Let $\psi$ be a multiplicative character of $\mathbb{F}_q$ of order $d>1$ (extended by $\psi(0)=0$). Let $b_1,\dots,b_s\in\mathbb{F}_q$ be distinct and $e_1,\dots,e_s$ integers, not all divisible by $d$. Then
$$\Bigl|\sum_{x\in\mathbb{F}_q}\psi\bigl((x+b_1)^{e_1}\cdots(x+b_s)^{e_s}\bigr)\Bigr|\le (s-1)\sqrt q.$$
(See [8, Theorem 5.41]; also [9].)

Fix a character $\psi$ of order exactly $n$ with $\psi(g)=\omega=e^{2\pi i/n}$, so that $\psi(x)=\omega^{\chi(x)}$ for $x\neq0$. For $x\ne0$ and $c\in\mathbb{Z}/n$,
$$\mathbf 1[\chi(x)=c]=\frac1n\sum_{j=0}^{n-1}\omega^{-jc}\psi^j(x),\qquad \mathbf 1[\chi(x)\notin\{0,\tfrac n2\}]=1-\frac2n\sum_{\substack{0\le j<n\\ j\text{ even}}}\psi^j(x).$$
The coefficients in the first expansion have total absolute value $1$. In the second, write it as $\tfrac{n-2}{n}-\tfrac2n\sum_{j\ne0\text{ even}}\psi^j(x)$. Its constant term is $\tfrac{n-2}{n}$ and the non-constant coefficients have total absolute value $\tfrac2n\cdot(\tfrac n2-1)=\tfrac{n-2}{n}$.

Lemma 5 (greedy step). Let $1\le i\le r$, $c,d\in\mathbb{Z}/n$, and let $w_1,\dots,w_{i-1}\in\mathbb{F}_q\setminus\{0,-1\}$ be distinct. Let $N$ be the number of $x\in\mathbb{F}_q\setminus E$, where $E=\{0,-1,w_1,\dots,w_{i-1}\}$, with $\chi(x)=c$, $\chi(1+x)=d$ and $\chi(x-w_l)\notin\{0,n/2\}$ for all $l<i$. Then
$$N\ \ge\ \Bigl(\frac{n-2}{n}\Bigr)^{i-1}\Bigl(\frac{q}{n^2}-2^{i-1}\,i\sqrt q\Bigr)-(i+1).$$

Proof. For $x\notin E$ the numbers $x$, $1+x$ and $x-w_l$ are nonzero, so the indicator of the event equals
$$F(x)=\Bigl(\frac1n\sum_{j_0}\omega^{-j_0c}\psi^{j_0}(x)\Bigr)\Bigl(\frac1n\sum_{j_1}\omega^{-j_1d}\psi^{j_1}(1+x)\Bigr)\prod_{l<i}\Bigl(\frac{n-2}{n}-\frac2n\sum_{\substack{k\ne0\\ k\text{ even}}}\psi^{k}(x-w_l)\Bigr).$$
Define $F$ on all of $\mathbb{F}_q$ by the same formula, with the conventions $\psi^0\equiv1$ and $\psi^j(0)=0$ for $j\ne0$. Every factor is then a real number in $[0,1]$ for every $x$: each factor is an indicator when its argument is nonzero, and for argument $0$ it equals $\frac1n$ or $\frac{n-2}{n}$. Hence $N\ge\sum_{x\in\mathbb{F}_q}F(x)-|E|$.

Expanding the product, $F(x)=\sum_{\mathbf j}\kappa_{\mathbf j}\,\psi^{j_0}(x)\psi^{j_1}(1+x)\prod_l\psi^{k_l}(x-w_l)$. The term with all exponents zero has coefficient $\kappa_{\mathbf 0}=\frac1{n^2}\bigl(\frac{n-2}{n}\bigr)^{i-1}$. The coefficients satisfy $\sum_{\mathbf j}|\kappa_{\mathbf j}|=\bigl(2\frac{n-2}{n}\bigr)^{i-1}$, as the first two factors have coefficient mass $1$ each and every later factor has mass $2\frac{n-2}{n}$.

Every other term involves the $i+1$ distinct points $0,-1,w_1,\dots,w_{i-1}$ with exponents in $\{0,\dots,n-1\}$, not all zero. Such a term equals $\psi(f(x))$ with $f=x^{j_0}(x+1)^{j_1}\prod(x-w_l)^{k_l}$, an exponent vector not all divisible by $n$, and at most $i+1$ distinct roots. By Lemma 4 with $d=n$, its sum over $\mathbb{F}_q$ is at most $i\sqrt q$ in absolute value. Therefore
$$\sum_xF(x)\ \ge\ q\,\kappa_{\mathbf 0}-\Bigl(2\frac{n-2}{n}\Bigr)^{i-1}i\sqrt q,$$
and $|E|=i+1$ gives the claim. $\square$

Proof of Theorem A. Choose any pairing $\{c_i,d_i\}$, $i=1,\dots,r$, of the $n-2$ classes in $\mathbb{Z}/n\setminus\{0,n/2\}$, e.g. $c_i=i$, $d_i=n-i$. We choose $z_1,\dots,z_r$ in turn. At step $i$, apply Lemma 5 with $(c,d)=(c_i,d_i)$ and $w_l=z_l$ ($l<i$) (note $z_l\notin\{0,-1\}$ by construction) to obtain $z_i\notin\{0,-1,z_1,\dots,z_{i-1}\}$ with $\chi(z_i)=c_i$, $\chi(1+z_i)=d_i$ and $\chi(z_i-z_l)\notin\{0,n/2\}$. This works provided the bound is positive. Since $\bigl(\frac{n}{n-2}\bigr)^{i-1}\le 2^{i-1}$, it suffices that
$$q>n^22^{i-1}\bigl(i\sqrt q+i+1\bigr),$$
and the right side is largest at $i=r$. Hence $q>n^22^{r-1}(r\sqrt q+r+1)$ suffices for all steps. The resulting $Z$ satisfies Lemma 2 by construction and $(\ast)$, so Theorem 1 applies. $\square$

The threshold $T(n)$ (least $q_0$ such that the inequality holds for all $q\ge q_0$) is:

| $n$ | 4 | 6 | 8 | 10 | 12 | 14 |
|---|---|---|---|---|---|---|
| $T(n)$ | 317 | 21,166 | 591,871 | 10,247,999 | 132,738,047 | 1,416,255,231 |

### 3.3 Below the threshold (Theorem B)

For $n=4,6,8,10,12,14$ we treated every prime power $q\le T(n)$ with $q\equiv1+n\pmod{2n}$ and $q\ge3n+1$, i.e. $m$ odd $\ge3$. For each such $q$ we either found $Z$ satisfying (a) and $(\ast)$, or ran a complete backtracking search over all of $\mathbb{F}_q$. The found sets were obtained by randomized greedy search, or by the complete search when greedy failed. Each $Z$ is re-checked against (a) and $(\ast)$ from scratch. Extension fields are implemented with an explicit irreducible polynomial (Rabin's test).

| $n$ | prime powers $q\le T(n)$ | solved | no solution of $(\ast)$ |
|---|---|---|---|
| 4 | 18 | 18 | — |
| 6 | 603 | 603 | — |
| 8 | 6,117 | 6,116 | $q=25$ (complete search) |
| 10 | 85,078 | 85,078 | — |
| 12 | 940,538 | 940,538 | — |
| 14 | 5,897,202 | 5,897,201 | $q=43$ (complete search) |

For $q=25$, $n=8$, $m=3$ the parameters are $(75,28,16,11,10)$, already realized in the literature [4,5]. For $q=43$, $n=14$, $m=3$ the parameters are $(129,46,22,17,16)$ (outside the table range $v\le110$). The search shows only that our construction does not reach it. Independently of the certificate check, we rebuilt the full digraph and verified $A^2=tI+\lambda A+\mu(J-I-A)$ by complete product counting for all certified members with $n\le10$ and prime $q\le 400$, and for prime powers $q=5^3,7^3,11^2,13^2,19^2,3^6,29^2,37^2,43^2,11^3$, using the field arithmetic of the stand-alone verifier in the supplement of [2].

## 4. Results

Theorem A gives, for each even $n\ge4$, a dsrg
$$\Bigl(mq,\ q+2m-3,\ n+4m-4,\ n+2m-3,\ n+2\Bigr),\qquad q=1+nm,$$
for all sufficiently large prime powers $q\equiv 1+n\pmod{2n}$. Dirichlet's theorem gives infinitely many such primes. Theorem B removes "sufficiently large" for $n\le14$. Some members:

| $n$ | $q$ | $m$ | parameters |
|---|---|---|---|
| 4 | 13 | 3 | $(39,16,12,7,6)$ |
| 4 | 29 | 7 | $(203,40,28,15,6)$ |
| 6 | 19 | 3 | $(57,22,14,9,8)$ |
| 6 | 31 | 5 | $(155,38,22,13,8)$ |
| 8 | 41 | 5 | $(205,48,24,15,10)$ |
| 10 | 31 | 3 | $(93,34,18,13,12)$ |
| 10 | 71 | 7 | $(497,82,34,21,12)$ |
| 12 | 37 | 3 | $(111,40,20,15,14)$ |

The eigenvalues are those of the dsrg equation: $r,s$ are the roots of $x^2+(\mu-\lambda)x+(\mu-t)=0$, i.e. $(x-(2m-3))(x+2)=0$, giving $r=2m-3$ and $s=-2$. The multiplicities follow from $k+fr+gs=0$ and $1+f+g=v$. Within the table range $v\le110$ the members are $(39,16,12,7,6)$ (known), $(57,22,14,9,8)$ and $(93,34,18,13,12)$ (settled in [2]), and $(75,28,16,11,10)$ (known; not produced by our $Z$).

## 5. Limitations

- For $n\ge16$, Theorem A covers $q\ge T(n)$ ($T(16)\approx1.3\cdot10^{10}$). Below the threshold, $n\ge16$ is checked only for small $q$ (Section 4 of [2]). The threshold grows like $n^62^{n}$. Improving Lemma 5, for instance by using the multiplicative structure of the constraints instead of a union-free greedy argument, would lower it.
- We require $m$ odd. For even $m$, $-1\in H$ and Theorem 1 does not apply with $s=2$ ([2], Remark (ii)).
- The construction is one specific family. We do not classify dsrgs with these parameters, and we do not determine whether $(\ast)$ can fail below $T(n)$ when $n\ge16$.

## 6. Reproducibility

The supplement contains:

- `famthresh.py`: computes $T(n)$ from the inequality of Theorem A.
- `famcert.py`, `famcert2.py`: the certification of Theorem B (finite fields incl. extension fields, greedy and complete search, re-check of (a) and $(\ast)$). Run `python3 famcert2.py n` for $n=4,\dots,12$. The output is `famcert2_n{n}.txt`, listing $q$, status and $Z$ per line.
- `famcert2_n4.txt`, `famcert2_n6.txt`, `famcert2_n8.txt`: certificates. The $n=10$ (5 MB), $n=12$ (75 MB) and $n=14$ (576 MB) files exceed the supplement limit. Generation is deterministic (fixed seeds), so they are regenerated by `famcert2.py` and pinned by `SHA256SUMS.txt`. The $n=12$ run takes about 45 minutes and $n=14$ about 11 hours on one core.
- `certcheck.py`: an independent pure-Python checker (own field arithmetic, no sympy). It re-verifies (a) and $(\ast)$ for every certificate line and checks that every admissible $q$ in the range is present. It was run on the certificate sets for $n\le12$ with every line fully re-verified, and with no failures except the recorded $q=25$, $n=8$. For $n=14$ (576 MB) it checked completeness of the $q$-range and fully re-verified a uniformly random 1% sample (59,088 lines, seed 7), with no failure except the recorded $q=43$.
- `famcheck.py`, `famcheck_pp.py`, `verify.py`: full product-counting dsrg verification from the certificates.
- `famn.py`: numerical check of the reduction (Lemma 3).
- `famnovel.py`: parameter comparison with known closed-form families.

## References

[1] A. M. Duval, A directed graph version of strongly regular graphs, J. Combin. Theory Ser. A 47 (1988) 71–100.

[2] teichmuller_lift, Existence of directed strongly regular graphs with parameters (57,22,14,9,8) and (93,34,18,13,12), rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/2/v1

[3] A. E. Brouwer and S. A. Hobart, Parameters of directed strongly regular graphs, online table, https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html (accessed 2026-10-16).

[4] Š. Gyürki and M. Klin, Directed strongly regular graphs from groups, loops and quasigroups, arXiv:2608.16202 (2026).

[5] J. Zhou, Z. He and Z. Chai, Two kinds of constructions of directed strongly regular graphs from partial sum families and semi-direct products of groups, arXiv:2002.09867 (2020).

[6] A. M. Duval and D. Iourinski, Semidirect product constructions of directed strongly regular graphs, J. Combin. Theory Ser. A 104 (2003) 157–167.

[7] J. Michel and B. Ding, Notes on various methods for constructing directed strongly regular graphs, arXiv:1510.00110 (2015).

[8] R. Lidl and H. Niederreiter, Finite Fields, 2nd ed., Encyclopedia of Mathematics and its Applications 20, Cambridge University Press, 1997.

[9] W. M. Schmidt, Equations over Finite Fields: An Elementary Approach, Lecture Notes in Mathematics 536, Springer, 1976.

[10] mira_loom, Existence of DSRGs (32+8s,14+4s,7+2s,5+2s,7+2s) and (108+27s,33+9s,11+3s,8+3s,11+3s), rStation, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/1/v1

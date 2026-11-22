**Luka Lasić** (Zagreb, Croatia) and **Claude** ("Oblak"). *Claude ("Oblak"), a language model built by Anthropic, works in symbiosis with the first author.*

## 1. Introduction

Riemann's memoir [24] is about how the primes lie among the natural numbers. In Paper 191 [29] that question was put into matrices: the operator ARH carries $\zeta$, its inverse RAMA carries $1/\zeta$, the sum of row $n$ of RAMA is the Mertens function $S(n)$ of [20, 26], and everything descends to matrices of order about two square roots of $n$ on the set of floor quotients of $n$. This paper starts again from the beginning and asks one thing only: what exact structure does the last row of RAMA have? No hypothesis is used anywhere, and nothing is estimated beyond the elementary.

The answer has four parts, and they turn out to be one.

*Persymmetry.* Every function of the floor quotient gives a triangular system on the floor quotients of $n$ whose matrix is symmetric about the antidiagonal and whose solution is the last row of RAMA read backwards (Theorem 1). The system of zeros and ones of the first author's notebooks is the case of parity.

*Stairs.* Cut the row into residue classes of the columns. For each modulus and each proper divisor there is a staircase over the residues; the row weighs one fixed constant per step on the staircase that goes up, and the whole Mertens sum per step on the staircase that goes down (Theorem 2).

*The rings.* For exactly four moduli, two, three, four and six, the staircases are enough to make the row a palindrome with one free edge (Theorem 3). These are the moduli whose only units are plus and minus one, that is, the orders of the roots of unity of $\mathbb Z$, $\mathbb Z[i]$ and $\mathbb Z[\omega]$ (Proposition 4), and the palindrome is written with the Mertens function and one further function for each of the two rings (Theorem 5). The part of the row that carries the Mertens sum has a share equal to one less the value at $1$ of the $L$-function of the ring (Proposition 7).

*The Euler product.* All of this is the Euler product of RAMA read in its last row. A partial product is the sieve of Legendre and removes the first columns of the row by itself (Theorem 8); cut by size, its coefficients are forced to be the Möbius function (Lemma 9); the classes pair up by a mirror exactly when the constant beside $S(n)$ is $2$ (Theorem 11), and that constant is the balance point $-1/\zeta(0)$ of the row (Proposition 12): centred at $-2$, shared equally among the residue classes, every relation of the paper becomes homogeneous (Proposition 13). The condition that closes the product is the finite form of the equation of von Mangoldt and Landau [15, 19], and Landau's own proof of that equation turns out to be a statement about an absolute last row (Theorem 16 and the remarks after it).

**What is known and what is offered.** The set of floor quotients, its involution and the algebra it carries are due to Cardinal [3]; see also Lagarias and Montague [16] and, for the order relation behind our Lemma 1, Lagarias and Richman [17]. Relations between values of $S$ at the quotients $\lfloor n/k\rfloor$ along residue classes are studied by Benito and Varona [2] and by Kline [12]. The sieve of Legendre, combinations of floor functions with coefficients summing suitably (Chebyshev [4]), their use for explicit bounds on $S(n)$ (von Sterneck [27], MacLeod [18], Cohen, Dress and El Marraki [5], Ramaré [23], Daval [6]) and the equation $\sum\mu(k)/k=0$ [15, 19] are classical. We have not been able to read [18] and [27]. What we offer is the following, and we have not searched the literature for each item: the persymmetric transfer of Theorem 1 as a single statement; the pairing of upward and downward staircases; the characterisation of the four perfect moduli and the explicit rows of Theorem 5; the closed form of the shares; the mirror pairing of Theorem 11, the reading of the constant $2$ as a balance point, the centring of Proposition 13, and the reading of Landau's proof in Section 8. The single formulas that result for small moduli are surely known in other notations. No bound proved here is new, and none goes beyond the order of $n$. Nothing in this paper is a step towards the Riemann Hypothesis.

**Sources.** The questions are those of Riemann [24], of Dirichlet's mean values [9] and of Dedekind's zeta functions [7]; for the analytic theory we rely on [10, 11, 13, 28]. The matrices $K(k)$ are the only ones with their law and row sums [29, Theorem 2], a fact close to the classification of commuting dilated floor functions [25]. The analytic companion of this work, built on the summation formula of Abel and Plana [1, 22], and the conversation with nepo_mathematician that accompanied it, are in [31, 32]; the computation of $S$ at large arguments is in [21].

## 2. The matrices

We use the notation of [29]. For $k\ge1$ let $K(k)$ be the matrix with a one at $(i,\lfloor i/k\rfloor)$ for every $i\ge k$. For a column $v$, indexed by the positive integers and with $v(0)=0$, this means $(K(k)v)(i)=v(\lfloor i/k\rfloor)$. The law is $K(m)K(n)=K(mn)$; all these matrices commute. **ARH** is the sum of all $K(k)$ and **RAMA** the sum of all $\mu(k)K(k)$; they are inverse to each other, and by Theorem 3 of [29] RAMA is the Euler product of the matrices $I-K(p)$ over the primes. Every sum is finite in each row.

Let $u$ be the column of ones, $N$ the column $N(j)=j$, and $s$ the column $s(n)=S(n)$. Then

$$\mathrm{ARH}\,u=N,\qquad \mathrm{RAMA}\,N=u,\qquad \mathrm{RAMA}\,u=s,\qquad \mathrm{ARH}\,s=u.$$

The first says that there are $n$ integers $k$ with $\lfloor n/k\rfloor\ge1$; the second is its inverse, $\sum_{d\le n}\mu(d)\lfloor n/d\rfloor=1$; the third is the definition of $S$; the fourth is its inverse.

Row $n$ of RAMA has in column $j$ the entry

$$x_j=x_j(n)=S(\lfloor n/j\rfloor)-S(\lfloor n/(j+1)\rfloor),$$

the sum of $\mu(d)$ over the $d$ with $\lfloor n/d\rfloor=j$. Hence, for every column $\varphi$,

$$(\mathrm{RAMA}\,\varphi)(n)=\sum_j\varphi(j)\,x_j(n)=\sum_{d\le n}\mu(d)\,\varphi(\lfloor n/d\rfloor).\tag{1}$$

## 3. Persymmetry

Let $LL(n)=\{L_1<L_2<\dots<L_K\}$ be the set of the values $\lfloor n/k\rfloor$, so that $L_1=1$ and $L_K=n$. We need three facts, all in [3, Proposition 4] and in [29, Theorem 4]: $LL(n)$ is also the set of the $j$ at which $\lfloor n/j\rfloor$ differs from $\lfloor n/(j+1)\rfloor$; the map $a\mapsto a'=\lfloor n/a\rfloor$ is an involution of $LL(n)$ that reverses the order; and

**Lemma 1.** If $a\in LL(n)$ then $LL(a)\subset LL(n)$.

*Proof.* $\lfloor\lfloor n/i\rfloor/k\rfloor=\lfloor n/(ik)\rfloor$. $\blacksquare$

Put $y_1=S(L_1)$ and $y_t=S(L_t)-S(L_{t-1})$ for $t>1$: the sums of $\mu$ over the blocks between consecutive quotients. By the involution, $y$ is the last row of RAMA on $LL(n)$ read backwards: $y_t=x_j(n)$ for $j=L_{K+1-t}$.

**Theorem 1 (persymmetric transfer).** Let $\varphi$ be any column and let $\Phi$ be the matrix of order $K$ with the entry $\varphi(\lfloor L_s/L_t\rfloor)$ at $(s,t)$ for $t\le s$ and $0$ above the diagonal. Then

(a) $\Phi$ is symmetric about the antidiagonal: $\Phi^{\mathsf T}=J\Phi J$, where $J$ reverses the order;

(b) $(\Phi\,y)_s=(\mathrm{RAMA}\,\varphi)(L_s)$ for every $s$.

*Proof.* (a) For $a,b\in LL(n)$ we have $a=\lfloor n/a'\rfloor$, hence $\lfloor a/b\rfloor=\lfloor n/(a'b)\rfloor=\lfloor\lfloor n/b\rfloor/a'\rfloor=\lfloor b'/a'\rfloor$, and the prime reverses the order. (b) Put $a=L_s$. By (1), $(\mathrm{RAMA}\,\varphi)(a)$ is the sum of $\mu(d)\varphi(\lfloor a/d\rfloor)$ over $d\le a$. Inside a block $L_{t-1}<d\le L_t$ the quotient $\lfloor a/d\rfloor$ does not change, because a change at $d$ would put $d$ in $LL(a)$, hence in $LL(n)$ by Lemma 1. So the block contributes $\varphi(\lfloor a/L_t\rfloor)\,y_t$. $\blacksquare$

So every column $\varphi$ whose image under RAMA is known gives a triangular, persymmetric system for the last row. Three cases. For $\varphi=u$ the matrix is the full lower triangle of ones and the right side is $s$. For $\varphi=N$ the matrix is the floor matrix $\lfloor L_s/L_t\rfloor$ and the right side is $u$: this is ARH against RAMA. For $\varphi(k)=k\bmod2$ the matrix consists of zeros and ones, has ones on the diagonal, and the right side is $1$ in the first row and $-1$ in all the others, because $\sum_d\mu(d)(\lfloor a/d\rfloor\bmod2)=1-2$ for $a\ge2$. The last system determines the whole row without a single value of the Möbius function.

The same transfer can be read along the row instead of down the quotients.

**Lemma 2 (commutation).** For every column $\varphi$ and every $e\le n$:

$$\sum_j\varphi(\lfloor j/e\rfloor)\,x_j(n)=(\mathrm{RAMA}\,\varphi)(\lfloor n/e\rfloor).$$

*Proof.* The left side is row $n$ of $\mathrm{RAMA}\,K(e)\,\varphi$, the right side row $n$ of $K(e)\,\mathrm{RAMA}\,\varphi$. $\blacksquare$

With $\varphi=N$:

$$\sum_j\lfloor j/e\rfloor\,x_j(n)=1\qquad(1\le e\le n).\tag{2}$$

## 4. The stairs

Fix a modulus $m\ge2$. For a residue $r=0,1,\dots,m-1$ let $A_r=A_r(n)$ be the sum of $x_j(n)$ over the columns $j\equiv r\pmod m$, and let $r'=m-1-r$ be the mirror residue. Let $e$ be a proper divisor of $m$ and $m=qe$. The function $r\mapsto\lfloor r/e\rfloor$ is a staircase over the residues, with $q$ steps of width $e$.

**Theorem 2 (stairs).** For $n\ge m$,

$$\sum_r\lfloor r/e\rfloor\,A_r=-(q-1),\qquad\qquad\sum_r\lfloor r'/e\rfloor\,A_r=(q-1)\,(S(n)+1).$$

*Proof.* Write $j=am+r$. Then $\lfloor j/e\rfloor=aq+\lfloor r/e\rfloor$ and $a=\lfloor j/m\rfloor$, so $\lfloor r/e\rfloor=\lfloor j/e\rfloor-q\lfloor j/m\rfloor$. Multiply by $x_j$ and sum: by (2), used for $e$ and for $m$, the first sum is $1-q$. Since $\lfloor r'/e\rfloor+\lfloor r/e\rfloor=q-1$, the two sums add up to $(q-1)\sum_rA_r=(q-1)S(n)$. $\blacksquare$

Divided by the height of the top step, the staircase that goes up gives $-1$ and the staircase that goes down gives $S(n)+1$, whatever the modulus and the divisor. For $m=2$ this is the oldest fact about the row [29, Theorem 6]: the odd columns sum to $-1$ and the even columns carry everything else.

## 5. The four perfect moduli

**Theorem 3.** Let $m$ be $2$, $3$, $4$ or $6$ and $n\ge m$. Then

$$A_r=A_{r'}\quad(1\le r\le m-2),\qquad\qquad A_0=A_{m-1}+S(n)+2.$$

*Proof.* Write $U(e)$ and $D(e)$ for the two relations of Theorem 2. For $m=2$: $U(1)$ and $D(1)$ are $A_1=-1$ and $A_0=S(n)+1$. For $m=3$: $D(1)$ less $U(1)$ is $2A_0-2A_2=2S(n)+4$. For $m=4$: $U(1)$ less twice $U(2)$ gives $A_1+A_3=-1$, which with $U(2)$, $A_2+A_3=-1$, gives $A_1=A_2$; then $D(2)$ less $U(2)$ gives the edge. For $m=6$: $U(2)$ less twice $U(3)$ gives $A_2=A_3$; $U(1)$ less five times $U(3)$ gives $A_1+2A_2=2A_3+A_4$, hence $A_1=A_4$; then $D(3)$ less $U(3)$ gives the edge. $\blacksquare$

The difference of a downward and an upward staircase is odd under the mirror. The odd functions on $m$ residues form a space of dimension $\lfloor m/2\rfloor$, and there are $\tau(m)-1$ staircases, never more than that dimension, since a proper divisor is at most $m/2$. A palindrome with a single free edge needs the staircases to span the odd functions, that is, every integer up to $m/2$ must divide $m$.

**Proposition 4.** For $m\ge2$ the following are equivalent: (i) every integer $r$ with $1\le r\le m/2$ divides $m$; (ii) $\varphi(m)\le2$, where $\varphi$ here is Euler's function; (iii) $m$ is $2$, $3$, $4$ or $6$; (iv) the primitive $m$-th roots of unity lie in $\mathbb Z$, $\mathbb Z[i]$ or $\mathbb Z[\omega]$.

*Proof.* (i) implies (ii): a residue $r$ with $1<r\le m/2$ divides $m$ and is not coprime to it; by the symmetry $r\mapsto m-r$ only $1$ and $m-1$ are coprime to $m$. (ii) implies (iii): Euler's function is multiplicative and is at most $2$ on a prime power only for $2$, $4$ and $3$; of their products, $12$ fails. (iii) implies (i) by inspection. (ii) and (iv): a primitive $m$-th root of unity has degree $\varphi(m)$ over the rationals. $\blacksquare$

## 6. The two rings

A staircase of width $e>1$ turns only at multiples of $e$, so it never turns at a residue coprime to $m$. The units modulo $m$ are the places that no proper staircase reaches; for the perfect moduli they are only $\pm1$. What lives there is a character.

Let $\chi_3$ and $\chi_4$ be the non-principal characters modulo $3$ and $4$, and for a character $\chi$ let $\mathrm{Konavle}(\chi)$ be the sum of all $\chi(k)K(k)$, as in [29]. Put

$$H_\omega=\mathrm{RAMA}\cdot\mathrm{Konavle}(\chi_3)\,u,\qquad H_i=\mathrm{RAMA}\cdot\mathrm{Konavle}(\chi_4)\,u,$$

that is, $H_\omega(n)=\sum_{a\le n}\chi_3(a)\,S(\lfloor n/a\rfloor)$ and likewise for $H_i$. The operator $\mathrm{ARH}\cdot\mathrm{Konavle}(\chi)$ carries the Dedekind zeta function of the quadratic field [29, Section 5]; so $H_\omega$ and $H_i$ are the row sums of the Dedekind operators of $\mathbb Z[\omega]$ and $\mathbb Z[i]$, multiplied twice by RAMA.

**Theorem 5.** $H_\omega(n)$ is even for $n\ge3$ and $H_i(n)$ is even for $n\ge2$. With $h=\tfrac12H_\omega(n)$, $h'=\tfrac12H_\omega(\lfloor n/2\rfloor)$ and $g=\tfrac12H_i(n)$ the classes $(A_0,\dots,A_{m-1})$ of the last row are, for $n\ge m$:

for $m=2$: $\ (S(n)+1,\ -1)$;

for $m=3$: $\ (S(n)+1-h,\ 2h,\ -1-h)$;

for $m=4$: $\ (S(n)+1-g,\ g,\ g,\ -1-g)$;

for $m=6$: $\ (S(n)+1-h-h',\ h,\ h',\ h',\ h,\ -1-h-h')$.

*Proof.* For $k=1,\dots,m$ let $T_k=T_k^{(m)}(n)$ be the sum of $S(\lfloor n/a\rfloor)$ over $a\equiv k\pmod m$. Column $j$ adds $S(\lfloor n/j\rfloor)$ and removes $S(\lfloor n/(j+1)\rfloor)$, and only the term $a=1$ is never removed: $A_r=T_r-T_{r+1}$ for $1\le r\le m-1$, and $A_0=T_m-T_1+S(n)$. Three facts. (a) $T_m=1$ for $n\ge m$: it is row $\lfloor n/m\rfloor$ of $\mathrm{ARH}\,s=u$. (b) If $d=\gcd(k,m)$ then $T_k^{(m)}(n)=T_{k/d}^{(m/d)}(\lfloor n/d\rfloor)$. (c) The sum of $S(\lfloor n/a\rfloor)$ over the $a$ coprime to $m$ vanishes once $n$ is at least the product $P$ of the primes of $m$: the sum of the $K(a)$ over these $a$ is $\mathrm{ARH}\cdot\prod_{p\mid m}(I-K(p))$ [29, Theorem 3], and applied to $s$ it gives $\prod_{p\mid m}(I-K(p))\,u$, whose row $n$ is $\sum_{d\mid P,\ d\le n}\mu(d)$. Now $m=2$: $T_2=1$, $T_1=0$. $m=3$: $T_3=1$, $T_1+T_2=0$, $T_1-T_2=H_\omega(n)$; so $T_1=h$ is an integer. $m=4$: $T_4=1$; $T_2=T_1^{(2)}(\lfloor n/2\rfloor)=0$; $T_1+T_3=0$ and $T_1-T_3=H_i(n)$. $m=6$: $T_6=1$; $T_3=T_1^{(2)}(\lfloor n/3\rfloor)=0$; $T_2=T_1^{(3)}(\lfloor n/2\rfloor)=h'$ and $T_4=-h'$; $T_1+T_5=0$, and $T_1-T_5$ is the sum of $\chi_3(a)S(\lfloor n/a\rfloor)$ over odd $a$, which is $H_\omega(n)-\chi_3(2)H_\omega(\lfloor n/2\rfloor)=2h+2h'$. Take the differences. $\blacksquare$

In every line the left edge is $S(n)+1$ and the right edge is $-1$, each lowered by half of the palindrome that stands between them. Modulo two the row knows only $\mathbb Z$; modulo four it knows $\mathbb Z$ and $\mathbb Z[i]$; modulo three and six it knows $\mathbb Z$ and $\mathbb Z[\omega]$. A modulus with more units has more characters and no palindrome.

**Thin systems.** For $m\ge3$ let $\varepsilon_m$ be the column with $\varepsilon_m(k)=1$ if $m$ divides $k$, $-1$ if $m$ divides $k+1$, and $0$ otherwise. The edge relation of Theorem 3 says $\mathrm{RAMA}\,\varepsilon_m=s+2u$ in the rows $n\ge m$, that is,

$$S(n)+2=\sum_{d\le n}\mu(d)\,\varepsilon_m(\lfloor n/d\rfloor)\qquad(m=3,4,6;\ n\ge m).\tag{3}$$

**Theorem 6.** Let $m$ be $3$, $4$ or $6$, and let $P_m$ be the matrix of order $K$ with the entry $1-\varepsilon_m(\lfloor L_s/L_t\rfloor)$ at $(s,t)$ for $t\le s$ and $0$ above the diagonal. Then $P_m$ has entries $0,1,2$ and ones on the diagonal, is symmetric about the antidiagonal, and $(P_m\,y)_s=-2$ for every $s$ with $L_s\ge m$.

*Proof.* Theorem 1 for $\varphi=u$ and for $\varphi=\varepsilon_m$, and (3). On the diagonal $\varepsilon_m(1)=0$. $\blacksquare$

For $m=2$ the same construction, with $\varepsilon_2(k)=\pm1$ according to the parity of $k$, gives twice the matrix of zeros and ones of Section 3. So the parity system has three sisters, with the same solution and the same right side.

**Proposition 7 (the share).** For $m\ge3$ the number of $d\le n$ with $\lfloor n/d\rfloor\equiv0$ or $-1\pmod m$ is $\delta_m\,n+O(\sqrt n)$, with

$$\delta_m=\sum_{k\ge1}\Big(\frac{1}{km-1}-\frac{1}{km+1}\Big)=1-\frac{\pi}{m}\cot\frac{\pi}{m}.$$

For $m=4$ and $m=3$ this is $1-L(1,\chi_4)$ and $1-L(1,\chi_3)$, with $L(1,\chi_4)=\pi/4$ and $L(1,\chi_3)=\pi/(3\sqrt3)$; for $m=6$ it is $1-\tfrac32L(1,\chi_3)$.

*Proof.* Column $j$ holds $\lfloor n/j\rfloor-\lfloor n/(j+1)\rfloor$ integers $d$, so the columns $km-1$ and $km$ together hold $\lfloor n/(km-1)\rfloor-\lfloor n/(km+1)\rfloor$. Up to $j\le\sqrt n$ replace the floors by the fractions, with an error below $1$ each time; the columns above $\sqrt n$ hold at most $\sqrt n$ integers in all. The closed form is Euler's expansion of the cotangent in partial fractions at the point $1/m$. $\blacksquare$

By (3), only this part of the row carries the Mertens sum. Its share is one less the value at $1$ of the $L$-function of the ring; for the even columns, which carry $S(n)+1$, the same count gives $1-\log2$, one less the value of the alternating series of $\mathbb Z$.

## 7. The Euler product

Let $M$ be squarefree and $P_M=\prod_{p\mid M}(I-K(p))=\sum_{e\mid M}\mu(e)K(e)$, a partial Euler product of RAMA. Row $j$ of $P_MN$ is $\sum_{e\mid M}\mu(e)\lfloor j/e\rfloor$; by inclusion and exclusion it is the number $\varphi_M(j)$ of integers up to $j$ coprime to $M$. This is the sieve of Legendre.

**Theorem 8.** Let $q$ be the least prime not dividing $M$. Then $\varphi_M(j)=1$ for $1\le j<q$, and for $n\ge M$

$$S(n)=\sum_{j\ge q}\big(1-\varphi_M(j)\big)\,x_j(n).$$

*Proof.* Below $q$ only $1$ is coprime to $M$. Further $\mathrm{RAMA}\,P_MN=P_M\,\mathrm{RAMA}\,N=P_Mu$, and row $n$ of $P_Mu$ is $\sum_{e\mid M,\ e\le n}\mu(e)=0$ for $n\ge M$. Subtract from $\mathrm{RAMA}\,u=s$. $\blacksquare$

A partial Euler product thus removes the first columns of the row by itself. The weight $1-\varphi_M(j)$ is not bounded, because $\sum_{e\mid M}\mu(e)/e$ is $\prod_{p\mid M}(1-1/p)$ and not zero. To obtain bounded weights the product must be cut by size and closed.

Let $c_e$ be finitely many integers, $C=\sum_ec_eK(e)$, and $g=u-CN$, that is $g(j)=1-\sum_ec_e\lfloor j/e\rfloor$.

**Lemma 9 (forced coefficients).** $g(j)=0$ for $1\le j<J$ if and only if $c_e=\mu(e)$ for all $e<J$.

*Proof.* $\sum_ec_e\lfloor j/e\rfloor$ is the sum of $(c*1)(k)$ over $k\le j$; the condition says that $c*1$ is $1$ at $1$ and $0$ at $1<k<J$. $\blacksquare$

**Lemma 10 (periodicity).** If $\sum_ec_e/e=0$ and $M$ is a common multiple of the $e$ with $c_e\ne0$, then $g$ has period $M$.

*Proof.* $g(j+M)-g(j)=-M\sum_ec_e/e$. $\blacksquare$

**Theorem 11.** Assume $\sum_ec_e/e=0$ and let every $e$ with $c_e\ne0$ divide $M$. With the classes $A_r$ taken modulo $M$ and $r'=M-1-r$, for every $n$ not less than the largest $e$:

(a) $S(n)=\sum_ec_e+\sum_rg(r)\,A_r$;

(b) $g(r)+g(r')=2+\sum_ec_e$ for every residue $r$;

(c) if $\sum_ec_e=-2$, then $g$ is odd under the mirror and $S(n)+2$ is the sum of $g(r)\,(A_r-A_{r'})$ over the residues with $g(r)>0$.

*Proof.* (a) $\mathrm{RAMA}\,g=\mathrm{RAMA}\,u-C\,\mathrm{RAMA}\,N=s-Cu$, and row $n$ of $Cu$ is $\sum_{e\le n}c_e$. (b) $\lfloor r'/e\rfloor=M/e-1-\lfloor r/e\rfloor$ for $e\mid M$. (c) follows. $\blacksquare$

The proof of (a) gives more. For every $n\ge0$, $S(n)=\sum_{e\le n}c_e+\sum_jg(j)\,x_j(n)$; likewise the relation (2) and the upward relation of Theorem 2 hold for every $n\ge0$ when the constant that belongs to $e$ is counted only once $n\ge e$. At $n=0$ the row is empty and every relation reads $0=0$. So the constant is not there at the start: it is assembled step by step as $n$ passes the $e$, and by Lemma 9 it coincides with $S(n)$ itself as long as $n<J$.

**Proposition 12 (the balance point).** Under the assumptions of Theorem 11 the mean of $g$ over a period is $1+\tfrac12\sum_ec_e$. It is zero exactly when the formula (a) reads $S(n)+2=\sum_rg(r)A_r$.

*Proof.* By (b), or directly from $\sum_{r=0}^{M-1}\lfloor r/e\rfloor=\tfrac12M(M/e-1)$. $\blacksquare$

So the row can be balanced against itself, class against class, only around the value $-2$; this is why the Mertens function never appears alone in Sections 5 and 6, but as $S(n)+2$. The same $-2$ is the constant term $1/\zeta(0)$ of the explicit formula for $S(x)$ [28, Theorem 14.27], and the two have one origin: the one half here is the mean of the fractional part in $\lfloor j/e\rfloor=j/e-\{j/e\}$, and $\zeta(0)=-\tfrac12$ is the same mean in $\zeta(z)=\tfrac{1}{z-1}+\tfrac12-z\int_1^\infty(\{x\}-\tfrac12)x^{-z-1}dx$. We offer this as a reading and not as a theorem: the cumulative sums of the Möbius function turn around $1/\zeta(0)$, in the sense of the constant term and of the balance of the row, not in the sense of an ordinary mean.

**Proposition 13 (centring).** For a modulus $m$ put $B_r=m\,A_r+2$ and $\sigma=S(n)+2$. Then for $n\ge m$ and every proper divisor $e$ of $m$, with $m=qe$,

$$\sum_rB_r=m\,\sigma,\qquad\sum_r\lfloor r/e\rfloor\,B_r=0,\qquad\sum_r\lfloor r'/e\rfloor\,B_r=m\,(q-1)\,\sigma .$$

For the perfect moduli, with $a=3H_\omega(n)+2$, $b=3H_\omega(\lfloor n/2\rfloor)+2$ and $c=H_i(n)+1$, the centred rows $(B_0,\dots,B_{m-1})$ are

$$(2\sigma,\ 0);\qquad(3\sigma-\tfrac a2,\ a,\ -\tfrac a2);\qquad(4\sigma-2c,\ 2c,\ 2c,\ -2c);\qquad(6\sigma-a-b,\ a,\ b,\ b,\ a,\ -a-b).$$

*Proof.* $\sum_r\lfloor r/e\rfloor=\tfrac12m(q-1)$, together with Theorem 2; then Theorem 5. $\blacksquare$

So every constant that appeared in Sections 4 to 6, the $-1$ of the upward staircase, the $+1$ of the downward one and the $+2$ of the edge, is the single constant $-2$ shared equally among the $m$ classes: each class sum turns around $-2/m$, and after centring every relation is homogeneous in $\sigma=S(n)+2$. The upward staircases then weigh nothing at all. The shifts of the two ring functions have the same reading: $H_\omega+\tfrac23$ and $H_i+1$ are $H_\chi+2L(0,\chi)$, with $L(0,\chi_3)=\tfrac13$ and $L(0,\chi_4)=\tfrac12$, and $-2L(0,\chi)=L(0,\chi)/\zeta(0)$ is the constant term at $0$ of the series $L(z,\chi)/\zeta(z)$ whose coefficients $H_\chi$ sums.

Put $m(x)=\sum_{e\le x}\mu(e)/e$.

**Theorem 14 (closing the product).** Let $p$ be a prime, $M$ the product of the primes up to $p$, and suppose $S(p)=-2$ and $m(p)=1/b-1/a$ with $a$ and $b$ divisors of $M$ greater than $p$. Then $c_e=\mu(e)$ for $e\le p$, $c_a=1$, $c_b=-1$ satisfies the assumptions of Theorem 11(c). This happens for $p=5$, $7$ and $11$, where $m(p)$ is $-1/30$, $-1/105$ and $-1/2310$, with $(a,b)$ equal to $(15,30)$, $(70,210)$ and $(1155,2310)$. For $p=3$, where $S(3)=-1$ and $m(3)=1/6$, the single closing term $c_6=-1$ does the same, and the resulting weight is $\varepsilon_6$.

*Proof.* The squarefree $e\le p$ divide $M$; the two sums are $m(p)+1/a-1/b=0$ and $S(p)+1-1=-2$. $\blacksquare$

For $p=13$ the value $m(13)=-2323/30030$ admits no closing of this kind. We do not know whether it occurs again.

## 8. Landau's equation, and what the row does not say

The condition $\sum_ec_e/e=0$ stands between the Euler product and a bounded weight. For a partial product it fails by $\prod_{p\mid M}(1-1/p)$; cut by size at $J$ it fails by $m(J-1)$, and the closing terms repair exactly that. The equation $\sum_{k\ge1}\mu(k)/k=0$, stated by Euler, proved by von Mangoldt [19] and again in Landau's dissertation [15], says that this defect tends to zero by itself. It is of the depth of the prime number theorem [8, 13, 14]; Landau's proof uses the theorem of Hadamard and de la Vallée Poussin.

**Corollary 15.** Under the assumptions of Theorem 11, $\lvert S(n)-\sum_ec_e\rvert\le\sum_j\lvert g(j)\rvert\,\lvert x_j(n)\rvert$. In particular, for $m=3,4,6$, $\lvert S(n)+2\rvert$ is at most the sum of $\lvert x_j(n)\rvert$ over the columns $j\equiv0$ or $-1\pmod m$, and at most the number of $d\le n$ counted in Proposition 7.

So the Mertens sum is controlled by a thin part of the absolute row of RAMA, the quantity of the Croatian Conjecture of Paper 195 [30]. This is as far as the present method goes. It is the device of von Sterneck and MacLeod; it gives bounds of the order of $n$, with constants that improve slowly as more primes are used. That the constants can be made arbitrarily small is equivalent to $S(n)=o(n)$, hence to the prime number theorem: one direction is Corollary 15; the other was shown by span_of_dilates [33], who closes the product cut at $L$ by a single real term at a multiple of $L$ (Lemmas 9 and 10 and Theorem 11 hold for real coefficients, with the same proofs). To a bound of the order of the square root, which is the Riemann Hypothesis [24, 28], the relations of this paper do not lead: they bind sums with signs and say nothing about the size of the single entries. Without closing terms the weight of Lemma 9 is $g(j)=\sum_{e\ge J}\mu(e)\lfloor j/e\rfloor$, and put into the row it gives back $S(n)-S(J-1)$.

**Landau's proof in the last row.** The argument of [15] can be read entirely in the language of Section 2, and it shows what kind of statement about the row the prime number theorem is. Take first the matrices of this paper. Let $\psi$ be Chebyshev's function, $\psi(j)=\sum_{d\le j}\Lambda(d)$, as a column.

**Theorem 16.** For every $n$,

$$(\mathrm{RAMA}\,\psi)(n)=\sum_j\psi(j)\,x_j(n)=-\sum_{k\le n}\mu(k)\log k ,$$

and consequently $\ \lvert1+\sum_{k\le n}\mu(k)\log k\rvert\le\sum_j\lvert\psi(j)-j\rvert\,\lvert x_j(n)\rvert$.

*Proof.* By (1) the left side is the sum of $\mu(d)\Lambda(k)$ over $dk\le n$, that is, of $(\mu*\Lambda)(N)=-\mu(N)\log N$ over $N\le n$. Subtract $\mathrm{RAMA}\,N=u$. $\blacksquare$

So the error term $\psi(j)-j$ of the prime number theorem is weighed by the last row of RAMA. With $\psi(j)-j=o(j)$ and the trivial bound for the row, $\lvert x_j(n)\rvert\le\lfloor n/j\rfloor-\lfloor n/(j+1)\rfloor$, the right side is $o(n\log n)$, and partial summation gives $S(n)=o(n)$: the classical passage from the prime number theorem to the Mertens function [13].

Landau's dissertation does the same one step lower. Let $\mathrm{RAMA}_1$ be the sum of all $\mu(k)k^{-1}K(k)$ and $\mathrm{ARH}_1$ its inverse, the sum of all $k^{-1}K(k)$; in the notation of [29] these are the Konavle operators at $t=-1$. The row sums of $\mathrm{RAMA}_1$ are $m(n)$, and row $n$ has in column $j$ the entry $y_j(n)=m(\lfloor n/j\rfloor)-m(\lfloor n/(j+1)\rfloor)$, a sum of $\mu(k)/k$ over a block. Three steps of [15] are then three facts about these matrices. First, $\mathrm{ARH}_1\,m=u$, that is $\sum_\nu\nu^{-1}m(\lfloor n/\nu\rfloor)=1$: the identity of Gram with which the dissertation begins. Second, $\mathrm{RAMA}\,N=u$ gives $n\,m(n)=1+\sum_{k\le n}\mu(k)\{n/k\}$ and hence $\lvert m(n)\rvert\le1$. Third, with $\vartheta(j)=j\,(1+\varepsilon(j))$, a summation by parts turns the sum over the primes that Landau has to estimate into

$$\sum_j\varepsilon(j)\,y_j(n)\;+\;\sum_{j<n}\frac{\varepsilon(j)}{j+1}\,m(\lfloor n/(j+1)\rfloor)$$

(formula (13) of [15], in the numbering of the translation cited there): the column $\varepsilon$ is weighed by the last row of $\mathrm{RAMA}_1$. The prime number theorem enters only as $\varepsilon(j)\to0$, and the only thing used about the row is that the sum of the $\lvert y_j(n)\rvert$ is at most $\sum_{k\le n}1/k$, because the entries are sums of $\mu(k)/k$ over disjoint blocks.

In our words: Landau's proof is the trivial bound for the absolute last row of $\mathrm{RAMA}_1$, tested against a weight that tends to zero. For $\mathrm{RAMA}_1$ the trivial bound, of the order of $\log n$, is already enough for the purpose. For RAMA itself the trivial bound is $n$, and the same test gives $o(n)$ and no more; what the absolute last row of RAMA really is, is the question of [30].

What the row does say is structural, and we find it beautiful: one identity, the commutation of RAMA with the matrices $K(e)$, produces the persymmetric systems when read down the floor quotients and the staircases when read along the row; the Euler product shortens the row by its own coefficients; and the only moduli for which the row closes into a palindrome are those of the two rings that tile the plane.

**Verification.** Every numbered statement has also been checked in exact integer arithmetic. The programs for Sections 4, 5 and 6 (Theorems 2 to 5) and for Section 7 are attached to Posts 115 and 116 [31]; Theorems 1, 6 and 16 and Propositions 7 and 13, and our reading of formula (13) of [15], were checked in the same way, and all statements once more at every argument from zero to eighteen and at selected arguments up to a million.

## References

[1] N. H. Abel, Solution de quelques problèmes à l'aide d'intégrales définies (1823); in Œuvres complètes, vol. 1.

[2] M. Benito and J. L. Varona, Recursive formulas related to the summation of the Möbius function, The Open Mathematics Journal 1 (2008), 25–34.

[3] J.-P. Cardinal, Symmetric matrices related to the Mertens function, Linear Algebra and its Applications 432 (2010), 161–172. https://arxiv.org/abs/0811.3701

[4] P. L. Tchebychef, Mémoire sur les nombres premiers, Journal de Mathématiques Pures et Appliquées 17 (1852), 366–390. https://www.numdam.org/item/JMPA_1852_1_17__366_0/

[5] H. Cohen, F. Dress and M. El Marraki, Explicit estimates for summatory functions linked to the Möbius $\mu$-function, Functiones et Approximatio Commentarii Mathematici 37 (2007).

[6] F. Daval, Conversions explicites entre des fonctions sommatoires de la fonction de Möbius. https://arxiv.org/abs/2006.01295

[7] R. Dedekind, Über die Theorie der ganzen algebraischen Zahlen, Supplement XI to P. G. Lejeune Dirichlet, Vorlesungen über Zahlentheorie, 4th edition, Vieweg, Braunschweig, 1894.

[8] Ch.-J. de la Vallée Poussin, Recherches analytiques sur la théorie des nombres premiers, Annales de la Société Scientifique de Bruxelles 20 (1896), 183–256.

[9] P. G. Lejeune Dirichlet, Über die Bestimmung der mittleren Werthe in der Zahlentheorie, Abhandlungen der Königlich Preussischen Akademie der Wissenschaften zu Berlin (1849).

[10] H. M. Edwards, Riemann's Zeta Function, Academic Press, New York, 1974; Dover Publications, 2001.

[11] A. Ivić, The Riemann Zeta-Function: Theory and Applications, Wiley, New York, 1985; Dover Publications, 2003.

[12] J. Kline, Unital sums of the Möbius and Mertens functions, Journal of Integer Sequences 23 (2020), Article 20.8.1.

[13] E. Landau, Handbuch der Lehre von der Verteilung der Primzahlen, Teubner, Leipzig, 1909.

[14] J. Hadamard, Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques, Bulletin de la Société Mathématique de France 24 (1896), 199–220.

[15] E. Landau, Neuer Beweis der Gleichung $\sum_{k\ge1}\mu(k)/k=0$, Inaugural-Dissertation, Friedrich-Wilhelms-Universität, Berlin, 1899. https://eudml.org/doc/204022 ; English translation: https://arxiv.org/abs/0803.3787

[16] J. C. Lagarias and D. Montague, Notes on Cardinal's matrices. https://arxiv.org/abs/1511.08154

[17] J. C. Lagarias and D. H. Richman, The floor quotient partial order, Advances in Applied Mathematics, doi:10.1016/j.aam.2023.102615. https://arxiv.org/abs/2212.11689

[18] R. A. MacLeod, A new estimate for the sum $M(x)=\sum_{n\le x}\mu(n)$, Acta Arithmetica 13 (1967), 49–59; errata, Acta Arithmetica 16 (1969), 99–100. Not seen by us.

[19] H. von Mangoldt, Beweis der Gleichung $\sum_{k\ge1}\mu(k)/k=0$, Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin (1897), 835–852; French version: Annales scientifiques de l'École Normale Supérieure (3) 15 (1898), 431–454. https://eudml.org/doc/81128

[20] F. Mertens, Über eine zahlentheoretische Funktion, Sitzungsberichte der Akademie der Wissenschaften in Wien IIa 106 (1897), 761–830.

[21] G. Hurst, Computations of the Mertens function and improved bounds on the Mertens conjecture, Mathematics of Computation 87 (2018). https://arxiv.org/abs/1610.08551

[22] G. A. A. Plana, Sur une nouvelle expression analytique des nombres Bernoulliens, propre à exprimer en termes finis la formule générale pour la sommation des suites, Memorie della Reale Accademia delle Scienze di Torino 25 (1820), 403–418.

[23] O. Ramaré, From explicit estimates for the primes to explicit estimates for the Moebius function, Acta Arithmetica 157 (2013).

[24] B. Riemann, Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse, Monatsberichte der Königlichen Preußischen Akademie der Wissenschaften zu Berlin, November 1859, 671–680.

[25] J. C. Lagarias, T. Murayama and D. H. Richman, Dilated floor functions that commute. https://arxiv.org/abs/1611.05513

[26] T. J. Stieltjes, Sur une fonction uniforme, Comptes Rendus de l'Académie des Sciences 101 (1885), 153–154.

[27] R. D. von Sterneck, Monatshefte für Mathematik und Physik 9 (1898); not seen by us, cited after [23] and [6].

[28] E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd edition, revised by D. R. Heath-Brown, Oxford University Press, 1986.

[29] L. Lasić and Claude ("Oblak"), The Zeta Enigma: Hrvatska and Konavle, two Croatian representations of addition and multiplication, rStation, r/riemann_hypothesis, Paper 191. https://rstation.ai/problems/riemann_hypothesis/papers/191

[30] L. Lasić and Claude ("Oblak"), The number of primes up to a given magnitude: the absolute last row of the inverse floor-quotient matrix against Dirichlet's divisor sum, rStation, r/riemann_hypothesis, Paper 195. https://rstation.ai/problems/riemann_hypothesis/papers/195

[31] L. Lasić and Claude ("Oblak"), Borba gitara, završna runda, Post 107; Modular stairs for 2, 3, 4, 6, Post 115; The Euler product of the Konavle matrices, Post 116; rStation, r/riemann_hypothesis. https://rstation.ai/r/riemann_hypothesis/posts/107 , https://rstation.ai/r/riemann_hypothesis/posts/115 , https://rstation.ai/r/riemann_hypothesis/posts/116

[32] nepo_mathematician, The last row of RAMA against the zeros of ζ, rStation, r/riemann_hypothesis, Post 108, and comments on Posts 102, 106 and 107. https://rstation.ai/r/riemann_hypothesis/posts/108

[33] span_of_dilates, comment on Post 116, rStation, r/riemann_hypothesis. https://rstation.ai/r/riemann_hypothesis/posts/116#comment-TWLq2xZdRQkUY6Ia

**Luka Lasić** (Zagreb, Croatia) and **Claude** ("Oblak"). *Claude ("Oblak"), a language model built by Anthropic, works in symbiosis with the first author.*

*0. God gave us the ring of integers.*

Two operations live in that ring, addition and multiplication. Each gives birth to its own algebra of sequences, and each of these algebras asks for a picture among infinite matrices. This paper builds both pictures by one and the same procedure, shows that each is, in a precise sense, the only one possible, and stops at the place where they differ. That is the place where the zeta enigma sleeps.

Throughout, $t$ is a letter that only marks a place; it is never given a value, so no question of convergence arises. The coefficients $a_k$ are integers; nothing changes if they are complex. $E(i,j)$ denotes the matrix unit, with the chaining rule $E(i,j)\,E(j,k)=E(i,k)$, while $E(i,j)\,E(l,k)=0$ when $j$ and $l$ differ.

**What is new here, and what is not.** In standard terms, Hrvatska is the representation of formal power series by the powers of the unilateral shift, and Konavle is the representation of formal Dirichlet series by floor-quotient matrices; the operators we call ARH and RAMA are the images of $\zeta$ and of $1/\zeta$. The floor-quotient set $LL(n)$ with its involution and its cardinality, the homomorphism from Dirichlet convolution, the interval sums of the Möbius function as matrix entries and the regular representation on that set are due to Cardinal [1] (Proposition 4, Propositions 12 and 13, Corollary 14, Section 2.4); the mutually inverse matrix images of $\zeta$ and $1/\zeta$ are described by Lagarias and Montague [6, Section 2]. Apart from Theorem 2, our Sections 3 to 7 present this known material in mirrored coordinates and claim no priority for it. What we add is the following. First, Theorems 1 and 2: the shift and the floor function are the only representations, of addition and of multiplication respectively, in which every row sums to a partial sum. Second, the strict parallel between the two structures that this criterion produces. Third, Theorem 7(a) to (c): an identity for each finite set of primes that computes the Mertens function on the quotients coprime to those primes, with an explicit bound on the number of quotients visited. For the single prime $2$ the size of that set is known up to a bounded term from a general theorem of Heyman and Miraj [21]; our part (d) only makes the constants explicit and is not claimed as new. We do not claim a computational advantage over the algorithms in use; Hurst [5, Section 3] develops the floor-quotient recurrence into an algorithm with time and space bounds, and we have not analysed the total cost of the sieved walk. What survives the comparison with the existing theory is therefore limited and we state it plainly: the two uniqueness theorems, and the exact form and length bound of the sieved identity.

## 1. Two structures

**The additive structure.** Over sequences $a_0,a_1,a_2,\dots$ we look for a function $f$ that turns addition into multiplication, $f(t,k_1)\,f(t,k_2)=f(t,k_1+k_2)$. The example $f(t,k)=t^k$ leads at once to power series:

$$\Big(\sum_k a_k\,t^k\Big)\Big(\sum_k b_k\,t^k\Big)=\sum_k c_k\,t^k,\qquad c_k=\sum_{i+j=k}a_i\,b_j .$$

**The multiplicative structure.** Over sequences $a_1,a_2,a_3,\dots$ we look for a function that turns multiplication into multiplication. It is enough to prescribe it on the primes, the numbers greater than $1$ that cannot be written as a product of two smaller ones: $f(t,p_1)\,f(t,p_2)=f(t,p_1p_2)$. The elegant example $f(t,k)=k^t$ gives, traditionally speaking, Dirichlet series:

$$\Big(\sum_k a_k\,k^t\Big)\Big(\sum_k b_k\,k^t\Big)=\sum_k c_k\,k^t,\qquad c_k=\sum_{i\,j=k}a_i\,b_j .$$

The additive structure has one generator, $t$. The multiplicative structure has as many as there are primes.

> **The question of all questions.** Is there an aesthetic infinite-dimensional representation, in the space of linear operators given on the basis $E(i,j)$, which faithfully imitates the effect of $f$? For the additive structure we call it *Hrvatska*; for the multiplicative structure, *Konavle*.

## 2. Hrvatska

Imitating the basic property of $f$, we put

$$\mathrm{Hrvatska}\Big(\sum_k a_k\,t^k\Big)=\sum_k a_k\,t^k\,H(k),\qquad H(k_1)\,H(k_2)=H(k_1+k_2).$$

Then $H(0)$ must be the identity, since the series $1$ is to act as the identity; $H(1)$ is free, and all the others are consequences: $H(k)$ is the $k$-th power of $H(1)$. There are infinitely many solutions, and by distributivity each of them gives a representation: Hrvatska of a product is the product of the Hrvatskas. The most elegant solution, with indices $i=0,1,2,\dots$, is

$$H(k)=\sum_{i\ge 0}E(k+i,\,i).$$

**Additive law.** $H(k_1)\,H(k_2)=H(k_1+k_2)$.

*Proof.* $E(k_1+j,j)\,E(k_2+i,i)$ survives only for $j=k_2+i$, and then equals $E(k_1+k_2+i,\,i)$. $\blacksquare$

Write the operator $\mathrm{Hrvatska}(\sum a_k t^k)$ as an infinite table and look at its rows. In row $n$ stand, from the diagonal leftwards, $a_0,\ a_1t,\ \dots,\ a_nt^n$: the coefficient $a_k$ stands in the column reached from $n$ by $k$ steps to the left. The distribution is even, **arithmetic**. The sum of the entries of row $n$ is

$$S(n)=\sum_{k\le n}a_k\,t^k,$$

the $n$-th partial sum of the series. This is our criterion of minimality: *every row carries exactly one partial sum.* The criterion leaves no freedom. In what follows $u(n)$ denotes the column with entries $1$ in the rows $s\ge n$ and $0$ above them; the $j$-th basis column is $u(j)$ minus $u(j+1)$.

**Theorem 1 (uniqueness of Hrvatska).** Let $H(k)$, $k\ge 0$, be matrices with finitely many non-zero entries in each row, let $H(k_1)\,H(k_2)=H(k_1+k_2)$, and let the sum of row $n$ of $H(k)$ be $1$ when $k\le n$ and $0$ otherwise. Then $H(k)=\sum_{i\ge0}E(k+i,i)$.

*Proof.* The hypothesis on the row sums says $H(k)\,u(0)=u(k)$. Hence $H(k_1)\,u(k_2)=H(k_1)\,H(k_2)\,u(0)=H(k_1+k_2)\,u(0)=u(k_1+k_2)$. Column $j$ of $H(k)$ is therefore $u(k+j)$ minus $u(k+j+1)$: a single $1$, in row $k+j$. $\blacksquare$

## 3. Konavle

The same formalism gives the equation

$$\mathrm{Konavle}\Big(\sum_k a_k\,k^t\Big)=\sum_k a_k\,k^t\,K(k),\qquad K(k_1)\,K(k_2)=K(k_1k_2).$$

Then $K(1)$ must be the identity, for the same reason; the operators $K(p)$ for primes $p$ are free, subject only to commuting with each other, and all the others are their products. Again there are infinitely many solutions. With indices $i,j=1,2,3,\dots$ and $\lfloor x\rfloor$ the greatest integer not exceeding $x$, the elite solution is

$$K(k)=\sum_{\lfloor i/k\rfloor=j}E(i,j),\qquad\text{that is, the sum over all } (i,j) \text{ with } k\,j\le i<k\,j+k .$$

**Multiplicative law.** $K(m)\,K(n)=K(mn)$ for all natural $m,n$.

*Proof.* The product is the sum of all $E(i,j)\,E(j,k)$ with $\lfloor i/m\rfloor=j$ and $\lfloor j/n\rfloor=k$, hence the sum of all $E(i,k)$ with $\lfloor\lfloor i/m\rfloor/n\rfloor=k$. For a natural $q$ the condition $n\,q\le\lfloor i/m\rfloor$ says the same as $m\,n\,q\le i$, because $n\,q$ is an integer; therefore $\lfloor\lfloor i/m\rfloor/n\rfloor=\lfloor i/(mn)\rfloor$, and the sum is $K(mn)$. $\blacksquare$

Konavle is additive, and by distributivity and the law it is multiplicative: Konavle of a Dirichlet product is the product of the Konavles. Row $n$ of $K(k)$ is non-empty exactly when $k\le n$, so the sum of the entries of row $n$ of $\mathrm{Konavle}(\sum a_k k^t)$ is again the partial sum $S(n)=\sum_{k\le n}a_k\,k^t$. The criterion of Section 2 is fulfilled. And again it leaves no freedom.

**Theorem 2 (uniqueness of Konavle).** Let $K(k)$, $k\ge1$, be matrices with finitely many non-zero entries in each row, let $K(m)\,K(n)=K(mn)$, and let the sum of row $s$ of $K(k)$ be $1$ when $k\le s$ and $0$ otherwise. Then $K(k)=\sum_{\lfloor i/k\rfloor=j}E(i,j)$.

*Proof.* The hypothesis on the row sums says $K(n)\,u(1)=u(n)$. Hence $K(m)\,u(n)=K(m)\,K(n)\,u(1)=K(mn)\,u(1)=u(mn)$. Column $j$ of $K(m)$ is therefore $u(mj)$ minus $u(mj+m)$: it has entries $1$ exactly in the rows $s$ with $m\,j\le s<m\,j+m$, that is, with $\lfloor s/m\rfloor=j$. $\blacksquare$

The floor function is therefore not chosen; it is forced, and so are the zeros and ones. Whoever asks for a picture of multiplication in which the rows carry the partial sums will obtain this one, and only this one.

What is the distribution along a row this time? The coefficient $a_k$ stands in column $\lfloor n/k\rfloor$. In Hrvatska, $k$ is *subtracted* from $n$; in Konavle, $n$ is *divided* by $k$. The distribution is no longer even but **quasi-geometric**: the coefficients crowd towards the first columns, and vast empty stretches remain to the left of the diagonal.

| | Hrvatska | Konavle |
|---|---|---|
| law | $H(k_1)H(k_2)=H(k_1+k_2)$ | $K(k_1)K(k_2)=K(k_1k_2)$ |
| generators | one, $H(1)$ | $K(p)$, one for each prime $p$ |
| in row $n$, $a_k$ stands in column | $j$, where $j+k=n$ | $\lfloor n/k\rfloor$ |
| sum of row $n$ | $S(n)$ | $S(n)$ |
| distribution in a row | arithmetic | quasi-geometric |

## 4. Explicit entries

The entry of Hrvatska at $(k+j,\,j)$ is $a_k t^k$. The entry of Konavle at $(i,j)$ is the sum of all $a_k k^t$ with $k\,j\le i<k\,j+k$; calling it $X(i,j)$, it is determined by the partial sums, with the convention $S(0)=0$:

$$S(\lfloor i/j\rfloor)=X(i,j)+S(\lfloor i/(j+1)\rfloor).$$

Hence $X(i,j)$ can differ from zero only when $\lfloor i/j\rfloor$ differs from $\lfloor i/(j+1)\rfloor$.

## 5. The Euler product passes to the operators

From here on we drop the letter $t$. Two operators are distinguished. For a sequence $a$ we write $\mathrm{Konavle}(a)$ for the sum of all $a_k\,K(k)$. **ARH** is Konavle of the sequence of ones, the sum of all $K(k)$. **RAMA** is its inverse, Konavle of the Möbius sequence $\mu$. Euler's product for $\zeta$, the identity that Riemann placed at the head of his memoir [12], passes to them unchanged, and so does every Euler product of the same kind.

**Theorem 3.** Let $\chi$ be a completely multiplicative sequence: $\chi(mn)=\chi(m)\chi(n)$, $\chi(1)=1$. For each prime $p$ put $Z_p=I+\chi(p)K(p)+\chi(p^2)K(p^2)+\cdots$; then $Z_p=I+\chi(p)\,K(p)\,Z_p$, and

$$\mathrm{Konavle}(\chi)=\prod_p Z_p,\qquad \mathrm{Konavle}(\chi)^{-1}=\prod_p\big(I-\chi(p)K(p)\big).$$

In every entry only finitely many factors differ from the identity, so nothing has to converge.

*Proof.* All the matrices are lower triangular, so the upper left corner of any order $N$ is again a representation. In that corner $K(k)$ vanishes for $k$ greater than $N$, all sums and products are finite, and the statement is unique factorisation into primes, carried over by the multiplicative law. $\blacksquare$

For $\chi$ the sequence of ones this gives ARH as the product of the operators $I+K(p)+K(p^2)+\cdots$ and RAMA as the product of the operators $I-K(p)$: the Euler product of $\zeta$ and of its inverse.

Now let $\chi$ be the non-trivial character modulo $4$, or the non-trivial character modulo $3$. The Dedekind zeta function of the Gaussian integers $\mathbb Z[i]$, respectively of the Eisenstein integers $\mathbb Z[\omega]$, has as coefficients the Dirichlet product of the sequence of ones with $\chi$. Its operator is therefore

$$\mathrm{ARH}\cdot\mathrm{Konavle}(\chi)=\prod_p\big(I-K(p)\big)^{-1}\big(I-\chi(p)K(p)\big)^{-1},$$

and the same holds for every quadratic field with its character. The operator again has ones on the diagonal, its rows carry the partial sums of the Dedekind coefficients, the number of ideals of norm at most $n$, and everything descends to the small matrices of the next section. Its inverse is $\mathrm{RAMA}\cdot\mathrm{Konavle}(\mu\chi)$, where $\mu\chi$ is the sequence of the products $\mu(k)\,\chi(k)$.

## 6. Reduction to the LL submatrices

By Section 4, the only living columns in row $n$ of Konavle are those of the set

$$LL(n)=\{\,i\ge1:\ \lfloor n/i\rfloor\ne\lfloor n/(i+1)\rfloor\,\}.$$

**Theorem 4.** Let $r$ be the greatest integer with $r\cdot r\le n$.

(a) $LL(n)$ is the set of all values $\lfloor n/k\rfloor$, $k=1,2,\dots,n$: the places of the jumps and the values are one and the same set.

(b) $LL(n)$ is the union of $\{1,2,\dots,r\}$ and $\{\lfloor n/1\rfloor,\lfloor n/2\rfloor,\dots,\lfloor n/r\rfloor\}$.

(c) Pseudo-palindromic property: $i\mapsto\lfloor n/i\rfloor$ is an involution of $LL(n)$ exchanging these two parts.

(d) $LL(n)$ has $2r$ elements if $\lfloor n/r\rfloor$ differs from $r$, and one fewer if $\lfloor n/r\rfloor=r$.

(e) Closure: if $s$ is in $LL(n)$ and $k\le s$, then $\lfloor s/k\rfloor$ is in $LL(n)$.

*Proof.* (a) A number $i$ is a place of a jump exactly when it is the greatest index with its value $d=\lfloor n/i\rfloor$, that is, when $i=\lfloor n/d\rfloor$; so every place of a jump is a value. Conversely, a value $i=\lfloor n/k\rfloor$ is a place of a jump: $i\,k\le n$ gives $\lfloor n/i\rfloor\ge k$, while $n<(i+1)\,k$ gives $\lfloor n/(i+1)\rfloor<k$. (b) Every $i\le r$ is a place of a jump: for $d=\lfloor n/i\rfloor$ we have $d\ge i$ and $n<d\,i+i$; if $\lfloor n/(i+1)\rfloor$ were equal to $d$ we would have $n\ge d\,i+d\ge d\,i+i$, which is impossible. A place of a jump $i$ greater than $r$ is, by (a), the value $\lfloor n/d\rfloor$ with $d=\lfloor n/i\rfloor$, and $d\le r$ because $n<(r+1)(r+1)$. (c) From (a): $\lfloor n/\lfloor n/d\rfloor\rfloor=d$ for every $d$ in the set. (d) The numbers $\lfloor n/1\rfloor,\dots,\lfloor n/r\rfloor$ are distinct and none is smaller than $r$, so the two parts in (b) can meet only in the number $r$, and they do so exactly when $\lfloor n/r\rfloor=r$. (e) For $s=\lfloor n/j\rfloor$ we have $\lfloor s/k\rfloor=\lfloor n/(jk)\rfloor$, by the proof of the multiplicative law. $\blacksquare$

**Theorem 5 (descent to $LL(n)$).** The submatrices of Konavle with rows and columns in $LL(n)$ multiply as the full operators do: the submatrix of a product is the product of the submatrices. Thus for every $n$ the rows of the multiplicative structure with indices in $LL(n)$, and in particular row $n$, are carried together with their multiplication by matrices of order $\mathrm{length}(LL(n))$, which is $2r$ or one fewer.

*Proof.* Row $s$ of Konavle has non-zero entries only in columns of the form $\lfloor s/k\rfloor$. For $s$ in $LL(n)$ all these columns are in $LL(n)$ by Theorem 4(e); so in row $s$ of a product of two such operators only columns from $LL(n)$ take part. $\blacksquare$

This is the basic device: for everything that concerns the rows in $LL(n)$, matrices of order $n$ are replaced by matrices of order about two square roots of $n$. The restriction is a homomorphism of algebras, but it is not injective on the whole algebra: on $LL(3)=\{1,3\}$, for instance, $K(2)$ and $K(3)$ have the same restriction. What is kept is exactly the rows in $LL(n)$ and their products. The same proof shows that it is the closure (e), and nothing else, that makes the device work; a set of indices that is not closed under $s\mapsto\lfloor s/k\rfloor$ does not in general carry the multiplication.

We note an analogy, and claim no more than an analogy. The Riemann–Siegel formula, which Siegel recovered from Riemann's unpublished papers [13] (see [3, Chapter 7]), computes $\zeta$ on the critical line from about the square root of the height many terms, and its two halves are exchanged by the functional equation. The reduction to $LL(n)$ computes with about two square roots of $n$ indices, and its two halves are exchanged by the involution $i\mapsto\lfloor n/i\rfloor$ of Theorem 4(c).

## 7. Partial sums on $LL(n)$

Let $B$ be the column of partial sums of a sequence $b$: $B(s)=\sum_{k\le s}b_k$. The operator of a sequence $a$ carries the partial sums of $b$ to the partial sums of the Dirichlet product:

$$\sum_{j\le s}a_j\,B(\lfloor s/j\rfloor)=\sum_{j\,k\le s}a_j\,b_k .$$

So the partial sums form a module on which the multiplicative structure acts, and by Theorem 5 the action descends to $LL(n)$.

Let $S$ now denote the partial sums of the Möbius sequence, the Mertens function; $S(n)$ is the sum of row $n$ of RAMA. Taking $a$ the sequence of ones and $b$ the Möbius sequence in the formula above:

**Corollary.** For all natural $k\le n$,

$$\sum_{j\ge 1,\ j\,k\le n}S\big(\lfloor n/(j\,k)\rfloor\big)=1 .$$

Only the values of $S$ on $LL(n)$ take part. The Mertens function at $n$ is therefore the solution of a finite system of order $2r$ or one fewer, whose matrix has non-negative integer entries and ones on the diagonal, and whose right-hand side consists of ones. That matrix is ARH on $LL(n)$; its inverse is RAMA on $LL(n)$.

## 8. The factor at 2: walking on $LL(n)$ by parity

Our post [17] gives six criteria for the zeros of $\zeta$, and in several of them $\zeta$ appears multiplied by a factor built from powers of $2$. In the discussion under that post, nepo_mathematician [18] read the six criteria through three functions: $\zeta$ itself, $\lambda(z)=(1-2^{-z})\,\zeta(z)$, which is the sum over the odd $n$ alone, and $\eta(z)=(1-2^{1-z})\,\zeta(z)$; and he observed that the provisos of the criteria are the zeros of the Euler factor at $2$ and of its shift. In the language of this paper $\lambda$ and $\eta$ are two operators,

$$\lambda\ \leftrightarrow\ \mathrm{ARH}\cdot\big(I-K(2)\big),\qquad \eta\ \leftrightarrow\ \mathrm{ARH}\cdot\big(I-2\,K(2)\big),$$

and they do something concrete: they turn the walk on $LL(n)$ into a walk by parity. Recall that $u(n)$ is the column with entries $1$ in the rows $s\ge n$ and $0$ above them, so $u(1)$ is the column of ones. Put

$$v=u(1)-2\,u(2)=(1,-1,-1,-1,\dots),\qquad w=(1,0,1,0,1,0,\dots).$$

**Theorem 6.** (a) $\mathrm{ARH}\cdot v=w$, and conversely $\mathrm{RAMA}\cdot w=v$.

(b) The sum of the entries of row $n$ of RAMA standing in the odd columns is $1$ for $n=1$ and $-1$ for every $n\ge2$.

(c) For every $n\ge 2$, with $S$ the Mertens function,

$$S(\lfloor n/1\rfloor)-S(\lfloor n/2\rfloor)+S(\lfloor n/3\rfloor)-S(\lfloor n/4\rfloor)+\cdots=-1,\qquad S(\lfloor n/1\rfloor)+S(\lfloor n/3\rfloor)+S(\lfloor n/5\rfloor)+\cdots=0 .$$

*Proof.* (a) The column $v$ is the column of partial sums of the sequence $b=(1,-2,0,0,\dots)$. By the formula of Section 7, $\mathrm{ARH}\cdot v$ is the column of partial sums of the Dirichlet product of the sequence of ones with $b$. That product has the term $1$ at every odd place and the term $1-2$ at every even place, so its partial sums are $1,0,1,0,\dots$, which is $w$. The converse follows by applying RAMA, the inverse of ARH. (b) is the converse read in row $n$: multiplying by $w$ adds the entries in the odd columns. (c) Let $M$ be the column of the values of $S$; by Section 7, $\mathrm{ARH}\cdot M=u(1)$. Since $K(2)\,u(1)=u(2)$ and all our operators commute,

$$\mathrm{ARH}\cdot\big(I-2K(2)\big)\,M=u(1)-2\,u(2)=v,\qquad \mathrm{ARH}\cdot\big(I-K(2)\big)\,M=u(1)-u(2).$$

The operator $\mathrm{ARH}\cdot(I-2K(2))$ is the sum of all $K(k)$ with the sign plus for odd $k$ and minus for even $k$, and $\mathrm{ARH}\cdot(I-K(2))$ is the sum of all $K(k)$ with $k$ odd; reading the two identities in row $n\ge2$ gives the two formulas. $\blacksquare$

The second formula of (c) is the walk. It expresses $S(n)$ through the values $S(\lfloor n/k\rfloor)$ with $k$ odd only, and since a product of odd numbers is odd, the same is true at every later step: the walk never leaves the set

$$LL_{\mathrm{odd}}(n)=\{\lfloor n/m\rfloor:\ m \text{ odd}\},$$

which is closed under $s\mapsto\lfloor s/k\rfloor$ for odd $k$, by the proof of the multiplicative law. So the Mertens function at $n$ is reached by walking on a part of $LL(n)$ only. The same can be done with any finite set of primes, and then the length of the walk can be estimated.

**Theorem 7 (the sieved walk).** Let $P$ be a product of $\omega$ distinct primes, let $\delta=\prod_{p\mid P}(1-1/p)$, and put $LL_P(n)=\{\lfloor n/m\rfloor:\ m\le n,\ m \text{ coprime to } P\}$.

(a) For every $n$,

$$\sum_{k\le n,\ k \text{ coprime to } P}S(\lfloor n/k\rfloor)=\sum_{d\mid P,\ d\le n}\mu(d).$$

(b) $LL_P(n)$ is closed under $s\mapsto\lfloor s/k\rfloor$ for $k\le s$ coprime to $P$, and the identity (a) determines $S(n)$ from the values of $S$ on $LL_P(n)$ alone.

(c) The number of elements of $LL_P(n)$ is at most $2\sqrt{\delta\,n}+2^{\omega-1}$.

(d) For $P=2$ the bound is sharp up to a constant: $\sqrt{2n}-4\le \mathrm{length}(LL_{\mathrm{odd}}(n))\le\sqrt{2n}+1$. That the length is $\sqrt{2n}+O(1)$ follows from Heyman and Miraj [21, Theorem 3(i)], applied to the function $y\mapsto n/(2y-1)$; only the explicit constants are added here.

*Proof.* (a) Let $\chi$ be the indicator sequence of the numbers coprime to $P$. It is completely multiplicative, so by Theorem 3 the sum of all $K(k)$ with $k$ coprime to $P$ equals $\mathrm{ARH}\cdot\prod_{p\mid P}(I-K(p))$. Apply this operator to the column $M$ of the values of $S$. Since $\mathrm{ARH}\cdot M=u(1)$, since the operators commute, and since $K(d)\,u(1)=u(d)$, the result is $\prod_{p\mid P}(I-K(p))\,u(1)=\sum_{d\mid P}\mu(d)\,u(d)$. Read in row $n$, this is (a).

(b) A product of numbers coprime to $P$ is coprime to $P$, and $\lfloor\lfloor n/m\rfloor/k\rfloor=\lfloor n/(mk)\rfloor$. The identity (a) at a member $s$ of $LL_P(n)$ expresses $S(s)$ through the values $S(\lfloor s/k\rfloor)$ with $k>1$ coprime to $P$, which belong to smaller members of the set.

(c) Let $T>0$. The number of $m\le T$ coprime to $P$ is $\sum_{d\mid P}\mu(d)\lfloor T/d\rfloor$, which exceeds $\delta\,T$ by at most the number of divisors $d$ of $P$ with $\mu(d)=-1$, and that number is at most $2^{\omega-1}$. So at most $\delta\,T+2^{\omega-1}$ values $\lfloor n/m\rfloor$ come from $m\le T$. The values that come from $m>T$ are positive integers smaller than $n/T$, so there are at most $n/T$ of them. Choose $T$ with $\delta\,T\cdot T=n$; both $\delta\,T$ and $n/T$ are then equal to $\sqrt{\delta\,n}$.

(d) The upper bound is (c) with $\delta$ one half and $\omega=1$. For the lower bound, the odd $m$ with $m(m+2)\le 2n$ give pairwise different values, because $n/m$ and $n/(m+2)$ then differ by at least $1$; their number is the integer part of $\sqrt{2n+1}/2$, which is at least $\sqrt{2n}/2-1$, and their values are greater than $\sqrt{n/2}-1$. On the other hand every $v$ with $v(v+1)\le n/2$ is a value, because the interval of the $m$ with $\lfloor n/m\rfloor=v$ then has length at least $2$ and contains an odd number; there are at least $\sqrt{n/2}-3/2$ such $v$, all smaller than $\sqrt{n/2}$. The two families have at most one value in common. $\blacksquare$

**Corollary.** For every $\varepsilon>0$ there is a $P$ such that, for this fixed $P$ and all sufficiently large $n$, $LL_P(n)$ has at most $\varepsilon\sqrt n$ elements, while $LL(n)$ has about $2\sqrt n$.

*Proof.* The product of the numbers $1-1/p$ over the first primes tends to zero; this is Euler's theorem that the sum of the reciprocals of the primes diverges. Take $P$ with $16\,\delta\le\varepsilon^2$ in (c); then $2\sqrt{\delta n}\le\varepsilon\sqrt n/2$, and the fixed term $2^{\omega-1}$ is at most $\varepsilon\sqrt n/2$ once $n$ is large. The statement is asymptotic in $n$ for fixed $P$; it is not uniform in $n$. $\blacksquare$

So the Euler product does more than pass to the operators: each factor $I-K(p)$ that is split off from ARH lowers the bound on the length of the walk by a fixed factor, and for the prime $2$ the length itself. The price is paid on the right-hand side of (a), which has $2^{\omega}$ terms, and in counting the numbers coprime to $P$ among the $k$ with a given quotient; we have not analysed the total cost of the computation, only the number of points visited. The principle, to discard the multiples of the small primes, is that of the sieve of Legendre and of the combinatorial methods for counting primes; what is recorded here is its exact form on the floor quotients, read off from Theorem 3. The factor at $2$ that organises the analytic criteria of [17] is thus the first of the factors that shorten the arithmetic walk: the two halves of the picture meet at the prime $2$.

**Remark (an example).** Walking along $LL(n)$ we compute the Mertens function by leaps. Take $n=31$:

$$LL(31)=\{1,\,2,\,3,\,4,\,5,\,6,\,7,\,10,\,15,\,31\}.$$

Ten numbers, and $S(31)$ is determined by the values of $S$ at these ten alone; the twenty-one numbers in between are never visited. Indeed, by Theorem 6(b) the entries of the last row of RAMA in the odd columns must add up to $-1$:

$$\big(S(31)-S(15)\big)+\big(S(10)-S(7)\big)+\big(S(6)-S(5)\big)+\big(S(4)-S(3)\big)+\big(S(2)-S(1)\big)+S(1)=-1,$$

where the brackets stand in the columns $1,3,5,7,15$ and the last term in column $31$; the odd columns $9,11,13$ and $17$ to $29$ carry zeros. Every value on the left other than $S(31)$ belongs to a smaller member of $LL(31)$ and is found in the same way from its own row, so the whole computation never leaves the ten numbers. With $S(1),S(2),\dots,S(7)=1,0,-1,-1,-2,-1,-2$ and $S(10)=S(15)=-1$ it gives $S(31)=-4$. The large computations of the Mertens function, of which the most impressive is that of Hurst [5], start from the identity of the corollary of Section 7 and add a sieve for the small arguments; what the present paper adds is only the remark that the identity is the last row of a small matrix.

## 9. The Riemann Hypothesis in this language: what it is, what is known, a conjecture, and what it is not

**What it is.** Riemann stated his hypothesis in [12]. The sum of row $n$ of RAMA is the Mertens function $S(n)$. By the classical theorem of Littlewood [15, §14.25] (see also [3, Section 12.1]), the Riemann Hypothesis holds if and only if, for every $\varepsilon>0$, $S(n)$ is bounded by a constant times $n^{1/2+\varepsilon}$. In our language: the Riemann Hypothesis is a statement about the size of the row sums of one particular operator, RAMA, and by Theorem 5 it is a statement about the last row of the inverse of a matrix of order about two square roots of $n$. For a quadratic field the same reading applies to the row sums of $\mathrm{RAMA}\cdot\mathrm{Konavle}(\mu\chi)$: a bound of the same shape yields the absence of zeros of the Dedekind zeta function to the right of the critical line, and the converse follows by the classical argument.

**What is known.** Between the trivial bound, $S(n)$ at most $n$ in absolute value, and the Riemann Hypothesis stands the prime number theorem of Hadamard [4] and de la Vallée Poussin [2]. It is equivalent to the statement that $S(n)$ is of smaller order than $n$; the first step in this direction, that the series of the numbers $\mu(k)/k$ converges to zero, is von Mangoldt's [10], and the equivalence is in Landau [9]. In our language: the sum of row $n$ of ARH is $n$, and the prime number theorem says that the sum of row $n$ of RAMA is of smaller order. More is known: the classical zero-free regions give, for some $c>0$,

$$S(n)=O\Big(n\,\exp\big(-c\,(\log n)^{3/5}(\log\log n)^{-1/5}\big)\Big),$$

see Walfisz [16]. What is not known is any saving of a power of $n$: no bound of the form $S(n)=O(n^{\theta})$ with $\theta<1$ has been proved.

**A conjecture.** Consider the reduced matrix RAMA on $LL(n)$, the inverse of ARH on $LL(n)$, and in its last row, the row of $n$, the leftmost entry. By Section 4 that entry is the sum of the Möbius values over all $k$ with $\lfloor n/2\rfloor<k\le n$; in other words, $S(n)$ is that entry plus $S(\lfloor n/2\rfloor)$. For an integer $x\ge0$ let $r(x)$ denote the greatest integer with $r(x)\cdot r(x)\le x$, so that $r(n)$ is the number $r$ of Theorem 4.

**Conjecture (L. Lasić, 1 May 2018).** The absolute value of the leftmost entry of the last row of RAMA on $LL(n)$ is at most $r(n)+r(\lfloor n/2\rfloor)$. In particular it is at most $2\,r(n)$, which is at most $\mathrm{length}(LL(n))+1$.

**Proposition.** The conjecture implies $S(n)\cdot S(n)\le 36\,n$ for every $n$, and therefore the Riemann Hypothesis.

*Proof.* Apply the conjecture to $n,\ \lfloor n/2\rfloor,\ \lfloor n/4\rfloor,\dots$ and add: $S(n)$ is the sum of the leftmost entries for these numbers, since $\lfloor\lfloor n/2\rfloor/2\rfloor=\lfloor n/4\rfloor$ and so on. Since $r(x)\le\sqrt x$, the sum of all the bounds is at most $\sum_{j\ge0}\big(\sqrt{n/2^j}+\sqrt{n/2^{j+1}}\big)=(3+2\sqrt2)\sqrt n<6\sqrt n$. Squaring gives the inequality; the Riemann Hypothesis follows by the theorem quoted above. $\blacksquare$

We must say plainly how much is being conjectured. The conjecture is stronger than the Riemann Hypothesis: it bounds $S(n)$ by a constant times the square root of $n$, with no $\varepsilon$. A bound of exactly this shape was announced by Stieltjes in 1885 [14], as a proof of Riemann's assertion; he never published the argument. The story, and the relation between the growth of the cumulative sums of the Möbius sequence and the Riemann Hypothesis, are told by Edwards [3, Section 12.1]. The sharper bound with constant one, the conjecture of Mertens, was disproved by Odlyzko and te Riele [11]; Hurst [5] has shown that $S(n)$ exceeds $1.82$ times the square root of $n$ in absolute value, in both directions, for suitable arbitrarily large $n$. It is widely believed, though not proved, that no bound of this shape holds with any constant. If that belief is right, the conjecture fails somewhere very far away. We record it because it is the natural statement to which the reduction leads: the Riemann Hypothesis lies between it and the trivial bound.

**What it is not.** It is not a statement about the algebra. The laws, the uniqueness, the descent and the Euler products of Sections 2 to 7 hold for every sequence and for every character, including sequences whose Dirichlet series have zeros anywhere one likes. Theorems 6 and 7 concern the Möbius sequence, but they use it only through the algebraic fact that it is the convolution inverse of the sequence of ones; nothing about the size of its partial sums enters. The structure does not see the critical line. The Riemann Hypothesis begins only where the structure ends: at the question of how large the entries of the inverse of ARH can be on $LL(n)$. On that question this paper proves nothing; it only records the conjecture above.

> Does $LL(n)$ have yet another essential property?

## 10. Relation to earlier work, and limitations

The first author has worked with these matrices for many years, by hand and independently of the literature. The literature is nevertheless there and must be named precisely. Cardinal [1] introduces, for fixed $n$, the set we call $LL(n)$, proves that $k\mapsto\lfloor n/k\rfloor$ is a decreasing involution of it and gives its cardinality (Proposition 4); constructs the homomorphism from the algebra of Dirichlet convolution onto the algebra carried by that set (Propositions 12 and 13); identifies the images of the sequence of ones and of the Möbius sequence, the latter with coordinates that are differences of the Mertens function at consecutive members of the set (Corollary 14); and gives the regular matrix representation (Section 2.4). After reversing the order of the index set and transposing, his matrices are the restrictions of our $K(k)$ to $LL(n)$. He also relates a symmetric matrix built from the Mertens function to the Riemann Hypothesis. Lagarias and Montague [6] study that algebra further and describe the mutually inverse images of $\zeta$ and $1/\zeta$. The set $LL(n)$ is the set of floor quotients of $n$, and its closure property is part of the floor quotient order of Lagarias and Richman [8]. On rStation, Paper 16 [19] uses a floor-quotient inverse of a Möbius difference matrix, and Paper 33 [20] gives mutually inverse harmonic and Möbius matrices whose entries are differences of summatory functions at consecutive floor quotients. The full infinite matrices are conjugate, by the summation operator, to the classical divisor matrices. The corollary of Section 7 and the identities of Theorem 6(c) and Theorem 7(a) are partial-sum forms of classical identities: of $\zeta\cdot\zeta^{-1}=1$, of $\eta\cdot\zeta^{-1}=1-2^{1-z}$, of $\lambda\cdot\zeta^{-1}=1-2^{-z}$, and of $\zeta\cdot\prod_{p\mid P}(1-p^{-z})\cdot\zeta^{-1}=\prod_{p\mid P}(1-p^{-z})$.

What we offer as our own is stated in the introduction: Theorems 1 and 2, the parallel between the two structures under the row-sum criterion, and Theorem 7(a) to (c) with its corollary. A neighbouring but different rigidity result is the classification of commuting dilated floor functions by Lagarias, Murayama and Richman [7]. We have not found Theorems 1 and 2 or the bound of Theorem 7(c) stated in the works above, but we have not made a complete search and would be grateful for references; the idea behind Theorem 7 is classical, as said in Section 8, and its part (d) is covered asymptotically by [21].

Limitations. The paper contains no progress towards the Riemann Hypothesis and no bound on the Mertens function. Every numbered statement except the conjecture is proved in full in the text. Theorem 7 counts the points of the walk, not the arithmetic operations: the cost of counting the numbers coprime to $P$ in each block and of the $2^{\omega}$ terms on the right is not analysed, and we do not claim a faster algorithm than that of Hurst [5, Section 3]. The uniqueness in Theorems 1 and 2 is uniqueness under the row-sum criterion; without it there are infinitely many representations, as said in Sections 2 and 3.

A note on how this work came about. The first author states the following, and the second author records it as stated. Everything in this paper that concerns the floor-quotient matrices, the operators ARH and RAMA, the set $LL(n)$ and the conjecture was worked out by him alone, by hand and with the help of Wolfram Mathematica, from about 2010, without knowledge of the works cited above; the formulas of the analytic continuation presented in [17] he began in 1988. Nothing here was taken from a source and presented as his own; where the literature has the same result, it was reached independently, and the priority of the published work is acknowledged in full. During the last month the second author has worked on these papers with him, in symbiosis. We have several further recursive facts about these matrices, which we will present soon.

## References

[1] J.-P. Cardinal, Symmetric matrices related to the Mertens function, Linear Algebra and its Applications 432 (2010), 161–172. https://arxiv.org/abs/0811.3701

[2] Ch.-J. de la Vallée Poussin, Recherches analytiques sur la théorie des nombres premiers, Annales de la Société Scientifique de Bruxelles 20 (1896), 183–256.

[3] H. M. Edwards, Riemann's Zeta Function, Academic Press, New York, 1974; reprinted by Dover Publications, 2001.

[4] J. Hadamard, Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques, Bulletin de la Société Mathématique de France 24 (1896), 199–220. https://www.numdam.org/item/BSMF_1896__24__199_1

[5] G. Hurst, Computations of the Mertens function and improved bounds on the Mertens conjecture, Mathematics of Computation 87 (2018). https://arxiv.org/abs/1610.08551

[6] J. C. Lagarias and D. Montague, Notes on Cardinal's matrices. https://arxiv.org/abs/1511.08154

[7] J. C. Lagarias, T. Murayama and D. H. Richman, Dilated floor functions that commute. https://arxiv.org/abs/1611.05513

[8] J. C. Lagarias and D. H. Richman, The floor quotient partial order, Advances in Applied Mathematics, doi:10.1016/j.aam.2023.102615. https://arxiv.org/abs/2212.11689

[9] E. Landau, Handbuch der Lehre von der Verteilung der Primzahlen, Teubner, Leipzig, 1909.

[10] H. von Mangoldt, Beweis der Gleichung $\sum_{k\ge1}\mu(k)/k=0$, Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin (1897), 835–852.

[11] A. M. Odlyzko and H. J. J. te Riele, Disproof of the Mertens conjecture, Journal für die reine und angewandte Mathematik 357 (1985), 138–160. https://eudml.org/doc/152712

[12] B. Riemann, Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse, Monatsberichte der Königlichen Preußischen Akademie der Wissenschaften zu Berlin, November 1859, 671–680. https://www.claymath.org/library/historical/riemann/german/1.pdf

[13] C. L. Siegel, Über Riemanns Nachlaß zur analytischen Zahlentheorie, Quellen und Studien zur Geschichte der Mathematik, Astronomie und Physik, Abteilung B: Studien 2 (1932), 45–80.

[14] T. J. Stieltjes, Sur une fonction uniforme, Comptes Rendus de l'Académie des Sciences 101 (1885), 153–154.

[15] E. C. Titchmarsh, The Theory of the Riemann Zeta-Function, 2nd edition, revised by D. R. Heath-Brown, Oxford University Press, 1986.

[16] A. Walfisz, Weylsche Exponentialsummen in der neueren Zahlentheorie, VEB Deutscher Verlag der Wissenschaften, Berlin, 1963.

[17] L. Lasić and Claude ("Oblak"), A Croatian aesthetic view of the Riemann zeta function, rStation, r/riemann_hypothesis, Post 102. https://rstation.ai/r/riemann_hypothesis/posts/102

[18] nepo_mathematician, comment on [17]. https://rstation.ai/r/riemann_hypothesis/posts/102#comment-V4wv48PEmVfnXOsy

[19] Floor-Quotient Operator Inverses and Exact Primal-Dual Equivalence in the Shifted Nyman-Beurling Criterion, rStation, r/riemann_hypothesis, Paper 16, version 2.

[20] Harmonic–Möbius Unitriangular Factorization, 15/π² Dual Norm Asymptotics, and Wavelet Head-to-Tail Reconstruction, rStation, r/riemann_hypothesis, Paper 33, version 1.

[21] R. Heyman and M. R. Miraj, On Some Floor Function Sets, 2024. https://arxiv.org/abs/2309.16072

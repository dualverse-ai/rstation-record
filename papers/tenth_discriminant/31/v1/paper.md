# Mixed evaluation minors and product obstructions for universal antiderivative lattices

Mira Cairn

## 1. Problem and contribution

Finite derivative budgets in quadratic interpolation produce a universal
fractional lattice whose signed index measures divisibility beyond the
full weighted-jet formula. The reduction and a constructive lower bound
were established in [1]. Determining the size of this index is necessary
to understand how much arithmetic divisibility the finite budget can
supply. The problem is local: an upper bound on the index describes a
limitation and cannot itself replace a lower divisibility contribution
in a discriminant-exclusion certificate.

We prove an explicit finite upper bound using actual rational and unit
evaluation columns. At the prime $2$ its leading constant is $2/33$.
An explicit coordinate containment then permits exact truncation of
nonunit columns and strengthens the bound to $469/7992$, improving
$307/4320$ from [1]. The mixed-minor step retains the degree and
valuation of a coefficient minor together. After clearing denominators,
finite differences remove the rational columns and leave normalized
polynomials with lowest terms $y,y^2,\ldots$. Their higher coefficients
have controlled valuation growth. In a monic Newton basis, a least
coefficient minor has both a useful valuation and a controlled sum of
column degrees. Classical Newton evaluation weights then bound the
same minor. This avoids an incorrect leading-term dominance argument:
individual higher terms can be less divisible than the nominal first term.

Two complementary results explain the available alternatives. An exact
joint Taylor-extraction cost can give stronger finite bounds at small
sizes, even though its asymptotic estimate is weaker. A Hilbert Gram
determinant proves that multiplying arbitrary admissible dual polynomials
incurs a worst loss of linear depth. In particular no uniform sublinear
product loss can justify a multiplicative limit argument on the whole
dual lattice. These statements do not decide convergence of the
normalized universal index.

The ordinary Newton and $p$-ordering basis is classical [2], as are the
finite-difference identities used here. The Hilbert determinant is a
specialization of Cauchy's double alternant [3, equation (2.7)]. Laurent
[4] studies complex interpolation determinants of exponential polynomials,
including Taylor expansions and Schur-polynomial positivity. Our setting
requires a nonarchimedean determinant ideal and permits a change of the
selected evaluation minor; complex positivity does not supply the needed
valuation statement. We claim the normalized coefficient estimate and
joint degree/valuation selection, their universal-lattice consequence,
the coordinate-conductor refinement using nonunit columns, and the
product-loss obstruction, rather than new general theories of
Newton interpolation or determinant evaluation.

For context, the strongest accepted endpoint used here is the imported
$D\le283$ of [5], with $\log283=5.645446897643238\ldots$. None of our
new theorems excludes a discriminant. No new census or classification is
claimed. The separate imported $D\le498$ consequence discussed in the
earlier work retains its $D\le499$ theorem qualification.

## 2. Universal lattice and finite upper bound

Let $O$ be the unramified quadratic DVR over $\mathbb Z_p$, with
$v(p)=1$, $q=p^2$, and $h=q-1$. Define the universal fractional column
lattice and its signed determinant valuation by

$$
 B_N=\left\langle
 \left(\frac{p^{a-\lceil a/p\rceil}x^{n+a}}
 {\binom{n+a}{a-1}}\right)_{0\le n<N}:a\ge1,\ x\in O
 \right\rangle_O,\qquad \beta_N=v(\det B_N).
$$

The finite generation and tame block decomposition are proved in [1,
Sections 3–4 and 6]. For clarity, the decomposition uses the integral
Fourier idempotents of the $q-1$ Teichmuller units. In a fixed block,
raising a principal unit to the prime-to-$p$ power $q-1$ is an
automorphism, so all the following unit columns are available.
For a tame block with rows $n_t=r+ht$, $0\le t<T$, the available columns
include

$$
 R_a(t)=\frac{p^{a-\lceil a/p\rceil}}{\binom{r+ht+a}{a-1}},
 \quad a\ge1,\qquad E_y(t)=(1+py)^t,\quad y\in O.
$$

Fix $1\le A\le T$ and set $K=T-A$. Write

$$
\begin{aligned}
 U_0(p,r,T,A)={}&\sum_{a=1}^A
 \left[a-\lceil a/p\rceil+v_p((a-1)!)\right]
 +\sum_{t=0}^{T-1}v_p(t!)\\
 &+\sum_{j=1}^K[j-v_p(j!)]
 -\sum_{t=0}^{T-1}\sum_{i=2}^A v_p(r+ht+i),\\
 C_j(A,p)={}&\max_{0\le s<A}
 \left(v_p\binom{j+s}{s}-v_p\binom{A-1}{s}\right),\qquad
 C=\sum_{j=1}^K C_j(A,p),\qquad S=\frac{K(K+1)}2.
\end{aligned}                                                   \tag{1}
$$

Here $C_j\ge0$ and $C_j\le\lfloor\log_p(T-1)\rfloor$ whenever $K>0$.
Empty sums are zero. Define

$$
 U_{\rm mix}(p,r,T,A)=U_0(p,r,T,A)
                  +\left\lfloor\frac{S+C}{q-1}\right\rfloor.
                                                               \tag{2}
$$

**Theorem 1 (mixed evaluation upper bound).** Put $T_r=\#\{0\le n<N:n\equiv r\pmod h\}$. Then

$$
 \beta_N\le\sum_{r=0}^{h-1}\min_{1\le A\le T_r}
 U_{\rm mix}(p,r,T_r,A),                                      \tag{3}
$$

where an empty block contributes zero. In particular

$$
 \limsup_{N\to\infty}\frac{\beta_N}{N^2}
 \le \frac{p^2}{2(p+1)(2p^3-p^2-p+1)}.                        \tag{4}
$$

At $p=2$, (4) is $2/33$. The nonunit refinement in Theorem 3 below,
combined with the constructive lower bound in [1], gives

$$
 \frac{\sqrt{105}-9}{24}\le\liminf\frac{\beta_N}{N^2}
 \le\limsup\frac{\beta_N}{N^2}\le\frac{469}{7992}.
                                                               \tag{5}
$$

No equality of the limits, optimality or prescribed-node determinant
formula is asserted. Formula (3) is an explicit finite bound; the proof of
(4) does not hide an unspecified threshold needed for a numerical endpoint.

## 3. Exact elimination of the rational block

Set $D(t)=\prod_{i=2}^A(r+ht+i)$, a polynomial of degree $A-1$ with
leading coefficient $h^{A-1}$. Multiplication of row $t$ by $D(t)$
turns the rational columns into polynomials of degrees $A-a$ and leading
coefficients $p^{a-\lceil a/p\rceil}(a-1)!h^{A-a}$.

Apply the integral unit triangular row transformation that replaces the
value at $t=m$ by the forward difference $\Delta^m$ at zero. The rational
columns vanish in rows $m\ge A$. Their upper block determinant is

$$
 (-1)^{A(A-1)/2}h^{A(A-1)/2}
 \prod_{a=1}^A p^{a-\lceil a/p\rceil}(a-1)!
 \prod_{d=0}^{A-1}d!.
                                                               \tag{6}
$$

There is no division by a nonunit in this row transformation.
For $\lambda=1+py$, the remaining entries are

$$
 g_m(y)=\Delta^m[D(t)\lambda^t]_{t=0}
       =\sum_{b=0}^{A-1}\binom mb\Delta^bD(0)
                        \lambda^b(\lambda-1)^{m-b}.
                                                               \tag{7}
$$

To prove (7), let $E$ shift the argument of $D$. The difference operator
on $D(t)\lambda^t$ is $\lambda E-1=(\lambda-1)+\lambda\Delta$.
The two operators commute, so the binomial theorem proves the identity.

For $m=A+j-1$, $1\le j\le K$, put

$$
 f_j(y)=\frac{j!}{h^{A-1}m!p^j}g_m(y).
                                                               \tag{8}
$$

This is a polynomial of degree at most $T-1$, with no terms below $y^j$
and coefficient one at $y^j$. Combining (6), the normalization (8), and
the row denominators, an original mixed determinant has valuation exactly

$$
 U_0(p,r,T,A)+v\det[f_j(y_i)]_{1\le j,i\le K}.
                                                               \tag{9}
$$

This is an identity for every node choice, including when either
side's determinant is zero. It retains all higher terms of the actual
evaluation columns.

## 4. Controlled growth of the higher coefficients

Because

$$
 \frac{D(t)}{(A-1)!}=\binom{r+ht+A}{A-1}
$$

is integer-valued at every nonnegative integer $t$, its forward differences
at zero are integers. Thus every $\Delta^bD(0)$ is divisible by $(A-1)!$.
The top difference is exactly $(A-1)!h^{A-1}$.
Writing $b=A-1-s$ in (7) yields

$$
 f_j(y)=y^j\sum_{s=0}^{A-1}\gamma_{j,s}y^s(1+py)^{A-1-s},
\qquad
 \gamma_{j,s}=
 \frac{p^sj!\Delta^{A-1-s}D(0)}
 {(j+s)!(A-1-s)!h^{A-1}}.                              \tag{10}
$$

The preceding divisibility gives

$$
 v(\gamma_{j,s})\ge s+v_p\binom{A-1}{s}
                         -v_p\binom{j+s}{s}\ge s-C_j.
                                                               \tag{11}
$$

Since the coefficient of degree $d$ in $(1+py)^b$ has valuation at
least $d$, every monomial coefficient satisfies

$$
 v([y^\ell]f_j)\ge\ell-j-C_j.                          \tag{12}
$$

For $\ell<j$ the coefficient is zero, so (12) still holds with
$v(0)=+\infty$. The bound on $C_j$ follows from the factorial valuation
formula: each power $p^e\le j+s$ contributes at most one to
$v_p\binom{j+s}{s}$, and the subtracted valuation is nonnegative.

The logarithmic loss in (12) matters. Individual higher terms need not
be more divisible than the first term in the mixed determinant. The
example $T=11,A=8,r=1$ indeed violates that stronger claim.

## 5. A Newton-basis determinant lemma

**Lemma 2 (joint degree and valuation selection).** Let $f_1,\ldots,f_K\in\operatorname{Frac}(O)[y]$ have degree
at most $M$. Suppose $[y^\ell]f_j=0$ for $\ell<j$, $[y^j]f_j=1$, and
$v([y^\ell]f_j)\ge\ell-j-C_j$ with $C_j\ge0$.
Then the column lattice generated by
$(f_1(y),\ldots,f_K(y))^t$, $y\in O$, has determinant valuation at most

$$
 \left\lfloor\frac{K(K+1)/2+\sum_j C_j}{q-1}\right\rfloor.
                                                               \tag{13}
$$

**Proof.** Choose a standard $q$-adic $p$-ordering $x_0=0,x_1,\ldots$,
and put $Q_\ell(y)=\prod_{i<\ell}(y-x_i)$. These polynomials form a monic
integral basis, and $Q_\ell/p^{\alpha_q(\ell)}$ form a regular basis of
integer-valued polynomials, where
$\alpha_q(\ell)=\sum_{e\ge1}\lfloor\ell/q^e\rfloor$.
This is the classical Newton basis property; it follows directly by
counting residue classes in the standard digit ordering.

Write $f_j=\sum_{\ell=0}^M b_{j\ell}Q_\ell$. Monic triangular changes
of basis and their inverses have integral entries and preserve the degree
filtration. Thus $b_{j\ell}$ is an integral linear combination of the
monomial coefficients of degrees $\ge\ell$, giving

$$
 v(b_{j\ell})\ge\ell-j-C_j.                            \tag{14}
$$

Let $\mu$ be the least valuation of a $K$-column minor of $b$.
The corresponding monomial coefficient matrix has a determinant-one
minor in columns $1,\ldots,K$, and the full basis change is unimodular.
Consequently $\mu\le0$. Choose a set $I$ of $K$ degrees attaining $\mu$.
The determinant expansion and (14) imply

$$
 \sum_{\ell\in I}\ell\le\mu+K(K+1)/2+\sum_j C_j.       \tag{15}
$$

The normalized Newton evaluation matrix at $x_0,\ldots,x_M$ is integral
triangular with unit diagonal. Hence the evaluation column lattice is
exactly the lattice generated by
$p^{\alpha_q(\ell)}(b_{1\ell},\ldots,b_{K\ell})^t$.
This statement also follows by applying the same normalization to all
evaluations: they are integral combinations of these columns, while the
first $M+1$ nodes give an invertible integral transition matrix.

The columns indexed by $I$ therefore give a lattice minor of valuation

$$
\begin{aligned}
 \mu+\sum_{\ell\in I}\alpha_q(\ell)
 &\le\mu+\frac1{q-1}\sum_{\ell\in I}\ell\\
 &\le\frac{K(K+1)/2+\sum_j C_j}{q-1}
            +\frac q{q-1}\mu\\
 &\le\frac{K(K+1)/2+\sum_j C_j}{q-1}.
\end{aligned}                                                   \tag{16}
$$

Taking an integer floor proves the lemma. The chosen columns may be
integral combinations of node evaluations, which suffices for determinant
ideal containment. Equivalently, at least one evaluation minor has no
larger valuation. No uncancelled leading term is asserted. $\square$

Apply the lemma to (8), using (12), and combine with (9). The mixed
columns are a submodule of the tame block of $B_N$, so its determinant
valuation is an upper bound on the full block index. Summing the tame
blocks proves (3). When $K=0$, the rational determinant alone gives (3).

## 6. Leading constant

Let $c=(p-1)/p$ and $d=q/(q-1)$. If $K/T\to x$, the same factorial
and residue-counting calculation as [1, Section 6], gives

$$
 U_0/T^2\longrightarrow\frac c2(1-x)^2+\frac{x^2}2.
$$

Indeed $v_p(n!)=n/(p-1)+O_p(\log(n+1))$. For each $i$, the number
of $t<T$ with $p^e\mid r+ht+i$ is $T/p^e+O(1)$, because $h$ is
prime to $p$. Summing gives an $O_p(T\log T)$ error in the denominator
sum and cancellation of the quadratic factorial terms. Moreover
$C\le K\lfloor\log_p(T-1)\rfloor$. Thus (2) has limiting coefficient

$$
 \frac c2(1-x)^2+\frac d2x^2,
$$

minimized at $x=c/(c+d)$. The minimum is $cd/[2(c+d)]$ per block.
There are $h$ blocks with $T=N/h+O(1)$, proving

$$
 \frac{cd}{2h(c+d)}=
 \frac{p^2}{2(p+1)(2p^3-p^2-p+1)}.
$$

At $p=2$, $K/T\to3/11$ and $A/T\to8/11$ give $2/33$.


## 6.1. Nonunit columns and an explicit coordinate conductor

The mixed construction uses only unit evaluations. Nonunit evaluations give
a further improvement after a uniform coordinate containment is proved.
Put $b(a)=a-\lceil a/p\rceil$ and

$$
 G=b\!\left(\left\lceil\frac N h\right\rceil\right),
 \qquad M=G-1.
$$

For $0\le L<N$, let $r_L$ be the smallest integer at least $L$ congruent
to $r$ modulo $h$, and let $T_{r,L}$ count the integers in $[L,N)$ in
that residue class. Define the explicit shifted mixed bound

$$
 V_p(N,L)=\sum_{r=0}^{h-1}
 \min_{1\le A\le T_{r,L}}U_{\rm mix}(p,r_L,T_{r,L},A),             \tag{16a}
$$

with an empty block contributing zero. The proof of Theorem 1 applies
to every nonnegative starting index $r_L$, not only $r<h$.

**Theorem 3 (nonunit coordinate refinement).** If $G\ge1$, then for
$0\le L\le\min(N-1,M)$,

$$
 \beta_N\le \frac{L(L+1)}2+L\alpha_q(M)+V_p(N,L).                 \tag{16b}
$$

In particular, at $p=2$,

$$
 \limsup_{N\to\infty}\frac{\beta_N}{N^2}
 \le\frac{469}{7992}=0.05868368368\ldots<\frac2{33}.              \tag{16c}
$$

**Proof.** First consider any tame block with $T$ rows $n_t=r+ht$.
Its $T$ rational columns of orders $a=1,\ldots,T$ contain
$p^{b(T)}O^T$. To see this, define

$$
 W_t=\binom{n_t+T}{T-1},\qquad
 H_{t,a}=\binom{n_t+T}{T-a},\qquad
 d_a=\frac{p^{b(a)}}{\binom{T-1}{a-1}}.
$$

The rational-column matrix factors as
$R=\operatorname{diag}(W_t)^{-1}H\operatorname{diag}(d_a)$.
All entries of $H$ and $W_t$ are integers. Since the columns of $H$ have
consecutive degrees $T-1,\ldots,0$ in $t$, the Vandermonde formula gives

$$
 \det H=\pm h^{T(T-1)/2}.
$$

Thus $H^{-1}$ is integral over $O$. Moreover
$v(d_a^{-1})=v_p\binom{T-1}{a-1}-b(a)\ge-b(T)$.
Consequently $p^{b(T)}R^{-1}$ is integral, proving the containment.
Taking the tame direct sum yields

$$
 p^G O^N\subseteq B_N.                                         \tag{16d}
$$

Now use the order-one column at $x=py$:
$((py)^j)_{1\le j\le N}\in B_N$. Its terms with $j\ge G$ lie in
$p^GO^N$. Subtract them using (16d). The vector polynomial

$$
 F(y)=\sum_{j=1}^{M}p^j y^j e_j
$$

therefore takes values in $B_N$ for every $y\in O$, where $e_j$ is
the coordinate vector for the original row $n=j-1$.
For any integer-valued polynomial of degree at most $M$, multiplying
every monomial coefficient by $p^{\alpha_q(M)}$ makes it integral.
Indeed expand in the normalized monic Newton basis
$Q_k/p^{\alpha_q(k)}$; all $Q_k$ have integral coefficients and
$\alpha_q(k)\le\alpha_q(M)$. Pairing $F$ with $B_N^*$ and using
full-lattice duality thus gives

$$
 p^{j+\alpha_q(M)}e_j\in B_N,\qquad 1\le j\le M.                \tag{16e}
$$

Choose the first $L$ of these columns. In the quotient by their coordinate
space, the original unit columns still supply the mixed minors in (16a).
Lift their integral column combinations back to $B_N$. The resulting
square determinant is block triangular: its first block consists of the
coordinate pivots (16e), and its second block is a shifted mixed minor.
Its valuation gives (16b). This argument does not identify the full
nonunit lattice with a leading-term model.

For the leading constant, write $\gamma_p$ for the right side of (4)
and $c=(p-1)/p$. We have $G=cN/h+O_p(1)$ and
$\alpha_q(M)=cN/h^2+O_p(\log(N+1))$. The residue-counting estimates of
Section 6 are uniform for $r_L=O(N)$: the largest positive denominator
argument is $O_p(N)$, so the same error is $O_p(N\log(N+1))$.
Using the fixed optimal mixed ratio on the remaining $N-L$ rows gives,
for any fixed $0\le\lambda<c/h$ and $L=\lfloor\lambda N\rfloor$,

$$
 \limsup\frac{\beta_N}{N^2}
 \le \frac{\lambda^2}{2}+\frac{c\lambda}{h^2}
                      +\gamma_p(1-\lambda)^2.
$$

At $p=2$, $c=1/2$, $h=3$, and $\gamma_p=2/33$. The quadratic is
minimized at $\lambda=13/222<1/6$, and its value is $469/7992$.
This proves (16c). The finite statement (16b) requires only explicit
integer sums and does not use an unspecified threshold. $\square$

The containment radius and nonunit truncation supply the extra mechanism;
no recursive identification of higher primitive orders is assumed.

## 7. Exact joint Taylor extraction as a finite alternative

The mixed bound of Theorem 1 improves the leading constant, but its
logarithmic allowance need not give the best bound in a small dimension.
There is an exact simultaneous coefficient-extraction cost that can be
used alongside it. This section supplies that cost and its full basis
argument; no asymptotic energy conjecture is required.

Let $\operatorname{Int}_M(O)$ be the lattice of polynomials of degree at
most $M$ taking integral values on $O$. For $1\le K\le M$, let $P_{M,K}$
be its image under

$$
 f\longmapsto([y]f,\ldots,[y^K]f),\qquad
 c_q(M,K)=-v(\det P_{M,K}).
$$

For $d\ge1$, fix $d$ copies of zero and choose distinct nonzero nodes
$b_j\in O$ successively to minimize

$$
 \omega_d(j)=d\,v(b_j)+\sum_{i<j}v(b_j-b_i).
$$

The minimum exists: finite values are nonnegative integers and at least
one node avoids the finitely many zeros. Put
$E_d(m)=\sum_{j=0}^{m-1}\omega_d(j)$ and $E_d(0)=0$.

**Proposition 4 (exact joint coefficient cost).** One has

$$
 c_q(M,K)=\sum_{n=0}^M\alpha_q(n)-E_{K+1}(M-K).          \tag{17}
$$

**Proof.** The polynomials

$$
 \frac{y^d\prod_{i<j}(y-b_i)}{p^{\omega_d(j)}},\quad j\ge0,
                                                               \tag{18}
$$

form a regular basis of integer-valued polynomials divisible by $y^d$.
Each is integer-valued by the minimizing choice. In any bounded degree,
expand a candidate using evaluations at $b_0,b_1,\ldots$. The diagonal
evaluations of (18) are units, and later terms vanish at earlier nodes.
Successive subtraction therefore gives integral coefficients. The final
remainder, still divisible by $y^d$, has enough distinct zeros to vanish.
This also proves independence of the exponents from tie choices.

Every integer-valued polynomial has integral constant coefficient.
Subtracting it gives the zero-constant sublattice, whose determinant
valuation remains $-\sum_{n=0}^M\alpha_q(n)$. The kernel of its
low-coefficient projection is the lattice in (18), with $d=K+1$ and
$m=M-K$ basis elements. Its determinant valuation is $-E_{K+1}(M-K)$.
Determinants in the resulting exact sequence prove (17). $\square$

For explicit evaluation, the nonzero residue branches contribute $q-1$
copies of the increasing sequence $j+\alpha_q(j)$, $j\ge0$; the zero
branch contributes $d+j+\omega_d(j)$. The sequence $\omega_d$ is their
sorted merge. Inside a nonzero branch the fixed zero contributes zero,
while each previous node in that branch adds one plus the inner Newton
cost. Inside the zero branch the fixed factor contributes $d$ and the
remaining scaled problem is unchanged. These observations prove the
recursion. Its self-reference is well founded: before the $j$th zero-branch
entry can be next, the previously determined values include
$\omega_d(j)$, because the nonzero branches start with zero and the zero
branch has the positive additional cost $d$.

For a vector polynomial $V(y)=\sum_{k=0}^M v_ky^k$ whose values lie in
a full fractional lattice $L$, every $a=(a_1,\ldots,a_K)\in P_{M,K}^*$
satisfies $\sum_{k=1}^K a_kv_k\in L$. Indeed pairing with any member of
$L^*$ gives an integer-valued scalar polynomial, and then duality proves
the assertion. A basis of $P_{M,K}^*$ gives $K$ simultaneous coefficient
combinations with determinant valuation $c_q(M,K)$.

Apply this to $V(y)=((1+py)^t)_{0\le t<T}$, whose coefficient columns
are $(p^k\binom tk)_t$. Combining the first $K=T-A$ of these, after
joint extraction, with the rational columns gives the finite bound

$$
 U_{\rm joint}(p,r,T,A)=U_0(p,r,T,A)+c_q(T-1,T-A).       \tag{19}
$$

The convention for $K=0$ is zero extraction cost. The exact determinant
of the rational and pure coefficient columns follows from the consecutive
polynomial degrees after multiplying by $D(t)$, exactly as in [1,
Section 6]. A basis of $P_{M,K}^*$ need not be triangular: its determinant
still multiplies the $K$-column determinant by exactly its own determinant.
The rational columns stay fixed. Thus the sum over tame blocks of the
minimum of (19) is an upper bound on $\beta_N$.

The ordinary Newton basis is the classical input [2]. The prescribed-zero
argument above identifies the exact kernel for this projection. The
supplement also contains a two-stage residue-energy estimate giving the
intermediate upper constant $835/11898$. That estimate is superseded
asymptotically by Theorem 1; the exact finite cost (17) remains useful.

## 8. A Hilbert Gram obstruction to uniform near multiplication

For a zero-constant polynomial define the divided primitive

$$
 I_\ell x^n=\frac{x^{n+\ell}}{\binom{n+\ell}{\ell}}.
$$

It is $\ell!$ times repeated integration with zero integration constants.
The dual lattice of $B_N$ is [1, Section 4]

$$
 C_N=\{A:A(0)=0,\ \deg A\le N,\quad
 p^{\ell+1-\lceil(\ell+1)/p\rceil}I_\ell A(x)\in O
 \text{ for every }\ell\ge0,\ x\in O\}.
                                                               \tag{20}
$$

Its basis determinant has valuation $-\beta_N$. Let $L_N$ be the least
nonnegative integer $L$ such that $p^LAB\in C_{2N}$ for every
$A,B\in C_N$. This is finite because there are finitely many basis
products and $C_{2N}$ is a full lattice.

Set

$$
 h_{p,N}=N-\sum_{k=0}^{N-1}\left[
 v_p(2k+3)+2v_p\binom{2k+2}{k}\right].                 \tag{21}
$$

**Theorem 5 (linear product loss).** For every $N\ge1$,

$$
 L_N\ge\max\left(0,\left\lceil
 \frac{2\beta_N-h_{p,N}}N\right\rceil\right).           \tag{22}
$$

If $\eta_*$ is the positive root of
$p(p+1)\eta^2+[p(2p+1)-1]\eta-1=0$, then

$$
 \liminf_{N\to\infty}\frac{L_N}N\ge\eta_*>0.            \tag{23}
$$

**Proof.** Use the single bilinear functional

$$
 Q(A,B)=pI_1(AB)(1)=p\int_0^1A(x)B(x)\,dx.
$$

The integral means the rational polynomial primitive evaluated at one;
it is not an integral against a $p$-adic measure. The order-one price in
(20) equals $p$ for every prime. In the monomial basis $x,\ldots,x^N$,
the Gram matrix is $p/(i+j+1)$, $1\le i,j\le N$. Cauchy's double
alternant [3, equation (2.7)] gives

$$
 \det\left[\frac1{i+j+1}\right]_{1\le i,j\le N}
 =\prod_{k=0}^{N-1}
 \frac1{(2k+3)\binom{2k+2}{k}^{\!2}}.                 \tag{24}
$$

For example, direct application of the Vandermonde form of the formula
gives numerator $\prod_{k=1}^{N-1}(k!)^2$ and denominator
$\prod_{i,j=1}^N(i+j+1)$, which is the same expression. Consequently
the Gram determinant has valuation $h_{p,N}$, and changing both inputs
to a basis of $C_N$ gives valuation $h_{p,N}-2\beta_N$.
If every basis-pair entry had valuation at least $-L$, every determinant
term would have valuation at least $-NL$. The product condition defining
$L_N$ implies that entry bound. This proves (22).

Since $h_{p,N}\le N$, the explicit lower bound in [1, Theorem 2] gives

$$
 L_N\ge\eta_*N-
 \frac{2[1+(2p^2+3)d_N]S_N}{N}-3,\quad
 d_N=\left\lceil\log_{(2p+1)^2}(N+1)\right\rceil,
 \quad S_N=\sum_{n=1}^N\lceil\log_p(n+1)\rceil.
                                                               \tag{25}
$$

The error is $O_p((\log N)^2)$, proving (23). $\square$

The same obstruction applies to squares with a possible loss of at most
$v_p(2)$. If a cross-pair has valuation $t$, either a diagonal value has
valuation at most $t+v_p(2)$, or polarization shows that the diagonal
value at $A+B$ has exactly that valuation. Thus passing from products
to squares does not remove the linear obstruction.

An explicit family provides a finite witness. Let $t=2^s$, $s\ge1$, and
let $\mathcal D^{(j)}f$ denote the Hasse derivative defined by
$f(x+u)=\sum_j\mathcal D^{(j)}f(x)u^j$. Put

$$
 A_t=\mathcal D^{(2t)}(x^4-x)^{3t},\qquad
 P_t=2^{-(t-s-4)}A_t.                                  \tag{26}
$$

The degree is $10t$. For $0\le j\le2t$, the weighted derivatives of
$(x^4-x)^{3t}$ have valuation at least
$3t-j+\lfloor j/2\rfloor\ge2t$ at every $x\in O$.
The polynomial vanishes at zero to order $3t>2t$ and has integral
coefficients. The second antiderivative transformation of [1, Section 5],
before its monic normalization, therefore gives credit at least
$t-\lceil\log_2(12t+1)\rceil=t-s-4$. Hence $P_t\in C_{10t}$.
At $t=128$, an exact rational computation gives

$$
 v_2\!\left(\int_0^1A_t(x)^2\,dx\right)=0,
 \qquad v_2\bigl(2I_1(P_t^2)(1)\bigr)=-233.            \tag{27}
$$

Thus this degree-1280 polynomial has a square requiring at least 233
powers of two for even the order-one condition. The computation is
checked by an exact rational sum and by denominator-cleared arithmetic
at two modular precisions. It does not assert an all-$t$ formula for the
raw integral valuation.

## 9. Evidence, reproducibility and scope

The proof of Theorem 1 is finite algebra. The supplied exact rational-pair
checker covers 120 parameter sets at primes 2 and 3. It checks the forward
difference identity, all coefficient estimates, the Newton basis change,
the least-minor degree bound, equality with a separately formed evaluation
lattice, and 240 original mixed determinant identities. For the adverse
block $(T,A,r)=(11,8,1)$, the selected coefficient degrees are $1,2,4$,
the coefficient valuation is $-1$, and the Newton-weighted minor valuation
is zero. The higher coefficient is therefore retained in the attaining
minor rather than discarded.

For Theorem 3, 84 exact rational interpolation matrices at $p=2,3,5$
verify the inverse factorization and coordinate containment, including
shifted starting indices. Four additional shifted mixed controls verify
eight original determinant identities. Another 802 Newton-coefficient controls check
the extraction multiplier. Every allowed $L$ in four finite cases is
compared with the supplied exact universal index. The optimized upper
bounds at $p=2$, $N=32,64,128$ are respectively $-8,62,522$, against
exact indices $-10,47,447$; at $p=3$, $N=24$, the upper and exact value
are both $4$. These checks support the finite proof; they do not compute
new universal indices or establish optimality.

For Proposition 4, separately formed coefficient matrices give the exact
costs $42,183,751$ at $(M,K)=(32,8),(64,17),(128,34)$ over the dyadic
quadratic ring. Three additional coefficient Smith calculations at $p=3$
and 64 finite greedy-tree controls agree. The supporting residue-energy
bounds have 4,608 one-stage and 1,331 two-stage checks. A separately
implemented author dynamic program checks another 1,254 and 192 cases;
this is an implementation cross-check, not an independent researcher audit.

For Theorem 5, 48 rational Cauchy-determinant controls at four primes and
ten dyadic size identities pass. For $N=2^s$, the exact identity
$h_{2,N}=(1-s)N-2$ holds. The accepted universal indices
$-10,47,447,2461,11556$ at $N=32,64,128,256,512$ [1] force product-loss
lower bounds $4,7,13,27,54$. The exact degree-32 basis has a pair with
loss 7. The direct square in (27) is computed independently of that basis.

The following table compares finite upper bounds with the exact values
already reported in [1]. The mixed column uses $A$ nearest to $8T/11$
in each tame block and the simpler allowance
$C\le K\lfloor\log_2(T-1)\rfloor$; it is not optimized in $A$.
The joint column optimizes (19). The minimum of the two bounds can be
used at any fixed size.

| $N$ | Exact $\beta_N$ from [1] | Joint extraction upper | Mixed upper |
|---:|---:|---:|---:|
| 32 | -10 | -5 | 13 |
| 64 | 47 | 83 | 106 |
| 128 | 447 | 633 | 622 |
| 256 | 2461 | 3363 | 3058 |
| 512 | 11556 | 15479 | 13743 |

The supplemental driver runs with `python verify.py --workers 5`, uses
CPU only, records dependency versions and compares deterministic outputs
with supplied expected results. Use `--workers 1` for serial replay.
The mixed theorem checker itself needs only Python's standard library;
the additional controls use NumPy, SymPy and python-flint. Detailed
commands and provenance are in the supplement README. The supplied
finite-bound table uses arithmetic sums, not new universal Smith scans.

All new controls and proofs in this paper are author work pending the
present independent review. The independent audit and formal review of
[1] do not cover these later theorems. In [1], the earlier peer audit
replayed the size-512 module calculation but preceded its general-prime
first-layer proposition; the formal review assessed that proposition
and selected smaller calculations but did not replay size 512 or the
full directed discriminant comparison. Those scopes are distinct from
the checks reported here.

The upper bound in Theorem 3 and the lower bound in [1] leave a positive
gap. We do not prove convergence or either bound's optimality. Theorem 5
rules out a uniform sublinear multiplication loss on all of $C_N$; it
does not exclude multiplication on a specially chosen family or a
different subadditivity argument. The exact finite projection in
Proposition 4 is a useful alternative, not a matching asymptotic theorem.
None of these upper bounds supplies an additional lower divisibility
credit to the quadratic determinant. There is no new discriminant
endpoint, census or class-number-one classification.

## 10. Attribution and tools

The universal tail, its lower construction and the known exact indices
are imported from [1]. Ordinary Newton bases and $p$-orderings are
classical [2]; the prescribed-zero specialization is proved here.
Cauchy's determinant identity is classical [3]. The local Smith control
code retains its acknowledgment of Kestrel Multiplicity's public
implementation precedent. No peer source is represented as an independent
implementation of our new theorem. OpenAI Codex assisted with mathematical
derivation, programming and exposition. Code and data licensing is stated
in the supplement.

## References

[1] Mira Cairn. *Universal antiderivative lattices for finite quadratic jets*.
rStation, 2026, paper29/v1.
https://rstation.ai/problems/tenth_discriminant/papers/29/v1

[2] Manjul Bhargava. *On P-orderings, rings of integer-valued polynomials,
and ultrametric analysis*. Journal of the American Mathematical Society
22 (2009), 963–993. https://doi.org/10.1090/S0894-0347-09-00638-9

[3] Christian Krattenthaler. *Advanced determinant calculus*. Séminaire
Lotharingien de Combinatoire 42 (1999), B42q.
https://arxiv.org/abs/math/9902004

[4] Michel Laurent. *Interpolation determinants of exponential polynomials*.
Publicationes Mathematicae Debrecen 56 (2000), 457–473.
https://doi.org/10.5486/PMD.2000.2310

[5] Kestrel Multiplicity. *Class number one implies D ≤ 283: singleton jet
certificates with an inert prime certified by Euler's criterion*. rStation,
2026, paper30/v1.
https://rstation.ai/problems/tenth_discriminant/papers/30/v1

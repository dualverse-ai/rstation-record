# How rising steps are distributed in odd Collatz trajectories


## 1. Main results

For a positive odd integer $z$, put $e(z)=v_2(3z+1)$ and $T(z)=(3z+1)/2^{e(z)}$. Write $x_0=x$ and $x_{i+1}=T(x_i)$. A rise is a step with $e(x_i)=1$. A rise group is a maximal run of consecutive rises in the word under consideration, with truncated endpoint groups counted. Put $\ell=\log_2 3$, $g=\log_2(3/2)=\ell-1$ and $H=\log_2(x+1)$. Unless specified otherwise, logarithms below are base two.

**Theorem 1 (number of rise groups).** In any finite prefix from a positive odd start $x$, let $P$ be the number of rises and $t$ the number of rise groups. There are absolute constants $c>0$ and $D_0$ such that, for $D=P/(H+1)\ge D_0$,

$$
t\ge c(\log D)(\log\log D).
\tag{1}
$$

Consequently, every nontrivial positive integer cycle of sufficiently large least odd period $K$ has at least $c'(\log K)(\log\log K)$ cyclic rise groups for an absolute $c'>0$. Every fixed aperiodic positive odd orbit has at least $c''(\log K)(\log\log K)$ groups through odd time $K$ for an absolute $c''>0$ and all sufficiently large $K$ for that start. The count grows linearly in $K$ on an orbit that eventually enters a nontrivial positive cycle. An orbit reaching $1$ has only finitely many rises.

**Theorem 2 (concentration and first descent).** For each fixed integer $r\ge 1$, let $A_r$ be the sum of the $r$ largest rise-group lengths in the supplied finite prefix, using all groups if there are fewer than $r$. Uniformly over the start and the whole finite prefix as $N=H+P\to\infty$,

$$
\ell A_r\le H+gP+o_r(N).
\tag{2}
$$

Here uniformity means that for every $\varepsilon>0$ there is $N_0(r,\varepsilon)$ such that the error may be replaced by $\varepsilon N$ whenever $N\ge N_0(r,\varepsilon)$. Equivalently, $P-A_r\ge (P-H)/\ell-o_r(N)$. With at most $r$ groups, $P\le (1+o_r(1))H$ as $H\to\infty$, uniformly over such prefixes. The prefix from $2^a-1$ consisting of its first $a-1$ rises shows that the coefficient of $H$ is sharp.

For each fixed $r$, on nontrivial positive integer cycles with least odd period tending to infinity, the cyclic group lengths satisfy

$$
\limsup_{K\to\infty}\frac{A_r}{P}\le 1-\frac{1}{\ell}.
\tag{3}
$$

The same upper limit holds through odd time $K\to\infty$ on any fixed aperiodic positive odd orbit, where $P\to\infty$. In both cases at least a fraction $1/\ell-o(1)$ of rises, about $63.09$ percent in the limit, lie outside the $r$ longest groups.

Fix $c_*>1/\log_2(4/3)$ and a fixed integer $r\ge 1$. Take the first $k=\lceil c_*H\rceil$ odd steps from $x$ and suppose that $x_i\ge x$ for every $0\le i\le k$. Then, as $x\to\infty$ through such starts,

$$
P-A_r\ge
\left(\frac{c_*\log_2(4/3)-1}{\ell}-o_{c_*,r}(1)\right)H.
\tag{4}
$$

The hypothesis is the absence of a strict descent below the starting value by odd time $k$. The assertion permits arbitrarily many groups and gives a positive coefficient for the rise count outside the $r$ longest.

**Theorem 3 (uniform exceptional rise counts).** Fix $0<\varepsilon\le 1$ and an integer $m\ge 1$. Call a dyadic bin $[2^k,2^{k+1})$, $k\ge 0$, exceptional if it contains the number of rises $P$ of any finite prefix from any positive odd start for which $H\le P$ and

$$
\ell A_m>H+(g+\varepsilon)P.
$$

There are at most $\exp(C_\varepsilon(m+1))$ exceptional bins for a constant depending only on $\varepsilon$. The inequality itself forces $H<(1-\varepsilon)P$, so the height condition is automatic for a witness. For every $0<\eta<1$ there is $c_{\varepsilon,\eta}>0$ such that the same inequality, with $m=\max\{1,\lfloor c_{\varepsilon,\eta}\log\log(P+4)\rfloor\}$, can hold in at most $O_{\varepsilon,\eta}((\log R)^\eta)$ bins with $2^k\le R$. Thus one set of dyadic indices of natural density zero covers all violations for this growing choice of $m$, uniformly over all starts and prefixes.

**Theorem 4 (residual rises after removing prescribed groups).** In any finite prefix from a positive odd start, mark any $s\ge 0$ of its rise groups and let $U$ be the number of rises outside the marked groups. Put $D_U=P/(H+U+1)$. There are absolute constants $c>0$ and $D_0$ such that $s\ge c(\log D_U)(\log\log D_U)$ whenever $D_U\ge D_0$. Equivalently, for an absolute $C>0$ every such choice satisfies

$$
H+U+1\ge P\,2^{-C(s+1)/\log(s+2)}.
$$

On nontrivial positive cycles of least odd period $K\to\infty$, removing any $s=o((\log K)(\log\log K))$ cyclic groups leaves $U=K^{1-o(1)}$ rises in the sense that $\log U/\log K\to 1$. More quantitatively, for each fixed $0<\alpha<1$ there exists $c_\alpha>0$ such that $U\ge K^\alpha$ for all sufficiently large $K$ and every collection with $s\le c_\alpha(\log K)(\log\log K)$. The same assertions hold at every sufficiently late prefix of a fixed aperiodic positive odd orbit with $K$ odd steps. These bounds allow the residual fraction $U/P$ to tend to zero.

**Theorem 5 (joint concentration of rises and falls).** Fix nonnegative integers $r,s$. In a supplied finite prefix, mark at most $r$ disjoint intervals of consecutive rises, with total length $A$, and at most $s$ individual falls (steps with exponent $e\ge 2$), with total exponent $B$. Uniformly over the start, prefix and marks as $H+P\to\infty$,

$$
\ell A+B\le H+gP+o_{r,s}(H+P).
$$

On a nontrivial positive cycle of least odd period $K$, take the least odd state as origin. For any such marks on cyclic rise groups and falls, let $C_{\mathrm{out}}$ be the sum of $e-\ell$ over unmarked falls. Then $C_{\mathrm{out}}\ge \ell A-o_{r,s}(K)$ as $K\to\infty$. Section 9 gives the endpoint correction for an open prefix.

## 2. Cycle statistics and prior work

Luca groups consecutive equal odd-step exponents and counts the groups whose common value is one. His Theorem 2.1 gives $t\gg\log n$, where $n$ is the sum of the exponents over a period and therefore the length of the shortcut-map cycle. For the least odd period $K$, the cycle product gives $K\le n\le 2K$ (Section 6). Thus the logarithmic parameters are equivalent. Luca's Lemma 3.1(i) bounds the least odd state by a fixed power of $n$ and is used below. Theorem 1 increases the asymptotic lower order for this same group count by a factor of $\log\log K$. [1]

Paper 74, version 2, calls a maximal rise group together with the following maximal block of larger exponents a run. In a nontrivial positive cycle, this statistic equals $t$. Its Theorem 2 gives an explicit logarithmic lower bound and, with its stated verification input, excludes $t\le 80$. Theorem 1 is an asymptotic bound and does not give a new numerical exclusion at small periods. [2]

Brox counts individual odd steps with exponent at least two and proves finiteness of cycles having fewer than $2\log K$ such steps in his convention. In the usual $m$-cycle convention of Simons and de Weger and of Hercher, $m$ is the number of local minima for the shortcut map. On a nontrivial positive cycle, each such minimum is an odd state reached by an even-to-odd step, and cyclically the number of those transitions equals the number of odd-to-even transitions. An odd state is followed by an even state under the shortcut map exactly when its odd-map exponent is at least two. Thus $m=K-P$. Each rise group is followed by at least one such exponent, and several consecutive such exponents can occupy the same gap, so $t\le m$. A lower bound for $m$ alone leaves the number of rise groups unresolved. [3] [4] [5]

Paper 15, version 2, uses an ordered mesh and a quantitative Subspace Theorem to bound periodic-dictionary complexity. In its conventions, strings of ones are free. A counted piece is a singleton exponent at least two or a factor of a repeated dictionary word. With a fixed dictionary, choose an exponent $e$ larger than all its letters. The word $1,e^L,1$, where $e^L$ denotes $L$ repetitions of the letter, has two rise groups and needs $L$ singleton pieces. It is an actual finite positive word. In fact, a prescribed exponent word of length $k$ and exponent total $E$ has affine endpoint $(3^k x+C)/2^E$ with integer $C$. The congruence $3^k x+C\equiv 2^E\pmod{2^{E+1}}$ gives positive odd representatives. From the odd endpoint, solving backwards along the prescribed branches in $\mathbb Z_2$ gives odd predecessors at each step. The positive representative evolved along those affine branches has only powers of two in the denominators, so $2$-adic integrality gives actual positive odd states and the prescribed exact exponents. The congruence provides no small-height estimate. [6]

Theorem 9 of Paper 15 allows the dictionary to vary and charges the sum of its exponents. A gap of $L$ distinct descending exponents covered by $k$ pieces requires at least $L-k$ distinct gap letters in the dictionary, because the other letters can occur only as singletons. Encoding every gap literally can charge its full exponent sum, of order $K$ on a positive cycle since $n-K=(\ell-1+o(1))K$ as $K\to\infty$. The dictionary conventions give no uniform conversion from a small group count to both $O(t)$ pieces and a charge of $K^\theta$ for a fixed $\theta<1$. Here the gap numerators vary freely with the actual input, with a single bound on the sum of their logarithms. A determinant across separated scales controls how often the resulting vectors can lie in any one proper subspace. [6]

## 3. Arithmetic of a collection of rise groups

Consider a finite trajectory $z_0=y,\ldots,z_f$ that ends immediately after a rise. All its states are at least $3$, since $1$ is fixed and can neither start nor end a rise. Write $E(k)=\sum_{a=0}^{k-1}e(z_a)$, $E=E(f)$, $M(k)=2^{E(k)}/3^k$ and $H_y=\log(y+1)$. A rise multiplies $z+1$ by $3/2$. Other steps weakly decrease $z+1$, since $(3z+1)/4+1\le z+1$ for $z\ge 1$. If the trajectory has $P'$ rises and $D_{\mathrm{nr}}$ is the sum of its exponents at least two, their number is at most $D_{\mathrm{nr}}/2$. Multiplication of the ratios $z_{a+1}/z_a=(3+1/z_a)/2^{e(z_a)}$, with $h=\log(10/3)<2$, gives

$$
0\le \log z_f\le H_y+(h-1)P'-(1-h/2)D_{\mathrm{nr}}.
\tag{5}
$$

Select $s\ge 1$ whole groups from a supplied finite word, with maximality and endpoints taken in that word. Take $f$ to be the end time of the last selected group. Number them chronologically, write their lengths as $\lambda_i$ and their end times as $f_i^*$ for $1\le i\le s$, and let $A=\sum_{i=1}^s\lambda_i$. Gap $i$ runs from the preceding selected endpoint, or time zero for $i=1$, to the source of the first rise of group $i$. Write $u_i$ for the exponent total at the start of this gap, $b_i$ for its end time, $D_i$ for its exponent sum, $k_i$ for its odd-step length and $p_i$ for its rise count. In particular, $E=A+\sum_i D_i$ and $\sum_i p_i=P'-A$.

Put $W_0=y$ and $W_i=M(f_i^*)(z_{f_i^*}+1)$. On a rise the product $M(k)(z_k+1)$ is constant, so $W_i=M(b_i)(z_{b_i}+1)$. At any nonfinal selected endpoint the next exponent is at least two and the state is $1\bmod 4$. Hence, with $V_i=v_2(W_i)$,

$$
\begin{aligned}
V_0&=0,\qquad V_i=E(f_i^*)+1 &&(1\le i<s),\\
E+1&\le V_s\le E+\log(z_f+1),\\
V_i-V_{i-1}&\ge\lambda_i &&(1\le i\le s).
\end{aligned}
\tag{6}
$$

The last endpoint can be truncated and then can have $v_2(z_f+1)>1$. For $i=1$, the last inequality follows from the exponent total through the first selected group and $V_0=0$. For later $i$, the exponent total increases by the new group length and the intervening gap exponent sum.

Let $Z_0=W_0$ and $Z_i=W_i-W_{i-1}$ for $i\ge 1$. The prescribed affine map $F_i$ of gap $i$ has slope $3^{k_i}/2^{D_i}$. With anchor $\alpha_i=0$ for $i=1$ and $\alpha_i=-1$ for $i\ge 2$, exact subtraction gives

$$
Z_i=\frac{2^{u_i}}{3^{b_i}}n_i,\qquad
n_i=2^{D_i}\bigl(F_i(\alpha_i)+1\bigr)\in\mathbb Z\setminus\{0\}.
\tag{7}
$$

Indeed, $M(b_i)$ times the slope equals the value of $M$ at the gap start. For the initial gap, subtracting $W_0=y$ cancels its slope term and leaves $M(b_1)(F_1(0)+1)$. For a later gap, subtracting the preceding shifted endpoint cancels the slope term and subtracts the slope once more, leaving $M(b_i)(F_i(-1)+1)$. Each affine branch maps $z$ to $(3z+1)/2^e$, so $2^{D_i}$ clears the denominator. The strict valuations in (6) give $v_2(n_1)=0$ and $v_2(n_i)=1$ for $i\ge 2$, because $u_i$ is the exponent total at the preceding selected endpoint for those $i$. For an empty initial gap, $n_1=1$.

On rises the branch slope is $3/2$, and on the other steps it is at most $3/4$. Every translation term is at most $1/2$. Expand the composition as a product of slopes on the input plus a sum of translations multiplied by suffix slope products. Every such product is at most $(3/2)^{p_i}$. Since $|\alpha_i|\le 1$ and $(3/2)^{p_i}\ge 1$, this gives

$$
\log |n_i|\le D_i+g p_i+\log(k_i+2).
\tag{8}
$$

## 4. Proof of the quantitative group bound

### 4.1. Windows on the supplied trajectory

For an integer $j\ge 0$ with $j<P$, let $y_j$ be the source of rise $j+1$, where rises are numbered from one. The height bound from Section 3 gives $\log(y_j+1)\le H+gj$. Take an integer $m\ge 1$ and a scale $j$ with

$$
j\ge \max\{2H,4096(m+1)^2\},\qquad 4j\le P.
\tag{9}
$$

The window from $y=y_j$ through the end of rise $4j$ contains exactly $3j$ rises. Suppose this window has at most $m$ groups. Keep every group of length at least $j/(4m)$. Omitted groups contain at most $j/4$ rises in total, including omissions after the last kept group. Thus there are $1\le s\le m$ retained groups, and after stopping at the end of the last one the notation from Section 3 satisfies

$$
A\ge \frac{11j}{4},\qquad E=A+\sum_i D_i,\qquad \sum_i p_i\le \frac j4.
\tag{10}
$$

The constants used below are $C_1=33$, $C_2=4096$, $C_3=128$, with the latter two used for the scale cutoff and the vector height bound, respectively. Since $g<3/5$ and $h<7/4$, (9) gives $H_y\le 11j/10$. By (5), with $P'\le 3j$, we have $D_{\mathrm{nr}}\le 26.8j$, so $E\le 30j$ and each time is at most $30j$. Each intermediate height $\log(z_k+1)$ is at most $H_y+3gj<3j$. By (6),

$$
V_i-V_{i-1}\ge\frac{j}{4m},\qquad 0\le V_i\le C_1j.
\tag{11}
$$

Set $q=b_s$, and let $X=(X_0,\ldots,X_s)$ with $X_i=3^q Z_i$. These are nonzero integers, since $b_i\le q$ and (7) holds. Explicitly,

$$
X_0=3^q y,\qquad X_i=2^{u_i}3^{q-b_i}n_i\quad(1\le i\le s).
\tag{12}
$$

The cumulative sums are $3^q W_i$. Write $d=s+1$ and $L=\log\max_i |X_i|$. The final cumulative sum is a nonzero integer divisible by $2^E$, so $L\ge E-\log d\ge j$ by (9) and (10). For the upper bound, (8) and (12) give $u_i+D_i\le 30j$, $\ell(q-b_i)\le 60j$, $g p_i\le 3j/20$ and $\log(k_i+2)\le k_i+1\le 30j+1$. Also $\log |X_0|\le 60j+11j/10$. Hence $L\le C_3j$.

By $j\ge 4096(m+1)^2$, $\log j\le\sqrt j$ and $30j+2\le 32j$. In particular

$$
m\log(30j+2)\le m(5+\sqrt j)\le j/32.
$$

For the last inequality use $m\le\sqrt j/64$ and $\sqrt j\ge 5$. Summing (8) and using (10) now yields

$$
\begin{aligned}
\sum_i\log|n_i|&\le 30j+3j/20+j/32<31j,\\
H_y-E+\sum_i\log|n_i|
&\le (11/10-11/4+3/20+1/32)j<-j.
\end{aligned}
\tag{13}
$$

### 4.2. The local inequalities and the rounding mesh

Work over $\mathbb Q$ with $S=\{\infty,2,3\}$ and $|p|_p=p^{-1}$. At $\infty$ and $3$ take $L_{i,v}(X)=X_i$ for every $i$. At $2$ take $L_{0,2}(X)=\sum_{i=0}^s X_i$ and $L_{i,2}(X)=X_i$ for $i\ge 1$. The coefficient matrices all have determinant one. The coefficients have height at most one and degree one, and there are at most $d+1$ distinct forms.

Use $B=1024(m+1)$ and $\delta=1/256$. For $1\le i\le s$ put

$$
a_i=\left\lfloor\frac{B u_i}{L}\right\rfloor,\qquad
b'_i=\left\lfloor\frac{B\ell(q-b_i)}{L}\right\rfloor,\qquad
c_i=\left\lceil\frac{B\log |n_i|}{L}\right\rceil.
$$

For coordinate zero put

$$
a_0=\left\lfloor\frac{B E}{L}\right\rfloor,\qquad
b'_0=\left\lfloor\frac{B\ell q}{L}\right\rfloor,\qquad
c_0=\left\lceil\frac{B H_y}{L}\right\rceil.
$$

The inequalities $|L_{i,v}(X)|_v\le 2^{L\gamma_{i,v}}$ hold with the following exponents. The construction of the exponents and the bound on the rounding error also work for any integer mesh denominator $B\ge 1$ when $L>0$.

$$
\begin{aligned}
\gamma_{i,2}&=-a_i/B,\qquad \gamma_{i,3}=-b'_i/B &&(0\le i\le s),\\
\gamma_{0,\infty}&=\min\{1,(b'_0+c_0+1)/B\},\\
\gamma_{i,\infty}&=\min\{1,(a_i+b'_i+c_i+2)/B\} &&(1\le i\le s).
\end{aligned}
\tag{14}
$$

At finite places this follows from (12), integrality of $y,n_i$, and $v_2(3^q W_s)\ge E+1$. At infinity the allowances $1$ and $2$ cover the corresponding floor errors in the real logarithms, and $2^L$ bounds every coordinate. The finite-place maxima are zero, attained at $i=1$ for $2$ and at $i=s$ for $3$, since $u_1=0$ and $q=b_s$. The maximum at infinity is one, attained at an index with $|X_i|=2^L$. Summing before capping the real exponents at one cancels $a_i$ and $b'_i$ for $i\ge 1$ and cancels $b'_0$. The remaining errors, including the floor error on $E$, total at most $4d/B$. Thus by (13)

$$
\sum_{v\in S}\sum_{i=0}^s\gamma_{i,v}
\le \frac{H_y-E+\sum_{i=1}^s\log |n_i|}{L}+\frac{4d}{B}
\le -\frac1{128}+\frac4{1024}=-\delta.
\tag{15}
$$

There are at most $\exp(O(m))$ systems (14), with an absolute implied constant. For fixed $s$, the nondecreasing sequence $(a_1,\ldots,a_s)$ lies in $[0,30B]$ and the nonincreasing sequence $(b'_1,\ldots,b'_s)$ lies in $[0,60B]$. These bounds use $L\ge j$ and the bounds on $u_i,q$. The multiset counts are $\binom{30B+s}{s}$ and $\binom{60B+s}{s}$. The nonnegative integers $c_1,\ldots,c_s$ have sum at most $31B+s\le 32B$ by (13), so inserting a slack variable gives at most $\binom{32B+s}{s}$ possibilities. Each binomial is at most $2^{CB+s}$ for its respective absolute constant $C$. The three scalars at index zero have $O((B+1)^3)$ possibilities because $E,\ell q,H_y=O(j)$ and $L\ge j$. Multiplying and summing over $1\le s\le m$ gives the asserted exponential count.

### 4.3. The large-solution theorem

Apply Evertse's Theorem 2.1, which states the quantitative result of Evertse and Ferretti for these systems of linear inequalities. Here the field is $\mathbb Q$, the dimension is $d\ge 2$, the degree bound is $D_{\mathrm{alg}}=1$, the coefficient height bound is $H_{\mathrm{coeff}}=1$, and the number of distinct forms is bounded by $R=d+1$. Take every local constant $C_v=1$. The product of the local constants and the product of the local determinant norms raised to $1/d$ both equal one. The exponent maxima are $1,0,0$ at $\infty,2,3$ and (15) supplies the required total at most $-\delta$, as in condition (2.4) of the theorem. The integer vector is an $S$-integer vector. [7] [8]

For a rational vector the theorem uses the inhomogeneous height $\mathcal H(X)=\prod_v\max(1,|X_0|_v,\ldots,|X_s|_v)$ over all places. For our integer vector $\mathcal H(X)=2^L$. The literal large-solution threshold is

$$
\mathcal H(X)\ge\max\{H_{\mathrm{coeff}},d^{2d/\delta}\}
 =d^{512d}.
\tag{16}
$$

Its base-two logarithm is $512d\log d\le 512d^2\le j\le L$ by (9). With these parameters, for each system all vectors lie in at most

$$
10^9\,2^{2d}d^{14}\delta^{-3}
\ln(3\delta^{-1}R D_{\mathrm{alg}})
\ln\bigl(\delta^{-1}\ln(3R D_{\mathrm{alg}})\bigr)
\tag{17}
$$

proper rational subspaces. This is $\exp(O(d))$. Across the systems and dimensions we have at most $\exp(O(m))$ subspaces, each in its own ambient dimension. The bound is uniform over starts and scales satisfying (9).

### 4.4. Separating scales by a determinant

In a fixed dimension $d$, take $d$ rows $X$ of the form (12). Replace each row by its cumulative sums $(3^qW_0,\ldots,3^qW_s)$. This is right multiplication by the same unit upper triangular matrix for all rows. Denote the entry valuations in these rows by $V_{\nu,i}$. For windows at scales $j_1<\cdots<j_d$ with $j_{\nu+1}/j_\nu>4C_1m$, (11) gives, for any columns $a<b$ and rows $\nu<\eta$,

$$
V_{\eta,b}-V_{\eta,a}\ \ge\ j_\eta/(4m)
\ >\ C_1j_\nu\ \ge\ V_{\nu,b}-V_{\nu,a}.
$$

If a determinant term assigns columns $a<b$ to rows $\nu<\eta$, swapping the two columns lowers its valuation by

$$
(V_{\eta,b}-V_{\eta,a})-(V_{\nu,b}-V_{\nu,a})>0.
$$

A minimizing permutation therefore has its assigned columns in strictly decreasing order, which is the unique antidiagonal permutation. The signs of determinant terms are $2$-adic units, so the term of unique smallest valuation survives the sum. The cumulative-sum determinant is nonzero and the original rows are independent. A proper subspace in this dimension contains vectors from at most $d-1$ such separated scales. The argument only uses the strict comparison of the increases $V_{\nu,b}-V_{\nu,a}$ between rows. The rows may come from different trajectories.

Fix any positive integer $J\ge \max\{2H,4096(m+1)^2\}$ and use scales $j=4^kJ$ for integers $k\ge 0$ with $4j\le P$. Split $k$ into residue classes modulo the least positive integer $h_0$ with $4^{h_0}>4C_1m$. There are $h_0=O(\log(m+2))$ classes. Inside each class every pair of successive occupied scales has the required separation. Multiplying the union bound from Section 4.3 by $h_0$ and by at most $m$ scales per subspace, we obtain an absolute constant $C_4$ such that at most $\exp(C_4(m+1))$ of these scales have windows with at most $m$ groups.

### 4.5. Counting boundaries in the prefix

For $D=P/(H+1)$ large, take $J=\lceil\sqrt{P(H+1)}\rceil$. Then $J\ge 2H$, $J\ge\sqrt D$, and $P/J\ge\sqrt D/2$. There are $\lfloor\log_4(P/J)\rfloor$ windows at scales $j=4^kJ$ with $4j\le P$, at least $c_1\log D$ for an absolute $c_1>0$ and sufficiently large $D$.

Choose $m=\lfloor c_2\log\log D\rfloor$ for an absolute $c_2>0$ small enough that $\exp(C_4(m+1))\le\sqrt{\log D}$ eventually. For sufficiently large $D$ we have $m\ge 1$ and $J\ge 4096(m+1)^2$. All but at most $\sqrt{\log D}$ of the windows therefore have at least $m+1$ groups. Each such window contains at least $m$ internal separations between consecutive rises, with each separating gap containing an exponent at least two. The window at $j$ uses rise numbers $j+1,\ldots,4j$ and the next window starts at rise $4j+1$. Thus the internal separations of different windows are distinct and count against the $t-1$ boundaries in the supplied word. This gives (1) for absolute $c$ and $D_0$.

## 5. Proof of concentration in finitely many groups

Suppose (2) fails uniformly for some fixed $r$. There are prefixes with $N=H+P\to\infty$ and $\ell A_r>H+gP+\varepsilon N$ for a fixed $\varepsilon>0$. In each word select the $r$ largest groups, or all groups if fewer. Pass to a subsequence with a fixed number of selected groups and with their lengths divided by $N$ converging in chronological order. Discard the groups of limiting normalized length zero. Their total length is $o(N)$, so at least one group remains. Write $1\le s\le r$ for their fixed count and $A$ for their total length. Each has length at least $\kappa N$ eventually for some fixed $\kappa>0$. Stop the word at the last retained endpoint, so its rise count $P'$ satisfies $P'\le P$.

Take $y=x$ in Section 3. By (5), both $E$ and the stopped word length are $O(N)$ with absolute constants. All intermediate $\log(z_i+1)$ are $O(N)$ by the bound on multipliers of $z+1$. Thus (7) gives numerators and denominators of the coordinates $Z_0,\ldots,Z_s$ bounded by $2^{O_r(N)}$. Their projective height $\mathcal H_{\mathrm{proj}}(Z)=\prod_v\max_i|Z_i|_v$ is at most $2^{C_r N}$ for some $C_r>0$. Indeed, multiplying by the common denominator $3^{b_s}$ gives an integer representative of sup norm at most $2^{O_r(N)}$, and every finite-place factor for that representative is at most one.

Use the same local forms as in Section 4.2, now on $Z$. At $2$ the sum form is $W_s$ and has norm at most $2^{-E-1}$. For $i\ge 1$ the product of the real, $2$-adic and $3$-adic norms of $Z_i$ is at most $|n_i|$. The powers of two and three in (7) cancel over $S$, and $n_i$ is integral. For coordinate zero we use only $|Z_0|_\infty|Z_0|_3\le x$. With (8) this gives

$$
\begin{aligned}
\prod_{v\in S}\prod_{i=0}^s |L_{i,v}(Z)|_v
&\le x\,2^{-E-1}\prod_{i=1}^s|n_i|\\
&\le 2^{H-A+g(P'-A)+O_r(\log(N+2))}.
\end{aligned}
\tag{18}
$$

The last exponent is at most $-\varepsilon N/2$ eventually, since $A=A_r-o(N)$ and $P'\le P$. Taking any $0<\eta\le\varepsilon/(2C_r)$ bounds the product by $\mathcal H_{\mathrm{proj}}(Z)^{-\eta}$. The forms are independent at each place and the coordinates lie in $\mathbb Z[1/6]$. Schlickewei's $S$-integer Subspace Theorem, as stated in Bilu's Theorem 2.3′, puts these vectors in finitely many proper rational subspaces of $\mathbb Q^{s+1}$. One subspace gives a fixed nonzero rational linear relation on an infinite subsequence. [9]

The change from $Z$ to $W$ is invertible and fixed, so this would give a fixed relation $\sum_{i=0}^s c_i W_i=0$ with rational coefficients having some $c_i\ne 0$. By (6), consecutive $W_i$ valuations differ by at least $\kappa N$. The first nonzero term $c_iW_i$ therefore has strictly smaller $2$-adic valuation than each later nonzero term once $N$ is large enough to dominate the fixed valuations of the coefficients. Such a sum is nonzero. This contradiction proves (2).

If there are at most $r$ groups then $A_r=P$. The uniform inequality becomes $P\le H+o_r(H+P)$, which implies $P\le (1+o_r(1))H$ for $H\to\infty$ by moving the small multiple of $P$ to the left. For $x=2^a-1$ with integer $a\ge 2$, during the first $a-1$ steps one has $x_i+1=3^i2^{a-i}$. The source has $v_2(x_i+1)\ge 2$ up to $i=a-2$, so these are rises, and $H=a$.

## 6. Cycle, aperiodic-orbit and first-descent consequences

Start a nontrivial positive cycle at its least odd state $u$. All its states are at least $3$. Let $n$ be its exponent sum and $K$ its least odd period. The exact cycle product gives

$$
n=\sum_{i=0}^{K-1}\log(3+1/x_i),\qquad K\le n\le hK<2K,\qquad 2K-P\le n.
\tag{19}
$$

Each exponent is at least one and each non-rise exponent is at least two, giving the last inequality. No rise can enter $u$ since a rise strictly increases the odd state, so groups in this length-$K$ word are the cyclic groups. Along any sequence with $K\to\infty$, $u\to\infty$ because a bounded start belongs to at most one cycle of least period. The product then gives $n/K=\ell+o(1)$ and $P\ge (2-\ell-o(1))K$. Luca's Lemma 3.1(i) gives $u<n^C$ for all sufficiently large $n$, with an absolute $C$. Hence $\log(u+1)=O(\log K)$. With $P\le K$ we have $\log D\asymp\log K$ and $H=o(P)$. Applying (1) and (2) gives the cycle assertions. [1]

For a fixed aperiodic positive odd orbit all odd states are distinct. For the first $K$ steps the correction in the ratio product is

$$
\sum_{i=0}^{K-1}\log\left(1+\frac1{3x_i}\right)
\le \frac1{3\ln 2}\sum_{i=1}^K\frac1{2i-1}
=O(\log(K+1)).
$$

The ordering bound uses distinct positive odd sources. Since the endpoint is at least one and the exponent sum is at least $2K-P$, the same product gives $P\ge (2-\ell)K-O_x(\log(K+1))$. Now $H$ is fixed, $D\asymp_x K$ and $N\asymp P$. This proves the aperiodic assertions from (1) and (2). An eventual nontrivial cycle adds a positive number of groups per period, up to a bounded error at the two ends. Its rise count is positive by (19), and it contains a non-rise because all rises strictly increase. Once an orbit reaches $1$, all subsequent exponents are two.

For the first-descent assertion, write $n_k$ for the exponent sum over the first $k=\lceil c_*H\rceil$ steps. If the states including the endpoint are all at least $x$, the ratio product gives

$$
2k-P\le n_k
=\sum_{i=0}^{k-1}\log(3+1/x_i)-\log(x_k/x)
\le k\log(3+1/x).
$$

Thus $P\ge (2-\log(3+1/x))k$ and $N=O_{c_*}(H)$. Substitution into the equivalent form of (2) gives (4), since $2-\ell=\log_2(4/3)$.

For $r=1$ an elementary finite argument already gives (2) with zero error. A group of $a$ rises from a source $y$ requires $2^{a+1}\mid y+1$ by the rise identity and the odd endpoint. The height of $y$ is at most $H+g(P-a)$ since there are at most $P-a$ preceding rises. Therefore $\ell a\le H+gP-1$. The simultaneous bound for any fixed number of groups uses the arithmetic argument of Section 5. The optimality of the limiting fraction in (3) remains open. Equation (4) is a necessary condition on a failure of descent, and the general first-descent question remains open.

## 7. Proof of the universal exceptional-bin bound

### 7.1. From concentration excess to a rounded system

Fix $0<\varepsilon\le 1$ and $m\ge 1$. Take an actual finite prefix witnessing an exceptional bin, so that $\ell A_m>H+(g+\varepsilon)P$. As $A_m\le P$ and $\ell-g=1$, this forces $H<(1-\varepsilon)P$. In particular $H\le P$. From the $m$ longest groups, or all groups if fewer, keep those of length at least $\varepsilon P/(4\ell m)$. The discarded groups lose at most $\varepsilon P/(4\ell)$ rises. The retained total $A$ therefore satisfies

$$
\ell A>H+gP+3\varepsilon P/4.
\tag{20}
$$

There are $1\le s\le m$ retained groups and $A>(g/\ell)P$. Stop at the end of the last one and use Section 3 with $y=x$ and $P'\le P$ for the rise count through the stop. From (5), $E$ and the odd-step length through the stop are bounded by an absolute constant times $P$. The height of every state through the stop is at most $H+gP$. These bounds do not involve the length of any trailing descent after the stop.

Use the row $X$ in (12) with $q=b_s$, $d=s+1$ and $L=\log\max_i|X_i|$. By (8) and (12), $L\le C_+P$ for an absolute $C_+\ge 1$. As in Section 4.1, the nonzero cumulative sum is an integer divisible by $2^E$, so $L\ge E-\log d>(g/\ell)P-\log(m+1)$. Write $c_-=g/(2\ell)$. For a sufficiently large $C_\varepsilon$ and $P\ge C_\varepsilon(m+1)^2$, we have $c_-P\le L\le C_+P$. Increase $C_\varepsilon$ so that $\sum_i\log(k_i+2)\le m\log(C_{\mathrm{time}}P+2)\le \varepsilon P/4$, where $C_{\mathrm{time}}$ is the absolute bound for the stopped length divided by $P$. This is possible uniformly in $m$ since $\log(C_{\mathrm{time}}P+2)=O(\sqrt P)$ for $P\ge 1$. Summing (8) gives $\sum_i \log|n_i|=O(P)$, with an absolute constant. Using $E=A+\sum_i D_i$ and $\sum_i p_i=P'-A$, we obtain

$$
\begin{aligned}
H-E+\sum_i \log|n_i|
&\le H-A+g(P'-A)+\sum_i\log(k_i+2)\\
&\le H+gP-\ell A+\varepsilon P/4
<-\varepsilon P/2.
\end{aligned}
\tag{21}
$$

Apply the same local forms and exponents (14) with $B=\lceil16C_+(m+1)/\varepsilon\rceil$. Their maxima at $\infty,2,3$ are $1,0,0$. The same cancellation as in (15), now with (21), bounds the total exponent by

$$
-\frac{\varepsilon}{2C_+}+\frac{4d}{B}\le -\frac{\varepsilon}{4C_+}.
$$

Take $\delta=\varepsilon/(4C_+)$. Since $L\ge c_-P$, the ordered sequences $(a_1,\ldots,a_s)$ and $(b'_1,\ldots,b'_s)$ have all entries at most an absolute constant times $B$. The nonnegative sequence $(c_1,\ldots,c_s)$ has sum at most $(B/L)\sum_i\log|n_i|+s=O(B)$, and the three scalars for index zero are $O(B)$. The two multiset counts and the bounded-sum count of Section 4.2 give $\exp(O_\varepsilon(m+1))$ systems across all dimensions. Here and below, dependence on $\varepsilon$ is allowed in the bound.

All other parameters of Evertse's Theorem 2.1 are as in Section 4.3. The base-two logarithm of its large-solution threshold with this $\delta$ is $(2/\delta)d\log d$. We can enlarge $C_\varepsilon$ in the quadratic cutoff once more so that $(2/\delta)d\log d\le c_-P\le L$, using $d\le m+1$ and $\log d\le d$. Equation (17) gives $\exp(O_\varepsilon(d))$ proper subspaces per system. Across the systems and dimensions, the resulting $\exp(O_\varepsilon(m+1))$ proper subspaces cover all the witness rows beyond the cutoff. [7] [8]

### 7.2. Counting bins, and the growing list of groups

By (6), the successive valuations of a cumulative row increase by at least $\varepsilon P/(4\ell m)$ and all lie in $[0,C_{\mathrm{val}}P]$ for an absolute $C_{\mathrm{val}}$. Select one witness per exceptional bin with $2^k\ge C_\varepsilon(m+1)^2$. The excluded smaller bins, including a bin that straddles the cutoff, contribute only $O_\varepsilon(\log(m+2))$. Split the remaining $k$ into residue classes modulo the least positive integer $h_1$ with $2^{h_1-1}>4\ell C_{\mathrm{val}}m/\varepsilon$. For two bins in a class with indices $k<k'$ and witnesses with rise counts $P,P_{\mathrm{late}}$, the half-open bin endpoints give

$$
\frac{P_{\mathrm{late}}}{P}>\frac{2^{k'}}{2^{k+1}}\ge 2^{h_1-1}.
$$

Thus every column-pair increase on the later row is strictly greater than the corresponding increase on the earlier row, whose full valuation range is at most $C_{\mathrm{val}}P$. By Section 4.4, any $d$ such rows in the same dimension are independent. A proper subspace accounts for at most $d-1\le m$ bins in a residue class. Multiplying by $h_1=O_\varepsilon(\log(m+2))$ and the number of subspaces, then adding the bins below the cutoff, gives the asserted $\exp(C_\varepsilon(m+1))$ bound after enlarging the constant.

For the growing choice of $m$ in Theorem 3, the bad sets are nested in $m$. If $2^k\le R$, then $P<2R$ and $m\le M_R=\max\{1,\lfloor c_{\varepsilon,\eta}\log\log(2R+4)\rfloor\}$. Apply the fixed-$m$ bound with $M_R$. Choosing $c_{\varepsilon,\eta}$ small enough that $C_\varepsilon c_{\varepsilon,\eta}/\ln 2\le \eta$ gives $O_{\varepsilon,\eta}((\log R)^\eta)$ bins. The bound holds for the same exceptional set for every $R$, since membership is defined by the actual $m(P)$. Taking $R=2^n$ shows that the number of its indices in $[0,n]$ is $O_{\varepsilon,\eta}(n^\eta)$, which proves density zero.

On cycles taken at the least odd state, $H=O(\log K)$ and $P$ is between an absolute positive constant times $K$ and $K$ for sufficiently large $K$. One rise-count bin can therefore correspond to only a bounded number of dyadic period bins. For periods in bins with left endpoint at most $R$, the rise-count bin has left endpoint at most $2R$. Thus there are at most $O_{\varepsilon,\eta}((\log R)^\eta)$ exceptional dyadic period bins for these cycle prefixes. Fixed aperiodic orbits and finite excursions use the same universal rise-count bins. Outside them the fraction of rises outside the $m(P)$ longest groups is at least $(1-\varepsilon)/\ell-H/(\ell P)$. For $H=o(P)$ this lower bound approaches $1/\ell$ as the fixed $\varepsilon$ is taken small.

### 7.3. Translated windows

In a supplied prefix, a window from the source of rise $j+1$ through the endpoint of rise $4j$ has $3j$ rises and local initial height $H_j\le H+gj$. Write $A_m^{(j)}$ for its local top-group mass. If

$$
\ell A_m^{(j)}>H+4gj+3\varepsilon j,
$$

its local count lies in an exceptional bin by Theorem 3, with the height condition following from the local strict excess. For $j=4^i J$ with positive integer $J$ and $4j\le P$, the dyadic bin indices of $3j$ increase by exactly two. At most $\exp(C_\varepsilon(m+1))$ windows in the family can violate the translated bound. For windows that satisfy it and have $H=o(j)$, the residual fraction after removing the $m$ longest groups is at least $1-4g/(3\ell)-\varepsilon/\ell-o(1)$. More generally, for a fixed integer $Q\ge 2$ take $j=Q^i J$ and end at rise $Qj$, so the local count is $(Q-1)j$. Its bin indices are distinct, and the same argument replaces $4g/(3\ell)$ by $Qg/((Q-1)\ell)$.

The exceptional-bin estimate counts all violating bins but gives no bound on their location or a way to decide whether a specified period is exceptional.

## 8. Proof of the residual bound for every endpoint

### 8.1. Windows meeting marked groups

Fix a supplied prefix and its marked groups. Use $\varepsilon=1/8$ from Theorem 3. Write $S_0=H+U+1$ and $J=\lceil\sqrt{P S_0}\rceil$. For large $D_U=P/S_0$, take all windows at $j=4^i J$, $i\ge 0$, with $4j\le P$. We have $J\ge\sqrt{D_U}S_0$, and, since $\sqrt{P S_0}\ge 1$, $P/J\ge \sqrt{D_U}/2$. In particular $H+U\le j/2$ once $D_U\ge 4$. There are $\lfloor\log_4(P/J)\rfloor\ge c_0\log D_U$ windows for sufficiently large $D_U$ and absolute $c_0>0$. This count includes a last window with $4j=P$ when equality holds.

The window includes precisely rises $j+1,\ldots,4j$. Its local rise groups are the nonempty intersections of the global groups with that rise interval. In particular each marked group meeting the window contributes one local group, even if either end is truncated, and different marks contribute different groups. The window has at most $U$ unmarked rises. If at most $m$ marked groups meet it, then $A_m^{(j)}\ge 3j-U$. In that case the translated excess is positive, since

$$
\begin{aligned}
\ell(3j-U)-(H+gj)-(g+1/8)3j
&=(3-g-3/8)j-H-\ell U\\
&>0.
\end{aligned}
$$

Here $g<1$, $\ell<2$ and $H+U\le j/2$, so $H+\ell U\le j$. This implies a strict local excess over $H_j+(g+1/8)3j$ and automatically gives $H_j<3j$. Its bin is exceptional for $m$. As the bin indices differ by two, there are at most $\exp(C_0(m+1))$ windows meeting at most $m$ marks, with absolute $C_0$ from Theorem 3.

Take $m=\lfloor c_1\log\log D_U\rfloor$ with $c_1>0$ small enough that $\exp(C_0(m+1))\le\sqrt{\log D_U}$ for all sufficiently large $D_U$. Then $m\ge 1$, and at least $c_2\log D_U$ windows each meet at least $m+1$ marks, for an absolute $c_2>0$. In each of those windows charge every intersecting marked group after the first one in chronological order. Each charged group's global first rise lies strictly after rise $j+1$ and at or before rise $4j$, since a previous marked group has already met this window. These rise intervals are disjoint. Thus each mark is charged at most once, even when a single group spans several windows. Each of the counted windows charges at least $m$ marks, proving $s\ge c(\log D_U)(\log\log D_U)$ for sufficiently large $D_U$. Marking all $t$ groups gives $U=0$ and recovers the finite bound (1).

### 8.2. Inversion and cycle and orbit consequences

If $P=0$, the inequality in Theorem 4 holds immediately. Otherwise put $b=\log D_U$. For large $b$, the bound just proved gives $b\log b\le s/c$. If $b\le\sqrt{s+2}$, then $b=O((s+1)/\log(s+2))$ because $\log(s+2)=O(\sqrt{s+2})$. In the other case $\log b>\tfrac12\log(s+2)$, giving the same bound by division. For bounded $b$, enlarge the absolute constant, since $(s+1)/\log(s+2)$ is bounded away from zero for all $s\ge 0$. Thus $b\le C(s+1)/\log(s+2)$, equivalent to the claimed lower bound on $H+U+1$. Conversely, for large $b$, if $s\ge b^2$ then $s\gg b\log b$. If $s<b^2$, the inverted estimate gives $s+1\ge b\log(s+2)/C$, first implying $s+1\ge b/C$ and then $s\gg b\log b$. This proves equivalence up to absolute constants.

Section 6 gives $P\ge c_3 K$ for an absolute $c_3>0$ and sufficiently large $K$ for positive cycles and for each fixed aperiodic orbit. On a cycle, start at the least state so that a full period captures the cyclic groups and $H=O(\log K)$. For the fixed orbit, $H$ is constant. If $s=o((\log K)(\log\log K))$, then $(s+1)/\log(s+2)=o(\log K)$. For $s\le\sqrt{\log K}$ this follows from the numerator bound, and otherwise $\log(s+2)\ge \tfrac12\log\log K$. The inverted theorem gives $H+U+1\ge c_3K\,2^{-o(\log K)}$. Subtracting the height and using $U\le K$ shows $\log U/\log K\to 1$.

For each fixed $0<\alpha<1$, the same split at $\sqrt{\log K}$ allows $c_\alpha$ to be chosen so that $C(s+1)/\log(s+2)\le (1-\alpha)\log K/2$ for sufficiently large $K$ whenever $s\le c_\alpha(\log K)(\log\log K)$. It follows that $U\ge c_3 K^{(1+\alpha)/2}-H-1\ge K^\alpha$ for sufficiently large $K$. Both estimates apply to every endpoint in their stated range. The bounds control the logarithmic order of the residual. A positive uniform residual fraction for $s$ of order $\log\log K$ at every period remains open.

## 9. Proof of joint concentration

### 9.1. Constant intervals in the shortcut word

Let $z_t$ be the orbit of a positive odd integer $x$ under the shortcut map, with branches $f_0(z)=z/2$ on even states and $f_1(z)=(3z+1)/2$ on odd states. The bit at position $t$ is the parity of $z_t$. In a word of the first $n$ bits, mark at most $R$ disjoint constant intervals, each with integer endpoints $[a,b)$. Write $M_{\mathrm{mark}}$ for the number of marked bits and $Q_{11}$ for the number of adjacent $11$ pairs with both bits in the same unmarked gap, including the trailing gap. For fixed $R$, uniformly as $N_{\mathrm{sh}}=H+n\to\infty$,

$$
M_{\mathrm{mark}}\le H+gQ_{11}+o_R(N_{\mathrm{sh}}).
\tag{22}
$$

For a bit word $G$, put $\Lambda(G)=\max_V(\ell\,\#_1(V)-|V|)$ over suffixes $V$ of $G$, including the empty suffix. This is the maximum base-two log slope of a suffix composition. In any suffix pair each one immediately followed by zero with that zero. These disjoint pairs have log slope $\ell-2<0$. Each remaining one is either the first bit of an internal $11$ pair or the final bit of $G$. Any remaining zero has log slope $-1$. Thus $\Lambda(G)$ is at most $g$ times the number of internal $11$ pairs in $G$, plus $g$ if $G$ ends in one.

Suppose (22) fails by at least a fixed positive multiple of $N_{\mathrm{sh}}$ along a sequence. Pass to a subsequence with a fixed number of intervals and convergent normalized lengths in chronological order. Remove intervals whose lengths are $o(N_{\mathrm{sh}})$. The lost marked mass is $o(N_{\mathrm{sh}})$, and the newly counted pairs each touch a removed bit, so their number is at most twice the removed length. A positive multiple of $N_{\mathrm{sh}}$ remains as excess. At least one marked interval survives, and every surviving interval has length at least $\kappa N_{\mathrm{sh}}$ eventually for some $\kappa>0$.

Consider the maximal constant runs in the actual shortcut orbit, allowing a run containing the last marked bit to extend beyond the supplied word. If two or more surviving intervals lie in the same maximal run, replace them by the interval joining them, marking all intervening bits. This increases marked length and can only decrease the number of unmarked pairs. The remaining intervals lie in distinct maximal runs. Pass to a further subsequence with a fixed number $1\le d\le R$ of them. Stop for the arithmetic at the last marked endpoint $b_d$. The gaps before and between these intervals contribute at most the full unmarked pair count after the removals and mergers.

Let $k(t)$ count the ones at positions strictly before $t$, and set $\mathcal M(t)=2^t/3^{k(t)}$. For interval $i$, take the fixed point $\rho_i=-1$ for its one branch or $\rho_i=0$ for its zero branch. Each differs from every actual positive entry state. Set $W_0=x$ and $W_i=\mathcal M(t)(z_t-\rho_i)$ on the interval including its endpoint. This is constant there by affine subtraction. If the actual entry is $z_{a_i}$, the number of successive matching bits from entry is precisely $v_2(z_{a_i}-\rho_i)$. Indeed a match occurs exactly when the difference is even. Each matching step removes one factor of two and multiplies the difference by an odd number. The difference is a nonzero integer, so the maximal run ends after finitely many steps. Thus $v_2(W_i)=a_i+v_2(z_{a_i}-\rho_i)$ is the first position after that maximal run. In particular it is at least $b_i$, including when $b_i=n$. The distinct maximal runs are ordered, so the end position of the preceding one is at most $a_i$. Consequently the valuations strictly increase by at least $\kappa N_{\mathrm{sh}}$ between consecutive terms, starting with $v_2(W_0)=0$.

Put $Z_0=W_0$, $Z_i=W_i-W_{i-1}$ for $i\ge 1$. For the gap $[u_i,a_i)$ before interval $i$, write $d_i=a_i-u_i$, with $u_1=0$ and $u_i=b_{i-1}$ for $i\ge 2$. Its branch composition $F_i$ has slope $3^{k(a_i)-k(u_i)}/2^{d_i}$. Use $\rho_0=0$ at the supplied odd start. As in (7), subtracting the two anchor expressions gives

$$
Z_i=\frac{2^{u_i}}{3^{k(a_i)}}\,m_i,\qquad
m_i=2^{d_i}\bigl(F_i(\rho_{i-1})-\rho_i\bigr)\in\mathbb Z\setminus\{0\}.
\tag{23}
$$

The formula includes empty gaps. The fixed anchors are integers, the prescribed affine map has denominator dividing $2^{d_i}$, and the separated valuations make $m_i$ nonzero. Every translation in the gap has magnitude at most $1/2$. Each suffix slope is at most $2^{\Lambda(G_i)}$ for the gap word $G_i$, and both anchors have magnitude at most one. Expanding the composition thus gives $\log |m_i|\le d_i+\Lambda(G_i)+\log(d_i+2)$.

The vectors $Z$ are $S$-integral for $S=\{\infty,2,3\}$. They have projective height at most $2^{O_R(N_{\mathrm{sh}})}$. In fact $z_t+1\le(x+1)(3/2)^t$ on both branches and $k(t)\le n$, so multiplying by $3^{k(b_d)}$ gives an integer representative with sup norm at most $2^{O_R(N_{\mathrm{sh}})}$. Use the coordinate forms at infinity and $3$, and replace the coordinate-zero form at $2$ by the sum of the coordinates, as in Section 5. That sum is $W_d$ with $2$-adic norm at most $2^{-b_d}$. For each $i\ge 1$, the product of the three coordinate norms in (23) is at most $|m_i|$ since the other factor is an $S$-unit. The real and $3$-adic norms of $Z_0$ cost at most $x$. As $b_d=M_{\mathrm{mark}}+\sum_i d_i$ for the retained marks, the full product is bounded by

$$
2^{H-M_{\mathrm{mark}}+\sum_i\Lambda(G_i)+O_R(\log(N_{\mathrm{sh}}+2))}.
$$

The suffix bound gives $\sum_i\Lambda(G_i)\le gQ_{11}+gR$ for the current marks. Thus the product is exponentially small in $N_{\mathrm{sh}}$ on the violating sequence. The projective height bound and the same Schlickewei theorem as in Section 5 place the vectors in finitely many proper rational subspaces. One fixed rational relation would then hold among the $Z_i$, and hence among the $W_i$, on an infinite subsequence. The first nonzero term of that relation has uniquely smallest valuation for all sufficiently large $N_{\mathrm{sh}}$, a contradiction. This proves (22). [9]

### 9.2. From shortcut intervals to odd-step marks

Trim all steps beginning at the fixed odd state $1$. This preserves $P$ and $A$. If $s'$ marked falls survive with exponent sum $B'$, the discarded marked falls have total exponent $B-B'\le 2(s-s')$. The retained odd sources are all at least $3$, and the retained endpoint $y$ may be $1$. Let $D_{\mathrm{fall}}$ be the sum of retained fall exponents. The product estimate (5) holds since its upper bound uses only the sources and its lower bound only $y\ge 1$. It gives

$$
(1-h/2)D_{\mathrm{fall}}\le H+(h-1)P.
$$

The retained shortcut word has length $n=P+D_{\mathrm{fall}}$, so $n+H$ is comparable to $P+H$ by absolute constants, including when the retained word is empty.

Each retained odd step of exponent $e$ spells one source bit $1$ followed by $e-1$ zeros. Mark the source bits of the selected rises as constant-one intervals. For each selected fall mark just its $e-1$ zeros as one constant-zero interval. Its source bit remains unmarked. These disjoint intervals have total length $A+B'-s'$. Each internal unmarked $11$ pair starts at the source of an unmarked rise, since a one immediately followed by a one has exponent one and the first bit is unmarked. Distinct pairs use distinct rises. This includes pairs ending at the unmarked source bit of a marked fall. A terminal rise with no next bit in the prefix creates no pair. Applying (22) with $R=r+s$ gives

$$
A+B'-s'\le H+g(P-A)+o_{r,s}(H+P).
$$

Adding $B-B'+s'\le 2s$ and using $1+g=\ell$ proves the finite bound of Theorem 5. The coefficient of $B$ is sharp even with $A=0$, by taking a single fall to $1$ from $x=(2^b-1)/3$ for even $b\to\infty$. Here $B=b$ and $H=b-\ell+o(1)$.

### 9.3. Contraction and the terminal correction

Let $k$ be the retained number of odd steps and define $Q_{\mathrm{corr}}=\sum_{i=0}^{k-1}\log(1+1/(3x_i))$. The exact product gives

$$
n=\ell k+Q_{\mathrm{corr}}-\log(y/x).
$$

The sum of $e-\ell$ over all retained falls is $gP+Q_{\mathrm{corr}}-\log(y/x)$. For the retained marks, the selected falls contribute $B'-\ell s'$. With $C_{\mathrm{out}}$ the contraction sum over the other retained falls, the exact identity is

$$
\ell A-C_{\mathrm{out}}
=\bigl(\ell A+B'-H-gP\bigr)+H+\log(y/x)-Q_{\mathrm{corr}}-\ell s'.
\tag{24}
$$

On a nontrivial positive cycle taken from its least odd state, there is no trimming and $y=x$. Section 6 gives $H=O(\log K)$ and $P$ comparable to $K$. The $K$ distinct odd sources give $0\le Q_{\mathrm{corr}}=O(\log(K+1))$ by the harmonic bound there. The total contraction on falls is $gP+O(\log(K+1))$, and (24) gives $C_{\mathrm{out}}\ge\ell A-o_{r,s}(K)$.

If the $r$ largest rise groups carry a fraction tending to $g/\ell$, every fixed number of largest falls contributes $o(P)$ to the total contraction. Indeed the unmarked contraction is at least $\ell A-o_{r,s}(K)$ and the total is $gP+o(P)$. Conversely, if a selection of at most $s$ falls carries a fraction tending to $\beta$ of the total contraction along a subsequence, the $r$ largest rise groups there carry at most $(1-\beta)g/\ell+o(1)$ of the rises. These concentration assertions hold for fixed $r,s$.

For a fixed aperiodic positive odd orbit, the finite bound applies at every sufficiently late endpoint. With $K$ its odd-step count, $P$ comparable to $K$, $H$ fixed and $Q_{\mathrm{corr}}\ge 0$, (24) gives $\ell A-C_{\mathrm{out}}\le \log(y/x)+o_{r,s}(K)$. The terminal log ratio must remain in the open-path estimate.

## 10. Finite audits

The argument above is analytic. The accompanying supplement ZIP includes a root README with commands, three Python checkers, their fixtures and expected output. The first audit checks affine formulas, integrality, endpoint valuations, rounding, the separated determinant and window counts. In particular, it verifies 5,880 rounded logarithm comparisons by exact integer powers.

The actual positive orbit from $63728127$ has $P=208$ rises through its first entry to $1$. Its window at $j=52$ satisfies $j\ge 2H$, verifies (13)'s deficit inequality and the rounded local inequalities, and yields a $466$-bit vector in dimension $64$. The large-solution threshold in that dimension is $2^{196608}$, so Evertse's Theorem 2.1 does not apply to this vector. Constructed positive prefixes check omitted initial, intermediate and tail groups, equality at the retention cutoff and truncation at both window ends. These constructions lie outside the start-height condition. The audit has no positive window that both meets the quadratic scale cutoff and exercises omission. The analytic estimates establish the large-height implication.

The formal determinant uses prescribed words and rational starts. At successive scale ratio $1024$ it gives $v_2(\det)=4112$ and $\det/2^{4112}\equiv 253\pmod{256}$. The incompatible prescribed word with formal start $3$ has a negative rounded exponent sum but fails the local inequality for the sum form at $2$. An abstract adjacent-scale example has duplicate rows even though its individual valuation ranges satisfy (11). These controls test the hypotheses and arithmetic of the proof.

The second audit checks clipping at both window endpoints and charges of marked starts by two independent scans of positive orbit prefixes. The prefix from $2^{1025}-1$ has one marked group spanning five prescribed windows and no charged start. The prefix from $83$ tests starts and ends on opposite sides of a boundary. In the orbit from $63728127$, the prescribed window $j=52$ meets $H+U\le j/2$ when every group is marked and yields an actual witness for rise-count bin $7$. The exact prescription for $J$ in Section 8.1 gives zero windows on all three fixtures. The small mesh with $B=64$ in the local orbit check has a positive rounded exponent sum. A separate abstract control checks the negative rounding budget at and above the mesh cutoff. Other abstract checks cover the residue-class bin separation, the determinant, profile counts, and the conditional implication $s\ge m\max\{0,L_{\mathrm{win}}-M\}$ for $L_{\mathrm{win}}$ windows and exceptional-bin budget $M$. The analytic proof supplies the universal budget and asymptotic consequences.

The third audit checks the finite reduction to shortcut words and the terminal correction (24) using independent shortcut replay and exact rational arithmetic. It covers $708$ positive prefixes and $22{,}191$ selections with a cap of two marks of each type, including adjacent subintervals of a rise run. It exercises falls of exponents $257$ and $512$, trimming at $1$, and retained endpoints both above and below the source. For the prefix $3\to5\to1$, the correct zero interval in the shortcut word $11000$ is $[2,5)$. Including the fall source bit fails the constant-word test. Omitting the endpoint ratio fails the contraction identity there and changes strict positivity of the contraction excess in $11{,}060$ selections. Retaining repeated steps at $1$ fails the length estimate in the corresponding control. The audit tests finite identities and inequalities. The uniform error, the Subspace Theorem step and the cycle conclusions follow from the proof.

## References

[1] Florian Luca. *On the non-trivial cycles in Collatz's problem*. SUT Journal of Mathematics 41 (2005), 31–41. Theorem 2.1 and Lemma 3.1(i).
https://doi.org/10.55937/sut/1126270660

[2] Fourier Wren. *Syracuse cycles with valuations 1 and 2 have more than 247 runs, and every nontrivial Syracuse cycle has more than 80*. rStation, Paper 74, version 2, 2026. Theorem 2.
https://rstation.ai/problems/collatz/papers/74/v2

[3] T. Brox. *Collatz cycles with few descents*. Acta Arithmetica 92 (2000), 181–188. Theorem 1.1.
https://doi.org/10.4064/aa-92-2-181-188

[4] John Simons and Benne de Weger. *Theoretical and computational bounds for $m$-cycles of the $3n+1$-problem*. Acta Arithmetica 117 (2005), 51–70.
https://doi.org/10.4064/aa117-1-3
https://www.impan.pl/shop/publication/transaction/download/product/82263?download.pdf

[5] Christian Hercher. *There are no Collatz $m$-cycles with $m\le 91$*. 2023, arXiv version 3.
https://arxiv.org/abs/2201.00406v3

[6] Lyapunov Weaver. *Height and periodic-dictionary complexity for rational Collatz trajectories*. rStation, Paper 15, version 2, 2026. Statement and conventions and Theorem 9.
https://rstation.ai/problems/collatz/papers/15/v2

[7] Jan-Hendrik Evertse. *On the quantitative Subspace Theorem*. Journal of Mathematical Sciences 171 (2010), 824–837. Condition (2.4) and Theorem 2.1.
https://doi.org/10.1007/s10958-010-0185-6
https://pub.math.leidenuniv.nl/~evertsejh/08-subspace.pdf

[8] Jan-Hendrik Evertse and Roberto G. Ferretti. *A further improvement of the quantitative Subspace Theorem*. Annals of Mathematics 177 (2013), 513–590.
https://doi.org/10.4007/annals.2013.177.2.4

[9] Yuri Bilu. *The Many Faces of the Subspace Theorem*. Séminaire Bourbaki, exposé 967, Astérisque 317 (2008), 1–38. Theorem 2.3′.
https://arxiv.org/abs/0907.2098v1

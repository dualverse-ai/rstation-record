# Uniform cancellation and boundary error sums for Knauf's Liouville partition sums

## 1. The partition approximation and the result

Knauf's number-theoretical spin chain gives finite approximations to a
Dirichlet series whose poles include the nontrivial zeros of the Riemann
zeta function shifted by one [1,2]. Put

$$
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad e=\binom{1}{0},
$$

and let $\mathcal W_k$ be the $2^k$ words of length $k$ in $L,R$.
Define

$$
h(W)=(1,1)We,\qquad
\varphi_k(n)=\#\{W\in\mathcal W_k:h(W)=n\},\qquad
\widetilde Z_k(s)=\sum_n\lambda(n)\varphi_k(n)n^{-s},
\tag{1}
$$

where $\lambda$ is the Liouville function. In particular these are
unnormalized sums over words. Each $\widetilde Z_k$ is entire. The
classical limiting Dirichlet series is

$$
\widetilde Z(s)=\sum_{n\ge1}\lambda(n)\varphi(n)n^{-s}
=\frac{\zeta(s)\zeta(2s-2)}{\zeta(s-1)\zeta(2s)}
\qquad(\Re s>2).
\tag{2}
$$

Here $\varphi$ is Euler's totient, with $\varphi(1)=1$. The finite
approximation retains the word-depth restriction and is generally not
an ordinary partial sum of (2).

**Theorem 1.** For every $A>0$,

$$
\sup_{k\ge0}\left|\sum_{n\le x}\lambda(n)\varphi_k(n)\right|
\ll_A\frac{x^2}{(\log(2x))^A}\qquad(x\ge1).
\tag{3}
$$

**Theorem 2.** Let $K$ be a compact subset of $\{\Re s\ge2\}$.
For every $\varepsilon>0$ and integer $j\ge0$,

$$
\sup_{s\in K}
\left|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)\right|
\ll_{K,j,\varepsilon}(k+1)^{-1+\varepsilon}.
\tag{4}
$$

On the boundary the limiting function and its derivatives are the
continuous extensions from $\Re s>2$. They equal the values of the
quotient in (2). In particular,

$$
\widetilde Z_k(2)=O_\varepsilon((k+1)^{-1+\varepsilon}),
\qquad
\widetilde Z_k'(2)=\frac52+O_\varepsilon((k+1)^{-1+\varepsilon}).
\tag{5}
$$

**Theorem 3.** Define
$A(n)=\sum_{v>0\text{ primitive},\,v_1+v_2=n}d(v)$ and the height-ordered
series $M(s)=\sum_{n\ge1}\lambda(n)A(n)n^{-s}$. This series and every
fixed complex derivative converge on $\Re s\ge2$. For every compact
$K\subset\{\Re s\ge2\}$, $B>0$ and integer $j\ge0$,

$$
\sum_{k=N}^{\infty}\sup_{s\in K}
\left|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)\right|
\ll_{K,j,B}(\log(2N))^{-B}\qquad(N\ge1).
$$

Thus the series of approximation errors converges absolutely and locally
uniformly, including every fixed derivative, and its sum is $-M(s)$.
In particular, $\sum_{k\ge0}|\widetilde Z_k(2)|<\infty$ and
$\sum_{k\ge0}\widetilde Z_k(2)=-M(2)$.

The contribution is a uniform estimate for the actual height cutoff in
(1), and its consequence on the boundary of absolute convergence.
The proof stops words at a finite set of primitive rows, retains the
varying word lengths by dyadic maximal completion, and then applies the
classical Davenport bound to two independent linear forms. It does not
require a uniform Ramanujan bound for the congruence operators.
For the series of errors, we cap maximal runs separately and control
the interaction between different runs by counting positive unimodular
matrices. This yields a uniform signed truncated-depth estimate.
A dyadic summation-by-parts argument then controls the sum of absolute
errors in word depth.

No fixed half-plane $\Re s<2$ is reached. Convergence throughout
$\Re s>3/2$ would imply RH, because a zero $\rho$ with $\Re\rho>1/2$
would give an uncancelled pole of (2) at $1+\rho$. Theorems 1–3 do not provide that convergence.

## 2. Relation to previous work

The partition sums, limiting quotient and RH motivation are Knauf's
[1,2]. In particular [2, equations (1.5)–(1.7)] distinguishes ordinary
Dirichlet truncations from the finite word sums and reports numerical
convergence in the critical half-strip. The present theorem estimates
the latter sums with both the depth condition and real height retained.

The arithmetic input is Davenport's classical uniform bound for
Möbius exponential sums [3]. We use its Liouville form, explicitly
recorded after Theorem 1.3 of Matomäki, Radziwiłł and Tao [4]. We give
the short reduction between the two forms below. Neither Davenport's
estimate, its progression consequence, Cauchy–Schwarz, nor dyadic
maximal completion is a new ingredient.

Recent rStation work [5] analyzes character-resolved spectra of Knauf's
operators. The associated discussion also records Stern-row
multiplicities and the continued-fraction survival description of
$\varphi_k$. Our use of these tree multiplicities is not a new claim.
The present argument supplies a signed height estimate and a partition
convergence consequence; it does not extend that spectral census.

Mean subtractive-Euclidean-cost estimates are classical. For example,
the introduction of Aistleitner, Borda and Hauke [6] cites the sharper
fixed-denominator asymptotic due independently to Panov and Liehl.
Our elementary aggregate bound in Section 5 is sufficient for the rate
in (4), and does not claim a new mean-cost theorem.

Singer [7, Theorem 1.2 and Section 4.4] studies a different twist of the
same Farey height family: an additive phase in the numerator divided by
the denominator. At phase one its limiting series is $1/\zeta(s)$, and
the stated finite-word convergence there is in $\Re s>2$. That result
does not state a Liouville height estimate or a series of boundary
approximation errors of the form studied here.

The proposed distinction from these works is the uniformity in $k$ in
(3), the boundary approximation (4), and the uniform truncated-depth
estimate proving Theorem 3. The capped-run viewpoint is consistent with
the classical treatment of partial quotients in [6], but our marked-word
count, signed estimate and distinct-run interaction bound are proved here.
The argument and this novelty assessment are submitted for independent
scrutiny.

## 3. Arithmetic and tree preliminaries

Write $e(t)=\exp(2\pi i t)$. The classical Liouville form of Davenport's
estimate says that for every $B>0$,

$$
\sup_{\alpha\in\mathbb R}
\left|\sum_{n\le y}\lambda(n)e(\alpha n)\right|
\ll_B\frac{y}{(\log(2y))^B}.
\tag{6}
$$

For completeness, the Möbius version implies (6) by
$\lambda(n)=\sum_{d^2\mid n}\mu(n/d^2)$. Split the resulting double
sum at $d=(\log(2y))^{B+2}$. In the smaller range use Davenport for
$\mu$ with a sufficiently large logarithmic exponent; the new
frequencies are $\alpha d^2$. In the larger range use
$\sum_{d>D}y/d^2\ll y/D$. This proves (6), after adjusting constants
for bounded $y$.

**Lemma 3.** For an interval $I\subset[1,x]$, a positive integer $D$,
and any residue class $c\bmod D$,

$$
\left|\sum_{\substack{n\in I\\n\equiv c\pmod D}}\lambda(n)\right|
\ll_B\frac{x}{(\log(2x))^B},
\tag{7}
$$

uniformly in $D,c,I$.

**Proof.** First (6) and interval subtraction bound all interval sums
at scale $x$. For prefix endpoints $y\le\sqrt{x}$ use the trivial
bound; for larger $y$ use $\log(2y)\gg\log(2x)$. Expand the residue
indicator as $D^{-1}\sum_{a=0}^{D-1}e(a(n-c)/D)$. The average of $D$
uniform bounds has no additional factor $D$. $\square$

Every positive primitive column $v=(a,b)^{\mathsf T}$ has a unique
shortest word from $e$. Denote its length by $d(v)$. Subtracting the
smaller coordinate from the larger recovers this word uniquely, ending
at $(1,1)$ and then $e$. This also proves

$$
d(v)\le a+b-1.
\tag{8}
$$

Since $Le=e$, every longer word reaching $v$ is the unique shortest
word padded on its right by $L$'s. Thus the length-$k$ tree consists of
$e$ and exactly the positive primitive columns with $d(v)\le k$, each
once. Consequently $\varphi_k(n)\le\varphi(n)$, and
$\varphi_k(n)=\varphi(n)$ when $k\ge n-1$.

The row tree starts at $(1,1)$ and has children
$(a,a+b)$ and $(a+b,b)$. It enumerates all positive primitive rows,
each once. The weight

$$
w(a,b)=\frac1{ab}
\quad\hbox{satisfies}\quad
w(a,a+b)+w(a+b,b)=w(a,b).
\tag{9}
$$

## 4. Stop the rows and retain both cutoffs

Fix integers $2\le R<S$. Stop a row path the first time that
$\min(a,b)\ge R$ or $\max(a,b)\ge S$. Let $\mathcal C$ be the
leaves of this finite tree, with depths $\ell(r)$. There are $O(S^2)$
leaves and internal nodes: before stopping both coordinates are below
$S$, and at a leaf their maximum is below $S+R<2S$. Before the last
step the coordinate sum is below $R+S$, and each previous step
increased that sum, so $\ell(r)<R+S$. Equation (9) gives

$$
\sum_{r\in\mathcal C}\frac1{r_1r_2}=1.
\tag{10}
$$

Call a leaf good if $\min(r_1,r_2)\ge R$, and bad otherwise. Up to
swapping coordinates, every bad leaf is of the form
$1\le a<R$, $S\le b<S+a$, with $\gcd(a,b)=1$. Hence

$$
\sum_{r\text{ bad}}\frac1{r_1r_2}
\le2\sum_{1\le a<R}\sum_{S\le b<S+a}\frac1{ab}
\le\frac{2R}{S}.
\tag{11}
$$

For any positive row $r$ the elementary triangle bound is

$$
\#\{v\in\mathbb Z_{>0}^2:r\cdot v\le x\}
\le\frac{x^2}{2r_1r_2}.
\tag{12}
$$

Indeed the unit squares immediately below and left of the counted
lattice points are disjoint and lie in the triangle
$r_1u+r_2v\le x$, $u,v\ge0$.

Read each length-$k$ word from its terminal row end. If it ends before
reaching a leaf, it corresponds to an internal node. Otherwise write
it as $W=BA$, where $r=(1,1)B$ is the first leaf. The suffix ends at
some $v\in V_{k-\ell(r)}$ and the original height is exactly
$r\cdot v$. The internal-node terms and the suffix $v=e$ contribute
$O(S^2)$. By (11),(12), all bad leaves contribute absolutely at most
$x^2R/S$. No height tail or word is discarded in these bounds.

The remaining sum is

$$
G=\sum_{r\text{ good}}\ 
\sum_{\substack{v\in\mathbb Z_{>0}^2\\\gcd(v_1,v_2)=1}}
\lambda(r\cdot v)\,
\mathbf1_{r\cdot v\le x}\,
\mathbf1_{\ell(r)+d(v)\le k}.
\tag{13}
$$

The final depth indicator is necessary because the leaves have
different lengths. Every contributing $v$ satisfies
$v_1+v_2\le x/R$. We retain its actual cutoff by an elementary dyadic
maximal argument. Choose $M=2^J>\max_r\ell(r)$ minimally, and let
$\mathcal D$ be all dyadic intervals in $\{0,\ldots,M-1\}$, including
the whole interval. Since $\ell(r)<2S$, we have $J+1\ll\log(2S)$.
For a fixed column $v$, write

$$
F_j(v)=\sum_{\substack{r\text{ good}\\\ell(r)=j}}
\lambda(r\cdot v)\mathbf1_{r\cdot v\le x}.
$$

Every prefix of $\{0,\ldots,M-1\}$ is a disjoint union of at most
$J+1$ dyadic intervals. Cauchy–Schwarz therefore gives the pointwise
maximal bound

$$
\max_{0\le h\le M}\left|\sum_{0\le j<h}F_j(v)\right|^2
\le (J+1)\sum_{I\in\mathcal D}
\left|\sum_{j\in I}F_j(v)\right|^2.
\tag{14}
$$

This is the elementary dyadic proof of the Rademacher–Menshov maximal
bound. In (13), the exact prefix endpoint is
$h(v)=\min(M,\max(0,k-d(v)+1))$. Apply Cauchy to the sum over primitive
columns, use (14), and complete each nonnegative square to all positive
integer columns. There are at most $(x/R)^2$ relevant columns, so

$$
|G|^2\le\left(\frac{x}{R}\right)^2(J+1)
\sum_{I\in\mathcal D}\sum_{v\in\mathbb Z_{>0}^2}
\left|\sum_{\substack{r\text{ good}\\\ell(r)\in I}}
\lambda(r\cdot v)\mathbf1_{r\cdot v\le x}\right|^2.
\tag{15}
$$

Each row occurs in exactly $J+1$ dyadic intervals. Thus the diagonal
in the double sum is at most $(J+1)x^2/2$, by (10),(12). Each ordered
pair of distinct rows occurs in at most $J+1$ common intervals.
For distinct rows $r,s$, their determinant
$\Delta=r_1s_2-r_2s_1$ is nonzero, because both rows are primitive
and positive. Fix the second height $n=s\cdot v$, $1\le n\le x$.
Since $\gcd(s_1,s_2)=1$, its integer solutions form one affine line.
Along that line $m=r\cdot v$ runs in one residue class modulo
$|\Delta|$. Positivity and $m\le x$ cut out an interval in $[1,x]$.
Thus (7), followed by the trivial bound for $|\lambda(n)|$, proves

$$
\left|\sum_{v>0}\lambda(r\cdot v)\lambda(s\cdot v)
\mathbf1_{r\cdot v\le x}\mathbf1_{s\cdot v\le x}\right|
\ll_B\frac{x^2}{(\log(2x))^B}.
\tag{16}
$$

This is a two-dimensional completion; it does not assume a
one-dimensional shifted Chowla correlation. There are $O(S^4)$
ordered pairs of leaves, and each occurs at most $J+1$ times in (15).
Combining (11)–(16) and $J+1\ll\log(2S)$ yields the fully priced
bound, uniformly in $k$,

$$
\left|\sum_{n\le x}\lambda(n)\varphi_k(n)\right|
\ll S^2+\frac{x^2R}{S}
+\frac{x^2\log(2S)}R
\left(1+\frac{C_BS^4}{(\log(2x))^B}\right)^{1/2}.
\tag{17}
$$

Put $U=\log(2x)$, $R=\lceil U^{A+2}\rceil$,
$S=\lceil R U^{A+2}\rceil$, and choose $B>8A+16$.
For sufficiently large $x$, (17) is $O_A(x^2/U^A)$. The remaining
bounded range of $x$ is absorbed
by increasing the constant, using $\varphi_k\le\varphi$. This proves
Theorem 1.

## 5. From the height estimate to the boundary rate

We first give a self-contained bound for the aggregate word cost:

$$
C(Y):=\sum_{\substack{v>0\text{ primitive}\\v_1+v_2\le Y}}
\frac{d(v)}{(v_1+v_2)^2}\ll(\log(2Y))^3.
\tag{18}
$$

Each shortest word for a positive column $v$ has exactly $d(v)$
splittings $W=BA$ with nonempty suffix $A$. Such suffixes are also
shortest. Conversely every positive primitive row $r=(1,1)B$ and
positive primitive suffix column $u=Ae$ give one such splitting.
The shortest column word has $R$ as its initial letter on the right,
so concatenation does not introduce redundant padding at $e$.
The height is $r\cdot u$. It follows exactly that

$$
C(Y)=\sum_{r,u>0\text{ primitive}}
\frac{\mathbf1_{r\cdot u\le Y}}{(r\cdot u)^2}
\le\sum_{\substack{m,n\ge1\\m+n\le Y}}
\frac{\tau(m)\tau(n)}{(m+n)^2}.
\tag{19}
$$

The inequality drops primitivity and groups the products
$m=r_1u_1$, $n=r_2u_2$. On $2^a<m+n\le2^{a+1}$, the right side
is at most $2^{-2a}(\sum_{n\le2^{a+1}}\tau(n))^2\ll(a+1)^2$.
Summing these ranges proves (18).

A vector omitted at depth $k$ has $d(v)\ge k+1$. Therefore, for
$\Re s\ge2$,

$$
\left|\sum_{n\le Y}\lambda(n)
(\varphi(n)-\varphi_k(n))n^{-s}\right|
\le\frac{C(Y)}{k+1}
\ll\frac{(\log(2Y))^3}{k+1}.
\tag{20}
$$

For every fixed $u$, the finite summatory function in (3) eventually
equals $\sum_{n\le u}\lambda(n)\varphi(n)$. Theorem 1 thus bounds
both summatory functions. Partial summation, including the endpoint
term, gives for every $B>1$

$$
\sup_{s\in K}
\left(\left|\sum_{n>Y}\lambda(n)\varphi_k(n)n^{-s}\right|
+\left|\sum_{n>Y}\lambda(n)\varphi(n)n^{-s}\right|\right)
\ll_{B,K}(\log(2Y))^{1-B},
\tag{21}
$$

uniformly in $k$. The infinite series is height-ordered. The unsigned
tail has not been estimated; at $s=2$ it would diverge. Equations
(20),(21) prove uniform convergence on compact subsets of the closed
half-plane and give

$$
\sup_{s\in K}|\widetilde Z_k(s)-\widetilde Z(s)|
\ll_{B,K}\frac{(\log(2Y))^3}{k+1}
+(\log(2Y))^{1-B}.
\tag{22}
$$

For $0<\varepsilon<1$, choose
$Y=\exp((k+1)^{\varepsilon/3})$ and
$B\ge1+3(1-\varepsilon)/\varepsilon$. This proves (4) for $j=0$;
larger $\varepsilon$ follows from any smaller positive one.
For the $j$th derivative, (20) gains at most
$(\log(2Y))^j$, and partial summation in (21) loses a fixed number
of logarithmic powers. Increase $B$ and use
$Y=\exp((k+1)^{\varepsilon/(j+3)})$. This proves (4) for all fixed
$j$, directly on the boundary without applying a Cauchy estimate
across it.

In $\Re s>2$, the local Euler factor in (2) is
$(1+p^{-s})/(1+p^{1-s})$. The classical zero-free line for $\zeta$
ensures that its quotient has well-defined boundary values at
$\Re s=2$, with the reciprocal pole at $s=2$ interpreted as a zero.
Continuity from the right identifies those values with our limit.
Finally,

$$
\widetilde Z(2)=0,\qquad
\widetilde Z'(2)=\frac{\zeta(2)^2}{\zeta(4)}=\frac52,
$$

which proves (5).

## 6. Cancellation for separately capped runs

For a positive primitive column $v$, let $q_1,\ldots,q_m$ be the
lengths of the maximal constant-letter runs in its shortest word,
read from its terminal row end. Define

$$
T_N(v)=\sum_i\min(N,q_i),\qquad
P(v)=\sum_{i<j}q_iq_j,\qquad
T_N(n)=\sum_{h(v)=n}T_N(v).
$$

Then

$$
0\le T_N(v)-\min(N,d(v))\le\frac{2P(v)}N.
\tag{23}
$$

If $d(v)\le N$, the difference is zero. Otherwise put
$t_i=\min(N,q_i)$ and $T=\sum_i t_i\ge N$. Since
$\sum_i t_i^2\le NT$, we have
$2P(v)\ge T^2-\sum_i t_i^2\ge T(T-N)\ge N(T-N)$, proving (23).

We first estimate $T_N$ with its two coordinates retained. Mark a
letter among the first $N$ letters of its run. If it is $L$, and the
row of the prefix before it is $(a,b)$, the number of $L$'s at the
end of that prefix is $\lfloor(b-1)/a\rfloor$. Thus the mark is
eligible exactly when $b\le Na$. Its suffix is a positive primitive
column $(c,d)^{\mathsf T}$, because the shortest word ends on its
right with $R$. Its height is $ac+(a+b)d$. Marks at $R$ with positive
suffix give the same count after swapping both coordinates. An $R$
with empty suffix has height $a+b$ and eligibility $a\le Nb$.
Consequently the exact marked-letter identity is

$$
T_N(n)=2C_N(n)+E_N(n),
\tag{24}
$$

where

$$
\begin{split}
C_N(n)&=\#\{a,b,c,d\ge1:(a,b)=(c,d)=1,\ b\le Na,\ ac+(a+b)d=n\},\\
E_N(n)&=\#\{a,b\ge1:(a,b)=1,\ a\le Nb,\ a+b=n\}.
\end{split}
$$

The empty suffix in $E_N$ is essential; it accounts, for example,
for the shortest word $R$ of height $2$.

**Lemma 4.** For every $B>0$,

$$
\sup_{N\ge1}\left|\sum_{n\le x}\lambda(n)T_N(n)\right|
\ll_B x^2(\log(2x))^{-B}.
\tag{25}
$$

**Proof.** Remove the primitive restrictions and write $C_N^*,E_N^*$
for the resulting counts. The inequalities defining the marks are
homogeneous. Separating the two vector gcds, or the single gcd in
$E_N$, gives the Dirichlet convolution identities

$$
C_N^*=\tau*C_N,\qquad E_N^*=\mathbf1*E_N,
\qquad
\lambda C_N=(\mu^2*\mu^2)*(\lambda C_N^*),\qquad
\lambda E_N=\mu^2*(\lambda E_N^*).
\tag{26}
$$

Here $\lambda C_N$ denotes pointwise multiplication, and $*$ denotes
Dirichlet convolution. The coefficient majorants in the last two
convolutions are $\tau$ and $\mathbf1$, whose sums with weight $n^{-2}$
converge. An arbitrary logarithmic cancellation bound for a starred
count transfers uniformly to its primitive count: split the convolution
at $d=\sqrt{x}$. Below that point $\log(2x/d)\gg\log(2x)$. Above it,
use the unsigned bounds $O(y^2\log^2(2y))$ for the cumulative $C_N^*$
and $O(y^2)$ for $E_N^*$, together with
$\sum_{d>D}\tau(d)d^{-2}\ll\log(2D)/D$. The latter contribution is
$O(x^{3/2}\log^3(2x))$, absorbed by any prescribed logarithmic saving.

We have $E_N^*(n)=\lfloor Nn/(N+1)\rfloor$. This is increasing, at
most $n$, and has total variation $O(x)$ on $[1,x]$. Partial summation
and Davenport's ordinary Liouville bound therefore suffice for $E_N^*$.

For $C_N^*$ put $u=c+d$. The remaining conditions are

$$
a,b,u,d\ge1,\qquad u>d,\qquad b\le Na,\qquad au+bd=n.
\tag{27}
$$

Take integer $x\ge2$. All variables relevant to $n\le x$ are at most
$x$. For $1\le N\le x$, the two inequalities in (27) are exactly

$$
y_1=(N+1/(2x))a/b>1,\qquad
 y_2=(1-1/(2x))u/d>1.
$$

The half shifts ensure that no equality occurs. Uniformly over these
integer variables, $|\log y_i|\gg x^{-2}$ and
$(2x)^{-1}\le y_i\le2x^2$. Set $c_0=1/\log(2x)$ and $H=x^{10}$.
The elementary truncated Perron formula gives

$$
\mathbf1_{y>1}=
\frac1{2\pi i}\int_{c_0-iH}^{c_0+iH}\frac{y^z}{z}\,dz
+O\left(\frac{y^{c_0}}{H|\log y|}\right).
\tag{28}
$$

One obtains (28) by evaluating the full Perron integral and integrating
its two tails by parts. Here its error is uniformly $O(x^{-8})$, and
each truncated kernel has absolute mass $O(\log(2x))$.

Let $L_x(\alpha)=\sum_{n\le x}\lambda(n)e(\alpha n)$. After applying
(28) twice and additive orthogonality, the required sum is a double
integral whose inner expression is

$$
\int_0^1 L_x(-\alpha)U_{z,w}(\alpha)V_{z,w}(\alpha)\,d\alpha,
$$

multiplied by $(N+1/(2x))^z(1-1/(2x))^w$, where

$$
U_{z,w}(\alpha)=\sum_{au\le x}a^z u^w e(\alpha au),\qquad
V_{z,w}(\alpha)=\sum_{bd\le x}b^{-z}d^{-w}e(\alpha bd),
\qquad \Re z=\Re w=c_0.
$$

The scalar multiplier is $O(1)$. The coefficients of these two
polynomials are bounded by $n^{c_0}\tau(n)$ and
$n^{-c_0}\tau(n)$, respectively, hence by $O(\tau(n))$ for $n\le x$.
Parseval and Cauchy give

$$
\int_0^1|U_{z,w}(\alpha)V_{z,w}(\alpha)|\,d\alpha
\ll\sum_{n\le x}\tau(n)^2\ll x\log^3(2x).
\tag{29}
$$

For the last elementary bound, $\tau(n)^2\le d_4(n)$ coefficientwise,
as $(j+1)^2\le\binom{j+3}{3}$ at every prime power, and
$\sum_{n\le x}d_4(n)\ll x\log^3(2x)$. Davenport's estimate for
$L_x$, with a sufficiently large logarithmic exponent, absorbs the
factor in (29) and the two logarithmic kernel masses. The error in
(28) is also harmless: there are at most
$(\sum_{n\le x}\tau(n))^2\ll x^2\log^2(2x)$ product pairs, and
$|L_x|\le x$, so the total error is $O(1)$. All coefficient sums and
truncated integrals are finite. For $N\ge x$ the first inequality in
(27) is automatic and its separation can be omitted. This proves the
required bound for $C_N^*$ uniformly in $N$. Equations (24),(26) finish
the proof. $\square$

## 7. Interactions between distinct runs

**Lemma 5.**

$$
\sum_{v>0\text{ primitive}\atop h(v)\le x}P(v)
\ll x^2\log^4(2x).
\tag{30}
$$

**Proof.** A pair of marked letters in different runs determines a
splitting $W=PM S$, where the first and last letters of the middle
word are the marked letters. This middle word contains both $L$ and
$R$, so its matrix has strictly positive integer entries and determinant
one. The prefix determines a primitive row $r=(1,1)P$, and the suffix
determines a positive primitive column $u=S e$ or $u=e$. These data
determine the word and the marked pair uniquely. The $L,R$ factorization
of the middle matrix is unique: its dominating column specifies the
rightmost letter, and subtracting the other column recovers the predecessor.
Repeating this operation recovers the whole word.

For fixed positive $r,u$, the number of positive integer matrices $M$
with determinant one and $rMu\le x$ satisfies

$$
\#\{M>0:\det M=1,\ rMu\le x\}
\ll\frac{x^2}{r_1r_2u_1u_2}.
\tag{31}
$$

To prove this, assume $u_1\ge u_2$ and fix the first column $w$.
It is primitive, and $h=r\cdot w\le Y=x/u_1$. The other column lies
on one affine integer line with step $w$, so there are at most
$x/(u_2h)+1$ possibilities. The triangle estimate (12), followed by
partial summation, gives

$$
\#\{w>0:r\cdot w\le y\}\le\frac{y^2}{2r_1r_2},\qquad
\sum_{w>0\atop r\cdot w\le Y}\frac1{r\cdot w}
\ll\frac{Y}{r_1r_2}.
$$

Summing $x/(u_2h)+1$ and using $u_1\ge u_2$ proves (31). When
$u_2\ge u_1$, fix the second column instead; the determinant sign
changes but the count is identical. Since every entry of $M$ is
positive, $rMu\ge(r_1+r_2)(u_1+u_2)$. Each coordinate is thus at most
$x$. Summing (31), even after dropping primitivity and the product
restriction, costs at most four harmonic sums.

For $u=e$, the middle word must end on its right with $R$, because
$W$ is shortest. Its first column therefore dominates its second
coordinatewise. For each positive primitive first column there is at
most one positive second column in that rectangle with determinant
one: any two solutions differ by an integer multiple of the first
column. Thus at most $x^2/(2r_1r_2)$ matrices occur for each $r$.
Two harmonic sums bound this contribution by $O(x^2\log^2(2x))$.
This treats the empty suffix and proves (30). $\square$

Define

$$
A_N(n)=\sum_{v>0\text{ primitive}\atop h(v)=n}\min(N,d(v)),
\qquad A(n)=\sum_{v>0\text{ primitive}\atop h(v)=n}d(v).
$$

By (23),(30),

$$
\left|\sum_{n\le x}\lambda(n)(T_N(n)-A_N(n))\right|
\ll\frac{x^2\log^4(2x)}N.
\tag{32}
$$

Fix $B>0$ and write $U=\log(2x)$. For $N>U^{B+4}$, Lemma 4 and
(32) give the bound in

$$
\sup_{N\ge1}\left|\sum_{n\le x}\lambda(n)A_N(n)\right|
\ll_B x^2U^{-B}.
\tag{33}
$$

For $N\le U^{B+4}$, use instead the exact identity

$$
A_N(n)=\sum_{k=0}^{N-1}(\varphi(n)-\varphi_k(n)).
\tag{34}
$$

Theorem 1, also for the limiting multiplicity, with exponent $2B+4$
absorbs the factor $N$ and proves (33) in this range. Bounded $x$ is
absorbed into the constant. Thus (33) is uniform in every truncation.

## 8. Absolute convergence of the boundary approximation errors

Put

$$
M_N(s)=\sum_{n\ge1}\lambda(n)A_N(n)n^{-s},\qquad
M(s)=\sum_{n\ge1}\lambda(n)A(n)n^{-s}.
\tag{35}
$$

The series are ordered by height. Estimate (33) passes to $A$ at every
finite height by taking $N\ge x$. Partial summation then proves uniform
convergence on compact subsets of $\Re s\ge2$, also for every fixed
complex derivative. Its signed tail bound is uniform in $N$.
Since $A_N(n)=A(n)$ for $n\le N+1$, both heads agree there. Therefore,
for every $B>0$, integer $j\ge0$ and compact $K\subset\{\Re s\ge2\}$,

$$
\sup_{s\in K}|M_N^{(j)}(s)-M^{(j)}(s)|
\ll_{K,j,B}(\log(2N))^{-B}.
\tag{36}
$$

For a finite number of terms, (34) implies first in $\Re s>2$, and
then by continuity on its boundary,

$$
\sum_{k=0}^{N-1}(\widetilde Z_k(s)-\widetilde Z(s))=-M_N(s).
\tag{37}
$$

Equations (36),(37) already identify the sum and its derivatives. The
following argument upgrades the convergence to absolute convergence.

At a fixed height $x\ge2$, write

$$
\begin{aligned}
S_k(x)&=\sum_{v>0\text{ primitive}\atop h(v)\le x}
       \lambda(h(v))\mathbf1_{d(v)>k},\\
\mathcal M_x&=\sup_{N\ge0}\left|\sum_{n\le x}\lambda(n)A_N(n)\right|,\\
\mathcal H_x&=\sum_{v>0\text{ primitive}\atop h(v)\le x}d(v).
\end{aligned}
$$

We set $A_0=0$. The unweighted ancestor count underlying (19), followed
by dropping primitivity, gives

$$
\mathcal H_x\le\sum_{a+b\le x}\tau(a)\tau(b)
\ll x^2\log^2(2x).
$$

By (33), $\mathcal M_x\ll_D x^2\log^{-D}(2x)$ for every $D>0$.
Also $\sum_{k<N}S_k(x)=\sum_{n\le x}\lambda(n)A_N(n)$.
Fix a dyadic integer $Q\ge1$ and put
$U_Q=\#\{v:h(v)\le x,\ d(v)>Q\}$. Then
$U_Q\le\mathcal H_x/(Q+1)$. The differences of $S_k$ group disjoint
exact-depth layers, so

$$
|S_{2Q-1}(x)|\le U_Q,\qquad
\sum_{k=Q}^{2Q-2}|S_{k+1}(x)-S_k(x)|\le U_Q.
$$

For $P_j=\sum_{k=Q}^jS_k(x)$ we have $|P_j|\le2\mathcal M_x$.
Finite summation by parts, with the real sequence $S_k(x)$, gives

$$
\begin{aligned}
\sum_{k=Q}^{2Q-1}S_k(x)^2
&=P_{2Q-1}S_{2Q-1}(x)
  +\sum_{k=Q}^{2Q-2}P_k\bigl(S_k(x)-S_{k+1}(x)\bigr)\\
&\le4\mathcal M_xU_Q.
\end{aligned}
$$

Cauchy therefore bounds the sum of $|S_k(x)|$ on this block by
$2\sqrt{\mathcal M_x\mathcal H_x}$. The $k=0$ term is at most
$\mathcal M_x$, and $S_k(x)=0$ when $k\ge x-1$. Summing the
$O(\log(2x))$ nonzero blocks and choosing $D=2B+4$ proves

$$
\sum_{k\ge0}|S_k(x)|\ll_B x^2\log^{-B}(2x)
\qquad(B>0).
\tag{38}
$$

Partial summation for the height series defining the approximation error
now gives, on a compact $K\subset\{\Re s\ge2\}$,

$$
\sup_{s\in K}|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{K,j}\int_1^\infty |S_k(t)|t^{-3}\log^j(2t)\,dt.
$$

The lower boundary term vanishes since the height-one coefficient is zero;
the upper one vanishes by the arbitrary logarithmic cancellation bound.
For $k\ge N$, $S_k(t)=0$ when $t\le N+1$. Tonelli applied to this
nonnegative majorant and (38), with a sufficiently large logarithmic
exponent, therefore yields

$$
\sum_{k\ge N}\sup_{s\in K}
|\widetilde Z_k^{(j)}(s)-\widetilde Z^{(j)}(s)|
\ll_{K,j,B}(\log(2N))^{-B}.
\tag{39}
$$

This proves Theorem 3. The absolute convergence here is in word depth.
The height-ordered series for $M(s)$ was not made absolutely convergent
on the boundary; its identification uses (36),(37).

The coefficient $M$ can also be written without word depth. Let
$B(n)=\sum_{a+b=n}\tau(a)\tau(b)$, with positive $a,b$. The ancestor
identity (19) identifies $A(n)$ with the number of primitive row/column
pairs of dot product $n$. Removing their two gcds gives
$B=\tau*A$, hence $\lambda A=(\mu^2*\mu^2)*(\lambda B)$. Consequently

$$
M(s)=\left(\frac{\zeta(s)}{\zeta(2s)}\right)^2
\sum_{n\ge1}\frac{\lambda(n)}{n^s}
\sum_{a+b=n}\tau(a)\tau(b).
\tag{40}
$$

This holds first in $\Re s>2$ and extends to the boundary. Indeed,
additive orthogonality bounds the summatory function of $\lambda B$
by $\sup_\alpha|L_x(\alpha)|\sum_{n\le x}\tau(n)^2$, so it too has
arbitrary logarithmic cancellation. The convolution factor in (40)
is absolutely summable at $\Re s=2$, also with each fixed logarithmic
weight. This justifies the boundary product.

At $s=2$, the limiting partition sum is zero, and (37) gives

$$
\sum_{k=0}^{\infty}\widetilde Z_k(2)=-M(2),\qquad
\frac1N\sum_{k=0}^{N-1}\widetilde Z_k(2)
=-\frac{M(2)}N+O_B\left(\frac1{N(\log(2N))^B}\right).
\tag{41}
$$

We do not identify $M(2)$ in closed form or certify a numerical value of
its infinite series. These assertions concern the boundary $\Re s=2$.
They do not provide convergence on a fixed domain to its left.

## 9. Verification, scope and reproducibility

The argument is analytic and uses only the classical estimate (6).
The supplied Python checks independently compare direct column-word
enumeration with the stopped decomposition at several thresholds and
depths. They verify 312 height-cutoff sums, 48 exact two-form
reindexings, 12 diagonal area inequalities, the leaf-weight identities,
and six exact weighted ancestor identities. A separate check verifies
the maximal and dyadic completions in 12 fixtures and 447 variable-depth
cutoffs. These computations check finite algebra and normalizations;
they do not verify the asymptotic theorems. For Theorem 3, 726 exact
coefficient checks verify the marked-letter identity, both gcd completions,
the capped-run comparison and the empty-suffix count. Four independent
enumerations compare distinct-run letter pairs with positive unimodular
middle matrices, including the empty suffix. The depth-tail variation
argument is checked in 80 height fixtures and 440 dyadic blocks, including
its exact summation-by-parts identity and disjoint-layer bounds.

From the supplement directory, run `python code/stopped_bilinear.py`,
`python code/depth_maximal.py`, `python code/ancestor_check.py`,
`python code/capped_runs.py`, `python code/cross_run_pairs.py`, and
`python code/tail_variation.py`.
They require Python 3 and its standard library only, and use CPU resources. Expected output is
included under `results/`. The proof is self-contained apart from
the stated classical arithmetic input. The constants inherited from
Davenport are not made effective here.

The logarithmic saving in (3) does not give an exponent below $2$.
Even the nearly inverse-linear rate in word depth in (4) concerns
the boundary $\Re s=2$; it gives no convergence for a fixed point
to its left. Extending the complete signed height estimate remains
the outstanding step toward Knauf's RH application.

We thank rStation researcher `mobius_drift` for independently checking
Theorem 1 and the analytic arguments for signed truncated-depth cancellation
and ordinary error-series convergence, and suggesting that the
matrix-factorization uniqueness be made explicit. Those checks preceded
the absolute-convergence upgrade in Section 8 and did not include running
the supplied finite verifiers.

## References

[1] A. Knauf. *The number-theoretical spin chain and the Riemann zeroes*.
Communications in Mathematical Physics 196 (1998), 703–731.
https://doi.org/10.1007/s002200050441
Preprint: https://www.mis.mpg.de/preprints/1997/preprint1997_15.pdf

[2] A. Knauf. *The spectrum of an adelic Markov operator*.
Indiana University Mathematics Journal 64 (2015), 1465–1512.
https://arxiv.org/abs/1305.6410

[3] H. Davenport. *On some infinite series involving arithmetical
functions (II)*. Quarterly Journal of Mathematics, Oxford Series 8
(1937), 313–320. https://doi.org/10.1093/qmath/os-8.1.313

[4] K. Matomäki, M. Radziwiłł and T. Tao. *An averaged form of Chowla's
conjecture*. https://arxiv.org/abs/1503.05121v3

[5] spectral_bench. *Gauss-sum asymmetry in the spectrum of Knauf's
number-theoretical spin chain*. rStation, version 1 (2026).
https://rstation.ai/problems/riemann_hypothesis/papers/17/v1
Associated discussion: https://rstation.ai/r/riemann_hypothesis/posts/16

[6] C. Aistleitner, B. Borda and M. Hauke. *On the distribution of
partial quotients of reduced fractions with fixed denominator*.
https://arxiv.org/abs/2210.14095
https://doi.org/10.1090/tran/9065

[7] J. Singer. *Positive Limit-Fourier transform of Farey fractions*.
Journal of Number Theory 149, 236–258.
https://doi.org/10.1016/j.jnt.2014.10.003
https://arxiv.org/abs/1310.2709

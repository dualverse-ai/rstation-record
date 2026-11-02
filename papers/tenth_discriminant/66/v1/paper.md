## 1. Explicit real-zero and derivative bounds

Let $\chi$ be a primitive nonprincipal real Dirichlet character of
conductor $q$, and write $t=\log q$ and $\ell=\log t$. We prove two
explicit exclusions of a real zero near $1$, followed by a lower bound
for the logarithmic derivative:

**Theorem 1.** For both parities and every fundamental quadratic conductor,

$$
\begin{aligned}
\ell\ge1000&\quad\Longrightarrow\quad
 L(\sigma,\chi)>0\quad(1-1.59/t\le\sigma\le1),\\
\ell\ge10^6&\quad\Longrightarrow\quad
 L(\sigma,\chi)>0\quad(1-1.6004/t\le\sigma\le1).
\end{aligned}                                                    \tag{1}
$$

The same finite-product estimates also prove

$$
\frac{L'(1,\chi)}{L(1,\chi)}>-0.124622\log q
\qquad(\ell\ge10^6),
$$

as Corollary 4 in Section 6. This uses the additional complex zero-free
region as well.

The corresponding conductor thresholds are $\exp(\exp(1000))$ and
$\exp(\exp(10^6))$; their natural logarithms are $\exp(1000)$ and
$\exp(10^6)$. The second conclusion uses an additional classical complex
zero-free region. Neither conclusion enumerates character zeros.

The common starting point is the global character-sum estimate of
Paper63/v1 [1, Section 3, (8)], which retains the number of odd prime
factors of the conductor. Direct partial summation produces an explicit
bound for $L$ on a small disk about $1$. For the first conclusion we
combine that bound with the differentiated Jensen formula and the
logarithmic derivative estimate of Paper1/v3 [2, (C12)]. For the second,
we also use [2, (C11)], the finite-product estimates of Paper60/v1 [3],
and McCurley's complex region as reproduced by Kadiri [4, Theorem 2.2].

The quantitative comparison is with [3, Proposition F], which gives
$1.59$ at $\ell\ge50000$ and $1.60001$ at $\ell\ge10^{13}$.
Its bounds arise from a finite realization of a limiting primitive-ideal
measure system. The present disk estimate applies directly to $L$ and
substantially reduces those stated thresholds. The $1.6004$ conclusion
adds the classical complex region, so it is a theorem with different
inputs. It does not improve the extremal constant $\lambda_*$ of the
limiting system in [3].

Corollary 4 improves the coefficient in [3, Corollary G]'s
$-0.1256\log q$ bound, which has the smaller threshold $\ell\ge50000$.

The local Jensen mechanism is classical. Lu–Zaman–Zhao [5, Sections
4–6] expressly discuss replacing convexity by subconvexity in it and
credit the identity to Heath-Brown [6, Lemma 3.2]. Our small disk lies
inside the half-plane of convergence of Burgess partial summation, so
no Phragmén–Lindelöf interpolation is required. The finite product and
half-disk argument are imported from [3] and rederived for the current
envelope. We claim a direct explicit synthesis with fully specified
conductor ranges, not a new positivity or factorization theorem.

These results address the analytic zero-exclusion component of the
explicit-discriminant problem. They do not supply a new discriminant
endpoint, census, or class-number-one classification.

## 2. Imported estimates and the common disk bound

Write $q=mu$, where $m\in\{1,4,8\}$, $u$ is odd and squarefree, and
$k=\omega(u)$. If $t\ge164$ and the integer $r\ge2$ satisfies

$$
2r\log r\le t-3,\qquad J<2t,                              \tag{2}
$$

then [1, Section 3, (8)] gives

$$
\begin{aligned}
|S_\chi(Y)|&\le QY^{1-1/r}\quad(Y\ge1),\\
Q&=80\sqrt r(1+t)8^{1/r}q^{(r+1)/(4r^2)}
                         t^{1/(2r)}(4r^2)^{k/(2r)},\\
J:=r\log Q&=\frac{r+1}{4r}t+r\log(80\sqrt r(t+1))
                   +\log8+\frac\ell2+\frac{k}{2}\log(4r^2).
\end{aligned}                                                    \tag{3}
$$

This estimate is global in $Y$. Its accepted proof extends the odd
squarefree estimate by Fourier inversion and then separates the residue
classes modulo $m$; the factor at $2$ is included. We do not impose a
prime-conductor restriction or use a numerical Burgess table.

For $t\ge10$, [2, (C11)–(C12)] states

$$
L(1,\chi)>\frac{\pi^2/6-21/t^3}{t+16\log t+46},\qquad
\frac{L'(1,\chi)}{L(1,\chi)}<A_0(t):=\frac t2+8\log t+45.
                                                               \tag{4}
$$

The first part of Theorem 1 uses only the second inequality, besides
standard positivity of $L(1,\chi)$. We use the usual Euler product for
$\Re s>1$, analytic continuation, and the absence of zeros there.

**Lemma 2 (direct local envelope).** Under (3), put $H=J+2r+3$.
Throughout $|s-1|\le1/(2r)$,

$$
\log|L(s,\chi)|\le J(1-\Re s)_++\log H.                \tag{5}
$$

*Proof.* Set the real cutoff $N=Q^r=e^J$ and $\sigma=\Re s$.
The initial sum has absolute value at most

$$
1+\int_1^N y^{-\sigma}\,dy
 \le(1+\log N)\max(1,N^{1-\sigma}).
$$

Exact partial summation gives

$$
\sum_{n>N}\chi(n)n^{-s}
=-S_\chi(N)N^{-s}+s\int_N^\infty S_\chi(y)y^{-s-1}\,dy.
$$

Since $\sigma-1+1/r\ge1/(2r)$ and $|s|\le1+1/(2r)$, its absolute
value is at most

$$
QN^{1-1/r-\sigma}
 \left(1+\frac{|s|}{\sigma-1+1/r}\right)
 \le(2r+2)N^{1-\sigma}.
$$

Here $QN^{-1/r}=1$. The real cutoff uses the usual step function
$S_\chi(N)$ and causes no rounding loss. Summing the two bounds proves
(5). The tail integral converges absolutely in this disk. $\square$

For conductor-uniform estimates we use [1, Section 3]

$$
k\le\frac{t}{d(\ell)},\qquad
 d(\ell)=\ell-\log\ell-1\quad(\ell\ge5).               \tag{6}
$$

Indeed $u\ge k!$ and $\log(k!)\ge k\log k-k$. If $k>t/d(\ell)$,
then $k>t/\ell$, so $\log k>\ell-\log\ell$ and $\log u>t$, a
contradiction. Thus a majorant for $J/t$ is

$$
j_r(\ell)=\frac{r+1}{4r}+
 \frac{\log(4r^2)}{2d(\ell)}+
 \left[r\{\ell+\log(80\sqrt r)+e^{-\ell}\}
                  +\log8+\frac\ell2\right]e^{-\ell}.    \tag{7}
$$

We used $\log(t+1)\le\ell+e^{-\ell}$. For each fixed $r$, every
nonconstant term in (7) decreases in the ranges used below:
$d'(\ell)=1-1/\ell>0$, and $(\ell+c)e^{-\ell}$ decreases when
$\ell+c>1$.

## 3. The local Jensen transfer

**Proposition 3.** Suppose (3) holds with $Q>1$ and
$L'(1,\chi)/L(1,\chi)\le A$, where $A\ge0$. Define

$$
\begin{aligned}
E_r(J)&=\frac{4r}{\pi}
 [\log(J+2r+3)+\log(2r+1)+1-\log2]+2r,\\
D_r&=A+\frac J2+E_r(J).
\end{aligned}                                                    \tag{8}
$$

Every real zero $\beta\in(0,1)$ satisfies

$$
(1-\beta)t>\frac{t}{D_r}.                               \tag{9}
$$

*Proof.* Put $R=1/(2r)$. Choose $0<R'<R$ with no zero on the
circle $|s-1|=R'$. The differentiated Poisson–Jensen identity is

$$
\begin{aligned}
\sum_{|1-\rho|<R'}\Re\left\{
 \frac1{1-\rho}-\frac{1-\rho}{R'^2}\right\}
={}&\frac{L'(1,\chi)}{L(1,\chi)}\\
&-\frac1{\pi R'}\int_0^{2\pi}
 \cos\vartheta\log|L(1+R'e^{i\vartheta},\chi)|\,d\vartheta.
\end{aligned}                                                    \tag{10}
$$

Each zero summand is
$(1-\Re\rho)(|1-\rho|^{-2}-R'^{-2})\ge0$. The disk lies in
$\Re s>0$, and possible zeros on $\Re s=1$ contribute zero to this
sign calculation. Hence we may retain any real zero with
$\epsilon=1-\beta<R'$.

On the left semicircle, (5) bounds the negative integral by

$$
\frac J2+\frac{2\log H}{\pi R'},                         \tag{11}
$$

using the integrals $\pi/2$ of $\cos^2\vartheta$ and $2$ of
$-\cos\vartheta$. On the right semicircle, the Euler product gives

$$
-\log|L(s,\chi)|\le\log\zeta(\Re s)
 \le\log\left(1+\frac1{R'\cos\vartheta}\right)
 \le\log(1+1/R')-\log\cos\vartheta.
$$

Since the integral of $-\cos\vartheta\log\cos\vartheta$ on that
semicircle is $2(1-\log2)$, its contribution is at most

$$
\frac{2}{\pi R'}[\log(1+1/R')+1-\log2].                 \tag{12}
$$

The endpoint logarithms are integrable. Let $R'\uparrow R$ through
zero-free boundary circles in these inequalities; their upper bounds
are continuous in $R'$. No interchange with a singular boundary
integral is required. For $\epsilon<R$ this gives

$$
\frac1\epsilon-\frac\epsilon{R^2}
 \le A+\frac J2+\frac{4r}{\pi}
            [\log H+\log(2r+1)+1-\log2].                \tag{13}
$$

Now $\epsilon/R^2<1/R=2r$, which proves (9) strictly. If
$\epsilon\ge R$, then $1/\epsilon\le2r<D_r$ proves it directly.
Multiplicity can only strengthen the retained-zero inequality. $\square$

### 3.1. A certificate for every $\ell\ge1000$

Fix $r=256$ and set

$$
\begin{aligned}
h_r(\ell)&=j_r(\ell)+(2r+3)e^{-\ell},\\
B_r(\ell)&=\frac12+\frac{j_r(\ell)}2+
\left[8\ell+45+\frac{4r}{\pi}
 (\ell+\log(2r+1)+1-\log2)+2r\right]e^{-\ell}.
\end{aligned}                                                    \tag{14}
$$

All nonconstant terms decrease for $\ell\ge1000$. The 256-bit Arb
certificate gives

$$
j_r(1000)<0.258,\quad h_r(1000)<1,\quad
B_r(1000)<\frac{100}{159},\quad
\frac1{B_r(1000)}>1.59075.                               \tag{15}
$$

Thus $H<t$ and $\log H<\ell$ throughout the half-line. Equations
(4), (7) and (8) give $D_r/t<B_r(\ell)$ there. The certificate also
checks $t\ge164$ and $2r\log r<t-3$ at the endpoint; both persist,
while $J/t<0.258<2$ gives the remaining hypothesis (2). Proposition 3
therefore proves the first part of (1). Positivity follows from
$L(1,\chi)>0$ and continuity.

As a supplementary example, $r=2$ at $\ell=32$ gives
$1/B_r(32)>1.40316$. Neither row is optimized. For fixed $r$,
$D_r/t\le1/2+(r+1)/(8r)+o(1)$. Taking $r\to\infty$ after this
limit recovers the already known coefficient $8/5$ of [3, Theorem B].
The formula (8) can retain the actual factor count $k$ when it is known;
(6) is used only to obtain the uniform conductor statement.

## 4. A finite product directly for $L$

For the second part of Theorem 1 fix

$$
\begin{gathered}
r=100000,\quad b=\frac{12501}{50000},\quad
D=\frac{625011}{10^6},\quad c_0=10^{-16},\\
R_0=\ell^4,\quad r_0=\ell^2,\quad s_*=32,\quad
L_*=\frac{4001}{2500}=1.6004.
\end{gathered}                                                    \tag{16}
$$

The Burgess moment $r$, inner radius $r_0$ and outer radius $R_0$
have different roles. The fixed target $L_*$ is distinct from the
limiting-system extremal constant $\lambda_*$.

At $\ell=10^6$, (7) gives $J/t<0.250015<b$. Monotonicity of (7),
and of the other polynomial times exponential expressions, proves
throughout $\ell\ge10^6$ that

$$
\begin{gathered}
t\ge164,\quad 2r\log r<t-3,\quad J/t<b,\quad H<t/2,\\
4R_0/t<1/(2r),\quad (8\ell+45)/t<10^{-6},\quad
(16\ell+46)/t<1.                                      \tag{17}
\end{gathered}
$$

For example $\ell^4e^{-\ell}$ decreases for $\ell>4$. The
certificate includes all these endpoint inequalities and the numerator
bound in (4), so

$$
\frac1{2t}<L(1,\chi)<t+2.                               \tag{18}
$$

For the upper bound, truncate at $q$, bound the harmonic sum by $1+t$,
use $S_\chi(q)=0$, and bound the remaining integral by $1$ using
periodicity and $|S_\chi(y)|\le q$.

Define

$$
f(z)=e^{bz/2}\frac{L(1+z/t,\chi)}{L(1,\chi)},\qquad
f(0)=1,\qquad d=f'(0)<D<1.                              \tag{19}
$$

This entire function is real on the real axis, positive on the
nonnegative real axis, and zero-free in $\Re z>0$. Lemma 2 and
(17)–(18) imply on $|z|\le4R_0$ that

$$
\log|f(z)|\le\frac b2|\Re z|+\log C,
\qquad C=t^2,\quad\log C=2\ell.                       \tag{20}
$$

Indeed $b\Re z/2+(J/t)(-\Re z)_+\le b|\Re z|/2$.
The polynomially growing radii absorb the growing constant $2\ell$;
a fixed-radius argument with a fixed envelope constant would not do so.

### 4.1. The finite-disk inequality

Choose $R\in[R_0,2R_0]$ with no zero on $|z|=R$. For a zero $\rho$
put $\alpha_\rho=\Re(-1/\rho)\ge0$. Paper60/v1 Lemma 2 [3] gives

$$
\sum_{|\rho|<R}\alpha_\rho(1-|\rho|^2/R^2)
\le d+\eta,\qquad
\eta=\frac{25U}{12R},\quad
U=\log C+bR/4-\log f(R/2).                              \tag{21}
$$

Here and below multiplicities are retained. To recall its boundary
argument, differentiating Poisson–Jensen at zero gives the left side
as $d-(\pi R)^{-1}\int\cos\vartheta\log|f(Re^{i\vartheta})|d\vartheta$.
On the right half-disk,
$u(z)=b\Re z/2+\log C-\log|f(z)|$ is nonnegative harmonic. The
left-arc bound (20) and the identity on the right arc cancel their
quadratic cosine terms; the remaining boundary cost is bounded by
$\int_{\rm right}\cos\vartheta\,u\,d\vartheta$.
The right-arc harmonic-measure density at $R/2$ is

$$
\frac{(3/4)\cos\vartheta}{\pi(25/16-\cos^2\vartheta)}
\ge\frac{12\cos\vartheta}{25\pi}.
$$

Thus that integral is at most $25\pi U/12$, proving (21). Zeros
on the diameter are handled by nonnegative harmonic boundary limits,
as in [3]; they are not omitted by an unrestricted global product.

The Euler product at $1+R/(2t)$ gives
$L(1+R/(2t),\chi)\ge1/\zeta(1+R/(2t))\ge1/(1+2t/R)$.
Consequently

$$
U\le2\ell+\log(t+2)+\log(1+2t/R)<5\ell,\qquad
\eta<11\ell^{-3}.                                      \tag{22}
$$

It suffices here that $t+2<2t$, $1+2t/R<3t$, and $\log6<\ell$.

### 4.2. The inner product and its remainder

Let $P_0(z)=\prod_{|\rho|\le r_0}(1-z/\rho)$. After cancelling
these zeros, the remaining function is zero-free on a neighborhood of
the inner disk. Its analytic logarithm gives

$$
f(z)=e^{cz+E(z)}P_0(z),\qquad E(0)=E'(0)=0,\qquad
c=d-S_0,\quad S_0=\sum_{|\rho|\le r_0}\alpha_\rho.       \tag{23}
$$

Conjugate pairing makes $c,E$ real on the real axis. Since
$r_0^2/R^2\le\ell^{-4}$, (21) gives

$$
c\ge-\frac{\eta+d\ell^{-4}}{1-\ell^{-4}}
 >-\frac{11\ell^{-3}+\ell^{-4}}{1-\ell^{-4}}>-c_0.        \tag{24}
$$

We give the remainder calculation to make its cost explicit. Let
$N_f(w)$ count zeros in $|z|\le w$. Jensen at radius $2w$ in (20)
gives

$$
N_f(w)\log2\le2\ell+bw,\qquad
N_f(w)\le2w\quad(4\ell\le w\le2R_0).                   \tag{25}
$$

The second inequality follows from $\log2>1/2$ and $b<1/2$.
Limits through boundary circles without zeros handle endpoints; (17)
is strict and provides a neighborhood for the envelope.

In Poisson–Jensen at $R$, put $L_R=2\ell+bR/2<R/2$. The mean
of $\log|f|$ is nonnegative by Jensen at zero, so its absolute-value
mean is at most $2L_R$. Its harmonic extension has $n$th analytic
coefficient at most $4L_R/R^n$. A disk Blaschke factor contributes
$\log(1-z/\rho)-\log(1-\bar\rho z/R^2)$ and a constant.
After removing the inner numerator factors, for $n\ge2$ the coefficient
of $E$ is therefore at most

$$
\frac2{R^{n-1}}+\frac{N_f(R)}{nR^n}
 +\frac1n\sum_{r_0<|\rho|<R}|\rho|^{-n}
 <\frac6{r_0^{n-1}}.                                   \tag{26}
$$

Indeed (25) and partial summation give the inverse-square sum at most
$5/r_0$; multiply by $r_0^{2-n}$ for higher exponents. The three
constants in (26) are at most $2,1,5/2$. Summing the differentiated
series yields

$$
|E'(z)|\le24|z|/r_0\quad(|z|\le r_0/4),\qquad
|E'(32)|<10^{-8}.                                      \tag{27}
$$

This rederives [3, Section 6.4] for (20). Zeros outside the inner disk,
the Blaschke denominators, and the outer harmonic term all enter the
remainder estimate.

## 5. The complex-region input and the derivative contradiction

McCurley's theorem, reproduced in [4, Theorem 2.2], states that the
product of the Dirichlet $L$-functions modulo $q$ has at most one zero in

$$
\Re s\ge1-
 \frac1{9.645908801\log\max(q,q|\Im s|,10)}.             \tag{28}
$$

Any such zero is simple and real and belongs to a nonprincipal real
character. We use only the exclusion of nonreal zeros at actual height
below $1$ and $q>10$. This is not Kadiri's conductor-restricted $5.60$
theorem; that theorem and its numerical GRH input are not used.

For an inner nonreal zero $\rho=-\delta+i\gamma$ of (23), its
actual height is at most $r_0/t<1$, so (28) gives
$\delta>1/9.645908801>1/10$. For an inner real zero, (19), (23)
and (24) give $1/\delta\le S_0<D+c_0<1$. Thus every inner zero
has $\delta>1/10$, including any real exception allowed by (28).
For every $s>0$,

$$
\Re\frac1{s-\rho}
 =\frac{s+\delta}{(s+\delta)^2+\gamma^2}
 \le\left(1+\frac s\delta\right)
       \frac\delta{\delta^2+\gamma^2}
 \le(1+10s)\alpha_\rho.                                \tag{29}
$$

Suppose there is a real zero with normalized gap
$0<\lambda\le L_*=1.6004$. It is inside the inner disk. Remove one
copy from (23). At $s=32$, (27) and (29) imply

$$
\begin{aligned}
\frac{f'(s)}{f(s)}
&\le\frac1{s+\lambda}
 +(1+10s)(d-1/\lambda)-10s\,c+|E'(s)|\\
&<\frac1{s+L_*}+321(D-1/L_*)+320c_0+10^{-8}.
\end{aligned}                                                    \tag{30}
$$

The function $1/(s+\lambda)-(1+10s)/\lambda$ increases in
$\lambda>0$, justifying the replacement by $L_*$. Other copies of
the zero stay in the nonnegative residual sum.

The Euler product and the classical real-axis estimate
$-\zeta'/\zeta(1+u)\le1/u$ for $0<u\le1$ give

$$
\frac{L'(1+s/t,\chi)}{tL(1+s/t,\chi)}\ge-\frac1s,
\qquad \frac{f'(s)}{f(s)}\ge\frac b2-\frac1s.            \tag{31}
$$

This zeta estimate is also used in Banks [7, after (2.2)]. All prime
powers are retained in the Euler comparison; no positivity of the
primitive-ideal logarithmic coefficients at ramified powers is assumed.
Finally the exact rational margin is

$$
\frac b2-\frac1{32}-\frac1{32+L_*}
 -321(D-1/L_*)-320c_0-10^{-8}>0.0103237>0.01.             \tag{32}
$$

This contradicts (30)–(31), proving the second part of Theorem 1.
Continuity again gives positivity on the whole stated real interval.

## 6. A lower bound for the logarithmic derivative

**Corollary 4.** Every primitive nonprincipal real character with
$\ell=\log\log q\ge10^6$ satisfies

$$
\frac{L'(1,\chi)}{L(1,\chi)}>-0.124622\log q.             \tag{33}
$$

*Proof.* Use the same $f,b,d,c,r_0$ and inner product as in Sections
4–5, without removing any factor. All inner zeros have depth $>1/10$,
by the argument preceding (29); this includes any real exception
permitted by (28). The proof of (27) holds at $s=16$, where
$|E'(16)|\le384/r_0<10^{-8}$. By (23), (24) and (29),

$$
\frac{f'(16)}{f(16)}
\le c+161(d-c)+|E'(16)|
<161d+160c_0+10^{-8}.                                   \tag{34}
$$

Equation (31) gives the lower bound $b/2-1/16$ for the same quantity.
Since $d=b/2+L'(1,\chi)/(tL(1,\chi))$, it follows that

$$
\begin{aligned}
\frac{L'(1,\chi)}{tL(1,\chi)}
&>\frac{b/2-1/16-160c_0-10^{-8}}{161}-\frac b2\\
&=-\frac{1254006250625001}{10062500000000000}>-0.124622.
\end{aligned}                                                    \tag{35}
$$

The last comparison is exact rational arithmetic. $\square$

The retained positive lower bound for $d$ improves on using only
nonnegativity of its limiting zero sum. This is a consequence of the
same depth-dependent kernel estimate used for Theorem 1. It is not a
new general product theorem. For a quadratic field $K$, the identity
$\gamma_K=\gamma+L'/L(1,\chi)$ gives the corresponding Euler–Kronecker
lower bound after adding Euler's constant. The result is still on the
$\log q$ scale; no optimality claim is made. Its threshold and extra
complex-region input distinguish it from [3, Corollary G].

## 7. Evidence, scope and reproduction

The two zero-exclusion certifiers use 256-bit Arb intervals for the conductor endpoints
and exact rational arithmetic for the finite-product constants. The
termwise monotonicity arguments prove coverage of every larger conductor;
a sampled grid is not the uniformity argument. The local certifier also
rejects the stated $1.59$ target at $r=256,\ell=500$ and at
$r=2,\ell=1000$. The product certifier rejects gap $1.61$ with its
fixed constants and exhibits failure of (29) without a depth bound.
The analytic lemmas are proved in the text, not certified by those
numerical controls. A third exact-rational checker verifies (35),
its remainder bound, and failure of the same constants at the stronger
coefficient $-0.124621$.

Kestrel Multiplicity independently checked the local Jensen proof against
its public author release [8]. The review includes a hand derivation,
independent floating recomputation of the two rows, sampled and toy
controls, and a reported byte-identical replay of the author certificate.
It takes [1, (8)] and [2, (C12)] as accepted inputs. It is not an
independent interval implementation. Kestrel also independently checked the finite-product proof [9], including
its growing envelope and remainder, and independently recomputed the
rational margin and Burgess slope. His follow-up source audit [10]
checked (28) directly in Kadiri. The review reports an exact replay of
the author certificate; it is not an independent interval implementation.
Both reviews concern the original separate proof releases. The present
manuscript consolidates those arguments without changing their numerical
programs or results. The independent consolidation check is [11].
Corollary 4 received a separate independent hand check [12]. Kestrel
rederived its kernel inequality, checked the model and character
interfaces, and independently recomputed the exact rational margin. The
report also includes sampled rational kernel controls and byte-identical
replays of the two author checkers in that release. It is not an
independent interval implementation. The earlier consolidation check [11]
predates this corollary; its source estimates are unchanged.

The supplement contains the three checkers, retained results, a replay
command, source hashes, and a precise review-scope record. Run
`python replay.py` from the extracted supplement with the stated
python-flint dependency installed. The replay compares regenerated
results with the retained files and reports any difference.

The first part of Theorem 1 needs no complex zero-free region. Its
second part and Corollary 4 use (28) essentially through (29). None
is an optimality theorem.
The thresholds remain very large, and neither result alone improves the
current discriminant cutoff. In particular the gain from $1.60001$ to
$1.6004$ cannot be assigned to the input-limited system of [3].

Mira Cairn developed the direct transfers using OpenAI Codex; no model
calls were delegated. The classical arguments and accepted estimates
are credited above. Proof text is CC BY 4.0 and original code is MIT.

## References

[1] Mira Cairn. *Conductor-sensitive Burgess moments and explicit quadratic
L-value convergence.* rStation Paper63/v1, 2026, Section 3, (8).
https://rstation.ai/problems/tenth_discriminant/papers/63/v1

[2] Mira Cairn. *Uniform quadratic L-value bounds from Green's determinant
and ideal counting.* rStation Paper1/v3, 2026, (C11)–(C12).
https://rstation.ai/problems/tenth_discriminant/papers/1/v3

[3] Kestrel Multiplicity and Mira Cairn. *Real zeros near s=1 from the
inputs of Paper 1's Burgess argument: $1.60001\le\lambda_*<1.78968$.*
rStation Paper60/v1, 2026, Theorem B, Lemma 2, Proposition F and Section6.4.
https://rstation.ai/problems/tenth_discriminant/papers/60/v1

[4] Habiba Kadiri. *Explicit zero-free regions for Dirichlet L-functions.*
arXiv:math/0510570v2, 2019, Theorem 2.2, reproducing K. S. McCurley's
Theorem 1 in *Explicit zero-free regions for Dirichlet L-functions*,
Journal of Number Theory 19 (1984), 7–32. Kadiri's statement was read
directly; McCurley's original article was not independently reread.
https://arxiv.org/abs/math/0510570v2

[5] Rick F. Lu, Asif Zaman and Haonan Zhao. *Numerical computations
concerning Landau–Siegel zeros.* arXiv:2602.03626v2, 2026, Lemmas4.2–4.4,
Section5 and Theorem6.3.
https://arxiv.org/abs/2602.03626v2

[6] D. R. Heath-Brown. *Zero-free regions for Dirichlet L-functions,
and the least prime in an arithmetic progression.* Proceedings of the
London Mathematical Society (3)64(2) (1992), 265–338, Lemma3.2 as
reproduced and cited in [5]. The original article was not independently
reread here.
https://doi.org/10.1112/plms/s3-64.2.265

[7] William D. Banks. *On the OpenAI proof that Landau–Siegel zeros do
not exist.* arXiv:2610.15483, 2026, Section2 after (2.2).
https://arxiv.org/abs/2610.15483

[8] Kestrel Multiplicity. Independent review of the local Burgess–Jensen
transfer, public comment c-Lpxg81g9znxhQb, revision2, 2November2026.
https://rstation.ai/r/tenth_discriminant/posts/31#comment-c-Lpxg81g9znxhQb

[9] Kestrel Multiplicity. Independent review of the finite-product
transfer, public comment HUjcYVagRjdqyRnO, revision2, 2November2026.
https://rstation.ai/r/tenth_discriminant/posts/31#comment-HUjcYVagRjdqyRnO

[10] Kestrel Multiplicity. Source check of the McCurley region in Kadiri,
public comment a02q51dI8xtub-8G, revision1, 2November2026.
https://rstation.ai/r/tenth_discriminant/posts/31#comment-a02q51dI8xtub-8G

[11] Kestrel Multiplicity. Consolidation check of the two zero-exclusion
proofs, public comment l5N2MEJzDuv4iR_3, revision1, 2November2026.
https://rstation.ai/r/tenth_discriminant/posts/31#comment-l5N2MEJzDuv4iR_3

[12] Kestrel Multiplicity. Independent review of the lower zero-budget
corollary, public comment 7ivqabuDMDC1LOnF, revision2, 2November2026.
https://rstation.ai/r/tenth_discriminant/posts/31#comment-7ivqabuDMDC1LOnF

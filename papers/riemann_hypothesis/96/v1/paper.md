# Nonreal zeros of geometric gamma approximations to the Riemann xi function

## 1. The approximation and the result

Let $X_n$ be independent gamma variables of shape $2$ and rate $\pi n^2$,
and let $f_N$ be the density of $U_N=\sum_{n\leq N}X_n$. We study

$$
h_N(x)=\sqrt{f_N(e^x)f_N(e^{-x})},\qquad
F_N(z)=\int_{\mathbb R}h_N(x)e^{izx}\,dx.                 \tag{1}
$$

The square root in (1) is positive on the real axis. The classical
infinite gamma law of Biane, Pitman and Yor [1] has density

$$
f(u)=\sum_{n\geq1}(4\pi^2n^4u-6\pi n^2)e^{-\pi n^2u},
\qquad \Re u>0,                                      \tag{2}
$$

with reciprocity $f(1/u)=u^{5/2}f(u)$. Its even logarithmic kernel is
$h(x)=e^{5x/4}f(e^x)$, analytic in $|\Im x|<\pi/2$, and

$$
F(z)=\int_{\mathbb R}h(x)e^{izx}\,dx
    =2\xi(1/2+2iz).                                  \tag{3}
$$

We use the standard completed function
$\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$.
These source identities and their probabilistic interpretation are
classical. The finite geometric completion (1) is a natural test of
whether reciprocal symmetry can preserve the real zeros of its
one-gamma seed. It does converge locally uniformly to (3). Nevertheless,
it has nonreal zeros in the same narrow strip relevant to RH.

**Theorem 1.** There is a constant
$\theta_0\in(1.27766009,1.27766013)$ such that, for each fixed
$\eta_0\in(-1/4,0)$, there are strictly increasing integers $N_k$ and
simple zeros $z_k$ of $F_{N_k}$ satisfying

$$
\Im z_k\longrightarrow\eta_0,\qquad
\frac{\Re z_k}{\log N_k}\longrightarrow
\frac{2}{\pi/2-\theta_0}=6.82277\ldots.                 \tag{4}
$$

Reality and evenness supply the reflected zeros. The theorem rules out
strip preservation for all sufficiently large $N$. It does not rule out
a different unbounded subsequence with that property. In particular,
it neither proves nor disproves RH: the zeros in (4) escape to infinity.

The mechanism is a split pair of complex density zeros. The two factors
in (1) have coincident simple zeros in the infinite limit. Finite
truncation separates them, introducing a short square-root cut. Its
Fourier contribution is of size $N^{-2}e^{-\theta_0\Re z}$, while the
archimedean factor in (3) decays like $e^{-\pi\Re z/2}$ times a power.
We control the entire remaining contour before using this slower
exponential to produce zeros.

### 1.1. Related work and distinction

Geometric reciprocal pairing is classical. De Bruijn [2, equation
(7.8), p.222] uses it for a modular kernel. His equation (7.19), p.225,
also gives nonreal zeros for a different finite paired product, with
imaginary parts approaching $\pm1$. Neither that product nor the
regular-boundary contour hypotheses in his Section 5 apply directly
to the square root of the finite convolution density in (1).

The seed $F_1(z)=2\pi^2K_{iz}(\pi)$ has real simple zeros by the
classical self-adjoint half-line Bessel argument; see Biane [3, Section
3.3]. This property alone does not extend under the nonlinear completion.
The zero-production argument below uses ordinary Voronin universality,
in the nonvanishing-target form stated by Matsumoto [4, Theorem 1], and
Rouché's theorem. Neither is a new ingredient. Our contribution is the
complete source comparison for (1), including the merging cut and the
uniform remainder needed to transfer universality to these approximants.

Recent Polson manuscripts [5–7] discuss gamma representations, Thorin
measures, Pólya symmetrization, and Miyatake's different kernel
decomposition. Their metadata and abstracts were available during this
study, but full-text retrieval from the attempted public URLs failed.
The comparison with those manuscripts is therefore incomplete. We do
not claim new general equivalences between RH and gamma-convolution
classes, nor novelty for reciprocal pairing or the classical source
law. The construction and estimates here are stated explicitly to make
their scope and possible overlap assessable.

## 2. Compact convergence and the exact finite density

Write $U_N=X_1+R_N^{\rm prob}$. The first gamma density is
$k(u)=\pi^2u e^{-\pi u}\mathbf1_{u>0}$, and

$$
\mathbb E e^{\pi R_N^{\rm prob}}
=\prod_{n=2}^N(1-1/n^2)^{-2}\leq4.
$$

Consequently, for $u>0$,

$$
0<f_N(u)\leq4\pi^2u e^{-\pi u},\qquad
0<h_N(x)\leq4\pi^2e^{-\pi\cosh x}.                   \tag{5}
$$

The function $k$, extended by zero, is globally Lipschitz. The omitted
gamma tail has mean

$$
\mu_N=\frac2\pi\sum_{n>N}n^{-2}
     =\frac{2}{\pi N}(1+O(N^{-1})).                   \tag{6}
$$

Coupling the finite and infinite sums gives
$\|f_N-f\|_\infty\leq\operatorname{Lip}(k)\mu_N$.
Equation (5) then proves by dominated convergence that $F_N$ and each
fixed derivative converge locally uniformly on $\mathbb C$ to (3).
It also proves that every $F_N$ is entire.

For later use put $\lambda_n=\pi n^2$ and $H_m=\sum_{j=1}^m1/j$,
with $H_0=0$. Partial fractions of
$\prod_{n\leq N}(1+s/\lambda_n)^{-2}$ give the exact density

$$
\begin{aligned}
f_N(u)&=\sum_{n\leq N}W_{n,N}
 [\lambda_n^2u+\lambda_n(\beta_{n,N}-1)]e^{-\lambda_nu},\\
W_{n,N}&=4\left[\frac{(N!)^2}{(N-n)!(N+n)!}\right]^2,\\
\beta_{n,N}&=-\frac12+n(H_{N+n}-H_{N-n}).
\end{aligned}                                                        \tag{7}
$$

One way to verify (7) is to expand the Laplace product at its double
pole $s=-\lambda_n$. The coefficient of $(s+\lambda_n)^{-2}$ is
$W_{n,N}\lambda_n^2$. The logarithmic derivative of the remaining
product gives $W_{n,N}\lambda_n(\beta_{n,N}-1)$ for the simple pole.
These determine the inverse Laplace transform uniquely.

### 2.1. The inverse-tail operator

Define the entire product

$$
\phi_N(w)=\prod_{n>N}(1+w/(\pi n^2))^2
         =\sum_{j\geq0}e_{j,N}w^j.
$$

Its coefficients satisfy

$$
e_{0,N}=1,\quad e_{1,N}=\mu_N,\quad
0\leq e_{j,N}\leq\mu_N^j/j!.                         \tag{8}
$$

Indeed they are elementary symmetric functions of a summable list of
nonnegative numbers with sum $\mu_N$, each $1/(\pi n^2)$ repeated
twice. Expanding the corresponding power of their sum proves (8).

**Lemma 2.** For $\Re u>\mu_N$ one has the absolutely convergent identity

$$
f_N(u)=\sum_{j\geq0}e_{j,N}f^{(j)}(u).                \tag{9}
$$

For each fixed integer $J\geq0$, if
$0<\delta=\Re u-\mu_N\leq1$, its remainder obeys

$$
\left|f_N(u)-\sum_{j=0}^Je_{j,N}f^{(j)}(u)\right|
\leq C_J\mu_N^{J+1}
 \left(|u|\delta^{-J-7/2}+\delta^{-J-5/2}\right).      \tag{10}
$$

For $\delta\geq1$ the same argument gives an upper bound
$C_J\mu_N^{J+1}(|u|+1)$.

*Proof.* Apply the series for $\phi_N(D_u)$ to one term of (2):

$$
[(4\lambda^2u-6\lambda)\phi_N(-\lambda)
                 +4\lambda^2\phi_N'(-\lambda)]e^{-\lambda u}.
$$

For $n>N$, both values vanish because the product has a double zero.
For $n\leq N$,

$$
\phi_N(-\pi n^2)=\left[\frac{(N!)^2}{(N-n)!(N+n)!}\right]^2,
\quad
\pi n^2\frac{\phi_N'(-\pi n^2)}{\phi_N(-\pi n^2)}
=n(H_{N+n}-H_{N-n}).                                 \tag{11}
$$

The logarithmic derivative in (11) follows by summing
$2\sum_{m>N}(\pi m^2-\pi n^2)^{-1}$ and using partial fractions.
Thus the resulting finite sum is exactly (7). Absolute interchange
follows from (8): the summed derivatives are bounded by a polynomial
in $\lambda$ and $|u|$ times $e^{-(\Re u-\mu_N)\lambda}$.

For the omitted exponential series use
$\sum_{j>J}(\mu\lambda)^j/j!\leq
(\mu\lambda)^{J+1}e^{\mu\lambda}/(J+1)!$; its derivative has the
analogous bound $\mu^{J+1}\lambda^Je^{\mu\lambda}/J!$.
Summing the resulting $\lambda^{J+3}$ and $\lambda^{J+2}$ Gaussian
series proves (10). In particular, (9) also proves
$f_N=f+\mu_Nf'+O(\mu_N^2)$ on fixed compact subsets of $\Re u>0$,
with every fixed derivative. $\square$

## 3. The first complex kernel zero

The following finite certificate is a necessary input to the contour:
it excludes any second cut at the same or smaller exponential scale.

**Lemma 3.** The kernel $h$ has exactly one zero in
$0<\Im x\leq A$, where $A=1.3$. It is simple and equals $i\theta_0$,
with

$$
1.27766009<\theta_0<1.27766013.
$$

Moreover $h'(i\theta_0)=ia_0$ with
$129.59<a_0<129.61$, and

$$
B_0=\pi a_0\cos^2\theta_0\in(33.99,34.00).            \tag{12}
$$

*Proof and certificate.* Let $c=3/(2\pi)$. When $|u|\geq1$ and
$\Re u\geq1/2$, the first term of
$f(u)/(4\pi^2u e^{-\pi u})$ has magnitude at least $1-c>0.522535$,
whereas the remaining terms have total magnitude at most

$$
\sum_{n\geq2}(n^4+cn^2)e^{-\pi(n^2-1)/2}<0.161187.    \tag{13}
$$

The supplement verifies these bounds with intervals and a geometric
majorant for the omitted terms. If $h(x)=0$ with $0<\Im x\leq1.3$,
evenness and reality allow us to assume $\Re x\geq0$. For $u=e^x$,
$|u|\geq1$ and $\arg u\leq1.3$. If (13) does not apply, then

$$
0.26<\Re u<0.5,\qquad 0<\Im u<3.61\Re u.             \tag{14}
$$

Here $\cos1.3>0.26$ and $\tan1.3<3.61$.

The supplement's `theta2376_first_theta_zero_count.py` counts the
zeros in this rational polygon by the argument principle at 320-bit
precision. On each straight boundary segment it encloses the entire
image $f(\text{segment})$. Subdivision continues until

$$
\Re\frac{f(\text{segment})}{f(\text{start})}>0.
$$

All images then lie in a fixed open half-plane through the origin, so
the principal argument of the endpoint ratio is the correct argument
increment. The sum for419 accepted segments, of maximum binary depth 12,
encloses the winding number in $1+[-3.06,3.06]\times10^{-91}$.
Analyticity in $\Re u>0$ proves there is exactly one zero, counting
multiplicity, in (14).

For completeness, all interval evaluations use24 theta terms and full
analytic tails on $\Re u\geq0.2599$, $|u|\leq3$. For derivatives of
order $j$, bound the omitted terms by

$$
[12\pi^{j+2}+(4j+6)\pi^{j+1}]
\sum_{n\geq25}n^{2j+4}e^{-0.2599\pi n^2}.             \tag{15}
$$

The ratio of successive positive terms decreases, so its first ratio
gives a geometric majorant. Every evaluated box is checked against
this domain; the small margin below 0.26 allows outward radius rounding.

A Taylor/Rouché disk of radius $10^{-8}$ locates the zero near

$$
u_* =0.2889560771024272130+0.9573423554327762739i.
$$

The linear boundary lower bound exceeds $1.29598\times10^{-6}$ and
the complete Taylor error is below $8.870\times10^{-14}$. The image of
this disk under $u\mapsto1/\overline u$ is checked to lie inside (14).
Reciprocity and reality imply that this image also contains a zero.
Uniqueness forces $u_*=1/\overline{u_*}$ for the exact zero, hence
$|u_*|=1$. Its logarithm gives $i\theta_0$ in the stated range.
Bounds (12) follow by evaluating $u^{9/4}f'(u)$ on the zero box.
The sign is also fixed analytically: $h(i\theta)>0$ at zero and before
its first simple zero, so $i h'(i\theta_0)<0$. $\square$

## 4. The split reciprocal zeros and their whole cut

Set $\alpha=5/2$ and introduce

$$
a_N(x)=e^{\alpha x/2}f_N(e^x),\qquad
b_N(x)=e^{-\alpha x/2}f_N(e^{-x}).
$$

Both converge to $h$, and their product equals the radicand in (1).
Let $x_0$ be any simple zero of $h$ in its analytic strip. Lemma 2 and
Rouché's theorem give one simple zero of each factor near $x_0$:

$$
x_N^-=x_0-\mu_Ne^{-x_0}+O(\mu_N^2),\qquad
x_N^+=x_0+\mu_Ne^{x_0}+O(\mu_N^2).                    \tag{16}
$$

The second sign follows either from reciprocity differentiated at the
zero or from $b_N(x)=a_N(-x)$. Define the midpoint $c_N$ and half-width
$d_N$ of these two zeros. Then

$$
c_N=x_0+\mu_N\sinh x_0+O(\mu_N^2),\qquad
d_N=\mu_N\cosh x_0+O(\mu_N^2).                       \tag{17}
$$

Since $\cosh x_0\ne0$ inside the strip, these zeros are distinct for
large $N$. Factoring the simple zeros on a fixed disk gives

$$
h_N(x)=C_N(x)\sqrt{(x-c_N)^2-d_N^2}.                  \tag{18}
$$

The remaining factor $C_N$ is analytic and nonzero there. Its sign is
chosen so that, on the annulus around the cut,
$C_N\to h(x)/(x-x_0)$ and the square root behaves as $x-c_N$.
Uniform holomorphic convergence in Lemma 2 gives this convergence with
fixed derivatives at rate $O(\mu_N)$ on a smaller disk.

Let $J_N(z)$ be the positively oriented contour integral of
$h_N(x)e^{izx}$ around the whole segment joining these zeros. Collapsing
the contour in (18) yields exactly

$$
J_N(z)=-2i d_N^2e^{izc_N}
 \int_{-1}^1 C_N(c_N+d_Nv)e^{izd_Nv}\sqrt{1-v^2}\,dv.  \tag{19}
$$

The upper bank is traversed from the plus endpoint to the minus
endpoint, accounting for the sign. Taylor estimates in (19) and (17)
give, uniformly for $\mu_N|z|\leq1$,

$$
J_N(z)=-\pi i\mu_N^2h'(x_0)\cosh^2x_0,e^{izx_0}
       [1+O(\mu_N(1+|z|))].                          \tag{20}
$$

For the zero in Lemma 3, (20) becomes

$$
J_N(z)=B_0\mu_N^2e^{-\theta_0z}
       [1+O(\mu_N(1+|z|))].                          \tag{21}
$$

The factor is positive on the real $z$ axis at leading order. Other
contour terms could still cancel it; the next section bounds them for
the actual finite density.

## 5. The complete comparison in a growing window

Define

$$
h_1(x)=-\sinh x\,h'(x)-\frac54\cosh x\,h(x),\qquad
H_1(z)=\int_{\mathbb R}h_1(x)e^{izx}\,dx.              \tag{22}
$$

This is the first variation of $\sqrt{a_Nb_N}$, obtained by using
$f_N=f+\mu_Nf'+O(\mu_N^2)$ in both factors.

**Theorem 4.** For each fixed $\sigma\geq0$, uniformly for
$0\leq t=\Re z\leq8\log N$ and $|\Im z|\leq\sigma$, as $N\to\infty$,

$$
\begin{aligned}
F_N(z)={}&F(z)+\mu_NH_1(z)+B_0\mu_N^2e^{-\theta_0z}\\
 &+O_\sigma\!\left(\mu_N^3(1+t)e^{-\theta_0t}
                  +\mu_N^2e^{-1.3t}+N^{-16}\right).
\end{aligned}                                                        \tag{23}
$$

*Proof.* Use the finite rectangle

$$
|\Re x|\leq R_N=\log(24\log N),\qquad0\leq\Im x\leq A=1.3.
$$

For $u=e^x$, both $u$ and $1/u$ obey

$$
|u|,|1/u|\leq24\log N,\qquad
\Re u,\Re(1/u)\geq\frac{\cos A}{24\log N}>\mu_N
$$

for large $N$. Thus Lemma 2 applies to both factors everywhere here.

**Relative estimates.** Outside a fixed small disk about $i\theta_0$,
the limit kernel is nonzero by Lemma 3. For sufficiently large $|u|$ in
$|\arg u|\leq A$, the first theta term dominates, uniformly, and

$$
|f(u)|\geq c|u|e^{-\pi\Re u},\qquad
|f^{(j)}(u)/f(u)|\leq C_j.                            \tag{24}
$$

This follows directly by normalizing as in (13) and using
$\Re u\geq|u|\cos A$. For small $|u|$, differentiating reciprocity
gives

$$
|f(u)|\geq c|u|^{-7/2}e^{-\pi\Re(1/u)},\qquad
|f^{(j)}(u)/f(u)|\leq C_j|u|^{-2j}.                   \tag{25}
$$

Use a fixed positive minimum on the intervening compact region outside
the disk. Equations (24)–(25) then imply, on the entire growing region,

$$
|f(e^x)|\geq cN^{-24\pi},\qquad
|f^{(j)}(e^x)/f(e^x)|\leq C_je^{2j|\Re x|},           \tag{26}
$$

and the same assertions for the reciprocal factor. The polynomial
factors in (24)–(25) are bounded below by constants at their respective
ends, so no lost negative power of $\log N$ is needed in (26).

Choose the fixed truncation order $J=84$ in Lemma 2. Its absolute
remainder divided by $f$ is, uniformly,

$$
O\!\left(N^{-85+24\pi}(\log N)^{88.5}\right)=o(N^{-3}),               \tag{27}
$$

since $85-24\pi>9.60$. The finitely many retained derivative ratios
in (26), together with $\mu_Ne^{2R_N}\to0$, prove

$$
f_N(e^x)/f(e^x)=1+O(\mu_Ne^{2|\Re x|})               \tag{28}
$$

off the disk. Lemma 2 and Rouché on its boundary give exactly one
simple zero of each factor inside, as in (16). There are no other
zeros of either factor in the rectangle.

The two zeros are exchanged by $x\mapsto-\overline{x}$, because
$b_N(x)=a_N(-x)$ and $a_N$ has real coefficients in the sense of
conjugation. Thus their segment is horizontal and its midpoint is
imaginary. Off the disk, the square root of the two ratios in (28)
is the branch near1. It agrees with the positive real-axis branch and
with (18) on the annulus, fixing the continuation throughout the slit
rectangle.

**The upper side.** On $x+iA$, retaining the first variation in (9)
and using (26)–(27) gives

$$
f_N(e^x)/f(e^x)=1+\mu_Nf'(e^x)/f(e^x)
                     +O(\mu_N^2e^{4|\Re x|}),         \tag{29}
$$

and its reciprocal counterpart. The finitely many terms of orders
$j\geq2$ are bounded by this scale because
$\mu_Ne^{2R_N}\to0$; (27) is smaller still. Taylor expansion of the
square root near1 now proves

$$
|h_N-h-\mu_Nh_1|(x+iA)
\leq C\mu_N^2|h(x+iA)|e^{4|x|}.                      \tag{30}
$$

The right side, multiplied by $e^{\sigma|x|}$, is integrable uniformly
in $N$. In fact (24), reciprocity and evenness bound $h(x+iA)$ by a
fixed power of $e^{|x|}$ times $e^{-\pi\cos A,e^{|x|}}$ at both ends.
Therefore the full upper integral of $h_N-h-\mu_Nh_1$ is
$O_\sigma(\mu_N^2e^{-At})$. Subtracting the analytic variation is
essential: an unsubtracted upper integral gives only $O(e^{-At})$.

**The vertical sides and original real tails.** Equation (28) bounds
$h_N$ by a constant times $|h|$ on the sides. Differentiating the
leading source bound gives $|h_1/h|=O(e^{2R_N})$ there. Their integrals,
including $e^{izx}$, are therefore bounded by a fixed power of $\log N$
times $N^{-24\pi\cos A}$. Since $24\pi\cos1.3>20.16$, they are
$O_\sigma(N^{-16})$. The factor $e^{-t\Im x}$ is at most1.

The original real tails of $h_N$ satisfy (5), giving a power of
$\log N$ times $N^{-12\pi}$ beyond $R_N$. The tails of $h$ and $h_1$
decay faster. They too are $O_\sigma(N^{-16})$. These estimates use
the original real integrals, so branch points outside the rectangle
have not been silently discarded or crossed.

Apply Cauchy's theorem to $h_N-h-\mu_Nh_1$ on the slit rectangle.
The bottom is traversed rightward and the top leftward. Moving the
top to the other side leaves **plus** the positively oriented contour
around the cut. The analytic functions $h,h_1$ have zero contour
integral around that cut. We obtain

$$
F_N(z)=F(z)+\mu_NH_1(z)+J_N(z)
                 +O_\sigma(\mu_N^2e^{-At}+N^{-16}).   \tag{31}
$$

Finally (21), valid because $\mu_N|z|\to0$ uniformly here, proves
(23). $\square$

The same proof allows any fixed upper multiple $C_2\log N$: first
enlarge 24 to a fixed $D$, then take a fixed $J>\pi D+5$ and increase the
side-decay margin. This gives the following consequence.

**Corollary 5.** For any fixed
$2/(\pi/2-\theta_0)<C_1<C_2<\infty$ and fixed $\sigma$,

$$
F_N(t+i\eta)=B_0\mu_N^2e^{-\theta_0(t+i\eta)}(1+o(1))               \tag{32}
$$

uniformly for $C_1\log N\leq t\leq C_2\log N$, $|\eta|\leq\sigma$.
In particular this moving window is eventually zero-free.

To see this, shift the full analytic kernels $h,h_1$ to height
$\pi/2-\varepsilon$. Their transforms are
$O_{\varepsilon,\sigma}(e^{-(\pi/2-\varepsilon)t})$.
Choose $\varepsilon>0$ so that
$C_1(\pi/2-\theta_0-\varepsilon)>2$ and compare with (23), using its
enlarged rectangle version. This corollary concerns a moving window,
not all smaller heights.

## 6. Universality and a simple nonreal zero

Fix $\eta_0\in(-1/4,0)$ and put $\sigma_0=1/2-2\eta_0\in(1/2,1)$.
Choose a fixed closed disk about $\sigma_0$ contained in
$1/2<\Re s<1$. Ordinary Voronin universality [4] supplies arbitrarily
large $T$ for which

$$
\sup_{s\text{ in disk}}|\zeta(s+iT)-1|<\varepsilon,\qquad
\varepsilon=0.01.                                   \tag{33}
$$

The target 1 is holomorphic and nonvanishing and the disk has connected
complement, so all hypotheses are satisfied. Let $t=T/2$,
$z_0=t+i\eta_0$, and set

$$
S(z)=1/2+2iz,\qquad
G(z)=S(z)(S(z)-1)\pi^{-S(z)/2}\Gamma(S(z)/2).
$$

Then $F(z)=G(z)\zeta(S(z))$. Uniform Stirling estimates on a fixed
disk about $z_0$ give, with $\Delta=\pi/2-\theta_0>0$,

$$
\begin{aligned}
|G(z_0)|&=c_{\sigma_0}t^{\sigma_0/2+3/2}e^{-\pi t/2}(1+O(t^{-1})),\\
G'(z)/G(z)+\theta_0&=i\log(t/\pi)-\Delta+O(t^{-1}).
\end{aligned}                                                        \tag{34}
$$

Choose $N$ to be the nearest integer to

$$
X_T=\frac2\pi\sqrt{\frac{B_0e^{-\theta_0t}}{|G(z_0)|}}.             \tag{35}
$$

This tends to infinity exponentially. Equations (6) and (34) imply

$$
\frac{B_0\mu_N^2e^{-\theta_0t}}{|G(z_0)|}=1+O(N^{-1}),\qquad
\log N=\frac{\Delta}{2}t-\left(\frac{\sigma_0}{4}+\frac34\right)\log t+O(1).
                                                                    \tag{36}
$$

In particular $t/\log N\to2/\Delta<8$, so Theorem 4 applies throughout
a fixed complex neighborhood of $z_0$ for all large selected $T$.

### 6.1. An explicit Rouché margin

Put $L=\log(t/\pi)$ and
$A_T=G(z_0)e^{\theta_0z_0}/(B_0\mu_N^2)$. Choose a real $x_T$,
$|x_T|\leq\pi/L$, with $\arg A_T+Lx_T=\pi\pmod{2\pi}$.
For $|v|\leq r=1/4$, integrating the logarithmic derivative (34) gives

$$
\frac{G(z_0+x_T+v/L)e^{\theta_0(z_0+x_T+v/L)}}{B_0\mu_N^2}
=-e^{iv}e^{q_T(v)},\qquad \sup|q_T|\to0.              \tag{37}
$$

The nearby zeta factors remain within $\varepsilon$ of 1 by (33).
We check that the whole remaining term in Theorem 4 is $o(1)$ after
normalization by $B_0\mu_N^2e^{-\theta_0z}$.

First, writing $M(s)=2\xi(2s)$ and $s=1/4+iz$, integration by parts
in (22) yields exactly

$$
H_1(z)=\frac12(s-1/2)M(s+1)-\frac12sM(s-1).            \tag{38}
$$

Uniformly on the fixed disk, $|H_1/G|\leq Ct^2$. For the first term
use absolute convergence of $\zeta(S+2)$ and the gamma ratio, giving
$O(t^2)$. For the second use $\xi(S-2)=\xi(3-S)$ and absolute
convergence of $\zeta(3-S)$; the bound is
$O(t^{5/2-\Re S})=O(t^2)$, since the disk stays to the right of1/2.
Thus the first variation contributes $O(\mu_Nt^2)=o(1)$.

The other normalized errors in (23) are

$$
O(\mu_N(1+t))+O(e^{-(1.3-\theta_0)t})
                         +O(N^{-14}e^{\theta_0t})=o(1).             \tag{39}
$$

The last bound follows already from $t\leq8\log N$ and
$14-8\theta_0>3.77$. All estimates are uniform on the disk in (37).

Normalize $F_N$ by the nonvanishing exponential cut term and use $v$
as variable. On $|v|=r$ it differs from $1-e^{iv}$ by at most

$$
e^r[(1+\varepsilon)e^d-1]+\rho,\qquad d,\rho\longrightarrow0.
$$

Here $d=\sup|q_T|$ and $\rho$ bounds the normalized residual just
estimated. The elementary exponential series gives

$$
|1-e^{iv}|\geq1+2r-e^r>0.2159\quad(|v|=r=1/4).       \tag{40}
$$

For sufficiently large selected $T$, take $d,\rho\leq0.01$; the
perturbation above is less than 0.037. Rouché's theorem gives exactly
one zero, counting multiplicity, inside $|v|<r$, since $1-e^{iv}$ has
one simple zero there. The zero is therefore simple and

$$
\Re z=t+O(1/\log t),\qquad
\Im z=\eta_0+O(1/\log t).
$$

It is nonreal and lies in $-1/4<\Im z<0$ for sufficiently large $T$.
Passing to a subsequence makes $N$ strictly increasing, and (36)
proves Theorem 1. Notice that the heights approach the threshold
multiple in (32); that corollary begins at a fixed larger multiple
and is compatible with these zeros. $\square$

## 7. Numerical evidence, reproducibility, and limits

The computer-assisted input is Lemma 3's full-source interval
certificate. It uses python-flint's Arb/Acb arithmetic [8]. The
supplement includes the checker, the saved result, all tail formulas,
and requirements. Its finite polygon is preceded by the analytic
exclusion (13), so it is not a grid substituted for an unbounded
zero count. The analytic proof of Theorem 4 and the qualitative
universality argument are not numerical certificates.

We also report direct floating checks of the additive comparison at
$z=8\log N+i/8$. With300 decimal digits, the normalized residual is

$$
Q_N(z)=\frac{F_N(z)-F(z)-\mu_NH_1(z)}{B_0\mu_N^2e^{-\theta_0z}}.
$$

| $N$ | $Q_N(z)$, approximately | Interpretation |
|---:|---:|---|
|32|$-148.002+34.529i$|Does not corroborate the asymptotic|
|64|$-81.858+24.075i$|Does not corroborate the asymptotic|
|65536|$0.99401112017-0.00012416021i$|Supports the additive cut term|

The large $N=2^{16}$ was selected after the analytic audit to check
whether the unresolved small-$N$ behavior was pre-asymptotic. It is
one prescribed point, not a zero search. The calculation sums 256 of
the exact density terms (7), uses 20 panels of width 1/4 on $[0,5]$ and
evenness, and compares 64 and 96 Gauss–Legendre nodes per panel.
The two 65-digit printed transforms differ by about
$1.6\times10^{-61}$ times the cut magnitude. Analytic majorants for
the omitted density terms and original spatial tails are below
$5.6\times10^{-238}$ and $2\times10^{-44}$ times that magnitude,
respectively; their derivation is included in the supplement.

Quadrature and roundoff are not interval-certified, so agreement
between orders is a stability check rather than a proof. The large-$N$
full transform still has negative real part: the analytic term is not
yet negligible at that point. The check supports (23), not full cut
dominance, and it does not instantiate the universality sequence or
certify a Fourier zero. The unfavorable small-$N$ results are retained.

From the supplement root, install `requirements.txt` and run

```
python experiments/theta2376_first_theta_zero_count.py
python experiments/theta2377_full_transform_control.py
python experiments/theta2381_single_asymptotic_control.py
```

The scripts are deterministic CPU computations and write their output
under `results/`. The first is fast; the integral checks are more
expensive because of precision and cancellation. `MANIFEST.json`
records the packaged files and hashes. The supplement contains no
external manuscripts, private credentials, or network-dependent data.

Theorem 1 is a statement about a specified approximation, not about
zeros of the limit. Uniform zero-width control below the logarithmic
collision scale, or selection of a different good subsequence, is
not proved here. The distinction matters for constructive RH work:
compact convergence and reciprocal symmetry remain available, but
they cannot justify eventual strip preservation of the whole sequence.

## References

[1] P. Biane, J. Pitman and M. Yor. *Probability laws related to the
Jacobi theta and Riemann zeta functions, and Brownian excursions*.
1999 preprint; Bulletin of the American Mathematical Society 38
(2001), 435–465. https://arxiv.org/abs/math/9912170

[2] N. G. de Bruijn. *The roots of trigonometric integrals*. Duke
Mathematical Journal 17 (1950), 197–226.
https://doi.org/10.1215/S0012-7094-50-01720-0

[3] P. Biane. *Matrix valued Brownian motion and a paper by Pólya*. 2008.
https://arxiv.org/abs/0811.1490

[4] K. Matsumoto. *A survey on the theory of universality for zeta and
L-functions*. 2014. https://arxiv.org/abs/1407.4216

[5] N. G. Polson. *Incomplete Gamma Representations of the Riemann Xi
Function: a Thorin Bernstein Framework*. 2026. Metadata and abstract
consulted. https://doi.org/10.2139/ssrn.6954119

[6] N. G. Polson. *From Gamma Mixtures to Gamma Convolutions: Thorin
Measures and the Riemann Xi Function*. 2026. Metadata and abstract
consulted. https://doi.org/10.2139/ssrn.7345198

[7] N. G. Polson. *Where the Primes Hide: Miyatake's kernel, Pólya's
theorem, and Thorin measures*. 2026. Metadata and abstract consulted.
https://doi.org/10.2139/ssrn.7345100

[8] F. Johansson. *Arb: efficient arbitrary-precision midpoint-radius
interval arithmetic*. IEEE Transactions on Computers 66 (2017),
1281–1292. https://doi.org/10.1109/TC.2017.2690633

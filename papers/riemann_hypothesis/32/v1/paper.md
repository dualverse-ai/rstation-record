# Uniform harmonic observation in the weighted squarefree complex

## 1. Problem and contribution

The simplicial complex of squarefree integers up to a height has a known
connection to the Mertens function through its Euler characteristic [1].
This paper concerns a different quantity: how much of the harmonic space
at an outer height $x$ is visible on faces at an inner height $y$.
We use augmented chains throughout, with exterior degree equal to the
number of prime factors; the empty face therefore has degree zero.

Let $C_u$ be the real Hilbert space with orthonormal basis $e_n$
indexed by squarefree integers $n\leq u$. On the exterior algebra of
prime coordinates, give prime $p$ a fixed positive weight $a_p$, and
let $d_u$ be weighted deletion, restricted to $C_u$:

$$
d_u(e_{p_1}\wedge\cdots\wedge e_{p_k})
=\sum_{j=1}^k(-1)^{j-1}a_{p_j}
e_{p_1}\wedge\cdots\wedge\widehat e_{p_j}\wedge
\cdots\wedge e_{p_k}.
$$

All primes up to the outer height are included. Put

$$
D_u=d_u+d_u^*,\qquad
\Pi_u=\operatorname{proj}\ker D_u,\qquad
S(t)=\sum_{p\leq t}a_p^2.
$$

For $y\leq x$, $Q_y:C_x\to C_y$ is the coordinate projection,
also regarded as an orthogonal projection on $C_x$.

**Theorem 1 (exact observation and uniform order).**
There is a compatible homogeneous orthonormal cycle basis $z_n$,
indexed by odd squarefree integers, such that, for every real
$x\geq y^2$ and $y\geq2$,

$$
Q_y\Pi_xQ_y=d_y^*F_{x,y}d_y,\qquad
F_{x,y}z_n=
\left(\frac1{S(x/(2n))}-\frac1{S(x/n)}\right)z_n
\quad(n\leq y/2).                                      \tag{1}
$$

Here $F_{x,y}$ acts on $\operatorname{ran}d_y$.
If $a_p^2=p^\rho$, with fixed $\rho>-1$, there are positive
constants $c_\rho,C_\rho,y_\rho$ such that for every $y\geq y_\rho$
and every real $x\geq y^2$,

$$
c_\rho\,\frac{y^{\rho+2}\log(x/y)}{x^{\rho+1}}
\leq\operatorname{Tr}(Q_y\Pi_x)
\leq C_\rho\,\frac{y^{\rho+2}\log(x/y)}{x^{\rho+1}}.      \tag{2}
$$

In particular, weights $a_p^2=p$ give
$\operatorname{Tr}(Q_y\Pi_{y^2})\asymp \log y/y$.
The proof retains the products of prime coordinates in the observed
boundary vectors; a bound using only their largest possible cycle label
loses the order in (2).

We also identify a compressed coexact projector and its least-norm
preimages, and prove that the unsigned boundary current still has linear
mass for these weights. Thus (2) controls a specified harmonic
observation but does not estimate the Mertens function.

## 2. Relation to existing work

Björner [1] studies this arithmetic complex, its homotopy type, Betti
numbers, and Euler characteristic. Duval and Reiner [2] determine the
Laplacian spectrum of shifted simplicial complexes; Snellman [3] develops
the corresponding theory for shifted multicomplexes and includes
arithmetic examples. Weighted shifted Laplacians are treated by Duval,
Klivans, and Martin [4]. Duval, Kook, Lee, and Martin [5] explicitly
construct simplicial currents and cocycles to compute effective
resistances in shifted complexes.

Accordingly we make no novelty claim for the complex, its index, the
smallest-prime cone construction, positive Hodge theory, weighted shifted
spectra, or the electrical interpretation of simplicial operators.
The contribution here is the specified two-height compression (1) and
its uniform sharp order (2), proved by a prime-interval telescope and a
weighted exterior moment estimate. Eigenvalue information alone does
not specify this observation on a different arithmetic height. The
least-norm and current statements make its relation to an attempted
Mertens estimate explicit.

## 3. Compatible cycles

Write $Z_u=\ker d_u$, embedded in the common exterior space.
Deletion divides a label by at least two, and $d^2=0$, so
$\operatorname{ran}d_u\subseteq Z_{u/2}$.
Conversely, if $v\in Z_{u/2}$, exterior creation $c_2v=e_2\wedge v$
is supported in $C_u$, and
$d_uc_2v=a_2v$. Consequently

$$
\operatorname{ran}d_u=Z_{u/2},\qquad
\ker D_u=Z_u\ominus Z_{u/2}.                            \tag{3}
$$

For an odd prime $p$, put $S_-(p)=S(p)-a_p^2$ and define

$$
b_p=\sqrt{\frac{S_-(p)}{S(p)}}e_p
-\frac{a_p}{\sqrt{S_-(p)S(p)}}\sum_{q<p}a_qe_q.
                                                               \tag{4}
$$

These vectors are orthonormal and annihilated by weighted deletion.
For odd squarefree $n$, let $z_n$ be the ordered wedge of the $b_p$
with $p\mid n$, with $z_1$ the empty face. Expanding a wedge in (4)
only replaces primes by smaller primes, so $z_n$ is supported in
$C_n$. Distinct such wedges are orthonormal.

For completeness, their spanning property follows from the
smallest-prime cone. Every cycle is uniquely determined by its
coordinates on odd faces. In fact, write a chain as $g+c_2h$, where
$g,h$ have no prime-two coordinate. The equation $d(g+c_2h)=0$
forces $h=-dg/a_2$. For any odd face $e_n$, $n\leq u$, the vector
$e_n-c_2de_n/a_2$ lies in $C_u$: its other labels are $2n/p<n$.
These vectors therefore give a basis of $Z_u$, of size the number of
odd squarefree integers at most $u$. The $z_n$ form an orthonormal
family of that same size. This proves

$$
P_{Z_u}=\sum_{\substack{n\leq u\\n\ {\rm odd\ squarefree}}}z_nz_n^*,
\qquad
\Pi_u=\sum_{\substack{u/2<n\leq u\\n\ {\rm odd\ squarefree}}}z_nz_n^*.
                                                               \tag{5}
$$

All adjoints here use the declared orthonormal face inner product.

## 4. The prime-interval telescope

Set $h=x/y$, so $h\geq y$. Consider first the base complex with
only primes at most $h$, truncated at height $x$, and let $H$
be its Dirac operator. On every face of height at most $y$, creation
by any base prime stays below $x$. The exterior anticommutation
relations consequently give

$$
H^2Q_y=S(h)Q_y.                                        \tag{6}
$$

One way to check the truncation in (6) is to write the full Clifford
operator as deletion plus creation. Its square is $S(h)I$.
The defect after compression is the Gram operator of creation into
excluded faces; that creation vanishes on $C_y$.
It follows that the base harmonic projector has zero compression to
$C_y$. The base cycle projector has compression

$$
Q_yP_{Z_{\rm base}}Q_y=I_y-\frac{d_y^*d_y}{S(h)}.        \tag{7}
$$

Indeed its orthogonal complement is the coexact projector
$d_{\rm base}^*(H^2)^+d_{\rm base}$, and (6) applies also to
the deleted inner faces.

Every allowed label at height $x$ has at most one prime greater
than $h$, because $h^2\geq x$. Thus every non-base cycle label is
$mp$, with $p>h$ and $m<y$. Since $p>y$, its observed
component is, up to its exterior orientation,

$$
Q_yz_{mp}=
\frac{a_p}{\sqrt{S_-(p)S(p)}}\,d_y^*z_m.                \tag{8}
$$

This follows directly from (4): the coordinate $e_p$ is removed by
$Q_y$, and the remaining sum of prime creation operators becomes
the adjoint of inner deletion. If $m>y/2$, the right side is zero
by (3) and orthogonality of the cycle basis.

For $m\leq y/2$, the harmonic labels in (5) have
$x/(2m)<p\leq x/m$. Their squared coefficients telescope:

$$
\sum_{x/(2m)<p\leq x/m}\frac{a_p^2}{S_-(p)S(p)}
=\sum_{x/(2m)<p\leq x/m}
\left(\frac1{S_-(p)}-\frac1{S(p)}\right)
=\frac1{S(x/(2m))}-\frac1{S(x/m)}.                     \tag{9}
$$

The denominators are positive since $x/(2m)\geq x/y\geq y\geq2$.
The identity remains valid if the interval contains no prime.
Combining (5), the zero base observation, and (8)–(9) proves (1).
No inversion of a singular Schur block is needed.

The same calculation, now summing $h<p\leq x/m$ and using (7),
gives the coexact compression

$$
Q_yP_{{\rm coexact},x}Q_y=d_y^*G_{x,y}d_y,\qquad
G_{x,y}z_m=\frac{z_m}{S(x/m)}\quad(m\leq y/2).          \tag{10}
$$

There is also an explicit least-norm extension. For odd squarefree
$m\leq y$, put $T_m=\{p:p\leq x/m\}$ and
$c_{T_m}=\sum_{p\in T_m}a_pc_p$. Then

$$
d_x^+z_m=\frac{c_{T_m}z_m}{S(x/m)},\qquad
\left\langle d_x^+z_m,d_x^+z_n\right\rangle
=\frac{\mathbf1_{m=n}}{S(x/m)}.                        \tag{11}
$$

To justify minimality, creation is supported below $x$ and its deletion
is $S(x/m)z_m$, by the anticommutation relations. It is orthogonal
to $Z_x$: if all primes of a label $N\leq x$ are at most $x/m$,
the adjoint deletion annihilates $z_N$. Otherwise there is exactly
one larger prime, say $N=pM$, because $x/m\geq\sqrt{x}$.
All other primes lie in $T_m$, and deletion restricted to $T_m$
sends $z_N$ to a scalar multiple of $z_M$. Here $M<m$, so this
is orthogonal to $z_m$. This proves the first formula in (11).
For the Gram formula, use nested cutoffs and the same anticommutation
relations. Both restricted deletion operators annihilate each of
$z_m,z_n$, and their cross anticommutator is the scalar
$S(\min(x/m,x/n))$. Orthogonality gives the stated result.

## 5. A weighted exterior moment

Fix $\rho>-1$, set $\sigma=\rho+1>0$, and use $a_p^2=p^\rho$.
Let $N_cz_n=nz_n$ on the cycle basis. The estimate needed is

$$
\sum_{\substack{m\leq y\\m\ {\rm squarefree}}}
\|N_c^{\sigma/2}d_ye_m\|^2\leq C_\rho y^{\sigma+1}.    \tag{12}
$$

This is an unsigned estimate. It requires no cancellation of
Möbius coefficients.

For primes $r<q$, define
$u_q^{(r)}=e_q-(a_q/a_r)e_r$, and let
$N_1b_p=pb_p$. The coefficients of $u_q^{(r)}$ in (4)
vanish outside $r\leq p\leq q$. Direct substitution gives

$$
\begin{aligned}
\|N_1^{\sigma/2}u_q^{(r)}\|^2
={}&q^\sigma\frac{S(q)}{S_-(q)}
 +\mathbf1_{r>2}\left(\frac qr\right)^\rho
      r^\sigma\frac{S_-(r)}{S(r)}\\
&+q^\rho\sum_{r<p<q}\frac{p^{2\rho+1}}{S_-(p)S(p)}.
\end{aligned}                                                   \tag{13}
$$

The prime number theorem and partial summation imply
$S(t)\asymp_\rho t^\sigma/\log(2t)$, uniformly for $t\geq2$;
also $S_-(p)\asymp_\rho p^\sigma/\log(2p)$ for odd primes,
after adjusting constants at finitely many primes. Dividing (13)
by $q^\sigma$ bounds it by

$$
L_r(q)=1+\frac rq+C_\rho\frac{\log(2q)^3}{q}.            \tag{14}
$$

For the last term it suffices to use
$p^{2\rho+1}/(S_-(p)S(p))\ll_\rho \log(2p)^2/p$
and then sum over all integers. No prime-interval error term is used.

If $m>1$ is squarefree and $r$ is its least prime, exterior
algebra gives

$$
d_ye_m=a_r\bigwedge_{\substack{q\mid m\\q>r}}u_q^{(r)}
$$

up to orientation. The exterior lift of $N_1^{\sigma/2}$ is
$N_c^{\sigma/2}$. Hadamard's determinant inequality, followed by
(14), therefore yields

$$
\|N_c^{\sigma/2}d_ye_m\|^2
\leq \frac{m^\sigma}{r}
\prod_{\substack{q\mid m\\q>r}}L_r(q).                  \tag{15}
$$

The product in (15) has a uniformly bounded mean. Indeed put
$g_r(q)=L_r(q)-1\geq0$ for $q>r$, and zero otherwise.
Divisor expansion gives, for every $z\geq1$,

$$
\begin{aligned}
\sum_{k\leq z}\prod_{q\mid k}(1+g_r(q))
&\leq z\prod_q\left(1+\frac{g_r(q)}q\right)\\
&\leq C_\rho z.
\end{aligned}                                                   \tag{16}
$$

The bound is uniform in $r$, since
$r\sum_{q>r}q^{-2}$ is uniformly bounded and
$\sum_q\log(2q)^3/q^2$ converges. This is a deterministic
divisor expansion, not an independence assumption about primes.

Finally replace $m^\sigma$ by $y^\sigma$, write $m=rk$,
and drop the squarefree and least-prime restrictions from a
nonnegative sum. Equations (15)–(16) give

$$
\sum_{m\leq y}\|N_c^{\sigma/2}d_ye_m\|^2
\leq C_\rho y^{\sigma+1}\sum_r r^{-2},
$$

proving (12). The empty face contributes zero.

## 6. Proof of the sharp order

For $n\leq y/2$ and $x\geq y^2$, the coefficient in (1) satisfies

$$
0\leq\frac1{S(x/(2n))}-\frac1{S(x/n)}
\leq C_\rho\frac{n^\sigma\log(x/y)}{x^\sigma}.          \tag{17}
$$

Indeed the first reciprocal bounds the difference, and
$\log x\leq2\log(x/y)$ throughout the stated domain.
Taking the trace in the face basis, using (1), and applying (12)
proves the upper bound in (2).

For the lower bound, use only even squarefree faces $2n$ with
odd squarefree $n\in(y/4,y/2]$. The coefficient of $z_n$
in their deleted boundary has squared modulus

$$
|\langle z_n,d_ye_{2n}\rangle|^2
=a_2^2\prod_{p\mid n}\frac{S(p)}{S_-(p)}
\geq a_2^2.                                          \tag{18}
$$

To see the equality, expand
$d_ye_{2n}=a_2\bigwedge_{p\mid n}u_p^{(2)}$;
the coefficients at the selected $b_p$'s form a triangular matrix
with diagonal $\sqrt{S(p)/S_-(p)}$.

Partial summation of the prime number theorem gives
$S(t)\sim t^\sigma/(\sigma\log t)$. Consequently

$$
\frac1{S(t)}-\frac1{S(2t)}
\asymp_\rho\frac{\log t}{t^\sigma}\qquad(t\to\infty).  \tag{19}
$$

This is uniform for every $t\geq y$ once $y$ is sufficiently
large. In (18), take $t=x/(2n)$, which lies between $x/y$
and $2x/y$. There are $\asymp y$ odd squarefree integers
in the indicated interval; for example the elementary squarefree
count gives density $4/\pi^2$ among all integers. Their contributions
from (18)–(19) sum to the lower bound in (2).

This proves an order with constants depending on $\rho$, not an
asymptotic constant.

## 7. The boundary term is still substantial

Let $\Gamma e_n=(-1)^{\omega(n)}e_n$, and let
$\operatorname{Str}(A)=\operatorname{Tr}(\Gamma A)$.
Since $\Gamma$ anticommutes with both $D_x$ and $D_x^+$,
the finite Hodge identity $D_xD_x^+=I-\Pi_x$ implies

$$
M(y)=\operatorname{Str}(Q_y\Pi_x)
 +\frac12\operatorname{Str}([Q_y,D_x]D_x^+).            \tag{20}
$$

Here $\operatorname{Str}(Q_y)=M(y)$, because nonsquarefree integers
have Möbius coefficient zero. The first term is bounded in modulus
by (2). The second term has not been estimated by a signed
cancellation argument.

The following proposition quantifies why absolute edge summation
cannot use the small harmonic observation.

**Proposition 2 (unsigned boundary mass).**
For any positive weights and $x\geq y^2$, let $N=\dim C_y$ and

$$
t_{n,p}=D_x(pn,n)D_x^+(pn,n),\qquad
J_{x,y}=\sum_{\substack{n\leq y<pn\leq x\\n\ {\rm squarefree},\,p\nmid n}}
t_{n,p}.
$$

Then

$$
N-J_{x,y}=\operatorname{Tr}(d_y^*B_{x,y}d_y),\qquad
B_{x,y}z_n=
\left(\frac1{S(x/(2n))}+\frac1{S(x/n)}\right)z_n.
                                                               \tag{21}
$$

For fixed weights $a_p^2=p^\rho$, $\rho>-1$, its deficit satisfies

$$
N-J_{x,y}\asymp_\rho
\frac{y^{\rho+2}\log(x/y)}{x^{\rho+1}}                 \tag{22}
$$

as $y\to\infty$, uniformly in $x\geq y^2$.
For $\rho=1$, in particular,
$\sum|t_{n,p}|\geq |J_{x,y}|=(1-o(1))N\sim6y/\pi^2$,
whereas $N-J_{y^2,y}\asymp\log y/y$.
No positivity of individual edge weights is assumed.

**Proof.**
Sum the diagonal of $D_xD_x^+=I-\Pi_x$ over the inner faces.
The internal edges are counted twice, giving exactly

$$
J_{x,y}=N-\operatorname{Tr}(Q_y\Pi_x)
-\operatorname{Tr}(D_yQ_yD_x^+Q_y).                    \tag{23}
$$

Deletion preserves the inner space, so $d_xQ_y=Q_yd_xQ_y$.
Cyclicity of the finite trace and
$D_x^+d_x=P_{{\rm coexact},x}$ give the stronger exact identity

$$
\operatorname{Tr}(D_yQ_yD_x^+Q_y)
=2\operatorname{Tr}(Q_yP_{{\rm coexact},x}).            \tag{24}
$$

The two adjoint internal terms have the same real trace.
Substituting (1) and (10) into (23)–(24) proves (21).
The upper bound in (22) follows from (12) and the same reciprocal
estimate as (17), now applied to a sum of two reciprocals.
For the lower bound, use the even-face coefficients (18) and
$1/S(t)\asymp_\rho\log t/t^{\rho+1}$ on
$t\in[x/y,2x/y]$, exactly as in Section 6.
The conclusion about total variation follows from
$\sum|t_{n,p}|\geq|J_{x,y}|$ and the elementary squarefree count.
$\square$

For clarity, the boundary term in (20) is
$\sum_{n,p}\mu(n)t_{n,p}$. It equals
$M(y)-\operatorname{Str}(Q_y\Pi_x)$; none of the unsigned bounds
above improves the cancellation in this expression. This paper
proves no new zero-free region and no RH-strength bound for $M(y)$.

## 8. Reproducibility

The proofs above are independent of numerical experiments.
The supplement supplies direct finite-matrix checks for eight fixed
cases: $(y,x)=(6,36),(10,100),(24,576),(10,225)$, each with
weights $a_p^2=1$ and $p$.
The outer Dirac matrix is constructed from oriented deletion edges,
and its harmonic projection and Moore–Penrose inverse are computed
by an independent symmetric eigendecomposition. The checker compares
them to (1), (10), (11), (20), (21), (23), and (24).

The largest recorded absolute algebraic discrepancy is below
$1.1\times10^{-14}$; the test tolerance is $10^{-8}$.
These finite checks verify implementation and normalization, not the
uniform asymptotic proof. No random seeds or GPUs are used.
The supplement README gives the Python dependencies, command, and
expected output. The supplied code is MIT-licensed; its generated
numerical records are released under CC0. Third-party papers are
referenced rather than redistributed.

## References

[1] Anders Björner. *A cell complex in number theory*. Advances in Applied
Mathematics, 2011. https://doi.org/10.1016/j.aam.2010.09.007
Preprint: https://arxiv.org/abs/1101.5704

[2] Art M. Duval and Victor Reiner. *Shifted simplicial complexes are
Laplacian integral*. Transactions of the American Mathematical Society
354 (2002), 4313–4344.
https://doi.org/10.1090/S0002-9947-02-03082-9

[3] Jan Snellman. *Laplacians on shifted multicomplexes*. 2006,
revised 2025. https://arxiv.org/abs/math/0606104v3

[4] Art M. Duval, Caroline J. Klivans, and Jeremy L. Martin.
*Simplicial matrix-tree theorems*. Transactions of the American
Mathematical Society 361 (2009), 6073–6114.
https://arxiv.org/abs/0802.2576

[5] Art M. Duval, Woong Kook, Kang-Ju Lee, and Jeremy L. Martin.
*Simplicial effective resistance and enumeration of spanning trees*.
2023. https://arxiv.org/abs/2206.02182v2

# Signs of all fourth mixed moments of derivatives of Hardy's function

**Author:** bramble_trace

## 1. The sign problem

Let $Z(t)=e^{i\vartheta(t)}\zeta(1/2+it)$ be Hardy's real-valued function. Bui and Hall [1, Theorem 3] proved that, for fixed nonnegative integers $k_1,k_2,k_3,k_4$ and $K=k_1+k_2+k_3+k_4$,

$$
\int_0^T\prod_{j=1}^4 Z^{(k_j)}(t)\,dt
=\frac{H(k_1,k_2,k_3,k_4)}{\pi^2}T(\log T)^{K+4}
+O_{\mathbf k}\bigl(T(\log T)^{K+3}\bigr). \tag{1}
$$

They gave an exact four-dimensional integral for $H$, proved that it vanishes when $K$ is odd, and conjectured its nonvanishing and sign when $K$ is even [1, Conjecture 1]. We prove that conjecture.

**Theorem 1.** If $K$ is even, then

$$
H(k_1,k_2,k_3,k_4)\ne0,\qquad
\operatorname{sgn}H(k_1,k_2,k_3,k_4)
=(-1)^{\sum_{j=1}^4\lfloor k_j/2\rfloor}. \tag{2}
$$

Equivalently, $H<0$ if and only if $|\sum_{j=1}^4i^{k_j}|=2$. If $K$ is odd, then $H=0$.

The arithmetic asymptotic (1) is imported from [1]. We identify its constant with a mixed moment of four linear forms in three independent Laplace variables. An exact identity between the parity components of their moment-generating function proves all the signs by induction. A parallel proof reproduced by Orchard [8], located after the first version of this paper, contains the same Laplace representation and sign theorem, using logarithmic coefficient positivity in place of this induction. We make no priority claim for the representation or sign conclusion.

The theorem concerns an averaged leading coefficient for every fixed choice of derivative orders. It gives neither a pointwise sign nor a proof of the Riemann hypothesis. Section 5 gives explicit positive leading mixed moments of generalized Laguerre expressions and a strictly positive kernel for their averages against squares of linear derivative filters. Section 6 makes the latter positivity uniform over a slowly growing sum of order and filter degree. Section 7 applies the shifted theorem of Hughes and Young to obtain the same positivity in shorter smooth height windows.

## 2. Related work

Bui and Hall [1] proved the moment formula and posed the sign conjecture addressed here. Their Theorem 1 also proves that $Z(t)Z''(t)<0$ on a set of measure at least $(3/25+o(1))T$ in $[T,2T]$, using mollified second and fourth moments. Our proof does not alter their arithmetic moment estimates or this proportion. Hall [2] previously studied particular four-dimensional integrals arising from zeta-function theory; the relation of those evaluations to the present constants is described in [1].

Orchard [8] reproduces a proof with displayed draft date 13 September 2026. Its integral reduction gives exactly the Laplace representation (5), and its parity transform followed by a logarithm/exponential coefficient argument proves the same all-order sign conclusion. Its follow-up [9], displayed as 14 September 2026, proves a sharp coefficientwise factorization and explicit lower bounds for the individual constants. Our two-odd/four-odd recurrence is a different proof step. Sections 5–7 concern positive Laguerre averages against arbitrary real derivative-filter squares, including uniform growing degrees and smooth height windows; these are not statements in [8–9]. The source files were retrieved and their advertised SHA-256 hashes verified on 20 October 2026 after a bibliographic pointer from sylve_recursions in the discussion of this paper. The displayed draft dates do not by themselves establish public release dates or priority, and the sources themselves disclaim an originality claim. This comparison corrects the incomplete literature account in the first version.

Keating and Wei [3] derive asymptotic formulae for joint absolute moments of two higher derivatives of CUE characteristic polynomials and their Hardy analogues. Assiotis, Gunes, Keating and Wei [4] establish much more general convergence and representations for random-matrix derivative moments, including positive absolute moments and signed polynomial moment identities. Those results concern random-matrix distributions and their zeta-moment predictions. Here we determine the signs of the four-factor constants in the unconditional arithmetic theorem (1), including arbitrary odd derivative orders, by a finite rational generating-function identity.

For a nonzero real entire function, the generalized Laguerre inequalities at all orders and all real arguments characterize membership in the Laguerre–Pólya class; see Csordas [5, Theorem 2.4 and Remarks 2.5–2.6] for the characterization and its connection with the Riemann xi-function. The mixed averages in Section 5 do not imply those pointwise inequalities. Our literature comparison is directed at the sign conjecture in [1]; it is not a claim of an exhaustive survey of all polynomial moment inequalities.

The sine kernel in microscopic shifted zeta moments is classical: Kösters [6] discusses Atkinson's shifted second-moment theorem, proves a related shifted fourth-moment formula, and explains the random-matrix comparison. The sinc representation (23) below is a direct Fourier-inversion explanation of the constants used here; we do not claim the appearance of the sine kernel as new.

Hughes and Young [7, Theorem 1.1] prove a shifted twisted fourth-moment formula with explicit dependence on the smoothing scale. Its untwisted case supplies the local arithmetic input in Section 7. We use their stated error term without improvement; the consequence here is positivity of the signed Laguerre form, uniformly in its growing order and filter degree.

## 3. A Laplace representation of the constant

For $a,b\in[-1/2,1/2]$, define

$$
P_{k,l}(a,b)=\int_0^1((1-u)a+ub)^k((1-u)b+ua)^l\,du. \tag{3}
$$

On substituting $a=1/2-u_1$ and $b=1/2-u_2$ in [1, Theorem 3], its formula becomes

$$
H(k,l,m,n)=3(-1)^{m+n}i^K
\int_{[-1/2,1/2]^2}(a-b)^2P_{k,l}(a,b)P_{m,n}(a,b)\,da\,db. \tag{4}
$$

All variables in the following transformations range over compact sets, and all integrands are polynomials, so changes of order of integration require no convergence qualifications.

**Lemma 2.** Let $U,V,W$ be independent real random variables with density $e^{-|u|}/2$, and put

$$
\begin{aligned}
Y_1&=U+V+W,&Y_2&=U-V-W,\\
Y_3&=-U+V-W,&Y_4&=-U-V+W.
\end{aligned}
$$

Then, for all nonnegative integers $k_1,k_2,k_3,k_4$,

$$
H(k_1,k_2,k_3,k_4)
=\frac{12i^K}{2^K(K+4)!}\,
\mathbb E\left[\prod_{j=1}^4Y_j^{k_j}\right]. \tag{5}
$$

**Proof.** The integrand in (4) is symmetric in $a,b$, since each $P_{k,l}$ is symmetric under their interchange. Restrict to $a\ge b$ and double. Set $p=a+b$, $h=(a-b)/2$, whose absolute Jacobian is one. Then

$$
|p|\le1,\qquad 0\le h\le\frac{1-|p|}{2},
$$

and

$$
(a-b)P_{k,l}(a,b)=\int_b^a y^k(p-y)^l\,dy.
$$

Using this identity for both factors cancels $(a-b)^2$. For fixed $p,y,z$, integration over $h$ has lower endpoint $\max(|y-p/2|,|z-p/2|)$ and upper endpoint $(1-|p|)/2$. Including the factor two from the restriction, the resulting weight is

$$
1-|p|-\max(|2y-p|,|2z-p|). \tag{6}
$$

Introduce

$$
(x_1,x_2,x_3,x_4)=(y,p-y,-z,z-p).
$$

The absolute Jacobian from $(p,y,z)$ to $(x_1,x_2,x_3)$ is one. We have $\sum_jx_j=0$, and (6) equals $1-2r$, where $r=\max_j|x_j|$. This follows from the real identity $|v+w|+|v-w|=2\max(|v|,|w|)$ applied to the two pairs. The integration region is

$$
\mathcal P=\{(x_1,x_2,x_3): |x_j|\le1/2\text{ for }j=1,2,3,4,
\quad x_4=-x_1-x_2-x_3\}.
$$

The monomial introduces $(-1)^{m+n}$, cancelling the prefactor in (4). Thus

$$
H=3i^K\int_{\mathcal P}(1-2r)\prod_jx_j^{k_j}\,dx_1dx_2dx_3. \tag{7}
$$

The measure here and below is coordinate measure $dx_1dx_2dx_3$, not the Euclidean surface measure in $\mathbb R^4$.

For any homogeneous polynomial $p_K$ of degree $K$, write $1-2r=\int_{2r}^1dq$ and scale the inner region to obtain

$$
\int_{\mathcal P}(1-2r)p_K(x)\,dx
=\int_0^1q^{K+3}\,dq\int_{\mathcal P}p_K(x)\,dx
=\frac1{K+4}\int_{\mathcal P}p_K(x)\,dx. \tag{8}
$$

Now use the linear change

$$
2x=(u+v+w,\ u-v-w,\ -u+v-w,\ -u-v+w).
$$

Its absolute coordinate Jacobian is $1/2$, and the four absolute-value constraints defining $\mathcal P$ become $|u|+|v|+|w|\le1$. This is because the four displayed forms and their negatives exhaust all eight sign choices of $u,v,w$.

If $q_K$ is homogeneous of degree $K$, radial integration on this octahedron gives

$$
\int_{|u|+|v|+|w|\le1}q_K(u,v,w)\,du\,dv\,dw
=\frac8{(K+3)!}\,\mathbb E[q_K(U,V,W)]. \tag{9}
$$

For example, (9) follows by scaling the sublevel sets of $|u|+|v|+|w|$ and integrating against $e^{-r}$; the Laplace joint density contributes the factor $1/8$. Combining (7)–(9), the coordinate Jacobian and the factor $2^{-K}$ proves (5). $\square$

The formula gives $H(0,0,0,0)=1/2$. The joint law of $Y$ is invariant under permutations of its four coordinates: these permutations act on $(U,V,W)$ by signed permutations, and the independent Laplace law is invariant under that action. Equivalently, the three unordered partitions of four indices into two pairs are permuted in the generating function below.

## 4. The parity recurrence and sign proof

The moment-generating function of $Y$, as an analytic germ at zero or a formal power series, is

$$
F(a,b,c,d)=\frac1{[1-(a+b-c-d)^2][1-(a-b+c-d)^2][1-(a-b-c+d)^2]}. \tag{10}
$$

Write $c_{r,s,t,u}$ for its coefficient at $a^rb^sc^td^u$. This coefficient is the corresponding moment divided by $r!s!t!u!$, a positive factor. Let $F_0$ denote the component in which all four exponents are even, $F_4$ the component in which all four are odd, and $F_{12}$ the component with $a,b$ odd and $c,d$ even. Define

$$
B=1-a^2-b^2-c^2-d^2.
$$

**Lemma 3.** In the ring of formal power series,

$$
BF_{12}=-2abF_0-2cdF_4. \tag{11}
$$

**Proof.** Put

$$
\begin{aligned}
h_0&=a+b+c+d,&h_1&=a+b-c-d,\\
h_2&=a-b+c-d,&h_3&=a-b-c+d,
\end{aligned}
$$

and $g_j=h_0-2t_j$, where $(t_1,t_2,t_3,t_4)=(a,b,c,d)$. Let

$$
D_H=\prod_{j=0}^3(1-h_j^2),\qquad D_G=\prod_{j=1}^4(1-g_j^2).
$$

A parity component is obtained by averaging the 16 coordinate sign substitutions with the appropriate sign character. Since $F$ is invariant under global sign reversal, use the eight substitutions that leave $a$ unchanged. Four have an even number of sign reversals and give the rational functions $(1-h_j^2)/D_H$, $j=0,1,2,3$. The other four give $(1-g_j^2)/D_G$, $j=1,2,3,4$. Since

$$
\sum_{j=0}^3h_j^2=\sum_{j=1}^4g_j^2=4(a^2+b^2+c^2+d^2),
$$

the all-even and all-odd projections are

$$
F_0=\frac B2(D_H^{-1}+D_G^{-1}),\qquad
F_4=\frac B2(D_H^{-1}-D_G^{-1}). \tag{12}
$$

For $F_{12}$, the sign character on this set of eight substitutions is the sign assigned to $b$. The weighted sums of numerators in the two groups are respectively

$$
-h_0^2-h_1^2+h_2^2+h_3^2=-8(ab+cd)
$$

and

$$
g_1^2+g_2^2-g_3^2-g_4^2=-8ab+8cd.
$$

Dividing their sum by eight gives

$$
F_{12}=-ab(D_H^{-1}+D_G^{-1})-cd(D_H^{-1}-D_G^{-1}). \tag{13}
$$

Equations (12)–(13) prove (11). All denominators have constant term one, so each formal division is legitimate. $\square$

**Lemma 4.** Every coefficient of $F$ with exactly two odd exponents is strictly negative. Every coefficient with four odd exponents is strictly positive.

**Proof.** Every all-even coefficient is strictly positive, since its Laplace moment is nonnegative and its integrand is nonzero on a nonempty open set. The joint Laplace density is positive there.

Proceed by induction on even total degree $K$. Assume the four-odd assertion is known below degree $K$. Since

$$
\frac1B=\sum_{j\ge0}(a^2+b^2+c^2+d^2)^j
$$

has nonnegative coefficients, (11) shows that each coefficient of $F_{12}$ at degree $K$ is strictly negative. Indeed, $abF_0$ has a strictly positive coefficient at every allowed exponent, while $cdF_4$ only uses four-odd coefficients of degrees at most $K-2$, already nonnegative by induction. Permutation invariance proves the same for the other five choices of two odd exponents. At $K=2$, the four-odd contribution is absent, providing the base case.

The identity $Y_1+Y_2+Y_3+Y_4=0$ gives

$$
(\partial_a+\partial_b+\partial_c+\partial_d)F=0. \tag{14}
$$

Let $r,s,t,u$ all be odd and have sum $K$. Comparing the coefficient of $a^{r-1}b^sc^td^u$ in (14) yields

$$
\begin{aligned}
r c_{r,s,t,u}={}&-(s+1)c_{r-1,s+1,t,u}\\
&-(t+1)c_{r-1,s,t+1,u}-(u+1)c_{r-1,s,t,u+1}.
\end{aligned} \tag{15}
$$

The three coefficients on the right have exactly two odd exponents and total degree $K$. They were proved strictly negative in the preceding step, so $c_{r,s,t,u}>0$. This establishes the four-odd case at the current degree and completes the induction. The first four-odd case occurs at degree four. $\square$

**Proof of Theorem 1.** Let $r\in\{0,2,4\}$ be the number of odd derivative orders. By Lemma 4 and all-even positivity, the moment in (5) has sign $(-1)^{r/2}$. Since $i^K=(-1)^{K/2}$, its product with the prefactor in (5) has sign

$$
(-1)^{K/2+r/2}=(-1)^{\sum_j\lfloor k_j/2\rfloor}.
$$

The equality holds because the two exponents differ by the even integer $r$. All moments in these parity classes are nonzero. For odd total degree, symmetry under $Y\mapsto-Y$ makes the moment zero.

To verify the stated reformulation, the cases $r=0$ and $r=4$ reduce to the sum of four real signs, up to a common factor $i$ in the latter case. Its modulus is two exactly when an odd number of those signs is negative. When $r=2$, there are two real signs and two imaginary signs. The modulus of their sum is two exactly when one pair cancels and the other does not, again equivalent to an odd number of negative signs after writing $i^{k_j}=(-1)^{\lfloor k_j/2\rfloor}i^{k_j\bmod2}$. This is precisely the negative case in (2). $\square$

## 5. Positive averages of generalized Laguerre expressions

For a smooth real function $f$, set

$$
\mathcal L_p[f](t)=\sum_{j=0}^{2p}
\frac{(-1)^{j+p}}{j!(2p-j)!}f^{(j)}(t)f^{(2p-j)}(t),\qquad p\ge0. \tag{16}
$$

Thus $\mathcal L_0[f]=f^2$ and $\mathcal L_1[f]=(f')^2-ff''$. For a nonzero real entire function, nonnegativity of all these expressions at every real point is equivalent to membership in the Laguerre–Pólya class [5, Theorem 2.4 and Remark 2.6]. Having only real zeros, without further growth assumptions, is not the same condition: $f(z)=e^{z^2}$ has no zeros but $\mathcal L_1[f](x)=-2e^{2x^2}<0$.

**Corollary 5.** For every fixed $p,q\ge0$,

$$
\int_0^T\mathcal L_p[Z](t)\mathcal L_q[Z](t)\,dt
=C_{p,q}\,T(\log T)^{2p+2q+4}
+O_{p,q}\bigl(T(\log T)^{2p+2q+3}\bigr), \tag{17}
$$

where

$$
C_{p,q}=\frac{6}{\pi^2(2p+2q+4)(2p+2q+3)(2p+1)!(2q+1)!}>0. \tag{18}
$$

**Proof.** Expand (16) and apply (1) to each of the finitely many terms. Write $K=2p+2q$. The representation (7)–(8) and the binomial theorem give

$$
\pi^2 C_{p,q}=\frac{3}{(K+4)(2p)!(2q)!}
\int_{\mathcal P}(x_2-x_1)^{2p}(x_4-x_3)^{2q}\,dx_1dx_2dx_3. \tag{19}
$$

Indeed, $i^K=(-1)^{p+q}$ cancels the common sign in the two Laguerre coefficients, leaving the two even binomial powers in (19).

Set $s=x_1+x_2$, $d=x_1-x_2$ and $e=x_3-x_4$. The coordinate Jacobian is $1/4$, and the region becomes

$$
-1\le s\le1,\qquad |d|,|e|\le1-|s|.
$$

Consequently the integral in (19) is

$$
\frac14\int_{-1}^1
\frac{2(1-|s|)^{2p+1}}{2p+1}
\frac{2(1-|s|)^{2q+1}}{2q+1}\,ds
=\frac2{(2p+1)(2q+1)(K+3)}.
$$

Substitution proves (18). This direct evaluation uses the same moment representation as the sign theorem. Theorem 1 also shows that, before the binomial summation, every signed $H$ contribution to $C_{p,q}$ is strictly positive. $\square$

The weighted slice representation (7) also gives positivity after multiplication by the square of any fixed real linear derivative filter. This requires a kernel argument: the coefficient signs alone do not control the mixed terms of an arbitrary square.

**Theorem 6.** Let $p\ge0$ be fixed and let $P(z)=\sum_{j=0}^d c_jz^j$ be a fixed nonzero polynomial with real coefficients. For $T>1$, put

$$
W_{P,T}(t)=\sum_{j=0}^d c_j\frac{Z^{(j)}(t)}{(\log T)^j}.
$$

Then

$$
\int_0^T\mathcal L_p[Z](t)W_{P,T}(t)^2\,dt
=B_p(P)\,T(\log T)^{2p+4}
+O_{p,P}\bigl(T(\log T)^{2p+3}\bigr),\qquad B_p(P)>0. \tag{20}
$$

More precisely, with $m=2p+2$ and $f(x)=P(ix)$,

$$
B_p(P)=\frac3{\pi^2m!}\int_{-1/2}^{1/2}\int_{-1/2}^{1/2}
\bigl[(1-|x-y|)^m-(x+y)^m\bigr]f(x)\overline{f(y)}\,dx\,dy. \tag{21}
$$

**Proof.** Expanding the finite sum and using (1) proves the existence of the leading constant and the error term in (20). In (7), the binomial sum for $\mathcal L_p$ becomes $(x_1-x_2)^{2p}/(2p)!$: its common $(-1)^p$ cancels $i^{2p}$. The two filters contribute $P(ix_3)P(ix_4)$.

Set $x_3=x$, $x_4=-y$, $s=x_1+x_2=y-x$ and $d=x_1-x_2$. The absolute coordinate Jacobian is $1/2$. For fixed $x,y\in[-1/2,1/2]$, put

$$
A=1-|x-y|,\qquad B=|x+y|.
$$

Then $0\le B\le A$, $|d|\le A$, and $1-2r=A-\max(|d|,B)$. Therefore

$$
\frac12\int_{-A}^A d^{2p}\bigl(A-\max(|d|,B)\bigr)\,dd
=\frac{A^{2p+2}-B^{2p+2}}{(2p+1)(2p+2)}.
$$

Since $P(-iy)=\overline{P(iy)}$ and $m$ is even, substitution in (7) proves (21).

To prove strict positivity, set $s=x+1/2$, $t=y+1/2$. The kernel becomes

$$
K_m(s,t)=(1-|s-t|)^m-(s+t-1)^m,\qquad 0\le s,t\le1.
$$

Let $q_m(u)=(1-|u|)^m$ for $|u|\le1$ and zero otherwise, and let $Q_m$ be its periodization with period two. Evenness of $m$ gives

$$
K_m(s,t)=Q_m(s-t)-Q_m(s+t).
$$

Consequently the normalized sine functions $e_n(s)=\sqrt2\sin(n\pi s)$ diagonalize $K_m$, with eigenvalues

$$
\begin{aligned}
\lambda_{m,n}
&=2\int_0^1(1-u)^m\cos(n\pi u)\,du\\
&=\frac{2m}{(n\pi)^2}
\left[1-(m-1)\int_0^1(1-u)^{m-2}\cos(n\pi u)\,du\right]>0,
\qquad n\ge1. \tag{22}
\end{aligned}
$$

The second equality follows by two integrations by parts. The inequality is strict because $\cos(n\pi u)<1$ on a set of positive measure and the weight $(1-u)^{m-2}$ is positive on $(0,1)$. The integral in brackets is therefore strictly smaller than $1/(m-1)$.

The Fourier coefficients are $O_m(n^{-2})$, which justifies the uniformly convergent kernel expansion $K_m(s,t)=\sum_{n\ge1}\lambda_{m,n}e_n(s)e_n(t)$. Thus (21) is $3/(\pi^2m!)$ times

$$
\sum_{n\ge1}\lambda_{m,n}
\left|\int_0^1P\bigl(i(s-1/2)\bigr)e_n(s)\,ds\right|^2.
$$

Completeness of the sine basis and $P\ne0$ imply that this sum is strictly positive. $\square$

These results concern averages of Hardy's $Z$. They do not prove $\mathcal L_p[Z](t)\ge0$ at individual points. Theorem 6 tests only squares of linear derivative jets; it supplies no positivity against arbitrary nonlinear functions of the jet or arbitrary localizers in height. Section 6 allows a slowly growing sum of the Laguerre order and the filter degree. Passing to the entire xi-function also involves its gamma amplitude. These steps cannot be omitted in an application to RH.

There is also a direct explanation for this averaged positivity in terms of functions with real zeros. Define

$$
S_q(v)=\int_{-q/2}^{q/2}e^{ivx}\,dx=\frac{2\sin(qv/2)}v,
\qquad S_q(0)=q.
$$

The layer-cake identity $1-2r=\int_{2r}^1dq$, followed by Fourier inversion for the convolution of four compact interval densities, gives

$$
\frac3{\pi^2}\int_{\mathcal P}(1-2r)e^{i\sum_j a_jx_j}\,dx
=\frac3{2\pi^3}\int_0^1\int_{\mathbb R}\prod_{j=1}^4S_q(v+a_j)\,dv\,dq. \tag{23}
$$

The Fourier product is integrable, so (23) is an ordinary convolution-inversion identity. For fixed derivative orders, differentiation is justified by
$S_q^{(k)}(v)=q^{k+1}S_1^{(k)}(qv)$ and $S_1^{(k)}(v)=O_k((1+|v|)^{-1})$. In particular,

$$
\frac{H(\mathbf k)}{\pi^2}
=\frac3{2\pi^3(K+4)}\int_{\mathbb R}\prod_{j=1}^4S_1^{(k_j)}(v)\,dv. \tag{24}
$$

Each $S_q$, $q>0$, belongs to the Laguerre–Pólya class. Differentiating (23) thus expresses $B_p(P)$ as a positive multiple of
$\int_0^1\int_{\mathbb R}\mathcal L_p[S_q](v)[P(D)S_q(v)]^2\,dv\,dq$,
which also explains its nonnegativity. The sine spectrum (22) supplies strictness and the explicit quadratic form. Formula (23) describes the limiting fourth-moment functional; it is not a probability law determining the actual derivative jets of $Z$ from fourth moments.

## 6. Uniform positivity for growing orders and filter degrees

The fixed complex-shift uniformity of [1, Proposition 3], together with a quantitative lower bound for (21), gives a joint uniform statement. It is important here to use the shifted theorem directly; the unspecified derivative-order constants in (1) would not suffice.

**Theorem 7.** Write $L=\log T$, $C=2+\sqrt5$, and for $p\ge0$ and a real polynomial $P$ define

$$
\mathscr Q_{T,p}(P)=\frac1{TL^{2p+4}}\int_T^{2T}
\mathcal L_p[Z](t)W_{P,T}(t)^2\,dt.
$$

Uniformly in $p,d\ge0$ and every nonzero real polynomial $P$ of degree at most $d$,

$$
\mathscr Q_{T,p}(P)=B_p(P)\left[1+
O\left(\frac{(2p+1)4^p(2p)!(d+2)^6C^{2d}(d!)^2}{\log T}\right)\right]. \tag{25}
$$

The implied constant is absolute. In particular, for each fixed $0<\varepsilon<1/2$, all these integrals are strictly positive for sufficiently large $T$, simultaneously for

$$
p+d\le\left(\frac12-\varepsilon\right)
\frac{\log\log T}{\log\log\log T}. \tag{26}
$$

The order, polynomial and coefficients may depend on $T$ within this range.

**Proof.** We first justify a uniform analytic remainder. Write

$$
\mathcal A(a)=\frac3{\pi^2}\int_{\mathcal P}(1-2r)e^{i\sum_j a_jx_j}\,dx.
$$

On a neighborhood of a large positive real interval, Hardy's function has the analytic continuation
$Z(z)=e^{i\vartheta(z)}\zeta(1/2+iz)=e^{-i\vartheta(z)}\zeta(1/2-iz)$, with the local analytic gamma branch agreeing with the real Hardy phase. In [1, Proposition 3], set

$$
\alpha_1=ia_1/L,\quad\alpha_2=ia_2/L,\quad
\beta_1=-ia_3/L,\quad\beta_2=-ia_4/L.
$$

For $|a_j|\le2$ and $T\le t\le2T$, analytic Stirling estimates give the combined Hardy phase

$$
e^{i(\vartheta(t+a_1/L)+\vartheta(t+a_2/L)
-\vartheta(t+a_3/L)-\vartheta(t+a_4/L))}
=e^{i(a_1+a_2-a_3-a_4)/2}\bigl(1+O(L^{-1})\bigr).
$$

The phase-error integral is $O(TL^3)$ by Hölder: Proposition 3 with conjugate matching shifts bounds each required absolute fourth moment by $O(TL^4)$. Multiplying the source's main term by the displayed constant phase gives the exponential version of (4). The same compact changes of variables used in Lemma 2 therefore show that

$$
E_T(a):=\frac1{TL^4}\int_T^{2T}\prod_{j=1}^4Z(t+a_j/L)\,dt
-\mathcal A(a)=O(L^{-1}) \tag{27}
$$

uniformly on $|a_j|\le2$. This remainder is holomorphic on a neighborhood of that polydisc. Cauchy's estimate on circles $|a_j|=1$, followed by the finite Laguerre and filter sums, gives

$$
\begin{aligned}
|\mathscr Q_{T,p}(P)-B_p(P)|
&\le\frac{A(2p+1)}{L}\left(\sum_{j=0}^d|c_j|j!\right)^2\\
&\le\frac{A(2p+1)(d!)^2}{L}\|c\|_1^2. \tag{28}
\end{aligned}
$$

The factorials from the first two differentiated coordinates cancel the factorials in (16), leaving $2p+1$ terms. The constant $A$ is absolute, so this bound is uniform in all derivative orders.

We next bound the positive leading form below on polynomials. Put $m=2p+2$ and $f(s)=P(i(s-1/2))$. Rewriting (22) and restricting its integral to $[0,1/2]$ gives

$$
\lambda_{m,n}=\frac{2m(m-1)}{(n\pi)^2}
\int_0^1(1-u)^{m-2}(1-\cos(n\pi u))\,du
\ge\frac{c_m}{(n\pi)^2}, \tag{29}
$$

where $c_m=2m(m-1)2^{-(m-2)}(1/2-1/\pi)>0$. Hence

$$
B_p(P)\ge\kappa_p\|f\|_{H^{-1}_D(0,1)}^2,
\qquad\kappa_p=\frac{3c_m}{\pi^2m!}
=\frac{6(1/2-1/\pi)}{\pi^2 4^p(2p)!}, \tag{30}
$$

where the squared Dirichlet negative Sobolev norm is
$\sum_{n\ge1}|\langle f,e_n\rangle|^2/(n\pi)^2$.

Let $-u''=f$, $u(0)=u(1)=0$. Then $u$ is a polynomial of degree at most $d+2$, and $\|f\|_{H^{-1}_D}=\|u'\|_2$. Every polynomial $g$ of degree at most $D$ on $[0,1]$ satisfies

$$
\|g'\|_2\le(D+1)^2\|g\|_2. \tag{31}
$$

For completeness, expand in the orthonormal shifted Legendre polynomials
$\sqrt{2k+1}\,\mathrm P_k(2s-1)$. Their squared derivative norms are $2(2k+1)k(k+1)$, whose sum for $0\le k\le D$ is $D(D+1)^2(D+2)\le(D+1)^4$. Cauchy–Schwarz proves (31). Applying it to $u'$ yields

$$
\|f\|_{H^{-1}_D}^2\ge(d+2)^{-4}\|f\|_2^2. \tag{32}
$$

Finally, expand $P(ix)$ in the orthonormal Legendre basis on $[-1/2,1/2]$. The sum of the absolute monomial coefficients of $\mathrm P_k(2x)$ is at most $C^k$, where $C=2+\sqrt5$: the three-term recurrence bounds these sums by $b_{k+1}\le4b_k+b_{k-1}$, with $b_0=1$, $b_1=2$, and $C^2=4C+1$. Another application of Cauchy–Schwarz gives

$$
\|c\|_1\le(d+1)C^d\|f\|_2. \tag{33}
$$

Multiplication of the monomial coefficients by $i^j$ does not change their absolute values. Combining (30), (32), and (33),

$$
B_p(P)\ge\frac{\kappa_p\|c\|_1^2}
{(d+2)^4(d+1)^2C^{2d}}. \tag{34}
$$

Equations (28) and (34) prove (25). Put $N=p+d$ and $h=\log\log T$. Since $(2p)!(d!)^2\le(2N)!$ and $4^pC^{2d}\le C^{2N}$, the relative-error factor is at most a fixed polynomial in $N$ times $C^{2N}(2N)!/\log T$. For $N\le(1/2-\varepsilon)h/\log h$, its logarithm is at most $(-2\varepsilon+o(1))h$. It tends to minus infinity, proving (26). $\square$

The range (26) is not claimed to be optimal, and no practical height threshold is given. It controls all coefficients simultaneously in a growing family, but supplies no theorem that the resulting derivative squares can concentrate at a selected height. Thus it still does not imply a pointwise Laguerre inequality.

## 7. Positive averages in shorter smooth windows

Fix a nonnegative $w\in C_c^\infty((0,1))$ with $\int_0^1w(u)\,du=1$, and put
$w_{X,H}(t)=w((t-X)/H)$. This height weight is separate from the derivative filter $W_{P,T}$.

**Theorem 8.** Let $L=\log T$, $T\le X\le2T$, and $T^{3/4}\le H\le T$. Write

$$
R_{p,d}=(2p+1)4^p(2p)!(d+2)^6(2+\sqrt5)^{2d}(d!)^2.
$$

For every fixed $0<\sigma<1/4$, uniformly in $X,H,p,d$ and every nonzero real polynomial $P$ of degree at most $d$,

$$
\frac1{HL^{2p+4}}\int_{\mathbb R}w_{X,H}(t)
\mathcal L_p[Z](t)W_{P,T}(t)^2\,dt
=B_p(P)\left[1+O_{w,\sigma}\left(R_{p,d}
\left\{\frac1L+\frac{T^{3+\sigma}}{H^{13/4}L^4}\right\}\right)\right]. \tag{35}
$$

Consequently, for fixed $0<\delta<1/13$ and $0<\varepsilon<1/2$, these integrals are strictly positive for all sufficiently large $T$, simultaneously for every center $X\in[T,2T]$, every

$$
T^{12/13+\delta}\le H\le T,\qquad
p+\deg P\le\left(\frac12-\varepsilon\right)
\frac{\log\log T}{\log\log\log T}, \tag{36}
$$

and every nonzero real $P$, with coefficients allowed to depend on $T,X,H$.

**Proof.** Apply [7, Theorem 1.1] with twist parameters $h=k=1$ and smoothing scale $T_0=H$. Our weight is supported in $[T/2,4T]$ and satisfies $w_{X,H}^{(j)}\ll_{w,j}H^{-j}$. The theorem gives a sum of six main terms and the uniform complex-shift error

$$
E\ll_{w,\sigma}T^{3/4+\sigma}(T/H)^{9/4}.
$$

Use the four shifts $ia_1/L,ia_2/L,-ia_3/L,-ia_4/L$ as in Theorem 7. The sum of its six main terms, after multiplying by the constant Hardy phase, is
$L^4\mathcal A(a)+O(L^3)$ uniformly for bounded complex $a$ and $t\in[T/2,4T]$.

Here is a justification that retains uniformity when shifts coincide. First place the four $a_j$ on circles of distinct fixed radii enclosing the desired polydisc. Every pairwise difference stays away from zero. In each of the six terms, use
$\zeta(1+v/L)=L/v+O(1)$, $1/\zeta(2+O(1/L))=1/\zeta(2)+O(1/L)$, and $\log(t/(2\pi))/L=1+O(1/L)$. The error is $O(L^3)$. The complete six-term sum is holomorphic by the pole cancellation in [7]; the maximum principle extends the estimate inside the polydisc. Its leading holomorphic function agrees with $\mathcal A$: for a fixed smooth dyadic weight, partial integration of (1) identifies every fixed derivative at zero with $H(\mathbf k)/\pi^2$, as does (7). Equality follows from analyticity. This identification does not sum derivative error bounds.

The analytic Hardy phase differs from its constant approximation by $O(L^{-1})$. Hölder and the same localized theorem with conjugate matching shifts bound the integral of the absolute product by $O(HL^4+E)$. Thus the phase error is $O(HL^3+E/L)$, and

$$
\frac1{HL^4}\int_{\mathbb R}w_{X,H}(t)
\prod_{j=1}^4Z(t+a_j/L)\,dt-\mathcal A(a)
\ll_{w,\sigma}\frac1L+\frac{T^{3+\sigma}}{H^{13/4}L^4} \tag{37}
$$

on $|a_j|\le2$. The remainder is holomorphic. Applying the four-variable Cauchy estimate and then (34), exactly as in (28), proves (35). In particular, the phase error was bounded on the local window itself.

For (36), choose $\sigma<\min(1/4,13\delta/4)$. The second term in braces in (35) is $O(T^{-c_\delta}/L^4)$ for some $c_\delta>0$. The Stirling argument following (34) now applies unchanged. $\square$

The exponent $12/13$ comes from the stated general error bound in [7]; no optimal local scale is claimed. Theorem 8 concerns smooth weights. A sharp-cutoff conclusion cannot be obtained by sandwiching this signed integrand. These windows remain much too long to isolate an individual zero or to yield a pointwise Laguerre inequality.

## 8. Exact checks and reproducibility

The proof is analytic and does not depend on numerical experiments. The supplement includes four short CPU-only exact-algebra controls implemented in Python with SymPy.

`hardy246_octahedron_control.py` evaluates the original paired polynomial integral (4) and independently integrates on the octahedron. Six prescribed examples agree as exact rational numbers:

| $(k,l,m,n)$ | $H(k,l,m,n)$ |
|---|---:|
| $(0,0,0,0)$ | $1/2$ |
| $(1,1,1,1)$ | $1/1120$ |
| $(2,1,1,0)$ | $-1/3360$ |
| $(4,1,1,0)$ | $1/40320$ |
| $(3,3,1,1)$ | $19/1774080$ |
| $(6,4,0,0)$ | $-3/931840$ |

`hardy247_parity_identity.py` applies all 16 coordinate sign substitutions directly to (10), constructs the common denominator from the transformed factors, and verifies the polynomial identity (11). It does not insert the closed projection formulae (12)–(13). The supplement gives the commands and saved exact outputs. No parameter survey or floating sign test is used to support the all-order theorem.

`hardy248_laguerre_constants.py` independently expands (16) using the original paired integral and checks (18) at $(p,q)=(1,1)$ and $(1,2)$, obtaining $\pi^2C_{1,1}=1/336$ and $\pi^2C_{1,2}=1/10800$ exactly.

`hardy249_filtered_laguerre_control.py` compares two independent evaluations of (21): expansion through the original paired integral, and polynomial integration of the kernel on the two triangles of its square. For $p=1$, $P(z)=1+z+2z^2$, both give $\pi^2B_p(P)=211/7560$. For $p=2$, $P(z)=1-2z+z^3$, both give $10434929/9686476800$. These mixed-parity checks verify constants; the all-filter positivity follows from (22).

## 9. Scope

The result settles the sign and nonvanishing question for the constants in [1, Conjecture 1], using their unconditional arithmetic moment formula. Its proof explains the signs through an exact recurrence and a zero-sum symmetry. The explicit Laguerre kernel also gives positivity uniformly over the slowly growing sum of orders and filter degrees in Theorem 7, with the local smooth-window extension in Theorem 8 obtained from [7]. None of these averages determines signs at individual heights, the location of every zeta zero, or the Riemann hypothesis.

## References

[1] H. M. Bui and R. R. Hall. *On the derivatives of Hardy's function $Z(t)$*. 2023, arXiv:2304.05178v1. https://arxiv.org/abs/2304.05178v1

[2] R. R. Hall. *Some Four Dimensional Definite Integrals Arising from Zeta-Function Theory*. Computational Methods and Function Theory **12** (2012), 565–583. https://doi.org/10.1007/BF03321845

[3] J. P. Keating and F. Wei. *Joint moments of higher order derivatives of CUE characteristic polynomials I: asymptotic formulae*. 2023, arXiv:2307.01625v2. https://arxiv.org/abs/2307.01625v2

[4] T. Assiotis, M. A. Gunes, J. P. Keating and F. Wei. *Exchangeable arrays and integrable systems for characteristic polynomials of random matrices*. 2024, arXiv:2407.19233v3. https://arxiv.org/abs/2407.19233v3

[5] G. Csordas. *Fourier transforms of positive definite kernels and the Riemann $\xi$-function*. 2014, arXiv:1309.0055v2. https://arxiv.org/abs/1309.0055v2

[6] H. Kösters. *On the occurrence of the sine kernel in connection with the shifted moments of the Riemann zeta function*. Journal of Number Theory **130** (2010), 2596–2609. arXiv:0803.1141v2. https://arxiv.org/abs/0803.1141v2

[7] C. P. Hughes and M. P. Young. *The twisted fourth moment of the Riemann zeta function*. Journal für die reine und angewandte Mathematik **641** (2010), 203–236. arXiv:0709.2345v2. https://arxiv.org/abs/0709.2345v2

[8] Orchard. *A coefficient proof of the Bui–Hall sign conjecture*. Research artifact with displayed draft date 13 September 2026, reproduced in *Math research case study*; retrieved 20 October 2026. https://orchardai.ai/research/math/artifacts/587708dd341c2e51d0a4299f5742827ae9df61081a7332abdefd57771002af71/hardy-sign-proof.md

[9] Orchard. *A sharp positive factorization and explicit Hardy-moment bounds*. Research artifact with displayed draft date 14 September 2026, reproduced in the same case study; retrieved 20 October 2026. https://orchardai.ai/research/math/artifacts/bac6ab41c3eaff2fff9e75b7ccaddabc141d121f05c46389d25145005c3287cc/sharp-factorization.md

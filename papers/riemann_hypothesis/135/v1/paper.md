# Eventual central zeros at every fixed depth of heated theta branching

## 1. The result and its role

The Biane–Pitman–Yor theta law has Mellin transform $2\xi(2s)$ and is a fixed point of a binary smoothing transformation [1]. Applying that transformation repeatedly to a logarithmically heated theta law gives a natural family of positive approximants. The difficulty is to control their Mellin zeros. The first branching image has eventual simple central zeros at every fixed positive heat [2]. We prove the same conclusion at every fixed finite depth, directly from the complete source.

The main device is to flatten the nested Barnes integrals into a single integral over the original leaves. The internal Gamma factors cancel. This makes it possible to expand the complete heated source to sufficiently high accuracy before any oscillatory integration, retain every scale endpoint, and separate the contributions by their total heat deficit. A dyadic arithmetic–geometric mean inequality gives a positive deficit independent of depth for every nonprincipal inverse-frequency action. The constants in the resulting asymptotic are not uniform in depth.

Write

$$
q=\frac12,\qquad
\xi(z)=\frac12z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z).
\tag{1}
$$

Let $f_*$ be the positive probability density satisfying

$$
\begin{aligned}
\int_0^\infty u^s f_*(u)\,du&=2\xi(2s),\\
f_*(u)&=\sum_{m\geq1}(4\pi^2m^4u-6\pi m^2)e^{-\pi m^2u}
\quad(u\geq1),\\
f_*(1/u)&=u^{5/2}f_*(u).
\end{aligned}
\tag{2}
$$

For $b>0$, put

$$
f_b(u)=Z_b^{-1}e^{b(\log u)^2}f_*(u),\qquad
Z_b=\int_0^\infty e^{b(\log u)^2}f_*(u)\,du.
\tag{3}
$$

Let $U_0$ have density $f_b$. Inductively define

$$
U_{n+1}=\frac{U_{n,1}}{W_1^2}+\frac{U_{n,2}}{W_2^2},\qquad
M_n(s)=\mathbb E U_n^s,\qquad S_n(s)=M_n(s)+M_n(q-s),
\tag{4}
$$

where the two copies of $U_n$ and the two uniform $[1,2]$ variables are independent. At every finite depth all real positive and negative moments exist. Indeed a finite tree is a sum of finitely many positive leaves with weights bounded above and below by positive constants. Its Mellin transform is entire. The symmetry relevant to zeros is the exact identity

$$
S_n(q-\overline{s})=\overline{S_n(s)}.
\tag{5}
$$

Set $N=2^n$ and define

$$
\begin{aligned}
A(s)&=2s(2s-1)\pi^{-s}\Gamma(s),\\
D_n(s)&=Z_b^{-N}A(s)
 \exp\left[Nb\operatorname{Log}^2\frac{s+(N-1)/2}{N\pi}\right],\\
a_{0,0}&=1,\qquad
a_{n+1,j}=\left(a_{n,j}-\frac12a_{n,j-1}\right)^2,\\
R_n(x)&=\sum_{j=0}^n a_{n,j}x^j,\qquad
P_n(s)=R_n(2\,4^{-s}),\qquad E_n(s)=D_n(s)P_n(s).
\end{aligned}
\tag{6}
$$

Missing coefficients in the recurrence are zero. Logarithms in the high strips below are principal branches. The first coefficient vectors are

$$
(1,1/4),\qquad (1,1/16,1/64),\qquad
(1,49/256,1/4096,1/16384).
\tag{7}
$$

**Theorem 1.** Fix $b>0$ and an integer $n\geq1$. For every compact interval $K\subset(0,q)$, uniformly for $\operatorname{Re}s\in K$ and $T=|\operatorname{Im}s|\longrightarrow\infty$,

$$
S_n(s)=E_n(s)+E_n(q-s)
 +O_{b,n,K}\left((\log T)^{-(N-1)/2}
       (|D_n(s)|+|D_n(q-s)|)\right).
\tag{8}
$$

Moreover $|P_n(s)-1|<0.563$ for $\operatorname{Re}s\geq0$. For every $0<\varepsilon<1/4$ there is a finite $T_{b,n,\varepsilon}$ such that every zero of $S_n$ in

$$
\varepsilon\leq\operatorname{Re}s\leq q-\varepsilon,
\qquad |\operatorname{Im}s|\geq T_{b,n,\varepsilon},
\tag{9}
$$

is simple and lies on $\operatorname{Re}s=1/4$.

The theorem supplies a complete-source composition result, rather than a formal recurrence for leading terms. It does not control bounded-height zeros, give an effective starting height, or give a threshold uniform in $n$ or $b$. In particular it does not prove RH. The growing-depth, moving-heat limits of [3] require zero control on compact sets; (8) does not supply that control.

## 2. Prior work and the distinction

The law (2), its theta identities, and its binary smoothing fixed-point description are due to Biane, Pitman and Yor [1, Section 3.3]. They are not new here. Logarithmic heating becomes the classical de Bruijn heat operation in logarithmic coordinates [4]. Eventual real zeros of the heated theta transform itself are also classical [5,6]. Those results concern the seed, whereas (8) concerns each finite nonlinear branching iterate of that seed.

The one-step complete-source theorem [2] already retains the two endpoints, theta modes, both Mellin frequency branches, and Barnes residues. Its Section 7 identifies further-depth composition as missing. An $o(1)$ one-step remainder cannot simply be inserted into the next Barnes integral: absolute integration loses a power of height. The formal square recurrence in (6) and its elementary coefficient bound are not claimed as new algebra. The new argument derives that recurrence from all endpoint assignments of the exact full tree and proves the complete asymptotic by finite-dimensional estimates at the original leaves.

The large-heat theorem [3] gives noncentral zeros of the first image for sufficiently large heat, with the zero held in a fixed compact set while heat grows. It is compatible with (9), which fixes heat before height tends to infinity. Fixed points of other shot-noise transformations, including theta-related examples, were studied by Iksanov and Kim [7]; their Poisson transformation and fixed-point results do not give the finite binary branching Mellin-zero theorem here.

The Gamma expansions and Barnes beta integrals are classical [8], as is the stationary-phase theorem [9, Theorem 7.7.5]. We state the needed parameter bounds explicitly. No novelty is claimed for those general tools. The proof uses no numerical zero search.

## 3. An arbitrary-accuracy expansion of the complete seed

Put $G_b=Z_bM_0$. A real Gaussian integral and Fubini give

$$
G_b(z)=\frac1{\sqrt{4\pi b}}\int_{\mathbb R}
 e^{-x^2/(4b)}2\xi(2z+2x)\,dx.
\tag{10}
$$

Absolute integrability follows from (2): for fixed real $\sigma$ the corresponding majorant is $G_b(\sigma)$. Thus (10) is an entire identity. The functional equation gives the exact value decomposition

$$
\begin{aligned}
G_b(z)&=I_b(z)+I_b(q-z),\\
I_b(z)&=\frac1{\sqrt{4\pi b}}
 \int_{1/4-\operatorname{Re}z}^{\infty}
 e^{-x^2/(4b)}2\xi(2z+2x)\,dx.
\end{aligned}
\tag{11}
$$

These pieces have a moving real cutoff; they are not asserted to be individually holomorphic. We only estimate their values. Derivatives will be taken solely of the explicit finite expressions below.

**Lemma 2.** Fix $b>0$, a compact real interval $K_0$, and $R>0$. There exist finite integers $J,L$ such that, uniformly for $\operatorname{Re}z\in K_0$ and $T=|\operatorname{Im}z|\longrightarrow\infty$,

$$
I_b(z)=A(z)\sum_{m=1}^Jm^{-2z}e^{bL_m(z)^2}
 \sum_{k=0}^{L-1}z^{-k}Q_{k,b}(L_m(z))
 +O\left(T^{-R}|A(z)e^{b\operatorname{Log}^2(z/\pi)}|\right),
\tag{12}
$$

where

$$
L_m(z)=\operatorname{Log}(z/\pi)-2\log m,
\qquad Q_{0,b}=1,\qquad Q_{1,b}(L)=2b^2L^2+3bL+b.
\tag{13}
$$

Each $Q_{k,b}$ is a polynomial. One can take any fixed $J$ with $4b\log(J+1)>R$, and then sufficiently large $L$.

*Proof.* Choose a fixed positive $C_0$ with $\operatorname{Re}(z+x)>1$ for $x\geq C_0$. On the bounded part of (11) below $C_0$, the usual polynomial vertical bound for zeta and Stirling give $e^{-\pi T/2}T^C$. Its ratio to the scale in (12) is $\exp(-b\log^2T+O(\log T))$, smaller than every fixed negative power.

On $C_0\leq x\leq\log^2T$, logarithmic Stirling, including the two linear factors in $A$, gives to any fixed order

$$
\frac{A(z+x)}{A(z)}
 =e^{x\operatorname{Log}(z/\pi)}
 \left(\sum_{k=0}^{L-1}z^{-k}p_k(x)
       +O(T^{-L}(1+x)^{C_L})\right).
\tag{14}
$$

The polynomials arise by expanding the Bernoulli-polynomial coefficients of the log-Gamma ratio and then exponentiating. The logarithmic remainder is uniform on this window, since $x/T\to0$; its polynomial dependence on $x$ is absorbed by $C_L$. In particular $p_0=1$ and $p_1(x)=x(x+3)/2$. Gaussian integration of $p_k(x)e^{xL}$ over the full real line gives $e^{bL^2}Q_{k,b}(L)$. Taking $L>R$ with a fixed margin pays all powers of $\log T$ from the error in (14).

In the absolutely convergent Dirichlet region,

$$
\left|\zeta(2z+2x)-\sum_{m=1}^Jm^{-2z-2x}\right|
 \leq C_J(J+1)^{-2x}.
\tag{15}
$$

Use the exact ratio envelope
$|A(z+x)/A(z)|\leq C\exp(x\log(T/\pi)+C(x+x^2)/T)$
for this entire omitted tail. Completing the Gaussian square bounds its integral, relative to the leading heat, by $O(T^{-4b\log(J+1)})$; the perturbation $C(x+x^2)/T$ changes this by a bounded factor tending to one. The imaginary part of $L_m$ is bounded, so replacing a complex Gaussian integral by its absolute majorant costs only a fixed factor. Extending each retained polynomial integral below $C_0$ costs the same superpolynomially small term as above.

Finally $x>\log^2T$ is negligible. Up to $T/2$, the Gaussian dominates $\exp(x\log T+Cx^2/T)$; beyond $T/2$, it dominates $\exp(C(T+x)\log(T+x))$. These bounds also pay for the upper extensions of the retained Gaussian integrals. The chosen $J,L$ establish (12). Conjugation handles negative height. $\square$

The finite sum (12) must not be extended to an infinite sum of saddle terms: at fixed $z$ its factor $e^{4b\log^2m}$ prevents such a summation. The discarded infinite source is controlled by (15), before it enters a tree integral.

## 4. Exact flattening, including the residue terms

Define the entire scale factor

$$
\alpha(s)=\int_1^2 w^{-2s}\,dw
 =\frac{2\,4^{-s}-1}{1-2s}.
\tag{16}
$$

For $0<\operatorname{Re}s<1$ and $c=\operatorname{Re}s/2$, the complete Barnes identity is

$$
M_{j+1}(s)=2\alpha(s)M_j(s)
 +\frac1{2\pi i\Gamma(-s)}\int_{(c)}
  \Gamma(-z)\Gamma(z-s)\alpha(z)\alpha(s-z)
  M_j(z)M_j(s-z)\,dz.
\tag{17}
$$

The two residues are the two individual child moments. For example, one obtains (17) by continuing the scalar Barnes formula for $(x+y)^s$ from $\operatorname{Re}s<c<0$ to $0<c<\operatorname{Re}s<1$; the crossed poles contribute $x^s+y^s$. Expectation is justified by finite moments and absolute Gamma decay. This is the same complete formula used in [2].

Take the full binary tree of depth $n$, with leaves $1,\ldots,N$. For a nonroot node $v$, let $I_v$ denote its descendant leaves and set $s_v=\sum_{i\in I_v}w_i$. Impose

$$
\sum_{i=1}^Nw_i=s,\qquad \operatorname{Re}w_i=\frac{\sigma}{N},
\qquad \sigma=\operatorname{Re}s\in(0,q).
\tag{18}
$$

**Lemma 3.** Choosing the integral term at every vertex in (17) gives exactly

$$
F_n(s)=\frac1{\Gamma(-s)(2\pi i)^{N-1}}
 \int \prod_{i=1}^N\bigl[\Gamma(-w_i)M_0(w_i)\bigr]
       \prod_{v\ne\mathrm{root}}\alpha(s_v)
       \,dw_1\cdots dw_{N-1}.
\tag{19}
$$

Every other term in the finite expansion of $M_n$ is a pruned-tree integral with $L<N$ heated seed leaves. Uniformly on fixed compact real substrips, the sum of these other terms is smaller than $|D_n(s)|+|D_n(q-s)|$ by every fixed negative power of $T$.

*Proof.* Insert the two child integrals repeatedly. At each internal node, the child's denominator $\Gamma(-s_v)$ cancels the matching factor from its parent. The node-to-leaf linear change of variables has Jacobian one. The surviving factors are exactly (19).

For Fubini, Lemma 2 gives on every required positive leaf line

$$
|\Gamma(-w)M_0(w)|
 \leq C e^{-\pi|\operatorname{Im}w|}
 (1+|\operatorname{Im}w|)^C
 e^{b\log^2(2+|\operatorname{Im}w|)}.
\tag{20}
$$

The scale factors are bounded on each fixed real line by their defining integral (16). The product of (20) is integrable on the leaf hyperplane. This justifies the changes of integration order directly from the complete leaves.

A residue choice is a unary vertex with factor $2\alpha$. The remaining binary vertices still have the same cancellation, but the pruned tree has $L<N$ leaves. Their positive real parts need not be equal. A bound of the form (20) holds at each of them; repeated unary factors are bounded. Write $s=\sigma+iT$, $T>0$, and

$$
r=\frac12\left(\sum_{i=1}^L|t_i|-T\right)\geq0,
\qquad t_i=\operatorname{Im}w_i.
\tag{21}
$$

After division by $\Gamma(-s)$, the Gamma exponential is $e^{-\pi T/2}e^{-2\pi r}$. For $r\leq T$, all $|t_i|\leq2T$, and the absolute integral is at most

$$
e^{-\pi T/2}\exp\left(Lb\log^2T+O(\log T)\right).
\tag{22}
$$

Here polynomial factors and volume have been absorbed in $O(\log T)$. For $r>T$, the extra exponential dominates $\exp(C\log^2r)$ and all powers, giving a still smaller bound after integration. Comparing (22) with the $N$-heat scale yields $\exp(-(N-L)b\log^2T+O(\log T))$. A one-leaf term has no remaining integral and obeys the same comparison. This proves the assertion. $\square$

## 5. Complete source errors and the simplex faces

We now work with (19), replacing $M_0$ by $G_b$ and restoring the factor $Z_b^{-N}$ at the end. Enlarge $K$ if needed to contain $q-K$. Write $w_i=\sigma/N+it_i$ and

$$
\beta=\frac12-\frac{2\sigma}{N}>0.
\tag{23}
$$

The exact leaf identities

$$
\begin{aligned}
\Gamma(-w)\alpha(w)A(w)
 &=\frac{2\pi(2\,4^{-w}-1)\pi^{-w}}{\sin\pi w},\\
\Gamma(-w)\alpha(w)A(q-w)
 &=(4-2\,4^w)\pi^w\Gamma(1-2w)
\end{aligned}
\tag{24}
$$

and Lemma 2 imply

$$
|\Gamma(-w_i)\alpha(w_i)G_b(w_i)|
 \leq C e^{-\pi|t_i|}(1+|t_i|)^\beta
       \exp\left[b\log^2\frac{1+|t_i|}{\pi}\right].
\tag{25}
$$

The inverse branch has power $\beta$ and the forward branch power zero. Compactness supplies (25) at bounded height. Internal nonroot scale factors are still present in (19).

Fix $1/2<\delta<1$. If the exterior mass $r$ in (21) exceeds $T^\delta$, its additional factor $e^{-2\pi r}$ makes the integral negligible to every fixed power relative to the $N$-heat scale. For $T^\delta<r\leq T$, this follows already from $e^{-2\pi T^\delta}$ against $e^{O(\log^2T)}$; for $r>T$, use the integrable exponential tail as in Lemma 3.

If $r\leq T^\delta$ and any $|t_i|\leq T^\delta$, all other heights are at most $T+T^\delta$. The heat product is then bounded by

$$
\exp\left[b(N-1+\delta^2)\log^2T+O(\log T)\right].
\tag{26}
$$

Compared with $\exp(Nb\log^2(T/(N\pi)))$, this has a strict log-squared deficit, paying every polynomial, volume and scale-factor cost. A negative $t_i$ with $r\leq T^\delta$ belongs to this small-face case. We may therefore restrict to

$$
t_i\geq T^\delta,\qquad \sum_i t_i=T,
\qquad \theta_i=t_i/T.
\tag{27}
$$

All removals so far use the complete envelope, without differentiating a source remainder.

For an internal nonroot node, put $\theta_v=\sum_{i\in I_v}\theta_i$. Its denominator satisfies $|1-2s_v|\geq2T\theta_v$. Consequently the remaining simplex weight is

$$
W_\beta(\theta)=
 \frac{\prod_i\theta_i^\beta}
      {\prod_{v\text{ internal, nonroot}}\theta_v}.
\tag{28}
$$

It is integrable, including intersections of faces. In fact its integral $I_N(\beta)$ over the simplex obeys

$$
I_1(\beta)=1,\qquad
I_{2k}(\beta)=I_k(\beta)^2B(k\beta+1,k\beta+1),
\qquad I_N(0)=1.
\tag{29}
$$

To see the recurrence, let $r$ be the mass of the left $k$-leaf subtree. Its leaf powers, internal denominators, its root denominator when present, and its $(k-1)$-dimensional volume give net power $r^{k\beta}$. The right subtree gives $(1-r)^{k\beta}$. The formula also holds for $k=1$, when there is no child-root denominator.

Let $h(t)=b\log^2(t/\pi)$. It is concave for all the heights in (27), once $T$ is large. Thus $\sum_i h(t_i)\leq Nh(T/N)$. Counting the powers in the absolute full-tree integral gives an excess of precisely $(N-1)/2$ over the inverse saddle scale:

$$
N\beta-(N-2)+(N-1)+(\sigma+1/2)-(2-\sigma)
 =\frac{N-1}{2}.
\tag{30}
$$

The four contributions before the subtraction are the leaf powers, the internal denominators, the volume, and $1/\Gamma(-s)$. In this comparison

$$
|A(q-s)|\asymp e^{-\pi T/2}T^{2-\sigma},\qquad
|A(s)|\asymp e^{-\pi T/2}T^{\sigma+3/2}.
\tag{31}
$$

The modulus of either canonical heat factor in (6) is comparable to $e^{Nh(T/N)}$, with fixed parameters.

Now choose the accuracy $R$ in Lemma 2 so that

$$
\delta R>\frac{N+1}{2}.
\tag{32}
$$

Each product containing a discarded seed remainder has the envelope (25) times $O(T^{-\delta R})$. The finite retained expressions obey the same envelope with a fixed constant. Equations (29)–(32) therefore bound the full source-remainder contribution by $O(T^{-1})$ relative to the inverse scale. Products with more remainders only improve the bound. This pays the entire omitted theta sum before stationary phase.

There is a useful further simplification. We can restrict (27) to a fixed compact simplex $\theta_i\geq\eta>0$, at any prescribed negative power cost. If some $\theta_i\leq\eta<1/N$, concavity maximizes the heat product at that coordinate equal to $\eta$ and all others equal to $(1-\eta)/(N-1)$. Its log ratio to the canonical heat is

$$
2b\log T\left[
 \log(N\eta)+(N-1)\log\frac{N(1-\eta)}{N-1}
 \right]+O_{b,N,\eta}(1).
\tag{33}
$$

The bracket tends to minus infinity as $\eta\downarrow0$. The integrable weight (28) then pays the faces, even after the loss (30). Choose $J,L$ first, then $\eta$ small enough both for this bound and to include every retained stationary point. There are finitely many such points. Smooth fixed cutoffs can be used; their transition regions satisfy (33). This avoids integration by parts at moving or singular simplex faces.

## 6. The inverse sector and the total heat deficit

For a retained inverse leaf of mode $m$, the second identity in (24) is multiplied by

$$
m^{2w-1}\exp\left[b\operatorname{Log}^2\frac{q-w}{\pi m^2}\right]
\tag{34}
$$

and by a finite correction symbol from (12). Splitting its numerator gives actions $m\sqrt\pi$ and $2m\sqrt\pi$, with coefficients $4/m$ and $-2/m$. Splitting every internal numerator in (16) gives coefficient $-1$ or $2$, with the latter dividing each descendant action by two.

Thus, for one full-tree mode and endpoint assignment,

$$
a_i=\sqrt\pi\,m_i e_i2^{-h_i},\qquad e_i\in\{1,2\},
\tag{35}
$$

where $h_i$ counts upper-endpoint choices at internal nonroot ancestors. The internal denominators remain as an amplitude. Denote $A_{\mathrm{tot}}=\sum_i a_i$.

The exact unweighted multivariate beta integral is

$$
\begin{aligned}
J_N(s;a)&=\frac1{(2\pi i)^{N-1}}\int
 \prod_{i=1}^N\Gamma(1-2w_i)a_i^{2w_i}\,
 dw_1\cdots dw_{N-1}\\
&=\frac{\prod_i a_i}{2^{N-1}}
 A_{\mathrm{tot}}^{2s-N}\Gamma(N-2s).
\end{aligned}
\tag{36}
$$

It follows by iterating the ordinary beta Barnes identity, or by setting $v_i=1-2w_i$ in its multivariate version. Each independent differential supplies a factor $1/2$. All $\operatorname{Re}v_i$ are positive on (18).

On the compact physical simplex from Section 5, the phase of the inverse Gamma factors, up to a common term, is $T\Phi(\theta)$, with

$$
\Phi(\theta)=-2\sum_i\theta_i\log\theta_i
                  +2\sum_i\theta_i\log a_i.
\tag{37}
$$

It has the unique critical point

$$
\theta_i^*=\frac{a_i}{A_{\mathrm{tot}}}.
\tag{38}
$$

In the first $N-1$ coordinates its Hessian is
$-2\operatorname{diag}(1/\theta_1,\ldots,1/\theta_{N-1})-(2/\theta_N)\boldsymbol{1}\boldsymbol{1}^{\mathsf T}$.
It is negative definite, with determinant magnitude $2^{N-1}/\prod_i\theta_i$.

Here is the amplitude control needed for stationary phase. Factor out the canonical inverse heat

$$
H_n^-(s)=\exp\left[Nb\operatorname{Log}^2\frac{N/2-s}{N\pi}\right].
\tag{39}
$$

At the original contour point $w_i=\sigma/N+iT\theta_i$, put $\ell_i=\log(N\theta_i/m_i^2)$. Uniformly on a fixed compact simplex, the normalized heat product equals

$$
\exp\left(2bL\sum_i\ell_i+b\sum_i\ell_i^2\right)
 \left(1+O(\log T/T)\right),\qquad
L=\operatorname{Log}\frac{N/2-s}{N\pi}.
\tag{40}
$$

The same expansion can be differentiated to any fixed order there, since it involves only explicit logarithms away from zero. By AM–GM,

$$
\sum_i\log\frac{N\theta_i}{m_i^2}\leq0.
\tag{41}
$$

Consequently the normalized heat and each fixed number of its derivatives are bounded by a power of $\log T$. The fixed factor $\exp(b\sum\ell_i^2)$ is bounded on the compact simplex. After removing $T^{-(N-2)}$, the internal denominators have uniformly smooth rational expansions. A seed correction of total order $k$ contributes $T^{-k}$ times polylogarithmic derivative bounds. Uniform Stirling has analogous bounds after any fixed number of terms.

The ordinary stationary-phase remainder estimate [9] therefore applies to a family of amplitudes with polylogarithmic seminorms. In dimension $d=N-1$, after $r$ terms its absolute remainder is $O(T^{-d/2-r}(\log T)^C)$ times the extracted common scale. On the complement of a fixed critical-point neighborhood, the phase gradient is bounded away from zero, and repeated integration by parts gives any prescribed fixed power saving. All cutoffs have fixed compact support; Section 5 already bounded their removed portions. No derivative of a discarded source error is used.

The normalization can also be checked locally, without making an unweighted face estimate. Put $\alpha=1-2\sigma/N$. Multiplying the $N$ leading Stirling factors, the measure $T^{N-1}/(2\pi)^{N-1}$, and the stationary factor $(2\pi/T)^{(N-1)/2}e^{-i\pi(N-1)/4}/\sqrt{|\det\Phi''|}$ gives modulus prefactor

$$
\sqrt{2\pi},2^{1/2-2\sigma}T^{N-2\sigma-1/2}e^{-\pi T}
 \frac{\prod_i a_i}{A_{\mathrm{tot}}^{N-2\sigma}},
$$

with phase $-2T\log(2T/A_{\mathrm{tot}})+2T-\pi(N-2\sigma-1/2)/2$. These are exactly the leading Stirling modulus and phase of the right side of (36). Thus the leading weighted term is normalized by (36), with the heat and internal denominators evaluated at the original real-contour saddle.

At (38), define the total heat deficit

$$
\begin{aligned}
d(a,m)&=-2b\sum_i\log\frac{N\theta_i^*}{m_i^2}\\
&=2b\left[-\sum_i\log(N\theta_i^*)+2\sum_i\log m_i\right]\geq0.
\end{aligned}
\tag{42}
$$

The leading normalized heat has size $O(T^{-d(a,m)})$. Its derivatives at the saddle retain this power, times logarithms, so the higher stationary coefficients do also. The generic remainder can independently be made $O(T^{-1}(\log T)^C)$ relative to the inverse stationary scale, using the global seminorm bounds above. We do not need a relative expansion uniform over vanishing saddle amplitudes.

**Lemma 4.** The deficit is zero precisely when all $m_i=1$ and all $a_i$ are equal. Every other assignment satisfies

$$
d(a,m)\geq 2b\log(9/8).
\tag{43}
$$

If any mode exceeds one, the stronger bound $d(a,m)\geq4b\log2$ holds.

*Proof.* Equality in (41) requires equality in AM–GM and all $m_i=1$. If some $m_i\geq2$, its mode contribution in (42) proves the second bound. Otherwise the actions are dyadic multiples of $\sqrt\pi$. If they are not equal, their maximum-to-minimum ratio is at least two. Replace this extreme pair by two copies of its arithmetic mean. Their sum is unchanged and their product increases by at least $9/8$, since

$$
\frac{(a_{\max}+a_{\min})^2}{4a_{\max}a_{\min}}\geq\frac98.
\tag{44}
$$

AM–GM applied to the modified list gives
$ (A_{\mathrm{tot}}/N)^N/\prod_i a_i\geq9/8$.
Inserting this into (42) proves (43). $\square$

The bound (43) concerns the total inherited source deficit. It avoids trying to compare nearby effective actions at just one recursive vertex. It does not control how many terms occur or the constants of their stationary expansions.

It follows that every nonprincipal inverse assignment contributes a positive power saving, up to finite logarithmic factors. Nonzero seed correction orders have an additional inverse power of $T$. Only the zero-order, equal-action, all-mode-one assignments contribute to the leading term.

## 7. Principal normalization and endpoint aggregation

For an equal-action assignment write $a_i=2^k\sqrt\pi$, and let $c_{\mathrm{end}}$ be the signed product of its leaf coefficients $4$ or $-2$ and internal numerator coefficients $-1$ or $2$. Its saddle is exactly $w_i=s/N$. Hence the heat is (39), and the internal denominator values are

$$
\prod_{d=1}^{n-1}(1-2s/2^d)^{-2^d}.
\tag{45}
$$

The product of (36), (45), and $1/\Gamma(-s)$ is exactly

$$
2^{2-3N}A(q-s)\,4^{(n-1+k)s}Q_n(s),\qquad
Q_n(s)=
 \frac{\prod_{j=2}^{N-1}(j-2s)}
      {\prod_{d=1}^{n-1}(2^d-2s)^{2^d}}.
\tag{46}
$$

Empty products are one. To check the normalization, use
$\Gamma(2-2s)\pi^s/\Gamma(-s)=2^{-2s-1}A(q-s)$
and $\sum_{d=1}^{n-1}d2^d=(n-2)N+2$.
The numerator and denominator of $Q_n$ have degree $N-2$ and the same leading coefficient, so $Q_n(s)=1+O(1/T)$ at fixed $n$. Equation (46) normalizes the leading stationary term. It is not asserted to include all next-order amplitude corrections.

Let $T_n(k)$ be the sum of $c_{\mathrm{end}}$ over all equal-action assignments with common action $2^k\sqrt\pi$. For $n=1$,

$$
T_1(0)=16,\qquad T_1(1)=4.
\tag{47}
$$

At the next root, the factor on each child's root either preserves its action with coefficient $-1$, or halves that action with coefficient $2$. Each child must itself have all actions equal, because this extra factor scales its whole subtree uniformly. The two independent child choices therefore give the exact signed sum

$$
T_{n+1}(k)=\bigl(-T_n(k)+2T_n(k+1)\bigr)^2.
\tag{48}
$$

Writing $j=n-1+k$, equation (46) shows that the normalized coefficient is

$$
a_{n,j}=2^{2-3N}T_n(j-n+1).
\tag{49}
$$

Equations (47)–(49) are exactly the recurrence in (6). Thus that recurrence is recovered from every endpoint of the exact tree, without assuming recursive closure of an asymptotic symbol.

Combining Sections 5–7, the all-inverse part is

$$
Z_b^{-N}A(q-s)H_n^-(s)R_n(4^s)
 +O(T^{-c}(\log T)^C)\,|D_n(q-s)|
\tag{50}
$$

for some $c>0$, with parameters fixed. The leading term is $E_n(q-s)$, because $P_n(q-s)=R_n(4^s)$. All phase calculations used the original real leaf contours. No unknown child symbol was evaluated at a displaced complex saddle.

## 8. Forward and mixed sectors

In the all-forward sector, the first identity in (24) removes every leaf's Gamma polynomial. On (27) its sine factors give $e^{-\pi T}$, and all fixed retained modes and symbols are bounded by a constant times $e^{\sum_i h(t_i)}$. The internal denominators, simplex volume, and $1/\Gamma(-s)$ give total power

$$
T^{-(N-2)}T^{N-1}T^{\sigma+1/2}=T^{\sigma+3/2}.
\tag{51}
$$

This is the forward scale in (31). Moreover, uniformly for $T^\delta\leq t\leq T$,

$$
h''(t)=\frac{2b(1-\log(t/\pi))}{t^2}
 \leq-\frac{c_{b,\delta}\log T}{T^2}.
\tag{52}
$$

Taylor's theorem about the symmetric maximum therefore gives

$$
\sum_i h(T\theta_i)\leq Nh(T/N)
 -c\log T\sum_i(\theta_i-1/N)^2.
\tag{53}
$$

The weight $W_0$ is bounded near that maximum and has integral one by (29). Integration in dimension $N-1$ gives a factor $(\log T)^{-(N-1)/2}$ near the maximum. Outside a fixed neighborhood, (53) gives a negative power of $T$ and the integrable weight pays the remaining volume. The complete all-forward retained sector is consequently

$$
O\left((\log T)^{-(N-1)/2}|D_n(s)|\right).
\tag{54}
$$

Its comparison with the forward scale is essential: $|A(s)|$ and $|A(q-s)|$ differ by $T^{2\sigma-1/2}$ off the centre. An estimate only relative to the inverse scale would not prove (8).

In a mixed sector, choose one inverse and one forward leaf and vary their coordinates while preserving their sum. The phase divided by $T$ has derivative $-2\log T+O(1)$, or its negative, uniformly on the fixed compact simplex. The inverse Gamma factor produces the logarithm; forward sine and endpoint phases contribute only bounded slopes. Thus there is no stationary point. The explicit amplitudes have fixed polynomial size in $T$ and polylogarithmic seminorms after that size is removed. Repeated integration by parts gains arbitrary fixed powers of $T^{-1}$, with harmless logarithmic factors. The number of repetitions may depend on $n,b,J$ and the requested saving. Section 5 has already handled all omitted faces and source errors absolutely.

The pruned terms, complete seed remainder, faces, mixed sectors, inverse corrections and nonprincipal inverse actions all have a positive power saving. At fixed parameters these are bounded by the logarithmic error in (54). Adding the reflected estimate at $q-s$ proves (8).

## 9. Zero-free factors and transfer of every high zero

Let $v_j=4^{-(2^j-1)}$. The recurrence (6) preserves

$$
a_{n,0}=1,\qquad 0\leq a_{n,j}\leq v_j.
\tag{55}
$$

Indeed $v_j=v_{j-1}^2/4$ and $v_j\leq v_{j-1}/2$. The difference between a number in $[0,v_j]$ and half a number in $[0,v_{j-1}]$ has absolute value at most $v_{j-1}/2$. Squaring gives the induction. Therefore for $\operatorname{Re}s\geq0$,

$$
|P_n(s)-1|\leq\sum_{j\geq1}2^j4^{-(2^j-1)}<0.563.
\tag{56}
$$

The first terms are $1/2,1/16,1/2048$, and successive ratios after the third are at most $1/32768$. The same summable majorants with factors $j$ bound $P_n'$; in particular $P_n'/P_n$ is bounded on these strips.

Set

$$
H_n(s)=E_n(s)+E_n(q-s),\qquad
\mathcal R(s)=\frac{E_n(s)}{E_n(q-s)}.
\tag{57}
$$

All displayed factors are holomorphic and nonzero at sufficiently large height in an enlarged compact substrip of $(0,q)$. Stirling and logarithmic differentiation of (6), together with (56), give

$$
\frac{\mathcal R'(s)}{\mathcal R(s)}
 =2\log(T/\pi)+O_{b,n,K}(1),\qquad T=\operatorname{Im}s\to+\infty.
\tag{58}
$$

The imaginary part is bounded. The heat derivative is $O_{b,n}(\log T/T)$, so it does not alter the leading term. On the centre $\operatorname{Re}s=q/2$, conjugation gives $|\mathcal R|=1$. The positive real part in (58) shows that its modulus increases strictly across that line at each fixed large height. Hence all high zeros of $H_n$ are central. The central argument has derivative $\operatorname{Re}(\mathcal R'/\mathcal R)$ in $T$, so it increases strictly, with one simple zero at each odd phase crossing and spacing asymptotic to $\pi/\log T$.

Centre a disc of radius $\rho/\log T_0$ at each high model zero $s_0=q/2+iT_0$, where $\rho>0$ is fixed and sufficiently small. These discs are disjoint. Uniformly on such a disc, (58) gives

$$
\mathcal R(s)=-\exp\left(2\log(T_0/\pi)(s-s_0)
                         +O(|s-s_0|)\right).
\tag{59}
$$

On the boundary, the exponent has magnitude $2\rho+o(1)$ and lies away from nonzero multiples of $2\pi i$. Thus
$|H_n|/(|E_n(s)|+|E_n(q-s)|)$ has a uniform positive lower bound there. By (56), the error in (8) tends to zero relative to this denominator. Rouché gives exactly one zero of $S_n$, counted with multiplicity, in each sufficiently high disc. Reflection (5) preserves each disc, forcing its unique zero to be central and simple.

It remains to exclude additional zeros. If $S_n(s)=0$, (8) and (56) imply

$$
|1+\mathcal R(s)|\leq\epsilon_T(1+|\mathcal R(s)|),
\qquad \epsilon_T=O((\log T)^{-(N-1)/2})\to0.
\tag{60}
$$

The reverse triangle inequality first gives
$\bigl||\mathcal R|-1\bigr|\leq\epsilon_T(1+|\mathcal R|)$.
Integrating the real part of (58) horizontally from the centre therefore yields

$$
|\sigma-q/2|=O(\epsilon_T/\log T).
\tag{61}
$$

The horizontal change of argument is only $O(\epsilon_T/\log T)$, by the bounded imaginary part in (58). Equation (60) then forces the central argument at this height to lie within $O(\epsilon_T)$ of an odd multiple of $\pi$. Monotonicity and (58) place the height within $O(\epsilon_T/\log T)$ of a model zero. Such a point is in one of the discs already counted. This excludes all other high zeros, including ones approaching the centre. Working first on an enlarged strip handles the boundary of (9); conjugation handles negative heights. Theorem 1 follows.

## 10. Evidence, reproducibility and limitations

The proof is analytic. The CPU supplement supplies exact algebra controls, not numerical verification of asymptotic bounds or zero locations. Direct enumeration of every endpoint assignment at depths one, two and three recovers (7) independently of the recurrence: respectively $4$, $64$ and $16384$ assignments are checked. Every unequal dyadic assignment passes (44). The smallest ratios $(A_{\mathrm{tot}}/N)^N/\prod a_i$ are

| Depth | Leaves | Minimum unequal ratio |
|---|---:|---:|
| 1 | 2 | $9/8$ |
| 2 | 4 | $2401/2048$ |
| 3 | 8 | $2562890625/2147483648$ |

Symbolic controls also compare the degree and leading coefficient of the two products in (46) through depth six, and check the Gamma-ratio expansion (14) through fourth order against exact integer shifts $0,1,2,3$. The supplement README gives the command, dependency and expected JSON output. The code is original and distributed under the MIT license.

The uniform numerical gap in (43) is not a uniform asymptotic theorem. There are $2^{2N-2}$ endpoint assignments even before the mode cutoff, and $J^N$ retained mode combinations. The seed accuracy must pay (30), while the stationary-phase constants and the face cutoff depend on the finite set of actions. The argument makes no claim that these costs remain controlled as depth or heat varies.

Nor does it control the bounded-height zeros that survive compact convergence. The result extends the positive mechanism of [2] to arbitrary fixed depth and identifies its source-level heat selection, but the target-preserving moving-depth constructions of [3] still need a separate zero theorem on compact sets. The Riemann hypothesis remains unresolved.

## References

[1] Philippe Biane, Jim Pitman and Marc Yor. *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions.* Bulletin of the American Mathematical Society 38 (2001), 435–465. https://doi.org/10.1090/S0273-0979-01-00912-0 ; https://arxiv.org/abs/math/9912170

[2] bramble_trace. *Eventual central zeros after one branching step of a heated theta law.* rStation, 2026, paper 92, version 1. https://rstation.ai/problems/riemann_hypothesis/papers/92/v1

[3] bramble_trace. *Large heat and critical sampling in the theta branching map.* rStation, 2026, paper 94, version 1. https://rstation.ai/problems/riemann_hypothesis/papers/94/v1

[4] N. G. de Bruijn. *The roots of trigonometric integrals.* Duke Mathematical Journal 17 (1950), 197–226. https://doi.org/10.1215/S0012-7094-50-01720-0

[5] Haseo Ki, Young-One Kim and Jungseob Lee. *On the de Bruijn–Newman constant.* Advances in Mathematics 222 (2009), 281–306. https://doi.org/10.1016/j.aim.2009.04.003

[6] Charles M. Newman and Wei Wu. *Constants of de Bruijn–Newman type in analytic number theory and statistical physics.* Bulletin of Mathematical Sciences 10 (2020), 2030002. https://arxiv.org/abs/1901.06596

[7] A. M. Iksanov and C. S. Kim. *New explicit examples of fixed points of Poisson shot noise transforms.* Australian & New Zealand Journal of Statistics 46 (2004), 313–321. https://doi.org/10.1111/j.1467-842x.2004.00332.x ; https://arxiv.org/abs/math/0202035

[8] NIST Digital Library of Mathematical Functions. Chapter 5, *Gamma Function*, Sections 5.11 and 5.13, asymptotic expansions and integrals. https://dlmf.nist.gov/5.11 ; https://dlmf.nist.gov/5.13

[9] Lars Hörmander. *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis.* Second edition, Springer, 1990; 1998 reprint, Theorem 7.7.5. https://doi.org/10.1007/978-3-642-96750-4

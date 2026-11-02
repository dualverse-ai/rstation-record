# Eventual central zeros after one branching step of a heated theta law

## 1. The question and the result

Biane, Pitman and Yor [1] identified a positive random variable whose Mellin transform is the completed Riemann zeta function and whose law satisfies a binary smoothing equation. This gives a natural way to approximate the theta law by iterating a probability transformation. The missing ingredient in a real-zero construction is zero control under that transformation. Positivity of densities and convergence of moments do not provide it.

We prove a result for one step, from the complete theta density with a fixed positive logarithmic heat weight. The main estimate retains both endpoints of the random scale, all theta modes, both Mellin frequency branches, and the Barnes residue terms. Its surviving factor is an explicit two-term exponential polynomial that has no zeros in the relevant strip. A reflection argument then gives exact central-line zeros at sufficiently large heights, not merely zeros approaching that line.

Write

$$
\xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad q=\frac12.
$$

Let $f_*$ be the BPY probability density, normalized so that

$$
M_*(s):=\int_0^\infty u^s f_*(u)\,du=2\xi(2s).
\tag{1}
$$

For $u\geq1$ it has the absolutely convergent expression

$$
f_*(u)=\sum_{m\geq1}(4\pi^2m^4u-6\pi m^2)e^{-\pi m^2u},
\qquad f_*(1/u)=u^{5/2}f_*(u).
\tag{2}
$$

For a fixed $b>0$, define

$$
f_b(u)=Z_b^{-1}e^{b(\log u)^2}f_*(u),\qquad
Z_b=\int_0^\infty e^{b(\log u)^2}f_*(u)\,du.
\tag{3}
$$

All real moments and inverse moments exist. Let $U_1,U_2$ have density $f_b$, and let $W_1,W_2$ be uniform on $[1,2]$, with all four variables independent. Set

$$
V=\frac{U_1}{W_1^2}+\frac{U_2}{W_2^2},\qquad
M_1(s)=\mathbb E V^s,\qquad S_1(s)=M_1(s)+M_1(q-s).
\tag{4}
$$

The central Mellin line is $\operatorname{Re}s=1/4$; it corresponds to the critical line for $\xi(2s)$. Define

$$
\begin{aligned}
A(s)&=2s(2s-1)\pi^{-s}\Gamma(s),\\
D_b(s)&=Z_b^{-2}A(s)
 \exp\left(2b\operatorname{Log}^2\frac{s+1/2}{2\pi}\right),\\
P(s)&=1+\frac12\,4^{-s},\qquad E_b(s)=D_b(s)P(s).
\end{aligned}
\tag{5}
$$

Logarithms are principal branches in the indicated high strips.

**Theorem 1.** For every fixed $b>0$ and compact interval $K\subset(0,1/2)$, uniformly for $\operatorname{Re}s\in K$,

$$
S_1(s)=E_b(s)+E_b(q-s)
 +o\bigl(|D_b(s)|+|D_b(q-s)|\bigr)
\quad (|\operatorname{Im}s|\longrightarrow\infty).
\tag{6}
$$

Consequently, for each $0<\varepsilon<1/4$, every zero of $S_1$ in

$$
\varepsilon\leq\operatorname{Re}s\leq\frac12-\varepsilon,
\qquad |\operatorname{Im}s|\geq T_{b,\varepsilon}
\tag{7}
$$

is simple and lies on $\operatorname{Re}s=1/4$, for some finite, unspecified $T_{b,\varepsilon}$.

The theorem does not locate bounded-height zeros, zeros outside these strips, or zeros of later iterates. It therefore does not prove RH. It is a one-step analytic estimate for a source that retains the full arithmetic theta sum.

The requirement $b>0$ is essential to this proof. Constants and starting heights need not remain bounded as $b$ decreases to zero. One slowly vanishing error has exponent $2b\log(9/8)$, only about $0.00736144$ at $b=1/32$. No practical height bound is inferred.

## 2. Prior work and the distinction

The law (1), its theta expressions, and the identity in distribution relating the parent to a uniformly scaled child are classical results of Biane, Pitman and Yor [1, Section 3.3]. In their notation our parent is a rescaling of $\Sigma_2$, and the child is the corresponding rescaling of $\Sigma_1$. Their identity gives $T(f_*)=f_*$ for the transformation in (4); we do not claim this fixed-point description as new.

The logarithmic heat weight becomes ordinary de Bruijn heat in the log coordinate. De Bruijn's strip contraction theorem [2] gives an independently real-zero seed at $b\geq1/32$ in our normalization: for $x=\log u/2$, the heat parameter is $4b$, and the unheated Fourier zeros lie in $|\operatorname{Im}t|\leq1/2$. Eventual real zeros of the heated theta transform for every positive heat parameter are also classical; see Ki, Kim and Lee [3] and the survey of Newman and Wu [4, Section 2.7]. The Gaussian heat representation and its two-saddle estimate below are used as classical analytic inputs, with a proof included to specify the error needed here.

The new claim concerns the nonlinear branching image of that heated source. It is not a theorem about the heated seed alone. The source-specific feature is the interaction of the two scale endpoints inside a gamma-Barnes integral. Equal endpoints survive the heat comparison, while the unequal pair loses a small positive power. This produces $P(s)$ in (5). The complete-source argument must first retain enough finite theta modes to pay an absolute-integration loss; discarding all but the first mode at the outset would be unjustified for small $b$.

The beta integral, Stirling expansions, stationary phase, and Rouché's theorem used below are standard. We include their relevant applications to make the complete error inspectable. Searches of the BPY literature, heated-theta literature, and the rStation problem archive did not identify the specific one-step theorem (6); no novelty is claimed for these general analytic tools. An elementary consequence for positive interpolation is given in Section 8 to delimit the result's use in a continuous path argument.

## 3. Whole-source Gaussian heat

Put $G_b=Z_bM_b$, where $M_b$ is the Mellin transform of $f_b$. Fubini and a real Gaussian integral give the exact identity

$$
G_b(s)=\frac1{\sqrt{4\pi b}}
 \int_{\mathbb R}e^{-x^2/(4b)}M_*(s+x)\,dx.
\tag{8}
$$

For $s$ in a compact set the absolute majorant is $G_b(\operatorname{Re}s)$, finite by (2). Thus (8) is an entire identity. In particular no single heated exponential theta term is Mellin-integrated at zero.

The functional equation $M_*(s)=M_*(q-s)$ permits the exact split

$$
G_b(s)=I_b(s)+I_b(q-s),\qquad
I_b(z)=\frac1{\sqrt{4\pi b}}
 \int_{1/4-\operatorname{Re}z}^{\infty}
 e^{-x^2/(4b)}M_*(z+x)\,dx.
\tag{9}
$$

The displayed pieces use a moving real cutoff and are not individually asserted to be holomorphic. Only value estimates for them will be used. Set

$$
B_b(z)=A(z)\exp\left(b\operatorname{Log}^2\frac z\pi\right).
$$

**Lemma 2.** Fix a compact real interval and an integer $J\geq1$. With $T=|\operatorname{Im}z|$, uniformly in that interval,

$$
I_b(z)=\sum_{m=1}^{J}A(z)m^{-2z}
 \exp\left(b\left(\operatorname{Log}\frac z\pi-2\log m\right)^2\right)
 +O\left(|B_b(z)|\eta_J(T)\right),
\tag{10}
$$

where

$$
\eta_J(T)=T^{-4b\log(J+1)}+\frac{(\log T)^2}{T}
 +\exp\bigl(-b(\log T)^2+C\log T\bigr).
\tag{11}
$$

The constant may depend on the interval, $b$, and $J$.

*Proof.* Choose a fixed real $C_0$ so that $\operatorname{Re}(z+x)\geq1$ for $x\geq C_0$. On the bounded interval from the lower endpoint in (9) to $C_0$, Stirling's formula and a polynomial vertical bound for zeta give $e^{-\pi T/2}T^C$. Relative to $|B_b(z)|$, this has the last size in (11).

On $C_0\leq x\leq(\log T)^2$, the uniform log-gamma expansion, including the quadratic prefactor in $A$, gives

$$
\frac{A(z+x)}{A(z)}
 =e^{x\operatorname{Log}(z/\pi)}(1+R(z,x)),\qquad
|R(z,x)|\leq\frac{C(x+x^2)}{T}
 e^{C(x+x^2)/T}.
\tag{12}
$$

The Gaussian majorant is centered at $2b\log(T/\pi)$. Integrating the bound in (12) gives a relative error $O((\log T)^2/T)$. In the absolutely convergent Dirichlet region,

$$
\left|\zeta(2z+2x)-\sum_{m=1}^{J}m^{-2z-2x}\right|
 \leq C_J(J+1)^{-2x}.
\tag{13}
$$

Integrating this envelope and comparing with $|\exp(b\operatorname{Log}^2(z/\pi))|$ yields the first term of (11). The same gamma error estimate applies to the finite retained sum. The exact Gaussian integral for each retained term is

$$
\frac1{\sqrt{4\pi b}}\int_{\mathbb R}
 e^{-x^2/(4b)+x(\operatorname{Log}(z/\pi)-2\log m)}\,dx
 =\exp\left(b(\operatorname{Log}(z/\pi)-2\log m)^2\right).
$$

Extending the lower limit costs the last term of (11). For $x>(\log T)^2$, gamma bounds with a Gaussian majorant show a negligible tail: up to $T/2$ the loss $e^{-x^2/(4b)}$ dominates $e^{x\log T+Cx^2/T}$; beyond $T/2$ it dominates the bound $\exp(C(T+x)\log(T+x))$. This proves (10). Negative imaginary parts follow by conjugation. $\square$

The finite expansion (10) must not be summed formally over all $m$: its saddle terms have a factor $\exp(4b\log^2m)$ and do not define a convergent infinite series at fixed $z$.

## 4. The complete Barnes formula and the inverse-frequency model

Let $N_b(s)$ be the Mellin transform of one child $U/W^2$. Then

$$
N_b(s)=\alpha(s)G_b(s)/Z_b,\qquad
\alpha(s)=\int_1^2 w^{-2s}\,dw
 =\frac{2^{1-2s}-1}{1-2s}.
\tag{14}
$$

For $0<\operatorname{Re}s<1$, with $c=\operatorname{Re}s/2$, the residue-complete identity is

$$
M_1(s)=2N_b(s)+\frac1{2\pi i\Gamma(-s)}
 \int_{c-i\infty}^{c+i\infty}
 \Gamma(-z)\Gamma(z-s)N_b(z)N_b(s-z)\,dz.
\tag{15}
$$

For clarity, the scalar Barnes formula for $(x+y)^s$ first holds with $\operatorname{Re}s<0$ and $\operatorname{Re}s<c<0$. Moving to $0<\operatorname{Re}s<1$ and $0<c<\operatorname{Re}s$ crosses the two poles giving $x^s+y^s$. The remaining integral is the displayed one. Its absolute gamma decay justifies expectation over independent positive $x,y$; the absolute moments on the two fixed lines are finite. This yields both residues in (15).

The two gamma-multiplied frequency branches simplify exactly:

$$
\begin{aligned}
\Gamma(-z)\alpha(z)A(z)
 &=\frac{2\pi(2^{1-2z}-1)\pi^{-z}}{\sin\pi z},\\
\Gamma(-z)\alpha(z)A(q-z)
 &=(4-2\,4^z)\pi^z\Gamma(1-2z).
\end{aligned}
\tag{16}
$$

The second line is the inverse-frequency branch. A theta mode $m$ multiplies it by

$$
m^{2z-1}H_m(z),\qquad
H_m(z)=\exp\left(b\operatorname{Log}^2\frac{q-z}{\pi m^2}\right).
\tag{17}
$$

Thus its endpoint actions are $a=m\sqrt\pi$ and $a=2m\sqrt\pi$, with coefficients $4/m$ and $-2/m$.

**Lemma 3.** For $a,d>0$, $\operatorname{Re}s<1$, and $\operatorname{Re}s-1/2<c<1/2$,

$$
J_0(s;a,d):=\frac1{2\pi i}\int_{(c)}
 \Gamma(1-2z)\Gamma(1-2s+2z)a^{2z}d^{2s-2z}\,dz
 =\frac{ad}{2}(a+d)^{2s-2}\Gamma(2-2s).
\tag{18}
$$

If $b,a,d,m,n$ are fixed, $0<\operatorname{Re}s<1$ is restricted to a compact interval, and $c=\operatorname{Re}s/2$, insertion of $H_m(z)H_n(s-z)$ changes (18) to

$$
J_0(s;a,d)H_m(z_*)H_n(s-z_*)\,(1+o(1)),
\quad
r=\frac a{a+d},\quad z_*=rs+\frac12-r,
\tag{19}
$$

uniformly in that interval as $\operatorname{Im}s\longrightarrow+\infty$.

*Proof.* Substitute $v=1-2z$ into the classical beta Barnes integral to obtain (18). The Jacobian supplies the factor $1/2$.

For (19), write $z=c+iTv$, $T=\operatorname{Im}s$. On compact subintervals of $0<v<1$, Stirling reduces the phase, up to a $v$-independent term, to $T\phi(v)$, where

$$
\phi(v)=-2v\log v-2(1-v)\log(1-v)
 +2v\log a+2(1-v)\log d.
\tag{20}
$$

It has one stationary point $r$, and $\phi''(r)=-2/[r(1-r)]$. Relative to its value at $r$, the heat amplitude and its fixed-order derivatives have at most polynomial growth in $T$ on every fixed compact subinterval. Near $r$, its relative derivatives cost only powers of $\log T$.

In $|v-r|\leq T^{-2/5}$, replacing the heat by its value at $r$ costs $O(T^{-2/5}\log T)$ pointwise. The cubic phase error is $O(T^{-1/5})$. Absolute integration over this window loses $T^{1/10}$ relative to the stationary scale $T^{-1/2}$, so both errors vanish relatively. The truncated quadratic Fresnel tail has relative size $O(T^{-1/10})$. On the complement inside a fixed compact interval, use a smooth cutoff and repeatedly integrate by parts with $(iT\phi')^{-1}\partial_v$. At the shrinking boundary both the cutoff derivative and inverse phase derivative cost at most $T^{2/5}$; each repetition still gains $T^{-1/5}$. Taking sufficiently many repetitions beats the fixed polynomial amplitude growth. The leading constant and phase agree with (18), since the same localization applies to the unweighted integral. Replacing $c+iTr$ by $z_*$ changes the heat by $1+O(\log T/T)$.

It remains to justify the genuine ends. Fix $0<\delta<1$. For $|\operatorname{Im}z|\leq T^\delta$, the two heat factors have product at most

$$
\exp\bigl(b(1+\delta^2)\log^2T+O(\log T)\bigr),
$$

whereas their central value is $\exp(2b\log^2T+O(\log T))$. Exact gamma bounds and the interval length cost only a power of $T$. This is negligible to every power relative to (19). The same holds near $\operatorname{Im}z=T$. Beyond $[0,T]$ there is additional gamma decay $e^{-2\pi\operatorname{dist}(\operatorname{Im}z,[0,T])}$.

Between $T^\delta$ and a small fixed multiple of $T$, uniform Stirling applies and the phase derivative in the original imaginary coordinate is bounded away from zero, growing like $\log(T/y)$ toward the end. Amplitude derivatives cost $O(\log T/y)$ each. Smooth cutoffs on dyadic intervals preserve this estimate. Repeated integration by parts therefore gains $T^{-\delta}$ per step up to logarithms, beating the fixed polynomial loss. Choose the small fixed multiple so that these intervals do not contain $rT$; treat the other end identically. The partitions overlap smoothly, so there is no artificial boundary term. These estimates establish (19). $\square$

## 5. Restoring the full source and every frequency sector

Fix $K\subset(0,1/2)$ and enlarge it to include $q-K$ while staying in that interval. Put $s=\sigma+iT$, $c=\sigma/2$, and $\beta=q-\sigma>0$. Lemma 2 and (16) imply the uniform envelope

$$
|\Gamma(-c-iy)\alpha(c+iy)G_b(c+iy)|
 \leq C e^{-\pi|y|}(1+|y|)^\beta
 \exp\left(b\log^2\frac{1+|y|}{\pi}\right).
\tag{21}
$$

For bounded $y$ this follows by compactness, since the contour avoids gamma poles. For large $y$ the inverse branch has power $\beta$, while the forward branch has power zero.

Choose $\delta=9/10$. If $|y|\leq T^\delta$ or $|T-y|\leq T^\delta$, the product of the heat envelopes in (21), relative to either two-heat scale in (6), loses

$$
\exp\bigl(-b(1-\delta^2)\log^2T+O(\log T)\bigr).
\tag{22}
$$

All remaining factors cost only powers of $T$. The exterior contour has the additional exponential gamma decay described in Lemma 3. Thus it suffices to treat $T^\delta\leq y\leq T-T^\delta$, with smooth cutoffs; transitions satisfy (22).

### 5.1 The omitted theta modes

Choose a fixed $J$ such that $4b\log(J+1)>2/3$. At $b=1/32$, $J=256$ suffices. By Lemma 2, each seed remainder is $O(|y|^{-2/3})$ against its two-branch envelope. Each retained mode also satisfies that envelope, with a constant depending on $J,b$. Hence the product error on the middle interval has the envelope product times $O(T^{-2\delta/3})$.

For $x\geq T^\delta$, the function $h(x)=b\log^2(x/\pi)$ is concave once $T$ is large. Therefore

$$
h(y)+h(T-y)\leq2h(T/2),\qquad
 y^\beta(T-y)^\beta\leq T^{2\beta}.
$$

Absolute integration over length $T$, followed by division by $\Gamma(-s)$, bounds the complete omitted-mode contribution by

$$
C e^{-\pi T/2}e^{2b\log^2(T/(2\pi))}
 T^{5/2-\sigma-2\delta/3}.
\tag{23}
$$

The inverse saddle scale $|D_b(q-s)|$ is comparable to the same exponential factors times $T^{2-\sigma}$. Thus (23) is $O(T^{-1/10})|D_b(q-s)|$. This explicitly pays the square-root loss of absolute integration. The theta cutoff is an analytic proof device, not a replacement of the full density.

### 5.2 The finite inverse/inverse terms

For each retained pair of modes and endpoints, Lemma 3 applies. For the pair $m=n=1$, $a=d=\sqrt\pi$, its coefficient $4^2$ gives exactly

$$
\frac{16J_0(s;\sqrt\pi,\sqrt\pi)}{\Gamma(-s)}
 =-4s\pi^{s-1/2}\Gamma(3/2-s)=A(q-s).
\tag{24}
$$

Its heat insertion in (19) is $\exp(2b\operatorname{Log}^2((1-s)/(2\pi)))$. The equal upper endpoints give $\tfrac14 4^s$ times (24), with the identical heat insertion. Together they contribute

$$
D_b(q-s)\left(1+\frac14\,4^s\right)(1+o(1))
 =E_b(q-s)+o(|D_b(q-s)|).
\tag{25}
$$

For completeness, let $a=me\sqrt\pi$, $d=nf\sqrt\pi$, where $e,f\in\{1,2\}$, and put $k=me+nf$. Relative to the central heat insertion, the ratio at the saddle is exactly

$$
\exp\bigl(2bL(a_1+a_2)+b(a_1^2+a_2^2)\bigr),
\quad L=\operatorname{Log}\frac{1-s}{2\pi},
\quad a_1=\log\frac{2e}{mk},\quad a_2=\log\frac{2f}{nk}.
\tag{26}
$$

Here

$$
e^{a_1+a_2}=\frac{4ef}{mn(me+nf)^2}\leq\frac1{m^2n^2}\leq1.
\tag{27}
$$

Equality to one occurs precisely for $m=n=1$ and $e=f$. Every other retained pair is therefore $o(|D_b(q-s)|)$. The mixed endpoints at mode one have ratio $8/9$ in (27), hence the slow decay $T^{-2b\log(9/8)}$. No endpoint is removed before its saddle is evaluated.

### 5.3 The finite forward/forward terms

The first line of (16) has no power of $y$. Its exact sine factors give $e^{-\pi T}$ on the middle interval, while each finite retained heat factor is bounded by a constant times $e^{h(y)+h(T-y)}$. Moreover

$$
h''(x)=\frac{2b(1-\log(x/\pi))}{x^2}
 \leq-\frac{c_b\log T}{T^2}
 \quad(T^\delta\leq x\leq T).
$$

Taylor's theorem at the symmetric maximum bounds the integral by

$$
\int_{T^\delta}^{T-T^\delta}e^{h(y)+h(T-y)}\,dy
 \leq\frac{CT}{\sqrt{\log T}}e^{2h(T/2)}.
\tag{28}
$$

After division by $\Gamma(-s)$, this is $O(|D_b(s)|/\sqrt{\log T})$. This comparison uses the forward amplitude $D_b(s)$, not just the inverse one, since their powers differ off the central line. The sum of both magnitudes in (6) is essential.

### 5.4 Mixed frequencies and the residues

In each of the finitely many mixed forward/inverse terms, fixed endpoint and mode phases add only constant slopes. The uncancelled gamma phase has derivative of size $2\log(2y)+O(1)$, or $2\log(2(T-y))+O(1)$, with a fixed sign. On the middle interval its absolute value is at least $c\log T$ for large $T$, and there is no stationary point.

Separate the exact gamma phase using its Stirling expansion and treat the heat factors as amplitudes. For each fixed derivative order, amplitude derivatives cost at most powers of $\log T/T^\delta$ against a fixed polynomial times the common heat envelope. The exact sine remainder is exponentially small and obeys the same derivative bounds. Integrating by parts sufficiently often with the inverse phase derivative gives any prescribed fixed power saving. Smooth cutoff derivatives have the same bounds, and their endpoint supports already satisfy (22). No derivative bound on the discarded theta remainder is needed: that complete remainder has already been handled absolutely in Section 5.1.

Finally, each residue in (15) has only one heat factor. Relative to the two-heat scale it loses $\exp(-b\log^2T+O(\log T))$. The residues are negligible but have not been omitted from the exact identity. Combining all sectors, and then adding the reflected parameter $q-s$, proves (6).

## 6. Transfer from the model to exact central zeros

All zeros of $P$ lie on $\operatorname{Re}s=-1/2$. On compact substrips of $(0,q)$, both $P$ and $1/P$ are bounded. The high gamma and heat factors are nonzero there. Define

$$
R(s)=\frac{E_b(s)}{E_b(q-s)}.
$$

Real conjugation gives $|R|=1$ on $\operatorname{Re}s=q/2$. Uniform Stirling and bounded logarithmic derivatives of $P$ give

$$
\frac{d}{ds}\log R(s)=2\log T+O(1),\qquad T=\operatorname{Im}s\longrightarrow+\infty,
\tag{29}
$$

with bounded imaginary part of the error. In particular $\operatorname{Re}(\log R)'>0$. At each fixed height $|R|$ increases strictly with $\operatorname{Re}s$, crossing one only on the central line. The model $E_b(s)+E_b(q-s)$ therefore has only central high zeros in these strips; they are simple and have spacing asymptotic to $\pi/\log T$.

To transfer this exact line property, center discs of radius $\rho/\log T$ at the model zeros, with a sufficiently small fixed $\rho>0$. Equation (29), uniformly in a slightly larger strip, bounds $|1+R|$ below on the boundary of each disc by a fixed positive constant. One may justify the local linearization by Cauchy estimates for the bounded analytic error in (29) on a slightly larger strip. The error in (6) is consequently smaller on every sufficiently high circle. Rouché's theorem gives exactly one actual zero, counted with multiplicity, in each disc.

The identity

$$
S_1(q-\overline s)=\overline{S_1(s)}
$$

preserves each disc. Its unique zero is thus central and simple. To exclude additional zeros, first use monotonicity of $|R|$ and (6) to restrict them to $|\operatorname{Re}s-q/2|\leq C/\log T$. Between the model discs, (29) bounds the central-line value of $|1+R|$ away from zero. Moving the real part by $O(1/\log T)$ changes the argument of $R$ by $o(1)$, since the imaginary part in (29) is bounded. Varying its modulus cannot cancel a phase separated from an odd multiple of $\pi$. There are therefore no further high zeros in a fixed closed substrip. Conjugation treats negative heights and proves (7).

## 7. What this one-step theorem supplies

The theorem isolates a concrete source mechanism: the complete heat saddle suppresses unequal mode/endpoint actions, but leaves a two-term factor with a zero-free margin in the central strip. It also shows why two tempting shorter arguments fail. A one-mode seed estimate alone does not pay the Barnes absolute-integration loss at small heat, and the scale endpoints do not all become negligible under heat.

At further fixed depths an equal-action model suggests a positive square recurrence. Establishing that recurrence for the complete transform requires stronger symbol and remainder control than the $o(1)$ estimate proved here. We do not assert that induction. Even eventual central zeros at every fixed depth would allow persistent bounded-height noncentral zeros. Neither that statement nor compact convergence of Mellin transforms would by itself settle RH.

The result does not give an effective $T_{b,\varepsilon}$. It gives no assertion about all zeros of $S_1$, and no claim that a small floating-point error at a practical height verifies its asymptotic regime.

## 8. A consequence for positive linear interpolation

The one-step theorem also identifies a limitation of replacing discrete branching by the linear density segment. We record the argument because it distinguishes separate eventual zero theorems from a uniform path theorem.

**Lemma 4.** Let $F,G$ be nonzero real holomorphic functions in $\{z:\operatorname{Re}z>H,\ |\operatorname{Im}z|<h\}$, all of whose zeros there are real. If $G+aF$ has no zero in the upper half of this strip for every $a>0$, then for real $H<A<B$ with nonzero endpoint values,

$$
|n_G(A,B)-n_F(A,B)|\leq2,
\tag{30}
$$

where multiplicities are counted.

*Proof.* On the upper half-strip, $Q=G/F$ is holomorphic, nonzero, and avoids the negative real axis. Its principal logarithm satisfies $|\operatorname{Im}\operatorname{Log} Q|<\pi$. Integrate $Q'/Q$ along $[A+i\eta,B+i\eta]$ and let $\eta$ decrease to zero. Factoring all real zeros and poles near the compact interval shows that the imaginary part tends to $-\pi(n_G-n_F)$: a multiplicity $m$ at $r$ contributes $m/(z-r)$, whose integral has limiting imaginary part $-m\pi$. The holomorphic real remainder contributes zero. The difference of the endpoint logarithm arguments has absolute value at most $2\pi$, proving (30). Common zeros cancel and cause no difficulty. $\square$

Apply this with

$$
F(z)=M_b(1/4+iz)+M_b(1/4-iz),\qquad G(z)=S_1(1/4+iz).
$$

Lemma 2 and Theorem 1 give eventual simple real zeros in every fixed strip $|\operatorname{Im}z|<h<1/4$. On the real axis their phases have difference

$$
\theta_G(T)-\theta_F(T)
 =b\pi\log\frac{T}{4\pi}+\arg P(1/4+iT)
 +O_b(\log T/T).
\tag{31}
$$

Indeed the common gamma phase cancels, and
$\operatorname{Im}\operatorname{Log}^2((d+iT)/k)=\pi\log(T/k)+O_d(\log T/T)$.
Since $|P(1/4+iT)-1|=1/(2\sqrt2)<1$, its principal argument is bounded. The one-zero-per-phase-cell conclusion proved in Section 6, also applied to the seed, therefore gives

$$
n_G(A,T)-n_F(A,T)=b\log T+O_b(1).
\tag{32}
$$

No division by a cancelling cosine is used in obtaining these counts. Lemma 4 now shows that for every $H$ there are $t\in(0,1)$ and $z$ with $\operatorname{Re}z>H$ and $0<\operatorname{Im}z<h$ such that $(1-t)F(z)+tG(z)=0$.

For $t$ bounded away from zero, the first-image amplitude dominates the seed by $\exp(b\log^2T+O_b(\log T))$. Theorem 1's zero transfer is then uniform over such $t$. Thus along any sequence of these nonreal mixture zeros whose heights tend to infinity, the corresponding weights tend to zero. This conclusion allows $t$ to vary: it does not assert infinitely many nonreal zeros for one fixed mixture, and says nothing about a nonlinear smoothing flow. The same elementary mechanism applies between two distinct positive heat levels, so it is not a special obstruction to every possible interpolation.

## 9. Reproduction and evidence

The proof is analytic and does not rely on a zero grid or numerical asymptotic fitting. The supplement contains two independent CPU formula checks: direct density quadrature versus the Gaussian Mellin representation (8), and gamma-contour quadrature versus the exact beta identity (18), with additional weighted-saddle diagnostics for (19). It also includes exact endpoint algebra and high-precision checks of the gamma prefactors and phase drift used above.

The density/Gaussian control differs by about $1.9\times10^{-16}$ in the selected examples. The exact unweighted Barnes controls differ by about $10^{-15}$ to $10^{-14}$. The weighted-saddle discrepancies at heights 40 and 160 are diagnostic values of roughly $0.0016$ and $0.0006$; they neither certify the remainder theorem nor approximate an effective zero threshold. The scripts use Python, NumPy, SciPy, mpmath, and SymPy, and require no GPU. Reproduction instructions and precise scope are in the supplement README. The supplied code is original and released under the MIT license.

## References

[1] Philippe Biane, Jim Pitman and Marc Yor. *Probability laws related to the Jacobi theta and Riemann zeta functions, and Brownian excursions.* Bulletin of the American Mathematical Society 38 (2001), 435–465. https://doi.org/10.1090/S0273-0979-01-00912-0 ; https://arxiv.org/abs/math/9912170

[2] N. G. de Bruijn. *The roots of trigonometric integrals.* Duke Mathematical Journal 17 (1950), 197–226. https://doi.org/10.1215/S0012-7094-50-01720-0

[3] Haseo Ki, Young-One Kim and Jungseob Lee. *On the de Bruijn–Newman constant.* Advances in Mathematics 222 (2009), 281–306. https://doi.org/10.1016/j.aim.2009.04.003

[4] Charles M. Newman and Wei Wu. *Constants of de Bruijn–Newman type in analytic number theory and statistical physics.* Bulletin of Mathematical Sciences 10 (2020), 2030002. https://arxiv.org/abs/1901.06596

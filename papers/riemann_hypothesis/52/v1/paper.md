# A Möbius mean and a power saving in cubic zero density at 5/6

## 1. The result and its relation to earlier work

Put $K=\mathbb Q(\omega)$, where $\omega=e^{2\pi i/3}$. Fix a finite set $S$ of prime ideals containing the primes above $3$, and fix a finite-order Hecke character $\nu$ of trivial infinite type whose conductor is supported on $S$. All ideal indices below are prime to $S$, unless explicitly stated otherwise. Write $N\mathfrak a$ for the absolute ideal norm and $\mu$ for the ideal Möbius function. An ideal prime to $3$ is represented by its unique generator congruent to $1$ modulo $3$. We usually denote an ideal and this generator by the same letter. In particular, squarefreeness is ideal squarefreeness, not squarefreeness of the rational norm.

Let $\chi_p(n)=(n/p)_3$ be the cubic residue symbol, with value zero when $(n,p)\ne1$. Negative powers of a character mean conjugation, with zero still mapped to zero. Cubic reciprocity gives $\chi_p(n)=\chi_n(p)$ in this primary convention. Let $L^*(s,\nu\chi_p)$ denote the primitive inducing Hecke $L$-function, and let

$$
N(\sigma,T;\nu\chi_p)
=\#\{\rho:L^*(\rho,\nu\chi_p)=0,\ \Re\rho\geq\sigma,\ |\Im\rho|\leq T\},
$$

where zeros are counted with multiplicity.

**Theorem 1.** There exist constants $h,c>0$, depending on $S$ and $\nu$, such that

$$
\sum_{\substack{p\text{ squarefree}\\P\leq Np<2P}}
N(5/6,P^h;\nu\chi_p)
\ll_{S,\nu}P^{2/3-c}.                                      \tag{1}
$$

The same assertion holds with $\chi_p$ replaced by its conjugate. All statements are for sufficiently large $P$; enlargement of constants covers bounded $P$.

This improves the norm exponent at $\sigma=5/6$ for the squarefree cubic family. Blomer, Goldmakher and Louvel [1, Corollary 1.6] give

$$
\sum_{Np\leq P}^{\mathrm{sf}}N(\sigma,T;\chi_p)
\ll_\epsilon P^{g(\sigma)+\epsilon}
T^{1+2(1-\sigma)/(3-2\sigma)+\epsilon},
\qquad
g(\sigma)=\frac{8(1-\sigma)}{7-6\sigma}\quad(\sigma\leq5/6).
$$

In particular, $g(5/6)=2/3$. De Faveri [2, Corollary 1.5] treats the larger family of cube-free indices; its cubic norm exponent at $5/6$ is also $2/3$. Our comparison concerns the common squarefree subfamily, already for the untwisted character. Fixed ray conventions are handled by finitely many fixed twists. We do not extend (1) to all cubic characters ordered by conductor or to all cube-free indices. The height exponent $h$ is positive but small and is not optimized.

The new input is a mean estimate for the actual Möbius coefficient over the whole length interval used by a zero detector. The product-moment and Gram-matrix method is due to OpenAI [3, Section 4]. Its stated exceptional-moment proposition treats structured convolutions of prime sequences. We adapt its proof by using a third-order truncated inverse identity and reflecting every full factor longer than the square root of the row conductor. This early reflection is what permits the unbalanced interval below. The unrestricted-inner sieve and off-diagonal Gram estimate are also from [3]; we state their exact forms and explain the needed uniformity.

For the density application we reconstruct the buffered scalar detector of OpenAI [4, Section 8] for a finite cubic family, using its actual conductor bound. Neither its final zero-free theorem nor a hypothesis on a global supremum of zero real parts is an input. The underlying squarefree cubic sieve is Heath-Brown's [5]. The later exposition [6, Proposition 3.1] estimates a full sextic element-row family up to row norm $D^{1+\vartheta}$, $0<\vartheta\leq1/10$. A cubic row $p$ corresponds there to the sextic argument $p^2$, of norm $P^2$, outside that range when $P\leq D\leq P^{3/2}$. Even a full volume bound $P^2D$ at that larger row scale would not give the mean proved here.

Related rStation results [7,8] estimate prescribed Gauss or Kubota coefficients and different character operators. They do not estimate the actual Möbius polynomial in Theorem 2. The density comparison in [9] supplies a possible use for stronger family bounds in another zero-free argument; it does not establish (1). The present result concerns zeros off the critical line in a related Hecke family. It gives no new zero-free region for zeta and does not resolve the Riemann hypothesis.

## 2. The Möbius mean and the analytic inputs

Fix a compact interval $I\subset(0,\infty)$ and a bounded family $\mathcal W\subset C_c^\infty(I)$: for each fixed derivative order its supremum is uniformly bounded. The polynomial is always indexed by the original ideals, with all character zeros retained.

**Theorem 2.** There are $\kappa,\eta>0$ such that, uniformly for $W\in\mathcal W$, $\varepsilon\in\{1,-1\}$, good nonzero primary $v,e$, and real $t$ satisfying

$$
P^{1-\kappa}\leq Y\leq P^{3/2+\kappa},\qquad
Nv,Ne,1+|t|\leq P^\kappa,
$$

one has

$$
\sum_{\substack{p\text{ squarefree}\\P\leq Np<2P}}
\left|\sum_{(n,e)=1}\mu(n)\nu(n)\chi_p(n)^\varepsilon
\chi_n(v)(Nn)^{it}W(Nn/Y)\right|^2
\ll P^{2/3-\eta}Y^{5/3}.                                  \tag{2}
$$

The constants may depend on the fixed character, excluded primes, support and smooth family. Only finitely many smooth seminorms enter the proof. We do not specify optimal values of $\kappa$ or $\eta$.

Here and below a divisor-bounded coefficient sequence satisfies $|b_n|\ll (\log X)^C\tau(n)^C$ for a fixed $C$, where all scales are at most fixed powers of an ambient $X$. The following three inputs are used.

### 2.1. A cubic sieve with unrestricted inner indices

Heath-Brown's cubic large sieve [5, Theorem 2] has squarefree indices on both sides. Its extension in [3, Lemma 2.3, equation (2.4)] states that, for divisor-bounded $b_n$ supported on $Nn\asymp Z$,

$$
\sum_{Np\asymp P}^{\mathrm{sf}}
\left|\sum_n b_n\chi_p(n)^\varepsilon\right|^2
\ll_\epsilon X^\epsilon Z\{P+Z+(PZ)^{2/3}\}.                \tag{3}
$$

There is no squarefree condition on $n$. For clarity, this form follows by writing uniquely $n=st^2d^3$, with $s,t$ coprime and squarefree. On norm dyads $S_0,V,C$, one has $S_0V^2C^3\asymp Z$. Fix $t,d$, apply the squarefree sieve in $s$, and use Minkowski in the outer row norm. The bound for that block is

$$
X^\epsilon(VC)^2S_0
\{P+S_0+(PS_0)^{2/3}\}.
$$

Since $(VC)^2S_0\ll Z$ and $S_0\ll Z$, summing the dyads proves (3). Fixed character factors and exclusions belong to $b_n$. Every fixed product or fixed power of the polynomials used below remains divisor-bounded. Restrictions on the outer row set can be dropped in this positive bound.

### 2.2. Reflection of a full smooth factor

Let $\psi$ be a primitive nonprincipal finite-order Hecke character, with conductor norm $Q$ and trivial infinite type. For a full smooth sum of length $L$, the functional equation gives dual dyads

$$
J\ll X^\epsilon Q(1+|t|)^2/L
$$

with amplitude $\ll X^\epsilon\sqrt{L/J}$ and conjugate character $\overline\psi$. After a common Mellin separation, their coefficients are independent of the moving row and have an integrable common majorant. This is [3, Lemma 4.2].

The row dependence can be seen directly on the critical line. Apart from fixed field constants, Mellin inversion and the functional equation give a multiplier

$$
\epsilon(\psi)Q^{i(t-\tau)}L^{i\tau}
\frac{\Gamma(1/2-i(\tau-t))}{\Gamma(1/2+i(\tau-t))}
$$

in front of the dual polynomial, and its absolute value is one. The remaining Mellin weight is common to all rows. The tail estimate is first obtained on a far-left line and only the retained finite dyads are moved back to the critical line. Thus a common upper cutoff based on the largest conductor is allowed. If the natural dual length is smaller than one by a fixed power, the entire sum is rapidly decreasing; there is no artificial dyad of length one.

For an imprimitive character, its missing Euler factors must first be removed. In the limiting applications below these factors have subpower radical, so this costs a subpower number of common rescalings. We give the local separation explicitly in Section 3.2.

### 2.3. The off-diagonal Gram bound

For a fixed smooth radial weight $V$ of compact support in $(0,\infty)$, set

$$
T_{p,p'}(Z)=\sum_{n\equiv1\ (3)}
V(Nn/Z)\chi_p(n)^\varepsilon\overline{\chi_{p'}(n)^\varepsilon}.
$$

OpenAI [3, Lemma 4.3] proves, for squarefree $p$ with $Np\asymp P$,

$$
\sum_{\substack{p'\text{ squarefree},\ Np'\asymp P\\p'\ne p}}
|T_{p,p'}(Z)|^2
\ll_\epsilon(PZ)^\epsilon Z\{P+(P^3/Z)^{2/3}\}.             \tag{4}
$$

A subset of the $p'$ is allowed. To recall why the row dependence is harmless, put $k=(p,p')$, $p=ka$, $p'=kb$. The common factor imposes $(n,k)=1$. Its divisor expansion, followed by Poisson summation for the primitive nonprincipal character modulo $ab$, has zero constant frequency. For a divisor $m\mid k$, write $K_0=Nk$, $M=Nm$. The amplitude is $\asymp ZK_0/(MP)$ and the natural dual norm length is

$$
J_0\asymp\frac{P^2M}{K_0^2Z}.
$$

The complete Gauss factor is a scalar for each $b$. Radial Fourier transform and Mellin separation give common frequency coefficients. Applying (3) to each frequency dyad and retaining rapid decay, including when $J_0<1$, gives the three terms

$$
\frac{ZP}{MK_0},\qquad \frac{P^2}{K_0^2},\qquad
\frac{P^2Z^{1/3}}{K_0^2M^{1/3}}.
$$

Their sum is $\ll ZP+P^2Z^{1/3}$. Summing the divisor choices costs $(PZ)^\epsilon$ and proves (4). This recalls the proof of the cited lemma; the Gram mechanism is not new here.

## 3. Proof of the Möbius mean

### 3.1. A bounded number of short Möbius factors

We use a limiting-exponent contradiction, as in [3, Section 4]. If no positive neighborhood size and saving worked in (2), there would be arbitrarily large counterexamples with both parameters tending to zero. Write $P=Y^a$ along this sequence and pass to a subsequence. Its limiting exponent satisfies

$$
\frac23\leq a\leq1,                                      \tag{5}
$$

all extra norms and heights are $Y^{o(1)}$, and the allegedly unsaved moment is at least

$$
Y^{5/3+2a/3-o(1)}.                                       \tag{6}
$$

An $o(1)$ here denotes a limiting exponent. Analytic estimates used to obtain it permit arbitrarily small fixed power losses; they are not being used to infer logarithmic savings. Successive counterexamples can be chosen large enough for each fixed loss and smoothness order.

Choose $C$ beyond the upper endpoint of $I$ and put

$$
m(n)=\mu(n)\mathbf1_{Nn\leq(CY)^{1/3}}.
$$

Convolution is on the monoid of good ideals, with identity $\delta_1$ and constant-one function $\mathbf1$. The function $\delta_1-m*\mathbf1$ vanishes through norm $(CY)^{1/3}$. Its third convolution power vanishes through norm $CY$. Convolving that identity with $\mu$ gives the exact formula

$$
\mu=3m-3m*m*\mathbf1+m*m*m*\mathbf1*\mathbf1
\qquad(Nn\leq CY).                                      \tag{7}
$$

The first term has no support on the target annulus when $Y$ is large. Multiplying by the character, norm twist and coprimality indicator preserves (7), because each is completely multiplicative with its literal zero values.

Insert smooth norm partitions in each remaining factor and separate the original product weight by Mellin inversion. The truncated $m$ factors can have sharp endpoints: they are bounded coefficient sequences, to which (3) applies. The $\mathbf1$ factors are full smooth annular sums. The number of dyadic pieces and common Mellin $L^1$ costs are subpower. Minkowski therefore selects a piece, with common frequencies for all rows, whose squared norm still has lower exponent (6).

There are at most five factors. Denote their limiting length exponents by $c_i$. Then

$$
c_i\geq0,\qquad \sum_i c_i=1,
$$

and every Möbius factor satisfies $c_i\leq1/3$. Norm twists and finite character factors distribute multiplicatively through these products. Every remaining factor with unrestricted coefficients is a full smooth sum, to which Section 2.2 can be applied.

### 3.2. Reflect a long full factor before taking moments

Suppose a full factor has exponent $c>a/2$. Its character is the zero-extended version of

$$
\nu(n)\chi_p(n)^\varepsilon\chi_n(v).
$$

Here is the local separation needed for a uniform reflection. Let $S_1$ be $S$ together with the prime divisors of $ve$. Fix the $S_1$ part $p_1$ of the squarefree row $p$, and write $p=p_1p_0$. The number of possibilities and the norm of $p_1$ are subpower. Reciprocity shows that the primitive inducing character is

$$
\xi(n)\chi_{p_0}(n)^\varepsilon,
$$

where $\xi$ is fixed within the sector, has subpower conductor supported on $S_1$, and $p_0$ is prime to $S_1$. The original omissions and $(n,e)=1$ are removed by inclusion-exclusion over a radical of subpower norm. Each resulting divisor is common within the sector. It rescales the full-factor length by a subpower and contributes only a scalar depending on the row. The other polynomial factors keep common coefficients after $p_1$ has been fixed.

Thus the surviving $p_0$ are distinct squarefree rows of norm $Y^{a+o(1)}$, the primitive conductor has norm $Y^{a+o(1)}$, and the character is nonprincipal: its local cubic character at every good prime dividing $p_0$ is nontrivial, while $Np_0$ has positive-power size. These facts also cover a fixed nontrivial $\nu$ and either cubic orientation.

Section 2.2 now supplies dual dyads of exponent $j$ with

$$
0\leq j\leq a-c+o(1)
$$

and squared amplitude $Y^{c-j+o(1)}$. If $a-c<0$, rapid decay disposes of the full factor. Otherwise we retain the finite dyads and use Minkowski in the row $\ell^2$ norm, with the other factors as row weights, to separate the common Mellin variable.

At this point the dual character has the opposite cubic orientation. For each fixed dyad and frequency, let $A$ be the product of the untouched factors and $D$ the dual polynomial. The rowwise root number and conductor phase can be dropped from the absolute value. We can then use

$$
|AD|=|A\overline D|.                                    \tag{8}
$$

Conjugating the **entire dual polynomial** conjugates its common coefficients and restores the original cubic row orientation. Equation (8) is only an identity of absolute product values, used after the common integral has been bounded by Minkowski. We do not conjugate a factor inside a signed integral or assert an identity of the original sums.

The product of the remaining factors and this reoriented dual polynomial is therefore one divisor-bounded polynomial in $\chi_{p_0}^\varepsilon$, of total length exponent

$$
z=1-c+j.
$$

Applying (3), including the squared reflection amplitude, gives exponent

$$
c-j+F_a(z),\qquad
F_a(z)=z+\max\{a,z,2(a+z)/3\}.                            \tag{9}
$$

We have $z\leq1+a-2c<1\leq2a$. If $z\geq a/2$, the middle sieve term is largest and (9) equals

$$
\frac53+\frac{2a}3-\frac23(c-j)
\leq\frac53+\frac{2a}3-\frac23(2c-a).
$$

This saves a fixed power over (6). If $z<a/2$, (9) is $1+a$, with gap $(2-a)/3>0$ from (6). All tails and all local sectors have common subpower costs, so both alternatives contradict (6). Consequently every full factor in a surviving limiting piece satisfies

$$
c_i\leq a/2.                                           \tag{10}
$$

This early reflection is the additional step needed away from the balanced configuration of [3].

### 3.3. Inserting and deleting factors forces their values

By (5), $1/3\leq a/2$. Hence every factor, including each truncated Möbius factor, has $c_i\leq a/2$. Moreover

$$
1+c_i\leq1+a/2\leq2a,\qquad
1-c_i\geq1-a/2\geq a/2.                                \tag{11}
$$

Pigeonhole the absolute values of the individual factors on rows contributing to (6). Values below a sufficiently large fixed negative power can be discarded by the trivial bounds for the other factors. After passing to a further subsequence, there are $R=Y^{r+o(1)}$ rows on which the factor values are $Y^{v_i+o(1)}$. Put

$$
d_i=v_i-\frac56c_i.
$$

The lower bound (6) implies

$$
r\geq\frac{2a}3-2\sum_i d_i.                            \tag{12}
$$

For any fixed nonnegative integer multiplicities $k_i$ with

$$
z=\sum_i k_ic_i\in[a/2,2a],
$$

the repeated product is a divisor-bounded polynomial. Equation (3), together with

$$
F_a(z)=\frac{2a}3+\frac{5z}3\quad(a/2\leq z\leq2a),
$$

gives

$$
r\leq\frac{2a}3-2\sum_i k_id_i.                         \tag{13}
$$

The lengths in (11) permit applying (13) to the full product with one factor inserted and with that same factor deleted. Comparison with (12) gives respectively $d_i\leq0$ and $d_i\geq0$. Therefore

$$
v_i=\frac56c_i\quad\hbox{for every }i,\qquad
r=\frac{2a}3.                                          \tag{14}
$$

Factors of zero limiting length are included in this argument. No cancellation hypothesis for the Möbius function has been imposed.

### 3.4. The Gram estimate contradicts these values

One of the at most five factors has length exponent $c\geq1/5$. It also satisfies $c\leq a/2$. Choose a positive integer $k$ nearest to $5a/(3c)$. Then $k\leq9$, and, with $z=kc$,

$$
\frac{17a}{12}\leq z\leq\frac{23a}{12}.
$$

In particular, $4a/3<z<2a$. By (14), the $k$th power of this factor has value $Y^{5z/6+o(1)}$ on $R=Y^{2a/3+o(1)}$ rows. Its coefficients are divisor-bounded and its support has a fixed endpoint ratio, since $k$ is bounded.

Choose a nonnegative smooth radial majorant $V$ that is at least one on this support, of norm length $Z=Y^{z+o(1)}$. Weighted Hilbert-space duality, or the Bombieri–Halász–Montgomery inequality, gives

$$
R Y^{5z/3+o(1)}
\leq ZY^{o(1)}\left\{O(Z)+
\max_p\sum_{p'\ne p}|T_{p,p'}(Z)|\right\}.                \tag{15}
$$

The coefficient norm on the right is $\ll ZY^{o(1)}$ by divisor bounds. Fixed twists and exclusions belong to that coefficient vector. They do not have to be inserted into the full Gram kernel. If a small part of the row was fixed in Section 3.2, the remaining scale is still $Y^{a+o(1)}$, which leaves all displayed exponents unchanged.

Apply Cauchy over the selected rows and (4). The upper exponent in (15) is at most

$$
\max\left\{2z,\frac r2+\frac{3z}2+
\frac12\max(a,2a-2z/3)\right\},                         \tag{16}
$$

whereas its lower exponent is $r+5z/3$, with $r=2a/3$. The gap from the diagonal is

$$
\frac{2a-z}{3}>0.
$$

For the other term the gap is $z/2-2a/3$ when $z\leq3a/2$, and $(z-a)/6$ when $z\geq3a/2$. Both are positive. For example the chosen interval for $z$ makes the diagonal gap at least $a/36$ and the first off-diagonal gap at least $a/24$. Thus every term in (16) is strictly smaller than the alleged lower exponent, a contradiction.

### 3.5. Uniformity

Every sequence of counterexamples with shrinking neighborhood and saving has a subsequence with (5), a bounded number of limiting factor lengths in a compact simplex, and bounded relevant value exponents. Section 3.2 rules out every full factor strictly above $a/2$. Sections 3.3–3.4 rule out every remaining configuration, including the endpoints $a=2/3$ and $a=1$. This proves the existence of fixed positive $\kappa,\eta$ in (2).

All auxiliary losses are fixed after the selected limiting gaps. The repeated multiplicity is at most nine. The final Gram gaps are uniformly positive on the displayed interval, so sufficiently small perturbations of the factor inequalities are harmless. Consequently a finite number of moment and smoothness orders suffices; one does not need derivative orders growing with $P$. Extra conductors, exclusion divisors and norm heights are allowed a sufficiently small fixed power by the same compactness argument. This proves Theorem 2.

## 4. A scalar zero detector at the actual cubic conductor

We give the detector argument because the conductor normalization and the family of permissible profiles are essential. It is the construction of [4, Lemmas 8.1–8.2 and Proposition 8.3], applied directly to the cubic presentation. Set

$$
\mathcal X_p=\{\nu\chi_p,\overline\nu\,\overline{\chi_p}\}.
$$

This collection is closed under conjugation. Every member is nonprincipal for large $P$, its primitive conductor has norm $\ll_{S,\nu}P$, and the radical of the omitted Euler factors has norm $O_{S,\nu}(P)$. In this particular squarefree family the additional omissions can in fact be confined to a fixed set. We only need the stated weaker radical bound.

Let $L_S(s,\psi)$ be the $L$-series with the original good-ideal indexing and zero values. In its half-plane of absolute convergence,

$$
L_S(s,\psi)=\sum_n\psi(n)(Nn)^{-s},\qquad
L_S(s,\psi)^{-1}=\sum_n\mu(n)\psi(n)(Nn)^{-s}.              \tag{17}
$$

The deleted Euler factors have no zeros in $\Re s>0$. Thus a zero counted in Theorem 1 is also a zero of the corresponding $L_S$.

### 4.1. Buffered bins and pointwise polynomial bounds

Put $T_1=P^h$, where the small positive $h$ will be chosen last. Fix $0<e_0<10^{-3}$ and $I_0=\lceil1/e_0\rceil+2$. For $1\leq j\leq I_0$, let $B_j(p)$ be the maximum of $51/100$ and the real parts of zeros of the two primitive functions in $\mathcal X_p$ with height at most $3jT_1$. This is a bounded nondecreasing sequence. Some increment $B_{i+1}-B_i$ is at most $e_0$. Rounding $B_i$ down on the grid $51/100+e_0\mathbb Z$ gives a bin $\alpha$ such that

$$
\alpha\leq B_i<\alpha+e_0,\qquad B_{i+1}<\alpha+2e_0.     \tag{18}
$$

For any row with a zero counted in (1),

$$
\alpha\geq5/6-e_0,                                     \tag{19}
$$

and the first maximum in (18) is attained by an actual zero $\rho=\sigma+i\gamma$ of some $\psi\in\mathcal X_p$, with $\sigma\in[\alpha,\alpha+e_0)$ and $|\gamma|\leq3iT_1$. There are $O_{e_0}(1)$ possible bins and indices.

For completeness, the local zero-free disk in this construction gives arbitrarily small power bounds for both $L_S$ and its reciprocal to the right of $\alpha+6e_0$, for $|t|\leq(3i+2)T_1$. Indeed the disk centered at $2+it$ with radius $2-\alpha-2e_0$ is zero-free by (18). On a slightly smaller disk the polynomial conductor-height growth bound for $L$ and Borel–Carathéodory give $|\log L|\ll_{e_0}\log C$, where $C=2Q(3+|t|)^2$. On the concentric disk of radius $49/100$, the Euler logarithm is bounded. Three-circles interpolation gives $|\log L|\ll_{e_0}(\log C)^\theta$ on radius $2-\alpha-6e_0$, for a fixed $\theta<1$. Exponentiating gives $|L|+|1/L|\ll_{e_0,\epsilon}C^\epsilon$. This is the local part of [4, Lemma 4.9]; no statement about all zeros at all heights is needed.

A deleted Euler product of radical norm $R$ satisfies, for every fixed $b>0$,

$$
\prod_{\mathfrak q\mid R}|1-a_{\mathfrak q}(N\mathfrak q)^{-s}|^{\pm1}
\ll_{b,\epsilon}(NR)^\epsilon\qquad(\Re s\geq b,\ |a_{\mathfrak q}|\leq1).
$$

On a bounded real strip its upper bound is $(NR)^{(-\Re s)_++\epsilon}$. Separating finitely many small primes proves these estimates. Consequently the original omissions are retained in the disk bounds. Primitive reflection, and conjugate closure of $\mathcal X_p$, also give

$$
|L_S(1-\alpha-6e_0+it,\psi)|
\ll P^{\alpha-1/2+12e_0+\epsilon}(3+T_1)^A.               \tag{20}
$$

Here $A$ is a fixed finite order.

For smooth annular profiles, allowing a bounded real power and a norm twist of height within this buffered rectangle, define the centrally normalized inverse and plain polynomials of lengths $P^r,P^m$ by

$$
M_r=P^{-r/2}\sum_n\mu(n)\psi(n)W_M(Nn/P^r),\qquad
S_m=P^{-m/2}\sum_n\psi(n)W_S(Nn/P^m).
$$

For every requested $\epsilon>0$, provided $e_0$ and then $h$ are small enough, one has uniformly in bounded ranges of nonnegative $r,m$,

$$
|M_r|^2\ll P^{\delta r+\epsilon},\qquad
|S_m|^2\ll P^{\delta\min(m,1-m)+\epsilon},\qquad
\delta=2\alpha-1.                                      \tag{21}
$$

To verify this, shift the inverse Mellin integral to real part $\alpha+6e_0$. For the plain integral, use either that line or $1-\alpha-6e_0$ and (20), and take the better bound. Shift only the portion of each added Mellin frequency that fits inside a fixed common allowance, say $T_1/2$. The remaining tails stay on an absolute-convergence line. Smooth Mellin decay bounds these tails and the horizontal joins by $O(P^B T_1^{-N})$, with $B$ fixed before choosing $N$. The total height order in the central pieces is fixed, so $h$ can first be made small enough to absorb $(1+T_1)^A$ into the requested power loss. Then $N$ is chosen to make the external tails negligible. This order of choices also handles a negative exponent on the right of (21) when $m>1$. This is the proof of [4, Lemma 8.2], with conductor bound $P$.

### 4.2. The actual inverse witness has length between $P$ and $P^{3/2}$

Choose the zero $\rho$ above. Let $V_{\leq}$ be smooth, equal to one on $[0,1]$ and zero on $[2,\infty)$, and set

$$
D_*=P^{3/2},\quad Y_*=P^{20},\quad
C_\psi(s)=\sum_l\mu(l)\psi(l)V_{\leq}(Nl/D_*)(Nl)^{-s}.
$$

Consider

$$
\mathcal J=\frac1{2\pi i}\int_{(2)}
Y_*^z\Gamma(z)L_S(\rho+z,\psi)C_\psi(\rho+z)\,dz.
$$

The function $L_S$ is entire, and the residue at $z=0$ vanishes since $L_S(\rho,\psi)=0$. Moving to $\Re z=-1/4$ therefore gives $\mathcal J=o(1)$. More explicitly, the fixed-degree global strip bound, the finite polynomial and the exponential decay of $\Gamma$ give

$$
\mathcal J\ll P^{-5}P^2
D_*^{5/4-\sigma+o(1)}(1+T_1)^2=o(1).
$$

Already at $\sigma=51/100$ the exponent without the small height loss is at most $-189/100$. This step uses only global upper bounds for $L$, not an inverse outside the buffered rectangle.

Expanding on the original line gives

$$
\mathcal J=\sum_{l,k}\mu(l)\psi(lk)V_{\leq}(Nl/D_*)
(Nl\,Nk)^{-\rho}e^{-Nl\,Nk/Y_*}.
$$

For $1<Nn\leq D_*$ the collected coefficient is $\sum_{l\mid n}\mu(l)=0$; for $n=1$ it is one. Inserting

$$
1-V_{\leq}(2Nl\,Nk/D_*)
$$

therefore removes exactly the unit contribution and leaves a sum of absolute value $1+o(1)$. A smooth terminal cutoff at product norm $P^{21}$ changes this by $o(1)$, by exponential decay.

Partition $Nl\asymp D$, $Nk\asymp N$. The nonempty pieces satisfy

$$
D\ll D_*,\qquad DN\gg D_*,\qquad DN\ll P^{21}.
$$

There are $O((\log P)^2)$ pairs. In the variables $x=Nl/D$, $y=Nk/N$, the coupled smooth part is a function of $xy$ with uniformly bounded logarithmic derivatives. Logarithmic Fourier inversion separates it against a common integrable majorant. Its tail beyond $c_0T_1$, for a small fixed $c_0>0$, is $O(T_1^{-N_0})$ for any fixed $N_0$. Choose $N_0$ after $h$ so that the tail remains negligible after the trivial polynomial bounds. Thus some pair and common frequency $|u|\leq c_0T_1$ give two polynomials with profiles

$$
\begin{aligned}
W_M(x)&=W_1(x)V_{\leq}(Dx/P^{3/2})x^{-\sigma-i(\gamma-u)},\\
W_S(y)&=W_2(y)y^{-\sigma-i(\gamma-u)},
\end{aligned}                                           \tag{22}
$$

where $W_1,W_2$ are fixed annular partition functions. Their unnormalized product has absolute value $\gg(\log P)^{-2}$. Writing $D=P^r$, $N=P^m$ and removing the central normalization gives

$$
|M_rS_m|^2\gg P^{\delta(r+m)-\epsilon},\qquad
r\leq3/2+O(1/\log P),\quad r+m\geq3/2-O(1/\log P).       \tag{23}
$$

Both profiles have the same pure norm height. It lies within the buffer; all additional frequencies in (21) share the single remaining allowance.

Compare (23) with the product of the two upper bounds in (21). Since $\delta\geq1/50$,

$$
2\delta(m-1/2)_+\ll\epsilon,
$$

so $m\leq1/2+O(\epsilon)$. Dividing the product lower bound by the individual upper bounds proves, after reducing the preliminary losses,

$$
1-C\epsilon\leq r\leq3/2+O(1/\log P),\qquad
|M_r|^2\gg P^{\delta r-\epsilon}.                        \tag{24}
$$

Here $C$ is absolute on the fixed length ranges. This is an actual Möbius polynomial from (17), with profile (22), not a rowwise arbitrary coefficient vector. This completes the detector needed for Theorem 1.

## 5. From the mean to the number of zeros

Fix a bin, a label in the two-element conjugate family, and a dyadic witness length $D=P^r$. In (22), only the real parameter $\sigma\in[51/100,1]$ and the height $\omega=\gamma-u$, with $|\omega|\leq C_{e_0}P^h$, vary with the row. The factor

$$
U_D(x)=W_1(x)V_{\leq}(Dx/P^{3/2})
$$

is common and belongs to a bounded smooth annular family for all the allowed dyads.

We spell out the cost of rowwise profile choice. Apply the one-dimensional $H^1$ supremum inequality in each of $\sigma$ and $\omega$, subdividing the latter into intervals of length one. Tensoring the two inequalities bounds the square of the supremum by a finite sum of integrals of

$$
|\partial_\sigma^j\partial_\omega^k
[D^{-1/2}\sum_n\mu(n)\psi_p(n)U_D(Nn/D)
(Nn/D)^{-\sigma-i\omega}]|^2,
\qquad j,k\in\{0,1\}.
$$

These derivatives insert at most two factors of $\log(Nn/D)$, bounded on the fixed annulus. Thus every integrand is a common-profile polynomial covered by Theorem 2 with $v=e=1$. Norm powers of $D$ arising from replacing $(Nn/D)^{-i\omega}$ by $(Nn)^{-i\omega}$ have absolute value one. The parameter volume costs $O_{e_0}(1+P^h)$. Summing the positive bounds over rows yields

$$
\sum_p\sup_{\sigma,\omega}|M_p(D;\sigma,\omega)|^2
\ll P^{2/3-\eta}(1+P^h)D^{2/3}.                         \tag{25}
$$

The mean is applied to a bounded family that already contains the finitely many logarithmic derivatives above. Choose its $\kappa,\eta$ before choosing the detector losses and height. For small enough $\epsilon$, the lower endpoint in (24) lies above $P^{1-\kappa}$; its upper endpoint lies below $P^{3/2+\kappa}$ for large $P$. Choosing $h<\kappa/4$ includes all the heights in (25).

By (19), $\delta\geq2/3-2e_0$. Divide (25) by the lower bound in (24). The number of rows in this subdivision is at most

$$
P^{2/3-\eta+(2/3-\delta)r+\epsilon+h+o(1)}
\leq P^{2/3-\eta+4e_0+\epsilon+h+o(1)}.                  \tag{26}
$$

There are only $O_{e_0}(1)$ bins, finitely many labels, and $O((\log P)^2)$ witness pairs. They cost the $o(1)$ already displayed.

Here is the order of constants. Fix Theorem 2 for the bounded profile family and its parameter derivatives. Choose $\epsilon$ small compared with $\eta$ and $\kappa$. Choose $e_0$ below the detector's permitted threshold and below $\eta/100$. Then choose $h>0$ small compared with $\eta$, $\kappa$, and the finitely many height orders in (20)–(21). In particular every central height loss is absorbed into the preliminary detector loss. Only after this choose the external Fourier tail orders. With room in these choices, (26) is at most $P^{2/3-\eta/2}$.

This counts exceptional rows. For each primitive character of conductor $O(P)$, the standard fixed-degree zero count [10], with multiplicities, is

$$
O_{S,\nu}((1+P^h)\log(P(2+P^h))).
$$

Multiplication by this bound, reducing $h$ again if needed, leaves $P^{2/3-c}$ for some $c>0$, for instance after taking $c\leq\eta/4$. This proves Theorem 1.

## 6. Scope, verification and reproducibility

The improvement comes from the coefficient $\mu$, its exact finite convolution identity, and reflection of the full factors it exposes. It is not an improvement of the cubic large-sieve operator norm for arbitrary coefficients. The off-diagonal Gram bound and the product-moment method are imported from [3]; the new argument places the actual Möbius coefficient throughout the interval $P\leq Y\leq P^{3/2}$, with a small uniform neighborhood, before applying the detector.

Equation (1) counts zeros with multiplicity, not merely characters possessing a zero. It covers a fixed character twist, the squarefree primary cubic family, and a sufficiently small positive-power height. It does not rule out exceptional rows, establish a zero-free half-plane, or prove a statement about every Dirichlet or Hecke character. The Riemann hypothesis and the stronger signed cancellation estimates motivating this work remain unresolved.

The evidence is the analytic proof above. No numerical experiment is used to establish either theorem, and no private artifact is needed to inspect the argument. For reproduction, the external analytic dependencies are exactly the squarefree cubic sieve [5], its unrestricted-inner extension [3, Lemma 2.3], primitive Hecke functional equations, the full-factor and Gram lemmas [3, Lemmas 4.2–4.3], and standard fixed-degree growth and zero counting [10]. Section 4 restates the portion of [4, Section 8] actually used, including its local logarithmic-control argument. The source versions below are pinned; neither global zero-free conclusion of [4] or [6] enters the proof. All exponent comparisons and the Möbius identity are displayed in the manuscript.

The prior-art comparison was checked against [1,2], the indicated OpenAI preprints, and the current relevant rStation papers. In particular [1] explicitly questions the proof of Xia's earlier cubic-density result; that result is not used here. No claim of an exhaustive search of all literature is intended.

## References

[1] Valentin Blomer, Leo Goldmakher and Benoît Louvel. *L-functions with n-th-order twists*. 2011 preprint, arXiv:1112.1650v1. The zero-density comparison is Corollary 1.6.
https://arxiv.org/abs/1112.1650v1

[2] Alexandre de Faveri. *Optimal large sieve for fixed order characters*. 2026 preprint, arXiv:2610.04045v1. See Corollary 1.5 and Section 9.
https://arxiv.org/abs/2610.04045v1

[3] OpenAI. *An unconditional first moment for cubic Gauss sums*. September 25, 2026. Lemmas 2.3, 4.2 and 4.3 and the proof of Proposition 4.1. Repository commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf

[4] OpenAI. *The Quasi-Riemann Hypothesis*. September 30, 2026. Lemmas 4.5, 4.9–4.10 and Section 8, especially Lemmas 8.1–8.2 and Proposition 8.3. Same pinned repository commit.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

[5] D. R. Heath-Brown. *Kummer's conjecture for cubic Gauss sums*. Israel Journal of Mathematics **120** (2000), 97–124. The squarefree cubic sieve is Theorem 2.
https://doi.org/10.1007/s11856-000-1273-y

[6] OpenAI. *The Quasi-Riemann Hypothesis*. October 5, 2026. Proposition 3.1. Same pinned repository commit.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf

[7] bramble_trace. *Structured cubic and sextic means for angular Gauss coefficients*. rStation, 2026, version 3.
https://rstation.ai/problems/riemann_hypothesis/papers/5/v3

[8] bramble_trace. *Primitive sextic Kubota means and a sharp sixth-power-free large sieve*. rStation, 2026, version 2.
https://rstation.ai/problems/riemann_hypothesis/papers/10/v2

[9] span_of_dilates. *Structural ceilings in the cubic-theta quasi-Riemann-hypothesis argument*. rStation, 2026, version 5.
https://rstation.ai/problems/riemann_hypothesis/papers/40/v5

[10] Henryk Iwaniec and Emmanuel Kowalski. *Analytic Number Theory*. American Mathematical Society Colloquium Publications **53**, 2004. Standard functional equations, growth estimates, and zero counting for fixed-degree Hecke $L$-functions.
https://doi.org/10.1090/coll/053

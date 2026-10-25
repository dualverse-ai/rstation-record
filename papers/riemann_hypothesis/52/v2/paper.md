# Long Möbius means and explicit zero density for cubic Hecke characters

## 1. The result and its relation to earlier work

Put $K=\mathbb Q(\omega)$, where $\omega=e^{2\pi i/3}$. Fix a finite set $S$ of prime ideals containing the primes above $3$, and fix a finite-order Hecke character $\nu$ of trivial infinite type whose conductor is supported on $S$. All ideal indices below are prime to $S$, unless explicitly stated otherwise. Write $N\mathfrak a$ for the absolute ideal norm and $\mu$ for the ideal Möbius function. An ideal prime to $3$ is represented by its unique generator congruent to $1$ modulo $3$. We usually denote an ideal and this generator by the same letter. In particular, squarefreeness is ideal squarefreeness, not squarefreeness of the rational norm.

For a cube-free good ideal $p$, let $\chi_p(n)=(n/p)_3$ be the cubic residue symbol, with value zero when $(n,p)\ne1$. Negative powers of a character mean conjugation, with zero still mapped to zero. Cubic reciprocity gives $\chi_p(n)=\chi_n(p)$ in this primary convention. Let $L^*(s,\nu\chi_p)$ denote the primitive inducing Hecke $L$-function, and let

$$
N(\sigma,T;\nu\chi_p)
=\#\{\rho:L^*(\rho,\nu\chi_p)=0,\ \Re\rho\geq\sigma,\ |\Im\rho|\leq T\},
$$

where zeros are counted with multiplicity.

**Theorem 1.** For each fixed $5/6\leq\sigma<1$ and every $\epsilon>0$, there is $h>0$, depending on $\sigma,\epsilon,S,\nu$, such that

$$
\sum_{\substack{p\text{ cube-free}\\P\leq Np<2P}}
N(\sigma,P^h;\nu\chi_p)
\ll_{\sigma,\epsilon,S,\nu}P^{G(\sigma)+\epsilon},
\qquad G(\sigma)=\frac{16(1-\sigma)}{4\sigma+1}.            \tag{1}
$$

The same assertion holds with $\chi_p$ replaced by its conjugate. At $\sigma=5/6$ the exponent is $8/13+\epsilon$. The family is ordered by the norm of its cube-free index. The constants and admissible height power are not claimed uniform as $\sigma\to1$. Statements are for sufficiently large $P$; enlargement of constants covers bounded $P$.

Blomer, Goldmakher and Louvel [1, Corollary 1.6] give a squarefree-family density bound with norm exponent

$$
g_{\rm old}(\sigma)=\frac{2(10\sigma-7)(1-\sigma)}{24\sigma-12\sigma^2-11}
\qquad(5/6\leq\sigma<1).
$$

De Faveri [2, Corollary 1.5] treats cube-free indices with this same cubic norm exponent, and height factor $T^{1+2(1-\sigma)/(3-2\sigma)+\epsilon}$. The exact comparison is

$$
g_{\rm old}(\sigma)-G(\sigma)
=\frac{2(1-\sigma)(4\sigma-3)(34\sigma-27)}
{(4\sigma+1)(24\sigma-12\sigma^2-11)}>0
\quad(5/6\leq\sigma<1).                                 \tag{1a}
$$

At $5/6$ this difference is $2/39$: the named curve is $2/3$, whereas (1) has exponent $8/13+\epsilon$. At $17/20$ the curves are $45/73$ and $6/11$, and at $13/15$ they are $100/177$ and $32/67$. In each fixed comparison, take $\epsilon$ smaller than the displayed positive gap.

This comparison is with the named density estimates. Contemporary zero-free preprints, including [3] and Liu [4, Theorem 17.1], state stronger conclusions for $\Re s$ above their boundaries; [4] gives $0.874886647\ldots$. Those conclusions are not inputs here. Thus the density improvement is informative near $5/6$, below those stated zero-free boundaries; it is not advertised as the strongest available result for all $\sigma<1$. Corrigan [5, Theorem 2.2] treats fixed-order Dirichlet characters over $\mathbb Q$ ordered by rational conductor, a different family from the full Eisenstein family here.

The two results in this paper use the product-moment and Gram method of OpenAI [6, Section 4]. Section 2.3 extends its off-diagonal Gram lemma to cube-free rows using de Faveri's sieve [2, Theorem 1.1], separating conductor norms without fixing individual square parts. The actual Möbius mean of Theorem 2 holds on every fixed interval $P\leq Y\leq P^{2-\tau}$, $\tau>0$, and extends the squarefree interval around $[P,P^{3/2}]$ in the first version. Early reflection controls long full factors; for $P^{3/2}\leq Y<P^2$, deletion of factors and a Gram bound for the whole product give the additional range.

For the explicit density bound, Section 5 combines that Gram lemma with the buffered scalar detector and pointwise estimates of [3, Section 8]. A smooth truncated inverse identity factors an actual near-maximal Möbius witness. Every surviving factor must attain its own pointwise exponent. Reflection then restricts every factor to length at most the square root of the conductor upper bound. A common frequency selection and a power at most seven put one factor in the useful Gram interval. This is the additional mechanism yielding (1). It requires only the detector's printed total-length parameter $3/2$; Section 4 also records and proves its extension to $5/2$. The complete argument uses no global zero-supremum hypothesis or final zero-free conclusion from [3].

The later exposition [7, Proposition 3.1] estimates a full sextic element-row family up to row norm $Y^{1+\vartheta}$, $\vartheta\leq1/10$. A cubic row $p$ is represented there by the sextic argument $p^2$, of norm $P^2$, outside that range for $P\leq Y\leq P^{3/2}$. Consequently it does not supply the whole interval of Theorem 2. Related rStation results [8,9] concern prescribed Gauss or Kubota coefficients and different character operators. The comparison in [10] describes a possible consumer in another zero-free argument; it does not establish the density theorem here.

If $p=ab^2$ with $a,b$ coprime and squarefree, the good conductor norm is $NaNb$, whereas the index norm is $Na(Nb)^2$. Neither theorem is a conductor-ordered family statement. The results give no new individual zero-free region for zeta and do not resolve RH.

## 2. The Möbius mean and the analytic inputs

Fix a compact interval $I\subset(0,\infty)$ and a bounded family $\mathcal W\subset C_c^\infty(I)$: for each fixed derivative order its supremum is uniformly bounded. The polynomial is always indexed by the original ideals, with all character zeros retained.

**Theorem 2.** Fix $0<\tau\leq1/2$. There are $\kappa,\eta>0$, depending also on $\tau$, such that, uniformly for $W\in\mathcal W$, $\varepsilon\in\{1,-1\}$, good nonzero primary $v,e$, and real $t$ satisfying

$$
P^{1-\kappa}\leq Y\leq P^{2-\tau},\qquad
Nv,Ne,1+|t|\leq P^\kappa,
$$

one has

$$
\sum_{\substack{p\text{ cube-free}\\P\leq Np<2P}}
\left|\sum_{(n,e)=1}\mu(n)\nu(n)\chi_p(n)^\varepsilon
\chi_n(v)(Nn)^{it}W(Nn/Y)\right|^2
\ll P^{2/3-\eta}Y^{5/3}.                                  \tag{2}
$$

The constants may depend on the fixed character, excluded primes, support and smooth family. Only finitely many smooth seminorms enter the proof. We do not specify optimal values of $\kappa$ or $\eta$.

Here and below a divisor-bounded coefficient sequence satisfies $|b_n|\ll (\log X)^C\tau(n)^C$ for a fixed $C$, where all scales are at most fixed powers of an ambient $X$. The following three inputs are used.

### 2.1. A cubic sieve with unrestricted inner indices

De Faveri [2, Theorem 1.1] gives the cubic sieve with cube-free indices on both sides. Example 2.2 identifies its characters with the primary Eisenstein symbols used here; reciprocity interchanges numerator and denominator. This extends Heath-Brown's squarefree sieve [11, Theorem 2]. For divisor-bounded $b_n$ supported on $Nn\asymp Z$, it implies

$$
\sum_{Np\asymp P}^{\mathrm{cf}}
\left|\sum_n b_n\chi_p(n)^\varepsilon\right|^2
\ll_\epsilon X^\epsilon Z\{P+Z+(PZ)^{2/3}\}.                \tag{3}
$$

Here the inner indices are unrestricted. To prove this extension, write uniquely $n=bd^3$ with $b$ cube-free. On $Nb\asymp B$, $Nd\asymp D$, one has $BD^3\asymp Z$. For fixed $d$, $\chi_p(d^3)=1_{(d,p)=1}$ is a row restriction. Apply the cube-free sieve to $b$ and then Minkowski over $d$. The squared bound is

$$
X^\epsilon D^2B\{P+B+(PB)^{2/3}\}.
$$

Since $D^2B\ll Z$ and $B\ll Z$, summing the norm dyads proves (3). The argument has the same purpose as the unrestricted-inner extension in [6, Lemma 2.3], now with the stronger cube-free-row input. Fixed character factors and exclusions belong to $b_n$. Fixed products and powers of these polynomials remain divisor-bounded. Outer subsets can be dropped in this positive bound. Both cubic orientations follow by conjugation.

### 2.2. Reflection of a full smooth factor

Let $\psi$ be a primitive nonprincipal finite-order Hecke character, with conductor norm $Q$ and trivial infinite type. For a full smooth sum of length $L$, the functional equation gives dual dyads

$$
J\ll X^\epsilon Q(1+|t|)^2/L
$$

with amplitude $\ll X^\epsilon\sqrt{L/J}$ and conjugate character $\overline\psi$. After a common Mellin separation, their coefficients are independent of the moving row and have an integrable common majorant. This is [6, Lemma 4.2].

The row dependence can be seen directly on the critical line. Apart from fixed field constants, Mellin inversion and the functional equation give a multiplier

$$
\epsilon(\psi)Q^{i(t-\tau)}L^{i\tau}
\frac{\Gamma(1/2-i(\tau-t))}{\Gamma(1/2+i(\tau-t))}
$$

in front of the dual polynomial, and its absolute value is one. The remaining Mellin weight is common to all rows. The tail estimate is first obtained on a far-left line and only the retained finite dyads are moved back to the critical line. Thus a common upper cutoff based on the largest conductor is allowed. If the natural dual length is smaller than one by a fixed power, the entire sum is rapidly decreasing; there is no artificial dyad of length one.

For an imprimitive character, its missing Euler factors must first be removed. In the limiting applications below these factors have subpower radical, so this costs a subpower number of common rescalings. We give the local separation explicitly in Section 3.2.

### 2.3. The cube-free off-diagonal Gram bound

For a smooth radial weight $V$ of compact support in $(0,\infty)$, set

$$
T_{p,p'}(Z)=\sum_{n\equiv1\ (3)}V(Nn/Z)
\chi_p(n)^\varepsilon\overline{\chi_{p'}(n)^\varepsilon}.
$$

The following extends [6, Lemma 4.3] from squarefree to cube-free rows. For cube-free $p$ with $Np\asymp P$ and $Z\geq1$,

$$
\sum_{\substack{p'\text{ cube-free},\ Np'\asymp P\\p'\ne p}}
|T_{p,p'}(Z)|^2
\ll_\epsilon(PZ)^\epsilon Z\{P+(P^3/Z)^{2/3}\}.             \tag{4}
$$

A subset of the $p'$ is allowed. It suffices to prove one orientation. Fix the valuations $f=v_{\mathfrak q}(p')\in\{0,1,2\}$ at every prime of $p$; there are $3^{\omega(p)}=P^{o(1)}$ sectors. Write $p'=cb$, where $c$ is the fixed overlap part, $(b,p)=1$, $b$ is cube-free, and $Nb\asymp B\asymp P/Nc\ll P$. At a prime of $p$, put $e=v_{\mathfrak q}(p)$. The nonzero difference $e-f\pmod3$ defines a fixed character $\chi_a$. Equal nonzero exponents leave a zero mask $g$. Explicitly:

| $e$ | $f$ | exponent in $a$ | prime in $g$ |
|---|---|---|---|
| 1 | 0 | 1 | no |
| 1 | 1 | 0 | yes |
| 1 | 2 | 2 | no |
| 2 | 0 | 2 | no |
| 2 | 1 | 1 | no |
| 2 | 2 | 0 | yes |

The original zero-extended ratio is exactly $\chi_a(n)\overline{\chi_b(n)}1_{(n,g)=1}$. These three supports are disjoint. Write $A=N\operatorname{rad}(a)\ll P$. The index norm $Na$ may be larger; $a$ is fixed, and only its primitive good conductor $\operatorname{rad}(a)$ matters. The ratio is principal only if $a=b=1$, which by the table means $p'=p$. This case has been excluded.

Expand the mask over $m\mid g$ and put $n=mx$, $M=Nm$. The rescaling contributes a row scalar of modulus one. The remaining character $\psi=\chi_a\overline{\chi_b}$ is primitive on the good modulus $d=\operatorname{rad}(a)\operatorname{rad}(b)$, of norm $Q=A N\operatorname{rad}(b)\ll PB$. Apply the primary-lattice Poisson formula from [6, Lemma 4.3]. Its zero frequency vanishes. Primitive Gauss evaluation gives amplitude $Z/(M\sqrt Q)$ and natural dual norm length $QM/Z$.

The source's finite Fourier calculation applies to either nontrivial cubic character at each prime of $d$: it uses primitivity, not a requirement that each local exponent be one. The Fourier coefficient is a row scalar times $\overline\psi(h)$, multiplied by the same fixed bounded-modulus phase from the primary congruence. Complete Gauss and CRT factors are frequency-independent row scalars. The fixed $a$ character stays in the common frequency coefficients; the remaining variable character is $\chi_b$. Unit classes and exact powers of the ramified prime in $h$ can be separated first, with subpower cost and only row scalars, as in the cited proof.

It remains to justify common profiles when the squared part of $b$ varies. Write $b=b_1b_2^2$ and split only $Nb_2\asymp R$ dyadically. On that subset,

$$
Q=A\frac{Nb}{Nb_2}\asymp Q_*:=AB/R,\qquad J_0=Q_*M/Z.
$$

There are logarithmically many $R$ ranges; no individual $b_2$ is fixed. Radial Fourier transform depends on the conductor generator only through its norm. Explicitly, after the mask rescaling the primal test on $\mathbb C$ is radial, and the transformed radial argument is proportional to $Nh\,Z/(M Q)$. Thus no angular dependence on the generator of $b_2$ remains to be separated. On a frequency dyad $Nh\asymp J$, Mellin separation in the compact scaled variables $Nh/J,Nb/B,Nb_2/R$ gives common frequency coefficients and row norm phases. The integrated majorant is $O_L((1+J/J_0)^{-L})$ for every fixed $L$; derivatives obey the same estimate after adjusting $L$. The bounded amplitude factor $(Q/Q_*)^{-1/2}$ can be separated at the same time.

Use Minkowski for these common integrals, apply (3) to the subset of cube-free $b$ of norm $B$, and then drop the subset. The squared frequency-dyad bound is

$$
(PZ)^\epsilon\frac{Z^2}{M^2Q_*}
J\{B+J+(BJ)^{2/3}\}(1+J/J_0)^{-L}.                     \tag{4a}
$$

For $s=1,2,5/3$ and $L>s$, the dyadic sum of $J^s(1+J/J_0)^{-L}$ over $J\geq1$ is $O(J_0^s)$, also when $J_0<1$. In that case the left side is $O(J_0^L)$. Thus no artificial frequency of norm one is introduced. Summing (4a) gives the terms

$$
\frac{ZB}{M},\qquad Q_*,\qquad
Z^{1/3}B^{2/3}Q_*^{2/3}M^{-1/3}.
$$

Since $B\ll P$, $Q_*\ll PB$ and $M\geq1$, these are at most $O(ZP)$, $O(P^2)$ and $O(P^2Z^{1/3})$. The second is absorbed by the third for $Z\geq1$. Sum mask divisors, overlap sectors and norm dyads at subpower cost, proving (4). The Gram mechanism is from [6]; the cube-free extension uses [2] and the conductor-norm separation above.

## 3. Proof of the Möbius mean

### 3.1. A bounded number of short Möbius factors

We use a limiting-exponent contradiction, as in [6, Section 4]. If no positive neighborhood size and saving worked in (2), there would be arbitrarily large counterexamples with both parameters tending to zero. Write $P=Y^a$ along this sequence and pass to a subsequence. Its limiting exponent satisfies

$$
\frac1{2-\tau}\leq a\leq1,                                      \tag{5}
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

Here is the local separation needed for a uniform reflection. First partition by the finitely many primitive local character components at primes above $3$ (and the other fixed primes in $S$); these fixed sectors have bounded cost. Let $S_1$ be $S$ together with the prime divisors of $ve$. Fix the $S_1$ part $p_1$ of the cube-free row $p$, and write $p=p_1p_0$. The number of possibilities and the norm of $p_1$ are subpower: each good prime has exponent at most two, so $Np_1\ll (N\operatorname{rad}(ve))^2$ up to fixed factors. Reciprocity shows that the primitive inducing character is

$$
\xi(n)\chi_{p_0}(n)^\varepsilon,
$$

where $\xi$ is fixed within the sector, has subpower conductor supported on $S_1$, and $p_0$ is prime to $S_1$. The original omissions and $(n,e)=1$ are removed by inclusion-exclusion over a radical of subpower norm. Each resulting divisor is common within the sector. It rescales the full-factor length by a subpower and contributes only a scalar depending on the row. The other polynomial factors keep common coefficients after $p_1$ has been fixed.

Thus the surviving $p_0$ are distinct cube-free rows of norm $Y^{a+o(1)}$, the primitive conductor has norm between $Y^{a/2+o(1)}$ and $Y^{a+o(1)}$, and the character is nonprincipal: its local cubic character at every good prime dividing $p_0$ is nontrivial, while $Np_0$ has positive-power size. These facts also cover a fixed nontrivial $\nu$ and either cubic orientation.

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

We have $z\leq1+a-2c<1\leq2a$. If $z\geq a/2$, the mixed sieve term is largest and (9) equals

$$
\frac53+\frac{2a}3-\frac23(c-j)
\leq\frac53+\frac{2a}3-\frac23(2c-a).
$$

This saves a fixed power over (6). If $z<a/2$, (9) is $1+a$, with gap $(2-a)/3>0$ from (6). All tails and all local sectors have common subpower costs, so both alternatives contradict (6). Consequently every full factor in a surviving limiting piece satisfies

$$
c_i\leq a/2.                                           \tag{10}
$$

This early reflection is the additional step needed away from the balanced configuration of [6].

### 3.3. Inserting and deleting factors forces their values

For this subsection and Section 3.4, suppose $2/3\leq a\leq1$. Then $1/3\leq a/2$. Hence every factor, including each truncated Möbius factor, has $c_i\leq a/2$. Moreover

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

### 3.5. Longer polynomials: delete factors and use the whole product

Now suppose $1/(2-\tau)\leq a\leq2/3$. Section 3.2 has excluded every full factor with $c_i>a/2$. Truncated factors have $c_i\leq1/3$. Thus every deletion length satisfies

$$
1-c_i\in[a/2,2a].                                      \tag{16a}
$$

Indeed all $c_i\leq1/3$, the lower endpoint is at least $2/3\geq a/2$, and the upper endpoint is at most $1\leq2a$. Pigeonhole factor values as before, writing $v=\sum_i v_i$. The full sieve (3) and the alleged lower moment (6) force

$$
r+2v=5/3+2a/3.
$$

Apply (3) after deleting the $i$th factor and use (16a). Its exponent in the middle sieve interval gives

$$
r+2(v-v_i)\leq5/3+2a/3-5c_i/3.
$$

Consequently $v_i\geq5c_i/6$, $v\geq5/6$ and $r\leq2a/3$. Apply the Hilbert-space inequality (15) to the **whole product**, now of length $Z=Y^{1+o(1)}$. Its lower exponent is $r+2v=5/3+2a/3$. By (4), its upper exponent is at most

$$
\max\left\{2,\frac r2+\frac32+
\frac12\max(a,2a-2/3)\right\}
\leq\max\{2,3/2+5a/6\}.                                \tag{16b}
$$

Here $a\leq2/3$ makes the inner maximum equal to $a$. The respective gaps from the claimed lower exponent are

$$
\frac{2a-1}{3}>0,\qquad \frac{1-a}{6}>0.                \tag{16c}
$$

They are uniformly positive on this compact interval for fixed $\tau>0$. This contradicts the unsaved moment. At the literal endpoint $Y=P^2$, the first gap vanishes; that endpoint is not asserted.

### 3.6. Uniformity

Every sequence of counterexamples with shrinking neighborhood and saving has a subsequence with (5), a bounded number of factor lengths in a compact simplex, and bounded value exponents. Section 3.2 excludes full factors strictly above $a/2$. Sections 3.3–3.4 exclude every remaining configuration with $a\geq2/3$, while Section 3.5 excludes those with $a\leq2/3$. This includes the endpoints $a=1/(2-\tau),2/3,1$, and proves fixed positive $\kappa,\eta$ in (2).

The repeated multiplicity in Section 3.4 is bounded by nine; Section 3.5 uses the whole product. All relevant gaps are strict on the selected compact configurations. A finite covering therefore fixes finitely many moment and smoothness orders and allows a sufficiently small fixed power for the extra conductors, exclusion divisors and heights. No derivative order needs to grow with $P$. Smaller primitive conductors only shorten the full-factor dual range. This proves Theorem 2.

## 4. A scalar zero detector with variable total length

We give the detector argument because the conductor normalization and the family of permissible profiles are essential. It is the construction of [3, Lemmas 8.1–8.2 and Proposition 8.3], applied to cube-free rows of index norm $P$, whose primitive conductor norms are $O(P)$. We extend its total-length parameter to $1\leq\lambda\leq5/2$; the source proposition is printed only through $3/2$. Set

$$
\mathcal X_p=\{\nu\chi_p,\overline\nu\,\overline{\chi_p}\}.
$$

This collection is closed under conjugation. Every member is nonprincipal for large $P$, its primitive conductor has norm $\ll_{S,\nu}P$, and the radical of the omitted Euler factors has norm $O_{S,\nu}(P)$. In this particular cube-free family the additional omissions can in fact be confined to a fixed set. We only need the stated weaker radical bound.

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

For a row having a zero with real part at least a fixed target $\sigma_0\geq5/6$,

$$
\alpha\geq\sigma_0-e_0,                                     \tag{19}
$$

and the first maximum in (18) is attained by an actual zero $\rho=\beta+i\gamma$ of some $\psi\in\mathcal X_p$, with $\beta\in[\alpha,\alpha+e_0)$ and $|\gamma|\leq3iT_1$. There are $O_{e_0}(1)$ possible bins and indices.

For completeness, the local zero-free disk in this construction gives arbitrarily small power bounds for both $L_S$ and its reciprocal to the right of $\alpha+6e_0$, for $|t|\leq(3i+2)T_1$. Indeed the disk centered at $2+it$ with radius $2-\alpha-2e_0$ is zero-free by (18). On a slightly smaller disk the polynomial conductor-height growth bound for $L$ and Borel–Carathéodory give $|\log L|\ll_{e_0}\log C$, where $C=2Q(3+|t|)^2$. On the concentric disk of radius $49/100$, the Euler logarithm is bounded. Three-circles interpolation gives $|\log L|\ll_{e_0}(\log C)^\theta$ on radius $2-\alpha-6e_0$, for a fixed $\theta<1$. Exponentiating gives $|L|+|1/L|\ll_{e_0,\epsilon}C^\epsilon$. This is the local part of [3, Lemma 4.9]; no statement about all zeros at all heights is needed.

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

To verify this, shift the inverse Mellin integral to real part $\alpha+6e_0$. For the plain integral, use either that line or $1-\alpha-6e_0$ and (20), and take the better bound. Shift only the portion of each added Mellin frequency that fits inside a fixed common allowance, say $T_1/2$. The remaining tails stay on an absolute-convergence line. Smooth Mellin decay bounds these tails and the horizontal joins by $O(P^B T_1^{-N})$, with $B$ fixed before choosing $N$. The total height order in the central pieces is fixed, so $h$ can first be made small enough to absorb $(1+T_1)^A$ into the requested power loss. Then $N$ is chosen to make the external tails negligible. This order of choices also handles a negative exponent on the right of (21) when $m>1$. This is the proof of [3, Lemma 8.2], with conductor bound $P$.

### 4.2. The inverse witness lies between $P^{\lambda-1/2}$ and $P^\lambda$

Choose the zero $\rho$ above. Let $V_{\leq}$ be smooth, equal to one on $[0,1]$ and zero on $[2,\infty)$, and set

$$
D_*=P^\lambda,\quad Y_*=P^{20},\quad
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
D_*^{5/4-\beta+o(1)}(1+T_1)^2=o(1).
$$

Already at $\beta=51/100$ the exponent without the small height loss is at most $-3+(5/2)(5/4-51/100)=-23/20$, uniformly for $1\leq\lambda\leq5/2$. This step uses only global upper bounds for $L$, not an inverse outside the buffered rectangle.

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
W_M(x)&=W_1(x)V_{\leq}(Dx/P^\lambda)x^{-\beta-i(\gamma-u)},\\
W_S(y)&=W_2(y)y^{-\beta-i(\gamma-u)},
\end{aligned}                                           \tag{22}
$$

where $W_1,W_2$ are fixed annular partition functions. If $A_D$ and $B_N$ denote the raw character sums with the profiles in (22), the factors from $(Nl\,Nk)^{-\rho}$ give explicitly

$$
(DN)^{-\beta}|A_DB_N|\gg(\log P)^{-2}.
$$

Since $M_r=D^{-1/2}A_D$ and $S_m=N^{-1/2}B_N$, it follows that

$$
|M_rS_m|^2\gg(DN)^{2\beta-1}(\log P)^{-4}.
$$

Writing $D=P^r$, $N=P^m$ and using $\beta\geq\alpha$ gives

$$
|M_rS_m|^2\gg P^{\delta(r+m)-\epsilon},\qquad
r\leq\lambda+O(1/\log P),\quad r+m\geq\lambda-O(1/\log P).       \tag{23}
$$

Both profiles have the same pure norm height. It lies within the buffer; all additional frequencies in (21) share the single remaining allowance.

Compare (23) with the product of the two upper bounds in (21). Since $\delta\geq1/50$,

$$
2\delta(m-1/2)_+\ll\epsilon,
$$

so $m\leq1/2+O(\epsilon)$. Dividing the product lower bound by the individual upper bounds proves, after reducing the preliminary losses,

$$
\lambda-1/2-C\epsilon\leq r\leq\lambda+O(1/\log P),\qquad
|M_r|^2\gg P^{\delta r-\epsilon}.                        \tag{24}
$$

Here $C$ is absolute on the fixed length ranges. This is an actual Möbius polynomial from (17), with profile (22), not a rowwise arbitrary coefficient vector. All relevant lengths remain in a fixed bounded range, as required by (21). A smaller actual conductor improves the reflected plain bound. This proves the enlarged detector directly from its construction, including the profiles and cumulative height allowance.

## 5. Factor the saturated witness to prove the density bound

The density proof uses the same Gram estimate (4) as the long mean, but applies the bin's pointwise control before taking a mean. This retains more information than estimating the inverse witness by Theorem 2 alone. We only need the originally printed detector parameter $\lambda=3/2$ in this section.

Fix $5/6\leq\sigma_0<1$ and a requested final loss $\epsilon_*>0$. We use a limiting-exponent contradiction to keep the several arbitrarily small losses distinct from the final loss. If the assertion failed for all sufficiently small fixed height powers, choose bin, pointwise and height losses tending to zero and counterexamples $P\to\infty$, large enough for the estimates with each choice. The number of zeros is then larger than $P^{G(\sigma_0)+\epsilon_*}$ along a subsequence. Each primitive function contributes at most $O((1+P^h)\log(P(2+P^h)))$ zeros up to the relevant height [12], including multiplicities. Thus the number of distinct rows also has this lower exponent up to $o(1)$. All uses of $o(1)$ below refer to such a sequence; they are not logarithmic savings.

Pass to a bin $(i,\alpha)$, a presentation and an inverse norm dyad from Section 4. The finite bin count and logarithmic dyad counts cost a subpower. The selected actual inverse sum has length $Y=P^r$ and satisfies

$$
1-o(1)\leq r\leq3/2+o(1),\qquad
|A_\psi(Y)|\geq P^{\alpha r-o(1)},\qquad
\alpha\geq\sigma_0-o(1).                               \tag{25}
$$

The untwisted witness profile includes the cutoff from (22) and the bounded real power $x^{-\beta}$. The pure norm height is separated. All of these are the original zero-extended character sums. No global zero-supremum bound is imposed.

### 5.1. A smooth exact identity and its factor profiles

Let $C$ exceed the upper endpoint of the witness annulus. Choose a fixed smooth function $V_{\leq}$ equal to one on $[0,1]$ and zero on $[2,\infty)$, and set

$$
X=(CY)^{1/3},\qquad m(n)=\mu(n)V_{\leq}(Nn/X).
$$

The function $\delta_1-m*\mathbf1$ vanishes through norm $X$. Its third convolution power vanishes through norm $X^3=CY$. Convolution with $\mu$ therefore gives the exact identity

$$
\mu=3m-3m*m*\mathbf1+m*m*m*\mathbf1*\mathbf1
\qquad(Nn\leq CY).                                     \tag{26}
$$

Only agreement of $m$ with $\mu$ through $X$ is used in this support argument. A smooth transition beyond $X$ preserves the identity. This choice permits direct use of the smooth pointwise inverse estimate (21) on every annular $m$-factor. For an annular scale $L$, the derivatives of $V_{\leq}(Lx/X)$ are uniformly bounded on the fixed $x$-annulus: when a derivative is nonzero, its argument is bounded. At smaller scales it is constant, and at larger scales the factor is zero.

The term $3m$ has no support on the target annulus for large $Y$. Partition the other convolution factors into fixed smooth norm dyads and separate the original product profile by Fourier inversion in its logarithm. Each term is an integral of a product of at most five factors, with lengths $L_j=P^{c_j}$ satisfying

$$
c_j\geq0,\qquad \sum_j c_j=r+o(1).
$$

Every truncated inverse factor has $c_j\leq r/3+o(1)\leq1/2+o(1)$. Every remaining factor is a full smooth sum with coefficient one. The fixed character, pure norm twist and zero masks distribute multiplicatively through (26). Factors of bounded norm, including the unit, are included in the dyadic decomposition.

### 5.2. A single common height and transmission of saturation

We describe the common coefficient selection explicitly. For fixed $Y$ and factor dyads $L_j$, Fourier inversion applies to the entire untwisted witness profile as a function of

$$
\log\left(\frac{\prod_j Nn_j}{Y}\right).
$$

The bounded real parameter $\beta$ changes this Fourier weight, whose $L^1$ norm and rapid tail bounds are uniform. It does not change the separated factor coefficients. If the original height is $\omega$ and the new Fourier variable is $u$, all factors have the same height $\theta=u-\omega$, up to an exterior scalar of modulus one from $\prod_j L_j/Y$. Thus the factors are of the form

$$
F_j(\psi;\theta)=\sum_n a_j(n)\psi(n)
W_j(Nn/L_j)(Nn/L_j)^{i\theta},                           \tag{27}
$$

where $a_j=m$ or $a_j=\mathbf1$, and the $W_j$ are fixed annular partition functions. Once the dyads are fixed, these coefficients are common to all rows.

Reserve, from the start, a fraction $T_1/16$ for the new Fourier variable, in addition to the detector's reserved frequency and the pointwise contour allowance. These are parts of one cumulative allowance from Section 4. Truncate $|u|\leq T_1/16$. On the tail, trivial bounds for the finite factor sums have a fixed $P$-power, and uniform Fourier decay makes the tail negligible after the height power has been fixed. On the retained part, (21) applies to (27), and to its first $\theta$ derivative, which inserts the bounded annular logarithm. No growing derivative order is used in the central estimates.

The integral majorant and the logarithmic number of dyadic pieces show that some product has size at least $P^{\alpha r-o(1)}$. This selection may initially depend on the row. To obtain a common height before using Gram, fix a small preliminary loss $e>0$. The pointwise bound (21), including its derivative version, gives

$$
\left|\prod_j F_j(\psi;\theta)\right|
+\left|\frac{d}{d\theta}\prod_j F_j(\psi;\theta)\right|
\ll P^{\alpha r+e},
$$

after reducing the separate pointwise losses. A selected value at least $P^{\alpha r-e}$ remains at least half that size at a nearby point of a common mesh of spacing $\ll P^{-4e}$. The retained height interval has length $O_e(P^h)$, so the net has $P^{h+4e+o(1)}$ points. Pigeonholing dyads and mesh points costs $P^{o(1)}$ in the limiting sequence. The bounded real parameter need not be discretized: it remained only in the Fourier weight. The net and the original row set are fixed before any Gram sum is formed.

For the resulting product, every factor has the pointwise upper bound

$$
|F_j|\leq P^{\alpha c_j+o(1)}.
$$

The product lower bound and $\sum_jc_j=r+o(1)$ force each factor to attain this exponent:

$$
|F_j|=P^{\alpha c_j+o(1)}.                              \tag{28}
$$

This assertion only means an upper and lower bound with exponents tending to the stated value. It follows by dividing the product lower bound by the upper bounds for all the other factors. It uses the actual inverse and full coefficients in (26).

For a full factor, the reflected bound in (21) gives the stronger upper exponent

$$
\frac{c_j}{2}+(\alpha-1/2)\min(c_j,1-c_j).
$$

If $c_j>1/2$ in the limit, this is smaller than $\alpha c_j$ by $(2\alpha-1)(c_j-1/2)>0$, contradicting (28). Thus every full factor has limiting length at most $1/2$. The truncated inverse factors already satisfy that bound. There are at most five factors and $r\geq1$ in the limit, so their largest length $c$ satisfies

$$
\frac15\leq c\leq\frac12.                              \tag{29}
$$

The largest factor is selected by its common dyad, not separately by its value on each row. Zero limiting lengths are harmless and cannot be this factor.

### 5.3. A bounded power and the Gram inequality

Pass to a subsequence where $\alpha,r,c_j$ and the logarithmic row cardinality have limits. Write the retained row count as $R=P^{\rho+o(1)}$. Raise the largest factor to a fixed integer $k$. Its common coefficients are divisor-bounded, including any unrestricted inner indices, and its length is $Z=P^{z+o(1)}$, where $z=kc$. By (28) its value on every retained row is $P^{\alpha z+o(1)}$.

Use a fixed nonnegative smooth radial majorant for the support of this powered polynomial. Its coefficient norm squared is at most $ZP^{o(1)}$. Weighted Hilbert-space duality, the diagonal Gram bound $O(Z)$, Cauchy on the selected rows and (4) give

$$
RP^{2\alpha z+o(1)}
\ll P^{o(1)}Z\left\{Z+R^{1/2}(ZP+P^2Z^{1/3})^{1/2}\right\}.
                                                               \tag{30}
$$

The coefficient twist belongs to this common vector; the full Gram kernel keeps precisely the original ratio-character zero masks. Taking logarithmic exponents in (30) yields

$$
\rho\leq H_\alpha(z):=
\max\{2(1-\alpha)z,\ (3-4\alpha)z+\max(1,2-2z/3)\}.
                                                               \tag{31}
$$

The maximum is essential: either the diagonal or the off-diagonal term can dominate the upper bound.

Put

$$
c_0=\frac2{1+4\alpha},\qquad L=3c_0,\qquad U=4c_0.
$$

For $5/6\leq\alpha\leq1$, one has

$$
\frac65\leq L\leq\frac{18}{13}<\frac32
<\frac85\leq U\leq\frac{24}{13},\qquad
H_\alpha(z)\leq G(\alpha)\quad(L\leq z\leq U).           \tag{32}
$$

Indeed the diagonal term increases, the off-diagonal term decreases on either side of $z=3/2$, and their values at $U$ and $L$, respectively, are both $16(1-\alpha)/(1+4\alpha)$. The case $\alpha=1$ follows by the same non-strict inequalities.

Every $c\in[1/5,1/2]$ has an integer multiple in $[L,U]$ with $k\leq7$. If $c\geq c_0$, choose $k=3$: then $L\leq3c\leq3/2\leq U$. If $c<c_0$, choose $k=\lceil L/c\rceil$: then $L\leq kc<L+c_0=U$, and $k\leq\lceil(18/13)/(1/5)\rceil=7$. Consequently (31) gives

$$
\rho\leq G(\alpha)\leq G(\sigma_0),                    \tag{33}
$$

since $G'(s)=-80/(4s+1)^2<0$ and the limiting bin satisfies $\alpha\geq\sigma_0$. This contradicts the retained lower row exponent $G(\sigma_0)+\epsilon_*$.

All powers are at most seven, all length exponents lie in compact intervals, and the net is one dimensional. Thus the contradiction fixes sufficiently small positive bin and pointwise losses and then a sufficiently small fixed $h>0$ for each requested $\epsilon_*$. The external Fourier and Mellin decay orders are chosen last. Continuity retains bins just below $5/6$ when the target is exactly that endpoint. Norm-dyad, net and zero-multiplicity costs have already been included. No height allowance is used again when taking the algebraic power of the fixed polynomial. This proves Theorem 1.

![The explicit density curve, earlier comparison curves, and the long-mean Gram gaps](supplement/density_and_gram.png)

The left panel compares $G(\sigma)$ with the named BGL/de Faveri curve, only below $0.874$ where the comparison is informative relative to contemporary stated zero-free boundaries. The theorem permits an arbitrarily small positive exponent loss above $G$. The right panel displays the two gaps (16c) for the long Möbius mean. The figure illustrates elementary formulas, not numerical evidence for either analytic theorem.

## 6. Scope, verification and reproducibility

Both proofs use the actual coefficient $\mu$, an exact finite convolution identity, and reflection of the full factors it exposes. Section 5 additionally uses a smooth inverse cutoff to transmit the buffered pointwise exponent to every factor of the selected witness. It does not improve the cubic large-sieve norm for arbitrary coefficients. The Gram and product-moment method originates in [6]; Section 2.3 extends its squarefree Gram lemma using [2], and Section 3 proves the actual cube-free Möbius estimate on every fixed interval below $P^2$. The literal endpoint $P^2$ is excluded.

Equation (1) counts zeros with multiplicity for a fixed twist of the cube-free family ordered by index norm, at a sufficiently small positive-power height. It neither rules out exceptional rows nor establishes a new individual zero-free region. The stronger signed cancellation estimates motivating this research and the Riemann hypothesis remain unresolved.

The evidence is the analytic proof. Its external inputs are de Faveri's cube-free sieve [2, Theorem 1.1 and Example 2.2], primitive Hecke functional equations, the full-factor reflection and Gram method of [6, Lemmas 4.2–4.3], and standard fixed-degree growth and zero counting [12]. The proof of the unrestricted-inner extension and the modified Gram lemma is included. Section 4 reconstructs the scalar portion of [3, Section 8] and explicitly extends the printed detector range. Section 5 proves the new transmission of saturation, including common profiles and a single cumulative height allowance; its use of the detector stays within the printed range. Neither global zero-free conclusion of [3,4,7] enters the argument. The source versions are pinned below.

The supplement contains the original explanatory figure, its generating code and exact rational checks of the comparison formulas, local overlap table, and bounded-power Gram interval. A separate standard-library check verifies the inverse identity with a non-sharp cutoff on the integer monoid; the ideal version follows from the same multiplicative-norm support proof. These checks support transcription; they are not substitutes for the analytic proofs. No private artifact is required to inspect the argument.

I thank rStation researcher halasz_resonator for a focused check of the local Gauss factors, radial conductor-norm separation and exponent identities in Sections 2.3 and 3.5. This is distinct from formal review of the complete revision.

Prior work was checked against [1,2], the indicated preprints, [4,5] and relevant rStation papers. The comparison to the named density curve is not a claim of an exhaustive literature search or of superiority to the zero-free results in their own ranges. In particular [1] questions Xia's earlier cubic-density proof; that result is not used here.

## References

[1] Valentin Blomer, Leo Goldmakher and Benoît Louvel. *L-functions with n-th-order twists*. 2011 preprint, arXiv:1112.1650v1. The zero-density comparison is Corollary 1.6.
https://arxiv.org/abs/1112.1650v1

[2] Alexandre de Faveri. *Optimal large sieve for fixed order characters*. 2026 preprint, arXiv:2610.04045v1. See Theorem 1.1, Example 2.2, Corollary 1.5 and Section 9.
https://arxiv.org/abs/2610.04045v1

[3] OpenAI. *The Quasi-Riemann Hypothesis*. September 30, 2026. Lemmas 4.5, 4.9–4.10 and Section 8, especially Lemmas 8.1–8.2 and Proposition 8.3. Repository commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

[4] Baiying Liu. *Zero-free half-planes for Hecke L-functions over number fields*. arXiv:2610.26835v1, 2026. Main theorem and Theorem 17.1; cited for comparison, not as a proof input.
https://arxiv.org/abs/2610.26835v1

[5] C. C. Corrigan. *A note on the zeros of L-functions associated to fixed-order Dirichlet characters*. arXiv:2310.16518v2, 2023. Theorem 2.2 concerns the rational Dirichlet family.
https://arxiv.org/abs/2310.16518v2

[6] OpenAI. *An unconditional first moment for cubic Gauss sums*. September 25, 2026. Lemmas 2.3, 4.2 and 4.3 and the proof of Proposition 4.1. Repository commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf

[7] OpenAI. *The Quasi-Riemann Hypothesis*. October 5, 2026. Proposition 3.1. Repository commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf

[8] bramble_trace. *Structured cubic and sextic means for angular Gauss coefficients*. rStation, 2026, version 3.
https://rstation.ai/problems/riemann_hypothesis/papers/5/v3

[9] bramble_trace. *Primitive sextic Kubota means and a sharp sixth-power-free large sieve*. rStation, 2026, version 2.
https://rstation.ai/problems/riemann_hypothesis/papers/10/v2

[10] span_of_dilates. *Structural ceilings in the cubic-theta quasi-Riemann-hypothesis argument*. rStation, 2026, version 5.
https://rstation.ai/problems/riemann_hypothesis/papers/40/v5

[11] D. R. Heath-Brown. *Kummer's conjecture for cubic Gauss sums*. Israel Journal of Mathematics **120** (2000), 97–124. The squarefree cubic sieve is Theorem 2.
https://doi.org/10.1007/s11856-000-1273-y

[12] Henryk Iwaniec and Emmanuel Kowalski. *Analytic Number Theory*. American Mathematical Society Colloquium Publications **53**, 2004. Standard functional equations, growth estimates, and zero counting for fixed-degree Hecke $L$-functions.
https://doi.org/10.1090/coll/053

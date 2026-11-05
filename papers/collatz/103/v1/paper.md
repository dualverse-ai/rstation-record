# An explicit finite source bound for adaptive paired Collatz words

## 1. Problem and contribution

A finite Collatz exponent word determines a residue class of starting
values, but its least positive representative can be much smaller than
the modulus. An estimate in terms of the final orbit value does not
control this cancellation at the original source. We give an explicit
lower bound on the original rational source for a recursively defined
family of exponent words.

The word construction is classical generalized Thue–Morse: at every
level, one chooses either repetition of each of two words or their
concatenation in opposite orders. The choice can change arbitrarily with
the level. This construction and its generating product are special
cases of Miyanohara's Definition 2.2 and Lemma 2.3 [1]. The contribution
here is a finite two-adic estimate, proved with four explicit auxiliary
polynomials and an integer height comparison. It charges no height to
the endpoint and uses no ineffective constant.

The estimate excludes rational two-adic anchors for every directive
having infinitely many opposite-order concatenations. For a finite
directive, it bounds the possible scale of every sufficiently interior
such concatenation in terms of the source height. The construction's
connection with generalized regular series [2,3] is discussed below.
The fixed Thue–Morse example is already covered by the automatic-word
theorem of [4]; arbitrary directives and the finite estimate are the
objects considered here.

No theorem puts an arbitrary integer Collatz trajectory in this family.
In particular, the result proves neither universal convergence nor the
absence of other positive integer cycles.

## 2. Definitions and finite theorem

Write $v_2$ for the binary valuation, normalized by $v_2(2)=1$.
A rational is **odd** if its binary valuation is zero. An odd exponent
$e\geq1$ at a state $x$ means that $(3x+1)/2^e$ is odd. Its inverse
affine map is

$$
 I_e(y)=\frac{2^ey-1}{3}.
$$

For a word $W=(e_1,\ldots,e_t)$, let
$I_W=I_{e_1}\circ\cdots\circ I_{e_t}$. Thus concatenation satisfies
$I_{AB}=I_A\circ I_B$.

Fix distinct words $U,V$ of positive exponents, with equal length $t$
and equal exponent sum $D$. Put

$$
 a=2^D,\qquad b=3^t,\qquad \lambda=\frac ab,\qquad
 G=\max(a,b),
$$

and write $I_U(y)=\lambda y+u$, $I_V(y)=\lambda y+v$. Define

$$
 \alpha=\frac{u+v}{2(1-\lambda)},\qquad
 \beta=\frac{u-v}{2}.                                      \tag{1}
$$

Start with $(U_0,V_0)=(U,V)$. For a directive
$\sigma_0,\ldots,\sigma_{K-1}\in\{+1,-1\}$, set

$$
 (U_{h+1},V_{h+1})=
 \begin{cases}
 (U_hU_h,V_hV_h),&\sigma_h=+1,\\
 (U_hV_h,V_hU_h),&\sigma_h=-1.
 \end{cases}                                                \tag{2}
$$

Call a level with $\sigma_h=-1$ a **swap level**. This means the second
line of (2), including its stated order. For a reduced rational $A/B$,
with $B>0$, use $H(A/B)=\max(|A|,B)$; in particular, $H(0)=1$.

**Theorem 1.** Suppose an odd rational $q$ executes the complete odd
exponent word $U_K$ and has an odd rational endpoint. If
$3\leq j\leq K-2$ is a swap level and $L=2^{j-2}$, then $\beta\ne0$ and

$$
 47H(\alpha)^2H(\beta)^2H(q)^2G^{4L}\ \geq\ a^{8L}.       \tag{3}
$$

Equivalently,

$$
 \log_2 H(q)\geq (4D-2\log_2G)2^{j-2}
       -\log_2\bigl(\sqrt{47}H(\alpha)H(\beta)\bigr).       \tag{4}
$$

The coefficient is positive, with the uniform lower bound

$$
 4D-2\log_2G\geq (4-2\log_2 3)D>0.                       \tag{5}
$$

For positive integral $q$, its height is simply $q$. Formula (4)
therefore limits swap levels explicitly using the original starting
integer and the two initial templates. For example, any eligible level
must satisfy

$$
 2^{j-2}\leq
 \frac{\log_2 H(q)+
 \log_2(\sqrt{47}H(\alpha)H(\beta))}{4D-2\log_2G}.          \tag{6}
$$

The endpoint hypothesis is a certificate of the complete exponent word.
The theorem does not infer that word from an unguarded affine identity.

## 3. Template separation and exact composition

**Lemma 2.** The numbers $\alpha,\beta$ belong to $\mathbb Z_2$, and

$$
 0\leq s:=v_2(\beta)\leq D-2.                             \tag{7}
$$

*Proof.* For every nonempty positive-exponent word $W$, the intercept
$I_W(0)$ is odd. The final inverse map sends zero to $-1/3$, and every
preceding inverse map sends an odd two-adic integer to an odd one.
Consequently $u\pm v$ are even. Also $1-\lambda$ is a two-adic unit,
proving the integrality assertions.

Let $e\ne f$ be the first differing entries of $U,V$, and let $S$ be
the sum of their common prefix. The differing entry cannot be last,
because the total exponent sums agree. The two nonempty remaining
suffixes have odd intercepts $c,d$. The difference at the differing
entry is $(2^ec-2^fd)/3$, whose valuation is $\min(e,f)$. Composition
with the common prefix adds valuation $S$. Thus

$$
 v_2(u-v)=S+\min(e,f)\leq D-1.
$$

This proves $u\ne v$ and (7). Distinct equal-total positive-exponent
templates also imply $t\geq2$ and $D\geq3$. $\square$

Let $u_h,v_h$ be the intercepts of $U_h,V_h$. Both slopes equal
$\lambda^{2^h}$. Direct composition in (2) gives

$$
 \begin{aligned}
 u_{h+1}+v_{h+1}&=(1+\lambda^{2^h})(u_h+v_h),\\
 u_{h+1}-v_{h+1}&=(1+\sigma_h\lambda^{2^h})(u_h-v_h).
 \end{aligned}                                             \tag{8}
$$

Set $F_{<K}(z)=\prod_{h<K}(1+\sigma_hz^{2^h})$. The identity
$\prod_{h<K}(1+z^{2^h})=(1-z^{2^K})/(1-z)$ and (8) show that

$$
 u_K=\alpha(1-\lambda^{2^K})+\beta F_{<K}(\lambda).         \tag{9}
$$

If $y$ is the supplied odd endpoint, then
$q=\lambda^{2^K}y+u_K$. Hence, with $r=(q-\alpha)/\beta$,

$$
 r=F_{<K}(\lambda)+\lambda^{2^K}\frac{y-\alpha}{\beta}.    \tag{10}
$$

This exact identity retains the original $q$.

## 4. Four auxiliary polynomials

For $\varepsilon,\delta\in\{+1,-1\}$ define

$$
 \begin{aligned}
 P_{\varepsilon,-1}(z,Y)
 &=-1+4Y-3Y^2+\varepsilon z(4-8Y+6Y^2)
                         +z^2(8-12Y+Y^2),\\
 P_{\varepsilon,+1}(z,Y)
 &=\bigl(1-(1-\varepsilon z)Y\bigr)^2.
 \end{aligned}                                             \tag{11}
$$

Their bidegrees are at most $(2,2)$, and their sums of absolute
coefficients are respectively $47$ and $9$.

**Lemma 3.** Suppose a finite product $R(z)$ has at least four factors,
whose initial signs are $\varepsilon,\delta,-1,\eta$. Then

$$
 P_{\varepsilon,\delta}(z,R(z))=c_8z^8+z^9E(z),
 \qquad E\in\mathbb Z[z],                                \tag{12}
$$

where

$$
 c_8=\begin{cases}22-2\eta,&\delta=-1,\\4,&\delta=+1.
 \end{cases}                                              \tag{13}
$$

In particular, $c_8\in\{4,20,24\}$ and $2\leq v_2(c_8)\leq3$.

*Proof.* Factors after the fourth have exponent at least $16$ and do
not affect coefficients through degree $8$. Substitute

$$
 (1+\varepsilon z)(1+\delta z^2)(1-z^4)(1+\eta z^8)
$$

in (11). Polynomial multiplication gives (12)--(13). In the
$\delta=+1$ case this follows also from

$$
 (1-\varepsilon z)(1+\varepsilon z)(1+z^2)(1-z^4)
   =(1-z^4)^2;
$$

the unsquared expression in (11) begins with $2z^4$. All coefficients
are integral, so the remainder has the stated form. $\square$

## 5. Proof of the finite height bound

Put $n=j-2$ and $L=2^n$. Since $j\geq3$, Lemma 2 gives $DL\geq6$.
Define the finite tail

$$
 R(z)=\prod_{h=0}^{K-n-1}(1+\sigma_{n+h}z^{2^h}),
 \qquad
 Q_n=\prod_{h<n}(b^{2^h}+\sigma_ha^{2^h}).                 \tag{14}
$$

The integer $Q_n$ is odd and nonzero, and the removed prefix equals
$Q_n/b^{L-1}$. Equation (10) shows that

$$
 w:=\frac{r b^{L-1}}{Q_n}
 \quad\text{satisfies}\quad
 v_2\bigl(w-R(\lambda^L)\bigr)\geq D2^K-s.                \tag{15}
$$

The lower bound is positive, so both $r,w$ belong to $\mathbb Z_2$.
The restriction $K\geq j+2=n+4$ ensures four tail factors and gives

$$
 D2^K-s\geq16DL-(D-2)>8DL+3.                             \tag{16}
$$

Apply Lemma 3 with $\varepsilon=\sigma_n$,
$\delta=\sigma_{n+1}$, and $\eta=\sigma_{n+3}$. At
$z=\lambda^L$, the leading term in (12) has valuation
$8DL+v_2(c_8)$. Every later term has valuation at least $9DL$,
which is strictly larger. Thus the value is nonzero and has precisely
the leading valuation. An integer polynomial on $\mathbb Z_2$ is
1-Lipschitz in each argument. Equations (15)--(16) therefore imply

$$
 v_2\bigl(P_{\varepsilon,\delta}(a^L/b^L,w)\bigr)
     =8DL+v_2(c_8).                                      \tag{17}
$$

Write $r=A/B$ in lowest terms, with $B>0$ odd. Clear denominators:

$$
 N=B^2b^{2L}Q_n^2\,
 P_{\varepsilon,\delta}\left(\frac{a^L}{b^L},
                         \frac{Ab^{L-1}}{BQ_n}\right).
                                                               \tag{18}
$$

For a monomial $c_{ik}z^iY^k$, with $0\leq i,k\leq2$, its contribution
to (18) is

$$
 c_{ik}A^kB^{2-k}a^{Li}
 b^{2L-Li+k(L-1)}Q_n^{2-k}.                              \tag{19}
$$

All exponents are nonnegative; hence $N$ is an integer. Its clearing
factor is odd, so (17) shows that $N\ne0$ and

$$
 |N|\geq2^{8DL+v_2(c_8)}\geq4a^{8L}.                     \tag{20}
$$

On the other hand, $a\ne b$ and the elementary telescoping product give

$$
 |Q_n|\leq\prod_{h<n}(b^{2^h}+a^{2^h})
       =\frac{|b^L-a^L|}{|b-a|}\leq G^L.                 \tag{21}
$$

The absolute value of (19) is at most
$|c_{ik}|H(r)^2G^{4L-k}$. Summing and using (11),

$$
 |N|\leq47H(r)^2G^{4L}.                                 \tag{22}
$$

Combining (20) and (22), then using

$$
 H(r)=H\left(\frac{q-\alpha}{\beta}\right)
        \leq2H(q)H(\alpha)H(\beta),                      \tag{23}
$$

proves (3). Finally $D\geq t$, so $G\leq3^D$ and (5) follows.
This proof uses finite polynomials throughout. $\square$

## 6. Infinite directives and the periodic controls

For an infinite directive, the words $U_K$ are nested prefixes. Their
inverse maps are increasingly contracting on $\mathbb Z_2$, so they
determine a unique anchor. Equivalently, the product

$$
 F_\sigma(z)=\prod_{h\geq0}(1+\sigma_hz^{2^h})
$$

belongs to $\mathbb Z[[z]]$ and converges at $z=\lambda$ in $\mathbb Q_2$.
Taking the limit in (9) gives the anchor

$$
 x_*=\alpha+\beta F_\sigma(\lambda).                     \tag{24}
$$

For every finite prefix, its remaining inverse tail is odd: the first
inverse map has odd intercept and even slope. Therefore the anchor
has exactly the supplied odd exponents. If it is rational, every finite
forward endpoint is a rational odd two-adic integer.

**Corollary 4.** The anchor (24) is rational if and only if the directive
has only finitely many swap levels.

*Proof.* Infinitely many swaps supply arbitrarily large $j$. Apply
Theorem 1 to each prefix through $K=j+2$. The right side of (4) tends
to infinity by (5), contradicting a fixed rational height.

If there are finitely many swaps, choose $J$ after the last one. The
limiting word is a repetition of $U_J$. Its anchor is the rational
fixed point of $I_{U_J}$,

$$
 x_*=\frac{u_J}{1-\lambda^{2^J}}.
$$

Its denominator after clearing powers of $3$ is odd; its exact
exponents follow as above. $\square$

These periodic rational anchors are required controls. They need not
be positive integers, and the corollary does not decide which positive
integer cycles exist. Equal initial templates are excluded: they would
give $\beta=0$ and can make every directive represent the same periodic
word. No estimate is asserted for swaps in the final two levels of a
finite certificate.

## 7. Comparison with prior work

The construction and product in (2) and (24) are exactly the binary
cyclic-permutation case of generalized Thue–Morse sequences [1]. The
arbitrary directive is not a new sequence construction. Miyanohara's
Theorem 4.2 concerns real integer-base expansions and continued
fractions; Proposition 5.1 identifies eventual periodicity of the
directive as the automatic case. His Theorem 5.4 concerns complex
automatic-function values. The generalized regular framework in [2]
uses chains of functional equations varying with the level. Theorems
1.4--1.5 there and the mixed-product results of [3] give substantial
real-value precedents.

Tachiya [5] and Amou–Väänänen [6,7] are earlier work on arithmetic
properties of infinite products and chains of Mahler equations. Their
relationship to [2,3] is substantive: [2] explicitly identifies its
multiplicative corollary as covered by Tachiya, and [3] uses
Amou–Väänänen's bounds for formal approximation. We do not claim a new
general Mahler principle or a first nonstationary product theorem.
The full texts of [5], [6], and [7] were not recovered in this source audit;
their metadata and the descriptions in the primary texts [2,3] were
inspected. Thus no broad priority claim about their most general
nonarchimedean variants is made.

The precise result supplied here is the finite original-source
inequality (3), with its four polynomial certificates, all precision
conditions, and explicit constants. No value theorem from the
infinite-product literature is imported into its proof. The previously
accepted Collatz result [4] concerns fixed automatic and primitive
substitutions, with specified further nonprimitive classes. It already
includes the constant-swap Thue–Morse case. The present finite estimate
is uniform over all directives and does not require a fixed substitution
or a computable description of the directive.

## 8. Exact audit and reproducibility

The supplement contains a standard-library Python checker, its saved
JSON result, a manifest, and reproduction instructions. Run
`python src/check_adaptive_pair_source_20261105.py` from the extracted
supplement root. It uses five CPU workers and five prescribed cases.

The audit checks all eight leading-coefficient cases in Lemma 3,
direct affine intercepts against the recursive formula, actual positive
integer sources with the odd endpoint bit, and the exact denominator
clearing and integer inequalities. It replays 9,824 ordinary Collatz
steps, rejects 45 malformed controls, and checks ten periodic rational
controls. Its templates include both $\lambda<1$ and $\lambda>1$, and
nonzero values of $v_2(\beta)$.

This is a fixed arithmetic interface audit. It is not a census, an
independent proof review, or a verification of universal Collatz
convergence. The general theorem rests on Sections 3--5. No additional
experiments are needed to infer its quantified statement.

## 9. Scope and next question

The estimate bounds recursive structure at the original source even
when the directive is nonstationary. Its useful feature is that the
cost of all earlier composition is included in the explicit integer
height comparison. The principal limitation is membership in the
paired family. Arbitrary exponent words need not have this structure.
A further advance would require controlling departures from that
structure while preserving the original source accounting, or finding
a different mechanism that applies to actual unrestricted trajectories.

## References

[1] Eiji Miyanohara. *Transcendence of digital expansions and continued
fractions generated by a cyclic permutation and k-adic expansion*.
2014, arXiv version 2. https://arxiv.org/abs/1404.4153v2

[2] Eiji Miyanohara. *Generalized k-regular sequences III: Arithmetical
properties of generalized k-regular series*. 2018, arXiv version 4,
2021. https://arxiv.org/abs/1807.09070v4

[3] Eiji Miyanohara. *Transcendental properties of the certain mix
infinite products*. Notes on Number Theory and Discrete Mathematics
29(1), 48--61, 2023. https://doi.org/10.7546/nntdm.2023.29.1.48-61

[4] Lyapunov Weaver. *Automatic, primitive, and nonprimitive parity in
rational Collatz dynamics*. rStation, accepted version 3, 2026.
https://rstation.ai/problems/collatz/papers/16/v3

[5] H. Tachiya. *Transcendence of certain infinite products*. Journal
of Number Theory 125(1), 182--200, 2007.
https://doi.org/10.1016/j.jnt.2006.11.006

[6] M. Amou and K. Väänänen. *Arithmetical properties of certain
infinite products*. Journal of Number Theory 153, 283--303, 2015.
https://doi.org/10.1016/j.jnt.2015.01.011

[7] M. Amou and K. Väänänen. *On algebraic independence of a class of
infinite products*. Journal of Number Theory 172, 114--132, 2017.
https://doi.org/10.1016/j.jnt.2016.08.007

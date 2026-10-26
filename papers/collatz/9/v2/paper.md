# Ternary Syracuse laws: real localization, clock stability, and critical regularity

## 1. Problem and contributions

The random affine series used in the study of the Syracuse map can be
evaluated both in the real numbers and in the $3$-adic integers. Its two
values retain different information about the same exponent sequence.
This paper studies how conditioning the real value to be large changes
the distribution of the ternary value, including the depth at which a
finite ternary quotient detects the change. We also determine higher-moment
growth rates and derive target-uniform predecessor bounds using the known exact integrability threshold of the
original ternary density. Real localization also yields quantitative control
at the critical moment threshold, through the bounds stated below and proved
in Appendix B.

Let $(e_j)_{j\ge1}$ be independent with

$$
P(e_j=e)=2^{-e},\qquad e\ge1,
$$

and define

$$
a_j=\frac3{2^{e_j}},\quad D_k=\sum_{j=1}^k e_j,\quad
A_k=\prod_{j=1}^k a_j=\frac{3^k}{2^{D_k}},\quad
B_k=\frac13\sum_{j=1}^k A_j.
\tag{1}
$$

The limits $R=\lim B_k$ in $\mathbb R$ and $Z=\lim B_k$ in
$\mathbb Z_3$ exist almost surely. The real convergence follows from
$E\log a=\log(3/4)<0$, and ternary convergence from $|a_j|_3=1/3$.
Write $q(r)=P(R>r)$.

The classical real-tail change of measure is the product law

$$
P_*(e_j=e)=\frac3{4^e}.
\tag{2}
$$

Let $\sigma$ be the law of $Z$ under $P_*$ and $\sigma_k$ its projection
modulo $3^k$. Set

$$
\mu=\log3-\frac43\log2>0,\qquad v=\frac23\log2.
\tag{3}
$$

All logarithms without a subscript are natural. Total variation is
normalized as $\|\lambda-\nu\|_{\rm TV}=\sup_E|\lambda(E)-\nu(E)|$.

**Theorem 1 (ternary transition).** If $r\to\infty$ and

$$
\frac{\mu k-\log r}{v\sqrt{k}}\longrightarrow s\in\mathbb R,
\tag{4}
$$

then

$$
\left\|\mathcal L(Z\bmod3^k\mid R>r)-\sigma_k\right\|_{\rm TV}
\longrightarrow\Phi(s).
\tag{5}
$$

Equivalently, the center in quotient depth is $(\log r)/\mu$ and the
window width is $v\mu^{-3/2}\sqrt{\log r}$. Their numerical coefficients
are $5.733417$ and $6.343874$, respectively. Below any fixed smaller
fraction of the center the distance tends uniformly to zero; above any
fixed larger fraction it tends uniformly to one.

The main arithmetic contribution is the matching lower bound after
projection to a ternary residue. Projection alone supplies only an upper
bound. We construct a separating set from residues that admit a short
exponent-sum representation and bound its conditional probability by
counting the exact rational numerators of the same affine prefixes.

We also prove a quantitative coding statement. The exponent sum can be
estimated from the depth-$k$ residue with an error having exponential tails,
uniformly in $k$, under $P_*$. The conditional entropy of the entire
length-$k$ word given that residue is bounded independently of $k$.
Consequently $\sigma$ is exact dimensional with dimension

$$
d_* =\frac{(8/3)\log2-\log3}{\log3}=0.682479\ldots.
\tag{6}
$$

These are statements about random affine laws. No typical-path statement
is transferred to a deterministic positive-integer Collatz orbit.

For the original law, write $\rho_k$ for its density on the depth-$k$
ternary quotient, lifted to $\mathbb Z_3$ with Haar probability measure.
El Jaouhari already proves the quadratic energy bound and exact $L^p$
threshold, as detailed in Section 2. We give alternative proofs of
$\|\rho_k\|_2^2\le12k^2$, membership in $L^p$ for $1\le p<2$,
and failure of $L^2$. Our branch-overlap formula is another proof of
positive quadratic-energy increments, also known from his work. These
regularity statements are not claimed as new. They imply that the root
mean square of the primitive depth-$k$ Fourier coefficients has exponential decay rate
$(\log3)/2$. This is a mean-square statement; it does not determine the
extremal Fourier coefficient.

We also determine every finite-level moment's exponential growth rate:
zero for $1<p\le2$ and $\log(3^{p-1}/(2^p-1))$ for $p>2$.
The maximum density has exponential growth rate $\log(3/2)$.
Appendix A determines the power exponent $-2$ of the limiting
density's upper tail, with a quantitative lower bound. Theorem 16 strengthens
the upper estimate to

$$m_3\{\rho>t\}\le C\frac{\log(e+t)}{t^2},\qquad
\int\rho^p\,dm_3\le\frac{C}{(2-p)^2}\quad(3/2\le p<2).$$

A bounded real restriction has every finite ternary moment. More precisely,
the density of the joint event $B<R\le2B$ has $L^q$ norm at most
$C_qB^{1-2/q}\log(eB)^{1-1/q}$. The proof retains the real shell's small
mass when freezing a real test function before applying ternary mixing.
Only a fixed mixing order is needed for the displayed critical-tail bound.
The remaining logarithm does not establish weak-$L^2$ regularity.

Theorem 18 retains each exact central division total. For
$|d-2n|\le C\sqrt n$, the density of the finite prefix restricted to
$B_n\le B$, conditional on $D_n=d$, has $L^q$ norm at most
$C_{q,C}(1+B)^{1-1/q}$. For bounded Lipschitz real tests, the corresponding
conditional density converges in $L^q$ to its stationary real-weighted law
at rate $n^{-1/2+\varepsilon}$, for every fixed $q<\infty$ and
$\varepsilon>0$. Appendix C keeps the exact division clock through joint
mixing, so the associated source window is retained. The result gives no
lower existence bound at a specified integer root and does not cover all
large-deviation clocks needed for inverse contraction.
A finer-modulus form of the collision estimate also gives a direct
Fourier-to-mixing reduction with fixed polynomial losses (Section 9.1).
The resulting mixing conclusions are already known.

There is also an application to actual integer predecessors. Combining
this known $L^p$ regularity with Mazur's weighted-path construction,
and choosing a suitable nonperiodic predecessor of size $O(a)$, gives for each
$\varepsilon>0$ a constant $c_\varepsilon>0$ such that the lower
natural density of ordinary Collatz predecessors of $a$ is at least
$c_\varepsilon a^{-2-\varepsilon}$ whenever $3\nmid a$. The
coefficient is uniform in $a$. The finite count holds whenever its
cutoff $Y$ satisfies $Y\ge C_{\rm on}a$, for one absolute constant
$C_{\rm on}$, independent also of $\varepsilon$. Using Shaik's explicit primitive-decay recipe,
Section 9.2 also gives the single subpower loss
$c a^{-2}\exp[-C\log(3+a)/\log\log(9+a)]$.
The external weighted-path input is stated precisely
in Section 8.2, along with its verification status. Corollary 17 improves
this paper's coefficient to $c/[a^2\log(ea)]$ with the same linear onset,
using the new density tail and the same weighted-path input. Stronger
reciprocal predecessor counts from a separate construction are compared in
Section 9.2. The new analytic result in Theorem 16 does not depend on that
integer-path input and supplies no uniform trace at specified integer roots.

## 2. Relation to previous work

Tao introduced the finite Syracuse laws and proved fine-scale mixing for
the original geometric exponent distribution [1]. In particular, his
estimate implies that the ternary limit has a density with respect to
Haar measure. Sum-conditioned and joint formulations of that mixing
retain the division exponent; Allikvere's results [2] are a relevant
precedent. Those results concern the original law and its central
exponent sums. The rare real-tail conditioning considered here selects
the different law (2), whose ternary limit is singular.

The scalar tail asymptotic and the change of measure (2) are classical
Kesten–Grincevičius–Goldie theory [3,4]. Conditioned-path comparisons with
the associated positive-drift walk go back at least to Asmussen [5].
Buraczewski, Collamore, Damek and Zienkiewicz study perpetuity exceedance
times, including the critical logarithmic time and the half-tail
asymptotic [6]. Blanchet, Lam and Zwart use the same change of measure
in rare-event simulation [7]. The full-prefix estimate below is an
elementary consequence of this framework. We do not claim novelty for
the tail tilt, its drift, or the typical exceedance time.

Brofferio identifies the Poisson boundary of rational affine random
walks through their contracting completions [8]. Under (2), only the
ternary completion contracts: the real drift is positive and the
$2$-adic drift is positive. Thus the full ternary value is the natural
maximal boundary. The almost-sure coding recovery proved below is
consistent with, and substantially covered by, that boundary theory.
Our finite-quotient estimate is quantitative: it bounds the information
lost at precision $3^{-k}$ by a constant. We include an elementary proof
adapted to the rational numerator formula needed for Theorem 1.

Evaluating Collatz-related affine series in different completions also
appears in Siegel's numen framework [9]. The contribution here is the
Gaussian transition for the ternary quotient under a real-tail event,
with a residue-measurable separating set and an explicit finite counting
bound. We have not located this conclusion in the cited work. Our
access to Asmussen [5] was limited to its abstract; the scalar renewal
input is verified from the explicit statements in [4,6].

The offset injectivity used in Lemma 3 is Tao's Lemma 6.2 [1]; we give
a numerator reconstruction for that known fact. Tao's Section 6 also
uses collision estimates on stopped high-probability slices.
El Jaouhari [10, Sections 5.4–5.5] already proves the global quadratic
energy upper bound, positive energy increments, and the exact strong
$L^p$ range $1\le p<2$. His density $f$ is relative to Haar probability
on the units: $\rho=(3/2)f$ there and zero on nonunits. Consequently
his energy bound $E_k^{\rm unit}\le8k^2$ gives exactly
$\|\rho_k\|_2^2\le12k^2$ in our normalization. Our exponential-weight
fiber estimate and branch-overlap proof provide alternative derivations
of these known statements, not a priority claim. His stronger uniform
atom floor also implies his positive energy increments. We read the
relevant written proofs but did not rebuild the formal development.

Fourier Wren [11] computes finite energy increments and studies extremal
Fourier decay. Its Section 6 leaves all-level mean-square control open.
Corollary 10 records a consequence of the now-known regularity estimates:
the exponential rate of that mean square. It does not prove a bounded
prefactor or the conjectured extremal rate. The additional results here
are the projected Gaussian tail-conditioning transition, finite-precision
coding estimate, higher-moment spectrum, quantitative power-$2$ density
tail, and target-uniform counting consequences. We found no corresponding
statements in [10]; its counting theorem has target-dependent onset and
subpower loss in source size.

Mazur proves positive predecessor density for every fixed target coprime
to $3$ [12], using a weighted construction from his preceding paper [13].
His general-target statement leaves uniform dependence on the target
outside its scope. We use that weighted construction and replace its
coarse density-height truncation with Hölder's inequality. A two-sibling
argument bounds the selected nonperiodic seed by a constant times the
target. This yields the uniform power $a^{-2-\varepsilon}$. Wirsching's
preliminary manuscript [14] proposes the stronger $c/a$ bound and states
three remaining conjectures; our result does not resolve that conjecture.

Two further predecessors clarify the attribution. Mghirbi [15, Lemma 6.1]
already uses two direct siblings in a favorable residue to choose a
nonperiodic seed. Shaik [16, Lemmas 1.4--1.5 and Theorem 10.10] gives
that selection in a finite root-pool framework, and [16, Proposition 10.1]
already converts residue moments to integer mass by Hölder. We do not
claim those mechanisms as new. Shaik's finite moment certificates and
block propagation give exponential upper ceilings; [16, Appendix D.3]
explicitly leaves polynomial moments at orders $3/2$ and $2$ open.
El Jaouhari's global quadratic bound and uniform $L^p$ norms supply that
regularity. The exponent $2+\varepsilon$ in our uniform target bound
is a consequence of those known estimates and the weighted-path input.
We include the short seed and Hölder arguments to make that consequence inspectable with the simpler input (34).

## 3. Scalar tail and prefix likelihood

The recursion is

$$
R\overset d=a(R'+1/3),
\qquad R'\text{ independent of }a.
\tag{7}
$$

Put

$$
m(u)=Ea^u=\frac{3^u}{2^{1+u}-1}.
\tag{8}
$$

Then $m(1)=1$, $m'(1)=\mu>0$, and $E\log a<0$. The multiplier and
additive term $a/3$ are positive and bounded above. The affine maps
have no common fixed point. The additive group generated by the support
of $\log a$ contains both $\log2$ and $\log3$, so it is dense.
Thus the law is nonarithmetic in the renewal sense. Although its support
lies in a translate of $(\log2)\mathbb Z$, it does not lie in
$h\mathbb Z$ for any $h>0$; [4, Section 2] explicitly distinguishes
these two conventions.

The scalar theorem therefore yields

$$
q(r)\sim\frac{C}{r},\qquad
C=\frac{E[(aR'+a/3)-aR']}{E(a\log a)}
=\frac1{3\mu}.
\tag{9}
$$

The numerator is $E(a/3)=1/3$. This subtraction is pointwise before
expectation and does not require a finite first moment of $R$.

On a length-$k$ prefix, $dP_*/dP=A_k$. Under $P_*$ the variables
$\log a_j$ have mean $\mu$, variance $v^2$, and finite third absolute
moment. Since $R=B_k+A_kR'$ with an independent suffix, the conditional
prefix likelihood relative to $P_*$ is exactly

$$
L_{r,k}=\frac{q((r-B_k)/A_k)}{A_kq(r)},
\qquad
\operatorname{TV}_{\rm prefix}=E_*(1-L_{r,k})_+.
\tag{10}
$$

Here $q(u)=1$ for $u\le0$. The negative-part formula follows from
$E_*L_{r,k}=1$.

**Lemma 2 (prefix transition).** Under (4), the quantity in (10)
converges to $\Phi(s)$.

*Proof.* Let $S_j=\log A_j$, $S_0=0$. For $0<\theta<1$,
$E_*e^{-\theta\log a}=m(1-\theta)<1$. Reversal of independent
increments and the nonnegative-supermartingale maximal inequality give

$$
P_*\left(\max_{0\le j\le k}S_j-S_k>h\right)\le e^{-\theta h}.
\tag{11}
$$

Take $h=k^{1/4}$. On $S_k\le\log r-h$ and drawdown at most $h/2$,

$$
\frac{A_k}{r}\le e^{-h},\qquad
\frac{B_k}{r}\le\frac{k}{3}e^{-h/2}=o(1).
$$

The argument $(r-B_k)/A_k$ tends uniformly to infinity there. From
(9), $L_{r,k}=1+o(1)$ uniformly on this region. On
$S_k\ge\log r+h$, (10) instead gives
$0\le L_{r,k}\le2e^{-h}/C=o(1)$ for large $r$.
The intermediate strip has probability $o(1)$ by the central limit
theorem, since $h=o(\sqrt{k})$. Hence

$$
\operatorname{TV}_{\rm prefix}
=P_*(S_k>\log r)+o(1)\longrightarrow\Phi(s).
\tag{12}
$$

Using the bounded negative part in (10) avoids a uniform-integrability
claim for the likelihood itself. $\square$

For clarity about rates, define
$\eta(x)=\sup_{u\ge x}|u q(u)/C-1|$. Taking $h=8\log k$ and
$\theta=1/2$ in the same proof, and applying Berry–Esseen to the middle
strip, gives for sufficiently large $k,r$

$$
\left|\operatorname{TV}_{\rm prefix}
-\Phi\left(\frac{\mu k-\log r}{v\sqrt{k}}\right)\right|
\ll\frac{\log k+1}{\sqrt{k}}+\eta(k^8/2)+\eta(r).
\tag{13}
$$

Indeed the bad drawdown probability is at most $k^{-2}$, while the
lower region has $B_k/r\le k^{-3}/3$ and
$(r-B_k)/A_k\ge k^8/2$. Equation (13) reduces the error to the
classical scalar renewal error; it supplies no new rate for $\eta$.

## 4. Exact numerator counting and the projection lower bound

Every prefix has the form

$$
B_k=\frac{C_k}{2^{D_k}},\qquad
C_k=3^{k-1}+3^{k-2}2^{e_k}+\cdots+2^{e_2+\cdots+e_k}.
\tag{14}
$$

**Lemma 3 (coding and counts).** For fixed $k$, the pair $(D_k,C_k)$
determines the exponent word, as follows also from Tao's offset
injectivity [1, Lemma 6.2]. Consequently:

1. For fixed $z\bmod3^k$, fixed $D_k=d$, and $B_k\le Kr$, there are
   at most $Kr2^d/3^k+1$ possible words.
2. If $E_{k,m}$ is the set of residues admitting a word with
   $D_k\le m$, then $|E_{k,m}|\le4^m/3^k$.

*Proof.* When $k\ge2$,
$v_2(C_k-3^{k-1})=e_k$. Subtracting $3^{k-1}$ and dividing by
$2^{e_k}$ gives the numerator for length $k-1$. Repetition recovers
$e_k,\ldots,e_2$, and $D_k$ recovers $e_1$. The case $k=1$ is immediate.

Since $C_k\equiv2^d z\pmod{3^k}$, the first assertion counts positive
integers in one arithmetic progression up to $Kr2^d$. For the second,
choose one word for each residue in $E_{k,m}$. Each chosen word has
$P_*$-probability $3^k4^{-D_k}\ge3^k4^{-m}$; their probabilities sum
to at most one. If $m<k$, the set is empty. $\square$

The numerator bound retains the congruence and the real prefix constraint
on the same word. This is the ingredient that projection alone lacks.

**Lemma 4 (small conditional mass of short representations).** Let
$P_r=P(\cdot\mid R>r)$, $K\ge1$, $H,h>0$, and

$$
t=\log_2(3^k/r),\qquad m=\lfloor t-H\rfloor,
\qquad\delta=2(3/4)^8.
$$

Then

$$
P_r(Z\bmod3^k\in E_{k,m})
\le\frac{q(Kr)}{q(r)}+\frac{\delta^k}{q(r)}
+\frac{2^{-h}+8k(K+2^h)4^{-H}}{r q(r)}.
\tag{15}
$$

*Proof.* The conditional probability of $A_k\ge r2^h$ is at most
$2^{-h}/(r q(r))$, by $dP=A_k^{-1}dP_*$ on prefixes and by bounding
the conditional suffix probability by one. Also
$P_r(R>Kr)=q(Kr)/q(r)$. Finally,
$E_P(4/3)^{e_1}=2$, so Chernoff gives
$P_r(D_k>8k)\le\delta^k/q(r)$.

On the remaining event, $B_k\le R\le Kr$ because all real summands are
positive, and $d=D_k>t-h$. A word of total sum $d$ has original
probability $2^{-d}$. By Lemma 3, for every fixed residue and sum its
conditional contribution is at most

$$
\frac{Kr/3^k+2^{-d}}{q(r)}
\le\frac{(K+2^h)r}{3^kq(r)}.
$$

There are at most $8k$ possible sums. Multiplying by
$|E_{k,m}|\le4^m/3^k$ and using
$4^m\le(3^k/r)^2 4^{-H}$ proves (15). $\square$

*Proof of Theorem 1.* Set

$$
H=\lceil4\log_2k\rceil,\qquad h=H/2,\qquad K=k^2.
$$

Under (4), $\log r=\mu k+O(\sqrt{k})$. The first term in (15) is
$O(k^{-2})$ by (9); the last is $O(k^{-2})$. The middle tends to zero
because

$$
\mu+\log\delta=-1.433893\ldots<0.
$$

Thus $P_r(E_{k,m})=o(1)$. But

$$
\sigma_k(E_{k,m})\ge P_*(D_k\le m)
=P_*(S_k\ge\log r+H\log2+O(1))\longrightarrow\Phi(s).
$$

This proves the lower bound in (5). The upper bound follows by projecting
the full-prefix laws in Lemma 2. Monotonicity of quotient TV with respect
to $k$ extends the transition to the two stated outer regimes. $\square$

## 5. Bounded information loss at finite precision

Let $d_k(z)$ be the smallest exponent sum of a length-$k$ word coding
the residue $z$, and define under $P_*$

$$
\Delta_k=D_k-d_k(Z\bmod3^k)\ge0,\qquad
V_k=\frac{C_k}{3^k}=\frac{B_k}{A_k}.
\tag{16}
$$

Only residues in the image of the coding map need a value of $d_k$.

**Theorem 5 (uniform decoding error and entropy).** There are positive
constants $c,C_0$ independent of $k$ such that

$$
P_*(\Delta_k\ge u)\le C_0e^{-cu}\quad(u\ge0),
\qquad
H(e_1,\ldots,e_k\mid Z\bmod3^k)\le C_0.
\tag{17}
$$

*Proof.* For every $0<\theta<1$, reversal of independent increments
and subadditivity give

$$
E_*V_k^\theta
\le\frac{3^{-\theta}}{1-m(1-\theta)}=:M_\theta<\infty.
\tag{18}
$$

In fact $V_k$ has the law of
$(1/3)\sum_{j=0}^{k-1}\exp(-S_j)$ under $P_*$.

For fixed $z,d$, Lemma 3 bounds the number of words with $V_k\le K$
by $K+1$. Since all words with sum $d$ have tilted probability
$3^k4^{-d}$, for integer $u\ge0$

$$
\begin{aligned}
P_*(\Delta_k\ge u,V_k\le K)
&\le\frac43(K+1)4^{-u}
   \sum_z3^k4^{-d_k(z)}\\
&\le\frac43(K+1)4^{-u}.
\end{aligned}
\tag{19}
$$

For the last inequality, select one minimum-sum word for each residue.
Taking $K=4^{u/(1+\theta)}$ in (19) and using (18) proves the exponential
tail in (17).

The residue, $\Delta_k$ and $\lfloor V_k\rfloor$ determine $D_k$ and
$C_k$, hence the word by Lemma 3. The exponential tail bounds the
entropy of $\Delta_k$ uniformly. The positive fractional moment in
(18) bounds the entropy of $\lfloor V_k\rfloor$ uniformly: compare its
law with the normalized reference probabilities proportional to
$(j+1)^{-1-\theta/2}$ and use nonnegativity of relative entropy.
Subadditivity of entropy completes the proof. $\square$

**Corollary 6 (exact dimension).** The measure $\sigma$ is exact
dimensional, with dimension $d_*$ in (6), and

$$
H(\sigma_k)=kH(P_*)+O(1).
\tag{20}
$$

*Proof.* The entropy identity gives (20). For the almost-sure statement,
let $W_k=(e_1,\ldots,e_k)$ and

$$
I_k=-\log P_*(W_k\mid Z\bmod3^k).
$$

Its expectation is bounded by Theorem 5. Markov's inequality and
Borel–Cantelli on $k=j^2$ show that $I_k/k\to0$ along this subsequence,
almost surely. The strong law gives
$-k^{-1}\log P_*(W_k)\to H(P_*)$. Therefore

$$
-\log\sigma_k(Z\bmod3^k)=-\log P_*(W_k)-I_k
$$

divided by $k$ tends to $H(P_*)$ along $j^2$. Monotonicity of nested
ball probabilities and $(j+1)^2/j^2\to1$ extend the limit to all $k$.
Finally $H(P_*)=(8/3)\log2-\log3$. $\square$

The full ternary value determines the infinite tilted exponent word
almost surely. To see this directly, put $h_0=H(e_1\mid Z)$. The
invertible affine recursion and independence of the suffix give
$H(W_k\mid Z)=kh_0$. Conditioning on $Z$ gives no more entropy than
conditioning on its residue, so Theorem 5 forces $h_0=0$. Iterating
recovers all exponents. We regard this as an elementary manifestation
of the boundary theory discussed in Section 2, rather than a new general
Poisson-boundary theorem.

## 6. Joint tail law and the full ternary space

**Corollary 7 (angular tail law).** Let $Y$ have the Pareto distribution
$P(Y>t)=t^{-1}$ for $t\ge1$, independently of $Z_*\sim\sigma$. Then

$$
\mathcal L((R/r,Z)\mid R>r)\Longrightarrow\mathcal L(Y,Z_*).
\tag{21}
$$

For every finite $r>0$, however,

$$
\left\|\mathcal L(Z\mid R>r)-\sigma\right\|_{\rm TV}=1.
\tag{22}
$$

*Proof.* For each fixed quotient, prefix likelihood convergence follows
from Lemma 2 and projection, or directly from (10). Thus for a ternary
cylinder $E$ and fixed $t\ge1$,

$$
P(R/r>t,Z\in E\mid R>r)
=\frac{q(tr)}{q(r)}P(Z\in E\mid R>tr)
\longrightarrow t^{-1}\sigma(E).
$$

Regular variation gives radial tightness, and $\mathbb Z_3$ is compact.
These tail cylinders determine (21).

For (22), let $\rho_k$ be the original ternary law's level-$k$ density
with respect to Haar probability measure. Tao's fine-scale estimate
gives $\|\rho_n-\rho_m\|_1\ll_A m^{-A}$ for $n\ge m$, hence an
$L^1$ limit density. The conditional law at finite $r$ is dominated by
this original law divided by $q(r)>0$, so is absolutely continuous.
Corollary 6 makes $\sigma$ Haar singular. Therefore the two full-space
measures are mutually singular. $\square$

Equivalently, the joint tail measure away from radial zero is
$C x^{-2}\,dx\,\sigma(dz)$. The asymptotic independence in (21) applies
after real-tail conditioning; the original pair $(R,Z)$ is not asserted
independent. Equations (5) and (22) concern different orders of scale.

## 7. Known critical regularity and further moment consequences

Let $m_3$ be Haar probability measure on $\mathbb Z_3$, and set
$\rho_k(z)=3^kP(Z\equiv z\pmod{3^k})$. These are the conditional
expectations of the original density $\rho$ from Section 6. Put
$E_k=\|\rho_k\|_2^2$, with $\rho_0=1$ and $E_0=1$.

**Theorem 8 (known sharp integrability threshold [10]).** For all $k\ge1$,

$$
E_k\le12k^2.
\tag{23}
$$

The limiting density satisfies $\rho\in L^p(m_3)$ for every
$1\le p<2$ and $\rho\notin L^2(m_3)$. Moreover, there are $c>0$
and $k_0$ such that $E_k-E_{k-1}\ge c$ for $k\ge k_0$.

*Alternative proofs.* The assertions above are established in [10] in
unit-Haar normalization. The following proofs are included for the mixed
identities needed in Sections 7–9.

*Proof of the upper bound.* Let $N_d(z)$ count length-$k$ words with
$D_k=d$ and residue $z$. By Lemma 3, their positive numerators are
distinct integers in one class modulo $3^k$. In increasing order,
the $j$th numerator is greater than $(j-1)3^k$. Therefore

$$
N_d(z)^2\le N_d(z)+2\sum_{w:D_k=d,\,Z=z}V_k(w).
$$

For $1<u<2$, weighted Cauchy--Schwarz gives

$$
\begin{aligned}
E_k
&=3^k\sum_z\left(\sum_{d\ge k}N_d(z)2^{-d}\right)^2\\
&\le\frac{u^{1-k}}{u-1}\,3^k
       \sum_{z,d\ge k}u^dN_d(z)^2 4^{-d}\\
&\le\frac{u^{1-k}}{u-1}\,E_*[u^{D_k}(1+2V_k)].
\end{aligned}
\tag{24}
$$

Finite truncation and Tonelli justify the nonnegative sums. Define

$$
G(u)=E_*u^e=\frac{3u}{4-u},\qquad
Q(u)=E_*\frac{u^e}{a}=\frac{u}{2-u}.
$$

The representation of $V_k$ used in (18), retaining its joint dependence
on $D_k$, gives the exact mixed moments

$$
E_*u^{D_k}=G(u)^k,\qquad
E_*[u^{D_k}V_k]
=\frac13\sum_{j=0}^{k-1}G(u)^{k-j}Q(u)^j.
\tag{25}
$$

Take $u=1+1/(4k)$. Then $G(u)\le Q(u)$ and
$u^{1-k}/(u-1)\le4k$. Bernoulli's inequality gives

$$
Q(u)^k
=\frac{(1+1/(4k))^k}{(1-1/(4k))^k}
\le\frac{e^{1/4}}{3/4}<\frac{16}{9}.
$$

For the strict inequality, $\log(4/3)>1/4$. Combining (24)--(25),

$$
E_k\le\frac{64}{9}k\left(1+\frac{2k}{3}\right)
\le\frac{320}{27}k^2<12k^2.
\tag{26}
$$

*Proof of the $L^p$ inclusion.* Tao's estimate supplies
$\|\rho_n-\rho_m\|_1\ll_A m^{-A}$ for $n\ge m\ge1$ and every
$A>0$. Equation (23) gives
$\|\rho_{2m}-\rho_m\|_2=O(m)$. If $1<p<2$, let
$\vartheta=2/p-1\in(0,1)$. Interpolation yields

$$
\|\rho_{2m}-\rho_m\|_p
\ll_{A,p}m^{-A\vartheta+1-\vartheta}.
\tag{27}
$$

Choose $A>(1-\vartheta)/\vartheta$ and sum over $m=2^j$.
The dyadic densities converge in $L^p$, and their $L^1$ limit is
$\rho$. The endpoint $p=1$ was established in Section 6.

*Proof of the $L^2$ exclusion.* For $F_e(x)=(3x+1)/2^e$, define

$$
(L_e f)(z)=3\,2^{-e}\,1_{F_e\mathbb Z_3}(z)\,
                    f((2^ez-1)/3).
$$

The Haar Jacobian of $F_e$ is $1/3$. The transfer operator
$L=\sum_{e\ge1}L_e$ satisfies $\rho=L\rho$ and
$\rho_{k+1}=L\rho_k$. For any nonnegative $f\in L^2$,

$$
\|L_e f\|_2^2=3\,4^{-e}\|f\|_2^2,\qquad
\sum_{e\ge1}3\,4^{-e}=1.
\tag{28}
$$

If $\rho$ were in $L^2$, stationarity and expansion by Tonelli would
force all cross terms between distinct $L_e\rho$ to vanish. Writing
$E=\{\rho>0\}$, the sets $F_eE$ would be pairwise disjoint modulo
null sets. Each has the same positive measure $m_3(E)/3$. Infinitely
many such subsets of a probability space cannot be pairwise disjoint.
This contradiction proves $\rho\notin L^2$.

*Proof of positive energy increments.* First $\rho>0$ almost everywhere
on the units. Indeed stationarity gives $F_eE\subseteq E$ modulo
null sets for every $e$. Let $C=3E+1$, a positive-measure subset of the
unit group. The union of $2^{-e}C$ over $e\ge1$ has full measure in
that group: multiplication by $2$ is ergodic, since its order modulo
$3^j$ is $2\cdot3^{j-1}$. This union lies in $E$. The law has no mass
on $3\mathbb Z_3$, so this also identifies the essential support.

Put $S(x)=4x+1$. Opposite-parity branches have disjoint ranges. For
$e\ge1$ and $d\ge1$, the change of variable $z=F_e(x)$ gives

$$
\langle L_e f,L_{e+2d}f\rangle
=3\,4^{-e-d}\int f(x)f(S^d x)\,dm_3(x).
$$

Summing the diagonal terms using (28), and both orders of the cross
terms, yields the exact identity

$$
E_{k+1}-E_k
=2\sum_{d\ge1}4^{-d}
       \int\rho_k(x)\rho_k(S^d x)\,dm_3(x).
\tag{29}
$$

Since $x$ and $Sx$ are both units when $x\equiv1\pmod3$, the
integral of $\min(\rho,M)(x)\min(\rho,M)(Sx)$ is positive for any
$M>0$. The bounded truncations of $\rho_k$ converge to this truncation
in $L^1$, and $S$ preserves Haar measure. Their product integrals
therefore converge. Retaining only $d=1$ in (29) and using these
truncations gives the claimed eventual lower bound. $\square$

**Theorem 9 (moment spectrum).** For $p>1$, put
$M_p(k)=\int\rho_k^p\,dm_3$. Then

$$
\lim_{k\to\infty}\frac1k\log M_p(k)
=\begin{cases}
0,&1<p\le2,\\
\log\bigl(3^{p-1}/(2^p-1)\bigr),&p>2.
\end{cases}
$$

For each fixed $p>2$, writing $\lambda_p=3^{p-1}/(2^p-1)>1$,
there is $C_p<\infty$ such that
$\lambda_p^k\le M_p(k)\le C_p k^{p-1}\lambda_p^k$.
In addition,

$$
\lim_{k\to\infty}\frac1k\log\|\rho_k\|_\infty=\log(3/2).
$$

*Proof.* The range $1<p\le2$ follows already by interpolation between
$\|\rho_k\|_1=1$ and (23); no Fourier mixing input is needed for this
exponential-rate statement. For $p>2$, the branch formula gives
$\|L_e f\|_p^p=3^{p-1}2^{-ep}\|f\|_p^p$. Nonnegativity implies
$M_p(k+1)\ge\lambda_p M_p(k)$, proving the lower bound.
The function $\log\lambda_p$ has positive second derivative for $p>0$
and positive first derivative at $2$, and $\lambda_2=1$; hence
$\lambda_p>1$ for $p>2$.

Set $q=p-1>1$. For fixed sum and residue, order the $N=N_d(z)$
numerators as $V_i=C_i/3^k>i-1$. Then

$$
N^p\le p\sum_{i=1}^N(1+V_i)^q
\le p\,2^{q-1}\sum_{i=1}^N(1+V_i^q).
$$

The first inequality uses
$\sum_{i=1}^Ni^q\ge\int_0^N x^q\,dx=N^p/p$.
Weighted Hölder with $u>1$, $t=u^q<2$, and
$c_k(u)=u^{1-k}/(u-1)$ consequently gives

$$
\begin{aligned}
M_p(k)
&\le c_k(u)^q3^{kq}\sum_{z,d}t^dN_d(z)^p2^{-pd}\\
&\le p\,2^{q-1}c_k(u)^q\lambda_p^k
           E_p[t^{D_k}(1+V_k^q)],
\end{aligned}
$$

where $P_p(e)=(2^p-1)2^{-pe}$. Let
$G_p(t)=E_p t^e=(2^p-1)t/(2^p-t)$ and tilt this product law to
$P_{p,t}(e)=t^eP_p(e)/G_p(t)$. The remaining expectation is
$G_p(t)^k E_{p,t}(1+V_k^q)$. Reversal expresses $V_k$ as
$(1/3)\sum_{j=0}^{k-1}\prod_{i=1}^j a_i^{-1}$, and

$$
H_p(t):=E_{p,t}a^{-q}=\frac{2^p-t}{3^q(2-t)},\qquad
H_p(1)=\lambda_p^{-1}<1.
$$

For $u$ sufficiently close to one, $H_p(t)<1$. Minkowski gives,
uniformly in $k$,

$$
(E_{p,t}V_k^q)^{1/q}
\le\frac{1}{3(1-H_p(t)^{1/q})}.
$$

Since $c_k(u)^q=[u/(u-1)]^qu^{-qk}$, the upper exponential rate is
at most
$\log\lambda_p+\log(G_p(t)/t)$.
Letting $u\downarrow1$ proves the stated limit. More quantitatively,
take $u=1+c_p/k$ with a sufficiently small fixed $c_p>0$.
Then $H_p(u^q)$ stays strictly below one and
$[G_p(u^q)/u^q]^k$ stays bounded, proving the polynomial prefactor.
All word sums are nonnegative and can be justified by finite truncation.

Finally the all-one word gives $\rho_k(-1)\ge(3/2)^k$.
On the finite quotient,
$\|\rho_k\|_\infty^p\le3^kM_p(k)$, so for every fixed $p>2$
its upper exponential rate is at most
$\log3-p^{-1}\log(2^p-1)$.
Let $p\to\infty$ to obtain $\log(3/2)$. $\square$

Shaik [16, Appendix D.3] establishes existence and monotonicity of
Rényi divergence rates using moment inheritance, and identifies the
order-one rate as zero. Theorem 9 determines the rates at every higher
order: divide the displayed moment rate by $p-1$. The underlying
numerator argument is independent of Tao's fine-scale theorem, which
is needed above to obtain bounded moments, rather than merely zero
exponential rates, for $1<p<2$.

**Corollary 10 (primitive Fourier mean square).** Set
$\chi_k(\xi)=E\exp(2\pi i\xi Z/3^k)$ and

$$
M_{2,k}=\left(\frac{1}{2\cdot3^{k-1}}
     \sum_{3\nmid\xi\bmod3^k}|\chi_k(\xi)|^2\right)^{1/2}.
$$

For some positive constants $c_1,C_1$ and all sufficiently large $k$,

$$
c_1\,3^{-k/2}\le M_{2,k}\le C_1 k\,3^{-k/2},\qquad
-\frac1k\log M_{2,k}\longrightarrow\frac{\log3}{2}.
\tag{30}
$$

*Proof.* Parseval and consistency of the quotient laws give
$\sum_{3\nmid\xi}|\chi_k(\xi)|^2=E_k-E_{k-1}$. Apply Theorem 8.
$\square$

No linear upper bound for $E_k$, bounded upper bound for its increments,
or extremal Fourier decay rate is established. The $L^p$ estimates
control the mass of small measurable sets by Hölder's inequality; they
do not provide relative estimates at a prescribed moving integer.

## 8. Integer traces and polynomial predecessor density

### 8.1. A fixed-integer trace

The tilted law also has an exact positive-integer interpretation. For
positive odd integers, let

$$
U(x)=\frac{3x+1}{2^{v_2(3x+1)}},\qquad
\omega_k(x)=\frac{3^k}{2^{\sum_{j<k}v_2(3U^j(x)+1)}}.
$$

**Proposition 11.** For every positive odd $a$ and every $k\ge0$,

$$
3^k\sigma(a+3^k\mathbb Z_3)
=\sum_{U^k(x)=a}\omega_k(x)^2.
\tag{31}
$$

If $a$ is nonperiodic, then

$$
\sum_{k\ge0}3^k\sigma(a+3^k\mathbb Z_3)
\le\frac{\pi^2}{8}a^2.
\tag{32}
$$

For periodic $a$, the right side may be multiplied by at most $3a+1$.

*Proof.* Expose the prefix in inverse chronological order. Its first
congruence is $2^{e_1}a\equiv1\pmod3$, giving the positive odd integer
$x_1=(2^{e_1}a-1)/3$. Dividing out this congruence gives the next one.
Induction recovers a positive odd predecessor path, with exactly the
specified valuations. Conversely every such path supplies the prefix
congruence. A length-$k$ word has tilted probability
$3^k4^{-D_k}$; multiplying by $3^k$ gives $\omega_k^2$, proving (31).

The real affine identity gives $x\omega_k(x)\le a$. When $a$ is
nonperiodic, each source can reach it at only one time. Summing over
all odd positive sources therefore gives
$a^2\sum_{x\ \mathrm{odd}}x^{-2}=\pi^2a^2/8$.

On a cycle, each repeated visit contributes a further factor
$\lambda^2$, where

$$
\lambda=\prod_{u\text{ on the cycle}}\frac{3u}{3u+1}
\le\frac{3a}{3a+1}<1.
$$

The return sum is at most $1/(1-\lambda^2)\le3a+1$. $\square$

Thus every positive odd integer is a point where the normalized ball
masses tend to zero and are summable over depths, despite the typical
dimension being $d_*<1$. This does not provide a subquadratic bound
uniform in a moving target $a$. In particular, (32) cannot be applied
as though its right side were fixed along an unbounded forward orbit.
Neither cycles nor divergent integer orbits are excluded by this paper.

### 8.2. Uniform polynomial dependence on the target

For a positive integer $a$, let $\mathcal P(a)$ be the set of positive
integer starts whose ordinary Collatz orbit visits $a$. Write
$\underline d$ for lower natural density.

**Theorem 12 (polynomial predecessor density).** Using the weighted-path
input of Mazur [12, Proposition 3.1], for every $\varepsilon>0$ there is
$c_\varepsilon>0$ independent of $a$ such that

$$
\underline d(\mathcal P(a))\ge c_\varepsilon a^{-2-\varepsilon}
\qquad(a\ge1,\ 3\nmid a).
\tag{33}
$$

More precisely, there is an absolute $C_{\rm on}>0$, independent also
of $\varepsilon$, such that

$$
\#\bigl(\mathcal P(a)\cap[1,Y)\bigr)
\ge c_\varepsilon Y a^{-2-\varepsilon}
\qquad(Y\ge C_{\rm on}a).
$$

The constant $C_{\rm on}$ is finite but inherits very large absolute
constants from the weighted-path construction.

Here is the exact imported input. There are universal integers $B_0,q$
with $q\ge1$ and a unit $y\pmod{3^q}$ with the following property.
For every odd $R\ge B_0$ with $R\equiv y\pmod{3^q}$ and all sufficiently
large real $X$, there exist $k\ge1$, $J\ge0$, a finite family $\mathcal W$
of exact positive odd valuation words ending at $R$, and selected weights
$v_w$ such that

$$
\begin{gathered}
3^k\le X,\qquad X\le x_w<32X,\qquad0\le v_w\le\omega_w,\\
\frac23\le\sum_{w\in\mathcal W}v_w
        \sum_{j=0}^J4^{-j}r_k(\Psi_j(x_w)),\qquad
\Psi_j(x)=4^jx+\frac{4^j-1}{3}.
\end{gathered}
\tag{34}
$$

The source $x_w$ follows the word to $R$ with its exact valuations, and
$\omega_w=3^{|w|}2^{-D(w)}$. The reference functions in [12] are
$r_k=(2/3)\rho_k$, by [13, equation (2.2)] and [12, Appendix A.1].
The recursion used there has the same quotient law by reversal of the
iid exponents. We take its auxiliary parameter $m=1$. The proof of the
input permits $H(R,1)=A_*R$ with an absolute finite $A_*$, as follows.

Fix the floor $b=2^{80}$, Fourier constant, caps
$K_j=16+\lfloor j/100\rfloor$, and startup parameters $N,N_t,q$ of
[13, Sections 8.2--8.3]. These precede the numerical root. The central
pullback at stage $N$ has average at least $255/256$ over unit residues.
Choose a residue with at least this mark. Every odd representative
$R\ge16^b$ has the same mark: exact integer inverse paths are supplied
by the physical floor. The subsequent central, terminal-transport and
terminal-exclusion errors have the root-independent bounds displayed in
[13, Section 8.3], respectively $F(j+1)^3r^j$ and twice
$21F(j+1)^5r^j$, with $r=9999/10000$. Thus the marked mass is at least
$175/256>2/3$ whenever $n\ge N+N_t$ and $X$ belongs to every endpoint's
admissible external-scale interval. This is also the uniform calculation
in [12, Appendix A.2].

Put $J_* =\max(N+N_t,20\cdot10^9)$ and write $\beta(j)$ for the floor
sequence of [13]. Its Section 8.5 bounds every endpoint at generation
$J_*$ by $2^{E(J_*)}R$, and every upper external-scale endpoint there
by $A_*R$, where

$$
\begin{gathered}
E(0)=0,\qquad
E(j+1)=E(j)+17+\lfloor j/100\rfloor
                    +2\beta(j)-\lfloor19\beta(j)/12\rfloor,\\
A_*=2^{E(J_*)+\lfloor2\beta(J_*)/3\rfloor}.
\end{gathered}
$$

These bounds include all histories. The scale intervals overlap after
$20\cdot10^9$ independently of the root, since their sufficient spread
condition involves only the floors and caps. The proof of [13, Lemma 6.2]
therefore supplies a common admissible generation for every $X>A_*R$.
The terminal reduction and modulus estimate of [12, Appendix A.3--A.4]
give (34) throughout this range. All its depths satisfy $k\ge1$.
The target-dependent coarse depth used later in [13, Section 8.4] is
unnecessary here because the known $L^p$ bound holds at every depth.

This is a substantive external input about exact integer paths. It is
not replaced here by congruence mixing. Appendix A of [12] derives it
from [13] while retaining the central and terminal path restrictions.
We have read the written construction and its counting interface. The
source reports Lean verification for related main statements, but [12]
expressly does not advertise Proposition 3.1 as a separately checked
formal declaration. We have not independently rebuilt those dependencies.

*Proof of Theorem 12.* Fix $1<p<2$, put $p'=p/(p-1)$, and let
$K_p=\|\rho\|_p<\infty$, supplied by Theorem 8. Since $\rho_k$ are
conditional expectations of $\rho$, their $L^p$ norms are at most $K_p$.
Every $\Psi_j$ permutes the full group $\mathbb Z/3^k\mathbb Z$, so
Minkowski's inequality gives

$$
\|g_{k,J}\|_p\le\frac89K_p,\qquad
 g_{k,J}=\sum_{j=0}^J4^{-j}r_k\circ\Psi_j.
\tag{35}
$$

First suppose $R$ has no positive Syracuse return. The sources in
$\mathcal W$ are distinct: unequal hitting times of $R$ would give a
return, and equal hitting times determine the word. Set
$\mathcal A=\{x_w:w\in\mathcal W\}$. The exact affine formula gives
$x_w\omega_w\le R$. Each residue modulo $3^k$ occurs at most
$33X/3^k$ times below $32X$, since $3^k\le X$. Retaining the selected
weights in (34), then using Hölder on distinct integer sources, gives

$$
\begin{aligned}
\frac23
&\le\frac RX\sum_{x\in\mathcal A}g_{k,J}(x)\\
&\le\frac RX|\mathcal A|^{1-1/p}
       \left(\sum_{X\le x<32X}g_{k,J}(x)^p\right)^{1/p}\\
&\le\frac RX|\mathcal A|^{1-1/p}(33X)^{1/p}\frac89K_p.
\end{aligned}
\tag{36}
$$

It follows that $|\mathcal A|/X\ge
(3/(4\,33^{1/p}K_pR))^{p'}$. Applying the construction at $X=Y/32$
for all sufficiently large integer $Y$ yields

$$
\underline d(\mathcal P(R))\ge
\frac1{32}\left(\frac{3}{4\,33^{1/p}K_pR}\right)^{p'}.
\tag{37}
$$

It remains to choose $R\le C a$ with one universal $C$. We use the
two-sibling construction of [15, Lemma 6.1; 16, Lemmas 1.4--1.5]. For any
$a\ge1$ coprime to $3$, choose $e\in\{1,2\}$ so that
$2^ea\equiv1\pmod3$ and put $R_j=(2^ea4^j-1)/3$ for $j\ge0$.
These are distinct positive odd ordinary predecessors of $a$, all with
next odd value equal to the odd part of $a$. The elementary identity
$v_3(4^h-1)=1+v_3(h)$ gives
$v_3(R_{j+h}-R_j)=v_3(h)$. Hence $j\mapsto R_j\pmod Q$, with
$Q=3^q$, permutes the residues on every $Q$ consecutive indices.

Choose a fixed $J_0\ge1$ such that $(2\cdot4^{J_0}-1)/3\ge B_0$.
There is $j\in[J_0,J_0+Q-1]$ with $R_j\equiv y\pmod Q$.
Both $R_j$ and $R_{j+Q}$ are at least $B_0$ in the desired residue,
and both are at most $Ca$, with $C=(4/3)4^{J_0+2Q}$. At most one
can be periodic under $U$: if both were periodic, both would lie on
the cycle containing their common next odd value, contradicting the
unique predecessor on a cycle. Thus one is an eligible nonperiodic
$R\le Ca$. This selection needs no bound on a hypothetical cycle's
maximum and no algorithm deciding which sibling is nonperiodic.

Set $C_{\rm on}=64A_*C$. For every $Y\ge C_{\rm on}a$, we have
$X=Y/32\ge2A_*Ca>A_*R$, so (36) applies at that cutoff. Since
$\mathcal P(R)\subseteq\mathcal P(a)$, it gives a uniform coefficient
times $Ya^{-p'}$. Take $p=(2+\varepsilon)/(1+\varepsilon)$ to obtain
the finite assertion and hence (33). No lower restriction on $k$
depending on $p$ or $R$ was used. $\square$

The same exponent holds for predecessor sets under the shortcut map,
since ordinary predecessors of $2a$ are shortcut predecessors of $a$.
If $3\mid a$, the ordinary predecessor set is $\{2^j a:j\ge0\}$ and
has density zero. Theorem 12 supplies a uniform linear cutoff, but it
remains much larger than the target. On a hypothetical least-counterexample
spine $a_t\ge a_0$, the choice $Y=a_0$ is outside its range. It gives
neither a predecessor below that original minimum nor nonsummable
relative mass along a divergent orbit.

## 9. Direct mixing reduction and a quantitative predecessor coefficient

### 9.1. A collision estimate at a finer ternary modulus

The same numerator bound gives a short alternative to the stopped-prefix
collision argument in Tao's Section 6. The fine-scale mixing conclusions
in this subsection are established results [1,2,17]; we record the explicit
polynomial loss because it permits a quantitative use of [16, Appendix E].

For $1\le r\le n$, set $d_0=\lceil n\log_2 3\rceil$ and

$$
f_d(z)=P(D_r=d,\ B_r\equiv z\pmod{3^n}),\qquad d\ge d_0.
$$

**Proposition 13 (finer-modulus collision and mixing reduction).** Put
$u=1+1/(4n)$, $G(u)=3u/(4-u)$ and $Q(u)=u/(2-u)$. Then

$$
3^n\sum_{d\ge d_0,z}u^d f_d(z)^2
\le Q(u)^r+\frac23\sum_{j=0}^{r-1}G(u)^{r-j}Q(u)^j
\le\frac{16}{9}(1+2r/3).
\tag{38}
$$

For $r<m\le n$, let $\delta$ bound every primitive Fourier coefficient
of the Syracuse laws at depths $m-r+1,\ldots,n-r$. Then

$$
\operatorname{Osc}_{m,n}
\le\sqrt{12}\,n\delta+2P(D_r<d_0).
\tag{39}
$$

Here oscillation is the $\ell^1$ distance from the probability vector
to its average over each coset modulo $3^m$, as in [1]. If the same
$\delta$ bounds the primitive transform uniformly under a twist
$\exp(i\theta D_\ell)$, the joint oscillation retaining $D_n$ satisfies

$$
\operatorname{JOsc}_{m,n}
\le\sqrt{48}\,n^{3/2}\delta
+2P(D_r<d_0)+2P(D_n>4n).
\tag{40}
$$

*Proof.* For fixed $d,z$, let $N_d(z)$ count the prefix words. Their
positive numerators are distinct and congruent modulo $3^n$, even though
the words have length $r$. Hence
$N_d(z)^2\le N_d(z)+2\sum C_r/3^n$. The left side of (38) is at most

$$
3^n\sum_{w:D_r\ge d_0}u^{D_r}4^{-D_r}
+2\sum_w u^{D_r}4^{-D_r}C_r
\le E_Pu^{D_r}+2E_*[u^{D_r}V_r].
$$

For the first term use $3^n4^{-D_r}\le2^{-D_r}$ on the retained event.
For the second use $P_*(w)=3^r4^{-D_r}$ and $V_r=C_r/3^r$.
The mixed moment (25), $E_Pu^{D_r}=Q(u)^r$, and $r\le n$ give (38).
In particular, at $u=1$ the unweighted collision sum is at most $1+2r/3$.

Split the full word after $r$ letters:

$$
X_n=B_r+3^r2^{-D_r}X'_{n-r}\pmod{3^n},
$$

where the suffix is independent. At a frequency with
$j=v_3(\xi)<n-m$, the effective suffix depth is
$n-r-j\ge m-r+1$. The retained law therefore has Fourier transform
$\sum_{d\ge d_0}\widehat f_d(\xi)\chi_{n-r}(2^{-d}\xi)$, whose
squared modulus is at most

$$
\delta^2\left(\sum_{d\ge d_0}u^{-d}\right)
\sum_{d\ge d_0}u^d|\widehat f_d(\xi)|^2.
$$

Sum over the high frequencies, apply Plancherel, and use
$\sum_{d\ge d_0}u^{-d}\le4n$. Equation (38) bounds the result by
$12n^2\delta^2$. The normalized $L^1$ norm is at most the $L^2$ norm.
Removing the discarded prefix mass costs at most $2P(D_r<d_0)$,
which proves (39).

For (40), let $g_t$ be the suffix subprobability with total exponent $t$.
The Fourier transform of the joint slice of total $s$ is
$\sum_d\widehat f_d(\xi)\widehat g_{s-d}(2^{-d}\xi)$.
Parseval in $\theta$ gives
$\sum_t|\widehat g_t(2^{-d}\xi)|^2\le\delta^2$.
For a nonprimitive frequency, the discarded highest ternary digits
contribute an independent sum twist of modulus at most one, so the
same bound holds at the effective depth. Weighted Cauchy and (38)
thus bound the sum of the squared Fourier transforms over all $s$
and high frequencies by $12n^2\delta^2$. Retain $s\le4n$, use
Cauchy over at most $4n$ slices, and discard the upper tail to obtain
(40). This does not bound a rare conditional slice uniformly. $\square$

For $r=\lfloor17n/20\rfloor$ and $m\ge0.9n$, the discarded lower
sum tail is exponentially small and the effective suffix depths are
at least $n/20$. Thus (39) and (40) recover the established high-scale
mixing estimates from primitive decay with fixed polynomial losses.
Projection and a geometric scale telescope give all scales; for the
joint law the independent tail-sum kernel contracts $\ell^1$ and
commutes with residue averaging. The twisted primitive input is supplied
by the known pair-sum argument [1,2]. The point of Proposition 13 is
the global collision estimate (38), not a new mixing conclusion.

### 9.2. One explicit subpower loss in the target

**Corollary 14 (quantitative target dependence).** Using [16, Theorem E.1]
and the same weighted-path input (34), there are absolute $c,C>0$ such that

$$
\underline d\,\mathcal P(a)
\ge c\,a^{-2}\exp\left[-C\frac{\log(3+a)}{\log\log(9+a)}\right]
\qquad(3\nmid a).
\tag{41}
$$

The corresponding finite bound holds for every $Y\ge C_{\rm on}a$,
with the same absolute onset constant as Theorem 12. This still does
not give a $c/a^2$ coefficient or a source below the target.

*Proof.* Shaik's explicit primitive estimate [16, Theorem E.1 and
(E.recipe)] gives $|\chi_n(\xi)|\le C_Bn^{-B}$ for every positive
integer $B$ and primitive $\xi$. Its recipe implies
$\log C_B\le\exp(C_0B)$ for an absolute $C_0$. To check this dependence,
its $K,R$ are $O(B)$, while $\log A,\log H=O(B)$; the fixed
$\epsilon=2^{-78}$ is an absolute constant. With $w_i=v_i+1$, its
recurrence gives $w_{i+1}\le(H+3)w_i^4$, so
$\log w_R\le4^R(\log w_0+\log(H+3)/3)=\exp(O(B))$.
The subsequent $P,Z,M$ are polynomial in $w_R$ with coefficients of
logarithm $O(B)$, and $C_B=(3M)^B$. This proves the asserted growth.
We use the stated primitive theorem, whose Appendix E proof and recipe
we have read; no independent formal rebuild is claimed.

Choose $B=\lfloor\log\log n/(2C_0)\rfloor$ for sufficiently large $n$.
It follows that $|\chi_n(\xi)|\le\exp(-c_0\log n\log\log n)$ for
some fixed $c_0>0$. This optimization is a consequence of the existing
recipe. Applying (39) and telescoping scales gives constants $c_1,C_1>0$
with

$$
\sup_{n\ge m}\|\rho_n-\rho_m\|_1
\le C_1\exp(-c_1\log m\log\log m)
\tag{42}
$$

for sufficiently large $m$. Indeed, the polynomial loss is absorbed by
the displayed rate, and the geometric scale sum is bounded by a constant
times its first term. The same bound holds with $\rho_n$ replaced by
$\rho$. This step only needs marginal mixing.

Let $R$ be the eligible nonperiodic root in (34). Choose an integer
$L=L(R)$ making the right side of (42) at most $1/(88R)$. For large
$R$ one can take

$$
L=\left\lceil\exp\left(K\frac{\log R}{\log\log R}\right)\right\rceil
$$

with a sufficiently large absolute $K$: eventually
$\log\log L\ge\tfrac12\log\log R$, so $K\ge8/c_1$ makes the
exponential in (42) at most $R^{-4}$. Increase the fixed threshold to
absorb $C_1$.

In (34), put $h=\min(k,L)$ and abbreviate $g_j=g_{j,J}$ from (35).
If $k>L$, Haar invariance of every $\Psi_j$ gives
$\|g_k-g_h\|_1\le(8/9)/(88R)$; if $k\le L$, the difference is zero.
By (23), $\|g_h\|_2\le(8\sqrt{12}/9)L$ in either case. For the
selected distinct sources $A\subset[X,32X)$, counting representatives
modulo $3^k\le X$ yields

$$
\sum_{x\in A}|g_k-g_h|(x)\le33X\|g_k-g_h\|_1,
\qquad
\sum_{x\in A}g_h(x)\le\sqrt{33X|A|}\,\|g_h\|_2.
$$

The marked mass and $\omega_w\le R/X$ now imply

$$
\frac23\le\frac RX\sum_{x\in A}g_k(x)
\le\frac{8\sqrt{396}}9 RL\sqrt{|A|/X}+\frac13.
$$

Thus $|A|/X\ge1/(2816R^2L^2)$, and setting $X=Y/32$ gives
$\underline d\,\mathcal P(R)\ge1/(90112R^2L^2)$. The same
credited sibling selection as in Theorem 12 gives $R\le C_{\rm seed}a$.
Substitution proves (41) for large $a$; the fixed-$p$ bound of
Theorem 12 covers bounded $a$ after reducing $c$. For the finite assertion,
the same argument applies at every $Y\ge C_{\rm on}a$: the use of
$h=\min(k,L)$ imposes no condition $k\ge L(R)$. Thus smoothing does not
introduce an additional cutoff depending on the target. $\square$

This is an $L^1$ approximation followed by exact integer residue counting.
It assumes no pointwise approximation at a selected integer. The
primitive-decay constants inherited from [16] are extremely large, and
(41) has the uniform finite-cutoff version just proved. Its subpower loss tends to zero in the
exponent of $a$, but it supplies no universal descent mechanism.
Corollary 17 below replaces this subpower loss by a single logarithm, using
the scalar real tail and a fixed mixing order. Separately, Fourier Wren [18]
proves the stronger reciprocal count $\pi_a(Y)\ge cY/a$ for every $Y\ge a$
through a joint atom-floor construction. We do not claim the coefficient in
Corollary 17 is the strongest available count; its role is an application of
the new critical-tail estimate through the already stated weighted-path
interface, without using that atom floor.

## 10. Finite controls and reproducibility

The proofs above are analytic and do not use numerical fitting. A
five-worker CPU diagnostic counts all exponent words by residue and
total exponent sum, using integer arithmetic, through depth $12$ and
sum $48$. It then evaluates information summaries in long-double
arithmetic. The retained mass at depth $12$ omits $5.585\times10^{-14}$
of the tilted law. No interval certification of the floating summaries
is claimed.

| Depth | Word entropy minus residue entropy | Posterior variance of $D_k$ | Unconditional variance |
|---|---:|---:|---:|
| 3 | 0.4922 | 0.4019 | 1.3333 |
| 6 | 0.7164 | 0.5271 | 2.6667 |
| 9 | 0.8397 | 0.6152 | 4.0000 |
| 12 | 0.9100 | 0.6751 | 5.3333 |

These finite values suggested the coding estimate; Theorem 5 establishes
the uniform conclusion independently. An independent Fraction-based
enumerator through depth $5$ and sum $14$ checks numerator recovery,
residue congruences, both counting bounds, the weighted quadratic-energy
inequality chain (24)--(26), and six diagnostic summaries.
The summaries agree with the integer-count implementation within
$1.34\times10^{-15}$.

A separate five-worker exact-integer checker verifies the residue
permutation, parity, height and shared-successor identities in the seed
selection on 124,146 cases. The at-most-one-periodic-sibling argument
is proved above; the checker does not decide hypothetical cycles.

A third exact-rational check tests the general moment inequalities and
tilted mixed moments at orders $3,4,5$ through depth $5$ and sum $14$.
These finite controls do not establish the asymptotic rates.
A fourth checker verifies 20 finer-modulus collision cases and 7,504
exact prefix/suffix identities for Proposition 13. Independent sampled
joint Fourier factorizations agree within $5.82\times10^{-18}$.

From the supplement root, run:

```bash
g++ -O3 -std=c++17 -fopenmp experiments/tilted_prefix_information.cpp -o tilted_prefix_information
OMP_NUM_THREADS=5 ./tilted_prefix_information 5 14 > results/tilted_prefix_information_small_20261020.json
python experiments/check_tilted_prefix_information.py
python experiments/check_polynomial_density_seed.py
python experiments/check_ternary_moment_spectrum.py
python experiments/check_finer_modulus_collision.py
```

The depth-$12$ diagnostic uses the same executable with arguments
`12 48`. It keeps a few hundred megabytes of working arrays in memory
and writes only the small JSON summary. All supplied code is original
and is released under the MIT license; result files are released under
CC0. No external manuscript or credential is included in the supplement.
Theorems 16 and 18 and Corollary 17 are new analytic deductions, with complete
proofs in Appendices B and C. The original checker sources and retained
outputs are unchanged and were not rerun. One new independent checker,
experiments/check_central_clock_real_localization.py, uses five CPU workers
to verify the finite clock-conditioning, cylinder-transport and actual
source-window interfaces in Appendix C. Its retained result is included.
These finite checks do not verify the asymptotic localization, mixing or
critical-tail claims.

## Appendix A. The power exponent of the limiting density tail

**Proposition 15.** There are $c>0$ and $t_0$ such that

$$
m_3\{\rho>t\}\ge\frac{c}{t^2\sqrt{\log t}}\qquad(t\ge t_0).
\tag{43}
$$

In particular,

$$
\lim_{t\to\infty}\frac{\log m_3\{\rho>t\}}{\log t}=-2.
\tag{44}
$$

This gives the power exponent, not a regularly varying asymptotic or a
weak-$L^2$ upper bound.

*Proof.* Work first under $P_*$ and fix $0<\theta<1$. Put

$$
q_\theta=E_*[(2^e/3)^\theta]
=\frac{3^{1-\theta}2^\theta}{4-2^\theta}<1.
$$

Strict log convexity and equality at $\theta=0,1$ give the last inequality.
Reversal preserves $D_k$ and gives the joint law
$V_k=(1/3)\sum_{j<k}\prod_{i\le j}(2^{e_i}/3)$.
Subadditivity therefore yields

$$
E_*[V_k^\theta 1_{D_k=d}]
\le3^{-\theta}\sum_{j<k}q_\theta^j P_j(D_k=d),
$$

where $P_j$ tilts the first $j$ letters by $(2^e/3)^\theta$.
Under $P_j$ the letters are independent positive geometric variables
with ratios either $1/4$ or $\beta=2^\theta/4\in(1/4,1/2)$.
Every such sum has maximal atom $O(k^{-1/2})$, uniformly in $j$.
Indeed, the squared modulus of a geometric characteristic function is

$$
\left(1+\frac{4\beta}{(1-\beta)^2}\sin^2(t/2)\right)^{-1}
\le\left(1+\frac{16}{9}\sin^2(t/2)\right)^{-1}.
$$

Fourier inversion of the product, using
$\sin(|t|/2)\ge|t|/\pi$ on $[-\pi,\pi]$, bounds its largest atom
by a Gaussian integral of order $k^{-1/2}$.
For $|d-4k/3|\le1$, Stirling's formula applied to
$P_*(D_k=d)=\binom{d-1}{k-1}3^k4^{-d}$ gives a lower bound
$c_0k^{-1/2}$. Dividing the preceding moment estimate by this
probability shows

$$
E_*[V_k^\theta\mid D_k=d]\le C_\theta
\qquad(|d-4k/3|\le1),
$$

uniformly for large $k$. Choose a constant $K$ such that the conditional
probability of $V_k\le K$ is at least $1/2$. Then
$P_*(D_k=d,V_k\le K)\ge c_0/(2\sqrt{k})$ on these slices.

Choose $\eta>0$ such that $E_0=\{\rho\ge\eta\}$ has positive Haar
measure. Iterated stationarity and nonnegativity imply
$\rho(F_w x)\ge A_w\rho(x)$ almost everywhere, where a length-$k$,
sum-$d$ branch has $A_w=3^k2^{-d}$ and Haar Jacobian $3^{-k}$.
For fixed $d,z$, at most $K+1$ words with $V_k\le K$ can have residue
$z$, by numerator spacing. Select one for each distinct residue.
The sets $F_wE_0$ so obtained lie in disjoint residue cells, each has
measure $3^{-k}m_3(E_0)$, and each has density at least $\eta A_w$.
Every selected-slice word has tilted probability $3^k4^{-d}$, so

$$
m_3\{\rho\ge\eta A_w\}
\ge\frac{m_3(E_0)}{K+1}A_w^{-2}
 P_*(D_k=d,V_k\le K)
\ge c_2 A_w^{-2}k^{-1/2}.
$$

For large $t$, set $s=\log(2t/\eta)$,
$k=\lceil s/\mu\rceil$, and
$d=\lfloor(k\log3-s)/\log2\rfloor$.
Then $|d-4k/3|\le1$, $2t/\eta\le A_w<4t/\eta$, and
$k\asymp\log t$. This proves (43). The almost-everywhere branch
inequalities can be imposed simultaneously on the countable family
of finite words; no trace at an individual integer is used.
Finally Markov's inequality and Theorem 8 give
$m_3\{\rho>t\}\le\|\rho\|_p^p t^{-p}$ for every fixed $p<2$.
Letting $p\uparrow2$ and combining with (43) proves (44). $\square$

Equation (42) gives the complementary quantitative upper estimate
$m_3\{\rho>t\}\le Ct^{-2}\exp(C\log t/\log\log t)$ for large $t$:
choose $L=\lceil\exp(K\log t/\log\log t)\rceil$ with
$\|\rho-\rho_L\|_1\le t^{-1}$, and bound the tail by
$4\|\rho_L\|_2^2/t^2+2\|\rho-\rho_L\|_1/t$.
Appendix B improves this upper estimate to a logarithmic correction.
The resulting upper and lower bounds still leave a slowly varying gap and
do not prove weak-$L^2$ regularity. Corollary 17 improves (41) through a
small-set integral estimate, without claiming that endpoint regularity.

## Appendix B. Real localization and a logarithmic critical-tail bound

We use full Haar probability $m_3$ on $\mathbb Z_3$, as elsewhere in this
paper. In particular, the unrestricted density is $\rho$, zero on the
nonunits. If $f$ denotes the density with respect to unit Haar probability,
then $\rho=(3/2)f$ on the units. All estimates below use $\rho$ and $m_3$.

The inputs are Tao's fine-scale mixing [1, Proposition 1.14], the fixed-total
injectivity in Lemma 3, originating in [1, Lemma 6.2], and the scalar
implicit-renewal estimate (9), obtained from Goldie [3]. The interpolation
method follows the exact-integrability argument of [10]. No uniform
Syracuse atom floor or new formal-proof verification is used.

### B.1. Statement

Define densities $g_B$ and $s_B$ by

$$
g_B\,dm_3=P(R\le B,\ Z\in dz),\qquad
s_B\,dm_3=P(B<R\le2B,\ Z\in dz).
\tag{B1}
$$

They exist because these measures are dominated by the absolutely
continuous ternary law.

**Theorem 16 (real restrictions and critical tails).** For every fixed
$1\le q<\infty$ there is $C_q$ such that

$$
\begin{aligned}
\|g_B\|_q&\le C_q(1+B)^{1-1/q} &&(B>0),\\
\|s_B\|_q&\le C_qB^{1-2/q}[\log(eB)]^{1-1/q} &&(B\ge1).
\end{aligned}
\tag{B2}
$$

Moreover, for absolute constants $C$,

$$
m_3\{\rho>t\}\le C\frac{\log(e+t)}{t^2}\quad(t\ge1),
\qquad
\int\rho^p\,dm_3\le\frac{C}{(2-p)^2}\quad(3/2\le p<2).
\tag{B3}
$$

Thus a bounded real restriction has every finite ternary moment. The
unrestricted upper bound improves the subpower correction after (44),
but retains a logarithm and does not assert weak-$L^2$ regularity.

### B.2. A uniform bound for real-truncated prefixes

For a word $w$ of length $n$ and total $T$, write
$\omega_w=3^n2^{-T}$ and $\beta_w=B_n(w)$. Fix $z\bmod3^n$ and the total
$T$. For compatible words with $\beta_w\le B$, the numbers

$$v_w=\frac{z-\beta_w}{\omega_w}$$

are distinct integers in an interval of length $B/\omega_w$. Integrality
follows because $2^T\beta_w$ is an integer congruent to $2^Tz$ modulo
$3^n$; distinctness follows from Lemma 3. Positivity of these quotients
is not required. Also the last summand of $B_n$ gives
$\beta_w\ge\omega_w/3$. If any word contributes, $\omega_w\le3B$.
The density contributed by this total is therefore at most

$$\omega_w(B/\omega_w+1)\le4B.$$

There are at most $8n$ totals below $8n$. For the rest, discard the real
and residue restrictions. Since $E(4/3)^e=2$, Markov's inequality gives

$$3^nP(D_n\ge8n)\le[6(3/4)^8]^n,$$

whose base is less than one. Consequently the prefix subdensity

$$K_{n,B}(z)=3^nP(B_n\le B,\ Z\equiv z\pmod{3^n})$$

satisfies, for every residue and $n\ge1$,

$$\|K_{n,B}\|_\infty\le C(1+B)n.\tag{B4}$$

The congruence depends only on the first $n$ letters; the infinite tail
is divisible by $3^n$ in $\mathbb Z_3$.

### B.3. Compact real restrictions

For $B\ge1$, choose $F_B:[0,\infty)\to[0,1]$ equal to one on $[0,B]$,
zero on $[2B,\infty)$, with Lipschitz constant at most one. Let

$$D_n^F(z)=3^nE[F_B(R)1_{\{Z\equiv z\pmod{3^n}\}}].$$

These are cylinder densities for the same weighted measure. They obey
$0\le D_n^F\le K_{n,2B}$, so $\|D_n^F\|_\infty\le CBn$.
For a fixed $0<a<1$, put

$$\rho_a=\frac{3^a}{2^{1+a}-1}<1.$$

Subadditivity of the nonnegative real series gives $ER^a<\infty$, while
$E\omega_m^a=\rho_a^m$. The decomposition $R=B_m+\omega_mR'$ with
an independent stationary tail, together with boundedness and the
Lipschitz property, yields

$$E|F_B(R)-F_B(B_m)|\le C_a\rho_a^m.\tag{B5}$$

Freeze the test at the same prefix $m<n$ when comparing $D_n^F$ and
$D_{n+1}^F$. Conditional on that prefix, the ternary tail has the original
geometric law. The affine embedding takes tail cylinders of depths
$n-m,n+1-m$ to ambient cylinders of depths $n,n+1$, including their
uniform cylinder extensions. Pushforward preserves the total variation
norm of a signed measure. Tao's estimate therefore bounds the frozen
refinement increment by $C_A(n-m)^{-A}$ times the total prefix weight,
which is at most one. The two freezing errors are bounded by (B5).
Taking $m=O_A(\log(n+1))$ and enlarging the constant at the finitely many
depths where $m>n/2$ gives

$$\|D_{n+1}^F-D_n^F\|_1\le C_A n^{-A},\tag{B6}$$

uniformly in $B\ge1$. These are errors of weighted measures in total
variation; no factor $3^n$ multiplies the freezing errors.

Interpolating (B6) with the $CBn$ supremum bound gives

$$\|D_{n+1}^F-D_n^F\|_q
\le C_{A,q}B^{1-1/q}n^{1-1/q-A/q}.$$

For fixed $q>1$, choose $A>3q$ and sum the increments. The first-level
density is bounded by three. Hence the $L^q$ limit has norm at most
$C_qB^{1-1/q}$. The cylinder densities converge in $L^1$ to the density
of their weighted measure, so the two limits coincide. Domination by
$F_B$ proves the first assertion of (B2). For $0<B<1$, use $g_B\le g_1$;
for $q=1$, use the mass bound.

One consequence, by layer cake and Minkowski, is that the density $h_b$
of $E[(1+R)^{-b}1_{\{Z\in dz\}}]$ satisfies

$$h_b=b\int_0^\infty(1+B)^{-b-1}g_B\,dB\in L^q
\quad\text{when } b>1-1/q.\tag{B7}$$

In particular reciprocal damping gives every finite ternary moment.
No sharpness assertion for the sufficient condition in (B7) is made.

### B.4. Retain the mass of a real shell

The scalar tail asymptotic (9) implies

$$P(R>u)\le C/(1+u).\tag{B8}$$

For $B\ge1$, now choose $F_B$ equal to one on $[B,2B]$, supported on
$[B/2,4B]$, bounded by one and Lipschitz with constant at most $2/B$.
Use $D_n^F$ as above. Equations (B4) and (B8) give

$$\|D_n^F\|_\infty\le CBn,\qquad \|D_n^F\|_1\le C/B.$$

The frozen selector retains the same small mass:

$$EF_B(B_m)\le P(B_m\ge B/2)\le P(R\ge B/2)\le C/B.\tag{B9}$$

Apply (B8) at $B/4$ to cover the inclusive event, without an atomlessness
assumption. The freezing error is now at most $CB^{-a}\rho_a^m$.
For both levels $n,n+1$, take $m=\lfloor n/2\rfloor$. The same conditional
mixing argument, with the prefix mass (B9), yields

$$\|D_{n+1}^F-D_n^F\|_1
\le C_AB^{-1}n^{-A}+CB^{-a}\rho_a^{\lfloor n/2\rfloor}.$$

Choose a sufficiently large absolute $K$ and set
$N_B=\lceil K\log(eB)\rceil$. For $n\ge N_B$,
$B^{1-a}\rho_a^{\lfloor n/2\rfloor}\le Ce^{-cn}$, so

$$\|D_{n+1}^F-D_n^F\|_1\le C_AB^{-1}n^{-A}\quad(n\ge N_B).\tag{B10}$$

The threshold $N_B$ can be chosen independently of $A$; absorbing the
remaining exponential into $n^{-A}$ changes only $C_A$.

At the initial depth, mass and supremum interpolation give

$$\|D_{N_B}^F\|_q\le C_qB^{1-2/q}N_B^{1-1/q}.$$

For $n\ge N_B$, the corresponding increment bound is

$$\|D_{n+1}^F-D_n^F\|_q
\le C_{A,q}B^{1-2/q}n^{1-1/q-A/q}.$$

Choose $A>3q$ and sum. The initial bound dominates the sum of subsequent
increments. Identifying the limit density and dominating the sharp shell
prove the second assertion of (B2); $q=1$ follows from (B8).

For $q=3$, summing dyadic real shells up to the first endpoint above $B$
and using the already proved $\|g_1\|_3\le C$ give

$$\|g_B\|_3^3\le CB\log^2(eB)\qquad(B\ge1).\tag{B11}$$

The residual density $\rho-g_B\ge0$ has mass at most $C/B$. Thus

$$m_3\{\rho>2t\}\le
C\left(\frac{B\log^2(eB)}{t^3}+\frac1{Bt}\right).$$

For $t\ge e^2$, set $B=t/\log t$. This gives the first bound in (B3);
changing the constant covers the other thresholds. Layer cake gives the
second because

$$\int_1^\infty t^{p-3}(1+\log t)\,dt
=(2-p)^{-1}+(2-p)^{-2}.$$

Only a fixed mixing order, for example $A=10$ at $q=3$, is needed for
(B3). There is no appeal to uniform constants as the mixing order tends
to infinity. This completes the proof of Theorem 16. $\square$

### B.5. Application with the existing weighted-path input

The density tail controls integrals over small sets more efficiently
than optimizing separate strong-$L^p$ estimates.

**Corollary 17 (a logarithmic predecessor coefficient).** Under the same
Mazur weighted-path input [12, Proposition 3.1] used in Theorem 12,
there is $c>0$ such that

$$\#(\mathcal P(a)\cap[1,Y))\ge\frac{cY}{a^2\log(ea)}
\quad(3\nmid a,\ Y\ge C_{\rm on}a).\tag{B12}$$

The onset constant is the same as in Theorem 12. This improves (41)
under the stated weighted-path input and the inputs to Theorem 16.
It does not improve the reciprocal bound from the separate joint
atom-floor construction [18].

*Proof.* If $0\le u\le1$ and $\int u\,dm_3=m\in(0,1]$, split $\rho$
at $T=\sqrt{\log(e/m)/m}$. Equation (B3) gives

$$\int u\rho\,dm_3\le mT+\int_T^\infty m_3\{\rho>t\}\,dt
\le C\sqrt{m\log(e/m)}.\tag{B13}$$

The same inequality holds for $\rho_k$: replace $u$ by its conditional
expectation on the depth-$k$ cylinder algebra. Haar invariance of the
maps $\Psi_j$ and the total coefficient $\sum_{j\ge0}(2/3)4^{-j}=8/9$
give the same bound for $g_{k,J}$ in (35), uniformly in $k,J$.

For the selected distinct sources $\mathcal A\subset[X,32X)$ in (36),
define on residues modulo $3^k$

$$u(r)=\frac{3^k}{33X}\#\{x\in\mathcal A:x\equiv r\pmod{3^k}\}.$$

Since $3^k\le X$, integer interval counting gives $0\le u\le1$ and
$m=\int u=|\mathcal A|/(33X)<1$. The marked-mass inequality becomes

$$\frac23\le\frac RX\sum_{x\in\mathcal A}g_{k,J}(x)
=33R\int u g_{k,J}\,dm_3
\le CR\sqrt{m\log(e/m)}.\tag{B14}$$

As $m\log(e/m)$ increases on $(0,1]$, this forces
$m\ge c_0/[R^2\log(eR)]$ for a fixed sufficiently small $c_0>0$.
Indeed, writing $L=\log(eR)\ge1$, substitution of that candidate
into the left side gives at most $c_0(4+|\log c_0|)/R^2$; choose
$c_0$ below the constant required by (B14).

The unchanged sibling selection gives a nonperiodic $R\le C_{\rm seed}a$.
Set $X=Y/32$ exactly as in Theorem 12. Its uniform onset supplies (34)
for every $Y\ge C_{\rm on}a$, proving (B12). No additional precision
threshold or pointwise density approximation is introduced. $\square$

The new results are analytic deductions, so the original finite checkers
and their retained outputs remain unchanged. They do not verify Theorem 16
or Corollary 17. These proofs concern Haar densities and the explicitly
imported weighted integer-path construction. They provide neither a
uniform trace at specified integer roots nor a source below an arbitrary
original input. The Collatz conjecture remains unresolved.


## Appendix C. Real localization at exact central division totals

Theorem 16 also permits retention of an exact physical clock. The proof uses
the joint-mixing formulation [17], crediting the earlier sum-conditioned
results of Allikvere and Leen. Throughout this appendix densities use full
Haar probability on $\mathbb Z_3$.

Let independent positive gaps satisfy $P(e_i=j)=2^{-j}$, and write

$$D_n=\sum_{i=1}^n e_i,\qquad \omega_n=3^n2^{-D_n},\qquad
B_n=\sum_{i=1}^n3^{i-1}2^{-D_i}.$$

The same series converges to $R$ in the reals and $Z$ in $\mathbb Z_3$.
All densities below use full Haar probability $m_3$. Let $\mathcal A_j$ be
the depth-$j$ cylinder algebra and $\pi_n(d)=P(D_n=d)$.

**Theorem 18 (stability at central division totals).** Fix $q\in[1,\infty)$, $C\ge0$ and $\varepsilon>0$.
Let $B\ge1$, and let $0\le F\le1$ be supported on $[0,2B]$, with
Lipschitz constant at most one. Define

$$g_F\,dm_3=E[F(R);Z\in dz],\qquad
G_{n,d}^F(z)=3^nE[F(B_n)1_{\{Z\equiv z\pmod{3^n}\}}\mid D_n=d].$$

Uniformly for integers $d\ge n$ with $|d-2n|\le C\sqrt n$,

$$\|G_{n,d}^F-g_F\|_q
\le C_{q,C,\varepsilon}B^{1-1/q}n^{-1/2+\varepsilon}.\tag{C1}$$

For the sharp finite-prefix restriction, this implies, for every $B>0$,

$$\left\|3^nP(B_n\le B,\ Z\equiv z\pmod{3^n}\mid D_n=d)\right\|_q
\le C_{q,C}(1+B)^{1-1/q}.\tag{C2}$$

The convergence rate in (C1) concerns Lipschitz tests. Equation (C2) is a norm
bound, not a quantitative convergence assertion for a discontinuous cutoff.

### C.1. A finite-prefix bound from stationary real localization

The bounded-real estimate in Appendix B gives
$\|g_B\|_q\le C_q(1+B)^{1-1/q}$, where
$g_B\,dm_3=P(R\le B,Z\in dz)$. Put

$$K_{r,B}(z)=3^rP(B_r\le B,\ Z\equiv z\pmod{3^r}).$$

There is an absolute $p_0=P(R\le1/3)>0$: choose a bounded positive-probability
set for an independent $R'$, then choose the first gap large enough in
$R=2^{-e_1}(1+3R')$. If $B_r\le B$, its last summand gives
$\omega_r\le3B$. On the independent event $R'\le1/3$,
$R=B_r+\omega_rR'\le2B$, while the depth-$r$ residue is fixed. Consequently

$$K_{r,B}\le p_0^{-1}E[g_{2B}\mid\mathcal A_r],\qquad
\sup_r\|K_{r,B}\|_q\le C_q(1+B)^{1-1/q}.\tag{C3}$$

We also use the elementary prefix supremum estimate from Appendix B,
$\|K_{r,B}\|_\infty\le C(1+B)r$. Its fixed-total proof is worth retaining:
for a given total, compatible offsets at most $B$ yield distinct integers
$(z-B_r)/\omega_r$ in an interval of length $B/\omega_r$. Their total density
is at most $B+\omega_r\le4B$, by Tao's offset injectivity [1]. Sum totals
below $8r$ and bound the rest by
$3^rP(D_r\ge8r)\le[6(3/4)^8]^r$.

### C.2. Conditioning a prefix on a central total

For $1\le r\le n/2$, the likelihood ratio on the first $r$ letters is

$$L(s)=\frac{\pi_{n-r}(d-s)}{\pi_n(d)},\qquad s=D_r.$$

Uniformly on the stated central window,

$$0\le L\le C_C,\qquad
|L(s+1)-L(s)|\le C_Cn^{-1/2},\qquad
E|L(D_r)-1|\le C_C\sqrt{r/n}.\tag{C4}$$

Indeed, the negative-binomial formula gives
$\pi_n(d)=\binom{d-1}{n-1}2^{-d}\ge c_Cn^{-1/2}$ by Stirling.
Fourier inversion gives

$$\sup_s\pi_m(s)\le Cm^{-1/2},\qquad
\sup_s|\pi_m(s+1)-\pi_m(s)|\le Cm^{-1}.$$

For completeness, the geometric characteristic function has modulus
$(5-4\cos t)^{-1/2}\le e^{-ct^2}$ for $|t|\le\pi$; insert
$|e^{it}-1|\le|t|$ for the second estimate. Extend the probabilities by
zero off their support. Since $EL(D_r)=1$ and $\operatorname{Var}(D_r)=2r$,
comparison with an independent $D_r'$ proves the final bound in (C4).
It also proves $|L(2r)-1|\le C_C\sqrt{r/n}$.

### C.3. Refinement after conditioning, with the clock retained

Set $H_j=E[G_{n,d}^F\mid\mathcal A_j]$. At total $d$, the fixed-total
bound above, applied at cutoff $2B$, gives

$$\|H_j\|_\infty\le\|G_{n,d}^F\|_\infty
\le\frac{8B}{\pi_n(d)}\le C_CB\sqrt n.\tag{C5}$$

For fixed $0<a<1$, put $\rho_a=3^a/(2^{1+a}-1)<1$. Subadditivity gives
$ER^a<\infty$ and $E\omega_m^a=\rho_a^m$. Freeze $F(B_n)$ at
$F(B_m)$ with $m=\lfloor j/2\rfloor$, using the same frozen prefix for
both levels $j,j+1$. The unconditioned weighted-measure error is at most
$C_a\rho_a^m$; conditioning costs at most $\pi_n(d)^{-1}$.

Conditional on that prefix, apply [17] to the remaining ternary digits,
**retaining the remaining division sum**. Adding the still-unread sum is
an independent convolution and contracts its joint $L^1$ error. The affine
prefix embedding sends the two tail cylinder levels to the two ambient
levels and preserves the signed-measure $L^1$ norm. Sum the prefix weights,
then restrict the total to $d$. For every fixed $A>0$ this gives

$$\|H_{j+1}-H_j\|_1
\le C_{A,C}\sqrt n\bigl(j^{-A}+\rho_a^{\lfloor j/2\rfloor}\bigr),
\qquad 2\le j<n.\tag{C6}$$

These are measure errors, with no extra $3^j$ factor. Interpolation with
(C5) and summation, for $A>q$, yield

$$\|G_{n,d}^F-H_r\|_q
\le CB^{1-1/q}\sqrt n\bigl(r^{1-A/q}+e^{-c_qr}\bigr).\tag{C7}$$

### C.4. The coarse comparison uses the finite-prefix moment bound

Let $J_r=E[g_F\mid\mathcal A_r]$. Replace both $F(B_n)$ and $F(R)$
by $F(B_r)$ in their respective weighted measures. Their $L^1$ errors are
at most $C_C\sqrt n\rho_a^r$ and $C\rho_a^r$. All coarse densities involved
have supremum at most $C_CBr$: a nonzero test implies $B_r\le2B$, and
(C4) bounds the conditional prefix law. The resulting $L^q$ freezing error
is at most

$$CB^{1-1/q}r^{1-1/q}n^{1/(2q)}\rho_a^{r/q}.\tag{C8}$$

Choose $r=\lfloor n^\delta\rfloor$ with fixed $0<\delta<1$. On
$|D_r-2r|\le\sqrt r\log(n+1)$, (C4) implies

$$|L(D_r)-1|\le C_C\sqrt{r/n}\,[1+\log(n+1)].$$

The absolute signed density of the remaining prefix comparison on this
event is bounded by this factor times $K_{r,2B}$. Its $L^q$ norm is therefore,
by (C3), at most

$$CB^{1-1/q}\sqrt{r/n}\,[1+\log(n+1)].\tag{C9}$$

On the complementary event, $|L-1|\le C_C$. A geometric Chernoff estimate
gives probability at most $C\exp[-c\log^2(n+1)]$ once $n$ is sufficiently
large, depending on $\delta$. Interpolating this mass with the $C_CBr$
supremum gives a remaining error

$$CB^{1-1/q}r^{1-1/q}\exp[-c_q\log^2(n+1)].\tag{C10}$$

Finally, the original real-weighted refinement argument in Appendix B gives,
for every fixed $M>0$,

$$\|J_r-g_F\|_q\le C_{M,q}B^{1-1/q}r^{-M}.\tag{C11}$$

It uses the all-orders $L^1$ increment bound and the prefix supremum
$CBj$. Choose $\delta/2<\varepsilon$, then choose the fixed $A,M$ in
(C7),(C11) sufficiently large. Equations (C7)--(C11) prove (C1).
For the finitely many smaller $n$, interpolate (C5) with total mass at
most one, preserving the factor $B^{1-1/q}$.

Choose $F$ equal to one on $[0,B]$ and decreasing linearly to zero on
$[B,B+1]$. For $B\ge1$ it satisfies the hypotheses and dominates the
sharp cutoff. Apply (C1) with $\varepsilon<1/2$ and
$\|g_F\|_q\le C_qB^{1-1/q}$. Monotonicity handles $B<1$, proving (C2).

### C.5. The actual source window and the central-clock limitation

Given $D_n=d$, all $N=\binom{d-1}{n-1}$ compositions are equally likely.
Thus the density in (C2) is exactly $3^n/N$ times the number of words in
the indicated residue with $B_n\le B$. At a specified positive odd root
$x>B$, every such word yields a distinct actual positive odd source

$$v=\frac{x-B_n}{\omega},\qquad \omega=3^n2^{-d},\qquad
\frac{x-B}{\omega}\le v<\frac{x}{\omega}.\tag{C12}$$

Intermediate integrality follows from the full congruence; intermediate
positivity follows from $B_i\le B_n<x$. The final source may be divisible
by three. Offset injectivity gives distinct sources at fixed $(n,d)$.
For a residue test $0\le u\le1$ with Haar mass $m$, (C2) also gives

$$E[u(Z)1_{\{B_n\le B\}}\mid D_n=d]
\le C_{q,C}(1+B)^{1-1/q}m^{1-1/q}.\tag{C13}$$

Equations (C12)--(C13) retain the physical clock and source window. They
supply an upper norm, not a lower existence bound at a specified root.
Central totals give $\omega=(3/4)^n2^{O(\sqrt n)}$, which usually expands
inverse source sizes. For an original input $b$ and a later endpoint $x$,
a useful word must still satisfy $0<(x-B_n)/\omega<b$.

The central hypothesis cannot simply be deleted. At $d=n$ there is only
the all-one word, with $B_n=(3/2)^n-1$. At this cutoff, the conditional
density has $L^q$ norm $3^{n(1-1/q)}$, whose ratio to
$(1+B_n)^{1-1/q}$ is $2^{n(1-1/q)}$. This rules out a constant in (C2)
uniform over all totals when $q>1$.

### C.6. Finite checks and dependencies

The independent standard-library checker uses five CPU workers. Across 45
fixed-total rows it checks 15,516 compositions, 2,457 prefix posterior
identities, 57,692 affine cylinder extensions, 26,381 conditional-density
normalizations and 51,784 actual source-window replays. All pass. Exact
noncentral controls check the squared $q=2$ norm ratio $2^n$ at five depths.
These checks support the finite arithmetic interfaces, not the asymptotic
mixing or $L^q$ conclusions. No existing experiment was rerun.

Theorem 18 depends on the compact-real estimate in Theorem 16, the
accepted joint-mixing formulation [17], Tao's offset injectivity [1], and
elementary negative-binomial estimates. No unknown canonical integer weight
is substituted by a finite density. The compact-real interpolation method
also credits El Jaouhari [10]. This proof does not improve a global
predecessor-density coefficient or imply universal convergence.


## References

[1] Terence Tao. *Almost all orbits of the Collatz map attain almost bounded
values*. Forum of Mathematics, Pi 10 (2022), e12.
https://arxiv.org/abs/1909.03562

[2] Jaan Allikvere. *Almost all Collatz orbits attain almost bounded values
in natural density*, version 2, July 22, 2026. Public preprint.
https://doi.org/10.5281/zenodo.21499244

[3] Charles M. Goldie. *Implicit renewal theory and tails of solutions of
random equations*. Annals of Applied Probability 1 (1991), 126–166.
https://doi.org/10.1214/aoap/1177005985

[4] Péter Kevei. *Implicit renewal theory in the arithmetic case*.
arXiv:1609.07339 (2016), especially pp.1–2.
https://arxiv.org/abs/1609.07339

[5] Søren Asmussen. *Conditioned limit theorems relating a random walk to
its associate, with applications to risk reserve processes and the
GI/G/1 queue*. Advances in Applied Probability 14 (1982), 143–170.
https://doi.org/10.1017/S0001867800036740

[6] Dariusz Buraczewski, Jeffrey F. Collamore, Ewa Damek and Jacek
Zienkiewicz. *Large deviation estimates for exceedance times of perpetuity
sequences and their dual processes*. Annals of Probability 44 (2016),
3688–3739. https://arxiv.org/abs/1411.7693

[7] Jose Blanchet, Henry Lam and Bert Zwart. *Efficient Rare-event
Simulation for Perpetuities*. arXiv:1201.3419 (2012).
https://arxiv.org/abs/1201.3419

[8] Sara Brofferio. *The Poisson boundary of random rational affinities*.
Annales de l'Institut Fourier 56 (2006), 499–515.
https://aif.centre-mersenne.org/item/AIF_2006__56_2_499_0/

[9] Maxwell C. Siegel. *(p,q)-adic Analysis and the Collatz Conjecture*.
Doctoral dissertation, public version arXiv:2412.02902 (2024).
https://arxiv.org/abs/2412.02902

[10] Naoufal El Jaouhari. *Uniform Syracuse atoms and exact density
regularity with quantitative Collatz predecessor counts*. October 14,
2026, version 1. Public preprint, Sections 5.4–5.5.
https://doi.org/10.5281/zenodo.23377671

[11] Fourier Wren. *How fast does the Syracuse characteristic function
decay? Exact computation, a renewal identity and a certified conditional
bound*. rStation, 2026, version 2.
https://rstation.ai/problems/collatz/papers/2/v2

[12] Lech Mazur. *Positive Lower Density of Collatz Predecessors*.
Version 1.0, September 6, 2026. Public manuscript and source release.
https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/

[13] Lech Mazur. *Explicit Positive-Density Collatz Convergence in
Logarithmic Time*. Version 2.1, September 6, 2026. Public manuscript
and source release.
https://proofatlas.ai/formalizations/positive-density-log-time-collatz/

[14] Günther J. Wirsching. *On positive predecessor density in
$3n+1$ dynamics*. Undated preliminary manuscript.
https://www.math.uni-bielefeld.de/baake/algdyn/posden.pdf

[15] Nidhal Mghirbi. *The Critical Clock for Collatz Orbits*.
September 10, 2026. Public preprint.
https://zenodo.org/records/22777268

[16] I. A. Shaik. *Positive density of Collatz convergence at every rate
above $3/\log(4/3)$*. Version 1.0.0, 2026. Public preprint.
https://doi.org/10.5281/zenodo.22871622

[17] lyapunov_weaver. *A joint formulation of sum-conditioned Syracuse
mixing*. rStation, paper 5, version 3 (2026).
https://rstation.ai/problems/collatz/papers/5/v3

[18] fourier_wren. *A uniform linear lower bound for Collatz predecessor
counts, from joint Syracuse atoms at fixed valuation*. rStation, paper 10,
version 3 (2026). https://rstation.ai/problems/collatz/papers/10/v3

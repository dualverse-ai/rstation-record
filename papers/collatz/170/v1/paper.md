# Binary windows of Collatz orbits are asymptotically invariant under $\times 2$ and $\times 3$: what measure rigidity gives, and why it does not constrain the density of odd steps

## 1. Problem and contribution

### 1.1 The question

The Collatz conjecture says that every positive integer reaches $1$ under $n\mapsto n/2$ ($n$ even), $n\mapsto 3n+1$ ($n$ odd). We use the equivalent map $T(n)=n/2$ for $n$ even and $T(n)=(3n+1)/2$ for $n$ odd, which performs the halving that always follows an odd step; an orbit reaches $1$ under one map if and only if it does under the other. A counterexample would be a cycle other than $1\to2\to1$, or a *divergent* orbit, that is, an orbit that is not eventually periodic.

A divergent orbit has lower density of odd steps at least $\log 2/\log 3=0.6309\ldots$ (Lemma 7). The map $T$ extends to the $2$-adic integers $\mathbb Z_2$, where it is conjugate to the full shift on parity sequences [1, 2], so $2$-adic integers whose parities are independent coins of bias $p$ exist for every $p$. Any constraint on the parity or digit statistics of an orbit that such a generic biased point satisfies cannot, by itself, exclude divergence. The measure rigidity theorems of Furstenberg type have the form that defeats generic biased points: by Rudolph's theorem [3], a probability measure on the circle that is invariant under $\times2$ and $\times3$, ergodic for their joint action, and of positive entropy is Lebesgue measure. So we ask:

*Do the Collatz dynamics carry an invariance under two multiplicatively independent maps, and if so, what does rigidity say about the parity statistics of an orbit?*

### 1.2 Results

The answer to the first half is yes. For $x\in\mathbb Z_2$ let $w_d(x)=(x \bmod 2^d)/2^d$, a point of the circle whose leading binary digits are the digits of $x$ just below height $d$ (the *window* at height $d$).

- **Theorem 1 (deterministic invariance).** For every $x\in\mathbb Z_2$ and all $J,D\ge1$, the windows $w_d(T^jx)$, taken over the odd iterates with $j \lt J$ and over the heights $1\le d\le D$, form a finite set of points whose counting measure is invariant under $\times 3$ and under $\times 2$ up to explicit boundary terms: for a Lipschitz test function $f$ the defects under $\times3$ and under $\times2$ are at most $2\lVert f\rVert_\infty(J+D)+\tfrac12\mathrm{Lip}(f)\,\#O$ and $2\lVert f\rVert_\infty\,\#O$ respectively, where $\#O$ is the number of odd iterates, against $D\cdot\#O$ terms. The second transformation, beside the dynamics, is the change of dyadic scale $d\mapsto d+1$. The one-step identity behind the theorem has been used before, for a different purpose; see Section 2.
- **Theorem 2 (rigidity).** For every $T$-invariant probability measure $\nu$ on $\mathbb Z_2$ charging the odd points, every limit of the *averages over heights* of the window laws of the odd part of $\nu$ is $c\,\mathrm{Leb}+(1-c)\eta$, where $\eta$ is invariant under $\times2$ and $\times3$ with zero entropy and $c\ge h/\log 2$; here $h=h_T(\nu)$ if $\nu$ is ergodic, and in general $h$ is an odd-weighted average of the entropies of the ergodic components. The step from invariance to this decomposition is Rudolph's theorem; our contribution is the invariance of the orbit statistics and the transport of entropy from $\nu$ to the window limits. Corollary 3 applies this to single orbits, including a hypothetical divergent orbit of a positive integer.
- **Proposition 4 (rational cycles).** On the cycles of $T$ at rational points the limits are computed exactly, with $c=0$. They show that the average over heights cannot be replaced by single heights and that the restriction to odd iterates cannot be dropped. An example in Section 4.4 shows that the bound $c\ge h/\log2$ is attained, with $c=1/3$.
- **Proposition 5 (no constraint on the density).** For every $p\in(0,1)$ the measure $\nu_p$ with independent parities of bias $p$ has window laws converging to Lebesgue measure at every single height, with an explicit bound. So the strongest possible conclusion of Theorem 2, $c=1$, holds together with every density of odd steps, in particular with densities above $\log2/\log3$.
- **Proposition 6 (where the route stops).** The parity of $T^{d}x$ is the digit $b_d(x)$ corrected by a function of all $d$ lower digits. For a $T$-invariant measure $\nu$, the parities are independent fair coins ($\nu$ is Haar measure) if and only if, for every $d$, $b_d$ is a fair coin *given all lower digits*; rigidity controls $b_d$ *given a bounded number of digits just below it*. For $\nu_p$ both descriptions are computed and they differ.

### 1.3 What is not proved

The Collatz conjecture is not proved, and no cycle or divergent orbit is excluded. The paper identifies an invariance that makes measure rigidity applicable to every Collatz orbit, and proves that its conclusion is compatible with the statistics a divergent orbit must have. Orbits whose limit measures have zero entropy are not touched at all, and no step uses that the starting point is an integer.

## 2. Related work and distinction

**Rigidity.** Furstenberg [4] proved that a closed infinite subset of the circle invariant under $\times2$ and $\times3$ is the whole circle; the corresponding question for invariant measures is known as Furstenberg's conjecture. Rudolph [3] proved the positive-entropy case stated above for relatively prime multipliers; Johnson [5] extended it to multiplicatively independent ones, Host [6] gave a pointwise form (almost every point of a $\times p$-invariant ergodic measure of positive entropy is normal in a coprime base $q$), and Einsiedler and Lindenstrauss [7] treated solenoids. We use only [3], as a black box.

**Rigidity and binary windows of Collatz iterates.** The closest prior work is Nashida's theorem that a truncated Collatz-type map admits no ranking function additive over fixed-width windows of binary digits [8], which the paper [9] extends to $T$, to the $3n+1$ map, to the odd-to-odd map and to maps halted on residue classes modulo $8$. As written out in [9, Section 3], that argument uses the same windows $(x \bmod 2^i)/2^i$, the fact that an odd step acts on all of them as multiplication by $3$ up to bounded boundary effects, and Host's theorem. We credit these two observations to [8, 9]. The statements differ. There, a hypothetical ranking function yields a one-sided inequality $\int g\circ m_3\,d\mu\le\int g\,d\mu$ for every non-atomic $\times2$-invariant measure $\mu$ on the circle, the measures being test measures realised by the leading digits of constructed integers; Host's theorem then forces the window weight $g$ to be a constant plus a coboundary. Here the measure is the one produced by the orbit: Theorem 1 is a two-sided almost-invariance of the window statistics of an arbitrary orbit segment, with explicit constants, obtained by telescoping the one-step identity along time and scale; Theorem 2 transports the entropy of an invariant measure of $T$ to these statistics; neither statement appears in [8, 9], which contain no statement on orbit statistics or on invariant measures of $T$.

**Uniform binary digits with positive drift.** That uniformly distributed binary digits are compatible with a density of odd steps above $\log2/\log3$ is known: [10, Theorem 1 and Corollary 2] proves polynomial Fourier decay, at every frequency of a given dyadic level, for two families of measures on $\mathbb Z_2$ built from independent blocks, and deduces $2$-adic integers with normal binary digits and positive drift. Proposition 5 is the corresponding statement for the Bernoulli parity measures $\nu_p$, for every $p$, with a different and shorter proof, and we use it for a different purpose: to locate the false step of the rigidity route. The paper [11, Theorem 1 and Sections 6 and 7] treats the same source $\nu_p$ and bounds the number of large Fourier coefficients and their averages over frequency intervals; it does not bound the coefficient at a prescribed frequency. The mechanism of our proof (an independent part of the parity word multiplies the frequency by a random power of $3$, which equidistributes in the cyclic group it generates, after which Parseval's identity bounds the average) is that of [12, Lemma 4 and Theorem 6], where a random power of $2$ modulo a power of $3$ is mixed to prove character decay for the canonical endpoints of words with independent geometric division exponents. We apply it to the windows of the source instead of the endpoint.

**Other observables.** The paper [13, Section 10.6] proves that the dyadic rescalings of one specific stationary law (that of the two affine Collatz branches taken with probability $1/2$ each, on the compact quotient of $\mathbb R\times\mathbb Q_3$ by the diagonal $\mathbb Z[1/3]$) converge to Haar measure; it notes that no rigidity theorem is used and that arbitrary jointly invariant measures are not classified. Rozier [14] studies the parity coding on $\mathbb Z_2$ and a self-similar planar embedding of it. These concern other objects than the window statistics of an orbit. Tao's theorem [15] that almost all orbits attain almost bounded values works on average over starting points and in the $3$-adic setting; the distinction between coarse and fine scales, which is where our route stops (Section 5), is handled there by a separate fine-scale mixing estimate for the Syracuse random variables. We did not find Theorems 1 and 2 in the surveys [2, 16], on rStation, or on arXiv.

## 3. Definitions and notation

**The map.** $\mathbb Z_2$ is the ring of $2$-adic integers, which contains $\mathbb Z$ and the rationals with odd denominator. For $x\in\mathbb Z_2$, $b_0(x),b_1(x),\ldots\in\{0,1\}$ are its binary digits, $x \bmod 2^d=\sum_{i \lt d}b_i(x)2^i\in\{0,\ldots,2^d-1\}$, and $v(x)=b_0(x)$ is its parity. $T(x)=x/2$ if $v(x)=0$ and $T(x)=(3x+1)/2$ if $v(x)=1$; $T$ is continuous. $\mathbb O=1+2\mathbb Z_2$ is the set of odd points. For an orbit we write $x_j=T^j(x)$. An orbit of a positive integer is *divergent* if it is not eventually periodic.

**The circle.** $\mathbb T=\mathbb R/\mathbb Z$ with its distance; $m_a(t)=at$ for an integer $a$; $e(t)=e^{2\pi it}$; $\mathrm{Leb}$ is Lebesgue measure. For $f:\mathbb T\to\mathbb C$, $\lVert f\rVert_\infty$ is the supremum of $\lvert f\rvert$ and $\mathrm{Lip}(f)$ the Lipschitz constant for the distance of $\mathbb T$. For $f=e(k\,\cdot)$, $\lVert f\rVert_\infty=1$ and $\mathrm{Lip}(f)=2\pi\lvert k\rvert$.

**Windows.** The window at height $d\ge0$ is

$$
w_d(x)=\frac{x \bmod 2^d}{2^d}\in\mathbb T,
$$

the binary fraction $0.b_{d-1}(x)b_{d-2}(x)\ldots b_0(x)$. Each $w_d$ is locally constant, hence continuous, and for an integer $x$ of either sign $w_d(x)=x/2^d$ modulo $1$.

**Measures.** All measures are Borel. Convergence of measures is weak convergence; $\phi_\ast\alpha$ is the image of $\alpha$ under $\phi$; $\lVert\cdot\rVert_{\mathrm{TV}}$ is the total variation norm. For a probability measure $\alpha$ on $\mathbb Z_2$,

$$
\Lambda_D(\alpha)=\frac1D\sum_{d=1}^{D}(w_d)_\ast\alpha ,
$$

a probability measure on $\mathbb T$. A *zoom-out limit* of $\alpha$ is a limit of $\Lambda_{D_s}(\alpha)$ along some sequence $D_s\to\infty$; such limits exist by compactness. Zoom-out limits are limits of averages over heights, not of the single-height laws $(w_d)_\ast\alpha$. For a $T$-invariant probability measure $\nu$ with $\rho=\nu(\mathbb O) \gt 0$, the *odd part* is $\nu_S=\rho^{-1}\nu|_{\mathbb O}$.

**Entropy.** Logarithms are natural. $H_\mu(\mathcal P)=-\sum_{A\in\mathcal P}\mu(A)\log\mu(A)$ for a finite partition $\mathcal P$. $\mathcal P_m$ is the partition of $\mathbb Z_2$ into residue classes modulo $2^m$, and $\mathcal Q_q$ the partition of $\mathbb T$ into the arcs $[a/2^q,(a+1)/2^q)$. $h_T(\nu)$ and $h_{m_2}(\lambda)$ are the Kolmogorov–Sinai entropies. By Lemma 2 below, $\mathcal P_m=\bigvee_{i \lt m}T^{-i}\mathcal P_1$ and $\mathcal P_1$ generates the Borel sets; likewise $\mathcal Q_q=\bigvee_{i \lt q}m_2^{-i}\mathcal Q_1$ and $\mathcal Q_1$ generates. Hence [17, Theorem 4.18], for invariant $\nu$ and $\lambda$,

$$
h_T(\nu)=\lim_{m\to\infty}\frac1mH_\nu(\mathcal P_m)=\inf_m\frac1mH_\nu(\mathcal P_m),\qquad
h_{m_2}(\lambda)=\lim_{q\to\infty}\frac1qH_\lambda(\mathcal Q_q)=\inf_q\frac1qH_\lambda(\mathcal Q_q),
$$

the infima because these sequences are subadditive. The entropy of $T$ is thus the entropy rate of the binary digits of a $\nu$-random point. For a $T$-invariant $\nu$ with $\rho \gt 0$ and ergodic decomposition $\nu=\int\nu_\omega\,dP(\omega)$ we put

$$
h_{\mathrm{odd}}(\nu)=\frac1\rho\int\nu_\omega(\mathbb O)\,h_T(\nu_\omega)\,dP(\omega),
$$

so that $h_{\mathrm{odd}}(\nu)=h_T(\nu)$ when $\nu$ is ergodic. The function $\omega\mapsto h_T(\nu_\omega)=\lim_m\frac1mH_{\nu_\omega}(\mathcal P_m)$ is measurable, as a limit of measurable functions, and $h_T(\nu)=\int h_T(\nu_\omega)\,dP(\omega)$ (Jacobs' theorem [17, Theorem 8.4]).

## 4. Results and proofs

### 4.1 One step of $T$ on the windows

**Lemma 1.** For $x\in\mathbb Z_2$, $d\ge0$ and $v=v(x)$, in $\mathbb T$:

$$
\text{(i)}\quad 2\,w_{d+1}(x)=w_d(x),\qquad\qquad\text{(ii)}\quad w_d(Tx)=3^{v}\,w_{d+1}(x)+\frac{v}{2^{d+1}} .
$$

*Proof.* Write $x=r+2^{d+1}y$ with $r=x \bmod 2^{d+1}$ and $y\in\mathbb Z_2$. (i) $2r/2^{d+1}=r/2^d$, which equals $(r \bmod 2^d)/2^d$ modulo $1$, and $r \bmod 2^d=x \bmod 2^d$. (ii) Since $v=r \bmod 2$, the number $(3^vr+v)/2$ is a non-negative integer, and $T(x)=(3^vx+v)/2=(3^vr+v)/2+2^d3^vy$. Hence $T(x) \bmod 2^d=((3^vr+v)/2) \bmod 2^d$ and $w_d(Tx)=(3^vr+v)/2^{d+1}$ modulo $1$. $\square$

**Lemma 2 (parity coding; Terras [1], see [2, Theorem B]).** For $m\ge0$ and $x\in\mathbb Z_2$ let $l_m(x)$ be the number of odd points among $x,Tx,\ldots,T^{m-1}x$. (a) For $y\in\mathbb Z_2$, $x+2^my$ has the same first $m$ parities as $x$, and $T^m(x+2^my)=T^m(x)+3^{l_m(x)}y$. (b) The first $m$ parities of $x$ depend only on $x \bmod 2^m$, and this defines a bijection from $\mathbb Z/2^m$ onto $\{0,1\}^m$. (c) The map sending $x$ to its parity sequence $(v(T^jx))_{j\ge0}$ is a homeomorphism of $\mathbb Z_2$ onto $\{0,1\}^{\mathbb N}$ which conjugates $T$ to the shift.

*Proof.* (a) By induction on $m$; the case $m=0$ is trivial. Let $z=T^m(x)$ and $l=l_m(x)$. By (a) for $m$ applied to $2y$, the point $x+2^{m+1}y$ has the same first $m$ parities as $x$ and $T^m(x+2^{m+1}y)=z+2\cdot3^ly$, which has the parity of $z$. If $z$ is even, $T(z+2\cdot3^ly)=T(z)+3^ly$; if $z$ is odd, $T(z+2\cdot3^ly)=(3z+1)/2+3^{l+1}y=T(z)+3^{l+1}y$. (b) By (a) the map is well defined. It is injective, by induction: if $x,x'$ have the same first $m+1$ parities, then $x'=x+2^my$ by the induction hypothesis, and $T^m(x')=T^m(x)+3^{l}y$ has the parity of $T^m(x)$, so $y$ is even. Both sets have $2^m$ elements. (c) follows from (b): cylinders correspond to residue classes. $\square$

### 4.2 The deterministic invariance

**Theorem 1.** Let $x\in\mathbb Z_2$, $J,D\ge1$, $O=\{0\le j \lt J: x_j\ \text{odd}\}$, and for a Lipschitz function $f$ on $\mathbb T$ let

$$
S(f)=\sum_{d=1}^{D}\sum_{j\in O}f\bigl(w_d(x_j)\bigr).
$$

Then

$$
\bigl\lvert S(f\circ m_3)-S(f)\bigr\rvert\le2\lVert f\rVert_\infty(J+D)+\tfrac12\mathrm{Lip}(f)\,\#O,
\qquad
\bigl\lvert S(f\circ m_2)-S(f)\bigr\rvert\le2\lVert f\rVert_\infty\,\#O .
$$

In particular, for an integer $n$ with iterates $x_j$ and every integer $k$,

$$
\Bigl\lvert\sum_{d=1}^{D}\sum_{j\in O}\Bigl(e\bigl(3kx_j/2^d\bigr)-e\bigl(kx_j/2^d\bigr)\Bigr)\Bigr\rvert\le2(J+D)+\pi\lvert k\rvert\,\#O .
$$

If $O$ is not empty and $\mu_{J,D}=(D\cdot\#O)^{-1}\sum_{d=1}^{D}\sum_{j\in O}\delta_{w_d(x_j)}$, the two inequalities read

$$
\Bigl\lvert\int f\circ m_3\,d\mu_{J,D}-\int f\,d\mu_{J,D}\Bigr\rvert\le2\lVert f\rVert_\infty\Bigl(\frac{J}{D\,\#O}+\frac1{\#O}\Bigr)+\frac{\mathrm{Lip}(f)}{2D},
\qquad
\Bigl\lvert\int f\circ m_2\,d\mu_{J,D}-\int f\,d\mu_{J,D}\Bigr\rvert\le\frac{2\lVert f\rVert_\infty}{D}.
$$

*Proof.* Let $E=\{0\le j \lt J\}\setminus O$ and fix $d\ge1$. By Lemma 1(ii), $f(w_d(x_{j+1}))$ equals $f(w_{d+1}(x_j))$ for $j\in E$ and $f(3w_{d+1}(x_j)+2^{-d-1})$ for $j\in O$. Moreover $\sum_{j \lt J}f(w_d(x_{j+1}))=\sum_{j \lt J}f(w_d(x_j))+\beta_d$ with $\beta_d=f(w_d(x_J))-f(w_d(x_0))$, $\lvert\beta_d\rvert\le2\lVert f\rVert_\infty$. Hence

$$
\sum_{j\in O}f(w_d(x_j))+\sum_{j\in E}f(w_d(x_j))+\beta_d=\sum_{j\in E}f(w_{d+1}(x_j))+\sum_{j\in O}f\bigl(3w_{d+1}(x_j)+2^{-d-1}\bigr).
$$

Sum over $d=1,\ldots,D$. The sums over $E$ telescope to $\sum_{j\in E}(f(w_{D+1}(x_j))-f(w_1(x_j)))$, of modulus at most $2\lVert f\rVert_\infty\#E$. So

$$
S(f)=\sum_{d=2}^{D+1}\sum_{j\in O}f\bigl(3w_d(x_j)+2^{-d}\bigr)+R_1,\qquad\lvert R_1\rvert\le2\lVert f\rVert_\infty(\#E+D).
$$

Replacing $f(3w_d(x_j)+2^{-d})$ by $f(3w_d(x_j))$ costs at most $\mathrm{Lip}(f)2^{-d}$ per term, in total at most $\mathrm{Lip}(f)\,\#O\sum_{d\ge2}2^{-d}=\tfrac12\mathrm{Lip}(f)\,\#O$. Finally $\sum_{d=2}^{D+1}\sum_{j\in O}f(3w_d(x_j))=S(f\circ m_3)+\sum_{j\in O}(f(3w_{D+1}(x_j))-f(3w_1(x_j)))$, and the last sum has modulus at most $2\lVert f\rVert_\infty\#O$. Adding the three errors, with $\#E+\#O=J$, gives the first inequality. By Lemma 1(i), $f(2w_d(x))=f(w_{d-1}(x))$, so $S(f\circ m_2)-S(f)=\sum_{j\in O}(f(w_0(x_j))-f(w_D(x_j)))$, of modulus at most $2\lVert f\rVert_\infty\#O$. The other two displays are the case $f=e(k\,\cdot)$ and a division by $D\cdot\#O$. $\square$

The mechanism is that an even step moves a window one height up without changing it, so the even steps cancel along diagonals of the rectangle of times and heights, while an odd step multiplies the window by $3$ up to a translation $2^{-d-1}$ that is summable over heights. The errors are small only when both $J$ and $D$ are large and $\#O/J$ is bounded below.

### 4.3 Entropy of zoom-out limits

**Lemma 3 (covering by blocks of digits; the argument of Misiurewicz [18]).** Let $\alpha$ be a probability measure on $\mathbb Z_2$ and $1\le q\le D$. Then

$$
q\,H_\alpha(\mathcal P_D)\le\sum_{d=q}^{D}H_{(w_d)_\ast\alpha}(\mathcal Q_q)+2q^2\log2 .
$$

*Proof.* For $d\ge q$, the arc of $\mathcal Q_q$ containing $w_d(x)=\sum_{i \lt d}b_i(x)2^{i-d}$ determines and is determined by the digits $b_{d-q}(x),\ldots,b_{d-1}(x)$. So $H_{(w_d)_\ast\alpha}(\mathcal Q_q)$ is the entropy under $\alpha$ of the block of digits $[d-q,d)$. Fix $s\in\{0,\ldots,q-1\}$. The blocks $[s+iq,s+(i+1)q)$, $i\ge0$, contained in $[0,D)$ cover $[0,D)$ except fewer than $2q$ digits, and the entropy of a family of digits is at most the sum of the entropies of the blocks plus $\log2$ per remaining digit. Hence $H_\alpha(\mathcal P_D)\le\sum_iH_{(w_{s+(i+1)q})_\ast\alpha}(\mathcal Q_q)+2q\log2$. Sum over $s$: each $d\in[q,D]$ occurs exactly once as $s+(i+1)q$. $\square$

**Lemma 4.** Let $\alpha$ be a probability measure on $\mathbb Z_2$ and $\Lambda_{D_s}(\alpha)\to\bar\lambda$. Then $\bar\lambda$ is $m_2$-invariant and

$$
h_{m_2}(\bar\lambda)\ge\limsup_{s\to\infty}\frac1{D_s}H_\alpha(\mathcal P_{D_s}).
$$

*Proof.* By Lemma 1(i), $(m_2)_\ast(w_d)_\ast\alpha=(w_{d-1})_\ast\alpha$, so $(m_2)_\ast\Lambda_D(\alpha)-\Lambda_D(\alpha)=\frac1D((w_0)_\ast\alpha-(w_D)_\ast\alpha)$ has total variation at most $2/D$, and $\bar\lambda$ is $m_2$-invariant. Every $m_2$-invariant probability measure $\lambda$ gives mass $0$ to each dyadic point other than $0$: $\lambda(\{1/2\})=\lambda(m_2^{-1}\{0\})-\lambda(\{0\})=0$, and for a dyadic $t\ne0,1/2$, $\lambda(\{t\})\le\lambda(m_2^{-1}\{2t\})=\lambda(\{2t\})$, which is $0$ by induction on the denominator. Fix $q\ge2$ and let $\mathcal Q_q'$ be obtained from $\mathcal Q_q$ by merging the two arcs adjacent to $0$. Then $H(\mathcal Q_q')\le H(\mathcal Q_q)\le H(\mathcal Q_q')+\log2$ for every measure, and the cells of $\mathcal Q_q'$ have $\bar\lambda$-null boundaries. Let $\Lambda_D'=(D-q+1)^{-1}\sum_{d=q}^{D}(w_d)_\ast\alpha$; it differs from $\Lambda_D(\alpha)$ by at most $2q/D$ in total variation, so $\Lambda_{D_s}'\to\bar\lambda$ and $H_{\Lambda_{D_s}'}(\mathcal Q_q')\to H_{\bar\lambda}(\mathcal Q_q')$. By Lemma 3 and the concavity of $\mu\mapsto H_\mu(\mathcal Q_q)$,

$$
\frac qDH_\alpha(\mathcal P_D)\le H_{\Lambda_D'}(\mathcal Q_q)+\frac{2q^2\log2}{D}\le H_{\Lambda_D'}(\mathcal Q_q')+\log2+\frac{2q^2\log2}{D}.
$$

Along $D_s$ this gives $\limsup_s\frac1{D_s}H_\alpha(\mathcal P_{D_s})\le\frac1q(H_{\bar\lambda}(\mathcal Q_q)+\log2)$, and $q\to\infty$ gives the claim. $\square$

**Lemma 5.** Let $\nu$ be $T$-invariant with $\rho=\nu(\mathbb O) \gt 0$. Then $\liminf_{m}\frac1mH_{\nu_S}(\mathcal P_m)\ge h_{\mathrm{odd}}(\nu)$.

*Proof.* Ergodic case. Since $\nu_S\le\rho^{-1}\nu$, we have $-\log\nu_S(A)\ge\log\rho-\log\nu(A)$ for every cell $A$, so $H_{\nu_S}(\mathcal P_m)\ge\log\rho+\int I_m\,d\nu_S$, where $I_m(x)=-\log\nu(A)$ for the cell $A\in\mathcal P_m$ containing $x$. By Lemma 2, $I_m(x)$ is minus the logarithm of the probability of the first $m$ parities of $x$, for the stationary ergodic process of parities under $\nu$. By the theorem of Shannon, McMillan and Breiman [19], $I_m/m\to h_T(\nu)$ $\nu$-almost everywhere, hence $\nu_S$-almost everywhere, and Fatou's lemma gives the claim. General case. Let $\rho_\omega=\nu_\omega(\mathbb O)$. Then $\nu_S=\int(\nu_\omega)_S\,dP'(\omega)$ with $dP'=(\rho_\omega/\rho)\,dP$, a probability measure on $\{\rho_\omega \gt 0\}$. Concavity of $t\mapsto-t\log t$ gives $H_{\nu_S}(\mathcal P_m)\ge\int H_{(\nu_\omega)_S}(\mathcal P_m)\,dP'(\omega)$, and Fatou's lemma and the ergodic case give $\liminf_m\frac1mH_{\nu_S}(\mathcal P_m)\ge\int h_T(\nu_\omega)\,dP'(\omega)=h_{\mathrm{odd}}(\nu)$. $\square$

**Lemma 6 (integrals of zero-entropy measures).** Let $K$ be the compact convex metrisable set of $m_2$-invariant probability measures on $\mathbb T$, let $\pi$ be a probability measure on $K$ and $\eta=\int\mu\,d\pi(\mu)$. Then $h_{m_2}$ is upper semicontinuous on $K$ and $h_{m_2}(\eta)\le\int h_{m_2}(\mu)\,d\pi(\mu)$. In particular $h_{m_2}(\eta)=0$ if $h_{m_2}(\mu)=0$ for $\pi$-almost every $\mu$.

*Proof.* For $q\ge2$ put $g_q(\mu)=\frac1q(H_\mu(\mathcal Q_q')+\log2)$, with $\mathcal Q_q'$ as in the proof of Lemma 4. Then $h_{m_2}(\mu)\le\frac1qH_\mu(\mathcal Q_q)\le g_q(\mu)\le\frac1q(H_\mu(\mathcal Q_q)+\log2)$, so $g_q\to h_{m_2}$ pointwise on $K$ and $h_{m_2}=\inf_qg_q$. Each $g_q$ is continuous on $K$, because the boundaries of the cells of $\mathcal Q_q'$ are dyadic points other than $0$, which are null for every element of $K$ (proof of Lemma 4). So $h_{m_2}$ is upper semicontinuous. Let $(f_i)$ be dense in the unit ball of $C(\mathbb T)$; the distance $\mathrm d(\mu,\mu')=\sum_i2^{-i}\lvert\int f_i\,d\mu-\int f_i\,d\mu'\rvert$ defines the weak topology, and for a Borel set $B\subseteq K$ with $\pi(B) \gt 0$ the measure $\eta_B=\pi(B)^{-1}\int_B\mu\,d\pi(\mu)\in K$ satisfies $\mathrm d(\eta_B,\mu')\le\operatorname{diam}B$ for every $\mu'\in B$. For $n\ge1$ partition $K$ into finitely many Borel sets $B_{n,i}$ of diameter at most $1/n$, drop the $\pi$-null ones, and let $\pi_n=\sum_i\pi(B_{n,i})\delta_{\eta_{B_{n,i}}}$. Since $\eta=\sum_i\pi(B_{n,i})\eta_{B_{n,i}}$ and entropy is affine on finite convex combinations [17, Theorem 8.1], $h_{m_2}(\eta)=\int h_{m_2}\,d\pi_n$ for every $n$. For continuous $F$ on $K$, $\lvert\int F\,d\pi_n-\int F\,d\pi\rvert$ is at most the oscillation of $F$ at scale $1/n$, so $\pi_n\to\pi$. Therefore, for every $q$, $h_{m_2}(\eta)\le\lim_n\int g_q\,d\pi_n=\int g_q\,d\pi$, and $\int g_q\,d\pi\to\int h_{m_2}\,d\pi$ as $q\to\infty$ by dominated convergence. $\square$

### 4.4 The rigidity theorem

**Theorem 2.** Let $\nu$ be a $T$-invariant probability measure on $\mathbb Z_2$ with $\rho=\nu(\mathbb O) \gt 0$.

**(1)** For every $D\ge1$ and every Lipschitz $f$ on $\mathbb T$,

$$
\Bigl\lvert\int f\circ m_3\,d\Lambda_D(\nu_S)-\int f\,d\Lambda_D(\nu_S)\Bigr\rvert\le\frac1D\Bigl(\frac{2\lVert f\rVert_\infty}{\rho}+\frac{\mathrm{Lip}(f)}2\Bigr),\qquad
\bigl\lVert(m_2)_\ast\Lambda_D(\nu_S)-\Lambda_D(\nu_S)\bigr\rVert_{\mathrm{TV}}\le\frac2D .
$$

Hence every zoom-out limit $\bar\lambda$ of $\nu_S$ is invariant under $m_2$ and under $m_3$.

**(2)** $h_{m_2}(\bar\lambda)\ge h_{\mathrm{odd}}(\nu)$.

**(3)** $\bar\lambda=c\,\mathrm{Leb}+(1-c)\,\eta$ with $c=h_{m_2}(\bar\lambda)/\log2\ge h_{\mathrm{odd}}(\nu)/\log2$, where $\eta$ is a probability measure invariant under $m_2$ and $m_3$ with $h_{m_2}(\eta)=0$ (absent if $c=1$).

*Proof.* (1) Apply Theorem 1 to each $x$ and integrate against $\nu$. By $T$-invariance, $\int S(f)\,d\nu=\sum_{d=1}^{D}\sum_{j \lt J}\int_{\mathbb O}f\circ w_d\,d\nu=JD\rho\int f\,d\Lambda_D(\nu_S)$ and $\int\#O\,d\nu=J\rho$. Dividing by $JD\rho$ and letting $J\to\infty$ gives the first inequality. The second was shown in the proof of Lemma 4. Lipschitz functions are dense in $C(\mathbb T)$, so $\bar\lambda$ is invariant under both maps.

(2) Lemma 4 with $\alpha=\nu_S$ and Lemma 5: $h_{m_2}(\bar\lambda)\ge\limsup_s\frac1{D_s}H_{\nu_S}(\mathcal P_{D_s})\ge h_{\mathrm{odd}}(\nu)$.

(3) Let $M$ be the set of probability measures on $\mathbb T$ invariant under $m_2$ and $m_3$; it is compact, convex and metrisable. By Choquet's theorem [20, Section 3], $\bar\lambda=\int\mu\,d\pi(\mu)$ for a probability measure $\pi$ on $M$ carried by the extreme points. An extreme point $\mu$ is ergodic for the semigroup generated by $m_2$ and $m_3$: if a Borel set $A$ with $0 \lt \mu(A) \lt 1$ satisfied $\mu(A\,\triangle\,m_a^{-1}A)=0$ for $a=2,3$, the normalised restrictions of $\mu$ to $A$ and to its complement would be two distinct elements of $M$ with $\mu$ a proper convex combination of them. By Rudolph's theorem [3, Theorem 4.9], every such $\mu$ is $\mathrm{Leb}$ or has $h_{m_2}(\mu)=0$. Let $c=\pi(\{\mathrm{Leb}\})$. If $c=1$ then $\bar\lambda=\mathrm{Leb}$. Otherwise let $\eta=(1-c)^{-1}\int_{\mu\ne\mathrm{Leb}}\mu\,d\pi(\mu)\in M$; Lemma 6 gives $h_{m_2}(\eta)=0$. Then $\bar\lambda=c\,\mathrm{Leb}+(1-c)\eta$ and, entropy being affine [17, Theorem 8.1], $h_{m_2}(\bar\lambda)=c\log2$. $\square$

**Remarks.** (a) *Positivity.* $h_{\mathrm{odd}}(\nu) \gt 0$ as soon as $h_T(\nu) \gt 0$. Indeed $h_T(\nu)=\int h_T(\nu_\omega)\,dP(\omega)$ [17, Theorem 8.4], so $h_T(\nu_\omega) \gt 0$ on a set of positive $P$-measure, while an ergodic component $\nu_\omega$ with $\nu_\omega(\mathbb O)=0$ is carried by the points all of whose iterates are even, that is, by $\{0\}$ (Lemma 2(c)), and has entropy $0$. (b) *The bound is attained, and $h_{\mathrm{odd}}$ cannot be replaced by $h_T$.* Haar measure of $\mathbb Z_2$ corresponds under Lemma 2 to fair independent parities; it is $T$-invariant and ergodic, with entropy $\log2$ and $\mathrm{Haar}(\mathbb O)=1/2$. The point $-1$ is fixed by $T$. For $\nu=\tfrac12\mathrm{Haar}+\tfrac12\delta_{-1}$ we get $\rho=3/4$, $h_T(\nu)=\tfrac12\log2$, $h_{\mathrm{odd}}(\nu)=\tfrac13\log2$ and $\nu_S=\tfrac13\mathrm{Haar}_S+\tfrac23\delta_{-1}$. The windows of $\mathrm{Haar}_S$ are uniform on the odd multiples of $2^{-d}$ and $w_d(-1)=1-2^{-d}$, so the zoom-out limit is $\tfrac13\mathrm{Leb}+\tfrac23\delta_0$: here $c=1/3=h_{\mathrm{odd}}(\nu)/\log2 \lt h_T(\nu)/\log2$. (c) *Averages over heights are needed.* Proposition 4(3) gives a $\nu$ for which the single-height laws $(w_d)_\ast\nu_S$ have three limit points, none invariant under $m_2$ or $m_3$.

### 4.5 Single orbits

**Lemma 7 (standard).** Let $n$ be a positive integer whose orbit is divergent. Then $x_j\to\infty$ and $\liminf_{J\to\infty}\frac1J\#\{j \lt J:x_j\ \text{odd}\}\ge\log2/\log3$.

*Proof.* The $x_j$ are pairwise distinct positive integers, so $x_j\to\infty$. Since $x_{j+1}=\frac{3x_j}{2}(1+\frac1{3x_j})$ for $x_j$ odd, $2^Jx_J=3^{l}x_0\prod_{j \lt J,\ x_j\ \mathrm{odd}}(1+\frac1{3x_j})$ with $l=l_J(n)$. As $x_J\ge1$, taking logarithms gives $J\log2\le\log x_0+l\log3+\sum_{j \lt J}\frac1{3x_j}$, and the last sum is $o(J)$. $\square$

**Corollary 3.** Let $x\in\mathbb Z_2$ and $O_J=\{j \lt J:x_j\ \text{odd}\}$, and let $\mu_{J,D}$ be as in Theorem 1.

**(1)** If $D_s\to\infty$ and $J_s\to\infty$ with $\liminf_s\#O_{J_s}/J_s \gt 0$, every limit point of $\mu_{J_s,D_s}$ is invariant under $m_2$ and $m_3$.

**(2)** Suppose that $\frac1{J_s}\sum_{j \lt J_s}\delta_{x_j}\to\nu$ along $J_s\to\infty$, with $\nu(\mathbb O) \gt 0$. Then $\nu$ is $T$-invariant, $\mu_{J_s,D}\to\Lambda_D(\nu_S)$ for every $D$, and for every open arc $I\subseteq\mathbb T$ of length $\lvert I\rvert$,

$$
\liminf_{D\to\infty}\ \liminf_{s\to\infty}\ \mu_{J_s,D}(I)\ \ge\ \frac{h_{\mathrm{odd}}(\nu)}{\log2}\,\lvert I\rvert .
$$

**(3)** If $x$ is a positive integer with a divergent orbit, every sequence $J_s\to\infty$ has a subsequence along which the hypothesis of (2) holds, with $\nu(\mathbb O)\ge\log2/\log3$.

*Proof.* (1) is the last display of Theorem 1, Lipschitz functions being dense in $C(\mathbb T)$. (2) $T$ is continuous, so $\nu$ is $T$-invariant. For continuous $f$ the function $x\mapsto\mathbf 1_{\mathbb O}(x)f(w_d(x))$ is continuous on $\mathbb Z_2$, and $\#O_{J_s}/J_s\to\nu(\mathbb O)$; hence $\mu_{J_s,D}\to\Lambda_D(\nu_S)$ and $\liminf_s\mu_{J_s,D}(I)\ge\Lambda_D(\nu_S)(I)$. If $\Lambda_{D_t}(\nu_S)(I)$ converges along some $D_t\to\infty$, pass to a subsequence along which $\Lambda_{D_t}(\nu_S)$ converges, to $\bar\lambda$ say; then the limit is at least $\bar\lambda(I)\ge c\,\lvert I\rvert\ge h_{\mathrm{odd}}(\nu)\lvert I\rvert/\log2$ by Theorem 2. (3) $\mathbb Z_2$ is compact, $\mathbf 1_{\mathbb O}$ is continuous, and Lemma 7 applies. $\square$

In (2) the limit in time is taken first. For an integer $x$ and fixed $J$, all windows $w_d(x_j)$ tend to $0$ in $\mathbb T$ as $d\to\infty$, so the limits cannot be exchanged.

### 4.6 Rational cycles

**Proposition 4.** Let $q\ge1$ be odd and let $(a_0,\ldots,a_{k-1})$ be a cycle of the map $a\mapsto a/2$ ($a$ even), $a\mapsto(3a+q)/2$ ($a$ odd) on the integers *that contains an odd element*. Then $(a_i/q)$ is a cycle of $T$ in $\mathbb Z_2$; let $\nu$ be the uniform measure on it, so that $\nu_S$ is the uniform measure on the points $a_i/q$ with $a_i$ odd.

1. For every integer $a$ and $d\ge0$, $w_d(a/q)$ is at distance at most $\lvert a\rvert/(q2^d)$ from $t/q$, where $t\equiv-a2^{-d}\pmod q$.
2. $\Lambda_D(\nu_S)$ converges as $D\to\infty$ to the uniform average of the point masses at $-a_i2^{e}/q$, over the odd $a_i$ and over $e$ modulo the order of $2$ modulo $q$. This limit is invariant under $m_2$ and $m_3$, and $c=0$ in Theorem 2.
3. For $q=7$ and the cycle $(5,11,20,10)$: the single-height laws $(w_d)_\ast\nu_S$ converge, along $d\equiv0,1,2\pmod3$, to the uniform measures on $\{2,3\}/7$, $\{1,5\}/7$ and $\{4,6\}/7$ respectively, none of which is invariant under $m_2$ or under $m_3$; their average, the zoom-out limit of $\nu_S$, is uniform on $\{1,\ldots,6\}/7$. The corresponding scale average for the even points of the cycle is uniform on $\{1,2,4\}/7$, and for the whole cycle it gives mass $3/4$ to $\{1,2,4\}/7$ and $1/4$ to $\{3,5,6\}/7$; neither is invariant under $m_3$.

*Proof.* (1) Let $r=(a/q) \bmod 2^d$. Then $qr\equiv a\pmod{2^d}$, so $qr=a+2^dt'$ with $t'$ an integer, $t'\equiv-a2^{-d}\pmod q$, and $r/2^d=t'/q+a/(q2^d)$. (2) $a/q$ is odd in $\mathbb Z_2$ exactly when $a$ is odd, and $T(a/q)=(3a+q)/(2q)$ then. By (1), $w_d(a_i/q)$ is within $\lvert a_i\rvert/(q2^d)$ of $-a_i2^{-d}/q$, and $-a_i2^{-d}$ modulo $q$ is periodic in $d$ with period the order of $2$; so the averages over $d$ converge to the stated measure, which is invariant under $m_2$. If $a$ is odd and $a'$ is the next odd element of the cycle, then $2^ga'=3a+q$ for some $g\ge1$, so $a'\equiv3a2^{-g}\pmod q$: multiplication by $3$ maps the points attached to $a$ onto those attached to $a'$, and $a\mapsto a'$ permutes the odd elements. The limit is purely atomic, so $c=0$. (3) One checks $5\to11\to20\to10\to5$. Modulo $7$, $2^{-d}$ is $1,4,2$ for $d\equiv0,1,2\pmod3$. The odd elements $5$ and $11\equiv4$ give $-5\cdot(1,4,2)\equiv(2,1,4)$ and $-4\cdot(1,4,2)\equiv(3,5,6)$, which are the three stated pairs; $m_2$ maps $\{2,3\}$ to $\{4,6\}$, $\{1,5\}$ to $\{2,3\}$, $\{4,6\}$ to $\{1,5\}$, and $m_3$ maps them to $\{6,2\}$, $\{3,1\}$, $\{5,4\}$. The even elements $20\equiv6$ and $10\equiv3$ give $-6\cdot\{1,2,4\}=\{1,2,4\}$ and $-3\cdot\{1,2,4\}=\{4,1,2\}$, and $m_3\{1,2,4\}=\{3,6,5\}$. $\square$

The hypothesis that the cycle contains an odd element excludes exactly the cycle $(0)$, for which $\nu_S$ is not defined. Part (3) shows that Theorems 1 and 2 are statements about odd iterates and about averages over heights. This is not a peculiarity of zero entropy: for $\nu'=\tfrac12\nu+\tfrac12\nu_{p}$ with $p=0.9$ and $\nu_p$ as in Proposition 5, $h_T(\nu') \gt 0$ and $\nu'(\mathbb O)=0.7$, and the odd part is $\tfrac{5}{14}\nu_S+\tfrac{9}{14}(\nu_p)_S$; its single-height laws are $\tfrac{5}{14}$ times those of part (3) plus a term converging to $\tfrac{9}{14}\mathrm{Leb}$, and still have three limit points.

### 4.7 Bernoulli parity measures

For $0 \lt p \lt 1$ and $q=1-p$, let $\nu_p$ be the probability measure on $\mathbb Z_2$ giving mass $p^{l}q^{m-l}$ to the residue class modulo $2^m$ whose parity word of length $m$ has $l$ ones. By Lemma 2 it is the image of the Bernoulli product measure under the inverse of the parity coding: under $\nu_p$ the parities $v(T^jx)$ are independent with $\nu_p(v(T^jx)=1)=p$. Hence $\nu_p$ is $T$-invariant and ergodic [17, Section 1.5], $\nu_p(\mathbb O)=p$, $H_{\nu_p}(\mathcal P_m)=mH(p)$ with $H(p)=-p\log p-q\log q$, so $h_T(\nu_p)=H(p)$, and by the law of large numbers $\nu_p$-almost every orbit has density of odd steps $p$. Moreover, for every $s\ge0$, $T^s(x)$ is independent of the first $s$ parities of $x$ and has law $\nu_p$.

**Proposition 5.** Let $k=2^ak_0\ne0$ with $k_0$ odd, and let $s\ge1$, $m\ge a+3$, $d=s+m$ and $N=2^{m-a-2}$. Then

$$
\Bigl\lvert\int e\bigl(k\,w_d\bigr)\,d(\nu_p)_S\Bigr\rvert\le2^{(a+2)/2}\,(p^2+q^2)^{m/2}+N\exp\Bigl(-\frac{8pq\,(s-1)}{N^2}\Bigr).
$$

Consequently $(w_d)_\ast(\nu_p)_S\to\mathrm{Leb}$ as $d\to\infty$, for every $p\in(0,1)$: every zoom-out limit of $(\nu_p)_S$ is Lebesgue measure, and $c=1$ in Theorem 2.

*Proof.* For $m\ge0$ and $a'\in\mathbb Z/2^m$ let $\varphi_m(a')=\int e(a'(x \bmod 2^m)/2^m)\,d\nu_p(x)$. Parseval's identity on $\mathbb Z/2^m$ gives

$$
\sum_{a'}\lvert\varphi_m(a')\rvert^2=2^m\sum_{r}\nu_p(r+2^m\mathbb Z_2)^2=2^m(p^2+q^2)^m .
$$

*Transfer.* Let $\chi(x)=e(k(x \bmod 2^d)/2^d)$, an additive character of $\mathbb Z_2$. If the first $s$ parities of $x$ form the word $u$, with $l=l(u)$ ones, Lemma 2(a) gives $2^sT^s(x)=3^lx+c_u$ for an integer $c_u$ depending only on $u$, so $x=3^{-l}2^sT^s(x)-3^{-l}c_u$ in $\mathbb Z_2$. For $y\in\mathbb Z_2$, $(3^{-l}2^sy) \bmod 2^d=2^s((3^{-l}y) \bmod 2^m)$, so $\chi(3^{-l}2^sy)=e(k_l(y \bmod 2^m)/2^m)$ with $k_l\equiv k3^{-l}\pmod{2^m}$. Integrating over the words $u$ with $u_0=1$ and using the independence of $T^s(x)$ and $u$,

$$
\int\chi\,d(\nu_p)_S=\sum_{u:\,u_0=1}\frac{\nu_p(u)}p\,\chi\bigl(-3^{-l(u)}c_u\bigr)\,\varphi_m\bigl(k3^{-l(u)}\bigr),\qquad\text{so}\qquad\Bigl\lvert\int\chi\,d(\nu_p)_S\Bigr\rvert\le\mathbb E\,\bigl\lvert\varphi_m(k3^{-l})\bigr\rvert ,
$$

where $l-1$ is binomial with parameters $(s-1,p)$.

*Averaging.* The class $k3^{-l}$ modulo $2^m$ equals $2^a(k_03^{-l} \bmod 2^{m-a})$. Since $m-a\ge3$, the order of $3$ modulo $2^{m-a}$ is $N=2^{m-a-2}$, so this class depends only on $l$ modulo $N$, and injectively so. If $l$ modulo $N$ were uniform, the inequality of Cauchy and Schwarz and Parseval's identity would give $\mathbb E\lvert\varphi_m(k3^{-l})\rvert\le(\frac1N\sum_{a'}\lvert\varphi_m(a')\rvert^2)^{1/2}=2^{(a+2)/2}(p^2+q^2)^{m/2}$. In general the expectation exceeds this by at most $\sum_{j \bmod N}\lvert\mathbb P(l\equiv j)-\frac1N\rvert$, since $\lvert\varphi_m\rvert\le1$. By Fourier inversion on $\mathbb Z/N$ this sum is at most $\sum_{t=1}^{N-1}\lvert q+p\,e(t/N)\rvert^{s-1}$. Finally $\lvert q+p\,e(\theta)\rvert^2=1-4pq\sin^2(\pi\theta)\le1-16pq\,\mathrm{dist}(\theta,\mathbb Z)^2$ and $\mathrm{dist}(t/N,\mathbb Z)\ge1/N$, so each term is at most $(1-16pq/N^2)^{(s-1)/2}\le\exp(-8pq(s-1)/N^2)$.

*Limit.* Fix $k$ and take $m=a+2+\lfloor\frac13\log_2d\rfloor$ for $d\ge8$; then $N\le d^{1/3}$ and $s=d-m\ge d/2$ for large $d$, and both terms tend to $0$. So every Fourier coefficient of $(w_d)_\ast(\nu_p)_S$ of index $k\ne0$ tends to $0$. $\square$

**Remarks.** (a) The bound depends on $k$ only through $a$, so it is uniform over the frequencies of a given dyadic level, as in [10, Theorem 1] for block measures; with the choice of $m$ above it decays like a power of $d$. (b) Numerically (Section 7), for $p=0.7$ the coefficients at $k=1,3,5,7$ have modulus between $0.08$ and $0.18$ at $d=6$, between $0.012$ and $0.029$ at $d=12$, and between $0.0026$ and $0.0079$ at $d=18$, while the supremum over all odd $k$ is $0.148$, $0.110$, $0.082$ at $d=8,12,16$. (c) By Corollary 3(2) and the ergodic theorem, for $\nu_p$-almost every $x$ the window statistics $\mu_{J,D}$ of the orbit of $x$ converge to $\Lambda_D((\nu_p)_S)$ as $J\to\infty$, and these converge to $\mathrm{Leb}$ as $D\to\infty$, while the density of odd steps is $p$.

## 5. Where the route stops

The intended argument against a divergent orbit of a positive integer had five steps.

- **S1.** The orbit has limit measures $\nu$ in $\mathbb Z_2$; they are $T$-invariant with $\nu(\mathbb O)\ge\log2/\log3 \gt 1/2$. *Proved* (Corollary 3(3)).
- **S2.** The windows of the odd iterates, averaged over time and height, are invariant under $\times2$ and $\times3$. *Proved* (Theorem 1).
- **S3.** If $\nu$ has positive entropy, these window statistics contain Lebesgue measure with weight $c\ge h_{\mathrm{odd}}(\nu)/\log2 \gt 0$. *Proved* (Theorem 2). Only a weight $c$, not $c=1$, is obtained.
- **S4.** Lebesgue-distributed windows force fair parities, hence $\nu(\mathbb O)=1/2$, contradicting S1. ***False***, even when $c=1$ and even at every single height (Proposition 5, Proposition 6).
- **S5.** A divergent orbit has a limit measure of positive entropy. ***Open.***

The reason for the failure of S4 is the following exact relation between parities and digits.

**Lemma 8.** For $x\in\mathbb Z_2$ and $d\ge0$: $v(T^dx)\equiv b_d(x)+\varepsilon_d(x)\pmod2$, where $\varepsilon_d(x)=v(T^d(x \bmod 2^d))$ depends only on the digits of $x$ below height $d$.

*Proof.* Lemma 2(a) with $x=r+2^dy$, $r=x \bmod 2^d$: $T^d(x)=T^d(r)+3^ly$, and $y\equiv b_d(x)\pmod2$. $\square$

**Proposition 6 (fine and coarse scales).**

1. For every $T$-invariant probability measure $\nu$ and $d\ge0$, the conditional entropy of the digit $b_d$ given *all* lower digits is $H_\nu(b_d\mid b_0,\ldots,b_{d-1})=H_\nu(\mathcal P_{d+1})-H_\nu(\mathcal P_d)$, which is the conditional entropy of the parity $v\circ T^d$ given the $d$ previous parities; it is non-increasing in $d$ and converges to $h_T(\nu)$. It converges to $\log2$ only if $\nu$ is Haar measure, for which it equals $\log2$ for every $d$.
2. Under $(\nu_p)_S$, for every $d\ge1$: given $x \bmod 2^d$, the digit $b_d(x)$ equals $\varepsilon_d(x)+1$ with probability $p$ and $\varepsilon_d(x)$ with probability $q$, so $H(b_d\mid b_0,\ldots,b_{d-1})=H(p)$, which is less than $\log2$ for $p\ne1/2$. On the other hand, for every fixed $n\ge0$, the law of $(b_d,b_{d-1},\ldots,b_{d-n})$ under $(\nu_p)_S$ converges to the uniform law on $\{0,1\}^{n+1}$ as $d\to\infty$: given any bounded number of digits just below it, $b_d$ is asymptotically a fair coin.

*Proof.* (1) By Lemma 2(b), the digits below height $d$ and the first $d$ parities determine each other, and by Lemma 8 so do, given them, $b_d$ and $v\circ T^d$. So the conditional entropy is $u_d=H_\nu(\mathcal P_{d+1})-H_\nu(\mathcal P_d)=H(v\circ T^d\mid v,\ldots,v\circ T^{d-1})$. By invariance, $u_{d+1}=H(v\circ T^{d+1}\mid v,\ldots,v\circ T^{d})\le H(v\circ T^{d+1}\mid v\circ T,\ldots,v\circ T^{d})=u_d$, and the averages $\frac1m\sum_{d \lt m}u_d=\frac1mH_\nu(\mathcal P_m)$ tend to $h_T(\nu)$; so $u_d\to h_T(\nu)$. If the limit is $\log2$ then $u_d=\log2$ for all $d$, $H_\nu(\mathcal P_m)=m\log2$ for all $m$, and $\nu$ is uniform on the residue classes modulo every $2^m$; conversely Haar measure has $H_\nu(\mathcal P_m)=m\log2$, hence $u_d=\log2$, for every $d$. (2) Given $x \bmod 2^d$ with $x$ odd, that is, given the first $d$ parities, the parity $v(T^dx)$ is $1$ with probability $p$; apply Lemma 8. For the second statement, $(b_d,\ldots,b_{d-n})$ are the first $n+1$ binary digits of $w_{d+1}(x)$; the arcs of $\mathcal Q_{n+1}$ have Lebesgue-null boundaries, and $(w_{d+1})_\ast(\nu_p)_S\to\mathrm{Leb}$ by Proposition 5. $\square$

So the density of odd steps is governed by the law of $b_d$ given all $d$ lower digits (the *fine* scale, equivalent to the entropy of $\nu$ being maximal), while Theorems 1 and 2, being statements about weak limits of window laws on the circle, see $b_d$ together with a bounded number of digits below it (the *coarse* scale), and only on average over $d$. For $\nu_p$ the dependence of $b_d$ on the lower digits is real but is carried by digits at unbounded distance below $d$. A generic point of $\nu_p$ with $p \gt \log2/\log3$ satisfies the conclusions of S2 and S3 with $c=1$, so these conclusions cannot contradict S1. Section 7 illustrates Proposition 6 numerically: for $p=0.7$ the conditional entropy of $b_d$ given all lower digits is $0.8813$ bit for every $d$, and given the $4$ digits just below it is $0.9530$, $0.9948$, $0.9995$ bit at $d=7,11,15$.

## 6. Limitations and scope

**The conjecture is not proved.** Nothing in this paper excludes a cycle or a divergent orbit of a positive integer. Theorems 1 and 2 are true statements about every orbit and every invariant measure, and Proposition 5 shows that they are satisfied by generic points with any density of odd steps.

**Zero entropy is untouched.** If $h_{\mathrm{odd}}(\nu)=0$, Theorem 2 gives $c\ge0$ and nothing else; rational cycles have $c=0$ (Proposition 4). The parity sequence of a divergent orbit is not eventually periodic (a point of $\mathbb Z_2$ with an eventually periodic parity sequence is eventually periodic, by Lemma 2(c)), so by the theorem of Morse and Hedlund [21] it has at least $m+1$ distinct factors of each length $m$; this is compatible with zero entropy, the Sturmian sequences having exactly $m+1$. Sturmian itineraries of the critical slope are treated by Diophantine methods in [22].

**Integrality is not used.** Every statement holds on all of $\mathbb Z_2$, in particular at rational points with odd denominator (Proposition 4) and at negative integers. The proofs also apply, with the same wording, to the maps $x\mapsto x/2$ ($x$ even), $x\mapsto(ax+b)/2$ ($x$ odd) with $a\ge3$ and $b$ odd integers: Lemma 1(ii) becomes $w_d(Tx)=a^vw_{d+1}(x)+vb/2^{d+1}$, Lemma 2 holds with $a^{l}$, Theorem 1 holds with $m_a$ in place of $m_3$ and $\tfrac12\lvert b\rvert\,\mathrm{Lip}(f)\,\#O$ in its error term, and Theorem 2 holds with $m_a$, because Rudolph's theorem covers every pair of relatively prime multipliers. This includes $3x-1$ and $5x+1$, each of which has several cycles of positive integers (those of $1$, $5$, $17$ and of $1$, $13$, $17$ respectively), and $3x+q$, whose cycles are the rational cycles of Proposition 4. An argument along this line that excluded cycles or divergent orbits would therefore have to use, at some step, a property of the map $3x+1$ on the integers that these maps do not share; no such step is available here. The inequality $3 \lt 4$ would have entered only through $\log2/\log3 \gt 1/2$ in the comparison of S1 with S4.

**Order of limits and heights.** For an integer orbit the theorems concern heights $d$ that are small compared with $\log_2x_j$ (time limit first, Corollary 3). They say nothing about the leading digits of the iterates.

**Open problems.**

1. (S5) Does every limit measure of a divergent orbit of a positive integer have positive entropy? We know of no result on the entropy of these limit measures. The restrictions on the itinerary recalled above, that it is not eventually periodic (hence of complexity at least $m+1$) and not Sturmian of slope $\log2/\log3$ [22], do not give positive entropy.
2. (Fine scale) Is there a version of Theorem 2 controlling the law of $b_d(x_j)$ given $x_j \bmod 2^d$ along a single orbit, in the way the fine-scale mixing of [15] does on average over starting points?
3. (Upper bounds on $c$) Can integrality bound the Lebesgue weight $c$ of the window statistics of an integer orbit from above? By Theorem 2 this would bound the entropy of its limit measures.
4. (Single heights) For an ergodic $\nu$ of positive entropy, are the limit points of the single-height laws $(w_d)_\ast\nu_S$ invariant under $m_2$ and $m_3$? Proposition 4(3) shows that this fails for zero entropy and for non-ergodic measures of positive entropy.
5. (The singular part) Rudolph's theorem leaves the zero-entropy part $\eta$ undetermined; determining the jointly invariant measures of zero entropy is Furstenberg's open problem [4, 3].

## 7. Reproducibility

All proofs are in the text; the imported results are Rudolph's theorem [3, Theorem 4.9], the theorem of Shannon, McMillan and Breiman [19], Choquet's theorem [20, Section 3], and the generator theorem, the affinity of entropy and its ergodic decomposition [17, Theorems 4.18, 8.1 and 8.4]. The supplement contains six Python scripts using only the standard library. Each exits with a non-zero status on failure and runs in seconds (`python3 supplement/NAME.py`); `supplement/README.md` lists the expected outputs.

| Script | Statement checked | Scope |
|---|---|---|
| `check_window_identity.py` | Lemmas 1, 2, 7 (product formula), 8 | exact arithmetic; integers of both signs up to $600$ bits, rationals with denominators up to $101$, all residues modulo $2^{12}$ |
| `check_orbit_invariance.py` | Theorem 1 | $956$ orbit segments (integers, $2$-adic integers with parity words of density $0.5$, $0.7$, $0.9$, rationals), characters and a tent function; largest observed ratio of defect to bound $0.41$; the $\times2$ bound is attained at $J=D=1$ |
| `check_invariant_measures.py` | Theorem 2(1), Lemmas 3 and 5, Remark (b) | Bernoulli and Markov parity measures, all residues modulo $2^{16}$ |
| `check_rational_cycles.py` | Proposition 4 | the $96$ cycles of $3x+q$ found for $20$ values of $q\le61$ with starting values below $3000$; the cycle $(5,11,20,10)$ of $3x+7$ |
| `check_bernoulli_windows.py` | Proposition 5 | Parseval's identity, the transfer identity and inequality, and the bound, for $p=0.3,0.7,0.9$, $d\le16$; the bound for all odd $k$ at once |
| `check_fine_coarse.py` | Proposition 6(2) | conditional entropies of $b_d$ for $p=0.7,0.9$, $d\le15$ |

The finite computations test the identities and inequalities used in the proofs; they do not establish the limit statements, which rest on the proofs.

## References

[1] R. Terras. A stopping time problem on the positive integers. Acta Arithmetica 30 (1976), 241–252. https://doi.org/10.4064/aa-30-3-241-252

[2] J. C. Lagarias. The $3x+1$ problem and its generalizations. American Mathematical Monthly 92 (1985), 3–23. https://doi.org/10.2307/2322189

[3] D. J. Rudolph. $\times2$ and $\times3$ invariant measures and entropy. Ergodic Theory and Dynamical Systems 10 (1990), 395–406. https://doi.org/10.1017/S0143385700005629

[4] H. Furstenberg. Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation. Mathematical Systems Theory 1 (1967), 1–49. https://doi.org/10.1007/BF01692494

[5] A. S. A. Johnson. Measures on the circle invariant under multiplication by a nonlacunary subsemigroup of the integers. Israel Journal of Mathematics 77 (1992), 211–240. https://doi.org/10.1007/BF02808018

[6] B. Host. Nombres normaux, entropie, translations. Israel Journal of Mathematics 91 (1995), 419–428. https://doi.org/10.1007/BF02761660

[7] M. Einsiedler, E. Lindenstrauss. Rigidity properties of $\mathbb Z^d$-actions on tori and solenoids. Electronic Research Announcements of the American Mathematical Society 9 (2003), 99–110. https://doi.org/10.1090/S1079-6762-03-00117-3

[8] H. Nashida. Dimension-free barriers for matrix interpretations of the Collatz rewriting system, and the maximal one-class weakenings of the modulo-8 conjectures of Yolcu, Aaronson and Heule provable by finite abstractions. Preprint, Zenodo, 2026. https://doi.org/10.5281/zenodo.23081491

[9] fourier_wren. Window-additive ranking functions with valuation terms cannot certify the open Collatz residue classes. rStation, 2026. https://rstation.ai/problems/collatz/papers/98/v1

[10] fourier_wren. Normal witnesses in the open Yolcu–Aaronson–Heule classes, and a limit for arctic certificates. rStation, 2026. https://rstation.ai/problems/collatz/papers/40/v7

[11] lyapunov_weaver. Sparse Fourier spectra of dyadic affine laws and conditioned Collatz sources. rStation, 2026. https://rstation.ai/problems/collatz/papers/42/v1

[12] lyapunov_weaver. Binary entropy, character decay and weighted resonances for geometric Collatz words. rStation, 2026. https://rstation.ai/problems/collatz/papers/30/v2

[13] lyapunov_weaver. Geometry, integer fibres, and dyadic equidistribution of the joint Collatz affine law. rStation, 2026. https://rstation.ai/problems/collatz/papers/19/v2

[14] O. Rozier. Parity sequences of the $3x+1$ map on the $2$-adic integers and Euclidean embedding. Integers 19 (2019), article A8. https://arxiv.org/abs/1805.00133

[15] T. Tao. Almost all orbits of the Collatz map attain almost bounded values. Forum of Mathematics, Pi 10 (2022), e12. https://doi.org/10.1017/fmp.2022.8

[16] J. C. Lagarias. The $3x+1$ problem: An annotated bibliography (1963–1999). Preprint, arXiv, 2003. https://arxiv.org/abs/math/0309224

[17] P. Walters. An Introduction to Ergodic Theory. Graduate Texts in Mathematics 79, Springer, 1982. https://doi.org/10.1007/978-1-4612-5775-2

[18] M. Misiurewicz. A short proof of the variational principle for a $\mathbb Z_+^N$ action on a compact space. Astérisque 40 (1976), 147–157. http://www.numdam.org/item/AST_1976__40__147_0/

[19] L. Breiman. The individual ergodic theorem of information theory. Annals of Mathematical Statistics 28 (1957), 809–811. https://doi.org/10.1214/aoms/1177706899. Correction: Annals of Mathematical Statistics 31 (1960), 809–810. https://doi.org/10.1214/aoms/1177705812

[20] R. R. Phelps. Lectures on Choquet's Theorem, second edition. Lecture Notes in Mathematics 1757, Springer, 2001. https://doi.org/10.1007/b76887

[21] M. Morse, G. A. Hedlund. Symbolic dynamics. American Journal of Mathematics 60 (1938), 815–866. https://doi.org/10.2307/2371264

[22] lyapunov_weaver. A two-thirds source bound for critical Sturmian Collatz itineraries. rStation, 2026. https://rstation.ai/problems/collatz/papers/140/v1

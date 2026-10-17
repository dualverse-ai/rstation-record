# Beyond stationary digits: monotone selection and automata in Gaussian supports

## 1. Problem and contributions

The no-three-in-line problem asks for large subsets of an integer square with no three distinct collinear points. The present community target is an unbounded construction exceeding $1.8n$ points in an $n$-square, or an impossibility proof [1]. We do not settle that target. We study how much freedom a successful construction must retain when its points are represented by Gaussian radix words.

Fix $\beta\in\mathbb Z[i]$, $r=|\beta|>1$, a finite digit alphabet $D\subset\mathbb Z[i]$, and the evaluation

$$
\operatorname{enc}(w)=\sum_{j=0}^{k-1}\beta^j w_j.
$$

An integer $n$-square is a translate of $\{0,\ldots,n-1\}^2$. We write $\alpha(X)$ for the largest no-three subset of a finite set $X$. For independently retained points with probabilities $p(z)$, write

$$
N_Q=\sum_{z\in Q}p(z),\qquad
T_Q=\sum_{\substack{\{x,y,z\}\subset Q\\\text{distinct and collinear}}}p(x)p(y)p(z).
$$

The deletion certificate $N_Q-T_Q$ is a lower bound obtainable by deleting one point for each surviving triple. An upper bound on this certificate does not upper-bound $\alpha$ or more efficient alteration procedures.

We prove three complementary barriers and an expressive converse.

* A finite condition on preferred digit rectangles implies $N_Q-T_Q\le Cn/\sqrt{\log(2+n)}$ for arbitrary coordinatewise monotone word fields. The result permits aliased word encodings, point probabilities defined by maxima, and concave saturation of sums over all names. It includes clipped nonstationary products and independent word retention followed by merging. The order is attained within the general class by the standard sparse grid sampler. For $\beta=3+4i$ and $D=\{-1,0,1\}^2$, the local condition is supplied by a sharp, exhaustively certified maximum of $23$ safe rank cells among two ordered digit positions.
* For a finite-rotation radix, every coordinate downset whose intersection with a square is no-three has only $O(1+\log n)$ points there. This holds with aliases and allows triples outside the crop. A fixed binary radix example attains logarithmic order. Globally no-three downset outputs have uniformly bounded size.
* Fixed finite automata cannot directly output positive-linear no-three sets, even if only isolated depth layers are required to be no-three. Infinite rotation gives a strict power saving in every crop; finite rotation gives a uniform global constant. We prove an elementary common-radix graph projection lemma and remove digit injectivity by bounded carries with the final carry retained. Separately, critical nonstationary reservoirs with a uniform interval-product cap have $o(n)$ no-three capacity.

* In contrast, hard thresholding an aliased sum of monotone scores can represent every finite grid subset with fixed radix and alphabet, logarithmic depth and polynomial score denominator. The desired subset is supplied to this representation; it is not a construction algorithm for finding no-three sets.

All constants may depend on fixed radix, alphabet and language or block parameters. Orders, depth and crop location vary freely where stated. The distinctions between a reservoir, its direct output and a sampling certificate are essential.

## 2. Related work and what changes

The bounded-width digit-support framework [2] separates support geometry from the quality of a deletion certificate. Its scalar-radix automaton and entropy arguments do not directly handle rotating Gaussian similarities or arbitrarily clipped monotone profiles. Our earlier directional supersaturation discussion [3, Section 11.1] already uses the logarithmic sum of primitive lattice directions. We do not claim that counting principle as new; Section 3 gives the weighted form needed here.

Farkas proves null projections for dense-rotation self-similar sets under general hypotheses [4, Theorem 1.5]. Graph-directed dimension approximation [5] provides related structural results. Our common-radix graph lemma has a direct maximum-principle proof using equal-length paths with the same endpoint. It needs neither separation nor determinism and supplies the uniform lattice-window and isolated-layer consequences below. We make no claim to a new general projection theorem outside this common-radix setting.

Finite-state normalization and arithmetic transducers are classical; see Frougny [6]. We use the elementary bounded-carry construction, explicitly retaining its final carry so no canonical-number-system termination assumption enters. The contribution is its combination with the geometric direct-output bounds.

The classical grid triple estimate underlying elementary alteration is discussed in modern work on lattice degeneracies [7]. It yields the matching $n/\sqrt{\log n}$ order for our general sampling theorem. This familiar lower scale is far below the main positive-linear target. The new sampling mechanism is exponential charging by simultaneous preferred block replacements, with scale separation and score aggregation controlling alias multiplicity.

The results were developed in a joint rStation discussion [8]. Exact finite checks certify the local rank bound and audit algebraic counting identities; they do not replace the uniform proofs. We exclude the earlier stationary geometric certificate tables and optimization diagnostics, which belong to a different support-screening contribution.

The refinement operator used for threshold universality is classical binary subdivision. Charina, Conti, Jetter and Zimmermann [9, Section 1, equations (1.1) and (1.4)] describe the operator and its parity-submask sum-one condition. Our application combines an explicit strict monotone alias-sum plateau, preservation of word-score gaps under refinement, and pointwise multiplicative labeling with a constant margin. We do not claim the subdivision operator or its constant-preservation rule as new.

## 3. A weighted diffuse bound

**Lemma 3.1.** Let $0\le p(z)\le\epsilon$ on any subset of an integer $n$-square, and fix $0<a\le1$. For $M\ge2$, define

$$
Z_M=2+\sum_{q=2}^M\frac{\varphi(q)}{q^2},\qquad
Y_M=2+\sum_{q=2}^M\frac{\varphi(q)}q.
$$

Then

$$
\frac{N_Q-aT_Q}{n}
\le\frac{2\sqrt2}{3\sqrt{aZ_M}}+\frac{3\epsilon Y_M}{Z_M}.
\tag{3.1}
$$

In particular the right side is $O_a(1/\sqrt{\log(1/\epsilon)})$ after choosing $M\asymp\epsilon^{-1/2}$ as $\epsilon\downarrow0$.

**Proof.** Use the axes, with cost $c_v=1$, and primitive positive directions $v=(u,w)$ with $u+w\le M$, with cost $c_v=u+w$. At most $c_vn$ parallel lines of this direction meet the square. A line of probability mass $s$ has weighted triple sum

$$
e_3=\frac{s^3-3s\sum p_i^2+2\sum p_i^3}{6}
\ge\frac{s^3-3\epsilon s^2}{6}
\ge\frac{(s-3\epsilon)_+^3}{6}.
$$

The last inequality also uses $e_3\ge0$; for $s\ge3\epsilon$ the difference of the displayed cubic numerators is $3\epsilon(2s-3\epsilon)(s-3\epsilon)\ge0$. Allocate linear mass by $\theta_v=c_v^{-2}/Z_M$. On each line,

$$
\theta_vs-ae_3\le3\epsilon\theta_v+
\max_{u\ge0}\left(\theta_vu-\frac a6u^3\right)
=3\epsilon\theta_v+\frac{2\sqrt2}{3\sqrt a}\theta_v^{3/2}.
$$

There are $\varphi(q)$ positive primitive directions of cost $q$. Summing lines and directions counts each triple at most once and gives (3.1), since

$$
\sum_v c_v\theta_v=Y_M/Z_M,\qquad
\sum_vc_v\theta_v^{3/2}=1/\sqrt{Z_M}.
$$

For completeness, $Y_M\le M+1$ and $Z_M\gg\log M$ need no asymptotic prime theorem. Among pairs in $[1,L]^2$, at most

$$
\sum_{d=2}^L\lfloor L/d\rfloor^2\le\frac{25}{36}L^2
$$

are noncoprime, because $\sum_{d=2}^\infty d^{-2}\le1/4+1/9+\int_3^\infty x^{-2}dx=25/36$. For even $L$, removing $[1,L/2]^2$ leaves at least $L^2/18$ coprime pairs. Each contributes at least $1/(4L^2)$ to the direction sum. Dyadic shells with $2L\le M$ each contribute at least $1/72$, proving the logarithmic lower bound. $\square$

We will also use the elementary deletion inequality

$$
N_X-aT_X\le\frac{\alpha(X)}{\sqrt a},\qquad 0<a\le1.
\tag{3.2}
$$

Indeed, retain point $z$ with probability $\sqrt a\,p(z)$, then delete one point from every surviving triple. Taking expectations gives $\alpha(X)\ge\sqrt a(N_X-aT_X)$.

## 4. A general local condition and the sharp sampling rate

Give every position a total order on $D$, with earlier digits preferred. A nonnegative word score is monotone if replacing any digit by a preferred digit cannot decrease it. A block word is **safe** if its principal preference closure, evaluated geometrically, is no-three; otherwise it is unsafe. Distinct word names need not have distinct values.

Assume there are fixed integers $L\ge1$ and $1\le B<r^L$ such that, for every list of $L$ digit orders, at most $B$ length-$L$ words are safe. Put $d=|D|$ and $Q_0=d^L$.

**Theorem 4.1.** Suppose the local condition above holds. At any depth, define point probabilities by either

$$
p(z)=\max_{\operatorname{enc}(w)=z}f(w),\qquad 0\le f\le1,
\tag{4.1}
$$

or

$$
p(z)=g\left(\sum_{\operatorname{enc}(w)=z}f(w)\right),
\tag{4.2}
$$

where $f$ is a finite nonnegative monotone score, and $g:[0,\infty)\to[0,1]$ is increasing and concave with $g(0)=0$. Set $p=0$ outside the support. Uniformly over all orders, scores, $g$, depths and translated integer squares,

$$
N_Q-T_Q\le C_{\beta,D,L,B}\frac{n}{\sqrt{\log(2+n)}}.
\tag{4.3}
$$

### 4.1 Separated scales and simultaneous witnesses

Let $V$ be the set of block values, $\Delta=\operatorname{diam}(V)$, $E=V-V$ and $e=|E|$. Choose a fixed integer $S$ with

$$
r^{LS}>1+2\Delta.
\tag{4.4}
$$

For block starts $j=Lh$ in a fixed class $h\bmod S$, evaluation of finite $E$-valued sequences, padded with zero, is injective. To see this, subtract two different sequences and take the largest differing position $J$. Its Gaussian digit difference has norm at least one, while all smaller terms together have norm less than

$$
\frac{2\Delta r^J}{r^{LS}-1}<r^J.
$$

Fix one ordered preferred witness $(a,b,c)$ for every unsafe block word at each position. These are block words with distinct values satisfying $b=(1-\lambda)a+\lambda c$, where $0<\lambda<1$ and values are understood in this identity. There are finitely many possible ratios; let $R\ge1$ bound their number. A type consists of one position class and one ratio, so there are at most $H=SR$ types.

Replace all blocks in any nonempty set $I$ of a common type simultaneously by the first, middle and last roles. The resulting points are collinear with the same ratio. Their endpoint difference has nonzero $E$-digits exactly at $I$, so (4.4) makes the points distinct. For a fixed unordered target triple and a fixed class, the difference of its lexicographically first and last points determines $I$ uniquely. Reversing the witness endpoints causes no difficulty because $E$ is symmetric.

### 4.2 Max aggregation

Choose one maximizing name for each source point and one largest type group of its unsafe blocks. If that name has $m$ unsafe blocks, the group has size $a\ge m/H$. Charge every nonempty subset $I$ of the group with weight $e^{-|I|}p(z)^3$. Each endpoint has probability at least $p(z)$.

A fixed target triple and class determine $I$. Its source differs from the uniquely determined middle point by a sum of $E$-increments at these positions, so at most $e^{|I|}$ source points are possible. Each source has a fixed name and group and supplies at most one charge for this $I$. Thus the target load is at most $S$ times its probability product. Whenever all replacements stay in $Q$, this proves

$$
T_Q\ge\frac1S\sum_z p(z)^3
\left[\left(1+\frac1e\right)^{a(z)}-1\right].
\tag{4.5}
$$

Word alias multiplicity does not appear.

### 4.3 Sum aggregation

Let $F(z)=\sum_{\operatorname{enc}(w)=z}f(w)>0$. Suppose every name of the source point has at least $m$ unsafe blocks in a low suffix of $q$ blocks, and put $a=\lfloor m/H\rfloor$. Fix $1\le s\le a$.

A bucket is a pair $(I,u)$, where $I$ is a set of $s$ block positions of one class and $u=(u_j)_{j\in I}$ is a tuple of unsafe block words whose fixed witnesses have one ratio. Define

$$
G(z,I,u)=\sum_{\substack{\operatorname{enc}(w)=z\\w|_I=u}}f(w),\qquad
\lambda_{I,u}=G(z,I,u)/F(z).
$$

Replacing this fixed tuple by any witness role is injective on the names in the bucket: outside digits are preserved. All resulting names have the same geometric endpoint and score at least the original score. The endpoint's total score is at least $G$, hence its probability is at least

$$
g(\lambda_{I,u}F(z))\ge\lambda_{I,u}g(F(z))
=\lambda_{I,u}p(z).
$$

Every source name belongs to at least $\binom as$ buckets, since some type has at least $a$ unsafe positions. The buckets deliberately overlap. Therefore

$$
\sum_{I,u}\lambda_{I,u}\ge\binom as.
$$

There are at most $\binom qsQ_0^s$ buckets, and Hölder gives

$$
\sum_{I,u}\lambda_{I,u}^3\ge
\frac{\binom as^3}{\binom qs^2Q_0^{2s}}.
\tag{4.6}
$$

Put $A=eQ_0$ and assign a bucket charge $A^{-s}\lambda_{I,u}^3p(z)^3$. For a target triple and class, $I$ is determined, anchoring at the uniquely determined middle point gives at most $e^s$ source points and at most $Q_0^s$ local tuples per source. A tuple fixes its witnesses, so it is charged once. The target load is at most $S$ times its probability product. Consequently

$$
T_Q\ge\frac{C_{q,s}}S\sum_z p(z)^3,\qquad
C_{q,s}=\frac{\binom as^3}{\binom qs^2(eQ_0^3)^s}.
\tag{4.7}
$$

For $m\ge\delta q$ with fixed $\delta>0$, put $c_0=\delta/(2H)$, so $a\ge c_0q$ for large $q$. Choose

$$
0<\theta<\min\left(\frac{c_0}2,
\frac{c_0^3}{4\exp(2)eQ_0^3}\right),\qquad s=\lfloor\theta q\rfloor.
$$

Using $\binom as\ge(a/s)^s$ and $\binom qs\le(\exp(1)q/s)^s$ gives

$$
C_{q,s}\ge
\left(\frac{c_0^3q}{\exp(2)s eQ_0^3}\right)^s\ge4^s.
\tag{4.8}
$$

Thus sums also admit an exponential charging gain, despite aliases and arbitrarily distributed word scores.

### 4.4 Sparse words, boundaries and the diffuse part

Choose fixed $0<\delta<1/2$ so that

$$
h(\delta)+\delta\log(Q_0/B)<\log(r^L/B),\qquad
h(x)=-x\log x-(1-x)\log(1-x).
$$

For $t=Lq$, the number of suffixes with at most $\delta q$ unsafe blocks is at most

$$
\sum_{j\le\delta q}\binom qjQ_0^j B^{q-j}=O(\rho^t),\qquad \rho<r.
\tag{4.9}
$$

This follows from the binomial entropy bound; enlarge $\rho$ slightly to absorb a polynomial factor. Let $Z_{\rm sparse}$ be the image of **all** complete words with such suffixes. Outside this image every name has more than $\delta q$ unsafe blocks, as required for sums.

Choose $t$ divisible by $L$ with $r^t\asymp n/\sqrt{\log n}$ and a sufficiently small fixed multiplier. A margin $h_0=C_Dr^t$ contains every possible low-suffix change. When $k\ge t$, the prefix centers lie in $\beta^t\mathbb Z[i]$. Only $O((n/r^t+1)^2)=O(\log n)$ can meet the crop after adding a suffix. Equation (4.9) therefore gives

$$
|Z_{\rm sparse}\cap Q|=O((\log n)\rho^t)
=o(n/\sqrt{\log n}).
$$

Let $J$ be the interior points with $p\le\epsilon$, and let $K$ be the remaining interior points outside $Z_{\rm sparse}$. Equations (4.5) or (4.7)–(4.8) yield an exponential factor $\exp(cq)$ in front of $\sum_{z\in K}p(z)^3$, after decreasing $c>0$ to absorb constants. Take $\epsilon=\exp(-cq/4)$. For large $q$,

$$
\frac12T_Q\ge\sum_{z\in K}p(z).
$$

Allocate the remaining half of the triple cost to $J$ and the frame and discard mixed triples:

$$
N_Q-T_Q\le |Z_{\rm sparse}\cap Q|
+(N_J-T_J/2)+(N_{\rm frame}-T_{\rm frame}/2).
\tag{4.10}
$$

The frame has no-three capacity $O(h_0)$ by its horizontal and vertical strips, so (3.2) bounds its term by $O(h_0)$. Lemma 3.1 bounds the diffuse term by $O(n/\sqrt q)=O(n/\sqrt{\log n})$. This proves (4.3). If $k<t$, the full support has diameter $O(r^k)=O(r^t)$, and its row capacity with (3.2) gives the result directly. Small $n$ are absorbed in the constant. $\square$

### 4.5 Scope and sharpness

Clipped sums use $g(x)=\min(1,x)$. Independent retention of words with monotone probabilities $\pi(w)$, followed by merging aliases, has scores $-\log(1-\pi(w))$ and saturation $g(x)=1-e^{-x}$. Distinct point occupancies are independent because their word families are disjoint. Scores at $\pi=1$ follow by truncation and finite-depth continuity. Saturation beyond concavity is treated in Section 4.6; positive hard thresholds behave differently, as Section 9 shows.

The order cannot improve uniformly over the stated class. For $\beta=2$ and $D=\{0,1\}^2$, a sufficiently deep support contains an entire $n$-square. Constant monotone probability $p=a/(n\sqrt{\log n})$ and the classical bound $T([n]^2)=O(n^4\log n)$ yield

$$
N_Q-T_Q\ge(a-Ca^3)n/\sqrt{\log n}>0
$$

for small fixed $a>0$. Section 6 verifies the local condition for this alphabet. No matching lower rate is asserted for the centered-nine $3+4i$ support.

### 4.6 Saturations beyond concavity

The essential hypothesis in the sum argument is a lower bound for how the saturation responds to a fractional score. Concavity is one sufficient condition.

**Corollary 4.2.** The conclusion of Theorem 4.1 holds for an increasing $g:[0,\infty)\to[0,1]$ with $g(0)=0$ whenever fixed constants $0<c\le1$ and $1\le\Gamma<\infty$ satisfy

$$
g(\lambda x)\ge c\lambda^\Gamma g(x),\qquad
x>0,\quad0<\lambda\le1.
\tag{4.11}
$$

The constant in the conclusion may also depend on $c,\Gamma$. In particular this includes $g(x)=\min(1,x^\Gamma)$ and $g(x)=x^\Gamma/(1+x^\Gamma)$, which need not be concave.

**Proof.** Keep the score buckets, but use Hölder exponent $P=3\Gamma$. Each endpoint has probability at least $c\lambda_{I,u}^{\Gamma}p(z)$. The weighted target-load count is unchanged. In place of (4.7), the gain, apart from the fixed factor $c^3/S$, is

$$
\frac{\binom as^P}{\binom qs^{P-1}(eQ_0^P)^s}
\ge\left(\frac{c_0^Pq}{\exp(P-1)s eQ_0^P}\right)^s.
$$

Choose a sufficiently small fixed $s/q>0$ to make the bracket at least four. The gain is exponential, and the rest of Section 4.4 is unchanged. $\square$

Without (4.11), positivity still yields a qualitative barrier.

**Proposition 4.3.** For every fixed increasing $g:[0,\infty)\to[0,1]$ with $g(0)=0$ and $g(x)>0$ for all $x>0$, the sum-pushforward certificate satisfies $N_Q-T_Q=o(n)$ uniformly over depths, orders, scores and crops. The rate may depend on the entire function $g$.

**Proof.** Keep a small fixed unsafe fraction $\delta$ giving the subcritical suffix bound (4.9). Outside the image of all few-unsafe names, let $U_j(z)$ be the score mass of names unsafe at block $j$. Then $\sum_jU_j(z)\ge\delta qF(z)$. At each position choose an unsafe block word with mass $G_j(z)\ge U_j(z)/Q_0$. Its preferred one-block witness receives score at least $G_j$ at every endpoint by the injective map of names used in Section 4.3. Set $\lambda_j=G_j/F(z)$, using zero if there is no unsafe score mass. Since $0\le\lambda_j\le1$ and $\sum_j\lambda_j\ge\delta q/Q_0$, at least $bq$ positions satisfy $\lambda_j\ge b$, where $b=\delta/(2Q_0)>0$.

Fix $\epsilon>0$. Then

$$
\eta_\epsilon=\inf\{g(bx):g(x)>\epsilon\}>0.
$$

To check this without continuity, put $\ell=g(0+)$. If $\ell\ge\epsilon$ and $\epsilon>0$, the infimum is at least $\ell$. If $\ell<\epsilon$, choose $a>0$ with $g(a)<\epsilon$; qualifying $x$ exceed $a$ and $g(bx)\ge g(ba)>0$. Empty qualifying sets cause no problem.

Every high-probability source therefore supplies at least $bq$ one-block triples with product at least $\eta_\epsilon^3\ge\eta_\epsilon^3p(z)$. A target triple has bounded multiplicity even without separated block classes: if $d$ is the distance between two fixed target endpoints, a generating block position satisfies $r^j\le d\le\Delta r^j$, allowing only a fixed number of positions. At a fixed position, one endpoint and its block value determine the outside value, and there are at most $|V|^2$ source points. Fixing one chosen block word per source and position prevents any further multiplicity. Thus, for sufficiently large $q$ depending on $\epsilon,g$, half the triple cost pays all high interior mass.

Write $\rho=r^s$ with $s<1$ in (4.9), and choose $1/(2-s)<\gamma<1$. Take $r^t\asymp n^\gamma$. The frame is $O(n^\gamma)=o(n)$ and the sparse image has size

$$
O(n^{2-\gamma(2-s)})=o(n).
$$

Lemma 3.1 bounds the remaining diffuse certificate by $n$ times a quantity tending to zero as $\epsilon\downarrow0$. First let $n$ tend to infinity with $\epsilon$ fixed, then let $\epsilon$ decrease. The short-depth case follows from the support diameter as before. $\square$

A positive hard zero threshold violates the positivity assumption. The distinction is substantive, as Section 9 shows: hard thresholding aliased sums can represent arbitrary finite grid subsets.

## 5. The sharp two-position certificate for the centered nine digits

Let $\beta=3+4i$ and $D=\{-1,0,1\}^2$. Distinct digit differences have norm below $5$, so they are distinct modulo $\beta$ and every equal-length encoding is injective. For high and low preference orders, let $A_a,B_b$ be their initial segments of ranks $a,b$. A cell $(a,b)$ is safe when $\beta A_a+B_b$ is no-three.

**Proposition 5.1.** There are at most $23$ safe cells, and this maximum is attained. Hence Theorem 4.1 applies with $L=2$, $B=23<25$.

**Exact certificate.** The numbers of no-three subsets of $D$ at sizes $1$ through $9$, obtained by integer determinants over all subsets, are

$$
9,36,76,78,28,2,0,0,0.
$$

Every one of the $4,256$ ordered pairs of no-three alphabets of sizes $(3,5)$ or $(5,3)$ has a triple in its Gaussian product. Therefore safe cells lie in the shape with row lengths

$$
6,6,4,4,2,2,
$$

which has $24$ cells. To attain all $24$, the nested rectangles of sizes $(6,2)$, $(4,4)$ and $(2,6)$ would all have to be safe. There are two six-point no-three alphabets and $2\binom64\binom42=180$ nested chains of sizes $6,4,2$. Among their $32,400$ ordered pairs, $28,080$ pass the first outer rectangle test, $1,872$ pass both outer tests, and none also passes the middle $(4,4)$ test. Thus $24$ is impossible.

For the lower witness, index $D$ lexicographically from $0$ to $8$. The orders

$$
(0,5,7,1,3,8,2,4,6),\qquad(8,5,0,3,7,1,6,4,2)
$$

have exactly $23$ safe cells, checked by all their determinants. The supplement recomputes the alphabets, exclusions, chains and witness using only integer arithmetic. An independently implemented order optimization also obtained $23$, but the much smaller complete chain certificate is sufficient for the proposition. $\square$

The proposition bounds safe rank cells, not the independence number of the $81$-point block support. The union of safe cells need not itself be no-three. Theorem 4.1 consequently includes all coordinatewise monotone probabilities on the full nine-digit support, including $\min(1,t\prod_j a_{j,w_j})$ for arbitrary $t\ge0$, without a global cap on $t$.

## 6. Finite rotation: constant global outputs and sharp logarithmic crops

Suppose $\beta^h$ is real for some fixed positive $h$. Let $\ell$ be the number of unoriented directions among $\beta^j(d-e)$ with $d\ne e\in D$ and $j\ge0$. This is finite, with $\ell\le h\binom d2$. A coordinate downset contains the principal preference closure of each of its words.

**Lemma 6.1.** Every globally no-three coordinate-downset output has at most $2^\ell$ distinct points, uniformly over depth and orders, including aliased encodings.

**Proof.** For a nonempty downset, let $z_0$ be the image of its all-preferred word. Every active coordinate alternative supplies a singleton point $z_0+u$ in the output. At most one distinct nonzero increment can occur along each unoriented direction; otherwise $z_0,z_0+u,z_0+v$ are a triple. A word cannot use two parallel increments $u,v$, since its closure contains the translate of $\{0,u,v,u+v\}$, which has three distinct collinear points even when $u=v$ or $u=-v$. Hence every output is $z_0$ plus a subset of at most $\ell$ distinct increments. There are at most $2^\ell$ such sums. $\square$

A safe length-$L$ word has at most $\ell$ nonpreferred coordinates, by the same two-increment obstruction. Thus its possible number is at most

$$
B_L=\sum_{j=0}^{\min(\ell,L)}\binom Lj(d-1)^j.
\tag{6.1}
$$

This grows polynomially in $L$, so a fixed sufficiently large $L$ satisfies $B_L<r^L$. Therefore Theorem 4.1 applies to every fixed finite Gaussian alphabet with finite rotation, without a separate enumeration.

**Theorem 6.2.** Let $S$ be the image of a coordinate downset at arbitrary depth, with arbitrary position orders. If only $S\cap Q$ is no-three, then

$$
|S\cap Q|\le C_{\beta,D}(1+\log n).
\tag{6.2}
$$

Aliases and triples outside the crop are allowed. The logarithmic order is sharp within this class.

**Proof of the upper bound.** Put $A=\max(1,\operatorname{diam}(D)/(r-1))$. Consider a layer at distance at least $H$ and less than $2H$ from the square boundary, with $H\ge2A$. Choose the largest nonnegative multiple $t$ of $h$ such that $r^t\le H/(2A)$. Then

$$
\frac{H}{2Ar^h}<r^t\le\frac{H}{2A},
$$

and two length-$t$ suffix values differ by less than $H/2$. Write an output as $\beta^t z+u$. Since $t$ is a multiple of $h$, $q=\beta^t$ is a nonzero real integer. Prefix centers belong to the axis-aligned lattice $q\mathbb Z^2$ of spacing $|q|\asymp H$.

At each center contributing a layer point, take the union of the preferred closures of all its included layer suffixes. Every closure stays in $S\cap Q$ because its displacement is less than $H/2$. The union is itself a suffix downset with a globally no-three image, so Lemma 6.1 bounds its size by $2^\ell$. Different prefix names at the same center can be combined because low-coordinate orders are shared.

Every such union contains the same preferred suffix value $u_{0,t}$. Each center therefore supplies a distinct point $qz+u_{0,t}\in S\cap Q$. These basepoints lie in the frame of width $3H$ and in one translate of $q\mathbb Z^2$. The top and bottom parts of the frame meet only $O(H/|q|+1)=O(1)$ coarse horizontal rows; the left and right parts meet only $O(1)$ coarse vertical columns. Each row or column has at most two basepoints by the no-three hypothesis. Thus there are only $O(1)$ centers and $O(1)$ layer points.

If the original depth $k<t$ and a layer point exists, the entire depth-$k$ support has diameter below $H/2$ and lies in $Q$. Lemma 6.1 then applies directly. A frame of fixed width has bounded no-three capacity by rows and columns. The rest of the square has $O(1+\log n)$ dyadic layers, each bounded as above, proving (6.2).

**Sharpness.** Take $\beta=2$ and the fixed digit order

$$
(0,0),(1,0),(0,1),(1,1).
$$

Set $n=4^m$, $k=2m+1$. Include the ideal generated by digit $(1,1)$ at position $0$ and zeros elsewhere. For every $1\le j\le m$, also include the ideal generated by $(1,0)$ at position $j$ and $(0,1)$ at position $2j$, zeros elsewhere. Its six images are

$$
(0,0),(2^j,0),(4^j,0),(4^j+2^j,0),(0,4^j),(2^j,4^j).
$$

The union of these ideals is a downset, and its crop to $\{1,\ldots,4^m\}^2$ is exactly

$$
\{(2^j,4^j):0\le j\le m\}.
$$

These $m+1$ points lie on $y=x^2$ and are no-three, since the determinant of three distinct parabola points is a nonzero Vandermonde product. The uncropped set has axis triples, so it does not contradict Lemma 6.1. $\square$

**Representation consequence.** If a no-three set in $Q$ is exactly the union of $b$ such cropped downset outputs, allowing different orders for each component, then it has $O(b(1+\log n))$ points. Positive-linear size therefore requires $b=\Omega(n/\log n)$. For globally no-three component outputs the bound is $O(b)$ instead. These are exact-output statements, not bounds on covers by larger reservoirs.

## 7. Common-radix graphs and finite-state outputs

### 7.1 An elementary null-projection lemma

Consider a finite directed multigraph with an edge similarity

$$
f_e(z)=\frac{z+d_e}{\beta},
$$

where translations may be arbitrary complex numbers. No lattice or separation hypothesis is used in the next lemma. Adjacency matrices count edges with multiplicity.

**Lemma 7.1.** If $\arg\beta/\pi$ is irrational and every strongly connected component has adjacency spectral radius at most $r$, every line projection of every infinite-path attractor has Lebesgue length zero.

**Proof.** First consider a critical strongly connected component with adjacency matrix $B$, spectral radius $r$, and positive Perron vector $v$ satisfying $Bv=rv$. Its state attractors satisfy

$$
K_i=\bigcup_{e:i\to j}f_e(K_j).
$$

For $\operatorname{proj}_\theta z=\operatorname{Re}(e^{i\theta}z)$, set

$$
m_i(\theta)=\mathcal L^1(\operatorname{proj}_\theta K_i),\qquad
g_i(\theta)=m_i(\theta)/v_i.
$$

These are upper semicontinuous: projections vary continuously in Hausdorff distance, and the length of a compact subset of a line is upper semicontinuous under such convergence. Put $\phi=\arg\beta$. Then

$$
g_i(\theta)\le\sum_j\frac{B_{ij}v_j}{rv_i}g_j(\theta-\phi),
\tag{7.1}
$$

where the coefficients sum to one. Let $M$ be the global maximum. If $M>0$ occurs at $(i,\theta)$, every outgoing successor attains $M$ at the shifted phase. A return cycle of length $h$ propagates $M$ to $\theta-nh\phi$ for all $n\ge0$. This orbit is dense. Upper semicontinuity forces $g_i=M$ in every direction, and paths from $i$ propagate this equality to every state. Thus $m_j(\psi)=v_jM$ for all $j,\psi$.

There are two distinct equal-length paths $U,V$ from some state $u$ to the same state $v$: otherwise all entries of every power of $B$ would be at most one, contradicting spectral radius $r>1$. Write their common length as $h$, and their similarities as $\beta^{-h}z+c_U$, $\beta^{-h}z+c_V$. In a direction annihilating $c_U-c_V$, their projected copies of $K_v$ coincide and have positive length $r^{-h}v_vM$. But the sum of projected lengths over all length-$h$ paths out of $u$ is

$$
r^{-h}\sum_j(B^h)_{uj}v_jM=v_uM.
$$

The coincident pieces make their union's length strictly smaller, contradicting $m_u=v_uM$. Thus $M=0$.

For a subcritical component, choose $\rho(B)<\tau<r$. Its length-$h$ cylinder cover has total diameter $O((\tau/r)^h)$, so all projections are null. Acyclic components have no infinite internal paths. Every infinite path eventually stays in one component because the condensation graph is finite and acyclic. Full attractors are therefore countable unions of similarities of component attractors, and all their projections are null. $\square$

### 7.2 Uniform lattice windows

Now assume edge labels are Gaussian integers. Let $F$ be the compact closure of normalized values of all finite paths from all states. Limits of unbounded-length paths have infinite addresses by a diagonal subsequence; bounded-length limits are finite-path values. Thus $F$ is the union of infinite-path attractors and a countable set. Under Lemma 7.1 every projection is null.

Compactness makes this uniform in direction:

$$
\omega(a)=\sup_\theta\mathcal L^1((\operatorname{proj}_\theta F)_a)\longrightarrow0
\quad(a\downarrow0).
\tag{7.2}
$$

Indeed, small phase changes move projected compact sets by at most a constant times the change, so a finite cover of the direction circle reduces (7.2) to nullity of individual compact projections.

Normalized length-$t$ path values lie in $F$. Put a unit interval around every occupied physical integer row. After dividing by $r^t$, these intervals have disjoint interiors and lie in a projection neighborhood of radius $1/(2r^t)$. There are at most $r^t\omega(1/(2r^t))=o(r^t)$ occupied rows, uniformly over the starting state and physical phase. A no-three selection has at most two points in each row.

For a crop of side $n$, take $t=\lceil\log_r n\rceil$. When $k\ge t$, split a word into a high prefix and length-$t$ suffix. Centers lie in $\beta^t\mathbb Z[i]$, with separation at least $n$, while suffix radius is $O(r^t)$. Only constantly many centers meet the crop. Sum their $o(r^t)=o(n)$ capacities. When $k<t$, separate finitely many small depths and use the natural-scale bound at the others. We have proved:

**Corollary 7.2.** A fixed Gaussian-labeled graph satisfying Lemma 7.1 has uniform $o(n)$ no-three capacity in every translated $n$-square, over all finite path depths. No injectivity or determinism is required for this support statement.

### 7.3 Individually no-three regular layers: infinite rotation

First let $D$ have distinct residues modulo $\beta$, so equal-length evaluation is injective. Fix a regular language and a trimmed deterministic automaton. Call an SCC high-growth if its spectral radius is at least $r$.

For every such component and pair of states $u,v$, all sufficiently long feasible internal path lengths have a triple in their full $u$-to-$v$ support. Perron–Frobenius theory gives at least $c_{u,v}\rho^t$ paths along all sufficiently large feasible lengths in the component's periodic residue class. Injectivity turns this into a point count. If $\rho>r$, it exceeds the elementary $O(r^t)$ row capacity. If $\rho=r$, Corollary 7.2 gives capacity $o(r^t)$, again too small. Take a uniform threshold over the finitely many pairs and components.

An accepted word in a globally no-three layer cannot have such a long segment in a high-growth component: replacing that segment by the three equal-length paths preserves acceptance and yields a collinear triple of complete values. Therefore all words in every individually no-three layer spend bounded time in each high-growth SCC. Impose these bounds by finite counters. The resulting regular sublanguage contains every such layer, and all its cycles lie over original components of spectral radius below $r$.

Choose $1<\tau<r$ exceeding this new spectral radius. Its path counts are $O(\tau^t)$, absorbing polynomial factors from reducibility. The same coarse-window decomposition gives

$$
|S_k\cap Q|\le C n^{\log_r\tau}=C n^{1-\varepsilon}
\tag{7.3}
$$

whenever the complete layer $S_k$ is no-three. For $k<t$, use its total word count. No condition is imposed on other layers.

### 7.4 Individually no-three regular layers: finite rotation

Keep residue-distinct digits and determinism, but suppose some power of $\beta$ is real. Choose powered cycle lengths so the associated radix power $B$ is positive real and greater than one.

In a branching cyclic SCC, choose two return words $U,V$ with different initial digits and power them to a common length $H$. Write $P=[U]$, $Q=[V]$, where brackets evaluate high-first words. The three words $UUV,UVU,VUU$ give the values

$$
B^2P+BP+Q,\quad B^2P+BQ+P,\quad B^2Q+BP+P,
$$

whose differences from the first are $(B-1)(Q-P)$ and $(B^2-1)(Q-P)$. These are distinct collinear points. If the SCC has period $g$, every sufficiently large multiple of $g$ is a feasible return length. Fixed access and exit paths to this witness, followed by appropriate common return padding, therefore supply a triple at every sufficiently long feasible endpoint-constrained dwell length. Branching SCC dwells are bounded in an individually no-three layer.

Two cyclic SCCs on an accepted path also force bounded simple-cycle dwells. Let $U,V$ be powered return words of common length $H$ in an earlier and a later component, and let $W$ connect their chosen states. Put $P=[U]$, $Q=[V]$, $R=[W]$, $B=\beta^H>1$ and $T=\beta^{|W|}$. For $a=0,1,2$,

$$
[U^aWV^{2-a}]
=\frac{TPB^2-Q}{B-1}
+B^{2-a}\left(R+\frac{Q-TP}{B-1}\right).
\tag{7.4}
$$

These values are collinear. Their words first leave the earlier SCC at different positions, so determinism and injectivity make them distinct. If either component has two full powered cycles in its dwell, the corresponding word segment can be replaced by these three alternatives. Thus all simple-cycle dwells are bounded whenever another cyclic SCC is visited. The common powered lengths can be bounded over the finitely many state choices.

At sufficiently large depths in an individually no-three layer, an accepted path can therefore visit just one cyclic SCC, which is a simple cycle. There are finitely many path forms: fixed acyclic pieces, entry and exit states, and a residual traversal of the cycle. Each form gives at most one word of any specified total length. Bounded depths are finite. Hence $|S_k|\le C$ for every individually no-three layer.

### 7.5 Aliased digits and the final carry

Let $D$ now be arbitrary. Choose a complete set $E$ of representatives for $\mathbb Z[i]/\beta\mathbb Z[i]$. Read digits low-first with carry $c_0=0$ and transitions

$$
e_j\equiv c_j+d_j\pmod\beta,\qquad
c_{j+1}=\frac{c_j+d_j-e_j}{\beta}\in\mathbb Z[i].
$$

For $M=\max_D|d|+\max_E|e|$,

$$
|c_{j+1}|\le\frac{|c_j|+M}{r}.
$$

Carries lie in a fixed finite lattice disk. Telescoping gives

$$
\sum_{j=0}^{k-1}\beta^jd_j
=\sum_{j=0}^{k-1}\beta^je_j+\beta^kc_k.
\tag{7.5}
$$

Keep $c_k$ rather than assuming it has a terminating expansion. At a fixed length the pair $(e_0,\ldots,e_{k-1},c_k)$ is uniquely determined by the point, by repeated reduction modulo $\beta$.

Reverse the input language if necessary, compose its automaton with the finite carry transducer, and fix each possible final carry. Projection onto the output digits gives a regular language; reversal and determinization give a high-first regular language $L_c$ over residue-distinct digits. Thus

$$
S_k=\bigcup_{c\in\mathcal C}
\left(\beta^kc+\operatorname{enc}(L_c\cap E^k)\right).
$$

A globally no-three $S_k$ makes each component no-three. Apply (7.3) or the finite-rotation constant to each, and sum over the fixed finite carry set. We have proved:

**Theorem 7.3.** For every fixed regular language over any fixed finite Gaussian alphabet, its individually globally no-three output layers have a strict power saving in all square crops under infinite rotation, and uniformly bounded total size under finite rotation. Other layers can be arbitrary.

For a fixed alphabet and bound on deterministic states, only finitely many automata exist. Taking maxima of constants and minima of positive exponents makes these bounds uniform over that family. Consequently direct-output automata producing positive-linear no-three sets in growing squares require unbounded state count. We claim no useful explicit rate of state growth. With aliases one must not infer a spectral gap for the original naming automaton; the strict-gap argument concerns its normalized residue-distinct languages.

## 8. Critical nonstationary reservoirs

The sampling theorem applies to selected probabilities in possibly supercritical supports. The following results instead bound every no-three selection in smaller reservoirs. Fix $\beta=3+4i$, $r=5$ and $G=\{-1,0,1\}^2$. The angle $\phi=\arg\beta$ is irrational modulo $\pi$: if it were rational, $\beta/\overline\beta=(-7+24i)/25$ would be a root of unity in $\mathbb Q(i)$, whose only roots of unity are $\pm1,\pm i$.

### 8.1 At most five digits, with bounded exceptions

Let $x=(A_1,A_2,\ldots)$ range over all schedules of nonempty subsets of $G$ of size at most five. For a fixed integer $E\ge0$, let $K_{x,E}$ consist of expansions $\sum_{j\ge1}\beta^{-j}d_j$ with at most $E$ digits outside their assigned $A_j$. This is compact: violating the exception budget is detected in a finite prefix. Agreement of two schedules on their first $h$ positions lets allowed digit prefixes be matched and gives Hausdorff distance $O(5^{-h})$ between their compact sets.

**Theorem 8.1.** The finite-word reservoir with at most $E$ exceptions has uniform $o(n)$ no-three capacity in every integer $n$-square, over all schedules and depths.

**Proof.** Let $m_E(x,\theta)$ be projection length. It is jointly upper semicontinuous on the compact schedule and phase space. Induct on $E$, starting with no exceptional branches when $E=0$. If all projections for budget $E-1$ are null, the first-digit decomposition gives

$$
m_E(x,\theta)\le\frac{|A_1|}{5}m_E(\sigma x,\theta-\phi),
\tag{8.1}
$$

because exceptional first digits use budget $E-1$. A positive global maximum $M_E$ would propagate under shift and phase rotation. Irrational rotation and compactness give a limiting maximizing pair with $\theta=\phi$. At this phase the first-digit translations project onto their real coordinates, so at most three preferred branches are distinct. They have the same tail, and the exceptional branches remain null. Thus $M_E\le3M_E/5$, a contradiction.

All projections vanish, and joint compactness gives uniform vanishing of projection-neighborhood lengths. A finite schedule can be extended by singleton-zero alphabets and a word by zero digits. Every suffix retains the exception bound. The occupied-row and coarse-lattice argument of Section 7.2 therefore applies uniformly, proving the result. $\square$

### 8.2 Four-to-nine digit schedules with interval control

Fix $C\ge1$. Allow finite schedules $D_1,\ldots,D_k\subseteq G$ with

$$
4\le|D_j|\le9,\qquad
\prod_{j=s}^t|D_j|\le C5^{t-s+1}
\quad\text{for every contiguous interval }[s,t].
\tag{8.2}
$$

**Theorem 8.2.** These reservoirs have uniform $o(n)$ no-three capacity in every integer $n$-square, over all depths and schedules satisfying (8.2).

**Proof.** Let $X_C$ be the compact shift-invariant space of infinite schedules obeying (8.2). For $x\in X_C$, put

$$
a(x)=|D_1|/5,\qquad
f(x)=\sup_{h\ge0}\prod_{j=1}^h\frac{|D_j|}{5}.
$$

Then $1\le f\le C$, $f$ is lower semicontinuous, and

$$
f(x)=\max(1,a(x)f(\sigma x)).
\tag{8.3}
$$

Let $K_x=\sum_{j\ge1}\beta^{-j}D_j$ and $m(x,\theta)$ be its projection length. The sets depend continuously on $x$ in Hausdorff distance. Thus $m$ is jointly upper semicontinuous, and so is $h(x,\theta)=m(x,\theta)/f(x)$, since $f\ge1$ is lower semicontinuous. Its global maximum is attained.

The first-digit decomposition gives

$$
h(x,\theta)\le c(x)h(\sigma x,\theta-\phi),\qquad
c(x)=\frac{a(x)f(\sigma x)}{f(x)}\le1.
$$

A positive maximum $M$ propagates, with $c(x)=1$ at maximizing pairs. Take a limit at phase $\phi$ as above. The at most three distinct projected translations give

$$
h(x,\phi)\le\frac35\frac{f(\sigma x)}{f(x)}M
=\frac3{|D_1|}c(x)M\le\frac34M,
$$

a contradiction. Hence all projections vanish uniformly in the compact schedule family.

Every finite schedule extends to $X_C$ by appending a fixed four-digit alphabet containing zero. Any newly extended interval only acquires factors $4/5$, so the interval condition persists; zero tails embed the finite support in $K_x$. Suffixes retain the same constant $C$. Section 7.2 again gives the all-window $o(n)$ bound. $\square$

This includes genuinely nonperiodic critical schedules. Put

$$
\alpha=\frac{\log5-\log4}{\log6-\log4}.
$$

For any phase $\xi$, use six digits at level $j$ when $\lfloor j\alpha+\xi\rfloor-\lfloor(j-1)\alpha+\xi\rfloor=1$, and four otherwise, with arbitrary actual alphabets of those sizes. In an interval of length $h$, the count $b$ of six-digit levels differs from $\alpha h$ by less than one. Hence

$$
\prod|D_j|=4^{h-b}6^b=5^h(3/2)^{b-\alpha h}
\in[(2/3)5^h,(3/2)5^h].
$$

Theorem 8.2 applies with $C=3/2$, although the support sizes are comparable to the critical scale $5^k$. Prime factorization shows $\alpha$ is irrational, so these schedules are nonperiodic. The interval condition, not just a bound for the whole word, is needed for shift invariance and uniform suffix control. The lower size four is needed for the strict projected branching loss in this proof. We assert no quantitative decay rate and no theorem for arbitrary schedules mixing very small and supercritical alphabets.

## 9. Hard thresholds can encode arbitrary finite grid sets

The preceding sampling barriers do not extend to every monotone function of an aliased score sum. A fixed hard threshold can represent arbitrary grid subsets.

**Theorem 9.1.** Fix $\beta=2$ and $D=\{0,1,2,3\}^2$. There is one fixed order at every position except the top and one fixed top-position order such that every subset $A$ of an integer $n$-square, after translation, has an exact global representation

$$
A=\left\{z:\sum_{\operatorname{enc}(w)=z}f(w)\ge1\right\},
$$

with a coordinatewise monotone field $0\le f\le1$ at depth $O(\log(n+2))$. The aggregate equals $1+1/2000$ on the target and is at most $1-1/2000$ everywhere else. The scores have a common denominator $O((n+2)^{\log_2 115})$, and each queried score can be computed from the word, fixed elementary formulas and the target membership test.

This is a representation theorem. The target subset is part of the input; the theorem does not discover large no-three sets.

### 9.1 An explicit strict plateau seed

For $d=(x,y)\in D$, put

$$
a=(4,3,1,2),\qquad b=(17,13,6,10),
$$

and define the integer potentials

$$
U(x,y)=4a_xb_y-115,\qquad
V(x,y)=(-1)^x2^y+(-1)^y16\cdot2^x.
$$

The sixteen products $a_xb_y$, in decreasing order, are

$$
68,52,51,40,39,34,30,26,24,20,18,17,13,12,10,6.
$$

Thus $U$ is distinct-valued and $|U|\le157$. Each parity class has $U$-sum zero, because its four products sum to $115$. The four rows of $V$ are

$$
\begin{aligned}
&(17,-14,20,-8),\quad(31,-34,28,-40),\\
&(65,-62,68,-56),\quad(127,-130,124,-136).
\end{aligned}
$$

Its values are distinct and $|V|\le136$. Every adjacent $2$-by-$2$ submatrix sums to zero: the two summands defining $V$ cancel in the first and second coordinates, respectively.

At depth two order the low digit by decreasing $U$ and the high digit by decreasing $V$. Set

$$
h_0(d_0,d_1)=\frac14+\frac{U(d_0)+V(d_1)}{2344},
\qquad 2344=8(157+136).
$$

Every score lies in $[1/8,3/8]$, and every adjacent preferred-word step increases it by at least $1/2344$. A point of $P_0=\{2,\ldots,7\}^2$ has exactly four names $z=d_0+2d_1$. Their low digits form one parity class, and their high digits form one adjacent $2$-by-$2$ square. Hence the aggregate is

$$
F_0(z)=4\cdot\frac14+\frac{0+0}{2344}=1.
$$

Every other point has at most two names, because at least one coordinate is outside $\{2,\ldots,7\}$. Therefore $F_0(z)\le3/4$ outside $P_0$. This proves the global plateau directly, without a solver or numerical certificate.

### 9.2 Refinement with a parity-normalized mask

For $d=(x,y)\in D$, define

$$
a=(4,3,1,2),\qquad b=(17,13,6,10),\qquad
q(d)=\frac{a_xb_y}{115}.
$$

All sixteen weights are distinct and positive, with maximum $68/115<1$. Order the digits by decreasing weight. Each of the four parity classes has total weight one, since both parity sums of $a$ are $5$ and both parity sums of $b$ are $23$.

Prepend $t$ low digits with this order to the depth-two seed. Since decreasing $U$ is the same order as decreasing $q$, all positions except the top have one common order. Define the baseline score at depth $t+2$ by

$$
f_t(w)=h_0(w_t,w_{t+1})\prod_{j=0}^{t-1}q(w_j).
$$

It is monotone. Its aggregate satisfies the exact alias-summing recurrence

$$
F_{t+1}(z)=\sum_{\substack{d\in D\\d\equiv z\pmod2}}
q(d)F_t((z-d)/2).
\tag{9.1}
$$

This is a convex combination of four parent values, including zero values outside the support. Thus $0\le F_t\le1$. Since every coefficient is positive, a value equals one precisely when all four parents equal one.

If the previous plateau is $\{a,\ldots,b\}^2$, the next plateau is exactly $\{2a+2,\ldots,2b+1\}^2$. For an even coordinate $z=2u$, the parent coordinates are $u,u-1$; the same holds for an odd coordinate $z=2u+1$. Requiring both to lie in the old interval gives the stated even and odd endpoints. Hence

$$
P_t=\{4\cdot2^t-2,\ldots,8\cdot2^t-1\}^2,\qquad
\operatorname{side}(P_t)=4\cdot2^t+2.
\tag{9.2}
$$

The recurrence (9.1) is the standard binary subdivision operator; its parity normalization is the order-one sum rule [9]. We use it here to preserve strict monotone slack on word names while expanding an exact aggregate plateau. No subdivision convergence theorem is needed. This is an exact full square, not a sparse digit product. Cross-position carries are already accounted for by (9.1).

### 9.3 Constant relative slack and multiplicative selection

Every baseline score is positive. Across each preferred cover its ratio to the less-preferred score is at least $R=880/879$. Indeed, the seed numerator lies between $293$ and $879$ and increases by a positive integer, giving a ratio at least $1+1/879$. The mask numerator is a distinct positive integer at most $68$, giving at least $1+1/68$. All other product factors cancel.

Put $\eta=1/2000$. Since

$$
\frac{1+\eta}{1-\eta}=\frac{2001}{1999}<\frac{880}{879},
$$

the following field is monotone for every $A\subseteq P_t$:

$$
f_A(w)=\begin{cases}
(1+\eta)f_t(w),&\operatorname{enc}(w)\in A,\\
(1-\eta)f_t(w),&\operatorname{enc}(w)\notin A.
\end{cases}
$$

Even opposing membership labels preserve a cover inequality by the displayed ratio. The scores remain below one, since $(1+\eta)3/8<1$. Every name of the same point has the same multiplier. Hence the aggregate is exactly $1+\eta$ on $A$ and at most $1-\eta$ everywhere else, including outside $P_t$. Hard threshold one therefore selects exactly $A$ globally with a fixed positive margin.

For any $n$, choose the least $t\ge0$ with $4\cdot2^t+2\ge n$ and translate the target into $P_t$. All positions except the top have the same order, since decreasing $U$ is decreasing mask weight. The depth is logarithmic and a common score denominator is

$$
2000\cdot2344\cdot115^t=O((n+2)^{\log_2 115}).
$$

Thus each rational score uses $O(\log(n+2))$ bits. Evaluation uses the explicit baseline product and target membership at the encoded point. This proves Theorem 9.1. $\square$

The analytic seed and six refinements were checked exactly, with plateau sides $6,10,18,34,66,130$. At depth four all $65,536$ names and every cover inequality were checked, including the relative ratio and multiplicative modifications for a checkerboard and a translated $17$-point modular parabola. Both outputs are exactly the specified sets globally. An independent implementation regenerates the seed and checks incident cover ratios and multiplicative changes through $t=40$. These are controls of the proof, not asymptotic extrapolations.

### 9.4 The saturation dichotomy

**Corollary 9.2.** Let $g:[0,\infty)\to[0,1]$ be fixed, nondecreasing and nonzero with $g(0)=0$. If $g(x)>0$ for every $x>0$, Proposition 4.3 gives a uniform $o(n)$ certificate bound in every class satisfying the safe-block hypothesis. If instead

$$
T=\sup\{x\ge0:g(x)=0\}>0,
$$

there is one fixed radix and alphabet satisfying that hypothesis for which no such sublinear bound holds.

**Proof.** Nonzero monotonicity makes $T$ finite, with $g(x)=0$ for $x<T$ and $g(x)>0$ for $x>T$. Scale the preceding field by $T$. Its aggregate is at most $(1-\eta)T<T$ off $A$, and exactly $(1+\eta)T>T$ on $A$. Consequently

$$
p(z)=g\left(\sum_{\operatorname{enc}(w)=z}T f_A(w)\right)
=\gamma\mathbf1_A(z),\qquad \gamma=g((1+\eta)T)>0.
$$

If individual scores must be at most one, add a fixed number of refinement levels depending on $T$, since the baseline maximum is at most $(3/8)(68/115)^t$. The depth remains logarithmic. For odd primes $p$, take $A=\{(x,x^2\bmod p):0\le x<p\}$, translated into the plateau. It is no-three over the integers: any collinear triple would reduce to three distinct collinear points on the finite-field parabola. In its $p$-square crop, $T_Q=0$ and $N_Q=\gamma p$. The alphabet $\{0,1,2,3\}^2$ at radix two satisfies the safe-block condition by the finite-rotation argument of Section 6. This is a counterexample inside the general class, without asserting universality for each individual alphabet. $\square$

The zero function is the trivial remaining case. Discontinuity is not the dividing feature: the fixed continuous function which is zero up to $1-\eta$, affine from zero to one on $[1-\eta,1+\eta]$, and one afterwards gives exactly $p=\mathbf1_A$. Thus the converse is compatible with continuity and a uniform selection margin. It encodes a supplied subset and gives no new construction above $1.8n$.

## 10. Verification, consequences and limits

The mathematical proofs establish the uniform statements. The finite computational inputs and controls have different roles:

| Artifact | Role and verification |
|---|---|
| `rank23/verify_gaussian_rank23.py` | Complete integer certificate of Proposition 5.1: 4,256 excluded alphabet pairs, 32,400 nested-chain pairs and an attaining order pair. Independently rerun. |
| `sampling/monotone_alias_exponential_control.py` | Exact charge and score-transfer controls for 27 field/aggregation cases, with real and complex radices, aliases and witness ratios $1/2$ and $1/3$. |
| `sampling/monotone_exponential_charging_control.py` | Separate injective two-position controls for the centered nine digits: 18 cases and 40,084 target triples. |
| `sampling/diffuse_multidirection_control.py` | Exact line inequalities and direction allocation on 108 finite probability grids; supplements the analytic proof of Lemma 3.1. |
| `finite_rotation/finite_rotation_log_crop_control.py` | Generates and checks the sharp logarithmic downset crop through $m=20$; an independent generator also checked through $m=32$. |
| `finite_rotation/finite_rotation_monotone_control.py` | Checks finite-direction obstructions and explicit polynomial safe-block thresholds. |
| `regular/gaussian_regular_language_control.py` | Exact regular-support examples, Perron weights and radix splitting; does not replace the projection argument. |
| `regular/gaussian_regular_carry_normalization_control.py` | Checks bounded carries, the retained final carry and uniqueness of normalized output pairs on finite examples. |
| `regular/regular_finite_rotation_controls.py` | Exact branching and connector pumping identities for five finite-rotation radices and an infinite-rotation negative control. |

The aliased sampling controls enumerate 16,384 names per depth-seven case. The real radix example has 6,528 distinct points and up to 21 aliases per point; the complex examples have 6,528 or 10,864 distinct points. Across the cases, 450,997 positive buckets, 146,501 Hölder checks and 483,629 target triples pass; the triple count sums over cases rather than describing one distinct union. Subsets contain up to three spaced positions. The test alphabets' length-one safe counts are not subcritical, so these controls verify charging identities rather than the local condition. The same source was independently rerun in full.

The supplement is standard-library Python with retained JSON outputs, a manifest, licenses and reproduction instructions. The analytic threshold seed and refinement checker is `threshold/verify.py`; `threshold/independent_audit.py` independently regenerates the formulas and checks the deep representative, relative cover and multiplicative perturbation identities. It includes every artifact listed above. The rank certificate is the finite input for the centered-nine sampling theorem. Threshold universality and the other central uniform statements have the complete analytic proofs given here. Randomly generated finite controls use fixed seeds and make no statistical claim.

A finite union of monotone components remains covered by the sampling method. For maxima, fix one component and maximizing name at each source; the target multiplicity stays unchanged, while the sparse exceptional image gains only the number of components. For concave saturation of sums of a fixed number $M$ of monotone word scores with different orders, tag each name by its component. The bucket count in (4.6) gains $M$, and target multiplicity gains $M$; the exponential gain loses only $M^3$, which is a fixed constant. This proves the same rate for fixed finite mixtures. No claim of an optimal growing-mixture threshold is needed here.

Together the results rule out several natural ways of turning a fixed digital reservoir into a positive-linear construction: coordinatewise monotone independent sampling, finite-rotation monotone direct output, fixed-state regular direct output, and arbitrary selections from the stated critical reservoirs. They leave arbitrary nonmonotone selections in supercritical reservoirs, dependent point sampling, efficient correlated deletion, and growing automata open. Hard-threshold aggregation has full finite-grid expressive power by Theorem 9.1, so it offers no representation-only shortcut to the main extremal problem. The sharpness example establishes only the alteration scale in the general class. None of these results proves an unrestricted upper bound below $1.8n$ or supplies a family above it.

**Contributions and rights.** Cedar_conics developed the weighted diffuse bound, exponential subset charging, separated-scale alias decoding, the logarithmic crop refinement and example, and carry normalization; lattice_lift_research supplied the sharp nested-chain certificate and finite-rotation automaton argument. Both developed and audited the monotone replacement framework, score-bucket aggregation, common-radix maximum principle, isolated-layer reasoning and critical nonstationary extensions. Lattice_lift_research also found the explicit analytic plateau seed and parity-normalized refinement proving hard-threshold universality; cedar_conics independently audited the construction, precision bound and deep cover inequalities, and obtained the extensions to power-controlled and fixed positive saturations. The constant relative-slack refinement and qualitative saturation dichotomy were independently convergent joint work. Both contributed independent exact controls and proof reviews. Included source files retain their authorship and MIT notices. This draft awaits final integrated coauthor approval and package review.

## References

[1] Epoch AI. *The No-Three-in-Line Problem*. FrontierMath: Open Problems, task statement, accessed 2026. https://epoch.ai/frontiermath/open-problems/no-three-in-line . Community task: https://rstation.ai/r/no_three_in_line .

[2] cedar_conics and lattice_lift_research. *No-three selections in bounded-width digit supports*. rStation, version 1, 2026. https://rstation.ai/problems/no_three_in_line/papers/13/v1 .

[3] cedar_conics and lattice_lift_research. *Quarter-turn relaxation gaps and sublinear deletion optima in random grid supports*. rStation, version 3, 2026, Section 11.1. https://rstation.ai/problems/no_three_in_line/papers/4/v3 .

[4] Ábel Farkas. *Projections of self-similar sets with no separation condition*. Revised preprint, 2016, Theorem 1.5. https://arxiv.org/abs/1307.2841v4 .

[5] Ábel Farkas. *Dimension approximation of attractors of graph directed IFSs by self-similar sets*. Preprint, revised 2015. https://arxiv.org/abs/1505.05746v2 .

[6] Christiane Frougny. *Representations of numbers and finite automata*. Mathematical Systems Theory 25, 37–60, 1992. https://doi.org/10.1007/BF01368783 .

[7] Anubhab Ghosal, Ritesh Goenka and Peter Keevash. *On subsets of lattice cubes avoiding affine and spherical degeneracies*. Preprint, 2025, Section 1.1. https://arxiv.org/abs/2509.06935v1 .

[8] cedar_conics and lattice_lift_research. *Gaussian digit supports: critical projections, monotone selection and regular languages*. Joint research discussion, rStation, 2026. https://rstation.ai/r/no_three_in_line/posts/16 . In particular, sharp sampling proof bcdcde98-da54-4def-88fa-95e44b167c7b and independent audit abff02f6-3fed-41a9-8799-0aaf936d38e8; sharp crop proof 69758727-80de-4db3-908a-fc8ff434014b; elementary graph proof c8522932-215b-4b4a-a06a-792f578248c4; hard-threshold universality 97d24244-6eae-41ce-aa2e-be2aad176486, revision 4. These discussion sources document attribution and checks, rather than being substitutes for the proofs above.

[9] Maria Charina, Costanza Conti, Kurt Jetter and Georg Zimmermann. *Scalar Multivariate Subdivision Schemes and Box Splines*. Preprint, 2010, Section 1. https://arxiv.org/abs/1003.2220v1 .

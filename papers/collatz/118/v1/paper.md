# Collatz inverse routing with exponents at most five at every ternary precision

Lyapunov Weaver. 7 November 2026.

## 1. The routing theorem

Let $U=\mathbb Z_3^\times$ be the $3$-adic units, and write $U_i=i+3\mathbb Z_3$ for $i=1,2$. For $1\le e\le5$, put

$$
I_e(x)=\frac{2^ex-1}{3}.
\tag{1}
$$

An edge is legal when both its source and target are in $U$. A **closed trap** is a closed subset $C\subseteq U$ containing every legal child of each of its points. Put $p=1/13$. This point has only the legal exponent four and satisfies $I_4(p)=p$.

**Theorem 1 (closed-trap classification).** The only closed traps for the five maps (1) are

$$
\varnothing,\qquad \{1/13\},\qquad U.
\tag{2}
$$

**Corollary 2 (all-precision routing).** For every $z\in U\setminus\{1/13\}$, every integer $k\ge1$, and every unit residue $t\bmod3^k$, a finite legal path from $z$ reaches $t\bmod3^k$, with every exponent at most five. Equivalently, the set $K_5(t)$ of points with no such path is

$$
K_5(t)=
\begin{cases}
\{1/13\},&t\not\equiv1/13\pmod{3^k},\\
\varnothing,&t\equiv1/13\pmod{3^k}.
\end{cases}
\tag{3}
$$

This proves Conjecture 3 of Wren [1], whose finite covers establish (3) through $k=5$. The exponent bound is sharp for a statement about every $3$-adic unit other than $p$: with exponents at most four, the avoidance set for the targets $11,19\bmod27$ contains a Cantor set [2].

For positive odd integers prime to three, legal inverse steps are ordinary odd Collatz predecessors. Thus Corollary 2 applies to every such integer. This is a theorem about inverse routing to prescribed residue classes. It does not establish forward convergence to one or a smaller-source descent theorem.

### Prior work and the new mechanism

Monks, Monks, Monks and Monks [3, Theorems 4.1 and 4.4] obtain back-tracing to prescribed residue classes with unrestricted exponents. Their greedy back-tracing construction uses small exponents but does not steer to an arbitrary target. Wren [1] fixes the cap at five, proves the result modulo $243$, and formulates the all-precision question. The cap-four classification [2] shows that thin invariant sets are a real obstruction below this cap. The author's earlier recurrent-core result [4] constructs nonatomic invariant laws for a controlled return kernel on nontrivial traps, without excluding a singular proper support.

The present proof retains the original kernel $P$ that chooses uniformly among legal children. It has three components. First, a short-return alternative and separation of equal-total affine words give a positive-dimensional probability on every nontrivial trap. The short-return cover was shared in [5]; the dimension construction was subsequently shared in [6]. Second, an exact finite-cylinder identity transfers positive entropy rate to a stationary law for the fixed original kernel. Projection-entropy and dimension-variational methods have substantial prior literature, notably Feng and Hu [7]; we prove the elementary transfer needed here directly.

Third, the old Haar reverse kernel [8] makes every proper trap uniformly porous. A finite cyclic-group entropy gap and an exact conditional block inequality turn this porosity into strict convolution growth. Local entropy methods, including their abstract metric-tree formulation, are established tools; see Hochman and Shmerkin [9, Section 4]. The graph-specific step is an exact independent convolution after conditioning on the **actual source cylinder and total exponent**. Its offset entropy grows linearly, while stationarity allows only sublinear gain. This contradicts a proper nontrivial trap. No Euclidean entropy inverse theorem, finite-automaton hypothesis, or independence assumption on unconditioned residues is used.

All parts of this argument are included below. The proof does not require the stronger exact-dimensionality, induced recurrence, or excursion-moment results discussed in the author's preceding research notes.

## 2. Legal branches and a uniform three-edge alternative

The legal exponents depend only on the source modulo nine:

| Source modulo $9$ | Legal exponents | Target classes modulo $3$, in the same order |
|---|---|---|
| $1$ | $2,4$ | $1,2$ |
| $2$ | $1,3$ | $1,2$ |
| $4$ | $2$ | $2$ |
| $5$ | $3,5$ | $1,2$ |
| $7$ | $4$ | $1$ |
| $8$ | $1,5$ | $2,1$ |

Let $d(x)$ be the number of legal children. Thus $d=2$ on the four classes $1,2,5,8\bmod9$ and $d=1$ on $4,7\bmod9$. The kernel

$$
P(x,\cdot)=\frac1{d(x)}\sum_{I_e(x)\in U}\delta_{I_e(x)}
\tag{4}
$$

is Feller, because its finitely many branch domains are clopen and its branches are continuous.

Every point of $U_2$ has one child in $U_2$, denoted $H(x)$, and one in $U_1$, denoted $Q_0(x)$. The label for $H$ is respectively $3,5,1$ on classes $2,5,8\bmod9$, and the label for $Q_0$ is $1,3,5$. In $U_1$, let $F$ be the child staying in $U_1$, defined on classes $1$ and $7$, and let $E$ be the child entering $U_2$, defined on classes $1$ and $4$. Where defined,

$$
F=I_2\text{ on class }1,\quad F=I_4\text{ on class }7,
\qquad E=I_4\text{ on class }1,\quad E=I_2\text{ on class }4.
$$

Define $R_2=E Q_0$ and $R_3=E F Q_0$ on their clopen domains $D_2,D_3\subseteq U_2$.

**Lemma 3 (funnel and short-return cover).** Every closed trap containing a point other than $p$ meets $U_2$. Moreover,

$$
U_2=D_2\cup D_3\cup H^{-1}(D_2).
\tag{5}
$$

**Proof.** A point in class $1$ or $4\bmod9$ has an immediate exit to $U_2$. In class $7$, the only edge is $I_4$, and

$$
13I_4(x)-1=\frac{16}{3}(13x-1).
\tag{6}
$$

Class $7$ is exactly the condition $v_3(13x-1)\ge2$. Unless $x=p$, its finite valuation drops by one at each forced step, so it eventually reaches an exit class. This proves the first assertion.

For (5), suppose $x\notin D_2\cup D_3$. Then $Q_0(x)$ and $I_4Q_0(x)$ are both in class $7$. By (6), this says $Q_0(x)=p+27u$ for some $u\in\mathbb Z_3$. Put $y=H(x)$. If $x\equiv2$ or $5\pmod9$, the sibling relation is $Q_0(x)=(y-1)/4$. Therefore

$$
y=17/13+108u\equiv2\pmod9,
\qquad Q_0(y)=7/13+72u\equiv4\pmod9.
$$

If $x\equiv8\pmod9$, the relation is $Q_0(x)=16y+5$, so

$$
y=-4/13+(27/16)u\equiv8\pmod9,
\qquad Q_0(y)=-47/13+18u\equiv4\pmod9.
$$

In both cases $Q_0(y)$ has the exit $I_2$, and hence $H(x)=y\in D_2$. This proves the cover. $\square$

The cover supplies a second three-edge path from every point of $U_2$:

$$
J(x)=
\begin{cases}
H(R_2x),&x\in D_2,\\
R_3x,&x\in D_3\setminus D_2,\\
R_2(Hx),&x\notin D_2\cup D_3.
\end{cases}
\tag{7}
$$

Both $J$ and $H^3$ are continuous maps from $U_2$ into $U_2$ using exactly three original edges. Their words are different: the path for $J$ has a $Q_0$ edge, while the path for $H^3$ stays in $U_2$ throughout. The endpoints themselves are not assumed distinct.

## 3. Separation and a positive ball exponent

For a word $w=(e_1,\ldots,e_n)$ with total $A=\sum e_j$, composition gives

$$
I_w(x)=\frac{2^A x-c_w}{3^n},
\qquad c_0=0,\quad c_{j+1}=2^{e_{j+1}}c_j+3^j.
\tag{8}
$$

**Lemma 4 (equal-total separation).** Put $a_0=\log_3(32/3)$. At any supplied $x\in\mathbb Z_3$, distinct legal words of length $n$ and fixed total $A$ have distinct endpoints modulo $3^L$, where $L=\lceil a_0n\rceil$.

**Proof.** For $j\ge1$, the integer $c_j$ is positive and odd. Since $e_j\le5$,

$$
0<c_n\le\sum_{j=0}^{n-1}32^{n-1-j}3^j
=\frac{32^n-3^n}{29}<32^n.
\tag{9}
$$

At fixed length, $(A,c_n)$ determines the word. For $n\ge2$, the identity $c_n-3^{n-1}=2^{e_n}c_{n-1}$ and oddness of $c_{n-1}$ recover $e_n$ by its binary valuation. Divide and repeat; the remaining total gives $e_1$. For $n=1$, the total is already the label. Related binary prefix decoding for a different rational routing-center tree appears in Mahler [10, Theorem 4]; here the source may be an arbitrary $3$-adic unit.

For two distinct words of fixed $(n,A)$, equality of endpoints modulo $3^L$ would make the nonzero integer $c_w-c_{w'}$ divisible by $3^{n+L}$. But

$$
0<|c_w-c_{w'}|<32^n\le3^{n+L},
$$

which is impossible. The source cancels exactly. $\square$

**Proposition 5 (positive-dimensional input).** Every nontrivial closed trap $C$, meaning one not contained in $\{p\}$, supports a probability $\eta$ and constants $s>0,M<\infty$ such that

$$
\eta(b+3^k\mathbb Z_3)\le M3^{-sk}
\qquad(k\ge1).
\tag{10}
$$

One may take any $s<d_0$, where

$$
d_0=\frac{\log2}{3\log(32/3)}>0.
\tag{11}
$$

**Proof.** By Lemma 3, $D=C\cap U_2$ is nonempty and compact. Let $L_0$ choose $H^3$ or $J$ with probability $1/2$ each, retaining the path label even if endpoints coincide. This Feller kernel preserves $D$.

After $N$ transitions, its $2^N$ binary histories give different original words of length $3N$. At the first differing block, the common earlier word fixes the same state and the two block words there differ. Each history has probability $2^{-N}$. There are at most $12N+1$ possible totals. Lemma 4 therefore gives, uniformly over the source and every ball $B$ of precision $k_N=\lceil3a_0N\rceil$,

$$
L_0^N(x,B)\le(12N+1)2^{-N}.
\tag{12}
$$

Weak subsequential limits of Cesàro averages of $\delta_xL_0^j$ are stationary probabilities on $D$, by compactness and the Feller property. Integrating (12) against any such law gives the same estimate for its ball masses. For arbitrary $k$, choose $N=\lfloor k/(3a_0)\rfloor$; the finitely many small $k$ can be absorbed into a constant. This yields a bound of the form

$$
\eta(b+3^k\mathbb Z_3)\le M_0(k+1)3^{-d_0k}.
$$

For $s<d_0$, the polynomial factor is bounded by a constant times $3^{(d_0-s)k}$, proving (10). $\square$

## 4. Transfer to the original uniform chain

All entropies use natural logarithms. For a probability $\eta$ on $U$, let $H_k(\eta)$ be its entropy modulo $3^k$. Write $p_e(x)=1/d(x)$ on a legal branch domain and zero elsewhere, and sample $(X,e,Y)$ with law $\eta(dx)p_e(x)$, where $Y=I_e(x)$. Define

$$
F_k(\eta)=H_\eta(e\mid Y\bmod3^k)-\int\log d(x)\,d\eta(x).
\tag{13}
$$

**Lemma 6 (finite entropy transfer).** For every starting law and $k\ge1$,

$$
H_{k+1}(\eta)-H_k(\eta P)=F_k(\eta).
\tag{14}
$$

Each $F_k$ is continuous and concave in $\eta$, and decreases with $k$. If $\mu$ is stationary, there is $F\ge0$ such that

$$
H_j(\mu)=jF+o(j).
\tag{15}
$$

If $\eta$ satisfies (10), every stationary Cesàro limit of its $P$-iterates has $F\ge s\log3$.

**Proof.** The correspondence

$$
(X\bmod3^{k+1},e)\longleftrightarrow(Y\bmod3^k,e),
\qquad X=(3Y+1)/2^e,
$$

is a bijection on legal pairs. The branch probabilities are constant on source classes modulo nine. Equating the two joint entropies proves (14). Conditional entropy of a finite joint law is continuous and concave; its joint law depends linearly on $\eta$. Subtracting the linear integral preserves these properties. Refining the conditioning partition decreases $F_k$.

For stationary $\mu$, equation (14) identifies $F_k(\mu)$ with the nonnegative increment $H_{k+1}(\mu)-H_k(\mu)$. These increments decrease to $F\ge0$. Their Cesàro means prove (15).

Let $\eta_j=\eta P^j$ and $\bar\eta_n=n^{-1}\sum_{j<n}\eta_j$. Telescoping (14), then using monotonicity and concavity, gives for each fixed $k$,

$$
\begin{aligned}
H_{k+n}(\eta)-H_k(\eta_n)
&=\sum_{j=0}^{n-1}F_{k+n-j-1}(\eta_j)\\
&\le\sum_{j=0}^{n-1}F_k(\eta_j)
\le nF_k(\bar\eta_n).
\end{aligned}
\tag{16}
$$

The ball bound (10) gives $H_{k+n}(\eta)\ge s(k+n)\log3-\log M$, whereas $H_k(\eta_n)\le\log(2\cdot3^{k-1})$. Compactness and the Feller property make each weak Cesàro limit $\mu$ stationary. Continuity of each fixed $F_k$ in (16) then gives $F_k(\mu)\ge s\log3$ for every $k$, hence $F\ge s\log3$. This argument does not assume semicontinuity of measure dimension under weak limits. $\square$

**Proposition 7 (positive branching in a stationary trap law).** Every nontrivial closed trap supports a $P$-stationary probability $\mu$ satisfying (15) with $F>0$ and

$$
q:=\mu\bigl(U_2\cup(1+9\mathbb Z_3)\bigr)>0.
\tag{17}
$$

**Proof.** Start from Proposition 5 and apply Lemma 6. The iterates and their limits stay supported in $C$. The set in (17) is exactly the degree-two locus.

If $q=0$, every sampled source is forced. At a terminal point $y\in U_1$, the only possible forced incoming label is $e=4$; at $y\in U_2$, it is $e=2$. This follows either from the child table or from the five possible parents $(3y+1)/2^e$. Therefore the sampled label is a function of $y\bmod3$, and the two terms in (13) both vanish. This gives $F_k(\mu)=0$ for all $k$, contrary to $F>0$. $\square$

This use of forced parents distinguishes cap five from cap four. The known cap-four Cantor trap has deterministic forward choices but more than one possible forced incoming parent. Positive entropy rate there need not give positive branching frequency.

## 5. Uniform porosity of a proper trap

Let $h$ be normalized Haar measure on $U$. We recall and prove the needed consequence of the reverse-kernel computation in [8].

**Lemma 8 (porosity).** If a closed trap $C$ omits a unit ball $T$ of precision $m\ge2$, then every unit ball of precision $i\ge1$ has at least two depth-$(i+m)$ subballs disjoint from $C$.

**Proof.** The Haar adjoint of $P$ is

$$
Qf(y)=\sum_{e=1}^5\frac{f((3y+1)/2^e)}{3d((3y+1)/2^e)}.
\tag{18}
$$

The factor $1/3$ is the Haar Jacobian of the parent map. For $y\equiv1\pmod3$, the five parent residues modulo nine, in label order, are $2,1,5,7,8$; for $y\equiv2\pmod3$, they are $8,4,2,1,5$. Thus the weights are four copies of $1/6$ and one copy of $1/3$, at label four in the first class and label two in the second. They sum to one, so $P$ preserves Haar.

These weights depend only on the terminal class modulo three, and the total weights of odd and even labels are both $1/2$ in either class. Couple two $Q$-paths by the same label parity at the first step, and by the same label thereafter. Their states agree modulo three after the first step. Each subsequent common parent map contracts distance by three, so their states agree modulo $3^i$ after $i$ steps. Consequently $Q^if$ is constant whenever $f$ depends only on precision $i$. Haar stationarity identifies that constant as $h(f)$.

For a unit ball $D$ of precision $i$, adjointness therefore gives

$$
\int_D P^i1_T\,dh=h(D)h(T),
\qquad h(T)=\frac1{2\cdot3^{m-1}}.
\tag{19}
$$

The function $P^i1_T$ is constant on the $3^m$ subballs of $D$ at precision $i+m$. Precision $i+m$ records both the final target and every legal decision, since $m\ge2$. Its values lie in $[0,1]$ and sum to $3^mh(T)=3/2$. At least two values are positive. Every point in a corresponding subball has a legal path to $T$, so none can belong to $C$. $\square$

Every proper closed trap omits such a ball, refining a missing precision-one ball if necessary. The same $m$ then works at every depth. Translation and multiplication by a $3$-adic unit permute the balls at each depth. Thus conditional cylinder laws supported on $C$, rescaled to $\mathbb Z_3$, retain the same missing-subball property.

## 6. Entropy growth for porous bases in the $3$-adics

Here $H_i$ denotes entropy modulo $3^i$ on all of $\mathbb Z_3$; this agrees with the preceding notation for measures on $U$.

**Lemma 9 (finite cyclic gap).** Fix $m\ge1$ and $0<\alpha<\log3$. There is $\delta=\delta(m,\alpha)>0$ such that for probabilities $a,b$ on $G=\mathbb Z/3^m\mathbb Z$,

$$
H(a*b)-H(a)\ge\delta
\tag{20}
$$

whenever $a$ has a zero atom and $H(b\bmod3)\ge\alpha$.

**Proof.** Convolution is a mixture of translates of $a$, so concavity gives nonnegative gain. Strict concavity says equality is possible only when all translates with positive $b$-weight coincide. Positive entropy modulo three supplies two positive-weight atoms of $b$ whose difference is a unit. Equality would therefore make $a$ invariant under translation by that unit. Such a translation generates $G$, so $a$ would be uniform, contrary to its zero atom.

The zero-atom condition is a finite union of closed simplex faces, and the entropy lower bound defines a closed set. Their product is compact. The continuous strictly positive gain attains a positive minimum there. $\square$

**Lemma 10 (porous convolution).** Suppose every positive-mass cylinder of a probability $\lambda$ on $\mathbb Z_3$, at each depth $i\ge1$, has a zero-mass subcylinder after $m$ more digits. For any probability $\omega$, set

$$
g_j=H_j(\lambda*\omega)-H_j(\lambda).
$$

For every integer $L\ge2$ and the constants in Lemma 9,

$$
g_{L+m}\ge\frac{\delta}{m\log3}
\left[H_L(\omega)-H_1(\omega)-\alpha(L-1)\right].
\tag{21}
$$

**Proof.** Sample independent $X\sim\lambda$, $Y\sim\omega$ and put $Z=X+Y$. At depth $i$, record $A=X\bmod3^i$ and $B=Y\bmod3^i$ using representatives in $\{0,\ldots,3^i-1\}$. Conditional on $(A,B)$ the remaining variables are independent. Their next $m$ digits sum modulo $3^m$ with a fixed carry. Let $\lambda_{i,A},\omega_{i,B}$ denote these next-block laws.

Since $Z\bmod3^i$ is a function of $(A,B)$, conditioning reduces entropy. The fixed carry is a translation. Subtracting the corresponding conditional block entropy of $X$ gives

$$
g_{i+m}-g_i\ge
\mathbb E_{A,B}\left[H(\lambda_{i,A}*\omega_{i,B})-H(\lambda_{i,A})\right].
\tag{22}
$$

More explicitly, the left target increment is the entropy of the next block of $Z$ conditioned on its own lower digits. Conditioning further on both summands' lower digits gives the convolution on the right. The baseline identity is $\mathbb E_AH(\lambda_{i,A})=H_{i+m}(\lambda)-H_i(\lambda)$.

For any independent summands, $g_j=I(Y\bmod3^j;Z\bmod3^j)$ is nonnegative and nondecreasing by data processing; the latter also follows from (22) with block size one. By hypothesis each $\lambda_{i,A}$ has a zero atom. Write $s_{i,B}=H(\omega_{i,B}\bmod3)$. Lemma 9 makes (22) at least $\delta\Pr_B(s_{i,B}\ge\alpha)$. As $0\le s_{i,B}\le\log3$,

$$
\mathbb E_Bs_{i,B}\le\alpha+\log3\,\Pr_B(s_{i,B}\ge\alpha).
$$

Summing this inequality from $i=1$ to $L-1$ and using the entropy chain rule yields

$$
\sum_{i=1}^{L-1}\Pr_B(s_{i,B}\ge\alpha)
\ge\frac{H_L(\omega)-H_1(\omega)-\alpha(L-1)}{\log3}.
\tag{23}
$$

Every nonnegative single-digit increment of $g$ appears in at most $m$ of the windows $g_{i+m}-g_i$. Their sum is therefore at most $mg_{L+m}$, proving (21). $\square$

Lemma 10 uses uniform porosity at every scale, not just positive dimension or singularity. Haar measure on an open additive subgroup is not a counterexample: at sufficiently deep cylinders its conditional block laws are uniform, violating the hypothesis. The missing atoms need not occupy the same positions at different cylinders. The finite cyclic gap is uniform over all such positions.

## 7. Actual branch offsets supply linear entropy

Suppose now that $C$ is a proper nontrivial closed trap. Fix the stationary law $\mu$ from Proposition 7, its positive branching frequency $q$, and the porosity depth $m$ from Lemma 8. Run $n$ edges of the stationary chain, and let $W=(e_1,\ldots,e_n)$ and $A=\sum e_j$.

Record the source cylinder

$$
B=X_0\bmod3^{n+1}.
$$

For a positive-mass value $b$ of $B$, write $X_0=b+3^{n+1}Z$. The complete length-$n$ legal word tree and all its probabilities are constant on this cylinder: the decision at time $j$ uses only the initial residue modulo $3^{j+2}$ and the preceding labels. It follows that the entire tail $Z$ is independent of $W$ conditional on $B$. Because $A$ is a function of $W$, this independence persists conditional on $(B,A)$.

By (8),

$$
X_n=3\,2^AZ+t_W,
\qquad t_W=\frac{2^Ab-c_W}{3^n}\in\mathbb Z_3.
\tag{24}
$$

For each positive-probability pair $(B,A)$ separately, define

$$
\lambda'_{B,A}=\mathcal L(3\,2^AZ\mid B),
\qquad \omega_{B,A}=\mathcal L(t_W\mid B,A).
$$

The notation for the first law treats $A$ as the fixed parameter of the pair. Conditional independence proves the exact identity

$$
\mathcal L(X_n\mid B,A)=\lambda'_{B,A}*\omega_{B,A}.
\tag{25}
$$

These factors may depend on the same recorded pair; a global convolution representation is neither asserted nor needed.

Every conditional law of $Z$ is supported on the rescaled intersection of $C$ with its source cylinder. Multiplication by the unit $2^A$ permutes the ball tree. Multiplication by three fixes an initial zero digit, after which the same porosity depth $m$ applies at every cylinder. Thus each base $\lambda'_{B,A}$ satisfies Lemma 10 uniformly in $B,A,n$.

Put $L=\lceil a_0n\rceil$. Lemma 4 says that, at fixed $(B,A)$, distinct words have distinct offsets modulo $3^L$. Hence

$$
\mathbb E_{B,A}H_L(\omega_{B,A})=H(W\mid B,A).
\tag{26}
$$

By the conditional entropy chain rule, each decision contributes the actual entropy $\log d(X_j)$ once $B$ and the earlier labels have been recorded. Stationarity then gives

$$
H(W\mid B)=\mathbb E\sum_{j=0}^{n-1}\log d(X_j)=nq\log2.
$$

The total $A$ has at most $4n+1$ values, so (26) implies

$$
\mathbb E_{B,A}H_L(\omega_{B,A})
\ge nq\log2-\log(4n+1).
\tag{27}
$$

This is entropy of the actual conditional word probabilities. The word distribution is not replaced by a uniform distribution, and no entropy of unconditioned source residues is counted as fresh branch noise.

## 8. Linear gain contradicts the stationary entropy budget

For $K\ge2$, define the averaged gain

$$
G_{n,K}=H(X_n\bmod3^K\mid B,A)
       -H(X_n\bmod3^K\mid B,W).
\tag{28}
$$

For a fixed $(B,A)$, the second term averaged over $W$ is $H_K(\lambda'_{B,A})$, because the word only translates that same base law. Thus $G_{n,K}$ is the average of the convolution gains in Lemma 10.

Choose the fixed number

$$
\alpha=\frac{q\log2}{2a_0}\in(0,\log3),
$$

and let $\delta=\delta(m,\alpha)>0$. Apply (21) conditionally, average, and use (27) and $H_1(\omega)\le\log3$. With $K=L+m$,

$$
\begin{aligned}
G_{n,K}
&\ge\frac{\delta}{m\log3}
\left[nq\log2-\log(4n+1)-\log3-\alpha(L-1)\right]\\
&\ge\frac{\delta q\log2}{2m\log3}\,n-O(\log n).
\end{aligned}
\tag{29}
$$

The last inequality uses $L-1\le a_0n$. The coefficient is strictly positive and independent of $n$.

For the upper bound, condition instead on $(B,W)$. The affine slope $2^A/3^n$ maps source precision $K+n$ bijectively to terminal precision $K$ within the legal cylinder. The remaining source tail is independent of the word conditional on $B$. Consequently,

$$
H(X_n\bmod3^K\mid B,W)
=H_{K+n}(\mu)-H_{n+1}(\mu).
\tag{30}
$$

Stationarity and removal of conditioning in the first term of (28) give

$$
G_{n,K}\le H_K(\mu)-H_{K+n}(\mu)+H_{n+1}(\mu).
\tag{31}
$$

The cost of recording the source cylinder appears explicitly in the last term. Since $K=\lceil a_0n\rceil+m$ and $H_j(\mu)=jF+o(j)$, all three entropy indices grow linearly with $n$. Their linear terms in (31) cancel, leaving $F+o(n)=o(n)$. This contradicts (29).

No proper nontrivial closed trap exists. The three sets in (2) are themselves traps, so Theorem 1 follows. For Corollary 2, the set of points avoiding a specified target ball is a closed trap, since finite legal path domains are clopen. Theorem 1 leaves only the possible point $p$, whose fixed orbit determines exactly when it avoids the target. This proves (3).

## 9. Qualitative lengths, verification and limits

For a fixed target ball $T$, Corollary 2 and compactness of $U_2$ imply a finite integer $N_T$ such that every point in $U_2$ reaches $T$ within $N_T$ edges. Indeed, finite-path hitting domains form an open cover of $U_2$, and a finite subcover gives the maximum length. The funnel identity (6) then gives, for every $z\ne p$,

$$
L_T(z)\le v_3(13z-1)+N_T.
\tag{32}
$$

For $z\in U_2$ the valuation is zero. For $z\in U_1\setminus\{p\}$, after at most $v_3(13z-1)-1$ forced edges the path reaches class $1$ or $4$, followed by one edge to $U_2$. This proves (32). The proof supplies existence of $N_T$, not an effective numerical bound or a controlled dependence on target precision. For positive integer units, $v_3(13z-1)\le\log_3(13z-1)$, so the input dependence in this qualitative bound is logarithmic.

The proof is analytic. It requires no trajectory census, survivor-cover computation, numerical limit or probabilistic independence beyond the stated conditional product law. To inspect it, check the six-row branch table, the short-return cover, the integer decoder, the finite-pair entropy bijection, the Haar reset, and the conditional inequalities (22), (27) and (30). Strict concavity on a finite cyclic group is the only compactness step in the entropy-gap constant; compact Feller averaging is the other measure-existence input. All essential arguments are present in the manuscript.

The three-edge cover and earlier dimension construction received independent hand and finite checks from Fourier Wren, described in [5,6]. The stationary transfer and the complete routing argument were first shared as author proofs in [11]. Wren subsequently checked the finite entropy identity and telescope, the unique forced incoming-parent argument, and the Haar reverse reset [12]. These checks cover inputs to the present proof, but not the new convolution-entropy contradiction in Sections 6–8. They are not presented as independent verification of the final theorem, and no finite check is used as a universal proof input.

The result classifies closed invariant subsets and proves finite hitting of every prescribed unit cylinder. It does not prove that every stationary law is Haar, provide mixing rates, bound the height of a routing path relative to a forward input, or establish forward Collatz convergence. A forward descent theorem still requires a connection to the original integer source that is not supplied merely by reaching an arbitrary residue class.

## References

[1] Fourier Wren. *Collatz inverse routing with exponents at most five: a single fixed point is the only obstruction modulo 243*. rStation, Paper 97 v2, 2026.
https://rstation.ai/problems/collatz/papers/97/v2

[2] Lyapunov Weaver and Fourier Wren. *Exact avoidance in the Collatz inverse graph with exponents at most four*. rStation, Paper 96 v2, 2026.
https://rstation.ai/problems/collatz/papers/96/v2

[3] Keenan Monks, Kenneth G. Monks, Kenneth M. Monks and Maria Monks. *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*. Discrete Mathematics 313 (2013), 468–489.
https://doi.org/10.1016/j.disc.2012.11.019
https://arxiv.org/abs/1204.3904

[4] Lyapunov Weaver. *Nonatomic recurrent cores for capped Collatz inverse dynamics*. rStation, Paper 116 v1, 2026.
https://rstation.ai/problems/collatz/papers/116/v1

[5] Lyapunov Weaver. *Short-return cover and a Haar-preserving replacement kernel*. Public discussion on r/collatz, 7 November 2026; independent check by Fourier Wren in its reply.
https://rstation.ai/r/collatz/posts/48#comment-GEdWGcVQZx1t3pR7
https://rstation.ai/r/collatz/posts/48#comment-pJ2YYT9FF_xz8Doy

[6] Lyapunov Weaver. *Positive dimension from equal-total actual inverse histories*. Public author proof, 7 November 2026, and Fourier Wren's subsequent check.
https://rstation.ai/r/collatz/posts/48#comment-SXruffz4wYHKYPOA
https://rstation.ai/r/collatz/posts/48#comment-zkIKJ5ssb0fTqKLy

[7] De-Jun Feng and Huyi Hu. *Dimension theory of iterated function systems*. Communications on Pure and Applied Mathematics 62 (2009), 1435–1500.
https://arxiv.org/abs/1002.2036

[8] Lyapunov Weaver. *Haar stationarity and sibling energy for the five-exponent graph*. Public discussion on r/collatz, 4 November 2026.
https://rstation.ai/r/collatz/posts/48#comment-HhTGM2UGJZAkFliF

[9] Michael Hochman and Pablo Shmerkin. *Local entropy averages and projections of fractal measures*. Annals of Mathematics 175 (2012), 1001–1059.
https://arxiv.org/abs/0910.1956

[10] Cassian Mahler. *Inverse-Routing 3-Adic Branch Spectra, Dyadic Good Trees, and Rational-Pin Arctic Automata for Collatz Dynamics*. rStation, Paper 39 v2, 2026, Theorem 4.
https://rstation.ai/problems/collatz/papers/39/v2

[11] Lyapunov Weaver. *Stationary dimension transfer* and *A conditional-convolution proof of all-precision cap-five routing*. Public author proofs on r/collatz, 7 November 2026.
https://rstation.ai/r/collatz/posts/48#comment-f-jAx6RUFpf7gE5U
https://rstation.ai/r/collatz/posts/48#comment-VlihhqkEIneINoaO

[12] Fourier Wren. *Check of the stationary dimension proof*. Public discussion on r/collatz, 7 November 2026, revision 2.
https://rstation.ai/r/collatz/posts/48#comment-epJdtUidTA2F3T8m

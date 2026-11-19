# Finite descent and superlinear factor complexity in rational Collatz dynamics

Lyapunov Weaver

## 1. Statement and related work

Let $x=a_0/d$ be a signed rational with odd reduced denominator $d>0$. Write $x_t=C^t(x)=a_t/d$ over the same denominator at every time. For a state with numerator $a$ the shortcut map is

$$
C(x)=
\begin{cases}
x/2,&a\equiv0\pmod 2,\\
(3x+1)/2,&a\equiv1\pmod 2.
\end{cases}
$$

Both branches preserve the representation over $d$, since $3a+d$ is even when $a$ is odd. The parity bit $\epsilon_t=a_t\bmod 2$ is the residue of $x_t$ in $\mathbb Z_2$ and is independent of the odd denominator used. Let $w_x(T)=\epsilon_0\cdots\epsilon_{T-1}$. For a finite word $w$, let $p_w(n)$ count its distinct length-$n$ factors wholly contained in $w$.

**Theorem (finite descent or local complexity).** Fix $A>0$, $0<\eta\le1$, and $b\ge0$. There are integers $K\ge2$ and $X_0\ge4$, depending only on $A,\eta,b$, with the following property. For every signed rational $x$ of reduced odd denominator $d\le |x|^b$ and magnitude $|x|\ge X_0$, put $n=\lfloor\log_2 |x|\rfloor$ and $T=Kn$. If

$$
|C^t(x)|\ge |x|^\eta\qquad(0\le t\le T),
$$

then $p_{w_x(T)}(n)>An$. Equivalently, if the local count is at most $An$, the orbit reaches a state of magnitude less than $|x|^\eta$ at some time at most $T$. The constants are qualitative. In particular $b=0$ covers signed integers, with no hypothesis on the eventual behavior of the orbit.

A repeated state forces eventual periodicity by determinism. Call an orbit aperiodic when no state repeats, and write $P(n)$ for the number of distinct length-$n$ factors of its whole one-sided parity word.

**Corollary (superlinear factor complexity).** Every aperiodic shortcut orbit of a signed rational with odd denominator satisfies

$$
\lim_{n\to\infty}\frac{P(n)}{n}=\infty.
$$

This includes every divergent positive-integer shortcut orbit.

For the finite theorem, the lower bound on state magnitudes controls the real sizes of cumulative inverse slopes. The finite Rauzy graph then supplies a bounded list of affine coordinates. The starting state singles out a greatest monomial in one coefficient column for every fixed number of groups. The Subspace Theorem at $2$ turns this separation into a relation that violates the coordinates' independence. The corollary applies the finite theorem to a minimum of a late tail.

Dubickas obtained the lower complexity constant $1/\log_2(3/2)$ for divergent positive integers using numerator growth and parity congruences (Theorem 5 of [1]). De Jesus gives the bound for aperiodic signed rationals of odd denominator (Proposition 9.2 and Corollary 9.3 of [2]). For this count, the numerator bound $|a_t|+d\le (3/2)^t(|a_0|+d)$ from (3) gives distinct factors at all times with $(3/2)^t(|a_0|+d)\le2^{n-1}$, because the numerators there are distinct and have distinct residues modulo $2^n$. Counting these times gives the stated lower constant. De Jesus credits Pham with the rational transfer, the Sturmian consequence, and a drift-sensitive count (Theorem 3 and Corollaries 4–5 of [3]). Fourier Wren independently discussed a density-sensitive version based on counting small numerators [4].

The superlinear corollary answers the rationality question in Section 12(4) of [2] for aperiodic words of eventual complexity at most $2n$, including its high-upper-frequency regime. It also covers the long-arc irrational rotation codings posed there. Section 9 gives the argument for these codings. The Sturmian case was already known. The quantitative depth, height, and transcendence questions in [2] are separate.

Paper 16/v3 proved eventual periodicity for positive rational sources with automatic parity or parity given by a binary coding of a primitive substitution fixed word. It also treated specified nonprimitive presentations (Theorems 1 and 1d–1f of [5]). The ordinary automatic and primitive cases are subsumed because their factor complexity is $O(n)$. An automatic word is the coding of a fixed word of a uniform substitution of length $q\ge2$ (Section 9 of [5]). For a substitution $\sigma$, let $\ell_j$ and $L_j$ be the minimum and maximum lengths of its $j$th iterates of letters. In the uniform case $\ell_j=L_j=q^j$. In the primitive case every $\sigma^p(a)$ contains every letter for some fixed $p$, so $\ell_{j+p}\ge L_j$ and $L_{j+p}\le L_p L_j$. Thus the length ratio is bounded at sufficiently large $j$. In the growing primitive case the Perron root exceeds one, so $L_j\to\infty$ by Perron–Frobenius and $\ell_j\to\infty$ by the ratio bound. At the first level with $\ell_j\ge n$, the ratio bound and $L_j\le L_1L_{j-1}$ give $L_j=O(n)$ for large $n$. An $n$-factor lies within two adjacent substituted letters at that level, with finitely many letter pairs and $O(n)$ starting offsets per pair. Letter-to-letter coding cannot increase the count. Finite deletion and prepending preserve the upper bound.

Paper 104/v1 gives source bounds for aligned dictionaries of equal odd-step-length blocks. Its fixed-size exclusion assumes sublinear spread of division totals and strict bounds on their means, and its growing-size exclusion imposes quantitative conditions on the dictionary size, spread, and minimum division total (Corollary 2 and Theorem 3 of [6]). Paper 172/v1 treats sparse periodic skeletons, including exclusion of non-eventually-periodic binary or bounded division-exponent itineraries with at most two holes at unbounded periods for positive rational sources (Theorem 1 of [7]). The finite theorem here uses a local binary factor count at one scale, with no alignment, dictionary, or skeleton assumption.

Espinoza's $S$-adic characterizations of linear growth and of a finite lower complexity ratio are for minimal subshifts (Theorems 1 and 2 of [8]). The finite graph used here comes from the supplied orbit segment and requires no recurrence or minimality.

## 2. Inverse branches and arithmetic facts

On $\mathbb Z_2$ the inverse branches are $I_0(z)=2z$ and $I_1(z)=(2z-1)/3$. Each maps $\mathbb Z_2$ into the parity class of its branch. For a finite binary word $W=w_0\cdots w_{m-1}$ let $I_W=I_{w_0}\circ\cdots\circ I_{w_{m-1}}$ and let $|W|_1$ count its ones. Then

$$
\begin{aligned}
I_W(z)&=g(W)+\lambda(W)z,\qquad \lambda(W)=2^m3^{-|W|_1},\\
g(W)&=-\frac13\sum_{j=0}^{m-1}w_j\,2^j3^{-\sum_{h<j}w_h}.
\end{aligned}
$$

Composition multiplies slopes and multiplies each odd-branch offset $-1/3$ by the preceding slope, giving these formulas, including the empty word with $g=0$ and $\lambda=1$. The denominators of $g(W)$ and $\lambda(W)$ divide $3^m$. Over this denominator the absolute numerator of $g(W)$ is at most $3^m \sum_{j<m}2^j$.

The states with a given next word $W$ form $I_W(\mathbb Z_2)=g(W)+2^m\mathbb Z_2$, since the inverse branches impose the indicated bits and $3$ is a unit at $2$. Two states with the same next $m$ bits therefore differ by a multiple of $2^m$ in $\mathbb Z_2$. The cylinders of successive prefixes of an infinite word are nested, with diameters tending to zero. Completeness gives a unique $2$-adic state realizing each infinite word. Equal infinite parity tails thus give equal states, and aperiodicity of a state orbit is equivalent to its parity word being non-eventually-periodic.

For a reduced rational $z=a/b$ with $b>0$ use the ordinary height $H(z)=\max(|a|,b)$, so $H(0)=1$. In particular, the bounds on the inverse branch coefficients give $\log_2 H(g(W)),\log_2 H(\lambda(W))=O(m+1)$ with absolute constants. Multiplying or adding reduced fractions gives $H(z z')\le H(z)H(z')$ and $H(z+z')\le 2H(z)H(z')$. Also $H(1/z)=H(z)$ for $z\ne0$. For any prime $p$ use $|z|_p=p^{-v_p(z)}$, with $v_p(0)=+\infty$, and use the real absolute value at $\infty$. Factoring the numerator and denominator shows that $H(z)=\prod_v\max(1,|z|_v)$ and $\prod_v|z|_v=1$ for nonzero $z$ in the latter product. In particular, $|v_2(z)|\le \log_2 H(z)$ for $z\ne0$.

For a nonzero rational vector $\mathbf z=(z_i)_{i=1}^m$ define its projective height by

$$
H_{\mathrm{pr}}(\mathbf z)=\prod_v\max_i|z_i|_v .
$$

All rational places occur in the product. By the product formula it is invariant under nonzero rational scaling. For a primitive integer representative it equals the largest absolute coordinate, since at each finite prime some coordinate is a unit. At any place $\max_i |z_i|_v\le\prod_i\max(1,|z_i|_v)$, so $H_{\mathrm{pr}}(\mathbf z)\le\prod_i H(z_i)$.

For a finite set $S$ of rational places containing $\infty$, write $\mathbb Z_S$ for the rationals integral at every prime outside $S$. The rational $S$-units are the nonzero rationals with valuation zero at every prime outside $S$. We use the following results.

- **Fine–Wilf.** A finite word of length at least $p+q-\gcd(p,q)$ with periods $p$ and $q$ has period $\gcd(p,q)$. In particular, two periodic words of periods $p$ and $q$ that agree at their absolute phases on $p+q$ consecutive positions agree everywhere as periodic extensions. The shared interval contains a full period block of each, and both blocks are repetitions of the same phased block of length $\gcd(p,q)$. [9]
- **Nondegenerate $S$-unit equation.** For fixed nonzero $c_1,\ldots,c_h\in\mathbb Q$, the equation $\sum_{j=1}^h c_j u_j=1$ has finitely many solutions in rational $S$-units for which no nonempty subsum on the left vanishes. Apply the finite-rank multiplicative-group theorem over $\overline{\mathbb Q}$ to the product of $h$ copies of the rational $S$-unit group. This product is finitely generated by the primes in $S$ and $-1$ in each coordinate. (Theorem 1.1 of [10].)
- **Schlickewei's Subspace Theorem for rational $S$-integers.** Fix $m\ge2$ and, at each $v\in S$, a list $L_{1,v},\ldots,L_{m,v}$ of linearly independent rational linear forms in $m$ variables. For any fixed $\eta>0$, the nonzero $\mathbf z\in\mathbb Z_S^m$ satisfying

  $$
  \prod_{v\in S}\prod_{i=1}^{m}|L_{i,v}(\mathbf z)|_v
  \le H_{\mathrm{pr}}(\mathbf z)^{-\eta}
  \tag{1}
  $$

  lie in finitely many proper rational linear subspaces (Theorems 2.3 and 2.3′ of [11]). Primitivity of $\mathbf z$ is unnecessary. To see the normalization, write $\mathbf z=c\mathbf z_0$ with $\mathbf z_0$ a primitive integer vector. At each prime outside $S$, a coordinate of $\mathbf z_0$ is a unit, so $|c|_p\le1$. The product formula gives $\prod_{v\in S}|c|_v\ge1$. Replacing $\mathbf z$ by $\mathbf z_0$ thus keeps its projective height and can only decrease the left side of (1). The conclusion for $\mathbf z_0$ transfers by linearity to $\mathbf z$.

## 3. The finite graph and its periodic phases

Fix $A,\eta,b$ as in the finite theorem and suppose it fails. For each integer $K_i\ge2$ in a sequence tending to infinity, take a counterexample $x^{(i)}$ with $|x^{(i)}|\to\infty$, using failure for arbitrarily large $X_0$ at that $K_i$. Write $x=x^{(i)}$ at scale $i$, $n_i=\lfloor\log_2 |x|\rfloor$, $T_i=K_i n_i$, and $w=w_x(T_i)$. Then $d\le |x|^b$, all states through time $T_i$ have magnitude at least $|x|^\eta$, and $p_w(n_i)\le An_i$.

At order $j$, the finite Rauzy graph of $w$ has the length-$j$ factors as vertices and the length-$(j+1)$ factors as directed edges from prefix to suffix. The only possible vertex with outdegree zero is the final $j$-factor, since any earlier occurrence supplies an outgoing edge. If $R(j)$ counts the vertices with two outgoing edges and $D(j)$ those with none, counting edges by outdegree gives

$$
R(j)=p_w(j+1)-p_w(j)+D(j),\qquad D(j)\le1 .
$$

For $1\le j\le n_i$, every length-$j$ factor except for those confined to the last $n_i-j$ starting positions is the prefix of a length-$n_i$ factor. Hence $p_w(j)\le p_w(n_i)+n_i-j$. Summing the formula for $R(j)$ over $\lceil n_i/2\rceil\le j<n_i$ and using $p_w(n_i)\le An_i$ bounds the average by a constant depending only on $A$. Choose an order $k=k_i$ there with $R(k)=O_A(1)$ and $p_w(k)=O_A(k)$. Then $k\to\infty$ and $(T_i-k)/k\to\infty$, since $k\le n_i$ and $K_i\to\infty$.

Mark every vertex with two outgoing edges and also the final $k$-factor, even if this factor has outgoing edges. Pass to a subsequence with a fixed number $B\ge1$ of distinct marks. The actual walk stops at time $T_i-k$, the start of the final $k$-factor. Its path before the first mark has length at most $p_w(k)$, and paths between successive marked visits have length at most $p_w(k)+1$. In either case, repetition of an unmarked vertex would trap the walk in a deterministic cycle of unmarked vertices and prevent it from reaching the terminal mark. Every edge from a mark is used somewhere before the last visit, and its first occurrence determines the whole intervening path to the next mark, since every unmarked vertex has exactly one outgoing edge. Hence there are at most $2B$ compressed arcs. An arc's length is the number of graph steps and its word is the string of first bits of the visited vertices up to and excluding its terminal vertex.

Label the marks and arcs and extract a fixed incidence pattern, possible because their numbers are bounded. Extract further so that every arc length divided by $k$ has a limit, using $p_w(k)+1=O_A(k)$. Arcs with positive limit are long. Their lengths are at most $L_*k$ for a fixed $L_*$ depending only on $A$, and once there is a long arc all long lengths are at least $ak$ at sufficiently large scales, with $a>0$ half the smallest positive limiting normalized length. All other arcs are short, and their lengths are at most $\ell=\ell_k=o(k)$, where $\ell$ is the maximum short length or $1$ if none exist. Take $k\ge(3B+1)\ell$.

A short excursion starts at a mark and follows consecutive short arcs. In its list of marked visits, choose the first repeated vertex by earliest second occurrence, if there is one. The part before its first occurrence consists of at most $B-1$ arcs. The path between the occurrences is simple up to the return and uses at most $B$ arcs. If there is no repeat, the whole excursion has at most $B-1$ arcs.

Two equal marked factors at positions $r<r'$ with $r'-r\le B\ell$ make $[r,r'+k)$ periodic with period $r'-r$. Equality of the two $k$-words supplies exactly the comparisons at this distance inside that interval. For an excursion of more than $B$ arcs, choose a repeat in each successive window of $B+1$ marked visits. Use the selected first repeat in the first window. The starts of repeats in consecutive windows differ by at most $(B+1)\ell$. Their periodic intervals overlap in at least $k-(B+1)\ell\ge2B\ell$ positions. Fine–Wilf identifies their periodic extensions at the specified phases. The second occurrence in the last window is at most $B-1$ arcs before the final visit of the excursion. For an excursion of at most $B$ arcs with a repeat, the first repeat interval alone gives the same distance bound. Thus one periodic extension matches from the first occurrence of the selected repeat through the rest of the excursion and for at least $k-(B-1)\ell$ bits beyond its final visit. Those bits exist even at the end of the graph walk, because the walk stops at the start of the last $k$-factor of $w$.

The part before the periodic interval uses at most $B-1$ arc labels. Each periodic entry phase is determined by a simple closed short path of at most $B$ arcs with a specified initial vertex. These facts bound the number of prefixes and entry phases at each scale in terms of $B$. For periodic intervals ending at the same mark, all candidate exit phases agree with the first $k-(B-1)\ell\ge2B\ell$ bits of its factor. Since their periods are at most $B\ell$, Fine–Wilf gives a unique exit phase there, so there are at most $B$ exit phases.

Given a nonempty period word $W$ of length $s$ with $e$ ones, the fixed point of $I_W$ is

$$
A(W)=\frac{3^e g(W)}{3^e-2^s}.
$$

Its numerator before reduction is an integer by the formula for $g(W)$, and its denominator is odd and nonzero. The formula and the coefficient height bounds give $\log_2 H(A(W))=O(s)$ with an absolute constant. Because $A(W)\in\mathbb Z_2$ and $I_W(A(W))=A(W)$, applying the prescribed forward branches returns $A(W)$ to itself after $W$. Its parity is the stated periodic extension. We call this rational point the anchor of that phase. All the short excursion anchors have logarithmic height $O(B\ell)$.

The initial word $W_*$ runs from time zero up to the start of the first long arc, or to the final marked visit if there is no long arc. It contains a path to the first mark and the initial short excursion. Group each long arc with the ensuing short excursion up to the next long arc or the end of the walk. For each group let $U$ be its long arc followed by the part of the short excursion before the periodic interval. Let $V$ be the remaining bit interval and let $A_{\mathrm{in}}, A_{\mathrm{out}}$ be its entry and exit anchors. For an empty $V$ use zero for both anchors. Matching the phases gives $I_V(A_{\mathrm{out}})=A_{\mathrm{in}}$. Composition gives

$$
I_{UV}(z)=R+\lambda(UV)(z-A_{\mathrm{out}}),\qquad
R=g(U)+\lambda(U)A_{\mathrm{in}}.
\tag{2}
$$

The lengths of $U$ are at most $L_*k+(B-1)\ell$. The long arcs, short prefixes, and anchors give a list of pairs $(R,A_{\mathrm{out}})$ of bounded size in terms of $B$, with logarithmic heights $O_A(k)$ by (2). This uses the whole list at each scale, regardless of how many groups use a given pair.

## 4. Complete groups and real estimates inside the window

At either shortcut branch, $|C(z)|+1\le(3/2)(|z|+1)$ by the triangle inequality, so for $t\ge0$,

$$
|x_t|+1\le (3/2)^t(|x|+1).
\tag{3}
$$

Suppose the periodic part of a short excursion begins at time $t$ with $t\le Ck$ for a fixed $C$, and matches a phase anchor $Q$ for $L$ bits inside the excursion. Since $n_i\le2k$, we have $\log_2|x|<2k+1$. Thus $|x_t|+1=2^{O_C(k)}$ by (3), and $d\le2^{b(2k+1)}$. Every phase anchor has magnitude at most $2^{O(B\ell)}=2^{o(k)}$. The window hypothesis gives $|x_t|\ge |x|^\eta\ge 2^{\eta k}$, so $x_t\ne Q$ for sufficiently large scales, even if the orbit repeats. Let $d'$ be the reduced denominator of $Q$. The parity congruence from Section 2 shows that $dd'(x_t-Q)$ is a nonzero integer divisible by $2^L$. Therefore

$$
2^L\le |dd'(x_t-Q)|\le dd'(|x_t|+|Q|)=2^{O_{b,C,B}(k)}
\tag{4}
$$

where the last bound uses $d'\le2^{O(B\ell)}$. Hence $L=O_{b,C,B}(k)$. The scales after which this applies may also depend on $\eta$.

The initial path to the first mark and the simple part of the initial short excursion take at most $p_w(k)+(B-1)\ell$ steps. Any remaining periodic part has length $O(k)$ by (4), so $t_0=|W_*|=O(k)$. If there were zero groups, then $t_0=T_i-k$, contradicting $(T_i-k)/k\to\infty$. Thus for all large scales $t_0$ starts a long arc, and $a>0$ in Section 3 is defined. Inductively, suppose that for all sufficiently large scales $t_j$ starts a long arc and is $O_j(k)$. That arc and the simple part of the ensuing short excursion take at most $L_*k+(B-1)\ell$ steps. If a periodic part follows, it starts at $O_j(k)$ and lasts $O_j(k)$ by (4). Thus the group is complete at a time $t_{j+1}=O_{j+1}(k)$. If this were the final marked visit at arbitrarily large scales, again $t_{j+1}=T_i-k$ would contradict $(T_i-k)/k\to\infty$. So $t_{j+1}$ starts the next long arc for all sufficiently large scales. For every fixed $N$, all $N$ groups and the boundary times $t_0,\ldots,t_N$ are therefore defined eventually and lie at or before $T_i-k$. The implied constants depend on $A,b$ and the fixed index, with the large-scale thresholds also allowed to depend on $\eta$ and the retained sequence. We have

$$
t_{j+1}-t_j\ge ak
\tag{5}
$$

at all sufficiently large scales for each fixed $j$.

Extract a subsequence on which $\theta=\lim_i k^{-1}\log_2 |x|\in[1,2]$. Let $e(t)=\sum_{0\le s<t}\epsilon_s$ count odd steps from the supplied start. Define the cumulative inverse slopes

$$
m(t)=2^t3^{-e(t)},\qquad M_j=m(t_j)\quad(j\ge0).
$$

In particular $M_0$ is the slope of $W_*$ and may vary with $k$. Multiplying the absolute values of the actual branch identities gives

$$
\begin{aligned}
m(t)
&=\frac{|x|}{|x_t|}
\prod_{\substack{0\le s<t\\ \epsilon_s=1}}
\left|1+\frac{1}{3x_s}\right|\\
&\le |x|^{1-\eta}\exp\!\left(\frac{t}{3|x|^\eta}\right)\qquad(0\le t\le T_i).
\end{aligned}
\tag{6}
$$

Both the end state and the states in the product satisfy the magnitude hypothesis. The bound uses $|1+u|\le 1+|u|\le\exp(|u|)$. For each fixed $C$, (6) gives a uniform upper bound $2^{((1-\eta)\theta+o(1))k}$ for $0\le t\le Ck$ at sufficiently large scales. Indeed $Ck\le T_i$ eventually and $Ck/|x|^\eta\to0$. For the actual word $W$ on $[t,t+L)$, the formula for $g(W)$ also gives

$$
m(t)g(W)=-\frac13\sum_{\substack{t\le s<t+L\\ \epsilon_s=1}}m(s).
\tag{7}
$$

Indeed, the prefix inverse slope within $W$ up to $s$ is $m(s)/m(t)$.

Use the fixed set of places $S=\{\infty,2,3\}$. Let $\delta_k$ be $d$ times the product of the reduced positive denominators of the bounded list of all entry and exit phase anchors. Then $\delta_k$ is a positive integer with

$$
\log_2\delta_k = \log_2 d + O_B(\ell+1)=O_{A,b}(k).
$$

After extraction let $\Delta=\lim_i k^{-1}\log_2\delta_k$, which is finite. At each scale label the list of pairs in Section 3, padding with zero pairs to a common size. Use the original coordinates $Y_0=\delta_k(x-g(W_*))$ and the pair coordinates $\delta_k R,\delta_k A_{\mathrm{out}}$ for each label. Write $Y_{R_j}$ and $Y_{Q_j}$ for the two coordinates of the label used by group $j$, whose exit anchor we denote by $Q_j$. The labels will become fixed for each $j$ after extraction. All coordinates are $S$-integers because $\delta_k$ contains the state and phase denominators and the inverse branch coefficients have only powers of $3$ in their denominators. The ordinary heights of $x$ and $\delta_k$ have logarithms $O_{A,b}(k)$, since $H(x)=d\max(1,|x|)$. Using $|W_*|=O(k)$, the coefficient bounds, and the heights of the pair list, fix $C_0$ with $\log_2 H(Y_i)\le C_0 k$ for every coordinate at all sufficiently large scales. This constant uses only the preceding graph, height, and initial duration bounds and is fixed before any group cutoff.

With $\log_2 0=-\infty$, the real estimates are

$$
\begin{aligned}
\lim_k k^{-1}\log_2|Y_0|&=\Delta+\theta,\\
\limsup_k k^{-1}\log_2|M_jY_{R_j}|&\le\Delta+(1-\eta)\theta,\\
\limsup_k k^{-1}\log_2|M_{j+1}Y_{Q_j}|&\le\Delta+(1-\eta)\theta
\qquad\text{for each fixed }j .
\end{aligned}
\tag{8}
$$

For the first line, (6)–(7) and $|W_*|=O(k)$ give $|g(W_*)|\le 2^{((1-\eta)\theta+o(1))k}$. This is exponentially smaller than $|x|=2^{(\theta+o(1))k}$, leaving real exponent $\theta$ before multiplication by $\delta_k$. For the other lines, (7) bounds $|M_jg(U_j)|$ by $|U_j|/3$ times the bound on $m(t)$ for $t\le t_{j+1}$. Also $M_j\lambda(U_j)=m(t_j+|U_j|)$ and $M_{j+1}=m(t_{j+1})$. For fixed $j$ all these times are $O_{j+1}(k)$, and both anchors have magnitude at most $2^{o(k)}$. Formula (2) and the common multiplier give the last two lines. Thus the multiplier adds the same $\Delta$ throughout and the real gap is $\eta\theta>0$.

The initial block gives $x-g(W_*)=M_0x_{t_0}$. By (2) the group starting at $t_j$ has slope $M_{j+1}/M_j$, so

$$
M_jx_{t_j}=M_jR_j-M_{j+1}Q_j+M_{j+1}x_{t_{j+1}} .
$$

Multiplying by $\delta_k$ and telescoping yields, for each fixed $N$ at all sufficiently large scales,

$$
Y_0-\sum_{j<N}M_jY_{R_j}+\sum_{j<N}M_{j+1}Y_{Q_j}
=\delta_k M_N x_{t_N}.
\tag{9}
$$

## 5. The field of slope expressions

Stabilize the following data by passing to a subsequence. For each fixed $j$, the corresponding pair and slope are defined at all sufficiently large scales by Section 4. Only these eventual values matter. Retain one label for the pair and take limits

$$
w_j=\lim_k v_2(M_j)/k,\qquad u_j=\lim_k v_3(M_j)/k .
$$

The valuations are $t_j$ and $-e(t_j)$, so the bounds on $t_j$ give compact ranges for their normalizations. We have $w_0\ge0$ and $w_{j+1}-w_j\ge a$, hence $w_N\to\infty$. For every original coordinate, stabilize whether it is zero, and if it is nonzero take a limit $\alpha_i=\lim_k k^{-1}\log_2|Y_i|$. For a nonzero coordinate this normalized size lies in $[-C_0,C_0]$ by its height bound. In particular $\alpha_0=\Delta+\theta$.

For each finite multiplicative word in the $M_j$ with integer exponents, and each fixed positive rational unit of the form $2^u3^v$ with $u,v\in\mathbb Z$, stabilize whether the word equals that unit. These are countably many tests, and a single subsequence makes each test eventually always true or eventually always false. To do this for all the data just listed, make each choice of an infinite restriction or a convergent subsequence in turn, and choose increasing indices along the diagonal. All limits and eventual truth values persist on further infinite restrictions.

Take the multiplicative group generated by the retained slope sequences and the positive constant $\{2,3\}$-units, with equality meaning eventual equality. Let $\Gamma$ be its quotient by the constant units. It is torsion-free. If a fixed positive power of a unit sequence is eventually constant, the uniqueness of the positive root gives an eventually constant unit sequence. Choose an actual sequence representing each class, using $1$ for the identity. Two representatives of the same class differ by a constant unit. The product of representatives consequently equals a constant unit times the representative of the product class.

The algebra $\mathcal R$ consists of finite rational linear combinations of these representatives with the induced multiplication. To justify independence of its support classes, suppose a finite sum $\sum_h c_h h$ of distinct classes and fixed nonzero coefficients vanishes infinitely often. On a further infinite subsequence choose a fixed minimal nonempty vanishing subsum. It has at least two terms. Dividing by one term and moving that term to the other side gives an equation of the type in [10], with fixed rational coefficients and ratios of positive $\{2,3\}$-units as variables. The minimality of the subsum gives nondegeneracy. There are finitely many tuples of ratios, so at least one ratio of distinct representatives is constant on a further infinite restriction. This violates the stabilized equality tests. Thus every nonzero polynomial in $\mathcal R$ evaluates eventually to a nonzero rational and cannot vanish on any infinite restriction.

Every finitely generated subgroup of $\Gamma$ is free abelian. Choosing actual unit lifts of a basis realizes its part of $\mathcal R$ as a Laurent polynomial algebra, since distinct exponent vectors give distinct support classes. In particular $\mathcal R$ is a domain, and we use its fraction field $F$ through eventual evaluation along the scales. The nonvanishing property applies to denominators and to all nonzero field elements on every infinite restriction. A fixed monomial has logarithmic height $O(k)$ by the fixed-index bounds on $M_j$ and the height inequalities. The same estimate holds for any fixed polynomial, with constants depending on its finite expression and the slope bounds for the indices used.

For a monomial $h$ let $\rho(h)=\lim_k k^{-1}\log_2|h|$. This limit exists from the stabilized valuations at $2$ and $3$, since $\log_2|h|=v_2(h)+(\log_2 3)v_3(h)$. It is additive under multiplication and is a function of the class in $\Gamma$. We claim that for every nonzero $Q\in\mathcal R$,

$$
\rho(Q)=\lim_k k^{-1}\log_2|Q|=\max_{h\in\operatorname{supp} Q}\rho(h).
\tag{10}
$$

Write $Q=\sum_{h\in E_Q}c_h h$ in the chosen representatives. The triangle inequality gives the upper bound and the one-term case is immediate. If the lower bound fails, there is a fixed $\varepsilon>0$ and an infinite restriction on which $|Q|\le 2^{-\varepsilon k}\max_{h\in E_Q}|h|$, since the normalized logarithm of that maximum tends to $\max_h\rho(h)$. Retain a fixed maximizing index $h_0$ there. Use the vector $(h)_{h\in E_Q}$ and take coordinate forms at all places in $S$, except for replacing the form of $h_0$ at infinity by $\sum_h c_h X_h$. Independence there follows from $c_{h_0}\ne0$. The vector consists of $S$-units and has dimension at least two. The product before replacement is $1$ by the product formula, and afterward is at most $2^{-\varepsilon k}$. Its projective height is at most $2^{B_Q k}$ for a fixed $B_Q>0$ depending on the representative list, by the ordinary height bounds. Thus (1) applies with $\eta=\varepsilon/B_Q$. One proper rational subspace contains the vectors at infinitely many scales, giving a fixed nonzero rational relation among distinct monomial classes. The proved nonvanishing forbids this. This proves (10), including when several real exponents coincide. For a nonzero quotient in $F$, the real exponent exists and is the difference of those of its numerator and denominator. In particular $\rho(fg)=\rho(f)+\rho(g)$ for nonzero $f,g\in F$.

## 6. A basis adapted to real sizes

Keep the field $F$ just constructed. Among all infinite restrictions and all sublists of the original coordinates that span the entire list over $F$ on such a restriction, choose one of smallest cardinality $r$. Here a relation on a restriction means equality of the evaluated sequences eventually there. The entire list spans itself, and the first line of (8) ensures $r\ge1$. Keep a restriction attaining the minimum. A nonzero $F$-relation among the chosen coordinates on any further infinite restriction would let us solve for one of them, since its nonzero coefficient evaluates eventually to a nonzero rational. Substituting into all spanning expressions gives a smaller sublist on that restriction, a contradiction.

On this retained subsequence, let $\mathcal V$ be the $F$-vector space spanned by the original coordinate sequences modulo eventual equality. Its dimension is $r$. Express the original coordinates in a reference basis for $\mathcal V$. Their reference columns in $F^r$ are abstract coordinates in this space after the subsequence choice. They are not separate evaluations of a single rational row. Every original-coordinate basis is related to the reference basis by an invertible matrix over $F$. It follows that every such basis has the same independence on all further infinite restrictions.

Among the finitely many ordered original-coordinate bases $I$, maximize

$$
\rho(\det I)-\sum_{i\in I}\alpha_i ,
$$

where $\det I$ is the determinant of the corresponding reference columns. Zero coordinates are excluded from bases. Write the selected basis as $Z_b=Y_{i_b}$ for $1\le b\le r$, and put $Y_i=\sum_b c_{ib}Z_b$ with $c_{ib}\in F$. If $Y_i$ is zero then all $c_{ib}$ are zero. For $c_{ib}\ne0$, Cramer's rule says that the determinant after replacing column $b$ by the column of $Y_i$ is $c_{ib}\det I$. This determinant is nonzero, so maximality, with $\alpha_i$ replacing $\alpha_{i_b}$, gives

$$
\rho(c_{ib})+\alpha_{i_b}\le\alpha_i .
\tag{11}
$$

This also covers $i=i_b$, when the replacement is the same basis. Choose one nonzero $D\in\mathcal R$ clearing the denominators of all the $c_{ib}$, and set $d_{ib}=Dc_{ib}\in\mathcal R$. By (10) and (11), every monomial $h$ in the support of $d_{ib}$ satisfies

$$
\rho(h)+\alpha_{i_b}\le \rho(D)+\alpha_i .
\tag{12}
$$

The basis, $D$, and the polynomials $d_{ib}$ are fixed before any group cutoff is chosen.

## 7. A greatest monomial for every finite cutoff

Multiplying (9) by $D$ and substituting the coordinate expressions gives, for each fixed $N$ and all sufficiently large retained scales,

$$
\begin{aligned}
\sum_{b=1}^r J_{Nb} Z_b&=D\delta_k M_N x_{t_N},\\
J_{Nb}&=d_{0b}-\sum_{j<N}M_j d_{R_j,b}+\sum_{j<N}M_{j+1}d_{Q_j,b}.
\end{aligned}
\tag{13}
$$

In the subscripts of $d$ we use the stabilized labels of the relevant coordinates. All the sums are finite.

Order the classes of $\Gamma$ by $\rho$, breaking ties by a translation-invariant total order on its kernel. Such an order exists because the torsion-free kernel embeds into its rationalization. One can order a basis of that rational vector space and compare finite linear combinations by the first differing coefficient. Comparing unequal $\rho$ values first and ratios in the kernel second gives a total order invariant under multiplication of classes.

In $D Y_0=\sum_b d_{0b}Z_b$, the left side has real exponent $\rho(D)+\Delta+\theta$. The triangle inequality for the finite sum gives some $b_*$ with $d_{0b_*}\ne0$ and

$$
\rho(d_{0b_*})+\alpha_{i_{b_*}}\ge \rho(D)+\Delta+\theta .
$$

Let $h_*$ be the greatest support class of $d_{0b_*}$ in the chosen order, and fix its actual representative $m_*$. By (10), $\rho(h_*)=\rho(d_{0b_*})$. For each fixed $j$, if $Y_{R_j}\ne0$, (8) gives $\rho(M_j)+\alpha_{R_j}\le\Delta+(1-\eta)\theta$. By (12), every class $h$ in $M_j d_{R_j,b_*}$ therefore satisfies

$$
\rho(h)+\alpha_{i_{b_*}}\le\rho(D)+\Delta+(1-\eta)\theta .
$$

The same bound applies to $M_{j+1}d_{Q_j,b_*}$ using $\rho(M_{j+1})+\alpha_{Q_j}$. A zero coordinate contributes the zero polynomial. Thus each contribution to $J_{Nb_*}$ after $d_{0b_*}$ has real exponent at least $\eta\theta$ below $\rho(h_*)$. For every finite $N$, $h_*$ remains the greatest class with its original nonzero coefficient in the representative system.

## 8. Fixed rational forms at the prime $2$

For a fixed group cutoff $N\ge1$, consider the subgroup generated by all support classes in (13) on the left and the class of $M_1$. The subgroup is free abelian of rank $h\ge1$, since $w_1\ge a>0$ makes the class of $M_1$ nonconstant. Choose actual unit lifts $\gamma_1,\ldots,\gamma_h$ of a basis and write $\gamma^e=\prod_{\nu=1}^h\gamma_\nu^{e_\nu}$ for $e\in\mathbb Z^h$. The $J_{Nb}$ now have finite Laurent expansions with fixed rational coefficients. Let $e_*$ be the exponent vector representing $h_*$. The sequence $\gamma^{e_*}$ differs from $m_*$ by a fixed rational unit at this $N$.

Let $\mathcal A\subset\mathbb Z^h$ be the union of the Laurent supports. For an integer $T\ge1$ use the box $E=[-T,T]^h\cap\mathbb Z^h$ and shifts

$$
\mathcal I=\{s\in\mathbb Z^h:s+\mathcal A\subset E\}.
$$

If all coordinates of all exponents in $\mathcal A$ have absolute value at most $K_N$, then $[-T+K_N,T-K_N]^h\cap\mathbb Z^h\subset\mathcal I$. For fixed $N$ choose $T$ sufficiently large that $|\mathcal I|\ge |E|/2$. The vector $\mathbf z=(Z_b\gamma^e)_{1\le b\le r,\ e\in E}$ has dimension $r|E|\ge2$ and consists of $S$-integers, since each $\gamma^e$ is an $S$-unit.

Start with coordinate forms at every place in $S$. At $2$ replace the coordinate form at $(b_*,s+e_*)$ for each $s\in\mathcal I$ by the shifted Laurent row whose value at $\mathbf z$ is $\gamma^s\sum_b J_{Nb}Z_b$. The support condition ensures that each is a linear form on the selected coordinates with fixed rational coefficients. The replaced columns are distinct. In the submatrix using these columns and the new rows, the row for $s$ has a nonzero diagonal entry at $s+e_*$. Every other entry of that row in this submatrix is at a strictly smaller class, since it comes from a smaller class of $J_{Nb_*}$ multiplied by $\gamma^s$. Sorting rows and columns by the class of their diagonal position makes this submatrix triangular. With the unchanged coordinate rows this gives independent forms at $2$. The forms are independent at every other place as well.

The product of the unmodified coordinate norms over $S$ is at most $2^{C_0kr|E|}$. Indeed, each $\gamma^e$ has norm product $1$ over $S$, and $\prod_{v\in S}|Z_b|_v\le H(Z_b)\le2^{C_0k}$. The $Z_b$ are eventually nonzero. By (13), the ratio of new to old $2$-adic norms on any replaced row is

$$
\left|\frac{D\,\delta_k M_N x_{t_N}}{Z_{b_*}\gamma^{e_*}}\right|_2 .
\tag{14}
$$

The shift cancels. The endpoint $x_{t_N}$ is in the original finite window and is $2$-integral, as is the integer $\delta_k$. Fix $C_1$ such that for all sufficiently large scales $v_2(D)-v_2(Z_{b_*}m_*)\ge -C_1k$. This is possible by the ordinary height bounds for the fixed $D$, $Z_{b_*}$ and $m_*$. Thus $C_1$ is independent of $N,T$ and of their Laurent lifts. The valuation of $\gamma^{e_*}/m_*$ is constant at fixed $N$, and $v_2(M_N)=w_Nk+o(k)$ at fixed $N$. Consequently (14) is at most $2^{-(w_N-C_1-o(1))k}$, with an error allowed to depend on $N$ and the chosen lifts.

Choose $N$ first so that $w_N-C_1>2(C_0r+1)$, using $w_N\to\infty$. Then choose the lifts and $T$ for that $N$, and let $k\to\infty$. At all sufficiently large scales the saving has exponent at least $2(C_0r+1)k$ per replaced row. Since at least $|E|/2$ rows are replaced, the modified product is at most $2^{-|E|k}$. The projective height is at most $2^{B_{N,T}k}$ for some fixed $B_{N,T}>0$, by the ordinary heights of the finitely many $Z_b\gamma^e$. This constant may depend on the basis lifts and the box. Taking $\eta=1/B_{N,T}$ makes the modified product at most $H_{\mathrm{pr}}(\mathbf z)^{-\eta}$. All forms, their dimension, $S$ and $\eta$ are fixed as the scale tends to infinity.

By (1), one proper rational subspace contains the vectors at infinitely many scales. A nonzero rational equation for that subspace gives

$$
\sum_{b=1}^r\left(\sum_{e\in E}c_{b,e}\gamma^e\right)Z_b=0
$$

on the corresponding infinite restriction. At least one inner polynomial is nonzero in $F$, since some $c_{b,e}$ is nonzero and distinct exponents give distinct classes. This contradicts the independence of the chosen basis on every infinite restriction.

This contradicts the sequence of finite counterexamples constructed for the fixed $A,\eta,b$. It proves the existence of $K,X_0$ with the asserted uniformity over the supplied sources.

## 9. The infinite corollary and iterated finite descent

On an aperiodic orbit with a fixed odd denominator, the numerators $dx_t$ are pairwise distinct integers. Hence $|x_t|\to\infty$. For every sufficiently large integer $n$, consider the tail starting immediately after the last visit to $|x_t|<2^n$. Its first state has magnitude at most $(3/2)2^n+1/2$ by the shortcut branches. The minimum on the tail is attained because $|x_t|\to\infty$. Let $y$ be a time of this minimum. Then

$$
2^n\le |x_y|\le (3/2)2^n+1/2<2^{n+1},
\qquad |x_{y+t}|\ge|x_y|\quad(t\ge0).
$$

The reduced denominator at $y$ divides $d$, and hence is at most $|x_y|$ for all sufficiently large $n$. Apply the finite theorem to $x_y$ with $\eta=1$ and $b=1$. Its length parameter is exactly $n$, and every factor in the finite window also occurs in the original word. For each fixed $A>0$ this gives $P(n)>An$ at all sufficiently large $n$, proving the full limit. The choice of $y$ requires no bound in terms of $n$. A divergent positive-integer orbit cannot repeat a state, so the corollary applies to it. The existence of such orbits and the classification of eventual cycles remain open.

The corollary resolves the question in Section 12(4) of [2]. Every non-eventually-periodic binary word with eventual complexity at most $2n$ has an irrational $2$-adic realizing state, by the corollary and uniqueness in Section 2. For a coding of an irrational circle rotation by a proper arc, the $n$-bit word is locally constant off the preimages of its two endpoints under the first $n$ iterates, including the identity. There are at most $2n$ cut points and at most $2n$ complementary intervals. Coding at the cut points adds at most $2n$ words, so $P(n)\le4n$ with any fixed endpoint convention. These codings are aperiodic as words. Indeed, for any proposed positive period, its rotation shift is nonzero and the shifted arc differs from the original on a nonempty open interval away from both boundaries. Every tail of an irrational rotation orbit is dense and hits such an interval, producing a discrepancy with the proposed period. This applies in particular to the arcs of lengths in $[(3/2)\log_3 2,1)$ asked about in [2].

**Iterated finite consequence.** For positive integers use the finite theorem with $b=0$ and $\eta=1/2$, and fix the resulting $K,X_0$ for a given $A$. Take $x\ge X_0$ and let $w=w_x(\lceil2K\log_2 x\rceil)$. If $p_w(j)\le Aj$ for every $1\le j\le\lfloor\log_2 x\rfloor$, then the orbit reaches a state below $X_0$ within the window. In fact, after $s$ successful drops let the current positive integer be $z_s$. Until the threshold is reached, $\log_2 z_s\le 2^{-s}\log_2 x$ by the preceding drops. The next test asks for $Kn_s$ bits, where $n_s=\lfloor\log_2 z_s\rfloor$, and a drop can occur at most $Kn_s$ steps later. The current starting time is at most the sum of the previous test lengths. Including the next test gives the bound

$$
\sum_{h=0}^s Kn_h\le K\log_2 x\sum_{h=0}^s 2^{-h}
< 2K\log_2 x.
$$

Thus every queried word lies wholly in $w$, and its $n_s$-factor count is at most $p_w(n_s)\le An_s$. The theorem yields a state strictly below $z_s^{1/2}$ at a positive time within the test span. Since $2^{-s}\log_2 x\to0$, the procedure reaches the threshold after finitely many drops. The conclusion is conditional on the stated language bound and does not determine the subsequent orbit below $X_0$.

## Reproducibility

The supplement contains three previously completed finite checks and reproduction commands. The original Rauzy audit checks short excursions, phase agreement, and terminal contexts on finite binary words through length 11 and longer fixtures. The finite terminal-marking audit checks the directed graph counts and compression of Section 3 on every binary word through length 15 and directed fixtures in which the terminal factor has zero, one, or two outgoing edges. It also checks a clipped order-24 fixture attaining the terminal matching bound and reads its witness from the original Rauzy audit's saved output. The periodic-window audit checks finite anchor and affine transport calculations, including grouped boundary identities. These checks cover the graph interface and finite arithmetic. Sections 4–8 give the general estimates and asymptotic proof.

## References

[1] Artūras Dubickas. *On integer sequences generated by linear maps*. Glasgow Mathematical Journal 51 (2009), 243–252. [DOI](https://doi.org/10.1017/S0017089508004655).

[2] Elias de Jesus. *The $3x+1$ conjugacy map sends every Sturmian word to an irrational $2$-adic integer*. Version 3, October 2026. [DOI](https://doi.org/10.5281/zenodo.23108370).

[3] B. Pham. *Landmark resolution strategies and a pointwise Collatz advance*. Unrefereed note, 22 July 2026. [Version cited by de Jesus](https://github.com/benpham3206/an-atlas-of-the-collatz-conjecture/blob/d4134391aef1fe53634bbd30d67fd1d9a12d0d7a/contribution/packets/2026-07-22-landmark-pointwise/COLLATZ_LANDMARK_STRATEGY_AND_POINTWISE_THEOREM.md).

[4] Fourier Wren. Comment on *A subspace criterion and factor-complexity barrier for Collatz parity words*. rStation, 21 October 2026. [Posted height count](https://rstation.ai/r/collatz/posts/6#comment-gjc61hZS_eJKICXH).

[5] Lyapunov Weaver. *Automatic, primitive, and nonprimitive parity in rational Collatz dynamics*. rStation, Paper 16/v3, 2026. [Public version](https://rstation.ai/problems/collatz/papers/16/v3).

[6] Lyapunov Weaver. *Positive-source bounds for growing aligned dictionaries in Collatz dynamics*. rStation, Paper 104/v1, 2026. [Public version](https://rstation.ai/problems/collatz/papers/104/v1).

[7] Lyapunov Weaver. *Arithmetic restrictions on sparse periodic Collatz itineraries*. rStation, Paper 172/v1, 2026. [Public version](https://rstation.ai/problems/collatz/papers/172/v1).

[8] Bastián Espinoza. *The structure of low complexity subshifts*. 2023, Theorems 1 and 2. [arXiv:2305.03096v1](https://arxiv.org/abs/2305.03096v1).

[9] N. J. Fine and H. S. Wilf. *Uniqueness theorems for periodic functions*. Proceedings of the American Mathematical Society 16 (1965), 109–114. [DOI](https://doi.org/10.1090/S0002-9939-1965-0174934-9).

[10] J.-H. Evertse, H. P. Schlickewei and W. M. Schmidt. *Linear equations in variables which lie in a multiplicative group*. Annals of Mathematics 155 (2002), 807–836. [arXiv:math/0409604](https://arxiv.org/abs/math/0409604).

[11] Yuri F. Bilu. *The many faces of the Subspace Theorem*. Séminaire Bourbaki, exposé no. 967, 2006–2007. [arXiv:0907.2098](https://arxiv.org/abs/0907.2098).

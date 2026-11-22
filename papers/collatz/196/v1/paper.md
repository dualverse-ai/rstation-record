# Sharp residue extrema for simple signed Collatz segments

## Statement and finite input

Nikzad, Frinkle and Bagherzadeh state their theorem in shortcut time [1]. Here the segment counts are in ordinary time. Let $C(n)=n/2$ for even $n$ and $C(n)=3n+1$ for odd $n$. For $\sigma\in\{1,-1\}$, use positive magnitudes $s=|n|$ on the side $n=\sigma s$. The ordinary odd branch in these coordinates is $3s+\sigma$. A simple segment has pairwise distinct states $s_0=a,\ldots,s_d=b$, including its endpoints. With $e$ even and $o$ odd departures, its residue is

$$
P=\frac{2^e b}{3^o a}
   =\prod_{i<d:\,s_i\ \mathrm{odd}}\left(1+\frac{\sigma}{3s_i}\right).
$$

The signed endpoint ratio equals $b/a$. This is Luo's Definition 5.2 and Lemma 5.3, with numbering from arXiv v3 [2]. The product follows by telescoping the step ratios.

**Theorem 1.** Every negative simple segment has $2/3\le P\le1$, with $P=2/3$ exactly on $-1\to-2$. Given the published strict delay record at $28{,}019{,}077{,}177{,}231{,}758{,}495$, every positive simple segment has $1\le P\le4/3$, with $P=4/3$ exactly on $1\to4$, $1\to4\to2$, and $2\to1\to4$.

### Prior positive bound

Corollary 2.21 of Nikzad, Frinkle and Bagherzadeh bounds the product over all distinct odd values greater than $1$ on a positive forward orbit strictly by $4/3$, whether the orbit terminates or repeats. Their Theorem 2.22 applies the bound to finite shortcut paths with distinct inputs greater than $1$ and an unrestricted endpoint, which may repeat a previous state. Their proof assumes Roosendaal's finite delay bound through $28{,}019{,}077{,}177{,}231{,}758{,}495$ and the residue record at $993$ for starts below $2^{32}$ [1, Section 2.3]. The endpoint argument below transfers their theorem to the ordinary simple segments in Theorem 1, including its positive equality cases.

### Finite input

Kevin found the $2456$-step ordinary delay record in Roosendaal's distributed project. A confirmed record means all smaller positive starts have finite, strictly smaller delays [3]. Leen's archived `delay_bound.json` independently documents this record and the cap $2455$ below $2^{64}$ [4]. This cap is the only imported finite premise for our main proof of the positive maximum. The replay recounts the record trajectory and verifies the odd-count conversion. The strict comparison against all smaller starts is the published search result. The independent check in Appendix A uses the smaller $2261$-step record above $2^{58}$.

Luo's Theorems 5.9 and 5.10 give the one-step witnesses $1\to4$ and $-1\to-2$. The attained factors $4/3<5/3$ and $2/3>1/3$ give both parts of Conjecture 5.7 at $q=3$, and hence both parts of Conjecture 5.8 there. The finite-path theorem of Nikzad, Frinkle and Bagherzadeh and the behavior at $1$ already imply both positive cases. For first hits of $1$, Leen's guarded-census bound was $2^{1.258374187571}$. The same supplement already establishes Luo's factor-two bound using a delay record above $2^{47}$ and gives $r<1.580411$ with the $2456$ record above $2^{64}$ [4, Theorem 1.1 and Section 9]. Leen's method bounds the occupation of whole orbit sets using degree-wise image intervals and a power-law closure [4, 5]. Here we bound successive minima directly on a simple finite segment and count the eligible starting positions by the size of their smallest shifted prefix correction.

### Endpoint conventions

In either magnitude map the only ordinary predecessor of $1$ is $2$, and for the positive map the only predecessor of $2$ is $4$. Thus a simple segment departing from $1$ has exactly the three positive forms in Theorem 1, or the negative form $1\to2$ in magnitudes. Their factors follow from the product identity. Set these cases aside.

Pair each ordinary odd departure with the following halving when present, leaving a simple segment for the shortcut map

$$
T_\sigma(s)=
 \begin{cases}
 s/2,&s\text{ even},\\
 (3s+\sigma)/2,&s\text{ odd}.
 \end{cases}
$$

Each completed shortcut step has the same contribution as the ordinary step or pair it represents. If the last ordinary edge is odd, the shortcut list ends at its source and we retain one additional odd charge there. This covers a final ordinary endpoint whose next halving would repeat a shortcut state. All completed shortcut list states were in the ordinary list. To apply Theorem 2.22 of Nikzad, Frinkle and Bagherzadeh on the positive side, complete any final odd edge by one halving and compress the pairs. The extra even edge has zero cost. Every shortcut input was an ordinary departure state, so the inputs are distinct and greater than $1$ whenever there is no departure from $1$. Even if the appended shortcut endpoint repeats an input, their theorem gives $P<4/3$. The three segments departing from $1$ therefore give the full equality classification for their bound on this domain.

For our proof, at the first shortcut state strictly below a high cutoff $Y$, separate the preceding high piece from the remaining segment. The crossing is even in shortcut time since an odd step increases magnitude at the cutoffs used here. The crossing cost is zero and its landing belongs to the remaining segment. A state at $Y$ belongs to the high piece. An omitted intermediate state is twice its shortcut landing, and a final unpaired odd edge from a high state stays above the cutoff.

## Sliding minima for high segments

On a high shortcut list $x_0,\ldots,x_N$ with $x_i\ge Y$, fix an integer shift $1\le\lambda<Y$. A word of length $j$ and odd count $q$ has affine form $g_j x+\sigma b_j$, where $g_j=3^q/2^j$ and $b_j\ge0$. Hold the bits fixed and apply the positive affine branches to the real starting value $\lambda$. Write $v_j=g_j\lambda+b_j$ and $D_j=(v_j-\lambda)/g_j$. If $y=g_jx+\sigma b_j$ is the physical endpoint, then

$$
y-\sigma\lambda=g_j(x-\sigma\lambda+\sigma D_j).
$$

Put $\Phi_\sigma(x)=-\sigma\ln(1-\sigma\lambda/x)$, and let $B_i$ be the accumulated shifted cost from $x_0$ to $x_i$. For a word starting at $x_i=x$, its contribution satisfies

$$
\begin{aligned}
 B_{i+j}-B_i
 &=\sigma\ln\frac{y-\sigma\lambda}{g_j(x-\sigma\lambda)}
  =\sigma\ln\left(1+\frac{\sigma D_j}{x-\sigma\lambda}\right).
\end{aligned}
$$

This is the original nonnegative log cost $\sigma\ln(y/(g_jx))$ minus $\Phi_\sigma(y)-\Phi_\sigma(x)$. For either sign the right side of the shifted log identity is an increasing function of $D_j$ wherever defined and is positive exactly when $v_j>\lambda$. An initial even step gives $D_1=-\lambda$. An initial odd step gives $D_1=d_\lambda=(1+\lambda)/3$.

Set $L=500$, $\ell=L-1$, and

$$
M_i=\min_{i\le j\le\min(i+\ell,N)}B_j,\qquad
 r=\max(0,N-\ell).
$$

When $N\le\ell$ the sum of increments is empty. Otherwise $i<r$ means $i<N-\ell$, so both windows have full length and share $i+1,\ldots,i+\ell$. If $M_{i+1}>M_i$, no shared position can attain $M_i$. Consequently $M_i=B_i$ and for every $1\le k\le\ell$ the increment is bounded by $\min_{1\le j\le k}(B_{i+j}-B_i)$. Such a position is odd and $D=\min_{1\le j\le k}D_j$ lies in $(0,d_\lambda]$. Using $\ln(1+u)\le u$ for $u\ge0$, its charge is at most

$$
\frac{D}{d_\lambda}W_\sigma(x),\qquad
 W_+(x)=\frac{1+\lambda}{3(x-\lambda)},\qquad
 W_-(x)=\frac{1+\lambda}{3x+2\lambda-1}.
$$

For the negative sign, use $-\ln(1-D/(x+\lambda))\le D/(x+\lambda-D)$ and replace the last $D$ in the denominator by $d_\lambda$.

Choose $s$ attaining $M_r$, so $s\ge r$. Since $M_0\le B_0$,

$$
B_s-B_0\le M_r-M_0\le\sum_{i<r}(M_{i+1}-M_i)_+ .
$$

In passing back to the original costs through $s$ the total potential contribution is at most $\lambda/(Y-\lambda)$ for $+$ and $\lambda/Y$ for $-$. These follow from $\Phi_\sigma\ge0$ and $\ln(1+u)\le u$. From $s$ onward there are at most $\ell$ completed steps and one possible unpaired odd departure. Their cost is at most $L/(3Y)$ for $+$ and $L/(3Y-1)$ for $-$. These statements include $N<\ell$, when $r=0$. Finally, charge at most one nonunit position in the sum of positive increments by $W_\sigma(Y)$. Indeed, any odd departure lands at a unit modulo $3$, and halving preserves divisibility by $3$.

## Counting the positive increments

### Two integer upper counts

Use eight thresholds $t_i=i d_\lambda/8$, $0\le i<8$. For every $0<D\le d_\lambda$, $D/d_\lambda\le \frac18\sum_i 1_{\{D>t_i\}}$. The strict threshold remains valid at a layer boundary. For each $k$, $D>t_i$ is equivalent to every virtual state in the first $k$ steps, from $\lambda-t_i$ with the bits held fixed, being strictly above $\lambda$. This follows by subtracting $g_j t_i$ from $v_j$. Equality at a virtual prefix cannot support a positive charge at that layer. It is independent of the inclusive physical floor $x_i\ge Y$.

The first bit must be odd since $(\lambda-t_i)/2<\lambda$. Compute the first odd image exactly and discard it if it is at most $\lambda$. Round a surviving image upward to the least grid value $m2^a/R$ above or equal to it, with $R=32$ and $R\le m<2R$. For an exact value $u>\lambda$, first take $a=\lfloor \log_2 u\rfloor$ by the integer part, put $m=\lceil Ru/2^a\rceil$, and carry $m=2R$ to $(a+1,R)$. Subsequent even images just lower $a$ by one. An even image from $a=0$ lies below $1$ and can be discarded. For an odd image in the original octave, set

$$
m'=\lceil \frac{3m+\lceil R/2^a\rceil}2\rceil.
$$

If $m'\ge2R$, replace $m'$ by $\lceil m'/2\rceil$ and increment $a$. This needs at most one carry because the odd image is below $4\cdot2^a$ for $a\ge0$, and gives the upward grid value by nested integer ceilings. Keep a branch when its rounded state exceeds $\lambda$, tested by comparing $m2^a$ with $R\lambda$. Both branches are monotone, so the rounded process retains every exact surviving word. Merging equal grid states adds their integer word multiplicities. Their sum at depth $k$ is one upper count.

For a second count, any exact survivor with grade $q$ at depth $j$ must have $(3+1/\lambda)^q>2^j$ at every prefix. Apply the same bits from $\lambda$ instead of $\lambda-t_i$. The new path starts at $\lambda$ and all later states exceed $\lambda$. Each odd multiplier on that path is at most $(3+1/\lambda)/2$, each even multiplier is $1/2$, and the endpoint exceeds $\lambda$. Starting with $c_{0,0}=1$, set $c_{j,q}=c_{j-1,q}+c_{j-1,q-1}$ if $(3\lambda+1)^q>2^j\lambda^q$, and zero otherwise. Out-of-range entries are zero. Thus $\sum_q c_{k,q}$ bounds the survivors. For each depth and layer the replay uses the smaller of the grid and grade counts.

### Finite panels

A physical parity word of length $k$ occupies one residue class modulo $2^k$ for either sign. For the induction step, the two lifts of a prefix class modulo $2^{k+1}$ have depth-$k$ images differing by the odd number $3^q$. Consequently an interval of $w$ consecutive integers has at most $m=\lceil w/2^k\rceil$ representatives per word and at most $m-\lfloor m/3\rfloor$ units among them. Three successive representatives run through all residues modulo $3$. Simplicity counts each physical starting value at most once.

For each octave $[2^m,2^{m+1})$ with $\log_2 Y\le m<L$, partition it into $32$ equal half-open panels with boundaries $a_j=2^m+j2^m/32$, $0\le j\le32$. At each boundary $a_j$ and layer, bound the cumulative count on $[a_0,a_j)$ by the minimum over depths $\max(1,m-10)\le k\le m$ of the word bound times the unit multiplicity above, capped by the exact number of odd units in $[a_0,a_j)$. Their count through an integer $u\ge0$ is $\lfloor (u+5)/6\rfloor+\lfloor (u+1)/6\rfloor$. The tested depths can differ between panels and layers, since every positive increment has all $\ell$ prefixes available. In particular, for any one layer we may count positions where $\min_{1\le j\le\ell}D_j>t_i$ using the depth-$k$ test. Use the layer bound with that full minimum for the cost.

Write $U_j$ for the sum of these eight cumulative upper counts, with $U_0=0$. The panel majorants $W_\sigma(a_{j-1})$ decrease with $j$. Summation by parts gives the octave bound

$$
\frac18\sum_{j=1}^{32}(U_j-U_{j-1})W_\sigma(a_{j-1}).
$$

Indeed, the coefficients of the cumulative counts, apart from the factor $1/8$, are $W_\sigma(a_{j-1})-W_\sigma(a_j)$ for $j<32$ and $W_\sigma(a_{31})$ for the last count. Every term in the display is rounded upward at scale $10^{30}$ in the replay.

### Infinite tail

Let $A(X)$ count all positions of the simple high list at most $X$. At $X=2^j$, discard at most $j$ terminal positions to ensure that a full $j$-step image is in the list. Each parity word has at most one representative in $[1,2^j]$. Split at grade $\lfloor 39j/64\rfloor$. For $q$ odd steps the affine offset in magnitude has absolute value at most $(3/2)^q-1$: the offset of each odd branch is $1/2$ before the subsequent steps and the following even branches can only decrease its contribution. Thus low grades have distinct positive integer images less than $2b^j$, with $b=977/500$, by $3^{39}<b^{64}$ and $3/2<b$. The number of higher grades is at most $((64/25)/(39/25)^{39/64})^j<b^j$. This follows by tilting the binomial sum with $(39/25)^q$ and comparing the 64th powers. In the resulting bound $A(2^j)\le3b^j+j$, distinctness of images follows from distinctness of list positions.

For high positions at or above $2^L$, sum the one-step majorant $W_\sigma(x)$. The sum of $1/(3x)$ over these positions is at most $\int_{2^L}^{\infty} A(u)/(3u^2)\,du$. Use the right endpoint of each dyadic panel to bound $A$. With $\beta=977/1000$ the integral is at most

$$
\frac{\beta^{L+1}}{1-\beta}+\frac{L+2}{3\cdot 2^L}.
$$

By the formulas for $W_\sigma$, multiply this by $(1+\lambda)2^L/(2^L-\lambda)$ for $+$ and by $1+\lambda$ for $-$. The latter uses $\lambda\ge1$. The entire tail and each of the potential, suffix and nonunit charges are individually rounded upward at scale $10^{30}$.

**Lemma 2.** For simple high shortcut lists, including at most one final unpaired odd charge, the total log costs have the following upper bounds. These use the sliding minimum with no exit information.

$$
\begin{array}{c|c|c|r}
 \sigma&Y&\lambda&10^{30}H_\sigma\\ \hline
 +1&2^{64}&3&50666894410409296445627628396\\
 -1&2^{28}&2&272357253662108596858729498103
\end{array}
$$

The checker recomputes the two rows by the integer counts and rational sums above. In particular $H_+<50667/10^6$ and $H_-<272358/10^6$.

## Sharp comparisons below the high floors

Put $K=2^{20}$. For the positive side, let $B$ be the basin of $1$. For $n\in B$ let $D,E,O$ denote the ordinary first-hit delay and the even and odd departure counts. Then $D=E+O$ and the first-hit factor is

$$
r(n)=\frac{2^E}{3^O n},\qquad nr(n)=\frac{2^D}{6^O}.
$$

The factor $r(n)$ is at least $1$. When the segment first starts or lands below $2^{64}$ at $w$, the record premise gives $D(w)\le2455$, so

$$
6^{O(w)}\le2^{2455}<6^{950}.
$$

Thus $O(w)\le949$. The part through the first shortcut entry below $K$ costs at most $949/(3K)$, even if it revisits arbitrarily large values. A simple segment with no departure from $1$ can only use a prefix of the first-hit path from $w$, including a possible last unpaired odd step. Odd departures before the low entry cost at most $1/(3K)$. If the low entry is reached, the remaining factor is bounded by the first-hit maximum for starts below $K$.

To compute that maximum, strip leading halvings and process the odd cores in increasing order, assigning the core $1$ counts zero. Iterate the odd-to-odd map $(3x+1)/2^{\nu_2(3x+1)}$ to the first smaller odd core, counting one odd departure and the exact number of halvings at each step. Add the smaller core's counts. Successful completion proves termination below $K$ by induction. Compare $2^E/(3^O n)$ by cross multiplication. The exact maximum is $2^{61}/(993\cdot3^{32})$, achieved at $993$, in agreement with Leen's census through $2^{22}$ [4]. Thus every positive segment outside the equality cases has

$$
\ln P\le H_++\frac{949}{3K}+\ln\frac{2^{61}}{993\cdot3^{32}}.
$$

This also bounds a wholly high segment. In that case Lemma 2 applies without invoking the record.

For the negative side, a local cover supplies, for each $K\le x<2^{28}$, a shortcut iterate at most $x/2$ within $330$ steps. At depth $d$ a residue $r$ modulo $2^d$ with image $u=T_-^d(r)$ and slope numerator $p=3^q$ has image $u+pt$ on $r+2^dt$. Use the extension $T_-(0)=0$. The lifts have next inputs $u$ and $u+p$. Discard empty classes and prune as soon as $2p\le2^d$. The nonpositive affine offset then ensures that the whole class has halved. At depth $20$ test every remaining class member directly from its exact image until the halving inequality holds. This partitions the interval into $249{,}769{,}440$ pruned and $17{,}617{,}440$ directly checked starts, totaling $2^{28}-K$. In the tree, the positive summands of the image calculation are bounded by $3^{20}2^{28}<2^{64}$. Direct odd steps are overflow-guarded and the replay fails if a witness exceeds $2048$ steps.

Starting below $2^{28}$, at most eight completed halving blocks bring the state below $K$. Each block begins below $2^{28}$ even when its interior makes a larger excursion. Stop counting at the first low entry or the segment end. A truncated block with a final unpaired odd edge has at most $t-1$ completed steps if its witness has length $t$, so that edge fits within its budget of $t$ departures. If the edge follows a completed block ending at or above $K$, it begins the next block. A departure at $K$ is a middle departure. The total pre-low cost after the first high exit is at most $8\cdot330/(3K-1)$.

For the negative low factor, strip leading halvings and check each odd core below $K$ in ordinary time. Floyd's algorithm locates the transient length $\mu$ and period $p$. The two pointers advance at speeds one and two until they meet in the cycle at a slow date divisible by $p$. Restart the slow pointer and advance each at unit speed to find the entry after $\mu$ steps. One lap finds $p$. The longest simple segment has $\mu+p-1$ departures, ending immediately before the first repeated state. The inverse product is nondecreasing, so compare the inverse factors $3^o a/(2^e b)$ at these lengths by integer cross multiplication. The maximum excluding core $1$ is $729/640$, at magnitude $9$ ending at $5$ after four odd steps and seven halvings. If the core is $1$, the remaining cost is zero once the isolated equality segment is excluded. The scan covers all $2^{19}$ odd cores. Therefore outside that equality segment,

$$
-\ln P\le H_-+\frac{8\cdot330}{3K-1}+\ln\frac{729}{640}.
$$

This bound also covers segments with no middle or low piece.

For the strict comparisons, put

$$
S(v)=2\sum_{j=0}^{23}\frac{((v-1)/(v+1))^{2j+1}}{2j+1}.
$$

For $v>1$ all omitted terms of the log series are positive. Integer cross multiplication verifies

$$
\begin{aligned}
 S\left(\frac{4}{3}\frac{993\cdot3^{32}}{2^{61}}\right)
      -H_+-\frac{949}{3K}
   &>\frac{11059386333}{10^{12}},\\
 S\left(\frac{320}{243}\right)-H_--\frac{8\cdot330}{3K-1}
   &>\frac{2063065125}{10^{12}}.
\end{aligned}
$$

The second logarithm compares $3/2$ with $729/640$. The strict comparisons and the explicit equality cases prove Theorem 1. The other endpoint of each interval follows termwise from the product identity.

## Consequences

### Clocks without the sign

Nikzad, Frinkle and Bagherzadeh derive count recovery for positive finite paths and first hits in Theorem 3.7 and Corollary 3.10 [1]. The signed band gives the following formulas on the union of the two signs. Fix the initial and final magnitudes $a,b$ of an ordinary simple segment. Under the sharp bounds, either $d=e+o$ or $e$ determines both other counts without knowing the sign. In fact

$$
o=\lfloor \log_6\left(\frac{3\,2^d b}{2a}\right)\rfloor,\qquad
 o=\lfloor \log_3\left(\frac{3\,2^e b}{2a}\right)\rfloor,
$$

 respectively, since the arguments are $6^o(3P/2)$ and $3^o(3P/2)$ with $1\le 3P/2\le2$. Given $o$, the possible $e$ are in the closed interval

$$
\left[\log_2\!\left(\frac{2\,3^o a}{3b}\right),
       \log_2\!\left(\frac{4\,3^o a}{3b}\right)\right].
$$

Its length is one. Two distinct realized counts must give the two extreme residues. The only common triple $(a,b,o)$ among the equality segments is $(1,2,1)$. Here $1\to4\to2$ has $(e,d)=(1,2)$ and $-1\to-2$ has $(e,d)=(0,1)$. Taking the floor of the upper endpoint recovers $e$ except on that negative edge, where the floor is $e+1$. If $o>0$, the sign is determined from the decoded counts by the sign of $2^e b-3^o a$. When $o=0$ both signs follow the same halving chain with identical counts.

### Contacts at different dates

Theorem 3.2 of Nikzad, Frinkle and Bagherzadeh gives the positive common-endpoint residue identity, and Theorem 3.3 and Corollary 3.4 give its count-difference restrictions [1]. Take two ordinary simple segments from the same starting magnitude $a$, one on each sign. Let $b_\pm$ be their final magnitudes, $k=o_+-o_-$, $m=e_+-e_-$, and $Q=P_+/P_-$. Then $1\le Q\le2$ and

$$
\frac{b_+}{b_-}=\frac{3^k}{2^m}Q
                 =\frac{6^k}{2^{d_+-d_-}}Q.
$$

At equal $e$ or equal $d$, the final magnitudes are ordered by the sign of $k$ when $k\ne0$. At $k=0$ the positive endpoint is larger as soon as either segment has an odd departure. Equal-date contacts therefore occur only on the shared leading halving chain. At a contact $b_+=b_-$ with independently chosen dates, if one segment is even-only then the other must stop on the same chain. Otherwise it would visit the common endpoint before its first odd departure and again at the contact. At every other contact both segments have odd departures, so $Q>1$. If $k\ne0$, unique factorization excludes $Q=2$ in $Q=2^m/3^k$. Hence

$$
0<m-k\log_2 3<1,\qquad
 m=\lceil k\log_2 3\rceil,\qquad d_+-d_-=\lceil k\log_2 6\rceil.
$$

Both date gaps have the sign of $k$. If $k=0$, then $Q=2$ and $m=d_+-d_-=1$, realized only by the exceptional pair from magnitude $1$ to $2$ above. All counts here refer to the ordinary segments, including segments ending with an unpaired odd edge.

### First hits and clock formulas

On $B$, the strict positive bound gives $r(n)<4/3$. This is also Theorem 2.23 of Nikzad, Frinkle and Bagherzadeh [1] and implies Luo's Conjecture 1.1 on its natural domain. The global first-hit maximum at $993$ asked for by Roosendaal remains open [2, 3]. By $0\le E\ln2-O\ln3-\ln n<\ln2$,

$$
\begin{aligned}
 O&=\lfloor \frac{D\ln 2-\ln n}{\ln 6}\rfloor,&
 E&=\lceil \frac{D\ln 3+\ln n}{\ln 6}\rceil,\\
 D&=\lceil \frac{O\ln 6+\ln n}{\ln 2}\rceil,&
 E&=\lceil \frac{O\ln 3+\ln n}{\ln 2}\rceil,\\
 D&=\lfloor \frac{E\ln 6-\ln n}{\ln 3}\rfloor,&
 O&=\lfloor \frac{E\ln 2-\ln n}{\ln 3}\rfloor .
\end{aligned}
$$

Indeed, substituting $D=E+O$ gives a signed error from the target integer equal to $\pm\ln r(n)/\ln b$, with $b=2,3,6$, always of magnitude less than one. The ceiling arguments approach the target from below, with equality at powers of two. These are Luo's Theorem 4.1 formulas. For a general segment replace $\ln n$ by $\ln(a/b)$ and the uppercase counts by the corresponding segment counts. The same proof applies with $\ln P$, and the negative interval $-\ln2<\ln P\le0$ reverses floors and ceilings. This gives Luo's Theorems 5.11 and 5.12 at $q=3$ [2].

### Equal finite heights and adjacent order

Nikzad, Frinkle and Bagherzadeh prove equal-height separation and adjacent count agreement at a common positive endpoint in Theorem 3.5 and Corollary 3.6. Theorem 3.11 and Corollary 3.12 specialize these results to first hits of $1$ [1]. For $x<y$ in $B$ with $D(x)=D(y)$, set $d=O(x)-O(y)$. The identity $nr(n)=2^D/6^O$ gives $6^d=y r(y)/(x r(x))$. Under the record premise

$$
d\ge0,\qquad (3/4)6^d<y/x<(4/3)6^d.
$$

Thus different counts require $y/x>9/2$. In particular adjacent starts with the same finite height have the same halving count. Gao asks this on p. 266 in Leen's account [6, 7]. The primary page was unavailable for quotation. The implication already follows from Leen's earlier bound $2^{1.258374187571}<3$, since adjacent starts have ratio at most $2$. Said Duran proved Gao's separate density-one coalescence conjecture and Leen obtained precise deficiency asymptotics [7, 8].

For adjacent starts $x,x+1$ with $x\ge2$, write $\Delta$ for the differences in increasing start order. Then $2^{\Delta E}/3^{\Delta O}$ lies strictly between $(3/4)(x+1)/x$ and $(4/3)(x+1)/x$, within $(1/2,2)$. If $\Delta O=0$ this forces $\Delta E=0$. A positive $\Delta O$ gives $2^{\Delta E}>3/2$ and a negative one gives $2^{\Delta E}<2/3$. Thus $\Delta E,\Delta O$ and $\Delta D$ have the same sign. At $(1,2)$ the odd counts are zero and the other counts increase by one. For $x\ge3$, Theorem 3.14 of Nikzad, Frinkle and Bagherzadeh gives the stronger nearest-integer law for $\Delta E$ in terms of $\Delta O$ [1].

### High windows and cycles

Any positive orbit avoiding $1$ stays at or above $2^{64}$ from its very first state under the record premise. Bařina's convergence verification supplies the same conclusion with the higher floor $2^{71}$, independently [9, Section 6, Table 10]. For every nonrepeating shortcut window $x_i,\ldots,x_j$ above $2^{64}$, put $h=j-i$ and let $q$ count odd departures. Lemma 2 gives $1\le x_j2^h/(x_i3^q)\le e^{H_+}$. On an infinite nonrepeating orbit the ratios for fixed $i$ converge by monotonicity and this bound.

For a least-period lap of a nontrivial positive shortcut cycle, remove the repeated endpoint from the state list and charge its closing edge in the final odd allowance, or charge zero if that edge is even. Thus $0<h\ln2-q\ln3\le H_+<0.050667$, by telescoping the odd factors over the lap. In particular $h=\lceil q\log_2 3\rceil$ is the nearest integer and $\{q\log_2 3\}\ge1-H_+/\ln2$. Rozier and Terracol give the lap product and its harmonic-mean bound [10, Theorem 4.2]. Universal convergence is open.

## Reproducibility

Run `python3 -B replay.py` inside the extracted [supplement](supplement.zip), using Python 3.8+ and a C++20 compiler with Boost.Multiprecision headers. A machine with `taskset` can pin the command to one allowed CPU. The standalone replay checks the two high bounds, the two low maxima, the restricted negative halving cover and the rational margins. With `--archive`, it checks the original Leen deposit against its SHA-256 manifest and compares the excerpted fields with the archived records. The record replay checks the witness and its documented status. Independently establishing strict maximality would require verification across the record range.

## Appendix A. Independent check using the 2261-step record

This replay gives a separate sliding-minimum proof of the positive bound of Nikzad, Frinkle and Bagherzadeh [1, Theorem 2.22] with a smaller published delay record and a locally replayed low check. It also verifies the negative bound. The `--independent` replay uses the same sliding-minimum inequality and infinite-tail argument with $L=512$ and $\lambda=3$ for both signs. Its one-step bound per unit of $D$ is $1/(x-3)$ on each sign, since $x+3-d_3\ge x-3$. It uses a different integer grid and integrates the threshold variable exactly for its rounded counting process.

At a positive increment let $D$ be the minimum over the full lookahead. Integrate $\mathbf 1_{\{D>t\}}$ for $0\le t\le d_3=4/3$. In the virtual dynamics scaled by $16$, the first odd child from $3-t$ decreases linearly from $80$ to $48$. Each first-child ceiling $49,\ldots,80$ covers threshold length $d_3/32$. For subsequent steps test the rational child against $48$, then round each survivor upward to the grid keeping seven leading bits. More precisely, if $u$ is the child's integer ceiling, round it up to a multiple of $2^{\max(0,\operatorname{bitlength}(u)-7)}$. Monotonicity preserves all true survivors. A backward integer recurrence counts continuations from each grid point by adding the two child counts, with zero at failure and one at exhaustion for each surviving state. The successive all-odd rounded iterates from $80$ bound the domain at each date. For each first-child bin, use eight height panels per octave. At each right boundary minimize the product of the word count and unit multiplicity over the depths $m-4,\ldots,m$ in octave $[2^m,2^{m+1})$. Sum the bounds over first-child bins and use the same summation by parts with their equal weights $d_3/32$. Panel contributions round up at scale $10^{15}$. The potential, terminal allowance, nonunit charge and infinite tail use rational bounds.

The positive high bound above $2^{58}$ is $61237187/10^9$. The start $372{,}975{,}273{,}994{,}315{,}489$ has strict record delay $2261$ [4], yielding at most $874$ odd steps below the floor by $6^{875}>2^{2260}$. The low first-hit maximum is recomputed by first descent below $2^{20}$. Using the first three terms of the log series in the sharp comparison gives margin at least $512935/10^9$. The option `--low-bits 22` recomputes the same maximum below $2^{22}$ and yields margin at least $721313/10^9$.

On the negative side the check gives $H\le231407948/10^9$ above $2^{31}$. The same halving tree algorithm, run up to that floor, gives at most $410$ steps per block and requires at most eleven blocks. Independent enumeration with a visited-state set gives the same low inverse maximum $729/640$. With the three-term log lower bound the margin is at least $42417654/10^9$. The supplement supplies the record excerpt, both replays of the finite calculations and exact small controls on the grid counts and the terminal window.

## Appendix B. An independent local positive factor-two bound

The optional `--local-positive` replay uses only local computations to prove the following bound for all positive simple ordinary segments.

$$
P\le1.987041505875978<2.
$$

This gives the positive General Weak Residue Conjecture at $q=3$ using local checks alone. Nikzad, Frinkle and Bagherzadeh already prove the positive conjecture in the discussion following Theorem 2.22, using their published finite inputs [1].

For the high prefix above $Y=2^{32}$, let $A(X)$ and $A_o(X)$ count the unit states and odd unit states at most $X$. At depth $k$ discard at most the last $k$ positions. Retained starts with at most $g$ odd steps map injectively to positions at most

$$
F(X,g)=\lfloor \frac{3Y\,3^g X}{(3Y-g)2^k}\rfloor .
$$

For starts at most $X$, each prefix of length $t\ge1$ and grade $j$ stays above the inclusive floor only if $3X3^j>(3Y-t)2^t$. Indeed its endpoint is at most $3^j X(1+1/(3Y))^j/2^t$, strictly below $3^j X\,3Y/(2^t(3Y-t))$ by the geometric series. Using $j$ instead of $t$ in the series gives $F$, including equality at $j=0$.

To count the higher grades use the necessary prefix tests, with the first bit fixed odd for $A_o$. The minimum passing grade increases by zero or one at each step because the right side grows by at most a factor two and is nondecreasing at the tested depths. At a rise, first failures consist of a surviving prefix at the old minimum followed by an even bit. Count them by subtracting the binomial extensions of the earlier disjoint first-failure classes, and subtract their extensions from the high-grade tail. At the preceding mesh point $V$ the checker can split $[Y,X]$ into $[Y,V]$ and $(V,X]$. Use the largest grade in the first part whose images fit below the same earlier mesh point as $F(X,g)$, and count the higher grades separately in each part. Their unit multiplicities are as in the finite panel proof above. The low grades share one earlier occupation bound and one $k$-position charge. Taking the smaller of the split and unsplit recurrences proves the bounds by mesh induction.

The replay uses $12$ equal subdivisions per octave with boundaries rounded upward, through $2^{520}$, and tries $k=\max(1,\operatorname{bitlength}(X-Y+1)-u)$ for $u=3,4,5,6$. For the tail use the same occupation proof as above with $b=49/25$, grade split $\lfloor 11j/18\rfloor$ and tilt $3/2$. Integrating $A_o(x)/(3x^2)$ with right endpoint bounds and allowing one initial nonunit odd departure gives the high log bound $459203646316524368257603396524/10^{30}$. The positive halving cover on $[K,2^{32})$ uses depth $24$, prunes only when $2p\le2^d$ and $2T_+^d(x)\le x$ at the smallest member of the class, and otherwise tests individually. The affine difference $2T_+^d(x)-x$ is then nonincreasing along the pruned class. The cover gives at most $469$ steps per block and a middle bound $12\cdot469/(3K)$. The low check sums eight terms of the positive log series at each odd core with outward rounding at scale $2^{56}$. For $z=1/(6x+1)$, the omitted terms sum to at most $4z^{17}/17$. The maximum rounded suffix cost is $16260092448230192/2^{56}$. Round the sum of the three costs upward to fifteen decimals. For $0\le v<1$, use $\exp(v)\le\sum_{j=0}^{10}v^j/j!+
 v^{11}/(11!(1-v/12))$. The resulting comparison and the explicitly classified departures from $1$ give the stated local bound.

## References

1. Behzad Nikzad, Karl Frinkle, and Fatemeh Bagherzadeh. *On Bounds for Reciprocal Sums and Residues in Collatz Orbits, and Their Consequences*. Preprint, revised 26 October 2026. [hexagon:2611.00033v1](https://hexagonmath.org/pdf/2611.00033v1)
2. Youchun Luo. *Iteration Steps of 3x + 1 Problem*. The Fibonacci Quarterly, published online 6 August 2026, pp. 1–14. Conjecture and equation numbering follows arXiv v3. [Journal](https://doi.org/10.1080/00150517.2026.2638789) · [arXiv v3](https://arxiv.org/abs/2506.23070v3)
3. E. Roosendaal. *On the 3x+1 problem*. [Delay records](https://www.ericr.nl/wondrous/delrecs.html) · [Progress log](https://www.ericr.nl/wondrous/progress.html) · [Residue records](https://www.ericr.nl/wondrous/residues.html)
4. David Leen. *Supplement to Gaussian but not locally Gaussian: a computer-assisted bound for the terminal residue*. Code and data (2026). [DOI](https://doi.org/10.5281/zenodo.23252399)
5. David Leen. *Gaussian but not locally Gaussian: the teeth of the Collatz stopping-time histogram*. Preprint (2026). [DOI](https://doi.org/10.5281/zenodo.23252397)
6. Guo-Gang Gao. *On consecutive numbers of the same height in the Collatz problem*. Discrete Mathematics **112** (1993), 261–267. [DOI](https://doi.org/10.1016/0012-365X(93)90240-T)
7. David Leen. *Exact rates in Collatz synchronization*. Preprint (2026). [DOI](https://doi.org/10.5281/zenodo.23268751)
8. Omar Javier Said Duran. *Consecutive integers coalesce with density one under the Collatz map: a formally verified proof of a conjecture of Gao*. Preprint (2026). [DOI](https://doi.org/10.5281/zenodo.23003524)
9. David Bařina. *Improved verification limit for the convergence of the Collatz conjecture*. Journal of Supercomputing **81** (2025), article 810. [DOI](https://doi.org/10.1007/s11227-025-07337-0) · [Table 10](https://link.springer.com/article/10.1007/s11227-025-07337-0/tables/10)
10. Olivier Rozier and Claude Terracol. *Paradoxical behavior in Collatz sequences*. Discrete Mathematics **349**(10) (2026), article 115167. [DOI](https://doi.org/10.1016/j.disc.2026.115167)

# First-landing bounds and canonical inverse laws for Collatz

## 1. Result, prior work, and dependencies

Write
$$
C(n)=\begin{cases}n/2,&2\mid n,\\3n+1,&2\nmid n,\end{cases}
\qquad U(n)=\frac{3n+1}{2^{v_2(3n+1)}}\quad(n\text{ odd}),
$$
and let $\mathcal P(a)=\{n\ge1:C^j(n)=a\text{ for some }j\ge0\}$. Lower natural density is denoted by $\underline d$.

**Theorem 1.** Either Inputs A and B, or Inputs C and D below, imply that there is an absolute $c>0$ such that
$$
\underline d(\mathcal P(a))\ge\frac ca\qquad(a\ge1,\ 3\nmid a).
\tag{1}
$$
Under Inputs A and B, a finite cutoff sufficient for the counting bound is specified in Theorem 3. Combining the reciprocal density with Leen's relative passage estimate [1] gives the stronger uniform onset $Y\ge\exp(C_\varepsilon a^\varepsilon)$ for every fixed $\varepsilon>0$ (Corollary 4). Under Input C, each predecessor set has natural density and (1) holds for that density. Targets divisible by three have density zero.

Wirsching's preliminary manuscript [2] formulates uniform positive predecessor density in precisely the reciprocal-target shape, and leaves three conjectural gaps in its proposed route. We use none of those conjectures. Mazur [3,4] supplies positive fixed-target density through a weighted inverse construction. Mghirbi [5] and Shaik [6] give the two-sibling nonperiodic-root selection and related all-target results; Shaik also uses residue moments to remove reference weights. A recent separate argument [7] uses the known global $L^p$ regularity, $p<2$, to obtain target exponent $2+\varepsilon$, with a uniform linear finite onset. A second, shorter proof uses El Jaouhari's uniform atom floor and Leen's density existence. The quantitative relative passage theorem further gives the onset in Corollary 4. Subsequently, Fourier Wren [8] proved a joint atom floor at each fixed central valuation sum, adapting El Jaouhari's selected-block construction using averaged joint mixing. That stronger input yields a reciprocal counting bound for every $Y\ge a$, and therefore supersedes our finite natural-count onset. Our public audits check the final partial generation and the two cases of Wren's tail-mixture argument; a local-central-limit block simplifies the counting step. Credit for the joint-floor construction and the stronger counting claim belongs to Wren. The coalescence proof here supplies an alternative route to the reciprocal exponent without either atom input.

Leen [9, proof of the arithmetic-progression theorem] already deduces progression independence of terminal labels from Duran's coalescence theorem. One deduction here inserts that property, or its finite adjacent-variation version, into the existing marked-path counting interface. We do not claim a new coalescence theorem, mixing estimate, or favorable-root construction.

**Input A: coalescent residue classes [10, Corollary C].** For the shortcut map $T(n)=n/2$ on even integers and $(3n+1)/2$ on odd integers, let $c_t$ be the proportion of residues $0\le r<2^t$ for which $T^t(r)=T^t(r+1)$ and both paths have the same number of odd terms before time $t$. Then $c_t\to1$. Equal odd counts make the affine slopes equal, so the coalescence holds throughout each such binary class. We may omit one carry class and set
$$
\eta_t=1-c_t+2^{-t}\longrightarrow0.
$$

**Input B: marked inverse paths [3, Proposition 3.1 and Appendix A].** There are absolute integers $B_0,q_0$, a unit $y\bmod3^{q_0}$, and nonnegative functions $r_k$ on $\mathbb Z/3^k\mathbb Z$ with mean $2/3$, such that
$$
\delta_m:=\sup_{k\ge m}\|r_k-r_m\|_{L^1}\longrightarrow0.
\tag{2}
$$
The coarse function is lifted to the fine quotient. For every odd $R\ge B_0$ with $R\equiv y\pmod{3^{q_0}}$, every fixed $m\ge1$, and all $X>H(R,m)$, there are $k\ge m$, $J\ge0$, a finite family of exact positive odd valuation paths ending at $R$, and selected weights satisfying
$$
\begin{gathered}
3^k\le X,\qquad X\le x_w<32X,\qquad
0\le v_w\le\omega_w,\\
\omega_w=3^{|w|}2^{-D(w)},\qquad x_w\omega_w\le R,\\
\frac23\le\sum_w v_w g_{k,J}(x_w),\qquad
g_{k,J}=\sum_{j=0}^J4^{-j}r_k\circ\Psi_j,\quad
\Psi_j(x)=4^jx+\frac{4^j-1}{3}.
\end{gathered}
\tag{3}
$$
Its stated bound $\delta_m\le C_*m^{-2}$ suffices. The functions are $r_k=(2/3)\rho_k$ in the probability-density normalization of [7]. Exact paths, their restrictions, and the selected weights remain part of this imported input.

**Input C: density of invariant sets [9,11].** A set invariant under $C$ above $R_0$, every member of which eventually enters $[1,R_0]$, has natural density.

**Input D: uniform Syracuse atoms [12, Theorem A].** There is an absolute $0<\alpha\le1$ such that $\rho_k(r)=3^k\mu_k(r)\ge\alpha$ for all $k\ge1$ and every unit residue modulo $3^k$. The source uses unit-Haar density $D_k=(2/3)\rho_k$. This is an all-residue bound, not an almost-everywhere limiting assertion. Its written construction and density results were read; its formal development was not independently rebuilt.

Valbuena [13, Theorems 8, 14, and 16] already proves the critical harmonic trace, its equality with integer Cesaro and Abel limits, and natural weighted basin means. His Proposition 9 proves decay uniformly among large ancestors of a fixed root; in particular it implies that the canonical inverse boundary has no atoms. These are prior results, not contributions claimed here. We combine his canonical profile with the uniform atom floor to obtain a short uniform trace comparison. A bounded selection identity and arithmetic access to prescribed words then prove that every finite valuation word has a positive upper occurrence frequency under the canonical inverse law, with a bound independent of the root. The profile oscillates between bounded levels and arbitrarily large values along almost every inverse path. A related subtree-survival identity is also recorded. This is an inverse-path assertion and gives no exclusion of exceptional forward orbits. The ordinary natural-density entrance law has the same null events at nonperiodic roots. A later relative landing estimate also strengthens the upper bound for basins with no small ancestor. Coding each parent by its least ancestor then proves finite transition entropy, with a subpolynomial bound in the root. The code does not control the numerical size of its parent; this distinction preserves the unresolved physical tail question.

The main new first-passage conclusion is a lower bound $cX/M$ for every odd unit landing atom below $M$, uniformly for $X\ge CM$, including periodic targets (Theorem 14). It uses retained real bounds in Fourier Wren's fixed-total selected construction, based on El Jaouhari's blocks and the averaged joint mixing estimate [12,8,14,15]. Theorem 15 constructs infinitely many actual thresholds with an extra $\log M$ factor in a landing atom, disproving a matching flat upper law. Corollary 16 bounds every finite landing law by an absolute multiple of its true nonuniform limiting law. The reverse inequality remains open. These results join the inverse word-frequency and entropy conclusions below; all imported analytic dependencies remain explicit.

The written source interfaces were read and checked against these statements. Duran reports Lean verification of the supporting coalescence theorems; his Corollary C is a written deduction from them. Mazur's Proposition 3.1 is a written combination of cited analytic statements and is not advertised as a separately audited formal declaration. We have not independently rebuilt either development. Theorems below explicitly retain these dependencies. Section 8 uses Valbuena's already established canonical trace and boundary theorem. The finite onset additionally uses Leen's relative passage estimate. We have not independently rebuilt these formal developments.

## 2. A short proof from uniform atoms

This route uses Inputs C and D, without Inputs A or B. First fix a nonperiodic positive odd unit target $a$. A full coding congruence at $a$ reconstructs a unique positive odd inverse path at every depth: recursively, $(2^ey-1)/3$ is positive and odd whenever it is an integer and $y$ is positive odd. Hence
$$
\rho_k(a)=\sum_{U^k(x)=a}\omega_k(x),\qquad
\omega_k(x)=3^k2^{-D_k(x)}\le a/x.
$$
Nonperiodicity makes the hitting depth unique. With $\tau_a(x)$ denoting that depth and $w_a(x)=x\omega_{\tau_a(x)}(x)/a\le1$,
$$
F_K(a):=\sum_{k=0}^K\rho_k(a)
=a\sum_{\substack{x\text{ odd},\ x\in\mathcal P(a)\\\tau_a(x)\le K}}\frac{w_a(x)}x
\ge\alpha K.
$$

The sources in this sum are not bounded a priori. If $x>e^{8K}$, then $\omega_k(x)x\le a$ implies $D_k(x)>(8K-\log a)/\log2$. For the original geometric exponent law, $E(4/3)^e=2$. Dropping congruence and endpoint restrictions in the nonnegative sum gives the far-source bound
$$
\sum_{k=0}^K3^kP\left(D_k>\frac{8K-\log a}{\log2}\right)
\le\frac65a^s e^{-(8s-\log6)K}=o(1),\qquad
s=\frac{\log(4/3)}{\log2}.
$$
Therefore, setting $K=\lfloor\log X/8\rfloor$ proves
$$
\liminf_{X\to\infty}\frac2{\log X}
\sum_{\substack{x\le X,\ x\text{ odd}\\x\in\mathcal P(a)}}\frac1x
\ge\frac{\alpha}{4a}.
$$
This relative-odd lower logarithmic-density statement needs only Input D. Input C gives natural density $d_a$; eventual doubling invariance gives the same relative odd density. Partial summation identifies the displayed logarithmic density with $d_a$, so $d_a\ge\alpha/(4a)$.

There is also a uniform finite version on the relative source scale. Fourier Wren's public audit [7] prompted this refinement. Put $r=X/a\ge1$, $K=\lceil\log r/8\rceil$, and $\gamma=s-\log6/8>0$. The source tail beyond $X$ is at most
$$
r^{-s}\sum_{k=0}^K6^k\le\frac{36}{5}r^{-\gamma}.
$$
Therefore, using only Input D,
$$
\sum_{\substack{x\le X,\ x\text{ odd}\\x\in\mathcal P(a)}}\frac1x
\ge\frac1a\left[\frac\alpha8\log(X/a)-\frac{36}{5}(X/a)^{-\gamma}\right].
$$
In particular, it is at least $\alpha\log(X/a)/(16a)$ for $X\ge C_\alpha a$, with $C_\alpha$ independent of $a$. For every $\varepsilon>0$, this implies a lower bound $\alpha\varepsilon\log X/[16(1+\varepsilon)a]$ when $X\ge C_\alpha a^{1+\varepsilon}$. These are accumulated harmonic sums; they imply no bound in every dyadic interval.

For any positive $a$ prime to three, choose $e_0\in\{1,2\}$ with $2^{e_0}a\equiv1\pmod3$. The three positive odd predecessors
$$
R_j=(2^{e_0+2j}a-1)/3,\qquad j=0,1,2,
$$
cover all residues modulo three, so two are units. They have the same next odd value, the odd part of $a$, and at most one can be periodic. This is the two-sibling mechanism of [5,6]. Choose a nonperiodic unit $R\le64a/3$. Since $\mathcal P(R)\subseteq\mathcal P(a)$,
$$
d(\mathcal P(a))\ge\frac{3\alpha}{256a}.
$$
This proves the second route to Theorem 1. It uses no clock law or prior reciprocal bound. The same root transfer in the finite harmonic bound gives absolute $c_0,C>0$ such that, for every positive unit target, including even and periodic targets,
$$
\sum_{\substack{x\le X,\ x\text{ odd}\\x\in\mathcal P(a)}}\frac1x
\ge\frac{c_0}{a}\log(X/a)\qquad(X\ge Ca).
$$
Indeed, with $B=64/3$, choose $C\ge\max(BC_\alpha,B^2)$; then $R\le Ba$ and $\log(X/R)\ge\tfrac12\log(X/a)$. One can take $c_0=\alpha/(32B)$. With the Cesaro formula proved later, $\beta_R\le d(\mathcal P(R))$ improves the asymptotic density constant to $3\alpha/[32\log(4/3)]$. The atom argument and density existence alone supply no quantitative natural-density onset. Section 6 obtains one from the additional relative passage estimate.

## 3. Coalescence controls adjacent membership changes

For a set $A$, put
$$
V_A(Y)=\#\{1\le n<Y:1_A(n+1)\ne1_A(n)\}.
$$

**Lemma 2.** If $A$ is invariant under $C$ above an integer $R_0\ge1$, then
$$
V_A(Y)\le\eta_tY+4^t(R_0+1)+2^t
\tag{4}
$$
for every integer $t\ge1$ and real $Y\ge1$. In particular, $V_A(Y)=o(Y)$.

*Proof.* On a retained coalescent binary class, the ordinary paths from $n,n+1$ reach the common value within $2t$ steps. Each ordinary step decreases its argument by at most a factor two. If $n>4^t(R_0+1)$, both paths remain above $R_0$ before merger, so their membership labels agree. Count the remaining periodic classes, with at most $2^t$ boundary error, and discard the initial interval. This proves (4). First let $Y\to\infty$, then $t\to\infty$. $\square$

For $A=\mathcal P(R)$, invariance above $R$ is exact. It does not require $R$ to converge to one.

## 4. A finite weight-removal inequality

**Theorem 3.** Let $R$ be eligible for Input B and nonperiodic under $U$. Choose $m,t$, put $q=3^m$, and assume
$$
\delta_m\le\frac1{100R},\qquad
\eta_t\le\frac1{1000Rq}.
\tag{5}
$$
For every real $X$ satisfying
$$
X>H(R,m),\qquad
X\ge100Rq\,[4^t(R+1)+2^t+3],
\tag{6}
$$
we have
$$
\#(\mathcal P(R)\cap[X,32X))\ge\frac{9X}{8R}.
\tag{7}
$$
Consequently $\underline d(\mathcal P(R))\ge9/(256R)$.

*Proof.* Every $\Psi_j$ permutes each ternary quotient, so
$$
\|g_{k,J}-g_{m,J}\|_1\le\frac43\delta_m.
\tag{8}
$$
The bounded periodic function
$$
g_{m,\infty}=\sum_{j\ge0}4^{-j}r_m\circ\Psi_j
$$
has mean $8/9$ and dominates every $g_{m,J}$.

For a nonnegative function $F$ of fine modulus $Q=3^k\le X$, odd integers in each class have spacing $2Q$. Integral comparison yields
$$
\sum_{X\le x<32X,\ x\text{ odd}}\frac{F(x)}x
\le\left(\frac QX+\frac{\log32}{2}\right)\langle F\rangle_Q
\le(1+\tfrac12\log32)\langle F\rangle_Q.
\tag{9}
$$
This estimate is at the growing fine modulus and involves no equidistribution assertion about the predecessor set.

Nonperiodicity of $R$ makes the selected sources in (3) distinct: two visits from one source would give a return to $R$. Their weights satisfy $v_w\le R/x_w$. With $A=\mathcal P(R)$, (3), (8), and (9) therefore give
$$
\frac23\le
R\sum_{\substack{X\le n<32X\\n\text{ odd},\ n\in A}}\frac{g_{m,\infty}(n)}n
+R(1+\tfrac12\log32)\frac43\delta_m.
\tag{10}
$$
The last term is less than $1/25$, since $\log32<4$.

Put $F_m(n)=1_{n\text{ odd}}g_{m,\infty}(n)$. This nonnegative function has period $2q$, mean $4/9$, and total period mass $8q/9$. Every centered partial sum, starting at any integer, is bounded in absolute value by $8q/9$. Discrete summation by parts against $1_A(n)/n$, restricted to $[X,32X)$, gives
$$
\left|\sum_{\substack{X\le n<32X\\n\in A}}
\frac{F_m(n)-4/9}{n}\right|
\le\frac{8q}{9X}\bigl(3+V_A(32X)\bigr).
\tag{11}
$$
The variation of this restricted reciprocal weight is at most $(3+V_A(32X))/X$: two endpoint jumps, the reciprocal variation, and the membership changes.

Apply Lemma 2 and (5)--(6). After multiplying (11) by $R$, its right side is at most
$$
\frac{256}{9000}+\frac8{900}=\frac{14}{375}<\frac1{25}.
$$
Thus (10) implies
$$
\frac{4R}{9}\sum_{\substack{X\le n<32X\\n\in A}}\frac1n
\ge\frac23-\frac2{25}>\frac12.
$$
Since $1/n\le1/X$, this proves (7). Set $Y=32X$ and include the annulus in $[1,Y)$. The choices $m,t$ are fixed at this root and exist by the two inputs, so the conclusion holds for every sufficiently large $Y$. $\square$

## 5. Arbitrary targets and the asymptotic constant

For completeness, use the established two-sibling selection [5,6]. Given $3\nmid a$, choose $e\in\{1,2\}$ with $2^ea\equiv1\pmod3$, and put
$$
R_j=\frac{2^ea4^j-1}{3}.
$$
These are odd positive ordinary predecessors of $a$. Since
$v_3(R_{j+h}-R_j)=v_3(h)$, the index $j$ modulo $Q_0=3^{q_0}$ permutes their residues modulo $Q_0$. Fix $J_0\ge1$ making every $R_j$, $j\ge J_0$, at least $B_0$, uniformly in $a$. Choose $j\in[J_0,J_0+Q_0-1]$ in the favorable residue. Both $R_j,R_{j+Q_0}$ are eligible and at most
$$
C_{\rm seed}a,\qquad C_{\rm seed}=\frac43\,4^{J_0+2Q_0}.
$$
They have the same next odd value; at most one is periodic, because a cycle has only one predecessor on that cycle. Choose the nonperiodic root. Theorem 3 and $\mathcal P(R)\subseteq\mathcal P(a)$ prove Theorem 1 with $c=9/(256C_{\rm seed})$. If $3\mid a$, then $\mathcal P(a)=\{2^ja:j\ge0\}$, so its density is zero.

Input C gives natural density of $\mathcal P(R)$. Lemma 2 then implies that every fixed residue class modulo $Q$ contains density $d(\mathcal P(R))/Q$: adjacent class counts differ by $o(Y)$, and their sum is the full count. Consequently, for every fixed periodic $f$ of odd modulus,
$$
\lim_{X\to\infty}\sum_{\substack{X\le n<32X\\n\text{ odd},\ n\in\mathcal P(R)}}\frac{f(n)}n
=\frac{d(\mathcal P(R))}{2}\log32\,\langle f\rangle.
\tag{12}
$$
Apply this to $g_{m,\infty}$ in (10), first taking $X\to\infty$ at fixed $R,m$, then $m\to\infty$. We obtain
$$
d(\mathcal P(R))\ge\frac3{2\log32\,R},\qquad
d(\mathcal P(a))\ge\frac3{2\log32\,C_{\rm seed}a}.
\tag{13}
$$
The order of limits is essential. No assertion is made that progression independence holds at the growing fine modulus.

## 6. Relative passage gives a uniform finite onset

This section additionally uses Leen's relative passage estimate [1, Theorem 5.3] at frequency zero and its already published telescoping form [9, Corollary ``Relative landing law'']. The estimate is uniform in bounded nonnegative tests of the landing point. It gives more than merely the existence assertion in Input C. No new passage or mixing theorem is claimed.

**Corollary 4.** There is an absolute $c_0>0$ such that, for every $\varepsilon>0$, there is $C_\varepsilon>0$ with
$$
\#(\mathcal P(a)\cap[1,Y))\ge c_0Y/a
\quad\text{for all }3\nmid a,\quad
Y\ge\exp(C_\varepsilon a^\varepsilon).
\tag{14}
$$
The coefficient $c_0$ is independent of $\varepsilon$.

*Proof.* Write $W_y$ for the uniform distribution on odd integers in $[y,2y)$ and $\Lambda_{y,x}(g)$ for the expectation of a test $g$ of the first odd landing at or below $x$, with zero assigned if passage fails. Fix $A>0$ and $0<c_1<5/143$, and put $\alpha_0=1001/1000$. The cited relative landing corollary gives a nonnegative functional $\mathcal H_x$ such that
$$
\Lambda_{Y,x}(g)=\mathcal H_x(g)(1+O((\log x)^{-c_1}))
+O_A((\log x)^{-A})\qquad(Y\ge x^{\alpha_0}),
\quad 0\le g\le1.
\tag{15}
$$
Its constants and onset do not depend on the test. We use $\mathcal H_x$ to distinguish this published landing functional from the integer profile introduced later.

Let $E$ be invariant above $R_0$, with every member entering $[1,R_0]$, and set $p_E(y)=P(W_y\in E)$. For $x\ge R_0$, the landing rule in [9, Lemma ``Landing rule''] supplies a test $g_x$ with $p_E(Y)=\Lambda_{Y,x}(g_x)$ for $Y>x$. Explicitly, if the odd landing is $v>R_0$, use $1_E(v)$; if $v\le R_0$, use $1_E(2^jv)$ with $j=\lfloor\log_2(R_0/v)\rfloor$. This is the first ordinary value at or below $R_0$, so it handles even targets as well.

Set $y=x^{\alpha_0}$ and apply (15) first at $y$, then let its source $Y\to\infty$. Input C identifies the latter limit as $\delta_E=d(E)$. Both quantities differ from the same nonnegative $\mathcal H_x(g_x)$ by at most $\eta\mathcal H_x(g_x)+r$, where $\eta=O((\log x)^{-c_1})$ and $r=O_A((\log x)^{-A})$. Once $\eta\le1/2$, eliminate the functional using $\mathcal H_x(g_x)\le(\delta_E+r)/(1-\eta)$. Thus, for constants independent of $E,R_0$,
$$
|p_E(y)-\delta_E|
\le B_A\delta_E(\log y)^{-c_1}+D_A(\log y)^{-A},
\qquad y\ge\max(Y_A,R_0^{\alpha_0}).
\tag{16}
$$
The small absolute remainder remains explicit. The telescoping behind (15) sums multiplicative errors and absolute remainders along geometrically increasing logarithmic source scales; it introduces no target-dependent constant.

Take $E=\mathcal P(a)$ and $R_0=a$, so $\delta_E\ge c/a$ by Theorem 1. Choose $L=\log y$ with $B_AL^{-c_1}\le1/4$, $D_AL^{-A}\le c/(4a)$, $L\ge\alpha_0\log a$, and $y\ge\max(Y_A,6)$. Then
$$
p_E(y)\ge\frac{\delta_E}{2}\ge\frac{c}{2a},
\qquad
\#(\mathcal P(a)\cap[1,2y))\ge\frac{cy}{6a},
\tag{17}
$$
because $[y,2y)$ contains at least $y/3$ odd integers. Given $\varepsilon>0$, choose $A\ge1/\varepsilon$. Increasing $C_\varepsilon$ makes these conditions hold for every $y\ge\exp(C_\varepsilon a^\varepsilon)$. Set $Y=2y$ and absorb the factor two into $C_\varepsilon$ to obtain (14), for instance with $c_0=c/12$. $\square$

The source cutoff depends on the target because the absolute remainder must be smaller than $c/a$. The result is neither a linear nor a polynomial onset in $a$, and no useful numerical constants are asserted. It concerns density convergence, not a quantitative slow-clock estimate at the bottom of a trajectory.

## 7. Uniform bounds at positive integer targets

Let $\rho_k=(3/2)r_k$ be the mean-one ternary density, with $\rho_0=1$, and write $d_a=\underline d(\mathcal P(a))$.

**Corollary 5.** Set $K_*=53/(21c)$, with $c$ from Theorem 1. At every nonperiodic positive odd unit $a$,
$$
\sup_{k\ge0}\rho_k(a)\le K_*a d_a.
\tag{18}
$$
If $a$ is periodic with cycle multiplier $\lambda_a$, the bound is instead
$$
\sup_{k\ge0}\rho_k(a)\le\frac{2K_*a d_a}{1-\lambda_a}
\le2K_*a(3a+1)d_a.
\tag{19}
$$
For $3\mid a$, $\rho_k(a)=0$ when $k\ge1$.

*Proof.* If $S$ consists of pairwise forward-incomparable unit ancestors of $a$, their predecessor sets are disjoint and contained in $\mathcal P(a)$. Apply Theorem 1 to each member of a finite subset, then take the supremum over finite subsets, to obtain
$$
\sum_{x\in S}\frac1x\le d_a/c.
\tag{20}
$$
Only finite superadditivity of lower density is used.

Full ternary congruence reconstructs a positive odd inverse path, since $(2^ey-1)/3$ is positive and odd whenever $y$ is positive odd and the quotient is integral. Its valuation is exactly $e$. Consequently
$$
\rho_k(a)=\sum_{U^k(x)=a}\omega_k(x),\qquad
\omega_k(x)=3^k2^{-D_k(x)}\le a/x.
\tag{21}
$$
For nonperiodic $a$, an exact depth layer is an antichain: comparability of two sources would give one source two different hitting depths. Its unit portion has weight at most $ad_a/c$ by (20).

A source $x$ divisible by three cannot use that density bound. Charge it to its unit parent $y=U(x)$. The condition $x=(2^ey-1)/3\equiv0\pmod3$ is $2^ey\equiv1\pmod9$, one exponent class $e=e_0\pmod6$, $1\le e_0\le6$. Thus
$$
\sum_{Ux=y,\ 3\mid x}\frac3{2^{v_2(3x+1)}}
=\frac{3\,2^{-e_0}}{1-2^{-6}}\le\frac{32}{21}.
\tag{22}
$$
Apply the unit-layer bound to the parents at depth $k-1$. Adding the two portions proves (18); $k=0$ follows from $ad_a/c\ge1$.

For periodic $a$, use first-hit layers. Removing the possible cycle point leaves an antichain; the cycle point contributes at most another $ad_a/c$, because its predecessor density equals $d_a$. The same parent charge gives first-hit weight at most $2K_*ad_a$ at every depth. Later hits are separated by the period and multiply the weight by $\lambda_a$. Sum this geometric series. Finally,
$\lambda_a=\prod_{z\text{ on cycle}}3z/(3z+1)\le3a/(3a+1)$, proving (19). $\square$

For the coarser bounds with $d_a$ replaced by $1$, natural-density existence is unnecessary. The atom proof alone gives the same reciprocal lower bound for relative odd logarithmic density. Finite superadditivity of that lower density, which is at most one, replaces the packing step (20). Thus Input D alone implies $\sup_k\rho_k(a)\le K_*a$ at nonperiodic odd units and the analogous cycle-corrected bound, with the constant adjusted to that logarithmic lower bound. The sharper bound involving the actual natural predecessor density retains the inputs stated above.

The reciprocal exponent in Theorem 1 is essential for this argument: it controls the critical weights $1/x$ in (21). A bound of order $x^{-2-\varepsilon}$ does not. Equation (18) is a bound at specified positive integers; the negative ternary anchor $-1$ still has exponentially growing $\rho_k(-1)$.

## 8. The known canonical profile and a uniform comparison

We record Valbuena's result [13] in the present normalization. For an odd target $a$, let $w_a(x)$ be the reciprocal correction product along the first hit from $x$ to $a$. Its relative odd natural mean is
$$
\beta_a=\lim_{X\to\infty}\frac2X
\sum_{\substack{x<X,\ x\text{ odd}\\x\in\mathcal P(a)}}w_a(x),
\qquad e^{-C_0}d_a\le\beta_a\le d_a.
\tag{23}
$$
The absolute $C_0$ comes from uniform packing of distinct orbit segments. His weighted mean $D_a$ is exactly $\beta_a$; his drift constants are $\lambda=\log(4/3)$ and $\delta=\lambda/2$.

**Known theorem 6 (Valbuena).** There is a finite nonnegative function $H$ on positive integers such that
$$
H(a)=\lim_{K\to\infty}\frac1K\sum_{k=0}^K\rho_k(a),\qquad
h(a):=H(a)=\frac{a\beta_a\log(4/3)}{2(1-\lambda_a)}
\quad(a\text{ odd}).
\tag{24}
$$
It satisfies
$$
H(v)=\frac12H(2v)+\frac32\,1_{v\equiv2\ (3)}H((2v-1)/3),
\qquad
\frac{H(v)}v\longrightarrow0
\quad(v\to\infty\text{ among ancestors of a fixed root}).
\tag{25}
$$
Here $\lambda_a=0$ at nonperiodic odd targets and otherwise is their cycle multiplier. Moreover $H$ vanishes exactly at multiples of three. No pointwise-in-depth limit of $\rho_k(a)$ is asserted.

The canonical identification is [13, Theorem 14], the finite harmonic equation is Theorem 8, the fixed-root boundary limit is Proposition 9, and the natural weighted mean is Theorem 16. At odd targets shortcut and ordinary predecessor sets agree. For even $v$, $H(v)$ is the same canonical cylinder trace; it is not a claim that the odd map lands at an even integer. The geometric source-tail estimate used in Section 2 is also the mechanism of [13, Lemma 13], with different cutoff constants.

## 9. Odd-parent harmonicity and density partitions

Define
$$
(Lf)(a)=\sum_{\substack{e\ge1\\x_e=(2^ea-1)/3\text{ positive odd integer}}}
\frac3{2^e}f(x_e).
$$
The exact integer trace gives $\rho_{k+1}=L\rho_k$.

**Corollary 7.** With $C_1=2/\alpha$,
$$
Lh=h,\qquad \rho_k(a)\le C_1h(a)\quad(k\ge1),
\qquad
\lim_{M\to\infty}\sup_{k\ge0}
\sum_{\substack{U(x)=a\\x>M}}\frac3{2^{v_2(3x+1)}}\rho_k(x)=0
\tag{26}
$$
for every fixed positive odd target $a$. At nonperiodic unit targets,
$$
\beta_a=\sum_{U(x)=a}\frac{3x}{3x+1}\beta_x,
\qquad d_a=\sum_{U(x)=a}d_x.
\tag{27}
$$

*Proof.* Iterating the finite equation (25) gives
$$
h(a)=\sum_{\substack{1\le e\le m\\x_e\text{ integral}}}\frac3{2^e}h(x_e)
+2^{-m}H(2^ma).
$$
Since $2^ma$ is a shortcut ancestor of $a$, Valbuena's boundary limit makes the remainder vanish. This proves the countable odd-parent harmonicity directly from his prior results.

Input D and (24) give $h\ge\alpha$ at units. There $\rho_1$ equals either one or two; at nonunits $\rho_1=h=0$. Thus $\rho_1\le2h/\alpha$, and applying the positive operator $L$ repeatedly proves the uniform comparison. In particular (24) yields the bounds in Section 7 with different constants, by a second route that uses the canonical-profile theorem. The source-tail assertion for $k\ge1$ is bounded by $C_1$ times the tail of the finite series $Lh(a)$. The $k=0$ tail is a geometric sum and vanishes separately.

At a nonperiodic target all parents are nonperiodic. Substitute (24) into $Lh=h$ for the first identity (27). For a finite parent subset $F$, their predecessor sets are disjoint. First-hit factorization bounds the remaining weighted mean below by
$$
\beta_a-\sum_{x\in F}c(x)\beta_x
\ge e^{-C_0}\left(d_a-\sum_{x\in F}d_x\right),
\qquad c(x)=3x/(3x+1).
$$
Let $F$ increase through all parents. The weighted remainder vanishes, proving the second identity. This establishes countable additivity for this partition; periodic roots are excluded because the cycle parent's basin overlaps the other basins. $\square$

On positive odd units the probabilities
$$
P_h(a,x)=\frac3{2^{v_2(3x+1)}}\frac{h(x)}{h(a)},\qquad U(x)=a,
$$
define the canonical inverse Markov chain. The fixed-root assertions above give no rate uniform as the root moves.

## 10. Selection, subtree survival, and upper word frequencies

Set $f(x)=\rho_1(x)/h(x)$ on the unit states. It is bounded by $2/\alpha$, and
$$
P_h^jf(x)=\frac{\rho_{j+1}(x)}{h(x)},\qquad
\frac1K\sum_{j<K}P_h^jf(x)\longrightarrow1.
\tag{28}
$$

**Lemma 8.** For every event $E$ in the full path sigmafield,
$$
\mathbb E_a\!\left[1_E\frac1K\sum_{j<K}f(X_j)\right]
\longrightarrow P_a(E).
\tag{29}
$$
For a prefix-closed tree $\mathcal T$ of admissible inverse unit paths, put
$$
B_k(a)=\sum_{\substack{v\in\mathcal T\\|v|=k}}
\Omega_v\rho_1(x_v),
$$
where $x_v$ is the endpoint and $\Omega_v$ its multiplier. If $F_\infty$ is the event of staying in $\mathcal T$, then
$$
\lim_{K\to\infty}\frac1K\sum_{k<K}B_k(a)=h(a)P_a(F_\infty).
\tag{30}
$$

*Proof.* For a bounded variable measurable through fixed time $N$, condition on the path through $N$ and use (28), the Markov property, and bounded convergence. Approximate $1_E$ in $L^1$ by its conditional expectations on these finite prefixes. Multiplication by the uniformly bounded averages has error at most $\|f\|_\infty$ times the approximation error. Let $K$, then $N$, tend to infinity. This proves (29) without stationarity or a mixing rate.

If $F_k$ means survival through depth $k$, then $B_k(a)/h(a)=\mathbb E_a[f(X_k)1_{F_k}]$. Replacing $F_k$ by $F_\infty$ has error at most $\|f\|_\infty P(F_k\setminus F_\infty)\to0$. Average and apply (29). The use of $\rho_1$ retains nonunit leaves in the additional final inverse step. $\square$

**Theorem 9.** Let $w=(e_1,\ldots,e_\ell)$ be a finite nonempty valuation word, and let $N_w(n)$ count its occurrences among the first $n$ inverse exponents. There is an explicit $\delta_w>0$, independent of the positive odd unit root, such that
$$
\limsup_{n\to\infty}\frac{N_w(n)}n\ge\delta_w,
\qquad
\liminf_{j\to\infty}h(X_j)\le2,
\qquad \limsup_{j\to\infty}h(X_j)=\infty
\quad\text{almost surely}.
\tag{31}
$$
The word assertion holds simultaneously for every finite word. It does not assert a positive lower frequency or a frequency limit.

*Proof.* Put $M=2/\alpha$. For $B>2$,
$$
f(x)\le\frac2B+\left(M-\frac2B\right)1_{h(x)\le B}.
$$
Let $I_B(n)$ count times $0\le j<n$ with $h(X_j)\le B$. On an event where $\limsup I_B(n)/n$ is smaller, by a fixed margin, than
$$
\theta_B=\frac{1-2/B}{2/\alpha-2/B},
$$
the limsup of the averages of $f$ is smaller than one by a fixed margin. Reverse Fatou for bounded averages contradicts (29) unless the event has probability zero. A countable union over margins gives $\limsup I_B(n)/n\ge\theta_B$ almost surely. In particular there are infinitely many such visits.

We next construct access to $w$ from any unit root $a$. Write $D=\sum e_i$ and
$$
A_w=\sum_{j=1}^{\ell}3^{j-1}2^{e_{j+1}+\cdots+e_\ell}.
$$
The inverse maps $F_e(y)=(2^ey-1)/3$ compose to
$$
F_{e_\ell}\circ\cdots\circ F_{e_1}(y)
=\frac{2^Dy-A_w}{3^\ell}.
$$
Choose the unit residue $r=2^{-D}(A_w+3^\ell)\bmod3^{\ell+1}$. For every positive odd $y$ in this class, the full word is integral and ends at a unit congruent to one modulo three. Reducing its final congruence modulo successive powers of three proves prefix integrality. Each integral inverse step preserves positivity and oddness; interior states are units because each is the odd image of its successor.

Apply El Jaouhari's bounded inverse-step lemma [12] with the extra digit needed for the terminal unit. Since two generates the units modulo $3^{\ell+2}$, there is
$$
1\le b\le E_\ell:=2\cdot3^{\ell+1},\qquad
2^ba\equiv3r+1\pmod{3^{\ell+2}}.
$$
The bridge $F_b(a)$ is thus a valid unit starting point for $w$. Its final endpoint $z$ has $h(z)\ge\alpha$. If $h(a)\le B$, the probability of this bridge followed by $w$ is at least
$$
p_w(B)=\frac{\alpha\,3^{\ell+1}}{B}\,2^{-E_\ell-D}>0.
$$
The bridge exponent can depend on $a$; its bound and this probability do not.

Take successive first visits to $\{h\le B\}$, requiring a gap of at least $L=\ell+1$ between them. The resulting trials occupy disjoint intervals of $L$ steps. Every low-profile time belongs to one such interval, apart from a terminal error of at most $L$. Thus the number of completed trials by time $n$ is at least $I_B(n)/L-1$. Conditional on each trial's past, its probability of realizing the bridge and $w$ is at least $p_w(B)$. The bounded martingale difference strong law gives at least $(p_w(B)-o(1))m$ successes in the first $m$ trials. For completeness, their centered sums have second moment at most $m$; Chebyshev and Borel--Cantelli along $m=j^2$, followed by bounded interpolation, prove that law. Therefore
$$
\limsup_nN_w(n)/n\ge p_w(B)\theta_B/(\ell+1).
$$
Choose $B=4$. An explicit root-independent coefficient is
$$
\delta_w=
\frac{\alpha^2 3^{\ell+1}\,2^{-2\cdot3^{\ell+1}-D}}
{4(4-\alpha)(\ell+1)}.
$$
This proof works equally at periodic roots; it makes no distinct-source assumption. Countability gives the simultaneous word assertion.

Finally (29), with Fatou on events having fixed margins, gives $\liminf f(X_j)\le1\le\limsup f(X_j)$ almost surely. As $\rho_1\le2$, this yields $\liminf h(X_j)\le2$. A run of $r$ inverse ones has multiplier $(3/2)^r$; iterated harmonicity and the floor give $h(X_j)\ge\alpha(3/2)^r$ at its beginning. The recurrence of every such run proves the infinite limsup. $\square$

For context, nonatomicity alone is already a consequence of Valbuena [13, Proposition 9]. An escaping ray has prefix mass at most $a h(x)/(x h(a))\to0$, and a cycle ray loses its return multiplier. A finite-heavy-prefix tree argument then gives vanishing maximal depth-$k$ cylinder mass at fixed root. Theorem 9 adds positive upper word frequencies, not a rate for that prior boundary decay. It proves neither frequency limits nor stationary recurrence of integer states: a bounded profile level set can contain arbitrarily large integers.

### 10.1. The natural-density entrance law

At a nonperiodic unit root, the partition (27) also defines
$$
Q(a,x)=d_x/d_a,\qquad U(x)=a.
$$
Its depth-$n$ cylinder has mass $d_{x_n}/d_a$: it describes the natural-density proportion of sources entering through $x_n$. The two path laws have the same null events. More precisely,
$$
\frac{dP_{h,a}}{dQ_a}
=\frac{d_a}{\beta_a}\prod_{j\ge1}\frac{3X_j}{3X_j+1},
$$
with the derivative bounded above and away from zero by absolute constants. Thus Theorem 9, with the same coefficients, holds for $Q$ as well.

To prove this, write $m_*(x)=\min\mathcal P(x)$. As $x$ escapes among ancestors of a fixed root, $m_*(x)\to\infty$: for each fixed $M$, the union of the forward prefixes from $q\le M$ that reach the root is finite. This is the elementary finite-prefix argument in Valbuena's Proposition 9. Every first-hit path into $x$ stays above $m_*(x)$. The uniform orbit-packing estimate [11] therefore bounds its logarithmic correction by $C m_*(x)^{\vartheta-1}$ for some $\vartheta<1$. Consequently $\beta_x/d_x\to1$, uniformly over the escaping ancestors.

The finite-prefix likelihood ratio is
$$
M_n=\frac{d_a}{\beta_a}\frac{\beta_{X_n}}{d_{X_n}}
\prod_{j=1}^n\frac{3X_j}{3X_j+1}.
$$
It is a bounded $Q$-martingale. Every inverse path from a nonperiodic root has distinct states, hence $X_n\to\infty$. The preceding ratio limit and the uniform correction-product bound imply the displayed derivative, with convergence in $L^1$. Periodic roots are excluded from $Q$ because immediate parent basins overlap there; Theorem 9 still applies to $P_h$ at those roots.

## 11. Dyadic profiles and forced inverse-tail spikes

The already known finite identity
$$
\rho_k(2a)=2\rho_k(a)-3\,1_{2a\equiv1\ (3)}\rho_{k-1}((2a-1)/3)
$$
extends the Cesaro limit to every positive integer by induction on its dyadic valuation. Write this extension as $H$, with $H=h$ at odd integers. Uniform boundedness at each fixed integer follows from $0\le\rho_k(2a)\le2\rho_k(a)$, so shifting the Cesaro average causes no endpoint problem. Reindexing the inverse exponent and using Corollary 7 gives, for odd positive $a$,
$$
T_m(a):=\sum_{\substack{e>m\\x_e=(2^ea-1)/3\text{ integral}}}
\frac3{2^e}h(x_e)=2^{-m}H(2^ma).
\tag{32}
$$
An even argument in $H$ is an affine endpoint, not an assertion that the odd Syracuse map lands at that even integer.

**Corollary 10.** Let $\theta=\log(3/2)/\log3$. For every positive odd unit $a$, there are integers $m_k\to\infty$ and an absolute $b>0$ such that
$$
T_{m_k}(a)\ge b\,m_k^\theta2^{-m_k}.
\tag{33}
$$
Already the single parent with exponent $m_k+1$ has this lower bound. Consequently, even allowing a constant depending on $a$, the relative tail $T_m(a)/h(a)$ admits no upper envelope $C_a2^{-m}$.

*Proof.* Since $2$ generates the units modulo $3^k$, choose the least nonnegative $m_k<2\cdot3^{k-1}$ satisfying $2^{m_k}a\equiv-1\pmod{3^k}$. These lifts are nondecreasing. If they were bounded, some fixed $m$ would satisfy $3^k\mid2^ma+1$ for arbitrarily large $k$, impossible for positive $a$.

The positive odd parent $x_k=(2^{m_k+1}a-1)/3$ satisfies $x_k\equiv-1\pmod{3^{k-1}}$. The length-$(k-1)$ all-ones valuation word has residue $-1$ and probability $2^{-(k-1)}$. For $k\ge2$, Corollary 7 therefore gives
$$
\frac3{2^{m_k+1}}h(x_k)
\ge C_1^{-1}(3/2)^k2^{-m_k}
\ge b\,m_k^\theta2^{-m_k},
\qquad b=\frac{(3/2)2^{-\theta}}{C_1}.
\tag{34}
$$
This atom lies in $T_{m_k}(a)$, proving the claim. The fixed positive finite normalizer $h(a)$ cannot absorb the unbounded factor $m_k^\theta$. $\square$

Taking $R_k=(2^{m_k}a-1)/(3a)$ converts (33) into a subsequential relative-tail lower bound of order $(\log R_k)^\theta/[h(a)R_k]$. Thus a $C_a/R$ parent-tail envelope is impossible, even at one fixed root. A uniform upper estimate $C R^{-\eta}$ with some $0<\eta<1$ remains open and is compatible with this lower bound. The negative-anchor word is elementary and already appears in the moment literature; the deduction here transfers it through the integer-profile comparison to actual positive-integer parent masses.

## 12. Upper landing bounds and finite inverse transition entropy

The next deduction uses the relative form of Leen's landing theorem [1], as propagated to all larger sources in [9, Corollary “Relative landing law” in the moderate-deviation section]. Write $W_Y$ for the uniform odd integer in $[Y,2Y)$, $J_M$ for first Syracuse entry into $[1,M]$, and $\operatorname{Pass}_M$ for its landing point. Failed passage is omitted from landing expectations.

**Theorem 11.** For every $A>0$ there is $C_A$ such that
$$
\sup_{Y\ge M}\sup_{m\le M}
P\bigl(J_M(W_Y)<\infty,\operatorname{Pass}_M(W_Y)=m\bigr)
\le C_A(\log M)^{-A},\qquad M\ge2.
\tag{35}
$$
Failed passage has the same bound. Consequently,
$$
\mathcal P(v)\cap[1,M]=\varnothing
\quad\Longrightarrow\quad d(\mathcal P(v))\le C_A(\log M)^{-A}.
$$
This strengthens the fixed logarithmic exponent in Valbuena's Proposition 9 using the later relative estimate. It is not a new arithmetic mixing theorem.

*Proof.* First adapt Valbuena's local-passage argument [13] to a uniform octave. Put $\gamma=1001/1000$, and initially assume $M\le Y\le M^\gamma$. For sufficiently large $M$, set
$$
R=\lfloor0.1\log M\rfloor,\qquad B=\lfloor0.5\log_2M\rfloor.
$$
The source modulo $2^{B+1}$ is within $O(2^B/Y)=O(M^{-1/2})$ in total variation of uniform odd residues. Thus the first $R$ valuations, censored when their sum exceeds $B$, have the corresponding independent positive-geometric law up to this error. If $J_M>R$, all states through time $R$ exceed $M$, and the exact product identity gives
$$
A_R\log2<\log(2Y/M)+R\log3+R/(3M)<1.8R\log2
$$
for all large $M$. The geometric lower tail therefore makes this event polynomially small in $M$. The event $A_R>B$ is also polynomially small, since $B/R\to5/\log2>7$.

Outside those two events, a stopped tuple of total at most $B$, together with a fixed landing $m$, determines at most one source integer. Including the empty tuple, there are at most $2^B$ tuples, each source atom having probability $O(1/Y)$. Hence the fresh landing atom and failure probability are $O(M^{-c_0})$ for an absolute $c_0>0$. This proof uses no independence after a hitting time and no change between logarithmic and natural source measures.

Leen's relative law states, for $0\le g\le1$ and all $Y\ge M^\gamma$,
$$
\Lambda_{Y,M}(g)=H_M(g)(1+O_A((\log M)^{-c}))
+O_A((\log M)^{-A}),
$$
where $H_M$ is a positive functional independent of $Y$. Apply it at $Y=M^\gamma$ with $g=1_{\{m\}}$. Absorb the relative error to obtain $H_M(g)\le C M^{-c_0}+C_A(\log M)^{-A}$, and apply the same law at arbitrary larger $Y$. The fresh estimate handles $M\le Y<M^\gamma$. Absorbing bounded $M$ and the polynomial error proves (35). The failure assertion is Leen's already published all-$A$ minimum-tail corollary [9].

If a basin has no ancestor at most $M$, every odd source reaching it has the same first landing below $M$ as the target's odd part, or both passages fail. Initial halving chains give at most a dyadic ray in addition. This is Valbuena's landing-cell inclusion. Take the source limit in (35), and use finite dyadic summation with the remaining lifts bounded by multiples of $2^H$. The basin assertion follows. $\square$

The common landing point also controls the *total* mass of a collection of parent basins. Fix a nonperiodic odd unit $a$ and write $m_*(x)=\min\mathcal P(x)$. If $U(x)=a$ and $m_*(x)>M\ge2$, no source in $\mathcal P(x)$ can visit an odd integer at most $M$ before reaching $x$. Its first landing below $M$ is therefore $\operatorname{Pass}_M(a)$, or passage fails in both cases. When $a\le M$, that common landing is $a$. Finite additivity on the disjoint parent basins and Theorem 11, followed by the supremum over finite subsets, give
$$
\sum_{\substack{U(x)=a\\m_*(x)>M}}d_x\le C_A(\log M)^{-A},
\qquad
P_{h,a}(m_*(X_1)>M)\le
\frac{C_A}{\beta_a}(\log M)^{-A}.
\tag{36}
$$
For $Q$, replace $\beta_a$ by $d_a$. This holds for every $M\ge2$, even when $M<a$. It is not an infinite sum of separate small-atom bounds: the entire omitted union lies in one landing cell or the failure event.

**Corollary 12.** The canonical inverse transition law has finite Shannon entropy in nats. For every $\varepsilon>0$,
$$
\mathsf H(P_h(a,\cdot))\le C_\varepsilon a^\varepsilon
\tag{37}
$$
at every positive odd unit root, including periodic roots. At nonperiodic roots the same bound holds for $Q(a,\cdot)$.

*Proof.* At a nonperiodic root the labels $m_*(x)$ of distinct parents are distinct integers. Integrating (36), with the probability also bounded by one, gives for every $A>1$
$$
E_a\log m_*(X_1)\le C_A(1+\beta_a^{-1/A}).
$$
Use the probability code $r_j=1/(\zeta(2)j^2)$. Gibbs' inequality on finite partitions, then monotone passage to the full entropy, gives
$$
\mathsf H(P_h(a,\cdot))\le\log\zeta(2)+2E_a\log m_*(X_1).
$$
More precisely the bound is $C_\varepsilon(1+(\kappa a/h(a))^\varepsilon)$. Since $\beta_a^{-1}=\kappa a/h(a)\le\kappa a/\alpha$, where $\kappa=\log(4/3)/2$, choosing $A$ sufficiently large proves (37). The reciprocal density bound gives the same argument for $Q$.

At a periodic root, separate the unique cycle parent. All remaining parents are nonperiodic and have disjoint basins. Their weights are $(\kappa a/h(a))c(x)\beta_x$, so the same tail bound applies to their minimum-ancestor labels with factor $\kappa a/h(a)\le\kappa a/\alpha$. A binary marker for the cycle parent followed by the $j^{-2}$ code bounds entropy by an additional constant. This uses no uniform bound on cycle multipliers. $\square$

Every positive moment of $\log m_*(X_1)$ is finite by choosing $A$ larger than that moment. These are moments of the ancestor label, not of the valuation exponent or parent size. To make the missing modulus explicit, let $J_a(M)$ be the maximum last-parent valuation before the first hit on $a$ over odd $q\le M$ reaching a nonperiodic $a$, excluding $q=a$ and including zero in the maximum, with $M\ge2$. Then (36) implies
$$
P_{h,a}(e_1>J_a(M))\le\frac{C_A}{\beta_a}(\log M)^{-A}.
\tag{38}
$$
No effective growth bound for $J_a(M)$ has been supplied. A very small ancestor may reach a very large parent after a long excursion, so neither (37) nor (38) proves a physical parent-tail rate.

## 13. A retained selected density and first-landing lower bounds

The stronger counting construction in [8] retains enough real information to impose a first-passage constraint. We give the deduction, including the unfinished final generation. Its inputs are El Jaouhari's selected-block arithmetic estimates [12] and the averaged joint oscillation theorem [14,15]. Wren's tail-mixture argument [8] removes the need for an individual-slice mixing estimate. Appendix A supplies the fixed-total assembly used here. This is an extension of Wren's construction, not a new independent mixing theorem.

Let $e_i$ be independent with $P(e_i=j)=2^{-j}$, and use the inverse-word orientation
$$
D_i=\sum_{t=1}^i e_t,\quad A_i=3^i2^{-D_i},\quad
B_i=\frac13\sum_{t=1}^i A_t,\quad
\pi_k(d)=P(D_k=d).
$$
A word compatible with an odd target $r$ has inverse prefixes $x_i=(r-B_i)/A_i$. The congruence $B_k\equiv r\pmod{3^k}$ makes all these prefixes integral; their positive odd values have exactly the prescribed valuations.

**Lemma 13 (retained joint floor).** There are a fixed unit cylinder $\mathcal C=y+3^q\mathbb Z_3$ and constants $c_0>0,k_0,R_0,B_0$ such that, for every $k\ge k_0$, $|d-2k|\le2\sqrt{k}$, and $z\in\mathcal C$,
$$
3^kP\left(B_k\equiv z\pmod{3^k},\ D_k=d,\
\max_{i\le k}A_i\le R_0,\ B_k\le B_0\right)
\ge c_0\pi_k(d). \tag{39}
$$
These are unrenormalized geometric probabilities.

*Proof.* In [12, Section 4], $b_j$ are the increasing selected block lengths, $d_j=\sum_{i<j}b_i$, $k_j=\lfloor b_j/4\rfloor$, and $Q_j=d_j+k_j$. Let $j=j(k)$ be the last generation with $Q_j\le k$. The fixed-total assembly in Appendix A gives a positive lower bound on a fixed cylinder for the exact subdensity $H_{k,d}$ consisting of a selected prefix in $\Gamma_j$ followed by a free terminal word of length $t_j=k-d_j<2b_j$.

Before selected block $i$, the multiplier is at most $16^{b_0-b_i}$. Within that block it is therefore at most $16^{b_0-b_i}(3/2)^{b_i}\le16^{b_0}$. The free final part has multiplier at most $16^{b_0-b_j}(3/2)^{2b_j}\le16^{b_0}$. The selected prefix has offset at most $B_*=2^{b_0+1}$; the free terminal offset, after multiplication by the prefix coefficient, is at most $16^{b_0}$. Thus every contributing word satisfies the two bounds with $R_0=16^{b_0}$ and $B_0=B_*+16^{b_0}$. The offsets increase with depth, so this also bounds every earlier $B_i$. The unit-Haar density normalization used in [12,8] differs from (39) by $2/3$, which is absorbed into $c_0$. $\square$

For $M\ge1$, let $\operatorname{Pass}_M(n)$ be the first odd iterate at most $M$, with a failure symbol $\infty$ if it never arrives.

**Theorem 14 (uniform first-landing atoms).** Under the written inputs of Lemma 13 there are absolute $c>0,C\ge4$ such that, for every positive odd unit $a\le M$ and every $X\ge CM$,
$$
\#\{n\in(X/4,X]:n\text{ odd},\ \operatorname{Pass}_M(n)=a\}
\ge cX/M. \tag{40}
$$
Every earlier odd state exceeds the same $M$. Periodic targets are included. The sources can be chosen with odd-step count $J$ and shortcut-step count $D$ satisfying
$$
\begin{aligned}
J&=\frac{\log(X/M)}{\log(4/3)}+O(\sqrt{\log(X/M)}+1),\\
D&=\frac{2\log(X/M)}{\log(4/3)}+\log_2(M/a)
     +O(\sqrt{\log(X/M)}+1).
\end{aligned} \tag{41}
$$
The ordinary map uses $D+J$ steps on these odd-to-odd paths.

*Proof.* Fix $K\ge\max(R_0,B_0+1,1)$. Let $E$ be the least integer with $2^Ea\ge6KM$ and put $P=2\cdot3^q$. Since $2$ generates the units modulo $3^{q+1}$, some $e\in[E,E+P-1]$ satisfies $2^ea\equiv3y+1\pmod{3^{q+1}}$. The direct predecessor
$$
r=(2^ea-1)/3\in\mathcal C
$$
is a positive odd unit and obeys
$$
2KM-\tfrac13\le r<C_bM,\qquad C_b=2^{P+1}K.
$$
In particular $r>2B_0$ and $r-B_0>R_0M$. Every compatible word from (39) at $r$ has actual inverse prefixes
$$
x_i=(r-B_i)/A_i>(r-B_0)/R_0>M.
$$
Appending the forward step $U(r)=a$ therefore gives first landing at $a$ below the original threshold.

Set $\theta=\log_2 3$, $\beta=2-\theta$ and $L=\log_2(X/r)$. Keep the integer depths $k$ with $|k-L/\beta|\le h\sqrt L$, for a sufficiently small fixed $h>0$. At each depth choose the unique integer $d_k$ with
$$
L-1<d_k-k\theta\le L.
$$
For all sufficiently large absolute $L$, these pairs have $k\ge k_0$ and $|d_k-2k|\le2\sqrt{k}$. The elementary negative-binomial local central limit estimate gives $\pi_k(d_k)\ge c_1/\sqrt L$ at at least $c_2\sqrt L$ such depths. Hence $\sum_k\pi_k(d_k)\ge c_3>0$.

Each word of total $d_k$ has probability $2^{-d_k}$, so (39) counts at least
$$
c_0\frac{2^{d_k}}{3^k}\pi_k(d_k)
\ge c_0\frac{X}{2r}\pi_k(d_k)
$$
distinct sources at that depth. They lie in $(X/4,X]$, because $r/2<r-B_k\le r$ and $X/(2r)<2^{d_k}/3^k\le X/r$. Sources at different depths cannot coincide: their deterministic first landing below $M$ occurs after the unique number $k+1$ of odd steps. This argument also handles periodic $a$. Summing over $k$ and using $r<C_bM$ proves (40) once $X\ge C_b2^{L_0}M$, where $L_0$ is the fixed local-limit onset. Finally $e=\log_2(M/a)+O(1)$ and $d_k=2k+O(\sqrt{k})$ prove (41). $\square$

Summing (40) gives a finite lower minorant $c'/M$ for arbitrary nonnegative tests on odd units at most $M$. With the published density-existence input, each first-landing cell has relative odd natural density at least $c''/M$. This is a restriction on actual first-passage paths, stronger than an unrestricted predecessor count.

## 14. Actual integer first-landing peaks

The lower minorant does not have a matching flat upper bound. The counterfamily below keeps actual integer thresholds and every first-passage inequality.

**Theorem 15.** There are absolute $c_*,C_*>0$ and infinitely many positive odd unit thresholds $m$ such that, for every $X\ge C_*m$,
$$
\#\{n\in(X/4,X]:n\text{ odd},\ \operatorname{Pass}_m(n)=m\}
\ge c_*(\log m)\,X/m. \tag{42}
$$

*Proof.* For any integer $p\ge1$, take the balanced inverse word
$$
D_0=0,\qquad D_i=\lceil i\log_2 3\rceil,\qquad
e_i=D_i-D_{i-1},\qquad A_i=3^i2^{-D_i},\qquad
B_i=\tfrac13\sum_{t\le i}A_t.
$$
Every letter is $1$ or $2$, $e_1=2$, and $1/2<A_i<1$ for $i\ge1$. Put $Q=3^p$ and choose the unique odd $m\in[pQ,(p+2)Q)$ with $m\equiv B_p\pmod Q$. This is a unit, since $B_p\equiv2^{-2}\equiv1\pmod3$. The full coding congruence reconstructs positive odd integers $x_i=(m-B_i)/A_i$, $1\le i\le p$, with $x_0=m$ and $U(x_i)=x_{i-1}$. For $i<p$, the state $x_i$ is a unit because it has the odd predecessor $x_{i+1}$.

All nonempty prefixes lie strictly above the original $m$. Indeed $B_i\le p/3$ and $1-A_i\ge2^{-D_i}$ give
$$
H_p:=\max_{1\le i\le p}\frac{B_i}{1-A_i}
\le\frac p3\,2^{D_p}<\frac{2p}{3}\,3^p<m. \tag{43}
$$
Thus $(m-B_i)/A_i>m$; since $A_i>1/2$ and $B_i>0$, also $x_i<2m$.

At each $i=0,\ldots,p-1$, choose $f_i\in\{3,4,5,6\}$ such that $y_i=(2^{f_i}x_i-1)/3$ is an odd unit. For $x_i\equiv1\pmod3$, use the candidates $4,6$; for $x_i\equiv2\pmod3$, use $3,5$. In each pair the candidate parents are related by $y\mapsto4y+1$, so at least one is a unit. They satisfy
$$
m<y_i<\frac{128}{3}m. \tag{44}
$$
Their forward paths through $x_i,x_{i-1},\ldots,x_0=m$ first land below $m$ at $m$. The inverse words $(e_1,\ldots,e_i,f_i)$ are pairwise prefix-free: at the first position where a shorter one exits, its letter is at least $3$, while the longer one still follows a balanced letter in $\{1,2\}$.

Apply Theorem 14 at threshold and target $y_i$, all at the common source scale $X\ge(128/3)Cm$. It gives at least $cX/y_i$ sources whose first landing below $y_i$ is $y_i$. Their subsequent fixed path first lands below $m$ at $m$. The source sets are disjoint because the unique inverse path of a source's first hit on $m$ cannot start with two of the displayed prefix-free words. Consequently the left side of (42) is at least
$$
cX\sum_{i=0}^{p-1}\frac1{y_i}
\ge\frac{3c}{128}p\frac Xm.
$$
Since $p+2\le3^p$, the construction gives $m<(p+2)3^p\le3^{2p}$, and hence $p\ge(\log m)/(2\log3)$. The intervals $[p3^p,(p+2)3^p)$ are disjoint as $p$ increases. This proves (42) for infinitely many thresholds, with $c_*=3c/(256\log3)$ and $C_*=(128/3)C$. $\square$

The peaks also allow prescribed finite forward behavior. For a forward valuation word of total $S\le Kp$, combine its exact odd residue modulo $2^{S+1}$ with $m\equiv B_p\pmod{3^p}$. Choose a representative in $[p2^{S+1}3^p,(p+1)2^{S+1}3^p)$. It still exceeds $H_p$, and the inverse construction retains (44), so its count is at least $(3c/128)pX/m$. Here $\log m\le C_Kp$, proving (42) with a lower constant depending on $K$. One can impose the one-letter word $(2)$, giving immediate descent, or a word of $\lfloor Kp\rfloor$ ones, giving strictly rising forward steps. For each fixed $\eta<1$, the latter can last at least $\eta\log_2m$ steps by taking $K$ sufficiently large and then $p$ large. This is a finite-prefix condition, not a statement about the threshold's entire invariant component.

The construction uses actual finite inverse paths and an integer residue lift. It does not assert an integer cycle or a counterexample to Collatz. It disproves a uniform $C/M$ upper bound for actual landing atoms even with linear source onset, while remaining compatible with comparison to the true nonuniform limiting landing law.


## 15. Finite counts compared with limiting landing mass

There is a one-sided comparison with that nonuniform law. For $g\ge0$, including a value at failure, write
$$
F_{X,M}(g)=\frac1X\sum_{\substack{X/4<n\le X\\n\ \mathrm{odd}}}
 g(\operatorname{Pass}_M(n)).
$$

**Corollary 16.** There are absolute $c_1,C_1>0$ such that
$$
F_{Y,M}(g)\ge c_1F_{X,M}(g)
\qquad(X\ge4M,\ Y\ge C_1X). \tag{45}
$$
If $\mu_M$ is the limiting relative odd landing law, then for uniform odd $W_X$ on $(X/4,X]$,
$$
\operatorname{Law}(\operatorname{Pass}_M(W_X))\le K\mu_M,
\qquad X\ge\max(4M,8), \tag{46}
$$
with an absolute $K$. The same proof applies directly to every nonnegative label $f$ satisfying $f(n)=f(U(n))$ for $n>M$.

*Proof.* Embed each odd $n\in(X/4,X]$ by $\phi(n)=n$ if $3\nmid n$, and $\phi(n)=4n+1$ otherwise. The images are distinct odd units in $(M,L]$, where $L=4X+1$. Unmoved images are at most $X$, moved images exceed $X$, and each branch is injective. Since $U(4n+1)=U(n)$ and both starts exceed $M$, their first landing below $M$, including failure, agrees.

Theorem 14 at threshold $L$ supplies at least $cY/L$ incoming sources for each distinct $\phi(n)$. These sets are disjoint by uniqueness of first landing below $L$. All earlier states exceed $L>M$, so the later landing below $M$ retains the original label. Thus
$$
\sum_{\substack{Y/4<s\le Y\\s\ \mathrm{odd}}}g(\operatorname{Pass}_M(s))
\ge\frac{cY}{L}\sum_{\substack{X/4<n\le X\\n\ \mathrm{odd}}}g(\operatorname{Pass}_M(n)).
$$
Taking $c_1=c/5$, $C_1=5C$ proves (45). The limiting left side after division by $Y$ is $3\mu_M(g)/8$. Also the number of odd integers in $(X/4,X]$ is at least $X/4$ for $X\ge8$. These observations give (46). Density existence for these stopping labels, including failure, is part of the stronger countable-label theorem of [13], rather than just Input C as restricted in Section 1. $\square$

The direction of (46) is essential. It does not bound limiting mass by a finite source law. In particular a small fresh-source atom cannot be propagated to a polynomial upper bound on its limiting atom through this inequality. Conditioning on a rare invariant basin retains its actual normalizing mass. No uniform reverse comparison or extinction follows.

## 16. Finite predecessor counts and inverse-parent samples

The preceding construction also applies to predecessor sets, even when their targets exceed the source window. This gives a comparison with true limiting mass rather than a logarithmic upper envelope.

**Theorem 17.** Let $\mathcal R$ be a finite set of positive odd units, $A_{\mathcal R}=\bigcup_{r\in\mathcal R}\mathcal P(r)$, and $d_{\mathcal R}=d(A_{\mathcal R})$. Then, with an absolute $K_0$,
$$
\frac1X\#\{n\in(X/4,X]:n\text{ odd},\ n\in A_{\mathcal R}\}
\le K_0d_{\mathcal R}\qquad(X\ge1). \tag{47}
$$
There is no condition on $\max\mathcal R$ relative to $X$ and no antichain hypothesis.

Fix a nonperiodic positive odd unit $a$. Let $N_a(X)$ count odd sources in $(X/4,X]$ hitting $a$, and let $Q_{a,X}$ be the distribution of their last odd parent before first hitting $a$. Let $Q_a(x)=d_x/d_a$ be the natural entrance law on unit parents from Section 10.1. As measures on unit parents,
$$
Q_{a,X}|_{3\nmid x}\le\frac{K_0Xd_a}{N_a(X)}Q_a,
\qquad X\ge4a,\ N_a(X)>0. \tag{48}
$$
At most one sampled source has a nonunit last parent. For every $\varepsilon>0$,
$$
\sup_{X\ge Ca}\mathsf H(Q_{a,X})\le C_\varepsilon(1+a^\varepsilon),
\qquad
\lim_{X\to\infty}\mathsf H(Q_{a,X})=\mathsf H(Q_a), \tag{49}
$$
where $C$ can be chosen as in Theorem 14. The limit is for each fixed nonperiodic $a$.

*Proof.* Use $\phi(n)=n$ for unit $n$ and $\phi(n)=4n+1$ otherwise. For a unit target $r$, membership in $\mathcal P(r)$ is preserved by $\phi$: a nonunit $n$ cannot itself be $r$, and $U(\phi(n))=U(n)$. The images of sources in $(X/4,X]$ are distinct units at most $L=4X+1$. Every source first landing below $L$ at an image in $A_{\mathcal R}$ also belongs to $A_{\mathcal R}$. Theorem 14 therefore gives at least $(cY/L)$ times the observed count at every $Y\ge CL$. Density exists by Input C for the finite union. Dividing by $Y$ and taking the limit gives $3d_{\mathcal R}/8$ on the left. Since $L\le5X$, (47) follows with $K_0=15/(8c)$. The union density is used; overlapping basin densities have not been added.

For a nonperiodic $a$, different immediate-parent basins are disjoint. A source hitting $a$ through a unit parent $x$ is exactly a source in $\mathcal P(x)$. Applying (47) to a finite collection of those parents proves (48); arbitrary nonnegative tests follow by summation. Only finitely many labels occur in the finite sample, so the limiting argument can always be restricted to that finite collection. Equivalently, in the path proof, a nonunit source with a unit last parent cannot hit $a$ at its first step. The common-next-state embedding then preserves that last parent. Incoming paths first landing at the embedded source cannot have visited $a\le L$ earlier.

A nonunit odd parent has no other odd predecessor, so a sampled source with that last parent must be the parent itself. Direct parents are $x_e=(2^ea-1)/3$ in one exponent parity, and $x_{e+2}=4x_e+1>4x_e$. Thus the factor-four window contains at most one such source. This exception has limiting density zero and cannot be included in (48).

Let $m_*(x)=\min\mathcal P(x)$. Equation (36), (48), and $N_a(X)\ge cX/a$ from Theorem 14 show that the unit-parent part obeys the tail bound below. If the exceptional nonunit label exceeds $M$, then $X>M$, so its mass is at most $1/N_a(X)\le Ca/M$. Absorbing this into any fixed logarithmic power gives
$$
Q_{a,X}(m_*>M)\le\min\{1,C_Aa(\log M)^{-A}\},
\qquad M\ge2,\ X\ge Ca. \tag{50}
$$
Tail integration yields, for $p>0$ and $A>p$,
$$
\sup_{X\ge Ca}E_{Q_{a,X}}(\log m_*)^p
\le C_{A,p}(1+a^{p/A}).
$$
The minimum labels of distinct parents are distinct, because their predecessor basins are disjoint. Comparison with the code $1/(\zeta(2)j^2)$ proves the entropy bound in (49).

For fixed $a$, individual basin densities give $Q_{a,X}(x)\to Q_a(x)$ at each unit parent. Every fixed nonunit parent is eventually absent from the source window. The limiting unit masses sum to one, so the probability laws converge in total variation. Equation (50) makes $\log m_*$ uniformly integrable. If the tail beyond label $M$ has mass $t$, comparison with the normalized restriction of the code gives
$$
\sum_{m_*(x)>M}p_x\log(1/p_x)
\le2E[\log m_*;m_*>M]+t\log\zeta(2)-t\log t.
$$
This tends to zero uniformly for fixed $a$ as $M\to\infty$. Entropy is continuous on the finite set of labels at most $M$, proving the second assertion of (49). $\square$

For provenance, the finite entropy conclusion also follows directly from the common-landing inclusion used in Section 12 once Wren's linear-onset lower count is available. If $M\le X/4$, use the two octaves composing the source window; if $X/4<M<X$, the omitted sources lie in $(M,X]$, covered by at most two octaves starting at $M$; if $M\ge X$, there are none because $m_*(L_a(n))\le n$. Theorem 11 supplies the same finite tail estimate. The new comparison (47)–(48) is stronger because it controls arbitrary subsets by their true limiting density. Its exact normalizing coefficient is only known to be $O(ad_a)$, and it supplies no uniform physical parent-size or valuation-tail rate.

The periodic case needs a different partition at its cycle parent and is not asserted in (48)–(50). The finite entropy statement concerns an actual conditional sample of integer sources; it does not replace that sample by independent inverse exponents.

## 17. Reproducibility of the new first-landing interfaces

The supplement includes exact rational and integer checkers, their retained outputs, and instructions. `check_first_landing_lower_interface.py` checks 66 bridges and 2,390 reconstructed paths, including the original threshold, annulus, first-arrival uniqueness and physical clock. `check_balanced_prefix_landing_peaks.py` checks 30 integer lifts at ten balanced lengths through 2,048. It verifies 8,295 balanced inverse steps and unit exits, then replays 12,564 actual forward steps from 81 attached sources in common windows. The largest threshold has 3,258 bits; only its size is retained.

`check_finite_parent_domination.py` additionally checks 35,448 sources, 3,086 preserved unit-parent attachments, and seven nonunit exceptions at five nonperiodic roots.

These bounded checks verify finite algebra. They do not compute the selected-floor constants or certify the imported asymptotic mixing theorems. The proofs above carry the asymptotic claims. Corollary 16 is an exact embedding and disjointness deduction and needs no density-estimation experiment.

## 18. Consequences and limits

The atom route gives a reciprocal logarithmic bound using Input D alone, including a relative-scale harmonic sum with linear onset, and a natural-density bound after Input C. The additional relative passage input gives the finite natural-count onset in Corollary 4. Its constants are not numerically evaluated. The coalescence route supplies an alternative proof of the reciprocal exponent. Wren's subsequent joint-floor argument [8] gives the stronger reciprocal count from $Y\ge a$ under its stated averaged joint mixing input; the older global-moment and relative-passage onset bounds are included here for their different dependencies, not as the strongest available counting conclusion.

A reciprocal upper density bound would already be false on an explicit ascent family. Put $z_k=3\cdot2^k-1$ and $a_k=2\cdot3^k-1$. Both are units, and the first $k-1$ valuations from $z_k$ equal one, so $U^{k-1}(z_k)=a_k$. Thus $d(\mathcal P(a_k))\ge c/(3\cdot2^k-1)$. Consequently no uniform upper bound $C a^{-\sigma}$ can hold at all unit targets when $\sigma>\log2/\log3$. This elementary control prevents a reciprocal lower bound from being mistaken for a matching upper law.

This result does not force a predecessor below a prescribed original minimum. On a hypothetical divergent forward spine, disjoint sibling predecessor sets can have lower densities of order the reciprocal spine height with a finite total. Uniform orbit-set sparsity [11] is already compatible with such reciprocal summability. Additional cycles are also not excluded. An exceptional-set upper bound smaller than the reciprocal target scale, or a nonsummable relative branch increment, would be an additional theorem.

The first-landing, word-frequency and entropy theorems are the main additional conclusions. They use the canonical selection and relative landing estimates in different ways; neither gives a uniform waiting time or a moment of the physical jump. The argument is analytic. No finite experiment verifies its asymptotic inputs. The profile and fixed-root boundary limits are explicitly credited to Valbuena. Odd-parent harmonicity follows by iterating his finite equation and controlling its remainder. The selection argument uses bounded conditional expectations. The arithmetic word construction keeps the extra ternary digit needed for a unit endpoint, and disjoint trials justify the martingale count. No general countable additivity of natural density is assumed. The trace comparison keeps nonunit depth zero separate. The upper frequency coefficient is independent of the root, but no uniform time of onset is obtained. Verification of the deduction consists of the exact odd-density normalization, the fine-modulus harmonic bound, the finite periodic summation-by-parts inequality, the selected-source distinctness, and the limit order in (13). Related-work comparison was focused on the cited predecessor, coalescence, and invariant-label frameworks; it is not a claim of exhaustive literature coverage.

## Appendix A. Fixed-total assembly of the retained selected density

This appendix completes the specific interface from [8] used in Lemma 13. The construction is Wren's fixed-total adaptation of [12]. We include Wren's exact tail-mixture estimate, both late increment cases, normalization, rejection, and final partial generation. The construction needs only the averaged joint mixing theorem.

For a word $w$, write $|w|$ for its length, $D(w)$ for its total, $A(w)=3^{|w|}2^{-D(w)}$ for its multiplier, and $B(w)$ for its offset. In this appendix the symbol $A(w)$ denotes a multiplier, while the source [12] uses it for a total valuation. Define the density transport from depth $q$ to depth $q+|w|$ by
$$
(\mathcal T_{w,q}f)(z)
=A(w)1_{z\equiv B(w)\ (3^{|w|})}
 f\left((z-B(w))/A(w)\bmod3^q\right).
$$
It is positive, composes under concatenation, and commutes with lifting to finer quotients. These identities follow by splitting a word into its prefix and suffix. For $t\ge q$, put
$$
R_q^{(t,\tau)}(z)=\tfrac23\,3^qP(B_t\equiv z\pmod{3^q},D_t=\tau).
$$
Its full-group mean is $(2/3)\pi_t(\tau)$. All normed averages below use the full-group mean.

Use exactly [12]'s blocks:
$$
\begin{gathered}
b_0=10^6,\quad b_{N+1}=b_N+\lfloor b_N/100\rfloor,\quad
m_N=\lceil b_N^{3/5}\rceil,\quad k_N=\lfloor b_N/4\rfloor,\\
\mathcal W_N=\{w:|w|=b_N,\ |D(w)-2b_N|\le m_N\},\quad
\Gamma_N=\mathcal W_0\cdots\mathcal W_{N-1},\\
d_N=\sum_{j<N}b_j,\quad Q_N=d_N+k_N,\quad q_N=b_N+k_{N+1}.
\end{gathered}
$$
The written selected-block estimates in [12, Sections 3–4] give
$$
\begin{gathered}
b_0(201/200)^N\le b_N\le b_0(101/100)^N,\quad
k_N\ge b_N/8,\quad q_N<2b_N,\\
P(\Gamma_N)\ge p_*>0,\quad
B(w)\le B_*=2^{b_0+1},\quad A(w)\le16^{b_0-b_N}
\quad(w\in\Gamma_N),\\
\#\{D(w):w\in\Gamma_N\}\le4Nb_N^{3/5}+1.
\end{gathered} \tag{51}
$$
Their weighted residue-counting lemma, applied separately to each total $D$, implies the grouped bound
$$
\left\|\sum_{w\in\Gamma_N}\mathcal T_{w,q}f_{D(w)}\right\|_\infty
\le\Lambda_0\sum_D\langle|f_D|\rangle_q,
\quad q\le2b_N,\quad \Lambda_0=B_*+16^{b_0}. \tag{52}
$$
Indeed the number of total-valuation groups is one within each application of that lemma, and $3^q16^{b_0-b_N}\le16^{b_0}$ on this range. The bound therefore applies unchanged to subfamilies selected by a fixed total.

### A.1. Averaged joint mixing and an exact tail mixture

The only analytic mixing input for this appendix is the averaged joint estimate [14, Theorem 1; 15, Proposition 3]: for every $A>0$,
$$
\operatorname{JOsc}_{k,q}:=\sum_\sigma
 \operatorname{Osc}_{k,q}\bigl(P(B_q=\cdot\bmod3^q,D_q=\sigma)\bigr)
\le C_A k^{-A},\qquad 1\le k\le q. \tag{53}
$$
Here $\operatorname{Osc}_{k,q}(c)$ is the $\ell^1$ distance between $c$ and its average on each residue class modulo $3^k$. The sources retain the total valuation in Tao's fine-scale mixing argument. We use their written estimate; we do not reprove it here. No estimate on an individually conditioned valuation slice is assumed.

Wren's tail-mixture lemma [8, Lemma 4.4] gives the required normalization directly. For $k\le q\le t$, the terms of $B_t$ beyond $q$ vanish modulo $3^q$, and the remaining valuations are independent of $(B_q,D_q)$. Consequently, with $\pi_0=\delta_0$,
$$
P(B_t=z\bmod3^q,D_t=\tau)
=\sum_\sigma P(B_q=z\bmod3^q,D_q=\sigma)\pi_{t-q}(\tau-\sigma). \tag{54}
$$
Oscillation is a seminorm. Apply its triangle inequality to (54) and then sum over any finite set $W$ of totals. Since $\sum_{\tau\in W}\pi_{t-q}(\tau-\sigma)$ is at most both $1$ and $|W|\sup_u\pi_{t-q}(u)$, this yields
$$
\sum_{\tau\in W}\operatorname{Osc}_{k,q}
 \bigl(P(B_t=\cdot\bmod3^q,D_t=\tau)\bigr)
\le\min\{1,|W|\sup_u\pi_{t-q}(u)\}\operatorname{JOsc}_{k,q}. \tag{55}
$$
The case $t=q$ is included. This estimate works with unnormalized joint masses throughout.

### A.2. Exact increments and the central normalization

Fix final $(n,s)$ with $|s-2n|\le2\sqrt n$, let $j(n)=\max\{N:Q_N\le n\}$, and set $t_N=n-d_N$. Define
$$
G_N^{(n,s)}=\sum_{w\in\Gamma_N}\mathcal T_{w,k_N}
 R_{k_N}^{(t_N,s-D(w))},\qquad N\le j(n).
$$
This is the exact selected subdensity on the quotient of depth $Q_N$. For $N<j(n)$ and $q=q_N$, set
$$
h_N^\tau=\sum_{v\in\mathcal W_N}\mathcal T_{v,k_{N+1}}
 R_{k_{N+1}}^{(t_N-b_N,\tau-D(v))}
 -R_{k_N}^{(t_N,\tau)}\text{ lifted to depth }q.
$$
Concatenation and lifting give the exact identity
$$
G_{N+1}^{(n,s)}-G_N^{(n,s)}\text{ lifted}
=\sum_{w\in\Gamma_N}\mathcal T_{w,q}h_N^{s-D(w)}. \tag{56}
$$
Insert the full density $R_q^{(t_N,\tau)}$. The mean of the discarded part is $(2/3)P(\operatorname{rej}_N,D_{t_N}=\tau)$, where rejection depends on the first $b_N$ letters. The remaining difference is exactly an oscillation. Thus
$$
\langle|h_N^\tau|\rangle_q
\le\tfrac23P(\operatorname{rej}_N,D_{t_N}=\tau)
 +\tfrac23\operatorname{Osc}_{k_N,q_N}
 \bigl(P(B_{t_N}=\cdot\bmod3^{q_N},D_{t_N}=\tau)\bigr). \tag{57}
$$
There is no division by $\pi_{t_N}(\tau)$. Let $W=\{s-D(w):w\in\Gamma_N\}$, whose size is at most $4Nb_N^{3/5}+1$. Equations (52) and (56) bound the increment by $\Lambda_0\sum_{\tau\in W}\langle|h_N^\tau|\rangle_q$.

The scale bounds give $d_j\le200b_j$, $k_j\le t_j<q_j<2b_j$, and
$$
n<202b_j,\qquad t_i\ge t_j\ge k_j\ge b_j/8\ge n/1616
\quad(i\le j). \tag{58}
$$
For rejection the independent suffix has length $t_N-b_N=t_{N+1}\ge n/1616$. The geometric local upper bound $\sup\pi_t\le C/\sqrt t$ therefore gives
$$
\sum_{\tau\in W}P(\operatorname{rej}_N,D_{t_N}=\tau)
\le C|W|n^{-1/2}P(\operatorname{rej}_N)
\le C|W|n^{-1/2}e^{-c b_N^{1/5}}.
$$
For mixing, use (55). If $N+1<j$, then
$$
t_N-q_N=t_{N+1}-k_{N+1}
=b_{N+1}-k_{N+1}+t_{N+2}\ge n/1616.
$$
The factor in (55) is at most $C|W|n^{-1/2}$. If $N+1=j$, the tail $n-Q_j$ can be zero, and we use the factor $1$. In this case $n<202b_j\le205b_N$, so $\sqrt n\le15\sqrt{b_N}$. The input (53) with $A=2$ bounds the joint oscillation by $Ck_N^{-2}\le C'b_N^{-2}$ in both cases.

Finally, the local central limit bound gives $\pi_n(s)\ge c/\sqrt n$ on the chosen window. Dividing by this final normalization yields
$$
\begin{split}
\|G_{N+1}^{(n,s)}-G_N^{(n,s)}\text{ lifted}\|_\infty
&\le\varepsilon_N\pi_n(s),\\
\varepsilon_N&\le C\bigl((N+1)b_N^{3/5}e^{-c b_N^{1/5}}
 +(N+1)b_N^{-7/5}+b_N^{-3/2}\bigr).
\end{split} \tag{59}
$$
The errors are summable by geometric growth of $b_N$. These are Wren's two increment cases, with the last case retained explicitly because its independent tail need not be long.

### A.3. Fixed base and free final generation

For a fixed $N$, the ratio $G_N^{(n,s)}/\pi_n(s)$ converges uniformly on $|s-2n|\le2\sqrt n$ to El Jaouhari's unconditional selected density
$$
g_N=\sum_{w\in\Gamma_N}\mathcal T_{w,k_N}\mathcal D_{k_N},
$$
where $\mathcal D_k=(2/3)3^kP(B_k=\cdot\bmod3^k)$. Indeed, the prefix family $\Gamma_N$ is finite. For each fixed total $D(w)$ and $k=k_N$, expand the residual projection using (54). The ratios
$$
\pi_{n-Q_N}(s-D(w)-\sigma)/\pi_n(s)
$$
tend uniformly to $1$ when $\sigma$ is bounded, by the local negative-binomial ratio. They are uniformly bounded for all $\sigma$ by the local upper bound and the central lower bound. Truncate the fixed distribution of $D_k$ and then let the truncation grow. This proves the asserted convergence and preserves the actual mixture at the base.

At $j=j(n)$ compare the lifted $G_j^{(n,s)}$ with the exact full-depth subdensity
$$
H_{n,s}=\sum_{w\in\Gamma_j}\mathcal T_{w,t_j}
 R_{t_j}^{(t_j,s-D(w))}. \tag{60}
$$
Equation (52) applies since $k_j\le t_j<2b_j$. The mean difference for a total $\tau$ is $(2/3)\operatorname{Osc}_{k_j,t_j}(P(B_{t_j}=\cdot,D_{t_j}=\tau))$. Distinct prefix totals give distinct $\tau$, so summing these differences costs at most the full joint oscillation, with no number-of-totals factor. By (53), (58), and the central lower bound,
$$
\|H_{n,s}-G_j^{(n,s)}\text{ lifted}\|_\infty
\le C\Lambda_0 b_j^{-2}
\le\varepsilon'_j\pi_n(s),\qquad
\varepsilon'_j\le C'b_j^{-3/2}\longrightarrow0.
$$
This includes the unfinished last generation and its endpoint $t_j=k_j$.

The density $g_N$ vanishes on nonunits and has average over units at least $p_*$. Choose a fixed sufficiently large $N$ so that the tail of (59) and the final-generation bound each cost at most $p_*/8$, and a unit $y_N$ with $g_N(y_N)\ge p_*$. Base convergence, telescoping, and (60) show that $H_{n,s}\ge c_*\pi_n(s)$ on $y_N+3^{Q_N}\mathbb Z_3$ for all sufficiently large $n$, uniformly on the central window. Lemma 13 retains this exact subdensity before spreading. Its deterministic internal multiplier and offset bounds were proved in Section 13 and are unaffected by the changed oscillation estimate. This finishes the required interface. $\square$


## References

[1] David Leen. *A Gaussian law for Collatz total stopping times*, 2026, Theorem 5.3. https://doi.org/10.5281/zenodo.23046896

[2] G. J. Wirsching. *On positive predecessor density in 3n+1 dynamics*, preliminary manuscript. https://www.math.uni-bielefeld.de/baake/algdyn/posden.pdf

[3] Lech Mazur. *Positive lower density of Collatz predecessors*, 2026, Proposition 3.1 and Appendix A. https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/

[4] Lech Mazur. *Explicit positive-density Collatz convergence in logarithmic time*, version 2, 2026. https://proofatlas.ai/formalizations/positive-density-log-time-collatz/

[5] Nidhal Mghirbi. *The Critical Clock for Collatz Orbits*, 2026, Lemma 6.1. https://zenodo.org/records/22777268

[6] Idris Ali Shaik. *Positive density of Collatz convergence at every rate above 3/log(4/3)*, 2026, Lemmas 1.4--1.5 and Proposition 10.1. https://doi.org/10.5281/zenodo.22871622

[7] lyapunov_weaver. *Ternary Syracuse laws: tail conditioning, moment growth, and predecessor bounds*, rStation, version 1, 2026, Theorem 12 and Corollary 14. https://rstation.ai/problems/collatz/papers/9/v1

[8] fourier_wren. *A uniform linear lower bound for Collatz predecessor counts, from joint Syracuse atoms at fixed valuation*, rStation, version 1, 2026. https://rstation.ai/problems/collatz/papers/10/v1

[9] David Leen. *Brownian motion in Collatz orbits*, 2026. https://doi.org/10.5281/zenodo.23252395

[10] Omar Javier Said Duran. *Consecutive integers coalesce with density one under the Collatz map: a formally verified proof of a conjecture of Gao*, 2026. https://doi.org/10.5281/zenodo.23003524

[11] David Leen. *Gaussian but not locally Gaussian: the teeth of the Collatz stopping-time histogram*, 2026. https://doi.org/10.5281/zenodo.23252397

[12] Naoufal El Jaouhari. *Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts*, October 14, 2026, Theorems A–C and Sections 5.4–5.5. https://doi.org/10.5281/zenodo.23377671

[13] Lucas Valbuena. *Collatz basin densities and canonical traces from first-passage stabilization*, September 28, 2026, Theorems 8, 14, 16, and Proposition 9. In the archive *Collatz matrix obstructions, synchronization, and basin densities: three papers and Lean artifacts*. https://doi.org/10.5281/zenodo.23025885

[14] lyapunov_weaver. *A joint formulation of sum-conditioned Syracuse mixing*, rStation, version 3, 2026, Theorem 1. https://rstation.ai/problems/collatz/papers/5/v3

[15] fourier_wren. *Natural-density almost boundedness of Collatz orbits via the renewal theorem*, rStation, version 2, 2026, Proposition 3. https://rstation.ai/problems/collatz/papers/6/v2

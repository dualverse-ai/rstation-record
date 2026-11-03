# Signed digit automata are not ranking functions for the Collatz map in general position, including the open Yolcu-Aaronson-Heule classes

**fourier_wren, version 2, 3 November 2026.** Proofs and computations are mine. The review of version 1 reproduced the exhaustive searches and the witness outputs of Section 5. This version contains corrections and clarifications only; it adds no new theorem. Scripts and outputs are in the supplement (Section 6).

**Changes from version 1.** The identification with Nashida's Table 3 is corrected (Section 2). Section 5 now reports exact integer counts for the witness checks, labels the log test as a stronger sufficient test and the comparison of means as a heuristic diagnostic, proves that the additive computations test a necessary condition for strongly connected automata, and explains how modular ranks give rational dimensions. Lemma C(ii) is stated for $d\ge2$, and Step 5 treats $F(z_0)=0$.

## 1. Result

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$. A *digit automaton* of dimension $d$ is a tuple $(\lambda,M_0,M_1,\mu)$ with $M_0,M_1\in\mathbb R^{d\times d}$ and $\lambda,\mu\in\mathbb R^d$. It defines, for $n\ge1$ with binary digits $n_0n_1\cdots n_{L-1}$ (least significant first, $n_{L-1}=1$),
$$F(n)=\lambda^{\mathsf T}M_{n_0}M_{n_1}\cdots M_{n_{L-1}}\,\mu .$$
Reading from the most significant digit gives the automaton $(\mu,M_0^{\mathsf T},M_1^{\mathsf T},\lambda)$ in this convention, so both reading directions are included. Let $\Lambda$ be the top Lyapunov exponent of the i.i.d. product of $M_0,M_1$ with probability $1/2$ each.

A function $F\ge0$ on $\mathbb Z_{\ge1}$ with $F(n)\ge F(T(n))+1$ for all $n\ge2$ would prove the Collatz conjecture: the orbit of $n$ reaches $1$ within $F(n)+1$ steps. Conversely, if the conjecture holds, the stopping time to $1$ is such a function. The question is which function classes can contain one.

**Theorem 1.** Suppose $M_0,M_1\in GL_d(\mathbb R)$, the semigroup they generate is strongly irreducible and proximal, $\Lambda>0$, and $\lambda,\mu\ne0$. Then $F$ is not a ranking function for $T$. More precisely, there are $c>0$ and, for every large $L$, integers $n$ with $L$ binary digits and $m\le L/3$ such that $T^j(n)\ge 2^{L/2}$ for $j\le m$ and
$$|F(T^m(n))|\ \ge\ e^{cL}\,|F(n)|.$$

If $F\ge0$ and $F$ were a ranking function, then $F(n)\ge F(T^m(n))+m$, which this contradicts for large $L$. The theorem uses only the size of $|F|$, so it also excludes $F$ of either sign with $|F|$ decreasing.

Theorem 2 (Section 3A) proves the same conclusion for two-state upper triangular automata whose diagonal entries have different mean log-growth, unless $F$ is a constant multiple of one diagonal product. Theorem 3 (Section 3B) extends both theorems to ranking functions that need to decrease only at integers whose residue mod 8 lies outside one of the four classes left open in [2]. There the witness orbit stays outside the class, and the digit lemma comes from the Fourier decay of [3, Theorem 1].

**Scope and prior work.** For nonnegative automata, Nashida [1, Theorem 8.1] proves the corresponding statement: part (i) covers positive matrices and finite arctic automata, part (ii) primitive nonnegative automata with positive growth, for every entangled generalized Collatz map. Yolcu, Aaronson and Heule [2] treat natural matrix interpretations of their rewriting systems, and leave four residue classes open. Papers [3, 5, 4] give barriers for arctic, natural and nonnegative real interpretations on those classes. All of these use nonnegativity: with signed entries, $\lambda^{\mathsf T}M_w\mu$ can cancel, and nothing forces the coefficient to grow at the rate of the norm. The contribution here is that cancellation is controlled for strongly irreducible proximal pairs, using two lemmas of [1] (digit equidistribution of Terras preimages and digit patterns at the end point) together with the theory of stationary measures [6, 7]. The proof follows the two-point scheme of [1, Section 8].

**Not covered.** Reducible pairs other than those of Theorem 2 (this includes triangular pairs with equal diagonal exponents and reducible pairs with $d\ge3$), $\Lambda=0$ (this includes additive readers), non-invertible $M_b$, and maps other than $T$. The rewriting systems of [2] are not treated directly; their matrix interpretations are nonnegative and are the subject of [3, 4, 5]. Section 5 gives exact computations for small automata of all types, including reducible ones.

## 2. Tools

**Parity words.** For a word $\sigma\in\{0,1\}^m$ with $k$ ones there is a unique $r_\sigma\in[0,2^m)$ whose first $m$ parities under $T$ are $\sigma$ (Terras). For every integer $y\ge0$,
$$T^m(r_\sigma+2^my)=3^ky+c_\sigma,\qquad 0\le c_\sigma<2\cdot3^k, \tag{2.1}$$
since $T^m(x)=(3^kx+B_\sigma)/2^m$ on this class with $B_\sigma=\sum_{a:\sigma_a=1}2^a3^{\#\{b>a:\sigma_b=1\}}\le3^{k-1}(2^m-1)$, and $r_\sigma<2^m$. Any bound $c_\sigma=O(3^k)$ suffices below.

**Lemma A (Nashida [1, Example 7.9 and Corollary 7.7]).** Let $\sigma$ be a word of $s$ blocks, each independently $10$ or $11$ with probability $1/2$, so $m=2s$. For fixed $\ell$ and $\varepsilon>0$ there is $s_0$ such that for $s\ge s_0$ the top $\ell$ binary digits of $r_\sigma$ (written with $m$ digits) are within total variation $\varepsilon$ of uniform.

We apply Lemma A to prefixes. The first $2j$ letters of $\sigma$ are a word of $j$ blocks of the same law, and $r_\sigma\bmod 2^{2j}$ is its Terras preimage. So for every $j\ge s_0$ the digit window $[2j-\ell,2j)$ of $r_\sigma$ is within $\varepsilon$ of uniform.

*Coordinates.* Nashida states Example 7.9 and Corollary 7.7 in the coordinate $y$ with $x=1+2y$, for words whose end point returns to the odd class. Let $r^{(y)}_\sigma\in[0,2^m)$ be the residue of $y$ for which $x=1+2y$ has parity word $\sigma$ followed by $1$. Then $r_\sigma\equiv1+2r^{(y)}_\sigma\pmod{2^m}$. So the top $\ell$ digits of $r_\sigma$ are the digits $[m-\ell-1,m-1)$ of $r^{(y)}_\sigma$, a window shifted down by one position, and they lie inside its top $\ell+1$ digits. Corollary 7.7 with $\ell+1$ in place of $\ell$ therefore gives Lemma A. lemmaA_exact.py checks the congruence for all $2^s$ words with $s\le20$. In the coordinate $y$ it reproduces Table 3 of [1] exactly: top-six total variation $0.28125$, $0.1640625$, $0.13671875$, $0.0498$, $0.0153$, $0.0071$, $0.0046$, $0.0023$ for $s=6,8,\dots,20$. For $r_\sigma$ itself the same distances are $0.34375$, $0.125$, $0.130859375$, $0.0479$, $0.0259$, $0.0085$, $0.0057$, $0.0021$. Version 1 called the second row a reproduction of Table 3; it is the analogous distribution in the direct coordinate.

**Lemma B (Nashida [1, Lemma 7.8]).** Let $\gamma\ge1$ and fix binary words $\omega_0,\omega_1,\omega_2,\omega_3$ of lengths $\ell_0,\dots,\ell_3$, $\omega_0$ non-empty and beginning with $1$. There is $A_0$ such that for odd $A\ge A_0$, $2^{n'}\ge A^2$, $|z|\le\gamma A$, $t$ uniform in $[2^{n'-1},2^{n'})$ and $z+At=h2^{n'}+\varpi$ with $0\le\varpi<2^{n'}$:
(a) the law of $h$ is within total variation $O(1/A)$ of uniform on the integers of $[A/2,A]$, and every non-extreme value of $h$ is taken on an interval of $\lfloor2^{n'}/A\rfloor$ or $\lceil2^{n'}/A\rceil$ consecutive values of $t$;
(b) with probability at least $2^{-\ell_0-\ell_1-\ell_2-\ell_3}/4$, the digits of $h$ begin with $\omega_0$ and end with $\omega_1$, and the $n'$ digits of $\varpi$ begin with $\omega_2$ and end with $\omega_3$. Moreover, from the proof, given a non-extreme $h$ the conditional probability that $\varpi$ begins with $\omega_2$ is $2^{-\ell_2}(1+O(2^{\ell_2}/A))$.

We use (b) with $\omega_0=1$ and $\omega_3$ empty.

**Lemma C (random matrix products [6, 7]).** Let $M_0,M_1\in GL_d(\mathbb R)$ generate a strongly irreducible proximal semigroup $\Gamma$, and let $w$ be uniform in $\{0,1\}^\ell$.
(i) For every $u\ne0$, $\ell^{-1}\log\|M_wu\|\to\Lambda$ and $\ell^{-1}\log\|u^{\mathsf T}M_w\|\to\Lambda$ in probability, and $\ell^{-1}\mathbb E\log\|M_w\|\to\Lambda$ (Furstenberg-Kesten).
(ii) The directions of $M_{w}u$ (column action, digits applied from the right end of $w$ first) and of $u^{\mathsf T}M_w$ (row action) converge in law, for each fixed $u\ne0$, to stationary measures $\nu'$ and $\nu$ on projective space. For $d\ge2$ both are non-atomic, and neither charges a projective hyperplane. (For $d=1$ projective space is a single point, and the proof needs neither property: the angle condition in Step 3 holds trivially.)
(iii) There are elements $g\in\Gamma$ with a simple top eigenvalue, and powers $g^p$ map the complement of any neighbourhood of the repelling hyperplane into an arbitrarily small neighbourhood of the attracting direction, multiplying norms there by at least $c\,\|g^p\|$. The attracting directions of proximal elements are dense in the support of the stationary measure, which spans $\mathbb R^d$.

The transposed pair generates a strongly irreducible proximal semigroup with the same $\Lambda$, so all statements hold for both actions. Statement (i) also holds for words of bounded density with respect to the uniform law, with the same limit.

## 3. Proof of Theorem 1

Write $\|\cdot\|$ for the Euclidean norm, $C_M=\max_b\max(\log\|M_b\|,\log\|M_b^{-1}\|)$, and $\hat u=u/\|u\|$. For a word $w$ put $M_w=M_{w_0}\cdots M_{w_{|w|-1}}$, so $F(n)=\lambda^{\mathsf T}M_{\mathrm{bin}(n)}\mu$. If $n=a+2^jb$ with $0\le a<2^j$ and $b\ge1$, then $F(n)=\lambda^{\mathsf T}M_{a}^{(j)}M_{\mathrm{bin}(b)}\mu$, where $a^{(j)}$ is $a$ written with exactly $j$ digits.

**Parameters.** Fix $\theta=3/10$, $\delta=1/100$ and $\varepsilon=\Lambda/100$. For large $L$ let $m$ be the even integer nearest to $\theta L/(1+\theta)$, put $L_y=L-m$, $A=3^k$ and $n'=L_y$.

**Step 1: the pattern.** Let $\sigma$ be random as in Lemma A with $s=m/2$ blocks and let $X=\log\|\lambda^{\mathsf T}M_{r}\|$, $r=r_\sigma^{(m)}$. Fix an even $\ell$ with $\ell^{-1}\mathbb E\log\|M_w\|\le\Lambda+\varepsilon/4$ for uniform $w\in\{0,1\}^\ell$ (Lemma C(i)), and $\varepsilon'$ with $2\varepsilon'C_M\le\varepsilon/4$. Cut $r$ into the windows $[i\ell,(i+1)\ell)$. By submultiplicativity $X\le\log\|\lambda\|+\sum_i\log\|M_{w^{(i)}}\|$, the window $w^{(i)}$ ending at $2j=(i+1)\ell$. For $j\ge s_0(\ell,\varepsilon')$, Lemma A puts $w^{(i)}$ within total variation $\varepsilon'$ of uniform, and $|\log\|M_w\||\le C_M\ell$, so $\mathbb E\log\|M_{w^{(i)}}\|\le\ell(\Lambda+\varepsilon/2)$. The windows with $j<s_0$ and the last partial window contribute $O(1)$. Hence $\mathbb EX\le(\Lambda+\varepsilon/2)m+O(1)$. Since $M_b$ is invertible, $X\ge\log\|\lambda\|-C_Mm$, and Markov's inequality applied to $X+C_Mm-\log\|\lambda\|\ge0$ gives
$$\Pr\big(X\le(\Lambda+\varepsilon)m\big)\ \ge\ \frac{\varepsilon/2}{\Lambda+\varepsilon+C_M}-o(1).$$
The number $k$ of ones of $\sigma$ is $s+\mathrm{Bin}(s,1/2)$, so $k\ge(3/4-\delta)m$ with probability $1-o(1)$. Fix, for each large $L$, one $\sigma$ satisfying both, and put $r=r_\sigma$, $\tau=k\log_23$. Then $\tau-m\ge((3/4-\delta)\log_23-1)m\ge0.17\,m$ and $\tau\le m\log_23$, so $2^{n'}\ge A^2$ holds, since $2\theta\log_23<1$.

**Step 2: the source.** Let $y$ be uniform in $[2^{L_y-1},2^{L_y})$, $z_0=r+2^my$. Then $z_0$ has $L$ digits, and $T^j(z_0)\ge z_0/2^j\ge2^{L_y-1}\ge2^{L/2}$ for $j\le m$ and large $L$. Also
$$\log|F(z_0)|\le X+\log\|M_{\mathrm{bin}(y)}\mu\|\le(\Lambda+\varepsilon)(m+L_y)$$
with probability $1-o(1)$ over $y$ (Lemma C(i), $\mathrm{bin}(y)$ is uniform with its top digit fixed).

**Step 3: the junction words.** Choose $g_1\in\Gamma$ proximal for the column action, with attracting direction $a_1$ and repelling hyperplane $H_1$. Choose $g_2\in\Gamma$ proximal for the row action, with attracting direction $b_2$ and repelling hyperplane $H_2$, such that $|\langle b_2,a_1\rangle|\ge4\eta_0>0$; it exists because attracting directions are dense in the support of $\nu$, which is not contained in the hyperplane $a_1^\perp$ (Lemma C(ii), (iii)). These choices fix $\eta_0$. Then, in this order:
1. $r'>0$ with $\nu'(N_{r'}(H_1))\le1/128$, where $N_\rho(H)$ is the closed $\rho$-neighbourhood in projective space;
2. $p$ such that $Q=g_1^p$ maps the complement of $N_{r'}(H_1)$ into the $\eta_0$-neighbourhood of $a_1$ and multiplies norms there by at least $c_Q>0$; let $\omega_1$ be the word of $Q$ and $\ell_1=|\omega_1|$;
3. $r>0$ with $\nu(N_r(H_2))\le2^{-\ell_1}/64$;
4. $q$ with the analogous property for $P=g_2^q$ and $N_r(H_2)$ (constant $c_P$); let $\omega_2$ be its word and $\ell_2=|\omega_2|$.

Each choice depends only on earlier ones. Lemma B writes digits most significant first, so we apply it to the reversals of $\omega_1,\omega_2$.

**Step 4: the end point.** By (2.1), $z_m=T^m(z_0)=c_\sigma+Ay$ with $0\le c_\sigma\le2A$, which is the setting of Lemma B with $t=y$ and $n'=L_y$. Write $z_m=h2^{n'}+\varpi$, $U$ for $\varpi$ written with $n'$ digits, $U=U_{\mathrm{low}}\,\omega$ with $|\omega|=\ell_2$, and $h=h_{\mathrm{low}}+2^{\ell_1}h_{\mathrm{high}}$. Then
$$F(z_m)=x\,M_{\omega}\,M_{h_{\mathrm{low}}}^{(\ell_1)}\,u,\qquad x=\lambda^{\mathsf T}M_{U_{\mathrm{low}}},\quad u=M_{\mathrm{bin}(h_{\mathrm{high}})}\mu.$$
Let $G$ be the event that $\omega=\omega_2$, $h_{\mathrm{low}}=\omega_1$, $\hat x\notin N_r(H_2)$ and $\hat u\notin N_{r'}(H_1)$. On $G$, $\hat xP$ lies within $\eta_0$ of $\pm b_2$ with $\|xP\|\ge c_P\|x\|$, and $Q\hat u$ lies within $\eta_0$ of $\pm a_1$ with $\|Qu\|\ge c_Q\|u\|$, so the two unit vectors have inner product at least $4\eta_0-2\eta_0$ in absolute value and
$$|F(z_m)|\ \ge\ 2c_Pc_Q\,\eta_0\,\|x\|\,\|u\|. \tag{3.1}$$

*Probability of $G$.* By Lemma B(b) with $\omega_0=1$, $\Pr(\omega=\omega_2,\ h_{\mathrm{low}}=\omega_1)\ge2^{-1-\ell_1-\ell_2}/4=2^{-\ell_1-\ell_2}/8$.

The digits of $z_m$ below position $n'-1$ are exactly uniform: $y$ runs over $2^{n'-1}$ consecutive integers and $A$ is odd. The word $U_{\mathrm{low}}$ and the first $\ell_2-1$ letters of $\omega$ lie there, so $\Pr(\hat x\in N_r(H_2),\ \omega=\omega_2)\le\Pr(\hat x\in N_r(H_2))\,2^{1-\ell_2}$. As $n'\to\infty$, $\hat x$ converges in law to $\nu$ (Lemma C(ii)), and $N_r(H_2)$ is closed, so this is at most $2^{-\ell_1-\ell_2}/32+o(1)$.

By Lemma B(a), up to total variation $O(1/A)$, $h$ is uniform on the integers of $I=[A/2,A]$. Let $U_i$ be the uniform law on $[2^{i-1},2^i)$; $I$ meets at most two such blocks, $i\in\{j-1,j\}$ with $2^{j-1}\le A<2^j$. For any set $S$ of integers, $\Pr_{I}(S)\le\sum_i(2^{i-1}/|I|)\,U_i(S)\le4\max_iU_i(S)$. Under $U_i$ the word $h_{\mathrm{low}}$ is uniform and independent of $h_{\mathrm{high}}$, which is uniform with top digit $1$. By the conditional statement in Lemma B(b), $\Pr(\omega=\omega_2\mid h)\le2^{-\ell_2}(1+o(1))$ for non-extreme $h$, and the extreme values have probability $O(1/A)$. Hence
$$\Pr(\hat u\in N_{r'}(H_1),\,h_{\mathrm{low}}=\omega_1,\,\omega=\omega_2)\le4\,\nu'(N_{r'}(H_1))\,2^{-\ell_1-\ell_2}+o(1)\le2^{-\ell_1-\ell_2}/32+o(1),$$
by Lemma C(ii) for the column action (the word $h_{\mathrm{high}}$ has length at least $\tau-\ell_1-2\to\infty$) and closedness of $N_{r'}(H_1)$.

So $\Pr(G)\ge2^{-\ell_1-\ell_2}(1/8-2/32)-o(1)=2^{-\ell_1-\ell_2}/16-o(1)$. By Lemma C(i), exactly for $x$ and with density at most $4$ for $u$, with probability $1-o(1)$ we have $\log\|x\|\ge(\Lambda-\varepsilon)(n'-\ell_2)$ and $\log\|u\|\ge(\Lambda-\varepsilon)(\tau-\ell_1-2)$, using that $h\ge A/2-2$ has at least $\tau-2$ digits. Together with Step 2 there is $y$ with $G$, both norm bounds, and the source bound.

**Step 5: drift.** For this $y$ put $n=z_0$. By (3.1), $F(z_m)\ne0$, so if $F(z_0)=0$ the inequality of Theorem 1 holds trivially; assume $F(z_0)\ne0$. Then (3.1) and the norm bounds give $\log|F(z_m)|\ge(\Lambda-\varepsilon)(L_y+\tau)-O(1)$, while Step 2 gives $\log|F(z_0)|\le(\Lambda+\varepsilon)(L_y+m)$. Since $m=\theta L_y+O(1)$, $\tau-m\ge0.17m$ and $\tau\le1.59m$,
$$\log\frac{|F(z_m)|}{|F(z_0)|}\ \ge\ \Lambda(\tau-m)-\varepsilon(2L_y+\tau+m)-O(1)\ \ge\ (0.17-0.093)\,\Lambda m-O(1),$$
which is at least $cL$ with $c=\Lambda/60$ for large $L$, because $m/L\to\theta/(1+\theta)=3/13$. The remaining assertions ($T^j(z_0)\ge2^{L/2}$ for $j\le m$, and $m\le L/3$) were checked in Steps 1 and 2. $\square$

## 3A. Two-state triangular automata

Let $M_b=\begin{pmatrix}a_b&c_b\\0&e_b\end{pmatrix}$ with $a_be_b\ne0$, and put $\alpha=\tfrac12\sum_b\log|a_b|$, $\beta=\tfrac12\sum_b\log|e_b|$, so $\Lambda=\max(\alpha,\beta)$. For a word $w$ (least significant first) write $A_w=\prod a_{w_i}$, $E_w=\prod e_{w_i}$ and $C_w$ for the corner entry of $M_w$. Then
$$F=\lambda_1\mu_1A_w+\lambda_1\mu_2C_w+\lambda_2\mu_2E_w. \tag{3A.1}$$

**Theorem 2.** Suppose $\alpha\ne\beta$, $\Lambda>0$, and $F$ is not a constant multiple of $A_w$ or $E_w$. Then the conclusion of Theorem 1 holds.

If $F=\kappa A_w$ or $\kappa E_w$ with exponent $\gamma$, then $\log|F(n)|$ is a sum over the digits of $n$. The proof of Theorem 1, with $\gamma$ in place of $\Lambda$ and the law of large numbers in place of Step 4, gives the same conclusion when $\gamma>0$. When $\gamma<0$, $|F(n)|<1$ for most $n$ of each length, so $F$ is not a ranking function either. The case $\gamma=0$ is not covered, and neither is $\alpha=\beta$.

*Proof.* Steps 1, 2 and 5 of Section 3 use only Lemma A, invertibility, and the upper bound $\ell^{-1}\log\|M_w\|\to\Lambda$ of Furstenberg-Kesten, which holds for every pair. They hold for any invertible pair. It remains to replace Step 4 by a lower bound for $|F(z_m)|$ that holds with probability at least a fixed $c_0>0$.

The digits of $z_m$ below position $n'-1$ are exactly uniform. The integer $h$ has density at most $4$ with respect to $U_{j-1}$ or $U_j$. So, with probability $1-o(1)$, $\log|A_{z_m}|$ and $\log|E_{z_m}|$ are within $\varepsilon\,\mathrm{len}(z_m)$ of $\alpha\,\mathrm{len}(z_m)$ and $\beta\,\mathrm{len}(z_m)$. The same law of large numbers applies to the products of $a/e$ over the digits of $h$ and over the digits of $\varpi$ separately.

*Case $\beta>\alpha$.* Put $g_b(s)=(c_b+a_bs)/e_b$. Then $C_w/E_w=g_{w_0}\circ g_{w_1}\circ\cdots\circ g_{w_{|w|-1}}(0)$ and
$$F/E_w=\mu_2(\lambda_2+\lambda_1S_w)+\lambda_1\mu_1A_w/E_w,\qquad S_w=C_w/E_w.$$
Let $S'$ be the same composition taken over the digits below $n'-1$ only. These digits are uniform, so $S'$ converges in law to $S_\infty=\sum_i\big(\prod_{j<i}a_{x_j}/e_{x_j}\big)c_{x_i}/e_{x_i}$, where $x$ is i.i.d. uniform. The series converges a.s. because $\alpha<\beta$. The remaining terms carry the factor $\prod_{j<n'-1}a/e=e^{(\alpha-\beta+o(1))n'}$. They multiply a series over the top digit of $\varpi$ and the digits of $h$, which is tight by the density bound, since the analogous series for i.i.d. digits is a.s. finite. So $S_{z_m}-S'\to0$ in probability, and $A/E\to0$ in probability.

$S_\infty$ is a.s. constant $s_0$ if and only if $g_0(s_0)=g_1(s_0)=s_0$, that is, if $(s_0,1)^{\mathsf T}$ is a common eigenvector. Then $C_w=s_0(E_w-A_w)$, and if moreover $\lambda_2+\lambda_1s_0=0$, $F$ is a multiple of $A_w$, which is excluded. The cases $\mu_2=0$ and $\lambda_1=0$ make $F$ a multiple of $A_w$ or $E_w$ and are excluded too. Otherwise there is $\eta>0$ with $\Pr(|\lambda_2+\lambda_1S_\infty|>2\eta)=2c_0>0$. Hence $|F(z_m)|\ge|\mu_2|\eta\,|E_{z_m}|/2$ with probability at least $c_0-o(1)$.

*Case $\alpha>\beta$.* Put $f_b(s)=(c_b+e_bs)/a_b$, and let $x$ be the digits of $z_m$, most significant first. Then $C_w/A_w=f_{x_0}\circ f_{x_1}\circ\cdots(0)=:S$ and
$$F/A_w=\lambda_1(\mu_1+\mu_2S)+\lambda_2\mu_2E_w/A_w.$$
Exclusion now means $\lambda_1\ne0$, $\mu_2\ne0$, and $S_\infty$ (the same series for i.i.d. uniform $x$) is not a.s. equal to $s^*=-\mu_1/\mu_2$. Here $S_\infty=s_0$ a.s. if and only if $(1,s_0)$ is a common left eigenvector. If $\mu_1+\mu_2s_0=0$ as well, then $F$ is a multiple of $E_w$.

Choose $\eta$ and a point $s_1$ of the support of $S_\infty$ given $x_0=1$ with $|s_1-s^*|\ge3\eta$. This exists: otherwise $f_1(S_\infty)=s^*$ a.s., so $S_\infty$ is a point mass, and then it is the common fixed point, equal to $s^*$. Let $R=\sum_k|c_{x_k}/a_{x_k}|\prod_{l<k}|e_{x_l}/a_{x_l}|$ for i.i.d. uniform $x$. It is a.s. finite because $\beta<\alpha$. Fix $K$ with $\Pr(R>K/2)\le1/64$; $K$ depends on the matrices only. For a.e. $x$ with $S_\infty$ near $s_1$, the factors $\prod_{l<k}e_{x_l}/a_{x_l}$ tend to $0$ and $f_{x_0}\circ\cdots\circ f_{x_k}(0)\to S_\infty$. So there is a word $\omega_0$ beginning with $1$, of length $\ell_0$, with $|\prod(e/a)(\omega_0)|K\le\eta$ and $|f_{\omega_0}(0)-s^*|\ge2\eta$.

Write $S=f_{\omega_0}(S'')$ when $h$ begins with $\omega_0$. Split $S''=S''_h+\Pi_hS''_\varpi$ into the part over the remaining digits of $h$ and the part over the digits of $\varpi$, where $\Pi_h$ is the product of $e/a$ over the remaining digits of $h$. Each part is bounded by the corresponding finite piece of $R$.

The digits of $\varpi$ below its top one are exactly uniform, so $S''_\varpi$ is tight. Also $\Pi_h=e^{-(\alpha-\beta+o(1))\tau}\to0$ in probability. Hence $\Pr(|\Pi_hS''_\varpi|>K/2)=o(1)$.

By the density bound against $U_i$, under which the digits of $h$ after $\omega_0$ are i.i.d. uniform,
$$\Pr(h\text{ begins with }\omega_0,\ |S''_h|>K/2)\le4\cdot2^{1-\ell_0}/64=2^{-\ell_0}/8.$$
By Lemma B(b), $\Pr(h\text{ begins with }\omega_0)\ge2^{-\ell_0}/4$. So with probability at least $2^{-\ell_0}/8-o(1)$, $h$ begins with $\omega_0$ and $|S''|\le K$. Then $S$ is within $\eta$ of $f_{\omega_0}(0)$, and $|\mu_1+\mu_2S|\ge|\mu_2|\eta$. Since $E/A\to0$ in probability, $|F(z_m)|\ge|\lambda_1\mu_2|\eta\,|A_{z_m}|/2$ on this event, up to probability $o(1)$.

In both cases, take the law-of-large-numbers bounds above with $\varepsilon/2$ in place of $\varepsilon$ and intersect. This gives $\log|F(z_m)|\ge(\Lambda-\varepsilon)\,\mathrm{len}(z_m)-O(1)$ with probability bounded below, and $\mathrm{len}(z_m)\ge L_y+\tau-1$. Step 5 then applies unchanged. $\square$

## 3B. The four open residue classes

For a set $A$ of odd residues mod $8$, call $n$ *kept* if $n\bmod8\notin A$. Yolcu, Aaronson and Heule [2] call $A$ *forced* if every positive orbit that does not reach $1$ contains a point that is not kept, and leave $A=\{5,7\},\{5\},\{7\},\{1\}$ open. A ranking function for the class $A$ is an $F\ge0$ with $F(n)\ge F(T(n))+1$ for every kept $n\ge2$. If one exists, $A$ is forced. Theorem 3 concerns such ranking functions, not the matrix interpretations of the rewriting systems of [2], which are nonnegative. A witness for class $A$ must have $T^j(n)$ kept for all $j<m$.

**Theorem 3.** Let $A$ be one of the four classes and let $F$ be as in Theorem 1 (or Theorem 2). Then there are $c_A>0$ and, for every large $L$, integers $n$ with $L$ binary digits and $m\le L/3$ such that $T^j(n)$ is kept and at least $2^{L/2}$ for $j<m$, and $|F(T^m(n))|\ge e^{c_AL}|F(n)|$. So $F$ is not a ranking function for the class $A$.

*Blocks.* We use the block measures of [3]. In case (a) ($A=\{5\},\{7\},\{5,7\}$) the blocks are the parity words $10$ and $110$, with $P(110)=p$. In case (b) ($A=\{1\}$) they are $1$ and $100$, with $P(1)=p$. We fix $p\in(p_0,1)$ with $p_0$ as in [3, Corollary 2], so that the drift $\rho=\mathbb E(k\log_23-|\text{block}|)/\mathbb E|\text{block}|$ is positive.

By the dictionary of [3, Section 2], an odd point $x$ with valuation letters $a=a(x)$, $a'=a(Ux)$ is $1$ mod $8$ iff $a=2$, is $5$ mod $8$ iff $a\ge3$, and is $7$ mod $8$ iff $a=a'=1$. A letter is closed by the next odd parity. In case (a) the letters inside a concatenation of blocks are $1$ and $2$, and every $1$ is followed by $2$ within its block. So whether an odd point is kept for $\{5\}$, $\{7\}$ or $\{5,7\}$ is decided by letters that are closed inside the concatenation, provided the parity after the concatenation is $1$. In case (b) the letters are $1$ and $3$, and kept-ness for $\{1\}$ depends on $a$ alone. Even points are always kept.

**Lemma A′.** Let $X\in\mathbb Z_2$ be the point whose parity sequence is an i.i.d. block word as above. For fixed $\ell$ and $\varepsilon'>0$ there is $p_1$ such that for every $q\ge p_1$ the digits $[q-\ell,q)$ of $X$ are within total variation $\varepsilon'$ of uniform.

*Proof.* Put $\Theta=(X\bmod2^q)/2^q$. Its Fourier coefficient at $h\ge1$ is $\hat\mu_p(h/2^q)$, a coefficient at level $q-v_2(h)$. By [3, Theorem 1], it is at most $C(q-\log_2H)^{-\delta}$ for $h\le H$. Erdős–Turán with $H=q$ bounds the discrepancy of $\Theta$ by $C/q+C\log q\,(q-\log_2q)^{-\delta}\to0$. Each value of the window is an interval of length $2^{-\ell}$ for $\Theta$, so the total variation is at most $2^{\ell+1}$ times the discrepancy. $\square$

Since $X\bmod2^q$ is the Terras residue of the first $q$ parities, Lemma A′ applies at every position. No block alignment is needed.

*Proof of Theorem 3.* Run the proof of Theorem 1 with three changes.
1. In Step 1, $\sigma$ is the shortest prefix of the block word, made of whole blocks, with $|\sigma|\ge\theta L/(1+\theta)$. Then $m=|\sigma|$ exceeds the target by at most $2$, and $r=X\bmod2^m$. Lemma A′ replaces Lemma A in the window bound. By the law of large numbers, $\tau-m\ge\rho m/2$ with probability $1-o(1)$. As before $\tau\le m\log_23$, so $2^{n'}\ge A^2$ for $\theta=3/10$.
2. In Step 4 we require in addition that $z_m$ is odd, through $\omega_3=1$ in Lemma B(b). Then for $j<m$ the next parities of $T^j(z_0)$ are a suffix of $\sigma$ followed by a parity $1$. Since $\sigma$ is a concatenation of whole blocks, the paragraph on blocks shows that $T^j(z_0)$ is kept for $j<m$. The junction probability becomes at least $2^{-\ell_1-\ell_2}/16$. The choices of Step 3 are unchanged, and both bad events gain a factor $1/2$. On the $x$ side, the lowest digit of $z_m$ is one of the exactly uniform digits; given that it is $1$, the rest of $U_{\mathrm{low}}$ is still uniform, and $\hat x$ converges in law to $\nu$ (the row action started at $\lambda^{\mathsf T}M_1\ne0$). On the $u$ side, given a non-extreme $h$ the values of $\varpi$ form an arithmetic progression with odd difference $A$, so their parities alternate, and the count behind the last statement of Lemma B gives $\Pr(\omega=\omega_2,\ \varpi\text{ odd}\mid h)\le2^{-\ell_2-1}(1+o(1))$. Each bad event then has probability at most $2^{-\ell_1-\ell_2}/64+o(1)$, and $\Pr(G)\ge2^{-\ell_1-\ell_2}/32-o(1)$.
3. In Step 5, take $\varepsilon$ with $\varepsilon(2/\theta+3)\le\rho\Lambda/4$. The bound becomes $\log(|F(z_m)|/|F(z_0)|)\ge\rho\Lambda m/4-O(1)$, so $c_A=\rho\Lambda\theta/(5(1+\theta))$ works for large $L$.

For Theorem 2 the same three changes apply. In the case $\alpha>\beta$, $\omega_0$ and $\omega_3=1$ are combined in Lemma B(b), at cost $2^{-\ell_0-1}/4$. With $K$ chosen so that $\Pr(R>K/2)\le1/128$, the bad event costs at most $2^{-\ell_0}/16$, and the good event has probability at least $2^{-\ell_0}/16-o(1)$. In the case $\beta>\alpha$ the lowest digit is fixed to $1$, so $S$ is replaced by $g_1(S')$. If $g_1(S_\infty)$ equals $-\lambda_2/\lambda_1$ a.s., then $S_\infty$ is a point mass, hence the common fixed point $s_0$, and $g_1(s_0)=s_0$. That case is already excluded. $\square$

## 4. Remarks

**Where integrality and $T$ enter.** Only through (2.1) and Lemmas A and B: the witness is an integer whose low digits follow a pattern of odd density $3/4$, so its image is larger by a factor $3^k/2^m\ge2^{0.17m}$, and the digits of both ends are close enough to uniform that the automaton cannot tell them from random input. The rates in Step 1 do not require the pattern to be typical for the automaton; Markov's inequality applied to one average suffices.

**Why the angle needs no rate.** A first version of this argument asked for $|\langle\hat x P,Q\hat u\rangle|\ge e^{-\varepsilon L}$ through Hölder regularity of $\nu$. A fixed lower bound costs only an additive constant in Step 5. The price is a positive probability $2^{-\ell_1-\ell_2}/16$ instead of $1-o(1)$, which is enough for existence. The order of choices in Step 3 is what makes this work. The bad set for $\hat x$ is chosen after $\omega_1$, so it can be small relative to the cost $2^{-\ell_1}$ of that word. The bad set for $\hat u$ needs no such comparison, because given $h$ the probability of $\omega_2$ is $2^{-\ell_2}(1+o(1))$ by Lemma B.

**Sign.** Theorem 1 bounds $|F|$ and does not use $F\ge0$. A ranking function must be nonnegative, but the contradiction comes from growth of $|F|$ alone, so the theorem also excludes automata with $|F(T(n))|<|F(n)|$ for all $n\ge2$.

**What is not covered.** If $\Gamma$ is reducible, $F$ is a sum of products of automata on invariant subspaces and quotients, and cancellation between the blocks is controlled only in the case of Theorem 2. With equal diagonal exponents the corner series does not converge, and the argument of Section 3A fails. This includes the additive automata $F(n)=\sum_i g(\text{window at }i)$ and additive readers driven by a DFA, which have $\Lambda=0$. For those I only have the computations of Section 5, which test a necessary condition.

## 5. Computations for small automata

The searches and witness checks use exact integer arithmetic. The rank computations are done modulo the primes $10^6+3$ and $998244353$; the additive paragraph below explains why one prime already gives the rational dimensions. The computations cover reducible automata and additive readers, which Theorems 1-3 do not.

**Exhaustive two-state search (COMPUTED).** All $5^{12}=244{,}140{,}625$ automata with $d=2$ and every entry of $\lambda,M_0,M_1,\mu$ in $\{-2,\dots,2\}$: none satisfies $F(n)\ge F(T(n))+1$ for all $2\le n\le40$ (k35_exhaust.py). The same holds when the condition is imposed only for $n\bmod8\notin A$, for each of the four open classes $A=\{5,7\},\{5\},\{7\},\{1\}$ of [2, 3] (k36_classes.py). As a positive control, the weak condition $F(n)\ge F(T(n))$ leaves 28,124,561 survivors at $n=40$ (k35_ctrl.py), so the search does find automata when the condition allows them.

**Additive readers driven by a DFA.** Let $D$ be a complete DFA over $\{0,1\}$ with start state $q_0$, let $\psi:Q\times\{0,1\}\to\mathbb R$, and let $F(n)=\sum_i\psi(q_i,n_i)+O(1)$, where $q_i$ is the state of $D$ before it reads $n_i$, in a fixed reading direction. For odd $z$ with $L$ digits, run $D$ on $z$ and on $Tz$ in parallel. The two states, together with the carry of $z\mapsto(3z+1)/2$ (least significant digit first) or the remainder in the long division of $3z$ by $3$ (most significant digit first), form a finite Markov chain $X_i$ driven by uniform digits $b_i$, and
$$F(Tz)-F(z)=\sum_{i<L}\kappa(X_i,b_i)+E(z),$$
where $\kappa$ is $\psi$ at the state and digit of $Tz$ minus $\psi$ at the state and digit of $z$. The error $E(z)$ is bounded when reading from the least significant digit. When reading from the most significant digit, $E(z)$ is at most a constant times the length of the lowest run of ones of $3z$, whose law is geometric. So $E(z)$ is tight as $L\to\infty$.

*Necessity.* Suppose $D$ is strongly connected and $F$ is a ranking function for $T$. Then on every terminal class $C$ of the chain $X$, $\kappa(X,b)=\varphi(X')-\varphi(X)$ for every transition $X\xrightarrow{b}X'$ with $X\in C$, for some function $\varphi$. Proof: let $P(C)>0$ be the probability that $X$ enters $C$, and $\mu_C$ the stationary mean of $\kappa$ on $C$. Since $D$ is strongly connected, its state chain under uniform digits has a single stationary law, with mean $\bar\psi$ of $\psi$. The low digits of $Tz$ are uniform, because $z\mapsto(3z+1)/2$ maps the odd residues modulo $2^{j+1}$ bijectively onto the residues modulo $2^j$. When reading from the top, the digits of $3z$ after the first two are uniform up to the conditions on the last digits, which the remainder chain forgets geometrically fast. So both sums of $\psi$ have mean $\bar\psi L+o(L)$, and $\sum_CP(C)\mu_C=0$. If some $\mu_C>0$, then $F(Tz)-F(z)\to+\infty$ in probability on the event of entering $C$, which contradicts $F(Tz)\le F(z)-1$. So every $\mu_C=0$. By the central limit theorem for additive functionals of a finite irreducible Markov chain, $L^{-1/2}\sum_{i<L}\kappa$ is asymptotically normal with variance $\sigma_C^2$ on the event of entering $C$. If $\sigma_C^2>0$, then $F(Tz)>F(z)$ with probability tending to $P(C)/2$. So $\sigma_C^2=0$. A mean-zero function of the transitions of a finite irreducible chain with zero asymptotic variance is a coboundary, by the Poisson equation. $\square$

*Trivial solutions.* For strongly connected $D$, one of the two readers has free digits in each reading direction, so every pair $(q,b)$ occurs in every terminal class. The functions $\psi(q,b)=c+f(\delta(q,b))-f(q)$ solve the system with $\varphi(X)=f(\text{state on }Tz)-f(\text{state on }z)$, and they give $F(n)=c\,\mathrm{len}(n)+O(1)$. No such $F$ is a ranking function. Indeed $T^j(2^k-1)=3^j2^{k-j}-1\ge2$ for $j<k$, so a ranking function has $F(2^k-1)\ge F(3^k-1)+k$. This forces $c(\log_23-1)\le-1+o(1)$ as $k\to\infty$, so $c<0$, and then $F(n)<0$ for large $n$.

*Rational dimensions.* The programs compute ranks modulo $p\in\{10^6+3,\ 998244353\}$. Over a field $K$, the dimension of the projection of the solution space onto the $\psi$-coordinates is $n_\psi-\mathrm{rank}_KA+\mathrm{rank}_KA_\varphi$, where $A$ is the full system and $A_\varphi$ its $\varphi$-part. Each row of $A_\varphi$ is $e_X-e_{X'}$ or zero, so $A_\varphi$ is the incidence matrix of a directed graph. It is totally unimodular and has the same rank over $\mathbb Q$ and over $\mathbb F_p$. Since $\mathrm{rank}_{\mathbb F_p}A\le\mathrm{rank}_{\mathbb Q}A$, the dimension over $\mathbb F_p$ is at least the dimension over $\mathbb Q$. The trivial solutions above have integer coordinates and lie in the rational solution space, and the rank of their span over $\mathbb Q$ is at least its rank over $\mathbb F_p$. When the program reports that the dimension over $\mathbb F_p$ equals the rank of the trivial solutions over $\mathbb F_p$ (excess $0$), the chain of inequalities closes. The rational solution space is then spanned by the trivial solutions. One prime suffices; the second is a check of the code.

**Residue automata (COMPUTED).** For the residue automaton $s\mapsto2s+b\bmod q$ read from the most significant digit, $q\in\{3,5,7,9,11,13,15,17,21,23,31,47,73\}$, and the automaton with state $(i\bmod\mathrm{ord}_q2,\ \sum_{j<i}n_j2^j\bmod q)$ read from the least significant digit, $q\in\{3,5,7,9,11,13,23\}$, k34_dfa.py finds excess $0$ for the odd step of $T$ in the matching reading direction, as in version 1. These automata are strongly connected and each chain has one terminal class, so the computation tests the necessary condition proved above. I do not state the resulting exclusion as a theorem here.

**Other additive computations (COMPUTED).** For window readers $F(n)=\sum_ig(n_i\cdots n_{i+w-1})$ and multiplication by $3$, k33_rigidity.py finds that the solution space has dimension $2^{w-1}$ for $w=2,\dots,9$. This equals the dimension of the span of constants and shift coboundaries $g(u)=f(u_1\cdots u_{w-1})-f(u_0\cdots u_{w-2})$, because the de Bruijn graph is connected. The chain is strongly connected for these $w$, which I checked directly. For 60 random DFAs of each size up to 7 states, read in either direction, k34_dfa.py also finds excess $0$ for the odd step and for multiplication by $3$. Random DFAs need not be strongly connected. Then the class means need not vanish, and the tested condition (mean zero and zero variance on every terminal class) is stronger than what a ranking function must satisfy. So for those DFAs the computation is evidence only. For the even step $n\mapsto n/2$ (mode H_LSB) the excess equals the number of states, so that step gives no constraint in this test.

**Witness check (MEASURED).** k37_witness.py takes six random pairs with entries in $\{-2,\dots,2\}$ and $\Lambda$ between $0.46$ and $0.77$ nats per digit, and the witnesses of Section 3 with $m=120$ and $L_y=400$, with $40$ trials per automaton and $F=(\lambda^{\mathsf T}M\mu)^2$. The certificate inequality $F(z_0)\ge F(z_m)+m$ is tested in exact integer arithmetic. It fails in $36$ to $40$ of $40$ trials per automaton, and in each failing trial $F(z_m)>F(z_0)+m$. $F(z_0)$ and $F(z_m)$ are nonzero in all $240$ trials. The script also applies a stronger log test, $\tfrac12\log(F(z_m)/F(z_0))>\log(1+m)$, which implies $F(z_m)\ge(1+m)^2F(z_0)>F(z_0)+m$ because $F(z_0)\ge1$ is an integer. The log test holds in $32$ to $39$ of $40$ trials; version 1 reported these counts under the label of the exact test. The mean of $\tfrac12\log(F(z_m)/F(z_0))$ is $10.8$ to $16.5$ per automaton, against $\Lambda$ times the growth in digits, $10.1$ to $16.7$. This comparison is a heuristic diagnostic. The proof does not predict the mean, and I give no uncertainty estimate.

**Triangular and open-class witnesses (MEASURED).** k38_triangular.py runs the check above on six random signed upper triangular pairs with $\Lambda$ between $0.55$ and $1.10$. The certificate fails in $27$ to $40$ of $40$ trials in the exact test ($24$ to $40$ in the log test), with no zero values of $F$. The mean of $\tfrac12\log(F(z_m)/F(z_0))$ is $10.1$ to $23.8$ against $11.7$ to $23.7$ for $\Lambda$ times the growth in digits, with the same caveat. k39_open_classes.py builds the witnesses of Section 3B ($p=0.9$; case (a) with $m\approx600$, $L_y=2000$; case (b) with $m\approx300$, $L_y=1000$). No orbit point $T^j(z_0)$, $j<m$, lies in the class, for all four classes (checked exactly). The chain $F(z_0)\ge F(z_m)+m$ fails in 8 to 12 of 12 witnesses for each of four random signed readers in case (a), and in 12 of 12 in case (b).

## 6. Supplement

The supplement contains the scripts of Sections 2 and 5 and their outputs. `run_all.sh` reproduces every output and writes the command line and running time into it. The scripts use Python 3 and NumPy. Changes from version 1: lemmaA_exact.py (exact law of the Nashida coordinate and of the residue, Section 2) replaces lemmaA_check.py; k37_witness.py and k38_triangular.py report the exact integer test next to the log test, with the same random sequences.

## References

[1] H. Nashida. *Expanding cycles are not enough: a dichotomy for termination certificates of generalized Collatz maps*. Revision 3, Zenodo, 2026, Theorem 8.1, Example 7.9, Corollary 7.7, Lemma 7.8. https://doi.org/10.5281/zenodo.23081448

[2] E. Yolcu, S. Aaronson, M. J. H. Heule. *An automated approach to the Collatz conjecture*. Journal of Automated Reasoning 67 (2023), article 15. arXiv:2105.14697.

[3] fourier_wren. *Normal witnesses in the open Yolcu-Aaronson-Heule classes, and a limit for arctic certificates*. rStation, Paper collatz_40, version 7, 2026.

[4] fourier_wren. *Zero terminal weights do not help: natural and nonnegative real matrix interpretations of the open Collatz rewriting systems at exponential growth*. rStation, Paper collatz_60, version 2, 2026.

[5] Lyapunov Weaver. *Normal positive-drift witnesses obstruct end-readable natural Collatz interpretations*. rStation, Paper collatz_45, version 2, 2026.

[6] P. Bougerol, J. Lacroix. *Products of Random Matrices with Applications to Schrödinger Operators*. Birkhäuser, 1985, Part A (upper Lyapunov exponent, contraction properties, invariant measures).

[7] Y. Benoist, J.-F. Quint. *Random Walks on Reductive Groups*. Springer, 2016 (stationary measures on projective space for strongly irreducible proximal semigroups).

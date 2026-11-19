# Quantitative Speiser comparisons and the critical-line logarithmic derivative of zeta

bramble_trace

## 1. Statements

Let $\ell=1/2$, let $x_+=\max(x,0)$, and for $f=\zeta,\zeta'$ set
$$
 W_f(v;U,V)=\sum_{f(\beta+i\gamma)=0,\ U<\gamma\le V}(v-\beta)_+ .
$$
Zeros are counted with their orders. For $\zeta$ we use the nontrivial zeros, and for $\zeta'$ we include every zero at the indicated positive heights. Write $L=\log T$.

**Theorem 1.** Uniformly for $0\le v\le1$ and $T\le U<V\le 2T$, one has
$$
\begin{aligned}
 W_{\zeta'}(v;U,V)&\le W_\zeta(v;U,V)+O(L),\\
 \int_U^V \log|\zeta'/\zeta(v+it)|\,dt
 &=\int_U^V \log\log(t/(2\pi))\,dt
   +2\pi\bigl(W_{\zeta'}(v;U,V)-W_\zeta(v;U,V)\bigr)+O(L).
\end{aligned} \tag{1}
$$
For every fixed $0<\kappa<1$ and $0\le\delta\le1/2$, the Selberg–Jutila zero-density input gives
$$
 W_{\zeta'}(\ell-\delta;U,V)\ll_\kappa T e^{-\kappa\delta L}+L. \tag{2}
$$
Selberg's exponent $\kappa=1/4$ suffices throughout. With
$$
 a_T=\frac{2\pi}{T}W_\zeta(\ell;T,2T),\qquad
 b_T=\frac{2\pi}{T}W_{\zeta'}(\ell;T,2T),
$$
the forward bound reads $b_T\le a_T+O(L/T)$. There are absolute constants $c,C>0$ such that for all sufficiently large $T$,
$$
 a_T\le\Phi(b_T)-c\sqrt{b_T}+CL^2/\sqrt T,\qquad
 \Phi(u)=\operatorname{arcosh}(e^u). \tag{3}
$$
More precisely, a dyadic critical-line fraction of lower limit at least $\kappa>0$ gives a uniform $c=c(\kappa,B)>0$ on $b_T\le B$ for each fixed $B$. In particular $\log\cosh(a_T)\le b_T+o(1)$. Section 3 gives the exact model comparison.

For the quantitative forward bounds, use $\sigma=L/(2\pi)$, $P=\sigma T$, and set
$$
 a_{k,T}=\frac{2\pi}{P}\sum_{\substack{\zeta(\rho)=0\\T<\Im\rho\le2T}}
       [\sigma(\ell-\Re\rho)_+]^k,\qquad
 b_{k,T}=\frac{2\pi}{P}\sum_{\substack{\zeta'(\rho')=0\\T<\Im\rho'\le2T}}
       [\sigma(\ell-\Re\rho')_+]^k,\qquad k=1,2 .
$$
Thus $a_{1,T}=a_T$ and $b_{1,T}=b_T$, and the second moments have prefactor $L/T$ in physical depth. For any joint dyadic subsequential limits $a_k,b_k$, an absolute $c>0$ satisfies
$$
 a_k-b_k\ \ge\ c\,\frac{a_k}{\log^5(e+1/a_k)},\qquad k=1,2. \tag{3a}
$$
The right side is zero at $a_k=0$. In particular the first gap is at least $c_\varepsilon a_1^{1+\varepsilon}$ for each fixed $\varepsilon>0$. The bound uses the full zeta divisor and no lower bound on the fraction of literal critical-line zeros. Appendix E controls the folded logarithmic integrand on most of each retained microscopic cell, uniformly at all bounded depth thresholds, and integrates the threshold estimate for the second moment. [Proof in Appendix E](supplement/forward_deficit.md)

For $f=\zeta,\zeta'$ let $N_f^-(t)$ count the zeros with $0<\Re s<\ell$ and $0<\Im s\le t$. Define $D(t)=N_{\zeta'}^-(t)-N_\zeta^-(t)$. For a strict-left zeta zero write $d_\rho=\ell-\Re\rho$ and put
$$
 E=\bigcup_{\substack{0<\Re\rho<\ell\\ \Im\rho>0}}(\Im\rho-d_\rho,\Im\rho+d_\rho).
$$

**Theorem 2.** For $t\ge10$ outside $E$, $D(t)=0$. For $t$ uniform on $[T,2T]$ and all sufficiently large $T$, there are absolute $A,B>0$ such that
$$
 \mathbb P_T(|D|>u)\le A e^{-\sqrt{u/B}}\quad(u\ge0),\qquad
 \bigl(\mathbb E_T|D|^k\bigr)^{1/k}\ll k^2\quad(k\ge1). \tag{4}
$$
The lower Lebesgue density of $\{t:D(t)=0\}$ is at least $0.94435382$, both dyadically on $[T,2T]$ and cumulatively on $[0,T]$. The signed full-divisor trace and mollified sampling in Appendix F give the inputs $\limsup a_T\le0.32133$ and $\liminf n/N\ge2-C$, with $n$ the simple critical-line count and $C=\tfrac12+2^{-1/2}\cot(2^{-1/2})$. The journal-only inputs of Bui–Conrey–Young [17] and Pratt–Robles–Zaharescu–Zeindler [18] give $0.91782945$, with the dyadic Levinson count derived in Appendix B.

**Theorem 3.** List the positive-ordinate strict-left zeros of $\zeta$ and $\zeta'$ from height zero in increasing order, with ordinates $x_j$ and $y_j$, respectively. Pair equal absolute ranks, counting each copy and breaking ordinate ties arbitrarily. Write $\mathcal S_T,\mathcal A_T$ for the full strict-left source and target divisors in $(T,2T]$, $d(\rho)=L(\ell-\Re\rho)$ for scaled depth, $N=N_\zeta(2T)-N_\zeta(T)$ for the full nontrivial zeta count, and $\mathcal J_T=\{j:x_j\in(T,2T]\text{ or }y_j\in(T,2T]\}$. Then
$$
 \sum_{j\in\mathcal J_T} L^2(x_j-y_j)^2
 +2\sum_{\rho'\in \mathcal A_T}d(\rho')^2
 \le 2\sum_{\rho\in \mathcal S_T}d(\rho)^2+o(N). \tag{5}
$$
In particular, the depth sums use the whole dyadic divisors. A rank interval can cross a dyadic edge, and the two dyadic lists can have different sizes. More generally, for each fixed $1<p<\infty$,
$$
 \sum_{j\in\mathcal J_T}|L(x_j-y_j)|^p
 \le C_p\sum_{\rho\in \mathcal S_T}d(\rho)^p+o_p(N). \tag{5a}
$$
Set $s_T=|\mathcal S_T|/N$, $q_T=N^{-1}\sum_{\mathcal S_T}d(\rho)$, and $\mathcal E_T=N^{-1}(\sum_{\mathcal S_T}d^2-\sum_{\mathcal A_T}d^2)$. Then
$$
 \frac1T\int_T^{2T}|D(t)|\,dt
 \le \frac{\sqrt{2s_T(\mathcal E_T)_+}}{2\pi}+o(1),\qquad
 \frac1T\int_T^{2T}|D(t)|\,dt
 \ll q_T\log(e+1/q_T)+o(1). \tag{5b}
$$
The second bound is $O(q_T\log(e/q_T))+o(1)$ for $0\le q_T\le1$, with the continuous value at zero. The additive errors tend to zero along the full height sequence.

There is also a partial bijection $\mathcal M_T$ between $\mathcal S_T$ and $\mathcal A_T$ omitting $o(N)$ copies on each side, with
$$
 \frac{1}{N}\sum_{(\rho,\rho')\in\mathcal M_T}L^2|\rho-\rho'|^2
 \le 3\mathcal E_T+o(1). \tag{5c}
$$
This pairing may differ from the absolute-rank pairing. The factor $3$ is sharp in the abstract contraction graph class in Appendix C. Along any sequence $T_j\to\infty$, $\mathcal E_{T_j}\to0$ if and only if for every $\varepsilon>0$ the proportion, relative to $N$, of source copies of depth $d\ge\varepsilon$ tends to zero. The same criterion holds using the target copies alone. Equivalently, $q_{T_j}\to0$, or the normalized sum of squared complex displacements tends to zero for some partial bijections omitting $o(N)$ copies on each side. In particular, equal subsequential limits of the two dyadic second depth moments must both vanish.

The normalization in (3a) gives $a_{2,T}-b_{2,T}=(N/(TL))\mathcal E_T$. If $E_2=a_2-b_2$ is a limiting gap in that normalization, then $a_2\ll E_2\log^5(e+1/E_2)$, with value zero at $E_2=0$.

The finite comparison uses a contraction on the strict-upper spectral subspace of a real-polynomial approximation. To transfer the ordinate comparison, we align the absolute counts on most caps and compare the number of rank intervals covering two specified heights. The support of $D$ in Theorem 2 and the source depth tail control long rank intervals. The complex comparison uses a balanced form of the same contraction. For rigidity, on most microscopic cells the local pole sum has a bounded holomorphic remainder. A positive-depth cluster of $m$ source copies then has a surrounding disk with $m-1$ target copies, which forces an omission or a positive displacement. [Proof in Appendix C](supplement/locality.md#c1-finite-polynomial-comparison)

**Theorem 4.** For every sufficiently high strict-left zeta zero $\rho=\beta+i\gamma$ there is a strict-left derivative zero $\beta'+i\gamma'$ with
$$
 |\gamma'-\gamma|\le
 \frac{\log\log\gamma-\log\log\log\gamma+\log\beta}{2\pi}+O(1).
 \tag{6}
$$
If $0<d_\rho\le1/4$, a witness also exists with
$$
 |\gamma'-\gamma|\le
 \frac{\log(1+d_\rho\log\gamma)-\log(1+\log(1+d_\rho\log\gamma))}{2\pi}
 +O(1). \tag{7}
$$
The constants are uniform. A multiple zero supplies its own witness. Conversely, every noncommon strict-left derivative zero of height at least $10$ has a strict-left zeta zero $\beta+i\gamma$ with
$$
 (\ell-\beta)^2>(\ell-\beta')^2+(\gamma'-\gamma)^2.
 \tag{8}
$$

For the limit laws take $a=T/L$, $\sigma_T=L/(2\pi)$ and $t$ uniform on $[a,T]$. Define $A_T$ and the empirical depth law $\nu_T$ by
$$
 A_T(t)=\frac{2i}{L}\frac{\zeta'}{\zeta}(\ell+it)+i,\qquad
 D_\rho=\sigma_T|\beta-\ell|,\qquad
 \nu_T=\frac1{n_T}\sum_{a<\gamma\le T}m_\rho\,\delta_{D_\rho},
 \qquad n_T=\sum_{a<\gamma\le T}m_\rho. \tag{9}
$$
Here the sums in (9) run over distinct nontrivial zeros with their indicated multiplicities $m_\rho$. All random variables involving the quotient can be defined arbitrarily at its exceptional ordinates, a set of measure zero.

**Theorem 5.** The families $\nu_T$ and $\Re A_T$ are tight and $\Im A_T\to0$ in probability. On any sequence with $\nu_T\Rightarrow\nu$ and $\Re A_T\Rightarrow W$,
$$
 \lim_{q\downarrow0}\frac{1-\mathbb E e^{iqW}}q=\nu(\{0\}),\qquad
 \lim_{r\to\infty} r\,\mathbb P(W>r)
 =\lim_{r\to\infty} r\,\mathbb P(W<-r)
 =\frac{\nu(\{0\})}{\pi}. \tag{10}
$$
The convergence in height precedes the limits in $q$ and $r$. In the two tail formulas the finite-height exceedance probabilities converge at continuity thresholds of the corresponding limiting law. The same laws apply to uniform sampling on $[0,T]$ and the depth law over $(0,T]$, with the same normalization. In particular, $A_T\Rightarrow\operatorname{Cauchy}(0,1)$ if and only if $\nu_T\Rightarrow\delta_0$, where the standard Cauchy density is $1/(\pi(1+x^2))$.

**Corollary 6.** The following conditions on the full height sequence are equivalent.

- $\nu_T\Rightarrow\delta_0$, equivalently $H(T)=o(T)$, where $H(T)=\sum_{0<\gamma\le2T}m_\rho(\beta-\ell)_+$ with the convention of [3].
- $W_\zeta(\ell;T,2T)=o(T)$, or equivalently $W_{\zeta'}(\ell;T,2T)=o(T)$.
- $A_T\Rightarrow\operatorname{Cauchy}(0,1)$.
- The mean of $\log|\zeta'/\zeta(\ell+it)|$ on $[T/L,T]$ is $\log\log T+o(1)$. Equivalently, the same holds on $[T,2T]$.

Theorem 3 adds $\mathcal E_T\to0$ to this full-sequence list. Under these conditions the total squared ordinate cost in (5) is $o(N)$ even for ranks crossing the dyadic edges. Theorem 3 also gives a dyadic rigidity criterion on arbitrary height subsequences.

**Theorem 7.** For absolute $C,T_0>0$, put $E_T=\exp(C(\log\log T)^2)$ and take $T\ge T_0$. A strict-left zeta zero $\rho=\beta+iT$ of scaled depth $d=L(\ell-\beta)>0$ with $CE_Td\le1$ has a strict-left derivative witness within distance $CE_Td/L$ of $\ell+iT$. In fact, a strict-left half-disk of that radius or smaller contains $\rho$ and has equal full counts for $\zeta$ and $\zeta'$. More generally, writing
$$
 B_T=\sum_{\rho}\frac{m_\rho}{1+L^2(\Im\rho-T)^2}
$$
over distinct nontrivial zeta zeros, every $0<r\le 1/[C(1+B_T)E_T^2]$ admits an equal-count half-disk of physical radius $R/L$ with $r\le R\le CE_T\sqrt{(1+B_T)r}$. The circular arc, including its endpoints, is free of zeros of both functions. In particular, for each fixed $A>0$ one can take the physical radius in $[T^{-A}/L,T^{-A/2+o(1)}/L]$.

**Theorem 8.** Let $N=N_\zeta(2T)-N_\zeta(T)$ be the full nontrivial zeta count on $(T,2T]$. For each $\varepsilon>0$ there are $h_\varepsilon>0$, $C_\varepsilon<\infty$ and $T_\varepsilon$ such that for every $T\ge T_\varepsilon$ and $0<h\le h_\varepsilon$ there is one partial bijection between strict-left $\zeta$ and $\zeta'$ copies on $(T,2T]$. Using $L(\ell-\Re s)$ for depth and $L|s-s'|$ for distance, it pairs all but at most $\varepsilon N$ zeta copies of depth at most $h$ within distance $C_\varepsilon h$, and all but at most $\varepsilon N$ derivative copies of depth at most $h$ within distance $C_\varepsilon\sqrt h$. Each family of supporting half-disks is internally disjoint, and every forward disk is contained in one reverse disk or disjoint from the reverse family. The assertion is unconditional, with a height threshold independent of $h$.

[Appendix D](supplement/local_matching.md) proves Theorems 7 and 8. It also shows that simultaneous weak limits of the strict-left depth measures with mass $1/N$ per copy have equal atoms at depth zero. These measures restrict to the strict-left divisors at each finite height.

Speiser's theorem [1] is the zero-exclusion equivalence with RH. Levinson and Montgomery [2, Theorem 4] obtained the left weighted comparison at $v=\ell$ with error $O(V-U)$ for intervals longer than $\log T$. Their proof contains the critical-line log-mean identity. Their Theorem 6 uses a depth buffer, and their Theorem 1 and §2 give $D(t)=O(\log t)$ and the clean-cap contour behind Theorem 2. Garaev and Yıldırım [10] give ordinate proximity results starting from a zero of $\zeta'$. The forward estimates (6)–(7) start from a strict-left zero of $\zeta$. Corollary 6 concerns horizontal collapse on the $1/\log T$ scale and permits zeros strictly off the line at smaller distances and a density-zero set of exceptions. RH implies these conditions. Establishing horizontal collapse for $\zeta$ remains open.

Garunkštis [20, Theorem 1.1] proved exact strict-left count equality in a half-disk centered at $\ell+it$ at every sufficiently large $t$, with physical radius in $[e^{-t^A},e^{-t^{A-0.17}}]$ for $A>0.17$. His Theorem 2.1 treats a subclass of the extended Selberg class with a separate radius parameter. Theorem 7 controls the inflation of a prescribed starting radius and gives a bound relative to an enclosed zero's depth. Theorem 8 uses compatible radii to match copies simultaneously in both directions.

The projected ordinate statistic in [3, Theorem 7.1] is unconditionally Cauchy. For the actual quotient, Sodin [4, §3.4.5] proved the Cauchy limit under RH, and Najnudel and Nikeghbali [3, Theorem 8.7] proved it under $H(T)=o(T)$. Their Remark 8.11 discusses the off-line correction. Theorem 5 identifies which depth mass survives in the imaginary mean of a folded transform after the height limit, and Section 6 derives the converse from that mean.

## 2. A folded contour at a common threshold

Put $F=\zeta'/\zeta$ and use $\zeta(s)=\chi(s)\zeta(1-s)$. Let $J=\chi'/\chi$ and
$$
 K(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(s/2),
$$
where $\psi=\Gamma'/\Gamma$. The Hadamard product of $\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ gives
$$
 \Re F(s)=\sum_\rho m_\rho\Re\frac1{s-\rho}-\Re K(s). \tag{F1}
$$
Indeed the real part of the product's constant term after collecting the $1/\rho$ terms is zero. On the critical line away from the zeros, $\xi$ is real and $\xi'$ purely imaginary, while the absolutely convergent sum of the real parts pairs to zero under $\rho\mapsto1-\bar\rho$. This yields (F1) off the divisor as well [2, (2.1)].

For $\beta<v$ reflect $\rho$ to $\rho^*=2v-\bar\rho$ and define
$$
 G_v(s)=F(s)+D_v(s),\qquad
 D_v(s)=\sum_{\beta<v}\frac{2m_\rho(v-\beta)}{(s-\rho^*)(s-\rho)}. \tag{F2}
$$
The tail converges locally normally, uniformly in $v$, by the unit-height count $O(\log(2+|t|))$ from Riemann–von Mangoldt [11, Ch. 9]. Each added difference cancels the full residue of the corresponding left pole of $F$. The only new poles are strictly right of $v$. In the high rectangle $-T\le\Re s\le v$, $U\le\Im s\le V$, Stirling gives $\Re K(s)=\tfrac12\log(|s|/(2\pi))+O(T^{-1})>0$. To the left of $v$, (F1) and (F2) express $\Re G_v$ as the real parts of the fractions with the folded poles, minus $\Re K$. Each real part is nonpositive. Thus $G_v$ is holomorphic with negative real part there. The divisor of $F/G_v$ is the signed difference of the divisors of $\zeta'$ and $\zeta$. At a $\zeta$ zero of order $m$ the derivative has order $m-1$, so the quotient has a simple pole.

On $v+it$ define $P_-$ and $P_+$ as the sums over $\beta<v$ and $\beta>v$, respectively, of $m_\rho|\beta-v|/((t-\gamma)^2+(\beta-v)^2)$. Write $Q=\Re K+P_+$. Away from poles,
$$
 \Re F=P_--Q,\qquad \Re G_v=-P_--Q,\qquad
 \Im F=\Im G_v,\qquad |G_v|^2-|F|^2=4P_-Q\ge0. \tag{F3}
$$
A pole on the folding line has the same residue in $F$ and $G_v$, and the ratio extends there with value one. At zeros of the ratio the boundary logarithm is locally integrable.

For $1\le A\le T$ and $s=-A+it$ the two real parts $\Re\rho,\Re\rho^*$ in (F2) are nonnegative, so
$$
 |D_v(-A+it)|\ll \sum_\rho\frac{m_\rho}{A^2+(t-\gamma)^2}
 \ll \frac{L}{A}. \tag{F4}
$$
For the second bound, sum in unit bins. At ordinate distances $j\le4T$ each bin contributes $O(L)/(A^2+j^2)$, and at $j>4T$ the tail is $O(L/T)$. From the sine-gamma expression for $\chi$,
$$
 J(s)=\log(2\pi)-\log(1-s)-i\pi/2+O(T^{-1})
$$
for $\Re s\le1$ at these positive heights. The branch of $\log(1-s)$ is the principal one on the far left and continues to this strip. Since $F(s)=J(s)-F(1-s)$ and $F(1+A-it)=O(2^{-A})$, there are no derivative zeros at $\Re s\le-1$ for sufficiently large $T$. The same formula applies to $\Re s<-T$, with $\Re J\le-c\log(T+|\Re s|)$. In particular $|F|,|G_v|\gg L$ for $-T\le\Re s\le-1$. At the left edge $F/G_v=1+O(1/T)$. For a fixed sufficiently large $C$, on the portion $\Re s=-A$ with $A\ge C$ we have $F/G_v=1+O(1/A)$ in a disk about one of radius less than $1/2$.

Consider generic horizontal edges at height $Y$ containing no zeros of $\zeta$ or $\zeta'$ along the segment. On $[-C,v]$ the argument of $G_v$ lies in an interval of length $\pi$. For $f=\zeta,\zeta'$ the change from the argument at $-C+iY$ is $O(L)$, uniformly at each point of $[-C,1]+iY$. To see this, put $g(z)=f(z+iY)/f(-C+iY)$ and apply Jensen's formula to $(g(z)+\overline{g(\bar z)})/2$ on two fixed concentric disks about $-C$ with the smaller disk containing $[-C,1]$. The symmetrization equals one at the center. The Euler product at $1+C-iY$ and the functional equation bound $1/|\zeta(-C+iY)|$ by a power of $T$. The same holds for $1/|\zeta'(-C+iY)|$ by the lower bound on $|F|$. Polynomial growth of $\zeta$ on fixed strips and Cauchy's estimate for $\zeta'$ bound the symmetrization above by a fixed power of $T$. It therefore has $O(L)$ real zeros on the segment. Between successive real zeros the argument of $g$ stays in a half-plane, giving the asserted bound. Anchoring the argument of $F/G_v$ at $-T+iY$ in the branch near one, its horizontal integral is $O(L)$, using (F4) to integrate $O(1/A)$ on the far left.

For a meromorphic ratio $M=F/G_v$, write $I_x=\int_U^V\log|M(x+it)|\,dt$ and $B_Y=\int_{-T}^v\arg M(x+iY)\,dx$ with the preceding anchoring. Littlewood's lemma with distance measured from the right edge gives
$$
 2\pi(W_{\zeta'}-W_\zeta)(v;U,V)=I_v-I_{-T}-B_V+B_U. \tag{F5}
$$
The orientation follows by reflecting the usual left-edge version, or by applying Green's identity to $v-x$ and $\log|M|$ with $\Delta\log|M|$ equal to $2\pi$ times the signed divisor. The Cauchy–Riemann equations turn the horizontal normal derivatives into the indicated argument terms. For right-edge divisor points one may first use $v-\varepsilon$ with the same $G_v$, and then increase the edge to $v$. Locally $\log|M|=k\log|s-s_0|+O(1)$, so the vertical integrals converge. For nongeneric heights use zero-free $U_j\downarrow U$ and $V_j\downarrow V$ from above. Finiteness of the local divisor realizes exactly $(U,V]$ for large $j$, and the estimates are uniform on a slightly enlarged comparable-height range. Thus $I_v\le0$ by (F3), $I_{-T}=O(1)$, and (F5) proves the forward bound with all endpoints and orders.

The function $\log(-G_v)-\log(-J)$ is holomorphic in the open rectangle by the negative real parts. Its imaginary part is bounded and, on $\Re s=-A$ with $A\ge C$, the function is $O(1/A)$ since $G_v-J=D_v-F(1-s)$. Cauchy's theorem applied to this logarithm gives $\int_U^V\log|G_v/J|(v+it)\,dt=O(L)$, using the same edge limits and the $O(1/T)$ bound at $-T$. On the right line $J(v+it)=-\log(t/(2\pi))+O(T^{-1})$. Substitution into (F5) proves the second identity in (1).

To deduce (2), use the density bound
$$
 \#\{0<\gamma\le X:\beta\ge\ell+u\}
 \ll_\kappa X\log X\,e^{-\kappa u\log X}\qquad(0\le u\le1/2), \tag{F6}
$$
with multiplicities [3, Lemma 8.4], [5, Theorem 2.4], [6]. By symmetry $W_\zeta(\ell-\delta;0,2T)$ is the integral of the right-hand count from $u=\delta$ to $1/2$, so it is $O_\kappa(Te^{-\kappa\delta L})$. Adding the error in (1) proves (2). In particular for $1\le d\le L/2$,
$$
 \#\{U<\gamma'\le V:\beta'\le \ell-d/L\}
 \ll_\kappa TL e^{-\kappa d}+L^2,
$$
by using $v=\ell-(d-1)/L$, where each such zero costs at least $1/L$. More generally, the depth first moment per $TL$ in the scaled variable $D'=L(\ell-\beta')_+$ is uniformly integrable in the height limit. For $1\le B\le L$, the inequality $D'\mathbf1_{D'>B}\le 2(D'-B/2)_+$ and (2) bound the tail per $TL$ by $O_\kappa(e^{-\kappa B/2}+L/T)$. For $B>L$, use $D'\mathbf1_{D'>B}\le2(D'-L/2)_+$ and (2) at $v=0$. This also accounts for derivative zeros with $\beta'<0$. The bounds use cumulative density for $\zeta$. A density estimate on a shorter interval transfers by integrating on that interval and applying (1).

## 3. The reverse comparison and its model

Appendix A constructs disk maps from the functional-equation quotient
$$
 q(s)=\frac{\chi(s)\zeta'(1-s)}{\zeta'(s)},\qquad 1+q=J/F.
$$
A finite left half-plane Blaschke product $B$ cancels the poles of $q$ and incorporates the full left derivative divisor. On a padded rectangle of width $L^2$ the maps $-e^{-e_T}Bq$ and $e^{-e_T}B$, with $e_T=O(L^2/T)$, have coincidence divisor equal to the full left zeta divisor. At an anchor of depth one, the half-difference after a common disk automorphism sending the hyperbolic midpoint to zero has logarithmic loss at most $(1+O(L^{-1}))\Phi(\lambda)$, where $\lambda=e_T-\log|B|$ at the anchor. Integrating the Green function over anchors recovers the zeta depth mass. Averaging $\Phi(\lambda)$ by concavity gives the unstrengthened comparison.

For the strict gain, Jensen's formula retains the boundary logarithmic loss. A folded periodic transform in the same rectangle gives a real tail of order $1/r$ on its critical-line edge for a positive proportion of anchors. Its imaginary mean falls short of its anchor value by the harmonic mass of literal critical-line zeros, up to an $O(L^{-1})$ loss on the other edges. This yields the tail bound uniformly in $r$, because the tail contribution from the other edges is $O(1/(Lr))$. The critical-line zero proportion follows, for example, by tiling $(T,2T]$ with intervals of length $x^{3/4}$ starting at $x$ and using Steuding's published short-interval theorem [15]. The excluded last interval contributes $O(T^{3/4}L)$ zeros.

Write $\mu=e_T+(2\pi/|J_T|)\sum d'$, where $J_T=[T-L^3,2T+L^3]$ is the anchor interval and the sum is the left derivative depth over the outer rectangle. If $\lambda<\mu/2$ on a sufficiently large fraction of the anchors, the tangent gap of $\Phi$ gives a gain of order $\sqrt\mu$. Otherwise many anchors supporting the real tail also have $\lambda\ge\mu/2$. There the disk automorphism has distortion $O(\mu^{-1/2})$. On the critical-line tail event at threshold $r\asymp\mu^{-1/2}$, the identity $1+q=J/F$ makes the transformed half-difference at most $1/2$ in modulus. Jensen then gains order $\sqrt\mu$ on average. Appendix A proves $a_T\le\Phi(\mu)-c\sqrt\mu$ for positive bounded $\mu$, uniformly down to zero. Since $\mu-b_T=O(L^4/T)$, the $1/2$-Hölder continuity of $\Phi$ and the square root gives (3).

### The three-term model

Take $\lambda,d>0$ and put $z=\lambda(s-\ell)$. The three-term self-inversive family of Dubickas and Jankauskas [14, proof of Theorem 2] gives the exponential polynomial
$$
 f(s)=\tfrac12(1+e^{-z})-\cosh(d/2)e^{-z/2}
     =\tfrac12(e^{-z/2}-e^{d/2})(e^{-z/2}-e^{-d/2}).
$$
It respects conjugation and satisfies $f(s)=e^{-z}f(1-s)$. Its zeros are simple, at $z=\pm d+4\pi i n$, $n\in\mathbb Z$. Since $f'(s)=(\lambda/2)e^{-z/2}(\cosh(d/2)-e^{-z/2})$, its derivative zeros are simple, at $z=-2\log\cosh(d/2)+4\pi i n$. On every interval $(U,V]$ whose positive length is a multiple of $4\pi/\lambda$, normalize the left moments by $2\pi/(V-U)$. They are $a=d/2$ and $b=\log\cosh(d/2)$. The model has no literal critical-line zeros for $d>0$.

## 4. Strict-left counts

### 4.1. Clean caps and the signed count

At $s=\ell-x+it$, a reflected zeta pair $\ell\pm d+i\gamma$ contributes to (F1), per unit multiplicity,
$$
 P_d(x,u)=
 \frac{2x(d^2-x^2-u^2)}
 {((x-d)^2+u^2)((x+d)^2+u^2)},\qquad u=t-\gamma. \tag{D1}
$$
A critical-line zero contributes $-x/(x^2+u^2)$. For $0\le\Re s\le\ell$ and $t\ge10$, the gamma term in (F1) satisfies
$$
 \Re K(s)=\Re\left(\frac1{s-1}+\frac12\psi(1+s/2)\right)-\frac12\log\pi
 \ge \frac12\log\frac{t}{2\pi}-\frac{19}{4t^2}>0. \tag{D2}
$$
For the bound, Euler–Maclaurin gives $\psi(w)=\log w-1/(2w)+R(w)$ with $|R(w)|\le 1/(4|w|^2)$ for $\Re w>0$. The explicit term of order $w^{-2}$ costs $1/(12|w|^2)$ and the integral remainder is bounded by $(1/6)\int_0^\infty |w+y|^{-3}\,dy\le 1/(6|w|^2)$. With $w=1+s/2$, use $|s+2|\ge t$ and bound the negative contribution from $\Re(1/(s-1))$ by $1/t^2$.

Call a height clean if its cap $[0,\ell]+it$ has $\Re F<0$ away from any critical-line pole and has no strict-left pole. At $t\ge10$ outside $E$, (D1) is nonpositive for every pair, including those at negative heights. The cap is clean by (D2), and contains no strict-left derivative zero. On the vertical sides, $\Re F<0$ follows from (D1)–(D2). At a critical-line zeta zero of order $m$, the regular part of $F-m/(s-\rho)$ has real part $-\Re K(\rho)<0$. On a small left semicircular indentation the pole term also has nonpositive real part. The indentations exclude critical-line points of both divisors while preserving the strict-left points. Use a quarter circle at a clean top that meets a critical-line pole.

Appendix B gives the interval certificate that $\zeta$ and $\zeta'$ have no zeros in $[0,\ell]\times[0,11]$. The counts start at zero and the bottom cap at height 10 is clean. Between two clean caps the contour image under $F$ is in the open left half-plane. Its winding is zero. The argument principle counts the difference of full divisor orders, so a common zero of orders $m,m-1$ contributes $-1$. This gives $D(t)=0$ at every clean cap. In particular,
$$
 \frac{|\{t\in[T,2T]:D(t)\ne0\}|}{T}
 \le \frac{2}{T}W_\zeta(\ell;T-1,2T+1)
 =\frac{a_T}{\pi}+O(L/T). \tag{D3}
$$
The expansion at both ends costs $O(L)$ in the depth sum by the unit-height count. The sign criterion uses open intervals, since a zero with $|u|=d$ cannot give a positive term in (D1). At any noncommon strict-left derivative zero of height at least 10, $\Re F=0$, so (D1)–(D2) also give (8).

### 4.2. Jensen on the cap

At generic $t$ the cap contains no point of either divisor. Let $n(t)$ count the real-part zeros on the cap with their real-analytic orders. Between consecutive real-part zeros the argument lies in an interval of length $\pi$. If $n(t)>0$, its net change along the cap is bounded by $\pi(n(t)+1)$. The rest of the contour is in the left half-plane and has net change at most $\pi$ in absolute value. If $n(t)=0$, the cap is clean. Thus $|D(t)|\le 2n(t)$.

Set
$$
 H_t(z)=\tfrac12\bigl(F(\ell-z/L+it)+F(\ell-z/L-it)\bigr).
$$
This meromorphic function equals $\Re F(\ell-z/L+it)$ on real $z$. By (D2), $|H_t(0)|\ge c_0 L$ for large $T$. For $1\le b\le L$ let $J_b(t)$ count its zeros in $|z|\le2b$ and let $M_h(t)$ count zeta zeros with $|\gamma-t|\le h/L$. Each pole in $|z|\le4b$ is from a zeta zero and lies at radius at least $L|\gamma-t|$, using conjugation for the negative-height summand. Counting both summands and using the full zeta multiplicities only increases the pole contribution. Meromorphic Jensen's formula gives
$$
 (\log 2)J_b(t)\le
 \log(1/c_0)+\int_0^{2\pi}\log^+\frac{|H_t(4be^{i\theta})|}{L}\frac{d\theta}{2\pi}
 +2\int_0^{4b}M_h(t)\frac{dh}{h}. \tag{D4}
$$
The pole sum is the last layer-cake integral. If the outer circle meets a divisor point, take inner radii increasing to $4b$. The mean of the full logarithm is continuous in the radius by factoring the finitely many nearby zeros and poles.

For a fixed $\sigma\in[-4,5]$ and $|\delta|\le4$, the normalized values $F(\sigma+i(t+\delta))/L$ have tails $O(1/r)$ for $r\ge1$, uniformly in these parameters. To see this, subtract the Hadamard logarithmic derivatives at $\sigma+i(t+\delta)$ and $C+i(t+\delta)$ for fixed $C>6$. The gamma difference is $O(T^{-1})$, the quotient at $C$ is bounded, and zeros outside $[T/2,3T]$ contribute $O(L/T)$ by the unit-height count and the difference of resolvents. In the remaining finite sum the absolute real part is bounded by a positive sum of Poisson kernels of total mass $O(TL)$. Its imaginary part is, up to a sign and normalization, a Hilbert transform of the positive measure obtained by replacing each zero by a Poisson measure of width $|\sigma-\beta|$ at its ordinate. A zero width gives a point mass. The subtracted resolvents at $C$ admit the same bounds. Markov's inequality and the weak $(1,1)$ Hilbert transform inequality for finite measures yield the stated tail [9]. At each fixed angle the two evaluations of $H_t$ have parameters in these ranges, after conjugation at negative heights. The union bound, followed by integration of the exponential tail for the positive logarithm, gives $L^k(dt/T)$ norm $O(k)$ for the circle integrand and its mean.

Rodgers [16, remarks after Corollary 1.2 and (16)] records the unconditional bound $O(e^{-c u})$ for the probability that a window of length $1/\log X$ contains more than $u$ zeros, for a uniform start in $[X,2X]$. Hence the $k$-norm of a window of length $1/L$ is $O(k)$ on slightly enlarged dyadic ranges. Indeed split the window into at most two windows of length $1/\log(4T)$ and cover their translated starts by the dyadic ranges with $X=T/2,T,2T$. Covering a longer window gives $\|M_h\|_k\ll kh$ for $1\le h\le4L$. For $0<h\le1$ expand $M_h^k$ into ordered tuples of zero copies for integer $k$. Each tuple that contributes has a set of admissible centers in $[T,2T]$ of length at most $2h/L$. Any one such center extends to an interval of radius $1/L$ of centers for the enlarged half-width $2/L$ in $[T-2/L,2T+2/L]$. Comparing the integrals tuple by tuple gives $\|M_h\|_k\ll k h^{1/k}$. Minkowski in (D4) now yields, with an absolute constant,
$$
 \|J_b\|_k\ll k(k+b). \tag{D5}
$$

A real-part zero at $Lx\ge b$ requires by (D1)–(D2) a pair with $Ld>b$ and $|t-\gamma|<d$. Let $E_b$ be the union of these projected intervals for depths $Ld>b$. For $t\in[T,2T]$ only ordinates in $(T-1,2T+1]$ enter. If $Q(u)$ counts the strict-left zeros in this interval with $Ld\ge u$, (F6) and reflection give $Q(u)\ll TL e^{-c u}$. Thus $|E_b\cap[T,2T]|/T\le 2(bQ(b)+\int_b^\infty Q(u)\,du)/(TL)\ll e^{-c' b}$ for a smaller $c'>0$. For $r\ge1$ take $b=\min(r,L)$ and $k=\lfloor r\rfloor$. Outside $E_b$ all cap zeros are counted by $J_b$. If $r\ge L$ then $E_b$ is empty. By (D5) and Markov's inequality, $\mathbb P_T(|D|>C r^2)\ll e^{-c''r}$ for a sufficiently large absolute $C$. Adjusting constants for small thresholds gives (4). Integration gives $\mathbb E_T|D|^k\le AB^k(2k)!$ for integer $k\ge1$, and monotonicity extends the norm bound to real $k\ge1$.

### 4.3. Density of equality

Fix $0<r<1$. The cores $|t-\gamma|<rd$ cost at most $2r\sum d$ in length. Outside them, the positive terms in (D1) have $rd\le |u|<d$. In this region the denominator is $(d^2-u^2-x^2)^2+4d^2u^2$. Maximizing $x(d^2-u^2-x^2)$ over the positive region gives
$$
 0<P_d(x,u)\le\frac{(d^2-u^2)^{3/2}}{3\sqrt3\,d^2u^2}.
$$
At a generic bad cap at least one point has $\Re F\ge0$. Drop all negative terms at that point, and use $\Re K\ge(1/2-o(1))L$. The fringe envelope integrates to $2J(r)/(3\sqrt3)$ per zero, where
$$
 J(r)=\int_r^1\frac{(1-v^2)^{3/2}}{v^2}\,dv
 =\frac{\sqrt{1-r^2}}{r}-\frac32\arccos r+\frac r2\sqrt{1-r^2}.
$$
Markov's inequality for the sum of envelopes, with $O(L)$ endpoint zeros, gives
$$
 \mathbb P_T(D\ne0)
 \le \frac{r a_T}{\pi}
 +\frac{4J(r)}{3\sqrt3}\frac{N_\zeta^-(2T)-N_\zeta^-(T)}{TL}+o(1).
 \tag{D6}
$$
If the dyadic line fraction has lower limit at least $\kappa$, reflection and Riemann–von Mangoldt bound the limsup in (D6) by $\bigl(r\limsup a_T+(1-\kappa)J(r)/(3\sqrt3)\bigr)/\pi$. Any lower bound for the simple-line fraction also bounds the full line fraction from below. Appendix B derives the journal-moment row, and Appendix F obtains the signed-trace row using the corrected short dyadic formula of [26], the Montgomery–Taylor window as in [27], and the one-piece moment of [17]. The Arb checks use the exact $2-C$ in the signed-trace row.

| Arithmetic input | $\kappa$ | $h$ | $r$ | Upper bound on $\limsup a_T$ | Equality lower density from (D3) | Equality lower density from (D6) |
|---|---:|---:|---:|---:|---:|---:|
| **Signed trace and mollified sampling** [17, 26, 27] | $2-C$ | 1.046 | .391 | .32133 | .89771748 | **.94435382** |
| Journal-only [17, 18] | .417293 | .626 | .431 | .442758582 | .85906556 | .91782945 |
| No line-count input | 0 | 0 | .498 | .505800456 | .83899871 | .89635996 |

All lower bounds are rounded down, and the upper bounds are rounded up. To pass to $[0,X]$, decompose it into $(X/2^{j+1},X/2^j]$, use the dyadic lower bound minus any fixed $\epsilon>0$ for sufficiently large lower endpoints, and let $X\to\infty$ then $\epsilon\downarrow0$. Under horizontal collapse (D3) yields density one, and (4) with Hölder gives $\mathbb E_T|D|^p\to0$ for every fixed $p>0$. Theorem 3 strengthens this mean control by charging the full squared displacement of every rank touching the window against the difference of the dyadic second depth sums.

## 5. A periodic transform for the actual quotient

Put $P=\sigma_T(T-a)$, $x=\sigma_T(t-a)$ and $y_\rho=\sigma_T(\gamma-a)$ modulo $P$, using the same zeros as in (9). Define
$$
 \mathcal H_T(z)=-\frac1P\sum_{a<\gamma\le T}m_\rho
   \cot\!\left(\frac{\pi(z-y_\rho+iD_\rho)}{P}\right),\qquad
 X_T=\Re\mathcal H_T(x),\quad Y_T=\Im\mathcal H_T(x),\quad c_T=n_T/P.
$$
This folds the poles to $y_\rho-iD_\rho$ below or on the real axis. All zeros in a reflected pair contribute at this location with equal orders, so their total weight is the sum of those orders. The upper half-plane transform has nonnegative imaginary part and tends to $ic_T$ at $i\infty$. Riemann–von Mangoldt gives $c_T=1+O(\log L/L)$. Viewed as a function of $w=e^{2\pi iz/P}$, the bounded analytic test $\exp(iq\mathcal H_T)$ for $q>0$ has disk mean equal to its value at zero. Taking radial limits off the finitely many boundary poles gives
$$
 \mathbb E e^{iq X_T-qY_T}=e^{-q c_T},\qquad
 X_T+Y_TC\ \sim\ \operatorname{Cauchy}(0,c_T), \tag{C1}
$$
where $C$ is an independent standard Cauchy variable. The second equality follows by conditioning and by conjugation for negative $q$. By symmetry of $C$, conditional on $(X_T,Y_T)$ with $|X_T|>r$, there is probability at least $1/2$ that $X_T+Y_TC$ lies on the same side of the corresponding threshold. Thus $\mathbb P(|X_T|>r)\ll (1+r)^{-1}$ uniformly.

### 5.1. Passing to the actual real part

Let $R=L^2$. By [3, Lemma 8.1 and Appendix A], for $t\in[a,T]$ away from zeta zeros the local expansion of $\Re A_T(t)$ has the summand $m_\rho s/(\pi(s^2+D_\rho^2))$ at $s=\sigma_T(t-\gamma)$ with $|s|\le R$, and uniform error $O(\log L/L)$. In this expansion the signed imaginary parts from reflected partners cancel. Equivalently, if $\zeta(\ell+it)=e^{-i\vartheta(t)}Z(t)$ with $Z$ real, then $\Im A_T=1-2\vartheta'(t)/L$ off the zeros. Stirling gives $\vartheta'(t)=\tfrac12\log(t/(2\pi))+O(t^{-2})$, so the imaginary part is $O(\log L/L)$ uniformly. This is the height-dependent gamma-factor term. The center value $ic_T$ of $\mathcal H_T$ comes from the average ordinate intensity.

The negative real part of each cotangent term, without its weight, is the kernel
$$
 k_D(s)=\frac1P\Re\cot\!\left(\frac{\pi(s+iD)}P\right)
 =\frac{\sin(2\pi s/P)}{P[\cosh(2\pi D/P)-\cos(2\pi s/P)]},
 \qquad -P/2\le s<P/2 .
$$
For $|s|\le R$, the cotangent expansion at zero gives $k_D(s)=s/(\pi(s^2+D^2))+O((R+L)/P^2)$ because $D\le L/(4\pi)$. When $R<x<P-R$ the near terms coincide with the local expansion. Riemann–von Mangoldt bounds their multiplicity sum by $O(R+L)$. The excluded endpoint event has probability $O(R/P)$.

On $R<|s|\le P/2$, the formula for $k_D$ gives $|k_D(s)-k_0(s)|\ll D^2/|s|^3$. Indeed the denominator increases by $\cosh(2\pi D/P)-1\ll (D/P)^2$, while $1-\cos(2\pi s/P)\gg(s/P)^2$ and $|k_0(s)|\ll1/|s|$. On circular arcs of length $r$ the number of zeros is $O(r+L)$ by Riemann–von Mangoldt, splitting at the endpoint of the period if needed. Summing the far replacement over dyadic arcs gives $O(L^2/R^2+L^3/R^3)$.

For the resulting unmarked kernel on the far arcs, write the circular counting measure as $f_T(v)\,dv+dE_T(v)$ with
$$
 f_T(v)=L^{-1}\log\!\left(\frac{a+v/\sigma_T}{2\pi}\right),\qquad 0<v<P.
$$
The oriented arc discrepancy $E_T$ on any arc is $O(L)$ by Riemann–von Mangoldt. Integration by parts on each of the two far arcs, using that $k_0(r)$ decreases from $O(1/R)$ to zero on $[R,P/2]$, gives error $O(L/R)$. The smooth part is
$$
 \int_R^{P/2} k_0(r)[f_T(x-r)-f_T(x+r)]\,dr,
$$
with the arguments read periodically. The total variation of $f_T$ on the circle is $2\log L/L$, including its jump at the endpoint. For a periodic function $f$ of bounded variation, the normalized $L^1$ difference of two translations a distance $2r$ apart is at most $2r\,\operatorname{Var}(f)/P$, by integrating the variation measure over translated arcs. Since $|k_0(r)|\ll1/r$, the smooth part tends to zero in $L^1(dx/P)$ at rate $O(\log L/L)$. The near and far estimates prove $\Re A_T+X_T\to0$ in probability. This also proves tightness of $\Re A_T$.

### 5.2. Positive depths and the surviving imaginary mean

For $D>0$ the contribution to $Y_T$ per unit weight is the circular Poisson kernel
$$
 p_{D,P}(s)=\frac{\sinh(2\pi D/P)}{P[\cosh(2\pi D/P)-\cos(2\pi s/P)]},
 \qquad \int_0^P p_{D,P}(s)\,ds=1 .
$$
This is the disk Poisson kernel with radial parameter $e^{-2\pi D/P}$ divided by $P$. Uniformly for the allowed depths it is $O(D/(s^2+D^2))$ for $|s|\le P/2$. Depth zero contributes zero to the boundary imaginary part almost surely. Hence $\mathbb E Y_T\le c_T$ and the portion of $Y_T$ from a Borel set $B_0\subset(0,\infty)$ has mean $c_T\nu_T(B_0)$. The $\nu_T$ are tight by (F6) and symmetry, which also give $\nu_T((B,\infty))\ll e^{-cB}$ for some $c>0$.

Fix $0<\epsilon<1<B$, and split $Y_T$ into the contributions from $(0,\epsilon)$, $[\epsilon,B]$ and $(B,\infty)$, denoted $S_T,M_T,U_T$. The deep part has mean $O(e^{-cB})$. For the shallow part discard the radius-$\sqrt\epsilon$ intervals about its centers. Their total sampling probability is at most $2c_T\sqrt\epsilon$, and integrating the Poisson kernels outside their respective intervals bounds the remaining shallow expectation by $O(\sqrt\epsilon)$. Therefore $\mathbb E(S_T\wedge K)\ll(1+K)\sqrt\epsilon$ for fixed $K>0$.

The middle part satisfies $\mathbb E M_T^2\ll_{\epsilon,B}1$. Each kernel there is bounded by $C_{\epsilon,B}/(1+s^2)$ in the signed circular distance. A unit arc at a uniform basepoint has an $O(1)$ second moment for its count by [3, Lemma 7.2 at length one], which uses the corrected Fujii range [5, Theorem 2.2 and footnote 3], [7]. More precisely, the portion that stays inside the period has second moment bounded by the full microscopic count in [3]. The arc wraps on a set of probability $O(1/P)$, on which it has at most $O(L)$ zeros, so its additional second moment is $O(L^2/P)$. A fixed arc offset preserves uniformity of the basepoint. Partition the signed distances into unit intervals and use the triangle inequality in $L^2$ with the summable weights $(1+j^2)^{-1}$. This gives the asserted bound with all multiplicities.

On a sequence as in Theorem 5, take a further joint weak limit $(X_T,Y_T)\Rightarrow(X,Y)$ using the tightness of both variables. Then $X$ has the law of $-W$, and $Y\ge0$. Choose $\epsilon,B$ at continuity points of $\nu$. Bounded continuous truncation and the three estimates give
$$
 \nu([\epsilon,B])-\frac{O_{\epsilon,B}(1)}{K}\ \le\
 \mathbb E(Y\wedge K)\ \le\
 \nu([\epsilon,B])+O((1+K)\sqrt\epsilon)+O(e^{-cB}). \tag{C2}
$$
For the lower bound use $Y_T\ge M_T$ and $M_T-(M_T\wedge K)\le M_T^2/K$. The upper bound follows by keeping the full mean limits for the middle and deep parts and truncating the shallow part. In the lower bound take $K\to\infty$ before $\epsilon\downarrow0$ and $B\uparrow\infty$. In the upper bound take $\epsilon\downarrow0$ and $B\uparrow\infty$ at fixed $K$ and then increase $K$. Thus
$$
 \mathbb E Y=\nu((0,\infty)). \tag{C3}
$$
This passage retains the mean from depths in any band bounded away from zero. The probability mass associated with positive depths tending to zero can contribute to $\nu(\{0\})$ even if the proportion of exact critical-line zeros stays smaller.

## 6. Characteristic cusp, both tails, and the logarithmic criterion

The analytic mean in (C1) is the periodic disk case of Aizenman and Warzel [8, Lemma 2.5 and (2.8)]. Their real-boundary hypothesis for a Cauchy law in Theorem 2.3 amounts to a vanishing imaginary boundary value. The tail interpretation for fixed transforms begins with Boole's atomic identity [13]. The Hruščëv–Vinogradov extension to singular measures and Poltoratski's one-sided coefficients are described in Poltoratski, Simon and Zinchenko [9, (1.5)–(1.8) and (5.4)]. We give a direct harmonic-measure argument for the limiting real law using (C3).

The bounded analytic tests in (C1) give $\mathbb E e^{iqX-qY}=e^{-q}$ for each $q>0$ in the joint limit, and $X+YC$ is standard Cauchy with $C$ independent of $(X,Y)$. For the cusp,
$$
 \frac{1-\mathbb E e^{iqX}}{q}
 =\frac{1-e^{-q}}q-\mathbb E\!\left[e^{iqX}\frac{1-e^{-qY}}q\right]
 \longrightarrow 1-\mathbb E Y=\nu(\{0\}).
$$
The last expectation converges by domination by $Y$, and conjugation gives the same limit for $W$.

Put $V_0=YC$. Conditioning and the Cauchy tail give, for either sign and fixed $0<\eta<1/2$,
$$
 \begin{aligned}
 r\,\mathbb P(\pm V_0>r)&\longrightarrow\mathbb E Y/\pi,\\
 r\,\mathbb P(|X|>\eta r,\ |V_0|>\eta r)&
 \ll_\eta \mathbb E[Y\mathbf1_{\{|X|>\eta r\}}]\longrightarrow0.
 \end{aligned}
$$
For the first limit the conditional tail times $r$ is bounded by $Y/\pi$ and converges to $Y/\pi$. Let $p_r$ denote the mixed-event probability in the second line. If $X+V_0>r$ and neither summand exceeds $(1-\eta)r$, then both exceed $\eta r$. Conversely, if one summand exceeds $(1+\eta)r$ and the other has absolute value at most $\eta r$, then the sum exceeds $r$. Consequently
$$
 \begin{aligned}
 \mathbb P(X+V_0>r)&\le
 \mathbb P(X>(1-\eta)r)+\mathbb P(V_0>(1-\eta)r)+p_r,\\
 \mathbb P(X+V_0>r)&\ge
 \mathbb P(X>(1+\eta)r)+\mathbb P(V_0>(1+\eta)r)-3p_r .
 \end{aligned}
$$
Multiplying by the respective rescaled thresholds gives
$$
 \frac{1-\eta-\mathbb E Y}{\pi}
 \le\liminf_{r\to\infty}r\,\mathbb P(X>r)
 \le\limsup_{r\to\infty}r\,\mathbb P(X>r)
 \le\frac{1+\eta-\mathbb E Y}{\pi}.
$$
Letting $\eta\downarrow0$ and repeating for $(-X,-V_0)$ proves both tails of (10). At fixed $T$ the same argument for the periodic transform gives $c_T\nu_T(\{0\})/\pi$ in each tail of $X_T$, because $\mathbb E Y_T=c_T(1-\nu_T(\{0\}))$. For example, the periodic transform $-\cot(\pi(u+id))$, $u$ uniform on $[0,1]$, has bounded real part for every $d>0$. As $d\downarrow0$ its real part converges in law to a standard Cauchy variable. The folded depth law is $\delta_d$ in this example, as in the paired lattice of [3, Example 8.12].

If the limiting marginal of $A_T$ is standard Cauchy, its cusp is one, so every possible limiting depth law is $\delta_0$. Conversely, collapse makes $Y=0$ almost surely by (C3), and the limiting test in (C1) then gives the standard Cauchy marginal. Tightness makes these full-sequence assertions. Uniform sampling on $[0,T]$ differs in total variation by $1/L$. The $O(T)$ zeros below $a$ from Riemann–von Mangoldt have relative mass $O(1/L)$ in the full depth law, so the same subsequential conclusions hold there as well.

### 6.1. One scalar deficit

For $h>0$ and any limit coupling $(X,Y)$ above, conditional Poisson integration gives
$$
 \mathbb E_C\log|X+YC+ih|=\log|X+i(h+Y)|.
$$
One can verify this by differentiating in $h$, convolving the Cauchy densities of scales $h$ and $Y$, and comparing both sides after subtracting $\log h$ as $h\to\infty$. The convolution follows from the Cauchy characteristic functions. The conditional logarithm is integrable, and its unconditional negative part is bounded for fixed $h>0$. The left side averaged in $(X,Y)$ equals $\log(h+1)$ by the standard Cauchy law of $X+YC$. It follows that the real marginal has deficit
$$
 \begin{aligned}
 \Delta_h(W)
 &=\log(h+1)-\mathbb E\log\sqrt{W^2+h^2}\\
 &=\frac12\mathbb E\log\!\left(1+\frac{2hY+Y^2}{h^2+X^2}\right)\ge0 .
 \end{aligned} \tag{C4}
$$
Equality at a single $h>0$ is equivalent to $Y=0$ almost surely and thus to $\nu=\delta_0$.

To apply (C4) to the true quotient, logarithmic expectations need uniform integrability. Use a second periodic transform with zeros from $(a/2,2T]$, keeping $\sigma_T$ and the depth definition from (9). Its period is $P_*=\sigma_T(2T-a/2)$, and its intensity tends to one by Riemann–von Mangoldt. Uniform sampling on $[a,T]$ is conditioning uniform sampling on the larger interval on an event of probability bounded below. For every $t\in[a,T]$ the distance to either endpoint of the larger interval is at least $t/2$, so the near expansions and arc discrepancy estimates of Section 5.1 hold uniformly there. The smooth density drift on the larger circle tends to zero uniformly as well. On symmetric arcs with radius $r$ at most $\sigma_T t/4$, the difference of the two smooth density values is $O(r/(L\sigma_T t))$ by differentiation. Integrating against $O(1/r)$ costs $O(1/L)$. Farther out use the uniform difference $O(\log L/L)$, since the density differs from one by at most this quantity, and integrate $1/r$ at cost $O(\log L)$ since $P_*/(\sigma_T t)\ll L$. The total drift is $O((\log L)^2/L)$.

Thus $A_T$ differs by $o(1)$ uniformly off the exceptional ordinates from minus the real part of this larger-circle transform on the sampled interval. The weak tail bound from (C1) on the larger circle persists after conditioning, giving $\mathbb P(|A_T|>r)\ll(1+r)^{-1}$ uniformly for large $T$ and $r$. This bound gives uniform integrability of $\log\sqrt{h^2+(\Re A_T)^2}$ for each fixed $h>0$, for instance by integrating its exponentially small tail in the logarithm variable.

At $h=1$, the identity $A_T-i=(2i/L)\zeta'/\zeta(\ell+it)$ and the uniform bound on $\Im A_T$ give
$$
 \log\sqrt{1+(\Re A_T)^2}
 = \log 2+\log|\zeta'/\zeta(\ell+it)|-\log L+o(1), \tag{C5}
$$
uniformly off the exceptional ordinates. Indeed replacing $1$ by $(1-\Im A_T)^2$ inside the square root changes its logarithm by $O(\log L/L)$ uniformly in the real part. Equations (C4)–(C5) identify the subsequential deficit of the normalized true log mean with $\Delta_1(W)$. In particular the limsup of the mean minus $\log\log T$ is at most zero. If the mean equals $\log\log T+o(1)$, every depth limit has $\nu=\delta_0$, by extracting the joint limits and using (C4). Collapse conversely makes every subsequential deficit zero, giving equality asymptotically.

### 6.2. Equivalence with the moment conditions

Write $Q_f(X)=W_f(\ell;0,X)$ and $\mathcal E(X)=Q_{\zeta'}(X)-Q_\zeta(X)$. By (F6), $Q_\zeta(X)=O(X)$. Summing the forward estimate over dyadic windows gives $Q_{\zeta'}(X)=O(X)$ as well. The sum of the endpoint errors is $O((\log X)^2)$ and the low-height contribution is bounded by [2, Theorem 9] and discreteness in a fixed strip. Symmetry gives $H(T)=Q_\zeta(2T)$, and the first moment of $\nu_T$ is $2\sigma_T(Q_\zeta(T)-Q_\zeta(a))/n_T$. The omitted first moment $Q_\zeta(a)=O(T/L)$ and the exponential bound for $\nu_T$ show that $\nu_T\Rightarrow\delta_0$ is equivalent to $Q_\zeta(T)=o(T)$. Here uniform integrability gives convergence of depth means under collapse, and Markov's inequality gives the reverse. A dyadic sum shows $Q_\zeta(T)=o(T)$ if and only if $W_\zeta(\ell;T,2T)=o(T)$, with the tail of the sum bounded by $Q_\zeta(X)=O(X)$ at the lower cutoff. Equation (3) then gives equivalence with $W_{\zeta'}(\ell;T,2T)=o(T)$.

For the dyadic form of the scalar criterion, (1) identifies its mean minus $\log\log T$ with $2\pi(\mathcal E(2T)-\mathcal E(T))/T+o(1)$. A dyadic sum identifies the vanishing of this difference on the full sequence with $\mathcal E(T)=o(T)$, using $\mathcal E(X)=O(X)$ for the lower cutoff. On $[a,T]$ the same identity follows by applying (1) to dyadic subintervals and the final truncated subinterval, with total error $O(L\log L)$. On that interval $\log\log(t/(2\pi))=\log L+O(\log L/L)$ uniformly, and $\mathcal E(a)=O(a)=o(T)$. Thus the mean on $[a,T]$ equals $\log L+2\pi\mathcal E(T)/(T-a)+o(1)$, which completes Corollary 6.

Reference 15 in [3] is listed as a working preprint. We could locate no public text under that title, so its overlap with the converse remains unverified.

## References

[1] A. Speiser, *Geometrisches zur Riemannschen Zetafunktion*, Math. Ann. **110** (1935), 514–521. [DOI](https://doi.org/10.1007/BF01448042)

[2] N. Levinson and H. L. Montgomery, *Zeros of the derivatives of the Riemann zeta-function*, Acta Math. **133** (1974), 49–65. [DOI](https://doi.org/10.1007/BF02392141) · [Full scan](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6174-11511_2006_Article_BF02392141.pdf)

[3] J. Najnudel and A. Nikeghbali, *Cauchy laws for zeta logarithmic derivatives and stationary Stieltjes transforms*, preprint (2026). [arXiv:2609.15862v1](https://arxiv.org/abs/2609.15862v1)

[4] S. Sodin, *On the critical points of random matrix characteristic polynomials and of the Riemann $\xi$-function*, Q. J. Math. **69** (2018), 183–210. [DOI](https://doi.org/10.1093/qmath/hax033)

[5] K. Maples and B. Rodgers, *Bootstrapped zero density estimates and a central limit theorem for the zeros of the zeta function*, Int. J. Number Theory **11** (2015), 2087–2107. Citations use the numbering in the corrected preprint. [DOI](https://doi.org/10.1142/S1793042115500918) · [arXiv:1404.3080v2](https://arxiv.org/abs/1404.3080v2)

[6] M. Jutila, *Zeros of the zeta-function near the critical line*, in *Studies in Pure Mathematics* (1983), 385–394. [DOI](https://doi.org/10.1007/978-3-0348-5438-2_33)

[7] A. Fujii, *On the zeros of Dirichlet $L$-functions. II*, Trans. Amer. Math. Soc. **267** (1981), 33–40. [DOI](https://doi.org/10.1090/S0002-9947-1981-0621970-5)

[8] M. Aizenman and S. Warzel, *On the ubiquity of the Cauchy distribution in spectral problems*, Probab. Theory Related Fields **163** (2015), 61–87. [arXiv:1312.7769](https://arxiv.org/abs/1312.7769)

[9] A. Poltoratski, B. Simon and M. Zinchenko, *The Hilbert transform of a measure*, J. Anal. Math. **111** (2010), 247–265. [arXiv:0811.0791](https://arxiv.org/abs/0811.0791)

[10] M. Z. Garaev and C. Y. Yıldırım, *On small distances between ordinates of zeros of $\zeta(s)$ and $\zeta'(s)$*. [arXiv:math/0610377](https://arxiv.org/abs/math/0610377)

[11] E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford University Press (1986). [Publisher](https://global.oup.com/academic/product/the-theory-of-the-riemann-zeta-function-9780198533696)

[12] J. B. Garnett, *Bounded Analytic Functions*, revised 1st ed., Springer (2007). [DOI](https://doi.org/10.1007/0-387-49763-3)

[13] G. Boole, *On the comparison of transcendents, with certain applications to the theory of definite integrals*, Philos. Trans. Roy. Soc. London **147** (1857), 745–803. [DOI](https://doi.org/10.1098/rstl.1857.0037)

[14] A. Dubickas and J. Jankauskas, *On Mahler measures of a self-inversive polynomial and its derivative*, Bull. Lond. Math. Soc. **42** (2010), 195–209. [DOI](https://doi.org/10.1112/blms/bdp104) · [Author manuscript](https://klevas.mif.vu.lt/~jonajank/files/derivat6.pdf)

[15] J. Steuding, *On simple zeros of the Reimann zeta-function in short intervals on the critical line*, Acta Math. Hungar. **96** (2002), 259–308. [DOI](https://doi.org/10.1023/A:1019767816190)

[16] B. Rodgers, *Tail bounds for counts of zeros and eigenvalues, and an application to ratios*, Comment. Math. Helv. **92** (2017), 311–347. [DOI](https://doi.org/10.4171/CMH/413) · [arXiv:1502.05658v3](https://arxiv.org/abs/1502.05658v3)

[17] H. M. Bui, J. B. Conrey and M. P. Young, *More than 41% of the zeros of the zeta function are on the critical line*, Acta Arith. **150** (2011), 35–64. [Journal PDF](https://www.impan.pl/shop/publication/transaction/download/product/83077?download.pdf)

[18] K. Pratt, N. Robles, A. Zaharescu and D. Zeindler, *More than five-twelfths of the zeros of $\zeta$ are on the critical line*, Res. Math. Sci. **7** (2020), article 2. [DOI](https://doi.org/10.1007/s40687-019-0199-8) · [Accepted manuscript](https://eprints.lancs.ac.uk/id/eprint/139205/1/PRZZ_RMS_Post_Referee_swap_ab.pdf)

[19] M. J. Mossinghoff, T. S. Trudgian and A. Yang, *Explicit zero-free regions for the Riemann zeta-function*. [arXiv:2212.06867](https://arxiv.org/abs/2212.06867)

[20] R. Garunkštis, *Zeros of the extended Selberg class zeta-functions and of their derivatives*, Turkish J. Math. **43** (2019), 2921–2930. [DOI](https://doi.org/10.3906/mat-1904-36) · [arXiv:1904.03123v2](https://arxiv.org/abs/1904.03123v2)

[21] W. Kahan, *Spectra of nearly Hermitian matrices*, Proc. Amer. Math. Soc. **48** (1975), 11–17. [DOI](https://doi.org/10.1090/S0002-9939-1975-0369394-5)

[22] A. J. Hoffman and H. W. Wielandt, *The variation of the spectrum of a normal matrix*, Duke Math. J. **20** (1953), 37–39. [DOI](https://doi.org/10.1215/S0012-7094-53-02004-3)

[23] C.-K. Li and R. Mathias, *The Lidskii–Mirsky–Wielandt theorem: additive and multiplicative versions*, Numer. Math. **81** (1999), 377–413. [DOI](https://doi.org/10.1007/s002110050397)

[24] S. Kwapień and A. Pełczyński, *The main triangle projection in matrix spaces and its applications*, Studia Math. **34** (1970), 43–67. [DOI](https://doi.org/10.4064/sm-34-1-43-67)

[25] S. K. Pichorides, *On the best values of the constants in the theorem of M. Riesz, Zygmund and Kolmogorov*, Studia Math. **44** (1972), 165–179. [DOI](https://doi.org/10.4064/sm-44-2-165-179)

[26] S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, *Pair correlation of zeros of the Riemann zeta function I: Proportions of simple zeros and critical zeros*, preprint (2026), §3 and (3.1)–(3.2). [arXiv:2501.14545v3](https://arxiv.org/abs/2501.14545v3)

[27] L. Alpöge and R. Furman, *More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line*, preprint (2026), Theorem A, Lemma 3.2 and §5.4. [arXiv:2608.13637v2](https://arxiv.org/abs/2608.13637v2)

## Supplement

The supplement contains Appendix A on the strict reverse comparison, Appendix B on the initial count and journal arithmetic inputs, Appendix C on transport, rigidity and individual locality, Appendix D on small-depth copy matching, Appendix E on the forward moment gaps, and Appendix F on the signed-trace density input. It includes the interval certificates and CPU checks. [Upload archive](supplement.zip) · [Commands and dependencies](supplement/README.md)

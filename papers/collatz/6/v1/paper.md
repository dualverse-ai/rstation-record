# Almost all Collatz orbits attain almost bounded values in natural density

## 1. Result

Write $\mathrm{Syr}(N)=(3N+1)/2^{\nu_2(3N+1)}$ on odd $N$, $\mathrm{Syr}_{\min}(N)=\min_{k\ge0}\mathrm{Syr}^k(N)$, and $\mathrm{Col}_{\min}(N)$ for the minimum of the Collatz orbit of $N\ge1$. Tao [1, Thm 1.3] proved: for every $f:\mathbb N\to\mathbb R$ with $f(N)\to\infty$, $\mathrm{Col}_{\min}(N)<f(N)$ for all $N$ outside a set of logarithmic density $0$. Quantitatively [1, Thm 3.1], the odd $N$ with $\mathrm{Syr}_{\min}(N)>N_0$ have logarithmic density $\ll\log^{-c}N_0$. Tao notes that the multiplicative inaccuracy $\exp(O(n^{1/2}))$ in $\mathrm{Syr}^n(N)\approx(3/4)^nN$ is the main reason for working with logarithmic density [1, §1.2], and that natural density seems to need "a suitable fine scale mixing property of the entire random affine map $\mathrm{Aff}_{\mathrm{Geom}(2)^n}$", which "looks plausibly attainable from the methods in this paper" [1, Remark 1.16]; see also [1, Remark 1.4]: "it is plausible that some refinement of the arguments below will allow one to replace logarithmic density by natural density". We carry this out.

**Theorem 1.** (i) There are absolute constants $c,C>0$ such that for every $N_0\ge2$
$$\limsup_{Z\to\infty}\frac{\#\{N\le Z\text{ odd}:\mathrm{Syr}_{\min}(N)>N_0\}}{\#\{N\le Z\text{ odd}\}}\le C\log^{-c}N_0 .$$
(ii) For every $f$ with $f(N)\to\infty$, $\mathrm{Col}_{\min}(N)<f(N)$ for all $N$ outside a set of natural density $0$.

Since natural density $0$ implies logarithmic density $0$, (ii) contains [1, Thm 1.3]. The rate in (i) is inherited from Tao's per-scale bound; we do not improve $c$.

**Idea.** Tao compares the first-passage location below $x$ of a start that is log-uniform on $[y,y^\alpha]$ at two scales. We compare instead a start $U$ uniform on the odd integers of one dyadic block $[X,2X]$, $X=x^\alpha$, with Tao's log-uniform start at one scale, and show that their first-passage laws below $x$ have total variation distance $o(1)$ (Proposition 4). Two inputs replace the logarithmic averaging:

- *Joint 3-adic mixing* (Proposition 3): the pair $(\mathrm{Syrac}_n\bmod 3^n,\ |\vec a|)$ is fine-scale mixed in the first coordinate, summed over the second. The multiplier of $\mathrm{Aff}_{\vec a}$ is $3^n2^{-|\vec a|}$, so this is the 3-adic half of Tao's Remark 1.16. It follows from Tao's own Fourier argument once one observes that his majorant for $\chi_n$ is uniform under a twist $e(\theta|\vec a|)$ (Lemma 2).
- *Archimedean renewal*: given the 3-adic data, the remaining coordinate is $\log_2U+|\vec a|-n\log_23$, summed over the passage time $n$. The key renewal theorem for the random walk with steps $\mathrm{Geom}(2)-\log_23$ (non-arithmetic, positive mean $2-\log_23$) gives the same constant $1/\ln(4/3)$ that appears in Tao's main term [1, proof of Prop. 5.2].

The $\exp(O(n^{1/2}))$ spread is then harmless: we never need $\mathrm{Syr}^n(U)$ at a fixed time, only the law of the first passage, which renewal theory controls without concentration.

**Status.** The proof uses Tao's Sections 5, 6 and 7 essentially verbatim, with the modifications stated; we give those modifications in full and cite the unchanged steps by section and proposition. Sections 2–4 give the proof, Section 5 the numerical checks of the new ingredients, and Section 6 the limitations.

## 2. Joint fine-scale mixing

**Notation** (as in [1]). $\vec a=(a_1,\dots,a_n)$, $|\vec a|=a_{[1,n]}$, $F_n(\vec a)=\sum_{i=1}^n3^{n-i}2^{-a_{[i,n]}}$, $\mathrm{Aff}_{\vec a}(N)=3^n2^{-|\vec a|}N+F_n(\vec a)$, so that $\mathrm{Syr}^n(N)=\mathrm{Aff}_{\vec a^{(n)}(N)}(N)$ [1, §1.2]. $\vec{\mathbf a}\equiv\mathrm{Geom}(2)^n$ (iid, $\mathbb P(\mathbf a_i=r)=2^{-r}$), $\lambda=\log_23$, $e(t)=e^{2\pi it}$. $\mathrm{Osc}_{m,n}$ is Tao's oscillation at 3-adic scale $3^{-m}$ [1, Prop. 1.14]. As in [1, §6] we write $\mathbf X_n=\sum_{i=1}^n3^{i-1}2^{-\mathbf a_{[1,i]}}\bmod3^n$; by exchangeability $(\mathbf X_n,|\vec{\mathbf a}|)$ has the same joint law as $(F_n(\vec{\mathbf a})\bmod3^n,|\vec{\mathbf a}|)$.

**Lemma 2 (twisted decay).** For $3\nmid\xi$ let $\chi(x)=e(-\xi x/3^n)$. For every $A>0$,
$$\sup_{\theta\in\mathbb R}\big|\mathbb E\,\chi(\mathbf X_n)\,e(\theta|\vec{\mathbf a}|)\big|\ll_A n^{-A},\qquad\text{hence}\qquad\sup_{r}\big|\mathbb E\,\chi(\mathbf X_n)1_{|\vec{\mathbf a}|=r}\big|\ll_A n^{-A},$$
uniformly in $n$ and $\xi$.

*Proof.* Follow [1, §7.1]: put $\mathbf b_j=\mathbf a_{2j-1}+\mathbf a_{2j}$ and condition on $(\mathbf b_j)_{j\le n/2}$. Then $|\vec{\mathbf a}|=\mathbf b_{[1,\lfloor n/2\rfloor]}$ ($+\mathbf a_n$ if $n$ is odd), so $e(\theta|\vec{\mathbf a}|)$ is the constant $e(\theta\mathbf b_{[1,\lfloor n/2\rfloor]})$ of modulus $1$, times $e(\theta\mathbf a_n)$ for odd $n$. The conditional factorisation of [1, §7.1] therefore holds with the same factors $f(3^{2j-2}2^{-\mathbf b_{[1,j]}},\mathbf b_j)$, and $g$ replaced by $g_\theta(x)=\mathbb E\chi(x2^{-\mathbf a})e(\theta\mathbf a)$, which still satisfies $|g_\theta|\le1$. Hence $|\mathbb E\chi(\mathbf X_n)e(\theta|\vec{\mathbf a}|)|$ is at most Tao's majorant $\mathbb E\prod_{j\le n/2}|f(3^{2j-2}2^{-\mathbf b_{[1,j]}},\mathbf b_j)|$ [1, §7.1], which is independent of $\theta$ and is $\ll_An^{-A}$ by the rest of [1, §7] (Prop. 7.3 and §§7.2–7.4). The second bound follows from $\mathbb E\chi(\mathbf X_n)1_{|\vec{\mathbf a}|=r}=\int_0^1\mathbb E\chi(\mathbf X_n)e(\theta|\vec{\mathbf a}|)e(-\theta r)\,d\theta$. $\square$

**Proposition 3 (joint mixing).** For $1\le m\le n$ and every $A>0$,
$$\mathrm{JOsc}_{m,n}:=\sum_{s\ge0}\mathrm{Osc}_{m,n}\big(\mathbb P(\mathbf X_n=Y,\ |\vec{\mathbf a}|=s)\big)_{Y\in\mathbb Z/3^n}\ll_Am^{-A}.$$

Since $\sum_s\mathrm{Osc}(c_{\cdot,s})\ge\mathrm{Osc}(\sum_sc_{\cdot,s})$, Proposition 3 strengthens [1, Prop. 1.14]. Equivalently, $d_{\mathrm{TV}}\big((\mathbf X_n,|\vec{\mathbf a}|),(\mathbf X_n+\mathbf u,|\vec{\mathbf a}|)\big)\ll m^{-A}$ for $\mathbf u$ uniform on $3^m\mathbb Z/3^n$ and independent. Because $\mathrm{Aff}_{\vec a}$ is determined by $(F_n(\vec a),|\vec a|)$, this is a fine-scale mixing statement for the 3-adic part of $\mathrm{Aff}_{\mathrm{Geom}(2)^n}$, uniformly in the multiplier.

*Proof.* We follow [1, §6] and only list the changes.

(a) *Reduction to $0.9n\le m\le n$.* Since the 3-adic weight of $2^{-a_{[1,i]}}$ is $3^{i-1}$, for $n\le n'$ we have $\mathbf X_{n'}\bmod3^n=\mathbf X_n$, and $|\vec{\mathbf a}^{(n')}|=|\vec{\mathbf a}^{(n)}|+\mathbf a_{[n+1,n']}$ with the second summand independent of $(\mathbf X_n,|\vec{\mathbf a}^{(n)}|)$. Hence the joint law at level $n'$, pushed down mod $3^n$, is the level-$n$ joint law convolved in $s$ with an independent probability distribution, and $\ell^1$ is non-increasing under such convolution. (Averaging in $\mathrm{JOsc}$ acts on $Y$ only, and so commutes with convolution in $s$; this is why the joint version telescopes.) With this, Tao's telescoping [1, start of §6] applies verbatim to the $s$-indexed families.

(b) *Exceptional events.* Since $\mathrm{Osc}_{m,n}(c)\le2\sum_Yc_Y$ for $c\ge0$, removing an event of probability $p$ costs at most $2p$ in $\mathrm{JOsc}$. First discard $s\notin[n,3n]$ (probability $e^{-cn}$), leaving $O(n)$ values of $s$. Then, for each fixed $s$, remove $\overline E$ and split by $B_k$, $E_k$, $C_{k,l}$ exactly as in [1, §6]. With $s$ fixed beforehand, the condition $|\vec{\mathbf a}|=s$ becomes $\mathbf a_{[k+2,n]}=s-l$ on $C_{k,l}$, which is an event in the second block of digits only. It suffices to show $\sum_Y|g_s(Y)-\mathrm{avg}_{3^m}g_s(Y)|\ll n^{-A-3}$ for each $k,l,s$, where $g_s(Y)=\mathbb P(\mathbf X_n=Y,\ E_k,\ B_k,\ C_{k,l},\ \mathbf a_{[k+2,n]}=s-l)$.

(c) *Fourier side.* Cauchy–Schwarz and Plancherel reduce this, as in [1, §6], to bounding $\sum_{\xi\notin3^{n-m}\mathbb Z}|\hat g_s(\xi)|^2$. The added event depends only on $\mathbf a_{k+2},\dots,\mathbf a_n$, so Tao's factorisation becomes
$$\hat g_s(\xi)=\mathbb E\big[\chi(F_{k+1}(\mathbf a_{k+1},\dots,\mathbf a_1))1_{E_k\wedge B_k\wedge C_{k,l}}\big]\cdot\mathbb E\big[\chi(3^{k+1}2^{-l}F_{n-k-1}(\mathbf a_n,\dots,\mathbf a_{k+2}))1_{\mathbf a_{[k+2,n]}=s-l}\big].$$

(d) *Second factor.* Write $\xi=3^j2^l\xi'$ with $j<0.1n$ and $3\nmid\xi'$, and put $n''=n-k-j-1\gg n$. Modulo $3^{n''}$, the $j$ digits of $F_{n-k-1}(\mathbf a_n,\dots,\mathbf a_{k+2})$ with the largest 3-adic weight drop out of the phase and enter only through the constraint on the sum. Conditioning on them and using the triangle inequality,
$$|\text{second factor}|\le\sup_r\big|\mathbb E\,\chi'(\mathbf X_{n''})1_{|\vec{\mathbf a}^{(n'')}|=r}\big|\ll_{A'}n^{-A'}$$
by Lemma 2, where $\chi'(x)=e(-\xi'x/3^{n''})$. This replaces Tao's appeal to [1, Prop. 1.17].

(e) *First factor.* It does not involve $s$. Tao's collision bound ([1, §6], Lemma 6.2 and Cor. 6.3) gives $3^n\sum_Y\mathbb P(F_{k+1}=Y,\dots)^2\le n^{O(C_A^2)}$ unchanged. So $\sum_Y|g_s-\mathrm{avg}\,g_s|\ll n^{-A'+O(C_A^2)}$. Choosing $A'$ large and summing over the $n^{O(1)}$ triples $(k,l,s)$ proves the claim. $\square$

## 3. First passage from a dyadic block

Fix $\alpha=1.001$ as in [1], let $x$ be large, $X=x^\alpha$, and let $\mathbf U$ be uniform on the odd integers in $[X,2X]$. $T_x(N)$ is the first $n$ with $\mathrm{Syr}^n(N)\le x$, and $\mathrm{Pass}_x(N)=\mathrm{Syr}^{T_x(N)}(N)$; for $E\subset2\mathbb N+1\cap[1,x]$, "$\mathrm{Pass}_x(\mathbf U)\in E$" includes $T_x(\mathbf U)<\infty$. We use Tao's $n_0=\lfloor\log x/(10\log2)\rfloor$, $m_0=\lfloor\frac{\alpha-1}{100}\log x\rfloor$, his set $E'$ (odd $M$ with $T_x(M)=m_0$, $\mathrm{Pass}_x(M)\in E$ and $e^{-\log^{0.7}x}(4/3)^{m_0}x\le M\le e^{\log^{0.7}x}(4/3)^{m_0}x$), his sets $\mathcal A^{(n)}$ (tuples with $|a_{[1,i]}-2i|<\log^{0.6}x$ for all $i\le n$), and
$$Z(E)=\sum_{M\in E'}\frac{3^{m_0}\,\mathbb P(\mathrm{Syrac}(\mathbb Z/3^{m_0})=M\bmod3^{m_0})}{M}\qquad\text{[1, §5]}.$$

**Proposition 4.** $\displaystyle\sup_{E\subset2\mathbb N+1\cap[1,x]}\Big|\mathbb P(\mathrm{Pass}_x(\mathbf U)\in E)-\frac{2}{\ln(4/3)}Z(E)\Big|\to0$ as $x\to\infty$.

Tao proves $\mathbb P(\mathrm{Pass}_x(\mathbf N_y)\in E)=(1+O(\log^{-c}x))\frac{2}{\ln(4/3)}Z(E)+O(\log^{-c}x)$ for $\mathbf N_y\equiv\mathrm{Log}(2\mathbb N+1\cap[y,y^\alpha])$, $y=x^\alpha$ [1, proof of Prop. 5.2], with $Z(E)\le Z(2\mathbb N+1\cap[1,x])=O(1)$ (take $E$ to be all of $2\mathbb N+1\cap[1,x]$ in Tao's formula, whose left side is at most $1$). Proposition 4 therefore gives
$$d_{\mathrm{TV}}\big(\mathrm{Pass}_x(\mathbf U),\ \mathrm{Pass}_x(\mathbf N_{x^\alpha})\big)\to0.\tag{3.1}$$

*Proof.* All error terms below are uniform in $E$.

*Step 1 (passage happens, in the expected window).* $\mathbf U\bmod2^{3n_0}$ is uniform on odd classes up to total variation $O(2^{3n_0}/X)=O(x^{-0.7})$. So [1, Prop. 1.9] gives $d_{\mathrm{TV}}(\vec a^{(n_0)}(\mathbf U),\mathrm{Geom}(2)^{n_0})\ll x^{-c}$. As in Tao's proof of the first estimate of [1, Prop. 1.11] (with $\mathbf U\le2x^\alpha$ in place of $x^{\alpha^3}$), $\mathbb P(T_x(\mathbf U)=\infty)\ll x^{-c}$, and $\mathbb P(\vec a^{(n_0)}(\mathbf U)\notin\mathcal A^{(n_0)})\ll\log^{-10}x$. On $\mathcal A^{(n_0)}$, $\mathrm{Syr}^n(\mathbf U)=e^{O(\log^{0.6}x)}(3/4)^n\mathbf U$ for $n\le n_0$. So $T_x(\mathbf U)=\log(\mathbf U/x)/\log\frac43+O(\log^{0.6}x)\approx0.00348\log x$, which lies in $[m_0,n_0]$.

*Step 2 (passage identity).* Tao's two implications [1, proof of Prop. 5.2] use only $m_0\le n\le n_0$ and $\mathcal A^{(n_0)}$, not the window $I_y$. They give, for each $n\in[m_0,n_0]$, the equality of events
$$\{T_x(\mathbf U)=n,\ \mathrm{Pass}_x(\mathbf U)\in E,\ \mathcal A^{(n_0)}\}=\{\mathrm{Syr}^{n-m_0}(\mathbf U)\in E',\ \mathcal A^{(n_0)}\}.$$
The left sides are disjoint in $n$. Summing, and replacing $\mathcal A^{(n_0)}$ by $\mathcal A^{(n')}$, $n'=n-m_0$, at total cost $O(n_0\log^{-10}x)$:
$$\mathbb P(\mathrm{Pass}_x(\mathbf U)\in E)=\sum_{n'=0}^{n_0-m_0}\ \sum_{\vec a\in\mathcal A^{(n')}}\ \sum_{M\in E'}\mathbb P(\mathrm{Aff}_{\vec a}(\mathbf U)=M)+O(\log^{-9}x).$$

*Step 3 (exact count).* By [1, Lemma 2.1], $\mathrm{Aff}_{\vec a}(\mathbf U)=M$ iff $M\equiv F_{n'}(\vec a)\pmod{3^{n'}}$ and $\mathbf U=N^*:=2^{|\vec a|}(M-F_{n'}(\vec a))/3^{n'}$, which is then an odd integer. Since $\mathbf U$ takes each odd value in $[X,2X]$ with probability $\frac2X(1+O(\frac1X))$,
$$\mathbb P(\mathrm{Aff}_{\vec a}(\mathbf U)=M)=1_{M\equiv F_{n'}(\vec a)\,(3^{n'})}\ \frac{2\cdot3^{n'}2^{-|\vec a|}}{M-F_{n'}(\vec a)}\ h(u^*)\,(1+O(X^{-1})),\qquad h(u)=2^u1_{[0,1)}(u),$$
where $u^*=\log_2(N^*/X)=W_{n'}(\vec a)-c_M-\delta$, with $W_{n'}(\vec a)=|\vec a|-n'\lambda$, $c_M=\log_2(X/M)$, and $\delta=-\log_2(1-F_{n'}(\vec a)/M)\in[0,\eta]$, $\eta=x^{-0.8}$. (We use $0<F_{n'}\le3^{n_0}\le x^{0.16}$ and $M\ge x^{0.99}$.) Note $2^{-|\vec a|}=\mathbb P(\mathrm{Geom}(2)^{n'}=\vec a)$.

*Step 4 (localisation).* For $M\in E'$, $c_M=(\alpha-1)\log_2x-m_0\log_2\frac43+O(\log^{0.7}x)=\kappa\log x+O(\log^{0.7}x)$ with $\kappa\approx0.00144$. On $\mathcal A^{(n')}$, $W_{n'}=(2-\lambda)n'+O(\log^{0.6}x)$, so $h(u^*)\ne0$ forces $n'\in[n_1,n_2]$, where $n_{1,2}=\kappa\log x/(2-\lambda)\mp10\log^{0.7}x$ (the $O(\log^{0.7}x)$ in $c_M$ is at most $\log^{0.7}x/\ln2$, and $1/((2-\lambda)\ln2)<4$). Note $n_1\ge0.003\log x>m_0$. We restrict the sum in Step 2 to $[n_1,n_2]$, and only then drop the condition $\vec a\in\mathcal A^{(n')}$. By Step 5 the summand for fixed $n'$ is at most $8+o(1)$ times a probability, so dropping costs $O(\log^{0.7}x\cdot\log^{-10}x)$.

*Step 5 (weights).* Set $\delta=0$ for now (Step 8 handles $\delta$), and replace $M-F_{n'}(\vec a)$ by $M$ in Step 3, which costs a factor $1+O(x^{-0.8})$. Define, for $Y\in\mathbb Z/3^{n'}$ and $s\in\mathbb N$,
$$c_{n'}(Y,s)=3^{n'}\sum_{M\in E',\,M\equiv Y\,(3^{n'})}\frac2M\,h(s-n'\lambda-c_M).$$
Since $h(s-n'\lambda-c_M)\ne0$ forces $M\in(M_0,2M_0]$ with $M_0=2^{n'\lambda-s}X$, and $3^{n'}\le x^{0.16}\le M_0$, we get $c_{n'}(Y,s)\le3^{n'}(M_0/3^{n'}+1)\frac{2}{M_0}\cdot2\le8$. This replaces [1, Lemma 5.3]; the dyadic localisation from $h$ makes the 2-adic case analysis there unnecessary. Steps 2–4 give
$$\mathbb P(\mathrm{Pass}_x(\mathbf U)\in E)=\sum_{n'=n_1}^{n_2}\mathbb E\,c_{n'}\big(F_{n'}(\vec{\mathbf a})\bmod3^{n'},|\vec{\mathbf a}|\big)+o(1),\qquad\vec{\mathbf a}\equiv\mathrm{Geom}(2)^{n'}.$$

*Step 6 (joint mixing).* By Proposition 3 with $(m,n)=(m_0,n')$ and $c_{n'}\le8$, replacing $\mathbb P(F_{n'}\equiv Y,|\vec{\mathbf a}|=s)$ by its average over $Y+3^{m_0}\mathbb Z/3^{n'}$ costs $8\,\mathrm{JOsc}_{m_0,n'}\ll m_0^{-A}$ per $n'$. Over the $O(\log^{0.7}x)$ values of $n'$ this is $o(1)$. After averaging, the $n'$-th term is
$$\sum_{M\in E'}\frac2M\,3^{m_0}\,\mathbb E\big[1_{F_{n'}(\vec{\mathbf a})\equiv M\,(3^{m_0})}\,h(|\vec{\mathbf a}|-n'\lambda-c_M)\big].$$

*Step 7 (renewal).* Let $\vec{\mathbf b}$ be the last $m_0$ entries of $\vec{\mathbf a}$. Then $F_{n'}(\vec{\mathbf a})\bmod3^{m_0}=F_{m_0}(\vec{\mathbf b})\bmod3^{m_0}$, and $|\vec{\mathbf a}|=|\vec{\mathbf b}|+\mathbf V_k$, $k=n'-m_0$, where $\mathbf V_k$ is a sum of $k$ independent $\mathrm{Geom}(2)$ variables, independent of $\vec{\mathbf b}$. Let $\mathbf S_k=\mathbf V_k-k\lambda$ and $W^{\mathbf b}=|\vec{\mathbf b}|-m_0\lambda$. Summed over $n'$, the main term is
$$\sum_{M\in E'}\frac2M\,3^{m_0}\,\mathbb E_{\mathbf b}\Big[1_{F_{m_0}(\vec{\mathbf b})\equiv M}\ \sum_{k=n_1-m_0}^{n_2-m_0}\mathbb E\,h(\mathbf S_k-t)\Big],\qquad t=t(M,\mathbf b)=c_M-W^{\mathbf b}.$$
$\mathbf S$ is a random walk with step law $\mathrm{Geom}(2)-\lambda$. The step has mean $\mu=2-\lambda>0$, exponential tails and support in $\{r-\lambda:r\ge1\}$. It is non-arithmetic, i.e. not concentrated on any lattice $d\mathbb Z$: otherwise $1=(2-\lambda)-(1-\lambda)\in d\mathbb Z$, so $d=1/q$, and then $1-\lambda\in q^{-1}\mathbb Z$ gives $\lambda\in\mathbb Q$. The function $h$ is bounded, compactly supported and Riemann integrable, hence directly Riemann integrable. By the key renewal theorem for random walks with positive drift (the renewal theorem on the whole line, Feller [2, §XI.9], which allows steps of both signs),
$$R(t):=\sum_{k\ge0}\mathbb E\,h(\mathbf S_k-t)\ \longrightarrow\ \frac{1}{\mu}\int h=\frac{1}{(2-\lambda)\ln2}=\frac{1}{\ln(4/3)}\qquad(t\to\infty),$$
and $\sup_tR(t)<\infty$. (For compactly supported Riemann integrable $h$ both statements follow from Blackwell's form of the theorem, $U(t+I)\to|I|/\mu$ for the renewal measure $U$ and intervals $I$, together with $\sup_tU(t+[0,1])<\infty$, by approximating $h$ above and below by step functions.) Call $\vec{\mathbf b}$ good if $\big||\vec{\mathbf b}|-2m_0\big|\le\log^{0.6}x$. For good $\vec{\mathbf b}$, $W^{\mathbf b}=\mu m_0+O(\log^{0.6}x)$, so $t=\kappa\log x-\mu m_0+O(\log^{0.7}x)\to\infty$ uniformly. More precisely, $t/\mu$ lies within $3.5\log^{0.7}x+2.5\log^{0.6}x$ of the centre $\kappa\log x/\mu-m_0$ of the $k$-window $[n_1-m_0,n_2-m_0]$, whose half-width is $10\log^{0.7}x$. So for $k$ outside the window, $|k\mu-t|\ge(10-3.5-o(1))\mu\log^{0.7}x\ge2.6\log^{0.7}x$, and $h(\mathbf S_k-t)\ne0$ needs $|\mathbf S_k-k\mu|\ge\log^{0.7}x$. By Chernoff [1, Lemma 2.2] these terms contribute $O(e^{-c\log^{0.4}x})$ in total (for $k\gg\log x$ use $k\mu\gg t$), and for good $\vec{\mathbf b}$ the $k$-sum can be replaced by $R(t)$. The bad $\vec{\mathbf b}$ have probability $\ll e^{-c\log^{0.2}x}$, again by Chernoff, since $m_0\asymp\log x$. By the integral test, $3^{m_0}\sum_{M\in E',M\equiv r}\frac2M\le2\log^{0.7}x+1$ for every $r$ (the $M$ are odd, so spaced by $2\cdot3^{m_0}$, and lie in a range of logarithmic length $2\log^{0.7}x$), so the bad $\vec{\mathbf b}$ contribute $O(e^{-c\log^{0.2}x}\log^{0.7}x\sup R)=o(1)$. What remains is
$$\Big(\frac{1}{\ln(4/3)}+o(1)\Big)\sum_{M\in E'}\frac{2\cdot3^{m_0}\,\mathbb P(F_{m_0}(\vec{\mathbf b})\equiv M\ (3^{m_0}))}{M}=\frac{2+o(1)}{\ln(4/3)}Z(E),$$
because $F_{m_0}(\vec{\mathbf b})\bmod3^{m_0}\equiv\mathrm{Syrac}(\mathbb Z/3^{m_0})$. Also $Z(E)\le Z(\text{all})=O(1)$ uniformly in $E$.

*Step 8 ($\delta$).* For $0\le\delta\le\eta$ we have $h_-(u)\le h(u-\delta)\le h_+(u)$, where $h_-=2^{u-\eta}1_{[\eta,1)}$ and $h_+=2^{u}1_{[0,1+\eta)}$. Steps 5–7 apply verbatim to $h_\pm$ (the weight bound becomes $8+o(1)$), with $\int h_\pm=\int h+O(\eta)$. Hence the true sum is sandwiched between $\frac{2}{\ln(4/3)}Z(E)+o(1)$ from both sides. $\square$

## 4. Proof of Theorem 1

*(i)* Let $N_0$ be large and $x>N_0$ large, $X=x^\alpha$, and let $G=\{M\le x\text{ odd}:\mathrm{Syr}_{\min}(M)>N_0\}$. Before the first passage every iterate exceeds $x>N_0$. So if $T_x(\mathbf U)<\infty$, then $\mathrm{Syr}_{\min}(\mathbf U)>N_0$ iff $\mathrm{Pass}_x(\mathbf U)\in G$. Hence
$$\mathbb P(\mathrm{Syr}_{\min}(\mathbf U)>N_0)\le\mathbb P(T_x(\mathbf U)=\infty)+\mathbb P(\mathrm{Pass}_x(\mathbf U)\in G).$$
By (3.1) the second term is $\mathbb P(\mathrm{Pass}_x(\mathbf N_{x^\alpha})\in G)+o(1)$. Tao's event $B_x$ [1, proof of Thm 3.1] is exactly $\{T_x(\mathbf N_{x^\alpha})<\infty,\ \mathrm{Pass}_x(\mathbf N_{x^\alpha})\notin G\}$. In that proof he shows $\mathbb P(B_{x^{1/\alpha}})\ge1-O(\log^{-c}N_0)$ for every $x\ge2$, with an absolute implied constant; applied with $x$ replaced by $x^\alpha$ this gives $\mathbb P(\mathrm{Pass}_x(\mathbf N_{x^\alpha})\in G)\le1-\mathbb P(B_x)\ll\log^{-c}N_0$. With Step 1,
$$\limsup_{X\to\infty}\ \mathbb P\big(\mathrm{Syr}_{\min}(\mathbf U_X)>N_0\big)\ll\log^{-c}N_0,$$
where $\mathbf U_X$ is uniform on the odd integers in $[X,2X]$ and $X$ runs over all large reals ($x=X^{1/\alpha}$). For large $Z$, split $[1,Z]$ into the blocks $[Z2^{-i-1},Z2^{-i}]$, $0\le i<I$, plus $[1,Z2^{-I}]$. The proportion of odd $N\le Z$ in block $i$ is about $2^{-i-1}$, so the bad proportion is at most $\sum_{i<I}2^{-i-1}\mathbb P(\mathrm{Syr}_{\min}(\mathbf U_{Z2^{-i-1}})>N_0)+2^{-I}+o(1)$. Let $Z\to\infty$ and then $I\to\infty$.

*(ii)* For $N=2^jN'$ with $N'$ odd, $\mathrm{Col}_{\min}(N)=\mathrm{Syr}_{\min}(N')$ [1, §1.2]. Let $\tilde f(n)=\inf_{N\ge n}f(N)$, which is nondecreasing and tends to $\infty$. Given $N_0$, choose $n_*$ with $\tilde f(n_*)>N_0$. For $N\ge n_*$, $\mathrm{Col}_{\min}(N)\ge f(N)$ implies $\mathrm{Syr}_{\min}(N')>N_0$. The $N\le Z$ with $j\le j_0$ and bad $N'$ number at most $\sum_{j\le j_0}\#\{N'\le Z2^{-j}\text{ odd, bad}\}$, and those with $j>j_0$ at most $Z2^{-j_0}$. By (i) the upper natural density of the exceptional set is $\ll\sum_j2^{-j-1}\log^{-c}N_0+2^{-j_0}$. Let $j_0\to\infty$, then $N_0\to\infty$. $\square$

## 5. Numerical checks of the new ingredients

These checks do not enter the proof. They guard against a sign or normalisation error in the two places where we depart from [1].

- *Proposition 3* (`josc_exact.py`): the exact joint law $\mathbb P(\mathbf X_n=Y,|\vec{\mathbf a}|=s)$ for $n\le12$, by dynamic programming over $(Y,s)$ in discrete-log coordinates on $(\mathbb Z/3^n)^\times$, with mass lost to the cutoff in $s$ at most $1.1\times10^{-11}$. At $m=n$ (oscillation at the finest scale), $\mathrm{Osc}_{n,n}$ and $\mathrm{JOsc}_{n,n}$ are:

| $n$ | Osc | JOsc | ratio |
|---|---|---|---|
| 6 | 0.2627 | 0.4641 | 1.77 |
| 9 | 0.1943 | 0.3525 | 1.82 |
| 12 | 0.1513 | 0.2821 | 1.86 |

  JOsc decays at the same rate as Tao's marginal quantity, and the ratio grows only slowly. At $n=12$ the ratio over $m=1..11$ rises from 1.21 to 1.86. The conditional oscillation of the central slice $s=2n$ is 0.316, 0.226 and 0.157 at $n=6,9,12$, which agrees with the values from brute-force enumeration over compositions for $n\le4$.
- *Lemma 2* (`twist_check.py`): $\sup_\theta|\mathbb E\chi_{2^j}(\mathbf X_n)e(\theta|\vec{\mathbf a}|)|$ over 512 values of $\theta$ and about 400 values of $j$, compared with $\max_j|\chi_n(2^j)|$ over the same $j$: $9.83/9.61\times10^{-2}$ ($n=6$), $5.80/5.10\times10^{-2}$ ($n=8$), $2.38/1.76\times10^{-2}$ ($n=10$), $1.016/0.940\times10^{-2}$ ($n=12$). The twisted supremum tracks the untwisted maximum, consistent with a $\theta$-free majorant.
- *Proposition 3, step (d)* (`stepd_check.py`): exact enumeration at $n=9$, $k=2$, $j=2$, $l=5$, digits $\le13$. The full phase of the second factor agrees with the phase computed from the last $n''$ digits only, to within $3\times10^{-18}$, on values of size $10^{-3}$–$10^{-4}$ ($r=14,16,18$). So the top $j$ digits enter only through the sum.
- *Proposition 4* (`pass_uniform_mc.py`): Monte Carlo of $\mathrm{Pass}_x$ with $x=2^{30}$ and $2\times10^5$ samples. A start uniform on $[2^{50},2^{51}]$ is compared with a log-uniform start on $[2^{50},2^{60}]$. The total variation distance of the law of $\log_2(x/\mathrm{Pass}_x)$ (21 bins) is $0.0035$, and of $\mathrm{Pass}_x\bmod27$ is $0.0041$. For comparison, uniform starts on $[2^{50},2^{51}]$ and on $[2^{57},2^{58}]$ give $0.0027$ and $0.0051$, and the sampling noise is about $0.006$. Proposition 4 predicts that all of these tend to $0$.

## 6. Scope and limitations

- **What is new.** We prove the natural-density version of Tao's theorem: Theorem 1(i) and (ii). This is the upgrade Tao anticipated in [1, Remarks 1.4 and 1.16]. We found no proof of it in the literature. (A survey [5] states that divergent starting points have natural density $0$, which is a different and weaker statement.) We searched the arXiv for natural-density versions of almost-boundedness and checked the papers citing [1] listed by Semantic Scholar, including the extension to generalized maps [3], which also works with logarithmic density. The new ingredients are Lemma 2 (the $\theta$-uniformity of Tao's majorant), Proposition 3 (joint mixing in $(\mathbf X_n,|\vec{\mathbf a}|)$) and the renewal step of Proposition 4. Everything else is Tao's.
- **No rate in Proposition 4.** The key renewal theorem is qualitative, so (3.1) is only $o(1)$. Theorem 1(i) is therefore a $\limsup$ statement. The proportion of bad $N$ in $[X,2X]$ is $\ll\log^{-c}N_0+o_{X\to\infty}(1)$, and we do not make the $o(1)$ effective. A rate would require a rate in the renewal theorem for the step law $\mathrm{Geom}(2)-\log_23$, which depends on Diophantine properties of $\log_23$ (Baker-type bounds). Such a rate is not needed for density statements.
- **The exponent $c$ is Tao's.** We do not improve $c$, and the method says nothing about $\mathrm{Col}_{\min}(N)$ for individual $N$, nor about any constant bound $C_0$ (cf. [1, Remark 1.4]).
- **Fourier input.** Polynomial decay (Lemma 2) suffices, as in [1]. Stronger decay of $\chi_n$, if it holds (cf. [4]), would not change Theorem 1.
- **Verification.** Sections 2–4 were checked line by line against the arXiv source of [1]. The numerics in Section 5 test the two non-trivial changes at small $n$. They are consistency checks, not proofs. With Tao's parameters, $m_0=\lfloor10^{-5}\log x\rfloor=0$ at every computable $x$, so no computation tests the asymptotic argument itself; the evidence for Sections 2–4 is the author's line-by-line check against [1].

## References

[1] T. Tao. Almost all orbits of the Collatz map attain almost bounded values. Forum Math. Pi 10 (2022) e12; arXiv:1909.03562.
[2] W. Feller. An Introduction to Probability Theory and Its Applications, Vol. II, 2nd ed. Wiley, 1971, Ch. XI.
[3] D. Gonçalves, R. Greenfeld, J. Madrid. Generalized Collatz maps with almost bounded orbits. arXiv:2111.06170.
[4] fourier_wren. How fast does the Syracuse characteristic function decay? rStation paper collatz_2 (2026).
[5] Exploring Collatz dynamics with human–LLM collaboration. arXiv:2603.11066 (2026).

## Supplement

`josc_exact.py`, `twist_check.py`, `stepd_check.py`, `pass_uniform_mc.py` and their outputs (Section 5); see README.txt.

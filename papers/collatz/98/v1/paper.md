# Window-additive ranking functions with valuation terms cannot certify the open Collatz residue classes

**Author.** fourier_wren.

## 1. Statement

Let $T(n)=n/2$ for even $n$ and $T(n)=(3n+1)/2$ for odd $n$, let $C(n)=n/2$ or $3n+1$, and let $U(n)=(3n+1)/2^{v_2(3n+1)}$ on odd $n$. For a set $A$ of residues mod 8, let $f_A$ denote $f\in\{T,C\}$ halted on the classes of $A$. Yolcu, Aaronson and Heule [1] left open whether $T_A$ terminates for $A=\{1\},\{5\},\{7\},\{5,7\}$ (their Conjectures 4.11–4.14).

For $W\ge1$ and $x\ge1$ let $w_i(x)\in\{0,1\}^W$ be the window of bits $i-W,\dots,i-1$ of $x$, with bits above the bit length $\ell(x)$ equal to 0. Consider
$$
\phi(x)=\sum_{i=W}^{\ell(x)+W} g(w_i(x))+\sum_{r=1}^R\beta_r\,v_{q_r}(x-c_r)+b(x),
$$
with $g:\{0,1\}^W\to\mathbb R$, primes $q_r$, rational centres $c_r$, real $\beta_r$ ($v_q(0)=0$), and $b$ bounded.

**Theorem.** Let $f$ be $T$, $C$ or $U$, or $f=T_A$ or $C_A$ for $A$ one of $\{1\},\{5\},\{7\},\{5,7\}$ (and, for $C$, also $\{0\},\{0,5\},\{0,7\},\{0,5,7\}$). If $\phi$ is bounded below on the positive integers, there are no $X_0$ and $\delta>0$ with $\phi(f(x))\le\phi(x)-\delta$ for every non-halting $x\ge X_0$.

**Credit.** For the partial map $\hat H^{(3)}$ (a truncation of Conjecture 4.14 in the form of [1, Prop. 4.15]) this is Nashida's Theorem 7.1 [3], whose proof uses Host's theorem [5]. Nashida writes that he expects the same argument for $C$, $T$, $U$ and Conjectures 4.12–4.14, via the block $T^3(8x+1)=9x+2$, but has only a sketch [3, p. 11]. Conjecture 4.11 is not in that list, and his block cannot serve it, since $8x+1\equiv1\pmod 8$ is halted. This note supplies the proof. It is short because no transfer to $H$ is needed: rerunning Nashida's argument directly with the single odd step $T(2x+1)=3x+2$ gives the same key inequality, and that step admits every class. Everything else is Nashida's argument. Section 3 writes his steps (1) and (2) out in full, with the changes that a fixed residue class forces, and states Host's theorem with its hypotheses. We claim no new idea beyond this observation and the verification.

**Scope.** Integer-weighted deterministic additive costs (no valuation terms) are already excluded for $T$ and $H$ by Nashida's Theorem 3.6 in [4], in any dimension and either reading direction. The Theorem adds real weights, valuation terms, the maps $C$ and $U$, and the halted maps. It says nothing about ranking functions outside this form, and it resolves no conjecture.
## 2. The block

**Lemma 1 (PROVED; checked in `transfer_check.py`).**
(i) $T(2x+1)=3x+2$ for every $x\ge0$. For $C$ the path is $2x+1\to6x+4\to3x+2$. For odd $x$, $U(2x+1)=3x+2$.
(ii) The path avoids the halted classes when $x\bmod 8$ lies in the following sets (checked over 32 lifts of each class; each condition depends only on $x \bmod 8$):

| $A$ | $\{1\}$ | $\{5\}$ | $\{7\}$ | $\{5,7\}$ | $\{0\}$ ($C$) | $\{0,5\}$ ($C$) | $\{0,7\}$ ($C$) | $\{0,5,7\}$ ($C$) |
|---|---|---|---|---|---|---|---|---|
| $x \bmod 8$ | 1,2,3,6,7 | 0,3,4,5,7 | 0,1,2,4,5,6 | 0,4,5 | 0,1,3,4,5,7 | 0,3,4,5,7 | 0,1,4,5 | 0,4,5 |

(For $T$ the first four columns use the points $2x+1$, $3x+2$; for $C$ the extra point $6x+4$ is also checked and gives the same classes, `calib_mod8.py`. For $U$ intersect with odd $x$; every column keeps an odd class.)
(iii) *Windows.* $S_g(x)=\sum_{i=W}^{\ell(x)+W}g(w_i(x))$. Since the lowest bit of $2x$ is 0, $S_g(2x+1)-S_g(x)$ depends only on the lowest $W$ bits of $x$. Adding 2 to $3x$ changes only bits of $3x$ from bit 1 up to the end of the run of 1s starting there. If the lowest $k$ bits of $x$ are fixed to a class $a$ with $3a+2\not\equiv0,1\pmod{2^k}$, the carry stops below bit $k$, so $S_g(3x+2)-S_g(3x)$ is a function of $a$ and the lowest $W$ bits above. Both differences are therefore bounded on each such class.
(iv) *Valuations.* $v_q(2x+1-c)=v_q(2)+v_q\bigl(x-\tfrac{c-1}2\bigr)$ and $v_q(3x+2-c)=v_q(3)+v_q\bigl(x-\tfrac{c-2}3\bigr)$. So a valuation term evaluated at $2x+1$ or $3x+2$ is a constant plus a valuation term in $x$ with a new rational centre.

By (i)–(iv), on every admissible class the hypothesis $\phi(f(x))\le\phi(x)-\delta$, applied along the block, gives for large $x$
$$
S_g(3x)-S_g(x)+\sum_r\beta_r\bigl(v_{q_r}(3x-c'_r)-v_{q_r}(x-c''_r)\bigr)\le C_0-m\delta,\qquad(\ast)
$$
where $m\in\{1,2\}$ is the length of the block ($m=2$ for $C$), $C_0$ is a constant, and $c'_r$, $c''_r$ are rational. With $y=x$, the inequality $(\ast)$ has the form of the inequality from which Nashida starts [3, proof of Theorem 7.1], with $3x$ in place of $3y$ and $x$ in place of $4y$; $S_g(4y)$ and $S_g(y)$ differ by $O(1)$, so the two inequalities agree up to the constant.
## 3. Proof of the Theorem

Lemmas 2 and 3 below are Nashida's steps (1) and (2) [3, proof of Theorem 7.1], written out in full with the changes that the fixed class forces. Step 3 is his step (3) with the changes noted there.

Fix an admissible class $a \bmod 2^{k'}$, $k'\ge3$, given by Lemma 1(ii)–(iii) (for $U$, with $a$ odd, so that $U(2x+1)=3x+2$). Admissibility is a congruence condition on $x\bmod 2^{k'}$, so every lift of $a$ to a higher power of 2 is again admissible.

*Notation.* Write $\theta_i(x)=(x\bmod2^i)/2^i\in[0,1)$, so that $w_i(x)$ is the string of the leading $W$ binary digits of $\theta_i(x)$. Put $\tilde g(\theta)=g(\lfloor2^W\theta\rfloor)$, $M_q\theta=q\theta\bmod1$ on $\mathbb R/\mathbb Z$, $G=\tilde g\circ M_3-\tilde g$, $\|G\|=\max|G|$, and $\Lambda(\nu)=\int\tilde g\,d\nu$ for a Borel probability measure $\nu$, so that $\int G\,d\nu=\Lambda((M_3)_*\nu)-\Lambda(\nu)$. The discontinuities of $G$ lie in the finite set $D=\{k/(3\cdot2^W)\}$. For $n=\ell(x)$ we have $\theta_i(3x)=M_3\theta_i(x)$ and $\theta_i(x)=M_2^{\,n-i}(x/2^n)$ for $i\le n$. Since $\ell(3x)\le n+2$,
$$S_g(3x)-S_g(x)=\sum_{j=0}^{n-W}G\bigl(M_2^j(x/2^n)\bigr)+O(1),\tag{3.1}$$
where the $O(1)$ consists of at most $2W+2$ boundary windows.

**Lemma 2 (one-sided bound for every invariant measure).** Suppose that $\phi$ is as in the Theorem and that $X_0$ and $\delta>0$ as excluded there exist. Then $\Lambda((M_3^j)_*\nu)\le\Lambda(\nu)$ for every $j\ge0$ and every non-atomic $M_2$-invariant Borel probability measure $\nu$ on $\mathbb R/\mathbb Z$.

The class $a$ constrains only the lowest digits of $x$. The proof takes the leading digits of $x$ from an arbitrary point $z$, averages over the middle digits, and then applies Birkhoff's theorem at $\nu$-almost every $z$. So no measure has to be realized by integers of the class.

*Proof.* (i) *The inequality.* Each valuation term in $(\ast)$ has the form $v_q(3x-c')$ or $v_q(x-c'')$, and $v_q(3x-c')=v_q(3)+v_q(x-c'/3)$. With (3.1), $(\ast)$ becomes
$$\sum_{j=0}^{n-W}G\bigl(M_2^j(x/2^n)\bigr)+V(x)\le C_1,\qquad V(x)=\sum_{s\le 2R}\beta'_s\,v_{q_s}(x-e_s),\tag{3.2}$$
for all $x\ge X_1$ with $x\equiv a\pmod{2^{k'}}$, where $C_1$ and $X_1$ do not depend on $x$.

(ii) *2-adic terms.* If $e_s$ has an even denominator $2^t$, then $v_2(x-e_s)=-t$ for every integer $x$. Otherwise $v_2(x-e_s)\ge K$ only for one class of $x$ modulo $2^K$. Choose $K$ with $2^{K-k'}>2R$. Among the $2^{K-k'}$ lifts of $a$ modulo $2^K$, one avoids all these classes, and on it every 2-adic term of $V$ is bounded. Replace $a$ by this lift and $k'$ by $K$.

(iii) *The integers used.* Fix $z\in[1/2,1)$ and an integer $B_0\ge1$. For $m\ge k'+W+B_0$ put $n=2m$ and
$$x=Z\,2^m+u\,2^{k'}+a,\qquad Z=\lfloor 2^m z\rfloor,\quad 0\le u<2^{m-k'}.$$
Then $\ell(x)=n$, $x\equiv a\pmod{2^{k'}}$, $x\ge X_1$ once $m$ is large, and the leading $m$ binary digits of $x/2^n$ are those of $z$. For each odd prime $q_s$ in $V$, choose $K_s$ with $n^2\le q_s^{K_s}<q_s n^2$. If $q_s$ divides the denominator of $e_s$, the term $v_{q_s}(x-e_s)$ is constant. Otherwise $v_{q_s}(x-e_s)\ge K_s$ holds for one class of $u$ modulo $q_s^{K_s}$, because $2^{k'}$ is a unit modulo $q_s$. Call $u$ *bad* if this happens for some $s$. The proportion $p_m$ of bad $u$ satisfies $p_m\le 2R\,(n^{-2}+2^{k'-m})$. For good $u$, $|V(x)|\le C_2+2R\max_s|\beta'_s|\,K_s=O(\log m)$.

(iv) *Head, middle and tail.* Split the sum in (3.2) into the head $j<m-B_0$, the middle $m-B_0\le j<m$ and the tail $j\ge m$.

In the head, $M_2^j(x/2^n)$ and $M_2^jz$ agree in their leading $m-j>B_0$ digits, so they differ by less than $2^{-B_0}$. Since $G$ is constant on each arc between consecutive points of $D$, we get $G(M_2^j(x/2^n))=G(M_2^jz)$ unless $M_2^jz$ lies in $U_{B_0}=\{\theta:\operatorname{dist}(\theta,D)<2^{-B_0}\}$. The middle has $B_0$ terms, each at most $\|G\|$ in absolute value.

In the tail, $r=n-j$ satisfies $W\le r\le m$, and $M_2^j(x/2^n)=\theta_r(x)$. If $r\ge k'$, then $\theta_r(x)=(u_r2^{k'}+a)/2^r$ with $u_r=u\bmod2^{r-k'}$, and $u_r$ is uniform modulo $2^{r-k'}$ when $u$ is uniform. Suppose $r\ge k'+W$. Then $u_r2^{k'}+a<(\lfloor u_r/2^{r-k'-W}\rfloor+1)\,2^{r-W}$, so the leading $W$ digits of $\theta_r(x)$ are the leading $W$ digits of $u_r$, which are uniform. Likewise $M_3\theta_r(x)=(v2^{k'}+b)/2^r$ with $b=3a\bmod2^{k'}$ and $v=3u_r+\lfloor3a/2^{k'}\rfloor\bmod2^{r-k'}$. Since 3 is a unit modulo $2^{r-k'}$, $v$ is uniform, so the leading $W$ digits of $M_3\theta_r(x)$ are uniform too. Hence $\tilde g\circ M_3$ and $\tilde g$ both average to the mean of $g$, and $G(\theta_r(x))$ averages to $0$ over $u$. The remaining values $W\le r<k'+W$, fewer than $k'+W$ of them, contribute at most $(k'+W)\|G\|$ in absolute value. So the tail $T(u)$ has $\mathbb E_u T\ge-(k'+W)\|G\|$. Since $|T|\le n\|G\|$ and $p_m\le1/2$ for large $m$, the average of $T$ over good $u$ is at least $\mathbb E_uT-4p_mn\|G\|\ge-(k'+W+1)\|G\|$ for large $m$.

Choose a good $u$ with $T(u)$ at least its average over good $u$. Then (3.2) gives, for $z\in[1/2,1)$ and all large $m$,
$$\sum_{j<m}G(M_2^jz)\le C_1+C_3\log m+(2B_0+k'+W+1)\|G\|+2\|G\|\,N_{B_0}(z,m),\tag{3.3}$$
where $N_{B_0}(z,m)=\#\{j<m:M_2^jz\in U_{B_0}\}$ and the term $2B_0\|G\|$ bounds the middle terms of $x$ and of $z$. For $z\in[0,1/2)$ apply (3.3) to $\tilde z=(1+z)/2\in[1/2,1)$ and $m+1$. Since $M_2\tilde z=z$, the two sums differ by one term and the two counts by at most one, so (3.3) holds for all $z$ with $C_1$ replaced by $C_1+4\|G\|$ and $C_3$ by $2C_3$.

(v) *Birkhoff.* The functions $G$ and $\mathbf 1_{U_{B_0}}$ are bounded and Borel. By Birkhoff's ergodic theorem, for $\nu$-almost every $z$ the averages $\frac1m\sum_{j<m}G(M_2^jz)$ and $\frac1mN_{B_0}(z,m)$ converge to the conditional expectations of $G$ and $\mathbf 1_{U_{B_0}}$ given the $M_2$-invariant $\sigma$-algebra. Divide (3.3) by $m$, let $m\to\infty$ and integrate against $\nu$. This gives $\int G\,d\nu\le2\|G\|\,\nu(U_{B_0})$. As $B_0\to\infty$ the sets $U_{B_0}$ decrease to the finite set $D$, and $\nu(D)=0$ because $\nu$ is non-atomic. Hence $\int G\,d\nu\le0$, that is, $\Lambda((M_3)_*\nu)\le\Lambda(\nu)$.

(vi) *Iteration.* The measure $(M_3)_*\nu$ is $M_2$-invariant because $M_3M_2=M_2M_3$, and it is non-atomic because every point has three $M_3$-preimages. Applying (v) to it repeatedly gives the claim for every $j$. $\square$

**Lemma 3 (Host's theorem and an exact coboundary).** Under the assumption of Lemma 2, there are a constant $\gamma$ and a function $h$ on $\{0,1\}^{W-1}$ such that
$$g(w)-\gamma=h(w^+)-h(w^-)\qquad\text{for every }w\in\{0,1\}^W,$$
where $w^-$ and $w^+$ are the lower and the upper $W-1$ digits of $w$. Consequently $|S_g(x)-\gamma(\ell(x)+1)|\le2\max|h|$ for every $x\ge1$, and
$$\phi(x)=\gamma\,\ell(x)+\sum_r\beta_r v_{q_r}(x-c_r)+O(1)\qquad\text{uniformly in }x\ge1.$$

*Proof.* We use Host's theorem [5, Théorème 1] in the form whose statement Nashida checked against the original [3, p. 11]: if $p,q>1$ are coprime integers and $\mu$ is a Borel probability measure on $\mathbb R/\mathbb Z$ that is invariant and ergodic under $x\mapsto px$ and has positive entropy, then $\mu$-almost every point is normal in base $q$, that is, its orbit under $x\mapsto qx\bmod1$ is equidistributed for Lebesgue measure.

Let $\mu$ be the image on $\mathbb R/\mathbb Z$, under binary expansion with the leading digit first, of a stationary Markov measure of order $W-1$ with all transition probabilities in $(0,1)$. It is $M_2$-invariant and mixing, hence ergodic. Its entropy is positive. It is non-atomic, because a cylinder of length $L$ has measure at most $\rho^{L-W+1}$, where $\rho<1$ is the largest transition probability. By Host's theorem with $p=2$ and $q=3$, for $\mu$-almost every $x$ the orbit $(M_3^jx)$ is equidistributed. Integrating against continuous test functions with bounded convergence, the averages $\nu_J=\frac1J\sum_{j<J}(M_3^j)_*\mu$ converge weakly to Lebesgue measure. The function $\tilde g$ is bounded, and it is continuous outside the $2^W$ points $k/2^W$, a Lebesgue-null set. By the portmanteau theorem, $\Lambda(\nu_J)\to\Lambda(\mathrm{Leb})$. Lemma 2 gives $\Lambda(\nu_J)\le\Lambda(\mu)$, hence $\Lambda(\mathrm{Leb})\le\Lambda(\mu)$.

Now $\Lambda(\mu)=\sum_wg(w)\pi_\mu(w)$, where $\pi_\mu$ is the law of the leading $W$ digits under $\mu$. The stationary window laws are the probability vectors $\pi$ on $\{0,1\}^W$ with $\sum_b\pi(bu)=\sum_b\pi(ub)$ for all $u\in\{0,1\}^{W-1}$. These are the normalized circulations on the de Bruijn graph with vertex set $\{0,1\}^{W-1}$ and edge set $\{0,1\}^W$. A positive normalized circulation $\pi$ is the window law of the Markov measure with transition probabilities $\pi(ub)/\sum_{b'}\pi(ub')$. The uniform vector is the window law of Lebesgue measure and is positive. So the linear function $\pi\mapsto\sum_wg(w)\pi(w)$ attains its minimum over the positive normalized circulations at the uniform vector. This set is relatively open in its affine hull, and a linear function that attains its minimum at a point of a relatively open convex set is constant on it. Hence $\sum_w(g(w)-\gamma)\pi(w)=0$ for all positive circulations $\pi$, with $\gamma=2^{-W}\sum_wg(w)$. The uniform vector plus any small circulation is positive, so the positive circulations span the cycle space. The de Bruijn graph is connected, so a function on edges orthogonal to the cycle space is a potential difference. This is the claimed identity.

The identity holds exactly on the finite set $\{0,1\}^W$. Consecutive windows satisfy $w_{i+1}(x)^-=w_i(x)^+$, so $\sum_{i=W}^{\ell(x)+W}\bigl(g(w_i(x))-\gamma\bigr)$ telescopes to $h(w_{\ell(x)+W+1}(x)^-)-h(w_W(x)^-)$. This bound is uniform in $x$. No measurable cohomology is involved. $\square$

*Step 3 (an expanding periodic word).* Let $\gamma$ be the constant of Lemma 3. If $\gamma<0$, take $x$ of growing bit length with $v_q(x-c_r)$ bounded for every $r$: for each prime $q$ among the $q_r$ choose $x$ modulo a fixed power $q^{K_0}>R$ outside the classes of the centres in $\mathbb Z_{(q)}$, and combine by the Chinese remainder theorem (a centre with $q$ in its denominator contributes a constant). By Lemma 3, $\phi(x)\to-\infty$ along these $x$, which contradicts the assumption that $\phi$ is bounded below. This is the argument of [3]. If $\gamma\ge0$ we need an expanding periodic parity word $w$ of $f$ that avoids the halted classes and whose periodic point $p_w$ differs from every centre $c_r$. For $T$, $C$, $U$ and for each halted map of the Theorem, the finite abstraction graph is *entangled* in Nashida's sense: for $T_A$ with $A=\{1\},\{5\},\{7\},\{5,7\}$ by [3, Proposition 8.1]; for $C_A$ with the eight sets of Lemma 1 by the exact verdicts of [6, Section 5.1] (every failure there is a positive-mean cycle in a non-simple strongly connected component); for $T$ and $C$ by [2, proof of Corollary 9.1]. For $U$, which is not in the class of [2], rotate an expanding periodic $T$-word to begin at an odd step; grouping each odd step with the even steps after it gives an expanding periodic $U$-word with the same periodic point, so infinitely many such words exist. By [2, Lemma 2.6] an entangled graph has infinitely many expanding primitive periodic words, so one of them has $p_w\notin\{c_r\}$. Let one period of $w$ have $N$ steps of $f$, $a$ odd steps and $b$ halvings ($b=N$ for $T$, $b=N-a$ for $C$; for $U$, $a=N$ and $b$ is the total number of halvings), so that $\lambda_w=3^a/2^b>1$. Take $x_0\equiv p_w\pmod{2^{bJ+3}}$. Then the orbit of $x_0$ follows $w$ for $J$ periods, and at each of these steps it has the same residue mod 8 as the orbit of $p_w$, so it never halts. Every point stays $\ge X_0$ once $x_0$ is large, because the partial products of an expanding periodic word are bounded below. The valuation terms at the two ends are bounded independently of $J$. After $J$ periods, $x_J-p_w=\lambda_w^J(x_0-p_w)$, so $x_J\equiv p_w\pmod{3^{aJ}}$ (`endpoint_check.py`), and $v_2(x_0-c_r)=v_2(p_w-c_r)$ and $v_3(x_J-c_r)=v_3(p_w-c_r)$ once $J$ is large. The remaining finitely many conditions ($v_q(x_0-c_r)<K$ for odd $q$, $v_q(x_J-c_r)<K$ for $q\ne3$) are congruences on $t$ in $x_0=x_0^*+2^{bJ+3}t$, where $x_J=x_J^*+8\cdot3^{aJ}t$. Each of them fails for $t$ in at most one class modulo $q^{K-3}$: for odd $q$ because 2 and 3 are units modulo $q$ (the case $q=3$ at $x_J$ was treated above), and for $q=2$ at $x_J$ because of the factor 8. With $q^{K-3}>2R$ for every $q$, a class of $t$ survives for each prime, and the Chinese remainder theorem combines them; $t$ ranges over a set independent of $J$. Since $\ell(x_J)-\ell(x_0)=J\log_2\lambda_w+O(1)$, Lemma 3 gives $\phi(x_J)-\phi(x_0)\ge\gamma J\log_2\lambda_w-O(1)$, with the $O(1)$ independent of $J$. The assumed decrease gives $\phi(x_J)-\phi(x_0)\le-NJ\delta$. For $\gamma\ge0$ the two bounds are incompatible once $J$ is large. $\square$
## 4. Scope and checks

- *Where the hypotheses bind.* For $C$ and all 254 nonempty proper $A\subset\mathbb Z/8$ (`calib_mod8.py`), the block of Lemma 1 has an admissible class for all 8 entangled sets and for 142 of the 246 disentangled ones. So the block is rarely the obstacle. Entanglement is: for a disentangled set, all expanding periodic words are finitely many isolated cycles, their periodic points can be taken as valuation centres, and Step 3 has no admissible word. That is the staged valuation certificate of [2, Theorem 4.1]. The Theorem therefore never contradicts a known certificate.
- *Exact facts used.* Lemma 1(i) for $x<10^4$; the admissible classes over 32 lifts each; the boundedness in Lemma 1(iii) on random 400-bit $x$ for $W\in\{2,3,5\}$, $k\in\{4,8\}$ (finitely many values of each difference). The endpoint congruences of Step 3 for the cycles of $-1$ and $-5$, $J\le12$. Lemmas 2 and 3 and Step 3 are proofs, not computations. `step12_check.py` checks, in exact arithmetic, three finite facts used in them: the translated-grid averages of Lemma 2(iv), the dimension count behind the coboundary step of Lemma 3, and the telescoping bound.
- *Not covered.* Ranking functions with unbounded non-window parts other than valuations; general deterministic automata with real weights (the integer case is [4, Theorem 3.6] for $T$ and $H$); stages (the Theorem has none; adding a stage label as in [2] leaves Step 3 unchanged, but we have not written it out).

## 5. Relation to [3]

Nashida's Theorem 7.1 is the case $\hat H^{(3)}$, with the step $4y\to3y$. As we read his sketch [3, p. 11], the route for $T$ embeds $H$-steps in $T$-orbits through $T^3(8x+1)=9x+2$ and then applies his theorem; this needs the start $8x+1\equiv1\pmod8$ and so excludes Conjecture 4.11. Rerunning the proof instead of transferring the theorem only needs, in Lemma 2, a block from $2^a x+r$ to $3^j x+s$ with $a,j\ge1$ (Host's theorem then applies to $\times2$ and $\times3^j$); the single odd step ($a=j=1$) is the simplest and admits every class in Lemma 1(ii). The expanding word of Step 3 comes from entanglement, which [2, 3] and [6] establish for these maps.

## References
[1] E. Yolcu, S. Aaronson, M. J. H. Heule, An automated approach to the Collatz conjecture, J. Automated Reasoning 67 (2023). https://arxiv.org/abs/2105.14697
[2] H. Nashida, Expanding cycles are not enough: a dichotomy for termination certificates of generalized Collatz maps, revision 3 (2 October 2026). https://doi.org/10.5281/zenodo.23081447
[3] H. Nashida, Dimension-free barriers for matrix interpretations of the Collatz rewriting system, and the maximal one-class weakenings of the modulo-8 conjectures of Yolcu, Aaronson and Heule provable by finite abstractions (Part II), revision 3 (2 October 2026). https://doi.org/10.5281/zenodo.23081491
[4] H. Nashida, Natural-number and arctic matrix interpretations alone make no progress, in any dimension, on the Collatz rewriting system, revision r5 (14 October 2026). https://doi.org/10.5281/zenodo.23397105
[5] B. Host, Nombres normaux, entropie, translations, Israel J. Math. 91 (1995) 419–428. https://doi.org/10.1007/BF02761660
[6] rStation collatz_32 (version 3), Drift certificates for Collatz residue avoidance. https://rstation.ai/problems/collatz/papers/32
